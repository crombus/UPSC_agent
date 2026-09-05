"""Run the shared pre-render audits on one authored Economy topic."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import refresh_all_v2_learning_sessions as refresh  # noqa: E402
import validate_v2_export as validator  # noqa: E402


SESSION_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Economy"
    / "learning-sessions"
    / "v2"
    / "subject-wide-syllabus"
)


def simulate(topic_key: str, title: str) -> dict[str, object]:
    source = SESSION_DIR / f"{topic_key}_Learning-Session.md"
    workbook = SESSION_DIR / f"{topic_key}_Solved-Workbook.md"
    markdown = source.read_text(encoding="utf-8")
    topic = refresh.Topic(
        key=topic_key,
        subject="Economy",
        section="Subject-Wide-Syllabus",
        topic_folder=topic_key,
        title=title,
        generation=1,
        record_id=f"{topic_key}:learner-v2:g1",
        markdown=source,
        main_pdf=source,
        workbook=workbook,
        source_record={},
    )
    transformed = refresh.sessionize(markdown, topic, refresh.merged_overrides())
    transformed = refresh.strip_legacy_progress_navigation(transformed)
    transformed, mcq_audit = refresh.rebalance_mcqs(transformed, topic_key)
    transformed, ascii_text = refresh.ensure_ascii_master(
        transformed,
        topic,
        require_manual=True,
    )
    audits = {
        "core_completeness_errors": refresh.core_completeness_errors(transformed),
        "ascii_master_errors": validator.validate_ascii_master_text(
            ascii_text,
            topic_key=topic_key,
        ),
        "markdown_validation": validator.validate_v2_markdown(source),
    }
    for name, text in (
        ("markdown_deep_defects", markdown),
        ("sessionized_deep_defects", transformed),
        ("workbook_deep_defects", workbook.read_text(encoding="utf-8")),
    ):
        audit = validator.deep_content_quality_audit_text(text, topic_key=topic_key)
        audits[name] = [
            item
            for item in audit["defects"]
            if item.get("severity") in {"blocker", "high"}
        ]
    authored = re.findall(r"(?m)^### SESSION (\d+) — (.+?) — (.+?)\s*$", markdown)
    published = re.findall(r"(?m)^### SESSION (\d+) — ", transformed)
    audits["session_errors"] = []
    if len(authored) != 15 or len(published) != 15:
        audits["session_errors"].append(
            f"authored={len(authored)}, published={len(published)}, expected=15"
        )
    if transformed.count("#### VISUAL FIRST") != 15:
        audits["session_errors"].append("published visual-first count is not 15")
    return {
        "topic_key": topic_key,
        "mcq_audit": {
            "counts": mcq_audit.get("answer_counts"),
            "total": mcq_audit.get("question_count"),
        },
        **audits,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_key")
    parser.add_argument("title")
    args = parser.parse_args()
    result = simulate(args.topic_key, args.title)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if any(
        result[name]
        for name in (
            "core_completeness_errors",
            "ascii_master_errors",
            "markdown_validation",
            "markdown_deep_defects",
            "sessionized_deep_defects",
            "workbook_deep_defects",
            "session_errors",
        )
    ) else 0


if __name__ == "__main__":
    raise SystemExit(main())
