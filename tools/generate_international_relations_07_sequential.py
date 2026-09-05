"""Build International Relations learner-v2 Topic 07 in authoring-only mode."""

from __future__ import annotations

from pathlib import Path

import generate_international_relations_common as common
import generate_international_relations_06_sequential as previous_batch
from international_relations_07_data import TOPIC_07


DATE = common.DATE
SUBJECT = common.SUBJECT
KNOWLEDGE = common.KNOWLEDGE
SESSION_DIR = common.SESSION_DIR
GRAPHICAL_DIR = common.GRAPHICAL_DIR
EXPORT_DIR = common.EXPORT_DIR
CATALOG = common.CATALOG
SECTION_MANIFEST = common.SECTION_MANIFEST
LOCAL_BOOKS = common.LOCAL_BOOKS
TOPICS = [TOPIC_07]
PREVIOUS_KEYS = ["international-relations-06"]
PANEL_DATA = {str(config["key"]): config["panels"] for config in TOPICS}
SESSION_PLANS = {str(config["key"]): config["session_plans"] for config in TOPICS}
ASCII_PATH = (
    common.ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "international-relations-07-2026-09-03-sequential.json"
)


def self_check(
    config: dict[str, object],
    markdown: str,
    workbook: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    common.self_check(config, markdown, workbook, session_count, graphical_path)


def main() -> int:
    return common.run_batch(
        topics=TOPICS,
        ascii_path=ASCII_PATH,
        scope="International Relations learner-v2 Topic 07",
        previous=previous_batch,
        previous_keys=PREVIOUS_KEYS,
    )


if __name__ == "__main__":
    raise SystemExit(main())
