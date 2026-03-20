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


def _truncate(text: str, max_len: int) -> str:
    """Truncate text at a word boundary to fit table columns on desktop."""
    if len(text) <= max_len:
        return text
    cut = text[:max_len].rsplit(" ", 1)[0]
    return cut + "…"


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
        desc = _truncate((repo.get("description") or "—").replace("|", "-"), 60)
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


def _forked_repos_table(repos: list[dict]) -> str:
    """Table of all forked repos sorted by upstream stars.

    Fork column shows only the parent URL.
    """
    if not repos:
        return "_No forked repos found_"

    sorted_repos = sorted(repos, key=lambda r: r.get("parent_stars") or 0, reverse=True)

    rows = [
        "| Fork | Stars | Forks | Language | Description |",
        "|------|------:|------:|----------|-------------|",
    ]
    for repo in sorted_repos:
        forked_from = repo.get("forked_from") or ""
        if forked_from:
            parent_url = f"https://github.com/{forked_from}"
            fork_cell = f"[{forked_from}]({parent_url})"
        else:
            owner = repo.get("owner", "")
            name = repo.get("name", "")
            fork_url = repo.get("github_url") or f"https://github.com/{owner}/{name}"
            fork_cell = f"[{owner}/{name}]({fork_url})"

        parent_stars = repo.get("parent_stars")
        stars_cell = f"{parent_stars:,}" if parent_stars else "—"

        parent_forks = repo.get("parent_forks")
        forks_cell = f"{parent_forks:,}" if parent_forks is not None else "—"

        lang = repo.get("primary_language") or "—"
        desc = _truncate((repo.get("description") or "—").replace("|", "-"), 55)

        rows.append(f"| {fork_cell} | {stars_cell} | {forks_cell} | {lang} | {desc} |")
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
        forked_note = ""

    lang_section = _lang_list(languages) if languages else "_No language data available_"

    degraded_note = (
        "\n> **Note:** reporium-api is unavailable. Data will appear once the API is deployed.\n"
        if degraded
        else ""
    )

    return f"""# Reporium Dataset
<!-- perditio-badges-start -->
[![Tests](https://github.com/perditioinc/reporium-dataset/actions/workflows/update.yml/badge.svg)](https://github.com/perditioinc/reporium-dataset/actions/workflows/update.yml)
![Last Commit](https://img.shields.io/github/last-commit/perditioinc/reporium-dataset)
![License](https://img.shields.io/github/license/perditioinc/reporium-dataset)
![python](https://img.shields.io/badge/python-3.11%2B-3776ab)
![suite](https://img.shields.io/badge/suite-Reporium-6e40c9)
![repos](https://img.shields.io/badge/repos-826-blue)
![updated](https://img.shields.io/badge/updated-nightly-blue)
<!-- perditio-badges-end -->

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


# ── Fallback: reporium-db raw files ───────────────────────────────────────────

_DB_RAW_BASE = "https://raw.githubusercontent.com/perditioinc/reporium-db/main/data"


async def _db_get(url: str, token: str) -> Optional[Any]:
    """Fetch a raw file from reporium-db. Returns parsed JSON or None."""
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            resp = await client.get(url, headers=headers)
            resp.raise_for_status()
            return resp.json()
    except Exception as exc:  # noqa: BLE001
        logger.warning("DB fallback fetch %s failed: %s", url, exc)
        return None


async def _fetch_fallback(token: str) -> tuple[Optional[dict], Optional[list]]:
    """Fallback: read stats and repos from reporium-db raw files.

    Converts reporium-db schema to the same shape build_readme expects.
    Used when REPORIUM_API_URL is not configured.
    """
    import asyncio

    index, raw_repos = await asyncio.gather(
        _db_get(f"{_DB_RAW_BASE}/index.json", token),
        _db_get(f"{_DB_RAW_BASE}/full/repos_0000.json", token),
    )

    stats: Optional[dict] = None
    if index:
        meta = index.get("meta", {})
        stats = {
            "total_repos": meta.get("total", 0),
            "languages": index.get("languages", {}),
            "last_updated": meta.get("last_updated"),
        }

    repos: Optional[list] = None
    if raw_repos:
        repos = []
        for r in raw_repos:
            nwo = r.get("nameWithOwner", "")
            parts = nwo.split("/", 1)
            owner = parts[0] if len(parts) == 2 else ""
            name = parts[1] if len(parts) == 2 else nwo
            repos.append({
                "name": name,
                "owner": owner,
                "description": r.get("description"),
                "is_fork": r.get("isFork", False),
                "forked_from": r.get("parentRepo"),
                "primary_language": r.get("primaryLanguage"),
                "github_url": f"https://github.com/{nwo}",
                "parent_stars": r.get("parentStars"),
                "parent_forks": r.get("parentForks"),
                "your_last_push_at": r.get("pushedAt"),
                "updated_at": r.get("updatedAt"),
            })
        if stats:
            forks = sum(1 for r in repos if r.get("is_fork"))
            stats["total_forks"] = forks
            stats["total_non_forks"] = len(repos) - forks

    return stats, repos


# ── Entry point ────────────────────────────────────────────────────────────────


async def main() -> None:
    """Fetch data and regenerate README.md.

    Tries reporium-api first; falls back to reporium-db raw files if the
    API URL is not configured or the request fails.
    """
    import asyncio

    t0 = time.monotonic()
    api_url = REPORIUM_API_URL

    stats, repos = await asyncio.gather(
        _fetch_stats(api_url),
        _fetch_all_repos(api_url),
    )

    if stats is None or repos is None:
        token = os.getenv("GH_TOKEN", "")
        logger.info("API unavailable — falling back to reporium-db raw files")
        stats, repos = await _fetch_fallback(token)

    readme = build_readme(stats, repos)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    total = (stats or {}).get("total_repos", 0)
    elapsed = time.monotonic() - t0
    logger.info("README generated in %.2fs - %d repos", elapsed, total)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
