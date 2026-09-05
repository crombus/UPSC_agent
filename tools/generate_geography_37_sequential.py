"""Build Geography learner-v2 Topic 37 in authoring-only mode."""

from __future__ import annotations

from pathlib import Path

import generate_geography_common as common
from geography_31_33_37_data import TOPIC_37


DATE = common.DATE
SUBJECT = common.SUBJECT
SECTION = "Part-B-Human-Economic-and-Regional-Geography"
SECTION_KEY = "part-b-human-economic-and-regional-geography"
GENERATION = 1
KNOWLEDGE = common.KNOWLEDGE
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / SECTION_KEY
GRAPHICAL_DIR = common.GRAPHICAL_DIR
EXPORT_DIR = common.EXPORT_DIR
CATALOG = common.CATALOG
SECTION_MANIFEST = (
    common.ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "geography--part-b-human-economic-and-regional-geography.json"
)
LOCAL_BOOKS = common.LOCAL_BOOKS
TOPICS = [TOPIC_37]
PANEL_DATA = {str(config["key"]): config["panels"] for config in TOPICS}
SESSION_PLANS = {str(config["key"]): config["session_plans"] for config in TOPICS}
ASCII_PATH = (
    common.ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "geography-37-2026-09-01-sequential.json"
)


def _configure_common() -> None:
    common.SECTION = SECTION
    common.SECTION_KEY = SECTION_KEY
    common.REQUIRED_TOPIC_NUMBERS = tuple(range(26, 38))
    common.GENERATION = GENERATION
    common.SUPERSEDES_TEMPLATE = None
    common.ALLOW_EXISTING_HISTORY = False
    common.SESSION_DIR = SESSION_DIR
    common.SECTION_MANIFEST = SECTION_MANIFEST


def self_check(
    config: dict[str, object],
    markdown: str,
    workbook: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    _configure_common()
    common.self_check(config, markdown, workbook, session_count, graphical_path)


def main() -> int:
    _configure_common()
    return common.run_batch(
        topics=TOPICS,
        ascii_path=ASCII_PATH,
        scope="Geography learner-v2 Topic 37 sequential build",
    )


if __name__ == "__main__":
    raise SystemExit(main())

