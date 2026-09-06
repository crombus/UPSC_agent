"""Tests for the Polity 16-20 hostile deep-review extension."""

from __future__ import annotations

import unittest

import regenerate_polity_16_20_deep_review as deep


class Polity1620DeepReviewTests(unittest.TestCase):
    def test_scope_contains_topics_01_20_for_runner_indexing(self) -> None:
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 21)],
            [topic.topic_key for topic in deep.topics()],
        )

    def test_new_controls_are_legally_specific(self) -> None:
        expected = {
            16: ("Article 75(3)", "Allocation of Business", "Article 77"),
            17: ("Article 110", "S.O. 1922(E)", "Article 334A"),
            18: ("Act 14 of 2026", "thirty-eight", "Article 142"),
            19: ("2025", "Article 161", "death sentence"),
            20: ("Article 169", "Padi Kaushik Reddy", "Article 207(3)"),
        }
        for number, terms in expected.items():
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            self.assertIn("Four-ledger", control)
            for term in terms:
                self.assertIn(term, control)

    def test_live_sources_are_official_and_date_controlled(self) -> None:
        expected_hosts = {
            16: ("legislative.gov.in", "pmindia.gov.in", "cabsec.gov.in"),
            17: ("legislative.gov.in", "sansad.in", "egazette.gov.in", "censusindia.gov.in"),
            18: ("legislative.gov.in", "sci.gov.in", "egazette.gov.in"),
            19: ("legislative.gov.in", "api.sci.gov.in"),
            20: ("legislative.gov.in", "sansad.in", "api.sci.gov.in"),
        }
        for number, hosts in expected_hosts.items():
            sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[number]
            for host in hosts:
                self.assertTrue(any(host in source for source in sources))
            self.assertIn("Rechecked 2026-09-05", note)

    def test_new_ascii_configs_have_twelve_authored_panels(self) -> None:
        for number in range(16, 21):
            key = f"polity-{number:02d}"
            panels = deep.CURRENT_AUTHORING_CONFIGS[key]["panels"]
            self.assertEqual(12, len(panels))
            self.assertEqual(12, len({panel[0] for panel in panels}))
            for title, structural_type, body, _ in panels:
                self.assertTrue(title)
                self.assertTrue(structural_type)
                self.assertGreaterEqual(len(body.splitlines()), 4)

    def test_current_law_repairs_remove_known_falsehoods(self) -> None:
        supreme = "\n".join(
            panel[2] for panel in deep.CURRENT_AUTHORING_CONFIGS["polity-18"]["panels"]
        )
        governor = "\n".join(
            panel[2] for panel in deep.CURRENT_AUTHORING_CONFIGS["polity-19"]["panels"]
        )
        self.assertIn("sanctioned 38 including CJI", supreme)
        self.assertNotIn("sanctioned 34 including CJI", supreme)
        self.assertIn("may pardon death within that field", governor)
        self.assertNotIn("cannot pardon death sentence", governor)
        overrides = (
            deep.ROOT / "tools" / "deep_content_quality_overrides.json"
        ).read_text(encoding="utf-8")
        self.assertNotIn("cannot pardon a death sentence, though", overrides)
        self.assertNotIn("the missing power is pardon", overrides)
        self.assertNotIn("cannot exercise those same limbs", overrides)

    def test_missing_manifest_sources_are_supplied_without_reordering(self) -> None:
        topics = deep.topics()
        for number in range(16, 21):
            topic = topics[number - 1]
            self.assertTrue(topic.cross_topic_sources)
            self.assertTrue(topic.pyq_sources)
            self.assertTrue(all(path.is_file() for path in topic.cross_topic_sources))
            self.assertTrue(all(path.is_file() for path in topic.pyq_sources))

    def test_repairs_are_idempotent(self) -> None:
        samples = {
            16: "| **Non-MP limit** | **6 months** (SC 1997) |",
            18: "sanctioned 34 including CJI | official sitting roster 34 | retirement 65",
            19: "Governor cannot pardon death sentence but may suspend/remit/commute.",
        }
        for number, source in samples.items():
            repaired = deep._repair_current_law(number, source)
            self.assertEqual(repaired, deep._repair_current_law(number, repaired))
            self.assertNotEqual(source, repaired)
        trap = (
            "The President can pardon a death sentence and court-martial "
            "punishment; the Governor cannot exercise those same limbs."
        )
        repaired = deep._repair_current_law(19, trap)
        self.assertIn("State offence-law field", repaired)
        self.assertNotIn("cannot exercise those same limbs", repaired)

    def test_nonstandard_answer_lines_are_counted(self) -> None:
        markdown = """## BASIC MCQS / REMEDIATION
#### OM1. First
A. one
B. two
C. three
D. four
**Answer: A.** [FACT]
#### OM2. Second
A. one
B. two
C. three
D. four
**Answer: B.** [FACT]
## PYQS AND ANSWER PRACTICE
"""
        _, metrics = deep.enforce_strict_rotation(markdown)
        self.assertEqual(2, metrics["count"])
        self.assertEqual(["A", "B"], metrics["keys"])

    def test_graphical_validator_normalizes_new_topic_case_years(self) -> None:
        self.assertIs(
            deep.deep.deep.deep.carvaka_flowchart.validate_spec,
            deep._validate_polity_graphical_spec,
        )


if __name__ == "__main__":
    unittest.main()
