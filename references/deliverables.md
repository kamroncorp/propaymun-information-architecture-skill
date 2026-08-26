# Deliverables and schemas

Read this reference when composing a complete IA package, a requested focused artifact, or a machine-readable model.

## Complete IA report

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

## Focused artifact behavior

When only one artifact is requested:

- state its scope and evidence status;
- include only prerequisite context;
- deliver the artifact in the requested format;
- identify dependencies or validation that could materially change it;
- do not pad it into a complete IA report.

## Semantic IA JSON

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

## Architecture alternative card

```markdown
### Option name
- Organizing principle:
- Best-supported tasks:
- Trade-offs:
- Failure risks:
- Search/personalization dependency:
- Governance cost:
- Supporting evidence:
- Validation needed:
```

## Decision log entry

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

