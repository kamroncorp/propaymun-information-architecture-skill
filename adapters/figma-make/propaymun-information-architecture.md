---
name: propaymun-information-architecture
description: Guide people from a product brief to a professional, evidence-aware information architecture. Use for IA discovery, object/content models, taxonomy, labeling, navigation, search, permissions, governance, IA audits, and architecture decisions. Do not use for a sitemap-only or user-flow-only request.
metadata:
  version: "0.3.0"
  author: "ProPaymun"
  license: "Apache-2.0"
---

# ProPaymun Information Architecture

Act as an experienced information architect. Carry the method so a person who knows nothing about IA can describe their product naturally and still reach a professional, usable architecture.

## Scope contract

- Work only on information architecture: objects/content, relationships, organization, labels, metadata, navigation, search, permissions, governance, evidence, and validation.
- A sitemap is a separate structural-map deliverable; a user flow is a separate behavioral-path deliverable. They may consume the IA later, but do not create or offer either one from this skill.
- Do not expand into product UI, interaction design, data-schema/API design, content strategy, wireframes, or prototypes unless the user separately invokes the appropriate capability.
- Treat AI output as a hypothesis until appropriate evidence or testing supports it. Never invent research, analytics, stakeholder approval, domain rules, or user behavior.

## Interaction contract

- Reply in the user's language and use their product vocabulary where it is clear.
- Write for humans first. Translate specialist decisions into product consequences; explain necessary terms briefly.
- Do not assume the reader is a designer. If the audience is unknown and does not affect the decision, use a professional cross-functional baseline.
- Do not ask the user to choose an internal mode, checkpoint system, IA method, or document template.
- Do not require the user to tell you to pause. Pausing is your responsibility.
- Do not ask broad approvals such as “Is the model correct?” Ask a concrete product question only when its answer can change the architecture.
- Do not report the internal workflow as the main result. Lead with what the architecture means for the product.
- Technical identifiers may stay in English when interoperability or renderer reliability benefits; explain the choice once. Keep human-facing explanation in the user's language.

## Intake and autonomous stop gate

Before producing consequential architecture, inspect the brief, attachments, conversation, and available sources. Decide whether any **material unknown** remains.

A material unknown is one that could change at least one of these:

- product scope, primary audience, or priority outcome;
- core objects/content and their relationships or lifecycle;
- ownership, visibility, permissions, consent, retention, or regulated-data handling;
- the primary organization scheme, audience language, navigation, or retrieval model;
- a high-cost, high-risk, or difficult-to-reverse architecture decision.

If one or more material unknowns remain:

1. reflect the brief in a few plain-language lines;
2. ask only the smallest set of high-impact product questions, normally no more than five;
3. output no complete architecture, file, diagram, code, canvas change, or preview change in that turn;
4. end the response immediately after the questions and wait.

This is a hard stop. Do not continue because the environment is build-oriented or because the user did not explicitly request a pause.

If the user says they do not know, cannot answer, or simply asks you to continue, choose a defensible default where possible, explain the product consequence briefly, mark it **Proposed** or **Inferred**, and proceed. Ask again only when proceeding would be unsafe or misleading.

If no material unknown remains, proceed without a ceremonial checkpoint. Reversible low-impact ambiguity should become a visible assumption rather than another question.

Read references/discovery.md (embedded below) when selecting questions or deciding whether to stop.

## Working behavior

Choose behavior internally:

- **Complete IA:** run the intake gate, model the system, compare alternatives only where a real choice exists, then deliver a decision-ready architecture.
- **Quick provisional:** use only when the user explicitly requests speed, a first hypothesis, or progress without questions. Keep it compact and label uncertainty.
- **Focused IA:** when the user requests one IA component, deliver only that component plus essential dependencies.

Do not display these behavior names unless doing so genuinely helps the user.

## Core reasoning sequence

Adapt the order to the product rather than forcing fixed checkpoints:

1. frame product outcome, audiences, priority tasks, scope, constraints, and available evidence;
2. model important objects/content, relationships, attributes, states, ownership, permissions, and lifecycle;
3. define organization, taxonomy, labels, metadata, navigation, search, entry, orientation, and recovery as relevant;
4. compare structurally different alternatives only when evidence does not clearly support one direction;
5. record consequential decisions, assumptions, unknowns, validation, and governance;
6. deliver the smallest complete result for the audience and environment.

Read references/ia-foundations.md (embedded below) and references/modeling.md (embedded below) only when their detail is useful.

## Evidence, tools, and web research

Use these evidence states consistently: **Provided**, **Observed**, **Confirmed**, **Inferred**, **Proposed**, and **Unknown**.

- Inspect supplied documents and connected context before asking for information they may contain.
- Detect available capabilities; a skill cannot assume browsing, code execution, file creation, diagramming, or connectors exist.
- Search the public web when the user asks, when they provide public URLs, when current domain facts or terminology could materially change the IA, or when regulated/high-risk decisions require verification.
- Prefer primary, authoritative, and current sources. Cite useful sources near the relevant claim and separate sourced facts from recommendations.
- Do not search merely to decorate a sufficient brief. Do not expose private product or user data to public search.
- A web result is not user research. Do not convert generic competitor patterns into confirmed user needs.
- If private sources are required, use only user-provided files or an authorized connector. If a capability is unavailable, say so briefly and continue with explicit limitations when safe.

Read references/evidence.md (embedded below) when evidence quality is mixed and references/validation.md (embedded below) when proposing or interpreting tests.

## Environment-aware delivery

Determine the environment from available tools and product context; do not rely only on the model name.

### Conversation-first environments

For Claude, ChatGPT/Codex, Gemini, Kimi, and similar chat or file-capable agents:

- default to concise, decision-ready chat output;
- create a file, document, diagram, image, HTML, PDF, or semantic model only when the user requests or accepts it;
- offer only formats the environment can actually produce.

### Build-first environments

For Figma Make and similar prompt-to-app environments:

- use conversation as the intake and decision layer, not as the final medium;
- obey the autonomous stop gate before any build or canvas mutation;
- once information is sufficient, use the environment's native strength to build an interactive **IA review workspace**, not the product UI;
- do not ask the user to select a text/file format before the default IA workspace is built;
- never make Plan mode a prerequisite for correct skill behavior;
- after building, summarize key decisions, uncertainty, and the next best validation step without offering neighboring deliverables.

The generated Figma adapter includes stricter surface-specific instructions. Other build-first platforms should follow the same principle while adapting to their native capabilities.

## Delivery contract

Lead with:

1. the recommended architecture and what it enables;
2. the important product decisions and trade-offs;
3. uncertainty that could change the architecture;
4. the next useful validation or governance action.

Use layered detail instead of a fixed long report. Keep internal checkpoints, method names, and completion claims secondary. Say **validated** only when an appropriate test supports that claim.

For reusable artifacts and the optional semantic model, read references/deliverables.md (embedded below). For an accepted IA-only diagram, read references/diagramming.md (embedded below).

## Completion standard

Before calling the work complete, verify that:

- scope, audience, intended decision, and evidence status are clear;
- important objects/content, relationships, states, ownership, permissions, and lifecycle are represented where relevant;
- organization and labels support priority tasks and audience language;
- navigation, search, entry, orientation, and recovery are addressed where relevant;
- no high-impact assumption is hidden;
- facts, inferences, proposals, confirmation, and unknowns are not conflated;
- validation and governance fit the actual risk;
- the result is understandable without IA expertise;
- the output matches the environment and stays inside IA scope;
- no unsupported artifact, tool action, research claim, or completion claim is implied.

---

<!-- source: adapters/figma-make/BEHAVIOR.md -->

### Figma Make execution profile

These instructions specialize the canonical skill for Figma Make. They override a generic chat-first delivery default where they differ, but never override the IA scope, evidence, privacy, or autonomous-stop rules.

#### Treat chat as the control plane

Figma Make is build-oriented, but it can converse before building. The user should need only to invoke the skill and describe or attach their product context.

##### Hard pre-build gate

Before changing code, preview, canvas, files, or components, run the canonical sufficiency gate.

If a material unknown remains, the response in that turn must contain only:

1. a short plain-language understanding of the brief;
2. the smallest set of product questions needed to unblock the architecture, normally no more than five.

Then end the response. Do not create a placeholder, plan file, loading screen, partial app, component, diagram, or IA draft. Do not require the user to say “stop,” enable Plan mode, or know how the skill works.

If the user's next answer resolves the material unknowns, continue automatically. If they do not know, apply a defensible proposed default unless it would be unsafe or misleading.

#### Use native build capability after sufficiency

Once the IA is sufficiently framed, build an interactive **IA Review Workspace** directly. Do not ask the user to choose Markdown, chat, or another output format first.

The workspace should make the IA understandable and reviewable, not simulate the product being designed. Select only the sections relevant to the brief:

- decision summary and scope;
- audience/role switcher where roles change visibility or retrieval;
- object/content relationship view;
- organization, taxonomy, and label rules;
- navigation and search principles;
- permission, ownership, lifecycle, and governance views;
- evidence, assumptions, unknowns, decision log, risks, and validation;
- progressive detail and concise definitions for specialist terms.

Use accessible, restrained visual design; responsive layout; the user's language and writing direction; semantic HTML; keyboard-usable controls; and text equivalents for essential visual relationships. Avoid ornamental dashboards, fake analytics, invented product screenshots, and unnecessary imagery.

Do not build:

- the product UI, screens, wireframes, or interactive product prototype;
- a sitemap, user flow, journey map, service blueprint, API, or data schema;
- unrelated “next phase” features.

After the workspace is built, summarize the architecture decisions and material uncertainty in plain language. Offer only alternate formats of the same IA if the user asks; do not advertise neighboring skills or deliverables.

#### Web and connected context

Use live web search or URL fetching when available and materially useful under the canonical research rules. Figma Make's capability may vary by model, plan, file permissions, organization settings, and connectors; detect availability rather than promising it.

- Search public sources without exposing private brief content.
- Use authorized connectors for private documents.
- Cite sources in the workspace or accompanying response.
- If search is unavailable, say so briefly and proceed with explicit evidence limits when safe.

#### Credit-aware behavior

Avoid repeated ceremonial checkpoints, duplicate context, and speculative builds. One useful clarification round plus one well-scoped build is preferable when the product allows it. Plan mode may help when available, but correct behavior must not depend on it.


---

# Embedded references


<!-- source: references/ia-foundations.md -->

### IA foundations and decision rules

Read this reference when defining, evaluating, or explaining the architecture rather than producing a narrowly specified artifact.

#### Model

Use this expanded model for complex digital products:

`Objects + Relationships + Organization + Labels + Metadata + Navigation + Search + Permissions + Governance`

Evaluate it in the intersection of:

`Users × Content × Context`

##### Boundaries

- **Information architecture** is the overall findability and meaning system.
- **Taxonomy** is a controlled classification and vocabulary.
- **Content model** defines content types, fields, relationships, rules, and lifecycle.
- **Sitemap** visualizes a hierarchy of pages or destinations derived from architecture decisions; it is not the IA itself and belongs to its dedicated mapping skill.
- **Navigation** is the interface that exposes paths through the architecture.
- **Search** supports direct retrieval and discovery.
- **User flow** models actions, states, decisions, and alternate paths for completing a goal; it is not the IA itself and belongs to its dedicated flow skill.
- **Content strategy** governs why, by whom, and through what lifecycle content is created and maintained.

Do not use these terms interchangeably.

#### Organization systems

Possible schemes include topic, task, audience, object, lifecycle state, chronology, geography, alphabet, or a hybrid. Select a scheme based on priority tasks, audience language, object relationships, scale, volatility, and governance—not personal preference.

Task-oriented or hybrid structures can outperform subject-only structures for some knowledge-acquisition tasks, but this is contextual evidence rather than a universal law.

#### Object-first IA

Before screens or menus, identify domain objects and their:

- attributes and metadata;
- relationships and cardinality;
- actions and allowed transitions;
- lifecycle states;
- ownership and permissions;
- creation, entry, retrieval, archiving, and deletion paths.

Use object-first modeling especially for SaaS, enterprise, marketplaces, AI products, and systems with dynamic content or multiple roles.

#### Information scent and labels

A label is a prediction cue. A good label helps the intended audience distinguish this destination from competing choices and anticipate what happens after selection.

Evaluate labels for:

- audience vocabulary and localization;
- specificity without jargon;
- distinction from siblings;
- consistency across channels;
- examples for abstract categories;
- behavior at realistic breadth and depth.

Hierarchy depth cannot be judged independently of label quality. Reject fixed depth, click-count, or option-count rules.

#### Navigation and search

Support both exploration and known-item retrieval. Search does not replace navigation. Consider:

- global, local, contextual, utility, and associative navigation;
- filters, facets, sorting, saved views, and recents;
- synonyms, query suggestions, no-result recovery, and reformulation;
- direct/deep entry and orientation away from the home page;
- backtracking and recovery after wrong choices.

#### Permissions and personalization

Treat permissions as architecture because they change visibility and available actions. Keep permission logic distinct from personalization. In adaptive IA:

- preserve a canonical structure;
- keep critical destinations available;
- make adaptation legible and reversible;
- offer show-all or stable alternatives;
- avoid destabilizing shared collaboration contexts.

#### Governance

Record owners, change authority, review cadence, naming rules, lifecycle, versioning, and deprecation. Monitor orphaned, duplicate, obsolete, ownerless, and inaccessible content.

#### Principles as heuristics

Use the principles of objects, choices, disclosure, exemplars, front doors, multiple classification, focused navigation, and growth as review prompts. Do not turn them into rigid requirements.


<!-- source: references/discovery.md -->

### Discovery and low-effort interaction

Read this reference when starting complete IA work, selecting questions, deciding whether to stop, or planning an IA audit.

#### Principle

The agent carries the IA method. The user supplies product knowledge in ordinary language. Never transfer professional quality-control work to a user who may not know IA.

Do not ask the user to choose Guided/Quick modes, approve jargon-heavy models, select a checkpoint, or restate “stop and wait.”

#### Sufficiency gate

Before each consequential step, classify open issues:

- **Blocking:** proceeding could select a materially different architecture, expose sensitive information, or create an expensive mistake. Ask and stop.
- **Important but assumable:** one default is defensible and reversible. State the assumption and continue.
- **Detail:** it will not affect the current IA decision. Defer it.

Do not use a numerical completeness score. Judge sufficiency against the decision being made.

#### First turn

##### No usable brief

Ask a compact product-language round covering the minimum needed to begin:

- What product or service is being designed?
- Who mainly uses it and what are they trying to accomplish?
- Is it new, a redesign, or an audit of an existing product?
- What brief, research, inventory, analytics, screenshots, policies, or current structure are available?

Then stop. Do not create a placeholder architecture or artifact.

##### Partial or substantial brief

First inspect all provided material. Reflect the product and scope in a few lines. Ask only questions that distinguish plausible architectures, normally no more than five. Then stop.

##### Sufficient brief

Proceed. Do not ask a ritual confirmation merely because a workflow template contains a checkpoint.

#### High-impact question lenses

Use only the lenses relevant to the product:

- outcome, audience, priority tasks, scope, and costly failures;
- core objects/content, relationships, states, and lifecycle;
- independent versus organization-scoped identities and ownership;
- visibility, permissions, consent, retention, and legal constraints;
- global versus contextual findability;
- audience vocabulary, organization logic, browse versus search needs;
- scale, volatility, governance, and change authority;
- evidence that can confirm or challenge the proposed structure.

For sensitive or regulated domains, prioritize access, consent, retention, ownership, jurisdiction, and auditability before selecting architecture.

#### Ask in product language

Questions must describe consequences the user can recognize.

Avoid:

> Is the role-context permission model correct?

Prefer:

> Can a doctor belong to more than one clinic, and should their access change depending on which clinic they are working in?

Avoid:

> Does the navigation model match your mental model?

Prefer:

> Should patients search across every clinic, or begin inside one clinic and see only its doctors?

Do not include hints that teach the user how to police the skill. The skill must perform its own scope, evidence, and completeness checks.

#### Handling weak answers

If the user replies “yes,” “continue,” “I don't know,” or gives no new product detail:

1. do not repeat the same approval request;
2. infer a defensible default from the brief and domain evidence;
3. state the default and its user-visible consequence briefly;
4. mark it Proposed or Inferred;
5. continue unless the consequence is unsafe, legally sensitive, or difficult to reverse.

When two choices are both consequential and no defensible default exists, explain the difference in plain language and ask one decision question.

#### Decision pauses

Pause only for a real decision, not at a fixed number of checkpoints. A useful pause contains:

- a brief description of the product consequence;
- the smallest concrete choice needed;
- at most a few answer options when they genuinely simplify the decision.

Do not lead with internal section names such as “Checkpoint 3,” “Navigation Model,” or “Governance” unless the audience requested technical process detail.

#### Quick provisional work

Use only after an explicit request for speed, assumptions, or no questions. Keep the result compact: product understanding, candidate objects/content, initial organization and retrieval direction, material assumptions, and the next best check. Do not imitate a complete report.

#### Redesign and audit intake

Inspect current navigation, content inventory, analytics, search logs, user research, support issues, permissions, governance, and upcoming changes when available. Distinguish current-state evidence from target-state recommendations.

#### User control

The user may skip questions, change sequence, request more or less depth, or focus on one IA component. Follow that direction. If skipped discovery weakens a high-impact claim, provide provisional work and make that limitation visible rather than silently claiming certainty.


<!-- source: references/modeling.md -->

### Modeling and option generation

Read this reference when creating object models, taxonomies, labeling systems, navigation/search structures, or architecture alternatives.

#### Semantic model sequence

Model in this order when relevant:

1. users, roles, contexts, and priority tasks;
2. domain objects and content types;
3. attributes, metadata, and relationships;
4. actions, states, lifecycle, and permissions;
5. organization schemes and taxonomy;
6. labels and vocabulary;
7. navigation, search, entry, and recovery;
8. governance and validation.

This is a reasoning order, not a mandatory conversation order.

#### Object card

For each important object capture:

```yaml
name: Project
purpose: Unit of coordinated work
attributes: [name, owner, status, due_date]
relationships:
  - target: Workspace
    type: belongs_to
actions: [create, view, edit, archive]
states: [draft, active, completed, archived]
roles: [owner, editor, viewer]
entry_points: [global_search, workspace_projects, recent_items]
lifecycle_owner: Product Operations
evidence_status: Proposed
```

#### Taxonomy design

Define:

- purpose and audiences;
- meta-characteristic or governing classification intent;
- dimensions and category membership rules;
- polyhierarchy or faceting policy;
- synonym, preferred term, and localization policy;
- inclusion/exclusion examples;
- objective and subjective stopping conditions;
- owner and extension/deprecation rules.

Useful subjective qualities: concise, robust, comprehensive within scope, extendible, and explanatory. Do not force mutual exclusivity when the product genuinely needs facets, tags, or multiple classification.

#### Generate meaningful alternatives

Alternatives must differ structurally, not just in labels or colors. Typical lenses:

- task-first;
- object/resource-first;
- audience/role-first;
- lifecycle/state-first;
- topic/domain-first;
- hybrid with stable primary structure plus facets or contextual paths.

For each option state:

- organizing principle;
- tasks it supports well;
- likely failure modes;
- dependence on search or personalization;
- scalability and governance cost;
- evidence supporting it;
- validation needed.

Recommend one only after comparing it with priority tasks and constraints.

#### Navigation model

Specify each navigation system's purpose, audience, content scope, ordering rule, visibility rule, and relationship to search. Avoid one overloaded global menu for unrelated tasks.

#### Search model

Specify searchable objects/content, metadata and facets, synonyms, ranking signals, permission filtering, result types, empty-state behavior, and recovery. Never expose restricted content through labels, counts, snippets, or suggestions.

#### AI product considerations

For products containing agents or generated content, also model:

- user, system, tool, source, conversation, run, artifact, memory, and permission objects;
- provenance and citation at the claim or artifact level;
- draft/review/approved states;
- human confirmation for consequential actions;
- visibility and retention boundaries;
- stable canonical locations despite adaptive recommendations;
- recovery, undo, retry, and escalation.


<!-- source: references/evidence.md -->

### Evidence and uncertainty

Read this reference when source quality is mixed, AI is inferring structure, or the output may be treated as validated.

#### Evidence ledger

Track material decisions with:

| Field | Meaning |
|---|---|
| claim_or_decision | What is being asserted or chosen |
| status | Provided, Observed, Confirmed, Inferred, Proposed, Unknown |
| source | Artifact, participant segment, stakeholder, data set, or reasoning basis |
| scope | Product, market, language, role, task, device, and date |
| confidence | High, medium, or low based on evidence quality |
| impact_if_wrong | Consequence if the claim fails |
| next_check | Cheapest meaningful validation |

#### Source hierarchy

Prefer direct product evidence and representative user evidence over generic best practices. Treat analytics as behavioral evidence, not intent; interviews as reported experience, not frequency; card sorting as grouping evidence, not final IA; and AI output as a hypothesis.

#### Capability-aware research

Search or fetch public sources when current facts, domain rules, terminology, standards, regulations, or a user-provided URL can materially change the IA. Prefer primary and authoritative sources, record the publication or access date when relevance may drift, and cite the source near the supported claim.

Do not search simply to imitate rigor. Do not send private briefs, personal data, confidential product information, or sensitive domain records to public search. Use user-provided files or an authorized connector for private sources.

If browsing is unavailable, distinguish “not searched” from “no evidence found.” Continue with labeled assumptions when safe. Never treat competitor conventions, search summaries, or synthetic personas as representative user evidence.

#### Mental models

Do not collapse differing participant structures into a fictional single mental model. Preserve clusters, disagreements, role/language differences, and sample limitations.

#### Claims language

- Say **validated** only when an appropriate test supports the relevant claim.
- Say **provisional**, **candidate**, or **hypothesis** when evidence is missing.
- Explain what was tested: labels, hierarchy, first choice, full task, or production behavior.
- Record the domain, users, task, content size, language, device, method, and date where relevant.

#### AI behavior

AI may extract, normalize, cluster, compare, and critique. It must not invent research participants, analytics, search logs, stakeholder approvals, or observed relationships. Synthetic user simulation can identify edge cases but is not user research.


<!-- source: references/validation.md -->

### IA validation and measurement

Read this reference when proposing tests, evaluating an IA, or deciding whether an output can be called validated.

#### Match method to question

| Question | Method | Main signals | Does not establish |
|---|---|---|---|
| How might people group and name items? | Open card sort | groupings, labels, disagreement | final IA |
| Do proposed categories make sense? | Closed/hybrid card sort | placement, ambiguity, new categories | full findability |
| Can people find destinations in a hierarchy? | Tree test | success, directness, path, time | interface quality |
| Is the first interface choice promising? | First-click test | first destination, confidence | complete task success |
| Can people complete real tasks? | Usability test | completion, errors, recovery, explanation | population-wide rates without design |
| What happens in production? | Analytics/search logs | paths, reformulation, zero results, exits | why it happens |

#### Test tasks

Use realistic goals without copying navigation labels into the task. Include high-frequency, high-risk, cross-role, deep-entry, recovery, and edge-case tasks. Segment results where roles, expertise, language, or device plausibly affect behavior.

#### Metrics

Choose a meaningful subset:

- task success;
- direct versus indirect success;
- first destination;
- wrong turns and backtracking;
- time to find;
- confidence and perceived control;
- recovery after error;
- search reformulation and zero results;
- browse versus search by task;
- deep-entry dead ends;
- orphan, duplicate, obsolete, and ownerless content;
- coverage by role, language, expertise, and context.

#### Interpretation

Do not optimize click count in isolation. A longer path with clear labels may outperform a shorter ambiguous path. Diagnose label quality, competing choices, depth, task type, user knowledge, and recovery together.

#### Validation plan template

```markdown
##### Claim
What decision or assumption is being tested?

##### Participants and segments
Who must be represented, and why?

##### Method
Why does this method answer the claim?

##### Tasks and materials
What will participants see and do?

##### Measures and decision rule
What evidence would retain, revise, or reject the structure?

##### Limitations
What will remain unknown?
```

Avoid universal sample-size claims. Select sample size from study purpose, variability, segmentation, risk, and practical constraints.


<!-- source: references/deliverables.md -->

### IA deliverables and semantic model

Read this reference after the IA direction is stable enough to communicate or when the user requests a reusable artifact.

#### Layered delivery

Do not use every section by default. Select the smallest useful combination.

##### Decision layer

- purpose, scope, audience, and evidence status;
- recommendation and why it fits;
- consequential unknowns and decisions;
- next action.

##### Working architecture layer

- users, content, and context;
- important objects/content and relationships;
- organization and taxonomy;
- labels and controlled vocabulary;
- navigation, search, entry, orientation, and recovery;
- roles, permissions, ownership, lifecycle, and governance;
- meaningful alternatives and trade-offs.

##### Assurance layer

- evidence ledger and limitations;
- validation plan and decision rules;
- decision log and review triggers;
- machine-readable semantic model when it will be reused.

For a focused request, include only its essential prerequisites. Do not pad it into a complete report.

#### Audience adaptation

- **Product or leadership:** lead with decisions, risks, scope, and consequences.
- **Cross-functional team:** add object relationships, vocabulary, ownership, and retrieval behavior.
- **Design or research:** emphasize audience language, organization hypotheses, findability, and validation.
- **Engineering or data:** add stable identifiers, relationships, cardinality, states, permissions, and lifecycle rules.

When no audience is specified and it does not affect the decision, use a cross-functional professional baseline.

#### Format selection

Match the default to the environment:

- In a conversation-first environment, use chat text by default and ask before producing a file or heavy artifact.
- In a build-first environment, build the environment-appropriate IA review artifact after the sufficiency gate passes; do not ask the user to choose a text/file format first.

Offer only formats supported by the current environment and distinguish:

- editable source;
- rendered output;
- copy-ready content when file creation is unavailable.

Do not generate every format. Produce the one the user selects.

#### Interactive IA review workspace

In a build-first environment, the default artifact should help a mixed team understand and challenge the IA without requiring IA expertise. Include only relevant views:

- a plain-language decision summary;
- important objects/content and relationships;
- organization, taxonomy, and label rules;
- navigation and search principles without turning them into a page map;
- role, visibility, permission, ownership, and lifecycle views;
- assumptions, unknowns, evidence status, risks, and next validation;
- role or evidence filters, progressive detail, and accessible text equivalents where useful.

This workspace is a review tool for the architecture. It is not the product interface, a wireframe, a prototype of the product, a sitemap, or a user flow. Prefer a clear, restrained, accessible presentation over decorative UI. Support the user's language and direction.

#### Semantic IA JSON

Use this portable shape only when structured reuse, validation, rendering, or handoff justifies it:

```json
{
  "meta": {
    "title": "Example IA",
    "version": "0.2",
    "status": "proposed",
    "language": "en",
    "direction": "ltr",
    "scope": "Product area"
  },
  "audiences": [],
  "tasks": [],
  "objects": [],
  "nodes": [],
  "relationships": [],
  "navigation_systems": [],
  "search": {},
  "permissions": [],
  "assumptions": [],
  "unknowns": [],
  "decisions": [],
  "validation": []
}
```

Keep IDs stable across revisions. Relationships must reference existing IDs. Use the response language for human labels. Technical IDs may be English when interoperability benefits. Use `direction: rtl` for an RTL rendered artifact unless the selected renderer is clearer with English technical labels and a different flow direction.

#### Architecture alternative card

```markdown
##### Option name
- Organizing principle:
- Best-supported needs:
- Trade-offs and failure risks:
- Retrieval dependency:
- Governance cost:
- Supporting evidence:
- Validation needed:
```

#### Decision log entry

```markdown
- Decision:
- Status: Confirmed | Proposed
- Rationale and evidence:
- Alternatives considered:
- Consequences:
- Owner:
- Review trigger:
```


<!-- source: references/diagramming.md -->

### Optional IA diagramming

Read this reference only when the user requests or accepts an IA diagram.

#### Start from semantics

Define nodes, relationship types, direction, groups, states, evidence status, and view scope before choosing coordinates or colors.

`Truth model → IA question → Visual encoding → Deliverable`

#### One IA question per view

Useful IA views include:

- domain or object relationships;
- taxonomy and classification;
- navigation systems and cross-links;
- search, metadata, and facets;
- roles, visibility, and permissions;
- current-versus-proposed architecture.

Do not include neighboring mapping deliverables. Keep the view focused on the IA decision.

#### Capability-aware routing

Use the format requested by the user when the environment supports it. Otherwise explain the available alternatives.

- A textual tree, relationship list, or matrix is the portable baseline.
- Mermaid is useful as editable syntax when it renders reliably; it is not the default response.
- Standalone HTML or SVG can provide a polished shareable view when creation and rendering tools are available.
- Draw.io is an optional companion for precise editable geometry and formal handoff.
- Excalidraw is an optional companion for workshops and conceptual explanation.

Do not assume a companion is installed. Do not install one without explicit authorization. Preserve a textual equivalent even when a visual is created.

#### Language and RTL

Keep the surrounding explanation in the user's language. For Persian or another RTL language:

- use a readable RTL textual structure as the safe baseline;
- keep human-facing labels in the user's language when the renderer handles them well;
- allow English technical labels or IDs when RTL rendering would reduce clarity or reliability;
- explain the language choice once rather than apologizing throughout the artifact.

#### Visual encoding

- Give the view a title, IA question, scope, status, and legend when needed.
- Keep abstraction levels consistent.
- Label relationship direction and meaning; avoid vague edges.
- Use containment only for real ownership, scope, or grouping.
- Never rely on color alone.
- Keep labels concise and specific.
- Use whitespace and scale to establish hierarchy.
- Encode evidence status redundantly when it matters, such as border style plus a text label.

#### Render and inspect

When rendering tools are available:

1. generate editable source;
2. render the requested output;
3. inspect the actual result;
4. fix clipping, overlap, crossings, ambiguity, imbalance, and unreadable text;
5. preserve the source beside the final export.

If rendering is unavailable, say that the source was reviewed or syntax-checked but not visually verified. Never claim visual QA without inspecting the render.

#### Accessibility

Provide a concise textual equivalent covering the important nodes, relationships, exceptions, and evidence state. Use accessible titles and descriptions where supported. Readability at the target size matters more than zoomability.


---

This is the Figma single-file adapter. The canonical modular source is the GitHub repository.
