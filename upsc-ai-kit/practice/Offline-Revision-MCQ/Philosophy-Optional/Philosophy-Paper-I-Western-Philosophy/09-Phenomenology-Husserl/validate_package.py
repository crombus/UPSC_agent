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
MCQ_AUDIT = TOPIC / "MCQ-AUDIT.json"
PYQ_DEMAND_AUDIT = TOPIC / "PYQ-DEMAND-AUDIT.json"
G4_DIR = (
    REPO
    / "knowledge/Learner-v2-Refreshed/Philosophy/Paper-I-Western-Philosophy"
    / "learning-sessions/topic-09/g4"
)
CANONICAL = REPO / "knowledge/Philosophy/paper-1/western/Phenomenology-Husserl.md"
KEY = "DADDADAACCBCAACDBABABCAABBDBBDCDCCDCBDBDCDCCBABADAACB"
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
    "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json",
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
GENERIC_OPTION_WRAPPERS = [
    "the proposed answer for this question is",
    "this formulation states the proposed relation",
    "it also identifies the methodological role",
    "it further distinguishes this view",
]
ANCHOR_STOPWORDS = {
    "a",
    "an",
    "and",
    "answer",
    "are",
    "as",
    "at",
    "be",
    "because",
    "been",
    "being",
    "but",
    "by",
    "claim",
    "correct",
    "did",
    "distinction",
    "do",
    "does",
    "each",
    "for",
    "formulation",
    "from",
    "has",
    "have",
    "in",
    "is",
    "it",
    "its",
    "not",
    "of",
    "on",
    "option",
    "or",
    "position",
    "proposition",
    "relevant",
    "statement",
    "that",
    "the",
    "their",
    "them",
    "therefore",
    "these",
    "they",
    "this",
    "those",
    "to",
    "under",
    "was",
    "were",
    "which",
    "while",
    "with",
    "within",
}
WORD_BANDS = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
DIRECT_PYQS = [
    ("2019", "Q1(b)", 10),
    ("2020", "Q1(c)", 10),
    ("2021", "Q4(a)", 20),
    ("2022", "Q1(d)", 10),
    ("2023", "Q3(b)", 15),
    ("2024", "Q4(b)", 15),
    ("2025", "Q4(a)", 20),
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


def anchor_content_words(value: str) -> list[str]:
    return [
        token.casefold().replace("’", "'")
        for token in words(value)
        if token.casefold().replace("’", "'") not in ANCHOR_STOPWORDS
        and len(token) > 2
    ]


def anchor_normalise(value: str) -> str:
    return " ".join(
        token.casefold().replace("’", "'")
        for token in words(value)
    )


def anchor_list_issues(
    anchors: object,
    carrier: str,
    label: str,
    minimum: int,
) -> list[str]:
    if not isinstance(anchors, list) or len(anchors) < minimum:
        return [f"{label} must declare at least {minimum} anchors"]
    issues = []
    for anchor in anchors:
        text = str(anchor).strip()
        if len(anchor_content_words(text)) < 2:
            issues.append(f"{label} anchor is not doctrinally specific: {text!r}")
        if anchor_normalise(text) not in anchor_normalise(carrier):
            issues.append(f"{label} anchor is absent from its audited text: {text!r}")
    return issues


def rationale_fingerprint(value: str) -> str:
    tokens = [
        token.casefold().replace("’", "'")
        for token in words(value)
        if token.casefold().replace("’", "'") not in ANCHOR_STOPWORDS
    ]
    return " ".join(tokens)


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
    generic_wrappers: list[list[object]] = []
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
            max(lengths.values()) - min(lengths.values()) > 200
            or max(lengths.values()) / min(lengths.values()) > 2.20
        ):
            outliers.append(number)
        template_by_letter: dict[str, bool] = {}
        for letter, option in options.items():
            lower = option.casefold()
            matches = [phrase for phrase in PADDING_PATTERNS if phrase in lower]
            template_by_letter[letter] = bool(matches)
            if matches:
                padded.append([number, letter, matches])
            wrapper_matches = [
                phrase for phrase in GENERIC_OPTION_WRAPPERS if phrase in lower
            ]
            if wrapper_matches:
                generic_wrappers.append([number, letter, wrapper_matches])
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
        "comparability_threshold": "max-minus-min <= 200 and max/min <= 2.20; locked answer-cue rates remain 15-40% correct-longest and 5-30% uniquely-longest",
        "comparability_outliers": outliers,
        "padding_matches": padded,
        "generic_wrapper_matches": generic_wrappers,
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
            and not generic_wrappers
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
    rationales = []
    try:
        audit_payload = json.loads(MCQ_AUDIT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return {
            "checked": 0,
            "failures": [["manifest", str(error)]],
            "pass": False,
        }
    audit_rows = {
        int(row["number"]): row
        for row in audit_payload.get("questions", [])
        if isinstance(row, dict) and str(row.get("number", "")).isdigit()
    }
    validation_spec = audit_payload.get("rationale_validation", {})
    generic_controls = validation_spec.get("generic_negative_controls", [])
    near_threshold = float(
        validation_spec.get("near_duplicate_similarity_threshold", 0.94)
    )
    for item in solutions:
        number = int(item["number"])
        options = dict(item["options"])
        explanations = dict(item["explanations"])
        correct_letter = KEY[number - 1]
        correct = options[correct_letter].rstrip(".")
        audit_row = audit_rows.get(number, {})
        audit_options = audit_row.get("options", {})
        for letter in "ABCD":
            checked += 1
            body = explanations.get(letter, "")
            rationale_match = re.search(r"\bRationale:\s*(.+)$", body)
            rationale = rationale_match.group(1).strip() if rationale_match else ""
            reasons = []
            audit_option = audit_options.get(letter, {})
            if not rationale:
                reasons.append("explicit rationale field is missing")
            if audit_option.get("rationale") != rationale:
                reasons.append("rationale does not match the parsed audit manifest")
            if letter == correct_letter:
                required_correct = f"Correct proposition: “{correct}.”"
                if required_correct not in body:
                    reasons.append("correct proposition is not named exactly")
                reasons.extend(
                    anchor_list_issues(
                        audit_option.get("rationale_anchors"),
                        rationale,
                        "correct rationale",
                        2,
                    )
                )
                rationales.append((number, letter, rationale, "correct"))
                if reasons:
                    failures.append([number, letter, reasons])
                continue
            wrong = options[letter].rstrip(".")
            required_wrong = f"False proposition: “{wrong}.”"
            required_correct = f"Correct replacement: “{correct}.”"
            if required_wrong not in body:
                reasons.append("false proposition is not named exactly")
            if required_correct not in body:
                reasons.append("correct replacement is not supplied exactly")
            reasons.extend(
                anchor_list_issues(
                    audit_option.get("false_proposition_anchors"),
                    wrong,
                    "false-proposition",
                    1,
                )
            )
            reasons.extend(
                anchor_list_issues(
                    audit_option.get("correction_anchors"),
                    rationale,
                    "distractor correction",
                    2,
                )
            )
            rationales.append((number, letter, rationale, "distractor"))
            if reasons:
                failures.append([number, letter, reasons])

    repeated_normalized = []
    grouped = defaultdict(list)
    for number, letter, rationale, kind in rationales:
        grouped[normalise(rationale)].append(f"{number}{letter}:{kind}")
    for rationale, locations in grouped.items():
        if rationale and len(locations) > 1:
            repeated_normalized.append(
                {"normalized_rationale": rationale, "locations": locations}
            )

    repeated_fingerprints = []
    fingerprint_groups = defaultdict(list)
    for number, letter, rationale, kind in rationales:
        fingerprint_groups[rationale_fingerprint(rationale)].append(
            f"{number}{letter}:{kind}"
        )
    for fingerprint, locations in fingerprint_groups.items():
        if fingerprint and len(locations) > 1:
            repeated_fingerprints.append(
                {"fingerprint": fingerprint, "locations": locations}
            )

    near_duplicate_rationales = []
    rationale_records = [
        {
            "mcq": number,
            "option": letter,
            "rationale": rationale,
            "kind": kind,
        }
        for number, letter, rationale, kind in rationales
    ]
    for index, first in enumerate(rationale_records):
        for second in rationale_records[index + 1 :]:
            ratio = SequenceMatcher(
                None,
                normalise(first["rationale"]),
                normalise(second["rationale"]),
            ).ratio()
            if ratio >= near_threshold:
                near_duplicate_rationales.append(
                    {
                        "first": f"{first['mcq']}{first['option']}:{first['kind']}",
                        "second": f"{second['mcq']}{second['option']}:{second['kind']}",
                        "similarity": round(ratio, 3),
                    }
                )

    anchor_frequency = Counter(
        normalise(str(anchor))
        for row in audit_rows.values()
        for option in row.get("options", {}).values()
        for field in ("rationale_anchors", "correction_anchors")
        for anchor in option.get(field, [])
    )
    repeated_declared_anchors = {
        anchor: count for anchor, count in anchor_frequency.items() if anchor and count > 2
    }
    generic_false_acceptances = []
    for number, row in audit_rows.items():
        for letter, option in row.get("options", {}).items():
            field = (
                "rationale_anchors"
                if option.get("truth_value") is True
                else "correction_anchors"
            )
            anchors = option.get(field, [])
            for control_number, control in enumerate(generic_controls, 1):
                if anchors and all(
                    anchor_normalise(str(anchor)) in anchor_normalise(str(control))
                    for anchor in anchors
                ):
                    generic_false_acceptances.append(
                        {
                            "mcq": number,
                            "option": letter,
                            "control": control_number,
                            "anchor_field": field,
                        }
                    )
    return {
        "checked": checked,
        "incorrect_options_checked": 159,
        "correct_options_checked": 53,
        "requirements": [
            "all 212 rationales reproduce the parsed audit manifest",
            "correct rationales contain at least two declared doctrinal anchors",
            "each distractor quotes the exact false proposition and exact correction",
            "each distractor rationale contains at least two declared correction anchors",
            "generic negative controls satisfy no option's anchor set",
            "normalized and near-duplicate rationale bodies are rejected",
        ],
        "validation_basis": (
            "Pass/fail is proposition-specific and manifest-driven; rationale word counts "
            "and enumerated stock-sentence blacklists are not acceptance criteria."
        ),
        "generic_negative_controls": generic_controls,
        "generic_control_false_acceptances": generic_false_acceptances,
        "repeated_normalized_rationale_bodies": repeated_normalized,
        "repeated_normalized_body_fingerprints": repeated_fingerprints,
        "near_duplicate_rationale_bodies": near_duplicate_rationales,
        "excessively_reused_declared_anchors": repeated_declared_anchors,
        "failures": failures,
        "pass": (
            checked == 212
            and not failures
            and not generic_false_acceptances
            and not repeated_normalized
            and not repeated_fingerprints
            and not near_duplicate_rationales
            and not repeated_declared_anchors
        ),
    }


def mcq_audit_checks(
    questions: list[dict[str, object]], solutions: list[dict[str, object]]
) -> dict[str, object]:
    failures = []
    try:
        payload = json.loads(MCQ_AUDIT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return {
            "manifest": str(MCQ_AUDIT.relative_to(REPO)),
            "failures": [f"manifest unreadable: {error}"],
            "pass": False,
        }
    rows = payload.get("questions", [])
    schema_version = payload.get("schema_version")
    rationale_validation = payload.get("rationale_validation", {})
    generic_controls = rationale_validation.get("generic_negative_controls", [])
    if schema_version != 2:
        failures.append(
            {"manifest": "schema_version", "reasons": ["schema version must be 2"]}
        )
    if not isinstance(generic_controls, list) or len(generic_controls) < 2:
        failures.append(
            {
                "manifest": "rationale_validation",
                "reasons": ["at least two generic negative controls are required"],
            }
        )
    by_number = {
        int(row["number"]): row
        for row in rows
        if isinstance(row, dict) and str(row.get("number", "")).isdigit()
    }
    question_by_number = {int(item["number"]): item for item in questions}
    solution_by_number = {int(item["number"]): item for item in solutions}
    for number in range(1, 54):
        row = by_number.get(number)
        question = question_by_number.get(number)
        solution = solution_by_number.get(number)
        reasons = []
        if not row or not question or not solution:
            failures.append({"mcq": number, "reasons": ["missing manifest or bank row"]})
            continue
        stem = str(row.get("stem", ""))
        refs = row.get("named_referents", [])
        options = row.get("options", {})
        answer = row.get("answer")
        if normalise(stem) != normalise(str(question["stem"])):
            reasons.append("manifest stem does not match visible stem")
        if (
            not isinstance(refs, list)
            or not refs
            or any(normalise(str(ref)) not in normalise(stem) for ref in refs)
        ):
            reasons.append("stem lacks one or more declared named referents")
        if re.search(r"\b(?:it|they|this|that)\b", stem.casefold()) and not refs:
            reasons.append("stem relies on an unnamed pronoun")
        if answer != KEY[number - 1]:
            reasons.append("manifest answer does not match locked key")
        unique_reason = str(row.get("unique_answer_reason", "")).strip()
        reasons.extend(
            anchor_list_issues(
                row.get("unique_answer_anchors"),
                unique_reason,
                "unique-answer",
                2,
            )
        )
        if set(options) != set("ABCD"):
            reasons.append("manifest does not contain exactly four keyed options")
        else:
            true_options = [
                letter for letter in "ABCD"
                if options[letter].get("truth_value") is True
            ]
            if true_options != [answer]:
                reasons.append("truth-value audit does not identify exactly one keyed answer")
            visible_options = dict(question["options"])
            solution_explanations = dict(solution["explanations"])
            correct_text = visible_options.get(str(answer), "")
            for letter in "ABCD":
                audit_option = options[letter]
                visible = visible_options.get(letter, "")
                if audit_option.get("text") != visible:
                    reasons.append(f"{letter} manifest text differs from visible option")
                rationale = str(audit_option.get("rationale", "")).strip()
                if f"Rationale: {rationale}" not in solution_explanations.get(letter, ""):
                    reasons.append(f"{letter} rationale is not reproduced in solutions")
                if letter == answer:
                    reasons.extend(
                        f"{letter} {issue}"
                        for issue in anchor_list_issues(
                            audit_option.get("rationale_anchors"),
                            rationale,
                            "correct rationale",
                            2,
                        )
                    )
                else:
                    if audit_option.get("false_proposition") != visible:
                        reasons.append(f"{letter} false proposition is not explicit and exact")
                    if audit_option.get("specific_correction") != correct_text:
                        reasons.append(f"{letter} correction is not the exact keyed proposition")
                    reasons.extend(
                        f"{letter} {issue}"
                        for issue in anchor_list_issues(
                            audit_option.get("false_proposition_anchors"),
                            str(audit_option.get("false_proposition", "")),
                            "false-proposition",
                            1,
                        )
                    )
                    reasons.extend(
                        f"{letter} {issue}"
                        for issue in anchor_list_issues(
                            audit_option.get("correction_anchors"),
                            rationale,
                            "distractor correction",
                            2,
                        )
                    )
        for control_number, control in enumerate(generic_controls, 1):
            if row.get("unique_answer_anchors") and all(
                anchor_normalise(str(anchor)) in anchor_normalise(str(control))
                for anchor in row["unique_answer_anchors"]
            ):
                reasons.append(
                    f"generic negative control {control_number} satisfies unique-answer anchors"
                )
        if reasons:
            failures.append({"mcq": number, "reasons": reasons})
    return {
        "manifest": str(MCQ_AUDIT.relative_to(REPO)),
        "schema_version": schema_version,
        "manifest_question_count": len(rows),
        "parsed_question_count": len(by_number),
        "all_visible_stems_have_declared_named_referents": not any(
            "named referents" in reason
            for failure in failures
            for reason in failure["reasons"]
        ),
        "all_questions_have_exactly_one_keyed_true_proposition": not any(
            "exactly one keyed answer" in reason
            for failure in failures
            for reason in failure["reasons"]
        ),
        "mechanical_limitations": (
            "This parsed proposition-level audit verifies exact stem and option alignment, "
            "declared referents, one keyed true proposition, explicit false propositions, "
            "specific corrections, and literal item-specific rationale anchors. Truth values were manually "
            "reviewed against the cited Topic 09 sources; parsing cannot independently prove "
            "philosophical truth or eliminate every reasonable interpretive dispute."
        ),
        "failures": failures,
        "pass": len(rows) == len(by_number) == 53 and not failures,
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


def doctrinal_consistency_checks(
    revision: str,
    toolkit: str,
    questions: list[dict[str, object]],
) -> dict[str, object]:
    combined = "\n".join((revision, toolkit))
    required_claims = {
        "categorial_forms_and_states_of_affairs": (
            "categorial forms and states of affairs" in normalise(combined)
        ),
        "categorial_beyond_simple_sensuous_intuition": (
            "beyond simple sensuous intuition" in normalise(combined)
        ),
        "eidetic_intuition_free_variation": (
            "eidetic intuition apprehends essences through free variation"
            in normalise(combined)
            or (
                "wesensschau" in normalise(combined)
                and "free imaginative variation" in normalise(combined)
            )
        ),
        "intuitions_related_not_identical": (
            "related" in normalise(combined)
            and "not identical" in normalise(combined)
        ),
        "reductions_have_distinct_functions": (
            "distinct functions" in normalise(combined)
            or "operations are related but not one mechanical" in normalise(combined)
        ),
        "no_universal_staircase": (
            "not a mandatory universal staircase" in normalise(combined)
            or "not one compulsory staircase" in normalise(combined)
        ),
        "eidetic_variation_independent_of_completed_transcendental_reduction": (
            "without awaiting a completed transcendental reduction"
            in normalise(combined)
            or "does not logically await a completed transcendental reduction"
            in normalise(combined)
        ),
    }
    forbidden_patterns = {
        "wesensschau_equated_with_categorial_intuition": (
            r"wesensschau.{0,100}\b(?:is|as)\b.{0,20}categorial intuition"
        ),
        "categorial_eidetic_slash_conflation": r"categorial\s*/\s*eidetic intuition",
        "categorial_intuition_gives_essential_structures": (
            r"categorial intuition.{0,80}gives?.{0,30}essential structures"
        ),
        "mandatory_reduction_staircase_heading": r"the staircase of reductions",
        "suspension_as_only_route_to_essence": r"only by suspending the factual",
        "bracketing_as_eidetic_gateway": r"bracketing is the gateway to the eidetic reduction",
        "shared_universality_conflation": (
            r"eidetic intuition and categorial intuition.{0,100}grasp universality"
        ),
    }
    forbidden_hits = {
        name: [
            match.group(0)
            for match in re.finditer(pattern, combined, flags=re.IGNORECASE | re.DOTALL)
        ]
        for name, pattern in forbidden_patterns.items()
    }

    inference_records = []
    for item in questions:
        number = int(item["number"])
        correct = KEY[number - 1]
        inference_records.append(
            {
                "number": number,
                "body": normalise(
                    f"{item['stem']} {dict(item['options'])[correct]}"
                ),
            }
        )
    inference_similarity_flags = []
    highest = (0.0, None)
    for index, first in enumerate(inference_records):
        for second in inference_records[index + 1 :]:
            ratio = SequenceMatcher(None, first["body"], second["body"]).ratio()
            if ratio > highest[0]:
                highest = (ratio, [first["number"], second["number"]])
            if ratio >= 0.75:
                inference_similarity_flags.append(
                    [first["number"], second["number"], round(ratio, 3)]
                )

    by_number = {int(item["number"]): item for item in questions}
    q9 = by_number.get(9, {})
    q13 = by_number.get(13, {})
    q13_stem = normalise(str(q13.get("stem", "")))
    duplicate_repair = {
        "mcq_9_tests_epoché_definition": (
            "epoché or bracketing" in normalise(str(q9.get("stem", "")))
        ),
        "mcq_13_is_application_case": (
            "remembered city" in q13_stem and "second move" in q13_stem
        ),
        "mcq_13_tests_phenomenological_redirection": (
            "phenomenological reduction redirects inquiry"
            in normalise(str(dict(q13.get("options", {})).get("A", "")))
        ),
        "mcq_9_and_13_correct_propositions_differ": (
            normalise(str(dict(q9.get("options", {})).get(KEY[8], "")))
            != normalise(str(dict(q13.get("options", {})).get(KEY[12], "")))
        ),
    }
    return {
        "required_claims": required_claims,
        "forbidden_patterns": forbidden_hits,
        "mcq_inference_similarity_threshold": 0.75,
        "highest_inference_similarity": round(highest[0], 3),
        "highest_inference_similarity_pair": highest[1],
        "inference_similarity_flags": inference_similarity_flags,
        "mcq_9_13_duplicate_repair": duplicate_repair,
        "pass": (
            all(required_claims.values())
            and not any(forbidden_hits.values())
            and not inference_similarity_flags
            and all(duplicate_repair.values())
        ),
    }


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


def latest_g4_source(pattern: str) -> Path:
    matches = sorted(G4_DIR.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No g4 source matched {pattern}")
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
    session_path = latest_g4_source("*Complete-Learning-Session*.md")
    workbook_path = latest_g4_source("*Solved-Practice-Workbook*.md")
    source_paths = {
        "g4_session": session_path,
        "g4_workbook": workbook_path,
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
            "g4_session": session_anchor,
            "g4_workbook": workbook_anchor,
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
            "g4_candidate": candidate,
            "tested_operation": cells[5],
        }

    source_candidates = parse_source_candidates(source_texts["g4_workbook"])
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
        candidate = mapping["g4_candidate"]
        if mapping["lineage"] == "adapted" and candidate not in source_candidates:
            reasons.append("adapted row lacks a valid g4 candidate")
        if mapping["lineage"] == "new" and candidate is not None:
            reasons.append("new row unexpectedly names a g4 candidate")
        if mapping["lineage"] not in {"adapted", "new"}:
            reasons.append("invalid lineage class")
        if reasons:
            mapping_failures.append({"mcq": number, "reasons": reasons})

    mapped_candidates = [
        mapping["g4_candidate"]
        for mapping in mappings.values()
        if mapping["g4_candidate"] is not None
    ]
    exact_retained = []
    for final_number, final in final_by_number.items():
        for source_number, source_stem in source_candidates.items():
            if normalise(str(final["stem"])) == normalise(source_stem):
                exact_retained.append(
                    {"final_mcq": final_number, "g4_candidate": source_number}
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
    untracked_diff_checks = []
    for relative in untracked:
        if not relative.casefold().endswith((".md", ".py", ".json")):
            continue
        probe = subprocess.run(
            [
                "git",
                "-C",
                str(REPO),
                "--no-pager",
                "diff",
                "--no-index",
                "--check",
                "--",
                "NUL",
                str(REPO / relative),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        output = (probe.stdout + probe.stderr).strip()
        untracked_diff_checks.append(
            {
                "file": relative,
                "exit_code": probe.returncode,
                "whitespace_diagnostics": output,
                "pass": not output,
            }
        )
        if output:
            failures.append(
                {
                    "file": relative,
                    "error": "git diff --no-index --check reported whitespace errors",
                    "output": output,
                }
            )
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
        "untracked_file_integrity_gate": {
            "all_untracked_text_files_were_inspected": all(
                not path.casefold().endswith((".md", ".py", ".json"))
                or any(item["file"].replace("\\", "/") == path.replace("\\", "/") for item in inspected)
                for path in untracked
            ),
            "stage_independent": True,
            "git_diff_no_index_checks": untracked_diff_checks,
        },
        "tracked_index_status_diff_check": {
            "exit_code": tracked_diff.returncode,
            "output": tracked_diff.stdout,
        },
        "failures": failures,
        "pass": bool(inspected) and not failures and all(
            not path.casefold().endswith((".md", ".py", ".json"))
            or any(item["file"].replace("\\", "/") == path.replace("\\", "/") for item in inspected)
            for path in untracked
        ),
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
    unsupported_marks_claims = [
        phrase
        for phrase in (
            "noesis-noema, hyle/morphe, principle of principles",
            "it names the source by section",
            "all four *Prolegomena* arguments",
            "integrates Frege with the correct date",
        )
        if phrase.casefold() in toolkit.casefold()
    ]
    why_sections = re.findall(r"^\*\*Why this earns marks:\*\* .+$", toolkit, re.MULTILINE)
    marks_logic_accuracy = {
        "why_sections_expected": 10,
        "why_sections_found": len(why_sections),
        "unsupported_claims": unsupported_marks_claims,
        "pass": len(why_sections) == 10 and not unsupported_marks_claims,
    }
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
        "marks_logic_accuracy": marks_logic_accuracy,
        "pass": all_pyq
        and all_original
        and all(path.is_file() for path in ledgers)
        and "learner-practice answers, never official UPSC answer keys" in toolkit
        and marks_logic_accuracy["pass"],
    }


def pyq_demand_audit_checks(toolkit: str) -> dict[str, object]:
    failures = []
    try:
        payload = json.loads(PYQ_DEMAND_AUDIT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return {
            "manifest": str(PYQ_DEMAND_AUDIT.relative_to(REPO)),
            "failures": [f"manifest unreadable: {error}"],
            "pass": False,
        }
    rows = payload.get("pyqs", [])
    expected = {f"{year} {question}": marks for year, question, marks in DIRECT_PYQS}
    seen = set()
    results = {}
    for row in rows:
        identity = str(row.get("id", ""))
        seen.add(identity)
        reasons = []
        if identity not in expected:
            failures.append({"pyq": identity, "reasons": ["unexpected PYQ identity"]})
            continue
        if row.get("marks") != expected[identity]:
            reasons.append("marks do not match the owned-PYQ ledger")
        section_match = re.search(
            rf"(?ms)^## \d+\. {re.escape(identity)} · \d+ marks\s+(.*?)(?=^## )",
            toolkit,
        )
        section = section_match.group(1) if section_match else ""
        question_match = re.search(r"^\*\*Question:\*\* (.+)$", section, re.MULTILINE)
        answer_match = re.search(
            r"### Timed independent model answer\n\n(.*?)\n\n"
            r"\*\*Measured model-answer words:\*\*",
            section,
            flags=re.DOTALL,
        )
        if not section or not question_match or not answer_match:
            reasons.append("toolkit section, exact question or timed answer is missing")
            answer = ""
        else:
            answer = answer_match.group(1)
            if normalise(question_match.group(1)) != normalise(str(row.get("question", ""))):
                reasons.append("manifest question does not match toolkit question")
        limb_results = []
        limbs = row.get("demand_limbs", [])
        if not isinstance(limbs, list) or not limbs:
            reasons.append("demand-limb list is empty")
        for limb in limbs if isinstance(limbs, list) else []:
            anchors = limb.get("anchors", [])
            anchor_results = {
                str(anchor): normalise(str(anchor)) in normalise(answer)
                for anchor in anchors
            }
            limb_pass = bool(anchor_results) and all(anchor_results.values())
            limb_results.append(
                {
                    "limb": limb.get("limb"),
                    "anchors": anchor_results,
                    "pass": limb_pass,
                }
            )
            if not limb_pass:
                reasons.append(f"demand limb missing anchors: {limb.get('limb')}")
        results[identity] = {
            "marks": row.get("marks"),
            "demand_limb_count": len(limbs) if isinstance(limbs, list) else 0,
            "limbs": limb_results,
            "pass": not reasons,
        }
        if reasons:
            failures.append({"pyq": identity, "reasons": reasons})
    return {
        "manifest": str(PYQ_DEMAND_AUDIT.relative_to(REPO)),
        "owned_pyq_count": len(rows),
        "expected_owned_pyqs": sorted(expected),
        "component_checks": results,
        "mechanical_limitations": (
            "This gate checks exact prompt identity and literal presence of all declared "
            "demand-limb anchors inside each timed answer. It does not infer whether those "
            "anchors are argued correctly, sufficiently developed or worthy of a particular mark."
        ),
        "failures": failures,
        "pass": len(rows) == 7 and seen == set(expected) and not failures,
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
        "Revision-Guide.pdf": "Philosophy Optional · Paper I · Western Philosophy · Topic 09",
        "MCQ-Questions.pdf": "53-question closed-book practice bank · no answer key",
        "MCQ-Solutions.pdf": "Explanations, traps, repairs and coverage mapping",
        "Answer-Writing-Toolkit.pdf": "Seven verified PYQs and three original solved answers",
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
            footer_label=f"Phenomenology (Husserl) | {source_name.removesuffix('.md')}",
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
        == list(range(1, 54)),
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
    ) and len(questions) == len(solutions) == 53
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
        for number in range(1, 54)
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
        "mechanical_abcd_rotation": any(
            "".join(answers) == (rotation * 14)[:len(answers)]
            for rotation in ("ABCD", "BCDA", "CDAB", "DABC")
        ),
        "key": "".join(answers),
        "pass": "".join(answers) == KEY and max_run <= 2 and not any(
            "".join(answers) == (rotation * 14)[:len(answers)]
            for rotation in ("ABCD", "BCDA", "CDAB", "DABC")
        ),
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
        "expected_each": 53,
        "pass": all(count == 53 for count in marker_counts.values()),
    }
    if not solutions_complete["pass"]:
        failures.append("solutions_complete")

    explanations = explanation_checks(solutions)
    if not explanations["pass"]:
        failures.append("distractor_explanations")
    mcq_audit = mcq_audit_checks(questions, solutions)
    if not mcq_audit["pass"]:
        failures.append("mcq_proposition_audit")

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
        "exact_duplicate_stems_absent": len({normalise(str(item["stem"])) for item in questions}) == 53,
        "highest_stem_similarity": round(highest[0], 3),
        "highest_similarity_pair": highest[1],
        "substantive_similarity_flags": stem_pairs,
        "final_count": 53,
        "pass": not stem_pairs,
    }
    if not deduplication["pass"]:
        failures.append("deduplication")

    source_lineage = source_integrity_checks(revision, ledger, questions)
    if not source_lineage["pass"]:
        failures.append("source_lineage")
    doctrinal_consistency = doctrinal_consistency_checks(
        revision, toolkit, questions
    )
    if not doctrinal_consistency["pass"]:
        failures.append("doctrinal_consistency")
    rapid_links = rapid_revision_link_checks(revision, ledger)
    if not rapid_links["pass"]:
        failures.append("rapid_revision_links")

    toolkit_result = toolkit_checks(toolkit)
    if not toolkit_result["pass"]:
        failures.append("toolkit")
    pyq_demand_audit = pyq_demand_audit_checks(toolkit)
    if not pyq_demand_audit["pass"]:
        failures.append("pyq_demand_audit")
    front_matter = revision.split("### Learning Roadmap", 1)[0]
    front_normal = normalise(front_matter)
    provenance_documents = {
        "revision_front_matter": front_matter,
        "readme": readme,
        "coverage_ledger": ledger,
    }
    forbidden_provenance_phrases = (
        "all substantive canonical cells are reorganised and retained without omission",
        "preserved verbatim",
        "sliced verbatim",
        "each canonical passage exactly once",
        "copied unchanged",
        "fixed question target",
    )
    provenance_wording = {
        "required_accuracy_statement": (
            "source-cell retention is checked mechanically"
            in front_normal
            and "does not prove semantic completeness" in front_normal
            and "substantive source cells were reconciled, adapted and mapped"
            in front_normal
            and "repeated apparatus was consolidated" in front_normal
        ),
        "documents_scanned": sorted(provenance_documents),
        "forbidden_claims": {
            name: [
                phrase
                for phrase in forbidden_provenance_phrases
                if phrase in normalise(text)
            ]
            for name, text in provenance_documents.items()
        },
    }
    provenance_wording["pass"] = (
        provenance_wording["required_accuracy_statement"]
        and not any(provenance_wording["forbidden_claims"].values())
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
        "topic_09_validated": any(
            item.get("topic") == "09 Phenomenology (Husserl)"
            and item.get("status") == "validated"
            and item.get("mcq_count") == 53
            for item in status_json["validated_topics"]
        ),
        "next_topic": "10 Existentialism" in status_json["next_action"],
    }
    index_expectations = {
        "topic_09_listed": "09 Phenomenology (Husserl)" in index and "53 MCQs" in index,
        "next_topic": "10 Existentialism" in index,
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
        "schema_version": 11,
        "topic": "09 Phenomenology (Husserl)",
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
            "mcq_proposition_audit": mcq_audit,
            "deduplication": deduplication,
            "doctrinal_consistency_and_inference_distinctness": doctrinal_consistency,
            "source_lineage": source_lineage,
            "rapid_revision_practice_links": rapid_links,
            **toolkit_result,
            "pyq_demand_audit": pyq_demand_audit,
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
                    "09-Phenomenology-Husserl" in line and line.startswith("??") for line in status
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
        f"{report['result']}: 53 MCQs; "
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
