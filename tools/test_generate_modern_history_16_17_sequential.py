"""Regression tests for Modern History learner-v2 Topics 16-17."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_14_15_sequential as previous
import generate_modern_history_16_17_sequential as generator
import notions_style_ascii_master as ascii_master


class ModernHistory1617GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-16", "modern-indian-history-17"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "Revolutionary Nationalism (Phase I, 1907-1917)",
                "Growth of Communalism & the Muslim League",
            ],
            [config["title"] for config in generator.TOPICS],
        )
        self.assertTrue(all(len(config["facts"]) == 20 for config in generator.TOPICS))
        self.assertTrue(all(len(config["mains"]) == 6 for config in generator.TOPICS))
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
            sessions = re.findall(
                r"(?m)^### SESSION (\d+) \u2014 (.+?) \u2014 (.+?)\s*$",
                markdown,
            )
            self.assertEqual(15, len(sessions), key)
            self.assertNotIn(" is the part of ", markdown, key)
            self.assertNotIn(" -> and -> ", markdown, key)
            generator.self_check(
                config,
                markdown,
                workbook_path.read_text(encoding="utf-8"),
                len(sessions),
                graphical_path,
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

    def test_generation_manifests_are_tracker_free_generation_one(self) -> None:
        for config in generator.TOPICS:
            path = (
                generator.EXPORT_DIR
                / f"{config['key']}-new-topic-{generator.DATE}.json"
            )
            manifest = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(1, manifest["generation"])
            self.assertIsNone(manifest["supersedes"])
            self.assertTrue(manifest["tracker_untouched"])
            self.assertEqual("strict-abcd-cycle", manifest["mcq_answer_policy"])
            self.assertEqual(12, manifest["ascii_panel_count"])
            self.assertEqual(13, manifest["graphical_stage_count"])
            self.assertTrue((ROOT / manifest["source_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["workbook_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["source_canonical"]).is_file())

    def test_import_does_not_mutate_topics_14_15(self) -> None:
        self.assertEqual(
            ["modern-indian-history-14", "modern-indian-history-15"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            [
                "Foundation of the INC & the Moderate Phase (1885-1905)",
                "Militant Nationalism, Swadeshi & the Partition of Bengal (1905-1908)",
            ],
            [config["title"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-14", "modern-indian-history-15"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(all(len(panels) == 12 for panels in previous.PANEL_DATA.values()))
        self.assertEqual(
            "modern-indian-history-14-15-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )


if __name__ == "__main__":
    unittest.main()
