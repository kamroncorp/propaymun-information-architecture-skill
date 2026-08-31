# Visual Builder Handoff

Read this reference only after the user asks to turn an IA into a build specification for Figma Make, Lovable, or another prompt-to-build surface.

## Boundary and readiness gate

The target builder is a renderer and review surface, not the information architect. Before exporting, rerun the adaptive sufficiency gate.

- If a material unknown blocks the intended output, ask the smallest necessary question and stop.
- If the user explicitly wants a provisional workshop artifact, export it with `Proposed` status and keep consequential unknowns visible.
- Never ask the builder to discover, infer, localize, or repair the IA.

## Deliver two artifacts

Always give the user both:

1. a self-contained Markdown build specification;
2. a short copy-ready launch instruction for the builder's text box.

Long prompts are often attached as files and do not activate the builder's Generate button. The launch instruction solves that without duplicating the specification.

Recommended English launch instruction:

> Read the attached Markdown file as the complete build specification. Build the first version exactly from it; do not redesign the information architecture or invent missing information.

Recommended Persian launch instruction:

> فایل Markdown پیوست‌شده را به‌عنوان مشخصات کامل ساخت بخوان و نسخه اولیه را دقیقاً براساس آن بساز؛ معماری اطلاعات را تغییر نده و اطلاعات جدید اختراع نکن.

Adapt this single sentence to the user's language and target tool. Keep it short.

## Specification contents

Include:

1. purpose, review audience, scope, readiness, language, writing direction, and relevant locale context;
2. every information domain and the items assigned to it;
3. the parent-child hierarchy within and across domains;
4. important objects/content types with concise definitions;
5. labeled typed cross-relationships that hierarchy cannot express;
6. relevant roles, visibility, ownership, lifecycle, taxonomy, labels, metadata, navigation, search, entry, orientation, and recovery;
7. consequential decisions, assumptions, conflicts, and unknowns in plain language;
8. hard exclusions, visual behavior, and acceptance checks;
9. the canonical semantic IA JSON as the source of truth.

## Required primary view

- Show all information domains as clearly labeled containers or regions.
- Place every visible item inside its assigned domain.
- Show containment with a continuous hierarchy connector and cross-domain relationships with labeled connectors.
- Fit the graph to the available viewport; the architecture should occupy roughly two-thirds or more of the primary canvas without clipping.
- Use readable item cards, a practical minimum body size, accessible contrast, and generous but not wasteful spacing.
- Hide technical IDs by default; expose them only in an optional inspect/detail state.
- Keep relationship labels legible and make direction understandable without relying on color.
- Put roles/access, lifecycle, assumptions, unknowns, decisions, and technical detail in a secondary panel or progressive disclosure.
- Provide a compact readable legend and a plain-text equivalent of hierarchy and relationships.

The connected architecture is the first view. A tabbed dashboard, card catalogue, or specialist review explorer must not replace it.

## Guardrails for the target

Tell the builder:

- do not add, remove, merge, or reinterpret IA elements;
- do not convert objects into screens or relationships into click sequences;
- do not create a sitemap, user flow, wireframe, product prototype, API, or database schema;
- do not invent research, approvals, local rules, permissions, relationships, or validation;
- show supplied uncertainty as review notes rather than noisy badges on every item;
- show a concise conflict notice instead of silently repairing inconsistent source data;
- do not ask product-discovery questions inside the built artifact.

## Acceptance checks

The handoff passes only if:

- a non-specialist can identify the domains, hierarchy, and important connections from the first view;
- every visible item is mapped to a domain and traceable to the canonical model;
- important access distinctions and consequential uncertainty are understandable without reading every detail;
- technical detail supports the architecture instead of displacing it;
- the layout remains readable in the target viewport and writing direction.
