"""Regression tests for International Relations learner-v2 Topic 04."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_04_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_honesty,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations04GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-04"],
            ["Indo-Pacific, Indian Ocean and Maritime Security"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-03"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_doctrine_is_a_declared_vision_and_mahasagar_extends_it(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        for phrase in (
            "Security and Growth for All in the Region",
            "12 March 2015",
            "Mutual and Holistic Advancement for Security and Growth Across Regions",
            "12 March 2025",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a declared vision guiding regional maritime engagement and not as a "
            "binding treaty or alliance",
            text,
        )
        self.assertIn(
            "an extension of scope to the wider Global South and never a "
            "replacement of the earlier doctrine",
            text,
        )

    def test_treaty_status_ladder_is_exact(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        for phrase in (
            "10 December 1982",
            "29 June 1995",
            "19 June 2023",
            "20 September 2023",
            "19 September 2025",
            "17 January 2026",
            "25 September 2024",
            "Territorial Waters, Continental Shelf, Exclusive Economic Zone and "
            "Other Maritime Zones Act, 1976",
        ):
            self.assertIn(phrase, text)
        self.assertIn("signatory and not party", text)
        self.assertIn(
            "a state which is not a party cannot vote at the Conference of the "
            "Parties",
            text,
        )

    def test_chairship_is_separated_from_control(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        for phrase in (
            "twenty-three-member",
            "Ebène",
            "November 2025",
            "20 February 2026",
            "Gurugram",
            "twenty-five partner countries",
            "fifteen countries",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a chairship confers agenda-setting and convening advantage rather "
            "than decision-making authority over members",
            text,
        )

    def test_participation_categories_are_never_collapsed(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        for phrase in (
            "20 November 2025",
            "Bangladesh, India, Maldives, Mauritius and Sri Lanka",
            "Seychelles attending as an observer and Malaysia as a guest",
            "9 February 2026",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "without an officially recorded effective accession date",
            text,
        )
        self.assertIn(
            "member, observer, guest and decided to join must never be collapsed",
            text,
        )

    def test_minilateral_instruments_carry_no_obligation(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        for phrase in (
            "4 November 2019",
            "ASEAN Outlook on the Indo-Pacific",
            "15 September 2021",
            "SSN-AUKUS",
            "five hundred and fifty-five million euro",
            "November 2025",
        ):
            self.assertIn(phrase, text)
        self.assertIn("an exercise creates no collective-defence obligation", text)
        self.assertIn("not a treaty, alliance or centralised funding body", text)
        self.assertIn("India is not an AUKUS member", text)

    def test_imo_adoption_failure_is_reported_honestly(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        for phrase in (
            "26 June 2025",
            "1 January 2020",
            "2026-27 biennium",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "was approved at committee level but was not adopted in October 2025",
            text,
        )
        self.assertIn(
            "rule-shaping access rather than a guarantee of preferred outcomes",
            text,
        )

    def test_the_2016_statement_does_not_pronounce_on_the_merits(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        self.assertIn("7 July 2014", text)
        self.assertIn("12 July 2016", text)
        self.assertIn("without pronouncing on the merits", text)

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        workbook = workbook_markdown(generator, "international-relations-04")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2020 General Studies Paper II Question 20",
            "2021 General Studies Paper II Question 20",
            "2023 General Studies Paper II Question 20",
            "2024 General Studies Paper II Question 20",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the opening clause of the printed stem was truncated in the scan",
            text,
        )
        self.assertIn(
            "no option or answer letter is recorded or inferred for either "
            "objective demand",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_honesty(self, generator, "international-relations-04")
        text = session_markdown(generator, "international-relations-04")
        for phrase in (
            "https://indiannavy.gov.in/",
            "https://shipmin.gov.in/",
            "https://www.imo.org/en/About/Pages/Default.aspx",
            "https://www.iora.int/en",
            "failed at transport level",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-04")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Maritime commons vs. territorial waters",
            "Island-state agency vs. dependency framing",
            "Legal-order participation vs. rule-shaping",
            "Chairship vs. control",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-04"),
            topic_key="international-relations-04",
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
