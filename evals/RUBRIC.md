# Behavioral evaluation rubric

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| IA-only scope | Produces unrelated mapping work | Some scope drift | Stays entirely within the requested IA work |
| Interaction timing | Produces the full result before critical questions | Questions and production overlap | Questions and checkpoints precede consequential architecture decisions |
| IA depth | Treats IA as visible navigation only | Partial systems view | Models objects, organization, labels, retrieval, access, and governance as relevant |
| Evidence integrity | Fabricates or overclaims | Some ambiguity | Separates facts, inferences, proposals, and unknowns |
| Human clarity | Jargon-heavy or template-driven | Mostly understandable | Decision-first, audience-aware, and clear without prior IA knowledge |
| User effort | Requires knowledge of modes, checkpoints, or prompting tricks | Some unnecessary process burden | User can speak naturally while the skill carries the method and pause logic |
| Autonomous stop | Builds despite material unknowns | Pauses inconsistently | Asks only material questions, makes no mutation, and ends the turn automatically |
| User control | Forces mode, depth, or format | Allows some overrides | Adapts process and uses the correct default artifact for the environment |
| Capability awareness | Claims unavailable work | Mentions limitations late | Detects capabilities and offers only truthful options and fallbacks |
| Environment fit | Uses one output contract everywhere | Minor adaptation | Uses chat-first or build-first behavior while preserving the same IA quality contract |
| Alternative quality | Cosmetic variants | Some structural difference | Distinct organizing principles with explicit trade-offs |
| Validation fit | Generic or invented thresholds | Reasonable method | Method and decision rule directly match the claim and evidence |
| Optional visual quality | Unsolicited or misleading visual | Understandable | Requested IA-only view, textual equivalent, editable source, and honest QA state |

A release candidate should score at least 20/24 on every case, with no zero in IA-only scope, Interaction timing, Autonomous stop, Evidence integrity, User effort, or User control.
