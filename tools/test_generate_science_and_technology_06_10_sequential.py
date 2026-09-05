"""Regression tests for Science and Technology learner-v2 Topics 06-10."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from science_and_technology_generator_test_support import (  # noqa: E402
    assert_no_publish_side_effects,
    assert_topic_contract,
    session_markdown,
)
import generate_science_and_technology_06_sequential as generator_06  # noqa: E402
import generate_science_and_technology_07_sequential as generator_07  # noqa: E402
import generate_science_and_technology_08_sequential as generator_08  # noqa: E402
import generate_science_and_technology_09_sequential as generator_09  # noqa: E402
import generate_science_and_technology_10_sequential as generator_10  # noqa: E402


class ScienceAndTechnology06To10Tests(unittest.TestCase):
    def test_topic_06_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_06, "science-and-technology-06",
            "Defence R&D: DRDO and Missile Systems", 1,
        )
        text = session_markdown(generator_06, "science-and-technology-06").casefold()
        for phrase in ("drdo-developer boundary", "ballistic-cruise boundary", "test-status ladder", "volatile-capability boundary"):
            self.assertIn(phrase, text)

    def test_topic_07_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_07, "science-and-technology-07",
            "Defence Indigenisation: Atmanirbhar and Procurement", 1,
        )
        text = session_markdown(generator_07, "science-and-technology-07").casefold()
        for phrase in ("design-manufacture-content boundary", "buy-ladder boundary", "aon-order boundary", "volatile-number boundary"):
            self.assertIn(phrase, text)

    def test_topic_08_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_08, "science-and-technology-08",
            "Digital India and India Stack: UPI, Aadhaar", 1,
        )
        text = session_markdown(generator_08, "science-and-technology-08").casefold()
        for phrase in ("programme-dpi boundary", "aadhaar-identity boundary", "upi-rail boundary", "npci-rbi boundary"):
            self.assertIn(phrase, text)

    def test_topic_09_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_09, "science-and-technology-09",
            "Artificial Intelligence Governance and IndiaAI", 1,
        )
        text = session_markdown(generator_09, "science-and-technology-09").casefold()
        for phrase in ("capability-deployment boundary", "compute-measure boundary", "guideline-law boundary", "procurement-accountability boundary"):
            self.assertIn(phrase, text)

    def test_topic_10_contract_and_boundaries(self) -> None:
        assert_topic_contract(
            self, generator_10, "science-and-technology-10",
            "National Quantum Mission and Quantum Technology", 1,
        )
        text = session_markdown(generator_10, "science-and-technology-10").casefold()
        for phrase in ("bit-qubit boundary", "entanglement-boundary", "qkd-pqc boundary", "target-achievement boundary"):
            self.assertIn(phrase, text)

    def test_generators_are_authoring_only(self) -> None:
        for generator in (generator_06, generator_07, generator_08, generator_09, generator_10):
            assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
