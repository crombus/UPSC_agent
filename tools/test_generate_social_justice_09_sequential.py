"""Regression tests for Social Justice learner-v2 Topic 09."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_09_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice09GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-09"],
            ["OBC, EWS and Social Mobility"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-08"]', source)

    def test_backward_class_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-09")
        for phrase in (
            "Article 342A",
            "Article 338B",
            "Article 15(6)",
            "Article 16(6)",
            "Indra Sawhney",
            "Janhit Abhiyan",
            "creamy layer",
            "Rohini Commission",
            "PM-YASASVI",
            "SECC 2011",
            "105th",
        ):
            self.assertIn(phrase, text)

    def test_the_two_routes_are_kept_constitutionally_distinct(self) -> None:
        text = session_markdown(generator, "social-justice-09")
        self.assertIn(
            "two constitutionally distinct routes and must never be merged",
            text,
        )
        self.assertIn(
            "the category is defined negatively as well as economically",
            text,
        )

    def test_identical_rupee_figures_are_separated_as_two_tests(self) -> None:
        text = session_markdown(generator, "social-justice-09")
        self.assertIn("September 2017", text)
        self.assertIn("31 January 2019", text)
        self.assertIn(
            "identical arithmetic therefore proves nothing about identical "
            "eligibility",
            text,
        )
        for asset in ("five acres", "1,000 sq ft", "100 sq yards", "200 sq yards"):
            self.assertIn(asset, text)

    def test_the_2022_majority_and_dissent_are_both_recorded(self) -> None:
        text = session_markdown(generator, "social-justice-09")
        self.assertIn("majority of three to two", text)
        self.assertIn("the dissent argued", text)

    def test_census_decision_is_not_presented_as_data(self) -> None:
        text = session_markdown(generator, "social-justice-09")
        self.assertIn("30 April 2025", text)
        self.assertIn("1 April to 30 September 2026", text)
        self.assertIn(
            "an approved and ongoing operation and not published caste data",
            text,
        )
        self.assertIn("1931", text)

    def test_transparent_zero_pyq_ownership_is_declared(self) -> None:
        text = session_markdown(generator, "social-justice-09")
        workbook = workbook_markdown(generator, "social-justice-09")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertIn(
            "routes both to the Polity commissions owner",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-09")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn("ncbc.nic.in", generator.TOPICS[0]["live_sources"][0])
        self.assertIn("2 September 2026", text)
        self.assertIn("2 April 1993", text)
        self.assertIn("14 August 2018", text)
        self.assertIn("Chairperson, a Vice-Chairperson and three other Members", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-09")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "identification paradox",
            "Sub-categorisation within OBCs",
            "Creamy-layer threshold lag",
            "Data blindness",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-09"),
            topic_key="social-justice-09",
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
