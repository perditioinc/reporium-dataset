"""Tests for generate.py."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import httpx
import respx

from generate import (
    _api_get,
    _fetch_all_repos,
    _fetch_stats,
    _fork_display,
    _freshness_label,
    build_readme,
)

API_BASE = "http://test-api.local"


# ── build_readme ──────────────────────────────────────────────────────────────


def test_readme_contains_total(sample_stats, sample_repos):
    """README shows formatted total repo count."""
    readme = build_readme(sample_stats, sample_repos)
    assert "818" in readme


def test_readme_has_required_sections(sample_stats, sample_repos):
    """README contains all required structural sections."""
    readme = build_readme(sample_stats, sample_repos)
    for section in [
        "## Overview",
        "## Perditio Projects",
        "## Forked AI Repos",
        "## Top Repos by Stars",
        "## Top Languages",
        "## Status",
        "## Data Access",
    ]:
        assert section in readme, f"Missing: {section}"


def test_readme_shows_top_languages(sample_stats, sample_repos):
    """README includes the top languages from stats."""
    readme = build_readme(sample_stats, sample_repos)
    assert "Python" in readme
    assert "TypeScript" in readme


def test_readme_shows_ingestion_note(sample_stats, sample_repos):
    """README is honest about ingestion pipeline not running."""
    readme = build_readme(sample_stats, sample_repos)
    assert "ingestion" in readme.lower()


def test_readme_graceful_degradation_when_none():
    """README renders without crashing when all data is None."""
    readme = build_readme(None, None)
    assert "# Reporium Dataset" in readme
    assert "unavailable" in readme


def test_readme_no_degraded_note_when_data_present(sample_stats, sample_repos):
    """No API-unavailable note when data is present."""
    readme = build_readme(sample_stats, sample_repos)
    assert "unavailable" not in readme


def test_readme_personal_section_shows_repos(sample_stats, sample_repos):
    """Perditio Projects section lists personal repos with owner/name."""
    readme = build_readme(sample_stats, sample_repos)
    assert "## Perditio Projects" in readme
    assert "perditioinc/reporium" in readme
    assert "perditioinc/reporium-api" in readme


def test_readme_forked_section_shows_repos(sample_stats, sample_repos):
    """Forked AI Repos section lists forked repos."""
    readme = build_readme(sample_stats, sample_repos)
    assert "## Forked AI Repos" in readme
    assert "llm-framework" in readme
    assert "rag-toolkit" in readme


def test_readme_forked_section_shows_upstream_path(sample_stats, sample_repos):
    """Fork column shows full parent repo path inline (no separate Forked From column)."""
    readme = build_readme(sample_stats, sample_repos)
    assert "upstream/llm-framework" in readme
    assert "bigco/rag-toolkit" in readme
    assert "Forked From" not in readme


def test_readme_forked_section_shows_stars_and_forks(sample_stats, sample_repos):
    """Forked repos table shows parent stars and forks."""
    readme = build_readme(sample_stats, sample_repos)
    assert "15,000" in readme  # parent_stars for llm-framework
    assert "2,000" in readme   # parent_forks for llm-framework


def test_readme_forked_sorted_by_upstream_stars(sample_stats, sample_repos):
    """Forked repos appear in descending upstream-star order."""
    readme = build_readme(sample_stats, sample_repos)
    pos_llm = readme.find("llm-framework")   # 15,000 upstream stars
    pos_rag = readme.find("rag-toolkit")     # 8,000 upstream stars
    assert pos_llm < pos_rag


def test_readme_personal_and_forked_sections_ordered(sample_stats, sample_repos):
    """Perditio Projects section appears before Forked AI Repos section."""
    readme = build_readme(sample_stats, sample_repos)
    assert readme.find("## Perditio Projects") < readme.find("## Forked AI Repos")


def test_readme_overview_shows_counts(sample_stats, sample_repos):
    """Overview table shows personal and forked counts."""
    readme = build_readme(sample_stats, sample_repos)
    assert "Perditio projects" in readme
    assert "Forked AI repos" in readme


def test_readme_fork_column_has_owner_slash_name(sample_stats, sample_repos):
    """Fork column shows owner/name format."""
    readme = build_readme(sample_stats, sample_repos)
    assert "perditioinc/llm-framework" in readme


def test_readme_repos_none_shows_unavailable(sample_stats):
    """Shows unavailable when repos is None but stats is present."""
    readme = build_readme(sample_stats, None)
    assert "# Reporium Dataset" in readme
    assert "unavailable" in readme


# ── _fork_display ──────────────────────────────────────────────────────────────


def test_fork_display_short_name():
    """Short names pass through unchanged."""
    assert _fork_display("perditioinc", "reporium") == "perditioinc/reporium"


def test_fork_display_truncates_long_name():
    """Names longer than max_len are truncated with ellipsis."""
    result = _fork_display("perditioinc", "a-very-long-repository-name-here", max_len=35)
    assert len(result) <= 35
    assert result.endswith("…")


def test_fork_display_exact_max_len():
    """Names exactly at max_len are not truncated."""
    name = "x" * 23  # perditioinc/ = 12 chars, so 12+23=35 exactly
    result = _fork_display("perditioinc", name, max_len=35)
    assert "…" not in result


# ── _freshness_label ──────────────────────────────────────────────────────────


def test_freshness_recent():
    """Returns '<1h' label for very recent timestamps."""
    ts = (datetime.now(timezone.utc) - timedelta(minutes=30)).isoformat()
    assert "less than 1h" in _freshness_label(ts)


def test_freshness_hours_ago():
    """Returns correct hour count for timestamps a few hours old."""
    ts = (datetime.now(timezone.utc) - timedelta(hours=5)).isoformat()
    assert "5h" in _freshness_label(ts)


def test_freshness_days_ago():
    """Returns day count for timestamps more than 24h old."""
    ts = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
    assert "2d" in _freshness_label(ts)


def test_freshness_none():
    """Returns fallback string when timestamp is None."""
    assert "unknown" in _freshness_label(None)


def test_freshness_invalid():
    """Returns fallback string for unparseable timestamp."""
    assert "unknown" in _freshness_label("not-a-date")


# ── _api_get / _fetch_all_repos / _fetch_stats ────────────────────────────────


@respx.mock
async def test_api_get_success():
    """Returns parsed JSON on 200."""
    respx.get(f"{API_BASE}/repos").mock(
        return_value=httpx.Response(200, json={"repos": [], "page": 1, "limit": 200})
    )
    async with httpx.AsyncClient(timeout=15) as client:
        result = await _api_get(client, API_BASE, "/repos", sort="stars", limit=200, page=1)
    assert result == {"repos": [], "page": 1, "limit": 200}


@respx.mock
async def test_api_get_returns_none_on_error():
    """Returns None on HTTP error."""
    respx.get(f"{API_BASE}/repos").mock(return_value=httpx.Response(503))
    async with httpx.AsyncClient(timeout=15) as client:
        result = await _api_get(client, API_BASE, "/repos")
    assert result is None


@respx.mock
async def test_fetch_all_repos_paginates():
    """Fetches multiple pages until batch < limit."""
    page1 = {"repos": [{"name": f"repo-{i}"} for i in range(200)], "page": 1, "limit": 200}
    page2 = {"repos": [{"name": "repo-last"}], "page": 2, "limit": 200}
    route = respx.get(f"{API_BASE}/repos")
    route.side_effect = [
        httpx.Response(200, json=page1),
        httpx.Response(200, json=page2),
    ]
    result = await _fetch_all_repos(API_BASE)
    assert result is not None
    assert len(result) == 201


@respx.mock
async def test_fetch_all_repos_returns_none_when_url_empty():
    """Returns None immediately when api_url is empty."""
    result = await _fetch_all_repos("")
    assert result is None


@respx.mock
async def test_fetch_stats_returns_stats_dict():
    """Extracts stats from /library response."""
    payload = {
        "repos": [],
        "stats": {"total_repos": 818, "total_forks": 808, "total_non_forks": 10,
                  "languages": {"Python": 314}, "top_tags": []},
        "categories": [],
        "tag_metrics": [],
        "total": 818,
        "page": 1,
        "limit": 1,
    }
    respx.get(f"{API_BASE}/library").mock(return_value=httpx.Response(200, json=payload))
    result = await _fetch_stats(API_BASE)
    assert result is not None
    assert result["total_repos"] == 818


@respx.mock
async def test_fetch_stats_returns_none_on_failure():
    """Returns None when API is unavailable."""
    respx.get(f"{API_BASE}/library").mock(side_effect=httpx.ConnectError("refused"))
    result = await _fetch_stats(API_BASE)
    assert result is None
