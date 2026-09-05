"""Regression tests for Science and Technology learner-v2 Topics 01-05."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from science_and_technology_generator_test_support import (
    assert_no_publish_side_effects,
    assert_topic_contract,
    session_markdown,
)
import generate_science_and_technology_01_sequential as generator_01
import generate_science_and_technology_02_sequential as generator_02
import generate_science_and_technology_03_sequential as generator_03
import generate_science_and_technology_04_sequential as generator_04
import generate_science_and_technology_05_sequential as generator_05


class ScienceAndTechnology01To05Tests(unittest.TestCase):
    def test_topic_01_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_01, "science-and-technology-01",
            "Space Programme: ISRO, Organisation and Launch Vehicles", 2,
        )
        text = session_markdown(generator_01, "science-and-technology-01").casefold()
        for phrase in ("dos-isro boundary", "launcher-spacecraft boundary", "gto-geo boundary", "nglv status boundary"):
            self.assertIn(phrase, text)

    def test_topic_02_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_02, "science-and-technology-02",
            "Satellites, NavIC, GAGAN and Applications", 1,
        )
        text = session_markdown(generator_02, "science-and-technology-02").casefold()
        for phrase in ("navic-system boundary", "gagan-system boundary", "integrity-accuracy boundary", "sbas-gbas boundary"):
            self.assertIn(phrase, text)

    def test_topic_03_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_03, "science-and-technology-03",
            "Human Spaceflight: Gaganyaan and Planetary Missions", 1,
        )
        text = session_markdown(generator_03, "science-and-technology-03").casefold()
        for phrase in ("human-rating boundary", "air-drop-test boundary", "axiom-gaganyaan boundary", "planetary-defence boundary"):
            self.assertIn(phrase, text)

    def test_topic_04_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_04, "science-and-technology-04",
            "Nuclear Power and the Three-Stage Programme", 1,
        )
        text = session_markdown(generator_04, "science-and-technology-04").casefold()
        for phrase in ("criticality boundary", "fissile-fertile boundary", "pfbr-status boundary", "capacity-generation boundary"):
            self.assertIn(phrase, text)

    def test_topic_05_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_05, "science-and-technology-05",
            "Nuclear Fusion and ITER", 1,
        )
        text = session_markdown(generator_05, "science-and-technology-05").casefold()
        for phrase in ("q-plasma boundary", "engineering-breakeven boundary", "iter-purpose boundary", "demo-commercial boundary"):
            self.assertIn(phrase, text)

    def test_generators_are_authoring_only(self) -> None:
        for generator in (generator_01, generator_02, generator_03, generator_04, generator_05):
            assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
