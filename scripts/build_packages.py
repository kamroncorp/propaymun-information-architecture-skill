#!/usr/bin/env python3
"""Build the installable Agent Skill Package and portable Workspace Kit."""

from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from pathlib import Path


REFERENCE_ORDER = [
    "ia-foundations.md",
    "discovery.md",
    "localization.md",
    "modeling.md",
    "capability-routing.md",
    "evidence.md",
    "validation.md",
    "deliverables.md",
    "diagramming.md",
    "visual-builder-handoff.md",
]

PACKAGE_FOLDER = "propaymun-information-architecture"
FIXED_ZIP_TIME = (2026, 1, 1, 0, 0, 0)


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)


def demote_headings(text: str) -> str:
    return "\n".join(("##" + line) if line.startswith("#") else line for line in text.splitlines()).strip()


def rewrite_reference_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\(references/[^)]+\)", r"\1 (embedded below)", text)


def build_workspace_kit(root: Path) -> str:
    skill = rewrite_reference_links(strip_frontmatter((root / "SKILL.md").read_text(encoding="utf-8")).strip())
    intro = """# ProPaymun IA Workspace Kit

## Operating instruction for the assistant

When the user asks for information architecture work, follow this file as operating instructions rather than background reading. The user only needs to describe the product, task, or source material naturally. Run the adaptive sufficiency loop yourself, pause whenever a material answer is required, stay inside IA scope, localize only from evidence, and answer in the user's language.

This self-contained package is designed for Projects, Gems, custom agents, knowledge workspaces, and file-capable chats that do not load a native Agent Skill package.
"""
    sections = [intro.strip(), "\n---\n", skill, "\n---\n\n# Embedded operating references\n"]
    for name in REFERENCE_ORDER:
        source = (root / "references" / name).read_text(encoding="utf-8")
        sections.append(f"\n<!-- source: references/{name} -->\n\n{demote_headings(source)}\n")
    sections.append("\n---\n\nCanonical source: https://github.com/kamroncorp/propaymun-information-architecture-skill\n")
    return "\n".join(sections).replace("\r\n", "\n")


def zip_write(archive: zipfile.ZipFile, arcname: str, data: bytes) -> None:
    info = zipfile.ZipInfo(arcname, FIXED_ZIP_TIME)
    info.create_system = 3
    info.compress_type = zipfile.ZIP_STORED
    info.external_attr = 0o644 << 16
    archive.writestr(info, data)


def build_agent_skill(root: Path, output: Path) -> None:
    files = [root / "SKILL.md", root / "LICENSE"]
    files.extend(sorted((root / "references").glob("*.md")))
    files.extend(sorted((root / "schema").glob("*")))
    files.extend(sorted((root / "scripts").glob("*.py")))
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as archive:
        for path in files:
            if path.is_file():
                relative = path.relative_to(root).as_posix()
                zip_write(archive, f"{PACKAGE_FOLDER}/{relative}", path.read_bytes())


def copy_alias(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--workspace-output", type=Path)
    parser.add_argument("--agent-output", type=Path)
    parser.add_argument("--skip-legacy-aliases", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    workspace_output = args.workspace_output or root / "packages" / "workspace-kit" / "propaymun-ia-workspace-kit.md"
    agent_output = args.agent_output or root / "packages" / "agent-skill" / "propaymun-information-architecture.zip"

    workspace_output.parent.mkdir(parents=True, exist_ok=True)
    workspace_output.write_text(build_workspace_kit(root), encoding="utf-8", newline="\n")
    build_agent_skill(root, agent_output)

    if not args.skip_legacy_aliases:
        copy_alias(workspace_output, root / "install" / "universal-web" / "propaymun-information-architecture.md")
        copy_alias(root / "packages" / "workspace-kit" / "WORKSPACE_INSTRUCTIONS.md", root / "install" / "universal-web" / "PROJECT_INSTRUCTIONS.md")
        copy_alias(agent_output, root / "install" / "claude-ai" / "propaymun-information-architecture.zip")

    print(workspace_output)
    print(agent_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
