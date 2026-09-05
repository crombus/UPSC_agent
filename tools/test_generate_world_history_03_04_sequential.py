"""Regression tests for World History learner-v2 Topics 03-04."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_01_02_sequential as previous
import generate_world_history_03_04_sequential as generator
from world_history_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class WorldHistory0304GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-03", "world-history-04"],
            ["French Revolution and Napoleon", "Industrial Revolution"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["world-history-01", "world-history-02"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_topics03_04_keep_bounded_no_live_item_language(self) -> None:
        for config in generator.TOPICS:
            self.assertEqual([], config["live_sources"])
            self.assertIn("no verified live item", config["current_note"])
            self.assertNotIn("america250.org", config["current_note"].casefold())

    def test_topic03_phase_chronology_is_precise(self) -> None:
        text = session_markdown(generator, "world-history-03")
        for phrase in (
            "17 June 1789",
            "20 June 1789",
            "14 July 1789",
            "1791",
            "republic declared in 1792",
            "1793-94",
            "1795-99",
            "coup in 1799",
            "Napoleonic Code of 1804",
            "Waterloo in 1815",
        ):
            self.assertIn(phrase, text)
        self.assertNotIn("Napoleonic Code of 1799", text)

    def test_topic03_terror_napoleon_and_exclusions_are_balanced(self) -> None:
        text = session_markdown(generator, "world-history-03")
        for phrase in (
            "seventeen thousand",
            "universal male political rights",
            "Women participated centrally",
            "final French abolition came in 1848",
            "heir to legal equality",
            "betrayer of republican sovereignty",
        ):
            self.assertIn(phrase, text)

    def test_topic03_verified_2019_and_2025_demands_are_solved(self) -> None:
        text = session_markdown(generator, "world-history-03")
        self.assertIn("2019", text)
        self.assertIn("2025", text)
        self.assertIn(
            "The French Revolution has enduring relevance to the contemporary world. Explain.",
            text,
        )

    def test_topic04_invention_sequence_and_social_response(self) -> None:
        text = session_markdown(generator, "world-history-04")
        for phrase in (
            "spinning jenny of 1764",
            "water frame",
            "power loom of 1785",
            "cotton gin of 1793",
            "Factory Act in England in 1802",
            "anti-union laws in 1824",
            "Chartism",
            "first passenger railway in 1830",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "Watt improved rather than solely invented the steam engine",
            text,
        )

    def test_topic04_verified_railway_and_handicraft_demands_are_solved(self) -> None:
        text = session_markdown(generator, "world-history-04")
        self.assertIn("2023", text)
        self.assertIn("2024", text)
        self.assertIn("socio-economic effects of railways", text)
        self.assertIn("decline of handicrafts and cottage industries in India", text)
        self.assertIn("technologically enabled but politically mediated", text)


if __name__ == "__main__":
    unittest.main()
