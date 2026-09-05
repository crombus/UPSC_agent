"""Validate learner-first v2 Markdown, paths, PDFs, and tracker records."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import notions_style_ascii_master as ascii_master


LEGACY_VARIANT = "legacy-v1"
V2_VARIANT = "learner-v2"
# Retained for compatibility with older topic-specific tests and manifests.
# Validation now applies the strict rotation policy repository-wide.
STRICT_ABCD_TOPIC_KEYS = {
    "philosophy-paper-i-western-philosophy-01",
    "philosophy-paper-i-western-philosophy-02",
    "philosophy-paper-i-western-philosophy-03",
    "philosophy-paper-i-western-philosophy-04",
    "philosophy-paper-i-western-philosophy-05",
    "philosophy-paper-i-western-philosophy-06",
    "philosophy-paper-i-western-philosophy-07",
    "philosophy-paper-i-western-philosophy-08",
    "philosophy-paper-i-western-philosophy-09",
    "philosophy-paper-i-western-philosophy-10",
    "philosophy-paper-i-western-philosophy-11",
    "philosophy-paper-ii-socio-political-philosophy-02",
    "philosophy-paper-ii-socio-political-philosophy-03",
    "philosophy-paper-ii-socio-political-philosophy-04",
    "philosophy-paper-ii-socio-political-philosophy-05",
    "philosophy-paper-ii-socio-political-philosophy-06",
    "philosophy-paper-ii-socio-political-philosophy-07",
    "philosophy-paper-ii-philosophy-of-religion-10",
    "polity-13",
    "polity-14",
    "polity-15",
    "polity-16",
    "polity-17",
    "polity-38",
    "polity-39",
    "polity-40",
    "polity-41",
    "polity-42",
}
ADVANCED_HEADING = "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"
REFRESHED_ROOT = "Learner-v2-Refreshed"
SESSION_HEADING = re.compile(
    r"^SESSION\s+(\d+)\s*[—-]\s*(.+)$",
    re.IGNORECASE,
)
LEGACY_PROGRESS_NAVIGATION_RE = re.compile(
    r"^.*\bProgress\s*:\s*(?:\*\*)?\s*\d+\s*/\s*\d+\b.*$",
    re.IGNORECASE,
)
SESSION_CONTRACT_HEADINGS = (
    "DEFINITION / WHAT THIS IS CALLED",
    "ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM",
    "MUST-WRITE KEYWORDS",
)
ASCII_MASTER_HEADING = "COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM"
ASCII_DESIGN_MANIFEST_NAME = (
    "notions-style-ascii-master-design-2026-08-23.json"
)
EDITORIAL_CLASSIFICATION_RE = re.compile(
    r"\bClassification\s*:\s*"
    r"(?:CORE|SUPPORTING|OPTIONAL(?:\s+ADVANCED)?)"
    r"(?:\s+(?:PRELIMS|MAINS))?"
    r"(?:\s*\+\s*(?:CORE|SUPPORTING|OPTIONAL(?:\s+ADVANCED)?)"
    r"(?:\s+(?:PRELIMS|MAINS))?)*",
    re.IGNORECASE,
)
EDITORIAL_TAG_RE = re.compile(
    r"\[(?:CORE\s+(?:PRELIMS|MAINS)|SUPPORTING(?:\s+(?:PRELIMS|MAINS))?|"
    r"OPTIONAL\s+ADVANCED|CURRENT-AFFAIRS\s+LINK)\]",
    re.IGNORECASE,
)
EDITORIAL_AID_LINE_RE = re.compile(
    r"^(?:"
    r"CORE\s+(?:PRELIMS|MAINS)(?:\s*\+\s*(?:CORE|SUPPORTING)\s+(?:PRELIMS|MAINS))?|"
    r"SUPPORTING(?:\s+(?:PRELIMS|MAINS))?|"
    r"CURRENT-AFFAIRS\s+LINK|"
    r"PRE-TEACH\s+CHECKLIST|"
    r"BOOK\s+CONTEXT(?:\s*:.*)?|"
    r"CA\s+(?:SEARCH|FOUND)(?:\s*:.*)?|"
    r"CAPTION\s*:.*|SEARCH\s+FINDING(?:\s*:.*)?|"
    r"CURRENT(?:-AFFAIRS)?\s+(?:ANCHOR|LINK|NOTE)(?:\s*:.*)?|"
    r"(?:NEWS|EVENT|REPORT)\s+(?:NOTE|ANCHOR|SUMMARY)(?:\s*:.*)?|"
    r"PROGRESS\s*:.*|STAGE\s*:.*|"
    r"SOURCE(?:-COMPLETE)?\s+(?:AUDIT|COVERAGE|OWNERSHIP|ORDER|LEDGER).*|"
    r"(?:COVERAGE|OWNERSHIP|PUBLICATION)\s+(?:AUDIT|METADATA|LEDGER).*|"
    r"(?:CATALOGUE|GENERATION)\s+IDENTITY\s*:.*|"
    r"APPROVAL\s*:.*|EVIDENCE\s+KEY\s*:.*|"
    r"ROADMAP(?:\s*:.*)?|LEARNING\s+ROADMAP(?:\s*:.*)?|"
    r"UPSC\s+TRAP|FACT|ANALYSIS|INFERENCE|LIMIT|ANSWER"
    r")$",
    re.IGNORECASE,
)
EDITORIAL_PREFIX_RE = re.compile(
    r"^(?:Major\s+(?:criticism|reply)|High-value\s+transition|"
    r"Recommended\s+opening\s+definition|Core\s+argument|"
    r"What\s+it\s+preserves\s+or\s+explains)\s*:\s*",
    re.IGNORECASE,
)
GENERIC_KEYWORD_RE = re.compile(
    r"^(?:answer|analysis|classification|concept|context|definition|effect|"
    r"evidence|fact|factor|feature|framework|impact|inference|mechanism|"
    r"process|question|roadmap|source|stage|supporting|trap|upsc\s+trap|"
    r"worthiness|owner\s+link|preservation\s+note|in\s+simple\s+words|"
    r"memory\s+line|search\s+finding|current|do|core\s+argument|"
    r"recommended\s+opening\s+definition|high-value\s+transition)$",
    re.IGNORECASE,
)
MONTH_RE = re.compile(
    r"^(?:january|february|march|april|may|june|july|august|september|"
    r"october|november|december)$",
    re.IGNORECASE,
)
METADATA_CONTENT_RE = re.compile(
    r"(?:^|\b)(?:caption|search finding|current-affairs|current affairs|"
    r"pre-teach|book context|ca search|ca found|source note|audit report|"
    r"news service|press release|monthly report|live search|live source|"
    r"curriculum discussion)(?:\b|:)",
    re.IGNORECASE,
)
EVENT_OPENING_RE = re.compile(
    r"^(?:✅\s*)?(?:Fact\s*:?\s*)?(?:In\s+|On\s+)?"
    r"(?:\d{1,2}\s+)?(?:January|February|March|April|May|June|July|August|"
    r"September|October|November|December)\s+\d{4}\b|"
    r"^In\s+\d{4},\s+[A-Z][A-Za-z.'’-]+(?:\s+[A-Z][A-Za-z.'’-]+){0,4}\s+"
    r"(?:stated|said|reported|announced|argued)\b|"
    r"^(?:The\s+)?(?:High Commission|Ministry|PIB|Religion News Service|"
    r"Supreme Court|NCS)\b.*\b(?:reported|announced|released|held|stated)\b",
    re.IGNORECASE,
)
DEFINITION_ROLE_RE = re.compile(
    r"\b(?:is|are|was|were|means|refers\s+to|denotes|describes|"
    r"is\s+called|are\s+called|consists\s+of|comprises|constitutes|"
    r"is\s+the\s+process|is\s+the\s+doctrine|is\s+the\s+theory|"
    r"occurs\s+when|arises\s+when|gives|links|connects|shows|explains|"
    r"depends\s+on|includes|holds\s+that)\b",
    re.IGNORECASE,
)
CONSEQUENCE_LEAD_RE = re.compile(
    r"^(?:because|therefore|thus|hence|consequently|although|however|"
    r"while|whereas|unlike|so\b|do\s+not|avoid\b|it\s+does\s+not|"
    r"the\s+exam-safe\s+lesson|upsc\b)",
    re.IGNORECASE,
)
TRAP_ROLE_RE = re.compile(
    r"\b(?:not|never|avoid|do\s+not|must\s+not|cannot|wrong|trap|"
    r"distinguish|do\s+not\s+equate|should\s+not|only\s+when|"
    r"rather\s+than|while|but|limit|qualification)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class SectionSpec:
    key: str
    canonical: str
    pattern: re.Pattern[str]


@dataclass(frozen=True)
class Heading:
    line_index: int
    text: str


@dataclass(frozen=True)
class PdfIndexEntry:
    level: int
    title: str
    page: int


@dataclass(frozen=True)
class PdfIndexInfo:
    page_count: int
    index_page: int | None
    index_text: str
    entries: tuple[PdfIndexEntry, ...]
    page_texts: tuple[str, ...]


SECTION_SPECS = (
    SectionSpec(
        "basic",
        "BASIC LEARNING SESSION",
        re.compile(r"^BASIC LEARNING SESSION$", re.IGNORECASE),
    ),
    SectionSpec(
        "mcqs",
        "BASIC MCQS / REMEDIATION",
        re.compile(r"^BASIC MCQS?\s*(?:/|AND)\s*REMEDIATION$", re.IGNORECASE),
    ),
    SectionSpec(
        "practice",
        "PYQS AND ANSWER PRACTICE",
        re.compile(r"^PYQS?\s*(?:/|AND|&)\s*ANSWER PRACTICE$", re.IGNORECASE),
    ),
    SectionSpec(
        "advanced",
        ADVANCED_HEADING,
        re.compile(
            r"^OPTIONAL ADVANCED DEPTH\s*[—-]\s*"
            r"NOT REQUIRED FOR A CORE ANSWER$",
            re.IGNORECASE,
        ),
    ),
    SectionSpec(
        "register",
        "CONSOLIDATED REGISTER NOTES",
        re.compile(r"^CONSOLIDATED REGISTER NOTES$", re.IGNORECASE),
    ),
)

PDF_INDEX_TITLES = {
    "main": "CONTENTS / SESSION INDEX",
    "workbook": "CONTENTS / WORKBOOK INDEX",
}

PDF_REQUIRED_SECTIONS = {
    "main": tuple(spec.canonical for spec in SECTION_SPECS),
    "workbook": (
        SECTION_SPECS[1].canonical,
        SECTION_SPECS[2].canonical,
    ),
}


def split_frontmatter(markdown: str) -> tuple[str, str]:
    normalized = markdown.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return "", normalized
    end = normalized.find("\n---\n", 4)
    if end < 0:
        return "", normalized
    return normalized[: end + 5], normalized[end + 5 :]


def clean_heading(text: str) -> str:
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def h2_headings(markdown: str) -> list[Heading]:
    _, body = split_frontmatter(markdown)
    headings: list[Heading] = []
    in_fence = False
    for index, line in enumerate(body.splitlines()):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^##(?!#)\s+(.+?)\s*$", stripped)
        if match:
            headings.append(Heading(index, clean_heading(match.group(1))))
    return headings


def match_section(text: str) -> SectionSpec | None:
    return next((spec for spec in SECTION_SPECS if spec.pattern.fullmatch(text)), None)


def legacy_progress_navigation_lines(markdown: str) -> list[tuple[int, str]]:
    """Return obsolete interactive progress markers outside fenced code blocks."""
    matches: list[tuple[int, str]] = []
    in_fence = False
    for line_number, line in enumerate(markdown.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and LEGACY_PROGRESS_NAVIGATION_RE.fullmatch(line):
            matches.append((line_number, line))
    return matches


def strip_legacy_progress_navigation(markdown: str) -> str:
    """Remove obsolete Progress X/Y navigation while preserving teaching content."""
    trailing_newline = markdown.endswith(("\n", "\r"))
    marker_lines = {
        line_number
        for line_number, _ in legacy_progress_navigation_lines(markdown)
    }
    if not marker_lines:
        return markdown
    cleaned = "\n".join(
        line
        for line_number, line in enumerate(markdown.splitlines(), 1)
        if line_number not in marker_lines
    )
    return cleaned + ("\n" if trailing_newline else "")


def validate_v2_markdown_text(markdown: str) -> list[str]:
    """Return structural errors for the canonical learner-first v2 sequence."""
    headings = h2_headings(markdown)
    errors: list[str] = []
    matched: dict[str, list[Heading]] = {spec.key: [] for spec in SECTION_SPECS}
    progress_markers = legacy_progress_navigation_lines(markdown)
    if progress_markers:
        lines = ", ".join(str(line_number) for line_number, _ in progress_markers[:8])
        errors.append(
            "Legacy Progress X/Y navigation is not allowed in learner-v2 Markdown; "
            f"use the SESSION hierarchy only (line(s): {lines})."
        )

    for heading in headings:
        spec = match_section(heading.text)
        if spec:
            matched[spec.key].append(heading)
        else:
            errors.append(
                f"Unexpected H2 section {heading.text!r}; v2 subtopics must use H3 or lower."
            )

    for spec in SECTION_SPECS:
        occurrences = matched[spec.key]
        if not occurrences:
            errors.append(f"Missing canonical H2 section: {spec.canonical}")
        elif len(occurrences) > 1:
            errors.append(f"Duplicate canonical H2 section: {spec.canonical}")

    if errors:
        return errors

    positions = [matched[spec.key][0].line_index for spec in SECTION_SPECS]
    if positions != sorted(positions):
        errors.append(
            "V2 H2 sections are out of order; required order is: "
            + " -> ".join(spec.canonical for spec in SECTION_SPECS)
        )

    if headings and matched["basic"][0] != headings[0]:
        errors.append("BASIC LEARNING SESSION must be the first H2 section.")
    if headings and matched["register"][0] != headings[-1]:
        errors.append("CONSOLIDATED REGISTER NOTES must be the final H2 section.")

    advanced_text = matched["advanced"][0].text
    if clean_heading(advanced_text).upper().replace("-", "—") != ADVANCED_HEADING:
        errors.append(
            f"Advanced H2 must use the canonical label: {ADVANCED_HEADING}"
        )
    return errors


def validate_v2_markdown(path: str | Path) -> list[str]:
    source = Path(path)
    if not source.is_file():
        return [f"Markdown file does not exist: {source}"]
    return validate_v2_markdown_text(source.read_text(encoding="utf-8"))


def markdown_heading_ranges(
    markdown: str,
    *,
    level: int,
) -> list[tuple[int, int, str]]:
    """Return non-fenced Markdown heading ranges at one exact level."""
    _, body = split_frontmatter(markdown)
    lines = body.splitlines()
    prefix = "#" * level
    heading_re = re.compile(rf"^{re.escape(prefix)}(?!#)\s+(.+?)\s*$")
    positions: list[tuple[int, str]] = []
    in_fence = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = heading_re.fullmatch(stripped)
        if match:
            positions.append((index, clean_heading(match.group(1))))
    return [
        (
            start,
            positions[position + 1][0] if position + 1 < len(positions) else len(lines),
            title,
        )
        for position, (start, title) in enumerate(positions)
    ]


def basic_session_text(markdown: str) -> str:
    """Return only the canonical Basic H2 body."""
    _, body = split_frontmatter(markdown)
    lines = body.splitlines()
    headings = h2_headings(body)
    locations = {
        match_section(heading.text).key: heading.line_index
        for heading in headings
        if match_section(heading.text)
    }
    if "basic" not in locations or "mcqs" not in locations:
        return ""
    return "\n".join(lines[locations["basic"] + 1 : locations["mcqs"]])


def clean_aid_value(value: str) -> str:
    """Normalize one generated semantic-aid value without changing its meaning."""
    value = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_`#>]", "", value)
    value = re.sub(
        r"^\[(?:FACT|ANALYSIS|INFERENCE|LIMIT|TRAP)]\s*",
        "",
        value,
        flags=re.IGNORECASE,
    )
    return re.sub(r"\s+", " ", value).strip()


def semantic_value_reasons(
    value: str,
    *,
    field: str,
) -> list[str]:
    """Return deterministic semantic-quality reasons for one aid value."""
    cleaned = clean_aid_value(value)
    reasons: list[str] = []
    if not cleaned:
        return ["empty semantic aid"]
    if EDITORIAL_CLASSIFICATION_RE.search(cleaned):
        reasons.append("editorial classification metadata")
    if EDITORIAL_TAG_RE.search(cleaned):
        reasons.append("editorial relevance tag")
    if EDITORIAL_AID_LINE_RE.fullmatch(cleaned):
        reasons.append("editorial, audit, navigation or source metadata")
    if EDITORIAL_PREFIX_RE.match(cleaned):
        reasons.append("editorial answer-role label")
    if re.match(r"^[.,;:!?]\s*\w", cleaned):
        reasons.append("leading-punctuation sentence fragment")
    if re.match(r"^\. The\b", cleaned, re.IGNORECASE):
        reasons.append("malformed '. The' sentence fragment")
    if re.match(r"^(?:The|This)\s+visual\b", cleaned, re.IGNORECASE):
        reasons.append("visual caption selected as semantic content")
    if METADATA_CONTENT_RE.search(cleaned):
        reasons.append("caption, current-affairs, source or search metadata")
    if field in {"plain", "technical", "opening"} and EVENT_OPENING_RE.search(
        cleaned
    ):
        reasons.append("dated news or event text selected as conceptual content")
    if field == "closure.start":
        return list(dict.fromkeys(reasons))
    if field.startswith("keyword"):
        word_count = len(re.findall(r"\b[\w'’.-]+\b", cleaned))
        if GENERIC_KEYWORD_RE.fullmatch(cleaned):
            reasons.append("generic or bare label, not a topic-specific keyword")
        if MONTH_RE.fullmatch(cleaned) or re.fullmatch(r"\d{4}", cleaned):
            reasons.append("month or year alone is not a substantive keyword")
        if METADATA_CONTENT_RE.search(cleaned):
            reasons.append("metadata selected as a keyword")
        if word_count > 9 or (
            cleaned.endswith((".", "!", "?"))
            and word_count >= 6
        ):
            reasons.append("full prose sentence selected as a keyword")
        return list(dict.fromkeys(reasons))

    word_count = len(re.findall(r"\b[\w'’.-]+\b", cleaned))
    if word_count < 6:
        reasons.append("incomplete or low-information fragment")
    if field in {"plain", "technical", "opening", "how"} and not cleaned.endswith(
        (".", "!", "?")
    ):
        reasons.append("incomplete sentence without terminal punctuation")
    return list(dict.fromkeys(reasons))


def semantic_aid_defects(
    markdown: str,
    *,
    topic_key: str | None = None,
) -> list[dict[str, object]]:
    """Return exact topic/session/field/reason records for learner-v2 aids."""
    basic = basic_session_text(markdown)
    ranges = markdown_heading_ranges(basic, level=3)
    sessions = [
        (start, end, title, SESSION_HEADING.fullmatch(title))
        for start, end, title in ranges
        if SESSION_HEADING.fullmatch(title)
    ]
    lines = basic.splitlines()
    defects: list[dict[str, object]] = []

    for start, end, title, match in sessions:
        session = "\n".join(lines[start + 1 : end]).strip()
        session_number = int(match.group(1))

        def add(field: str, value: str, reason: str) -> None:
            defects.append(
                {
                    "topic_key": topic_key,
                    "session": session_number,
                    "session_title": match.group(2).strip(),
                    "field": field,
                    "value": clean_aid_value(value),
                    "reason": reason,
                }
            )

        field_patterns = {
            "plain": (
                r"\*\*Plain-language definition:\*\*\s*(.+?)\s*(?=\n|$)"
            ),
            "technical": (
                r"\*\*Technical definition:\*\*\s*(.+?)\s*(?=\n|$)"
            ),
            "opening": (
                r"####\s+ANSWER-GRABBING OPENING.*?\n+\s*>\s*(.+?)\s*(?=\n|$)"
            ),
            "how": r"\*\*How to use them:\*\*\s*(.+?)\s*(?=\n|$)",
        }
        values: dict[str, str] = {}
        for field, pattern in field_patterns.items():
            found = re.search(pattern, session, re.IGNORECASE | re.DOTALL | re.MULTILINE)
            value = found.group(1).strip() if found else ""
            values[field] = value
            for reason in semantic_value_reasons(value, field=field):
                add(field, value, reason)

        keyword_match = re.search(
            r"(?is)####\s+MUST-WRITE KEYWORDS\s*(.*?)(?=^####\s+|\Z)",
            session,
            re.MULTILINE,
        )
        keyword_text = keyword_match.group(1) if keyword_match else ""
        keywords = [
            item.strip()
            for item in re.findall(
                r"(?m)^\s*[-*]\s+\*\*(.+?)\*\*\s*$",
                keyword_text,
            )
        ]
        if not 4 <= len(keywords) <= 8:
            add(
                "keywords",
                " | ".join(keywords),
                f"requires 4-8 topic-specific keywords; found {len(keywords)}",
            )
        normalized_keywords = [clean_aid_value(item).casefold() for item in keywords]
        if len(normalized_keywords) != len(set(normalized_keywords)):
            add("keywords", " | ".join(keywords), "duplicate keyword entries")
        for number, keyword in enumerate(keywords, 1):
            for reason in semantic_value_reasons(
                keyword,
                field=f"keyword[{number}]",
            ):
                add(f"keyword[{number}]", keyword, reason)
        title_text = match.group(2).strip()
        meaningful = [
            keyword
            for keyword in keywords
            if not GENERIC_KEYWORD_RE.fullmatch(clean_aid_value(keyword))
        ]
        if meaningful and all(
            clean_aid_value(keyword).casefold() == title_text.casefold()
            for keyword in meaningful
        ):
            add(
                "keywords",
                " | ".join(keywords),
                "session title is the only meaningful keyword",
            )

        opening = clean_aid_value(values.get("opening", ""))
        how = clean_aid_value(values.get("how", ""))
        if opening and how and opening.casefold() == how.casefold():
            add("how", how, "How to use them duplicates the answer opening")

        closing = re.search(
            r"(?is)^####\s+CLOSING RECALL FLOW(?:\s*[—-][^\n]*)?\s*$"
            r"\s*```(?:text|closure-flow)\s*(.*?)```",
            session,
            re.MULTILINE,
        )
        if closing:
            closure_fields = (
                ("closure.start", r"^(?:START / CONCEPT|STARTING CONCEPT):\s*(.+)$"),
                (
                    "closure.keywords",
                    r"^(?:EXACT TERMS|KEY TERMS / DEFINITIONS):\s*(.+)$",
                ),
                (
                    "closure.mechanism",
                    r"^MECHANISM / ARGUMENT:\s*(.+)$",
                ),
                (
                    "closure.consequence",
                    r"^CONSEQUENCE / CONTRAST:\s*(.+)$",
                ),
                (
                    "closure.trap",
                    r"^UPSC TRAP / ANSWER-USE:\s*(.+)$",
                ),
                (
                    "closure.opening",
                    r"^ANSWER-GRABBING FORMULATION:\s*(.+)$",
                ),
            )
            for field, pattern in closure_fields:
                found = re.search(pattern, closing.group(1), re.IGNORECASE | re.MULTILINE)
                value = found.group(1).strip() if found else ""
                if field == "closure.keywords":
                    closure_keywords = [
                        item.strip()
                        for item in re.split(r"\s*(?:·|\|)\s*", value)
                        if item.strip()
                    ]
                    if not 4 <= len(closure_keywords) <= 8:
                        add(
                            field,
                            value,
                            "closure requires 4-8 exact topic-specific terms",
                        )
                    for number, keyword in enumerate(closure_keywords, 1):
                        for reason in semantic_value_reasons(
                            keyword,
                            field=f"keyword[closure-{number}]",
                        ):
                            add(field, keyword, reason)
                    continue
                for reason in semantic_value_reasons(
                    value,
                    field=field,
                ):
                    add(field, value, reason)
        else:
            add("closure", "", "missing or unreadable closure-flow fields")

    return defects


DEEP_TOKEN_STOPWORDS = {
    "a",
    "an",
    "and",
    "answer",
    "architecture",
    "core",
    "distinctions",
    "for",
    "from",
    "in",
    "introduction",
    "of",
    "on",
    "session",
    "the",
    "to",
    "towards",
    "upsc",
    "with",
}


def _normalized_token(value: str) -> str:
    token = value.casefold().strip("'’.-")
    if len(token) > 5 and token.endswith("ies"):
        token = token[:-3] + "y"
    elif len(token) > 4 and token.endswith("s"):
        token = token[:-1]
    return token


def _content_tokens(value: str) -> set[str]:
    return {
        token
        for raw in re.findall(r"[A-Za-zÀ-žĀ-ž][\w'’.-]{2,}", value)
        for token in (_normalized_token(raw),)
        if token and token not in DEEP_TOKEN_STOPWORDS
    }


def _normalized_semantic(value: str) -> str:
    return re.sub(r"\W+", " ", clean_aid_value(value)).strip().casefold()


def _near_duplicate(left: str, right: str) -> bool:
    first = _normalized_semantic(left)
    second = _normalized_semantic(right)
    if not first or not second:
        return False
    if first == second:
        return True
    left_tokens = set(first.split())
    right_tokens = set(second.split())
    union = left_tokens | right_tokens
    jaccard = len(left_tokens & right_tokens) / len(union) if union else 0.0
    return (
        jaccard >= 0.88
        or difflib.SequenceMatcher(None, first, second).ratio() >= 0.93
    )


def _teaching_only_session(session: str) -> str:
    body = re.sub(
        r"(?ims)^####\s+DEFINITION / WHAT THIS IS CALLED\s*$.*?"
        r"^\*\*How to use them:\*\*[^\n]*$",
        "",
        session,
    )
    return re.sub(
        r"(?ims)^####\s+CLOSING RECALL FLOW(?:\s*[—-][^\n]*)?\s*$"
        r"\s*```(?:text|closure-flow).*?```\s*",
        "",
        body,
    )


def _session_fields(session: str) -> tuple[dict[str, str], list[str], dict[str, str]]:
    patterns = {
        "plain": r"\*\*Plain-language definition:\*\*\s*(.+?)\s*(?=\n|$)",
        "technical": r"\*\*Technical definition:\*\*\s*(.+?)\s*(?=\n|$)",
        "opening": (
            r"####\s+ANSWER-GRABBING OPENING.*?\n+\s*>\s*(.+?)\s*(?=\n|$)"
        ),
        "how": r"\*\*How to use them:\*\*\s*(.+?)\s*(?=\n|$)",
    }
    fields = {
        field: (
            found.group(1).strip()
            if (
                found := re.search(
                    pattern,
                    session,
                    re.IGNORECASE | re.DOTALL | re.MULTILINE,
                )
            )
            else ""
        )
        for field, pattern in patterns.items()
    }
    keyword_match = re.search(
        r"(?is)####\s+MUST-WRITE KEYWORDS\s*(.*?)(?=^####\s+|\Z)",
        session,
        re.MULTILINE,
    )
    keywords = re.findall(
        r"(?m)^\s*[-*]\s+\*\*(.+?)\*\*\s*$",
        keyword_match.group(1) if keyword_match else "",
    )
    closing = re.search(
        r"(?is)^####\s+CLOSING RECALL FLOW(?:\s*[—-][^\n]*)?\s*$"
        r"\s*```(?:text|closure-flow)\s*(.*?)```",
        session,
        re.MULTILINE,
    )
    closure: dict[str, str] = {}
    if closing:
        for field, pattern in (
            ("start", r"^(?:START / CONCEPT|STARTING CONCEPT):\s*(.+)$"),
            ("keywords", r"^(?:EXACT TERMS|KEY TERMS / DEFINITIONS):\s*(.+)$"),
            ("mechanism", r"^MECHANISM / ARGUMENT:\s*(.+)$"),
            ("consequence", r"^CONSEQUENCE / CONTRAST:\s*(.+)$"),
            ("trap", r"^UPSC TRAP / ANSWER-USE:\s*(.+)$"),
            ("opening", r"^ANSWER-GRABBING FORMULATION:\s*(.+)$"),
        ):
            found = re.search(pattern, closing.group(1), re.IGNORECASE | re.MULTILINE)
            closure[field] = found.group(1).strip() if found else ""
    return fields, keywords, closure


def deep_content_quality_audit_text(
    markdown: str,
    *,
    topic_key: str | None = None,
) -> dict[str, object]:
    """Audit every named session for conceptual quality and useful granularity."""
    basic = basic_session_text(markdown)
    lines = basic.splitlines()
    ranges = markdown_heading_ranges(basic, level=3)
    session_rows: list[dict[str, object]] = []
    package_defects: list[dict[str, object]] = []

    def package_add(
        category: str,
        reason: str,
        *,
        severity: str = "medium",
        value: str = "",
    ) -> None:
        package_defects.append(
            {
                "topic_key": topic_key,
                "session": None,
                "session_title": None,
                "category": category,
                "field": category,
                "severity": severity,
                "value": clean_aid_value(value),
                "reason": reason,
            }
        )

    for start, end, title in ranges:
        match = SESSION_HEADING.fullmatch(title)
        if not match:
            continue
        session = "\n".join(lines[start + 1 : end]).strip()
        fields, keywords, closure = _session_fields(session)
        title_text = match.group(2).strip()
        title_tokens = _content_tokens(title_text)
        keyword_concept_tokens = set().union(
            *(
                _content_tokens(keyword)
                for keyword in keywords
                if not GENERIC_KEYWORD_RE.fullmatch(clean_aid_value(keyword))
                and not MONTH_RE.fullmatch(clean_aid_value(keyword))
                and not re.fullmatch(r"\d{4}", clean_aid_value(keyword))
            )
        ) if keywords else set()
        alignment_tokens = title_tokens | keyword_concept_tokens
        teaching = _teaching_only_session(session)
        teaching_tokens = _content_tokens(teaching)
        defects: list[dict[str, object]] = []

        def add(
            category: str,
            field: str,
            value: str,
            reason: str,
            *,
            severity: str = "medium",
        ) -> None:
            item = {
                "topic_key": topic_key,
                "session": int(match.group(1)),
                "session_title": title_text,
                "category": category,
                "field": field,
                "severity": severity,
                "value": clean_aid_value(value),
                "reason": reason,
            }
            identity = (
                item["field"],
                item["reason"],
                _normalized_semantic(str(item["value"])),
            )
            if not any(
                (
                    existing["field"],
                    existing["reason"],
                    _normalized_semantic(str(existing["value"])),
                )
                == identity
                for existing in defects
            ):
                defects.append(item)

        for legacy in semantic_aid_defects(
            "## BASIC LEARNING SESSION\n\n"
            + f"### SESSION {match.group(1)} — {title_text}\n\n"
            + session
            + "\n\n## BASIC MCQS / REMEDIATION\n"
            + "## PYQS AND ANSWER PRACTICE\n"
            + f"## {ADVANCED_HEADING}\n"
            + "## CONSOLIDATED REGISTER NOTES\n"
            + f"### {ASCII_MASTER_HEADING}\n```text\nx\n```\n",
            topic_key=topic_key,
        ):
            reason = str(legacy["reason"])
            severity = (
                "high"
                if "metadata" in reason
                or "dated news" in reason
                or legacy["field"] in {"plain", "technical", "opening"}
                and "fragment" in reason
                else "medium"
            )
            add(
                "semantic-aid",
                str(legacy["field"]),
                str(legacy["value"]),
                reason,
                severity=severity,
            )

        for field in ("plain", "technical"):
            value = clean_aid_value(fields[field])
            value_tokens = _content_tokens(value)
            if value and CONSEQUENCE_LEAD_RE.search(value):
                add(
                    "definition-quality",
                    field,
                    value,
                    "definition is a warning, consequence, qualification or answer instruction",
                    severity="high",
                )
            if (
                value
                and field == "plain"
                and re.search(
                    r"\b(?:because|therefore)\b.*\b(?:faster|slower|longer|"
                    r"shorter|more\s+than|less\s+than|compared\s+with)\b|"
                    r"\b(?:example|illustrates?|shows?\s+that)\b",
                    value,
                    re.IGNORECASE,
                )
            ):
                add(
                    "definition-quality",
                    field,
                    value,
                    "plain definition is merely an example, comparison or consequence",
                    severity="high",
                )
            if value and alignment_tokens and not (alignment_tokens & value_tokens):
                add(
                    "definition-alignment",
                    field,
                    value,
                    "definition is not reasonably aligned with the named session",
                    severity="high",
                )
            if value and EVENT_OPENING_RE.search(value):
                add(
                    "definition-quality",
                    field,
                    value,
                    "isolated historical/current event is evidence, not a definition",
                    severity="high",
                )

        plain = clean_aid_value(fields["plain"])
        technical = clean_aid_value(fields["technical"])
        if plain and technical and _near_duplicate(plain, technical):
            precise_definition = (
                DEFINITION_ROLE_RE.search(plain)
                and bool(alignment_tokens & _content_tokens(plain))
                and not CONSEQUENCE_LEAD_RE.search(plain)
                and not EVENT_OPENING_RE.search(plain)
            )
            if not precise_definition:
                add(
                    "definition-quality",
                    "plain/technical",
                    plain,
                    "plain and technical definitions are identical without being genuinely both plain and precise",
                    severity="high",
                )

        opening = clean_aid_value(fields["opening"])
        if opening:
            if CONSEQUENCE_LEAD_RE.search(opening) and not (
                alignment_tokens & _content_tokens(opening)
            ):
                add(
                    "opening-quality",
                    "opening",
                    opening,
                    "opening is a generic warning or repeated consequence, not a conceptual answer opening",
                    severity="high",
                )
            if alignment_tokens and not (
                alignment_tokens & _content_tokens(opening)
            ):
                add(
                    "opening-alignment",
                    "opening",
                    opening,
                    "opening is unrelated to the named session",
                    severity="high",
                )

        for number, keyword in enumerate(keywords, 1):
            cleaned = clean_aid_value(keyword)
            keyword_tokens = _content_tokens(cleaned)
            if (
                GENERIC_KEYWORD_RE.fullmatch(cleaned)
                or MONTH_RE.fullmatch(cleaned)
                or re.fullmatch(r"\d{4}", cleaned)
                or METADATA_CONTENT_RE.search(cleaned)
                or cleaned.casefold() in {"do", "current", "search finding"}
            ):
                add(
                    "keyword-quality",
                    f"keyword[{number}]",
                    cleaned,
                    "keyword is metadata, a date/month, a label or a generic instruction",
                    severity="medium",
                )
        covered_title_tokens = set().union(
            *(_content_tokens(keyword) for keyword in keywords)
        ) & title_tokens if keywords else set()
        grounded_keyword_count = sum(
            bool(_content_tokens(keyword) & teaching_tokens)
            for keyword in keywords
        )
        if (
            title_tokens
            and not covered_title_tokens
            and grounded_keyword_count < min(4, len(keywords))
        ):
            add(
                "keyword-coverage",
                "keywords",
                " | ".join(keywords),
                "keywords do not reasonably cover the named doctrine, process or problem",
                severity="medium",
            )

        how = clean_aid_value(fields["how"])
        how_hits = sum(
            bool(_content_tokens(keyword) & _content_tokens(how))
            for keyword in keywords
        )
        if how and how_hits < min(3, len(keywords)):
            add(
                "guidance-quality",
                "how",
                how,
                "answer guidance does not meaningfully map the selected terms into an answer spine",
                severity="medium",
            )
        if how and opening and _near_duplicate(how, opening):
            add(
                "guidance-quality",
                "how",
                how,
                "answer guidance duplicates the opening",
                severity="medium",
            )

        closure_roles = {
            role: clean_aid_value(closure.get(role, ""))
            for role in ("mechanism", "consequence", "trap", "opening")
        }
        duplicate_pairs = [
            (left, right)
            for index, left in enumerate(closure_roles)
            for right in list(closure_roles)[index + 1 :]
            if _near_duplicate(closure_roles[left], closure_roles[right])
        ]
        if duplicate_pairs:
            add(
                "closure-quality",
                "closure",
                " | ".join(
                    f"{left}={closure_roles[left]}"
                    for pair in duplicate_pairs
                    for left in pair
                ),
                "closure nodes must be distinct; duplicate or near-identical role content found",
                severity="high" if len(duplicate_pairs) >= 3 else "medium",
            )
        trap = closure_roles["trap"]
        if trap and not TRAP_ROLE_RE.search(trap):
            add(
                "closure-quality",
                "closure.trap",
                trap,
                "trap node does not state a misconception, limit, contrast or answer qualification",
                severity="medium",
            )
        for role, value in closure_roles.items():
            if value and (
                METADATA_CONTENT_RE.search(value)
                or EVENT_OPENING_RE.search(value)
            ):
                add(
                    "closure-quality",
                    f"closure.{role}",
                    value,
                    "closure role uses caption, search, source, news or event metadata",
                    severity="high",
                )

        session_rows.append(
            {
                "session": int(match.group(1)),
                "title": title_text,
                "word_count": len(re.findall(r"\b[\w'’.-]+\b", teaching)),
                "substantive_nested_headings": len(
                    [
                        heading
                        for level in (4, 5)
                        for _, _, heading in markdown_heading_ranges(
                            teaching,
                            level=level,
                        )
                        if clean_heading(heading).casefold()
                        not in {
                            item.casefold()
                            for item in SESSION_CONTRACT_HEADINGS
                        }
                        and not clean_heading(heading)
                        .casefold()
                        .startswith("closing recall flow")
                    ]
                ),
                "status": "pass" if not defects else "fail",
                "defects": defects,
            }
        )

    if topic_key and topic_key.casefold().startswith("philosophy-"):
        if len(session_rows) < 7:
            package_add(
                "granularity",
                "Philosophy package has fewer than seven searchable major sessions",
                severity="high",
                value=str(len(session_rows)),
            )
        for row in session_rows:
            if (
                int(row["word_count"]) >= 5000
                and int(row["substantive_nested_headings"]) >= 5
            ):
                package_add(
                    "granularity",
                    "giant Philosophy session hides multiple doctrine-level blocks",
                    severity="high",
                    value=f"SESSION {row['session']}: {row['title']}",
                )

    all_defects = [
        defect
        for row in session_rows
        for defect in row["defects"]
    ] + package_defects
    blocking = [
        defect
        for defect in all_defects
        if defect["severity"] in {"blocker", "high", "medium"}
    ]
    return {
        "topic_key": topic_key,
        "session_count": len(session_rows),
        "status": "pass" if not blocking else "fail",
        "severity_counts": {
            severity: sum(
                defect["severity"] == severity for defect in all_defects
            )
            for severity in ("blocker", "high", "medium", "low")
        },
        "sessions": session_rows,
        "package_defects": package_defects,
        "defects": all_defects,
    }


def deep_content_quality_errors(
    markdown: str,
    *,
    topic_key: str | None = None,
) -> list[str]:
    audit = deep_content_quality_audit_text(markdown, topic_key=topic_key)
    return [
        (
            f"{'PACKAGE' if defect['session'] is None else 'SESSION ' + str(defect['session'])}"
            f"{'' if defect['session_title'] is None else ' — ' + str(defect['session_title'])}: "
            f"{defect['field']} [{defect['severity']}] {defect['reason']}: "
            f"{defect['value']!r}"
        )
        for defect in audit["defects"]
        if defect["severity"] in {"blocker", "high", "medium"}
    ]


def semantic_aid_quality_errors(
    markdown: str,
    *,
    topic_key: str | None = None,
) -> list[str]:
    return [
        (
            f"SESSION {defect['session']} — {defect['session_title']}: "
            f"{defect['field']} contains {defect['reason']}: "
            f"{defect['value']!r}"
        )
        for defect in semantic_aid_defects(markdown, topic_key=topic_key)
    ]


def mcq_section_text(markdown: str) -> str:
    """Return only Basic MCQs/remediation, excluding verified-PYQ practice."""
    _, body = split_frontmatter(markdown)
    lines = body.splitlines()
    headings = h2_headings(body)
    locations = {
        match_section(heading.text).key: heading.line_index
        for heading in headings
        if match_section(heading.text)
    }
    if "mcqs" not in locations or "practice" not in locations:
        return ""
    return "\n".join(lines[locations["mcqs"] + 1 : locations["practice"]])


def extract_mcq_answer_keys(markdown: str) -> list[str]:
    """Extract objective answer letters from the Basic MCQ section."""
    section = mcq_section_text(markdown)
    matches = [
        (match.start(), match.group(1).upper())
        for pattern in (
            r"(?im)^\s*>?\s*(?:✅\s*)?\*\*Answer:\s*\(?([A-D])\)?"
            r"(?:\.)?(?:\s+[^*\n]+?)?\*\*",
            r"(?im)^\s*>?\s*(?:✅\s*)?\*\*Answer:\s*\(?([A-D])\)?\.\s+",
            r"(?im)^\s*>?\s*\*\*Correct answer:\s*\(?([A-D])\)?(?:\.)?\*\*",
            r"(?im)^\s*[-*]?\s*Correct answer:\s*\(?([A-D])\)?(?:\.)?\s*$",
            r"(?im)^\s*[-*]\s*(?:CORRECT\s+)?ANSWER:\s*\(?([A-D])\)?\s+-",
        )
        for match in re.finditer(pattern, section)
    ]
    return [
        letter
        for _, letter in sorted(dict(matches).items())
    ]


def answer_key_pattern_errors(
    markdown: str,
    *,
    topic_key: str | None = None,
) -> list[str]:
    """Check the repository-wide strict A-B-C-D objective-key policy."""
    keys = extract_mcq_answer_keys(markdown)
    if not keys:
        return ["No objective answer keys were found in BASIC MCQS / REMEDIATION."]
    counts = {letter: keys.count(letter) for letter in "ABCD"}
    errors: list[str] = []
    if max(counts.values()) - min(counts.values()) > 1:
        errors.append(f"MCQ answer keys are not balanced: {counts}.")
    expected = [letter for index in range(len(keys)) for letter in "ABCD"][
        : len(keys)
    ]
    if keys != expected:
        errors.append(
            "MCQ answer keys do not follow the required strict A-B-C-D rotation."
        )
    if re.search(r"(.)\1\1", "".join(keys)):
        errors.append("MCQ answer keys contain a run of three identical answers.")
    if (
        topic_key
        and topic_key.casefold().startswith("philosophy-")
        and re.search(r"\bPrelims\s+PYQs?\b", mcq_section_text(markdown), re.I)
        and not re.search(
            r"(?:not|never|explicitly\s+not)\s+(?:a\s+)?(?:Prelims\s+)?PYQs?",
            mcq_section_text(markdown),
            re.I,
        )
    ):
        errors.append(
            "Philosophy Optional objective practice must not be described as Prelims PYQs."
        )
    return errors


def mcq_answer_text_errors(markdown: str) -> list[str]:
    """Check that an explicit answer text matches the selected option text."""
    section = mcq_section_text(markdown)
    question_matches = list(
        re.finditer(
            r"(?m)^####\s+Q?(?P<number>\d+)"
            r"(?:[.)]\s+|\s*[—:-]\s+|(?=\s*$))",
            section,
        )
    )
    errors: list[str] = []

    def normalize(text: str) -> str:
        text = re.sub(r"[*_`]", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip().rstrip(".").casefold()

    for index, question_match in enumerate(question_matches):
        block_end = (
            question_matches[index + 1].start()
            if index + 1 < len(question_matches)
            else len(section)
        )
        block = section[question_match.start() : block_end]
        options = {
            match.group("label").upper(): match.group("text").strip()
            for match in re.finditer(
                r"(?m)^\s*(?:[-*]\s*)?(?P<label>[A-D])[.)]\s+"
                r"(?P<text>.+?)\s*$",
                block,
            )
        }
        answer_match = re.search(
            r"(?im)^\s*>?\s*(?:✅\s*)?\*\*(?:Correct\s+)?Answer:\s*"
            r"\(?(?P<label>[A-D])\)?(?:\.)?\s*(?P<text>.*?)\*\*\s*$",
            block,
        )
        if not answer_match:
            continue
        answer_text = answer_match.group("text").strip()
        if not answer_text:
            continue
        label = answer_match.group("label").upper()
        option_text = options.get(label)
        if option_text is None:
            continue
        if normalize(answer_text) != normalize(option_text):
            errors.append(
                f"MCQ {question_match.group('number')} answer text does not match "
                f"option {label}: {answer_text!r} != {option_text!r}."
            )
    return errors


def validate_refreshed_markdown_text(
    markdown: str,
    *,
    topic_key: str | None = None,
    ascii_spec_path: str | Path | None = None,
) -> list[str]:
    """Validate the learner-v2 refreshed named-session and ASCII contract."""
    errors = validate_v2_markdown_text(markdown)
    basic = basic_session_text(markdown)
    ranges = markdown_heading_ranges(basic, level=3)
    sessions = [
        (start, end, title, SESSION_HEADING.fullmatch(title))
        for start, end, title in ranges
        if SESSION_HEADING.fullmatch(title)
    ]
    if not sessions:
        errors.append("BASIC LEARNING SESSION has no numbered SESSION H3 headings.")
        return errors

    numbers = [int(match.group(1)) for _, _, _, match in sessions]
    if numbers != list(range(1, len(numbers) + 1)):
        errors.append(
            "Numbered SESSION headings must be continuous from 1; "
            f"found {numbers}."
        )

    basic_lines = basic.splitlines()
    for start, end, title, _ in sessions:
        session = "\n".join(basic_lines[start + 1 : end]).strip()
        h4s = markdown_heading_ranges(session, level=4)
        h4_titles = [item[2] for item in h4s]
        required_positions: list[int] = []
        for required in SESSION_CONTRACT_HEADINGS:
            try:
                required_positions.append(
                    next(
                        index
                        for index, heading in enumerate(h4_titles)
                        if clean_heading(heading).casefold() == required.casefold()
                    )
                )
            except StopIteration:
                errors.append(f"{title}: missing {required}.")
        if len(required_positions) == len(SESSION_CONTRACT_HEADINGS):
            if required_positions != sorted(required_positions):
                errors.append(f"{title}: definition/opening/keywords are out of order.")
            if required_positions[0] != 0:
                errors.append(
                    f"{title}: DEFINITION / WHAT THIS IS CALLED must be immediately below the session heading."
                )

        definition_match = re.search(
            r"(?is)####\s+DEFINITION / WHAT THIS IS CALLED\s*(.*?)"
            r"(?=^####\s+ANSWER-GRABBING OPENING)",
            session,
            re.MULTILINE,
        )
        definition = definition_match.group(1) if definition_match else ""
        if not re.search(r"\*\*Plain-language definition:\*\*\s+\S", definition):
            errors.append(f"{title}: missing a plain-language definition.")
        if not re.search(r"\*\*Technical definition:\*\*\s+\S", definition):
            errors.append(f"{title}: missing a technical definition.")

        keyword_match = re.search(
            r"(?is)####\s+MUST-WRITE KEYWORDS\s*(.*?)(?=^####\s+|\Z)",
            session,
            re.MULTILINE,
        )
        keyword_text = keyword_match.group(1) if keyword_match else ""
        if len(re.findall(r"(?m)^\s*[-*]\s+\S", keyword_text)) < 2:
            errors.append(f"{title}: MUST-WRITE KEYWORDS needs at least two terms.")
        if not re.search(r"\*\*How to use them:\*\*\s+\S", keyword_text):
            errors.append(f"{title}: missing How to use them guidance.")

        closing_matches = list(
            re.finditer(
                r"(?im)^####\s+CLOSING RECALL FLOW(?:\s*[—-][^\n]*)?\s*$",
                session,
            )
        )
        if len(closing_matches) != 1:
            errors.append(
                f"{title}: expected exactly one CLOSING RECALL FLOW; "
                f"found {len(closing_matches)}."
            )
        elif not re.fullmatch(
            r"(?is)####\s+CLOSING RECALL FLOW(?:\s*[—-][^\n]*)?\s*\n+"
            r"```(?:text|closure-flow).*?```\s*",
            session[closing_matches[0].start() :],
        ):
            errors.append(
                f"{title}: closure must be a final text-native fenced flow before the next session."
            )

    errors.extend(
        deep_content_quality_errors(
            markdown,
            topic_key=topic_key,
        )
    )

    register_match = re.search(
        r"(?is)^##\s+CONSOLIDATED REGISTER NOTES\s*(.*)\Z",
        split_frontmatter(markdown)[1],
        re.MULTILINE,
    )
    register = register_match.group(1) if register_match else ""
    ascii_match = re.search(
        rf"(?is)^###\s+{re.escape(ASCII_MASTER_HEADING)}\s*(.*)\Z",
        register,
        re.MULTILINE,
    )
    if not ascii_match:
        errors.append(
            f"{ASCII_MASTER_HEADING} must be inside the final register notes."
        )
    else:
        errors.extend(
            validate_ascii_master_text(
                ascii_match.group(1),
                topic_key=topic_key,
                ascii_spec_path=ascii_spec_path,
            )
        )
    errors.extend(answer_key_pattern_errors(markdown, topic_key=topic_key))
    errors.extend(mcq_answer_text_errors(markdown))
    return errors


def _ascii_manifest_topic(topic_key: str | None) -> dict[str, object] | None:
    if not topic_key:
        return None
    manifest = (
        Path(__file__).resolve().parents[1]
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / ASCII_DESIGN_MANIFEST_NAME
    )
    if not manifest.is_file():
        return None
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    topics = data.get("topics", {})
    if not isinstance(topics, dict):
        return None
    value = topics.get(topic_key)
    return value if isinstance(value, dict) else None


def _manual_ascii_topic(
    topic_key: str | None,
    ascii_spec_path: str | Path | None = None,
) -> ascii_master.ManualTopicSpec | None:
    if not topic_key:
        return None
    if ascii_spec_path is not None:
        explicit = ascii_master.normalize_manual_spec_file(
            Path(ascii_spec_path)
        ).get(topic_key)
        if explicit is None:
            raise ValueError(
                f"Explicit ASCII spec does not contain topic {topic_key}: "
                f"{ascii_spec_path}"
            )
        return explicit
    spec_dir = (
        Path(__file__).resolve().parents[1]
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
    )
    try:
        registered = ascii_master.load_manual_topic_specs(spec_dir).get(topic_key)
        if registered is not None:
            return registered
    except (OSError, ValueError, json.JSONDecodeError):
        pass
    for path in sorted(spec_dir.glob("*.json")):
        try:
            discovered = ascii_master.normalize_manual_spec_file(path).get(topic_key)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        if discovered is not None:
            return discovered
    return None


def validate_ascii_master_text(
    fragment: str,
    *,
    topic_key: str | None = None,
    standalone_text: str | None = None,
    ascii_spec_path: str | Path | None = None,
) -> list[str]:
    """Reject linear session dumps and enforce a Notions-style panel topology."""
    errors: list[str] = []
    blocks = ascii_master.panel_blocks(fragment)
    headings = list(ascii_master.PANEL_HEADING_RE.finditer(fragment))
    if not blocks:
        return [
            "Final ASCII master must use labelled PANEL X/N headings with one "
            "ascii-master code block per panel."
        ]
    totals = {total for _, total, _, _ in blocks}
    expected_total = blocks[0][1]
    numbers = [number for number, _, _, _ in blocks]
    if len(totals) != 1 or expected_total != len(blocks):
        errors.append(
            "ASCII master panel headings must share a total matching the panel count."
        )
    if numbers != list(range(1, len(blocks) + 1)):
        errors.append(
            f"ASCII master panel numbers must be sequential from 1; found {numbers}."
        )
    normalized_titles = [
        re.sub(r"\s+", " ", title).strip().casefold()
        for _, _, title, _ in blocks
    ]
    if len(set(normalized_titles)) != len(normalized_titles):
        errors.append("ASCII master panel titles must be unique and topic-specific.")
    if len(headings) != len(blocks):
        errors.append("Every ASCII master panel must have exactly one fenced code block.")

    manual_spec = _manual_ascii_topic(topic_key, ascii_spec_path)
    topic_spec = _ascii_manifest_topic(topic_key)
    exception = bool(topic_spec and topic_spec.get("panel_count_exception"))
    if not exception and not 6 <= len(blocks) <= 12:
        errors.append(
            f"ASCII master requires 6–12 panels by default; found {len(blocks)}."
        )

    complete = "\n".join(body for _, _, _, body in blocks)
    if re.search(
        r"How should the complete structure|"
        r"be defined,\s*related,\s*compared and evaluated",
        complete,
        re.I,
    ):
        errors.append("ASCII master contains prohibited generic central wording.")
    placeholder_patterns = {
        "ZONE / LAYER A": r"\bZONE\s*/\s*LAYER\s+A\b",
        "CAUSE / CONDITION 1": r"\bCAUSE\s*/\s*CONDITION\s+1\b",
        "AXIS 1": r"(?im)^\s*AXIS\s+1\s*:",
    }
    authored_complete = (
        "\n".join(panel.body for panel in manual_spec.panels)
        if manual_spec is not None
        else ""
    )
    for label, pattern in placeholder_patterns.items():
        if re.search(pattern, complete) and not re.search(pattern, authored_complete):
            errors.append(f"ASCII master contains prohibited placeholder label {label}.")
    if re.search(r"\.\.\.|…", complete):
        errors.append("ASCII master contains truncation ellipses inside master nodes.")
    if len(re.findall(r"(?im)^\s*KEY TERMS\s*:", complete)) > 1:
        errors.append("ASCII master repeats prohibited KEY TERMS scaffolding.")
    if re.search(r"(?m)^\+--\s*SESSION\s+\d+", complete, re.I):
        errors.append("ASCII master contains the prohibited +-- SESSION linear dump.")
    session_dump_lines = re.findall(
        r"(?im)^\s*(?:[+|├└─-]+\s*)?SESSION\s+\d+\b",
        complete,
    )
    if len(session_dump_lines) >= max(3, len(blocks) - 1):
        errors.append("ASCII master mechanically maps panels/nodes to numbered sessions.")
    if re.search(
        r"(?im)^\s*(?:DEFINITION / TERMS|EXAM OPENING|"
        r"CONSEQUENCE / CONTRAST|TRAP / ANSWER-USE)\s*:",
        complete,
    ):
        errors.append("ASCII master pastes the obsolete closure-card field template.")

    branching_panels = 0
    signatures: set[str] = set()
    repeated_lines: dict[str, set[int]] = {}
    topology_failures: list[int] = []
    for index, (_, _, title, body) in enumerate(blocks, 1):
        nonblank = [line for line in body.splitlines() if line.strip()]
        if len(nonblank) < 4:
            errors.append(f"ASCII master panel {index} is blank or too shallow.")
        wide = [
            (line_no, len(line))
            for line_no, line in enumerate(body.splitlines(), 1)
            if len(line) > ascii_master.MAX_LINE_WIDTH
        ]
        if wide:
            errors.append(
                f"ASCII master panel {index} exceeds {ascii_master.MAX_LINE_WIDTH} "
                f"columns at lines {[line_no for line_no, _ in wide[:4]]}."
            )
        connector_lines = sum(
            bool(
                re.fullmatch(r"[\s+|/\\<>vV^=\-]+", line)
                and re.search(r"[+|/\\<>vV^=\-]", line)
            )
            for line in body.splitlines()
        )
        topology = bool(
            connector_lines >= 1
            or re.search(r"(?:->|<-|\+--|[┌┐└┘┬┴├┤┼│▼])", body)
            or (
                manual_spec is not None
                and bool(manual_spec.panels[index - 1].structural_type.strip())
            )
        )
        if not topology:
            topology_failures.append(index)
        junctions = len(re.findall(r"[┬┴├┤┼]", body))
        multi_column = bool(
            re.search(r"┌─+┬─+┐|│[^│\n]+│[^│\n]+│", body)
        )
        if junctions >= 2 or multi_column:
            branching_panels += 1
        if "┼" in body or multi_column:
            signatures.add("matrix")
        if re.search(r"[├┬]", body):
            signatures.add("branch-tree")
        if "▼" in body and re.search(
            r"\b(?:CAUSE|MECHANISM|ARGUMENT|PROCESS|STAGE|SEQUENCE)\b",
            body,
            re.I,
        ):
            signatures.add("causal-sequence")
        if re.search(r"\b(?:ZONE|LAYER|SPATIAL|CROSS-SECTION)\b", body, re.I):
            signatures.add("spatial")
        if re.search(r"\b(?:OBJECTION|PROBLEM|RESPONSE|VERDICT|LIMIT)\b", body, re.I):
            signatures.add("problem-response")
        if re.search(r"\b(?:ANSWER|REVISION|PYQ|EXAM)\b", title + "\n" + body, re.I):
            signatures.add("exam-synthesis")
        for line in nonblank:
            normalized = re.sub(r"\s+", " ", line.strip()).casefold()
            if (
                len(normalized) >= 52
                and not re.fullmatch(r"[─┌┐└┘┬┴├┤┼│▼ ]+", normalized)
                and not re.match(
                    r"^(?:system result|final control|spatial control|control:|"
                    r"compare on the same axis|sequence control):",
                    normalized,
                )
                and not normalized.startswith("key terms:")
            ):
                repeated_lines.setdefault(normalized, set()).add(index)

    if topology_failures:
        errors.append(
            "ASCII master panels lack branch/flow topology: "
            + ", ".join(map(str, topology_failures))
        )

    if manual_spec is not None:
        expected_fragment = ascii_master.build_manual_fragment(manual_spec)
        if ascii_master.normalized_panel_text(fragment) != (
            ascii_master.normalized_panel_text(expected_fragment)
        ):
            errors.append("Embedded ASCII master does not exactly match its manual spec.")
        integrity = ascii_master.manual_spec_integrity_errors(
            Path(__file__).resolve().parents[1],
            {manual_spec.topic_key: manual_spec},
        )
        errors.extend(
            f"Manual ASCII spec integrity failure: {error}"
            for error in integrity
        )
        if standalone_text is not None:
            standalone = ascii_master.normalized_panel_text(standalone_text)
            expected = ascii_master.normalized_panel_text(expected_fragment)
            if not standalone:
                errors.append("Standalone ascii-master.txt has no valid panel content.")
            elif standalone != expected:
                errors.append(
                    "Standalone ASCII master does not exactly match its manual spec."
                )
        return errors

    if branching_panels < max(4, len(blocks) // 2):
        errors.append(
            "ASCII master lacks real branching in enough panels "
            f"({branching_panels}/{len(blocks)})."
        )
    if len(signatures) < 4:
        errors.append(
            "ASCII master repeats too few structural patterns; "
            f"found {sorted(signatures)}."
        )
    duplicate_prose = [
        line for line, panels in repeated_lines.items() if len(panels) >= 3
    ]
    if duplicate_prose:
        errors.append(
            "ASCII master duplicates long closure/prose lines across panels: "
            + " | ".join(duplicate_prose[:3])
        )

    first_title = blocks[0][2]
    first_body = blocks[0][3]
    if not re.search(
        r"\b(?:CENTRAL|ROOT|QUESTION|CONCEPTUAL|ANALYTICAL)\b",
        first_title + "\n" + first_body,
        re.I,
    ):
        errors.append("ASCII master first panel lacks a central question/root concept.")
    all_titles = "\n".join(title for _, _, title, _ in blocks)
    if not re.search(
        r"\b(?:CLASSIFICATION|CONCEPT|TAXONOM|HIERARCH|DOCTRINE|CHRONOLOG)\w*",
        all_titles + "\n" + complete,
        re.I,
    ):
        errors.append("ASCII master lacks a classification or conceptual-map panel.")
    if not re.search(
        r"\b(?:MECHANISM|ARGUMENT|CAUSE|CAUSAL|PROCESS|PROCEDURE)\b",
        all_titles + "\n" + complete,
        re.I,
    ):
        errors.append("ASCII master lacks a mechanism/argument/causal panel.")
    if not re.search(
        r"\b(?:COMPARE|COMPARISON|CONTRAST|PROBLEM|OBJECTION|RESPONSE|DEBATE)\b",
        all_titles + "\n" + complete,
        re.I,
    ):
        errors.append("ASCII master lacks a comparison or problem-response panel.")
    final_title = blocks[-1][2]
    final_body = blocks[-1][3]
    if not re.search(
        r"\b(?:ANSWER|REVISION|SYNTHESIS|SPINE)\b",
        final_title + "\n" + final_body,
        re.I,
    ):
        errors.append("ASCII master final panel is not an integrated answer/revision spine.")

    if topic_spec:
        panels = topic_spec.get("panels", [])
        concepts = [
            clean_aid_value(str(concept)).casefold()
            for panel in panels
            if isinstance(panel, dict)
            for concept in panel.get("key_concepts", [])
            if clean_aid_value(str(concept))
        ]
        unique = list(dict.fromkeys(concepts))
        normalized_complete = clean_aid_value(complete).casefold()
        covered = [
            concept for concept in unique if concept in normalized_complete
        ]
        if unique and len(covered) / len(unique) < 0.55:
            errors.append(
                "ASCII master topic-specific vocabulary coverage is too low: "
                f"{len(covered)}/{len(unique)} manifest concepts."
            )

    if standalone_text is not None:
        embedded = ascii_master.normalized_panel_text(fragment)
        standalone = ascii_master.normalized_panel_text(standalone_text)
        if not standalone:
            errors.append("Standalone ascii-master.txt has no valid panel content.")
        elif standalone != embedded:
            errors.append(
                "Standalone ASCII master does not exactly match embedded panel content."
            )
    return errors


def validate_refreshed_markdown(
    path: str | Path,
    *,
    topic_key: str | None = None,
    ascii_spec_path: str | Path | None = None,
) -> list[str]:
    source = Path(path)
    if not source.is_file():
        return [f"Markdown file does not exist: {source}"]
    return validate_refreshed_markdown_text(
        source.read_text(encoding="utf-8"),
        topic_key=topic_key,
        ascii_spec_path=ascii_spec_path,
    )


def extract_v2_workbook_markdown(markdown: str) -> str:
    """Extract Basic MCQs/remediation and PYQ/answer practice from assembled v2 Markdown."""
    errors = validate_v2_markdown_text(markdown)
    if errors:
        raise ValueError("; ".join(errors))

    _, body = split_frontmatter(markdown)
    lines = body.splitlines()
    headings = h2_headings(body)
    locations = {
        match_section(heading.text).key: heading.line_index
        for heading in headings
        if match_section(heading.text)
    }
    source_title = next(
        (line for line in lines if re.match(r"^#(?!#)\s+\S", line.strip())),
        "# Solved Practice Workbook",
    )
    title = source_title.strip()
    if re.search(r"\blearning session\b", title, re.I):
        title_text = re.sub(r"^#\s*", "", title)
        title_text = re.sub(
            r"\s+[—–-]\s+.*\bLearning Session\b.*$",
            "",
            title_text,
            flags=re.I,
        ).strip()
        if not title_text:
            title_text = re.sub(
                r"\bLearning Session\b",
                "",
                re.sub(r"^#\s*", "", title),
                flags=re.I,
            ).strip(" —-")
        title = f"# {title_text} — Solved Practice Workbook"
    practice = lines[locations["mcqs"] : locations["advanced"]]
    return title + "\n\n" + "\n".join(practice).strip() + "\n"


def validate_v2_paths(
    repository_root: str | Path,
    markdown_path: str | Path,
    output_path: str | Path,
    topic_key: str,
    mode: str,
) -> list[str]:
    root = Path(repository_root).resolve()
    source = Path(markdown_path).resolve()
    output = Path(output_path).resolve()
    errors: list[str] = []

    try:
        source_parts = source.relative_to(root).parts
    except ValueError:
        return [f"Markdown path is outside repository root: {source}"]

    if len(source_parts) < 6:
        errors.append(f"Markdown path is not a canonical v2 path: {source}")
        return errors
    expected_prefix = ("upsc-ai-kit", "knowledge")
    if tuple(part.casefold() for part in source_parts[:2]) != expected_prefix:
        errors.append("V2 Markdown must be under upsc-ai-kit\\knowledge\\<Subject>.")
        return errors

    subject = source_parts[2]
    source_tail = tuple(part.casefold() for part in source_parts[3:])
    refreshed_markdown = (
        len(source_parts) >= 8
        and source_parts[2].casefold() == REFRESHED_ROOT.casefold()
        and source_parts[5].casefold() == "learning-sessions"
        and source_parts[-2]
        and source.suffix.casefold() == ".md"
    )
    legacy_markdown_tail = (
        "learning-sessions",
        "v2",
        f"{topic_key}_learning-session.md".casefold(),
    )
    preferred_markdown = (
        len(source_tail) == 4
        and source_tail[:2] == ("learning-sessions", "v2")
        and source_tail[2]
        and source_tail[3] == f"{topic_key}_learning-session.md".casefold()
    )
    preferred_workbook_markdown = (
        mode == "workbook"
        and len(source_tail) == 4
        and source_tail[:2] == ("learning-sessions", "v2")
        and source_tail[2]
        and source_tail[3] == f"{topic_key}_solved-workbook.md".casefold()
    )
    notions_legacy_markdown = (
        topic_key.casefold()
        == "philosophy-paper-ii-philosophy-of-religion-01"
        and source_tail
        == (
            "philosophy-of-religion",
            "learning-sessions",
            "notions-of-god",
            "notions-of-god_uncompressed-complete-learning-session_2026-08-22.md",
        )
    )
    if (
        source_tail != legacy_markdown_tail
        and not preferred_markdown
        and not preferred_workbook_markdown
        and not notions_legacy_markdown
        and not refreshed_markdown
    ):
        errors.append(
            "V2 Markdown path must be "
            "upsc-ai-kit\\knowledge\\<Subject>\\learning-sessions\\v2\\"
            f"<section-key>\\{topic_key}_Learning-Session.md, or the matching "
            "_Solved-Workbook.md in workbook mode. Existing direct-v2 pilot "
            "paths remain accepted for compatibility."
        )

    try:
        output_parts = output.relative_to(root).parts
    except ValueError:
        errors.append(f"PDF path is outside repository root: {output}")
        return errors

    legacy_output_prefix = (
        "notes",
        subject,
        "learning-session-v2",
        topic_key,
    )
    output_folded = tuple(part.casefold() for part in output_parts)
    refreshed_output = (
        len(output_parts) >= 7
        and output_parts[0].casefold() == "notes"
        and output_parts[1].casefold() == REFRESHED_ROOT.casefold()
        and output_parts[4].casefold() == "learning-sessions"
        and output.suffix.casefold() == ".pdf"
    )
    expected_kind = "notes" if mode == "main" else "workbooks"
    preferred_output = (
        len(output_parts) == 6
        and output_folded[:3]
        == ("notes", subject.casefold(), "learning-session-v2")
        and bool(output_parts[3])
        and output_folded[4] == expected_kind
    )
    legacy_output = (
        len(output_parts) == 5
        and output_folded[:4]
        == tuple(part.casefold() for part in legacy_output_prefix)
    )
    notions_legacy_filename = (
        "notions-of-god_uncompressed-complete-learning-session_2026-08-22.pdf"
        if mode == "main"
        else "notions-of-god_solved-practice-workbook_2026-08-22.pdf"
    )
    notions_legacy_output = (
        topic_key.casefold()
        == "philosophy-paper-ii-philosophy-of-religion-01"
        and len(output_parts) == 6
        and output_folded[:5]
        == (
            "notes",
            "philosophy",
            "philosophy-of-religion",
            "learning-sessions",
            "notions-of-god",
        )
        and output.name.casefold() == notions_legacy_filename
    )
    if (
        not preferred_output
        and not legacy_output
        and not notions_legacy_output
        and not refreshed_output
    ):
        errors.append(
            "V2 PDFs must be under "
            f"notes\\{subject}\\learning-session-v2\\<section-key>\\"
            f"{expected_kind}\\. Existing topic-folder pilot paths remain accepted "
            "for compatibility."
        )

    suffix = "Learning-Session" if mode == "main" else "Solved-Workbook"
    name_pattern = re.compile(
        rf"^{re.escape(topic_key)}_{suffix}_(\d{{4}}-\d{{2}}-\d{{2}})\.pdf$",
        re.IGNORECASE,
    )
    match = name_pattern.fullmatch(output.name)
    notions_legacy_name = (
        topic_key.casefold()
        == "philosophy-paper-ii-philosophy-of-religion-01"
        and output.name.casefold() == notions_legacy_filename
    )
    refreshed_name = (
        refreshed_output
        and (
            (
                mode == "main"
                and re.fullmatch(
                    r".+_Complete-Learning-Session_\d{4}-\d{2}-\d{2}\.pdf",
                    output.name,
                    re.I,
                )
            )
            or (
                mode == "workbook"
                and re.fullmatch(
                    r".+_Solved-Practice-Workbook_\d{4}-\d{2}-\d{2}\.pdf",
                    output.name,
                    re.I,
                )
            )
        )
    )
    if not match and not notions_legacy_name and not refreshed_name:
        errors.append(
            f"V2 {mode} PDF filename must be "
            f"{topic_key}_{suffix}_<YYYY-MM-DD>.pdf."
        )
    elif match:
        try:
            date.fromisoformat(match.group(1))
        except ValueError:
            errors.append(f"PDF filename has an invalid ISO date: {match.group(1)}")
    return errors


def normalize_pdf_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"[^\w]+", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip()


def inspect_pdf_index(path: str | Path) -> PdfIndexInfo:
    """Read the visible early index and PDF outline using PyMuPDF."""
    try:
        import fitz
    except ImportError as exc:  # pragma: no cover - required in the v2 toolchain
        raise RuntimeError(
            "PyMuPDF is required for learner-v2 internal-index validation."
        ) from exc

    with fitz.open(Path(path)) as document:
        page_texts = tuple(page.get_text("text") for page in document)
        expected_index_markers = tuple(
            normalize_pdf_text(title) for title in PDF_INDEX_TITLES.values()
        )
        index_page = next(
            (
                number
                for number, text in enumerate(page_texts[:5], 1)
                if any(
                    marker in normalize_pdf_text(text)
                    for marker in expected_index_markers
                )
            ),
            None,
        )
        entries = tuple(
            PdfIndexEntry(int(level), str(title), int(page))
            for level, title, page in document.get_toc(simple=True)
        )
        first_content_page = min(
            (
                entry.page
                for entry in entries
                if 1 <= entry.page <= document.page_count
            ),
            default=(index_page or 1) + 1,
        )
        if index_page is None:
            index_text = ""
        else:
            end_page = max(index_page, first_content_page - 1)
            index_text = "\n".join(page_texts[index_page - 1 : end_page])
        return PdfIndexInfo(
            page_count=document.page_count,
            index_page=index_page,
            index_text=index_text,
            entries=entries,
            page_texts=page_texts,
        )


def matching_pdf_entry(
    entries: tuple[PdfIndexEntry, ...],
    title: str,
) -> PdfIndexEntry | None:
    expected = normalize_pdf_text(title)
    return next(
        (
            entry
            for entry in entries
            if normalize_pdf_text(entry.title) == expected
        ),
        None,
    )


def index_context_has_page_number(index_text: str, title: str, page: int) -> bool:
    lines = [line.strip() for line in index_text.splitlines() if line.strip()]
    expected = normalize_pdf_text(title)
    for position in range(len(lines)):
        title_lines: list[str] = []
        for end in range(position, min(len(lines), position + 4)):
            title_lines.append(lines[end])
            if expected not in normalize_pdf_text(" ".join(title_lines)):
                continue
            context = " ".join(
                lines[max(0, position - 1) : end + 1]
            )
            if re.search(rf"(?<!\d){page}(?!\d)", context):
                return True
            break
    return False


def validate_v2_pdf_index(path: str | Path, mode: str) -> list[str]:
    if mode not in PDF_INDEX_TITLES:
        return [f"Unknown learner-v2 PDF mode for index validation: {mode}"]
    try:
        info = inspect_pdf_index(path)
    except Exception as exc:
        return [f"Cannot inspect learner-v2 internal index: {exc}"]

    errors: list[str] = []
    expected_title = PDF_INDEX_TITLES[mode]
    if info.index_page is None:
        errors.append(f"Missing early internal page titled {expected_title}.")
        return errors
    if info.index_page > 5:
        errors.append(
            f"Internal index starts too late on page {info.index_page}; it must be near the beginning."
        )
    if normalize_pdf_text(expected_title) not in normalize_pdf_text(info.index_text):
        errors.append(f"Internal index title is not visible: {expected_title}.")

    normalized_index = normalize_pdf_text(info.index_text)
    for entry in info.entries:
        if not 1 <= entry.page <= info.page_count:
            errors.append(
                f"Indexed page {entry.page} for {entry.title!r} is outside "
                f"the PDF range 1-{info.page_count}."
            )
            continue
        normalized_title = normalize_pdf_text(entry.title)
        if normalized_title not in normalized_index:
            errors.append(f"Internal index does not visibly list: {entry.title}")
        destination = normalize_pdf_text(info.page_texts[entry.page - 1])
        if normalized_title not in destination:
            errors.append(
                f"Indexed page {entry.page} for {entry.title!r} does not contain "
                "that heading."
            )
        if not index_context_has_page_number(
            info.index_text,
            entry.title,
            entry.page,
        ):
            errors.append(
                f"Internal index does not show page number {entry.page} beside "
                f"{entry.title!r}."
            )

    required_entries: list[PdfIndexEntry] = []
    for title in PDF_REQUIRED_SECTIONS[mode]:
        if normalize_pdf_text(title) not in normalized_index:
            errors.append(f"Internal index does not visibly list required section: {title}")
        entry = matching_pdf_entry(info.entries, title)
        if entry is None:
            errors.append(
                f"Internal index/bookmark hierarchy is missing required section: {title}"
            )
            continue
        required_entries.append(entry)
        if not 1 <= entry.page <= info.page_count:
            continue

    if required_entries:
        levels = {entry.level for entry in required_entries}
        if len(levels) != 1:
            errors.append(
                "Required major sections do not share one consistent index hierarchy level."
            )
        pages = [entry.page for entry in required_entries]
        if pages != sorted(pages):
            errors.append("Required sections are not indexed in document order.")
    return errors


def validate_pdf(
    path: str | Path,
    *,
    variant: str = LEGACY_VARIANT,
    mode: str | None = None,
) -> list[str]:
    pdf_path = Path(path)
    if not pdf_path.is_file():
        return [f"PDF does not exist: {pdf_path}"]
    if pdf_path.stat().st_size < 1024:
        return [f"PDF is unexpectedly small: {pdf_path.stat().st_size} bytes"]

    with pdf_path.open("rb") as handle:
        header = handle.read(8)
        handle.seek(max(0, pdf_path.stat().st_size - 2048))
        trailer = handle.read()
    errors = []
    if not header.startswith(b"%PDF-"):
        errors.append("PDF header is missing.")
    if b"%%EOF" not in trailer:
        errors.append("PDF EOF marker is missing.")

    page_count: int | None = None
    try:
        from pypdf import PdfReader

        page_count = len(PdfReader(str(pdf_path)).pages)
    except ImportError:
        try:
            import fitz

            with fitz.open(pdf_path) as document:
                page_count = document.page_count
        except ImportError:
            page_count = None
        except Exception as exc:  # pragma: no cover - dependency-specific detail
            errors.append(f"PDF parser rejected the file: {exc}")
    except Exception as exc:  # pragma: no cover - dependency-specific detail
        errors.append(f"PDF parser rejected the file: {exc}")
    if page_count is not None and page_count < 1:
        errors.append("PDF contains no pages.")
    if variant == V2_VARIANT:
        if mode not in {"main", "workbook"}:
            errors.append("Learner-v2 PDF validation requires mode='main' or 'workbook'.")
        elif not errors:
            errors.extend(validate_v2_pdf_index(pdf_path, mode))
    return errors


def validate_pdf_layout(path: str | Path) -> tuple[list[str], dict[str, object]]:
    """Check renderability, blank/near-empty pages, clipping and replacement glyphs."""
    pdf_path = Path(path)
    metrics: dict[str, object] = {
        "page_count": 0,
        "blank_pages": [],
        "near_empty_pages": [],
        "clipped_text_pages": [],
        "replacement_glyph_pages": [],
    }
    if not pdf_path.is_file():
        return [f"PDF does not exist: {pdf_path}"], metrics
    try:
        import fitz
    except ImportError as exc:  # pragma: no cover
        return [f"PyMuPDF is required for layout validation: {exc}"], metrics

    errors: list[str] = []
    blank: list[int] = []
    near_empty: list[int] = []
    clipped: list[int] = []
    replacements: list[int] = []
    try:
        with fitz.open(pdf_path) as document:
            metrics["page_count"] = document.page_count
            for page_number, page in enumerate(document, 1):
                text = page.get_text("text")
                normalized = re.sub(r"\s+", "", text)
                images = page.get_images(full=True)
                drawings = page.get_drawings()
                if not normalized and not images and not drawings:
                    blank.append(page_number)
                elif len(normalized) < 24 and not images:
                    near_empty.append(page_number)
                if "\ufffd" in text or "�" in text:
                    replacements.append(page_number)
                rect = page.rect
                for block in page.get_text("blocks"):
                    x0, y0, x1, y1 = block[:4]
                    if (
                        x0 < rect.x0 - 1
                        or y0 < rect.y0 - 1
                        or x1 > rect.x1 + 1
                        or y1 > rect.y1 + 1
                    ):
                        clipped.append(page_number)
                        break
                # Rendering every page catches broken image streams and fonts.
                page.get_pixmap(matrix=fitz.Matrix(0.35, 0.35), alpha=False)
    except Exception as exc:
        errors.append(f"PDF render/layout inspection failed: {exc}")

    metrics.update(
        {
            "blank_pages": blank,
            "near_empty_pages": near_empty,
            "clipped_text_pages": clipped,
            "replacement_glyph_pages": replacements,
        }
    )
    if blank:
        errors.append(f"PDF has blank pages: {blank}.")
    if near_empty:
        errors.append(f"PDF has near-empty pages without images: {near_empty}.")
    if clipped:
        errors.append(f"PDF has text blocks outside page bounds: {clipped}.")
    if replacements:
        errors.append(f"PDF has replacement glyphs on pages: {replacements}.")
    return errors, metrics


def validate_tracker_record(
    tracker_path: str | Path,
    topic_key: str,
    variant: str,
    generation: int,
    *,
    repository_root: str | Path | None = None,
    check_paths: bool = True,
) -> list[str]:
    tracker = Path(tracker_path)
    if not tracker.is_file():
        return [f"Tracker does not exist: {tracker}"]
    data = json.loads(tracker.read_text(encoding="utf-8"))
    errors = []
    if data.get("schema_version") != 2:
        errors.append("Tracker schema_version must be 2.")

    records = [
        entry
        for entry in data.get("exports", [])
        if isinstance(entry, dict)
        and entry.get("topic_key") == topic_key
        and entry.get("variant") == variant
        and entry.get("generation") == generation
    ]
    if len(records) != 1:
        errors.append(
            "Expected exactly one tracker record for "
            f"{topic_key}/{variant}/g{generation}; found {len(records)}."
        )
        return errors
    record = records[0]

    for field in ("record_id", "topic_key", "variant", "generation", "supersedes"):
        if field not in record:
            errors.append(f"Tracker record is missing {field}.")
    expected_record_id = f"{topic_key}:{variant}:g{generation}"
    if record.get("record_id") != expected_record_id:
        errors.append(f"Tracker record_id must be {expected_record_id}.")

    approval = record.get("approval")
    if not isinstance(approval, dict) or "approved" not in approval:
        errors.append("Tracker record must contain approval.approved.")
    elif bool(record.get("approved")) != bool(approval.get("approved")):
        errors.append("Backward-compatible approved value disagrees with approval.approved.")

    provenance = record.get("provenance")
    required_provenance = {
        "source_basic",
        "source_advanced",
        "assembled_markdown",
        "renderer",
        "generation_date",
        "superseded_v1",
    }
    if not isinstance(provenance, dict):
        errors.append("Tracker record must contain a provenance object.")
    else:
        missing = sorted(required_provenance - provenance.keys())
        if missing:
            errors.append("Provenance is missing: " + ", ".join(missing))
        renderer = provenance.get("renderer")
        if not isinstance(renderer, dict) or not renderer.get("name") or not renderer.get("version"):
            errors.append("Provenance renderer must contain name and version.")
        if provenance.get("assembled_markdown") != record.get("markdown"):
            errors.append("Provenance assembled_markdown must equal the record markdown path.")
        try:
            date.fromisoformat(str(provenance.get("generation_date")))
        except ValueError:
            errors.append("Provenance generation_date must be an ISO date.")

        if variant == V2_VARIANT:
            if not provenance.get("source_basic"):
                errors.append("V2 provenance must identify the Basic owner.")
            if not provenance.get("assembled_markdown"):
                errors.append("V2 provenance must identify the assembled Markdown.")
            legacy_exists = any(
                isinstance(entry, dict)
                and (
                    entry.get("topic_key") == topic_key
                    or entry.get("record_id") == record.get("supersedes")
                )
                and entry.get("variant") == LEGACY_VARIANT
                for entry in data.get("exports", [])
            )
            if legacy_exists and not provenance.get("superseded_v1"):
                errors.append("V2 provenance must identify the superseded legacy-v1 record.")

    if generation > 1 and not record.get("supersedes"):
        errors.append("Generation > 1 must identify the record it supersedes.")

    if check_paths:
        root = (
            Path(repository_root).resolve()
            if repository_root
            else tracker.resolve().parent
        )
        for field in ("main_pdf", "workbook", "markdown"):
            relative = record.get(field)
            if not relative or not (root / str(relative)).exists():
                errors.append(f"Tracker {field} path does not exist: {relative}")
        if variant == V2_VARIANT and isinstance(provenance, dict):
            for field in ("source_basic", "source_advanced"):
                relative = provenance.get(field)
                if relative and not (root / str(relative)).exists():
                    errors.append(f"Provenance {field} path does not exist: {relative}")
            legacy_package = provenance.get("legacy_v1_source_package")
            if legacy_package and not (root / str(legacy_package)).is_file():
                errors.append(
                    "Provenance legacy_v1_source_package path does not exist: "
                    f"{legacy_package}"
                )
            legacy_assets = provenance.get("reused_legacy_asset_folder")
            if legacy_assets and not (root / str(legacy_assets)).is_dir():
                errors.append(
                    "Provenance reused_legacy_asset_folder path does not exist: "
                    f"{legacy_assets}"
                )
            if all(record.get(field) for field in ("main_pdf", "workbook", "markdown")):
                errors.extend(
                    validate_v2_paths(
                        root,
                        root / str(record["markdown"]),
                        root / str(record["main_pdf"]),
                        topic_key,
                        "main",
                    )
                )
                errors.extend(
                    validate_v2_paths(
                        root,
                        root / str(record["markdown"]),
                        root / str(record["workbook"]),
                        topic_key,
                        "workbook",
                    )
                )
            asset_folder = record.get("asset_folder")
            if asset_folder:
                main_parts = Path(str(record["main_pdf"])).parts
                if len(main_parts) < 2:
                    errors.append("Cannot derive the v2 subject from main_pdf.")
                else:
                    legacy_assets = (
                        root
                        / "notes"
                        / main_parts[1]
                        / "learning-session-v2"
                        / topic_key
                        / "assets"
                    )
                    preferred_assets = None
                    if len(main_parts) >= 6 and main_parts[4].casefold() == "notes":
                        preferred_assets = (
                            root
                            / "notes"
                            / main_parts[1]
                            / "learning-session-v2"
                            / main_parts[3]
                            / "assets"
                            / topic_key
                        )
                    actual_assets = (root / str(asset_folder)).resolve()
                    accepted_assets = {legacy_assets.resolve()}
                    if (
                        len(main_parts) >= 7
                        and main_parts[0].casefold() == "notes"
                        and main_parts[1].casefold() == REFRESHED_ROOT.casefold()
                        and main_parts[4].casefold() == "learning-sessions"
                    ):
                        refreshed_assets = (
                            root
                            / "upsc-ai-kit"
                            / "knowledge"
                            / REFRESHED_ROOT
                            / main_parts[2]
                            / main_parts[3]
                            / "learning-sessions"
                            / main_parts[5]
                            / "assets"
                        )
                        accepted_assets.add(refreshed_assets.resolve())
                        if (
                            len(main_parts) >= 8
                            and main_parts[6].casefold()
                            == f"g{generation}".casefold()
                        ):
                            accepted_assets.add(
                                (
                                    refreshed_assets.parent
                                    / main_parts[6]
                                    / "assets"
                                ).resolve()
                            )
                    if preferred_assets:
                        accepted_assets.add(preferred_assets.resolve())
                        accepted_assets.add(
                            (
                                preferred_assets.parent
                                / f"{topic_key}-g{generation}"
                            ).resolve()
                        )
                    if actual_assets not in accepted_assets:
                        expected = preferred_assets or legacy_assets
                        errors.append(
                            f"V2 asset_folder must be {expected.relative_to(root)}."
                        )
                    if not actual_assets.is_dir():
                        errors.append(
                            f"Tracker asset_folder does not exist: {asset_folder}"
                        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--repository-root", type=Path)
    parser.add_argument("--topic-key")
    parser.add_argument(
        "--ascii-spec",
        type=Path,
        help=(
            "Explicit generation-specific manual ASCII spec. Defaults to "
            "topic-key discovery for existing first-generation workflows."
        ),
    )
    parser.add_argument("--main-pdf", type=Path)
    parser.add_argument("--workbook", type=Path)
    parser.add_argument("--tracker", type=Path)
    parser.add_argument("--variant", default=V2_VARIANT)
    parser.add_argument("--generation", type=int, default=1)
    parser.add_argument("--skip-tracker-paths", action="store_true")
    parser.add_argument(
        "--refreshed-contract",
        action="store_true",
        help="Also enforce named sessions, final ASCII master, and non-patterned keys.",
    )
    args = parser.parse_args()

    root = args.repository_root or Path(__file__).resolve().parents[1]
    errors = (
        validate_refreshed_markdown(
            args.markdown,
            topic_key=args.topic_key,
            ascii_spec_path=args.ascii_spec,
        )
        if args.refreshed_contract
        else validate_v2_markdown(args.markdown)
    )
    if args.main_pdf:
        if not args.topic_key:
            errors.append("--topic-key is required with --main-pdf.")
        else:
            errors.extend(
                validate_v2_paths(root, args.markdown, args.main_pdf, args.topic_key, "main")
            )
        errors.extend(
            validate_pdf(args.main_pdf, variant=args.variant, mode="main")
        )
        if args.refreshed_contract:
            errors.extend(validate_pdf_layout(args.main_pdf)[0])
    if args.workbook:
        if not args.topic_key:
            errors.append("--topic-key is required with --workbook.")
        else:
            errors.extend(
                validate_v2_paths(
                    root, args.markdown, args.workbook, args.topic_key, "workbook"
                )
            )
        errors.extend(
            validate_pdf(args.workbook, variant=args.variant, mode="workbook")
        )
        if args.refreshed_contract:
            errors.extend(validate_pdf_layout(args.workbook)[0])
    if args.tracker:
        if not args.topic_key:
            errors.append("--topic-key is required with --tracker.")
        else:
            errors.extend(
                validate_tracker_record(
                    args.tracker,
                    args.topic_key,
                    args.variant,
                    args.generation,
                    repository_root=root,
                    check_paths=not args.skip_tracker_paths,
                )
            )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("V2 export validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
