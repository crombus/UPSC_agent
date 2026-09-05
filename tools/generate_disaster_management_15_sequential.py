"""Build Disaster Management learner-v2 Topic 15 in authoring-only mode."""

from pathlib import Path

import generate_disaster_management_14_sequential as previous
import generate_disaster_management_common as common
from disaster_management_15_data import TOPIC_15


DATE, SUBJECT, KNOWLEDGE = common.DATE, common.SUBJECT, common.KNOWLEDGE
SESSION_DIR, GRAPHICAL_DIR, EXPORT_DIR = common.SESSION_DIR, common.GRAPHICAL_DIR, common.EXPORT_DIR
CATALOG, SECTION_MANIFEST, LOCAL_BOOKS = common.CATALOG, common.SECTION_MANIFEST, common.LOCAL_BOOKS
TOPICS = [TOPIC_15]
PANEL_DATA = {str(config["key"]): config["panels"] for config in TOPICS}
SESSION_PLANS = {str(config["key"]): config["session_plans"] for config in TOPICS}
ASCII_PATH = common.ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs" / f"disaster-management-15-{DATE}-sequential.json"


def self_check(config: dict[str, object], markdown: str, workbook: str, session_count: int, graphical_path: Path) -> None:
    common.self_check(config, markdown, workbook, session_count, graphical_path)


def main() -> int:
    return common.run_batch(
        topics=TOPICS,
        ascii_path=ASCII_PATH,
        scope="Disaster Management learner-v2 Topic 15",
        previous=previous,
        previous_keys=["disaster-management-14"],
    )


if __name__ == "__main__":
    raise SystemExit(main())
