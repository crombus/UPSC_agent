"""Regression tests for Indian Society learner-v2 Topic 01."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_01_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)


class IndianSociety01GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-01"],
            ["Salient Features and Diversity of Indian Society"],
        )

    def test_diversity_evidence_and_claim_limits_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-01")
        for phrase in (
            "75 Particularly Vulnerable Tribal Groups",
            "18 States and the Union Territory of Andaman and Nicobar Islands",
            "9 July 2024",
            "121 languages",
            "States Reorganisation Act, 1956",
            "S.O. 2681(E)",
            "VERIFIED PYQ OWNERSHIP AUDIT",
        ):
            self.assertIn(phrase, text)

    def test_verified_pyq_wording_is_reproduced_without_invention(self) -> None:
        text = session_markdown(generator, "indian-society-01")
        self.assertIn(
            "Critically analyse the proposition that there is a high correlation "
            "between India's cultural diversities and socio-economic marginalities.",
            text,
        )
        self.assertIn(
            "What makes the Indian society unique in sustaining its culture?",
            text,
        )
        self.assertIn("routing artefacts", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-01")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Cross-cutting cleavage",
            "Recognition versus redistribution",
            "Aggregation masking",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-01"),
            topic_key="indian-society-01",
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
