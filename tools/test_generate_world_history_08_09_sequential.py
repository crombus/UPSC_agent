"""Regression tests for World History learner-v2 Topics 08-09."""

from __future__ import annotations

import unittest
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_06_07_sequential as previous
import generate_world_history_08_09_sequential as generator
from world_history_generator_test_support import (
    assert_batch_contract,
    session_markdown,
    workbook_markdown,
)


class WorldHistory0809GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-08", "world-history-09"],
            ["Latin American Independence Movements", "World in 1914 and Outbreak of WWI"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["world-history-06", "world-history-07"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_latin_america_five_paths_and_social_verdict(self) -> None:
        text = session_markdown(generator, "world-history-08")
        for phrase in (
            "Haiti became independent in 1804",
            "Iberian crisis, 1808",
            "Brazil became independent under Pedro I in 1822",
            "five distinct political and social routes",
            "Political independence without equality",
        ):
            self.assertIn(phrase, text)

    def test_topic09_exact_pyq_and_balance_qualification(self) -> None:
        learning = session_markdown(generator, "world-history-09")
        workbook = workbook_markdown(generator, "world-history-09")
        exact = (
            "How far is it correct to say that the First World War was fought "
            "essentially for the preservation of balance of power?"
        )
        self.assertIn(exact, learning)
        self.assertIn(exact, workbook)
        self.assertIn("2024 GS-I demand", learning)
        self.assertIn("not the complete purpose", learning)

    def test_topic08_uses_only_the_verified_panama_linkage(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual(
            [
                "https://usoas.usmission.gov/"
                "u-s-addresses-commemoration-of-bicentennial-of-the-amphictyonic-congress-of-panama/"
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-08")
        for phrase in (
            "commemorates in 2026 the bicentennial",
            "1826 Amphictyonic Congress of Panama",
            "Bolivar's post-independence regional cooperation project",
            "no decorative event detail",
        ):
            self.assertIn(phrase, text)

    def test_topic09_remains_bounded_without_live_source(self) -> None:
        config = generator.TOPICS[1]
        self.assertIn("no verified live item", str(config["current_note"]))
        self.assertEqual([], config["live_sources"])


if __name__ == "__main__":
    unittest.main()
