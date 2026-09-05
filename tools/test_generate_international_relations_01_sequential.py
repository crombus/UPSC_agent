"""Regression tests for International Relations learner-v2 Topic 01."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_01_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_honesty,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations01GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-01"],
            ["Foreign-Policy Foundations and Strategic Autonomy"],
        )

    def test_this_is_the_first_topic_of_the_sequence(self) -> None:
        self.assertIsNone(generator.main.__defaults__)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=None", source)
        self.assertIn("previous_keys=None", source)

    def test_doctrinal_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "international-relations-01")
        for phrase in (
            "non-alignment",
            "strategic autonomy",
            "multi-alignment",
            "Panchsheel",
            "hedging",
            "bandwagoning",
            "balancing",
            "issue-based coalition",
            "minilateral",
            "autonomy-dependence trade-off",
            "Bipan Chandra",
            "Sikri",
            "Tharoor",
        ):
            self.assertIn(phrase, text)

    def test_doctrine_dates_and_status_are_exact(self) -> None:
        text = session_markdown(generator, "international-relations-01")
        for phrase in (
            "29 April 1954",
            "12 March 2015",
            "12 March 2025",
            "17 August 2024",
            "12 to 13 January 2023",
            "17 November 2023",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "both are declared visions and not treaties",
            text,
        )
        self.assertIn("MAHASAGAR did not replace or supersede SAGAR", text)

    def test_dated_stress_test_is_carried_as_reversible(self) -> None:
        text = session_markdown(generator, "international-relations-01")
        for phrase in (
            "took effect on 27 August 2025",
            "removed from 7 February 2026",
            "4 and 5 December 2025",
            "31 October 2025",
            "unjustified and unreasonable",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "exposure and secondary risk rather than a binding international-law "
            "duty on India",
            text,
        )

    def test_dependence_figures_carry_body_year_and_status(self) -> None:
        text = session_markdown(generator, "international-relations-01")
        self.assertIn("Petroleum Planning and Analysis Cell", text)
        self.assertIn("88.2 per cent", text)
        self.assertIn("about 88.7 per cent provisional", text)
        self.assertIn(
            "carried with its issuing body, financial year and provisional status",
            text,
        )

    def test_objective_only_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-01")
        workbook = workbook_markdown(generator, "international-relations-01")
        self.assertIn("VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertIn("2024 Prelims General Studies Paper I, question 86", text)
        self.assertIn("no option or answer is recorded or inferred", text)
        self.assertIn(
            "no General Studies Paper II Mains question in the audited "
            "2024-2025 papers directly names strategic autonomy",
            text,
        )
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_honesty(self, generator, "international-relations-01")

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-01")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Non-alignment as method, not blueprint",
            "Hedging vs. bandwagoning vs. balancing",
            "Co-option vs. autonomous positioning",
            "Issue-based coalition vs. alliance",
            "NAM's declining institutional salience",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-01"),
            topic_key="international-relations-01",
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
