"""Regression tests for World History learner-v2 Topics 11-12."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_10_sequential as previous
import generate_world_history_11_12_sequential as generator
from world_history_generator_test_support import (
    assert_batch_contract,
    session_markdown,
    workbook_markdown,
)


class WorldHistory1112GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-11", "world-history-12"],
            ["International Relations 1919-39", "Rise of Fascism: Italy, Germany, Japan"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(["world-history-10"], [item["key"] for item in previous.TOPICS])

    def test_interwar_chronology_and_collective_security_verdict(self) -> None:
        text = session_markdown(generator, "world-history-11")
        for phrase in (
            "10 January 1920",
            "Dawes Plan used American credit",
            "western frontiers but left its eastern frontiers unguaranteed",
            "Japan's seizure of Manchuria",
            "Half-hearted sanctions",
            "Prague in March 1939",
        ):
            self.assertIn(phrase, text)

    def test_topic12_verified_2021_demand_is_transparent(self) -> None:
        learning = session_markdown(generator, "world-history-12")
        workbook = workbook_markdown(generator, "world-history-12")
        demand = "Evaluate the challenge to the democratic state system between the two World Wars."
        self.assertIn(demand, learning)
        self.assertIn(demand, workbook)
        self.assertIn("neutral rendering", learning)
        self.assertIn("not claimed as verbatim", learning)

    def test_fascism_comparison_and_power_transfer_are_precise(self) -> None:
        text = session_markdown(generator, "world-history-12")
        for phrase in (
            "more bluff than conquest",
            "never won an overall electoral majority",
            "Enabling Law of March 1933",
            "race was constitutive",
            "military authoritarianism is safer",
        ):
            self.assertIn(phrase, text)

    def test_topic11_uses_only_verified_locarno_linkage(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual(
            [
                "https://www.gov.uk/government/speeches/"
                "the-foreign-secretarys-locarno-centenary-speech"
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-11")
        for phrase in (
            "hundredth anniversary of the 1925 treaty signing",
            "present security and multilateral cooperation",
            "limits of the 'spirit of Locarno'",
            "incomplete guarantees",
        ):
            self.assertIn(phrase, text)

    def test_topic12_uses_bounded_un_remembrance_link(self) -> None:
        config = generator.TOPICS[1]
        self.assertEqual(
            [
                "https://www.un.org/en/outreach-programme-holocaust/"
                "united-nations-holocaust-memorial-observance"
            ],
            config["live_sources"],
        )
        text = session_markdown(generator, "world-history-12")
        for phrase in (
            "27 January 2026",
            "Holocaust Remembrance for Dignity and Human Rights",
            "consequences of Nazism",
            "not evidence about Italian fascism or Japanese militarism",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
