"""Author explicit Cārvāka graphical stage specs from trusted learner-v2 sources."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import carvaka_flowchart
import polity_flowchart_case_years
import refresh_all_v2_learning_sessions as refresh


ROOT = Path(__file__).resolve().parents[1]
SPEC_ROOT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
)


def _references(value: object) -> list[str]:
    if isinstance(value, list):
        return [
            json.dumps(item, ensure_ascii=False, sort_keys=True)
            if isinstance(item, dict)
            else str(item)
            for item in value
        ]
    if isinstance(value, dict):
        return [
            f"{key}: "
            + (
                json.dumps(item, ensure_ascii=False, sort_keys=True)
                if isinstance(item, (dict, list))
                else str(item)
            )
            for key, item in value.items()
        ]
    return [str(value)]


def spec_path(subject: str, topic_key: str) -> Path:
    return SPEC_ROOT / subject / f"{topic_key}.json"


def build_specs(topic_keys: set[str] | None = None) -> list[Path]:
    tracker = refresh.load_tracker()
    topics = refresh.latest_validated_topics(tracker, refresh.merged_overrides())
    manual = refresh.manual_ascii_specs()
    active = {topic.key for topic in topics}
    if active != set(manual):
        missing = sorted(active - set(manual))
        extra = sorted(set(manual) - active)
        raise refresh.RefreshError(
            f"Graphical spec source coverage mismatch; missing={missing}, extra={extra}"
        )
    selected = [
        topic for topic in topics
        if topic_keys is None or topic.key in topic_keys
    ]
    if topic_keys is not None:
        missing = sorted(topic_keys - {topic.key for topic in selected})
        if missing:
            raise refresh.RefreshError(f"Unknown active topic keys: {missing}")
    written: list[Path] = []
    for topic in selected:
        ascii_spec = manual[topic.key]
        panels = [
            {
                "title": panel.title,
                "body": panel.body,
                "structural_type": panel.structural_type,
                "source_references": _references(panel.source_references),
            }
            for panel in ascii_spec.panels
        ]
        spec = carvaka_flowchart.author_topic_spec(
            topic_key=topic.key,
            subject=topic.subject,
            title=topic.title,
            source_markdown=topic.markdown.read_text(encoding="utf-8"),
            source_markdown_path=refresh.relative(topic.markdown),
            ascii_spec_path=refresh.relative(ascii_spec.source_path),
            ascii_spec_sha256=refresh.sha256(ascii_spec.source_path),
            panels=panels,
            source_generation=topic.generation,
        )
        if topic.subject == "Polity":
            spec, _ = polity_flowchart_case_years.normalize_graphical_spec(spec)
            case_errors = polity_flowchart_case_years.graphical_spec_errors(spec)
            if case_errors:
                raise refresh.RefreshError(
                    f"{topic.key}: Polity case-year validation failed: "
                    + " | ".join(case_errors)
                )
        output = spec_path(topic.subject, topic.key)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        written.append(output)
    index = {
        "schema_version": carvaka_flowchart.SCHEMA_VERSION,
        "renderer": carvaka_flowchart.RENDERER_NAME,
        "renderer_version": carvaka_flowchart.RENDERER_VERSION,
        "generated_on": refresh.GRAPHICAL_REPAIR_DATE,
        "reference_folder": str(
            carvaka_flowchart.REFERENCE_FOLDER
        ).replace("/", "\\"),
        "reference_hashes": carvaka_flowchart.REFERENCE_HASHES,
        "topic_count": len(active),
        "specs": [
            {
                "topic_key": topic.key,
                "subject": topic.subject,
                "source_generation": topic.generation,
                "path": refresh.relative(
                    spec_path(topic.subject, topic.key)
                ),
            }
            for topic in topics
            if spec_path(topic.subject, topic.key).is_file()
        ],
    }
    SPEC_ROOT.mkdir(parents=True, exist_ok=True)
    index_path = SPEC_ROOT / "index.json"
    index_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if index_path not in written:
        written.append(index_path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topics", nargs="+")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    if not args.all and not args.topics:
        parser.error("Pass --all or --topics.")
    try:
        written = build_specs(set(args.topics) if args.topics else None)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(f"written={len(written)} root={refresh.relative(SPEC_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
