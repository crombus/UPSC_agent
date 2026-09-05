"""Regression tests for International Relations learner-v2 Topic 05."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_05_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_honesty,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations05GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-05"],
            ["Central Asia, Eurasia and Connectivity"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-04"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_the_access_constraint_is_taught_as_structural(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        for phrase in (
            "Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan and Uzbekistan",
            "Connect Central Asia Policy",
            "Xinjiang",
            "Karakoram",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a structural rather than a merely technical problem",
            text,
        )
        self.assertIn(
            "political, security, economic and cultural connections",
            text,
        )

    def test_economic_instrument_status_is_never_upgraded(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        for phrase in (
            "Comprehensive Economic Cooperation Agreement",
            "3 June 2017",
            "St Petersburg",
            "22-25 June 2026",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "under negotiation and neither signed nor in force",
            text,
        )

    def test_participation_tiers_are_current_and_dated(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        for phrase in (
            "Belarus, China, India, Iran, Kazakhstan, Kyrgyzstan, Pakistan, "
            "Russia, Tajikistan and Uzbekistan",
            "Afghanistan and Mongolia",
            "fifteen dialogue partners",
            "1 September 2025",
            "Tianjin Declaration",
            "Bishkek",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "whose enabling amendments had not entered into force",
            text,
        )
        self.assertIn("period-specific", text)

    def test_the_unheld_second_summit_is_stated_honestly(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        for phrase in ("27 January 2022", "6 June 2025", "16 October 2025"):
            self.assertIn(phrase, text)
        self.assertIn(
            "no second leader-level summit had been recorded as held by "
            "3 August 2026",
            text,
        )

    def test_connectivity_instruments_carry_exact_levels(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        for phrase in (
            "13 May 2024",
            "India Ports Global Limited",
            "25 April 2011",
            "3 February 2018",
            "International North-South Transport Corridor",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "an announced credit window rather than as delivered equipment or "
            "disbursed finance",
            text,
        )
        self.assertIn(
            "a facilitation framework rather than an infrastructure-finance "
            "mechanism",
            text,
        )
        self.assertIn(
            "an announced and developing corridor with operating segments "
            "rather than a completed, full-capacity corridor",
            text,
        )

    def test_sanctions_exposure_is_distinguished_from_obligation(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        for phrase in ("16 September 2025", "29 September 2025", "26 April 2026"):
            self.assertIn(phrase, text)
        self.assertIn(
            "creates exposure risk for entities rather than an international "
            "legal obligation binding on India",
            text,
        )

    def test_competitive_field_and_functional_cooperation_are_both_kept(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        self.assertIn("New Great Game", text)
        self.assertIn(
            "will always attract foreign presences",
            text,
        )
        self.assertIn(
            "only benefiting the energy producers",
            text,
        )
        self.assertIn(
            "a platform but not privileged influence",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        workbook = workbook_markdown(generator, "international-relations-05")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(2, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(2, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2018 General Studies Paper II Question 10",
            "2024 General Studies Paper II Question 10",
            "2025 Prelims General Studies Paper I question 62",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the printed word-limit tail was corrupted in the scan",
            text,
        )
        self.assertIn(
            "No option or answer letter is recorded or inferred for that "
            "objective demand",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_honesty(self, generator, "international-relations-05")
        text = session_markdown(generator, "international-relations-05")
        for phrase in (
            "https://eng.sectsco.org/",
            "http://www.eaeunion.org/?lang=en",
            "no membership, participation-category or summit-outcome claim",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-05")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Two-route geography problem (Sikri)",
            "INSTC/Chabahar as work-around, not solution",
            "India-China energy-competition management (Sikri)",
            "New Great Game",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-05"),
            topic_key="international-relations-05",
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
