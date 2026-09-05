"""Targeted tests for the adapter-driven Socio-Political learner-v2 generator."""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_philosophy_socio_political_topic_v2 as generator
from validate_v2_export import (
    answer_key_pattern_errors,
    extract_mcq_answer_keys,
    legacy_progress_navigation_lines,
    mcq_answer_text_errors,
    validate_v2_markdown_text,
)


CASTE_SPEC = "philosophy_socio_political_caste_gandhi_ambedkar_v2_spec"
DEVELOPMENT_SPEC = (
    "philosophy_socio_political_development_and_social_progress_v2_spec"
)


class TopicAdapterTests(unittest.TestCase):
    def test_adapter_loading_supports_retained_and_fallback_topics(self) -> None:
        development = generator.load_topic_adapter(DEVELOPMENT_SPEC)
        caste = generator.load_topic_adapter(CASTE_SPEC)

        self.assertEqual(8, development.number)
        self.assertTrue(development.uses_retained_package)
        self.assertEqual(10, caste.number)
        self.assertFalse(caste.uses_retained_package)
        self.assertEqual(10, len(caste.session_specs))
        self.assertEqual(12, len(caste.ascii_panels))
        self.assertEqual(set(range(1, 11)), set(caste.owner_session_ranges))

    def test_latest_identity_starts_unpublished_topics_at_learner_g2(self) -> None:
        tracker = {"schema_version": 2, "exports": []}
        generation, supersedes, legacy_id = generator.latest_identity(
            tracker,
            "philosophy-paper-ii-socio-political-philosophy-09",
        )
        self.assertEqual(2, generation)
        self.assertEqual(
            "philosophy-paper-ii-socio-political-philosophy-09:legacy-v1:g1",
            supersedes,
        )
        self.assertIsNone(legacy_id)

    def test_retained_workbook_pyq_heading_stops_before_original_mains(self) -> None:
        workbook = """\
### SOLVED PYQ BANK - EXACTLY 2 VERIFIED OWNER QUESTIONS

**Question:** First verified question?

**Question:** Second verified question?

### ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS

**Question:** Original practice question?
"""
        self.assertEqual(
            ["First verified question?", "Second verified question?"],
            generator._workbook_pyqs(workbook),
        )


class CanonicalFallbackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.adapter = generator.load_topic_adapter(CASTE_SPEC)
        cls.owner = generator.repo_path(cls.adapter.canonical_owner).read_text(
            encoding="utf-8"
        )
        dossier = generator.repo_path(cls.adapter.advanced_dossier).read_text(
            encoding="utf-8"
        )
        ledger = generator.repo_path(cls.adapter.pyq_ledger).read_text(
            encoding="utf-8"
        )
        cls.source_pyqs = generator.owner_pyqs(cls.adapter, ledger)
        cls.markdown = generator.assemble_canonical_fallback(
            cls.adapter,
            cls.owner,
            dossier,
            ledger,
        )

    def test_fallback_has_five_sections_and_complete_core_structure(self) -> None:
        self.assertEqual(
            [
                "BASIC LEARNING SESSION",
                "BASIC MCQS / REMEDIATION",
                "PYQS AND ANSWER PRACTICE",
                "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                "CONSOLIDATED REGISTER NOTES",
            ],
            re.findall(r"(?m)^##\s+(.+?)\s*$", self.markdown),
        )
        self.assertEqual(
            10,
            len(re.findall(r"(?m)^###\s+SESSION\s+\d+\s+—", self.markdown)),
        )
        self.assertFalse(validate_v2_markdown_text(self.markdown))
        self.assertFalse(
            generator._owner_coverage_errors(self.owner, self.markdown)
        )

    def test_fallback_practice_counts_rotation_and_answer_text_agree(self) -> None:
        keys = extract_mcq_answer_keys(self.markdown)
        self.assertEqual(48, len(keys))
        self.assertEqual(list("ABCD" * 12), keys)
        self.assertFalse(
            answer_key_pattern_errors(
                self.markdown,
                topic_key=self.adapter.topic_key,
            )
        )
        self.assertFalse(mcq_answer_text_errors(self.markdown))
        self.assertEqual(
            len(self.source_pyqs),
            len(
                re.findall(
                    r"(?m)^####\s+PYQ\s+\d+\s+—",
                    self.markdown,
                )
            ),
        )
        self.assertEqual(
            {10, 15, 20},
            {int(item["marks"]) for item in self.adapter.original_mains},
        )

    def test_fallback_contains_no_forbidden_progress_navigation(self) -> None:
        self.assertFalse(legacy_progress_navigation_lines(self.markdown))
        self.assertNotRegex(
            self.markdown,
            r"(?im)^\s*Progress:\s*\d+\s*/\s*\d+",
        )


if __name__ == "__main__":
    unittest.main()
