"""Correctness tests for the Qualifying English semantic runtime."""

from __future__ import annotations

import json
import re
import unittest

import qualifying_english_semantic_runtime as runtime


class QualifyingEnglishSemanticRuntimeTests(unittest.TestCase):
    def test_catalogue_titles_and_order_are_authoritative(self) -> None:
        catalogue = runtime.load(runtime.CATALOGUE)
        rows = [row for row in catalogue["topics"] if row["topic_key"].startswith("qualifying-english-")]
        self.assertEqual([f"qualifying-english-{number:02d}" for number in range(1, 8)], [row["topic_key"] for row in rows])
        self.assertEqual([row["display_title"] for row in rows], [topic.title for topic in runtime.topics()])

    def test_every_topic_has_twelve_distinct_flow_stages(self) -> None:
        for topic in runtime.topics():
            self.assertEqual(12, len(topic.stages))
            self.assertEqual(12, len({title for title, _ in topic.stages}))

    def test_every_question_bank_has_valid_rotation_and_keys(self) -> None:
        for topic in runtime.topics():
            questions = runtime.questions_for(topic)
            self.assertEqual([], runtime.validate_questions(topic, questions), topic.key)
            self.assertEqual(48, len(questions))
            self.assertEqual(["ABCD"[index % 4] for index in range(48)], [q.answer for q in questions])

    def test_canonical_owners_contain_required_semantic_terms(self) -> None:
        for topic in runtime.topics():
            text = (
                topic.basic.read_text(encoding="utf-8")
                + "\n"
                + topic.ownership
                + "\n"
                + topic.verification
                + "\n"
                + topic.advanced
                + "\n"
                + "\n".join(title + " " + body for title, body in topic.stages)
            ).casefold()
            for term in topic.required_terms:
                self.assertIn(term.casefold(), text, f"{topic.key}: {term}")

    def test_official_paper_demands_are_locally_verifiable(self) -> None:
        rows = runtime.official_paper_audit()
        self.assertEqual(7, len(rows))
        self.assertTrue(all(not row["errors"] for row in rows))
        self.assertTrue(all(row["one_third_precis"] and row["no_title_precis"] for row in rows))

    def test_comprehension_and_precis_constraints_are_explicit(self) -> None:
        topic = runtime.topics()[5]
        text = (topic.basic.read_text(encoding="utf-8") + topic.advanced).casefold()
        for phrase in ("outside knowledge", "one-third", "do not add opinion", "do not give a title"):
            self.assertIn(phrase, text)

    def test_essay_models_obey_claimed_word_band(self) -> None:
        text = (runtime.KNOWLEDGE / "basic" / "07_Short-Essay-Writing.md").read_text(encoding="utf-8")
        counts = [int(value) for value in re.findall(r"\*\*Practice count:\*\* (\d+) words", text)]
        self.assertGreaterEqual(len(counts), 2)
        self.assertTrue(all(560 <= count <= 640 for count in counts))

    def test_semantic_queue_has_at_most_one_active_topic(self) -> None:
        state = json.loads(runtime.SEMANTIC.read_text(encoding="utf-8"))
        active = [
            row["topic_key"]
            for row in state["topics"]
            if row["status"] in {"in_progress", "changes_required", "repair_in_progress", "revalidation_pending"}
        ]
        self.assertLessEqual(len(active), 1)


if __name__ == "__main__":
    unittest.main()
