"""Regression tests for World History learner-v2 Topics 06-07."""

from __future__ import annotations

import unittest
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_05_sequential as previous
import generate_world_history_06_07_sequential as generator
from world_history_generator_test_support import assert_batch_contract, session_markdown


class WorldHistory0607GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-06", "world-history-07"],
            ["Unification of Italy and Germany", "New Imperialism and Scramble for Africa"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(["world-history-05"], [item["key"] for item in previous.TOPICS])

    def test_unification_chronology_and_comparison(self) -> None:
        text = session_markdown(generator, "world-history-06")
        for phrase in (
            "Kingdom of Italy was proclaimed in 1861",
            "Venetia joined Italy in 1866",
            "Rome joined Italy in 1870",
            "Seven Weeks' War of 1866",
            "German Empire was proclaimed at Versailles in January 1871",
            "state-led and military",
        ):
            self.assertIn(phrase, text)

    def test_scramble_precision_and_african_agency(self) -> None:
        text = session_markdown(generator, "world-history-07")
        for phrase in (
            "15 November 1884 to 26 February 1885",
            "representatives of fourteen countries",
            "effective occupation",
            "not a complete cartographic act",
            "defeated Italy at Adwa in 1896",
            "genocide of the Herero and Nama",
        ):
            self.assertIn(phrase, text)

    def test_no_unverified_pyq_is_claimed(self) -> None:
        for config in generator.TOPICS:
            text = session_markdown(generator, str(config["key"]))
            self.assertIn("No direct UPSC PYQ is verified", text)

    def test_topic06_remains_bounded_without_live_source(self) -> None:
        config = generator.TOPICS[0]
        self.assertIn("no verified live item", str(config["current_note"]))
        self.assertEqual([], config["live_sources"])

    def test_topic07_uses_only_the_verified_au_linkage(self) -> None:
        config = generator.TOPICS[1]
        self.assertEqual(
            [
                "https://au.int/en/pressreleases/20260525/"
                "au-leaders-issue-joint-africa-day-call-unity-reform-and-renewed-commitment"
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-07")
        for phrase in (
            "63 years since the founding of the Organization of African Unity",
            "reparatory justice",
            "enduring legacy of slavery and colonialism",
            "continuing legacy of imperialism and decolonisation",
            "does not directly discuss the Berlin Conference",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
