from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

import fitz


TOPIC = Path(__file__).resolve().parent
REPO = TOPIC.parents[4]
TOOLS = REPO.parent / "tools"
PDF_DIR = TOPIC / "pdf"
VALIDATION = TOPIC / "VALIDATION.json"
G5_DIR = (
    REPO
    / "knowledge/Learner-v2-Refreshed/Philosophy/Paper-I-Western-Philosophy"
    / "learning-sessions/topic-08/g5"
)
CANONICAL = REPO / "knowledge/Philosophy/paper-1/western/Later-Wittgenstein.md"
KEY = "BCABBCDBBDACCADADDACBABCACCDACBBCACADABBDBCDADCDADB"
PDF_SOURCES = {
    "Revision-Guide.pdf": "REVISION-GUIDE.md",
    "MCQ-Questions.pdf": "MCQ-QUESTIONS.md",
    "MCQ-Solutions.pdf": "MCQ-SOLUTIONS.md",
    "Answer-Writing-Toolkit.pdf": "ANSWER-WRITING-TOOLKIT.md",
}
REQUIRED = [
    "README.md",
    "REVISION-GUIDE.md",
    "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md",
    "COVERAGE-LEDGER.md",
    "PRACTICE-LOG.md",
    "ANSWER-WRITING-TOOLKIT.md",
    "validate_package.py",
    *(f"pdf/{name}" for name in PDF_SOURCES),
]
PADDING_PATTERNS = [
    "on the stated view",
    "within the documented scope",
    "within the documented historical and doctrinal scope",
    "within the philosophical position described",
    "as part of the relevant analysis",
    "as a claim about the exact distinction under review",
    "as maintained within",
    "as asserted within",
    "as assessed under",
    "under the doctrine being assessed",
    "in the relevant context",
    "complete evidential and logical framework",
]
GENERIC_EXPLANATIONS = [
    "sequence confuses authors and texts",
    "none shares that formulation",
    "both descriptions reverse their positions",
    "each attribution reverses",
    "memberships and authorship are false",
]
WORD_BANDS = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
DIRECT_PYQS = [
    ("2018", "Q1(c)", 10),
    ("2019", "Q3(b)", 15),
    ("2020", "Q4(c)", 15),
    ("2022", "Q1(c)", 10),
    ("2023", "Q4(c)", 15),
    ("2024", "Q1(d)", 10),
    ("2025", "Q3(a)", 20),
    ("2026", "Q3(c)", 15),
]
OPTION_CUE_PATTERNS = {
    "semicolon": r";",
    "colon": r":",
    "em_or_en_dash": r"[—–]",
    "parentheses": r"[()]",
    "but": r"\bbut\b",
    "however": r"\bhowever\b",
    "whereas": r"\bwhereas\b",
    "although": r"\balthough\b",
    "yet": r"\byet\b",
    "though": r"\bthough\b",
    "despite": r"\bdespite\b",
    "absolutist_quantifier": (
        r"\b(?:universal|every|always|never|only|entirely)\b"
    ),
}


def normalise(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_`#>|]", " ", value)
    value = value.replace("–", "-").replace("—", "-").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", value).strip().casefold()


def words(value: str) -> list[str]:
    value = re.sub(r"```[a-zA-Z-]*\n?", "", value).replace("```", "")
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_`#>|]", " ", value)
    return re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", value, flags=re.UNICODE)


def parse_mcqs(text: str) -> list[dict[str, object]]:
    result = []
    for block in re.split(r"(?=^## MCQ \d+$)", text, flags=re.MULTILINE)[1:]:
        number = int(re.search(r"^## MCQ (\d+)$", block, flags=re.MULTILINE).group(1))
        lines = block.splitlines()
        stem = next(
            line.strip()
            for line in lines[1:]
            if line.strip() and not re.match(r"^[A-D]\. ", line)
        )
        options = {
            match.group(1): match.group(2).strip()
            for match in re.finditer(r"^([A-D])\. (.+)$", block, flags=re.MULTILINE)
        }
        answer = re.search(r"^\*\*Answer:\s*([A-D])\.\*\*$", block, flags=re.MULTILINE)
        explanations = {
            match.group(1): match.group(2).strip()
            for match in re.finditer(
                r"^- \*\*([A-D]):\*\* (.+)$", block, flags=re.MULTILINE
            )
        }
        result.append(
            {
                "number": number,
                "stem": stem,
                "options": options,
                "answer": answer.group(1) if answer else None,
                "explanations": explanations,
                "block": block,
            }
        )
    return result


def repeated_templates(mcqs: list[dict[str, object]]) -> dict[str, object]:
    suffixes: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    prefixes: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for item in mcqs:
        number = int(item["number"])
        correct = KEY[number - 1]
        option_tokens = {
            letter: re.findall(r"[a-z]+(?:-[a-z]+)?", option.casefold())
            for letter, option in dict(item["options"]).items()
        }
        for letter, option in dict(item["options"]).items():
            tokens = option_tokens[letter]
            bucket = 0 if letter == correct else 1
            for size in (3, 4, 5):
                if len(tokens) >= size:
                    prefix = " ".join(tokens[:size])
                    suffix = " ".join(tokens[-size:])
                    if not all(
                        len(other) >= size and " ".join(other[:size]) == prefix
                        for other in option_tokens.values()
                    ):
                        prefixes[prefix][bucket] += 1
                    if not all(
                        len(other) >= size and " ".join(other[-size:]) == suffix
                        for other in option_tokens.values()
                    ):
                        suffixes[suffix][bucket] += 1
    suspicious_suffixes = {
        phrase: {"correct": counts[0], "distractor": counts[1]}
        for phrase, counts in suffixes.items()
        if counts[1] >= 3 and counts[0] <= 1
    }
    suspicious_prefixes = {
        phrase: {"correct": counts[0], "distractor": counts[1]}
        for phrase, counts in prefixes.items()
        if counts[1] >= 3 and counts[0] <= 1
    }
    return {
        "suffix_frequency_correct_vs_distractor": suspicious_suffixes,
        "prefix_template_frequency_correct_vs_distractor": suspicious_prefixes,
        "pass": not suspicious_suffixes and not suspicious_prefixes,
    }


def cue_correlation_checks(mcqs: list[dict[str, object]]) -> dict[str, object]:
    correct_total = len(mcqs)
    distractor_total = correct_total * 3
    feature_results = {}
    unique_correct_markers = []
    all_distractors_marked = []
    failures = []
    for feature, pattern in OPTION_CUE_PATTERNS.items():
        correct_hits = []
        distractor_hits = []
        for item in mcqs:
            number = int(item["number"])
            correct = KEY[number - 1]
            hits = [
                letter
                for letter, option in dict(item["options"]).items()
                if re.search(pattern, option, flags=re.IGNORECASE)
            ]
            if hits == [correct]:
                unique_correct_markers.append(
                    {"mcq": number, "feature": feature, "correct_option": correct}
                )
            if correct not in hits and set(hits) == (set("ABCD") - {correct}):
                all_distractors_marked.append(
                    {"mcq": number, "feature": feature, "correct_option": correct}
                )
            for letter in hits:
                target = correct_hits if letter == correct else distractor_hits
                target.append(f"{number}{letter}")

        correct_count = len(correct_hits)
        distractor_count = len(distractor_hits)
        occurrence_count = correct_count + distractor_count
        correct_rate = correct_count / correct_total if correct_total else 0
        distractor_rate = (
            distractor_count / distractor_total if distractor_total else 0
        )
        correct_share = (
            correct_count / occurrence_count if occurrence_count else 0
        )
        rate_ratio = (
            correct_rate / distractor_rate
            if distractor_rate
            else (None if not correct_rate else "infinite")
        )
        exclusive_correct = correct_count >= 2 and distractor_count == 0
        exclusive_distractor = distractor_count >= 2 and correct_count == 0
        low_frequency_overwhelming = (
            2 <= occurrence_count <= 12 and correct_share > 0.50
        )
        common_feature_rate_imbalance = (
            occurrence_count > 12
            and correct_count >= 3
            and correct_rate > 2 * distractor_rate
            and correct_rate - distractor_rate >= 0.05
        )
        common_distractor_rate_imbalance = (
            occurrence_count > 12
            and distractor_count >= 6
            and distractor_rate > 4 * correct_rate
            and distractor_rate - correct_rate >= 0.20
        )
        feature_pass = not (
            exclusive_correct
            or exclusive_distractor
            or low_frequency_overwhelming
            or common_feature_rate_imbalance
            or common_distractor_rate_imbalance
        )
        if not feature_pass:
            failures.append(feature)
        feature_results[feature] = {
            "correct_count": correct_count,
            "distractor_count": distractor_count,
            "correct_option_rate_percent": round(100 * correct_rate, 2),
            "distractor_option_rate_percent": round(100 * distractor_rate, 2),
            "correct_share_of_occurrences_percent": round(100 * correct_share, 2),
            "correct_to_distractor_option_rate_ratio": rate_ratio,
            "correct_locations": correct_hits,
            "distractor_locations": distractor_hits,
            "exclusive_to_correct_options": exclusive_correct,
            "exclusive_to_distractor_options": exclusive_distractor,
            "low_frequency_overwhelming_correct_share": low_frequency_overwhelming,
            "common_feature_rate_imbalance": common_feature_rate_imbalance,
            "common_distractor_rate_imbalance": common_distractor_rate_imbalance,
            "pass": feature_pass,
        }
    return {
        "population": {
            "correct_options": correct_total,
            "distractor_options": distractor_total,
        },
        "thresholds": {
            "low_frequency_definition": "2-12 total option occurrences",
            "exclusive_correct_rule": "fail when a feature occurs in at least two correct options and zero distractors",
            "exclusive_distractor_rule": "fail when a feature occurs in at least two distractors and zero correct options",
            "low_frequency_rule": "fail when more than 50% of 2-12 occurrences are in correct options",
            "common_feature_rule": "for more than 12 occurrences, fail when correct-option rate exceeds 2x distractor-option rate by at least 5 percentage points",
            "common_distractor_rule": "for more than 12 occurrences, fail when distractor-option rate exceeds 4x correct-option rate by at least 20 percentage points",
            "within_question_rule": "fail when the correct option alone carries a listed marker",
            "all_distractors_rule": "fail when all three distractors and not the correct option carry a listed marker",
        },
        "features": feature_results,
        "unique_marker_only_on_correct_option": unique_correct_markers,
        "marker_on_all_distractors_not_correct": all_distractors_marked,
        "failed_features": failures,
        "pass": not failures and not unique_correct_markers and not all_distractors_marked,
    }


def option_checks(mcqs: list[dict[str, object]]) -> dict[str, object]:
    correct_lengths: list[int] = []
    distractor_lengths: list[int] = []
    correct_longest: list[int] = []
    uniquely_longest: list[int] = []
    outliers: list[int] = []
    incomplete: list[list[object]] = []
    punctuation = Counter()
    padded: list[list[object]] = []
    only_correct_lacks_template: list[int] = []
    finite = re.compile(
        r"\b(?:is|are|was|were|be|been|being|has|have|had|do|does|did|"
        r"can|could|may|might|must|shall|should|will|would|"
        r"\w+(?:s|ed))\b",
        flags=re.IGNORECASE,
    )
    for item in mcqs:
        number = int(item["number"])
        correct = KEY[number - 1]
        options = dict(item["options"])
        lengths = {letter: len(option) for letter, option in options.items()}
        correct_lengths.append(lengths[correct])
        distractor_lengths.extend(
            length for letter, length in lengths.items() if letter != correct
        )
        if lengths[correct] == max(lengths.values()):
            correct_longest.append(number)
        if lengths[correct] > max(
            length for letter, length in lengths.items() if letter != correct
        ):
            uniquely_longest.append(number)
        if (
            max(lengths.values()) - min(lengths.values()) > 70
            or max(lengths.values()) / min(lengths.values()) > 2.10
        ):
            outliers.append(number)
        template_by_letter: dict[str, bool] = {}
        for letter, option in options.items():
            lower = option.casefold()
            matches = [phrase for phrase in PADDING_PATTERNS if phrase in lower]
            template_by_letter[letter] = bool(matches)
            if matches:
                padded.append([number, letter, matches])
            punctuation[("correct" if letter == correct else "distractor", option[-1:])] += 1
            if (
                len(words(option)) < 8
                or not option[:1].isupper()
                or option[-1:] not in ".!?"
                or not finite.search(option)
            ):
                incomplete.append([number, letter, option])
        if (
            not template_by_letter[correct]
            and all(template_by_letter[letter] for letter in "ABCD" if letter != correct)
        ):
            only_correct_lacks_template.append(number)
    count = len(mcqs)
    correct_longest_rate = round(100 * len(correct_longest) / count, 2)
    unique_rate = round(100 * len(uniquely_longest) / count, 2)
    correct_period = punctuation[("correct", ".")]
    distractor_period = punctuation[("distractor", ".")]
    punctuation_gap = round(
        abs(correct_period / count - distractor_period / (count * 3)) * 100, 2
    )
    templates = repeated_templates(mcqs)
    cue_correlations = cue_correlation_checks(mcqs)
    return {
        "metric": "Unicode character count of each visible option",
        "correct_is_longest_count": len(correct_longest),
        "correct_is_longest_rate_percent": correct_longest_rate,
        "uniquely_longest_correct_count": len(uniquely_longest),
        "uniquely_longest_rate_percent": unique_rate,
        "correct_mean_characters": round(sum(correct_lengths) / len(correct_lengths), 3),
        "distractor_mean_characters": round(
            sum(distractor_lengths) / len(distractor_lengths), 3
        ),
        "comparability_threshold": "max-minus-min <= 70 and max/min <= 2.10",
        "comparability_outliers": outliers,
        "padding_matches": padded,
        "grammatically_incomplete_options": incomplete,
        "punctuation": {
            "correct_period_count": correct_period,
            "correct_period_rate_percent": round(100 * correct_period / count, 2),
            "distractor_period_count": distractor_period,
            "distractor_period_rate_percent": round(
                100 * distractor_period / (count * 3), 2
            ),
            "absolute_rate_gap_percent": punctuation_gap,
        },
        "token_and_punctuation_correlation": cue_correlations,
        "repeated_templates": templates,
        "only_correct_lacks_repeated_or_padded_template": only_correct_lacks_template,
        "pass": (
            15 <= correct_longest_rate <= 40
            and 5 <= unique_rate <= 30
            and not outliers
            and not padded
            and not incomplete
            and punctuation_gap == 0
            and cue_correlations["pass"]
            and templates["pass"]
            and not only_correct_lacks_template
        ),
    }


def explanation_checks(solutions: list[dict[str, object]]) -> dict[str, object]:
    failures = []
    checked = 0
    for item in solutions:
        number = int(item["number"])
        options = dict(item["options"])
        explanations = dict(item["explanations"])
        correct_letter = KEY[number - 1]
        correct = options[correct_letter].rstrip(".")
        for letter in "ABCD":
            checked += 1
            body = explanations.get(letter, "")
            if letter == correct_letter:
                continue
            wrong = options[letter].rstrip(".")
            required_wrong = f"False proposition: “{wrong}.”"
            required_correct = f"Correct replacement: “{correct}.”"
            reasons = []
            if required_wrong not in body:
                reasons.append("false proposition is not named exactly")
            if required_correct not in body:
                reasons.append("correct replacement is not supplied exactly")
            if len(words(body)) < 24:
                reasons.append("insufficient substantive content")
            lower = body.casefold()
            if any(pattern in lower for pattern in GENERIC_EXPLANATIONS):
                reasons.append("generic verdict pattern remains")
            if reasons:
                failures.append([number, letter, reasons])
    return {
        "checked": checked,
        "incorrect_options_checked": 153,
        "requirements": [
            "name the false proposition exactly",
            "state the correct replacement exactly",
            "include a substantive doctrinal rationale",
            "exclude listed generic-verdict patterns",
        ],
        "failures": failures,
        "pass": not failures,
    }


def markdown_link_checks() -> dict[str, object]:
    checked = 0
    broken = []
    for path in TOPIC.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = match.group(1).split("#", 1)[0]
            if not target or re.match(r"^[a-z]+://", target):
                continue
            checked += 1
            if not (path.parent / target).resolve().exists():
                broken.append({"file": path.name, "target": target})
    return {"checked": checked, "broken": broken, "pass": not broken}


def substantive_section(
    text: str, heading: str, next_heading_level: int, assertions: list[list[str]]
) -> dict[str, object]:
    start = text.find(heading)
    if start < 0:
        return {"heading": False, "words": 0, "assertions": [], "pass": False}
    body_start = start + len(heading)
    marker = "\n" + ("#" * next_heading_level) + " "
    end = text.find(marker, body_start)
    if end < 0:
        end = len(text)
    body = text[body_start:end]
    assertion_results = []
    normal = normalise(body)
    for alternatives in assertions:
        assertion_results.append(any(normalise(term) in normal for term in alternatives))
    return {
        "heading": True,
        "words": len(words(body)),
        "assertions": assertion_results,
        "pass": len(words(body)) >= 120 and all(assertion_results),
    }


def latest_g5_source(pattern: str) -> Path:
    matches = sorted(G5_DIR.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No g5 source matched {pattern}")
    return matches[-1]


def markdown_table_rows(text: str, heading: str) -> list[list[str]]:
    start = text.find(heading)
    if start < 0:
        return []
    tail = text[start + len(heading) :]
    next_heading = re.search(r"(?m)^## ", tail)
    section = tail[: next_heading.start()] if next_heading else tail
    rows = []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if cells and not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            rows.append(cells)
    return rows[1:] if rows else []


def anchored_section(text: str, anchor: str) -> str:
    match = re.search(rf"(?m)^{re.escape(anchor)}.*$", text)
    if not match:
        return ""
    level = len(anchor) - len(anchor.lstrip("#"))
    next_heading = re.search(
        rf"(?m)^#{{1,{level}}}\s+",
        text[match.end() :],
    )
    end = match.end() + next_heading.start() if next_heading else len(text)
    return text[match.start() : end]


def parse_source_candidates(text: str) -> dict[int, str]:
    candidates = {}
    pattern = re.compile(r"(?m)^#### (?:Remedial )?MCQ (\d+)\s*$")
    matches = list(pattern.finditer(text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end() : end]
        stem = next(
            (
                line.strip()
                for line in block.splitlines()
                if line.strip() and not re.match(r"^[A-D]\. ", line)
            ),
            "",
        )
        candidates[int(match.group(1))] = stem
    return candidates


def source_integrity_checks(
    revision: str, ledger: str, final_questions: list[dict[str, object]]
) -> dict[str, object]:
    session_path = latest_g5_source("*Complete-Learning-Session*.md")
    workbook_path = latest_g5_source("*Solved-Practice-Workbook*.md")
    source_paths = {
        "g5_session": session_path,
        "g5_workbook": workbook_path,
        "canonical": CANONICAL,
    }
    source_texts = {
        name: path.read_text(encoding="utf-8") for name, path in source_paths.items()
    }

    inventory_rows = markdown_table_rows(ledger, "## Mechanical source-cell inventory")
    inventory = {}
    inventory_failures = []
    for cells in inventory_rows:
        if len(cells) != 6 or not re.fullmatch(r"S\d{2}", cells[0]):
            inventory_failures.append({"row": cells, "reason": "malformed inventory row"})
            continue
        source_cell, coverage_cells, session_anchor, workbook_anchor, canonical_anchor, witnesses = cells
        anchors = {
            "g5_session": session_anchor,
            "g5_workbook": workbook_anchor,
            "canonical": canonical_anchor,
        }
        sections = {
            name: anchored_section(source_texts[name], anchor)
            for name, anchor in anchors.items()
        }
        witness_terms = [term.strip() for term in witnesses.split(";") if term.strip()]
        combined_source = "\n".join(sections.values())
        witness_results = {
            term: {
                "in_anchored_sources": normalise(term) in normalise(combined_source),
                "in_revision_guide": normalise(term) in normalise(revision),
            }
            for term in witness_terms
        }
        row_pass = (
            all(sections.values())
            and all(
                result["in_anchored_sources"] and result["in_revision_guide"]
                for result in witness_results.values()
            )
        )
        inventory[source_cell] = {
            "coverage_cells": [value.strip() for value in coverage_cells.split(",")],
            "anchors": anchors,
            "anchored_source_characters": {
                name: len(section) for name, section in sections.items()
            },
            "witnesses": witness_results,
            "pass": row_pass,
        }
        if not row_pass:
            inventory_failures.append({"source_cell": source_cell, "reason": "anchor or witness"})

    matrix_rows = markdown_table_rows(ledger, "## Explicit coverage matrix")
    coverage_for_question = {}
    for cells in matrix_rows:
        if len(cells) < 4 or not re.fullmatch(r"C\d{2}", cells[0]):
            continue
        match = re.fullmatch(r"(\d+)[–-](\d+)", cells[3])
        if not match:
            continue
        for number in range(int(match.group(1)), int(match.group(2)) + 1):
            coverage_for_question[number] = cells[0]

    mapping_rows = markdown_table_rows(ledger, "## Per-question lineage mapping")
    mappings = {}
    mapping_failures = []
    for cells in mapping_rows:
        if len(cells) != 6 or not cells[0].isdigit():
            mapping_failures.append({"row": cells, "reason": "malformed lineage row"})
            continue
        number = int(cells[0])
        source_cells = [value.strip() for value in cells[3].split(",") if value.strip()]
        candidate = None if cells[4] in {"—", "-", ""} else int(cells[4])
        mappings[number] = {
            "coverage_cell": cells[1],
            "lineage": cells[2].casefold(),
            "source_cells": source_cells,
            "g5_candidate": candidate,
            "tested_operation": cells[5],
        }

    source_candidates = parse_source_candidates(source_texts["g5_workbook"])
    final_by_number = {int(item["number"]): item for item in final_questions}
    for number, mapping in mappings.items():
        reasons = []
        if number not in final_by_number:
            reasons.append("final MCQ missing")
        if mapping["coverage_cell"] != coverage_for_question.get(number):
            reasons.append("coverage cell does not match matrix range")
        if not mapping["source_cells"] or any(
            cell not in inventory for cell in mapping["source_cells"]
        ):
            reasons.append("unknown source cell")
        candidate = mapping["g5_candidate"]
        if mapping["lineage"] == "adapted" and candidate not in source_candidates:
            reasons.append("adapted row lacks a valid g5 candidate")
        if mapping["lineage"] == "new" and candidate is not None:
            reasons.append("new row unexpectedly names a g5 candidate")
        if mapping["lineage"] not in {"adapted", "new"}:
            reasons.append("invalid lineage class")
        if reasons:
            mapping_failures.append({"mcq": number, "reasons": reasons})

    mapped_candidates = [
        mapping["g5_candidate"]
        for mapping in mappings.values()
        if mapping["g5_candidate"] is not None
    ]
    exact_retained = []
    for final_number, final in final_by_number.items():
        for source_number, source_stem in source_candidates.items():
            if normalise(str(final["stem"])) == normalise(source_stem):
                exact_retained.append(
                    {"final_mcq": final_number, "g5_candidate": source_number}
                )
    lineage_counts = Counter(mapping["lineage"] for mapping in mappings.values())
    unmapped_candidates = sorted(set(source_candidates) - set(mapped_candidates))
    complete_mapping = set(mappings) == set(range(1, len(final_questions) + 1))
    unique_mapping_rows = len(mapping_rows) == len(mappings)
    unique_adapted_candidates = len(mapped_candidates) == len(set(mapped_candidates))
    inventory_coverage = {
        coverage
        for item in inventory.values()
        for coverage in item["coverage_cells"]
    }
    matrix_coverage = set(coverage_for_question.values())
    source_files = {
        name: {
            "path": str(path.relative_to(REPO)),
            "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
        for name, path in source_paths.items()
    }
    return {
        "source_files_read": source_files,
        "source_cell_inventory": inventory,
        "source_cell_count": len(inventory),
        "source_inventory_failures": inventory_failures,
        "lineage_mapping_count": len(mappings),
        "lineage_counts": dict(lineage_counts),
        "source_candidate_count": len(source_candidates),
        "mapped_unique_source_candidates": len(set(mapped_candidates)),
        "unmapped_source_candidates": unmapped_candidates,
        "unmapped_source_candidate_count": len(unmapped_candidates),
        "retained_exact_stems": exact_retained,
        "mechanical_limitations": (
            "This gate verifies file identity, source anchors, term witnesses, matrix ranges "
            "and declared candidate links. It does not prove semantic completeness or the "
            "philosophical correctness of each adaptation."
        ),
        "pass": (
            len(inventory) > 0
            and not inventory_failures
            and complete_mapping
            and unique_mapping_rows
            and not mapping_failures
            and len(source_candidates) > 0
            and unique_adapted_candidates
            and inventory_coverage == matrix_coverage
            and not exact_retained
        ),
        "complete_mapping": complete_mapping,
        "unique_mapping_rows": unique_mapping_rows,
        "inventory_covers_matrix_cells": inventory_coverage == matrix_coverage,
        "unique_adapted_candidate_links": unique_adapted_candidates,
        "mapping_failures": mapping_failures,
    }


def rapid_revision_link_checks(revision: str, ledger: str) -> dict[str, object]:
    matrix_rows = markdown_table_rows(ledger, "## Explicit coverage matrix")
    expected = {}
    for cells in matrix_rows:
        if len(cells) >= 4 and re.fullmatch(r"C\d{2}", cells[0]):
            match = re.fullmatch(r"(\d+)[–-](\d+)", cells[3])
            if match:
                expected[int(cells[0][1:])] = (
                    int(match.group(1)),
                    int(match.group(2)),
                )
    actual = {}
    for number in sorted(expected):
        section = anchored_section(revision, f"### RAPID REVISION {number} —")
        match = re.search(r"\*\*Practice link:\*\* MCQs (\d+)[–-](\d+)", section)
        actual[number] = (
            (int(match.group(1)), int(match.group(2))) if match else None
        )
    return {
        "expected_from_coverage_matrix": {
            str(number): list(value) for number, value in expected.items()
        },
        "actual_from_revision_guide": {
            str(number): list(value) if value else None
            for number, value in actual.items()
        },
        "pass": len(expected) == 10 and actual == expected,
    }


def text_integrity_checks(status: list[str]) -> dict[str, object]:
    text_paths = sorted(
        path
        for path in TOPIC.rglob("*")
        if path.is_file() and path.suffix.casefold() in {".md", ".py", ".json"}
    )
    inspected = []
    failures = []
    for path in text_paths:
        relative = str(path.relative_to(REPO))
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            failures.append({"file": relative, "error": f"invalid UTF-8: {error}"})
            continue
        trailing = [
            number
            for number, line in enumerate(text.splitlines(), 1)
            if line.endswith((" ", "\t"))
        ]
        if trailing:
            failures.append({"file": relative, "trailing_whitespace_lines": trailing})
        inspected.append(
            {
                "file": relative,
                "bytes": len(raw),
                "lines": len(text.splitlines()),
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
    tracked_diff = subprocess.run(
        [
            "git",
            "-C",
            str(REPO),
            "--no-pager",
            "diff",
            "--check",
            "--",
            "practice/Offline-Revision-MCQ/INDEX.md",
            "practice/Offline-Revision-MCQ/STATUS.json",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    untracked = subprocess.run(
        [
            "git",
            "-C",
            str(REPO),
            "ls-files",
            "--others",
            "--exclude-standard",
            "--",
            str(TOPIC.relative_to(REPO)),
        ],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    if not inspected:
        failures.append({"error": "no package text content was examined"})
    if tracked_diff.returncode:
        failures.append(
            {"error": "tracked INDEX/STATUS diff check failed", "output": tracked_diff.stdout}
        )
    return {
        "mechanism": (
            "Stage-independent UTF-8 and trailing-whitespace audit of every package .md/.py/.json "
            "file, plus git diff --check for tracked INDEX.md and STATUS.json."
        ),
        "package_text_files_inspected": inspected,
        "package_text_file_count": len(inspected),
        "untracked_package_files_reported_by_git": untracked,
        "tracked_index_status_diff_check": {
            "exit_code": tracked_diff.returncode,
            "output": tracked_diff.stdout,
        },
        "failures": failures,
        "pass": bool(inspected) and not failures,
    }


def toolkit_checks(toolkit: str) -> dict[str, object]:
    ledgers = (
        REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2018-2025.md",
        REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2026.md",
    )
    ledger_text = "\n".join(path.read_text(encoding="utf-8") for path in ledgers)
    sections = re.split(r"(?=^## (?:\d+\.|Original \d+))", toolkit, flags=re.MULTILINE)[1:]
    pyq_results = {}
    original_results = {}
    for section in sections:
        heading = section.splitlines()[0]
        question_match = re.search(r"^\*\*Question:\*\* (.+)$", section, flags=re.MULTILINE)
        answer_match = re.search(
            r"### Timed (?:independent )?model answer\n\n(.*?)\n\n"
            r"\*\*Measured model-answer words:\*\* (\d+)",
            section,
            flags=re.DOTALL,
        )
        if not question_match or not answer_match:
            continue
        question = question_match.group(1)
        measured = len(words(answer_match.group(1)))
        stated = int(answer_match.group(2))
        marks_match = re.search(r"· (\d+) marks", heading)
        marks = int(marks_match.group(1))
        band = WORD_BANDS[marks]
        common = {
            "marks": marks,
            "band": list(band),
            "measured_words": measured,
            "stated_words": stated,
            "count_tolerance": 1,
            "matches_stated": abs(measured - stated) <= 1,
            "in_band": band[0] <= measured <= band[1],
            "demand_decoding": "demand decoding" in section.casefold(),
            "model_answer": "timed" in section.casefold() and "model answer" in section.casefold(),
            "qualification_or_criticism": bool(
                re.search(r"critici|qualification|objection|limit", section, re.IGNORECASE)
            ),
            "word_time_guidance": bool(
                re.search(r"word(?: and |/)time guidance", section, re.IGNORECASE)
            ),
        }
        if heading.startswith("## Original"):
            common["why_it_earns_marks"] = "Why this earns marks:" in section
            original_results[heading] = common
        else:
            identity = re.search(r"(\d{4}) (Q\d+\([a-z]\))", heading)
            label = f"{identity.group(1)} {identity.group(2)}"
            common["exact_prompt_match"] = normalise(question) in normalise(ledger_text)
            pyq_results[label] = common
    expected = {f"{year} {question}" for year, question, _ in DIRECT_PYQS}
    all_pyq = (
        set(pyq_results) == expected
        and all(
            all(
                value
                for key, value in result.items()
                if key
                in {
                    "matches_stated",
                    "in_band",
                    "demand_decoding",
                    "model_answer",
                    "qualification_or_criticism",
                    "word_time_guidance",
                    "exact_prompt_match",
                }
            )
            for result in pyq_results.values()
        )
    )
    all_original = len(original_results) == 3 and all(
        all(
            value
            for key, value in result.items()
            if key
            in {
                "matches_stated",
                "in_band",
                "demand_decoding",
                "model_answer",
                "qualification_or_criticism",
                "word_time_guidance",
                "why_it_earns_marks",
            }
        )
        for result in original_results.values()
    )
    return {
        "verified_pyqs": {
            "directly_owned_count": len(pyq_results),
            "parts": DIRECT_PYQS,
            "component_checks": pyq_results,
            "all_exact_and_complete": all_pyq,
        },
        "original_solved_practice": {
            "question_count": len(original_results),
            "solutions": original_results,
            "all_complete": all_original,
        },
        "portable_provenance": {
            "ledger_files_exist": all(path.is_file() for path in ledgers),
            "learner_practice_not_official_keys": (
                "learner-practice answers, never official UPSC answer keys" in toolkit
            ),
        },
        "pass": all_pyq
        and all_original
        and all(path.is_file() for path in ledgers)
        and "learner-practice answers, never official UPSC answer keys" in toolkit,
    }


def pdf_checks(path: Path) -> dict[str, object]:
    blank_pages = []
    replacement_glyphs = 0
    out_of_bounds = []
    overlap_pages = []
    raw_markdown = []
    page_texts = []
    with fitz.open(path) as document:
        for page_number, page in enumerate(document, 1):
            text = page.get_text("text")
            page_texts.append(text)
            if len(text.strip()) < 20 and not page.get_images(full=True):
                blank_pages.append(page_number)
            replacement_glyphs += text.count("�")
            for line in text.splitlines():
                if (
                    "**" in line
                    or "`" in line
                    or re.match(r"^\s*#{1,6}\s+", line)
                    or re.search(r"\[[^\]]+\]\([^)]+\)", line)
                ):
                    raw_markdown.append({"page": page_number, "text": line[:160]})
            blocks = [
                block
                for block in page.get_text("blocks")
                if str(block[4]).strip() and not str(block[4]).startswith("HIDX")
            ]
            for block in blocks:
                x0, y0, x1, y1 = block[:4]
                if x0 < -1 or y0 < -1 or x1 > page.rect.width + 1 or y1 > page.rect.height + 1:
                    out_of_bounds.append(page_number)
                    break
            if page_number == 2:
                continue
            for index, first in enumerate(blocks):
                first_rect = fitz.Rect(first[:4])
                for second in blocks[index + 1 :]:
                    second_rect = fitz.Rect(second[:4])
                    intersection = first_rect & second_rect
                    if intersection.is_empty:
                        continue
                    smaller = min(first_rect.get_area(), second_rect.get_area())
                    if smaller and intersection.get_area() / smaller > 0.35:
                        overlap_pages.append(page_number)
                        break
                if overlap_pages and overlap_pages[-1] == page_number:
                    break
        page_count = document.page_count
    heading_order = []
    if path.name.startswith("MCQ-"):
        for page_number, text in enumerate(page_texts[2:], 3):
            heading_order.extend(
                (int(number), page_number)
                for number in re.findall(r"(?m)^MCQ (\d+)\s*$", text)
            )
    order_valid = not heading_order or [
        number for number, _ in heading_order
    ] == sorted({number for number, _ in heading_order})
    return {
        "bytes": path.stat().st_size,
        "pages": page_count,
        "blank_pages": sorted(set(blank_pages)),
        "replacement_glyphs": replacement_glyphs,
        "out_of_bounds_text_pages": sorted(set(out_of_bounds)),
        "content_overlap_pages": sorted(set(overlap_pages)),
        "page_order_validated": order_valid,
        "raw_markdown_artifacts": raw_markdown,
        "pass": (
            page_count > 0
            and not blank_pages
            and replacement_glyphs == 0
            and not out_of_bounds
            and not overlap_pages
            and order_valid
            and not raw_markdown
        ),
    }


def regenerate_pdfs() -> dict[str, object]:
    sys.path.insert(0, str(TOOLS))
    import unicode_markdown_pdf

    started_at = datetime.now().astimezone()
    descriptors = {
        "Revision-Guide.pdf": "Philosophy Optional · Paper I · Western Philosophy · Topic 08",
        "MCQ-Questions.pdf": "51-question closed-book practice bank · no answer key",
        "MCQ-Solutions.pdf": "Explanations, traps, repairs and coverage mapping",
        "Answer-Writing-Toolkit.pdf": "Eight verified PYQs and three original solved answers",
    }
    regenerated = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        output = PDF_DIR / pdf_name
        if output.exists():
            output.unlink()
        unicode_markdown_pdf.build_pdf(
            TOPIC / source_name,
            output,
            internal_index=True,
            index_title="CONTENTS",
            cover_descriptor=descriptors[pdf_name],
            footer_label=f"Later Wittgenstein | {source_name.removesuffix('.md')}",
        )
        regenerated[pdf_name] = {
            "source": source_name,
            "exists_after_generation": output.is_file(),
            "bytes": output.stat().st_size if output.is_file() else 0,
            "modified_at": (
                datetime.fromtimestamp(output.stat().st_mtime).astimezone().isoformat()
                if output.is_file()
                else None
            ),
            "sha256": (
                hashlib.sha256(output.read_bytes()).hexdigest()
                if output.is_file()
                else None
            ),
        }
    return {
        "requested": True,
        "started_at": started_at.isoformat(),
        "files": regenerated,
        "all_four_regenerated": (
            set(regenerated) == set(PDF_SOURCES)
            and all(item["exists_after_generation"] for item in regenerated.values())
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regenerate", action="store_true")
    args = parser.parse_args()
    regeneration = {
        "requested": False,
        "files": {},
        "all_four_regenerated": False,
    }
    if args.regenerate:
        regeneration = regenerate_pdfs()

    readme = (TOPIC / "README.md").read_text(encoding="utf-8")
    questions_text = (TOPIC / "MCQ-QUESTIONS.md").read_text(encoding="utf-8")
    solutions_text = (TOPIC / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8")
    revision = (TOPIC / "REVISION-GUIDE.md").read_text(encoding="utf-8")
    toolkit = (TOPIC / "ANSWER-WRITING-TOOLKIT.md").read_text(encoding="utf-8")
    ledger = (TOPIC / "COVERAGE-LEDGER.md").read_text(encoding="utf-8")
    questions = parse_mcqs(questions_text)
    solutions = parse_mcqs(solutions_text)

    failures = []
    required = {name: (TOPIC / name).is_file() for name in REQUIRED}
    if not all(required.values()):
        failures.append("required_files")

    numbering = {
        "question_count": len(questions),
        "solution_count": len(solutions),
        "exact_match": [item["number"] for item in questions]
        == [item["number"] for item in solutions]
        == list(range(1, 52)),
        "all_questions_have_four_options": all(
            set(dict(item["options"])) == set("ABCD") for item in questions
        ),
        "question_solution_prompts_match": all(
            normalise(str(q["stem"])) == normalise(str(s["stem"]))
            and q["options"] == s["options"]
            for q, s in zip(questions, solutions)
        ),
    }
    numbering["pass"] = all(
        value for key, value in numbering.items() if key not in {"question_count", "solution_count"}
    ) and len(questions) == len(solutions) == 51
    if not numbering["pass"]:
        failures.append("mcq_numbering")

    leakage_markers = [
        "**Answer:",
        "Option explanations:",
        "Examiner trap",
        "Repair action:",
        "Coverage mapping:",
        "PYQ linkage:",
        "Correct answer:",
    ]
    question_leakage = {marker: marker in questions_text for marker in leakage_markers}
    if any(question_leakage.values()):
        failures.append("question_leakage")

    source_norms = {
        normalise(str(item["stem"])) for item in questions
    } | {
        normalise(option)
        for item in questions
        for option in dict(item["options"]).values()
    }
    cross_leakage = {}
    for name, text in {
        "REVISION-GUIDE.md": revision,
        "ANSWER-WRITING-TOOLKIT.md": toolkit,
    }.items():
        matches = sorted(value for value in source_norms if len(value) >= 45 and value in normalise(text))
        cross_leakage[name] = {"matches": matches, "pass": not matches}
    if not all(item["pass"] for item in cross_leakage.values()):
        failures.append("cross_file_answer_leakage")

    neutral_titles = all(
        re.search(rf"^## MCQ {number}$", questions_text, flags=re.MULTILINE)
        for number in range(1, 52)
    )
    option_quality = option_checks(questions)
    if not option_quality["pass"]:
        failures.append("option_quality")

    answers = [str(item["answer"]) for item in solutions]
    max_run = 1
    run = 1
    for previous, current in zip(answers, answers[1:]):
        run = run + 1 if previous == current else 1
        max_run = max(max_run, run)
    answer_pattern = {
        "distribution": dict(Counter(answers)),
        "maximum_consecutive_same_answer": max_run,
        "mechanical_abcd_rotation": "".join(answers)
        in ("ABCD" * 14, "BCDA" * 14, "CDAB" * 14, "DABC" * 14),
        "key": "".join(answers),
        "pass": "".join(answers) == KEY and max_run <= 2,
    }
    if not answer_pattern["pass"]:
        failures.append("answer_pattern")

    marker_counts = {
        marker: solutions_text.count(marker)
        for marker in (
            "**Answer:",
            "**Option explanations:**",
            "**Examiner trap",
            "**Repair action:**",
            "**Coverage mapping:**",
            "**PYQ linkage:**",
        )
    }
    solutions_complete = {
        **marker_counts,
        "expected_each": 51,
        "pass": all(count == 51 for count in marker_counts.values()),
    }
    if not solutions_complete["pass"]:
        failures.append("solutions_complete")

    explanations = explanation_checks(solutions)
    if not explanations["pass"]:
        failures.append("distractor_explanations")

    stem_pairs = []
    highest = (0.0, None)
    for index, first in enumerate(questions):
        for second in questions[index + 1 :]:
            ratio = SequenceMatcher(
                None, normalise(str(first["stem"])), normalise(str(second["stem"]))
            ).ratio()
            if ratio > highest[0]:
                highest = (ratio, [first["number"], second["number"]])
            if ratio >= 0.86:
                stem_pairs.append([first["number"], second["number"], round(ratio, 3)])
    deduplication = {
        "exact_duplicate_stems_absent": len({normalise(str(item["stem"])) for item in questions}) == 51,
        "highest_stem_similarity": round(highest[0], 3),
        "highest_similarity_pair": highest[1],
        "substantive_similarity_flags": stem_pairs,
        "final_count": 51,
        "pass": not stem_pairs,
    }
    if not deduplication["pass"]:
        failures.append("deduplication")

    source_lineage = source_integrity_checks(revision, ledger, questions)
    if not source_lineage["pass"]:
        failures.append("source_lineage")
    rapid_links = rapid_revision_link_checks(revision, ledger)
    if not rapid_links["pass"]:
        failures.append("rapid_revision_links")

    toolkit_result = toolkit_checks(toolkit)
    if not toolkit_result["pass"]:
        failures.append("toolkit")
    front_matter = revision.split("### Learning Roadmap", 1)[0]
    front_normal = normalise(front_matter)
    provenance_wording = {
        "required_accuracy_statement": (
            "source-cell retention is checked mechanically"
            in front_normal
            and "does not prove semantic completeness" in front_normal
        ),
        "forbidden_claims": [
            phrase
            for phrase in (
                "all substantive canonical cells are reorganised and retained without omission",
                "preserved verbatim",
                "copied unchanged",
                "fixed question target",
            )
            if phrase in front_normal
        ],
    }
    provenance_wording["pass"] = (
        provenance_wording["required_accuracy_statement"]
        and not provenance_wording["forbidden_claims"]
    )
    if not provenance_wording["pass"]:
        failures.append("provenance_wording")

    links = markdown_link_checks()
    if not links["pass"]:
        failures.append("markdown_links")

    pdf_results = {
        name: pdf_checks(PDF_DIR / name) for name in PDF_SOURCES
    }
    if not all(result["pass"] for result in pdf_results.values()):
        failures.append("pdfs")
    readme_claims_four_pdf_regeneration = "regenerate all four pdfs" in readme.casefold()
    regeneration["readme_claims_four_pdf_regeneration"] = (
        readme_claims_four_pdf_regeneration
    )
    regeneration["readme_consistent"] = (
        not readme_claims_four_pdf_regeneration
        or regeneration["all_four_regenerated"]
    )
    if not regeneration["readme_consistent"]:
        failures.append("pdf_regeneration")

    temp_files = [
        str(path.relative_to(TOPIC))
        for pattern in ("*.render.html", "*.layout-pass.pdf", "*.finalized.pdf", "*.tmp", "*_data.py")
        for path in TOPIC.rglob(pattern)
    ]
    temp_files.extend(
        str(path.relative_to(TOPIC))
        for path in TOPIC.rglob("__pycache__")
        if path.is_dir()
    )
    temp_files.extend(
        str(path.relative_to(TOPIC)) for path in TOPIC.rglob("*.pyc")
    )
    temp_files = sorted(set(temp_files))
    if temp_files:
        failures.append("temporary_files")

    status = subprocess.run(
        ["git", "-C", str(REPO), "--no-pager", "status", "--short"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    text_integrity = text_integrity_checks(status)
    if not text_integrity["pass"]:
        failures.append("text_integrity")
    index = (REPO / "practice/Offline-Revision-MCQ/INDEX.md").read_text(encoding="utf-8")
    status_json = json.loads(
        (REPO / "practice/Offline-Revision-MCQ/STATUS.json").read_text(encoding="utf-8")
    )
    status_expectations = {
        "topic_08_validated": any(
            item.get("topic") == "08 Later Wittgenstein"
            and item.get("status") == "validated"
            and item.get("mcq_count") == 51
            for item in status_json["validated_topics"]
        ),
        "next_topic": "09 Phenomenology (Husserl)" in status_json["next_action"],
    }
    index_expectations = {
        "topic_08_listed": "08 Later Wittgenstein" in index and "51 MCQs" in index,
        "next_topic": "09 Phenomenology (Husserl)" in index,
    }
    if not all(status_expectations.values()) or not all(index_expectations.values()):
        failures.append("repository_status_files")

    practice_log = (TOPIC / "PRACTICE-LOG.md").read_text(encoding="utf-8")
    practice_log_blank = not re.search(
        r"(?im)^\s*(?:score|attempt|answer)\s*:\s*\S+", practice_log
    )
    if not practice_log_blank:
        failures.append("practice_log")

    report = {
        "schema_version": 8,
        "topic": "08 Later Wittgenstein",
        "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "result": "PASS" if not failures else "FAIL",
        "result_gate": "PASS only when every recorded check passes",
        "pdf_generation": {
            "mechanism": "C:/up/tools/unicode_markdown_pdf.py build_pdf() via installed Chrome and PyMuPDF",
            **regeneration,
        },
        "checks": {
            "required_files": required,
            "mcq_numbering": numbering,
            "question_leakage": question_leakage,
            "cross_file_answer_leakage": cross_leakage,
            "revision_guide_separation": {
                "solved_mcq_headings": len(re.findall(r"^## MCQ \d+$", revision, re.MULTILINE)),
                "correct_answer_markers": revision.count("**Answer:"),
                "option_explanation_markers": revision.count("**Option explanations:**"),
                "pass": not re.search(r"^## MCQ \d+$", revision, re.MULTILINE)
                and "**Answer:" not in revision
                and "**Option explanations:**" not in revision,
            },
            "neutral_titles": {
                "questions_all_exactly_mcq_number": neutral_titles,
                "revealing_title_count": 0 if neutral_titles else 1,
            },
            "option_formatting_cues": option_quality,
            "answer_pattern": answer_pattern,
            "solutions_complete": solutions_complete,
            "specific_distractor_explanations": explanations,
            "deduplication": deduplication,
            "source_lineage": source_lineage,
            "rapid_revision_practice_links": rapid_links,
            **toolkit_result,
            "revision_front_matter_provenance": provenance_wording,
            "current_affairs_nonfabrication": (
                "no direct verified current-affairs event is established" in revision.casefold()
            ),
            "markdown_links": links,
            "pdfs": pdf_results,
            "practice_log_blank_template": practice_log_blank,
            "temporary_files_left": temp_files,
            "text_and_diff_integrity": text_integrity,
            "git_status_awareness": {
                "short_status": status,
                "topic_package_is_untracked": any(
                    "08-Later-Wittgenstein" in line and line.startswith("??") for line in status
                ),
            },
            "status_expectations": status_expectations,
            "index_expectations": index_expectations,
        },
        "failures": failures,
    }
    VALIDATION.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    page_summary = ", ".join(
        f"{name}: {value['pages']}" for name, value in pdf_results.items()
    )
    print(
        f"{report['result']}: 51 MCQs; "
        f"correct-longest={option_quality['correct_is_longest_rate_percent']}%; "
        f"unique-longest={option_quality['uniquely_longest_rate_percent']}%; "
        f"PDF pages={{{page_summary}}}"
    )
    if failures:
        print("Failures:", ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
