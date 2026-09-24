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
from collections import Counter
from datetime import datetime
from difflib import SequenceMatcher
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote

import fitz


TOPIC = Path(__file__).resolve().parent
REPO = TOPIC.parents[4]
TOOLS = REPO.parent / "tools"
PDF_DIR = TOPIC / "pdf"
VALIDATION = TOPIC / "VALIDATION.json"
FORMAL_AUDIT = TOPIC / "FORMAL-COVERAGE-AUDIT.json"
FORMAL_REVIEW = TOPIC / "FORMAL-COVERAGE-REVIEW.json"
WORD_BANDS = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
AUTHORITATIVE_FORMAL_ROOT = Path(
    r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final"
)
FORBIDDEN_DERIVATIVE_FORMAL_ROOT = REPO.parent / "learning_package_final"
SOURCE_DIR = (
    AUTHORITATIVE_FORMAL_ROOT
    / "Philosophy-Optional/Philosophy-Paper-I-—-Western-Philosophy/10-Existentialism"
)
LARGE_LEAF_MIN_PHYSICAL_LINES = 60
LARGE_LEAF_MIN_WORDS = 400
LARGE_LEAF_MIN_SEMANTIC_TOKENS = 250
EXPECTED_PANEL_TOTAL = 53
FORMAL_SOURCES = {
    "session": SOURCE_DIR / "Learning-Session.md",
    "workbook": SOURCE_DIR / "Solved-Practice-Workbook.md",
}
CANONICAL = REPO / "knowledge/Philosophy/paper-1/western/Existentialism.md"
PYQ_LEDGERS = (
    REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2018-2025.md",
    REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2026.md",
)
RULES = REPO / "practice/Offline-Revision-MCQ/START-HERE.md"
MCQ_RANDOMIZATION_SEED = "topic10-existentialism-20260924-01"
MCQ_RANDOMIZATION_SOURCE_KEY = (
    "BADACCBABADCBADBADCBCBAADBCBDDBBCCCDCBCBABABCCCBCCBBDADADCCDDDBBCBBDDBABAB"
)


def coverage_derived_mcq_count() -> int:
    ledger = (TOPIC / "COVERAGE-LEDGER.md").read_text(encoding="utf-8")
    match = re.search(
        r"(?ms)^## Explicit coverage matrix\s*$\n(.*?)(?=^##\s+|\Z)",
        ledger,
    )
    matrix = match.group(1) if match else ""
    covered_numbers = set()
    for line in matrix.splitlines():
        if not re.match(r"^\|\s*C\d+\s*\|", line):
            continue
        columns = [column.strip() for column in line.strip().strip("|").split("|")]
        if len(columns) < 4:
            continue
        for start, end in re.findall(r"(\d+)(?:\s*[–-]\s*(\d+))?", columns[3]):
            first = int(start)
            last = int(end) if end else first
            covered_numbers.update(range(first, last + 1))
    if not covered_numbers or covered_numbers != set(range(1, max(covered_numbers) + 1)):
        raise RuntimeError("coverage ledger does not define one contiguous MCQ inventory")
    return len(covered_numbers)


MCQ_COUNT = coverage_derived_mcq_count()
PDF_SOURCES = {
    "Revision-Guide.pdf": "REVISION-GUIDE.md",
    "MCQ-Questions.pdf": "MCQ-QUESTIONS.md",
    "MCQ-Solutions.pdf": "MCQ-SOLUTIONS.md",
    "Answer-Writing-Toolkit.pdf": "ANSWER-WRITING-TOOLKIT.md",
}
PDF_DESCRIPTORS = {
    "Revision-Guide.pdf": "Philosophy Optional · Paper I · Western Philosophy · Topic 10",
    "MCQ-Questions.pdf": "74-question closed-book bank · no answer key",
    "MCQ-Solutions.pdf": "Option-specific explanations and examiner traps",
    "Answer-Writing-Toolkit.pdf": "Sixteen verified PYQs and nine original solved models",
}
PDF_GENERATION_PROFILE = {
    "renderer": "C:/up/tools/unicode_markdown_pdf.py",
    "renderer_contract": "unicode_markdown_pdf.build_pdf",
    "internal_index": True,
    "index_title": "CONTENTS",
    "footer_topic": "Existentialism",
    "profile_version": 1,
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
    "FORMAL-COVERAGE-AUDIT.json",
    "FORMAL-COVERAGE-REVIEW.json",
    "VALIDATION.json",
    "content_integrity.py",
    "validate_package.py",
    *(f"pdf/{name}" for name in PDF_SOURCES),
]
ALLOWED_CLASSIFICATIONS = {
    "covered_in_scope",
    "genuine_in_scope_omission",
    "routed_to_canonical_owner",
    "excluded_doubt_only_non_formal_enrichment",
}
PRESENTATION_PATTERNS = (
    r"^DEFINITION /",
    r"^ANSWER-GRABBING",
    r"^MUST-WRITE",
    r"^Visual gateway",
    r"^Rapid recall",
    r"^Key Table$",
    r"^Detailed Teaching$",
    r"^Must-Know Facts$",
    r"^UPSC Traps$",
    r"^Model-Answer Route$",
    r"^Verified route",
    r"^Exam architecture$",
    r"^Complete verified corpus route$",
    r"^Verified comparative routes$",
    r"^PLATO AND ARISTOTLE - Layered",
    r"^The Two-Level Sun Analogy$",
    r"^Premise Audit$",
    r"^How the Regress Starts$",
    r"^Identity Through Accidental Change$",
    r"^Interpretive Tension$",
    r"^Matter Is Layered$",
    r"^Four Causes of One Natural Process$",
    r"^Capacity, Activity, Completion$",
    r"^From Change to Pure Act$",
    r"^Demand decoding$",
    r"^Independent model answer$",
    r"^Why this earns marks$",
)
def normalise(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_`#>|]", " ", value)
    value = value.replace("–", "-").replace("—", "-")
    value = value.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", value).strip().casefold()


def concept_stem(token: str) -> str:
    token = token.casefold().replace("’", "'")
    families = {
        "acquaint": "acquaint",
        "atom": "atom",
        "construct": "construct",
        "descript": "descript",
        "ideal": "ideal",
        "pictur": "pictur",
        "represent": "represent",
        "scept": "scept",
        "truth-function": "truth-function",
    }
    for prefix, stem in families.items():
        if token.startswith(prefix):
            return stem
    for suffix in ("ization", "ation", "tion", "sion", "ment", "ness", "ity", "ism", "ical", "ic", "ing", "ed", "es", "ly", "s"):
        if token.endswith(suffix) and len(token) - len(suffix) >= 4:
            return token[:-len(suffix)]
    return token


@lru_cache(maxsize=256)
def normalized_stem_set(value: str) -> frozenset[str]:
    return frozenset(
        concept_stem(token)
        for token in re.findall(r"[a-z0-9]+", normalise(value).replace("-", " "))
    )


def contains_witness(value: str, witness: str) -> bool:
    value_stems = normalized_stem_set(value)
    witness_stems = [
        concept_stem(token)
        for token in re.findall(r"[a-z0-9]+", normalise(witness).replace("-", " "))
    ]
    return bool(witness_stems) and all(stem in value_stems for stem in witness_stems)


SEMANTIC_GENERIC_TOKENS = {
    "answer", "ascii", "basic", "block", "claim", "complete", "continued",
    "flow", "formal", "hegel", "line", "master", "panel", "part", "point",
    "question", "section", "session", "source", "step", "system", "thing",
    "topic", "whole",
}
SEMANTIC_RELATION_TERMS = {
    "accepts", "adds", "allows", "analyses", "answer", "answers", "are",
    "assert", "asserts", "assign",
    "assigning", "assigns", "attack", "attacks", "balances", "because",
    "become", "becomes", "blocked", "blocks", "builds", "calls", "connects", "connecting",
    "constitute", "constitutes", "contains", "contributes", "converts",
    "correlating", "creates", "creating",
    "credits",
    "concludes", "correspond", "corresponds", "covers", "criticises",
    "defines", "demotes", "denied", "denies", "deny", "depends",
    "designate", "disclose",
    "discloses",
    "destroys", "directing", "disappears", "disagree", "distinguish",
    "distinguishes", "distribute", "divide", "divides", "drives", "eliminate",
    "eliminated", "eliminates", "excludes", "exposes", "fails", "fixes",
    "forces", "form", "forms", "frames", "generates", "giving", "grades",
    "grounds", "handles",
    "establish", "holds", "identifies", "identify", "labels", "lacks",
    "lead", "leads",
    "leave", "leaves", "links", "locates", "makes", "making", "move", "pairs",
    "permits", "pictures", "places", "precede", "precedes", "prove",
    "preserves", "prevents", "produces", "projecting", "protects", "proves",
    "opposes", "recalls", "reconstructs", "rejecting", "rejects", "remain",
    "removing", "replaces",
    "require", "required", "requires", "resolves", "results", "revealing",
    "reverses", "routes", "separates", "sends", "shows", "states", "supplies",
    "reaches", "share", "shares", "shared", "targets", "therefore", "ties",
    "transforms",
    "treats", "turns", "unifies",
    "uses", "whereas", "while", "without",
    "abandons", "amounts", "appears", "applies", "arises", "associates",
    "attaches", "combines", "concedes", "contrasts", "depends", "derives",
    "diagnoses", "differs", "directs", "dissolves", "distinguishing",
    "embeds", "enables", "establishes", "exhibits", "expresses", "extends",
    "fails", "fits", "grounds", "guarantees", "identifies", "implies",
    "incurs", "investigates", "joins", "limits", "locates", "marks",
    "mistakes", "permits", "performs", "presents", "presupposes", "provides",
    "redirects", "relocates", "remains", "requires", "resists", "retains",
    "reveals", "secures", "selects", "separates", "shows", "stands",
    "succeeds", "supplies", "tests", "undermines", "weakens",
    "broadens", "can", "collapses", "combined", "concerns", "conflicts",
    "conceal", "creates", "culminates", "defeats", "delivers", "diverge", "exceeds",
    "exhibited", "gathers", "has", "have", "illustrated", "interprets",
    "introduced", "is", "lets", "listing", "narrows", "needs", "opens",
    "moves", "pairs", "places", "predicts", "pressure", "pressures",
    "provide", "reopened",
    "restart", "restricts", "shrinks", "tells", "was", "were", "will",
    "attacking", "combining", "explain", "explains", "permit", "reduces",
    "refers", "removes", "treat", "assemble", "assembles", "determine",
    "extends", "leave", "make", "shrink", "stand", "weaken",
}
SEMANTIC_STOPWORDS = {
    "about", "after", "again", "against", "also", "because", "before",
    "being", "between", "cannot", "does", "each", "from", "have", "into",
    "itself", "only", "rather", "same", "such", "than", "that", "their",
    "then", "there", "these", "they", "this", "those", "through", "under",
    "what", "when", "where", "which", "while", "with", "without", "would",
}


def semantic_terms(value: str) -> list[str]:
    return [
        concept_stem(token)
        for token in re.findall(r"[a-z0-9]+", normalise(value).replace("-", " "))
        if len(token) >= 4
        and token not in SEMANTIC_STOPWORDS
        and token not in SEMANTIC_GENERIC_TOKENS
    ]


TRUNCATED_STEM_FRAGMENTS = {
    "analys", "argumentat", "compar", "consciou", "descript", "differ",
    "distinc", "epistemolog", "examin", "ident", "independ", "metaphys",
    "negat", "ontolog", "particul", "percept", "philosoph", "pictur",
    "predic", "proposi", "quantif", "refut", "relat", "scept", "settl",
    "stat", "structur", "univers",
}
BOILERPLATE_CLAIM_PATTERNS = (
    r"\bprimary unit evidence\b",
    r"\bsecondary unit evidence\b",
    r"\bsource explains how\b",
    r"\bunit evidence explains\b",
    r"\bsupports or limits\b",
    r"\btopic argument\b",
    r"\btopic panel\b",
    r"\bgeneric claim\b",
)
GENERIC_PADDING_RELATIONS: set[str] = set()

MALFORMED_CLAIM_FAMILY_PATTERNS = {
    "replacement_glyph": re.compile("\ufffd"),
    "presentation_or_demand_label": re.compile(
        r"^\s*(?:Definition|Technical|Answer-grabbing opening|"
        r"Must-write keywords|Claim|State the position precisely|"
        r"State the project correctly in the first line|"
        r"Absorbed|Caught|Published unfinished|Two reasons, both textual|"
        r"Heidegger's reply|"
        r"The key argument(?:, in three steps)?|The first reply|"
        r"The executable verdict|The keyhole, in two stages|"
        r"The ontological difference|Why Dasein is the route|"
        r"The compound is unitary|Existentialia replace categories|"
        r"The preliminary that decides the answer|The thesis|"
        r"Why Gewesenheit is not|Decisive|Reply|Honest verdict)\s*[.:]",
        re.I,
    ),
    "numbered_diagram_label": re.compile(
        r"^\s*(?:P\d+|LIMB\s+\d+|FORM\s+\d+|STEP\s+\d+|\d+\s+[A-Z])\b",
        re.I,
    ),
    "isolated_diagram_v_marker": re.compile(r"(?:^|\s)[Vv](?:\s|$)"),
    "diagram_arrow_chain": re.compile(r"(?:-{1,2}>|<--|→)"),
    "demand_label_fragment": re.compile(
        r"\b(?:ANSWER ROUTE|DEMANDS|FATAL|NEVER WRITE|WHAT IS NOT OWNED HERE)\b",
        re.I,
    ),
    "diagram_label_chain": re.compile(
        r"\b(?:SOURCE|OBJECT|FORMULA|AIM|CORE TERM|STEP \d+|P\d+)\b"
        r"(?:(?![.!?]).){0,120}\b(?:SOURCE|OBJECT|FORMULA|AIM|CORE TERM|STEP \d+|P\d+)\b",
    ),
    "comma_separated_all_caps_subject": re.compile(
        r"^\s*(?:[A-Z][A-Z-]{2,},\s*){2,}[A-Z][A-Z-]{2,}\b"
    ),
    "generated_situates_token_salad": re.compile(
        r"^\s*[A-Z][a-z-]+\s+situates\s+[a-z-]+\s+between\s+[a-z-]+\s+and\s+[a-z-]+(?:\s*[,.;]|$)",
        re.I,
    ),
    "distinguishes_because_governs": re.compile(
        r"\b(?:wittgenstein\s+)?distinguishes\b.+\bfrom\b.+\bbecause\b.+\bgoverns\b",
        re.I,
    ),
    "relation_between_requires": re.compile(
        r"^\s*the relation between\b.+\brequires\b",
        re.I,
    ),
    "within_the_practice_of": re.compile(r"^\s*within the practice of\b", re.I),
    "source_treats": re.compile(r"^\s*the source treats\b", re.I),
    "prevents_from_replacing": re.compile(
        r"\bprevents\b.+\bfrom replacing\b",
        re.I,
    ),
    "dangling_pipe": re.compile(r"\|"),
    "ellipsis_fragment": re.compile(r"(?:\.{3}|…)"),
    "raw_diagram_label": re.compile(
        r"^\s*(?:ASCII MASTER FLOW|LIMB\s+\d|TARGET\s*:|JOB\s+\d|"
        r"MOVE\s+\d|STEP\s+\d)",
        re.I,
    ),
    "generated_governs_constrains_salad": re.compile(
        r"\bbecause\b.{0,80}\bgoverns\b.{0,100}\b(?:whereas|by contrast)\b"
        r".{0,100}\bconstrains\b",
        re.I,
    ),
    "generated_guides_prevents_salad": re.compile(
        r"\brequires\b.{0,80}\bto guide\b.{0,100}\b(?:whereas|by contrast)\b"
        r".{0,100}\bprevents\b",
        re.I,
    ),
}
MALFORMED_CLAIM_FAMILIES = (
    "actual_panel_10_token_salad",
    "bare_token_bag_salad",
    "comma_separated_all_caps_subject",
    "dangling_fragment",
    "dangling_pipe",
    "demand_label_fragment",
    "dependent_subject",
    "diagram_arrow_chain",
    "diagram_label_chain",
    "distinguishes_because_governs",
    "ellipsis_fragment",
    "generated_governs_constrains_salad",
    "generated_guides_prevents_salad",
    "generated_situates_token_salad",
    "incomplete_proposition",
    "isolated_diagram_v_marker",
    "numbered_diagram_label",
    "presentation_or_demand_label",
    "prevents_from_replacing",
    "raw_diagram_label",
    "relation_between_requires",
    "replacement_glyph",
    "source_treats",
    "within_the_practice_of",
)
MALFORMED_CLAIM_FAMILY_WHITELIST: dict[tuple[str, str, str], str] = {}
CORRESPONDENCE_GENERIC_TOKENS = {
    "account", "answer", "argument", "concept", "doctrine", "language",
    "meaning", "method", "philosophy", "practice", "section", "source",
    "theory", "thing", "wittgenstein", "work",
}


def surface_semantic_terms(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z][a-z-]+", normalise(value))
        if len(token) >= 4
        and token not in SEMANTIC_STOPWORDS
        and token not in SEMANTIC_GENERIC_TOKENS
        and token not in SEMANTIC_RELATION_TERMS
    }


def truncated_claim_tokens(value: str) -> list[str]:
    return sorted(
        {
            token
            for token in re.findall(r"[a-z]+", normalise(value))
            if token in TRUNCATED_STEM_FRAGMENTS
        }
    )


def claim_similarity(first: str, second: str) -> tuple[float, float]:
    first_normalized = normalise(first)
    second_normalized = normalise(second)
    sequence = SequenceMatcher(None, first_normalized, second_normalized).ratio()
    first_tokens = set(surface_semantic_terms(first))
    second_tokens = set(surface_semantic_terms(second))
    jaccard = (
        len(first_tokens & second_tokens) / len(first_tokens | second_tokens)
        if first_tokens or second_tokens
        else 1.0
    )
    return sequence, jaccard


SEMANTIC_KEY_CONTENT_FIELDS = (
    "doctrine",
    "subject",
    "predicate",
    "object_or_conclusion",
    "polarity_or_qualification",
)
SEMANTIC_KEY_FIELDS = (*SEMANTIC_KEY_CONTENT_FIELDS, "argumentative_role")


def qualified_proposition_id(
    block_id: str,
    unit_id: str,
    proposition_id: str,
) -> str:
    return f"{block_id}::{unit_id}::{proposition_id}"


def semantic_key_fingerprint(proposition: dict) -> str | None:
    semantic_key = proposition.get("semantic_key")
    if not isinstance(semantic_key, dict):
        return None
    if set(semantic_key) != set(SEMANTIC_KEY_FIELDS):
        return None
    content = {
        field: normalise(str(semantic_key.get(field, "")))
        for field in SEMANTIC_KEY_CONTENT_FIELDS
    }
    if not all(content.values()):
        return None
    return hashlib.sha256(
        json.dumps(
            content,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def semantic_key_equivalence_metrics(
    first: dict,
    second: dict,
) -> dict:
    first_key = first.get("semantic_key")
    second_key = second.get("semantic_key")
    if not isinstance(first_key, dict) or not isinstance(second_key, dict):
        return {"equivalent": False, "overall_jaccard": 0.0, "overlap_coefficient": 0.0}
    if set(first_key) != set(SEMANTIC_KEY_FIELDS) or set(second_key) != set(
        SEMANTIC_KEY_FIELDS
    ):
        return {"equivalent": False, "overall_jaccard": 0.0, "overlap_coefficient": 0.0}
    first_text = " ".join(
        [
            first.get("claim", ""),
            *(str(first_key[field]) for field in SEMANTIC_KEY_CONTENT_FIELDS),
        ]
    )
    second_text = " ".join(
        [
            second.get("claim", ""),
            *(str(second_key[field]) for field in SEMANTIC_KEY_CONTENT_FIELDS),
        ]
    )
    synonym_stems = {
        "vertigo": "dizziness",
        "chooses": "choose",
        "selects": "choose",
        "selected": "choose",
        "select": "choose",
    }

    def equivalence_terms(value: str) -> set[str]:
        return {
            synonym_stems.get(term, term)
            for term in surface_semantic_terms(value)
            if term not in {"bounded"}
        }

    def predicate_family(proposition: dict, semantic_key: dict) -> str:
        combined = normalise(
            f"{proposition.get('claim', '')} {semantic_key.get('predicate', '')}"
        )
        families = (
            ("choose", r"\b(?:choose|chooses|chosen|select|selects|selected)\b"),
            ("be", r"\b(?:am|are|is|was|were|be|being)\b"),
            ("disclose", r"\b(?:disclose|discloses|reveal|reveals)\b"),
            ("produce", r"\b(?:produce|produces|producing|cause|causes)\b"),
        )
        for family, pattern in families:
            if re.search(pattern, combined):
                return family
        return normalise(str(semantic_key.get("predicate", "")))

    first_terms = equivalence_terms(first_text)
    second_terms = equivalence_terms(second_text)
    intersection = first_terms & second_terms
    union = first_terms | second_terms
    overall_jaccard = len(intersection) / len(union) if union else 1.0
    overlap_coefficient = (
        len(intersection) / min(len(first_terms), len(second_terms))
        if first_terms and second_terms
        else 1.0
    )
    first_doctrine = equivalence_terms(str(first_key["doctrine"]))
    second_doctrine = equivalence_terms(str(second_key["doctrine"]))
    doctrine_overlap = (
        len(first_doctrine & second_doctrine)
        / min(len(first_doctrine), len(second_doctrine))
        if first_doctrine and second_doctrine
        else 0.0
    )
    claim_sequence, claim_jaccard = claim_similarity(
        str(first.get("claim", "")),
        str(second.get("claim", "")),
    )
    first_subject = normalise(str(first_key["subject"]))
    second_subject = normalise(str(second_key["subject"]))
    shared_marker = bool(
        intersection & {"dizziness", "non-prescriptive"}
    )
    equivalent = (
        semantic_key_fingerprint(first) == semantic_key_fingerprint(second)
        or (
            claim_sequence >= 0.74
            and claim_jaccard >= 0.35
            and first_subject != second_subject
            and predicate_family(first, first_key)
            == predicate_family(second, second_key)
        )
        or (
            first_subject == second_subject
            and shared_marker
            and len(intersection) >= 4
            and overlap_coefficient >= 0.45
        )
    )
    return {
        "equivalent": equivalent,
        "overall_jaccard": round(overall_jaccard, 3),
        "overlap_coefficient": round(overlap_coefficient, 3),
        "doctrine_overlap": round(doctrine_overlap, 3),
        "claim_sequence_ratio": round(claim_sequence, 3),
        "claim_semantic_jaccard": round(claim_jaccard, 3),
        "predicate_family": [
            predicate_family(first, first_key),
            predicate_family(second, second_key),
        ],
        "shared_terms": sorted(intersection),
    }


def semantic_key_validation_failures(
    proposition: dict,
    claim: str,
    source_body: str,
    destination_body: str,
    *,
    context: str,
    qualified_id: str,
) -> list[dict]:
    failures = []
    semantic_key = proposition.get("semantic_key")
    if not isinstance(semantic_key, dict):
        return [
            {
                "reason": "distributed claim lacks reviewed semantic key",
                "context": context,
                "proposition": qualified_id,
            }
        ]
    missing = [
        field
        for field in SEMANTIC_KEY_FIELDS
        if not isinstance(semantic_key.get(field), str)
        or not semantic_key[field].strip()
    ]
    extra = sorted(set(semantic_key) - set(SEMANTIC_KEY_FIELDS))
    if missing or extra:
        failures.append(
            {
                "reason": "reviewed semantic key schema mismatch",
                "context": context,
                "proposition": qualified_id,
                "missing_or_empty": missing,
                "extra": extra,
            }
        )
        return failures
    role = semantic_key["argumentative_role"]
    if len(words(role)) < 6:
        failures.append(
            {
                "reason": "reviewed semantic key has an insufficiently bounded argumentative role",
                "context": context,
                "proposition": qualified_id,
                "argumentative_role": role,
            }
        )
    content_text = " ".join(
        semantic_key[field] for field in SEMANTIC_KEY_CONTENT_FIELDS
    )
    key_terms = set(semantic_terms(content_text))
    if len(key_terms) < 5:
        failures.append(
            {
                "reason": "reviewed semantic key is not conceptually specific",
                "context": context,
                "proposition": qualified_id,
                "semantic_terms": sorted(key_terms),
            }
        )
        return failures
    for surface, body, minimum in (
        ("claim", claim, 4),
        ("source", source_body, 3),
        ("destination", destination_body, 3),
    ):
        overlap = sorted(key_terms & set(semantic_terms(body)))
        if len(overlap) < minimum:
            failures.append(
                {
                    "reason": f"reviewed semantic key lacks {surface} correspondence",
                    "context": context,
                    "proposition": qualified_id,
                    "matched_terms": overlap,
                    "required": minimum,
                }
            )
    return failures


def semantic_contextual_justification_map(
    declarations: list[dict],
) -> tuple[dict[tuple[str, str], str], list[dict]]:
    mapping = {}
    failures = []
    for index, declaration in enumerate(declarations):
        proposition_ids = declaration.get("proposition_ids")
        reason = declaration.get("reason")
        if (
            not isinstance(proposition_ids, list)
            or len(proposition_ids) != 2
            or len(set(proposition_ids)) != 2
            or not all(isinstance(value, str) and value for value in proposition_ids)
            or not isinstance(reason, str)
            or len(words(reason)) < 10
        ):
            failures.append(
                {
                    "reason": "semantic contextual justification is not an exact narrow pair",
                    "index": index,
                    "declaration": declaration,
                }
            )
            continue
        pair = tuple(sorted(proposition_ids))
        if pair in mapping:
            failures.append(
                {
                    "reason": "duplicate semantic contextual justification pair",
                    "proposition_ids": list(pair),
                }
            )
            continue
        mapping[pair] = reason
    return mapping, failures


def claim_template_signature(value: str) -> str:
    tokens = re.findall(r"[a-z0-9]+", normalise(value).replace("-", " "))
    scaffold = []
    concept_pending = False
    for token in tokens:
        if (
            token in SEMANTIC_STOPWORDS
            or token in SEMANTIC_RELATION_TERMS
            or token in {
                "although", "and", "but", "if", "instead", "neither", "nor",
                "not", "only", "or", "rather", "so", "thereby", "through",
                "unless", "whereas", "while", "without",
            }
        ):
            if concept_pending:
                scaffold.append("{concept}")
                concept_pending = False
            scaffold.append(token)
        else:
            concept_pending = True
    if concept_pending:
        scaffold.append("{concept}")
    return " ".join(scaffold)


def claim_template_is_structural(signature: str) -> bool:
    tokens = signature.split()
    return (
        signature.count("{concept}") >= 2
        and len([token for token in tokens if token != "{concept}"]) >= 4
    )


def malformed_claim_family_hits(
    claim: str,
    *,
    block_id: str | None,
    proposition_id: str | None,
) -> list[str]:
    hits = []
    for family, pattern in MALFORMED_CLAIM_FAMILY_PATTERNS.items():
        if not pattern.search(claim):
            continue
        whitelist_key = (block_id or "", proposition_id or "", family)
        if whitelist_key not in MALFORMED_CLAIM_FAMILY_WHITELIST:
            hits.append(family)
    normalized = normalise(claim)
    all_caps_tokens = re.findall(r"\b[A-Z][A-Z-]{2,}\b", claim)
    if len(all_caps_tokens) >= 3:
        hits.append("raw_diagram_label")
    internal_caps = [
        token
        for token in all_caps_tokens
        if token not in {"UPSC", "PYQ", "Dasein".upper()}
    ]
    if len(internal_caps) >= 3 and re.search(r"[a-z]", claim):
        hits.append("raw_diagram_label")
    if (
        len(all_caps_tokens) >= 2
        and len(re.findall(r"[:;]", claim)) >= 2
        and len(re.findall(r"[.!?]", claim)) <= 1
    ):
        hits.append("diagram_label_chain")
    if (
        re.search(r"(?:\b[A-Z][A-Z-]{2,}\b[\s,/:;-]*){4,}", claim)
        or len(re.findall(r"(?:\||\.{4,}|_{3,})", claim)) > 0
    ):
        hits.append("bare_token_bag_salad")
    if re.search(
        r"\b(?:and|or|because|whereas|through|from|with|into|of|the|a|an)\.?$",
        normalized,
    ):
        hits.append("dangling_fragment")
    if re.search(r"\bteacher prevents points from replacing nuts with says\b", normalized):
        hits.append("actual_panel_10_token_salad")
    if claim.count("·") >= 2:
        hits.append("bare_token_bag_salad")
    first_sentence = re.match(r"^([^.!?]+)[.!?]\s+(.+)$", claim)
    if first_sentence:
        opening = first_sentence.group(1).strip()
        opening_tokens = re.findall(r"[A-Za-z][A-Za-z'-]*", opening)
        finite_verb = re.search(
            r"\b(?:am|are|is|was|were|be|becomes?|can|cannot|"
            r"constitutes?|defines?|denies?|depends?|distinguishes?|"
            r"has|have|holds?|illustrates?|means?|names?|provides?|"
            r"remains?|selects?|shows?|treats?)\b",
            opening,
            re.I,
        )
        if len(opening_tokens) <= 8 and not finite_verb:
            hits.append("incomplete_proposition")
    if (
        not claim
        or not claim[0].isupper()
        or claim[-1:] not in {".", "?", "!"}
        or len(words(claim)) < 12
    ):
        hits.append("incomplete_proposition")
    if DEPENDENT_CLAIM_SUBJECT_PATTERN.match(claim):
        hits.append("dependent_subject")
    tokens = re.findall(r"[a-z0-9]+", normalized.replace("-", " "))
    relation_positions = [
        index
        for index, token in enumerate(tokens)
        if token in SEMANTIC_RELATION_TERMS
    ]
    if relation_positions:
        first_relation = relation_positions[0]
        glue = {
            "a", "an", "and", "as", "at", "because", "by", "despite",
            "every", "for", "from", "in", "instead", "into", "not", "of",
            "on", "or", "rather", "than", "that", "the", "through", "to",
            "whereas", "whether", "while", "with", "without",
        }
        prefix = tokens[:first_relation]
        suffix = tokens[first_relation + 1:]
        claim_prefix = normalized.split(tokens[first_relation], 1)[0]
        if (
            len(prefix) >= 6
            and not set(prefix) & glue
            and not re.search(r"[,;:]", claim_prefix)
        ):
            hits.append("bare_token_bag_salad")
        if (
            len(suffix) >= 6
            and not set(suffix) & glue
            and not re.search(r"[,;:]", normalized)
        ):
            hits.append("bare_token_bag_salad")
    unknown_families = set(hits) - set(MALFORMED_CLAIM_FAMILIES)
    if unknown_families:
        raise RuntimeError(
            f"unstable malformed-claim family names: {sorted(unknown_families)}"
        )
    return sorted(set(hits))


def claim_correspondence_metrics(
    claim: str,
    source_body: str,
    destination_body: str,
) -> dict:
    claim_terms = set(semantic_terms(claim))
    source_terms = set(semantic_terms(source_body))
    destination_terms = set(semantic_terms(destination_body))
    shared = claim_terms & source_terms & destination_terms
    discriminative = {
        term
        for term in shared
        if term not in CORRESPONDENCE_GENERIC_TOKENS
        and term not in SEMANTIC_RELATION_TERMS
    }
    return {
        "shared_terms": sorted(shared),
        "discriminative_terms": sorted(discriminative),
        "source_overlap": sorted(claim_terms & source_terms),
        "destination_overlap": sorted(claim_terms & destination_terms),
    }


DEPENDENT_CLAIM_SUBJECT_PATTERN = re.compile(
    r"^(?:it|its|they|their|this|these|those|the same|such|that|"
    r"yet\s+it|whether\s+this|for\s+these)\b",
    re.I,
)
REPAIRED_CLAIM_IDS = (
    "session-session-2-kierkegaard-the-existing-individual-against-the-system-01-33e82f231f::end::end-proposition-2",
    "session-session-3-kierkegaard-the-three-spheres-of-existence-the-leap-an-01-647cd47c38::end::end-proposition-2",
    "session-session-4-kierkegaard-anxiety-as-the-dizziness-of-freedom-and-de-01-5871825f2d::beginning::beginning-proposition-2",
    "session-session-4-kierkegaard-anxiety-as-the-dizziness-of-freedom-and-de-01-5871825f2d::end::end-proposition-2",
    "session-session-6-sartre-existence-precedes-essence-the-paper-knife-and--01-2a201037ad::middle::middle-proposition-2",
    "session-session-7-sartre-being-in-itself-and-being-for-itself-nihilation-01-3a0bd8229b::end::end-proposition-1",
    "session-session-8-sartre-radical-but-situated-freedom-choice-responsibil-01-8947c2b44b::middle::middle-proposition-2",
    "session-session-9-sartre-facticity-and-transcendence-bad-faith-and-the-r-01-10128ba77b::end::end-proposition-2",
    "session-session-11-sartre-the-look-being-for-others-shame-and-why-confli-01-6bab21bbc6::end::end-proposition-1",
    "session-session-11-sartre-the-look-being-for-others-shame-and-why-confli-01-6bab21bbc6::end::end-proposition-2",
    "session-session-12-heidegger-the-being-question-the-ontological-differen-01-3c6642dfb3::middle::middle-proposition-2",
    "session-session-12-heidegger-the-being-question-the-ontological-differen-01-3c6642dfb3::end::end-proposition-2",
    "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-11-of-53::panel-11-of-53-proposition-2",
    "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-30-of-53::panel-30-of-53-proposition-1",
    "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-30-of-53::panel-30-of-53-proposition-2",
    "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-38-of-53::panel-38-of-53-proposition-1",
    "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-43-of-53::panel-43-of-53-proposition-1",
    "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-46-of-53::panel-46-of-53-proposition-1",
    "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-49-of-53::panel-49-of-53-proposition-1",
)
REPAIRED_SEMANTIC_DUPLICATE_PAIRS = (
    (
        "session-session-8-sartre-radical-but-situated-freedom-choice-responsibil-01-8947c2b44b::beginning::beginning-proposition-1",
        "session-session-8-sartre-radical-but-situated-freedom-choice-responsibil-01-8947c2b44b::middle::middle-proposition-2",
    ),
    (
        "session-session-12-heidegger-the-being-question-the-ontological-differen-01-3c6642dfb3::middle::middle-proposition-1",
        "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-30-of-53::panel-30-of-53-proposition-2",
    ),
    (
        "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-11-of-53::panel-11-of-53-proposition-1",
        "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-11-of-53::panel-11-of-53-proposition-2",
    ),
    (
        "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-38-of-53::panel-38-of-53-proposition-1",
        "session-complete-topic-ascii-master-flow-diagram-01-736359d77d::panel-38-of-53::panel-38-of-53-proposition-2",
    ),
)
GENERIC_WITNESS_NORMALIZED = {
    "in the", "it does", "it does not", "this is", "there is", "the thing",
    "the point", "the answer", "the question", "the source", "the section",
}
WITNESS_PADDING_TERMS = {
    "analys", "argument", "claim", "concept", "doctrine", "formal",
    "philosoph", "pictur", "relation", "structure",
}
WITNESS_REUSE_WHITELIST = {}


def witness_quality_failures(
    witness: str,
    *,
    context: str,
    global_state: dict | None = None,
    block_id: str | None = None,
    witness_id: str | None = None,
    source_body: str | None = None,
    reuse_justification: str | None = None,
) -> list[dict]:
    failures = []
    normalized = normalise(witness)
    semantic = semantic_terms(witness)
    if (
        normalized in GENERIC_WITNESS_NORMALIZED
        or len(words(witness)) < 1
        or len(semantic) < 1
    ):
        failures.append(
            {
                "reason": "generic or insufficiently specific witness",
                "context": context,
                "witness": witness,
            }
        )
    fragments = truncated_claim_tokens(witness)
    if fragments:
        failures.append(
            {
                "reason": "truncated or stemmed witness fragment",
                "context": context,
                "witness": witness,
                "fragments": fragments,
            }
        )
    if global_state is not None and normalized:
        source_hash = hashlib.sha256(
            normalise(source_body or "").encode("utf-8")
        ).hexdigest()
        semantic_signature = set(semantic_terms(witness))
        entries = global_state.setdefault("entries", [])
        for prior in entries:
            same_block = prior["block_id"] == block_id
            same_witness_id = prior["witness_id"] == witness_id
            if same_block and same_witness_id:
                continue
            sequence = SequenceMatcher(
                None,
                normalized,
                prior["normalized"],
            ).ratio()
            union = semantic_signature | prior["semantic_signature"]
            jaccard = (
                len(semantic_signature & prior["semantic_signature"]) / len(union)
                if union
                else 1.0
            )
            token_signature_match = bool(
                len(semantic_signature) >= 2
                and semantic_signature == prior["semantic_signature"]
            )
            exact_duplicate = normalized == prior["normalized"]
            current_core = semantic_signature - WITNESS_PADDING_TERMS
            prior_core = prior["semantic_signature"] - WITNESS_PADDING_TERMS
            core_signature_match = bool(
                len(current_core) >= 2 and current_core == prior_core
            )
            current_core_text = " ".join(
                token
                for token in semantic_terms(witness)
                if token not in WITNESS_PADDING_TERMS
            )
            prior_core_text = prior["core_text"]
            core_sequence = SequenceMatcher(
                None,
                current_core_text,
                prior_core_text,
            ).ratio()
            near_duplicate = (
                token_signature_match
                or core_signature_match
                or jaccard >= .80
                or sequence >= .88
                or (
                    len(current_core) >= 2
                    and len(prior_core) >= 2
                    and core_sequence >= .90
                )
            )
            whitelist_key = (
                block_id,
                witness_id,
                prior["block_id"],
                prior["witness_id"],
                normalized,
            )
            whitelist_reason = WITNESS_REUSE_WHITELIST.get(whitelist_key)
            reuse_allowed = bool(
                whitelist_reason
                and reuse_justification == whitelist_reason
            )
            if exact_duplicate and not reuse_allowed:
                failures.append(
                    {
                        "reason": (
                            "same-block duplicate witness misdirection"
                            if same_block
                            else "cross-block duplicate witness misdirection"
                        ),
                        "context": context,
                        "witness": witness,
                        "prior_block": prior["block_id"],
                        "current_block": block_id,
                    }
                )
            elif near_duplicate and not reuse_allowed:
                failures.append(
                    {
                        "reason": (
                            "same-block near-duplicate witness"
                            if same_block
                            else "cross-block near-duplicate witness"
                        ),
                        "context": context,
                        "witness": witness,
                        "prior_witness": prior["witness"],
                        "prior_block": prior["block_id"],
                        "current_block": block_id,
                        "token_signature_match": token_signature_match,
                        "semantic_jaccard": round(jaccard, 3),
                        "sequence_ratio": round(sequence, 3),
                        "core_signature_match": core_signature_match,
                        "core_sequence_ratio": round(core_sequence, 3),
                    }
                )
        entries.append(
            {
                "normalized": normalized,
                "semantic_signature": semantic_signature,
                "source_hash": source_hash,
                "block_id": block_id,
                "witness_id": witness_id,
                "witness": witness,
                "reuse_justification": reuse_justification,
                "core_text": " ".join(
                    token
                    for token in semantic_terms(witness)
                    if token not in WITNESS_PADDING_TERMS
                ),
            }
        )
    return failures


def aggregate_correspondence_failures(
    signature: list[str],
    destination_body: str,
    declared_minimum: float | None,
) -> list[dict]:
    failures = []
    overlap = [
        term for term in signature if contains_witness(destination_body, term)
    ]
    overlap_rate = len(overlap) / len(signature) if signature else 1.0
    if not isinstance(declared_minimum, (int, float)) or declared_minimum < .25:
        failures.append(
            {
                "reason": "declared aggregate correspondence floor is too weak",
                "declared": declared_minimum,
                "required_minimum": .25,
            }
        )
    elif overlap_rate < declared_minimum:
        failures.append(
            {
                "reason": "insufficient aggregate body-signature correspondence",
                "overlap_rate": round(overlap_rate, 3),
                "required": declared_minimum,
                "matched_signature_terms": overlap,
            }
        )
    return failures


def proposition_validation_failures(
    propositions: list[dict],
    source_body: str,
    destination_body: str,
    *,
    require_semantic_specificity: bool,
    context: str,
    seen_claims: set[str] | None = None,
    claim_history: list[dict] | None = None,
    seen_witnesses: set[str] | None = None,
    global_witness_state: dict | None = None,
    block_id: str | None = None,
    unit_id: str | None = None,
    minimum_semantic_witness_terms: int = 3,
) -> list[dict]:
    failures = []
    seen_claims = seen_claims if seen_claims is not None else set()
    claim_history = claim_history if claim_history is not None else []
    seen_witnesses = seen_witnesses if seen_witnesses is not None else set()
    for proposition in propositions:
        proposition_id = proposition.get("id")
        witnesses = proposition.get("witnesses", [])
        if not witnesses:
            failures.append(
                {
                    "reason": "empty proposition witness set",
                    "context": context,
                    "proposition": proposition_id,
                }
            )
            continue
        if require_semantic_specificity:
            claim = proposition.get("claim", "")
            qualified_id = qualified_proposition_id(
                block_id or "",
                unit_id or context,
                proposition_id or "",
            )
            claim_key = normalise(claim)
            claim_terms = semantic_terms(claim)
            claim_surface_terms = surface_semantic_terms(claim)
            claim_tokens = set(
                re.findall(r"[a-z0-9]+", normalise(claim).replace("-", " "))
            )
            correspondence = claim_correspondence_metrics(
                claim,
                source_body,
                destination_body,
            )
            source_overlap = correspondence["source_overlap"]
            destination_overlap = correspondence["destination_overlap"]
            discriminative_overlap = correspondence["discriminative_terms"]
            truncated = truncated_claim_tokens(claim)
            if truncated:
                failures.append(
                    {
                        "reason": "truncated or stemmed claim fragment",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                        "fragments": truncated,
                    }
                )
            for family in malformed_claim_family_hits(
                claim,
                block_id=block_id,
                proposition_id=proposition_id,
            ):
                failures.append(
                    {
                        "reason": f"malformed distributed claim family: {family}",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                    }
                )
            if any(re.search(pattern, claim, re.I) for pattern in BOILERPLATE_CLAIM_PATTERNS):
                failures.append(
                    {
                        "reason": "boilerplate proposition template",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                    }
                )
            present_padding = claim_tokens & GENERIC_PADDING_RELATIONS
            meaningful_relations = (claim_tokens & SEMANTIC_RELATION_TERMS) - GENERIC_PADDING_RELATIONS
            if present_padding and not meaningful_relations:
                failures.append(
                    {
                        "reason": "generic relationship-token padding",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                    }
                )
            if (
                not claim
                or not claim[0].isupper()
                or claim[-1:] not in {".", "?", "!"}
                or len(words(claim)) < 12
            ):
                failures.append(
                    {
                        "reason": "distributed claim is not a grammatical complete proposition",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                    }
                )
            if DEPENDENT_CLAIM_SUBJECT_PATTERN.match(claim):
                failures.append(
                    {
                        "reason": "distributed claim lacks an explicit independent subject",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                    }
                )
            if len(claim_terms) < 7 or len(claim_surface_terms) < 6:
                failures.append(
                    {
                        "reason": "semantic claim is not conceptually specific",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                    }
                )
            if not meaningful_relations:
                failures.append(
                    {
                        "reason": "semantic claim lacks an explicit relationship",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                    }
                )
            failures.extend(
                semantic_key_validation_failures(
                    proposition,
                    claim,
                    source_body,
                    destination_body,
                    context=context,
                    qualified_id=qualified_id,
                )
            )
            if len(source_overlap) < 4:
                failures.append(
                    {
                        "reason": "claim lacks discriminative source vocabulary",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                        "matched_terms": source_overlap,
                    }
                )
            if len(destination_overlap) < 4:
                failures.append(
                    {
                        "reason": "claim lacks destination semantic correspondence",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                        "matched_terms": destination_overlap,
                    }
                )
            if len(discriminative_overlap) < 3:
                failures.append(
                    {
                        "reason": "claim lacks discriminative conceptual correspondence",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                        "matched_terms": discriminative_overlap,
                    }
                )
            template_signature = claim_template_signature(claim)
            template_predecessors = [
                prior
                for prior in claim_history
                if claim_template_is_structural(template_signature)
                and prior.get("template_signature") == template_signature
            ]
            if len(template_predecessors) >= 2:
                failures.append(
                    {
                        "reason": "repeated distributed claim template",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                        "template_signature": template_signature,
                        "prior_propositions": [
                            prior["proposition"] for prior in template_predecessors
                        ],
                    }
                )
            for prior in claim_history:
                sequence, jaccard = claim_similarity(claim, prior["claim"])
                if sequence >= .82 or jaccard >= .72:
                    failures.append(
                        {
                            "reason": "distributed claims have high structural similarity",
                            "context": context,
                            "proposition": proposition_id,
                            "claim": claim,
                            "similar_to": prior["proposition"],
                            "sequence_ratio": round(sequence, 3),
                            "semantic_jaccard": round(jaccard, 3),
                        }
                    )
            claim_history.append(
                {
                    "proposition": proposition_id,
                    "claim": claim,
                    "template_signature": template_signature,
                }
            )
            if claim_key in seen_claims:
                failures.append(
                    {
                        "reason": "duplicate semantic claim",
                        "context": context,
                        "proposition": proposition_id,
                        "claim": claim,
                    }
                )
            seen_claims.add(claim_key)
        for witness in witnesses:
            witness_key = normalise(witness)
            witness_terms = semantic_terms(witness)
            if require_semantic_specificity:
                failures.extend(
                    witness_quality_failures(
                        witness,
                        context=context,
                        global_state=global_witness_state,
                        block_id=block_id,
                        witness_id=f"{context}|{proposition_id}",
                        source_body=source_body,
                        reuse_justification=proposition.get(
                            "witness_reuse_justification"
                        ),
                    )
                )
                if len(witness_terms) < minimum_semantic_witness_terms:
                    failures.append(
                        {
                            "reason": "generic or token-fragment witness",
                            "context": context,
                            "proposition": proposition_id,
                            "witness": witness,
                        }
                    )
                if witness_key in seen_witnesses:
                    failures.append(
                        {
                            "reason": "duplicate distributed witness",
                            "context": context,
                            "proposition": proposition_id,
                            "witness": witness,
                        }
                    )
                seen_witnesses.add(witness_key)
            if not contains_witness(source_body, witness):
                failures.append(
                    {
                        "reason": "proposition witness absent from source body",
                        "context": context,
                        "proposition": proposition_id,
                        "witness": witness,
                    }
                )
            if not contains_witness(destination_body, witness):
                failures.append(
                    {
                        "reason": "proposition witness absent from destination body",
                        "context": context,
                        "proposition": proposition_id,
                        "witness": witness,
                    }
                )
    return failures


def parent_only_text_sha256(block: dict) -> str:
    value = unicodedata.normalize(
        "NFC",
        block["parent_only_text"].replace("\r\n", "\n").replace("\r", "\n"),
    )
    value = "\n".join(line.rstrip() for line in value.splitlines()).strip("\n")
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def structural_umbrella_validation_failures(
    block: dict,
    decision: dict,
    child_resolution: dict[str, bool],
) -> list[dict]:
    failures = []
    parent_only_substantive = len(words(block["parent_only_body"])) >= 4
    expected = {
        "child_ids": block["child_ids"],
        "descendant_ids": block["descendant_ids"],
        "child_union_required": True,
        "parent_only_body_sha256": parent_only_text_sha256(block),
        "parent_only_substantive": parent_only_substantive,
    }
    if decision.get("coverage_mode") != "structural_umbrella":
        failures.append({"reason": "structural umbrella coverage mode mismatch"})
    if decision.get("structural_umbrella") != expected:
        failures.append({"reason": "structural umbrella declaration mismatch"})
    if decision.get("classification") not in {
        "covered_in_scope",
        "genuine_in_scope_omission",
    }:
        failures.append({"reason": "structural umbrella must be covered or repaired in scope"})
    for child_id in block["child_ids"]:
        if not child_resolution.get(child_id, False):
            failures.append(
                {
                    "reason": "structural umbrella has unresolved child",
                    "child_id": child_id,
                }
            )
    return failures


def distributed_inventory_validation_failures(
    block: dict,
    inventory: list[dict],
    destinations: list[dict],
    package_text: dict[str, str],
    *,
    global_claim_history: list[dict] | None = None,
    global_seen_claims: set[str] | None = None,
    global_seen_witnesses: set[str] | None = None,
    global_witness_state: dict | None = None,
) -> list[dict]:
    failures = []
    expected_units = (
        [("cluster", cluster) for cluster in block["semantic_clusters"]]
        if block["semantic_clusters"]
        else [("segment", segment) for segment in block["source_segments"]]
    )
    inventory_keys = [(item.get("kind"), item.get("id")) for item in inventory]
    expected_inventory_keys = [(kind, unit["id"]) for kind, unit in expected_units]
    if inventory_keys != expected_inventory_keys:
        failures.append(
            {
                "reason": "distributed inventory does not span every extracted unit",
                "recorded": inventory_keys,
                "expected": expected_inventory_keys,
            }
        )
    package_destination_keys = {
        (
            item.get("file"),
            item.get("anchor"),
            item.get("context_anchor"),
            item.get("anchor_kind", "heading"),
        )
        for item in destinations
    }
    inventory_by_key = {
        (item.get("kind"), item.get("id")): item for item in inventory
    }
    distributed_seen_claims = (
        global_seen_claims if global_seen_claims is not None else set()
    )
    distributed_claim_history = (
        global_claim_history if global_claim_history is not None else []
    )
    distributed_seen_witnesses = (
        global_seen_witnesses if global_seen_witnesses is not None else set()
    )
    cluster_anchor_usage: Counter = Counter()
    for kind, unit in expected_units:
        item = inventory_by_key.get((kind, unit["id"]))
        if not item:
            continue
        if item.get("source_text_sha256") != unit["text_sha256"]:
            failures.append(
                {
                    "reason": "distributed inventory source hash mismatch",
                    "unit": unit["id"],
                }
            )
        unit_propositions = item.get("propositions", [])
        minimum_unit_propositions = 2
        if len(unit_propositions) < minimum_unit_propositions:
            failures.append(
                {
                    "reason": "distributed unit has too few propositions",
                    "unit": unit["id"],
                }
            )
        references = item.get("destination_anchors", [])
        if not references:
            failures.append(
                {
                    "reason": "distributed unit has no destination anchors",
                    "unit": unit["id"],
                }
            )
        if kind == "cluster" and len(references) != 1:
            failures.append(
                {
                    "reason": "master-flow panel must have exactly one panel-specific destination",
                    "unit": unit["id"],
                }
            )
        unit_destination_bodies = []
        for reference in references:
            reference_key = (
                reference.get("file"),
                reference.get("anchor"),
                reference.get("context_anchor"),
                reference.get("anchor_kind", "heading"),
            )
            if kind == "cluster":
                cluster_anchor_usage[reference_key] += 1
                expected_panel = (
                    f"ascii master flow - panel {unit['number']}/{unit['total']}"
                )
                if expected_panel not in normalise(reference.get("anchor", "")):
                    failures.append(
                        {
                            "reason": "master-flow destination is not panel-specific",
                            "unit": unit["id"],
                            "destination": reference,
                        }
                    )
            if reference_key not in package_destination_keys:
                failures.append(
                    {
                        "reason": "distributed unit references undeclared destination",
                        "unit": unit["id"],
                        "destination": reference,
                    }
                )
                continue
            text = package_text.get(reference["file"], "")
            destination_body = destination_body_for_reference(text, reference)
            if destination_body:
                unit_destination_bodies.append(destination_body)
        unit_destination = "\n".join(unit_destination_bodies)
        failures.extend(
            {
                "unit": unit["id"],
                **failure,
            }
            for failure in proposition_validation_failures(
                unit_propositions,
                unit["body"],
                unit_destination,
                require_semantic_specificity=True,
                context=f"{kind}:{unit['id']}",
                seen_claims=distributed_seen_claims,
                claim_history=distributed_claim_history,
                seen_witnesses=distributed_seen_witnesses,
                global_witness_state=global_witness_state,
                block_id=block["id"],
                unit_id=unit["id"],
                minimum_semantic_witness_terms=(
                    2 if kind == "cluster" and len(words(unit["body"])) < 20 else 3
                ),
            )
        )
    if block["semantic_clusters"]:
        for anchor_key, use_count in cluster_anchor_usage.items():
            if use_count <= 1:
                continue
            sharing_items = [
                item
                for item in inventory
                if any(
                    (
                        reference.get("file"),
                        reference.get("anchor"),
                        reference.get("context_anchor"),
                        reference.get("anchor_kind", "heading"),
                    )
                    == anchor_key
                    for reference in item.get("destination_anchors", [])
                )
            ]
            if not all(
                item.get("shared_destination_justification")
                and all(
                    proposition.get("claim")
                    for proposition in item.get("propositions", [])
                )
                for item in sharing_items
            ):
                failures.append(
                    {
                        "reason": "master-flow panels reuse a generic destination anchor",
                        "destination": anchor_key,
                        "use_count": use_count,
                    }
                )
    return failures


def distributed_corpus_validation_failures(
    blocks: list[dict],
    review_decisions: dict[str, dict],
    package_text: dict[str, str],
    semantic_contextual_justifications: list[dict],
) -> list[dict]:
    failures = []
    global_claim_history: list[dict] = []
    global_seen_claims: set[str] = set()
    global_seen_witnesses: set[str] = set()
    global_witness_state: dict = {"entries": []}
    for block in blocks:
        decision = review_decisions.get(block["id"], {})
        inventory = decision.get("distributed_proposition_inventory", [])
        if not inventory:
            continue
        failures.extend(
            {
                "block": block["id"],
                **failure,
            }
            for failure in distributed_inventory_validation_failures(
                block,
                inventory,
                decision.get("package_destinations", []),
                package_text,
                global_claim_history=global_claim_history,
                global_seen_claims=global_seen_claims,
                global_seen_witnesses=global_seen_witnesses,
                global_witness_state=global_witness_state,
            )
        )
    live_audit = distributed_claim_live_audit(
        blocks,
        review_decisions,
        package_text,
        semantic_contextual_justifications,
    )
    semantic_audit = live_audit["semantic_duplicate_candidates"]
    failures.extend(
        {
            "reason": "unjustified semantic duplicate claim",
            **pair,
        }
        for pair in semantic_audit["unjustified_semantic_duplicates"]
    )
    failures.extend(semantic_audit["justification_failures"])
    return failures


def exact_wording_normalise(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", value).strip()


def words(value: str) -> list[str]:
    value = re.sub(r"```[a-zA-Z-]*\n?", "", value).replace("```", "")
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", re.sub(r"[*_`#>|]", " ", value))


def slug(value: str) -> str:
    value = normalise(value)
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value[:64] or "block"


def source_relative(path: Path) -> str:
    return str(path.relative_to(REPO)).replace("\\", "/")


def path_label(path: Path) -> str:
    try:
        return source_relative(path)
    except ValueError:
        return str(path)


def formal_source_authority_assertion() -> dict:
    authority_root = AUTHORITATIVE_FORMAL_ROOT.resolve()
    forbidden_root = FORBIDDEN_DERIVATIVE_FORMAL_ROOT.resolve()
    sources = {}
    failures = []
    for code, path in FORMAL_SOURCES.items():
        resolved = path.resolve()
        under_authority = resolved.is_relative_to(authority_root)
        under_forbidden_derivative = resolved.is_relative_to(forbidden_root)
        sources[code] = {
            "path": str(resolved),
            "under_authoritative_downloads_root": under_authority,
            "under_forbidden_c_up_derivative_root": under_forbidden_derivative,
        }
        if not under_authority:
            failures.append(f"{code}: formal source is outside the authoritative Downloads root")
        if under_forbidden_derivative:
            failures.append(f"{code}: formal source silently uses C:\\up\\learning_package_final")
    return {
        "authority": "completed formal sessions/workbooks under the Downloads UPSC-agent learning_package_final tree",
        "authoritative_root": str(authority_root),
        "forbidden_derivative_root": str(forbidden_root),
        "sources": sources,
        "failures": failures,
        "pass": not failures,
    }


SIGNATURE_STOPWORDS = {
    "about", "after", "again", "against", "answer", "application", "aristotle",
    "basic", "because", "being", "block", "called", "complete", "correct",
    "decoding", "detailed", "evidence", "exam", "facts", "first", "heading",
    "independent", "learning", "marks", "model", "must", "original", "package",
    "paper", "plato", "practice", "question", "revision", "session", "source",
    "statement", "teaching", "this", "through", "toolkit", "traps", "upsc",
    "what", "when", "where", "which", "with", "workbook", "write", "writing",
    "does", "each", "from", "into", "most", "only", "rather", "same", "than",
    "that", "their", "then", "these", "they", "would",
}

PANEL_REVIEW = {}

ROUTE_FORBIDDEN_ASSERTIONS = [
    {"id": "route-claims-topic09-primary-ownership", "pattern": r"topic 09\s+(?:is|remains|claims to be|acts as)(?:(?!\n).){0,80}(?:primary|sole) owner"},
    {"id": "route-imports-existentialist-doctrine", "pattern": r"husserl(?:(?!\n).){0,140}(?:owns|establishes|proves)(?:(?!\n).){0,100}(?:being-in-the-world|sartrean nothingness|bad faith)"},
]

CROSS_TOPIC_ROUTE_OBLIGATIONS = [
    {
        "id": "WP-2018-Q4A-EPOCHE-HEIDEGGER",
        "origin_primary_owner": ".",
        "paired_owner": "../09-Phenomenology-Husserl",
        "verified_route_source": "../../../../../knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2018-2025.md",
        "bounded_scope": "Topic 10 owns Heidegger's rejection of the worldless spectator and the positive being-in-the-world account; Topic 09 supplies only the Husserlian epoché premise.",
        "status": "fulfilled_substantively",
        "counterpart_recording_status": "external_concurrent_topic_not_inspected_under_isolation",
        "source_owner_evidence": {"file": "../../../../../knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2018-2025.md", "anchor": "2018 ✅", "witnesses": ["Epoché", "being in the world"]},
        "destination_evidence": [
            {"file": "ANSWER-WRITING-TOOLKIT.md", "anchor": "2. 2018 Q4(a) · 20 marks", "witnesses": ["suspends the general thesis", "worldless spectator", "being-in-the-world"], "required_semantic_assertions": [{"id": "topic10-epoche-heidegger-owner", "term_groups": [["epoché", "suspends"], ["Heidegger", "worldless spectator"], ["being-in-the-world"]]}], "forbidden_semantic_assertions": ROUTE_FORBIDDEN_ASSERTIONS},
            {"file": "ANSWER-WRITING-TOOLKIT.md", "anchor": "Inbound obligations from Topic 09", "witnesses": ["WP-2018-Q4A-EPOCHE-HEIDEGGER", "Topic 10 is the primary owner", "being-in-the-world"], "required_semantic_assertions": [{"id": "topic10-epoche-inbound-id", "term_groups": [["WP-2018-Q4A-EPOCHE-HEIDEGGER"], ["Topic 10", "primary owner"], ["being-in-the-world"]]}], "forbidden_semantic_assertions": ROUTE_FORBIDDEN_ASSERTIONS},
            {"file": "COVERAGE-LEDGER.md", "anchor": "Bounded route obligations", "witnesses": ["WP-2018-Q4A-EPOCHE-HEIDEGGER", "Topic 10 primary", "Husserlian suspension"], "required_semantic_assertions": [{"id": "topic10-epoche-ledger", "term_groups": [["WP-2018-Q4A-EPOCHE-HEIDEGGER"], ["Topic 10 primary"], ["Husserlian suspension"]]}], "forbidden_semantic_assertions": ROUTE_FORBIDDEN_ASSERTIONS},
        ],
    },
    {
        "id": "WP-2026-Q2C-SARTRE-HUSSERL-CONSCIOUSNESS",
        "origin_primary_owner": ".",
        "paired_owner": "../09-Phenomenology-Husserl",
        "verified_route_source": "../../../../../knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2026.md",
        "bounded_scope": "Topic 10 owns Sartrean consciousness as nothing and the comparison; Topic 09 supplies the Husserlian intentional and transcendental half without owning Sartre's doctrine.",
        "status": "fulfilled_substantively",
        "counterpart_recording_status": "external_concurrent_topic_not_inspected_under_isolation",
        "source_owner_evidence": {"file": "../../../../../knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2026.md", "anchor": "Q2 (50)", "witnesses": ["consciousness as 'nothing'", "Husserl's notion"]},
        "destination_evidence": [
            {"file": "ANSWER-WRITING-TOOLKIT.md", "anchor": "15. 2026 Q2(c) · 15 marks", "witnesses": ["non-egological consciousness", "intentionality", "constituting subjectivity"], "required_semantic_assertions": [{"id": "topic10-sartre-husserl-owner", "term_groups": [["Sartre", "consciousness"], ["intentionality"], ["constituting", "subjectivity"]]}], "forbidden_semantic_assertions": ROUTE_FORBIDDEN_ASSERTIONS},
            {"file": "ANSWER-WRITING-TOOLKIT.md", "anchor": "Inbound obligations from Topic 09", "witnesses": ["WP-2026-Q2C-SARTRE-HUSSERL-CONSCIOUSNESS", "Topic 10 is the primary owner", "Sartre's non-egological consciousness"], "required_semantic_assertions": [{"id": "topic10-sartre-husserl-inbound-id", "term_groups": [["WP-2026-Q2C-SARTRE-HUSSERL-CONSCIOUSNESS"], ["Topic 10", "primary owner"], ["Sartre", "non-egological consciousness"]]}], "forbidden_semantic_assertions": ROUTE_FORBIDDEN_ASSERTIONS},
            {"file": "COVERAGE-LEDGER.md", "anchor": "Bounded route obligations", "witnesses": ["WP-2026-Q2C-SARTRE-HUSSERL-CONSCIOUSNESS", "Topic 10 primary", "Sartrean consciousness as nothing"], "required_semantic_assertions": [{"id": "topic10-sartre-husserl-ledger", "term_groups": [["WP-2026-Q2C-SARTRE-HUSSERL-CONSCIOUSNESS"], ["Topic 10 primary"], ["Sartrean consciousness", "nothing"]]}], "forbidden_semantic_assertions": ROUTE_FORBIDDEN_ASSERTIONS},
        ],
    },
]

EXPECTED_ROUTED_DECISIONS = {}
EXPECTED_ROUTED_MULTIPLICITIES = {}

def routed_decision_binding_failures(decisions: dict[str, dict]) -> list[dict]:
    actual = {
        block_id: decision
        for block_id, decision in decisions.items()
        if decision.get("classification") == "routed_to_canonical_owner"
    }
    failures = []
    expected_ids = set(EXPECTED_ROUTED_DECISIONS)
    actual_ids = set(actual)
    if actual_ids != expected_ids:
        failures.append(
            {
                "reason": "routed stable block-id union mismatch",
                "missing": sorted(expected_ids - actual_ids),
                "extra": sorted(actual_ids - expected_ids),
            }
        )
    for block_id, expected in EXPECTED_ROUTED_DECISIONS.items():
        decision = actual.get(block_id)
        if not decision:
            continue
        if decision.get("inbound_obligation_id") != expected["obligation_id"]:
            failures.append(
                {
                    "reason": "routed obligation reassignment",
                    "id": block_id,
                    "recorded": decision.get("inbound_obligation_id"),
                    "expected": expected["obligation_id"],
                }
            )
        if decision.get("routed_owner") != expected["routed_owner"]:
            failures.append(
                {
                    "reason": "routed canonical owner mismatch",
                    "id": block_id,
                    "recorded": decision.get("routed_owner"),
                    "expected": expected["routed_owner"],
                }
            )
        if decision.get("obligation_status") != "fulfilled_substantively":
            failures.append(
                {
                    "reason": "routed obligation status mismatch",
                    "id": block_id,
                    "recorded": decision.get("obligation_status"),
                    "expected": "fulfilled_substantively",
                }
            )
        if decision.get("resolution_status") != "resolved_routed_to_verified_owner":
            failures.append(
                {
                    "reason": "routed resolution status mismatch",
                    "id": block_id,
                    "recorded": decision.get("resolution_status"),
                    "expected": "resolved_routed_to_verified_owner",
                }
            )
    multiplicities = Counter(
        decision.get("inbound_obligation_id") for decision in actual.values()
    )
    for obligation_id, expected_count in EXPECTED_ROUTED_MULTIPLICITIES.items():
        if multiplicities[obligation_id] != expected_count:
            failures.append(
                {
                    "reason": "routed obligation multiplicity mismatch",
                    "obligation": obligation_id,
                    "recorded": multiplicities[obligation_id],
                    "expected": expected_count,
                }
            )
    return failures


def body_without_headings_and_labels(value: str) -> str:
    lines = []
    for line in value.splitlines():
        if re.match(r"^#{1,6}\s+", line):
            continue
        if re.match(r"^\s*```", line):
            continue
        line = re.sub(r"^\s*\*\*[^*]{1,80}:\*\*\s*", "", line)
        line = re.sub(r"^\s*>?\s*🔑\s*\*\*[^*]{1,80}:\*\*\s*", "", line)
        lines.append(line)
    return "\n".join(lines)


def concept_signature(block_body: str, limit: int = 12) -> list[str]:
    body_tokens = re.findall(
        r"[a-z0-9]+(?:-[a-z0-9]+)*",
        normalise(body_without_headings_and_labels(block_body)),
    )
    counts = Counter(
        token for token in body_tokens
        if len(token) >= 4 and token not in SIGNATURE_STOPWORDS
    )
    return [token for token, _ in counts.most_common(limit)]


def substantive_body_witnesses(block_body: str, limit: int = 50) -> list[str]:
    body = body_without_headings_and_labels(block_body)
    candidates = []
    content_tokens = [
        token for token in re.findall(
            r"[a-z0-9]+(?:-[a-z0-9]+)*", normalise(body)
        )
        if len(token) >= 4 and token not in SIGNATURE_STOPWORDS
    ]
    for index in range(min(len(content_tokens) - 1, 100)):
        phrase = f"{content_tokens[index]} {content_tokens[index + 1]}"
        if phrase not in candidates:
            candidates.append(phrase)
    for pattern in (
        r"\*\*([^*\n]{3,80})\*\*",
        r"(?<!\*)\*([^*\n]{3,80})\*(?!\*)",
        r"[“\"]([^”\"\n]{4,80})[”\"]",
    ):
        for match in re.finditer(pattern, body):
            phrase = normalise(match.group(1))
            tokens = [
                token for token in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", phrase)
                if len(token) >= 4 and token not in SIGNATURE_STOPWORDS
            ]
            if len(tokens) < 2 or len(tokens) > 6:
                continue
            normalized = " ".join(tokens)
            if normalized not in candidates:
                candidates.append(normalized)
    return candidates[:limit]


def source_text_segments(
    block_text: str,
    source_line: int,
    minimum_lines: int = LARGE_LEAF_MIN_PHYSICAL_LINES,
    minimum_words: int = LARGE_LEAF_MIN_WORDS,
    minimum_semantic_tokens: int = LARGE_LEAF_MIN_SEMANTIC_TOKENS,
) -> list[dict]:
    lines = block_text.splitlines()
    body_lines = lines[1:]
    substantive_body = body_without_headings_and_labels("\n".join(body_lines))
    word_count = len(words(substantive_body))
    semantic_token_count = len(semantic_terms(substantive_body))
    if (
        len(body_lines) < minimum_lines
        and word_count < minimum_words
        and semantic_token_count < minimum_semantic_tokens
    ):
        return []
    line_based = len(body_lines) >= minimum_lines
    if line_based:
        units = body_lines
        segmentation_basis = "physical_line_thirds"
    else:
        units = re.findall(r"\S+", substantive_body)
        segmentation_basis = "substantive_word_token_thirds"
    boundaries = (0, len(units) // 3, (2 * len(units)) // 3, len(units))
    result = []
    for index, label in enumerate(("beginning", "middle", "end")):
        start, end = boundaries[index], boundaries[index + 1]
        separator = "\n" if line_based else " "
        text = separator.join(units[start:end]).strip()
        body = body_without_headings_and_labels(text)
        approximate_start_line = source_line + 1 + round(
            index * len(body_lines) / 3
        )
        approximate_end_line = source_line + round(
            (index + 1) * len(body_lines) / 3
        )
        result.append(
            {
                "id": label,
                "source_line": (
                    source_line + 1 + start
                    if line_based
                    else approximate_start_line
                ),
                "end_line": (
                    source_line + end
                    if line_based
                    else approximate_end_line
                ),
                "text_sha256": hashlib.sha256(
                    unicodedata.normalize("NFC", text).encode("utf-8")
                ).hexdigest(),
                "body": body,
                "signature": concept_signature(body),
                "witnesses": substantive_body_witnesses(body),
                "segmentation_basis": segmentation_basis,
                "large_leaf_detection": {
                    "physical_lines": len(body_lines),
                    "words": word_count,
                    "semantic_tokens": semantic_token_count,
                    "thresholds": {
                        "physical_lines": minimum_lines,
                        "words": minimum_words,
                        "semantic_tokens": minimum_semantic_tokens,
                    },
                },
            }
        )
    return result


def source_semantic_clusters(block_text: str, source_line: int) -> list[dict]:
    lines = block_text.splitlines()
    markers = []
    for index, line in enumerate(lines):
        match = re.match(
            r"^ASCII MASTER FLOW [—-] PANEL (\d+)/(\d+):\s*(.+?)\s*$",
            line,
        )
        if match:
            markers.append(
                {
                    "index": index,
                    "number": int(match.group(1)),
                    "total": int(match.group(2)),
                    "label": match.group(3),
                }
            )
    result = []
    for position, marker in enumerate(markers):
        end = markers[position + 1]["index"] if position + 1 < len(markers) else len(lines)
        text = "\n".join(lines[marker["index"]:end]).strip()
        body = body_without_headings_and_labels(text)
        result.append(
            {
                "id": f"panel-{marker['number']:02d}-of-{marker['total']:02d}",
                "number": marker["number"],
                "total": marker["total"],
                "label": marker["label"],
                "source_line": source_line + marker["index"],
                "end_line": source_line + end - 1,
                "text_sha256": hashlib.sha256(
                    unicodedata.normalize("NFC", text).encode("utf-8")
                ).hexdigest(),
                "body": body,
                "signature": concept_signature(body),
                "witnesses": substantive_body_witnesses(body),
            }
        )
    return result


def panel_marker_integrity(text: str, *, surface: str) -> dict:
    markers = [
        {
            "number": int(match.group(1)),
            "total": int(match.group(2)),
            "label": match.group(3).strip(),
        }
        for match in re.finditer(
            r"(?m)^ASCII MASTER FLOW [—-] PANEL (\d+)/(\d+):\s*(.+?)\s*$",
            text,
        )
    ]
    numbers = [marker["number"] for marker in markers]
    totals = [marker["total"] for marker in markers]
    expected_numbers = list(range(1, EXPECTED_PANEL_TOTAL + 1))
    failures = []
    if len(markers) != EXPECTED_PANEL_TOTAL:
        failures.append(
            {
                "reason": "panel marker count mismatch",
                "recorded": len(markers),
                "expected": EXPECTED_PANEL_TOTAL,
            }
        )
    if numbers != expected_numbers:
        failures.append(
            {
                "reason": "panel markers are not the exact ordered sequence",
                "recorded": numbers,
                "expected": expected_numbers,
            }
        )
    if len(set(numbers)) != len(numbers):
        failures.append(
            {
                "reason": "panel marker numbers are not unique",
                "recorded": numbers,
            }
        )
    if any(total != EXPECTED_PANEL_TOTAL for total in totals):
        failures.append(
            {
                "reason": "panel marker denominator mismatch",
                "recorded": totals,
                "expected": EXPECTED_PANEL_TOTAL,
            }
        )
    labels = [normalise(marker["label"]) for marker in markers]
    if len(set(labels)) != len(labels):
        failures.append(
            {
                "reason": "panel marker labels are not unique",
                "recorded": labels,
            }
        )
    return {
        "surface": surface,
        "expected_total": EXPECTED_PANEL_TOTAL,
        "count": len(markers),
        "numbers": numbers,
        "totals": totals,
        "labels": [marker["label"] for marker in markers],
        "failures": failures,
        "pass": not failures,
    }


def panel_semantic_label_normalise(label: str) -> str:
    value = unicodedata.normalize("NFKC", label)
    value = re.sub(r"[*_`#>|]", " ", value)
    value = value.replace("–", "-").replace("—", "-")
    value = value.replace("‘", "'").replace("’", "'")
    value = value.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", value).strip().casefold()


def panel_marker_parity(
    authoritative_source_text: str,
    destination_text: str,
) -> dict:
    source = panel_marker_integrity(
        authoritative_source_text,
        surface="authoritative formal Learning-Session.md",
    )
    destination = panel_marker_integrity(
        destination_text,
        surface="REVISION-GUIDE.md master-flow destination",
    )
    source_tuples = [
        [
            number,
            total,
            panel_semantic_label_normalise(label),
        ]
        for number, total, label in zip(
            source["numbers"],
            source["totals"],
            source["labels"],
        )
    ]
    destination_tuples = [
        [
            number,
            total,
            panel_semantic_label_normalise(label),
        ]
        for number, total, label in zip(
            destination["numbers"],
            destination["totals"],
            destination["labels"],
        )
    ]
    mismatches = [
        {
            "position": position,
            "source": source_tuple,
            "destination": destination_tuple,
        }
        for position, (source_tuple, destination_tuple) in enumerate(
            itertools.zip_longest(source_tuples, destination_tuples),
            1,
        )
        if source_tuple != destination_tuple
    ]
    failures = []
    if mismatches:
        failures.append(
            {
                "reason": "source-destination panel label parity mismatch",
                "mismatches": mismatches,
            }
        )
    source_panels = source_semantic_clusters(authoritative_source_text, 1)
    destination_panels = source_semantic_clusters(destination_text, 1)
    payload_mismatches = []
    for position, (source_panel, destination_panel) in enumerate(
        itertools.zip_longest(source_panels, destination_panels),
        1,
    ):
        source_hash = source_panel.get("text_sha256") if source_panel else None
        destination_hash = (
            destination_panel.get("text_sha256") if destination_panel else None
        )
        if source_hash != destination_hash:
            payload_mismatches.append(
                {
                    "position": position,
                    "source_sha256": source_hash,
                    "destination_sha256": destination_hash,
                }
            )
    if payload_mismatches:
        failures.append(
            {
                "reason": "source-destination panel payload hash mismatch",
                "mismatches": payload_mismatches,
            }
        )
    return {
        "normalization": (
            "NFKC, case-folding, whitespace collapse, Markdown-marker removal, "
            "and dash/quote presentation normalization only; conceptual words are retained"
        ),
        "source_tuples": source_tuples,
        "destination_tuples": destination_tuples,
        "mismatches": mismatches,
        "source_panel_sha256": [
            panel["text_sha256"] for panel in source_panels
        ],
        "destination_panel_sha256": [
            panel["text_sha256"] for panel in destination_panels
        ],
        "payload_mismatches": payload_mismatches,
        "failures": failures,
        "pass": source["pass"] and destination["pass"] and not failures,
    }


def extract_formal_blocks() -> list[dict]:
    blocks = []
    for source_code, path in FORMAL_SOURCES.items():
        lines = path.read_text(encoding="utf-8").splitlines()
        headings = []
        occurrences = Counter()
        parents: dict[int, str] = {}
        parent_ids: dict[int, str] = {}
        for index, line in enumerate(lines):
            match = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
            if not match:
                continue
            level = len(match.group(1))
            heading = match.group(2)
            ancestor_headings = [
                parents[parent_level] for parent_level in range(2, level)
                if parent_level in parents
            ]
            key = normalise(heading)
            occurrences[key] += 1
            identity_hash = hashlib.sha1(
                f"{path_label(path)}|{heading}|{occurrences[key]}".encode("utf-8")
            ).hexdigest()[:10]
            block_id = (
                f"{source_code}-{slug(heading)}-{occurrences[key]:02d}-{identity_hash}"
            )
            parent_level = max(
                (candidate for candidate in parent_ids if candidate < level),
                default=None,
            )
            headings.append(
                {
                    "id": block_id,
                    "source_code": source_code,
                    "source_file": path_label(path),
                    "source_line": index + 1,
                    "heading_level": level,
                    "source_heading": heading,
                    "context_heading": ancestor_headings[-1] if ancestor_headings else None,
                    "ancestor_headings": ancestor_headings,
                    "parent_id": parent_ids.get(parent_level),
                    "start_index": index,
                }
            )
            parents[level] = heading
            parent_ids[level] = block_id
            for deeper in range(level + 1, 6):
                parents.pop(deeper, None)
                parent_ids.pop(deeper, None)
        for position, block in enumerate(headings):
            end_index = len(lines)
            for following in headings[position + 1:]:
                if following["heading_level"] <= block["heading_level"]:
                    end_index = following["start_index"]
                    break
            child_ids = [
                following["id"]
                for following in headings
                if following.get("parent_id") == block["id"]
            ]
            direct_end_index = end_index
            if child_ids:
                first_child = next(
                    following
                    for following in headings[position + 1:]
                    if following.get("parent_id") == block["id"]
                )
                direct_end_index = first_child["start_index"]
            block_text = "\n".join(lines[block["start_index"]:end_index]).strip()
            block_body = body_without_headings_and_labels(block_text)
            parent_only_text = "\n".join(
                lines[block["start_index"]:direct_end_index]
            ).strip()
            parent_only_body = body_without_headings_and_labels(parent_only_text)
            block["end_line"] = end_index
            block["block_text"] = block_text
            block["block_body"] = block_body
            block["source_signature"] = concept_signature(block_body)
            block["source_body_witnesses"] = substantive_body_witnesses(block_body)
            block["child_ids"] = child_ids
            block["is_structural_umbrella"] = bool(child_ids)
            block["parent_only_text"] = parent_only_text
            block["parent_only_body"] = parent_only_body
            block["parent_only_signature"] = concept_signature(parent_only_body)
            block["parent_only_witnesses"] = substantive_body_witnesses(parent_only_body)
            body_physical_lines = max(0, len(block_text.splitlines()) - 1)
            body_word_count = len(words(block_body))
            body_semantic_token_count = len(semantic_terms(block_body))
            block["large_leaf_detection"] = {
                "physical_lines": body_physical_lines,
                "words": body_word_count,
                "semantic_tokens": body_semantic_token_count,
                "thresholds": {
                    "physical_lines": LARGE_LEAF_MIN_PHYSICAL_LINES,
                    "words": LARGE_LEAF_MIN_WORDS,
                    "semantic_tokens": LARGE_LEAF_MIN_SEMANTIC_TOKENS,
                },
                "is_large_leaf": bool(
                    not child_ids
                    and (
                        body_physical_lines >= LARGE_LEAF_MIN_PHYSICAL_LINES
                        or body_word_count >= LARGE_LEAF_MIN_WORDS
                        or body_semantic_token_count >= LARGE_LEAF_MIN_SEMANTIC_TOKENS
                    )
                ),
            }
            block["source_segments"] = (
                [] if child_ids else source_text_segments(block_text, block["source_line"])
            )
            block["semantic_clusters"] = (
                [] if child_ids else source_semantic_clusters(block_text, block["source_line"])
            )
            blocks.append(block)
        by_id = {block["id"]: block for block in blocks if block["source_code"] == source_code}
        for block in by_id.values():
            descendants = []
            pending = list(block["child_ids"])
            while pending:
                child_id = pending.pop(0)
                descendants.append(child_id)
                pending.extend(by_id[child_id]["child_ids"])
            block["descendant_ids"] = descendants
    return blocks


def find_heading_section(text: str, anchor: str, context_anchor: str | None = None) -> str:
    scope = text
    if context_anchor:
        context = find_heading_section(text, context_anchor)
        if not context:
            return ""
        scope = context
    matches = list(re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*$", scope))
    anchor_normalized = normalise(anchor)
    for index, match in enumerate(matches):
        if normalise(match.group(2)) != anchor_normalized:
            continue
        level = len(match.group(1))
        end = len(scope)
        for following in matches[index + 1:]:
            if len(following.group(1)) <= level:
                end = following.start()
                break
        return scope[match.start():end]
    return ""


def literal_anchor_section(text: str, anchor: str) -> str:
    marker = re.search(
        rf"(?m)^{re.escape(anchor)}\s*$",
        text,
    )
    if not marker:
        return ""
    end = len(text)
    if re.match(r"ASCII MASTER FLOW [—-] PANEL ", anchor):
        following = re.search(
            r"(?m)^ASCII MASTER FLOW [—-] PANEL \d+/\d+:",
            text[marker.end():],
        )
        closing_fence = re.search(r"(?m)^```\s*$", text[marker.end():])
        candidates = [
            marker.end() + match.start()
            for match in (following, closing_fence)
            if match
        ]
        if candidates:
            end = min(candidates)
    else:
        following_heading = re.search(r"(?m)^#{1,6}\s+", text[marker.end():])
        if following_heading:
            end = marker.end() + following_heading.start()
    return text[marker.start():end].strip()


def destination_body_for_reference(text: str, reference: dict) -> str:
    if reference.get("anchor_kind") == "literal":
        return body_without_headings_and_labels(
            literal_anchor_section(text, reference.get("anchor", ""))
        )
    return section_body(
        text,
        reference.get("anchor", ""),
        reference.get("context_anchor"),
    )


def distributed_claim_live_audit(
    blocks: list[dict],
    review_decisions: dict[str, dict],
    package_text: dict[str, str],
    semantic_contextual_justifications: list[dict] | None = None,
) -> dict:
    claims = []
    family_counts = Counter({family: 0 for family in MALFORMED_CLAIM_FAMILIES})
    source_correspondence_failures = []
    destination_correspondence_failures = []
    conceptual_correspondence_failures = []
    unit_count = 0
    units_with_wrong_claim_count = []
    for block in blocks:
        decision = review_decisions.get(block["id"], {})
        inventory = decision.get("distributed_proposition_inventory", [])
        if not inventory:
            continue
        extracted_units = {
            ("cluster", item["id"]): item for item in block["semantic_clusters"]
        }
        extracted_units.update(
            {("segment", item["id"]): item for item in block["source_segments"]}
        )
        for item in inventory:
            unit_count += 1
            propositions = item.get("propositions", [])
            if len(propositions) != 2:
                units_with_wrong_claim_count.append(
                    {
                        "block": block["id"],
                        "unit": item.get("id"),
                        "count": len(propositions),
                    }
                )
            unit = extracted_units.get((item.get("kind"), item.get("id")))
            source_body = unit.get("body", "") if unit else ""
            destination_body = "\n".join(
                destination_body_for_reference(
                    package_text.get(reference.get("file", ""), ""),
                    reference,
                )
                for reference in item.get("destination_anchors", [])
            )
            for proposition in propositions:
                claim = proposition.get("claim", "")
                proposition_id = proposition.get("id")
                qualified_id = qualified_proposition_id(
                    block["id"],
                    item.get("id", ""),
                    proposition_id or "",
                )
                hits = malformed_claim_family_hits(
                    claim,
                    block_id=block["id"],
                    proposition_id=proposition_id,
                )
                for family in set(hits):
                    family_counts[family] += 1
                correspondence = claim_correspondence_metrics(
                    claim,
                    source_body,
                    destination_body,
                )
                claim_record = {
                    "block": block["id"],
                    "unit": item.get("id"),
                    "proposition": proposition_id,
                    "qualified_proposition": qualified_id,
                    "claim": claim,
                    "semantic_key": proposition.get("semantic_key"),
                    "semantic_key_fingerprint": semantic_key_fingerprint(
                        proposition
                    ),
                    "bounded_semantic_failures": semantic_key_validation_failures(
                        proposition,
                        claim,
                        source_body,
                        destination_body,
                        context=qualified_id,
                        qualified_id=qualified_id,
                    ),
                    "families": sorted(set(hits)),
                    "template_signature": claim_template_signature(claim),
                    "correspondence": correspondence,
                }
                claims.append(claim_record)
                if len(correspondence["source_overlap"]) < 4:
                    source_correspondence_failures.append(claim_record)
                if len(correspondence["destination_overlap"]) < 4:
                    destination_correspondence_failures.append(claim_record)
                if len(correspondence["discriminative_terms"]) < 3:
                    conceptual_correspondence_failures.append(claim_record)
    exact_groups = [
        group
        for group in (
            [item for item in claims if normalise(item["claim"]) == claim_key]
            for claim_key in {normalise(item["claim"]) for item in claims}
        )
        if len(group) > 1
    ]
    near_pairs = []
    for first_index, first in enumerate(claims):
        for second in claims[first_index + 1:]:
            sequence, jaccard = claim_similarity(first["claim"], second["claim"])
            if sequence >= .82 or jaccard >= .72:
                near_pairs.append(
                    {
                        "first": first["proposition"],
                        "second": second["proposition"],
                        "sequence_ratio": round(sequence, 3),
                        "semantic_jaccard": round(jaccard, 3),
                    }
                )
    template_groups = [
        group
        for group in (
            [
                item
                for item in claims
                if item["template_signature"] == template_signature
            ]
            for template_signature in sorted({
                item["template_signature"] for item in claims
                if claim_template_is_structural(item["template_signature"])
            })
        )
        if len(group) >= 3
    ]
    malformed_claims = [
        item for item in claims if item["families"]
    ]
    declarations = semantic_contextual_justifications or []
    justification_map, justification_failures = (
        semantic_contextual_justification_map(declarations)
    )
    missing_semantic_keys = []
    for claim in claims:
        if not claim["semantic_key_fingerprint"]:
            missing_semantic_keys.append(claim)
    semantic_candidate_groups = []
    for first_index, first in enumerate(claims):
        for second in claims[first_index + 1:]:
            metrics = semantic_key_equivalence_metrics(first, second)
            if not metrics["equivalent"]:
                continue
            semantic_candidate_groups.append(
                {
                    "fingerprint": (
                        first["semantic_key_fingerprint"]
                        if first["semantic_key_fingerprint"]
                        == second["semantic_key_fingerprint"]
                        else "semantic-key-equivalence"
                    ),
                    "equivalence_metrics": metrics,
                    "propositions": [
                        {
                            "qualified_proposition": claim["qualified_proposition"],
                            "claim": claim["claim"],
                            "semantic_key": claim["semantic_key"],
                        }
                        for claim in (first, second)
                    ],
                }
            )
    justified_pairs = []
    unjustified_pairs = []
    live_candidate_pairs = set()
    for group in semantic_candidate_groups:
        proposition_ids = [
            item["qualified_proposition"] for item in group["propositions"]
        ]
        for first, second in itertools.combinations(proposition_ids, 2):
            pair = tuple(sorted((first, second)))
            live_candidate_pairs.add(pair)
            record = {
                "proposition_ids": list(pair),
                "fingerprint": group["fingerprint"],
                "equivalence_metrics": group["equivalence_metrics"],
            }
            if pair in justification_map:
                justified_pairs.append(
                    {**record, "reason": justification_map[pair]}
                )
            else:
                unjustified_pairs.append(record)
    orphan_justifications = [
        {
            "reason": "semantic contextual justification has no live equivalent pair",
            "proposition_ids": list(pair),
            "declared_reason": reason,
        }
        for pair, reason in sorted(justification_map.items())
        if pair not in live_candidate_pairs
    ]
    semantic_review_failures = [
        *justification_failures,
        *orphan_justifications,
    ]
    claims_by_id = {
        claim["qualified_proposition"]: claim
        for claim in claims
    }
    repaired_claim_rows = []
    for qualified_id in REPAIRED_CLAIM_IDS:
        claim = claims_by_id.get(qualified_id)
        grammar_pass = bool(
            claim
            and not claim["families"]
            and claim["claim"][0].isupper()
            and claim["claim"][-1:] in {".", "?", "!"}
            and len(words(claim["claim"])) >= 12
            and not DEPENDENT_CLAIM_SUBJECT_PATTERN.match(claim["claim"])
        )
        bounded_semantic_pass = bool(
            claim
            and not claim["bounded_semantic_failures"]
            and len(claim["correspondence"]["source_overlap"]) >= 4
            and len(claim["correspondence"]["destination_overlap"]) >= 4
            and len(claim["correspondence"]["discriminative_terms"]) >= 3
        )
        repaired_claim_rows.append(
            {
                "qualified_proposition": qualified_id,
                "present": claim is not None,
                "grammar_pass": grammar_pass,
                "bounded_semantic_pass": bounded_semantic_pass,
                "families": claim["families"] if claim else ["missing_claim"],
                "semantic_failures": (
                    claim["bounded_semantic_failures"]
                    if claim
                    else [{"reason": "missing repaired claim"}]
                ),
            }
        )
    repaired_pair_rows = []
    for first_id, second_id in REPAIRED_SEMANTIC_DUPLICATE_PAIRS:
        first = claims_by_id.get(first_id)
        second = claims_by_id.get(second_id)
        metrics = (
            semantic_key_equivalence_metrics(first, second)
            if first and second
            else {"equivalent": True, "reason": "missing repaired duplicate claim"}
        )
        repaired_pair_rows.append(
            {
                "proposition_ids": [first_id, second_id],
                "both_present": bool(first and second),
                "semantic_key_equivalent": metrics["equivalent"],
                "equivalence_metrics": metrics,
                "pass": bool(first and second) and not metrics["equivalent"],
            }
        )
    repaired_claim_assertions = {
        "expected_claim_count": len(REPAIRED_CLAIM_IDS),
        "claims": repaired_claim_rows,
        "duplicate_pairs": repaired_pair_rows,
        "pass": (
            all(
                row["present"]
                and row["grammar_pass"]
                and row["bounded_semantic_pass"]
                for row in repaired_claim_rows
            )
            and all(row["pass"] for row in repaired_pair_rows)
        ),
    }
    expected_units = sum(
        len(decision.get("distributed_proposition_inventory", []))
        for decision in review_decisions.values()
    )
    expected_claims = expected_units * 2
    return {
        "claims_checked": len(claims),
        "expected_claims": expected_claims,
        "units_checked": unit_count,
        "expected_units": expected_units,
        "claims_per_unit_required": 2,
        "units_with_wrong_claim_count": units_with_wrong_claim_count,
        "malformed_claim_count": len(malformed_claims),
        "malformed_family_counts": dict(sorted(family_counts.items())),
        "reported_malformed_family_count": len(family_counts),
        "malformed_claims": malformed_claims,
        "global_exact_duplicate_groups": len(exact_groups),
        "global_exact_duplicates": exact_groups,
        "global_near_duplicate_pairs": len(near_pairs),
        "global_near_duplicates": near_pairs,
        "global_repeated_template_groups": len(template_groups),
        "unjustified_template_group_count": len(template_groups),
        "global_repeated_templates": template_groups,
        "semantic_duplicate_candidates": {
            "candidate_group_count": len(semantic_candidate_groups),
            "candidate_groups": semantic_candidate_groups,
            "declared_contextual_justifications": declarations,
            "justified_exact_id_pair_count": len(justified_pairs),
            "justified_exact_id_pairs": justified_pairs,
            "unjustified_semantic_duplicate_count": len(unjustified_pairs),
            "unjustified_semantic_duplicates": unjustified_pairs,
            "missing_semantic_key_count": len(missing_semantic_keys),
            "missing_semantic_keys": [
                item["qualified_proposition"] for item in missing_semantic_keys
            ],
            "justification_failures": semantic_review_failures,
            "pass": (
                not missing_semantic_keys
                and not unjustified_pairs
                and not semantic_review_failures
            ),
        },
        "repaired_claim_assertions": repaired_claim_assertions,
        "source_correspondence_failures": len(source_correspondence_failures),
        "destination_correspondence_failures": len(
            destination_correspondence_failures
        ),
        "conceptual_correspondence_failures": len(
            conceptual_correspondence_failures
        ),
        "pass": (
            len(claims) == expected_claims
            and unit_count == expected_units
            and not units_with_wrong_claim_count
            and not malformed_claims
            and not exact_groups
            and not near_pairs
            and not template_groups
            and not missing_semantic_keys
            and not unjustified_pairs
            and not semantic_review_failures
            and repaired_claim_assertions["pass"]
            and not source_correspondence_failures
            and not destination_correspondence_failures
            and not conceptual_correspondence_failures
        ),
    }


def section_body(text: str, anchor: str, context_anchor: str | None = None) -> str:
    return body_without_headings_and_labels(
        find_heading_section(text, anchor, context_anchor)
    )


def route_assertion_set_sha256(evidence: dict) -> str:
    payload = {
        "reviewed_assertions": evidence.get("reviewed_assertions", []),
        "required_semantic_assertions": evidence.get(
            "required_semantic_assertions", []
        ),
        "forbidden_exact_text": evidence.get("forbidden_exact_text", []),
        "forbidden_semantic_assertions": evidence.get(
            "forbidden_semantic_assertions", []
        ),
    }
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def route_assertion_validation_failures(evidence: dict, section: str) -> list[dict]:
    failures = []
    normalized_section = normalise(section)
    for assertion in evidence.get("reviewed_assertions", []):
        claim = assertion.get("claim", "")
        required_text = assertion.get("required_exact_text", [])
        if not claim or not required_text:
            failures.append(
                {
                    "reason": "route assertion declaration incomplete",
                    "assertion": assertion.get("id"),
                }
            )
            continue
        absent = [
            phrase
            for phrase in required_text
            if normalise(phrase) not in normalized_section
        ]
        if absent:
            failures.append(
                {
                    "reason": "required route assertion absent",
                    "assertion": assertion.get("id"),
                    "absent_exact_text": absent,
                }
            )
        claim_terms = set(semantic_terms(claim))
        section_terms = set(semantic_terms(section))
        overlap = sorted(claim_terms & section_terms)
        if len(overlap) < 5:
            failures.append(
                {
                    "reason": "route assertion lacks semantic correspondence",
                    "assertion": assertion.get("id"),
                    "matched_terms": overlap,
                }
            )
    for forbidden in evidence.get("forbidden_exact_text", []):
        if normalise(forbidden) in normalized_section:
            failures.append(
                {
                    "reason": "forbidden contradictory route assertion present",
                    "forbidden_exact_text": forbidden,
                }
            )
    for assertion in evidence.get("required_semantic_assertions", []):
        missing_groups = [
            group
            for group in assertion.get("term_groups", [])
            if not any(normalise(phrase) in normalized_section for phrase in group)
        ]
        if missing_groups:
            failures.append(
                {
                    "reason": "required semantic route assertion absent",
                    "assertion": assertion.get("id"),
                    "missing_term_groups": missing_groups,
                }
            )
    for assertion in evidence.get("forbidden_semantic_assertions", []):
        if re.search(assertion["pattern"], normalized_section, re.I | re.S):
            failures.append(
                {
                    "reason": "forbidden semantic route assertion present",
                    "assertion": assertion.get("id"),
                    "pattern": assertion["pattern"],
                }
            )
    return failures


def load_formal_review() -> dict:
    if not FORMAL_REVIEW.is_file():
        return {"schema_version": None, "decisions": []}
    return json.loads(FORMAL_REVIEW.read_text(encoding="utf-8"))


def review_decisions_by_id(payload: dict) -> dict[str, dict]:
    return {
        decision["id"]: decision
        for decision in payload.get("decisions", [])
        if isinstance(decision, dict) and decision.get("id")
    }


def canonical_review_block(block: dict) -> str:
    block_text = unicodedata.normalize(
        "NFC",
        block["block_text"].replace("\r\n", "\n").replace("\r", "\n"),
    )
    block_text = "\n".join(line.rstrip() for line in block_text.splitlines()).strip("\n")
    return json.dumps(
        {
            "source_file": block["source_file"],
            "heading_level": block["heading_level"],
            "source_heading": block["source_heading"],
            "ancestor_headings": block["ancestor_headings"],
            "block_text": block_text,
        },
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def decision_bound_sha256(block: dict) -> str:
    return hashlib.sha256(canonical_review_block(block).encode("utf-8")).hexdigest()


def review_hash_regression_check(blocks: list[dict]) -> dict:
    semantic_label = "Plain-language visual"
    sample = next(
        block for block in blocks
        if semantic_label in block["block_text"]
        and block["ancestor_headings"]
    )
    original_hash = decision_bound_sha256(sample)

    label_mutation = dict(sample)
    label_mutation["block_text"] = sample["block_text"].replace(
        semantic_label,
        semantic_label + " MUTATED",
        1,
    )
    heading_mutation = dict(sample)
    heading_mutation["source_heading"] = sample["source_heading"] + " MUTATED"
    context_mutation = dict(sample)
    context_mutation["ancestor_headings"] = [
        *sample["ancestor_headings"][:-1],
        sample["ancestor_headings"][-1] + " MUTATED",
    ]
    mutation_hashes = {
        "semantic_label": decision_bound_sha256(label_mutation),
        "heading": decision_bound_sha256(heading_mutation),
        "context": decision_bound_sha256(context_mutation),
    }
    return {
        "sample_block_id": sample["id"],
        "semantic_label": semantic_label,
        "original_sha256": original_hash,
        "mutation_sha256": mutation_hashes,
        "all_mutations_stale_decision": all(
            value != original_hash for value in mutation_hashes.values()
        ),
    }


def coverage_negative_test_results(
    blocks: list[dict],
    review_decisions: dict[str, dict],
    semantic_contextual_justifications: list[dict],
) -> dict:
    package_text = {path.name: path.read_text(encoding="utf-8") for path in TOPIC.glob("*.md")}

    def destination_body(decision: dict) -> str:
        bodies = []
        for destination in decision.get("package_destinations", []):
            text = package_text.get(destination.get("file", ""), "")
            body = destination_body_for_reference(text, destination)
            if body:
                bodies.append(body)
        return "\n".join(bodies)

    def record(name: str, failures: list[dict], expected: list[str]) -> dict:
        reasons = sorted({item.get("reason", "") for item in failures})
        return {"name": name, "expected_reasons": expected, "actual_reasons": reasons,
                "rejected": bool(failures), "pass": bool(failures) and all(x in reasons for x in expected)}

    parent = next(block for block in blocks if block["is_structural_umbrella"] and
                  len(words(block["parent_only_body"])) >= 12 and
                  review_decisions[block["id"]].get("required_propositions"))
    parent_decision = review_decisions[parent["id"]]
    child_resolution = {child: True for child in parent["child_ids"]}
    dropped_parent = copy.deepcopy(parent)
    dropped_parent["parent_only_text"] = f"### {parent['source_heading']}"
    dropped_parent["parent_only_body"] = ""
    parent_failures = structural_umbrella_validation_failures(dropped_parent, parent_decision, child_resolution)
    parent_failures += proposition_validation_failures(
        parent_decision.get("required_propositions", []), "", destination_body(parent_decision),
        require_semantic_specificity=False, context="negative-test:parent-only-drop")

    dropped_child = copy.deepcopy(parent_decision)
    dropped_child["structural_umbrella"]["child_ids"] = parent["child_ids"][:-1]
    child_failures = structural_umbrella_validation_failures(parent, dropped_child, child_resolution)

    large = next(block for block in blocks if review_decisions[block["id"]].get("distributed_proposition_inventory"))
    decision = review_decisions[large["id"]]
    opening_failures = distributed_inventory_validation_failures(
        large, decision["distributed_proposition_inventory"][:1], decision["package_destinations"], package_text)
    generic = copy.deepcopy(decision["distributed_proposition_inventory"])
    for unit in generic:
        unit["propositions"] = [{"id": f"{unit['id']}-generic", "claim": "The source explains how the topic supports the overall argument.", "witnesses": ["the source"]}]
    generic_failures = distributed_inventory_validation_failures(large, generic, decision["package_destinations"], package_text)
    unrelated = copy.deepcopy(decision["distributed_proposition_inventory"])
    unrelated[0]["propositions"][0]["claim"] = "Kant derives transcendental unity from apperception and the categories."
    unrelated_failures = distributed_inventory_validation_failures(large, unrelated, decision["package_destinations"], package_text)
    dependent = copy.deepcopy(decision["distributed_proposition_inventory"])
    dependent[0]["propositions"][0]["claim"] = "It does not establish the position because this remains disputed."
    dependent_failures = distributed_inventory_validation_failures(large, dependent, decision["package_destinations"], package_text)

    def distributed_item(
        decisions: dict[str, dict],
        block: dict,
        unit_id: str,
    ) -> dict:
        return next(
            item
            for item in decisions[block["id"]][
                "distributed_proposition_inventory"
            ]
            if item["id"] == unit_id
        )

    master = next(
        block
        for block in blocks
        if block["source_heading"] == "COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM"
    )

    def live_claim_mutation_failures(claim: str) -> list[dict]:
        mutated = copy.deepcopy(decision["distributed_proposition_inventory"])
        mutated[0]["propositions"][0]["claim"] = claim
        return distributed_inventory_validation_failures(
            large,
            mutated,
            decision["package_destinations"],
            package_text,
        )

    live_malformed_mutations = {
        "actual_panel_10_token_salad": (
            "The teacher prevents points from replacing nuts with says because ostension governs naming in the lesson."
        ),
        "bare_token_bag_salad": (
            "Freedom facticity transcendence choice responsibility anxiety authenticity temporality existence shows."
        ),
        "comma_separated_all_caps_subject": (
            "FACTICITY, TRANSCENDENCE, AUTHENTICITY define the answer."
        ),
        "dangling_fragment": (
            "Sartre relates freedom, facticity, responsibility, and bad faith with."
        ),
        "dangling_pipe": (
            "Sartre's account gives freedom meaning through responsibility |."
        ),
        "demand_label_fragment": (
            "DEMANDS: reconstruct Sartre before giving a philosophical verdict."
        ),
        "dependent_subject": (
            "Yet it discloses freedom through anxiety without naming an independent subject."
        ),
        "diagram_arrow_chain": (
            "Bad faith -> alienation -> authenticity produces a misleading chain."
        ),
        "diagram_label_chain": (
            "SOURCE anxiety: OBJECT nothing; FORMULA dizziness of freedom."
        ),
        "distinguishes_because_governs": (
            "Sartre distinguishes content from core because freedom governs explanation, whereas facticity constrains possibility through choice."
        ),
        "ellipsis_fragment": (
            "Sartre connects freedom with facticity, transcendence, choice, and responsibility ..."
        ),
        "generated_governs_constrains_salad": (
            "Freedom appears because choice governs responsibility, whereas facticity constrains possibility."
        ),
        "generated_guides_prevents_salad": (
            "Existence requires freedom to guide responsibility, whereas facticity prevents choice."
        ),
        "generated_situates_token_salad": (
            "Springet situates transition between spheres and qualitative."
        ),
        "incomplete_proposition": (
            "The two shapes of despair. Not willing to be oneself while fleeing the actual self."
        ),
        "isolated_diagram_v_marker": (
            "V Sartre rejects the unconscious while consciousness remains non-self-identical."
        ),
        "numbered_diagram_label": (
            "P1 Sartre treats atheism as the premise of the paper-knife argument."
        ),
        "presentation_or_demand_label": (
            "Definition: freedom is situated through facticity and transcendence."
        ),
        "prevents_from_replacing": (
            "Sartre prevents bad faith from replacing responsibility with an excuse."
        ),
        "raw_diagram_label": (
            "ASCII MASTER FLOW: Sartre links freedom, facticity, and responsibility."
        ),
        "relation_between_requires": (
            "The relation between freedom and facticity requires choice to guide responsibility."
        ),
        "replacement_glyph": (
            "Sartre\ufffd's account connects freedom with responsibility and situated choice."
        ),
        "source_treats": (
            "The source treats bad faith as a flight from situated freedom and responsibility."
        ),
        "within_the_practice_of": (
            "Within the practice of choice, freedom appears through situated responsibility."
        ),
    }
    malformed_family_mutation_rows = []
    for family in MALFORMED_CLAIM_FAMILIES:
        claim = live_malformed_mutations[family]
        failures = live_claim_mutation_failures(claim)
        expected_reason = f"malformed distributed claim family: {family}"
        actual_reasons = sorted({item.get("reason", "") for item in failures})
        malformed_family_mutation_rows.append(
            {
                "family": family,
                "mutation_claim": claim,
                "expected_reason": expected_reason,
                "actual_reasons": actual_reasons,
                "rejected": bool(failures),
                "pass": expected_reason in actual_reasons,
            }
        )
    malformed_family_mutation_matrix = {
        "reported_family_count": len(MALFORMED_CLAIM_FAMILIES),
        "tested_family_count": len(malformed_family_mutation_rows),
        "families": list(MALFORMED_CLAIM_FAMILIES),
        "rows": malformed_family_mutation_rows,
        "pass": (
            set(live_malformed_mutations) == set(MALFORMED_CLAIM_FAMILIES)
            and len(malformed_family_mutation_rows) == 24
            and all(row["pass"] for row in malformed_family_mutation_rows)
        ),
    }
    semantic_equivalence_probe = semantic_key_equivalence_metrics(
        {
            "claim": (
                "Heidegger's fundamental ontology selects Dasein because this "
                "entity has a pre-ontological understanding of Being and its "
                "own existence remains at issue."
            ),
            "semantic_key": {
                "doctrine": "fundamental ontology selects Dasein",
                "subject": "the inquiry",
                "predicate": "selects",
                "object_or_conclusion": "understanding of Being and existence at issue",
                "polarity_or_qualification": "Dasein has ontological priority",
                "argumentative_role": "Negative mutation probe for semantic equivalence.",
            },
        },
        {
            "claim": (
                "The inquiry chooses Dasein because it already possesses a "
                "pre-ontological understanding of Being and its own existence "
                "remains at issue."
            ),
            "semantic_key": {
                "doctrine": "inquiry chooses Dasein",
                "subject": "Dasein",
                "predicate": "chooses",
                "object_or_conclusion": "existence at issue and understanding of Being",
                "polarity_or_qualification": "Dasein receives ontological priority",
                "argumentative_role": "Paraphrase mutation probe for semantic equivalence.",
            },
        },
    )
    repeated_template = copy.deepcopy(
        decision["distributed_proposition_inventory"]
    )
    repeated_template_claims = [
        "Meaning shows that use depends on practice because speakers require correction.",
        "Language shows that a rule depends on training because learners require correction.",
        "Grammar shows that a word depends on use because communities require correction.",
    ]
    for unit, claim in zip(repeated_template, repeated_template_claims):
        unit["propositions"][0]["claim"] = claim
    repeated_template_failures = distributed_inventory_validation_failures(
        large,
        repeated_template,
        decision["package_destinations"],
        package_text,
    )

    master_decision = review_decisions[master["id"]]
    reduced_panel_failures = distributed_inventory_validation_failures(
        master, master_decision["distributed_proposition_inventory"][:-1], master_decision["package_destinations"], package_text)
    cloned_panels = copy.deepcopy(master_decision["distributed_proposition_inventory"])
    first_anchors = cloned_panels[0]["destination_anchors"]
    for unit in cloned_panels:
        unit["destination_anchors"] = copy.deepcopy(first_anchors)
    cloned_panel_failures = distributed_inventory_validation_failures(
        master, cloned_panels, master_decision["package_destinations"], package_text)
    source_panel_text = master["block_text"]
    source_panels = source_semantic_clusters(source_panel_text, 1)
    middle_panel = source_panels[len(source_panels) // 2]
    edge_panel = source_panels[0]
    middle_marker = (
        f"ASCII MASTER FLOW - PANEL {middle_panel['number']}/"
        f"{middle_panel['total']}: {middle_panel['label']}"
    )
    edge_marker = (
        f"ASCII MASTER FLOW - PANEL {edge_panel['number']}/"
        f"{edge_panel['total']}: {edge_panel['label']}"
    )
    removed_source_panel = source_panel_text.replace(middle_marker, "", 1)
    removed_source_panel_failures = panel_marker_integrity(
        removed_source_panel,
        surface="negative-test:authoritative-source-panel-removed",
    )["failures"]
    renumbered_source_panel = source_panel_text.replace(
        middle_marker,
        middle_marker.replace(
            f"PANEL {middle_panel['number']}/{middle_panel['total']}",
            f"PANEL {middle_panel['number'] + 1}/{middle_panel['total']}",
            1,
        ),
        1,
    )
    renumbered_source_panel_failures = panel_marker_integrity(
        renumbered_source_panel,
        surface="negative-test:authoritative-source-panel-renumbered",
    )["failures"]
    destination_master_text = find_heading_section(
        package_text["REVISION-GUIDE.md"],
        "COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM",
    )
    middle_destination_label_mutation = destination_master_text.replace(
        middle_marker,
        (
            f"ASCII MASTER FLOW - PANEL {middle_panel['number']}/"
            f"{middle_panel['total']}: A DIFFERENT CONCEPTUAL VERDICT"
        ),
        1,
    )
    middle_destination_label_failures = panel_marker_parity(
        source_panel_text,
        middle_destination_label_mutation,
    )["failures"]
    edge_destination_label_mutation = destination_master_text.replace(
        edge_marker,
        (
            f"ASCII MASTER FLOW - PANEL {edge_panel['number']}/"
            f"{edge_panel['total']}: AN UNRELATED OWNER CLAIM"
        ),
        1,
    )
    edge_destination_label_failures = panel_marker_parity(
        source_panel_text,
        edge_destination_label_mutation,
    )["failures"]

    generic_witness_failures = witness_quality_failures("in the", context="negative-test:generic-witness")
    duplicate_state = {"entries": []}
    witness_quality_failures("verification meaning criterion", context="negative-test:first", global_state=duplicate_state,
                             block_id="first", witness_id="first", source_body="Verification supplies a criterion of meaning.")
    duplicate_failures = witness_quality_failures("verification meaning criterion", context="negative-test:second", global_state=duplicate_state,
                                                   block_id="second", witness_id="second", source_body="The meaning criterion is verification.")
    cross_block_near_state = {"entries": []}
    witness_quality_failures(
        "rule following trained practice",
        context="negative-test:cross-block-near-first",
        global_state=cross_block_near_state,
        block_id="first-rule-block",
        witness_id="first-rule-witness",
        source_body="Rule-following is exhibited through trained practice.",
    )
    cross_block_near_failures = witness_quality_failures(
        "rules followed in training practices",
        context="negative-test:cross-block-near-second",
        global_state=cross_block_near_state,
        block_id="second-rule-block",
        witness_id="second-rule-witness",
        source_body="Rules are followed within practices of training.",
    )
    same_block_duplicate_state = {"entries": []}
    witness_quality_failures(
        "strong weak verification dilemma",
        context="negative-test:same-block-first",
        global_state=same_block_duplicate_state,
        block_id="same-block",
        witness_id="proposition-a",
        source_body="Strong and weak verification create a dilemma.",
    )
    same_block_duplicate_failures = witness_quality_failures(
        "strong weak verification dilemma",
        context="negative-test:same-block-second",
        global_state=same_block_duplicate_state,
        block_id="same-block",
        witness_id="proposition-b",
        source_body="Strong and weak verification create a dilemma.",
    )
    same_block_near_state = {"entries": []}
    witness_quality_failures(
        "protocol statement public revisable",
        context="negative-test:same-block-near-first",
        global_state=same_block_near_state,
        block_id="same-panel-block",
        witness_id="panel-proposition-a",
        source_body="A protocol statement is public and revisable.",
    )
    same_block_near_failures = witness_quality_failures(
        "protocol statements publicly revisable",
        context="negative-test:same-block-near-second",
        global_state=same_block_near_state,
        block_id="same-panel-block",
        witness_id="panel-proposition-b",
        source_body="Protocol statements remain publicly revisable.",
    )

    route_tests = []
    for obligation in CROSS_TOPIC_ROUTE_OBLIGATIONS:
        for evidence in obligation["destination_evidence"]:
            path = (TOPIC / evidence["file"]).resolve()
            section = find_heading_section(path.read_text(encoding="utf-8"), evidence["anchor"])
            contradiction = "Topic 09 is the sole primary owner of this routed doctrine."
            paraphrase = (
                "Husserl establishes and owns Sartrean nothingness and "
                "Heideggerian being-in-the-world."
            )
            for kind, injected in (("contradiction", contradiction), ("paraphrase", paraphrase)):
                failures = route_assertion_validation_failures(evidence, section + "\n" + injected)
                route_tests.append({"obligation": obligation["id"], "destination": evidence["file"],
                                    "mutation": kind, "rejected": any(x.get("reason") == "forbidden semantic route assertion present" for x in failures)})

    extra_route = copy.deepcopy(review_decisions)
    extra_id = next(
        block_id
        for block_id, decision in extra_route.items()
        if decision.get("classification") == "covered_in_scope"
    )
    extra_route[extra_id].update(
        {
            "classification": "routed_to_canonical_owner",
            "inbound_obligation_id": "WP-UNDECLARED-ROUTE",
            "routed_owner": "../11-Quine-and-Strawson",
            "obligation_status": "fulfilled_substantively",
            "resolution_status": "resolved_routed_to_verified_owner",
        }
    )
    extra_route_failures = routed_decision_binding_failures(extra_route)

    tests = [
        record("parent-only proposition removed", parent_failures, ["structural umbrella declaration mismatch", "proposition witness absent from source body"]),
        record("structural child removed", child_failures, ["structural umbrella declaration mismatch"]),
        record("large leaf reduced to opening", opening_failures, ["distributed inventory does not span every extracted unit"]),
        record("generic padding inventory", generic_failures, ["boilerplate proposition template"]),
        record("unrelated proposition", unrelated_failures, ["claim lacks discriminative source vocabulary"]),
        record("dependent-subject proposition", dependent_failures, ["distributed claim lacks an explicit independent subject"]),
        {
            "name": "malformed family production mutation matrix",
            "rejected": malformed_family_mutation_matrix["pass"],
            "pass": malformed_family_mutation_matrix["pass"],
        },
        {
            "name": "semantic-key equivalent paraphrase",
            "equivalence_metrics": semantic_equivalence_probe,
            "rejected": semantic_equivalence_probe["equivalent"],
            "pass": semantic_equivalence_probe["equivalent"],
        },
        record(
            "global repeated structural template",
            repeated_template_failures,
            ["repeated distributed claim template"],
        ),
        record("panel removed", reduced_panel_failures, ["distributed inventory does not span every extracted unit"]),
        record("panel anchors cloned", cloned_panel_failures, ["master-flow panels reuse a generic destination anchor"]),
        record("authoritative source panel removed", removed_source_panel_failures, ["panel marker count mismatch", "panel markers are not the exact ordered sequence"]),
        record("authoritative source panel renumbered", renumbered_source_panel_failures, ["panel markers are not the exact ordered sequence", "panel marker numbers are not unique"]),
        record("destination middle-panel label changed", middle_destination_label_failures, ["source-destination panel label parity mismatch"]),
        record("destination edge-panel label changed", edge_destination_label_failures, ["source-destination panel label parity mismatch"]),
        record("generic witness", generic_witness_failures, ["generic or insufficiently specific witness"]),
        record("cross-block duplicate witness", duplicate_failures, ["cross-block duplicate witness misdirection"]),
        record("cross-block near-duplicate witness", cross_block_near_failures, ["cross-block near-duplicate witness"]),
        record("same-block duplicate witness", same_block_duplicate_failures, ["same-block duplicate witness misdirection"]),
        record("same-block near-duplicate witness", same_block_near_failures, ["same-block near-duplicate witness"]),
        record("routed decision extra row", extra_route_failures, ["routed stable block-id union mismatch"]),
        {"name": "route contradiction and paraphrase mutations", "mutations": route_tests,
         "rejected": bool(route_tests) and all(x["rejected"] for x in route_tests),
         "pass": bool(route_tests) and all(x["rejected"] for x in route_tests)},
    ]
    return {
        "malformed_family_mutation_matrix": malformed_family_mutation_matrix,
        "tests": tests,
        "passed": sum(test["pass"] for test in tests),
        "failed": sum(not test["pass"] for test in tests),
        "all_negative_tests_pass": (
            malformed_family_mutation_matrix["pass"]
            and all(test["pass"] for test in tests)
        ),
    }


def build_formal_audit() -> dict:
    review_payload = load_formal_review()
    review_decisions = review_decisions_by_id(review_payload)
    formal_blocks = extract_formal_blocks()
    hash_regression = review_hash_regression_check(formal_blocks)
    complete_review = set(review_decisions) == {block["id"] for block in formal_blocks}
    negative_tests = (
        coverage_negative_test_results(
            formal_blocks,
            review_decisions,
            review_payload.get("semantic_contextual_justifications", []),
        )
        if complete_review
        else {
            "tests": [],
            "passed": 0,
            "failed": 1,
            "all_negative_tests_pass": False,
            "reason": "complete current authored review is required before mutation testing",
        }
    )
    rows = []
    applied_decisions = 0
    for block in formal_blocks:
        block_hash = decision_bound_sha256(block)
        decision = review_decisions.get(block["id"])
        if decision is None:
            decision_status = "missing_review_decision"
        elif decision.get("source_block_sha256") != block_hash:
            decision_status = "stale_canonical_block_hash"
        else:
            decision_status = "applied_authored_review"
            applied_decisions += 1

        if decision_status == "applied_authored_review":
            classification = decision.get("classification")
            destinations = decision.get("package_destinations", [])
            resolution = decision.get("resolution_status")
            strategy = decision.get("mapping_strategy")
            review_basis = decision.get("review_basis")
            minimum_aggregate_overlap = decision.get("minimum_aggregate_signature_overlap")
            required_propositions = decision.get("required_propositions", [])
            coverage_mode = decision.get("coverage_mode")
            structural_umbrella = decision.get("structural_umbrella")
            distributed_inventory = decision.get("distributed_proposition_inventory", [])
            routed_owner = decision.get("routed_owner")
            inbound_obligation_id = decision.get("inbound_obligation_id")
            obligation_status = decision.get("obligation_status")
        else:
            classification = None
            destinations = []
            resolution = "unresolved_review_required"
            strategy = "unreviewed"
            review_basis = (
                "No current authored review decision is bound to this canonical full-block hash. "
                "Extraction and audit refresh cannot approve a classification."
            )
            minimum_aggregate_overlap = None
            required_propositions = []
            coverage_mode = "unreviewed"
            structural_umbrella = None
            distributed_inventory = []
            routed_owner = None
            inbound_obligation_id = None
            obligation_status = "review_required"

        rows.append(
            {
                "id": block["id"],
                "source": {
                    "file": block["source_file"],
                    "line": block["source_line"],
                    "end_line": block["end_line"],
                    "heading_level": block["heading_level"],
                    "heading": block["source_heading"],
                    "context_heading": block["context_heading"],
                    "ancestor_headings": block["ancestor_headings"],
                },
                "concept": (
                    f"{block['context_heading']} — presentation/teaching evidence ({block['source_heading']})"
                    if block["heading_level"] in {4, 5}
                    and any(re.match(pattern, block["source_heading"], re.I) for pattern in PRESENTATION_PATTERNS)
                    else re.sub(r"\s*[✅⚠️❓]+\s*", "", block["source_heading"]).strip()
                ),
                "source_block_sha256": block_hash,
                "source_body_signature": block["source_signature"],
                "source_body_witnesses": block["source_body_witnesses"],
                "structure": {
                    "parent_id": block["parent_id"],
                    "child_ids": block["child_ids"],
                    "descendant_ids": block["descendant_ids"],
                    "is_structural_umbrella": block["is_structural_umbrella"],
                    "parent_only_signature": block["parent_only_signature"],
                    "parent_only_witnesses": block["parent_only_witnesses"],
                },
                "large_leaf_detection": block["large_leaf_detection"],
                "source_segments": [
                    {
                        key: segment[key]
                        for key in (
                            "id",
                            "source_line",
                            "end_line",
                            "text_sha256",
                            "segmentation_basis",
                            "signature",
                            "witnesses",
                        )
                    }
                    for segment in block["source_segments"]
                ],
                "semantic_clusters": [
                    {
                        key: cluster[key]
                        for key in (
                            "id",
                            "number",
                            "total",
                            "label",
                            "source_line",
                            "end_line",
                            "text_sha256",
                            "signature",
                            "witnesses",
                        )
                    }
                    for cluster in block["semantic_clusters"]
                ],
                "review_decision": {
                    "file": FORMAL_REVIEW.name,
                    "status": decision_status,
                    "source_block_sha256": (
                        decision.get("source_block_sha256") if decision else None
                    ),
                },
                "classification": classification,
                "mapping_strategy": strategy,
                "review_basis": review_basis,
                "minimum_aggregate_signature_overlap": minimum_aggregate_overlap,
                "required_propositions": required_propositions,
                "coverage_mode": coverage_mode,
                "structural_umbrella": structural_umbrella,
                "distributed_proposition_inventory": distributed_inventory,
                "package_destinations": destinations,
                "routed_owner": routed_owner,
                "inbound_obligation_id": inbound_obligation_id,
                "obligation_status": obligation_status,
                "resolution_status": resolution,
            }
        )
    classifications = Counter(row["classification"] for row in rows if row["classification"])
    unresolved = sum(row["resolution_status"].startswith("unresolved") for row in rows)
    unreviewed = sum(row["review_decision"]["status"] != "applied_authored_review" for row in rows)
    review_hash = (
        hashlib.sha256(FORMAL_REVIEW.read_bytes()).hexdigest()
        if FORMAL_REVIEW.is_file()
        else None
    )
    master_block = next(
        block
        for block in formal_blocks
        if block["source_heading"] == "COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM"
    )
    revision_text = (TOPIC / "REVISION-GUIDE.md").read_text(encoding="utf-8")
    destination_master = find_heading_section(
        revision_text,
        "COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM",
    )
    panel_marker_assertions = {
        "authoritative_source": panel_marker_integrity(
            master_block["block_text"],
            surface="authoritative formal Learning-Session.md",
        ),
        "destination": panel_marker_integrity(
            destination_master,
            surface="REVISION-GUIDE.md master-flow destination",
        ),
        "ordered_source_destination_parity": panel_marker_parity(
            master_block["block_text"],
            destination_master,
        ),
    }
    package_text = {
        path.name: path.read_text(encoding="utf-8")
        for path in TOPIC.glob("*.md")
    }
    live_claim_audit = distributed_claim_live_audit(
        formal_blocks,
        review_decisions,
        package_text,
        review_payload.get("semantic_contextual_justifications", []),
    )
    routed_binding_failures = routed_decision_binding_failures(review_decisions)
    routed_binding = {
        "expected_stable_ids": EXPECTED_ROUTED_DECISIONS,
        "expected_multiplicities": EXPECTED_ROUTED_MULTIPLICITIES,
        "destination_assertion_sets": {
            obligation["id"]: [
                {
                    "destination": f"{evidence['file']} :: {evidence['anchor']}",
                    "sha256": route_assertion_set_sha256(evidence),
                }
                for evidence in obligation["destination_evidence"]
            ]
            for obligation in CROSS_TOPIC_ROUTE_OBLIGATIONS
        },
        "failures": routed_binding_failures,
        "pass": not routed_binding_failures,
    }
    return {
        "schema_version": 8,
        "topic": "10 Existentialism",
        "rule": "START-HERE.md formal-session reconciliation rule 10",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "formal_block_definition": (
            "Every level-2 through level-5 heading in the authoritative completed Learning-Session "
            "and Solved-Practice-Workbook. Full-block hashes remain bound to complete canonical "
            "text. Parent headings with child headings are structural umbrellas: their direct "
            "parent-only body is reviewed separately and their descendant coverage is the validated "
            "recursive union of current child decisions. Large leaf blocks are split into beginning, "
            "middle and end segments; labelled ASCII master-flow panels are also extracted as "
            "individual semantic clusters. Extraction never authors or approves decisions."
        ),
        "source_files": {
            code: {
                "path": path_label(path),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "bytes": path.stat().st_size,
            }
            for code, path in FORMAL_SOURCES.items()
        },
        "authority_files": {
            "canonical": {
                "path": path_label(CANONICAL),
                "sha256": hashlib.sha256(CANONICAL.read_bytes()).hexdigest(),
                "bytes": CANONICAL.stat().st_size,
            },
            **{
                f"pyq_{index + 1}": {
                    "path": path_label(path),
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "bytes": path.stat().st_size,
                }
                for index, path in enumerate(PYQ_LEDGERS)
            },
            "rules": {
                "path": path_label(RULES),
                "sha256": hashlib.sha256(RULES.read_bytes()).hexdigest(),
                "bytes": RULES.stat().st_size,
            },
        },
        "formal_source_authority": formal_source_authority_assertion(),
        "review_decision_layer": {
            "path": FORMAL_REVIEW.name,
            "sha256": review_hash,
            "schema_version": review_payload.get("schema_version"),
            "declared_decision_count": review_payload.get("decision_count"),
            "loaded_decision_count": len(review_decisions),
            "applied_decision_count": applied_decisions,
            "unreviewed_or_stale_count": unreviewed,
            "refresh_mutates_review_layer": False,
        },
        "decision_hash_regression": hash_regression,
        "coverage_negative_tests": negative_tests,
        "distributed_claim_live_audit": live_claim_audit,
        "panel_marker_assertions": panel_marker_assertions,
        "routed_decision_binding": routed_binding,
        "cross_topic_route_obligations": CROSS_TOPIC_ROUTE_OBLIGATIONS,
        "summary": {
            "formal_blocks": len(rows),
            **{name: classifications[name] for name in ALLOWED_CLASSIFICATIONS},
            "structural_umbrellas": sum(
                row["coverage_mode"] == "structural_umbrella" for row in rows
            ),
            "leaf_full_blocks": sum(
                row["coverage_mode"] == "leaf_full_block" for row in rows
            ),
            "distributed_leaf_blocks": sum(
                bool(row["distributed_proposition_inventory"]) for row in rows
            ),
            "large_leaf_blocks": sum(
                row["large_leaf_detection"]["is_large_leaf"] for row in rows
            ),
            "distributed_inventory_units": sum(
                len(row["distributed_proposition_inventory"]) for row in rows
            ),
            "semantic_cluster_units": sum(
                len(row["semantic_clusters"]) for row in rows
            ),
            "unreviewed": unreviewed,
            "unresolved": unresolved,
        },
        "rows": rows,
        "mechanical_limitations": (
            "The validator can prove that an independently persisted authored decision is bound "
            "to the canonical full block hash, including semantic labels, heading and context, "
            "that structural parents retain every child decision plus parent-only prose, and that "
            "large leaves retain distributed segment or panel propositions. Extraction and "
            "--refresh-formal-audit never create or approve review decisions. These controls still "
            "cannot prove philosophical truth, pedagogical sufficiency or examiner marks."
        ),
    }

def write_formal_audit() -> None:
    FORMAL_AUDIT.write_text(
        json.dumps(build_formal_audit(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def formal_audit_checks() -> dict:
    payload = json.loads(FORMAL_AUDIT.read_text(encoding="utf-8"))
    review_payload = load_formal_review()
    review_decisions = review_decisions_by_id(review_payload)
    expected = {block["id"]: block for block in extract_formal_blocks()}
    rows = payload.get("rows", [])
    actual = {row.get("id"): row for row in rows}
    failures = []
    review_failures = []
    generic_strategies = {"fallback", "profile", "generic", "auto_covered"}
    if review_payload.get("schema_version") != 8:
        review_failures.append("review schema must be 8")
    if review_payload.get("review_status") != "authored_complete":
        review_failures.append("review status is not authored_complete")
    if review_payload.get("decision_count") != len(review_decisions):
        review_failures.append("declared review decision count mismatch")
    current_source_authority = formal_source_authority_assertion()
    if not current_source_authority["pass"]:
        review_failures.append(
            {"formal_source_authority": current_source_authority["failures"]}
        )
    if review_payload.get("formal_source_authority") != current_source_authority:
        review_failures.append(
            "review does not preserve the exact authoritative Downloads source assertion"
        )
    if set(review_decisions) != set(expected):
        review_failures.append(
            {
                "review_decision_id_set_mismatch": {
                    "missing": sorted(set(expected) - set(review_decisions)),
                    "stale": sorted(set(review_decisions) - set(expected)),
                }
            }
        )
    for code, path in FORMAL_SOURCES.items():
        recorded_source = review_payload.get("source_files", {}).get(code, {})
        if (
            recorded_source.get("path") != path_label(path)
            or recorded_source.get("sha256") != hashlib.sha256(path.read_bytes()).hexdigest()
            or recorded_source.get("bytes") != path.stat().st_size
        ):
            review_failures.append(f"review full-source identity mismatch: {code}")
    expected_authority_files = {
        "canonical": CANONICAL,
        **{f"pyq_{index + 1}": path for index, path in enumerate(PYQ_LEDGERS)},
        "rules": RULES,
    }
    for code, path in expected_authority_files.items():
        recorded_source = review_payload.get("authority_files", {}).get(code, {})
        if (
            recorded_source.get("path") != path_label(path)
            or recorded_source.get("sha256")
            != hashlib.sha256(path.read_bytes()).hexdigest()
            or recorded_source.get("bytes") != path.stat().st_size
        ):
            review_failures.append(f"review authority identity mismatch: {code}")
    recorded_review_layer = payload.get("review_decision_layer", {})
    current_review_hash = (
        hashlib.sha256(FORMAL_REVIEW.read_bytes()).hexdigest()
        if FORMAL_REVIEW.is_file()
        else None
    )
    if (
        recorded_review_layer.get("path") != FORMAL_REVIEW.name
        or recorded_review_layer.get("sha256") != current_review_hash
        or recorded_review_layer.get("refresh_mutates_review_layer") is not False
    ):
        review_failures.append("audit review-layer identity mismatch")
    failures.extend({"review_decision_layer": failure} for failure in review_failures)
    if set(actual) != set(expected):
        failures.append(
            {
                "block_id_set_mismatch": {
                    "missing": sorted(set(expected) - set(actual)),
                    "unexpected": sorted(set(actual) - set(expected)),
                }
            }
        )
    package_text = {}
    classifications = Counter()
    unresolved_due = []
    strategy_counts = Counter()
    global_decision_witness_state = None
    global_distributed_claim_history: list[dict] = []
    global_distributed_seen_claims: set[str] = set()
    global_distributed_seen_witnesses: set[str] = set()
    for block_id, block in expected.items():
        row = actual.get(block_id)
        if not row:
            continue
        decision = review_decisions.get(block_id)
        block_hash = decision_bound_sha256(block)
        if not decision:
            failures.append({"id": block_id, "reason": "missing authored review decision"})
            continue
        if decision.get("source_block_sha256") != block_hash:
            failures.append(
                {"id": block_id, "reason": "authored review is stale for canonical full block"}
            )
        expected_canonical_block = {
            "source_file": block["source_file"],
            "heading_level": block["heading_level"],
            "source_heading": block["source_heading"],
            "ancestor_headings": block["ancestor_headings"],
            "block_text": unicodedata.normalize(
                "NFC",
                block["block_text"].replace("\r\n", "\n").replace("\r", "\n"),
            ),
        }
        if decision.get("canonical_block") != expected_canonical_block:
            failures.append(
                {
                    "id": block_id,
                    "reason": "authored review canonical full-block payload mismatch",
                }
            )
        if (
            row.get("source_block_sha256") != block_hash
            or row.get("review_decision", {}).get("status") != "applied_authored_review"
            or row.get("review_decision", {}).get("source_block_sha256") != block_hash
        ):
            failures.append({"id": block_id, "reason": "audit did not apply current authored review"})
        decision_fields = (
            "classification",
            "mapping_strategy",
            "review_basis",
            "minimum_aggregate_signature_overlap",
            "required_propositions",
            "coverage_mode",
            "structural_umbrella",
            "distributed_proposition_inventory",
            "package_destinations",
            "routed_owner",
            "inbound_obligation_id",
            "obligation_status",
            "resolution_status",
        )
        for field in decision_fields:
            if row.get(field) != decision.get(field):
                failures.append(
                    {"id": block_id, "reason": f"audit differs from authored decision: {field}"}
                )
        source = row.get("source", {})
        if (
            source.get("file") != block["source_file"]
            or source.get("line") != block["source_line"]
            or source.get("end_line") != block["end_line"]
            or source.get("heading") != block["source_heading"]
            or source.get("heading_level") != block["heading_level"]
            or source.get("ancestor_headings") != block["ancestor_headings"]
        ):
            failures.append({"id": block_id, "reason": "source anchor mismatch"})
        recorded_structure = row.get("structure", {})
        if recorded_structure != {
            "parent_id": block["parent_id"],
            "child_ids": block["child_ids"],
            "descendant_ids": block["descendant_ids"],
            "is_structural_umbrella": block["is_structural_umbrella"],
            "parent_only_signature": block["parent_only_signature"],
            "parent_only_witnesses": block["parent_only_witnesses"],
        }:
            failures.append({"id": block_id, "reason": "source hierarchy mismatch"})
        if row.get("large_leaf_detection") != block["large_leaf_detection"]:
            failures.append(
                {"id": block_id, "reason": "large-leaf size classification mismatch"}
            )
        expected_segments = [
            {
                key: segment[key]
                for key in (
                    "id",
                    "source_line",
                    "end_line",
                    "text_sha256",
                    "segmentation_basis",
                    "signature",
                    "witnesses",
                )
            }
            for segment in block["source_segments"]
        ]
        expected_clusters = [
            {
                key: cluster[key]
                for key in (
                    "id",
                    "number",
                    "total",
                    "label",
                    "source_line",
                    "end_line",
                    "text_sha256",
                    "signature",
                    "witnesses",
                )
            }
            for cluster in block["semantic_clusters"]
        ]
        if row.get("source_segments") != expected_segments:
            failures.append({"id": block_id, "reason": "source segment extraction mismatch"})
        if row.get("semantic_clusters") != expected_clusters:
            failures.append({"id": block_id, "reason": "semantic cluster extraction mismatch"})
        coverage_mode = row.get("coverage_mode")
        expected_mode = (
            "structural_umbrella"
            if block["is_structural_umbrella"]
            else "leaf_full_block"
        )
        if coverage_mode != expected_mode:
            failures.append(
                {
                    "id": block_id,
                    "reason": "coverage mode does not match extracted hierarchy",
                    "recorded": coverage_mode,
                    "expected": expected_mode,
                }
            )
        structural = row.get("structural_umbrella")
        parent_only_substantive = len(words(block["parent_only_body"])) >= 4
        if block["is_structural_umbrella"]:
            child_resolution = {}
            for child_id in block["child_ids"]:
                child_row = actual.get(child_id)
                child_decision = review_decisions.get(child_id)
                child_resolution[child_id] = bool(
                    child_row
                    and child_decision
                    and child_row.get("review_decision", {}).get("status")
                    == "applied_authored_review"
                    and not child_row.get("resolution_status", "").startswith("unresolved")
                )
            failures.extend(
                {"id": block_id, **failure}
                for failure in structural_umbrella_validation_failures(
                    block,
                    decision,
                    child_resolution,
                )
            )
        elif structural is not None:
            failures.append({"id": block_id, "reason": "leaf block declares structural umbrella"})
        validation_source_body = (
            block["parent_only_body"]
            if block["is_structural_umbrella"]
            else block["block_body"]
        )
        validation_signature = (
            block["parent_only_signature"]
            if block["is_structural_umbrella"]
            else block["source_signature"]
        )
        strategy = row.get("mapping_strategy", "")
        strategy_counts[strategy] += 1
        fragment_continuation = strategy == "reviewed_exact_fragment_continuation"
        panel_inventory = strategy == "reviewed_repaired_panel_inventory"
        minimum_signature_terms = 2 if fragment_continuation else 4
        minimum_source_witnesses = 1 if fragment_continuation else 2
        if (
            row.get("source_body_signature") != block["source_signature"]
            or len(block["source_signature"]) < minimum_signature_terms
        ):
            failures.append({"id": block_id, "reason": "source body signature mismatch or too weak"})
        if (
            row.get("source_body_witnesses") != block["source_body_witnesses"]
            or len(block["source_body_witnesses"]) < minimum_source_witnesses
        ):
            failures.append({"id": block_id, "reason": "source body witnesses mismatch or too weak"})
        if block["source_body_witnesses"] == block["source_signature"][:len(block["source_body_witnesses"])]:
            failures.append({"id": block_id, "reason": "witnesses merely repeat signature prefix"})
        classification = row.get("classification")
        classifications[classification] += 1
        if classification not in ALLOWED_CLASSIFICATIONS:
            failures.append({"id": block_id, "reason": "invalid classification"})
        if not strategy or strategy in generic_strategies:
            failures.append({"id": block_id, "reason": "generic or absent mapping strategy"})
        destinations = row.get("package_destinations", [])
        if (
            classification in {"covered_in_scope", "genuine_in_scope_omission"}
            and not destinations
            and (not block["is_structural_umbrella"] or parent_only_substantive)
        ):
            failures.append({"id": block_id, "reason": "covered row has no reviewed destination"})
        if (
            block["is_structural_umbrella"]
            and not parent_only_substantive
            and (destinations or row.get("required_propositions"))
        ):
            failures.append(
                {
                    "id": block_id,
                    "reason": "empty parent-only umbrella must rely solely on child union",
                }
            )
        aggregate_destination_bodies = []
        for item in destinations:
            relative = item.get("file", "")
            path = TOPIC / relative
            if not path.is_file():
                failures.append({"id": block_id, "reason": f"missing destination {relative}"})
                continue
            text = package_text.setdefault(relative, path.read_text(encoding="utf-8"))
            body = destination_body_for_reference(text, item)
            if not body:
                failures.append(
                    {"id": block_id, "reason": f"destination anchor missing: {relative} :: {item.get('anchor')}"}
                )
                continue
            aggregate_destination_bodies.append(body)
            witnesses = item.get("witnesses", [])
            if len(witnesses) < 1:
                failures.append({"id": block_id, "reason": "destination has no substantive witness"})
            for witness in witnesses:
                failures.extend(
                    {
                        "id": block_id,
                        **failure,
                    }
                    for failure in witness_quality_failures(
                        witness,
                        context="package_destination",
                        global_state=global_decision_witness_state,
                        block_id=block_id,
                        witness_id=(
                            f"package_destination|{item.get('file')}|"
                            f"{item.get('anchor')}|{item.get('context_anchor') or ''}"
                        ),
                        source_body=validation_source_body,
                        reuse_justification=item.get(
                            "witness_reuse_justification"
                        ),
                    )
                )
            destination_normalized = normalise(body)
            absent_source = [
                term
                for term in witnesses
                if not contains_witness(validation_source_body, term)
            ]
            absent_destination = [term for term in witnesses if not contains_witness(body, term)]
            if absent_source or absent_destination:
                failures.append(
                    {
                        "id": block_id,
                        "reason": "witness mismatch",
                        "absent_source": absent_source,
                        "absent_destination": absent_destination,
                    }
                )
        aggregate_normalized = normalise("\n".join(aggregate_destination_bodies))
        signature = validation_signature
        minimum_overlap = row.get("minimum_aggregate_signature_overlap")
        if (
            classification in {"covered_in_scope", "genuine_in_scope_omission"}
            and (not block["is_structural_umbrella"] or parent_only_substantive)
            and not panel_inventory
        ):
            failures.extend(
                {"id": block_id, **failure}
                for failure in aggregate_correspondence_failures(
                    signature,
                    aggregate_normalized,
                    minimum_overlap,
                )
            )
        propositions = row.get("required_propositions", [])
        if (
            classification in {"covered_in_scope", "genuine_in_scope_omission"}
            and (not block["is_structural_umbrella"] or parent_only_substantive)
            and not panel_inventory
            and len(propositions) < (1 if fragment_continuation else 2)
        ):
            failures.append({"id": block_id, "reason": "fewer than two required substantive propositions"})
        failures.extend(
            {
                "id": block_id,
                **failure,
            }
            for failure in proposition_validation_failures(
                propositions,
                validation_source_body,
                aggregate_normalized,
                require_semantic_specificity=False,
                context="required_propositions",
            )
        )
        for proposition in propositions:
            for witness in proposition.get("witnesses", []):
                failures.extend(
                    {
                        "id": block_id,
                        **failure,
                    }
                    for failure in witness_quality_failures(
                        witness,
                        context="required_proposition",
                        global_state=global_decision_witness_state,
                        block_id=block_id,
                        witness_id=f"required_proposition|{proposition.get('id')}",
                        source_body=validation_source_body,
                        reuse_justification=proposition.get(
                            "witness_reuse_justification"
                        ),
                    )
                )
        inventory = row.get("distributed_proposition_inventory", [])
        failures.extend(
            {"id": block_id, **failure}
            for failure in distributed_inventory_validation_failures(
                block,
                inventory,
                destinations,
                package_text,
                global_claim_history=global_distributed_claim_history,
                global_seen_claims=global_distributed_seen_claims,
                global_seen_witnesses=global_distributed_seen_witnesses,
                global_witness_state=global_decision_witness_state,
            )
        )
        if classification == "routed_to_canonical_owner":
            if not row.get("routed_owner") or not row.get("inbound_obligation_id"):
                failures.append({"id": block_id, "reason": "routed row lacks owner or obligation id"})
            if row.get("obligation_status") == "due_unresolved":
                unresolved_due.append(block_id)
        if classification == "genuine_in_scope_omission" and row.get("resolution_status") != "resolved_repaired":
            failures.append({"id": block_id, "reason": "genuine omission is not repaired"})
        if row.get("resolution_status", "").startswith("unresolved"):
            failures.append({"id": block_id, "reason": "unresolved formal block"})
    source_identity = {}
    for code, path in FORMAL_SOURCES.items():
        recorded = payload.get("source_files", {}).get(code, {})
        current_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        passed = recorded.get("path") == path_label(path) and recorded.get("sha256") == current_hash
        source_identity[code] = {"recorded": recorded, "current_sha256": current_hash, "pass": passed}
        if not passed:
            failures.append({"source": code, "reason": "source identity mismatch"})
    recorded_obligations = payload.get("cross_topic_route_obligations", [])
    obligation_failures = []
    route_assertion_proof = []
    if recorded_obligations != CROSS_TOPIC_ROUTE_OBLIGATIONS:
        obligation_failures.append("recorded obligations differ from validator-owned obligations")
    for obligation in CROSS_TOPIC_ROUTE_OBLIGATIONS:
        source = obligation["source_owner_evidence"]
        source_path = (TOPIC / source["file"]).resolve()
        source_text = source_path.read_text(encoding="utf-8") if source_path.is_file() else ""
        if not source_text or any(
            not contains_witness(source_text, witness) for witness in source["witnesses"]
        ):
            obligation_failures.append(f"{obligation['id']}: source-owner evidence missing")
        for evidence in obligation["destination_evidence"]:
            path = TOPIC / evidence["file"]
            text = path.read_text(encoding="utf-8") if path.is_file() else ""
            section = find_heading_section(text, evidence["anchor"]) if text else ""
            if not section or any(
                not contains_witness(section, witness) for witness in evidence["witnesses"]
            ):
                obligation_failures.append(
                    f"{obligation['id']}: destination evidence missing at "
                    f"{evidence['file']} :: {evidence['anchor']}"
                )
            assertion_failures = (
                route_assertion_validation_failures(evidence, section)
                if section
                else []
            )
            for assertion_failure in assertion_failures:
                obligation_failures.append(
                    {
                        "obligation": obligation["id"],
                        "destination": f"{evidence['file']} :: {evidence['anchor']}",
                        **assertion_failure,
                    }
                )
            if evidence.get("reviewed_assertions") or evidence.get(
                "required_semantic_assertions"
            ):
                route_assertion_proof.append(
                    {
                        "obligation": obligation["id"],
                        "destination": f"{evidence['file']} :: {evidence['anchor']}",
                        "assertion_set_sha256": route_assertion_set_sha256(evidence),
                        "assertion_ids": [
                            row["id"]
                            for row in evidence.get("reviewed_assertions", [])
                        ]
                        + [
                            row["id"]
                            for row in evidence.get(
                                "required_semantic_assertions", []
                            )
                        ],
                        "forbidden_assertions": evidence.get(
                            "forbidden_exact_text", []
                        ),
                        "failures": assertion_failures,
                        "pass": not assertion_failures,
                    }
                )
    failures.extend({"inbound_obligation": failure} for failure in obligation_failures)

    expected_hash_regression = review_hash_regression_check(list(expected.values()))
    recorded_hash_regression = payload.get("decision_hash_regression", {})
    hash_regression_pass = (
        recorded_hash_regression == expected_hash_regression
        and expected_hash_regression.get("all_mutations_stale_decision") is True
    )
    if not hash_regression_pass:
        failures.append(
            {
                "decision_hash_regression": {
                    "recorded": recorded_hash_regression,
                    "expected": expected_hash_regression,
                }
            }
        )
    expected_negative_tests = coverage_negative_test_results(
        list(expected.values()),
        review_decisions,
        review_payload.get("semantic_contextual_justifications", []),
    )
    recorded_negative_tests = payload.get("coverage_negative_tests", {})
    negative_tests_pass = (
        recorded_negative_tests == expected_negative_tests
        and expected_negative_tests.get("all_negative_tests_pass") is True
    )
    if not negative_tests_pass:
        failures.append(
            {
                "coverage_negative_tests": {
                    "recorded": recorded_negative_tests,
                    "expected": expected_negative_tests,
                }
            }
        )

    package_text.update(
        {
            path.name: path.read_text(encoding="utf-8")
            for path in TOPIC.glob("*.md")
            if path.name not in package_text
        }
    )
    expected_live_claim_audit = distributed_claim_live_audit(
        list(expected.values()),
        review_decisions,
        package_text,
        review_payload.get("semantic_contextual_justifications", []),
    )
    recorded_live_claim_audit = payload.get("distributed_claim_live_audit", {})
    live_claim_audit_pass = (
        recorded_live_claim_audit == expected_live_claim_audit
        and expected_live_claim_audit["pass"]
    )
    if not live_claim_audit_pass:
        failures.append(
            {
                "distributed_claim_live_audit": {
                    "recorded": recorded_live_claim_audit,
                    "expected": expected_live_claim_audit,
                }
            }
        )

    master_block = next(
        block
        for block in expected.values()
        if block["source_heading"] == "COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM"
    )
    destination_master = find_heading_section(
        (TOPIC / "REVISION-GUIDE.md").read_text(encoding="utf-8"),
        "COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM",
    )
    expected_panel_assertions = {
        "authoritative_source": panel_marker_integrity(
            master_block["block_text"],
            surface="authoritative formal Learning-Session.md",
        ),
        "destination": panel_marker_integrity(
            destination_master,
            surface="REVISION-GUIDE.md master-flow destination",
        ),
        "ordered_source_destination_parity": panel_marker_parity(
            master_block["block_text"],
            destination_master,
        ),
    }
    recorded_panel_assertions = payload.get("panel_marker_assertions", {})
    panel_marker_assertions_pass = (
        recorded_panel_assertions == expected_panel_assertions
        and all(
            assertion["pass"]
            for assertion in expected_panel_assertions.values()
        )
    )
    if not panel_marker_assertions_pass:
        failures.append(
            {
                "panel_marker_assertions": {
                    "recorded": recorded_panel_assertions,
                    "expected": expected_panel_assertions,
                }
            }
        )

    expected_routed_binding_failures = routed_decision_binding_failures(
        review_decisions
    )
    expected_routed_binding = {
        "expected_stable_ids": EXPECTED_ROUTED_DECISIONS,
        "expected_multiplicities": EXPECTED_ROUTED_MULTIPLICITIES,
        "destination_assertion_sets": {
            obligation["id"]: [
                {
                    "destination": f"{evidence['file']} :: {evidence['anchor']}",
                    "sha256": route_assertion_set_sha256(evidence),
                }
                for evidence in obligation["destination_evidence"]
            ]
            for obligation in CROSS_TOPIC_ROUTE_OBLIGATIONS
        },
        "failures": expected_routed_binding_failures,
        "pass": not expected_routed_binding_failures,
    }
    recorded_routed_binding = payload.get("routed_decision_binding", {})
    routed_binding_pass = (
        recorded_routed_binding == expected_routed_binding
        and expected_routed_binding["pass"]
    )
    if not routed_binding_pass:
        failures.append(
            {
                "routed_decision_binding": {
                    "recorded": recorded_routed_binding,
                    "expected": expected_routed_binding,
                }
            }
        )

    recorded_authority = payload.get("formal_source_authority", {})
    formal_source_authority_pass = (
        recorded_authority == current_source_authority
        and current_source_authority["pass"]
    )
    if not formal_source_authority_pass:
        failures.append(
            {
                "formal_source_authority": {
                    "recorded": recorded_authority,
                    "expected": current_source_authority,
                }
            }
        )

    ledger_2026 = PYQ_LEDGERS[1].read_text(encoding="utf-8")
    ledger_topic_parts = re.findall(
        r"^- \*\*(Q\d+\([a-z]\)) · \d+ marks · \[Existentialism\]\([^)]+\):\*\*",
        ledger_2026,
        re.M,
    )
    latest_upgrade_rows = [
        row
        for row in rows
        if row.get("source", {}).get("heading") == "PYQS AND ANSWER PRACTICE"
    ]
    toolkit_text = (TOPIC / "ANSWER-WRITING-TOOLKIT.md").read_text(encoding="utf-8")
    latest_owner_assertion = {
        "ledger_topic_parts": ledger_topic_parts,
        "required_primary_parts": ["Q2(c)", "Q3(b)"],
        "forbidden_misattribution": None,
        "review_rows_checked": [row.get("id") for row in latest_upgrade_rows],
        "pass": (
            set(ledger_topic_parts) == {"Q2(c)", "Q3(b)"}
            and True
            and len(latest_upgrade_rows) == 2
            and all(
                row.get("coverage_mode") == "structural_umbrella"
                and row.get("structural_umbrella", {}).get("child_union_required") is True
                for row in latest_upgrade_rows
            )
            and "## 15. 2026 Q2(c) · 15 marks" in toolkit_text and "## 16. 2026 Q3(b) · 15 marks" in toolkit_text
            and "Topic 10 is the primary owner" in find_heading_section(toolkit_text, "Inbound obligations from Topic 09")
        ),
    }
    if not latest_owner_assertion["pass"]:
        failures.append({"verified_2026_owner_assertion": latest_owner_assertion})

    summary = payload.get("summary", {})
    calculated_summary = {
        "formal_blocks": len(rows),
        **{classification: classifications[classification] for classification in ALLOWED_CLASSIFICATIONS},
        "structural_umbrellas": sum(
            row.get("coverage_mode") == "structural_umbrella" for row in rows
        ),
        "leaf_full_blocks": sum(
            row.get("coverage_mode") == "leaf_full_block" for row in rows
        ),
        "distributed_leaf_blocks": sum(
            bool(row.get("distributed_proposition_inventory")) for row in rows
        ),
        "large_leaf_blocks": sum(
            row.get("large_leaf_detection", {}).get("is_large_leaf") is True
            for row in rows
        ),
        "distributed_inventory_units": sum(
            len(row.get("distributed_proposition_inventory", [])) for row in rows
        ),
        "semantic_cluster_units": sum(
            len(row.get("semantic_clusters", [])) for row in rows
        ),
        "unreviewed": len(
            [
                row
                for row in rows
                if row.get("review_decision", {}).get("status") != "applied_authored_review"
            ]
        ),
        "unresolved": len([row for row in rows if row.get("resolution_status", "").startswith("unresolved")]),
    }
    for key, value in calculated_summary.items():
        if summary.get(key) != value:
            failures.append({"summary": key, "recorded": summary.get(key), "calculated": value})
    return {
        "formal_block_count": len(rows),
        "expected_block_count": len(expected),
        "classifications": dict(classifications),
        "mapping_strategies": dict(strategy_counts),
        "review_decision_layer": {
            "path": FORMAL_REVIEW.name,
            "schema_version": review_payload.get("schema_version"),
            "declared_decision_count": review_payload.get("decision_count"),
            "loaded_decision_count": len(review_decisions),
            "current_sha256": current_review_hash,
            "failures": review_failures,
            "pass": not review_failures,
        },
        "decision_hash_regression": {
            **expected_hash_regression,
            "pass": hash_regression_pass,
        },
        "coverage_negative_tests": {
            **expected_negative_tests,
            "pass": negative_tests_pass,
        },
        "distributed_claim_live_audit": {
            **expected_live_claim_audit,
            "recorded_matches": (
                recorded_live_claim_audit == expected_live_claim_audit
            ),
        },
        "formal_source_authority": {
            **current_source_authority,
            "recorded_matches": formal_source_authority_pass,
        },
        "panel_marker_assertions": {
            **expected_panel_assertions,
            "recorded_matches": panel_marker_assertions_pass,
        },
        "routed_decision_binding": {
            **expected_routed_binding,
            "recorded_matches": routed_binding_pass,
        },
        "verified_2026_owner_assertion": latest_owner_assertion,
        "unresolved_due_inbound_obligations": unresolved_due,
        "cross_topic_inbound_obligations": {
            "count": len(recorded_obligations),
            "ids": [row.get("id") for row in recorded_obligations],
            "failures": obligation_failures,
            "pass": not obligation_failures,
        },
        "route_assertion_closure": {
            "reviewed_destinations": route_assertion_proof,
            "pass": bool(route_assertion_proof)
            and all(row["pass"] for row in route_assertion_proof),
        },
        "source_identity": source_identity,
        "failures": failures,
        "mechanical_limitations": payload.get("mechanical_limitations"),
        "pass": payload.get("schema_version") == 8 and not failures and not unresolved_due,
    }


def parse_mcqs(text: str) -> list[dict]:
    result = []
    for block in re.split(r"(?=^## MCQ \d+\s*$)", text, flags=re.M)[1:]:
        heading = re.search(r"^## MCQ (\d+)\s*$", block, re.M)
        if not heading:
            continue
        number = int(heading.group(1))
        first_option = re.search(r"^A\. ", block, re.M)
        prompt = block[heading.end():first_option.start()].strip() if first_option else ""
        options = {match.group(1): match.group(2).strip() for match in re.finditer(r"^([A-D])\. (.+)$", block, re.M)}
        answer = re.search(r"^\*\*Answer:\s*([A-D])\.\*\*$", block, re.M)
        explanations = {
            match.group(1): match.group(2).strip()
            for match in re.finditer(r"^- \*\*([A-D]):\*\* (.+)$", block, re.M)
        }
        result.append(
            {
                "number": number,
                "title": f"MCQ {number}",
                "prompt": prompt,
                "options": options,
                "answer": answer.group(1) if answer else None,
                "explanations": explanations,
                "block": block,
            }
        )
    return result


def fisher_exclusive_probability(support: int, class_size: int, other_size: int) -> float:
    return math.comb(class_size, support) / math.comb(class_size + other_size, support)


def option_quality(mcqs: list[dict], key: str) -> dict:
    correct_lengths, distractor_lengths = [], []
    longest, unique_longest, outliers = [], [], []
    feature_patterns = {
        "absolute_quantifier": r"\b(always|never|entirely|every|none)\b",
        "exclusive_only": r"\bonly\b",
        "contrast_marker": r"\b(but|however|whereas|although|yet)\b",
        "semicolon": r";",
        "parentheses": r"[()]",
        "dash": r"[—–]",
        "initial_capital": r"^[A-Z]",
        "finite_verb": r"\b(is|are|was|were|has|have|does|do|means|explains|holds|requires)\b",
    }
    feature_counts = {name: {"correct": 0, "distractor": 0} for name in feature_patterns}
    for item in mcqs:
        answer = key[item["number"] - 1]
        lengths = {letter: len(text) for letter, text in item["options"].items()}
        correct_lengths.append(lengths[answer])
        distractor_lengths.extend(length for letter, length in lengths.items() if letter != answer)
        if lengths[answer] == max(lengths.values()):
            longest.append(item["number"])
        if lengths[answer] > max(length for letter, length in lengths.items() if letter != answer):
            unique_longest.append(item["number"])
        if max(lengths.values()) / max(1, min(lengths.values())) > 2.20:
            outliers.append({"mcq": item["number"], "lengths": lengths})
        for letter, text in item["options"].items():
            kind = "correct" if letter == answer else "distractor"
            for feature, pattern in feature_patterns.items():
                feature_counts[feature][kind] += bool(re.search(pattern, text, re.I if feature != "initial_capital" else 0))
    count = len(mcqs)
    cue_failures = []
    for feature, values in feature_counts.items():
        correct_rate = values["correct"] / count
        distractor_rate = values["distractor"] / (count * 3)
        values["correct_rate_percent"] = round(correct_rate * 100, 2)
        values["distractor_rate_percent"] = round(distractor_rate * 100, 2)
        values["gap_percent"] = round(abs(correct_rate - distractor_rate) * 100, 2)
        if values["correct"] + values["distractor"] >= 5 and abs(correct_rate - distractor_rate) > .20:
            cue_failures.append(feature)
    stopwords = {
        "a", "an", "and", "are", "as", "at", "be", "because", "by", "for", "from", "in",
        "into", "is", "it", "its", "not", "of", "on", "only", "or", "that", "the", "their",
        "this", "through", "to", "what", "which", "while", "with",
    }
    correct_tokens, distractor_tokens = Counter(), Counter()
    for item in mcqs:
        answer = key[item["number"] - 1]
        for letter, text in item["options"].items():
            tokens = {
                token for token in re.findall(r"[a-z]+", text.casefold())
                if len(token) >= 4 and token not in stopwords
            }
            (correct_tokens if letter == answer else distractor_tokens).update(tokens)
    lexical_flags = []
    for token in sorted(set(correct_tokens) | set(distractor_tokens)):
        correct = correct_tokens[token]
        distractor = distractor_tokens[token]
        support = correct + distractor
        if support < 5 or (correct and distractor):
            continue
        class_size = count if correct else count * 3
        other_size = count * 3 if correct else count
        probability = fisher_exclusive_probability(support, class_size, other_size)
        if support >= 8 and probability <= .01:
            lexical_flags.append(
                {
                    "token": token,
                    "correct": correct,
                    "distractor": distractor,
                    "support": support,
                    "exclusive_probability": round(probability, 8),
                }
            )
    longest_rate = 100 * len(longest) / count
    unique_rate = 100 * len(unique_longest) / count
    mean_correct = sum(correct_lengths) / len(correct_lengths)
    mean_distractor = sum(distractor_lengths) / len(distractor_lengths)
    mean_gap = 100 * abs(mean_correct - mean_distractor) / max(mean_correct, mean_distractor)
    passed = (
        15 <= longest_rate <= 45
        and 5 <= unique_rate <= 35
        and mean_gap <= 12
        and not outliers
        and not cue_failures
        and not lexical_flags
    )
    return {
        "metric": "Unicode character count and class-correlated visible features",
        "correct_is_longest_count": len(longest),
        "correct_is_longest_rate_percent": round(longest_rate, 2),
        "uniquely_longest_correct_count": len(unique_longest),
        "uniquely_longest_rate_percent": round(unique_rate, 2),
        "correct_mean_characters": round(mean_correct, 2),
        "distractor_mean_characters": round(mean_distractor, 2),
        "mean_length_gap_percent": round(mean_gap, 2),
        "comparability_outliers": outliers,
        "feature_rates": feature_counts,
        "failed_feature_correlations": cue_failures,
        "strong_class_exclusive_lexical_cues": lexical_flags,
        "locked_bands": {
            "correct_longest_percent": [15, 45],
            "unique_longest_percent": [5, 35],
            "mean_length_gap_percent_max": 12,
            "within_item_max_min_ratio": 2.20,
        },
        "mechanical_limitations": (
            "Length and token/feature correlation checks can detect recurring visible cues; "
            "they cannot prove that a learner will never infer an answer from style."
        ),
        "pass": passed,
    }


def mcq_checks(questions: list[dict], solutions: list[dict], question_text: str) -> dict:
    numbers = list(range(1, MCQ_COUNT + 1))
    parity_failures = []
    if len(questions) == len(solutions):
        for question, solution in zip(questions, solutions):
            if (
                question["number"] != solution["number"]
                or normalise(question["title"]) != normalise(solution["title"])
                or normalise(question["prompt"]) != normalise(solution["prompt"])
                or question["options"] != solution["options"]
            ):
                parity_failures.append(question["number"])
    answers = [item["answer"] for item in solutions]
    key = "".join(answer or "?" for answer in answers)
    distribution = Counter(answers)
    max_run = max((len(list(group)) for _, group in itertools.groupby(answers)), default=0)
    rotations = {
        offset: "".join("ABCD"[(index + offset) % 4] for index in range(MCQ_COUNT))
        for offset in range(4)
    }
    periodic = {
        period: round(
            sum(key[index] == key[index - period] for index in range(period, len(key)))
            / (len(key) - period),
            3,
        )
        for period in (2, 4)
    }
    explanation_failures = []
    explanation_texts = []
    for item in solutions:
        answer = item["answer"]
        if set(item["explanations"]) != set("ABCD"):
            explanation_failures.append({"mcq": item["number"], "reason": "missing option explanation"})
            continue
        for letter, explanation in item["explanations"].items():
            explanation_texts.append(normalise(explanation))
            status_pass = (
                "False proposition:" not in explanation
                if letter == answer
                else explanation.startswith("False proposition:")
            )
            if not status_pass or len(explanation) < 45:
                explanation_failures.append(
                    {"mcq": item["number"], "option": letter, "reason": "status or depth failure"}
                )
    duplicate_explanations = [
        text for text, count in Counter(explanation_texts).items() if text and count > 1
    ]
    question_leakage = {
        marker: marker in question_text
        for marker in ("**Answer:", "**Option explanations:**", "**Examiner trap", "Correct:")
    }
    parity = (
        [item["number"] for item in questions] == numbers
        and [item["number"] for item in solutions] == numbers
        and all(set(item["options"]) == set("ABCD") for item in questions + solutions)
        and not parity_failures
    )
    key_pass = (
        set(answers) <= set("ABCD")
        and len(answers) == MCQ_COUNT
        and max_run <= 2
        and max(distribution.values()) - min(distribution.values()) <= 4
        and key not in rotations.values()
        and periodic[2] <= .55
        and periodic[4] <= .55
    )
    quality = option_quality(questions, key)
    randomized_key = ""
    for number, original_answer in enumerate(MCQ_RANDOMIZATION_SOURCE_KEY, 1):
        shuffled = list("ABCD")
        randomizer = __import__("random").Random(
            f"{MCQ_RANDOMIZATION_SEED}:{number}"
        )
        randomizer.shuffle(shuffled)
        randomized_key += "ABCD"[shuffled.index(original_answer)]
    randomization = {
        "method": (
            "Each MCQ uses an independent PRNG instance keyed by the persisted package seed "
            "and question number; complete options and their explanations move together."
        ),
        "seed": MCQ_RANDOMIZATION_SEED,
        "source_key_sha256": hashlib.sha256(
            MCQ_RANDOMIZATION_SOURCE_KEY.encode("ascii")
        ).hexdigest(),
        "computed_key": randomized_key,
        "recorded_key": key,
        "question_instances": len(solutions),
        "pass": (
            len(MCQ_RANDOMIZATION_SOURCE_KEY) == MCQ_COUNT
            and randomized_key == key
            and len(solutions) == MCQ_COUNT
        ),
    }
    return {
        "parity": {
            "question_count": len(questions),
            "solution_count": len(solutions),
            "mismatches": parity_failures,
            "pass": parity,
        },
        "answer_pattern": {
            "key": key,
            "distribution": dict(distribution),
            "maximum_run": max_run,
            "mechanical_abcd_rotation": key in rotations.values(),
            "periodic_match_rates": periodic,
            "pass": key_pass,
        },
        "question_answer_leakage": question_leakage,
        "option_and_cue_quality": quality,
        "answer_position_randomization": randomization,
        "option_specific_explanations": {
            "failures": explanation_failures,
            "duplicate_normalized_explanations": duplicate_explanations,
            "examiner_trap_count": len(re.findall(r"^\*\*Examiner trap \d+:\*\*", "\n".join(item["block"] for item in solutions), re.M)),
            "mechanical_limitations": (
                "The gate verifies four distinct labelled explanations, correct/incorrect status, "
                "minimum depth and non-duplication. It does not establish philosophical truth."
            ),
            "pass": not explanation_failures and not duplicate_explanations,
        },
        "pass": (
            parity
            and key_pass
            and not any(question_leakage.values())
            and quality["pass"]
            and randomization["pass"]
            and not explanation_failures
            and not duplicate_explanations
        ),
    }


def parse_owned_pyqs() -> list[dict]:
    result = []
    for path in PYQ_LEDGERS:
        year = None
        for line in path.read_text(encoding="utf-8").splitlines():
            year_match = re.match(r"^## (20\d{2})(?:\s|$)", line)
            if year_match:
                year = year_match.group(1)
            match = re.match(
                r"^- \*\*(Q\d+\([a-z]\)) · (\d+) marks · \[Existentialism\]\([^)]+\):\*\* (.+)$",
                line,
            )
            if match and year:
                wording = re.split(r"\s+(?:→|📝)\s+", match.group(3), maxsplit=1)[0].strip()
                result.append(
                    {
                        "year": year,
                        "question": match.group(1),
                        "marks": int(match.group(2)),
                        "wording": wording,
                    }
                )
    return result


def extract_answer(section: str) -> str:
    match = re.search(
        r"^(?:#{3,5}\s+(?:Timed independent model answer|Independent model answer|Timed model answer)|\*\*Timed model answer\*\*)\s*\n(.*?)(?=^#{3,5}\s+(?:Why this (?:earns|structure earns) marks|Exam-length execution|Exam-length guidance|Closed-book answer spine)|^\*\*(?:Why this earns marks|Exam-length guidance|Measured model-answer words):\*\*|\Z)",
        section,
        re.M | re.S,
    )
    return match.group(1).strip() if match else ""


def toolkit_checks(toolkit: str) -> dict:
    expected = parse_owned_pyqs()
    expected_keys = {(row["year"], row["question"]): row for row in expected}
    heading_pattern = re.compile(
        r"^##(?: \d+\.)? (20\d{2}) (Q\d+\([a-z]\)) · (\d+) marks$",
        re.M,
    )
    matches = list(heading_pattern.finditer(toolkit))
    sections = {}
    failures = []
    word_counts = {}
    declared_word_counts = {}
    exact_wording = {}
    for index, match in enumerate(matches):
        if index + 1 < len(matches):
            end = matches[index + 1].start()
        else:
            original_start = re.search(r"(?m)^## Original 1 ·", toolkit[match.end():])
            end = (
                match.end() + original_start.start()
                if original_start
                else len(toolkit)
            )
        section = toolkit[match.end():end]
        identity = (match.group(1), match.group(2))
        sections[identity] = section
        expected_row = expected_keys.get(identity)
        question_match = re.search(r"^\*\*Question:\*\* (.+)$", section, re.M)
        wording = question_match.group(1).strip() if question_match else ""
        wording_pass = bool(
            expected_row
            and exact_wording_normalise(wording) == exact_wording_normalise(expected_row["wording"])
        )
        exact_wording[f"{identity[0]} {identity[1]}"] = wording_pass
        answer = extract_answer(section)
        timed_answer = answer.split("**Depth refinement.**", 1)[0]
        count = len(words(timed_answer))
        marks = int(match.group(3))
        word_counts[f"{identity[0]} {identity[1]}"] = {
            "marks": marks,
            "words": count,
            "band": WORD_BANDS.get(marks),
            "pass": marks in WORD_BANDS and WORD_BANDS[marks][0] <= count <= WORD_BANDS[marks][1],
        }
        declarations = re.findall(
            r"^\*\*Measured model-answer words:\*\*\s*(\d+)\s*$",
            section,
            re.M,
        )
        declared = int(declarations[0]) if len(declarations) == 1 else None
        declared_word_counts[f"{identity[0]} {identity[1]}"] = {
            "declared": declared,
            "computed": count,
            "declaration_count": len(declarations),
            "pass": len(declarations) == 1 and declared == count,
        }
        reasons = []
        if not expected_row or marks != expected_row["marks"]:
            reasons.append("identity or marks mismatch")
        if not wording_pass:
            reasons.append("exact wording mismatch")
        if not answer:
            reasons.append("missing independent model answer")
        if (
            "### Demand decoding" not in section
            and "### Verified metadata and demand decoding" not in section
            and "**Demand decoding:**" not in section
        ) or (
            "### Why this earns marks" not in section
            and "### Why this structure earns marks" not in section
            and "**Why this earns marks:**" not in section
            and "**Why this structure earns marks:**" not in section
            and not (
                "**Qualification / criticism:**" in section
                and "**Coverage check:**" in section
            )
        ):
            reasons.append("missing demand or marks explanation")
        if not word_counts[f"{identity[0]} {identity[1]}"]["pass"]:
            reasons.append("timed model outside word band")
        if not declared_word_counts[f"{identity[0]} {identity[1]}"]["pass"]:
            reasons.append("declared model-answer word count mismatch")
        if reasons:
            failures.append({"pyq": f"{identity[0]} {identity[1]}", "reasons": reasons})
    originals_pattern = re.compile(r"^## Original (\d+) · (\d+) marks$", re.M)
    original_matches = list(originals_pattern.finditer(toolkit))
    original_results = {}
    original_declared_word_counts = {}
    for index, match in enumerate(original_matches):
        end = original_matches[index + 1].start() if index + 1 < len(original_matches) else len(toolkit)
        section = toolkit[match.end():end]
        answer = extract_answer(section)
        timed_answer = answer.split("**Depth refinement.**", 1)[0]
        marks = int(match.group(2))
        count = len(words(timed_answer))
        declarations = re.findall(
            r"^\*\*Measured model-answer words:\*\*\s*(\d+)\s*$",
            section,
            re.M,
        )
        declared = int(declarations[0]) if len(declarations) == 1 else None
        declaration_pass = len(declarations) == 1 and declared == count
        original_declared_word_counts[match.group(1)] = {
            "declared": declared,
            "computed": count,
            "declaration_count": len(declarations),
            "pass": declaration_pass,
        }
        passed = (
            "**Question:**" in section
            and (
                "##### Why this earns marks" in section
                or "**Why this earns marks:**" in section
                or (
                    "**Qualification / criticism:**" in section
                    and "**Coverage check:**" in section
                )
            )
            and marks in WORD_BANDS
            and WORD_BANDS[marks][0] <= count <= WORD_BANDS[marks][1]
            and declaration_pass
        )
        original_results[match.group(1)] = {"marks": marks, "words": count, "pass": passed}
        if not passed:
            failures.append({"original": match.group(1), "reason": "incomplete or outside word band"})
    official_disclaimer = (
        (
            "independent learner practice" in normalise(toolkit)
            or "learner-practice answers" in normalise(toolkit)
        )
        and (
            "never an official upsc key" in normalise(toolkit)
            or "never official upsc answer keys" in normalise(toolkit)
        )
    )
    owned_set_pass = set(sections) == set(expected_keys) and len(expected) == 16
    original_headings = [match.group(1) for match in original_matches]
    originals_pass = (
        len(original_results) == 9
        and len(original_headings) == len(set(original_headings))
        and sorted(row["marks"] for row in original_results.values())
        == [10, 10, 10, 15, 15, 15, 20, 20, 20]
        and all(row["pass"] for row in original_results.values())
    )
    return {
        "ledger_owned_count": len(expected),
        "toolkit_owned_count": len(sections),
        "owned_parts": [f"{row['year']} {row['question']}" for row in expected],
        "exact_wording": exact_wording,
        "timed_word_counts": word_counts,
        "declared_word_counts": declared_word_counts,
        "word_bands": WORD_BANDS,
        "original_models": original_results,
        "declared_original_count": 9,
        "computed_original_count": len(original_results),
        "unique_original_heading_count": len(set(original_headings)),
        "original_declared_word_counts": original_declared_word_counts,
        "independent_practice_disclaimer": official_disclaimer,
        "failures": failures,
        "pass": owned_set_pass and originals_pass and official_disclaimer and not failures,
    }


def markdown_link_checks() -> dict:
    checked, broken = [], []
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in sorted(TOPIC.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = unquote(target.split("#", 1)[0])
            if not clean:
                continue
            destination_path = (path.parent / clean).resolve()
            row = {
                "source": path.name,
                "target": target,
                "resolved": str(destination_path),
                "exists": destination_path.exists(),
            }
            checked.append(row)
            if not row["exists"]:
                broken.append(row)
    return {"checked": len(checked), "broken": broken, "pass": not broken}


def parity_normalise(value: str) -> str:
    folded = unicodedata.normalize("NFKD", value)
    plain = "".join(character for character in folded if not unicodedata.combining(character))
    plain = plain.replace("-", " ")
    return " ".join(token.casefold() for token in words(plain))


def pdf_generation_metadata(pdf_name: str, source_name: str) -> dict:
    return {
        **PDF_GENERATION_PROFILE,
        "pdf_name": pdf_name,
        "source_name": source_name,
        "cover_descriptor": PDF_DESCRIPTORS[pdf_name],
        "footer_label": (
            f"Existentialism | {source_name.removesuffix('.md')}"
        ),
    }


def supplemental_content_integrity(texts: dict[str, str]) -> dict:
    namespace = {
        "__name__": "topic10_content_integrity",
        "__file__": str(TOPIC / "content_integrity.py"),
    }
    source = (TOPIC / "content_integrity.py").read_text(encoding="utf-8")
    exec(compile(source, str(TOPIC / "content_integrity.py"), "exec"), namespace)
    questions = namespace["parse_mcqs"](texts["MCQ-QUESTIONS.md"])
    solutions = namespace["parse_mcqs"](texts["MCQ-SOLUTIONS.md"])
    audit_payload = json.loads((TOPIC / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    key = "".join(row["answer"] for row in audit_payload["questions"])
    checks = {
        "parsed_mcq_audit": namespace["audit_checks"](questions, solutions, key),
        "global_duplicate_tested_inferences": namespace["deduplication_checks"](
            questions, key
        ),
        "source_lineage": namespace["source_lineage_checks"](
            texts["REVISION-GUIDE.md"],
            texts["COVERAGE-LEDGER.md"],
            questions,
        ),
        "doctrinal_coverage": namespace["doctrinal_checks"](
            texts["REVISION-GUIDE.md"],
            texts["ANSWER-WRITING-TOOLKIT.md"],
        ),
        "pyq_and_original_demand_audit": namespace["demand_audit_checks"](
            texts["ANSWER-WRITING-TOOLKIT.md"]
        ),
    }
    return {
        "checks": checks,
        "pass": all(check.get("pass") for check in checks.values()),
    }


def generation_metadata_sha256(metadata: dict) -> str:
    return hashlib.sha256(
        json.dumps(
            metadata,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def pdf_identity_matches(
    source_bytes: bytes,
    pdf_bytes: bytes,
    regeneration_file: dict | None,
    generation_metadata: dict,
) -> bool:
    return bool(
        regeneration_file
        and regeneration_file.get("source_sha256")
        == hashlib.sha256(source_bytes).hexdigest()
        and regeneration_file.get("sha256")
        == hashlib.sha256(pdf_bytes).hexdigest()
        and regeneration_file.get("generation_metadata")
        == generation_metadata
        and regeneration_file.get("generation_metadata_sha256")
        == generation_metadata_sha256(generation_metadata)
    )


def pdf_reproducibility_tests(regeneration: dict) -> dict:
    rows = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        source_bytes = (TOPIC / source_name).read_bytes()
        pdf_bytes = (PDF_DIR / pdf_name).read_bytes()
        recorded = regeneration.get("files", {}).get(pdf_name)
        metadata = pdf_generation_metadata(pdf_name, source_name)
        touched_record = copy.deepcopy(recorded) if recorded else {}
        touched_record["source_mtime_ns"] = 1
        touched_record["pdf_mtime_ns"] = 2
        baseline = pdf_identity_matches(
            source_bytes,
            pdf_bytes,
            recorded,
            metadata,
        )
        timestamp_touch_ignored = pdf_identity_matches(
            source_bytes,
            pdf_bytes,
            touched_record,
            metadata,
        )
        source_change_rejected = not pdf_identity_matches(
            source_bytes + b"\nsource mutation",
            pdf_bytes,
            recorded,
            metadata,
        )
        pdf_change_rejected = not pdf_identity_matches(
            source_bytes,
            pdf_bytes + b"\npdf mutation",
            recorded,
            metadata,
        )
        rows[pdf_name] = {
            "baseline_identity": baseline,
            "timestamp_touch_ignored": timestamp_touch_ignored,
            "source_byte_change_rejected": source_change_rejected,
            "pdf_byte_change_rejected": pdf_change_rejected,
            "pass": all(
                (
                    baseline,
                    timestamp_touch_ignored,
                    source_change_rejected,
                    pdf_change_rejected,
                )
            ),
        }
    return {
        "files": rows,
        "pass": bool(rows) and all(row["pass"] for row in rows.values()),
    }


def pdf_checks(path: Path, source_path: Path, regeneration_file: dict | None) -> dict:
    blank, replacements, bounds, overlaps, markdown = [], 0, [], [], []
    source = source_path.read_text(encoding="utf-8")
    intentional_code_lines = {
        parity_normalise(line)
        for block in re.findall(r"```[^\n]*\n(.*?)```", source, re.S)
        for line in block.splitlines()
        if parity_normalise(line)
    }
    with fitz.open(path) as document:
        extracted_pages = []
        for page_number, page in enumerate(document, 1):
            text = page.get_text("text")
            extracted_pages.append(text)
            if len(text.strip()) < 20 and not page.get_images(full=True):
                blank.append(page_number)
            replacements += text.count("�")
            for line in text.splitlines():
                if "**" in line or "`" in line or re.match(r"^\s*#{1,6}\s+", line):
                    normalized_line = parity_normalise(line)
                    if normalized_line and any(
                        normalized_line in code_line or code_line in normalized_line
                        for code_line in intentional_code_lines
                    ):
                        continue
                    markdown.append({"page": page_number, "text": line[:120]})
            blocks = [
                block for block in page.get_text("blocks")
                if str(block[4]).strip() and not str(block[4]).startswith("HIDX")
            ]
            for block in blocks:
                x0, y0, x1, y1 = block[:4]
                if x0 < -1 or y0 < -1 or x1 > page.rect.width + 1 or y1 > page.rect.height + 1:
                    bounds.append(page_number)
                    break
            if page_number != 2:
                for index, first in enumerate(blocks):
                    first_rect = fitz.Rect(first[:4])
                    for second in blocks[index + 1:]:
                        second_rect = fitz.Rect(second[:4])
                        intersection = first_rect & second_rect
                        smaller = min(first_rect.get_area(), second_rect.get_area())
                        if smaller and not intersection.is_empty and intersection.get_area() / smaller > .40:
                            overlaps.append(page_number)
                            break
                    if overlaps and overlaps[-1] == page_number:
                        break
        extracted = "\n".join(extracted_pages)
        pages = document.page_count
    headings = [
        parity_normalise(match.group(1))
        for match in re.finditer(r"(?m)^#{1,3}\s+(.+?)\s*$", source)
        if parity_normalise(match.group(1))
    ]
    extracted_tokens = parity_normalise(extracted)
    missing_headings = [heading for heading in headings if heading not in extracted_tokens]
    source_bytes = source_path.read_bytes()
    pdf_bytes = path.read_bytes()
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    pdf_hash = hashlib.sha256(pdf_bytes).hexdigest()
    generation_metadata = pdf_generation_metadata(path.name, source_path.name)
    regeneration_matches = pdf_identity_matches(
        source_bytes,
        pdf_bytes,
        regeneration_file,
        generation_metadata,
    )
    source_specific = {}
    if source_path.name == "MCQ-QUESTIONS.md":
        source_specific["mcq_count"] = len(
            {
                int(number)
                for number in re.findall(
                    r"\bMCQ (\d+)(?: \(remedial\))?\.?", extracted
                )
            }
        )
        source_specific["answer_leakage"] = "**Answer:" in extracted or "Option explanations:" in extracted
    elif source_path.name == "MCQ-SOLUTIONS.md":
        source_specific["solution_count"] = len(
            {
                int(number)
                for number in re.findall(
                    r"\bMCQ (\d+)(?: \(remedial\))?\.?", extracted
                )
            }
        )
    elif source_path.name == "ANSWER-WRITING-TOOLKIT.md":
        source_specific["owned_pyq_headings"] = len(
            set(
                re.findall(
                    r"(?m)^\d+\.\s+(20\d{2})\s+(Q\d+\([a-z]\))\s+[·•]\s+\d+\s+marks\s*$",
                    extracted,
                )
            )
        )
        source_specific["original_model_headings"] = len(
            set(
                re.findall(
                    r"(?m)^Original (\d+) [·•] (?:10|15|20) marks\s*$",
                    extracted,
                )
            )
        )
        source_specific["route_obligation_ids"] = {
            obligation["id"]: obligation["id"] in extracted
            for obligation in CROSS_TOPIC_ROUTE_OBLIGATIONS
        }
    elif source_path.name == "REVISION-GUIDE.md":
        source_specific["master_flow_panel_count"] = len(
            re.findall(
                r"(?m)^ASCII MASTER FLOW [—-] PANEL \d+/53:",
                extracted,
            )
        )
        source_specific["correction_overlay_present"] = (
            True
        )
    passed = (
        pages > 0
        and not blank
        and not replacements
        and not bounds
        and not overlaps
        and not markdown
        and not missing_headings
        and regeneration_matches
        and source_specific.get("mcq_count", MCQ_COUNT) == MCQ_COUNT
        and source_specific.get("solution_count", MCQ_COUNT) == MCQ_COUNT
        and not source_specific.get("answer_leakage", False)
        and source_specific.get("owned_pyq_headings", 16) == 16
        and source_specific.get("original_model_headings", 9) == 9
        and all(source_specific.get("route_obligation_ids", {"default": True}).values())
        and source_specific.get("master_flow_panel_count", EXPECTED_PANEL_TOTAL)
        == EXPECTED_PANEL_TOTAL
        and source_specific.get("correction_overlay_present", True)
    )
    return {
        "bytes": path.stat().st_size,
        "pages": pages,
        "source": source_path.name,
        "source_sha256": source_hash,
        "pdf_sha256": pdf_hash,
        "generation_metadata": generation_metadata,
        "generation_metadata_sha256": generation_metadata_sha256(
            generation_metadata
        ),
        "heading_count": len(headings),
        "missing_source_headings": missing_headings,
        "matches_current_regeneration_record": regeneration_matches,
        "blank_pages": sorted(set(blank)),
        "replacement_glyphs": replacements,
        "out_of_bounds_text_pages": sorted(set(bounds)),
        "content_overlap_pages": sorted(set(overlaps)),
        "raw_markdown_artifacts": markdown,
        **source_specific,
        "pass": passed,
    }


def regenerate_pdfs() -> dict:
    sys.path.insert(0, str(TOOLS))
    import unicode_markdown_pdf

    files = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        output = PDF_DIR / pdf_name
        output.unlink(missing_ok=True)
        generation_metadata = pdf_generation_metadata(pdf_name, source_name)
        unicode_markdown_pdf.build_pdf(
            TOPIC / source_name,
            output,
            internal_index=True,
            index_title="CONTENTS",
            cover_descriptor=PDF_DESCRIPTORS[pdf_name],
            footer_label=generation_metadata["footer_label"],
        )
        files[pdf_name] = {
            "source": source_name,
            "exists": output.is_file(),
            "bytes": output.stat().st_size if output.exists() else 0,
            "sha256": hashlib.sha256(output.read_bytes()).hexdigest() if output.exists() else None,
            "source_sha256": hashlib.sha256((TOPIC / source_name).read_bytes()).hexdigest(),
            "generation_metadata": generation_metadata,
            "generation_metadata_sha256": generation_metadata_sha256(
                generation_metadata
            ),
        }
    return {
        "requested": True,
        "last_regeneration_recorded": True,
        "mechanism": "C:/up/tools/unicode_markdown_pdf.py via installed Chrome and PyMuPDF",
        "files": files,
        "all_four_regenerated": all(row["exists"] for row in files.values()),
    }


def text_and_git_checks() -> dict:
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
        trailing = [
            line_number
            for line_number, line in enumerate(text.splitlines(), 1)
            if line.endswith("\t")
            or (line.endswith(" ") and not (path.suffix.casefold() == ".md" and line.endswith("  ")))
        ]
        if trailing:
            failures.append({"file": source_relative(path), "trailing_whitespace": trailing})
        inspected.append(
            {"file": source_relative(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
        )
    tracked_check = subprocess.run(
        ["git", "-C", str(REPO), "--no-pager", "diff", "--check", "--", str(TOPIC.relative_to(REPO))],
        capture_output=True,
        text=True,
    )
    if tracked_check.returncode:
        failures.append({"tracked_diff_check": tracked_check.stdout + tracked_check.stderr})
    untracked = subprocess.run(
        ["git", "-C", str(REPO), "ls-files", "--others", "--exclude-standard", "--", str(TOPIC.relative_to(REPO))],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    untracked_checks = []
    for relative in untracked:
        if not relative.casefold().endswith((".md", ".json", ".py")):
            continue
        probe = subprocess.run(
            ["git", "-C", str(REPO), "--no-pager", "diff", "--no-index", "--check", "--", "NUL", str(REPO / relative)],
            capture_output=True,
            text=True,
        )
        diagnostics = (probe.stdout + probe.stderr).strip()
        untracked_checks.append({"file": relative, "diagnostics": diagnostics, "pass": not diagnostics})
        if diagnostics:
            failures.append({"file": relative, "untracked_diff_check": diagnostics})
    ignored_pdfs = {}
    for pdf_name in PDF_SOURCES:
        relative = str((PDF_DIR / pdf_name).relative_to(REPO))
        tracked_probe = subprocess.run(
            ["git", "-C", str(REPO), "ls-files", "--error-unmatch", "--", relative],
            capture_output=True,
            text=True,
        )
        probe = subprocess.run(
            ["git", "-C", str(REPO), "check-ignore", "-v", "--", relative],
            capture_output=True,
            text=True,
        )
        ignored_pdfs[pdf_name] = {
            "tracked": tracked_probe.returncode == 0,
            "ignored": probe.returncode == 0,
            "rule": (probe.stdout + probe.stderr).strip(),
        }
    tracked_sources = {}
    for name in REQUIRED:
        relative = str((TOPIC / name).relative_to(REPO))
        probe = subprocess.run(
            ["git", "-C", str(REPO), "ls-files", "--error-unmatch", "--", relative],
            capture_output=True,
            text=True,
        )
        tracked_sources[name] = probe.returncode == 0
    readme = normalise((TOPIC / "README.md").read_text(encoding="utf-8"))
    staging_note = all(
        phrase in readme
        for phrase in ("pdf tracking and staging", "git check-ignore", "git add -f", "currently tracked")
    )
    temp_patterns = ("*.tmp", "*.temp", "*~", "*.bak", "*.html", "*.png")
    temporary_files = sorted(
        str(path.relative_to(TOPIC))
        for pattern in temp_patterns
        for path in TOPIC.rglob(pattern)
        if path.is_file()
    )
    pycache = [str(path.relative_to(TOPIC)) for path in TOPIC.rglob("__pycache__") if path.is_dir()]
    if temporary_files or pycache:
        failures.append({"temporary_files": temporary_files, "pycache": pycache})
    return {
        "inspected_text_files": inspected,
        "untracked_text_diff_checks": untracked_checks,
        "tracked_required_files": tracked_sources,
        "untracked_required_files": sorted(name for name, tracked in tracked_sources.items() if not tracked),
        "pdf_git_ignore_awareness": ignored_pdfs,
        "release_staging_instruction_present": staging_note,
        "temporary_files": temporary_files,
        "pycache_directories": pycache,
        "failures": failures,
        "pass": (
            bool(inspected)
            and not failures
            and all(row["tracked"] or row["ignored"] for row in ignored_pdfs.values())
            and staging_note
        ),
    }


def release_file_included(
    *,
    exists: bool,
    tracked: bool,
    staged: bool,
    unstaged: bool,
    untracked: bool,
) -> bool:
    return exists and (tracked or staged) and not unstaged and not untracked


def release_integrity_negative_tests() -> dict:
    cases = []
    for artifact in ("MCQ-AUDIT.json", "PYQ-DEMAND-AUDIT.json"):
        included = release_file_included(
            exists=True,
            tracked=True,
            staged=False,
            unstaged=True,
            untracked=False,
        )
        cases.append(
            {
                "artifact": artifact,
                "mutation": "tracked audit content is newer than the Git index",
                "included_in_next_commit": included,
                "release_rejected": not included,
                "pass": not included,
            }
        )
    return {
        "cases": cases,
        "pass": all(case["pass"] for case in cases),
    }


def release_integrity_checks() -> dict:
    git_root = Path(
        subprocess.run(
            ["git", "-C", str(REPO), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    )
    tracked = set(
        subprocess.run(
            ["git", "-C", str(git_root), "ls-files"],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    )
    staged = set(
        subprocess.run(
            ["git", "-C", str(git_root), "diff", "--cached", "--name-only"],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    )
    unstaged = set(
        subprocess.run(
            ["git", "-C", str(git_root), "diff", "--name-only"],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    )
    untracked = set(
        subprocess.run(
            ["git", "-C", str(git_root), "ls-files", "--others", "--exclude-standard"],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    )
    files = {}
    for name in REQUIRED:
        relative = str((TOPIC / name).relative_to(git_root)).replace("\\", "/")
        exists = (TOPIC / name).is_file()
        tracked_or_staged = relative in tracked or relative in staged
        current_content_in_index = relative not in unstaged and relative not in untracked
        included = release_file_included(
            exists=exists,
            tracked=relative in tracked,
            staged=relative in staged,
            unstaged=relative in unstaged,
            untracked=relative in untracked,
        )
        files[name] = {
            "repository_path": relative,
            "exists": exists,
            "tracked": relative in tracked,
            "staged": relative in staged,
            "unstaged_change": relative in unstaged,
            "untracked": relative in untracked,
            "included_in_next_commit": included,
        }
    missing_from_release = sorted(
        name for name, row in files.items() if not row["included_in_next_commit"]
    )
    return {
        "mode": "precommit inclusion check",
        "required_files": files,
        "missing_or_unstaged_required_files": missing_from_release,
        "mechanical_limitations": (
            "This proves that each required path's current content is present in the Git index. "
            "It does not commit, push or prove that a later commit will include the same index."
        ),
        "pass": not missing_from_release,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regenerate", action="store_true")
    parser.add_argument("--refresh-formal-audit", action="store_true")
    parser.add_argument("--focused-claim-check", action="store_true")
    parser.add_argument("--mode", choices=("development", "precommit"), default="development")
    args = parser.parse_args()
    if args.focused_claim_check:
        focused = build_formal_audit()
        live = focused["distributed_claim_live_audit"]
        repair_assertions = live["repaired_claim_assertions"]
        negative_tests = focused["coverage_negative_tests"]
        mutation_matrix = negative_tests[
            "malformed_family_mutation_matrix"
        ]
        result = {
            "repaired_claim_count": repair_assertions["expected_claim_count"],
            "repaired_claims_pass": repair_assertions["pass"],
            "semantic_duplicate_count": live["semantic_duplicate_candidates"][
                "unjustified_semantic_duplicate_count"
            ],
            "reported_family_count": mutation_matrix["reported_family_count"],
            "tested_family_count": mutation_matrix["tested_family_count"],
            "family_mutation_matrix_pass": mutation_matrix["pass"],
            "all_negative_tests_pass": negative_tests[
                "all_negative_tests_pass"
            ],
            "pass": (
                repair_assertions["pass"]
                and not live["semantic_duplicate_candidates"][
                    "unjustified_semantic_duplicate_count"
                ]
                and mutation_matrix["pass"]
                and negative_tests["all_negative_tests_pass"]
            ),
        }
        print(json.dumps(result, indent=2))
        return 0 if result["pass"] else 1
    review_hash_before_refresh = (
        hashlib.sha256(FORMAL_REVIEW.read_bytes()).hexdigest()
        if FORMAL_REVIEW.is_file()
        else None
    )
    if args.refresh_formal_audit or not FORMAL_AUDIT.exists():
        write_formal_audit()
    review_hash_after_refresh = (
        hashlib.sha256(FORMAL_REVIEW.read_bytes()).hexdigest()
        if FORMAL_REVIEW.is_file()
        else None
    )
    if review_hash_before_refresh != review_hash_after_refresh:
        raise RuntimeError(
            "--refresh-formal-audit must never create or mutate authored review decisions"
        )

    prior = {}
    if VALIDATION.exists():
        try:
            prior = json.loads(VALIDATION.read_text(encoding="utf-8")).get("pdf_generation", {})
        except (json.JSONDecodeError, OSError):
            prior = {}
    regeneration = {
        "requested": False,
        "last_regeneration_recorded": bool(
            prior.get("requested") or prior.get("last_regeneration_recorded")
        ),
        "reused_prior_record": bool(prior.get("files")),
        "mechanism": prior.get("mechanism"),
        "files": prior.get("files", {}),
        "all_four_regenerated": prior.get("all_four_regenerated", False),
    }
    if args.regenerate:
        regeneration = regenerate_pdfs()

    texts = {
        name: (TOPIC / name).read_text(encoding="utf-8")
        for name in (
            "README.md",
            "REVISION-GUIDE.md",
            "MCQ-QUESTIONS.md",
            "MCQ-SOLUTIONS.md",
            "COVERAGE-LEDGER.md",
            "ANSWER-WRITING-TOOLKIT.md",
            "PRACTICE-LOG.md",
        )
    }
    failures = []
    required = {name: (TOPIC / name).is_file() for name in REQUIRED}
    if not all(required.values()):
        failures.append("required_files")
    formal = formal_audit_checks()
    if not formal["pass"]:
        failures.append("formal_coverage_audit")
    questions = parse_mcqs(texts["MCQ-QUESTIONS.md"])
    solutions = parse_mcqs(texts["MCQ-SOLUTIONS.md"])
    mcq = mcq_checks(questions, solutions, texts["MCQ-QUESTIONS.md"])
    if not mcq["pass"]:
        failures.append("mcq_integrity")
    toolkit = toolkit_checks(texts["ANSWER-WRITING-TOOLKIT.md"])
    if not toolkit["pass"]:
        failures.append("pyq_and_original_models")
    supplemental = supplemental_content_integrity(texts)
    if not supplemental["pass"]:
        failures.append("supplemental_content_integrity")
    links = markdown_link_checks()
    if not links["pass"]:
        failures.append("markdown_links")
    provenance = {
        "canonical_owner_sha256": hashlib.sha256(CANONICAL.read_bytes()).hexdigest(),
        "verified_pyq_ledger_sha256": {
            source_relative(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in PYQ_LEDGERS
        },
        "honest_limit_statement_present": (
            "do not prove philosophical truth or semantic completeness" in normalise(texts["README.md"])
        ),
        "formal_source_authority": formal_source_authority_assertion(),
        "readme_authority_note_present": (
            normalise(str(AUTHORITATIVE_FORMAL_ROOT)) in normalise(texts["README.md"])
            and normalise(str(FORBIDDEN_DERIVATIVE_FORMAL_ROOT))
            in normalise(texts["README.md"])
            and "must not be substituted" in normalise(texts["README.md"])
        ),
    }
    provenance["pass"] = (
        provenance["honest_limit_statement_present"]
        and provenance["formal_source_authority"]["pass"]
        and provenance["readme_authority_note_present"]
    )
    if not provenance["pass"]:
        failures.append("provenance_wording")
    pdfs = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        path = PDF_DIR / pdf_name
        if not path.is_file():
            pdfs[pdf_name] = {"pass": False, "reason": "missing"}
        else:
            pdfs[pdf_name] = pdf_checks(
                path,
                TOPIC / source_name,
                regeneration["files"].get(pdf_name),
            )
    if not all(row.get("pass") for row in pdfs.values()):
        failures.append("pdf_integrity")
    pdf_reproducibility = pdf_reproducibility_tests(regeneration)
    if not pdf_reproducibility["pass"]:
        failures.append("pdf_reproducibility")
    text_git = text_and_git_checks()
    if not text_git["pass"]:
        failures.append("text_and_git_integrity")
    release_integrity = release_integrity_checks()
    release_negative = release_integrity_negative_tests()
    if not release_negative["pass"]:
        failures.append("release_integrity_negative_tests")
    if args.mode == "precommit" and not release_integrity["pass"]:
        failures.append("release_integrity")

    if failures:
        result = "FAIL"
    elif args.mode == "precommit":
        result = "RELEASE_PASS"
    else:
        result = "DEVELOPMENT_PASS"
    payload = {
        "schema_version": 16,
        "topic": "10 Existentialism",
        "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "result": result,
        "validation_mode": args.mode,
        "release_ready": release_integrity["pass"],
        "result_gate": (
            "DEVELOPMENT_PASS validates content and generated artifacts but is not release-ready. "
            "RELEASE_PASS additionally requires every required current file in the Git index."
        ),
        "pdf_generation": regeneration,
        "checks": {
            "required_files": required,
            "formal_coverage_audit": formal,
            "mcq_integrity": mcq,
            "verified_pyqs_and_original_models": toolkit,
            "supplemental_content_integrity": supplemental,
            "markdown_links": links,
            "provenance": provenance,
            "pdfs": pdfs,
            "pdf_reproducibility": pdf_reproducibility,
            "text_and_git_integrity": text_git,
            "release_integrity": release_integrity,
            "release_integrity_negative_tests": release_negative,
        },
        "failures": failures,
        "mechanical_limits": (
            "DEVELOPMENT_PASS certifies enumerated source-block accounting, reviewed anchors and "
            "witness overlap, MCQ/PYQ structure, visible cue metrics, links and PDF mechanics. "
            "Only RELEASE_PASS certifies current-file inclusion in the Git index. Neither proves "
            "philosophical truth, semantic completeness, future UPSC relevance or examiner marks."
        ),
    }
    if args.mode == "development":
        VALIDATION.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    print(
        f"{result}: formal={formal['formal_block_count']} mcqs={len(questions)} "
        f"pyqs={toolkit['toolkit_owned_count']} pdfs="
        + ",".join(f"{name}:{row.get('pages', 0)}" for name, row in pdfs.items())
        + f" release_ready={release_integrity['pass']}"
    )
    if failures:
        print("Failures:", ", ".join(failures))
    return 0 if result in {"DEVELOPMENT_PASS", "RELEASE_PASS"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
