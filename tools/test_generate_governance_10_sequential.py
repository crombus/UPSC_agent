"""Regression tests for Governance learner-v2 Topic 10."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_09_sequential as previous
import generate_governance_10_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance10GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-10"],
            ["Administrative Reforms and the Second ARC"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-09"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_both_commissions_are_dated_and_correctly_attributed(self) -> None:
        text = session_markdown(generator, "governance-10")
        for phrase in (
            "ran from 1966 to 1970",
            "Morarji Desai",
            "K. Hanumanthaiah",
            "constituted in 2005",
            "M. Veerappa Moily",
            "fifteen reports between 2006 and 2009",
        ):
            self.assertIn(phrase, text)

    def test_recommendation_is_never_presented_as_law(self) -> None:
        text = session_markdown(generator, "governance-10")
        self.assertIn(
            "becomes binding only when separately enacted as law, notified as a "
            "rule or order, or adopted as administrative practice",
            text,
        )
        self.assertIn("proposed, partially implemented or adopted", text)

    def test_five_status_ladder_is_complete_with_its_evidence(self) -> None:
        text = session_markdown(generator, "governance-10")
        for phrase in (
            "accepted in principle",
            "notified or enacted",
            "operational where institutions, staff, budget and procedure actually function",
            "evaluated where independent evidence exists",
        ):
            self.assertIn(phrase, text)

    def test_fifteen_report_routing_table_is_complete(self) -> None:
        text = session_markdown(generator, "governance-10")
        for title in (
            "Right to Information",
            "Unlocking Human Capital",
            "Crisis Management",
            "Ethics in Governance",
            "Public Order",
            "Local Governance",
            "Capacity Building for Conflict Resolution",
            "Combating Terrorism",
            "Social Capital",
            "Refurbishing of Personnel Administration",
            "Promoting e-Governance",
            "Citizen-Centric Administration",
            "Organisational Structure of the Government of India",
            "Strengthening Financial Management Systems",
            "State and District Administration",
        ):
            self.assertIn(title, text)

    def test_paper_three_reports_are_excluded_not_forced(self) -> None:
        text = session_markdown(generator, "governance-10")
        self.assertIn("Reports three, five, seven and eight", text)
        self.assertIn(
            "cross-referenced rather than forced into a Paper-II governance answer",
            text,
        )

    def test_federal_step_and_attribution_trap_are_stated(self) -> None:
        text = session_markdown(generator, "governance-10")
        self.assertIn("federal-capacity fact rather than a Union-indifference fact", text)
        self.assertIn("thematic similarity is not implementation evidence", text)
        self.assertIn(
            "the single most common fabricated claim in this area",
            text,
        )

    def test_nodal_department_cannot_compel(self) -> None:
        text = session_markdown(generator, "governance-10")
        self.assertIn("Department of Administrative Reforms and Public Grievances", text)
        self.assertIn(
            "coordinative and advisory rather than directive",
            text,
        )

    def test_zero_direct_mains_ownership_is_recorded_honestly(self) -> None:
        text = session_markdown(generator, "governance-10")
        workbook = workbook_markdown(generator, "governance-10")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertIn("no direct Mains demand is routed here", text)
        self.assertEqual(1, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(1, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no option, answer letter or distractor is recorded or inferred", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-10")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Report-routing vs report-duplication",
            "Selective implementation as the norm, not the exception",
            "DARPG functions as the continuing institutional memory",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-10"),
            topic_key="governance-10",
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
