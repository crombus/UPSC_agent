"""Regression tests for International Relations learner-v2 Topic 09."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_09_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_attempt_log,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations09GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-09"],
            ["Indian Diaspora, Consular Protection and Soft Power"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-08"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_population_categories_carry_their_exact_status(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        for phrase in (
            "35,421,987",
            "19,571,375",
            "15,850,612",
            "6,079,221",
            "4,344,008",
            "2,902,370",
            "2,750,551",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a population-stock estimate and never as a count of citizens abroad",
            text,
        )
        self.assertIn(
            "Overseas Citizen of India status is not dual citizenship",
            text,
        )

    def test_welfare_stack_is_named_and_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        for phrase in (
            "8-10 January 2025",
            "Bhubaneswar",
            "Viksit Bharat",
            "21 February 2015",
            "MADAD 2.0",
            "Pravasi Bharatiya Sahayata Kendras",
            "Indian Community Welfare Fund",
            "Pravasi Bharatiya Bima Yojana",
            "8,536,398",
            "2,222",
            "Protector General of Emigrants",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "no nineteenth edition officially recorded as held or announced as "
            "of 3 August 2026",
            text,
        )

    def test_consular_treaty_frame_is_dated_and_limited(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        for phrase in (
            "Vienna Convention on Consular Relations",
            "4 March to 22 April 1963",
            "ninety-five States",
            "24 April 1963",
            "19 March 1967",
            "79 articles",
            "Article 36",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "not an unlimited power to override host-country law or secure release",
            text,
        )

    def test_caseload_and_evacuation_boundaries_are_stated(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        for phrase in (
            "10,152",
            "28 March 2025",
            "Operation Sindhu",
            "4,415",
            "3,597",
            "27 June 2025",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a measure of consular workload rather than of diaspora wrongdoing",
            text,
        )
        self.assertIn(
            "the relief and logistics cycle belongs to the Disaster Management owner",
            text,
        )

    def test_remittance_evidence_never_replaces_the_political_limb(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        for phrase in (
            "USD 135.4 billion",
            "3.5 per cent",
            "27.7 per cent",
            "19.2",
            "10.8",
            "6.6",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "must never be substituted for the political half of a question",
            text,
        )
        self.assertIn(
            "advanced economies now contribute more of India's inward remittances",
            text,
        )

    def test_instrument_population_mismatch_is_diagnosed(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        self.assertIn("Emigration-Check-Required", text)
        self.assertIn(
            "visa regimes, social-security portability and professional "
            "qualification recognition",
            text,
        )
        self.assertIn(
            "instead of proposing more of an instrument that does not reach "
            "that segment",
            text,
        )

    def test_soft_power_is_evidenced_through_the_named_inventory(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        for phrase in (
            "Bollywood",
            "Ayurveda",
            "yoga",
            "sporting exchanges",
            "Now-Required-Indians",
            "Indian Council for Cultural Relations",
            "public diplomacy division",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "explicitly conditional on India adopting such a policy",
            text,
        )
        self.assertIn(
            "a documented proposal and not an implemented reform",
            text,
        )
        self.assertIn("especially in the South Asian region", text)

    def test_political_influence_carries_its_liability_side(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        for phrase in ("Kamala Harris", "Rishi Sunak", "119th Congress"):
            self.assertIn(phrase, text)
        self.assertIn(
            "cannot be treated as agents of India",
            text,
        )
        self.assertIn(
            "allegations, charges, pleas and final judicial findings must be "
            "kept distinct",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        workbook = workbook_markdown(generator, "international-relations-09")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(2, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(2, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2020 General Studies Paper II Question 10",
            "2023 General Studies Paper II Question 10",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "No objective demand from any audited Prelims routing ledger is "
            "routed to this owner",
            text,
        )
        self.assertIn(
            "deliberately not converted into a solved demand card",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_attempt_log(
            self,
            generator,
            "international-relations-09",
        )
        text = session_markdown(generator, "international-relations-09")
        for phrase in (
            "https://madad.gov.in/",
            "https://www.emigrate.gov.in/",
            "https://www.iccr.gov.in/",
            "https://legal.un.org/avl/ha/vccr/vccr.html",
            "host-resolution error",
            "no treaty article wording was quoted from it",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-09")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Institutional fragmentation critique",
            "Diaspora as bridge vs. diaspora as lever",
            "Composition shift as a policy-design variable",
            "Evacuation coordination as diplomatic architecture",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-09"),
            topic_key="international-relations-09",
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
