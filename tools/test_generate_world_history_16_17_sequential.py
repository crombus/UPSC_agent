"""Regression tests for World History learner-v2 Topics 16-17."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_15_sequential as previous
import generate_world_history_16_17_sequential as generator
from world_history_generator_test_support import assert_batch_contract, session_markdown


class WorldHistory1617GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-16", "world-history-17"],
            ["United Nations and Global Governance", "China, Communism and Asia"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(["world-history-15"], [item["key"] for item in previous.TOPICS])

    def test_un_structure_and_case_categories_are_precise(self) -> None:
        text = session_markdown(generator, "world-history-16")
        for phrase in (
            "came into existence in October 1945",
            "six principal bodies",
            "fifteen members, including five permanent and ten non-permanent",
            "ICC is an independent treaty-based court",
            "collective enforcement, not ordinary blue-helmet peacekeeping",
            "WTO is not a UN specialised agency",
        ):
            self.assertIn(phrase, text)

    def test_china_chronology_reform_and_bloc_diversity_are_precise(self) -> None:
        text = session_markdown(generator, "world-history-17")
        for phrase in (
            "Chinese Communist Party was founded in 1921",
            "Long March, 1934-35",
            "People's Republic of China in 1949",
            "Great Leap Forward, 1958-61",
            "Cultural Revolution, 1966-76",
            "growth without multi-party political reform",
            "China attacked Soviet-aligned Vietnam in February 1979",
        ):
            self.assertIn(phrase, text)

    def test_topics16_17_have_no_claimed_pyq(self) -> None:
        for config in generator.TOPICS:
            text = session_markdown(generator, str(config["key"]))
            self.assertIn("No direct UPSC PYQ is verified", text)

    def test_topic16_uses_only_verified_un80_sources(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual(
            [
                "https://www.un.org/un80-initiative/en/news/what-un80-initiative",
                "https://news.un.org/en/interview/2026/06/1167739",
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-16")
        for phrase in (
            "Secretariat efficiency",
            "mandate implementation review",
            "structural or programmatic realignment",
            "movement from diagnosis towards action and implementation",
            "no unsupported budget, staffing or job figure",
        ):
            self.assertIn(phrase, text)

    def test_topic17_remains_bounded_without_live_source(self) -> None:
        config = generator.TOPICS[1]
        self.assertEqual([], config["live_sources"])
        self.assertIn("no verified live item", str(config["current_note"]))


if __name__ == "__main__":
    unittest.main()
