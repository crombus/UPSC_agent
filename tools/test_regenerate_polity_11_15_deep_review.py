"""Tests for the Polity 11-15 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_11_15_deep_review as deep


class Polity1115DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_15_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 16)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_are_legally_specific(self) -> None:
        expected = {
            11: ("Article 75(3)", "Ninety-first Amendment", "129th Amendment"),
            12: ("Bommai", "Article 246A", "Sixteenth Finance Commission"),
            13: ("Article 254", "Special Reference No. 1 of 2025", "Section 6"),
            14: ("Article 358", "S.R. Bommai", "4 February 2026"),
            15: ("Article 61", "Krishna Kumar Singh", "C. P. Radhakrishnan"),
        }
        for number, terms in expected.items():
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            self.assertIn("Four-ledger", control)
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_official_and_date_controlled(self) -> None:
        expected_hosts = {
            11: ("legislative.gov.in", "cabsec.gov.in", "sansad.in"),
            12: ("legislative.gov.in", "sci.gov.in", "fincomindia.nic.in"),
            13: ("legislative.gov.in", "sci.gov.in", "mha.gov.in", "indiacode.nic.in"),
            14: ("legislative.gov.in", "egazette.gov.in", "sci.gov.in"),
            15: ("legislative.gov.in", "presidentofindia.gov.in", "eci.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(11, 16):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            for title, structural_type, body, _ in panels:
                self.assertTrue(title)
                self.assertTrue(structural_type)
                self.assertGreaterEqual(len(body.splitlines()), 4)
        federal_text = "\n".join(
            panel[2] for panel in deep.CURRENT_AUTHORING_CONFIGS["polity-12"]["panels"]
        )
        self.assertIn("2024 West Bengal ruling", federal_text)
        self.assertIn("preliminary objections", federal_text)

    def test_missing_manifest_sources_are_supplied_without_reordering(self) -> None:
        topics = deep.topics()
        for number in range(13, 16):
            topic = topics[number - 1]
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_nonstandard_om_mcqs_are_counted_and_rotation_checked(self) -> None:
        markdown = """## BASIC MCQS / REMEDIATION
#### OM1. First
A. one
B. two
C. three
D. four
**Answer: A.**
#### OM2. Second
A. one
B. two
C. three
D. four
**Answer: B.**
## PYQS AND ANSWER PRACTICE
"""
        _, metrics = deep.enforce_strict_rotation(markdown)
        self.assertEqual(2, metrics["count"])
        self.assertEqual(["A", "B"], metrics["keys"])

    def test_owner_supplement_is_idempotent(self) -> None:
        topic = deep.topics()[10]
        source = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        markdown = deep.repo(source["markdown"]).read_text(encoding="utf-8")
        repaired = deep.deep.deep.augment_topic_semantic_content(topic, markdown)
        second = deep.deep.deep.augment_topic_semantic_content(topic, repaired)
        self.assertEqual(repaired, second)
        self.assertEqual(
            1, repaired.count("Semantic-completeness ownership and PYQ control")
        )


if __name__ == "__main__":
    unittest.main()
