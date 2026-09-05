"""Regression tests for Social Justice learner-v2 Topic 08."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_08_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice08GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-08"],
            ["Scheduled Tribes, PVTGs and Tribal Welfare"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-07"]', source)

    def test_tribal_welfare_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        for phrase in (
            "individual forest rights",
            "community forest resource rights",
            "minor forest produce",
            "four hectares",
            "Section 4(2)",
            "critical wildlife habitat",
            "Scheduled Areas",
            "Van Dhan Vikas Kendra",
            "Eklavya Model Residential School",
            "Article 338A",
            "Chotanagpur Tenancy Act",
            "Samatha",
            "Niyamgiri",
            "Xaxa Committee",
        ):
            self.assertIn(phrase, text)

    def test_three_rights_categories_are_named_separately(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        self.assertIn(
            "recognises three categories that must be named separately",
            text,
        )
        self.assertIn("heritable, so it passes within the family", text)
        self.assertIn("not transferable or alienable", text)

    def test_rejection_is_not_treated_as_eviction_authority(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        self.assertIn(
            "rejection of a claim does not erase due-process duties or justify "
            "automatic eviction",
            text,
        )
        self.assertIn("was stayed", text)

    def test_protected_area_safeguards_are_cumulative(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        self.assertIn("free informed consent of the Gram Sabha", text)
        self.assertIn("this is not a general relocation power", text)

    def test_vulnerable_group_category_is_not_generalised(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        self.assertIn("seventy-five", text)
        self.assertIn("15 November 2023", text)
        self.assertIn("eighteen States", text)
        self.assertIn(
            "must not be described as a universal tribal-welfare scheme",
            text,
        )
        self.assertIn(
            "not all Scheduled Tribes are such groups",
            text,
        )

    def test_transparent_pyq_ownership_for_objective_only_routing(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        workbook = workbook_markdown(generator, "social-justice-08")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertIn("2019 Prelims General Studies Paper I Question 51", text)
        self.assertIn("2021 Prelims General Studies Paper I Question 84", text)
        self.assertIn(
            "routes that question to the Indian Society owner",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn(
            "Particularly Vulnerable Tribal Groups PVTGs criteria India",
            text,
        )
        self.assertIn("Nodal ministry for Forest Rights Act 2006", text)

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn("tribal.nic.in", generator.TOPICS[0]["live_sources"][0])
        self.assertIn("2 September 2026", text)
        self.assertIn("undo the historical injustice", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-08")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "PVTG criteria",
            "FRA rejection vs eviction",
            "Land alienation",
            "R&R policy",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-08"),
            topic_key="social-justice-08",
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
