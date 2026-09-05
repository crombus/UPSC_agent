"""Targeted tests for the 21-topic World History deep-review driver."""

from __future__ import annotations

import unittest
from pathlib import Path

import regenerate_world_history_deep_review as deep


class WorldHistoryDeepReviewTests(unittest.TestCase):
    def test_manifest_order_contains_all_twenty_one_topics(self) -> None:
        topics = deep.topics()
        self.assertEqual(21, len(topics))
        self.assertEqual(
            [f"world-history-{number:02d}" for number in range(1, 22)],
            [topic.topic_key for topic in topics],
        )

    def test_review_controls_cover_exact_chronology(self) -> None:
        america = deep._review_block(deep.topics()[1])
        for phrase in ("Stamp Act (1765)", "Saratoga (1777)", "Paris (1783)"):
            self.assertIn(phrase, america)
        wars = deep._review_block(deep.topics()[13])
        for phrase in ("Pearl Harbor (1941)", "Midway", "Stalingrad"):
            self.assertIn(phrase, wars)
        end = deep._review_block(deep.topics()[20])
        for phrase in (
            "German reunification in 1990",
            "failed August 1991 coup",
            "December Soviet dissolution",
            "Gulf coalition",
            "Global South and Indian agency",
        ):
            self.assertIn(phrase, end)

    def test_contested_topics_are_qualified(self) -> None:
        imperialism = deep._review_block(deep.topics()[6])
        self.assertIn("did not draw every African border", imperialism)
        fascism = deep._review_block(deep.topics()[11])
        self.assertIn("without an overall electoral majority", fascism)
        cold_war = deep._review_block(deep.topics()[14])
        self.assertIn("did not erase non-alignment", cold_war)

    def test_topics_06_21_have_idempotent_canonical_controls(self) -> None:
        for number in range(6, 22):
            control = deep.CANONICAL_OWNER_CONTROLS[number]
            for heading in (
                "Owned core",
                "Boundary",
                "Date control",
                "Mechanism control",
                "Verified PYQ",
            ):
                self.assertIn(heading, control)
        self.assertIn("Topic 09 owns the pre-1914", deep.CANONICAL_OWNER_CONTROLS[6])
        self.assertIn("Topic 18 owns decolonisation", deep.CANONICAL_OWNER_CONTROLS[7])
        self.assertIn("Topic 19 owns twentieth-century", deep.CANONICAL_OWNER_CONTROLS[8])
        self.assertIn("Topic 10 owns the", deep.CANONICAL_OWNER_CONTROLS[9])
        self.assertIn("war's military course", deep.CANONICAL_OWNER_CONTROLS[9])
        self.assertIn("Topic 11 owns interwar", deep.CANONICAL_OWNER_CONTROLS[10])
        self.assertIn("Topic 12 owns fascist regimes", deep.CANONICAL_OWNER_CONTROLS[11])
        self.assertIn("Topic 20 owns the Depression", deep.CANONICAL_OWNER_CONTROLS[12])
        self.assertIn("Topic 15 owns", deep.CANONICAL_OWNER_CONTROLS[13])
        self.assertIn("Topic 16 owns the United Nations", deep.CANONICAL_OWNER_CONTROLS[14])
        self.assertIn("Topic 17 owns China's revolution", deep.CANONICAL_OWNER_CONTROLS[15])
        self.assertIn("Topic 18 owns mass", deep.CANONICAL_OWNER_CONTROLS[16])
        self.assertIn("Topic 21 owns the post-1991 order", deep.CANONICAL_OWNER_CONTROLS[17])
        self.assertIn("Modern Indian", deep.CANONICAL_OWNER_CONTROLS[18])
        self.assertIn("Topic 20 owns the thematic world", deep.CANONICAL_OWNER_CONTROLS[19])
        self.assertIn("Topic 21 owns the", deep.CANONICAL_OWNER_CONTROLS[20])
        self.assertIn("Topic 15 owns the whole Cold War", deep.CANONICAL_OWNER_CONTROLS[21])

    def test_review_lines_respect_ascii_width(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_stale_world_review_control_is_replaced(self) -> None:
        topic = deep.topics()[20]
        source = """# Topic

## BASIC LEARNING SESSION

### WORLD HISTORY DEEP-REVIEW CORE CONTROL

- **Must remember:** stale chronology
- **Close distinction:** stale mechanism
- **Evidence / interpretation limit:** stale verdict

## BASIC MCQS / REMEDIATION
"""
        repaired = deep.insert_contract(source, topic, {})
        self.assertIn(deep._review_block(topic).strip(), repaired)
        self.assertNotIn("stale chronology", repaired)
        self.assertEqual(
            1,
            repaired.count("### WORLD HISTORY DEEP-REVIEW CORE CONTROL"),
        )

    def test_topic21_deep_review_uses_current_authored_ascii_atlas(self) -> None:
        topic = deep.topics()[20]
        spec = deep.build_ascii_spec(
            topic,
            {},
            99,
            "# Topic\n",
            topic.canonical_path,
        )
        panels = spec["topics"][0]["panels"]
        self.assertEqual(
            [
                "Reform paradox",
                "Why the Cold War ended",
                "Eastern Europe, 1988-89",
                "Germany's negotiated reunification",
                "Soviet dissolution chain",
                "Gulf War order test",
                "Unipolarity's three tests",
                "Yugoslavia and NATO",
                "European integration settlement",
                "Globalisation and postcolonial agency",
                "India after the systemic rupture",
                "Cold War end answer spine",
            ],
            [panel["title"] for panel in panels],
        )
        joined = "\n".join(
            line for panel in panels for line in panel["ascii_lines"]
        )
        self.assertEqual(1, joined.count("MUST REMEMBER:"))
        self.assertEqual(1, joined.count("CLOSE DISTINCTION:"))
        self.assertEqual(1, joined.count("EVIDENCE LIMIT:"))

    def test_topic21_deep_review_uses_repaired_authoring_masters(self) -> None:
        topic = deep.topics()[20]
        main, workbook = deep.generation_sources(topic, {})
        self.assertTrue(deep.topic21_session_matches_authored(main, workbook))
        self.assertIn("German reunification", main)
        self.assertIn("Gulf War as order test", main)
        self.assertIn("Global South agency", main)
        self.assertNotIn(
            "### SESSION 15 — CORE SYNTHESIS — Arab Spring",
            main,
        )

    def test_long_output_paths_remain_windows_safe(self) -> None:
        for topic in deep.topics():
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_authored_q_heading_mcqs_are_rotated(self) -> None:
        source = """# Topic

## BASIC MCQS / REMEDIATION

### Q1. Which chronology is correct?
A. wrong
B. correct sequence
C. wronger
D. wrongest

**Answer: B.**

## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.enforce_strict_rotation(source)
        self.assertEqual(["A"], metrics["keys"])
        self.assertIn("A. correct sequence", repaired)

    def test_original_mains_gets_full_exam_contract(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Discuss the historical transformation. Answer in 250 words.
**Model thesis:** Change was substantial but uneven.
**Claim → named evidence → analysis → qualification:**
- Treaty evidence supports a bounded claim.
**Qualified conclusion:** Change and continuity coexisted.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(1, metrics["question_count"])
        self.assertIn("**Demand decoding:**", repaired)
        self.assertIn(
            "**Executable exam-length answer / compression plan:**",
            repaired,
        )
        self.assertIn("**Detailed examiner-grade model answer:**", repaired)
        self.assertIn("**Analytical body:**", repaired)
        self.assertIn("**How to improve this answer:**", repaired)

    def test_source_contract_requires_non_eurocentric_discipline(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        self.assertIn("Europe is never the default universal viewpoint", contract)
        self.assertIn("teleology", contract)
        self.assertIn("approved: false", contract)

    def test_porcelain_parser_preserves_unicode_spaces_and_renames(self) -> None:
        output = (
            " M notes/Final-Learning-Packages/World History/"
            "Subject-wide Syllabus/session — file.pdf\0"
            "R  notes/History/new — name.md\0"
            "notes/History/old name.md\0"
        ).encode("utf-8")
        current, removed = deep._parse_porcelain_v1_z(output)
        self.assertEqual(
            {
                "notes\\Final-Learning-Packages\\World History\\"
                "Subject-wide Syllabus\\session — file.pdf",
                "notes\\History\\new — name.md",
            },
            current,
        )
        self.assertEqual({"notes\\History\\old name.md"}, removed)

    def test_shared_validation_has_no_stale_exception_or_topic_count(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertNotIn("known_export_inventory_drift", source)
        self.assertNotIn('"topic_count": 259', source)
        self.assertIn('full_library_result["topic_count"]', source)


if __name__ == "__main__":
    unittest.main()
