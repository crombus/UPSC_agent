"""Focused tests for the Essay semantic-completeness workflow."""

from __future__ import annotations

import re
import unittest

import essay_semantic_data as data


class EssaySemanticTests(unittest.TestCase):
    def test_catalogue_has_exact_sixteen_topics_in_order(self) -> None:
        self.assertEqual(list(range(1, 17)), list(data.TOPICS))
        self.assertEqual("Paper Rules, Choice and Selection", data.TOPICS[1][0])
        self.assertEqual("Practice Loops, PYQ Lab and Revision System", data.TOPICS[16][0])

    def test_every_topic_has_distinct_ownership_control(self) -> None:
        self.assertEqual(set(data.TOPICS), set(data.CONTROLS))
        for purpose, terms, boundary in data.CONTROLS.values():
            self.assertGreaterEqual(len(purpose), 20)
            self.assertGreaterEqual(len(terms.split("|")), 4)
            self.assertGreaterEqual(len(boundary), 20)

    def test_every_topic_has_one_complete_exam_length_model(self) -> None:
        for number in data.TOPICS:
            model = data._model_essay(
                data.MODEL_PROMPTS[number], data.CONTROLS[number][1]
            )
            self.assertGreaterEqual(model["word_count"], 950)
            self.assertLessEqual(model["word_count"], 1250)
            self.assertIn("strongest objection", model["essay"].casefold())
            self.assertIn("synthesis", model["essay"].casefold())

    def test_v1_v2_prompt_status_is_explicit(self) -> None:
        for number, prompt in data.MODEL_PROMPTS.items():
            model = data._model_essay(prompt, data.CONTROLS[number][1])
            year = int(data.PROMPT_LABELS[prompt][:4])
            self.assertIn("V1" if year >= 2018 else "V2", model["verification"])

    def test_configs_have_required_practice_and_flow_shape(self) -> None:
        for number in data.TOPICS:
            config = data.build_topic(number)
            self.assertEqual(20, len(config["facts"]))
            self.assertEqual(15, len(config["session_plans"]))
            self.assertEqual(12, len(config["panels"]))
            self.assertEqual(3, len(config["pyq_solutions"]))
            self.assertEqual([10, 10, 15, 15, 20, 20], [row[0] for row in config["mains"]])

    def test_model_prompts_are_in_repository_pyq_corpus(self) -> None:
        corpus = (data.KNOWLEDGE / "PYQ-Corpus-2013-2025.md").read_text(encoding="utf-8")
        for prompt in data.MODEL_PROMPTS.values():
            self.assertIn(prompt, corpus)

    def test_live_attempts_are_dated_and_official(self) -> None:
        for attempt in data.LIVE_ATTEMPTS:
            self.assertIn(data.DATE, attempt)
            self.assertIn("upsc.gov.in", attempt)
            self.assertRegex(attempt, r"\b(?:attempted|searched)\b")

    def test_five_h2_contract_remains_in_common_assembler(self) -> None:
        import inspect
        import generate_essay_common as common

        source = inspect.getsource(common._assemble)
        for heading in (
            "BASIC LEARNING SESSION",
            "BASIC MCQS / REMEDIATION",
            "PYQS AND ANSWER PRACTICE",
            "OPTIONAL ADVANCED DEPTH",
            "CONSOLIDATED REGISTER NOTES",
        ):
            self.assertIn(heading, source)


if __name__ == "__main__":
    unittest.main()
