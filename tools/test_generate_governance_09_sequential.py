"""Regression tests for Governance learner-v2 Topic 09."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_08_sequential as previous
import generate_governance_09_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance09GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-09"],
            ["Civil Services and Mission Karmayogi"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-08"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_three_classical_traits_are_taught_as_one_package(self) -> None:
        text = session_markdown(generator, "governance-09")
        self.assertIn("political neutrality, permanence and anonymity", text)
        self.assertIn("designed as one package", text)
        self.assertIn("it does not mean the absence of policy influence", text)
        self.assertIn("accountability displacement rather than accountability absence", text)

    def test_constitutional_setting_is_exact_and_bounded(self) -> None:
        text = session_markdown(generator, "governance-09")
        for phrase in (
            "Articles 309 to 311",
            "doctrine of pleasure",
            "Article 312",
            "Rajya Sabha resolution",
        ):
            self.assertIn(phrase, text)
        self.assertIn("is owned by Polity and must be cross-linked", text)

    def test_mission_karmayogi_status_is_dated_and_not_fabricated(self) -> None:
        text = session_markdown(generator, "governance-09")
        for phrase in (
            "2 September 2020",
            "Ministry of Personnel, Public Grievances and Pensions",
            "rules-based compliance to role-based and competency-driven",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "rather than a change of delivery mode from an offline classroom",
            text,
        )
        self.assertIn("no learner count, course count, completion total", text)

    def test_capacity_building_commission_live_anchor_is_dated(self) -> None:
        text = session_markdown(generator, "governance-09")
        self.assertIn("read on 2 September 2026", text)
        self.assertIn("established on 1 April 2021", text)
        self.assertIn("https://cbc.gov.in/", generator.TOPICS[0]["live_sources"])
        self.assertIn("Annual Capacity Building Plans", text)
        self.assertIn("Karmayogi Competency Model", text)

    def test_institutional_chain_is_four_tiered_and_not_collapsed(self) -> None:
        text = session_markdown(generator, "governance-09")
        for phrase in (
            "Prime Minister's Human Resources Council",
            "Cabinet Secretariat Coordination Unit",
            "Capacity Building Commission",
            "Karmayogi Bharat",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "describing the Commission as the sole implementing or platform-operating body is inaccurate",
            text,
        )

    def test_lateral_entry_scope_is_bounded(self) -> None:
        text = session_markdown(generator, "governance-09")
        self.assertIn("Joint Secretary, Director or Deputy Secretary level", text)
        self.assertIn(
            "periodic and targeted supplement to regular cadre promotion",
            text,
        )
        self.assertIn("does not mean the absence of policy influence", text)

    def test_politicisation_chain_and_protections_are_paired(self) -> None:
        text = session_markdown(generator, "governance-09")
        self.assertIn("posting and transfer discretion", text)
        self.assertIn("permanence protects the office rather than the post", text)
        self.assertIn("anonymity becomes asymmetric", text)
        self.assertIn("minimum-tenure norms", text)
        self.assertIn("reciprocal obligation", text)

    def test_routed_demands_and_recorded_ownership_conflict(self) -> None:
        text = session_markdown(generator, "governance-09")
        workbook = workbook_markdown(generator, "governance-09")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(3, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("Institutional quality is a crucial driver of economic performance", text)
        self.assertIn(
            "The ethos of civil service in India stand for the combination of "
            "professionalism with nationalistic consciousness",
            text,
        )
        self.assertIn("no option, answer letter or distractor is recorded or inferred", text)
        self.assertIn(
            "routes that demand to the citizen-centric-administration owner",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-09")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Doctrine of Democratic Governance (as framed in the 2024 PYQ)",
            "Anonymity as accountability displacement, not accountability absence",
            "Generalist-specialist debate as a capacity-allocation problem",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-09"),
            topic_key="governance-09",
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
