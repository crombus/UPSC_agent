"""Regression tests for Social Justice learner-v2 Topic 16."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_16_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice16GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-16"],
            ["Urban Poor, Homeless and Migrant Workers"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-15"]', source)

    def test_urban_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-16")
        for phrase in (
            "DAY-NULM",
            "Shelter for Urban Homeless",
            "PM SVANidhi",
            "Street Vendors (Protection of Livelihood and Regulation of Street Vending) Act, 2014",
            "Town Vending Committees",
            "ONORC",
            "ePoS",
            "PMAY-U 2.0",
            "OSHWC",
            "Special Purpose Vehicle",
        ):
            self.assertIn(phrase, text)

    def test_urban_and_rural_missions_are_not_merged(self) -> None:
        text = session_markdown(generator, "social-justice-16")
        self.assertIn("DAY-NRLM", text)
        self.assertIn(
            "the similarly branded rural livelihoods mission belongs to the "
            "rural development ministry",
            text,
        )
        self.assertIn("60:40", text)
        self.assertIn("90:10", text)

    def test_credit_is_not_confused_with_the_right_to_vend(self) -> None:
        text = session_markdown(generator, "social-justice-16")
        self.assertIn("ten thousand, twenty thousand and fifty thousand rupees", text)
        self.assertIn("these are loans and not grants", text)
        self.assertIn("procedural safeguards against eviction", text)

    def test_verified_official_eligibility_condition_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-16")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn("pmsvanidhi.mohua.gov.in", generator.TOPICS[0]["live_sources"][0])
        self.assertIn("2 September 2026", text)
        self.assertIn(
            "only those States and Union Territories which have notified rules "
            "and scheme under the Street Vendors",
            text,
        )

    def test_portability_and_migrant_law_status_are_exact(self) -> None:
        text = session_markdown(generator, "social-justice-16")
        self.assertIn("21 November 2025", text)
        self.assertIn("repealed the Inter-State Migrant Workmen Act, 1979", text)
        self.assertIn(
            "portability mechanism within the existing food-security framework",
            text,
        )
        self.assertIn("rather than issuing a new one", text)

    def test_scale_anchor_is_bounded_by_its_exclusions(self) -> None:
        text = session_markdown(generator, "social-justice-16")
        self.assertIn("65.5 million", text)
        self.assertIn("17.4", text)
        self.assertIn(
            "does not include every informal renter, every homeless person or "
            "every unnotified settlement",
            text,
        )

    def test_cross_paper_questions_are_routed_away_from_this_owner(self) -> None:
        text = session_markdown(generator, "social-justice-16")
        workbook = workbook_markdown(generator, "social-justice-16")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertIn("to the Geography migration-theories-and-patterns owner", text)
        self.assertIn("to the Indian Society urbanisation owner", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-16")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "In-situ slum upgrading vs resettlement",
            "Tenure security vs title",
            "Agglomeration economies",
            "Area-based vs pan-city smart-city model",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-16"),
            topic_key="social-justice-16",
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
