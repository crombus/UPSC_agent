"""Regression tests for Governance learner-v2 Topic 12."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_11_sequential as previous
import generate_governance_12_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance12GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-12"],
            ["Local Governance and Service Delivery"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-11"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_three_legs_are_taught_as_inputs_not_outcomes(self) -> None:
        text = session_markdown(generator, "governance-12")
        self.assertIn("own-source revenue and predictable formula-based transfers", text)
        self.assertIn("subjects actually transferred in practice", text)
        self.assertIn(
            "staff genuinely accountable to and controlled by the local body",
            text,
        )
        self.assertIn("constitutional status without delivery capacity", text)

    def test_constitutional_functional_domains_are_exact(self) -> None:
        text = session_markdown(generator, "governance-12")
        for phrase in (
            "Article 243G",
            "Eleventh Schedule",
            "twenty-nine listed subjects",
            "Twelfth Schedule",
            "eighteen municipal functions",
        ):
            self.assertIn(phrase, text)
        self.assertIn("the Schedule is enabling rather than self-executing", text)

    def test_planning_committees_use_exact_articles_and_rules(self) -> None:
        text = session_markdown(generator, "governance-12")
        self.assertIn("Article 243ZD", text)
        self.assertIn("at least four-fifths of the members elected by and from", text)
        self.assertIn("Article 243ZE", text)
        self.assertIn("no national compliance count may be invented", text)

    def test_fiscal_architecture_is_complete(self) -> None:
        text = session_markdown(generator, "governance-12")
        for phrase in (
            "State Finance Commission",
            "Article 280(3)(bb)",
            "Article 280(3)(c)",
            "tied and project-specific grants",
        ):
            self.assertIn(phrase, text)

    def test_scheduled_areas_precision_is_consultation_not_consent(self) -> None:
        text = session_markdown(generator, "governance-12")
        self.assertIn("Panchayats Extension to Scheduled Areas Act, 1996", text)
        self.assertIn("Fifth Schedule", text)
        self.assertIn(
            "consultation before land acquisition and resettlement in Scheduled Areas "
            "rather than a universal consent requirement",
            text,
        )

    def test_benchmark_carries_no_invented_percentage(self) -> None:
        text = session_markdown(generator, "governance-12")
        self.assertIn("Kerala People's Plan Campaign of 1996", text)
        self.assertIn(
            "no percentage of plan outlay is attached to it here",
            text,
        )

    def test_merger_is_balanced_with_a_decision_rule(self) -> None:
        text = session_markdown(generator, "governance-12")
        self.assertIn("unified planning across a functionally continuous settlement", text)
        self.assertIn("dilutes rural representation inside a larger urban body", text)
        self.assertIn("graduated reclassification with a transition period", text)

    def test_live_official_anchor_is_dated_and_bounded(self) -> None:
        text = session_markdown(generator, "governance-12")
        self.assertIn("read on 2 September 2026", text)
        self.assertIn("established in May 2004", text)
        self.assertIn("https://panchayat.gov.in/", generator.TOPICS[0]["live_sources"])
        self.assertIn("volatile personnel fact", text)

    def test_routed_demands_and_provisional_key_discipline(self) -> None:
        text = session_markdown(generator, "governance-12")
        workbook = workbook_markdown(generator, "governance-12")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(6, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(6, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "The strength and sustenance of local institutions in India has shifted",
            text,
        )
        self.assertIn(
            "To what extent, in your opinion, has the decentralisation of power in India",
            text,
        )
        self.assertIn(
            "Analyse the role of local bodies in providing good governance at local level",
            text,
        )
        self.assertIn("2026 Set-A key held locally is provisional", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-12")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Activity mapping vs functional devolution",
            "Parastatal encroachment",
            "Merger as service-continuity solution vs merger as representation-dilution risk",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-12"),
            topic_key="governance-12",
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
