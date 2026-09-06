"""Correctness tests for the Qualifying Hindi semantic runtime."""

from __future__ import annotations

import json
import re
import unittest

import qualifying_hindi_semantic_runtime as runtime


class QualifyingHindiSemanticRuntimeTests(unittest.TestCase):
    def test_catalogue_titles_and_order_are_authoritative(self) -> None:
        catalogue = runtime.load(runtime.CATALOGUE)
        rows = [row for row in catalogue["topics"] if row["topic_key"].startswith("qualifying-hindi-")]
        self.assertEqual([f"qualifying-hindi-{number:02d}" for number in range(1, 7)], [row["topic_key"] for row in rows])
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

    def test_canonical_owners_and_closures_cover_required_terms(self) -> None:
        for topic in runtime.topics():
            text = (
                topic.basic.read_text(encoding="utf-8")
                + "\n"
                + runtime.CANONICAL_ADDITIONS[topic.number]
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

    def test_complete_catalogue_specific_grammar_coverage(self) -> None:
        text = (
            runtime.topics()[1].basic.read_text(encoding="utf-8")
            + runtime.CANONICAL_ADDITIONS[2]
        )
        for term in ("संधि", "समास", "उपसर्ग", "प्रत्यय", "लिंग", "वचन", "कारक", "काल", "वाच्य", "वाक्य-रचना", "वर्तनी", "विराम", "वाक्य-शुद्धि"):
            self.assertIn(term, text)

    def test_official_paper_demands_are_locally_verifiable(self) -> None:
        rows = runtime.official_paper_audit()
        self.assertEqual(7, len(rows))
        self.assertTrue(all(not row["errors"] for row in rows))
        precise = [row for row in rows if row["year"] in {"2022", "2023"}]
        self.assertTrue(all(row["one_third_precis"] and row["no_title_precis"] for row in precise))
        self.assertTrue(all(not row["one_third_precis"] for row in rows if row["year"] not in {"2022", "2023"}))

    def test_comprehension_precis_translation_and_essay_constraints_are_explicit(self) -> None:
        combined = "\n".join(
            topic.basic.read_text(encoding="utf-8") + "\n" + runtime.CANONICAL_ADDITIONS[topic.number] + "\n" + topic.advanced
            for topic in runtime.topics()[3:]
        ).casefold()
        for phrase in ("पाठ-आधार", "एक-तिहाई", "शीर्षक", "qualified thesis", "back-check", "actor"):
            self.assertIn(phrase.casefold(), combined)

    def test_hindi_unicode_is_clean_and_normalized(self) -> None:
        for topic in runtime.topics():
            text = topic.basic.read_text(encoding="utf-8")
            self.assertNotIn("\ufffd", text)
            self.assertIsNone(re.search(r"[\u200b\ufeff]", text))
            self.assertRegex(text, r"[\u0900-\u097f]")

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
