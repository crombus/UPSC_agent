"""Build Environment and Ecology learner-v2 Topic 24 in authoring-only mode."""

from __future__ import annotations

from pathlib import Path

import generate_environment_and_ecology_23_sequential as previous_batch
import generate_environment_and_ecology_common as common
from environment_and_ecology_24_data import TOPIC_24


DATE = common.DATE
SUBJECT = common.SUBJECT
KNOWLEDGE = common.KNOWLEDGE
SESSION_DIR = common.SESSION_DIR
GRAPHICAL_DIR = common.GRAPHICAL_DIR
EXPORT_DIR = common.EXPORT_DIR
CATALOG = common.CATALOG
SECTION_MANIFEST = common.SECTION_MANIFEST
LOCAL_BOOKS = common.LOCAL_BOOKS
TOPICS = [TOPIC_24]
PANEL_DATA = {str(config["key"]): config["panels"] for config in TOPICS}
SESSION_PLANS = {str(config["key"]): config["session_plans"] for config in TOPICS}
ASCII_PATH = (
    common.ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    / "environment-and-ecology-24-2026-09-03-sequential.json"
)


def self_check(config: dict[str, object], markdown: str, workbook: str, session_count: int, graphical_path: Path) -> None:
    common.self_check(config, markdown, workbook, session_count, graphical_path)


def main() -> int:
    return common.run_batch(
        topics=TOPICS,
        ascii_path=ASCII_PATH,
        scope="Environment and Ecology learner-v2 Topic 24",
        previous=previous_batch,
        previous_keys=["environment-and-ecology-23"],
    )


if __name__ == "__main__":
    raise SystemExit(main())
