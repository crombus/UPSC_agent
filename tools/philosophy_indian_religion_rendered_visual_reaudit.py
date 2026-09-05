"""Repair and rerender the exact 15 active Philosophy visual-audit packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import textwrap
from pathlib import Path
from typing import Any

import markdown_learning_pdf


ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "EXPORT-PDF-STATUS.json"
PRIOR_VALIDATION_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "philosophy-indian-religion-deep-quality-repair-2026-08-25-validation.json"
)
AUDIT_ID = "philosophy-indian-religion-rendered-visual-reaudit-2026-08-26"
REPORT_PATH = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "PHILOSOPHY-INDIAN-RELIGION-RENDERED-VISUAL-REAUDIT-REPORT.md"
)
VALIDATION_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{AUDIT_ID}-validation.json"
)
SCRATCH_MAP_ROOT = ROOT / ".agent-scratch" / "visual-reaudit" / "render-maps"

TOPIC_KEYS = (
    *(f"philosophy-paper-i-indian-philosophy-{index:02d}" for index in range(1, 6)),
    *(
        f"philosophy-paper-ii-philosophy-of-religion-{index:02d}"
        for index in range(1, 11)
    ),
)

CARVAKA_OLD_LEDGER = """```text
                    perception (pratyakṣa)  inference (anumāna)  comparison
                      (upamāna)  verbal testimony (śabda)  postulation
                      (arthāpatti)  non-cognition (anupalabdhi)
                    (percep.)  (infer.) (compar.) (test.) (postul.)  (non-cogn.)
   -----------------------------------------------------------------------------
   CARVAKA             YES        no       no      no       no          no    = 1
   Vaisesika           YES       YES       no      no       no          no    = 2
   Buddhism            YES       YES       no      no       no          no    = 2
   Samkhya / Yoga      YES       YES       no     YES       no          no    = 3
   Nyaya               YES       YES      YES     YES       no          no    = 4
   Prabhakara Mimamsa  YES       YES      YES     YES      YES          no    = 5
   Bhatta Mimamsa /    YES       YES      YES     YES      YES         YES    = 6
   Advaita Vedanta
   -----------------------------------------------------------------------------
        ^
        |
   CARVAKA SITS AT THE MINIMUM OF THE LEDGER.
   Everything else in the system follows from that single cell.
```"""

CARVAKA_NEW_LEDGER = """**Legend:** `P` = perception (*pratyakṣa*); `A` = inference (*anumāna*);
`U` = comparison (*upamāna*); `S` = verbal testimony (*śabda*);
`Ar` = postulation (*arthāpatti*); `An` = non-cognition (*anupalabdhi*).

| School | P | A | U | S | Ar | An | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cārvāka | Yes | No | No | No | No | No | 1 |
| Vaiśeṣika | Yes | Yes | No | No | No | No | 2 |
| Mainstream Buddhist epistemology* | Yes | Yes | No | No | No | No | 2 |
| Sāṃkhya-Yoga | Yes | Yes | No | Yes | No | No | 3 |
| Nyāya | Yes | Yes | Yes | Yes | No | No | 4 |
| Prābhākara Mīmāṃsā | Yes | Yes | Yes | Yes | Yes | No | 5 |
| Bhāṭṭa Mīmāṃsā | Yes | Yes | Yes | Yes | Yes | Yes | 6 |
| Advaita Vedānta* | Yes | Yes | Yes | Yes | Yes | Yes | 6 |

> **Takeaway:** Cārvāka alone recognises perception as the sole independent
> *means of valid knowledge (pramāṇa)* in this standard comparison.

*This is the standard pedagogical ledger. Buddhist classifications vary by
school and period; Advaita's standard later account admits six. Cārvāka may
use inference as fallible practical expectation while denying it independent
status as a means of valid knowledge.*"""


TABLE_SPLITS: dict[str, tuple[tuple[int, ...], tuple[int, ...], str, str]] = {
    "philosophy-paper-i-indian-philosophy-01": (
        (0, 1, 2, 3, 4),
        (0, 5, 6, 7, 8),
        "A. Knowledge, self and continuity",
        "B. Authority, value and liberation",
    ),
    "philosophy-paper-i-indian-philosophy-02": (
        (0, 1, 2, 3),
        (0, 4, 5, 6, 7),
        "A. Knowledge, self and change",
        "B. Universals, causation, God and liberation",
    ),
    "philosophy-paper-i-indian-philosophy-03": (
        (0, 1, 2, 3),
        (0, 4, 5, 6, 7),
        "A. Knowledge, self and change",
        "B. Causation, universals, scripture and liberation",
    ),
    "philosophy-paper-i-indian-philosophy-04": (
        (0, 1, 2, 3),
        (0, 4, 5, 6, 7),
        "A. Knowledge, validity and error",
        "B. Universals, causation, God, self and liberation",
    ),
    "philosophy-paper-i-indian-philosophy-05": (
        (0, 1, 2, 3, 4),
        (0, 5, 6, 7, 8),
        "A. Knowledge, self, plurality and causation",
        "B. God, bondage and forms of liberation",
    ),
    "philosophy-paper-ii-philosophy-of-religion-01": (
        (0, 1, 2, 3),
        (0, 4, 5),
        "A. Model, thinker and ultimate-reality relation",
        "B. Criticism and likely UPSC demand",
    ),
    "philosophy-paper-ii-philosophy-of-religion-03": (
        (0, 1, 2, 3, 4),
        (0, 5, 6, 7),
        "A. Classical defences",
        "B. Process and Indian comparisons",
    ),
}

TABLE_HEADERS: dict[str, str] = {
    "philosophy-paper-i-indian-philosophy-01": (
        "| School | Means of valid knowledge (pramāṇas) | Self | Consciousness | "
        "Action and moral consequence (karma)/rebirth | Scripture | God | "
        "Puruṣārthas | Liberation |"
    ),
    "philosophy-paper-i-indian-philosophy-02": (
        "| School | Means of valid knowledge (pramāṇas) admitted | Self | "
        "Permanence vs change | Universals | Causation | Creator God | Liberation |"
    ),
    "philosophy-paper-i-indian-philosophy-03": (
        "| School | Means of valid knowledge (pramāṇas) | Ontology of self | "
        "Permanence / change | Causation | Universals | Scripture | Liberation |"
    ),
    "philosophy-paper-i-indian-philosophy-04": (
        "| School | Means of valid knowledge (pramāṇas) | Validity theory | "
        "Error theory | Universals | Causation / atomism | God | Self and liberation |"
    ),
    "philosophy-paper-i-indian-philosophy-05": (
        "| School | Means of valid knowledge (pramāṇas) | Self | Plurality/unity | "
        "Causation | God | Bondage | Liberation | Jīvanmukti |"
    ),
    "philosophy-paper-ii-philosophy-of-religion-01": (
        "| Concept/model | Thinker/school | Nature of ultimate reality | "
        "God-world / God-human relation | Central criticism | Likely question form |"
    ),
    "philosophy-paper-ii-philosophy-of-religion-03": (
        "| Test | Freedom | Soul-making | Augustine | Leibniz | Process | Karma | "
        "Buddhism |"
    ),
}


class ReauditError(RuntimeError):
    """Raised when an active scoped package cannot be repaired safely."""


def repo_path(value: str) -> Path:
    return ROOT / value.replace("\\", os.sep)


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT)).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".visual-reaudit-pending")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def write_json_atomic(path: Path, data: object) -> None:
    write_text_atomic(
        path,
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    )


def active_records(status: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for topic_key in TOPIC_KEYS:
        candidates = [
            record
            for record in status["exports"]
            if record.get("topic_key") == topic_key
            and record.get("variant") == "learner-v2"
        ]
        if not candidates:
            raise ReauditError(f"{topic_key}: no learner-v2 record.")
        record = max(candidates, key=lambda item: int(item.get("generation") or 0))
        if not all(
            repo_path(str(record[field])).is_file()
            for field in ("markdown", "main_pdf", "workbook")
        ):
            raise ReauditError(f"{topic_key}: active package is incomplete.")
        records.append(record)
    if len(records) != 15:
        raise ReauditError(f"Expected 15 active records, found {len(records)}.")
    return records


def parse_markdown_table(lines: list[str]) -> list[list[str]]:
    if len(lines) < 2:
        raise ReauditError("Malformed Markdown table.")
    return [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in [lines[0], *lines[2:]]
    ]


def format_markdown_table(rows: list[list[str]], columns: tuple[int, ...]) -> str:
    selected = [[row[index] for index in columns] for row in rows]
    header = "| " + " | ".join(selected[0]) + " |"
    separator = "|" + "|".join("---" for _ in columns) + "|"
    body = [
        "| " + " | ".join(row) + " |"
        for row in selected[1:]
    ]
    return "\n".join([header, separator, *body])


def split_wide_table(
    text: str,
    topic_key: str,
) -> tuple[str, dict[str, Any]]:
    header = TABLE_HEADERS[topic_key]
    start = text.find(header)
    if start < 0:
        raise ReauditError(f"{topic_key}: wide comparison table header not found.")
    end = start
    while end < len(text):
        line_end = text.find("\n", end)
        if line_end < 0:
            line_end = len(text)
        line = text[end:line_end]
        if end > start and not line.strip().startswith("|"):
            break
        end = line_end + 1
    block = text[start:end].rstrip("\n")
    table_lines = block.splitlines()
    rows = parse_markdown_table(table_lines)
    groups = TABLE_SPLITS[topic_key]
    expected_width = len(rows[0])
    if any(len(row) != expected_width for row in rows):
        raise ReauditError(f"{topic_key}: inconsistent source table width.")
    first = format_markdown_table(rows, groups[0])
    second = format_markdown_table(rows, groups[1])
    replacement = (
        f"**{groups[2]}**\n\n{first}\n\n"
        f"**{groups[3]}**\n\n{second}"
    )
    repaired = text[:start] + replacement + text[end:]
    return repaired, {
        "original_columns": expected_width,
        "replacement_columns": [len(groups[0]), len(groups[1])],
        "rows_preserved": len(rows) - 1,
        "labels": [groups[2], groups[3]],
    }


def wrap_preformatted_line(line: str, width: int = 92) -> list[str]:
    if len(line) <= 100:
        return [line]
    leading = re.match(r"^\s*", line).group(0)
    label = re.match(r"^(\s*[^:]{1,18}:\s+)", line)
    continuation = (
        " " * len(label.group(1))
        if label
        else leading + " " * 8
    )
    wrapper = textwrap.TextWrapper(
        width=width,
        subsequent_indent=continuation,
        break_long_words=False,
        break_on_hyphens=False,
        replace_whitespace=False,
        drop_whitespace=True,
    )
    return wrapper.wrap(line)


def reflow_plain_fences(text: str) -> tuple[str, list[dict[str, Any]]]:
    lines = text.splitlines()
    output: list[str] = []
    changes: list[dict[str, Any]] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.strip().startswith("```"):
            start = index
            language = line.strip()[3:].strip().lower()
            body: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                body.append(lines[index])
                index += 1
            if index >= len(lines):
                raise ReauditError("Unclosed preformatted fence.")
            reflowed: list[str] = []
            wrapped_lines = 0
            for body_line in body:
                parts = (
                    wrap_preformatted_line(body_line)
                    if not language
                    else [body_line]
                )
                reflowed.extend(parts)
                if len(parts) > 1:
                    wrapped_lines += 1
            output.append(line)
            output.extend(reflowed)
            output.append(lines[index])
            if wrapped_lines:
                changes.append(
                    {
                        "markdown_body_line_start": start + 1,
                        "wrapped_source_lines": wrapped_lines,
                        "max_before": max(map(len, body), default=0),
                        "max_after": max(map(len, reflowed), default=0),
                    }
                )
            index += 1
            continue
        output.append(line)
        index += 1
    return "\n".join(output) + ("\n" if text.endswith("\n") else ""), changes


def repair_markdown(
    record: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    topic_key = str(record["topic_key"])
    markdown = repo_path(str(record["markdown"]))
    original = markdown.read_text(encoding="utf-8")
    repaired = original
    result: dict[str, Any] = {
        "topic_key": topic_key,
        "markdown": relative(markdown),
        "carvaka_ledger_changed": False,
        "wide_table_split": None,
        "plain_fence_reflows": [],
    }
    if topic_key == "philosophy-paper-i-indian-philosophy-01":
        if CARVAKA_OLD_LEDGER in repaired:
            repaired = repaired.replace(CARVAKA_OLD_LEDGER, CARVAKA_NEW_LEDGER, 1)
            result["carvaka_ledger_changed"] = True
        elif CARVAKA_NEW_LEDGER in repaired:
            result["carvaka_ledger_changed"] = True
        else:
            raise ReauditError("Active Cārvāka ledger fixture was not found.")
    if topic_key in TABLE_SPLITS:
        if TABLE_HEADERS[topic_key] in repaired:
            repaired, split_result = split_wide_table(repaired, topic_key)
        elif all(label in repaired for label in TABLE_SPLITS[topic_key][2:]):
            split_result = {
                "already_split": True,
                "replacement_columns": [
                    len(TABLE_SPLITS[topic_key][0]),
                    len(TABLE_SPLITS[topic_key][1]),
                ],
                "labels": list(TABLE_SPLITS[topic_key][2:]),
            }
        else:
            raise ReauditError(f"{topic_key}: split comparison table not found.")
        result["wide_table_split"] = split_result
    repaired, reflows = reflow_plain_fences(repaired)
    result["plain_fence_reflows"] = reflows
    result["workbook_visual_changed"] = bool(reflows)
    result["source_changed"] = repaired != original
    result["sha256_before"] = hashlib.sha256(original.encode("utf-8")).hexdigest()
    result["sha256_after"] = hashlib.sha256(repaired.encode("utf-8")).hexdigest()
    if result["source_changed"]:
        write_text_atomic(markdown, repaired)
    return repaired, result


def render_record(
    record: dict[str, Any],
    repair_result: dict[str, Any],
) -> dict[str, Any]:
    topic_key = str(record["topic_key"])
    markdown = repo_path(str(record["markdown"]))
    main_pdf = repo_path(str(record["main_pdf"]))
    SCRATCH_MAP_ROOT.mkdir(parents=True, exist_ok=True)
    main_map = SCRATCH_MAP_ROOT / f"{topic_key}-main.json"
    markdown_learning_pdf.build_pdf(
        markdown,
        main_pdf,
        mode="main",
        variant="learner-v2",
        topic_key=topic_key,
        repository_root=ROOT,
        visual_audit_path=main_map,
    )
    workbook = repo_path(str(record["workbook"]))
    workbook_map = SCRATCH_MAP_ROOT / f"{topic_key}-workbook.json"
    markdown_learning_pdf.build_pdf(
        markdown,
        workbook,
        mode="workbook",
        variant="learner-v2",
        topic_key=topic_key,
        repository_root=ROOT,
        visual_audit_path=workbook_map,
    )
    return {
        "main_pdf": relative(main_pdf),
        "main_pdf_sha256": sha256(main_pdf),
        "main_audit_map": relative(main_map),
        "workbook_regenerated": True,
        "workbook_source_visual_reflow": bool(
            repair_result["workbook_visual_changed"]
        ),
        "workbook_pdf_sha256": sha256(workbook),
        "workbook_audit_map": relative(workbook_map),
    }


def sync_final_package(
    record: dict[str, Any],
    prior_validation: dict[str, Any],
    workbook_changed: bool,
) -> dict[str, Any]:
    topic_key = str(record["topic_key"])
    package = prior_validation["final_learning_packages"]["topics"][topic_key]
    main_destination = repo_path(
        str(package["complete_learning_session"]["destination"])
    )
    main_destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(repo_path(str(record["main_pdf"])), main_destination)
    result = {
        "main_destination": relative(main_destination),
        "main_equal": (
            sha256(repo_path(str(record["main_pdf"])))
            == sha256(main_destination)
        ),
        "workbook_destination": str(
            package["solved_practice_workbook"]["destination"]
        ),
        "workbook_equal": True,
        "workbook_copied": False,
    }
    workbook_destination = repo_path(
        str(package["solved_practice_workbook"]["destination"])
    )
    workbook_destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(repo_path(str(record["workbook"])), workbook_destination)
    result["workbook_equal"] = (
        sha256(repo_path(str(record["workbook"])))
        == sha256(workbook_destination)
    )
    result["workbook_copied"] = True
    return result


def update_tracker_pending(
    status: dict[str, Any],
    records: list[dict[str, Any]],
    repair_results: dict[str, dict[str, Any]],
) -> None:
    selected = {str(record["record_id"]): record for record in records}
    for record in status["exports"]:
        active = selected.get(str(record.get("record_id")))
        if not active:
            continue
        topic_key = str(record["topic_key"])
        repair = repair_results[topic_key]
        provenance = record.setdefault("provenance", {})
        provenance["rendered_visual_reaudit"] = {
            "id": AUDIT_ID,
            "date": "2026-08-26",
            "report": relative(REPORT_PATH),
            "validation": relative(VALIDATION_PATH),
            "generation_identity_preserved": True,
            "approval_preserved": True,
            "source_changed": bool(repair["source_changed"]),
            "workbook_visual_changed": bool(repair["workbook_visual_changed"]),
            "workbook_regenerated_for_shared_table_readability": True,
        }
        record["validation"] = {
            "state": "pending",
            "validated_on": None,
            "validator": (
                "tools/validate_philosophy_indian_religion_"
                "rendered_visual_reaudit.py"
            ),
        }
    write_json_atomic(STATUS_PATH, status)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Repair and rerender the exact 15 active visual-audit packages."
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not args.apply:
        parser.error("Pass --apply.")
    status = load_json(STATUS_PATH)
    prior_validation = load_json(PRIOR_VALIDATION_PATH)
    records = active_records(status)
    repair_results: dict[str, dict[str, Any]] = {}
    render_results: dict[str, dict[str, Any]] = {}
    final_results: dict[str, dict[str, Any]] = {}
    for record in records:
        topic_key = str(record["topic_key"])
        _, repair_result = repair_markdown(record)
        repair_results[topic_key] = repair_result
        render_result = render_record(record, repair_result)
        render_results[topic_key] = render_result
        final_results[topic_key] = sync_final_package(
            record,
            prior_validation,
            bool(repair_result["workbook_visual_changed"]),
        )
    update_tracker_pending(status, records, repair_results)
    summary_path = SCRATCH_MAP_ROOT / "repair-summary.json"
    write_json_atomic(
        summary_path,
        {
            "schema_version": 1,
            "audit_id": AUDIT_ID,
            "scope": list(TOPIC_KEYS),
            "repairs": repair_results,
            "renders": render_results,
            "final_packages": final_results,
        },
    )
    print(f"Repaired and rendered {len(records)} active topic packages.")
    print(f"Repair summary: {relative(summary_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
