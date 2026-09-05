"""Build Internal Security learner-v2 Topic 04 in authoring-only mode."""

from pathlib import Path

import generate_internal_security_03_sequential as previous
import generate_internal_security_common as common
from internal_security_04_data import TOPIC_04


DATE, SUBJECT, KNOWLEDGE = common.DATE, common.SUBJECT, common.KNOWLEDGE
SESSION_DIR, GRAPHICAL_DIR, EXPORT_DIR = common.SESSION_DIR, common.GRAPHICAL_DIR, common.EXPORT_DIR
CATALOG, SECTION_MANIFEST, LOCAL_BOOKS = common.CATALOG, common.SECTION_MANIFEST, common.LOCAL_BOOKS
TOPICS = [TOPIC_04]
PANEL_DATA = {str(config["key"]): config["panels"] for config in TOPICS}
SESSION_PLANS = {str(config["key"]): config["session_plans"] for config in TOPICS}
ASCII_PATH = common.ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs" / "internal-security-04-2026-09-04-sequential.json"


def self_check(config: dict[str, object], markdown: str, workbook: str, session_count: int, graphical_path: Path) -> None:
    common.self_check(config, markdown, workbook, session_count, graphical_path)


def main() -> int:
    return common.run_batch(
        topics=TOPICS,
        ascii_path=ASCII_PATH,
        scope="Internal Security learner-v2 Topic 04",
        previous=previous,
        previous_keys=["internal-security-03"],
    )


if __name__ == "__main__":
    raise SystemExit(main())
