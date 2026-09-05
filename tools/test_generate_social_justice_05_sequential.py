"""Regression tests for Social Justice learner-v2 Topic 05."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_05_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice05GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-05"],
            ["Women and Gender Justice"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-04"]', source)

    def test_gender_justice_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        for phrase in (
            "Protection of Women from Domestic Violence Act, 2005",
            "protection order",
            "residence order",
            "Protection Officer",
            "Section 31",
            "relationship in the nature of marriage",
            "Internal Committee",
            "Local Committee",
            "District Officer",
            "Mission Shakti",
            "Sambal",
            "Samarthya",
            "Maternity Benefit Act",
            "National Commission for Women Act, 1990",
            "Gender Budget Statement",
        ):
            self.assertIn(phrase, text)

    def test_statutory_and_constitutional_status_are_kept_apart(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        self.assertIn("Article 338A", text)
        self.assertIn(
            "the National Commission for Women is a statutory body created by "
            "ordinary legislation",
            text,
        )
        self.assertIn("recommends rather than enforces", text)

    def test_maternity_entitlement_and_transfer_are_not_merged(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        self.assertIn("26 weeks", text)
        self.assertIn("5,000 rupees", text)
        self.assertIn("6,000 rupees", text)
        self.assertIn(
            "creates no leave entitlement binding on any employer",
            text,
        )

    def test_survey_values_carry_round_and_scope(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        for phrase in ("78.6", "54.0", "20.1", "23.3", "29 May 2026"):
            self.assertIn(phrase, text)
        self.assertIn(
            "must be cited separately rather than mixed with the fifth round",
            text,
        )

    def test_representation_sequencing_is_not_upgraded(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        self.assertIn("106th Amendment", text)
        self.assertIn("Article 334A", text)
        self.assertIn(
            "numerical presence does not by itself defeat proxy control",
            text,
        )

    def test_verified_pyq_ownership_and_cross_routing(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        workbook = workbook_markdown(generator, "social-justice-05")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(7, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(7, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2019 General Studies Paper II Question 13",
            "2020 General Studies Paper II Question 15",
            "2021 General Studies Paper II Question 2",
            "2021 General Studies Paper II Question 17",
            "2023 General Studies Paper II Question 12",
            "2023 General Studies Paper II Question 14",
            "2025 General Studies Paper II Question 6",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "routes that question to the Indian Society owner, so no demand card "
            "is manufactured for it here",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn(
            "Maternity Benefit Amendment Act 2017 key provisions",
            text,
        )

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn("wcd.gov.in", generator.TOPICS[0]["live_sources"][0])
        self.assertIn("30 January 2006", text)
        self.assertIn("nothing further has been inferred from it", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-05")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Protection order vs residence order",
            "Internal Committee vs Local Committee",
            "Gender Budget Statement — allocation vs outcome",
            "Statutory body vs constitutional body",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-05"),
            topic_key="social-justice-05",
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
