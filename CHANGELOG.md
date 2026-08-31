# Changelog

All notable changes to this project are documented here. The project follows Semantic Versioning.

## [Unreleased]

### Changed

- Reclassified Figma Make from a runtime adapter to an optional downstream visualization prompt generated only after the IA is stable.
- Added a deterministic, self-contained Figma Make prompt exporter that carries the canonical semantic model and forbids architecture reinvention.
- Added a Universal Web distribution for Projects, Gems, custom Agents, and file-capable chats, plus a short persistent activation instruction.
- Added a deterministic Claude.ai upload ZIP with `SKILL.md` and its resources in the required skill-folder package.
- Rewrote installation guidance to distinguish native Skill installation from Project/Gem configuration and one-off file use.
- Re-centered every output on one canonical semantic IA model before rendering.
- Defined the requested IA Structure Explorer as a downstream view led by connected hierarchy, typed relationships, and progressive detail.
- Added capability-first routing and a portable output ladder independent of model branding.
- Clarified that hierarchical IA maps use semantic domains and objects, while page maps and action paths remain separate sitemap and user-flow deliverables.
- Kept evidence status as model metadata and limited user-facing indicators to decision-relevant, plain-language uncertainty.
- Added behavioral coverage for existing-product audits, capability fallbacks, semantic consistency, Universal Web activation, and downstream Figma prompts.

## [0.3.0] - 2026-08-26

### Changed

- Added a shared autonomous sufficiency gate: material unknowns trigger a questions-only response and a hard stop without requiring prompting instructions from the user.
- Replaced fixed, jargon-heavy checkpoints with product-language decisions and consequence-aware assumptions for novice users.
- Clarified IA as the canonical semantic foundation while keeping sitemap and user-flow production in dedicated skills.
- Added environment-aware delivery shared by the canonical skill: conversation-first agents default to concise chat, while build-first environments use their native output medium.
- Reworked the Figma Make profile to build an architecture-first IA Structure Explorer after discovery instead of returning only text or building the product UI.
- Made Plan mode optional rather than a prerequisite for correct Figma behavior.
- Expanded capability-aware public research, private-data boundaries, source citation, and unavailable-tool fallbacks.
- Added a cross-platform adapter manifest and deterministic parity checks so the canonical skill, Figma adapter, metadata, and documentation release together.
- Added behavioral cases for empty Figma intake, sufficient Figma briefs, minimal novice answers, autonomous stopping, and source-aware public research.

## [0.2.0] - 2026-08-26

### Changed

- Restricted the skill to information architecture only; neighboring mapping deliverables are intentionally excluded.
- Made guided, question-first behavior the default for complete, complex, multi-role, sensitive, and consequential IA work.
- Limited quick provisional work to explicit speed or no-question requests and reduced its default depth.
- Replaced the default Markdown-and-Mermaid artifact with concise, decision-ready chat output.
- Required user acceptance before creating files, diagrams, images, or machine-readable models.
- Added audience-aware, human-first language guidance and pragmatic English technical labels for unreliable RTL renderers.
- Added capability detection, chat-only fallbacks, browsing/source rules, and privacy boundaries.
- Made IA diagrams optional and Draw.io/Excalidraw optional companions that require explicit installation authorization.
- Reworked deliverable guidance around layered, audience-specific communication instead of a fixed complete-report template.
- Expanded behavioral evaluation for natural Persian intake, medical-data risk, artifact consent, chat-only environments, and RTL diagrams.
- Made Figma adapter generation line-ending-stable across operating systems.

## [0.1.0] - 2026-08-25

### Added

- Guided, Quick Draft, and Focused Artifact modes.
- Evidence-aware IA workflow with five optional human checkpoints.
- Object-first modeling, taxonomy, labeling, navigation, search, permissions, validation, and governance references.
- Portable semantic IA JSON schema and structural validator.
- Standalone accessible HTML renderer with RTL support.
- Mermaid-first diagram routing with Draw.io and Excalidraw guidance.
- Single-file Figma agent/Figma Make adapter.
- English and Persian documentation.
- Three behavioral evaluation scenarios and deterministic script tests.

[Unreleased]: https://github.com/kamroncorp/propaymun-information-architecture-skill/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/kamroncorp/propaymun-information-architecture-skill/releases/tag/v0.3.0
[0.2.0]: https://github.com/kamroncorp/propaymun-information-architecture-skill/releases/tag/v0.2.0
[0.1.0]: https://github.com/kamroncorp/propaymun-information-architecture-skill/releases/tag/v0.1.0
