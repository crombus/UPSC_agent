"""Regression tests for Indian Society learner-v2 Topic 12."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_11_sequential as previous
import generate_indian_society_12_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety12GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-12"],
            ["Social Change and Modernisation"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-11"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_change_vocabulary_and_scholars_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-12")
        for phrase in (
            "Sanskritisation",
            "Westernisation",
            "M. N. Srinivas",
            "Robert Redfield",
            "McKim Marriott",
            "Great Tradition",
            "Little Tradition",
            "universalisation",
            "parochialisation",
            "status inconsistency",
            "diffusionist",
            "structural-functionalism",
            "conflict theory",
        ):
            self.assertIn(phrase, text)

    def test_secularisation_boundary_is_kept_three_way(self) -> None:
        text = session_markdown(generator, "indian-society-12")
        self.assertIn("secularisation", text)
        self.assertIn("desacralisation", text)
        self.assertIn(
            "constitutional doctrine of secularism",
            text,
        )
        self.assertIn("Articles 25 to 28", text.replace("Article 25 to Article 28", "Articles 25 to 28"))

    def test_durable_theory_topic_forces_no_current_anchor(self) -> None:
        text = session_markdown(generator, "indian-society-12")
        self.assertIn("durable-theory topic", text)
        self.assertIn("no dated current-affairs anchor is forced", text)

    def test_routed_pyq_status_is_transparent_and_unfabricated(self) -> None:
        text = session_markdown(generator, "indian-society-12")
        workbook = workbook_markdown(generator, "indian-society-12")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no verbatim wording is claimed", text)
        self.assertIn(
            "How do you account for the growing fast food industries given "
            "that there are increased health concerns",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_cryptocurrency_answer_stays_on_the_society_layer(self) -> None:
        text = session_markdown(generator, "indian-society-12")
        self.assertIn("asserts no price, no legal status and no adoption figure", text)
        self.assertIn("Economy digital-economy owner", text)

    def test_cross_owner_conflict_is_recorded_not_resolved(self) -> None:
        text = session_markdown(generator, "indian-society-12")
        self.assertIn("Globalisation owner's own answer-architecture table", text)
        self.assertIn("cross-owner conflict is stated openly", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-12")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Sanskritisation-Westernisation-Modernisation interaction chain",
            "Universalisation-parochialisation chain",
            "Secularisation chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-12"),
            topic_key="indian-society-12",
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
