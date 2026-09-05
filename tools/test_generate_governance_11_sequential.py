"""Regression tests for Governance learner-v2 Topic 11."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_10_sequential as previous
import generate_governance_11_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance11GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-11"],
            ["Regulatory Governance and Independent Regulators"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-10"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_trilemma_is_paired_not_listed(self) -> None:
        text = session_markdown(generator, "governance-11")
        self.assertIn("autonomy", text.casefold())
        self.assertIn("independence is a variable to be calibrated", text)
        self.assertIn("annual report laid before Parliament", text)
        self.assertIn("audit of the regulator's own accounts", text)
        self.assertIn("mandatory consultation with a published response", text)

    def test_each_regulator_has_its_own_statute(self) -> None:
        text = session_markdown(generator, "governance-11")
        self.assertIn("each created by their own separate statute", text)
        self.assertIn(
            "the standard trap is to assume they share a uniform independence",
            text,
        )

    def test_capture_is_described_as_lawful(self) -> None:
        text = session_markdown(generator, "governance-11")
        for phrase in (
            "information asymmetry",
            "revolving door",
            "agenda and framing capture",
            "treating capture as a synonym for corruption",
        ):
            self.assertIn(phrase, text)
        self.assertIn("ministerial capture", text.casefold())

    def test_competition_regulator_is_exact_and_case_free(self) -> None:
        text = session_markdown(generator, "governance-11")
        for phrase in (
            "Competition Act, 2002",
            "National Company Law Appellate Tribunal",
            "dominance itself is not unlawful and only its abuse is",
            "tying and bundling",
        ):
            self.assertIn(phrase, text)
        self.assertIn("read on 2 September 2026", text)
        self.assertIn("https://www.cci.gov.in/", generator.TOPICS[0]["live_sources"])

    def test_tribunal_reform_status_is_dated_and_unresolved(self) -> None:
        text = session_markdown(generator, "governance-11")
        for phrase in (
            "Tribunals Reforms Act, 2021",
            "2025 INSC 1330",
            "19 November 2025",
            "fifty-year minimum age",
            "two-name recommendation panel",
            "Madras Bar Association",
            "National Tribunals Commission",
            "9 March 2026",
            "8 September 2026",
        ):
            self.assertIn(phrase, text)
        self.assertIn("must be described as unresolved", text)
        self.assertIn("did not abolish all tribunals in India", text)

    def test_financial_architecture_proposal_is_not_adoption(self) -> None:
        text = session_markdown(generator, "governance-11")
        for phrase in (
            "Financial Sector Legislative Reforms Commission",
            "B.N. Srikrishna",
            "Unified Financial Agency",
            "Indian Financial Code",
            "regulation-by-activity principle",
        ):
            self.assertIn(phrase, text)
        self.assertIn("as a partial related step rather than as adoption", text)

    def test_trust_based_regulation_is_bounded(self) -> None:
        text = session_markdown(generator, "governance-11")
        self.assertIn("Jan Vishwas", text)
        self.assertIn("one hundred and eighty-three provisions across forty-two Central Acts", text)
        self.assertIn("decriminalisation is not deregulation", text)

    def test_routed_demands_and_recorded_ownership_conflict(self) -> None:
        text = session_markdown(generator, "governance-11")
        workbook = workbook_markdown(generator, "governance-11")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(3, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "Discuss the role of the Competition Commission of India in containing "
            "the abuse of dominant position by the Multi-National Corporations in India",
            text,
        )
        self.assertIn(
            "routes that demand to the Polity administrative-tribunals owner",
            text,
        )
        self.assertIn("no option, answer letter or distractor is recorded or inferred", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-11")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "De jure vs de facto independence",
            "Tribunalisation's dual rationale and dual risk",
            "Search-cum-selection committees as a capture safeguard",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-11"),
            topic_key="governance-11",
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
