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
| Last updated | Updated less than 1h ago |

Data is fetched nightly from GitHub via GraphQL and written to partitioned JSON files
in [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db).

## Perditio Projects

10 repositories built and maintained by Perditio.

| Repo | Description | Stars | Language | Last Active |
|------|-------------|------:|----------|-------------|
| [reporium](https://github.com/perditioinc/reporium) | Your GitHub repos as a living AI-native knowledge graph library tool - an AI trend intelligence system that speaks to the people who need to understand what developers are building. Your curation, your lens, your industry perspective. Insights compounds, getting smarter every day. | 1 | TypeScript | 2026-03-18 |
| [reporium-api](https://github.com/perditioinc/reporium-api) | Backend API for Reporium : read/write access to repository database, designed for public queries and private ingestion updates. Gatekeeper API that talks to the database, handles authorized writes, serves data to clients/frontends. Public-facing, but writes are only authorized. | 1 | Python | 2026-03-15 |
| [reporium-ingestion](https://github.com/perditioinc/reporium-ingestion) | Local data ingestion and analysis scripts for Reporium : fetch, process, and generate embeddings for repositories, communicating with Reporium API. AI-native analysis, embeddings, scraping, tagging. Pushes updates to API. Standalone and private by default. | 1 | Python | 2026-03-16 |
| [forksync](https://github.com/perditioinc/forksync) | Tooling ⚙️: Keep your GitHub forks updated automatically. Runs nightly. | 1 | Python | 2026-03-19 |
| [portfolio](https://github.com/perditioinc/portfolio) | Portfolio of AI discovery tools, developer tooling, and automation systems built by Kim Loza | 1 | Python | 2026-03-19 |
| [reporium-db](https://github.com/perditioinc/reporium-db) | Nightly GitHub metadata sync — powers reporium.com. Supports 100K repos via GraphQL tiers, checkpointing, and partitioned output. | 1 | Python | 2026-03-19 |
| [reporium-dataset](https://github.com/perditioinc/reporium-dataset) | Public dataset mirror for reporium.com — nightly-updated AI dev tool stats from reporium-db. | 1 | Python | 2026-03-19 |
| [reporium-roadmap](https://github.com/perditioinc/reporium-roadmap) | Public product roadmap for reporium.com — auto-updated nightly with live GitHub stats. | 1 | Python | 2026-03-19 |
| [reporium-metrics](https://github.com/perditioinc/reporium-metrics) | Platform performance tracking over time — ASCII trend charts, nightly collection. | 1 | Python | 2026-03-19 |
| [repo-intelligence](https://github.com/perditioinc/repo-intelligence) | Score any GitHub repo 0-100 — README, activity, community, CI. Pip-installable. | 1 | Python | 2026-03-19 |

## Forked AI Repos

> Showing top 100 of 808 forked repos (by upstream stars). Full dataset: [`data/full/repos_0000.json`](https://github.com/perditioinc/reporium-db/blob/main/data/full/repos_0000.json)

| Fork | Forked From | Stars | Forks | Language | Description |
|------|------------|------:|------:|----------|-------------|
| [awesome](https://github.com/perditioinc/awesome) | [sindresorhus](https://github.com/sindresorhus) | 446,773 | 0 | — | 😎 Awesome lists about all kinds of interesting topics |
| [public-apis](https://github.com/perditioinc/public-apis) | [public-apis](https://github.com/public-apis) | 412,000 | 0 | Python | A collective list of free APIs |
| [openclaw](https://github.com/perditioinc/openclaw) | [openclaw](https://github.com/openclaw) | 323,515 | 0 | TypeScript | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞  |
| [awesome-python](https://github.com/perditioinc/awesome-python) | [vinta](https://github.com/vinta) | 287,863 | 0 | Python | An opinionated list of awesome Python frameworks, libraries, software and resour… |
| [project-based-learning](https://github.com/perditioinc/project-based-learning) | [practical-tutorials](https://github.com/practical-tutorials) | 261,212 | 0 | — | Curated list of project-based tutorials |
| [Python](https://github.com/perditioinc/Python) | [TheAlgorithms](https://github.com/TheAlgorithms) | 218,804 | 0 | Python | All Algorithms implemented in Python |
| [tensorflow](https://github.com/perditioinc/tensorflow) | [tensorflow](https://github.com/tensorflow) | 194,210 | 0 | C++ | An Open Source Machine Learning Framework for Everyone |
| [vscode](https://github.com/perditioinc/vscode) | [microsoft](https://github.com/microsoft) | 182,811 | 0 | TypeScript | Visual Studio Code |
| [AutoGPT](https://github.com/perditioinc/AutoGPT) | [Significant-Gravitas](https://github.com/Significant-Gravitas) | 182,590 | 0 | Python | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our… |
| [Python-100-Days](https://github.com/perditioinc/Python-100-Days) | [jackfrued](https://github.com/jackfrued) | 179,800 | 0 | Jupyter Notebook | Python - 100天从新手到大师 |
| [ollama](https://github.com/perditioinc/ollama) | [ollama](https://github.com/ollama) | 165,517 | 0 | Go | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemm… |
| [stable-diffusion-webui](https://github.com/perditioinc/stable-diffusion-webui) | [AUTOMATIC1111](https://github.com/AUTOMATIC1111) | 161,852 | 0 | Python | Stable Diffusion web UI |
| [transformers](https://github.com/perditioinc/transformers) | [huggingface](https://github.com/huggingface) | 158,052 | 0 | Python | 🤗 Transformers: the model-definition framework for state-of-the-art machine lear… |
| [langflow](https://github.com/perditioinc/langflow) | [langflow-ai](https://github.com/langflow-ai) | 145,863 | 0 | Python | Langflow is a powerful tool for building and deploying AI-powered agents and wor… |
| [dify](https://github.com/perditioinc/dify) | [langgenius](https://github.com/langgenius) | 133,464 | 0 | TypeScript | Production-ready platform for agentic workflow development. |
| [system-prompts-and-models-of-ai-tools](https://github.com/perditioinc/system-prompts-and-models-of-ai-tools) | [x1xhlol](https://github.com/x1xhlol) | 131,962 | 0 | — | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Juni… |
| [PowerToys](https://github.com/perditioinc/PowerToys) | [microsoft](https://github.com/microsoft) | 130,673 | 0 | C# | Microsoft PowerToys is a collection of utilities that supercharge productivity a… |
| [langchain](https://github.com/perditioinc/langchain) | [langchain-ai](https://github.com/langchain-ai) | 130,123 | 0 | Python | The agent engineering platform |
| [open-webui](https://github.com/perditioinc/open-webui) | [open-webui](https://github.com/open-webui) | 127,770 | 0 | Python | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [generative-ai-for-beginners](https://github.com/perditioinc/generative-ai-for-beginners) | [microsoft](https://github.com/microsoft) | 108,234 | 0 | Jupyter Notebook | 21 Lessons, Get Started Building with Generative AI  |
| [TypeScript_](https://github.com/perditioinc/TypeScript_) | [microsoft](https://github.com/microsoft) | 108,201 | 0 | TypeScript | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [godot](https://github.com/perditioinc/godot) | [godotengine](https://github.com/godotengine) | 108,086 | 0 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| [ComfyUI](https://github.com/perditioinc/ComfyUI) | [Comfy-Org](https://github.com/Comfy-Org) | 106,286 | 0 | Python | The most powerful and modular diffusion model GUI, api and backend with a graph/… |
| [awesome-llm-apps](https://github.com/perditioinc/awesome-llm-apps) | [Shubhamsaboo](https://github.com/Shubhamsaboo) | 102,771 | 0 | Python | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, G… |
| [terminal](https://github.com/perditioinc/terminal) | [microsoft](https://github.com/microsoft) | 102,249 | 0 | C++ | The new Windows Terminal and the original Windows console host, all in the same … |
| [DeepSeek-V3](https://github.com/perditioinc/DeepSeek-V3) | [deepseek-ai](https://github.com/deepseek-ai) | 102,224 | 0 | Python | — |
| [llama.cpp](https://github.com/perditioinc/llama.cpp) | [ggml-org](https://github.com/ggml-org) | 98,506 | 0 | C++ | LLM inference in C/C++ |
| [pytorch](https://github.com/perditioinc/pytorch) | [pytorch](https://github.com/pytorch) | 98,372 | 0 | Python | Tensors and Dynamic neural networks in Python with strong GPU acceleration |
| [gemini-cli](https://github.com/perditioinc/gemini-cli) | [google-gemini](https://github.com/google-gemini) | 98,301 | 0 | TypeScript | An open-source AI agent that brings the power of Gemini directly into your termi… |
| [skills_](https://github.com/perditioinc/skills_) | [anthropics](https://github.com/anthropics) | 97,106 | 0 | Python | Public repository for Agent Skills |
| [superpowers](https://github.com/perditioinc/superpowers) | [obra](https://github.com/obra) | 96,833 | 0 | Shell | An agentic skills framework & software development methodology that works. |
| [whisper](https://github.com/perditioinc/whisper) | [openai](https://github.com/openai) | 96,202 | 0 | Python | Robust Speech Recognition via Large-Scale Weak Supervision |
| [Web-Dev-For-Beginners](https://github.com/perditioinc/Web-Dev-For-Beginners) | [microsoft](https://github.com/microsoft) | 95,432 | 0 | JavaScript | 24 Lessons, 12 Weeks, Get Started as a Web Developer |
| [immich](https://github.com/perditioinc/immich) | [immich-app](https://github.com/immich-app) | 95,101 | 0 | TypeScript | High performance self-hosted photo and video management solution. |
| [markitdown](https://github.com/perditioinc/markitdown) | [microsoft](https://github.com/microsoft) | 90,954 | 0 | Python | Python tool for converting files and office documents to Markdown. |
| [LLMs-from-scratch](https://github.com/perditioinc/LLMs-from-scratch) | [rasbt](https://github.com/rasbt) | 88,675 | 0 | Jupyter Notebook | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step |
| [hugo](https://github.com/perditioinc/hugo) | [gohugoio](https://github.com/gohugoio) | 87,148 | 0 | Go | The world’s fastest framework for building websites. |
| [everything-claude-code](https://github.com/perditioinc/everything-claude-code) | [affaan-m](https://github.com/affaan-m) | 86,057 | 0 | JavaScript | The agent harness performance optimization system. Skills, instincts, memory, se… |
| [ML-For-Beginners](https://github.com/perditioinc/ML-For-Beginners) | [microsoft](https://github.com/microsoft) | 84,560 | 0 | Jupyter Notebook | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all |
| [playwright](https://github.com/perditioinc/playwright) | [microsoft](https://github.com/microsoft) | 84,525 | 0 | TypeScript | Playwright is a framework for Web Testing and Automation. It allows testing Chro… |
| [animate.css](https://github.com/perditioinc/animate.css) | [animate-css](https://github.com/animate-css) | 82,627 | 0 | CSS | 🍿 A cross-browser library of CSS animations. As easy to use as an easy thing. |
| [browser-use](https://github.com/perditioinc/browser-use) | [browser-use](https://github.com/browser-use) | 81,242 | 0 | Python | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. |
| [claude-code](https://github.com/perditioinc/claude-code) | [anthropics](https://github.com/anthropics) | 79,777 | 0 | Shell | Claude Code is an agentic coding tool that lives in your terminal, understands y… |
| [vite](https://github.com/perditioinc/vite) | [vitejs](https://github.com/vitejs) | 79,163 | 0 | TypeScript | Next generation frontend tooling. It's fast! |
| [netdata](https://github.com/perditioinc/netdata) | [netdata](https://github.com/netdata) | 78,124 | 0 | C | The fastest path to AI-powered full stack observability, even for lean teams. |
| [cs-video-courses](https://github.com/perditioinc/cs-video-courses) | [Developer-Y](https://github.com/Developer-Y) | 77,322 | 0 | — | List of Computer Science courses with video lectures. |
| [gpt4all](https://github.com/perditioinc/gpt4all) | [nomic-ai](https://github.com/nomic-ai) | 77,233 | 0 | C++ | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial … |
| [llm-course](https://github.com/perditioinc/llm-course) | [mlabonne](https://github.com/mlabonne) | 77,014 | 0 | — | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebook… |
| [ragflow](https://github.com/perditioinc/ragflow) | [infiniflow](https://github.com/infiniflow) | 75,456 | 0 | TypeScript | RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine tha… |
| [vllm](https://github.com/perditioinc/vllm) | [vllm-project](https://github.com/vllm-project) | 73,598 | 0 | Python | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [redis](https://github.com/perditioinc/redis) | [redis](https://github.com/redis) | 73,459 | 0 | C | For developers, who are building real-time data-driven applications, Redis is th… |
| [tesseract](https://github.com/perditioinc/tesseract) | [tesseract-ocr](https://github.com/tesseract-ocr) | 72,990 | 0 | C++ | Tesseract Open Source OCR Engine (main repository) |
| [stable-diffusion](https://github.com/perditioinc/stable-diffusion) | [CompVis](https://github.com/CompVis) | 72,713 | 0 | Jupyter Notebook | A latent text-to-image diffusion model |
| [PaddleOCR](https://github.com/perditioinc/PaddleOCR) | [PaddlePaddle](https://github.com/PaddlePaddle) | 72,582 | 0 | Python | Turn any PDF or image document into structured data for your AI. A powerful, lig… |
| [openai-cookbook](https://github.com/perditioinc/openai-cookbook) | [openai](https://github.com/openai) | 72,214 | 0 | Jupyter Notebook | Examples and guides for using the OpenAI API |
| [awesome-machine-learning](https://github.com/perditioinc/awesome-machine-learning) | [josephmisiti](https://github.com/josephmisiti) | 72,030 | 0 | Python | A curated list of awesome Machine Learning frameworks, libraries and software. |
| [Prompt-Engineering-Guide](https://github.com/perditioinc/Prompt-Engineering-Guide) | [dair-ai](https://github.com/dair-ai) | 71,903 | 0 | MDX | 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, conte… |
| [strapi](https://github.com/perditioinc/strapi) | [strapi](https://github.com/strapi) | 71,646 | 0 | TypeScript | 🚀 Strapi is the leading open-source headless CMS. It’s 100% JavaScript/TypeScrip… |
| [openhands](https://github.com/perditioinc/openhands) | [OpenHands](https://github.com/OpenHands) | 69,369 | 0 | Python | 🙌 OpenHands: AI-Driven Development |
| [LLaMA-Factory](https://github.com/perditioinc/LLaMA-Factory) | [hiyouga](https://github.com/hiyouga) | 68,678 | 0 | Python | Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) |
| [daytona](https://github.com/perditioinc/daytona) | [daytonaio](https://github.com/daytonaio) | 67,080 | 0 | TypeScript | Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code |
| [codex](https://github.com/perditioinc/codex) | [openai](https://github.com/openai) | 66,194 | 0 | Rust | Lightweight coding agent that runs in your terminal |
| [annotated_deep_learning_paper_implementations](https://github.com/perditioinc/annotated_deep_learning_paper_implementations) | [labmlai](https://github.com/labmlai) | 66,033 | 0 | Python | 🧑‍🏫 60+ Implementations/tutorials of deep learning papers with side-by-side note… |
| [MetaGPT](https://github.com/perditioinc/MetaGPT) | [FoundationAgents](https://github.com/FoundationAgents) | 65,542 | 0 | Python | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language… |
| [scikit-learn](https://github.com/perditioinc/scikit-learn) | [scikit-learn](https://github.com/scikit-learn) | 65,425 | 0 | Python | scikit-learn: machine learning in Python |
| [Java](https://github.com/perditioinc/Java) | [TheAlgorithms](https://github.com/TheAlgorithms) | 65,232 | 0 | Java | All Algorithms implemented in Java |
| [ladybird](https://github.com/perditioinc/ladybird) | [LadybirdBrowser](https://github.com/LadybirdBrowser) | 61,389 | 0 | C++ | Truly independent web browser |
| [git](https://github.com/perditioinc/git) | [git](https://github.com/git) | 59,762 | 0 | C | Git Source Code Mirror - This is a publish-only repository but pull requests can… |
| [cline](https://github.com/perditioinc/cline) | [cline](https://github.com/cline) | 59,133 | 0 | TypeScript | Autonomous coding agent right in your IDE, capable of creating/editing files, ex… |
| [llm-app](https://github.com/perditioinc/llm-app) | [pathwaycom](https://github.com/pathwaycom) | 57,377 | 0 | Jupyter Notebook | Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with l… |
| [MinerU](https://github.com/perditioinc/MinerU) | [opendatalab](https://github.com/opendatalab) | 56,532 | 0 | Python | Transforms complex documents like PDFs into LLM-ready markdown/JSON for your Age… |
| [anything-llm](https://github.com/perditioinc/anything-llm) | [Mintplex-Labs](https://github.com/Mintplex-Labs) | 56,437 | 0 | JavaScript | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-… |
| [unsloth](https://github.com/perditioinc/unsloth) | [unslothai](https://github.com/unslothai) | 56,047 | 0 | Python | Fine-tuning & Reinforcement Learning for LLMs. 🦥 Train OpenAI gpt-oss, DeepSeek,… |
| [autogen](https://github.com/perditioinc/autogen) | [microsoft](https://github.com/microsoft) | 55,859 | 0 | Python | A programming framework for agentic AI |
| [ai-agents-for-beginners](https://github.com/perditioinc/ai-agents-for-beginners) | [microsoft](https://github.com/microsoft) | 54,410 | 0 | Jupyter Notebook | 12 Lessons to Get Started Building AI Agents |
| [agency-agents](https://github.com/perditioinc/agency-agents) | [msitarzewski](https://github.com/msitarzewski) | 54,377 | 0 | Shell | A complete AI agency at your fingertips - From frontend wizards to Reddit commun… |
| [segment-anything](https://github.com/perditioinc/segment-anything) | [facebookresearch](https://github.com/facebookresearch) | 53,704 | 0 | Jupyter Notebook | The repository provides code for running inference with the SegmentAnything Mode… |
| [material-design-icons](https://github.com/perditioinc/material-design-icons) | [google](https://github.com/google) | 52,994 | 0 | — | Material Design icons by Google (Material Symbols) |
| [free-certifications](https://github.com/perditioinc/free-certifications) | [cloudcommunity](https://github.com/cloudcommunity) | 52,764 | 0 | — | A curated list of free courses with certifications. Also available at https://fr… |
| [PowerShell](https://github.com/perditioinc/PowerShell) | [PowerShell](https://github.com/PowerShell) | 51,914 | 0 | C# | PowerShell for every system! |
| [guava](https://github.com/perditioinc/guava) | [google](https://github.com/google) | 51,506 | 0 | Java | Google core libraries for Java |
| [mem0](https://github.com/perditioinc/mem0) | [mem0ai](https://github.com/mem0ai) | 50,335 | 0 | Python | Universal memory layer for AI Agents |
| [100-Days-Of-ML-Code](https://github.com/perditioinc/100-Days-Of-ML-Code) | [Avik-Jain](https://github.com/Avik-Jain) | 49,968 | 0 | — | 100 Days of ML Coding |
| [nanochat](https://github.com/perditioinc/nanochat) | [karpathy](https://github.com/karpathy) | 49,445 | 0 | Python | The best ChatGPT that $100 can buy. |
| [ai-hedge-fund](https://github.com/perditioinc/ai-hedge-fund) | [virattt](https://github.com/virattt) | 49,330 | 0 | Python | An AI Hedge Fund Team |
| [llama_index](https://github.com/perditioinc/llama_index) | [run-llama](https://github.com/run-llama) | 47,780 | 0 | Python | LlamaIndex is the leading document agent and OCR platform |
| [PythonDataScienceHandbook](https://github.com/perditioinc/PythonDataScienceHandbook) | [jakevdp](https://github.com/jakevdp) | 47,075 | 0 | Jupyter Notebook | Python Data Science Handbook: full text in Jupyter Notebooks |
| [Made-With-ML](https://github.com/perditioinc/Made-With-ML) | [GokuMohandas](https://github.com/GokuMohandas) | 46,849 | 0 | Jupyter Notebook | Learn how to design, develop, deploy and iterate on production-grade ML applicat… |
| [crewAI](https://github.com/perditioinc/crewAI) | [crewAIInc](https://github.com/crewAIInc) | 46,503 | 0 | Python | Framework for orchestrating role-playing, autonomous AI agents. By fostering col… |
| [MediaCrawler](https://github.com/perditioinc/MediaCrawler) | [NanmiCoder](https://github.com/NanmiCoder) | 46,144 | 0 | Python | 小红书笔记 - 评论爬虫、抖音视频 - 评论爬虫、快手视频 - 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬… |
| [AI-For-Beginners](https://github.com/perditioinc/AI-For-Beginners) | [microsoft](https://github.com/microsoft) | 46,132 | 0 | Jupyter Notebook | 12 Weeks, 24 Lessons, AI for All! |
| [awesome-claude-skills](https://github.com/perditioinc/awesome-claude-skills) | [ComposioHQ](https://github.com/ComposioHQ) | 45,829 | 0 | Python | A curated list of awesome Claude Skills, resources, and tools for customizing Cl… |
| [monaco-editor](https://github.com/perditioinc/monaco-editor) | [microsoft](https://github.com/microsoft) | 45,777 | 0 | JavaScript | A browser based code editor |
| [LocalAI](https://github.com/perditioinc/LocalAI) | [mudler](https://github.com/mudler) | 43,983 | 0 | Go | :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hos… |
| [milvus](https://github.com/perditioinc/milvus) | [milvus-io](https://github.com/milvus-io) | 43,372 | 0 | Go | Milvus is a high-performance, cloud-native vector database built for scalable ve… |
| [tmux](https://github.com/perditioinc/tmux) | [tmux](https://github.com/tmux) | 43,223 | 0 | C | tmux source code |
| [Umi-OCR](https://github.com/perditioinc/Umi-OCR) | [hiroi-sora](https://github.com/hiroi-sora) | 42,640 | 0 | Python | OCR software, free and offline. 开源、免费的离线OCR软件。支持截屏/批量导入图片，PDF文档识别，排除水印/页眉页脚，扫描/生… |
| [Files](https://github.com/perditioinc/Files) | [files-community](https://github.com/files-community) | 42,476 | 0 | C# | A modern file manager that helps users organize their files and folders. |
| [autoresearch](https://github.com/perditioinc/autoresearch) | [karpathy](https://github.com/karpathy) | 42,396 | 0 | Python | AI agents running research on single-GPU nanochat training automatically |
| [aider](https://github.com/perditioinc/aider) | [Aider-AI](https://github.com/Aider-AI) | 42,126 | 0 | Python | aider is AI pair programming in your terminal |

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
