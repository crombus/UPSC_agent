"""Regression tests for Modern History learner-v2 Topics 18-19."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_16_17_sequential as previous
import generate_modern_history_18_19_sequential as generator
import notions_style_ascii_master as ascii_master


class ModernHistory1819GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-18", "modern-indian-history-19"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "First World War, the Home Rule League & the Lucknow Pact (1914–1918)",
                "Gandhi's Rise: Champaran, Kheda, Ahmedabad; Rowlatt & Jallianwala Bagh (1917–1919)",
            ],
            [config["title"] for config in generator.TOPICS],
        )
        self.assertTrue(all(len(config["facts"]) == 20 for config in generator.TOPICS))
        self.assertTrue(all(len(config["mains"]) == 6 for config in generator.TOPICS))
        self.assertTrue(
            all(
                [item[0] for item in config["mains"]] == [10, 10, 15, 15, 20, 20]
                for config in generator.TOPICS
            )
        )
        self.assertTrue(
            all(
                len(generator.SESSION_PLANS[str(config["key"])]) == 15
                for config in generator.TOPICS
            )
        )

    def test_generated_sessions_and_workbooks_pass_contracts(self) -> None:
        for config in generator.TOPICS:
            key = str(config["key"])
            session_path = generator.SESSION_DIR / f"{key}_Learning-Session.md"
            workbook_path = generator.SESSION_DIR / f"{key}_Solved-Workbook.md"
            graphical_path = generator.GRAPHICAL_DIR / f"{key}.json"
            markdown = session_path.read_text(encoding="utf-8")
            workbook = workbook_path.read_text(encoding="utf-8")
            sessions = re.findall(
                r"(?m)^### SESSION (\d+) \u2014 (.+?) \u2014 (.+?)\s*$",
                markdown,
            )
            session_mcqs = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)
            workbook_mcqs = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", workbook)
            self.assertEqual(15, len(sessions), key)
            self.assertEqual(80, len(session_mcqs), key)
            self.assertEqual(80, len(set(session_mcqs)), key)
            self.assertEqual(80, len(workbook_mcqs), key)
            self.assertEqual(80, len(set(workbook_mcqs)), key)
            self.assertEqual(
                list("ABCD") * 20,
                re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown),
                key,
            )
            self.assertEqual(6, markdown.count("### ORIGINAL MAINS"), key)
            self.assertNotIn(" is the part of ", markdown, key)
            self.assertNotIn(" -> and -> ", markdown, key)
            self.assertNotIn("an evidence-led unit connecting", markdown, key)
            self.assertNotIn("Missing topic-specific session visual", markdown, key)
            generator.self_check(
                config,
                markdown,
                workbook,
                len(sessions),
                graphical_path,
            )

    def test_official_question_inventory_and_routed_cards(self) -> None:
        names = {path.name for path in generator.OFFICIAL_QUESTION_SOURCES}
        self.assertTrue(
            {
                "QP-CSP-18-GS-I-C.pdf.md",
                "CSP_2020_GS_Paper-1.pdf.md",
                "csp-p1.pdf.md",
                "GENERAL-STUDIES-PAPER-I.pdf.md",
                "QP-CSM19-GeneralStudies-I.pdf.md",
                "QP-CSM-23-GENERAL-STUDIES-PAPER-I-180923.pdf.md",
                "UPSC Mains 2024 GS Paper I.md",
                "2026-GS1-Set A.md",
            }.issubset(names)
        )
        topic18 = generator.TOPICS[0]
        topic19 = generator.TOPICS[1]
        self.assertIn("2018", {card[0] for card in topic18["pyq_solutions"]})
        self.assertEqual(
            {"2018", "2019", "2020", "2023"},
            {card[0] for card in topic19["pyq_solutions"]},
        )
        unkeyed_cards = [
            topic18["pyq_solutions"][0],
            topic19["pyq_solutions"][0],
            topic19["pyq_solutions"][1],
            topic19["pyq_solutions"][2],
        ]
        self.assertTrue(
            all("key-unavailable" in card[3] for card in unkeyed_cards)
        )
        self.assertTrue(
            all(
                re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I) is None
                for card in unkeyed_cards
            )
        )

    def test_ascii_and_graphical_specs_are_exact(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        self.assertEqual(set(generator.PANEL_DATA), set(specs))
        for key, spec in specs.items():
            self.assertEqual(12, len(spec.panels), key)
            self.assertTrue(
                all(
                    len(line) <= 100
                    for panel in spec.panels
                    for line in panel.body.splitlines()
                ),
                key,
            )
            graph = json.loads(
                (generator.GRAPHICAL_DIR / f"{key}.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual([], carvaka_flowchart.validate_spec(graph), key)
            self.assertEqual(13, len(graph["stages"]), key)
            if key == "modern-indian-history-19":
                comparison = next(
                    stage
                    for stage in graph["stages"]
                    if stage["title"] == "THREE LOCAL LABORATORIES"
                )
                combined = " ".join(comparison["sequence"])
                self.assertIn("CHAMPARAN", combined)
                self.assertIn("AHMEDABAD", combined)
                self.assertIn("KHEDA", combined)
                self.assertNotIn("AXIS CHAMPARAN AHMEDABAD KHEDA base", combined)

    def test_generation_manifests_are_tracker_free_generation_one(self) -> None:
        required_question_sources = {
            "knowledge-export\\Prelims PYQ\\QP-CSP-18-GS-I-C.pdf.md",
            "knowledge-export\\Prelims PYQ\\CSP_2020_GS_Paper-1.pdf.md",
            "knowledge-export\\Prelims PYQ\\csp-p1.pdf.md",
            "knowledge-export\\Mains PYQ\\GENERAL-STUDIES-PAPER-I.pdf.md",
            "knowledge-export\\Mains PYQ\\QP-CSM19-GeneralStudies-I.pdf.md",
            "knowledge-export\\Mains PYQ\\QP-CSM-23-GENERAL-STUDIES-PAPER-I-180923.pdf.md",
            "knowledge-export\\Mains PYQ\\UPSC Mains 2024 GS Paper I.md",
            "knowledge-export\\Prelims PYQ\\2026-GS1-Set A.md",
        }
        for config in generator.TOPICS:
            path = (
                generator.EXPORT_DIR
                / f"{config['key']}-new-topic-{generator.DATE}.json"
            )
            manifest = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(1, manifest["generation"])
            self.assertIsNone(manifest["supersedes"])
            self.assertTrue(manifest["tracker_untouched"])
            self.assertEqual("learner-v2", manifest["variant"])
            self.assertEqual("strict-abcd-cycle", manifest["mcq_answer_policy"])
            self.assertEqual(12, manifest["ascii_panel_count"])
            self.assertEqual(13, manifest["graphical_stage_count"])
            self.assertTrue(
                required_question_sources.issubset(
                    set(manifest["official_question_sources"])
                )
            )
            self.assertTrue((ROOT / manifest["source_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["workbook_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["source_canonical"]).is_file())

    def test_authored_visual_and_definition_maps_are_complete(self) -> None:
        titles = {
            item[0]
            for plans in generator.SESSION_PLANS.values()
            for item in plans
        }
        self.assertEqual(titles, set(generator.SESSION_VISUALS))
        self.assertEqual(titles, set(generator.SESSION_DEFINITIONS))
        self.assertTrue(
            all("KEY TERMS:" not in visual for visual in generator.SESSION_VISUALS.values())
        )
        self.assertTrue(
            all(
                "an evidence-led unit" not in definition
                for definition in generator.SESSION_DEFINITIONS.values()
            )
        )

    def test_import_does_not_mutate_topics_16_17(self) -> None:
        self.assertEqual(
            ["modern-indian-history-16", "modern-indian-history-17"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            [
                "Revolutionary Nationalism (Phase I, 1907-1917)",
                "Growth of Communalism & the Muslim League",
            ],
            [config["title"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-16", "modern-indian-history-17"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(all(len(panels) == 12 for panels in previous.PANEL_DATA.values()))
        self.assertEqual(
            "modern-indian-history-16-17-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )


if __name__ == "__main__":
    unittest.main()
