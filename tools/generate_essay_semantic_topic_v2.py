"""Generate one standard learner-v2 Essay topic for semantic review."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ["ESSAY_TOPIC_DATE"] = "2026-09-06"

import essay_semantic_data as data  # noqa: E402
import generate_essay_common as common  # noqa: E402


DATE = "2026-09-06"
ROOT = Path(__file__).resolve().parents[1]


def generate(number: int) -> dict[str, object]:
    common.DATE = DATE
    common.SESSION_DIR = (
        ROOT / "upsc-ai-kit" / "knowledge" / "Essay"
        / "learning-sessions" / "v2" / "subject-wide-syllabus"
    )
    changed_owner = data.canonical_repair(number)
    config = data.build_topic(number)
    ascii_path = (
        ROOT / "upsc-ai-kit" / "manifests" / "retrofits"
        / "ascii-panel-specs" / f"essay-{number:02d}-{DATE}-sequential.json"
    )
    with common._configured():
        common._base.run_batch(
            topics=[config],
            ascii_path=ascii_path,
            scope=f"Essay semantic learner-v2 Topic {number:02d}",
        )
    return {
        "topic_key": config["key"],
        "title": config["title"],
        "canonical_owner_changed": changed_owner,
        "generation_spec": str(
            common.EXPORT_DIR / f"{config['key']}-new-topic-{DATE}.json"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=range(1, 17), required=True)
    args = parser.parse_args()
    print(generate(args.topic))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
