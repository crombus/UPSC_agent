"""Regression tests for International Relations learner-v2 Topic 02."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_02_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_honesty,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations02GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-02"],
            ["India and the Neighbourhood"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-01"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_doctrinal_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "international-relations-02")
        for phrase in (
            "Neighbourhood First",
            "Gujral Doctrine",
            "non-reciprocal",
            "near-neighbour",
            "regional framework",
            "people-to-people",
            "implementation-credibility",
        ):
            self.assertIn(phrase, text)

    def test_connectivity_evidence_is_dated_and_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-02")
        for phrase in (
            "Akhaura-Agartala",
            "1 November 2023",
            "Motor Vehicles Agreement",
            "Mangdechhu",
            "Sittwe Port",
            "1 June 2026",
            "5 April 2025",
            "25 July 2025",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "Bhutan's non-ratification has constrained four-country implementation",
            text,
        )
        self.assertIn("ground-breaking rather than its commissioning", text)

    def test_status_distinctions_are_never_upgraded(self) -> None:
        text = session_markdown(generator, "international-relations-02")
        self.assertIn(
            "expressly not treaty termination and not a formal ceasefire agreement",
            text,
        )
        self.assertIn(
            "the official record contains no recognition declaration",
            text,
        )
        self.assertIn("held in abeyance with immediate effect", text)
        self.assertIn("21 October 2025", text)
        self.assertIn("no free trade agreement has been concluded", text)

    def test_crisis_assistance_is_time_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-02")
        self.assertIn("By 3 May 2022", text)
        self.assertIn("more than three billion United States dollars", text)
        self.assertIn("around four billion dollars over 2022", text)
        self.assertIn(
            "emergency financing did not remove Sri Lanka's structural debt",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-02")
        workbook = workbook_markdown(generator, "international-relations-02")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(1, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(1, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("2022 General Studies Paper II Question 9", text)
        self.assertIn("2020 Prelims General Studies Paper I question 64", text)
        self.assertIn("2023 Prelims General Studies Paper I question 10", text)
        self.assertIn("2026 Prelims General Studies Paper I questions 61 and 67", text)
        self.assertIn(
            "No option or answer letter is recorded or inferred for any objective demand",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_honesty(self, generator, "international-relations-02")

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-02")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Regional-framework preference (Sikri)",
            "Extra-regional power involvement as a constraint",
            "Historical influence vs. present-day interventionism",
            "Water as the hardest case for non-reciprocity",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-02"),
            topic_key="international-relations-02",
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
