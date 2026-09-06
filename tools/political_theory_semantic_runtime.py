"""Load Political Theory deep-review tooling for dated semantic review."""

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
    1: ("political theory", "political science", "political philosophy", "Easton", "Strauss"),
    2: ("ideology", "Marx", "Mannheim", "Popper", "end of ideology"),
    3: ("classical liberalism", "welfare liberalism", "neoliberalism", "Hayek", "Nozick"),
    4: ("historical materialism", "alienation", "base", "superstructure", "Gramsci"),
    5: ("socialism", "fascism", "anarchism", "Gandhism", "conservatism"),
    6: ("patriarchy", "sex", "gender", "Butler", "intersectionality"),
    7: ("political situation", "communitarianism", "MacIntyre", "Taylor", "Sandel"),
    8: ("behaviouralism", "post-behaviouralism", "Easton", "Almond", "Deutsch"),
    9: ("interdisciplinary", "history", "economics", "sociology", "psychology"),
    10: ("state", "government", "civil society", "nation", "internationalism"),
    11: ("sovereignty", "Austin", "Bodin", "Rousseau", "pluralism"),
    12: ("globalisation", "sovereignty", "interdependence", "transnational", "policy"),
    13: ("organic", "social contract", "Marxist", "pluralist", "feminist"),
    14: ("political obligation", "consent", "resistance", "civil disobedience", "rule of law"),
    15: ("power", "authority", "legitimacy", "hegemony", "Lukes"),
    16: ("citizenship", "Marshall", "civil rights", "political rights", "social rights"),
    17: ("human rights", "civil liberties", "democratic rights", "natural rights", "legal rights"),
    18: ("negative liberty", "positive liberty", "equality", "property", "non-domination"),
    19: ("justice", "procedural", "distributive", "recognition", "Rawls"),
    20: ("Rawls", "Nozick", "Marx", "Sen", "justice"),
    21: ("common good", "community", "communitarian", "public interest", "cooperative"),
    22: ("democracy", "representation", "delegate", "trustee", "deliberative"),
    23: ("democratisation", "social change", "development", "populism", "ecological"),
}


def load_runtime() -> ModuleType:
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    module = importlib.import_module("regenerate_political_theory_deep_review")
    module.DATE = REPORT_DATE
    module.generator.GENERATION_DATE = REPORT_DATE
    module.topics = lambda: [module.generator.TOPICS[number] for number in range(1, 24)]

    original_validate = module.validate_generated

    def validate_generated(*args: object, **kwargs: object) -> dict:
        payload = original_validate(*args, **kwargs)
        gates = payload["hard_gates"]
        gates["verified_pyq_metadata_and_key_discipline"] = gates[
            "verified_pyq_metadata_and_ownership"
        ]
        return payload

    module.validate_generated = validate_generated

    def ensure_canonical_owner_control(topic: object) -> bool:
        basic = topic.basic_path.read_text(encoding="utf-8")
        advanced = topic.advanced_path.read_text(encoding="utf-8")
        missing = [
            marker
            for marker in CANONICAL_MARKERS[topic.number]
            if marker.casefold() not in basic.casefold()
        ]
        if missing:
            raise ValueError(f"{topic.topic_key}: canonical Basic owner lacks {missing}.")
        if len(basic) < 20000 or len(advanced) < 10000:
            raise ValueError(
                f"{topic.topic_key}: Basic/Advanced owners are not learner-ready."
            )
        required = ("answer", "objection", "reply")
        absent = [item for item in required if item.casefold() not in basic.casefold()]
        if absent:
            raise ValueError(
                f"{topic.topic_key}: hostile semantic controls missing {absent}."
            )
        if not all(mark in basic for mark in ("10", "15", "20")):
            raise ValueError(f"{topic.topic_key}: mark-scaled answer architecture missing.")
        return False

    module.ensure_canonical_owner_control = ensure_canonical_owner_control

    def add_all_operation_generation_paths(
        rows: list[dict], changed: set[str]
    ) -> None:
        for row in rows:
            key = row["topic_key"]
            generation = int(row["new_generation"])
            topic = module.generator.TOPICS[int(key[-2:])]
            paths = module.review_paths(topic, generation)
            for name in ("knowledge_dir", "notes_dir", "flow_dir"):
                directory = paths[name]
                if directory.is_dir():
                    changed.update(module.rel(path) for path in directory.rglob("*") if path.is_file())
            for name in ("ascii_spec", "graphical_spec", "content_spec", "record", "validation"):
                path = paths[name]
                if path.is_file():
                    changed.add(module.rel(path))
            review_dir = module.REVIEW_ROOT / "reviews" / key
            if review_dir.is_dir():
                changed.update(
                    module.rel(path) for path in review_dir.rglob("*") if path.is_file()
                )

    module.add_all_operation_generation_paths = add_all_operation_generation_paths
    return module


def topic_slug(title: str, number: int) -> str:
    return f"{number:02d}-" + re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-")
