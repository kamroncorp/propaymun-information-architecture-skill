# ProPaymun Information Architecture

[![Version](https://img.shields.io/badge/version-0.3.0-5B4BDB)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-2E7D32)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-19172B)](SKILL.md)

An IA-only Agent Skill that acts as an experienced information architect: it guides people from an initial product brief and high-impact questions to a professional, evidence-aware information architecture.

**ProPaymun** comes from the Persian word «پروپیمان»: full, complete, and generously filled. Completeness here means decision-ready—not unnecessarily long.

[فارسی](README.fa.md)

## What it does

- guides people who do not already understand IA;
- asks consequential questions before committing to a complete architecture;
- models objects/content, relationships, organization, taxonomy, labels, navigation, search, access, lifecycle, and governance;
- distinguishes supplied evidence, observation, inference, proposal, confirmation, and unknowns;
- adapts language and depth for product, design, research, content, engineering, or cross-functional readers;
- detects whether it is running in a conversation-first or build-first environment and uses that environment appropriately;
- stops by itself when a material answer is required—the user does not need prompting tricks;
- uses public web research and connected context when available and materially useful;
- supports greenfield IA, redesign, audits, and focused IA components.

The skill stays within information architecture. Separate mapping disciplines belong to their own dedicated skills.

## Default experience

For complete IA work, the skill normally:

1. reflects the brief and existing evidence;
2. asks a compact set of architecture-changing questions;
3. stops automatically when those answers are required;
4. proceeds with visible assumptions for reversible unknowns;
5. delivers the best IA artifact for the current environment.

A detailed brief does not silently trigger a full draft when important access, lifecycle, role, or domain decisions remain unresolved. A compact provisional answer is available when the user explicitly asks for speed or work without questions.

## Quick start

### Universal installer

```bash
npx skills add https://github.com/kamroncorp/propaymun-information-architecture-skill
```

Then ask naturally:

```text
Help me design the information architecture for my product. Here is the brief...
```

The user does not need to choose a mode, understand checkpoints, request a pause, or know IA terminology.

### Claude Code

Clone or copy this repository to:

```text
~/.claude/skills/propaymun-information-architecture/
```

The repository can also be packaged as a zip and uploaded as a custom Skill where Claude supports skill uploads.

### Codex / ChatGPT

Place the repository at:

```text
~/.codex/skills/propaymun-information-architecture/
```

For OpenAI API Skills, upload the skill directory or a release zip. The included [`agents/openai.yaml`](agents/openai.yaml) provides UI metadata.

### Gemini CLI

```bash
gemini skills install https://github.com/kamroncorp/propaymun-information-architecture-skill
```

### Figma agent and Figma Make

Upload the generated single-file adapter:

```text
adapters/figma-make/propaymun-information-architecture.md
```

Invoke it with `/propaymun-information-architecture` and describe the product naturally. If material information is missing, the skill asks a few questions and makes no build change in that turn. Once sufficient, it uses Figma Make to build an interactive IA Review Workspace—not the product UI, a sitemap, or a user flow. Plan mode is optional, not required.

## Outputs

Conversation-first agents default to concise chat text and create heavier artifacts only after acceptance. Build-first environments default to an environment-native IA review artifact after the autonomous stop gate passes.

IA diagrams are optional. A portable textual representation is always available; Mermaid, HTML/SVG, or another installed diagram capability may be used when requested and supported.

### Optional diagram companions

These are not required and are never installed without explicit user authorization:

- [Draw.io Skill](https://github.com/Agents365-ai/drawio-skill) — precise editable geometry and formal handoff
- [Excalidraw Diagram Skill](https://github.com/coleam00/excalidraw-diagram-skill) — workshops and conceptual explanation

## Portable semantic model

When structured reuse is requested, the skill can produce a renderer-independent IA JSON model. Environments with Python can validate or render it:

```bash
python scripts/validate_ia_model.py path/to/ia.json
python scripts/render_ia_html.py path/to/ia.json -o ia.html
```

Chat-only environments return the requested semantic source directly and do not pretend these scripts ran.

## Development and validation

```bash
python scripts/package_figma.py
python -m unittest discover -s tests -v
python /path/to/skill-creator/scripts/quick_validate.py .
```

[`adapters/manifest.json`](adapters/manifest.json) records the shared release version and delivery profile for Claude, ChatGPT/Codex, Gemini, and Figma Make. Tests verify that the canonical skill, generated Figma adapter, manifest, and documentation stay version-aligned.

Behavioral cases cover natural Persian intake, autonomous stopping, minimal novice answers, chat-only capability limits, Figma build-first delivery, public research, artifact consent, and RTL diagram fallback. See [`evals/cases.yaml`](evals/cases.yaml).

## Quality policy

The skill does not invent research or universal success thresholds, call an untested structure validated, create unsolicited artifacts, or use hidden high-impact assumptions to select an architecture.

## Versioning and license

The project uses Semantic Versioning and Apache License 2.0. See [CHANGELOG.md](CHANGELOG.md) and [LICENSE](LICENSE).
