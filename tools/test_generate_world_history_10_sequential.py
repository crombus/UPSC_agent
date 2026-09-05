"""Regression tests for World History learner-v2 Topic 10."""

from __future__ import annotations

import unittest
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_08_09_sequential as previous
import generate_world_history_10_sequential as generator
from world_history_generator_test_support import (
    assert_batch_contract,
    session_markdown,
    workbook_markdown,
)


class WorldHistory10GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-10"],
            ["First World War and Aftermath"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["world-history-08", "world-history-09"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_course_total_war_and_treaty_cluster(self) -> None:
        text = session_markdown(generator, "world-history-10")
        for phrase in (
            "Battle of the Marne in September 1914",
            "United States entered in April 1917",
            "Treaty of Brest-Litovsk in March 1918",
            "fighting ended on 11 November 1918",
            "St Germain for Austria",
            "Lausanne in 1923",
            "one hundred thousand",
        ):
            self.assertIn(phrase, text)

    def test_topic09_pyq_not_misowned(self) -> None:
        learning = session_markdown(generator, "world-history-10")
        workbook = workbook_markdown(generator, "world-history-10")
        self.assertIn("exact 2024 balance-of-power demand belongs to Topic 09", learning)
        self.assertNotIn(
            "How far is it correct to say that the First World War was fought essentially",
            workbook,
        )

    def test_current_linkage_remains_bounded(self) -> None:
        config = generator.TOPICS[0]
        self.assertIn("no verified live item", str(config["current_note"]))
        self.assertEqual([], config["live_sources"])


if __name__ == "__main__":
    unittest.main()
