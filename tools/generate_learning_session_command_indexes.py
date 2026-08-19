"""Generate copy-ready learning-session command indexes for every subject."""

from __future__ import annotations

import re
import json
from difflib import SequenceMatcher
from pathlib import Path

from generate_export_command_index import (
    PHILOSOPHY_BLOCKS,
    SUPPLEMENTAL_TOPICS,
    read_topic_table,
)


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge"
INDEX_NAME = "LEARNING-SESSION-COMMAND-INDEX.md"

SKIP_DIRECTORIES = {"_source-library", "Philosophy"}

SUBJECT_STRATEGIES = {
    "Ancient-Indian-History": "Chronology -> sources -> institutions and society -> historical debate -> maps/PYQs.",
    "Medieval-Indian-History": "Chronology -> state formation -> administration/economy -> culture -> historian debate/PYQs.",
    "Modern-Indian-History": "Chronology -> cause and consequence -> ideological strands -> personalities -> PYQs.",
    "World-History": "Timeline -> structural causes -> competing interpretations -> global consequences -> Mains answers.",
    "Polity": "Constitutional logic -> Articles and institutions -> judgments -> close-option traps -> Mains application.",
    "Political-Theory": "Concept -> thinker and argument -> criticism -> Indian application -> comparative answer.",
    "Philosophy": "Argument map -> concepts -> objections and replies -> inter-school comparison -> PYQ answer writing.",
    "Geography": "Visual process/map first -> causal mechanism -> Indian examples -> current linkage -> map/PYQ practice.",
    "Economy": "Mechanism -> indicator -> transmission channel -> policy trade-off -> current data and questions.",
    "Environment-and-Ecology": "Ecological process -> law/institution -> Indian example -> species/location traps -> current affairs.",
    "Science-and-Technology": "Scientific principle -> application -> Indian programme -> governance risks -> current affairs.",
    "International-Relations": "Background -> Indian interests -> areas of convergence/divergence -> options -> current developments.",
    "Governance": "Framework -> institution/process -> implementation gap -> evidence -> reforms and case studies.",
    "Social-Justice": "Constitutional basis -> affected group -> scheme/institution -> exclusion gap -> reforms and data.",
    "Indian-Society": "Concept -> causes -> manifestations -> data/examples -> impacts -> policy and social response.",
    "Internal-Security": "Threat architecture -> drivers -> institutions/law -> operational response -> safeguards and case studies.",
    "Disaster-Management": "Hazard-risk mechanism -> prevention/preparedness -> institutions -> response/recovery -> case study.",
    "Ethics": "Definition -> thinker/framework -> administrative example -> dilemma -> case-study application.",
    "Essay": "Theme interpretation -> dimensions -> evidence/examples -> counter-view -> coherent outline and writing drill.",
    "Indian-Art-and-Culture": "Identification features -> chronology -> regional examples -> comparison -> image/PYQ recognition.",
    "CSAT": "Concept or passage skill -> worked method -> timed drill -> error classification -> speed/accuracy retest.",
    "Qualifying-English": "Rule/skill -> worked example -> timed language exercise -> correction and retest.",
    "Qualifying-Hindi": "Rule/skill -> worked example -> timed language exercise -> correction and retest.",
}


def display_name(name: str) -> str:
    return name.replace("-", " ")


def clean_title(path: Path) -> str:
    stem = re.sub(r"^\d+_", "", path.stem)
    stem = re.sub(r"_Complete-Topic-Package$", "", stem)
    return stem.replace("-", " ").replace("_", " ").strip()


def normalized(path: Path) -> str:
    return re.sub(r"[^a-z0-9]", "", clean_title(path).lower())


def title_tokens(value: Path | str) -> set[str]:
    text = clean_title(value) if isinstance(value, Path) else value
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    ignored = {"and", "of", "the", "to", "in", "for"}
    return {
        token[:-1] if token.endswith("s") and len(token) > 4 else token
        for token in tokens
        if token not in ignored
    }


def best_match(owner: Path, candidates: list[Path]) -> Path | None:
    if not candidates:
        return None
    target = normalized(owner)
    exact = [candidate for candidate in candidates if normalized(candidate) == target]
    if exact:
        return exact[0]
    owner_tokens = title_tokens(owner)

    def score(candidate: Path) -> float:
        candidate_tokens = title_tokens(candidate)
        overlap = owner_tokens & candidate_tokens
        if not overlap:
            token_score = 0.0
        else:
            owner_coverage = len(overlap) / len(owner_tokens)
            candidate_coverage = len(overlap) / len(candidate_tokens)
            token_score = 2 * owner_coverage * candidate_coverage / (
                owner_coverage + candidate_coverage
            )
        sequence_score = SequenceMatcher(
            None, target, normalized(candidate)
        ).ratio()
        return 0.75 * token_score + 0.25 * sequence_score

    ranked = sorted(candidates, key=score, reverse=True)
    return ranked[0] if score(ranked[0]) >= 0.36 else None


def best_title_match(title: str, candidates: list[Path]) -> Path | None:
    probe = Path(re.sub(r"\s+", "-", title) + ".md")
    return best_match(probe, candidates)


def package_for_number(
    number: str, title: str, packages: list[Path]
) -> Path | None:
    numbered = [
        path
        for path in packages
        if re.match(rf"^{int(number):02d}_", path.name)
    ]
    if numbered:
        return numbered[0]
    return best_title_match(title, packages)


def ordered_subject_topics(subject: Path) -> list[tuple[str, str, Path, bool]]:
    advanced = sorted(
        path
        for path in (subject / "advanced").glob("*.md")
        if re.match(r"^\d+_", path.name)
    )
    basics = sorted((subject / "basic").glob("*.md"))
    packages = sorted(subject.glob("*Complete-Topic-Package.md"))

    listed_topics = read_topic_table(subject)
    if listed_topics:
        listed_topics.extend(SUPPLEMENTAL_TOPICS.get(subject.name, []))
        topics: list[tuple[str, str, Path, bool]] = []
        for topic_number, title in listed_topics:
            number = f"{topic_number:02d}"
            core = best_title_match(title, basics)
            if core is None:
                core = best_title_match(title, advanced)
            if core is None:
                continue
            package = package_for_number(number, title, packages)
            topics.append((number, title, core, package is not None))
        return topics

    if advanced:
        topics = []
        for advanced_path in advanced:
            match = re.match(r"^(\d+)_", advanced_path.name)
            if not match:
                continue
            number = match.group(1).zfill(2)
            core = best_match(advanced_path, basics) or advanced_path
            package = package_for_number(number, clean_title(advanced_path), packages)
            topics.append((number, clean_title(advanced_path), core, package is not None))
        existing_numbers = {int(number) for number, *_ in topics}
        for topic_number, title in SUPPLEMENTAL_TOPICS.get(subject.name, []):
            if topic_number in existing_numbers:
                continue
            number = f"{topic_number:02d}"
            core = best_title_match(title, basics)
            if core is None:
                continue
            package = package_for_number(number, title, packages)
            topics.append((number, title, core, package is not None))
        return topics

    source_files = basics or packages
    topics = []
    for index, core in enumerate(source_files, 1):
        match = re.match(r"^(\d+)_", core.name)
        number = match.group(1).zfill(2) if match else f"{index:02d}"
        package = best_match(core, packages)
        topics.append((number, clean_title(core), core, package is not None))
    return topics


def exported_commands() -> set[str]:
    status_file = ROOT / "EXPORT-PDF-STATUS.json"
    if not status_file.exists():
        return set()
    data = json.loads(status_file.read_text(encoding="utf-8"))
    return {
        entry["command"]
        for entry in data.get("exports", [])
        if isinstance(entry, dict) and entry.get("command")
    }


def philosophy_topics(subject: Path) -> list[tuple[str, str, str, Path, bool]]:
    result: list[tuple[str, str, str, Path, bool]] = []
    files = [
        path
        for path in subject.glob("paper-*/*/*.md")
        if not path.name.startswith(("_", "00_"))
        and path.name.lower() != "readme.md"
        and path.parent.name != "_themes"
    ]
    statuses = exported_commands()
    for block, titles in PHILOSOPHY_BLOCKS:
        label = block.removeprefix("Philosophy ")
        for index, title in enumerate(titles, 1):
            number = f"{index:02d}"
            owner = best_title_match(title, files)
            if owner is None:
                continue
            export_command = f"Export PDF for {block} {number} — {title}"
            result.append(
                (label, number, title, owner, export_command in statuses)
            )
    return result


def command_cell(command: str) -> str:
    return f"`{command}`"


def common_header(subject_name: str, topic_count: int) -> list[str]:
    subject_display = display_name(subject_name)
    strategy = SUBJECT_STRATEGIES.get(
        subject_name,
        "Core concept -> visual explanation -> exam distinctions -> retrieval practice -> revision.",
    )
    return [
        f"# {subject_display} Learning Session Command Index",
        "",
        f"> **Topics indexed:** {topic_count}  ",
        f"> **Subject method:** {strategy}",
        "",
        "## How to use these commands",
        "",
        f"- **Core learning:** copy `Start {subject_display} <number>`. The tutor must analyse the Core owner and cluster it into efficient 45-75 minute blocks instead of following every Markdown heading.",
        f"- **Deep mode is optional:** use `Deep {subject_display} <number>` only for a difficult concept, a direct Mains/PYQ theme, or Core-test accuracy below 70%. It is not a compulsory second reading.",
        f"- **Practice:** use `Test {subject_display} <number>` after Core learning. Answers must not be leaked before submission.",
        f"- **Revision:** use `Revise {subject_display} <number>` for the final register, error log and high-yield distinctions.",
        f"- **Resume:** use `Resume {subject_display}` to continue from saved progress.",
        f"- **Progress:** use `Progress {subject_display}` for completed blocks, accuracy and due revisions.",
        "",
        "### Learning-session rule",
        "",
        "The complete package remains the master reference. A live session should select all exam-relevant Core material, use advanced material only where it adds marks, run one genuine current-affairs check per integrated block, and end with cumulative retrieval rather than an MCQ after every small heading.",
        "",
    ]


def render_standard_subject(subject: Path) -> str:
    topics = ordered_subject_topics(subject)
    subject_display = display_name(subject.name)
    lines = common_header(subject.name, len(topics))
    lines.extend(
        [
            "## Copy-ready topic commands",
            "",
            "| No. | Topic and source status | Core learning | Optional depth | Test | Revision |",
            "|---:|---|---|---|---|---|",
        ]
    )
    for number, title, core, has_package in topics:
        status = "complete package available" if has_package else "Core owner ready"
        topic = f"**{title}**<br>{status}; `{core.relative_to(subject).as_posix()}`"
        prefix = f"{subject_display} {number}"
        lines.append(
            "| "
            + " | ".join(
                [
                    number,
                    topic,
                    command_cell(f"Start {prefix} - {title}"),
                    command_cell(f"Deep {prefix}"),
                    command_cell(f"Test {prefix}"),
                    command_cell(f"Revise {prefix}"),
                ]
            )
            + " |"
        )
    lines.extend(["", f"Use `{command_cell(f'Resume {subject_display}')[1:-1]}` to continue the subject.", ""])
    return "\n".join(lines)


def render_philosophy(subject: Path) -> str:
    topics = philosophy_topics(subject)
    lines = common_header(subject.name, len(topics))
    lines.extend(
        [
            "## Copy-ready topic commands",
            "",
            "| Section | No. | Topic and source status | Core learning | Optional depth | Test | Revision |",
            "|---|---:|---|---|---|---|---|",
        ]
    )
    for section, number, title, core, has_package in topics:
        status = "complete package available" if has_package else "canonical owner ready"
        topic = f"**{title}**<br>{status}; `{core.relative_to(subject).as_posix()}`"
        prefix = f"Philosophy {section} {number}"
        lines.append(
            "| "
            + " | ".join(
                [
                    section,
                    number,
                    topic,
                    command_cell(f"Start {prefix} - {title}"),
                    command_cell(f"Deep {prefix}"),
                    command_cell(f"Test {prefix}"),
                    command_cell(f"Revise {prefix}"),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    subjects = sorted(
        path
        for path in KNOWLEDGE.iterdir()
        if path.is_dir()
        and not path.name.startswith("_")
        and path.name not in SKIP_DIRECTORIES
    )

    master_rows: list[tuple[str, int, str]] = []
    for subject in subjects:
        if subject.name == "Philosophy":
            content = render_philosophy(subject)
            count = len(philosophy_topics(subject))
        else:
            topics = ordered_subject_topics(subject)
            if not topics:
                continue
            content = render_standard_subject(subject)
            count = len(topics)
        output = subject / INDEX_NAME
        output.write_text(content, encoding="utf-8")
        master_rows.append((display_name(subject.name), count, output.relative_to(KNOWLEDGE).as_posix()))

    master = [
        "# UPSC Learning Session Command Index",
        "",
        "Use this page to open the copy-ready command index for each subject. Each subject is handled separately because its learning unit, visual method, current-affairs burden and practice style differ.",
        "",
        "## Mode rule",
        "",
        "- `Start` is the normal learning path.",
        "- `Deep` is optional and should be used selectively, not after every session.",
        "- `Test` is closed-book practice.",
        "- `Revise` is compressed revision from register notes and the personal error log.",
        "",
        "| Subject | Topics | Command index |",
        "|---|---:|---|",
    ]
    for subject, count, path in master_rows:
        master.append(f"| {subject} | {count} | [{INDEX_NAME}]({path}) |")
    master.append("")
    (KNOWLEDGE / INDEX_NAME).write_text("\n".join(master), encoding="utf-8")

    print(f"Generated {len(master_rows)} subject indexes and one master index.")


if __name__ == "__main__":
    main()
