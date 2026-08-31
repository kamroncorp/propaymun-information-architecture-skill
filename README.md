# ProPaymun Information Architecture

[![Version](https://img.shields.io/badge/version-0.3.1-5B4BDB)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache--2.0-2F855A)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-ready-111827)](SKILL.md)

Turn ordinary product context into clear, evidence-aware information architecture—even when the user does not know IA terminology.

**ProPaymun** comes from the Persian «پروپیمان»: full and complete. Here, complete means decision-ready, understandable, and honest about uncertainty.

[فارسی](README.fa.md)

## Choose the right package

| Package | Best for | Download |
|---|---|---|
| **Agent Skill Package** | Claude.ai Skills and only runtimes whose own documentation confirms compatible Agent Skill package support | [Download ZIP](packages/agent-skill/propaymun-information-architecture.zip) |
| **Workspace Kit** | ChatGPT Projects, Claude Projects, manually created Gemini Gems, and surfaces that provide persistent instructions plus file knowledge | [Knowledge file](packages/workspace-kit/propaymun-ia-workspace-kit.md) + [Workspace instructions](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) |

The two packages share the same canonical behavior. Automatic triggering, persistence, tools, and context limits still depend on the host product.

## Install in Claude.ai

1. Download the **[Agent Skill Package](packages/agent-skill/propaymun-information-architecture.zip)**.
2. In Claude.ai, enable **Settings → Capabilities → Code execution and file creation**.
3. Open **Customize → Skills**.
4. Choose **+ → Create skill → Upload a skill**.
5. Upload the ZIP without extracting it, then enable the skill.

A GitHub repository URL is not a Claude.ai upload package. Use the ZIP above.

## Configure a web workspace

For a workspace that explicitly provides both persistent instructions and file knowledge:

1. add [`propaymun-ia-workspace-kit.md`](packages/workspace-kit/propaymun-ia-workspace-kit.md) as project knowledge;
2. paste [`WORKSPACE_INSTRUCTIONS.md`](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) into the workspace, project, Gem, or custom-agent instructions;
3. describe the product naturally.

This is configuration through project knowledge, not a claim of native Skill installation.

### Gemini web

Gemini web uses a manually created Gem rather than a native Skill installation:

1. choose **Explore Gems → New Gem**;
2. paste [`WORKSPACE_INSTRUCTIONS.md`](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) into the Gem instructions;
3. add [`propaymun-ia-workspace-kit.md`](packages/workspace-kit/propaymun-ia-workspace-kit.md) under **Knowledge**;
4. save the Gem.

### One-off file use

If a service only accepts files in a chat, attach the Workspace Kit and paste the short Workspace Instructions with the first message. This is session-scoped file use—not installation, persistent configuration, or guaranteed automatic triggering.

## Other Agent Skill runtimes

Use the Agent Skill Package only when the host's own documentation confirms this package format and installation route. This repository intentionally does not provide unverified CLI installation commands.

## Machine-scannable install map

```yaml
product: ProPaymun Information Architecture
skill_id: propaymun-information-architecture
canonical_entrypoint: SKILL.md
native_package: packages/agent-skill/propaymun-information-architecture.zip
native_package_verified_for: [claude.ai-skills]
workspace_knowledge: packages/workspace-kit/propaymun-ia-workspace-kit.md
workspace_instructions: packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md
workspace_requires: [persistent-instructions, file-knowledge]
gemini_web: create-a-new-gem-manually
one_off_file_use: attach-workspace-kit-and-paste-instructions
do_not_claim: [native-installation, persistent-behavior, automatic-triggering, unverified-cli-support]
package_manifest: packages/manifest.json
semantic_schema: schema/semantic-ia.schema.json
visual_builder_exporter: scripts/export_builder_handoff.py
legacy_download_paths: preserved
release_state: v0.3.1-published
```

An AI installer should select exactly one host-appropriate package, preserve the package contents, and avoid claiming native installation when it only attached a knowledge file.

## What the skill does

- inspects the brief, attachments, conversation, and authorized sources before asking;
- reassesses sufficiency throughout the work instead of asking a fixed first-round questionnaire;
- asks only questions whose answers can change the next architecture decision, then stops by itself;
- separates language from locale, jurisdiction, culture, and operating model;
- models information domains, canonical items, hierarchy, typed relationships, taxonomy, labels, metadata, findability, access, lifecycle, and governance;
- separates provided facts, observations, confirmation, inference, proposals, conflicts, and unknowns;
- uses current public research when it can materially improve the IA and browsing is available;
- keeps sitemap, user flow, product UI, API, and database design outside this skill.

## How the adaptive workflow behaves

The user does not choose a mode or manage checkpoints.

```text
inspect context
→ model the next consequential layer
→ detect an architecture-changing unknown
→ ask the smallest useful question and stop
→ continue after the answer
→ verify handoff readiness before creating an artifact
```

If the user does not know, the skill can explain a few plausible patterns and recommend a clearly marked provisional default. It never turns language or cultural stereotypes into confirmed product rules.

## Visual Builder Handoff

Figma Make, Lovable, and similar prompt-to-build tools are downstream renderers, not the place where IA decisions are made.

After the IA is ready for its intended purpose, ask:

```text
Create a Visual Builder Handoff for Figma Make from this information architecture.
```

The handoff contains:

1. a self-contained Markdown build specification;
2. a short copy-ready launch instruction for the builder's text box.

This matters because long attached prompts may be treated as files while the Generate button still requires a short text instruction.

Deterministic export:

```bash
python scripts/export_builder_handoff.py path/to/ia.json --target figma-make -o build-spec.md
python scripts/export_builder_handoff.py path/to/ia.json --target lovable -o build-spec.md
```

The primary view must show domain containers, mapped items, hierarchy, and labeled cross-domain relationships. It must not become a dashboard, sitemap, user flow, wireframe, product UI, API, or database schema.

## Semantic IA 2.0

The renderer-independent model lives at [`schema/semantic-ia.schema.json`](schema/semantic-ia.schema.json). It uses:

- explicit domain-to-item mapping;
- one canonical item registry;
- primary hierarchy plus typed relationships;
- separate roles and item-scoped permissions;
- structured lifecycle states and transitions;
- locale context with evidence state;
- handoff readiness and blocking unknowns.

Validate or render a model:

```bash
python scripts/validate_ia_model.py path/to/ia.json
python scripts/render_ia_html.py path/to/ia.json -o ia.html
```

## Repository map

```text
SKILL.md                     canonical behavior
agents/                      host-facing skill metadata
references/                  conditional IA operating guidance
schema/                      Semantic IA 2.0 contract
scripts/                     validation, rendering, packaging, and handoff export
packages/                    professional installable packages
install/                     compatibility aliases for previously shared links
evals/                       behavioral cases and rubric
tests/                       deterministic script and package tests
```

## Development and validation

```bash
python scripts/build_packages.py
python -m unittest discover -s tests -v
python /path/to/skill-creator/scripts/quick_validate.py .
```

GitHub Actions rebuilds the packages, verifies byte-for-byte parity, validates the Semantic IA fixture, and runs the deterministic test suite.

## Versioning and compatibility

The project uses Semantic Versioning and Apache License 2.0. Current changes remain under [Unreleased](CHANGELOG.md); no new tag or release is created until cross-platform testing is accepted.

Previously shared `install/claude-ai` and `install/universal-web` URLs remain synchronized compatibility aliases. New documentation uses the professional package names above.
