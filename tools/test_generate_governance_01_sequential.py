"""Regression tests for Governance learner-v2 Topic 01."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_01_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance01GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-01"],
            ["Good Governance: Concepts and Frameworks"],
        )

    def test_this_is_the_first_topic_of_the_sequence(self) -> None:
        self.assertIsNone(generator.main.__defaults__)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=None", source)
        self.assertIn("previous_keys=None", source)

    def test_conceptual_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "governance-01")
        for phrase in (
            "Worldwide Governance Indicators",
            "Voice and Accountability",
            "Control of Corruption",
            "Regulatory Quality",
            "UNDP governance principles",
            "Second Administrative Reforms Commission",
            "Department of Administrative Reforms and Public Grievances",
            "Ministry of Personnel, Public Grievances and Pensions",
            "National e-Governance Service Delivery Assessment",
            "Devolution Index",
            "Sevottam",
        ):
            self.assertIn(phrase, text)

    def test_index_edition_status_is_exact_and_bounded(self) -> None:
        text = session_markdown(generator, "governance-01")
        self.assertIn("launched by the Department of Administrative Reforms", text)
        self.assertIn("25 December 2019", text)
        self.assertIn("Good Governance Index 2020-21", text)
        self.assertIn("released on 25 December 2021", text)
        self.assertIn("13 August 2026", text)
        self.assertIn("three groups while the 2020-21 edition used four", text)
        self.assertIn("the correction record of 13 August 2026 withdraws the claim", text)
        self.assertIn(
            "no post-2021 national edition, rank, score, top performer or indicator "
            "count may be asserted",
            text,
        )

    def test_rule_of_law_index_attribution_is_correct(self) -> None:
        text = session_markdown(generator, "governance-01")
        self.assertIn(
            "The Rule of Law Index is published by the World Justice Project and "
            "not by the World Bank",
            text,
        )
        self.assertIn("District Good Governance Index", text)

    def test_norm_to_instrument_anchors_are_named_with_limits(self) -> None:
        text = session_markdown(generator, "governance-01")
        for phrase in (
            "Article 14 non-arbitrariness",
            "Right to Information Act, 2005",
            "Articles 148 to 151",
            "Lokpal and Lokayuktas Act, 2013",
            "Central Vigilance Commission Act, 2003",
            "Pre-Legislative Consultation Policy of 2014",
            "Madhya Pradesh in 2010",
            "Output-Outcome Monitoring Framework",
            "Economic Survey 2018-19 Chapter 2",
        ):
            self.assertIn(phrase, text)
        self.assertIn("none of which is a general grievance authority", text)
        self.assertIn("executive rather than statutory", text)

    def test_zero_direct_mains_pyq_audit_is_transparent(self) -> None:
        text = session_markdown(generator, "governance-01")
        workbook = workbook_markdown(generator, "governance-01")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertIn(
            "No direct General Studies Mains demand is routed to this owner",
            text,
        )
        self.assertIn("official key as unavailable locally", text)
        self.assertIn(
            "no option set, no official key and no verbatim stem is reproduced "
            "or inferred",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "governance-01")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn("Organization that releases Rule of Law Index annually", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-01")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Indicator capture",
            "Perception-measurement gap",
            "Federal comparability problem",
            "auditability test",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-01"),
            topic_key="governance-01",
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
