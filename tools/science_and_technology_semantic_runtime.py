"""Load the proven Science and Technology deep-review engine for semantic review."""

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
REPORT_DATE = "2026-09-06"


def load_runtime() -> ModuleType:
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    module = importlib.import_module(
        "regenerate_science_and_technology_deep_review"
    )
    module.DATE = REPORT_DATE

    def generation_sources(
        topic: object,
        record: dict[str, object],
    ) -> tuple[str, str]:
        workbook_value = record.get("workbook_markdown") or (
            record.get("provenance") or {}
        ).get("workbook_markdown")
        main = module.repo(record["markdown"]).read_text(encoding="utf-8")
        workbook = module.repo(workbook_value).read_text(encoding="utf-8")
        for old_date in ("2026-09-04", "2026-09-03"):
            main = main.replace(old_date, REPORT_DATE)
            workbook = workbook.replace(old_date, REPORT_DATE)
        return main, workbook

    module.generation_sources = generation_sources

    inherited_augment = module.augment_topic_semantic_content

    def augment_topic_semantic_content(
        topic: object,
        markdown: str,
        *,
        workbook: bool = False,
    ) -> str:
        text = markdown
        if workbook:
            return inherited_augment(topic, text, workbook=True)
        marker = "### SCIENCE AND TECHNOLOGY DEEP-REVIEW CORE CONTROL"
        if marker in text:
            return text
        return inherited_augment(topic, text, workbook=False)

    module.augment_topic_semantic_content = augment_topic_semantic_content

    def ensure_canonical_owner_control(topic: object) -> None:
        basic = topic.basic_path.read_text(encoding="utf-8")
        advanced = topic.advanced_path.read_text(encoding="utf-8")
        required_basic = ("## 1.", "Mechanism", "Prelims", "Answer")
        missing = [term for term in required_basic if term.casefold() not in basic.casefold()]
        if missing:
            raise ValueError(
                f"{topic.topic_key}: canonical Basic owner lacks {missing}."
            )
        if not any(
            term.casefold() in basic.casefold()
            for term in ("Mains", "GS-III", "GS Paper")
        ):
            raise ValueError(
                f"{topic.topic_key}: canonical Basic owner lacks a Mains/GS route."
            )
        if not any(
            term.casefold() in basic.casefold()
            for term in ("Current", "recent", "dated", "verified")
        ):
            raise ValueError(
                f"{topic.topic_key}: canonical Basic owner lacks currentness control."
            )
        if len(basic) < 8000 or len(advanced) < 2000:
            raise ValueError(
                f"{topic.topic_key}: canonical owners are not learner-ready."
            )
        points = module.SCIENCE_AND_TECHNOLOGY_REVIEW_POINTS[topic.number]
        if len(points) != 3 or any(len(point) < 100 for point in points):
            raise ValueError(
                f"{topic.topic_key}: hostile semantic controls are incomplete."
            )

    module.ensure_canonical_owner_control = ensure_canonical_owner_control
    return module


def topic_slug(title: str, number: int) -> str:
    return (
        f"{number:02d}-"
        + re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-")
    )
