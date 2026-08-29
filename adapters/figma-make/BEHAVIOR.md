# Figma Make execution profile

These instructions specialize the canonical skill for Figma Make. They override a generic chat-first delivery default where they differ, but never override the IA scope, evidence, privacy, or autonomous-stop rules.

## Treat chat as the control plane

Figma Make is build-oriented, but it can converse before building. The user should need only to invoke the skill and describe or attach their product context.

### Hard pre-build gate

Before changing code, preview, canvas, files, or components, run the canonical sufficiency gate.

If a material unknown remains, the response in that turn must contain only:

1. a short plain-language understanding of the brief;
2. the smallest set of product questions needed to unblock the architecture, normally no more than five.

Then end the response. Do not create a placeholder, plan file, loading screen, partial app, component, diagram, or IA draft. Do not require the user to say “stop,” enable Plan mode, or know how the skill works.

If the user's next answer resolves the material unknowns, continue automatically. If they do not know, apply a defensible proposed default unless it would be unsafe or misleading.

## Use native build capability after sufficiency

Once the IA is sufficiently framed, build an interactive **IA Structure Explorer** directly. Do not ask the user to choose Markdown, chat, or another output format first.

### Primary surface: the connected architecture

The first and dominant view must communicate the architecture itself:

- information domains at the first meaningful level;
- important concepts, objects, and content types nested beneath them;
- containment or classification through visible hierarchy;
- important non-hierarchical relationships through labeled connectors;
- concise findability cues showing how people browse, search, enter, orient, and recover.

Keep node abstraction consistent. Nodes are not product screens, URLs, menu items, database tables, or user-flow steps. A hierarchical IA structure view is allowed and expected; a page-level sitemap is not.

Use a clear overview first, then progressive detail. When the architecture is large, provide an overview map plus focused domain views rather than one giant graph. Selecting a node or relationship may reveal purpose, attributes, rules, roles, lifecycle, labels, evidence, and decisions in a contextual detail panel.

### Supporting views

Add only the focused views needed to answer real IA questions, such as:

- organization, taxonomy, label, and metadata rules;
- navigation and search systems;
- roles, visibility, permissions, ownership, and lifecycle;
- consequential decisions, assumptions, unknowns, risks, and validation.

These are supporting views, not equal-weight dashboard tabs. Tables and card collections may support detail, but must not replace the connected hierarchy as the main representation.

Keep evidence states in the underlying model. In the primary view, show them only when they change interpretation and use plain-language wording. Do not cover nodes with unexplained “confirmed,” “proposed,” or “unknown” badges.

Use accessible, restrained visual design; responsive layout; the user's language and writing direction; semantic HTML; keyboard-usable controls; and text equivalents for essential visual relationships. Avoid ornamental dashboards, fake analytics, invented product screenshots, arbitrary metrics, and unnecessary imagery.

Do not build:

- the product UI, screens, wireframes, or interactive product prototype;
- a sitemap, user flow, journey map, service blueprint, API, or data schema;
- unrelated “next phase” features.

After the explorer is built, summarize the architecture decisions and material uncertainty in plain language. Offer only alternate formats of the same IA if the user asks; do not advertise neighboring skills or deliverables.

## Web and connected context

Use live web search or URL fetching when available and materially useful under the canonical research rules. Figma Make's capability may vary by model, plan, file permissions, organization settings, and connectors; detect availability rather than promising it.

- Search public sources without exposing private brief content.
- Use authorized connectors for private documents.
- Cite sources in the workspace or accompanying response.
- If search is unavailable, say so briefly and proceed with explicit evidence limits when safe.

## Credit-aware behavior

Avoid repeated ceremonial checkpoints, duplicate context, and speculative builds. One useful clarification round plus one well-scoped build is preferable when the product allows it. Plan mode may help when available, but correct behavior must not depend on it.
