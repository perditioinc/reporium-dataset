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


async def _fetch_json(url: str, token: str) -> Optional[dict[str, Any]]:
    """Fetch a JSON file from a raw GitHub URL.

    Returns None on any error (graceful degradation).
    """
    headers = {"Authorization": f"Bearer {token}"}
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            resp = await client.get(url, headers=headers)
            resp.raise_for_status()
            return resp.json()
    except Exception as exc:  # noqa: BLE001
        logger.warning("Could not fetch %s: %s", url, exc)
        return None


def _freshness_label(last_updated: Optional[str]) -> str:
    """Return a human-readable freshness label for the dataset.

    Args:
        last_updated: ISO-8601 timestamp or None.

    Returns:
        e.g. 'Updated 2h ago' or 'Updated today'.
    """
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
    """Format the top-starred repos as a markdown table.

    Args:
        top_starred: List of repo dicts from top_starred.json.

    Returns:
        Markdown table string.
    """
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
    """Format top 5 languages as a markdown list.

    Args:
        languages: Ordered dict of language → count.

    Returns:
        Markdown bullet list string.
    """
    items = list(languages.items())[:5]
    return "\n".join(f"- **{lang}**: {count:,} repos" for lang, count in items)


def _category_list(categories: dict[str, int]) -> str:
    """Format top 5 categories as a markdown list.

    Args:
        categories: Ordered dict of category → count.

    Returns:
        Markdown bullet list string.
    """
    items = list(categories.items())[:5]
    return "\n".join(f"- **{cat}**: {count:,} repos" for cat, count in items)


def build_readme(
    index: Optional[dict],
    recent: Optional[list],
    top_starred: Optional[list],
) -> str:
    """Build README.md content from fetched data with graceful degradation.

    Args:
        index: Parsed index.json or None if unavailable.
        recent: Parsed recent.json list or None.
        top_starred: Parsed top_starred.json list or None.

    Returns:
        Markdown string for README.md.
    """
    if index is None:
        meta: dict = {}
        languages: dict = {}
        categories: dict = {}
        degraded = True
    else:
        meta = index.get("meta", {})
        languages = index.get("languages", {})
        categories = index.get("categories", {})
        degraded = False

    total = meta.get("total", 0)
    last_updated = meta.get("last_updated")
    freshness = _freshness_label(last_updated)

    stars_table = _top_stars_table(top_starred or [])
    lang_section = _lang_list(languages) if languages else "_No language data available_"

    # Enrichment categories from the reporium-ingestion pipeline
    enrichment_cats = (
        "- **Agents** · **LLM Serving** · **Evaluation** · **RAG** · **Fine-tuning** · "
        "**Observability** · **Vector Stores** · **Orchestration** · **Code Generation** · "
        "**Data Pipelines** · **Tooling** · **Models**"
    )

    degraded_note = (
        "\n> **Note:** Source data is temporarily unavailable. Showing cached info.\n"
        if degraded
        else ""
    )

    return f"""# Reporium Dataset
> {total:,} AI development tools tracked on GitHub. Nightly updates. 12 enrichment categories.
> The open dataset behind [reporium.com](https://reporium.com) — find what AI engineers are actually building.
{degraded_note}
[![Updated nightly](https://img.shields.io/badge/updated-nightly-blue)](https://github.com/perditioinc/reporium-db)
[![Repos tracked](https://img.shields.io/badge/repos-{total:,}-green)](https://reporium.com)

## Overview

This dataset is automatically updated every night from [reporium-db](https://github.com/perditioinc/reporium-db),
which fetches GitHub repository metadata via the GraphQL API. Repos are AI-enriched by
[reporium-ingestion](https://github.com/perditioinc/reporium-ingestion) across 12 categories.

**{freshness}** | [{total:,} repos tracked](https://reporium.com) | 12 AI categories

## AI Categories

{enrichment_cats}

## Top Repos by Stars

{stars_table}

## Top Languages

{lang_section}

## Data Files

| File | Description |
|------|-------------|
| `data/index.json` | Counts + metadata (tiny, always fast) |
| `data/recent.json` | Repos pushed in last 7 days (max 500) |
| `data/top_starred.json` | Top 100 by stars |
| `data/by_language/*.json` | One file per language |
| `data/by_category/*.json` | One file per category/topic |
| `data/full/repos_NNNN.json` | Full dataset, 10K repos per file |

## Platform

This dataset powers [reporium.com](https://reporium.com) - search and discovery for AI development tools.

Source: [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db)

## License

Data is sourced from the GitHub API. MIT license.
"""


async def main() -> None:
    """Fetch data from reporium-db and regenerate README.md."""
    t0 = time.monotonic()
    token = os.getenv("GH_TOKEN", "")

    index = await _fetch_json(f"{BASE_RAW_URL}/index.json", token)
    recent = await _fetch_json(f"{BASE_RAW_URL}/recent.json", token)
    top_starred = await _fetch_json(f"{BASE_RAW_URL}/top_starred.json", token)

    readme = build_readme(index, recent, top_starred)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    elapsed = time.monotonic() - t0
    total = (index or {}).get("meta", {}).get("total", 0)
    logger.info("README generated in %.2fs - %d repos", elapsed, total)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
