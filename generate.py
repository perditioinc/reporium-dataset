"""Generate README.md from live reporium-db data files."""

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

BASE_RAW_URL = "https://raw.githubusercontent.com/perditioinc/reporium-db/main/data"
TIMEOUT = 15
FORK_TABLE_LIMIT = 100  # cap forked-repo table to avoid README cut-off


async def _fetch_json(url: str, token: str) -> Optional[dict[str, Any] | list]:
    """Fetch a JSON file from a raw GitHub URL.

    Returns None on any error (graceful degradation).
    """
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            resp = await client.get(url, headers=headers)
            resp.raise_for_status()
            return resp.json()
    except Exception as exc:  # noqa: BLE001
        logger.warning("Could not fetch %s: %s", url, exc)
        return None


def _freshness_label(last_updated: Optional[str]) -> str:
    """Return a human-readable freshness label for the dataset."""
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


def _top_stars_table(top_starred: list[dict]) -> str:
    """Format the top-starred repos as a markdown table."""
    if not top_starred:
        return "_No data available_"
    rows = ["| Repo | Stars | Language |", "|------|-------|----------|"]
    for repo in top_starred[:10]:
        name = repo.get("nameWithOwner", "")
        stars = f"{repo.get('stars', 0):,}"
        lang = repo.get("primaryLanguage") or "—"
        url = f"https://github.com/{name}"
        rows.append(f"| [{name}]({url}) | {stars} | {lang} |")
    return "\n".join(rows)


def _lang_list(languages: dict[str, int]) -> str:
    """Format top 10 languages as a markdown list."""
    items = list(languages.items())[:10]
    return "\n".join(f"- **{lang}**: {count:,} repos" for lang, count in items)


def _personal_repos_table(repos: list[dict]) -> str:
    """Table of personal (non-fork) repos sorted by stars."""
    if not repos:
        return "_No personal repos found_"
    sorted_repos = sorted(repos, key=lambda r: r.get("stars", 0), reverse=True)
    rows = [
        "| Repo | Description | Stars | Language | Last Active |",
        "|------|-------------|------:|----------|-------------|",
    ]
    for repo in sorted_repos:
        name = repo.get("nameWithOwner", "")
        short = name.split("/", 1)[-1]
        stars = f"{repo.get('stars', 0):,}"
        lang = repo.get("primaryLanguage") or "—"
        desc = (repo.get("description") or "—").replace("|", "-")
        pushed = (repo.get("pushedAt") or "")[:10] or "—"
        url = f"https://github.com/{name}"
        rows.append(f"| [{short}]({url}) | {desc} | {stars} | {lang} | {pushed} |")
    return "\n".join(rows)


def _forked_repos_table(repos: list[dict], limit: int = FORK_TABLE_LIMIT) -> str:
    """Table of forked repos, sorted by upstream stars (or pushedAt), capped at limit."""
    if not repos:
        return "_No forked repos found_"

    has_parent_stars = any(r.get("parentStars") for r in repos)
    if has_parent_stars:
        sorted_repos = sorted(repos, key=lambda r: r.get("parentStars") or 0, reverse=True)
    else:
        sorted_repos = sorted(repos, key=lambda r: r.get("pushedAt") or "", reverse=True)

    shown = sorted_repos[:limit]
    rows = [
        "| Fork | Upstream Repo | Upstream ⭐ | Language | Description |",
        "|------|--------------|------------:|----------|-------------|",
    ]
    for repo in shown:
        name = repo.get("nameWithOwner", "")
        short = name.split("/", 1)[-1]
        lang = repo.get("primaryLanguage") or "—"
        raw_desc = (repo.get("description") or "—").replace("|", "-")
        desc = raw_desc[:80] + ("…" if len(raw_desc) > 80 else "")
        fork_url = f"https://github.com/{name}"

        parent = repo.get("parentRepo")
        parent_stars = repo.get("parentStars")
        if parent:
            parent_url = f"https://github.com/{parent}"
            parent_cell = f"[{parent}]({parent_url})"
            stars_cell = f"{parent_stars:,}" if parent_stars else "—"
        else:
            parent_cell = "—"
            stars_cell = "—"

        rows.append(f"| [{short}]({fork_url}) | {parent_cell} | {stars_cell} | {lang} | {desc} |")
    return "\n".join(rows)


def build_readme(
    index: Optional[dict],
    recent: Optional[list],
    top_starred: Optional[list],
    all_repos: Optional[list] = None,
) -> str:
    """Build README.md content from fetched data with graceful degradation."""
    if index is None:
        meta: dict = {}
        languages: dict = {}
        degraded = True
    else:
        meta = index.get("meta", {})
        languages = index.get("languages", {})\

        degraded = False

    total = meta.get("total", 0)
    last_updated = meta.get("last_updated")
    freshness = _freshness_label(last_updated)

    stars_table = _top_stars_table(top_starred or [])
    lang_section = _lang_list(languages) if languages else "_No language data available_"

    if all_repos is None:
        personal_section = "_Personal repos data unavailable_"
        forked_section = "_Forked repos data unavailable_"
        personal_count = 0
        forked_count = 0
        forked_note = ""
    else:
        personal = [r for r in all_repos if not r.get("isFork")]
        forked = [r for r in all_repos if r.get("isFork")]
        personal_count = len(personal)
        forked_count = len(forked)
        personal_section = _personal_repos_table(personal)
        forked_section = _forked_repos_table(forked)
        shown = min(FORK_TABLE_LIMIT, forked_count)
        if forked_count > 0:
            sort_note = "by upstream stars" if any(r.get("parentStars") for r in forked) else "by last activity"
            forked_note = (
                f"\n> Showing top {shown:,} of {forked_count:,} forked repos ({sort_note})."
                f" Full dataset: [`data/full/repos_0000.json`]"
                f"(https://github.com/perditioinc/reporium-db/blob/main/data/full/repos_0000.json)\n"
            )
        else:
            forked_note = ""

    degraded_note = (
        "\n> **Note:** Source data is temporarily unavailable. Showing cached info.\n"
        if degraded
        else ""
    )

    return f"""# Reporium Dataset

> Open dataset of AI development tool repositories tracked on GitHub — updated nightly.
> Powering [reporium.com](https://reporium.com).
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

Data is fetched nightly from GitHub via GraphQL and written to partitioned JSON files
in [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db).

## Perditio Projects

{personal_count:,} repositories built and maintained by Perditio.

{personal_section}

## Forked AI Repos
{forked_note}
{forked_section}

## Top Repos by Stars

Upstream repos with the most stars, tracked in this dataset.

{stars_table}

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

## Data Files

| File | Description |
|------|-------------|
| `data/index.json` | Counts + metadata (tiny, always fast) |
| `data/recent.json` | Repos pushed in last 7 days (max 500) |
| `data/top_starred.json` | Top 100 by stars |
| `data/by_language/*.json` | One file per language |
| `data/by_category/*.json` | One file per category/topic _(empty until ingestion runs)_ |
| `data/full/repos_NNNN.json` | Full dataset, up to 10K repos per file |

## Platform

This dataset powers [reporium.com](https://reporium.com) — search and discovery for AI development tools.

Source data: [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db)

## License

Data is sourced from the GitHub API. MIT license.
"""


async def main() -> None:
    """Fetch data from reporium-db and regenerate README.md."""
    import asyncio

    t0 = time.monotonic()
    token = os.getenv("GH_TOKEN", "")

    index, recent, top_starred, all_repos = await asyncio.gather(
        _fetch_json(f"{BASE_RAW_URL}/index.json", token),
        _fetch_json(f"{BASE_RAW_URL}/recent.json", token),
        _fetch_json(f"{BASE_RAW_URL}/top_starred.json", token),
        _fetch_json(f"{BASE_RAW_URL}/full/repos_0000.json", token),
    )

    readme = build_readme(index, recent, top_starred, all_repos)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    elapsed = time.monotonic() - t0
    total = (index or {}).get("meta", {}).get("total", 0)
    logger.info("README generated in %.2fs - %d repos", elapsed, total)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
