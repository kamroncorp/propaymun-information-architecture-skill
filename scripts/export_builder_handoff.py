#!/usr/bin/env python3
"""Export Semantic IA 2.0 as a Markdown visual-builder specification and short launch text."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from validate_ia_model import validate_model


TARGET_NAMES = {
    "figma-make": "Figma Make",
    "lovable": "Lovable",
    "generic": "the visual builder",
}


def launch_text(language: str) -> str:
    if language.lower().startswith("fa"):
        return "فایل Markdown پیوست‌شده را به‌عنوان مشخصات کامل ساخت بخوان و نسخه اولیه را دقیقاً براساس آن بساز؛ معماری اطلاعات را تغییر نده و اطلاعات جدید اختراع نکن."
    return "Read the attached Markdown file as the complete build specification. Build the first version exactly from it; do not redesign the information architecture or invent missing information."


def bullet(lines: list[str]) -> str:
    return "\n".join(f"- {line}" for line in lines) if lines else "- None supplied"


def structural_summary(model: dict) -> str:
    items = model.get("items", [])
    item_by_id = {item.get("id"): item for item in items}
    domain_lines: list[str] = []
    for domain in model.get("domains", []):
        members = [item for item in items if item.get("domain_id") == domain.get("id")]
        member_text = ", ".join(f"{item.get('label')} ({item.get('id')})" for item in members) or "no mapped items"
        domain_lines.append(f"{domain.get('label')} ({domain.get('id')}): {member_text}")

    hierarchy_lines: list[str] = []
    for item in items:
        parent_id = item.get("parent_id")
        if parent_id:
            parent = item_by_id.get(parent_id, {})
            hierarchy_lines.append(f"{parent.get('label', parent_id)} → {item.get('label')} [contains/scopes]")
        for alternative in item.get("alternative_parent_ids", []):
            parent = item_by_id.get(alternative, {})
            hierarchy_lines.append(f"{parent.get('label', alternative)} → {item.get('label')} [alternative scope; not a second default parent]")

    relationship_lines = [
        f"{item_by_id.get(rel.get('from'), {}).get('label', rel.get('from'))} → "
        f"{item_by_id.get(rel.get('to'), {}).get('label', rel.get('to'))} "
        f"[{rel.get('type')}] {rel.get('label')}: {rel.get('meaning')}"
        for rel in model.get("relationships", [])
    ]
    return f"""### Domain-to-item map
{bullet(domain_lines)}

### Primary hierarchy
{bullet(hierarchy_lines)}

### Typed cross-relationships
{bullet(relationship_lines)}"""


def export_specification(model: dict, target: str) -> str:
    errors, warnings = validate_model(model)
    if errors:
        raise ValueError("Cannot export invalid Semantic IA:\n- " + "\n- ".join(errors))

    meta = model["meta"]
    readiness = meta.get("handoff", {}).get("readiness", "not-ready")
    if readiness == "not-ready":
        raise ValueError("Semantic IA handoff readiness is not-ready; resolve material unknowns before export")

    target_name = TARGET_NAMES[target]
    payload = json.dumps(model, ensure_ascii=False, indent=2)
    warning_block = bullet(warnings) if warnings else "- No structural validator warnings"
    locale = json.dumps(meta.get("locale_context", {}), ensure_ascii=False)
    return f"""# Build a Connected Information Architecture Blueprint

## Target role

You are using {target_name} as a renderer of an already-developed information architecture. Do not redesign, expand, simplify, localize, or reinterpret the supplied IA.

## Context

- Title: {meta.get('title')}
- Scope: {meta.get('scope')}
- Model status: {meta.get('status')}
- Handoff purpose: {meta.get('handoff', {}).get('purpose')}
- Handoff readiness: {readiness}
- Language: {meta.get('language')}
- Writing direction: {meta.get('direction')}
- Locale context: {locale}

## Human-readable structural summary

{structural_summary(model)}

## Canonical Semantic IA

This JSON is the source of truth. Every visible domain, item, label, state, permission, and connection must trace to it.

```json
{payload}
```

## Primary-view requirements

1. Make the first view the connected information architecture itself.
2. Show every information domain as a clearly labeled container or region.
3. Place every visible item inside its assigned domain; do not drop or merge items to simplify layout.
4. Use continuous connectors for the primary hierarchy and labeled connectors for typed cross-domain relationships.
5. Fit the graph to the available viewport. The architecture should occupy at least about two-thirds of the primary canvas without clipping or excessive empty space.
6. Use readable item cards, practical text sizes, accessible contrast, and spacing that supports scanning.
7. Hide technical IDs by default. Reveal them only in an optional inspect/detail view.
8. Make relationship direction and meaning understandable without relying on color. Keep labels readable at the default zoom.
9. Put roles/access, lifecycle, assumptions, conflicts, unknowns, decisions, evidence, and technical details in progressive secondary views.
10. Provide a compact readable legend and a plain-text equivalent of the hierarchy and relationships.
11. Use {meta.get('language')} for human-facing text and implement a real {meta.get('direction')} layout.

The connected blueprint must not be replaced by a tabbed dashboard, card catalogue, or specialist review explorer.

## Hard exclusions

- Do not create a sitemap, user flow, wireframe, product prototype, API, or database schema.
- Do not turn semantic items into screens or relationships into click paths.
- Do not invent research, approval, local rules, permissions, entities, relationships, or validation results.
- Do not silently repair contradictions; show a concise conflict notice.
- Do not ask product-discovery questions inside the built artifact.

## Source warnings

{warning_block}

## Acceptance checks

- A non-specialist can identify the domains, hierarchy, and important connections from the first view.
- Every visible item is mapped to a domain and traceable to the canonical JSON.
- Access distinctions and consequential uncertainty are understandable without reading every detail.
- The default view is readable without zooming into tiny labels or searching across large empty areas.
- Secondary detail supports the connected architecture rather than replacing it.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("--target", choices=sorted(TARGET_NAMES), default="figma-make")
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--launch-output", type=Path)
    args = parser.parse_args()

    model = json.loads(args.model.read_text(encoding="utf-8"))
    try:
        specification = export_specification(model, args.target)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    output = args.output or args.model.with_name(f"{args.model.stem}-{args.target}-handoff.md")
    launch_output = args.launch_output or output.with_name(f"{output.stem}-launch.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(specification, encoding="utf-8", newline="\n")
    launch_output.write_text(launch_text(model["meta"].get("language", "en")) + "\n", encoding="utf-8", newline="\n")
    print(output)
    print(launch_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
