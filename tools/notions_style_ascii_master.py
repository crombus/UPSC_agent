"""Build and validate topic-specific, Notions-style multi-panel ASCII masters."""

from __future__ import annotations

import json
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

import polity_flowchart_case_years


PANEL_HEADING_RE = re.compile(
    r"^#### ASCII MASTER FLOW — PANEL (\d+)/(\d+): (.+?)\s*$",
    re.MULTILINE,
)
PANEL_BLOCK_RE = re.compile(
    r"^#### ASCII MASTER FLOW — PANEL (\d+)/(\d+): (.+?)\s*\n+"
    r"```ascii-master\s*\n(.*?)\n```\s*$",
    re.MULTILINE | re.DOTALL,
)
STANDALONE_PANEL_HEADING_RE = re.compile(
    r"^ASCII MASTER FLOW — PANEL (\d+)/(\d+): (.+?)\s*$",
    re.MULTILINE,
)
SESSION_RE = re.compile(
    r"(?im)^###\s+SESSION\s+(\d+)\s*[—-]\s*(.+?)\s*$"
)
MAX_LINE_WIDTH = 100
MANUAL_SPEC_FILENAMES = (
    "ancient-indian-history-2026-08-23.json",
    "ancient-indian-history-2026-08-29-sequential.json",
    "ancient-indian-history-17-21-2026-08-29-sequential.json",
    "ancient-indian-history-22-23-2026-08-30-sequential.json",
    "ancient-indian-history-24-25-2026-08-30-sequential.json",
    "ancient-indian-history-26-27-2026-08-30-sequential.json",
    "medieval-indian-history-01-02-2026-08-30-sequential.json",
    "medieval-indian-history-03-04-2026-08-30-sequential.json",
    "medieval-indian-history-05-06-2026-08-30-sequential.json",
    "medieval-indian-history-07-08-2026-08-30-sequential.json",
    "medieval-indian-history-09-10-2026-08-30-sequential.json",
    "medieval-indian-history-11-12-2026-08-30-sequential.json",
    "medieval-indian-history-13-14-2026-08-30-sequential.json",
    "medieval-indian-history-15-16-2026-08-30-sequential.json",
    "medieval-indian-history-17-18-2026-08-30-sequential.json",
    "medieval-indian-history-19-20-2026-08-30-sequential.json",
    "medieval-indian-history-21-22-2026-08-30-sequential.json",
    "medieval-indian-history-23-25-2026-08-30-sequential.json",
    "modern-indian-history-01-02-2026-08-30-sequential.json",
    "modern-indian-history-03-04-2026-08-30-sequential.json",
    "modern-indian-history-05-06-2026-08-30-sequential.json",
    "modern-indian-history-07-08-2026-08-30-sequential.json",
    "modern-indian-history-09-13-2026-08-30-sequential.json",
    "modern-indian-history-14-15-2026-08-31-sequential.json",
    "modern-indian-history-16-17-2026-08-31-sequential.json",
    "modern-indian-history-18-19-2026-08-31-sequential.json",
    "modern-indian-history-20-21-2026-08-31-sequential.json",
    "modern-indian-history-22-23-2026-08-31-sequential.json",
    "modern-indian-history-24-25-2026-08-31-sequential.json",
    "modern-indian-history-26-27-2026-08-31-sequential.json",
    "modern-indian-history-28-29-2026-08-31-sequential.json",
    "modern-indian-history-30-31-2026-08-31-sequential.json",
    "modern-indian-history-32-33-2026-08-31-sequential.json",
    "modern-indian-history-34-35-2026-08-31-sequential.json",
    "modern-indian-history-36-37-2026-08-31-sequential.json",
    "modern-indian-history-38-2026-08-31-sequential.json",
    "world-history-01-02-2026-09-01-sequential.json",
    "world-history-03-04-2026-09-01-sequential.json",
    "world-history-05-2026-09-01-sequential.json",
    "world-history-06-07-2026-09-01-sequential.json",
    "world-history-08-09-2026-09-01-sequential.json",
    "world-history-10-2026-09-01-sequential.json",
    "world-history-11-12-2026-09-01-sequential.json",
    "world-history-13-14-2026-09-01-sequential.json",
    "world-history-15-2026-09-01-sequential.json",
    "world-history-16-17-2026-09-01-sequential.json",
    "world-history-18-2026-09-01-sequential.json",
    "world-history-19-20-2026-09-01-sequential.json",
    "world-history-21-2026-09-01-sequential.json",
    "indian-art-and-culture-01-02-2026-09-01-sequential.json",
    "indian-art-and-culture-03-04-2026-09-01-sequential.json",
    "indian-art-and-culture-05-2026-09-01-sequential.json",
    "indian-art-and-culture-06-07-2026-09-01-sequential.json",
    "indian-art-and-culture-08-09-2026-09-01-sequential.json",
    "indian-art-and-culture-10-2026-09-01-sequential.json",
    "indian-art-and-culture-11-12-2026-09-01-sequential.json",
    "indian-art-and-culture-13-14-2026-09-01-sequential.json",
    "indian-art-and-culture-15-2026-09-01-sequential.json",
    "geography-05-06-2026-09-01-sequential.json",
    "geography-07-08-2026-09-01-sequential.json",
    "geography-09-2026-09-01-sequential.json",
    "geography-10-11-2026-09-01-sequential.json",
    "geography-12-13-2026-09-01-sequential.json",
    "geography-14-2026-09-01-sequential.json",
    "geography-15-16-2026-09-01-sequential.json",
    "geography-17-18-2026-09-01-sequential.json",
    "geography-19-2026-09-01-sequential.json",
    "geography-20-2026-09-01-sequential.json",
    "geography-21-2026-09-01-sequential.json",
    "geography-22-2026-09-01-sequential.json",
    "geography-23-2026-09-01-sequential.json",
    "geography-24-2026-09-01-sequential.json",
    "geography-25-2026-09-01-sequential.json",
    "geography-26-2026-09-01-sequential-g3.json",
    "geography-27-2026-09-01-sequential-g3.json",
    "geography-29-2026-09-01-sequential-g3.json",
    "geography-31-2026-09-01-sequential.json",
    "geography-33-2026-09-01-sequential.json",
    "geography-34-2026-09-01-sequential.json",
    "geography-35-2026-09-01-sequential.json",
    "geography-36-2026-09-01-sequential.json",
    "geography-37-2026-09-01-sequential.json",
    "indian-society-01-2026-09-02-sequential.json",
    "indian-society-02-2026-09-02-sequential.json",
    "indian-society-03-2026-09-02-sequential.json",
    "indian-society-04-2026-09-02-sequential.json",
    "indian-society-05-2026-09-02-sequential.json",
    "indian-society-06-2026-09-02-sequential.json",
    "indian-society-07-2026-09-02-sequential.json",
    "indian-society-08-2026-09-02-sequential.json",
    "indian-society-09-2026-09-02-sequential.json",
    "indian-society-10-2026-09-02-sequential.json",
    "indian-society-11-2026-09-02-sequential.json",
    "indian-society-12-2026-09-02-sequential.json",
    "indian-society-13-2026-09-02-sequential.json",
    "indian-society-14-2026-09-02-sequential.json",
    "indian-society-15-2026-09-02-sequential.json",
    "governance-01-2026-09-02-sequential.json",
    "governance-02-2026-09-02-sequential.json",
    "governance-03-2026-09-02-sequential.json",
    "governance-04-2026-09-02-sequential.json",
    "governance-05-2026-09-02-sequential.json",
    "governance-06-2026-09-02-sequential.json",
    "governance-07-2026-09-02-sequential.json",
    "governance-08-2026-09-02-sequential.json",
    "governance-09-2026-09-02-sequential.json",
    "governance-10-2026-09-02-sequential.json",
    "governance-11-2026-09-02-sequential.json",
    "governance-12-2026-09-02-sequential.json",
    "governance-13-2026-09-02-sequential.json",
    "governance-14-2026-09-02-sequential.json",
    "governance-15-2026-09-02-sequential.json",
    "governance-16-2026-09-02-sequential.json",
    "social-justice-01-2026-09-02-sequential.json",
    "social-justice-02-2026-09-02-sequential.json",
    "social-justice-03-2026-09-02-sequential.json",
    "social-justice-04-2026-09-02-sequential.json",
    "social-justice-05-2026-09-02-sequential.json",
    "social-justice-06-2026-09-02-sequential.json",
    "social-justice-07-2026-09-02-sequential.json",
    "social-justice-08-2026-09-02-sequential.json",
    "social-justice-09-2026-09-02-sequential.json",
    "social-justice-10-2026-09-02-sequential.json",
    "social-justice-11-2026-09-02-sequential.json",
    "social-justice-12-2026-09-02-sequential.json",
    "social-justice-13-2026-09-02-sequential.json",
    "social-justice-14-2026-09-02-sequential.json",
    "social-justice-15-2026-09-02-sequential.json",
    "social-justice-16-2026-09-02-sequential.json",
    "social-justice-17-2026-09-02-sequential.json",
    "international-relations-01-2026-09-03-sequential.json",
    "international-relations-02-2026-09-03-sequential.json",
    "international-relations-03-2026-09-03-sequential.json",
    "international-relations-04-2026-09-03-sequential.json",
    "international-relations-05-2026-09-03-sequential.json",
    "international-relations-06-2026-09-03-sequential.json",
    "international-relations-07-2026-09-03-sequential.json",
    "international-relations-08-2026-09-03-sequential.json",
    "international-relations-09-2026-09-03-sequential.json",
    "international-relations-10-2026-09-03-sequential.json",
    "international-relations-11-2026-09-03-sequential.json",
    "international-relations-12-2026-09-03-sequential.json",
    "economy-01-2026-09-03-sequential.json",
    "economy-02-2026-09-03-sequential.json",
    "economy-03-2026-09-03-sequential.json",
    "economy-04-2026-09-03-sequential.json",
    "economy-05-2026-09-03-sequential.json",
    "economy-06-2026-09-03-sequential.json",
    "economy-07-2026-09-03-sequential.json",
    "economy-08-2026-09-03-sequential.json",
    "economy-09-2026-09-03-sequential.json",
    "economy-10-2026-09-03-sequential.json",
    "economy-11-2026-09-03-sequential.json",
    "economy-12-2026-09-03-sequential.json",
    "economy-13-2026-09-03-sequential.json",
    "economy-14-2026-09-03-sequential.json",
    "economy-15-2026-09-03-sequential.json",
    "economy-16-2026-09-03-sequential.json",
    "economy-17-2026-09-03-sequential.json",
    "economy-18-2026-09-03-sequential.json",
    "economy-19-2026-09-03-sequential.json",
    "economy-20-2026-09-03-sequential.json",
    "economy-21-2026-09-03-sequential.json",
    "economy-22-2026-09-03-sequential.json",
    "economy-23-2026-09-03-sequential.json",
    "economy-24-2026-09-03-sequential.json",
    "economy-25-2026-09-03-sequential.json",
    "economy-26-2026-09-03-sequential.json",
    "economy-27-2026-09-03-sequential.json",
    "economy-28-2026-09-03-sequential.json",
    "economy-29-2026-09-03-sequential.json",
    "economy-30-2026-09-03-sequential.json",
    "economy-31-2026-09-03-sequential.json",
    "environment-and-ecology-01-2026-09-03-sequential.json",
    "environment-and-ecology-02-2026-09-03-sequential.json",
    "environment-and-ecology-03-2026-09-03-sequential.json",
    "environment-and-ecology-04-2026-09-03-sequential.json",
    "environment-and-ecology-05-2026-09-03-sequential.json",
    "environment-and-ecology-06-2026-09-03-sequential.json",
    "environment-and-ecology-07-2026-09-03-sequential.json",
    "environment-and-ecology-08-2026-09-03-sequential.json",
    "environment-and-ecology-09-2026-09-03-sequential.json",
    "environment-and-ecology-10-2026-09-03-sequential.json",
    "environment-and-ecology-11-2026-09-03-sequential.json",
    "environment-and-ecology-12-2026-09-03-sequential.json",
    "environment-and-ecology-13-2026-09-03-sequential.json",
    "environment-and-ecology-14-2026-09-03-sequential.json",
    "environment-and-ecology-15-2026-09-03-sequential.json",
    "environment-and-ecology-16-2026-09-03-sequential.json",
    "environment-and-ecology-17-2026-09-03-sequential.json",
    "environment-and-ecology-18-2026-09-03-sequential.json",
    "environment-and-ecology-19-2026-09-03-sequential.json",
    "environment-and-ecology-20-2026-09-03-sequential.json",
    "environment-and-ecology-21-2026-09-03-sequential.json",
    "environment-and-ecology-22-2026-09-03-sequential.json",
    "environment-and-ecology-23-2026-09-03-sequential.json",
    "environment-and-ecology-24-2026-09-03-sequential.json",
    "environment-and-ecology-25-2026-09-03-sequential.json",
    "environment-and-ecology-26-2026-09-03-sequential.json",
    "environment-and-ecology-27-2026-09-03-sequential.json",
    "environment-and-ecology-28-2026-09-03-sequential.json",
    "science-and-technology-01-2026-09-03-sequential.json",
    "science-and-technology-02-2026-09-03-sequential.json",
    "science-and-technology-03-2026-09-03-sequential.json",
    "science-and-technology-04-2026-09-03-sequential.json",
    "science-and-technology-05-2026-09-03-sequential.json",
    "science-and-technology-06-2026-09-03-sequential.json",
    "science-and-technology-07-2026-09-03-sequential.json",
    "science-and-technology-08-2026-09-03-sequential.json",
    "science-and-technology-09-2026-09-03-sequential.json",
    "science-and-technology-10-2026-09-03-sequential.json",
    "science-and-technology-11-2026-09-04-sequential.json",
    "science-and-technology-12-2026-09-04-sequential.json",
    "science-and-technology-13-2026-09-04-sequential.json",
    "science-and-technology-14-2026-09-04-sequential.json",
    "science-and-technology-15-2026-09-04-sequential.json",
    "science-and-technology-16-2026-09-04-sequential.json",
    "science-and-technology-17-2026-09-04-sequential.json",
    "science-and-technology-18-2026-09-04-sequential.json",
    "science-and-technology-19-2026-09-04-sequential.json",
    "science-and-technology-20-2026-09-04-sequential.json",
    "science-and-technology-21-2026-09-04-sequential.json",
    "science-and-technology-22-2026-09-04-sequential.json",
    "science-and-technology-23-2026-09-04-sequential.json",
    "science-and-technology-24-2026-09-04-sequential.json",
    "science-and-technology-25-2026-09-04-sequential.json",
    "science-and-technology-26-2026-09-04-sequential.json",
    "internal-security-01-2026-09-04-sequential.json",
    "internal-security-02-2026-09-04-sequential.json",
    "internal-security-03-2026-09-04-sequential.json",
    "internal-security-04-2026-09-04-sequential.json",
    "internal-security-05-2026-09-04-sequential.json",
    "internal-security-06-2026-09-04-sequential.json",
    "internal-security-07-2026-09-04-sequential.json",
    "internal-security-08-2026-09-04-sequential.json",
    "internal-security-09-2026-09-04-sequential.json",
    "internal-security-10-2026-09-04-sequential.json",
    "internal-security-11-2026-09-04-sequential.json",
    "internal-security-12-2026-09-04-sequential.json",
    "disaster-management-01-2026-09-04-sequential.json",
    "disaster-management-02-2026-09-04-sequential.json",
    "disaster-management-03-2026-09-04-sequential.json",
    "disaster-management-04-2026-09-04-sequential.json",
    "disaster-management-05-2026-09-04-sequential.json",
    "disaster-management-06-2026-09-04-sequential.json",
    "disaster-management-07-2026-09-04-sequential.json",
    "disaster-management-08-2026-09-04-sequential.json",
    "disaster-management-09-2026-09-04-sequential.json",
    "disaster-management-10-2026-09-04-sequential.json",
    "disaster-management-11-2026-09-04-sequential.json",
    "disaster-management-12-2026-09-04-sequential.json",
    "disaster-management-13-2026-09-04-sequential.json",
    "disaster-management-14-2026-09-04-sequential.json",
    "disaster-management-15-2026-09-04-sequential.json",
    "disaster-management-16-2026-09-04-sequential.json",
    "disaster-management-17-2026-09-04-sequential.json",
    "disaster-management-18-2026-09-04-sequential.json",
    "essay-01-2026-09-04-sequential.json",
    "essay-02-2026-09-04-sequential.json",
    "essay-03-2026-09-04-sequential.json",
    "essay-04-2026-09-04-sequential.json",
    "geography-2026-08-23.json",
    "philosophy-2026-08-23.json",
    "polity-2026-08-23.json",
    "polity-2026-08-24-sequential-batch.json",
    "polity-13-2026-08-24-sequential.json",
    "polity-14-2026-08-24-sequential.json",
    "polity-15-2026-08-24-sequential.json",
    "polity-16-2026-08-24-sequential.json",
    "polity-17-2026-08-24-sequential.json",
)
EDITORIAL_RE = re.compile(
    r"\b(?:mains angle|study link|mains/pyq use|one-line memory|memory hook|"
    r"source audit|ownership audit|owner-topic|repository advanced owner|"
    r"ownership transfer|primary ownership|priority:\s*primary|"
    r"verification and answer protocol|verified-question protocol|"
    r"content classification|progress and pacing|book context|ca search|ca found|"
    r"simple explanation|india-centric example|exam link|why this matters for upsc|"
    r"core argument/criticism|final verdict|major reply|doctrine statement|"
    r"canonical example|named evidence/example|"
    r"answer-grabbing line|write/adapt in the exam|"
    r"classification:\s*(?:core|supporting|optional))\b",
    re.I,
)
PREFIX_RE = re.compile(
    r"^(?:\[(?:THESIS|REPLY|QUALIFICATION|FACT|ANALYSIS|INFERENCE|CURRENT)]\s*|"
    r"(?:final verdict|high-value transition|answer-grabbing line|"
    r"memory hook|mains angle|study link|core argument/criticism|"
    r"statement|argument|reply|distinction|assessment|example|qualification|"
    r"mains route|answer route|exam payoff|"
    r"correct|why this section exists|the operative mechanism is that)\s*[.:]\s*)+",
    re.I,
)
GENERIC_ONLY_RE = re.compile(
    r"^(?:argument|statement|reply|distinction|assessment|example|answer-use|"
    r"thesis|formation|method|discovery|analysis|consequence|mechanism|"
    r"read the structure first|jaina reply|why this matters for upsc|"
    r"not|this|recent|nodes?|angle|hook|ai|c)$",
    re.I,
)


@dataclass(frozen=True)
class ManualPanel:
    title: str
    body: str
    structural_type: str
    source_references: object


@dataclass(frozen=True)
class ManualTopicSpec:
    topic_key: str
    title: str
    panels: tuple[ManualPanel, ...]
    source_path: Path
    source_markdown: str
    source_record: str
    approved_reference: str
    benchmark_preservation: str


def _manual_panel_body(panel: dict[str, Any]) -> str:
    available = [
        key
        for key in ("ascii_text", "full_text", "lines", "ascii_lines")
        if key in panel
    ]
    if len(available) != 1:
        raise ValueError(
            "Manual ASCII panel must contain exactly one authored body field; "
            f"found {available}."
        )
    value = panel[available[0]]
    if isinstance(value, str):
        body = value.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    elif isinstance(value, list) and all(isinstance(line, str) for line in value):
        if any("\n" in line or "\r" in line for line in value):
            raise ValueError("Manual ASCII line arrays must contain one line per item.")
        body = "\n".join(value)
    else:
        raise ValueError("Manual ASCII panel body must be a string or string array.")
    if not body:
        raise ValueError("Manual ASCII panel body cannot be empty.")
    return body


def _manual_panel_references(panel: dict[str, Any]) -> object:
    for key in ("source_references", "source_session_heading_references"):
        if key in panel:
            return panel[key]
    raise ValueError("Manual ASCII panel lacks source references.")


def normalize_manual_spec_file(path: Path) -> dict[str, ManualTopicSpec]:
    """Normalize the four authored schemas without rewriting panel content."""
    data = json.loads(path.read_text(encoding="utf-8"))
    raw_topics = data.get("topics")
    if isinstance(raw_topics, dict):
        topic_items = list(raw_topics.items())
    elif isinstance(raw_topics, list):
        topic_items = [
            (str(topic.get("topic_key") or ""), topic)
            for topic in raw_topics
            if isinstance(topic, dict)
        ]
        if len(topic_items) != len(raw_topics):
            raise ValueError(f"{path.name}: every topic must be an object.")
    else:
        raise ValueError(f"{path.name}: topics must be an object or array.")

    normalized: dict[str, ManualTopicSpec] = {}
    for mapping_key, raw_topic in topic_items:
        if not isinstance(raw_topic, dict):
            raise ValueError(f"{path.name}: topic {mapping_key!r} must be an object.")
        topic_key = str(raw_topic.get("topic_key") or mapping_key)
        if not topic_key:
            raise ValueError(f"{path.name}: topic_key is required.")
        if topic_key in normalized:
            raise ValueError(f"{path.name}: duplicate topic_key {topic_key}.")
        title = raw_topic.get("title", raw_topic.get("display_title"))
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"{topic_key}: manual topic title is required.")
        raw_panels = raw_topic.get("panels")
        if not isinstance(raw_panels, list) or not raw_panels:
            raise ValueError(f"{topic_key}: manual panels must be a non-empty array.")
        panels: list[ManualPanel] = []
        for number, raw_panel in enumerate(raw_panels, 1):
            if not isinstance(raw_panel, dict):
                raise ValueError(f"{topic_key}: panel {number} must be an object.")
            panel_title = raw_panel.get("title", raw_panel.get("panel_title"))
            if not isinstance(panel_title, str) or not panel_title.strip():
                raise ValueError(f"{topic_key}: panel {number} title is required.")
            if panel_title != panel_title.strip():
                raise ValueError(
                    f"{topic_key}: panel {number} title has outer whitespace."
                )
            panels.append(
                ManualPanel(
                    title=panel_title,
                    body=_manual_panel_body(raw_panel),
                    structural_type=str(raw_panel.get("structural_type") or ""),
                    source_references=_manual_panel_references(raw_panel),
                )
            )
        declared = raw_topic.get("panel_count")
        if declared is not None and int(declared) != len(panels):
            raise ValueError(
                f"{topic_key}: declared panel_count {declared} != {len(panels)}."
            )
        normalized[topic_key] = ManualTopicSpec(
            topic_key=topic_key,
            title=title,
            panels=tuple(panels),
            source_path=path,
            source_markdown=str(
                raw_topic.get("source_markdown")
                or raw_topic.get("source_session")
                or ""
            ),
            source_record=str(raw_topic.get("source_record") or ""),
            approved_reference=str(
                raw_topic.get("approved_master_reference") or ""
            ),
            benchmark_preservation=str(
                raw_topic.get("benchmark_preservation") or ""
            ),
        )
    return normalized


def load_manual_topic_specs(spec_dir: Path) -> dict[str, ManualTopicSpec]:
    topics: dict[str, ManualTopicSpec] = {}
    required_paths = [spec_dir / filename for filename in MANUAL_SPEC_FILENAMES]
    required_names = {path.name.casefold() for path in required_paths}
    optional_paths = [
        path
        for path in sorted(spec_dir.glob("polity-*-sequential.json"))
        if path.name.casefold() not in required_names
    ]
    for path in [*required_paths, *optional_paths]:
        if not path.is_file():
            raise ValueError(f"Required manual ASCII spec is missing: {path}")
        for topic_key, spec in normalize_manual_spec_file(path).items():
            if topic_key in topics:
                raise ValueError(f"Duplicate manual ASCII topic: {topic_key}")
            topics[topic_key] = spec
    return topics


def manual_spec_integrity_errors(
    root: Path,
    specs: dict[str, ManualTopicSpec],
) -> list[str]:
    errors: list[str] = []
    for topic_key, spec in specs.items():
        if spec.approved_reference:
            approved_reference = root / Path(
                spec.approved_reference.replace("\\", "/")
            )
            if not approved_reference.is_file():
                errors.append(
                    f"{topic_key}: approved reference is missing: "
                    f"{spec.approved_reference}."
                )
        if len(spec.panels) < 1:
            errors.append(f"{topic_key}: manual spec has no panels.")
            continue
        if len({panel.title.casefold() for panel in spec.panels}) != len(spec.panels):
            errors.append(f"{topic_key}: manual panel titles are not unique.")
        source_path = (
            root / Path(spec.source_markdown.replace("\\", "/"))
            if spec.source_markdown
            else None
        )
        if source_path is None or not source_path.is_file():
            errors.append(
                f"{topic_key}: manual spec source Markdown is missing: "
                f"{spec.source_markdown or '<none>'}."
            )
            source_text = ""
        else:
            source_text = source_path.read_text(encoding="utf-8")
        for number, panel in enumerate(spec.panels, 1):
            refs = panel.source_references
            populated = bool(refs)
            if isinstance(refs, (list, tuple)):
                populated = bool(refs) and all(
                    isinstance(item, (str, int)) and str(item).strip()
                    for item in refs
                )
            elif isinstance(refs, dict):
                populated = bool(refs) and any(bool(value) for value in refs.values())
            if not populated:
                errors.append(
                    f"{topic_key}: panel {number} has empty source references."
                )
            for line_number, line in enumerate(panel.body.splitlines(), 1):
                if len(line) > MAX_LINE_WIDTH:
                    errors.append(
                        f"{topic_key}: panel {number} line {line_number} exceeds "
                        f"{MAX_LINE_WIDTH} characters."
                    )
            if source_text and isinstance(refs, dict):
                sessions = refs.get("sessions", [])
                if isinstance(sessions, list):
                    for session in sessions:
                        if isinstance(session, int) and not re.search(
                            rf"(?im)^###\s+SESSION\s+{session}\b",
                            source_text,
                        ):
                            errors.append(
                                f"{topic_key}: panel {number} references missing "
                                f"SESSION {session}."
                            )
                line_ranges = refs.get("markdown_lines", [])
                line_count = len(source_text.splitlines())
                if isinstance(line_ranges, list):
                    for line_range in line_ranges:
                        match = re.fullmatch(r"(\d+)-(\d+)", str(line_range))
                        if (
                            not match
                            or int(match.group(1)) < 1
                            or int(match.group(2)) < int(match.group(1))
                            or int(match.group(2)) > line_count
                        ):
                            errors.append(
                                f"{topic_key}: panel {number} has invalid source "
                                f"line range {line_range!r}."
                            )
            if source_text and isinstance(refs, (list, tuple)):
                for reference in refs:
                    if not isinstance(reference, str):
                        continue
                    if "#" in reference and ("\\" in reference or "/" in reference):
                        raw_path, anchor = reference.split("#", 1)
                        referenced = root / Path(raw_path.replace("\\", "/"))
                        if not referenced.is_file():
                            errors.append(
                                f"{topic_key}: panel {number} references missing "
                                f"file {raw_path}."
                            )
                        elif anchor and anchor not in referenced.read_text(
                            encoding="utf-8"
                        ):
                            errors.append(
                                f"{topic_key}: panel {number} references missing "
                                f"anchor {anchor!r}."
                            )
        if topic_key.startswith("polity-"):
            case_text = "\n".join(
                f"{panel.title}\n{panel.body}" for panel in spec.panels
            )
            errors.extend(
                polity_flowchart_case_years.ascii_topic_errors(
                    topic_key,
                    case_text,
                )
            )
    return errors


def build_manual_fragment(spec: ManualTopicSpec) -> str:
    total = len(spec.panels)
    chunks: list[str] = []
    for number, panel in enumerate(spec.panels, 1):
        chunks.extend(
            [
                f"#### ASCII MASTER FLOW — PANEL {number}/{total}: {panel.title}",
                "",
                "```ascii-master",
                panel.body,
                "```",
                "",
            ]
        )
    return "\n".join(chunks).rstrip()


def clean(value: str) -> str:
    value = re.sub(r"!\[[^\]]*]\([^)]+\)", " ", value)
    value = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", value)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"[*_`#>|✅⚠️🔑]", " ", value)
    value = value.replace("→", " -> ")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -:;,.")


def source_clean(value: str, fallback: str = "") -> str:
    value = clean(value)
    value = PREFIX_RE.sub("", value).strip()
    value = re.sub(
        r"\s*[—-]\s*\[(?:CORE|SUPPORTING|OPTIONAL)[^\]]*(?:]|\Z)",
        "",
        value,
        flags=re.I,
    )
    value = re.sub(
        r"^(?:do not miss this limiting distinction|caution)\s*:\s*|"
        r"^(?:the resulting consequence is that|"
        r"the operative mechanism is that|technically,)\s*",
        "",
        value,
        flags=re.I,
    )
    if (
        not value
        or GENERIC_ONLY_RE.fullmatch(value)
        or EDITORIAL_RE.search(value)
        or re.search(r"\bis analysed by relating\b", value, re.I)
        or re.search(r"\bthen testing the relationship through\b", value, re.I)
    ):
        value = clean(fallback)
    return value


def short(value: str, width: int = 68) -> str:
    value = source_clean(value)
    sentences = re.split(r"(?<=[.;!?])\s+", value)
    value = next(
        (
            cleaned
            for sentence in sentences
            if (cleaned := source_clean(sentence))
        ),
        "",
    )
    if len(value) <= width:
        return value
    clipped = value[: width].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return (clipped or value[: width - 1]).rstrip() + "…"


def display_short(value: str, width: int = 68) -> str:
    value = clean(value)
    suffix_match = re.search(
        r":\s*((?:central question|traps|map traps|close-option traps|"
        r"examiner traps|integrated revision).*)$",
        value,
        re.I,
    )
    if suffix_match and len(value) > width:
        suffix = suffix_match.group(1)
        prefix = value[: suffix_match.start()].rstrip(" :")
        available = max(18, width - len(suffix) - 3)
        return f"{display_short(prefix, available)}: {suffix}"
    if len(value) <= width:
        return value
    clipped = value[: width].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return (clipped or value[: width - 1]).rstrip() + "…"


def wrapped(value: str, width: int = 76, prefix: str = "") -> list[str]:
    content = short(value, max(width * 3, width))
    return [
        prefix + line
        for line in textwrap.wrap(
            content,
            width=max(12, width - len(prefix)),
            break_long_words=False,
            break_on_hyphens=False,
        )
    ] or [prefix]


def session_sections(markdown: str) -> dict[int, str]:
    basic_match = re.search(
        r"(?ims)^##\s+BASIC LEARNING SESSION\s*(.*?)"
        r"(?=^##\s+BASIC MCQS / REMEDIATION)",
        markdown,
    )
    basic = basic_match.group(1) if basic_match else markdown
    headings = list(SESSION_RE.finditer(basic))
    return {
        int(match.group(1)): basic[
            match.end() : headings[index + 1].start()
            if index + 1 < len(headings)
            else len(basic)
        ]
        for index, match in enumerate(headings)
    }


def session_keywords(markdown: str) -> dict[int, list[str]]:
    result: dict[int, list[str]] = {}
    for number, body in session_sections(markdown).items():
        match = re.search(
            r"(?ims)^####\s+MUST-WRITE KEYWORDS\s*(.*?)"
            r"(?=^####\s+|\Z)",
            body,
        )
        candidates: list[str] = []
        if match:
            for line in match.group(1).splitlines():
                bullet = re.match(r"^\s*[-*]\s+(.+?)\s*$", line)
                if bullet:
                    value = source_clean(bullet.group(1))
                    if (
                        value
                        and not EDITORIAL_RE.search(value)
                        and len(value.split()) <= 10
                        and value.casefold() not in {
                        item.casefold() for item in candidates
                        }
                    ):
                        candidates.append(value)
        result[number] = candidates[:6]
    return result


def session_facts(markdown: str) -> dict[int, list[str]]:
    """Extract concise substantive sentences outside generated flow/code blocks."""
    result: dict[int, list[str]] = {}
    for number, body in session_sections(markdown).items():
        candidates: list[str] = []
        loose: list[str] = []
        in_fence = False
        for raw in body.splitlines():
            stripped = raw.strip()
            if stripped.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or not stripped:
                continue
            if stripped.startswith(("#", "![", "|---", "<!--")):
                continue
            if re.match(r"^\|?\s*[-:]{3,}", stripped):
                continue
            value = source_clean(
                re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", stripped)
            )
            value = re.sub(
                r"^(?:Plain-language definition|Technical definition|"
                r"How to use them)\s*:\s*",
                "",
                value,
                flags=re.I,
            ).strip()
            if not value or GENERIC_ONLY_RE.fullmatch(value) or EDITORIAL_RE.search(value):
                continue
            if 4 <= len(value.split()) < 7:
                loose.append(short(value, 120))
                continue
            if len(value.split()) < 7 or len(value) > 260:
                continue
            value = short(value, 120)
            if value.casefold() not in {item.casefold() for item in candidates}:
                candidates.append(value)
            if len(candidates) >= 8:
                break
        if len(candidates) < 3:
            for value in loose:
                if value.casefold() not in {item.casefold() for item in candidates}:
                    candidates.append(value)
                if len(candidates) >= 5:
                    break
        result[number] = candidates
    return result


def practice_themes(markdown: str) -> list[str]:
    match = re.search(
        r"(?ims)^##\s+PYQS AND ANSWER PRACTICE\s*(.*?)"
        r"(?=^##\s+OPTIONAL ADVANCED DEPTH)",
        markdown,
    )
    if not match:
        return []
    themes: list[str] = []
    for line in match.group(1).splitlines():
        stripped = clean(line)
        if (
            18 <= len(stripped) <= 180
            and (
                line.lstrip().startswith(("###", "####"))
                or re.search(
                    r"\b(?:discuss|examine|analyse|evaluate|comment|compare|"
                    r"critically|explain|question|pyq)\b",
                    stripped,
                    re.I,
                )
            )
            and not EDITORIAL_RE.search(stripped)
            and stripped.casefold()
            not in {item.casefold() for item in themes}
            and stripped.casefold() not in {
                "verified question",
                "verified pyq",
                "pyq",
                "question",
            }
            and not re.search(
                r"\b(?:complete solutions|independent practice models)\b",
                stripped,
                re.I,
            )
        ):
            themes.append(short(stripped, 76))
    return themes[:5]


def _card_value(card: Any, field: str, fallback: str = "") -> str:
    value = source_clean(str(getattr(card, field, fallback) or fallback), fallback)
    return short(value)


def card_records(cards: Sequence[Any], markdown: str) -> list[dict[str, Any]]:
    keywords = session_keywords(markdown)
    facts = session_facts(markdown)
    records: list[dict[str, Any]] = []
    for number, card in enumerate(cards, 1):
        title = source_clean(str(getattr(card, "title", "")), f"Session {number}")
        title = short(title, 72)
        found = list(keywords.get(number, []))
        evidence = list(facts.get(number, []))
        keyword_fallback = (
            found[0]
            if found
            else evidence[0]
            if evidence
            else title
        )
        raw_terms = _card_value(card, "terms", "")
        terms = raw_terms or (evidence[0] if evidence else keyword_fallback)
        if not found:
            found = [
                item
                for item in (
                    short(title, 36),
                    short(terms, 42),
                )
                if item
            ]
        records.append(
            {
                "number": number,
                "title": title,
                "terms": terms,
                "mechanism": _card_value(card, "mechanism", "")
                or (evidence[1] if len(evidence) > 1 else terms),
                "consequence": _card_value(card, "consequence", "")
                or (evidence[2] if len(evidence) > 2 else terms),
                "trap": _card_value(card, "trap", "")
                or next(
                    (
                        item
                        for item in evidence
                        if re.search(
                            r"\b(?:not|avoid|distinguish|limit|"
                            r"however|but|rather than)\b",
                            item,
                            re.I,
                        )
                    ),
                    evidence[-1] if evidence else terms,
                ),
                "answer": _card_value(card, "answer", "")
                or (evidence[0] if evidence else terms),
                "keywords": found[:6],
            }
        )
    return records


def _partition(numbers: list[int], groups: int = 5) -> list[list[int]]:
    if not numbers:
        return [[] for _ in range(groups)]
    result: list[list[int]] = []
    for index in range(groups):
        start = round(index * len(numbers) / groups)
        end = round((index + 1) * len(numbers) / groups)
        group = numbers[start:end]
        if not group:
            group = [numbers[min(start, len(numbers) - 1)]]
        result.append(group)
    return result


def _focus(records: list[dict[str, Any]], numbers: Iterable[int]) -> str:
    selected = [
        records[number - 1]["title"]
        for number in numbers
        if 1 <= number <= len(records)
    ]
    if not selected:
        return "core concepts"
    if len(selected) == 1:
        return short(selected[0], 54)
    return short(f"{selected[0]} to {selected[-1]}", 66)


def auto_design(
    *,
    topic_key: str,
    title: str,
    subject: str,
    cards: Sequence[Any],
    markdown: str,
) -> dict[str, Any]:
    records = card_records(cards, markdown)
    numbers = list(range(1, len(records) + 1))
    groups = _partition(numbers)
    sample = sorted(
        {
            1,
            max(1, len(numbers) // 3),
            max(1, (2 * len(numbers)) // 3),
        }
    )
    subject_key = subject.casefold()
    if "history" in subject_key:
        types = (
            "root-axes",
            "chronology",
            "causal-system",
            "institution-society-map",
            "comparison",
            "evidence-debate",
            "application-pyq",
            "answer-spine",
        )
        labels = (
            f"{title}: scope, evidence and central historical questions",
            f"Chronological spine: {_focus(records, groups[0])}",
            f"Causation and transition: {_focus(records, groups[1])}",
            f"Institutions, society, economy and culture: {_focus(records, groups[2])}",
            f"Comparative map: {_focus(records, groups[3])}",
            f"Evidence, debates, limits and legacy: {_focus(records, groups[4])}",
            f"{title}: examiner traps, PYQ routes and applied lessons",
            f"{title}: integrated revision and answer-writing spine",
        )
    elif "geography" in subject_key:
        types = (
            "root-axes",
            "classification",
            "causal-system",
            "spatial-cross-section",
            "comparison",
            "hazard-response",
            "application-pyq",
            "answer-spine",
        )
        labels = (
            f"{title}: earth-system root and analytical axes",
            f"Classification and process families: {_focus(records, groups[0])}",
            f"Process chain: {_focus(records, groups[1])}",
            f"Spatial zones and cross-section: {_focus(records, groups[2])}",
            f"Global–India comparison: {_focus(records, groups[3])}",
            f"Hazards, impacts and interventions: {_focus(records, groups[4])}",
            f"{title}: map traps, PYQ routes and applications",
            f"{title}: integrated revision and answer-writing spine",
        )
    elif "polity" in subject_key:
        types = (
            "root-axes",
            "constitutional-hierarchy",
            "chronology",
            "institution-balance",
            "doctrine-case-law",
            "problem-response",
            "application-pyq",
            "answer-spine",
        )
        labels = (
            f"{title}: constitutional root, authority and analytical axes",
            f"Constitutional hierarchy and categories: {_focus(records, groups[0])}",
            f"Evolution and procedure: {_focus(records, groups[1])}",
            f"Institutions, powers and checks: {_focus(records, groups[2])}",
            f"Doctrine, Articles and case-law logic: {_focus(records, groups[3])}",
            f"Limits, accountability and federal tensions: {_focus(records, groups[4])}",
            f"{title}: close-option traps, PYQ routes and applications",
            f"{title}: integrated revision and answer-writing spine",
        )
    else:
        types = (
            "root-axes",
            "doctrine-map",
            "argument-tree",
            "comparison",
            "problem-response",
            "path-consequence",
            "application-pyq",
            "answer-spine",
        )
        labels = (
            f"{title}: central philosophical question and analytical axes",
            f"Doctrine map: {_focus(records, groups[0])}",
            f"Argument structure: {_focus(records, groups[1])}",
            f"Conceptual comparison: {_focus(records, groups[2])}",
            f"Objections, replies and qualified verdicts: {_focus(records, groups[3])}",
            f"Ethical, practical or liberation consequences: {_focus(records, groups[4])}",
            f"{title}: examiner traps, PYQ routes and applications",
            f"{title}: integrated revision and answer-writing spine",
        )

    sources = [sample, *groups, numbers, numbers]
    sections = [
        ["BASIC LEARNING SESSION"],
        ["BASIC LEARNING SESSION"],
        ["BASIC LEARNING SESSION"],
        ["BASIC LEARNING SESSION", "CONSOLIDATED REGISTER NOTES"],
        ["BASIC LEARNING SESSION", "CONSOLIDATED REGISTER NOTES"],
        ["BASIC LEARNING SESSION", "OPTIONAL ADVANCED DEPTH"],
        ["PYQS AND ANSWER PRACTICE", "CONSOLIDATED REGISTER NOTES"],
        ["CONSOLIDATED REGISTER NOTES", "PYQS AND ANSWER PRACTICE"],
    ]
    panels: list[dict[str, Any]] = []
    for panel_type, label, source_numbers, source_sections in zip(
        types, labels, sources, sections
    ):
        concepts: list[str] = []
        for number in source_numbers:
            if 1 <= number <= len(records):
                for value in [
                    *records[number - 1]["keywords"],
                    records[number - 1]["title"],
                ]:
                    value = short(value, 40)
                    if value and value.casefold() not in {
                        item.casefold() for item in concepts
                    }:
                        concepts.append(value)
                    if len(concepts) >= 5:
                        break
            if len(concepts) >= 5:
                break
        panels.append(
            {
                "title": short(label, 88),
                "structural_type": panel_type,
                "source_sessions": source_numbers,
                "source_sections": source_sections,
                "key_concepts": concepts,
            }
        )
    return {
        "topic_key": topic_key,
        "title": title,
        "subject": subject,
        "session_count": len(records),
        "review_status": "auto-designed-pending-manual-review",
        "panels": panels,
    }


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"topics": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    topics = data.get("topics", {})
    if not isinstance(topics, dict):
        raise ValueError("ASCII-master design manifest topics must be an object.")
    return data


def extract_reference_fragment(markdown: str) -> str:
    match = re.search(
        r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*"
        r"(?:\n+\*\*High-yield use:\*\*.*?\n+)?"
        r"(?P<panels>^####\s+ASCII MASTER FLOW — PANEL\s+1/\d+:.*)"
        r"(?=\n<!--|\Z)",
        markdown,
    )
    if not match:
        raise ValueError("Reference Markdown has no multi-panel ASCII master.")
    return match.group("panels").strip()


def _select(records: list[dict[str, Any]], panel: dict[str, Any]) -> list[dict[str, Any]]:
    selected = [
        records[number - 1]
        for number in panel.get("source_sessions", [])
        if isinstance(number, int) and 1 <= number <= len(records)
    ]
    return selected or records[: min(3, len(records))]


def _sample_records(
    records: list[dict[str, Any]],
    count: int,
) -> list[dict[str, Any]]:
    if len(records) <= count:
        return records
    indexes = {
        round(index * (len(records) - 1) / (count - 1))
        for index in range(count)
    }
    return [records[index] for index in sorted(indexes)]


def _concepts(
    panel: dict[str, Any],
    selected: list[dict[str, Any]],
    limit: int = 6,
) -> list[str]:
    values = [
        short(str(item), 42)
        for item in panel.get("key_concepts", [])
        if clean(str(item))
    ]
    for record in selected:
        values.extend(record["keywords"])
        values.append(record["title"])
    unique: list[str] = []
    for value in values:
        value = short(value, 42)
        if value and value.casefold() not in {item.casefold() for item in unique}:
            unique.append(value)
        if len(unique) >= limit:
            break
    return unique


def _branch_record(record: dict[str, Any], *, include_answer: bool = False) -> list[str]:
    lines = [f"├── {short(record['title'], 64)}"]
    lines.extend(wrapped(record["terms"], 82, "│   ├─ TERMS: "))
    lines.extend(wrapped(record["mechanism"], 82, "│   ├─ LOGIC: "))
    lines.extend(wrapped(record["consequence"], 82, "│   └─ RESULT: "))
    if include_answer:
        lines.extend(wrapped(record["answer"], 82, "│      ANSWER USE: "))
    return lines


def _render_root(
    topic_title: str,
    selected: list[dict[str, Any]],
    concepts: list[str],
) -> list[str]:
    nodes = (selected + selected[:1] * 3)[:3]
    lines = [
        f"{short(topic_title, 84).upper()} — CONCEPTUAL ATLAS",
        "",
        "                         CENTRAL QUESTION / ROOT",
        f"        How should the complete structure of {short(topic_title, 54)}",
        "        be defined, related, compared and evaluated?",
        "                                  │",
        "                                  ▼",
        f"                       {short(nodes[0]['terms'], 70)}",
        "                                  │",
        "          ┌───────────────────────┼───────────────────────┐",
        "          ▼                       ▼                       ▼",
    ]
    for index, node in enumerate(nodes, 1):
        lines.append(f"AXIS {index}: {short(node['title'], 66)}")
        lines.append(f"  • {short(node['keywords'][0], 66)}")
        lines.append(f"  • {short(node['mechanism'], 66)}")
    lines.extend(
        [
            "          └───────────────────────┼───────────────────────┘",
            "                                  ▼",
            "                         CROSS-PANEL CONTROL",
        ]
    )
    lines.extend(wrapped(" • ".join(concepts[:4]), 92, "  "))
    lines.extend(
        [
            "                                  │",
            "                                  ▼",
            "          Definition → relation → mechanism → comparison → verdict",
        ]
    )
    return lines


def _render_tree(
    heading: str,
    selected: list[dict[str, Any]],
    concepts: list[str],
) -> list[str]:
    lines = [heading.upper(), "│", "├── KEY CONCEPTS"]
    for index, concept in enumerate(concepts[:5]):
        connector = "└──" if index == min(4, len(concepts) - 1) else "├──"
        lines.append(f"│   {connector} {concept}")
    lines.append("│")
    for record in selected[:5]:
        lines.extend(_branch_record(record))
    lines.extend(
        [
            "│",
            "└── CONVERGENCE",
            "    ├─ Distinguish the branches before combining them",
            "    └─ Reconnect each branch to the topic's central explanatory problem",
        ]
    )
    return lines


def _render_sequence(
    heading: str,
    selected: list[dict[str, Any]],
) -> list[str]:
    lines = [heading.upper(), ""]
    for index, record in enumerate(selected[:6], 1):
        lines.append(f"STAGE {index:02d}  {short(record['title'], 70)}")
        lines.extend(wrapped(record["terms"], 82, "  ├─ CONDITION / TERM: "))
        lines.extend(wrapped(record["mechanism"], 82, "  ├─ CHANGE / MECHANISM: "))
        lines.extend(wrapped(record["consequence"], 82, "  └─ OUTCOME: "))
        if index < len(selected[:6]):
            lines.extend(["                  │", "                  ▼"])
    lines.extend(
        [
            "                  │",
            "                  ▼",
            "SEQUENCE CONTROL: chronology is evidence-led, not a bare dynasty/date list.",
        ]
    )
    return lines


def _render_causal(
    heading: str,
    selected: list[dict[str, Any]],
) -> list[str]:
    lines = [heading.upper(), ""]
    for index, record in enumerate(selected[:4], 1):
        lines.extend(
            [
                f"CAUSE / CONDITION {index}: {short(record['terms'], 62)}",
                "          │",
                "          ├── MECHANISM",
                *wrapped(record["mechanism"], 82, "          │   "),
                "          │",
                "          └── EFFECT / CONTRAST",
                *wrapped(record["consequence"], 82, "              "),
            ]
        )
        if index < len(selected[:4]):
            lines.extend(["          │", "          ▼"])
    lines.extend(
        [
            "          │",
            "          ▼",
            "SYSTEM RESULT: causes interact; mechanism explains why the outcome follows.",
        ]
    )
    return lines


def _table_rows(
    selected: list[dict[str, Any]],
    *,
    middle: str = "CORE POSITION",
    right: str = "DISTINCTION / RESULT",
) -> list[str]:
    widths = (24, 31, 31)
    top = "┌" + "┬".join("─" * width for width in widths) + "┐"
    sep = "├" + "┼".join("─" * width for width in widths) + "┤"
    bottom = "└" + "┴".join("─" * width for width in widths) + "┘"

    def row(values: Sequence[str]) -> list[str]:
        columns = [
            textwrap.wrap(
                short(value, width * 3),
                width=width - 2,
                break_long_words=False,
                break_on_hyphens=False,
            )
            or [""]
            for value, width in zip(values, widths)
        ]
        return [
            "│"
            + "│".join(
                f" {columns[column][line] if line < len(columns[column]) else '':<{widths[column] - 2}} "
                for column in range(3)
            )
            + "│"
            for line in range(max(map(len, columns)))
        ]

    lines = [top, *row(("MODEL / BRANCH", middle, right)), sep]
    for index, record in enumerate(selected[:5]):
        lines.extend(
            row((record["title"], record["terms"], record["consequence"]))
        )
        if index < len(selected[:5]) - 1:
            lines.append(sep)
    lines.append(bottom)
    return lines


def _render_comparison(
    heading: str,
    selected: list[dict[str, Any]],
) -> list[str]:
    return [
        heading.upper(),
        "",
        *_table_rows(selected),
        "                                  │",
        "                                  ▼",
        "COMPARE ON THE SAME AXIS: definition • mechanism • consequence • limit",
    ]


def _render_problem(
    heading: str,
    selected: list[dict[str, Any]],
) -> list[str]:
    lines = [
        heading.upper(),
        "",
        "                 CLAIM / SYSTEM UNDER EXAMINATION",
        "                                  │",
        "                                  ▼",
    ]
    for index, record in enumerate(selected[:4], 1):
        lines.extend(
            [
                f"PROBLEM / OBJECTION {index}",
                *wrapped(record["trap"], 82, "  ├─ ISSUE: "),
                *wrapped(record["mechanism"], 82, "  ├─ RESPONSE / CONTROL: "),
                *wrapped(record["consequence"], 82, "  └─ QUALIFIED VERDICT: "),
            ]
        )
        if index < len(selected[:4]):
            lines.extend(["                  │", "                  ▼"])
    lines.extend(
        [
            "                                  │",
            "                                  ▼",
            "FINAL CONTROL: preserve the strongest insight while stating its limit.",
        ]
    )
    return lines


def _render_spatial(
    heading: str,
    selected: list[dict[str, Any]],
) -> list[str]:
    lines = [
        heading.upper(),
        "",
        "UPSTREAM / OUTER SETTING",
        "        │",
        "        ▼",
    ]
    labels = ("ZONE / LAYER A", "ZONE / LAYER B", "ZONE / LAYER C", "INDIA / LOCAL EXPRESSION")
    for label, record in zip(labels, selected[:4]):
        lines.extend(
            [
                "┌──────────────────────────────────────────────────────────────────────┐",
                f"│ {label:<68} │",
                f"│ {short(record['title'], 68):<68} │",
                f"│ Process: {short(record['mechanism'], 59):<59} │",
                f"│ Result : {short(record['consequence'], 59):<59} │",
                "└──────────────────────────────────────────────────────────────────────┘",
                "        │",
                "        ▼",
            ]
        )
    lines.append("SPATIAL CONTROL: locate the process, then compare scale and regional expression.")
    return lines


def _render_application(
    heading: str,
    selected: list[dict[str, Any]],
    themes: list[str],
) -> list[str]:
    lines = [
        heading.upper(),
        "",
        "                         EXAM APPLICATION ROOT",
        "                                  │",
        "          ┌───────────────────────┼───────────────────────┐",
        "          ▼                       ▼                       ▼",
        "    CLOSE-OPTION TRAPS         PYQ / QUESTION ROUTES      ANSWER USE",
    ]
    sampled = _sample_records(selected, 4)
    for record in sampled:
        lines.extend(wrapped(record["trap"], 82, "├── "))
    lines.append("│")
    for theme in themes[:4]:
        lines.extend(wrapped(theme, 82, "├── "))
    lines.append("│")
    for record in _sample_records(selected, 3):
        lines.extend(wrapped(record["answer"], 82, "└── "))
    lines.extend(
        [
            "                                  │",
            "                                  ▼",
            "CONTROL: identify demand → select exact evidence → expose trap → qualify.",
        ]
    )
    return lines


def _render_answer(
    topic_title: str,
    selected: list[dict[str, Any]],
    concepts: list[str],
) -> list[str]:
    records = selected or []
    values = [
        records[0]["terms"] if records else topic_title,
        concepts[0] if concepts else topic_title,
        records[len(records) // 3]["mechanism"] if records else topic_title,
        concepts[min(2, len(concepts) - 1)] if concepts else topic_title,
        records[-1]["trap"] if records else topic_title,
        records[-1]["answer"] if records else topic_title,
    ]
    labels = (
        "1. DEFINE THE PRECISE TOPIC / TERM",
        "2. MAP THE MAIN TYPES, STAGES OR INSTITUTIONS",
        "3. EXPLAIN THE MECHANISM / ARGUMENT / CAUSAL LINK",
        "4. COMPARE ON A COMMON ANALYTICAL AXIS",
        "5. TEST WITH OBJECTION, LIMIT, EXCEPTION OR TRAP",
        "6. GIVE A QUALIFIED, TOPIC-SPECIFIC VERDICT",
    )
    lines = [f"{short(topic_title, 82).upper()} — ANSWER / REVISION SPINE", ""]
    for index, (label, value) in enumerate(zip(labels, values)):
        lines.append(label)
        lines.extend(wrapped(value, 82, "   └─ "))
        if index < len(labels) - 1:
            lines.extend(["                  │", "                  ▼"])
    lines.extend(
        [
            "",
            "HIGH-YIELD FORMULA",
            "  ROOT CONCEPT",
            "      + CLASSIFICATION / SEQUENCE",
            "      + MECHANISM / EVIDENCE",
            "      + COMPARISON / APPLICATION",
            "      + OBJECTION / LIMIT",
            "      = QUALIFIED ANSWER",
        ]
    )
    return lines


def render_panel(
    *,
    topic_title: str,
    panel: dict[str, Any],
    selected: list[dict[str, Any]],
    themes: list[str],
) -> str:
    panel_type = str(panel.get("structural_type") or "classification")
    heading = display_short(str(panel.get("title") or topic_title), 88)
    concepts = _concepts(panel, selected)
    if panel_type == "root-axes":
        lines = _render_root(topic_title, selected, concepts)
    elif panel_type in {"chronology", "procedure-sequence"}:
        lines = _render_sequence(heading, selected)
    elif panel_type in {
        "causal-system",
        "argument-tree",
        "institution-balance",
        "doctrine-case-law",
        "hazard-response",
        "path-consequence",
    }:
        lines = _render_causal(heading, selected)
    elif panel_type in {"comparison"}:
        lines = _render_comparison(heading, selected)
    elif panel_type in {"problem-response", "evidence-debate"}:
        lines = _render_problem(heading, selected)
    elif panel_type in {"spatial-cross-section"}:
        lines = _render_spatial(heading, selected)
    elif panel_type == "application-pyq":
        lines = _render_application(heading, selected, themes)
    elif panel_type == "answer-spine":
        lines = _render_answer(topic_title, selected, concepts)
    else:
        lines = _render_tree(heading, selected, concepts)
    key_line = " • ".join(concepts)
    if key_line and not all(concept.casefold() in "\n".join(lines).casefold() for concept in concepts):
        insertion = ["", *wrapped(key_line, 92, "KEY TERMS: ")]
        lines[2:2] = insertion
    return "\n".join(line.rstrip() for line in lines)


def build_master_fragment(
    *,
    root: Path,
    manifest_path: Path,
    topic_key: str,
    title: str,
    subject: str,
    cards: Sequence[Any],
    markdown: str,
) -> str:
    manifest = load_manifest(manifest_path)
    topic_spec = manifest.get("topics", {}).get(topic_key)
    if not isinstance(topic_spec, dict):
        topic_spec = auto_design(
            topic_key=topic_key,
            title=title,
            subject=subject,
            cards=cards,
            markdown=markdown,
        )
    reference = topic_spec.get("reference_master")
    if reference:
        path = root / Path(str(reference).replace("\\", "/"))
        return extract_reference_fragment(path.read_text(encoding="utf-8"))

    panels = topic_spec.get("panels")
    if not isinstance(panels, list) or not panels:
        raise ValueError(f"{topic_key}: ASCII design has no panels.")
    records = card_records(cards, markdown)
    themes = practice_themes(markdown)
    total = len(panels)
    chunks: list[str] = []
    for number, panel in enumerate(panels, 1):
        if not isinstance(panel, dict):
            raise ValueError(f"{topic_key}: panel {number} must be an object.")
        title_text = display_short(
            str(panel.get("title") or f"Panel {number}"),
            90,
        )
        body = render_panel(
            topic_title=title,
            panel=panel,
            selected=_select(records, panel),
            themes=themes,
        )
        chunks.extend(
            [
                f"#### ASCII MASTER FLOW — PANEL {number}/{total}: {title_text}",
                "",
                "```ascii-master",
                body,
                "```",
                "",
            ]
        )
    return "\n".join(chunks).rstrip()


def panel_blocks(fragment: str) -> list[tuple[int, int, str, str]]:
    return [
        (int(number), int(total), title.strip(), body.rstrip())
        for number, total, title, body in PANEL_BLOCK_RE.findall(fragment.strip())
    ]


def standalone_panel_blocks(fragment: str) -> list[tuple[int, int, str, str]]:
    matches = list(STANDALONE_PANEL_HEADING_RE.finditer(fragment.strip()))
    return [
        (
            int(match.group(1)),
            int(match.group(2)),
            match.group(3).strip(),
            fragment.strip()[
                match.end() : (
                    matches[index + 1].start()
                    if index + 1 < len(matches)
                    else len(fragment.strip())
                )
            ].strip("\n"),
        )
        for index, match in enumerate(matches)
    ]


def any_panel_blocks(fragment: str) -> list[tuple[int, int, str, str]]:
    return panel_blocks(fragment) or standalone_panel_blocks(fragment)


def standalone_panel_text(fragment: str) -> str:
    blocks = panel_blocks(fragment)
    if not blocks:
        raise ValueError("Embedded ASCII fragment has no panel blocks.")
    return "\n\n".join(
        f"ASCII MASTER FLOW — PANEL {number}/{total}: {title}\n{body}"
        for number, total, title, body in blocks
    ).rstrip() + "\n"


def normalized_panel_text(fragment: str) -> str:
    blocks = any_panel_blocks(fragment)
    return "\n\n".join(
        f"PANEL {number}/{total}: {title}\n{body.rstrip()}"
        for number, total, title, body in blocks
    ).strip()
