from __future__ import annotations

import argparse
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
MCQ_COUNT = 41
WORD_BANDS = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
SOURCE_DIR = Path(
    r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final"
) / "Philosophy-Optional/Philosophy-Paper-I-—-Western-Philosophy/03-Empiricism"
FORMAL_SOURCES = {
    "session": SOURCE_DIR / "Learning-Session.md",
    "workbook": SOURCE_DIR / "Solved-Practice-Workbook.md",
}
CANONICAL = REPO / "knowledge/Philosophy/paper-1/western/Empiricism.md"
PYQ_LEDGERS = (
    REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2018-2025.md",
    REPO / "knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2026.md",
)
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
    "FORMAL-COVERAGE-AUDIT.json",
    "FORMAL-COVERAGE-REVIEW.json",
    "VALIDATION.json",
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
        "caus": "caus",
        "hylomorph": "hylomorph",
        "particip": "particip",
        "separat": "separat",
        "teleolog": "teleolog",
        "univers": "univers",
        "explain": "explain",
        "develop": "develop",
        "actual": "actual",
        "potential": "potential",
    }
    for prefix, stem in families.items():
        if token.startswith(prefix):
            return stem
    for suffix in ("ization", "ation", "tion", "sion", "ment", "ness", "ity", "ism", "ical", "ic", "ing", "ed", "es", "ly", "s"):
        if token.endswith(suffix) and len(token) - len(suffix) >= 4:
            return token[:-len(suffix)]
    return token


def contains_witness(value: str, witness: str) -> bool:
    value_stems = {
        concept_stem(token)
        for token in re.findall(r"[a-z0-9]+", normalise(value).replace("-", " "))
    }
    witness_stems = [
        concept_stem(token)
        for token in re.findall(r"[a-z0-9]+", normalise(witness).replace("-", " "))
    ]
    return bool(witness_stems) and all(stem in value_stems for stem in witness_stems)


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

CROSS_TOPIC_INBOUND_OBLIGATIONS = [
    {
        "id": "WP-2026-Q2B-KANT-CAUSAL-NECESSITY",
        "origin_primary_owner": ".",
        "paired_owner": "../04-Kant",
        "verified_route_source": "../../../../../knowledge/Philosophy/paper-1/_PYQ-Western-Philosophy-2026.md",
        "bounded_scope": (
            "Supply only Kant's response to Hume through the category of causality, the "
            "Second Analogy's objective temporal succession and the phenomena-only limit; "
            "retain Topic 03 as the sole primary owner of 2026 Q2(b)."
        ),
        "status": "fulfilled",
        "source_owner_evidence": {
            "file": "COVERAGE-LEDGER.md",
            "anchor": "Cross-topic inbound obligation",
            "witnesses": [
                "WP-2026-Q2B-KANT-CAUSAL-NECESSITY",
                "sole primary owner",
                "category of causality",
            ],
        },
        "destination_evidence": [
            {
                "file": "../04-Kant/COVERAGE-LEDGER.md",
                "anchor": "Inbound obligation from Empiricism",
                "witnesses": [
                    "WP-2026-Q2B-KANT-CAUSAL-NECESSITY",
                    "category of causality",
                    "Second Analogy",
                ],
            },
            {
                "file": "../04-Kant/REVISION-GUIDE.md",
                "anchor": "2026 Q2(b) · 15 marks — cross-link only",
                "witnesses": [
                    "category of causality",
                    "Second Analogy",
                    "objective succession",
                    "phenomena",
                ],
            },
            {
                "file": "../04-Kant/ANSWER-WRITING-TOOLKIT.md",
                "anchor": "2026 cross-link — Q2(b), primarily owned by Empiricism",
                "witnesses": [
                    "Hume",
                    "causality as a category",
                    "Second Analogy",
                    "primary-owner count",
                ],
            },
        ],
    }
]


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


def extract_formal_blocks() -> list[dict]:
    blocks = []
    for source_code, path in FORMAL_SOURCES.items():
        lines = path.read_text(encoding="utf-8").splitlines()
        headings = []
        occurrences = Counter()
        parents: dict[int, str] = {}
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
            headings.append(
                {
                    "id": f"{source_code}-{slug(heading)}-{occurrences[key]:02d}-{identity_hash}",
                    "source_code": source_code,
                    "source_file": path_label(path),
                    "source_line": index + 1,
                    "heading_level": level,
                    "source_heading": heading,
                    "context_heading": ancestor_headings[-1] if ancestor_headings else None,
                    "ancestor_headings": ancestor_headings,
                    "start_index": index,
                }
            )
            parents[level] = heading
            for deeper in range(level + 1, 6):
                parents.pop(deeper, None)
        for position, block in enumerate(headings):
            end_index = len(lines)
            for following in headings[position + 1:]:
                if following["heading_level"] <= block["heading_level"]:
                    end_index = following["start_index"]
                    break
            block_text = "\n".join(lines[block["start_index"]:end_index]).strip()
            block_body = body_without_headings_and_labels(block_text)
            block["end_line"] = end_index
            block["block_text"] = block_text
            block["block_body"] = block_body
            block["source_signature"] = concept_signature(block_body)
            block["source_body_witnesses"] = substantive_body_witnesses(block_body)
            blocks.append(block)
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


def section_body(text: str, anchor: str, context_anchor: str | None = None) -> str:
    return body_without_headings_and_labels(
        find_heading_section(text, anchor, context_anchor)
    )


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
    sample = next(
        block for block in blocks
        if "Plain-language definition" in block["block_text"]
        and block["ancestor_headings"]
    )
    original_hash = decision_bound_sha256(sample)

    label_mutation = dict(sample)
    label_mutation["block_text"] = sample["block_text"].replace(
        "Plain-language definition",
        "Plain-language definition MUTATED",
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
        "semantic_label": "Plain-language definition",
        "original_sha256": original_hash,
        "mutation_sha256": mutation_hashes,
        "all_mutations_stale_decision": all(
            value != original_hash for value in mutation_hashes.values()
        ),
    }


def build_formal_audit() -> dict:
    review_payload = load_formal_review()
    review_decisions = review_decisions_by_id(review_payload)
    formal_blocks = extract_formal_blocks()
    hash_regression = review_hash_regression_check(formal_blocks)
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
    return {
        "schema_version": 4,
        "topic": "03 Empiricism",
        "rule": "START-HERE.md formal-session reconciliation rule 10",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "formal_block_definition": (
            "Every level-2 through level-5 heading in the authoritative completed Learning-Session "
            "and Solved-Practice-Workbook. Extraction derives stable IDs, canonical full-block "
            "hashes, body signatures and witnesses only. The decision-bound representation retains "
            "the source heading, ancestor context, semantic labels and complete block text while "
            "normalizing only line endings, Unicode composition and trailing whitespace. "
            "Classification and destination decisions come solely "
            "from the separately authored FORMAL-COVERAGE-REVIEW.json layer."
        ),
        "source_files": {
            code: {
                "path": path_label(path),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "bytes": path.stat().st_size,
            }
            for code, path in FORMAL_SOURCES.items()
        },
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
        "cross_topic_inbound_obligations": CROSS_TOPIC_INBOUND_OBLIGATIONS,
        "summary": {
            "formal_blocks": len(rows),
            **{name: classifications[name] for name in ALLOWED_CLASSIFICATIONS},
            "unreviewed": unreviewed,
            "unresolved": unresolved,
        },
        "rows": rows,
        "mechanical_limitations": (
            "The validator can prove that an independently persisted authored decision is bound "
            "to the canonical full block hash, including semantic labels, heading and context, "
            "and that its anchors, witnesses and propositions "
            "remain present. Extraction and --refresh-formal-audit never create or approve review "
            "decisions. These controls still cannot prove philosophical truth, pedagogical "
            "sufficiency or examiner marks."
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
    if review_payload.get("schema_version") != 2:
        review_failures.append("review schema must be 2")
    if review_payload.get("review_status") != "authored_complete":
        review_failures.append("review status is not authored_complete")
    if review_payload.get("decision_count") != len(review_decisions):
        review_failures.append("declared review decision count mismatch")
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
        strategy = row.get("mapping_strategy", "")
        strategy_counts[strategy] += 1
        fragment_continuation = strategy == "reviewed_exact_fragment_continuation"
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
        if classification == "covered_in_scope" and not destinations:
            failures.append({"id": block_id, "reason": "covered row has no reviewed destination"})
        aggregate_destination_bodies = []
        for item in destinations:
            relative = item.get("file", "")
            path = TOPIC / relative
            if not path.is_file():
                failures.append({"id": block_id, "reason": f"missing destination {relative}"})
                continue
            text = package_text.setdefault(relative, path.read_text(encoding="utf-8"))
            if item.get("anchor_kind") == "literal":
                body = body_without_headings_and_labels(text) if item.get("anchor", "") in text else ""
            else:
                body = section_body(text, item.get("anchor", ""), item.get("context_anchor"))
            if not body:
                failures.append(
                    {"id": block_id, "reason": f"destination anchor missing: {relative} :: {item.get('anchor')}"}
                )
                continue
            aggregate_destination_bodies.append(body)
            witnesses = item.get("witnesses", [])
            if len(witnesses) < (1 if fragment_continuation else 2):
                failures.append({"id": block_id, "reason": "destination has fewer than two witnesses"})
            source_normalized = normalise(block["block_body"])
            destination_normalized = normalise(body)
            absent_source = [term for term in witnesses if not contains_witness(block["block_body"], term)]
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
        signature = block["source_signature"]
        overlap = [term for term in signature if contains_witness(aggregate_normalized, term)]
        overlap_rate = len(overlap) / len(signature) if signature else 0
        minimum_overlap = row.get("minimum_aggregate_signature_overlap")
        if classification == "covered_in_scope" and (
            not isinstance(minimum_overlap, (int, float))
            or minimum_overlap < .45
            or overlap_rate < minimum_overlap
        ):
            failures.append(
                {
                    "id": block_id,
                    "reason": "insufficient aggregate body-signature correspondence",
                    "overlap_rate": round(overlap_rate, 3),
                    "required": minimum_overlap,
                    "matched_signature_terms": overlap,
                }
            )
        propositions = row.get("required_propositions", [])
        if classification == "covered_in_scope" and len(propositions) < (1 if fragment_continuation else 2):
            failures.append({"id": block_id, "reason": "fewer than two required substantive propositions"})
        source_body_normalized = normalise(block["block_body"])
        for proposition in propositions:
            witnesses = proposition.get("witnesses", [])
            if not witnesses:
                failures.append(
                    {
                        "id": block_id,
                        "reason": "empty proposition witness set",
                        "proposition": proposition.get("id"),
                    }
                )
                continue
            absent_source = [
                witness for witness in witnesses
                if not contains_witness(block["block_body"], witness)
            ]
            absent_destination = [
                witness for witness in witnesses
                if not contains_witness(aggregate_normalized, witness)
            ]
            if absent_source or absent_destination:
                failures.append(
                    {
                        "id": block_id,
                        "reason": "aggregate proposition coverage failure",
                        "proposition": proposition.get("id"),
                        "absent_source": absent_source,
                        "absent_destination": absent_destination,
                    }
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
    recorded_obligations = payload.get("cross_topic_inbound_obligations", [])
    obligation_failures = []
    if recorded_obligations != CROSS_TOPIC_INBOUND_OBLIGATIONS:
        obligation_failures.append("recorded obligations differ from validator-owned obligations")
    for obligation in CROSS_TOPIC_INBOUND_OBLIGATIONS:
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

    ledger_2026 = PYQ_LEDGERS[1].read_text(encoding="utf-8")
    ledger_empiricism_parts = re.findall(
        r"^- \*\*(Q\d+\([a-z]\)) · \d+ marks · \[Empiricism\]\([^)]+\):\*\*",
        ledger_2026,
        re.M,
    )
    latest_upgrade_rows = [
        row
        for row in rows
        if row.get("mapping_strategy") == "manual_latest_paper_upgrade"
        and row.get("source", {}).get("heading") == "PYQS AND ANSWER PRACTICE"
    ]
    latest_owner_assertion = {
        "ledger_empiricism_parts": ledger_empiricism_parts,
        "required_primary_part": "Q1(b)",
        "forbidden_misattribution": "Q1(a)",
        "review_rows_checked": [row.get("id") for row in latest_upgrade_rows],
        "pass": (
            "Q1(b)" in ledger_empiricism_parts
            and "Q1(a)" not in ledger_empiricism_parts
            and len(latest_upgrade_rows) == 2
            and all(
                "2026 Q1(b)" in row.get("review_basis", "")
                and "2026 Q1(a)" not in row.get("review_basis", "")
                for row in latest_upgrade_rows
            )
        ),
    }
    if not latest_owner_assertion["pass"]:
        failures.append({"verified_2026_owner_assertion": latest_owner_assertion})

    summary = payload.get("summary", {})
    calculated_summary = {
        "formal_blocks": len(rows),
        **{classification: classifications[classification] for classification in ALLOWED_CLASSIFICATIONS},
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
        "verified_2026_owner_assertion": latest_owner_assertion,
        "unresolved_due_inbound_obligations": unresolved_due,
        "cross_topic_inbound_obligations": {
            "count": len(recorded_obligations),
            "ids": [row.get("id") for row in recorded_obligations],
            "failures": obligation_failures,
            "pass": not obligation_failures,
        },
        "source_identity": source_identity,
        "failures": failures,
        "mechanical_limitations": payload.get("mechanical_limitations"),
        "pass": payload.get("schema_version") == 4 and not failures and not unresolved_due,
    }


def parse_mcqs(text: str) -> list[dict]:
    result = []
    for block in re.split(r"(?=^## MCQ \d+(?: \(remedial\))?\.)", text, flags=re.M)[1:]:
        heading = re.search(r"^## MCQ (\d+)(?: \(remedial\))?\.\s*(.+)$", block, re.M)
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
                "title": heading.group(2).strip(),
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
        "absolute_quantifier": r"\b(always|never|only|entirely|every|none)\b",
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
            expected = "Correct:" if letter == answer else "Incorrect:"
            if not explanation.startswith(expected) or len(words(explanation)) < 12:
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
                r"^- \*\*(Q\d+\([a-z]\)) · (\d+) marks · \[Empiricism\]\([^)]+\):\*\* (.+?)(?: → .*)?$",
                line,
            )
            if match and year:
                result.append(
                    {
                        "year": year,
                        "question": match.group(1),
                        "marks": int(match.group(2)),
                        "wording": match.group(3).strip(),
                    }
                )
    return result


def extract_answer(section: str) -> str:
    match = re.search(
        r"^##### Independent model answer\s*\n(.*?)(?=^##### (?:Qualification and criticism|Why this earns marks|Exam-length execution|Closed-book answer spine))",
        section,
        re.M | re.S,
    )
    return match.group(1).strip() if match else ""


def toolkit_checks(toolkit: str) -> dict:
    expected = parse_owned_pyqs()
    expected_keys = {(row["year"], row["question"]): row for row in expected}
    heading_pattern = re.compile(r"^#### (20\d{2}) · (Q\d+\([a-z]\)) · (\d+) marks$", re.M)
    matches = list(heading_pattern.finditer(toolkit))
    sections = {}
    failures = []
    word_counts = {}
    exact_wording = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else toolkit.find(
            "### ORIGINAL MAINS PRACTICE", match.end()
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
        reasons = []
        if not expected_row or marks != expected_row["marks"]:
            reasons.append("identity or marks mismatch")
        if not wording_pass:
            reasons.append("exact wording mismatch")
        if not answer:
            reasons.append("missing independent model answer")
        if "##### Demand decoding" not in section or "##### Why this earns marks" not in section:
            reasons.append("missing demand or marks explanation")
        if not word_counts[f"{identity[0]} {identity[1]}"]["pass"]:
            reasons.append("timed model outside word band")
        if reasons:
            failures.append({"pyq": f"{identity[0]} {identity[1]}", "reasons": reasons})
    originals_pattern = re.compile(r"^#### Original (\d+) · (\d+) marks$", re.M)
    original_matches = list(originals_pattern.finditer(toolkit))
    original_results = {}
    for index, match in enumerate(original_matches):
        end = original_matches[index + 1].start() if index + 1 < len(original_matches) else len(toolkit)
        section = toolkit[match.end():end]
        answer = extract_answer(section)
        timed_answer = answer.split("**Depth refinement.**", 1)[0]
        marks = int(match.group(2))
        count = len(words(timed_answer))
        passed = (
            "**Question:**" in section
            and "##### Why this earns marks" in section
            and marks in WORD_BANDS
            and WORD_BANDS[marks][0] <= count <= WORD_BANDS[marks][1]
        )
        original_results[match.group(1)] = {"marks": marks, "words": count, "pass": passed}
        if not passed:
            failures.append({"original": match.group(1), "reason": "incomplete or outside word band"})
    official_disclaimer = (
        "independent learner practice" in normalise(toolkit)
        and "never an official upsc key" in normalise(toolkit)
    )
    owned_set_pass = set(sections) == set(expected_keys) and len(expected) == 14
    originals_pass = (
        len(original_results) == 6
        and sorted(row["marks"] for row in original_results.values()) == [10, 10, 15, 15, 20, 20]
        and all(row["pass"] for row in original_results.values())
    )
    return {
        "ledger_owned_count": len(expected),
        "toolkit_owned_count": len(sections),
        "owned_parts": [f"{row['year']} {row['question']}" for row in expected],
        "exact_wording": exact_wording,
        "timed_word_counts": word_counts,
        "word_bands": WORD_BANDS,
        "original_models": original_results,
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


def pdf_checks(path: Path, source_path: Path, regeneration_file: dict | None) -> dict:
    blank, replacements, bounds, overlaps, markdown = [], 0, [], [], []
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
    source = source_path.read_text(encoding="utf-8")
    headings = [
        parity_normalise(match.group(1))
        for match in re.finditer(r"(?m)^#{1,3}\s+(.+?)\s*$", source)
        if parity_normalise(match.group(1))
    ]
    extracted_tokens = parity_normalise(extracted)
    missing_headings = [heading for heading in headings if heading not in extracted_tokens]
    source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
    pdf_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    regeneration_matches = bool(
        regeneration_file
        and regeneration_file.get("source_sha256") == source_hash
        and regeneration_file.get("sha256") == pdf_hash
        and regeneration_file.get("source_mtime_ns") == source_path.stat().st_mtime_ns
    )
    source_specific = {}
    if source_path.name == "MCQ-QUESTIONS.md":
        source_specific["mcq_count"] = len(
            {
                int(number)
                for number in re.findall(
                    r"\bMCQ (\d+)(?: \(remedial\))?\.", extracted
                )
            }
        )
        source_specific["answer_leakage"] = "**Answer:" in extracted or "Option explanations:" in extracted
    elif source_path.name == "MCQ-SOLUTIONS.md":
        source_specific["solution_count"] = len(
            {
                int(number)
                for number in re.findall(
                    r"\bMCQ (\d+)(?: \(remedial\))?\.", extracted
                )
            }
        )
    elif source_path.name == "ANSWER-WRITING-TOOLKIT.md":
        source_specific["owned_pyq_headings"] = len(
            re.findall(r"\b20\d{2}\s*[·•]\s*Q\d+\([a-z]\)", extracted)
        )
    passed = (
        pages > 0
        and not blank
        and not replacements
        and not bounds
        and not overlaps
        and not markdown
        and not missing_headings
        and path.stat().st_mtime_ns >= source_path.stat().st_mtime_ns
        and regeneration_matches
        and source_specific.get("mcq_count", MCQ_COUNT) == MCQ_COUNT
        and source_specific.get("solution_count", MCQ_COUNT) == MCQ_COUNT
        and not source_specific.get("answer_leakage", False)
        and source_specific.get("owned_pyq_headings", 14) == 14
    )
    return {
        "bytes": path.stat().st_size,
        "pages": pages,
        "source": source_path.name,
        "source_sha256": source_hash,
        "pdf_sha256": pdf_hash,
        "source_mtime_ns": source_path.stat().st_mtime_ns,
        "pdf_mtime_ns": path.stat().st_mtime_ns,
        "pdf_not_older_than_source": path.stat().st_mtime_ns >= source_path.stat().st_mtime_ns,
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

    descriptors = {
        "Revision-Guide.pdf": "Philosophy Optional · Paper I · Western Philosophy · Topic 03",
        "MCQ-Questions.pdf": "41-question closed-book bank · no answer key",
        "MCQ-Solutions.pdf": "Option-specific explanations and examiner traps",
        "Answer-Writing-Toolkit.pdf": "Fourteen verified PYQs and six original solved models",
    }
    files = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        output = PDF_DIR / pdf_name
        output.unlink(missing_ok=True)
        unicode_markdown_pdf.build_pdf(
            TOPIC / source_name,
            output,
            internal_index=True,
            index_title="CONTENTS",
            cover_descriptor=descriptors[pdf_name],
            footer_label=f"Empiricism | {source_name.removesuffix('.md')}",
        )
        files[pdf_name] = {
            "source": source_name,
            "exists": output.is_file(),
            "bytes": output.stat().st_size if output.exists() else 0,
            "sha256": hashlib.sha256(output.read_bytes()).hexdigest() if output.exists() else None,
            "source_sha256": hashlib.sha256((TOPIC / source_name).read_bytes()).hexdigest(),
            "source_mtime_ns": (TOPIC / source_name).stat().st_mtime_ns,
            "pdf_mtime_ns": output.stat().st_mtime_ns if output.exists() else None,
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
        files[name] = {
            "repository_path": relative,
            "exists": exists,
            "tracked": relative in tracked,
            "staged": relative in staged,
            "unstaged_change": relative in unstaged,
            "untracked": relative in untracked,
            "included_in_next_commit": exists and tracked_or_staged and current_content_in_index,
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


def moore_route_consistency_checks(texts: dict[str, str]) -> dict:
    forbidden = {
        "transparency_entails_direct_realism": (
            r"transparency.{0,140}(?:support(?:s|ed)?|yield(?:s|ed)?|"
            r"establish(?:es|ed)?|prov(?:e|es|ed)|entail(?:s|ed)?).{0,100}"
            r"direct realism"
        ),
        "moore_directly_knows_object": (
            r"moore(?:(?!russell).){0,180}(?:ordinary )?object"
            r"(?:(?!russell).){0,100}directly known|"
            r"moore(?:(?!russell).){0,180}directly known"
            r"(?:(?!russell).){0,100}(?:ordinary )?object"
        ),
        "moore_defends_object": (
            r"moore(?:(?!russell).){0,180}"
            r"(?:defend(?:s|ed)?|keep(?:s|ing)?|retain(?:s|ed)?)"
            r"(?:(?!russell).){0,100}(?:ordinary )?object"
        ),
        "moore_restores_common_sense": (
            r"moore(?:(?!russell).){0,180}(?:restore(?:s|d)?|recover(?:s|ed)?|"
            r"re-establish(?:es|ed)?)(?:(?!russell).){0,80}common sense"
        ),
    }
    surfaces = [
        {
            "file": "ANSWER-WRITING-TOOLKIT.md",
            "anchor": "2018 · Q3(a) · 20 marks",
            "groups": [
                ["act of awareness"],
                ["object"],
                ["blocks the identity inference"],
                ["does not itself supply a full replacement theory of perception"],
                ["russell reconstructs"],
            ],
        },
        {
            "file": "REVISION-GUIDE.md",
            "anchor": (
                "SESSION 9 — BERKELEY III: SPIRITS, NOTIONS, GOD, CONTINUITY, "
                "AND THE MOORE, RUSSELL AND HEGEL COMPARISONS"
            ),
            "groups": [
                ["act of awareness", "act-object distinction"],
                ["transparency diagnoses", "transparency diagnosis"],
                ["perceptual theory open", "no complete replacement theory"],
                ["russell reconstructs", "logical construction"],
            ],
        },
        {
            "file": "MCQ-QUESTIONS.md",
            "anchor": "MCQ 20. Moore and Russell against Berkeley",
            "groups": [
                ["moore blocks the act-object identity"],
                ["leaving perception open"],
                ["russell reconstructs physical objects"],
            ],
        },
        {
            "file": "MCQ-SOLUTIONS.md",
            "anchor": "MCQ 20. Moore and Russell against Berkeley",
            "groups": [
                ["transparency diagnosis"],
                ["act-object confusion"],
                ["without supplying a complete perceptual theory"],
                ["russell reconstructs physical-object discourse"],
            ],
        },
    ]
    failures = []
    checked = []
    for surface in surfaces:
        section = find_heading_section(
            texts[surface["file"]],
            surface["anchor"],
        )
        normalized = normalise(section)
        missing = [
            group
            for group in surface["groups"]
            if not any(normalise(phrase) in normalized for phrase in group)
        ]
        if not section or missing:
            failures.append(
                {
                    "file": surface["file"],
                    "anchor": surface["anchor"],
                    "reason": "required qualified Moore route assertion absent",
                    "missing_groups": missing,
                }
            )
        surface_forbidden = [
            name
            for name, pattern in forbidden.items()
            if re.search(pattern, normalized, re.I | re.S)
        ]
        if surface_forbidden:
            failures.append(
                {
                    "file": surface["file"],
                    "anchor": surface["anchor"],
                    "reason": "forbidden Moore route overclaim present",
                    "assertions": surface_forbidden,
                }
            )
        checked.append(
            {
                "file": surface["file"],
                "anchor": surface["anchor"],
                "required_groups": len(surface["groups"]),
                "pass": bool(section) and not missing and not surface_forbidden,
            }
        )
    package_forbidden = []
    for file_name in (
        "ANSWER-WRITING-TOOLKIT.md",
        "REVISION-GUIDE.md",
        "MCQ-QUESTIONS.md",
        "MCQ-SOLUTIONS.md",
    ):
        normalized = normalise(texts[file_name])
        for name, pattern in forbidden.items():
            if re.search(pattern, normalized, re.I | re.S):
                package_forbidden.append({"file": file_name, "assertion": name})
    if package_forbidden:
        failures.append(
            {
                "reason": "forbidden Moore overclaim exists outside routed anchor",
                "matches": package_forbidden,
            }
        )
    return {
        "surfaces_checked": checked,
        "package_wide_forbidden_matches": package_forbidden,
        "failures": failures,
        "pass": not failures and len(checked) == 4,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regenerate", action="store_true")
    parser.add_argument("--refresh-formal-audit", action="store_true")
    parser.add_argument("--mode", choices=("development", "precommit"), default="development")
    args = parser.parse_args()
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
    moore_route = moore_route_consistency_checks(texts)
    if not moore_route["pass"]:
        failures.append("moore_route_consistency")
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
    }
    provenance["pass"] = provenance["honest_limit_statement_present"]
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
    text_git = text_and_git_checks()
    if not text_git["pass"]:
        failures.append("text_and_git_integrity")
    release_integrity = release_integrity_checks()
    if args.mode == "precommit" and not release_integrity["pass"]:
        failures.append("release_integrity")

    if failures:
        result = "FAIL"
    elif args.mode == "precommit":
        result = "RELEASE_PASS"
    else:
        result = "DEVELOPMENT_PASS"
    payload = {
        "schema_version": 15,
        "topic": "03 Empiricism",
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
            "moore_route_consistency": moore_route,
            "markdown_links": links,
            "provenance": provenance,
            "pdfs": pdfs,
            "text_and_git_integrity": text_git,
            "release_integrity": release_integrity,
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
