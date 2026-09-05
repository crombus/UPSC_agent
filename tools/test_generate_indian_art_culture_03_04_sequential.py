"""Regression tests for Indian Art and Culture learner-v2 Topics 03-04."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_01_02_sequential as previous
import generate_indian_art_culture_03_04_sequential as generator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture0304GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-03", "indian-art-and-culture-04"],
            [
                "Temple Architecture and Chandella Khajuraho",
                "Indo-Islamic and Regional Architecture",
            ],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-art-and-culture-01", "indian-art-and-culture-02"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_temple_pyq_cluster_and_close_option_distinctions_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-03")
        for phrase in (
            "vigour comes from dynamic carving",
            "maithuna is only one",
            "Pallava patronage moved from rock-cut mandapas",
            "Chola legacy combines monumental granite temples",
            "Khajuraho and Mitaoli are different monuments",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))

    def test_indo_islamic_synthesis_and_routing_correction_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-04")
        for phrase in (
            "scientifically executed arches, vaults and domes",
            "material from twenty-seven demolished Hindu and Jaina temples",
            "collective workshop achievement",
            "Kalyana Mandapa objective demand belongs to Vijayanagara",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(["https://whc.unesco.org/en/list/1739"], generator.TOPICS[1]["live_sources"])


if __name__ == "__main__":
    unittest.main()

