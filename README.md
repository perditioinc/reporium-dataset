# Reporium Dataset

> Open dataset of AI development tool repositories — updated nightly from [reporium-api](https://github.com/perditioinc/reporium-api).

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

## Perditio Projects

10 repositories built and maintained by Perditio.

| Repo | Description | Language | Last Active |
|------|-------------|----------|-------------|
| [perditioinc/reporium](https://github.com/perditioinc/reporium) | Your GitHub repos as a living AI-native knowledge graph library tool - an AI trend intelligence system that speaks to the people who need to understand what developers are building. Your curation, your lens, your industry perspective. Insights compounds, getting smarter every day. | TypeScript | 2026-03-18 |
| [perditioinc/reporium-api](https://github.com/perditioinc/reporium-api) | Backend API for Reporium : read/write access to repository database, designed for public queries and private ingestion updates. Gatekeeper API that talks to the database, handles authorized writes, serves data to clients/frontends. Public-facing, but writes are only authorized. | Python | 2026-03-15 |
| [perditioinc/reporium-ingestion](https://github.com/perditioinc/reporium-ingestion) | Local data ingestion and analysis scripts for Reporium : fetch, process, and generate embeddings for repositories, communicating with Reporium API. AI-native analysis, embeddings, scraping, tagging. Pushes updates to API. Standalone and private by default. | Python | 2026-03-16 |
| [perditioinc/forksync](https://github.com/perditioinc/forksync) | Tooling ⚙️: Keep your GitHub forks updated automatically. Runs nightly. | Python | 2026-03-19 |
| [perditioinc/portfolio](https://github.com/perditioinc/portfolio) | Portfolio of AI discovery tools, developer tooling, and automation systems built by Kim Loza | Python | 2026-03-19 |
| [perditioinc/reporium-db](https://github.com/perditioinc/reporium-db) | Nightly GitHub metadata sync — powers reporium.com. Supports 100K repos via GraphQL tiers, checkpointing, and partitioned output. | Python | 2026-03-19 |
| [perditioinc/reporium-dataset](https://github.com/perditioinc/reporium-dataset) | Public dataset mirror for reporium.com — nightly-updated AI dev tool stats from reporium-db. | Python | 2026-03-19 |
| [perditioinc/reporium-roadmap](https://github.com/perditioinc/reporium-roadmap) | Public product roadmap for reporium.com — auto-updated nightly with live GitHub stats. | Python | 2026-03-19 |
| [perditioinc/reporium-metrics](https://github.com/perditioinc/reporium-metrics) | Platform performance tracking over time — ASCII trend charts, nightly collection. | Python | 2026-03-19 |
| [perditioinc/repo-intelligence](https://github.com/perditioinc/repo-intelligence) | Score any GitHub repo 0-100 — README, activity, community, CI. Pip-installable. | Python | 2026-03-19 |

## Forked AI Repos

| Fork | Stars | Forks | Language | Description |
|------|------:|------:|----------|-------------|
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 446,773 | — | — | 😎 Awesome lists about all kinds of interesting topics |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 412,000 | — | Python | A collective list of free APIs |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 323,515 | — | TypeScript | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞  |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 287,863 | — | Python | An opinionated list of awesome Python frameworks, libraries, software and resources. |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 261,212 | — | — | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 218,804 | — | Python | All Algorithms implemented in Python |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 194,210 | — | C++ | An Open Source Machine Learning Framework for Everyone |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 182,811 | — | TypeScript | Visual Studio Code |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 182,590 | — | Python | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. |
| [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) | 179,800 | — | Jupyter Notebook | Python - 100天从新手到大师 |
| [ollama/ollama](https://github.com/ollama/ollama) | 165,517 | — | Go | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. |
| [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 161,852 | — | Python | Stable Diffusion web UI |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 158,052 | — | Python | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.  |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 145,863 | — | Python | Langflow is a powerful tool for building and deploying AI-powered agents and workflows. |
| [langgenius/dify](https://github.com/langgenius/dify) | 133,464 | — | TypeScript | Production-ready platform for agentic workflow development. |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 131,962 | — | — | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models |
| [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 130,673 | — | C# | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 130,123 | — | Python | The agent engineering platform |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 127,770 | — | Python | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 108,234 | — | Jupyter Notebook | 21 Lessons, Get Started Building with Generative AI  |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 108,201 | — | TypeScript | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [godotengine/godot](https://github.com/godotengine/godot) | 108,086 | — | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 106,286 | — | Python | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 102,771 | — | Python | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 102,249 | — | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | 102,224 | — | Python | — |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 98,506 | — | C++ | LLM inference in C/C++ |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | 98,372 | — | Python | Tensors and Dynamic neural networks in Python with strong GPU acceleration |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 98,301 | — | TypeScript | An open-source AI agent that brings the power of Gemini directly into your terminal. |
| [anthropics/skills](https://github.com/anthropics/skills) | 97,106 | — | Python | Public repository for Agent Skills |
| [obra/superpowers](https://github.com/obra/superpowers) | 96,833 | — | Shell | An agentic skills framework & software development methodology that works. |
| [openai/whisper](https://github.com/openai/whisper) | 96,202 | — | Python | Robust Speech Recognition via Large-Scale Weak Supervision |
| [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 95,432 | — | JavaScript | 24 Lessons, 12 Weeks, Get Started as a Web Developer |
| [immich-app/immich](https://github.com/immich-app/immich) | 95,101 | — | TypeScript | High performance self-hosted photo and video management solution. |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 90,954 | — | Python | Python tool for converting files and office documents to Markdown. |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 88,675 | — | Jupyter Notebook | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step |
| [gohugoio/hugo](https://github.com/gohugoio/hugo) | 87,148 | — | Go | The world’s fastest framework for building websites. |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | 86,057 | — | JavaScript | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. |
| [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 84,560 | — | Jupyter Notebook | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 84,525 | — | TypeScript | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API.  |
| [animate-css/animate.css](https://github.com/animate-css/animate.css) | 82,627 | — | CSS | 🍿 A cross-browser library of CSS animations. As easy to use as an easy thing. |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 81,242 | — | Python | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 79,777 | — | Shell | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [vitejs/vite](https://github.com/vitejs/vite) | 79,163 | — | TypeScript | Next generation frontend tooling. It's fast! |
| [netdata/netdata](https://github.com/netdata/netdata) | 78,124 | — | C | The fastest path to AI-powered full stack observability, even for lean teams. |
| [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | 77,322 | — | — | List of Computer Science courses with video lectures. |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 77,233 | — | C++ | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 77,014 | — | — | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 75,456 | — | TypeScript | RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 73,598 | — | Python | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [redis/redis](https://github.com/redis/redis) | 73,459 | — | C | For developers, who are building real-time data-driven applications, Redis is the preferred, fastest, and most feature-rich cache, data structure server, and document and vector query engine. |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | 72,990 | — | C++ | Tesseract Open Source OCR Engine (main repository) |
| [CompVis/stable-diffusion](https://github.com/CompVis/stable-diffusion) | 72,713 | — | Jupyter Notebook | A latent text-to-image diffusion model |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 72,582 | — | Python | Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages. |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 72,214 | — | Jupyter Notebook | Examples and guides for using the OpenAI API |
| [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 72,030 | — | Python | A curated list of awesome Machine Learning frameworks, libraries and software. |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 71,903 | — | MDX | 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents. |
| [strapi/strapi](https://github.com/strapi/strapi) | 71,646 | — | TypeScript | 🚀 Strapi is the leading open-source headless CMS. It’s 100% JavaScript/TypeScript, fully customizable, and developer-first. |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 69,369 | — | Python | 🙌 OpenHands: AI-Driven Development |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | 68,678 | — | Python | Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) |
| [daytonaio/daytona](https://github.com/daytonaio/daytona) | 67,080 | — | TypeScript | Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code |
| [openai/codex](https://github.com/openai/codex) | 66,194 | — | Rust | Lightweight coding agent that runs in your terminal |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | 66,033 | — | Python | 🧑‍🏫 60+ Implementations/tutorials of deep learning papers with side-by-side notes 📝; including transformers (original, xl, switch, feedback, vit, ...), optimizers (adam, adabelief, sophia, ...), gans(cyclegan, stylegan2, ...), 🎮 reinforcement learning (ppo, dqn), capsnet, distillation, ... 🧠 |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 65,542 | — | Python | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65,425 | — | Python | scikit-learn: machine learning in Python |
| [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) | 65,232 | — | Java | All Algorithms implemented in Java |
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | 61,389 | — | C++ | Truly independent web browser |
| [git/git](https://github.com/git/git) | 59,762 | — | C | Git Source Code Mirror - This is a publish-only repository but pull requests can be turned into patches to the mailing list via GitGitGadget (https://gitgitgadget.github.io/). Please follow Documentation/SubmittingPatches procedure for any of your improvements. |
| [cline/cline](https://github.com/cline/cline) | 59,133 | — | TypeScript | Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. |
| [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | 57,377 | — | Jupyter Notebook | Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with live data. 🐳Docker-friendly.⚡Always in sync with Sharepoint, Google Drive, S3, Kafka, PostgreSQL, real-time data APIs, and more. |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | 56,532 | — | Python | Transforms complex documents like PDFs into LLM-ready markdown/JSON for your Agentic workflows. |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 56,437 | — | JavaScript | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more. |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 56,047 | — | Python | Fine-tuning & Reinforcement Learning for LLMs. 🦥 Train OpenAI gpt-oss, DeepSeek, Qwen, Llama, Gemma, TTS 2x faster with 70% less VRAM. |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 55,859 | — | Python | A programming framework for agentic AI |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 54,410 | — | Jupyter Notebook | 12 Lessons to Get Started Building AI Agents |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 54,377 | — | Shell | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables. |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 53,704 | — | Jupyter Notebook | The repository provides code for running inference with the SegmentAnything Model (SAM), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. |
| [google/material-design-icons](https://github.com/google/material-design-icons) | 52,994 | — | — | Material Design icons by Google (Material Symbols) |
| [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | 52,764 | — | — | A curated list of free courses with certifications. Also available at https://free-certifications.com/ |
| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | 51,914 | — | C# | PowerShell for every system! |
| [google/guava](https://github.com/google/guava) | 51,506 | — | Java | Google core libraries for Java |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 50,335 | — | Python | Universal memory layer for AI Agents |
| [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) | 49,968 | — | — | 100 Days of ML Coding |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | 49,445 | — | Python | The best ChatGPT that $100 can buy. |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | 49,330 | — | Python | An AI Hedge Fund Team |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 47,780 | — | Python | LlamaIndex is the leading document agent and OCR platform |
| [jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) | 47,075 | — | Jupyter Notebook | Python Data Science Handbook: full text in Jupyter Notebooks |
| [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) | 46,849 | — | Jupyter Notebook | Learn how to design, develop, deploy and iterate on production-grade ML applications. |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 46,503 | — | Python | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 46,144 | — | Python | 小红书笔记 - 评论爬虫、抖音视频 - 评论爬虫、快手视频 - 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫  - 知乎问答文章｜评论爬虫 |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 46,132 | — | Jupyter Notebook | 12 Weeks, 24 Lessons, AI for All! |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 45,829 | — | Python | A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows |
| [microsoft/monaco-editor](https://github.com/microsoft/monaco-editor) | 45,777 | — | JavaScript | A browser based code editor |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 43,983 | — | Go | :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 43,372 | — | Go | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search |
| [tmux/tmux](https://github.com/tmux/tmux) | 43,223 | — | C | tmux source code |
| [hiroi-sora/Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) | 42,640 | — | Python | OCR software, free and offline. 开源、免费的离线OCR软件。支持截屏/批量导入图片，PDF文档识别，排除水印/页眉页脚，扫描/生成二维码。内置多国语言库。 |
| [files-community/Files](https://github.com/files-community/Files) | 42,476 | — | C# | A modern file manager that helps users organize their files and folders. |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 42,396 | — | Python | AI agents running research on single-GPU nanochat training automatically |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 42,126 | — | Python | aider is AI pair programming in your terminal |
| [ray-project/ray](https://github.com/ray-project/ray) | 41,770 | — | Python | Ray is an AI compute engine. Ray consists of a core distributed runtime and a set of AI Libraries for accelerating ML workloads. |
| [janhq/jan](https://github.com/janhq/jan) | 41,146 | — | TypeScript | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | 40,570 | — | Jupyter Notebook | This is a repo with links to everything you'd ever want to learn about data engineering |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 40,021 | — | Go | Fabric is an open-source framework for augmenting humans using AI. It provides a modular system for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 39,573 | — | Python | Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardrails, loadbalancing and logging. [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM] |
| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 39,483 | — | Python | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | 39,464 | — | — | The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.🦞 |
| [google/styleguide](https://github.com/google/styleguide) | 39,107 | — | HTML | Style guides for Google-originated open-source projects |
| [suno-ai/bark](https://github.com/suno-ai/bark) | 39,044 | — | Jupyter Notebook | 🔊 Text-Prompted Generative Audio Model |
| [microsoft/qlib](https://github.com/microsoft/qlib) | 38,995 | — | Python | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 38,800 | — | Python | Build, run, manage agentic software at scale. |
| [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) | 38,788 | — | Python | Query Engine for AI Analytics: Build self-reasoning agents across all your live data |
| [google/googletest](https://github.com/google/googletest) | 38,371 | — | C++ | GoogleTest - Google Testing and Mocking Framework |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 38,180 | — | TypeScript | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | 38,138 | — | Rust | π RuView: WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without a single pixel of video.  |
| [Kong/insomnia](https://github.com/Kong/insomnia) | 38,098 | — | TypeScript | The open-source, cross-platform API client for GraphQL, REST, WebSockets, SSE and gRPC. With Cloud, Local and Git storage. |
| [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore) | 37,772 | — | C# | ASP.NET Core is a cross-platform .NET framework for building modern cloud-based web applications on Windows, Mac, or Linux. |
| [google-research/google-research](https://github.com/google-research/google-research) | 37,486 | — | Jupyter Notebook | Google Research |
| [openai/gym](https://github.com/openai/gym) | 37,103 | — | Python | A toolkit for developing and comparing reinforcement learning algorithms. |
| [reworkd/AgentGPT](https://github.com/reworkd/AgentGPT) | 35,846 | — | TypeScript | 🤖 Assemble, configure, and deploy autonomous AI Agents in your browser. |
| [microsoft/BitNet](https://github.com/microsoft/BitNet) | 35,680 | — | Python | Official inference framework for 1-bit LLMs |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | 35,295 | — | Jupyter Notebook | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [google/langextract](https://github.com/google/langextract) | 34,793 | — | Python | A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. |
| [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | 34,615 | — | Python | A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物 |
| [directus/directus](https://github.com/directus/directus) | 34,520 | — | TypeScript | The flexible backend for all your projects 🐰 Turn your DB into a headless CMS, admin panels, or apps with a custom UI, instant APIs, auth & more. |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 34,511 | — | TypeScript | 💖🧸 Self hosted, you-owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | 34,275 | — | Jupyter Notebook | 10 Weeks, 20 Lessons, Data Science for All! |
| [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe) | 34,200 | — | C++ | Cross-platform, customizable ML solutions for live and streaming media. |
| [TheAlgorithms/JavaScript](https://github.com/TheAlgorithms/JavaScript) | 34,089 | — | JavaScript | Algorithms and Data Structures implemented in JavaScript for beginners, following best practices. |
| [TheAlgorithms/C-Plus-Plus](https://github.com/TheAlgorithms/C-Plus-Plus) | 33,944 | — | C++ | Collection of various algorithms in mathematics, machine learning, computer science and physics implemented in C++ for educational purposes. |
| [jqlang/jq](https://github.com/jqlang/jq) | 33,855 | — | C | Command-line JSON processor |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 33,600 | — | Jupyter Notebook | Anthropic's Interactive Prompt Engineering Tutorial |
| [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | 32,985 | — | Python | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 32,980 | — | Python | TradingAgents: Multi-Agents LLM Financial Trading Framework |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 32,900 | — | Python | DSPy: The framework for programming—not prompting—language models |
| [openai/CLIP](https://github.com/openai/CLIP) | 32,866 | — | Jupyter Notebook | CLIP (Contrastive Language-Image Pretraining),  Predict the most relevant text snippet given an image |
| [datalab-to/marker](https://github.com/datalab-to/marker) | 32,798 | — | Python | Convert PDF to markdown + JSON quickly with high accuracy |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | 32,559 | — | TypeScript | Bash is all you need -  A nano Claude Code–like agent, built from 0 to 1 |
| [ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) | 32,309 | — | — | 500 AI Machine learning Deep learning Computer vision NLP Projects with code |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 32,274 | — | Jupyter Notebook | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |
| [continuedev/continue](https://github.com/continuedev/continue) | 31,937 | — | TypeScript | ⏩ Source-controlled AI checks, enforceable in CI. Powered by the open-source Continue CLI |
| [microsoft/MS-DOS](https://github.com/microsoft/MS-DOS) | 31,760 | — | Assembly | The original sources of MS-DOS 1.25, 2.0, and 4.0 for reference purposes |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 31,753 | — | Python | An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours. |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 31,604 | — | Python | A modular graph-based Retrieval-Augmented Generation (RAG) system |
| [microsoft/WSL](https://github.com/microsoft/WSL) | 31,452 | — | C++ | Windows Subsystem for Linux |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 31,086 | — | Python | 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl! |
| [microsoft/calculator](https://github.com/microsoft/calculator) | 30,871 | — | C++ | Windows Calculator: A simple yet powerful calculator that ships with Windows |
| [openai/openai-python](https://github.com/openai/openai-python) | 30,270 | — | Python | The official Python library for the OpenAI API |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 30,149 | — | TypeScript | Chrome DevTools for coding agents |
| [ageron/handson-ml2](https://github.com/ageron/handson-ml2) | 29,934 | — | Jupyter Notebook | A series of Jupyter notebooks that walk you through the fundamentals of Machine Learning and Deep Learning in Python using Scikit-Learn, Keras and TensorFlow 2. |
| [nginx/nginx](https://github.com/nginx/nginx) | 29,707 | — | C | The official NGINX Open Source repository. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 29,649 | — | Rust | Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cloud https://cloud.qdrant.io/ |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 29,580 | — | Python | [EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation" |
| [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) | 29,401 | — | — | 😎 A curated list of awesome GitHub Profile which updates in real time  |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 29,232 | — | TypeScript | Playwright MCP server |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 29,210 | — | TypeScript | Open-source orchestration for zero-human companies |
| [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 29,120 | — | C++ | Official source code of FreeCAD, a free and opensource multiplatform 3D parametric modeler. |
| [JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR) | 29,109 | — | Python | Ready-to-use OCR with 80+ supported languages and all popular writing scripts including Latin, Chinese, Arabic, Devanagari, Cyrillic and etc. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 29,042 | — | Python | A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic |
| [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) | 28,906 | — | Python | Python sample codes and textbook for robotics algorithms. |
| [barry-ran/QtScrcpy](https://github.com/barry-ran/QtScrcpy) | 28,890 | — | C++ | Android real-time display control software |
| [academic/awesome-datascience](https://github.com/academic/awesome-datascience) | 28,653 | — | — | :memo: An awesome Data Science repository to learn and apply for real world problems. |
| [mongodb/mongo](https://github.com/mongodb/mongo) | 28,200 | — | C++ | The MongoDB Database |
| [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | 28,185 | — | Python | SOTA Open Source TTS |
| [stanford-oval/storm](https://github.com/stanford-oval/storm) | 28,011 | — | Python | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | 27,908 | — | Rust | Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀 |
| [ChristosChristofidis/awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning) | 27,723 | — | — | A curated list of awesome Deep Learning tutorials, projects and communities. |
| [microsoft/cascadia-code](https://github.com/microsoft/cascadia-code) | 27,583 | — | Python | This is a fun, new monospaced font that includes programming ligatures and is designed to enhance the modern look and feel of the Windows Terminal. |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 27,504 | — | C# | Integrate cutting-edge LLM technology quickly and easily into your apps |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | 27,434 | — | TypeScript | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action. |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 27,045 | — | TypeScript | Open-source platform to build and deploy AI agent workflows. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 26,709 | — | Rust | Open-source search and retrieval database for AI applications. |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | 26,702 | — | MDX | This repository contains the Hugging Face Agents Course.  |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 26,518 | — | — | A list of AI autonomous agents |
| [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | 26,488 | — | — | Awesome-LLM: a curated list of Large Language Model |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 26,142 | — | Python | 🤗 smolagents: a barebones library for agents that think in code. |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 26,094 | — | Jupyter Notebook | This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. RAG systems combine information retrieval with generative models to provide accurate and contextually rich responses. |
| [huggingface/open-r1](https://github.com/huggingface/open-r1) | 25,952 | — | Python | Fully open reproduction of DeepSeek-R1 |
| [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | 25,858 | — | Python | Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨ |
| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | 25,619 | — | TypeScript | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [TheAlgorithms/Rust](https://github.com/TheAlgorithms/Rust) | 25,584 | — | Rust |  All Algorithms implemented in Rust  |
| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | 25,410 | — | Go | Tiny, Fast, and Deployable anywhere — automate the mundane, unleash your creativity |
| [aishwaryanr/awesome-generative-ai-guide](https://github.com/aishwaryanr/awesome-generative-ai-guide) | 25,397 | — | HTML | A one stop repository for generative AI research updates, interview resources, notebooks and much more! |
| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | 25,035 | — | TypeScript | 一款提示词优化器，助力于编写高质量的提示词 |
| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | 24,900 | — | C++ | An MCP-based chatbot - 一个基于MCP的聊天机器人 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | 24,820 | — | Python | The open source AI engineering platform. MLflow enables teams of all sizes to debug, evaluate, monitor, and optimize production-quality AI agents, LLM applications, and ML models while controlling costs and managing access to models and data. |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 24,727 | — | Python | SGLang is a high-performance serving framework for large language models and multimodal models. |
| [openai/gpt-2](https://github.com/openai/gpt-2) | 24,699 | — | Python | Code for the paper "Language Models are Unsupervised Multitask Learners" |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 24,669 | — | TypeScript | Use Garry Tan's exact Claude Code setup: 6 opinionated tools that serve as CEO, Eng Manager, Release Manager and QA Engineer |
| [ml-explore/mlx](https://github.com/ml-explore/mlx) | 24,607 | — | C++ | MLX: An array framework for Apple silicon |
| [haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA) | 24,582 | — | Python | [NeurIPS'23 Oral] Visual Instruction Tuning (LLaVA) built towards GPT-4V level capabilities and beyond. |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 24,582 | — | Python | JARVIS, a system to connect LLMs with ML community. Paper: https://arxiv.org/pdf/2303.17580.pdf |
| [microsoft/OmniParser](https://github.com/microsoft/OmniParser) | 24,551 | — | Jupyter Notebook | A simple screen parsing tool towards pure vision based GUI agent |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | 24,549 | — | MDX | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems. |
| [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | 24,538 | — | JavaScript | LLM Frontend for Power Users. |
| [Lissy93/dashy](https://github.com/Lissy93/dashy) | 24,266 | — | Vue | 🚀 A self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more! |
| [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | 24,183 | — | Jupyter Notebook | Official code repo for the O'Reilly Book - "Hands-On Large Language Models" |
| [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) | 23,803 | — | C | Distribute and run LLMs with a single file. |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 23,799 | — | Python | Open-Source Frontier Voice AI |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 23,447 | — | Rust | Browser automation CLI for AI agents |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 23,391 | — | TypeScript | 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23  |
| [toon-format/toon](https://github.com/toon-format/toon) | 23,356 | — | TypeScript | 🎒 Token-Oriented Object Notation (TOON) – JSON for LLM prompts at half the tokens. Spec, benchmarks & TypeScript implementation. |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 22,887 | — | Python | LLM驱动的 A/H/美股智能分析器：多数据源行情 + 实时新闻 + LLM决策仪表盘 + 多渠道推送，零成本定时运行，纯白嫖. LLM-powered stock analysis system for A/H/US markets. |
| [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | 22,817 | — | JavaScript | Introduction to Machine Learning Systems |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 22,231 | — | Python | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| [yoheinakajima/babyagi](https://github.com/yoheinakajima/babyagi) | 22,199 | — | Python | — |
| [wandb/openui](https://github.com/wandb/openui) | 22,172 | — | TypeScript | OpenUI let's you describe UI using your imagination, then see it rendered live. |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) | 22,124 | — | TypeScript | From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack. |
| [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | 21,895 | — | Zig | Lightpanda: the headless browser designed for AI and automation |
| [TheAlgorithms/C](https://github.com/TheAlgorithms/C) | 21,818 | — | C | Collection of various algorithms in mathematics, machine learning, computer science, physics, etc implemented in C for educational purposes. |
| [letta-ai/letta](https://github.com/letta-ai/letta) | 21,653 | — | Python | Letta is the platform for building stateful agents: AI with advanced memory that can learn and self-improve over time. |
| [dolthub/dolt](https://github.com/dolthub/dolt) | 21,489 | — | Go | Dolt – Git for Data |
| [guidance-ai/guidance](https://github.com/guidance-ai/guidance) | 21,358 | — | Jupyter Notebook | A guidance language for controlling large language models. |
| [openai/chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin) | 21,221 | — | Python | The ChatGPT Retrieval Plugin lets you easily find personal or work documents by asking questions in natural language. |
| [openai/swarm](https://github.com/openai/swarm) | 21,189 | — | Python | Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team. |
| [usestrix/strix](https://github.com/usestrix/strix) | 21,036 | — | Python | ✨ Open-source AI hackers for your apps 👨🏻‍💻 |
| [Lissy93/personal-security-checklist](https://github.com/Lissy93/personal-security-checklist) | 20,965 | — | TypeScript | 🔒 A compiled checklist of 300+ tips for protecting digital security and privacy in 2026 |
| [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | 20,954 | — | Jupyter Notebook | Neural Networks: Zero to Hero |
| [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) | 20,855 | — | Python | Automate browser based workflows with AI |
| [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) | 20,646 | — | Jupyter Notebook | This repository provides tutorials and implementations for various Generative AI Agent techniques, from basic to advanced. It serves as a comprehensive guide for building intelligent, interactive AI systems. |
| [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | 20,300 | — | — | 280+ free n8n automation templates — ready-to-use workflows for Gmail, Telegram, Slack, Discord, WhatsApp, Google Drive, Notion, OpenAI, and more. AI agents, RAG   chatbots, email automation, social media, DevOps, and document processing. The largest open-source n8n template collection. |
| [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) | 20,260 | — | — | A curated list of awesome open source libraries to deploy, monitor, version and scale your machine learning |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 20,109 | — | Python | A lightweight, powerful framework for multi-agent workflows |
| [fchollet/deep-learning-with-python-notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks) | 19,993 | — | Jupyter Notebook | Jupyter notebooks for the code samples of the book "Deep Learning with Python" |
| [GoogleCloudPlatform/microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo) | 19,964 | — | Go | Sample cloud-first application with 10 microservices showcasing Kubernetes, Istio, and gRPC. |
| [navidrome/navidrome](https://github.com/navidrome/navidrome) | 19,930 | — | Go | 🎧☁️ Your Personal Streaming Service |
| [openai/gpt-oss](https://github.com/openai/gpt-oss) | 19,919 | — | Python | gpt-oss-120b and gpt-oss-20b are two open-weight language models by OpenAI |
| [microsoft/fluentui](https://github.com/microsoft/fluentui) | 19,879 | — | TypeScript | Fluent UI web represents a collection of utilities, React components, and web components for building web applications. |
| [magenta/magenta](https://github.com/magenta/magenta) | 19,773 | — | Python | Magenta: Music and Art Generation with Machine Intelligence |
| [anthropics/courses](https://github.com/anthropics/courses) | 19,586 | — | Jupyter Notebook | Anthropic's educational courses |
| [ish-app/ish](https://github.com/ish-app/ish) | 19,552 | — | C | Linux shell for iOS |
| [stitionai/devika](https://github.com/stitionai/devika) | 19,500 | — | Python | Devika is the first open-source implementation of an Agentic Software Engineer. Initially started as an open-source alternative to Devin. |
| [karpathy/llama2.c](https://github.com/karpathy/llama2.c) | 19,289 | — | C | Inference Llama 2 in one file of pure C |
| [mikeroyal/Self-Hosting-Guide](https://github.com/mikeroyal/Self-Hosting-Guide) | 18,958 | — | Dockerfile | Self-Hosting Guide. Learn all about  locally hosting (on premises & private web servers) and managing software applications by yourself or your organization. Including Cloud, LLMs, WireGuard, Automation, Home Assistant, and Networking. |
| [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | 18,779 | — | Python | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024]  |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 18,767 | — | Python | CLI-Anything: Making ALL Software Agent-Native |
| [facebookresearch/sam2](https://github.com/facebookresearch/sam2) | 18,718 | — | Jupyter Notebook | The repository provides code for running inference with the Meta Segment Anything Model 2 (SAM 2), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. |
| [QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) | 18,690 | — | Jupyter Notebook | Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 18,647 | — | HTML | practice made claude perfect |
| [google/adk-python](https://github.com/google/adk-python) | 18,450 | — | Python | An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | 18,320 | — | Jupyter Notebook |  This repository delivers end-to-end, code-first tutorials covering every layer of production-grade GenAI agents, guiding you from spark to scale with proven patterns and reusable blueprints for real-world launches. |
| [keon/awesome-nlp](https://github.com/keon/awesome-nlp) | 18,300 | — | — | :book: A curated list of resources dedicated to Natural Language Processing (NLP) |
| [bitwarden/server](https://github.com/bitwarden/server) | 18,284 | — | C# | Bitwarden infrastructure/backend (API, database, Docker, etc). |
| [uvdesk/community-skeleton](https://github.com/uvdesk/community-skeleton) | 18,195 | — | CSS | UVdesk Open Source Community Helpdesk is a comprehensive ticketing support system designed for everyone, offering robust features to streamline customer support and collaboration. |
| [openai/evals](https://github.com/openai/evals) | 18,041 | — | Python | Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks. |
| [microsoft/AirSim](https://github.com/microsoft/AirSim) | 18,027 | — | C++ | Open source simulator for autonomous vehicles built on Unreal Engine / Unity, from Microsoft AI & Research |
| [google-gemini/gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) | 18,003 | — | Jupyter Notebook | Get started with building Fullstack Agents using Gemini 2.5 and LangGraph |
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | 17,918 | — | C# | Lean Algorithmic Trading Engine by QuantConnect (Python, C#) |
| [TheAlgorithms/Go](https://github.com/TheAlgorithms/Go) | 17,886 | — | Go | Algorithms and Data Structures implemented in Go for beginners, following best practices. |
| [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | 17,825 | — | Rust | Hundreds of models & providers. One command to find what runs on your hardware. |
| [dotnet/runtime](https://github.com/dotnet/runtime) | 17,727 | — | C# | .NET is a cross-platform runtime for cloud, mobile, desktop, and IoT apps. |
| [huggingface/trl](https://github.com/huggingface/trl) | 17,707 | — | Python | Train transformer language models with reinforcement learning. |
| [wled/WLED](https://github.com/wled/WLED) | 17,698 | — | C++ | Control WS2812B and many more types of digital RGB LEDs with an ESP32 over WiFi! |
| [ujjwalkarn/Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) | 17,633 | — | — | machine learning and deep learning tutorials, articles and other resources  |
| [openai/tiktoken](https://github.com/openai/tiktoken) | 17,609 | — | Python | tiktoken is a fast BPE tokeniser for use with OpenAI's models. |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | 17,588 | — | TypeScript | GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 17,490 | — | TypeScript | Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, Llama, and more. Simple declarative configs with command line and CI/CD integration. |
| [mrdbourke/pytorch-deep-learning](https://github.com/mrdbourke/pytorch-deep-learning) | 17,422 | — | Jupyter Notebook | Materials for the Learn PyTorch for Deep Learning: Zero to Mastery course. |
| [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin) | 17,326 | — | C++ | Marlin is a firmware for RepRap 3D printers optimized for both 8 and 32 bit microcontrollers.  Marlin supports all common platforms.   Many commercial 3D printers come with Marlin installed.  Check with your vendor if you need source code for your specific machine. |
| [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 17,279 | — | Python | <⚡️> SuperAGI - A dev-first open source autonomous AI agent framework. Enabling developers to build, manage & run useful autonomous agents quickly and reliably. |
| [microsoft/react-native-windows](https://github.com/microsoft/react-native-windows) | 17,206 | — | C++ | A framework for building native Windows apps with React. |
| [allenai/olmocr](https://github.com/allenai/olmocr) | 17,034 | — | Python | Toolkit for linearizing PDFs for LLM datasets/training |
| [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | 16,896 | — | TypeScript | Kilo is the all-in-one agentic engineering platform. Build, ship, and iterate faster with the most popular open source coding agent. #1 coding agent on OpenRouter. 1.5M+ Kilo Coders. 25T+ tokens processed |
| [NVIDIA/open-gpu-kernel-modules](https://github.com/NVIDIA/open-gpu-kernel-modules) | 16,814 | — | C | NVIDIA Linux open GPU kernel module source |
| [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | 16,776 | — | Jupyter Notebook | Code for Machine Learning for Algorithmic Trading, 2nd edition. |
| [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | 16,772 | — | Jupyter Notebook | Examples and guides for using the Gemini API |
| [openai/baselines](https://github.com/openai/baselines) | 16,673 | — | Python | OpenAI Baselines: high-quality implementations of reinforcement learning algorithms |
| [bharathgs/Awesome-pytorch-list](https://github.com/bharathgs/Awesome-pytorch-list) | 16,423 | — | — | A comprehensive list of pytorch related content on github,such as different models,implementations,helper libraries,tutorials etc. |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 16,408 | — | Python | 🐫 CAMEL: The first and the best multi-agent framework. Finding the Scaling Law of Agents. https://www.camel-ai.org |
| [ellisonleao/magictools](https://github.com/ellisonleao/magictools) | 16,310 | — | Markdown | :video_game: :pencil: A list of Game Development resources to make magic happen. |
| [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | 16,301 | — | Jupyter Notebook | Sample code and notebooks for Generative AI on Google Cloud, with Gemini on Vertex AI |
| [Snapchat/Valdi](https://github.com/Snapchat/Valdi) | 16,285 | — | C++ | Valdi is a cross-platform UI framework that delivers native performance without sacrificing developer velocity. |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | 16,211 | — | Python | Agent Zero AI framework |
| [projectdiscovery/katana](https://github.com/projectdiscovery/katana) | 16,118 | — | Go | A next-generation crawling and spidering framework. |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | 15,965 | — | Python | Fully automatic censorship removal for language models |
| [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick) | 15,954 | — | C | ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and offers powerful command-line tools and APIs for automation, scripting, and integration across platforms. |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 15,897 | — | Python | OpenViking is an open-source context database designed specifically for AI Agents(such as openclaw). OpenViking unifies the management of context (memory, resources, and skills) that Agents need through a file system paradigm, enabling hierarchical context delivery and self-evolving. |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 15,829 | — | Go | Weaviate is an open-source vector database that stores both objects and vectors, allowing for the combination of vector search with structured filtering with the fault tolerance and scalability of a cloud-native database​. |
| [openai/gpt-3](https://github.com/openai/gpt-3) | 15,753 | — | — | GPT-3: Language Models are Few-Shot Learners |
| [browser-use/web-ui](https://github.com/browser-use/web-ui) | 15,734 | — | Python | 🖥️ Run AI Agent in your browser. |
| [NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | 15,725 | — | Python | Ongoing research training transformer models at scale |
| [microsoft/Bringing-Old-Photos-Back-to-Life](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life) | 15,703 | — | Python | Bringing Old Photo Back to Life (CVPR 2020 oral) |
| [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | 15,678 | — | Python | Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 15,568 | — | Python | GenAI Agent Framework, the Pydantic way |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | 15,479 | — | Python | The absolute trainer to light up AI agents. |
| [treeverse/dvc](https://github.com/treeverse/dvc) | 15,457 | — | Python | 🦉 Data Versioning and ML Experiments |
| [systemd/systemd](https://github.com/systemd/systemd) | 15,446 | — | C | The systemd System and Service Manager  |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | 15,383 | — | Python | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| [mml-book/mml-book.github.io](https://github.com/mml-book/mml-book.github.io) | 15,208 | — | Jupyter Notebook | Companion webpage to the book "Mathematics For Machine Learning" |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | 15,208 | — | Python | Deep Agents is an agent harness built on langchain and langgraph. Deep Agents are equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - making them well-equipped to handle complex agentic tasks. |
| [microsoft/data-formulator](https://github.com/microsoft/data-formulator) | 15,138 | — | TypeScript | 🪄 Create rich visualizations with AI  |
| [plandex-ai/plandex](https://github.com/plandex-ai/plandex) | 15,108 | — | Go | Open source AI coding agent. Designed for large projects and real world tasks. |
| [karpathy/micrograd](https://github.com/karpathy/micrograd) | 15,097 | — | Jupyter Notebook | A tiny scalar-valued autograd engine and a neural net library on top of it with PyTorch-like API |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | 14,937 | — | Python | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 14,919 | — | Rust | Open-source Agent Operating System |
| [NVIDIA/DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples) | 14,747 | — | Jupyter Notebook | State-of-the-Art Deep Learning scripts organized by models - easy to train and deploy with reproducible accuracy and performance on enterprise-grade infrastructure. |
| [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) | 14,714 | — | Python | Wan: Open and Advanced Large-Scale Video Generative Models |
| [openai/skills](https://github.com/openai/skills) | 14,594 | — | Python | Skills Catalog for Codex |
| [terkelg/awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding) | 14,586 | — | HTML | Creative Coding: Generative Art, Data visualization, Interaction Design, Resources. |
| [GoogleCloudPlatform/terraformer](https://github.com/GoogleCloudPlatform/terraformer) | 14,521 | — | Go | CLI tool to generate terraform files from existing infrastructure (reverse Terraform). Infrastructure to Code |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | 14,399 | — | Python | "RAG-Anything: All-in-One RAG Framework" |
| [microsoft/nni](https://github.com/microsoft/nni) | 14,346 | — | Python | An open source AutoML toolkit for automate machine learning lifecycle, including feature engineering, neural architecture search, model compression and hyper-parameter tuning. |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 14,333 | — | Python | Knowledge Engine for AI Agent Memory in 6 lines of code |
| [DataTalksClub/mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | 14,331 | — | Jupyter Notebook | Free MLOps course from DataTalks.Club |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 14,311 | — | Shell | A collection of 100+ specialized Claude Code subagents covering a wide range of development use cases |
| [oxnr/awesome-bigdata](https://github.com/oxnr/awesome-bigdata) | 14,285 | — | — | A curated list of awesome big data frameworks, ressources and other awesomeness. |
| [ggml-org/ggml](https://github.com/ggml-org/ggml) | 14,243 | — | C++ | Tensor library for machine learning |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | 14,193 | — | Jupyter Notebook | AirLLM 70B inference with single 4GB GPU |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 14,158 | — | Python | The LLM Evaluation Framework |
| [marcuswestin/store.js](https://github.com/marcuswestin/store.js) | 14,013 | — | JavaScript | Cross-browser storage for all use cases, used across the web. |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 14,009 | — | Python | A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems. Use when building, optimizing, or debugging agent systems that require effective context management. |
| [M2Team/NanaZip](https://github.com/M2Team/NanaZip) | 13,653 | — | C++ | The 7-Zip derivative intended for the modern Windows experience |
| [JoeanAmier/TikTokDownloader](https://github.com/JoeanAmier/TikTokDownloader) | 13,650 | — | Python | TikTok 发布/喜欢/合辑/直播/视频/图集/音乐；抖音发布/喜欢/收藏/收藏夹/视频/图集/实况/直播/音乐/合集/评论/账号/搜索/热榜数据采集工具/下载工具 |
| [dottxt-ai/outlines](https://github.com/dottxt-ai/outlines) | 13,576 | — | Python | Structured Outputs |
| [hrydgard/ppsspp](https://github.com/hrydgard/ppsspp) | 13,572 | — | C++ | A PSP emulator for Android, Windows, Mac and Linux, written in C++. Want to contribute? Join us on Discord at https://discord.gg/5NJB6dD or just send pull requests / issues. For discussion use the forums at forums.ppsspp.org. |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | 13,458 | — | Go | MCP Toolbox for Databases is an open source MCP server for databases. |
| [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | 13,448 | — | JavaScript | 一个基于 JavaScript 的网盘文件下载地址获取工具。基于【网盘直链下载助手】修改 ，支持 百度网盘 / 阿里云盘 / 中国移动云盘 / 天翼云盘 / 迅雷云盘 / 夸克网盘 / UC网盘 / 123云盘 八大网盘 |
| [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 13,424 | — | TypeScript | The open-source voice synthesis studio powered by Qwen3-TTS. |
| [openai/symphony](https://github.com/openai/symphony) | 13,393 | — | Elixir | Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents. |
| [google/A2UI](https://github.com/google/A2UI) | 13,390 | — | TypeScript | — |
| [microsoft/LoRA](https://github.com/microsoft/LoRA) | 13,348 | — | Python | Code for loralib, an implementation of "LoRA: Low-Rank Adaptation of Large Language Models" |
| [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | 13,139 | — | Python | TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way. |
| [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | 13,040 | — | Python | Memory for 24/7 proactive agents like openclaw (moltbot, clawdbot). |
| [jupyter/notebook](https://github.com/jupyter/notebook) | 13,011 | — | Jupyter Notebook | Jupyter Interactive Notebook |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) | 12,999 | — | Python | Supercharge Your LLM Application Evaluations 🚀 |
| [OrcaSlicer/OrcaSlicer](https://github.com/OrcaSlicer/OrcaSlicer) | 12,937 | — | C++ | G-code generator for 3D printers (Bambu, Prusa, Voron, VzBot, RatRig, Creality, etc.) |
| [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT) | 12,800 | — | C++ | NVIDIA® TensorRT™ is an SDK for high-performance deep learning inference on NVIDIA GPUs. This repository contains the open source components of TensorRT. |
| [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | 12,737 | — | TypeScript | An all-in-one enhancement suite for Google Gemini & AI Studio - timeline navigation, folder management, prompt library, and chat export in one powerful extension. / Google Gemini & AI Studio 全能增强插件：集成时间轴导航、文件夹管理、提示词库及聊天导出等众多功能。 |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 12,683 | — | Python | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
| [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | 12,628 | — | Python | Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities. |
| [ageron/handson-ml3](https://github.com/ageron/handson-ml3) | 12,586 | — | Jupyter Notebook | A series of Jupyter notebooks that walk you through the fundamentals of Machine Learning and Deep Learning in Python using Scikit-Learn, Keras and TensorFlow 2. |
| [coder/coder](https://github.com/coder/coder) | 12,575 | — | Go | Secure environments for developers and their agents |
| [567-labs/instructor](https://github.com/567-labs/instructor) | 12,557 | — | Python | structured outputs for llms  |
| [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2) | 12,551 | — | Jupyter Notebook | PyTorch code and models for the DINOv2 self-supervised learning method. |
| [khangich/machine-learning-interview](https://github.com/khangich/machine-learning-interview) | 12,427 | — | — | Machine Learning Interviews from FAANG, Snapchat, LinkedIn. I have offers from Snapchat, Coupang, Stitchfix etc. Blog: mlengineer.io. |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | 12,399 | — | Python | SQL Native Memory Layer for LLMs, AI Agents & Multi-Agent Systems |
| [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | 12,238 | — | Python | Transform your favorite cities into beautiful, minimalist designs. MapToPoster lets you create and export visually striking map posters with code. |
| [openai/shap-e](https://github.com/openai/shap-e) | 12,222 | — | Python | Generate 3D objects conditioned on text or images |
| [getomni-ai/zerox](https://github.com/getomni-ai/zerox) | 12,186 | — | TypeScript | OCR & Document Extraction using vision models |
| [microsoft/TRELLIS](https://github.com/microsoft/TRELLIS) | 12,010 | — | Python | Official repo for paper "Structured 3D Latents for Scalable and Versatile 3D Generation" (CVPR'25 Spotlight). |
| [microsoft/RD-Agent](https://github.com/microsoft/RD-Agent) | 11,897 | — | Python | Research and development (R&D) is crucial for the enhancement of industrial productivity, especially in the AI era, where the core aspects of R&D are mainly focused on data and models. We are committed to automating these high-value generic R&D processes through R&D-Agent, which lets AI drive data-driven AI. 🔗https://aka.ms/RD-Agent-Tech-Report |
| [microsoft/garnet](https://github.com/microsoft/garnet) | 11,774 | — | C# | Garnet is a remote cache-store from Microsoft Research that offers strong performance (throughput and latency), scalability, storage, recovery, cluster sharding, key migration, and replication features. Garnet can work with existing Redis clients. |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 11,744 | — | Python | A framework for few-shot evaluation of language models. |
| [openai/spinningup](https://github.com/openai/spinningup) | 11,655 | — | Python | An educational resource to help anyone learn deep reinforcement learning. |
| [steven2358/awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) | 11,632 | — | — | A curated list of modern Generative Artificial Intelligence projects and services |
| [robotframework/robotframework](https://github.com/robotframework/robotframework) | 11,488 | — | Python | Generic automation framework for acceptance testing and RPA |
| [alibaba/page-agent](https://github.com/alibaba/page-agent) | 11,438 | — | TypeScript | JavaScript in-page GUI agent. Control web interfaces with natural language. |
| [simonw/llm](https://github.com/simonw/llm) | 11,368 | — | Python | Access large language models from the command-line |
| [e2b-dev/E2B](https://github.com/e2b-dev/E2B) | 11,342 | — | MDX | Open-source, secure environment with real-world tools for enterprise-grade agents. |
| [NVIDIA/FastPhotoStyle](https://github.com/NVIDIA/FastPhotoStyle) | 11,179 | — | Python | Style transfer, deep learning, feature transform |
| [mjhea0/awesome-fastapi](https://github.com/mjhea0/awesome-fastapi) | 11,171 | — | — | A curated list of awesome things related to FastAPI |
| [microsoft/promptflow](https://github.com/microsoft/promptflow) | 11,072 | — | Python | Build high-quality LLM apps - from prototyping, testing to production deployment and monitoring. |
| [microsoft/TypeScript-React-Starter](https://github.com/microsoft/TypeScript-React-Starter) | 11,064 | — | TypeScript | A starter template for TypeScript and React with a detailed README describing how to use the two together. |
| [NoFxAiOS/nofx](https://github.com/NoFxAiOS/nofx) | 10,964 | — | Go | Your personal AI trading assistant. Any market. Any model. Pay with USDC, not API keys. |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 10,958 | — | TypeScript | A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API. |
| [wandb/wandb](https://github.com/wandb/wandb) | 10,916 | — | Python | The AI developer platform. Use Weights & Biases to train and fine-tune models, and manage models from experimentation to production. |
| [openai/DALL-E](https://github.com/openai/DALL-E) | 10,876 | — | Python | PyTorch package for the discrete VAE used for DALL·E. |
| [google/dopamine](https://github.com/google/dopamine) | 10,855 | — | Jupyter Notebook | Dopamine is a research framework for fast prototyping of reinforcement learning algorithms.  |
| [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) | 10,808 | — | Python | Large Language Model Text Generation Inference |
| [microsoft/frontend-bootcamp](https://github.com/microsoft/frontend-bootcamp) | 10,807 | — | TypeScript | Frontend Workshop from HTML/CSS/JS to TypeScript/React/Redux |
| [openai/openai-node](https://github.com/openai/openai-node) | 10,743 | — | TypeScript | Official JavaScript / TypeScript library for the OpenAI API |
| [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | 10,721 | — | Jupyter Notebook | Official inference library for Mistral models |
| [betaflight/betaflight](https://github.com/betaflight/betaflight) | 10,721 | — | C | Open Source Flight Controller Firmware |
| [amnezia-vpn/amnezia-client](https://github.com/amnezia-vpn/amnezia-client) | 10,646 | — | C++ | Amnezia VPN Client (Desktop+Mobile) |
| [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | 10,501 | — | JavaScript | Stremio - Freedom to Stream |
| [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | 10,331 | — | Python | RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application on your personal device. |
| [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | 10,299 | — | JavaScript | — |
| [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | 10,255 | — | C++ | Production ready toolkit to run AI locally |
| [dotnet/eShop](https://github.com/dotnet/eShop) | 10,239 | — | C# | A reference .NET application implementing an eCommerce site |
| [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | 10,169 | — | TypeScript | Agentic AI Infrastructure for magnifying HUMAN capabilities. |
| [google/magika](https://github.com/google/magika) | 10,160 | — | Python | Fast and accurate AI powered file content types detection  |
| [google-research/timesfm](https://github.com/google-research/timesfm) | 10,077 | — | Python | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |
| [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | 10,067 | — | Go | ✨ Fully autonomous AI Agents system capable of performing complex penetration testing tasks |
| [KalyanKS-NLP/llm-engineer-toolkit](https://github.com/KalyanKS-NLP/llm-engineer-toolkit) | 10,029 | — | — | A curated list of  120+ LLM libraries category wise.  |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 9,953 | — | Python | Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork |
| [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) | 9,944 | — | Python | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. |
| [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) | 9,822 | — | C++ | A multi core friendly rigid body physics and collision detection library. Written in C++. Suitable for games and VR applications. Used by Horizon Forbidden West and Death Stranding 2. |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | 9,740 | — | Python | A research prototype of a human-centered web agent |
| [aikorea/awesome-rl](https://github.com/aikorea/awesome-rl) | 9,660 | — | — | Reinforcement learning resources curated |
| [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) | 9,610 | — | Python | Official repository for LTX-Video |
| [Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies](https://github.com/Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies) | 9,588 | — | — | This repository contains a curated collection of 300+ case studies from over 80 companies, detailing practical applications and insights into machine learning (ML) system design. The contents are organized to help you easily find relevant case studies based on industry or specific ML use cases.  |
| [opendatalab/PDF-Extract-Kit](https://github.com/opendatalab/PDF-Extract-Kit) | 9,487 | — | Python | A Comprehensive Toolkit for High-Quality PDF Content Extraction |
| [NVIDIA/cutlass](https://github.com/NVIDIA/cutlass) | 9,460 | — | C++ | CUDA Templates and Python DSLs for High-Performance Linear Algebra |
| [huggingface/skills](https://github.com/huggingface/skills) | 9,338 | — | Python | — |
| [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | 9,283 | — | TypeScript | Open-source AI coworker, with memory |
| [ahrm/sioyek](https://github.com/ahrm/sioyek) | 9,247 | — | C | Sioyek is a PDF viewer with a focus on textbooks and research papers |
| [thewhiteh4t/seeker](https://github.com/thewhiteh4t/seeker) | 9,156 | — | CSS | Accurately Locate Smartphones using Social Engineering  |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | 9,143 | — | JavaScript | NVIDIA plugin for secure installation of OpenClaw |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 9,072 | — | C++ | A lightweight, lightning-fast, in-process vector database |
| [OpenPipe/ART](https://github.com/OpenPipe/ART) | 9,040 | — | Python | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen3.5, GPT-OSS, Llama, and more! |
| [NVIDIA/cuda-samples](https://github.com/NVIDIA/cuda-samples) | 8,976 | — | C | Samples for CUDA Developers which demonstrates features in CUDA Toolkit |
| [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | 8,959 | — | TypeScript | OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration. |
| [NVIDIA/apex](https://github.com/NVIDIA/apex) | 8,934 | — | Python | A PyTorch Extension:  Tools for easy mixed precision and distributed training in Pytorch |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 8,921 | — | Jupyter Notebook | AI Observability & Evaluation |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 8,909 | — | Python | The agent that grows with you |
| [graviraja/MLOps-Basics](https://github.com/graviraja/MLOps-Basics) | 8,738 | — | Jupyter Notebook | — |
| [NVIDIA/vid2vid](https://github.com/NVIDIA/vid2vid) | 8,714 | — | Python | Pytorch implementation of our method for high-resolution (e.g. 2048x1024) photorealistic video-to-video translation. |
| [HKUDS/AutoAgent](https://github.com/HKUDS/AutoAgent) | 8,674 | — | Python | "AutoAgent: Fully-Automated and Zero-Code LLM Agent Framework" |
| [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | 8,640 | — | Python | OpenSandbox is a general-purpose sandbox platform for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluation, AI Code Execution, and RL Training. |
| [apify/crawlee-python](https://github.com/apify/crawlee-python) | 8,639 | — | Python | Crawlee—A web scraping and browser automation library for Python to build reliable crawlers. Extract data for AI, LLMs, RAG, or GPTs. Download HTML, PDF, JPG, PNG, and other files from websites. Works with Parsel, BeautifulSoup, Playwright, and raw HTTP. Both headful and headless mode. With proxy rotation. |
| [microsoft/TypeChat](https://github.com/microsoft/TypeChat) | 8,633 | — | TypeScript | TypeChat is a library that makes it easy to build natural language interfaces using types. |
| [fmhy/edit](https://github.com/fmhy/edit) | 8,573 | — | JavaScript | Make changes to FMHY |
| [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | 8,486 | — | TypeScript | Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio.  |
| [GoogleCloudPlatform/training-data-analyst](https://github.com/GoogleCloudPlatform/training-data-analyst) | 8,469 | — | Jupyter Notebook | Labs and demos for courses for GCP Training (http://cloud.google.com/training). |
| [TeamWiseFlow/wiseflow](https://github.com/TeamWiseFlow/wiseflow) | 8,127 | — | JavaScript | enhance any agent's browser use skill |
| [NVIDIA/Cosmos](https://github.com/NVIDIA/Cosmos) | 8,089 | — | — | New repo collection for NVIDIA Cosmos: https://github.com/nvidia-cosmos |
| [openai/jukebox](https://github.com/openai/jukebox) | 8,044 | — | Python | Code for the paper "Jukebox: A Generative Model for Music" |
| [soulmachine/machine-learning-cheat-sheet](https://github.com/soulmachine/machine-learning-cheat-sheet) | 8,015 | — | TeX | Classical equations and diagrams in machine learning |
| [GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples) | 8,014 | — | Jupyter Notebook | Code samples used on cloud.google.com |
| [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | 7,948 | — | Go | High-performance browser automation bridge and multi-instance orchestrator with advanced stealth injection and real-time dashboard. |
| [alirezadir/Machine-Learning-Interviews](https://github.com/alirezadir/Machine-Learning-Interviews) | 7,917 | — | Jupyter Notebook | This repo is meant to serve as a guide for Machine Learning/AI technical interviews.  |
| [apple/ml-sharp](https://github.com/apple/ml-sharp) | 7,904 | — | Python | Sharp Monocular View Synthesis in Less Than a Second |
| [LMCache/LMCache](https://github.com/LMCache/LMCache) | 7,716 | — | Python | Supercharge Your LLM with the Fastest KV Cache Layer |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 7,710 | — | — | PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth. |
| [weaviate/Verba](https://github.com/weaviate/Verba) | 7,609 | — | Python | Retrieval Augmented Generation (RAG) chatbot powered by Weaviate |
| [fontforge/fontforge](https://github.com/fontforge/fontforge) | 7,600 | — | C | Free (libre) font editor for Windows, Mac OS X and GNU+Linux |
| [awslabs/agent-squad](https://github.com/awslabs/agent-squad) | 7,521 | — | Python | Flexible and powerful framework for managing multiple AI agents and handling complex conversations |
| [openai/universe](https://github.com/openai/universe) | 7,515 | — | Python | Universe: a software platform for measuring and training an AI's general intelligence across the world's supply of games, websites and other applications. |
| [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | 7,412 | — | C | Fast and accurate automatic speech recognition (ASR) for edge devices |
| [superset-sh/superset](https://github.com/superset-sh/superset) | 7,406 | — | TypeScript | IDE for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine |
| [GoogleCloudPlatform/kubectl-ai](https://github.com/GoogleCloudPlatform/kubectl-ai) | 7,362 | — | Go | AI powered Kubernetes Assistant |
| [microsoft/TinyTroupe](https://github.com/microsoft/TinyTroupe) | 7,329 | — | Jupyter Notebook | LLM-powered multiagent persona simulation for imagination enhancement and business insights. |
| [openai/guided-diffusion](https://github.com/openai/guided-diffusion) | 7,316 | — | Python | — |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | 7,298 | — | HTML | the LLM vulnerability scanner |
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | 7,262 | — | C# | Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity. |
| [asg017/sqlite-vec](https://github.com/asg017/sqlite-vec) | 7,206 | — | C | A vector search SQLite extension that runs anywhere! |
| [google/adk-go](https://github.com/google/adk-go) | 7,193 | — | Go | An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | 7,132 | — | Python | MiroThinker is a deep research agent optimized for complex research and prediction tasks. Our latest models, MiroThinker-1.7 and MiroThinker-H1, achieve 74.0 and 88.2 on the BrowseComp, respectively. |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 7,006 | — | Python | 66 Specialized Skills for Full-Stack Developers. Transform Claude Code into your expert pair programmer. |
| [NVIDIA/pix2pixHD](https://github.com/NVIDIA/pix2pixHD) | 6,979 | — | Python | Synthesizing and manipulating 2048x1024 images with conditional GANs |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | 6,933 | — | Python | Open-source observability for your GenAI or LLM application, based on OpenTelemetry |
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | 6,889 | — | Go | Dynamic, resilient AI orchestration. Coordinate data, models, and compute as you build AI workflows. Flyte 2 now available locally: https://github.com/flyteorg/flyte-sdk |
| [arcee-ai/mergekit](https://github.com/arcee-ai/mergekit) | 6,877 | — | Python | Tools for merging pretrained large language models. |
| [openai/point-e](https://github.com/openai/point-e) | 6,871 | — | Python | Point cloud diffusion for 3D model synthesis |
| [openai/openai-realtime-agents](https://github.com/openai/openai-realtime-agents) | 6,798 | — | TypeScript | This is a simple demonstration of more advanced, agentic patterns built on top of the Realtime API. |
| [Serial-Studio/Serial-Studio](https://github.com/Serial-Studio/Serial-Studio) | 6,715 | — | C++ | Open-source telemetry dashboard. Supports UART, BLE, MQTT, Modbus, CAN Bus and more.  |
| [huggingface/smol-course](https://github.com/huggingface/smol-course) | 6,612 | — | Jupyter Notebook | A course on aligning smol models. |
| [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | 6,554 | — | Python | Adding guardrails to large language models. |
| [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | 6,552 | — | Zig | Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig |
| [openai/consistency_models](https://github.com/openai/consistency_models) | 6,474 | — | Python | Official repo for consistency models. |
| [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | 6,452 | — | Jupyter Notebook | NVIDIA Isaac GR00T N1.6 -  A Foundation Model for Generalist Robots. |
| [microsoft/call-center-ai](https://github.com/microsoft/call-center-ai) | 6,402 | — | Python | Send a phone call from AI agent, in an API call. Or, directly call the bot from the configured phone number! |
| [NVIDIA/FasterTransformer](https://github.com/NVIDIA/FasterTransformer) | 6,395 | — | C++ | Transformer related optimization, including BERT, GPT |
| [vudovn/antigravity-kit](https://github.com/vudovn/antigravity-kit) | 6,379 | — | TypeScript | — |
| [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) | 6,374 | — | TypeScript | — |
| [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | 6,362 | — | Python | — |
| [NVIDIA/warp](https://github.com/NVIDIA/warp) | 6,339 | — | Python | A Python framework for accelerated simulation, data generation and spatial computing. |
| [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | 6,323 | — | Python | A text-to-speech (TTS), speech-to-text (STT) and speech-to-speech (STS) library built on Apple's MLX framework, providing efficient speech analysis on Apple Silicon. |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 6,310 | — | Python | Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw. |
| [LumaTeam/Luma3DS](https://github.com/LumaTeam/Luma3DS) | 6,282 | — | C | Nintendo 3DS "Custom Firmware" |
| [evcc-io/evcc](https://github.com/evcc-io/evcc) | 6,274 | — | Go | solar charging ☀️🚘 |
| [TelegramMessenger/MTProxy](https://github.com/TelegramMessenger/MTProxy) | 6,247 | — | C | — |
| [kiloreux/awesome-robotics](https://github.com/kiloreux/awesome-robotics) | 6,235 | — | — | A list of awesome Robotics resources |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | 6,143 | — | Python | VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning |
| [RapidAI/RapidOCR](https://github.com/RapidAI/RapidOCR) | 6,139 | — | Python | 📄 Awesome OCR multiple programing languages toolkits based on ONNXRuntime, OpenVINO, MNN, PaddlePaddle and PyTorch. |
| [microsoft/TaskWeaver](https://github.com/microsoft/TaskWeaver) | 6,127 | — | Python | The first "code-first" agent framework for seamlessly planning and executing data analytics tasks.  |
| [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | 6,095 | — | Python | YuE: Open Full-song Music Generation Foundation Model, something similar to Suno.ai but open |
| [GoogleCloudPlatform/agent-starter-pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) | 5,988 | — | Python | A collection of production-ready Generative AI Agent templates built for Google Cloud. It accelerates development by providing a holistic, production-ready solution, addressing common challenges (Deployment & Operations, Evaluation, Customization, Observability) in building and deploying GenAI agents. |
| [mindee/doctr](https://github.com/mindee/doctr) | 5,963 | — | Python | docTR (Document Text Recognition) - a seamless, high-performing & accessible library for OCR-related tasks powered by Deep Learning. |
| [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | 5,937 | — | Python | Demo of a customer service use case implemented with the OpenAI Agents SDK |
| [dair-ai/Mathematics-for-ML](https://github.com/dair-ai/Mathematics-for-ML) | 5,840 | — | — | 🧮  A collection of resources to learn mathematics for machine learning |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 5,825 | — | Python | +180 production-ready skills & plugins for Claude Code, OpenAI Codex, and OpenClaw — engineering, marketing, product, compliance, C-level advisory, and more. Install via /plugin marketplace. |
| [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 5,815 | — | Python | NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems. |
| [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | 5,803 | — | Python | PersonaPlex code. |
| [arthenica/ffmpeg-kit](https://github.com/arthenica/ffmpeg-kit) | 5,777 | — | C | FFmpeg Kit for applications. Supports Android, Flutter, iOS, Linux, macOS, React Native and tvOS. Supersedes MobileFFmpeg, flutter_ffmpeg and react-native-ffmpeg. |
| [BrainBlend-AI/atomic-agents](https://github.com/BrainBlend-AI/atomic-agents) | 5,776 | — | Python | Building AI agents, atomically |
| [meta-pytorch/torchtune](https://github.com/meta-pytorch/torchtune) | 5,705 | — | Python | PyTorch native post-training library |
| [NVIDIA/DALI](https://github.com/NVIDIA/DALI) | 5,644 | — | C++ | A GPU-accelerated library containing highly optimized building blocks and an execution engine for data processing to accelerate deep learning training and inference applications. |
| [leejet/stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) | 5,580 | — | C++ | Diffusion model(SD,Flux,Wan,Qwen Image,Z-Image,...) inference in pure C/C++ |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 5,573 | — | Python | — |
| [youssefHosni/Data-Science-Interview-Questions-Answers](https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers) | 5,539 | — | — | Curated list of data science interview questions and answers |
| [jellyfin/jellyfin-desktop](https://github.com/jellyfin/jellyfin-desktop) | 5,484 | — | C++ | Jellyfin Desktop Client |
| [AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops) | 5,383 | — | Python | Python SDK for AI agent monitoring, LLM cost tracking, benchmarking, and more. Integrates with most LLMs and agent frameworks including CrewAI, Agno, OpenAI Agents SDK, Langchain, Autogen, AG2, and CamelAI |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3) | 5,347 | — | C | Iceman Fork - Proxmark3 |
| [NVIDIA/tacotron2](https://github.com/NVIDIA/tacotron2) | 5,306 | — | Jupyter Notebook | Tacotron 2 - PyTorch implementation with faster-than-realtime inference |
| [zenml-io/zenml](https://github.com/zenml-io/zenml) | 5,281 | — | Python | ZenML 🙏: One AI Platform from Pipelines to Agents. https://zenml.io. |
| [Helicone/helicone](https://github.com/Helicone/helicone) | 5,270 | — | TypeScript | 🧊 Open source LLM observability platform. One line of code to monitor, evaluate, and experiment. YC W23 🍓 |
| [microsoft/SynapseML](https://github.com/microsoft/SynapseML) | 5,214 | — | Scala | Simple and Distributed Machine Learning |
| [dotenvx/dotenvx](https://github.com/dotenvx/dotenvx) | 5,214 | — | JavaScript | a secure dotenv–from the creator of `dotenv` |
| [ashishps1/learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering) | 5,162 | — | — | Learn AI and LLMs from scratch using free resources |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 4,982 | — | Python | Hindsight: Agent Memory That  Learns |
| [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | 4,939 | — | Python | Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model. |
| [unslothai/notebooks](https://github.com/unslothai/notebooks) | 4,915 | — | Jupyter Notebook | 250+ Fine-tuning & RL Notebooks for text, vision, audio, embedding, TTS models. |
| [psviderski/uncloud](https://github.com/psviderski/uncloud) | 4,914 | — | Go | A lightweight tool for deploying and managing containerised applications across a network of Docker hosts. Bridging the gap between Docker and Kubernetes ✨ |
| [InsForge/InsForge](https://github.com/InsForge/InsForge) | 4,911 | — | TypeScript | Give agents everything they need to ship fullstack apps. The backend built for agentic development.  |
| [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | 4,838 | — | TypeScript |  Agentic orchestrator for parallel coding agents — plans tasks, spawns agents, and autonomously handles CI    fixes, merge conflicts, and code reviews. |
| [inclusionAI/AReaL](https://github.com/inclusionAI/AReaL) | 4,836 | — | Python | Lightning-Fast RL for LLM Reasoning and Agents. Made Simple & Flexible. |
| [transformerlab/transformerlab-app](https://github.com/transformerlab/transformerlab-app) | 4,827 | — | TypeScript | Open Source Application for Advanced LLM + Diffusion Engineering: interact, train, fine-tune, and evaluate large language models on your own computer. |
| [BoltzmannEntropy/interviews.ai](https://github.com/BoltzmannEntropy/interviews.ai) | 4,816 | — | — | It is my belief that you, the postgraduate students and job-seekers for whom the book is primarily meant will benefit from reading it; however, it is my hope that even the most experienced researchers will find it fascinating as well. |
| [praydog/REFramework](https://github.com/praydog/REFramework) | 4,804 | — | C++ | Mod loader, scripting platform, and VR support for all RE Engine games |
| [Coder-World04/Complete-System-Design](https://github.com/Coder-World04/Complete-System-Design) | 4,741 | — | — | This repository contains everything you need to become proficient in System Design |
| [DataTalksClub/llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | 4,725 | — | Jupyter Notebook | LLM Zoomcamp - a free online course about real-life applications of LLMs. In 10 weeks you will learn how to build an AI system that answers questions about your knowledge base. |
| [GoogleCloudPlatform/golang-samples](https://github.com/GoogleCloudPlatform/golang-samples) | 4,597 | — | Go | Sample apps and code written for Google Cloud in the Go programming language. |
| [YishenTu/claudian](https://github.com/YishenTu/claudian) | 4,573 | — | TypeScript | An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault |
| [chiphuyen/dmls-book](https://github.com/chiphuyen/dmls-book) | 4,543 | — | — | Summaries and resources for Designing Machine Learning Systems book (Chip Huyen, O'Reilly 2022) |
| [andrewekhalel/MLQuestions](https://github.com/andrewekhalel/MLQuestions) | 4,518 | — | — | Machine Learning and Computer Vision Engineer - Technical Interview Questions |
| [dusty-nv/jetson-containers](https://github.com/dusty-nv/jetson-containers) | 4,487 | — | Jupyter Notebook | Machine Learning Containers for NVIDIA Jetson and JetPack-L4T |
| [openai/simple-evals](https://github.com/openai/simple-evals) | 4,406 | — | Python | — |
| [ed-donner/agents](https://github.com/ed-donner/agents) | 4,372 | — | Jupyter Notebook | Repo for the Complete Agentic AI Engineering Course |
| [microsoft/LMOps](https://github.com/microsoft/LMOps) | 4,301 | — | Python | General technology for enabling AI capabilities w/ LLMs and MLLMs |
| [microsoft/AI-System](https://github.com/microsoft/AI-System) | 4,239 | — | Python | System for AI Education Resource. |
| [openai/grok](https://github.com/openai/grok) | 4,239 | — | Python | — |
| [openai/plugins-quickstart](https://github.com/openai/plugins-quickstart) | 4,238 | — | Python | Get a ChatGPT plugin up and running in under 5 minutes! |
| [openai/harmony](https://github.com/openai/harmony) | 4,235 | — | Rust | Renderer for the harmony response format to be used with gpt-oss |
| [NVIDIA/nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) | 4,159 | — | Go | Build and run containers leveraging NVIDIA GPUs |
| [bambulab/BambuStudio](https://github.com/bambulab/BambuStudio) | 4,135 | — | C++ | PC Software for BambuLab and other 3D printers |
| [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) | 4,133 | — | — | VIP cheatsheet for Stanford's CME 295 Transformers and Large Language Models |
| [github/gh-aw](https://github.com/github/gh-aw) | 4,131 | — | Go | GitHub Agentic Workflows |
| [modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | 4,106 | — | C# | The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft. |
| [mithi/robotics-coursework](https://github.com/mithi/robotics-coursework) | 4,067 | — | — | 🤖 Places where you can learn robotics (and stuff like that) online 🤖 |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | 3,990 | — | Jupyter Notebook | Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes. |
| [QwenLM/Qwen2.5-Omni](https://github.com/QwenLM/Qwen2.5-Omni) | 3,952 | — | Jupyter Notebook | Qwen2.5-Omni is an end-to-end multimodal model by Qwen team at Alibaba Cloud, capable of understanding text, audio, vision, video, and performing real-time speech generation. |
| [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | 3,930 | — | TypeScript | 3D Gaussian Splat Editor |
| [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | 3,916 | — | Python | — |
| [browser-use/workflow-use](https://github.com/browser-use/workflow-use) | 3,907 | — | Python | ⚙️ Create and run workflows (RPA 2.0) |
| [riffusion/riffusion-hobby](https://github.com/riffusion/riffusion-hobby) | 3,883 | — | Python | Stable diffusion for real-time music generation |
| [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | 3,858 | — | Python | An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities. |
| [NVIDIA/GenerativeAIExamples](https://github.com/NVIDIA/GenerativeAIExamples) | 3,856 | — | Jupyter Notebook | Generative AI reference workflows optimized for accelerated infrastructure and microservice architecture. |
| [Facepunch/sbox-public](https://github.com/Facepunch/sbox-public) | 3,839 | — | C# | s&box is a modern game engine, built on Valve's Source 2 and the latest .NET technology, it provides a modern intuitive editor for creating games |
| [openai/improved-diffusion](https://github.com/openai/improved-diffusion) | 3,808 | — | Python | Release for Improved Denoising Diffusion Probabilistic Models |
| [huggingface/course](https://github.com/huggingface/course) | 3,780 | — | MDX | The Hugging Face course on Transformers |
| [termux/termux-x11](https://github.com/termux/termux-x11) | 3,719 | — | C | Termux X-server add-on. |
| [openai/glide-text2im](https://github.com/openai/glide-text2im) | 3,690 | — | Python | GLIDE: a diffusion-based text-conditional image synthesis model |
| [anthropics/original_performance_takehome](https://github.com/anthropics/original_performance_takehome) | 3,687 | — | Python | Anthropic's original performance take-home, now open for you to try! |
| [dagger/container-use](https://github.com/dagger/container-use) | 3,646 | — | Go | Development environments for coding agents. Enable multiple agents to work safely and independently with your preferred stack. |
| [rasbt/reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch) | 3,606 | — | Jupyter Notebook | Implement a reasoning LLM in PyTorch from scratch, step by step |
| [openai/retro](https://github.com/openai/retro) | 3,575 | — | C | Retro Games in Gym |
| [Azure/PyRIT](https://github.com/Azure/PyRIT) | 3,567 | — | Python | The Python Risk Identification Tool for generative AI (PyRIT) is an open source framework built to empower security professionals and engineers to proactively identify risks in generative AI systems. |
| [openai/openai-realtime-console](https://github.com/openai/openai-realtime-console) | 3,566 | — | JavaScript | React app for inspecting, building and debugging with the Realtime API |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | 3,553 | — | TypeScript | OpenClaw-RL: Train any agent simply by talking |
| [archestra-ai/archestra](https://github.com/archestra-ai/archestra) | 3,542 | — | TypeScript | Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator |
| [tobi/try](https://github.com/tobi/try) | 3,516 | — | Ruby | fresh directories for every vibe |
| [microsoft/tensorwatch](https://github.com/microsoft/tensorwatch) | 3,466 | — | Jupyter Notebook | Debugging, monitoring and visualization for Python Machine Learning and Data Science |
| [jellyfin/jellyfin-web](https://github.com/jellyfin/jellyfin-web) | 3,442 | — | JavaScript | The Free Software Media System - Official Web Client |
| [facebookresearch/sam-audio](https://github.com/facebookresearch/sam-audio) | 3,393 | — | Python | The repository provides code for running inference with the Meta Segment Anything Audio Model (SAM-Audio), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. |
| [Infatoshi/cuda-course](https://github.com/Infatoshi/cuda-course) | 3,385 | — | Cuda | CUDA Course on FreeCodeCamp |
| [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | 3,346 | — | C | Open-source, low-cost 10.5 GHz PLFM phased array RADAR system |
| [IDEA-Research/Grounded-SAM-2](https://github.com/IDEA-Research/Grounded-SAM-2) | 3,334 | — | Jupyter Notebook | Grounded SAM 2: Ground and Track Anything in Videos with Grounding DINO, Florence-2 and SAM 2 |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | 3,315 | — | TypeScript | Annotate and review coding agent plans and code diffs visually, share with your team, send feedback to agents with one click. |
| [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | 3,302 | — | Python | OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch.  |
| [Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) | 3,298 | — | Python | LTX-Video Support for ComfyUI |
| [NVIDIA/flownet2-pytorch](https://github.com/NVIDIA/flownet2-pytorch) | 3,276 | — | Python | Pytorch implementation of FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks |
| [aadi1011/AI-ML-Roadmap-from-scratch](https://github.com/aadi1011/AI-ML-Roadmap-from-scratch) | 3,238 | — | — | Become skilled in Artificial Intelligence, Machine Learning, Generative AI, Deep Learning, Data Science, Natural Language Processing, Reinforcement Learning and more with this complete 0 to 100 repository. |
| [magenta/ddsp](https://github.com/magenta/ddsp) | 3,234 | — | Python |  DDSP: Differentiable Digital Signal Processing |
| [NVIDIA/TransformerEngine](https://github.com/NVIDIA/TransformerEngine) | 3,225 | — | Python | A library for accelerating Transformer models on NVIDIA GPUs, including using 8-bit and 4-bit floating point (FP8 and FP4) precision on Hopper, Ada and Blackwell GPUs, to provide better performance with lower memory utilization in both training and inference. |
| [chenyme/grok2api](https://github.com/chenyme/grok2api) | 3,193 | — | Python | 基于 FastAPI 构建的 Grok2API，全面适配 OpenAI 兼容的调用格式，支持流式/非流式对话、图像生成、图像编辑、视频生成、工具调用、语音聊天、一键NSFW、号池并发与自动负载均衡一体化。 |
| [NVIDIA/cuda-python](https://github.com/NVIDIA/cuda-python) | 3,189 | — | Cython | CUDA Python: Performance meets Productivity |
| [Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor) | 3,188 | — | TypeScript | An app to monitor the (Codex) situation |
| [openai/glow](https://github.com/openai/glow) | 3,181 | — | Python | Code for reproducing results in "Glow: Generative Flow with Invertible 1x1 Convolutions" |
| [openai/human-eval](https://github.com/openai/human-eval) | 3,167 | — | Python | Code for the paper "Evaluating Large Language Models Trained on Code" |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | 3,166 | — | TypeScript | Agent Skills as a Memory Layer |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | 3,159 | — | Shell | TinyClaw is a team of personal agents that collaborate with each other |
| [openai/mujoco-py](https://github.com/openai/mujoco-py) | 3,117 | — | Cython | MuJoCo is a physics engine for detailed, efficient rigid body simulations with contacts. mujoco-py allows using MuJoCo from Python 3. |
| [ericc-ch/copilot-api](https://github.com/ericc-ch/copilot-api) | 3,071 | — | TypeScript | Turn GitHub Copilot into OpenAI/Anthropic API compatible server. Usable with Claude Code! |
| [openai/openai-go](https://github.com/openai/openai-go) | 3,066 | — | Go | The official Go library for the OpenAI API |
| [rsxdalv/TTS-WebUI](https://github.com/rsxdalv/TTS-WebUI) | 3,020 | — | TypeScript | A single Gradio + React WebUI with extensions for ACE-Step, Kimi Audio, Piper TTS, GPT-SoVITS, CosyVoice, XTTSv2, DIA, Kokoro, OpenVoice, ParlerTTS, Stable Audio, MMS, StyleTTS2, MAGNet, AudioGen, MusicGen, Tortoise, RVC, Vocos, Demucs, SeamlessM4T, and Bark! |
| [maximhq/bifrost](https://github.com/maximhq/bifrost) | 3,018 | — | Go | Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS. |
| [brave/brave-core](https://github.com/brave/brave-core) | 3,016 | — | C++ | Core engine for the Brave browser for mobile and desktop. For issues https://github.com/brave/brave-browser/issues |
| [GoogleCloudPlatform/professional-services](https://github.com/GoogleCloudPlatform/professional-services) | 3,010 | — | Python | Common solutions and tools developed by Google Cloud's Professional Services team. This repository and its contents are not an officially supported Google product. |
| [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | 2,990 | — | Python | GLM-OCR: Accurate ×  Fast × Comprehensive |
| [anthropics/anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) | 2,977 | — | Python | — |
| [geo-tp/ESP32-Bus-Pirate](https://github.com/geo-tp/ESP32-Bus-Pirate) | 2,965 | — | C++ | A Hardware Hacking Tool with Web-Based CLI That Speaks Every Protocol  |
| [GoogleCloudPlatform/nodejs-docs-samples](https://github.com/GoogleCloudPlatform/nodejs-docs-samples) | 2,964 | — | JavaScript | Node.js samples for Google Cloud Platform products. |
| [mazzzystar/Queryable](https://github.com/mazzzystar/Queryable) | 2,926 | — | Swift | Run OpenAI's CLIP and Apple's MobileCLIP model on iOS to search photos. |
| [voidzero-dev/vite-plus](https://github.com/voidzero-dev/vite-plus) | 2,897 | — | Rust | Vite+ is the unified toolchain and entry point for web development. It manages your runtime, package manager, and frontend toolchain in one place. |
| [microsoft/genaiscript](https://github.com/microsoft/genaiscript) | 2,891 | — | TypeScript | Automatable GenAI Scripting |
| [NVIDIA/MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine) | 2,886 | — | Python | Minkowski Engine is an auto-diff neural network library for high-dimensional sparse tensors |
| [NVIDIA/NeMo-Retriever](https://github.com/NVIDIA/NeMo-Retriever) | 2,874 | — | Python | NeMo Retriever Library is a scalable, performance-oriented document content and metadata extraction microservice. NeMo Retriever extraction uses specialized NVIDIA NIM microservices to find, contextualize, and extract text, tables, charts and images that you can use in downstream generative applications. |
| [google-gemini/computer-use-preview](https://github.com/google-gemini/computer-use-preview) | 2,867 | — | Python | — |
| [GoogleCloudPlatform/tensorflow-without-a-phd](https://github.com/GoogleCloudPlatform/tensorflow-without-a-phd) | 2,841 | — | Jupyter Notebook | A crash course in six episodes for software developers who want to become machine learning practitioners. |
| [openai/openai-fm](https://github.com/openai/openai-fm) | 2,825 | — | TypeScript | Code for openai.fm, a demo for the OpenAI Speech API |
| [microsoft/mcp](https://github.com/microsoft/mcp) | 2,808 | — | C# | Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration |
| [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | 2,806 | — | Python | GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website — citability scoring, AI crawler analysis, brand authority, schema markup, platform-specific optimization, and PDF reports.  If you want learn how to sell this to real businesses, check out the skool community |
| [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | 2,805 | — | Python | A specialized Claude Code workspace for creating long-form, SEO-optimized blog content for any business. This system helps you research, write, analyze, and optimize content that ranks well and serves your target audience. |
| [qdrant/fastembed](https://github.com/qdrant/fastembed) | 2,785 | — | Python | Fast, Accurate, Lightweight Python library to make State of the Art Embedding |
| [google-gemini/gemma-cookbook](https://github.com/google-gemini/gemma-cookbook) | 2,746 | — | Jupyter Notebook | A collection of guides and examples for the Gemma open models from Google. |
| [gcui-art/suno-api](https://github.com/gcui-art/suno-api) | 2,741 | — | TypeScript | Use API to call the music generation AI of suno.ai, and easily integrate it into agents like GPTs. |
| [openai/multiagent-particle-envs](https://github.com/openai/multiagent-particle-envs) | 2,740 | — | Python | Code for a multi-agent particle environment used in the paper "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments" |
| [ErsatzTV/ErsatzTV](https://github.com/ErsatzTV/ErsatzTV) | 2,723 | — | C# | Open-source platform that transforms your personal media library into live, custom TV channels. |
| [TheAlgorithms/TypeScript](https://github.com/TheAlgorithms/TypeScript) | 2,694 | — | TypeScript | Algorithms and Data Structures implemented in TypeScript for beginners, following best practices. |
| [openai/openai-quickstart-node](https://github.com/openai/openai-quickstart-node) | 2,631 | — | JavaScript | Node.js example app from the OpenAI API quickstart tutorial |
| [dmno-dev/varlock](https://github.com/dmno-dev/varlock) | 2,629 | — | TypeScript | .env files built for sharing powered by @env-spec decorator comments |
| [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio) | 2,574 | — | C++ | LichtFeld Studio: Where reality and the digital world blend. |
| [openai/weak-to-strong](https://github.com/openai/weak-to-strong) | 2,550 | — | Python | — |
| [dynobo/normcap](https://github.com/dynobo/normcap) | 2,546 | — | Python | OCR powered screen-capture tool to capture information instead of images |
| [anthropics/claudes-c-compiler](https://github.com/anthropics/claudes-c-compiler) | 2,544 | — | Rust | Claude Opus 4.6 wrote a dependency-free C compiler in Rust, with backends targeting x86 (64- and 32-bit), ARM, and RISC-V, capable of compiling a booting Linux kernel. |
| [openai/openai-dotnet](https://github.com/openai/openai-dotnet) | 2,537 | — | C# | The official .NET library for the OpenAI API |
| [GoogleCloudPlatform/asl-ml-immersion](https://github.com/GoogleCloudPlatform/asl-ml-immersion) | 2,509 | — | Jupyter Notebook | This repos contains notebooks for the Advanced Solutions Lab: ML Immersion |
| [google-gemini/live-api-web-console](https://github.com/google-gemini/live-api-web-console) | 2,499 | — | TypeScript | A react-based starter app for using the Live API over websockets with Gemini |
| [openai/openai-agents-js](https://github.com/openai/openai-agents-js) | 2,487 | — | TypeScript | A lightweight, powerful framework for multi-agent workflows and voice agents |
| [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | 2,425 | — | TypeScript | Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered—anytime, anywhere. |
| [milvus-io/bootcamp](https://github.com/milvus-io/bootcamp) | 2,395 | — | Jupyter Notebook | Dealing with all unstructured data, such as reverse image search, audio search, molecular search, video analysis, question and answer systems, NLP, etc. |
| [ray-project/kuberay](https://github.com/ray-project/kuberay) | 2,380 | — | Go | A toolkit to run Ray applications on Kubernetes |
| [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | 2,358 | — | JavaScript | Synkra AIOS: AI-Orchestrated System for Full Stack Development - Core Framework v4.0 |
| [NVIDIA/CUDALibrarySamples](https://github.com/NVIDIA/CUDALibrarySamples) | 2,349 | — | C++ | CUDA Library Samples |
| [renode/renode](https://github.com/renode/renode) | 2,339 | — | RobotFramework | Renode - Antmicro's open source simulation and virtual development framework for complex embedded systems |
| [openai/openai-openapi](https://github.com/openai/openai-openapi) | 2,339 | — | — | OpenAPI specification for the OpenAI API |
| [NVIDIA/waveglow](https://github.com/NVIDIA/waveglow) | 2,339 | — | Python | A Flow-based Generative Network for Speech Synthesis |
| [openai/improved-gan](https://github.com/openai/improved-gan) | 2,336 | — | Python | Code for the paper "Improved Techniques for Training GANs" |
| [openlit/openlit](https://github.com/openlit/openlit) | 2,294 | — | Python | Open source platform for AI Engineering: OpenTelemetry-native LLM Observability, GPU Monitoring, Guardrails, Evaluations, Prompt Management, Vault, Playground. 🚀💻 Integrates with 50+ LLM Providers, VectorDBs, Agent Frameworks and GPUs. |
| [openai/finetune-transformer-lm](https://github.com/openai/finetune-transformer-lm) | 2,283 | — | Python | Code and model for the paper "Improving Language Understanding by Generative Pre-Training" |
| [google/XNNPACK](https://github.com/google/XNNPACK) | 2,277 | — | C | High-efficiency floating-point neural network inference operators for mobile, server, and Web |
| [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) | 2,270 | — | — | Skills for the Gemini API, SDK and model/agent interactions |
| [google-gemini/deprecated-generative-ai-python](https://github.com/google-gemini/deprecated-generative-ai-python) | 2,267 | — | Python | This SDK is now deprecated, use the new unified Google GenAI SDK.  |
| [google/generative-ai-docs](https://github.com/google/generative-ai-docs) | 2,238 | — | Jupyter Notebook | This repository is deprecated and will be archived |
| [ZHZisZZ/dllm](https://github.com/ZHZisZZ/dllm) | 2,234 | — | Python | dLLM: Simple Diffusion Language Modeling |
| [GoogleCloudPlatform/gcsfuse](https://github.com/GoogleCloudPlatform/gcsfuse) | 2,217 | — | Go | A user-space file system for interacting with Google Cloud Storage |
| [openai/consistencydecoder](https://github.com/openai/consistencydecoder) | 2,213 | — | Python | Consistency Distilled Diff VAE |
| [openai/roboschool](https://github.com/openai/roboschool) | 2,169 | — | Python | DEPRECATED: Open-source software for robot simulation, integrated with OpenAI Gym. |
| [openai/openai-apps-sdk-examples](https://github.com/openai/openai-apps-sdk-examples) | 2,153 | — | TypeScript | Example apps for the Apps SDK |
| [torinmb/mediapipe-touchdesigner](https://github.com/torinmb/mediapipe-touchdesigner) | 2,127 | — | JavaScript | GPU Accelerated MediaPipe Plugin for TouchDesigner |
| [magenta/magenta-js](https://github.com/magenta/magenta-js) | 2,113 | — | TypeScript | Magenta.js: Music and Art Generation with Machine Learning in the browser |
| [PRBonn/kiss-icp](https://github.com/PRBonn/kiss-icp) | 2,108 | — | C++ | A LiDAR odometry pipeline that just works |
| [openai/prm800k](https://github.com/openai/prm800k) | 2,105 | — | Python | 800,000 step-level correctness labels on LLM solutions to MATH problems |
| [openai/image-gpt](https://github.com/openai/image-gpt) | 2,088 | — | Python | — |
| [google-gemini/genai-processors](https://github.com/google-gemini/genai-processors) | 2,078 | — | Python | GenAI Processors is a lightweight Python library that enables efficient, parallel content processing. |
| [GoogleCloudPlatform/ml-design-patterns](https://github.com/GoogleCloudPlatform/ml-design-patterns) | 2,073 | — | Jupyter Notebook | Source code accompanying O'Reilly book: Machine Learning Design Patterns |
| [jamubc/gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool) | 2,072 | — | TypeScript | MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding |
| [geode-sdk/geode](https://github.com/geode-sdk/geode) | 2,047 | — | C++ | The ultimate Geometry Dash modding framework |
| [NVIDIA/NeMo-Agent-Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | 2,028 | — | Python | The NVIDIA NeMo Agent toolkit is an open-source library for efficiently connecting and optimizing teams of AI agents. |
| [GoogleCloudPlatform/PerfKitBenchmarker](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker) | 2,001 | — | Python | PerfKit Benchmarker (PKB) contains a set of benchmarks to measure and compare cloud offerings. The benchmarks use default settings to reflect what most users will see. PerfKit Benchmarker is licensed under the Apache 2 license terms. Please make sure to read, understand and agree to the terms of the LICENSE and CONTRIBUTING files before proceeding. |
| [Circuit-Digest/ESP-Drone](https://github.com/Circuit-Digest/ESP-Drone) | 1,996 | — | C | — |
| [NVIDIA/Stable-Diffusion-WebUI-TensorRT](https://github.com/NVIDIA/Stable-Diffusion-WebUI-TensorRT) | 1,995 | — | Python | TensorRT Extension for Stable Diffusion Web UI |
| [zhukunpenglinyutong/idea-claude-code-gui](https://github.com/zhukunpenglinyutong/idea-claude-code-gui) | 1,995 | — | TypeScript | IDEA Claude Code GUI Plugin |
| [openai/openai-assistants-quickstart](https://github.com/openai/openai-assistants-quickstart) | 1,964 | — | TypeScript | OpenAI Assistants API quickstart with Next.js. |
| [google-ai-edge/LiteRT](https://github.com/google-ai-edge/LiteRT) | 1,960 | — | C++ | LiteRT, successor to TensorFlow Lite. is Google's On-device framework for high-performance ML & GenAI deployment on edge platforms, via efficient conversion, runtime, and optimization |
| [thesysdev/openui](https://github.com/thesysdev/openui) | 1,951 | — | TypeScript | The Open Standard for Generative UI |
| [apache/burr](https://github.com/apache/burr) | 1,948 | — | Python | Build applications that make decisions (chatbots, agents, simulations, etc...). Monitor, trace, persist, and execute on your own infrastructure. |
| [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | 1,946 | — | Shell | A tremendous feat of documentation, this guide covers Claude Code from beginner to power user, with production-ready templates for Claude Code features, guides on agentic workflows, and a lot of great learning materials, including quizzes and a handy "cheatsheet". Whether it's the "ultimate" guide to Claude Code will be up to the reader :) |
| [win4r/AISuperDomain](https://github.com/win4r/AISuperDomain) | 1,934 | — | C# | Aila(AI超元域): The premier AI integration tool for Windows, macOS, and Android. Ask once, get answers from 10+ AIs like ChatGPT, Gemini, Claude3, Copilot, Poe, perplexity and more. Features customizable AI and prompts. |
| [letta-ai/letta-code](https://github.com/letta-ai/letta-code) | 1,902 | — | TypeScript | The memory-first coding agent |
| [weaviate/elysia](https://github.com/weaviate/elysia) | 1,881 | — | Python | Python package and backend for the Elysia platform app. |
| [google-github-actions/run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli) | 1,867 | — | TypeScript | A GitHub Action invoking the Gemini CLI. |
| [browser-use/macOS-use](https://github.com/browser-use/macOS-use) | 1,862 | — | Python | Make Mac apps accessible for AI agents |
| [MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals) | 1,862 | — | — | — |
| [openai/gpt-5-coding-examples](https://github.com/openai/gpt-5-coding-examples) | 1,855 | — | HTML | GPT-5 coding examples |
| [allenk/GeminiWatermarkTool](https://github.com/allenk/GeminiWatermarkTool) | 1,853 | — | C++ | Gemini Nano Banana / Pro watermark maintenance tool |
| [anthropics/hh-rlhf](https://github.com/anthropics/hh-rlhf) | 1,830 | — | — | Human preference data for "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback" |
| [NVIDIA/semantic-segmentation](https://github.com/NVIDIA/semantic-segmentation) | 1,816 | — | Python | Nvidia Semantic Segmentation monorepo |
| [vmayoral/ros-robotics-companies](https://github.com/vmayoral/ros-robotics-companies) | 1,784 | — | Shell | A list of robotics companies using the Robot Operating System (ROS and ROS 2).  |
| [NVIDIA/aistore](https://github.com/NVIDIA/aistore) | 1,784 | — | Go | AIStore: scalable storage for AI applications |
| [agno-agi/dash](https://github.com/agno-agi/dash) | 1,779 | — | Python | Self-learning data agent that grounds its answers in 6 layers of context. Inspired by OpenAI's in-house implementation. |
| [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | 1,755 | — | Python | The Dimensional Framework |
| [anthropics/claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos) | 1,749 | — | TypeScript | Claude Code SDK Demos |
| [csteinmetz1/ai-audio-startups](https://github.com/csteinmetz1/ai-audio-startups) | 1,743 | — | — | Community list of startups working with AI in audio and music technology |
| [anthropics/anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript) | 1,735 | — | TypeScript | Access to Anthropic's safety-first language model APIs in TypeScript |
| [Comfy-Org/ComfyUI_frontend](https://github.com/Comfy-Org/ComfyUI_frontend) | 1,707 | — | TypeScript | Official front-end implementation of ComfyUI |
| [magenta/mt3](https://github.com/magenta/mt3) | 1,685 | — | Python | MT3: Multi-Task Multitrack Music Transcription |
| [agno-agi/agent-ui](https://github.com/agno-agi/agent-ui) | 1,678 | — | TypeScript | A modern chat interface for AI agents built with Next.js, Tailwind CSS, and TypeScript.  |
| [Intent-Lab/VisionClaw](https://github.com/Intent-Lab/VisionClaw) | 1,671 | — | — | Real-time AI assistant for Meta Ray-Ban smart glasses -- voice + vision + agentic actions via Gemini Live and OpenClaw |
| [openai/Video-Pre-Training](https://github.com/openai/Video-Pre-Training) | 1,663 | — | Python | Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online Videos |
| [google/aiyprojects-raspbian](https://github.com/google/aiyprojects-raspbian) | 1,660 | — | Python |  API libraries, samples, and system images for AIY Projects (Voice Kit and Vision Kit) |
| [openai/openai-realtime-embedded](https://github.com/openai/openai-realtime-embedded) | 1,582 | — | — | Instructions on how to use the Realtime API on Microcontrollers and Embedded Platforms |
| [dune3d/dune3d](https://github.com/dune3d/dune3d) | 1,569 | — | C | 3D CAD application |
| [GoogleCloudPlatform/localllm](https://github.com/GoogleCloudPlatform/localllm) | 1,549 | — | Python | — |
| [databricks/megablocks](https://github.com/databricks/megablocks) | 1,546 | — | Python | — |
| [Paulescu/hands-on-rl](https://github.com/Paulescu/hands-on-rl) | 1,539 | — | Jupyter Notebook | Free course that takes you from zero to Reinforcement Learning PRO 🦸🏻‍🦸🏽 |
| [GoogleCloudPlatform/cloudml-samples](https://github.com/GoogleCloudPlatform/cloudml-samples) | 1,539 | — | Python | Cloud ML Engine repo. Please visit the new Vertex AI samples repo at https://github.com/GoogleCloudPlatform/vertex-ai-samples |
| [deepseek-ai/DeepSeek-V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) | 1,511 | — | Python | — |
| [raphaelmansuy/edgequake](https://github.com/raphaelmansuy/edgequake) | 1,475 | — | Rust | High-performance GraphRAG inspired from LightRag written in Rust |
| [DocumindHQ/documind](https://github.com/DocumindHQ/documind) | 1,464 | — | JavaScript | Open-source platform for extracting structured data from documents using AI. |
| [FareedKhan-dev/all-rl-algorithms](https://github.com/FareedKhan-dev/all-rl-algorithms) | 1,463 | — | Jupyter Notebook | Implementation of all RL algorithms in a simpler way |
| [Snowflake-Labs/pg_lake](https://github.com/Snowflake-Labs/pg_lake) | 1,461 | — | C | pg_lake: Postgres with Iceberg and data lake access |
| [GoogleCloudPlatform/cloud-builders](https://github.com/GoogleCloudPlatform/cloud-builders) | 1,448 | — | Go | Builder images and examples commonly used for Google Cloud Build |
| [protectai/rebuff](https://github.com/protectai/rebuff) | 1,445 | — | TypeScript | LLM Prompt Injection Detector |
| [unchihugo/FluentFlyout](https://github.com/unchihugo/FluentFlyout) | 1,433 | — | C# | The modern Flyout app for Windows 11, built with Fluent 2 Design principles. Media Flyouts, Taskbar Widgets and more. |
| [GoogleCloudPlatform/data-science-on-gcp](https://github.com/GoogleCloudPlatform/data-science-on-gcp) | 1,421 | — | Jupyter Notebook | Source code accompanying book: Data Science on the Google Cloud Platform, Valliappa Lakshmanan, O'Reilly 2017 |
| [google/oss-fuzz-gen](https://github.com/google/oss-fuzz-gen) | 1,375 | — | Python | LLM powered fuzzing via OSS-Fuzz. |
| [NVIDIA/VideoProcessingFramework](https://github.com/NVIDIA/VideoProcessingFramework) | 1,375 | — | C++ | Set of Python bindings to C++ libraries which provides full HW acceleration for video decoding, encoding and GPU-accelerated color space and pixel format conversions |
| [google/adk-java](https://github.com/google/adk-java) | 1,369 | — | Java | An open-source, code-first Java toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) | 1,357 | — | C# | AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project. |
| [milvus-io/pymilvus](https://github.com/milvus-io/pymilvus) | 1,355 | — | Python | Python SDK for Milvus Vector Database |
| [magenta/magenta-demos](https://github.com/magenta/magenta-demos) | 1,348 | — | Jupyter Notebook | Demonstrations of Magenta Models |
| [Seeed-Projects/reBot-DevArm](https://github.com/Seeed-Projects/reBot-DevArm) | 1,307 | — | — | Open Source Robotic Arm for All Developers |
| [GoogleCloudPlatform/cloud-builders-community](https://github.com/GoogleCloudPlatform/cloud-builders-community) | 1,305 | — | Go | Community-contributed images for Google Cloud Build |
| [GoogleCloudPlatform/bank-of-anthos](https://github.com/GoogleCloudPlatform/bank-of-anthos) | 1,305 | — | Java | Retail banking sample application showcasing Kubernetes and Google Cloud |
| [PRBonn/depth_clustering](https://github.com/PRBonn/depth_clustering) | 1,299 | — | C++ | :taxi: Fast and robust clustering of point clouds generated with a Velodyne sensor.  |
| [GoogleCloudPlatform/berglas](https://github.com/GoogleCloudPlatform/berglas) | 1,295 | — | Go | A tool for managing secrets on Google Cloud |
| [google-gemini/starter-applets](https://github.com/google-gemini/starter-applets) | 1,294 | — | TypeScript | Google AI Studio Starter Apps |
| [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) | 1,288 | — | Python | An official Qdrant Model Context Protocol (MCP) server implementation |
| [KalyanKS-NLP/rag-zero-to-hero-guide](https://github.com/KalyanKS-NLP/rag-zero-to-hero-guide) | 1,277 | — | Jupyter Notebook | Comprehensive guide to learn RAG from basics to advanced.  |
| [melpon/wandbox](https://github.com/melpon/wandbox) | 1,256 | — | TypeScript | Social Compilation Service |
| [zed-industries/claude-agent-acp](https://github.com/zed-industries/claude-agent-acp) | 1,254 | — | TypeScript | Use Claude Agent SDK from any ACP client such as Zed! |
| [qdrant/qdrant-client](https://github.com/qdrant/qdrant-client) | 1,244 | — | Python | Python client for Qdrant vector search engine |
| [alexeygrigorev/ai-engineering-field-guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) | 1,234 | — | HTML | Research into AI engineering interview assignments, take-home challenges, and hiring practices from Q4 2025 / Q1 2026 |
| [google/adk-docs](https://github.com/google/adk-docs) | 1,232 | — | Python | An open-source, code-first toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [cfregly/ai-performance-engineering](https://github.com/cfregly/ai-performance-engineering) | 1,217 | — | Python | — |
| [magenta/magenta-studio](https://github.com/magenta/magenta-studio) | 1,217 | — | JavaScript | Magenta Studio is a collection of music plugins built on Magenta’s open source tools and models |
| [NVlabs/GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl) | 1,205 | — | C++ | Welcome to GR00T Whole-Body Control (WBC)! This is a unified platform for developing and deploying advanced humanoid controllers. This includes: Decoupled WBC models used in NVIDIA Isaac-Gr00t, Gr00t N1.5 and N1.6 and GEAR-SONIC  |
| [wandb/examples](https://github.com/wandb/examples) | 1,202 | — | Jupyter Notebook | Example deep learning projects that use wandb's features. |
| [ageron/handson-mlp](https://github.com/ageron/handson-mlp) | 1,184 | — | Jupyter Notebook | A series of Jupyter notebooks that walk you through the fundamentals of Machine Learning and Deep Learning in Python using Scikit-Learn, PyTorch, and Hugging Face libraries. |
| [mavlink/mavros](https://github.com/mavlink/mavros) | 1,135 | — | C++ | MAVLink to ROS gateway with proxy for Ground Control Station |
| [engcang/SLAM-application](https://github.com/engcang/SLAM-application) | 1,122 | — | C++ | LeGO-LOAM, LIO-SAM, LVI-SAM, FAST-LIO2, Faster-LIO, VoxelMap, R3LIVE, Point-LIO, KISS-ICP, DLO, DLIO, Ada-LIO, PV-LIO, SLAMesh, ImMesh, FAST-LIO-MULTI, M-LOAM, LOCUS, SLICT, MA-LIO, CT-ICP, GenZ-ICP, iG-LIO, SR-LIO application and comparison on Gazebo and real-world datasets. Installation and config files are provided.  |
| [cline/prompts](https://github.com/cline/prompts) | 1,105 | — | — | Library of prompts from the Cline community |
| [QwenLM/Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math) | 1,068 | — | Python | A series of math-specific large language models of our Qwen2 series. |
| [decolua/9router](https://github.com/decolua/9router) | 1,066 | — | JavaScript | Connect All AI Code Tools (Claude Code, Cursor, Antigravity, Copilot, Codex, Gemini, OpenCode, Cline, OpenClaw...) to 40+ AI Providers & 100+ Models |
| [wandb/weave](https://github.com/wandb/weave) | 1,061 | — | Python | Weave is a toolkit for developing AI-powered applications, built by Weights & Biases. |
| [unjs/unpdf](https://github.com/unjs/unpdf) | 1,051 | — | TypeScript | 📄 PDF extraction and rendering across all JavaScript runtimes |
| [PRBonn/lidar-bonnetal](https://github.com/PRBonn/lidar-bonnetal) | 1,033 | — | Python | Semantic and Instance Segmentation of LiDAR point clouds for autonomous driving |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 1,011 | — | CSS | Kolibri Learning Platform: the offline app for universal education |
| [magenta/magenta-realtime](https://github.com/magenta/magenta-realtime) | 1,009 | — | Python | Google Magenta RT forked |
| [metauto-ai/GPTSwarm](https://github.com/metauto-ai/GPTSwarm) | 1,008 | — | Python | 🐝  The First Self-Improving Agentic Solution |
| [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering) | 1,004 | — | Python | — |
| [PRBonn/semantic_suma](https://github.com/PRBonn/semantic_suma) | 999 | — | C++ | SuMa++: Efficient LiDAR-based Semantic SLAM (Chen et al IROS 2019) |
| [anthropics/claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript) | 979 | — | Shell | — |
| [DataExpert-io/ai-engineer-handbook](https://github.com/DataExpert-io/ai-engineer-handbook) | 960 | — | — | All the links, books, and creators you need to follow to stay up to date with AI! |
| [google/adk-js](https://github.com/google/adk-js) | 914 | — | TypeScript | An open-source, code-first Typescript toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [PRBonn/semantic-kitti-api](https://github.com/PRBonn/semantic-kitti-api) | 892 | — | Python | SemanticKITTI API for visualizing dataset, processing data, and evaluating results. |
| [7836246/cursor2api](https://github.com/7836246/cursor2api) | 883 | — | TypeScript | 将 Cursor API 转换为 OpenAI/Anthropic 兼容格式的代理服务。提供 Claude Code工具及图片支持。 |
| [kaplanelad/shellfirm](https://github.com/kaplanelad/shellfirm) | 883 | — | Rust | Safety guardrails for ai coding agents and human terminal commands |
| [carlosmccosta/dynamic_robot_localization](https://github.com/carlosmccosta/dynamic_robot_localization) | 873 | — | C++ | Point cloud registration pipeline for robot localization and 3D perception |
| [google/generative-ai-go](https://github.com/google/generative-ai-go) | 853 | — | Go | Go SDK for Google Generative AI |
| [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | 853 | — | JavaScript | Skills for pi coding agent (compatible with Claude Code and Codex CLI) |
| [AnswerDotAI/fasthtml-example](https://github.com/AnswerDotAI/fasthtml-example) | 831 | — | CSS | Example fasthtml applications demonstrating a range of web programming techniques |
| [FreddeFrallan/Multilingual-CLIP](https://github.com/FreddeFrallan/Multilingual-CLIP) | 828 | — | Jupyter Notebook | OpenAI CLIP text encoders for multiple languages! |
| [GoogleCloudPlatform/dotnet-docs-samples](https://github.com/GoogleCloudPlatform/dotnet-docs-samples) | 828 | — | C# | .NET code samples used on https://cloud.google.com |
| [linorobot/linorobot2](https://github.com/linorobot/linorobot2) | 827 | — | Python | Autonomous mobile robots (2WD, 4WD, Mecanum Drive) |
| [browser-use/vibetest-use](https://github.com/browser-use/vibetest-use) | 778 | — | Python | Vibetest MCP - automated QA testing using Browser-Use agents |
| [NVIDIA/cuopt](https://github.com/NVIDIA/cuopt) | 765 | — | Cuda | GPU accelerated decision optimization  |
| [NVIDIA-NeMo/Gym](https://github.com/NVIDIA-NeMo/Gym) | 747 | — | Python | Build RL environments for LLM training |
| [getnao/nao](https://github.com/getnao/nao) | 743 | — | TypeScript | 👾 nao is an open source analytics agent. (1) Create context with nao-core cli, (2) deploy nao chat interface for everyone |
| [PRBonn/OverlapNet](https://github.com/PRBonn/OverlapNet) | 721 | — | Python | OverlapNet - Loop Closing for 3D LiDAR-based SLAM (chen2020rss) |
| [Zasder3/train-CLIP](https://github.com/Zasder3/train-CLIP) | 720 | — | Python | A PyTorch Lightning solution to training OpenAI's CLIP from scratch. |
| [OpenRL-Lab/Wandb_Tutorial](https://github.com/OpenRL-Lab/Wandb_Tutorial) | 698 | — | Python | How to use wandb? |
| [NVIDIA-NeMo/Nemotron](https://github.com/NVIDIA-NeMo/Nemotron) | 688 | — | Jupyter Notebook | Developer Asset Hub for NVIDIA Nemotron — A one-stop resource for training recipes, usage cookbooks, datasets, and full end-to-end reference examples to build with Nemotron models |
| [mathiasmantelli/awesome-mobile-robotics](https://github.com/mathiasmantelli/awesome-mobile-robotics) | 676 | — | — | Useful links of different content related to AI, Computer Vision, and Robotics. |
| [wandb/edu](https://github.com/wandb/edu) | 668 | — | Jupyter Notebook | Educational materials on deep learning by Weights & Biases |
| [gtbook/robotics](https://github.com/gtbook/robotics) | 663 | — | Jupyter Notebook | Notebook-based book "Introduction to Robotics and Perception" by Frank Dellaert and Seth Hutchinson |
| [mem0ai/mem0-chrome-extension](https://github.com/mem0ai/mem0-chrome-extension) | 660 | — | TypeScript | OpenMemory Chrome Extension: Long-term memory for ChatGPT, Claude, Perplexity, Grok etc |
| [Snowflake-Labs/schemachange](https://github.com/Snowflake-Labs/schemachange) | 647 | — | Python | A Database Change Management tool for Snowflake |
| [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) | 637 | — | Python | — |
| [landing-ai/ade-python](https://github.com/landing-ai/ade-python) | 621 | — | Python | Python library for Agentic Document Extraction (ADE). |
| [anthropics/claude-code-base-action](https://github.com/anthropics/claude-code-base-action) | 611 | — | TypeScript | This repo is a mirror of the contents of base-action in https://github.com/anthropics/claude-code-action. |
| [engcang/vins-application](https://github.com/engcang/vins-application) | 587 | — | C++ | VINS-Fusion, VINS-Fisheye, OpenVINS, EnVIO, ROVIO, S-MSCKF, ORB-SLAM2, NVIDIA Elbrus application of different sets of cameras and imu on different board including desktop and Jetson boards |
| [lumalabs/imm](https://github.com/lumalabs/imm) | 577 | — | Python | Official implementation of Inductive Moment Matching |
| [Snowflake-Labs/snowflake-arctic](https://github.com/Snowflake-Labs/snowflake-arctic) | 560 | — | Python | — |
| [Snowflake-Labs/Snowflake-AI-Toolkit](https://github.com/Snowflake-Labs/Snowflake-AI-Toolkit) | 553 | — | Python | Snowflake AI Toolkit is an AI Accelerator and Playground for enabling AI in Snowflake. It is an Plug and Play Streamlit based Native App that can be used to explore, learn and build rapid prototypes of AI Solutions in Snowflake powered by the Snowflake's Cortex and AI Functions.  |
| [asimovinc/asimov-v0](https://github.com/asimovinc/asimov-v0) | 552 | — | — | v0 of Asimov, an open-source humanoid robot |
| [unbody-io/unbody](https://github.com/unbody-io/unbody) | 516 | — | TypeScript | The Supabase of AI era. A modular, open-source backend for building AI-native software — designed for knowledge, not static data. |
| [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) | 515 | — | Python | A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma |
| [wafer-ai/gpu-perf-engineering-resources](https://github.com/wafer-ai/gpu-perf-engineering-resources) | 478 | — | — | A curriculum for learning about gpu performance engineering, from scratch to what the frontier AI labs do |
| [google/cameratrapai](https://github.com/google/cameratrapai) | 478 | — | Python | AI models trained by Google to classify species in images from motion-triggered wildlife cameras. |
| [NVIDIA/cuopt-examples](https://github.com/NVIDIA/cuopt-examples) | 423 | — | Jupyter Notebook | NVIDIA cuOpt examples for decision optimization |
| [MegviiRobot/OdomLaserCalibraTool](https://github.com/MegviiRobot/OdomLaserCalibraTool) | 423 | — | C++ | Extrinsic Calibration of a Odom and 2d Laser |
| [Lightricks/LTX-Video-Trainer](https://github.com/Lightricks/LTX-Video-Trainer) | 418 | — | Python | Community trainer for Lightricks' LTX Video model 🎬 ⚡️ |
| [akshetP/robotics-resources](https://github.com/akshetP/robotics-resources) | 395 | — | HTML | A complete library of resources that caters to all levels of Roboticists. |
| [awslabs/fullstack-solution-template-for-agentcore](https://github.com/awslabs/fullstack-solution-template-for-agentcore) | 395 | — | TypeScript | Flexible Fullstack solution template for production-ready deployments of any use case on Amazon Bedrock AgentCore. |
| [XiaomiRobotics/Xiaomi-Robotics-0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0) | 372 | — | Python | — |
| [yihong1120/Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection) | 357 | — | Python | Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy. |
| [MaverickPeter/MR_SLAM](https://github.com/MaverickPeter/MR_SLAM) | 354 | — | C++ | [IEEE T-RO 2023] A modularized multi-robot SLAM system with elevation mapping and a costmap converter for easy navigation. Different odometry and loop closure algorithms can be easily integrated into the system. |
| [leggedrobotics/icp_localization](https://github.com/leggedrobotics/icp_localization) | 345 | — | C++ | This package provides localization in a pre-built map using ICP and odometry (or the IMU measurements). |
| [Phylliade/awesome-machine-learning-robotics](https://github.com/Phylliade/awesome-machine-learning-robotics) | 323 | — | — | A curated list of resources about Machine Learning for Robotics |
| [url-kaist/TRAVEL](https://github.com/url-kaist/TRAVEL) | 320 | — | C++ | Traversable ground and above-ground object segmentation using graph representation of 3D LiDAR scans |
| [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems) | 314 | — | C++ | super repo for rocm systems projects |
| [YibinWu/LIO-EKF](https://github.com/YibinWu/LIO-EKF) | 310 | — | C++ | [ICRA2024] Maybe the simplest LiDAR-inertial odometry that one can have. |
| [nepfaff/scenesmith](https://github.com/nepfaff/scenesmith) | 306 | — | Python | Code for "SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes" |
| [yangshun/tree-node-cli](https://github.com/yangshun/tree-node-cli) | 281 | — | TypeScript | List directory contents in a tree-like format, similar to the Linux tree command |
| [engcang/FAST-LIO-SAM](https://github.com/engcang/FAST-LIO-SAM) | 280 | — | C++ | a SLAM implementation combining FAST-LIO2 with pose graph optimization and loop closing based on LIO-SAM paper |
| [utiasASRL/steam_icp](https://github.com/utiasASRL/steam_icp) | 253 | — | C++ | Continuous-time lidar, radar, lidar-inertial, and radar-inertial odometry |
| [ColinShaw/robotics-and-machine-vision-resources](https://github.com/ColinShaw/robotics-and-machine-vision-resources) | 243 | — | Python | Book, articles and interesting things related to robotics |
| [langflow-ai/langflow-embedded-chat](https://github.com/langflow-ai/langflow-embedded-chat) | 241 | — | TypeScript | The Langflow Embedded Chat is a powerful web component that enables seamless communication with Langflow |
| [8thwall/8thwall](https://github.com/8thwall/8thwall) | 233 | — | TypeScript | Build immersive AR and interactive 3D. Free and open. |
| [googlecolab/colab-mcp](https://github.com/googlecolab/colab-mcp) | 232 | — | Python | An MCP server for interacting with Google Colab |
| [google/xrblocks](https://github.com/google/xrblocks) | 219 | — | TypeScript | XR Blocks is a lightweight WebXR + WebAI library for rapidly prototyping advanced XR and AI experiences. |
| [Livox-SDK/livox_relocalization](https://github.com/Livox-SDK/livox_relocalization) | 215 | — | C++ | A relocalization package for Livox LiDARs. |
| [lumalabs/ComfyUI-LumaAI-API](https://github.com/lumalabs/ComfyUI-LumaAI-API) | 208 | — | Python | ComfyUI custom nodes for Luma AI Dream Machine API |
| [bandasaikrishna/Autonomous_Mobile_Robot](https://github.com/bandasaikrishna/Autonomous_Mobile_Robot) | 204 | — | C++ | Autonomous mobile robot navigation using ROS Navigation Stack. |
| [TheNoobInventor/lidarbot](https://github.com/TheNoobInventor/lidarbot) | 201 | — | Python | A differential drive robot is controlled using ROS2 Humble running on a Raspberry Pi 4 (running Ubuntu server 22.04). The vehicle is equipped with a raspberry pi camera for visual feedback and an RPlidar A1 sensor used for Simultaneous Localization and Mapping (SLAM), autonomous navigation and obstacle avoidance. |
| [AntoBrandi/Robotics-and-ROS-2-Learn-by-Doing-Manipulators](https://github.com/AntoBrandi/Robotics-and-ROS-2-Learn-by-Doing-Manipulators) | 196 | — | Python | About 3D Printed robot arm powered by ROS 2 and Arduino and controlled via MoveIt! 2 and Amazon Alexa. It is developed and programmed in the online course named "Robotics and ROS 2 - Learn by Doing! Manipulators" |
| [addy1997/Robotics-Resources](https://github.com/addy1997/Robotics-Resources) | 166 | — | — | List of commonly used robotics libraries and packages |
| [google/sec-gemini](https://github.com/google/sec-gemini) | 154 | — | Svelte | Sec-Gemini v1 is a cutting-edge AI model designed to enhance cybersecurity capabilities and empower defenders in the ongoing battle against cyber threats. |
| [google/aistreamer](https://github.com/google/aistreamer) | 152 | — | C++ | Google AIStreamer |
| [anesriad/Regression_ML_EndtoEnd](https://github.com/anesriad/Regression_ML_EndtoEnd) | 149 | — | Jupyter Notebook | Machine learning End to End project from data collection to deployment and monitoring (Regression problem) |
| [dataiku/kiji-proxy](https://github.com/dataiku/kiji-proxy) | 117 | — | Python | Privacy proxy for your OpenAI requests |
| [Shubhamsaboo/openclaw-vertexai-memorybank](https://github.com/Shubhamsaboo/openclaw-vertexai-memorybank) | 113 | — | TypeScript | Vertex AI Memory Bank Plugin for OpenClaw |
| [mcomunita/nablafx](https://github.com/mcomunita/nablafx) | 112 | — | Python |  Framework for differentiable black-box and gray-box audio effects modeling |
| [dataiku/dataiku-contrib](https://github.com/dataiku/dataiku-contrib) | 107 | — | Python | Public repository for DSS plugins |
| [purzbeats/purz-comfyui-workflows](https://github.com/purzbeats/purz-comfyui-workflows) | 106 | — | — | Purz's ComfyUI Workflows |
| [fiberplane/mcp-lite](https://github.com/fiberplane/mcp-lite) | 100 | — | TypeScript | Lightweight, composable MCP framework for TypeScript |
| [robometer/robometer](https://github.com/robometer/robometer) | 98 | — | Python | Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons |
| [the-full-stack/fsdl-text-recognizer](https://github.com/the-full-stack/fsdl-text-recognizer) | 77 | — | Jupyter Notebook | Repo that generates https://github.com/full-stack-deep-learning/fsdl-text-recognizer-project |
| [OneWave-AI/claude-skills](https://github.com/OneWave-AI/claude-skills) | 62 | — | Python | 100 Production-Ready Claude Code Skills - The most comprehensive collection of AI skills for sales, business automation, content creation, and development |
| [EmptyBlueBox/DexLatent](https://github.com/EmptyBlueBox/DexLatent) | 61 | — | Python | — |
| [KhanhPham2411/n8n-atom](https://github.com/KhanhPham2411/n8n-atom) | 54 | — | TypeScript | World's first n8n client that manage workflow collections inside VSCode/Cursor/Antigravity |
| [zetic-ai/ZETIC_Melange_apps](https://github.com/zetic-ai/ZETIC_Melange_apps) | 51 | — | Swift | NPU powered On-device AI Mobile applications using Melange |
| [google/ai_video_dubbing](https://github.com/google/ai_video_dubbing) | 51 | — | Python | — |
| [google/airdialogue](https://github.com/google/airdialogue) | 47 | — | Python | — |
| [atzberg/geo_neural_op](https://github.com/atzberg/geo_neural_op) | 42 | — | Python | Geometric Neural Operators (GNPs) for machine learning tasks on point-cloud representations: curvature estimation, shape deformations, solvers for geometric PDEs.  Also, includes weights of pretrained transferable GNP models. |
| [synaptic-ai-consulting/crewai-LL-series](https://github.com/synaptic-ai-consulting/crewai-LL-series) | 36 | — | Python | Code Repository for CrewAI Lightning Lessons Series |
| [Snapchat/SnapRHI](https://github.com/Snapchat/SnapRHI) | 35 | — | C++ | A lightweight, modern Render Hardware Interface (RHI) abstraction layer for C++ SnapRHI provides a clean, unified API that abstracts away the complexity of modern graphics APIs — enabling you to write rendering code once and target multiple backends seamlessly. |
| [google/genie-for-sap-abap-ai-assistant-sample](https://github.com/google/genie-for-sap-abap-ai-assistant-sample) | 34 | — | ABAP | Genie for SAP enables AI based features (Code Explan, Code Review, Suggest Code and Suggest ABAP Unit Test) in SAP ABAP Editor on RIGHT-CLICK |
| [google/vertex-ai-nas](https://github.com/google/vertex-ai-nas) | 31 | — | Python | With Vertex AI NAS, you can search for optimal neural architectures in terms of accuracy, latency, memory, a combination of these, or a custom metric. |
| [jeantimex/splat](https://github.com/jeantimex/splat) | 28 | — | TypeScript | 3D Gaussian Splatting Viewer |
| [wilwaldon/Claude-Code-Frontend-Design-Toolkit](https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit) | 27 | — | — | Everything I've found that actually makes Claude Code output better-looking frontends. Skills, plugins, MCP servers, CLAUDE.md tricks |
| [google/embardiment](https://github.com/google/embardiment) | 24 | — | C# | Packages and tools to enable EmBARDiment type of AI agents inside Android XR. |
| [google/airio](https://github.com/google/airio) | 24 | — | Python | — |
| [yugaaank/ffflow](https://github.com/yugaaank/ffflow) | 23 | — | Rust | Ffflow is a lightweight CLI tool for building structured, repeatable ffmpeg workflows. It helps organize complex media commands into clean, modular pipelines. Designed for power users who want clarity over command-line chaos. Simple structure, powerful media processing. |
| [rudybear/lux](https://github.com/rudybear/lux) | 22 | — | Python | Lux — math-first shader language that compiles to SPIR-V for Vulkan |
| [AnkunHuang/Agentic_Design_Patterns](https://github.com/AnkunHuang/Agentic_Design_Patterns) | 21 | — | Jupyter Notebook | Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems by Antonio Gulli |
| [microsoft/physical-ai-toolchain](https://github.com/microsoft/physical-ai-toolchain) | 20 | — | TypeScript | — |
| [kekzl/imp](https://github.com/kekzl/imp) | 15 | — | Cuda | High-performance LLM inference engine in C++/CUDA for NVIDIA Blackwell GPUs (RTX 5090) |
| [stefanros481/ott-platform](https://github.com/stefanros481/ott-platform) | 14 | — | Python | Learning Claude Code via a real-world OTT streaming platform implementation |
| [Chris4212/Encodex](https://github.com/Chris4212/Encodex) | 13 | — | Python | Smart batch video encoding made simple. |
| [PatchedReality/ManifolderMCP](https://github.com/PatchedReality/ManifolderMCP) | 5 | — | TypeScript | MCP server exposing Open Metaverse Fabric editing tools for AI agents. |
| [jeffreygroneberg/ai_scheduler](https://github.com/jeffreygroneberg/ai_scheduler) | 4 | — | Python | — |
| [CelestialCreator/mtp-lm](https://github.com/CelestialCreator/mtp-lm) | 4 | — | Python | Source code to accompany research paper on training multi token prediction language models using self-distillation. |
| [PatchedReality/Manifolder](https://github.com/PatchedReality/Manifolder) | 4 | — | JavaScript | A map explorer for the Open Metaverse AKA Open Spatial Internet |
| [coderextreme/JSONvirse](https://github.com/coderextreme/JSONvirse) | 1 | — | JavaScript | Initially, a multiuser system for research, design, development, of 3D scenes. Ultimately, I want to do a block party. |

## Top Repos by Stars

| Fork | Upstream Stars | Language |
|------|---------------:|----------|
| [perditioinc/awesome](https://github.com/perditioinc/awesome) | 446,773 | — |
| [perditioinc/public-apis](https://github.com/perditioinc/public-apis) | 412,000 | Python |
| [perditioinc/openclaw](https://github.com/perditioinc/openclaw) | 323,515 | TypeScript |
| [perditioinc/awesome-python](https://github.com/perditioinc/awesome-python) | 287,863 | Python |
| [perditioinc/project-based-learning](https://github.com/perditioinc/project-based-learning) | 261,212 | — |
| [perditioinc/Python](https://github.com/perditioinc/Python) | 218,804 | Python |
| [perditioinc/tensorflow](https://github.com/perditioinc/tensorflow) | 194,210 | C++ |
| [perditioinc/vscode](https://github.com/perditioinc/vscode) | 182,811 | TypeScript |
| [perditioinc/AutoGPT](https://github.com/perditioinc/AutoGPT) | 182,590 | Python |
| [perditioinc/Python-100-Days](https://github.com/perditioinc/Python-100-Days) | 179,800 | Jupyter Notebook |

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
