"""Shared test fixtures for reporium-dataset."""

from __future__ import annotations

import pytest


@pytest.fixture
def sample_stats() -> dict:
    """A minimal /library stats payload."""
    return {
        "total_repos": 818,
        "total_forks": 808,
        "total_non_forks": 10,
        "languages": {"Python": 314, "TypeScript": 112, "Go": 37},
        "top_tags": [],
        "last_updated": "2026-03-17T05:01:30+00:00",
    }


@pytest.fixture
def sample_repos() -> list:
    """A minimal /repos payload — mix of personal and forked repos."""
    return [
        {
            "name": "reporium",
            "owner": "perditioinc",
            "description": "The reporium platform",
            "is_fork": False,
            "forked_from": None,
            "primary_language": "Python",
            "github_url": "https://github.com/perditioinc/reporium",
            "parent_stars": None,
            "parent_forks": None,
            "your_last_push_at": "2026-03-10T00:00:00Z",
            "updated_at": "2026-03-10T00:00:00Z",
        },
        {
            "name": "reporium-api",
            "owner": "perditioinc",
            "description": "Backend API for reporium",
            "is_fork": False,
            "forked_from": None,
            "primary_language": "Python",
            "github_url": "https://github.com/perditioinc/reporium-api",
            "parent_stars": None,
            "parent_forks": None,
            "your_last_push_at": "2026-03-08T00:00:00Z",
            "updated_at": "2026-03-08T00:00:00Z",
        },
        {
            "name": "llm-framework",
            "owner": "perditioinc",
            "description": "Great LLM framework for building agents",
            "is_fork": True,
            "forked_from": "upstream/llm-framework",
            "primary_language": "Python",
            "github_url": "https://github.com/perditioinc/llm-framework",
            "parent_stars": 15000,
            "parent_forks": 2000,
            "your_last_push_at": "2026-03-15T00:00:00Z",
            "updated_at": "2026-03-15T00:00:00Z",
        },
        {
            "name": "rag-toolkit",
            "owner": "perditioinc",
            "description": "RAG toolkit",
            "is_fork": True,
            "forked_from": "bigco/rag-toolkit",
            "primary_language": "TypeScript",
            "github_url": "https://github.com/perditioinc/rag-toolkit",
            "parent_stars": 8000,
            "parent_forks": 1200,
            "your_last_push_at": "2026-03-12T00:00:00Z",
            "updated_at": "2026-03-12T00:00:00Z",
        },
    ]
