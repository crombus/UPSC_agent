"""Load the Ethics deep-review engine for dated sequential semantic review."""

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
REPORT_DATE = "2026-09-06"

CANONICAL_MARKERS = {
    1: ("ethics", "morality", "propriety", "constitutional morality"),
    2: ("family", "society", "education", "Gandhi", "Ambedkar"),
    3: ("cognitive", "affective", "behavioural", "persuasion", "coercion"),
    4: ("integrity", "impartiality", "non-partisanship", "objectivity", "compassion"),
    5: ("emotional intelligence", "Goleman", "Salovey", "empathy"),
    6: ("Kautilya", "Buddha", "Gandhi", "Ambedkar", "Vivekananda"),
    7: ("Socrates", "Aristotle", "Kant", "Mill", "Rawls"),
    8: ("deontology", "consequentialism", "virtue ethics", "care ethics", "justice"),
    9: ("public service", "conflict of interest", "discretion", "political neutrality"),
    10: ("law", "rules", "regulations", "conscience", "crisis of conscience"),
    11: ("accountability", "answerability", "CAG", "CVC", "social audit"),
    12: ("corporate governance", "stakeholder", "international ethics", "UNCAC"),
    13: ("artificial intelligence", "privacy", "environment", "precaution", "intergenerational"),
    14: ("probity", "public service", "propriety", "constitutional morality"),
    15: ("Right to Information", "Section 4", "Section 8", "Section 10", "Section 19", "Section 20"),
    16: ("code of ethics", "code of conduct", "CCS", "conflict of interest"),
    17: ("Citizens' Charter", "Sevottam", "CPGRAMS", "service delivery"),
    18: ("economy", "efficiency", "effectiveness", "equity", "corruption", "public funds"),
    19: ("Prevention of Corruption Act", "Section 7", "17A", "Section 19"),
    20: ("CVC", "CBI", "Lokpal", "Lokayukta"),
    21: ("vigilance", "PIDPI", "whistleblower", "honest officials"),
    22: (
        "stakeholder",
        "fact/value",
        "ethical issues",
        "options",
        "consequence",
        "duty",
        "virtue",
        "justice",
        "care",
        "public interest",
        "constitutional morality",
        "legality versus ethics",
        "short-term",
        "long-term",
        "vulnerable",
        "final choice",
        "preventive institutional reforms",
    ),
    23: ("Manjunath", "Dubey", "Mudgal", "MKSS", "Bhoomi", "ICAC", "Vishaka"),
}


def load_runtime() -> ModuleType:
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    module = importlib.import_module("regenerate_ethics_deep_review")
    module.DATE = REPORT_DATE

    def ensure_canonical_owner_control(topic: object) -> bool:
        basic = topic.basic_path.read_text(encoding="utf-8")
        advanced = topic.advanced_path.read_text(encoding="utf-8")
        missing = [
            marker
            for marker in CANONICAL_MARKERS[topic.number]
            if marker.casefold() not in basic.casefold()
        ]
        if missing:
            raise ValueError(
                f"{topic.topic_key}: canonical Basic owner lacks {missing}."
            )
        if len(basic) < 12000 or len(advanced) < 11000:
            raise ValueError(
                f"{topic.topic_key}: Basic/Advanced owners are not learner-ready."
            )
        if "PYQ" not in basic:
            raise ValueError(f"{topic.topic_key}: Basic owner lacks explicit PYQ routing.")
        if "Mains" not in basic and "answer" not in basic.casefold():
            raise ValueError(f"{topic.topic_key}: Basic owner lacks Mains architecture.")
        points = module.ETHICS_REVIEW_POINTS[topic.number]
        if len(points) != 3 or any(len(point) < 120 for point in points):
            raise ValueError(
                f"{topic.topic_key}: hostile Ethics semantic controls are incomplete."
            )
        return False

    module.ensure_canonical_owner_control = ensure_canonical_owner_control
    return module


def topic_slug(title: str, number: int) -> str:
    return f"{number:02d}-" + re.sub(
        r"[^a-z0-9]+", "-", title.casefold()
    ).strip("-")
