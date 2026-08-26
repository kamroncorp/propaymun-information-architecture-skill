# IA deliverables and semantic model

Read this reference after the IA direction is stable enough to communicate or when the user requests a reusable artifact.

## Layered delivery

Do not use every section by default. Select the smallest useful combination.

### Decision layer

- purpose, scope, audience, and evidence status;
- recommendation and why it fits;
- consequential unknowns and decisions;
- next action.

### Working architecture layer

- users, content, and context;
- important objects/content and relationships;
- organization and taxonomy;
- labels and controlled vocabulary;
- navigation, search, entry, orientation, and recovery;
- roles, permissions, ownership, lifecycle, and governance;
- meaningful alternatives and trade-offs.

### Assurance layer

- evidence ledger and limitations;
- validation plan and decision rules;
- decision log and review triggers;
- machine-readable semantic model when it will be reused.

For a focused request, include only its essential prerequisites. Do not pad it into a complete report.

## Audience adaptation

- **Product or leadership:** lead with decisions, risks, scope, and consequences.
- **Cross-functional team:** add object relationships, vocabulary, ownership, and retrieval behavior.
- **Design or research:** emphasize audience language, organization hypotheses, findability, and validation.
- **Engineering or data:** add stable identifiers, relationships, cardinality, states, permissions, and lifecycle rules.

When no audience is specified and it does not affect the decision, use a cross-functional professional baseline.

## Format selection

Match the default to the environment:

- In a conversation-first environment, use chat text by default and ask before producing a file or heavy artifact.
- In a build-first environment, build the environment-appropriate IA review artifact after the sufficiency gate passes; do not ask the user to choose a text/file format first.

Offer only formats supported by the current environment and distinguish:

- editable source;
- rendered output;
- copy-ready content when file creation is unavailable.

Do not generate every format. Produce the one the user selects.

## Interactive IA review workspace

In a build-first environment, the default artifact should help a mixed team understand and challenge the IA without requiring IA expertise. Include only relevant views:

- a plain-language decision summary;
- important objects/content and relationships;
- organization, taxonomy, and label rules;
- navigation and search principles without turning them into a page map;
- role, visibility, permission, ownership, and lifecycle views;
- assumptions, unknowns, evidence status, risks, and next validation;
- role or evidence filters, progressive detail, and accessible text equivalents where useful.

This workspace is a review tool for the architecture. It is not the product interface, a wireframe, a prototype of the product, a sitemap, or a user flow. Prefer a clear, restrained, accessible presentation over decorative UI. Support the user's language and direction.

## Semantic IA JSON

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

## Architecture alternative card

```markdown
### Option name
- Organizing principle:
- Best-supported needs:
- Trade-offs and failure risks:
- Retrieval dependency:
- Governance cost:
- Supporting evidence:
- Validation needed:
```

## Decision log entry

```markdown
- Decision:
- Status: Confirmed | Proposed
- Rationale and evidence:
- Alternatives considered:
- Consequences:
- Owner:
- Review trigger:
```
