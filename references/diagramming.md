# Optional IA diagramming

Read this reference only when the user requests or accepts an IA diagram.

## Start from semantics

Define nodes, relationship types, direction, groups, states, evidence status, and view scope before choosing coordinates or colors.

`Truth model → IA question → Visual encoding → Deliverable`

## One IA question per view

Useful IA views include:

- domain or object relationships;
- taxonomy and classification;
- navigation systems and cross-links;
- search, metadata, and facets;
- roles, visibility, and permissions;
- current-versus-proposed architecture.

Do not include neighboring mapping deliverables. Keep the view focused on the IA decision.

## Capability-aware routing

Use the format requested by the user when the environment supports it. Otherwise explain the available alternatives.

- A textual tree, relationship list, or matrix is the portable baseline.
- Mermaid is useful as editable syntax when it renders reliably; it is not the default response.
- Standalone HTML or SVG can provide a polished shareable view when creation and rendering tools are available.
- Draw.io is an optional companion for precise editable geometry and formal handoff.
- Excalidraw is an optional companion for workshops and conceptual explanation.

Do not assume a companion is installed. Do not install one without explicit authorization. Preserve a textual equivalent even when a visual is created.

## Language and RTL

Keep the surrounding explanation in the user's language. For Persian or another RTL language:

- use a readable RTL textual structure as the safe baseline;
- keep human-facing labels in the user's language when the renderer handles them well;
- allow English technical labels or IDs when RTL rendering would reduce clarity or reliability;
- explain the language choice once rather than apologizing throughout the artifact.

## Visual encoding

- Give the view a title, IA question, scope, status, and legend when needed.
- Keep abstraction levels consistent.
- Label relationship direction and meaning; avoid vague edges.
- Use containment only for real ownership, scope, or grouping.
- Never rely on color alone.
- Keep labels concise and specific.
- Use whitespace and scale to establish hierarchy.
- Encode evidence status redundantly when it matters, such as border style plus a text label.

## Render and inspect

When rendering tools are available:

1. generate editable source;
2. render the requested output;
3. inspect the actual result;
4. fix clipping, overlap, crossings, ambiguity, imbalance, and unreadable text;
5. preserve the source beside the final export.

If rendering is unavailable, say that the source was reviewed or syntax-checked but not visually verified. Never claim visual QA without inspecting the render.

## Accessibility

Provide a concise textual equivalent covering the important nodes, relationships, exceptions, and evidence state. Use accessible titles and descriptions where supported. Readability at the target size matters more than zoomability.
