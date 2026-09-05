from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import polity_answer_line_visual_repair as repair


class PolityAnswerLineVisualRepairTests(unittest.TestCase):
    BAD_REGRESSION_FIXTURES = (
        "Cross-link and A system-level characteristic produced by several rules organise What counts as a salient constitutional feature to advance constitutional governance.",
        "The 1861 Act widened participation; institutionally, this supports democratic constitutionalism, while its institutional inheritance acquires legitimacy only through popular sovereignty, constitutional limits and democratic accountability.",
        "Adopted: 26 Nov 1949 Signed: 24 Jan 1950 Commenced: 26 Jan 1950 Article 395: repeals; institutionally, this supports democratic constitutionalism.",
        "colonial statutes built a centralised state while the Constitution located sovereignty in the people.",
        "Mention Kihoto Hollohan.",
        "Part IX master map.",
        "It is the duty of the State to apply them in making laws.",
        "Verdict: The institution is important but requires reform.",
        "Current evidence: The scheme remains under review.",
        "\"Explain how ministries are organised.\".",
    )
    GOOD_REGRESSION_FIXTURES = (
        "The Tenth Schedule protects governmental stability, but its broad application can convert legislative accountability into party-commanded conformity.",
        "Article 110 confines Money Bills to listed fiscal matters, while Financial Bills follow wider bicameral procedures that preserve Rajya Sabha scrutiny.",
        "PESA strengthens Gram Sabha authority in Fifth Schedule areas, but its distinct statutory verbs do not create a universal veto.",
    )

    def test_rejects_curated_bad_regression_fixtures(self) -> None:
        for value in self.BAD_REGRESSION_FIXTURES:
            self.assertTrue(repair.answer_line_issues(value), value)

    def test_rejects_fragment_instruction_and_mechanical_copy(self) -> None:
        bad = (
            "Added by the 52nd Amendment.",
            "Mention Kihoto Hollohan.",
            "Federalism denotes the constitutional rules and institutional links organised around power.",
        )
        for value in bad:
            self.assertTrue(repair.answer_line_issues(value), value)

    def test_authored_validator_rejects_exam_instructions(self) -> None:
        value = (
            "Trace the move from consultation to scrutiny while emphasising "
            "that association did not create responsible government."
        )
        self.assertIn("instruction", repair.authored_answer_issues(value))

    def test_accepts_curated_good_regression_fixtures(self) -> None:
        for value in self.GOOD_REGRESSION_FIXTURES:
            self.assertEqual([], repair.answer_line_issues(value), value)

    def test_rejects_repeated_cross_topic_phrase(self) -> None:
        lines = [
            (
                f"polity-{number:02d}",
                1,
                "Session",
                "This constitutional safeguard protects rights, but formal independence alone cannot secure accountable outcomes across public institutions.",
            )
            for number in range(1, 5)
        ]
        audit = repair.duplicate_phrase_audit(lines)
        self.assertTrue(audit["repeated_six_word_prefixes"])
        self.assertTrue(audit["repeated_eight_word_cross_topic_phrases"])

    def test_reviewed_map_covers_all_active_sessions(self) -> None:
        reviewed = repair.load_json(repair.REVIEWED_MAP_PATH)
        sessions = [
            session
            for topic in reviewed["topics"].values()
            for session in topic["sessions"]
        ]
        self.assertEqual(55, len(reviewed["topics"]))
        self.assertEqual(1477, len(sessions))
        self.assertTrue(all(session["final"] for session in sessions))

    def test_closing_flow_becomes_structured_flow(self) -> None:
        source = """#### CLOSING RECALL FLOW — TEST

```text
START / CONCEPT: Test
        |
        v
EXACT TERMS: one · two
        |
        v
MECHANISM / ARGUMENT: The Constitution distributes power.
        |
        v
CONSEQUENCE / CONTRAST: Accountability follows constitutional responsibility.
        |
        v
UPSC TRAP / ANSWER-USE: Power is not unlimited.
        |
        v
ANSWER-GRABBING FORMULATION: Constitutional power enables government, but remains limited by accountability.
```"""
        result, count = repair.CLOSING_FLOW_RE.subn(
            repair._closure_replacement,
            source,
        )
        self.assertEqual(1, count)
        self.assertIn("```closure-flow", result)
        self.assertIn("SUBTOPIC: Test", result)
        self.assertIn("KEY TERMS / DEFINITIONS: one · two", result)

    def test_wraps_overlong_visual_lines_without_truncation(self) -> None:
        line = (
            "RIGHT TO KNOW? -> STATE OF U.P. V. RAJ NARAIN (1975) / "
            "S.P. GUPTA V. UNION OF INDIA (1981) -> constitutional transparency"
        )
        wrapped = repair._wrap_visual_line(line)
        self.assertGreater(len(wrapped), 1)
        self.assertTrue(all(len(item) <= repair.MAX_TEXT_FENCE_WIDTH for item in wrapped))
        joined = " ".join(item.strip(" ->") for item in wrapped)
        self.assertIn("constitutional transparency", joined)


if __name__ == "__main__":
    unittest.main()
