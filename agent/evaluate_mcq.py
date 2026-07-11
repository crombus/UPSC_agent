#!/usr/bin/env python3
"""
UPSC Agent — MCQ Answer Evaluator
Scores GS1 and CSAT attempts from JSON answer key + attempts files.

Usage:
  python -m agent.evaluate_mcq --answer-key key.json --attempts my_answers.json
  python -m agent.evaluate_mcq --answer-key key.json --attempts my_answers.json --output result.json

Answer key JSON format:
{
  "questions": [
    {"question_id": "GS1-1", "paper": "GS1", "answer": "A", "topic": "Polity"},
    {"question_id": "CSAT-1", "paper": "CSAT", "answer": "C", "topic": "Reasoning"}
  ]
}

Attempts JSON format:
{
  "answers": {
    "GS1-1": "A",
    "GS1-2": "skip",
    "CSAT-1": "unclear"
  }
}
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

SCORING: Dict[str, Dict[str, float]] = {
    "GS1":  {"correct": 2.0,  "incorrect": -0.33, "skip": 0.0},
    "CSAT": {"correct": 2.5,  "incorrect": -0.83, "skip": 0.0},
}

_SKIP_VALUES    = {"", "-", "skip", "skipped", "blank", "na", "n/a", "not attempted", "unattempted"}
_UNCLEAR_VALUES = {"unclear", "unknown", "illegible", "cannot read", "ambiguous"}

READINESS_BANDS = [
    (85, "Highly ready for this content set"),
    (70, "Good — revise traps"),
    (50, "Moderate — revise concepts and facts"),
    (30, "Weak — repeat major topics"),
    (0,  "Not ready — restart revision"),
]


def _norm_paper(value: Any) -> str:
    text = str(value or "GS1").strip().upper().replace(" ", "")
    if text in {"GS", "GSI", "GS-I", "PRELIMSGS", "PRELIMSGS1", "PAPERI", "PAPER-I"}:
        return "GS1"
    if text in {"PAPERII", "PAPER-II", "CSAT", "GS2", "GS-II"}:
        return "CSAT"
    return text


def _norm_answer(value: Any) -> str:
    text = str(value or "").strip().upper().replace("OPTION", "").strip("()")
    if text.lower() in _SKIP_VALUES:
        return "SKIP"
    if text.lower() in _UNCLEAR_VALUES:
        return "UNCLEAR"
    return text


def evaluate(answer_key: Dict[str, Any], attempts: Dict[str, Any]) -> Dict[str, Any]:
    questions: List[Dict[str, Any]] = answer_key.get("questions", [])
    answers: Dict[str, Any] = attempts.get("answers", attempts)

    summary: Dict[str, Dict[str, Any]] = {}
    rows: List[Dict[str, Any]] = []

    for q in questions:
        qid    = str(q.get("question_id") or q.get("id") or q.get("number") or "?")
        paper  = _norm_paper(q.get("paper", "GS1"))
        correct = _norm_answer(q.get("answer", ""))
        user   = _norm_answer(answers.get(qid, ""))

        if paper not in summary:
            summary[paper] = {
                "total": 0, "attempted": 0, "correct": 0,
                "incorrect": 0, "skipped": 0, "unclear": 0,
                "score": 0.0, "topics": {},
            }
        s = summary[paper]
        s["total"] += 1

        if user == "UNCLEAR":
            result, marks = "unclear", 0.0
            s["unclear"] += 1
        elif user == "SKIP":
            result, marks = "skipped", 0.0
            s["skipped"] += 1
        elif user == correct:
            result = "correct"
            marks  = SCORING.get(paper, SCORING["GS1"])["correct"]
            s["attempted"] += 1
            s["correct"]   += 1
        else:
            result = "incorrect"
            marks  = SCORING.get(paper, SCORING["GS1"])["incorrect"]
            s["attempted"]  += 1
            s["incorrect"]  += 1

        s["score"] += marks
        topic = str(q.get("topic") or "Unmapped")
        ts = s["topics"].setdefault(topic, {"total": 0, "correct": 0, "incorrect": 0, "skipped": 0, "unclear": 0})
        ts["total"] += 1
        ts[result]   = ts.get(result, 0) + 1

        rows.append({
            "question_id":    qid,
            "paper":          paper,
            "topic":          topic,
            "correct_answer": correct,
            "user_answer":    user,
            "result":         result,
            "marks":          round(marks, 2),
        })

    for paper, s in summary.items():
        s["score"] = round(s["score"], 2)
        s["accuracy_among_attempted"] = (
            round(s["correct"] / s["attempted"] * 100, 2) if s["attempted"] else 0.0
        )
        max_score = s["total"] * SCORING.get(paper, SCORING["GS1"])["correct"]
        pct = (s["score"] / max_score * 100) if max_score else 0
        for threshold, label in READINESS_BANDS:
            if pct >= threshold:
                s["readiness"] = label
                break

    return {"summary": summary, "rows": rows}


def format_report(result: Dict[str, Any]) -> str:
    """Return a human-readable score report."""
    lines = ["━" * 50, "UPSC MCQ EVALUATION REPORT", "━" * 50]
    for paper, s in result["summary"].items():
        scoring = SCORING.get(paper, SCORING["GS1"])
        max_score = round(s["total"] * scoring["correct"], 2)
        lines += [
            f"\n{paper} — Prelims Paper {'I' if paper == 'GS1' else 'II'}",
            f"  Total:       {s['total']}",
            f"  Attempted:   {s['attempted']}",
            f"  Correct:     {s['correct']}",
            f"  Incorrect:   {s['incorrect']}",
            f"  Skipped:     {s['skipped']}",
            f"  Unclear:     {s['unclear']}",
            f"  Score:       {s['score']} / {max_score}",
            f"  Accuracy:    {s['accuracy_among_attempted']}%",
            f"  Readiness:   {s.get('readiness', '—')}",
        ]
        if s["topics"]:
            lines.append("\n  Topic-wise:")
            for topic, ts in s["topics"].items():
                lines.append(
                    f"    {topic}: {ts['correct']}✓ {ts['incorrect']}✗ {ts['skipped']}— {ts['unclear']}?"
                )
    lines.append("\n⚠️  Readiness score is inference-based — not an official UPSC score.")
    lines.append("━" * 50)
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate UPSC GS1/CSAT MCQ attempts")
    parser.add_argument("--answer-key", required=True, help="Path to answer key JSON")
    parser.add_argument("--attempts",   required=True, help="Path to attempts JSON")
    parser.add_argument("--output",     help="Optional output JSON path")
    parser.add_argument("--report",     action="store_true", help="Print human-readable report")
    args = parser.parse_args()

    key_data = json.loads(Path(args.answer_key).read_text(encoding="utf-8"))
    att_data = json.loads(Path(args.attempts).read_text(encoding="utf-8"))
    result   = evaluate(key_data, att_data)

    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"✅ Results saved to {args.output}")

    if args.report or not args.output:
        print(format_report(result))


if __name__ == "__main__":
    main()
