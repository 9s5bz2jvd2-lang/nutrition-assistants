# Yuan Nutrition MAS Harness

**Yuan Nutrition MAS Harness** is a nutritionist-friendly Multi-Agent System (MAS) harness developed by **Wang Runyuan** on top of [LingTai](https://github.com/Lingtai-AI/lingtai).

It is designed to make lightweight agent orchestration, API management, safety approvals, rollback, and structured task handoff easier for nutrition professionals and nutrition-AI workflows.

## What this project is

Yuan Nutrition MAS Harness is not a shell or a button-only GUI. It is a lightweight LingTai-based harness that organizes each WeChat or GUI request into an auditable workflow:

```text
intake -> route -> approval -> dispatch -> collect -> return
```

The harness is intended to help nutrition professionals work with AI agents more safely and more transparently, especially when tasks involve evidence collection, nutrition education materials, structured workflow handoff, or multi-agent collaboration.

## Current capabilities

The current standalone project includes:

- local GUI for a lightweight LingTai harness;
- unified Task Router for GUI / WeChat-style inputs;
- approval queue and scoped approval grants;
- API / model center for OpenAI-compatible providers and custom endpoints;
- Secret Vault design with Keychain-first and restricted `.secrets` fallback;
- local budget / cost guardrails;
- git Time Machine / rollback with confirmation;
- LingTai internal mailbox dispatch and reply collection;
- controlled worker dispatch protocol with structured `HARNESS_REPLY_JSON` results;
- lightweight multi-agent orchestration, insight, soul-flow, and shougong records.

## Repository

Canonical runnable repository:

- <https://github.com/9s5bz2jvd2-lang/yuan-nutrition-mas-harness>

If the standalone repository is private during early development, this directory serves as the public project entry inside Nutrition Assistants. When the runnable repository is made public, this page should point users there as the canonical download/install location.

## Safety scope

This project is a local-first harness and safety layer. It is not a substitute for professional nutrition judgment, clinical diagnosis, or medical treatment. Nutrition content and user-facing outputs still need evidence review, human oversight, and appropriate safety boundaries.

Runtime safety boundaries include:

- API calls may create cost and should remain confirmation-gated;
- rollback can only affect repository files and cannot undo external side effects;
- logs, screenshots, reports, and credentials should be scanned and redacted before sharing;
- worker dispatch should remain auditable and should not silently start high-impact actions.

## Maintainer

Maintained by **Wang Runyuan**, a China Registered Nutritionist and master's graduate in Nutrition and Food Hygiene from Kunming Medical University.
