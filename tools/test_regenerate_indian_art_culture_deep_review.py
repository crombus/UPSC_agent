"""Targeted tests for the live Indian Art and Culture deep-review driver."""

from __future__ import annotations

import unittest
from pathlib import Path

import regenerate_indian_art_culture_deep_review as deep


class IndianArtCultureDeepReviewTests(unittest.TestCase):
    def test_manifest_order_contains_all_live_topics_without_fabrication(self) -> None:
        topics = deep.topics()
        self.assertEqual(15, len(topics))
        self.assertEqual(
            [f"indian-art-and-culture-{number:02d}" for number in range(1, 16)],
            [topic.topic_key for topic in topics],
        )

    def test_architecture_controls_preserve_attribution_limits(self) -> None:
        harappan = deep._review_block(deep.topics()[0])
        self.assertIn("no palace or temple is securely identified", harappan)
        islamic = deep._review_block(deep.topics()[3])
        self.assertIn("Arches and domes were not wholly unknown", islamic)
        colonial = deep._review_block(deep.topics()[4])
        self.assertIn("Indo-Gothic and Lutyens-Baker", colonial)

    def test_performing_arts_controls_keep_classifications_separate(self) -> None:
        music = deep._review_block(deep.topics()[7])
        self.assertIn("seventy-two Carnatic melakartas", music)
        dance = deep._review_block(deep.topics()[8])
        self.assertIn("108 refers to karanas", dance)
        theatre = deep._review_block(deep.topics()[9])
        self.assertIn("Lokadharmi is realistic", theatre)

    def test_heritage_and_language_status_firewalls_are_explicit(self) -> None:
        language = deep._review_block(deep.topics()[10])
        self.assertIn("composition, redaction, manuscript and recognition", language)
        heritage = deep._review_block(deep.topics()[13])
        self.assertIn("Tentative List is not inscription", heritage)
        crafts = deep._review_block(deep.topics()[11])
        self.assertIn("neither UNESCO status nor a quality certificate", crafts)

    def test_review_lines_respect_ascii_width(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_long_output_paths_remain_windows_safe(self) -> None:
        for topic in deep.topics():
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_authored_q_heading_mcqs_are_rotated(self) -> None:
        source = """# Topic

## BASIC MCQS / REMEDIATION

### Q1. Which monument pairing is correct?
A. wrong
B. correct pairing
C. wronger
D. wrongest

**Answer: B.**

## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.enforce_strict_rotation(source)
        self.assertEqual(["A"], metrics["keys"])
        self.assertIn("A. correct pairing", repaired)

    def test_original_mains_gets_full_exam_contract(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Discuss the evolution of the artistic form. Answer in 250 words.
**Model thesis:** Form changed through patronage and regional adaptation.
**Claim → named evidence → analysis → qualification:**
- A named monument supports a bounded claim.
**Qualified conclusion:** Change and continuity coexisted.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(1, metrics["question_count"])
        self.assertIn("**Demand decoding:**", repaired)
        self.assertIn("**Detailed examiner-grade model answer:**", repaired)
        self.assertIn("**Analytical body:**", repaired)
        self.assertIn(
            "**Executable exam-length answer / compression plan:**", repaired
        )
        self.assertIn("**How to improve this answer:**", repaired)

    def test_source_contract_requires_status_and_interpretive_discipline(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        self.assertIn("present status remain distinct", contract)
        self.assertIn("commissioned representation as a social census", contract)
        self.assertIn("approved: false", contract)

    def test_allocation_rereads_section_export_master_and_review(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation = source[source.index("def allocate(") :]
        allocation = allocation[: allocation.index("def _wrapped_review_groups")]
        self.assertIn("load(SECTION_MANIFEST)", allocation)
        base_source = Path(deep._BASE).read_text(encoding="utf-8")
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", base_source)

    def test_unicode_nul_inventory_is_implemented(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn('b"\\0"', source)
        self.assertIn("encode(\"utf-8\")", source)
        self.assertIn("endswith(b\"\\0\")", source)

    def test_shared_validation_has_no_stale_library_topic_count(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        republish = source[source.index("def _republish_master_library") :]
        republish = republish[: republish.index("def _rewrite_command_history")]
        self.assertNotIn("259", republish)
        self.assertIn("count = len(selected_keys)", republish)

    def test_authoritative_scope_has_no_stale_six_topic_blocker(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertNotIn("Expected topics 16-21", source)
        self.assertNotIn('["requested_topic_count"] = 21', source)
        self.assertIn('["requested_topic_count"] = len(topic_rows)', source)


if __name__ == "__main__":
    unittest.main()
