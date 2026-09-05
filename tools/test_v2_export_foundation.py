"""Focused regression tests for the learner-first v2 export foundation."""

from __future__ import annotations

import json
import shutil
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "upsc-ai-kit" / "tools"))

import build_study_index as study_index
import generate_export_command_index as export_index
import generate_learning_session_command_indexes as session_index
import markdown_learning_pdf
import validate_v2_export


VALID_MARKDOWN = """---
topic_key: geography-14
---
# Geography 14 Learning Session

## BASIC LEARNING SESSION

### Visual gateway

Basic explanation.

## BASIC MCQS / REMEDIATION

1. Basic check

## PYQS AND ANSWER PRACTICE

### Solved PYQ

Answer practice.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

Optional enrichment.

## CONSOLIDATED REGISTER NOTES

Final recall.
"""


class ExportIndexTests(unittest.TestCase):
    def test_variant_generations_do_not_collide(self) -> None:
        command = "Export PDF for Geography 14 — India Climatic Regions"
        data = {
            "exports": [
                {
                    "command": command,
                    "topic_key": "geography-14",
                    "variant": "legacy-v1",
                    "generation": 1,
                },
                {
                    "command": command,
                    "topic_key": "geography-14",
                    "variant": "learner-v2",
                    "generation": 1,
                },
                {
                    "command": command,
                    "topic_key": "geography-14",
                    "variant": "learner-v2",
                    "generation": 2,
                },
            ]
        }
        indexed = export_index.index_status_records(data)
        self.assertEqual(3, len(indexed))
        self.assertIn(("geography-14", "legacy-v1", 1), indexed)
        self.assertIn(("geography-14", "learner-v2", 1), indexed)
        self.assertIn(("geography-14", "learner-v2", 2), indexed)

    def test_v2_topic_slug_is_grouped_with_superseded_legacy_topic(self) -> None:
        statuses = export_index.index_status_records(
            {
                "exports": [
                    {
                        "record_id": "geography-28:legacy-v1:g1",
                        "topic_key": "geography-28",
                        "variant": "legacy-v1",
                        "generation": 1,
                    },
                    {
                        "record_id": (
                            "geography-28-human-settlements-and-urbanisation:"
                            "learner-v2:g2"
                        ),
                        "topic_key": (
                            "geography-28-human-settlements-and-urbanisation"
                        ),
                        "variant": "learner-v2",
                        "generation": 2,
                        "supersedes": "geography-28:legacy-v1:g1",
                    },
                ]
            }
        )
        records = export_index.records_for(
            "geography-28", statuses, export_index.V2_VARIANT
        )
        self.assertEqual([2], [generation for generation, _ in records])

    def test_schema_v1_records_have_a_backward_compatible_identity(self) -> None:
        data = {
            "exports": [
                {
                    "command": "Export PDF for Geography 14 — India Climatic Regions"
                }
            ]
        }
        indexed = export_index.index_status_records(data)
        self.assertEqual(
            [("geography-14", "legacy-v1", 1)],
            list(indexed),
        )

    def test_v1_approval_does_not_approve_v2(self) -> None:
        shared = {
            "main_pdf": "AGENTS.md",
            "workbook": "AGENTS.md",
            "markdown": "AGENTS.md",
        }
        statuses = export_index.index_status_records(
            {
                "exports": [
                    {
                        **shared,
                        "topic_key": "geography-14",
                        "variant": "legacy-v1",
                        "generation": 1,
                        "approved": True,
                    },
                    {
                        **shared,
                        "topic_key": "geography-14",
                        "variant": "learner-v2",
                        "generation": 1,
                        "approved": False,
                    },
                ]
            }
        )
        self.assertEqual(
            "generated",
            export_index.latest_state(
                "geography-14", statuses, export_index.V2_VARIANT
            ),
        )
        rendered = export_index.status_line(
            "Export PDF for Geography 14 — India Climatic Regions",
            "geography-14",
            statuses,
        )
        self.assertTrue(rendered.startswith("- [ ] 🟡"))
        self.assertIn("legacy/reference v1:** g1 ✅ approved", rendered)

    def test_numbered_owners_define_syllabus_topics(self) -> None:
        self.assertEqual(37, len(export_index.subject_topics("Geography")))
        self.assertEqual(8, len(export_index.subject_topics("CSAT")))

    def test_geography_learning_index_includes_stale_range_and_basic_owner(self) -> None:
        subject = ROOT / "upsc-ai-kit" / "knowledge" / "Geography"
        topics = session_index.ordered_subject_topics(subject)
        by_number = {number: (title, core) for number, title, core, _ in topics}
        self.assertEqual(37, len(topics))
        self.assertIn("15", by_number)
        self.assertEqual(
            "basic/14_Climate-Classification-Koppen.md",
            by_number["14"][1].relative_to(subject).as_posix(),
        )
        tracker = json.loads(
            (ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8")
        )
        records = [
            record
            for record in tracker["exports"]
            if record.get("topic_key")
            == "geography-28-human-settlements-and-urbanisation"
            and record.get("variant") == "learner-v2"
        ]
        latest = max(records, key=lambda record: int(record["generation"]))
        self.assertEqual(
            Path(latest["markdown"]).as_posix(),
            session_index.learning_session_for_number(
                subject, 28
            ).relative_to(ROOT).as_posix(),
        )

    def test_unnumbered_supplemental_owners_remain_indexed(self) -> None:
        subject = ROOT / "upsc-ai-kit" / "knowledge" / "Polity"
        topics = session_index.ordered_subject_topics(subject)
        self.assertEqual(55, len(topics))
        self.assertIn("55", {number for number, *_ in topics})

    def test_study_index_reads_number_from_v2_topic_slug(self) -> None:
        path = Path(
            "geography-32-industries-and-industrial-regions_"
            "Learning-Session.md"
        )
        self.assertEqual("32", study_index.topic_number(path))

    def test_philosophy_index_keeps_v1_and_v2_separate(self) -> None:
        subject = ROOT / "upsc-ai-kit" / "knowledge" / "Philosophy"
        rendered = session_index.render_philosophy(subject)
        carvaka_row = next(
            line for line in rendered.splitlines()
            if "Paper I — Indian Philosophy | 01" in line
        )
        self.assertIn("learner-v2 available", carvaka_row)
        self.assertIn("legacy-v1 retained", carvaka_row)

    def test_study_index_matches_carvaka_v1_and_v2_sessions(self) -> None:
        subject = ROOT / "upsc-ai-kit" / "knowledge" / "Philosophy"
        owner = subject / "paper-1" / "indian" / "Carvaka.md"
        sessions = study_index.matched_sessions(subject, owner)
        labels = {study_index.session_label(path) for path in sessions}
        self.assertIn("V2 session", labels)
        self.assertIn("Legacy/reference v1 session", labels)


class MarkdownV2Tests(unittest.TestCase):
    def test_sovereignty_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-ii-socio-political-philosophy-02"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_individual_and_state_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-ii-socio-political-philosophy-03"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_forms_of_government_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-ii-socio-political-philosophy-04"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_political_ideologies_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-ii-socio-political-philosophy-05"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_humanism_secularism_multiculturalism_uses_strict_abcd_policy(
        self,
    ) -> None:
        topic_key = "philosophy-paper-ii-socio-political-philosophy-06"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_crime_and_punishment_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-ii-socio-political-philosophy-07"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_quine_strawson_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-11"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_existentialism_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-10"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_husserl_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-09"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_later_wittgenstein_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-08"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_logical_positivism_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-07"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_moore_russell_early_wittgenstein_uses_strict_abcd_policy(
        self,
    ) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-06"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_hegel_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-05"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_kant_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-04"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_empiricism_uses_strict_abcd_policy(self) -> None:
        topic_key = "philosophy-paper-i-western-philosophy-03"
        self.assertIn(topic_key, validate_v2_export.STRICT_ABCD_TOPIC_KEYS)
        markdown = VALID_MARKDOWN.replace(
            "1. Basic check",
            "\n\n".join(
                [
                    f"### MCQ {index}\n\n**Correct answer: {answer}**"
                    for index, answer in enumerate("ABCDABCD", 1)
                ]
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.answer_key_pattern_errors(
                markdown,
                topic_key=topic_key,
            ),
        )

    def test_exact_v2_sequence_is_valid(self) -> None:
        self.assertEqual(
            [],
            validate_v2_export.validate_v2_markdown_text(VALID_MARKDOWN),
        )

    def test_legacy_progress_navigation_is_rejected_and_removable(self) -> None:
        invalid = VALID_MARKDOWN.replace(
            "Basic explanation.",
            (
                "Philosophy Optional | Progress: 1 / 7 | "
                "Philosophy Layered Session | "
                "Subtopic: Framework\n\nBasic explanation."
            ),
        )
        errors = validate_v2_export.validate_v2_markdown_text(invalid)
        self.assertTrue(any("Legacy Progress X/Y" in error for error in errors))
        cleaned = validate_v2_export.strip_legacy_progress_navigation(invalid)
        self.assertNotIn("Progress: 1 / 7", cleaned)
        self.assertIn("Basic explanation.", cleaned)
        self.assertEqual(
            [],
            validate_v2_export.validate_v2_markdown_text(cleaned),
        )

    def test_progress_example_inside_code_fence_is_preserved(self) -> None:
        fenced = VALID_MARKDOWN.replace(
            "Basic explanation.",
            "```text\nProgress: 1 / 7\n```\n\nBasic explanation.",
        )
        self.assertEqual(
            fenced,
            validate_v2_export.strip_legacy_progress_navigation(fenced),
        )
        self.assertEqual(
            [],
            validate_v2_export.validate_v2_markdown_text(fenced),
        )

    def test_register_notes_must_be_last(self) -> None:
        invalid = VALID_MARKDOWN + "\n## APPENDIX\n\nNot allowed after notes.\n"
        errors = validate_v2_export.validate_v2_markdown_text(invalid)
        self.assertTrue(any("Unexpected H2" in error for error in errors))

    def test_advanced_label_must_be_canonical(self) -> None:
        invalid = VALID_MARKDOWN.replace(
            validate_v2_export.ADVANCED_HEADING,
            "OPTIONAL ADVANCED MATERIAL",
        )
        errors = validate_v2_export.validate_v2_markdown_text(invalid)
        self.assertTrue(any("Missing canonical H2" in error for error in errors))

    def test_workbook_derives_from_both_practice_sections(self) -> None:
        workbook = markdown_learning_pdf.select_markdown(
            VALID_MARKDOWN,
            "workbook",
            validate_v2_export.V2_VARIANT,
        )
        self.assertIn("## BASIC MCQS / REMEDIATION", workbook)
        self.assertIn("## PYQS AND ANSWER PRACTICE", workbook)
        self.assertNotIn(validate_v2_export.ADVANCED_HEADING, workbook)
        self.assertNotIn("## CONSOLIDATED REGISTER NOTES", workbook)

    def test_canonical_v2_paths_are_accepted(self) -> None:
        source = (
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Geography"
            / "learning-sessions"
            / "v2"
            / "geography-14_Learning-Session.md"
        )
        output = (
            ROOT
            / "notes"
            / "Geography"
            / "learning-session-v2"
            / "geography-14"
            / "geography-14_Learning-Session_2026-08-20.pdf"
        )
        self.assertEqual(
            [],
            validate_v2_export.validate_v2_paths(
                ROOT, source, output, "geography-14", "main"
            ),
        )

    def test_section_wise_v2_paths_are_accepted(self) -> None:
        source = (
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Geography"
            / "learning-sessions"
            / "v2"
            / "human-economic-geography"
            / "geography-28_Learning-Session.md"
        )
        workbook_source = source.with_name("geography-28_Solved-Workbook.md")
        notes = (
            ROOT
            / "notes"
            / "Geography"
            / "learning-session-v2"
            / "human-economic-geography"
            / "notes"
            / "geography-28_Learning-Session_2026-08-20.pdf"
        )
        workbook = (
            ROOT
            / "notes"
            / "Geography"
            / "learning-session-v2"
            / "human-economic-geography"
            / "workbooks"
            / "geography-28_Solved-Workbook_2026-08-20.pdf"
        )
        self.assertEqual(
            [],
            validate_v2_export.validate_v2_paths(
                ROOT, source, notes, "geography-28", "main"
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.validate_v2_paths(
                ROOT, source, workbook, "geography-28", "workbook"
            ),
        )
        self.assertEqual(
            [],
            validate_v2_export.validate_v2_paths(
                ROOT, workbook_source, workbook, "geography-28", "workbook"
            ),
        )


class MarkdownRendererTests(unittest.TestCase):
    def test_answer_grabbing_callout_preserves_exact_dash_characters(self) -> None:
        rendered = markdown_learning_pdf.inline(
            "**ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM** "
            "The c. 600–321 BCE frame and corridor—from west to east—remain qualified."
        )
        self.assertIn("ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM", rendered)
        self.assertIn("600–321", rendered)
        self.assertIn("corridor—from west to east—remain", rendered)
        self.assertEqual("ordinary - text", markdown_learning_pdf.inline("ordinary — text"))

    def test_deep_markdown_headings_render_without_literal_hashes(self) -> None:
        story = markdown_learning_pdf.markdown_story(
            "##### Deep heading\n\nBody text.",
            ROOT,
        )
        rendered = [
            flowable.getPlainText()
            for flowable in story
            if hasattr(flowable, "getPlainText")
        ]
        self.assertIn("Deep heading", rendered)
        self.assertNotIn("##### Deep heading", rendered)

    def test_fenced_visual_reserves_space_before_rendering(self) -> None:
        story = markdown_learning_pdf.markdown_story(
            "```text\nONE\nTWO\nTHREE\n```",
            ROOT,
        )
        self.assertTrue(
            any(isinstance(flowable, markdown_learning_pdf.CondPageBreak) for flowable in story)
        )

    def test_heading_is_grouped_with_following_fenced_visual(self) -> None:
        story = markdown_learning_pdf.markdown_story(
            "### SESSION 3 - Translating public-service values\n\n"
            "#### Translating values into rules\n\n"
            "```text\nVALUE -> RULE\n```",
            ROOT,
        )
        grouped = [
            flowable
            for flowable in story
            if isinstance(flowable, markdown_learning_pdf.KeepTogether)
        ]
        self.assertEqual(1, len(grouped))
        self.assertEqual(
            [
                "SESSION 3 - Translating public-service values",
                "Translating values into rules",
            ],
            [
                flowable.getPlainText()
                for flowable in grouped[0]._content[:2]
            ],
        )

    def test_heading_is_grouped_with_following_table(self) -> None:
        story = markdown_learning_pdf.markdown_story(
            "#### Civil-service conduct rules\n\n"
            "##### CCS rule families\n\n"
            "| Rule family | Safe use |\n"
            "|---|---|\n"
            "| Rule 3 | General conduct |",
            ROOT,
            visual_audit_records=[],
        )
        grouped = [
            flowable
            for flowable in story
            if isinstance(flowable, markdown_learning_pdf.KeepTogether)
        ]
        self.assertEqual(1, len(grouped))
        self.assertEqual(
            ["Civil-service conduct rules", "CCS rule families"],
            [
                flowable.getPlainText()
                for flowable in grouped[0]._content[:2]
            ],
        )

    def test_basic_mcq_section_is_grouped_with_first_question_heading(self) -> None:
        story = markdown_learning_pdf.markdown_story(
            "## BASIC MCQS / REMEDIATION\n\n"
            "#### MCQ 1\n\n"
            "Question stem.",
            ROOT,
        )
        grouped = [
            flowable
            for flowable in story
            if isinstance(flowable, markdown_learning_pdf.KeepTogether)
        ]
        self.assertEqual(1, len(grouped))
        self.assertEqual(
            ["BASIC MCQS / REMEDIATION", "MCQ 1"],
            [flowable.getPlainText() for flowable in grouped[0]._content],
        )


class InternalPdfIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = ROOT / "_test_v2_internal_indexes"
        shutil.rmtree(cls.root, ignore_errors=True)
        cls.source = (
            cls.root
            / "upsc-ai-kit"
            / "knowledge"
            / "Test-Subject"
            / "learning-sessions"
            / "v2"
            / "test-section"
            / "test-topic_Learning-Session.md"
        )
        cls.main_pdf = (
            cls.root
            / "notes"
            / "Test-Subject"
            / "learning-session-v2"
            / "test-section"
            / "notes"
            / "test-topic_Learning-Session_2026-08-20.pdf"
        )
        cls.workbook_pdf = (
            cls.root
            / "notes"
            / "Test-Subject"
            / "learning-session-v2"
            / "test-section"
            / "workbooks"
            / "test-topic_Solved-Workbook_2026-08-20.pdf"
        )
        cls.legacy_pdf = cls.root / "legacy-v1-compatibility.pdf"
        cls.source.parent.mkdir(parents=True)
        cls.source.write_text(
            VALID_MARKDOWN.replace(
                "# Geography 14 Learning Session",
                "# Cārvāka and Pratyakṣa Learning Session",
            ).replace(
                "### Visual gateway",
                "### Pratyakṣa as the meaningful subtopic\n\n"
                "### Model solution",
            ),
            encoding="utf-8",
        )
        markdown_learning_pdf.build_pdf(
            cls.source,
            cls.main_pdf,
            variant=validate_v2_export.V2_VARIANT,
            topic_key="test-topic",
            repository_root=cls.root,
        )
        cls.first_main_bytes = cls.main_pdf.read_bytes()
        markdown_learning_pdf.build_pdf(
            cls.source,
            cls.main_pdf,
            variant=validate_v2_export.V2_VARIANT,
            topic_key="test-topic",
            repository_root=cls.root,
        )
        cls.second_main_bytes = cls.main_pdf.read_bytes()
        markdown_learning_pdf.build_pdf(
            cls.source,
            cls.workbook_pdf,
            mode="workbook",
            variant=validate_v2_export.V2_VARIANT,
            topic_key="test-topic",
            repository_root=cls.root,
        )
        markdown_learning_pdf.build_pdf(
            cls.source,
            cls.legacy_pdf,
            variant=markdown_learning_pdf.LEGACY_VARIANT,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(cls.root, ignore_errors=True)

    def test_main_and_workbook_have_separate_early_internal_indexes(self) -> None:
        main = validate_v2_export.inspect_pdf_index(self.main_pdf)
        workbook = validate_v2_export.inspect_pdf_index(self.workbook_pdf)
        self.assertEqual(2, main.index_page)
        self.assertEqual(2, workbook.index_page)
        self.assertIn("CONTENTS / SESSION INDEX", main.index_text)
        self.assertIn("CONTENTS / WORKBOOK INDEX", workbook.index_text)
        self.assertNotIn(
            validate_v2_export.ADVANCED_HEADING,
            workbook.index_text,
        )
        self.assertNotIn("CONSOLIDATED REGISTER NOTES", workbook.index_text)

    def test_index_page_numbers_are_accurate_and_within_range(self) -> None:
        for path, mode in (
            (self.main_pdf, "main"),
            (self.workbook_pdf, "workbook"),
        ):
            self.assertEqual(
                [],
                validate_v2_export.validate_pdf(
                    path,
                    variant=validate_v2_export.V2_VARIANT,
                    mode=mode,
                ),
            )
            info = validate_v2_export.inspect_pdf_index(path)
            for entry in info.entries:
                self.assertGreaterEqual(entry.page, 1)
                self.assertLessEqual(entry.page, info.page_count)
                self.assertIn(
                    validate_v2_export.normalize_pdf_text(entry.title),
                    validate_v2_export.normalize_pdf_text(
                        info.page_texts[entry.page - 1]
                    ),
                )

    def test_rendering_is_deterministic(self) -> None:
        self.assertEqual(self.first_main_bytes, self.second_main_bytes)

    def test_unicode_heading_is_indexed_and_utility_heading_is_not(self) -> None:
        info = validate_v2_export.inspect_pdf_index(self.main_pdf)
        titles = [entry.title for entry in info.entries]
        self.assertTrue(all("\ufffd" not in title for title in titles))
        self.assertIn("Cārvāka and Pratyakṣa Learning Session", titles)
        self.assertIn("Pratyakṣa as the meaningful subtopic", titles)
        self.assertNotIn("Model solution", titles)
        self.assertIn("Cārvāka", info.index_text)
        self.assertIn("Pratyakṣa", info.index_text)

    def test_register_notes_are_the_last_major_main_section(self) -> None:
        info = validate_v2_export.inspect_pdf_index(self.main_pdf)
        major_sections = [
            entry.title
            for entry in info.entries
            if entry.level == 2
        ]
        self.assertEqual(
            [
                validate_v2_export.normalize_pdf_text(spec.canonical)
                for spec in validate_v2_export.SECTION_SPECS
            ],
            [
                validate_v2_export.normalize_pdf_text(title)
                for title in major_sections
            ],
        )
        self.assertEqual("CONSOLIDATED REGISTER NOTES", major_sections[-1])

    def test_legacy_rendering_remains_unindexed_and_valid(self) -> None:
        self.assertEqual([], validate_v2_export.validate_pdf(self.legacy_pdf))
        info = validate_v2_export.inspect_pdf_index(self.legacy_pdf)
        self.assertIsNone(info.index_page)
        self.assertEqual((), info.entries)

    def test_outline_levels_are_clamped_when_h3_precedes_first_h2(self) -> None:
        source = self.source.parent / "outline-level-jump_Learning-Session.md"
        output = (
            self.main_pdf.parent
            / "outline-level-jump_Learning-Session_2026-08-20.pdf"
        )
        source.write_text(
            VALID_MARKDOWN.replace(
                "## BASIC LEARNING SESSION",
                "### Coverage lock\n\nFront-matter check.\n\n"
                "## BASIC LEARNING SESSION",
            ),
            encoding="utf-8",
        )
        markdown_learning_pdf.build_pdf(
            source,
            output,
            variant=validate_v2_export.V2_VARIANT,
            topic_key="outline-level-jump",
            repository_root=self.root,
        )
        info = validate_v2_export.inspect_pdf_index(output)
        coverage = next(
            entry for entry in info.entries if entry.title == "Coverage lock"
        )
        self.assertEqual(2, coverage.level)
        self.assertEqual(
            [],
            validate_v2_export.validate_pdf(
                output,
                variant=validate_v2_export.V2_VARIANT,
                mode="main",
            ),
        )


class TrackerMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(
            (ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8")
        )

    def test_tracker_is_schema_v2_without_record_loss(self) -> None:
        self.assertEqual(2, self.data["schema_version"])
        legacy = [
            entry
            for entry in self.data["exports"]
            if entry["variant"] == "legacy-v1" and entry["generation"] == 1
        ]
        self.assertGreaterEqual(len(legacy), 190)
        identities = {
            (
                entry["topic_key"],
                entry["variant"],
                entry["generation"],
            )
            for entry in self.data["exports"]
        }
        self.assertEqual(len(self.data["exports"]), len(identities))

    def test_legacy_approvals_and_provenance_are_preserved(self) -> None:
        legacy = [
            entry for entry in self.data["exports"]
            if entry["variant"] == "legacy-v1"
        ]
        approved = [entry for entry in legacy if entry["approved"]]
        self.assertEqual(1, len(approved))
        self.assertIn("Modern History 03", approved[0]["command"])
        required = {
            "source_basic",
            "source_advanced",
            "assembled_markdown",
            "renderer",
            "generation_date",
            "superseded_v1",
        }
        for entry in legacy:
            self.assertEqual("legacy-v1", entry["variant"])
            self.assertEqual(1, entry["generation"])
            self.assertEqual(
                entry["approved"],
                entry["approval"]["approved"],
            )
            self.assertTrue(required.issubset(entry["provenance"]))

    def test_carvaka_generation_two_is_unapproved_and_supersedes_v1(self) -> None:
        record = next(
            entry
            for entry in self.data["exports"]
            if entry.get("record_id")
            == "philosophy-paper-i-indian-philosophy-01:learner-v2:g2"
        )
        self.assertFalse(record["approved"])
        self.assertFalse(record["approval"]["approved"])
        self.assertEqual(
            "philosophy-paper-i-indian-philosophy-01:legacy-v1:g1",
            record["supersedes"],
        )


if __name__ == "__main__":
    unittest.main()
