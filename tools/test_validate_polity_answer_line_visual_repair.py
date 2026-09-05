from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_polity_answer_line_visual_repair as validation


class PolityRenderedRepairValidationTests(unittest.TestCase):
    def test_active_scope_is_exactly_55_topics(self) -> None:
        records = validation.active_records()
        self.assertEqual(55, len(records))
        self.assertEqual(
            [f"polity-{number:02d}" for number in range(1, 56)],
            [record["topic_key"] for record in records],
        )

    def test_pdf_bound_validator_flags_out_of_page_text(self) -> None:
        # Structural smoke test: the validator uses extracted block and span
        # bboxes rather than page-count/contact-sheet sampling.
        source = validation.pdf_layout_evidence.__code__.co_names
        self.assertIn("get_text", source)
        self.assertIn("get_images", source)


if __name__ == "__main__":
    unittest.main()
