"""Targeted tests for the Modern History 01-02 authoring generator."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_01_02_sequential as generator
import notions_style_ascii_master as ascii_master


class ModernHistory0102GeneratorTests(unittest.TestCase):
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

    def test_generated_sessions_pass_internal_contracts(self) -> None:
        for config in generator.TOPICS:
            key = str(config["key"])
            session_path = generator.SESSION_DIR / f"{key}_Learning-Session.md"
            graph_path = generator.GRAPHICAL_DIR / f"{key}.json"
            generator.self_check(
                session_path.read_text(encoding="utf-8"),
                key,
                graph_path,
            )

    def test_graphical_specs_have_twelve_core_stages(self) -> None:
        for key in generator.PANEL_DATA:
            path = generator.GRAPHICAL_DIR / f"{key}.json"
            spec = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual([], carvaka_flowchart.validate_spec(spec), key)
            self.assertEqual(13, len(spec["stages"]), key)
            self.assertEqual(
                12,
                len([stage for stage in spec["stages"] if stage["role"] != "extra"]),
            )


if __name__ == "__main__":
    unittest.main()
