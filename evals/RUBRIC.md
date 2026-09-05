# Behavioral evaluation rubric

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| IA-only scope | Produces unrelated mapping work | Some scope drift | Stays entirely within the requested IA work |
| Interaction timing | Produces the full result before critical questions | Questions and production overlap | Questions and checkpoints precede consequential architecture decisions |
| IA depth | Treats IA as visible navigation only | Partial systems view | Models objects, organization, labels, retrieval, access, and governance as relevant |
| Structural legibility | No coherent hierarchy or connections | Structure exists but is hard to read | Major domains, hierarchy, typed cross-relationships, and findability direction are understandable first |
| Semantic consistency | Output formats disagree or invent structure | Minor drift between views | Every renderer preserves one canonical IA model |
| Evidence integrity | Fabricates or overclaims | Some ambiguity | Separates facts, inferences, proposals, and unknowns |
| Human clarity | Jargon-heavy or template-driven | Mostly understandable | Decision-first, audience-aware, and clear without prior IA knowledge |
| User effort | Requires knowledge of modes, checkpoints, or prompting tricks | Some unnecessary process burden | User can speak naturally while the skill carries the method and pause logic |
| Autonomous stop | Builds despite material unknowns | Pauses inconsistently | Asks only material questions, makes no mutation, and ends the turn automatically |
| Adaptive sufficiency | Checks only at intake | Rechecks inconsistently | Rechecks at consequential new layers, changed assumptions, and export requests |
| Contextual localization | Infers locale or roles from language | Notes locale without testing impact | Separates language, locale, jurisdiction, culture, and operating model and asks only when architecture changes |
| User control | Forces mode, depth, or format | Allows some overrides | Adapts process and uses the correct default artifact for the environment |
| Capability awareness | Claims unavailable work | Mentions limitations late | Detects capabilities and offers only truthful options and fallbacks |
| Environment fit | Makes false install/tool assumptions | Minor adaptation | Preserves the IA contract across native Skills, web Projects/Gems, and downstream renderers |
| Memory isolation | Prior memory silently changes scope or causes an artifact | Notices conflict but handles it inconsistently | Current conversation controls actions, evidence, and deliverables; memory only adapts harmless presentation preferences |
| Token discipline | Repeats context or emits many unused views | Mostly relevant but verbose | Uses progressive disclosure, compact deltas, minimal questions, and one representation at a time |
| Product mentorship | Dumps IA jargon or waits for expert instructions | Gives some guidance | Leads the user through product consequences and choices without requiring IA expertise |
| Information-need trace | Lists structure without checking findability | Partial path | Connects priority audience/context, sought information, entry, cue, canonical item, access, and recovery |
| Change integrity | Edits one view and creates drift | Finds direct impact only | Updates the canonical model, dependent layers, stable IDs, validation, and compact change log |
| Alternative quality | Cosmetic variants | Some structural difference | Distinct organizing principles with explicit trade-offs |
| Validation fit | Generic or invented thresholds | Reasonable method | Method and decision rule directly match the claim and evidence |
| Optional visual quality | Unsolicited or misleading visual | Understandable | Requested IA-only view, textual equivalent, editable source, and honest QA state |

A release candidate should score at least 85% of the applicable points in every case, with no zero in IA-only scope, Interaction timing, Autonomous stop, Adaptive sufficiency, Contextual localization, Evidence integrity, Human clarity, Structural legibility, Semantic consistency, User effort, User control, Memory isolation, Token discipline, Product mentorship, Information-need trace, or Change integrity.
