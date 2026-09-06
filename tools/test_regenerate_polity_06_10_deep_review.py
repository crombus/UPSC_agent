"""Tests for the Polity 06-10 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_06_10_deep_review as deep


class Polity0610DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_10_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 11)],
            [topic.topic_key for topic in deep.topics()[:10]],
        )

    def test_new_controls_are_legally_specific(self) -> None:
        expected = {
            6: ("Article 9", "Section 6A", "G.S.R. 742(E)"),
            7: ("Article 226", "Davinder Singh", "G.S.R. 843(E)"),
            8: ("Article 31C", "Property Owners Association", "7 April 2026"),
            9: ("Article 51A", "Swaran Singh", "Durga Dutt"),
            10: ("Article 279A", "Anjum Kadari", "S.O. 1922(E)"),
        }
        for number, terms in expected.items():
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            self.assertIn("Four-ledger", control)
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_official_and_date_controlled(self) -> None:
        expected_hosts = {
            6: ("legislative.gov.in", "indiacode.nic.in", "mha.gov.in", "sci.gov.in"),
            7: ("legislative.gov.in", "sci.gov.in", "meity.gov.in"),
            8: ("legislative.gov.in", "sci.gov.in", "nalsa.gov.in", "ucc.uk.gov.in"),
            9: ("legislative.gov.in", "sci.gov.in", "indiacode.nic.in"),
            10: ("legislative.gov.in", "sci.gov.in", "egazette.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(6, 11):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            for title, structural_type, body, _ in panels:
                self.assertTrue(title)
                self.assertTrue(structural_type)
                self.assertGreaterEqual(len(body.splitlines()), 4)

    def test_owner_supplement_is_idempotent(self) -> None:
        topic = deep.topics()[5]
        source = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        markdown = deep.repo(source["markdown"]).read_text(encoding="utf-8")
        repaired = deep.deep.augment_topic_semantic_content(topic, markdown)
        second = deep.deep.augment_topic_semantic_content(topic, repaired)
        self.assertEqual(repaired, second)
        self.assertEqual(
            1, repaired.count("Semantic-completeness ownership and PYQ control")
        )


if __name__ == "__main__":
    unittest.main()
