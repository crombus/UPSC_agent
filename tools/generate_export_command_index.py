"""Generate copy-paste PDF export commands from knowledge-base topic indexes."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge"
OUTPUT = ROOT / "EXPORT-PDF-COMMAND-INDEX.md"
STATUS_FILE = ROOT / "EXPORT-PDF-STATUS.json"

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
    for tier in ("advanced", "basic"):
        tier_dir = subject_dir / tier
        if not tier_dir.exists():
            continue
        topics = {}
        for path in tier_dir.glob("*.md"):
            match = re.match(r"^(\d{2})_(.+)\.md$", path.name)
            if match:
                topics[int(match.group(1))] = clean_title(
                    match.group(2).replace("-", " ")
                )
        if topics:
            return sorted(topics.items())
    return []


def subject_topics(folder: str) -> list[tuple[int, str]]:
    subject_dir = KNOWLEDGE / folder
    topics = read_topic_table(subject_dir)
    file_topics = read_numbered_files(subject_dir)

    # Prefer the topic map, but use numbered files when the README has no complete map.
    if file_topics and len(file_topics) > len(topics):
        topics = file_topics

    merged = {number: title for number, title in topics}
    for number, title in SUPPLEMENTAL_TOPICS.get(folder, []):
        merged.setdefault(number, title)
    return sorted(merged.items())


def load_statuses() -> dict[str, dict[str, object]]:
    if not STATUS_FILE.exists():
        return {}

    data = json.loads(STATUS_FILE.read_text(encoding="utf-8"))
    return {
        entry["command"]: entry
        for entry in data.get("exports", [])
        if isinstance(entry, dict) and entry.get("command")
    }


def resolved_status(
    command: str, statuses: dict[str, dict[str, object]]
) -> tuple[str, list[str]]:
    entry = statuses.get(command)
    if not entry:
        return "remaining", []

    missing = []
    for field in ("main_pdf", "workbook", "markdown"):
        relative_path = entry.get(field)
        if not relative_path or not (ROOT / str(relative_path)).exists():
            missing.append(field)

    if missing:
        return "incomplete", missing
    if entry.get("approved"):
        return "approved", []
    return "generated", []


def status_line(command: str, status: str) -> str:
    if status == "approved":
        return f"- [x] ✅ `{command}`"
    if status == "generated":
        return f"- [ ] 🟡 `{command}`"
    if status == "incomplete":
        return f"- [ ] ⚠️ `{command}`"
    return f"- [ ] ⬜ `{command}`"


def render_subject(
    display: str,
    topics: list[tuple[int, str]],
    statuses: dict[str, dict[str, object]],
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
        status, _ = resolved_status(command, statuses)
        subject_counts[status] += 1
        totals[status] += 1
        resolved.append((number, title, command, status))

    lines = [
        f"## {display} ({first:02d}–{last:02d}; {len(topics)} topics)",
        "",
        (
            f"**Progress:** {subject_counts['approved']} approved · "
            f"{subject_counts['generated']} generated awaiting approval · "
            f"{subject_counts['remaining']} remaining"
        ),
        "",
    ]
    for _, _, command, status in resolved:
        lines.append(status_line(command, status))
    lines.append("")
    return lines


def render_philosophy(
    statuses: dict[str, dict[str, object]], totals: dict[str, int]
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
        for command in commands:
            status, _ = resolved_status(command, statuses)
            block_counts[status] += 1
            totals[status] += 1
            resolved.append((command, status))

        lines.extend(
            [
                f"## {display} (01–{len(titles):02d}; {len(titles)} topics)",
                "",
                (
                    f"**Progress:** {block_counts['approved']} approved · "
                    f"{block_counts['generated']} generated awaiting approval · "
                    f"{block_counts['remaining']} remaining"
                ),
                "",
            ]
        )
        for command, status in resolved:
            lines.append(status_line(command, status))
        lines.append("")
    return lines


def main() -> None:
    statuses = load_statuses()
    totals = {
        "approved": 0,
        "generated": 0,
        "remaining": 0,
        "incomplete": 0,
    }
    lines = [
        "# UPSC Topic PDF Export Command Index",
        "",
        "Copy and send **one command at a time**. The topic number and title are both",
        "included to prevent numbering ambiguity. Each command means: use the complete",
        "basic and advanced sources, create the learning-session PDF and solved workbook,",
        "retain reusable Markdown, include relevant PYQs, mark inferred Prelims answers",
        "when an official key is unavailable, and validate both PDFs before completion.",
        "",
        "**Status legend:**",
        "",
        "- [x] ✅ Approved complete — user approved all three deliverables.",
        "- [ ] 🟡 Generated — main PDF, workbook and reusable Markdown exist; approval is pending.",
        "- [ ] ⚠️ Incomplete — the status ledger references a missing deliverable.",
        "- [ ] ⬜ Remaining — no complete package is recorded.",
        "",
        "> Export state is stored in `EXPORT-PDF-STATUS.json`, so regeneration does not",
        "> erase ticks. Only explicit user approval should set `approved` to `true`.",
        "> Regenerate with `python tools\\generate_export_command_index.py` whenever a",
        "> package is generated, approved, or a subject index changes.",
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
        lines.extend(render_subject(display, topics, statuses, totals))

    philosophy_count = sum(len(titles) for _, titles in PHILOSOPHY_BLOCKS)
    total += philosophy_count
    lines.extend(render_philosophy(statuses, totals))
    lines.extend(
        [
            "# Index Summary",
            "",
            f"- **Total copy-paste commands:** {total}",
            f"- **Approved complete:** {totals['approved']}",
            f"- **Generated awaiting approval:** {totals['generated']}",
            f"- **Incomplete recorded packages:** {totals['incomplete']}",
            f"- **Remaining topics:** {totals['remaining']}",
            f"- **General/qualifying subject sections:** {len(SUBJECTS) - len(missing)}",
            f"- **Philosophy syllabus blocks:** {len(PHILOSOPHY_BLOCKS)}",
        ]
    )
    if missing:
        lines.append(f"- **Indexes requiring manual review:** {', '.join(missing)}")
    else:
        lines.append("- **Indexes requiring manual review:** None")
    lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Index saved: {OUTPUT}")
    print(f"Commands: {total}")


if __name__ == "__main__":
    main()
