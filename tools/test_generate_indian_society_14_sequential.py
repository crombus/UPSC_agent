"""Regression tests for Indian Society learner-v2 Topic 14."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_13_sequential as previous
import generate_indian_society_14_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety14GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-14"],
            ["Regionalism"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-13"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_four_concepts_and_movement_forms_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-14")
        for phrase in (
            "regional disparity",
            "sub-regionalism",
            "identity-driven regionalism",
            "disparity-driven regionalism",
            "statehood demand",
            "autonomy demand",
            "secessionist demand",
            "fiscal capacity",
            "human development",
            "recognition",
            "redistribution",
        ):
            self.assertIn(phrase, text)

    def test_disparity_and_diversity_are_kept_independent(self) -> None:
        text = session_markdown(generator, "indian-society-14")
        self.assertIn("diversity vs disparity as independent axes", text)
        self.assertIn("colonial-era investment patterns", text)
        self.assertIn(
            "outcome-based development concept rather than a description of "
            "cultural difference",
            text,
        )

    def test_index_anchor_is_edition_bound_and_limited(self) -> None:
        text = session_markdown(generator, "indian-society-14")
        self.assertIn("NITI Aayog SDG India Index", text)
        self.assertIn("2023-24 edition", text)
        self.assertIn("as of July 2026", text)
        self.assertIn("mask intra-state variation", text)

    def test_accommodation_record_and_statute_are_present(self) -> None:
        text = session_markdown(generator, "indian-society-14")
        self.assertIn("States Reorganisation Act, 1956", text)
        self.assertIn("least common form in the typology", text)
        self.assertIn("not a compulsory escalation ladder", text.replace(
            "rather than a compulsory escalation ladder",
            "not a compulsory escalation ladder",
        ))

    def test_routed_pyq_status_is_transparent_and_unfabricated(self) -> None:
        text = session_markdown(generator, "indian-society-14")
        workbook = workbook_markdown(generator, "indian-society-14")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(2, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(2, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no verbatim wording is claimed", text)
        self.assertIn(
            "What is regional disparity? How does it differ from diversity? "
            "How Serious is the issue of regional disparity in India?",
            text,
        )
        self.assertIn("printed capitalisation irregularity", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_no_state_ranking_or_income_figure_is_asserted(self) -> None:
        text = session_markdown(generator, "indian-society-14")
        self.assertIn(
            "No state ranking, index score, per-capita income or "
            "infrastructure figure is asserted",
            text,
        )

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-14")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Diversity-disparity independence chain",
            "Sub-regionalism escalation chain",
            "Policy-response chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-14"),
            topic_key="indian-society-14",
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
