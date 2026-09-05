"""Regression tests for Indian Society learner-v2 Topic 03."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_02_sequential as previous
import generate_indian_society_03_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)


class IndianSociety03GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-03"],
            ["Tribe and Tribal Society"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-02"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_tribal_policy_and_official_evidence_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-03")
        for phrase in (
            "Verrier Elwin",
            "G.S. Ghurye",
            "Panchsheel for Tribals",
            "Article 342",
            "75 Particularly Vulnerable Tribal Groups",
            "9 July 2024",
            "Halbi",
        ):
            self.assertIn(phrase, text)

    def test_three_verified_pyq_demands_are_reproduced(self) -> None:
        text = session_markdown(generator, "indian-society-03")
        for phrase in (
            "Does tribal development in India centre around two axes, those of "
            "displacement and of rehabilitation?",
            "Examine the uniqueness of tribal knowledge system when compared with "
            "mainstream knowledge and cultural systems.",
            "Given the diversities among tribal communities in India, in which "
            "specific contexts should they be considered as a single category?",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))

    def test_unkeyed_prelims_item_is_not_solved(self) -> None:
        text = session_markdown(generator, "indian-society-03")
        self.assertIn("official key is not held locally", text)
        self.assertIn("no option is inferred", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-03")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Isolation (Elwin) vs integration (Nehru)",
            "Displacement vs land alienation",
            "Displacement-rehabilitation chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-03"),
            topic_key="indian-society-03",
        )
        high = [
            item
            for item in audit["defects"]
            if item["severity"] in {"high", "blocker"}
        ]
        self.assertEqual([], high)

    def test_generator_has_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
