# ProPaymun Information Architecture

[![Version](https://img.shields.io/badge/version-0.1.0-5B4BDB)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-2E7D32)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-19172B)](SKILL.md)

An evidence-aware Agent Skill that helps product managers, product designers, researchers, founders, and product teams create professional information architecture with AI.

**ProPaymun** comes from the Persian word «پروپیمان»: full, complete, and generously filled. The project aims to produce IA that is complete enough to act on without pretending that unknowns are known.

[فارسی](README.fa.md)

## What it does

The skill supports greenfield design, redesign, and focused IA work for any digital product. It can produce a complete IA or only the artifact requested by the user:

- IA brief and audit
- domain/object model
- taxonomy and labeling system
- navigation and search model
- roles, permissions, and visibility
- architecture alternatives and decision rationale
- validation plan, metrics, and governance
- semantic JSON, Mermaid, Draw.io/Excalidraw guidance, HTML, or image-ready output

It offers two default working modes:

- **Guided:** compact discovery rounds and human checkpoints.
- **Quick Draft:** a useful provisional architecture with assumptions and unknowns clearly marked.

Users can override the process, order, depth, checkpoints, and output format at any time.

## Quick start

### Universal installer

If your agent supports the Agent Skills installer:

```bash
npx skills add https://github.com/kamroncorp/propaymun-information-architecture-skill
```

Then ask:

```text
Use propaymun-information-architecture to design the IA for my product.
```

### Claude Code

Clone or copy this repository to:

```text
~/.claude/skills/propaymun-information-architecture/
```

Claude Code discovers the root `SKILL.md`. The repository can also be packaged as a zip and uploaded as a custom Skill where Claude supports skill uploads.

### Codex / ChatGPT

For Codex, place the repository at:

```text
~/.codex/skills/propaymun-information-architecture/
```

For OpenAI API Skills, upload the skill directory or a release zip using the Skills API. The included [`agents/openai.yaml`](agents/openai.yaml) provides Codex/ChatGPT-facing metadata.

### Gemini CLI

```bash
gemini skills install https://github.com/kamroncorp/propaymun-information-architecture-skill
```

Alternatively, link a local checkout while developing:

```bash
gemini skills link /path/to/propaymun-information-architecture-skill
```

### Figma agent and Figma Make

Figma custom skill uploads accept one Markdown file and do not load supporting directories. Upload:

```text
adapters/figma-make/propaymun-information-architecture.md
```

Invoke it with:

```text
/propaymun-information-architecture
```

## Example requests

```text
Create a complete information architecture for a multi-role education platform. Use Guided mode.
```

```text
Here is our current navigation and search log summary. Audit the IA and propose two alternatives.
```

```text
Only create a taxonomy and labeling system for this content inventory. Return Markdown and Mermaid.
```

```text
Build a quick provisional IA from this brief, mark every assumption, and generate a standalone HTML view.
```

## Default output behavior

When no format is requested, the skill produces a concise Markdown report and a Mermaid diagram. It can also create or guide delivery in Draw.io, Excalidraw, standalone HTML, SVG, PNG, or PDF when the environment supports those formats.

Visuals should always preserve an editable source and include a textual equivalent of essential information.

## Repository structure

```text
SKILL.md                         Canonical skill entrypoint
agents/openai.yaml               OpenAI UI and invocation metadata
references/                      Progressive-disclosure IA guidance
assets/semantic-ia.schema.json   Portable semantic model schema
scripts/                         Validation, HTML, and Figma packaging tools
adapters/figma-make/             Generated single-file Figma adapter
evals/                           Behavioral test cases and rubric
tests/                           Deterministic script tests
```

## Semantic IA model

The skill can represent IA independently of a rendering tool. This prevents meaning from becoming locked into Mermaid syntax, Draw.io XML, or canvas coordinates.

Validate a model:

```bash
python scripts/validate_ia_model.py path/to/ia.json
```

Render standalone HTML:

```bash
python scripts/render_ia_html.py path/to/ia.json -o ia.html
```

Rebuild the Figma single-file adapter:

```bash
python scripts/package_figma.py
```

## Quality and evidence policy

The skill distinguishes `Provided`, `Observed`, `Confirmed`, `Inferred`, `Proposed`, and `Unknown`. It does not call synthetic AI groupings user research, does not claim an untested structure is validated, and rejects universal click-count, menu-size, and hierarchy-depth rules.

## Development

Run deterministic tests:

```bash
python -m unittest discover -s tests -v
```

Run the Agent Skill structure validator:

```bash
python /path/to/skill-creator/scripts/quick_validate.py .
```

Behavioral cases live in [`evals/cases.yaml`](evals/cases.yaml). Evaluate observable decisions and artifacts rather than exact phrasing.

## Versioning

This project uses semantic versioning. GitHub Releases provide installable snapshots. See [CHANGELOG.md](CHANGELOG.md).

## Contributing

Focused improvements are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

Apache License 2.0. See [LICENSE](LICENSE).


