"""Regression tests for Social Justice learner-v2 Topic 10."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_10_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice10GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-10"],
            ["Minorities: Rights and Welfare"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-09"]', source)

    def test_minority_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-10")
        for phrase in (
            "Section 2(c)",
            "Article 29",
            "Article 30",
            "Article 350A",
            "Article 350B",
            "TMA Pai Foundation",
            "National Commission for Minority Educational Institutions Act, 2004",
            "PM VIKAS",
            "PMJVK",
            "Central Waqf Council",
            "Sachar",
        ):
            self.assertIn(phrase, text)

    def test_statutory_status_is_not_upgraded(self) -> None:
        text = session_markdown(generator, "social-justice-10")
        self.assertIn(
            "it is therefore a statutory body created by ordinary legislation",
            text,
        )
        self.assertIn(
            "Chairperson, a Vice-Chairperson and five Members",
            text,
        )
        self.assertIn("advisory rather than self-executing orders", text)

    def test_state_level_minority_determination_is_recorded(self) -> None:
        text = session_markdown(generator, "social-justice-10")
        self.assertIn(
            "determined at the State level rather than at the national level",
            text,
        )
        self.assertIn("both religious and linguistic minorities", text)

    def test_the_interim_order_is_reported_provision_by_provision(self) -> None:
        text = session_markdown(generator, "social-justice-10")
        self.assertIn("5 April 2025", text)
        self.assertIn("15 September 2025", text)
        self.assertIn("declined to stay the Act in its entirety", text)
        self.assertIn("five years of practising Islam", text)
        self.assertIn("four out of twenty-two", text)
        self.assertIn("three out of eleven", text)
        self.assertIn(
            "did not stay the prospective abolition of waqf by user",
            text,
        )
        self.assertIn("remain pending final adjudication", text)

    def test_umbrella_scheme_is_not_collapsed_into_area_targeting(self) -> None:
        text = session_markdown(generator, "social-justice-10")
        for phrase in (
            "Seekho aur Kamao",
            "USTTAD",
            "Hamari Dharohar",
            "Nai Roshni",
            "Nai Manzil",
            "Fifteenth Finance Commission",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "it is not the area-infrastructure programme for "
            "minority-concentration areas",
            text,
        )

    def test_transparent_zero_pyq_ownership_is_declared(self) -> None:
        text = session_markdown(generator, "social-justice-10")
        workbook = workbook_markdown(generator, "social-justice-10")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertIn("routes it to the Polity commissions owner", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-10")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn(
            "pmvikas.minorityaffairs.gov.in",
            generator.TOPICS[0]["live_sources"][0],
        )
        self.assertIn("2 September 2026", text)
        self.assertIn("Sustainable Development Goals 1, 5, 8 and 10", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-10")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Waqf by user vs waqf by deed",
            "Scheme targeting vs stigma",
            "Outcome measurement gap",
            "advisory-only mandate",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-10"),
            topic_key="social-justice-10",
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
