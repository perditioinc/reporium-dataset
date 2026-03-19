# Reporium Dataset

> Open dataset of AI development tool repositories — updated nightly from [reporium-api](https://github.com/perditioinc/reporium-api).

[![Updated nightly](https://img.shields.io/badge/updated-nightly-blue)](https://github.com/perditioinc/reporium-db)
[![Repos tracked](https://img.shields.io/badge/repos-818-green)](https://reporium.com)

## Overview

| Stat | Value |
|------|------:|
| Total repos | 818 |
| Perditio projects | 0 |
| Forked AI repos | 0 |
| Languages tracked | 29 |
| AI categories enriched | 0 _(ingestion pipeline not yet running)_ |
| Last updated | Updated less than 1h ago |

## Perditio Projects

0 repositories built and maintained by Perditio.

_Personal repos data unavailable_

## Forked AI Repos

_Forked repos data unavailable_

## Top Repos by Stars

_No data available_

## Top Languages

- **Python**: 314 repos
- **TypeScript**: 112 repos
- **Jupyter Notebook**: 87 repos
- **C++**: 67 repos
- **Go**: 37 repos
- **C**: 30 repos
- **JavaScript**: 27 repos
- **C#**: 21 repos
- **Rust**: 15 repos
- **Shell**: 8 repos

## Status

| Component | Status |
|-----------|--------|
| Repo tracking | Active — 818 repos, nightly sync |
| Language breakdown | Active — 29 languages tracked |
| AI enrichment categories | Not yet active — ingestion pipeline not running |
| README summaries | Not yet active — ingestion pipeline not running |

> AI enrichment (Agents, LLM Serving, RAG, Fine-tuning, Observability, etc.) will be populated
> once the reporium-ingestion pipeline is deployed.

## Data Access

Data is served via the [reporium-api](https://github.com/perditioinc/reporium-api):

| Endpoint | Description |
|----------|-------------|
| `GET /repos?sort=stars` | All repos sorted by upstream stars |
| `GET /repos?is_fork=false` | Personal projects only |
| `GET /repos?is_fork=true` | Forked repos only |
| `GET /library` | Stats, language breakdown, categories |
| `GET /repos/{name}` | Single repo detail |

## Platform

This dataset powers [reporium.com](https://reporium.com) — search and discovery for AI development tools.

Source: [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db) |
API: [perditioinc/reporium-api](https://github.com/perditioinc/reporium-api)

## License

Data is sourced from the GitHub API. MIT license.
