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
        self.assertEqual(version, "0.2.0")
        self.assertIn(f'version: "{version}"', skill)
        self.assertIn(f'version-{version}-', readme)

    def test_core_scope_excludes_neighboring_map_deliverables(self) -> None:
        paths = [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        self.assertIsNone(re.search(r"site\s*map|user\s*flow", combined, flags=re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
