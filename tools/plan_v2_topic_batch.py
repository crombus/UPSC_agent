"""Plan a deterministic learner-v2 topic batch without generating content."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from generate_v2_section_indexes import (
    ManifestError,
    plan_catalog_topic_batch,
)


ROOT = Path(__file__).resolve().parents[1]


def render_plan(plan: dict[str, object]) -> str:
    subject = plan["subject"]
    section = plan["section"]
    lines = [
        f"Batch command: {plan['batch_command']}",
        f"Subject: {subject['display_name']} ({subject['key']})",
        f"Section: {section['name']} ({section['key']})",
        f"Manifest: {plan['manifest'] or 'catalogue order (not materialised)'}",
        (
            f"Selected: {plan['selected_count']} of requested "
            f"{plan['requested_count']}"
        ),
        "",
    ]
    topics = plan["topics"]
    if not topics:
        lines.append("No eligible planned or incomplete topics remain.")
    for number, topic in enumerate(topics, 1):
        lines.extend(
            [
                (
                    f"{number:02d}. {topic['topic_key']} — "
                    f"{topic['display_title']} [{topic['state']}]"
                ),
                f"    {topic['command']}",
            ]
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("subject", help="Exact catalogue subject name or key.")
    parser.add_argument("section", help="Exact catalogue section name or key.")
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument(
        "--regenerate",
        action="store_true",
        help="Make completed validated topics eligible in manifest order.",
    )
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the deterministic plan as UTF-8 JSON.",
    )
    args = parser.parse_args()
    try:
        plan = plan_catalog_topic_batch(
            args.repository_root,
            args.subject,
            args.section,
            count=args.count,
            regenerate=args.regenerate,
        )
    except (ManifestError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(render_plan(plan), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
