"""Regression tests for Indian Art and Culture learner-v2 Topic 05."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_03_04_sequential as previous
import generate_indian_art_culture_05_sequential as generator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture05GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-05"],
            ["Colonial and Post-Independence Architecture"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-art-and-culture-03", "indian-art-and-culture-04"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_modern_architecture_precision_and_zero_pyq_audit_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-05")
        for phrase in (
            "Le Corbusier's Chandigarh",
            "filler slabs",
            "first Indian Pritzker laureate in 2018",
            "Padma Vibhushan 2023 posthumous",
            "no Padma or other award is attributed to Raj Rewal",
            "1927 building survives as Samvidhan Sadan",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)
        self.assertIn("the 2020 award was Padma Bhushan", text)
        self.assertEqual(["https://whc.unesco.org/en/list/1480/"], generator.TOPICS[0]["live_sources"])


if __name__ == "__main__":
    unittest.main()
