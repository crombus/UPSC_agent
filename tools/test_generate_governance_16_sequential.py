"""Regression tests for Governance learner-v2 Topic 16."""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_governance_15_sequential as previous
import generate_governance_16_sequential as generator
import validate_v2_export as validator
from governance_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class Governance16GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["governance-16"],
            ["Sports Governance, Institutions and Major Tournaments"],
        )

    def test_canonical_owner_title_is_preserved_with_plural_tournaments(self) -> None:
        self.assertEqual(
            "Sports Governance, Institutions and Major Tournaments",
            generator.TOPICS[0]["title"],
        )
        self.assertTrue(Path(generator.TOPICS[0]["basic"]).is_file())
        self.assertTrue(Path(generator.TOPICS[0]["advanced"]).is_file())
        self.assertIn(
            "16_Sports-Governance-Institutions-and-Major-Tournaments",
            str(generator.TOPICS[0]["basic"]),
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["governance-15"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_governance_layers_and_institutional_roles_are_exact(self) -> None:
        text = session_markdown(generator, "governance-16")
        for phrase in (
            "International Olympic Committee",
            "World Anti-Doping Code",
            "Court of Arbitration for Sport",
            "Ministry of Youth Affairs and Sports",
            "Sports Authority of India",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "does not organise tournaments",
            text,
        )

    def test_autonomy_is_bounded_and_monopoly_is_named(self) -> None:
        text = session_markdown(generator, "governance-16")
        self.assertIn(
            "it does not confer immunity from national law",
            text,
        )
        self.assertIn("structural monopoly", text)
        self.assertIn("no exit for the athlete", text)

    def test_tournament_architecture_and_entry_routes_are_precise(self) -> None:
        text = session_markdown(generator, "governance-16")
        for phrase in (
            "Australian Open, Roland-Garros, Wimbledon and the US Open",
            "common Grand Slam Rule Book",
            "direct ranking acceptance",
            "protected or special entry",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "a limit on the number of wild-card slots available in a draw is not "
            "the same thing as a cap",
            text,
        )
        self.assertIn(
            "an age threshold in a rule book is an eligibility condition",
            text,
        )

    def test_statute_trail_and_status_ladder_are_complete(self) -> None:
        text = session_markdown(generator, "governance-16")
        for phrase in (
            "National Sports Governance Act, 2025",
            "23 July 2025",
            "18 August 2025",
            "Act No. 25 of 2025",
            "1 January 2026",
            "12 May 2026",
            "S.O. 2406(E)",
            "National Sports Board",
            "National Sports Tribunal",
            "National Sports Development Code of India, 2011",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "enactment is not commencement of a provision",
            text,
        )
        self.assertIn(
            "was not located in a commenced tranche as of 13 August 2026",
            text,
        )

    def test_anti_doping_layer_marks_the_unverified_amendment(self) -> None:
        text = session_markdown(generator, "governance-16")
        self.assertIn("National Anti-Doping Act, 2022", text)
        self.assertIn("National Anti-Doping (Amendment) Act, 2025", text)
        self.assertIn(
            "recorded from secondary reporting rather than from a gazette text",
            text,
        )
        self.assertIn("strict liability", text)

    def test_legal_character_distinctions_are_correct(self) -> None:
        text = session_markdown(generator, "governance-16")
        self.assertIn(
            "registered as a society under the Societies Registration Act, 1860",
            text,
        )
        self.assertIn(
            "is not a statutory corporation created by its own Act",
            text,
        )
        self.assertIn("based in Lausanne and established in 1984", text)

    def test_no_decorative_match_or_athlete_trivia_is_asserted(self) -> None:
        text = session_markdown(generator, "governance-16")
        register = text.split("## CONSOLIDATED REGISTER NOTES", 1)[1]
        self.assertIn("no medal tally, funding figure or tournament result", register)
        self.assertNotRegex(
            register,
            r"(?i)\bwon the (?:title|final|gold)\b|\bmedal tally of\b",
        )

    def test_live_official_anchor_is_dated_and_policy_intention_is_bounded(self) -> None:
        text = session_markdown(generator, "governance-16")
        self.assertIn("read on 2 September 2026", text)
        self.assertIn(
            "https://yas.gov.in/sports/national-sports-governance-act-2025",
            generator.TOPICS[0]["live_sources"],
        )
        self.assertIn(
            "recorded as a stated policy intention and not as a claim about the "
            "present entry-list position",
            text,
        )

    def test_routed_objective_demand_infers_no_answer(self) -> None:
        text = session_markdown(generator, "governance-16")
        workbook = workbook_markdown(generator, "governance-16")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(1, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(1, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn(
            "no option, answer letter or distractor is recorded or inferred",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "governance-16")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Central tension",
            "Analytical matrix",
            "Mains framework",
        ):
            self.assertIn(phrase, advanced)

    def test_mcq_rotation_is_strict_in_both_deliverables(self) -> None:
        text = session_markdown(generator, "governance-16")
        workbook = workbook_markdown(generator, "governance-16")
        pattern = r"(?m)^\*\*Answer: ([ABCD])\.\*\*$"
        self.assertEqual(list("ABCD") * 20, re.findall(pattern, text))
        self.assertEqual(list("ABCD") * 20, re.findall(pattern, workbook))

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "governance-16"),
            topic_key="governance-16",
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
