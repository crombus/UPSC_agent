"""Regression tests for Social Justice learner-v2 Topic 01."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_01_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice01GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-01"],
            ["Social Justice, Inclusion and Welfare-State Framework"],
        )

    def test_this_is_the_first_topic_of_the_sequence(self) -> None:
        self.assertIsNone(generator.main.__defaults__)
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=None", source)
        self.assertIn("previous_keys=None", source)

    def test_conceptual_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-01")
        for phrase in (
            "Distributive justice",
            "Corrective justice",
            "Recognitive justice",
            "capability approach",
            "functionings",
            "Nussbaum",
            "difference principle",
            "Nancy Fraser",
            "Ambedkar",
            "Horizontal equity",
            "vertical equity",
            "inclusion error",
            "exclusion error",
            "residual",
            "institutional",
        ):
            self.assertIn(phrase, text)

    def test_constitutional_anchor_is_exact_and_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-01")
        for phrase in (
            "Preamble",
            "Articles 38, 39, 41 to 43 and 46 to 47",
            "Article 46",
            "Minerva Mills",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "not directly justiciable and create no individual cause of action",
            text,
        )

    def test_international_standard_status_is_not_upgraded(self) -> None:
        text = session_markdown(generator, "social-justice-01")
        self.assertIn("Social Protection Floors Recommendation, 2012", text)
        self.assertIn("2 September 2026", text)
        self.assertIn("access to essential health care including maternity care", text)
        self.assertIn(
            "a Recommendation rather than a ratified Convention, so it creates no "
            "self-executing domestic legal obligation",
            text,
        )

    def test_verified_pyq_ownership_is_transparent(self) -> None:
        text = session_markdown(generator, "social-justice-01")
        workbook = workbook_markdown(generator, "social-justice-01")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        for phrase in (
            "2019 General Studies Paper II Question 6",
            "2023 General Studies Paper I Question 16",
            "2024 General Studies Paper I Question 18",
            "2025 General Studies Paper II Question 16",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "No objective demand is routed to this topic in the audited",
            text,
        )
        self.assertIn("Why this earns marks", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_owner_pyq_ledger_extract_is_carried(self) -> None:
        text = session_markdown(generator, "social-justice-01")
        self.assertIn("OWNER PYQ LEDGER EXTRACTS", text)
        self.assertIn(
            "Underprivileged sections not getting full benefits of affirmative action",
            text,
        )

    def test_indicator_and_status_boundary_is_declared(self) -> None:
        text = session_markdown(generator, "social-justice-01")
        self.assertIn(
            "no Human Development Index or Multidimensional Poverty Index value, "
            "rank or year",
            text,
        )
        self.assertIn("no scheme eligibility rule or coverage count", text)
        self.assertIn("no budget or expenditure number", text)

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-01")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Central capabilities (Nussbaum list)",
            "Inclusion error vs exclusion error",
            "Horizontal vs vertical equity",
            "Residual vs institutional welfare state",
            "Commission overload",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-01"),
            topic_key="social-justice-01",
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
