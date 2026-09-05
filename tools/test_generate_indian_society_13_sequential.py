"""Regression tests for Indian Society learner-v2 Topic 13."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_12_sequential as previous
import generate_indian_society_13_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety13GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-13"],
            ["Communalism"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-12"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_mobilisation_mechanisms_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-13")
        for phrase in (
            "primordialism",
            "instrumentalist",
            "constructivist",
            "relative deprivation",
            "power struggle",
            "rumour",
            "amplification",
            "polarisation",
            "segregation",
            "institutional impartiality",
            "separatist communalism",
            "communal harmony",
        ):
            self.assertIn(phrase, text)

    def test_communalism_is_separated_from_religious_belief(self) -> None:
        text = session_markdown(generator, "indian-society-13")
        self.assertIn(
            "distinct from personal religious belief or devotion",
            text,
        )
        self.assertIn("the personal holding and practice of faith", text)

    def test_statute_is_bounded_and_no_litigation_outcome_is_claimed(self) -> None:
        text = session_markdown(generator, "indian-society-13")
        self.assertIn("Places of Worship (Special Provisions) Act, 1991", text)
        self.assertIn("15 August 1947", text)
        self.assertIn("Ayodhya-only exception", text)
        self.assertIn("21 July 2026", text)
        self.assertIn("did not yield a final merits order", text)

    def test_escalation_chain_is_kept_conditional(self) -> None:
        text = session_markdown(generator, "indian-society-13")
        self.assertIn("diagnostic risk heuristic", text)
        self.assertIn("not a universal chronology", text.replace(
            "never a universal chronology", "not a universal chronology"
        ))

    def test_zero_recent_pyq_is_recorded_honestly(self) -> None:
        text = session_markdown(generator, "indian-society-13")
        workbook = workbook_markdown(generator, "indian-society-13")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(2, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(2, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "No direct standalone communalism demand appears in the audited "
            "2024-2025 Mains ledger",
            text,
        )
        self.assertIn("no verbatim wording is claimed", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_no_riot_or_casualty_statistic_is_asserted(self) -> None:
        text = session_markdown(generator, "indian-society-13")
        self.assertIn(
            "No riot statistic, casualty figure or court order is asserted",
            text,
        )

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-13")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Instrumentalist mobilisation chain",
            "Riot causal chain (structural + triggering)",
            "Trust-repair chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-13"),
            topic_key="indian-society-13",
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
