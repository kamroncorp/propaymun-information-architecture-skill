#!/usr/bin/env python3
"""Build the Universal Web file and the Claude.ai upload ZIP."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path


REFERENCE_ORDER = [
    "ia-foundations.md",
    "discovery.md",
    "modeling.md",
    "capability-routing.md",
    "evidence.md",
    "validation.md",
    "deliverables.md",
    "diagramming.md",
    "figma-make-export.md",
]

PACKAGE_FOLDER = "propaymun-information-architecture"
FIXED_ZIP_TIME = (2026, 1, 1, 0, 0, 0)


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)


def demote_headings(text: str) -> str:
    return "\n".join(("##" + line) if line.startswith("#") else line for line in text.splitlines()).strip()


def rewrite_reference_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\(references/[^)]+\)", r"\1 (embedded below)", text)


def build_universal(root: Path) -> str:
    skill = rewrite_reference_links(strip_frontmatter((root / "SKILL.md").read_text(encoding="utf-8")).strip())
    intro = """# ProPaymun Information Architecture — Universal Web

## Operating instruction for the assistant

When the user asks for information architecture work, follow this file as operating instructions, not merely as background reading. The user should only need to describe the product, task, or source material naturally. Apply the autonomous stop gate yourself, stay inside IA scope, and answer in the user's language.

This portable file is for web Projects, Gems, custom Agents, and file-capable chats that do not load a native `SKILL.md` package. Native Skill runtimes should use the repository package instead.
"""
    sections = [intro.strip(), "\n---\n", skill, "\n---\n\n# Embedded operating references\n"]
    for name in REFERENCE_ORDER:
        source = (root / "references" / name).read_text(encoding="utf-8")
        sections.append(f"\n<!-- source: references/{name} -->\n\n{demote_headings(source)}\n")
    sections.append("\n---\n\nCanonical source: https://github.com/kamroncorp/propaymun-information-architecture-skill\n")
    return "\n".join(sections).replace("\r\n", "\n")


def zip_write_text(archive: zipfile.ZipFile, arcname: str, data: bytes) -> None:
    info = zipfile.ZipInfo(arcname, FIXED_ZIP_TIME)
    info.create_system = 3
    # Stored entries avoid zlib-version differences between Windows packaging
    # and Linux CI, making the committed upload ZIP byte-for-byte reproducible.
    info.compress_type = zipfile.ZIP_STORED
    info.external_attr = 0o644 << 16
    archive.writestr(info, data)


def build_claude_zip(root: Path, output: Path) -> None:
    files = [root / "SKILL.md", root / "LICENSE"]
    files.extend(sorted((root / "references").glob("*.md")))
    files.extend(sorted((root / "assets").glob("*")))
    files.extend(sorted((root / "scripts").glob("*.py")))
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as archive:
        for path in files:
            if path.is_file():
                relative = path.relative_to(root).as_posix()
                zip_write_text(archive, f"{PACKAGE_FOLDER}/{relative}", path.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--universal-output", type=Path)
    parser.add_argument("--claude-output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    universal_output = args.universal_output or root / "install" / "universal-web" / "propaymun-information-architecture.md"
    claude_output = args.claude_output or root / "install" / "claude-ai" / "propaymun-information-architecture.zip"
    universal_output.parent.mkdir(parents=True, exist_ok=True)
    universal_output.write_text(build_universal(root), encoding="utf-8", newline="\n")
    build_claude_zip(root, claude_output)
    print(universal_output)
    print(claude_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
