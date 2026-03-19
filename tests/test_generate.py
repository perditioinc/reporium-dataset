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
    for section in ["## Overview", "## Top Repos by Stars", "## Top Languages", "## Data Files"]:
        assert section in readme, f"Missing: {section}"


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
