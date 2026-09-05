"""Regression tests for International Relations learner-v2 Topic 06."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_06_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_honesty,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations06GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-06"],
            ["West Asia, Energy Security and Connectivity"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-05"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_dependence_figures_carry_their_period_boundaries(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        for phrase in (
            "eighty-eight point two per cent",
            "eighty-eight point seven per cent",
            "approximately seventy per cent",
            "Economic Survey 2025-26",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "diversification of sources and not reduction of aggregate dependence",
            text,
        )
        self.assertIn(
            "devised to process the quality of crude oil that Iran supplies",
            text,
        )

    def test_balancing_is_active_rather_than_equidistance(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        self.assertIn("Look West", text)
        self.assertIn(
            "not at the expense of its friendships with Arab and other Muslim "
            "states",
            text,
        )
        self.assertIn(
            "active balancing rather than passive equidistance",
            text,
        )
        self.assertIn("recognised the State of Palestine in 1988", text)

    def test_israel_track_is_diverse_and_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        for phrase in (
            "1992",
            "July 2017",
            "Barak-8",
            "Indo-Israel Agricultural Project",
            "Technological Innovation Fund",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "funded projects must be distinguished from announced cooperation",
            text,
        )

    def test_gulf_instruments_are_dated_and_force_status_is_exact(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        for phrase in (
            "9 September 2024",
            "Riyadh",
            "22 April 2025",
            "18 February 2025",
            "25 January 2017",
            "1 May 2022",
            "18 December 2025",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "entry into force requiring separate verification",
            text,
        )

    def test_corridor_and_minilateral_claims_are_not_upgraded(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        for phrase in ("9 September 2023", "24 June 2024", "13 February 2025"):
            self.assertIn(phrase, text)
        self.assertIn(
            "no completed construction or operating segment is officially "
            "established",
            text,
        )
        self.assertIn(
            "no four-party I2U2 meeting or outcome in 2024 to 2026 could be "
            "verified from official sources",
            text,
        )
        self.assertIn("Abraham Accords", text)

    def test_iran_track_status_is_disputed_and_reversible(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        for phrase in (
            "14 July 2015",
            "resolution 2231",
            "8 May 2018",
            "May 2019",
            "13 May 2024",
            "29 September 2025",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "must not be described as normally functioning",
            text,
        )
        self.assertIn(
            "a reversible foreign executive measure rather than a permanent "
            "legal guarantee",
            text,
        )

    def test_compounding_risk_and_consular_obligation_are_evidenced(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        for phrase in (
            "Strait of Hormuz",
            "Operation Sindhu",
            "27 June 2025",
            "4,344,008",
            "2,750,551",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "population-stock estimates rather than citizenship or Overseas "
            "Citizen of India counts",
            text,
        )
        self.assertIn("energy trilemma", text)

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        workbook = workbook_markdown(generator, "international-relations-06")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(3, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2018 General Studies Paper II Question 9",
            "2018 General Studies Paper II Question 20",
            "2025 General Studies Paper II Question 19",
            "2026 Prelims General Studies Paper I question 30",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the printed word-limit tail was corrupted in the scan",
            text,
        )
        self.assertIn(
            "No option or answer letter is recorded or inferred for any of the "
            "four objective demands",
            text,
        )
        self.assertIn("provisional status is preserved exactly", text)
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_honesty(self, generator, "international-relations-06")
        text = session_markdown(generator, "international-relations-06")
        for phrase in (
            "https://www.gcc-sg.org/en-us/Pages/default.aspx",
            "https://www.ppac.gov.in/",
            "no energy share or dependence figure was taken from it",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-06")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Energy trilemma applied to West Asia",
            "Refinery lock-in as a hidden switching cost",
            "Connectivity-diplomacy vs. connectivity-infrastructure",
            "Regional-conflict spillover",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-06"),
            topic_key="international-relations-06",
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
