"""Regression tests for Social Justice learner-v2 Topic 13."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_13_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice13GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-13"],
            ["Transgender Persons and Denotified/Nomadic Communities"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-12"]', source)

    def test_recognitive_justice_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        for phrase in (
            "Transgender Persons (Protection of Rights) Act, 2019",
            "NALSA v. Union of India",
            "Section 7",
            "National Council for Transgender Persons",
            "Garima Greh",
            "Criminal Tribes Act, 1871",
            "Renke Commission",
            "Idate Commission",
            "Bhiku Ramji Idate",
            "DWBDNC",
            "SEED",
        ):
            self.assertIn(phrase, text)

    def test_certificate_routes_are_never_merged(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        self.assertIn(
            "no medical or surgical requirement applies to it",
            text,
        )
        self.assertIn(
            "an additional route and not a precondition for basic recognition",
            text,
        )
        self.assertIn("self-perceived transgender identity", text)

    def test_judgment_and_statute_are_kept_apart(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        self.assertIn("Articles 14, 15 and 21", text)
        self.assertIn("the 2019 Act did not fully adopt that direction", text)
        self.assertIn(
            "no uniform national horizontal-reservation rule be invented",
            text,
        )

    def test_denotification_is_not_presented_as_exoneration(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        self.assertIn("repealed in 1952", text)
        self.assertIn(
            "did not provide rehabilitation and did not remove social stigma",
            text,
        )
        self.assertIn("registration, surveillance and restriction of movement", text)

    def test_board_is_not_upgraded_into_a_statutory_commission(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        self.assertIn("21 February 2019", text)
        self.assertIn("it is not a statutory commission with quasi-judicial powers", text)
        self.assertIn("has not been enacted", text)

    def test_dated_scheme_and_counting_boundaries_are_carried(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        self.assertIn("16 February 2022", text)
        self.assertIn("4,87,803", text)
        self.assertIn(
            "no unsourced all-India population or community total should be used",
            text,
        )

    def test_transparent_zero_pyq_ownership_is_stated(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        workbook = workbook_markdown(generator, "social-justice-13")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertIn("route no General Studies question to this owner", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_no_live_source_is_claimed_for_this_owner(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        self.assertEqual([], generator.TOPICS[0]["live_sources"])
        self.assertIn(
            "No live official page was verified for this topic on 2026-09-02",
            text,
        )

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-13")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "DM-certificate bottleneck",
            "No statutory central list",
            "Advisory body vs statutory commission",
            "Visible vs invisible minorities",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-13"),
            topic_key="social-justice-13",
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
