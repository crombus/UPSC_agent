"""Build Economy learner-v2 Topic 01 in authoring-only mode."""

from pathlib import Path

import generate_economy_common as common
from economy_01_data import TOPIC_01

DATE, SUBJECT, KNOWLEDGE = common.DATE, common.SUBJECT, common.KNOWLEDGE
SESSION_DIR, GRAPHICAL_DIR, EXPORT_DIR = common.SESSION_DIR, common.GRAPHICAL_DIR, common.EXPORT_DIR
CATALOG, SECTION_MANIFEST, LOCAL_BOOKS = common.CATALOG, common.SECTION_MANIFEST, common.LOCAL_BOOKS
TOPICS = [TOPIC_01]
PANEL_DATA = {str(item["key"]): item["panels"] for item in TOPICS}
SESSION_PLANS = {str(item["key"]): item["session_plans"] for item in TOPICS}
ASCII_PATH = common.ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs" / "economy-01-2026-09-03-sequential.json"


def self_check(config: dict[str, object], markdown: str, workbook: str, session_count: int, graphical_path: Path) -> None:
    common.self_check(config, markdown, workbook, session_count, graphical_path)


def main() -> int:
    return common.run_batch(topics=TOPICS, ascii_path=ASCII_PATH, scope="Economy learner-v2 Topic 01", previous=None, previous_keys=None)


if __name__ == "__main__":
    raise SystemExit(main())
