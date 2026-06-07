"""Smoke test: exercise the real generate.py against the local OSS api-stub.

Runs inside the runner container. REPORIUM_API_URL points at the local stub,
so generate.py takes its primary (API) code path with no cloud access. The
generated README.md is then asserted against the seeded dataset.

Exit 0 = PASS, non-zero = FAIL.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys

# generate.py lives at repo root, mounted read-only at /app.
sys.path.insert(0, "/app")

import generate  # noqa: E402


def _fail(msg: str) -> None:
    print(f"[smoke] FAIL: {msg}")
    sys.exit(1)


async def _wait_for_api(url: str, attempts: int = 30) -> None:
    import httpx

    for i in range(attempts):
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                resp = await client.get(f"{url}/health")
                if resp.status_code == 200:
                    print(f"[smoke] api-stub healthy: {resp.json()}")
                    return
        except Exception:  # noqa: BLE001
            pass
        await asyncio.sleep(1)
    _fail(f"api-stub never became healthy at {url} after {attempts}s")


def main() -> None:
    api_url = os.getenv("REPORIUM_API_URL", "")
    if not api_url:
        _fail("REPORIUM_API_URL not set — smoke must exercise the API code path")

    seed_path = os.getenv("LOCAL_SEED", "/seed/dataset.json")
    with open(seed_path, encoding="utf-8") as f:
        seed = json.load(f)
    expected_total = seed["stats"]["total_repos"]
    expected_personal = sum(1 for r in seed["repos"] if not r.get("is_fork"))
    expected_forked = sum(1 for r in seed["repos"] if r.get("is_fork"))

    asyncio.run(_wait_for_api(api_url))

    # Run the REAL entry point. It writes README.md in the cwd.
    out_dir = os.getenv("SMOKE_OUT", "/out")
    os.makedirs(out_dir, exist_ok=True)
    os.chdir(out_dir)
    asyncio.run(generate.main())

    readme_path = os.path.join(out_dir, "README.md")
    if not os.path.exists(readme_path):
        _fail("generate.py did not write README.md")

    with open(readme_path, encoding="utf-8") as f:
        readme = f.read()

    # Structural assertions — the real README contract.
    required_sections = [
        "# Reporium Dataset",
        "## Overview",
        "## Perditio Projects",
        "## Forked AI Repos",
        "## Top Repos by Stars",
        "## Top Languages",
        "## Status",
        "## Data Access",
    ]
    for section in required_sections:
        if section not in readme:
            _fail(f"README missing section: {section}")

    # Data assertions — values must reflect the seeded dataset (API path, not degraded).
    if "unavailable" in readme:
        _fail("README is in degraded mode — API path was not exercised")
    if f"{expected_total:,}" not in readme:
        _fail(f"README missing total repo count {expected_total:,}")
    if f"| Perditio projects | {expected_personal:,} |" not in readme:
        _fail(f"README missing personal count {expected_personal}")
    if f"| Forked AI repos | {expected_forked:,} |" not in readme:
        _fail(f"README missing forked count {expected_forked}")

    # Forked table sort order: 15,000-star fork must precede 8,000-star fork.
    if readme.find("llm-framework") >= readme.find("rag-toolkit"):
        _fail("forked repos not sorted by upstream stars")

    print(f"[smoke] PASS: README built from API stub — {expected_total} repos, "
          f"{expected_personal} personal, {expected_forked} forked")
    sys.exit(0)


if __name__ == "__main__":
    main()
