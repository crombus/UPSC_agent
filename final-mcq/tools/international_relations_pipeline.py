"""Read-only release checks for the International Relations final-MCQ queue."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "International-Relations"
INDEX = SUBJECT / "INDEX.md"
CATALOGUE = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
QUESTION = re.compile(r"^### (\d+)\. (.+)$", re.M)
ANSWER = re.compile(r"^### (\d+)\. ([A-D])\s*$", re.M)


def inspect_bank(folder: Path) -> tuple[dict, list[str]]:
    findings: list[str] = []
    qpath, apath, cpath = folder / "QUESTIONS.md", folder / "ANSWERS.md", folder / "COVERAGE.md"
    if not all(p.is_file() for p in (qpath, apath, cpath)):
        return {}, ["missing QUESTIONS.md, ANSWERS.md or COVERAGE.md"]
    questions = qpath.read_text(encoding="utf-8")
    answers = apath.read_text(encoding="utf-8")
    qm = list(QUESTION.finditer(questions))
    am = list(ANSWER.finditer(answers))
    qnums = [int(m.group(1)) for m in qm]
    anums = [int(m.group(1)) for m in am]
    if len(qnums) < 40:
        findings.append("fewer than 40 questions")
    if qnums != list(range(1, len(qnums) + 1)):
        findings.append("question numbering is not contiguous")
    if anums != qnums:
        findings.append("answer mapping is not one-to-one")
    for i, m in enumerate(qm):
        end = qm[i + 1].start() if i + 1 < len(qm) else len(questions)
        options = re.findall(r"^[A-D]\. (.+)$", questions[m.end():end], re.M)
        if len(options) != 4:
            findings.append(f"Q{m.group(1)} lacks four options")
            continue
        lengths = [len(x) for x in options]
        if max(lengths) > 1.65 * max(1, min(lengths)):
            findings.append(f"Q{m.group(1)} option-length cue")
    for i, m in enumerate(am):
        end = am[i + 1].start() if i + 1 < len(am) else len(answers)
        body = answers[m.end():end]
        rationales = re.findall(r"^- \*\*([A-D])\s+[^:]+:\*\*", body, re.M)
        if sorted(rationales) != list("ABCD"):
            findings.append(f"Q{m.group(1)} lacks four option-specific rationales")
        if "**Sources:**" not in body or "**Examiner trap:**" not in body:
            findings.append(f"Q{m.group(1)} lacks source or trap")
    for pattern in (r"\*\*Correct answer", r"\*\*Sources:", r"\*\*Examiner trap:", r"Answer key"):
        if re.search(pattern, questions, re.I):
            findings.append(f"answer leakage: {pattern}")
    keys = Counter(m.group(2) for m in am)
    return {"questions": len(qnums), "answers": len(anums), "keys": dict(keys)}, findings


def next_topic() -> str:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    entries = data.get("topics", data) if isinstance(data, dict) else data
    ir = [e for e in entries if isinstance(e, dict) and e.get("subject", {}).get("key") == "International-Relations"]
    ir.sort(key=lambda e: e["topic_order"])
    index_text = INDEX.read_text(encoding="utf-8")
    completed = {
        int(match.group(1))
        for match in re.finditer(r"^\|\s*(\d+)\s*\|.*?\|\s*\*\*`?complete", index_text, re.M | re.I)
    }
    for entry in ir:
        if int(entry["topic_order"]) not in completed:
            return entry["display_title"]
    return "none"


def main() -> None:
    required = [
        "COVERAGE.md",
        "SOURCE-AND-PYQ-HOLDS.md",
        "STRUCTURAL-AUDIT.md",
        "HOSTILE-AUDIT.md",
        "AUDIT-REPORT.md",
        "VALIDATION.json",
    ]
    completed_orders = sorted(
        int(match.group(1))
        for match in re.finditer(
            r"^\|\s*(\d+)\s*\|.*?\|\s*\*\*`?complete", INDEX.read_text(encoding="utf-8"), re.M | re.I
        )
    )
    if not completed_orders:
        raise SystemExit("IR PIPELINE: FAIL — no completed topic is indexed")
    all_results: dict[int, dict[int, dict]] = {}
    for order in completed_orders:
        folders = sorted(SUBJECT.glob(f"{order:02d}-*"))
        if len(folders) != 1:
            raise SystemExit(f"IR PIPELINE: FAIL — expected one folder for topic {order:02d}")
        topic = folders[0]
        missing = [name for name in required if not (topic / name).is_file()]
        if missing:
            raise SystemExit(f"IR PIPELINE: FAIL — topic {order:02d} missing {missing}")
        results: dict[int, dict] = {}
        stems: set[str] = set()
        for revision in range(1, 4):
            result, findings = inspect_bank(topic / f"revision-{revision}")
            if findings:
                raise SystemExit(
                    f"IR PIPELINE: FAIL — topic {order:02d} revision-{revision}: "
                    + "; ".join(findings)
                )
            coverage = (topic / f"revision-{revision}" / "COVERAGE.md").read_text(encoding="utf-8")
            if len(re.findall(r"^\|\s*\d+\s*\|", coverage, re.M)) < result["questions"]:
                raise SystemExit(
                    f"IR PIPELINE: FAIL — topic {order:02d} revision-{revision} coverage ledger is incomplete"
                )
            qtext = (topic / f"revision-{revision}" / "QUESTIONS.md").read_text(encoding="utf-8")
            for match in QUESTION.finditer(qtext):
                stem = re.sub(r"\s+", " ", match.group(2).strip()).lower()
                if stem in stems:
                    raise SystemExit(
                        f"IR PIPELINE: FAIL — topic {order:02d} duplicate stem: Q{match.group(1)}"
                    )
                stems.add(stem)
            results[revision] = result
        all_results[order] = results
    if "complete" not in INDEX.read_text(encoding="utf-8").lower():
        raise SystemExit("IR PIPELINE: FAIL — subject index is not complete")
    total = sum(r["questions"] for topic_results in all_results.values() for r in topic_results.values())
    latest = max(all_results)
    latest_result = all_results[latest]
    print(
        f"INTERNATIONAL RELATIONS PIPELINE: PASS — completed topics {','.join(f'{x:02d}' for x in completed_orders)}, "
        f"{total} questions across all released R1/R2/R3 banks; "
        f"latest keys={latest_result[1]['keys']}/{latest_result[2]['keys']}/{latest_result[3]['keys']}"
    )
    print(f"NEXT PENDING: {next_topic()}")


if __name__ == "__main__":
    main()
