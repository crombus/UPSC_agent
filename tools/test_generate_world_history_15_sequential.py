"""Regression tests for World History learner-v2 Topic 15."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_13_14_sequential as previous
import generate_world_history_15_sequential as generator
from world_history_generator_test_support import assert_batch_contract, session_markdown


class WorldHistory15GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-15"],
            ["Cold War and International Relations"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["world-history-13", "world-history-14"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_cold_war_chronology_and_global_agency_are_precise(self) -> None:
        text = session_markdown(generator, "world-history-15")
        for phrase in (
            "Truman Doctrine and Marshall Plan, 1947",
            "Berlin blockade was answered by airlift",
            "war ended near the thirty-eighth parallel",
            "Berlin Wall physicalised",
            "SALT I, the US-China opening and Helsinki",
            "non-alignment to protect sovereignty",
            "China's 1979 attack on Soviet-aligned Vietnam",
            "1987 INF Treaty",
        ):
            self.assertIn(phrase, text)

    def test_middle_east_and_detente_are_qualified(self) -> None:
        text = session_markdown(generator, "world-history-15")
        self.assertIn("had autonomous force even when superpowers intervened", text)
        self.assertIn("managed but did not end rivalry", text)
        self.assertNotIn("every Middle Eastern conflict was a proxy", text)

    def test_no_unverified_pyq_is_claimed(self) -> None:
        config = generator.TOPICS[0]
        text = session_markdown(generator, "world-history-15")
        self.assertIn("No direct UPSC PYQ is verified", text)

    def test_only_verified_diplomacy_museum_links_are_used(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual(
            [
                "https://diplomacy.state.gov/about-nmad/",
                "https://diplomacy.state.gov/discover-diplomacy/period/cold-war-diplomacy/",
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-15")
        for phrase in (
            "scheduled to open in October 2026",
            "Berlin Wall segment",
            "Berlin Airlift, nuclear rivalry, proxy wars and diplomacy",
            "renewed attention to Cold War diplomacy",
            "not a present-day geopolitical analogy",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
