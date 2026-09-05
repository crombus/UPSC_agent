"""Regression tests for Social Justice learner-v2 Topic 02."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_02_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice02GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-02"],
            ["Poverty, Hunger, Food and Nutrition Security"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-01"]', source)

    def test_entitlement_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-02")
        for phrase in (
            "National Food Security Act, 2013",
            "Antyodaya Anna Yojana",
            "Central Issue Price",
            "One Nation One Ration Card",
            "Poshan 2.0",
            "PM POSHAN",
            "Food Security Allowance Rules, 2015",
            "take-home ration",
            "hot cooked meal",
            "Anaemia Mukt Bharat",
            "nutrition-sensitive",
            "first thousand days",
        ):
            self.assertIn(phrase, text)

    def test_price_and_policy_status_are_kept_apart(self) -> None:
        text = session_markdown(generator, "social-justice-02")
        self.assertIn(
            "three rupees per kilogram for rice, two rupees per kilogram for wheat "
            "and one rupee per kilogram for coarse grains",
            text,
        )
        self.assertIn("since 1 January 2023", text)
        self.assertIn("through December 2028", text)
        self.assertIn(
            "the statutory ceiling and the current distribution policy are two "
            "different facts",
            text,
        )

    def test_official_coverage_facts_are_dated_and_attributed(self) -> None:
        text = session_markdown(generator, "social-justice-02")
        self.assertIn("read on 2 September 2026", text)
        self.assertIn("enacted on 5 July 2013", text)
        self.assertIn("81.34 crore persons", text)
        self.assertIn("not less than six thousand rupees", text)

    def test_survey_rounds_are_never_merged(self) -> None:
        text = session_markdown(generator, "social-justice-02")
        self.assertIn("35.5 per cent", text)
        self.assertIn("29.3 per cent", text)
        self.assertIn("29 May 2026", text)
        self.assertIn("715 districts", text)
        self.assertIn(
            "indicators from the two rounds must never be combined without naming "
            "each round",
            text,
        )

    def test_verified_pyq_ownership_and_unavailable_keys(self) -> None:
        text = session_markdown(generator, "social-justice-02")
        workbook = workbook_markdown(generator, "social-justice-02")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(3, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2018 General Studies Paper II Question 17",
            "2019 General Studies Paper II Question 7",
            "2024 General Studies Paper II Question 7",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the official 2018-2023 Prelims keys are not held locally, so no option, "
            "key or inferred answer is recorded",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-02")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn(
            "Poverty-malnutrition vicious cycle and human-capital formation",
            text,
        )

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-02")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Nutrition-specific interventions",
            "Nutrition-sensitive interventions",
            "Severe Acute Malnutrition (SAM) vs Moderate Acute Malnutrition (MAM)",
            "Take-home ration (THR) vs hot cooked meal (HCM)",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-02"),
            topic_key="social-justice-02",
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
