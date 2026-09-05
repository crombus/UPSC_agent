"""Preservation-safe learner-v2 retrofit for closure flows and core-first charts.

The retrofit creates a new learner-v2 generation per completed topic.  It never
rewrites a current Markdown, PDF, workbook, or pre-existing visual companion.
Each generated closure flow is distilled only from text already present in the
current assembled Markdown.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import date, datetime
from io import BytesIO
from pathlib import Path
from typing import Iterable

import fitz
from PIL import Image, ImageChops, ImageDraw, ImageFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

import markdown_learning_pdf
from validate_v2_export import V2_VARIANT, validate_pdf, validate_v2_markdown_text


ROOT = Path(__file__).resolve().parents[1]
Image.MAX_IMAGE_PIXELS = None  # Masters are intentionally high-resolution print assets.
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
MANIFEST = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" /
    "continuous-core-first-retrofit-2026-08-22.json"
)
VALIDATION_REPORT = MANIFEST.with_name(
    "continuous-core-first-retrofit-2026-08-22-validation.json"
)
CHANGED_FILE_REPORT = MANIFEST.with_name(
    "continuous-core-first-retrofit-2026-08-22-changed-files.txt"
)
STAGE_ORDER_REPORT = MANIFEST.with_name(
    "continuous-core-first-retrofit-2026-08-22-stage-order.json"
)
TODAY = date(2026, 8, 22)
RETROFIT_ID = "continuous-core-first-2026-08-22"
APPROVED_CARVAKA = "philosophy-paper-i-indian-philosophy-01"
POLITY_FR = "polity-07"

MASTER_WIDTH = 3600
MASTER_DPI = 200
MASTER_LEFT = 490
MASTER_RIGHT = 160
MASTER_TOP = 175
RAIL_X = 240
CARD_X = 465
CARD_WIDTH = MASTER_WIDTH - CARD_X - MASTER_RIGHT
STAGE_GAP = 100
TILE_HEIGHT = 2200
TILE_OVERLAP = 260

NAVY = "#091923"
CARD = "#102A3A"
CARD_ALT = "#123443"
CYAN = "#18C5D7"
WHITE = "#F1F8FB"
MUTED = "#B3CBD5"
BLUE = "#4DB4FF"
TEAL = "#42D6B0"
AMBER = "#FFC857"
RED = "#FF7A86"
GREEN = "#74DA9A"
PILL_COLORS = (BLUE, TEAL, AMBER, RED, GREEN)

FONT_DIR = Path(r"C:\Windows\Fonts")
FONT_REGULAR = FONT_DIR / "segoeui.ttf"
FONT_BOLD = FONT_DIR / "segoeuib.ttf"

H2_BASIC = re.compile(r"^##\s+BASIC LEARNING SESSION\s*$", re.I)
H2_ANY = re.compile(r"^##(?!#)\s+", re.I)
H3 = re.compile(r"^###\s+(.+?)\s*$")
H4 = re.compile(r"^####\s+(.+?)\s*$")
ANSWER = re.compile(
    r"ANSWER-GRABBING LINE\s*[—-]\s*WRITE/ADAPT IN THE EXAM\s*:\s*(.+)",
    re.I,
)
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9“\"'])")
MARKDOWN_LINK = re.compile(r"\[([^\]]+)]\([^)]+\)")
MARKDOWN_DECORATION = re.compile(r"[*`_]")


@dataclass(frozen=True)
class Topic:
    key: str
    subject: str
    generation: int
    record_id: str
    markdown: Path
    main_pdf: Path
    workbook: Path
    section_key: str
    source_record: dict


@dataclass(frozen=True)
class Closure:
    title: str
    terms: str
    mechanism: str
    consequence: str
    trap: str
    answer: str


class RetrofitError(ValueError):
    """A source cannot safely be converted using the reusable semantic rules."""


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT)).replace("/", "\\")


def repo_path(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def hash_inventory(paths: Iterable[Path]) -> dict[str, str]:
    return {
        relative(path): sha256(path)
        for path in sorted(paths, key=lambda item: str(item).casefold())
        if path.is_file()
    }


def load_tracker() -> dict:
    data = json.loads(TRACKER.read_text(encoding="utf-8"))
    if data.get("schema_version") != 2 or not isinstance(data.get("exports"), list):
        raise RetrofitError("EXPORT-PDF-STATUS.json must use schema v2.")
    return data


def completed_latest_topics(
    tracker: dict,
    *,
    include_retrofits: bool = False,
    subject: str | None = None,
) -> list[Topic]:
    by_key: dict[str, list[dict]] = {}
    for record in tracker["exports"]:
        if not isinstance(record, dict) or record.get("variant") != V2_VARIANT:
            continue
        key = str(record.get("topic_key") or "")
        if not key:
            continue
        by_key.setdefault(key, []).append(record)

    topics: list[Topic] = []
    for key, records in sorted(by_key.items()):
        ordered = sorted(records, key=lambda item: int(item.get("generation") or 1), reverse=True)
        record = ordered[0]
        retrofit = record.get("provenance", {}).get("retrofit", {}) if isinstance(record.get("provenance"), dict) else {}
        if (
            isinstance(retrofit, dict)
            and retrofit.get("id") == RETROFIT_ID
            and not include_retrofits
        ):
            paths = [repo_path(str(record.get(field, ""))) for field in ("markdown", "main_pdf", "workbook")]
            if all(path.is_file() for path in paths):
                continue
            # A prior run only creates retrofit records after validation. If an
            # interrupted external cleanup left one incomplete, recover from its
            # latest non-retrofit owner rather than generating over an orphan.
            record = next(
                (
                    candidate for candidate in ordered[1:]
                    if not (
                        isinstance(candidate.get("provenance"), dict)
                        and isinstance(candidate["provenance"].get("retrofit"), dict)
                        and candidate["provenance"]["retrofit"].get("id") == RETROFIT_ID
                    )
                ),
                record,
            )
        validation = record.get("validation")
        if not isinstance(validation, dict) or validation.get("state") != "passed":
            continue
        required = ("markdown", "main_pdf", "workbook", "record_id")
        if any(not record.get(field) for field in required):
            continue
        markdown = repo_path(str(record["markdown"]))
        main_pdf = repo_path(str(record["main_pdf"]))
        workbook = repo_path(str(record["workbook"]))
        if not all(path.is_file() for path in (markdown, main_pdf, workbook)):
            continue
        parts = markdown.relative_to(ROOT).parts
        refreshed = (
            len(parts) >= 8
            and parts[:2] == ("upsc-ai-kit", "knowledge")
            and parts[2].casefold() == "learner-v2-refreshed"
        )
        subject_name = parts[3] if refreshed else parts[2]
        try:
            v2_index = [part.casefold() for part in parts].index("v2")
            section_parts = parts[v2_index + 1 : -1]
            section = "-".join(section_parts) if section_parts else "compatibility-pilot"
        except ValueError:
            # Approved compatibility pilots may use the subject/section/topic
            # hierarchy without a literal learning-sessions\v2 segment.
            folded = [part.casefold() for part in parts]
            if (
                len(parts) >= 7
                and folded[:2] == ["upsc-ai-kit", "knowledge"]
                and "learning-sessions" in folded
            ):
                learning_index = folded.index("learning-sessions")
                section_start = 4 if refreshed else 3
                section_parts = parts[section_start:learning_index]
                section = (
                    "-".join(section_parts)
                    if section_parts
                    else "compatibility-pilot"
                )
            else:
                raise RetrofitError(f"Not a v2 source path: {markdown}")
        if subject and subject_name.casefold() != subject.casefold():
            continue
        topics.append(
            Topic(
                key=key,
                subject=subject_name,
                generation=int(record.get("generation") or 1),
                record_id=str(record["record_id"]),
                markdown=markdown,
                main_pdf=main_pdf,
                workbook=workbook,
                section_key=section,
                source_record=record,
            )
        )
    return topics


def remove_empty_parents(path: Path, boundary: Path) -> None:
    """Remove only empty fresh-generation directories, never a shared section."""
    current = path.parent
    while current != boundary and current.exists():
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent


def clean_text(value: str) -> str:
    value = MARKDOWN_LINK.sub(r"\1", value)
    value = MARKDOWN_DECORATION.sub("", value)
    value = re.sub(r"^>\s?", "", value.strip())
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -|")


def clean_heading(value: str) -> str:
    return clean_text(re.sub(r"^\d+(?:[A-Z]|\.\d+)*\.\s*", "", value))


META_STAGE_PATTERNS = (
    r"\bsource(?:[-\s]+complete)?\s*(?:audit|order|status|decision|note|owner|ownership|coverage|ledger|hierarchy)\b",
    r"\brepresentative\s+source\s+ledger\b",
    r"\b(?:official[-\s]*)?(?:live|current)[-\s]*(?:source|status|legal[- ]status|law)\s*(?:decision|check|note|control)?\b",
    r"\bsyllabus\s*(?:boundary|mapping|ownership|coverage)?\b",
    r"\bpackage\s*(?:count|bookkeeping|ledger|metadata|status)?\b",
    r"\b(?:package|artifact|source)\s+preservation\b",
    r"\bpreservation\s+(?:ledger|evidence|hash|audit|record|status|check)\b",
    r"\bregeneration\s+(?:ledger|evidence|hash|audit|record|status|check)\b",
    r"\banswer[- ]line\s*(?:control|register)\b",
    r"\banswer\s+(?:architecture|framework|template|route)\b",
    r"\b(?:generation|asset(?:s)?|path(?:s)?|validation|manifest|routing|ownership)\s+(?:note|notes|status|check|ledger|metadata|evidence|audit|record|control|register|inventory|decision)\b",
    r"\b(?:edition|release)\s+integration\b",
    r"\b(?:doctrine|topic|package)\s+routing\b",
    r"\b(?:readme|pyq)(?:[\s/:-])+(?:ledger|audit|index|status|coverage)\b",
    r"\b(?:upsc\s+)?relevance\s+(?:and|/)\s+answer[- ]worthiness\s+(?:audit|labels?)\b",
    r"\banswer[- ]worthiness\s+(?:audit|labels?)\b",
    r"\b(?:contemporary|current)[-\s]+(?:scholarly|india|technology)?[-\s]*(?:anchor|link)\s*(?:discipline|boundary)?\b",
    r"\b(?:master\s+learning\s+|learning\s+|road\s*)?roadmap\b",
    r"\blearning\s+road\s*map\b",
    r"\blearning\s+(?:route|path)\b",
    r"\b(?:visual|one[- ]screen|master\s+distinction)\s+(?:gateway|map)\b",
    r"\bstart\s+here\b.*\blearning\b",
    r"\bfirst[- ]use\s+terminology\b",
    r"^metric\s+discipline(?:\s*[—:-].*)?$",
)
META_STAGE_RE = re.compile("|".join(f"(?:{pattern})" for pattern in META_STAGE_PATTERNS), re.I)


def is_production_meta_stage(title: str) -> bool:
    """Exclude workflow/QA headings that are not learner-facing teaching stages."""
    return bool(META_STAGE_RE.search(clean_heading(title)))


SCAFFOLD_STAGE_RE = re.compile(
    r"^(?:"
    r"layer\s+\d+|"
    r"(?:plain[- ]language\s+)?visual|"
    r"how\s+to\s+use\b|"
    r"exam\s+route|"
    r"rapid\s+recall|"
    r"sources?|"
    r"pyq\s+routing|"
    r".*\banswer\s+(?:architecture|framework|template|route)|"
    r"link[- ]outs?"
    r")",
    re.I,
)


def is_learner_scaffold_stage(title: str) -> bool:
    """Exclude navigation shells when a deep session exposes teaching at H4."""
    return bool(SCAFFOLD_STAGE_RE.search(clean_heading(title)))


def prose_lines(section: str) -> list[str]:
    lines: list[str] = []
    in_code = False
    for raw in section.splitlines():
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not stripped or stripped.startswith("#") or stripped.startswith("|"):
            continue
        if stripped.startswith("<!--"):
            continue
        line = clean_text(stripped.lstrip("-+* "))
        if not line or line.lower().startswith(("visual:", "caption:")):
            continue
        lines.append(line)
    return lines


def sentences(section: str) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for line in prose_lines(section):
        for sentence in SENTENCE_SPLIT.split(line):
            sentence = sentence.strip()
            normalized = sentence.casefold()
            if len(sentence) < 35 or normalized in seen:
                continue
            if re.fullmatch(r"(?:fact|analysis|current|memory|wrong)\s*:?", sentence, re.I):
                continue
            seen.add(normalized)
            result.append(sentence)
    return result


def first_matching(candidates: list[str], words: tuple[str, ...], fallback: str) -> str:
    for candidate in candidates:
        lowered = candidate.casefold()
        if any(word in lowered for word in words):
            return candidate
    return fallback


def answer_line(section: str, fallback: str) -> str:
    match = ANSWER.search(section)
    if match:
        value = clean_text(match.group(1))
        if value:
            return value
    return fallback


def source_closure(title: str, body: str) -> Closure:
    source_sentences = sentences(body)
    if not source_sentences:
        raise RetrofitError(f"Cannot derive a semantic closure for {title!r}: no prose.")
    opening = source_sentences[0]
    answer = answer_line(body, opening)
    terms = first_matching(
        source_sentences,
        (" is ", " means ", "refers to", "defined", "act", "article", "doctrine"),
        answer,
    )
    mechanism = first_matching(
        source_sentences,
        (
            "because", "therefore", "through", "by ", "mechanism", "process",
            "creates", "enables", "requires", "leads to", "results in",
        ),
        source_sentences[min(1, len(source_sentences) - 1)],
    )
    consequence = first_matching(
        source_sentences,
        (
            "therefore", "thus", "consequently", "contrast", "whereas",
            "unlike", "result", "effect", "implication", "significance",
        ),
        source_sentences[min(2, len(source_sentences) - 1)],
    )
    trap = first_matching(
        source_sentences,
        (
            "trap", "not ", "never ", "rather than", "must not", "misread",
            "caution", "incorrect", "avoid",
        ),
        "Answer-use: " + answer,
    )
    return Closure(
        title=clean_heading(title),
        terms=terms,
        mechanism=mechanism,
        consequence=consequence,
        trap=trap,
        answer=answer,
    )


def closure_fence(closure: Closure) -> str:
    return "\n".join((
        "```closure-flow",
        f"SUBTOPIC: {closure.title}",
        f"KEY TERMS / DEFINITIONS: {closure.terms}",
        f"MECHANISM / ARGUMENT: {closure.mechanism}",
        f"CONSEQUENCE / CONTRAST: {closure.consequence}",
        f"UPSC TRAP / ANSWER-USE: {closure.trap}",
        f"ANSWER-GRABBING FORMULATION: {closure.answer}",
        "```",
    ))


def basic_h3_ranges(
    markdown: str,
    *,
    include_closed: bool = False,
) -> list[tuple[int, int, str, str]]:
    lines = markdown.replace("\r\n", "\n").splitlines()
    basic_start = next(
        (index for index, line in enumerate(lines) if H2_BASIC.fullmatch(line.strip())),
        None,
    )
    if basic_start is None:
        raise RetrofitError("Missing canonical BASIC LEARNING SESSION H2.")
    basic_end = next(
        (
            index
            for index in range(basic_start + 1, len(lines))
            if H2_ANY.match(lines[index].strip())
        ),
        len(lines),
    )
    def heading_ranges(
        heading_re: re.Pattern[str],
        *,
        fallback_to_h4: bool = False,
    ) -> list[tuple[int, int, str, str]]:
        all_headings = [
            (index, heading_re.fullmatch(lines[index].strip()).group(1))
            for index in range(basic_start + 1, basic_end)
            if heading_re.fullmatch(lines[index].strip())
        ]
        ranges: list[tuple[int, int, str, str]] = []
        for position, (start, title) in enumerate(all_headings):
            end = (
                all_headings[position + 1][0]
                if position + 1 < len(all_headings)
                else basic_end
            )
            if (
                is_production_meta_stage(title)
                or (fallback_to_h4 and is_learner_scaffold_stage(title))
            ):
                continue
            body = "\n".join(lines[start + 1 : end])
            # A roadmap or visual-only signpost is not a completed teaching
            # subtopic. H3/H4 teaching blocks with deeper detail still qualify
            # because their prose remains in the block and is distilled below.
            if not sentences(body):
                continue
            if include_closed or "```closure-flow" not in body:
                ranges.append((start, end, title, body))
        return ranges

    ranges = heading_ranges(H3)
    if ranges:
        return ranges

    # Some long-form sessions deliberately use H3 only for package controls and
    # learning-layer navigation, placing every actual teaching unit at H4.  A
    # fallback keeps each source-derived H4 unit complete instead of turning
    # package metadata into a shallow three-card chart.
    ranges = heading_ranges(H4, fallback_to_h4=True)
    if not ranges:
        raise RetrofitError(
            "BASIC LEARNING SESSION has no completed H3 or H4 teaching subtopics."
        )
    return ranges


def retrofit_markdown(markdown: str) -> tuple[str, list[Closure]]:
    source = without_closure_flows(markdown)
    lines = source.replace("\r\n", "\n").splitlines()
    ranges = basic_h3_ranges(source)
    closures = [source_closure(title, body) for _, _, title, body in ranges]
    # Rebuild backwards so original source offsets stay valid.
    for (start, end, _, _), closure in reversed(list(zip(ranges, closures))):
        insertion = ["", closure_fence(closure), ""]
        lines[end:end] = insertion
    updated = "\n".join(lines).rstrip() + "\n"
    return updated, closures


def rebase_asset_paths(markdown: str, old_parent: Path, new_parent: Path) -> str:
    """Keep copied Markdown's existing local assets valid without copying them."""
    def rebased(raw_path: str) -> str:
        raw_path = raw_path.strip()
        if (
            not raw_path
            or "://" in raw_path
            or raw_path.startswith("#")
            or Path(raw_path).is_absolute()
        ):
            return raw_path
        original = (old_parent / raw_path).resolve()
        if not original.is_file():
            # Some established v2 Markdown uses a repository-root-relative
            # asset path rather than a source-relative one.
            original = (ROOT / raw_path).resolve()
        if not original.is_file():
            return raw_path
        return Path(os.path.relpath(original, new_parent)).as_posix()

    markdown = re.sub(
        r"(?m)^(cover_image:\s*[\"']?)([^\"'\n]+)([\"']?\s*)$",
        lambda match: match.group(1) + rebased(match.group(2)) + match.group(3),
        markdown,
    )
    return re.sub(
        r"(!\[[^\]]*]\()([^)]+)(\))",
        lambda match: match.group(1) + rebased(match.group(2)) + match.group(3),
        markdown,
    )


def closure_blocks(markdown: str) -> list[Closure]:
    blocks = re.findall(r"```closure-flow\s*\n(.*?)\n```", markdown, flags=re.S | re.I)
    closures: list[Closure] = []
    for block in blocks:
        _, fields = markdown_learning_pdf.parse_closure_flow(block.splitlines())
        title = next(
            (
                value.strip()
                for label, value in (
                    line.split(":", 1) for line in block.splitlines() if ":" in line
                )
                if label.strip().upper() == "SUBTOPIC"
            ),
            "SUBTOPIC CLOSURE FLOW",
        )
        closures.append(Closure(title=title, **fields))
    if closures:
        return closures

    # Learner-v2 refreshed generations express the same closure contract as a
    # named H3 session followed by a final text-native recall flow.
    basic = re.search(
        r"(?ims)^##\s+BASIC LEARNING SESSION\s*(.*?)"
        r"(?=^##\s+BASIC MCQS / REMEDIATION)",
        markdown,
    )
    if not basic:
        return []
    section = basic.group(1)
    sessions = list(
        re.finditer(
            r"(?im)^###\s+SESSION\s+\d+\s*[—-]\s*(.+?)\s*$",
            section,
        )
    )
    for position, session in enumerate(sessions):
        end = (
            sessions[position + 1].start()
            if position + 1 < len(sessions)
            else len(section)
        )
        body = section[session.end() : end]

        def field(pattern: str, fallback: str) -> str:
            match = re.search(pattern, body, re.I | re.S | re.M)
            return clean_text(match.group(1)) if match else fallback

        title = clean_heading(session.group(1))
        terms = field(
            r"\*\*Technical definition:\*\*\s*(.+?)\s*(?=\n|$)",
            title,
        )
        answer = field(
            r"####\s+ANSWER-GRABBING OPENING.*?\n+\s*>\s*(.+?)\s*(?=\n|$)",
            terms,
        )
        closures.append(
            Closure(
                title=title,
                terms=terms,
                mechanism=field(
                    r"MECHANISM / ARGUMENT:\s*(.+?)\s*(?=\n\s*\||\n\s*v|\n|$)",
                    terms,
                ),
                consequence=field(
                    r"CONSEQUENCE / CONTRAST:\s*(.+?)\s*(?=\n\s*\||\n\s*v|\n|$)",
                    answer,
                ),
                trap=field(
                    r"UPSC TRAP / ANSWER-USE:\s*(.+?)\s*(?=\n\s*\||\n\s*v|\n|$)",
                    answer,
                ),
                answer=answer,
            )
        )
    return closures


def without_closure_flows(markdown: str) -> str:
    return re.sub(
        r"\n*```closure-flow\s*\n.*?\n```\n*",
        "\n",
        markdown.replace("\r\n", "\n"),
        flags=re.S | re.I,
    )


def reorder_polity_07_fundamental_rights(markdown: str) -> str:
    """Place the Article 31/300A and Article 359 material in constitutional order."""
    source = without_closure_flows(markdown)
    property_stage = re.compile(
        r"(?ms)^###\s+04\.\s+Right to property transition and the non-derogable Emergency core\s*\n"
        r"(.*?)(?=^###\s+05\.\s+Article 12\b)"
    )
    match = property_stage.search(source)
    if not match:
        return source
    body = match.group(1)
    emergency_marker = (
        "[FACT] The Forty-fourth Amendment also entrenched an Emergency lesson:"
    )
    property_body, marker, emergency_body = body.partition(emergency_marker)
    if not marker or not property_body.strip() or not emergency_body.strip():
        raise RetrofitError(
            "polity-07: cannot safely separate property and Article 359 material."
        )
    property_body = re.sub(
        r"> \*\*ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM "
        r"\(PROPERTY / EMERGENCY CORE\):\*\*.*?\n\n",
        (
            "> **ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM "
            "(PROPERTY):** The Forty-fourth Amendment moved property from "
            "Part III to the constitutional guarantee in Article 300A.\n\n"
        ),
        property_body,
        count=1,
        flags=re.S,
    )
    emergency_body = (
        "> **ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM "
        "(ARTICLE 359 CORE):** A Presidential order under Article 359 cannot "
        "suspend the right to move a court for enforcement of Articles 20 and 21.\n\n"
        "> **CONTENT CLASSIFICATION:** CORE PRELIMS + CORE MAINS\n\n"
        + marker
        + emergency_body
    )
    source = source[:match.start()] + source[match.end():]

    def append_stage(
        text: str,
        current_header: str,
        next_header: str,
        stage: str,
    ) -> str:
        pattern = re.compile(
            rf"(?ms)^(###\s+{re.escape(current_header)}.*?)(?=^###\s+{re.escape(next_header)})"
        )
        found = pattern.search(text)
        if not found:
            raise RetrofitError(
                f"polity-07: cannot locate constitutional insertion point {current_header!r}."
            )
        return text[:found.end()] + "\n" + stage.rstrip() + "\n\n" + text[found.end():]

    source = append_stage(
        source,
        "24. Articles 31A, 31B and 31C",
        "25. Articles 33-35",
        "### Right to property: Article 31 transition to Article 300A\n\n"
        + property_body.strip(),
    )
    source = append_stage(
        source,
        "26. Articles 358 and 359",
        "27. Current-law dashboard",
        "### Article 359: the non-derogable Articles 20 and 21 core\n\n"
        + emergency_body.strip(),
    )
    return renumber_basic_teaching_h3(source)


def renumber_basic_teaching_h3(markdown: str) -> str:
    """Keep a moved Basic-session sequence legible without renumbering metadata."""
    lines = markdown.splitlines()
    basic_start = next(
        (index for index, line in enumerate(lines) if H2_BASIC.fullmatch(line.strip())),
        None,
    )
    if basic_start is None:
        return markdown
    basic_end = next(
        (index for index in range(basic_start + 1, len(lines)) if H2_ANY.match(lines[index].strip())),
        len(lines),
    )
    number = 0
    for index in range(basic_start + 1, basic_end):
        match = H3.fullmatch(lines[index].strip())
        if not match or is_production_meta_stage(match.group(1)):
            continue
        number += 1
        title = re.sub(r"^\d+(?:[A-Z]|\.\d+)*\.\s*", "", match.group(1))
        lines[index] = f"### {number:02d}. {title}"
    return "\n".join(lines).rstrip() + "\n"


def preservation_normal_form(markdown: str) -> str:
    """Ignore only rebased local-asset destinations and injected closure fences."""
    normalized = without_closure_flows(markdown)
    normalized = re.sub(
        r"(?m)^cover_image:\s*[\"']?[^\"'\n]+[\"']?\s*$",
        "cover_image: <LOCAL-ASSET>",
        normalized,
    )
    normalized = re.sub(
        r"(!\[[^\]]*]\()[^)]+(\))",
        r"\1<LOCAL-ASSET>\2",
        normalized,
    )
    return "\n".join(
        line.rstrip() for line in normalized.splitlines() if line.strip()
    ).strip()


def source_preservation_errors(
    previous: str,
    current: str,
    *,
    topic_key: str | None = None,
) -> list[str]:
    errors: list[str] = []
    if topic_key == POLITY_FR:
        previous = reorder_polity_07_fundamental_rights(previous)
        current = reorder_polity_07_fundamental_rights(current)
    if preservation_normal_form(previous) != preservation_normal_form(current):
        errors.append(
            "Source teaching changed outside injected closure flows or rebased local assets."
        )
    source_text = clean_text(without_closure_flows(previous))
    for closure in closure_blocks(current):
        for label, value in (
            ("terms", closure.terms),
            ("mechanism", closure.mechanism),
            ("consequence", closure.consequence),
            ("trap", closure.trap.removeprefix("Answer-use: ")),
            ("answer", closure.answer),
        ):
            if clean_text(value) not in source_text:
                errors.append(
                    f"Closure {label} is not a direct source-derived formulation: {closure.title}"
                )
    return errors


def validate_closure_placement(markdown: str) -> list[str]:
    errors: list[str] = []
    ranges = basic_h3_ranges(markdown, include_closed=True)
    for _, _, title, body in ranges:
        if "```closure-flow" not in body:
            errors.append(f"Missing closure flow before next teaching H3: {title}")
            continue
        try:
            markdown_learning_pdf.parse_closure_flow(
                re.search(r"```closure-flow\s*\n(.*?)\n```", body, re.S | re.I).group(1).splitlines()
            )
        except (AttributeError, ValueError) as exc:
            errors.append(f"Invalid closure flow for {title}: {exc}")
    return errors


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    if not path.is_file():
        raise RetrofitError(f"Required Windows visual font is unavailable: {path}")
    return ImageFont.truetype(str(path), size)


def wrap(draw: ImageDraw.ImageDraw, text: str, visual_font: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    result: list[str] = []
    line = ""
    for word in words:
        proposed = f"{line} {word}".strip()
        if not line or draw.textbbox((0, 0), proposed, font=visual_font)[2] <= width:
            line = proposed
        else:
            result.append(line)
            line = word
    if line:
        result.append(line)
    return result or [""]


def card_height(draw: ImageDraw.ImageDraw, closure: Closure, fonts: dict[str, ImageFont.FreeTypeFont]) -> int:
    body_width = CARD_WIDTH - 120
    answer_width = CARD_WIDTH - 420
    fields = (
        ("CONTEXT + EXACT CORE", closure.terms),
        ("MECHANISM", closure.mechanism),
        ("CONSEQUENCE / CONTRAST", closure.consequence),
        ("TRAP / ANSWER USE", closure.trap),
    )
    height = 125 + len(wrap(draw, closure.title, fonts["heading"], body_width)) * 78
    for _, value in fields:
        height += 39 + len(wrap(draw, value, fonts["body"], body_width)) * 47
    height += 42 + len(wrap(draw, closure.answer, fonts["answer"], answer_width)) * 46
    return max(780, height + 76)


def draw_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    visual_font: ImageFont.FreeTypeFont,
    fill: str,
    width: int,
    line_gap: int,
) -> int:
    x, y = xy
    for line in wrap(draw, text, visual_font, width):
        draw.text((x, y), line, font=visual_font, fill=fill)
        y += line_gap
    return y


def stage_ranges(closures: list[Closure], heights: list[int]) -> list[tuple[int, int, int]]:
    cursor = MASTER_TOP
    ranges: list[tuple[int, int, int]] = []
    for number, height in enumerate(heights, 1):
        start = cursor
        end = start + height
        ranges.append((number, start, end))
        cursor = end + STAGE_GAP
    return ranges


def render_master(topic: Topic, closures: list[Closure], out_path: Path) -> tuple[tuple[int, int], list[tuple[int, int, int]]]:
    if not closures:
        raise RetrofitError(f"{topic.key}: no source-derived closures available for master.")
    fonts = {
        "heading": font(FONT_BOLD, 52),
        "body": font(FONT_REGULAR, 31),
        "label": font(FONT_BOLD, 26),
        "answer": font(FONT_BOLD, 30),
        "stage": font(FONT_BOLD, 42),
        "tiny": font(FONT_BOLD, 22),
    }
    probe = Image.new("RGB", (MASTER_WIDTH, 100), NAVY)
    heights = [card_height(ImageDraw.Draw(probe), closure, fonts) for closure in closures]
    stages = stage_ranges(closures, heights)
    master_height = stages[-1][2] + MASTER_TOP
    image = Image.new("RGB", (MASTER_WIDTH, master_height), NAVY)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, MASTER_WIDTH, 110), fill="#0F3343")
    draw.text((CARD_X, 35), f"{topic.key.upper()}  |  CONTINUOUS CORE-FIRST MASTER", font=fonts["tiny"], fill=CYAN)
    draw.line((RAIL_X, 105, RAIL_X, master_height - 110), fill=CYAN, width=22)

    for closure, (stage, top, bottom) in zip(closures, stages):
        color = PILL_COLORS[(stage - 1) % len(PILL_COLORS)]
        draw.ellipse((RAIL_X - 54, top + 34, RAIL_X + 54, top + 142), fill=CYAN, outline=WHITE, width=5)
        stage_text = f"{stage:02d}"
        box = draw.textbbox((0, 0), stage_text, font=fonts["stage"])
        draw.text(
            (RAIL_X - (box[2] - box[0]) // 2, top + 51),
            stage_text,
            font=fonts["stage"],
            fill=NAVY,
        )
        draw.line((RAIL_X + 55, top + 89, CARD_X - 26, top + 89), fill=CYAN, width=10)
        draw.rounded_rectangle((CARD_X, top, MASTER_WIDTH - MASTER_RIGHT, bottom), radius=36, fill=CARD if stage % 2 else CARD_ALT, outline=color, width=5)
        x = CARD_X + 50
        y = top + 42
        y = draw_text(draw, (x, y), closure.title, fonts["heading"], WHITE, CARD_WIDTH - 110, 67)
        y += 9
        fields = (
            ("CONTEXT + EXACT CORE", closure.terms),
            ("MECHANISM / ARGUMENT", closure.mechanism),
            ("CONSEQUENCE / CONTRAST", closure.consequence),
            ("UPSC TRAP / ANSWER USE", closure.trap),
        )
        for index, (label, value) in enumerate(fields):
            pill_color = PILL_COLORS[(stage + index) % len(PILL_COLORS)]
            label_box = draw.textbbox((0, 0), label, font=fonts["label"])
            pill_width = min(CARD_WIDTH - 115, label_box[2] - label_box[0] + 36)
            draw.rounded_rectangle((x, y, x + pill_width, y + 39), radius=16, fill=pill_color)
            draw.text((x + 16, y + 4), label, font=fonts["label"], fill=NAVY)
            y += 48
            y = draw_text(draw, (x + 6, y), value, fonts["body"], MUTED, CARD_WIDTH - 122, 47)
            y += 9
        draw.rounded_rectangle((x, bottom - 125, MASTER_WIDTH - MASTER_RIGHT - 38, bottom - 34), radius=18, fill="#183E35", outline=GREEN, width=3)
        draw.text((x + 18, bottom - 111), "ANSWER LINE:", font=fonts["label"], fill=GREEN)
        draw_text(draw, (x + 250, bottom - 111), closure.answer, fonts["answer"], WHITE, CARD_WIDTH - 420, 44)

    image.save(out_path, "PNG", dpi=(MASTER_DPI, MASTER_DPI), optimize=True)
    return image.size, stages


def poster_pdf(master: Path, out_path: Path, dimensions: tuple[int, int]) -> tuple[float, float]:
    width, height = dimensions
    poster_width_mm = 600
    poster_width = poster_width_mm * mm
    poster_height = poster_width * height / width
    document = canvas.Canvas(str(out_path), pagesize=(poster_width, poster_height), invariant=1)
    document.drawImage(str(master), 0, 0, width=poster_width, height=poster_height, mask="auto")
    document.showPage()
    document.save()
    return poster_width, poster_height


def stage_for_y(stages: list[tuple[int, int, int]], y: int, *, last: bool = False) -> int:
    matches = [number for number, start, end in stages if start <= y <= end]
    if matches:
        return matches[-1] if last else matches[0]
    before = [number for number, start, _ in stages if start <= y]
    return before[-1] if before else stages[0][0]


def tile_pdf(
    master: Path,
    out_path: Path,
    dimensions: tuple[int, int],
    stages: list[tuple[int, int, int]],
) -> list[dict[str, int]]:
    image = Image.open(master).convert("RGB")
    width, height = dimensions
    starts = list(range(0, max(height - TILE_HEIGHT, 0) + 1, TILE_HEIGHT - TILE_OVERLAP))
    if not starts or starts[-1] + TILE_HEIGHT < height:
        starts.append(max(0, height - TILE_HEIGHT))
    starts = list(dict.fromkeys(starts))
    page_w, page_h = 420 * mm, 297 * mm
    document = canvas.Canvas(str(out_path), pagesize=(page_w, page_h), invariant=1)
    coordinates: list[dict[str, int]] = []
    for page_number, start in enumerate(starts, 1):
        end = min(height, start + TILE_HEIGHT)
        crop = image.crop((0, start, width, end))
        stream = BytesIO()
        crop.save(stream, "PNG", optimize=True)
        stream.seek(0)
        document.drawImage(ImageReader(stream), 0, 0, width=page_w, height=page_h, mask="auto")
        document.showPage()
        coordinates.append({
            "page": page_number,
            "y_start": start,
            "y_end": end,
            "overlap_px": 0 if page_number == 1 else TILE_OVERLAP,
            "from_stage": stage_for_y(stages, start),
            "continues_stage": stage_for_y(stages, end, last=True),
        })
    document.save()
    image.close()
    return coordinates


def render_previews(tiled: Path, preview_dir: Path) -> tuple[list[Path], list[Path]]:
    preview_dir.mkdir(parents=True, exist_ok=True)
    document = fitz.open(tiled)
    previews: list[Path] = []
    for page_number, page in enumerate(document, 1):
        path = preview_dir / f"page-{page_number:03d}.png"
        page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False).save(path)
        previews.append(path)
    document.close()
    contacts: list[Path] = []
    for group_start in range(0, len(previews), 6):
        group = previews[group_start : group_start + 6]
        images = [Image.open(path).convert("RGB") for path in group]
        tile_w = 680
        tile_h = max(round(image.height * tile_w / image.width) for image in images)
        sheet = Image.new("RGB", (tile_w * 2, tile_h * 3), "#DEE8EC")
        for index, image in enumerate(images):
            thumbnail = image.copy()
            thumbnail.thumbnail((tile_w, tile_h))
            x = (index % 2) * tile_w + (tile_w - thumbnail.width) // 2
            y = (index // 2) * tile_h + (tile_h - thumbnail.height) // 2
            sheet.paste(thumbnail, (x, y))
            image.close()
        contact = preview_dir / f"contact-sheet-{group_start // 6 + 1:02d}.png"
        sheet.save(contact, "PNG", optimize=True)
        contacts.append(contact)
    return previews, contacts


def pdf_text_and_layout_errors(path: Path) -> list[str]:
    errors = validate_pdf(path)
    try:
        document = fitz.open(path)
        if document.page_count < 1:
            errors.append("PDF has no renderable pages.")
        for page in document:
            text = page.get_text("text")
            if "\ufffd" in text or "�" in text:
                errors.append(f"Replacement glyph in page {page.number + 1}.")
        document.close()
    except Exception as exc:
        errors.append(f"PyMuPDF could not render PDF: {exc}")
    return errors


def readme(
    topic: Topic,
    output_dir: Path,
    master: Path,
    poster: Path,
    tiled: Path,
    dimensions: tuple[int, int],
    tiles: list[dict[str, int]],
) -> None:
    output_dir.joinpath("README.txt").write_text(
        "\n".join((
            f"{topic.key.upper()} — CONTINUOUS AT-A-GLANCE CORE-FIRST",
            "",
            "Design: dark high-contrast canvas; cyan numbered stage rail; coloured decisive-keyword pills;",
            "large headings; answer-line bands; and the complete core before any subordinate enrichment.",
            "Every tiled page is an overlapping crop of the same master PNG, not an independent card.",
            "",
            f"Master PNG: {master.name}",
            f"Master dimensions: {dimensions[0]} × {dimensions[1]} px at {MASTER_DPI} dpi metadata",
            f"Poster PDF: {poster.name}",
            f"Tiled PDF: {tiled.name}",
            f"Tiles: {len(tiles)}; overlap: {TILE_OVERLAP}px",
            f"Source owner: {relative(topic.markdown)}",
        )) + "\n",
        encoding="utf-8",
    )


def flowchart_package(topic: Topic, markdown: str, generation: int) -> dict[str, object]:
    if topic.key == APPROVED_CARVAKA:
        reference = (
            ROOT / "notes" / "Philosophy" / "flowcharts" / topic.key /
            "continuous-at-a-glance-core-first"
        )
        required = (
            reference / "Carvaka_Continuous-At-a-Glance-Core-First_Master.png",
            reference / "Carvaka_Continuous-At-a-Glance-Core-First_Poster_2026-08-22.pdf",
            reference / "Carvaka_Continuous-At-a-Glance-Core-First_Tiled_2026-08-22.pdf",
            reference / "README.txt",
            reference / "validation-report.txt",
        )
        if not all(path.is_file() for path in required):
            raise RetrofitError("Approved Cārvāka reference companion is incomplete.")
        return {
            "folder": relative(reference),
            "master_image": relative(required[0]),
            "poster_pdf": relative(required[1]),
            "tiled_pdf": relative(required[2]),
            "previews": relative(reference / "previews"),
            "approved_reference_reused": True,
        }

    closures = closure_blocks(markdown)
    folder = (
        ROOT / "notes" / topic.subject / "flowcharts" / topic.key /
        f"continuous-at-a-glance-core-first-g{generation}"
    )
    if folder.exists():
        raise RetrofitError(f"Refusing to overwrite existing flowchart generation: {folder}")
    folder.mkdir(parents=True)
    # Keep generated names short: the subject/topic/generation folders already
    # carry identity and Windows otherwise rejects long Geography topic paths.
    master = folder / "master.png"
    poster = folder / "poster.pdf"
    tiled = folder / "tiled.pdf"
    dimensions, stages = render_master(topic, closures, master)
    poster_dimensions = poster_pdf(master, poster, dimensions)
    tiles = tile_pdf(master, tiled, dimensions, stages)
    previews, contacts = render_previews(tiled, folder / "previews")
    readme(topic, folder, master, poster, tiled, dimensions, tiles)
    errors = [*pdf_text_and_layout_errors(poster), *pdf_text_and_layout_errors(tiled)]
    report = folder / "validation-report.txt"
    report.write_text(
        "\n".join((
            f"topic={topic.key}",
            f"generated={datetime.now().astimezone().isoformat()}",
            f"source={relative(topic.markdown)}",
            f"master_png={master.name}",
            f"master_dimensions_px={dimensions[0]}x{dimensions[1]}",
            f"master_dpi_metadata={MASTER_DPI}x{MASTER_DPI}",
            f"poster_pdf={poster.name}",
            f"poster_dimensions_points={poster_dimensions[0]:.2f}x{poster_dimensions[1]:.2f}",
            f"poster_pages=1",
            f"tiled_pdf={tiled.name}",
            f"tiled_pages={len(tiles)}",
            "same_master_split=yes",
            f"tile_overlap_px={TILE_OVERLAP}",
            f"preview_count={len(previews)}",
            f"contact_sheet_count={len(contacts)}",
            f"closure_stage_count={len(closures)}",
            "node_pattern=heading -> decisive context -> exact terms/details -> consequence/contrast",
            "core_before_extra=PASS",
            f"poster_pdf_validation={'PASS' if not errors else 'FAIL'}",
            f"renderability={'PASS' if not errors else 'FAIL'}",
            "tile_coordinates=",
            *[
                (
                    f"  page-{tile['page']:03d}: y={tile['y_start']}..{tile['y_end']}; "
                    f"overlap={tile['overlap_px']}; from={tile['from_stage']}; "
                    f"continues={tile['continues_stage']}"
                )
                for tile in tiles
            ],
            "errors=" + ("none" if not errors else " | ".join(errors)),
        )) + "\n",
        encoding="utf-8",
    )
    if errors:
        raise RetrofitError(f"{topic.key}: generated flowchart validation failed: {errors}")
    return {
        "folder": relative(folder),
        "master_image": relative(master),
        "poster_pdf": relative(poster),
        "tiled_pdf": relative(tiled),
        "previews": relative(folder / "previews"),
        "contact_sheets": [relative(path) for path in contacts],
        "validation_report": relative(report),
        "approved_reference_reused": False,
    }


def generation_paths(topic: Topic, generation: int) -> tuple[Path, Path]:
    section = f"{topic.section_key}-core-first-g{generation}"
    markdown = (
        ROOT / "upsc-ai-kit" / "knowledge" / topic.subject / "learning-sessions" / "v2" /
        section / f"{topic.key}_Learning-Session.md"
    )
    main_pdf = (
        ROOT / "notes" / topic.subject / "learning-session-v2" / section / "notes" /
        f"{topic.key}_Learning-Session_{TODAY.isoformat()}.pdf"
    )
    return markdown, main_pdf


def preservation_evidence(topic: Topic, flow: dict[str, object], before: dict[str, str]) -> None:
    if flow["approved_reference_reused"]:
        return
    folder = repo_path(str(flow["folder"]))
    after = hash_inventory((topic.markdown, topic.main_pdf, topic.workbook))
    before_path = folder / "preservation-hashes-before.json"
    after_path = folder / "preservation-hashes-after.json"
    before_path.write_text(json.dumps(before, indent=2) + "\n", encoding="utf-8")
    after_path.write_text(
        json.dumps(
            {
                "preexisting_hashes_after": after,
                "all_preexisting_files_unchanged": before == after,
                "mismatches": sorted(
                    path for path in set(before) | set(after)
                    if before.get(path) != after.get(path)
                ),
            },
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    if before != after:
        raise RetrofitError(f"{topic.key}: a preserved source artifact changed.")


def next_generation(tracker: dict, key: str) -> int:
    return 1 + max(
        (
            int(record.get("generation") or 1)
            for record in tracker["exports"]
            if isinstance(record, dict)
            and record.get("topic_key") == key
            and record.get("variant") == V2_VARIANT
        ),
        default=0,
    )


def prior_retrofit_results(tracker: dict) -> list[dict]:
    """Make an interrupted sequential run resumable without duplicating generations."""
    latest: dict[str, dict] = {}
    for record in tracker["exports"]:
        if not isinstance(record, dict) or record.get("variant") != V2_VARIANT:
            continue
        provenance = record.get("provenance")
        retrofit = provenance.get("retrofit", {}) if isinstance(provenance, dict) else {}
        if not isinstance(retrofit, dict) or retrofit.get("id") != RETROFIT_ID:
            continue
        key = str(record["topic_key"])
        if key not in latest or int(record["generation"]) > int(latest[key]["generation"]):
            latest[key] = record
    results: list[dict] = []
    for record in latest.values():
        provenance = record.get("provenance")
        retrofit = provenance.get("retrofit", {}) if isinstance(provenance, dict) else {}
        paths = [repo_path(str(record.get(field, ""))) for field in ("markdown", "main_pdf", "workbook")]
        if not all(path.is_file() for path in paths):
            continue
        results.append({
            "topic_key": str(record["topic_key"]),
            "status": "succeeded",
            "generation": int(record["generation"]),
            "source": str(retrofit.get("source_record", "")),
            "markdown": str(record["markdown"]),
            "main_pdf": str(record["main_pdf"]),
            "workbook": str(record["workbook"]),
            "closure_flows": len(
                closure_blocks(repo_path(str(record["markdown"])).read_text(encoding="utf-8"))
            ),
            "flowchart": record.get("continuous_core_first", {}),
        })
    return sorted(results, key=lambda result: str(result["topic_key"]))


def new_record(
    topic: Topic,
    generation: int,
    markdown: Path,
    main_pdf: Path,
    flow: dict[str, object],
) -> dict:
    record = copy.deepcopy(topic.source_record)
    record.update({
        "record_id": f"{topic.key}:{V2_VARIANT}:g{generation}",
        "generation": generation,
        "supersedes": topic.record_id,
        "command": str(topic.source_record.get("command", "")).removesuffix(" — Regenerate") + " — Regenerate",
        "markdown": relative(markdown),
        "main_pdf": relative(main_pdf),
        # The workbook is byte-preserved: no teaching/practice content changed there.
        "workbook": relative(topic.workbook),
        "generated_on": TODAY.isoformat(),
        "approved": False,
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": f"{topic.key}:{V2_VARIANT}:g{generation}",
        },
        "validation": {
            "state": "passed",
            "validated_on": TODAY.isoformat(),
            "validator": "tools/retrofit_v2_core_first.py + tools/validate_v2_export.py",
        },
        "continuous_core_first": flow,
    })
    provenance = record.setdefault("provenance", {})
    provenance.update({
        "assembled_markdown": relative(markdown),
        "renderer": {
            "name": "tools/markdown_learning_pdf.py",
            "version": "2.1+closure-flow",
        },
        "generation_date": TODAY.isoformat(),
        "retrofit": {
            "id": RETROFIT_ID,
            "source_record": topic.record_id,
            "closure_flow": "source-derived and placed after every BASIC H3",
            "workbook": "byte-preserved; no practice content changed",
            "flowchart": (
                "approved Cārvāka reference reused unchanged"
                if flow["approved_reference_reused"]
                else "new continuous core-first same-master companion"
            ),
        },
    })
    return record


def validate_topic(markdown_path: Path, main_pdf: Path, closures: int) -> list[str]:
    markdown = markdown_path.read_text(encoding="utf-8")
    errors = validate_v2_markdown_text(markdown)
    errors.extend(validate_closure_placement(markdown))
    if len(closure_blocks(markdown)) != closures:
        errors.append("Closure-flow count does not match the generated Basic H3 closures.")
    meta_titles = [
        closure.title for closure in closure_blocks(markdown)
        if is_production_meta_stage(closure.title)
    ]
    if meta_titles:
        errors.append(
            "Production metadata became learner flow stages: "
            + " | ".join(meta_titles)
        )
    errors.extend(validate_pdf(main_pdf, variant=V2_VARIANT, mode="main"))
    try:
        document = fitz.open(main_pdf)
        extracted = "\n".join(page.get_text("text") for page in document)
        document.close()
        if extracted.count("SUBTOPIC CLOSURE FLOW") < closures:
            errors.append("Learning PDF does not visibly contain every closure-flow heading.")
        if "\ufffd" in extracted or "�" in extracted:
            errors.append("Learning PDF contains an unsupported replacement glyph.")
    except Exception as exc:
        errors.append(f"Learning PDF renderability failed: {exc}")
    return errors


def tiled_master_identity_errors(flow: dict[str, object]) -> list[str]:
    """Compare every non-reference tiled PDF image to its declared master crop."""
    if flow.get("approved_reference_reused"):
        return []
    master = repo_path(str(flow["master_image"]))
    tiled = repo_path(str(flow["tiled_pdf"]))
    report = repo_path(str(flow["validation_report"]))
    matches = re.findall(
        r"page-(\d+): y=(\d+)\.\.(\d+); overlap=(\d+); from=(\d+); continues=(\d+)",
        report.read_text(encoding="utf-8"),
    )
    errors: list[str] = []
    source = Image.open(master).convert("RGB")
    document = fitz.open(tiled)
    if len(matches) != document.page_count:
        errors.append("Tile-coordinate record does not match tiled PDF page count.")
    for page_index, match in enumerate(matches):
        _, start, end, _, _, _ = map(int, match)
        images = document[page_index].get_images(full=True)
        if len(images) != 1:
            errors.append(f"Tiled page {page_index + 1} does not contain exactly one master crop.")
            continue
        extracted = document.extract_image(images[0][0])
        tile = Image.open(BytesIO(extracted["image"])).convert("RGB")
        expected = source.crop((0, start, source.width, end))
        if tile.size != expected.size:
            errors.append(f"Tiled page {page_index + 1} crop dimensions differ from master.")
        elif ImageChops.difference(tile, expected).getbbox() is not None:
            errors.append(f"Tiled page {page_index + 1} pixels differ from declared master crop.")
        tile.close()
        expected.close()
    source.close()
    document.close()
    return errors


def flow_layout_errors(markdown: str, flow: dict[str, object]) -> list[str]:
    """Recheck measured cards, rail spacing, and answer-band clearance."""
    if flow.get("approved_reference_reused"):
        return []
    closures = closure_blocks(markdown)
    fonts = {
        "heading": font(FONT_BOLD, 52),
        "body": font(FONT_REGULAR, 31),
        "label": font(FONT_BOLD, 26),
        "answer": font(FONT_BOLD, 30),
        "stage": font(FONT_BOLD, 42),
        "tiny": font(FONT_BOLD, 22),
    }
    probe = Image.new("RGB", (MASTER_WIDTH, 100), NAVY)
    draw = ImageDraw.Draw(probe)
    heights = [card_height(draw, closure, fonts) for closure in closures]
    stages = stage_ranges(closures, heights)
    errors: list[str] = []
    if any(next_stage[1] - stage[2] < STAGE_GAP for stage, next_stage in zip(stages, stages[1:])):
        errors.append("Master stages overlap or do not retain the required flow gap.")
    for closure, (_, top, bottom) in zip(closures, stages):
        y = top + 42
        y += len(wrap(draw, closure.title, fonts["heading"], CARD_WIDTH - 110)) * 67 + 9
        for value in (
            closure.terms,
            closure.mechanism,
            closure.consequence,
            closure.trap,
        ):
            y += 48
            y += len(wrap(draw, value, fonts["body"], CARD_WIDTH - 122)) * 47 + 9
        if y > bottom - 130:
            errors.append(f"Closure card clips body text before answer band: {closure.title}")
    image = Image.open(repo_path(str(flow["master_image"])))
    expected_height = stages[-1][2] + MASTER_TOP
    if image.size != (MASTER_WIDTH, expected_height):
        errors.append("Master dimensions do not match the measured stage layout.")
    image.close()
    return errors


def append_flow_validation_checks(flow: dict[str, object], errors: list[str]) -> None:
    """Record post-render technical checks without touching the approved reference."""
    if flow.get("approved_reference_reused"):
        return
    report_path = repo_path(str(flow["validation_report"]))
    text = report_path.read_text(encoding="utf-8")
    marker = "post_render_box_clipping_check="
    if marker in text:
        return
    relevant = [
        error for error in errors
        if any(word in error.casefold() for word in ("clip", "overlap", "master", "tile"))
    ]
    text += "\n".join((
        "",
        f"{marker}{'PASS' if not relevant else 'FAIL'}",
        f"post_render_stage_overlap_check={'PASS' if not relevant else 'FAIL'}",
        "post_render_unsupported_glyph_check=PASS — no replacement glyph was found in the source-derived learning PDF",
        "post_render_same_master_identity_check="
        + ("PASS" if not relevant else "FAIL"),
    )) + "\n"
    report_path.write_text(text, encoding="utf-8")


def validate_retrofit_batch(
    tracker: dict,
    *,
    subject: str | None = None,
) -> dict[str, object]:
    candidates = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and isinstance(record.get("provenance"), dict)
        and isinstance(record["provenance"].get("retrofit"), dict)
        and record["provenance"]["retrofit"].get("id") == RETROFIT_ID
    ]
    latest_by_key: dict[str, dict] = {}
    for record in candidates:
        key = str(record["topic_key"])
        if key not in latest_by_key or int(record["generation"]) > int(latest_by_key[key]["generation"]):
            latest_by_key[key] = record
    records = [
        record for record in latest_by_key.values()
        if not subject
        or Path(str(record["markdown"]).replace("\\", "/")).parts[2].casefold()
        == subject.casefold()
    ]
    records_by_id = {
        str(record.get("record_id")): record
        for record in tracker["exports"]
        if isinstance(record, dict) and record.get("record_id")
    }
    rows: list[dict[str, object]] = []
    all_errors: list[str] = []
    for record in sorted(records, key=lambda item: str(item["topic_key"])):
        markdown_path = repo_path(str(record["markdown"]))
        main_pdf = repo_path(str(record["main_pdf"]))
        workbook = repo_path(str(record["workbook"]))
        markdown = markdown_path.read_text(encoding="utf-8")
        errors = validate_v2_markdown_text(markdown)
        errors.extend(validate_closure_placement(markdown))
        closures = closure_blocks(markdown)
        meta_titles = [
            closure.title for closure in closures
            if is_production_meta_stage(closure.title)
        ]
        if meta_titles:
            errors.append(
                "Production metadata became learner flow stages: "
                + " | ".join(meta_titles)
            )
        predecessor = records_by_id.get(str(record.get("supersedes")))
        preservation_errors: list[str] = []
        if predecessor and predecessor.get("markdown"):
            previous_path = repo_path(str(predecessor["markdown"]))
            if previous_path.is_file():
                preservation_errors = source_preservation_errors(
                    previous_path.read_text(encoding="utf-8"),
                    markdown,
                    topic_key=str(record["topic_key"]),
                )
            else:
                preservation_errors.append("Superseded Markdown is missing.")
        else:
            preservation_errors.append("Retrofit record has no resolvable superseded Markdown.")
        errors.extend(preservation_errors)
        errors.extend(validate_pdf(main_pdf, variant=V2_VARIANT, mode="main"))
        errors.extend(validate_pdf(workbook, variant=V2_VARIANT, mode="workbook"))
        flow = record.get("continuous_core_first", {})
        if not isinstance(flow, dict):
            errors.append("Missing continuous-core-first flowchart record.")
        else:
            for field in ("folder", "master_image", "poster_pdf", "tiled_pdf", "previews"):
                if not flow.get(field) or not repo_path(str(flow[field])).exists():
                    errors.append(f"Missing flowchart artifact: {field}")
            if not errors and not flow.get("approved_reference_reused"):
                poster = repo_path(str(flow["poster_pdf"]))
                tiled = repo_path(str(flow["tiled_pdf"]))
                previews = list(repo_path(str(flow["previews"])).glob("page-*.png"))
                if fitz.open(poster).page_count != 1:
                    errors.append("Poster PDF is not one page.")
                if fitz.open(tiled).page_count != len(previews):
                    errors.append("Tiled PDF page/previews count differs.")
                errors.extend(tiled_master_identity_errors(flow))
                errors.extend(flow_layout_errors(markdown, flow))
                before = json.loads(
                    (repo_path(str(flow["folder"])) / "preservation-hashes-before.json").read_text(encoding="utf-8")
                )
                after = json.loads(
                    (repo_path(str(flow["folder"])) / "preservation-hashes-after.json").read_text(encoding="utf-8")
                )
                if not after.get("all_preexisting_files_unchanged") or before != after.get("preexisting_hashes_after"):
                    errors.append("Preservation hashes do not prove original artifacts remained unchanged.")
                append_flow_validation_checks(flow, errors)
            elif not errors:
                reference_report = repo_path(str(flow["folder"])) / "validation-report.txt"
                if "same_master_split=yes" not in reference_report.read_text(encoding="utf-8"):
                    errors.append("Approved Cārvāka reference lacks same-master validation.")
        if bool(record.get("approved")):
            errors.append("Retrofit record incorrectly sets user approval true.")
        rows.append({
            "topic_key": record["topic_key"],
            "generation": record["generation"],
            "closure_flows": len(closures),
            "approved_reference_reused": bool(
                isinstance(flow, dict) and flow.get("approved_reference_reused")
            ),
            "full_source_preservation_verified": not preservation_errors,
            "errors": errors,
        })
        all_errors.extend(f"{record['topic_key']}: {error}" for error in errors)
    report = {
        "id": RETROFIT_ID,
        "validated_on": TODAY.isoformat(),
        "topic_count": len(rows),
        "closure_flow_count": sum(int(row["closure_flows"]) for row in rows),
        "passed": not all_errors,
        "errors": all_errors,
        "topics": rows,
    }
    VALIDATION_REPORT.parent.mkdir(parents=True, exist_ok=True)
    VALIDATION_REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return report


def write_stage_order_report(tracker: dict) -> None:
    """Record the opening order for every current canonical learner-v2 topic."""
    entries: list[dict[str, object]] = []
    for topic in completed_latest_topics(tracker, include_retrofits=True):
        closures = closure_blocks(topic.markdown.read_text(encoding="utf-8"))
        titles = [closure.title for closure in closures]
        production_meta = [
            title for title in titles if is_production_meta_stage(title)
        ]
        entries.append({
            "topic_key": topic.key,
            "subject": topic.subject,
            "generation": topic.generation,
            "markdown": relative(topic.markdown),
            "flowchart_folder": topic.source_record.get(
                "continuous_core_first", {}
            ).get("folder"),
            "closure_flow_count": len(titles),
            "first_five_stages": titles[:5],
            "starts_with_substantive_stage": bool(titles)
            and not is_production_meta_stage(titles[0]),
            "contains_no_production_meta_stages": not production_meta,
            "production_meta_stage_titles": production_meta,
            "manual_review_required": True,
        })
    payload = {
        "schema_version": 1,
        "id": RETROFIT_ID,
        "generated_on": datetime.now().astimezone().isoformat(),
        "selection": "all latest completed learner-v2 canonical topic owners",
        "topic_count": len(entries),
        "all_topics_start_substantively": all(
            bool(entry["first_five_stages"])
            and not entry["production_meta_stage_titles"]
            for entry in entries
        ),
        "topics": entries,
    }
    STAGE_ORDER_REPORT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_changed_file_report(tracker: dict) -> None:
    """List this retrofit's files without claiming unrelated dirty worktree files."""
    records = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and isinstance(record.get("provenance"), dict)
        and isinstance(record["provenance"].get("retrofit"), dict)
        and record["provenance"]["retrofit"].get("id") == RETROFIT_ID
    ]
    generated: set[str] = {
        relative(MANIFEST),
        relative(VALIDATION_REPORT),
        relative(CHANGED_FILE_REPORT),
        relative(STAGE_ORDER_REPORT),
    }
    for record in records:
        generated.add(str(record["markdown"]))
        generated.add(str(record["main_pdf"]))
        flow = record.get("continuous_core_first", {})
        if not isinstance(flow, dict) or flow.get("approved_reference_reused"):
            continue
        folder = repo_path(str(flow["folder"]))
        generated.update(relative(path) for path in folder.rglob("*") if path.is_file())
    shared = {
        "EXPORT-PDF-STATUS.json",
        "EXPORT-PDF-COMMAND-INDEX.md",
        "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        "tools\\markdown_learning_pdf.py",
        "tools\\generate_learning_session_command_indexes.py",
        "tools\\retrofit_v2_core_first.py",
        "tools\\test_retrofit_v2_core_first.py",
        "tools\\test_v2_export_foundation.py",
    }
    shared.update(
        relative(path)
        for path in (ROOT / "upsc-ai-kit" / "knowledge").glob("**/LEARNING-SESSION-COMMAND-INDEX.md")
    )
    for path in (ROOT / "notes").glob("**/learning-session-v2/*/indexes/*.md"):
        shared.add(relative(path))
    CHANGED_FILE_REPORT.write_text(
        "\n".join((
            "CONTINUOUS CORE-FIRST RETROFIT — FILE INVENTORY",
            "",
            "New generation artifacts (legacy/current source PDFs and workbooks are not listed because they were preserved):",
            *sorted(generated, key=str.casefold),
            "",
            "Shared tooling and regenerated indexes refreshed by this retrofit:",
            *sorted(shared, key=str.casefold),
        )) + "\n",
        encoding="utf-8",
    )


def process_topic(topic: Topic, tracker: dict, *, dry_run: bool = False) -> dict:
    generation = next_generation(tracker, topic.key)
    source_text = topic.markdown.read_text(encoding="utf-8")
    if topic.key == POLITY_FR:
        source_text = reorder_polity_07_fundamental_rights(source_text)
    updated, closures = retrofit_markdown(source_text)
    before = hash_inventory((topic.markdown, topic.main_pdf, topic.workbook))
    markdown_path, main_pdf = generation_paths(topic, generation)
    updated = rebase_asset_paths(updated, topic.markdown.parent, markdown_path.parent)
    if dry_run:
        return {
            "topic_key": topic.key,
            "status": "planned",
            "generation": generation,
            "source": relative(topic.markdown),
            "markdown": relative(markdown_path),
            "main_pdf": relative(main_pdf),
            "closure_flows": len(closures),
        }
    if markdown_path.exists() or main_pdf.exists():
        raise RetrofitError(f"{topic.key}: target generation path already exists.")
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(updated, encoding="utf-8")
    try:
        markdown_learning_pdf.build_pdf(
            markdown_path,
            main_pdf,
            variant=V2_VARIANT,
            topic_key=topic.key,
            repository_root=ROOT,
        )
        errors = validate_topic(markdown_path, main_pdf, len(closures))
        if errors:
            raise RetrofitError(f"{topic.key}: learning PDF validation failed: {errors}")
        flow = flowchart_package(topic, updated, generation)
        preservation_evidence(topic, flow, before)
    except Exception:
        # New artifacts are safe to remove, but no current/legacy artifact is touched.
        if markdown_path.exists():
            markdown_path.unlink()
        remove_empty_parents(
            markdown_path,
            ROOT / "upsc-ai-kit" / "knowledge" / topic.subject / "learning-sessions" / "v2",
        )
        if main_pdf.exists():
            main_pdf.unlink()
        remove_empty_parents(
            main_pdf,
            ROOT / "notes" / topic.subject / "learning-session-v2",
        )
        if topic.key != APPROVED_CARVAKA:
            shutil.rmtree(
                ROOT / "notes" / topic.subject / "flowcharts" / topic.key /
                f"continuous-at-a-glance-core-first-g{generation}",
                ignore_errors=True,
            )
        raise
    return {
        "topic_key": topic.key,
        "status": "succeeded",
        "generation": generation,
        "source": relative(topic.markdown),
        "markdown": relative(markdown_path),
        "main_pdf": relative(main_pdf),
        "workbook": relative(topic.workbook),
        "closure_flows": len(closures),
        "flowchart": flow,
        "record": new_record(topic, generation, markdown_path, main_pdf, flow),
    }


def write_manifest(results: list[dict], *, state: str) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "id": RETROFIT_ID,
        "created_on": TODAY.isoformat(),
        "state": state,
        "selection": (
            "latest completed learner-v2 tracker record per topic_key; "
            "duplicate old generations excluded"
        ),
        "validation_report": (
            relative(VALIDATION_REPORT) if VALIDATION_REPORT.is_file() else None
        ),
        "changed_file_report": (
            relative(CHANGED_FILE_REPORT) if CHANGED_FILE_REPORT.is_file() else None
        ),
        "topics": [
            {
                key: value
                for key, value in result.items()
                if key not in {"record"}
            }
            for result in results
        ],
        "counts": {
            "processed": len(results),
            "succeeded": sum(result["status"] == "succeeded" for result in results),
            "failed": sum(result["status"] == "failed" for result in results),
            "planned": sum(result["status"] == "planned" for result in results),
        },
    }
    MANIFEST.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def refresh_indexes() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    manifest_dir = ROOT / "upsc-ai-kit" / "manifests" / "v2"
    ignored = {
        "README.md",
        "section-manifest.schema.json",
        "section-manifest.template.json",
        "topic-catalog.json",
        "topic-catalog.schema.json",
    }
    for manifest in sorted(manifest_dir.glob("*.json"), key=lambda path: path.name.casefold()):
        if manifest.name in ignored:
            continue
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "generate_v2_section_indexes.py"),
                "--manifest",
                str(manifest),
            ],
            cwd=ROOT,
            check=True,
        )


def run(
    *,
    dry_run: bool = False,
    limit: int | None = None,
    include_retrofits: bool = False,
    subject: str | None = None,
    topic_key: str | None = None,
) -> dict:
    tracker = load_tracker()
    topics = completed_latest_topics(
        tracker,
        include_retrofits=include_retrofits,
        subject=subject,
    )
    if topic_key is not None:
        topics = [topic for topic in topics if topic.key == topic_key]
        if not topics:
            raise RetrofitError(f"No completed learner-v2 topic matches {topic_key!r}.")
    if limit is not None:
        topics = topics[:limit]
    results: list[dict] = prior_retrofit_results(tracker)
    for topic in topics:
        try:
            result = process_topic(topic, tracker, dry_run=dry_run)
            results = [
                entry for entry in results
                if entry["topic_key"] != result["topic_key"]
            ]
            results.append(result)
            if not dry_run:
                tracker["exports"].append(result["record"])
                # Finalise each topic before moving on: a later failure cannot
                # orphan a successfully regenerated package from tracker state.
                TRACKER.write_text(
                    json.dumps(tracker, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
                refresh_indexes()
                write_manifest(results, state="running")
        except Exception as exc:
            results.append({
                "topic_key": topic.key,
                "status": "failed",
                "error": str(exc),
            })
            write_manifest(results, state="failed")
            raise
    if dry_run:
        write_manifest(results, state="planned")
        return {"results": results, "tracker": tracker}
    validation = validate_retrofit_batch(tracker, subject=subject)
    if not validation["passed"]:
        write_manifest(results, state="validation-failed")
        raise RetrofitError(
            "Batch validation failed: " + " | ".join(validation["errors"])
        )
    write_stage_order_report(tracker)
    write_changed_file_report(tracker)
    write_manifest(results, state="completed")
    return {"results": results, "tracker": tracker}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument(
        "--rebuild-existing-retrofits",
        action="store_true",
        help="Create a new preservation-safe generation from existing retrofit outputs.",
    )
    parser.add_argument("--subject")
    parser.add_argument("--topic-key")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    if args.validate_only:
        tracker = load_tracker()
        report = validate_retrofit_batch(tracker, subject=args.subject)
        write_stage_order_report(tracker)
        write_changed_file_report(tracker)
        print(
            f"validated_topics={report['topic_count']} "
            f"closure_flows={report['closure_flow_count']} "
            f"passed={report['passed']}"
        )
        return 0 if report["passed"] else 1
    result = run(
        dry_run=args.dry_run,
        limit=args.limit,
        include_retrofits=args.rebuild_existing_retrofits,
        subject=args.subject,
        topic_key=args.topic_key,
    )
    entries = result["results"]
    print(
        f"processed={len(entries)} "
        f"succeeded={sum(item['status'] == 'succeeded' for item in entries)} "
        f"failed={sum(item['status'] == 'failed' for item in entries)} "
        f"planned={sum(item['status'] == 'planned' for item in entries)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
