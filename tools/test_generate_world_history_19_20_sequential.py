"""Regression tests for World History learner-v2 Topics 19-20."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_18_sequential as previous
import generate_world_history_19_20_sequential as generator
import notions_style_ascii_master as ascii_master
from world_history_generator_test_support import (
    assert_batch_contract,
    session_markdown,
    workbook_markdown,
)


class WorldHistory1920GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-19", "world-history-20"],
            ["Latin America (20th Century)", "World Economy and Population since 1900"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(["world-history-18"], [item["key"] for item in previous.TOPICS])

    def test_latin_america_cases_and_mechanisms_are_specific(self) -> None:
        text = session_markdown(generator, "world-history-19")
        for phrase in (
            "US influence in Latin America usually operated",
            "Guatemala was overturned",
            "Cuba's revolution survived",
            "Sandinistas took power in 1979",
            "import-substituting industrialisation",
            "ninety-six-billion-dollar overseas debt",
            "inflation around nine hundred per cent",
        ):
            self.assertIn(phrase, text)

    def test_world_economy_population_and_depression_logic_is_precise(self) -> None:
        text = session_markdown(generator, "world-history-20")
        for phrase in (
            "1944 Bretton Woods framework",
            "2008 crisis demonstrated",
            "death rates fell",
            "China's one-child policy",
            "Wall Street Crash as a symptom",
            "reduced spending in 1938 produced another recession",
            "Germany's employment recovery rested on militarisation",
        ):
            self.assertIn(phrase, text)

    def test_legacy_2013_depression_demand_is_neutral_and_solved(self) -> None:
        learning = session_markdown(generator, "world-history-20")
        workbook = workbook_markdown(generator, "world-history-20")
        demand = "policy instruments deployed to contain the Great Economic Depression"
        self.assertIn("2013", learning)
        self.assertIn(demand, learning)
        self.assertIn(demand, workbook)
        self.assertIn("not claimed as verbatim", learning)
        self.assertIn("marks and verbatim wording not locally held", workbook)
        self.assertNotIn("2013 Q", learning)

    def test_topic19_has_no_claimed_pyq(self) -> None:
        self.assertIn(
            "No direct UPSC PYQ is verified",
            session_markdown(generator, "world-history-19"),
        )

    def test_topic19_uses_only_verified_argentina_source(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual(
            [
                "https://www.ohchr.org/en/press-releases/2026/03/argentina-alarming-setbacks-transitional-justice-50th-anniversary-coup-detat"
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-19")
        for phrase in (
            "19 March 2026",
            "fiftieth anniversary",
            "Argentina's 1976 military dictatorship",
            "transitional justice, truth, memory",
            "guarantees of non-repetition",
            "no unverified crowd or other numerical claim",
        ):
            self.assertIn(phrase, text)

    def test_topic20_uses_only_verified_un_economy_and_population_sources(self) -> None:
        config = generator.TOPICS[1]
        self.assertEqual(
            [
                "https://unctad.org/publication/world-economic-situation-and-prospects-2026",
                "https://population.un.org/wpp/",
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-20")
        for phrase in (
            "slower and uneven world growth",
            "trade and investment headwinds",
            "stronger policy coordination",
            "official current demographic-data anchor",
            "no 2026 population estimate",
            "unfetched economic figure",
        ):
            self.assertIn(phrase, text)

    def test_ascii_spec_is_registered_for_production_rendering(self) -> None:
        self.assertIn(generator.ASCII_PATH.name, ascii_master.MANUAL_SPEC_FILENAMES)


if __name__ == "__main__":
    unittest.main()
