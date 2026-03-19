"""Generate README.md from reporium-api data."""

from __future__ import annotations

import logging
import os
import time
from datetime import datetime, timezone
from typing import Any, Optional

import httpx
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

REPORIUM_API_URL = os.getenv("REPORIUM_API_URL", "")
TIMEOUT = 15
FORK_TABLE_LIMIT = 100


# ── API fetching ───────────────────────────────────────────────────────────────


async def _api_get(
    client: httpx.AsyncClient,
    api_url: str,
    path: str,
    **params: Any,
) -> Optional[Any]:
    """GET a single reporium-api endpoint. Returns parsed JSON or None on error."""
    try:
        resp = await client.get(f"{api_url}{path}", params=params)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:  # noqa: BLE001
        logger.warning("API %s failed: %s", path, exc)
        return None


async def _fetch_all_repos(api_url: str) -> Optional[list[dict]]:
    """Paginate through /repos?sort=stars to get all repos. Returns None on failure."""
    if not api_url:
        return None
    all_repos: list[dict] = []
    page = 1
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        while True:
            data = await _api_get(client, api_url, "/repos", sort="stars", limit=200, page=page)
            if data is None:
                return None if not all_repos else all_repos
            batch = data.get("repos", [])
            if not batch:
                break
            all_repos.extend(batch)
            if len(batch) < 200:
                break
            page += 1
    return all_repos


async def _fetch_stats(api_url: str) -> Optional[dict]:
    """Fetch summary stats from /library. Returns None on failure."""
    if not api_url:
        return None
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        data = await _api_get(client, api_url, "/library", limit=1)
        if data:
            return data.get("stats")
    return None


# ── Formatting helpers ─────────────────────────────────────────────────────────


def _freshness_label(last_updated: Optional[str]) -> str:
    """Return a human-readable freshness label for a dataset timestamp."""
    if not last_updated:
        return "Update time unknown"
    try:
        updated = datetime.fromisoformat(last_updated.replace("Z", "+00:00"))
        delta = datetime.now(timezone.utc) - updated
        hours = delta.total_seconds() / 3600
        if hours < 1:
            return "Updated less than 1h ago"
        if hours < 24:
            return f"Updated {int(hours)}h ago"
        return f"Updated {delta.days}d ago"
    except ValueError:
        return "Update time unknown"


def _top_stars_table(repos: list[dict]) -> str:
    """Top 10 forked repos by upstream star count."""
    forks = [r for r in repos if r.get("is_fork") and r.get("parent_stars")]
    top = sorted(forks, key=lambda r: r.get("parent_stars") or 0, reverse=True)[:10]
    if not top:
        return "_No data available_"
    rows = ["| Fork | Upstream Stars | Language |", "|------|---------------:|----------|"]
    for repo in top:
        owner = repo.get("owner", "")
        name = repo.get("name", "")
        full_name = f"{owner}/{name}"
        stars = f"{repo.get('parent_stars', 0):,}"
        lang = repo.get("primary_language") or "—"
        url = repo.get("github_url") or f"https://github.com/{full_name}"
        rows.append(f"| [{full_name}]({url}) | {stars} | {lang} |")
    return "\n".join(rows)


def _lang_list(languages: dict[str, int]) -> str:
    """Top 10 languages as a markdown bullet list."""
    items = list(languages.items())[:10]
    return "\n".join(f"- **{lang}**: {count:,} repos" for lang, count in items)


def _personal_repos_table(repos: list[dict]) -> str:
    """Table of personal (non-fork) repos."""
    if not repos:
        return "_No personal repos found_"
    rows = [
        "| Repo | Description | Language | Last Active |",
        "|------|-------------|----------|-------------|",
    ]
    for repo in repos:
        owner = repo.get("owner", "")
        name = repo.get("name", "")
        full_name = f"{owner}/{name}"
        lang = repo.get("primary_language") or "—"
        desc = (repo.get("description") or "—").replace("|", "-")[:80]
        pushed = (repo.get("your_last_push_at") or repo.get("updated_at") or "")[:10] or "—"
        url = repo.get("github_url") or f"https://github.com/{full_name}"
        rows.append(f"| [{full_name}]({url}) | {desc} | {lang} | {pushed} |")
    return "\n".join(rows)


def _fork_display(owner: str, name: str, max_len: int = 35) -> str:
    """Return owner/name truncated to max_len chars."""
    full = f"{owner}/{name}"
    if len(full) <= max_len:
        return full
    return full[: max_len - 1] + "…"


def _forked_repos_table(repos: list[dict], limit: int = FORK_TABLE_LIMIT) -> str:
    """Table of forked repos sorted by upstream stars, capped at limit.

    Columns: Fork (owner/name truncated) | Forked From (upstream owner) |
             Stars | Forks | Language | Description
    """
    if not repos:
        return "_No forked repos found_"

    sorted_repos = sorted(repos, key=lambda r: r.get("parent_stars") or 0, reverse=True)
    shown = sorted_repos[:limit]

    rows = [
        "| Fork | Forked From | Stars | Forks | Language | Description |",
        "|------|------------|------:|------:|----------|-------------|",
    ]
    for repo in shown:
        owner = repo.get("owner", "")
        name = repo.get("name", "")
        display = _fork_display(owner, name)
        url = repo.get("github_url") or f"https://github.com/{owner}/{name}"
        fork_cell = f"[{display}]({url})"

        forked_from = repo.get("forked_from") or ""
        if forked_from:
            upstream_owner = forked_from.split("/")[0]
            forked_from_cell = f"[{upstream_owner}](https://github.com/{upstream_owner})"
        else:
            forked_from_cell = "—"

        parent_stars = repo.get("parent_stars")
        stars_cell = f"{parent_stars:,}" if parent_stars else "—"

        parent_forks = repo.get("parent_forks")
        forks_cell = f"{parent_forks:,}" if parent_forks is not None else "—"

        lang = repo.get("primary_language") or "—"
        raw_desc = (repo.get("description") or "—").replace("|", "-")
        desc = raw_desc[:70] + ("…" if len(raw_desc) > 70 else "")

        rows.append(
            f"| {fork_cell} | {forked_from_cell} | {stars_cell} | {forks_cell} | {lang} | {desc} |"
        )
    return "\n".join(rows)


# ── README builder ─────────────────────────────────────────────────────────────


def build_readme(
    stats: Optional[dict],
    repos: Optional[list],
) -> str:
    """Build README.md content from reporium-api data with graceful degradation.

    Args:
        stats: Dict from /library stats endpoint (total_repos, languages, etc.) or None.
        repos: List of repo dicts from /repos endpoint or None.

    Returns:
        Markdown string for README.md.
    """
    degraded = stats is None

    total = (stats or {}).get("total_repos", 0)
    languages: dict = (stats or {}).get("languages", {})
    last_updated = (stats or {}).get("last_updated")
    freshness = _freshness_label(last_updated)

    if repos is None:
        personal_section = "_Personal repos data unavailable_"
        forked_section = "_Forked repos data unavailable_"
        personal_count = 0
        forked_count = 0
        forked_note = ""
        top_stars = "_No data available_"
    else:
        personal = [r for r in repos if not r.get("is_fork")]
        forked = [r for r in repos if r.get("is_fork")]
        personal_count = len(personal)
        forked_count = len(forked)
        personal_section = _personal_repos_table(personal)
        forked_section = _forked_repos_table(forked)
        top_stars = _top_stars_table(repos)
        shown = min(FORK_TABLE_LIMIT, forked_count)
        if forked_count > 0:
            sort_note = "by upstream stars" if any(r.get("parent_stars") for r in forked) else "by last activity"
            forked_note = (
                f"\n> Showing top {shown:,} of {forked_count:,} forked repos ({sort_note})."
                f" Full dataset available via [reporium-api](https://github.com/perditioinc/reporium-api).\n"
            )
        else:
            forked_note = ""

    lang_section = _lang_list(languages) if languages else "_No language data available_"

    degraded_note = (
        "\n> **Note:** reporium-api is unavailable. Data will appear once the API is deployed.\n"
        if degraded
        else ""
    )

    return f"""# Reporium Dataset

> Open dataset of AI development tool repositories — updated nightly from [reporium-api](https://github.com/perditioinc/reporium-api).
{degraded_note}
[![Updated nightly](https://img.shields.io/badge/updated-nightly-blue)](https://github.com/perditioinc/reporium-db)
[![Repos tracked](https://img.shields.io/badge/repos-{total:,}-green)](https://reporium.com)

## Overview

| Stat | Value |
|------|------:|
| Total repos | {total:,} |
| Perditio projects | {personal_count:,} |
| Forked AI repos | {forked_count:,} |
| Languages tracked | {len(languages):,} |
| AI categories enriched | 0 _(ingestion pipeline not yet running)_ |
| Last updated | {freshness} |

## Perditio Projects

{personal_count:,} repositories built and maintained by Perditio.

{personal_section}

## Forked AI Repos
{forked_note}
{forked_section}

## Top Repos by Stars

{top_stars}

## Top Languages

{lang_section}

## Status

| Component | Status |
|-----------|--------|
| Repo tracking | Active — {total:,} repos, nightly sync |
| Language breakdown | Active — {len(languages):,} languages tracked |
| AI enrichment categories | Not yet active — ingestion pipeline not running |
| README summaries | Not yet active — ingestion pipeline not running |

> AI enrichment (Agents, LLM Serving, RAG, Fine-tuning, Observability, etc.) will be populated
> once the reporium-ingestion pipeline is deployed.

## Data Access

Data is served via the [reporium-api](https://github.com/perditioinc/reporium-api):

| Endpoint | Description |
|----------|-------------|
| `GET /repos?sort=stars` | All repos sorted by upstream stars |
| `GET /repos?is_fork=false` | Personal projects only |
| `GET /repos?is_fork=true` | Forked repos only |
| `GET /library` | Stats, language breakdown, categories |
| `GET /repos/{{name}}` | Single repo detail |

## Platform

This dataset powers [reporium.com](https://reporium.com) — search and discovery for AI development tools.

Source: [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db) |
API: [perditioinc/reporium-api](https://github.com/perditioinc/reporium-api)

## License

Data is sourced from the GitHub API. MIT license.
"""


# ── Entry point ────────────────────────────────────────────────────────────────


async def main() -> None:
    """Fetch data from reporium-api and regenerate README.md."""
    import asyncio

    t0 = time.monotonic()
    api_url = REPORIUM_API_URL
    if not api_url:
        logger.warning("REPORIUM_API_URL not set — README will show degraded state")

    stats, repos = await asyncio.gather(
        _fetch_stats(api_url),
        _fetch_all_repos(api_url),
    )

    readme = build_readme(stats, repos)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    total = (stats or {}).get("total_repos", 0)
    elapsed = time.monotonic() - t0
    logger.info("README generated in %.2fs - %d repos", elapsed, total)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
