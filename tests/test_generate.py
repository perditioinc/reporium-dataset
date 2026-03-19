"""Tests for generate.py."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import httpx
import respx

from generate import _fetch_json, _freshness_label, build_readme

RAW_BASE = "https://raw.githubusercontent.com/perditioinc/reporium-db/main/data"


# ── build_readme ──────────────────────────────────────────────────────────────


def test_readme_contains_total(sample_index, sample_top_starred):
    """README shows formatted total repo count."""
    readme = build_readme(sample_index, [], sample_top_starred)
    assert "805" in readme


def test_readme_has_top_repos_table(sample_index, sample_top_starred):
    """README includes a top-repos stars table."""
    readme = build_readme(sample_index, [], sample_top_starred)
    assert "owner/alpha" in readme
    assert "5,000" in readme


def test_readme_shows_top_languages(sample_index, sample_top_starred):
    """README includes the top languages section."""
    readme = build_readme(sample_index, [], sample_top_starred)
    assert "Python" in readme
    assert "TypeScript" in readme


def test_readme_shows_top_categories(sample_index, sample_top_starred):
    """README is honest about category enrichment status."""
    readme = build_readme(sample_index, [], sample_top_starred)
    assert "ingestion" in readme.lower()


def test_readme_graceful_degradation_when_none():
    """README renders without crashing when all source data is None."""
    readme = build_readme(None, None, None)
    assert "# Reporium Dataset" in readme
    assert "temporarily unavailable" in readme


def test_readme_no_degraded_note_when_data_present(sample_index, sample_top_starred):
    """No degradation note when index is available."""
    readme = build_readme(sample_index, [], sample_top_starred)
    assert "temporarily unavailable" not in readme


def test_readme_has_required_sections(sample_index, sample_top_starred):
    """README contains all required structural sections."""
    readme = build_readme(sample_index, [], sample_top_starred)
    for section in [
        "## Overview",
        "## Perditio Projects",
        "## Forked AI Repos",
        "## Top Repos by Stars",
        "## Top Languages",
        "## Data Files",
    ]:
        assert section in readme, f"Missing: {section}"


def test_readme_personal_repos_section(sample_index, sample_top_starred, sample_all_repos):
    """README includes the personal repos section with non-fork repos."""
    readme = build_readme(sample_index, [], sample_top_starred, sample_all_repos)
    assert "## Perditio Projects" in readme
    assert "owner/repo-a" in readme
    assert "owner/repo-b" in readme


def test_readme_personal_repos_sorted_by_stars(sample_index, sample_top_starred, sample_all_repos):
    """Personal repos table is sorted by stars descending."""
    readme = build_readme(sample_index, [], sample_top_starred, sample_all_repos)
    pos_a = readme.find("repo-a")  # 8000 stars
    pos_b = readme.find("repo-b")  # 2000 stars
    assert pos_a < pos_b


def test_readme_forked_repos_section(sample_index, sample_top_starred, sample_all_repos):
    """README includes the forked repos section."""
    readme = build_readme(sample_index, [], sample_top_starred, sample_all_repos)
    assert "## Forked AI Repos" in readme
    assert "forked-llm" in readme


def test_readme_forked_repos_show_parent(sample_index, sample_top_starred, sample_all_repos):
    """Forked repos table shows upstream owner username, stars, and forks."""
    readme = build_readme(sample_index, [], sample_top_starred, sample_all_repos)
    # shows owner username (not full repo path)
    assert "upstream" in readme
    assert "upstream/llm-framework" not in readme
    assert "15,000" in readme


def test_readme_personal_and_forked_separated(sample_index, sample_top_starred, sample_all_repos):
    """Personal repos and forked repos appear in distinct sections."""
    readme = build_readme(sample_index, [], sample_top_starred, sample_all_repos)
    personal_pos = readme.find("## Perditio Projects")
    forked_pos = readme.find("## Forked AI Repos")
    assert personal_pos < forked_pos
    # repo-a/b (personal) should appear before forked-llm
    pos_personal = readme.find("repo-a")
    pos_fork = readme.find("forked-llm")
    assert pos_personal < pos_fork


def test_readme_full_repo_table_missing_gracefully(sample_index, sample_top_starred):
    """README renders without crash when full repos are unavailable."""
    readme = build_readme(sample_index, [], sample_top_starred, None)
    assert "# Reporium Dataset" in readme
    assert "unavailable" in readme


def test_readme_overview_shows_counts(sample_index, sample_top_starred, sample_all_repos):
    """Overview table shows personal and forked counts."""
    readme = build_readme(sample_index, [], sample_top_starred, sample_all_repos)
    assert "Perditio projects" in readme
    assert "Forked AI repos" in readme


# ── _freshness_label ──────────────────────────────────────────────────────────


def test_freshness_recent():
    """Returns '<1h' label for very recent timestamps."""
    ts = (datetime.now(timezone.utc) - timedelta(minutes=30)).isoformat()
    assert "less than 1h" in _freshness_label(ts)


def test_freshness_hours_ago():
    """Returns correct hour count for timestamps a few hours old."""
    ts = (datetime.now(timezone.utc) - timedelta(hours=5)).isoformat()
    label = _freshness_label(ts)
    assert "5h" in label


def test_freshness_days_ago():
    """Returns day count for timestamps more than 24h old."""
    ts = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
    label = _freshness_label(ts)
    assert "2d" in label


def test_freshness_none():
    """Returns fallback string when timestamp is None."""
    assert "unknown" in _freshness_label(None)


def test_freshness_invalid():
    """Returns fallback string for unparseable timestamp."""
    assert "unknown" in _freshness_label("not-a-date")


# ── _fetch_json ───────────────────────────────────────────────────────────────


@respx.mock
async def test_fetch_json_success():
    """Returns parsed JSON on 200 response."""
    url = f"{RAW_BASE}/index.json"
    respx.get(url).mock(return_value=httpx.Response(200, json={"meta": {"total": 5}}))
    result = await _fetch_json(url, "test-token")
    assert result == {"meta": {"total": 5}}


@respx.mock
async def test_fetch_json_returns_none_on_404():
    """Returns None gracefully on 404."""
    url = f"{RAW_BASE}/missing.json"
    respx.get(url).mock(return_value=httpx.Response(404))
    result = await _fetch_json(url, "test-token")
    assert result is None


@respx.mock
async def test_fetch_json_returns_none_on_network_error():
    """Returns None gracefully when network request fails."""
    url = f"{RAW_BASE}/index.json"
    respx.get(url).mock(side_effect=httpx.ConnectError("timeout"))
    result = await _fetch_json(url, "test-token")
    assert result is None
