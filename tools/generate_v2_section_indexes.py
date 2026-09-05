"""Generate deterministic learner-v2 section coverage and deliverable indexes."""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
V2_VARIANT = "learner-v2"
INDEX_FILES = (
    "TOPIC-COVERAGE-INDEX.md",
    "NOTES-PDF-INDEX.md",
    "WORKBOOK-PDF-INDEX.md",
)
COMMAND_GUIDE_FILE = "V2-SUBJECT-SECTION-COMMAND-INDEX.md"
TOPIC_CATALOG_FILE = (
    Path("upsc-ai-kit") / "manifests" / "v2" / "topic-catalog.json"
)

PHILOSOPHY_SECTIONS = {
    "paper-i-western-philosophy": (
        "paper-1/western",
        (
            "Plato and Aristotle",
            "Rationalism",
            "Empiricism",
            "Kant",
            "Hegel",
            "Moore, Russell and Early Wittgenstein",
            "Logical Positivism",
            "Later Wittgenstein",
            "Phenomenology (Husserl)",
            "Existentialism",
            "Quine and Strawson",
        ),
    ),
    "paper-i-indian-philosophy": (
        "paper-1/indian",
        (
            "Carvaka",
            "Jainism",
            "Schools of Buddhism",
            "Nyaya–Vaisesika",
            "Samkhya",
            "Yoga",
            "Mimamsa",
            "Schools of Vedanta",
            "Aurobindo",
        ),
    ),
    "paper-ii-socio-political-philosophy": (
        "paper-2/socio-political",
        (
            "Social and Political Ideals",
            "Sovereignty",
            "Individual and State",
            "Forms of Government",
            "Political Ideologies",
            "Humanism, Secularism and Multiculturalism",
            "Crime and Punishment",
            "Development and Social Progress",
            "Gender Discrimination",
            "Caste Discrimination: Gandhi and Ambedkar",
        ),
    ),
    "paper-ii-philosophy-of-religion": (
        "paper-2/religion",
        (
            "Notions of God",
            "Proofs for the Existence of God",
            "Problem of Evil",
            "Soul: Immortality, Rebirth and Liberation",
            "Reason, Revelation and Faith",
            "Religious Experience",
            "Religion without God",
            "Religion and Morality",
            "Religious Pluralism and Absolute Truth",
            "Nature of Religious Language",
        ),
    ),
}


class ManifestError(ValueError):
    """Raised when an explicit section manifest is invalid."""


class AmbiguousDiscoveryError(ValueError):
    """Raised when repository indexes do not define one safe section boundary."""


@dataclass(frozen=True)
class TopicState:
    topic: dict[str, object]
    record: dict[str, object] | None
    assembled_markdown: str
    notes_pdf: str
    workbook_pdf: str
    package_state: str
    approval_state: str
    validation_state: str
    missing: tuple[str, ...]


def slugify(value: str) -> str:
    value = value.casefold().replace("&", " and ")
    value = re.sub(r"[^\w]+", "-", value, flags=re.UNICODE)
    return value.strip("-_")


def repo_path(root: Path, value: str) -> Path:
    """Resolve a repository-relative path containing either slash style."""
    normalized = value.replace("\\", os.sep).replace("/", os.sep)
    path = Path(normalized)
    if path.is_absolute():
        raise ManifestError(f"Manifest paths must be repository-relative: {value}")
    resolved = (root / path).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise ManifestError(f"Manifest path escapes repository root: {value}") from exc
    return resolved


def windows_path(value: str | Path) -> str:
    return str(value).replace("/", "\\")


def clean_title(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "").replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", value).strip(" |")


def title_tokens(value: str) -> set[str]:
    ignored = {"and", "the", "of", "in", "to", "for", "with", "part", "topics"}
    return {
        token
        for token in re.findall(r"\w+", value.casefold(), flags=re.UNICODE)
        if token not in ignored and not token.isdigit()
    }


def compatible_title(left: str, right: str) -> bool:
    left_tokens = title_tokens(left)
    right_tokens = title_tokens(right)
    if not left_tokens or not right_tokens:
        return False
    overlap = len(left_tokens & right_tokens)
    return overlap / min(len(left_tokens), len(right_tokens)) >= 0.5


def resolve_subject_directory(root: Path, subject: str) -> Path:
    knowledge = root / "upsc-ai-kit" / "knowledge"
    direct = knowledge / subject
    if direct.is_dir():
        return direct
    target = slugify(subject)
    matches = [
        path
        for path in knowledge.iterdir()
        if path.is_dir() and slugify(path.name) == target
    ]
    if len(matches) != 1:
        raise ManifestError(
            f"Cannot resolve one knowledge subject directory for {subject!r}."
        )
    return matches[0]


def read_readme_titles(subject_dir: Path) -> dict[int, str]:
    readme = subject_dir / "README.md"
    if not readme.is_file():
        return {}
    titles: dict[int, str] = {}
    for line in readme.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\|\s*(\d{1,2})\s*\|\s*([^|]+)\|", line)
        if match:
            titles.setdefault(int(match.group(1)), clean_title(match.group(2)))
    return titles


def numbered_owner_catalog(subject_dir: Path) -> dict[int, dict[str, object]]:
    readme_titles = read_readme_titles(subject_dir)
    basics: dict[int, Path] = {}
    advanced: dict[int, Path] = {}
    for tier, target in (("basic", basics), ("advanced", advanced)):
        directory = subject_dir / tier
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            match = re.match(r"^(\d{1,2})_(.+)\.md$", path.name)
            if match:
                target[int(match.group(1))] = path

    catalog: dict[int, dict[str, object]] = {}
    for number in sorted(set(readme_titles) | set(basics) | set(advanced)):
        basic = basics.get(number)
        advanced_owner = advanced.get(number)
        owner = basic or advanced_owner
        if owner is None:
            continue
        owner_title = clean_title(re.sub(r"^\d+_", "", owner.stem).replace("-", " "))
        readme_title = readme_titles.get(number)
        title = (
            readme_title
            if readme_title and compatible_title(readme_title, owner_title)
            else owner_title
        )
        catalog[number] = {
            "number": number,
            "display_title": title,
            "source_basic": (
                windows_path(basic.relative_to(subject_dir.parents[2]))
                if basic
                else None
            ),
            "source_canonical": windows_path(owner.relative_to(subject_dir.parents[2])),
            "source_advanced": (
                windows_path(advanced_owner.relative_to(subject_dir.parents[2]))
                if advanced_owner
                else None
            ),
        }
    return catalog


def philosophy_owner_catalog(
    root: Path,
    subject_dir: Path,
    section_key: str,
) -> dict[int, dict[str, object]]:
    canonical_key = section_key.removesuffix("-pilot")
    definition = PHILOSOPHY_SECTIONS.get(canonical_key)
    if not definition:
        return {}
    relative_directory, titles = definition
    directory = subject_dir / Path(relative_directory)
    if not directory.is_dir():
        return {}
    candidates = sorted(
        path
        for path in directory.glob("*.md")
        if path.name.casefold() != "readme.md"
    )
    catalog: dict[int, dict[str, object]] = {}
    for number, title in enumerate(titles, 1):
        matches = [
            path
            for path in candidates
            if compatible_title(title, clean_title(path.stem.replace("-", " ")))
        ]
        if len(matches) != 1:
            continue
        owner = matches[0]
        relative = windows_path(owner.relative_to(root))
        catalog[number] = {
            "number": number,
            "display_title": title,
            "source_basic": relative,
            "source_canonical": relative,
            "source_advanced": None,
        }
    return catalog


def owner_catalog(
    root: Path,
    subject_dir: Path,
    section_key: str,
) -> dict[int, dict[str, object]]:
    if subject_dir.name.casefold() == "philosophy":
        philosophy = philosophy_owner_catalog(root, subject_dir, section_key)
        if philosophy:
            return philosophy
    return numbered_owner_catalog(subject_dir)


def heading_table_sections(path: Path) -> list[tuple[str, tuple[int, ...]]]:
    if not path.is_file():
        return []
    current_heading = ""
    sections: dict[str, list[int]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^#{2,6}\s+(.+?)\s*$", line)
        if heading:
            current_heading = clean_title(heading.group(1))
            continue
        row = re.match(
            r"^\|\s*(\d{1,2})(?:\s*-\s*(\d{1,2}))?\s*\|",
            line,
        )
        if row and current_heading:
            start = int(row.group(1))
            end = int(row.group(2) or start)
            sections.setdefault(current_heading, []).extend(range(start, end + 1))
    return [
        (heading, tuple(dict.fromkeys(numbers)))
        for heading, numbers in sections.items()
        if numbers
    ]


def section_matches(query: str, heading: str) -> bool:
    query_tokens = title_tokens(query)
    heading_tokens = title_tokens(heading)
    if not query_tokens or not heading_tokens:
        return False
    overlap = len(query_tokens & heading_tokens)
    return overlap / min(len(query_tokens), len(heading_tokens)) >= 0.6


def discover_section_numbers(
    subject_dir: Path,
    section_key: str,
    section_name: str,
    catalog: dict[int, dict[str, object]],
) -> tuple[int, ...]:
    canonical_philosophy_key = section_key.removesuffix("-pilot")
    if (
        subject_dir.name.casefold() == "philosophy"
        and canonical_philosophy_key in PHILOSOPHY_SECTIONS
        and catalog
    ):
        return tuple(sorted(catalog))

    if slugify(section_name) == slugify(subject_dir.name):
        return tuple(sorted(catalog))

    candidates: set[tuple[int, ...]] = set()
    query = f"{section_key} {section_name}"
    for name in (
        "README.md",
        "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
        "OFFICIAL-UPSC-SYLLABUS-VERBATIM.md",
        "LEARNING-SESSION-COMMAND-INDEX.md",
    ):
        for heading, numbers in heading_table_sections(subject_dir / name):
            if section_matches(query, heading):
                owned = tuple(number for number in numbers if number in catalog)
                if owned:
                    candidates.add(owned)

    if len(candidates) != 1:
        reason = "no matching section boundary" if not candidates else "conflicting section boundaries"
        raise AmbiguousDiscoveryError(
            f"Automatic discovery found {reason} for {subject_dir.name}/"
            f"{section_key}. Create an explicit manifest from "
            "upsc-ai-kit\\manifests\\v2\\section-manifest.template.json."
        )
    return next(iter(candidates))


def default_manifest_path(root: Path, subject: str, section_key: str) -> Path:
    return (
        root
        / "upsc-ai-kit"
        / "manifests"
        / "v2"
        / f"{slugify(subject)}--{section_key}.json"
    )


def build_discovered_manifest(
    root: Path,
    subject: str,
    section_key: str,
    section_name: str,
) -> dict[str, object]:
    subject_dir = resolve_subject_directory(root, subject)
    catalog = owner_catalog(root, subject_dir, section_key)
    if not catalog:
        raise AmbiguousDiscoveryError(
            f"No canonical topic owners were found for {subject}/{section_key}; "
            "use an explicit manifest."
        )
    numbers = discover_section_numbers(subject_dir, section_key, section_name, catalog)
    topics = []
    for number in numbers:
        owner = catalog[number]
        topic_key = f"{slugify(subject_dir.name)}-{number:02d}"
        topics.append(
            {
                "topic_key": topic_key,
                "display_title": owner["display_title"],
                "syllabus_mapping": (
                    f"{section_name}; repository topic {number:02d}. "
                    "Confirm the exact official clause in the section manifest before generation."
                ),
                "source_basic": owner["source_basic"],
                "source_canonical": owner["source_canonical"],
                "source_advanced": owner["source_advanced"],
                "cross_topic_sources": [],
                "verified_pyq_sources": [],
            }
        )
    return {
        "schema_version": 1,
        "variant": V2_VARIANT,
        "subject": {
            "key": subject_dir.name,
            "display_name": subject_dir.name.replace("-", " "),
        },
        "section": {
            "key": section_key,
            "name": section_name,
            "scope": "official-section",
            "complete_syllabus_section": False,
            "syllabus_sources": [
                windows_path(path.relative_to(root))
                for path in (
                    subject_dir / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
                    subject_dir / "OFFICIAL-UPSC-SYLLABUS-VERBATIM.md",
                    subject_dir / "README.md",
                    subject_dir / "LEARNING-SESSION-COMMAND-INDEX.md",
                )
                if path.is_file()
            ],
            "notes": (
                "Automatically discovered. Review the official boundary, exact syllabus "
                "mappings, cross-topic owners and verified PYQs; set "
                "complete_syllabus_section to true only after that review."
            ),
        },
        "topics": topics,
    }


def load_manifest(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise ManifestError(f"Manifest does not exist: {path}")
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ManifestError(f"Manifest is not valid JSON: {exc}") from exc
    validate_manifest(manifest)
    return manifest


def validate_manifest(manifest: dict[str, object]) -> None:
    if manifest.get("schema_version") != 1:
        raise ManifestError("Section manifest schema_version must be 1.")
    if manifest.get("variant") != V2_VARIANT:
        raise ManifestError("Section manifest variant must be learner-v2.")
    subject = manifest.get("subject")
    section = manifest.get("section")
    topics = manifest.get("topics")
    if not isinstance(subject, dict) or not subject.get("key"):
        raise ManifestError("Manifest subject.key is required.")
    if not isinstance(section, dict) or not section.get("key") or not section.get("name"):
        raise ManifestError("Manifest section.key and section.name are required.")
    scope = str(section.get("scope") or "").strip().casefold()
    if scope not in {"official-section", "pilot"}:
        raise ManifestError(
            f"Manifest section.scope must be official-section or pilot, got {section.get('scope')!r}."
        )
    section["scope"] = scope
    if not isinstance(section.get("complete_syllabus_section"), bool):
        raise ManifestError("Manifest section.complete_syllabus_section must be boolean.")
    if section.get("scope") == "pilot" and section.get("complete_syllabus_section"):
        raise ManifestError("A pilot manifest cannot claim a complete syllabus section.")
    if not isinstance(section.get("syllabus_sources"), list):
        raise ManifestError("Manifest section.syllabus_sources must be a list.")
    if not isinstance(topics, list) or not topics:
        raise ManifestError("Manifest topics must be a non-empty list.")
    keys: set[str] = set()
    for position, topic in enumerate(topics, 1):
        if not isinstance(topic, dict):
            raise ManifestError(f"Topic {position} must be an object.")
        for field in ("topic_key", "display_title", "syllabus_mapping"):
            if not topic.get(field):
                raise ManifestError(f"Topic {position} is missing {field}.")
        key = str(topic["topic_key"])
        if key in keys:
            raise ManifestError(f"Duplicate topic_key in manifest: {key}")
        keys.add(key)
        if not (topic.get("source_basic") or topic.get("source_canonical")):
            raise ManifestError(
                f"Topic {key} needs source_basic or source_canonical."
            )
        for field in ("cross_topic_sources", "verified_pyq_sources"):
            value = topic.get(field, [])
            if not isinstance(value, list):
                raise ManifestError(f"Topic {key} field {field} must be a list.")


def validate_manifest_source_paths(root: Path, manifest: dict[str, object]) -> None:
    checks: list[tuple[str, str]] = []
    section = manifest["section"]
    for value in section.get("syllabus_sources", []):
        checks.append(("section syllabus source", str(value)))
    for topic in manifest["topics"]:
        key = str(topic["topic_key"])
        for field in ("source_basic", "source_canonical", "source_advanced"):
            if topic.get(field):
                checks.append((f"{key} {field}", str(topic[field])))
        for field in ("cross_topic_sources", "verified_pyq_sources"):
            for value in topic.get(field, []):
                checks.append((f"{key} {field}", str(value)))
    missing = [
        f"{label}: {value}"
        for label, value in checks
        if not repo_path(root, value).is_file()
    ]
    if missing:
        raise ManifestError(
            "Manifest source owners must exist before index generation:\n"
            + "\n".join(missing)
        )


def load_tracker(path: Path) -> list[dict[str, object]]:
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 2:
        raise ManifestError("EXPORT-PDF-STATUS.json schema_version must be 2.")
    records = [
        record
        for record in data.get("exports", [])
        if isinstance(record, dict)
    ]
    identities: set[tuple[str, str, int]] = set()
    for record in records:
        identity = (
            str(record.get("topic_key")),
            str(record.get("variant")),
            int(record.get("generation") or 1),
        )
        if identity in identities:
            raise ManifestError(
                "Duplicate tracker identity: "
                f"{identity[0]} / {identity[1]} / g{identity[2]}"
            )
        identities.add(identity)
    return records


def latest_record(
    topic: dict[str, object],
    records: list[dict[str, object]],
) -> dict[str, object] | None:
    keys = {str(topic["topic_key"])}
    keys.update(str(value) for value in topic.get("tracker_topic_keys", []))
    matches = [
        record
        for record in records
        if record.get("variant") == V2_VARIANT
        and str(record.get("topic_key")) in keys
    ]
    if not matches:
        return None
    return max(matches, key=lambda record: int(record.get("generation") or 1))


def default_paths(
    subject: str,
    section_key: str,
    topic_key: str,
) -> tuple[str, str, str]:
    markdown = (
        f"upsc-ai-kit\\knowledge\\{subject}\\learning-sessions\\v2\\"
        f"{section_key}\\{topic_key}_Learning-Session.md"
    )
    notes = (
        f"notes\\{subject}\\learning-session-v2\\{section_key}\\notes\\"
        f"{topic_key}_Learning-Session_<YYYY-MM-DD>.pdf"
    )
    workbook = (
        f"notes\\{subject}\\learning-session-v2\\{section_key}\\workbooks\\"
        f"{topic_key}_Solved-Workbook_<YYYY-MM-DD>.pdf"
    )
    return markdown, notes, workbook


def approved(record: dict[str, object]) -> bool:
    approval = record.get("approval")
    if isinstance(approval, dict):
        return bool(approval.get("approved"))
    return bool(record.get("approved"))


def validation_passed(record: dict[str, object] | None) -> bool:
    if record is None:
        return False
    validation = record.get("validation")
    if not isinstance(validation, dict):
        return False
    return str(
        validation.get("state") or validation.get("status") or ""
    ).casefold() == "passed"


def validation_label(record: dict[str, object] | None, missing: tuple[str, ...]) -> str:
    if record is None:
        return "pending"
    validation = record.get("validation")
    if isinstance(validation, dict):
        return str(validation.get("state") or validation.get("status") or "not-recorded")
    if missing:
        return "blocked: missing " + ", ".join(missing)
    return "not-recorded"


def resolve_topic_states(
    root: Path,
    manifest: dict[str, object],
    records: list[dict[str, object]],
) -> list[TopicState]:
    subject = str(manifest["subject"]["key"])
    section_key = str(manifest["section"]["key"])
    states: list[TopicState] = []
    for topic in manifest["topics"]:
        topic_key = str(topic["topic_key"])
        defaults = default_paths(subject, section_key, topic_key)
        record = latest_record(topic, records)
        assembled = str(
            (record or {}).get("markdown")
            or topic.get("assembled_markdown")
            or defaults[0]
        )
        notes = str(
            (record or {}).get("main_pdf")
            or topic.get("notes_pdf")
            or defaults[1]
        )
        workbook = str(
            (record or {}).get("workbook")
            or topic.get("workbook_pdf")
            or defaults[2]
        )
        missing = tuple(
            label
            for label, value in (
                ("assembled Markdown", assembled),
                ("notes PDF", notes),
                ("workbook PDF", workbook),
            )
            if "<YYYY-MM-DD>" in value or not repo_path(root, value).is_file()
        )
        is_approved = approved(record) if record else False
        if record is None:
            package_state = "planned"
            approval_state = "not generated"
        elif missing or not validation_passed(record):
            package_state = "incomplete"
            approval_state = "approved" if is_approved else "pending"
        elif is_approved:
            package_state = "approved"
            approval_state = "approved"
        else:
            package_state = "generated"
            approval_state = "pending explicit topic approval"
        states.append(
            TopicState(
                topic=topic,
                record=record,
                assembled_markdown=assembled,
                notes_pdf=notes,
                workbook_pdf=workbook,
                package_state=package_state,
                approval_state=approval_state,
                validation_state=validation_label(record, missing),
                missing=missing,
            )
        )
    return states


def cell(value: object) -> str:
    text = str(value if value not in (None, "") else "—")
    return text.replace("|", "\\|").replace("\r", " ").replace("\n", "<br>")


def path_cell(root: Path, index_path: Path, value: str) -> str:
    display = windows_path(value)
    if "<YYYY-MM-DD>" in value:
        return f"`{cell(display)}`"
    target = repo_path(root, value)
    if not target.exists():
        return f"`{cell(display)}`"
    relative = os.path.relpath(target, index_path.parent).replace("\\", "/")
    href = quote(relative, safe="/#-_.~")
    return f"[`{cell(display)}`]({href})"


def list_paths(root: Path, index_path: Path, values: object) -> str:
    if not isinstance(values, list) or not values:
        return "—"
    return "<br>".join(path_cell(root, index_path, str(value)) for value in values)


def owner_cell(root: Path, index_path: Path, topic: dict[str, object]) -> str:
    owners: list[str] = []
    basic = topic.get("source_basic")
    canonical = topic.get("source_canonical")
    if basic:
        owners.append("Basic: " + path_cell(root, index_path, str(basic)))
    if canonical and canonical != basic:
        owners.append("Canonical: " + path_cell(root, index_path, str(canonical)))
    return "<br>".join(owners) if owners else "—"


def record_variant(record: dict[str, object] | None) -> str:
    if not record:
        return "learner-v2 / planned"
    return f"{record.get('variant', V2_VARIANT)} / g{int(record.get('generation') or 1)}"


def superseded_value(state: TopicState) -> str:
    if state.record:
        provenance = state.record.get("provenance")
        provenance_value = (
            provenance.get("superseded_v1")
            if isinstance(provenance, dict)
            else None
        )
        return str(
            state.record.get("supersedes")
            or provenance_value
            or state.topic.get("superseded_v1")
            or "—"
        )
    return str(state.topic.get("superseded_v1") or "—")


def summary_lines(manifest: dict[str, object], states: list[TopicState]) -> list[str]:
    section = manifest["section"]
    scope = str(section.get("scope") or "official-section")
    complete = bool(section.get("complete_syllabus_section"))
    counts = {
        state: sum(item.package_state == state for item in states)
        for state in ("planned", "incomplete", "generated", "approved")
    }
    lines = [
        f"> **Section type:** {scope}",
        f"> **Complete official section:** {'yes' if complete else 'no'}",
        (
            "> **Progress:** "
            f"{counts['approved']} approved · {counts['generated']} generated/unapproved · "
            f"{counts['incomplete']} incomplete · {counts['planned']} planned"
        ),
    ]
    if scope == "pilot" or not complete:
        lines.append(
            "> **Pilot boundary:** this index records completed pilot topics only; it is "
            "not a claim that the complete syllabus section is covered."
        )
    lines.extend(
        [
            "",
            "> Markdown owners are the source of truth, but completeness is never inferred "
            "from one file alone. It must reconcile the official syllabus, Basic/canonical "
            "owners, cross-topic/thematic files, available verified PYQs, and Advanced material "
            "last. OCR PDFs and live sources supplement this chain; they do not replace it.",
            "",
        ]
    )
    return lines


def render_coverage(
    root: Path,
    index_path: Path,
    manifest: dict[str, object],
    states: list[TopicState],
) -> str:
    subject = manifest["subject"]
    section = manifest["section"]
    lines = [
        f"# {section['name']} — Topic Coverage Index",
        "",
        f"> **Subject:** {subject.get('display_name') or subject['key']}",
        f"> **Section key:** `{section['key']}`",
        f"> **Manifest:** `{windows_path(manifest['_manifest_path'])}`",
        (
            "> **Official syllabus/index sources:** "
            + list_paths(root, index_path, section.get("syllabus_sources"))
        ),
        (
            f"> **Section note:** {cell(section['notes'])}"
            if section.get("notes")
            else "> **Section note:** —"
        ),
        *summary_lines(manifest, states),
        "## Planned coverage and current status",
        "",
        "| # | Topic key | Display title | Syllabus mapping | Basic/canonical source | Advanced source | Cross-topic/thematic sources | Verified PYQs | Assembled Markdown | Notes PDF | Workbook PDF | Variant / generation | Package state | Approval | Validation | Superseded v1 |",
        "|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for number, state in enumerate(states, 1):
        topic = state.topic
        lines.append(
            "| "
            + " | ".join(
                [
                    str(number),
                    f"`{cell(topic['topic_key'])}`",
                    cell(topic["display_title"]),
                    cell(topic["syllabus_mapping"]),
                    owner_cell(root, index_path, topic),
                    (
                        path_cell(root, index_path, str(topic["source_advanced"]))
                        if topic.get("source_advanced")
                        else "—"
                    ),
                    list_paths(root, index_path, topic.get("cross_topic_sources")),
                    list_paths(root, index_path, topic.get("verified_pyq_sources")),
                    path_cell(root, index_path, state.assembled_markdown),
                    path_cell(root, index_path, state.notes_pdf),
                    path_cell(root, index_path, state.workbook_pdf),
                    cell(record_variant(state.record)),
                    cell(state.package_state),
                    cell(state.approval_state),
                    cell(state.validation_state),
                    f"`{cell(superseded_value(state))}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Required per-topic sequence",
            "",
            "1. Basic learning session.",
            "2. Basic MCQs and remediation.",
            "3. Verified PYQs and answer practice.",
            "4. Optional Advanced depth.",
            "5. Consolidated register notes.",
            "6. Validate, update tracker, refresh the global command index, then refresh these section indexes immediately.",
            "",
        ]
    )
    return "\n".join(lines)


def render_deliverable_index(
    root: Path,
    index_path: Path,
    manifest: dict[str, object],
    states: list[TopicState],
    deliverable: str,
) -> str:
    section = manifest["section"]
    is_notes = deliverable == "notes"
    title = "Notes PDF Index" if is_notes else "Workbook PDF Index"
    column = "Notes PDF" if is_notes else "Solved workbook PDF"
    lines = [
        f"# {section['name']} — {title}",
        "",
        f"> **Section key:** `{section['key']}`",
        "> This index intentionally contains only one deliverable type.",
        "",
        f"| # | Topic key | Display title | {column} | Package state | Approval | Validation | Variant / generation |",
        "|---:|---|---|---|---|---|---|---|",
    ]
    for number, state in enumerate(states, 1):
        path_value = state.notes_pdf if is_notes else state.workbook_pdf
        lines.append(
            "| "
            + " | ".join(
                [
                    str(number),
                    f"`{cell(state.topic['topic_key'])}`",
                    cell(state.topic["display_title"]),
                    path_cell(root, index_path, path_value),
                    cell(state.package_state),
                    cell(state.approval_state),
                    cell(state.validation_state),
                    cell(record_variant(state.record)),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def write_if_changed(path: Path, content: str) -> bool:
    encoded = content.replace("\r\n", "\n").encode("utf-8")
    if path.is_file() and path.read_bytes() == encoded:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encoded)
    return True


def registered_manifests(root: Path) -> list[tuple[Path, dict[str, object]]]:
    directory = root / "upsc-ai-kit" / "manifests" / "v2"
    manifests: list[tuple[Path, dict[str, object]]] = []
    if not directory.is_dir():
        return manifests
    ignored = {
        "section-manifest.schema.json",
        "section-manifest.template.json",
        "topic-catalog.json",
        "topic-catalog.schema.json",
    }
    for path in sorted(directory.glob("*.json"), key=lambda item: item.name.casefold()):
        if path.name.casefold() in ignored:
            continue
        raw = json.loads(path.read_text(encoding="utf-8"))
        if str((raw.get("section") or {}).get("scope") or "").strip().casefold() not in {
            "official-section",
            "pilot",
        }:
            continue
        manifests.append((path, load_manifest(path)))
    return sorted(
        manifests,
        key=lambda item: (
            str(item[1]["subject"].get("display_name") or item[1]["subject"]["key"]).casefold(),
            str(item[1]["section"]["name"]).casefold(),
            str(item[1]["section"]["key"]).casefold(),
            item[0].name.casefold(),
        ),
    )


def guide_link(root: Path, path: Path) -> str:
    relative = path.relative_to(root).as_posix()
    return f"[`{windows_path(relative)}`]({quote(relative, safe='/#-_.~')})"


def section_kind(section: dict[str, object]) -> str:
    if section.get("scope") == "pilot":
        return "Pilot"
    if section.get("complete_syllabus_section"):
        return "Full"
    return "Full (boundary pending)"


def section_command(
    subject_name: str,
    section_name: str,
    suffix: str | None = None,
) -> str:
    command = f"Generate learner-v2 section: {subject_name} — {section_name}"
    return f"{command} — {suffix}" if suffix else command


def topic_command(
    subject_name: str,
    section_name: str,
    topic_title: str,
    suffix: str | None = None,
) -> str:
    command = (
        f"Generate learner-v2 topic: {subject_name} — {section_name} — "
        f"{topic_title}"
    )
    return f"{command} — {suffix}" if suffix else command


def batch_command(
    subject_name: str,
    section_name: str,
    suffix: str | None = None,
) -> str:
    command = (
        f"Generate next 10 learner-v2 topics: {subject_name} — {section_name}"
    )
    return f"{command} — {suffix}" if suffix else command


def quick_topic_command(
    subject_name: str,
    section_name: str,
    topic_title: str,
    state: TopicState,
) -> str:
    suffix = None if state.package_state == "planned" else "Regenerate"
    return topic_command(subject_name, section_name, topic_title, suffix)


def command_state(state: TopicState) -> tuple[str, str]:
    if state.package_state == "approved":
        return "approved", "completed, approved"
    if state.package_state == "generated":
        return "generated", "completed, unapproved"
    if state.package_state == "incomplete":
        return (
            "generated",
            "incomplete or validation failed; regeneration/finalisation required",
        )
    return "planned", "not generated"


def command_topic_titles(states: list[TopicState]) -> dict[str, str]:
    title_counts: dict[str, int] = {}
    for state in states:
        title = str(state.topic["display_title"])
        title_counts[title] = title_counts.get(title, 0) + 1
    return {
        str(state.topic["topic_key"]): (
            str(state.topic["display_title"])
            if title_counts[str(state.topic["display_title"])] == 1
            else (
                f"{state.topic['display_title']} "
                f"[topic key: {state.topic['topic_key']}]"
            )
        )
        for state in states
    }


def load_topic_catalog(root: Path) -> dict[str, object] | None:
    path = root / TOPIC_CATALOG_FILE
    if not path.is_file():
        return None
    try:
        catalog = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ManifestError(f"Topic catalogue is not valid JSON: {exc}") from exc
    if catalog.get("schema_version") != 1:
        raise ManifestError("Topic catalogue schema_version must be 1.")
    if catalog.get("variant") != V2_VARIANT:
        raise ManifestError("Topic catalogue variant must be learner-v2.")
    topics = catalog.get("topics")
    if not isinstance(topics, list):
        raise ManifestError("Topic catalogue topics must be a list.")
    topic_keys: set[str] = set()
    commands: set[str] = set()
    for position, topic in enumerate(topics, 1):
        if not isinstance(topic, dict):
            raise ManifestError(f"Topic catalogue entry {position} must be an object.")
        for field in (
            "subject",
            "section",
            "topic_key",
            "topic_order",
            "display_title",
            "learner_v2_command",
            "discovery_status",
        ):
            if field not in topic:
                raise ManifestError(
                    f"Topic catalogue entry {position} is missing {field}."
                )
        key = str(topic["topic_key"])
        command = str(topic["learner_v2_command"])
        if key in topic_keys:
            raise ManifestError(f"Duplicate topic_key in topic catalogue: {key}")
        if command in commands:
            raise ManifestError(f"Duplicate command in topic catalogue: {command}")
        topic_keys.add(key)
        commands.add(command)
        for field in ("source_basic", "source_canonical", "source_advanced"):
            value = topic.get(field)
            if value and not repo_path(root, str(value)).is_file():
                raise ManifestError(
                    f"Topic catalogue path does not exist for {key}: {value}"
                )
        for field in ("syllabus_sources", "index_sources"):
            values = topic.get(field, [])
            if not isinstance(values, list):
                raise ManifestError(f"Topic catalogue {key} {field} must be a list.")
            for value in values:
                if not repo_path(root, str(value)).is_file():
                    raise ManifestError(
                        f"Topic catalogue path does not exist for {key}: {value}"
                    )
    return catalog


def catalog_topic_sort_key(topic: dict[str, object]) -> tuple[object, ...]:
    return (
        int(topic["subject"].get("order") or 0),
        int(topic["section"].get("order") or 0),
        int(topic.get("topic_order") or 0),
        str(topic["topic_key"]).casefold(),
    )


def catalog_topic_generated(
    topic: dict[str, object],
    records: list[dict[str, object]],
) -> bool:
    return latest_record(topic, records) is not None


def catalog_topic_state(
    root: Path,
    topic: dict[str, object],
    records: list[dict[str, object]],
) -> tuple[str, dict[str, object] | None, tuple[str, ...]]:
    record = latest_record(topic, records)
    if record is None:
        return "planned", None, ()
    missing = tuple(
        label
        for label, field in (
            ("assembled Markdown", "markdown"),
            ("notes PDF", "main_pdf"),
            ("workbook PDF", "workbook"),
        )
        if not record.get(field)
        or "<YYYY-MM-DD>" in str(record[field])
        or not repo_path(root, str(record[field])).is_file()
    )
    if missing or not validation_passed(record):
        return "incomplete", record, missing
    return "completed", record, ()


def resolve_catalog_section(
    catalog: dict[str, object],
    subject_query: str,
    section_query: str,
) -> tuple[dict[str, object], dict[str, object], list[dict[str, object]]]:
    ready = [
        topic
        for topic in catalog["topics"]
        if topic.get("discovery_status") == "source-ready"
        and topic.get("source_canonical")
    ]
    subjects: dict[str, dict[str, object]] = {}
    for topic in ready:
        subject = topic["subject"]
        subjects.setdefault(str(subject["key"]), subject)

    def matches(query: str, *values: object) -> bool:
        normalized = query.strip().casefold()
        query_slug = slugify(query)
        return any(
            normalized == str(value).strip().casefold()
            or query_slug == slugify(str(value))
            for value in values
        )

    subject_matches = [
        subject
        for subject in subjects.values()
        if matches(subject_query, subject["key"], subject["display_name"])
    ]
    if not subject_matches:
        available = ", ".join(
            str(subject["display_name"])
            for subject in sorted(
                subjects.values(),
                key=lambda item: (
                    int(item.get("order") or 0),
                    str(item["display_name"]).casefold(),
                ),
            )
        )
        raise ManifestError(
            f"No catalogue subject exactly matches {subject_query!r}. "
            f"Available subjects: {available}"
        )
    if len(subject_matches) > 1:
        choices = ", ".join(
            f"{subject['display_name']} ({subject['key']})"
            for subject in subject_matches
        )
        raise ManifestError(
            f"Ambiguous catalogue subject {subject_query!r}: {choices}"
        )
    subject = subject_matches[0]
    subject_topics = [
        topic
        for topic in ready
        if str(topic["subject"]["key"]) == str(subject["key"])
    ]
    sections: dict[str, dict[str, object]] = {}
    for topic in subject_topics:
        section = topic["section"]
        sections.setdefault(str(section["key"]), section)
    section_matches = [
        section
        for section in sections.values()
        if matches(section_query, section["key"], section["name"])
    ]
    if not section_matches:
        available = ", ".join(
            f"{section['name']} ({section['key']})"
            for section in sorted(
                sections.values(),
                key=lambda item: (
                    int(item.get("order") or 0),
                    str(item["name"]).casefold(),
                ),
            )
        )
        raise ManifestError(
            f"No section in {subject['display_name']} exactly matches "
            f"{section_query!r}. Available sections: {available}"
        )
    if len(section_matches) > 1:
        choices = ", ".join(
            f"{section['name']} ({section['key']})"
            for section in section_matches
        )
        raise ManifestError(
            f"Ambiguous section {section_query!r} in "
            f"{subject['display_name']}: {choices}"
        )
    section = section_matches[0]
    topics = sorted(
        [
            topic
            for topic in subject_topics
            if str(topic["section"]["key"]) == str(section["key"])
        ],
        key=catalog_topic_sort_key,
    )
    return subject, section, topics


def matching_catalog_manifest(
    root: Path,
    subject_key: str,
    section_key: str,
) -> tuple[Path, dict[str, object]] | None:
    matches = [
        (path, manifest)
        for path, manifest in registered_manifests(root)
        if str(manifest["subject"]["key"]) == subject_key
        and str(manifest["section"]["key"]) == section_key
    ]
    if len(matches) > 1:
        paths = ", ".join(str(path.relative_to(root)) for path, _ in matches)
        raise ManifestError(
            f"Ambiguous manifests for {subject_key}/{section_key}: {paths}"
        )
    return matches[0] if matches else None


def plan_catalog_topic_batch(
    root: Path,
    subject_query: str,
    section_query: str,
    *,
    count: int = 10,
    regenerate: bool = False,
    catalog: dict[str, object] | None = None,
    records: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    if count < 1:
        raise ManifestError("Batch count must be at least 1.")
    root = root.resolve()
    catalog = catalog if catalog is not None else load_topic_catalog(root)
    if catalog is None:
        raise ManifestError("The full learner-v2 topic catalogue does not exist.")
    records = (
        records
        if records is not None
        else load_tracker(root / "EXPORT-PDF-STATUS.json")
    )
    subject, section, catalog_topics = resolve_catalog_section(
        catalog,
        subject_query,
        section_query,
    )
    by_key = {
        str(topic["topic_key"]): topic
        for topic in catalog_topics
    }
    manifest_match = matching_catalog_manifest(
        root,
        str(subject["key"]),
        str(section["key"]),
    )
    if manifest_match:
        manifest_path, manifest = manifest_match
        ordered_topics = []
        for manifest_topic in manifest["topics"]:
            topic_key = str(manifest_topic["topic_key"])
            if topic_key not in by_key:
                raise ManifestError(
                    f"Manifest topic {topic_key} is absent from the source-ready "
                    "catalogue section."
                )
            ordered_topics.append(by_key[topic_key])
    else:
        manifest_path = None
        ordered_topics = catalog_topics

    selected: list[dict[str, object]] = []
    for topic in ordered_topics:
        state, record, missing = catalog_topic_state(root, topic, records)
        if state == "completed" and not regenerate:
            continue
        command = str(topic["learner_v2_command"])
        if record is not None:
            command += " — Regenerate"
        selected.append(
            {
                "topic_key": str(topic["topic_key"]),
                "display_title": str(topic["display_title"]),
                "state": state,
                "command": command,
                "missing": list(missing),
            }
        )
        if len(selected) == count:
            break

    keys = [str(topic["topic_key"]) for topic in selected]
    commands = [str(topic["command"]) for topic in selected]
    if len(keys) != len(set(keys)) or len(commands) != len(set(commands)):
        raise ManifestError("Batch plan contains duplicate topic keys or commands.")
    subject_name = str(subject["display_name"])
    section_name = str(section["name"])
    return {
        "batch_command": batch_command(
            subject_name,
            section_name,
            "Regenerate" if regenerate else None,
        ),
        "subject": {
            "key": str(subject["key"]),
            "display_name": subject_name,
        },
        "section": {
            "key": str(section["key"]),
            "name": section_name,
        },
        "manifest": (
            windows_path(manifest_path.relative_to(root))
            if manifest_path is not None
            else None
        ),
        "requested_count": count,
        "selected_count": len(selected),
        "regenerate": regenerate,
        "topics": selected,
    }


def render_full_catalog_commands(
    root: Path,
    catalog: dict[str, object],
    records: list[dict[str, object]],
) -> list[str]:
    topics = sorted(catalog["topics"], key=catalog_topic_sort_key)
    ready = [
        topic
        for topic in topics
        if topic.get("discovery_status") == "source-ready"
        and topic.get("source_canonical")
    ]
    unresolved = [topic for topic in topics if topic not in ready]
    subjects: list[tuple[dict[str, object], list[dict[str, object]]]] = []
    for topic in ready:
        subject_key = str(topic["subject"]["key"])
        if not subjects or str(subjects[-1][0]["key"]) != subject_key:
            subjects.append((topic["subject"], []))
        subjects[-1][1].append(topic)

    stats = catalog.get("statistics", {})
    lines = [
        "## Catalogue statistics",
        "",
        f"- **Subjects:** {stats.get('subjects', len(subjects))}",
        f"- **Sections:** {stats.get('sections', 0)}",
        f"- **Topics:** {stats.get('topics', len(topics))}",
        f"- **Source-ready topics / commands:** {len(ready)}",
        f"- **Ambiguous or unresolved entries:** {len(unresolved)}",
        (
            "- **Duplicate topic keys / commands:** "
            f"{stats.get('duplicate_topic_keys', 0)} / "
            f"{stats.get('duplicate_commands', 0)}"
        ),
        "",
        "## Subject table of contents",
        "",
        "| Subject | Sections | Topics |",
        "|---|---:|---:|",
    ]
    for subject, subject_topics in subjects:
        section_count = len(
            {
                str(topic["section"]["key"])
                for topic in subject_topics
            }
        )
        anchor = "subject-" + slugify(str(subject["display_name"]))
        lines.append(
            f"| [{cell(subject['display_name'])}](#{anchor}) | "
            f"{section_count} | {len(subject_topics)} |"
        )
    lines.append("")

    emitted: set[str] = set()
    for subject_number, (subject, subject_topics) in enumerate(subjects, 1):
        subject_name = str(subject["display_name"])
        anchor = "subject-" + slugify(subject_name)
        lines.extend(
            [
                f'<a id="{anchor}"></a>',
                f"## {subject_number}. {subject_name} — {len(subject_topics)} topics",
                "",
            ]
        )
        sections: list[tuple[dict[str, object], list[dict[str, object]]]] = []
        for topic in subject_topics:
            section_key = str(topic["section"]["key"])
            if not sections or str(sections[-1][0]["key"]) != section_key:
                sections.append((topic["section"], []))
            sections[-1][1].append(topic)
        for section, section_topics in sections:
            completed: list[dict[str, object]] = []
            pending: list[tuple[dict[str, object], str]] = []
            for topic in section_topics:
                state, record, _ = catalog_topic_state(root, topic, records)
                command = str(topic["learner_v2_command"])
                if record is not None:
                    command += " — Regenerate"
                if state == "completed":
                    completed.append(topic)
                else:
                    pending.append((topic, command))
            next_ten = batch_command(subject_name, str(section["name"]))
            for command in [next_ten, *(command for _, command in pending)]:
                if command in emitted:
                    raise ManifestError(
                        f"Duplicate generated catalogue command: {command}"
                    )
                if "<" in command or ">" in command:
                    raise ManifestError(
                        f"Catalogue command contains a placeholder: {command}"
                    )
                emitted.add(command)
            lines.extend(
                [
                    f"### {section['name']} (`{section['key']}`) — "
                    f"{len(section_topics)} topics",
                    "",
                    "**Next 10 — safe sequential batch:**",
                    "",
                    "```text",
                    next_ten,
                    "```",
                    "",
                    f"**Completed:** {len(completed)} / {len(section_topics)}",
                    "",
                ]
            )
            if completed:
                lines.extend(
                    f"- ✅ DONE — {topic['display_title']}"
                    for topic in completed
                )
            else:
                lines.append("- None.")
            lines.extend(
                [
                    "",
                    f"#### Pending / incomplete queue — {len(pending)} topics",
                    "",
                ]
            )
            if pending:
                lines.extend(
                    [
                        "```text",
                        *(command for _, command in pending),
                        "```",
                        "",
                    ]
                )
            else:
                lines.extend(["No planned or incomplete topics remain.", ""])
            if completed:
                regenerate_commands = [
                    f"{topic['learner_v2_command']} — Regenerate"
                    for topic in completed
                ]
                for command in regenerate_commands:
                    if command in emitted:
                        raise ManifestError(
                            f"Duplicate generated catalogue command: {command}"
                        )
                    emitted.add(command)
                lines.extend(
                    [
                        "#### Optional completed-topic regeneration",
                        "",
                        "```text",
                        *regenerate_commands,
                        "```",
                        "",
                    ]
                )

    lines.extend(["## Unresolved catalogue entries", ""])
    if not unresolved:
        lines.extend(
            [
                "None. Every catalogued topic has a usable canonical Markdown owner.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "These entries are withheld from the copy-paste command blocks until a "
                "usable owner is resolved.",
                "",
                "| Subject | Section | Topic key | Display title | Warning |",
                "|---|---|---|---|---|",
            ]
        )
        for topic in unresolved:
            lines.append(
                "| "
                + " | ".join(
                    [
                        cell(topic["subject"]["display_name"]),
                        cell(topic["section"]["name"]),
                        f"`{cell(topic['topic_key'])}`",
                        cell(topic["display_title"]),
                        cell(topic.get("ambiguity_warning") or "Unresolved owner"),
                    ]
                )
                + " |"
            )
        lines.append("")
    return lines


def render_command_guide(
    root: Path,
    manifests: list[tuple[Path, dict[str, object]]],
    records: list[dict[str, object]],
    catalog: dict[str, object] | None = None,
) -> str:
    manifest_states: list[
        tuple[Path, dict[str, object], list[TopicState]]
    ] = [
        (manifest_path, manifest, resolve_topic_states(root, manifest, records))
        for manifest_path, manifest in manifests
    ]
    lines = [
        "# Learner-v2 Subject/Section Command Index",
        "",
        "## Use",
        "",
        "For a bounded automatic run, paste the section's **Next 10** command. For manual "
        "control, copy one command from its pending queue, wait for completion, then paste "
        "the next line.",
        "",
        "Every `Generate learner-v2 topic: ...` command creates four integrated outputs: "
        "complete reusable Markdown, an indexed learning-session PDF, a separate indexed "
        "solved workbook, and the user-approved continuous at-a-glance core-first flowchart "
        "package (master image, large-format poster, same-master tiled PDF, previews and "
        "contact sheets). Every completed teaching subtopic in the learning PDF also ends "
        "with its own compact closure flow diagram before the next subtopic begins.",
        "",
    ]
    catalog = catalog if catalog is not None else load_topic_catalog(root)
    if catalog is not None:
        lines.extend(render_full_catalog_commands(root, catalog, records))
    else:
        quick_commands: set[str] = set()
        for _, manifest, states in manifest_states:
            subject = manifest["subject"]
            section = manifest["section"]
            subject_name = str(subject.get("display_name") or subject["key"])
            section_name = str(section["name"])
            titles = command_topic_titles(states)
            pending_commands = [
                quick_topic_command(
                    subject_name,
                    section_name,
                    titles[str(state.topic["topic_key"])],
                    state,
                )
                for state in states
                if state.package_state in {"planned", "incomplete"}
            ]
            completed_commands = [
                topic_command(
                    subject_name,
                    section_name,
                    titles[str(state.topic["topic_key"])],
                    "Regenerate",
                )
                for state in states
                if state.package_state in {"generated", "approved"}
            ]
            next_ten = batch_command(subject_name, section_name)
            for command in [next_ten, *pending_commands, *completed_commands]:
                if command in quick_commands:
                    raise ManifestError(f"Duplicate generated quick command: {command}")
                quick_commands.add(command)
            lines.extend(
                [
                    f"### {subject_name} — {section_name}",
                    "",
                    "**Next 10 — safe sequential batch:**",
                    "",
                    "```text",
                    next_ten,
                    "```",
                    "",
                    f"**Completed:** {len(completed_commands)} / {len(states)}",
                    "",
                ]
            )
            completed_states = [
                state
                for state in states
                if state.package_state in {"generated", "approved"}
            ]
            if completed_states:
                lines.extend(
                    f"- ✅ DONE — {state.topic['display_title']}"
                    for state in completed_states
                )
            else:
                lines.append("- None.")
            lines.extend(
                [
                    "",
                    f"#### Pending / incomplete queue — {len(pending_commands)} topics",
                    "",
                ]
            )
            if pending_commands:
                lines.extend(["```text", *pending_commands, "```", ""])
            else:
                lines.extend(["No planned or incomplete topics remain.", ""])
            if completed_commands:
                lines.extend(
                    [
                        "#### Optional completed-topic regeneration",
                        "",
                        "```text",
                        *completed_commands,
                        "```",
                        "",
                    ]
                )
        if not manifest_states:
            lines.extend(["No registered sections.", ""])
    lines.extend(
        [
        "## Detailed reference — optional",
        "",
        "> **This is the authoritative human-facing file to follow when giving "
        "section-generation instructions.** The JSON manifests under "
        "`upsc-ai-kit\\manifests\\v2\\` are machine-readable plans; they are not the "
        "user command guide.",
        "",
        "> **Recommended default:** paste one topic command at a time in catalogue order "
        "(and manifest order after on-demand materialisation). Each topic command generates, "
        "validates and finalises that topic, then refreshes coverage, notes and workbook "
        "indexes before the next topic begins. For a bounded automatic run, use the exact "
        "next-ten command printed before that section's pending queue. The full-section "
        "command remains available, but it is not the recommended default.",
        "",
        "## Exact request syntax",
        "",
        "### Safe next-ten command",
        "",
        "`Generate next 10 learner-v2 topics: <Subject> — <Section name or key>`",
        "",
        "The agent resolves the catalogue and manifest, selects the next ten planned or "
        "incomplete topics in manifest order, and processes strictly one topic at a time. "
        "After each topic it validates, finalises the tracker, and refreshes the global "
        "command index plus section coverage, notes and workbook indexes. It stops "
        "immediately on the first failure or ambiguity and never marks later topics "
        "complete. If fewer than ten remain, it processes all remaining topics. Successfully "
        "generated and validated topics are excluded unless `— Regenerate` is explicitly "
        "appended. Topic approval remains false until explicit user approval.",
        "",
        "### Recommended one-topic command",
        "",
        "Use one exact learner-v2 topic command from the full catalogue above. Do not "
        "construct a command from a placeholder template.",
        "",
        "Optional suffixes may be appended exactly, only where meaningful:",
        "",
        "- `— Regenerate` — intentionally replace an existing topic generation.",
        "- `— Generate index only` — reconcile indexes without generating topic content.",
        "- `— Pause after generation before finalising` — stop for review before validation, "
        "tracker and index finalisation.",
        "",
        "### Full-section command (available, not recommended by default)",
        "",
        "Exact full-section commands appear in the registered-manifest detail below when "
        "a section manifest already exists.",
        "",
        "Section-level controls may be appended where useful:",
        "",
        "- `— Generate index only`",
        "- `— Start from topic` followed by the exact catalogue display title",
        "",
        "## Workflow and locations",
        "",
        "1. The agent resolves the topic in the full machine-readable catalogue. If its "
        "section has no registered manifest yet, the agent materialises the complete section "
        "manifest and the three external indexes on demand; the user never creates JSON "
        "manually.",
        "2. The user pastes either the next one-topic command or the bounded next-ten command. "
        "Every selected topic must be generated, validated and finalised before the next one "
        "starts, with tracker and all global/section indexes refreshed after each topic.",
        "3. A next-ten run stops at the first failure or ambiguity; it does not generate or "
        "mark later topics complete. Use the full-section command only when an unbounded batch "
        "is explicitly preferred.",
        "4. Every notes PDF has its own internal contents/session index before teaching. Every "
        "workbook PDF has its own internal workbook index before questions. Those internal "
        "page-numbered indexes are generated from headings and are independent of the external "
        "progress indexes below.",
        "5. Preferred future outputs stay separate under "
        "`notes\\<Subject>\\learning-session-v2\\<section-key>\\notes\\` and "
        "`...\\workbooks\\`. Existing pilot compatibility paths remain unmoved.",
        "6. External coverage/deliverable indexes stay under "
        "`notes\\<Subject>\\learning-session-v2\\<section-key>\\indexes\\`: "
        "`TOPIC-COVERAGE-INDEX.md`, `NOTES-PDF-INDEX.md`, and "
        "`WORKBOOK-PDF-INDEX.md`.",
        "",
        "## Registered section manifests",
        "",
        "| Subject | Section name | Section key | Pilot / full | Topics | Manifest | Coverage index | Notes index | Workbook index |",
        "|---|---|---|---|---:|---|---|---|---|",
        ]
    )
    for manifest_path, manifest, states in manifest_states:
        subject = manifest["subject"]
        section = manifest["section"]
        subject_key = str(subject["key"])
        subject_name = str(subject.get("display_name") or subject_key)
        section_key = str(section["key"])
        index_root = (
            root
            / "notes"
            / subject_key
            / "learning-session-v2"
            / section_key
            / "indexes"
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(subject_name),
                    cell(section["name"]),
                    f"`{cell(section_key)}`",
                    section_kind(section),
                    str(len(manifest["topics"])),
                    guide_link(root, manifest_path),
                    guide_link(root, index_root / INDEX_FILES[0]),
                    guide_link(root, index_root / INDEX_FILES[1]),
                    guide_link(root, index_root / INDEX_FILES[2]),
                ]
            )
            + " |"
        )
    if not manifests:
        lines.append("| — | — | — | — | 0 | — | — | — | — |")
    lines.append("")

    emitted_commands: set[str] = set()

    def append_command(label: str, command: str) -> None:
        if command in emitted_commands:
            raise ManifestError(f"Duplicate generated command: {command}")
        emitted_commands.add(command)
        lines.extend([f"{label} `{command}`", ""])

    for manifest_path, manifest, states in manifest_states:
        subject = manifest["subject"]
        section = manifest["section"]
        subject_name = str(subject.get("display_name") or subject["key"])
        section_name = str(section["name"])
        section_key = str(section["key"])
        counts = {"planned": 0, "generated": 0, "approved": 0}
        for state in states:
            label, _ = command_state(state)
            counts[label] += 1
        lines.extend(
            [
                f"## {subject_name} — {section_name}",
                "",
                f"- **Section key:** `{section_key}`",
                f"- **Manifest:** {guide_link(root, manifest_path)}",
                (
                    "- **Command states:** "
                    f"{counts['planned']} planned · {counts['generated']} generated/unapproved "
                    f"· {counts['approved']} approved"
                ),
                "",
            ]
        )
        append_command(
            "**Full-section command (available, not the recommended default):**",
            section_command(subject_name, section_name),
        )
        append_command(
            "**Generate or refresh this section's indexes only:**",
            section_command(subject_name, section_name, "Generate index only"),
        )
        resumable = next(
            (
                state
                for state in states
                if state.package_state in {"planned", "incomplete"}
            ),
            None,
        )
        titles = command_topic_titles(states)
        if resumable is not None and len(states) > 1:
            append_command(
                "**Resume a full-section run from the first unfinished topic:**",
                section_command(
                    subject_name,
                    section_name,
                    (
                        "Start from topic "
                        + titles[str(resumable.topic["topic_key"])]
                    ),
                ),
            )
        lines.extend(
            [
                "### Topic states in manifest order",
                "",
            ]
        )
        for number, state in enumerate(states, 1):
            topic_key = str(state.topic["topic_key"])
            state_name, state_detail = command_state(state)
            lines.extend(
                [
                    f"#### {number}. {state.topic['display_title']}",
                    "",
                    f"- **Topic key:** `{topic_key}`",
                    f"- **Current state:** **{state_name} — {state_detail}**",
                    "",
                ]
            )
    lines.extend(
        [
            "> Regenerate the full catalogue with "
            "`python tools\\generate_v2_topic_command_catalog.py --guide`. Registered "
            "manifests remain detailed execution plans, while catalogue-only sections are "
            "materialised automatically when their first exact topic command is received.",
            "",
        ]
    )
    return "\n".join(lines)


def generate_command_guide(root: Path) -> Path:
    root = root.resolve()
    output = root / COMMAND_GUIDE_FILE
    records = load_tracker(root / "EXPORT-PDF-STATUS.json")
    write_if_changed(
        output,
        render_command_guide(
            root,
            registered_manifests(root),
            records,
            load_topic_catalog(root),
        ),
    )
    return output


def catalog_manifest_topic(topic: dict[str, object]) -> dict[str, object]:
    manifest_topic = {
        "topic_key": topic["topic_key"],
        "display_title": topic["display_title"],
        "syllabus_mapping": (
            f"{topic['section']['name']}; catalogue topic "
            f"{int(topic.get('source_number') or topic['topic_order']):02d}."
        ),
        "source_canonical": topic["source_canonical"],
        "source_advanced": topic.get("source_advanced"),
        "cross_topic_sources": [],
        "verified_pyq_sources": [],
    }
    if topic.get("source_basic"):
        manifest_topic["source_basic"] = topic["source_basic"]
    if topic.get("tracker_topic_keys"):
        manifest_topic["tracker_topic_keys"] = topic["tracker_topic_keys"]
    return manifest_topic


def catalog_section_topics(
    catalog: dict[str, object],
    subject_key: str,
    section_key: str,
) -> list[dict[str, object]]:
    return sorted(
        [
            topic
            for topic in catalog["topics"]
            if str(topic["subject"]["key"]) == subject_key
            and str(topic["section"]["key"]) == section_key
            and topic.get("discovery_status") == "source-ready"
            and topic.get("source_canonical")
        ],
        key=catalog_topic_sort_key,
    )


def resolve_catalog_topic_command(
    catalog: dict[str, object],
    command: str,
) -> tuple[dict[str, object], str | None]:
    allowed_suffixes = (
        "Regenerate",
        "Generate index only",
        "Pause after generation before finalising",
    )
    for topic in catalog["topics"]:
        base = str(topic["learner_v2_command"])
        if command == base:
            return topic, None
        for suffix in allowed_suffixes:
            if command == f"{base} — {suffix}":
                return topic, suffix
    raise ManifestError(
        "Topic command does not exactly match a source-ready catalogue entry."
    )


def materialize_catalog_section_manifest(
    root: Path,
    catalog: dict[str, object],
    target_topic: dict[str, object],
) -> Path:
    subject = target_topic["subject"]
    section = target_topic["section"]
    subject_key = str(subject["key"])
    section_key = str(section["key"])
    section_topics = catalog_section_topics(catalog, subject_key, section_key)
    if not section_topics:
        raise ManifestError(
            f"No source-ready topics exist for {subject_key}/{section_key}."
        )
    target = default_manifest_path(root, subject_key, section_key)
    existing: dict[str, object] | None = load_manifest(target) if target.is_file() else None
    existing_topics = {
        str(topic["topic_key"]): topic
        for topic in (existing or {}).get("topics", [])
    }
    syllabus_sources = sorted(
        {
            str(value)
            for topic in section_topics
            for field in ("syllabus_sources", "index_sources")
            for value in topic.get(field, [])
        },
        key=str.casefold,
    )
    manifest = {
        "schema_version": 1,
        "variant": V2_VARIANT,
        "subject": {
            "key": subject_key,
            "display_name": subject["display_name"],
        },
        "section": {
            "key": section_key,
            "name": section["name"],
            "scope": "official-section",
            "complete_syllabus_section": True,
            "syllabus_sources": syllabus_sources,
            "notes": (
                "Materialised on demand from the full learner-v2 topic catalogue. "
                "The user does not need to create or edit JSON manually."
            ),
        },
        "topics": [
            existing_topics.get(str(topic["topic_key"]))
            or catalog_manifest_topic(topic)
            for topic in section_topics
        ],
    }
    validate_manifest(manifest)
    validate_manifest_source_paths(root, manifest)
    write_if_changed(
        target,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )
    return target


def prepare_catalog_topic_command(
    root: Path,
    command: str,
    tracker_path: Path | None = None,
) -> dict[str, Path | str]:
    catalog = load_topic_catalog(root)
    if catalog is None:
        raise ManifestError("The full learner-v2 topic catalogue does not exist.")
    topic, suffix = resolve_catalog_topic_command(catalog, command)
    if topic.get("discovery_status") != "source-ready" or not topic.get(
        "source_canonical"
    ):
        raise ManifestError(
            f"Topic is unresolved and cannot be generated: {topic['topic_key']}"
        )
    manifest_path = materialize_catalog_section_manifest(root, catalog, topic)
    outputs = generate_section_indexes(root, manifest_path, tracker_path)
    return {
        "topic_key": str(topic["topic_key"]),
        "suffix": suffix or "",
        "manifest": manifest_path,
        **outputs,
    }


def generate_section_indexes(
    root: Path,
    manifest_path: Path,
    tracker_path: Path | None = None,
) -> dict[str, Path]:
    root = root.resolve()
    manifest_path = manifest_path.resolve()
    manifest = load_manifest(manifest_path)
    validate_manifest_source_paths(root, manifest)
    manifest["_manifest_path"] = windows_path(manifest_path.relative_to(root))
    subject = str(manifest["subject"]["key"])
    section_key = str(manifest["section"]["key"])
    indexes = (
        root
        / "notes"
        / subject
        / "learning-session-v2"
        / section_key
        / "indexes"
    )
    records = load_tracker((tracker_path or (root / "EXPORT-PDF-STATUS.json")).resolve())
    states = resolve_topic_states(root, manifest, records)
    outputs = {
        "coverage": indexes / INDEX_FILES[0],
        "notes": indexes / INDEX_FILES[1],
        "workbooks": indexes / INDEX_FILES[2],
    }
    write_if_changed(
        outputs["coverage"],
        render_coverage(root, outputs["coverage"], manifest, states),
    )
    write_if_changed(
        outputs["notes"],
        render_deliverable_index(root, outputs["notes"], manifest, states, "notes"),
    )
    write_if_changed(
        outputs["workbooks"],
        render_deliverable_index(
            root, outputs["workbooks"], manifest, states, "workbooks"
        ),
    )
    outputs["command_guide"] = generate_command_guide(root)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--subject")
    parser.add_argument("--section-key")
    parser.add_argument("--section-name")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument(
        "--write-manifest",
        type=Path,
        help="Write a conservatively auto-discovered manifest before generating indexes.",
    )
    parser.add_argument("--tracker", type=Path)
    parser.add_argument(
        "--guide-only",
        action="store_true",
        help="Regenerate only the root human-facing section command guide.",
    )
    parser.add_argument(
        "--topic-command",
        help=(
            "Resolve one exact learner-v2 topic command through the full catalogue, "
            "materialise its section manifest/indexes on demand, and report the topic plan."
        ),
    )
    args = parser.parse_args()

    root = args.repository_root.resolve()
    if args.topic_command:
        tracker = args.tracker
        if tracker and not tracker.is_absolute():
            tracker = root / tracker
        try:
            outputs = prepare_catalog_topic_command(
                root,
                args.topic_command,
                tracker,
            )
        except (ManifestError, json.JSONDecodeError) as exc:
            parser.error(str(exc))
        for name, value in outputs.items():
            if isinstance(value, Path):
                print(f"{name}: {value.relative_to(root)}")
            elif value:
                print(f"{name}: {value}")
        return 0

    if args.guide_only:
        try:
            output = generate_command_guide(root)
        except (ManifestError, json.JSONDecodeError) as exc:
            parser.error(str(exc))
        print(f"command_guide: {output.relative_to(root)}")
        return 0

    manifest_path = args.manifest
    if manifest_path and not manifest_path.is_absolute():
        manifest_path = root / manifest_path

    if manifest_path is None:
        if not args.subject or not args.section_key or not args.section_name:
            parser.error(
                "--subject, --section-key and --section-name are required when "
                "--manifest is omitted."
            )
        default = default_manifest_path(root, args.subject, args.section_key)
        if default.is_file() and not args.write_manifest:
            manifest_path = default
        else:
            try:
                manifest = build_discovered_manifest(
                    root,
                    args.subject,
                    args.section_key,
                    args.section_name,
                )
            except (ManifestError, AmbiguousDiscoveryError) as exc:
                parser.error(str(exc))
            manifest_path = args.write_manifest or default
            if not manifest_path.is_absolute():
                manifest_path = root / manifest_path
            manifest_path.parent.mkdir(parents=True, exist_ok=True)
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    try:
        manifest = load_manifest(manifest_path)
        if args.subject and slugify(str(manifest["subject"]["key"])) != slugify(args.subject):
            raise ManifestError("--subject does not match manifest subject.key.")
        if args.section_key and manifest["section"]["key"] != args.section_key:
            raise ManifestError("--section-key does not match manifest section.key.")
        if args.section_name and manifest["section"]["name"] != args.section_name:
            raise ManifestError("--section-name does not match manifest section.name.")
        tracker_path = args.tracker
        if tracker_path and not tracker_path.is_absolute():
            tracker_path = root / tracker_path
        outputs = generate_section_indexes(root, manifest_path, tracker_path)
    except (ManifestError, AmbiguousDiscoveryError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    for label, path in outputs.items():
        print(f"{label}: {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
