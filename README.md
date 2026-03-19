# Reporium Dataset

> Open dataset of AI development tool repositories tracked on GitHub — updated nightly.
> Powering [reporium.com](https://reporium.com).

[![Updated nightly](https://img.shields.io/badge/updated-nightly-blue)](https://github.com/perditioinc/reporium-db)
[![Repos tracked](https://img.shields.io/badge/repos-818-green)](https://reporium.com)

## Overview

| Stat | Value |
|------|------:|
| Total repos | 818 |
| Perditio projects | 10 |
| Forked AI repos | 808 |
| Languages tracked | 29 |
| AI categories enriched | 0 _(ingestion pipeline not yet running)_ |
| Last updated | Updated 1h ago |

Data is fetched nightly from GitHub via GraphQL and written to partitioned JSON files
in [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db).

## Perditio Projects

10 repositories built and maintained by Perditio.

| Repo | Description | Stars | Language | Last Active |
|------|-------------|------:|----------|-------------|
| [reporium](https://github.com/perditioinc/reporium) | Your GitHub repos as a living AI-native knowledge graph library tool - an AI trend intelligence system that speaks to the people who need to understand what developers are building. Your curation, your lens, your industry perspective. Insights compounds, getting smarter every day. | 1 | TypeScript | 2026-03-18 |
| [reporium-api](https://github.com/perditioinc/reporium-api) | Backend API for Reporium : read/write access to repository database, designed for public queries and private ingestion updates. Gatekeeper API that talks to the database, handles authorized writes, serves data to clients/frontends. Public-facing, but writes are only authorized. | 1 | Python | 2026-03-15 |
| [reporium-ingestion](https://github.com/perditioinc/reporium-ingestion) | Local data ingestion and analysis scripts for Reporium : fetch, process, and generate embeddings for repositories, communicating with Reporium API. AI-native analysis, embeddings, scraping, tagging. Pushes updates to API. Standalone and private by default. | 1 | Python | 2026-03-16 |
| [forksync](https://github.com/perditioinc/forksync) | Tooling ⚙️: Keep your GitHub forks updated automatically. Runs nightly. | 1 | Python | 2026-03-17 |
| [portfolio](https://github.com/perditioinc/portfolio) | Portfolio of AI discovery tools, developer tooling, and automation systems built by Kim Loza | 1 | Python | 2026-03-19 |
| [reporium-db](https://github.com/perditioinc/reporium-db) | Nightly GitHub metadata sync — powers reporium.com. Supports 100K repos via GraphQL tiers, checkpointing, and partitioned output. | 1 | Python | 2026-03-19 |
| [reporium-dataset](https://github.com/perditioinc/reporium-dataset) | Public dataset mirror for reporium.com — nightly-updated AI dev tool stats from reporium-db. | 1 | Python | 2026-03-19 |
| [reporium-roadmap](https://github.com/perditioinc/reporium-roadmap) | Public product roadmap for reporium.com — auto-updated nightly with live GitHub stats. | 1 | Python | 2026-03-19 |
| [reporium-metrics](https://github.com/perditioinc/reporium-metrics) | Platform performance tracking over time — ASCII trend charts, nightly collection. | 1 | Python | 2026-03-19 |
| [repo-intelligence](https://github.com/perditioinc/repo-intelligence) | Score any GitHub repo 0-100 — README, activity, community, CI. Pip-installable. | 1 | Python | 2026-03-19 |

## Forked AI Repos

> Showing top 100 of 808 forked repos (by last activity). Full dataset: [`data/full/repos_0000.json`](https://github.com/perditioinc/reporium-db/blob/main/data/full/repos_0000.json)

| Fork | Upstream Repo | Upstream ⭐ | Language | Description |
|------|--------------|------------:|----------|-------------|
| [NemoClaw](https://github.com/perditioinc/NemoClaw) | — | — | JavaScript | NVIDIA plugin for secure installation of OpenClaw |
| [colab-mcp](https://github.com/perditioinc/colab-mcp) | — | — | Python | An MCP server for interacting with Google Colab |
| [generative-ai](https://github.com/perditioinc/generative-ai) | — | — | Jupyter Notebook | Sample code and notebooks for Generative AI on Google Cloud, with Gemini on Vert… |
| [directus](https://github.com/perditioinc/directus) | — | — | TypeScript | The flexible backend for all your projects 🐰 Turn your DB into a headless CMS, a… |
| [langflow](https://github.com/perditioinc/langflow) | — | — | Python | Langflow is a powerful tool for building and deploying AI-powered agents and wor… |
| [coder](https://github.com/perditioinc/coder) | — | — | Go | Secure environments for developers and their agents |
| [pentagi](https://github.com/perditioinc/pentagi) | — | — | Go | ✨ Fully autonomous AI Agents system capable of performing complex penetration te… |
| [LocalAI](https://github.com/perditioinc/LocalAI) | — | — | Go | :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hos… |
| [handson-mlp](https://github.com/perditioinc/handson-mlp) | — | — | Jupyter Notebook | A series of Jupyter notebooks that walk you through the fundamentals of Machine … |
| [edit](https://github.com/perditioinc/edit) | — | — | JavaScript | Make changes to FMHY |
| [jellyfin-web](https://github.com/perditioinc/jellyfin-web) | — | — | JavaScript | The Free Software Media System - Official Web Client |
| [navidrome](https://github.com/perditioinc/navidrome) | — | — | Go | 🎧☁️ Your Personal Streaming Service |
| [brave-core](https://github.com/perditioinc/brave-core) | — | — | C++ | Core engine for the Brave browser for mobile and desktop. For issues https://git… |
| [attention-residuals](https://github.com/perditioinc/attention-residuals) | — | — | — | — |
| [FreeCAD](https://github.com/perditioinc/FreeCAD) | — | — | C++ | Official source code of FreeCAD, a free and opensource multiplatform 3D parametr… |
| [mongo](https://github.com/perditioinc/mongo) | — | — | C++ | The MongoDB Database |
| [mlx-audio](https://github.com/perditioinc/mlx-audio) | — | — | Python | A text-to-speech (TTS), speech-to-text (STT) and speech-to-speech (STS) library … |
| [JoltPhysics](https://github.com/perditioinc/JoltPhysics) | — | — | C++ | A multi core friendly rigid body physics and collision detection library. Writte… |
| [plannotator](https://github.com/perditioinc/plannotator) | — | — | TypeScript | Annotate and review coding agent plans and code diffs visually, share with your … |
| [openscreen](https://github.com/perditioinc/openscreen) | — | — | TypeScript | Create stunning demos for free. Open-source, no subscriptions, no watermarks, an… |
| [ott-platform](https://github.com/perditioinc/ott-platform) | — | — | Python | Learning Claude Code via a real-world OTT streaming platform implementation |
| [PLFM_RADAR](https://github.com/perditioinc/PLFM_RADAR) | — | — | C | Open-source, low-cost 10.5 GHz PLFM phased array RADAR system |
| [gstack](https://github.com/perditioinc/gstack) | — | — | TypeScript | Use Garry Tan's exact Claude Code setup: 6 opinionated tools that serve as CEO, … |
| [fullstack-solution-template-for-agentcore](https://github.com/perditioinc/fullstack-solution-template-for-agentcore) | — | — | TypeScript | Flexible Fullstack solution template for production-ready deployments of any use… |
| [chrome-devtools-mcp](https://github.com/perditioinc/chrome-devtools-mcp) | — | — | TypeScript | Chrome DevTools for coding agents |
| [nanochat](https://github.com/perditioinc/nanochat) | — | — | Python | The best ChatGPT that $100 can buy. |
| [idea-claude-code-gui](https://github.com/perditioinc/idea-claude-code-gui) | — | — | TypeScript | IDEA Claude Code GUI Plugin |
| [scikit-learn](https://github.com/perditioinc/scikit-learn) | — | — | Python | scikit-learn: machine learning in Python |
| [awesome-machine-learning](https://github.com/perditioinc/awesome-machine-learning) | — | — | Python | A curated list of awesome Machine Learning frameworks, libraries and software. |
| [openclaw-vertexai-memorybank](https://github.com/perditioinc/openclaw-vertexai-memorybank) | — | — | TypeScript | Vertex AI Memory Bank Plugin for OpenClaw |
| [pageindex](https://github.com/perditioinc/pageindex) | — | — | Python | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| [dimos](https://github.com/perditioinc/dimos) | — | — | Python | The Dimensional Framework |
| [transformers](https://github.com/perditioinc/transformers) | — | — | Python | 🤗 Transformers: the model-definition framework for state-of-the-art machine lear… |
| [langchain](https://github.com/perditioinc/langchain) | — | — | Python | The agent engineering platform |
| [tensorflow](https://github.com/perditioinc/tensorflow) | — | — | C++ | An Open Source Machine Learning Framework for Everyone |
| [TransformerEngine](https://github.com/perditioinc/TransformerEngine) | — | — | Python | A library for accelerating Transformer models on NVIDIA GPUs, including using 8-… |
| [cuda-python](https://github.com/perditioinc/cuda-python) | — | — | Cython | CUDA Python: Performance meets Productivity |
| [NeMo-Retriever](https://github.com/perditioinc/NeMo-Retriever) | — | — | Python | NeMo Retriever Library is a scalable, performance-oriented document content and … |
| [CUDALibrarySamples](https://github.com/perditioinc/CUDALibrarySamples) | — | — | C++ | CUDA Library Samples |
| [NeMo-Agent-Toolkit](https://github.com/perditioinc/NeMo-Agent-Toolkit) | — | — | Python | The NVIDIA NeMo Agent toolkit is an open-source library for efficiently connecti… |
| [Megatron-LM](https://github.com/perditioinc/Megatron-LM) | — | — | Python | Ongoing research training transformer models at scale |
| [Isaac-GR00T](https://github.com/perditioinc/Isaac-GR00T) | — | — | Jupyter Notebook | NVIDIA Isaac GR00T N1.6 -  A Foundation Model for Generalist Robots. |
| [DALI](https://github.com/perditioinc/DALI) | — | — | C++ | A GPU-accelerated library containing highly optimized building blocks and an exe… |
| [openai-go](https://github.com/perditioinc/openai-go) | — | — | Go | The official Go library for the OpenAI API |
| [openai-agents-js](https://github.com/perditioinc/openai-agents-js) | — | — | TypeScript | A lightweight, powerful framework for multi-agent workflows and voice agents |
| [cuopt](https://github.com/perditioinc/cuopt) | — | — | Cuda | GPU accelerated decision optimization  |
| [aistore](https://github.com/perditioinc/aistore) | — | — | Go | AIStore: scalable storage for AI applications |
| [claude-code-base-action](https://github.com/perditioinc/claude-code-base-action) | — | — | TypeScript | This repo is a mirror of the contents of base-action in https://github.com/anthr… |
| [claude-agent-sdk-typescript](https://github.com/perditioinc/claude-agent-sdk-typescript) | — | — | Shell | — |
| [symphony](https://github.com/perditioinc/symphony) | — | — | Elixir | Symphony turns project work into isolated, autonomous implementation runs, allow… |
| [adk-java](https://github.com/perditioinc/adk-java) | — | — | Java | An open-source, code-first Java toolkit for building, evaluating, and deploying … |
| [adk-docs](https://github.com/perditioinc/adk-docs) | — | — | Python | An open-source, code-first toolkit for building, evaluating, and deploying sophi… |
| [claude-code-action](https://github.com/perditioinc/claude-code-action) | — | — | TypeScript | — |
| [claude-agent-sdk-python](https://github.com/perditioinc/claude-agent-sdk-python) | — | — | Python | — |
| [AirSim](https://github.com/perditioinc/AirSim) | — | — | C++ | Open source simulator for autonomous vehicles built on Unreal Engine / Unity, fr… |
| [react-native-windows](https://github.com/perditioinc/react-native-windows) | — | — | C++ | A framework for building native Windows apps with React. |
| [garnet](https://github.com/perditioinc/garnet) | — | — | C# | Garnet is a remote cache-store from Microsoft Research that offers strong perfor… |
| [guava](https://github.com/perditioinc/guava) | — | — | Java | Google core libraries for Java |
| [vscode](https://github.com/perditioinc/vscode) | — | — | TypeScript | Visual Studio Code |
| [PowerToys](https://github.com/perditioinc/PowerToys) | — | — | C# | Microsoft PowerToys is a collection of utilities that supercharge productivity a… |
| [markitdown](https://github.com/perditioinc/markitdown) | — | — | Python | Python tool for converting files and office documents to Markdown. |
| [monaco-editor](https://github.com/perditioinc/monaco-editor) | — | — | JavaScript | A browser based code editor |
| [golang-samples](https://github.com/perditioinc/golang-samples) | — | — | Go | Sample apps and code written for Google Cloud in the Go programming language. |
| [gcsfuse](https://github.com/perditioinc/gcsfuse) | — | — | Go | A user-space file system for interacting with Google Cloud Storage |
| [bank-of-anthos](https://github.com/perditioinc/bank-of-anthos) | — | — | Java | Retail banking sample application showcasing Kubernetes and Google Cloud |
| [Java](https://github.com/perditioinc/Java) | — | — | Java | All Algorithms implemented in Java |
| [ray](https://github.com/perditioinc/ray) | — | — | Python | Ray is an AI compute engine. Ray consists of a core distributed runtime and a se… |
| [PerfKitBenchmarker](https://github.com/perditioinc/PerfKitBenchmarker) | — | — | Python | PerfKit Benchmarker (PKB) contains a set of benchmarks to measure and compare cl… |
| [aider](https://github.com/perditioinc/aider) | — | — | Python | aider is AI pair programming in your terminal |
| [weave](https://github.com/perditioinc/weave) | — | — | Python | Weave is a toolkit for developing AI-powered applications, built by Weights & Bi… |
| [guardrails_](https://github.com/perditioinc/guardrails_) | — | — | Python | Adding guardrails to large language models. |
| [archestra](https://github.com/perditioinc/archestra) | — | — | TypeScript | Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator |
| [garak](https://github.com/perditioinc/garak) | — | — | HTML | the LLM vulnerability scanner |
| [chroma](https://github.com/perditioinc/chroma) | — | — | Rust | Open-source search and retrieval database for AI applications. |
| [milvus](https://github.com/perditioinc/milvus) | — | — | Go | Milvus is a high-performance, cloud-native vector database built for scalable ve… |
| [nginx](https://github.com/perditioinc/nginx) | — | — | C | The official NGINX Open Source repository. |
| [proxmark3](https://github.com/perditioinc/proxmark3) | — | — | C | Iceman Fork - Proxmark3 |
| [renode](https://github.com/perditioinc/renode) | — | — | RobotFramework | Renode - Antmicro's open source simulation and virtual development framework for… |
| [netdata](https://github.com/perditioinc/netdata) | — | — | C | The fastest path to AI-powered full stack observability, even for lean teams. |
| [jq](https://github.com/perditioinc/jq) | — | — | C | Command-line JSON processor |
| [git](https://github.com/perditioinc/git) | — | — | C | Git Source Code Mirror - This is a publish-only repository but pull requests can… |
| [redis](https://github.com/perditioinc/redis) | — | — | C | For developers, who are building real-time data-driven applications, Redis is th… |
| [sbox-public](https://github.com/perditioinc/sbox-public) | — | — | C# | s&box is a modern game engine, built on Valve's Source 2 and the latest .NET tec… |
| [mcp](https://github.com/perditioinc/mcp) | — | — | C# | Catalog of official Microsoft MCP (Model Context Protocol) server implementation… |
| [server](https://github.com/perditioinc/server) | — | — | C# | Bitwarden infrastructure/backend (API, database, Docker, etc). |
| [unity-mcp](https://github.com/perditioinc/unity-mcp) | — | — | C# | Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to inte… |
| [PowerShell](https://github.com/perditioinc/PowerShell) | — | — | C# | PowerShell for every system! |
| [FluentFlyout](https://github.com/perditioinc/FluentFlyout) | — | — | C# | The modern Flyout app for Windows 11, built with Fluent 2 Design principles. Med… |
| [QtScrcpy](https://github.com/perditioinc/QtScrcpy) | — | — | C++ | Android real-time display control software |
| [ESP32-Bus-Pirate](https://github.com/perditioinc/ESP32-Bus-Pirate) | — | — | C++ | A Hardware Hacking Tool with Web-Based CLI That Speaks Every Protocol  |
| [REFramework](https://github.com/perditioinc/REFramework) | — | — | C++ | Mod loader, scripting platform, and VR support for all RE Engine games |
| [Files](https://github.com/perditioinc/Files) | — | — | C# | A modern file manager that helps users organize their files and folders. |
| [Lean](https://github.com/perditioinc/Lean) | — | — | C# | Lean Algorithmic Trading Engine by QuantConnect (Python, C#) |
| [NanaZip](https://github.com/perditioinc/NanaZip) | — | — | C++ | The 7-Zip derivative intended for the modern Windows experience |
| [WSL](https://github.com/perditioinc/WSL) | — | — | C++ | Windows Subsystem for Linux |
| [ladybird](https://github.com/perditioinc/ladybird) | — | — | C++ | Truly independent web browser |
| [amnezia-client](https://github.com/perditioinc/amnezia-client) | — | — | C++ | Amnezia VPN Client (Desktop+Mobile) |
| [LichtFeld-Studio](https://github.com/perditioinc/LichtFeld-Studio) | — | — | C++ | LichtFeld Studio: Where reality and the digital world blend. |
| [ppsspp](https://github.com/perditioinc/ppsspp) | — | — | C++ | A PSP emulator for Android, Windows, Mac and Linux, written in C++. Want to cont… |
| [mlx](https://github.com/perditioinc/mlx) | — | — | C++ | MLX: An array framework for Apple silicon |

## Top Repos by Stars

Upstream repos with the most stars, tracked in this dataset.

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

## Data Files

| File | Description |
|------|-------------|
| `data/index.json` | Counts + metadata (tiny, always fast) |
| `data/recent.json` | Repos pushed in last 7 days (max 500) |
| `data/top_starred.json` | Top 100 by stars |
| `data/by_language/*.json` | One file per language |
| `data/by_category/*.json` | One file per category/topic _(empty until ingestion runs)_ |
| `data/full/repos_NNNN.json` | Full dataset, up to 10K repos per file |

## Platform

This dataset powers [reporium.com](https://reporium.com) — search and discovery for AI development tools.

Source data: [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db)

## License

Data is sourced from the GitHub API. MIT license.
