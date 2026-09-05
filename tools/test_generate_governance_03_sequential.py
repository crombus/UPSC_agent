"""Regression tests for Governance learner-v2 Topic 03."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_02_sequential as previous
import generate_governance_03_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance03GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-03"],
            ["Development Processes and the Development Industry"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-02"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_legal_vehicle_boundaries_are_exact(self) -> None:
        text = session_markdown(generator, "governance-03")
        self.assertIn(
            "Section 1 of the Indian Trusts Act, 1882 expressly excludes public or "
            "private religious or charitable endowments",
            text,
        )
        self.assertIn("Societies Registration Act, 1860", text)
        self.assertIn("Section 8 company", text)
        self.assertIn("prohibited from distributing profits", text)
        self.assertIn(
            "never be cited as a uniform national incorporation statute",
            text,
        )

    def test_corporate_responsibility_is_statutory_and_rule_bounded(self) -> None:
        text = session_markdown(generator, "governance-03")
        self.assertIn("Section 135 of the Companies Act, 2013", text)
        self.assertIn("two per cent of the average net profits", text)
        self.assertIn("Schedule VII", text)
        self.assertIn(
            "statutory minimum-spend obligation with a bounded activity list rather "
            "than voluntary corporate charity",
            text,
        )
        self.assertIn("Companies (Corporate Social Responsibility Policy) Rules", text)
        self.assertIn("no rupee threshold or national spend total is asserted", text)

    def test_accountability_direction_and_grid_are_present(self) -> None:
        text = session_markdown(generator, "governance-03")
        self.assertIn("reports upward to trustees, donors and regulators", text)
        for phrase in (
            "additionality",
            "need-fit",
            "sustainability",
            "federal or local fit",
        ):
            self.assertIn(phrase, text)
        self.assertIn("substitution", text)
        self.assertIn("complementarity", text)
        self.assertIn("visible-need bias", text)

    def test_multi_level_planning_evidence_is_named(self) -> None:
        text = session_markdown(generator, "governance-03")
        self.assertIn("District Planning Committee", text)
        self.assertIn("Article 243ZD", text)
        self.assertIn("State Finance Commission", text)
        self.assertIn("Kerala People's Plan Campaign", text)
        self.assertIn("1996", text)

    def test_routed_demands_are_solved_and_conflict_is_recorded(self) -> None:
        text = session_markdown(generator, "governance-03")
        workbook = workbook_markdown(generator, "governance-03")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(3, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "In contemporary development models, decision-making and problem-solving "
            "responsibilities are not located close to the source of information and "
            "execution",
            text,
        )
        self.assertIn(
            "One ownership conflict is recorded openly rather than resolved by "
            "assertion",
            text,
        )
        self.assertIn(
            "routes that demand to the non-governmental organisations, self-help "
            "groups and civil-society owner",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_prohibited_figures_are_declared(self) -> None:
        text = session_markdown(generator, "governance-03")
        self.assertIn(
            "No national or company corporate social responsibility spend total",
            text,
        )
        self.assertIn("devolution percentage", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-03")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Accountability substitution",
            "briefcase NGOs",
            "Evaluation grid for a non-state development intervention",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-03"),
            topic_key="governance-03",
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
