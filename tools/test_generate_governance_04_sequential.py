"""Regression tests for Governance learner-v2 Topic 04."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_03_sequential as previous
import generate_governance_04_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance04GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-04"],
            ["NGOs, SHGs and Civil-Society Stakeholders"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-03"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_civil_society_scope_is_wider_than_ngos(self) -> None:
        text = session_markdown(generator, "governance-04")
        for phrase in (
            "trade unions",
            "cooperatives",
            "faith-based bodies",
            "professional associations",
            "resident welfare associations",
            "informal collectives",
        ):
            self.assertIn(phrase, text)
        self.assertIn("is a scope error an examiner can see immediately", text)

    def test_social_capital_typology_is_sequenced(self) -> None:
        text = session_markdown(generator, "governance-04")
        for phrase in ("bonding", "bridging", "linking", "Putnam"):
            self.assertIn(phrase, text)
        self.assertIn("none substituting for another", text)
        self.assertIn("Village Organisations and Cluster-Level Federations", text)
        self.assertIn("Deendayal Antyodaya Yojana", text)

    def test_no_mobilisation_count_is_asserted(self) -> None:
        text = session_markdown(generator, "governance-04")
        self.assertIn(
            "No cumulative self-help group or household count is asserted",
            text,
        )
        self.assertIn("rises continuously", text)

    def test_foreign_funding_and_identification_layers_are_exact(self) -> None:
        text = session_markdown(generator, "governance-04")
        self.assertIn("Foreign Contribution (Regulation) Act, 2010", text)
        self.assertIn("amended in 2020", text)
        self.assertIn("State Bank of India main branch in New Delhi", text)
        self.assertIn("fifty per cent to twenty per cent", text)
        self.assertIn("renewable every five years", text)
        self.assertIn("NGO Darpan", text)
        self.assertIn(
            "not incorporation, not foreign-funding permission and not tax exemption",
            text,
        )
        self.assertIn("Sections 12A and 80G", text)

    def test_structural_category_is_separated_from_political_label(self) -> None:
        text = session_markdown(generator, "governance-04")
        self.assertIn(
            "converts a constitutional freedom into a suspicion",
            text,
        )
        self.assertIn("justify or contest the label case by case", text)
        self.assertIn("a right needs an addressee who can be compelled", text)

    def test_micro_finance_evaluation_is_graded_and_bounded(self) -> None:
        text = session_markdown(generator, "governance-04")
        self.assertIn("micro-credit is only one component", text)
        self.assertIn(
            "strongest as a consumption-smoothing and vulnerability-reduction "
            "instrument and weakest as a structural poverty-exit instrument",
            text,
        )
        self.assertIn("over-indebtedness and multiple lending", text)
        self.assertIn("coercive recovery", text)
        self.assertIn("this is a convergence claim", text)
        self.assertIn("must not present a measured income-to-nutrition effect", text)

    def test_six_routed_demands_and_two_recorded_conflicts(self) -> None:
        text = session_markdown(generator, "governance-04")
        workbook = workbook_markdown(generator, "governance-04")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(6, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(6, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "Two ownership conflicts are recorded openly rather than resolved by "
            "assertion",
            text,
        )
        self.assertIn(
            "routed by the audited 2024-2025 ledger to the Social Justice women and "
            "gender-justice owner",
            text,
        )
        self.assertIn("Polity pressure-groups owner", text)
        self.assertIn("no verbatim ownership is claimed for either", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_exclusion_limit_and_representation_gate_are_stated(self) -> None:
        text = session_markdown(generator, "governance-04")
        self.assertIn(
            "The most excluded households are frequently not members of any "
            "self-help group",
            text,
        )
        self.assertIn(
            "party ticket distribution is the actual gate and is not civil-society "
            "controlled",
            text,
        )
        self.assertIn("elite capture", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-04")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Empowerment chain",
            "Suspicion/anti-State perception chain",
            "Pressure-group influence chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-04"),
            topic_key="governance-04",
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
