"""Regression tests for Governance learner-v2 Topic 07."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_06_sequential as previous
import generate_governance_07_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance07GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-07"],
            ["Citizen-Centric Administration"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-06"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_three_pillars_and_architecture_scope(self) -> None:
        text = session_markdown(generator, "governance-07")
        self.assertIn("Sevottam", text)
        self.assertIn("service delivery capability", text)
        self.assertIn(
            "an institutional architecture rather than a single document",
            text,
        )
        self.assertIn("assessment and improvement model rather than a statute", text)

    def test_charter_origin_and_design_stage_limitation(self) -> None:
        text = session_markdown(generator, "governance-07")
        self.assertIn("from 1997 on the United Kingdom model", text)
        self.assertIn(
            "a design-stage limitation rather than an implementation failure",
            text,
        )

    def test_statutory_guarantee_and_five_element_test(self) -> None:
        text = session_markdown(generator, "governance-07")
        self.assertIn("Right to Public Services", text)
        self.assertIn("Madhya Pradesh in 2010", text)
        for phrase in (
            "whether the service is notified",
            "whether a designated officer is named",
            "first and second appeal",
            "penalty, compensation, deemed approval or nothing",
        ):
            self.assertIn(phrase, text)

    def test_penalty_and_compensation_are_separated(self) -> None:
        text = session_markdown(generator, "governance-07")
        self.assertIn(
            "many State statutes provide the first without the second",
            text,
        )
        self.assertIn(
            "generalising one State's arrangement to all States is a common and "
            "avoidable error",
            text,
        )

    def test_grievance_platform_limits_and_dated_benchmarks(self) -> None:
        text = session_markdown(generator, "governance-07")
        self.assertIn("Centralised Public Grievance Redress and Monitoring System", text)
        self.assertIn(
            "cannot compel a service, decide a statutory entitlement or award "
            "compensation",
            text,
        )
        self.assertIn("21-day benchmark", text)
        self.assertIn("30 days for appeals", text)
        self.assertIn("August 2024", text)

    def test_layer_mismatch_and_capability_counterpoint(self) -> None:
        text = session_markdown(generator, "governance-07")
        self.assertIn("analytical claim", text)
        self.assertIn("the capability layer is frequently the weakest link", text)
        self.assertIn(
            "refusal to accept applications, procedural rejection to stop the clock",
            text,
        )

    def test_chain_break_and_quality_measure(self) -> None:
        text = session_markdown(generator, "governance-07")
        self.assertIn("auto-detectable against the stated timeline", text)
        self.assertIn(
            "resolution, reasoned closure, recurrence, appeal outcome and citizen "
            "feedback",
            text,
        )
        self.assertIn("rights-holder", text)

    def test_two_routed_demands_and_one_recorded_conflict(self) -> None:
        text = session_markdown(generator, "governance-07")
        workbook = workbook_markdown(generator, "governance-07")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(5, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(5, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "One ownership conflict is recorded openly rather than resolved by "
            "assertion",
            text,
        )
        self.assertIn(
            "routes that demand to the transparency, accountability, "
            "grievance-redress and social-audit owner",
            text,
        )
        self.assertIn("Doctrine of Democratic Governance", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-07")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Charter proliferation vs charter quality",
            "CPGRAMS as monitoring, not adjudication",
            "Single-window delivery vs actual back-end integration",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-07"),
            topic_key="governance-07",
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
