"""Regression tests for Environment and Ecology learner-v2 Topic 16."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)
import generate_environment_and_ecology_16_sequential as generator


class EnvironmentAndEcology16Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-16"], ["Environmental Impact Assessment and NGT"])

    def test_clearance_process_and_jurisdiction_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-16").casefold()
        for phrase in (
            "prior ec boundary", "ec and consent boundary", "multiple-clearance boundary",
            "screening boundary", "public-consultation boundary", "original-jurisdiction boundary",
            "appellate-jurisdiction boundary", "limitation discipline", "instrument and evidence boundary",
        ):
            self.assertIn(phrase, text)

    def test_live_eia_ngt_failures_are_honest(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-16")
        for phrase in ("visibly legacy procedural text", "PARIVESH", "HTTP 403", "transport level"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
