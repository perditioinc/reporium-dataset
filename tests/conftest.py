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


@pytest.fixture
def sample_all_repos() -> list:
    """A minimal full repos payload — mix of personal and forked repos."""
    return [
        {
            "nameWithOwner": "owner/repo-b",
            "name": "repo-b",
            "stars": 2000,
            "primaryLanguage": "Go",
            "description": "Fast inference engine",
            "isFork": False,
            "pushedAt": "2026-03-01T00:00:00Z",
            "parentRepo": None,
            "parentStars": None,
        },
        {
            "nameWithOwner": "owner/repo-a",
            "name": "repo-a",
            "stars": 8000,
            "primaryLanguage": "Python",
            "description": "Top RAG library",
            "isFork": False,
            "pushedAt": "2026-03-10T00:00:00Z",
            "parentRepo": None,
            "parentStars": None,
        },
        {
            "nameWithOwner": "owner/forked-llm",
            "name": "forked-llm",
            "stars": 0,
            "primaryLanguage": "Python",
            "description": "Great LLM framework",
            "isFork": True,
            "pushedAt": "2026-03-15T00:00:00Z",
            "parentRepo": "upstream/llm-framework",
            "parentStars": 15000,
        },
    ]
