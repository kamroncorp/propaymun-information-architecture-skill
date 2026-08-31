# ProPaymun Information Architecture

[![Version](https://img.shields.io/badge/version-0.3.0-5B4BDB)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-2E7D32)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-19172B)](SKILL.md)

An IA-only expert workflow that guides a person from a natural product brief to a professional, evidence-aware information architecture—even when they do not know IA terminology.

**ProPaymun** comes from the Persian «پروپیمان»: full and complete. Here, complete means decision-ready, not unnecessarily long.

[فارسی](README.fa.md)

## What it does

- inspects the brief and available sources before asking questions;
- asks only questions whose answers can change the architecture, then stops by itself;
- models information domains, objects/content, hierarchy, typed relationships, taxonomy, labels, metadata, findability, access, lifecycle, and governance;
- separates provided facts, observation, inference, proposal, confirmation, and unknowns;
- adapts language and depth to the user and the available environment;
- uses current public research when it can materially improve the IA and browsing is available;
- keeps sitemap, user flow, UI, API, and database design outside this skill.

## Two supported distributions

There is no honest one-click installer shared by every AI product. ProPaymun provides two synchronized distributions instead:

1. **Native Agent Skill** — [`SKILL.md`](SKILL.md) plus references, assets, and helpers for Claude.ai, Claude Code, Codex, Gemini CLI, ZCode, and other Skill-compatible agents.
2. **Universal Web** — one self-contained Markdown file for Projects, Gems, custom Agents, or file-capable chats that do not load native Skills.

Uploading a file to a Project is configuration, not a native Skill installation. The IA behavior is shared, while automatic triggering, persistence, tools, and context limits depend on the host.

## Install or configure

### Claude.ai web — native Skill, including Free

Download the ready-to-upload [`propaymun-information-architecture.zip`](install/claude-ai/propaymun-information-architecture.zip). In Claude.ai:

1. enable **Code execution and file creation** in **Settings → Capabilities**;
2. open **Customize → Skills**;
3. choose **+ → Create skill → Upload a skill**;
4. upload the ZIP and enable it.

A GitHub repository URL is not a Claude.ai Skill installer. Claude.ai expects the packaged ZIP.

### Claude Projects — universal fallback

Create a Project, upload [`install/universal-web/propaymun-information-architecture.md`](install/universal-web/propaymun-information-architecture.md) to project knowledge, and paste [`PROJECT_INSTRUCTIONS.md`](install/universal-web/PROJECT_INSTRUCTIONS.md) into Project Instructions.

### ChatGPT web

Create a Project, upload the Universal Web file, and paste the Project Instructions text into the project's instructions. Then describe the product naturally. This is the recommended personal ChatGPT web path; it does not require a terminal.

### Gemini web

Create a Gem, paste the Project Instructions text into the Gem instructions, and add the Universal Web file as Knowledge. For one-off use, attach the Universal Web file to a chat and ask Gemini to follow it as operating instructions.

### Kimi web

Create a Kimi Project, upload the Universal Web Markdown as a project file, and paste the Project Instructions text into project instructions. Kimi Agent users may also use Kimi's own Skill creator, but the Project route is the portable no-terminal setup.

### Z.AI / GLM web and other file-capable assistants

Where the product offers a Project, custom Agent, knowledge base, or persistent instructions, add the Universal Web file and the Project Instructions text there. Otherwise attach the file to a chat and explicitly ask the assistant to follow it as operating instructions for that conversation. Do not assume native Skill persistence unless the product confirms it.

### Claude Code, Codex, Gemini CLI, ZCode, and compatible agents

```bash
npx skills add https://github.com/kamroncorp/propaymun-information-architecture-skill
```

Platform-native alternatives include copying the repository into the agent's Skill directory or, for Gemini CLI:

```bash
gemini skills install https://github.com/kamroncorp/propaymun-information-architecture-skill
```

## Use

Ask naturally:

```text
Help me design the information architecture for my product. Here is the brief...
```

The user does not need to choose a mode, mention checkpoints, request a pause, or know IA vocabulary. The skill decides when it has enough information and stops when a material answer is required.

## Outputs

The default is concise, decision-ready conversation. Files, semantic JSON, Mermaid, HTML, PDF, or a professional diagram are created only when requested and supported. Every format must represent the same canonical semantic IA model.

Optional diagram companions are never required or installed without permission:

- [Draw.io Skill](https://github.com/Agents365-ai/drawio-skill) for precise editable handoff;
- [Excalidraw Diagram Skill](https://github.com/coleam00/excalidraw-diagram-skill) for workshops and conceptual explanation.

## Figma Make is a downstream output

Figma Make is no longer an installation target or the default place to reason about IA. After the IA is stable, ask the active assistant:

```text
Create a self-contained Figma Make prompt from this approved information architecture.
```

The skill carries the canonical IA, hierarchy, relationships, access, language, uncertainty, guardrails, and acceptance criteria into the prompt. Figma Make is instructed to visualize the architecture—not invent it. Environments with Python can also export deterministically:

```bash
python scripts/export_figma_make_prompt.py path/to/ia.json -o figma-make-prompt.md
```

## Portable semantic model

```bash
python scripts/validate_ia_model.py path/to/ia.json
python scripts/render_ia_html.py path/to/ia.json -o ia.html
```

Chat-only environments return the requested source directly and never pretend a helper ran.

## Development and validation

```bash
python scripts/package_distributions.py
python -m unittest discover -s tests -v
python /path/to/skill-creator/scripts/quick_validate.py .
```

Generated Universal Web and Claude.ai packages are tested against the canonical source. [`adapters/manifest.json`](adapters/manifest.json) records distributions and downstream exports. Behavioral evaluations are in [`evals/cases.yaml`](evals/cases.yaml).

## Versioning and license

The project uses Semantic Versioning and Apache License 2.0. Current unreleased changes remain under [Unreleased](CHANGELOG.md); no new tag or release is created until testing is accepted.
