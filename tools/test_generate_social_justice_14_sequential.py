"""Regression tests for Social Justice learner-v2 Topic 14."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_14_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice14GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-14"],
            ["Sanitation, Manual Scavenging and Safai Karamcharis"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-13"]', source)

    def test_sanitation_labour_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-14")
        for phrase in (
            "Prohibition of Employment as Manual Scavengers and their Rehabilitation Act, 2013",
            "hazardous cleaning",
            "insanitary latrine",
            "Safai Karamchari Andolan",
            "Dr Balram Singh",
            "NAMASTE",
            "NCSK",
            "World Toilet Organization",
        ):
            self.assertIn(phrase, text)

    def test_two_prohibited_practices_are_never_merged(self) -> None:
        text = session_markdown(generator, "social-justice-14")
        self.assertIn(
            "protective equipment does not turn manual scavenging into a lawful practice",
            text,
        )
        self.assertIn(
            "without the prescribed protective gear, cleaning devices and safety precautions",
            text,
        )
        self.assertIn("requiring human intervention for the removal of excreta", text)

    def test_compensation_tiers_travel_with_their_judicial_source(self) -> None:
        text = session_markdown(generator, "social-justice-14")
        self.assertIn("20 October 2023", text)
        self.assertIn("thirty lakh rupees", text)
        self.assertIn("at least twenty lakh rupees for permanent disability", text)
        self.assertIn(
            "judicial directions and not a statutory schedule",
            text,
        )

    def test_commission_status_is_stated_with_its_verified_history(self) -> None:
        text = session_markdown(generator, "social-justice-14")
        self.assertIn("12 August 1994", text)
        self.assertIn("31 March 1997", text)
        self.assertIn("February 2004", text)
        self.assertIn("31 March 2028", text)
        self.assertIn("Articles 338 and 338A", text)

    def test_mechanisation_is_not_presented_as_substitution(self) -> None:
        text = session_markdown(generator, "social-justice-14")
        self.assertIn("2022-23", text)
        self.assertIn(
            "mechanisation which merely adds protective equipment while still "
            "requiring human entry does not eliminate the hazard",
            text,
        )
        self.assertIn("stores it unused for want of trained operators", text)

    def test_verified_objective_ownership_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-14")
        workbook = workbook_markdown(generator, "social-justice-14")
        self.assertIn("VERIFIED OBJECTIVE-DEMAND OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED OBJECTIVE-DEMAND OWNERSHIP AUDIT", workbook)
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertIn("question 24 of the 2024 Prelims General Studies Paper I", text)
        self.assertIn("no option, no key and no inferred answer letter", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-14")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn("ncsk.nic.in", generator.TOPICS[0]["live_sources"][0])
        self.assertIn("2 September 2026", text)
        self.assertIn("sub-section (4) of Section 1", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-14")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Prohibition vs abolition",
            "Rehabilitation vs reparation",
            "Survey under-count",
            "Worker-entrepreneur model gap",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-14"),
            topic_key="social-justice-14",
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
