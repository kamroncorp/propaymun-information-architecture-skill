# IA diagramming

Read this reference whenever visual output is requested or generated.

## Start from semantics

Define nodes, relationship types, direction, groups, states, evidence status, and view scope before choosing coordinates or colors.

Use this model:

`Truth model → Viewpoint → Visual encoding → Deliverable`

## Split views by question

Do not force all IA into one canvas. Typical views:

- domain/object relationship map;
- taxonomy or classification map;
- destination hierarchy/sitemap;
- navigation and cross-link map;
- search/facet model;
- roles and permissions matrix/map;
- current versus proposed comparison.

Keep behavioral user flows separate unless showing one example path is necessary to validate the IA.

## Default routing

When the user does not specify a format, provide Markdown plus Mermaid. Choose:

- `flowchart` for hierarchy, object relationships, and navigation maps;
- `classDiagram` or `erDiagram` when formal object/data relationships matter;
- multiple small diagrams rather than one crowded graph.

Recommend Draw.io for editable formal handoff, custom icons, swimlanes, exact routing, and multi-page diagrams. Recommend Excalidraw for workshops and teaching-oriented narratives. Use HTML for a shareable standalone artifact or interactive exploration.

## Visual encoding

- Give every diagram a title, type, scope, status, and legend.
- Keep abstraction levels consistent within a view.
- Label relationship direction and meaning; avoid generic “uses.”
- Use containment only for real ownership, scope, or grouping.
- Use color consistently and never as the only carrier of meaning.
- Keep labels concise but specific and audience-appropriate.
- Route edges around unrelated nodes and labels.
- Use whitespace and scale to establish hierarchy.
- Adapt flow direction to language and audience; do not assume LTR for Persian.

## Evidence display

When helpful, encode evidence status with a redundant combination of label/pattern and color, for example:

- solid border + `Confirmed`;
- ordinary border + `Proposed`;
- dashed border + `Inferred`;
- dotted placeholder + `Unknown`.

Always include a legend.

## Render and inspect

When rendering tools are available:

1. generate editable source;
2. render to SVG or PNG;
3. inspect the actual image;
4. fix clipping, overlap, crossings, ambiguity, imbalance, and unreadable text;
5. re-render until the view is usable;
6. preserve source alongside the final export.

If rendering is unavailable, state that the source was syntax-checked or reviewed but not visually verified.

## Accessibility

Provide a concise textual equivalent that conveys nodes, hierarchy, important relationships, exceptions, and status. For SVG/Mermaid, add an accessible title and description when supported. Check the target output size; zoom is not a substitute for readable defaults.

