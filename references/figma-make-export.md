# Figma Make downstream prompt

Read this reference only after the user asks to turn a sufficiently stable IA into a Figma Make prompt.

## Boundary

Figma Make is the renderer and review surface, not the information architect. Do not send an incomplete brief and ask it to discover, infer, or redesign the IA. If a material unknown remains, resolve it in the current conversation first.

## Prompt contents

Create one self-contained prompt containing:

1. the purpose, review audience, scope, language, and writing direction;
2. the approved information domains and parent-child hierarchy;
3. important objects/content types and concise definitions;
4. labeled typed cross-relationships not expressible by the hierarchy;
5. relevant roles, visibility, ownership, lifecycle, taxonomy, labels, metadata, navigation, search, entry, orientation, and recovery;
6. consequential decisions and uncertainty, using plain language;
7. explicit exclusions: no product UI, sitemap, user flow, API, or database schema;
8. visual and interaction requirements;
9. acceptance checks.

## Required visual behavior

- The first view is a connected information architecture, not a dashboard of IA terminology.
- Show the primary hierarchy clearly and keep abstraction levels consistent.
- Use labeled connections for important cross-domain relationships.
- Put definitions, attributes, permissions, evidence, and decisions behind selection, expansion, filters, or focused secondary views.
- Provide an overview before detail and preserve a readable text equivalent.
- Use the user's language. For RTL, implement actual RTL layout; concise English technical IDs are allowed when they prevent rendering ambiguity.
- Keep visual style quiet and legible. Color supports grouping or state but never carries meaning alone.

## Guardrails for the target

Tell Figma Make:

- do not add, remove, merge, or reinterpret IA elements;
- do not convert objects into screens or relationships into click sequences;
- do not invent research, approval, rules, permissions, or validation;
- display supplied uncertainty as review notes, not as noisy badges on every item;
- if the supplied model is internally inconsistent, report the conflict instead of silently repairing it.

## Acceptance checks

The output passes only if a non-specialist can identify the main information domains, hierarchy, important connections, access distinctions, and unresolved decision without reading every detail. Every rendered element must trace to the supplied IA model.
