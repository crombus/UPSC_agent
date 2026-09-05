"""Regression tests for Environment and Ecology learner-v2 Topic 22."""

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
import generate_environment_and_ecology_22_sequential as generator


class EnvironmentAndEcology22Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-22"], ["Multilateral Environmental Conventions (CBD, Basel, Stockholm, Montreal)"])

    def test_treaty_scope_protocol_and_status_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-22").casefold()
        for phrase in (
            "treaty-scope map", "treaty-status sequence", "cbd three objectives",
            "cbd convention-protocol boundary", "basel pic mechanism",
            "stockholm annex functions", "poprc-to-cop sequence",
            "vienna-montreal hierarchy", "kigali hfc boundary",
        ):
            self.assertIn(phrase, text)

    def test_current_listings_and_obligations_not_invented(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-22")
        for phrase in ("No Party count", "current annex listing", "fund figure", "implementation result"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
