"""Targeted correctness tests for the CSAT semantic runtime."""

from __future__ import annotations

import json
import itertools
import math
import unittest

import csat_semantic_runtime as runtime


class CsatSemanticRuntimeTests(unittest.TestCase):
    def test_catalogue_titles_and_order_are_authoritative(self) -> None:
        catalogue = runtime.load(runtime.CATALOGUE)
        expected = [row for row in catalogue["topics"] if row["topic_key"].startswith("csat-")]
        self.assertEqual([f"csat-{n:02d}" for n in range(1, 9)], [row["topic_key"] for row in expected])
        self.assertEqual([row["display_title"] for row in expected], [topic.title for topic in runtime.topics()])

    def test_every_topic_has_twelve_distinct_flow_stages(self) -> None:
        for topic in runtime.topics():
            self.assertEqual(12, len(topic.stages))
            self.assertEqual(12, len({title for title, _ in topic.stages}))

    def test_every_question_bank_recomputes_and_rotates(self) -> None:
        for topic in runtime.topics():
            questions = runtime.questions_for(topic)
            self.assertEqual([], runtime.validate_questions(topic, questions), topic.key)
            self.assertEqual(48, len(questions))
            self.assertEqual(["ABCD"[i % 4] for i in range(48)], [q.answer for q in questions])

    def test_reading_answers_have_passage_support(self) -> None:
        for question in runtime.reading_questions():
            self.assertIn(
                question.support.casefold(),
                question.stem.split("\n\n", 1)[0].casefold(),
            )
            self.assertNotIn("according to outside knowledge", question.explanation.casefold())

    def test_semantic_queue_has_at_most_one_active_topic(self) -> None:
        state = json.loads(runtime.SEMANTIC.read_text(encoding="utf-8"))
        active = [
            row["topic_key"] for row in state["topics"]
            if row["status"] in {"in_progress", "changes_required", "repair_in_progress", "revalidation_pending"}
        ]
        self.assertLessEqual(len(active), 1)

    def test_number_and_counting_helpers_match_brute_force(self) -> None:
        for value in range(1, 201):
            brute_divisors = sum(value % candidate == 0 for candidate in range(1, value + 1))
            self.assertEqual(brute_divisors, runtime.divisor_count(value))
        factorial = 1
        for value in range(1, 101):
            factorial *= value
            brute_zeros = len(str(factorial)) - len(str(factorial).rstrip("0"))
            self.assertEqual(brute_zeros, runtime.trailing_zeros(value))
        for n in range(2, 8):
            for r in range(0, n + 1):
                brute = len(list(itertools.permutations(range(n), r)))
                self.assertEqual(brute, math.perm(n, r))

    def test_canonical_owners_contain_required_semantic_terms(self) -> None:
        for topic in runtime.topics():
            text = (
                topic.basic.read_text(encoding="utf-8")
                + "\n"
                + topic.advanced.read_text(encoding="utf-8")
            ).casefold()
            for term in topic.required_terms:
                self.assertIn(term.casefold(), text, f"{topic.key}: {term}")


if __name__ == "__main__":
    unittest.main()
