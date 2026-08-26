---
name: propaymun-information-architecture
description: Design, evaluate, or restructure information architecture for digital products, including object and content models, taxonomy, labeling, navigation, search, permissions, validation, and IA diagrams. Use when a user asks for information architecture, IA, content organization, taxonomy or navigation architecture, or wants product requirements turned into a findable structure. Do not use for a sitemap-only or user-flow-only request unless IA decisions are also needed.
metadata:
  version: "0.1.0"
  author: "ProPaymun"
  license: "Apache-2.0"
---

# ProPaymun Information Architecture

Help product managers, product designers, researchers, content practitioners, founders, and other product contributors create evidence-aware information architecture with AI.

## Operating principles

- Treat IA as a system of objects, relationships, organization, labels, metadata, navigation, search, permissions, and governance—not merely a menu or sitemap.
- Preserve the user's scope, requested artifacts, terminology, sequence, and output format. The workflow is a useful default, not a restriction.
- Distinguish supplied or observed facts from confirmed decisions, inferences, proposals, and unknowns.
- Do not represent AI-generated groupings as users' mental models or an untested structure as validated IA.
- Prefer a small set of justified alternatives over one falsely certain answer when evidence is weak.
- Match depth to product complexity, decision risk, and the user's requested fidelity.
- Reply in the user's language. For Persian and other RTL languages, make reading direction and diagram flow deliberate.

## Select the working mode

Use **Guided mode** by default when the user wants a complete IA, the product is complex or consequential, or critical context is missing. Gather information in compact rounds and use the checkpoints below.

Use **Quick Draft mode** when the user requests speed, supplies a substantial brief, or asks for an initial hypothesis. Produce useful work immediately, mark assumptions and unknowns, and state what needs validation.

Use **Focused artifact mode** when the user asks for only one or a subset of outputs, such as taxonomy, labeling, navigation, search, permissions, object model, IA audit, or validation plan. Do not force the complete workflow.

For choosing questions and handling missing inputs, read [references/discovery.md](references/discovery.md).

## Core workflow

Adapt or reorder these phases when the user directs otherwise.

1. **Frame** — establish product, users and roles, priority tasks, context, scope, constraints, evidence, and success criteria.
2. **Inventory** — identify content, capabilities, destinations, data, duplication, gaps, owners, and lifecycle state.
3. **Model** — define domain objects, attributes, relationships, actions, states, permissions, and lifecycle before committing to pages or menus.
4. **Research and language** — extract user vocabulary, tasks, observed behavior, segments, locale, and current search/navigation evidence.
5. **Generate alternatives** — propose structurally distinct organization and labeling options with trade-offs.
6. **Select and specify** — choose or combine a direction, then specify taxonomy, labels, navigation, search, entry points, recovery, permissions, and governance.
7. **Validate** — design structure, interface, and production checks proportionate to risk.
8. **Deliver** — provide only the requested artifacts, plus enough assumptions and rationale to make them safe to use.

For IA concepts and decision rules, read [references/ia-foundations.md](references/ia-foundations.md). For modeling and alternative generation, read [references/modeling.md](references/modeling.md).

## Default checkpoints

In Guided mode, pause for confirmation at these points unless the user asks to proceed without pauses:

1. framing: scope, users, tasks, evidence, and success;
2. inventory/model: important objects, content, relationships, states, and permissions;
3. alternatives: compare viable structures and recommend one;
4. architecture: confirm the selected IA and unresolved exceptions;
5. validation/delivery: confirm the validation plan and requested formats.

Ask no more than a compact group of high-impact questions at a time. Do not repeat answered questions. When a reasonable reversible assumption enables progress, state it and continue.

## Evidence states

Tag material when its status matters:

- **Provided** — stated or supplied by the user;
- **Observed** — directly found in an inspected artifact or data source;
- **Confirmed** — explicitly accepted by an authorized stakeholder;
- **Inferred** — reasoned from evidence but not directly established;
- **Proposed** — a design recommendation;
- **Unknown** — missing or unresolved.

Use confidence only for the quality of evidence behind a claim. Do not treat model confidence as user evidence. Read [references/evidence.md](references/evidence.md) for provenance rules.

## Deliverables

For a complete IA, offer or produce the relevant subset of:

- IA brief and executive summary;
- Users × Content × Context;
- inventory and audit findings;
- domain/object model;
- taxonomy and classification rules;
- labeling system and controlled vocabulary;
- navigation, search, entry points, and recovery model;
- roles, permissions, and visibility;
- architecture alternatives and decision rationale;
- assumptions, unknowns, evidence status, and decision log;
- validation plan and success measures;
- governance and change policy;
- semantic IA model and visual map.

If the user requests only one artifact, create that artifact and include only dependencies essential to understand it. For schemas and output patterns, read [references/deliverables.md](references/deliverables.md).

## Diagram and format routing

Honor an explicit format request. If none is given, use a concise Markdown report plus Mermaid for a fast, professional, versionable result. Also provide a short textual equivalent of every essential diagram.

- **Mermaid** — default for Git/Markdown, quick review, and reproducibility.
- **Draw.io** — recommend or use when precise geometry, custom shapes, swimlanes, multi-page editing, or formal handoff matters.
- **Excalidraw** — recommend or use for conceptual explanation, workshops, or teaching-oriented visual arguments.
- **HTML** — use when the user needs a shareable interactive or standalone browser artifact.
- **Image/SVG/PDF** — use when presentation or distribution matters; preserve an editable source when possible.

Do not mix taxonomy, sitemap, and behavioral flow into one unreadable diagram. Split views when questions or abstraction levels differ. Read [references/diagramming.md](references/diagramming.md) when visual output is requested.

## Validation

Choose methods by the claim being tested:

- open card sorting discovers candidate groupings and vocabulary;
- closed or hybrid sorting examines proposed categories;
- tree testing evaluates findability in hierarchy and labels without visual design;
- first-click testing examines the initial choice in an interface;
- usability testing examines complete tasks in the actual experience;
- analytics and search logs show behavior and retrieval problems, not user intent by themselves.

Do not rely on universal rules such as three clicks, three levels, a fixed number of menu items, or “flatter is always better.” Evaluate information scent, task success, directness, recovery, confidence, and segment differences. Read [references/validation.md](references/validation.md) for test design and metrics.

## Completion standard

Before calling work complete, verify that:

- scope, audience, status, and requested artifacts are explicit;
- important objects, relationships, roles, states, permissions, and lifecycle constraints are represented where relevant;
- labels use audience language and distinguish competing choices;
- alternative entry points, search, recovery, and deep links are considered;
- facts, inferences, proposals, and unknowns are not conflated;
- the visual output matches the semantic model and has been rendered and inspected when tools permit;
- diagrams do not rely on color alone and have a textual equivalent;
- validation and governance are proportionate to the decision risk;
- the user can edit or reuse the result in the requested format.

