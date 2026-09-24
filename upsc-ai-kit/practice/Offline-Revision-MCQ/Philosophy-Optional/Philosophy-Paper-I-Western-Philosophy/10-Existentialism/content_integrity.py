from __future__ import annotations

import argparse
import hashlib
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


TOPIC = Path(__file__).resolve().parent
REPO = TOPIC.parents[4]
TOOLS = REPO.parent / "tools"
PDF_DIR = TOPIC / "pdf"
VALIDATION = TOPIC / "VALIDATION.json"
MCQ_COUNT = 74
DIRECT_PYQS = [
    ("2018", "Q1(d)", 10), ("2018", "Q4(a)", 20),
    ("2019", "Q3(a)", 20), ("2019", "Q4(c)", 15),
    ("2020", "Q3(a)", 20), ("2020", "Q4(a)", 20),
    ("2021", "Q4(b)", 15), ("2022", "Q2(a)", 20),
    ("2022", "Q4(a)", 20), ("2023", "Q1(d)", 10),
    ("2023", "Q3(c)", 15), ("2024", "Q1(e)", 10),
    ("2024", "Q4(a)", 20), ("2025", "Q1(c)", 10),
    ("2026", "Q2(c)", 15), ("2026", "Q3(b)", 15),
]
WORD_BANDS = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
CORRELATION_ALLOWLIST = {
    "transcendental ego",
    "the transcendental ego",
    "ready to hand",
    "present at hand",
    "being in the world",
    "relation to god",
}
CORRELATION_STOPWORDS = {
    "a", "an", "and", "as", "at", "be", "because", "by", "for", "from", "in",
    "into", "is", "it", "its", "not", "of", "on", "or", "that", "the",
    "their", "this", "through", "to", "while", "with",
}
LINEAGE_STOPWORDS = CORRELATION_STOPWORDS | {
    "does", "existentialism", "heidegger", "how", "kierkegaard", "mean",
    "means", "most", "sartre", "sartrean", "should", "what", "which", "why",
}
LEAKED_ANSWER_LABELS = (
    "critical account of being-in-the-world",
    "objection, reply, verdict",
    "doctrine and the pivotal argument",
    "the slogan and its argument",
    "correcting the question",
    "subjectivity defined",
    "the three stages",
    "the leap and the link to subjectivity",
    "being-in-the-world vs the transcendental ego",
)
G6_DIR = (
    REPO
    / "knowledge/Learner-v2-Refreshed/Philosophy/Paper-I-Western-Philosophy"
    / "learning-sessions/topic-10/g6"
)
CANONICAL = REPO / "knowledge/Philosophy/paper-1/western/Existentialism.md"
PDF_SOURCES = {
    "Revision-Guide.pdf": "REVISION-GUIDE.md",
    "MCQ-Questions.pdf": "MCQ-QUESTIONS.md",
    "MCQ-Solutions.pdf": "MCQ-SOLUTIONS.md",
    "Answer-Writing-Toolkit.pdf": "ANSWER-WRITING-TOOLKIT.md",
}
REQUIRED = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md", "COVERAGE-LEDGER.md", "PRACTICE-LOG.md",
    "ANSWER-WRITING-TOOLKIT.md", "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json", "validate_package.py",
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
            correct_rate = correct / len(class_rows["correct"])
            distractor_rate = distractor / len(class_rows["distractor"])
            gap = abs(correct_rate - distractor_rate)
            exclusive = correct == 0 or distractor == 0
            fisher_probability = None
            if exclusive and support:
                class_size = len(class_rows["correct"]) if correct else len(class_rows["distractor"])
                other_size = len(class_rows["distractor"]) if correct else len(class_rows["correct"])
                fisher_probability = exclusive_fisher_probability(support, class_size, other_size)
            row = {
                "ngram": size, "feature": feature, "correct_count": correct,
                "distractor_count": distractor, "support": support,
                "correct_rate_percent": round(correct_rate * 100, 2),
                "distractor_rate_percent": round(distractor_rate * 100, 2),
                "rate_gap_percent": round(gap * 100, 2), "class_exclusive": exclusive,
                "exclusive_fisher_probability": round(fisher_probability, 8) if fisher_probability is not None else None,
            }
            if support >= threshold["statistical_minimum_support"]:
                inspected.append(row)
            automatic = support >= threshold["automatic_exclusive_support"]
            statistical = (
                support >= threshold["statistical_minimum_support"]
                and fisher_probability is not None
                and fisher_probability <= threshold["maximum_fisher_probability"]
            )
            if exclusive and (automatic or statistical):
                flagged.append(row)
    return {
        "method": "Per-option presence counts for normalized 1-, 2- and 3-grams across 74 correct and 222 distractor options.",
        "thresholds": thresholds,
        "allowlist": sorted(CORRELATION_ALLOWLIST),
        "allowlist_scope": "Only unavoidable multiword doctrine terms are exempt; generic adverbs, determiners and generated filler are not allowlisted.",
        "high_support_features_inspected": inspected,
        "strong_class_exclusive_features": flagged,
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
    }
    features = {name: {"correct": 0, "distractor": 0} for name in feature_patterns}
    incomplete = []
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
            if not text[:1].isupper() or text[-1:] != "." or len(words(text)) < 8:
                incomplete.append([n, letter, text])
            for name, pattern in feature_patterns.items():
                if re.search(pattern, text, re.I):
                    features[name][kind] += 1
    count = len(mcqs)
    longest_rate = round(100 * len(longest) / count, 2)
    unique_rate = round(100 * len(unique) / count, 2)
    cue_failures = []
    for name, values in features.items():
        correct_rate = values["correct"] / count
        distractor_rate = values["distractor"] / (count * 3)
        values["correct_rate_percent"] = round(100 * correct_rate, 2)
        values["distractor_rate_percent"] = round(100 * distractor_rate, 2)
        values["gap_percent"] = round(100 * abs(correct_rate - distractor_rate), 2)
        if values["correct"] + values["distractor"] >= 5 and abs(correct_rate - distractor_rate) > 0.20:
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
        "lexical_and_punctuation_features": features,
        "failed_feature_correlations": cue_failures,
        "two_sentence_rate_gap_percent": syntactic_gap,
        "data_driven_token_ngram_correlation": correlation,
        "locked_bands": {"correct_longest": [15, 40], "unique_longest": [5, 30]},
        "pass": 15 <= longest_rate <= 40 and 5 <= unique_rate <= 30
        and not outliers and not incomplete and not cue_failures and syntactic_gap <= 12
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
        "abraham", "anxiety", "authenticity", "care", "camus", "consciousness",
        "dasein", "despair", "epoché", "facticity", "freedom", "heidegger",
        "husserl", "kierkegaard", "nietzsche", "sartre", "temporality",
        "transcendence",
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


def rationale_specificity(value: str, false_text: str, correction: str, anchors: list[str]) -> bool:
    residual = strip_declared_propositions(value, false_text, correction)
    normalized = token_normalise(residual)
    domain_terms = {
        "absolute", "anxiety", "appropriation", "authenticity", "being", "care",
        "choice", "consciousness", "dasein", "despair", "duty", "ego", "essence",
        "existence", "facticity", "faith", "freedom", "historicality", "humanism",
        "intentionality", "inwardness", "nihilation", "ontology", "possibility",
        "project", "reduction", "responsibility", "selfhood", "temporality",
        "transcendence", "world", "camus", "heidegger", "husserl",
        "kierkegaard", "nietzsche", "sartre", "abraham", "aesthetic",
        "attunement", "conscience", "crowd", "dasein", "death", "ethical",
        "equipment", "equipmental", "future", "god", "historical",
        "inauthenticity", "look", "paper-knife", "practical", "pseudonyms",
        "religious", "role", "self", "system", "tool",
    }
    residual_tokens = set(normalized.split())
    return (
        len(words(residual)) >= 18
        and len(anchors) >= 2
        and all(token_normalise(anchor) in normalized for anchor in anchors)
        and len({token for token in normalized.split() if len(token) >= 5 and token not in CORRELATION_STOPWORDS}) >= 6
        and len(residual_tokens & domain_terms) >= 1
    )


def audit_checks(questions: list[dict], solutions: list[dict], key: str) -> dict:
    payload = json.loads((TOPIC / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    rows = {int(row["number"]): row for row in payload.get("questions", [])}
    failures = []
    rationale_bodies = []
    rationale_frames = []
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
        if row.get("answer") != key[n - 1]:
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
        true_letters = [letter for letter in "ABCD" if audited_options.get(letter, {}).get("truth_value") is True]
        if true_letters != [key[n - 1]]:
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
            anchors = option.get("rationale_anchors" if letter == key[n - 1] else "correction_anchors", [])
            if len(anchors) < 2 or any(token_normalise(anchor) not in token_normalise(rationale) for anchor in anchors):
                reasons.append(f"{letter} rationale anchors fail")
            if letter != key[n - 1]:
                if option.get("false_proposition") != visible:
                    reasons.append(f"{letter} false proposition mismatch")
                if option.get("specific_correction") != question["options"][key[n - 1]]:
                    reasons.append(f"{letter} correction mismatch")
                false_anchors = option.get("false_proposition_anchors", [])
                if len(false_anchors) < 2 or any(token_normalise(anchor) not in token_normalise(visible) for anchor in false_anchors):
                    reasons.append(f"{letter} false-proposition anchors fail")
                wrong = visible.rstrip(".")
                correct = question["options"][key[n - 1]].rstrip(".")
                body = solution["explanations"].get(letter, "")
                if f"False proposition: “{wrong}.”" not in body or f"Correct replacement: “{correct}.”" not in body:
                    reasons.append(f"{letter} exact false/correction text missing")
                if not option.get("error_type"):
                    reasons.append(f"{letter} missing error type")
                if not rationale_specificity(rationale, visible, question["options"][key[n - 1]], anchors):
                    reasons.append(f"{letter} residual rationale lacks option-specific diagnosis or correction")
                residual = strip_declared_propositions(rationale, visible, question["options"][key[n - 1]])
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
        negative_controls[f"control_{index}"] = not rationale_specificity(
            control["rationale"], control["false_proposition"],
            control["specific_correction"], control["rationale_anchors"],
        )
    return {
        "schema_version": payload.get("schema_version"),
        "manifest_question_count": len(rows),
        "visible_question_count": len(questions),
        "repeated_normalized_rationales": duplicates,
        "repeated_normalized_sentence_frames": repeated_frames,
        "near_duplicate_rationale_pairs": near_duplicates,
        "within_item_option_similarity_flags": within_item_similarity,
        "exact_duplicate_options_across_items": option_duplicates,
        "generic_negative_controls_rejected": negative_controls,
        "failures": failures,
        "mechanical_limitations": "Quoted predicates, correction anchors, frame diversity and similarity checks can reject boilerplate; they cannot independently establish philosophical truth.",
        "pass": payload.get("schema_version") == 4 and len(rows) == MCQ_COUNT
        and not failures and not duplicates and not repeated_frames and not near_duplicates
        and not within_item_similarity and not option_duplicates
        and controls and all(negative_controls.values()),
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


def source_lineage_checks(revision: str, ledger: str, questions: list[dict]) -> dict:
    session = sorted(G6_DIR.glob("*Complete-Learning-Session*.md"))[-1]
    workbook = sorted(G6_DIR.glob("*Solved-Practice-Workbook*.md"))[-1]
    sources = {"g6_session": session, "g6_workbook": workbook, "canonical": CANONICAL}
    texts = {name: path.read_text(encoding="utf-8") for name, path in sources.items()}
    inventory_rows = table_rows(ledger, "## Mechanical source-cell inventory")
    inventory, failures = {}, []
    for row in inventory_rows:
        if len(row) != 6:
            failures.append({"row": row, "reason": "malformed source cell"})
            continue
        cell, coverage, session_anchor, workbook_anchor, canonical_anchor, witness_text = row
        sections = {
            "g6_session": anchored_section(texts["g6_session"], session_anchor),
            "g6_workbook": anchored_section(texts["g6_workbook"], workbook_anchor),
            "canonical": anchored_section(texts["canonical"], canonical_anchor),
        }
        witnesses = [term.strip() for term in witness_text.split(";")]
        combined = "\n".join(sections.values())
        checks = {term: normalise(term) in normalise(combined) and normalise(term) in normalise(revision) for term in witnesses}
        passed = all(sections.values()) and all(checks.values())
        inventory[cell] = {"coverage": coverage, "witnesses": checks, "pass": passed}
        if not passed:
            failures.append({"source_cell": cell, "reason": "anchor or witness missing"})
    candidates = parse_source_candidates(texts["g6_workbook"])
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
    return {
        "source_files_read": source_files,
        "source_cell_count": len(inventory),
        "source_cells": inventory,
        "lineage_mapping_count": len(mapped),
        "lineage_counts": dict(Counter(value["lineage"] for value in mapped.values())),
        "mapped_unique_source_candidates": len(set(used_candidates)),
        "unmapped_source_candidates": sorted(set(candidates) - set(used_candidates)),
        "failures": failures,
        "mechanical_limitations": "This checks file identity, anchors, witnesses and declared candidate links; it does not prove semantic completeness.",
        "pass": len(inventory) == 11 and len(mapped) == MCQ_COUNT
        and set(mapped) == set(range(1, MCQ_COUNT + 1))
        and len(used_candidates) == len(set(used_candidates)) and not failures,
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
        if len(words(sentence)) < 5 and not finite_verb.search(sentence)
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
        "pass": set(pyqs) == expected and len(originals) == 9 and not failures
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
        and len(payload.get("pyqs", [])) == 16 and len(payload.get("originals", [])) == 9
        and set(results) == set(expected) | {f"Original {number}" for number in range(1, 10)}
        and not failures,
    }


def doctrinal_checks(revision: str, toolkit: str) -> dict:
    combined = normalise(revision + "\n" + toolkit)
    required = {
        "family_not_flattened": "family of distinct projects" in combined,
        "kierkegaard_complete": all(term in combined for term in ("single individual","truth is subjectivity","aesthetic","ethical","religious","anxiety","despair")),
        "nietzsche_bounded": "nietzsche" in combined and "bounded" in combined,
        "heidegger_complete": all(term in combined for term in ("dasein","being-in-the-world","care","thrown","projection","falling","das man","being-toward-death","temporality")),
        "heidegger_nonmoral": "not a moral" in combined or "non-moral" in combined,
        "sartre_complete": all(term in combined for term in ("existence precedes essence","being-in-itself","being-for-itself","nothingness","facticity","transcendence","bad faith","the look")),
        "freedom_not_arbitrary": "situated freedom" in combined and "arbitrary" in combined,
        "husserl_boundary": "epoché" in combined and "transcendental ego" in combined and "intentionality" in combined,
        "variants_and_absurdity": "theistic" in combined and "atheistic" in combined and "absurd" in combined,
        "criticism": "formal emptiness" in combined and "fideism" in combined and "oppression" in combined,
    }
    forbidden = {
        "all_existentialists_own_slogan": r"all existentialists (?:accept|share|use).{0,40}existence precedes essence",
        "sartrean_omnipotence": r"sartre.{0,80}freedom means.{0,40}(?:anything|unlimited physical)",
        "heidegger_moral_authenticity": r"heidegger.{0,80}authenticity (?:is|means) moral goodness",
        "sartre_refuted_husserl": r"sartre refuted husserl",
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
        "matches_current_regeneration_record": regeneration_matches,
        "blank_pages": sorted(set(blank)), "replacement_glyphs": replacements,
        "out_of_bounds_text_pages": sorted(set(bounds)),
        "content_overlap_pages": sorted(set(overlaps)),
        "raw_markdown_artifacts": markdown,
        "pass": pages > 0 and not blank and not replacements and not bounds and not overlaps
        and not markdown and not missing_headings and path.stat().st_mtime_ns >= source_path.stat().st_mtime_ns
        and regeneration_matches,
    }


def regenerate_pdfs() -> dict:
    sys.path.insert(0, str(TOOLS))
    import unicode_markdown_pdf
    descriptors = {
        "Revision-Guide.pdf": "Philosophy Optional · Paper I · Western Philosophy · Topic 10",
        "MCQ-Questions.pdf": "74-question closed-book practice bank · no answer key",
        "MCQ-Solutions.pdf": "Proposition-specific explanations and repairs",
        "Answer-Writing-Toolkit.pdf": "Sixteen verified PYQs and three original solved answers",
    }
    files = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        output = PDF_DIR / pdf_name
        output.unlink(missing_ok=True)
        unicode_markdown_pdf.build_pdf(
            TOPIC / source_name, output, internal_index=True, index_title="CONTENTS",
            cover_descriptor=descriptors[pdf_name],
            footer_label=f"Existentialism | {source_name.removesuffix('.md')}",
        )
        files[pdf_name] = {
            "source": source_name, "exists": output.is_file(),
            "bytes": output.stat().st_size if output.exists() else 0,
            "sha256": hashlib.sha256(output.read_bytes()).hexdigest() if output.exists() else None,
            "source_sha256": hashlib.sha256((TOPIC / source_name).read_bytes()).hexdigest(),
            "source_mtime_ns": (TOPIC / source_name).stat().st_mtime_ns,
            "pdf_mtime_ns": output.stat().st_mtime_ns if output.exists() else None,
        }
    return {"requested": True, "files": files, "all_four_regenerated": all(x["exists"] for x in files.values())}


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regenerate", action="store_true")
    args = parser.parse_args()
    regeneration = {"requested": False, "files": {}, "all_four_regenerated": False}
    if args.regenerate:
        regeneration = regenerate_pdfs()

    texts = {name: (TOPIC / name).read_text(encoding="utf-8") for name in (
        "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
        "COVERAGE-LEDGER.md", "ANSWER-WRITING-TOOLKIT.md", "PRACTICE-LOG.md")}
    questions = parse_mcqs(texts["MCQ-QUESTIONS.md"])
    solutions = parse_mcqs(texts["MCQ-SOLUTIONS.md"])
    audit_payload = json.loads((TOPIC / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    key = "".join(row["answer"] for row in audit_payload["questions"])
    failures = []

    required = {name: (TOPIC / name).is_file() for name in REQUIRED}
    if not all(required.values()):
        failures.append("required_files")
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
        "mechanical_abcd_rotation": any("".join(answers) == (pattern * 19)[:MCQ_COUNT] for pattern in ("ABCD","BCDA","CDAB","DABC")),
    }
    answer_pattern["pass"] = "".join(answers) == key and max_run <= 2 and max(distribution.values()) - min(distribution.values()) <= 2 and not answer_pattern["mechanical_abcd_rotation"]
    if not answer_pattern["pass"]:
        failures.append("answer_pattern")
    option_result = option_quality(questions, key)
    if not option_result["pass"]:
        failures.append("option_quality")
    audit_result = audit_checks(questions, solutions, key)
    if not audit_result["pass"]:
        failures.append("mcq_audit")
    dedup = deduplication_checks(questions, key)
    if not dedup["pass"]:
        failures.append("deduplication")
    marker_counts = {marker: texts["MCQ-SOLUTIONS.md"].count(marker) for marker in ("**Answer:","**Option explanations:**","**Examiner trap:**","**Repair action:**","**Coverage mapping:**","**PYQ linkage:**")}
    solutions_complete = {"counts": marker_counts, "expected": MCQ_COUNT, "pass": all(value == MCQ_COUNT for value in marker_counts.values())}
    if not solutions_complete["pass"]:
        failures.append("solutions_complete")
    lineage = source_lineage_checks(texts["REVISION-GUIDE.md"], texts["COVERAGE-LEDGER.md"], questions)
    if not lineage["pass"]:
        failures.append("source_lineage")
    doctrinal = doctrinal_checks(texts["REVISION-GUIDE.md"], texts["ANSWER-WRITING-TOOLKIT.md"])
    if not doctrinal["pass"]:
        failures.append("doctrinal")
    toolkit = toolkit_checks(texts["ANSWER-WRITING-TOOLKIT.md"])
    if not toolkit["pass"]:
        failures.append("toolkit")
    demand = demand_audit_checks(texts["ANSWER-WRITING-TOOLKIT.md"])
    if not demand["pass"]:
        failures.append("pyq_demand_audit")
    provenance_docs = {name: texts[name] for name in ("README.md","REVISION-GUIDE.md","COVERAGE-LEDGER.md")}
    forbidden = ("preserved verbatim","sliced verbatim","each canonical passage exactly once","copied unchanged","semantic completeness is guaranteed")
    provenance = {
        "required_statement": all(phrase in token_normalise(texts["README.md"] + texts["REVISION-GUIDE.md"]) for phrase in (
            "substantive source cells were reconciled adapted and mapped",
            "repeated apparatus was consolidated",
            "does not prove semantic completeness",
        )),
        "forbidden_claims": {name: [phrase for phrase in forbidden if phrase in normalise(text)] for name, text in provenance_docs.items()},
    }
    provenance["pass"] = provenance["required_statement"] and not any(provenance["forbidden_claims"].values())
    if not provenance["pass"]:
        failures.append("provenance_wording")
    pdfs = {
        name: pdf_checks(
            PDF_DIR / name,
            TOPIC / source,
            regeneration["files"].get(name) if args.regenerate else None,
        )
        for name, source in PDF_SOURCES.items()
    }
    release_regeneration = {
        "regenerate_flag_required": True,
        "regenerate_flag_present": args.regenerate,
        "all_four_regenerated": regeneration["all_four_regenerated"],
        "source_hash_timestamp_records_complete": all(
            value["matches_current_regeneration_record"] for value in pdfs.values()
        ),
        "pass": args.regenerate and regeneration["all_four_regenerated"]
        and all(value["matches_current_regeneration_record"] for value in pdfs.values()),
    }
    if not release_regeneration["pass"]:
        failures.append("release_regeneration")
    if not all(value["pass"] for value in pdfs.values()):
        failures.append("pdfs")
    temp = sorted(str(path.relative_to(TOPIC)) for pattern in ("*.tmp","*_data.py","*.render.html","*.layout-pass.pdf","*.finalized.pdf","*.pyc") for path in TOPIC.rglob(pattern))
    temp += sorted(str(path.relative_to(TOPIC)) for path in TOPIC.rglob("__pycache__") if path.is_dir())
    if temp:
        failures.append("temporary_files")
    integrity = text_integrity()
    if not integrity["pass"]:
        failures.append("text_integrity")
    status = json.loads((REPO / "practice/Offline-Revision-MCQ/STATUS.json").read_text(encoding="utf-8"))
    index = (REPO / "practice/Offline-Revision-MCQ/INDEX.md").read_text(encoding="utf-8")
    repository_status = {
        "topic_10_validated": any(x.get("topic") == "10 Existentialism" and x.get("mcq_count") == MCQ_COUNT and x.get("directly_owned_solved_pyqs") == 16 for x in status["validated_topics"]),
        "next_topic_11": "11 Quine and Strawson" in status["next_action"] and "11 Quine and Strawson" in index,
        "topic_10_indexed": "10 Existentialism" in index and "74 MCQs" in index,
    }
    if not all(repository_status.values()):
        failures.append("repository_status")
    practice_blank = not re.search(r"(?im)^\s*(score|attempt|answer)\s*:\s*\S+", texts["PRACTICE-LOG.md"])
    if not practice_blank:
        failures.append("practice_log")

    report = {
        "schema_version": 13,
        "topic": "10 Existentialism",
        "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "result": "PASS" if not failures else "FAIL",
        "result_gate": "PASS only when every recorded check passes",
        "pdf_generation": {"mechanism": "C:/up/tools/unicode_markdown_pdf.py via installed Chrome and PyMuPDF", **regeneration},
        "checks": {
            "required_files": required, "mcq_numbering": numbering,
            "question_answer_leakage": leakage, "answer_pattern": answer_pattern,
            "option_and_cue_quality": option_result, "parsed_mcq_audit": audit_result,
            "duplicate_tested_inferences": dedup, "solutions_complete": solutions_complete,
            "source_lineage": lineage, "doctrinal_coverage": doctrinal,
            "answer_writing_toolkit": toolkit, "pyq_demand_audit": demand,
            "provenance_wording": provenance,
            "release_regeneration_gate": release_regeneration,
            "pdfs": pdfs,
            "practice_log_blank_template": practice_blank,
            "temporary_files_left": temp, "text_and_diff_integrity": integrity,
            "repository_status_files": repository_status,
        },
        "failures": failures,
    }
    VALIDATION.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pages = ", ".join(f"{name}: {value['pages']}" for name, value in pdfs.items())
    print(f"{report['result']}: {MCQ_COUNT} MCQs; correct-longest={option_result['correct_is_longest_rate_percent']}%; unique-longest={option_result['uniquely_longest_rate_percent']}%; PDF pages={{{pages}}}")
    if failures:
        print("Failures:", ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    print("Run validate_package.py; content_integrity.py is an internal companion gate.")
    raise SystemExit(2)
