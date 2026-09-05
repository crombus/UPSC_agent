"""Regression tests for World History learner-v2 Topics 13-14."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_11_12_sequential as previous
import generate_world_history_13_14_sequential as generator
from world_history_generator_test_support import assert_batch_contract, session_markdown


class WorldHistory1314GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-13", "world-history-14"],
            ["Russian Revolution and USSR under Stalin", "Second World War"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["world-history-11", "world-history-12"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_revolution_chronology_and_stalinist_cost_are_bounded(self) -> None:
        text = session_markdown(generator, "world-history-13")
        for phrase in (
            "abdicated on 2 March 1917",
            "night of 25-26 October",
            "Assembly in January 1918",
            "Brest-Litovsk to remove Russia from war",
            "New Economic Policy restored peasant incentives",
            "estimates above five million deaths",
            "5 March 1953",
        ):
            self.assertIn(phrase, text)

    def test_second_world_war_is_global_cumulative_and_source_bounded(self) -> None:
        text = session_markdown(generator, "world-history-14")
        for phrase in (
            "Two regional wars fused in 1941",
            "Operation Barbarossa, 22 June 1941",
            "Pearl Harbor, 7 December 1941",
            "D-Day, 6 June 1944",
            "about 5.7 million murdered Jews",
            "Vidkun Quisling",
            "accelerated, but did not instantly complete, decolonisation",
        ):
            self.assertIn(phrase, text)

    def test_no_unverified_pyqs_are_claimed(self) -> None:
        for config in generator.TOPICS:
            text = session_markdown(generator, str(config["key"]))
            self.assertIn("No direct UPSC PYQ is verified", text)

    def test_topic13_remains_bounded_without_live_source(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual([], config["live_sources"])
        self.assertIn("no verified live item", str(config["current_note"]))

    def test_topic14_uses_only_bounded_nuremberg_linkage(self) -> None:
        config = generator.TOPICS[1]
        self.assertEqual(
            [
                "https://www.roberthjackson.org/"
                "80-years-of-nuremberg-an-international-reflection/"
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-14")
        for phrase in (
            "marks eighty years of Nuremberg",
            "war crimes, crimes against humanity and genocide",
            "Second World War's legal aftermath",
            "not new evidence about the war's campaigns",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
