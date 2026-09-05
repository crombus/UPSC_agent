"""Regression tests for Governance learner-v2 Topic 13."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_12_sequential as previous
import generate_governance_13_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance13GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-13"],
            ["Public Finance and Service-Delivery Tools"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-12"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_the_tool_stack_is_taught_as_four_distinct_layers(self) -> None:
        text = session_markdown(generator, "governance-13")
        self.assertIn("JAM trinity", text)
        self.assertIn("Jan Dhan universal bank-account access", text)
        self.assertIn(
            "diversion and idle balances at the agency and intermediary level",
            text,
        )
        self.assertIn(
            "which is a different leakage risk from the beneficiary-level risk",
            text,
        )
        self.assertIn("Department of Expenditure in the Ministry of Finance", text)

    def test_transfer_scope_is_broader_than_cash(self) -> None:
        text = session_markdown(generator, "governance-13")
        self.assertIn(
            "cash transfers to individuals, in-kind benefits delivered through "
            "authenticated systems and certain transfers to service enablers",
            text,
        )
        self.assertIn("treating it as a synonym for cash transfer is a scope error", text)

    def test_release_architecture_carries_its_dated_notification_trail(self) -> None:
        text = session_markdown(generator, "governance-13")
        for phrase in (
            "Office Memorandum No. 1(27)/PFMS/2020 dated 13 July 2023",
            "thirty-seven further schemes from 1 July 2025",
            "from 1 November 2025 it applies to all centrally sponsored schemes",
            "States and Union Territories with legislatures",
            "State Integrated Financial Management Information System",
            "RBI e-Kuber",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "applicability by notification is not verified operational onboarding",
            text,
        )

    def test_the_2021_model_is_marked_as_superseded_and_bounded(self) -> None:
        text = session_markdown(generator, "governance-13")
        self.assertIn(
            "rather than to central-sector schemes, to Finance Commission grants "
            "or to government expenditure generally",
            text,
        )
        self.assertIn("the release design has since been superseded", text)

    def test_error_framework_is_complete_with_the_asymmetry_judgment(self) -> None:
        text = session_markdown(generator, "governance-13")
        self.assertIn("inclusion error", text)
        self.assertIn("exclusion error", text)
        self.assertIn(
            "inclusion error is a fiscal cost to the state while exclusion error "
            "is a subsistence cost to a person",
            text,
        )
        self.assertIn(
            "manual override reintroduces part of the discretion",
            text,
        )

    def test_savings_claim_carries_no_invented_total(self) -> None:
        text = session_markdown(generator, "governance-13")
        self.assertIn(
            "no cumulative rupee total may be asserted as a permanently citable number",
            text,
        )
        self.assertIn("dashboard totals are reporting-date-bound", text)

    def test_procurement_and_local_finance_layers_are_exact(self) -> None:
        text = session_markdown(generator, "governance-13")
        for phrase in (
            "General Financial Rules, 2017",
            "value for money",
            "lowest-cost selection for quality-dependent services",
            "confidentiality of adverse information does not extinguish the duty "
            "to disclose the risk to the competent authority",
            "Article 280(3)(bb)",
            "Article 280(3)(c)",
        ):
            self.assertIn(phrase, text)

    def test_live_official_anchor_is_dated_and_bounded(self) -> None:
        text = session_markdown(generator, "governance-13")
        self.assertIn("read on 2 September 2026", text)
        self.assertIn(
            "https://financialservices.gov.in/",
            generator.TOPICS[0]["live_sources"],
        )
        self.assertIn(
            "nothing beyond that statement of role is imported from it",
            text,
        )
        self.assertIn("failed at the transport level", text)

    def test_routed_demand_is_single_verified_and_word_for_word(self) -> None:
        text = session_markdown(generator, "governance-13")
        workbook = workbook_markdown(generator, "governance-13")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(1, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(1, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "Reforming the government delivery system through the Direct Benefit "
            "Transfer Scheme is a progressive step, but it has its limitations too.",
            text,
        )
        self.assertIn(
            "core routing supersedes that older Advanced pointer",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-13")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Leakage reduction vs targeting-error correction",
            "Just-in-time release vs state flexibility",
            "inclusion-error/\nexclusion-error (Type I/Type II) framework",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-13"),
            topic_key="governance-13",
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
