"""Regression tests for World History learner-v2 Topic 05."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_03_04_sequential as previous
import generate_world_history_05_sequential as generator
from world_history_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class WorldHistory05GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-05"],
            ["Congress of Vienna and Concert of Europe"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["world-history-03", "world-history-04"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_topic05_keeps_bounded_no_live_item_language(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual([], config["live_sources"])
        self.assertIn("no verified live item", config["current_note"])
        self.assertNotIn("america250.org", config["current_note"].casefold())

    def test_vienna_principles_and_map_changes_are_preserved(self) -> None:
        text = session_markdown(generator, "world-history-05")
        for phrase in (
            "1814-15",
            "Final Act signed in June 1815",
            "Metternich",
            "legitimacy",
            "Balance-of-power",
            "Compensation",
            "thirty-nine states",
            "Lombardy and Venetia",
            "Congress Poland",
            "Swiss neutrality",
        ):
            self.assertIn(phrase, text)

    def test_concert_holy_alliance_and_congresses_are_distinct(self) -> None:
        text = session_markdown(generator, "world-history-05")
        for phrase in (
            "Concert was a diplomatic habit",
            "Holy Alliance of Russia, Austria and Prussia",
            "Aix-la-Chapelle in 1818",
            "Carlsbad Decrees of 1819",
            "Troppau and Laibach",
            "Congress of Verona in 1822",
        ):
            self.assertIn(phrase, text)
        self.assertNotIn("Holy Alliance was the whole Concert of Europe", text)

    def test_belgium_1848_and_dual_verdict_are_bounded(self) -> None:
        text = session_markdown(generator, "world-history-05")
        self.assertIn("Belgian independence in 1830", text)
        self.assertIn("revolutions of 1848", text)
        self.assertIn("dynastic armies", text)
        self.assertIn("stability with a legitimacy deficit", text)
        self.assertIn("No direct UPSC PYQ is verified", text)


if __name__ == "__main__":
    unittest.main()
