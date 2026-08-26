#!/usr/bin/env python3
"""Build the single-file Figma Make adapter from the canonical skill sources."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REFERENCE_ORDER = [
    "ia-foundations.md",
    "discovery.md",
    "modeling.md",
    "evidence.md",
    "validation.md",
    "deliverables.md",
    "diagramming.md",
]

FIGMA_PROFILE = Path("adapters") / "figma-make" / "BEHAVIOR.md"


def demote_headings(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.startswith("#"):
            line = "##" + line
        lines.append(line)
    return "\n".join(lines).strip()


def rewrite_reference_links(text: str) -> str:
    """Replace modular reference links that cannot resolve in Figma uploads."""
    return re.sub(
        r"\[([^\]]+)\]\(references/[^)]+\)",
        r"\1 (embedded below)",
        text,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output or root / "adapters" / "figma-make" / "propaymun-information-architecture.md"

    skill = rewrite_reference_links(
        (root / "SKILL.md").read_text(encoding="utf-8").rstrip()
    )
    figma_profile = demote_headings(
        (root / FIGMA_PROFILE).read_text(encoding="utf-8")
    )
    sections = [
        skill,
        f"\n---\n\n<!-- source: {FIGMA_PROFILE.as_posix()} -->\n\n{figma_profile}\n",
        "\n---\n\n# Embedded references\n",
    ]
    for name in REFERENCE_ORDER:
        path = root / "references" / name
        sections.append(f"\n<!-- source: references/{name} -->\n\n{demote_headings(path.read_text(encoding='utf-8'))}\n")
    sections.append(
        "\n---\n\nThis is the Figma single-file adapter. The canonical modular source is the GitHub repository.\n"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(sections), encoding="utf-8", newline="\n")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
