from __future__ import annotations

import unittest

from release_live_session import ROOT, matching_index_rows
from validate_live_session import (
    EXCLUDED_SOURCE_CATEGORIES,
    SOURCE_CATEGORIES,
    ValidationFailure,
    natural_variation,
    parse_mcq_labels,
    parse_source_manifest,
    validate_concept_check_chunk,
)


class NaturalVariationTests(unittest.TestCase):
    def test_accepts_concept_sensitive_pattern(self) -> None:
        self.assertTrue(natural_variation([2, 4, 3, 2, 4, 3, 4, 2, 3, 4, 3]))

    def test_rejects_constant_pattern(self) -> None:
        self.assertFalse(natural_variation([3, 3, 3, 3]))

    def test_rejects_alternating_pattern(self) -> None:
        self.assertFalse(natural_variation([2, 4, 2, 4, 2, 4]))

    def test_rejects_short_repeating_pattern(self) -> None:
        self.assertFalse(natural_variation([2, 3, 4, 2, 3, 4]))

    def test_rejects_out_of_range_counts(self) -> None:
        self.assertFalse(natural_variation([2, 3, 5]))


class McqLabelTests(unittest.TestCase):
    def test_accepts_answer_separated_format(self) -> None:
        raw = "\n".join(
            [
                "**MCQ 1**",
                "**Question:** Example?",
                "",
                "**MCQ 1 — Answer and explanation**",
                "**Correct answer: A**",
            ]
        )
        labels, _ = parse_mcq_labels(raw, allow_legacy=False)
        self.assertEqual(labels, [("1", "A")])

    def test_rejects_answer_bearing_question_heading(self) -> None:
        with self.assertRaises(ValidationFailure):
            parse_mcq_labels("**MCQ 1: A**\n", allow_legacy=False)

    def test_allows_legacy_heading_only_for_legacy_audit(self) -> None:
        labels, _ = parse_mcq_labels("**MCQ 1: A**\n", allow_legacy=True)
        self.assertEqual(labels, [("1", "A")])

    def test_rejects_missing_answer_block(self) -> None:
        with self.assertRaises(ValidationFailure):
            parse_mcq_labels("**MCQ 1**\n", allow_legacy=False)


class ConceptCheckTests(unittest.TestCase):
    def test_accepts_complete_concept_check(self) -> None:
        chunk = "\n".join(
            [
                "### Concept check",
                "",
                "**Question:** Why does the mechanism matter?",
                "",
                "**Model answer:** It connects the cause to the observed outcome.",
                "",
                "**Misconception to avoid:** Correlation alone does not prove causation.",
            ]
        )
        self.assertEqual(validate_concept_check_chunk(chunk, 1), 1)

    def test_rejects_missing_misconception_note(self) -> None:
        chunk = "\n".join(
            [
                "### Concept check",
                "**Question:** Why?",
                "**Model answer:** Because the mechanism links cause and outcome.",
            ]
        )
        with self.assertRaises(ValidationFailure):
            validate_concept_check_chunk(chunk, 1)


class SourceManifestTests(unittest.TestCase):
    def manifest(
        self,
        omit: str | None = None,
        status_overrides: dict[str, str] | None = None,
    ) -> str:
        status_overrides = status_overrides or {}
        rows = [
            (
                f"| {category} | "
                f"{status_overrides.get(category, 'not relevant' if category in EXCLUDED_SOURCE_CATEGORIES else 'checked')} "
                "| exact path or documented evidence |"
            )
            for category in SOURCE_CATEGORIES
            if category != omit
        ]
        return "\n".join(
            [
                "## SOURCE-MANIFEST GATE",
                "",
                "| Category | Status | Evidence or reason |",
                "|---|---|---|",
                *rows,
                "",
            ]
        )

    def test_accepts_complete_manifest(self) -> None:
        result = parse_source_manifest(self.manifest(), allow_missing=False)
        self.assertEqual(set(result), set(SOURCE_CATEGORIES))

    def test_rejects_missing_category(self) -> None:
        with self.assertRaises(ValidationFailure):
            parse_source_manifest(
                self.manifest(omit="official live sources"),
                allow_missing=False,
            )

    def test_rejects_checked_excluded_category(self) -> None:
        with self.assertRaises(ValidationFailure):
            parse_source_manifest(
                self.manifest(status_overrides={"final learner package": "checked"}),
                allow_missing=False,
            )

    def test_rejects_available_excluded_workbook(self) -> None:
        with self.assertRaises(ValidationFailure):
            parse_source_manifest(
                self.manifest(status_overrides={"solved workbook": "not available"}),
                allow_missing=False,
            )

    def test_legacy_flag_allows_absent_manifest(self) -> None:
        self.assertEqual(
            parse_source_manifest("# SOURCE LEDGER\n", allow_missing=True),
            {},
        )


class IndexRowTests(unittest.TestCase):
    def test_accepts_index_relative_topic_link(self) -> None:
        index = ROOT / "live_sessions" / "INDEX.md"
        topic = ROOT / "live_sessions" / "Subject" / "Topic" / "Session.md"
        raw = (
            "| Subject | Topic | 1 | 100 | `abcdef123456` | "
            "[file](Subject/Topic/Session.md) |\n"
        )
        self.assertEqual(len(matching_index_rows(raw, topic, index)), 1)

    def test_accepts_repository_relative_topic_link(self) -> None:
        index = ROOT / "live_sessions" / "INDEX.md"
        topic = ROOT / "live_sessions" / "Subject" / "Topic" / "Session.md"
        raw = (
            "| Subject | Topic | 1 | 100 | `abcdef123456` | "
            "[file](live_sessions/Subject/Topic/Session.md) |\n"
        )
        self.assertEqual(len(matching_index_rows(raw, topic, index)), 1)


if __name__ == "__main__":
    unittest.main()
