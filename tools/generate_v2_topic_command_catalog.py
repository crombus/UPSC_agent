"""Build the complete learner-v2 topic command catalogue from repository owners."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

from generate_export_command_index import PHILOSOPHY_BLOCKS, SUBJECTS


ROOT = Path(__file__).resolve().parents[1]
CATALOG_RELATIVE = Path("upsc-ai-kit") / "manifests" / "v2" / "topic-catalog.json"
SCHEMA_RELATIVE = (
    Path("upsc-ai-kit") / "manifests" / "v2" / "topic-catalog.schema.json"
)
V2_VARIANT = "learner-v2"

PHILOSOPHY_OWNER_FILES = {
    "Philosophy Paper I — Western Philosophy": (
        "paper-1\\western",
        (
            "Plato-Aristotle.md",
            "Rationalism.md",
            "Empiricism.md",
            "Kant.md",
            "Hegel.md",
            "Moore-Russell-EarlyWittgenstein.md",
            "Logical-Positivism.md",
            "Later-Wittgenstein.md",
            "Phenomenology-Husserl.md",
            "Existentialism.md",
            "Quine-Strawson.md",
        ),
        "_advanced\\Western-Philosophy-Dossier.md",
    ),
    "Philosophy Paper I — Indian Philosophy": (
        "paper-1\\indian",
        (
            "Carvaka.md",
            "Jainism.md",
            "Buddhism.md",
            "Nyaya-Vaisesika.md",
            "Samkhya.md",
            "Yoga.md",
            "Mimamsa.md",
            "Vedanta.md",
            "Aurobindo.md",
        ),
        "_advanced\\Indian-Philosophy-Dossier.md",
    ),
    "Philosophy Paper II — Socio-Political Philosophy": (
        "paper-2\\socio-political",
        (
            "Social-Political-Ideals.md",
            "Sovereignty.md",
            "Individual-and-State.md",
            "Forms-of-Government.md",
            "Political-Ideologies.md",
            "Humanism-Secularism-Multiculturalism.md",
            "Crime-and-Punishment.md",
            "Development-Social-Progress.md",
            "Gender-Discrimination.md",
            "Caste-Gandhi-Ambedkar.md",
        ),
        "_advanced\\Socio-Political-Dossier.md",
    ),
    "Philosophy Paper II — Philosophy of Religion": (
        "paper-2\\philosophy-of-religion",
        (
            "Notions-of-God.md",
            "Proofs-for-God.md",
            "Problem-of-Evil.md",
            "Soul-Immortality-Rebirth.md",
            "Reason-Revelation-Faith.md",
            "Religious-Experience.md",
            "Religion-without-God.md",
            "Religion-and-Morality.md",
            "Religious-Pluralism.md",
            "Religious-Language.md",
        ),
        "_advanced\\Philosophy-of-Religion-Dossier.md",
    ),
}


class CatalogError(ValueError):
    """Raised when catalogue discovery would produce unsafe commands."""


def slugify(value: str) -> str:
    value = value.casefold().replace("&", " and ")
    value = re.sub(r"[^\w]+", "-", value, flags=re.UNICODE)
    return value.strip("-_")


def windows_path(value: str | Path) -> str:
    return str(value).replace("/", "\\")


def repo_path(root: Path, value: str) -> Path:
    path = Path(value.replace("\\", os.sep).replace("/", os.sep))
    if path.is_absolute():
        raise CatalogError(f"Catalogue paths must be repository-relative: {value}")
    resolved = (root / path).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise CatalogError(f"Catalogue path escapes repository root: {value}") from exc
    return resolved


def relative_path(root: Path, path: Path) -> str:
    return windows_path(path.resolve().relative_to(root.resolve()))


def clean_title(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "").replace("**", "").replace("*", "")
    value = re.sub(r"<br\s*/?>.*", "", value, flags=re.I)
    return re.sub(r"\s+", " ", value).strip(" |")


def standard_topic_key(folder: str, number: int) -> str:
    return f"{slugify(folder)}-{number:02d}"


def philosophy_topic_key(section_name: str, number: int) -> str:
    return f"{slugify(section_name)}-{number:02d}"


def parse_export_index(root: Path) -> dict[str, dict[str, object]]:
    path = root / "EXPORT-PDF-COMMAND-INDEX.md"
    if not path.is_file():
        return {}
    mapping: dict[str, dict[str, object]] = {}
    pattern = re.compile(
        r"`(?P<command>Export PDF for .+? (?P<number>\d{2}) — "
        r"(?P<title>.+?))` — `(?P<topic_key>[^`]+)`"
    )
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.search(line)
        if not match:
            continue
        key = match.group("topic_key")
        record = {
            "topic_key": key,
            "number": int(match.group("number")),
            "display_title": clean_title(match.group("title")),
            "command": match.group("command"),
            "source": relative_path(root, path),
        }
        previous = mapping.get(key)
        if previous and previous != record:
            raise CatalogError(f"Conflicting export mappings for {key}")
        mapping[key] = record
    return mapping


def parse_command_index(subject_dir: Path) -> dict[int, dict[str, object]]:
    path = subject_dir / "LEARNING-SESSION-COMMAND-INDEX.md"
    if not path.is_file():
        return {}
    rows: dict[int, dict[str, object]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\|\s*(\d{1,3})\s*\|\s*([^|]+)\|", line)
        if not match:
            continue
        number = int(match.group(1))
        title = clean_title(match.group(2))
        references = re.findall(
            r"`((?:basic|advanced)[\\/][^`]+\.md)`",
            line,
            flags=re.I,
        )
        rows[number] = {
            "display_title": title,
            "references": tuple(dict.fromkeys(references)),
            "source": path,
        }
    return rows


def read_readme_titles(subject_dir: Path) -> dict[int, str]:
    path = subject_dir / "README.md"
    if not path.is_file():
        return {}
    titles: dict[int, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\|\s*(\d{1,3})\s*\|\s*([^|]+)\|", line)
        if match:
            titles.setdefault(int(match.group(1)), clean_title(match.group(2)))
    return titles


def numbered_owners(subject_dir: Path) -> dict[int, dict[str, Path]]:
    owners: dict[int, dict[str, Path]] = {}
    for tier in ("basic", "advanced"):
        directory = subject_dir / tier
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md"), key=lambda item: item.name.casefold()):
            match = re.match(r"^(\d{1,3})_(.+)\.md$", path.name)
            if not match or int(match.group(1)) == 0:
                continue
            owners.setdefault(int(match.group(1)), {})[tier] = path
    return owners


def explicit_readme_sections(subject_dir: Path) -> list[dict[str, object]]:
    path = subject_dir / "README.md"
    if not path.is_file():
        return []
    sections: list[dict[str, object]] = []
    pattern = re.compile(
        r"^#{2,4}\s+(.+?)\s*\(Topics?\s+(\d{1,3})\s*[-–]\s*(\d{1,3})"
        r"(?:[^)]*)\)\s*$",
        flags=re.I,
    )
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        name = clean_title(match.group(1))
        sections.append(
            {
                "key": slugify(name),
                "name": name,
                "start": int(match.group(2)),
                "end": int(match.group(3)),
                "basis": relative_path(subject_dir.parents[2], path),
            }
        )
    return sections


def subject_sources(root: Path, subject_dir: Path) -> tuple[list[str], list[str]]:
    syllabus_names = (
        "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
        "OFFICIAL-UPSC-SYLLABUS-VERBATIM.md",
        "README.md",
    )
    index_names = (
        "LEARNING-SESSION-COMMAND-INDEX.md",
    )
    syllabus = [
        relative_path(root, subject_dir / name)
        for name in syllabus_names
        if (subject_dir / name).is_file()
    ]
    indexes = [
        relative_path(root, subject_dir / name)
        for name in index_names
        if (subject_dir / name).is_file()
    ]
    return syllabus, indexes


def section_for_topic(
    subject_dir: Path,
    display_name: str,
    number: int,
) -> dict[str, object]:
    for section in explicit_readme_sections(subject_dir):
        if int(section["start"]) <= number <= int(section["end"]):
            return {
                "key": section["key"],
                "name": section["name"],
                "basis": "explicit-readme-range",
                "order": int(section["start"]),
            }
    return {
        "key": "subject-wide-syllabus",
        "name": "Subject-wide Syllabus",
        "basis": "subject-topic-map",
        "order": 1,
    }


def cited_owner(
    subject_dir: Path,
    references: Iterable[str],
    tier: str,
) -> Path | None:
    prefix = tier.casefold() + "\\"
    for value in references:
        normalized = windows_path(value)
        if normalized.casefold().startswith(prefix):
            return subject_dir / Path(normalized.replace("\\", os.sep))
    return None


def owner_title(path: Path | None) -> str:
    if path is None:
        return ""
    title = re.sub(r"^\d+_", "", path.stem).replace("-", " ")
    return clean_title(title)


def manifest_owners(root: Path) -> dict[str, dict[str, Path]]:
    result: dict[str, dict[str, Path]] = {}
    manifest_dir = root / "upsc-ai-kit" / "manifests" / "v2"
    ignored = {
        "section-manifest.schema.json",
        "section-manifest.template.json",
        "topic-catalog.json",
        "topic-catalog.schema.json",
    }
    for path in manifest_dir.glob("*.json"):
        if path.name.casefold() in ignored:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for topic in data.get("topics", []):
            if not isinstance(topic, dict) or not topic.get("topic_key"):
                continue
            mapped: dict[str, Path] = {}
            for field in ("source_basic", "source_canonical", "source_advanced"):
                value = topic.get(field)
                if isinstance(value, str) and value:
                    mapped[field] = root / Path(
                        value.replace("\\", os.sep)
                    )
            if mapped:
                result[str(topic["topic_key"])] = mapped
    return result


def make_standard_topics(
    root: Path,
    folder: str,
    display_name: str,
    subject_order: int,
    export_mapping: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    subject_dir = root / "upsc-ai-kit" / "knowledge" / folder
    if not subject_dir.is_dir():
        return []
    command_rows = parse_command_index(subject_dir)
    readme_titles = read_readme_titles(subject_dir)
    owners = numbered_owners(subject_dir)
    declared_owners = manifest_owners(root)
    export_numbers = {
        int(record["number"])
        for key, record in export_mapping.items()
        if key.startswith(slugify(folder) + "-")
        and re.fullmatch(rf"{re.escape(slugify(folder))}-\d+", key)
    }
    numbers = sorted(set(owners) | set(command_rows) | export_numbers)
    syllabus_sources, index_sources = subject_sources(root, subject_dir)
    topics: list[dict[str, object]] = []
    for number in numbers:
        key = standard_topic_key(folder, number)
        declared = declared_owners.get(key, {})
        row = command_rows.get(number, {})
        references = row.get("references", ())
        basic = owners.get(number, {}).get("basic") or cited_owner(
            subject_dir, references, "basic"
        ) or declared.get("source_basic")
        advanced = owners.get(number, {}).get("advanced") or cited_owner(
            subject_dir, references, "advanced"
        ) or declared.get("source_advanced")
        canonical = basic or declared.get("source_canonical") or advanced
        export = export_mapping.get(key)
        title = clean_title(
            str(
                (export or {}).get("display_title")
                or row.get("display_title")
                or readme_titles.get(number)
                or owner_title(canonical)
                or f"Unresolved topic {number:02d}"
            )
        )
        section = section_for_topic(subject_dir, display_name, number)
        command = (
            f"Generate learner-v2 topic: {display_name} — "
            f"{section['name']} — {title}"
        )
        missing_owner = canonical is None or not canonical.is_file()
        warning = (
            "No usable canonical/basic/advanced Markdown owner was discovered; "
            "the command is withheld."
            if missing_owner
            else None
        )
        topics.append(
            {
                "subject": {
                    "key": folder,
                    "display_name": display_name,
                    "order": subject_order,
                },
                "section": section,
                "topic_key": key,
                "topic_order": number,
                "source_number": number,
                "display_title": title,
                "learner_v2_command": command,
                "export_mapping": {
                    "topic_key": key,
                    "command": (export or {}).get("command"),
                    "source": (export or {}).get("source"),
                },
                "source_basic": relative_path(root, basic) if basic and basic.is_file() else None,
                "source_canonical": (
                    relative_path(root, canonical)
                    if canonical and canonical.is_file()
                    else None
                ),
                "source_advanced": (
                    relative_path(root, advanced)
                    if advanced and advanced.is_file()
                    else None
                ),
                "syllabus_sources": syllabus_sources,
                "index_sources": index_sources,
                "discovery_status": "unresolved" if missing_owner else "source-ready",
                "ambiguity_warning": warning,
            }
        )
    return topics


def make_philosophy_topics(
    root: Path,
    subject_order: int,
    export_mapping: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    subject_dir = root / "upsc-ai-kit" / "knowledge" / "Philosophy"
    syllabus_sources, index_sources = subject_sources(root, subject_dir)
    topics: list[dict[str, object]] = []
    for section_order, (section_name, titles) in enumerate(PHILOSOPHY_BLOCKS, 1):
        owner_dir, owner_files, advanced_file = PHILOSOPHY_OWNER_FILES[section_name]
        if len(owner_files) != len(titles):
            raise CatalogError(f"Philosophy owner map mismatch: {section_name}")
        section_key = slugify(section_name.removeprefix("Philosophy "))
        for number, (fallback_title, owner_file) in enumerate(
            zip(titles, owner_files), 1
        ):
            key = philosophy_topic_key(section_name, number)
            export = export_mapping.get(key)
            title = clean_title(
                str((export or {}).get("display_title") or fallback_title)
            )
            owner = subject_dir / Path(owner_dir.replace("\\", os.sep)) / owner_file
            advanced = subject_dir / Path(advanced_file.replace("\\", os.sep))
            missing_owner = not owner.is_file()
            command = (
                f"Generate learner-v2 topic: Philosophy Optional — "
                f"{section_name} — {title}"
            )
            topics.append(
                {
                    "subject": {
                        "key": "Philosophy",
                        "display_name": "Philosophy Optional",
                        "order": subject_order,
                    },
                    "section": {
                        "key": section_key,
                        "name": section_name,
                        "basis": "official-philosophy-paper-section",
                        "order": section_order,
                    },
                    "topic_key": key,
                    "topic_order": number,
                    "source_number": number,
                    "display_title": title,
                    "learner_v2_command": command,
                    "export_mapping": {
                        "topic_key": key,
                        "command": (export or {}).get("command"),
                        "source": (export or {}).get("source"),
                    },
                    "source_basic": None,
                    "source_canonical": (
                        relative_path(root, owner) if owner.is_file() else None
                    ),
                    "source_advanced": (
                        relative_path(root, advanced) if advanced.is_file() else None
                    ),
                    "syllabus_sources": syllabus_sources,
                    "index_sources": index_sources,
                    "discovery_status": (
                        "unresolved" if missing_owner else "source-ready"
                    ),
                    "ambiguity_warning": (
                        "The official Philosophy owner file is missing; the command is withheld."
                        if missing_owner
                        else None
                    ),
                }
            )
    return topics


def duplicate_values(topics: list[dict[str, object]], field: str) -> list[str]:
    counts = Counter(str(topic[field]) for topic in topics)
    return sorted(value for value, count in counts.items() if count > 1)


def declared_paths(topic: dict[str, object]) -> list[str]:
    values = [
        topic.get("source_basic"),
        topic.get("source_canonical"),
        topic.get("source_advanced"),
    ]
    values.extend(topic.get("syllabus_sources", []))
    values.extend(topic.get("index_sources", []))
    export = topic.get("export_mapping")
    if isinstance(export, dict):
        values.append(export.get("source"))
    return [str(value) for value in values if value]


def discover_tracker_aliases(root: Path) -> dict[str, list[str]]:
    directory = root / "upsc-ai-kit" / "manifests" / "v2"
    aliases: dict[str, set[str]] = {}
    ignored = {
        "section-manifest.schema.json",
        "section-manifest.template.json",
        "topic-catalog.json",
        "topic-catalog.schema.json",
    }
    if directory.is_dir():
        for path in sorted(directory.glob("*.json"), key=lambda item: item.name.casefold()):
            if path.name.casefold() in ignored:
                continue
            try:
                manifest = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            for topic in manifest.get("topics", []):
                if not isinstance(topic, dict) or not topic.get("topic_key"):
                    continue
                alias = str(topic["topic_key"])
                stable = None
                superseded = topic.get("superseded_v1")
                if superseded:
                    match = re.match(r"^(.+?):legacy-v1:g\d+$", str(superseded))
                    stable = match.group(1) if match else None
                for candidate in topic.get("tracker_topic_keys", []):
                    aliases.setdefault(str(candidate), set()).add(alias)
                if stable and stable != alias:
                    aliases.setdefault(stable, set()).add(alias)
    return {
        key: sorted(values, key=str.casefold)
        for key, values in aliases.items()
    }


def validate_catalog(root: Path, catalog: dict[str, object]) -> None:
    if catalog.get("schema_version") != 1:
        raise CatalogError("Topic catalogue schema_version must be 1.")
    if catalog.get("variant") != V2_VARIANT:
        raise CatalogError("Topic catalogue variant must be learner-v2.")
    topics = catalog.get("topics")
    if not isinstance(topics, list):
        raise CatalogError("Topic catalogue topics must be a list.")
    duplicate_keys = duplicate_values(topics, "topic_key")
    duplicate_commands = duplicate_values(topics, "learner_v2_command")
    if duplicate_keys or duplicate_commands:
        details = []
        if duplicate_keys:
            details.append("topic keys: " + ", ".join(duplicate_keys))
        if duplicate_commands:
            details.append("commands: " + ", ".join(duplicate_commands))
        raise CatalogError("Duplicate catalogue identities: " + "; ".join(details))
    missing = [
        f"{topic['topic_key']}: {value}"
        for topic in topics
        for value in declared_paths(topic)
        if not repo_path(root, value).is_file()
    ]
    if missing:
        raise CatalogError(
            "Every declared catalogue source path must exist:\n" + "\n".join(missing)
        )
    for topic in topics:
        if topic.get("discovery_status") == "source-ready" and not topic.get(
            "source_canonical"
        ):
            raise CatalogError(
                f"Source-ready topic lacks source_canonical: {topic['topic_key']}"
            )


def build_catalog(
    root: Path,
    *,
    subjects: list[tuple[str, str]] | None = None,
    include_philosophy: bool = True,
) -> dict[str, object]:
    root = root.resolve()
    export_mapping = parse_export_index(root)
    topics: list[dict[str, object]] = []
    configured_subjects = subjects if subjects is not None else SUBJECTS
    for subject_order, (folder, display_name) in enumerate(configured_subjects, 1):
        topics.extend(
            make_standard_topics(
                root,
                folder,
                display_name,
                subject_order,
                export_mapping,
            )
        )
    if include_philosophy and (root / "upsc-ai-kit" / "knowledge" / "Philosophy").is_dir():
        topics.extend(
            make_philosophy_topics(root, len(configured_subjects) + 1, export_mapping)
        )
    tracker_aliases = discover_tracker_aliases(root)
    for topic in topics:
        topic["tracker_topic_keys"] = tracker_aliases.get(
            str(topic["topic_key"]),
            [],
        )
    topics.sort(
        key=lambda topic: (
            int(topic["subject"]["order"]),
            int(topic["section"]["order"]),
            int(topic["topic_order"]),
            str(topic["topic_key"]).casefold(),
        )
    )
    subjects_seen = {
        str(topic["subject"]["key"])
        for topic in topics
    }
    sections_seen = {
        (str(topic["subject"]["key"]), str(topic["section"]["key"]))
        for topic in topics
    }
    ready = sum(topic["discovery_status"] == "source-ready" for topic in topics)
    unresolved = len(topics) - ready
    duplicate_keys = duplicate_values(topics, "topic_key")
    duplicate_commands = duplicate_values(topics, "learner_v2_command")
    catalog = {
        "$schema": "topic-catalog.schema.json",
        "schema_version": 1,
        "variant": V2_VARIANT,
        "catalogue_policy": {
            "topic_identity": (
                "Basic/advanced pairs are one topic. Meta, audit, revision, prompt, "
                "support and assembled learning-session files are not topics unless the "
                "stable export syllabus explicitly maps them to a command topic."
            ),
            "command_readiness": (
                "Only source-ready topics are emitted as learner commands. Unresolved "
                "entries remain machine-readable and appear in the generated appendix."
            ),
            "on_demand_sections": (
                "A valid topic command may target a section with no registered section "
                "manifest. The agent resolves this catalogue, materialises that full "
                "section manifest and its indexes, then generates only the requested topic."
            ),
        },
        "discovery_sources": [
            "upsc-ai-kit\\knowledge\\<Subject>\\basic\\*.md",
            "upsc-ai-kit\\knowledge\\<Subject>\\advanced\\*.md",
            "upsc-ai-kit\\knowledge\\<Subject>\\README.md",
            "upsc-ai-kit\\knowledge\\<Subject>\\OFFICIAL-UPSC-SYLLABUS-*.md",
            "upsc-ai-kit\\knowledge\\<Subject>\\LEARNING-SESSION-COMMAND-INDEX.md",
            "EXPORT-PDF-COMMAND-INDEX.md",
        ],
        "statistics": {
            "subjects": len(subjects_seen),
            "sections": len(sections_seen),
            "topics": len(topics),
            "source_ready_topics": ready,
            "ambiguous_or_unresolved_entries": unresolved,
            "duplicate_topic_keys": len(duplicate_keys),
            "duplicate_commands": len(duplicate_commands),
        },
        "duplicates": {
            "topic_keys": duplicate_keys,
            "commands": duplicate_commands,
        },
        "topics": topics,
    }
    validate_catalog(root, catalog)
    return catalog


def write_catalog(root: Path, output: Path | None = None) -> Path:
    root = root.resolve()
    path = (output or (root / CATALOG_RELATIVE)).resolve()
    catalog = build_catalog(root)
    content = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8", newline="\n")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--guide",
        action="store_true",
        help="Regenerate the root learner-v2 command guide after writing the catalogue.",
    )
    args = parser.parse_args()
    root = args.repository_root.resolve()
    output = args.output
    if output and not output.is_absolute():
        output = root / output
    try:
        path = write_catalog(root, output)
        catalog = json.loads(path.read_text(encoding="utf-8"))
        validate_catalog(root, catalog)
    except (CatalogError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(f"catalogue: {path.relative_to(root)}")
    print(json.dumps(catalog["statistics"], ensure_ascii=False, sort_keys=True))
    if args.guide:
        from generate_v2_section_indexes import generate_command_guide

        guide = generate_command_guide(root)
        print(f"command_guide: {guide.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
