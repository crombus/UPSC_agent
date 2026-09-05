"""Focused tests for the full learner-v2 topic command catalogue."""

from __future__ import annotations

import json
import re
import shutil
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_v2_section_indexes as section_indexes
import generate_v2_topic_command_catalog as topic_catalog


class TopicCommandCatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = ROOT / "_test_v2_topic_command_catalog"
        shutil.rmtree(self.root, ignore_errors=True)
        subject = self.root / "upsc-ai-kit" / "knowledge" / "Test-Subject"
        (subject / "basic").mkdir(parents=True)
        (subject / "advanced").mkdir(parents=True)
        (subject / "basic" / "01_Planned-Topic.md").write_text(
            "# Planned Topic\n", encoding="utf-8"
        )
        (subject / "advanced" / "01_Planned-Topic-Depth.md").write_text(
            "# Planned Topic Advanced\n", encoding="utf-8"
        )
        (subject / "basic" / "02_Carvaka-Unicode.md").write_text(
            "# Cārvāka — Unicode\n", encoding="utf-8"
        )
        (subject / "advanced" / "02_Carvaka-Unicode-Depth.md").write_text(
            "# Cārvāka Advanced\n", encoding="utf-8"
        )
        (subject / "basic" / "03_Third-Topic.md").write_text(
            "# Third Topic\n", encoding="utf-8"
        )
        (subject / "00_Master-Framework.md").write_text(
            "# Not a topic\n", encoding="utf-8"
        )
        (subject / "ANSWER-WORTHINESS-AUDIT.md").write_text(
            "# Not a topic\n", encoding="utf-8"
        )
        (subject / "README.md").write_text(
            "# Test Subject\n\n"
            "### Part A — Foundations (Topics 01-02)\n\n"
            "| # | Topic |\n|---|---|\n"
            "| 01 | Planned Topic |\n"
            "| 02 | Cārvāka — Unicode |\n\n"
            "### Part B — Application (Topics 03-04)\n\n"
            "| # | Topic |\n|---|---|\n"
            "| 03 | Third Topic |\n"
            "| 04 | Missing Owner Topic |\n",
            encoding="utf-8",
        )
        (subject / "LEARNING-SESSION-COMMAND-INDEX.md").write_text(
            "# Commands\n\n"
            "| # | Topic | Start |\n|---|---|---|\n"
            "| 01 | **Planned Topic**<br>`basic/01_Planned-Topic.md` | `Start 01` |\n"
            "| 02 | **Cārvāka — Unicode**<br>`basic/02_Carvaka-Unicode.md` | `Start 02` |\n"
            "| 03 | **Third Topic**<br>`basic/03_Third-Topic.md` | `Start 03` |\n"
            "| 04 | **Missing Owner Topic** | `Start 04` |\n",
            encoding="utf-8",
        )
        export_lines = ["# Export index", ""]
        for number, title in (
            (1, "Planned Topic"),
            (2, "Cārvāka — Unicode"),
            (3, "Third Topic"),
            (4, "Missing Owner Topic"),
        ):
            export_lines.append(
                f"- [ ] ⬜ `Export PDF for Test Subject {number:02d} — {title}` "
                f"— `test-subject-{number:02d}`"
            )
        (self.root / "EXPORT-PDF-COMMAND-INDEX.md").write_text(
            "\n".join(export_lines) + "\n",
            encoding="utf-8",
        )
        (self.root / "EXPORT-PDF-STATUS.json").write_text(
            json.dumps(
                {
                    "schema_version": 2,
                    "exports": [
                        {
                            "record_id": "test-subject-02:learner-v2:g1",
                            "topic_key": "test-subject-02",
                            "variant": "learner-v2",
                            "generation": 1,
                            "approved": False,
                        }
                    ],
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        self.catalog = topic_catalog.build_catalog(
            self.root,
            subjects=[("Test-Subject", "Test Subject")],
            include_philosophy=False,
        )
        self.catalog_path = (
            self.root
            / "upsc-ai-kit"
            / "manifests"
            / "v2"
            / "topic-catalog.json"
        )
        self.catalog_path.parent.mkdir(parents=True)
        self.catalog_path.write_text(
            json.dumps(self.catalog, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def render(self) -> str:
        records = section_indexes.load_tracker(
            self.root / "EXPORT-PDF-STATUS.json"
        )
        return section_indexes.render_command_guide(
            self.root,
            [],
            records,
            self.catalog,
        )

    def test_basic_advanced_pair_counted_once_and_meta_excluded(self) -> None:
        self.assertEqual(4, self.catalog["statistics"]["topics"])
        keys = [topic["topic_key"] for topic in self.catalog["topics"]]
        self.assertEqual(
            [
                "test-subject-01",
                "test-subject-02",
                "test-subject-03",
                "test-subject-04",
            ],
            keys,
        )
        rendered = json.dumps(self.catalog, ensure_ascii=False)
        self.assertNotIn("00_Master-Framework", rendered)
        self.assertNotIn("ANSWER-WORTHINESS-AUDIT", rendered)

    def test_numbered_order_subject_section_grouping_and_unicode(self) -> None:
        guide = self.render()
        self.assertIn("## 1. Test Subject — 3 topics", guide)
        self.assertIn("### Part A — Foundations (`part-a-foundations`) — 2 topics", guide)
        self.assertIn("### Part B — Application (`part-b-application`) — 1 topics", guide)
        self.assertLess(guide.index("Planned Topic"), guide.index("Cārvāka — Unicode"))
        self.assertLess(guide.index("Cārvāka — Unicode"), guide.index("Third Topic"))

    def test_exact_commands_have_no_placeholders_and_state_suffix_is_exact(self) -> None:
        guide = self.render()
        blocks = re.findall(r"```text\n(.*?)\n```", guide, re.DOTALL)
        commands = [
            command
            for block in blocks
            for command in block.splitlines()
            if command.startswith("Generate learner-v2 topic: ")
        ]
        self.assertEqual(3, len(commands))
        self.assertTrue(
            all(command.startswith("Generate learner-v2 topic: ") for command in commands)
        )
        self.assertTrue(all("<" not in command and ">" not in command for command in commands))
        self.assertIn(
            "Generate learner-v2 topic: Test Subject — Part A — Foundations — "
            "Cārvāka — Unicode — Regenerate",
            commands,
        )
        self.assertIn(
            "Generate learner-v2 topic: Test Subject — Part A — Foundations — "
            "Planned Topic",
            commands,
        )
        self.assertNotIn(
            "Generate learner-v2 topic: Test Subject — Part A — Foundations — "
            "Planned Topic — Regenerate",
            commands,
        )
        self.assertIn(
            "Generate next 10 learner-v2 topics: Test Subject — Part A — Foundations",
            guide,
        )

    def test_unresolved_topic_is_withheld_and_reported(self) -> None:
        guide = self.render()
        self.assertNotIn(
            "Generate learner-v2 topic: Test Subject — Part B — Application — "
            "Missing Owner Topic\n",
            guide,
        )
        self.assertIn("`test-subject-04`", guide)
        self.assertIn("No usable canonical/basic/advanced Markdown owner", guide)

    def test_duplicate_topic_and_command_detection(self) -> None:
        duplicated = json.loads(json.dumps(self.catalog))
        duplicate = dict(duplicated["topics"][0])
        duplicate["topic_key"] = "test-subject-duplicate"
        duplicated["topics"].append(duplicate)
        with self.assertRaises(topic_catalog.CatalogError):
            topic_catalog.validate_catalog(self.root, duplicated)
        duplicated["topics"][-1]["learner_v2_command"] += " unique"
        duplicated["topics"][-1]["topic_key"] = duplicated["topics"][0]["topic_key"]
        with self.assertRaises(topic_catalog.CatalogError):
            topic_catalog.validate_catalog(self.root, duplicated)

    def test_all_declared_paths_exist_and_schema_parses(self) -> None:
        topic_catalog.validate_catalog(self.root, self.catalog)
        schema = json.loads(
            (
                ROOT
                / "upsc-ai-kit"
                / "manifests"
                / "v2"
                / "topic-catalog.schema.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(
            "Learner-v2 full topic command catalogue",
            schema["title"],
        )
        for topic in self.catalog["topics"]:
            for value in topic_catalog.declared_paths(topic):
                self.assertTrue(topic_catalog.repo_path(self.root, value).is_file())

    def test_generation_is_deterministic(self) -> None:
        first = json.dumps(self.catalog, ensure_ascii=False, indent=2) + "\n"
        second_catalog = topic_catalog.build_catalog(
            self.root,
            subjects=[("Test-Subject", "Test Subject")],
            include_philosophy=False,
        )
        second = json.dumps(second_catalog, ensure_ascii=False, indent=2) + "\n"
        self.assertEqual(first, second)
        self.assertEqual(self.render(), self.render())

    def test_on_demand_section_manifest_semantics_are_implemented_and_documented(
        self,
    ) -> None:
        command = (
            "Generate learner-v2 topic: Test Subject — Part A — Foundations — "
            "Planned Topic"
        )
        outputs = section_indexes.prepare_catalog_topic_command(
            self.root,
            command,
        )
        manifest_path = outputs["manifest"]
        self.assertTrue(manifest_path.is_file())
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual("part-a-foundations", manifest["section"]["key"])
        self.assertEqual(2, len(manifest["topics"]))
        self.assertIn("Materialised on demand", manifest["section"]["notes"])
        for name in ("coverage", "notes", "workbooks", "command_guide"):
            self.assertTrue(outputs[name].is_file())
        guide = outputs["command_guide"].read_text(encoding="utf-8")
        self.assertIn("materialises the complete section manifest", guide)
        self.assertIn("the user never creates JSON manually", guide)
        self.assertIn(
            "A valid topic command may target a section with no registered section manifest",
            self.catalog["catalogue_policy"]["on_demand_sections"],
        )


if __name__ == "__main__":
    unittest.main()
