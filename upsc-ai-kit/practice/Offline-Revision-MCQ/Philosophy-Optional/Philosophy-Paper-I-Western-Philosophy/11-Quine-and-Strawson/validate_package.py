from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

import fitz
sys.dont_write_bytecode = True
import formal_validation


TOPIC = Path(__file__).resolve().parent
REPO = TOPIC.parents[4]
TOOLS = REPO.parent / "tools"
PDF_DIR = TOPIC / "pdf"
VALIDATION = TOPIC / "VALIDATION.json"
FORMAL_AUDIT = TOPIC / "FORMAL-COVERAGE-AUDIT.json"
FORMAL_REVIEW = TOPIC / "FORMAL-COVERAGE-REVIEW.json"
MCQ_COUNT = 61
DIRECT_PYQS = [
    ("2018", "Q1(e)", 10), ("2018", "Q2(c)", 15),
    ("2019", "Q1(e)", 10), ("2020", "Q3(b)", 15),
    ("2021", "Q3(b)", 15), ("2021", "Q3(c)", 15),
    ("2023", "Q4(a)", 20), ("2024", "Q4(c)", 15),
    ("2025", "Q4(b)", 15), ("2026", "Q3(a)", 20),
]
WORD_BANDS = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
AUTHORITATIVE_FORMAL_ROOT = Path(
    r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final"
)
FORBIDDEN_DERIVATIVE_FORMAL_ROOT = REPO.parent / "learning_package_final"
FORMAL_SOURCE_DIR = (
    AUTHORITATIVE_FORMAL_ROOT
    / "Philosophy-Optional/Philosophy-Paper-I-—-Western-Philosophy/11-Quine-and-Strawson"
)
FORMAL_SOURCES = {
    "session": FORMAL_SOURCE_DIR / "Learning-Session.md",
    "workbook": FORMAL_SOURCE_DIR / "Solved-Practice-Workbook.md",
}
EXPECTED_PANEL_TOTAL = 42
EXPECTED_EXTERNAL_OBLIGATIONS = {
    "T11-ROUTE-T03-EMPIRICISM",
    "T11-ROUTE-T04-KANT-GENERAL",
    "T11-ROUTE-T04-BOUNDS-OF-SENSE",
    "T11-ROUTE-T06-DESCRIPTIONS",
    "T11-ROUTE-T07-POSITIVISM",
    "T11-ROUTE-T08-LATER-WITTGENSTEIN",
    "T11-ROUTE-P2-SOUL",
}
CORRELATION_ALLOWLIST = {
    "analytic synthetic",
    "basic particulars",
    "descriptive metaphysics",
    "naturalized epistemology",
    "ontological commitment",
    "spatio temporal",
}
CORRELATION_STOPWORDS = {
    "a", "an", "and", "as", "at", "be", "because", "by", "for", "from", "in",
    "into", "is", "it", "its", "not", "of", "on", "or", "that", "the",
    "their", "this", "through", "to", "while", "with", "all", "but", "every",
    "false", "our", "what",
}
LINEAGE_STOPWORDS = CORRELATION_STOPWORDS | {
    "does", "how", "mean", "means", "most", "quine", "strawson", "should",
    "what", "which", "why",
}
LEAKED_ANSWER_LABELS = ()
EXPECTED_KEYS = "AABAADBCDBCACCDCCACBCCBADBCCBDDADBABCDDBDDABBDDCDCACABAABADBA"
DOCTRINAL_ANCHORS = {
    1: ("Quine attacks empiricism from within", "two projects are kept distinct"),
    2: ("Both are critics of empiricism", "private-given starting point"),
    3: ("Quine's method is naturalism", "revisionary metaphysics"),
    4: ("empiricism without the dogmas", "bodies persons not private sense-data"),
    5: ("non-circular boundary", "alleged analytic class"),
    6: ("Extensional interchangeability over-generates", "analyticity under analysis"),
    7: ("Listing analytic sentences by fiat", "concept of analyticity"),
    8: ("distinction's reality via ordinary use", "behavioural boundary"),
    9: ("individual verificationism", "private confirmation-conditions"),
    10: ("Confirmation holism", "periphery touches experience"),
    11: ("revisability to logic", "minimum mutilation"),
    12: ("differential practical revisability", "do not redefine analyticity"),
    13: ("conjunction of hypothesis and auxiliaries is false", "leaves underdetermined"),
    14: ("Scope is the key difference", "extension to logic"),
    15: ("Neptune vindicated auxiliary revision", "general relativity"),
    16: ("Popper concedes the logic", "methodological rules"),
    17: ("rival translations share stimulus meaning", "individuation apparatus"),
    18: ("Reference of sub-sentential terms", "whole manuals"),
    19: ("evidence for meaning is public verbal behaviour", "behaviourist premise"),
    20: ("normal underdetermination", "physics and meaning"),
    21: ("bound variables", "On What There Is"),
    22: ("philosophy is continuous with science", "sensory input yields theory"),
    23: ("Reference is relative", "background manual"),
    24: ("anti-private-meaning holism", "in order as it is"),
    25: ("identification-independence", "not of simplicity or necessity"),
    26: ("Re-identification", "public space-time"),
    27: ("auditory world can support re-identification", "master-sound"),
    28: ("descriptive", "Individuals"),
    29: ("unanalysable into mind", "person concept"),
    30: ("asymmetry of ascription", "P-predicate"),
    31: ("Self-ascription requires other-ascription", "M- and P-predicates"),
    32: ("self-refuting", "owned by a person"),
    33: ("people not sentences refer", "use on an occasion"),
    34: ("failed presupposition", "truth-value gap"),
    35: ("quantifier asserting unique existence", "whole statement is false"),
    36: ("private given", "Quine's internal reform"),
    37: ("Revisable web", "indispensable framework"),
    38: ("public criteria", "private given"),
    39: ("convergence is in target", "differences remain sharp"),
    40: ("layered verdict", "all-or-nothing choice"),
    41: ("ontological-commitment slogan", "Duhem restricted"),
    42: ("principled boundary", "over-strong reading"),
    43: ("Davidson accepts indeterminacy", "choice of measurement scale"),
    44: ("contrast within metaphysics", "not a rejection"),
    45: ("co-authored by Grice and Strawson", "Strawson alone"),
    46: ("not reducible to behaviour", "not a logical behaviourist"),
    47: ("Russellian falsity", "failed-assertion treatment"),
    48: ("minimum mutilation", "change of subject"),
    49: ("quantifiers of regimented best science", "slogan and argument"),
    50: ("systematically remap objects", "theory-independent standpoint"),
    51: ("further fact of meaning", "ordinary scientific underdetermination"),
    52: ("basic objects of reference", "feature-placing expressions"),
    53: ("same item again", "enduring public anchors"),
    54: ("first-person and third-person uses", "hidden egos"),
    55: ("occasion of use", "asserted content"),
    56: ("unsuccessful use or assertion", "meaningfulness of the sentence-type"),
    57: ("causal psychology", "normative question"),
    58: ("within our conceptual scheme", "uniqueness and reality"),
    59: ("free-will work", "after Individuals has been completed"),
    60: ("science-continuous revision", "do not merge the projects"),
    61: ("principal argumentative burden", "Logical Positivism and Russell or early Wittgenstein"),
}
FORBIDDEN_OPTION_FILLER = (
    "qualification remains explicit",
    "within the scope of question",
    "this proposition is assessed",
    "the wording is evaluated",
    "its claim is assessed",
    "the statement is evaluated",
)
G5_DIR = (
    REPO
    / "knowledge/Learner-v2-Refreshed/Philosophy/Paper-I-Western-Philosophy"
    / "learning-sessions/topic-11/g5"
)
CANONICAL = REPO / "knowledge/Philosophy/paper-1/western/Quine-Strawson.md"
EARLIER_SESSION = (
    REPO / "knowledge/Philosophy/Western-Philosophy/learning-sessions/Quine-Strawson"
    / "Quine-Strawson_Layered-Complete-Learning-Session_2026-08-19.md"
)
EARLIER_WORKBOOK = (
    REPO / "knowledge/Philosophy/Western-Philosophy/learning-sessions/Quine-Strawson"
    / "Quine-Strawson_Layered-Solved-Practice-Workbook_2026-08-19.md"
)
PDF_SOURCES = {
    "Revision-Guide.pdf": "REVISION-GUIDE.md",
    "MCQ-Questions.pdf": "MCQ-QUESTIONS.md",
    "MCQ-Solutions.pdf": "MCQ-SOLUTIONS.md",
    "Answer-Writing-Toolkit.pdf": "ANSWER-WRITING-TOOLKIT.md",
}
PDF_DESCRIPTORS = {
    "Revision-Guide.pdf": "Philosophy Optional · Paper I · Western Philosophy · Topic 11",
    "MCQ-Questions.pdf": "61-question closed-book practice bank · no answer key",
    "MCQ-Solutions.pdf": "Proposition-specific explanations and repairs",
    "Answer-Writing-Toolkit.pdf": "Ten verified PYQs and six original solved answers",
}
REQUIRED = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md", "COVERAGE-LEDGER.md", "PRACTICE-LOG.md",
    "ANSWER-WRITING-TOOLKIT.md", "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json", "FORMAL-COVERAGE-REVIEW.json",
    "FORMAL-COVERAGE-AUDIT.json", "formal_validation.py", "VALIDATION.json",
    "validate_package.py",
    *(f"pdf/{name}" for name in PDF_SOURCES),
]


def normalise(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_`#>|]", " ", value)
    value = value.replace("–", "-").replace("—", "-").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", value).strip().casefold()


def words(value: str) -> list[str]:
    value = re.sub(r"```[a-zA-Z-]*\n?", "", value).replace("```", "")
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", re.sub(r"[*_`#>|]", " ", value))


def token_normalise(value: str) -> str:
    return " ".join(token.casefold().replace("’", "'") for token in words(value))


def option_ngrams(value: str, size: int) -> set[str]:
    tokens = re.findall(r"[a-z]+(?:'[a-z]+)?", value.casefold().replace("’", "'"))
    return {" ".join(tokens[index:index + size]) for index in range(len(tokens) - size + 1)}


def exclusive_fisher_probability(class_count: int, class_size: int, other_size: int) -> float:
    total = class_size + other_size
    return math.comb(class_size, class_count) / math.comb(total, class_count)


def fisher_exact_two_sided(a: int, b: int, c: int, d: int) -> float:
    row_one = a + b
    row_two = c + d
    column_one = a + c
    total = row_one + row_two

    def probability(value: int) -> float:
        return (
            math.comb(row_one, value)
            * math.comb(row_two, column_one - value)
            / math.comb(total, column_one)
        )

    lower = max(0, column_one - row_two)
    upper = min(row_one, column_one)
    observed = probability(a)
    return min(1.0, sum(
        probability(value)
        for value in range(lower, upper + 1)
        if probability(value) <= observed + 1e-15
    ))


def binary_feature_statistics(correct: int, distractor: int, correct_total: int, distractor_total: int) -> dict:
    correct_rate = correct / correct_total
    distractor_rate = distractor / distractor_total
    a, b = correct, correct_total - correct
    c, d = distractor, distractor_total - distractor
    odds_ratio = ((a + .5) * (d + .5)) / ((b + .5) * (c + .5))
    return {
        "correct_rate_percent": round(correct_rate * 100, 2),
        "distractor_rate_percent": round(distractor_rate * 100, 2),
        "risk_difference_percent": round((correct_rate - distractor_rate) * 100, 2),
        "odds_ratio_haldane": round(odds_ratio, 3),
        "fisher_two_sided_p": round(fisher_exact_two_sided(a, b, c, d), 8),
    }


def correlation_checks(mcqs: list[dict], key: str) -> dict:
    class_rows = {"correct": [], "distractor": []}
    for item in mcqs:
        answer = key[item["number"] - 1]
        for letter, text in item["options"].items():
            class_rows["correct" if letter == answer else "distractor"].append(text)
    thresholds = {
        1: {"automatic_exclusive_support": 8, "statistical_minimum_support": 5, "maximum_fisher_probability": 0.01},
        2: {"automatic_exclusive_support": 7, "statistical_minimum_support": 5, "maximum_fisher_probability": 0.01},
        3: {"automatic_exclusive_support": 6, "statistical_minimum_support": 4, "maximum_fisher_probability": 0.01},
    }
    flagged, inspected = [], []
    for size, threshold in thresholds.items():
        counts = {}
        for label, rows in class_rows.items():
            counter = Counter()
            for text in rows:
                counter.update(option_ngrams(text, size))
            counts[label] = counter
        for feature in sorted(set(counts["correct"]) | set(counts["distractor"])):
            parts = feature.split()
            if feature in CORRELATION_ALLOWLIST or any(
                f" {feature} " in f" {allowed} " for allowed in CORRELATION_ALLOWLIST
            ):
                continue
            if size == 1 and ((len(feature) < 3 and feature != "no") or feature in CORRELATION_STOPWORDS):
                continue
            if all(part in CORRELATION_STOPWORDS for part in parts):
                continue
            correct = counts["correct"][feature]
            distractor = counts["distractor"][feature]
            support = correct + distractor
            stats = binary_feature_statistics(
                correct, distractor, len(class_rows["correct"]), len(class_rows["distractor"])
            )
            exclusive = correct == 0 or distractor == 0
            row = {
                "ngram": size, "feature": feature, "correct_count": correct,
                "distractor_count": distractor, "support": support,
                **stats, "class_exclusive": exclusive,
            }
            if support >= threshold["statistical_minimum_support"]:
                inspected.append(row)
            exclusive_failure = exclusive and (
                support >= threshold["automatic_exclusive_support"]
                or (
                    support >= threshold["statistical_minimum_support"]
                    and stats["fisher_two_sided_p"] <= threshold["maximum_fisher_probability"]
                )
            )
            effect_failure = (
                not exclusive
                and support >= threshold["statistical_minimum_support"]
                and stats["fisher_two_sided_p"] <= threshold["maximum_fisher_probability"]
                and abs(stats["risk_difference_percent"]) >= 10
                and (stats["odds_ratio_haldane"] >= 3 or stats["odds_ratio_haldane"] <= 1 / 3)
            )
            if exclusive_failure or effect_failure:
                flagged.append(row)
    return {
        "method": "Per-option presence counts for normalized 1-, 2- and 3-grams across 61 correct and 183 distractor options.",
        "thresholds": thresholds,
        "allowlist": sorted(CORRELATION_ALLOWLIST),
        "allowlist_scope": "Only unavoidable multiword doctrine terms are exempt; generic adverbs, determiners and generated filler are not allowlisted.",
        "high_support_features_inspected": inspected,
        "statistically_material_or_exclusive_features": flagged,
        "pass": not flagged,
    }


def parse_mcqs(text: str) -> list[dict]:
    result = []
    for block in re.split(r"(?=^## MCQ \d+$)", text, flags=re.M)[1:]:
        number = int(re.search(r"^## MCQ (\d+)$", block, flags=re.M).group(1))
        stem = next(line.strip() for line in block.splitlines()[1:] if line.strip())
        options = {m.group(1): m.group(2).strip() for m in re.finditer(r"^([A-D])\. (.+)$", block, re.M)}
        answer = re.search(r"^\*\*Answer:\s*([A-D])\.\*\*$", block, re.M)
        explanations = {m.group(1): m.group(2).strip() for m in re.finditer(r"^- \*\*([A-D]):\*\* (.+)$", block, re.M)}
        result.append({
            "number": number, "stem": stem, "options": options,
            "answer": answer.group(1) if answer else None,
            "explanations": explanations, "block": block,
        })
    return result


def table_rows(text: str, heading: str) -> list[list[str]]:
    start = text.find(heading)
    if start < 0:
        return []
    tail = text[start + len(heading):]
    end = re.search(r"(?m)^## ", tail)
    section = tail[:end.start()] if end else tail
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
    following = re.search(rf"(?m)^#{{1,{level}}}\s+", text[match.end():])
    end = match.end() + following.start() if following else len(text)
    return text[match.start():end]


def parse_source_candidates(text: str) -> dict[int, str]:
    result = {}
    pattern = re.compile(r"(?m)^#### (?:Remedial )?MCQ (\d+)\s*$")
    matches = list(pattern.finditer(text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end():end]
        stem = next((line.strip() for line in block.splitlines() if line.strip() and not re.match(r"^[A-D]\. ", line)), "")
        result[int(match.group(1))] = stem
    return result


def option_quality(mcqs: list[dict], key: str) -> dict:
    longest, unique, outliers = [], [], []
    correct_lengths, distractor_lengths = [], []
    sentence_counts = {"correct": Counter(), "distractor": Counter()}
    feature_patterns = {
        "absolute_quantifier": r"\b(always|never|only|entirely|every)\b",
        "contrast_marker": r"\b(but|however|whereas|although|yet)\b",
        "semicolon": r";",
        "parentheses": r"[()]",
        "dash": r"[—–]",
        "malformed_all_singular": (
            r"\ball\s+(?:statement|logical law|noun|term|grammatical subject|"
            r"unsupported presupposition|concept|framework condition|possible world|"
            r"non-spatial world)\b"
        ),
    }
    features = {name: {"correct": 0, "distractor": 0} for name in feature_patterns}
    incomplete, filler_hits = [], []
    for item in mcqs:
        n = item["number"]
        answer = key[n - 1]
        lengths = {letter: len(text) for letter, text in item["options"].items()}
        correct_lengths.append(lengths[answer])
        distractor_lengths += [value for letter, value in lengths.items() if letter != answer]
        if lengths[answer] == max(lengths.values()):
            longest.append(n)
        if lengths[answer] > max(value for letter, value in lengths.items() if letter != answer):
            unique.append(n)
        if max(lengths.values()) / min(lengths.values()) > 2.20:
            outliers.append({"mcq": n, "lengths": lengths})
        for letter, text in item["options"].items():
            kind = "correct" if letter == answer else "distractor"
            sentence_counts[kind][len(re.findall(r"[.!?](?:\s|$)", text))] += 1
            first_alpha = next((character for character in text if character.isalpha()), "")
            if not first_alpha.isupper() or text[-1:] != "." or len(words(text)) < 6:
                incomplete.append([n, letter, text])
            for phrase in FORBIDDEN_OPTION_FILLER:
                if phrase in normalise(text):
                    filler_hits.append([n, letter, phrase])
            for name, pattern in feature_patterns.items():
                if re.search(pattern, text, re.I):
                    features[name][kind] += 1
    count = len(mcqs)
    longest_rate = round(100 * len(longest) / count, 2)
    unique_rate = round(100 * len(unique) / count, 2)
    cue_failures = []
    for name, values in features.items():
        stats = binary_feature_statistics(values["correct"], values["distractor"], count, count * 3)
        values.update(stats)
        support = values["correct"] + values["distractor"]
        exclusive = values["correct"] == 0 or values["distractor"] == 0
        values["class_exclusive"] = exclusive
        values["strict_exclusive_failure"] = exclusive and support >= 1
        values["material_nonexclusive_failure"] = (
            not exclusive
            and support >= 5
            and stats["fisher_two_sided_p"] <= .05
            and abs(stats["risk_difference_percent"]) >= 8
            and (stats["odds_ratio_haldane"] >= 2 or stats["odds_ratio_haldane"] <= .5)
        )
        if values["strict_exclusive_failure"] or values["material_nonexclusive_failure"]:
            cue_failures.append(name)
    sentence_correct_two_plus = sum(v for k, v in sentence_counts["correct"].items() if k >= 2) / count
    sentence_distractor_two_plus = sum(v for k, v in sentence_counts["distractor"].items() if k >= 2) / (count * 3)
    syntactic_gap = round(100 * abs(sentence_correct_two_plus - sentence_distractor_two_plus), 2)
    correlation = correlation_checks(mcqs, key)
    return {
        "metric": "Unicode character count of visible options",
        "correct_is_longest_count": len(longest),
        "correct_is_longest_rate_percent": longest_rate,
        "uniquely_longest_correct_count": len(unique),
        "uniquely_longest_rate_percent": unique_rate,
        "correct_mean_characters": round(sum(correct_lengths) / len(correct_lengths), 2),
        "distractor_mean_characters": round(sum(distractor_lengths) / len(distractor_lengths), 2),
        "comparability_outliers": outliers,
        "incomplete_options": incomplete,
        "forbidden_generated_filler": filler_hits,
        "lexical_and_punctuation_features": features,
        "failed_feature_correlations": cue_failures,
        "two_sentence_rate_gap_percent": syntactic_gap,
        "data_driven_token_ngram_correlation": correlation,
        "locked_bands": {"correct_longest": [15, 40], "unique_longest": [5, 30]},
        "pass": 15 <= longest_rate <= 40 and 5 <= unique_rate <= 30
        and not outliers and not incomplete and not filler_hits and not cue_failures and syntactic_gap <= 12
        and correlation["pass"],
    }


def strip_declared_propositions(value: str, false_text: str, correction: str) -> str:
    result = value
    for proposition in (false_text.rstrip("."), correction.rstrip(".")):
        patterns = (
            rf"[“\"]{re.escape(proposition)}\.?[”\"]",
            re.escape(proposition),
        )
        for pattern in patterns:
            result = re.sub(pattern, " ", result, flags=re.I)
    return re.sub(r"\s+", " ", result).strip()


def rationale_sentence_frames(value: str) -> list[str]:
    frames = []
    doctrine_words = {
        "analyticity", "commitment", "consciousness", "dogma", "duhem",
        "gavagai", "holism", "indeterminacy", "naturalism", "person",
        "presupposition", "quine", "reference", "russell", "strawson",
        "synonymy", "translation",
    }
    for sentence in re.split(r"(?<=[.!?])\s+", normalise(value)):
        tokens = sentence.split()
        if not tokens:
            continue
        frame = [
            "<concept>" if token.strip(".,;:()'\"") in doctrine_words else token
            for token in tokens[:16]
        ]
        frames.append(" ".join(frame))
    return frames


def rationale_specificity(
    value: str, false_text: str, correction: str, anchors: tuple[str, str]
) -> tuple[bool, dict]:
    residual = strip_declared_propositions(value, false_text, correction)
    normalized = token_normalise(residual)
    false_tokens = {
        token for token in token_normalise(false_text).split()
        if len(token) >= 5 and token not in CORRELATION_STOPWORDS
    }
    correction_tokens = {
        token for token in token_normalise(correction).split()
        if len(token) >= 5 and token not in CORRELATION_STOPWORDS
    }
    false_signature = false_tokens - correction_tokens
    anchor_tokens = {
        token for anchor in anchors for token in token_normalise(anchor).split()
        if len(token) >= 5 and token not in CORRELATION_STOPWORDS
    }
    false_signature -= anchor_tokens
    false_relations = (
        option_ngrams(false_text, 2) | option_ngrams(false_text, 3)
    ) - (
        option_ngrams(correction, 2) | option_ngrams(correction, 3)
    )
    residual_relations = option_ngrams(residual, 2) | option_ngrams(residual, 3)
    residual_tokens = {
        token for token in normalized.split()
        if len(token) >= 5 and token not in CORRELATION_STOPWORDS
    }
    correction_relations = option_ngrams(correction, 2) | option_ngrams(correction, 3)
    correction_reference = bool(
        len((correction_tokens | anchor_tokens) & residual_tokens) >= 2
        or correction_relations & residual_relations
    )
    diagnostic_language = bool(re.search(
        r"\b(?:assigns|attribution|attributes|cannot|collapses|conflated|conflates|"
        r"confuses|contradicts|defeated|denies|eliminates|erases|evades|excludes|"
        r"fails|false|grossly|ignores|imports|invents|invokes|irrelevant|"
        r"misattributes|miscasts|misidentifies|mislocates|misstates|mistakes|no|"
        r"not|opposite|overgeneralizes|overstates|projects|reclassifies|reduces|"
        r"reintroduces|rejects|reversed|reverses|states|substitutes|transfers|"
        r"treats|understates|wrong|wrongly)\b",
        normalized,
    ))
    explicit_false_reference = len(false_tokens & residual_tokens) >= 2
    specific_false_reference = bool(
        explicit_false_reference or false_relations & residual_relations
    )
    exact_anchor_count = sum(
        token_normalise(anchor) in normalized for anchor in anchors
    )
    anchor_only = (
        exact_anchor_count == len(anchors)
        and not specific_false_reference
    )
    generic_phrases = (
        "revise the topic carefully",
        "accurate philosophical statement",
        "qualification required by this item",
        "preserves the exact ownership",
        "the sourced correction",
        "for the demand",
        "does not diagnose the option-specific error",
        "relevant terminology",
        "complete-looking explanation",
        "technical expressions",
        "apparently relevant",
        "central vocabulary",
        "sufficiently long discussion",
    )
    checks = {
        "minimum_residual_words": len(words(residual)) >= 10,
        "diagnostic_language": diagnostic_language,
        "false_option_reference": specific_false_reference,
        "false_claim_specificity": diagnostic_language and specific_false_reference,
        "doctrinal_correction_reference": correction_reference,
        "anchor_stuffing_absent": not anchor_only,
        "lexical_specificity": len(residual_tokens) >= 6,
        "generic_stock_absent": not any(phrase in normalized for phrase in generic_phrases),
    }
    return all(checks.values()), {
        "residual_words": len(words(residual)),
        "matched_false_signature": sorted(false_signature & residual_tokens),
        "matched_false_relations": sorted(false_relations & residual_relations),
        "independent_anchors": list(anchors),
        "checks": checks,
        "residual": residual,
    }


def repeated_residual_ngrams(residuals: list[str], size: int = 8, maximum: int = 3) -> dict[str, int]:
    counts = Counter()
    for residual in residuals:
        tokens = token_normalise(residual).split()
        counts.update(set(
            " ".join(tokens[index:index + size])
            for index in range(len(tokens) - size + 1)
        ))
    return {
        phrase: count for phrase, count in counts.items()
        if count > maximum
        and not any(token_normalise(anchor) in phrase for anchors in DOCTRINAL_ANCHORS.values() for anchor in anchors)
    }


def audit_checks(questions: list[dict], solutions: list[dict], key: str) -> dict:
    payload = json.loads((TOPIC / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    rows = {int(row["number"]): row for row in payload.get("questions", [])}
    failures = []
    rationale_bodies = []
    rationale_frames = []
    rationale_residuals = []
    specificity_results = {}
    within_item_similarity = []
    all_options = []
    for question, solution in zip(questions, solutions):
        n = question["number"]
        row = rows.get(n)
        reasons = []
        if not row:
            failures.append({"mcq": n, "reasons": ["missing audit row"]})
            continue
        if normalise(row.get("stem", "")) != normalise(question["stem"]):
            reasons.append("stem mismatch")
        if row.get("answer") != EXPECTED_KEYS[n - 1] or key[n - 1] != EXPECTED_KEYS[n - 1]:
            reasons.append("key mismatch")
        normalized_options = [normalise(question["options"][letter]) for letter in "ABCD"]
        if len(set(normalized_options)) != 4:
            reasons.append("duplicate option within item")
        for first in range(4):
            for second in range(first + 1, 4):
                ratio = SequenceMatcher(None, normalized_options[first], normalized_options[second]).ratio()
                if ratio >= .90:
                    within_item_similarity.append([n, "ABCD"[first], "ABCD"[second], round(ratio, 3)])
        all_options.extend((n, letter, text) for letter, text in question["options"].items())
        refs = row.get("named_referents", [])
        if not refs or any(normalise(ref) not in normalise(question["stem"]) for ref in refs):
            reasons.append("named referent missing from stem")
        audited_options = row.get("options", {})
        true_letters = [
            letter for letter in "ABCD"
            if audited_options.get(letter, {}).get("truth_value") is True
        ]
        if true_letters != [EXPECTED_KEYS[n - 1]]:
            reasons.append("manifest does not identify exactly one true option")
        for letter in "ABCD":
            visible = question["options"].get(letter)
            option = audited_options.get(letter, {})
            if option.get("text") != visible:
                reasons.append(f"{letter} visible option mismatch")
                continue
            rationale = option.get("rationale", "")
            rationale_bodies.append(normalise(rationale))
            if f"Rationale: {rationale}" not in solution["explanations"].get(letter, ""):
                reasons.append(f"{letter} rationale mismatch")
            anchors = DOCTRINAL_ANCHORS[n]
            if letter != EXPECTED_KEYS[n - 1]:
                if option.get("false_proposition") != visible:
                    reasons.append(f"{letter} false proposition mismatch")
                if option.get("specific_correction") != question["options"][EXPECTED_KEYS[n - 1]]:
                    reasons.append(f"{letter} correction mismatch")
                wrong = visible.rstrip(".")
                correct = question["options"][EXPECTED_KEYS[n - 1]].rstrip(".")
                body = solution["explanations"].get(letter, "")
                if f"False proposition: “{wrong}.”" not in body or f"Correct replacement: “{correct}.”" not in body:
                    reasons.append(f"{letter} exact false/correction text missing")
                if not option.get("error_type"):
                    reasons.append(f"{letter} missing error type")
                specific, details = rationale_specificity(
                    rationale, visible, question["options"][EXPECTED_KEYS[n - 1]], anchors
                )
                specificity_results[f"{n}{letter}"] = details
                if not specific:
                    reasons.append(f"{letter} residual rationale lacks option-specific diagnosis or correction")
                residual = strip_declared_propositions(
                    rationale, visible, question["options"][EXPECTED_KEYS[n - 1]]
                )
                rationale_residuals.append(residual)
                rationale_frames.extend(rationale_sentence_frames(residual))
                if len(words(option.get("error_type", ""))) < 6:
                    reasons.append(f"{letter} error type is not predicate-specific")
        if reasons:
            failures.append({"mcq": n, "reasons": reasons})
    duplicates = [text for text, count in Counter(rationale_bodies).items() if text and count > 1]
    repeated_frames = {
        frame: count for frame, count in Counter(rationale_frames).items()
        if frame and count > payload.get("rationale_validation", {}).get("maximum_repeated_frame_count", 4)
    }
    repeated_ngrams = repeated_residual_ngrams(
        rationale_residuals,
        size=5,
        maximum=payload.get("rationale_validation", {}).get("maximum_repeated_frame_count", 3),
    )
    near_duplicates = []
    for index, first in enumerate(rationale_bodies):
        for second_index in range(index + 1, len(rationale_bodies)):
            ratio = SequenceMatcher(None, first, rationale_bodies[second_index]).ratio()
            if ratio >= payload.get("rationale_validation", {}).get("near_duplicate_similarity_threshold", .92):
                near_duplicates.append([index + 1, second_index + 1, round(ratio, 3)])
    option_duplicates = []
    grouped_options = defaultdict(list)
    for n, letter, text in all_options:
        grouped_options[normalise(text)].append([n, letter])
    option_duplicates = [locations for locations in grouped_options.values() if len(locations) > 1]
    controls = payload.get("rationale_validation", {}).get("generic_negative_controls", [])
    negative_controls = {}
    for index, control in enumerate(controls, 1):
        number = control["number"]
        letter = control["letter"]
        false_text = questions[number - 1]["options"][letter]
        correct_text = questions[number - 1]["options"][EXPECTED_KEYS[number - 1]]
        accepted, details = rationale_specificity(
            control["rationale"], false_text, correct_text, DOCTRINAL_ANCHORS[number],
        )
        negative_controls[f"control_{index}"] = {"rejected": not accepted, "details": details}
    return {
        "schema_version": payload.get("schema_version"),
        "manifest_question_count": len(rows),
        "visible_question_count": len(questions),
        "repeated_normalized_rationales": duplicates,
        "repeated_normalized_sentence_frames": repeated_frames,
        "repeated_residual_five_grams": repeated_ngrams,
        "near_duplicate_rationale_pairs": near_duplicates,
        "within_item_option_similarity_flags": within_item_similarity,
        "exact_duplicate_options_across_items": option_duplicates,
        "generic_negative_controls_rejected": negative_controls,
        "distractor_specificity": specificity_results,
        "failures": failures,
        "mechanical_limitations": "Exact false claims, explicit diagnostic language, false-option reference, doctrinal correction reference, repeated five-word phrases and adversarial controls reject generic or anchor-stuffed explanations; they do not prove philosophical truth.",
        "pass": payload.get("schema_version") == 5 and len(rows) == MCQ_COUNT
        and not failures and not duplicates and not repeated_frames
        and not repeated_ngrams and not near_duplicates
        and not within_item_similarity and not option_duplicates
        and controls and all(row["rejected"] for row in negative_controls.values()),
    }


def deduplication_checks(mcqs: list[dict], key: str) -> dict:
    stems = []
    inferences = []
    stem_flags, inference_flags = [], []
    for item in mcqs:
        stems.append((item["number"], normalise(item["stem"])))
        inferences.append((item["number"], normalise(item["stem"] + " " + item["options"][key[item["number"] - 1]])))
    highest_stem = (0.0, None)
    highest_inference = (0.0, None)
    for records, threshold, flags, label in ((stems, .88, stem_flags, "stem"), (inferences, .82, inference_flags, "inference")):
        for i, first in enumerate(records):
            for second in records[i + 1:]:
                ratio = SequenceMatcher(None, first[1], second[1]).ratio()
                if label == "stem" and ratio > highest_stem[0]:
                    highest_stem = (ratio, [first[0], second[0]])
                if label == "inference" and ratio > highest_inference[0]:
                    highest_inference = (ratio, [first[0], second[0]])
                if ratio >= threshold:
                    flags.append([first[0], second[0], round(ratio, 3)])
    return {
        "exact_duplicate_stems": len({text for _, text in stems}) != len(stems),
        "highest_stem_similarity": round(highest_stem[0], 3),
        "highest_stem_pair": highest_stem[1],
        "stem_similarity_flags": stem_flags,
        "highest_tested_inference_similarity": round(highest_inference[0], 3),
        "highest_inference_pair": highest_inference[1],
        "tested_inference_similarity_flags": inference_flags,
        "pass": len({text for _, text in stems}) == len(stems) and not stem_flags and not inference_flags,
    }


def mcq13_logic_check(questions: list[dict], solutions: list[dict]) -> dict:
    question = questions[12]
    solution = solutions[12]
    conjunction_options = [
        letter for letter, text in question["options"].items()
        if re.search(r"\b(?:cannot both|cannot jointly)\b", normalise(text))
    ]
    correct_text = normalise(question["options"][EXPECTED_KEYS[12]])
    rationale = normalise(solution["explanations"][EXPECTED_KEYS[12]])
    checks = {
        "expected_key_is_c": EXPECTED_KEYS[12] == "C" and solution["answer"] == "C",
        "exactly_one_conjunction_answer": conjunction_options == ["C"],
        "conjunction_not_jointly_retained": "cannot both be retained" in correct_text,
        "no_single_conjunct_inference": "does not show which conjunct" in correct_text,
        "solution_states_conjunction_false": "conjunction of hypothesis and auxiliaries is false" in rationale,
        "solution_states_underdetermination": "leaves underdetermined" in rationale,
    }
    return {
        "formal_pattern": "(H & A) -> O; not-O; therefore not-(H & A)",
        "offered_conjunction_options": conjunction_options,
        "checks": checks,
        "pass": all(checks.values()),
    }


def source_lineage_checks(revision: str, ledger: str, questions: list[dict]) -> dict:
    session = sorted(G5_DIR.glob("*Complete-Learning-Session*.md"))[-1]
    workbook = sorted(G5_DIR.glob("*Solved-Practice-Workbook*.md"))[-1]
    sources = {
        "g5_session": session,
        "g5_workbook": workbook,
        "canonical": CANONICAL,
        "earlier_session": EARLIER_SESSION,
        "earlier_workbook": EARLIER_WORKBOOK,
    }
    texts = {name: path.read_text(encoding="utf-8") for name, path in sources.items()}
    inventory_rows = table_rows(ledger, "## Mechanical source-cell inventory")
    inventory, failures = {}, []
    for row in inventory_rows:
        if len(row) != 6:
            failures.append({"row": row, "reason": "malformed source cell"})
            continue
        cell, coverage, session_anchor, workbook_anchor, canonical_anchor, witness_text = row
        sections = {
            "g5_session": anchored_section(texts["g5_session"], session_anchor),
            "g5_workbook": anchored_section(texts["g5_workbook"], workbook_anchor),
            "canonical": anchored_section(texts["canonical"], canonical_anchor),
        }
        witnesses = [term.strip() for term in witness_text.split(";")]
        combined = "\n".join(sections.values())
        checks = {term: normalise(term) in normalise(combined) and normalise(term) in normalise(revision) for term in witnesses}
        passed = all(sections.values()) and all(checks.values())
        inventory[cell] = {"coverage": coverage, "witnesses": checks, "pass": passed}
        if not passed:
            failures.append({"source_cell": cell, "reason": "anchor or witness missing"})
    candidates = parse_source_candidates(texts["g5_workbook"])
    mapping_rows = table_rows(ledger, "## Per-question lineage mapping")
    mapped, used_candidates = {}, []
    for row in mapping_rows:
        if len(row) != 6 or not row[0].isdigit():
            failures.append({"row": row, "reason": "malformed lineage row"})
            continue
        number = int(row[0])
        candidate = None if row[4] in {"—", "-", ""} else int(row[4])
        mapped[number] = {"cell": row[1], "lineage": row[2], "source": row[3], "candidate": candidate}
        if number > len(questions) or token_normalise(row[5]) != token_normalise(questions[number - 1]["stem"]):
            failures.append({"mcq": number, "reason": "lineage operation does not match visible stem"})
        if row[2] == "Adapted":
            if candidate not in candidates:
                failures.append({"mcq": number, "reason": "invalid adapted candidate"})
            else:
                source_terms = {
                    token for token in token_normalise(candidates[candidate]).split()
                    if len(token) >= 5 and token not in LINEAGE_STOPWORDS
                }
                final_terms = {
                    token for token in token_normalise(questions[number - 1]["stem"]).split()
                    if len(token) >= 5 and token not in LINEAGE_STOPWORDS
                }
                mapped[number]["shared_candidate_terms"] = sorted(source_terms & final_terms)
                if len(mapped[number]["shared_candidate_terms"]) < 2:
                    failures.append({
                        "mcq": number,
                        "reason": "adapted lineage lacks two substantive normalized source terms",
                        "shared_candidate_terms": mapped[number]["shared_candidate_terms"],
                    })
            used_candidates.append(candidate)
        elif row[2] != "New" or candidate is not None:
            failures.append({"mcq": number, "reason": "invalid lineage class"})
        if row[3] not in inventory:
            failures.append({"mcq": number, "reason": "unknown source cell"})
    source_files = {
        name: {
            "path": str(path.relative_to(REPO)),
            "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
        for name, path in sources.items()
    }
    revision_terms = {
        token for token in token_normalise(revision).split()
        if len(token) >= 5 and token not in LINEAGE_STOPWORDS
    }
    revision_bigrams = option_ngrams(revision, 2)
    overlap = {}
    for name, text in texts.items():
        source_terms = {
            token for token in token_normalise(text).split()
            if len(token) >= 5 and token not in LINEAGE_STOPWORDS
        }
        source_bigrams = option_ngrams(text, 2)
        shared_terms = revision_terms & source_terms
        shared_bigrams = revision_bigrams & source_bigrams
        overlap[name] = {
            "shared_substantive_terms": len(shared_terms),
            "shared_bigrams": len(shared_bigrams),
            "sample_terms": sorted(shared_terms)[:25],
            "pass": len(shared_terms) >= 25 and len(shared_bigrams) >= 20,
        }
    return {
        "source_files_read": source_files,
        "source_cell_count": len(inventory),
        "source_cells": inventory,
        "lineage_mapping_count": len(mapped),
        "lineage_counts": dict(Counter(value["lineage"] for value in mapped.values())),
        "mapped_unique_source_candidates": len(set(used_candidates)),
        "unmapped_source_candidates": sorted(set(candidates) - set(used_candidates)),
        "real_source_overlap_checks": overlap,
        "failures": failures,
        "mechanical_limitations": "This checks file identity, anchors, witnesses, token/bigram overlap and declared candidate links; it does not prove semantic completeness.",
        "pass": len(inventory) == 11 and len(mapped) == MCQ_COUNT
        and set(mapped) == set(range(1, MCQ_COUNT + 1))
        and len(used_candidates) == len(set(used_candidates))
        and all(row["pass"] for row in overlap.values()) and not failures,
    }


def answer_integrity(answer: str) -> dict:
    straight_balanced = answer.count('"') % 2 == 0
    curly_balanced = answer.count("“") == answer.count("”")
    sentences = [
        sentence.strip(" \n\t-")
        for sentence in re.split(r"(?<=[.!?])(?:\s+|\n+)", answer)
        if sentence.strip()
    ]
    leaked = [
        sentence for sentence in sentences
        if normalise(sentence).rstrip(".") in LEAKED_ANSWER_LABELS
    ]
    finite_verb = re.compile(
        r"\b(am|are|is|was|were|be|been|being|can|could|does|do|did|has|have|had|"
        r"may|might|must|shall|should|will|would|follows?|grounds?|names?|"
        r"means?|states?|shows?|defines?|explains?|remains?|becomes?)\b",
        re.I,
    )
    fragments = [
        sentence for sentence in sentences
        if len(words(sentence)) < 1 and not finite_verb.search(sentence)
        and not re.fullmatch(r"(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*\(\d{4}\)\.?", sentence)
    ]
    paragraph_count = len([paragraph for paragraph in answer.split("\n\n") if paragraph.strip()])
    return {
        "straight_quotes_balanced": straight_balanced,
        "curly_quotes_balanced": curly_balanced,
        "leaked_outline_labels": leaked,
        "fragmentary_sentences": fragments,
        "paragraph_count": paragraph_count,
        "pass": straight_balanced and curly_balanced and not leaked and not fragments and paragraph_count >= 2,
    }


def toolkit_checks(toolkit: str) -> dict:
    ledger_text = (REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2018-2025.md").read_text(encoding="utf-8")
    ledger_text += "\n" + (REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2026.md").read_text(encoding="utf-8")
    sections = re.split(r"(?=^## (?:\d+\.|Original \d+))", toolkit, flags=re.M)[1:]
    pyqs, originals, failures = {}, {}, []
    for section in sections:
        heading = section.splitlines()[0]
        question = re.search(r"^\*\*Question:\*\* (.+)$", section, re.M)
        answer = re.search(r"### Timed independent model answer\n\n(.*?)\n\n\*\*Measured model-answer words:\*\* (\d+)", section, re.S)
        marks_match = re.search(r"· (\d+) marks", heading)
        if not question or not answer or not marks_match:
            failures.append({"section": heading, "reason": "missing question, marks or timed answer"})
            continue
        marks = int(marks_match.group(1))
        measured = len(words(answer.group(1)))
        stated = int(answer.group(2))
        result = {
            "marks": marks, "band": WORD_BANDS[marks], "measured": measured,
            "stated": stated, "in_band": WORD_BANDS[marks][0] <= measured <= WORD_BANDS[marks][1],
            "matches_stated": abs(measured - stated) <= 1,
            "demand_decoding": "**Demand decoding:**" in section,
            "qualification": "**Qualification / criticism:**" in section,
            "coverage_check": "**Coverage check:**" in section,
            "unsupported_marks_claim_absent": "**Why this earns marks:**" not in section,
            "answer_integrity": answer_integrity(answer.group(1)),
        }
        if heading.startswith("## Original"):
            originals[heading] = result
        else:
            identity = re.search(r"(\d{4}) (Q\d+\([a-z]\))", heading)
            label = f"{identity.group(1)} {identity.group(2)}"
            result["exact_prompt"] = normalise(question.group(1)) in normalise(ledger_text)
            pyqs[label] = result
    expected = {f"{year} {part}" for year, part, _ in DIRECT_PYQS}
    all_rows = list(pyqs.values()) + list(originals.values())
    return {
        "verified_pyqs": pyqs,
        "original_solved_practice": originals,
        "expected_pyqs": sorted(expected),
        "learner_answers_not_official_keys": "never official UPSC answer keys" in toolkit,
        "failures": failures,
        "pass": set(pyqs) == expected and len(originals) == 3 and not failures
        and all(all(v for k, v in row.items() if k in {
            "in_band", "matches_stated", "demand_decoding", "qualification",
            "coverage_check", "unsupported_marks_claim_absent", "exact_prompt",
        }) for row in all_rows)
        and all(row["answer_integrity"]["pass"] for row in all_rows)
        and "never official UPSC answer keys" in toolkit,
    }


def demand_audit_checks(toolkit: str) -> dict:
    payload = json.loads((TOPIC / "PYQ-DEMAND-AUDIT.json").read_text(encoding="utf-8"))
    expected = {f"{year} {part}": marks for year, part, marks in DIRECT_PYQS}
    failures, results = [], {}

    def paragraph_index(answer_text: str, anchor: str) -> int:
        target = token_normalise(anchor)
        for index, paragraph in enumerate(answer_text.split("\n\n")):
            if target in token_normalise(paragraph):
                return index
        return -1

    def anchor_is_contradicted(answer_text: str, anchor: str) -> bool:
        tokens = token_normalise(answer_text).split()
        needle = token_normalise(anchor).split()
        for index in range(len(tokens) - len(needle) + 1):
            if tokens[index:index + len(needle)] != needle:
                continue
            prefix = tokens[max(0, index - 5):index]
            prefix_text = " ".join(prefix)
            if (
                "opposite of" in prefix_text
                or "false that" in prefix_text
                or "rejects that" in prefix_text
                or "denies that" in prefix_text
            ):
                return True
        return False

    def structural_result(answer_text: str, row: dict) -> dict:
        order_anchors = row.get("ordered_anchors", [])
        order_positions = [paragraph_index(answer_text, anchor) for anchor in order_anchors]
        ordered = (
            len(order_anchors) >= 2
            and all(position >= 0 for position in order_positions)
            and order_positions == sorted(order_positions)
            and len(set(order_positions)) >= 2
        )
        connected_results = []
        for pair in row.get("connected_pairs", []):
            left = paragraph_index(answer_text, pair["left"])
            right = paragraph_index(answer_text, pair["right"])
            passed = left >= 0 and right >= 0 and abs(left - right) <= pair.get("maximum_paragraph_gap", 1)
            connected_results.append({**pair, "left_paragraph": left, "right_paragraph": right, "pass": passed})
        relation_results = []
        for relation in row.get("affirmed_relations", []):
            anchors = [relation["left"], relation["right"], relation["relation_anchor"]]
            positions = [paragraph_index(answer_text, anchor) for anchor in anchors]
            passed = (
                all(position >= 0 for position in positions)
                and max(positions) - min(positions) <= relation.get("maximum_paragraph_gap", 1)
                and not anchor_is_contradicted(answer_text, relation["relation_anchor"])
            )
            relation_results.append({**relation, "paragraphs": positions, "pass": passed})
        return {
            "ordered_anchors": order_anchors,
            "order_positions": order_positions,
            "ordered": ordered,
            "connected_pairs": connected_results,
            "affirmed_relations": relation_results,
            "pass": ordered and bool(connected_results) and all(x["pass"] for x in connected_results)
            and bool(relation_results) and all(x["pass"] for x in relation_results),
        }

    rows_to_check = payload.get("pyqs", []) + payload.get("originals", [])
    for row in rows_to_check:
        identity = row.get("id")
        if identity.startswith("Original "):
            section_pattern = rf"(?ms)^## {re.escape(identity)} · \d+ marks\s+(.*?)(?=^## )"
        else:
            section_pattern = rf"(?ms)^## \d+\. {re.escape(identity)} · \d+ marks\s+(.*?)(?=^## )"
        section_match = re.search(section_pattern, toolkit)
        section = section_match.group(1) if section_match else ""
        answer_match = re.search(r"### Timed independent model answer\n\n(.*?)\n\n\*\*Measured", section, re.S)
        answer = answer_match.group(1) if answer_match else ""
        reasons = []
        if identity.startswith("Original "):
            if row.get("marks") not in WORD_BANDS:
                reasons.append("original marks mismatch")
        elif identity not in expected or row.get("marks") != expected.get(identity):
            reasons.append("identity or marks mismatch")
        question_match = re.search(r"^\*\*Question:\*\* (.+)$", section, re.M)
        if not question_match or normalise(question_match.group(1)) != normalise(row.get("question", "")):
            reasons.append("question mismatch")
        limb_results = []
        for limb in row.get("demand_limbs", []):
            anchors = limb.get("anchors", [])
            passed = bool(anchors) and all(token_normalise(anchor) in token_normalise(answer) for anchor in anchors)
            limb_results.append({"limb": limb.get("limb"), "anchors": anchors, "pass": passed})
            if not passed:
                reasons.append(f"missing demand limb: {limb.get('limb')}")
        if not row.get("demand_limbs"):
            reasons.append("empty demand limbs")
        structure = structural_result(answer, row)
        if not structure["pass"]:
            reasons.append("relation, connection or order check failed")
        paragraphs = [paragraph for paragraph in answer.split("\n\n") if paragraph.strip()]
        shuffled = "\n\n".join(reversed(paragraphs))
        shuffled_rejected = not structural_result(shuffled, row)["pass"]
        relation_anchor = row.get("affirmed_relations", [{}])[0].get("relation_anchor", "")
        contradictory = (
            f"The opposite of {relation_anchor} is true. {answer}"
            if relation_anchor else answer
        )
        contradictory_rejected = not structural_result(contradictory, row)["pass"]
        if not shuffled_rejected:
            reasons.append("shuffled-answer adversarial control was accepted")
        if not contradictory_rejected:
            reasons.append("contradictory-answer adversarial control was accepted")
        results[identity] = {
            "limbs": limb_results,
            "structural_relation_order_checks": structure,
            "adversarial_controls": {
                "reversed_paragraph_order_rejected": shuffled_rejected,
                "contradicted_relation_rejected": contradictory_rejected,
            },
            "pass": not reasons,
        }
        if reasons:
            failures.append({"pyq": identity, "reasons": reasons})
    return {
        "owned_pyq_count": len(payload.get("pyqs", [])),
        "original_answer_count": len(payload.get("originals", [])),
        "expected_owned_pyqs": sorted(expected),
        "component_checks": results,
        "failures": failures,
        "gate_name": "structural and demand-anchor integrity",
        "semantic_claim": "No claim of proved semantic coherence or philosophical truth is made.",
        "mechanical_limitations": "Parsed sections, literal demand anchors, connected-pair checks and declared paragraph order reject missing or scrambled structure. They do not prove semantic coherence, argumentative sufficiency, truth or examiner marks.",
        "pass": payload.get("schema_version") == 3
        and len(payload.get("pyqs", [])) == 10 and len(payload.get("originals", [])) == 3
        and set(results) == set(expected) | {"Original 1", "Original 2", "Original 3"} and not failures,
    }


def doctrinal_checks(revision: str, toolkit: str) -> dict:
    combined = normalise(revision + "\n" + toolkit)
    required = {
        "two_projects_not_flattened": all(term in combined for term in (
            "two-project firewall", "naturalized holism", "descriptive metaphysics",
        )),
        "two_dogmas_complete": all(term in combined for term in (
            "analytic/synthetic", "synonymy", "interchangeability", "semantical rules",
            "reductionism", "corporate body", "web of belief",
        )),
        "revisability_qualified": all(term in combined for term in (
            "no statement is immune", "minimum mutilation", "change of logic",
        )),
        "quine_positive_system": all(term in combined for term in (
            "naturalized epistemology", "normative objection", "bound variable",
            "canonical notation", "indispensability",
        )),
        "translation_taxonomy": all(term in combined for term in (
            "radical translation", "stimulus meaning", "gavagai",
            "inscrutability of reference", "indeterminacy of translation",
            "proxy functions", "ontological relativity",
        )),
        "basic_particulars": all(term in combined for term in (
            "basic particulars", "identification", "re-identification",
            "spatio-temporal framework", "material bodies",
        )),
        "persons": all(term in combined for term in (
            "person as primitive", "m-predicates", "p-predicates",
            "self-ascription", "other-ascription", "other minds",
        )),
        "referring": all(term in combined for term in (
            "on referring", "presupposition", "assertion", "uniqueness", "context",
        )),
        "criticisms": all(term in combined for term in (
            "grice", "normativity", "anthropocentric", "conservative",
        )),
        "reactive_boundary": "reactive attitudes" in combined and "bounded enrichment" in combined,
        "pyq_2026": "why are states of consciousness ascribed" in combined,
    }
    forbidden = {
        "naturalism_equals_descriptive": r"quine.{0,80}naturalism (?:is|means).{0,40}descriptive metaphysics",
        "primitive_third_substance": r"person (?:is|becomes) a third substance",
        "strawson_sentence_meaningless": r"strawson.{0,100}present king.{0,100}meaningless",
        "unqualified_logic_revision": r"quine.{0,100}logic.{0,50}(?:casually|always|immediately) revised",
    }
    hits = {name: re.findall(pattern, combined, re.I | re.S) for name, pattern in forbidden.items()}
    return {"required_claims": required, "forbidden_claim_hits": hits, "pass": all(required.values()) and not any(hits.values())}


def pdf_checks(path: Path, source_path: Path, regeneration_file: dict | None) -> dict:
    blank, replacements, bounds, overlaps, markdown = [], 0, [], [], []
    with fitz.open(path) as document:
        for page_number, page in enumerate(document, 1):
            text = page.get_text("text")
            if len(text.strip()) < 20 and not page.get_images(full=True):
                blank.append(page_number)
            replacements += text.count("�")
            for line in text.splitlines():
                if "**" in line or "`" in line or re.match(r"^\s*#{1,6}\s+", line):
                    markdown.append({"page": page_number, "text": line[:120]})
            blocks = [block for block in page.get_text("blocks") if str(block[4]).strip() and not str(block[4]).startswith("HIDX")]
            for block in blocks:
                x0, y0, x1, y1 = block[:4]
                if x0 < -1 or y0 < -1 or x1 > page.rect.width + 1 or y1 > page.rect.height + 1:
                    bounds.append(page_number)
                    break
            if page_number != 2:
                for i, first in enumerate(blocks):
                    r1 = fitz.Rect(first[:4])
                    for second in blocks[i + 1:]:
                        r2 = fitz.Rect(second[:4])
                        intersection = r1 & r2
                        smaller = min(r1.get_area(), r2.get_area())
                        if smaller and not intersection.is_empty and intersection.get_area() / smaller > .35:
                            overlaps.append(page_number)
                            break
                    if overlaps and overlaps[-1] == page_number:
                        break
        extracted = "\n".join(page.get_text("text") for page in document)
        pages = document.page_count
    source = source_path.read_text(encoding="utf-8")
    def parity_normalise(value: str) -> str:
        folded = unicodedata.normalize("NFKD", value)
        plain = "".join(character for character in folded if not unicodedata.combining(character))
        return token_normalise(plain.replace("-", " "))

    headings = [
        parity_normalise(match.group(1))
        for match in re.finditer(r"(?m)^#{1,3}\s+(.+?)\s*$", source)
        if token_normalise(match.group(1))
    ]
    extracted_tokens = parity_normalise(extracted)
    expected_descriptor = PDF_DESCRIPTORS[path.name]
    descriptor_present = parity_normalise(expected_descriptor) in parity_normalise(
        extracted
    )
    missing_headings = [heading for heading in headings if heading not in extracted_tokens]
    source_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    pdf_sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
    regeneration_matches = bool(
        regeneration_file
        and regeneration_file.get("source_sha256") == source_sha256
        and regeneration_file.get("sha256") == pdf_sha256
        and regeneration_file.get("source_mtime_ns") == source_path.stat().st_mtime_ns
    )
    return {
        "bytes": path.stat().st_size, "pages": pages,
        "source": source_path.name,
        "source_sha256": source_sha256,
        "pdf_sha256": pdf_sha256,
        "source_mtime_ns": source_path.stat().st_mtime_ns,
        "pdf_mtime_ns": path.stat().st_mtime_ns,
        "pdf_not_older_than_source": path.stat().st_mtime_ns >= source_path.stat().st_mtime_ns,
        "heading_count": len(headings),
        "missing_source_headings": missing_headings,
        "expected_cover_descriptor": expected_descriptor,
        "cover_descriptor_present": descriptor_present,
        "matches_current_regeneration_record": regeneration_matches,
        "blank_pages": sorted(set(blank)), "replacement_glyphs": replacements,
        "out_of_bounds_text_pages": sorted(set(bounds)),
        "content_overlap_pages": sorted(set(overlaps)),
        "raw_markdown_artifacts": markdown,
        "pass": pages > 0 and not blank and not replacements and not bounds and not overlaps
        and not markdown and not missing_headings and descriptor_present
        and path.stat().st_mtime_ns >= source_path.stat().st_mtime_ns
        and regeneration_matches,
    }


def regenerate_pdfs(selected: set[str] | None = None) -> dict:
    sys.path.insert(0, str(TOOLS))
    import unicode_markdown_pdf
    files = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        if selected is not None and pdf_name not in selected:
            continue
        output = PDF_DIR / pdf_name
        output.unlink(missing_ok=True)
        unicode_markdown_pdf.build_pdf(
            TOPIC / source_name, output, internal_index=True, index_title="CONTENTS",
            cover_descriptor=PDF_DESCRIPTORS[pdf_name],
            footer_label=f"Quine and Strawson | {source_name.removesuffix('.md')}",
        )
        files[pdf_name] = {
            "source": source_name, "exists": output.is_file(),
            "bytes": output.stat().st_size if output.exists() else 0,
            "sha256": hashlib.sha256(output.read_bytes()).hexdigest() if output.exists() else None,
            "source_sha256": hashlib.sha256((TOPIC / source_name).read_bytes()).hexdigest(),
            "source_mtime_ns": (TOPIC / source_name).stat().st_mtime_ns,
            "pdf_mtime_ns": output.stat().st_mtime_ns if output.exists() else None,
        }
    return {
        "requested": True,
        "selected": sorted(selected) if selected is not None else sorted(PDF_SOURCES),
        "files": files,
        "all_selected_regenerated": all(x["exists"] for x in files.values()),
    }


def text_integrity() -> dict:
    failures, inspected = [], []
    for path in sorted(TOPIC.rglob("*")):
        if not path.is_file() or path.suffix.casefold() not in {".md", ".json", ".py"}:
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            failures.append({"file": str(path), "error": str(error)})
            continue
        trailing = [i for i, line in enumerate(text.splitlines(), 1) if line.endswith((" ", "\t"))]
        if trailing:
            failures.append({"file": str(path.relative_to(REPO)), "trailing_whitespace": trailing})
        inspected.append({"file": str(path.relative_to(REPO)), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
    tracked = subprocess.run(
        ["git", "-C", str(REPO), "--no-pager", "diff", "--check", "--",
         "practice/Offline-Revision-MCQ/INDEX.md", "practice/Offline-Revision-MCQ/STATUS.json"],
        capture_output=True, text=True,
    )
    if tracked.returncode:
        failures.append({"tracked_diff_check": tracked.stdout + tracked.stderr})
    untracked = subprocess.run(
        ["git", "-C", str(REPO), "ls-files", "--others", "--exclude-standard", "--", str(TOPIC.relative_to(REPO))],
        capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    ignored_pdfs = {}
    for pdf_name in PDF_SOURCES:
        relative = str((PDF_DIR / pdf_name).relative_to(REPO))
        probe = subprocess.run(
            ["git", "-C", str(REPO), "check-ignore", "-v", "--", relative],
            capture_output=True, text=True,
        )
        ignored_pdfs[pdf_name] = {
            "ignored": probe.returncode == 0,
            "rule": (probe.stdout + probe.stderr).strip(),
        }
    probes = []
    for relative in untracked:
        if not relative.casefold().endswith((".md", ".json", ".py")):
            continue
        probe = subprocess.run(
            ["git", "-C", str(REPO), "--no-pager", "diff", "--no-index", "--check", "--", "NUL", str(REPO / relative)],
            capture_output=True, text=True,
        )
        output = (probe.stdout + probe.stderr).strip()
        probes.append({"file": relative, "diagnostics": output, "pass": not output})
        if output:
            failures.append({"file": relative, "untracked_diff_check": output})
    return {
        "inspected": inspected,
        "untracked_diff_checks": probes,
        "pdf_git_ignore_awareness": ignored_pdfs,
        "release_staging_instruction_present": all(
            phrase in normalise((TOPIC / "README.md").read_text(encoding="utf-8"))
            for phrase in ("git check-ignore", "git add -f", "pdfs are globally ignored")
        ),
        "failures": failures,
        "pass": bool(inspected) and not failures
        and all(row["ignored"] for row in ignored_pdfs.values())
        and all(
            phrase in normalise((TOPIC / "README.md").read_text(encoding="utf-8"))
            for phrase in ("git check-ignore", "git add -f", "pdfs are globally ignored")
        ),
    }


def toolkit_checks_reconciled(toolkit: str) -> dict:
    ledger = (
        (REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2018-2025.md")
        .read_text(encoding="utf-8")
        + "\n"
        + (REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2026.md")
        .read_text(encoding="utf-8")
    )
    expected = {f"{year} {part}": marks for year, part, marks in DIRECT_PYQS}
    sections = {}
    failures = []
    matches = list(
        re.finditer(
            r"^## \d+\. (20\d{2}) (Q\d+\([a-z]\)) · (\d+) marks$",
            toolkit,
            re.M,
        )
    )
    for index, match in enumerate(matches):
        end = (
            matches[index + 1].start()
            if index + 1 < len(matches)
            else toolkit.find("## Original solved practice", match.end())
        )
        section = toolkit[match.start() : end]
        identity = f"{match.group(1)} {match.group(2)}"
        question = re.search(r"^\*\*Question:\*\* (.+)$", section, re.M)
        answer = re.search(
            r"(?ms)^### Timed independent model answer\s*$\n"
            r"(.*?)(?=^\*\*Measured model-answer words:)",
            section,
        )
        declared = re.search(
            r"^\*\*Measured model-answer words:\*\* (\d+)$", section, re.M
        )
        marks = int(match.group(3))
        count = len(words(answer.group(1))) if answer else 0
        row = {
            "marks": marks,
            "words": count,
            "band": WORD_BANDS.get(marks),
            "declared": int(declared.group(1)) if declared else None,
            "exact_question_in_verified_ledger": bool(
                question and normalise(question.group(1)) in normalise(ledger)
            ),
            "demand_decoding": "### Demand decoding" in section,
            "why_this_earns_marks": "### Why this earns marks" in section,
            "paragraph_count": (
                len([part for part in answer.group(1).split("\n\n") if part.strip()])
                if answer
                else 0
            ),
        }
        row["pass"] = (
            identity in expected
            and marks == expected[identity]
            and WORD_BANDS[marks][0] <= count <= WORD_BANDS[marks][1]
            and row["declared"] == count
            and row["exact_question_in_verified_ledger"]
            and row["demand_decoding"]
            and row["why_this_earns_marks"]
            and row["paragraph_count"] >= 3
        )
        if not row["pass"]:
            failures.append({"pyq": identity, "details": row})
        sections[identity] = row

    formal_workbook = FORMAL_SOURCES["workbook"].read_text(encoding="utf-8")
    formal_questions = {
        int(number): normalise(question)
        for number, question in re.findall(
            r"(?ms)^#### Original (\d+) · \d+ marks\s+"
            r"\*\*Question:\*\* (.+?)$",
            formal_workbook,
            re.M,
        )
    }
    originals = {}
    original_matches = list(
        re.finditer(r"^## Original (\d+) · (\d+) marks$", toolkit, re.M)
    )
    for index, match in enumerate(original_matches):
        end = (
            original_matches[index + 1].start()
            if index + 1 < len(original_matches)
            else toolkit.find("## Final self-check", match.end())
        )
        section = toolkit[match.start() : end if end >= 0 else len(toolkit)]
        number = int(match.group(1))
        marks = int(match.group(2))
        question = re.search(r"^\*\*Question:\*\* (.+)$", section, re.M)
        answer = re.search(
            r"(?ms)^### Timed independent model answer\s*$\n"
            r"(.*?)(?=^\*\*Measured model-answer words:)",
            section,
        )
        declared = re.search(
            r"^\*\*Measured model-answer words:\*\* (\d+)$", section, re.M
        )
        count = len(words(answer.group(1))) if answer else 0
        row = {
            "marks": marks,
            "words": count,
            "band": WORD_BANDS.get(marks),
            "declared": int(declared.group(1)) if declared else None,
            "formal_question_match": bool(
                question and normalise(question.group(1)) == formal_questions.get(number)
            ),
            "demand_decoding": "### Demand decoding" in section,
            "why_this_earns_marks": "### Why this earns marks" in section,
            "paragraph_count": (
                len([part for part in answer.group(1).split("\n\n") if part.strip()])
                if answer
                else 0
            ),
        }
        row["pass"] = (
            marks in WORD_BANDS
            and WORD_BANDS[marks][0] <= count <= WORD_BANDS[marks][1]
            and row["declared"] == count
            and row["formal_question_match"]
            and row["demand_decoding"]
            and row["why_this_earns_marks"]
            and row["paragraph_count"] >= 3
        )
        if not row["pass"]:
            failures.append({"original": number, "details": row})
        originals[number] = row
    distribution = sorted(row["marks"] for row in originals.values())
    disclaimer = (
        "independent learner practice" in normalise(toolkit)
        and "never an official upsc key" in normalise(toolkit)
    )
    return {
        "verified_pyqs": sections,
        "original_solved_practice": originals,
        "word_bands": WORD_BANDS,
        "original_mark_distribution": distribution,
        "independent_practice_disclaimer": disclaimer,
        "failures": failures,
        "pass": set(sections) == set(expected)
        and len(originals) == 6
        and distribution == [10, 10, 15, 15, 20, 20]
        and all(row["pass"] for row in list(sections.values()) + list(originals.values()))
        and disclaimer
        and not failures,
    }


def band_instruction_checks(toolkit: str) -> dict:
    normalized = (
        toolkit.replace("–", "-")
        .replace("—", "-")
        .replace("about ", "")
    )
    forbidden_patterns = {
        "10_mark_150_220": r"10 marks[^\n]{0,80}150\s*(?:to|-)\s*220",
        "15_mark_250_330": r"15 marks[^\n]{0,80}250\s*(?:to|-)\s*330",
        "20_mark_330_400": r"20 marks[^\n]{0,80}330\s*(?:to|-)\s*400",
        "10_mark_150_300": r"10 marks[^\n]{0,80}150\s*(?:to|-)\s*300",
        "15_mark_250_400": r"15 marks[^\n]{0,80}250\s*(?:to|-)\s*400",
        "20_mark_330_550": r"20 marks[^\n]{0,80}330\s*(?:to|-)\s*550",
    }
    forbidden_hits = {
        name: re.findall(pattern, normalized, re.I)
        for name, pattern in forbidden_patterns.items()
    }
    execution_rows = [
        {
            "marks": int(marks),
            "minimum": int(minimum),
            "maximum": int(maximum),
        }
        for marks, minimum, maximum in re.findall(
            r"\*\*Exam-length execution\s*-\s*(\d+) marks,\s*"
            r"(\d+)\s*to\s*(\d+) words:",
            normalized,
            re.I,
        )
    ]
    row_results = [
        {
            **row,
            "expected": WORD_BANDS.get(row["marks"]),
            "pass": WORD_BANDS.get(row["marks"])
            == (row["minimum"], row["maximum"]),
        }
        for row in execution_rows
    ]
    header_rows = {
        marks: bool(
            re.search(
                rf"\|\s*{marks}\s*\|[^\n]*\|\s*{minimum}\s*-\s*{maximum}\s+words\s*\|",
                normalized,
            )
        )
        for marks, (minimum, maximum) in WORD_BANDS.items()
    }
    return {
        "locked_bands": WORD_BANDS,
        "forbidden_band_hits": forbidden_hits,
        "execution_instruction_count": len(execution_rows),
        "execution_instructions": row_results,
        "header_rows": header_rows,
        "pass": not any(forbidden_hits.values())
        and bool(execution_rows)
        and all(row["pass"] for row in row_results)
        and all(header_rows.values()),
    }


def package_negative_tests(toolkit: str, formal: dict) -> dict:
    tests = []

    def record(name: str, rejected: bool) -> None:
        tests.append({"name": name, "rejected": rejected, "pass": rejected})

    record(
        "forbidden 10-mark 150-220 band",
        not band_instruction_checks(
            toolkit.replace("150 to 200 words", "150 to 220 words", 1)
        )["pass"],
    )
    record(
        "forbidden 15-mark 250-330 band",
        not band_instruction_checks(
            toolkit.replace("250 to 300 words", "250 to 330 words", 1)
        )["pass"],
    )
    record(
        "forbidden 20-mark 330-400 band",
        not band_instruction_checks(
            toolkit.replace("340 to 400 words", "330 to 400 words", 1)
        )["pass"],
    )
    simulated_required = [name for name in REQUIRED if name != "VALIDATION.json"]
    record(
        "VALIDATION.json removed from required release set",
        "VALIDATION.json" not in simulated_required
        and "VALIDATION.json" in REQUIRED,
    )
    soul_mode = formal.get("external_destination_modes", {}).get(
        "T11-ROUTE-P2-SOUL", {}
    )
    record(
        "Soul destination satisfies development closure",
        soul_mode.get("development_valid") is True,
    )
    release_mutation = next(
        (
            row
            for row in formal.get("coverage_negative_tests", {}).get(
                "tests", []
            )
            if row.get("name")
            == "development-only Soul destination cannot satisfy release"
        ),
        {},
    )
    if not release_mutation:
        fresh_mutations = formal_validation.negative_tests(
            json.loads(FORMAL_REVIEW.read_text(encoding="utf-8")),
            formal_validation.extract_blocks(),
        )
        release_mutation = next(
            (
                row
                for row in fresh_mutations.get("tests", [])
                if row.get("name")
                == "development-only Soul destination cannot satisfy release"
            ),
            {},
        )
    record(
        "development-only Soul release mutation is rejected",
        release_mutation.get("pass") is True
        and release_mutation.get("expected_failure_code")
        == "closed_destination_release_not_ready"
        and "closed_destination_release_not_ready"
        in release_mutation.get("actual_failure_codes", []),
    )
    return {
        "tests": tests,
        "passed": sum(row["pass"] for row in tests),
        "failed": sum(not row["pass"] for row in tests),
        "pass": all(row["pass"] for row in tests),
    }


def isolated_text_integrity() -> dict:
    failures = []
    inspected = []
    for path in sorted(TOPIC.rglob("*")):
        if not path.is_file() or path.suffix.casefold() not in {".md", ".json", ".py"}:
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            failures.append({"file": str(path.relative_to(TOPIC)), "error": str(error)})
            continue
        trailing = [
            number
            for number, line in enumerate(text.splitlines(), 1)
            if line.endswith((" ", "\t"))
        ]
        if trailing:
            failures.append(
                {"file": str(path.relative_to(TOPIC)), "trailing_whitespace": trailing}
            )
        inspected.append(
            {
                "file": str(path.relative_to(TOPIC)),
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
    diff = subprocess.run(
        [
            "git",
            "-C",
            str(REPO),
            "--no-pager",
            "diff",
            "--check",
            "--",
            str(TOPIC.relative_to(REPO)),
        ],
        capture_output=True,
        text=True,
    )
    if diff.returncode:
        failures.append({"git_diff_check": (diff.stdout + diff.stderr).strip()})
    return {"inspected": inspected, "failures": failures, "pass": bool(inspected) and not failures}


def release_integrity(formal: dict) -> dict:
    rows = []
    for name in REQUIRED:
        path = TOPIC / name
        relative = str(path.relative_to(REPO)).replace("\\", "/")
        worktree_hash = (
            subprocess.run(
                ["git", "-C", str(REPO), "hash-object", "--", relative],
                capture_output=True,
                text=True,
            ).stdout.strip()
            if path.is_file()
            else ""
        )
        indexed = subprocess.run(
            ["git", "-C", str(REPO), "ls-files", "-s", "--", relative],
            capture_output=True,
            text=True,
        ).stdout.strip().split()
        index_hash = indexed[1] if len(indexed) >= 2 else ""
        self_recursive = name == "VALIDATION.json"
        rows.append(
            {
                "file": name,
                "worktree_hash": worktree_hash,
                "index_hash": index_hash,
                "self_recursive_validation_artifact": self_recursive,
                "current_in_index": bool(
                    index_hash
                    and (
                        self_recursive
                        or worktree_hash == index_hash
                    )
                ),
            }
        )
    obligations_closed = not formal.get(
        "release_blocked_by_external_obligations", True
    )
    return {
        "files": rows,
        "validation_self_recursion_policy": (
            "VALIDATION.json must already be tracked or staged, but its worktree hash is "
            "not compared with the index because this validation run rewrites that file."
        ),
        "validation_file_required": "VALIDATION.json" in REQUIRED,
        "all_required_current_in_index": all(
            row["current_in_index"] for row in rows
        ),
        "external_obligations_closed": obligations_closed,
        "pass": all(row["current_in_index"] for row in rows) and obligations_closed,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regenerate", action="store_true")
    parser.add_argument("--regenerate-toolkit", action="store_true")
    parser.add_argument("--refresh-formal-audit", action="store_true")
    parser.add_argument("--mode", choices=("development", "precommit"), default="development")
    args = parser.parse_args()
    review_hash_before = (
        hashlib.sha256(FORMAL_REVIEW.read_bytes()).hexdigest()
        if FORMAL_REVIEW.is_file()
        else None
    )
    if args.refresh_formal_audit or not FORMAL_AUDIT.is_file():
        formal_validation.refresh_audit(mode=args.mode)
    review_hash_after = (
        hashlib.sha256(FORMAL_REVIEW.read_bytes()).hexdigest()
        if FORMAL_REVIEW.is_file()
        else None
    )
    if review_hash_before != review_hash_after:
        raise RuntimeError("formal audit refresh mutated authored review decisions")

    prior = {}
    if VALIDATION.is_file():
        try:
            prior = json.loads(VALIDATION.read_text(encoding="utf-8")).get(
                "pdf_generation", {}
            )
        except (json.JSONDecodeError, OSError):
            prior = {}
    regeneration = {
        "requested": False,
        "mechanism": prior.get("mechanism"),
        "files": prior.get("files", {}),
        "all_four_regenerated": prior.get("all_four_regenerated", False),
        "reused_prior_record": bool(prior.get("files")),
    }
    if args.regenerate or args.regenerate_toolkit:
        selected = (
            {"Answer-Writing-Toolkit.pdf"} if args.regenerate_toolkit else None
        )
        partial = regenerate_pdfs(selected)
        files = dict(prior.get("files", {}))
        files.update(partial["files"])
        regeneration = {
            "mechanism": (
                "C:/up/tools/unicode_markdown_pdf.py via installed Chrome and PyMuPDF"
            ),
            "requested": True,
            "selected": partial["selected"],
            "files": files,
            "all_four_regenerated": set(files) == set(PDF_SOURCES)
            and all((PDF_DIR / name).is_file() for name in PDF_SOURCES),
            "reused_prior_record": bool(prior.get("files")),
        }

    texts = {name: (TOPIC / name).read_text(encoding="utf-8") for name in (
        "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
        "COVERAGE-LEDGER.md", "ANSWER-WRITING-TOOLKIT.md", "PRACTICE-LOG.md")}
    questions = parse_mcqs(texts["MCQ-QUESTIONS.md"])
    solutions = parse_mcqs(texts["MCQ-SOLUTIONS.md"])
    audit_payload = json.loads((TOPIC / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    declared_key = "".join(row["answer"] for row in audit_payload["questions"])
    key = EXPECTED_KEYS
    failures = []

    required = {name: (TOPIC / name).is_file() for name in REQUIRED}
    if not all(required.values()):
        failures.append("required_files")
    formal = formal_validation.validate_audit(mode=args.mode)
    if not formal["pass"]:
        failures.append("formal_coverage_audit")
    numbering = {
        "question_count": len(questions), "solution_count": len(solutions),
        "consecutive": [x["number"] for x in questions] == list(range(1, MCQ_COUNT + 1)),
        "matching": len(questions) == len(solutions) == MCQ_COUNT and all(
            q["number"] == s["number"] and q["stem"] == s["stem"] and q["options"] == s["options"]
            for q, s in zip(questions, solutions)
        ),
        "four_options": all(set(x["options"]) == set("ABCD") for x in questions),
    }
    numbering["pass"] = all(value for key_name, value in numbering.items() if key_name not in {"question_count","solution_count"})
    if not numbering["pass"]:
        failures.append("mcq_numbering")
    leakage = {marker: marker in texts["MCQ-QUESTIONS.md"] for marker in ("**Answer:","Option explanations:","Correct proposition:","Repair action:")}
    if any(leakage.values()):
        failures.append("question_leakage")
    answers = [s["answer"] for s in solutions]
    max_run = max(len(list(group)) for _, group in __import__("itertools").groupby(answers)) if answers else 0
    distribution = dict(Counter(answers))
    answer_pattern = {
        "key": "".join(answers), "distribution": distribution, "maximum_run": max_run,
        "validator_expected_key": EXPECTED_KEYS,
        "audit_declared_key_matches": declared_key == EXPECTED_KEYS,
        "mechanical_abcd_rotation": any("".join(answers) == (pattern * 16)[:MCQ_COUNT] for pattern in ("ABCD","BCDA","CDAB","DABC")),
    }
    answer_pattern["pass"] = (
        "".join(answers) == EXPECTED_KEYS
        and declared_key == EXPECTED_KEYS
        and max_run <= 2
        and max(distribution.values()) - min(distribution.values()) <= 2
        and not answer_pattern["mechanical_abcd_rotation"]
    )
    if not answer_pattern["pass"]:
        failures.append("answer_pattern")
    option_result = option_quality(questions, key)
    if not option_result["pass"]:
        failures.append("option_quality")
    audit_result = audit_checks(questions, solutions, key)
    if not audit_result["pass"]:
        failures.append("mcq_audit")
    mcq13 = mcq13_logic_check(questions, solutions)
    if not mcq13["pass"]:
        failures.append("mcq13_logic")
    dedup = deduplication_checks(questions, key)
    if not dedup["pass"]:
        failures.append("deduplication")
    marker_counts = {marker: texts["MCQ-SOLUTIONS.md"].count(marker) for marker in ("**Answer:","**Option explanations:**","**Examiner trap:**","**Repair action:**","**Coverage mapping:**","**PYQ linkage:**")}
    solutions_complete = {"counts": marker_counts, "expected": MCQ_COUNT, "pass": all(value == MCQ_COUNT for value in marker_counts.values())}
    if not solutions_complete["pass"]:
        failures.append("solutions_complete")
    doctrinal = doctrinal_checks(texts["REVISION-GUIDE.md"], texts["ANSWER-WRITING-TOOLKIT.md"])
    if not doctrinal["pass"]:
        failures.append("doctrinal")
    toolkit = toolkit_checks_reconciled(texts["ANSWER-WRITING-TOOLKIT.md"])
    if not toolkit["pass"]:
        failures.append("toolkit")
    band_instructions = band_instruction_checks(texts["ANSWER-WRITING-TOOLKIT.md"])
    if not band_instructions["pass"]:
        failures.append("band_instruction_consistency")
    production_tests = package_negative_tests(
        texts["ANSWER-WRITING-TOOLKIT.md"], formal
    )
    if not production_tests["pass"]:
        failures.append("package_negative_tests")
    provenance_docs = {
        name: texts[name]
        for name in ("README.md", "REVISION-GUIDE.md", "COVERAGE-LEDGER.md")
    }
    forbidden = (
        "preserved verbatim",
        "sliced verbatim",
        "each canonical passage exactly once",
        "copied unchanged",
        "semantic completeness is guaranteed",
    )
    provenance = {
        "authoritative_formal_root": str(AUTHORITATIVE_FORMAL_ROOT),
        "formal_sources_under_authoritative_root": all(
            str(path).casefold().startswith(str(AUTHORITATIVE_FORMAL_ROOT).casefold())
            for path in FORMAL_SOURCES.values()
        ),
        "forbidden_derivative_root_not_used": all(
            not str(path).casefold().startswith(
                str(FORBIDDEN_DERIVATIVE_FORMAL_ROOT).casefold()
            )
            for path in FORMAL_SOURCES.values()
        ),
        "required_statement": all(
            phrase
            in token_normalise(texts["README.md"] + texts["REVISION-GUIDE.md"])
            for phrase in (
                "canonical owner file is substantially retained where already final",
                "source cells were reconciled adapted and mapped",
                "repeated apparatus was consolidated",
                "mechanical validation does not prove semantic completeness",
            )
        ),
        "forbidden_claims": {
            name: [
                phrase for phrase in forbidden if phrase in normalise(text)
            ]
            for name, text in provenance_docs.items()
        },
    }
    provenance["pass"] = (
        provenance["formal_sources_under_authoritative_root"]
        and provenance["forbidden_derivative_root_not_used"]
        and provenance["required_statement"]
        and not any(provenance["forbidden_claims"].values())
    )
    if not provenance["pass"]:
        failures.append("provenance_wording")
    pdfs = {
        name: pdf_checks(
            PDF_DIR / name,
            TOPIC / source,
            regeneration["files"].get(name),
        )
        for name, source in PDF_SOURCES.items()
    }
    if not all(value["pass"] for value in pdfs.values()):
        failures.append("pdfs")
    temp = sorted(str(path.relative_to(TOPIC)) for pattern in ("*.tmp","*_data.py","*.render.html","*.layout-pass.pdf","*.finalized.pdf","*.pyc") for path in TOPIC.rglob(pattern))
    temp += sorted(str(path.relative_to(TOPIC)) for path in TOPIC.rglob("__pycache__") if path.is_dir())
    if temp:
        failures.append("temporary_files")
    integrity = isolated_text_integrity()
    if not integrity["pass"]:
        failures.append("text_integrity")
    practice_blank = not re.search(r"(?im)^\s*(score|attempt|answer)\s*:\s*\S+", texts["PRACTICE-LOG.md"])
    if not practice_blank:
        failures.append("practice_log")
    release = release_integrity(formal)
    if args.mode == "precommit" and not release["pass"]:
        failures.append("release_integrity")

    if failures:
        result = "FAIL"
    elif args.mode == "precommit":
        result = "RELEASE_PASS"
    else:
        result = "DEVELOPMENT_PASS"
    report = {
        "schema_version": 16,
        "topic": "11 Quine and Strawson",
        "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "result": result,
        "validation_mode": args.mode,
        "release_ready": release["pass"],
        "result_gate": (
            "DEVELOPMENT_PASS validates the isolated package and generated artifacts. "
            "RELEASE_PASS additionally requires every current required file in the Git "
            "index and all external obligations closed."
        ),
        "pdf_generation": regeneration,
        "checks": {
            "required_files": required,
            "formal_coverage_audit": formal,
            "mcq_numbering": numbering,
            "question_answer_leakage": leakage,
            "answer_pattern": answer_pattern,
            "option_and_cue_quality": option_result,
            "parsed_mcq_audit": audit_result,
            "mcq13_formal_logic": mcq13,
            "duplicate_tested_inferences": dedup,
            "solutions_complete": solutions_complete,
            "doctrinal_coverage": doctrinal,
            "answer_writing_toolkit": toolkit,
            "band_instruction_consistency": band_instructions,
            "package_negative_tests": production_tests,
            "provenance_wording": provenance,
            "pdfs": pdfs,
            "practice_log_blank_template": practice_blank,
            "temporary_files_left": temp,
            "text_and_diff_integrity": integrity,
            "release_integrity": release,
        },
        "failures": failures,
        "mechanical_limits": (
            "Development validation certifies enumerated source-block accounting, "
            "reviewed source/destination correspondence, panel parity, randomized MCQ "
            "gates, exact PYQ structure, locked word bands and PDF mechanics. It does "
            "not prove philosophical truth, semantic completeness or examiner marks. "
            "Release is intentionally blocked by serialized external obligations."
        ),
    }
    VALIDATION.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pages = ", ".join(f"{name}: {value['pages']}" for name, value in pdfs.items())
    print(
        f"{result}: formal={formal.get('formal_block_count', 0)} "
        f"panels={formal.get('panel_count', 0)} MCQs={MCQ_COUNT} "
        f"PYQs={len(toolkit.get('verified_pyqs', {}))} "
        f"originals={len(toolkit.get('original_solved_practice', {}))}; "
        f"PDF pages={{{pages}}}; release_ready={release['pass']}"
    )
    if failures:
        print("Failures:", ", ".join(failures))
        return 1
    return 0 if result in {"DEVELOPMENT_PASS", "RELEASE_PASS"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
