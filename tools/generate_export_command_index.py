"""Generate copy-paste PDF export commands from knowledge-base topic indexes."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge"
OUTPUT = ROOT / "EXPORT-PDF-COMMAND-INDEX.md"
STATUS_FILE = ROOT / "EXPORT-PDF-STATUS.json"

LEGACY_VARIANT = "legacy-v1"
V2_VARIANT = "learner-v2"

SUBJECTS = [
    ("Ancient-Indian-History", "Ancient History"),
    ("Medieval-Indian-History", "Medieval History"),
    ("Modern-Indian-History", "Modern History"),
    ("World-History", "World History"),
    ("Indian-Art-and-Culture", "Indian Art and Culture"),
    ("Geography", "Geography"),
    ("Indian-Society", "Indian Society"),
    ("Polity", "Polity"),
    ("Governance", "Governance"),
    ("Social-Justice", "Social Justice"),
    ("International-Relations", "International Relations"),
    ("Economy", "Economy"),
    ("Environment-and-Ecology", "Environment and Ecology"),
    ("Science-and-Technology", "Science and Technology"),
    ("Internal-Security", "Internal Security"),
    ("Disaster-Management", "Disaster Management"),
    ("Ethics", "Ethics"),
    ("Political-Theory", "Political Theory"),
    ("Essay", "Essay"),
    ("CSAT", "CSAT"),
    ("Qualifying-English", "Qualifying English"),
    ("Qualifying-Hindi", "Qualifying Hindi"),
]

SUPPLEMENTAL_TOPICS = {
    "Polity": [
        (50, "Concept of the Constitution"),
        (51, "Rights and Liabilities of the Government"),
        (52, "NCRWC and Working of the Constitution"),
        (53, "Special Provisions Relating to Certain Classes"),
        (54, "Lok Adalats and Other Courts"),
        (55, "Constitutional Interpretation Doctrines"),
    ],
}

PHILOSOPHY_BLOCKS = [
    (
        "Philosophy Paper I — Western Philosophy",
        [
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
        ],
    ),
    (
        "Philosophy Paper I — Indian Philosophy",
        [
            "Carvaka",
            "Jainism",
            "Schools of Buddhism",
            "Nyaya–Vaisesika",
            "Samkhya",
            "Yoga",
            "Mimamsa",
            "Schools of Vedanta",
            "Aurobindo",
        ],
    ),
    (
        "Philosophy Paper II — Socio-Political Philosophy",
        [
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
        ],
    ),
    (
        "Philosophy Paper II — Philosophy of Religion",
        [
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
        ],
    ),
]

DISPLAY_TO_FOLDER = {display: folder for folder, display in SUBJECTS}


def slugify(value: str) -> str:
    value = value.casefold().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def topic_key(folder: str, number: int | str) -> str:
    """Return the stable, path-safe identity for a standard syllabus topic."""
    return f"{slugify(folder)}-{int(number):02d}"


def philosophy_topic_key(block: str, number: int | str) -> str:
    """Return a stable identity where topic numbers repeat across Philosophy blocks."""
    return f"{slugify(block)}-{int(number):02d}"


def parse_command_identity(command: str) -> tuple[str, int] | None:
    match = re.match(r"^Export PDF for (.+) (\d{2}) — .+$", command)
    if not match:
        return None
    prefix, raw_number = match.groups()
    number = int(raw_number)
    if prefix in DISPLAY_TO_FOLDER:
        return topic_key(DISPLAY_TO_FOLDER[prefix], number), number
    if prefix in {block for block, _ in PHILOSOPHY_BLOCKS}:
        return philosophy_topic_key(prefix, number), number
    return None


def infer_topic_key(entry: dict[str, object]) -> str:
    existing = entry.get("topic_key")
    if existing:
        return str(existing)
    parsed = parse_command_identity(str(entry.get("command", "")))
    if parsed:
        return parsed[0]
    raise ValueError(
        "Export record has no topic_key and its command cannot be mapped: "
        f"{entry.get('command')!r}"
    )


def record_identity(entry: dict[str, object]) -> tuple[str, str, int]:
    return (
        infer_topic_key(entry),
        str(entry.get("variant") or LEGACY_VARIANT),
        int(entry.get("generation") or 1),
    )


def index_status_records(
    data: dict[str, object],
) -> dict[tuple[str, str, int], dict[str, object]]:
    """Index records by topic + variant + generation, never by command alone."""
    statuses: dict[tuple[str, str, int], dict[str, object]] = {}
    for entry in data.get("exports", []):
        if not isinstance(entry, dict):
            continue
        identity = record_identity(entry)
        if identity in statuses:
            raise ValueError(
                "Duplicate export identity "
                f"{identity[0]} / {identity[1]} / generation {identity[2]}"
            )
        statuses[identity] = entry
    return statuses


def clean_title(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "").replace("**", "").replace("*", "")
    value = re.sub(r"<br\s*/?>.*", "", value, flags=re.I)
    return re.sub(r"\s+", " ", value).strip(" |")


def read_topic_table(subject_dir: Path) -> list[tuple[int, str]]:
    readme = subject_dir / "README.md"
    if not readme.exists():
        return []

    topics: dict[int, str] = {}
    for line in readme.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\|\s*(\d{1,2})\s*\|\s*([^|]+)\|", line)
        if not match:
            continue
        number = int(match.group(1))
        title = clean_title(match.group(2))
        if title and not re.fullmatch(r"-+", title):
            topics.setdefault(number, title)
    return sorted(topics.items())


def read_numbered_files(subject_dir: Path) -> list[tuple[int, str]]:
    topics: dict[int, str] = {}
    for tier in ("basic", "advanced"):
        tier_dir = subject_dir / tier
        if not tier_dir.exists():
            continue
        for path in tier_dir.glob("*.md"):
            match = re.match(r"^(\d{2})_(.+)\.md$", path.name)
            if match:
                topics.setdefault(
                    int(match.group(1)),
                    clean_title(match.group(2).replace("-", " ")),
                )
    return sorted(topics.items())


def title_tokens(value: str) -> set[str]:
    ignored = {"and", "the", "of", "in", "to", "for", "with"}
    return {
        token
        for token in re.findall(r"[a-z0-9]+", value.casefold())
        if token not in ignored
    }


def compatible_topic_title(index_title: str, owner_title: str) -> bool:
    index_tokens = title_tokens(index_title)
    owner_tokens = title_tokens(owner_title)
    if not index_tokens or not owner_tokens:
        return False
    overlap = len(index_tokens & owner_tokens)
    return overlap / min(len(index_tokens), len(owner_tokens)) >= 0.5


def subject_topics(folder: str) -> list[tuple[int, str]]:
    subject_dir = KNOWLEDGE / folder
    readme_topics = dict(read_topic_table(subject_dir))
    file_topics = read_numbered_files(subject_dir)

    # Numbered owner files define the actual syllabus units. The README may provide
    # a richer title for the same number, but unrelated numbered tables must not
    # create phantom topics (the former CSAT index did this).
    if file_topics:
        topics = [
            (
                number,
                readme_topics[number]
                if number in readme_topics
                and compatible_topic_title(readme_topics[number], title)
                else title,
            )
            for number, title in file_topics
        ]
    else:
        topics = sorted(readme_topics.items())

    merged = {number: title for number, title in topics}
    for number, title in SUPPLEMENTAL_TOPICS.get(folder, []):
        merged.setdefault(number, title)
    return sorted(merged.items())


def load_statuses(
    status_file: Path = STATUS_FILE,
) -> dict[tuple[str, str, int], dict[str, object]]:
    if not status_file.exists():
        return {}

    data = json.loads(status_file.read_text(encoding="utf-8"))
    return index_status_records(data)


def resolved_status(
    entry: dict[str, object] | None,
    *,
    root: Path = ROOT,
) -> tuple[str, list[str]]:
    if not entry:
        return "remaining", []

    missing = []
    for field in ("main_pdf", "workbook", "markdown"):
        relative_path = entry.get(field)
        if not relative_path or not (root / str(relative_path)).exists():
            missing.append(field)

    if missing:
        return "incomplete", missing
    approval = entry.get("approval")
    approved = (
        approval.get("approved")
        if isinstance(approval, dict)
        else entry.get("approved")
    )
    if approved:
        return "approved", []
    return "generated", []


def status_records_by_id(
    statuses: dict[tuple[str, str, int], dict[str, object]],
) -> dict[str, tuple[tuple[str, str, int], dict[str, object]]]:
    return {
        str(entry["record_id"]): (identity, entry)
        for identity, entry in statuses.items()
        if entry.get("record_id")
    }


def record_lineage_topics(
    identity: tuple[str, str, int],
    entry: dict[str, object],
    by_record_id: dict[
        str, tuple[tuple[str, str, int], dict[str, object]]
    ],
) -> set[str]:
    topics = {identity[0]}
    reference = entry.get("supersedes")
    seen: set[str] = set()
    while reference and str(reference) not in seen:
        raw_reference = str(reference)
        seen.add(raw_reference)
        parent = by_record_id.get(raw_reference)
        if parent:
            parent_identity, parent_entry = parent
            topics.add(parent_identity[0])
            reference = parent_entry.get("supersedes")
            continue
        stable_match = re.match(
            r"^(.+?):(?:legacy-v1|learner-v2):g\d+$",
            raw_reference,
        )
        topics.add(stable_match.group(1) if stable_match else raw_reference)
        break
    return topics


def records_for(
    topic: str,
    statuses: dict[tuple[str, str, int], dict[str, object]],
    variant: str,
) -> list[tuple[int, dict[str, object]]]:
    by_record_id = status_records_by_id(statuses)
    records = [
        (identity[2], entry)
        for identity, entry in statuses.items()
        if identity[1] == variant
        and topic in record_lineage_topics(identity, entry, by_record_id)
    ]
    return sorted(records, key=lambda item: item[0], reverse=True)


def latest_state(
    topic: str,
    statuses: dict[tuple[str, str, int], dict[str, object]],
    variant: str,
) -> str:
    records = records_for(topic, statuses, variant)
    return resolved_status(records[0][1])[0] if records else "remaining"


def variant_history(
    topic: str,
    statuses: dict[tuple[str, str, int], dict[str, object]],
    variant: str,
) -> str:
    records = records_for(topic, statuses, variant)
    if not records:
        return "⬜ remaining"
    rendered = []
    for generation, entry in records:
        state, missing = resolved_status(entry)
        if state == "approved":
            label = "✅ approved"
        elif state == "generated":
            label = "🟡 generated; approval pending"
        elif state == "incomplete":
            label = f"⚠️ incomplete ({', '.join(missing)})"
        else:
            label = "⬜ remaining"
        rendered.append(f"g{generation} {label}")
    return "; ".join(rendered)


def status_line(
    command: str,
    key: str,
    statuses: dict[tuple[str, str, int], dict[str, object]],
) -> str:
    v2_state = latest_state(key, statuses, V2_VARIANT)
    checkbox = "x" if v2_state == "approved" else " "
    state_icon = {
        "approved": "✅",
        "generated": "🟡",
        "incomplete": "⚠️",
        "remaining": "⬜",
    }[v2_state]
    return (
        f"- [{checkbox}] {state_icon} `{command}` — `{key}` · "
        f"**learner-first v2:** {variant_history(key, statuses, V2_VARIANT)} · "
        f"**legacy/reference v1:** {variant_history(key, statuses, LEGACY_VARIANT)}"
    )


def render_subject(
    folder: str,
    display: str,
    topics: list[tuple[int, str]],
    statuses: dict[tuple[str, str, int], dict[str, object]],
    totals: dict[str, int],
) -> list[str]:
    if not topics:
        return []
    first, last = topics[0][0], topics[-1][0]
    commands = [
        (number, title, f"Export PDF for {display} {number:02d} — {title}")
        for number, title in topics
    ]
    subject_counts = {key: 0 for key in totals}
    resolved = []
    for number, title, command in commands:
        key = topic_key(folder, number)
        status = latest_state(key, statuses, V2_VARIANT)
        subject_counts[status] += 1
        totals[status] += 1
        resolved.append((number, title, command, key))

    lines = [
        f"## {display} ({first:02d}–{last:02d}; {len(topics)} topics)",
        "",
        (
            f"**Learner-first v2 progress:** {subject_counts['approved']} approved · "
            f"{subject_counts['generated']} generated awaiting approval · "
            f"{subject_counts['incomplete']} incomplete · "
            f"{subject_counts['remaining']} remaining"
        ),
        "",
    ]
    for _, _, command, key in resolved:
        lines.append(status_line(command, key, statuses))
    lines.append("")
    return lines


def render_philosophy(
    statuses: dict[tuple[str, str, int], dict[str, object]],
    totals: dict[str, int],
) -> list[str]:
    lines = [
        "# Philosophy Optional",
        "",
        "> Every Philosophy export command uses the five-layer format: SIMPLE START -> "
        "CORE UPSC -> ADVANCED -> EXAM APPLICATION -> RAPID REVISION.",
        "> For a single layered notes PDF plus Markdown, use "
        "`Philosophy Notes: <Topic>`. For the full package, use any command below "
        "or `Export Philosophy PDF: <Topic>`.",
        "",
    ]
    for display, titles in PHILOSOPHY_BLOCKS:
        commands = [
            f"Export PDF for {display} {number:02d} — {title}"
            for number, title in enumerate(titles, 1)
        ]
        block_counts = {key: 0 for key in totals}
        resolved = []
        for number, command in enumerate(commands, 1):
            key = philosophy_topic_key(display, number)
            status = latest_state(key, statuses, V2_VARIANT)
            block_counts[status] += 1
            totals[status] += 1
            resolved.append((command, key))

        lines.extend(
            [
                f"## {display} (01–{len(titles):02d}; {len(titles)} topics)",
                "",
                (
                    f"**Learner-first v2 progress:** {block_counts['approved']} approved · "
                    f"{block_counts['generated']} generated awaiting approval · "
                    f"{block_counts['incomplete']} incomplete · "
                    f"{block_counts['remaining']} remaining"
                ),
                "",
            ]
        )
        for command, key in resolved:
            lines.append(status_line(command, key, statuses))
        lines.append("")
    return lines


def syllabus_topic_keys() -> set[str]:
    keys = {
        topic_key(folder, number)
        for folder, _ in SUBJECTS
        for number, _ in subject_topics(folder)
    }
    keys.update(
        philosophy_topic_key(block, number)
        for block, titles in PHILOSOPHY_BLOCKS
        for number in range(1, len(titles) + 1)
    )
    return keys


def tracker_variant_counts(
    statuses: dict[tuple[str, str, int], dict[str, object]],
) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for _, variant, _ in statuses:
        counts[variant] += 1
    return dict(counts)


def main() -> None:
    statuses = load_statuses()
    variant_counts = tracker_variant_counts(statuses)
    totals = {
        "approved": 0,
        "generated": 0,
        "remaining": 0,
        "incomplete": 0,
    }
    lines = [
        "# UPSC Topic PDF Export Command Index",
        "",
        "Learner-first v2 is the default for new exports. Start a subject section by",
        "creating/reviewing its section manifest and topic-coverage index; then generate",
        "the listed topics sequentially unless interrupted. The individual commands below",
        "remain available for targeted runs, retries and explicit topic approval tracking.",
        "The topic number and title are both included to prevent numbering ambiguity.",
        "New exports use the learner-first v2",
        "sequence: Basic learning session -> Basic MCQs/remediation -> PYQs and answer",
        "practice -> OPTIONAL ADVANCED DEPTH -> consolidated register notes.",
        "",
        "Each tracker row is keyed by `topic_key + variant + generation`; command text is",
        "display-only and cannot make v1 and v2 collide. The checkbox reflects the latest",
        "**learner-first v2** generation. Existing packages remain visible as",
        "**legacy/reference v1** and keep their own approval state.",
        "",
        "**Status legend:**",
        "",
        "- [x] ✅ Learner-first v2 approved — explicit approval for that v2 generation.",
        "- [ ] 🟡 Learner-first v2 generated — all deliverables exist; approval is pending.",
        "- [ ] ⚠️ Learner-first v2 incomplete — a recorded deliverable is missing.",
        "- [ ] ⬜ Learner-first v2 remaining — no v2 generation is recorded.",
        "- Legacy/reference v1 status is shown separately and never transfers approval to v2.",
        "",
        "> Export state is stored in `EXPORT-PDF-STATUS.json`, so regeneration does not",
        "> erase ticks. Only explicit user approval should set `approved` to `true`.",
        "> Regenerate with `python tools\\generate_export_command_index.py` whenever a",
        "> package is generated, approved, or a subject index changes.",
        "> Regenerate the active section's three indexes with",
        "> `python tools\\generate_v2_section_indexes.py --manifest <manifest.json>`.",
        "",
        "# General Studies, Essay and Qualifying Papers",
        "",
    ]

    total = 0
    missing = []
    for folder, display in SUBJECTS:
        topics = subject_topics(folder)
        if not topics:
            missing.append(folder)
            continue
        total += len(topics)
        lines.extend(render_subject(folder, display, topics, statuses, totals))

    philosophy_count = sum(len(titles) for _, titles in PHILOSOPHY_BLOCKS)
    total += philosophy_count
    lines.extend(render_philosophy(statuses, totals))
    lines.extend(
        [
            "# Index Summary",
            "",
            f"- **Total copy-paste commands:** {total}",
            f"- **Learner-first v2 approved:** {totals['approved']}",
            f"- **Learner-first v2 generated awaiting approval:** {totals['generated']}",
            f"- **Learner-first v2 incomplete:** {totals['incomplete']}",
            f"- **Learner-first v2 remaining:** {totals['remaining']}",
            f"- **Legacy/reference v1 records:** {variant_counts.get(LEGACY_VARIANT, 0)}",
            f"- **Learner-first v2 records:** {variant_counts.get(V2_VARIANT, 0)}",
            f"- **General/qualifying subject sections:** {len(SUBJECTS) - len(missing)}",
            f"- **Philosophy syllabus blocks:** {len(PHILOSOPHY_BLOCKS)}",
        ]
    )
    if missing:
        lines.append(f"- **Indexes requiring manual review:** {', '.join(missing)}")
    else:
        lines.append("- **Indexes requiring manual review:** None")

    known_keys = syllabus_topic_keys()
    by_record_id = status_records_by_id(statuses)
    orphaned = sorted(
        identity
        for identity, entry in statuses.items()
        if not (record_lineage_topics(identity, entry, by_record_id) & known_keys)
    )
    lines.append(f"- **Recorded generations outside the current syllabus map:** {len(orphaned)}")
    if orphaned:
        lines.extend(
            [
                "",
                "## Recorded generations outside the current syllabus map",
                "",
                *[
                    f"- `{topic}` · `{variant}` · generation {generation}"
                    for topic, variant, generation in orphaned
                ],
            ]
        )
    lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Index saved: {OUTPUT}")
    print(f"Commands: {total}")


if __name__ == "__main__":
    main()
