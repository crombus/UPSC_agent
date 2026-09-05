"""Regression tests for Environment and Ecology learner-v2 Topics 25-28."""

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
import generate_environment_and_ecology_25_sequential as generator_25
import generate_environment_and_ecology_26_sequential as generator_26
import generate_environment_and_ecology_27_sequential as generator_27
import generate_environment_and_ecology_28_sequential as generator_28


class EnvironmentAndEcology25To28Tests(unittest.TestCase):
    def test_topic_25_complete_contract_and_boundaries(self) -> None:
        assert_batch_contract(self, generator_25, ["environment-and-ecology-25"], ["Renewable Energy and Green Hydrogen"])
        text = session_markdown(generator_25, "environment-and-ecology-25").casefold()
        for phrase in ("capacity-generation boundary", "target-achievement boundary", "label-standard-certification boundary", "mission-target-outcome boundary"):
            self.assertIn(phrase, text)

    def test_topic_26_complete_contract_and_boundaries(self) -> None:
        assert_batch_contract(self, generator_26, ["environment-and-ecology-26"], ["Disaster Management Framework and Sendai"])
        text = session_markdown(generator_26, "environment-and-ecology-26").casefold()
        for phrase in ("hazard boundary", "risk relation", "ndma-nec boundary", "priorities-targets boundary", "global-domestic boundary"):
            self.assertIn(phrase, text)

    def test_topic_27_complete_contract_and_boundaries(self) -> None:
        assert_batch_contract(self, generator_27, ["environment-and-ecology-27"], ["Environmental Institutions (MoEFCC, CPCB, NBA, WII)"])
        text = session_markdown(generator_27, "environment-and-ecology-27").casefold()
        for phrase in ("institution-type boundary", "standards-consent boundary", "central-state jurisdiction boundary", "science-regulation boundary"):
            self.assertIn(phrase, text)

    def test_topic_28_complete_contract_and_boundaries(self) -> None:
        assert_batch_contract(self, generator_28, ["environment-and-ecology-28"], ["Species and Current Affairs Tracker"])
        text = session_markdown(generator_28, "environment-and-ecology-28").casefold()
        for phrase in ("taxonomic-identity boundary", "iucn-assessment boundary", "trigger-static boundary", "stale-current firewall"):
            self.assertIn(phrase, text)

    def test_generators_have_no_publish_side_effects(self) -> None:
        for generator in (generator_25, generator_26, generator_27, generator_28):
            assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
