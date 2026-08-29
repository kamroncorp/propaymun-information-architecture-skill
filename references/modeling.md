# Modeling and option generation

Read this reference when creating object models, taxonomies, labeling systems, navigation/search structures, or architecture alternatives.

## Semantic model sequence

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

## Model the information universe

Before choosing a visual or document structure, distinguish:

- **information domain:** a stable subject or responsibility area;
- **concept or object:** a recognizable thing people reason about or act on;
- **content type or record:** a governed information structure with attributes and lifecycle;
- **classification:** a way of grouping or faceting items;
- **destination or page:** a later interface exposure that belongs in a sitemap, not the canonical IA hierarchy;
- **task step:** an action or state transition that belongs in a user flow.

Build a parent-child hierarchy only where containment, scope, or classification is real. Add typed relationships for association, dependency, reference, membership, ownership, lifecycle, visibility, or derivation. Name the relationship in product language so a non-specialist can understand its consequence.

For an existing product, derive the candidate model from the content inventory, current structure, search/navigation evidence, policies, and observed failures. For a new product, derive it from audiences, priority tasks, planned capabilities, domain rules, and information that must be created, found, understood, governed, or retained.

## Object card

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

## Taxonomy design

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

## Generate meaningful alternatives

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

## Navigation model

Specify each navigation system's purpose, audience, content scope, ordering rule, visibility rule, and relationship to search. Avoid one overloaded global menu for unrelated tasks.

## Search model

Specify searchable objects/content, metadata and facets, synonyms, ranking signals, permission filtering, result types, empty-state behavior, and recovery. Never expose restricted content through labels, counts, snippets, or suggestions.

## AI product considerations

For products containing agents or generated content, also model:

- user, system, tool, source, conversation, run, artifact, memory, and permission objects;
- provenance and citation at the claim or artifact level;
- draft/review/approved states;
- human confirmation for consequential actions;
- visibility and retention boundaries;
- stable canonical locations despite adaptive recommendations;
- recovery, undo, retry, and escalation.
