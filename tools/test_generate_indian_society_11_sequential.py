"""Regression tests for Indian Society learner-v2 Topic 11."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_10_sequential as previous
import generate_indian_society_11_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety11GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-11"],
            ["Effects of Globalisation on Indian Society"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-10"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_globalisation_channels_and_distinctions_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-11")
        for phrase in (
            "glocalisation",
            "homogenisation",
            "structural consumerism",
            "cultural consumerism",
            "bounded rationality",
            "fast-food paradox",
            "digital divide",
            "service-sector",
            "remittance",
            "glocalised",
        ):
            self.assertIn(phrase, text)

    def test_labour_statistics_carry_period_and_boundary(self) -> None:
        text = session_markdown(generator, "indian-society-11")
        self.assertIn("Periodic Labour Force Survey Annual Report 2023-24", text)
        self.assertIn("23 September 2024", text)
        self.assertIn("41.7 per cent", text)
        self.assertIn("40.0 per cent", text)
        self.assertIn("January to December 2025 reference period", text)
        self.assertIn("never proof of that stream", text)

    def test_provisional_survey_status_is_stated(self) -> None:
        text = session_markdown(generator, "indian-society-11")
        self.assertIn("64.3 per cent", text)
        self.assertIn("33.3 per cent", text)
        self.assertIn("labelled provisional", text)
        self.assertIn("current connectivity estimate", text)

    def test_routed_pyq_status_is_transparent_and_unfabricated(self) -> None:
        text = session_markdown(generator, "indian-society-11")
        workbook = workbook_markdown(generator, "indian-society-11")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(6, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(6, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no verbatim wording is claimed", text)
        self.assertIn(
            "Do you think that globalization results in only an aggressive "
            "consumer culture?",
            text,
        )
        self.assertIn(
            "Globalization has increased urban migration by skilled, young, "
            "unmarried women from various classes.",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_cross_owner_conflict_is_recorded_not_resolved(self) -> None:
        text = session_markdown(generator, "indian-society-11")
        self.assertIn("Social Change and Modernisation owner", text)
        self.assertIn("cross-owner conflict", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-11")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Consumer-culture-versus-multi-domain chain (2025 Q10)",
            "Women's-migration-family chain (2024 Q19)",
            "Fast-food-paradox chain (2025 Q18)",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-11"),
            topic_key="indian-society-11",
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
