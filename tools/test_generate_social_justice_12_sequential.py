"""Regression tests for Social Justice learner-v2 Topic 12."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_12_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice12GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-12"],
            ["Elderly and Senior Citizens"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-11"]', source)

    def test_ageing_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        for phrase in (
            "Section 2(h)",
            "Section 23",
            "Maintenance Tribunal",
            "AVYAY",
            "Rashtriya Vayoshri Yojana",
            "Senior Citizen Opportunities for Productive Engagement",
            "Seniorcare Ageing Growth Engine",
            "Bureau of Indian Standards",
            "Elderline",
            "14567",
            "LASI",
            "Madrid International Plan of Action on Ageing",
        ):
            self.assertIn(phrase, text)

    def test_statutory_limits_travel_with_the_remedy(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        self.assertIn("ninety days", text)
        self.assertIn("₹10,000", text)
        self.assertIn(
            "children and on relatives, relatives being those who are or who "
            "will be the legal heirs",
            text,
        )
        self.assertIn("one hundred and fifty indigent senior citizens", text)

    def test_lapsed_and_pending_bills_are_not_presented_as_law(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        self.assertIn("lapsed with the dissolution of that Lok Sabha", text)
        self.assertIn("Private Members' Bills", text)
        self.assertIn(
            "the law in force is the 2007 Act",
            text,
        )

    def test_five_official_components_are_named(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        for phrase in (
            "Integrated Programme for Senior Citizens",
            "State Action Plan for Senior Citizens",
        ):
            self.assertIn(phrase, text)
        self.assertIn("five components", text)

    def test_counts_and_projections_are_separated(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        self.assertIn("1.98 crore in 1951", text)
        self.assertIn("10.38 crore in 2011", text)
        self.assertIn("17.3 crore in 2026", text)
        self.assertIn(
            "an enumerated figure and a projection are different objects",
            text,
        )

    def test_verified_pyq_ownership_is_solved_and_divided(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        workbook = workbook_markdown(generator, "social-justice-12")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(1, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertEqual(1, text.count("### PYQ DEMAND CARD"))
        self.assertIn(
            "### PYQ DEMAND CARD 1 — 2020 General Studies Paper II",
            text,
        )
        self.assertIn(
            "the maternal limb as belonging to the health-systems owner",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn("Health policies for geriatric and maternal care", text)

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn(
            "socialjustice.gov.in/schemes/43",
            generator.TOPICS[0]["live_sources"][0],
        )
        self.assertIn("2 September 2026", text)
        self.assertIn("promoting the silver economy", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-12")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Old-age dependency ratio",
            "Active ageing",
            "Formal vs informal care",
            "Health-system disconnect",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-12"),
            topic_key="social-justice-12",
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
