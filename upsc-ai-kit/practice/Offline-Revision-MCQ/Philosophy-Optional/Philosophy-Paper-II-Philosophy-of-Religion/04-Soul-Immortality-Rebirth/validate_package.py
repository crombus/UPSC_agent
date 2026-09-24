from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path

import fitz


sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

DEFAULT_TOPIC = Path(__file__).resolve().parent
TOPIC = Path(os.environ.get("SOUL_TOPIC_ROOT", DEFAULT_TOPIC)).resolve()
DEFAULT_REPO = DEFAULT_TOPIC.parents[4]
REPO = Path(os.environ.get("SOUL_REPO_ROOT", DEFAULT_REPO)).resolve()
TOOLS = REPO.parent / "tools"
VALIDATION = TOPIC / "VALIDATION.json"
INBOUND_ID = "T11-ROUTE-P2-SOUL"
WORD_BANDS = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
CANONICAL = REPO / "knowledge/Philosophy/paper-2/philosophy-of-religion/Soul-Immortality-Rebirth.md"
PYQ_LEDGER = REPO / "knowledge/Philosophy/paper-2/_PYQ-PhilosophyOfReligion-2018-2025.md"
PYQ_2026 = REPO / "knowledge/Philosophy/paper-2/_PYQ-PhilosophyOfReligion-2026-Supplement.md"
REFERENCE_DIR = REPO / "knowledge/Philosophy/Philosophy-of-Religion/learning-sessions/Soul-Immortality-Rebirth-Liberation"
REFERENCE_SESSION = REFERENCE_DIR / "Soul-Immortality-Rebirth-Liberation_Layered-Complete-Learning-Session_2026-08-19.md"
REFERENCE_WORKBOOK = REFERENCE_DIR / "Soul-Immortality-Rebirth-Liberation_Layered-Solved-Practice-Workbook_2026-08-19.md"

REQUIRED = (
    "README.md",
    "SOURCE-PROVENANCE.json",
    "REVISION-GUIDE.md",
    "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md",
    "MCQ-AUDIT.json",
    "ANSWER-WRITING-TOOLKIT.md",
    "PYQ-DEMAND-AUDIT.json",
    "COVERAGE-LEDGER.md",
    "CANONICAL-COVERAGE-REVIEW.json",
    "FORMAL-COVERAGE-AUDIT.json",
    "PRACTICE-LOG.md",
    "validate_package.py",
    "VALIDATION.json",
    "attempts/.gitkeep",
    "pdf/Revision-Guide.pdf",
    "pdf/MCQ-Questions.pdf",
    "pdf/MCQ-Solutions.pdf",
    "pdf/Answer-Writing-Toolkit.pdf",
)
PDF_SOURCES = {
    "Revision-Guide.pdf": "REVISION-GUIDE.md",
    "MCQ-Questions.pdf": "MCQ-QUESTIONS.md",
    "MCQ-Solutions.pdf": "MCQ-SOLUTIONS.md",
    "Answer-Writing-Toolkit.pdf": "ANSWER-WRITING-TOOLKIT.md",
}
PDF_DESCRIPTORS = {
    "Revision-Guide.pdf": "Complete learning, revision, visuals and register notes",
    "MCQ-Questions.pdf": "Coverage-derived question-only practice",
    "MCQ-Solutions.pdf": "Option-specific solutions and trap analysis",
    "Answer-Writing-Toolkit.pdf": "17 verified PYQs and six timed original models",
}

CANONICAL_PROPOSITIONS = {
    "Exact printed ownership and cross-topic firewall": "The package distinguishes survival, rebirth and liberation questions from adjacent Paper I metaphysics, revelation, evil, religious experience and religion-without-God owners.",
    "0. ONE-SCREEN MAP ⚠️": "Immortality, rebirth and liberation are distinct relations: survival does not by itself entail another embodiment, and Buddhist rebirth does not require a substantial immortal soul.",
    "0A. SOUL, SELF, PERSON AND CONTINUITY-BEARER ⚠️": "Competing substance, embodied-person, bundle and causal-continuity models supply different answers to who or what persists through death and rebirth.",
    "1. IMMORTALITY OF THE SOUL ✅": "Plato and several Indian schools defend enduring soul models, while Kantian and body-brain objections challenge whether survival has been demonstrated.",
    "1.1 Arguments for immortality and their limits": "Simplicity, identity, moral-order, desire and religious-experience arguments support immortality only with contestable premises and do not independently establish rebirth.",
    "2. REBIRTH (Karma-Saṃsāra) ✅": "Rebirth extends karmic continuity across lives; substantialist schools add a transmigrating bearer, whereas Buddhism explains renewed becoming without a permanent self.",
    "3. LIBERATION ✅ (the goal — varies by school)": "Liberation names non-identical goals across Advaita, Viśiṣṭādvaita, Nyāya, Sāṃkhya-Yoga, Jainism, Buddhism and Western traditions.",
    "4. FOUNDATIONAL STATEMENT BANK ⚠️": "The foundational facts connect Gītā imagery, Platonic recollection, Buddhist causal continuity, jīvanmukti and Nyāya apavarga to exam-ready distinctions.",
    "5. APPLIED-QUESTION DRILLS ⚠️": "The drill bank routes each major doctrine to a specific evaluative demand rather than treating immortality, rebirth and liberation as interchangeable.",
    "5A. LIBERATION PARITY BENCH — the six terms must never be merged ⚠️": "Mokṣa, apavarga, kaivalya, Jain liberation, nirvāṇa and resurrection differ over what ends, what remains and whether consciousness persists.",
    "6. PYQ-MAPPED MODEL-ANSWER SKELETONS ⚠️": "The answer skeletons convert recurring PYQ demands into thesis, comparison, objection and qualified-verdict structures.",
    "6.1 — \"Is immortality of the soul a necessary condition for rebirth? (w.r.t. Buddhism)\" (2022, 10m)": "Buddhism defeats necessity, while substantial-soul immortality remains insufficient by itself because rebirth also requires a transmigration or re-embodiment account.",
    "6.2 — \"Nature of jīvanmukti in Advaita Vedānta.\" (2025, 10m)": "Advaita presents jīvanmukti as liberation through knowledge while embodied life continues under prārabdha karma until videhamukti.",
    "6.3 — \"Evaluate the concept of Bhakti (Devotion) as a pathway to attain liberation.\" (2018, 15m)": "Bhakti traditions differ over devotion, surrender, grace and whether bhakti directly liberates or prepares the aspirant for knowledge.",
    "6.4 — \"Are Knowledge, Action and Devotion the means to liberation in Indian tradition?\" (2020, 15m)": "Indian schools classify knowledge, action and devotion as direct, preparatory, sequential or grace-dependent means according to their account of bondage.",
    "6.5 — \"Karma, Rebirth and Reincarnation in Hinduism.\" (2019, 20m)": "Karma supplies moral causation, rebirth supplies the cross-life field, and reincarnation adds the school-specific claim of a substantial bearer entering another body.",
    "8. ADVANCED DOCTRINE DOSSIERS": "The advanced dossiers deepen the canonical doctrines through arguments, presuppositions, distinctions, examples and objection-reply pairs.",
    "8.1 Plato's immortality arguments": "Plato's cyclical, recollection, affinity and Form-of-Life arguments require separate evaluation because pre-existence and resemblance to Forms do not automatically prove post-mortem survival.",
    "8.2 Vedāntic ātman, rebirth and mokṣa": "Vedāntic systems connect an enduring self with karmic embodiment but diverge sharply between Advaitic non-dual realization and Viśiṣṭādvaitic personal communion.",
    "8.3 Buddhist rebirth without an immortal soul": "Dependent origination and neither-same-nor-different continuity explain karmic rebirth without an unchanging owner of the aggregates.",
    "8.4 Jain jīva and liberation": "Jainism treats jīva as enduring, karma as material bondage, and liberation as the perfected soul's release through stopping and shedding karmic influx.",
    "8.5 Nyāya apavarga and Advaita jīvanmukti": "Nyāya apavarga as cessation without liberated consciousness contrasts with Advaita jīvanmukti as self-luminous freedom while living.",
    "8.6 Bhakti as a path to liberation (2018 Q7(c) owner-module)": "Bhakti theories compare disciplined remembrance, surrender, grace, divine dependence and the tension between dualistic love and non-dual liberation.",
    "8.7 Jñāna, karma and bhakti — how the three means are related (2020 Q8(c) owner-module)": "The three means converge in transforming agency but diverge over whether liberation is produced, received or disclosed by removing ignorance.",
    "8.8 Resurrection versus rebirth — and rebirth versus reincarnation": "Resurrection reconstitutes the embodied person after one life, rebirth is the wider cross-life continuity category, and reincarnation presupposes a substantial transmigrant.",
    "8.9 Sāṃkhya and Yoga: *kaivalya*, and how it differs from every other liberation": "Sāṃkhya-Yoga kaivalya isolates puruṣa from prakṛti and must not be confused with Brahman-identity, divine communion, omniscience or Buddhist cessation.",
    "9. INTER-THINKER / INTER-SCHOOL DEBATES": "The comparative debates test soul versus no-self continuity, identity versus communion, conscious versus non-conscious release, and natural immortality versus resurrection.",
    "10. CRITICISMS AND REPLIES": "Memory, verification, bodily dependence, justice and identity objections each require a doctrine-specific reply rather than a generic appeal to faith.",
    "11. COMMON UPSC TRAPS": "The trap list prevents conflating rebirth with reincarnation, nirvāṇa with annihilation, apavarga with bliss, kaivalya with kevala and liberation with merger.",
    "12. KEYWORD & STATEMENT BANK": "The keyword bank supplies precise terms and formulations for continuity, bondage, release, identity and school-specific mechanisms.",
    "CORPUS-DRIVEN DEPTH DELTA (expanded PYQ audit)": "The depth delta adds the doctrine, thinker and comparison material demanded by the verified PYQ corpus beyond a minimal syllabus outline.",
    "13. PYQ ROUTING (2018–2025)": "The routing table assigns each verified question to this owner, a supporting module or an explicit boundary so ownership remains auditable.",
    "14. ANSWER ARCHITECTURE (10 / 15 / 20 MARKS)": "Answer architecture scales argument density, comparison and evaluation to the locked 10-, 15- and 20-mark formats.",
    "10 marks": "A 10-mark response uses a direct definition, compact doctrinal contrast, one objection and a qualified conclusion within 150 to 200 words.",
    "15 marks": "A 15-mark response develops two or three doctrinal axes, evaluation and a reasoned verdict within 250 to 300 words.",
    "20 marks": "A 20-mark response integrates conceptual distinctions, multiple traditions, objections, replies and a defended synthesis within 340 to 400 words.",
    "15. DIRECTIVE DECODER": "The directive decoder distinguishes descriptive, comparative and critical tasks so the answer's operations match the command word.",
    "16. GRADED VERDICT LADDER": "The verdict ladder replaces absolute conclusions with calibrated judgments about logical possibility, doctrinal dependence and evidential strength.",
    "17. FACTUAL AND QUOTATION DISCIPLINE": "Factual discipline separates canonical text, interpretive inference and illustrative analogy while avoiding invented quotations or empirical proof claims.",
    "18. LINK-OUTS": "The link-outs preserve boundaries with adjacent philosophy-of-religion and Indian-philosophy topics without transferring this owner's core obligations.",
    "SOURCES": "The source section identifies canonical texts, standard philosophical debates and bounded reference materials supporting the package.",
}

DOCTRINAL_CORRECTIONS = {
    "6.1 — \"Is immortality of the soul a necessary condition for rebirth? (w.r.t. Buddhism)\" (2022, 10m)",
    "16. GRADED VERDICT LADDER",
}

FORBIDDEN_MCQQ_FILLER = (
    "for the conceptual distinction at issue",
    "for the precise conceptual distinction at issue",
    "for the precise doctrinal distinction currently at issue",
    "under the precise doctrinal comparison presented in this question only",
    "as a claim under the doctrinal comparison presented in this question",
    "as a claim under the exact doctrinal comparison presented in this question",
    "as a claim evaluated under the exact doctrinal comparison presented in this question",
    "as a claim being evaluated under the exact specific doctrinal comparison presented in this question",
    "as a claim evaluated under the exact specific doctrinal comparison presented in this question",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_sha(text: str) -> str:
    return hashlib.sha256(text.strip().encode("utf-8")).hexdigest()


def words(text: str) -> list[str]:
    text = re.sub(r"(?m)^\s*```[^\n]*$", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`#>|]", " ", text)
    return re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE)


def word_count(text: str) -> int:
    return len(words(text))


def normalise(text: str) -> str:
    folded = unicodedata.normalize("NFKD", text)
    plain = "".join(character for character in folded if not unicodedata.combining(character))
    return " ".join(token.casefold().replace("’", "'") for token in words(plain))


def heading_blocks(path: Path, source_label: str) -> list[dict]:
    lines = read(path).splitlines()
    rows = []
    occurrences = Counter()
    for index, line in enumerate(lines):
        match = re.match(r"^(#{2,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        heading = match.group(2).strip()
        occurrences[normalise(heading)] += 1
        rows.append(
            {
                "line_index": index,
                "line": index + 1,
                "level": len(match.group(1)),
                "heading": heading,
                "occurrence": occurrences[normalise(heading)],
            }
        )
    stack = []
    for index, row in enumerate(rows):
        while stack and rows[stack[-1]]["level"] >= row["level"]:
            stack.pop()
        row["parent_index"] = stack[-1] if stack else None
        row["child_indices"] = []
        if stack:
            rows[stack[-1]]["child_indices"].append(index)
        stack.append(index)
    for index, row in enumerate(rows):
        end = len(lines)
        for later in rows[index + 1 :]:
            if later["level"] <= row["level"]:
                end = later["line_index"]
                break
        row["end_index"] = end
        row["payload"] = "\n".join(lines[row["line_index"] + 1 : end]).strip()
    for row in rows:
        end = row["end_index"]
        cursor = row["line_index"] + 1
        parent_only = []
        for child_index in row["child_indices"]:
            child = rows[child_index]
            parent_only.extend(lines[cursor : child["line_index"]])
            cursor = child["end_index"]
        parent_only.extend(lines[cursor:end])
        row["parent_only_payload"] = "\n".join(parent_only).strip()
        ancestors = []
        parent = row["parent_index"]
        while parent is not None:
            ancestors.append(rows[parent]["heading"])
            parent = rows[parent]["parent_index"]
        row["ancestors"] = list(reversed(ancestors))
        stable = f"{source_label}|{' > '.join(row['ancestors'] + [row['heading']])}|{row['occurrence']}"
        row["id"] = f"{source_label}-{hashlib.sha256(stable.encode('utf-8')).hexdigest()[:20]}"
        row["heading_sha256"] = text_sha(row["heading"])
        row["payload_sha256"] = text_sha(row["payload"])
        row["parent_only_sha256"] = text_sha(row["parent_only_payload"])
    for row in rows:
        row["child_ids"] = [rows[index]["id"] for index in row["child_indices"]]
        row["child_union_sha256"] = hashlib.sha256(
            "|".join(rows[index]["payload_sha256"] for index in row["child_indices"]).encode("utf-8")
        ).hexdigest()
    return rows


def destination_blocks(file_name: str) -> list[dict]:
    rows = heading_blocks(TOPIC / file_name, file_name)
    for row in rows:
        row["anchor_id"] = hashlib.sha256(
            f"{file_name}|{normalise(row['heading'])}|{row['occurrence']}".encode("utf-8")
        ).hexdigest()[:20]
    return rows


def canonical_rows() -> list[dict]:
    return heading_blocks(CANONICAL, "canonical")


def matching_destination(source: dict, destination_rows: list[dict]) -> dict:
    matches = [
        row for row in destination_rows
        if normalise(row["heading"]) == normalise(source["heading"])
    ]
    if not matches:
        raise ValueError(f"No destination heading for canonical block: {source['heading']}")
    return matches[-1]


def parse_mcqs(text: str) -> list[dict]:
    matches = list(re.finditer(r"(?m)^## MCQ (\d+)\s*$", text))
    result = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end() : end]
        stem_match = re.search(r"\A\s*(.*?)\n\nA\.", block, re.S)
        options = dict(re.findall(r"(?m)^([A-D])\.\s+(.+?)\s*$", block))
        answer = re.search(r"\*\*Answer:\*\*\s*([A-D])", block)
        rationales = dict(re.findall(r"(?m)^- \*\*([A-D]):\*\*\s+(.+)$", block))
        result.append(
            {
                "number": int(match.group(1)),
                "stem": re.sub(r"\s+", " ", stem_match.group(1).strip()) if stem_match else "",
                "options": options,
                "answer": answer.group(1) if answer else None,
                "rationales": rationales,
                "block": block,
            }
        )
    return result


def parse_pyq_rows() -> list[dict]:
    year = None
    rows = []
    for line in read(PYQ_LEDGER).splitlines():
        year_match = re.match(r"^## (20\d{2})", line)
        if year_match:
            year = year_match.group(1)
        match = re.match(
            r"^- \*\*(Q\d+\([a-e]\)) · (\d+) marks(?: \([^)]*\))? · "
            r"\[Soul, Immortality, Rebirth and Liberation\]\([^)]+\):\*\* (.+)$",
            line,
        )
        if match:
            rows.append(
                {
                    "year": year,
                    "part": match.group(1),
                    "marks": int(match.group(2)),
                    "question": match.group(3),
                }
            )
    return rows


def parse_answers(toolkit: str, kind: str) -> list[dict]:
    pattern = (
        re.compile(r"(?m)^## Verified PYQ (\d+) — (20\d{2}) (Q\d+\([a-e]\)) · (\d+) marks\s*$")
        if kind == "verified"
        else re.compile(r"(?m)^## Original (\d+) · (\d+) marks\s*$")
    )
    matches = list(pattern.finditer(toolkit))
    result = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(toolkit)
        if kind == "verified" and index + 1 == len(matches):
            marker = toolkit.find("## Coverage-derived original Mains practice", match.end())
            if marker >= 0:
                end = marker
        block = toolkit[match.end() : end]
        question_label = "Exact verified question" if kind == "verified" else "Question"
        question = re.search(rf"(?m)^\*\*{question_label}:\*\*\s*(.+)$", block)
        answer = re.search(
            r"\*\*Independent model answer\*\*\s*(.*?)\n\n\*\*Measured model-answer words:\*\*",
            block,
            re.S,
        )
        declared = re.search(r"\*\*Measured model-answer words:\*\*\s*(\d+)", block)
        why = re.search(r"\*\*Why this structure earns marks:\*\*\s*(.+)", block)
        row = {
            "number": int(match.group(1)),
            "marks": int(match.group(4) if kind == "verified" else match.group(2)),
            "question": question.group(1).strip() if question else "",
            "answer": answer.group(1).strip() if answer else "",
            "declared": int(declared.group(1)) if declared else None,
            "why": why.group(1).strip() if why else "",
            "block": block,
        }
        if kind == "verified":
            row.update({"year": match.group(2), "part": match.group(3)})
        result.append(row)
    return result


def make_destination_record(file_name: str, row: dict) -> dict:
    return {
        "file": file_name,
        "anchor_kind": "heading",
        "anchor": row["heading"],
        "occurrence": row["occurrence"],
        "destination_line": row["line"],
        "destination_anchor_id": row["anchor_id"],
        "destination_payload_sha256": row["payload_sha256"],
        "destination_payload_words": word_count(row["payload"]),
        "parent_only_payload_sha256": row["parent_only_sha256"],
        "child_anchor_ids": [
            hashlib.sha256(
                f"{file_name}|{normalise(destination_blocks(file_name)[index]['heading'])}|"
                f"{destination_blocks(file_name)[index]['occurrence']}".encode("utf-8")
            ).hexdigest()[:20]
            for index in row["child_indices"]
        ],
        "child_union_sha256": row["child_union_sha256"],
        "mapping_method": "authored_canonical_heading_mapping",
    }


def build_review() -> dict:
    sources = canonical_rows()
    destinations = destination_blocks("REVISION-GUIDE.md")
    if len(sources) != 41 or set(CANONICAL_PROPOSITIONS) != {row["heading"] for row in sources}:
        raise ValueError("The authored canonical proposition table must match all 41 canonical headings exactly.")
    rows = []
    for source in sources:
        destination = matching_destination(source, destinations)
        proposition = CANONICAL_PROPOSITIONS[source["heading"]]
        transformed = any(
            (
                source["payload_sha256"] != destination["payload_sha256"],
                source["parent_only_sha256"] != destination["parent_only_sha256"],
                source["child_union_sha256"] != destination["child_union_sha256"],
            )
        )
        if source["heading"] in DOCTRINAL_CORRECTIONS:
            delta_note = (
                "The destination preserves the canonical question while correcting the mistaken "
                "inference from immortality alone to rebirth."
            )
        elif transformed:
            delta_note = (
                "The bounded destination differs because reviewed descendant or presentation "
                "material was transformed; the recorded parent-only and child-union hashes expose "
                "the exact structural delta."
            )
        else:
            delta_note = None
        rows.append(
            {
                "id": source["id"],
                "authority_source_type": "canonical_owner",
                "source_path": str(CANONICAL),
                "source_anchor": {
                    "heading": source["heading"],
                    "heading_occurrence": source["occurrence"],
                    "line": source["line"],
                    "ancestor_headings": source["ancestors"],
                },
                "source_heading_sha256": source["heading_sha256"],
                "source_payload_sha256": source["payload_sha256"],
                "source_payload_words": word_count(source["payload"]),
                "classification": "structural_umbrella" if source["child_ids"] else "covered_leaf",
                "source_structure": {
                    "parent_only_payload_sha256": source["parent_only_sha256"],
                    "parent_only_words": word_count(source["parent_only_payload"]),
                    "child_ids": source["child_ids"],
                    "child_union_sha256": source["child_union_sha256"],
                },
                "proposition": proposition,
                "proposition_sha256": text_sha(normalise(proposition)),
                "status": "covered_with_reviewed_transformation" if transformed else "covered",
                "delta_note": delta_note,
                "destinations": [make_destination_record("REVISION-GUIDE.md", destination)],
            }
        )
    toolkit_blocks = {row["heading"]: row for row in destination_blocks("ANSWER-WRITING-TOOLKIT.md")}
    solution_blocks = {row["heading"]: row for row in destination_blocks("MCQ-SOLUTIONS.md")}
    verified = parse_answers(read(TOPIC / "ANSWER-WRITING-TOOLKIT.md"), "verified")
    originals = parse_answers(read(TOPIC / "ANSWER-WRITING-TOOLKIT.md"), "original")
    mcqs = parse_mcqs(read(TOPIC / "MCQ-SOLUTIONS.md"))
    pyq_obligations = []
    for row in verified:
        heading = f"Verified PYQ {row['number']} — {row['year']} {row['part']} · {row['marks']} marks"
        destination = toolkit_blocks[heading]
        pyq_obligations.append(
            {
                "id": f"PYQ-{row['year']}-{row['part'].replace('(', '').replace(')', '')}",
                "source": str(PYQ_LEDGER),
                "question_sha256": text_sha(row["question"]),
                "proposition": f"{row['year']} {row['part']} is owned here and has an independently written {row['marks']}-mark model in the locked word band.",
                "destination": make_destination_record("ANSWER-WRITING-TOOLKIT.md", destination),
                "status": "verified_and_solved",
            }
        )
    practice_obligations = []
    for row in mcqs:
        destination = solution_blocks[f"MCQ {row['number']}"]
        practice_obligations.append(
            {
                "id": f"MCQ-{row['number']:02d}",
                "kind": "mcq",
                "proposition": row["stem"],
                "answer": row["answer"],
                "destination": make_destination_record("MCQ-SOLUTIONS.md", destination),
                "status": "implemented_and_explained",
            }
        )
    for row in originals:
        heading = f"Original {row['number']} · {row['marks']} marks"
        destination = toolkit_blocks[heading]
        practice_obligations.append(
            {
                "id": f"ORIGINAL-{row['number']:02d}",
                "kind": "original_mains",
                "proposition": row["question"],
                "destination": make_destination_record("ANSWER-WRITING-TOOLKIT.md", destination),
                "status": "implemented_and_solved",
            }
        )
    inbound_destination = matching_destination(
        next(row for row in destinations if row["heading"] == "Inbound obligation: diachronic personal identity and survival"),
        destinations,
    )
    return {
        "schema_version": 3,
        "authority_mode": "canonical_without_formal_session",
        "formal_session_reconciliation_performed": False,
        "frozen": True,
        "proof_model": "Authored canonical propositions mapped by exact reviewed heading identity; no reference row expansion, excerpt generation, similarity scoring or token-overlap destination selection.",
        "canonical_source": {
            "path": str(CANONICAL),
            "sha256": sha(CANONICAL),
            "heading_count": 41,
        },
        "supplementary_provenance": [
            {"path": str(REFERENCE_SESSION), "sha256": sha(REFERENCE_SESSION), "mandatory_rows": 0},
            {"path": str(REFERENCE_WORKBOOK), "sha256": sha(REFERENCE_WORKBOOK), "mandatory_rows": 0},
        ],
        "canonical_row_count": len(rows),
        "rows": rows,
        "inbound_obligations": [
            {
                "id": INBOUND_ID,
                "source_topic": "Paper I Topic 11 Quine and Strawson",
                "proposition": "Apply diachronic identity, branching and public identification conditions to survival, rebirth and resurrection claims without importing Paper I ownership.",
                "destination": make_destination_record("REVISION-GUIDE.md", inbound_destination),
                "testing": "MCQs 49-54",
                "answer_writing": "Originals 4-6",
                "status": "closed_in_destination",
            }
        ],
        "pyq_obligations": pyq_obligations,
        "practice_obligations": practice_obligations,
        "counts": {
            "canonical_rows": 41,
            "supplementary_reference_rows": 0,
            "inbound_routes": 1,
            "verified_pyqs": 17,
            "mcqs": 54,
            "original_mains": 6,
        },
        "limitations": [
            "canonical_without_formal_session is the only authority mode used.",
            "Reference learning-session and workbook files are supplementary provenance, not mandatory coverage rows.",
            "Hashes prove artifact identity and bounded mapping, not philosophical truth or examiner outcomes.",
        ],
    }


def build_audit(review: dict) -> dict:
    validation = validate_review(review)
    return {
        "schema_version": 3,
        "authority_mode": "canonical_without_formal_session",
        "formal_session_reconciliation_performed": False,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "canonical_review_file": "CANONICAL-COVERAGE-REVIEW.json",
        "canonical_review_sha256": text_sha(json.dumps(review, ensure_ascii=False, sort_keys=True)),
        "summary": validation,
        "canonical_rows": [
            {
                "id": row["id"],
                "source_payload_sha256": row["source_payload_sha256"],
                "proposition_sha256": row["proposition_sha256"],
                "destination_payload_sha256": row["destinations"][0]["destination_payload_sha256"],
                "status": row["status"],
            }
            for row in review["rows"]
        ],
        "counts": review["counts"],
        "pass": validation["pass"],
        "limitation": "Canonical-only audit under canonical_without_formal_session; no formal-session authority is claimed.",
    }


def refresh_coverage_artifacts() -> tuple[dict, dict]:
    review = build_review()
    (TOPIC / "CANONICAL-COVERAGE-REVIEW.json").write_text(
        json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    audit = build_audit(review)
    (TOPIC / "FORMAL-COVERAGE-AUDIT.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return review, audit


def validate_destination(record: dict, catalogs: dict[str, list[dict]]) -> tuple[bool, list[str]]:
    failures = []
    rows = catalogs.get(record.get("file"), [])
    resolved = next(
        (
            row for row in rows
            if row["heading"] == record.get("anchor")
            and row["occurrence"] == record.get("occurrence")
        ),
        None,
    )
    if not resolved:
        return False, ["destination_anchor_missing"]
    expected = make_destination_record(record["file"], resolved)
    for key in (
        "destination_anchor_id",
        "destination_payload_sha256",
        "destination_payload_words",
        "parent_only_payload_sha256",
        "child_anchor_ids",
        "child_union_sha256",
    ):
        if record.get(key) != expected.get(key):
            failures.append(f"destination_{key}_mismatch")
    return not failures, failures


def validate_review(review: dict) -> dict:
    failures = []
    codes = set()
    sources = canonical_rows()
    expected = {row["id"]: row for row in sources}
    rows = review.get("rows", [])
    actual = {row.get("id"): row for row in rows if row.get("id")}
    catalogs = {
        name: destination_blocks(name)
        for name in ("REVISION-GUIDE.md", "MCQ-SOLUTIONS.md", "ANSWER-WRITING-TOOLKIT.md")
    }
    if len(rows) != len(actual):
        codes.add("duplicate_source_id")
    if set(actual) != set(expected):
        codes.add("source_row_set_mismatch")
    for source_id, source in expected.items():
        row = actual.get(source_id)
        if not row:
            continue
        proposition = CANONICAL_PROPOSITIONS.get(source["heading"])
        field_checks = {
            "authority_source_type": row.get("authority_source_type") == "canonical_owner",
            "source_path": row.get("source_path") == str(CANONICAL),
            "source_heading": row.get("source_anchor", {}).get("heading") == source["heading"],
            "source_occurrence": row.get("source_anchor", {}).get("heading_occurrence") == source["occurrence"],
            "source_line": row.get("source_anchor", {}).get("line") == source["line"],
            "source_ancestors": row.get("source_anchor", {}).get("ancestor_headings") == source["ancestors"],
            "source_heading_hash": row.get("source_heading_sha256") == source["heading_sha256"],
            "source_payload_hash": row.get("source_payload_sha256") == source["payload_sha256"],
            "source_payload_words": row.get("source_payload_words") == word_count(source["payload"]),
            "classification": row.get("classification") == ("structural_umbrella" if source["child_ids"] else "covered_leaf"),
            "source_structure": row.get("source_structure") == {
                "parent_only_payload_sha256": source["parent_only_sha256"],
                "parent_only_words": word_count(source["parent_only_payload"]),
                "child_ids": source["child_ids"],
                "child_union_sha256": source["child_union_sha256"],
            },
            "authored_proposition": row.get("proposition") == proposition,
            "proposition_hash": row.get("proposition_sha256") == text_sha(normalise(proposition or "")),
        }
        destinations = row.get("destinations", [])
        if len(destinations) == 1:
            destination_record = destinations[0]
            transformed = any(
                (
                    source["payload_sha256"] != destination_record.get("destination_payload_sha256"),
                    source["parent_only_sha256"] != destination_record.get("parent_only_payload_sha256"),
                    source["child_union_sha256"] != destination_record.get("child_union_sha256"),
                )
            )
            field_checks["status"] = row.get("status") == (
                "covered_with_reviewed_transformation" if transformed else "covered"
            )
            field_checks["delta_note"] = (
                isinstance(row.get("delta_note"), str) and word_count(row["delta_note"]) >= 8
                if transformed
                else row.get("delta_note") is None
            )
        else:
            transformed = False
        for name, passed in field_checks.items():
            if not passed:
                codes.add(f"{name}_mismatch")
                failures.append({"id": source_id, "reason": f"{name}_mismatch"})
        if len(destinations) != 1:
            codes.add("destination_count_mismatch")
            failures.append({"id": source_id, "reason": "destination_count_mismatch"})
        else:
            passed, destination_codes = validate_destination(destinations[0], catalogs)
            if not passed:
                codes.update(destination_codes)
                failures.extend({"id": source_id, "reason": code} for code in destination_codes)
        if row.get("classification") == "covered_leaf" and (
            row.get("source_payload_words", 0) <= 0
            or not destinations
            or destinations[0].get("destination_payload_words", 0) <= 0
        ):
            codes.add("covered_leaf_zero_words")
            failures.append({"id": source_id, "reason": "covered_leaf_zero_words"})
    expected_counts = {
        "canonical_rows": 41,
        "supplementary_reference_rows": 0,
        "inbound_routes": 1,
        "verified_pyqs": 17,
        "mcqs": 54,
        "original_mains": 6,
    }
    structural_checks = {
        "authority_mode": review.get("authority_mode") == "canonical_without_formal_session",
        "formal_reconciliation_false": review.get("formal_session_reconciliation_performed") is False,
        "frozen": review.get("frozen") is True,
        "canonical_count": len(rows) == 41,
        "reference_rows_zero": all(row.get("mandatory_rows") == 0 for row in review.get("supplementary_provenance", [])),
        "counts": review.get("counts") == expected_counts,
        "inbound": len(review.get("inbound_obligations", [])) == 1
        and review["inbound_obligations"][0].get("id") == INBOUND_ID
        and review["inbound_obligations"][0].get("status") == "closed_in_destination",
        "pyqs": len(review.get("pyq_obligations", [])) == 17,
        "practice": len(review.get("practice_obligations", [])) == 60,
        "no_reference_mandatory_rows": all(row.get("authority_source_type") == "canonical_owner" for row in rows),
    }
    for name, passed in structural_checks.items():
        if not passed:
            codes.add(name)
    for collection in ("inbound_obligations", "pyq_obligations", "practice_obligations"):
        for obligation in review.get(collection, []):
            destination = obligation.get("destination")
            if destination:
                passed, destination_codes = validate_destination(destination, catalogs)
                if not passed:
                    codes.update(destination_codes)
                    failures.extend({"id": obligation.get("id"), "reason": code} for code in destination_codes)
    checks = {**structural_checks, "no_failures": not failures and not codes}
    return {
        "row_count": len(rows),
        "canonical_rows": len(rows),
        "supplementary_reference_rows": 0,
        "pyq_obligations": len(review.get("pyq_obligations", [])),
        "practice_obligations": len(review.get("practice_obligations", [])),
        "failure_codes": sorted(codes),
        "failures": failures,
        "checks": checks,
        "pass": all(checks.values()),
    }


def coverage_checks() -> dict:
    review = json.loads(read(TOPIC / "CANONICAL-COVERAGE-REVIEW.json"))
    audit = json.loads(read(TOPIC / "FORMAL-COVERAGE-AUDIT.json"))
    validation = validate_review(review)
    expected_audit = build_audit(review)
    audit_checks = {
        "authority_mode": audit.get("authority_mode") == "canonical_without_formal_session",
        "formal_reconciliation_false": audit.get("formal_session_reconciliation_performed") is False,
        "review_hash": audit.get("canonical_review_sha256") == expected_audit["canonical_review_sha256"],
        "summary_current": audit.get("summary") == expected_audit["summary"],
        "rows_current": audit.get("canonical_rows") == expected_audit["canonical_rows"],
        "counts_current": audit.get("counts") == expected_audit["counts"],
        "audit_pass": audit.get("pass") is True,
    }
    failure_codes = set(validation["failure_codes"])
    failure_codes.update(f"audit_{name}_mismatch" for name, passed in audit_checks.items() if not passed)
    return {
        **validation,
        "audit_checks": audit_checks,
        "failure_codes": sorted(failure_codes),
        "pass": validation["pass"] and all(audit_checks.values()),
    }


def source_checks() -> dict:
    provenance = json.loads(read(TOPIC / "SOURCE-PROVENANCE.json"))
    expected = {
        str(CANONICAL): sha(CANONICAL),
        str(PYQ_LEDGER): sha(PYQ_LEDGER),
        str(PYQ_2026): sha(PYQ_2026),
        str(REFERENCE_SESSION): sha(REFERENCE_SESSION),
        str(REFERENCE_WORKBOOK): sha(REFERENCE_WORKBOOK),
    }
    recorded = {provenance["primary_authority"]["path"]: provenance["primary_authority"]["sha256"]}
    recorded.update({row["path"]: row["sha256"] for row in provenance["verified_pyq_ledgers"]})
    recorded.update({row["path"]: row["sha256"] for row in provenance["reference_only"]})
    formal = provenance["formal_authority_check"]
    checks = {
        "authority_mode": provenance.get("authority_mode") == "canonical_without_formal_session",
        "hashes_current": expected == recorded,
        "formal_ineligible": formal.get("completed_formal_source_eligible") is False,
        "formal_candidates_not_used": formal.get("candidate_files_read_hashed_or_used") is False,
        "limitations_present": len(provenance.get("limitations", [])) >= 3,
    }
    return {
        "recorded_sources": recorded,
        "current_sources": expected,
        "checks": checks,
        "failure_codes": [name for name, passed in checks.items() if not passed],
        "pass": all(checks.values()),
    }


def false_sufficiency_hits(text: str) -> list[str]:
    flattened = re.sub(r"\s+", " ", text)
    patterns = (
        r"(?i)(?:immortality(?: of (?:a |the )?(?:substantial )?soul)?|(?:a |the )?(?:persisting|immortal|substantial) soul)"
        r".{0,55}(?:is |may be |would be |would guarantee |guarantees )?suff(?:icient|\.)"
        r".{0,35}(?:for )?rebirth",
        r"(?i)(?:immortality|soul).{0,45}suff(?:icient|\.).{0,25}not necessar",
    )
    hits = []
    for pattern in patterns:
        for match in re.finditer(pattern, flattened):
            value = match.group(0)
            normalized = normalise(value)
            if (
                "not sufficient" in normalized
                or "neither sufficient" in normalized
                or "insufficient" in normalized
                or "mistaken inference" in normalized
            ):
                continue
            hits.append(value)
    return sorted(set(hits))


def extracted_pdf_text(path: Path) -> str:
    with fitz.open(path) as document:
        return "\n".join(page.get_text("text") for page in document)


def doctrine_checks() -> dict:
    markdown_names = sorted(path.name for path in TOPIC.glob("*.md"))
    json_names = (
        "MCQ-AUDIT.json",
        "CANONICAL-COVERAGE-REVIEW.json",
        "FORMAL-COVERAGE-AUDIT.json",
        "VALIDATION.json",
    )
    artifacts = {name: read(TOPIC / name) for name in markdown_names}
    audit_data = json.loads(read(TOPIC / "MCQ-AUDIT.json"))
    asserted_mcq_text = "\n".join(
        (
            row["stem"]
            + "\n"
            + row["options"][row["answer"]]["text"]
            + "\n"
            + row["options"][row["answer"]]["rationale"]
        )
        for row in audit_data["questions"]
    )
    artifacts["MCQ-QUESTIONS.md"] = asserted_mcq_text
    artifacts["MCQ-SOLUTIONS.md"] = asserted_mcq_text
    for name in json_names:
        path = TOPIC / name
        if not path.is_file():
            continue
        if name == "VALIDATION.json":
            data = json.loads(read(path))
            data.get("checks", {}).pop("doctrine", None)
            artifacts[name] = json.dumps(data, ensure_ascii=False)
        elif name == "MCQ-AUDIT.json":
            artifacts[name] = asserted_mcq_text
        else:
            artifacts[name] = read(path)
    distractors = [
        normalise(option["text"])
        for row in audit_data["questions"]
        for letter, option in row["options"].items()
        if letter != row["answer"]
    ]
    for pdf_name in PDF_SOURCES:
        path = TOPIC / "pdf" / pdf_name
        if path.is_file():
            artifacts[f"pdf/{pdf_name}"] = extracted_pdf_text(path)
    per_artifact = {}
    for name, text in artifacts.items():
        normalized = normalise(text)
        hits = false_sufficiency_hits(text)
        if name in (
            "MCQ-QUESTIONS.md",
            "MCQ-SOLUTIONS.md",
            "MCQ-AUDIT.json",
            "pdf/MCQ-Questions.pdf",
            "pdf/MCQ-Solutions.pdf",
        ):
            hits = [
                hit for hit in hits
                if not any(
                    normalise(hit) in distractor or distractor in normalise(hit)
                    for distractor in distractors
                )
            ]
        required = {
            "not_sufficient": "immortality alone is not sufficient for rebirth" in normalized,
            "additional_doctrine": (
                "additional transmigration or re-embodiment doctrine" in normalized
                or "transmigration or re-embodiment" in normalized
            ),
            "not_necessary": "substantial immortal soul is not necessary" in normalized,
            "buddhist_countermodel": "buddhist causal continuity" in normalized,
        }
        doctrine_surface = any(
            token in normalized
            for token in ("immortality", "rebirth", "transmigration", "buddhist causal continuity")
        )
        per_artifact[name] = {
            "false_sufficiency_hits": hits,
            "required_when_doctrine_surface": required if doctrine_surface else {},
            "pass": not hits,
        }
    required_union = {
        "not_sufficient": any(
            row.get("required_when_doctrine_surface", {}).get("not_sufficient")
            for row in per_artifact.values()
        ),
        "additional_doctrine": any(
            row.get("required_when_doctrine_surface", {}).get("additional_doctrine")
            for row in per_artifact.values()
        ),
        "not_necessary": any(
            row.get("required_when_doctrine_surface", {}).get("not_necessary")
            for row in per_artifact.values()
        ),
        "buddhist_countermodel": any(
            row.get("required_when_doctrine_surface", {}).get("buddhist_countermodel")
            for row in per_artifact.values()
        ),
    }
    codes = [
        f"false_rebirth_sufficiency:{name}"
        for name, row in per_artifact.items()
        if row["false_sufficiency_hits"]
    ]
    codes.extend(f"missing_{name}" for name, passed in required_union.items() if not passed)
    return {
        "artifacts": per_artifact,
        "required_union": required_union,
        "failure_codes": codes,
        "pass": not codes,
    }


def mcq_checks(questions_text: str, solutions_text: str) -> dict:
    questions = parse_mcqs(questions_text)
    solutions = parse_mcqs(solutions_text)
    audit = json.loads(read(TOPIC / "MCQ-AUDIT.json"))
    answer_key = "".join(row["answer"] or "" for row in solutions)
    distribution = Counter(answer_key)
    runs = [len(list(group)) for _, group in itertools.groupby(answer_key)]
    cue_hits = [
        {"number": row["number"], "letter": letter, "text": text}
        for row in questions
        for letter, text in row["options"].items()
        if any(filler in text.casefold() for filler in FORBIDDEN_MCQQ_FILLER)
    ]
    item_spreads = []
    correct_lengths = []
    distractor_lengths = []
    unique_correct_longest = []
    for row in solutions:
        lengths = {letter: word_count(text) for letter, text in row["options"].items()}
        item_spreads.append(max(lengths.values()) - min(lengths.values()))
        maximum = max(lengths.values())
        if list(lengths.values()).count(maximum) == 1 and lengths[row["answer"]] == maximum:
            unique_correct_longest.append(row["number"])
        for letter, length in lengths.items():
            (correct_lengths if letter == row["answer"] else distractor_lengths).append(length)
    average_correct = sum(correct_lengths) / len(correct_lengths)
    average_distractor = sum(distractor_lengths) / len(distractor_lengths)
    audit_key = "".join(row["answer"] for row in audit.get("questions", []))
    audit_parity = all(
        audit_row.get("stem") == solution["stem"]
        and audit_row.get("answer") == solution["answer"]
        and all(
            audit_row.get("options", {}).get(letter, {}).get("text") == solution["options"][letter]
            and audit_row.get("options", {}).get(letter, {}).get("rationale") == solution["rationales"][letter]
            for letter in "ABCD"
        )
        for audit_row, solution in zip(audit.get("questions", []), solutions)
    )
    cells = Counter(row.get("coverage_cell") for row in audit.get("questions", []))
    checks = {
        "counts": len(questions) == len(solutions) == audit.get("question_count") == 54,
        "numbering": [row["number"] for row in questions] == list(range(1, 55))
        and [row["number"] for row in solutions] == list(range(1, 55)),
        "parity": all(
            left["stem"] == right["stem"] and left["options"] == right["options"]
            for left, right in zip(questions, solutions)
        ),
        "four_options": all(set(row["options"]) == set("ABCD") for row in questions),
        "four_rationales": all(set(row["rationales"]) == set("ABCD") for row in solutions),
        "wrong_option_specificity": all(
            row["options"][letter] in row["rationales"][letter]
            for row in solutions for letter in "ABCD" if letter != row["answer"]
        ),
        "audit_parity": audit_parity,
        "audit_key": answer_key == audit.get("answer_key") == audit_key,
        "distribution": max(distribution.values()) - min(distribution.values()) <= 2,
        "maximum_run": max(runs) <= 2,
        "not_rotation": "ABCDABCD" not in answer_key and "DCBADCBA" not in answer_key,
        "question_leakage": not any(
            marker in questions_text
            for marker in ("**Answer:**", "**Option explanations:**", "**Correct answer:")
        ),
        "no_parenthetical_filler": not cue_hits,
        "option_length_balance": max(item_spreads) <= 12,
        "correct_not_uniquely_long": len(unique_correct_longest) / len(solutions) <= 0.35,
        "aggregate_length_ratio": 0.75 <= average_correct / average_distractor <= 1.25,
        "unique_stems": len({normalise(row["stem"]) for row in questions}) == 54,
        "unique_options": all(len({normalise(text) for text in row["options"].values()}) == 4 for row in questions),
        "all_coverage_cells": all(cells.get(f"C{index:02d}", 0) > 0 for index in range(1, 13)),
    }
    codes = [
        "question_answer_leakage" if name == "question_leakage" else f"mcq_{name}"
        for name, passed in checks.items() if not passed
    ]
    return {
        "answer_key": answer_key,
        "distribution": dict(distribution),
        "maximum_run": max(runs),
        "cue_hits": cue_hits,
        "maximum_option_word_spread": max(item_spreads),
        "unique_correct_longest": unique_correct_longest,
        "average_correct_option_words": average_correct,
        "average_distractor_option_words": average_distractor,
        "coverage_cell_counts": dict(cells),
        "checks": checks,
        "failure_codes": codes,
        "pass": all(checks.values()),
    }


def answer_checks(toolkit: str) -> dict:
    expected = parse_pyq_rows()
    verified = parse_answers(toolkit, "verified")
    originals = parse_answers(toolkit, "original")
    verified_rows = []
    for expected_row, actual in zip(expected, verified):
        computed = word_count(actual["answer"])
        minimum, maximum = WORD_BANDS[actual["marks"]]
        verified_rows.append(
            {
                "id": f"{actual.get('year')} {actual.get('part')}",
                "exact_question": actual["question"] == expected_row["question"],
                "year_part_marks": (
                    actual.get("year"), actual.get("part"), actual["marks"]
                ) == (
                    expected_row["year"], expected_row["part"], expected_row["marks"]
                ),
                "declared": actual["declared"],
                "computed": computed,
                "declared_equals_computed": actual["declared"] == computed,
                "within_band": minimum <= computed <= maximum,
                "why_present": len(words(actual["why"])) >= 8,
            }
        )
    original_rows = []
    for actual in originals:
        computed = word_count(actual["answer"])
        minimum, maximum = WORD_BANDS[actual["marks"]]
        original_rows.append(
            {
                "number": actual["number"],
                "marks": actual["marks"],
                "declared": actual["declared"],
                "computed": computed,
                "declared_equals_computed": actual["declared"] == computed,
                "within_band": minimum <= computed <= maximum,
                "why_present": len(words(actual["why"])) >= 8,
            }
        )
    checks = {
        "verified_count": len(expected) == len(verified) == 17,
        "verified_exact": all(
            row["exact_question"] and row["year_part_marks"]
            and row["declared_equals_computed"] and row["within_band"] and row["why_present"]
            for row in verified_rows
        ),
        "no_2026_owner": "Soul, Immortality, Rebirth and Liberation](./philosophy-of-religion/Soul-Immortality-Rebirth.md)"
        not in "\n".join(line for line in read(PYQ_2026).splitlines() if re.match(r"^- \*\*Q", line)),
        "original_count": len(originals) == 6,
        "original_marks": Counter(row["marks"] for row in originals) == Counter({10: 2, 15: 2, 20: 2}),
        "original_bands": all(
            row["declared_equals_computed"] and row["within_band"] and row["why_present"]
            for row in original_rows
        ),
        "independent_disclaimer": "not official UPSC answer keys" in toolkit,
    }
    codes = []
    if not checks["verified_count"]:
        codes.append("verified_pyq_count_mismatch")
    if any(not row["exact_question"] for row in verified_rows):
        codes.append("verified_question_wording_mismatch")
    if any(not row["declared_equals_computed"] for row in verified_rows + original_rows):
        codes.append("declared_word_count_mismatch")
    if any(not row["within_band"] for row in verified_rows + original_rows):
        codes.append("timed_word_band_mismatch")
    codes.extend(f"answer_{name}" for name, passed in checks.items() if not passed and not codes)
    return {
        "verified": verified_rows,
        "originals": original_rows,
        "checks": checks,
        "failure_codes": sorted(set(codes)),
        "pass": all(checks.values()),
    }


def visual_checks(revision: str) -> dict:
    checks = {
        "minimum_fenced_visuals": len(re.findall(r"(?m)^```", revision)) // 2 >= 20,
        "minimum_tables": len(re.findall(r"(?m)^\|[-:| ]+\|$", revision)) >= 20,
        "inbound_identity_flow": "QUALITATIVE SIMILARITY" in revision and "NUMERICAL IDENTITY" in revision,
        "inbound_strawson_flow": "CLAIM: an immaterial soul survives" in revision,
        "final_register_notes_last": revision.rfind("## Final consolidated register notes")
        > revision.rfind("## Canonical authority appendix"),
    }
    return {"checks": checks, "failure_codes": [f"visual_{name}" for name, passed in checks.items() if not passed], "pass": all(checks.values())}


def provenance_wording_checks(texts: dict[str, str]) -> dict:
    combined = "\n".join(texts.values())
    forbidden = {
        "claims_formal_reconciliation": r"(?i)(completed|authoritative) formal (learning )?(session|source).{0,40}(used|reconciled|authority)",
        "claims_formal_coverage": r"(?i)formal-session reconciliation (?:was|has been) (?:performed|completed)",
        "claims_reference_authority": r"(?i)reference-only files? (?:is|are) (?:the )?(?:primary|formal) authority",
    }
    hits = {name: [match.group(0) for match in re.finditer(pattern, combined)] for name, pattern in forbidden.items()}
    normalized = normalise(combined)
    required = {
        "authority_mode_visible": "canonical_without_formal_session" in combined,
        "no_formal_claim_visible": "no completed formal learning session or formal workbook is claimed or reconciled" in normalized,
        "reference_only_visible": "derivative reference evidence only" in combined,
        "mechanical_limit_visible": "Mechanical validation does not prove" in combined,
    }
    codes = [name for name, values in hits.items() if values]
    codes.extend(f"missing_{name}" for name, passed in required.items() if not passed)
    return {"required": required, "forbidden_hits": hits, "failure_codes": codes, "pass": all(required.values()) and not any(hits.values())}


def regenerate_pdfs(selected: set[str] | None = None) -> dict:
    sys.path.insert(0, str(TOOLS))
    import unicode_markdown_pdf

    files = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        if selected is not None and pdf_name not in selected:
            continue
        output = TOPIC / "pdf" / pdf_name
        output.unlink(missing_ok=True)
        source_path = TOPIC / source_name
        source_text = read(source_path)
        normalized_lines = []
        previous_level = 1
        for line in source_text.splitlines():
            match = re.match(r"^(#{1,6})(\s+.*)$", line)
            if match:
                level = min(len(match.group(1)), previous_level + 1)
                line = "#" * level + match.group(2)
                previous_level = level
            normalized_lines.append(line)
        with tempfile.TemporaryDirectory(prefix="soul-pdf-") as temporary:
            render_source = Path(temporary) / source_name
            render_source.write_text("\n".join(normalized_lines) + "\n", encoding="utf-8")
            unicode_markdown_pdf.build_pdf(
                render_source,
                output,
                internal_index=True,
                index_title="CONTENTS",
                cover_descriptor=PDF_DESCRIPTORS[pdf_name],
                footer_label=f"Soul, Immortality and Rebirth | {source_name.removesuffix('.md')}",
            )
        files[pdf_name] = {
            "source": source_name,
            "source_sha256": sha(source_path),
            "sha256": sha(output),
            "bytes": output.stat().st_size,
        }
    return {
        "mechanism": "C:/up/tools/unicode_markdown_pdf.py via Chrome and PyMuPDF",
        "requested": True,
        "selected": sorted(selected) if selected is not None else sorted(PDF_SOURCES),
        "all_four_regenerated": len(files) == 4,
        "files": files,
    }


def pdf_check(path: Path, source: Path, record: dict | None) -> dict:
    blank = []
    replacements = 0
    bounds = []
    overlaps = []
    markdown = []
    with fitz.open(path) as document:
        extracted_pages = []
        for page_number, page in enumerate(document, 1):
            text = page.get_text("text")
            extracted_pages.append(text)
            if len(text.strip()) < 20 and not page.get_images(full=True):
                blank.append(page_number)
            replacements += text.count("\ufffd")
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
                for first_index, first in enumerate(blocks):
                    first_rect = fitz.Rect(first[:4])
                    for second in blocks[first_index + 1 :]:
                        second_rect = fitz.Rect(second[:4])
                        intersection = first_rect & second_rect
                        smaller = min(first_rect.get_area(), second_rect.get_area())
                        if smaller and not intersection.is_empty and intersection.get_area() / smaller > 0.4:
                            overlaps.append(page_number)
                            break
                    if overlaps and overlaps[-1] == page_number:
                        break
        extracted = "\n".join(extracted_pages)
        pages = document.page_count
        metadata = document.metadata
    source_headings = [match.group(1) for match in re.finditer(r"(?m)^##\s+(.+?)\s*$", read(source))]
    extracted_norm = normalise(extracted)
    missing = []
    for heading in source_headings:
        probe = " ".join(normalise(heading).split()[:6])
        if probe and probe not in extracted_norm:
            missing.append(heading)
    current = {"source_sha256": sha(source), "sha256": sha(path)}
    checks = {
        "pages": pages > 0,
        "no_blank": not blank,
        "no_replacement_glyph": replacements == 0,
        "no_out_of_bounds": not bounds,
        "no_overlap": not overlaps,
        "no_raw_markdown": not markdown,
        "heading_parity": not missing,
        "descriptor": normalise(PDF_DESCRIPTORS[path.name]) in extracted_norm,
        "metadata_title": bool(metadata.get("title")),
        "hash_identity": bool(record) and all(record.get(key) == current[key] for key in current),
    }
    return {
        "pages": pages,
        "bytes": path.stat().st_size,
        "blank_pages": blank,
        "replacement_glyphs": replacements,
        "out_of_bounds_pages": sorted(set(bounds)),
        "overlap_pages": sorted(set(overlaps)),
        "raw_markdown": markdown,
        "missing_headings": missing,
        "metadata": metadata,
        "current": current,
        "checks": checks,
        "failure_codes": [f"pdf_{name}" for name, passed in checks.items() if not passed],
        "pass": all(checks.values()),
    }


def text_and_temp_checks() -> dict:
    text_failures = []
    inspected = []
    for path in sorted(TOPIC.rglob("*")):
        if not path.is_file() or path.suffix.lower() == ".pdf":
            continue
        inspected.append(str(path.relative_to(TOPIC)))
        try:
            text = read(path)
        except UnicodeDecodeError:
            text_failures.append(f"{path.name}: invalid UTF-8")
            continue
        if "\x00" in text or "\ufffd" in text:
            text_failures.append(f"{path.name}: invalid character")
    temporary = sorted(
        str(path.relative_to(TOPIC))
        for pattern in ("*.tmp", "*_data.py", "*.render.html", "*.layout-pass.pdf", "*.finalized.pdf", "*.pyc")
        for path in TOPIC.rglob(pattern)
    )
    temporary += sorted(str(path.relative_to(TOPIC)) for path in TOPIC.rglob("__pycache__") if path.is_dir())
    diff = subprocess.run(
        ["git", "-C", str(REPO.parent), "diff", "--check", "--", str(DEFAULT_TOPIC)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return {
        "inspected": inspected,
        "text_failures": text_failures,
        "temporary": temporary,
        "git_diff_check_stdout": diff.stdout,
        "git_diff_check_stderr": diff.stderr,
        "pass": not text_failures and not temporary and diff.returncode == 0,
    }


def artifact_integrity() -> dict:
    hashes = {}
    missing = []
    for name in REQUIRED:
        path = TOPIC / name
        if not path.is_file():
            missing.append(name)
            continue
        if name != "VALIDATION.json":
            hashes[name] = sha(path)
    return {
        "algorithm": "sha256",
        "files": hashes,
        "missing": missing,
        "validation_json_policy": "Required release artifact; excluded from its own embedded hash manifest to avoid self-hash recursion.",
        "deterministic_order": sorted(hashes) == list(sorted(hashes)),
        "pass": not missing,
    }


def atomic_write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def release_integrity() -> dict:
    rows = []
    for name in REQUIRED:
        path = TOPIC / name
        working_sha256 = sha(path) if path.is_file() else None
        try:
            relative = path.relative_to(REPO.parent)
        except ValueError:
            rows.append(
                {
                    "path": name,
                    "working_sha256": working_sha256,
                    "staged_sha256": None,
                    "staged_blob_present": False,
                    "staged_matches_worktree": False,
                }
            )
            continue
        relative_posix = str(relative).replace("\\", "/")
        staged_object = subprocess.run(
            ["git", "-C", str(REPO.parent), "rev-parse", f":{relative_posix}"],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        working_object = subprocess.run(
            [
                "git",
                "-C",
                str(REPO.parent),
                "hash-object",
                f"--path={relative_posix}",
                str(path),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        staged_oid = staged_object.stdout.strip() if staged_object.returncode == 0 else None
        working_oid = working_object.stdout.strip() if working_object.returncode == 0 else None
        rows.append(
            {
                "path": name,
                "working_sha256": working_sha256,
                "working_git_oid": working_oid,
                "staged_git_oid": staged_oid,
                "staged_blob_present": staged_oid is not None,
                "staged_matches_worktree": (
                    working_oid is not None and staged_oid == working_oid
                ),
            }
        )
    return {
        "files": rows,
        "pass": all(
            row["staged_blob_present"] and row["staged_matches_worktree"]
            for row in rows
        ),
        "validation_mode": (
            "Precommit verification is non-mutating. Every required artifact, including "
            "VALIDATION.json, must already be staged with the same Git clean-filter-normalized "
            "content as the final working tree."
        ),
    }


def flatten_strings(value) -> list[str]:
    if isinstance(value, dict):
        return [item for child in value.values() for item in flatten_strings(child)]
    if isinstance(value, list):
        return [item for child in value for item in flatten_strings(child)]
    return [str(value)]


def run_negative_case(
    name: str,
    mutation,
    expected_code: str,
    mode: str = "development",
    expect_validation_unchanged: bool = False,
) -> dict:
    with tempfile.TemporaryDirectory(prefix="soul-validator-negative-") as temporary:
        case = Path(temporary) / "04-Soul-Immortality-Rebirth"
        shutil.copytree(TOPIC, case, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        validation_sha_before = sha(case / "VALIDATION.json")
        mutation(case)
        environment = os.environ.copy()
        environment["SOUL_TOPIC_ROOT"] = str(case)
        environment["SOUL_REPO_ROOT"] = str(REPO)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        completed = subprocess.run(
            [sys.executable, "-B", str(case / "validate_package.py"), "--mode", mode, "--skip-negative-tests"],
            cwd=case,
            env=environment,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=300,
        )
        report = json.loads(read(case / "VALIDATION.json"))
        observed = set(flatten_strings(report))
        observed.update(completed.stdout.split())
        observed.update(completed.stderr.split())
        diagnostic_observed = (
            expected_code in observed
            or expected_code in completed.stdout
            or expected_code in completed.stderr
        )
        validation_sha_after = sha(case / "VALIDATION.json")
        validation_unchanged = validation_sha_before == validation_sha_after
        return {
            "name": name,
            "expected_diagnostic": expected_code,
            "exit_code": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "rejected": completed.returncode != 0,
            "diagnostic_observed": diagnostic_observed,
            "validation_sha256_before": validation_sha_before,
            "validation_sha256_after": validation_sha_after,
            "validation_unchanged": validation_unchanged,
            "pass": completed.returncode != 0
            and diagnostic_observed
            and (validation_unchanged if expect_validation_unchanged else True),
        }


def production_negative_tests() -> dict:
    tests = [
        run_negative_case(
            "missing required Markdown",
            lambda case: (case / "README.md").unlink(),
            "missing_required_markdown",
        ),
        run_negative_case(
            "precommit missing Markdown is non-mutating",
            lambda case: (case / "README.md").unlink(),
            "missing_required_markdown",
            mode="precommit",
            expect_validation_unchanged=True,
        ),
        run_negative_case(
            "missing required audit JSON",
            lambda case: (case / "MCQ-AUDIT.json").unlink(),
            "missing_required_audit_json",
        ),
        run_negative_case(
            "missing validator source input",
            lambda case: (case / "SOURCE-PROVENANCE.json").unlink(),
            "missing_validator_input",
        ),
        run_negative_case(
            "missing required PDF",
            lambda case: (case / "pdf/MCQ-Questions.pdf").unlink(),
            "missing_required_pdf",
        ),
        run_negative_case(
            "canonical source hash corruption",
            lambda case: mutate_json(case / "CANONICAL-COVERAGE-REVIEW.json", ("rows", 0, "source_payload_sha256"), "0" * 64),
            "source_payload_hash_mismatch",
        ),
        run_negative_case(
            "destination payload corruption",
            lambda case: mutate_json(case / "CANONICAL-COVERAGE-REVIEW.json", ("rows", 0, "destinations", 0, "destination_payload_sha256"), "0" * 64),
            "destination_destination_payload_sha256_mismatch",
        ),
        run_negative_case(
            "MCQ cue and answer leakage",
            lambda case: (case / "MCQ-QUESTIONS.md").write_text(
                read(case / "MCQ-QUESTIONS.md") + "\n**Answer:** A\n(for the conceptual distinction at issue)\n",
                encoding="utf-8",
            ),
            "question_answer_leakage",
        ),
        run_negative_case(
            "stale PDF source integrity",
            lambda case: (case / "REVISION-GUIDE.md").write_text(
                read(case / "REVISION-GUIDE.md") + "\n<!-- stale-source-mutation -->\n",
                encoding="utf-8",
            ),
            "pdf_hash_identity",
        ),
        run_negative_case(
            "release readiness and staging",
            lambda case: None,
            "release_integrity",
            mode="precommit",
        ),
    ]
    return {
        "mechanism": "Each case copies the complete package, mutates a real artifact, invokes the copied production validate_package.py entry point, and checks non-zero exit plus the expected diagnostic.",
        "tests": tests,
        "passed": sum(row["pass"] for row in tests),
        "failed": sum(not row["pass"] for row in tests),
        "pass": all(row["pass"] for row in tests),
    }


def mutate_json(path: Path, keys: tuple, value) -> None:
    data = json.loads(read(path))
    cursor = data
    for key in keys[:-1]:
        cursor = cursor[key]
    cursor[keys[-1]] = value
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def missing_required_codes(missing: list[str]) -> list[str]:
    codes = {"required_files"}
    for name in missing:
        if name.lower().endswith(".md"):
            codes.add("missing_required_markdown")
        if name.endswith("AUDIT.json"):
            codes.add("missing_required_audit_json")
        if name == "SOURCE-PROVENANCE.json":
            codes.add("missing_validator_input")
        if name.lower().endswith(".pdf"):
            codes.add("missing_required_pdf")
        codes.add(f"missing:{name}")
    return sorted(codes)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regenerate", action="store_true")
    parser.add_argument("--regenerate-pdf", choices=tuple(PDF_SOURCES))
    parser.add_argument("--refresh-coverage", action="store_true")
    parser.add_argument("--skip-negative-tests", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--mode", choices=("development", "precommit"), default="development")
    args = parser.parse_args()

    if args.mode == "precommit" and (
        args.refresh_coverage or args.regenerate or args.regenerate_pdf
    ):
        diagnostic = {
            "result": "FAIL",
            "release_ready": False,
            "failure_codes": ["precommit_mutation_option_forbidden"],
        }
        print(json.dumps(diagnostic, sort_keys=True), file=sys.stderr)
        return 1

    if args.refresh_coverage:
        refresh_coverage_artifacts()

    prior = {}
    if VALIDATION.is_file():
        try:
            prior = json.loads(read(VALIDATION)).get("pdf_generation", {})
        except (OSError, json.JSONDecodeError):
            prior = {}
    regeneration = prior
    if args.regenerate or args.regenerate_pdf:
        partial = regenerate_pdfs({args.regenerate_pdf} if args.regenerate_pdf else None)
        files = dict(prior.get("files", {}))
        files.update(partial["files"])
        regeneration = {**partial, "files": files, "all_four_regenerated": set(files) == set(PDF_SOURCES)}

    required = {name: (TOPIC / name).is_file() for name in REQUIRED}
    failures = []
    if not all(required.values()):
        missing = [name for name, present in required.items() if not present]
        failure_codes = missing_required_codes(missing)
        report = {
            "schema_version": 2,
            "topic": "04 Soul, Immortality and Rebirth",
            "authority_mode": "canonical_without_formal_session",
            "formal_session_reconciliation_performed": False,
            "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "validation_mode": args.mode,
            "result": "FAIL",
            "release_ready": False,
            "checks": {
                "required_files": required,
                "missing_required": missing,
                "failure_codes": failure_codes,
            },
            "failures": failure_codes,
            "mechanical_limit": "Validation stopped safely because required package inputs were missing.",
        }
        if args.mode == "development":
            atomic_write_json(VALIDATION, report)
        print(
            json.dumps(
                {
                    "result": "FAIL",
                    "release_ready": False,
                    "failure_codes": failure_codes,
                    "missing_required": missing,
                },
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 1
    text_names = (
        "README.md",
        "REVISION-GUIDE.md",
        "MCQ-QUESTIONS.md",
        "MCQ-SOLUTIONS.md",
        "ANSWER-WRITING-TOOLKIT.md",
        "COVERAGE-LEDGER.md",
        "PRACTICE-LOG.md",
    )
    texts = {name: read(TOPIC / name) for name in text_names if (TOPIC / name).is_file()}
    source = source_checks()
    coverage = coverage_checks()
    doctrine = doctrine_checks()
    visuals = visual_checks(texts["REVISION-GUIDE.md"])
    mcqs = mcq_checks(texts["MCQ-QUESTIONS.md"], texts["MCQ-SOLUTIONS.md"])
    answers = answer_checks(texts["ANSWER-WRITING-TOOLKIT.md"])
    wording = provenance_wording_checks(
        {name: texts[name] for name in ("README.md", "REVISION-GUIDE.md", "COVERAGE-LEDGER.md")}
    )
    for name, check in (
        ("source_provenance", source),
        ("coverage_review", coverage),
        ("doctrine", doctrine),
        ("visuals", visuals),
        ("mcqs", mcqs),
        ("answers", answers),
        ("provenance_wording", wording),
    ):
        if not check["pass"]:
            failures.append(name)

    pdfs = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        path = TOPIC / "pdf" / pdf_name
        if not path.is_file():
            pdfs[pdf_name] = {"pass": False, "missing": True, "failure_codes": ["pdf_missing"]}
        else:
            pdfs[pdf_name] = pdf_check(path, TOPIC / source_name, regeneration.get("files", {}).get(pdf_name))
    if not all(row.get("pass") for row in pdfs.values()):
        failures.append("pdfs")
    integrity = text_and_temp_checks()
    if not integrity["pass"]:
        failures.append("text_temp_diff_integrity")
    artifacts = artifact_integrity()
    if not artifacts["pass"]:
        failures.append("artifact_integrity")
    practice_blank = not re.search(r"(?im)^\s*(score|attempt|answer)\s*:\s*\S+", texts["PRACTICE-LOG.md"])
    if not practice_blank:
        failures.append("practice_log")
    negatives = (
        {"skipped": True, "pass": True, "tests": []}
        if args.skip_negative_tests
        else production_negative_tests()
    )
    if not negatives["pass"]:
        failures.append("production_negative_tests")
    release = release_integrity()
    if args.mode == "precommit" and not release["pass"]:
        failures.append("release_integrity")

    result = "FAIL" if failures else ("RELEASE_PASS" if args.mode == "precommit" else "DEVELOPMENT_PASS")
    report = {
        "schema_version": 2,
        "topic": "04 Soul, Immortality and Rebirth",
        "authority_mode": "canonical_without_formal_session",
        "formal_session_reconciliation_performed": False,
        "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "validation_mode": args.mode,
        "result": result,
        "release_ready": result == "RELEASE_PASS",
        "pdf_generation": regeneration,
        "artifact_integrity": artifacts,
        "checks": {
            "required_files": required,
            "source_provenance": source,
            "canonical_coverage": coverage,
            "doctrine": doctrine,
            "panels_and_visuals": visuals,
            "mcq_bank": mcqs,
            "pyqs_and_original_answers": answers,
            "provenance_wording": wording,
            "pdfs": pdfs,
            "text_temp_and_diff_integrity": integrity,
            "practice_log_blank": practice_blank,
            "production_negative_tests": negatives,
            "release_integrity": release,
        },
        "failures": failures,
        "mechanical_limit": (
            "Mechanical validation verifies canonical_without_formal_session provenance, authored canonical mappings, "
            "hierarchy hashes, obligations, MCQ/PYQ structure, locked word bands, copied-package negative controls and "
            "PDF integrity. It does not claim formal-session authority, philosophical truth or an examiner score."
        ),
    }
    if args.mode == "development":
        atomic_write_json(VALIDATION, report)
    pages = ", ".join(f"{name}:{row.get('pages', 0)}" for name, row in pdfs.items())
    print(
        f"{result}: canonical_rows={coverage['canonical_rows']} MCQs={len(parse_mcqs(texts['MCQ-QUESTIONS.md']))} "
        f"PYQs={len(parse_answers(texts['ANSWER-WRITING-TOOLKIT.md'], 'verified'))} "
        f"originals={len(parse_answers(texts['ANSWER-WRITING-TOOLKIT.md'], 'original'))} "
        f"PDF pages [{pages}] release_ready={report['release_ready']}"
    )
    if failures:
        print("Failures: " + ", ".join(failures))
    return 0 if result != "FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
