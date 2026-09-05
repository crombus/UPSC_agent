"""Regression tests for Governance learner-v2 Topic 02."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_01_sequential as previous
import generate_governance_02_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance02GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-02"],
            ["Government Policy Design and Implementation"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-01"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_implementation_theory_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "governance-02")
        for phrase in (
            "Pressman and Wildavsky",
            "clearance point",
            "Michael Lipsky",
            "street-level bureaucracy",
            "creaming",
            "top-down",
            "bottom-up",
            "design realism",
            "convergence",
            "regulatory impact assessment",
        ):
            self.assertIn(phrase, text)

    def test_statute_scope_rule_is_exact(self) -> None:
        text = session_markdown(generator, "governance-02")
        self.assertIn("Public Examinations (Prevention of Unfair Means) Act, 2024", text)
        self.assertIn("21 June 2024", text)
        self.assertIn("S.O. 2422(E)", text)
        self.assertIn("Union Public Service Commission", text)
        self.assertIn("National Testing Agency", text)
        self.assertIn(
            "not automatically covered merely because the Act extends to India",
            text,
        )
        self.assertIn(
            "an executive statement of adoption is not a notification",
            text,
        )

    def test_programme_design_figures_are_bounded(self) -> None:
        text = session_markdown(generator, "governance-02")
        self.assertIn("112 districts", text)
        self.assertIn("49 key performance indicators", text)
        self.assertIn("Champions of Change", text)
        self.assertIn("delta ranking", text)
        self.assertIn("513 blocks", text)
        self.assertIn("largely district-self-reported", text)
        self.assertIn(
            "administrative-attention and convergence instrument",
            text,
        )

    def test_coordination_is_separated_from_authority(self) -> None:
        text = session_markdown(generator, "governance-02")
        self.assertIn("PM GatiShakti", text)
        self.assertIn("geographic-information-system", text)
        self.assertIn("coordinates information rather than authority", text)
        self.assertIn("Viability Gap Funding", text)
        self.assertIn("Hybrid Annuity Model", text)

    def test_four_routed_demands_are_solved_and_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "governance-02")
        workbook = workbook_markdown(generator, "governance-02")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "confirmed word for word in the locally held OCR-searchable official "
            "question papers",
            text,
        )
        self.assertIn("core routing supersedes the older Advanced pointer", text)
        self.assertIn("partly word-scrambled in the scan", text)
        self.assertIn("No official answer key is held locally", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_targeting_error_distinction_is_kept(self) -> None:
        text = session_markdown(generator, "governance-02")
        self.assertIn("inclusion error", text)
        self.assertIn("exclusion error", text)
        self.assertIn("offline or assisted fallback", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-02")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Agenda setting bias",
            "Design realism vs design ambition",
            "Consultation depth vs consultation compliance",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-02"),
            topic_key="governance-02",
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
