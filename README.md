# Reporium Dataset
<!-- perditio-badges-start -->
[![Tests](https://github.com/perditioinc/reporium-dataset/actions/workflows/test.yml/badge.svg)](https://github.com/perditioinc/reporium-dataset/actions/workflows/test.yml)
[![Nightly](https://github.com/perditioinc/reporium-dataset/actions/workflows/update.yml/badge.svg)](https://github.com/perditioinc/reporium-dataset/actions/workflows/update.yml)
![Last Commit](https://img.shields.io/github/last-commit/perditioinc/reporium-dataset)
![python](https://img.shields.io/badge/python-3.11%2B-3776ab)
![suite](https://img.shields.io/badge/suite-Reporium-6e40c9)
<!-- perditio-badges-end -->

> Open dataset of AI development tool repositories — updated nightly from [reporium-api](https://github.com/perditioinc/reporium-api).

> **Note:** reporium-api is unavailable. Data will appear once the API is deployed.

[![Updated nightly](https://img.shields.io/badge/updated-nightly-blue)](https://github.com/perditioinc/reporium-db)
[![Repos tracked](https://img.shields.io/badge/repos-0-green)](https://reporium.com)

## Overview

| Stat | Value |
|------|------:|
| Total repos | 0 |
| Perditio projects | 0 |
| Forked AI repos | 0 |
| Languages tracked | 0 |
| AI categories enriched | 0 _(ingestion pipeline not yet running)_ |
| Last updated | Update time unknown |

## Perditio Projects

0 repositories built and maintained by Perditio.

_Personal repos data unavailable_

## Forked AI Repos

_Forked repos data unavailable_

## Top Repos by Stars

_No data available_

## Top Languages

_No language data available_

## Status

| Component | Status |
|-----------|--------|
| Repo tracking | Active — 0 repos, nightly sync |
| Language breakdown | Active — 0 languages tracked |
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
