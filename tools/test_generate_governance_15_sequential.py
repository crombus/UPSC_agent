"""Regression tests for Governance learner-v2 Topic 15."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_14_sequential as previous
import generate_governance_15_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance15GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-15"],
            ["Monitoring, Evaluation and Outcomes"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-14"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_results_chain_is_complete_and_ordered(self) -> None:
        text = session_markdown(generator, "governance-15")
        for rung in ("input", "activity", "output", "outcome", "impact"):
            self.assertIn(rung, text)
        self.assertIn(
            "most Indian scheme reporting stops at the output rung",
            text,
        )
        self.assertIn("name the rung on which a cited statistic sits", text)

    def test_evaluation_office_is_dated_and_bounded(self) -> None:
        text = session_markdown(generator, "governance-15")
        self.assertIn("attached office of NITI Aayog", text)
        self.assertIn("constituted in September 2015", text)
        self.assertIn("Program Evaluation Office", text)
        self.assertIn("Independent Evaluation Office", text)
        self.assertIn("read on 2 September 2026", text)
        self.assertIn("https://dmeo.gov.in/", generator.TOPICS[0]["live_sources"])
        self.assertIn(
            "it is an evaluator without authority to redesign",
            text,
        )

    def test_budget_framework_coverage_carries_its_year_rule(self) -> None:
        text = session_markdown(generator, "governance-15")
        self.assertIn("Output-Outcome Monitoring Framework", text)
        self.assertIn("Budget Division", text)
        self.assertIn("it does not cover every scheme in every year", text)
        self.assertIn(
            "must always be cited with its Budget year and never carried forward",
            text,
        )

    def test_district_and_block_programmes_are_kept_separate(self) -> None:
        text = session_markdown(generator, "governance-15")
        self.assertIn("Aspirational Districts Programme", text)
        self.assertIn("one hundred and twelve districts", text)
        self.assertIn("forty-nine key performance indicators", text)
        self.assertIn("Champions of Change", text)
        self.assertIn("Aspirational Blocks Programme", text)
        self.assertIn("five hundred and thirteen blocks", text)
        self.assertIn(
            "merging district and block unit counts or their indicator sets",
            text,
        )

    def test_delta_ranking_carries_its_gaming_risk(self) -> None:
        text = session_markdown(generator, "governance-15")
        self.assertIn("rate of improvement over a defined period", text)
        self.assertIn("gamed through baseline understatement", text)

    def test_attribution_baseline_and_method_limits_are_present(self) -> None:
        text = session_markdown(generator, "governance-15")
        for phrase in (
            "whether it moved because of the intervention",
            "requires a counterfactual",
            "without a baseline measured before the intervention",
            "limited external validity",
            "only as reliable as the incentive of whoever enters the data",
        ):
            self.assertIn(phrase, text)

    def test_indicator_failure_modes_are_paired_with_corrections(self) -> None:
        text = session_markdown(generator, "governance-15")
        for phrase in (
            "Goodhart",
            "aggregation masking",
            "output substitution",
            "definition drift",
            "resistant to manipulation",
        ):
            self.assertIn(phrase, text)

    def test_zero_direct_pyq_audit_is_transparent_and_unmanufactured(self) -> None:
        text = session_markdown(generator, "governance-15")
        workbook = workbook_markdown(generator, "governance-15")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertNotIn("### PYQ DEMAND CARD", text)
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertIn(
            "No question has been invented from the locally held OCR-searchable "
            "official papers",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-15")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Delta-ranking vs absolute-ranking",
            "Self-reported dashboard data vs independently validated data",
            "DMEO REESI+C+E framework",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-15"),
            topic_key="governance-15",
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
