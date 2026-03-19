# Reporium Dataset
> 818 AI development tools tracked on GitHub. Nightly updates. 12 enrichment categories.
> The open dataset behind [reporium.com](https://reporium.com) — find what AI engineers are actually building.

[![Updated nightly](https://img.shields.io/badge/updated-nightly-blue)](https://github.com/perditioinc/reporium-db)
[![Repos tracked](https://img.shields.io/badge/repos-818-green)](https://reporium.com)

## Overview

This dataset is automatically updated every night from [reporium-db](https://github.com/perditioinc/reporium-db),
which fetches GitHub repository metadata via the GraphQL API. Repos are AI-enriched by
[reporium-ingestion](https://github.com/perditioinc/reporium-ingestion) across 12 categories.

**Updated less than 1h ago** | [818 repos tracked](https://reporium.com) | 12 AI categories

## AI Categories

- **Agents** · **LLM Serving** · **Evaluation** · **RAG** · **Fine-tuning** · **Observability** · **Vector Stores** · **Orchestration** · **Code Generation** · **Data Pipelines** · **Tooling** · **Models**

## Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| [perditioinc/reporium](https://github.com/perditioinc/reporium) | 1 | TypeScript |
| [perditioinc/reporium-api](https://github.com/perditioinc/reporium-api) | 1 | Python |
| [perditioinc/reporium-ingestion](https://github.com/perditioinc/reporium-ingestion) | 1 | Python |
| [perditioinc/forksync](https://github.com/perditioinc/forksync) | 1 | Python |
| [perditioinc/portfolio](https://github.com/perditioinc/portfolio) | 1 | Python |
| [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db) | 1 | Python |
| [perditioinc/reporium-dataset](https://github.com/perditioinc/reporium-dataset) | 1 | Python |
| [perditioinc/reporium-roadmap](https://github.com/perditioinc/reporium-roadmap) | 1 | Python |
| [perditioinc/reporium-metrics](https://github.com/perditioinc/reporium-metrics) | 1 | Python |
| [perditioinc/repo-intelligence](https://github.com/perditioinc/repo-intelligence) | 1 | Python |

## Top Languages

- **Python**: 314 repos
- **TypeScript**: 112 repos
- **Jupyter Notebook**: 87 repos
- **C++**: 67 repos
- **Go**: 37 repos

## Data Files

| File | Description |
|------|-------------|
| `data/index.json` | Counts + metadata (tiny, always fast) |
| `data/recent.json` | Repos pushed in last 7 days (max 500) |
| `data/top_starred.json` | Top 100 by stars |
| `data/by_language/*.json` | One file per language |
| `data/by_category/*.json` | One file per category/topic |
| `data/full/repos_NNNN.json` | Full dataset, 10K repos per file |

## Platform

This dataset powers [reporium.com](https://reporium.com) - search and discovery for AI development tools.

Source: [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db)

## License

Data is sourced from the GitHub API. MIT license.
