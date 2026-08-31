#!/usr/bin/env python3
"""Export a stable semantic IA JSON model as a self-contained Figma Make prompt."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def bullets(items: list[dict], fields: tuple[str, ...]) -> str:
    lines = []
    for item in items:
        if not isinstance(item, dict):
            lines.append(f"- {item}")
            continue
        values = [str(item.get(field, "")).strip() for field in fields]
        values = [value for value in values if value]
        if values:
            lines.append("- " + " — ".join(values))
    return "\n".join(lines) or "- None supplied"


def export_prompt(model: dict) -> str:
    meta = model.get("meta", {})
    language = meta.get("language", "en")
    direction = meta.get("direction", "ltr")
    relationships = []
    for rel in model.get("relationships", []):
        relationships.append({
            "id": rel.get("id", ""),
            "meaning": f"{rel.get('from_id', rel.get('from', '?'))} → {rel.get('to_id', rel.get('to', '?'))} [{rel.get('type', 'related')}] {rel.get('label', rel.get('meaning', ''))}".strip(),
        })
    payload = json.dumps(model, ensure_ascii=False, indent=2)
    return f"""# Build an Information Architecture Review Explorer

You are a renderer of an already-developed information architecture. Do not redesign, expand, simplify, or reinterpret the supplied IA.

## Context

- Title: {meta.get('title', 'Information Architecture')}
- Scope: {meta.get('scope', 'Supplied IA scope')}
- Status: {meta.get('status', 'proposed')}
- Language: {language}
- Writing direction: {direction}

## Human-readable structural summary

### Information domains
{bullets(model.get('information_domains', []), ('id', 'name', 'description'))}

### Objects and content types
{bullets(model.get('objects', []), ('id', 'name', 'description'))}

### Hierarchical nodes
{bullets(model.get('nodes', []), ('id', 'label', 'parent_id'))}

### Typed cross-relationships
{bullets(relationships, ('id', 'meaning'))}

## Canonical semantic IA model

Use this JSON as the source of truth. Every visible item and connection must trace to it.

```json
{payload}
```

## Build requirements

1. Make the first view a connected IA hierarchy: information domains, important objects/content types, containment, and labeled cross-relationships.
2. Preserve abstraction levels. Do not turn objects into screens or relationships into click paths.
3. Put definitions, attributes, states, roles/access, taxonomy, findability, decisions, and uncertainty behind selection, expansion, filters, or focused secondary views.
4. Make hierarchy and relationship direction understandable without relying on color. Provide a compact legend and a readable text equivalent.
5. Use {language} for human-facing text and implement a real {direction} layout. Concise English technical IDs are allowed when they improve reliability.
6. Keep the visual language calm, spacious, accessible, and review-oriented. This is not a product dashboard or product UI.

## Hard exclusions

- Do not create a sitemap, user flow, wireframe, product prototype, API, or database schema.
- Do not invent research, approval, rules, permissions, entities, relationships, or validation results.
- Do not silently repair contradictions. Show a concise conflict notice instead.
- Do not ask product-discovery questions inside the built artifact.

## Acceptance checks

- A non-specialist can identify the main domains, hierarchy, and important connections from the first view.
- Access distinctions and consequential uncertainty are understandable without reading every detail.
- Specialist detail supports the connected architecture rather than replacing it with tabs, tables, or cards.
- Every rendered element is traceable to the supplied JSON.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    model = json.loads(args.model.read_text(encoding="utf-8"))
    prompt = export_prompt(model)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(prompt, encoding="utf-8", newline="\n")
        print(args.output)
    else:
        print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
