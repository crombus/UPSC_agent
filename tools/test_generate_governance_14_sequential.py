"""Regression tests for Governance learner-v2 Topic 14."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_13_sequential as previous
import generate_governance_14_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance14GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-14"],
            ["Participatory Governance"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-13"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_subsidiarity_is_taught_as_an_efficiency_principle(self) -> None:
        text = session_markdown(generator, "governance-14")
        self.assertIn(
            "its force is informational rather than sentimental",
            text,
        )
        self.assertIn(
            "a principle of the appropriate level rather than a blanket rule",
            text,
        )

    def test_quality_and_frequency_are_separated(self) -> None:
        text = session_markdown(generator, "governance-14")
        self.assertIn("participation quality", text)
        self.assertIn("participation frequency", text)
        self.assertIn(
            "an assembly that ratifies a plan already settled elsewhere",
            text,
        )

    def test_participation_ladder_is_complete_and_ordered(self) -> None:
        text = session_markdown(generator, "governance-14")
        for rung in (
            "information",
            "consultation",
            "involvement",
            "co-decision",
            "co-production",
            "delegated control",
        ):
            self.assertIn(rung, text)
        self.assertIn(
            "the most institutionalised instruments occupy the weakest rungs",
            text,
        )

    def test_consultation_policy_status_is_exact(self) -> None:
        text = session_markdown(generator, "governance-14")
        for phrase in (
            "Pre-Legislative Consultation Policy of 2014",
            "ordinarily at least thirty days for comments",
            "an executive policy rather than a statute",
            "comments are not binding",
            "no general duty to publish a reasoned response",
            "consultation feedback matrix",
        ):
            self.assertIn(phrase, text)

    def test_named_forums_carry_their_exact_anchors(self) -> None:
        text = session_markdown(generator, "governance-14")
        for phrase in (
            "Article 243S",
            "three lakh or more",
            "Gram Sabha",
            "participatory budgeting",
            "Panchayats Extension to Scheduled Areas Act, 1996",
            "Fifth Schedule",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "consultation before land acquisition and resettlement rather than a "
            "universal consent requirement",
            text,
        )

    def test_scale_and_capture_are_stated_honestly(self) -> None:
        text = session_markdown(generator, "governance-14")
        self.assertIn(
            "scattered set of municipal and ward-level pilots",
            text,
        )
        self.assertIn("elite capture", text.casefold())
        self.assertIn("economies of scale in large infrastructure", text)

    def test_live_official_anchor_is_dated_and_bounded(self) -> None:
        text = session_markdown(generator, "governance-14")
        self.assertIn("read on 2 September 2026", text)
        self.assertIn("start date of 10 July 2026", text)
        self.assertIn("end date of 20 August 2026", text)
        self.assertIn("https://www.mygov.in/", generator.TOPICS[0]["live_sources"])
        self.assertIn(
            "no campaign count, participation count, submission total or "
            "consultation outcome is asserted",
            text,
        )

    def test_routed_demands_and_recorded_routing_conflict(self) -> None:
        text = session_markdown(generator, "governance-14")
        workbook = workbook_markdown(generator, "governance-14")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(3, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "The need for cooperation among various service sectors has been an "
            "inherent component of development discourse.",
            text,
        )
        self.assertIn(
            "Do you agree with the view that increasing dependence on donor "
            "agencies for development",
            text,
        )
        self.assertIn("2026 Set-A key held locally is provisional", text)
        self.assertIn(
            "One ownership conflict is recorded openly rather than resolved by "
            "assertion",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-14")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Subsidiarity as an efficiency principle, not only a democratic-values principle",
            "Elite capture as a subsidiarity-implementation risk",
            "Centralisation's legitimate rationales",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-14"),
            topic_key="governance-14",
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
