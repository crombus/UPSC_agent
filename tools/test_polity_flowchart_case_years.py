"""Targeted regression tests for Polity flowchart judicial case years."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import notions_style_ascii_master as ascii_master
import polity_flowchart_case_years as case_years


class PolityCaseYearTests(unittest.TestCase):
    def test_known_case_without_year_is_normalized(self) -> None:
        changes: list[dict[str, object]] = []
        actual = case_years.normalize_text(
            "polity-07",
            "Shreya Singhal: 66A void.",
            changes=changes,
        )
        self.assertEqual("Shreya Singhal (2015): 66A void.", actual)
        self.assertEqual("shreya-singhal", changes[0]["case_id"])

    def test_reporter_year_is_corrected_to_decision_year(self) -> None:
        actual = case_years.normalize_text(
            "polity-10",
            "1965 SAJJAN SINGH -> 1981 WAMAN RAO",
        )
        self.assertEqual(
            "SAJJAN SINGH (1964) -> WAMAN RAO (1980)",
            actual,
        )

    def test_unknown_case_is_not_guessed(self) -> None:
        text = "Unregistered Example Case remains pending."
        self.assertEqual(text, case_years.normalize_text("polity-07", text))

    def test_tulsiram_alias_does_not_duplicate_case_name(self) -> None:
        actual = case_years.normalize_text(
            "polity-41",
            "Union of India v Tulsiram Patel upheld the proviso architecture.",
        )
        self.assertEqual(
            "Union of India v. Tulsiram Patel (1985) upheld the proviso architecture.",
            actual,
        )

    def test_validator_rejects_missing_known_year(self) -> None:
        errors = case_years.ascii_topic_errors(
            "polity-03",
            "Minerva Mills explains constitutional harmony.",
        )
        self.assertTrue(any("Minerva Mills (1980)" in error for error in errors))

    def test_all_authored_polity_ascii_specs_have_case_years(self) -> None:
        specs = ascii_master.load_manual_topic_specs(
            ROOT
            / "upsc-ai-kit"
            / "manifests"
            / "retrofits"
            / "ascii-panel-specs"
        )
        polity_specs = {
            key: spec for key, spec in specs.items() if key.startswith("polity-")
        }
        self.assertEqual(55, len(polity_specs))
        for topic_key, spec in polity_specs.items():
            text = "\n".join(
                f"{panel.title}\n{panel.body}" for panel in spec.panels
            )
            self.assertEqual(
                [],
                case_years.ascii_topic_errors(topic_key, text),
                topic_key,
            )

    def test_all_polity_graphical_specs_have_case_years(self) -> None:
        root = (
            ROOT
            / "upsc-ai-kit"
            / "manifests"
            / "retrofits"
            / "carvaka-graphical-specs"
            / "Polity"
        )
        paths = sorted(root.glob("polity-*.json"))
        self.assertEqual(55, len(paths))
        for path in paths:
            spec = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(
                [],
                case_years.graphical_spec_errors(spec),
                path.name,
            )


if __name__ == "__main__":
    unittest.main()
