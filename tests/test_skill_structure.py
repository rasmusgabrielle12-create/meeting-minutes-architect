from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skill/meeting-minutes-architect"


class SkillStructureTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [
            "SKILL.md",
            "agents/openai.yaml",
            "assets/minutes-template.md",
            "references/evidence-policy.md",
            "references/meeting-type-playbook.md",
            "references/output-contract.md",
            "references/examples.md",
            "scripts/validate_minutes.py",
        ]
        for relative in required:
            self.assertTrue((SKILL_ROOT / relative).is_file(), relative)

    def test_frontmatter_has_only_required_keys(self) -> None:
        content = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        self.assertIsNotNone(match)
        keys = {
            line.split(":", 1)[0].strip()
            for line in match.group(1).splitlines()
            if ":" in line
        }
        self.assertEqual({"name", "description"}, keys)

    def test_skill_name_matches_directory(self) -> None:
        content = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: meeting-minutes-architect", content)
        self.assertEqual("meeting-minutes-architect", SKILL_ROOT.name)

    def test_skill_body_stays_compact(self) -> None:
        lines = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertLess(len(lines), 500)


if __name__ == "__main__":
    unittest.main()
