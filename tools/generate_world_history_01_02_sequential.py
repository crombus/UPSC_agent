"""Build World History learner-v2 Topics 01-02 in authoring-only mode."""

from __future__ import annotations

from pathlib import Path

import generate_world_history_common as common
from world_history_01_05_data import TOPIC_01, TOPIC_02


DATE = common.DATE
SUBJECT = common.SUBJECT
KNOWLEDGE = common.KNOWLEDGE
SESSION_DIR = common.SESSION_DIR
GRAPHICAL_DIR = common.GRAPHICAL_DIR
EXPORT_DIR = common.EXPORT_DIR
CATALOG = common.CATALOG
SECTION_MANIFEST = common.SECTION_MANIFEST
LOCAL_BOOKS = common.LOCAL_BOOKS
TOPICS = [TOPIC_01, TOPIC_02]
PANEL_DATA = {str(config["key"]): config["panels"] for config in TOPICS}
SESSION_PLANS = {
    str(config["key"]): config["session_plans"] for config in TOPICS
}
ASCII_PATH = (
    common.ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "world-history-01-02-2026-09-01-sequential.json"
)


def self_check(
    config: dict[str, object],
    markdown: str,
    workbook: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    common.self_check(
        config,
        markdown,
        workbook,
        session_count,
        graphical_path,
    )


def main() -> int:
    return common.run_batch(
        topics=TOPICS,
        ascii_path=ASCII_PATH,
        scope="World History learner-v2 Topics 01-02",
    )


if __name__ == "__main__":
    raise SystemExit(main())
