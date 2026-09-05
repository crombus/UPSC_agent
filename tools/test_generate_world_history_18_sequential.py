"""Regression tests for World History learner-v2 Topic 18."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_16_17_sequential as previous
import generate_world_history_18_sequential as generator
from world_history_generator_test_support import (
    assert_batch_contract,
    session_markdown,
    workbook_markdown,
)


class WorldHistory18GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-18"],
            ["Decolonization of Africa and Asia"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["world-history-16", "world-history-17"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_decolonisation_routes_and_postcolonial_mechanisms_are_specific(self) -> None:
        text = session_markdown(generator, "world-history-18")
        for phrase in (
            "Ghana achieved relatively smooth constitutional transfer",
            "Algeria, 1962",
            "only seventeen graduates",
            "Malayan Emergency and independence",
            "inter-communal Alliance victory in 1955",
            "outsiders worsened rather than created the conflict",
            "ended through negotiated majority rule in 1994",
        ):
            self.assertIn(phrase, text)

    def test_both_legacy_pyq_demands_are_transparent_and_solved(self) -> None:
        learning = session_markdown(generator, "world-history-18")
        workbook = workbook_markdown(generator, "world-history-18")
        for year, demand in (
            ("2015", "problems of decolonisation in the Malay Peninsula"),
            ("2016", "role of Western-educated Africans"),
        ):
            self.assertIn(year, learning)
            self.assertIn(demand, learning)
            self.assertIn(demand, workbook)
        self.assertIn("not claimed as verbatim", learning)
        self.assertIn("marks and verbatim wording not locally held", workbook)

    def test_topic18_uses_only_verified_c24_sources(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual(
            [
                "https://news.un.org/en/story/2026/02/1166971",
                "https://press.un.org/en/2026/gacol3398.doc.htm",
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-18")
        for phrase in (
            "17 remaining Non-Self-Governing Territories",
            "continuing legacy of colonialism",
            "information from administering Powers",
            "visiting or special missions",
            "unfinished UN business",
            "must not be conflated with the historical mass decolonization",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
