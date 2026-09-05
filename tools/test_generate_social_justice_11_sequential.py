"""Regression tests for Social Justice learner-v2 Topic 11."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_11_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice11GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-11"],
            ["Persons with Disabilities"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-10"]', source)

    def test_disability_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-11")
        for phrase in (
            "Section 2(y)",
            "benchmark disability",
            "Unique Disability Identity",
            "Chief Commissioner for Persons with Disabilities",
            "universal design",
            "retrofitting",
            "Vikash Kumar",
            "Jeeja Ghosh",
            "thalassaemia",
            "deafblindness",
            "March 2024",
        ):
            self.assertIn(phrase, text)

    def test_statutory_reservation_is_not_filed_under_article_16(self) -> None:
        text = session_markdown(generator, "social-justice-11")
        self.assertIn(
            "statutory reservation created by ordinary legislation and not the "
            "constitutional mechanism of Article 16(4)",
            text,
        )
        self.assertIn("four per cent", text)
        self.assertIn("five per cent", text)

    def test_accommodation_carries_both_limbs(self) -> None:
        text = session_markdown(generator, "social-justice-11")
        self.assertIn("not imposing a disproportionate or undue burden", text)
        self.assertIn(
            "denial of reasonable accommodation is expressly recognised as a "
            "form of discrimination",
            text,
        )

    def test_trust_statute_scope_mismatch_is_stated(self) -> None:
        text = session_markdown(generator, "social-justice-11")
        self.assertIn("covers only those four conditions", text)
        self.assertIn(
            "is neither the regulator nor the accessibility mission",
            text,
        )

    def test_verified_pyq_ownership_is_solved_and_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-11")
        workbook = workbook_markdown(generator, "social-justice-11")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(1, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertEqual(1, text.count("### PYQ DEMAND CARD"))
        self.assertIn(
            "### PYQ DEMAND CARD 1 — 2022 General Studies Paper II",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn(
            "question 56 of the 2026 Prelims General Studies Paper I",
            text,
        )
        self.assertIn("locally held 2026 Set-A key is provisional", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-11")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn(
            "Rights of Persons with Disabilities Act 2016 and sensitisation",
            text,
        )

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-11")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn("depwd.gov.in", generator.TOPICS[0]["live_sources"][0])
        self.assertIn("2 September 2026", text)
        self.assertIn("2.68 crore", text)
        self.assertIn("2.21 per cent", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-11")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Benchmark rigidity",
            "National Trust scope mismatch",
            "Retrofitting cost",
            "Private-sector coverage",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-11"),
            topic_key="social-justice-11",
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
