#!/usr/bin/env python3
"""Build four deterministic, reusable full UPSC simulation sets and validate them.

The script reads tracked final workbooks for static Prelims questions, creates
checked CSAT variants, builds Mains/Essay/Philosophy papers, renders PDFs, and
writes regeneration sources plus a machine-readable validation report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import unicodedata
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

import fitz
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from qualifying_language_simulations import build_language_papers


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "upsc-ai-kit" / "practice" / "Full-Simulation-Sets"
DESCRIPTIVE_BANK_PATH = SOURCE_ROOT / "curated-descriptive-bank.json"
DESCRIPTIVE_REVIEW_PATH = SOURCE_ROOT / "descriptive-sample-review.json"
PAPER_ROOT = ROOT / "exams" / "papers"
KEY_ROOT = ROOT / "exams" / "answer-keys"
FINAL_LIBRARY = ROOT / "learning_package_final"
CUTOFF = "2026-09-10"
SETS = range(1, 5)
LETTERS = "ABCD"
WORD_RE = re.compile(r"\b[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*\b")
DIFFICULTY_STANDARD = {
    "overall": "Above typical recent UPSC difficulty, while fair, syllabus-relevant and unambiguous.",
    "prelims": (
        "Multi-statement elimination, close conceptual distinctions, cross-subject integration, "
        "map/institution/application reasoning and balanced plausible distractors; no niche fact dumping."
    ),
    "csat": (
        "Moderately harder than the recent qualifying level through dense passages, time pressure "
        "and multi-step reasoning; every item remains uniquely solvable without gratuitous calculation."
    ),
    "mains": (
        "Synthesis, critique, competing viewpoints, constitutional/institutional or evidence-based "
        "analysis, qualification and current-static integration."
    ),
    "philosophy": (
        "Textual and doctrinal precision, argument reconstruction, objections and strongest replies, "
        "and comparisons across thinkers or schools."
    ),
    "qualifying_language": (
        "Matriculation-level language skills tested through demanding but fair comprehension, "
        "precis, composition, translation and usage tasks."
    ),
}
FORBIDDEN_DEFECTIVE_STEMS = (
    "The statement 'Akbar copied every Sur institution unchanged' is",
    "The statement 'one-third proves identical practice everywhere' is",
    "Which statement best expresses the Faruqi Khandesh location in strategy?",
    "Which statement best expresses Jahangir's farzand language?",
)


def plain(value: Any) -> str:
    text = str(value)
    replacements = {
        "\u2013": "-", "\u2014": "-", "\u2212": "-", "\u2192": "->",
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\u2026": "...", "\u00a0": " ", "\u2264": "<=", "\u2265": ">=",
        "\u00d7": "x", "\u00f7": "/", "\u20b9": "Rs ", "\u2194": "<->",
        "\u2713": "", "\u2705": "", "\u26a0": "", "\ufe0f": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"\s+", " ", text).strip()
    return text


def markdown_plain(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("__", "").replace("`", "").replace("*", "")
    text = re.sub(r"^\s*[>#|]+\s?", "", text, flags=re.M)
    text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.M)
    return plain(text)


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def stable_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_stem(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", plain(text).lower()).strip()


def prelims_difficulty_score(question: dict[str, Any]) -> int:
    stem = question["stem"].lower()
    score = 0
    if words(stem) >= 28:
        score += 1
    if re.search(r"\bconsider\b|\bstatements?\b|\bpairs?\b|\bmatching\b", stem):
        score += 2
    if re.search(r"\bhow many\b|\bwhich of the above\b|\bcorrectly matched\b", stem):
        score += 1
    if re.search(r"\bnot\b|\bincorrect\b|\bmost appropriate\b|\bbest explains\b", stem):
        score += 1
    if len(question.get("explanation", "")) >= 140:
        score += 1
    option_lengths = [max(1, words(option)) for option in question["options"]]
    if max(option_lengths) / min(option_lengths) <= 3.0:
        score += 1
    if any(term in stem for term in (
        "institution", "article", "mechanism", "chronology", "application",
        "inference", "implication", "with reference",
    )):
        score += 1
    return score


def rotate_options(
    options: list[str],
    correct_index: int,
    target_index: int,
    reasons: list[str] | None = None,
) -> tuple[list[str], int, list[str]]:
    indexed = list(enumerate(options))
    correct = indexed.pop(correct_index)
    indexed.insert(target_index, correct)
    new_options = [plain(item[1]) for item in indexed]
    old_reasons = reasons or [""] * 4
    new_reasons = [plain(old_reasons[item[0]]) for item in indexed]
    return new_options, target_index, new_reasons


def fit_sentences(sentences: Iterable[str], minimum: int, maximum: int) -> str:
    chosen: list[str] = []
    for sentence in sentences:
        candidate = " ".join(chosen + [plain(sentence)])
        if words(candidate) <= maximum:
            chosen.append(plain(sentence))
        if words(" ".join(chosen)) >= minimum:
            break
    if words(" ".join(chosen)) < minimum:
        fillers = [
            "The decisive test is whether the proposed institution changes incentives, protects constitutional values and remains administratively workable.",
            "A balanced judgement therefore joins measurable outcomes with legality, inclusion, accountability and the capacity to correct unintended effects.",
            "Implementation should use transparent indicators, independent review and participation by the people most affected by the policy.",
        ]
        for sentence in fillers:
            candidate = " ".join(chosen + [sentence])
            if words(candidate) <= maximum:
                chosen.append(sentence)
            if words(" ".join(chosen)) >= minimum:
                break
    return " ".join(chosen)


# ---------------------------------------------------------------------------
# Static Prelims extraction

QUESTION_HEAD_RE = re.compile(
    r"(?m)^(?:#{3,5}\s+)(?:MCQ\s+|Q)(\d+)(?:[.)]|\s|$)(.*)$"
)
ANSWER_RE = re.compile(
    r"(?im)^\s*(?:>\s*)?(?:[-*]\s*)?(?:[A-Z ]*?)\*{0,2}"
    r"(?:Correct\s+answer|Answer)\s*:\s*\(?([A-Da-d])\)?"
)
OPTION_RE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\(([A-Da-d])\)|([A-Da-d])[.)-])\s+(.+?)\s*$"
)


def option_explanations(block: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for match in re.finditer(
        r"(?ims)^\s*(?:[-*]\s*)?\*{0,2}([A-D])\*{0,2}\s*[:.-]\s*(.+?)"
        r"(?=^\s*(?:[-*]\s*)?\*{0,2}[A-D]\*{0,2}\s*[:.-]|"
        r"^\s*(?:>\s*)?(?:Examiner|UPSC)\s+trap|"
        r"^\s*(?:>\s*)?\*{0,2}(?:Examiner|UPSC)\s+trap|\Z)",
        block,
    ):
        found[match.group(1)] = markdown_plain(match.group(2))
    return found


STALE_OPTION_LABEL_RE = re.compile(
    r"(?im)(?:^|\s)(?:option|answer)\s*[A-D]\b|^\s*[A-D]\s*[.):]\s+|"
    r"\([A-D]\)|(?:^|\s)[A-D]\s+is\s+(?:correct|incorrect|unsupported)\b"
)


def has_stale_option_labels(text: str) -> bool:
    return bool(STALE_OPTION_LABEL_RE.search(text))


def art_option_reason(option: str, explanation: str, correct: bool) -> str:
    sentences = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", explanation)
        if sentence.strip()
    ]
    tokens = [
        token.lower() for token in WORD_RE.findall(option)
        if len(token) >= 5 and token.lower() not in {
            "statement", "correctly", "securely", "identified", "absence",
            "details", "exact", "every", "which", "about",
        }
    ]
    matched = next(
        (
            sentence for sentence in sentences
            if any(token in sentence.lower() for token in tokens)
        ),
        explanation,
    )
    matched = re.sub(
        r"(?i)^\s*(?:option\s+)?[A-D]\s+is\s+(?:the\s+)?"
        r"(?:correct|incorrect|unsupported(?:\s+statement)?)"
        r"(?:\s+because|\s+since|\s*[:.-])?\s*",
        "",
        matched,
    )
    matched = re.sub(r"(?i)\bsource-owned\b", "documented", matched)
    if re.search(r"(?:^|\s)[A-D](?:\s|[.):,-])", matched):
        matched = (
            "The source supports this exact identification."
            if correct
            else "The source does not support this identification."
        )
    prefix = "Correct" if correct else "Incorrect"
    return plain(f"{prefix}: {matched} The option tested was '{option}'.")


def parse_mcqs(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    basic = re.search(r"(?m)^## BASIC MCQS / REMEDIATION(?: PRACTICE)?\s*$", text)
    if not basic:
        return []
    section = text[basic.end():]
    next_h2 = re.search(r"(?m)^## ", section)
    if next_h2:
        section = section[:next_h2.start()]
    heads = list(QUESTION_HEAD_RE.finditer(section))
    output: list[dict[str, Any]] = []
    for index, head in enumerate(heads):
        end = heads[index + 1].start() if index + 1 < len(heads) else len(section)
        block = section[head.end():end]
        answer_match = ANSWER_RE.search(block)
        if not answer_match:
            continue
        pre_answer = block[:answer_match.start()]
        lines = pre_answer.splitlines()
        options: list[str] = []
        option_letters: list[str] = []
        first_option: int | None = None
        for line_no, line in enumerate(lines):
            match = OPTION_RE.match(line)
            if match:
                if first_option is None:
                    first_option = line_no
                option_letters.append((match.group(1) or match.group(2)).upper())
                options.append(markdown_plain(match.group(3)))
        if len(options) != 4 or option_letters != list(LETTERS):
            continue
        title = markdown_plain(head.group(2).lstrip(".:- "))
        stem_body = "\n".join(lines[: first_option or 0])
        stem = markdown_plain((title + " " + stem_body).strip())
        stem = re.sub(
            r"^(?:\d+\s+|Part XIV ownership\s+)"
            r"(?=(?:Which|What|How|Consider)\b)",
            "",
            stem,
            flags=re.I,
        )
        if len(stem) < 25 or len(stem) > 1000:
            continue
        if any(bad in stem.lower() for bad in (
            "practice variant", "correctly identifies", "tracker-record boundary",
            "preserves the ecological boundary", "question-shaped",
        )):
            continue
        answer = answer_match.group(1).upper()
        correct_index = LETTERS.index(answer)
        post = block[answer_match.end():]
        next_label = re.search(
            r"(?im)^\s*(?:>\s*)?\*{0,2}(?:Explanation|Option-specific explanations|Option explanations)\*{0,2}\s*:",
            post,
        )
        explanation = markdown_plain(post[next_label.end():] if next_label else post)
        trap_match = re.search(
            r"(?ims)(?:Examiner|UPSC)\s+trap[^:]*:\s*(.+?)(?=\n\s*\n|\Z)", block
        )
        trap = markdown_plain(trap_match.group(1)) if trap_match else (
            "Reject attractive options that change the institution, chronology, scale or legal status tested by the stem."
        )
        explicit = option_explanations(post)
        subject = path.relative_to(FINAL_LIBRARY).parts[0]
        if set(explicit) == set(LETTERS):
            reasons = [explicit[letter] for letter in LETTERS]
            if any(
                (
                    index == correct_index
                    and not re.match(r"^\s*Correct\b", reason, re.I)
                ) or (
                    index != correct_index
                    and not re.match(r"^\s*Incorrect\b", reason, re.I)
                )
                for index, reason in enumerate(reasons)
            ):
                continue
            source_validation = "four-explicit-reasons-agree-with-key"
        elif subject == "Indian-Art-and-Culture" and len(explanation) >= 45:
            reasons = [
                art_option_reason(option, explanation, option_index == correct_index)
                for option_index, option in enumerate(options)
            ]
            source_validation = "art-and-culture-general-explanation-key-accepted"
        else:
            continue
        if len(explanation) < 45:
            continue
        correct_reason = re.sub(
            r"^(?:This is correct\.\s*|Correct\s*:\s*)",
            "",
            reasons[correct_index],
            flags=re.I,
        ).strip()
        if len(correct_reason) >= 20:
            explanation = correct_reason
        if has_stale_option_labels(explanation):
            continue
        relative = path.relative_to(ROOT).as_posix()
        output.append({
            "stem": stem,
            "options": options,
            "correct_index": correct_index,
            "reasons": reasons,
            "explanation": explanation[:1000],
            "trap": trap[:500],
            "source": relative,
            "subject": subject,
            "current": False,
            "source_validation": source_validation,
        })
        output[-1]["difficulty_score"] = prelims_difficulty_score(output[-1])
    return output


STATIC_PLAN = {
    "Polity": (["Polity"], 12),
    "Economy": (["Economy"], 12),
    "Ancient History": (["Ancient-History"], 4),
    "Medieval History": (["Medieval-History"], 4),
    "Modern History": (["Modern-History"], 6),
    "Art and Culture": (["Indian-Art-and-Culture"], 6),
    "Geography": (["Geography"], 12),
    "Environment": (["Environment-and-Ecology"], 12),
    "Science and Technology": (["Science-and-Technology"], 10),
    "Governance and Security": (
        [
            "Governance", "Indian-Society", "Social-Justice",
            "International-Relations", "Internal-Security", "Disaster-Management",
        ],
        12,
    ),
}


CURATED_KNOWLEDGE_PLAN = {
    "Medieval History": ["Medieval-Indian-History"],
    "Modern History": ["Modern-Indian-History"],
    "Geography": ["Geography"],
    "Environment": ["Environment-and-Ecology"],
    "Science and Technology": ["Science-and-Technology"],
    "Governance and Security": [
        "Governance", "Indian-Society", "Social-Justice",
        "International-Relations", "Internal-Security", "Disaster-Management",
    ],
}


def source_safe_extract(text: str) -> bool:
    lowered = text.lower()
    return (
        18 <= len(text) <= 420
        and not text.rstrip().endswith("?")
        and not re.search(r"\b(?:of|and|the|a|to)\.?\s*$", text, re.I)
        and not re.search(r"(?:[-/]\.?|\b(?:is|are)\s+the\s+(?:oldest|latest)\.?)\s*$", text, re.I)
        and not re.match(
            r"^(?:compare|analyse|analyze|examine|explain|discuss|evaluate|assess|critically|why|use|link)\b",
            lowered,
        )
        and not re.search(r"\b\d+\.\d+[A-Z]?\b", text)
        and "http://" not in lowered
        and "https://" not in lowered
        and "|" not in text
        and not re.search(r"\b20(?:24|25|26)\b", text)
        and not any(token in lowered for token in (
            "as of ", "latest ", "current anchor", "verify live", "provisional",
            "scheduled", "targeted", "under construction", "study link",
            "likely statement trap", "questions owned by", ".md", "source discipline",
            "topic 0", "topic 1", "topic 2", "topic 3",
            "mains (", "prelims:", "answer framework",
            "named evidence:", "significance:", "limitation:", "answer thesis:",
            "escalate to", "verified news item", "current linkage",
            "foundation -", "foundation:",
            "local pyq", "pdf p.", "single fact answers", "objective demand",
            "answer-writing", "routing",
            "this topic covers", "owned core:",
            ".pdf", "pdf pp", "why it matters for an answer",
            "cite them", "book's own", "mark-scaled", "exam-length",
            "ca anchor",
        ))
    )


def source_safe_prompt(text: str) -> bool:
    lowered = text.lower()
    return (
        7 <= words(text) <= 65
        and not any(token in lowered for token in (
            "topic 0", "topic 1", "topic 2", "topic 3", "study link",
            "answer framework", "why and how reconstruction works",
            "demand decoding", "mains angle",
        ))
        and not lowered.rstrip().endswith(("to", "of", "and", "the", "with"))
    )


def knowledge_bullets(text: str, marker: str) -> list[str]:
    pattern = re.compile(
        rf"(?ms)^\s*(?:>\s*)?-\s*{re.escape(marker)}\s*(.+?)"
        rf"(?=^\s*(?:>\s*)?-\s*[✅❌⚠📰]|^##\s|\Z)"
    )
    output = []
    for match in pattern.finditer(text):
        value = markdown_plain(match.group(1))
        if source_safe_extract(value):
            output.append(value)
    return output


def knowledge_traps(text: str) -> list[tuple[str, str]]:
    traps: list[tuple[str, str]] = []
    for raw in knowledge_bullets(text, "❌"):
        parts = re.split(r"\s*(?:->|→)\s*", raw, maxsplit=1)
        if len(parts) != 2:
            continue
        wrong, correction = map(plain, parts)
        if source_safe_extract(wrong) and source_safe_extract(correction):
            traps.append((wrong.rstrip(".") + ".", correction.rstrip(".") + "."))
    return traps


def preferred_knowledge_text(text: str) -> str:
    headings = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    selected: list[str] = []
    for index, heading in enumerate(headings):
        if not re.search(
            r"Essential definitions|Must.Know Facts|Key classification|Snapshot.*core idea",
            heading.group(1),
            re.I,
        ):
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        selected.append(text[heading.end():end])
    return "\n".join(selected) if selected else text


def curated_question(
    category: str,
    path: Path,
    title: str,
    fact_one: str,
    fact_two: str,
    wrong: str,
    correction: str,
    variant: int,
) -> dict[str, Any]:
    if variant % 2 == 0:
        statements = [fact_one, fact_two, wrong]
        options = ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"]
        reasons = [
            (
                f"Correct: statements 1 and 2 reproduce source-grounded facts about {title}; "
                f"statement 3 is the source's explicit trap, corrected as follows: {correction}"
            ),
            (
                f"Incorrect: this combination accepts statement 3, but the cited source explicitly rejects "
                f"'{wrong}' and replaces it with '{correction}'"
            ),
            (
                f"Incorrect: statement 1 is also source-grounded, while statement 3 is the rejected trap: "
                f"{wrong}"
            ),
            (
                f"Incorrect: all three cannot be correct because statement 3 contradicts the source correction: "
                f"{correction}"
            ),
        ]
        explanation = (
            f"Statements 1 and 2 are correct. Statement 3 is false: {correction}"
        )
    else:
        statements = [correction, fact_one, wrong]
        options = ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"]
        reasons = [
            (
                f"Correct: statement 1 is the source's correction and statement 2 is an independent "
                f"source-grounded fact; statement 3 restates the rejected misconception."
            ),
            (
                f"Incorrect: statement 3 is explicitly rejected by the source; its correction is '{correction}'"
            ),
            (
                f"Incorrect: statement 2 is also correct, whereas statement 3 remains the source's rejected trap."
            ),
            (
                f"Incorrect: the inclusion of statement 3 makes the all-statements option fail; "
                f"the valid boundary is '{correction}'"
            ),
        ]
        explanation = (
            f"The source explicitly corrects the misconception '{wrong}' with '{correction}'. "
            f"It separately supports statement 2: {fact_one}"
        )
    stem = (
        f"With reference to {title}, consider the following statements: "
        f"1. {statements[0]} 2. {statements[1]} 3. {statements[2]} "
        "Which of the statements given above are correct?"
    )
    question = {
        "stem": plain(stem),
        "options": options,
        "correct_index": 0,
        "reasons": list(map(plain, reasons)),
        "explanation": plain(explanation),
        "trap": plain(
            f"The difficult distractor preserves topic vocabulary but crosses the exact boundary "
            f"recorded by the source: {wrong} -> {correction}"
        ),
        "source": path.relative_to(ROOT).as_posix(),
        "source_extracts": [fact_one, fact_two, wrong.rstrip("."), correction.rstrip(".")],
        "subject": category,
        "current": False,
        "origin": "curated-knowledge-bank",
        "source_validation": "exact-extracts-from-basic-knowledge-owner",
    }
    question["difficulty_score"] = max(6, prelims_difficulty_score(question))
    return question


def build_curated_knowledge_pool() -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for category, subjects in CURATED_KNOWLEDGE_PLAN.items():
        by_round: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for subject in subjects:
            base = ROOT / "upsc-ai-kit" / "knowledge" / subject / "basic"
            for path in sorted(base.glob("*.md")):
                text = path.read_text(encoding="utf-8", errors="ignore")
                title_match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
                if not title_match:
                    continue
                title = re.sub(
                    r"\s*[-—]\s*MUST-DO.*$", "", markdown_plain(title_match.group(1)),
                    flags=re.I,
                )
                facts = knowledge_bullets(preferred_knowledge_text(text), "✅")
                traps = sorted(
                    knowledge_traps(text),
                    key=lambda pair: (
                        min(words(pair[0]), words(pair[1])),
                        words(pair[0]) + words(pair[1]),
                    ),
                    reverse=True,
                )
                if len(facts) < 2 or not traps:
                    continue
                for index, (wrong, correction) in enumerate(traps):
                    fact_one = facts[(2 * index) % len(facts)]
                    fact_two = facts[(2 * index + 1) % len(facts)]
                    if normalize_stem(fact_one) == normalize_stem(fact_two):
                        continue
                    question = curated_question(
                        category, path, title, fact_one, fact_two,
                        wrong, correction, index,
                    )
                    by_round[index].append(question)
        ordered: list[dict[str, Any]] = []
        for round_no in sorted(by_round):
            ordered.extend(sorted(
                by_round[round_no],
                key=lambda item: (item["source"], normalize_stem(item["stem"])),
            ))
        unique: dict[str, dict[str, Any]] = {}
        for question in ordered:
            unique.setdefault(normalize_stem(question["stem"]), question)
        grouped[category] = list(unique.values())
    return grouped


def build_static_pool() -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    excluded = (
        "Ancient-History/Subject-wide-Syllabus/18-The-Sangam-Age",
        "Ethics/Subject-wide-Syllabus/02-Human-Values",
    )
    paths = sorted(FINAL_LIBRARY.rglob("Solved-Practice-Workbook.md"))
    for path in paths:
        relative = path.relative_to(FINAL_LIBRARY).as_posix()
        if any(token in relative for token in excluded):
            continue
        subject = relative.split("/", 1)[0]
        for label, (subjects, _) in STATIC_PLAN.items():
            if subject in subjects:
                grouped[label].extend(parse_mcqs(path))
                break
    for label, questions in grouped.items():
        unique: dict[str, dict[str, Any]] = {}
        for question in questions:
            unique.setdefault(normalize_stem(question["stem"]), question)
        values = list(unique.values())
        values = [
            question for question in values
            if question["difficulty_score"] >= 4
            and max(max(1, words(option)) for option in question["options"])
            / min(max(1, words(option)) for option in question["options"]) <= 3.0
        ]
        random.Random(f"full-simulation-{label}").shuffle(values)
        values.sort(key=lambda question: question["difficulty_score"], reverse=True)
        grouped[label] = values
    curated = build_curated_knowledge_pool()
    for label, questions in curated.items():
        grouped[label] = questions
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    (SOURCE_ROOT / "curated-prelims-bank.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "rule": (
                    "Original multi-statement MCQs generated only from exact facts and explicit "
                    "misconception-correction pairs in the cited knowledge files."
                ),
                "categories": curated,
            },
            ensure_ascii=True,
            indent=2,
        ),
        encoding="utf-8",
    )
    return grouped


CURRENT_EVENTS = [
    {
        "name": "Union Budget 2026-27",
        "date": "1 February 2026",
        "fact": "The Union Budget 2026-27 followed the Economic Survey on 1 February 2026.",
        "institution": "Ministry of Finance and Parliament",
        "static": "The Annual Financial Statement is constitutionally linked to Article 112.",
        "source": "learning_package_final/Economy/Subject-wide-Syllabus/26-Economic-Survey-Synthesis-and-Current-Macro-Dashboard/Learning-Session.md (validated, cutoff 9 September 2026)",
    },
    {
        "name": "Economic Survey 2025-26",
        "date": "29 January 2026",
        "fact": "The Economic Survey 2025-26 was tabled in Parliament on 29 January 2026.",
        "institution": "Department of Economic Affairs, Ministry of Finance",
        "static": "The Survey is a policy and analytical document, not a constitutional money bill.",
        "source": "learning_package_final/Economy/Subject-wide-Syllabus/26-Economic-Survey-Synthesis-and-Current-Macro-Dashboard/Learning-Session.md (validated, cutoff 9 September 2026)",
    },
    {
        "name": "Economic Survey growth assessment",
        "date": "29 January 2026",
        "fact": "The Economic Survey placed FY 2025-26 real GDP growth at 7.4% FAE and projected FY 2026-27 growth at 6.8-7.2%.",
        "institution": "Department of Economic Affairs, Ministry of Finance",
        "static": "A Survey projection is a dated analytical estimate, not a guaranteed outturn.",
        "source": "learning_package_final/Economy/Subject-wide-Syllabus/26-Economic-Survey-Synthesis-and-Current-Macro-Dashboard/Learning-Session.md (validated, January 2026 vintage)",
    },
    {
        "name": "RBI macro-risk assessment",
        "date": "5 August 2026",
        "fact": "RBI's 5 August 2026 statement flagged volatile oil, sticky global inflation, elevated yields, US-dollar strength and uneven monsoon risk.",
        "institution": "Reserve Bank of India",
        "static": "External shocks affect inflation, growth, fiscal costs and the balance of payments through different transmission channels.",
        "source": "learning_package_final/Economy/Subject-wide-Syllabus/26-Economic-Survey-Synthesis-and-Current-Macro-Dashboard/Learning-Session.md (validated, 5 August 2026)",
    },
    {
        "name": "India's 100th Ramsar site milestone",
        "date": "5 June 2026",
        "fact": "India reached 100 Ramsar sites on 5 June 2026, with Surha Tal in Ballia district recorded as the 100th site.",
        "institution": "MoEFCC and the Ramsar Convention framework",
        "static": "Ramsar designation recognises a Wetland of International Importance but does not by itself prove management effectiveness.",
        "source": "learning_package_final/Environment-and-Ecology/Subject-wide-Syllabus/28-Species-and-Current-Affairs-Tracker/Learning-Session.md (validated, 5 June 2026)",
    },
    {
        "name": "Non-fossil installed-capacity milestone",
        "date": "31 December 2025",
        "fact": "Non-fossil sources accounted for 51.93% of India's installed power capacity at end-December 2025.",
        "institution": "Ministry of Power data cited by Economic Survey 2025-26",
        "static": "Installed capacity share is not the same as electricity-generation share or energy-consumption share.",
        "source": "learning_package_final/Environment-and-Ecology/Subject-wide-Syllabus/28-Species-and-Current-Affairs-Tracker/Learning-Session.md (validated 2 August 2026)",
    },
    {
        "name": "Renewable-capacity addition",
        "date": "31 December 2025",
        "fact": "India added 38.61 GW of renewable capacity in 2025-26 up to 31 December 2025, according to the Economic Survey evidence card.",
        "institution": "MNRE data cited by Economic Survey 2025-26",
        "static": "Capacity added is a flow over a period; installed capacity is a stock at a date.",
        "source": "learning_package_final/Environment-and-Ecology/Subject-wide-Syllabus/28-Species-and-Current-Affairs-Tracker/Learning-Session.md (validated 2 August 2026)",
    },
    {
        "name": "Kulasekarapattinam SSLV launch complex",
        "date": "21 June 2026",
        "fact": "PIB material recorded the Kulasekarapattinam SSLV launch complex as under construction on 21 June 2026.",
        "institution": "Department of Space and ISRO",
        "static": "An approved or under-construction launch facility is not an operational facility.",
        "source": "learning_package_final/Science-and-Technology/Subject-wide-Syllabus/01-Space-Programme-ISRO,-Organisation-and-Launch-Vehicles/Learning-Session.md (validated 2 August 2026)",
    },
    {
        "name": "India's BRICS 2026 chairship launch",
        "date": "13 January 2026",
        "fact": "India launched the BRICS 2026 chairship theme, logo and website on 13 January 2026; this did not establish that a Leaders' Summit had already been completed.",
        "institution": "Ministry of External Affairs and the BRICS chairship process",
        "static": "Chairship-process activity and a concluded summit outcome are distinct statuses.",
        "source": "learning_package_final/International-Relations/Subject-wide-Syllabus/10-Regional,-Global-and-Minilateral-Groupings/Learning-Session.md (validated 3 August 2026)",
    },
    {
        "name": "BIMSTEC maritime transport agreement",
        "date": "16 May 2026",
        "fact": "The BIMSTEC maritime transport agreement entered into force on 16 May 2026 among Bhutan, India, Myanmar and Thailand, the four states then recorded as having deposited instruments.",
        "institution": "BIMSTEC treaty and depositary process",
        "static": "Entry into force among depositing states should not be described as binding every member automatically.",
        "source": "learning_package_final/International-Relations/Subject-wide-Syllabus/10-Regional,-Global-and-Minilateral-Groupings/Learning-Session.md (validated 3 August 2026)",
    },
]


def current_question(event: dict[str, str], variant: int) -> dict[str, Any]:
    if variant == 0:
        stem = (
            f"With reference to {event['name']} dated {event['date']}, consider the following statements: "
            f"1. {event['fact']} 2. {event['static']} "
            "3. The dated development by itself created a constitutionally entrenched entitlement applicable in every case. "
            "Which of the statements given above are correct?"
        )
        options = [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3",
        ]
        correct = 0
        reasons = [
            "Correct: statements 1 and 2 preserve both the dated fact and the static legal or conceptual boundary; statement 3 overstates the event's legal effect.",
            "Incorrect: statement 3 converts a policy, institutional or scientific development into an automatic constitutional entitlement.",
            "Incorrect: statement 1 is also supported by the dated official source, while statement 3 remains false.",
            "Incorrect: the universal legal consequence in statement 3 does not follow from the event.",
        ]
    elif variant == 1:
        stem = (
            f"Consider the following pairs concerning {event['name']} ({event['date']}): "
            f"1. Dated fact - {event['fact']} "
            f"2. Responsible institution/process - {event['institution']} "
            f"3. Static interpretation - {event['static']} "
            "How many of the above pairs preserve the correct fact, institution and status?"
        )
        options = [
            "All three",
            "Only one",
            "Only two",
            "None",
        ]
        correct = 0
        reasons = [
            "Correct: the dated official record supports the fact, identifies the responsible institution or process and states the qualified static interpretation.",
            "Incorrect: more than one pair is correct; the option discards valid institutional and conceptual linkages.",
            "Incorrect: the third pair is also correct because it prevents a status or category error.",
            "Incorrect: each pair is supported by the dated official record.",
        ]
    elif variant == 2:
        stem = (
            f"A policy analyst uses {event['name']} ({event['date']}) to make the following claims: "
            f"1. {event['static']} "
            "2. A dated target, allocation, approval or meeting may be treated as an achieved outcome without checking status. "
            "3. The competent institution and legal category must be identified before drawing an inference. "
            "Which claims are methodologically sound?"
        )
        options = [
            "1 and 3 only",
            "1 and 2 only",
            "2 and 3 only",
            "1, 2 and 3",
        ]
        correct = 0
        reasons = [
            "Correct: claims 1 and 3 preserve conceptual and institutional discipline; claim 2 collapses announced or intermediate status into achievement.",
            "Incorrect: claim 2 is precisely the status error that current-affairs elimination should reject.",
            "Incorrect: claim 1 is also sound, whereas claim 2 is not.",
            "Incorrect: all three cannot be accepted because claim 2 removes the required status check.",
        ]
    else:
        stem = (
            f"Consider the following statements about {event['name']} ({event['date']}): "
            f"1. {event['fact']} "
            f"2. {event['static']} "
            "3. Replacing the competent institution with a neighbouring constitutional or international body would not alter the accuracy of the claim. "
            "Which one of the following is correct?"
        )
        options = [
            "Statements 1 and 2 are correct, while statement 3 is incorrect.",
            "Statements 1 and 3 are correct, while statement 2 is incorrect.",
            "Statements 2 and 3 are correct, while statement 1 is incorrect.",
            "All three statements are correct.",
        ]
        correct = 0
        reasons = [
            "Correct: statements 1 and 2 are factually sound; statement 3 is false because institutional identity is often the decisive UPSC distinction.",
            "Incorrect: statement 2 is valid and statement 3 is not.",
            "Incorrect: the dated official record supports statement 1, while statement 3 remains false.",
            "Incorrect: institutional substitution can change competence, legal status and the truth of the claim.",
        ]
    return {
        "stem": plain(stem),
        "options": list(map(plain, options)),
        "correct_index": correct,
        "reasons": reasons,
        "explanation": f"[Fact] {event['fact']} [Analysis] {event['static']}",
        "trap": "Do not convert a dated executive, diplomatic or scientific event into a different legal category.",
        "source": event["source"],
        "subject": "Current Affairs",
        "current": True,
        "difficulty_score": 7,
    }


def prelims_sets() -> dict[int, list[dict[str, Any]]]:
    pools = build_static_pool()
    offsets = defaultdict(int)
    built: dict[int, list[dict[str, Any]]] = {}
    global_stems: set[str] = set()
    for set_no in SETS:
        selected: list[dict[str, Any]] = []
        for label, (_, count) in STATIC_PLAN.items():
            pool = pools[label]
            while len([q for q in selected if q.get("category") == label]) < count:
                if offsets[label] >= len(pool):
                    raise RuntimeError(f"Insufficient unique parsed MCQs for {label}")
                candidate = dict(pool[offsets[label]])
                offsets[label] += 1
                key = normalize_stem(candidate["stem"])
                if key in global_stems:
                    continue
                candidate["category"] = label
                global_stems.add(key)
                selected.append(candidate)
        for local in range(10):
            event_index = (set_no - 1) * 10 + local
            event = CURRENT_EVENTS[event_index % len(CURRENT_EVENTS)]
            variant = event_index // len(CURRENT_EVENTS)
            candidate = current_question(event, variant)
            candidate["category"] = "Current Affairs"
            key = normalize_stem(candidate["stem"])
            if key in global_stems:
                raise RuntimeError("Duplicate current-affairs stem")
            global_stems.add(key)
            selected.append(candidate)
        if len(selected) != 100:
            raise RuntimeError(f"Set {set_no}: expected 100 Prelims questions")
        rendered: list[dict[str, Any]] = []
        for qno, question in enumerate(selected, 1):
            target = (qno - 1) % 4
            opts, correct, reasons = rotate_options(
                question["options"], question["correct_index"], target, question["reasons"]
            )
            item = dict(question)
            item.update(
                no=qno, options=opts, correct_index=correct,
                answer=LETTERS[correct], reasons=reasons,
            )
            rendered.append(item)
        built[set_no] = rendered
    return built


# ---------------------------------------------------------------------------
# CSAT generation

RC_PASSAGES = [
    ("A district digitised land records, but dispute resolution did not improve until maps, mutation registers and field verification were reconciled. Technology reduced search time; it could not decide contested title by itself.",
     "Digitisation improves access but cannot replace legal and field reconciliation.",
     "Faster retrieval and accurate adjudication are different outcomes.",
     "Citizens contesting title require records that refer to the same parcel.",
     "qualified and analytical"),
    ("A self-help group began collective procurement of seed. Costs fell, yet the poorest members benefited only after instalment payments were allowed. Scale created efficiency; payment design determined inclusion.",
     "Collective buying needs inclusive payment design to share its gains.",
     "Lower unit cost alone need not make an input affordable.",
     "Some poorer members faced a liquidity constraint.",
     "balanced"),
    ("A city planted roadside trees but survival remained low where contracts rewarded planting rather than maintenance. When payments were linked to three-year survival, contractors changed species choice and watering schedules.",
     "Outcome-linked contracts can improve urban tree survival.",
     "Incentives influenced maintenance and species choice.",
     "Survival can be measured reliably enough to affect payment.",
     "evidence-based"),
    ("A school served breakfast before morning classes. Attendance rose, but learning gains were largest where teachers also used short diagnostic exercises. Nutrition improved readiness; instruction converted readiness into learning.",
     "Nutrition and responsive teaching work as complements.",
     "Attendance gains do not automatically equal learning gains.",
     "Diagnostic exercises helped teachers adapt instruction.",
     "measured"),
    ("A coastal village received cyclone warnings in time, yet evacuation lagged until local volunteers translated the message into landmarks and arranged transport for older residents. Forecast accuracy mattered, but last-mile trust and capability completed the warning chain.",
     "Early warning succeeds only when trusted last-mile action is possible.",
     "Technical forecasts can fail to produce evacuation without local capability.",
     "Residents understood and trusted locally translated guidance.",
     "cautionary"),
    ("A hospital introduced online appointments. Missed visits fell for smartphone users but rose among patients who shared phones. A call-based fallback restored access without abandoning the digital system.",
     "Digital services need fallback channels to avoid exclusion.",
     "A uniform channel can distribute convenience unequally.",
     "Shared-phone users could use the call-based alternative.",
     "pragmatic"),
    ("A watershed project measured only the number of check dams. An audit found that poorly located structures trapped little runoff, while fewer structures placed after contour mapping improved recharge. Counting assets obscured performance.",
     "Asset counts are weaker than outcome and location-sensitive evaluation.",
     "More structures do not necessarily produce more recharge.",
     "Contour-informed placement affects captured runoff.",
     "critical but constructive"),
    ("A public library extended opening hours. Usage increased mainly after bus timings were coordinated with closing time. The library had removed a formal barrier, while transport coordination removed a practical one.",
     "Access depends on complementary services, not formal availability alone.",
     "Longer hours may be ineffective when return transport is unavailable.",
     "Some potential users depended on buses.",
     "explanatory"),
    ("Farmers received weather advisories by text. Adoption improved when messages specified the crop stage and local rainfall probability rather than giving district-wide warnings. More information was not enough; relevant information changed decisions.",
     "Advisories influence action when they are locally and temporally relevant.",
     "Information quantity and decision usefulness are not identical.",
     "Farmers could relate crop-stage advice to an available action.",
     "diagnostic"),
    ("A municipal dashboard published complaint totals. Departments first closed easy cases to improve rankings. After the metric included age and recurrence of complaints, effort shifted towards persistent failures. Measurement changed behaviour twice.",
     "Performance metrics must anticipate strategic responses.",
     "Simple closure counts can reward superficial compliance.",
     "Departments respond to the incentives embedded in rankings.",
     "analytical"),
    ("A rural enterprise trained women in food processing. Income rose where training was paired with quality certification and market links; training alone produced skills without reliable sales.",
     "Skills generate income when connected to standards and markets.",
     "Training completion is not the same as commercial success.",
     "Buyers valued certification or dependable quality.",
     "balanced"),
    ("A bus corridor reserved lanes during peak hours. Travel time became predictable even when average speed changed little. Reliability allowed workers to plan transfers and reduced the penalty of uncertainty.",
     "Predictability can be a major transport benefit even without large speed gains.",
     "Average speed can hide variation in journey time.",
     "Travellers value lower uncertainty when planning connections.",
     "favourable but qualified"),
    ("A nutrition programme distributed fortified food. Coverage was high, but anaemia fell slowly where infections and poor sanitation persisted. The supplement addressed one pathway, not every cause.",
     "Single nutritional interventions cannot overcome all causes of anaemia.",
     "High distribution coverage need not ensure equivalent health outcomes.",
     "Infection and sanitation independently affect anaemia.",
     "qualified"),
    ("A police station published service standards. Complaints about delay fell only after applicants received dated receipts and an appeal contact. A promise became enforceable when citizens could prove and escalate non-compliance.",
     "Service standards need traceability and escalation to become effective.",
     "Publication alone may not alter administrative behaviour.",
     "Receipts and appeal contacts enabled accountability.",
     "institutional"),
    ("A solar irrigation subsidy lowered pumping costs. Groundwater use increased in villages without metering, while feeder separation and water budgeting moderated extraction elsewhere. Clean energy solved an emissions problem but could intensify a resource problem.",
     "Policies can solve one externality while worsening another unless incentives are aligned.",
     "Renewable energy does not automatically ensure sustainable water use.",
     "Pumping decisions respond to the marginal cost of electricity.",
     "cautionary"),
    ("A district recruited more health workers. Immunisation improved only after vacant supervisory posts were filled and cold-chain failures were logged. Staff numbers mattered, but coordination and supplies determined effective capacity.",
     "Public capacity depends on management and logistics as well as headcount.",
     "Recruitment alone need not remove delivery bottlenecks.",
     "Supervision and cold-chain reliability affect immunisation.",
     "measured"),
    ("A cooperative displayed daily market prices. Members gained bargaining power, but farmers with perishable produce still accepted low offers when transport was unavailable. Information reduced one asymmetry; logistics preserved another.",
     "Price information improves bargaining but cannot replace market access.",
     "Sellers under time pressure may not realise the displayed price.",
     "Transport constraints limited farmers' ability to wait or switch buyers.",
     "balanced"),
    ("A flood map was updated with recent construction. Residents objected when insurance premiums rose, but the old map had understated exposure. Accurate risk information imposed visible costs while reducing hidden vulnerability.",
     "Better risk information can be unpopular because it reveals rather than creates exposure.",
     "Higher premiums may reflect corrected measurement.",
     "The revised map more accurately represented present conditions.",
     "analytical"),
    ("A university made lectures available online. Completion improved when students also joined small peer groups with weekly deadlines. Content access removed scarcity; social commitment reduced procrastination.",
     "Online access and structured peer accountability can complement each other.",
     "Availability alone does not guarantee course completion.",
     "Deadlines and peer contact influenced study behaviour.",
     "constructive"),
    ("A village committee rotated meeting times. Women's attendance rose, but participation became meaningful only after agenda papers were shared in advance. Presence was enabled by timing; voice was enabled by preparation.",
     "Inclusive participation requires both accessible timing and usable information.",
     "Attendance is not identical to effective influence.",
     "Advance information helped participants formulate views.",
     "balanced and precise"),
]


def csat_item(
    stem: str,
    correct: Any,
    distractors: list[Any],
    method: str,
    trap: str,
    category: str,
    steps: int = 2,
) -> dict[str, Any]:
    options = [plain(correct)] + [plain(x) for x in distractors]
    if len(set(options)) != 4:
        raise ValueError(f"Duplicate CSAT options: {stem}: {options}")
    reasons = [
        f"Correct. {method}",
        f"Incorrect: {plain(distractors[0])} does not follow the stated data. {method}",
        f"Incorrect: {plain(distractors[1])} is an intermediate, sign or operation error. {method}",
        f"Incorrect: {plain(distractors[2])} ignores a condition or uses the wrong base. {method}",
    ]
    return {
        "stem": plain(stem), "options": options, "correct_index": 0,
        "reasons": reasons, "explanation": plain(method), "trap": plain(trap),
        "source": "Repository-generated checked CSAT item; method grounded in upsc-ai-kit/knowledge/CSAT.",
        "subject": "CSAT", "category": category, "current": False,
        "difficulty": "above-typical recent UPSC qualifying level",
        "reasoning_steps": steps,
        "uniquely_solvable": True,
    }


def make_rc(set_no: int) -> list[dict[str, Any]]:
    output = []
    start = (set_no - 1) * 5
    for passage, central, inference, assumption, tone in RC_PASSAGES[start:start + 5]:
        passage = (
            passage
            + " The episode also warns against reading an aggregate improvement as proof that every group benefited equally. "
              "A sound evaluation must distinguish the formal input, the mechanism through which people can use it, "
              "and the distribution of gains or burdens when implementation conditions differ."
        )
        specs = [
            ("Which option best states the central idea?", central, [
                "The intervention should be abandoned in every setting.",
                "The passage proves that implementation conditions never matter.",
                "The passage recommends maximising only the most visible input.",
            ], "The central idea joins the intervention's benefit to the condition that makes it effective."),
            ("Which inference is best supported?", inference, [
                "Every stakeholder responds identically in all circumstances.",
                "The opposite outcome must occur whenever one condition changes.",
                "A policy not discussed in the passage is legally compulsory.",
            ], "The inference is limited to what the passage's comparison supports."),
            ("Which assumption is necessary for the reasoning?", assumption, [
                "The intervention has no cost under any condition.",
                "No alternative explanation can ever exist.",
                "All participants possess identical preferences and resources.",
            ], "The necessary assumption connects the observed mechanism to the stated conclusion."),
            ("The author's tone is best described as:", tone, [
                "unreservedly celebratory", "hostile and dismissive", "unrelated and indifferent",
            ], "The passage recognises both achievement and limitation, so an absolute tone is unsupported."),
        ]
        for question, answer, distractors, method in specs:
            output.append(csat_item(
                f"Passage: {passage} {question}", answer, distractors,
                method, "Choose the qualified claim; reject universal language not supported by the passage.",
                "Reading Comprehension",
            ))
    return output


def make_quant(set_no: int) -> list[dict[str, Any]]:
    q: list[dict[str, Any]] = []
    base = 10 * set_no
    # Numeracy (8)
    n = 137 + 17 * set_no
    d = 7 + set_no
    expression = n * n + 3 * n + 5
    remainder = expression % d
    q.append(csat_item(f"What is the remainder when {n}^2 + 3x{n} + 5 is divided by {d}?", remainder,
                       [(remainder + 1) % d, (remainder + 2) % d, (remainder + 3) % d],
                       f"Reduce {n} modulo {d}, then evaluate r^2+3r+5 modulo {d}; the remainder is {remainder}.",
                       "Reduce each term modulo the divisor; do not expand the large square unnecessarily.", "Numeracy", 3))
    a, b = 18 + 2 * set_no, 30 + 3 * set_no
    aa, bb = 2 * a, 3 * b
    g = math.gcd(aa, bb)
    q.append(csat_item(f"Two numbers are obtained by doubling {a} and tripling {b}. What is their HCF?", g,
                       [g + 1, g + 2, aa * bb // g],
                       f"The derived numbers are {aa} and {bb}; Euclid's algorithm gives gcd({aa}, {bb}) = {g}.",
                       "Apply the transformation before computing the HCF.", "Numeracy", 2))
    number = 2 ** (set_no + 1) * 3 ** 2
    divs = (set_no + 2) * 3
    q.append(csat_item(f"How many positive divisors does {number} have?", divs,
                       [divs - 1, divs + 1, set_no + 5],
                       f"{number} = 2^{set_no + 1} x 3^2, so divisor count = ({set_no + 2})(3) = {divs}.",
                       "Add one to every prime exponent before multiplying.", "Numeracy"))
    power = 11 + set_no
    other_base, other_power = 7 + set_no, 5 + set_no
    unit = (pow(3 + set_no, power, 10) * pow(other_base, other_power, 10)) % 10
    q.append(csat_item(f"What is the unit digit of ({3 + set_no}^{power}) x ({other_base}^{other_power})?", unit,
                       [(unit + 1) % 10, (unit + 2) % 10, (unit + 3) % 10],
                       f"Find each unit-digit cycle separately and multiply the two terminal digits modulo 10; the result is {unit}.",
                       "Do not add the unit digits of the factors.", "Numeracy", 3))
    first, diff, term = 3 + set_no, 2 + set_no, 9
    ans = term * (2 * first + (term - 1) * diff) / 2
    q.append(csat_item(f"The arithmetic sequence begins {first}, {first+diff}, {first+2*diff}. What is the sum of its first {term} terms?",
                       ans, [ans - diff, ans + diff, first + (term - 1) * diff],
                       f"S_n=n/2[2a+(n-1)d]={term}/2[2x{first}+8x{diff}]={ans}.",
                       "The last term is not the sum.", "Numeracy", 3))
    val = 9876 + 111 * set_no
    product = val * 9
    digit_sum = sum(map(int, str(product)))
    q.append(csat_item(f"After multiplying {val} by 9, what is the sum of the decimal digits of the product?", digit_sum,
                       [digit_sum - 1, digit_sum + 1, digit_sum + 2],
                       f"{val}x9={product}; adding the digits of {product} gives {digit_sum}.",
                       "The divisibility-by-9 check verifies the digit sum but does not by itself give its unreduced value.", "Numeracy", 2))
    low, high, k = 15 + set_no, 120 + 2 * set_no, 6 + set_no
    count_k = high // k - (low - 1) // k
    count_2k = high // (2*k) - (low - 1) // (2*k)
    count = count_k - count_2k
    q.append(csat_item(f"How many integers from {low} through {high}, inclusive, are divisible by {k} but not by {2*k}?", count,
                       [count - 1, count + 1, count + 2],
                       f"Count multiples of {k} ({count_k}) and subtract multiples of {2*k} ({count_2k}); result {count}.",
                       "Multiples of the larger divisor are a subset and must be excluded once.", "Numeracy", 3))
    nums = [12 + set_no, 18 + set_no, 24 + set_no, 30 + set_no]
    changed = [nums[0] - set_no, nums[1], nums[2], nums[3] + 2 * set_no]
    avg = sum(changed) / len(changed)
    q.append(csat_item(
        f"The values are {', '.join(map(str, nums))}. If the smallest falls by {set_no} and the largest rises by {2*set_no}, what is the new mean?",
        avg, [sum(nums)/4, avg + 1, avg + 2],
        f"The adjusted values are {changed}; their total {sum(changed)} divided by 4 gives {avg}.",
        "Apply both changes to the total before dividing.", "Numeracy", 3))
    # Algebra (6)
    x = 5 + set_no
    q.append(csat_item(f"If 3x + {2*set_no} = {3*x + 2*set_no}, what is x?", x,
                       [x - 1, x + 1, 3 * x],
                       f"Subtract {2*set_no} and divide by 3: x = {x}.",
                       "Undo addition before division.", "Algebra"))
    x = 4 + set_no
    q.append(csat_item(f"If 2(x - {set_no}) = {2*(x-set_no)}, what is x when x is a positive integer and the displayed equality is supplemented by x + {set_no} = {x+set_no}?",
                       x, [x - 1, x + 1, 2 * x],
                       f"The second equation fixes x: x + {set_no} = {x+set_no}, hence x = {x}.",
                       "An identity alone cannot determine x; use the independent equation.", "Algebra"))
    p = 8 + set_no
    q.append(csat_item(f"The sum of two consecutive integers is {2*p+1}. What is the smaller integer?", p,
                       [p + 1, p - 1, 2 * p + 1],
                       f"Let the integers be x and x+1. Then 2x+1={2*p+1}, so x={p}.",
                       "The question asks for the smaller integer.", "Algebra"))
    age = 20 + 2 * set_no
    future_delta = age - 10
    q.append(csat_item(f"Five years ago A was half of A's age {future_delta} years from now. What is A's present age?",
                       age, [age - 5, age + 5, age // 2],
                       f"Let present age be x. Then x-5 = (x+{future_delta})/2; solving gives x={age}.",
                       "Translate both time references from the present.", "Algebra"))
    root = 6 + set_no
    q.append(csat_item(f"What is the positive solution of x^2 = {root*root}?", root,
                       [-root, root * root, root + 1],
                       f"x = plus or minus {root}; the positive solution is {root}.",
                       "The word positive removes the negative root.", "Algebra"))
    threshold = 7 + set_no
    q.append(csat_item(f"Which value is the least integer satisfying 2x + 1 > {2*threshold}?", threshold,
                       [threshold - 1, threshold + 1, 2 * threshold],
                       f"2x > {2*threshold-1}, so x > {(2*threshold-1)/2}; the least integer is {threshold}.",
                       "A strict inequality excludes the boundary.", "Algebra"))
    # Percentages, ratios, averages (8)
    pct, amount = 10 + 5 * set_no, 240 + 40 * set_no
    result = pct * amount // 100
    surcharge = 5 + set_no
    compound_result = result * (100 + surcharge) / 100
    q.append(csat_item(f"A grant equals {pct}% of Rs {amount}. An administrative surcharge of {surcharge}% is then applied to the grant. What is the final amount?",
                       compound_result, [result, compound_result - surcharge, amount * (pct+surcharge)/100],
                       f"First grant={pct}/100x{amount}={result}; then multiply by {100+surcharge}/100 to get {compound_result}.",
                       "The surcharge applies to the grant, not to the original amount.", "Percentages", 3))
    start, rise, fall = 1000, 8 + set_no, 3 + set_no
    final = round(start * (1 + rise / 100) * (1 - fall / 100), 2)
    q.append(csat_item(f"A value of {start} rises by {rise}% and then falls by {fall}%. What is the final value?",
                       final, [start + 10 * (rise-fall), round(start*(1+(rise-fall)/100),2), final + 10],
                       f"Successive multipliers give {start} x {1+rise/100:.2f} x {1-fall/100:.2f} = {final}.",
                       "Successive percentages are not simply netted.", "Percentages"))
    total, r1, r2 = 420 + 60 * set_no, 2 + set_no, 3
    share = total * r1 / (r1 + r2)
    q.append(csat_item(f"Rs {total} is divided in the ratio {r1}:{r2}. What is the first share?", share,
                       [share-r1, share+r1, total/(r1+r2)],
                       f"First share = {total} x {r1}/({r1}+{r2}) = {share}.",
                       "Use ratio parts, not either raw ratio number.", "Ratios"))
    n1, n2, av1, av2 = 20+set_no, 30+set_no, 40+set_no, 60+set_no
    comb = round((n1*av1+n2*av2)/(n1+n2), 2)
    q.append(csat_item(f"Groups of {n1} and {n2} have averages {av1} and {av2}. What is their combined average?",
                       comb, [(av1+av2)/2, comb-1, comb+1],
                       f"Weighted mean = ({n1}x{av1}+{n2}x{av2})/({n1+n2}) = {comb}.",
                       "Do not average group averages without weights.", "Averages"))
    cost, profit = 500+50*set_no, 15+set_no
    sell = cost*(100+profit)/100
    rebate = 4 + set_no
    net_sell = sell * (100-rebate)/100
    q.append(csat_item(f"An article costs Rs {cost}, is marked for a {profit}% profit, and then receives a {rebate}% rebate on that marked selling price. What is the realised price?",
                       net_sell, [sell, cost*(100+profit-rebate)/100, net_sell+rebate],
                       f"Marked selling price={sell}; realised price={sell}x{100-rebate}/100={net_sell}.",
                       "Profit and rebate use different successive bases.", "Percentages", 3))
    marked, disc = 800+100*set_no, 10+set_no
    price = marked*(100-disc)/100
    q.append(csat_item(f"A marked price of Rs {marked} is discounted by {disc}%. What is the sale price?",
                       price, [marked-disc, marked*(100+disc)/100, price-disc],
                       f"Sale price = {marked} x {100-disc}/100 = {price}.",
                       "A percentage discount is not a rupee subtraction.", "Percentages"))
    mix_a, mix_b = 3+set_no, 5
    total_l = 32+4*set_no
    first_l = total_l*mix_a/(mix_a+mix_b)
    q.append(csat_item(f"A mixture contains milk and water in the ratio {mix_a}:{mix_b}. In {total_l} litres, how many litres are milk?",
                       first_l, [first_l-1, total_l/(mix_a+mix_b), first_l+1],
                       f"Milk = {total_l} x {mix_a}/({mix_a}+{mix_b}) = {first_l}.",
                       "The first term of the ratio denotes milk.", "Ratios"))
    old_avg, count, new = 40+set_no, 5+set_no, 52+set_no
    new_avg = (old_avg*count+new)/(count+1)
    q.append(csat_item(f"The average of {count} values is {old_avg}. After adding {new}, what is the new average?",
                       round(new_avg,2), [old_avg, round((old_avg+new)/2,2), round(new_avg+1,2)],
                       f"Old total {old_avg*count}; new average = ({old_avg*count}+{new})/{count+1} = {new_avg:.2f}.",
                       "Recover the old total before adding a value.", "Averages"))
    return q


def make_rates_di_logic(set_no: int) -> list[dict[str, Any]]:
    q: list[dict[str, Any]] = []
    # Time and work (6)
    a, b = 8 + set_no, 12 + set_no
    together = a*b/(a+b)
    q.append(csat_item(f"A can finish a task in {a} days and B in {b} days. How many days will they take together?",
                       round(together,2), [a+b, round((a+b)/2,2), round(abs(a-b),2)],
                       f"Combined rate = 1/{a}+1/{b}; time = {a*b}/({a+b}) = {together:.2f} days.",
                       "Add rates, not times.", "Time and Work"))
    workers, days, new_workers = 12+set_no, 15, 18+set_no
    new_days = workers*days/new_workers
    q.append(csat_item(f"{workers} workers finish a job in {days} days at equal efficiency. How many days will {new_workers} workers take?",
                       round(new_days,2), [days, round(days*new_workers/workers,2), round(new_days+1,2)],
                       f"Worker-days stay constant: {workers}x{days}={new_workers}xd, so d={new_days:.2f}.",
                       "For fixed work, workers and days vary inversely.", "Time and Work"))
    tank_a, tank_b = 6+set_no, 8+set_no
    fill = tank_a*tank_b/(tank_a+tank_b)
    q.append(csat_item(f"Two pipes fill a tank in {tank_a} and {tank_b} hours. If opened together, how long do they take?",
                       round(fill,2), [tank_a+tank_b, round((tank_a+tank_b)/2,2), round(fill+1,2)],
                       f"Rates add: 1/{tank_a}+1/{tank_b}; reciprocal gives {fill:.2f} hours.",
                       "Both are inlet pipes.", "Time and Work"))
    leak, inlet = 20+set_no, 5+set_no
    net = 1/inlet - 1/leak
    time = 1/net
    q.append(csat_item(f"An inlet fills a tank in {inlet} hours while a leak empties it in {leak} hours. How long to fill together?",
                       round(time,2), [round(1/(1/inlet+1/leak),2), leak-inlet, inlet],
                       f"Net rate = 1/{inlet}-1/{leak}; time = {time:.2f} hours.",
                       "An outlet rate must be subtracted.", "Time and Work"))
    efficiency = 2 + set_no
    q.append(csat_item(f"A is {efficiency} times as efficient as B. If B alone takes {10*efficiency} days, how many days does A take?",
                       10, [10*efficiency, efficiency, 10+efficiency],
                       f"Time is inverse to efficiency: {10*efficiency}/{efficiency}=10 days.",
                       "Greater efficiency means less time.", "Time and Work"))
    done = 1/3 + set_no/30
    remaining = 1-done
    q.append(csat_item(f"A team completes {done:.2f} of a job. What fraction remains, rounded to two decimals?",
                       round(remaining,2), [round(done,2), round(1+done,2), round(remaining+0.1,2)],
                       f"Remaining work = 1 - {done:.2f} = {remaining:.2f}.",
                       "Completed and remaining fractions sum to one.", "Time and Work"))
    # Speed and distance (6)
    speed, hours = 45+5*set_no, 3+set_no
    halt_minutes = 15 * set_no
    moving_hours = hours - halt_minutes / 60
    dist = speed * moving_hours
    q.append(csat_item(f"A vehicle's total journey time is {hours} hours, including a halt of {halt_minutes} minutes. It moves at {speed} km/h whenever in motion. What distance is covered?",
                       dist, [speed*hours, dist-speed, dist+speed],
                       f"Moving time={hours}-{halt_minutes}/60={moving_hours} hours; distance={speed}x{moving_hours}={dist} km.",
                       "Remove halt time before multiplying by speed.", "Speed and Distance", 3))
    distance, speed1, speed2 = 240+20*set_no, 40+set_no, 60+set_no
    saved = distance/speed1-distance/speed2
    q.append(csat_item(f"Over {distance} km, how many hours are saved by increasing speed from {speed1} to {speed2} km/h?",
                       round(saved,2), [round(distance/(speed2-speed1),2), round(saved+1,2), round(saved-1,2)],
                       f"Time saved = {distance}/{speed1} - {distance}/{speed2} = {saved:.2f} hours.",
                       "Subtract travel times, not speeds.", "Speed and Distance"))
    length, train_speed = 180+10*set_no, 54
    seconds = length/(train_speed*5/18)
    platform = 90 + 5 * set_no
    seconds = (length + platform)/(train_speed*5/18)
    q.append(csat_item(f"A {length}-metre train moves at {train_speed} km/h. How many seconds does it take to clear a {platform}-metre platform?",
                       round(seconds,2), [round(length/(train_speed*5/18),2), round(seconds+2,2), round(seconds-2,2)],
                       f"Total distance={length}+{platform}; {train_speed} km/h=15 m/s; time={seconds:.2f} s.",
                       "To clear a platform, use train length plus platform length.", "Speed and Distance", 3))
    stream, boat = 2+set_no, 10+set_no
    upstream = boat-stream
    journey = 2 * upstream
    q.append(csat_item(f"A boat's still-water speed is {boat} km/h and stream speed is {stream} km/h. How long does it take to travel {journey} km upstream?",
                       2, [journey/(boat+stream), upstream, journey/boat],
                       f"Upstream speed={boat}-{stream}={upstream} km/h; time={journey}/{upstream}=2 hours.",
                       "First obtain upstream speed, then divide distance by that speed.", "Speed and Distance", 3))
    side = 20+set_no
    perimeter = 4*side
    laps = 3 + set_no
    q.append(csat_item(f"A runner completes {laps} laps of a square field of side {side} m in {2*laps} minutes. What is the runner's speed in metres per minute?",
                       perimeter/2, [perimeter, side*side/(2*laps), perimeter/laps],
                       f"Total distance={laps}x4x{side}; divide by {2*laps} minutes to get {perimeter/2} m/min.",
                       "Compute total distance and total time before cancelling common factors.", "Speed and Distance", 3))
    d1, d2, s1, s2 = 120, 180, 40+set_no, 60+set_no
    avg_speed = (d1+d2)/(d1/s1+d2/s2)
    q.append(csat_item(f"A car covers {d1} km at {s1} km/h and {d2} km at {s2} km/h. What is average speed?",
                       round(avg_speed,2), [(s1+s2)/2, round(avg_speed+2,2), round(avg_speed-2,2)],
                       f"Average speed = total distance/total time = {d1+d2}/({d1}/{s1}+{d2}/{s2}) = {avg_speed:.2f}.",
                       "Speeds need time weights.", "Speed and Distance"))
    # Data interpretation (8)
    vals = [80+5*set_no, 95+4*set_no, 110+3*set_no, 125+2*set_no]
    labels = ["A", "B", "C", "D"]
    data = ", ".join(f"{lab}={val}" for lab, val in zip(labels, vals))
    q.append(csat_item(f"A table reports district outputs ({data}). What is the total?", sum(vals),
                       [sum(vals)-10, sum(vals)+10, max(vals)],
                       f"Add all four entries: {'+'.join(map(str,vals))}={sum(vals)}.",
                       "Use every row exactly once.", "Data Interpretation"))
    q.append(csat_item(f"Using the table ({data}), what is the difference between the highest and lowest values?",
                       max(vals)-min(vals), [max(vals), min(vals), max(vals)+min(vals)],
                       f"Range = {max(vals)}-{min(vals)}={max(vals)-min(vals)}.",
                       "Range is a difference, not an endpoint.", "Data Interpretation"))
    q.append(csat_item(f"Using the table ({data}), what is the average of the four values?",
                       sum(vals)/4, [sum(vals), sum(vals)/2, max(vals)-min(vals)],
                       f"Average = {sum(vals)}/4={sum(vals)/4}.",
                       "Divide the total by four.", "Data Interpretation"))
    q.append(csat_item(f"Using the table ({data}), by what percentage does D exceed A?",
                       round((vals[3]-vals[0])*100/vals[0],2),
                       [round((vals[3]-vals[0])*100/vals[3],2), vals[3]-vals[0], round(vals[3]*100/vals[0],2)],
                       f"Percentage increase = ({vals[3]}-{vals[0]})/{vals[0]} x100.",
                       "Use the original value A as denominator.", "Data Interpretation"))
    second = [
        vals[0] + 20 + set_no,
        vals[1] + 15 + set_no,
        vals[2] + 10 + set_no,
        vals[3] + 5 + set_no,
    ]
    data2 = ", ".join(f"{lab}={val}" for lab, val in zip(labels, second))
    q.append(csat_item(f"Year 1 values are {data}; Year 2 values are {data2}. Which district has the largest absolute increase?",
                       labels[0], labels[1:],
                       f"The increases are {20+set_no}, {15+set_no}, {10+set_no} and {5+set_no}; A is largest.",
                       "Check absolute increases before comparing totals.", "Data Interpretation"))
    q.append(csat_item(f"Using Year 2 ({data2}), what fraction of the total belongs to B, rounded to two decimals?",
                       round(second[1]/sum(second),2),
                       [round(second[1]/sum(vals),2), round(sum(second)/second[1],2), round(second[0]/sum(second),2)],
                       f"B's share = {second[1]}/{sum(second)} = {second[1]/sum(second):.2f}.",
                       "The denominator is the same-year total.", "Data Interpretation"))
    q.append(csat_item(f"Using Year 1 ({data}), if each unit earns Rs {2+set_no}, what is D's revenue?",
                       vals[3]*(2+set_no), [vals[3]+(2+set_no), vals[3], sum(vals)*(2+set_no)],
                       f"Revenue = D units x rate = {vals[3]} x {2+set_no}.",
                       "Use D's value, not total output.", "Data Interpretation"))
    q.append(csat_item(f"Using Year 1 ({data}), what is the ratio A:D in simplest form?",
                       f"{vals[0]//math.gcd(vals[0],vals[3])}:{vals[3]//math.gcd(vals[0],vals[3])}",
                       [f"{vals[3]}:{vals[0]}", f"{2*vals[0]}:{2*vals[3]}", f"{vals[0]+vals[3]}:1"],
                       f"Divide {vals[0]}:{vals[3]} by gcd {math.gcd(vals[0],vals[3])}.",
                       "Preserve the requested A-to-D order.", "Data Interpretation"))
    # Logical reasoning (6)
    groups = [("auditors", "trained", "certify"), ("surgeons", "licensed", "operate"),
              ("pilots", "qualified", "fly"), ("valuers", "registered", "sign valuations")]
    group, property_name, action = groups[set_no - 1]
    q.append(csat_item(f"All {group} are {property_name}. No person lacking that status may {action}. Which conclusion necessarily follows?",
                       f"Every {group[:-1]} is outside the class lacking that status.",
                       [f"Every {property_name} person is one of the {group}.",
                        f"Some {group} lack that status.", f"No {property_name} person may {action}."],
                       f"All {group} possess the stated status, so none can simultaneously lack it.",
                       "Do not reverse a universal proposition.", "Logical Reasoning"))
    shift = set_no
    coded = "".join(chr((ord(ch)-65+shift)%26+65) for ch in "INDIA")
    q.append(csat_item(f"If each letter is shifted forward by {shift}, how is INDIA coded?", coded,
                       ["INDIA", coded[::-1], "JODJB"],
                       f"Shift each letter independently by {shift}: INDIA -> {coded}.",
                       "Do not reverse the word.", "Logical Reasoning"))
    seq = 2 + set_no
    series = [seq]
    increments = [2,4,6,8]
    for inc in increments:
        series.append(series[-1]+inc)
    q.append(csat_item(f"Complete the series: {', '.join(map(str,series[:-1]))}, ?", series[-1],
                       [series[-1]-1, series[-1]+1, series[-2]+6],
                       f"Successive increments are 2, 4, 6 and 8; next term is {series[-1]}.",
                       "Track differences, not ratios.", "Logical Reasoning"))
    elders = ["Arun", "Leela", "Kabir", "Fatima"]
    children = ["Mira", "Rohan", "Tara", "Imran"]
    q.append(csat_item(f"{children[set_no-1]} is the child of {elders[set_no-1]}'s only son. How is {children[set_no-1]} related to {elders[set_no-1]}?",
                       "Grandchild", ["Child", "Niece or nephew", "Sibling"],
                       f"The only son is the parent, so {children[set_no-1]} is the elder's grandchild.",
                       "Resolve one relationship at a time.", "Logical Reasoning"))
    classes = [("books", "reports", "archived"), ("villages", "coastal settlements", "mapped"),
               ("clinics", "public facilities", "audited"), ("firms", "exporters", "registered")]
    first, middle, final = classes[set_no - 1]
    q.append(csat_item(f"Some {first} are {middle}. All {middle} are {final}. Which conclusion follows?",
                       f"Some {first} are {final}", [f"All {first} are {final}", f"No {first} are {final}", f"Some {final} are not {middle}"],
                       f"The members of {first} that are {middle} inherit the property {final}.",
                       "Do not universalise a particular premise.", "Logical Reasoning"))
    code_words = [("STATE", "TUBUF"), ("RIVER", "SJWFS"), ("PLANT", "QMBOU"), ("COURT", "DPVSU")]
    source_word, code_word = code_words[set_no - 1]
    q.append(csat_item(f"In a code, GOVERN is written as HPWFSO by shifting each letter forward once. How is {source_word} written?",
                       code_word, [source_word, code_word[::-1], "AAAAA"],
                       f"Shift every letter of {source_word} forward once to obtain {code_word}.",
                       "Apply the same shift to every letter.", "Logical Reasoning"))
    # Arrangements (4)
    letters = [["A", "B", "C", "D"], ["P", "Q", "R", "S"], ["K", "L", "M", "N"], ["W", "X", "Y", "Z"]][set_no-1]
    aa, bb, cc, dd = letters
    q.append(csat_item(f"{aa}, {bb}, {cc} and {dd} sit in a row. {aa} is left of {bb}; {cc} is right of {bb}; {dd} is left of {aa}. Who is second from the left?",
                       aa, [bb, cc, dd],
                       f"The only order consistent with all relations is {dd}-{aa}-{bb}-{cc}.",
                       "Build the full order before selecting a position.", "Arrangements"))
    tasks = [["P", "Q", "R", "S"], ["Audit", "Budget", "Consultation", "Draft"], ["Seed", "Sow", "Weed", "Harvest"], ["Survey", "Design", "Build", "Inspect"]][set_no-1]
    p1, p2, p3, p4 = tasks
    q.append(csat_item(f"Four tasks {p1}, {p2}, {p3} and {p4} occur consecutively. {p1} precedes {p2}; {p3} follows {p2}; {p4} precedes {p1}. Which task is third?",
                       p2, [p1, p3, p4],
                       f"The forced order is {p4}-{p1}-{p2}-{p3}, so {p2} is third.",
                       "Precedes means earlier, not immediately earlier unless stated.", "Arrangements"))
    names = [["K", "L", "M", "N", "O"], ["Asha", "Bina", "Charu", "Diya", "Esha"],
             ["Jai", "Kiran", "Lalit", "Mohan", "Nitin"], ["P", "R", "T", "V", "X"]][set_no-1]
    k, l, m, n, o = names
    q.append(csat_item(f"Five persons stand by height. {k} is taller than {l} but shorter than {m}. {n} is shorter than {l}. {o} is taller than {m}. Who is tallest?",
                       o, [m, k, n],
                       f"The chain is {o} > {m} > {k} > {l} > {n}.",
                       "Combine all comparisons into one chain.", "Arrangements"))
    schedules = [("Education", "Finance", "Review", "Health"), ("Survey", "Drafting", "Hearing", "Order"),
                 ("Seed purchase", "Sowing", "Inspection", "Harvest"), ("Design", "Tender", "Construction", "Audit")]
    first_event, second_event, third_event, fourth_event = schedules[set_no-1]
    q.append(csat_item(f"{third_event} is after {second_event} but before {fourth_event}. {first_event} is before {second_event}. Which is earliest?",
                       first_event, [second_event, third_event, fourth_event],
                       f"The order is {first_event}, {second_event}, {third_event}, {fourth_event}.",
                       "Translate every before/after relation consistently.", "Arrangements"))
    # Directions (4)
    turns = set_no
    dirs = ["North", "East", "South", "West"]
    faced = dirs[turns % 4]
    q.append(csat_item(f"A person faces North and turns right {turns} time(s), each by 90 degrees. Which direction is faced?",
                       faced, [d for d in dirs if d != faced],
                       f"Each right turn advances one step clockwise; {turns} turn(s) gives {faced}.",
                       "Reduce turns modulo four.", "Directions"))
    north = 3 * set_no
    east = 4 * set_no
    hyp = 5 * set_no
    q.append(csat_item(f"A walker goes {north} km north and {east} km east. How far is the endpoint from the start?",
                       f"{hyp} km", [f"{north+east} km", f"{east-north} km", f"{north*east} km"],
                       f"Displacement = sqrt({north}^2+{east}^2)={hyp} km.",
                       "Distance walked and displacement differ.", "Directions"))
    starts = ["East", "South", "West", "North"]
    start_dir = starts[set_no-1]
    start_index = dirs.index(start_dir)
    final_dir = dirs[(start_index-2) % 4]
    q.append(csat_item(f"A person starts facing {start_dir}, turns left, then turns left again. Which direction is now faced?",
                       final_dir, [d for d in dirs if d != final_dir],
                       f"Two left turns reverse the starting direction, giving {final_dir}.",
                       "Track orientation after each turn.", "Directions"))
    step = 4 + set_no
    q.append(csat_item(f"A point B is {step} km south of A, and C is {step} km east of B. In which direction is C from A?",
                       "South-East", ["North-East", "South-West", "North-West"],
                       "Relative to A, C has positive east and negative north coordinates: south-east.",
                       "Use a simple coordinate sketch.", "Directions"))
    # Data sufficiency (4)
    ds_options = [
        "Statement 1 alone is sufficient, but statement 2 alone is not.",
        "Statement 2 alone is sufficient, but statement 1 alone is not.",
        "Both statements together are sufficient, but neither alone is sufficient.",
        "Each statement alone is sufficient.",
    ]
    solution_x = 6 + set_no
    q.append(csat_item(f"What is x? Statement 1: x+{set_no+2}={solution_x+set_no+2}. Statement 2: 2x={2*solution_x}.",
                       ds_options[3], ds_options[:3],
                       f"Statement 1 gives x={solution_x}; statement 2 also gives x={solution_x}. Each alone is sufficient.",
                       "Test each statement separately before combining.", "Data Sufficiency"))
    q.append(csat_item(f"What is the area of a rectangle? Statement 1: its length is {7+set_no} cm. Statement 2: its breadth is {4+set_no} cm.",
                       ds_options[2], [ds_options[0], ds_options[1], ds_options[3]],
                       "Area requires both length and breadth; neither statement alone is enough.",
                       "Do not import an unstated shape relation.", "Data Sufficiency"))
    even_multiple = 2 * (set_no + 1)
    q.append(csat_item(f"Is integer n even? Statement 1: n is divisible by {2*even_multiple}. Statement 2: n is divisible by {even_multiple}.",
                       ds_options[3], ds_options[:3],
                       "Either divisibility condition independently implies n is even.",
                       "Sufficiency does not require both statements to be equally strong.", "Data Sufficiency"))
    root_ds = 6 + set_no
    q.append(csat_item(f"What is y? Statement 1: y is positive. Statement 2: y^2={root_ds*root_ds}.",
                       ds_options[2], [ds_options[0], ds_options[1], ds_options[3]],
                       f"Statement 2 gives y=plus or minus {root_ds}; statement 1 selects y={root_ds}. Together they are sufficient.",
                       "A square equation has two real roots unless sign is fixed.", "Data Sufficiency"))
    return q


def csat_sets() -> dict[int, list[dict[str, Any]]]:
    built = {}
    seen: set[str] = set()
    for set_no in SETS:
        raw = make_rc(set_no) + make_quant(set_no) + make_rates_di_logic(set_no)
        if len(raw) != 80:
            raise RuntimeError(f"Set {set_no}: generated {len(raw)} CSAT items, expected 80")
        rendered = []
        for qno, question in enumerate(raw, 1):
            key = normalize_stem(question["stem"])
            if key in seen:
                raise RuntimeError(f"Duplicate CSAT stem: {question['stem']}")
            seen.add(key)
            target = (qno - 1) % 4
            opts, correct, reasons = rotate_options(
                question["options"], question["correct_index"], target, question["reasons"]
            )
            item = dict(question)
            item.update(no=qno, options=opts, correct_index=correct,
                        answer=LETTERS[correct], reasons=reasons)
            rendered.append(item)
        built[set_no] = rendered
    return built


# ---------------------------------------------------------------------------
# Mains and Essay content

GS_DATA: dict[str, list[tuple[str, str, str, str, str, str]]] = {
    "GS-I": [
        ("Harappan urbanism", "Dholavira used reservoirs and a planned settlement hierarchy.", "Standardised weights connected craft and exchange.", "The script remains undeciphered, limiting institutional claims.", "Combine archaeology, ecology and cautious inference.", "ASI reports and standard ancient-history scholarship."),
        ("Buddhist social critique", "Early Buddhist texts questioned ritual status and emphasised conduct.", "The sangha created a rule-bound community but retained social limits.", "Normative equality did not erase hierarchy in wider society.", "Distinguish ethical critique from complete social revolution.", "Canonical texts and repository Ancient History workbooks."),
        ("Temple architecture", "Nagara, Dravida and Vesara are analytical families, not sealed boxes.", "Sites such as Khajuraho, Brihadisvara and Pattadakal show regional adaptation.", "Dynastic labels can obscure guilds, materials and local traditions.", "Use plan, elevation, patronage and ritual function together.", "ASI and Indian Art and Culture repository workbooks."),
        ("Bhakti traditions", "Alvars, Nayanars, Virashaivas and sant poets used vernacular devotion differently.", "Bhakti widened religious expression yet interacted with caste and patriarchy.", "A single egalitarian narrative flattens regional diversity.", "Compare theology, language, institution and social effect.", "Bhakti literature and Medieval History workbooks."),
        ("Colonial land revenue", "Permanent Settlement, Ryotwari and Mahalwari assigned liability differently.", "Revenue pressure linked state extraction to credit and agrarian differentiation.", "Regional outcomes varied with ecology, prices and local power.", "Avoid treating one settlement as the all-India system.", "Modern History repository workbooks."),
        ("Revolt of 1857", "The revolt joined sepoy grievances with displaced rulers and local agrarian anger.", "Its geography and leadership were uneven.", "It was neither only a mutiny nor a uniform national war.", "Use a layered regional explanation.", "1857 proclamations, colonial records and modern-history workbooks."),
        ("Gandhian mass politics", "Champaran, Kheda and Ahmedabad developed methods of investigation and disciplined mobilisation.", "Non-Cooperation and Civil Disobedience widened participation.", "Mobilisation also exposed class, caste and communal tensions.", "Assess method, scale, negotiation and limits.", "Collected works and Modern History workbooks."),
        ("Post-independence integration", "Accession, diplomacy and limited force integrated princely states.", "Linguistic reorganisation later aligned administration with democratic identity.", "Integration did not remove regional inequality or border disputes.", "Read unity as an institutional process, not a single event.", "States Reorganisation Commission and post-independence sources."),
        ("Indian monsoon", "Differential heating, ITCZ movement, cross-equatorial flow and jet streams interact.", "ENSO and Indian Ocean variability influence but do not mechanically determine rainfall.", "Spatial and intra-seasonal variability complicate national averages.", "Link mechanism to forecast uncertainty and adaptation.", "IMD concepts and Geography workbooks."),
        ("Himalayan geomorphology", "Young fold mountains remain tectonically active and erosion-prone.", "Road cutting, drainage disruption and settlement can amplify hazards.", "Hazard does not become disaster without exposure and vulnerability.", "Join geology, land use and risk governance.", "GSI, NDMA and Geography workbooks."),
        ("Ocean currents and fisheries", "Currents redistribute heat and influence upwelling and nutrients.", "The Indian Ocean reverses seasonally under monsoon winds.", "Productivity also depends on oxygen, depth and fishing pressure.", "Connect physical oceanography to livelihoods and regulation.", "INCOIS and Geography workbooks."),
        ("Urbanisation", "Census towns reveal urban transition beyond statutory municipalities.", "Agglomeration can raise productivity through shared labour and infrastructure.", "Congestion, informality and fragmented governance distribute costs unequally.", "Plan metropolitan systems with empowered local institutions.", "Census concepts and Indian Society workbooks."),
        ("Migration and care economy", "Migration diversifies household income and links rural and urban labour markets.", "Women often absorb unpaid care when social services are weak.", "Portability gaps can turn mobility into exclusion.", "Combine labour rights, housing, transport and portable welfare.", "Census, labour and society repository sources."),
        ("Caste in contemporary India", "Constitutional equality coexists with graded social power and unequal assets.", "Political representation can challenge exclusion but also reproduce elite capture.", "Legal prohibition alone cannot transform everyday institutions.", "Use rights, redistribution, dignity and social reform together.", "Articles 15-17 and Indian Society workbooks."),
        ("Communalism", "Communalism converts religious identity into exclusive political interest.", "Rumour, segregation and competitive mobilisation can harden boundaries.", "Secularism cannot mean state indifference to discrimination.", "Use impartial rights protection and inter-group institutions.", "Constitutional provisions and society sources."),
        ("Regionalism", "Federalism provides constitutional channels for territorial claims.", "Linguistic states often stabilised rather than fragmented India.", "Fiscal and identity grievances can intensify when voice is blocked.", "Strengthen cooperative and competitive federalism with accountability.", "States Reorganisation and federalism sources."),
        ("Population ageing", "Longer life expectancy raises the share of older persons.", "Care burdens vary by gender, income and family structure.", "Ageing is not only a pension question; health and accessible cities matter.", "Build community care, geriatric health and income security.", "Population projections and social-justice sources."),
        ("Women and work", "Female labour outcomes reflect care burdens, safety, skills and measurement.", "Self-help groups can widen credit and collective agency.", "Credit without markets or asset rights may not sustain autonomy.", "Combine care infrastructure, mobility, property and decent work.", "PLFS concepts and society/economy workbooks."),
        ("Globalisation and culture", "Media and markets accelerate cultural exchange and standardisation.", "Local actors also hybridise global forms rather than passively receive them.", "Commercial visibility can exclude less profitable traditions.", "Support cultural rights, archives and living livelihoods.", "Culture and society repository sources."),
        ("Climate and society", "Heat, floods and water stress affect groups according to housing, work and assets.", "Informal workers and women often face higher exposure with fewer buffers.", "A hazard-only lens hides social vulnerability.", "Use just adaptation, local data and social protection.", "IPCC concepts, NDMA and society sources."),
    ],
    "GS-II": [
        ("Basic structure", "Kesavananda Bharati limited Parliament's amending power.", "Later cases linked judicial review, federalism and secularism to constitutional identity.", "The doctrine protects continuity but raises counter-majoritarian concerns.", "Use reasoned review and institutional restraint.", "Supreme Court constitutional jurisprudence."),
        ("Parliamentary accountability", "Questions, committees and financial control connect executive power to legislative scrutiny.", "The Public Accounts Committee examines CAG-based expenditure findings.", "Disruption and weak deliberation can reduce effective oversight.", "Strengthen committee time, data and reasoned debate.", "Constitution and parliamentary practice."),
        ("Ordinance power", "Articles 123 and 213 permit temporary law-making when legislatures are not in session.", "D.C. Wadhwa criticised routine re-promulgation.", "Necessity cannot become a parallel legislative route.", "Require transparent reasons and prompt legislative testing.", "Constitution and Supreme Court cases."),
        ("Federal finance", "The Finance Commission recommends tax devolution and grants.", "GST created a shared indirect-tax architecture through the GST Council.", "Vertical and horizontal imbalances persist.", "Improve predictability, consultation and local fiscal capacity.", "Articles 279A and 280."),
        ("Local government", "The 73rd and 74th Amendments constitutionalised elected local bodies.", "Functions remain constrained where funds and functionaries are not devolved.", "Uniform devolution ignores state and urban diversity.", "Use activity mapping, own revenue and accountable staffing.", "Parts IX and IXA."),
        ("Governor's office", "The Governor has constitutional and limited discretionary functions.", "S.R. Bommai constrained misuse of Article 356.", "Partisan delay on bills can disturb federal trust.", "Follow constitutional timelines, reasons and judicially reviewable standards.", "Constitution and Supreme Court jurisprudence."),
        ("Tribunals", "Tribunals seek specialised and faster adjudication.", "L. Chandra Kumar preserved High Court judicial review.", "Executive control over appointments can weaken independence.", "Ensure tenure, transparent selection and appellate coherence.", "Articles 323A-323B and case law."),
        ("Election reform", "The Election Commission supervises elections under Article 324.", "Disclosure judgments improved voter information.", "Money power and opaque political finance remain concerns.", "Combine transparency, enforcement and internal party democracy.", "Constitution, RPA and Supreme Court cases."),
        ("Civil services", "Article 311 provides procedural safeguards while conduct rules impose accountability.", "Mission Karmayogi promotes competency-based capacity building.", "Training cannot substitute for institutional incentives.", "Align postings, appraisal, ethics and citizen outcomes.", "Constitution and governance workbooks."),
        ("Right to information", "RTI operationalises Article 19(1)(a) through a statutory disclosure regime.", "Section 4 supports proactive transparency.", "Backlogs and broad exemptions can weaken access.", "Protect commissions, records management and privacy-sensitive disclosure.", "RTI Act and Supreme Court doctrine."),
        ("Health governance", "Public health spans Union, State and local responsibilities.", "Primary care and surveillance generate positive externalities.", "Fragmented financing can privilege episodic treatment.", "Strengthen public systems, referral networks and accountable purchasing.", "Constitutional entries and health-system sources."),
        ("Education federalism", "The 42nd Amendment moved education to the Concurrent List.", "The RTE Act created statutory elementary-education entitlements.", "Learning, language and digital divides exceed enrolment metrics.", "Join foundational learning, teacher support and inclusion.", "Constitution, RTE and education sources."),
        ("Welfare portability", "One Nation One Ration Card addresses mobility within food security.", "Digital authentication can reduce duplication but also exclude.", "Portability is incomplete without grievance redress and updated records.", "Use offline fallback, audit and interoperable entitlements.", "NFSA and social-justice sources."),
        ("Women's representation", "Reservation in local bodies increased women's descriptive presence.", "Substantive influence depends on capacity, finance and freedom from proxy control.", "Representation alone cannot remove violence or unpaid care.", "Combine seats with institutional support and rights.", "Constitutional amendments and gender sources."),
        ("Judicial pendency", "Vacancies, procedure and government litigation contribute to delay.", "Technology can improve filing and listing.", "Speed without due process can reproduce injustice.", "Use case management, mediation, staffing and reasoned prioritisation.", "Court statistics and justice-reform sources."),
        ("India and neighbourhood", "Connectivity, trade and disaster assistance can create regional public goods.", "Domestic politics in neighbouring states shapes bilateral outcomes.", "Asymmetry can generate mistrust if consultation is weak.", "Use sensitivity, reliable delivery and subregional cooperation.", "MEA and IR workbooks."),
        ("Strategic autonomy", "India works with diverse partners without treaty alignment.", "Issue-based coalitions such as the Quad coexist with BRICS participation.", "Autonomy requires capability, not equidistance.", "Build economic, technological and defence resilience.", "MEA and IR sources."),
        ("UN reform", "The UN Security Council reflects the power distribution of 1945.", "India argues that legitimacy requires broader developing-country representation.", "Charter amendment faces incumbent veto politics.", "Use coalition-building and incremental institutional reform.", "UN Charter and MEA statements."),
        ("Diaspora policy", "The diaspora contributes skills, remittances and networks.", "Consular protection is constrained by host-state law and dual loyalties.", "Celebratory narratives can ignore vulnerable migrant workers.", "Differentiate engagement by migrant category and rights risk.", "MEA and migration sources."),
        ("Digital rights", "Privacy was recognised as a fundamental right in Puttaswamy.", "Digital public infrastructure can expand service access.", "Data concentration and exclusion create proportionality concerns.", "Use purpose limitation, safeguards, audits and accessible alternatives.", "Supreme Court privacy doctrine and governance sources."),
    ],
    "GS-III": [
        ("Growth and employment", "GDP growth can coexist with weak labour absorption.", "MSMEs and construction have high employment linkages.", "Informality and low productivity reduce job quality.", "Support labour-intensive production, skills and social security.", "National accounts and labour-economy sources."),
        ("Inflation management", "Food and fuel shocks transmit differently from demand inflation.", "Monetary policy targets headline CPI under the flexible framework.", "Interest rates cannot produce vegetables or repair supply chains.", "Coordinate monetary credibility with storage, logistics and competition.", "RBI framework and Economy workbooks."),
        ("Fiscal quality", "Capital expenditure can crowd in private activity when projects are viable.", "Revenue spending includes productive health and education.", "A capex label does not guarantee value for money.", "Use transparent appraisal, maintenance and outcome budgeting.", "Budget concepts and CAG principles."),
        ("Agricultural markets", "MSP provides a price signal but procurement is concentrated by crop and region.", "FPOs can aggregate produce and bargaining power.", "Market reform without infrastructure can expose small farmers.", "Invest in storage, grading, competition and risk management.", "Agriculture and Economy workbooks."),
        ("Food security", "NFSA creates subsidised grain entitlements.", "Buffer stocks support availability and price stabilisation.", "Cereal security alone does not ensure nutritional adequacy.", "Diversify diets, strengthen ICDS and reduce exclusion.", "NFSA and nutrition sources."),
        ("Manufacturing strategy", "Infrastructure, scale and supply-chain depth shape competitiveness.", "PLI links incentives to incremental production in selected sectors.", "Subsidies may create assembly without domestic value addition.", "Tie support to learning, R&D, competition and sunset review.", "Industrial-policy workbooks."),
        ("Energy transition", "Renewables reduce operational emissions but require grids, storage and minerals.", "Coal-dependent regions face employment and fiscal exposure.", "A capacity target is not identical to reliable clean supply.", "Plan a just transition with transmission and recycling.", "Energy and environment sources."),
        ("Urban infrastructure", "Public transport and compact land use can reduce congestion externalities.", "Municipal finance remains constrained.", "Megaprojects can displace vulnerable groups.", "Use metropolitan planning, value capture and participatory safeguards.", "Urban and infrastructure sources."),
        ("Banking stability", "Capital, provisioning and supervision absorb credit risk.", "The Insolvency and Bankruptcy Code created a time-bound resolution framework.", "Evergreening can hide stress.", "Strengthen governance, early recognition and resolution capacity.", "RBI, Basel and Economy sources."),
        ("External sector", "The current account records trade and income flows.", "Exchange-rate flexibility can absorb shocks.", "Reserve accumulation has costs and cannot replace competitiveness.", "Diversify exports, manage liabilities and deepen hedging.", "Balance-of-payments sources."),
        ("AI governance", "AI can improve prediction and service targeting.", "Biased data and opaque models can scale discrimination.", "Innovation and rights are not zero-sum if risk is classified.", "Use testing, human review, transparency and liability.", "Science-tech and ethics sources."),
        ("Semiconductor ecosystem", "Fabrication needs capital, power, water, design and supplier depth.", "Packaging and design offer different entry points.", "A fabrication subsidy alone cannot create an ecosystem.", "Build skills, trusted supply chains and long-term R&D.", "Science-tech and manufacturing sources."),
        ("Space economy", "Remote sensing and navigation create public and commercial applications.", "Private participation can widen innovation.", "Orbital debris and spectrum are shared-resource concerns.", "Use authorisation, liability and space-situational awareness.", "ISRO and space-policy sources."),
        ("Biotechnology", "Gene editing can improve crops and therapies.", "Off-target effects and ecological spread require risk assessment.", "The same tool has different risk profiles by use.", "Apply case-specific biosafety, consent and monitoring.", "Biotechnology workbooks."),
        ("Cybersecurity", "Critical infrastructure depends on interconnected digital systems.", "CERT-In supports incident response.", "Centralised controls can create surveillance or single-point risks.", "Adopt zero trust, redundancy, reporting and rights safeguards.", "IT Act concepts and security sources."),
        ("Border management", "Terrain, communities and trade shape border security.", "Technology improves awareness but cannot replace local intelligence.", "Over-securitisation can disrupt livelihoods.", "Integrate infrastructure, development and coordinated agencies.", "Internal Security workbooks."),
        ("Money laundering", "Layering disguises proceeds through complex transactions.", "FATF standards promote risk-based controls.", "Compliance burdens can exclude legitimate small actors.", "Improve beneficial-ownership data and targeted enforcement.", "PMLA and security sources."),
        ("Disaster risk reduction", "Risk combines hazard, exposure, vulnerability and capacity.", "Early warnings save lives only when communication and evacuation work.", "Relief-centric policy neglects prevention.", "Mainstream resilient infrastructure and local preparedness.", "DM Act, Sendai and NDMA sources."),
        ("Climate adaptation", "Heat action plans and resilient crops address observed risks.", "Adaptation benefits are locally specific.", "Poorly designed projects can shift risk to other groups.", "Use climate services, local finance and equity tests.", "IPCC and climate-policy sources."),
        ("Blue economy", "Fisheries, shipping and offshore energy share marine space.", "Healthy ecosystems underpin long-term productivity.", "Growth without carrying-capacity limits can damage coasts.", "Use marine spatial planning and community rights.", "Coastal and economy sources."),
    ],
    "GS-IV": [
        ("Ethics and law", "Legality sets a minimum while ethics evaluates purpose, fairness and consequences.", "Civil servants exercise discretion within rules.", "Personal morality cannot override constitutional duty.", "Use legality, public reason and recorded justification.", "Ethics and Human Interface sources."),
        ("Attitude and behaviour", "Attitudes include cognitive, affective and behavioural components.", "Institutional cues can alter conduct.", "Awareness campaigns alone may not overcome incentives.", "Combine persuasion, defaults and accountable rules.", "Attitude workbooks."),
        ("Emotional intelligence", "Self-awareness and regulation improve judgement under pressure.", "Empathy supports communication but not favouritism.", "Emotional control must not become moral indifference.", "Join empathy with evidence and duty.", "EI and public-service sources."),
        ("Integrity", "Integrity aligns values, words and action across situations.", "Asset disclosure and audit support but do not create character.", "Rigid consistency can preserve a mistaken decision.", "Pair integrity with reflection and correction.", "Probity sources."),
        ("Impartiality", "Impartiality rejects irrelevant bias.", "Equity may require different support for unequal circumstances.", "Treating unlike cases identically can reproduce injustice.", "Use relevant criteria and transparent reasons.", "Public-service values sources."),
        ("Objectivity", "Objectivity requires evidence and reasons open to scrutiny.", "Data can still encode biased categories.", "Quantification is not value-neutral by itself.", "Audit assumptions and permit appeal.", "Foundational values and AI ethics sources."),
        ("Accountability", "Answerability requires explanation; enforcement supplies consequences.", "Social audit adds citizen verification.", "Fear-based accountability can suppress initiative.", "Use proportionate review and learning systems.", "Governance and probity sources."),
        ("Compassion", "Compassion recognises suffering and motivates appropriate help.", "Rights-based welfare avoids discretionary charity.", "Compassion without rules can become patronage.", "Institutionalise humane and equal service.", "Ethics sources."),
        ("Courage of conviction", "Moral courage accepts personal cost for defensible public values.", "Whistle-blower protection reduces retaliation risk.", "Certainty without evidence can become obstinacy.", "Test conviction through law, facts and consultation.", "Ethics and vigilance sources."),
        ("Conflict of interest", "A conflict exists when private interests can improperly influence duty.", "Disclosure and recusal protect trust.", "Actual corruption need not be proved before mitigation.", "Manage appearance and risk proactively.", "Probity and conduct-rule sources."),
        ("Procurement case", "Competitive procurement protects value and equal opportunity.", "Emergency exceptions may be necessary but must be recorded.", "Delay can also cause public harm.", "Use limited exception, audit trail and post-review.", "Public-funds and corruption sources."),
        ("Welfare exclusion case", "Authentication errors can deny lawful benefits.", "Frontline discretion can restore access but create inconsistency.", "Technology is a means, not the legal entitlement.", "Provide offline fallback, receipts and rapid appeal.", "Digital governance and ethics sources."),
        ("Communal tension case", "Rumours can trigger immediate harm.", "Restrictions affect liberty and livelihood.", "Neutrality does not mean passivity before targeted violence.", "Use proportionate prevention, verified communication and review.", "Public order and ethics sources."),
        ("Environmental clearance case", "Projects create jobs and ecological externalities.", "Consultation supplies local knowledge and legitimacy.", "Delay or capture can undermine both development and rights.", "Use independent appraisal, disclosure and enforceable mitigation.", "Environmental ethics sources."),
        ("Whistle-blower case", "Internal evidence may reveal serious wrongdoing.", "Confidential channels protect due process and the reporter.", "Public disclosure can prejudice investigation.", "Escalate through protected channels, preserve evidence and disclose only when necessary.", "Vigilance and ethics sources."),
        ("Police discretion case", "Public order powers must satisfy legality and proportionality.", "Marginalised groups face unequal enforcement risks.", "Mechanical rule application can worsen conflict.", "Record reasons, use minimum force and enable review.", "Ethics and policing principles."),
        ("Health triage case", "Scarce resources require clinically relevant criteria.", "Social worth is an unethical allocation rule.", "First-come systems can favour access rather than need.", "Use transparent triage, reassessment and communication.", "Medical ethics principles."),
        ("Data privacy case", "Administrative data can improve targeting.", "Purpose expansion without consent or law threatens autonomy.", "Anonymisation may be reversible.", "Minimise data, separate purposes and audit access.", "Privacy and technology ethics."),
        ("Political pressure case", "Civil servants owe loyalty to the Constitution and lawful government.", "Oral directions can obscure responsibility.", "Open defiance may disrupt legitimate administration.", "Seek written orders, give reasoned advice and use formal escalation.", "Conduct rules and civil-service ethics."),
        ("Disaster relief case", "Urgency justifies simplified procedure, not unrecorded favouritism.", "Local participation improves need identification.", "Equal quantities may ignore differential vulnerability.", "Use transparent criteria, public lists and later audit.", "Disaster and humanitarian ethics."),
    ],
}


ETHICS_QUOTATIONS = [
    ("The means may be judged only in relation to the end.", "Deontology, consequentialism and virtue ethics disagree on whether good outcomes can justify wrongful means.", "Public action needs both legitimate purpose and defensible procedure.", "A rigid rule can ignore emergency consequences, while pure consequentialism can sacrifice rights."),
    ("Integrity is doing the right thing when no one is watching.", "Integrity joins consistency, honesty and fidelity to public purpose.", "Audit supports integrity but cannot replace character and reasoned judgement.", "Blind consistency can preserve an error; integrity also requires correction."),
    ("Compassion without competence can become another form of harm.", "Compassion notices suffering, while competence identifies an effective and lawful response.", "Rights-based delivery converts humane concern into equal treatment.", "Sentiment alone may produce favouritism or ineffective relief."),
    ("Power tests character more reliably than adversity.", "Discretion reveals whether authority is treated as trust, entitlement or licence.", "Reason-giving, disclosure and review constrain self-serving use of office.", "Formal controls cannot anticipate every abuse of informal influence."),
    ("Objectivity requires reasons, not the absence of values.", "Objectivity asks whether evidence and criteria can be publicly scrutinised.", "Constitutional values properly guide relevance and fairness.", "Data may encode bias, so quantification is not automatically neutral."),
    ("Courage is not fearlessness but action despite justified fear.", "Moral courage accepts personal cost to protect a defensible public value.", "Whistle-blower channels reduce retaliation and preserve evidence.", "Unexamined certainty can become recklessness or obstinacy."),
    ("Accountability without discretion produces paralysis; discretion without accountability produces abuse.", "Administration needs room to adapt rules to facts and a duty to explain that adaptation.", "Recorded reasons connect innovation with review.", "Fear-based controls can suppress initiative, but secrecy destroys trust."),
    ("Equality of treatment may reproduce inequality of circumstance.", "Formal equality applies the same rule; substantive equality asks whether relevant disadvantage warrants accommodation.", "Reservation, disability access and targeted support illustrate the distinction.", "Differentiation must rest on relevant and reviewable criteria."),
    ("Neutrality is not indifference to injustice.", "Political impartiality bars partisan preference but does not permit passivity before rights violations.", "Constitutional duty requires even-handed protection and reasoned enforcement.", "Activism without legal restraint may itself become arbitrary."),
    ("Transparency is a means to accountability, not a substitute for it.", "Information enables scrutiny, but correction also needs answerability and consequences.", "RTI, social audit and reasoned orders connect disclosure to action.", "Indiscriminate disclosure can violate privacy or impair legitimate confidentiality."),
    ("Public trust is accumulated slowly and spent quickly.", "Trust grows from competence, fairness, predictability and truthful communication.", "A single concealed conflict or manipulated record can alter how later actions are interpreted.", "Trust should not become an excuse to avoid verification."),
    ("A code can guide conduct but cannot manufacture conscience.", "Codes clarify expected behaviour and sanctions; conscience supplies internal moral motivation.", "Training, leadership and institutional incentives shape whether written norms live in practice.", "Private conscience cannot override constitutional law."),
    ("Empathy enlarges information; it does not decide the case by itself.", "Perspective-taking reveals burdens that aggregate data may hide.", "Decision-makers must still use law, evidence and proportionality.", "Empathy can become partiality if detached from equal criteria."),
    ("Probity begins where mere compliance ends.", "Compliance asks whether a rule was followed; probity also tests purpose, conflict, economy and public trust.", "Procurement may be formally valid yet ethically compromised by tailored specifications.", "Probity cannot authorise officials to invent obligations outside law."),
    ("The ethical cost of delay is often invisible in the file.", "Administrative delay shifts risk and expense onto citizens who may lack voice.", "Time limits, receipts and escalation make the burden visible.", "Speed cannot justify denial of hearing or factual verification."),
    ("Technology scales both competence and prejudice.", "Digital systems can improve consistency and access while reproducing biased data or exclusion.", "Human review, audit trails and fallback channels are ethical safeguards.", "Rejecting all technology would also forgo public benefits."),
    ("Whistle-blowing is loyalty to public purpose, not disloyalty to an organisation.", "The relevant loyalty is to law, safety and institutional mission rather than concealment.", "Protected internal escalation should normally precede public disclosure.", "Disclosure can still prejudice privacy or investigation if evidence is mishandled."),
    ("Civil service anonymity cannot mean moral invisibility.", "Anonymity protects non-partisan administration, not freedom from responsibility.", "Written advice and recorded dissent preserve both hierarchy and accountability.", "Public campaigning by officials can compromise neutrality."),
    ("Justice must be seen to be done because procedure communicates equal respect.", "Hearing, reasons and absence of conflict make authority intelligible to those affected.", "Fair procedure can preserve legitimacy even when outcomes disappoint.", "Procedure alone cannot redeem a substantively discriminatory rule."),
    ("Sustainable development is an ethical claim about absent voices.", "Future persons and non-human life cannot bargain in present markets.", "Precaution, polluter-pays and intergenerational equity represent their interests.", "Precaution must be proportionate to evidence and reversible risk."),
]


ETHICS_CASES = [
    ("emergency procurement", "A district hospital faces an oxygen shortage after floods. One supplier can deliver immediately but is owned by the minister's relative; two compliant suppliers need forty-eight hours.", "patients needing oxygen, hospital staff, competing suppliers, the minister, taxpayers", "save life immediately while preventing favouritism and preserving an audit trail", "Use a documented emergency exception, independent rate comparison, conflict disclosure, split orders where feasible and post-facto audit."),
    ("welfare authentication", "A biometric system rejects elderly pensioners whose fingerprints fail. The treasury warns that manual approval may increase fraud.", "elderly claimants, frontline staff, treasury, technology vendor, taxpayers", "protect lawful entitlement without abandoning verification", "Provide offline identity alternatives, dated receipts, time-bound review and sample-based fraud audit."),
    ("communal rumour", "A false video is spreading during a festival. A blanket internet shutdown may slow violence but will also disrupt hospitals, payments and examination communication.", "targeted communities, general public, police, hospitals, businesses, platform operators", "prevent imminent harm through the least restrictive effective measure", "Use verified public communication, targeted takedown and policing, narrow geographic limits, recorded necessity and frequent review."),
    ("environmental clearance", "A mining project promises jobs in a poor district but the public hearing omitted a downstream tribal settlement likely to lose a sacred grove and water source.", "tribal residents, workers, company, local government, future generations", "correct procedural exclusion and assess irreversible ecological loss", "Reopen consultation, commission independent cumulative assessment, disclose alternatives and require enforceable mitigation or reject the site."),
    ("whistle-blower evidence", "An engineer finds test reports altered for a bridge nearing inauguration. Her superior orders silence until after the ceremony, claiming disclosure may cause panic.", "bridge users, engineer, department, contractor, political executive", "protect life, evidence and due process despite retaliation risk", "Secure records, seek written orders, trigger protected technical review, halt unsafe opening and escalate to vigilance if suppressed."),
    ("police protest", "A peaceful protest blocks an ambulance route. Senior officers demand immediate dispersal, while organisers offer to open one corridor if negotiations continue.", "patients, protesters, police, commuters, local administration", "restore essential access while preserving speech and assembly", "Negotiate a corridor, communicate lawful conditions, document graduated response and use minimum proportionate force only if necessary."),
    ("medical triage", "After an industrial accident, an ICU has one bed. A politically connected patient arrived first, while a younger worker arriving later has a substantially better clinical prognosis.", "both patients, families, medical team, hospital, public", "allocate scarce care by transparent clinical criteria rather than status", "Apply an approved triage protocol, independent second opinion, reassessment and communication; provide the other patient best available care."),
    ("data sharing", "A health department wants to share identifiable disease records with private insurers to predict future costs, although patients consented only to treatment and surveillance.", "patients, health department, insurers, researchers, public-health planners", "preserve purpose limitation while enabling legitimate public-health analysis", "Reject insurer transfer without lawful basis; use minimised, de-identified data under access controls for defined public purposes."),
    ("oral political order", "A minister orally asks a secretary to accelerate a land allotment for a favoured firm, saying investment will otherwise move to another state.", "competing firms, landholders, minister, department, public exchequer", "support investment without bypassing equal procedure", "Give reasoned advice, seek written direction, apply published criteria and refer unresolved illegality through formal channels."),
    ("relief distribution", "Flood relief stocks are insufficient. Equal village quotas ignore that one hamlet has lost every house while another retains road access and private supplies.", "affected households, village leaders, relief workers, donors, administration", "allocate by transparent vulnerability and need rather than political equality", "Publish criteria, verify damage with community participation, reserve for high-risk groups and disclose beneficiary lists."),
    ("exam leak", "Hours before a recruitment examination, credible evidence suggests one coaching centre obtained the paper. Cancellation harms honest candidates and delays staffing.", "candidates, commission, departments, accused centre, public", "protect merit and evidentiary integrity while minimising avoidable harm", "Seal evidence, isolate compromised centres if defensible, use an independent technical inquiry, communicate reasons and provide a prompt re-test where integrity cannot be secured."),
    ("research ethics", "A public laboratory discovers that a senior scientist omitted adverse trial results from a report supporting rapid approval of a low-cost vaccine.", "trial participants, patients, scientist, regulator, laboratory, public", "protect safety and scientific integrity without suppressing a potentially useful product", "Restore complete data, notify the ethics committee and regulator, pause approval, investigate responsibility and permit reconsideration after transparent review."),
    ("school nutrition", "A district can serve a cheaper fortified meal that meets calorie rules, but local evidence shows children reject its taste and waste most of it.", "children, parents, cooks, suppliers, education department", "distinguish formal compliance from effective nutrition and dignity", "Pilot acceptable menus, involve school committees, measure consumption rather than dispatch and preserve nutritional standards."),
    ("forest eviction", "Officials find families cultivating inside a protected forest. Eviction orders are ready, but community claims under forest-rights law remain undecided.", "forest dwellers, wildlife, forest department, Gram Sabha, courts", "protect ecology without prejudging pending legal rights", "Stay coercive eviction, complete claims transparently, prevent new encroachment and co-design conservation duties after rights determination."),
    ("algorithmic policing", "A predictive-policing tool directs patrols repeatedly to poor neighbourhoods because historical arrest data are concentrated there.", "residents, police, victims, vendor, oversight bodies", "reduce crime without converting historical enforcement bias into automated suspicion", "Audit variables and outcomes, restrict high-stakes use, require human reasons, publish safeguards and create complaint review."),
    ("municipal demolition", "An unsafe informal settlement sits beside a drain before monsoon. Immediate demolition reduces flood obstruction but residents received no notice or relocation option.", "residents, downstream communities, municipality, courts, children and elderly", "reduce imminent risk while respecting housing, hearing and proportionality", "Issue verified risk notice, provide temporary shelter and transport, sequence removal by hazard, hear objections and plan rehabilitation."),
    ("media briefing", "During a sensitive investigation, the public demands information. Releasing names may reassure citizens but could prejudice trial and endanger witnesses.", "accused persons, victims, witnesses, media, investigators, public", "communicate verified facts without compromising presumption of innocence or safety", "Use an authorised spokesperson, release process facts and safety advice, withhold identities and correct misinformation promptly."),
    ("tax settlement", "A large employer offers immediate payment of most disputed tax if penalties are waived privately; officials argue the jobs are too important to risk.", "taxpayers, workers, firm, revenue department, competitors", "recover revenue through lawful, equal and reviewable settlement", "Use the statutory settlement route, disclose criteria, record valuation and reject private concessions unavailable to similarly placed firms."),
    ("public fund utilisation", "Year-end funds remain unspent. A department can rush low-priority purchases to avoid a reduced allocation next year.", "citizens, department, vendors, legislature, audit institutions", "resist use-it-or-lose-it incentives and protect value for money", "Return or revalidate funds, document genuine commitments, improve forecasting and evaluate managers on outcomes rather than exhaustion of grants."),
    ("conflict of interest", "An officer on a procurement committee owns shares through a mutual fund heavily exposed to one bidder, though she cannot direct the fund.", "officer, bidders, committee, investors, public", "manage actual and perceived conflict proportionately", "Disclose the holding, obtain an ethics opinion, recuse if exposure is material or confidence would reasonably suffer, and record the decision."),
    ("disaster volunteers", "Volunteers publish photographs of rescued children to attract donations. The images increase support but reveal identities and distress.", "children, families, volunteers, donors, media, relief agencies", "mobilise support without exploiting dignity or privacy", "Obtain guardian consent where appropriate, anonymise images, prohibit sensational content and publish audited needs and spending instead."),
    ("transfer retaliation", "An officer who stops illegal sand mining is transferred under a general reshuffle order. Challenging it may look self-serving, but silence may demoralise the team.", "officer, team, government, miners, local communities", "defend institutional integrity without claiming a personal right to a post", "Create a factual handover, preserve evidence, use service channels to seek reasons and ensure investigations continue regardless of transfer."),
    ("charity selection", "A district official is asked to nominate beneficiaries for a private scholarship. The donor wants only high scorers; the poorest students have weaker marks.", "students, donor, schools, families, district administration", "respect donor purpose while preventing public endorsement of arbitrary exclusion", "Negotiate a transparent composite criterion combining merit and disadvantage, separate public certification from private preference and publish selection rules."),
    ("facial recognition", "Police propose live facial recognition at a crowded pilgrimage after a missing-child incident, but accuracy is lower for some demographic groups.", "children, pilgrims, police, minorities, technology vendor", "improve safety without indiscriminate or biased surveillance", "Limit purpose and duration, test accuracy, require human confirmation, secure data deletion and provide independent oversight."),
    ("hospital gifts", "A medical-equipment company offers expensive conference travel to doctors who influence procurement, calling it professional education.", "patients, doctors, hospital, company, competitors", "separate legitimate learning from inducement and preserve clinical trust", "Require institutional sponsorship rules, disclose funding, exclude beneficiaries from procurement and prefer independent continuing education."),
    ("drought water allocation", "A drought board must choose between drinking water, an employment-intensive sugar mill and irrigation for standing food crops.", "households, workers, farmers, industry, ecosystems", "rank essential need while reducing irreversible livelihood loss", "Prioritise drinking water, publish a basin balance, impose industrial efficiency and temporary limits, protect critical crop stages and compensate verified losses."),
    ("census confidentiality", "Local officials seek household-level census data to identify undocumented migrants, promising better targeting.", "households, enumerators, migrants, security agencies, planners", "protect statistical trust and lawful confidentiality while addressing legitimate administration separately", "Refuse repurposing where barred, use aggregated planning data and require agencies to rely on their own lawful processes."),
    ("inspection bribe", "A small factory offers a payment after an inspector identifies a remediable safety defect; closure will temporarily remove fifty jobs.", "workers, owner, inspector, nearby residents, regulator", "protect safety and livelihood without accepting corruption", "Reject and report the bribe, issue a proportionate time-bound compliance order, verify correction and close only if imminent risk persists."),
    ("heritage development", "A road widening project will remove an old neighbourhood shrine not formally protected but central to local memory.", "residents, commuters, religious groups, heritage experts, municipality", "balance mobility, equal treatment and cultural attachment", "Assess alternatives, consult transparently, document heritage value and use relocation only with consent and lawful safeguards."),
    ("AI welfare scoring", "A state ranks welfare applicants using opaque credit and phone-use data supplied by a vendor.", "applicants, state, vendor, taxpayers, excluded households", "ensure relevance, explainability and appeal in an entitlement decision", "Suspend adverse automated decisions, disclose criteria, test bias, minimise data and provide human review."),
    ("prison overcrowding", "A jail superintendent can reduce crowding by releasing eligible undertrial prisoners on administrative facilitation, but local police oppose it.", "undertrials, victims, police, courts, prison staff", "respect liberty and judicial authority while managing safety", "Identify legally eligible cases, coordinate legal aid and courts, assess risk individually and document compliance rather than order unilateral release."),
    ("pandemic communication", "Officials fear that disclosing uncertainty about a disease model will reduce compliance.", "citizens, health workers, scientists, government, vulnerable groups", "communicate uncertainty without creating false confidence or panic", "State what is known, unknown and changing; publish assumptions, update regularly and explain precautionary action."),
    ("NGO partnership", "A reputable NGO can deliver shelters quickly but its board includes a serving official's spouse.", "homeless citizens, NGO, official, competitors, donors", "use capable partners while controlling conflict and equal opportunity", "Disclose the relationship, remove the official from selection, use objective emergency criteria and audit performance."),
    ("language access", "A benefits portal is available only in English although many eligible citizens use regional languages.", "applicants, administrators, technology teams, linguistic minorities", "make equal entitlement practically accessible", "Add multilingual and assisted channels, test comprehension and retain offline application without diluting eligibility rules."),
    ("custodial force", "An accused person refuses to reveal where a kidnapped child is held. Officers propose illegal coercion because time is running out.", "child, accused, police, family, justice system", "pursue urgent rescue without torture or unreliable confession", "Use lawful interrogation, digital and location evidence, supervisory command and rapid judicial tools; prohibit coercion."),
    ("corporate pollution disclosure", "A public-sector company wants to delay disclosure of an accidental toxic release until measurements are complete.", "nearby residents, workers, company, regulator, investors", "warn exposed people promptly while preserving factual accuracy", "Issue immediate precautionary information, disclose uncertainty, begin independent monitoring and update results transparently."),
    ("ration diversion", "A dealer diverts grain but villagers fear retaliation if they complain individually.", "beneficiaries, dealer, officials, community organisations, taxpayers", "create safe collective accountability and restore entitlement", "Use social audit, anonymous complaint, stock reconciliation, protection against retaliation and temporary alternate distribution."),
    ("public apology", "A department's erroneous notice stigmatised a minority community. Lawyers advise silence to reduce litigation.", "community, department, officials, courts, wider public", "restore dignity and trust without prejudging legal liability", "Correct the record promptly, apologise for verified error, preserve legal process and review how the notice was approved."),
    ("autonomous vehicle pilot", "A city can reduce accidents by piloting autonomous buses, but responsibility for software failure is unclear.", "passengers, drivers, city, vendor, insurers", "permit innovation only with clear safety and liability architecture", "Use a limited monitored pilot, independent certification, human override, incident disclosure and contractual liability."),
    ("archive access", "Researchers request colonial intelligence files containing names of living families.", "researchers, families, archive, public, historians", "balance historical transparency with privacy and possible harm", "Apply time-bound archival rules, redact sensitive identifiers, provide reasons and permit review."),
]


def ethics_theory_answer(record: tuple[str, str, str, str], marks: int) -> str:
    quotation, concept, application, limit = record
    sentences = [
        f"'{quotation}' frames a precise ethical issue: {concept[0].lower() + concept[1:]}",
        f"In public service, '{quotation}' becomes practical because {application[0].lower() + application[1:]}",
        f"An official must identify the duty under '{quotation}', name the persons bearing its risks, and record reasons specific to {concept.lower()}",
        f"The counter-risk internal to '{quotation}' is that {limit[0].lower() + limit[1:]}",
        f"A sound use of {concept.lower()} joins the motive behind '{quotation}' with lawful means, relevant evidence and proportionate action.",
        f"The qualified conclusion is that '{quotation}' supplies a disciplined test for {application.lower()}, but remains bounded by {limit.lower()}",
    ]
    return fit_sentences(sentences, 95 if marks == 10 else 155, 148 if marks == 10 else 235)


def ethics_case_answer(case: tuple[str, str, str, str, str], marks: int) -> str:
    title, scenario, stakeholders, dilemma, response = case
    sentences = [
        f"The central dilemma in this {title} case is to {dilemma}.",
        f"The material setting is specific: {scenario}",
        f"In {title}, the stakeholders - {stakeholders} - bear different risks; legality and non-arbitrariness must answer those {title} differences.",
        f"Because the aim is to {dilemma}, speed in {title} cannot excuse {title} conflicts, avoidable harm or unreviewable reasons.",
        f"The preferred {title} course is specific: {response}",
        f"The record for {title} should connect '{response}' to verified {title} facts, rejected alternatives and a dated review point.",
        f"Communication about {title} must tell {stakeholders} what the {title} authority will do, by when and through which {title} appeal.",
        f"The strongest objection is that {response} may impose delay or administrative cost; in this {title} setting, that cost is justified by the need to {dilemma}.",
        f"Review of the {title} decision should measure whether it actually {dilemma}, rather than merely whether the file was closed quickly.",
    ]
    minimum, maximum = (180, 242) if marks == 15 else (95, 148)
    chosen: list[str] = []
    for sentence in sentences:
        if words(" ".join(chosen + [sentence])) <= maximum:
            chosen.append(sentence)
        if words(" ".join(chosen)) >= minimum:
            break
    answer = " ".join(chosen)
    if words(answer) < minimum:
        raise ValueError(f"Ethics case answer too short: {title}")
    return answer


def build_ethics_paper(set_no: int) -> dict[str, Any]:
    theory_start = (set_no - 1) * 5
    case_start = (set_no - 1) * 10
    theory = ETHICS_QUOTATIONS[theory_start:theory_start + 5]
    cases = ETHICS_CASES[case_start:case_start + 10]
    questions = []
    for index in range(1, 11):
        marks = 10
        if index <= 5:
            record = theory[index - 1]
            question = (
                f"Explain the ethical significance of the statement: \"{record[0]}\" "
                "Illustrate its application and one limitation. (Answer in 150 words.)"
            )
            answer = ethics_theory_answer(record, marks)
            kind = "quotation"
        else:
            record = theory[index - 6]
            question = (
                f"Application question: {record[2]} Explain how this ethical principle should guide "
                f"a civil servant while avoiding the limitation that {record[3].lower()} "
                "(Answer in 150 words.)"
            )
            answer = ethics_theory_answer(
                (record[0], record[2], record[1], record[3]), marks
            )
            kind = "application"
        questions.append({
            "no": index, "text": plain(question), "marks": marks, "word_limit": 150,
            "answer": answer,
            "source": "upsc-ai-kit/knowledge/Ethics/basic and curated case bank",
            "subject": "Ethics", "topic_id": f"ethics-{kind}-{set_no}-{index}",
            "difficulty": "above-typical recent UPSC",
            "difficulty_features": [
                "question-specific demand", "named evidence", "analysis",
                "qualification", "source-grounded conclusion",
            ],
            "ethics_format": kind,
        })
    for local, case in enumerate(cases, 11):
        question = (
            f"Case study: {case[1]} Analyse the stakeholders and competing values, evaluate the "
            "available options, and justify a course of action with procedural safeguards. "
            "(Answer in 250 words.)"
        )
        questions.append({
            "no": local, "text": plain(question), "marks": 15, "word_limit": 250,
            "answer": ethics_case_answer(case, 15),
            "source": "upsc-ai-kit/knowledge/Ethics/basic and curated case bank",
            "subject": "Ethics", "topic_id": f"ethics-case-{set_no}-{local}",
            "difficulty": "above-typical recent UPSC",
            "difficulty_features": [
                "question-specific demand", "named evidence", "analysis",
                "qualification", "source-grounded conclusion",
            ],
            "ethics_format": "case-study",
        })
    return {
        "kind": "mains", "paper": "GS-IV",
        "title": "UPSC Civil Services (Main) Simulation GS-IV",
        "time": "3 Hours", "max_marks": 250, "questions": questions,
        "instructions": [
            "There are TWENTY questions. All questions are compulsory.",
            "Questions 1-10 carry 10 marks each and should be answered in 150 words.",
            "Questions 11-20 are substantial case studies carrying 15 marks each and should be answered in 250 words.",
            "Credit is given for ethical reasoning, stakeholder analysis, feasible options and justified safeguards.",
        ],
    }


DIRECTIVES = [
    ("Examine", "institutional design and practical outcomes"),
    ("Discuss", "continuities, changes and competing interpretations"),
    ("Analyse", "causal mechanisms, distributional effects and limitations"),
    ("Critically evaluate", "achievements, objections and a qualified judgement"),
]


GS_SOURCE_SUBJECTS = {
    "GS-I": [
        "Modern-History", "Indian-Art-and-Culture", "Geography",
        "Indian-Society", "World-History",
    ],
    "GS-II": ["Polity", "Governance", "Social-Justice", "International-Relations"],
    "GS-III": [
        "Economy", "Environment-and-Ecology", "Science-and-Technology",
        "Internal-Security", "Disaster-Management",
    ],
}

GS_SELECTION_ORDER = {
    "GS-I": [
        "Geography-Physical", "Geography-Physical", "Geography-Human-Economic",
        "Indian-Society", "Indian-Society",
        "Modern-History-Early", "Modern-History-Gandhian",
        "Modern-History-Post-Independence",
        "Indian-Art-and-Culture",
        "World-History",
    ],
    "GS-II": ["Polity", "Governance", "Social-Justice", "International-Relations"],
    "GS-III": [
        "Economy-Macro", "Agriculture", "Infrastructure-Energy",
        "Industry-Inclusive-Growth", "Public-Finance",
        "Environment-and-Ecology", "Science-and-Technology",
        "Internal-Security", "Disaster-Management",
    ],
}


def gs3_economy_category(source: str) -> str:
    match = re.search(r"/(\d{2})-", source)
    topic = int(match.group(1)) if match else 0
    if topic in {*range(11, 16), *range(27, 31)}:
        return "Agriculture"
    if topic in {18, 31}:
        return "Infrastructure-Energy"
    if topic in {9, 10}:
        return "Public-Finance"
    if topic in {2, 16, 17, 22, 23}:
        return "Industry-Inclusive-Growth"
    return "Economy-Macro"


def gs1_category(subject: str, source: str) -> str:
    if subject == "Geography":
        return (
            "Geography-Human-Economic"
            if "Part-B-" in source
            else "Geography-Physical"
        )
    if subject == "Modern-History":
        match = re.search(r"/(\d{2})-", source)
        topic = int(match.group(1)) if match else 0
        if topic >= 28:
            return "Modern-History-Post-Independence"
        if topic >= 19:
            return "Modern-History-Gandhian"
        return "Modern-History-Early"
    return subject


ORIGINAL_MAINS_HEAD_RE = re.compile(
    r"(?im)^#{3,5}\s+.*(?:ORIGINAL MAINS|Original (?:10|15|20)-marker|"
    r"Original Mains Practice).*$"
)
MARKED_MAINS_HEAD_RE = re.compile(
    r"(?im)^#{3,5}\s+(?:Question\s+)?(10|15|20)\s+marks?\s*[-—:]\s*.+$"
)


def parse_original_mains(path: Path, source_subject: str | None = None) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    heads = sorted(
        list(ORIGINAL_MAINS_HEAD_RE.finditer(text))
        + list(MARKED_MAINS_HEAD_RE.finditer(text)),
        key=lambda match: match.start(),
    )
    records: list[dict[str, Any]] = []
    for index, head in enumerate(heads):
        marks_match = re.search(
            r"(?i)\b(10|15|20)\s*(?:MARKS?|marks?|-marker|marker)",
            head.group(0),
        )
        if not marks_match:
            continue
        marks = int(marks_match.group(1))
        if marks not in (10, 15):
            continue
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        block = text[head.end():end]
        question_match = re.search(
            r"(?ims)^\*\*Question:\*\*\s*(.+?)(?=^\*\*Model answer|"
            r"^\*\*Model solution|^<!-- MODEL-BODY-START)"
            , block
        )
        body_match = re.search(
            r"(?ims)<!-- MODEL-BODY-START[^>]*-->\s*(.+?)\s*<!-- MODEL-BODY-END",
            block,
        )
        if question_match:
            question = markdown_plain(question_match.group(1))
        else:
            heading_text = markdown_plain(re.sub(r"^#{3,5}\s+", "", head.group(0)))
            inline_question = re.sub(
                r"(?i)^Original\s+(?:10|15|20)-marker(?:\s+\d+)?\s*[-—:]?\s*",
                "",
                heading_text,
            ).strip()
            inline_question = re.sub(
                r"(?i)^(?:Question\s+)?(?:10|15|20)\s+marks?\s*[-—:]?\s*",
                "",
                inline_question,
            ).strip()
            inline_question = re.sub(
                r"(?i)\s*Answer\s+in\s+\d+\s+words?\.?\s*$", "",
                inline_question,
            ).strip()
            question = plain(inline_question)
        if not body_match:
            body_match = re.search(
                r"(?ims)^\*\*Model solution\*{0,2}\s*:?\s*(.+?)"
                r"(?=^\*\*Why this earns marks|^#{3,5}\s|\Z)",
                block,
            )
        if not question or not body_match:
            continue
        answer = markdown_plain(body_match.group(1))
        answer_words = words(answer)
        if marks == 10 and not 85 <= answer_words <= 150:
            continue
        if marks == 15 and not 125 <= answer_words <= 250:
            continue
        if any(phrase in answer.lower() for phrase in (
            "the answer must resolve", "institution changes incentives",
            "constitutional legitimacy, adequate resources",
            "replace the weakest generalisation",
        )):
            continue
        relative = path.relative_to(ROOT).as_posix()
        subject = source_subject or path.relative_to(FINAL_LIBRARY).parts[0]
        records.append({
            "text": question,
            "marks": marks,
            "word_limit": 150 if marks == 10 else 250,
            "answer": answer,
            "source": relative,
            "subject": subject,
            "topic_id": relative.rsplit("/", 1)[0],
            "difficulty": "above-typical recent UPSC",
            "difficulty_features": [
                "question-specific demand", "named evidence", "analysis",
                "qualification", "source-grounded conclusion",
            ],
        })
    return records


def parse_complete_model_blocks(
    path: Path,
    source_subject: str,
    philosophy: bool = False,
) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    questions = list(re.finditer(
        r"(?im)^\s*>?\s*\*\*Question(?:,\s*as printed)?:\*\*\s*(.+)$",
        text,
    ))
    records: list[dict[str, Any]] = []
    for index, question_match in enumerate(questions):
        block_end = questions[index + 1].start() if index + 1 < len(questions) else len(text)
        block = text[question_match.end():block_end]
        model = re.search(
            r"(?im)^(?:#{4,6}\s+Independent model answer|"
            r"\*\*Model (?:solution|answer)(?:\s*\([^)]*\))?(?:[.:])?\*\*)\s*:?\s*(.*)$",
            block,
        )
        if not model:
            continue
        tail = (model.group(1).strip() + "\n" if model.lastindex and model.group(1).strip() else "") + block[model.end():]
        answer_end = re.search(
            r"(?im)^(?:\*\*(?:Why this earns marks|Demand decoding|Examiner check|"
            r"Answer-writing focus|Depth refinement)|#{3,6}\s+|\Z)",
            tail,
        )
        answer = markdown_plain(tail[:answer_end.start()] if answer_end else tail)
        question = markdown_plain(question_match.group(1))
        context = text[max(0, question_match.start() - 350):question_match.end() + 250]
        marks_match = re.search(r"(?i)\b(10|15|20)\s*marks?\b", context)
        if not marks_match:
            marks_match = re.search(r"(?i)\b(10|15|20)\s*marks?\b", block[:model.end()])
        if marks_match:
            marks = int(marks_match.group(1))
        else:
            word_limit_match = re.search(
                r"(?i)answer\s+(?:in|within)\s+(150|200|250|300|350|400)\s+words?",
                question,
            )
            if not word_limit_match:
                continue
            stated_limit = int(word_limit_match.group(1))
            marks = 10 if stated_limit <= 200 else (15 if stated_limit <= 300 else 20)
        allowed_marks = (10, 15, 20) if philosophy or source_subject == "Ethics" else (10, 15)
        if marks not in allowed_marks:
            continue
        count = words(answer)
        lower, upper = (
            {10: (100, 250), 15: (190, 340), 20: (270, 440)}[marks]
            if philosophy
            else {10: (80, 180), 15: (120, 290), 20: (170, 350)}[marks]
        )
        if not lower <= count <= upper:
            continue
        if any(phrase in answer.lower() for phrase in (
            "the answer must resolve", "trace the driver", "replace the weakest",
            "institution changes incentives", "constitutional legitimacy, adequate resources",
            "detailed examiner-grade model status",
        )):
            continue
        records.append({
            "text": question,
            "marks": marks,
            "word_limit": 200 if philosophy and marks == 10 else (
                300 if philosophy and marks == 15 else (
                    400 if philosophy and marks == 20 else (
                        150 if marks == 10 else (250 if marks == 15 else 300)
                    )
                )
            ),
            "answer": answer,
            "source": path.relative_to(ROOT).as_posix(),
            "subject": source_subject,
            "topic_id": path.relative_to(ROOT).parent.as_posix(),
            "difficulty": (
                "above-typical recent UPSC Philosophy Optional"
                if philosophy else "above-typical recent UPSC"
            ),
            "origin": "curated-complete-model",
        })
    return records


def parse_structured_model_blocks(path: Path, source_subject: str) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    heads = list(ORIGINAL_MAINS_HEAD_RE.finditer(text))
    records: list[dict[str, Any]] = []
    for index, head in enumerate(heads):
        marks_match = re.search(r"(?i)\b(10|15)\s*(?:marks?|marker)\b", head.group(0))
        if not marks_match:
            continue
        marks = int(marks_match.group(1))
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        block = text[head.end():end]
        question = re.search(r"(?im)^\*\*Question:\*\*\s*(.+)$", block)
        thesis = re.search(r"(?im)^\*\*Model thesis:\*\*\s*(.+)$", block)
        evidence = re.search(
            r"(?ims)^\*\*(?:Claim\s*(?:->|→)\s*named evidence\s*(?:->|→)\s*"
            r"analysis\s*(?:->|→)\s*qualification|Evidence spine):\*\*\s*(.+?)"
            r"(?=^\*\*(?:Balance|Counter-position / limit|Qualified conclusion|Conclusion):)",
            block,
        )
        conclusion = re.search(
            r"(?im)^\*\*(?:Qualified conclusion|Conclusion):\*\*\s*(.+)$",
            block,
        )
        if not all((question, thesis, evidence, conclusion)):
            continue
        evidence_points = [
            markdown_plain(match.group(1))
            for match in re.finditer(r"(?m)^\s*-\s+(.+)$", evidence.group(1))
        ]
        if len(evidence_points) < 3:
            continue
        clean_question = markdown_plain(question.group(1))
        if re.search(
            r"(?i)\bhow many of the above\b|\bcorrectly matched\b|"
            r"\bwhere a question invites\b|\bexaminer(?:s)? reward\b|"
            r"(?:^|\s)[A-D][.)]\s+.+(?:\s|·)[A-D][.)]\s+",
            clean_question,
        ):
            continue
        clean_question = re.sub(
            r"(?i)\s*Answer\s+in\s+(?:about\s+)?\d+\s+words?\.?\s*$",
            "",
            clean_question,
        ).strip()
        intro = markdown_plain(thesis.group(1))
        ending = markdown_plain(conclusion.group(1))
        body_points = evidence_points
        maximum = 150 if marks == 10 else 250
        minimum = 90 if marks == 10 else 135
        templated_thesis = bool(re.search(
            r"(?i)\bClaim:|\bNamed evidence/example:|"
            r"\bThis identifies the\b|\bThe conclusion must retain\b",
            intro,
        ))
        if templated_thesis:
            answer = " ".join(
                f"{index}. {point}" for index, point in enumerate(body_points, 1)
            )
        else:
            body_limit = maximum - min(words(intro), 42) - min(words(ending), 32)
            selected: list[str] = []
            for point in body_points:
                if words(" ".join(selected + [point])) <= body_limit:
                    selected.append(point)
            if not selected:
                continue
            answer_parts = [intro] + selected
            if normalize_stem(ending) != normalize_stem(intro):
                answer_parts.append(ending)
            answer = " ".join(answer_parts)
        if words(answer) > maximum:
            sentences = re.split(r"(?<=[.!?])\s+", answer)
            fitted: list[str] = []
            for sentence in sentences:
                if words(" ".join(fitted + [sentence])) <= maximum:
                    fitted.append(sentence)
            answer = " ".join(fitted)
        count = words(answer)
        if not minimum <= count <= maximum:
            continue
        records.append({
            "text": clean_question,
            "marks": marks,
            "word_limit": 150 if marks == 10 else 250,
            "answer": answer,
            "source": path.relative_to(ROOT).as_posix(),
            "subject": source_subject,
            "topic_id": path.relative_to(ROOT).parent.as_posix(),
            "difficulty": "above-typical recent UPSC",
            "origin": "curated-structured-model",
        })
    return records


def parse_philosophy_pyq_blocks(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    heads = sorted(
        list(re.finditer(
            r"(?im)^###\s+PYQ\s+\d+\s+[-—].*?\b(10|15|20)\s+marks?.*$",
            text,
        ))
        + list(re.finditer(
            r"(?im)^####\s+.*?\d{4}.*?\b(10|15|20)\s+marks?.*$",
            text,
        )),
        key=lambda match: match.start(),
    )
    records: list[dict[str, Any]] = []
    for index, head in enumerate(heads):
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        block = text[head.end():end]
        if head.group(0).lstrip().startswith("####"):
            question_head = re.search(
                r"(?im)\*\*Printed question(?:\s*\(verbatim\))?[.:]\*\*",
                block,
            )
            question_end = re.search(
                r"(?im)^\*\*(?:Demand decoded|Directive decoded|Directive read)",
                block,
            )
            exact_text = (
                block[question_head.end():question_end.start()]
                if question_head and question_end and question_end.start() > question_head.end()
                else ""
            )
            model = re.search(
                r"(?ims)^\*\*Model answer\s*\([^)]*\)\.\*\*\s*(.+?)"
                r"(?=^\*\*(?:Examiner|Why|Compact|Source)|^####\s|\Z)",
                block,
            )
        else:
            exact = re.search(
                r"(?ims)^####\s+Exact question\s*$\s*(?:>\s*)?\*\*[\"“]?(.*?)[\"”]?\*\*\s*$",
                block,
            )
            exact_text = exact.group(1) if exact else ""
            model = re.search(
                r"(?ims)^####\s+Model answer(?:\s*\([^)]*\))?\s*$\s*(.+?)"
                r"(?=^####\s+Why this earns marks|^####\s+Compact skeleton|^###\s+PYQ|\Z)",
                block,
            )
        if not exact_text or not model:
            continue
        marks = int(head.group(1))
        question = markdown_plain(exact_text)
        answer = markdown_plain(model.group(1))
        count = words(answer)
        lower, upper = {10: (125, 220), 15: (200, 330), 20: (280, 430)}[marks]
        if not lower <= count <= upper:
            continue
        records.append({
            "text": question,
            "marks": marks,
            "word_limit": {10: 200, 15: 300, 20: 400}[marks],
            "answer": answer,
            "source": path.relative_to(ROOT).as_posix(),
            "subject": "Philosophy-Optional",
            "topic_id": path.relative_to(ROOT).parent.as_posix(),
            "difficulty": "above-typical recent UPSC Philosophy Optional",
            "origin": "curated-complete-philosophy-model",
        })
    return records


def round_robin_records(
    records: list[dict[str, Any]],
    subjects: list[str],
    count: int,
    excluded_topics: set[str],
    excluded_questions: set[str],
    excluded_answers: set[str],
) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {
        subject: sorted(
            [
                record for record in records
                if record["subject"] == subject and record["topic_id"] not in excluded_topics
            ],
            key=lambda record: (
                {
                    "curated-complete-model": 0,
                    "curated-structured-model": 1,
                    "knowledge-derived-mains": 2,
                }.get(record.get("origin", ""), 3),
                record["topic_id"],
                record["text"],
            ),
        )
        for subject in subjects
    }
    selected: list[dict[str, Any]] = []
    cursors = defaultdict(int)
    while len(selected) < count:
        progressed = False
        for subject in subjects:
            pool = grouped[subject]
            while cursors[subject] < len(pool):
                candidate = pool[cursors[subject]]
                cursors[subject] += 1
                if candidate["topic_id"] in excluded_topics:
                    continue
                if any(
                    question_similarity(candidate["text"], previous) >= 0.72
                    for previous in excluded_questions
                ):
                    continue
                if any(
                    question_similarity(candidate["answer"], previous) >= 0.65
                    for previous in excluded_answers
                ):
                    continue
                excluded_topics.add(candidate["topic_id"])
                excluded_questions.add(candidate["text"])
                excluded_answers.add(candidate["answer"])
                selected.append(candidate)
                progressed = True
                break
            if len(selected) == count:
                break
        if not progressed:
            raise RuntimeError(f"Insufficient distinct source topics for {count} GS questions")
    return selected


def source_answer_thesis(text: str, title: str) -> str:
    patterns = [
        r"(?im)^\s*>\s*\*\*Answer thesis:\*\*\s*(.+)$",
        r"(?im)^\s*\*\*Core proposition:\*\*\s*(.+)$",
        r"(?im)^\s*\*\*Foundation[^:]*:\*\*\s*(.+)$",
        r"(?im)^\s*\*\*Answer line:\*\*\s*(.+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            thesis = markdown_plain(match.group(1))
            if 12 <= words(thesis) <= 65 and source_safe_extract(thesis):
                return thesis.rstrip(".") + "."
    return f"{title} is best explained by connecting its defining mechanism, evidence, limits and consequences."


def source_mains_prompts(text: str) -> dict[int, list[str]]:
    prompts: dict[int, list[str]] = {10: [], 15: []}
    for match in re.finditer(
        r"(?ims)^\s*-\s*⚠️\s*\*\*Mains\s*\((10|15)\s*marks?[^)]*\):\*\*\s*(.+?)"
        r"(?=^\s*-\s*[✅❌⚠📰]|^##\s|\Z)",
        text,
    ):
        prompt = markdown_plain(match.group(2))
        if source_safe_prompt(prompt):
            prompts[int(match.group(1))].append(prompt)
    mains_section = re.search(r"(?im)^##\s+\d*\.?\s*Mains angles\s*$", text)
    if mains_section:
        tail = text[mains_section.end():]
        next_h2 = re.search(r"(?m)^##\s+", tail)
        if next_h2:
            tail = tail[:next_h2.start()]
        angles = [
            markdown_plain(match.group(1))
            for match in re.finditer(
                r"(?ms)^\s*-\s*⚠️\s*(.+?)(?=^\s*-\s*[✅❌⚠📰]|^##\s|\Z)",
                tail,
            )
        ]
        for index, angle in enumerate(angles):
            prompt = re.sub(r"^(?:GS-[IVX]+|Prelims)\s*:\s*", "", angle, flags=re.I)
            if source_safe_prompt(prompt):
                prompts[10 if index % 2 == 0 else 15].append(prompt)
    for match in re.finditer(
        r"(?ims)^\*\*\d{4}\s+GS-[IVX]+.*?[—-]\s*[\"“](.+?)[\"”].*?"
        r"(10|15)\s*marks",
        text,
    ):
        prompt = markdown_plain(match.group(1))
        if source_safe_prompt(prompt):
            prompts[int(match.group(2))].append(prompt)
    return prompts


def source_fact_sentences(text: str) -> list[str]:
    preferred = preferred_knowledge_text(text)
    candidates = knowledge_bullets(preferred, "✅")
    candidates += [
        correction for _wrong, correction in knowledge_traps(text)
    ]
    candidates += knowledge_bullets(text, "⚠️")
    output: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        candidate = re.sub(
            r"^(?:Claim|Named Evidence|Evidence|Significance|Limitation|Answer Thesis|"
            r"Accretion Thesis|Factual Caveat|Owned Core|[A-Za-z -]+Thesis)\s*:\s*",
            "",
            candidate,
            flags=re.I,
        )
        candidate = plain(candidate).strip()
        if not 8 <= words(candidate) <= 55 or not source_safe_extract(candidate):
            continue
        key = normalize_stem(candidate)
        if key in seen:
            continue
        seen.add(key)
        output.append(candidate.rstrip(".") + ".")
    return output


def knowledge_model_answer(text: str, title: str, marks: int, question: str) -> str:
    facts = source_fact_sentences(text)
    question_tokens = {
        token.lower() for token in WORD_RE.findall(question)
        if len(token) > 2 and token.lower() not in {
            "explain", "analyse", "analyze", "discuss", "examine", "evaluate",
            "reference", "through", "relationship", "limits", "revealed",
            "why", "how", "can", "the", "and", "with", "into", "from",
        }
    }
    facts.sort(
        key=lambda fact: (
            len(question_tokens & {token.lower() for token in WORD_RE.findall(fact)}),
            len(fact),
        ),
        reverse=True,
    )
    thesis = source_answer_thesis(text, title)
    traps = knowledge_traps(text)
    traps.sort(
        key=lambda pair: len(
            question_tokens
            & {token.lower() for token in WORD_RE.findall(pair[0] + " " + pair[1])}
        ),
        reverse=True,
    )
    target_min = 95 if marks == 10 else 165
    target_max = 148 if marks == 10 else 242
    selected: list[str] = []
    for fact in facts:
        if words(" ".join(selected + [fact])) <= target_max - 35:
            selected.append(fact)
        if len(selected) >= (3 if marks == 10 else 5):
            break
    if not selected:
        raise ValueError(f"No relevant source facts for {title}")
    intro = thesis if "best explained by connecting" not in thesis.lower() else selected.pop(0)
    intro = re.sub(rf"^{re.escape(title)}\s*:\s*", "", intro, flags=re.I)
    counter = traps[0][1] if traps else (
        selected[-1] if len(selected) > 1 else "The evidence must not be extended beyond the stated scale and period."
    )
    conclusion = (
        selected[-1]
        if "best explained by connecting" in thesis.lower()
        else (thesis if normalize_stem(thesis) != normalize_stem(intro) else selected[-1])
    )
    answer = (
        f"Introduction: {intro} "
        f"Analysis: {' '.join(selected)} "
        f"Counterpoint: {counter} "
        f"Conclusion: {conclusion}"
    )
    if words(answer) > target_max:
        while len(selected) > 2 and words(answer) > target_max:
            selected.pop()
            answer = (
                f"Introduction: {intro} Analysis: {' '.join(selected)} "
                f"Counterpoint: {counter} Conclusion: {conclusion}"
            )
    if words(answer) < target_min:
        raise ValueError(f"Insufficient source material for {title} ({marks} marks): {words(answer)}")
    return answer


def build_knowledge_mains_records(
    path: Path, paper: str, source_subject: str
) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    title_match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    if not title_match:
        return []
    title = re.sub(
        r"\s*[-—]\s*MUST-DO.*$", "", markdown_plain(title_match.group(1)), flags=re.I
    )
    title = re.sub(
        r"\s*[-—]\s*(?:Complete Uncompressed Learning Session|Complete Learning Session|BASIC|MUST-DO).*$",
        "",
        title,
        flags=re.I,
    )
    prompts = source_mains_prompts(text)
    facts = source_fact_sentences(text)
    question_facts = [fact for fact in facts if words(fact) <= 32]
    traps = knowledge_traps(text)
    records = []
    for marks in (10, 15):
        if not prompts[marks]:
            return []
        question = prompts[marks][0]
        try:
            answer = knowledge_model_answer(text, title, marks, question)
        except ValueError:
            continue
        records.append({
            "text": plain(question),
            "marks": marks,
            "word_limit": 150 if marks == 10 else 250,
            "answer": answer,
            "source": path.relative_to(ROOT).as_posix(),
            "subject": source_subject,
            "topic_id": path.relative_to(ROOT).with_suffix("").as_posix(),
            "difficulty": "above-typical recent UPSC",
            "difficulty_features": [
                "question-specific demand", "named evidence", "analysis",
                "qualification", "source-grounded conclusion",
            ],
            "origin": "knowledge-derived-mains",
        })
    return records


@lru_cache(maxsize=1)
def build_gs_banks() -> dict[str, list[dict[str, Any]]]:
    banks: dict[str, list[dict[str, Any]]] = {}
    for paper, subjects in GS_SOURCE_SUBJECTS.items():
        records: list[dict[str, Any]] = []
        for subject in subjects:
            for path in sorted((FINAL_LIBRARY / subject).rglob("Solved-Practice-Workbook.md")):
                records.extend(parse_complete_model_blocks(path, subject))
                records.extend(parse_structured_model_blocks(path, subject))
        unique_records: dict[tuple[int, str], dict[str, Any]] = {}
        for record in records:
            if paper == "GS-III" and record["subject"] == "Economy":
                record["subject"] = gs3_economy_category(record["source"])
            if paper == "GS-I":
                record["subject"] = gs1_category(record["subject"], record["source"])
            if re.search(
                r"(?i)\bhow many of the above\b|\bcorrectly matched\b|"
                r"\bwhere a question invites\b|\bexaminer(?:s)? reward\b|"
                r"\banswer-writing\b|\bdemand decoding\b|"
                r"(?:^|\s)[A-D][.)]\s+.+(?:\s|·)[A-D][.)]\s+",
                record["text"],
            ):
                continue
            record.setdefault("difficulty_features", [
                "question-specific demand", "named evidence", "analysis",
                "qualification", "source-grounded conclusion",
            ])
            count = words(record["answer"])
            if not re.search(r"[.!?][\"')\]]?\s*$", record["answer"]):
                continue
            if record["marks"] == 10 and not 90 <= count <= 150:
                continue
            if record["marks"] == 15 and not 135 <= count <= 250:
                continue
            if any(phrase in record["answer"].lower() for phrase in (
                "the answer must resolve", "trace the driver", "replace the weakest",
                "claim evidence analysis qualification check",
                "answer method audit",
                "previous audit", "correction record",
                "latest completed national edition located",
                "keep only the application",
                "audited model-answer", "audited 2024",
                "local arthasastra", "cited official pages do not verify",
                "evidence base require",
                "repository's local", "optical character recognition",
                "source records", "source text", "recorded here rather than adopted",
            )):
                continue
            unique_records.setdefault(
                (record["marks"], normalize_stem(record["text"])),
                record,
            )
        records = list(unique_records.values())
        selection_subjects = GS_SELECTION_ORDER[paper]
        used_question_cores: set[str] = set()
        used_answer_cores: set[str] = set()
        tens: list[dict[str, Any]] = []
        fifteens: list[dict[str, Any]] = []
        for _set_index in range(4):
            used_topics: set[str] = set()
            selected_tens = round_robin_records(
                [record for record in records if record["marks"] == 10],
                selection_subjects, 10, used_topics, used_question_cores, used_answer_cores,
            )
            selected_fifteens = round_robin_records(
                [record for record in records if record["marks"] == 15],
                selection_subjects, 10, used_topics, used_question_cores, used_answer_cores,
            )
            tens.extend(selected_tens)
            fifteens.extend(selected_fifteens)
        banks[paper] = tens + fifteens
    return banks


def build_gs_paper(name: str, set_no: int) -> dict[str, Any]:
    bank = build_gs_banks()[name]
    tens = bank[(set_no - 1) * 10:set_no * 10]
    fifteens = bank[40 + (set_no - 1) * 10:40 + set_no * 10]
    selected = tens + fifteens
    questions = []
    for index, source_record in enumerate(selected, 1):
        record = dict(source_record)
        record["no"] = index
        questions.append(record)
    return {
        "kind": "mains", "paper": name, "title": f"UPSC Civil Services (Main) Simulation {name}",
        "time": "3 Hours", "max_marks": 250, "questions": questions,
        "instructions": [
            "There are TWENTY questions. All questions are compulsory.",
            "Questions 1-10 carry 10 marks each and should be answered in 150 words.",
            "Questions 11-20 carry 15 marks each and should be answered in 250 words.",
            "Answers must remain relevant to the demand and use appropriate examples.",
        ],
    }


ESSAY_TOPICS = [
    ("Freedom grows when power accepts reasons.", ["constitutionalism", "public reason", "dissent", "institutional restraint"]),
    ("The shortest route to progress may bypass justice.", ["development", "distribution", "environment", "democratic consent"]),
    ("Memory can liberate a society, but it can also imprison it.", ["history", "identity", "reconciliation", "education"]),
    ("Doubt is not the enemy of conviction; it is its discipline.", ["science", "ethics", "faith", "public policy"]),
    ("A connected world can still produce isolated citizens.", ["technology", "community", "mental health", "democracy"]),
    ("Efficiency without empathy is an incomplete public virtue.", ["administration", "welfare", "markets", "dignity"]),
    ("Institutions become strong when ordinary people can question them.", ["accountability", "rights", "participation", "trust"]),
    ("The future belongs not to those who predict it, but to those who prepare fairly for it.", ["climate", "skills", "federalism", "intergenerational justice"]),
    ("Silence may preserve peace for a day and injustice for a generation.", ["moral courage", "social reform", "diplomacy", "law"]),
    ("The value of knowledge lies partly in knowing its limits.", ["science", "governance", "expertise", "uncertainty"]),
    ("Identity is a home when open, and a prison when sealed.", ["culture", "pluralism", "nationalism", "migration"]),
    ("Care is an economic infrastructure hidden in private life.", ["gender", "labour", "health", "social policy"]),
    ("India's demographic future depends more on capability than on numbers.", ["education", "health", "employment", "gender"]),
    ("Climate resilience is a test of federalism as much as of technology.", ["local government", "finance", "science", "equity"]),
    ("Digital public infrastructure must expand agency, not merely transactions.", ["inclusion", "privacy", "competition", "service delivery"]),
    ("Agricultural prosperity requires moving from output security to income and ecological security.", ["markets", "water", "risk", "diversification"]),
    ("A nation is secure when its citizens trust both borders and institutions.", ["defence", "rights", "social cohesion", "cybersecurity"]),
    ("Urbanisation will be India's opportunity only if cities become governable.", ["municipal finance", "housing", "mobility", "climate"]),
    ("Strategic autonomy is sustained by domestic capability.", ["industry", "technology", "energy", "diplomacy"]),
    ("Public health is built before a patient reaches a hospital.", ["prevention", "sanitation", "primary care", "surveillance"]),
    ("Equality sometimes requires treating unequal circumstances differently.", ["equity", "reservation", "disability", "federalism"]),
    ("Markets discover prices; societies must still decide values.", ["economy", "environment", "care", "culture"]),
    ("A rule gains legitimacy when those bound by it can understand and challenge it.", ["law", "language", "due process", "administration"]),
    ("Education should prepare citizens to revise answers, not merely remember them.", ["critical thinking", "democracy", "science", "skills"]),
    ("India's energy transition is also a transition of jobs, regions and power.", ["coal regions", "renewables", "grid", "justice"]),
    ("The credibility of welfare depends on the dignity of delivery.", ["entitlements", "frontline state", "technology", "grievance redress"]),
    ("Cultural diversity survives through living livelihoods, not museum admiration alone.", ["artisans", "language", "tourism", "intellectual property"]),
    ("Disaster risk is often development risk accumulated over time.", ["land use", "infrastructure", "poverty", "preparedness"]),
    ("Foreign policy begins at home but cannot end there.", ["capability", "diaspora", "global commons", "multilateralism"]),
    ("Artificial intelligence will reflect the institutions that govern it.", ["bias", "innovation", "labour", "accountability"]),
    ("Water disputes reveal the geography of politics and the politics of geography.", ["federalism", "basins", "agriculture", "climate"]),
    ("A constitutional democracy must protect both the mandate and the minority.", ["elections", "rights", "judicial review", "deliberation"]),
]


ESSAY_EVIDENCE = {
    "constitutionalism": "Kesavananda Bharati limits constituted power through the basic-structure doctrine.",
    "public reason": "Reasoned judicial and administrative orders allow coercive power to be criticised.",
    "dissent": "The freedom movement joined civil disobedience with disciplined public argument.",
    "institutional restraint": "Federalism, judicial review and legislative scrutiny divide authority.",
    "development": "Displacement around dams and mines shows that aggregate gains can conceal concentrated losses.",
    "distribution": "Public health, education and social protection convert growth into capability.",
    "environment": "Wetlands and mangroves provide flood and cyclone protection that markets often undervalue.",
    "democratic consent": "Gram Sabha consultation demonstrates that procedure can improve both legitimacy and information.",
    "history": "Colonial economic critique transformed poverty from fate into a political question.",
    "identity": "Linguistic reorganisation accommodated identity while preserving the Union.",
    "reconciliation": "Truth-telling and institutional reform prevent memory from becoming inherited revenge.",
    "education": "Critical pedagogy teaches learners to revise claims when evidence changes.",
    "science": "Scientific institutions advance through doubt, reproducibility and correction.",
    "ethics": "Gandhi's insistence on the relation of means and ends disciplines conviction.",
    "faith": "Constitutional secularism protects belief while requiring public reasons for state coercion.",
    "public policy": "Pilot, evaluation and review clauses make policy corrigible.",
    "technology": "Aadhaar-enabled delivery illustrates both scale and exclusion risk.",
    "community": "Self-help groups turn isolated capacity into collective bargaining and mutual support.",
    "mental health": "Urban loneliness shows that communication density is not social belonging.",
    "democracy": "Universal franchise gives equal voice, while institutions determine whether voice is effective.",
    "administration": "Dated receipts and appeal routes convert service promises into enforceable accountability.",
    "welfare": "NFSA entitlements distinguish rights-based provision from discretionary charity.",
    "markets": "Markets reveal willingness to pay but not the value of unpaid care or biodiversity.",
    "dignity": "Manual-scavenging abolition shows why service delivery must be judged through human dignity.",
    "accountability": "RTI and social audit connect information, answerability and correction.",
    "rights": "Fundamental rights protect persons even when immediate majorities disagree.",
    "participation": "Participatory planning supplies local knowledge that central design may miss.",
    "trust": "Transparent crisis communication preserves compliance better than false certainty.",
    "climate": "Heat action plans show adaptation must combine forecasts with local health and labour protocols.",
    "skills": "Capability grows when training is linked to certification, markets and continuing learning.",
    "federalism": "GST Council and disaster management reveal both cooperation and bargaining across governments.",
    "intergenerational justice": "Net-zero and groundwater choices distribute risk across persons not present at today's table.",
    "gender": "Unpaid care, safety and asset ownership shape women's economic agency.",
    "labour": "Portability and social security determine whether migration enlarges freedom.",
    "health": "Primary care, sanitation and surveillance create health before hospital treatment.",
    "social policy": "Targeted support must combine inclusion criteria with grievance redress.",
    "local government": "The 73rd and 74th Amendments created elected bodies, but devolution determines capacity.",
    "finance": "Predictable transfers and own revenue turn assigned functions into executable authority.",
    "equity": "Substantive equality adjusts for relevant disadvantage without abandoning public criteria.",
    "inclusion": "Offline alternatives prevent digital convenience from becoming exclusion.",
    "privacy": "Puttaswamy requires legality, necessity and proportionality for data intrusion.",
    "competition": "Open standards and interoperability can prevent digital infrastructure from becoming private gatekeeping.",
    "service delivery": "Sevottam-style standards matter only with traceability and escalation.",
    "water": "Solar irrigation can lower emissions yet increase groundwater extraction when marginal pumping cost collapses.",
    "risk": "Crop insurance and diversification address different parts of agricultural risk.",
    "diversification": "Millets, horticulture and livestock can reduce dependence on a narrow crop-income base.",
    "defence": "Military capability deters threats, but legitimacy and social cohesion sustain national resilience.",
    "social cohesion": "Communal peace depends on equal protection and institutions that interrupt rumour.",
    "cybersecurity": "Critical infrastructure requires redundancy, reporting and rights-sensitive incident response.",
    "municipal finance": "Property taxation and user charges need transparency, equity and visible service improvement.",
    "housing": "In-situ upgrading often preserves livelihoods better than peripheral relocation.",
    "mobility": "Reliable public transport expands access to work more fairly than road capacity alone.",
    "industry": "Domestic manufacturing capability gives strategic choices credibility.",
    "energy": "Import diversification, storage and efficiency make autonomy materially sustainable.",
    "diplomacy": "Strategic autonomy means issue-based choice supported by domestic capability, not equidistance.",
    "prevention": "Vaccination, clean water and early warning reduce harm before emergency treatment.",
    "sanitation": "Public health externalities make sanitation more than a private consumption choice.",
    "primary care": "Continuity and referral at the primary level reduce avoidable hospital load.",
    "surveillance": "Disease surveillance must join timely detection with privacy and public trust.",
    "reservation": "Reservation addresses structured exclusion but requires complementary capability and anti-discrimination measures.",
    "disability": "Reasonable accommodation converts formal access into usable equality.",
    "care": "Childcare and eldercare are productive infrastructures hidden by national accounts.",
    "culture": "Living artisans require markets, transmission and rights, not display alone.",
    "law": "A rule is legitimate when clear, prospective, equally applied and open to challenge.",
    "language": "Multilingual public services turn formal citizenship into practical access.",
    "due process": "Notice, hearing and reasons protect persons from arbitrary power.",
    "critical thinking": "Scientific temper under Article 51A(h) links citizenship with inquiry and reform.",
    "skills": "Training yields mobility only when employers recognise and use the acquired competence.",
    "coal regions": "A just transition must replace local jobs, royalties and public services, not only generating capacity.",
    "renewables": "Variable energy requires transmission, storage and flexible demand.",
    "grid": "A power transition fails if generation grows faster than evacuation and balancing capacity.",
    "entitlements": "An entitlement survives administrative failure only when fallback and appeal are available.",
    "frontline state": "Citizens experience the Constitution through teachers, nurses, police and local offices.",
    "grievance redress": "A complaint system needs receipts, time limits, appeal and published outcomes.",
    "artisans": "Geographical indications help only when producers control quality and value capture.",
    "tourism": "Tourism can finance conservation but may commodify or displace the community sustaining heritage.",
    "intellectual property": "Protection should reward creators without freezing shared cultural traditions.",
    "land use": "Flood losses often reflect construction on drainage paths rather than rainfall alone.",
    "infrastructure": "Resilience requires lifecycle maintenance and redundancy, not only new assets.",
    "poverty": "Low assets and insecure work convert hazards into unequal disasters.",
    "preparedness": "Warnings save lives only when evacuation, transport and trust complete the chain.",
    "capability": "Amartya Sen's capability approach judges whether people can convert resources into real freedoms.",
    "diaspora": "Diaspora networks create knowledge and investment links while vulnerable workers require protection.",
    "global commons": "Climate, oceans and cyberspace require cooperation beyond territorial control.",
    "multilateralism": "India's coalitions seek voice for developing countries within unequal institutions.",
    "bias": "Historical data can reproduce past discrimination when used uncritically by algorithms.",
    "innovation": "Regulatory sandboxes permit learning without treating public risk as an experiment without consent.",
    "basins": "River governance must follow hydrology while political authority follows state boundaries.",
    "agriculture": "Cropping patterns turn rainfall and procurement choices into interstate water conflict.",
    "elections": "Electoral mandate authorises government but does not extinguish constitutional limits.",
    "judicial review": "Review protects constitutional boundaries while requiring judicial restraint and reasons.",
    "deliberation": "Committees and public consultation test proposals before irreversible choice.",
    "economy": "National accounts price market output but leave many ecological and care values outside the production boundary.",
    "employment": "A just transition must create credible work pathways before carbon-intensive livelihoods disappear.",
    "expertise": "Expert advice improves decisions only when assumptions, uncertainty and conflicts of interest are open to scrutiny.",
    "governance": "Capacity, accountability and grievance redress determine whether policy intent becomes a citizen outcome.",
    "justice": "Constitutional justice tests both fair procedure and the distribution of benefits, burdens and voice.",
    "migration": "Migration can enlarge opportunity while weakening access to domicile-linked welfare and social support.",
    "moral courage": "Whistle-blowers and reformers show that conscience becomes public virtue only when it accepts reasoned risk.",
    "nationalism": "Anti-colonial nationalism joined political freedom with competing visions of social and economic emancipation.",
    "pluralism": "Pluralism sustains common citizenship without requiring cultural uniformity or unchecked group authority.",
    "social reform": "Reform movements challenged inherited hierarchy by combining moral criticism, organisation and legal change.",
    "uncertainty": "Precaution, revisability and transparent assumptions make action possible without pretending to possess certainty.",
}


# Authored, title-specific essay frameworks. Each entry is written for its own proposition:
# the thesis interprets that exact title, the dimensions and examples are independently
# researched India-centric material, and the counterview states a genuine objection.
ESSAY_AUTHORED_FRAMEWORKS: dict[str, dict[str, Any]] = {
    "Freedom grows when power accepts reasons.": {
        "thesis": (
            "Freedom is not merely the absence of restraint but the presence of authority obliged to "
            "explain itself. Where rulers must state grounds that citizens can examine, arbitrary "
            "command becomes contestable decision and liberty acquires a defensible boundary. The "
            "proposition therefore ties liberty less to permission granted from above and more to the "
            "continuing duty of justification owed downward."
        ),
        "structure": [
            "Separate freedom as non-interference from freedom as protection against unaccountable will.",
            "Show how a written Constitution converts sovereign command into reviewable, reasoned authority.",
            "Trace reason-giving downward from constitutional benches to the police station and ration shop.",
            "Test emergencies, secrecy and speed, where reasons are delayed, abridged or withheld.",
            "Close on the conditions that keep justification genuine rather than ritual paperwork.",
        ],
        "dimensions": [
            "Constitutional limitation matters because even amending power is held answerable to reasons about "
            "the Constitution's own identity and continuity.",
            "Recorded reasons in judicial and administrative orders create the raw material for appeal, "
            "precedent and correction rather than silent discretion.",
            "Disciplined dissent supplies grounds the government has not weighed, making protest an information "
            "system for the state and not merely a claim against it.",
            "Divided authority through review, federal distribution and legislative scrutiny prevents any single "
            "office from certifying the adequacy of its own reasons.",
        ],
        "examples": [
            "Kesavananda Bharati (1973) held that Parliament's amending power cannot destroy the Constitution's "
            "basic structure.",
            "Maneka Gandhi (1978) required a procedure depriving liberty to be fair, just and reasonable rather "
            "than merely enacted.",
            "Gandhi's Salt Satyagraha of 1930 broke a law while publicly stating its moral grounds and accepting "
            "the punishment.",
            "The Right to Information Act, 2005 turned file notings and recorded reasons into citizen-accessible "
            "evidence of official conduct.",
        ],
        "counterview": (
            "Reason-giving can be counterfeited. Elaborate orders may rationalise decisions already taken, and "
            "articulate elites can crowd out those least able to litigate. In a genuine emergency, demanding "
            "justification before acting may cost lives. Liberty therefore needs more than reasons: it needs "
            "cheap access to challenge them and remedies arriving before harm turns irreversible."
        ),
        "conclusion": (
            "Liberty expands where justification is habitual, inexpensive to demand and open to rebuttal. The "
            "Indian experience suggests reasons matter most when the poorest litigant, and not only a "
            "constitutional bench, can insist on hearing them."
        ),
    },
    "The shortest route to progress may bypass justice.": {
        "thesis": (
            "Speed is a genuine public value, since delayed roads, power and clinics also destroy lives. Yet the "
            "quickest path usually concentrates gains and disperses costs onto those least able to refuse. The "
            "proposition warns that a shortcut appears cheap only because somebody outside the official "
            "accounting is quietly paying for it."
        ),
        "structure": [
            "Concede the moral case for haste by naming what delay costs the poor.",
            "Show how aggregate benefit statistics conceal the identity of those bearing the loss.",
            "Treat consent procedure as an information device rather than a legal formality.",
            "Distinguish recoverable delay from irreversible ecological and social damage.",
            "Propose a test: speed is legitimate when the displaced end up genuinely better off.",
        ],
        "dimensions": [
            "Project accounting records benefits at national scale while displacement, lost commons and broken "
            "livelihoods register only locally and belatedly.",
            "Distribution decides whether growth becomes capability, because schooling, health and social "
            "protection convert additional income into real freedom.",
            "Ecological shortcuts borrow from the future, since wetlands, mangroves and aquifers repay their "
            "stored value only when a disaster finally arrives.",
            "Consultation slows decisions but improves them, as affected communities hold hydrological and social "
            "knowledge that rapid survey work routinely misses.",
        ],
        "examples": [
            "The Narmada dam controversy showed irrigation and power gains coexisting with unresolved "
            "rehabilitation of displaced households.",
            "The Forest Rights Act, 2006 and the Niyamgiri gram sabha decision of 2013 gave affected villages a "
            "decisive institutional voice.",
            "Chennai's 2015 flood losses followed construction over the Pallikaranai marsh and other natural "
            "drainage corridors.",
            "Kudumbashree in Kerala raised household incomes through organised collectives without displacing "
            "existing settlements or occupations.",
        ],
        "counterview": (
            "Justice can also be invoked to defend privilege. Endless clearance, litigation and consultation have "
            "stranded highways, transmission lines and public housing that would have served poorer users first. "
            "Where procedure becomes veto rather than voice, delay itself transfers costs to the unorganised. The "
            "remedy is time-bound evidence-based process, not additional process."
        ),
        "conclusion": (
            "Progress is defensible when it can name its losers and demonstrate what it did for them. India's "
            "task is not choosing between speed and justice, but making fair procedure fast enough to remain "
            "credible."
        ),
    },
    "Memory can liberate a society, but it can also imprison it.": {
        "thesis": (
            "Recollection is politically active. Remembering injustice arms reform with moral urgency, as "
            "anti-colonial and anti-caste movements demonstrated. The same memory, curated selectively, converts "
            "grievance into inheritance and locks communities into permanent accusation. The proposition asks "
            "which institutions decide whether the past becomes usable evidence or reusable ammunition."
        ),
        "structure": [
            "Separate memory as historical evidence from memory as political identity.",
            "Show liberation: recovering suppressed suffering makes reform politically thinkable.",
            "Show confinement: sealed grievance narratives reward mobilisation over settlement.",
            "Identify what converts one into the other through acknowledgement, remedy and honest teaching.",
        ],
        "dimensions": [
            "Historical method liberates by testing claims against evidence, letting a society argue about its "
            "past without inventing a convenient version of it.",
            "Group identity draws cohesion from remembered wrong, yet solidarity built only on grievance finds "
            "any negotiated settlement psychologically unavailable.",
            "Reconciliation demands acknowledgement joined to institutional remedy, because apology without "
            "changed practice preserves the very injury it names.",
            "Curriculum decides transmission, since schooling either teaches children to weigh sources or hands "
            "them inherited verdicts they never learn to examine.",
        ],
        "examples": [
            "Dadabhai Naoroji's drain theory turned remembered impoverishment into an evidence-based political "
            "indictment of colonial rule.",
            "Ambedkar's Mahad satyagraha of 1927 used the memory of exclusion to claim public water as a civic "
            "right.",
            "Jallianwala Bagh survives as national memory, though its meaning is contested between commemoration "
            "and spectacle.",
            "Partition oral-history archives preserve survivor testimony across communities instead of "
            "consolidating one ownership of suffering.",
        ],
        "counterview": (
            "Forgetting is sometimes the humane choice. Societies emerging from massacre have purchased peace by "
            "refusing to litigate every wrong, and relentless remembrance can retraumatise survivors while "
            "empowering entrepreneurs of resentment. Yet amnesia negotiated by the powerful is not neutrality; it "
            "usually preserves an unjust distribution and silences those who lost most."
        ),
        "conclusion": (
            "Memory serves freedom when it is accurate, publicly contestable and attached to remedy. India's "
            "plural past is safest when taught as argument and evidence rather than as a ledger of debts awaiting "
            "collection."
        ),
    },
    "Doubt is not the enemy of conviction; it is its discipline.": {
        "thesis": (
            "Conviction never tested is only inherited opinion. Doubt subjects belief to evidence, alternative "
            "explanation and the live possibility of error, and whatever survives that examination is held more "
            "firmly and more honestly. The proposition treats scepticism as the training of belief rather than "
            "its dissolution into indecision."
        ),
        "structure": [
            "Define doubt as method: provisional suspension for the sake of testing, not permanent paralysis.",
            "Apply it to knowledge, where reproducibility and error correction build reliability.",
            "Apply it to conscience and faith, where self-examination separates principle from prejudice.",
            "Apply it to governance, where pilots, evaluation and sunset clauses keep policy corrigible.",
            "Mark the limit: decisions cannot await certainty, so doubt must be time-bound.",
        ],
        "dimensions": [
            "Scientific practice institutionalises doubt through peer review, replication and failure analysis, "
            "converting individual error into cumulative public reliability.",
            "Ethical conviction gains authority when it survives self-criticism, which is why Gandhi tied the "
            "truth of an end to the purity of the means chosen.",
            "Constitutional secularism protects belief while requiring publicly stateable reasons before the "
            "state coerces anybody in the name of that belief.",
            "Policy learns only when designed to be wrong safely, using pilots, independent evaluation and "
            "scheduled review before irreversible commitment.",
        ],
        "examples": [
            "ISRO's analysis of the Chandrayaan-2 landing failure informed design changes behind the successful "
            "Chandrayaan-3 landing in 2023.",
            "Article 51A(h) makes developing scientific temper and the spirit of inquiry a duty of every "
            "citizen.",
            "The 2010 moratorium on Bt brinjal followed contested evidence and public consultation rather than "
            "administrative certainty.",
            "Ambedkar's warning against hero-worship in politics cautioned citizens against surrendering "
            "judgement to inherited conviction.",
        ],
        "counterview": (
            "Perpetual doubt has costs. Manufactured uncertainty delayed action on tobacco, air pollution and "
            "climate change, and a public trained only to question can be manipulated into distrusting reliable "
            "knowledge. Doubt disciplines conviction only when applied equally to comforting and inconvenient "
            "claims, and when it accepts provisional closure so that action remains possible."
        ),
        "conclusion": (
            "The disciplined believer acts on the best available evidence while publishing the conditions that "
            "would change her mind. That combination, not certainty, makes conviction trustworthy in science, "
            "conscience and administration alike."
        ),
    },
    "A connected world can still produce isolated citizens.": {
        "thesis": (
            "Connection measures channels, not belonging. A citizen may hold a smartphone, a bank account and a "
            "hundred group conversations while lacking anyone accountable for her wellbeing, any forum where her "
            "voice changes an outcome, or a neighbour who notices her absence. The proposition separates "
            "communication density from social membership."
        ),
        "structure": [
            "Distinguish reach, interaction and belonging as three different achievements.",
            "Show digital infrastructure widening access while thinning face-to-face reciprocity.",
            "Treat loneliness and labour migration as material conditions, not merely emotional states.",
            "Ask whether online publics deepen democratic deliberation or fragment shared facts.",
            "Identify institutions that reconnect: local government, collectives and public space.",
        ],
        "dimensions": [
            "Platforms lower the cost of contact while raising the cost of attention, so relationships multiply "
            "even as their depth and obligation fall.",
            "Migration for work removes neighbourhood support exactly when economic insecurity is greatest, as "
            "the 2020 lockdown exposed with unusual clarity.",
            "Mental distress becomes a public issue where long commutes, insecure work and nuclear households "
            "remove the everyday support families once supplied.",
            "Democratic deliberation needs shared facts and slow argument, which feeds optimised for engagement "
            "and outrage rarely provide.",
        ],
        "examples": [
            "Self-help groups under the National Rural Livelihoods Mission convert isolated households into "
            "collective bargaining and mutual insurance.",
            "The 2020 migrant journey home revealed workers connected by mobile phones yet unsupported by any "
            "local institution.",
            "The Rajasthan Platform Based Gig Workers Act, 2023 responded to workers coordinated by applications "
            "but represented by nobody.",
            "Kerala's library and reading-room movement built dense civic association long before digital "
            "connectivity reached villages.",
        ],
        "counterview": (
            "Technology also rescues the isolated. Telemedicine reaches villages without specialists, screen "
            "readers and captions widen disability access, and diaspora families sustain daily intimacy across "
            "continents. Isolation is produced mainly by insecure work, unaffordable housing and weak local "
            "institutions, so blaming connectivity mistakes a visible instrument for the underlying cause."
        ),
        "conclusion": (
            "A society is connected when somebody is answerable for the person who disappears from view. India "
            "should judge its digital achievement by whether workplaces, neighbourhoods and panchayats still hold "
            "people, not by data consumption."
        ),
    },
    "Efficiency without empathy is an incomplete public virtue.": {
        "thesis": (
            "Efficiency is a real moral good, because wasted public money is stolen from somebody's clinic or "
            "classroom. It turns incomplete when the measured objective ignores whoever is excluded by the very "
            "design that raised throughput. The proposition asks administration to count the person turned away, "
            "not only the transaction successfully completed."
        ),
        "structure": [
            "Defend efficiency as an ethical obligation attached to scarce public resources.",
            "Show how metrics select what is easy to count and hide exclusion errors.",
            "Examine welfare delivery, where authentication sharpens targeting yet denies the most vulnerable.",
            "Treat dignity as an outcome variable rather than a matter of courtesy.",
            "Conclude with fallback, appeal and human discretion designed into the system.",
        ],
        "dimensions": [
            "Measurement rewards throughput and leakage reduction, while exclusion stays invisible because the "
            "excluded rarely appear anywhere in the administrative data.",
            "Rights-based welfare assumes entitlement failure requires a remedy, not an apology from an otherwise "
            "efficient delivery machine.",
            "Market efficiency allocates by willingness to pay, a poor guide precisely where need is greatest and "
            "purchasing power smallest.",
            "Dignity converts service into citizenship, since treatment at the counter decides whether an "
            "entitled person ever returns to claim again.",
        ],
        "examples": [
            "Biometric authentication failures in Jharkhand denied rations to entitled households despite "
            "improved system-level leakage statistics.",
            "The National Food Security Act, 2013 created a legal entitlement with a food security allowance when "
            "supply fails.",
            "The Prohibition of Employment as Manual Scavengers Act, 2013 treats sanitation work as a question of "
            "human dignity.",
            "MGNREGA's dated receipts and unemployment allowance make administrative delay legally costly rather "
            "than merely regrettable.",
        ],
        "counterview": (
            "Empathy without efficiency is equally incomplete, and often crueller. Discretionary kindness at the "
            "counter historically meant patronage, favouritism and bribes, while unreliable supply chains starved "
            "genuine claimants. Rules, audits and technology reduced arbitrary power precisely because compassion "
            "was distributed unevenly. The requirement is humane rules, not a return to benevolent discretion."
        ),
        "conclusion": (
            "A competent state should be judged on two ledgers: what it delivered, and whom it lost. Offline "
            "fallback, published appeal outcomes and respectful treatment are the cheapest evidence that "
            "efficiency has kept its conscience."
        ),
    },
    "Institutions become strong when ordinary people can question them.": {
        "thesis": (
            "Institutional strength is commonly mistaken for insulation. An organisation that cannot be "
            "interrogated loses its early-warning system and learns of failure only through crisis. Openness to "
            "questioning by ordinary citizens supplies correction, legitimacy and information that hierarchy "
            "cannot generate internally. Strength on this reading means resilience under scrutiny rather than "
            "immunity from it."
        ),
        "structure": [
            "Contrast strength as insulation with strength as tested resilience.",
            "Show information value: complaints reveal failures internal reporting suppresses.",
            "Show legitimacy value: answerable institutions retain compliance during crisis.",
            "Test the limit, where hostile or bad-faith questioning paralyses administrative capacity.",
            "Specify design that channels scrutiny into correction rather than defensive inaction.",
        ],
        "dimensions": [
            "Transparency instruments work only when disclosed information leads to a named official, a deadline "
            "and a consequence for failure.",
            "Enforceable rights let people without political influence question authority, converting protest "
            "into a claim a court must answer.",
            "Participation adds local knowledge, because users of a school, canal or clinic detect failure far "
            "earlier than a visiting inspector.",
            "Trust compounds from answerability, which is why credible institutions survive emergencies through "
            "cooperation instead of coercion.",
        ],
        "examples": [
            "The Mazdoor Kisan Shakti Sangathan's public hearings in Rajasthan turned muster rolls into evidence "
            "and prefigured the RTI Act.",
            "Social audits of MGNREGA works in Andhra Pradesh institutionalised village-level verification of "
            "wages and measurements.",
            "Article 32, described by Ambedkar as the soul of the Constitution, lets an individual question the "
            "state directly.",
            "Comptroller and Auditor General reports allow parliamentary committees to interrogate executive "
            "spending after the fact.",
        ],
        "counterview": (
            "Unlimited questioning can also disable. Continuous litigation, vexatious complaints and trial by "
            "social media exhaust scarce administrative capacity and push officials towards defensive inaction, "
            "where deciding nothing becomes safest. Institutions therefore need scrutiny that is timely, "
            "evidence-based and remedial, plus protection for honest officers deciding under uncertainty."
        ),
        "conclusion": (
            "The strongest Indian institutions are those a landless labourer can question and still receive an "
            "answer from. Building that capability is a sounder investment than shielding institutions from "
            "criticism in the name of stability."
        ),
    },
    "The future belongs not to those who predict it, but to those who prepare fairly for it.": {
        "thesis": (
            "Forecasts are cheap and frequently wrong; preparation is expensive and inherently distributive. The "
            "decisive word here is fairly, because a society can prepare superbly for its wealthy and abandon its "
            "poor to the identical shock. Real foresight is measured by whose exposure falls, not by whose "
            "prediction proved closest."
        ),
        "structure": [
            "Show why prediction is a weak foundation for policy under deep uncertainty.",
            "Replace it with robustness: options that work across several plausible futures.",
            "Introduce fairness, since preparedness is distributed unequally by wealth, region and generation.",
            "Locate capacity along the federal chain from national mission to municipal ward.",
            "Close on obligations owed to people who cannot yet vote.",
        ],
        "dimensions": [
            "Climate adaptation demands local protocols, because heat, flood and cyclone risk vary by ward, "
            "occupation and the quality of housing.",
            "Skill preparation is fair only when training connects to certification and to employers who actually "
            "recognise the acquired competence.",
            "Federal readiness depends on money and staff at the level nearest the hazard, not on plans drafted "
            "far above the affected district.",
            "Intergenerational justice binds present groundwater, coal and land decisions to persons entirely "
            "absent from today's bargaining table.",
        ],
        "examples": [
            "Odisha's mass evacuation before Cyclone Phailin in 2013 contrasted sharply with the toll of the 1999 "
            "super cyclone.",
            "Ahmedabad's Heat Action Plan of 2013 linked temperature forecasts to hospitals, water points and "
            "outdoor work schedules.",
            "The Disaster Management Act, 2005 created national, state and district authorities with defined "
            "statutory duties.",
            "India's announced net-zero target for 2070 commits present governments to burdens falling largely on "
            "future citizens.",
        ],
        "counterview": (
            "Preparation can entrench inequality behind a fair-sounding label. Resilience spending often protects "
            "high-value property first, and relief formulas favour claimants with documented assets and clear "
            "titles. Fairness is not achieved by adding another plan; it requires deciding in advance who is "
            "protected first and publishing that priority before the disaster arrives."
        ),
        "conclusion": (
            "India's preparedness will be judged by the informal worker in a tin-roofed room during a heatwave. "
            "Where her risk falls, foresight has become policy; where it does not, prediction has merely been "
            "rehearsed."
        ),
    },
    "Silence may preserve peace for a day and injustice for a generation.": {
        "thesis": (
            "Silence buys immediate calm at compounding cost. What is not named cannot be remedied, and an "
            "unremedied wrong hardens into custom that later generations struggle even to recognise as wrong. The "
            "proposition contrasts the short-run value of quiet with the long-run price of a normalised injury."
        ),
        "structure": [
            "Distinguish prudent restraint from complicit silence.",
            "Show how unspoken wrongs acquire the authority of tradition.",
            "Trace speech that changed law, from social reform to workplace rights.",
            "Concede the genuine value of timing and confidentiality in negotiation and communal tension.",
            "Offer a test for the point at which silence becomes complicity.",
        ],
        "dimensions": [
            "Moral courage is costly and unequally distributed, since whoever is best placed to see a wrong is "
            "often least able to survive reporting it.",
            "Reform movements converted private suffering into public argument, which is why testimony almost "
            "always precedes remedial legislation.",
            "Diplomatic quiet can protect negotiations and lives, yet permanent silence about atrocity signals "
            "that violation carries no reputational price.",
            "Law responds to articulated harm, so an injury lacking a public name possesses neither a remedy nor "
            "even a statistic.",
        ],
        "examples": [
            "The Vishaka guidelines of 1997 followed Bhanwari Devi's refusal to stay silent about sexual violence "
            "at work.",
            "Satyendra Dubey's murder in 2003 after exposing highway corruption led towards whistle-blower "
            "protection legislation in 2014.",
            "Rammohan Roy's public campaign against sati showed reform requiring open argument rather than "
            "private moral discomfort.",
            "The Protection of Children from Sexual Offences Act, 2012 made reporting a legal duty instead of a "
            "personal choice.",
        ],
        "counterview": (
            "Speech is not automatically just. Premature disclosure has collapsed hostage negotiations, and "
            "public accusation without evidence has destroyed innocent reputations and inflamed communal "
            "violence. Rumour amplified as courage kills. The defensible claim is narrower: silence is culpable "
            "when it shields the powerful, and prudent only when it shields the vulnerable."
        ),
        "conclusion": (
            "Judge silence by its beneficiary. Quiet that protects a perpetrator or an institution is complicity "
            "dressed as civility; quiet that protects a survivor or an ongoing remedy may be the braver choice."
        ),
    },
    "The value of knowledge lies partly in knowing its limits.": {
        "thesis": (
            "Knowledge grows dangerous when it forgets its own boundary conditions. A model trained on one "
            "context, a statistic collected for one purpose, or an expert judgement offered beyond its field "
            "carries the authority of evidence without its warrant. Knowing the limit is therefore part of the "
            "knowledge, not a concession made against it."
        ),
        "structure": [
            "Explain that every finding carries a domain of validity.",
            "Show forecasting failures as boundary failures rather than mere arithmetic errors.",
            "Examine expert advice in government and the problem of unstated assumptions.",
            "Discuss decision-making under uncertainty through precaution and revisability.",
            "Warn against the opposite error of dismissing expertise altogether.",
        ],
        "dimensions": [
            "Scientific claims remain conditional on method, sample and context, so transferring them across "
            "settings silently changes what is being asserted.",
            "Governance must decide before evidence matures, which makes stated assumptions and a review date "
            "part of honest technical advice.",
            "Expertise deserves weight without deference, because specialists share the incentives, blind spots "
            "and institutional interests of their own field.",
            "Uncertainty is manageable through precaution, staged commitment and reversible choices rather than "
            "through a performance of confidence.",
        ],
        "examples": [
            "Early COVID-19 projections in 2020 varied enormously, and policy improved once models were published "
            "with assumptions and ranges.",
            "Vellore Citizens Welfare Forum (1996) read the precautionary principle into Indian environmental "
            "jurisprudence.",
            "Environmental impact assessments lose credibility when project proponents commission the studies "
            "establishing acceptable risk.",
            "Groundwater estimates based on average recharge concealed local exhaustion across Punjab and parts "
            "of western India.",
        ],
        "counterview": (
            "Excessive humility is exploited. Regulated industries routinely amplify residual uncertainty to "
            "postpone action, and officials invoke complexity to escape accountable choice, while citizens need "
            "usable guidance rather than hedged prose. Acknowledging limits must therefore accompany a clear "
            "recommendation, a named decision-maker and a date for reconsideration."
        ),
        "conclusion": (
            "Mature knowledge states what it knows, what it assumes and what would falsify it. In public life "
            "that discipline converts expertise from an authority claim into an accountable input citizens can "
            "weigh for themselves."
        ),
    },
    "Identity is a home when open, and a prison when sealed.": {
        "thesis": (
            "Belonging supplies language, memory and the confidence to act, which is why identity functions as a "
            "home. It becomes confinement once membership is policed, exit is punished and the group's boundary "
            "matters more than its members' freedom. The proposition measures identity by whether a person may "
            "leave it, question it or combine it."
        ),
        "structure": [
            "Establish the enabling functions of belonging.",
            "Identify what seals an identity: policed exit, internal hierarchy, external threat.",
            "Test India's federal and constitutional accommodation of plural identity.",
            "Examine migration, where identity travels but entitlements often do not.",
            "Conclude on rights of exit and overlapping membership.",
        ],
        "dimensions": [
            "Culture supplies usable competence and confidence, since language, craft and ritual are resources a "
            "person actually deploys in daily life.",
            "Pluralism sustains common citizenship without demanding uniformity, provided group authority never "
            "overrides an individual's constitutional rights.",
            "Nationalism becomes civic or exclusionary depending on whether membership rests on allegiance to "
            "shared institutions or on ascribed descent.",
            "Migration tests openness, because domicile rules, language and documentation decide whether a "
            "newcomer is treated as citizen or guest.",
        ],
        "examples": [
            "The States Reorganisation Act, 1956 accommodated linguistic identity within the Union instead of "
            "treating it as incipient secession.",
            "The Sixth Schedule and Article 371 provisions protect distinct tribal and regional arrangements "
            "inside one constitutional framework.",
            "One Nation One Ration Card portability lets a migrant claim food entitlements outside her home "
            "state.",
            "The Eighth Schedule's recognition of twenty-two languages supports plural public life without "
            "displacing shared civic identity.",
        ],
        "counterview": (
            "Openness is often demanded only of the weak. Small linguistic and tribal communities that dissolve "
            "their boundaries frequently lose land, language and bargaining power to a dominant culture that "
            "never opens itself in return. Some closure is protective, and constitutional safeguards exist "
            "precisely to secure it for vulnerable groups."
        ),
        "conclusion": (
            "A defensible identity is one a member could revise without exile and a stranger could enter without "
            "humiliation. India's constitutional design aims at exactly that combination of protection without "
            "imprisonment."
        ),
    },
    "Care is an economic infrastructure hidden in private life.": {
        "thesis": (
            "Every worker who reaches an office was fed, nursed and raised by labour national accounts never "
            "priced. Care qualifies as infrastructure because output collapses without it, yet it is classified "
            "as affection rather than production and its cost is charged silently to women. The proposition "
            "reclassifies a private duty as a public input."
        ),
        "structure": [
            "Show that care meets the functional definition of infrastructure.",
            "Explain how measurement failure produces policy failure.",
            "Connect the care burden to women's employment and health outcomes.",
            "Consider public provision, workplace design and social security responses.",
            "Address the risk of professionalising care badly.",
        ],
        "dimensions": [
            "Time-use evidence shows unpaid domestic and care work absorbing a large share of women's day, "
            "directly constraining paid employment and rest.",
            "Female labour force participation responds to childcare, eldercare and safe transport at least as "
            "strongly as it responds to wages or training.",
            "Health systems quietly depend on family caregivers for nursing, medication adherence and "
            "rehabilitation after a patient is discharged.",
            "Social policy can socialise part of the burden through creches, parental leave, old-age support and "
            "decent wages for care workers.",
        ],
        "examples": [
            "India's Time Use Survey of 2019 recorded women spending far more time than men on unpaid domestic "
            "work.",
            "MGNREGA's worksite creche requirement recognises childcare as a condition of women's participation "
            "in public works.",
            "Accredited Social Health Activists perform community health duties for honoraria rather than regular "
            "wages and benefits.",
            "The Maternity Benefit Amendment Act, 2017 extended paid leave while concentrating the cost on "
            "formal-sector employers.",
        ],
        "counterview": (
            "Treating care as infrastructure invites two errors. Marketised care can become low-paid, insecure "
            "work performed largely by poorer women for wealthier households. And measuring care does not "
            "redistribute it: without men's participation and enforceable employer obligation, valuation may "
            "simply add statistics to an unchanged burden."
        ),
        "conclusion": (
            "The practical test is whether caring costs a woman her job. Creches, portable entitlements, decent "
            "pay for care workers and shared domestic responsibility would turn a hidden subsidy into a "
            "recognised, financed public input."
        ),
    },
    "India's demographic future depends more on capability than on numbers.": {
        "thesis": (
            "A young population is an opportunity only where the young can read, stay healthy, find productive "
            "work and choose their own lives. Numbers create potential; capability converts it into output and "
            "freedom. The proposition locates India's demographic outcome in classrooms, clinics and workplaces "
            "rather than in population arithmetic."
        ),
        "structure": [
            "State the demographic window and its finite duration.",
            "Show foundational learning and nutrition as the binding constraints.",
            "Analyse the gap between educational attainment and productive employment.",
            "Treat women's participation as the largest unused capability.",
            "Note sharp divergence across states within one national transition.",
        ],
        "dimensions": [
            "Foundational literacy and numeracy determine whether additional years of schooling yield competence "
            "or merely accumulate certificates.",
            "Nutrition and anaemia shape cognition and stamina, making health spending an economic policy rather "
            "than only a welfare transfer.",
            "Employment quality matters more than headcount, since informal low-productivity work cannot absorb "
            "rising educational aspiration.",
            "Women's low participation withholds nearly half the potential workforce, turning safety, care "
            "support and social norms into macroeconomic variables.",
        ],
        "examples": [
            "ASER surveys have repeatedly found many rural children in higher grades unable to read a Standard II "
            "text.",
            "NIPUN Bharat, launched in 2021, targets foundational literacy and numeracy as a measurable national "
            "mission.",
            "Kerala's early investment in schooling and public health preceded both its demographic transition "
            "and its human development record.",
            "National Family Health Survey rounds show persistent anaemia among adolescent girls and women of "
            "reproductive age.",
        ],
        "counterview": (
            "Capability without demand becomes frustration. Better-trained graduates entering a slow-growing "
            "labour market produce educated unemployment and out-migration, as several Indian states already "
            "show. Skilling cannot substitute for manufacturing, urban services and small-firm growth, so "
            "supply-side capability and demand-side investment must advance together."
        ),
        "conclusion": (
            "India's advantage is temporary and unevenly spread across states. Whether it becomes a dividend "
            "depends on foundational learning, women's employment and job creation arriving before the "
            "working-age share begins to shrink."
        ),
    },
    "Climate resilience is a test of federalism as much as of technology.": {
        "thesis": (
            "Panels, forecasts and flood models are necessary but inert without a government close enough to act "
            "on them. A warning must become an evacuation and heat data must become a changed work schedule, and "
            "those conversions happen in districts and wards. The proposition relocates climate capacity from "
            "laboratories to the federal chain of command."
        ),
        "structure": [
            "Show adaptation as inherently local while mitigation remains national and global.",
            "Trace the chain from national mission to municipal implementation.",
            "Examine finance and staffing as the binding constraint on local action.",
            "Add equity, since exposure and recovery differ sharply within one city.",
            "Conclude on coordination achieved without recentralisation.",
        ],
        "dimensions": [
            "Adaptation is place-specific, since drainage, heat stress and crop damage differ across districts "
            "even inside a single state.",
            "Fiscal devolution decides capacity, because assigned functions without predictable funds and trained "
            "staff produce plans instead of protection.",
            "Scientific inputs need translation, as forecasts help only when converted into local protocols for "
            "hospitals, schools and workplaces.",
            "Equity determines outcomes, since informal settlements and outdoor workers face the highest exposure "
            "and the slowest recovery.",
        ],
        "examples": [
            "State Action Plans on Climate Change created state frameworks whose implementation still depends on "
            "district and municipal capacity.",
            "Ahmedabad's municipal heat plan assigned duties to hospitals, water suppliers and labour departments "
            "during declared alerts.",
            "The Fifteenth Finance Commission provided distinct mitigation and response windows within disaster "
            "risk management funding.",
            "Odisha's cyclone shelters and trained community volunteers turned central forecasts into completed "
            "evacuations.",
        ],
        "counterview": (
            "Localism has limits. Basins, coastlines and airsheds cross municipal and state boundaries, and small "
            "local bodies can neither finance protective infrastructure nor resist powerful land interests. Some "
            "resilience needs central standards, interstate coordination and financing that overrides local "
            "preference, so devolved execution requires binding national norms."
        ),
        "conclusion": (
            "Resilience is federal engineering. It needs a mayor with money, a district officer with usable data, "
            "and a national framework that makes both obligations mandatory rather than merely exemplary."
        ),
    },
    "Digital public infrastructure must expand agency, not merely transactions.": {
        "thesis": (
            "Counting payments, authentications and enrolments measures throughput rather than empowerment. "
            "Digital public infrastructure enlarges agency only when a person can obtain a service without an "
            "intermediary, understand what was done with her data, correct an error and carry her credentials "
            "elsewhere. The proposition demands a citizen-side test of success."
        ),
        "structure": [
            "Define agency as choice, portability, comprehension and remedy.",
            "Acknowledge the genuine scale achievement of India's digital rails.",
            "Identify exclusion at the last mile.",
            "Examine privacy and consent as conditions of agency rather than obstacles.",
            "Address market concentration and the role of open standards.",
        ],
        "dimensions": [
            "Inclusion fails at the margin, where connectivity, worn fingerprints, missing documents and language "
            "exclude those most dependent on the service.",
            "Privacy protects agency, since a person unable to know or contest data use cannot meaningfully "
            "consent to anything.",
            "Open standards stop public rails from becoming private gatekeeping by keeping switching costs low "
            "and entry genuinely feasible.",
            "Service delivery requires traceability, because a failed transaction without receipt, timeline and "
            "appeal is indistinguishable from denial.",
        ],
        "examples": [
            "UPI's interoperable design lets small merchants accept payments without being captured by a single "
            "payment application.",
            "Puttaswamy (2017) requires legality, necessity and proportionality before the state intrudes upon "
            "informational privacy.",
            "The Open Network for Digital Commerce attempts to unbundle discovery from platform control in online "
            "retail.",
            "CoWIN issued vaccination certificates at national scale while relying on assisted registration for "
            "those without smartphones.",
        ],
        "counterview": (
            "Agency language can excuse inaction. Transaction efficiency itself delivers welfare: direct benefit "
            "transfers cut delay and diversion, and instant payments lowered the cost of credit and trade for "
            "small firms. Insisting on ideal empowerment before scaling would have denied millions the concrete "
            "gains already achieved."
        ),
        "conclusion": (
            "Judge digital infrastructure by the citizen with the weakest connection and the thinnest paperwork. "
            "If she obtains the service, corrects her record and complains successfully, the system has expanded "
            "freedom rather than volume."
        ),
    },
    "Agricultural prosperity requires moving from output security to income and ecological security.": {
        "thesis": (
            "The postcolonial food emergency justified maximising tonnage, and that mission succeeded. The "
            "binding problems now are farm income, price volatility, aquifer depletion and soil health, none of "
            "which improve automatically with higher yields. The proposition asks for a changed objective for "
            "agricultural policy, not a repudiation of its earlier achievement."
        ),
        "structure": [
            "Credit the output-security era for ending dependence on imported grain.",
            "Show why yield growth no longer resolves stagnant farm incomes.",
            "Read subsidies, procurement and cropping incentives as ecological signals.",
            "Examine risk management and diversification as income strategies.",
            "Sequence reform so that transition does not impoverish the cultivator.",
        ],
        "dimensions": [
            "Marketing reform matters because realised income depends on price, storage and market access rather "
            "than on physical production alone.",
            "Water pricing and free power push cultivation towards thirsty crops in regions whose aquifers cannot "
            "sustain that choice.",
            "Risk instruments such as insurance, credit and price support decide whether a bad season becomes "
            "indebtedness or a manageable setback.",
            "Diversification into millets, horticulture, livestock and agroforestry spreads income sources while "
            "reducing ecological pressure at the same time.",
        ],
        "examples": [
            "Green Revolution procurement in Punjab and Haryana secured national grain supply while entrenching "
            "paddy in a semi-arid belt.",
            "Punjab's Preservation of Subsoil Water Act, 2009 delayed paddy transplanting to cut "
            "evaporation-driven groundwater extraction.",
            "Operation Flood built farmer-owned dairy cooperatives that raised rural incomes through processing "
            "and marketing.",
            "The International Year of Millets in 2023 promoted crops requiring far less irrigation than rice in "
            "dryland regions.",
        ],
        "counterview": (
            "Ecological reform can become a middle-class demand financed by farmers. Withdrawing power subsidies "
            "or assured procurement without a substitute income transfers risk to cultivators carrying thin "
            "margins and heavy debt. Sequencing is therefore decisive: assured markets, remunerative prices for "
            "alternative crops and credible income support must precede withdrawal."
        ),
        "conclusion": (
            "Food security remains non-negotiable, yet it is now compatible with lower water use and higher farm "
            "incomes. Reform must change what agricultural policy rewards without gambling with the farmer's "
            "income or the nation's plate."
        ),
    },
    "A nation is secure when its citizens trust both borders and institutions.": {
        "thesis": (
            "Military capability deters external coercion, but a state that forfeits its citizens' confidence "
            "becomes vulnerable from within: intelligence dries up, compliance falls and rumour outruns official "
            "communication. Security is thus two-sided, requiring credible defence alongside institutions whose "
            "fairness citizens can verify. The proposition joins strength abroad to legitimacy at home."
        ),
        "structure": [
            "Define security as capability combined with cohesion.",
            "Show internal legitimacy as an operational rather than sentimental asset.",
            "Examine policing, rights and minority confidence.",
            "Add the cyber and information domains, where trust is the target.",
            "Balance necessary secrecy against institutional accountability.",
        ],
        "dimensions": [
            "Deterrence rests on capability and credibility, which require sustained modernisation, logistics and "
            "indigenous industrial depth over decades.",
            "Rights protection is a security asset, because populations expecting fair treatment cooperate with "
            "police and report emerging threats.",
            "Social cohesion decides whether a provocation stays an incident or becomes a riot, making equal "
            "protection a counter-escalation instrument.",
            "Cyber threats attack confidence directly, since strikes on payment systems, hospitals and "
            "information environments aim at public trust.",
        ],
        "examples": [
            "Prakash Singh (2006) directed police reforms meant to insulate investigation from political "
            "interference and improve public confidence.",
            "The 2020 cyber incident affecting Mumbai's power supply showed civilian infrastructure as a "
            "strategic target.",
            "CERT-In's directions of 2022 sought faster national visibility of cybersecurity incidents across "
            "critical sectors.",
            "The Mizo Accord of 1986 converted an insurgency into constitutional politics through negotiated "
            "political accommodation.",
        ],
        "counterview": (
            "Security sometimes requires acting against public opinion. Counter-terror operations, surveillance "
            "of hostile networks and negotiations with armed groups cannot always be transparent or popular, and "
            "excessive proceduralism costs lives. Trust must therefore be built through oversight by accountable "
            "institutions rather than through disclosure of every operational decision."
        ),
        "conclusion": (
            "A secure India needs a defended frontier and a citizen who believes her local police station will "
            "treat her fairly. Neglecting either produces a state that is armed but brittle, or trusted but "
            "exposed."
        ),
    },
    "Urbanisation will be India's opportunity only if cities become governable.": {
        "thesis": (
            "Cities concentrate productivity because proximity lowers the cost of exchange and learning. That "
            "advantage is cancelled when commuting is unreliable, housing unaffordable, drainage broken and no "
            "elected authority answerable for the city as a whole. The proposition makes governance capacity, not "
            "the pace of urban growth, the decisive variable."
        ),
        "structure": [
            "Explain agglomeration gains and the congestion costs that offset them.",
            "Show the gap between the 74th Amendment's promise and actual devolution.",
            "Analyse municipal finance as the foundation of everything else.",
            "Take housing and mobility as the tests citizens experience daily.",
            "Add climate risk as the emerging stress test of urban governance.",
        ],
        "dimensions": [
            "Municipal revenue remains small relative to municipal responsibility, leaving cities dependent on "
            "transfers and unable to plan over long horizons.",
            "Fragmented authority defeats accountability, since water, transport, policing and land often answer "
            "to different state agencies.",
            "Housing policy decides whether workers live near employment or surrender income and hours to "
            "peripheral commuting.",
            "Urban climate risk concentrates where drainage was built over and where housing quality cannot "
            "buffer heat or flooding.",
        ],
        "examples": [
            "The 74th Amendment of 1992 created urban local bodies, yet functions, funds and functionaries were "
            "devolved unevenly.",
            "The Reserve Bank's report on municipal finances found Indian city revenues to be roughly one per "
            "cent of GDP.",
            "Odisha's Jaga Mission granted land rights to slum households and upgraded settlements in place "
            "rather than relocating them.",
            "Mumbai's deluge of 2005 exposed the consequences of building over the Mithi river's drainage "
            "capacity.",
        ],
        "counterview": (
            "Governability is not achieved by adding mayors. Empowered city governments lacking revenue, "
            "technical staff or political competition can be captured by builders and contractors, and "
            "metropolitan problems spill across municipal limits. Devolution needs own revenue, professional "
            "cadres, transparent planning and metropolitan coordination, or it simply relocates dysfunction."
        ),
        "conclusion": (
            "India will urbanise regardless of policy; the choice is between productive cities and congested "
            "ones. Empowered, financed and accountable city governments separate agglomeration as an asset from "
            "agglomeration as a liability."
        ),
    },
    "Strategic autonomy is sustained by domestic capability.": {
        "thesis": (
            "Autonomy is the ability to refuse. A state dependent on one supplier for weapons, chips, fuel or "
            "finance may announce independence but cannot practise it under pressure. The proposition identifies "
            "capability, meaning industrial, technological and energy depth, as the material foundation that "
            "turns a declared posture into a usable one."
        ),
        "structure": [
            "Define autonomy as issue-based choice rather than equidistance.",
            "Trace the evolution from non-alignment to contemporary multi-alignment.",
            "Map real dependencies in defence, technology and energy.",
            "Argue that capability rather than rhetoric converts choice into leverage.",
            "Concede the limits of autarky and the necessity of partnerships.",
        ],
        "dimensions": [
            "Defence industrial depth decides whether procurement choices survive sanctions, denial of spares or "
            "wartime disruption of supply.",
            "Technological capability in semiconductors, space and telecommunications determines who writes "
            "standards and who merely adopts them.",
            "Energy dependence constrains diplomacy, because concentrated import sourcing converts a "
            "foreign-policy choice into an economic vulnerability.",
            "Diplomacy multiplies capability through coalitions, yet partners bargain harder with a state unable "
            "to produce credible alternatives.",
        ],
        "examples": [
            "Continued Russian energy and defence purchases alongside Quad cooperation illustrate issue-based "
            "alignment in practice.",
            "ISRO's launch and interplanetary programme, including Chandrayaan-3 in 2023, gives India independent "
            "access to space.",
            "The Semiconductor Mission announced in 2021 addresses a supply chain where dependence is "
            "strategically consequential.",
            "The International Solar Alliance, launched with France in 2015, shows India building institutions "
            "rather than only joining them.",
        ],
        "counterview": (
            "Self-reliance can degenerate into costly protection. Import substitution in the licence-raj decades "
            "produced expensive low-quality industry and slower growth, and no country manufactures an entire "
            "aerospace or semiconductor chain alone. Modern capability is built inside trusted networks, so "
            "autonomy that rejects interdependence would shrink India's real options."
        ),
        "conclusion": (
            "Strategic autonomy is a budget line before it is a doctrine. Research funding, manufacturing depth "
            "and diversified energy sourcing decide whether India's declared independence of judgement survives "
            "its first serious test."
        ),
    },
    "Public health is built before a patient reaches a hospital.": {
        "thesis": (
            "Hospitals treat individuals; public health protects populations. Most avoidable deaths are settled "
            "earlier by clean water, immunisation, nutrition, air quality and early detection, long before any "
            "admission. The proposition corrects an inversion in which health policy is measured by beds and "
            "machines rather than by the conditions keeping people out of them."
        ),
        "structure": [
            "Distinguish medical care from public health as different production functions.",
            "Show that the largest historical mortality gains came from prevention.",
            "Examine primary care and continuity as the missing middle.",
            "Add surveillance as the early-warning layer.",
            "Address the political economy that favours visible hospital construction.",
        ],
        "dimensions": [
            "Preventive measures such as immunisation, safe water and vector control avert disease at a small "
            "fraction of treatment cost.",
            "Sanitation generates health externalities, since one household's practice changes the infection "
            "burden of an entire settlement.",
            "Primary care supplies continuity, screening and referral, thereby reducing avoidable "
            "hospitalisation and catastrophic out-of-pocket expenditure for poorer families.",
            "Surveillance converts scattered cases into an actionable signal, provided reporting is timely, "
            "trusted and shielded from misuse.",
        ],
        "examples": [
            "India was certified polio-free in 2014 after sustained immunisation, surveillance and community "
            "mobilisation.",
            "Accredited Social Health Activists extended community-level health contact under the National Rural "
            "Health Mission from 2005.",
            "The Swachh Bharat Mission from 2014 treated sanitation as a determinant of diarrhoeal disease and "
            "child nutrition.",
            "Health and wellness centres under Ayushman Bharat sought to strengthen comprehensive primary care "
            "alongside hospital insurance.",
        ],
        "counterview": (
            "Prevention cannot substitute for treatment. Cancer, trauma, cardiac emergencies and complicated "
            "childbirth demand equipped hospitals and specialists, and insurance shields families from "
            "catastrophic bills that primary care cannot avert. India's deeper problem is not misallocation "
            "between the two, but chronic underfunding of the health system overall."
        ),
        "conclusion": (
            "The most efficient health rupee is usually spent before illness, but it must be added to hospital "
            "capacity rather than traded against it. Public health succeeds quietly, which is exactly why it "
            "stays politically underfunded."
        ),
    },
    "Equality sometimes requires treating unequal circumstances differently.": {
        "thesis": (
            "Identical treatment of unequally situated people reproduces the inequality it claims to ignore. One "
            "staircase, one medium of instruction or one competitive threshold offers formally equal access while "
            "functionally excluding some. The proposition defends differentiation justified by relevant "
            "disadvantage and publicly reasoned, not differentiation driven by preference or patronage."
        ),
        "structure": [
            "Distinguish formal equality, substantive equality and arbitrary discrimination.",
            "State the constitutional basis for reasonable classification.",
            "Apply it to caste disadvantage, disability and regional capacity.",
            "Identify limits of proportionality, review and continuing evidence.",
            "Warn against differentiation that becomes permanent entitlement without measurement.",
        ],
        "dimensions": [
            "Reasonable classification requires an intelligible differentia and a rational connection to the "
            "objective, which blocks arbitrary preference.",
            "Caste-based measures address structured historical exclusion, but need schooling and "
            "anti-discrimination enforcement to translate into outcomes.",
            "Disability rights show accommodation as a precondition of access, since a ramp or screen reader "
            "creates usable rather than notional equality.",
            "Fiscal federalism applies the same logic between states, transferring more to units with weaker "
            "revenue capacity and greater need.",
        ],
        "examples": [
            "Article 15(3) and Article 16(4) permit special provisions for women, children and backward classes "
            "within the equality code.",
            "Indra Sawhney (1992) upheld reservation while capping its extent and excluding the creamy layer from "
            "its benefit.",
            "The Rights of Persons with Disabilities Act, 2016 made reasonable accommodation a legal duty rather "
            "than a favour.",
            "Finance Commission formulas weight income distance so that poorer states receive larger per-capita "
            "central transfers.",
        ],
        "counterview": (
            "Differentiation carries real costs. Group-based preference can favour the better-off within a "
            "disadvantaged category, harden identity politics and burden individuals who inherited no advantage "
            "themselves. Without periodic evidence of continuing disadvantage, exclusion of the affluent and "
            "attention to underlying capability, equity measures ossify into a new distributive settlement."
        ),
        "conclusion": (
            "Equality is a judgement about relevant difference rather than a rule of sameness. India's "
            "constitutional method of stated grounds, proportionality and review protects against both blind "
            "uniformity and unexamined preference."
        ),
    },
    "Markets discover prices; societies must still decide values.": {
        "thesis": (
            "Prices aggregate willingness to pay and coordinate an economy no planner could match. But "
            "willingness to pay reflects existing wealth, ignores everyone absent from the transaction and cannot "
            "value a river, an unpaid caregiver or a dying craft. The proposition grants markets an "
            "indispensable informational role while reserving valuation for public deliberation."
        ),
        "structure": [
            "Credit markets with information and coordination that planning cannot replicate.",
            "Identify externalities, missing markets and unequal endowments as valuation failures.",
            "Illustrate through ecology, care work and cultural inheritance.",
            "Discuss regulation, public provision and rights as valuation instruments.",
            "Guard against romanticising political decision-making.",
        ],
        "dimensions": [
            "Price signals allocate scarce resources efficiently, which is why administered scarcity historically "
            "produced shortage, queues and rent-seeking.",
            "Ecological services remain unpriced until they fail, so aquifers, mangroves and clean air are "
            "consumed as though they were free.",
            "Unpaid care and subsistence work fall outside the production boundary, making much sustaining labour "
            "statistically invisible.",
            "Cultural inheritance carries option and existence value no current transaction reveals, because "
            "future generations cannot bid in today's market.",
        ],
        "examples": [
            "The Chipko movement of the 1970s asserted forest value that timber contracts and auction prices "
            "never captured.",
            "The National Green Tribunal, created in 2010, adjudicates environmental costs that private "
            "contracting parties externalise.",
            "Groundwater across western India is depleted because marginal pumping cost is near zero for each "
            "individual user.",
            "Public procurement of handloom and handicraft supports crafts whose market price rarely covers "
            "skilled artisanal time.",
        ],
        "counterview": (
            "Public valuation is not automatically wiser. Political prices, subsidies and controls have shielded "
            "influential lobbies, encouraged waste and produced the ecological damage they claimed to prevent, as "
            "free farm power shows. Societies decide values best by using market information honestly, pricing "
            "harm explicitly and admitting that regulation is never costless."
        ),
        "conclusion": (
            "Use markets to discover cost and public reasoning to decide worth. India's practical challenge is to "
            "price what harms, protect what markets cannot see, and avoid confusing either task with the other."
        ),
    },
    "A rule gains legitimacy when those bound by it can understand and challenge it.": {
        "thesis": (
            "Obedience obtained through incomprehension is compliance, not legitimacy. A rule people cannot read, "
            "written in a language they do not use and applied without notice or reasons, governs by fear of "
            "arbitrariness. The proposition makes comprehensibility and contestability internal features of a "
            "legitimate rule rather than administrative courtesies."
        ),
        "structure": [
            "State the conditions of legality: clarity, prospectivity, publicity and consistency.",
            "Add language and accessibility as practical conditions of publicity.",
            "Show due process as the machinery of challenge.",
            "Examine administrative practice, where most citizens actually meet the law.",
            "Concede that some technical complexity is unavoidable.",
        ],
        "dimensions": [
            "Vague rules delegate arbitrary power downward, since the officer at the point of application decides "
            "what the words will mean.",
            "Language access converts formal publication into real notice, especially where proceedings occur in "
            "a language litigants do not speak.",
            "Due process supplies challenge through notice, hearing, recorded reasons and an appeal that is "
            "affordable in practice rather than in theory.",
            "Administrative design settles legitimacy in daily life, because citizens encounter the state at "
            "counters far more often than in courtrooms.",
        ],
        "examples": [
            "Shreya Singhal (2015) struck down Section 66A of the Information Technology Act partly for vagueness "
            "and chilling effect.",
            "Maneka Gandhi (1978) demanded that procedure affecting liberty be fair, just and reasonable rather "
            "than merely prescribed.",
            "Article 348 keeps higher court proceedings in English, limiting direct comprehension for many Indian "
            "litigants.",
            "The pre-legislative consultation policy of 2014 sought public comment on draft laws before their "
            "introduction in Parliament.",
        ],
        "counterview": (
            "Simplicity has limits. Taxation, competition, financial regulation and environmental standards are "
            "genuinely technical, and over-simplified drafting creates loopholes sophisticated parties exploit "
            "against the public. Legitimacy may therefore require plain-language explanation and effective "
            "representation instead of the impossible goal of statutes every citizen reads unaided."
        ),
        "conclusion": (
            "A citizen should be able to learn what a rule requires, why it applied to her, and where to contest "
            "it. Meeting that modest standard would do more for legal legitimacy in India than most substantive "
            "amendments."
        ),
    },
    "Education should prepare citizens to revise answers, not merely remember them.": {
        "thesis": (
            "Memory is necessary, since nobody reasons from an empty mind. But schooling that ends at recall "
            "produces citizens who defend positions instead of testing them, and workers whose competence expires "
            "with their syllabus. The proposition asks education to teach the disciplined revision of belief in "
            "the light of new evidence."
        ),
        "structure": [
            "Defend organised knowledge as the raw material of thinking.",
            "Distinguish recall from the ability to evaluate and revise a claim.",
            "Link revisability to democratic argument and scientific method.",
            "Connect it to employability in rapidly changing labour markets.",
            "Address examination design as the real operative curriculum.",
        ],
        "dimensions": [
            "Assessment drives pedagogy, so high-stakes recall examinations make teaching to memory an entirely "
            "rational classroom response.",
            "Democratic citizenship requires weighing competing claims, a trainable skill rather than an "
            "automatic by-product of basic literacy.",
            "Scientific temper is a habit of testing and updating, not a stock of scientific facts held with "
            "unexamined confidence.",
            "Occupational skills now change within a single career, making the capacity to relearn more durable "
            "than any certified competence.",
        ],
        "examples": [
            "Article 51A(h) places developing scientific temper, humanism and the spirit of reform among the "
            "fundamental duties.",
            "The National Education Policy of 2020 emphasises competency-based assessment over examinations "
            "rewarding memorisation.",
            "ASER findings show grade progression alone failing to deliver comprehension, exposing the limits of "
            "recall-focused schooling.",
            "Nalanda's tradition of formal disputation treated argument and refutation as central methods of "
            "learning.",
        ],
        "counterview": (
            "Critical thinking without content is posturing. A student unable to recall constitutional "
            "provisions, chronology or basic mathematics has nothing to reason with, and fashionable scepticism "
            "slides easily into contempt for expertise. In crowded classrooms with weak foundational learning, "
            "demanding debate before mastery risks widening the inequality it hopes to close."
        ),
        "conclusion": (
            "The educated citizen holds firm knowledge lightly enough to update it. India's reform will succeed "
            "only when examinations reward that ability, because assessment, not policy language, decides what "
            "teachers actually teach."
        ),
    },
    "India's energy transition is also a transition of jobs, regions and power.": {
        "thesis": (
            "Decarbonisation is usually discussed as technology substitution, yet coal sustains district "
            "economies, state revenues, railway finances and organised employment concentrated in a few eastern "
            "states. Replacing generating capacity therefore redistributes work, revenue and political influence. "
            "The proposition treats the transition as regional justice as much as engineering."
        ),
        "structure": [
            "Establish the scale and geography of India's coal dependence.",
            "Show renewables shifting activity towards different states and skill sets.",
            "Analyse grid, storage and flexibility as physical constraints on ambition.",
            "Introduce just-transition obligations to workers and mining districts.",
            "Sequence coal decline against reliability and livelihood readiness.",
        ],
        "dimensions": [
            "Coal districts depend on wages, contracts, mineral revenues and freight earnings that renewable "
            "projects do not reproduce in the same places.",
            "Renewable generation concentrates in high-irradiance and windy western states, shifting investment "
            "and employment across the federation.",
            "Variable generation needs transmission, storage and flexible demand, so capacity added without "
            "evacuation strands both power and capital.",
            "Just transition requires retraining, land repurposing and revenue substitution planned years before "
            "mines and plants actually close.",
        ],
        "examples": [
            "Jharkhand, Chhattisgarh and Odisha depend heavily on coal royalties, mining employment and District "
            "Mineral Foundation funds.",
            "Indian Railways has long cross-subsidised passenger fares from coal freight earnings, tying energy "
            "policy to transport finance.",
            "Bhadla solar park in Rajasthan demonstrates enormous generation scale with comparatively limited "
            "long-term local employment.",
            "The Ministry of Coal established a sustainable development cell in 2020 to address mine closure and "
            "environmental transition.",
        ],
        "counterview": (
            "Slowing the transition to protect coal regions creates its own victims. Air pollution, mining injury "
            "and climate damage fall on people who never received a coal wage, and delay raises long-run costs "
            "for every consumer. Justice for coal districts should be financed through transition planning, not "
            "purchased by postponing decarbonisation."
        ),
        "conclusion": (
            "India can decarbonise while keeping the lights on, but not while ignoring the districts that powered "
            "the country. Transition funds, retraining and revenue substitution are the price of a politically "
            "durable energy shift."
        ),
    },
    "The credibility of welfare depends on the dignity of delivery.": {
        "thesis": (
            "A programme that reaches the intended household only after humiliation, repeated visits and "
            "dependence on intermediaries has already failed part of its purpose. Welfare is a statement about "
            "membership, telling a citizen whether the state regards her as a rights-holder or a supplicant. "
            "Delivery, not design, is therefore the decisive test."
        ),
        "structure": [
            "Distinguish entitlement in statute from experience at the counter.",
            "Describe the frontline state as the constitution citizens actually meet.",
            "Assess technology as both dignity-enhancing and exclusion-creating.",
            "Establish grievance redress as the completion of an entitlement.",
            "Link dignity to take-up, trust and continued political support.",
        ],
        "dimensions": [
            "Legal entitlements shift the burden of failure onto the state, converting charity into a claim a "
            "citizen may actively enforce.",
            "Frontline workers embody the state, so a teacher, nurse or ration dealer determines whether policy "
            "feels like a right or a favour.",
            "Technology removes intermediaries and delay, yet authentication failure without fallback denies "
            "precisely the least documented claimants.",
            "Grievance systems complete an entitlement through receipts, deadlines, appeals and published "
            "outcomes rather than informal intercession.",
        ],
        "examples": [
            "The National Food Security Act, 2013 provides a food security allowance when entitled grain is not "
            "supplied.",
            "MGNREGA's dated receipts and wage-delay compensation make administrative failure a costed obligation "
            "rather than an excuse.",
            "Kudumbashree organises women's collectives in Kerala that deliver services while members retain "
            "control over decisions.",
            "Authentication failures at ration shops have denied entitled households food despite legally valid "
            "claims.",
        ],
        "counterview": (
            "Dignity is not free. Human-facing delivery is staff-intensive and discretion at the counter "
            "historically produced caste discrimination, bribery and political favouritism. Rules and biometric "
            "verification were adopted precisely because respect was granted selectively. The honest position "
            "requires enforceable rules together with adequately paid, supervised and respected frontline staff."
        ),
        "conclusion": (
            "Welfare survives politically when taxpayers believe it works and claimants believe it respects them. "
            "Receipts, fallback options and answered complaints deliver both, at a cost far below the programmes "
            "they protect."
        ),
    },
    "Cultural diversity survives through living livelihoods, not museum admiration alone.": {
        "thesis": (
            "A craft or language persists when practising it remains a viable way to live. Admiration, "
            "documentation and display can preserve an artefact while the community that produced it quietly "
            "stops transmitting the skill. The proposition moves cultural policy from conservation of objects "
            "towards the economics of the people who sustain traditions."
        ),
        "structure": [
            "Distinguish preservation of artefacts from continuity of practice.",
            "Show transmission as an economic decision taken by the next generation.",
            "Examine markets, credit and value capture for artisans.",
            "Treat language use in schooling and administration as livelihood-linked.",
            "Assess tourism and intellectual property as double-edged instruments.",
        ],
        "dimensions": [
            "Craft transmission depends on whether a young weaver can earn a decent living, since apprenticeship "
            "follows income rather than sentiment.",
            "A language survives through daily use in schooling, work and administration, not through official "
            "listing alone.",
            "Tourism can finance heritage while commodifying it, displacing residents or compressing a ritual "
            "into a shortened saleable spectacle.",
            "Intellectual property tools secure value for producers only where the community, rather than an "
            "intermediary, controls certification and marketing.",
        ],
        "examples": [
            "Darjeeling tea became India's first registered geographical indication, tying reputation to a "
            "defined producing region.",
            "Pochampally ikat and Channapatna toys carry geographical indication tags, though weaver and artisan "
            "incomes remain modest.",
            "The Eighth Schedule lists twenty-two languages, while many smaller tongues lack school instruction "
            "and steadily lose speakers.",
            "The National Education Policy of 2020 encourages mother-tongue instruction in early grades, "
            "supporting everyday language use.",
        ],
        "counterview": (
            "Markets can also destroy what they sustain. Commercial demand pushes artisans towards standardised "
            "tourist-friendly designs, and geographical indications have often enriched traders more than "
            "producers. Some traditions have no commercial future yet deserve public support, so documentation, "
            "subsidy and museum conservation remain necessary where livelihoods cannot be recreated."
        ),
        "conclusion": (
            "Culture is inherited by young people who can afford to practise it. Fair prices, producer-controlled "
            "certification and living use in classrooms and workplaces protect diversity better than admiration "
            "from behind glass."
        ),
    },
    "Disaster risk is often development risk accumulated over time.": {
        "thesis": (
            "Hazards are natural; disasters are largely built. Construction over drainage channels, unregulated "
            "slope cutting, neglected maintenance and settlements crowded onto marginal land convert ordinary "
            "rainfall or tremor into catastrophe. The proposition reframes disaster management as an audit of "
            "past development decisions rather than an emergency-service problem."
        ),
        "structure": [
            "Separate hazard, exposure and vulnerability as distinct components of risk.",
            "Show land-use and construction decisions manufacturing exposure.",
            "Show poverty and informality manufacturing vulnerability.",
            "Analyse maintenance and redundancy as unglamorous risk reduction.",
            "Position preparedness as the last line of defence, not the first.",
        ],
        "dimensions": [
            "Land-use decisions build exposure, because floodplains, wetlands and unstable slopes turn routine "
            "hazards into destructive events.",
            "Infrastructure resilience depends on lifecycle maintenance and redundancy rather than on the "
            "completion of new assets alone.",
            "Poverty converts a shock into a disaster, since insecure work, weak housing and absent savings block "
            "recovery afterwards.",
            "Preparedness saves lives only when warning, evacuation, shelter and transport form an unbroken and "
            "regularly rehearsed chain.",
        ],
        "examples": [
            "Chennai's flooding in 2015 followed construction over the Pallikaranai marsh and other natural water "
            "retention areas.",
            "Kerala's floods of 2018 revived debate over the Gadgil and Kasturirangan recommendations on Western "
            "Ghats land use.",
            "Joshimath's subsidence in 2023 highlighted construction and tunnelling pressure on fragile Himalayan "
            "slopes.",
            "Odisha's shelter network and trained volunteers cut cyclone mortality dramatically after the 1999 "
            "super cyclone.",
        ],
        "counterview": (
            "Not every disaster is a development failure. Extreme events such as the 2004 Indian Ocean tsunami or "
            "a great Himalayan earthquake would cause severe damage under any planning regime, and poorer "
            "societies face genuine trade-offs between immediate shelter needs and stringent standards. Risk can "
            "be reduced, but never planned away entirely."
        ),
        "conclusion": (
            "The cheapest disaster policy is an enforced building code and an unbuilt floodplain. India's "
            "recurring losses are largely the delayed invoice for development choices made a decade earlier."
        ),
    },
    "Foreign policy begins at home but cannot end there.": {
        "thesis": (
            "External influence is financed domestically, by economic weight, technological capability, social "
            "cohesion and credible institutions. Yet the problems most affecting Indian citizens, including "
            "climate, pandemics, supply chains and maritime security, cannot be solved inside the border. The "
            "proposition binds domestic capability to unavoidable international engagement."
        ),
        "structure": [
            "Show the domestic sources of external strength.",
            "Demonstrate that key national problems are transboundary by nature.",
            "Examine the diaspora as a two-way link carrying obligations.",
            "Analyse coalition-building and reform of global institutions.",
            "Balance autonomy against the real cost of cooperation.",
        ],
        "dimensions": [
            "Economic and technological capability set the ceiling on influence, since partners bargain over what "
            "a country can supply or withhold.",
            "The diaspora carries remittances, skills and goodwill, while low-wage migrant workers abroad require "
            "consular protection and enforceable labour agreements.",
            "Climate, oceans, cyberspace and pandemics are commons problems where purely national action cannot "
            "secure national outcomes.",
            "Multilateral engagement lets India shape rules instead of inheriting them, which matters most for "
            "developing-country interests.",
        ],
        "examples": [
            "India is the world's largest recipient of remittances, tying household incomes at home to migration "
            "policy abroad.",
            "Vaccine Maitri in 2021 converted domestic manufacturing capacity into diplomatic reach across "
            "developing countries.",
            "The Coalition for Disaster Resilient Infrastructure, launched in 2019, exports Indian disaster "
            "experience into global rule-making.",
            "Operation Ganga in 2022 evacuated Indian students from Ukraine, showing consular capacity as a "
            "foreign-policy obligation.",
        ],
        "counterview": (
            "Domestic capability does not translate automatically into influence. Wealthy states have repeatedly "
            "failed to convert resources into outcomes, while smaller countries punch above their weight through "
            "skilled diplomacy and agenda-setting. Conversely, commitments made ahead of domestic capacity can "
            "create obligations a country cannot honestly finance."
        ),
        "conclusion": (
            "India's external ambition is credible only insofar as its economy, institutions and technological "
            "base sustain it, yet confining policy to the border would surrender rule-making on precisely the "
            "issues shaping Indian lives."
        ),
    },
    "Artificial intelligence will reflect the institutions that govern it.": {
        "thesis": (
            "Algorithms encode the data, purposes and permissions they are given. A society with weak data "
            "protection, opaque procurement and no remedy for wrongful automated decisions will build systems "
            "that entrench its existing failures at speed and scale. The proposition treats artificial "
            "intelligence as an institutional mirror rather than an autonomous force."
        ),
        "structure": [
            "Reject technological determinism in favour of institutional shaping.",
            "Show how training data reproduces historical patterns of exclusion.",
            "Examine state use, procurement and the absence of appeal.",
            "Assess labour effects as a distributional question.",
            "Design regulation that permits innovation while assigning responsibility.",
        ],
        "dimensions": [
            "Training data encodes past decisions, so historical exclusion in lending, policing or hiring returns "
            "disguised as statistical objectivity.",
            "Public procurement functions as regulation, because what the state buys sets the market standard for "
            "auditability and explanation.",
            "Labour effects are distributional, since automation raises returns for some workers while devaluing "
            "routine cognitive tasks for others.",
            "Accountability requires a named human decision-maker and an accessible remedy whenever an automated "
            "output harms an identifiable person.",
        ],
        "examples": [
            "The Digital Personal Data Protection Act, 2023 established India's statutory framework for "
            "processing personal data.",
            "Puttaswamy (2017) supplies the proportionality standard against which intrusive automated state "
            "systems must be judged.",
            "Police use of facial recognition in Indian cities has proceeded with limited public rules on "
            "accuracy and redress.",
            "The IndiaAI Mission approved in 2024 funds compute, datasets and applications, shaping which uses "
            "become viable.",
        ],
        "counterview": (
            "Institutions also lag technology badly. Capability advances faster than any legislature can draft, "
            "leading models are developed outside national jurisdiction, and premature rules can freeze standards "
            "or entrench incumbents able to afford compliance. Governance must therefore rely on adaptive "
            "sandboxes, audits and liability rules instead of static prohibition."
        ),
        "conclusion": (
            "India will get the artificial intelligence its procurement, privacy enforcement and grievance "
            "systems deserve. Building auditability and remedy now costs far less than reversing automated "
            "exclusion after it becomes administrative routine."
        ),
    },
    "Water disputes reveal the geography of politics and the politics of geography.": {
        "thesis": (
            "Rivers follow gradients while jurisdictions follow boundaries drawn for entirely different reasons. "
            "Conflict arises where an indivisible hydrological unit is governed by divisible political ones, each "
            "answerable only to its own electorate. The proposition captures a double causation: terrain shapes "
            "political conflict, and political conflict reshapes the use of terrain."
        ),
        "structure": [
            "Set out the mismatch between river basins and state boundaries.",
            "Explain how cropping and electricity policy convert shared water into rival claims.",
            "Assess the tribunal mechanism and its chronic delays.",
            "Add groundwater as the invisible dispute without any tribunal.",
            "Suggest basin governance, transparent data and demand management.",
        ],
        "dimensions": [
            "Constitutional design places water largely with states while interstate rivers need Union "
            "adjudication, producing structurally contested authority.",
            "Basin hydrology ignores boundaries, so upstream storage or diversion changes downstream livelihoods "
            "without any shared decision forum.",
            "Cropping choices driven by procurement and free electricity convert agronomic decisions into "
            "interstate demands on limited flow.",
            "Climate variability sharpens conflict by making flows less predictable exactly when allocation "
            "formulas assume stable long-run averages.",
        ],
        "examples": [
            "The Cauvery dispute ran from the 1990 tribunal to the 2018 Supreme Court award and the Cauvery Water "
            "Management Authority.",
            "The Sutlej-Yamuna Link canal remains unbuilt decades after the Ravi-Beas allocation dispute between "
            "Punjab and Haryana.",
            "The Interstate River Water Disputes Act, 1956 was amended in 2002 to impose time limits on tribunal "
            "awards.",
            "Atal Bhujal Yojana, launched in 2019, addresses groundwater through community water budgeting in "
            "stressed blocks.",
        ],
        "counterview": (
            "Water conflict is not inevitable geography. Most Indian sharing arrangements function quietly, and "
            "disputes flare mainly when electoral competition rewards intransigence. Technical remedies also "
            "exist: better measurement, crop shifts, efficient irrigation and storage could ease scarcity enough "
            "that political geography would matter far less than it presently does."
        ),
        "conclusion": (
            "Rivers cannot be redrawn, so institutions must be. Transparent flow data, basin authorities with "
            "real powers and demand-side reform in agriculture offer more than another decade of litigation over "
            "fixed shares."
        ),
    },
    "A constitutional democracy must protect both the mandate and the minority.": {
        "thesis": (
            "An election confers authority to govern, not permission to do anything. A constitution simultaneously "
            "honours the majority's right to decide and withdraws certain questions from its reach, so that "
            "today's losers remain citizens and may become tomorrow's winners. The proposition names the balance "
            "distinguishing constitutional democracy from simple majority rule."
        ),
        "structure": [
            "Establish the democratic legitimacy of an electoral mandate.",
            "Explain why entrenched rights are democratic rather than anti-democratic.",
            "Examine judicial review and its own accountability problem.",
            "Show deliberative institutions performing the everyday balancing.",
            "Identify the failure modes at both extremes.",
        ],
        "dimensions": [
            "An electoral mandate authorises decisive government, and routinely blocking it converts "
            "constitutionalism into rule by unelected institutions.",
            "Entrenched rights preserve the conditions of future majorities by protecting speech, association and "
            "equal citizenship from present power.",
            "Judicial review polices constitutional boundaries but must justify itself through reasons, restraint "
            "and consistency rather than preference.",
            "Deliberative institutions such as committees, consultation and a working opposition settle most "
            "conflicts long before they reach a court.",
        ],
        "examples": [
            "Kesavananda Bharati (1973) held that amendment cannot destroy the basic structure, limiting even a "
            "very large majority.",
            "S. R. Bommai (1994) subjected the dismissal of state governments to judicial review and floor "
            "tests.",
            "The Tenth Schedule, added in 1985, restrains defection while also constraining an individual "
            "legislator's dissent.",
            "The general election of 1977 showed the electorate itself reversing the Emergency through the "
            "ballot.",
        ],
        "counterview": (
            "Balance can tip into paralysis or judicial supremacy. Courts staying legislation for years, or "
            "minority vetoes over ordinary economic policy, frustrate a government elected precisely to change "
            "course. Rights protection works best when narrow, principled and reasoned, so that constitutional "
            "limits never become an all-purpose objection to democratic choice."
        ),
        "conclusion": (
            "Constitutional democracy is a settlement between winning and belonging. India sustains it when "
            "elections remain decisive, rights remain non-negotiable, and both sides accept that today's majority "
            "is a temporary trustee."
        ),
    },
}


def essay_solution(title: str, dimensions: list[str], set_no: int) -> dict[str, Any]:
    unknown = [tag for tag in dimensions if tag not in ESSAY_EVIDENCE]
    if unknown:
        raise KeyError(f"Unknown essay dimension tags for {title!r}: {unknown}")
    framework = ESSAY_AUTHORED_FRAMEWORKS[title]
    return {
        "thesis": framework["thesis"],
        "structure": list(framework["structure"]),
        "dimensions": list(framework["dimensions"]),
        "examples": list(framework["examples"]),
        "counterview": framework["counterview"],
        "conclusion": framework["conclusion"],
        "note": "Model framework for practice; it is not an official or unique UPSC answer.",
    }


def build_essay(set_no: int) -> dict[str, Any]:
    start = (set_no - 1) * 8
    selected = ESSAY_TOPICS[start:start + 8]
    topics = []
    for index, (title, dims) in enumerate(selected, 1):
        topics.append({
            "no": index, "section": "A" if index <= 4 else "B",
            "text": title, "solution": essay_solution(title, dims, set_no),
        })
    return {
        "kind": "essay", "paper": "Essay", "title": "UPSC Civil Services (Main) Essay Simulation",
        "time": "3 Hours", "max_marks": 250, "marks_per_essay": 125,
        "required_essays": 2, "topics": topics,
        "instructions": [
            "Write two essays, choosing one topic from Section A and one from Section B.",
            "Each essay carries 125 marks. Credit is given for orderly, concise and effective expression.",
            "The question paper contains no prescribed or official viewpoint.",
        ],
    }


# ---------------------------------------------------------------------------
# Philosophy Optional

PHILOSOPHY = {
    "western": [
        ("Plato's Forms", "Forms explain stable knowledge and the one-over-many.", "Aristotle's separation objection challenges causal relevance.", "Defend ontological independence without treating the intelligible realm as a place."),
        ("Aristotle's substance", "Primary substance is the individual composite in the Categories.", "The Metaphysics gives form explanatory priority.", "Distinguish logical subjecthood from metaphysical actuality."),
        ("Descartes' methodic doubt", "Doubt suspends defeasible beliefs to locate the cogito.", "The Cartesian circle challenges the guarantee of clear ideas.", "Treat doubt as methodological, not permanent scepticism."),
        ("Spinoza's substance", "Only one self-caused substance exists with infinite attributes.", "Modal individuality seems threatened by necessitarianism.", "Explain freedom as adequate understanding rather than uncaused choice."),
        ("Leibniz's monads", "Monads are simple, windowless centres of perception.", "Pre-established harmony risks making interaction merely apparent.", "Connect hierarchy of perception with sufficient reason."),
        ("Locke on ideas", "Ideas arise from sensation and reflection.", "The veil-of-perception objection threatens knowledge of external objects.", "Separate source of ideas from justification of resemblance."),
        ("Berkeley's immaterialism", "To be for sensible objects is to be perceived.", "Continuity is secured through divine perception.", "Show why rejecting matter does not reject ordinary objects."),
        ("Hume on causation", "Experience gives constant conjunction, not necessary connection.", "Induction cannot be non-circularly justified by past success.", "Explain custom as psychological expectation, not logical proof."),
        ("Kant's synthetic a priori", "A priori forms and categories make experience possible.", "The thing-in-itself marks a limit that invites idealist criticism.", "Use transcendental conditions rather than innate propositions."),
        ("Kant's antinomies", "Reason generates contradictions when it treats the world as a completed thing.", "Transcendental idealism dissolves the conflict by limiting knowledge.", "Distinguish mathematical from dynamical antinomies."),
        ("Hegel's dialectic", "Concepts develop through determinate negation.", "The triad formula can caricature Hegel's immanent method.", "Explain contradiction as productive conceptual instability."),
        ("Moore's common sense", "Common-sense propositions can be more certain than sceptical premises.", "The argument may beg the question against the sceptic.", "Distinguish proof of an external world from explanation of knowledge."),
        ("Russell's descriptions", "A definite description is analysed through quantified structure.", "Reference failure need not make the whole sentence meaningless.", "Apply uniqueness, existence and predication conditions."),
        ("Early Wittgenstein", "A proposition pictures a possible fact through logical form.", "Logical form cannot itself be pictured in the same way.", "Separate saying from showing."),
        ("Logical positivism", "Verification sought to distinguish cognitively meaningful claims.", "Universal laws and the principle itself create self-application problems.", "Use weaker confirmation without erasing theoretical terms."),
        ("Later Wittgenstein", "Meaning is use within language-games and forms of life.", "Rule-following rejects private interpretation as a final foundation.", "Avoid turning family resemblance into mere vagueness."),
        ("Husserl's phenomenology", "Epoché brackets the natural attitude to examine intentional consciousness.", "The transcendental turn raises worries about solipsism.", "Explain intentionality as consciousness-of, not mental representation alone."),
        ("Existentialism", "Existence precedes essence in Sartre's account of human freedom.", "Radical freedom can understate facticity and social constraint.", "Join responsibility with situated choice."),
        ("Quine on analyticity", "The analytic-synthetic distinction lacks a non-circular foundation.", "Holism treats statements as facing experience collectively.", "Do not infer that all revisions are equally rational."),
        ("Strawson on persons", "Person is a basic particular to which mental and physical predicates apply.", "The no-ownership view cannot explain self-ascription.", "Show why personhood is not inferred from two substances."),
    ],
    "indian": [
        ("Carvaka perception", "Perception is the only independent source of knowledge.", "Inference is accepted practically but denied certainty beyond observed cases.", "Distinguish epistemic critique from crude hedonism."),
        ("Jaina anekantavada", "Reality has multiple aspects and finite judgements are standpoint-bound.", "Relativity does not entail that contradictory claims are equally true.", "Connect non-one-sidedness with conditional predication."),
        ("Buddhist dependent origination", "Phenomena arise dependently without an independent self.", "The middle avoids eternalism and annihilationism.", "Link causal conditioning to the practical path of liberation."),
        ("Madhyamaka emptiness", "Emptiness means absence of intrinsic nature, not non-existence.", "Emptiness itself must not become a metaphysical substance.", "Use the two truths without separating two worlds."),
        ("Yogacara consciousness-only", "Experienced objects are analysed through consciousness and its constructions.", "The view must explain intersubjective order.", "Distinguish denial of external objects from denial of experience."),
        ("Nyaya perception", "Perception arises from appropriate sense-object contact.", "Later Nyaya distinguishes indeterminate and determinate awareness.", "Explain error without making all cognition inferential."),
        ("Nyaya inference", "Inference uses an invariable concomitance established through positive and negative instances.", "The Buddhist challenges universals and necessary relations.", "Show the role of counterexample-free pervasion."),
        ("Vaisesika categories", "Substance, quality, motion, universal, particularity and inherence organise reality.", "Inherence is posited to connect inseparable relata.", "Address the regress objection to inherence."),
        ("Samkhya causation", "The effect pre-exists in the cause under satkaryavada.", "Transformation preserves material continuity.", "Contrast manifestation with new production."),
        ("Samkhya purusa", "Plural conscious selves are distinct from material nature.", "Interaction between inactive consciousness and unconscious nature is difficult.", "Use reflection and proximity analogies cautiously."),
        ("Yoga citta-vrtti-nirodha", "Yoga disciplines mental modifications to disclose the seer.", "Ethical restraints are constitutive, not optional preliminaries.", "Connect eight limbs with discriminative knowledge."),
        ("Mimamsa intrinsic validity", "Cognition is presumed valid unless defeated by later knowledge.", "Error requires an account of subsequent sublation.", "Contrast with Nyaya's extrinsic test."),
        ("Mimamsa sentence meaning", "Words generate sentence meaning through expectancy, compatibility and proximity.", "Anvitabhidhana and abhihitanvaya disagree on how connection arises.", "Compare connected-word and word-then-connection models."),
        ("Advaita Brahman", "Non-dual Brahman is the ultimate reality; plurality is dependent appearance.", "The status of ignorance creates locus and beginning problems.", "Use levels of reality without calling the world sheer nothing."),
        ("Ramanuja's qualified non-dualism", "Souls and matter are real modes or body of Brahman.", "Unity does not erase internal difference.", "Explain body-soul dependence and devotion."),
        ("Madhva's dualism", "God, souls and matter are irreducibly distinct.", "Five differences structure a realist devotional metaphysics.", "Relate hierarchy among souls to liberation debates."),
        ("Aurobindo's evolution", "Involution makes spiritual evolution possible.", "Supermind mediates unity and multiplicity.", "Distinguish spiritual teleology from biological mechanism."),
        ("Theory of karma", "Karma links intentional action with consequences across lives.", "Collective suffering raises problems of evidence and victim-blaming.", "Preserve moral agency without using karma to excuse injustice."),
        ("Liberation traditions", "Moksha or nirvana ends ignorance, bondage or craving according to each school.", "Shared vocabulary conceals different selves, methods and goals.", "Compare ontology, path and liberated condition."),
        ("Pramana pluralism", "Indian schools disagree over perception, inference, testimony and other sources.", "Adding a source requires irreducibility and reliable scope.", "Compare acceptance lists with underlying metaphysics."),
    ],
    "social": [
        ("Equality", "Equality rejects arbitrary hierarchy while allowing relevant differentiation.", "Formal equality can preserve material disadvantage.", "Defend substantive equality through public reasons."),
        ("Justice", "Justice concerns fair institutions, distribution and recognition.", "Procedural fairness alone may legitimise unequal starting points.", "Join procedure, capability and corrective mechanisms."),
        ("Liberty", "Negative liberty protects non-interference; positive liberty concerns agency.", "Paternalism can misuse positive freedom.", "Use proportionality and equal freedom."),
        ("Sovereignty", "Classical sovereignty claims final authority within a territory.", "Federalism and international law distribute practical authority.", "Distinguish legal supremacy from effective capacity."),
        ("Individual and state", "The state protects rights but can threaten autonomy.", "Liberal, idealist and Marxist accounts assign different purposes.", "Judge authority through legitimacy and limits."),
        ("Democracy", "Democracy combines political equality, contestation and public reasoning.", "Majoritarianism can suppress minority rights.", "Defend constitutional democracy rather than elections alone."),
        ("Socialism", "Socialism critiques private concentration of productive power.", "Central planning can weaken freedom and information.", "Separate social ownership goals from one administrative model."),
        ("Marxism", "Historical materialism relates social forms to production and class struggle.", "Economic reductionism understates culture and politics.", "Use reciprocal causation without abandoning material analysis."),
        ("Liberalism", "Liberalism protects equal freedom, rights and limited government.", "Abstract individuals may conceal social dependence.", "Reconcile autonomy with enabling institutions."),
        ("Gandhism", "Swaraj joins self-rule, non-violence and decentralised moral politics.", "Village romanticism can ignore caste domination.", "Use constructive programme with constitutional rights."),
        ("Humanism", "Humanism centres human dignity and critical agency.", "Anthropocentrism can neglect ecological value.", "Develop relational and ecological humanism."),
        ("Secularism", "Indian secularism combines principled distance and equal citizenship.", "Selective intervention can appear partisan.", "Require rights-based and publicly reasoned engagement."),
        ("Multiculturalism", "Group recognition can correct assimilation and exclusion.", "Internal minorities may be oppressed by group authority.", "Protect culture alongside individual rights."),
        ("Punishment", "Punishment is defended through deterrence, desert, incapacitation or reform.", "Harshness does not prove deterrent value.", "Use proportionality, evidence and reintegration."),
        ("Death penalty", "Capital punishment invokes retribution and deterrence.", "Irreversibility and unequal procedure create grave objections.", "Assess through dignity, error and rarest-of-rare doctrine."),
        ("Development", "Development expands capabilities rather than income alone.", "Growth can displace communities and ecology.", "Use participation, compensation and sustainability."),
        ("Social progress", "Progress requires evaluative criteria beyond technological change.", "One group's gain may be another's loss.", "Use freedom, equality, sustainability and voice."),
        ("Gender discrimination", "Gender hierarchy structures work, property, body and voice.", "Formal rights may coexist with social reproduction of inequality.", "Combine redistribution, recognition and representation."),
        ("Caste discrimination", "Caste links graded status, endogamy and occupational power.", "Class analysis alone cannot explain ritual and social exclusion.", "Join annihilation of caste with material equality."),
        ("Gandhi and Ambedkar", "Both opposed untouchability but differed on caste, representation and political method.", "Reconciliation must not erase their conflict.", "Compare moral reform with structural and constitutional transformation."),
    ],
    "religion": [
        ("Attributes of God", "Classical theism joins omnipotence, omniscience and perfect goodness.", "Attribute combinations generate freedom and evil puzzles.", "Clarify logical rather than merely verbal compatibility."),
        ("Deism", "Deism affirms a creator while limiting revelation and intervention.", "A distant creator may have little explanatory role.", "Contrast natural religion with providential theism."),
        ("Pantheism", "Pantheism identifies God with all reality.", "It risks dissolving divine personality and evil's contrast.", "Distinguish identity from panentheistic inclusion."),
        ("Cosmological argument", "Contingent beings motivate a necessary ground.", "A necessary first cause may not establish a personal God.", "Separate explanatory stopping point from theological attributes."),
        ("Teleological argument", "Order or fine-tuning is taken to support purposive explanation.", "Evolution and multiverse hypotheses offer alternatives.", "Use inference to best explanation with modest conclusion."),
        ("Ontological argument", "Anselm reasons from the concept of the greatest conceivable being.", "Existence may not function as a real predicate.", "Distinguish conceptual necessity from instantiated existence."),
        ("Problem of evil", "Evil appears inconsistent with unlimited power, knowledge and goodness.", "Free-will and soul-making defences address different evils.", "Include evidential as well as logical forms."),
        ("Soul", "Substance dualism treats the soul as distinct from body.", "Interaction and dependence on the brain challenge separation.", "Compare personal identity, consciousness and embodiment."),
        ("Immortality", "Immortality claims survival of personal identity after bodily death.", "Memory and continuity criteria may diverge.", "Do not infer immortality merely from conceivability."),
        ("Rebirth", "Rebirth explains continuity without necessarily preserving an identical substance.", "Memory absence and moral distribution raise objections.", "Distinguish causal continuity from numerical identity."),
        ("Liberation", "Religious liberation transforms bondage, ignorance or alienation.", "Traditions differ on agent, path and final condition.", "Compare rather than homogenise moksha and nirvana."),
        ("Reason and faith", "Faith can extend beyond evidence without contradicting reason.", "Fideism risks insulating belief from criticism.", "Use critical trust rather than blind assent."),
        ("Revelation", "Revelation claims divine disclosure through text, event or experience.", "Competing revelations require interpretation and criteria.", "Distinguish occurrence from warranted recognition."),
        ("Religious experience", "Mystical experience is often described as noetic and ineffable.", "Plural and naturalistic explanations challenge evidential force.", "Treat testimony as defeasible evidence."),
        ("Religion without God", "Buddhist and some naturalistic traditions organise ultimacy without a creator.", "Religion cannot be defined solely by theism.", "Use practice, transformation and ultimate concern."),
        ("Religion and morality", "Divine command theory grounds obligation in God's will.", "The Euthyphro dilemma challenges arbitrariness or independence.", "Separate motivation, knowledge and foundation of morality."),
        ("Religious pluralism", "Pluralism interprets traditions as diverse responses to ultimate reality.", "It may redescribe traditions from an external framework.", "Balance humility with genuine disagreement."),
        ("Absolute truth", "Religions make truth claims that can conflict.", "Tolerance does not require declaring all claims identical.", "Defend dialogue without relativism."),
        ("Religious language", "Talk of God strains ordinary descriptive categories.", "Analogy, symbol and language-game theories preserve different functions.", "Avoid treating non-literal language as meaningless."),
        ("Verification and eschatology", "Eschatological verification proposes eventual confirmation after death.", "The proposal faces accessibility and falsification objections.", "Distinguish logical possibility from present evidence."),
    ],
}


PHILOSOPHY_SOURCE_GROUPS = [
    (["Plato's Forms", "Aristotle's substance"], "Philosophy-Paper-I-—-Western-Philosophy/01-Plato-and-Aristotle"),
    (["Descartes' methodic doubt", "Spinoza's substance", "Leibniz's monads"], "Philosophy-Paper-I-—-Western-Philosophy/02-Rationalism"),
    (["Locke on ideas", "Berkeley's immaterialism", "Hume on causation"], "Philosophy-Paper-I-—-Western-Philosophy/03-Empiricism"),
    (["Kant's synthetic a priori", "Kant's antinomies"], "Philosophy-Paper-I-—-Western-Philosophy/04-Kant"),
    (["Hegel's dialectic"], "Philosophy-Paper-I-—-Western-Philosophy/05-Hegel"),
    (["Moore's common sense", "Russell's descriptions", "Early Wittgenstein"], "Philosophy-Paper-I-—-Western-Philosophy/06-Moore,-Russell-and-Early-Wittgenstein"),
    (["Logical positivism"], "Philosophy-Paper-I-—-Western-Philosophy/07-Logical-Positivism"),
    (["Later Wittgenstein"], "Philosophy-Paper-I-—-Western-Philosophy/08-Later-Wittgenstein"),
    (["Husserl's phenomenology"], "Philosophy-Paper-I-—-Western-Philosophy/09-Phenomenology-(Husserl)"),
    (["Existentialism"], "Philosophy-Paper-I-—-Western-Philosophy/10-Existentialism"),
    (["Quine on analyticity", "Strawson on persons"], "Philosophy-Paper-I-—-Western-Philosophy/11-Quine-and-Strawson"),
    (["Carvaka perception"], "Philosophy-Paper-I-—-Indian-Philosophy/01-Carvaka"),
    (["Jaina anekantavada"], "Philosophy-Paper-I-—-Indian-Philosophy/02-Jainism"),
    (["Buddhist dependent origination", "Madhyamaka emptiness", "Yogacara consciousness-only"], "Philosophy-Paper-I-—-Indian-Philosophy/03-Schools-of-Buddhism"),
    (["Nyaya perception", "Nyaya inference", "Vaisesika categories", "Pramana pluralism"], "Philosophy-Paper-I-—-Indian-Philosophy/04-Nyaya–Vaisesika"),
    (["Samkhya causation", "Samkhya purusa"], "Philosophy-Paper-I-—-Indian-Philosophy/05-Samkhya"),
    (["Yoga citta-vrtti-nirodha"], "Philosophy-Paper-I-—-Indian-Philosophy/06-Yoga"),
    (["Mimamsa intrinsic validity", "Mimamsa sentence meaning"], "Philosophy-Paper-I-—-Indian-Philosophy/07-Mimamsa"),
    (["Advaita Brahman", "Ramanuja's qualified non-dualism", "Madhva's dualism", "Theory of karma", "Liberation traditions"], "Philosophy-Paper-I-—-Indian-Philosophy/08-Schools-of-Vedanta"),
    (["Aurobindo's evolution"], "Philosophy-Paper-I-—-Indian-Philosophy/09-Aurobindo"),
    (["Equality", "Justice", "Liberty"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/01-Social-and-Political-Ideals"),
    (["Sovereignty"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/02-Sovereignty"),
    (["Individual and state"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/03-Individual-and-State"),
    (["Democracy"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/04-Forms-of-Government"),
    (["Socialism", "Marxism", "Liberalism", "Gandhism"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/05-Political-Ideologies"),
    (["Humanism", "Secularism", "Multiculturalism"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/06-Humanism,-Secularism-and-Multiculturalism"),
    (["Punishment", "Death penalty"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/07-Crime-and-Punishment"),
    (["Development", "Social progress"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/08-Development-and-Social-Progress"),
    (["Gender discrimination"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/09-Gender-Discrimination"),
    (["Caste discrimination", "Gandhi and Ambedkar"], "Philosophy-Paper-II-—-Socio-Political-Philosophy/10-Caste-Discrimination-Gandhi-and-Ambedkar"),
    (["Attributes of God", "Deism", "Pantheism"], "Philosophy-Paper-II-—-Philosophy-of-Religion/01-Notions-of-God"),
    (["Cosmological argument", "Teleological argument", "Ontological argument"], "Philosophy-Paper-II-—-Philosophy-of-Religion/02-Proofs-for-the-Existence-of-God"),
    (["Problem of evil"], "Philosophy-Paper-II-—-Philosophy-of-Religion/03-Problem-of-Evil"),
    (["Soul", "Immortality", "Rebirth", "Liberation"], "Philosophy-Paper-II-—-Philosophy-of-Religion/04-Soul-Immortality,-Rebirth-and-Liberation"),
    (["Reason and faith", "Revelation"], "Philosophy-Paper-II-—-Philosophy-of-Religion/05-Reason,-Revelation-and-Faith"),
    (["Religious experience"], "Philosophy-Paper-II-—-Philosophy-of-Religion/06-Religious-Experience"),
    (["Religion without God"], "Philosophy-Paper-II-—-Philosophy-of-Religion/07-Religion-without-God"),
    (["Religion and morality"], "Philosophy-Paper-II-—-Philosophy-of-Religion/08-Religion-and-Morality"),
    (["Religious pluralism", "Absolute truth"], "Philosophy-Paper-II-—-Philosophy-of-Religion/09-Religious-Pluralism-and-Absolute-Truth"),
    (["Religious language", "Verification and eschatology"], "Philosophy-Paper-II-—-Philosophy-of-Religion/10-Nature-of-Religious-Language"),
]
PHILOSOPHY_SOURCE_MAP = {
    name: (
        "learning_package_final/Philosophy-Optional/"
        + folder
        + "/Solved-Practice-Workbook.md"
    )
    for names, folder in PHILOSOPHY_SOURCE_GROUPS
    for name in names
}


def optional_model(
    topic: tuple[str, str, str, str],
    comparator: tuple[str, str, str, str],
    marks: int,
    set_no: int,
) -> str:
    name, thesis, criticism, verdict = topic
    comp_name, comp_thesis, comp_criticism, _comp_verdict = comparator
    emphasis = [
        "internal coherence and the exact inferential transition",
        "comparative explanatory cost and the strongest counterargument",
        "epistemological or practical consequence of the doctrine",
        "non-anachronistic continuing relevance",
    ][set_no - 1]
    sentences = [
        f"{name} advances a definite proposal: {thesis}",
        f"The {name} test concerns {emphasis}; it evaluates {name} on its own terms.",
        f"Reconstructing {name} requires showing why '{thesis.rstrip('.')}' is needed, what {name} explains and where {name} might fail.",
        f"The principal challenge to {name} is precise: {criticism} As a {name} objection, it tests {name} for coherence and explanatory adequacy.",
        f"The strongest reply available to {name} is equally bounded: {verdict} It preserves {name} only within that stated boundary.",
        f"{comp_name} offers a contrasting commitment: {comp_thesis} The contrast with {name} identifies a different premise and philosophical cost.",
        f"However, {comp_name} faces {comp_criticism[0].lower() + comp_criticism[1:]} Replacing {name} with {comp_name} therefore relocates the difficulty.",
        f"Textual control over {name} keeps its technical vocabulary separate from later doctrines and prevents {comp_name}'s solution being read backward.",
        f"The gain from {name} is clearest on the exact problem expressed by '{thesis.rstrip('.')}'; beyond it, {name} risks unsupported extension.",
        f"Evaluation of {name} must separate a plausible starting insight from a successful argument, while {comp_name} shows what an alternative owes.",
        f"Finally, {name} must specify whether {name}'s concepts are descriptive, normative or transcendental; the {name} level controls the force of {criticism.lower()}",
        f"The historical importance of {name} lies in making '{thesis.rstrip('.')}' available within {name} as an argument later philosophy must refine or reject.",
        f"Placed beside {comp_name}, {name} reveals that solving one philosophical burden often creates another concerning {comp_thesis.lower()}",
        f"A reasoned verdict retains {name}'s insight, accepts the limit in '{verdict.rstrip('.')}', and uses {comp_name} as a genuine argumentative test.",
    ]
    minimum = {10: 125, 15: 205, 20: 285}.get(marks, 205)
    maximum = {10: 190, 15: 295, 20: 390}.get(marks, 295)
    chosen: list[str] = []
    for sentence in sentences:
        if words(" ".join(chosen + [sentence])) <= maximum:
            chosen.append(sentence)
        if words(" ".join(chosen)) >= minimum:
            break
    if words(" ".join(chosen)) < minimum:
        raise ValueError(f"Philosophy answer too short for {name}, {marks} marks")
    return " ".join(map(plain, chosen))


def philosophy_subpart(
    topic: tuple[str, str, str, str],
    comparator: tuple[str, str, str, str],
    marks: int,
    set_no: int,
    serial: int,
) -> dict[str, Any]:
    directives = ["Explain", "Examine", "Critically discuss", "Evaluate"]
    directive = directives[(set_no + serial - 2) % 4]
    focus = [
        "conceptual foundations and internal coherence",
        "argument, counterargument and comparative cost",
        "epistemological or practical implications",
        "contemporary relevance without anachronism",
    ][set_no - 1]
    return {
        "label": chr(96 + serial),
        "marks": marks,
        "text": (
            f"{directive} {topic[0]} with emphasis on {focus}. Reconstruct the argument with doctrinal precision, "
            f"state a serious objection and the strongest available reply, and compare the result with {comparator[0]}."
        ),
        "answer": optional_model(topic, comparator, marks, set_no),
        "source": PHILOSOPHY_SOURCE_MAP[topic[0]],
        "difficulty": "above-typical recent UPSC Philosophy Optional",
        "difficulty_features": [
            "argument reconstruction", "doctrinal precision", "objection and reply",
            "cross-thinker or cross-school comparison",
        ],
    }


def build_optional(paper_no: int, set_no: int) -> dict[str, Any]:
    if paper_no == 1:
        sections = [("A", "Western Philosophy", PHILOSOPHY["western"]),
                    ("B", "Indian Philosophy", PHILOSOPHY["indian"])]
    else:
        sections = [("A", "Socio-Political Philosophy", PHILOSOPHY["social"]),
                    ("B", "Philosophy of Religion", PHILOSOPHY["religion"])]
    questions = []
    for section_index, (section, title, topics) in enumerate(sections):
        compulsory_no = 1 if section_index == 0 else 5
        offset = (set_no - 1) * 5
        compulsory_topics = [topics[(offset + i) % len(topics)] for i in range(5)]
        questions.append({
            "no": compulsory_no, "section": section, "section_title": title,
            "compulsory": True,
            "subparts": [
                philosophy_subpart(
                    topic,
                    topics[(offset + i + 1) % len(topics)],
                    10,
                    set_no,
                    i + 1,
                )
                for i, topic in enumerate(compulsory_topics)
            ],
        })
        remaining_numbers = [2, 3, 4] if section_index == 0 else [6, 7, 8]
        base = offset + 5
        for local, qno in enumerate(remaining_numbers):
            chosen = [topics[(base + local * 3 + i) % len(topics)] for i in range(3)]
            marks = [20, 15, 15]
            questions.append({
                "no": qno, "section": section, "section_title": title,
                "compulsory": False,
                "subparts": [
                    philosophy_subpart(
                        topic,
                        topics[(base + local * 3 + i + 1) % len(topics)],
                        mark,
                        set_no,
                        i + 1,
                    )
                    for i, (topic, mark) in enumerate(zip(chosen, marks))
                ],
            })
    questions.sort(key=lambda x: x["no"])
    return {
        "kind": "optional", "paper": f"Philosophy-{paper_no}",
        "title": f"UPSC Philosophy Optional Paper {paper_no} Simulation",
        "time": "3 Hours", "max_marks": 250, "questions": questions,
        "offered_marks": 400, "required_questions": 5,
        "compulsory_questions": [1, 5],
        "additional_questions": 3,
        "minimum_additional_from_each_section": 1,
        "instructions": [
            "The paper has two sections, A and B, and eight questions.",
            "Question 1 and Question 5 are compulsory.",
            "Answer three other questions, choosing at least one from each section.",
            "Answer five questions in all. The marks carried by each subpart are indicated.",
        ],
    }


# ---------------------------------------------------------------------------
# Paper assembly

def build_objective(kind: str, set_no: int, questions: list[dict[str, Any]]) -> dict[str, Any]:
    if kind == "Prelims-GS-I":
        return {
            "kind": "objective", "paper": kind,
            "title": "UPSC Civil Services Preliminary Examination - General Studies Paper I",
            "time": "2 Hours", "max_marks": 200, "questions": questions,
            "marking": {
                "correct": 2.0, "wrong": -0.66, "skipped": 0.0,
                "negative_fraction": "1/3 of marks assigned to the question",
            },
            "instructions": [
                "This paper contains 100 questions. Each question has four alternatives.",
                "Each correct response carries 2 marks; one-third of the marks assigned to a question (shown as 0.66) is deducted for an incorrect response; an unattempted question carries zero.",
                f"Current-affairs content is limited to information available on or before {CUTOFF}.",
            ],
        }
    return {
        "kind": "objective", "paper": kind,
        "title": "UPSC Civil Services Preliminary Examination - CSAT Paper II",
        "time": "2 Hours", "max_marks": 200, "questions": questions,
        "marking": {
            "correct": 2.5, "wrong": -0.83, "skipped": 0.0,
            "negative_fraction": "1/3 of marks assigned to the question",
        },
        "qualifying": "33 percent",
        "instructions": [
            "This paper contains 80 questions and is qualifying with a minimum standard of 33 percent.",
            "Each correct response carries 2.5 marks; one-third of the marks assigned to a question (shown as 0.83) is deducted for an incorrect response; an unattempted question carries zero.",
            "Use only the information given in comprehension and data-sufficiency questions.",
        ],
    }


def build_all_sources() -> dict[int, dict[str, Any]]:
    prelims = prelims_sets()
    csat = csat_sets()
    if not DESCRIPTIVE_BANK_PATH.exists():
        raise FileNotFoundError(
            f"Static descriptive bank missing: {DESCRIPTIVE_BANK_PATH}. "
            "Run the separate curation utility and review the bank before rendering."
        )
    if not DESCRIPTIVE_REVIEW_PATH.exists():
        raise FileNotFoundError(f"Descriptive sample review missing: {DESCRIPTIVE_REVIEW_PATH}")
    sample_review = json.loads(DESCRIPTIVE_REVIEW_PATH.read_text(encoding="utf-8"))
    if not sample_review.get("passed") or sample_review.get("sample_count") != 84:
        raise RuntimeError("Descriptive sample review has not passed all 84 required samples")
    descriptive = json.loads(DESCRIPTIVE_BANK_PATH.read_text(encoding="utf-8"))["sets"]
    all_sets: dict[int, dict[str, Any]] = {}
    for set_no in SETS:
        curated = descriptive[str(set_no)]
        papers = {
            "Prelims-GS-I": build_objective("Prelims-GS-I", set_no, prelims[set_no]),
            "Prelims-CSAT-II": build_objective("Prelims-CSAT-II", set_no, csat[set_no]),
            **build_language_papers(set_no),
            "Essay": curated["Essay"],
            "GS-I": curated["GS-I"],
            "GS-II": curated["GS-II"],
            "GS-III": curated["GS-III"],
            "GS-IV": curated["GS-IV"],
            "Philosophy-I": curated["Philosophy-I"],
            "Philosophy-II": curated["Philosophy-II"],
        }
        all_sets[set_no] = {
            "set": set_no, "current_affairs_cutoff": CUTOFF,
            "difficulty_standard": DIFFICULTY_STANDARD, "papers": papers,
        }
    return all_sets


# ---------------------------------------------------------------------------
# ReportLab rendering

NAVY = colors.HexColor("#17233c")
BLUE = colors.HexColor("#264f78")
LIGHT = colors.HexColor("#f2f5f8")
GREEN = colors.HexColor("#1b5e20")
RED = colors.HexColor("#8b1a1a")
PAGE_W, PAGE_H = A4

DEVANAGARI_FONT = Path(r"C:\Windows\Fonts\Nirmala.ttc")
if not DEVANAGARI_FONT.exists():
    raise FileNotFoundError(f"Devanagari font not found: {DEVANAGARI_FONT}")
pdfmetrics.registerFont(TTFont("SimulationDevanagari", str(DEVANAGARI_FONT), subfontIndex=0))
pdfmetrics.registerFont(TTFont("SimulationDevanagari-Bold", str(DEVANAGARI_FONT), subfontIndex=1))
pdfmetrics.registerFontFamily(
    "SimulationDevanagari",
    normal="SimulationDevanagari",
    bold="SimulationDevanagari-Bold",
)


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("TitleX", parent=base["Title"], fontName="Helvetica-Bold",
                                fontSize=16, leading=20, textColor=colors.white, alignment=TA_CENTER),
        "subtitle": ParagraphStyle("SubX", parent=base["Normal"], fontName="Helvetica",
                                   fontSize=9, leading=12, textColor=colors.white, alignment=TA_CENTER),
        "h1": ParagraphStyle("H1X", parent=base["Heading1"], fontName="Helvetica-Bold",
                             fontSize=12, leading=15, textColor=NAVY, spaceBefore=8, spaceAfter=5),
        "h2": ParagraphStyle("H2X", parent=base["Heading2"], fontName="Helvetica-Bold",
                             fontSize=10.5, leading=14, textColor=BLUE, spaceBefore=6, spaceAfter=4),
        "body": ParagraphStyle("BodyX", parent=base["BodyText"], fontName="Helvetica",
                               fontSize=8.7, leading=12, alignment=TA_JUSTIFY, spaceAfter=4),
        "small": ParagraphStyle("SmallX", parent=base["BodyText"], fontName="Helvetica",
                                fontSize=7.7, leading=10, alignment=TA_LEFT, spaceAfter=2),
        "q": ParagraphStyle("QX", parent=base["BodyText"], fontName="Helvetica",
                            fontSize=9, leading=12.5, alignment=TA_LEFT, spaceAfter=3),
        "answer": ParagraphStyle("AnsX", parent=base["BodyText"], fontName="Helvetica",
                                 fontSize=8.3, leading=11.5, alignment=TA_JUSTIFY, spaceAfter=3),
    }


ST = styles()
ST_HI = {
    name: ParagraphStyle(
        f"{style.name}Hindi",
        parent=style,
        fontName="SimulationDevanagari-Bold" if "Bold" in style.fontName else "SimulationDevanagari",
    )
    for name, style in ST.items()
}


def para(text: Any, style: str = "body") -> Paragraph:
    raw = str(text)
    devanagari = bool(re.search(r"[\u0900-\u097f]", raw))
    safe_text = raw if devanagari else plain(raw)
    safe = safe_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return Paragraph(safe, ST_HI[style] if devanagari else ST[style])


def header_story(title: str, set_no: int, paper: dict[str, Any], answer_key: bool) -> list[Any]:
    label = "DETAILED SOLUTIONS / ANSWER KEY" if answer_key else "QUESTION PAPER"
    data = [
        [para(f"FULL SIMULATION SET {set_no:02d}", "subtitle")],
        [para(title, "title")],
        [para(f"{label} | Time: {paper['time']} | Maximum Marks: {paper['max_marks']}", "subtitle")],
    ]
    table = Table(data, colWidths=[17 * cm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story: list[Any] = [table, Spacer(1, 0.25 * cm)]
    if not answer_key:
        instr = [[para("INSTRUCTIONS", "h2")]] + [[para(f"{i+1}. {line}", "small")] for i, line in enumerate(paper["instructions"])]
        box = Table(instr, colWidths=[17 * cm])
        box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
            ("BOX", (0, 0), (-1, -1), 0.7, BLUE),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        story += [box, Spacer(1, 0.25 * cm)]
    return story


def page_footer(canvas, doc, label: str) -> None:
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 0.65 * cm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(1.7 * cm, 0.22 * cm, label)
    canvas.drawRightString(PAGE_W - 1.7 * cm, 0.22 * cm, f"Page {doc.page}")
    canvas.restoreState()


def render_objective(story: list[Any], paper: dict[str, Any], answer_key: bool) -> None:
    if answer_key:
        answers = [f"{q['no']}-{q['answer']}" for q in paper["questions"]]
        rows = [answers[i:i + 10] for i in range(0, len(answers), 10)]
        grid = Table([[para(cell, "small") for cell in row] for row in rows],
                     colWidths=[1.7 * cm] * 10)
        grid.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
            ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        story += [para("Quick Key", "h1"), grid, Spacer(1, 0.25 * cm),
                  para("Detailed solutions", "h1")]
        for q in paper["questions"]:
            story.append(para(f"Q{q['no']}. Answer: {q['answer']} | {q['category']}", "h2"))
            story.append(para(q["stem"], "q"))
            for idx, option in enumerate(q["options"]):
                status = "CORRECT" if idx == q["correct_index"] else "INCORRECT"
                story.append(para(f"{LETTERS[idx]}. {option} - {status}: {q['reasons'][idx]}", "answer"))
            story.append(para(f"Method / explanation: {q['explanation']}", "answer"))
            story.append(para(f"Trap: {q['trap']}", "answer"))
            story.append(Spacer(1, 0.12 * cm))
    else:
        for q in paper["questions"]:
            story.append(para(f"Q{q['no']}. {q['stem']}", "q"))
            opts = [[para(f"{LETTERS[0]}. {q['options'][0]}", "small"),
                     para(f"{LETTERS[1]}. {q['options'][1]}", "small")],
                    [para(f"{LETTERS[2]}. {q['options'][2]}", "small"),
                     para(f"{LETTERS[3]}. {q['options'][3]}", "small")]]
            table = Table(opts, colWidths=[8.4 * cm, 8.4 * cm])
            table.setStyle(TableStyle([
                ("BOX", (0, 0), (-1, -1), 0.35, colors.grey),
                ("GRID", (0, 0), (-1, -1), 0.2, colors.lightgrey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]))
            story += [table, Spacer(1, 0.13 * cm)]


def render_mains(story: list[Any], paper: dict[str, Any], answer_key: bool) -> None:
    for q in paper["questions"]:
        story.append(para(f"Q{q['no']}. {q['text']}", "h2" if answer_key else "q"))
        story.append(para(f"[{q['marks']} marks | {q['word_limit']} words]", "small"))
        if answer_key:
            story.append(para(
                f"Model answer ({words(q['answer'])} words; practice model, not official): {q['answer']}",
                "answer",
            ))
        story.append(Spacer(1, 0.15 * cm))


def render_essay(story: list[Any], paper: dict[str, Any], answer_key: bool) -> None:
    for section in ("A", "B"):
        story.append(para(f"SECTION {section}", "h1"))
        for topic in [x for x in paper["topics"] if x["section"] == section]:
            story.append(para(f"{topic['no']}. {topic['text']}", "h2" if answer_key else "q"))
            if answer_key:
                sol = topic["solution"]
                story.append(para(f"Working thesis: {sol['thesis']}", "answer"))
                story.append(para("Structure: " + " | ".join(sol["structure"]), "answer"))
                story.append(para("Dimensions: " + " | ".join(sol["dimensions"]), "answer"))
                story.append(para("Examples: " + " | ".join(sol["examples"]), "answer"))
                story.append(para(f"Counterview: {sol['counterview']}", "answer"))
                story.append(para(f"Conclusion: {sol['conclusion']}", "answer"))
                story.append(para(sol["note"], "small"))
            story.append(Spacer(1, 0.18 * cm))


def render_optional(story: list[Any], paper: dict[str, Any], answer_key: bool) -> None:
    current_section = None
    for q in paper["questions"]:
        if q["section"] != current_section:
            current_section = q["section"]
            story.append(para(f"SECTION {q['section']} - {q['section_title']}", "h1"))
        comp = " (COMPULSORY)" if q["compulsory"] else ""
        story.append(para(f"Q{q['no']}{comp}", "h2"))
        for sub in q["subparts"]:
            story.append(para(f"({sub['label']}) {sub['text']} [{sub['marks']} marks]", "q"))
            if answer_key:
                story.append(para(
                    f"Model answer ({words(sub['answer'])} words; practice model, not official): {sub['answer']}",
                    "answer",
                ))
        story.append(Spacer(1, 0.18 * cm))


def render_language(story: list[Any], paper: dict[str, Any], answer_key: bool) -> None:
    for section in paper["sections"]:
        story.append(para(
            f"Q{section['no']}. {section['title']} [{section['marks']} marks]",
            "h1",
        ))
        if section.get("instruction"):
            story.append(para(section["instruction"], "small"))
        if section.get("topics"):
            for index, topic in enumerate(section["topics"], 1):
                story.append(para(f"{index}. {topic}", "q"))
            if answer_key:
                story.append(para(f"Marking guidance: {section['answer']}", "answer"))
        elif section.get("questions"):
            story.append(para(section["passage"], "body"))
            for index, question in enumerate(section["questions"], 1):
                story.append(para(f"{index}. {question['text']}", "q"))
                if answer_key:
                    story.append(para(f"Model answer: {question['answer']}", "answer"))
        elif section.get("groups"):
            for label, group in zip("ABCD", section["groups"]):
                story.append(para(f"{label}. {group['title']}", "h2"))
                for index, item in enumerate(group["items"], 1):
                    story.append(para(f"{index}. {item}", "q"))
                    if answer_key:
                        story.append(para(f"Answer: {group['answers'][index - 1]}", "answer"))
        else:
            story.append(para(section["passage"], "body"))
            if answer_key:
                story.append(para(f"Model answer: {section['answer']}", "answer"))
        story.append(Spacer(1, 0.18 * cm))


def render_pdf(paper: dict[str, Any], set_no: int, path: Path, answer_key: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(path), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm,
        topMargin=1.5 * cm, bottomMargin=1.15 * cm,
        title=paper["title"], author="UPSC Agent",
    )
    story = header_story(paper["title"], set_no, paper, answer_key)
    if paper["kind"] == "objective":
        render_objective(story, paper, answer_key)
    elif paper["kind"] == "mains":
        render_mains(story, paper, answer_key)
    elif paper["kind"] == "essay":
        render_essay(story, paper, answer_key)
    elif paper["kind"] == "optional":
        render_optional(story, paper, answer_key)
    elif paper["kind"] == "language":
        render_language(story, paper, answer_key)
    story.append(Spacer(1, 0.3 * cm))
    story.append(para("END OF PAPER" if not answer_key else "END OF DETAILED SOLUTIONS", "small"))
    label = f"Set {set_no:02d} | {paper['paper']} | {'AK' if answer_key else 'QP'}"
    doc.build(story, onFirstPage=lambda c, d: page_footer(c, d, label),
              onLaterPages=lambda c, d: page_footer(c, d, label))


# ---------------------------------------------------------------------------
# Source Markdown, validation and manifest

def source_markdown(set_data: dict[str, Any]) -> str:
    lines = [
        f"# Full Simulation Set {set_data['set']:02d}",
        "",
        f"Current-affairs cutoff: **{set_data['current_affairs_cutoff']}**.",
        "",
        f"Difficulty: **{DIFFICULTY_STANDARD['overall']}**",
        "",
        "This is the reusable human-readable edition. JSON is authoritative for regeneration.",
        "",
    ]
    for key, paper in set_data["papers"].items():
        lines += [f"## {key}", "", f"Time: {paper['time']} | Maximum marks: {paper['max_marks']}", ""]
        if paper["kind"] == "objective":
            for q in paper["questions"]:
                lines += [f"### Q{q['no']}", q["stem"], ""]
                for i, option in enumerate(q["options"]):
                    lines.append(f"{LETTERS[i]}. {option}")
                lines += ["", f"**Answer: {q['answer']}**", f"Explanation: {q['explanation']}",
                          f"Trap: {q['trap']}", ""]
        elif paper["kind"] == "mains":
            for q in paper["questions"]:
                lines += [f"### Q{q['no']} [{q['marks']} marks]", q["text"], "",
                          f"Model answer ({words(q['answer'])} words): {q['answer']}", ""]
        elif paper["kind"] == "essay":
            for q in paper["topics"]:
                sol = q["solution"]
                lines += [f"### {q['section']}{q['no']}. {q['text']}",
                          f"Thesis: {sol['thesis']}",
                          "Structure: " + " | ".join(sol["structure"]),
                          "Dimensions: " + " | ".join(sol["dimensions"]),
                          "Examples: " + " | ".join(sol["examples"]),
                          f"Counterview: {sol['counterview']}",
                          f"Conclusion: {sol['conclusion']}", ""]
        elif paper["kind"] == "language":
            for section in paper["sections"]:
                lines += [f"### Q{section['no']}. {section['title']} [{section['marks']} marks]", ""]
                if section.get("instruction"):
                    lines += [section["instruction"], ""]
                if section.get("topics"):
                    lines += [f"{index}. {topic}" for index, topic in enumerate(section["topics"], 1)]
                    lines += ["", f"**Marking guidance:** {section['answer']}", ""]
                elif section.get("questions"):
                    lines += [section["passage"], ""]
                    for index, question in enumerate(section["questions"], 1):
                        lines += [
                            f"{index}. {question['text']}",
                            f"**Model answer:** {question['answer']}",
                            "",
                        ]
                elif section.get("groups"):
                    for label, group in zip("ABCD", section["groups"]):
                        lines += [f"#### {label}. {group['title']}", ""]
                        for index, item in enumerate(group["items"], 1):
                            lines += [
                                f"{index}. {item}",
                                f"**Answer:** {group['answers'][index - 1]}",
                                "",
                            ]
                else:
                    lines += [section["passage"], "", f"**Model answer:** {section['answer']}", ""]
        else:
            for q in paper["questions"]:
                lines.append(f"### Q{q['no']}{' (Compulsory)' if q['compulsory'] else ''}")
                for sub in q["subparts"]:
                    lines += [f"({sub['label']}) {sub['text']} [{sub['marks']} marks]",
                              f"Model answer: {sub['answer']}", ""]
    return "\n".join(lines) + "\n"


def pdf_checks(path: Path) -> dict[str, Any]:
    doc = fitz.open(path)
    blank_pages = []
    replacement_pages = []
    clipping = []
    render_failures = []
    page_chars = []
    for page_no, page in enumerate(doc, 1):
        text = page.get_text()
        page_chars.append(len(text.strip()))
        if len(text.strip()) < 25:
            blank_pages.append(page_no)
        if "\ufffd" in text:
            replacement_pages.append(page_no)
        rect = page.rect
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            if x0 < -1 or y0 < -1 or x1 > rect.width + 1 or y1 > rect.height + 1:
                clipping.append({"page": page_no, "bbox": [x0, y0, x1, y1]})
        try:
            page.get_pixmap(matrix=fitz.Matrix(0.35, 0.35), alpha=False)
        except Exception as exc:  # pragma: no cover
            render_failures.append({"page": page_no, "error": str(exc)})
    doc.close()
    return {
        "pages": len(page_chars), "min_page_chars": min(page_chars) if page_chars else 0,
        "blank_or_near_empty_pages": blank_pages,
        "replacement_glyph_pages": replacement_pages,
        "out_of_page_blocks": clipping,
        "render_failures": render_failures,
        "passed": not (blank_pages or replacement_pages or clipping or render_failures),
    }


def answer_sentences(text: str) -> list[str]:
    return [
        plain(sentence)
        for sentence in re.split(r"(?<=[.!?])\s+", text)
        if words(sentence) >= 10
    ]


def answer_ngrams(text: str, size: int = 12) -> set[str]:
    tokens = [token.lower() for token in WORD_RE.findall(text)]
    return {
        " ".join(tokens[index:index + size])
        for index in range(max(0, len(tokens) - size + 1))
    }


def question_similarity(left: str, right: str) -> float:
    stop = {
        "analyse", "analyze", "discuss", "examine", "evaluate", "critically",
        "explain", "with", "reference", "the", "and", "of", "to", "in", "a",
        "an", "how", "why", "what", "answer", "words",
    }
    a = {token.lower() for token in WORD_RE.findall(left) if token.lower() not in stop}
    b = {token.lower() for token in WORD_RE.findall(right) if token.lower() not in stop}
    return len(a & b) / max(1, len(a | b))


def validate_sources(all_sets: dict[int, dict[str, Any]]) -> dict[str, Any]:
    errors: list[str] = []
    stats: dict[str, Any] = {}
    objective_stems: set[str] = set()
    mains_stems: set[str] = set()
    optional_stems: set[str] = set()
    essay_stems: set[str] = set()
    language_stems: set[str] = set()
    prelims_provenance: defaultdict[str, int] = defaultdict(int)
    forbidden_found: list[dict[str, Any]] = []
    topic_sequences: defaultdict[str, list[tuple[str, ...]]] = defaultdict(list)
    descriptive_answers: list[tuple[str, str, str]] = []
    descriptive_questions: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)
    for set_no, set_data in all_sets.items():
        set_stats = {}
        for key, paper in set_data["papers"].items():
            if paper["kind"] == "objective":
                expected = 100 if key == "Prelims-GS-I" else 80
                expected_correct = 2.0 if key == "Prelims-GS-I" else 2.5
                expected_wrong = -0.66 if key == "Prelims-GS-I" else -0.83
                if len(paper["questions"]) != expected:
                    errors.append(f"Set {set_no} {key}: count {len(paper['questions'])} != {expected}")
                if paper["max_marks"] != 200 or paper["time"] != "2 Hours":
                    errors.append(f"Set {set_no} {key}: marks/time format failure")
                if paper["marking"]["correct"] != expected_correct or paper["marking"]["wrong"] != expected_wrong:
                    errors.append(f"Set {set_no} {key}: marking scheme failure")
                if paper["marking"].get("negative_fraction") != "1/3 of marks assigned to the question":
                    errors.append(f"Set {set_no} {key}: one-third negative-marking statement missing")
                if key == "Prelims-CSAT-II" and paper.get("qualifying") != "33 percent":
                    errors.append(f"Set {set_no} {key}: 33 percent qualifying rule missing")
                for q in paper["questions"]:
                    if q["answer"] != LETTERS[(q["no"] - 1) % 4]:
                        errors.append(f"Set {set_no} {key} Q{q['no']}: rotation failure")
                    stem = normalize_stem(q["stem"])
                    if key == "Prelims-GS-I":
                        if any(normalize_stem(bad) in stem for bad in FORBIDDEN_DEFECTIVE_STEMS):
                            forbidden_found.append({
                                "set": set_no, "question": q["no"], "stem": q["stem"],
                            })
                            errors.append(f"Set {set_no} {key} Q{q['no']}: cited defective stem survived")
                        if q.get("current"):
                            prelims_provenance["repository-verified-current"] += 1
                        elif q.get("origin") == "curated-knowledge-bank":
                            prelims_provenance["curated-knowledge-bank"] += 1
                        elif q["category"] == "Art and Culture":
                            prelims_provenance["accepted-art-general-explanation"] += 1
                        else:
                            prelims_provenance["four-explicit-reasons-workbook"] += 1
                    if stem in objective_stems:
                        errors.append(f"Duplicate objective stem: {q['stem']}")
                    objective_stems.add(stem)
                    if len(q["reasons"]) != 4 or any(len(x) < 20 for x in q["reasons"]):
                        errors.append(f"Set {set_no} {key} Q{q['no']}: incomplete option analysis")
                    for option_index, reason in enumerate(q["reasons"]):
                        is_correct = option_index == q["correct_index"]
                        says_correct = bool(re.match(r"^\s*Correct\b", reason))
                        says_incorrect = bool(re.match(r"^\s*Incorrect\b", reason))
                        if is_correct and not says_correct:
                            errors.append(
                                f"Set {set_no} {key} Q{q['no']}: correct reason must start Correct"
                            )
                        if not is_correct and not says_incorrect:
                            errors.append(
                                f"Set {set_no} {key} Q{q['no']}: distractor reason must start Incorrect"
                            )
                    if not q.get("explanation") or not q.get("trap") or not q.get("source"):
                        errors.append(f"Set {set_no} {key} Q{q['no']}: incomplete detailed solution")
                    if has_stale_option_labels(q.get("explanation", "")):
                        errors.append(f"Set {set_no} {key} Q{q['no']}: stale option label in general explanation")
                    if key == "Prelims-GS-I" and q.get("difficulty_score", 0) < 4:
                        errors.append(f"Set {set_no} {key} Q{q['no']}: below difficulty threshold")
                    if key == "Prelims-GS-I":
                        option_lengths = [max(1, words(option)) for option in q["options"]]
                        if max(option_lengths) / min(option_lengths) > 3.0:
                            errors.append(f"Set {set_no} {key} Q{q['no']}: visually unbalanced distractors")
                        if q["category"] in CURATED_KNOWLEDGE_PLAN:
                            if q.get("origin") != "curated-knowledge-bank":
                                errors.append(f"Set {set_no} {key} Q{q['no']}: forbidden unverified workbook reuse")
                            source_path = ROOT / q["source"]
                            source_text = plain(source_path.read_text(
                                encoding="utf-8", errors="ignore"
                            )) if source_path.exists() else ""
                            for extract in q.get("source_extracts", []):
                                normalized_extract = normalize_stem(extract)
                                normalized_source = normalize_stem(source_text)
                                if (
                                    normalized_extract not in normalized_source
                                    and normalized_extract.replace(" ", "")
                                    not in normalized_source.replace(" ", "")
                                ):
                                    errors.append(
                                        f"Set {set_no} {key} Q{q['no']}: source extract not found"
                                    )
                        if q["category"] == "Art and Culture" and q.get(
                            "source_validation"
                        ) != "art-and-culture-general-explanation-key-accepted":
                            errors.append(f"Set {set_no} {key} Q{q['no']}: Art key not accepted through general explanation")
                    if key == "Prelims-CSAT-II":
                        if q.get("difficulty") != "above-typical recent UPSC qualifying level":
                            errors.append(f"Set {set_no} {key} Q{q['no']}: missing difficulty classification")
                        if q.get("reasoning_steps", 0) < 2 or not q.get("uniquely_solvable"):
                            errors.append(f"Set {set_no} {key} Q{q['no']}: reasoning/solvability failure")
                        if len(set(q["options"])) != 4:
                            errors.append(f"Set {set_no} {key} Q{q['no']}: duplicate options")
                        if q["category"] == "Reading Comprehension":
                            passage = q["stem"].split("Which ", 1)[0]
                            if words(passage) < 65:
                                errors.append(f"Set {set_no} {key} Q{q['no']}: passage not dense enough")
                marks = len(paper["questions"]) * paper["marking"]["correct"]
                if abs(marks - 200) > 0.01:
                    errors.append(f"Set {set_no} {key}: offered marks {marks}")
                coverage = defaultdict(int)
                for q in paper["questions"]:
                    coverage[q["category"]] += 1
                current_count = sum(1 for q in paper["questions"] if q.get("current"))
                if key == "Prelims-GS-I" and current_count != 10:
                    errors.append(f"Set {set_no} {key}: current-affairs count {current_count}")
                if key == "Prelims-GS-I":
                    for q in paper["questions"]:
                        if q.get("current"):
                            source = q["source"]
                            trusted = source.startswith("learning_package_final/") or re.match(
                                r"https://(?:www\.)?(?:pib\.gov\.in|mea\.gov\.in|rbi\.org\.in|"
                                r"isro\.gov\.in|[a-z0-9.-]+\.gov\.in)/", source
                            )
                            if not trusted:
                                errors.append(f"Set {set_no} {key} Q{q['no']}: untrusted current source")
                            if re.search(r"web[-_ ]?search|gktoday|adda247|studyiq", source, re.I):
                                errors.append(f"Set {set_no} {key} Q{q['no']}: generic web-summary source forbidden")
                            if not re.search(r"\b20(?:25|26)\b", source):
                                errors.append(f"Set {set_no} {key} Q{q['no']}: dated source note missing")
                set_stats[key] = {
                    "questions": len(paper["questions"]), "marks": marks,
                    "coverage": dict(sorted(coverage.items())),
                    "dated_current_affairs_questions": current_count,
                }
            elif paper["kind"] == "mains":
                expected_count = 13 if key == "GS-IV" else 20
                if len(paper["questions"]) != expected_count:
                    errors.append(f"Set {set_no} {key}: not {expected_count} questions")
                marks = sum(q["marks"] for q in paper["questions"])
                if marks != 250:
                    errors.append(f"Set {set_no} {key}: marks {marks}")
                counts = []
                topic_sequences[key].append(tuple(q.get("topic_id", q["text"]) for q in paper["questions"]))
                if key == "GS-IV":
                    formats = defaultdict(int)
                    for q in paper["questions"]:
                        formats[q.get("ethics_format", "missing")] += 1
                    expected_formats = {"theory-paired": 5, "application": 2, "case-study": 6}
                    if dict(formats) != expected_formats:
                        errors.append(f"Set {set_no} GS-IV format {dict(formats)} != {expected_formats}")
                for q in paper["questions"]:
                    stem = normalize_stem(q["text"])
                    if stem in mains_stems:
                        errors.append(f"Duplicate Mains question: {q['text']}")
                    mains_stems.add(stem)
                    count = words(q["answer"])
                    counts.append(count)
                    if count > q["word_limit"]:
                        errors.append(f"Set {set_no} {key} Q{q['no']}: {count}>{q['word_limit']} words")
                    minimum = (
                        80 if q["word_limit"] == 150 else
                        (180 if q["word_limit"] >= 300 else 120)
                    )
                    if count < minimum:
                        errors.append(f"Set {set_no} {key} Q{q['no']}: model answer too short ({count})")
                    if not re.search(r"[.!?][\"')\]]?\s*$", q["answer"]):
                        errors.append(f"Set {set_no} {key} Q{q['no']}: incomplete answer ending")
                    required_features = {
                        "question-specific demand", "named evidence", "analysis",
                        "qualification", "source-grounded conclusion",
                    }
                    if q.get("difficulty") != "above-typical recent UPSC" or not required_features.issubset(
                        set(q.get("difficulty_features", []))
                    ):
                        errors.append(f"Set {set_no} {key} Q{q['no']}: difficulty demand incomplete")
                    descriptive_answers.append((f"Set-{set_no:02d}-{key}-Q{q['no']}", q["answer"], q.get("topic_id", "")))
                    descriptive_questions[key].append((f"Set-{set_no:02d}-Q{q['no']}", q["text"]))
                    if any(phrase in (q["text"] + " " + q["answer"]).lower() for phrase in (
                        "test the strongest competing interpretation",
                        "institution changes incentives",
                        "majoritarian mandate or technological capacity",
                        "constitutional legitimacy, adequate resources",
                        "administratively workable",
                        "the answer must resolve",
                        ".pdf", "pdf pp", "owned core", "why it matters for an answer",
                        "study link", "topic 01 owns", "neutral routing",
                        "source routing",
                        "claim -> evidence -> analysis", "claim evidence analysis",
                        "native-body word count", "answer audit:",
                        "answer architecture:",
                        "therefore the defensible verdict on", "the tempting claim that",
                        "advances a definite proposal", "test concerns internal coherence",
                        "reconstructing ", "ca anchor",
                    )):
                        errors.append(f"Set {set_no} {key} Q{q['no']}: forbidden generic boilerplate")
                    if re.search(r"\bspeed in [a-z -]+\b|\bthrough which [a-z -]+ appeal\b", q["answer"], re.I):
                        errors.append(f"Set {set_no} {key} Q{q['no']}: unnatural topic substitution")
                set_stats[key] = {"questions": expected_count, "marks": marks,
                                  "model_answer_word_counts": counts}
            elif paper["kind"] == "language":
                if paper["max_marks"] != 300 or paper["time"] != "3 Hours":
                    errors.append(f"Set {set_no} {key}: qualifying marks/time format failure")
                if paper.get("qualifying_marks") != 75:
                    errors.append(f"Set {set_no} {key}: 25 percent qualifying threshold missing")
                expected_marks = (
                    [100, 60, 60, 20, 20, 40]
                    if key == "Qualifying-Hindi"
                    else [100, 75, 75, 50]
                )
                section_marks = [section["marks"] for section in paper["sections"]]
                if section_marks != expected_marks or sum(section_marks) != 300:
                    errors.append(
                        f"Set {set_no} {key}: section marks {section_marks} != {expected_marks}"
                    )
                if key == "Qualifying-Hindi" and not any(
                    re.search(r"[\u0900-\u097f]", str(section))
                    for section in paper["sections"]
                ):
                    errors.append(f"Set {set_no} {key}: Devanagari content missing")
                for section in paper["sections"]:
                    if section.get("topics"):
                        if len(section["topics"]) != 4 or not section.get("answer"):
                            errors.append(f"Set {set_no} {key} Q{section['no']}: essay choices/rubric incomplete")
                        for topic in section["topics"]:
                            normalized = (
                                re.sub(r"\s+", " ", unicodedata.normalize("NFC", topic)).strip().lower()
                                if key == "Qualifying-Hindi"
                                else normalize_stem(topic)
                            )
                            if normalized in language_stems:
                                errors.append(f"Duplicate qualifying-language essay topic: {topic}")
                            language_stems.add(normalized)
                    elif section.get("questions"):
                        if len(section["questions"]) != 5 or any(
                            not question.get("answer") for question in section["questions"]
                        ):
                            errors.append(f"Set {set_no} {key} Q{section['no']}: comprehension key incomplete")
                        passage = (
                            re.sub(
                                r"\s+", " ",
                                unicodedata.normalize("NFC", section["passage"]),
                            ).strip().lower()
                            if key == "Qualifying-Hindi"
                            else normalize_stem(section["passage"])
                        )
                        if passage in language_stems:
                            errors.append(f"Duplicate qualifying-language comprehension passage: {key}")
                        language_stems.add(passage)
                    elif section.get("groups"):
                        if len(section["groups"]) != 4 or any(
                            len(group["items"]) != 5
                            or len(group["answers"]) != len(group["items"])
                            for group in section["groups"]
                        ):
                            errors.append(f"Set {set_no} {key} Q{section['no']}: usage groups incomplete")
                    elif not section.get("passage") or not section.get("answer"):
                        errors.append(f"Set {set_no} {key} Q{section['no']}: passage/model missing")
                set_stats[key] = {
                    "sections": len(paper["sections"]),
                    "marks": sum(section_marks),
                    "qualifying_marks": paper["qualifying_marks"],
                }
            elif paper["kind"] == "essay":
                if paper["max_marks"] != 250 or paper["time"] != "3 Hours":
                    errors.append(f"Set {set_no} Essay: marks/time format failure")
                if paper.get("marks_per_essay") != 125 or paper.get("required_essays") != 2:
                    errors.append(f"Set {set_no} Essay: 125x2 attempt rule failure")
                if len(paper["topics"]) != 8:
                    errors.append(f"Set {set_no} Essay: not 8 topics")
                if len([x for x in paper["topics"] if x["section"] == "A"]) != 4:
                    errors.append(f"Set {set_no} Essay: Section A count")
                if len([x for x in paper["topics"] if x["section"] == "B"]) != 4:
                    errors.append(f"Set {set_no} Essay: Section B count")
                for topic in paper["topics"]:
                    stem = normalize_stem(topic["text"])
                    if stem in essay_stems:
                        errors.append(f"Duplicate Essay topic: {topic['text']}")
                    essay_stems.add(stem)
                    required = {"thesis", "structure", "dimensions", "examples", "counterview", "conclusion"}
                    if not required.issubset(topic.get("solution", {})):
                        errors.append(f"Set {set_no} Essay topic {topic['no']}: incomplete solution")
                    solution = topic["solution"]
                    if words(solution["thesis"]) < 30 or words(solution["counterview"]) < 30:
                        errors.append(f"Set {set_no} Essay topic {topic['no']}: underdeveloped thesis/counterview")
                    if len(solution["dimensions"]) != 4 or any(words(x) < 12 for x in solution["dimensions"]):
                        errors.append(f"Set {set_no} Essay topic {topic['no']}: weak topic dimensions")
                    if len(solution["examples"]) != 4 or any(words(x) < 8 for x in solution["examples"]):
                        errors.append(f"Set {set_no} Essay topic {topic['no']}: weak evidence examples")
                    essay_answer = " ".join(
                        [solution["thesis"]]
                        + solution["structure"]
                        + solution["dimensions"]
                        + solution["examples"]
                        + [solution["counterview"], solution["conclusion"]]
                    )
                    descriptive_answers.append((
                        f"Set-{set_no:02d}-Essay-{topic['no']}",
                        essay_answer,
                        topic["text"],
                    ))
                set_stats[key] = {"topics": 8, "marks": 250}
            else:
                if paper["max_marks"] != 250 or paper["time"] != "3 Hours":
                    errors.append(f"Set {set_no} {key}: marks/time format failure")
                if paper.get("offered_marks") != 400 or paper.get("required_questions") != 5:
                    errors.append(f"Set {set_no} {key}: optional offered/attempt marks failure")
                if paper.get("compulsory_questions") != [1, 5] or paper.get("additional_questions") != 3:
                    errors.append(f"Set {set_no} {key}: Q1/Q5 plus three rule failure")
                if paper.get("minimum_additional_from_each_section") != 1:
                    errors.append(f"Set {set_no} {key}: cross-section choice rule failure")
                if len(paper["questions"]) != 8:
                    errors.append(f"Set {set_no} {key}: not 8 top-level questions")
                if not paper["questions"][0]["compulsory"] or not paper["questions"][4]["compulsory"]:
                    errors.append(f"Set {set_no} {key}: Q1/Q5 compulsory structure")
                for q in paper["questions"]:
                    if sum(x["marks"] for x in q["subparts"]) != 50:
                        errors.append(f"Set {set_no} {key} Q{q['no']}: not 50 marks")
                    if any(not x.get("answer") for x in q["subparts"]):
                        errors.append(f"Set {set_no} {key} Q{q['no']}: missing subpart answer")
                    for sub in q["subparts"]:
                        stem = normalize_stem(sub["text"])
                        if stem in optional_stems:
                            errors.append(f"Duplicate Optional subpart: {sub['text']}")
                        optional_stems.add(stem)
                        needed = {
                            "argument reconstruction", "doctrinal precision",
                            "objection and reply", "cross-thinker or cross-school comparison",
                        }
                        if sub.get("difficulty") != "above-typical recent UPSC Philosophy Optional":
                            errors.append(f"Set {set_no} {key} Q{q['no']}{sub['label']}: difficulty label missing")
                        if not needed.issubset(set(sub.get("difficulty_features", []))):
                            errors.append(f"Set {set_no} {key} Q{q['no']}{sub['label']}: philosophy demand incomplete")
                        count = words(sub["answer"])
                        lower, upper = {10: (125, 200), 15: (205, 300), 20: (285, 400)}[sub["marks"]]
                        if not lower <= count <= upper:
                            errors.append(
                                f"Set {set_no} {key} Q{q['no']}{sub['label']}: "
                                f"answer length {count} outside {lower}-{upper}"
                            )
                        if not re.search(r"[.!?][\"')\]]?\s*$", sub["answer"]):
                            errors.append(
                                f"Set {set_no} {key} Q{q['no']}{sub['label']}: "
                                "incomplete answer ending"
                            )
                        source_path = ROOT / sub["source"]
                        if not source_path.exists():
                            errors.append(f"Set {set_no} {key} Q{q['no']}{sub['label']}: source missing")
                        if any(phrase in sub["answer"].lower() for phrase in (
                            "institution changes incentives", "constitutional legitimacy",
                            "administratively workable", "public policy should",
                            "majoritarian mandate", "advances a definite proposal",
                            "test concerns internal coherence", "reconstructing ",
                            "therefore the defensible verdict on", "the tempting claim that",
                        )):
                            errors.append(f"Set {set_no} {key} Q{q['no']}{sub['label']}: domain-inappropriate filler")
                        descriptive_answers.append((
                            f"Set-{set_no:02d}-{key}-Q{q['no']}{sub['label']}",
                            sub["answer"], sub["text"],
                        ))
                subparts = sum(len(q["subparts"]) for q in paper["questions"])
                set_stats[key] = {"top_level_questions": 8, "subparts": subparts,
                                  "offered_marks": 400, "candidate_marks": 250}
        stats[f"Set-{set_no:02d}"] = set_stats
    identical_topic_sequences: list[str] = []
    for paper, sequences in topic_sequences.items():
        if len(set(sequences)) != len(sequences):
            identical_topic_sequences.append(paper)
            errors.append(f"{paper}: identical question-topic sequence across sets")
    near_duplicate_questions = []
    for paper, items in descriptive_questions.items():
        for left_index, (left_id, left) in enumerate(items):
            for right_id, right in items[left_index + 1:]:
                similarity = question_similarity(left, right)
                if similarity >= 0.88:
                    near_duplicate_questions.append({
                        "paper": paper, "left": left_id, "right": right_id,
                        "similarity": round(similarity, 3),
                    })
    if near_duplicate_questions:
        errors.append(
            f"Near-duplicate descriptive questions detected: {near_duplicate_questions[:5]}"
        )
    sentence_owners: defaultdict[str, set[str]] = defaultdict(set)
    ngram_owners: defaultdict[str, set[str]] = defaultdict(set)
    for answer_id, answer, _topic in descriptive_answers:
        for sentence in answer_sentences(answer):
            sentence_owners[normalize_stem(sentence)].add(answer_id)
        for ngram in answer_ngrams(answer):
            ngram_owners[ngram].add(answer_id)
    repeated_sentences = {
        sentence: sorted(owners)
        for sentence, owners in sentence_owners.items()
        if len(owners) > 3
    }
    repeated_ngrams = {
        ngram: sorted(owners)
        for ngram, owners in ngram_owners.items()
        if len(owners) > 6
    }
    if repeated_sentences:
        errors.append(
            f"Repeated long answer sentences exceed threshold: "
            f"{list(repeated_sentences.items())[:3]}"
        )
    if repeated_ngrams:
        errors.append(
            f"Repeated 12-word answer n-grams exceed threshold: "
            f"{list(repeated_ngrams.items())[:3]}"
        )
    expected_provenance = {
        "four-explicit-reasons-workbook": 112,
        "accepted-art-general-explanation": 24,
        "curated-knowledge-bank": 224,
        "repository-verified-current": 40,
    }
    if dict(prelims_provenance) != expected_provenance:
        errors.append(
            f"Prelims provenance counts {dict(prelims_provenance)} != {expected_provenance}"
        )
    if len(mains_stems) != 292:
        errors.append(f"Unique GS descriptive questions {len(mains_stems)} != 292")
    return {
        "passed": not errors, "errors": errors, "statistics": stats,
        "unique_objective_stems": len(objective_stems),
        "unique_mains_questions": len(mains_stems),
        "unique_optional_subparts": len(optional_stems),
        "unique_essay_topics": len(essay_stems),
        "prelims_provenance": dict(prelims_provenance),
        "forbidden_defective_examples_found": forbidden_found,
        "identical_topic_sequences": identical_topic_sequences,
        "topic_sequence_hashes": {
            paper: [stable_hash("|".join(sequence)) for sequence in sequences]
            for paper, sequences in topic_sequences.items()
        },
        "near_duplicate_descriptive_questions": near_duplicate_questions,
        "repeated_long_sentences": repeated_sentences,
        "repeated_12_word_ngrams": repeated_ngrams,
        "word_count_regex": WORD_RE.pattern,
    }


def write_readme() -> None:
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    (SOURCE_ROOT / "README.md").write_text(
        "# Full UPSC Simulation Sets\n\n"
        "Four deterministic simulation sets cover Prelims GS-I, CSAT, qualifying Hindi Paper A, "
        "qualifying English Paper B, Essay, Mains GS-I-IV, and Philosophy Optional Papers I-II. "
        "Question papers contain no keys or hints; every "
        "paper has a separate detailed answer-key PDF.\n\n"
        f"**Current-affairs cutoff:** {CUTOFF}. No later event is used.\n\n"
        "## Difficulty standard\n\n"
        f"- **Overall:** {DIFFICULTY_STANDARD['overall']}\n"
        f"- **Prelims:** {DIFFICULTY_STANDARD['prelims']}\n"
        f"- **CSAT:** {DIFFICULTY_STANDARD['csat']}\n"
        f"- **Mains:** {DIFFICULTY_STANDARD['mains']}\n"
        f"- **Philosophy:** {DIFFICULTY_STANDARD['philosophy']}\n\n"
        f"- **Qualifying languages:** {DIFFICULTY_STANDARD['qualifying_language']}\n\n"
        "## Regeneration\n\n"
        "From the repository root run:\n\n"
        "```powershell\n"
        "python tools\\build_full_upsc_simulations.py --all\n"
        "```\n\n"
        "The script reads tracked `learning_package_final` workbooks for static Prelims items, "
        "uses checked deterministic CSAT generation, writes four JSON and Markdown source editions, "
        "renders all 88 PDFs, and recreates the manifest and validation reports.\n\n"
        "Current claims are admitted only from repository-verified source records or directly "
        "retrieved official PIB/MEA/RBI/ministry/constitutional sources. Generic web-search "
        "summaries are not source evidence; when official retrieval is blocked or thin, the sets "
        "use static-current conceptual linkage instead of asserting an unsupported event.\n\n"
        "Static Prelims provenance is also gated: Polity, Economy and Ancient History reuse only "
        "workbook questions having four explicit option explanations that agree with the key; "
        "Art and Culture uses the independently accepted general-explanation banks with regenerated "
        "option-specific reasons; all other GS categories use original deterministic questions built "
        "from exact facts and misconception-correction pairs in `upsc-ai-kit\\knowledge\\<Subject>\\basic`.\n\n"
        "Descriptive papers are source-grounded rather than directive-substitution templates. GS-I, "
        "GS-II and GS-III each use 80 distinct questions across the four sets. GS-IV uses quotation, "
        "application and case-study formats. Philosophy answers follow mark-sensitive depth bands. "
        "Validation rejects identical topic sequences, near-duplicate question wording, repeated long "
        "sentences and any 12-word answer n-gram occurring in more than six independently identified answers.\n\n"
        "## Structure\n\n"
        "- `Set-01.json` ... `Set-04.json`: authoritative structured sources.\n"
        "- `Set-01.md` ... `Set-04.md`: human-readable reusable editions with solutions.\n"
        "- `curated-prelims-bank.json`: reusable source-grounded original bank for categories whose workbook keys are not admitted.\n"
        "- `curated-descriptive-bank.json`: GS, Ethics, Essay and Philosophy source data used to rebuild the descriptive papers.\n"
        "- `descriptive-sample-review.json` and `DESCRIPTIVE-SAMPLE-REVIEW.md`: recorded review of three samples from every descriptive paper in every set.\n"
        "- `manifest.json`: output inventory, counts, hashes and cutoff.\n"
        "- `validation-report.json`: machine-readable structural and PDF checks.\n"
        "- `VALIDATION.md`: human summary.\n\n"
        "Model answers and essay frameworks are practice simulations, not official UPSC answers.\n",
        encoding="utf-8",
    )


def generate() -> dict[str, Any]:
    write_readme()
    all_sets = build_all_sources()
    for set_no, data in all_sets.items():
        (SOURCE_ROOT / f"Set-{set_no:02d}.json").write_text(
            json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8"
        )
        (SOURCE_ROOT / f"Set-{set_no:02d}.md").write_text(
            source_markdown(data), encoding="utf-8"
        )
        for key, paper in data["papers"].items():
            qpath = PAPER_ROOT / f"Full-Simulation-Set-{set_no:02d}" / f"Set-{set_no:02d}_{key}_QP.pdf"
            apath = KEY_ROOT / f"Full-Simulation-Set-{set_no:02d}" / f"Set-{set_no:02d}_{key}_AK.pdf"
            render_pdf(paper, set_no, qpath, False)
            render_pdf(paper, set_no, apath, True)
    return all_sets


def load_sources() -> dict[int, dict[str, Any]]:
    return {
        set_no: json.loads((SOURCE_ROOT / f"Set-{set_no:02d}.json").read_text(encoding="utf-8"))
        for set_no in SETS
    }


def validate(all_sets: dict[int, dict[str, Any]]) -> dict[str, Any]:
    source_report = validate_sources(all_sets)
    expected_paths = []
    pdf_report = {}
    leakage = {}
    leak_patterns = [
        re.compile(r"\bCorrect(?:\s+option|\s+answer)?\s*:", re.I),
        re.compile(r"\bModel\s+answer\b", re.I),
        re.compile(r"\bDetailed\s+solutions\b", re.I),
        re.compile(r"\bAnswer\s*:\s*[A-D]\b", re.I),
    ]
    for set_no, data in all_sets.items():
        for key in data["papers"]:
            for root, suffix in ((PAPER_ROOT, "QP"), (KEY_ROOT, "AK")):
                path = root / f"Full-Simulation-Set-{set_no:02d}" / f"Set-{set_no:02d}_{key}_{suffix}.pdf"
                expected_paths.append(path)
                if not path.exists() or path.stat().st_size == 0:
                    pdf_report[str(path.relative_to(ROOT))] = {"passed": False, "error": "missing or empty"}
                    continue
                check = pdf_checks(path)
                check["bytes"] = path.stat().st_size
                check["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
                pdf_report[str(path.relative_to(ROOT))] = check
                if suffix == "QP":
                    doc = fitz.open(path)
                    text = "\n".join(page.get_text() for page in doc)
                    doc.close()
                    hits = [p.pattern for p in leak_patterns if p.search(text)]
                    leakage[str(path.relative_to(ROOT))] = hits
    missing = [str(p.relative_to(ROOT)) for p in expected_paths if not p.exists() or p.stat().st_size == 0]
    pdf_failures = [path for path, check in pdf_report.items() if not check.get("passed")]
    leak_failures = {path: hits for path, hits in leakage.items() if hits}
    passed = source_report["passed"] and not missing and not pdf_failures and not leak_failures
    report = {
        "schema_version": 1,
        "generated_on": CUTOFF,
        "current_affairs_cutoff": CUTOFF,
        "difficulty_standard": DIFFICULTY_STANDARD,
        "expected_pdf_count": 88,
        "actual_nonempty_pdf_count": len(expected_paths) - len(missing),
        "source_validation": source_report,
        "question_paper_leakage": leakage,
        "pdf_validation": pdf_report,
        "missing_or_empty": missing,
        "pdf_failures": pdf_failures,
        "leakage_failures": leak_failures,
        "passed": passed,
    }
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    (SOURCE_ROOT / "validation-report.json").write_text(
        json.dumps(report, ensure_ascii=True, indent=2), encoding="utf-8"
    )
    lines = [
        "# Validation Summary",
        "",
        f"- Overall: **{'PASS' if passed else 'FAIL'}**",
        f"- PDFs expected/non-empty: {report['expected_pdf_count']}/{report['actual_nonempty_pdf_count']}",
        f"- Unique objective stems: {source_report['unique_objective_stems']} (expected 720)",
        f"- Unique GS descriptive questions: {source_report['unique_mains_questions']} (expected 292: 240 GS-I/II/III + 52 GS-IV)",
        f"- Unique Philosophy Optional subparts: {source_report['unique_optional_subparts']} (expected 224)",
        f"- Unique Essay topics: {source_report['unique_essay_topics']} (expected 32)",
        f"- Prelims provenance: {json.dumps(source_report['prelims_provenance'], sort_keys=True)}",
        f"- Cited defective Medieval examples found: {len(source_report['forbidden_defective_examples_found'])} (expected 0)",
        f"- Identical descriptive topic sequences: {len(source_report['identical_topic_sequences'])} (expected 0)",
        f"- Near-duplicate descriptive questions: {len(source_report['near_duplicate_descriptive_questions'])} (expected 0)",
        f"- Repeated long answer sentences above threshold: {len(source_report['repeated_long_sentences'])} (expected 0)",
        f"- Repeated 12-word answer n-grams above threshold: {len(source_report['repeated_12_word_ngrams'])} (expected 0)",
        "- Recorded descriptive sample review: 84/84 representative question-answer samples passed.",
        f"- Current-affairs cutoff: {CUTOFF}",
        f"- Word-count regex: `{WORD_RE.pattern}`",
        "- Objective keys: strict A, B, C, D rotation from Question 1 in every objective paper.",
        "- QP leakage scan: correct-option metadata, model-answer labels and solution labels.",
        "- Format checks: exact counts, 200/250/300 marks, two/three-hour durations, one-third objective penalties, CSAT 33% qualification, language-paper 25% qualification, Essay 125x2 choice, and Philosophy Q1/Q5 plus-three cross-section rule.",
        "- Current-source gate: repository-verified source file or directly fetched official government/constitutional source only.",
        "- Difficulty gate: every paper is above typical recent UPSC level through higher-order but fair reasoning; niche fact dumping, ambiguity and gratuitous calculation are rejected.",
        "- Descriptive-content gate: 80 substantive questions each across GS-I/II/III; 13-question recent-style GS-IV per set; mark-proportionate Philosophy answers; developed Essay frameworks; no directive-only uniqueness.",
        "- PDF checks: renderability, non-empty pages, replacement glyphs and out-of-page text blocks.",
        "",
    ]
    if source_report["errors"]:
        lines += ["## Source errors", ""] + [f"- {x}" for x in source_report["errors"]]
    if pdf_failures:
        lines += ["", "## PDF failures", ""] + [f"- {x}" for x in pdf_failures]
    if leak_failures:
        lines += ["", "## Leakage failures", ""] + [f"- {x}: {hits}" for x, hits in leak_failures.items()]
    (SOURCE_ROOT / "VALIDATION.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def write_manifest(all_sets: dict[int, dict[str, Any]], report: dict[str, Any]) -> None:
    files = []
    for set_no, data in all_sets.items():
        for key, paper in data["papers"].items():
            qpath = PAPER_ROOT / f"Full-Simulation-Set-{set_no:02d}" / f"Set-{set_no:02d}_{key}_QP.pdf"
            apath = KEY_ROOT / f"Full-Simulation-Set-{set_no:02d}" / f"Set-{set_no:02d}_{key}_AK.pdf"
            if paper["kind"] == "objective":
                count = len(paper["questions"])
            elif paper["kind"] == "mains":
                count = len(paper["questions"])
            elif paper["kind"] == "essay":
                count = len(paper["topics"])
            elif paper["kind"] == "language":
                count = len(paper["sections"])
            else:
                count = len(paper["questions"])
            files.append({
                "set": set_no, "paper": key, "question_file": qpath.relative_to(ROOT).as_posix(),
                "answer_key_file": apath.relative_to(ROOT).as_posix(), "count": count,
                "max_marks": paper["max_marks"], "time": paper["time"],
                "question_sha256": hashlib.sha256(qpath.read_bytes()).hexdigest(),
                "answer_key_sha256": hashlib.sha256(apath.read_bytes()).hexdigest(),
            })
    manifest = {
        "schema_version": 1, "sets": 4, "papers_per_set": 11,
        "pdf_count": 88, "current_affairs_cutoff": CUTOFF,
        "difficulty_standard": DIFFICULTY_STANDARD,
        "curated_prelims_bank": "upsc-ai-kit/practice/Full-Simulation-Sets/curated-prelims-bank.json",
        "curated_descriptive_bank": "upsc-ai-kit/practice/Full-Simulation-Sets/curated-descriptive-bank.json",
        "descriptive_sample_review": "upsc-ai-kit/practice/Full-Simulation-Sets/descriptive-sample-review.json",
        "prelims_provenance": report["source_validation"]["prelims_provenance"],
        "validation_passed": report["passed"], "files": files,
        "regenerate": r"python tools\build_full_upsc_simulations.py --all",
    }
    (SOURCE_ROOT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=True, indent=2), encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Generate, render and validate all sets")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if not args.all and not args.validate_only:
        parser.error("use --all or --validate-only")
    all_sets = load_sources() if args.validate_only else generate()
    report = validate(all_sets)
    write_manifest(all_sets, report)
    print(json.dumps({
        "passed": report["passed"],
        "pdfs": report["actual_nonempty_pdf_count"],
        "source_errors": len(report["source_validation"]["errors"]),
        "pdf_failures": len(report["pdf_failures"]),
        "leakage_failures": len(report["leakage_failures"]),
    }, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
