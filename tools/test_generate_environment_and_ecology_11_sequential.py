"""Regression tests for Environment and Ecology learner-v2 Topic 11."""

from __future__ import annotations

import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)
import generate_environment_and_ecology_11_sequential as generator


class EnvironmentAndEcology11Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-11"],
            ["Forest Types and Forest Rights Act"],
        )

    def test_forest_and_rights_category_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-11").casefold()
        for phrase in (
            "four forest vocabularies",
            "recorded forest area",
            "forest or tree cover is a canopy measurement",
            "13 december 2005",
            "individual forest right",
            "community rights",
            "community forest resource right",
            "gram sabha",
            "sub-divisional",
            "district level",
            "recognition is not assumed",
        ):
            self.assertIn(phrase, text)

    def test_audited_mains_route_is_carried(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-11")
        for phrase in ("2020 GS-I Q17", "official UPSC solution", "Section 4(5)"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
