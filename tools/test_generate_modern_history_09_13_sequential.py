"""Regression tests for Modern History learner-v2 Topics 09-13."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_09_13_sequential as generator
import notions_style_ascii_master as ascii_master


class ModernHistory0913GeneratorTests(unittest.TestCase):
    def test_five_learner_first_topics_are_configured(self) -> None:
        self.assertEqual(
            [f"modern-indian-history-{number:02d}" for number in range(9, 14)],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertTrue(all(len(config["facts"]) == 20 for config in generator.TOPICS))

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
            self.assertTrue(manifest["tracker_untouched"])
            self.assertEqual("strict-abcd-cycle", manifest["mcq_answer_policy"])
            self.assertEqual(12, manifest["ascii_panel_count"])
            self.assertEqual(13, manifest["graphical_stage_count"])
            self.assertTrue((ROOT / manifest["source_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["workbook_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["source_canonical"]).is_file())


if __name__ == "__main__":
    unittest.main()
