# Local OSS substrate (`local/`)

A self-contained, `$0`, OSS-only development substrate for `reporium-dataset`.
It lets you run the real `generate.py` end to end on your machine without any
production endpoints, hosted services, or secrets.

This directory is **additive and local-only**. It changes no application code,
no CI, and contacts no cloud service.

## What it stands up

`generate.py` builds `README.md` from two upstream data sources:

| Real dependency | What it is | Local OSS substitute |
|-----------------|-----------|----------------------|
| `reporium-api` | Hosted HTTP API (`/repos`, `/library`) — the **primary** source | `api-stub` — a zero-dependency Python stdlib HTTP server (`stub/api_stub.py`) serving the exact same contract from a seed file |
| `reporium-db` raw files on `raw.githubusercontent.com` | The **fallback** source when the API is down | Not contacted. The smoke drives the primary (API) path, so there is no network egress. |

The substitution is **env-pointed**: the real `generate.py` runs unmodified,
with `REPORIUM_API_URL` aimed at the local stub via a Docker network alias.
The repo source is mounted **read-only**.

## API contract the stub mirrors

```
GET /repos?sort=stars&limit=<n>&page=<n>  -> {"repos": [...], "page", "limit", "total"}
GET /library?limit=1                       -> {"stats": {...}, ...}
GET /health                                -> {"status": "ok", ...}   (substrate-only)
```

This matches what `_fetch_all_repos` and `_fetch_stats` in `generate.py` expect,
including `sort=stars`, `limit=200` pagination, and the `stats` envelope.

## Usage

From the repo root (root `Makefile` passes through) or from `local/`:

```bash
make up      # start the api-stub (OSS reporium-api substitute), wait until healthy
make seed    # show the seeded dataset the stub serves
make smoke   # run the real generate.py against the stub and assert the README
make down    # stop + remove containers and volumes (teardown)
```

`make smoke` runs `smoke.py`, which:

1. waits for `api-stub` to report healthy,
2. invokes the real `generate.main()` with `REPORIUM_API_URL=http://api-stub:8000`,
3. asserts the generated `README.md` has every required section, is **not** in
   degraded mode (proving the API path was used), and that the repo counts and
   fork sort order reflect the seeded dataset.

Exit code `0` = PASS.

## Customizing the data

Edit `seed/dataset.json`. Both the stub and the smoke read it, so counts stay
in sync automatically. The schema matches the reporium-api `/library` `stats`
object and the `/repos` repo objects.

## Requirements

- Docker with Compose v2 (`docker compose`). Images: `python:3.11-slim` only.
- No secrets, no tokens, no paid services.
