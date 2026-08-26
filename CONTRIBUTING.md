# Contributing

Thanks for helping improve ProPaymun Information Architecture.

## Principles

- Preserve user intent and flexible output selection.
- Add rules only when they improve real decisions or prevent demonstrated failure.
- Separate evidence from heuristics and proposed conventions.
- Do not turn one product, language, user group, or test result into a universal IA rule.
- Keep `SKILL.md` concise; route conditional detail to focused references.
- Keep the Figma adapter generated from canonical sources rather than editing it independently.

## Workflow

1. Create a focused branch.
2. Update canonical files in `SKILL.md`, `references/`, `assets/`, or `scripts/`.
3. Rebuild the Figma adapter with `python scripts/package_figma.py`.
4. Run `python -m unittest discover -s tests -v`.
5. Run the Agent Skill quick validator.
6. Add or refine an eval case when behavior changes.
7. Explain the user-observable improvement in the pull request.

Avoid tests that require exact prose. Test decisions, evidence handling, output selection, schema validity, and artifact usability.

