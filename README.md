# ProPaymun Information Architecture

[![Version](https://img.shields.io/badge/version-0.2.0-5B4BDB)](CHANGELOG.md)
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
- works chat-first, then offers supported reusable formats only after the user accepts them;
- supports greenfield IA, redesign, audits, and focused IA components.

The skill stays within information architecture. Separate mapping disciplines belong to their own dedicated skills.

## Default experience

For complete IA work, the skill normally:

1. reflects the brief and existing evidence;
2. asks a compact set of architecture-changing questions;
3. progresses through human checkpoints;
4. delivers a concise decision-ready result in chat;
5. offers supported file or visual formats only after the architecture is stable.

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

The user does not need to choose or understand an internal mode.

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

## Outputs

The default output is concise chat text. After confirmation, the skill may offer Markdown, document, PDF, HTML, image, or structured data only when the current environment can actually create it.

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

Behavioral cases cover natural Persian intake, chat-only capability limits, explicit quick work, audience-neutral delivery, artifact consent, and RTL diagram fallback. See [`evals/cases.yaml`](evals/cases.yaml).

## Quality policy

The skill does not invent research or universal success thresholds, call an untested structure validated, create unsolicited artifacts, or use hidden high-impact assumptions to select an architecture.

## Versioning and license

The project uses Semantic Versioning and Apache License 2.0. See [CHANGELOG.md](CHANGELOG.md) and [LICENSE](LICENSE).
