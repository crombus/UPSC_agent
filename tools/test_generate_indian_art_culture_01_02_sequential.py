"""Regression tests for Indian Art and Culture learner-v2 Topics 01-02."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_01_02_sequential as generator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture0102GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-01", "indian-art-and-culture-02"],
            [
                "Architecture Foundations and Harappan Urbanism",
                "Mauryan, Buddhist, Jain and Rock-Cut Heritage",
            ],
        )

    def test_harappan_evidence_boundaries_and_pyq_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-01")
        for phrase in (
            "standardised burnt mud bricks",
            "House drains joined larger covered street drains",
            "No large structure has been securely identified",
            "Lothal's basin is conventionally called a dockyard",
            "Discuss the salient features of the Harappan architecture",
        ):
            self.assertIn(phrase, text)
        self.assertIn("https://whc.unesco.org/en/list/1645/", generator.TOPICS[0]["live_sources"])

    def test_rock_cut_route_and_site_distinctions_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-02")
        for phrase in (
            "dedicated by Ashoka and Dasharatha to the Ajivikas",
            "chaitya is a prayer or assembly hall",
            "Ajanta lies in the Waghora gorge",
            "Ellora's thirty-four caves",
            "Rock-cut architecture as a source for early Indian art and history",
        ):
            self.assertIn(phrase, text)
        self.assertIn("Verified neutral routed demand", text)


if __name__ == "__main__":
    unittest.main()
