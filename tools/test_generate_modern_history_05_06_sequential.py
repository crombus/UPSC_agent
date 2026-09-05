"""Targeted tests for the Modern History 05-06 authoring generator."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_05_06_sequential as generator
import notions_style_ascii_master as ascii_master


class ModernHistory0506GeneratorTests(unittest.TestCase):
    def test_authored_ascii_spec_is_exact(self) -> None:
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

    def test_generated_markdown_and_workbooks_pass_internal_contracts(self) -> None:
        expected_sessions = {
            "modern-indian-history-05": 26,
            "modern-indian-history-06": 16,
        }
        for config in generator.TOPICS:
            key = str(config["key"])
            session_path = generator.SESSION_DIR / f"{key}_Learning-Session.md"
            workbook_path = generator.SESSION_DIR / f"{key}_Solved-Workbook.md"
            graph_path = generator.GRAPHICAL_DIR / f"{key}.json"
            generator.self_check(
                session_path.read_text(encoding="utf-8"),
                workbook_path.read_text(encoding="utf-8"),
                key,
                expected_sessions[key],
                graph_path,
            )

    def test_graphical_specs_are_valid_and_have_twelve_core_stages(self) -> None:
        for key in generator.PANEL_DATA:
            path = generator.GRAPHICAL_DIR / f"{key}.json"
            spec = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual([], carvaka_flowchart.validate_spec(spec), key)
            self.assertEqual(13, len(spec["stages"]), key)
            self.assertEqual(
                12,
                len([stage for stage in spec["stages"] if stage["role"] != "extra"]),
            )
            self.assertEqual("extra", spec["stages"][-1]["role"])

    def test_generation_manifests_preserve_authoring_only_state(self) -> None:
        for key in generator.PANEL_DATA:
            path = generator.EXPORT_DIR / f"{key}-new-topic-{generator.DATE}.json"
            manifest = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(manifest["tracker_untouched"])
            self.assertEqual("strict-abcd-cycle", manifest["mcq_answer_policy"])
            self.assertEqual(12, manifest["ascii_panel_count"])
            self.assertEqual(13, manifest["graphical_stage_count"])
            self.assertTrue((ROOT / manifest["source_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["workbook_markdown"]).is_file())


if __name__ == "__main__":
    unittest.main()
