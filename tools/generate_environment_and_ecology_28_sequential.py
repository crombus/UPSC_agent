"""Build Environment and Ecology learner-v2 Topic 28 in authoring-only mode."""

from pathlib import Path

import generate_environment_and_ecology_27_sequential as previous_batch
import generate_environment_and_ecology_common as common
from environment_and_ecology_25_28_data import TOPIC_28

DATE, SUBJECT, KNOWLEDGE = common.DATE, common.SUBJECT, common.KNOWLEDGE
SESSION_DIR, GRAPHICAL_DIR, EXPORT_DIR = common.SESSION_DIR, common.GRAPHICAL_DIR, common.EXPORT_DIR
CATALOG, SECTION_MANIFEST, LOCAL_BOOKS = common.CATALOG, common.SECTION_MANIFEST, common.LOCAL_BOOKS
TOPICS = [TOPIC_28]
PANEL_DATA = {str(config["key"]): config["panels"] for config in TOPICS}
SESSION_PLANS = {str(config["key"]): config["session_plans"] for config in TOPICS}
ASCII_PATH = common.ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs" / "environment-and-ecology-28-2026-09-03-sequential.json"


def self_check(config: dict[str, object], markdown: str, workbook: str, session_count: int, graphical_path: Path) -> None:
    common.self_check(config, markdown, workbook, session_count, graphical_path)


def main() -> int:
    return common.run_batch(topics=TOPICS, ascii_path=ASCII_PATH, scope="Environment and Ecology learner-v2 Topic 28", previous=previous_batch, previous_keys=["environment-and-ecology-27"])


if __name__ == "__main__":
    raise SystemExit(main())
