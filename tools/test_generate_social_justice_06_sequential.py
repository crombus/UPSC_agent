"""Regression tests for Social Justice learner-v2 Topic 06."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_06_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice06GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-06"],
            ["Children and Child Protection"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-05"]', source)

    def test_child_protection_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        for phrase in (
            "Protection of Children from Sexual Offences Act, 2012",
            "Juvenile Justice Board",
            "Child Welfare Committee",
            "heinous offence",
            "Section 15",
            "Section 18(3)",
            "Children's Court",
            "Child Labour (Prohibition and Regulation) Amendment Act, 2016",
            "Prohibition of Child Marriage Act, 2006",
            "Child Marriage Prohibition Officer",
            "Mission Vatsalya",
            "1098",
            "Commissions for Protection of Child Rights Act, 2005",
            "e-Box",
        ):
            self.assertIn(phrase, text)

    def test_age_thresholds_are_kept_apart_by_statute(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        self.assertIn(
            "employment of a child below fourteen years is completely prohibited",
            text,
        )
        self.assertIn(
            "prohibited only from hazardous occupations and processes listed in "
            "the Schedule",
            text,
        )
        self.assertIn("gender-neutral", text)

    def test_transfer_gateway_is_not_described_as_automatic(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        self.assertIn(
            "adult treatment is therefore exceptional and never automatic",
            text.replace("Adult", "adult"),
        )
        self.assertIn("minimum punishment under the general penal law is "
                      "imprisonment of seven years or more", text)

    def test_marriage_validity_distinction_is_exact(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        self.assertIn("voidable", text)
        self.assertIn(
            "a voidable marriage stands until the party who was a child elects "
            "to avoid it",
            text,
        )

    def test_scheduled_data_regime_is_not_upgraded(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        self.assertIn("13 May 2027", text)
        self.assertIn("21 July 2026", text)
        self.assertIn(
            "a notified future compliance framework and not current enforcement",
            text,
        )

    def test_dated_anchors_carry_their_source(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        for phrase in ("20.1", "23.3", "10.1 million"):
            self.assertIn(phrase, text)
        self.assertIn(
            "does not capture every hidden, unpaid or hazardous form of child "
            "work",
            text,
        )

    def test_verified_pyq_ownership_and_cross_routing(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        workbook = workbook_markdown(generator, "social-justice-06")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(1, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(1, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("2025 General Studies Paper II Question 18", text)
        self.assertIn("2018 Prelims General Studies Paper I Question 30", text)
        self.assertIn(
            "records the official keys for that period as not held locally",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn("ILO Conventions 138 and 182 subject matter", text)

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn("wcd.gov.in", generator.TOPICS[0]["live_sources"][0])
        self.assertIn("30 January 2006", text)
        self.assertIn("nothing further has been inferred from it", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-06")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Preliminary assessment (JJ Act)",
            "Intermediary obligations (IT Rules)",
            "NCPCR vs SCPCR",
            "Online grooming",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-06"),
            topic_key="social-justice-06",
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
