from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"


class SkillScriptTests(unittest.TestCase):
    def run_script(self, name: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPTS / name), *args], cwd=ROOT, text=True, capture_output=True, check=False)

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
            result = self.run_script("render_ia_html.py", str(FIXTURES / "valid-semantic-ia.json"), "-o", str(output))
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            rendered = output.read_text(encoding="utf-8")
            self.assertIn('<html lang="en" dir="ltr">', rendered)
            self.assertIn("Team Knowledge Product", rendered)
            self.assertIn("Projects reference working documents", rendered)
            self.assertIn("Information structure", rendered)
            self.assertNotIn("status-proposed", rendered)

    def test_universal_web_distribution_is_self_contained(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            universal = Path(directory) / "universal.md"
            claude_zip = Path(directory) / "claude.zip"
            result = self.run_script("package_distributions.py", "--root", str(ROOT), "--universal-output", str(universal), "--claude-output", str(claude_zip))
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            packaged = universal.read_text(encoding="utf-8")
            self.assertIn("Operating instruction for the assistant", packaged)
            self.assertIn("autonomous stop gate", packaged.lower())
            self.assertIn("source: references/figma-make-export.md", packaged)
            self.assertIn("Figma Make is the renderer", packaged)
            self.assertNotIn("](references/", packaged)

    def test_generated_distributions_are_current(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            universal = Path(directory) / "universal.md"
            claude_zip = Path(directory) / "claude.zip"
            result = self.run_script("package_distributions.py", "--root", str(ROOT), "--universal-output", str(universal), "--claude-output", str(claude_zip))
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            self.assertEqual(universal.read_bytes(), (ROOT / "install" / "universal-web" / "propaymun-information-architecture.md").read_bytes())
            self.assertEqual(claude_zip.read_bytes(), (ROOT / "install" / "claude-ai" / "propaymun-information-architecture.zip").read_bytes())

    def test_claude_zip_has_skill_folder_and_resources(self) -> None:
        archive_path = ROOT / "install" / "claude-ai" / "propaymun-information-architecture.zip"
        with zipfile.ZipFile(archive_path) as archive:
            names = set(archive.namelist())
            base = "propaymun-information-architecture/"
            self.assertIn(base + "SKILL.md", names)
            self.assertIn(base + "references/discovery.md", names)
            self.assertIn(base + "assets/semantic-ia.schema.json", names)
            self.assertNotIn(base + "tests/test_scripts.py", names)

    def test_figma_prompt_export_is_model_bound(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "figma-prompt.md"
            result = self.run_script("export_figma_make_prompt.py", str(FIXTURES / "valid-semantic-ia.json"), "-o", str(output))
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            prompt = output.read_text(encoding="utf-8")
            self.assertIn("Team Knowledge Product", prompt)
            self.assertIn("projects → documents [references]", prompt)
            self.assertIn("source of truth", prompt)
            self.assertIn("Do not create a sitemap, user flow", prompt)
            self.assertIn("Do not redesign", prompt)

    def test_release_version_is_consistent(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        manifest = json.loads((ROOT / "adapters" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(version, "0.3.0")
        self.assertIn(f'version: "{version}"', skill)
        self.assertIn(f'version-{version}-', readme)
        self.assertEqual(manifest["version"], version)

    def test_core_scope_routes_neighboring_maps_without_producing_them(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(skill, re.compile(r"sitemap.*page/destination", flags=re.IGNORECASE))
        self.assertRegex(skill, re.compile(r"user flow.*action/state", flags=re.IGNORECASE))
        self.assertIn("do not create either one", skill)
        self.assertIn("hierarchical, connected structural view", skill)

    def test_autonomous_stop_is_in_core_and_universal(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        universal = (ROOT / "install" / "universal-web" / "propaymun-information-architecture.md").read_text(encoding="utf-8")
        self.assertIn("autonomous stop gate", skill.lower())
        self.assertIn("hard stop", skill.lower())
        self.assertIn("autonomous stop gate", universal.lower())

    def test_figma_is_downstream_not_runtime(self) -> None:
        manifest = json.loads((ROOT / "adapters" / "manifest.json").read_text(encoding="utf-8"))
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("figma_make", manifest["surfaces"])
        self.assertEqual(manifest["downstream_exports"]["figma_make"]["type"], "post-approval-prompt")
        self.assertIn("Do not use Figma Make", skill)
        legacy = ROOT / "adapters" / "figma-make"
        self.assertFalse(legacy.exists() and any(legacy.iterdir()))

    def test_capability_routing_does_not_require_diagram_companions(self) -> None:
        routing = (ROOT / "references" / "capability-routing.md").read_text(encoding="utf-8")
        self.assertIn("Route by capability, not brand", routing)
        self.assertIn("complete fallback", routing)
        self.assertIn("Do not require either companion", routing)


if __name__ == "__main__":
    unittest.main()
