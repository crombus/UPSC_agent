"""Regression tests for Indian Society learner-v2 Topic 15."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_14_sequential as previous
import generate_indian_society_15_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety15GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-15"],
            ["Secularism"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-14"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_lived_practice_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-15")
        for phrase in (
            "lived secularism",
            "sarva-dharma-sama-bhava",
            "syncretism",
            "equal public space",
            "tolerance",
            "assimilation",
            "pluralism",
            "substantive equality",
            "formal equality",
            "community autonomy",
        ):
            self.assertIn(phrase, text)

    def test_normative_doctrine_is_separated_from_descriptive_outcome(self) -> None:
        text = session_markdown(generator, "indian-society-15")
        self.assertIn("Articles 25 to 28", text)
        self.assertIn(
            "everyday coexistence never proves that the doctrine has been "
            "satisfied",
            text,
        )
        self.assertIn(
            "single episode of exclusion never proves that the doctrine has "
            "failed",
            text,
        )

    def test_uttarakhand_code_status_is_exact(self) -> None:
        text = session_markdown(generator, "indian-society-15")
        self.assertIn("Uniform Civil Code, Uttarakhand, 2024", text)
        self.assertIn("27 January 2025", text)
        self.assertIn("Rules, 2025", text)
        self.assertIn("reported as an ordinance", text)
        self.assertIn("absence of an official enacted text", text)
        self.assertIn("Portuguese Civil Code", text)

    def test_practice_analysis_names_a_mechanism_not_a_community(self) -> None:
        text = session_markdown(generator, "indian-society-15")
        self.assertIn(
            "exclusion or coercion mechanism in shared space rather than "
            "merely because it is religious",
            text,
        )
        self.assertIn("never move from a practice to a verdict about a community", text)

    def test_routed_pyq_status_and_support_role_are_transparent(self) -> None:
        text = session_markdown(generator, "indian-society-15")
        workbook = workbook_markdown(generator, "indian-society-15")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no verbatim wording is claimed", text)
        self.assertIn("named only as society support", text)
        self.assertIn(
            "No direct standalone secularism demand appears in the audited "
            "2024-2025 General Studies Paper-I ledger",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-15")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "UCC social-debate chain",
            "Uttarakhand implementation chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-15"),
            topic_key="indian-society-15",
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
