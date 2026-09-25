from __future__ import annotations

import unittest

from release_live_session import ROOT, matching_index_rows
from validate_live_session import (
    SOURCE_CATEGORIES,
    ValidationFailure,
    natural_variation,
    parse_source_manifest,
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


class SourceManifestTests(unittest.TestCase):
    def manifest(self, omit: str | None = None) -> str:
        rows = [
            f"| {category} | checked | exact path or documented evidence |"
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
