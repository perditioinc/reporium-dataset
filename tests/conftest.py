"""Shared test fixtures for reporium-dataset."""

from __future__ import annotations

import pytest


@pytest.fixture
def sample_index() -> dict:
    """A minimal realistic index.json payload."""
    return {
        "meta": {
            "total": 805,
            "last_updated": "2026-03-17T05:01:30+00:00",
            "version": "1.0.0",
        },
        "languages": {"Python": 400, "TypeScript": 200, "Go": 100},
        "categories": {"llm": 300, "rag": 100, "agents": 80},
    }


@pytest.fixture
def sample_top_starred() -> list:
    """A minimal top_starred.json payload."""
    return [
        {
            "nameWithOwner": "owner/alpha",
            "stars": 5000,
            "primaryLanguage": "Python",
            "description": "Best LLM framework",
        },
        {
            "nameWithOwner": "owner/beta",
            "stars": 3000,
            "primaryLanguage": "TypeScript",
            "description": "Another great tool",
        },
    ]
