"""Focused tests for the Essay-specific immutable deep-review driver."""

from __future__ import annotations

import inspect
import unittest
from pathlib import Path

import export_four_item_library as exporter
import markdown_learning_pdf
import regenerate_essay_deep_review as deep


class EssayDeepReviewTests(unittest.TestCase):
    def test_manifest_and_catalogue_keep_sixteen_topics_with_four_live_packages(self) -> None:
        scope = deep.authoritative_scope()
        self.assertEqual(16, scope["manifest_topic_count"])
        self.assertEqual(16, scope["catalogue_topic_count"])
        self.assertEqual(list(deep.TOPIC_KEYS), scope["review_topic_keys"])

    def test_purposes_follow_authoritative_owners(self) -> None:
        self.assertEqual(
            [
                "Paper Rules, Choice and Selection",
                "Philosophical Quote Decoding",
                "Issue-Based Prompt Scoping",
                "Brainstorming and Dimensional Expansion",
            ],
            [topic.title for topic in deep.topics()],
        )
        for topic in deep.topics():
            self.assertTrue(topic.basic.is_file())
            self.assertTrue(topic.advanced.is_file())

    def test_completed_untracked_essay_specific_generations_are_discovered(self) -> None:
        identities = {
            item["record_id"] for item in deep.additional_completed_identities()
        }
        self.assertTrue(
            {
                "essay-01:learner-v2:g3",
                "essay-02:learner-v2:g2",
                "essay-03:learner-v2:g2",
                "essay-04:learner-v2:g2",
            }.issubset(identities)
        )

    def test_generation_paths_preserve_essay_structure(self) -> None:
        paths = deep.generation_paths(deep.topics()[0], 99)
        self.assertIn(
            r"notes\Essay\Subject-Wide-Syllabus\essay-01\g99",
            str(paths["guide_pdf"]),
        )
        self.assertNotIn("learning-session-v2", str(paths["guide_pdf"]))
        self.assertTrue(paths["guide_pdf"].name.endswith("_Knowledge-Guide_2026-09-04.pdf"))
        self.assertTrue(paths["solutions_pdf"].name.endswith("_Practice-Solutions_2026-09-04.pdf"))

    def test_practice_spans_targeted_essay_skills_without_mcqs(self) -> None:
        combined = ""
        for topic in deep.topics():
            workbook, solutions = deep.practice_documents(topic)
            combined += workbook + solutions
            self.assertNotRegex(combined, r"(?m)^### Q\d+\.")
            self.assertIn("FULL ESSAY", workbook)
        for marker in (
            "Thesis correction",
            "Evidence selection",
            "Introduction",
            "Conclusion",
            "Paragraph repair",
            "Transition",
            "OUTLINES",
        ):
            self.assertIn(marker, combined)

    def test_full_models_are_exam_length_and_marks_guidance_is_explicit(self) -> None:
        for demand in deep.MODEL_EVIDENCE:
            model, count = deep.full_model_essay(demand)
            self.assertGreaterEqual(count, 950, demand)
            self.assertLessEqual(count, 1250, demand)
            self.assertIn("qualified", model.casefold())
        sample = deep.solution_block(
            1,
            "2024-A3",
            "There is no path to happiness, Happiness is the path.",
            "Exact V1 wording.",
        )
        self.assertIn("#### Why this earns marks", sample)
        self.assertIn("#### How to improve under exam conditions", sample)
        self.assertIn("#### Paragraph-level reasoning", sample)

    def test_ascii_and_graphical_grammar_is_essay_specific(self) -> None:
        flow = deep.ascii_workflow(deep.topics()[3])
        self.assertIn("DEMAND -> THESIS -> ARGUMENT JOBS", flow)
        self.assertIn("evidence", flow.casefold())
        self.assertIn("synthesis", flow.casefold())
        self.assertNotIn("TIMELINE OF EVENTS", flow)

    def test_allocation_rereads_live_trackers_and_starts_null(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation = source[source.index("def allocate("):source.index("def owner_body")]
        self.assertIn("load(STATUS)", allocation)
        self.assertIn("load(MASTER)", allocation)
        self.assertIn("load(REVIEW)", allocation)
        self.assertIn('"scores": pending_scores()', allocation)
        self.assertIn('"hard_gates": pending_gates()', allocation)
        self.assertIn('"approved": False', allocation)

    def test_exporter_has_an_explicit_essay_contract(self) -> None:
        self.assertEqual(
            {
                "01-Knowledge-Guide",
                "02-Practice-Workbook",
                "03-Practice-Solutions",
                "04-Integrated-Workflow-Atlas",
            },
            set(exporter.ESSAY_DELIVERABLES),
        )
        self.assertTrue(
            exporter.essay_specific_record(
                {"artifact_contract": exporter.ESSAY_CONTRACT}
            )
        )

    def test_driver_uses_direct_subprocess_tests_and_direct_nul_inventory(self) -> None:
        source = inspect.getsource(deep)
        self.assertIn(
            '[sys.executable, "-m", "unittest", "-v", module]',
            source,
        )
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn("payload.endswith(b\"\\0\")", source)
        self.assertNotIn("exec(compile(", source)
        self.assertNotIn("_prior_main", source)
        self.assertNotIn("def load_tests(", source)

    def test_table_break_hints_are_real_zero_width_spaces_not_literal_entities(self) -> None:
        source = Path(markdown_learning_pdf.__file__).read_text(encoding="utf-8")
        start = source.index("def parse_table(")
        parse_table = source[start:start + 3500]
        self.assertIn(r'"/\u200b"', parse_table)
        self.assertNotIn("/&#8203;", parse_table)


if __name__ == "__main__":
    unittest.main()
