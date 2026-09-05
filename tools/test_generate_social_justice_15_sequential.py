"""Regression tests for Social Justice learner-v2 Topic 15."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_15_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice15GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-15"],
            ["Labour Social Security, Unorganised and Gig Workers"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-14"]', source)

    def test_social_security_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        for phrase in (
            "Code on Social Security, 2020",
            "Section 114",
            "e-Shram",
            "PM-SYM",
            "BOCW",
            "EPFO",
            "ESIC",
            "Unorganised Workers' Social Security Act, 2008",
        ):
            self.assertIn(phrase, text)

    def test_commencement_status_is_stated_exactly(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        self.assertIn("commenced on 21 November 2025", text)
        self.assertIn("final Central Rules were notified in May 2026", text)
        self.assertIn("labour is a concurrent subject", text)

    def test_contribution_range_and_cap_travel_together(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        self.assertIn(
            "at least one per cent and not more than two per cent of an "
            "aggregator's annual turnover",
            text,
        )
        self.assertIn(
            "cap of five per cent of the amount paid or payable",
            text,
        )
        self.assertIn(
            "not evidence of a notified rate, a collection ledger, a fund "
            "balance or a paid claim",
            text,
        )

    def test_registration_is_not_presented_as_entitlement(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        self.assertIn(
            "delivery and convergence tool rather than an automatic pension",
            text,
        )
        self.assertIn("₹3,000", text)
        self.assertIn("three thousand rupees after the age of sixty", text)

    def test_invented_thresholds_are_expressly_refused(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        self.assertIn(
            "no ninety-day or one-hundred-and-twenty-day national eligibility "
            "rule may be asserted",
            text,
        )
        self.assertIn("7.7 million", text)
        self.assertIn("23.5 million", text)

    def test_verified_objective_ownership_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        workbook = workbook_markdown(generator, "social-justice-15")
        self.assertIn("VERIFIED OBJECTIVE-DEMAND OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED OBJECTIVE-DEMAND OWNERSHIP AUDIT", workbook)
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertIn("question 100 of the 2024 Prelims General Studies Paper I", text)
        self.assertIn("no option, key or inferred answer letter", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_labour_codes_mains_demand_is_not_claimed_here(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        self.assertIn(
            "is analysed in the Economy employment and labour-codes owner",
            text,
        )

    def test_no_live_source_is_claimed_for_this_owner(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        self.assertEqual([], generator.TOPICS[0]["live_sources"])
        self.assertIn(
            "No live official page was verified for this topic on 2026-09-02",
            text,
        )

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-15")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Portability vs interoperability",
            "Universal floor vs contributory top-up",
            "Platform-power failure chain",
            "Insurance-led bias",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-15"),
            topic_key="social-justice-15",
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
