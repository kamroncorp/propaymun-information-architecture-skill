from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"


class SkillScriptTests(unittest.TestCase):
    def run_script(self, name: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPTS / name), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_valid_model_passes(self) -> None:
        result = self.run_script("validate_ia_model.py", str(FIXTURES / "valid-semantic-ia.json"), "--json")
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertTrue(json.loads(result.stdout)["valid"])

    def test_invalid_model_fails(self) -> None:
        result = self.run_script("validate_ia_model.py", str(FIXTURES / "invalid-semantic-ia.json"), "--json")
        self.assertEqual(result.returncode, 1)
        self.assertFalse(json.loads(result.stdout)["valid"])

    def test_html_renderer_outputs_rtl_aware_document(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "ia.html"
            result = self.run_script(
                "render_ia_html.py",
                str(FIXTURES / "valid-semantic-ia.json"),
                "-o",
                str(output),
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            rendered = output.read_text(encoding="utf-8")
            self.assertIn('<html lang="en" dir="ltr">', rendered)
            self.assertIn("Team Knowledge Product", rendered)
            self.assertIn("Project documents", rendered)

    def test_figma_adapter_contains_embedded_references(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "figma.md"
            result = self.run_script("package_figma.py", "--root", str(ROOT), "--output", str(output))
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            packaged = output.read_text(encoding="utf-8")
            self.assertIn("name: propaymun-information-architecture", packaged)
            self.assertIn("Embedded references", packaged)
            self.assertIn("source: adapters/figma-make/BEHAVIOR.md", packaged)
            self.assertIn("Hard pre-build gate", packaged)
            self.assertIn("IA Review Workspace", packaged)
            self.assertIn("source: references/diagramming.md", packaged)
            self.assertNotIn("](references/", packaged)

    def test_figma_adapter_is_current(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "figma.md"
            result = self.run_script("package_figma.py", "--root", str(ROOT), "--output", str(output))
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            committed = ROOT / "adapters" / "figma-make" / "propaymun-information-architecture.md"
            self.assertEqual(output.read_bytes(), committed.read_bytes())

    def test_release_version_is_consistent(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        manifest = json.loads((ROOT / "adapters" / "manifest.json").read_text(encoding="utf-8"))
        figma = (ROOT / "adapters" / "figma-make" / "propaymun-information-architecture.md").read_text(encoding="utf-8")
        self.assertEqual(version, "0.3.0")
        self.assertIn(f'version: "{version}"', skill)
        self.assertIn(f'version-{version}-', readme)
        self.assertEqual(manifest["version"], version)
        self.assertIn(f'version: "{version}"', figma)

    def test_core_scope_routes_neighboring_map_deliverables_without_producing_them(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(skill, re.compile(r"sitemap.*separate", flags=re.IGNORECASE))
        self.assertRegex(skill, re.compile(r"user flow.*separate", flags=re.IGNORECASE))
        self.assertIn("do not create or offer either one", skill)

    def test_autonomous_stop_is_shared_by_core_and_figma(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        figma_profile = (ROOT / "adapters" / "figma-make" / "BEHAVIOR.md").read_text(encoding="utf-8")
        self.assertIn("autonomous stop gate", skill.lower())
        self.assertIn("hard stop", skill.lower())
        self.assertIn("hard pre-build gate", figma_profile.lower())
        self.assertIn("do not require the user to say", figma_profile.lower())


if __name__ == "__main__":
    unittest.main()
