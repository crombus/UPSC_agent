"""Regression tests for International Relations learner-v2 Topic 10."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_10_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_attempt_log,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations10GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-10"],
            ["Regional, Global and Minilateral Groupings"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-09"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_every_grouping_is_placed_in_a_named_layer(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        for phrase in (
            "South Asian Association for Regional Cooperation",
            "Mekong-Ganga Cooperation",
            "Indian Ocean Rim Association",
            "Shanghai Cooperation Organisation",
            "Group of Twenty",
            "I2U2",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the layer to be named before the body is analysed",
            text,
        )

    def test_south_asian_layer_separates_stagnation_from_dissolution(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        for phrase in (
            "26-27 November 2014",
            "30 March 2022",
            "20 May 2024",
            "4 April 2025",
            "Bangkok Vision 2030",
            "Eminent Persons Group",
            "8 February 2004",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "dissolution must not be asserted without a specific verified source",
            text,
        )
        self.assertIn(
            "the two names are one institutional lineage and not two organisations",
            text,
        )

    def test_partial_entry_into_force_is_stated_exactly(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        for phrase in (
            "3 April 2025",
            "16 May 2026",
            "13 May 2026",
            "Bhutan, India, Myanmar and Thailand",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "an agreement in force and an agreement binding the whole region are "
            "different claims",
            text,
        )
        self.assertIn("variable-geometry ratification", text)

    def test_participation_tiers_are_kept_apart_from_membership(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        for phrase in (
            "twenty-three member states",
            "twelve dialogue partners",
            "fifteen dialogue partners",
            "24 October 2024",
            "9 September 2023",
            "Timor-Leste",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the partner category confers participation without the rights and "
            "obligations of membership",
            text,
        )
        self.assertIn(
            "India is not a member of the Regional Comprehensive Economic Partnership",
            text,
        )

    def test_treaty_alliance_comparator_is_verified_and_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        for phrase in (
            "4 April 1949",
            "Washington, D.C.",
            "Article 5",
            "11 September 2001",
            "2 October 2001",
            "Operation Eagle Assist",
            "830 crew members",
            "thirty-second member in March 2024",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "must never be conflated with a non-treaty functional minilateral that "
            "carries no collective-defence commitment",
            text,
        )

    def test_unverified_outcomes_are_reported_as_gaps(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        self.assertIn(
            "no India-hosted Leaders' Summit and no formal postponement is "
            "officially verified",
            text,
        )
        self.assertIn(
            "no 2026 Leaders' Summit outcome was officially verified as of "
            "3 August 2026",
            text,
        )
        self.assertIn(
            "no officially verified meeting since the eighteenth Foreign Ministers' "
            "Meeting convened virtually on 26 November 2021",
            text,
        )

    def test_regime_membership_distinctions_are_exact(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        for phrase in (
            "thirty-fifth member on 27 June 2016",
            "Nuclear Suppliers Group",
            "Asian Infrastructure Investment Bank",
            "25 July 2014",
            "Asia-Europe Meeting in 2007",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a waiver is not membership and admission requires consensus",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        workbook = workbook_markdown(generator, "international-relations-10")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(6, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(6, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2020 General Studies Paper II Question 19",
            "2021 General Studies Paper II Question 19",
            "2022 General Studies Paper II Question 10",
            "2022 General Studies Paper II Question 19",
            "2023 General Studies Paper II Question 9",
            "2023 General Studies Paper II Question 19",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the 2020 General Studies Paper II is not among the locally held "
            "official papers",
            text,
        )
        self.assertIn(
            "the 150-word limit is taken from the paper's instruction block",
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
            "international-relations-10",
        )
        text = session_markdown(generator, "international-relations-10")
        for phrase in (
            "https://bimstec.org/about-bimstec",
            "https://asean.org/member-states/",
            "https://www.iora.int/en/about/about-iora",
            "https://eng.sectsco.org/about_sco/",
            "https://www.g20.org/en/about-g20/",
            "https://brics-india2026.in/",
            "https://www.nato.int/cps/en/natohq/nato_countries.htm",
            "https://www.nato.int/cps/en/natohq/topics_110496.htm",
            "host-resolution error",
            "omitted the Location header",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-10")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Regionalism vs. minilateralism",
            "ASEAN centrality",
            "Institutional-effectiveness spectrum",
            "Partial entry into force as an effectiveness datum",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-10"),
            topic_key="international-relations-10",
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
