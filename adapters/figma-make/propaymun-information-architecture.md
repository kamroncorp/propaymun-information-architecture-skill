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

For choosing questions and handling missing inputs, read references/discovery.md (embedded below).

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

For IA concepts and decision rules, read references/ia-foundations.md (embedded below). For modeling and alternative generation, read references/modeling.md (embedded below).

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

Use confidence only for the quality of evidence behind a claim. Do not treat model confidence as user evidence. Read references/evidence.md (embedded below) for provenance rules.

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

If the user requests only one artifact, create that artifact and include only dependencies essential to understand it. For schemas and output patterns, read references/deliverables.md (embedded below).

## Diagram and format routing

Honor an explicit format request. If none is given, use a concise Markdown report plus Mermaid for a fast, professional, versionable result. Also provide a short textual equivalent of every essential diagram.

- **Mermaid** — default for Git/Markdown, quick review, and reproducibility.
- **Draw.io** — recommend or use when precise geometry, custom shapes, swimlanes, multi-page editing, or formal handoff matters.
- **Excalidraw** — recommend or use for conceptual explanation, workshops, or teaching-oriented visual arguments.
- **HTML** — use when the user needs a shareable interactive or standalone browser artifact.
- **Image/SVG/PDF** — use when presentation or distribution matters; preserve an editable source when possible.

Do not mix taxonomy, sitemap, and behavioral flow into one unreadable diagram. Split views when questions or abstraction levels differ. Read references/diagramming.md (embedded below) when visual output is requested.

## Validation

Choose methods by the claim being tested:

- open card sorting discovers candidate groupings and vocabulary;
- closed or hybrid sorting examines proposed categories;
- tree testing evaluates findability in hierarchy and labels without visual design;
- first-click testing examines the initial choice in an interface;
- usability testing examines complete tasks in the actual experience;
- analytics and search logs show behavior and retrieval problems, not user intent by themselves.

Do not rely on universal rules such as three clicks, three levels, a fixed number of menu items, or “flatter is always better.” Evaluate information scent, task success, directness, recovery, confidence, and segment differences. Read references/validation.md (embedded below) for test design and metrics.

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
- **Sitemap** is a representation of page or destination structure.
- **Navigation** is the interface that exposes paths through the architecture.
- **Search** supports direct retrieval and discovery.
- **User flow** represents a path through states and decisions to accomplish a task.
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

### Discovery and intake

Read this reference when context is incomplete, when selecting Guided or Quick Draft mode, or when planning an IA audit.

#### Minimum framing

Try to establish:

1. product and business outcome;
2. primary audiences, roles, expertise, language, and accessibility needs;
3. priority tasks and high-risk failures;
4. content, capabilities, domain objects, and lifecycle;
5. current-state structure and pain points, if any;
6. evidence available: research, analytics, search logs, support data, content inventory, or existing maps;
7. technical, organizational, legal, security, and timeline constraints;
8. requested artifacts, formats, and level of detail.

Do not ask for every item if the user already supplied enough to proceed.

#### Guided mode question strategy

Ask compact rounds of high-impact questions. Prefer questions that separate possible architectures.

##### Round A — framing

- What product or service is this, and what outcome should the IA improve?
- Who are the main audiences or roles, and which tasks matter most?
- Is this greenfield, redesign, or an audit of an existing structure?
- What evidence or artifacts can be inspected?

Checkpoint: summarize scope, success, knowns, and unknowns for confirmation.

##### Round B — inventory and model

- What are the important objects, content types, capabilities, and destinations?
- What actions, states, relationships, and permissions affect them?
- What must be globally findable, and what is contextual or role-specific?
- What changes frequently, grows quickly, or requires governance?

Checkpoint: present a compact inventory and object model for correction.

##### Round C — structure and delivery

- Do audiences use different vocabulary or classification approaches?
- Which retrieval behaviors are browse-first, search-first, or both?
- Which outputs and editable/rendered formats are required?
- What validation can realistically be performed before launch?

Checkpoint: compare alternatives before finalizing.

#### Quick Draft behavior

When speed is requested:

1. state the assumed product, users, tasks, and scope;
2. identify missing evidence that could materially change the design;
3. build a provisional architecture from supplied information;
4. separate high-confidence structure from tentative decisions;
5. give the next most valuable validation step.

Do not withhold all useful work merely because research is absent.

#### Redesign intake

Inspect or request the current sitemap/navigation, content inventory, analytics, search logs, user research, support issues, permissions, governance, and upcoming product changes. Distinguish current-state facts from target-state recommendations.

#### Freehand override

The user may request a different process, skip checkpoints, dictate a format, or ask for one artifact. Follow that direction unless it would make a high-risk claim misleading; in that case, provide the requested result and clearly label its limits.


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

### Deliverables and schemas

Read this reference when composing a complete IA package, a requested focused artifact, or a machine-readable model.

#### Complete IA report

Use only sections that help the decision:

1. Executive summary
2. Scope, status, and audience
3. Evidence and limitations
4. Users × Content × Context
5. Inventory and audit
6. Domain/object model
7. Taxonomy and labels
8. Navigation and search
9. Roles, permissions, and visibility
10. Architecture alternatives
11. Selected architecture and rationale
12. Semantic model and visual map
13. Validation plan and metrics
14. Governance and decision log

Lead with the recommendation and important uncertainty rather than process narration.

#### Focused artifact behavior

When only one artifact is requested:

- state its scope and evidence status;
- include only prerequisite context;
- deliver the artifact in the requested format;
- identify dependencies or validation that could materially change it;
- do not pad it into a complete IA report.

#### Semantic IA JSON

Use this portable shape when a machine-readable source is useful:

```json
{
  "meta": {
    "title": "Example IA",
    "version": "0.1",
    "status": "proposed",
    "language": "en",
    "direction": "ltr",
    "scope": "Product area"
  },
  "audiences": [],
  "tasks": [],
  "objects": [],
  "nodes": [
    {
      "id": "home",
      "label": "Home",
      "type": "destination",
      "parent_id": null,
      "evidence_status": "Proposed"
    }
  ],
  "relationships": [
    {
      "id": "rel-1",
      "from": "home",
      "to": "projects",
      "type": "contains",
      "label": "Primary destination",
      "evidence_status": "Proposed"
    }
  ],
  "navigation_systems": [],
  "search": {},
  "permissions": [],
  "assumptions": [],
  "unknowns": [],
  "decisions": [],
  "validation": []
}
```

Keep node IDs stable across revisions. Relationships must reference existing node IDs. Use `direction: rtl` for Persian/Arabic output unless the user requests a different diagram flow.

#### Architecture alternative card

```markdown
##### Option name
- Organizing principle:
- Best-supported tasks:
- Trade-offs:
- Failure risks:
- Search/personalization dependency:
- Governance cost:
- Supporting evidence:
- Validation needed:
```

#### Decision log entry

```markdown
- Decision:
- Status: Confirmed | Proposed
- Rationale:
- Evidence:
- Alternatives considered:
- Consequences:
- Owner:
- Review trigger:
```


<!-- source: references/diagramming.md -->

### IA diagramming

Read this reference whenever visual output is requested or generated.

#### Start from semantics

Define nodes, relationship types, direction, groups, states, evidence status, and view scope before choosing coordinates or colors.

Use this model:

`Truth model → Viewpoint → Visual encoding → Deliverable`

#### Split views by question

Do not force all IA into one canvas. Typical views:

- domain/object relationship map;
- taxonomy or classification map;
- destination hierarchy/sitemap;
- navigation and cross-link map;
- search/facet model;
- roles and permissions matrix/map;
- current versus proposed comparison.

Keep behavioral user flows separate unless showing one example path is necessary to validate the IA.

#### Default routing

When the user does not specify a format, provide Markdown plus Mermaid. Choose:

- `flowchart` for hierarchy, object relationships, and navigation maps;
- `classDiagram` or `erDiagram` when formal object/data relationships matter;
- multiple small diagrams rather than one crowded graph.

Recommend Draw.io for editable formal handoff, custom icons, swimlanes, exact routing, and multi-page diagrams. Recommend Excalidraw for workshops and teaching-oriented narratives. Use HTML for a shareable standalone artifact or interactive exploration.

#### Visual encoding

- Give every diagram a title, type, scope, status, and legend.
- Keep abstraction levels consistent within a view.
- Label relationship direction and meaning; avoid generic “uses.”
- Use containment only for real ownership, scope, or grouping.
- Use color consistently and never as the only carrier of meaning.
- Keep labels concise but specific and audience-appropriate.
- Route edges around unrelated nodes and labels.
- Use whitespace and scale to establish hierarchy.
- Adapt flow direction to language and audience; do not assume LTR for Persian.

#### Evidence display

When helpful, encode evidence status with a redundant combination of label/pattern and color, for example:

- solid border + `Confirmed`;
- ordinary border + `Proposed`;
- dashed border + `Inferred`;
- dotted placeholder + `Unknown`.

Always include a legend.

#### Render and inspect

When rendering tools are available:

1. generate editable source;
2. render to SVG or PNG;
3. inspect the actual image;
4. fix clipping, overlap, crossings, ambiguity, imbalance, and unreadable text;
5. re-render until the view is usable;
6. preserve source alongside the final export.

If rendering is unavailable, state that the source was syntax-checked or reviewed but not visually verified.

#### Accessibility

Provide a concise textual equivalent that conveys nodes, hierarchy, important relationships, exceptions, and status. For SVG/Mermaid, add an accessible title and description when supported. Check the target output size; zoom is not a substitute for readable defaults.


---

This is the Figma single-file adapter. The canonical modular source is the GitHub repository.
