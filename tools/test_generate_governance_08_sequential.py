"""Regression tests for Governance learner-v2 Topic 08."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_07_sequential as previous
import generate_governance_08_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance08GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-08"],
            ["Transparency, Accountability, RTI, Grievance Redress and Social Audit"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-07"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_three_part_chain_is_separated(self) -> None:
        text = session_markdown(generator, "governance-08")
        self.assertIn("transparency, meaning visibility of records", text)
        self.assertIn("answerability, meaning an identifiable authority obliged to explain", text)
        self.assertIn("enforceability, meaning correction, remedy or consequence", text)
        self.assertIn(
            "built the first extensively, the second unevenly and the third rarely",
            text,
        )

    def test_information_route_timelines_are_exact(self) -> None:
        text = session_markdown(generator, "governance-08")
        for phrase in (
            "Right to Information Act, 2005",
            "ordinarily 30 days",
            "48 hours",
            "within 90 days",
            "two hundred and fifty rupees per day",
            "twenty-five thousand rupees",
        ):
            self.assertIn(phrase, text)
        self.assertIn("does not create information, order a service", text)

    def test_exemption_structure_and_current_status(self) -> None:
        text = session_markdown(generator, "governance-08")
        self.assertIn("section 8(2) public-interest override", text)
        self.assertIn("section 24", text)
        self.assertIn(
            "stands substituted by section 44(3) of the Digital Personal Data "
            "Protection Act, 2023",
            text,
        )
        self.assertIn("13 and 14 November 2025", text)
        self.assertIn(
            "the challenge is stated as pending and no outcome is asserted",
            text,
        )

    def test_social_audit_statutory_basis_is_complete(self) -> None:
        text = session_markdown(generator, "governance-08")
        for phrase in (
            "Section 17 of the Mahatma Gandhi National Rural Employment Guarantee Act, 2005",
            "Audit of Schemes Rules, 2011",
            "State Social Audit Unit",
            "at least once every six months",
            "Meghalaya Community Participation and Public Services Social Audit Act, 2017",
        ):
            self.assertIn(phrase, text)
        self.assertIn("must not be presented as a national model in force", text)

    def test_dual_layer_design_is_not_contrasted(self) -> None:
        text = session_markdown(generator, "governance-08")
        self.assertIn(
            "it is incorrect to contrast a community-only model with a "
            "separate-unit model",
            text,
        )
        self.assertIn("capture can arise at either layer", text)

    def test_answerability_and_enforceability_tests(self) -> None:
        text = session_markdown(generator, "governance-08")
        self.assertIn("independence test", text.casefold())
        self.assertIn("follow-up test", text.casefold())
        self.assertIn("answerability without enforceability", text)
        self.assertIn("breaks between verification and follow-up", text)

    def test_routing_and_four_functions_are_stated(self) -> None:
        text = session_markdown(generator, "governance-08")
        for phrase in (
            "Articles 148 to 151",
            "Central Vigilance Commission Act, 2003",
            "Lokpal and Lokayuktas Act, 2013",
            "Audit examines records and systems after the fact",
            "adjudication decides rights between parties with due process",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "no operative route until the data-protection Board's members are appointed",
            text,
        )

    def test_whistle_blower_gap_is_stated_exactly(self) -> None:
        text = session_markdown(generator, "governance-08")
        self.assertIn("Whistle Blowers Protection Act, 2014", text)
        self.assertIn("9 May 2014", text)
        self.assertIn("has still not been brought into force by notification", text)
        self.assertIn("enacted but not commenced", text)

    def test_routed_demands_and_provisional_key_discipline(self) -> None:
        text = session_markdown(generator, "governance-08")
        workbook = workbook_markdown(generator, "governance-08")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(5, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(5, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("2026 Set-A key held locally is provisional", text)
        self.assertIn("record no answer letter", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-08")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Statutory mandate vs administrative guideline",
            "Answerability without enforceability",
            "RTI remedy boundary",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-08"),
            topic_key="governance-08",
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
