from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import notions_style_ascii_master
import philosophy_indian_religion_deep_quality_repair as repair
import philosophy_indian_religion_reviewed_content as reviewed
import repair_philosophy_religion_mcq_rotation as rotation
import validate_philosophy_indian_religion_deep_quality_repair as validation


class ReviewedContentTests(unittest.TestCase):
    def test_exact_scope_and_session_count(self) -> None:
        self.assertEqual(set(reviewed.SESSION_REVIEWS), set(repair.TOPIC_KEYS))
        self.assertEqual(sum(map(len, reviewed.SESSION_REVIEWS.values())), 134)

    def test_keyword_and_usage_quality(self) -> None:
        for topic_key, sessions in reviewed.SESSION_REVIEWS.items():
            for number, item in enumerate(sessions, 1):
                self.assertEqual(
                    repair.keyword_errors(list(item["keywords"])),
                    [],
                    f"{topic_key} session {number}",
                )
                usage = str(item["how_to_use"])
                self.assertGreaterEqual(len(usage.split()), 14)
                self.assertRegex(usage, repair.USAGE_ACTION_RE)

    def test_reviewed_answer_lines_are_complete(self) -> None:
        for topic_key, sessions in reviewed.SESSION_REVIEWS.items():
            for number, item in enumerate(sessions, 1):
                if "answer_line" not in item:
                    continue
                self.assertEqual(
                    repair.answer_line_errors(str(item["answer_line"])),
                    [],
                    f"{topic_key} session {number}",
                )
        for topic_key, stages in reviewed.GRAPHICAL_ANSWER_OVERRIDES.items():
            for stage, line in stages.items():
                self.assertEqual(
                    repair.answer_line_errors(line, minimum=12, maximum=42),
                    [],
                    f"{topic_key} graphical stage {stage}",
                )

    def test_ascii_specs_are_bounded_and_topic_specific(self) -> None:
        selected = {}
        for path in (repair.INDIAN_ASCII_SPEC, repair.RELIGION_ASCII_SPEC):
            selected.update(
                notions_style_ascii_master.normalize_manual_spec_file(path)
            )
        for topic_key in repair.TOPIC_KEYS:
            spec = selected[topic_key]
            self.assertGreaterEqual(len(spec.panels), 8)
            for panel in spec.panels:
                self.assertTrue(panel.structural_type)
                self.assertTrue(panel.source_references)
                for line in panel.body.splitlines():
                    self.assertLessEqual(
                        len(line),
                        notions_style_ascii_master.MAX_LINE_WIDTH,
                    )


class RotationTests(unittest.TestCase):
    def test_rotation_preserves_option_propositions(self) -> None:
        block = """**1. Which claim is correct?**

A. First false claim
B. Correct qualified claim
C. Second false claim
D. Third false claim

**Answer: B.**

B is correct; A, C and D fail for different reasons.
"""
        rotated, audit = rotation.rotate_block(block, "D")
        self.assertEqual(audit["before_answer"], "B")
        self.assertEqual(audit["after_answer"], "D")
        self.assertIn("D. Correct qualified claim", rotated)
        self.assertIn("**Answer: D.**", rotated)
        self.assertEqual(
            audit["option_content_sha256"],
            rotation.option_content_hash(rotated),
        )

    def test_every_topic_has_curated_core_fixtures(self) -> None:
        self.assertEqual(set(validation.CORE_FIXTURES), set(repair.TOPIC_KEYS))
        for topic_key, fixtures in validation.CORE_FIXTURES.items():
            self.assertGreaterEqual(len(fixtures), 6, topic_key)
            for label, phrases in fixtures:
                self.assertTrue(label)
                self.assertTrue(phrases)


if __name__ == "__main__":
    unittest.main()
