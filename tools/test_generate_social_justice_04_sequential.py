"""Regression tests for Social Justice learner-v2 Topic 04."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_04_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice04GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-04"],
            ["Education and Human-Resource Development"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-03"]', source)

    def test_education_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-04")
        for phrase in (
            "Article 21-A",
            "Right of Children to Free and Compulsory Education Act, 2009",
            "National Education Policy, 2020",
            "Samagra Shiksha",
            "foundational literacy and numeracy",
            "gross enrolment ratio",
            "Academic Bank of Credits",
            "NCVET",
            "NAPS",
            "NSQF",
            "DIKSHA",
            "SWAYAM",
        ):
            self.assertIn(phrase, text)

    def test_statutory_and_policy_status_are_kept_apart(self) -> None:
        text = session_markdown(generator, "social-justice-04")
        self.assertIn("Eighty-sixth Amendment of 2002", text)
        self.assertIn(
            "is a policy document and not a statute",
            text,
        )
        self.assertIn(
            "its extension of focus to early childhood care and education creates "
            "no statutory entitlement",
            text,
        )

    def test_survey_values_carry_round_and_scope(self) -> None:
        text = session_markdown(generator, "social-justice-04")
        for phrase in ("28.4", "27.3", "28.5", "2021-22", "23.4 per cent"):
            self.assertIn(phrase, text)
        self.assertIn(
            "must not be silently generalised to urban India",
            text,
        )
        self.assertIn("2026-27", text)

    def test_regulatory_status_is_not_upgraded(self) -> None:
        text = session_markdown(generator, "social-justice-04")
        self.assertIn("approved by the Cabinet in December 2025", text)
        self.assertIn(
            "as of mid-2026 it has not been enacted",
            text,
        )

    def test_verified_pyq_ownership_and_cross_routing(self) -> None:
        text = session_markdown(generator, "social-justice-04")
        workbook = workbook_markdown(generator, "social-justice-04")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(6, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(6, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2020 General Studies Paper I Question 20",
            "2020 General Studies Paper II Question 18",
            "2021 General Studies Paper II Question 7",
            "2022 General Studies Paper II Question 18",
            "2023 General Studies Paper II Question 6",
            "2023 General Studies Paper II Question 18",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "routes that question to the Governance owner, so no demand card is "
            "manufactured for it here",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-04")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn(
            "Right to Education Act teacher qualification eligibility provisions",
            text,
        )

    def test_no_live_source_is_claimed_and_refusals_are_recorded(self) -> None:
        text = session_markdown(generator, "social-justice-04")
        self.assertEqual([], generator.TOPICS[0]["live_sources"])
        self.assertIn(
            "No live official page was verified for this topic on 2026-09-02",
            text,
        )
        self.assertIn("all three were refused with an access error", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-04")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "No-detention policy (RTE 2009) and its amendment",
            "Learning poverty",
            "Academic Bank of Credits (ABC)",
            "Skill-qualification framework",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-04"),
            topic_key="social-justice-04",
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
