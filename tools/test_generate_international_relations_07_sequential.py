"""Regression tests for International Relations learner-v2 Topic 07."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_international_relations_07_sequential as generator
import validate_v2_export as validator
from international_relations_generator_test_support import (
    assert_batch_contract,
    assert_live_source_attempt_log,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class InternationalRelations07GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["international-relations-07"],
            ["India-Africa Development and Digital Partnership"],
        )

    def test_the_previous_topic_of_the_sequence_is_pinned(self) -> None:
        self.assertEqual(["international-relations-06"], generator.PREVIOUS_KEYS)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous_batch", source)
        self.assertIn("previous_keys=PREVIOUS_KEYS", source)

    def test_summit_cycle_is_dated_and_the_gap_is_stated(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        for phrase in (
            "8-9 April 2008",
            "24-25 May 2011",
            "26-29 October 2015",
            "23 April 2026",
            "21 May 2026",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "an announced and postponed summit rather than a held one",
            text,
        )

    def test_capacity_building_figures_are_kept_apart(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        for phrase in (
            "five hundred million United States dollars",
            "one thousand six hundred training positions",
            "nineteen institutions",
            "ten thousand to fifteen thousand African students",
            "Economic Survey 2025-26",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "is a global programme total with an explicit South Asian emphasis "
            "and is not an Africa-specific data point",
            text,
        )

    def test_digital_layer_is_a_dated_succession(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        for phrase in (
            "Pan African e-Network",
            "concluded in 2017",
            "e-VidyaBharati and e-ArogyaBharati Network Project",
            "10 September 2018",
            "twenty-two African countries",
            "15,116 scholarships offered",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a historical precursor and not an ongoing flagship platform",
            text,
        )
        self.assertIn(
            "scholarships offered is an input measure",
            text,
        )

    def test_the_dated_memorandum_is_not_upgraded(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        for phrase in (
            "2 July 2024",
            "14 October 1997",
            "Regional Indicative Strategic Development Plan 2020-2030",
            "Digital Transformation Strategy",
            "digital public infrastructure",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a statement of intent whose entry into force and delivery need "
            "separate verification",
            text,
        )

    def test_commitments_are_never_reported_as_disbursements(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        for phrase in ("190 Lines of Credit", "USD 10 billion", "41 African countries"):
            self.assertIn(phrase, text)
        self.assertIn(
            "a line of credit extended is a commitment",
            text,
        )
        self.assertIn("USD 81.99 billion", text)
        self.assertIn("belong to the Economy owner", text)

    def test_model_claim_carries_its_verification_test(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        self.assertIn(
            "non-intrusive support to the development of democratic institutions",
            text,
        )
        self.assertIn("implementation and maintenance test", text)
        self.assertIn(
            "announcement scale is not evidence of partnership depth",
            text,
        )
        self.assertIn("digital sovereignty", text)

    def test_security_and_representation_limbs_are_bounded(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        for phrase in (
            "Lucknow Declaration",
            "February 2020",
            "October 2022",
            "AFINDEX",
            "March 2023",
            "9 September 2023",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "episodic exercises do not create a defence alliance",
            text,
        )
        self.assertIn(
            "membership of one forum does not resolve Africa's financing",
            text,
        )

    def test_political_risk_and_comparator_are_not_caricatured(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        for phrase in (
            "Mali, Guinea, Burkina Faso and Niger",
            "Forum on China-Africa Cooperation",
            "Coalition for Disaster Resilient Infrastructure",
            "23 September 2019",
            "International Solar Alliance",
            "6 December 2017",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "may be generalised across the continent or caricatured as "
            "uniformly extractive",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        workbook = workbook_markdown(generator, "international-relations-07")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(2, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(2, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2021 General Studies Paper II Question 9",
            "2025 General Studies Paper II Question 9",
            "2023 Prelims General Studies Paper I question 98",
            "2024 Prelims General Studies Paper I question 91",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "No option or answer letter is recorded or inferred for either "
            "objective demand",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_live_official_source_attempts_are_recorded_honestly(self) -> None:
        assert_live_source_attempt_log(
            self,
            generator,
            "international-relations-07",
        )
        text = session_markdown(generator, "international-relations-07")
        for phrase in (
            "https://au.int/en/agenda2063/overview",
            "https://au.int/en/documents",
            "Agenda 2063",
            "50th Anniversary Solemn Declaration",
            "no India-Africa project, figure, credit line or outcome was taken "
            "from it",
        ):
            self.assertIn(phrase, text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "international-relations-07")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Human resource development vs. infrastructure aid",
            "Digital sovereignty",
            "Co-development vs. one-way aid transfer",
            "Implementation/maintenance test",
        ):
            self.assertIn(phrase, advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "international-relations-07"),
            topic_key="international-relations-07",
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
