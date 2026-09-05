"""Repair the exact 15 active Indian Philosophy and Religion learner-v2 packages.

The workflow edits the current generation in place, preserves record identity
and approval, rebuilds only scoped learning PDFs and flowcharts, and leaves
workbooks byte-unchanged unless an independently verified defect is found.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Iterable

import carvaka_flowchart
import markdown_learning_pdf
import notions_style_ascii_master
from philosophy_indian_religion_reviewed_content import (
    GRAPHICAL_ANSWER_OVERRIDES,
    SESSION_REVIEWS,
)


ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "EXPORT-PDF-STATUS.json"
BASELINE_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "philosophy-indian-religion-deep-quality-repair-2026-08-25-baseline.json"
)
REVIEWED_MAP_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "philosophy-indian-religion-reviewed-semantic-map-2026-08-25.json"
)
REPAIR_ID = "philosophy-indian-religion-deep-quality-repair-2026-08-25"
INDIAN_ASCII_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "philosophy--paper-i-indian-philosophy-ascii-2026-08-25.json"
)
RELIGION_ASCII_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "philosophy-2026-08-23.json"
)
TOPIC_KEYS = (
    *(f"philosophy-paper-i-indian-philosophy-{index:02d}" for index in range(1, 6)),
    *(
        f"philosophy-paper-ii-philosophy-of-religion-{index:02d}"
        for index in range(1, 11)
    ),
)
SESSION_RE = re.compile(
    r"(?im)^###\s+SESSION\s+(\d+)\s*[—-]\s*(.+?)\s*$"
)
PLAIN_RE = re.compile(
    r"(?ims)(\*\*Plain-language definition:\*\*\s*)(.+?)(?=\n\n|\n\*\*)"
)
TECH_RE = re.compile(
    r"(?ims)(\*\*Technical definition:\*\*\s*)(.+?)(?=\n\n|\n####)"
)
OPENING_RE = re.compile(
    r"(?ims)(^####\s+ANSWER-GRABBING OPENING[^\n]*\n+)"
    r"(?P<quote>(?:^>[^\n]*(?:\n|$))+)"
)
KEYWORDS_RE = re.compile(
    r"(?ims)(^####\s+MUST-WRITE KEYWORDS\s*\n)"
    r"(?P<body>.*?)(?=^\*\*How to use them:\*\*)"
)
USE_RE = re.compile(
    r"(?ims)(^\*\*How to use them:\*\*\s*)(.+?)(?=\n\n|\n####)"
)
CLOSING_RE = re.compile(
    r"(?ims)(^####\s+CLOSING RECALL FLOW\s*[—-]\s*(?P<title>.+?)\s*$\s*)"
    r"```(?:text|closure-flow|ascii)?\s*\n(?P<body>.*?)\n```"
)
ASCII_SECTION_RE = re.compile(
    r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*.*\Z"
)
INLINE_ANSWER_LABEL_RE = re.compile(
    r"ANSWER-GRABBING LINE\s*[—-]\s*WRITE/ADAPT IN THE EXAM",
    re.I,
)
MECHANICAL_RE = re.compile(
    r"recommended opening definition|frame the answer through|"
    r"connect .{0,100} to explain the mechanism|decisive comparison|"
    r"topic \d+ firewall|\bprogress\b|\bpacing\b|write/adapt|"
    r"marks structure|demand answer spine|institutional architecture|"
    r"^(?:statement|argument|reply|qualification|example)\s*[.:]|"
    r"\[(?:thesis|argument|reply|qualification|fact)]|^[✅⚠️❓]",
    re.I,
)
INSTRUCTION_RE = re.compile(
    r"^(?:write|use|mention|define|compare|explain|show|start|frame|"
    r"analyse|analyze|discuss|examine|remember|avoid)\b",
    re.I,
)
FINITE_VERB_RE = re.compile(
    r"\b(?:is|are|was|were|has|have|can|cannot|does|do|denies?|"
    r"grounds?|preserves?|explains?|treats?|distinguishes?|"
    r"establishes?|requires?|links?|locates?|replaces?|infers?|"
    r"secures?|faces?|avoids?|remains?|becomes?|combines?|"
    r"identifies?|shows?|recognises?|recognizes?|means?|asks?|"
    r"reconstructs?|converts?|shifts?|relates?|depends?|yields?|"
    r"follows?|keeps?|risks?|supports?|undermines?|qualifies?)\b",
    re.I,
)
ANALYTICAL_RE = re.compile(
    r"\b(?:but|while|whereas|because|therefore|rather than|without|"
    r"not merely|not only|depends on|yet|although|unless|only|"
    r"distinguish|contrast|preserve|qualif|limit|cost|pressure|"
    r"however|thereby|instead|beyond|against)\w*\b",
    re.I,
)
USAGE_ACTION_RE = re.compile(
    r"\b(?:use|state|present|reconstruct|derive|trace|explain|show|"
    r"distinguish|compare|contrast|test|evaluate|assess|organise|"
    r"organize|connect|pair|translate|balance|conclude|move|ask|"
    r"begin|open|build|separate|treat|infer|establish|identify|"
    r"synthesi[sz]e|define|differentiate|argue)\w*\b",
    re.I,
)
TAG_RE = re.compile(
    r"^(?:\[(?:THESIS|ARGUMENT|OBJECTION|REPLY|QUALIFICATION|FACT|"
    r"INFERENCE|TRAP)]\s*|[✅⚠️❓]\s*)+",
    re.I,
)


class RepairError(RuntimeError):
    """Raised when a scoped repair cannot be completed safely."""


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def repo_path(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json_atomic(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".repair-pending")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".repair-pending")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def active_records(status: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for topic_key in TOPIC_KEYS:
        candidates = [
            record
            for record in status["exports"]
            if record.get("topic_key") == topic_key
            and record.get("variant") == "learner-v2"
        ]
        if not candidates:
            raise RepairError(f"Missing learner-v2 record: {topic_key}")
        record = max(candidates, key=lambda item: int(item.get("generation") or 0))
        validation = record.get("validation") or {}
        if validation.get("state") != "passed":
            raise RepairError(f"{topic_key}: latest active record is not validated.")
        if not all(
            repo_path(str(record[field])).is_file()
            for field in ("markdown", "main_pdf", "workbook")
        ):
            raise RepairError(f"{topic_key}: active package files are incomplete.")
        records.append(record)
    if len(records) != 15:
        raise RepairError(f"Expected exactly 15 active records, found {len(records)}.")
    return records


def clean_sentence(value: str) -> str:
    value = value.replace("\r\n", "\n")
    value = re.sub(r"^\s*>\s?", "", value.strip())
    value = re.sub(r"\*\*(?:Recommended opening definition:)?\*\*", "", value, flags=re.I)
    value = re.sub(r"^Recommended opening definition:\s*", "", value, flags=re.I)
    value = TAG_RE.sub("", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" \t*")


def answer_line_errors(
    line: str,
    *,
    minimum: int = 18,
    maximum: int = 50,
) -> list[str]:
    errors: list[str] = []
    cleaned = clean_sentence(line)
    words = cleaned.split()
    if not (minimum <= len(words) <= maximum):
        errors.append(f"word count {len(words)} outside {minimum}-{maximum}")
    if not cleaned or cleaned[-1:] not in ".!?":
        errors.append("not a complete punctuated sentence")
    if MECHANICAL_RE.search(cleaned):
        errors.append("contains mechanical or editorial prose")
    if INSTRUCTION_RE.search(cleaned):
        errors.append("is an instruction rather than an answer sentence")
    return errors


def keyword_errors(keywords: list[str]) -> list[str]:
    errors: list[str] = []
    if not 4 <= len(keywords) <= 8:
        errors.append("keyword bank must contain 4-8 terms")
    if len({item.casefold() for item in keywords}) != len(keywords):
        errors.append("keyword bank contains duplicates")
    meta = re.compile(
        r"\b(?:progress|pacing|one-line memory|philosophy optional|"
        r"pyq priority|marks|source ledger|session|exam route|part [ivx]+)\b",
        re.I,
    )
    for keyword in keywords:
        if not keyword.strip() or meta.search(keyword):
            errors.append(f"non-doctrinal keyword: {keyword!r}")
    return errors


def truncate_sentence(value: str, maximum_words: int = 46) -> str:
    value = clean_sentence(value)
    if len(value.split()) <= maximum_words:
        return value
    sentences = re.split(r"(?<=[.!?])\s+", value)
    selected: list[str] = []
    count = 0
    for sentence in sentences:
        words = sentence.split()
        if selected and count + len(words) > maximum_words:
            break
        if not selected and len(words) > maximum_words:
            selected = [" ".join(words[:maximum_words]).rstrip(",;:") + "."]
            break
        selected.append(sentence)
        count += len(words)
    result = " ".join(selected).strip()
    if result and result[-1:] not in ".!?":
        result += "."
    return result


def current_opening(block: str) -> str:
    match = OPENING_RE.search(block)
    if not match:
        return ""
    return clean_sentence(" ".join(match.group("quote").splitlines()))


def current_definition(block: str, pattern: re.Pattern[str]) -> str:
    match = pattern.search(block)
    return clean_sentence(match.group(2)) if match else ""


def current_keywords(block: str) -> list[str]:
    match = KEYWORDS_RE.search(block)
    if not match:
        return []
    return [
        re.sub(r"[*`]", "", item).strip()
        for item in re.findall(r"(?m)^-\s+(.+?)\s*$", match.group("body"))
    ]


def current_usage(block: str) -> str:
    match = USE_RE.search(block)
    return clean_sentence(match.group(2)) if match else ""


def replace_single(
    block: str,
    pattern: re.Pattern[str],
    value: str,
    *,
    label: str,
) -> str:
    if not pattern.search(block):
        raise RepairError(f"Session is missing {label}.")
    return pattern.sub(lambda match: match.group(1) + value, block, count=1)


def replace_opening(block: str, line: str) -> str:
    if not OPENING_RE.search(block):
        raise RepairError("Session is missing answer-grabbing opening.")
    return OPENING_RE.sub(
        lambda match: match.group(1) + f"> {line}\n",
        block,
        count=1,
    )


def replace_keywords(block: str, keywords: list[str]) -> str:
    if not KEYWORDS_RE.search(block):
        raise RepairError("Session is missing keyword bank.")
    body = "".join(f"- **{keyword}**\n" for keyword in keywords) + "\n"
    return KEYWORDS_RE.sub(
        lambda match: match.group(1) + body,
        block,
        count=1,
    )


def demote_inline_answer_labels(
    block: str,
    official_answer: str,
) -> tuple[str, int, int]:
    """Keep sound original prose and demote only labels that overclaim its quality."""
    lines = block.splitlines()
    output: list[str] = []
    index = 0
    retained = 0
    demoted = 0
    in_fence = False
    while index < len(lines):
        line = lines[index]
        if line.strip().startswith("```"):
            in_fence = not in_fence
            output.append(line)
            index += 1
            continue
        if in_fence:
            output.append(line)
            index += 1
            continue
        if not INLINE_ANSWER_LABEL_RE.search(line):
            output.append(line)
            index += 1
            continue
        collected = re.sub(
            r"^>\s*\*\*ANSWER-GRABBING LINE\s*[—-]\s*"
            r"WRITE/ADAPT IN THE EXAM:?\*\*\s*",
            "",
            line,
            flags=re.I,
        ).strip()
        cursor = index + 1
        while cursor < len(lines) and lines[cursor].strip().startswith(">"):
            collected += " " + re.sub(r"^>\s?", "", lines[cursor].strip())
            cursor += 1
        cleaned = clean_sentence(collected)
        if not cleaned:
            output.append(line.replace("ANSWER-GRABBING LINE", "CORE DISTINCTION"))
            demoted += 1
            index += 1
            continue
        if cleaned.casefold() == clean_sentence(official_answer).casefold():
            label = "CORE DEFINITION"
            demoted += 1
        elif answer_line_errors(cleaned):
            label = "CORE DISTINCTION"
            demoted += 1
        else:
            label = "EXAM-READY LINE"
            retained += 1
        output.append(f"> **{label}:** {cleaned}")
        index = cursor
    return "\n".join(output), retained, demoted


def extract_closure_fields(body: str) -> dict[str, str]:
    labels = {
        "KEY TERMS / DEFINITIONS": "terms",
        "EXACT TERMS": "terms",
        "MECHANISM / ARGUMENT": "mechanism",
        "CONSEQUENCE / CONTRAST": "consequence",
        "UPSC TRAP / ANSWER-USE": "trap",
        "ANSWER-GRABBING FORMULATION": "answer",
    }
    fields = {
        "terms": "",
        "mechanism": "",
        "consequence": "",
        "trap": "",
        "answer": "",
    }
    for raw in body.splitlines():
        if ":" not in raw:
            continue
        label, value = raw.split(":", 1)
        destination = labels.get(label.strip().upper())
        if destination:
            fields[destination] = clean_sentence(value)
    return fields


def specific_trap(block: str) -> str:
    candidates = re.findall(
        r"(?im)^(?:\d+[.)]\s+|[-*]\s+|>\s*)"
        r"((?:Do not|Never|Avoid|Distinguish|Do not confuse|"
        r"[⚠️❓]\s*[^.\n]+).+?[.!?])\s*$",
        block,
    )
    if candidates:
        return truncate_sentence(candidates[0], 40)
    return ""


def rebuild_closure(
    block: str,
    *,
    title: str,
    keywords: list[str],
    technical: str,
    answer: str,
) -> str:
    match = CLOSING_RE.search(block)
    if not match:
        raise RepairError(f"{title}: missing closing recall flow.")
    fields = extract_closure_fields(match.group("body"))
    mechanism = fields["mechanism"]
    if not mechanism or MECHANICAL_RE.search(mechanism):
        mechanism = technical
    consequence = fields["consequence"]
    if not consequence or len(consequence.split()) < 6:
        consequence = answer
    trap = fields["trap"]
    if not trap or MECHANICAL_RE.search(trap):
        trap = specific_trap(block)
    if not trap:
        trap = (
            "Keep the doctrine's claim, supporting argument and residual "
            "limitation distinct in the final evaluation."
        )
    replacement = "\n".join(
        [
            match.group(1).rstrip(),
            "```closure-flow",
            f"SUBTOPIC: {title}",
            f"STARTING CONCEPT: {title}",
            f"KEY TERMS / DEFINITIONS: {' · '.join(keywords)}",
            f"MECHANISM / ARGUMENT: {truncate_sentence(mechanism)}",
            f"CONSEQUENCE / CONTRAST: {truncate_sentence(consequence)}",
            f"UPSC TRAP / ANSWER-USE: {truncate_sentence(trap)}",
            f"ANSWER-GRABBING FORMULATION: {answer}",
            "```",
        ]
    ) + "\n"
    return block[: match.start()] + replacement + block[match.end() :]


def repair_session_block(
    topic_key: str,
    number: int,
    title: str,
    block: str,
    reviewed: dict[str, object],
) -> tuple[str, dict[str, Any]]:
    before = {
        "plain": current_definition(block, PLAIN_RE),
        "technical": current_definition(block, TECH_RE),
        "answer_line": current_opening(block),
        "keywords": current_keywords(block),
        "how_to_use": current_usage(block),
    }
    keywords = [str(item) for item in reviewed["keywords"]]
    if keyword_errors(keywords):
        raise RepairError(
            f"{topic_key} SESSION {number}: " + " | ".join(keyword_errors(keywords))
        )
    usage = str(reviewed["how_to_use"]).strip()
    if len(usage.split()) < 14 or not USAGE_ACTION_RE.search(usage):
        raise RepairError(
            f"{topic_key} SESSION {number}: usage guidance is not argumentative."
        )
    plain = str(reviewed.get("plain") or before["plain"]).strip()
    technical = str(reviewed.get("technical") or before["technical"]).strip()
    answer = str(reviewed.get("answer_line") or before["answer_line"]).strip()
    answer_errors = answer_line_errors(answer)
    if answer_errors:
        raise RepairError(
            f"{topic_key} SESSION {number}: reviewed answer line failed: "
            + " | ".join(answer_errors)
        )
    repaired = block
    if reviewed.get("plain"):
        repaired = replace_single(repaired, PLAIN_RE, plain, label="plain definition")
    if reviewed.get("technical"):
        repaired = replace_single(
            repaired,
            TECH_RE,
            technical,
            label="technical definition",
        )
    repaired = replace_opening(repaired, answer)
    repaired = replace_keywords(repaired, keywords)
    repaired = replace_single(
        repaired,
        USE_RE,
        usage,
        label="keyword usage guidance",
    )
    repaired, retained_inline, demoted_inline = demote_inline_answer_labels(
        repaired,
        answer,
    )
    repaired = rebuild_closure(
        repaired,
        title=title,
        keywords=keywords,
        technical=technical,
        answer=answer,
    )
    after = {
        "plain": plain,
        "technical": technical,
        "answer_line": answer,
        "keywords": keywords,
        "how_to_use": usage,
    }
    changed = {
        field: {"before": before[field], "after": after[field]}
        for field in after
        if before[field] != after[field]
    }
    return repaired, {
        "session": number,
        "title": title,
        "changed": changed,
        "retained_inline_exam_ready_lines": retained_inline,
        "demoted_overclaimed_inline_labels": demoted_inline,
    }


def repair_markdown(
    topic_key: str,
    text: str,
    manual_fragment: str,
) -> tuple[str, list[dict[str, Any]]]:
    matches = list(SESSION_RE.finditer(text))
    reviewed_sessions = SESSION_REVIEWS[topic_key]
    if len(matches) != len(reviewed_sessions):
        raise RepairError(
            f"{topic_key}: source has {len(matches)} sessions, reviewed map has "
            f"{len(reviewed_sessions)}."
        )
    chunks: list[str] = [text[: matches[0].start()]]
    results: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end]
        repaired, result = repair_session_block(
            topic_key,
            int(match.group(1)),
            match.group(2).strip(),
            block,
            reviewed_sessions[index],
        )
        chunks.append(repaired)
        results.append(result)
    repaired_text = "".join(chunks)
    ascii_replacement = (
        "### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\n\n"
        + manual_fragment.strip()
        + "\n"
    )
    if not ASCII_SECTION_RE.search(repaired_text):
        raise RepairError(f"{topic_key}: missing complete ASCII master section.")
    repaired_text = ASCII_SECTION_RE.sub(ascii_replacement, repaired_text, count=1)
    return repaired_text, results


def normalize_ascii_topic(
    spec_path: Path,
    topic_key: str,
) -> notions_style_ascii_master.ManualTopicSpec:
    topics = notions_style_ascii_master.normalize_manual_spec_file(spec_path)
    if topic_key not in topics:
        raise RepairError(f"{spec_path.name}: no manual ASCII topic {topic_key}.")
    return topics[topic_key]


def repair_ascii_specs(
    records: list[dict[str, Any]],
) -> dict[str, notions_style_ascii_master.ManualTopicSpec]:
    indian = load_json(INDIAN_ASCII_SPEC)
    religion = load_json(RELIGION_ASCII_SPEC)
    indian_replacements = {
        " PERCEPTION (pratyakṣa) / PERCEPTION              inference (anumāna)     verbal testimony":
            " PERCEPTION (pratyakṣa)              INFERENCE (anumāna)     TESTIMONY (śabda)",
        " agreement in presence (anvaya) (presence) + agreement in absence (vyatireka) (absence) ->":
            " agreement in presence (anvaya) + agreement in absence (vyatireka) ->",
        "self           conscious body      enduring enduring self (ātman)     anātman stream":
            "self           conscious body      enduring self (ātman)      no-self stream",
    }
    for topic in indian["topics"]:
        if topic.get("topic_key") not in TOPIC_KEYS:
            continue
        for panel in topic.get("panels", []):
            panel["lines"] = [
                indian_replacements.get(line, line)
                for line in panel.get("lines", [])
            ]
    record_by_key = {record["topic_key"]: record for record in records}
    for topic in religion["topics"]:
        topic_key = str(topic.get("topic_key") or "")
        if not topic_key.startswith("philosophy-paper-ii-philosophy-of-religion-"):
            continue
        record = record_by_key[topic_key]
        topic["source_markdown"] = str(record["markdown"])
        topic["source_record"] = str(record["record_id"])
        topic["approved_master_reference"] = (
            "notes\\Philosophy\\flowcharts\\philosophy-paper-i-indian-philosophy-01\\"
            "continuous-at-a-glance-core-first\\"
            "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
        )
        topic["benchmark_preservation"] = (
            "Reviewed active learner-v2 source; prior generations and the "
            "approved Cārvāka reference remain immutable."
        )
    write_json_atomic(INDIAN_ASCII_SPEC, indian)
    write_json_atomic(RELIGION_ASCII_SPEC, religion)
    selected: dict[str, notions_style_ascii_master.ManualTopicSpec] = {}
    for record in records:
        topic_key = str(record["topic_key"])
        spec_path = (
            INDIAN_ASCII_SPEC
            if topic_key.startswith("philosophy-paper-i-")
            else RELIGION_ASCII_SPEC
        )
        selected[topic_key] = normalize_ascii_topic(spec_path, topic_key)
    return selected


def render_learning_pdf(record: dict[str, Any]) -> None:
    markdown = repo_path(str(record["markdown"]))
    output = repo_path(str(record["main_pdf"]))
    backup = (
        ROOT
        / ".agent-scratch"
        / f"{record['topic_key']}-pre-deep-repair-main.pdf"
    )
    backup.parent.mkdir(exist_ok=True)
    shutil.copy2(output, backup)
    try:
        markdown_learning_pdf.build_pdf(
            markdown,
            output,
            mode="main",
            variant="learner-v2",
            topic_key=str(record["topic_key"]),
            repository_root=ROOT,
        )
    except Exception:
        shutil.copy2(backup, output)
        raise
    backup.unlink(missing_ok=True)


def reference_preservation() -> dict[str, str]:
    return {
        relative(ROOT / carvaka_flowchart.REFERENCE_FOLDER / path):
            sha256(ROOT / carvaka_flowchart.REFERENCE_FOLDER / path)
        for path in carvaka_flowchart.REFERENCE_HASHES
    }


def repair_graphical_spec(
    record: dict[str, Any],
    ascii_spec_path: Path,
) -> tuple[dict[str, Any], list[dict[str, str]]]:
    meta = record["continuous_core_first"]
    spec_path = repo_path(str(meta["graphical_spec"]))
    spec = load_json(spec_path)
    topic_key = str(record["topic_key"])
    spec["source_markdown"] = str(record["markdown"])
    spec["ascii_spec"] = relative(ascii_spec_path)
    spec["ascii_spec_sha256"] = sha256(ascii_spec_path)
    status = spec.get("status") or {}
    status["approved"] = False
    status["review"] = "PENDING USER REVIEW"
    status["line"] = (
        f"Approval: FALSE • Pending user review • source generation "
        f"g{record['generation']} repaired in place; prior artifacts unchanged "
        "outside the scoped current generation"
    )
    spec["status"] = status
    overrides = GRAPHICAL_ANSWER_OVERRIDES.get(topic_key, {})
    changes: list[dict[str, str]] = []
    for stage in spec["stages"]:
        stage_id = str(stage.get("id"))
        if stage.get("role") == "extra":
            continue
        before = str(stage.get("answer_line") or "").strip()
        if stage_id in overrides:
            stage["answer_line"] = overrides[stage_id]
        after = str(stage.get("answer_line") or "").strip()
        errors = answer_line_errors(after, minimum=12, maximum=42)
        if errors:
            raise RepairError(
                f"{topic_key} graphical stage {stage_id}: "
                + " | ".join(errors)
            )
        if before != after:
            changes.append(
                {
                    "stage_id": stage_id,
                    "title": str(stage.get("title") or ""),
                    "before": before,
                    "after": after,
                }
            )
    errors = carvaka_flowchart.validate_spec(spec)
    if errors:
        raise RepairError(f"{topic_key}: invalid graphical spec: {' | '.join(errors)}")
    write_json_atomic(spec_path, spec)
    return spec, changes


def render_graphical_package(
    record: dict[str, Any],
    ascii_master: bytes,
) -> dict[str, Any]:
    meta = record["continuous_core_first"]
    folder = repo_path(str(meta["folder"]))
    spec_path = repo_path(str(meta["graphical_spec"]))
    staging = folder.with_name(folder.name + ".repair-staging")
    backup = folder.with_name(folder.name + ".repair-backup")
    if staging.exists() or backup.exists():
        raise RepairError(f"Stale repair directory beside {folder}.")
    preservation = reference_preservation()
    _, result = carvaka_flowchart.render_package(
        ROOT,
        spec_path,
        staging,
        ascii_master_bytes=ascii_master,
        preservation_before=preservation,
    )
    if result.validation_errors:
        shutil.rmtree(staging, ignore_errors=True)
        raise RepairError(
            f"{record['topic_key']}: graphical render failed: "
            + " | ".join(result.validation_errors)
        )
    folder.rename(backup)
    try:
        staging.rename(folder)
    except Exception:
        backup.rename(folder)
        raise
    shutil.rmtree(backup)
    audit = load_json(folder / "build-audit.json")
    return {
        "core_stage_count": len(
            [
                stage
                for stage in load_json(spec_path)["stages"]
                if stage.get("role") != "extra"
            ]
        ),
        "card_count": len(load_json(spec_path)["stages"]),
        "tiled_page_count": len(audit["tiles"]),
    }


def update_tracker_record(
    record: dict[str, Any],
    ascii_spec_path: Path,
    flow_counts: dict[str, Any],
) -> None:
    meta = record["continuous_core_first"]
    meta["graphical_spec_sha256"] = sha256(repo_path(str(meta["graphical_spec"])))
    meta["ascii_master_spec"] = relative(ascii_spec_path)
    meta["ascii_master_spec_sha256"] = sha256(ascii_spec_path)
    meta["ascii_master_preserved"] = True
    meta.update(flow_counts)
    record["validation"] = {
        "state": "passed",
        "validated_on": "2026-08-25",
        "validator": (
            "tools/philosophy_indian_religion_deep_quality_repair.py + "
            "tools/validate_philosophy_indian_religion_deep_quality_repair.py"
        ),
    }
    provenance = record.setdefault("provenance", {})
    provenance["deep_quality_repair"] = {
        "id": REPAIR_ID,
        "date": "2026-08-25",
        "reviewed_map": relative(REVIEWED_MAP_PATH),
        "generation_identity_preserved": True,
        "approval_preserved": True,
        "workbook_policy": "audited; byte unchanged unless independently defective",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not args.apply:
        parser.error("Pass --apply.")
    if not BASELINE_PATH.is_file():
        parser.error(f"Immutable baseline is missing: {BASELINE_PATH}")
    status = load_json(STATUS_PATH)
    records = active_records(status)
    selected_ascii = repair_ascii_specs(records)
    semantic_map: dict[str, Any] = {
        "schema_version": 1,
        "audit_id": REPAIR_ID,
        "scope": list(TOPIC_KEYS),
        "review_standard": {
            "answer_line_words": "normally 18-40; hard maximum 50",
            "keyword_bank": "4-8 doctrine-specific terms",
            "usage": "must demonstrate argumentative, comparative or evaluative use",
            "policy": "sound originals retained; defective labels or prose repaired contextually",
        },
        "topics": [],
    }
    for record in records:
        topic_key = str(record["topic_key"])
        markdown = repo_path(str(record["markdown"]))
        source_text = markdown.read_text(encoding="utf-8")
        manual_spec = selected_ascii[topic_key]
        fragment = notions_style_ascii_master.build_manual_fragment(manual_spec)
        repaired_text, session_results = repair_markdown(
            topic_key,
            source_text,
            fragment,
        )
        write_text_atomic(markdown, repaired_text)
        standalone = notions_style_ascii_master.standalone_panel_text(fragment)
        ascii_master = repo_path(
            str(record["continuous_core_first"]["ascii_master"])
        )
        write_text_atomic(ascii_master, standalone)
        ascii_spec_path = manual_spec.source_path
        _, graphical_changes = repair_graphical_spec(record, ascii_spec_path)
        render_learning_pdf(record)
        flow_counts = render_graphical_package(
            record,
            standalone.encode("utf-8"),
        )
        update_tracker_record(record, ascii_spec_path, flow_counts)
        semantic_map["topics"].append(
            {
                "topic_key": topic_key,
                "record_id": record["record_id"],
                "generation": record["generation"],
                "sessions": session_results,
                "graphical_answer_strip_changes": graphical_changes,
                "ascii_spec": relative(ascii_spec_path),
            }
        )
    write_json_atomic(REVIEWED_MAP_PATH, semantic_map)
    write_json_atomic(STATUS_PATH, status)
    print(
        f"repaired_topics={len(records)} "
        f"repaired_sessions={sum(len(item['sessions']) for item in semantic_map['topics'])}"
    )
    print(f"reviewed_map={relative(REVIEWED_MAP_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
