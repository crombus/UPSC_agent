"""Generate one deep-learning register PDF for every Polity topic.

The compiler pairs the Basic and Advanced Markdown chapters, preserves their
teaching content, and converts it into bounded visual cards accepted by
upsc_register_pdf.py.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from upsc_register_pdf import build_pdf


ROOT = Path(__file__).resolve().parents[1]
POLITY = ROOT / "upsc-ai-kit" / "knowledge" / "Polity"
BASIC_DIR = POLITY / "basic"
ADVANCED_DIR = POLITY / "advanced"
OUTPUT_DIR = ROOT / "notes" / "Polity" / "Topic-PDFs"

MAX_POINTS_PER_CARD = 7
MAX_TABLE_ROWS = 8


@dataclass
class Section:
    heading: str
    level: int
    lines: list[str] = field(default_factory=list)


def clean_inline(text: str) -> str:
    """Remove Markdown syntax that ReportLab paragraphs do not understand."""
    text = text.strip()
    text = re.sub(r"^>\s?", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("`", "")
    text = (
        text.replace("<=", "≤")
        .replace(">=", "≥")
        .replace("<->", "↔")
        .replace("->", "→")
        .replace("<-", "←")
        .replace("=>", "⇒")
    )
    text = text.replace("<", "less than ").replace(">", "greater than ")
    text = re.sub(r"^[-+*]\s+", "", text)
    text = re.sub(r"^\d+[.)]\s+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" -")


def plain_text(text: str) -> str:
    """Return text without Markdown emphasis for titles and metadata."""
    return re.sub(r"[*_#]", "", clean_inline(text)).strip()


def split_sections(markdown: str) -> tuple[str, list[Section]]:
    lines = markdown.replace("\r\n", "\n").splitlines()
    title = "Polity"
    sections: list[Section] = []
    current = Section("Core Foundation", 2)
    in_code = False

    for line in lines:
        if line.startswith("```"):
            in_code = not in_code
            current.lines.append("[DIAGRAM]" if in_code else "[/DIAGRAM]")
            continue
        if not in_code:
            match = re.match(r"^(#{1,3})\s+(.+?)\s*$", line)
            if match:
                level = len(match.group(1))
                heading = plain_text(match.group(2))
                if level == 1 and title == "Polity":
                    title = heading
                    continue
                if current.lines:
                    sections.append(current)
                current = Section(heading, level)
                continue
        current.lines.append(line.rstrip())

    if current.lines:
        sections.append(current)
    return title, sections


def is_separator_row(line: str) -> bool:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_table(lines: list[str], start: int) -> tuple[dict | None, int]:
    block = []
    index = start
    while index < len(lines) and lines[index].strip().startswith("|"):
        block.append(lines[index].strip())
        index += 1

    if len(block) < 2 or not is_separator_row(block[1]):
        return None, start + 1

    def cells(line: str) -> list[str]:
        return [clean_inline(cell) for cell in line.strip().strip("|").split("|")]

    headers = cells(block[0])
    rows = [cells(line) for line in block[2:] if not is_separator_row(line)]
    width = len(headers)
    rows = [(row + [""] * width)[:width] for row in rows]
    return {"headers": headers, "rows": rows}, index


def parse_section(section: Section) -> dict:
    points: list[str] = []
    tables: list[dict] = []
    diagrams: list[list[str]] = []
    current_paragraph: list[str] = []
    current_diagram: list[str] | None = None
    index = 0

    def flush_paragraph() -> None:
        if current_paragraph:
            text = clean_inline(" ".join(current_paragraph))
            if text and not text.startswith("Subject:") and not text.startswith("Grounded in:"):
                points.append(text)
            current_paragraph.clear()

    while index < len(section.lines):
        raw = section.lines[index]
        stripped = raw.strip()

        if stripped == "[DIAGRAM]":
            flush_paragraph()
            current_diagram = []
            index += 1
            continue
        if stripped == "[/DIAGRAM]":
            if current_diagram:
                diagrams.append(current_diagram)
            current_diagram = None
            index += 1
            continue
        if current_diagram is not None:
            if stripped:
                current_diagram.append(stripped)
            index += 1
            continue
        if stripped.startswith("|"):
            flush_paragraph()
            table, next_index = parse_table(section.lines, index)
            if table:
                tables.append(table)
                index = next_index
                continue
        if not stripped or stripped == "---":
            flush_paragraph()
            index += 1
            continue
        if re.match(r"^([-+*]|\d+[.)])\s+", stripped) or stripped.startswith(">"):
            flush_paragraph()
            text = clean_inline(stripped)
            if text and not text.startswith(("Subject:", "Grounded in:", "Companion:")):
                points.append(text)
        else:
            current_paragraph.append(stripped)
        index += 1

    flush_paragraph()
    return {"points": points, "tables": tables, "diagrams": diagrams}


def extract_trap(text: str) -> dict | None:
    if "❌" not in text and "WRONG:" not in text.upper():
        return None
    cleaned = text.replace("❌", "").strip()
    parts = re.split(r"\s*(?:->|→|—>)\s*", cleaned, maxsplit=1)
    if len(parts) == 2:
        return {"wrong": parts[0].strip(), "correct": parts[1].strip()}
    return {
        "wrong": cleaned,
        "correct": "Recheck the precise constitutional rule, exception, or institutional limit.",
    }


def diagram_steps(lines: list[str]) -> list[dict]:
    steps = []
    for line in lines:
        cleaned = plain_text(line)
        if not cleaned or re.fullmatch(r"[|+\-vV><=\s]+", cleaned):
            continue
        fragments = [
            plain_text(part)
            for part in re.split(r"\s*(?:→|->|\+--?>|=>)\s*", cleaned)
            if plain_text(part)
        ]
        for fragment in fragments:
            if fragment not in [step["title"] for step in steps]:
                steps.append({"title": fragment[:100], "text": ""})
    return steps[:7]


def classify_heading(heading: str) -> str:
    lower = heading.lower()
    if "trap" in lower:
        return "traps"
    if "mains" in lower or "pyq" in lower or "answer" in lower:
        return "mains"
    if "current" in lower or "ca hook" in lower or "news" in lower:
        return "current"
    if "timeline" in lower or "evolution" in lower or "history" in lower:
        return "timeline"
    return "theory"


def year_events(points: list[str]) -> list[dict]:
    events = []
    for point in points:
        match = re.search(r"\b(17|18|19|20)\d{2}\b", point)
        if match:
            events.append({"period": match.group(0), "event": plain_text(point)[:95]})
    return events[:6]


def make_cards(source_label: str, sections: list[Section], subject_title: str) -> list[dict]:
    cards: list[dict] = []

    for section in sections:
        parsed = parse_section(section)
        points = parsed["points"]
        tables = parsed["tables"]
        diagrams = parsed["diagrams"]
        kind = classify_heading(section.heading)

        traps = [trap for point in points if (trap := extract_trap(point))]
        narrative = [point for point in points if extract_trap(point) is None]

        if kind == "mains" and narrative:
            mains_text = " ".join(narrative)
            narrative = []
        else:
            mains_text = ""

        if kind == "current" and narrative:
            news_text = " ".join(narrative[:3])
            narrative = narrative[3:]
        else:
            news_text = ""

        # Tables are isolated and row-bounded so no table can overflow a page.
        for table_number, table in enumerate(tables, 1):
            rows = table["rows"] or [["—"] * len(table["headers"])]
            for offset in range(0, len(rows), MAX_TABLE_ROWS):
                chunk = rows[offset : offset + MAX_TABLE_ROWS]
                suffix = "" if len(rows) <= MAX_TABLE_ROWS else f" · Table {table_number}.{offset // MAX_TABLE_ROWS + 1}"
                cards.append(
                    {
                        "title": f"{source_label} · {section.heading}{suffix}",
                        "relevance": "HIGH",
                        "gs_paper": "GS-II",
                        "subject": "Indian Polity",
                        "intro": f"Structured comparison from the {source_label.lower()} source layer.",
                        "table": {"headers": table["headers"], "rows": chunk},
                        "static_link": f"{subject_title} → {section.heading}",
                    }
                )

        # Diagram blocks become genuine vector flow diagrams.
        for diagram_number, diagram in enumerate(diagrams, 1):
            steps = diagram_steps(diagram)
            if steps:
                cards.append(
                    {
                        "title": f"{source_label} · {section.heading} · Visual {diagram_number}",
                        "relevance": "HIGH",
                        "gs_paper": "GS-II",
                        "subject": "Indian Polity",
                        "intro": "Visual-first reconstruction of the source logic.",
                        "flow_diagram": {
                            "title": f"{section.heading}: Process Logic",
                            "steps": steps,
                        },
                        "static_link": f"{subject_title} → {section.heading}",
                    }
                )

        if not narrative and not traps and not mains_text and not news_text and (tables or diagrams):
            continue

        chunks = [
            narrative[index : index + MAX_POINTS_PER_CARD]
            for index in range(0, len(narrative), MAX_POINTS_PER_CARD)
        ] or [[]]

        for chunk_number, chunk in enumerate(chunks, 1):
            suffix = "" if len(chunks) == 1 else f" · Part {chunk_number}"
            title = f"{source_label} · {section.heading}{suffix}"
            card = {
                "title": title,
                "relevance": "HIGH",
                "gs_paper": "GS-II",
                "subject": "Indian Polity",
                "intro": chunk[0] if chunk else f"Exam-ready treatment of {section.heading}.",
                "origin": f"{source_label} learning layer: concepts → constitutional detail → UPSC application.",
                "static_theory": chunk[1:] if len(chunk) > 1 else [],
                "static_link": f"{subject_title} → {section.heading}",
            }

            factual = [
                point.replace("✅", "").strip()
                for point in chunk
                if "✅" in point
            ][:6]
            if factual:
                card["must_know_facts"] = factual

            if chunk_number == 1 and traps:
                card["traps"] = traps[:7]
            if chunk_number == 1 and news_text:
                card["news_trigger"] = news_text
            if chunk_number == 1 and mains_text:
                card["mains_angle"] = mains_text

            timeline = year_events(chunk)
            if kind == "timeline" and len(timeline) >= 2:
                card["visual_timeline"] = {
                    "title": f"{section.heading}: Chronology",
                    "events": timeline,
                }
            elif chunk_number == 1 and len(chunk) >= 3:
                card["concept_map"] = {
                    "title": f"{section.heading}: Recall Map",
                    "center": section.heading,
                    "branches": [
                        {"title": f"Dimension {i}", "text": plain_text(item)[:150]}
                        for i, item in enumerate(chunk[:4], 1)
                    ],
                }

            if "🔑" in " ".join(chunk):
                hooks = [point.replace("🔑", "").strip() for point in chunk if "🔑" in point]
                card["memory_hook"] = " | ".join(hooks)

            cards.append(card)

    return cards


def find_basic_file(advanced_path: Path, advanced_text: str) -> Path:
    companion = re.search(r"`basic/([^`]+\.md)`", advanced_text)
    if companion:
        candidate = BASIC_DIR / companion.group(1)
        if candidate.exists():
            return candidate

    stem = re.sub(r"^\d+_", "", advanced_path.stem)
    aliases = {
        "Centre-State-and-Inter-State-Relations": "Centre-State-Relations",
        "Governor-CM-State-Council": "Governor-and-CM",
        "High-Court-and-Subordinate-Courts": "High-Court",
        "Attorney-General-and-Advocate-General": "Attorney-General",
    }
    candidate = BASIC_DIR / f"{aliases.get(stem, stem)}.md"
    if not candidate.exists():
        raise FileNotFoundError(f"No Basic companion for {advanced_path.name}")
    return candidate


def build_one(advanced_path: Path) -> tuple[Path, int]:
    advanced_text = advanced_path.read_text(encoding="utf-8")
    basic_path = find_basic_file(advanced_path, advanced_text)
    basic_text = basic_path.read_text(encoding="utf-8")

    basic_title, basic_sections = split_sections(basic_text)
    advanced_title, advanced_sections = split_sections(advanced_text)
    subject_title = plain_text(advanced_title or basic_title)
    number_match = re.match(r"^(\d+)_", advanced_path.name)
    number = number_match.group(1) if number_match else "00"

    topics = make_cards("Foundation", basic_sections, subject_title)
    topics.extend(make_cards("Advanced", advanced_sections, subject_title))
    if not topics:
        raise ValueError(f"No renderable content found in {advanced_path.name}")

    data = {
        "document_label": "UPSC INDIAN POLITY",
        "document_tagline": "Foundation • Constitutional Depth • Prelims Traps • Mains Application",
        "title": f"{subject_title}\nDeep-Learning Visual Notes",
        "meta": [
            "Indian Polity · GS Paper II · Prelims + Mains",
            "Layer 1: Basic foundation · Layer 2: Advanced constitutional and exam depth",
            f"Sources: {basic_path.name} + {advanced_path.name}",
            f"Learning cards: {len(topics)}",
        ],
        "topics": topics,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_name = f"{number}_{re.sub(r'[^A-Za-z0-9-]+', '-', advanced_path.stem.split('_', 1)[-1]).strip('-')}_Deep-Learning.pdf"
    output_path = OUTPUT_DIR / output_name
    build_pdf(data, str(output_path))
    return output_path, len(topics)


def main() -> int:
    advanced_files = sorted(ADVANCED_DIR.glob("[0-9][0-9]_*.md"))
    if not advanced_files:
        print(f"No Advanced Polity chapters found in {ADVANCED_DIR}", file=sys.stderr)
        return 1

    failures = []
    total_cards = 0
    for index, advanced_path in enumerate(advanced_files, 1):
        try:
            output_path, cards = build_one(advanced_path)
            total_cards += cards
            print(f"[{index:02d}/{len(advanced_files)}] {output_path.name} ({cards} cards)")
        except Exception as exc:  # Keep the batch running and report every failed chapter.
            failures.append((advanced_path.name, str(exc)))
            print(f"[{index:02d}/{len(advanced_files)}] FAILED {advanced_path.name}: {exc}", file=sys.stderr)

    print(
        f"Generated {len(advanced_files) - len(failures)}/{len(advanced_files)} PDFs "
        f"with {total_cards} learning cards in {OUTPUT_DIR}"
    )
    if failures:
        print("Failures:", file=sys.stderr)
        for name, error in failures:
            print(f"  - {name}: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
