"""Tests for the Polity 01-05 hostile deep-review support."""

from __future__ import annotations

import unittest

import regenerate_polity_01_05_deep_review as deep


class PolityDeepReviewTests(unittest.TestCase):
    def test_scope_starts_with_topics_01_05(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 6)],
            [topic.topic_key for topic in deep.topics()[:5]],
        )

    def test_owner_controls_are_constitutionally_specific(self) -> None:
        expected = {
            1: ("1935", "1909", "1919"),
            2: ("Article 393", "Article 394", "Article 395"),
            3: ("Part XVIII", "97th Amendment", "Rajendra N. Shah"),
            4: ("Berubari", "Kesavananda", "2024 INSC 893"),
            5: ("Article 3", "First/Fourth Schedules", "100th Amendment"),
        }
        for number, terms in expected.items():
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            self.assertIn("Four-ledger hostile audit", control)
            self.assertIn("Verified PYQ ownership, 2018-2026", control)
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_authoritative_and_date_controlled(self) -> None:
        expected_hosts = {
            1: ("legislative.gov.in",),
            2: ("legislative.gov.in", "pib.gov.in", "sansad.in"),
            3: ("legislative.gov.in", "sci.gov.in"),
            4: ("legislative.gov.in", "sci.gov.in"),
            5: ("legislative.gov.in", "indiacode.nic.in", "mha.gov.in", "sci.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_owner_supplement_is_idempotent_and_basic_first(self) -> None:
        topic = deep.topics()[0]
        source = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        markdown = deep.repo(source["markdown"]).read_text(encoding="utf-8")
        repaired = deep.augment_topic_semantic_content(topic, markdown)
        second = deep.augment_topic_semantic_content(topic, repaired)
        self.assertEqual(repaired, second)
        marker = "Semantic-completeness ownership and PYQ control"
        self.assertEqual(1, repaired.count(marker))
        self.assertLess(repaired.index(marker), repaired.index("## BASIC MCQS"))
        self.assertLess(
            repaired.index("## BASIC MCQS"),
            repaired.index("## OPTIONAL ADVANCED DEPTH"),
        )
        self.assertLess(
            repaired.index("## OPTIONAL ADVANCED DEPTH"),
            repaired.index("## CONSOLIDATED REGISTER NOTES"),
        )

    def test_ascii_configs_have_twelve_manually_authored_panels(self) -> None:
        for topic in deep.topics():
            config = deep.CURRENT_AUTHORING_CONFIGS[topic.topic_key]
            self.assertEqual(12, len(config["panels"]))
            self.assertEqual(12, len({panel[0] for panel in config["panels"]}))
            for title, structural_type, body, _ in config["panels"]:
                self.assertTrue(title)
                self.assertTrue(structural_type)
                self.assertGreaterEqual(len(body.splitlines()), 4)


if __name__ == "__main__":
    unittest.main()
