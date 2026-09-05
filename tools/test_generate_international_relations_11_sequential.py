"""Regression tests for International Relations learner-v2 Topic 11."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_11_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_attempt_log,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations11GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-11"],
            ["Globalisation, Trade Agreements and External-Policy Effects"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-10"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_the_two_forces_are_taught_as_co_present(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        self.assertIn(
            "simultaneously operating forces of differing relative strength",
            text,
        )
        self.assertIn("waning rather than ended", text)
        for phrase in ("trade channel", "technology channel", "climate channel"):
            self.assertIn(phrase, text.casefold())

    def test_the_trade_organisation_structure_is_verified(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "run by its member governments",
            "at least once every two years",
            "normally taken by consensus",
            "Trade Policy Review Body",
            "1995",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a weakened institution and expressly not an irrelevant one",
            text,
        )

    def test_consensus_and_the_ministerial_cycle_are_exact(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "Abu Dhabi",
            "26 February to 2 March 2024",
            "Yaounde",
            "26 to 30 March 2026",
            "165 of 166",
            "Investment Facilitation for Development",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "the veto point is procedural rather than majoritarian",
            text,
        )

    def test_appellate_paralysis_is_dated_and_two_sided(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "10 December 2019",
            "30 November 2020",
            "DS582",
            "DS584",
            "DS579",
            "8 December 2023",
            "17 May 2023",
            "24 December 2021",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "India equally cannot obtain binding appellate review against others",
            text,
        )

    def test_the_fisheries_sequence_carries_three_dates(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "Agreement on Fisheries Subsidies",
            "17 June 2022",
            "15 September 2025",
            "20 July 2026",
            "Buenos Aires Ministerial Decision",
            "Negotiating Group on Rules",
        ):
            self.assertIn(phrase, text)

    def test_the_legal_stage_ladder_is_complete_and_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "1 May 2022",
            "29 December 2022",
            "10 March 2024",
            "1 October 2025",
            "24 July 2025",
            "15 July 2026",
            "Double Contributions Convention",
            "27 January 2026",
            "4 November 2019",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "concluded, signed, ratified and in force are four different claims",
            text,
        )
        self.assertIn(
            "a shared objective stated in the agreement's framework rather than "
            "realised investment or realised employment",
            text,
        )

    def test_the_carbon_border_regime_is_verified_and_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "Carbon Border Adjustment Mechanism",
            "1 January 2026",
            "cement, iron and steel, aluminium, fertilisers, electricity and hydrogen",
            "Emissions Trading System",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "without being bound as a party to the European Union's internal law",
            text,
        )

    def test_tariff_volatility_is_named_as_the_mechanism(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "7 August 2025",
            "27 August 2025",
            "7 February 2026",
            "Section 301",
            "24 July 2026",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "volatility rather than tariff level is the transmission mechanism",
            text,
        )

    def test_climate_commitments_are_not_presented_as_outcomes(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "forty-five per cent",
            "2070",
            "Loss and Damage",
            "Economic Complexity Index",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "targets are commitments and not proof of realised outcomes",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        workbook = workbook_markdown(generator, "international-relations-11")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(3, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2025 General Studies Paper II Question 10",
            "2018 General Studies Paper II Question 19",
            "2022 General Studies Paper II Question 20",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "its printed stem is deliberately not reconstructed, quoted or paraphrased",
            text,
        )
        self.assertIn(
            "this owner holds the trade, negotiating and external-policy half and "
            "topic 12 holds the institutional half",
            text,
        )
        self.assertIn(
            "No objective demand from any audited Prelims routing ledger is routed "
            "to this owner",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_attempt_log(
            self,
            generator,
            "international-relations-11",
        )
        text = session_markdown(generator, "international-relations-11")
        for phrase in (
            "https://commerce.gov.in/international-trade/trade-agreements/",
            "https://www.efta.int/free-trade/free-trade-agreements/india",
            "https://www.wto.org/english/thewto_e/whatis_e/tif_e/org1_e.htm",
            "https://www.wto.org/english/thewto_e/minist_e/mc14_e/mc14_e.htm",
            "https://www.wto.org/english/tratop_e/rulesneg_e/fish_e/fish_e.htm",
            "https://www.wto.org/english/tratop_e/dispu_e/appellate_body_e.htm",
            "returned HTTP 429",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-11")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Co-presence, not succession",
            "De-risking as a specific trade-technology response",
            "Trade-technology-climate linkage",
            "Consensus as the binding constraint",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-11"),
            topic_key="international-relations-11",
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
