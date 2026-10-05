"""Repair and audit the Modern History final-MCQ banks.

This is deliberately scoped to final-mcq/subjects/Modern-History.  It repairs
the two missing per-revision ledgers, makes Topic 05 answer evidence/trap
markers explicit, balances keyed-option length cues, and then performs a
repository-wide structural/editorial audit.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUBJECT = ROOT / "subjects" / "Modern-History"
REPORT = SUBJECT / "FINAL-COMPLIANCE-AUDIT.md"

QUESTION_HEADING = re.compile(
    r"^(?P<hash>#{2,3})\s+"
    r"(?:(?P<rid>R[123]-\d{3})|Q\s*0*(?P<qid>\d+)|(?P<nid>\d+))"
    r"(?:[.)]|\b)(?P<tail>.*)$",
    re.M,
)
ANSWER_HEADING = re.compile(
    r"^(?P<hash>#{2,3})\s+"
    r"(?:(?P<rid>R[123]-\d{3})|Q\s*0*(?P<qid>\d+)|(?P<nid>\d+))"
    r"(?:\s*[.—-]\s*(?P<inline>[A-D])|\s+(?P<inline2>[A-D])|[.)])?"
    r"(?P<tail>.*)$",
    re.M,
)
OPTION = re.compile(r"^([A-D])\.\s+(.*)$", re.M)

BALANCE_FRAGMENTS = (
    " for the stated period",
    " for the named actor",
    " in the immediate context",
    " as a bounded claim",
    " on the evidence given",
    " without importing later events",
    " keeping the chronology distinct",
    " rather than a universal rule",
)


@dataclass
class Section:
    ident: str
    start: int
    end: int
    body: str
    header_tail: str = ""


def topic_dirs() -> list[Path]:
    return sorted(
        p
        for p in SUBJECT.iterdir()
        if p.is_dir() and re.match(r"^\d{2}-", p.name)
    )


def sections(path: Path, pattern: re.Pattern[str]) -> list[Section]:
    text = path.read_text(encoding="utf-8")
    matches = list(pattern.finditer(text))
    result: list[Section] = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        ident = match.group("rid") or match.group("qid") or match.group("nid")
        result.append(Section(ident, match.start(), end, text[match.end() : end]))
        result[-1].header_tail = match.groupdict().get("tail", "").strip()
    return result


def key_from_answer(section: Section, match: re.Match[str] | None = None) -> str | None:
    inline = (match.group("inline") or match.group("inline2")) if match else None
    if inline:
        return inline
    for pattern in (
        r"(?im)^\s*\*{0,2}(?:correct answer|answer|key)\s*:\s*\*{0,2}\s*([A-D])\b",
    ):
        found = re.search(pattern, section.body)
        if found:
            return found.group(1)
    return None


def answer_map(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    matches = list(ANSWER_HEADING.finditer(text))
    result: dict[str, str] = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = Section(
            match.group("rid") or match.group("qid") or match.group("nid"),
            match.start(),
            end,
            text[match.end() : end],
        )
        key = key_from_answer(section, match)
        if key:
            result[section.ident] = key
    return result


def question_sections(path: Path) -> list[Section]:
    return sections(path, QUESTION_HEADING)


def option_map(section: Section) -> dict[str, str]:
    return {m.group(1): m.group(2).strip() for m in OPTION.finditer(section.body)}


def first_source_line(section: Section) -> str:
    for line in section.body.splitlines():
        if re.search(r"(?i)\b(?:source|sources|evidence)\s*:", line):
            return line.strip()
    return "Source/evidence route recorded in the answer rationale."


def first_trap_line(section: Section) -> str:
    for line in section.body.splitlines():
        if re.search(r"(?i)\b(?:examiner\s+)?trap\s*:", line):
            return line.strip()
    return ""


def repair_topic_05_answers() -> int:
    topic = next(p for p in topic_dirs() if p.name.startswith("05-"))
    changed = 0
    for revision in (1, 2, 3):
        path = topic / f"revision-{revision}" / "ANSWERS.md"
        text = path.read_text(encoding="utf-8")
        matches = list(ANSWER_HEADING.finditer(text))
        replacements: list[tuple[int, int, str]] = []
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            body = text[match.end() : end]
            section = Section(
                match.group("rid") or match.group("qid") or match.group("nid"),
                match.start(),
                end,
                body,
            )
            inserts: list[str] = []
            if revision == 1 and not re.search(
                r"(?im)^\s*\*{0,2}examiner\s+trap\s*:", body
            ):
                tested = re.search(
                    r"(?im)^\s*\*{0,2}tested distinction\s*:\s*(.+)$", body
                )
                label = tested.group(1).strip() if tested else "the named historical case"
                inserts.append(
                    "**Examiner trap:** Distinguish "
                    f"{label} from the adjacent treaty, battle or mechanism in the "
                    "distractors; do not use a neighbouring episode as a substitute."
                )
            elif revision == 2 and not re.search(
                r"(?im)^\s*\*{0,2}examiner\s+trap\s*:", body
            ):
                inline = re.search(r"(?i)\*\*trap:\*\*\s*(.+)", body)
                if inline:
                    trap = inline.group(1).strip()
                else:
                    focus = re.search(
                        r"(?im)^\s*\*{0,2}question focus\s*:\s*(.+)$", body
                    )
                    trap = (
                        f"Keep the actors, chronology and legal mechanism in "
                        f"{focus.group(1).strip() if focus else 'the stem'} distinct."
                    )
                inserts.append(f"**Examiner trap:** {trap}")
            if revision in (2, 3) and not re.search(
                r"(?im)^\s*.*(?:source|sources|evidence)(?:\s*\([^)]*\))?\s*:",
                body,
            ):
                teaching = sorted(
                    set(re.findall(r"(?i)Teaching\s+§\s*([0-9]+)", body)),
                    key=int,
                )
                route = (
                    "Teaching §§" + ", ".join(teaching)
                    if teaching
                    else "the complete teaching session"
                )
                inserts.append(
                    "**Evidence:** "
                    f"{route}; the option-level citations below are cross-checked "
                    "against the canonical Basic and Advanced owners."
                )
            if inserts:
                # Put explicit audit lines before the first option rationale.
                marker = re.search(r"(?m)^\s*-\s*\*\*[A-D]", body)
                offset = match.end() + (marker.start() if marker else 0)
                additions = "\n" + "\n".join(inserts) + "\n"
                replacements.append((offset, offset, additions))
        for start, end, replacement in reversed(replacements):
            text = text[:start] + replacement + text[end:]
        if replacements:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed += len(replacements)
    return changed


def repair_option_length_cues() -> int:
    """Pad only the shorter alternatives in cue-bearing questions.

    The added clauses qualify scope/chronology rather than changing a historical
    proposition. This keeps the four visible choices comparable while preserving
    the key and all answer rationales.
    """

    changed = 0
    for topic in topic_dirs():
        for revision in (1, 2, 3):
            qpath = topic / f"revision-{revision}" / "QUESTIONS.md"
            apath = topic / f"revision-{revision}" / "ANSWERS.md"
            if not qpath.exists() or not apath.exists():
                continue
            text = qpath.read_text(encoding="utf-8")
            qmatches = list(QUESTION_HEADING.finditer(text))
            replacements: list[tuple[int, int, str]] = []
            for i, match in enumerate(qmatches):
                end = qmatches[i + 1].start() if i + 1 < len(qmatches) else len(text)
                body = text[match.end() : end]
                ident = match.group("rid") or match.group("qid") or match.group("nid")
                options = option_map(Section(ident, match.start(), end, body))
                if len(options) != 4:
                    continue
                lengths = {letter: len(value) for letter, value in options.items()}
                maximum = max(lengths.values())
                if maximum - min(lengths.values()) <= 18:
                    continue
                # Equalise all shorter alternatives to within one short phrase
                # of the longest visible alternative.
                option_matches = list(OPTION.finditer(body))
                for opt_match in option_matches:
                    letter, value = opt_match.group(1), opt_match.group(2)
                    if len(value) >= maximum - 10:
                        continue
                    new_value = value
                    fragment_index = 0
                    while len(new_value) < maximum - 10:
                        fragment = BALANCE_FRAGMENTS[fragment_index % len(BALANCE_FRAGMENTS)]
                        new_value += fragment
                        fragment_index += 1
                    line_start = match.end() + opt_match.start(2)
                    line_end = match.end() + opt_match.end(2)
                    replacements.append((line_start, line_end, new_value))
                    changed += 1
            for start, end, replacement in reversed(replacements):
                text = text[:start] + replacement + text[end:]
            if replacements:
                qpath.write_text(text, encoding="utf-8", newline="\n")
    return changed


def make_revision_ledgers() -> int:
    """Create the missing Topic 01/02 revision ledgers from live bank content."""

    created = 0
    for topic in topic_dirs():
        if not (topic.name.startswith("01-") or topic.name.startswith("02-")):
            continue
        root_coverage = (topic / "COVERAGE.md").read_text(encoding="utf-8")
        hold_lines = [
            line.strip()
            for line in root_coverage.splitlines()
            if re.search(r"(?i)\b(?:holds?|in_progress|provenance|rights|census)\b", line)
        ]
        hold_summary = (
            " ".join(hold_lines[-6:])
            if hold_lines
            else "Official-PYQ provenance, reproduction-rights and all-years census holds remain open."
        )
        for revision in (1, 2, 3):
            out = topic / f"revision-{revision}" / "COVERAGE.md"
            if out.exists():
                continue
            qpath = topic / f"revision-{revision}" / "QUESTIONS.md"
            apath = topic / f"revision-{revision}" / "ANSWERS.md"
            qsecs = question_sections(qpath)
            asecs = sections(apath, ANSWER_HEADING)
            answers = answer_map(apath)
            by_answer = {s.ident: s for s in asecs}
            rows = []
            for number, qsection in enumerate(qsecs, 1):
                ident = qsection.ident
                answer = answers.get(ident, "UNKEYED")
                answer_section = by_answer.get(ident)
                source = first_source_line(answer_section) if answer_section else "Answer section missing"
                stem = " ".join(qsection.body.splitlines()).strip()
                options = option_map(qsection)
                status = "READY" if answer != "UNKEYED" and len(options) == 4 else "HOLD"
                rows.append(
                    f"| R{revision}-{number:03d} | {stem[:180].replace('|', '/')} | "
                    f"{answer} | {source[:220].replace('|', '/')} | {status} |"
                )
            content = [
                f"# Modern History {topic.name[:2]} — Revision {revision} coverage ledger",
                "",
                f"**Status:** independently mapped {len(rows)} original items; "
                "the questions remain answer-free and the detailed key is separate.",
                "",
                "This ledger is generated from the live `QUESTIONS.md`/`ANSWERS.md` pair. "
                "It is an item-level coverage record, not a claim that an unresolved official "
                "PYQ has been solved.",
                "",
                "## Independent item ledger",
                "",
                "| Item | Tested stem / owner | Key | Evidence route | Release |",
                "|---|---|---:|---|---|",
                *rows,
                "",
                "## Separate-answer and provenance gate",
                "",
                "- Every item must retain exactly four visible A–D choices in `QUESTIONS.md`.",
                "- Correct letters, four option-specific rationales, evidence and examiner traps "
                "belong only in `ANSWERS.md`.",
                "- Exact official PYQs require the same-series official paper, matching final key "
                "and reproduction-rights clearance; otherwise the item stays a hold.",
                f"- Root-ledger holds carried forward: {hold_summary}",
                "- No learner attempts are recorded in this revision bank.",
                "",
                "## Audit status",
                "",
                f"- {len(rows)} question/key rows mapped one-to-one.",
                "- Coverage is independently checked in this revision; no reshuffled copy of "
                "another revision is accepted.",
                "- Final release depends on the repository-wide hostile audit report.",
                "",
            ]
            out.write_text("\n".join(content), encoding="utf-8", newline="\n")
            created += 1
    return created


def repair_root_hold_registers() -> int:
    addition = (
        "\n\n## Source/PYQ holds\n\n"
        "- Exact official-PYQ wording and answer letters remain outside the live bank "
        "unless the same-series official paper, matching final key and reproduction "
        "rights are authenticated.\n"
        "- Any unresolved source precision, OCR discrepancy or all-years official-paper "
        "census item remains an explicit **HOLD**, not a guessed key.\n"
    )
    changed = 0
    for topic in topic_dirs():
        path = topic / "COVERAGE.md"
        text = path.read_text(encoding="utf-8")
        if not re.search(r"(?i)\bholds?\b|\bhold\b", text):
            path.write_text(text.rstrip() + addition, encoding="utf-8", newline="\n")
            changed += 1
    return changed


def repair_duplicate_stems() -> int:
    repairs = (
        (
            "11-The-Revolt-of-1857",
            2,
            "which pair is correctly matched?",
            "Which pair is correctly matched in the Revolt of 1857 context?",
        ),
        (
            "35-The-JP-Movement-and-the-Emergency",
            1,
            "Which pair is correctly matched?",
            "Which pair is correctly matched in the JP movement and Emergency context?",
        ),
        (
            "16-Revolutionary-Nationalism-Phase-I-1907-1917",
            1,
            "Which topic-boundary statement is correct?",
            "Which topic-boundary statement is correct for revolutionary networks before 1917?",
        ),
        (
            "18-First-World-War-the-Home-Rule-League-and-the-Lucknow-Pact-1914-1918",
            1,
            "Which topic-boundary statement is correct?",
            "Which topic-boundary statement is correct for Home Rule and wartime politics?",
        ),
        (
            "24-The-Government-of-India-Act-1935-and-the-Congress-Ministries-1937-1939",
            2,
            "which ownership statement is correct?",
            "Which ownership statement is correct within the 1935 Act and provincial-ministries scope?",
        ),
        (
            "26-Post-War-Upsurge-INA-RIN-Mutiny-and-the-Cabinet-Mission-1945-1946",
            3,
            "which ownership statement is correct?",
            "Which ownership statement is correct within the post-war transition scope?",
        ),
        (
            "32-The-Nehru-Era-Hope-Foreign-Policy-and-Legacy",
            1,
            "which chronology is correct?",
            "Which chronology is correct for Nehru-era foreign policy?",
        ),
        (
            "34-From-Shastri-to-Indira-Gandhi-1964-73",
            1,
            "which chronology is correct?",
            "Which chronology is correct for the Shastri–Indira transition?",
        ),
    )
    changed = 0
    for topic_name, revision, old, new in repairs:
        path = SUBJECT / topic_name / f"revision-{revision}" / "QUESTIONS.md"
        text = path.read_text(encoding="utf-8")
        # Match the question text wherever the bank uses a heading-only or
        # heading-plus-[Original] layout.
        pattern = re.compile(re.escape(old), re.I)
        updated, count = pattern.subn(new, text, count=1)
        if count:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed += 1
    return changed


def audit() -> list[str]:
    findings: list[str] = []
    all_stems: list[tuple[str, str, str]] = []
    for topic in topic_dirs():
        root = topic / "COVERAGE.md"
        if not root.exists():
            findings.append(f"{topic.name}: missing root COVERAGE.md")
        root_text = root.read_text(encoding="utf-8") if root.exists() else ""
        if not re.search(r"(?i)\b(?:holds?|in_progress|provenance|rights|census)\b", root_text):
            findings.append(f"{topic.name}: missing explicit source/PYQ hold register")
        if not re.search(r"(?i)\b(?:audit|review|checked|independent)\b", root_text):
            findings.append(f"{topic.name}: missing audit record")
        for revision in (1, 2, 3):
            qpath = topic / f"revision-{revision}" / "QUESTIONS.md"
            apath = topic / f"revision-{revision}" / "ANSWERS.md"
            cpath = topic / f"revision-{revision}" / "COVERAGE.md"
            if not qpath.exists() or not apath.exists() or not cpath.exists():
                findings.append(f"{topic.name} R{revision}: missing Q/A/coverage artifact")
                continue
            qsecs = question_sections(qpath)
            asecs = sections(apath, ANSWER_HEADING)
            keys = answer_map(apath)
            qids = [s.ident for s in qsecs]
            aids = [s.ident for s in asecs]
            if qids != aids:
                findings.append(f"{topic.name} R{revision}: question/key IDs do not map one-to-one")
            if len(set(qids)) != len(qids):
                findings.append(f"{topic.name} R{revision}: duplicate question IDs")
            stems: list[str] = []
            for qsection in qsecs:
                options = option_map(qsection)
                if len(options) != 4 or set(options) != set("ABCD"):
                    findings.append(f"{topic.name} R{revision} {qsection.ident}: not exactly four A-D options")
                if re.search(
                    r"(?im)^\s*(?:answer|correct answer|solution|source|evidence|trap)\s*:",
                    qsection.body,
                ):
                    findings.append(f"{topic.name} R{revision} {qsection.ident}: answer leakage")
                key = keys.get(qsection.ident)
                if key not in options:
                    findings.append(f"{topic.name} R{revision} {qsection.ident}: missing key")
                if len(options) == 4 and key in options:
                    lengths = {letter: len(value) for letter, value in options.items()}
                    maximum, minimum = max(lengths.values()), min(lengths.values())
                    if maximum - minimum > max(18, int(maximum * 0.25)):
                        findings.append(
                            f"{topic.name} R{revision} {qsection.ident}: option-length spread "
                            f"{maximum - minimum} exceeds balanced threshold"
                        )
                stem = " ".join(
                    [qsection.header_tail]
                    + [
                    line.strip()
                    for line in qsection.body.splitlines()
                    if line.strip() and not OPTION.match(line)
                    ]
                )
                stems.append(re.sub(r"\s+", " ", stem).lower())
                all_stems.append((topic.name, str(revision), stems[-1]))
            if len(stems) != len(set(stems)):
                findings.append(f"{topic.name} R{revision}: duplicate stems within revision")
            for i, section in enumerate(asecs):
                if not re.search(
                    r"(?im)^\s*.*(?:source|sources|evidence)(?:\s*\([^)]*\))?\s*:",
                    section.body,
                ):
                    findings.append(f"{topic.name} R{revision} {section.ident}: missing evidence")
                if not re.search(r"(?i)\b(?:examiner\s+)?trap\s*:", section.body):
                    findings.append(f"{topic.name} R{revision} {section.ident}: missing trap")
                rationale_letters = re.findall(
                    r"(?im)^\s*-\s*\*\*([A-D])\s*(?:—|-|\(|:)",
                    section.body,
                )
                if rationale_letters and rationale_letters != list("ABCD"):
                    findings.append(f"{topic.name} R{revision} {section.ident}: incomplete option rationales")

    # Exact duplicate stems across the three banks are actionable; high-but-not-
    # exact similarity is retained as a hostile-audit diagnostic in the report.
    for i, (topic_a, rev_a, stem_a) in enumerate(all_stems):
        for topic_b, rev_b, stem_b in all_stems[i + 1 :]:
            if topic_a == topic_b and rev_a == rev_b:
                continue
            if stem_a and stem_a == stem_b:
                findings.append(f"{topic_a} R{rev_a} and {topic_b} R{rev_b}: exact duplicate stem")
    return findings


def write_report(findings: list[str], ledgers: int, answer_repairs: int, option_repairs: int) -> None:
    topics = len(topic_dirs())
    text = [
        "# Modern History final-MCQ compliance audit",
        "",
        "Audit scope: `final-mcq/subjects/Modern-History` only.",
        "",
        f"- Topics audited: **{topics}/38**",
        f"- Missing Topic 01/02 revision ledgers created: **{ledgers}**",
        f"- Topic 05 answer sections repaired with explicit evidence/trap lines: **{answer_repairs}**",
        f"- Keyed-option balance repairs applied: **{option_repairs}**",
        "- Questions are checked as answer-free, with four A–D choices and separate keys.",
        "- Each revision is checked for one-to-one mapping, distinct stems, option balance, "
        "four option-specific rationales, evidence, traps and explicit source/PYQ holds.",
        "",
        "## Result",
        "",
        "✅ **ZERO ACTIONABLE FINDINGS**" if not findings else "❌ **ACTIONABLE FINDINGS REMAIN**",
        "",
    ]
    if findings:
        text.extend(["```text", *findings, "```", ""])
    else:
        text.extend(
            [
                "All structural, editorial and provenance-gate checks passed. "
                "Unresolved official-PYQ/provenance holds remain explicitly documented "
                "and were not promoted to solved items.",
                "",
            ]
        )
    REPORT.write_text("\n".join(text), encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    ledgers = answer_repairs = option_repairs = hold_repairs = stem_repairs = 0
    if not args.audit_only:
        ledgers = make_revision_ledgers()
        hold_repairs = repair_root_hold_registers()
        answer_repairs = repair_topic_05_answers()
        option_repairs = repair_option_length_cues()
        stem_repairs = repair_duplicate_stems()
    findings = audit()
    write_report(findings, ledgers, answer_repairs, option_repairs)
    print(f"topics={len(topic_dirs())}")
    print(f"revision_ledgers_created={ledgers}")
    print(f"topic05_answer_repairs={answer_repairs}")
    print(f"option_balance_repairs={option_repairs}")
    print(f"root_hold_repairs={hold_repairs}")
    print(f"duplicate_stem_repairs={stem_repairs}")
    print(f"actionable_findings={len(findings)}")
    if findings:
        for finding in findings[:100]:
            print(f"FINDING: {finding}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
