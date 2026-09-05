"""Regression tests for Governance learner-v2 Topic 05."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_04_sequential as previous
import generate_governance_05_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance05GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-05"],
            ["E-Governance Models and User-Centricity"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-04"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_five_models_are_named_and_not_ranked(self) -> None:
        text = session_markdown(generator, "governance-05")
        for phrase in (
            "Broadcasting",
            "Critical Flow",
            "Comparative Analysis",
            "Mobilisation and Networking",
            "Interactive Service",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "rather than forming an official chronological maturity ladder",
            text,
        )
        self.assertIn("one platform may run several of them at once", text)

    def test_three_axes_are_kept_separate(self) -> None:
        text = session_markdown(generator, "governance-05")
        self.assertIn("government to citizen, government to business", text)
        self.assertIn(
            "presence and information through interaction, transaction and integration",
            text,
        )
        self.assertIn("calling a downloadable-form page transactional", text)

    def test_assessment_parameters_and_dated_status_are_exact(self) -> None:
        text = session_markdown(generator, "governance-05")
        self.assertIn("National e-Governance Service Delivery Assessment", text)
        self.assertIn("Department of Administrative Reforms and Public Grievances", text)
        self.assertIn("end service delivery", text)
        self.assertIn("integrated service delivery", text)
        self.assertIn("must not be described as guaranteed biennial", text)
        self.assertIn("56 identified mandatory e-services", text)
        self.assertIn("25 May 2026", text)
        self.assertIn(
            "do not amount to the publication of a completed assessment report",
            text,
        )

    def test_back_end_bias_is_explained_as_a_mechanism(self) -> None:
        text = session_markdown(generator, "governance-05")
        self.assertIn("cannot easily specify that a citizen completes the task", text)
        self.assertIn("technology-push vs user-pull design", text)
        self.assertIn(
            "higher maturity raises rather than lowers the design risk",
            text,
        )

    def test_transparency_and_accountability_are_separated(self) -> None:
        text = session_markdown(generator, "governance-05")
        self.assertIn(
            "transparency vs accountability in the Interactive Service Model",
            text,
        )
        self.assertIn(
            "a log identifies the delay without identifying who must correct it",
            text,
        )

    def test_use_value_and_inclusion_checklist_are_complete(self) -> None:
        text = session_markdown(generator, "governance-05")
        for phrase in (
            "availability",
            "accessibility",
            "use value",
            "reasoned rejection",
            "document-burden test",
            "cost test",
        ):
            self.assertIn(phrase, text)
        self.assertIn("Common Service Centre", text)

    def test_no_unsourced_status_claim_is_asserted(self) -> None:
        text = session_markdown(generator, "governance-05")
        self.assertIn(
            "no official Indian policy, definition or target is attributed",
            text,
        )
        self.assertIn(
            "the official Press Information Bureau release page returned an access error",
            text,
        )

    def test_six_routed_mains_demands_are_solved(self) -> None:
        text = session_markdown(generator, "governance-05")
        workbook = workbook_markdown(generator, "governance-05")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(6, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(6, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("core routing supersedes the older Advanced pointer", text)
        self.assertIn(
            "no option, answer or distractor is recorded or inferred for it",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-05")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Technology-push vs user-pull design",
            "NeSDA's twin service-completion parameters",
            "Model vs maturity stage",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-05"),
            topic_key="governance-05",
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
