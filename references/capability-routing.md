# Capability-aware execution and output routing

Read this reference when adapting the same IA work to different agents, chat surfaces, build environments, or installed tools.

## Route by capability, not brand

Product names are hints, not guarantees. Before choosing behavior or format, inspect the actual capabilities available in the current session:

- Can the agent ask a question, end the turn, and continue from the answer?
- Can it inspect attachments, URLs, repositories, or authorized connected sources?
- Can it search the public web without exposing private context?
- Can it create files or execute code?
- Can it render Mermaid reliably in the user's language and direction?
- Can it create a native document, artifact, app, canvas, or diagram?
- Can the result be visually inspected rather than merely generated?
- Is a diagram companion installed and authorized?

Never claim a capability from the model name alone. If an important capability is absent, use the strongest truthful fallback.

## Shared behavioral invariant

Every surface uses the same intake gate and semantic IA model. Environment adaptation changes interaction pacing and rendering, not architecture quality, evidence standards, or IA scope.

## Output ladder

### Level 0 — portable text

Use in any environment. Include:

- the architecture recommendation in plain language;
- an indented hierarchy of information domains and important objects/content;
- a concise list of typed cross-relationships that the tree cannot express;
- findability, access, and consequential uncertainty only where relevant.

This is a complete fallback, not an apology or a placeholder.

### Level 1 — structured text

Use Markdown tables or Mermaid only when they improve comprehension. Preserve a textual equivalent. For unreliable RTL rendering, keep the explanation and hierarchy in the user's language and use concise English technical IDs only where they improve renderer reliability.

### Level 2 — native artifact

Use a document, interactive HTML, artifact, canvas, or generated app when the environment supports it and the user requested a durable artifact or the surface is inherently build-first. The artifact must render the canonical semantic model rather than invent a new structure.

### Level 3 — professional diagram

Use a native diagram tool or an optional companion when precise geometry, editable connectors, workshop facilitation, or formal handoff justifies it. Draw.io suits precise editable handoff; Excalidraw suits conceptual explanation and workshops. Do not require either companion for a complete IA and do not install one without authorization.

## Surface profiles

### Conversation-first chat

Default to Level 0. Ask before creating a heavy file or visual. If the user requests a richer output, select the highest available truthful level.

### Chat with artifact or canvas capability

Keep intake conversational. After sufficiency, use Level 2 when an interactive or durable view materially improves review. Do not skip clarification merely because a canvas is available.

### CLI or agent with files and code execution

May produce and validate structured IA JSON, HTML, SVG, or other editable sources. Run and inspect deterministic helpers when available. Distinguish syntax validation from visual inspection.

### Build-first surface

Ask material questions before any mutation. Once sufficient, build a Level 2 architecture-first artifact whose primary surface shows hierarchy and connections. Avoid a generic dashboard, document reader, or product prototype.

### Diagram-capable surface

Use Level 3 only when the requested IA question benefits from a diagram. Keep the diagram scoped and preserve text for accessibility and portability.

## Research routing

Use web or connected sources when they can materially change terminology, domain rules, compliance, content inventory, or current-state understanding. Do not turn missing search capability into fabricated evidence. A build surface may be able to create visuals but lack reliable browsing; these capabilities must be judged separately.
