"""Repair and validate active Polity answer lines and bounded visual text.

This is an in-generation correction workflow: it edits the active record in
place, preserves its generation identity and approval state, and never touches
workbook content.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import textwrap
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import polity_flowchart_case_years


ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "EXPORT-PDF-STATUS.json"
MASTER_TRACKER_PATH = ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
BASELINE_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "polity-answer-line-visual-boundary-repair-2026-08-25-baseline.json"
)
OVERRIDES_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "polity-answer-line-visual-boundary-overrides-2026-08-25.json"
)
REVIEWED_MAP_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "polity-answer-line-reviewed-map-2026-08-25.json"
)
GRAPHICAL_SPEC_ROOT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / "Polity"
)
REPAIR_ID = "polity-answer-line-visual-boundary-repair-2026-08-25"
MAX_ANSWER_WORDS = 48
MIN_ANSWER_WORDS = 12
MAX_TEXT_FENCE_WIDTH = 96

SESSION_RE = re.compile(
    r"(?im)^###\s+SESSION\s+(\d+)\s*[—-]\s*(.+?)\s*$"
)
FORMULATION_RE = re.compile(
    r"(?m)^(ANSWER-GRABBING FORMULATION:\s*)(.+?)\s*$"
)
INLINE_ANSWER_RE = re.compile(
    r"(?m)^(>\s*\*\*ANSWER-GRABBING LINE\s*[—-]\s*"
    r"WRITE/ADAPT IN THE EXAM(?:\s*\([^)]*\))?\s*:?\*\*\s*)(.+?)\s*$",
    re.I,
)
OPENING_BLOCK_RE = re.compile(
    r"(?im)(^####\s+ANSWER-GRABBING OPENING\s*[—-]\s*"
    r"WRITE/ADAPT IN THE EXAM\s*$\n+)(?P<quote>(?:^>[^\n]*(?:\n|$))+)"
)
CLOSING_FLOW_RE = re.compile(
    r"(?ims)(^####\s+CLOSING RECALL FLOW\s*[—-]\s*(?P<title>.+?)\s*$\s*)"
    r"```text\s*\n(?P<body>.*?)\n```"
)
LEGACY_CLOSING_START_RE = re.compile(
    r"(?im)^####\s+CLOSING RECALL FLOW\s*[—-].*$\n+\s*```text\s*$"
)
TEXT_FENCE_RE = re.compile(r"(?ms)^```text\s*\n(?P<body>.*?)\n```")

MECHANICAL_RE = re.compile(
    r"denotes the constitutional rules|operates through|organised around|"
    r"its principal consequence|the exam-safe limitation|"
    r"the operative mechanism matters|the decisive contrast is|"
    r"method central question|problem in question|marks structure|"
    r"demand answer spine|(?:^|\s)trap:|,,|"
    r"\b(?:describe|attribute|read|treat|call|use|mention)\s+"
    r"(?:it|this|them|the)\b",
    re.I,
)
REJECTED_TEMPLATE_RE = re.compile(
    r"supports democratic constitutionalism|"
    r"institutionally,\s+this supports|"
    r"institutional inheritance acquires legitimacy|"
    r"formal independence produces accountability only when|"
    r"political centralisation cannot erase|"
    r"practical authority remains subject to constitutional text|"
    r"\bdenotes the constitutional rules\b|"
    r"\borganis(?:e|es) .{0,90} to advance\b|"
    r"\bstructures .{0,90} within\b",
    re.I,
)
INSTRUCTION_RE = re.compile(
    r"^(?:mention|use|write|remember|avoid|do not|start|explain|discuss|"
    r"examine|analyse|analyze|show|trace|claim|frame|define|compare|"
    r"distinguish|read|describe|recite|make)\b",
    re.I,
)
PROHIBITED_START_RE = re.compile(
    r"^(?:cross-link|exam use|mention|use|write|remember|avoid|"
    r"definition|caption|owner link|mains route|prelims route|"
    r"examiner line|qualified verdict|core proposition|"
    r"elimination note|why this earns marks|verdict|tested concept|"
    r"assessment|master distinction|current evidence|what it proves|"
    r"institutional analysis|status caution|counter|analytical verdict|"
    r"conclusion|qualification|probable|memory line|prelims trap|caveat|"
    r"mains thesis|(?:fact|analysis|trap|evidence|claim)\s*:|"
    r"it|its|this|these|those|they|that)\b",
    re.I,
)
FINITE_VERB_RE = re.compile(
    r"\b(?:is|are|was|were|has|have|had|can|cannot|could|should|"
    r"must|may|does|do|did|protects?|preserves?|limits?|limited|"
    r"requires?|required|creates?|created|converts?|converted|"
    r"ensures?|ensured|balances?|balanced|allows?|allowed|"
    r"constrains?|constrained|links?|linked|anchors?|anchored|"
    r"recognis(?:es|ed)|allocates?|allocated|subjects?|subjected|"
    r"strengthens?|strengthened|weakens?|weakened|translates?|"
    r"translated|disciplines?|disciplined|prevents?|prevented|"
    r"makes?|made|remains?|remained|depends?|depended|rests?|"
    r"turns?|turned|governs?|governed|authoris(?:es|ed)|binds?|"
    r"bound|enables?|enabled|establishes?|established|reflects?|"
    r"reflected|reconciles?|reconciled|secures?|secured|risks?|"
    r"risked|channels?|channelled|ends?|ended|introduced|retained|"
    r"replaced|widened|holds?|held|provides?|provided|"
    r"distinguishes?|distinguished|addresses?|addressed|"
    r"enshrines?|enshrined|vests?|vested|gives?|gave|marks?|"
    r"marked|combines?|combined|moves?|moved|separates?|separated|"
    r"arises?|arose|applies?|applied|keeps?|kept|alters?|altered|"
    r"covers?|covered|"
    r"commences?|commenced|proposes?|proposed|distributes?|distributed|"
    r"abolishes?|abolished|introduces?|introduced|prevents?|"
    r"permits?|permitted|invalidates?|invalidated|operates?)\b",
    re.I,
)
ANALYTICAL_RE = re.compile(
    r"\b(?:but|while|whereas|however|thereby|so that|subject to|"
    r"depends on|without|rather than|only|yet|although|unless|within|"
    r"therefore|because|accountability|legitimacy|federal|democratic|"
    r"institutional|constitutional(?:ly)?|legal(?:ly)?|consequence|limits?|protects?|"
    r"preserves?|balances?|constrains?|transforms?|translates?|"
    r"enables?|ensures?|risks?|prevents?|requires?|links?|conversion|"
    r"converts?|combines?|making|even as|nevertheless|not automatically|"
    r"depends less|does not)\b",
    re.I,
)
BALANCE_RE = re.compile(
    r"\b(?:but|while|whereas|however|thereby|so that|subject to|"
    r"depends on|without|rather than|only|yet|although|unless|within|"
    r"therefore|because|cannot|does not|do not|not merely|not simply|"
    r"conversion|converts?|links?|combines?|making|even as|"
    r"nevertheless|not automatically|depends less)\b",
    re.I,
)
STRONG_ANALYTICAL_RE = re.compile(
    r"\b(?:but|while|whereas|however|thereby|so that|depends on|"
    r"rather than|yet|although|because|not merely|not simply|"
    r"does not|cannot|only when)\b",
    re.I,
)
CONSEQUENCE_RE = re.compile(
    r"\b(?:accountability|legitimacy|autonomy|review|power|authority|"
    r"representation|remedy|rights?|federalism|federal|democratic|"
    r"institutional|governance|stability|independence|competence|"
    r"devolution|responsibility|control|protection|participation|"
    r"transparency|equality|liberty|justice|coherence|uniformity|access|"
    r"administration|settlement|deliberation|scrutiny|consent|"
    r"pluralism|integration|sovereignty|enforcement|adjudication)\b",
    re.I,
)
ANALYTICAL_SIGNAL_RE = re.compile(
    r"\b(?:but|while|whereas|however|thereby|therefore|because|"
    r"rather than|without|subject to|yet|although|unless|only when|"
    r"depends? on|not|never|unlike|even as|so that|instead of|"
    r"constrain(?:s|ed|ing)?|convert(?:s|ed|ing)?|"
    r"transform(?:s|ed|ing)?|protect(?:s|ed|ing)?|"
    r"limit(?:s|ed|ing)?|enable(?:s|d|ing)?|ensure(?:s|d|ing)?|"
    r"risk(?:s|ed|ing)?|balanc(?:e|es|ed|ing)|"
    r"link(?:s|ed|ing)?|reconcil(?:e|es|ed|ing)|"
    r"reveal(?:s|ed|ing)?|show(?:s|ed|ing)?|allow(?:s|ed|ing)?|"
    r"centralis(?:e|es|ed|ing|ation)|decentralis(?:e|es|ed|ing|ation)|"
    r"differentiat(?:e|es|ed|ing)|subject(?:s|ed|ing)?|"
    r"replac(?:e|es|ed|ing)|widen(?:s|ed|ing)?|narrow(?:s|ed|ing)?|"
    r"entrench(?:es|ed|ing)?|shift(?:s|ed|ing)?|expos(?:e|es|ed|ing)|"
    r"condition(?:s|ed|ing)?|insulat(?:e|es|ed|ing)|"
    r"subordinat(?:e|es|ed|ing)|institutionalis(?:e|es|ed|ing)|"
    r"redistribut(?:e|es|ed|ing)|separat(?:e|es|ed|ing)|"
    r"strengthen(?:s|ed|ing)?|weaken(?:s|ed|ing)?|"
    r"authoris(?:e|es|ed|ing)|prohibit(?:s|ed|ing)?|"
    r"channel(?:s|led|ling)?|mediat(?:e|es|ed|ing)|"
    r"legitimis(?:e|es|ed|ing)|qualif(?:y|ies|ied|ying)|"
    r"displac(?:e|es|ed|ing)|correct(?:s|ed|ing)?|"
    r"integrat(?:e|es|ed|ing)|accommodat(?:e|es|ed|ing)|"
    r"concentrat(?:e|es|ed|ing)|transfer(?:s|red|ring)?|"
    r"abolish(?:es|ed|ing)?|introduc(?:e|es|ed|ing)|"
    r"retain(?:s|ed|ing)?|anchor(?:s|ed|ing)?|"
    r"secur(?:e|es|ed|ing)|prevent(?:s|ed|ing)?|"
    r"govern(?:s|ed|ing)?|extend(?:s|ed|ing)?|"
    r"distinguish(?:es|ed|ing)?|combin(?:e|es|ed|ing)|"
    r"expand(?:s|ed|ing)?|distribut(?:e|es|ed|ing)|"
    r"preserv(?:e|es|ed|ing)?|remain(?:s|ed|ing)?|"
    r"require(?:s|d|ing)?|affect(?:s|ed|ing)?|"
    r"determin(?:e|es|ed|ing)|undermin(?:e|es|ed|ing)|"
    r"improv(?:e|es|ed|ing)|reduc(?:e|es|ed|ing)|"
    r"promot(?:e|es|ed|ing)|support(?:s|ed|ing)|"
    r"advance(?:s|d|ing)|restrict(?:s|ed|ing)|"
    r"exclude(?:s|d|ing)|include(?:s|d|ing)|"
    r"clarif(?:y|ies|ied|ying)|sustain(?:s|ed|ing)|"
    r"test(?:s|ed|ing)?|symbolis(?:e|es|ed|ing)|"
    r"translat(?:e|es|ed|ing)|mak(?:e|es|ing)|"
    r"operat(?:e|es|ed|ing)|aris(?:e|es|en|ing)|"
    r"differ(?:s|ed|ing)?|vary|varies|varied|"
    r"only|except|within|through|across|"
    r"can|cannot|may|must|means?|matters?|different|distinct|"
    r"connect(?:s|ed|ing)?|"
    r"more .{0,40} than|less .{0,40} than|so)\b",
    re.I,
)
RISKY_ABSOLUTE_RE = re.compile(
    r"\b(?:always|never|completely|entirely|automatically|absolute|"
    r"unlimited|without exception|in all cases)\b",
    re.I,
)
QUALIFIER_RE = re.compile(
    r"\b(?:generally|ordinarily|subject to|except|unless|not absolute|"
    r"not an absolute|not automatically|limited|but|while|whereas|"
    r"however|although|yet|rather than|without|only|within|cannot|"
    r"does not|do not|replaced|rebuttable|overbroad|qualified)\b",
    re.I,
)
LEGAL_TERM_RE = re.compile(
    r"\b(?:Article|Articles|Part|Schedule|Act|Amendment|Court|Parliament|"
    r"Constitution|constitutional|statutory|federal|democratic|judicial|"
    r"executive|legislative|right|rights|duty|duties|commission|tribunal|"
    r"election|governance|jurisdiction|review|federalism|accountability|"
    r"representation|sovereignty|autonomy|remedy|competence)\b",
    re.I,
)
SOURCE_LABEL_RE = re.compile(
    r"^(?:\[(?:FACT|ANALYSIS|LIMIT|CURRENT|INFERENCE|TRAP)\]\s*|"
    r"(?:FACT|ANALYSIS|LIMIT|TRAP|Mains route|Examiner opening|"
    r"Core argument|Core thesis|Criticism|Transition|Final verdict|"
    r"Continuity line|Qualification|Answer line|Rule|Anchor|Purpose|"
    r"Mechanism|Evidence|Claim|Thesis|Balanced conclusion)\s*:\s*)+",
    re.I,
)
GENERIC_TITLE_WORDS = {
    "answer",
    "application",
    "architecture",
    "basic",
    "complete",
    "concept",
    "constitutional",
    "core",
    "demand",
    "evidence",
    "facts",
    "framework",
    "introduction",
    "map",
    "master",
    "overview",
    "practice",
    "rapid",
    "recall",
    "revision",
    "session",
    "structure",
    "system",
    "topic",
    "article",
    "analytical",
    "common",
    "core",
    "forms",
    "idea",
    "ix-a",
    "principles",
    "routes",
    "sheet",
    "snapshot",
    "status",
    "tensions",
    "types",
    "why",
}


@dataclass
class Session:
    number: int
    title: str
    start: int
    end: int
    body: str
    before: str
    after: str = ""
    method: str = ""
    issues_before: tuple[str, ...] = ()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def status_records() -> list[dict[str, Any]]:
    status = load_json(STATUS_PATH)
    records = status.get("records") or status.get("exports")
    if not isinstance(records, list):
        raise ValueError("EXPORT-PDF-STATUS.json has no records/exports array.")
    return records


def active_polity_records() -> list[dict[str, Any]]:
    tracker = load_json(MASTER_TRACKER_PATH)
    ids = {
        item["topic_key"]: item["source_record_id"]
        for item in tracker.get("topics", [])
        if item.get("subject") == "Polity"
    }
    records = {record.get("record_id"): record for record in status_records()}
    selected = []
    for number in range(1, 56):
        topic_key = f"polity-{number:02d}"
        record_id = ids.get(topic_key)
        if not record_id or record_id not in records:
            raise ValueError(f"Cannot resolve latest active record for {topic_key}.")
        record = records[record_id]
        if record.get("approved") is not False:
            raise ValueError(f"{record_id}: approved state is not false.")
        selected.append(record)
    return selected


def clean_markdown(value: str) -> str:
    value = re.sub(r"!\[[^\]]*]\([^)]+\)", " ", value)
    value = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", value)
    value = re.sub(r"\[(?:FACT|ANALYSIS|LIMIT|CURRENT|INFERENCE|TRAP)\]", "", value)
    value = value.replace("⚖️", "").replace("📜", "")
    value = re.sub(r"[*_`>#]", "", value)
    value = re.sub(
        r"^ANSWER-GRABBING LINE\s*[—-]\s*WRITE/ADAPT IN THE EXAM"
        r"(?:\s*\([^)]*\))?\s*:?\s*",
        "",
        value,
        flags=re.I,
    )
    value = SOURCE_LABEL_RE.sub("", value.strip())
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -:")


def words(value: str) -> list[str]:
    return re.findall(r"\b[\w'’.-]+\b", value)


def answer_line_issues(value: str) -> list[str]:
    line = re.sub(r"\s+", " ", value).strip()
    count = len(words(line))
    issues: list[str] = []
    if count < MIN_ANSWER_WORDS:
        issues.append("fragment-or-too-short")
    if count > MAX_ANSWER_WORDS:
        issues.append("overlong")
    if line and line[0].islower():
        issues.append("lower-case-start")
    if not line.endswith((".", "!", "?")):
        issues.append("missing-terminal-punctuation")
    if re.search(
        r"(?<!\bv)(?<!\bV)(?<!\bS\.R)(?<!\b[A-Z])"
        r"[.!?]\s+(?=(?:The|This|It|However|Yet|Therefore|Thus|A|An)\b)",
        line,
    ):
        issues.append("multiple-sentences")
    if re.search(r"\.\s+[a-z]", line):
        issues.append("multiple-sentences")
    if re.search(
        r"\b(?:the|and|or|of|to|for|with|from|by|as|at|under|"
        r"requires?|includes?|including|such as|into|relates to)\s*[.!?]$",
        line,
        re.I,
    ):
        issues.append("incomplete-ending")
    if not ANALYTICAL_SIGNAL_RE.search(line):
        issues.append("no-analytical-connection")
    if MECHANICAL_RE.search(line) or REJECTED_TEMPLATE_RE.search(line):
        issues.append("mechanical-or-instructional")
    if INSTRUCTION_RE.search(line) or PROHIBITED_START_RE.search(line):
        issues.append("instruction")
    if re.match(r"^(?:[-*+]|\d+[.)])\s+", line):
        issues.append("list-syntax")
    if line.count(":") >= 2:
        issues.append("colon-heavy")
    if len(re.findall(r"\b(?:17|18|19|20)\d{2}\b", line)) >= 3:
        issues.append("date-list")
    if re.search(
        r"\b(?:correct:|wrong:|owner link:|visual \d+|"
        r"book context:|current control:|source \d+:)\b",
        line,
        re.I,
    ):
        issues.append("heading-or-metadata")
    if re.search(
        r"\b(?:do not (?:cite|write|state|assume|attribute|"
        r"memorise|reproduce)|should (?:write|cite|state|mention|begin|"
        r"conclude|identify)|re-verify|mark it|route detailed|"
        r"name the operating|state the criteria)\b",
        line,
        re.I,
    ):
        issues.append("instruction")
    if re.match(
        r'^"?(?:explain|discuss|examine|analyse|analyze|evaluate|comment)\b',
        line,
        re.I,
    ):
        issues.append("question-or-heading")
    if re.search(r"[🧾📜⚖️📰]", line):
        issues.append("metadata-glyph")
    if "�" in line:
        issues.append("replacement-character")
    if (
        RISKY_ABSOLUTE_RE.search(line)
        and not QUALIFIER_RE.search(line)
    ):
        issues.append("legally-risky-absolute")
    if re.search(
        r"\b(?:metadata|caption|keyword|book context|"
        r"this package|local repository)\b",
        line,
        re.I,
    ):
        issues.append("metadata")
    if re.search(r"\bANSWER-GRABBING LINE\b", line, re.I):
        issues.append("metadata")
    return issues


def authored_answer_issues(value: str) -> list[str]:
    return answer_line_issues(value)


def phrase_tokens(value: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9]+(?:['’.-][A-Za-z0-9]+)*", value.casefold())


def duplicate_phrase_audit(
    lines: list[tuple[str, int, str, str]],
) -> dict[str, list[dict[str, Any]]]:
    repeated_prefixes: dict[str, list[str]] = {}
    repeated_suffixes: dict[str, list[str]] = {}
    repeated_eight_grams: dict[str, set[str]] = {}

    for topic_key, number, _, line in lines:
        tokens = phrase_tokens(line)
        location = f"{topic_key}/session-{number}"
        if len(tokens) >= 6:
            repeated_prefixes.setdefault(" ".join(tokens[:6]), []).append(location)
            repeated_suffixes.setdefault(" ".join(tokens[-6:]), []).append(location)
        for index in range(max(0, len(tokens) - 7)):
            phrase = " ".join(tokens[index:index + 8])
            repeated_eight_grams.setdefault(phrase, set()).add(topic_key)

    return {
        "repeated_six_word_prefixes": [
            {"phrase": phrase, "locations": locations}
            for phrase, locations in sorted(repeated_prefixes.items())
            if len(locations) > 3
        ],
        "repeated_six_word_suffixes": [
            {"phrase": phrase, "locations": locations}
            for phrase, locations in sorted(repeated_suffixes.items())
            if len(locations) > 3
        ],
        "repeated_eight_word_cross_topic_phrases": [
            {"phrase": phrase, "topics": sorted(topics)}
            for phrase, topics in sorted(repeated_eight_grams.items())
            if len(topics) > 3
        ],
    }


def title_terms(title: str) -> set[str]:
    output: set[str] = set()
    for token in re.findall(r"[A-Za-z][A-Za-z'’-]+", title):
        normalized = token.casefold()
        if len(normalized) <= 3 or normalized in GENERIC_TITLE_WORDS:
            continue
        if normalized.endswith("ies") and len(normalized) > 5:
            normalized = normalized[:-3] + "y"
        elif normalized.endswith("s") and not normalized.endswith("ss") and len(normalized) > 5:
            normalized = normalized[:-1]
        output.add(normalized)
    return output


def session_title_is_generic(title: str) -> bool:
    return len(title_terms(title)) <= 1


def _remove_generated_aids(block: str) -> str:
    text = re.sub(
        r"(?ims)^####\s+DEFINITION / WHAT THIS IS CALLED\s*$.*?"
        r"^\*\*How to use them:\*\*[^\n]*\n?",
        "\n",
        block,
    )
    text = re.sub(
        r"(?ims)^####\s+CLOSING RECALL FLOW.*?^```\s*$",
        "\n",
        text,
    )
    text = INLINE_ANSWER_RE.sub("\n", text)
    text = re.sub(r"(?ms)^```.*?```", "\n", text)
    text = re.sub(r"(?m)^!\[[^\n]+$", "\n", text)
    text = re.sub(r"(?im)^\*Caption:.*$", "\n", text)
    text = re.sub(r"(?m)^#{1,6}\s+.*$", "\n", text)
    text = re.sub(r"(?m)^\|.*$", "\n", text)
    text = re.sub(
        r"(?im)^(?:EXACT TERMS|MECHANISM / ARGUMENT|"
        r"CONSEQUENCE / CONTRAST|UPSC TRAP / ANSWER-USE|"
        r"ANSWER-GRABBING FORMULATION):.*$",
        "\n",
        text,
    )
    text = re.sub(
        r"(?im)^.*(?:denotes the constitutional rules and institutional links|"
        r"operates through).*$",
        "\n",
        text,
    )
    text = re.sub(
        r"(?im)^(?:The operative mechanism matters because|"
        r"Its principal consequence is that|The decisive contrast is between|"
        r"The exam-safe limitation is that).*$",
        "\n",
        text,
    )
    return text


def _paragraphs(block: str) -> list[str]:
    cleaned = _remove_generated_aids(block)
    output: list[str] = []
    pending: list[str] = []
    for raw in cleaned.replace("\r\n", "\n").splitlines():
        stripped = raw.strip()
        if not stripped:
            if pending:
                output.append(" ".join(pending))
                pending = []
            continue
        stripped = re.sub(r"^\s*(?:[-+*]|\d+[.)])\s+", "", stripped)
        stripped = clean_markdown(stripped)
        if not stripped:
            continue
        if pending and re.match(r"^(?:Correct|Wrong|Answer|Explanation):", stripped, re.I):
            output.append(" ".join(pending))
            pending = []
        pending.append(stripped)
    if pending:
        output.append(" ".join(pending))
    return output


def _candidate_sentences(block: str) -> list[str]:
    candidates: list[str] = []
    for paragraph in _paragraphs(block):
        for raw in re.split(
            r"(?<=[.!?])\s+(?=(?:[\"'“‘(]?[A-Z0-9]))",
            paragraph,
        ):
            sentence = clean_markdown(raw)
            if not sentence:
                continue
            if not sentence.endswith((".", "!", "?")):
                sentence += "."
            if (
                MECHANICAL_RE.search(sentence)
                or INSTRUCTION_RE.search(sentence)
                or re.match(r"^(?:Wrong|Correct|Answer|Explanation):", sentence, re.I)
            ):
                continue
            candidates.append(sentence)
    return candidates


def _candidate_score(sentence: str, title: str) -> int:
    count = len(words(sentence))
    if count < 9 or count > 56 or not FINITE_VERB_RE.search(sentence):
        return -1000
    score = max(0, 12 - abs(count - 27) // 2)
    overlap = title_terms(title) & title_terms(sentence)
    score += min(12, len(overlap) * 4)
    if ANALYTICAL_RE.search(sentence):
        score += 10
    if re.search(
        r"\b(?:but|while|rather than|without|subject to|only|however|"
        r"thereby|yet|although|unless|does not|cannot)\b",
        sentence,
        re.I,
    ):
        score += 8
    if LEGAL_TERM_RE.search(sentence):
        score += 5
    if re.search(r"\b(?:current|2026|reported|announced|portal)\b", sentence, re.I):
        score -= 8
    if ":" in sentence and count < 16:
        score -= 5
    return score


def _explicit_answer_candidates(block: str, session_title: str) -> list[str]:
    output: list[str] = []
    relevance = relevance_terms(session_title, block)
    for match in INLINE_ANSWER_RE.finditer(block):
        value = clean_markdown(match.group(2))
        if (
            value
            and not authored_answer_issues(value)
            and (
                session_title_is_generic(session_title)
                or not relevance
                or relevance & title_terms(value)
            )
        ):
            output.append(value)
    return output


def _topic_qualification(topic_title: str, session_title: str) -> str:
    text = f"{topic_title} {session_title}".casefold()
    if re.fullmatch(
        r"(?:historical background|making of the constitution|salient features|"
        r"preamble|concept of the constitution)",
        topic_title.casefold(),
    ):
        return (
            "its institutional inheritance acquires legitimacy only through "
            "popular sovereignty, constitutional limits and democratic accountability"
        )
    if re.search(r"municip|\bpanchayat\b|\blocal government\b|\bward\b|district planning", text):
        return (
            "effective self-government still depends on State-law devolution "
            "of functions, staff and finance"
        )
    if re.search(r"centre-state|union-state|\bfederal|inter-state|finance commission|\bgst\b", text):
        return (
            "its operation must balance Union coordination with the "
            "constitutionally protected sphere of the States"
        )
    if re.search(r"commission|cag|upsc|nhrc|cic|lokpal|ombudsman|cbi|niti", text):
        return (
            "formal independence produces accountability only when tenure, "
            "resources, jurisdiction and follow-up are institutionally secured"
        )
    if re.search(r"language|\btribal\b|asymmetry|special provision|fifth schedule|sixth schedule", text):
        return (
            "constitutional accommodation must protect pluralism without "
            "dissolving equality, accountability or national integration"
        )
    if re.search(r"right|equality|liberty|citizenship|minority|scheduled|reservation", text):
        return (
            "its protection remains subject to the Constitution's express "
            "scope, reasonable qualifications and judicial review"
        )
    if re.search(r"court|judge|judicial|doctrine|precedent|tribunal|review", text):
        return (
            "judicial application must remain anchored in constitutional text, "
            "binding precedent and institutional competence"
        )
    if re.search(r"parliament|legislature|president|governor|minister|executive", text):
        return (
            "political centralisation cannot erase the Constitution's distinct "
            "lines of ministerial responsibility and legislative control"
        )
    if re.search(r"election|party|defection|representation|delimitation", text):
        return (
            "representative legitimacy depends on impartial administration, "
            "transparent procedure and legally reviewable decisions"
        )
    if re.search(r"emergency|security|armed force", text):
        return (
            "exceptional public power remains subject to temporal, "
            "parliamentary and judicial checks"
        )
    return (
        "its practical authority remains subject to constitutional text, "
        "institutional competence and reviewable procedure"
    )


def _topic_impact(topic_title: str, session_title: str) -> str:
    text = f"{topic_title} {session_title}".casefold()
    if re.fullmatch(
        r"(?:historical background|making of the constitution|salient features|"
        r"preamble|concept of the constitution)",
        topic_title.casefold(),
    ):
        return "democratic constitutionalism"
    if re.search(r"municip|\bpanchayat\b|\blocal government\b|\bward\b|district planning", text):
        return "a constitutional foundation for representative local government"
    if re.search(r"centre-state|union-state|\bfederal|inter-state|finance commission|\bgst\b", text):
        return "a constitutionally ordered allocation of Union-State authority"
    if re.search(r"commission|cag|upsc|nhrc|cic|lokpal|ombudsman|cbi|niti", text):
        return "credible public accountability"
    if re.search(r"language|\btribal\b|asymmetry|special provision|fifth schedule|sixth schedule", text):
        return "plural accommodation within a common constitutional order"
    if re.search(r"right|equality|liberty|citizenship|minority|scheduled|reservation", text):
        return "meaningful restraints on public power"
    if re.search(r"court|judge|judicial|doctrine|precedent|tribunal|review", text):
        return "structured adjudication and constitutional control of public power"
    if re.search(r"parliament|legislature|president|governor|minister|executive", text):
        return "responsible government and legislative scrutiny"
    if re.search(r"election|party|defection|representation|delimitation", text):
        return "representative legitimacy and electoral accountability"
    if re.search(r"emergency|security|armed force", text):
        return "exceptional state capacity under constitutional control"
    return "accountable governance"


def _named_anchors(block: str) -> list[str]:
    source = _remove_generated_aids(block)
    patterns = (
        r"\bArticles?\s+\d+[A-Z]?(?:\(\d+\))*"
        r"(?:\s*(?:,|and|to|–|-)\s*\d+[A-Z]?(?:\(\d+\))*)*",
        r"\b\d+(?:st|nd|rd|th)\s+Amendment\b",
        r"\b(?:Part|Schedule)\s+[IVXLC0-9-]+\b",
        r"\b[A-Z][A-Za-z.'’ -]{2,45}\s+Act(?:,\s*\d{4}|\s+\d{4})\b",
    )
    anchors: list[str] = []
    for pattern in patterns:
        for match in re.finditer(pattern, source):
            value = re.sub(r"\s+", " ", match.group(0)).strip()
            if value.casefold() not in {item.casefold() for item in anchors}:
                anchors.append(value)
            if len(anchors) == 3:
                return anchors
    return anchors


def _focus_phrases(block: str) -> list[str]:
    source = re.sub(
        r"(?ims)^####\s+CLOSING RECALL FLOW.*?^```\s*$",
        "\n",
        block,
    )
    source = re.sub(r"(?ms)^```.*?```", "\n", source)
    source = re.sub(r"(?m)^!\[[^\n]+$", "\n", source)
    candidates: list[str] = []
    candidates.extend(_named_anchors(block))
    candidates.extend(re.findall(r"\*\*([^*\n]{3,80})\*\*", source))
    for raw in source.splitlines():
        if not raw.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
        if cells:
            candidates.append(cells[0])
    output: list[str] = []
    banned = re.compile(
        r"^(?:fact|analysis|limit|trap|answer|explanation|question|"
        r"correct|wrong|session|classification|mains route|prelims route|"
        r"mark|marks|structure|dimension|test|feature|provision|article|"
        r"memory line|high-value trap|visual|how to use them|"
        r"plain-language definition|technical definition|"
        r"answer-grabbing opening|must-write keywords|"
        r"its principal consequence|operative mechanism|"
        r"decisive contrast|exam-safe limitation)$",
        re.I,
    )
    for candidate in candidates:
        value = clean_markdown(candidate)
        value = re.sub(r"^[A-Z /-]+:\s*", "", value)
        if (
            not value
            or banned.fullmatch(value)
            or MECHANICAL_RE.search(value)
            or INSTRUCTION_RE.search(value)
            or re.match(
                r"^(?:the\s+)?(?:decisive contrast|operative mechanism|"
                r"principal consequence|exam-safe limitation)\b",
                value,
                re.I,
            )
            or value.casefold() in {"its", "it", "this", "these", "those"}
            or re.search(
                r"\b(?:exam|answer|memory|trap|visual|UPSC|GS-I{1,3})\b",
                value,
                re.I,
            )
            or len(words(value)) > 7
            or re.search(r"[.!?]$", value)
            or re.match(r"^(?:visual|figure|table|caption)\b", value, re.I)
            or any(
                value.casefold() in item.casefold()
                or item.casefold() in value.casefold()
                for item in output
            )
        ):
            continue
        output.append(value)
        if len(output) == 3:
            break
    return output


def _joined_phrases(values: list[str]) -> str:
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return f"{values[0]} and {values[1]}"
    return f"{values[0]}, {values[1]} and {values[2]}"


def _sentence_phrase(value: str) -> str:
    phrase = value.lower()
    replacements = {
        "gs-ii": "GS-II",
        "upsc": "UPSC",
        "ncrwc": "NCRWC",
        "nhrc": "NHRC",
        "cbi": "CBI",
        "cag": "CAG",
        "eci": "ECI",
        "gst": "GST",
        "usa": "USA",
        "uk": "UK",
        "ipu": "IPU",
        "cpa": "CPA",
        "india": "India",
        "act": "Act",
        "article": "Article",
        "part": "Part",
        "schedule": "Schedule",
        "amendment": "Amendment",
    }
    for source, replacement in replacements.items():
        phrase = re.sub(rf"\b{re.escape(source)}\b", replacement, phrase)
    return _capitalized(phrase)


def _best_limitation(block: str, relevance: set[str]) -> str:
    candidates = []
    for candidate in _candidate_sentences(block):
        if not re.search(
            r"\b(?:but|while|however|cannot|does not|do not|only|"
            r"depends on|subject to|remains|without|requires?|"
            r"safeguards?)\b",
            candidate,
            re.I,
        ):
            continue
        if re.search(
            r"\b(?:UPSC|exam|question|option|stem|PYQ|answer)\b",
            candidate,
            re.I,
        ):
            continue
        if len(words(candidate)) > 34:
            continue
        score = _candidate_score(candidate, "")
        if relevance & title_terms(candidate):
            score += 8
        candidates.append((score, candidate))
    if not candidates:
        return ""
    candidates.sort(key=lambda item: (item[0], -len(item[1])), reverse=True)
    return candidates[0][1].strip().rstrip(".")


def relevance_terms(session_title: str, block: str) -> set[str]:
    values = [
        session_title,
        *_named_anchors(block),
        *_focus_phrases(block),
    ]
    terms: set[str] = set()
    for value in values:
        terms.update(title_terms(value))
    return terms


def _compress(sentence: str, maximum: int = 30) -> str:
    sentence = re.sub(r"\s+", " ", sentence).strip()
    tokens = words(sentence)
    if len(tokens) <= maximum:
        return sentence.rstrip(".")
    clauses = re.split(r"\s*[;:]\s*|\s+but\s+|\s+while\s+|\s+however,\s+", sentence)
    for clause in clauses:
        clause = clause.strip(" .")
        if 10 <= len(words(clause)) <= maximum and FINITE_VERB_RE.search(clause):
            return clause
    return ""


def _lower_subject(sentence: str) -> str:
    if not sentence:
        return sentence
    first, rest = sentence[0], sentence[1:]
    if len(sentence) > 1 and first.isupper() and rest[:1].islower():
        return first.lower() + rest
    return sentence


def _capitalized(sentence: str) -> str:
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]


def select_answer_line(
    *,
    topic_title: str,
    session_title: str,
    block: str,
    current: str,
    allow_explicit: bool = True,
) -> tuple[str, str]:
    if not authored_answer_issues(current):
        return current, "retained-ready"

    relevance = relevance_terms(session_title, block)
    explicit = (
        _explicit_answer_candidates(block, session_title)
        if allow_explicit
        else []
    )
    if explicit:
        return explicit[0], "retained-authored"

    ranked = sorted(
        (
            (_candidate_score(candidate, session_title), candidate)
            for candidate in _candidate_sentences(block)
        ),
        key=lambda item: (item[0], -len(item[1])),
        reverse=True,
    )
    balanced = [
        candidate
        for score, candidate in ranked
        if score >= 20
        and not answer_line_issues(candidate)
        and STRONG_ANALYTICAL_RE.search(candidate)
        and (
            session_title_is_generic(session_title)
            or not relevance
            or relevance & title_terms(candidate)
        )
    ]
    if balanced:
        return balanced[0], "source-analytical"

    primary = next(
        (
            candidate
            for score, candidate in ranked
            if score >= 6
            and 10 <= len(words(candidate)) <= 34
            and FINITE_VERB_RE.search(candidate)
            and not re.match(
                r"^(?:it|this|these|those|they|therefore|thus|"
                r"answer|purpose|make|do not)\b",
                candidate,
                re.I,
            )
            and (
                session_title_is_generic(session_title)
                or not relevance
                or relevance & title_terms(candidate)
            )
        ),
        "",
    )
    qualification = _topic_qualification(topic_title, session_title)
    impact = _topic_impact(topic_title, session_title)
    if primary:
        base = _capitalized(_compress(primary, 22))
        if not base:
            primary = ""
        else:
            line = (
                f"{base}; institutionally, this supports {impact}, while "
                f"{qualification}."
            )
        if base and not answer_line_issues(line):
            return line, "source-plus-qualification"

    clean_title = re.sub(r"^\d+(?:\.\d+)*\s*", "", session_title).strip()
    clean_title = clean_title.replace("?", "").replace("!", "")
    anchors = _named_anchors(block)
    focus_phrases = [
        phrase
        for phrase in _focus_phrases(block)
        if not (
            phrase.casefold() == clean_title.casefold()
            or
            title_terms(phrase)
            and title_terms(phrase) <= title_terms(clean_title)
        )
    ]
    target = (
        topic_title
        if session_title_is_generic(clean_title)
        else _sentence_phrase(clean_title)
    )
    limitation = _best_limitation(block, relevance)
    if focus_phrases and limitation:
        focus = _joined_phrases(focus_phrases[:3])
        frame_verb = "define" if len(focus_phrases[:3]) > 1 else "defines"
        line = (
            f"{focus} {frame_verb} the institutional architecture of "
            f"{target}, but "
            f"{_lower_subject(limitation)}."
        )
        if not answer_line_issues(line):
            return line, "focus-limit-synthesis"
    if anchors:
        focus = ", ".join(anchors)
        structure_verb = (
            "structure"
            if len(anchors) > 1 or focus.casefold().startswith("articles ")
            else "structures"
        )
        line = (
            f"Under {topic_title}, {focus} "
            f"{structure_verb} {target} to advance {impact}, but {qualification}."
        )
    else:
        if focus_phrases:
            focus = _joined_phrases(focus_phrases)
            organise = "organise" if len(focus_phrases) > 1 else "organises"
            line = (
                f"{focus} {organise} {target} "
                f"to advance {impact}, but {qualification}."
            )
        else:
            subject = _sentence_phrase(clean_title)
            if "," in clean_title and " and " in clean_title.casefold():
                subject = "The relationship among " + subject
            line = (
                f"{subject} structures {impact} within "
                f"{topic_title}, but {qualification}."
            )
    line = _capitalized(line)
    for source, replacement in (
        (r"\bupsc\b", "UPSC"),
        (r"\bspsc\b", "SPSC"),
        (r"\bnjac\b", "NJAC"),
        (r"\becourts\b", "eCourts"),
        (r"\bgs-ii\b", "GS-II"),
        (r"\beci\b", "ECI"),
        (r"\bgst\b", "GST"),
        (r"\bcbi\b", "CBI"),
        (r"\bnhrc\b", "NHRC"),
        (r"\bcag\b", "CAG"),
    ):
        line = re.sub(source, replacement, line, flags=re.I)
    if len(words(line)) > MAX_ANSWER_WORDS:
        line = (
            f"{_sentence_phrase(clean_title)} links constitutional design to "
            f"{impact} within {topic_title}, but {qualification}."
        )
    if answer_line_issues(line):
        raise ValueError(
            f"Cannot produce a valid answer line for {session_title!r}: "
            + ", ".join(answer_line_issues(line))
        )
    return line, "topic-specific-fallback"


def parse_sessions(markdown: str, topic_title: str) -> list[Session]:
    matches = list(SESSION_RE.finditer(markdown))
    sessions: list[Session] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        body = markdown[match.end():end]
        formulations = FORMULATION_RE.findall(body)
        if len(formulations) != 1:
            raise ValueError(
                f"{match.group(2)}: expected one answer formulation, "
                f"found {len(formulations)}."
            )
        before = clean_markdown(formulations[0][1])
        session = Session(
            number=int(match.group(1)),
            title=match.group(2).strip(),
            start=match.start(),
            end=end,
            body=body,
            before=before,
            issues_before=tuple(answer_line_issues(before)),
        )
        session.after = before
        session.method = "embedded"
        sessions.append(session)
    return sessions


def force_unique_line(topic_title: str, session_title: str) -> str:
    clean_title = re.sub(r"^\d+(?:\.\d+)*\s*", "", session_title).strip()
    clean_title = clean_title.replace("?", "").replace("!", "")
    impact = _topic_impact(topic_title, session_title)
    qualification = _topic_qualification(topic_title, session_title)
    line = (
        f"In {topic_title}, {clean_title.lower()} links the governing rules to "
        f"{impact}, while {qualification}."
    )
    if len(words(line)) > MAX_ANSWER_WORDS:
        line = (
            f"{clean_title.title()} links {topic_title} to {impact}, while "
            f"{qualification}."
        )
    issues = answer_line_issues(line)
    if issues:
        raise ValueError(
            f"Cannot disambiguate {topic_title}/{session_title}: "
            + ", ".join(issues)
        )
    return line


def _closure_replacement(match: re.Match[str]) -> str:
    title = match.group("title").strip()
    fields: dict[str, str] = {}
    aliases = {
        "START / CONCEPT": "SUBTOPIC",
        "EXACT TERMS": "KEY TERMS / DEFINITIONS",
        "MECHANISM / ARGUMENT": "MECHANISM / ARGUMENT",
        "CONSEQUENCE / CONTRAST": "CONSEQUENCE / CONTRAST",
        "UPSC TRAP / ANSWER-USE": "UPSC TRAP / ANSWER-USE",
        "ANSWER-GRABBING FORMULATION": "ANSWER-GRABBING FORMULATION",
    }
    for line in match.group("body").splitlines():
        if ":" not in line:
            continue
        label, value = line.split(":", 1)
        mapped = aliases.get(label.strip().upper())
        if mapped:
            fields[mapped] = value.strip()
    fields.setdefault("SUBTOPIC", title)
    order = (
        "SUBTOPIC",
        "KEY TERMS / DEFINITIONS",
        "MECHANISM / ARGUMENT",
        "CONSEQUENCE / CONTRAST",
        "UPSC TRAP / ANSWER-USE",
        "ANSWER-GRABBING FORMULATION",
    )
    missing = [field for field in order if not fields.get(field)]
    if missing:
        raise ValueError(
            f"Closing flow {title!r} is missing fields: {', '.join(missing)}"
        )
    body = "\n".join(f"{field}: {fields[field]}" for field in order)
    return f"{match.group(1)}```closure-flow\n{body}\n```"


def _wrap_visual_line(line: str) -> list[str]:
    if len(line) <= MAX_TEXT_FENCE_WIDTH:
        return [line]
    indent = re.match(r"^\s*", line).group(0)
    content = line[len(indent):]
    continuation = indent + "  "
    if " -> " in content:
        continuation = indent + "  -> "
    elif " → " in content:
        continuation = indent + "  → "
    return textwrap.wrap(
        content,
        width=MAX_TEXT_FENCE_WIDTH - len(indent),
        initial_indent=indent,
        subsequent_indent=continuation,
        break_long_words=False,
        break_on_hyphens=False,
    )


def _wrap_text_fence(match: re.Match[str]) -> str:
    wrapped: list[str] = []
    for line in match.group("body").splitlines():
        wrapped.extend(_wrap_visual_line(line))
    return "```text\n" + "\n".join(wrapped) + "\n```"


def patch_session_body(body: str, answer: str) -> str:
    body, opening_count = OPENING_BLOCK_RE.subn(
        lambda match: match.group(1) + f"> {answer}\n",
        body,
        count=1,
    )
    if opening_count != 1:
        raise ValueError("Session lacks one answer-grabbing opening block.")
    body = INLINE_ANSWER_RE.sub(
        lambda match: match.group(1) + answer,
        body,
    )
    body, formulation_count = FORMULATION_RE.subn(
        lambda match: match.group(1) + answer,
        body,
        count=1,
    )
    if formulation_count != 1:
        raise ValueError("Session lacks one closure answer formulation.")
    if "```closure-flow" in body:
        closure_count = 1
    else:
        body, closure_count = CLOSING_FLOW_RE.subn(
            _closure_replacement,
            body,
            count=1,
        )
    if closure_count != 1:
        raise ValueError("Session lacks one text-fenced closing recall flow.")
    return body


def patch_markdown(markdown: str, sessions: list[Session]) -> str:
    output: list[str] = []
    cursor = 0
    for session in sessions:
        output.append(markdown[cursor:session.start])
        heading_end = session.start + markdown[session.start:session.end].find("\n")
        output.append(markdown[session.start:heading_end])
        output.append(patch_session_body(session.body, session.after))
        cursor = session.end
    output.append(markdown[cursor:])
    patched = "".join(output)
    patched = TEXT_FENCE_RE.sub(_wrap_text_fence, patched)
    return patched


def normalized_heading(value: str) -> str:
    value = re.sub(r"^\d+(?:\.\d+)*\s*", "", value)
    value = re.sub(r"[^A-Za-z0-9]+", " ", value).casefold()
    return re.sub(r"\s+", " ", value).strip()


def update_graphical_spec(
    topic_key: str,
    markdown_path: Path,
    generation: int,
    sessions: list[Session],
) -> dict[str, Any]:
    path = GRAPHICAL_SPEC_ROOT / f"{topic_key}.json"
    spec = load_json(path)
    by_title = {normalized_heading(session.title): session for session in sessions}
    used: set[str] = set()
    changes: list[dict[str, str]] = []
    for stage in spec.get("stages", []):
        if stage.get("role") == "extra":
            continue
        reference_titles: list[str] = []
        for reference in stage.get("source_references", []):
            match = re.search(r"#SESSION\s+\d+\s*[—-]\s*(.+)$", str(reference), re.I)
            if match:
                reference_titles.append(normalized_heading(match.group(1)))
        candidates = [
            by_title[title]
            for title in reference_titles
            if title in by_title and by_title[title].after.casefold() not in used
        ]
        if not candidates:
            stage_terms = title_terms(str(stage.get("title") or ""))
            ranked = sorted(
                (
                    (
                        len(stage_terms & title_terms(session.title)),
                        -abs(session.number - int(str(stage.get("id") or "0"))),
                        session,
                    )
                    for session in sessions
                    if session.after.casefold() not in used
                ),
                key=lambda item: (item[0], item[1]),
                reverse=True,
            )
            candidates = [ranked[0][2]] if ranked else []
        if not candidates:
            raise ValueError(f"{topic_key}: cannot map graphical stage {stage.get('id')}.")
        selected = candidates[0]
        before = str(stage.get("answer_line") or "").strip()
        stage["answer_line"] = selected.after
        used.add(selected.after.casefold())
        if before != selected.after:
            changes.append(
                {
                    "stage_id": str(stage.get("id")),
                    "stage_title": str(stage.get("title")),
                    "before": before,
                    "after": selected.after,
                    "source_session": selected.title,
                }
            )
    spec["source_markdown"] = relative(markdown_path)
    spec.setdefault("status", {})["line"] = (
        "Approval: FALSE • Pending user review • active generation "
        f"g{generation} repaired in place for answer-line and visual-boundary "
        "quality • all prior artifacts unchanged"
    )
    spec["presentation_quality_repair"] = {
        "repair_id": REPAIR_ID,
        "date": "2026-08-25",
        "generation_preserved": generation,
        "answer_strips_audited": len(
            [stage for stage in spec.get("stages", []) if stage.get("role") != "extra"]
        ),
        "answer_strips_changed": len(changes),
    }
    spec, _ = polity_flowchart_case_years.normalize_graphical_spec(spec)
    case_errors = polity_flowchart_case_years.graphical_spec_errors(spec)
    if case_errors:
        raise ValueError(
            f"{topic_key}: graphical case-year validation failed: "
            + " | ".join(case_errors)
        )
    write_json(path, spec)
    return {"path": relative(path), "changes": changes}


def graphical_changes_from_published_package(
    record: dict[str, Any],
    topic_key: str,
) -> list[dict[str, str]]:
    folder = (
        (record.get("continuous_core_first") or {}).get("folder")
        if isinstance(record.get("continuous_core_first"), dict)
        else None
    )
    if not folder:
        return []
    old_path = (
        ROOT
        / Path(str(folder).replace("\\", "/"))
        / "editable"
        / "topic-spec.json"
    )
    new_path = GRAPHICAL_SPEC_ROOT / f"{topic_key}.json"
    if not old_path.is_file() or not new_path.is_file():
        return []
    old = load_json(old_path)
    new = load_json(new_path)
    old_stages = {
        str(stage.get("id")): stage
        for stage in old.get("stages", [])
        if stage.get("role") != "extra"
    }
    output: list[dict[str, str]] = []
    for stage in new.get("stages", []):
        if stage.get("role") == "extra":
            continue
        stage_id = str(stage.get("id"))
        old_stage = old_stages.get(stage_id, {})
        before = str(old_stage.get("answer_line") or "").strip()
        after = str(stage.get("answer_line") or "").strip()
        if before != after:
            output.append(
                {
                    "stage_id": stage_id,
                    "stage_title": str(stage.get("title") or ""),
                    "before": before,
                    "after": after,
                    "source_session": "",
                }
            )
    return output


def build_overrides(*, apply: bool) -> dict[str, Any]:
    tracker = load_json(MASTER_TRACKER_PATH)
    topic_titles = {
        item["topic_key"]: item["topic_title"]
        for item in tracker.get("topics", [])
        if item.get("subject") == "Polity"
    }
    reviewed = load_json(REVIEWED_MAP_PATH)
    reviewed_topics = reviewed.get("topics", {})
    if set(reviewed_topics) != {f"polity-{number:02d}" for number in range(1, 56)}:
        raise ValueError("Reviewed answer-line map must contain exactly polity-01 through polity-55.")

    previous_current: dict[tuple[str, int], str] = {}
    previous_graphical: dict[str, list[dict[str, str]]] = {}
    if OVERRIDES_PATH.is_file():
        prior = load_json(OVERRIDES_PATH)
        if prior.get("repair_id") == REPAIR_ID:
            for topic_key, topic in prior.get("topics", {}).items():
                for session in topic.get("sessions", []):
                    previous_current[(topic_key, int(session["number"]))] = str(
                        session.get("after") or ""
                    )
                previous_graphical[topic_key] = list(
                    topic.get("graphical_spec", {}).get("changes", [])
                )

    work: list[
        tuple[dict[str, Any], str, Path, str, list[Session], dict[int, dict[str, Any]]]
    ] = []
    for record in active_polity_records():
        topic_key = str(record["topic_key"])
        markdown_path = ROOT / Path(str(record["markdown"]).replace("\\", "/"))
        markdown = markdown_path.read_text(encoding="utf-8")
        sessions = parse_sessions(markdown, topic_titles[topic_key])
        reviewed_topic = reviewed_topics[topic_key]
        reviewed_sessions = {
            int(item["number"]): item
            for item in reviewed_topic.get("sessions", [])
        }
        if set(reviewed_sessions) != {session.number for session in sessions}:
            raise ValueError(f"{topic_key}: reviewed session set does not match active Markdown.")
        for session in sessions:
            item = reviewed_sessions[session.number]
            if normalized_heading(session.title) != normalized_heading(str(item["title"])):
                raise ValueError(
                    f"{topic_key} session {session.number}: reviewed title mismatch."
                )
            rejected = str(item["rejected_after"]).strip()
            final = str(item["final"]).strip()
            allowed_active = {
                rejected,
                final,
                previous_current.get((topic_key, session.number), ""),
            }
            if session.before not in allowed_active:
                raise ValueError(
                    f"{topic_key} session {session.number}: active line differs from both "
                    "the rejected and final reviewed text."
                )
            session.before = rejected
            session.after = final
            session.method = str(item["origin"])
            session.issues_before = tuple(answer_line_issues(rejected))
        work.append(
            (record, topic_key, markdown_path, markdown, sessions, reviewed_sessions)
        )

    topics: dict[str, Any] = {}
    for (
        record,
        topic_key,
        markdown_path,
        markdown,
        sessions,
        reviewed_sessions,
    ) in work:
        if apply:
            markdown_path.write_text(
                patch_markdown(markdown, sessions),
                encoding="utf-8",
                newline="\n",
            )
        graphical = (
            update_graphical_spec(
                topic_key,
                markdown_path,
                int(record["generation"]),
                sessions,
            )
            if apply
            else {"path": relative(GRAPHICAL_SPEC_ROOT / f"{topic_key}.json"), "changes": []}
        )
        if apply:
            published_changes = graphical_changes_from_published_package(
                record,
                topic_key,
            )
            if published_changes:
                graphical["changes"] = published_changes
        if apply and previous_graphical.get(topic_key):
            merged_by_stage = {
                item["stage_id"]: item
                for item in previous_graphical[topic_key]
            }
            for change in graphical["changes"]:
                prior_change = merged_by_stage.get(change["stage_id"])
                if prior_change:
                    change["before"] = prior_change["before"]
                merged_by_stage[change["stage_id"]] = change
            graphical["changes"] = [
                merged_by_stage[key]
                for key in sorted(merged_by_stage)
            ]
        topics[topic_key] = {
            "record_id": record["record_id"],
            "generation": record["generation"],
            "approved": record["approved"],
            "topic_title": topic_titles[topic_key],
            "markdown": relative(markdown_path),
            "main_pdf": record["main_pdf"],
            "workbook": record["workbook"],
            "sessions_audited": len(sessions),
            "answer_lines_changed": sum(
                session.before != session.after for session in sessions
            ),
            "sessions": [
                {
                    "number": session.number,
                    "title": session.title,
                    "original_before": reviewed_sessions[session.number]["before"],
                    "before": session.before,
                    "after": session.after,
                    "changed": session.before != session.after,
                    "method": session.method,
                    "issues_before": list(session.issues_before),
                }
                for session in sessions
            ],
            "graphical_spec": graphical,
        }
    payload = {
        "schema_version": 1,
        "repair_id": REPAIR_ID,
        "generated_at": datetime.now().astimezone().isoformat(),
        "subject": "Polity",
        "active_topic_count": len(topics),
        "generation_policy": "deterministic human-reviewed answer-line map",
        "approval_preserved": False,
        "topics": topics,
    }
    if apply:
        write_json(OVERRIDES_PATH, payload)
    return payload


def validate_overrides(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    lines: list[tuple[str, int, str, str]] = []
    for topic_key, topic in data.get("topics", {}).items():
        for session in topic.get("sessions", []):
            line = str(session.get("after") or "")
            for issue in answer_line_issues(line):
                errors.append(
                    f"{topic_key} session {session.get('number')}: {issue}: {line}"
                )
            lines.append(
                (
                    topic_key,
                    int(session.get("number") or 0),
                    str(session.get("title") or ""),
                    line,
                )
            )
    duplicates = Counter(line.casefold() for _, _, _, line in lines)
    for normalized, count in duplicates.items():
        if count <= 1:
            continue
        locations = [
            f"{topic_key}/session-{number}"
            for topic_key, number, _, line in lines
            if line.casefold() == normalized
        ]
        errors.append(
            f"duplicate answer line across sessions ({count}): "
            + ", ".join(locations)
        )
    phrase_audit = duplicate_phrase_audit(lines)
    for finding in phrase_audit["repeated_six_word_prefixes"]:
        errors.append(
            "repeated six-word prefix across sessions: "
            f"{finding['phrase']}: {', '.join(finding['locations'])}"
        )
    for finding in phrase_audit["repeated_six_word_suffixes"]:
        errors.append(
            "repeated six-word suffix across sessions: "
            f"{finding['phrase']}: {', '.join(finding['locations'])}"
        )
    for finding in phrase_audit["repeated_eight_word_cross_topic_phrases"]:
        errors.append(
            "repeated eight-word phrase across unrelated topics: "
            f"{finding['phrase']}: {', '.join(finding['topics'])}"
        )
    return errors


def visual_source_errors(markdown: str) -> list[str]:
    errors: list[str] = []
    if LEGACY_CLOSING_START_RE.search(markdown):
        errors.append("legacy text-fenced closing flow remains")
    for match in TEXT_FENCE_RE.finditer(markdown):
        for number, line in enumerate(match.group("body").splitlines(), 1):
            if len(line) > MAX_TEXT_FENCE_WIDTH:
                errors.append(
                    f"text visual line {number} is {len(line)} characters "
                    f"(maximum {MAX_TEXT_FENCE_WIDTH})"
                )
    for match in re.finditer(
        r"(?ms)^```ascii-master\s*\n(?P<body>.*?)\n```",
        markdown,
    ):
        for number, line in enumerate(match.group("body").splitlines(), 1):
            if len(line) > 100:
                errors.append(
                    f"ASCII-master line {number} is {len(line)} characters "
                    "(maximum 100)"
                )
    return errors


def validate_active_sources(data: dict[str, Any]) -> list[str]:
    errors = validate_overrides(data)
    for topic_key, topic in data.get("topics", {}).items():
        markdown_path = ROOT / Path(str(topic["markdown"]).replace("\\", "/"))
        markdown = markdown_path.read_text(encoding="utf-8")
        sessions = parse_sessions(markdown, str(topic["topic_title"]))
        expected_items = {
            int(item["number"]): item
            for item in topic.get("sessions", [])
        }
        if len(sessions) != len(expected_items):
            errors.append(f"{topic_key}: session count changed after repair")
        for session in sessions:
            expected = expected_items.get(session.number, {})
            if session.before != str(expected.get("after") or ""):
                errors.append(
                    f"{topic_key} session {session.number}: "
                    "embedded answer line does not match override"
                )
        errors.extend(
            f"{topic_key}: {error}" for error in visual_source_errors(markdown)
        )
        spec = load_json(
            GRAPHICAL_SPEC_ROOT / f"{topic_key}.json"
        )
        graphical_lines = [
            str(stage.get("answer_line") or "")
            for stage in spec.get("stages", [])
            if stage.get("role") != "extra"
        ]
        if len(graphical_lines) != len(set(line.casefold() for line in graphical_lines)):
            errors.append(f"{topic_key}: duplicate graphical answer strips")
        for index, line in enumerate(graphical_lines):
            for issue in answer_line_issues(line):
                errors.append(
                    f"{topic_key} graphical stage {index:02d}: {issue}: {line}"
                )
    return errors


def command_summary(data: dict[str, Any]) -> dict[str, int]:
    sessions = [
        session
        for topic in data["topics"].values()
        for session in topic["sessions"]
    ]
    graphical = [
        change
        for topic in data["topics"].values()
        for change in topic["graphical_spec"]["changes"]
    ]
    defect_counts = Counter(
        issue for session in sessions for issue in session["issues_before"]
    )
    return {
        "topics": len(data["topics"]),
        "sessions": len(sessions),
        "answer_lines_changed": sum(item["changed"] for item in sessions),
        "graphical_answer_strips_changed": len(graphical),
        "duplicate_defects": defect_counts["duplicate"],
        "generic_or_mechanical_defects": (
            defect_counts["mechanical-or-instructional"]
            + defect_counts["non-analytical"]
            + defect_counts["metadata"]
        ),
        "legal_absolute_defects": defect_counts["legally-risky-absolute"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()
    data = build_overrides(apply=args.apply)
    errors = validate_active_sources(data) if args.apply or args.validate else validate_overrides(data)
    print(json.dumps(command_summary(data), indent=2))
    if errors:
        print("errors=" + str(len(errors)))
        for error in errors[:100]:
            print("- " + error)
        return 1
    print("validation=passed")
    if args.apply:
        print(f"overrides={relative(OVERRIDES_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
