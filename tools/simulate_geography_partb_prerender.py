"""Pre-render simulation for Geography Part-B learner-v2 topics.

Runs sessionize, MCQ rebalance, ASCII master embedding, deep semantic audit and
core-completeness checks against an assembled learning session before any PDF is
rendered or any tracker is touched.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import refresh_all_v2_learning_sessions as refresh  # noqa: E402
import validate_v2_export as validator  # noqa: E402


SECTION = "Part-B-Human-Economic-and-Regional-Geography"
SECTION_KEY = "part-b-human-economic-and-regional-geography"
SESSION_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Geography"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
)


def simulate(topic_key: str, title: str) -> dict[str, object]:
    source = SESSION_DIR / f"{topic_key}_Learning-Session.md"
    workbook = SESSION_DIR / f"{topic_key}_Solved-Workbook.md"
    markdown = source.read_text(encoding="utf-8")
    topic = refresh.Topic(
        key=topic_key,
        subject="Geography",
        section=SECTION,
        topic_folder=topic_key,
        title=title,
        generation=1,
        record_id=f"{topic_key}:legacy-v1:g1",
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
    core_errors = refresh.core_completeness_errors(transformed)
    ascii_errors = validator.validate_ascii_master_text(
        ascii_text,
        topic_key=topic_key,
    )
    deep = validator.deep_content_quality_audit_text(markdown, topic_key=topic_key)
    deep_high = [
        defect
        for defect in deep["defects"]
        if defect.get("severity") in {"blocker", "high"}
    ]
    workbook_deep = validator.deep_content_quality_audit_text(
        workbook.read_text(encoding="utf-8"),
        topic_key=topic_key,
    )
    workbook_high = [
        defect
        for defect in workbook_deep["defects"]
        if defect.get("severity") in {"blocker", "high"}
    ]
    return {
        "topic_key": topic_key,
        "sessionize_ok": bool(transformed),
        "mcq_audit": {
            "counts": mcq_audit.get("answer_counts"),
            "total": mcq_audit.get("question_count"),
        },
        "core_completeness_errors": core_errors,
        "ascii_master_errors": ascii_errors,
        "markdown_deep_defects": deep_high,
        "workbook_deep_defects": workbook_high,
        "markdown_validation": validator.validate_v2_markdown(source),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_key")
    parser.add_argument("title")
    args = parser.parse_args()
    result = simulate(args.topic_key, args.title)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    failed = any(
        result[field]
        for field in (
            "core_completeness_errors",
            "ascii_master_errors",
            "markdown_deep_defects",
            "workbook_deep_defects",
            "markdown_validation",
        )
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
