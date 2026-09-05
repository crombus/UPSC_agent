"""Build Geography learner-v2 Topic 21 in authoring-only mode."""

from __future__ import annotations

from pathlib import Path

import generate_geography_20_sequential as previous
import generate_geography_common as common
from geography_20_22_data import TOPIC_21


DATE = common.DATE
SUBJECT = common.SUBJECT
SECTION = common.SECTION
KNOWLEDGE = common.KNOWLEDGE
SESSION_DIR = common.SESSION_DIR
GRAPHICAL_DIR = common.GRAPHICAL_DIR
EXPORT_DIR = common.EXPORT_DIR
CATALOG = common.CATALOG
SECTION_MANIFEST = common.SECTION_MANIFEST
LOCAL_BOOKS = common.LOCAL_BOOKS
TOPICS = [TOPIC_21]
PANEL_DATA = {str(config["key"]): config["panels"] for config in TOPICS}
SESSION_PLANS = {str(config["key"]): config["session_plans"] for config in TOPICS}
ASCII_PATH = (
    common.ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "geography-21-2026-09-01-sequential.json"
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
        scope="Geography learner-v2 Topic 21",
        previous=previous,
        previous_keys=["geography-20"],
    )


if __name__ == "__main__":
    raise SystemExit(main())
