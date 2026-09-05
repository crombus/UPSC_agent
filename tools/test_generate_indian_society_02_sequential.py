"""Regression tests for Indian Society learner-v2 Topic 02."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_01_sequential as previous
import generate_indian_society_02_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)


class IndianSociety02GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-02"],
            ["Caste System: Structure and Contemporary Dynamics"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-01"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_caste_structure_and_mobility_evidence_is_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-02")
        for phrase in (
            "M.N. Srinivas",
            "Rampura",
            "gotra exogamy",
            "dominant caste",
            "Special Marriage Act, 1954",
            "VERIFIED PYQ OWNERSHIP AUDIT",
        ):
            self.assertIn(phrase, text)

    def test_five_verified_pyq_demands_are_reproduced(self) -> None:
        text = session_markdown(generator, "indian-society-02")
        for phrase in (
            "Intercaste marriages between castes which have socio-economic parity",
            "Caste system is assuming new identities and associational forms",
            "Has caste lost its relevance in understanding the multi-cultural Indian Society?",
            "Analyse the salience of 'sect' in Indian society vis-a-vis caste, region and religion.",
            "Why is caste identity in India both fluid and static?",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(5, text.count("### PYQ DEMAND CARD"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-02")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Sanskritisation vs Westernisation",
            "Dominant caste vs ritually superior caste",
            "Marriage-boundary chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-02"),
            topic_key="indian-society-02",
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
