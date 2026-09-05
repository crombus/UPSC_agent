"""Regression tests for Social Justice learner-v2 Topic 03."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_03_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice03GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-03"],
            ["Health Systems, Public Health and Universal Health Coverage"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-02"]', source)

    def test_health_system_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-03")
        for phrase in (
            "universal health coverage",
            "National Health Policy, 2017",
            "National Health Mission",
            "Ayushman Arogya Mandir",
            "Pradhan Mantri Jan Arogya Yojana",
            "National Health Authority",
            "National Health Accounts",
            "out-of-pocket expenditure",
            "catastrophic health expenditure",
            "Clinical Establishments Act, 2010",
            "Alma-Ata",
            "Mental Healthcare Act, 2017",
            "Indian Public Health Standards",
        ):
            self.assertIn(phrase, text)

    def test_mission_dates_are_official_and_dated(self) -> None:
        text = session_markdown(generator, "social-justice-03")
        self.assertIn("read on 2 September 2026", text)
        self.assertIn("12 April 2005", text)
        self.assertIn("decision dated 1 May 2013", text)
        self.assertIn(
            "the mission is urban as well as rural and treating it as rural-only "
            "is a factual error",
            text,
        )

    def test_two_enrolment_routes_are_not_conflated(self) -> None:
        text = session_markdown(generator, "social-justice-03")
        self.assertIn("five lakh rupees per family per year", text)
        self.assertIn("seventy years and above", text)
        self.assertIn(
            "an age-specific expansion must never be written up as universal "
            "coverage for every age",
            text,
        )

    def test_expenditure_series_carries_accounting_years(self) -> None:
        text = session_markdown(generator, "social-justice-03")
        for phrase in ("47.1 per cent", "44.4 per cent", "39.4 per cent", "2021-22"):
            self.assertIn(phrase, text)
        self.assertIn(
            "the publication date must never be confused with the accounting year",
            text,
        )

    def test_verified_pyq_ownership_and_key_discipline(self) -> None:
        text = session_markdown(generator, "social-justice-03")
        workbook = workbook_markdown(generator, "social-justice-03")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2018 General Studies Paper II Question 7",
            "2020 General Studies Paper II Question 6",
            "2021 General Studies Paper II Question 6",
            "2024 General Studies Paper II Question 17",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "cross-cutting Core ownership shared with the senior-citizens topic",
            text,
        )
        self.assertIn(
            "this package records no option, key or inferred answer for any of the "
            "three",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-03")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn("State's role against marketisation of public healthcare", text)

    def test_dashboard_boundary_is_declared(self) -> None:
        text = session_markdown(generator, "social-justice-03")
        self.assertIn(
            "cumulative card counts and cumulative claim counts are dashboard "
            "outputs",
            text,
        )
        self.assertIn("no State rank or score is asserted", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-03")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Comprehensive Primary Health Care (CPHC)",
            "Social Health Insurance (SHI) vs tax-funded",
            "Catastrophic health expenditure",
            "Standard Treatment Guidelines",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-03"),
            topic_key="social-justice-03",
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
