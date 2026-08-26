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

Use chat text by default. Ask before producing a file or heavy artifact. Offer only formats supported by the current environment and distinguish:

- editable source;
- rendered output;
- copy-ready content when file creation is unavailable.

Do not generate every format. Produce the one the user selects.

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
