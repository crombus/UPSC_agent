"""Programmatic proof of the Governance 13-16 learner-v2 per-topic contracts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
KEYS = ["governance-13", "governance-14", "governance-15", "governance-16"]
REQUIRED_H2 = [
    "BASIC LEARNING SESSION",
    "BASIC MCQS / REMEDIATION",
    "PYQS AND ANSWER PRACTICE",
    "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
    "CONSOLIDATED REGISTER NOTES",
]
READ_ONLY_PREFIXES = (
    "books\\",
    "upsc-ai-kit\\knowledge\\_PYQ-ROUTING",
    "upsc-ai-kit\\knowledge\\Governance\\basic\\",
    "upsc-ai-kit\\knowledge\\Governance\\advanced\\",
    "upsc-ai-kit\\manifests\\v2\\topic-catalog.json",
)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    tracker = json.loads((ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8"))
    failures: list[str] = []
    for key in KEYS:
        record_id = f"{key}:learner-v2:g1"
        records = [
            item
            for item in tracker["exports"]
            if isinstance(item, dict) and item.get("record_id") == record_id
        ]
        if len(records) != 1:
            failures.append(f"{key}: expected exactly one record, found {len(records)}")
            continue
        record = records[0]
        completion = json.loads(
            (
                ROOT
                / "upsc-ai-kit"
                / "manifests"
                / "exports"
                / f"{key}-learner-v2-g1-2026-09-02-completion.json"
            ).read_text(encoding="utf-8")
        )
        metrics = completion["metrics"]
        gates = completion["hard_gates"]
        markdown = (ROOT / str(record["markdown"])).read_text(encoding="utf-8")
        workbook_md = (ROOT / str(record["workbook_markdown"])).read_text(
            encoding="utf-8"
        )
        headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
        ordered = [item for item in headings if item in REQUIRED_H2]
        answers = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown)
        workbook_answers = re.findall(
            r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook_md
        )
        with fitz.open(ROOT / str(record["main_pdf"])) as pdf:
            main_pages = pdf.page_count
        with fitz.open(ROOT / str(record["workbook"])) as pdf:
            workbook_pages = pdf.page_count
        changed = (
            ROOT
            / "upsc-ai-kit"
            / "manifests"
            / "exports"
            / f"{key}-learner-v2-g1-2026-09-02-changed-files.txt"
        ).read_text(encoding="utf-8").splitlines()
        leaked = [
            line
            for line in changed
            if line.strip() and line.startswith(READ_ONLY_PREFIXES)
        ]
        checks = {
            "single_unapproved_record": record.get("approved") is False
            and record["approval"]["approved"] is False,
            "all_hard_gates": all(gates.values()),
            "twenty_fact_anchors": metrics["fact_anchor_count"] == 20,
            "fifteen_visual_first_sessions": metrics["learner_session_count"] == 15
            and metrics["visual_first_count"] == 15,
            "eighty_unique_mcqs": metrics["mcq_count"] == 80
            and metrics["mcq_unique_stem_count"] == 80,
            "strict_abcd_a20_b20_c20_d20": answers == list("ABCD") * 20
            and workbook_answers == list("ABCD") * 20
            and {letter: answers.count(letter) for letter in "ABCD"}
            == {letter: 20 for letter in "ABCD"},
            "mains_10_10_15_15_20_20": metrics["original_mains_weights"]
            == [10, 10, 15, 15, 20, 20],
            "twelve_ascii_panels": metrics["ascii_panel_count"] == 12,
            "thirteen_graphical_stages": metrics["graphical_stage_count"] == 13,
            "required_h2_order": ordered == REQUIRED_H2,
            "register_notes_final_h2": headings[-1] == "CONSOLIDATED REGISTER NOTES",
            "real_pdf_pages": main_pages > 0 and workbook_pages > 0,
            "changed_files_exclude_read_only": not leaked,
        }
        bad = [name for name, ok in checks.items() if not ok]
        failures.extend(f"{key}: {name}" for name in bad)
        print(
            json.dumps(
                {
                    "record_id": record_id,
                    "generation": record["generation"],
                    "approved": record["approved"],
                    "main_pdf_pages": main_pages,
                    "workbook_pdf_pages": workbook_pages,
                    "answer_distribution": {
                        letter: answers.count(letter) for letter in "ABCD"
                    },
                    "final_h2": headings[-1],
                    "changed_file_count": len([x for x in changed if x.strip()]),
                    "checks_passed": f"{len(checks) - len(bad)}/{len(checks)}",
                    "failed_checks": bad,
                },
                ensure_ascii=False,
            )
        )
    print("RESULT:", "PASSED" if not failures else f"FAILED {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
