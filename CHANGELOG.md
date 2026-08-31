# Changelog

All notable changes to this project are documented here. The project follows Semantic Versioning.

## [Unreleased]

### Changed

- Replaced model-branded distribution names with two professional packages: **Agent Skill Package** for native Skill upload and **Workspace Kit** for Projects, Gems, custom agents, and file-capable chats.
- Added an adaptive sufficiency loop that repeats whenever the work reaches a consequential new layer, an assumption changes, or an export is requested.
- Added contextual localization that separates language, locale, jurisdiction, culture, and operating model instead of inferring local roles or rules from language alone.
- Upgraded the canonical machine-readable contract to Semantic IA 2.0 with information domains, a single item registry, typed relationships, roles, permissions, lifecycle transitions, blocking unknowns, and handoff readiness.
- Reclassified Figma Make and Lovable as optional downstream **Visual Builder Handoff** targets generated only after the IA is ready.
- Added a deterministic builder exporter that produces both a self-contained Markdown specification and a short launch instruction for builder input fields.
- Required builder outputs to lead with a readable, connected domain-to-item architecture and explicitly exclude product UI, dashboards, sitemaps, user flows, APIs, and database schemas.
- Added deterministic package generation, a machine-scannable package manifest, canonical package paths, and synchronized legacy download aliases.
- Rewrote English and Persian repository guidance for human comprehension and reliable AI-assisted installation.
- Expanded behavioral and script coverage for midstream clarification, localization, Semantic IA integrity, package parity, export readiness, and downstream builder handoff.

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
