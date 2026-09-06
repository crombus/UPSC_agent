"""Load the proven Internal Security deep-review engine for semantic review."""

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
    module = importlib.import_module("regenerate_internal_security_deep_review")
    module.DATE = REPORT_DATE

    def ensure_canonical_owner_control(topic: object) -> bool:
        basic = topic.basic_path.read_text(encoding="utf-8")
        advanced = topic.advanced_path.read_text(encoding="utf-8")
        required_basic = (
            "## 1.",
            "Prelims",
            "Mains",
            "answer architecture",
            "current anchor",
            "PYQ",
        )
        missing = [
            term for term in required_basic
            if term.casefold() not in basic.casefold()
        ]
        if missing:
            raise ValueError(
                f"{topic.topic_key}: canonical Basic owner lacks {missing}."
            )
        if len(basic) < 18000 or len(advanced) < 12000:
            raise ValueError(
                f"{topic.topic_key}: canonical owners are not learner-ready."
            )
        points = module.INTERNAL_SECURITY_REVIEW_POINTS[topic.number]
        if len(points) != 3 or any(len(point) < 100 for point in points):
            raise ValueError(
                f"{topic.topic_key}: hostile semantic controls are incomplete."
            )
        return False

    module.ensure_canonical_owner_control = ensure_canonical_owner_control
    return module


def topic_slug(title: str, number: int) -> str:
    return (
        f"{number:02d}-"
        + re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-")
    )
