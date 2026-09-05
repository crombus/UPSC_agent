"""Regression tests for Governance learner-v2 Topic 06."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_05_sequential as previous
import generate_governance_06_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance06GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-06"],
            ["Digital Public Infrastructure and Data Governance"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-05"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_three_layers_are_separated(self) -> None:
        text = session_markdown(generator, "governance-06")
        self.assertIn("the reusable rails, the specific service delivered on them", text)
        self.assertIn("Puttaswamy", text)
        self.assertIn("cross-linked rather than re-derived here", text)

    def test_stack_components_carry_exact_owners(self) -> None:
        text = session_markdown(generator, "governance-06")
        for phrase in (
            "Aadhaar (Targeted Delivery of Financial and Other Subsidies, "
            "Benefits and Services) Act, 2016",
            "Unique Identification Authority of India",
            "National Payments Corporation of India",
            "DigiLocker",
            "Data Empowerment and Protection Architecture",
            "Open Network for Digital Commerce",
            "Department for Promotion of Industry and Internal Trade",
            "Ayushman Bharat Digital Mission",
            "National Health Authority",
        ):
            self.assertIn(phrase, text)
        self.assertIn("is not proof of citizenship", text)
        self.assertIn(
            "does not create one central government-owned clinical record",
            text,
        )

    def test_commencement_is_stated_by_tranche_and_date(self) -> None:
        text = session_markdown(generator, "governance-06")
        for phrase in (
            "G.S.R. 843(E)",
            "G.S.R. 846(E)",
            "G.S.R. 892(E)",
            "13 November 2025",
            "13 November 2026",
            "13 May 2027",
        ):
            self.assertIn(phrase, text)
        self.assertIn("enacted, commenced and operational are three separate states", text)

    def test_section_44_split_is_correct(self) -> None:
        text = session_markdown(generator, "governance-06")
        self.assertIn(
            "Section 44(3) of the Digital Personal Data Protection Act, 2023 "
            "substitutes section 8(1)(j) of the Right to Information Act, 2005",
            text,
        )
        self.assertIn(
            "section 44(2) amends the Information Technology Act, 2000 and is "
            "deferred to 13 May 2027",
            text,
        )
        self.assertIn("no final judgment was located", text)

    def test_board_status_is_bounded(self) -> None:
        text = session_markdown(generator, "governance-06")
        self.assertIn("Data Protection Board of India", text)
        self.assertIn("one Chairperson and four Members", text)
        self.assertIn(
            "must not be described as hearing complaints, issuing rulings or "
            "imposing penalties",
            text,
        )

    def test_two_consent_constructs_are_distinguished(self) -> None:
        text = session_markdown(generator, "governance-06")
        self.assertIn("technically incapable of viewing, storing or monetising", text)
        self.assertIn(
            "conceptually parallel and legally distinct registrations",
            text,
        )

    def test_exclusion_stack_and_safeguards_are_complete(self) -> None:
        text = session_markdown(generator, "governance-06")
        for phrase in (
            "device access and sharing",
            "connectivity quality and cost",
            "functional digital literacy",
            "authentication failure",
            "necessity and proportionality",
            "data minimisation",
            "assisted and offline fallback",
            "reasoned human review and appeal",
        ):
            self.assertIn(phrase, text)
        self.assertIn("access to the citizen's credentials", text)

    def test_ai_guidelines_are_marked_non_statutory(self) -> None:
        text = session_markdown(generator, "governance-06")
        self.assertIn("India AI Governance Guidelines", text)
        self.assertIn("5 November 2025", text)
        self.assertIn(
            "non-statutory, voluntary-compliance framework rather than an "
            "artificial-intelligence statute or binding code",
            text,
        )

    def test_objective_demands_are_not_converted_into_answers(self) -> None:
        text = session_markdown(generator, "governance-06")
        workbook = workbook_markdown(generator, "governance-06")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(5, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(5, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no option, answer letter or distractor is recorded or inferred", text)
        self.assertIn("record no answer letter", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-06")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "presence-less, paperless, cashless",
            "Purpose limitation vs data-linkage risk",
            "Techno-legal vs purely legal regulation",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-06"),
            topic_key="governance-06",
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
