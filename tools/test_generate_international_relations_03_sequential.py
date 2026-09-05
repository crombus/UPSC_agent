"""Regression tests for International Relations learner-v2 Topic 03."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_03_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_honesty,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations03GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-03"],
            ["India, China, Major Powers and Resilient Supply Chains"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-02"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_policy_term_discipline_is_preserved(self) -> None:
        text = session_markdown(generator, "international-relations-03")
        for phrase in (
            "De-risking",
            "decoupling",
            "Friend-shoring",
            "tactical partnership",
            "complementarity",
            "minilateral",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "an alternative production and technology-cooperation base rather than "
            "a replacement for China",
            text,
        )

    def test_technology_and_defence_instruments_are_dated_and_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-03")
        for phrase in (
            "31 January 2023",
            "17 June 2024",
            "21 September 2024",
            "13 February 2025",
            "31 October 2025",
            "Logistics Exchange Memorandum of Agreement of 2016",
            "Communications Compatibility and Security Agreement of 2018",
            "Basic Exchange and Cooperation Agreement of 2020",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a cooperation initiative and not a treaty or framework agreement",
            text,
        )
        self.assertIn(
            "the official text does not state that TRUST terminated or superseded iCET",
            text,
        )
        self.assertIn("a framework is not a mutual-defence treaty", text)

    def test_border_architecture_is_process_not_settlement(self) -> None:
        text = session_markdown(generator, "international-relations-03")
        for phrase in (
            "21 October 2024",
            "Depsang and Demchok",
            "18 December 2024",
            "19 August 2025",
            "Lipulekh, Shipki La and Nathu La",
            "31 August 2025",
            "27 May 2026",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a patrolling and process architecture and not a boundary settlement",
            text,
        )

    def test_tariff_cycle_is_dated_and_reversible(self) -> None:
        text = session_markdown(generator, "international-relations-03")
        for phrase in (
            "Executive Order 14326",
            "Executive Order 14329",
            "Executive Order 14384",
            "Executive Order 14389",
            "24 July 2026",
            "unjustified and unreasonable",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "dated, reversible executive actions rather than as a standing rate",
            text,
        )

    def test_unverified_russia_figures_are_refused(self) -> None:
        text = session_markdown(generator, "international-relations-03")
        self.assertIn(
            "S-400 delivery status and Russian-crude volumes be treated as "
            "separately unverified without an official figure",
            text,
        )
        self.assertIn("4 and 5 December 2025", text)

    def test_european_union_agreement_is_not_in_force(self) -> None:
        text = session_markdown(generator, "international-relations-03")
        self.assertIn("27 January 2026", text)
        self.assertIn(
            "legal review and ratification remained necessary before entry into force",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-03")
        workbook = workbook_markdown(generator, "international-relations-03")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2019 General Studies Paper II Question 9",
            "2019 General Studies Paper II Question 20",
            "2021 General Studies Paper II Question 10",
            "2024 General Studies Paper II Question 9",
        ):
            self.assertIn(phrase, text)
        self.assertIn("econimic", text)
        self.assertIn(
            "No option or answer letter is recorded or inferred for either "
            "objective demand",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_honesty(self, generator, "international-relations-03")

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-03")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Trade interdependence vs. strategic trust (China)",
            "Tactical partnership vs. alliance (US)",
            "Technology-access asymmetry",
            "Minilateral balancing",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-03"),
            topic_key="international-relations-03",
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
