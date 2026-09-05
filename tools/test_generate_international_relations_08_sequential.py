"""Regression tests for International Relations learner-v2 Topic 08."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_08_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_attempt_log,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations08GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-08"],
            ["Global South and Development Partnering"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-07"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_category_and_coalitions_are_kept_distinct(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        for phrase in (
            "political-development category",
            "over 120 developing countries",
            "Non-Aligned Movement",
            "Rio de Janeiro Declaration",
            "24 October 2024",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "is not fully coextensive with it",
            text,
        )
        self.assertIn(
            "widens participation without widening membership rights",
            text,
        )

    def test_group_of_77_machinery_is_sourced_and_dated(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        for phrase in (
            "South Summit",
            "Havana",
            "10-14 April 2000",
            "Doha",
            "12-16 June 2005",
            "Oriental Republic of Uruguay",
            "Caracas Programme of Action",
            "1981",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "recorded here as the page's own state on the date of access",
            text,
        )

    def test_south_south_doctrine_uses_the_exact_principles(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        for phrase in (
            "respect for national sovereignty",
            "national ownership and independence",
            "non-conditionality",
            "non-interference in domestic affairs",
            "mutual benefit",
            "Buenos Aires Plan of Action",
            "resolution 33/134",
            "triangular cooperation",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "led and owned by Southern actors",
            text,
        )

    def test_leadership_claim_stays_aspirational(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        self.assertIn(
            "India has become a potential leader",
            text,
        )
        self.assertIn(
            "India speaks within the Global South rather than for it",
            text,
        )

    def test_convening_instruments_are_dated_and_not_upgraded(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        for phrase in (
            "12-13 January 2023",
            "17 November 2023",
            "17 August 2024",
            "Global Development Compact",
            "trade for development",
            "technology sharing",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "no fourth edition officially recorded as held or announced as of "
            "3 August 2026",
            text,
        )
        self.assertIn(
            "a proposal announced at a summit rather than as an operational "
            "institution",
            text,
        )

    def test_material_base_is_reported_as_commitment_not_delivery(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        for phrase in (
            "260 Lines of Credit",
            "USD 26 billion",
            "62 countries",
            "70 members",
            "Global Biofuels Alliance",
            "30 July 2026",
            "International Solar Alliance",
            "6 December 2017",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "extended or committed facilities and not disbursed amounts",
            text,
        )
        self.assertIn(
            "membership counts and aggregate targets are not country-level "
            "delivery evidence",
            text,
        )

    def test_representation_ask_and_outcome_are_at_real_scale(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        for phrase in ("9 September 2023", "13 July 2026", "2028-29"):
            self.assertIn(phrase, text)
        self.assertIn(
            "one forum and one seat rather than systemic redistribution",
            text,
        )

    def test_latin_american_limb_carries_exact_legal_status(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        for phrase in ("MERCOSUR", "1 June 2009", "May 2025", "5 December 2025", "CELAC"):
            self.assertIn(phrase, text)
        self.assertIn(
            "negotiation progress and not an agreement concluded or in force",
            text,
        )

    def test_internal_contestation_is_conceded(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        self.assertIn(
            "a negotiated outcome rather than a natural given",
            text,
        )
        self.assertIn("norm entrepreneurship", text.casefold())

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        workbook = workbook_markdown(generator, "international-relations-08")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(1, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(1, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("2019 General Studies Paper II Question 19", text)
        self.assertIn(
            "No objective demand from any audited Prelims routing ledger is "
            "routed to this owner",
            text,
        )
        self.assertIn(
            "instead of force-fitting an adjacent question onto this owner",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_attempt_log(
            self,
            generator,
            "international-relations-08",
        )
        text = session_markdown(generator, "international-relations-08")
        for phrase in (
            "https://www.g77.org/doc/",
            "https://unsouthsouth.org/about/about-sstc/",
            "no Indian programme, figure or outcome was taken from it",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-08")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Norm entrepreneurship",
            "Internal contestation within the South",
            "Representation deficit as the unifying grievance",
            "aspirational leadership framing",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-08"),
            topic_key="international-relations-08",
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
