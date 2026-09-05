"""Regression tests for International Relations learner-v2 Topic 12."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_12_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_attempt_log,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations12GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-12"],
            ["UN and International Institutions: Global Governance"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-11"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_charter_composition_and_obligation_are_quoted_exactly(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        for phrase in (
            "Article 23",
            "fifteen Members",
            "Union of Soviet Socialist Republics",
            "not be eligible for immediate re-election",
            "Article 24",
            "Article 25",
            "Article 29",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "an answer must distinguish the Charter's text from the practice that "
            "followed it",
            text,
        )

    def test_the_voting_rule_defines_the_veto_precisely(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        for phrase in (
            "Article 27",
            "affirmative vote of nine members",
            "concurring votes of the permanent members",
            "paragraph 3 of Article 52",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the word veto does not appear as a grant of a special power",
            text,
        )

    def test_the_amendment_rule_is_stated_as_the_structural_lock(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        for phrase in ("Article 108", "Article 109", "two thirds"):
            self.assertIn(phrase, text)
        self.assertIn(
            "requires ratification by exactly the states whose relative position it "
            "would change",
            text,
        )

    def test_counter_terrorism_bodies_are_kept_apart(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        for phrase in (
            "resolution 1373",
            "28 September 2001",
            "Delhi Declaration",
            "29 October 2022",
            "5 January 2029",
            "1267",
            "2253",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "coordinate, monitor and assess member-state compliance without "
            "independent enforcement power",
            text,
        )

    def test_reform_evidence_is_kept_at_its_evidentiary_level(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        for phrase in (
            "Group of Four",
            "Open-Ended Working Group",
            "25 September 2025",
            "Ezulwini Consensus",
            "Sirte Declaration",
            "20 April 2026",
            "twenty-six-member Council",
            "31 October 2025",
            "Kuwait and the Netherlands",
            "22 September 2024",
            "Global Digital Compact",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "neither a consolidated model nor a decision commencing text-based "
            "negotiations",
            text,
        )
        self.assertIn("a negotiating position and not reform achieved", text)

    def test_the_advisory_function_and_its_limit_are_verified(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        for phrase in (
            "five United Nations organs, fifteen specialized agencies and one "
            "related organization",
            "advisory opinions are not binding",
            "great legal weight and moral authority",
            "23 July 2025",
            "Rome Statute",
        ):
            self.assertIn(phrase, text)

    def test_peacekeeping_principles_are_verified_and_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        for phrase in (
            "consent of the parties",
            "non-use of force except in self-defence and defence of the mandate",
            "not an enforcement tool",
            "275,000",
            "Liberia",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "does not automatically yield a permanent seat",
            text,
        )

    def test_agency_and_financing_status_is_stated_honestly(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        for phrase in (
            "58-member Executive Board",
            "31 December 2018",
            "30 January 2020",
            "146 economies",
            "20 May 2025",
            "19 September 2025",
            "2.75 per cent",
            "2.63 per cent",
            "17 January 2026",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "notification is expressly not completed withdrawal",
            text,
        )
        self.assertIn(
            "leaving relative quota and voting shares unchanged",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        workbook = workbook_markdown(generator, "international-relations-12")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(5, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(5, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2024 General Studies Paper II Question 19",
            "2025 General Studies Paper II Question 20",
            "2019 General Studies Paper II Question 10",
            "2020 General Studies Paper II Question 9",
            "2022 General Studies Paper II Question 20",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "its printed stem is deliberately not reconstructed, quoted or paraphrased",
            text,
        )
        self.assertIn(
            "this owner holds the institutional half while topic 11 holds the trade, "
            "negotiating and external-policy half",
            text,
        )
        self.assertIn("no option, answer letter or inferred key is recorded", text)
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_attempt_log(
            self,
            generator,
            "international-relations-12",
        )
        text = session_markdown(generator, "international-relations-12")
        for phrase in (
            "https://main.un.org/securitycouncil/en/content/current-members",
            "https://www.un.org/en/about-us/un-charter/chapter-5",
            "https://www.un.org/en/about-us/un-charter/chapter-18",
            "https://www.icj-cij.org/advisory-jurisdiction",
            "https://peacekeeping.un.org/en/principles-of-peacekeeping",
            "https://www.who.int/about/governance",
            "only a photograph caption line",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-12")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Veto as both stabiliser and blocker",
            "Financing as an underexamined reform dimension",
            "CTC's coordinating, not enforcing, mandate",
            "UNGA-strengthening argument",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-12"),
            topic_key="international-relations-12",
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
