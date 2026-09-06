import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
OUTPUT_ROOT = ROOT / "quick_galance"
STATUS_PATH = OUTPUT_ROOT / "TREE-CHART-STATUS.json"
INDEX_PATH = OUTPUT_ROOT / "TREE-CHART-INDEX.md"
COMMAND_INDEX_PATH = OUTPUT_ROOT / "TREE-CHART-COMMAND-INDEX.md"
EXCLUDED_SUBJECTS = {"Essay", "CSAT", "Qualifying-English", "Qualifying-Hindi"}


def output_stem(topic: dict) -> str:
    source = topic.get("source_basic") or topic["source_canonical"]
    source_path = Path(source)
    if source_path.parent.name == "basic":
        return source_path.stem
    return topic["topic_key"]


def expected_output(topic: dict) -> Path:
    subject = topic["subject"]["key"]
    return OUTPUT_ROOT / subject / f"{output_stem(topic)}_Tree-Chart.md"


def build_records(catalog: dict) -> list[dict]:
    records = []
    included_topics = [
        topic
        for topic in catalog["topics"]
        if topic["subject"]["key"] not in EXCLUDED_SUBJECTS
    ]
    included_topics.sort(
        key=lambda topic: (
            topic["subject"]["order"],
            topic["section"]["order"],
            topic["topic_order"],
            topic["topic_key"],
        )
    )

    for sequence, topic in enumerate(included_topics, start=1):
        output = expected_output(topic)
        records.append(
            {
                "sequence": sequence,
                "subject": topic["subject"]["key"],
                "subject_display": topic["subject"]["display_name"],
                "section": topic["section"]["name"],
                "topic_key": topic["topic_key"],
                "title": topic["display_title"],
                "source_basic": topic.get("source_basic"),
                "source_advanced": topic.get("source_advanced"),
                "source_canonical": topic["source_canonical"],
                "output_path": str(output.relative_to(ROOT)),
                "status": "completed" if output.exists() else "pending",
            }
        )
    return records


def write_status(records: list[dict]) -> None:
    completed = sum(record["status"] == "completed" for record in records)
    payload = {
        "schema_version": 1,
        "policy": {
            "generation_mode": "strictly sequential, one topic at a time",
            "coverage": "canonical Basic, Advanced and verified PYQ material; no batch chart generation",
            "excluded_subjects": sorted(EXCLUDED_SUBJECTS),
            "output_root": "quick_galance",
        },
        "statistics": {
            "total_topics": len(records),
            "completed": completed,
            "pending": len(records) - completed,
        },
        "next_pending": next(
            (record["topic_key"] for record in records if record["status"] == "pending"),
            None,
        ),
        "topics": records,
    }
    STATUS_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def clean_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value).replace("|", "\\|")


def write_index(records: list[dict]) -> None:
    completed = sum(record["status"] == "completed" for record in records)
    lines = [
        "# Quick-Glance Tree-Chart Completion Index",
        "",
        f"**Total included topics:** {len(records)}  ",
        f"**Completed:** {completed}  ",
        f"**Pending:** {len(records) - completed}  ",
        "**Excluded:** Essay, CSAT, Qualifying English and Qualifying Hindi",
        "",
        "## Generation rule",
        "",
        "Charts are generated strictly in catalogue order, one topic at a time. Each chart must be",
        "manually derived from its canonical Basic/Core owner, Advanced owner and relevant verified",
        "PYQs. No batch content generation, generic template filling or source compression is allowed.",
        "",
    ]

    current_subject = None
    for record in records:
        if record["subject"] != current_subject:
            if current_subject is not None:
                lines.append("")
            current_subject = record["subject"]
            lines.extend(
                [
                    f"## {record['subject_display']}",
                    "",
                    "| Seq. | Status | Topic | Section | Output |",
                    "|---:|---|---|---|---|",
                ]
            )
        mark = "✅ Completed" if record["status"] == "completed" else "⬜ Pending"
        output = record["output_path"]
        output_link = str(Path(output).relative_to("quick_galance")).replace("\\", "/")
        lines.append(
            f"| {record['sequence']} | {mark} | "
            f"{clean_cell(record['title'])} | {clean_cell(record['section'])} | "
            f"[`{clean_cell(output)}`]({output_link}) |"
        )
    INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def topic_command(record: dict) -> str:
    if record["subject"] == "Philosophy":
        return (
            f"Export Tree Chart: {record['subject_display']} — "
            f"{record['section']} — {record['title']}"
        )
    return f"Export Tree Chart: {record['subject_display']} — {record['title']}"


def write_command_index(records: list[dict]) -> None:
    pending = [record for record in records if record["status"] == "pending"]
    lines = [
        "# Quick-Glance Tree-Chart Copy-Ready Commands",
        "",
        f"**Pending commands:** {len(pending)}  ",
        "**Execution rule:** submit commands strictly from top to bottom, one at a time.",
        "",
        "## Repeatable next-topic command",
        "",
        "Use this same command whenever you want the tracker to resolve and generate exactly the",
        "first pending topic:",
        "",
        "```text",
        "Continue Quick-Glance Atlas",
        "```",
        "",
    ]

    if pending:
        lines.extend(
            [
                "## Next specific command",
                "",
                "```text",
                topic_command(pending[0]),
                "```",
                "",
            ]
        )

    current_subject = None
    for record in pending:
        if record["subject"] != current_subject:
            current_subject = record["subject"]
            lines.extend([f"## {record['subject_display']}", ""])
        lines.extend(
            [
                f"### {record['sequence']}. {record['title']}",
                "",
                "```text",
                topic_command(record),
                "```",
                "",
            ]
        )
    COMMAND_INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    records = build_records(catalog)
    write_status(records)
    write_index(records)
    write_command_index(records)
    print(
        f"Indexed {len(records)} topics: "
        f"{sum(record['status'] == 'completed' for record in records)} completed."
    )


if __name__ == "__main__":
    main()
