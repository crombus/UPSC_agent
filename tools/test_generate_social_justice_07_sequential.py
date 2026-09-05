"""Regression tests for Social Justice learner-v2 Topic 07."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_social_justice_07_sequential as generator
import validate_v2_export as validator
from social_justice_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class SocialJustice07GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["social-justice-07"],
            ["Scheduled Castes: Rights, Atrocities and Welfare"],
        )

    def test_previous_topic_of_the_sequence_is_pinned(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        self.assertIn("previous=previous", source)
        self.assertIn('previous_keys=["social-justice-06"]', source)

    def test_scheduled_caste_vocabulary_is_preserved(self) -> None:
        text = session_markdown(generator, "social-justice-07")
        for phrase in (
            "Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989",
            "Protection of Civil Rights Act, 1955",
            "Article 17",
            "Article 338",
            "Deputy Superintendent of Police",
            "Special Public Prosecutor",
            "Exclusive Special Court",
            "Section 18A",
            "Prathvi Raj Chauhan",
            "PM-AJAY",
            "NSFDC",
            "Davinder Singh",
            "E.V. Chinnaiah",
            "Presidential List",
        ):
            self.assertIn(phrase, text)

    def test_amendment_sequence_is_not_inverted(self) -> None:
        text = session_markdown(generator, "social-justice-07")
        self.assertIn(
            "Parliament responded by inserting Section 18A",
            text,
        )
        self.assertIn(
            "the 2018 amendment implemented a judicial direction when it in fact "
            "overrode one",
            text,
        )

    def test_judgment_boundaries_are_not_widened(self) -> None:
        text = session_markdown(generator, "social-justice-07")
        self.assertIn("1 August 2024", text)
        self.assertIn("seven-judge Constitution Bench by a majority of six to one", text)
        self.assertIn(
            "does not alter the Presidential List of Scheduled Castes, does not "
            "itself allot any sub-quota",
            text,
        )
        self.assertIn(
            "no general creamy-layer exclusion for those categories has been "
            "legislated",
            text,
        )

    def test_court_notification_is_not_universalised(self) -> None:
        text = session_markdown(generator, "social-justice-07")
        self.assertIn(
            "concurrence of the Chief Justice of the concerned High Court",
            text,
        )
        self.assertIn(
            "must not be stated that an Exclusive Special Court automatically "
            "exists in every district",
            text,
        )

    def test_registered_data_are_not_read_as_prevalence(self) -> None:
        text = session_markdown(generator, "social-justice-07")
        self.assertIn("16.6", text)
        self.assertIn(
            "a rise may reflect rising victimisation, improving reporting or both",
            text,
        )

    def test_transparent_zero_direct_pyq_audit(self) -> None:
        text = session_markdown(generator, "social-justice-07")
        workbook = workbook_markdown(generator, "social-justice-07")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertNotIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertIn(
            "route no General Studies Mains demand and no objective demand to "
            "this owner",
            text,
        )
        self.assertIn(
            "routes it to the Polity commissions owner",
            text,
        )
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_verified_live_source_is_bounded(self) -> None:
        text = session_markdown(generator, "social-justice-07")
        self.assertEqual(1, len(generator.TOPICS[0]["live_sources"]))
        self.assertIn(
            "socialjustice.gov.in",
            generator.TOPICS[0]["live_sources"][0],
        )
        self.assertIn("March 2021", text)
        self.assertIn(
            "no coverage, disbursement or beneficiary count is asserted",
            text,
        )

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "social-justice-07")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "PoA Act 1989 vs 2015 Amendment",
            "Davinder Singh sub-classification",
            "NCRB atrocity data",
            "Political-economy trade-off",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "social-justice-07"),
            topic_key="social-justice-07",
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
