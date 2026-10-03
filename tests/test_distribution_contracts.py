import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HQ = ROOT / "templates/Agent HQ"


class DistributionContractTests(unittest.TestCase):
    def test_frozen_legacy_references_and_public_skill_names_preserved(self):
        manifest = json.loads((ROOT / "examples/legacy-workflow-manifest.json").read_text())
        self.assertEqual(manifest["public_skill_names"], sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")))
        for relative, expected in manifest["files"].items():
            with self.subTest(path=relative):
                self.assertEqual(expected, hashlib.sha256((ROOT / relative).read_bytes()).hexdigest())

    def test_selected_workflow_routes_resolve_without_bulk_legacy_loads(self):
        names = ["Daily Glide Check-In", "Nightly Research Review", "Area Review",
                 "Life Systems Review", "Contradiction Review", "WOOP Goal Review",
                 "Decision Packet", "Update User Profile", "Harness Drift Review",
                 "Eval Loop", "Weekly Review", "Monthly Review"]
        for name in names:
            text = (HQ / "Checklists" / (name + ".md")).read_text()
            with self.subTest(workflow=name):
                reference = "Reference/Legacy Workflows/" + name + ".md"
                self.assertIn(reference, text)
                self.assertTrue((HQ / reference).is_file())
                self.assertNotIn("Evals/*.md", text)
                self.assertNotIn("Areas/*/Reminders.md", text)
        # Default execution must route to owned checklists, rather than a second
        # copy of source selection/update rules in every harness prompt.
        routes = {
            "DAILY_GLIDE_CHECK_IN.md": "glide-daily-check-in",
            "NIGHTLY_RESEARCH_REVIEW.md": "glide-nightly-research-review",
            "HARNESS_DRIFT_REVIEW.md": "glide-harness-drift-review",
        }
        for harness in ["codex", "claude-code", "generic"]:
            for file, skill in routes.items():
                text = (ROOT / "adapters" / harness / file).read_text()
                self.assertIn("$" + skill, text)
                self.assertNotIn("Follow-Through Ledger.md", text)
                self.assertNotIn("Evals/*.md", text)

    def test_active_skill_and_workflow_path_references_resolve(self):
        paths = list((ROOT / "skills").glob("*/SKILL.md")) + list((HQ / "Checklists").glob("*.md")) + [HQ / "AGENTS.md", HQ / "Memory Protocol.md"]
        for path in paths:
            if path.name == "SKILL.md":
                text = path.read_text()
                self.assertRegex(text, r"(?m)^name: " + re.escape(path.parent.name) + r"$")
                self.assertRegex(text, r"(?m)^description: .+")
            for ref in re.findall(r"`([^`]+[.]md)`", path.read_text()):
                if any(c in ref for c in ["*", "<", ">", "$"]):
                    continue
                if ref.startswith("docs/"):
                    target = ROOT / ref
                elif ref.startswith("Agent HQ/"):
                    target = ROOT / "templates" / ref
                else:
                    candidates = [HQ / ref, path.parent / ref, HQ / "Checklists" / ref, HQ / "Evals" / ref]
                    if path.parent.name == "glide-create-area":
                        candidates.append(HQ / "Areas/Finance" / ref)  # Standard area scaffold exemplar.
                    target = next((candidate for candidate in candidates if candidate.is_file()), candidates[0])
                with self.subTest(source=str(path.relative_to(ROOT)), reference=ref):
                    self.assertTrue(target.is_file(), str(target))

    def test_generated_contract_identity_and_synthetic_pin(self):
        for name in ["Memory Core.md", "Recovery Core.md"]:
            text = (HQ / "Contracts" / name).read_text()
            self.assertIn("generated", text.lower())
            self.assertNotIn("{{HQ}}", text)
        compat = json.loads((ROOT / "compatibility.json").read_text())["optional_memory_runtime"]
        example = json.loads((ROOT / "examples/install-manifest.example.json").read_text())["runtime"]
        self.assertEqual((compat["version"], compat["build"]), (example["version"], example["build"]))


if __name__ == "__main__":
    unittest.main()
