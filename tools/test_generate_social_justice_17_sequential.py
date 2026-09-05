"""Regression tests for Social Justice learner-v2 Topic 17."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_17_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice17GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-17"],
            ["Scheme Performance, Convergence, Targeting and Data"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-16"]', source)

    def test_capstone_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        for phrase in (
            "NSAP",
            "IGNOAPS",
            "IGNWPS",
            "IGNDPS",
            "NFBS",
            "Annapurna",
            "SECC 2011",
            "DMEO",
            "OOMF",
            "PM-JANMAN",
            "Puttaswamy",
            "Economic Survey 2025-26",
        ):
            self.assertIn(phrase, text)

    def test_targeting_errors_are_defined_in_the_right_direction(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        self.assertIn(
            "inclusion error, also called Type I error, as the inclusion of "
            "ineligible beneficiaries",
            text,
        )
        self.assertIn(
            "exclusion error, also called Type II error, as the exclusion of "
            "eligible beneficiaries",
            text,
        )

    def test_survey_round_discipline_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        self.assertIn("29 May 2026", text)
        self.assertIn("29.3", text)
        self.assertIn("35.5", text)
        self.assertIn(
            "the round travel with every indicator and that values from two "
            "rounds never be silently merged",
            text,
        )

    def test_pending_caste_enumeration_is_not_presented_as_a_database(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        self.assertIn("30 April 2025", text)
        self.assertIn("1 April to 30 September 2026", text)
        self.assertIn(
            "an ongoing operation rather than a published database or a "
            "ready-made targeting list",
            text,
        )

    def test_transfer_evidence_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        self.assertIn(
            "improve short-term consumption and food security without "
            "consistently improving child nutrition",
            text,
        )
        self.assertIn(
            "supports a convergence argument and does not support a claim that "
            "transfer coverage alone proves social-sector success",
            text,
        )

    def test_two_verified_pyq_demands_are_solved(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        workbook = workbook_markdown(generator, "social-justice-17")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(2, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertEqual(2, text.count("### PYQ DEMAND CARD"))
        self.assertIn("### PYQ DEMAND CARD 1 — 2019 General Studies Paper II", text)
        self.assertIn("### PYQ DEMAND CARD 2 — 2023 General Studies Paper II", text)
        self.assertEqual(2, text.count("Why this earns marks"))
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn(
            "Welfare schemes for vulnerable sections and awareness and involvement",
            text,
        )
        self.assertIn(
            "Development and welfare schemes for the vulnerable as discriminatory",
            text,
        )

    def test_no_live_source_is_claimed_for_this_owner(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        self.assertEqual([], generator.TOPICS[0]["live_sources"])
        self.assertIn(
            "No live official page was verified for this topic on 2026-09-02",
            text,
        )

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-17")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Universalism-targeting trade-off",
            "Horizontal vs vertical convergence",
            "Data-architecture gap",
            "Proxy-means-testing limits",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-17"),
            topic_key="social-justice-17",
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
