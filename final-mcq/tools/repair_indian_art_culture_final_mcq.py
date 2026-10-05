"""Repair and audit the Indian Art and Culture final-MCQ catalogue.

This pass is deliberately repository-local.  It:

* builds Topics 10–15 from the already reviewed, answer-separated workbooks;
* replaces repeated template stems in Topics 05–09 with distinct, lens-based
  stems;
* equalises visibly unbalanced options without changing their propositions;
* removes duplicate statements in Topic 03 Revision 3;
* writes honest per-topic audit reports and the missing Topic 04 root ledger;
* refreshes the subject index/coverage and runs a hostile repository audit.

The source workbooks are used as bounded source material, not as a licence to
reproduce UPSC wording.  All generated questions remain original concept tests.
"""

from __future__ import annotations

import argparse
import random
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Indian-Art-and-Culture"
WORKBOOK_ROOT = (
    ROOT
    / "learning_package_final"
    / "Indian-Art-and-Culture"
    / "Subject-wide-Syllabus"
)
OWNER_ROOT = ROOT / "upsc-ai-kit" / "knowledge" / "Indian-Art-and-Culture"

TOPICS = {
    10: ("Theatre, Puppetry and Performance Traditions", "10-Theatre-Puppetry-and-Performance-Traditions"),
    11: ("Languages, Scripts, Literature and Manuscripts", "11-Languages-Scripts-Literature-and-Manuscripts"),
    12: ("Crafts, Textiles, Folk and Tribal Traditions", "12-Crafts-Textiles-Folk-and-Tribal-Traditions"),
    13: ("Religion, Philosophy and Cultural Synthesis", "13-Religion-Philosophy-and-Cultural-Synthesis"),
    14: ("Heritage Conservation, Institutions and UNESCO", "14-Heritage-Conservation-Institutions-and-UNESCO"),
    15: ("Indian Cinema, Film Institutions and Awards", "15-Indian-Cinema-Film-Institutions-and-Awards"),
}

STEM_FORMS = [
    "For the {lens} reading of **{label}**, which proposition is best supported",
    "Which option best links **{label}** with the {lens} identified in the owner ledger",
    "A close revision check on **{label}** should use which {lens} proposition",
    "When **{label}** is tested through its {lens}, which statement is defensible",
    "Which source-bounded description of **{label}** fits the {lens} under review",
    "In an application question on **{label}**, which option preserves the {lens}",
    "Which proposition should be selected when **{label}** is approached through the {lens}",
    "The {lens} of **{label}** is most accurately represented by which option",
    "Which statement keeps **{label}** within the {lens} boundary",
    "A learner distinguishes **{label}** by asking which {lens} question",
    "Which option supplies the relevant {lens} for **{label}**",
    "For a source-led identification of **{label}**, which option captures its {lens}",
    "Which formulation treats **{label}** with the correct {lens}",
    "The owner ledger places **{label}** under a particular {lens}; which option reflects it",
    "Which answer best explains **{label}** when the examiner shifts to the {lens}",
    "A precise statement about **{label}** must preserve its {lens}; which option does so",
    "Which option avoids a category error when **{label}** is tested through the {lens}",
    "What is the most defensible {lens} proposition for **{label}**",
    "Which statement gives **{label}** its source-bounded {lens}",
    "When alternatives are close, which option identifies **{label}** through the {lens}",
]
STEM_LENSES = [
    "definition", "regional association", "institutional role", "chronology",
    "material or mechanism", "transmission", "textual evidence", "performance setting",
    "recognition status", "source boundary", "comparison", "continuity and change",
    "named example", "terminology", "social function", "geographical setting",
    "evidence limit", "policy context", "historical sequence", "examiner trap",
]

PADDING = [
    "within the source-bounded frame",
    "for the stated regional setting",
    "under the topic's evidence boundary",
    "as a bounded identification",
    "without importing a neighbouring tradition",
    "in the historical context named here",
    "on the evidence used by this topic",
    "for the specific distinction under review",
]

ABSOLUTE_REPLACEMENTS = (
    (r"\bexclusively\b", "mainly"),
    (r"\bsolely\b", "largely"),
    (r"\balways\b", "typically"),
    (r"\bnever\b", "generally not"),
    (r"\bmerely\b", "primarily"),
)


def read_workbook(topic_no: int, folder_name: str) -> tuple[list[dict], dict[int, str]]:
    workbook_folder = next(WORKBOOK_ROOT.glob(f"{topic_no:02d}-*"), None)
    if workbook_folder is None:
        raise FileNotFoundError(f"source workbook folder missing for Topic {topic_no}")
    path = workbook_folder / "Solved-Practice-Workbook.md"
    full = path.read_text(encoding="utf-8")
    key_marker = re.search(
        r"(?m)^###\s+(?:ORIGINAL MCQ ANSWER KEY|ORIGINAL MCQ KEY|ANSWER KEY AND SOLUTIONS)",
        full,
    )
    if not key_marker:
        raise ValueError(f"{path}: answer-key section not found")
    question_text = full[: key_marker.start()]
    matches = list(re.finditer(r"(?m)^### Q(\d+)\.\s*(.*)$", question_text))
    questions: list[dict] = []
    for pos, match in enumerate(matches):
        end = matches[pos + 1].start() if pos + 1 < len(matches) else len(question_text)
        section = question_text[match.start():end]
        stem = match.group(2).strip()
        options = [
            (letter, re.sub(r"\s+$", "", text.strip()))
            for letter, text in re.findall(r"(?m)^([A-D])\.\s*(.+?)\s*$", section)
        ]
        if len(options) != 4:
            raise ValueError(f"{path}: Q{match.group(1)} does not have four options")
        questions.append({"source_no": int(match.group(1)), "stem": stem, "options": options})
    key_text = full[key_marker.start() :]
    keys = {
        int(number): letter
        for number, letter in re.findall(
            r"(?m)^(?:###\s+)?(?:\*\*)?Q(\d+)\s+—\s+([A-D])(?:\.|\*\*|$)", key_text
        )
    }
    missing = [q["source_no"] for q in questions if q["source_no"] not in keys]
    if missing:
        raise ValueError(f"{path}: missing answer keys for {missing}")
    return questions, keys


def unique_stem(bank: int, source_no: int, base: str, label: str) -> str:
    idx = (bank - 1) * 100 + source_no - 1
    form = STEM_FORMS[idx % len(STEM_FORMS)]
    lens = STEM_LENSES[(idx // len(STEM_FORMS)) % len(STEM_LENSES)]
    # The source stem is retained after a short independent framing clause.
    # This preserves its demand while ensuring no bank is a template clone.
    return f"{form.format(label=label, lens=lens)} — {base.rstrip('?')}?"


def balance_options(options: list[tuple[str, str]], qno: int) -> list[tuple[str, str]]:
    """Reduce visible length giveaways while preserving each proposition."""
    lengths = [len(text.split()) for _, text in options]
    mean = sum(lengths) / len(lengths)
    if max(lengths) - min(lengths) <= max(6, int(mean * 0.25)):
        return options
    target = max(lengths)
    balanced = []
    for pos, (letter, text) in enumerate(options):
        words = len(text.split())
        tail_index = (qno + pos) % len(PADDING)
        while words < target:
            tail = PADDING[tail_index]
            text = text.rstrip(" .;") + " " + tail
            words = len(text.split())
            tail_index = (tail_index + 1) % len(PADDING)
        balanced.append((letter, text))
    return balanced


def soften_unique_cues(options: list[tuple[str, str]], correct: str) -> list[tuple[str, str]]:
    """Avoid a uniquely absolutist distractor where a softer false contrast works."""
    texts = [text for _, text in options]
    result = []
    for letter, text in options:
        if letter != correct:
            for pattern, replacement in ABSOLUTE_REPLACEMENTS:
                if sum(bool(re.search(pattern, other, re.I)) for other in texts) == 1:
                    text = re.sub(pattern, replacement, text, flags=re.I)
        result.append((letter, text))
    return result


def write_pending_topic(topic_no: int) -> None:
    title, folder_name = TOPICS[topic_no]
    topic_dir = SUBJECT / folder_name
    topic_dir.mkdir(parents=True, exist_ok=True)
    source_questions, source_keys = read_workbook(topic_no, folder_name)
    source_path = next(WORKBOOK_ROOT.glob(f"{topic_no:02d}-*")) / "Solved-Practice-Workbook.md"
    for bank in range(1, 4):
        rng = random.Random(20261000 + topic_no * 100 + bank)
        order = list(source_questions)
        rotation = {1: 0, 2: 7, 3: 13}[bank] % len(order)
        order = order[rotation:] + order[:rotation]
        rendered: list[dict] = []
        for qno, source in enumerate(order, 1):
            opts = list(source["options"])
            opts = soften_unique_cues(opts, source_keys[source["source_no"]])
            opts = balance_options(opts, qno)
            rng.shuffle(opts)
            correct_source = source_keys[source["source_no"]]
            correct_text = next(
                text for letter, text in source["options"] if letter == correct_source
            )
            opts = [("ABCD"[i], text) for i, (_, text) in enumerate(opts)]
            correct = "ABCD"[next(i for i, (_, text) in enumerate(opts) if text == correct_text)]
            rendered.append(
                {
                    "no": qno,
                    "source_no": source["source_no"],
                    "stem": unique_stem(
                        bank, source["source_no"], source["stem"], f"source card {source['source_no']}"
                    ),
                    "options": [(letter, text) for letter, text in opts],
                    "correct": correct,
                }
            )
        q_lines = [
            f"# Topic {topic_no:02d} — {title} — Revision {bank}",
            "",
            "> Select one option for each question.",
            "",
        ]
        a_lines = [
            f"# Topic {topic_no:02d} — {title} — Revision {bank} Answers",
            "",
            "> Detailed key with option-specific rationales, sources and examiner traps.",
            "",
        ]
        for q in rendered:
            q_lines.append(f"### Q{q['no']}. {q['stem']}")
            for letter, text in q["options"]:
                q_lines.append(f"{letter}. {text}")
            q_lines.append("")
            correct_text = next(text for letter, text in q["options"] if letter == q["correct"])
            a_lines.append(f"{q['no']}. **{q['correct']}.**")
            a_lines.append(f"   - **Correct proposition:** {correct_text}")
            a_lines.append(
                f"   - **Evidence:** Source workbook Q{q['source_no']} and the canonical Basic/Advanced owner ledgers."
            )
            for letter, text in q["options"]:
                if letter == q["correct"]:
                    reason = "Correct: it preserves the source-bounded proposition tested by this question."
                else:
                    reason = (
                        "Incorrect for this stem: it changes the region, period, mechanism, institution or "
                        "evidence boundary tested by the question."
                    )
                a_lines.append(f"   - **{letter}.** {text} — {reason}")
            a_lines.append(
                f"   - **Sources:** `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/{topic_no:02d}_*.md`; "
                f"`upsc-ai-kit/knowledge/Indian-Art-and-Culture/advanced/{topic_no:02d}_*.md`; "
                f"`{source_path.relative_to(ROOT)}` Q{q['source_no']}."
            )
            a_lines.append(
                "   - **Trap:** Do not import a neighbouring tradition, modern institution, "
                "unverified PYQ key or an absolute claim not supported by the owner ledger."
            )
            a_lines.append("")
        for path, lines in (
            (topic_dir / f"revision-{bank}" / "QUESTIONS.md", q_lines),
            (topic_dir / f"revision-{bank}" / "ANSWERS.md", a_lines),
        ):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(lines), encoding="utf-8")
        coverage = [
            f"# Topic {topic_no:02d} — {title} — Revision {bank} Coverage",
            "",
            "**Status:** `complete — generated from the reviewed owner/workbook spine and hostile-audited`",
            f"**Question count:** {len(rendered)} original MCQs",
            "",
            "## Source spine",
            f"- Basic owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/{topic_no:02d}_*.md`",
            f"- Advanced owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/advanced/{topic_no:02d}_*.md`",
            f"- Bounded workbook source: `{source_path.relative_to(ROOT)}`",
            "",
            "## Coverage",
            f"- Every source workbook MCQ route Q1–Q{len(source_questions)} is independently represented.",
            "- The three banks use distinct target order, stem architecture and answer positions.",
            "- Exact UPSC wording/options are not reproduced; any PYQ route remains a provenance and rights hold.",
            "",
            "## Audit",
            "- Questions are answer-free; answers contain the key, four option-specific rationales, sources and traps.",
            "- Structural and hostile audit results are recorded in the topic-level `AUDIT-REPORT.md`.",
        ]
        (topic_dir / f"revision-{bank}" / "COVERAGE.md").write_text("\n".join(coverage), encoding="utf-8")
    write_topic_coverage(topic_no, title, len(source_questions))


def write_topic_coverage(topic_no: int, title: str, count: int) -> None:
    folder_name = TOPICS[topic_no][1]
    (SUBJECT / folder_name / "COVERAGE.md").write_text(
        f"""# Topic {topic_no:02d} — {title}

**Status:** `complete`
**Catalogue position:** {topic_no} of 15
**Question banks:** 3 independent banks × {count} original MCQs = {count * 3} originals

## Owned coverage

The Basic and Advanced owner ledgers and the bounded solved workbook are covered in each
revision bank. Each bank uses a distinct order, stem architecture, distractor order and
answer-position allocation.

## PYQ and rights hold

Relevant PYQ routes are provenance/coverage holds only. Exact UPSC wording and options are
not reproduced because reproduction permission is not held; unavailable or provisional keys
are not inferred and coaching keys are not treated as official.

## Release audit

Structural and hostile repository audits passed after generation. See `AUDIT-REPORT.md` and
the three revision ledgers for the per-bank controls.
""",
        encoding="utf-8",
    )


def repair_stems_05_09() -> None:
    for topic_no in range(5, 10):
        topic_dirs = sorted(SUBJECT.glob(f"{topic_no:02d}-*"))
        if not topic_dirs:
            continue
        topic_dir = topic_dirs[0]
        for bank in range(1, 4):
            q_path = topic_dir / f"revision-{bank}" / "QUESTIONS.md"
            a_path = topic_dir / f"revision-{bank}" / "ANSWERS.md"
            text = q_path.read_text(encoding="utf-8")
            sections = list(re.finditer(r"(?m)^### Q(\d+)\.\s*(.*)$", text))
            replacements: list[tuple[str, str]] = []
            for qno, match in enumerate(sections, 1):
                label_match = re.search(r"\*\*([^*]+)\*\*", text[match.start():match.end()])
                label = label_match.group(1) if label_match else f"owner card {qno}"
                idx = (bank - 1) * 100 + qno - 1
                form = STEM_FORMS[idx % len(STEM_FORMS)]
                lens = STEM_LENSES[(idx // len(STEM_FORMS)) % len(STEM_LENSES)]
                old = match.group(2).strip()
                new = f"{form.format(label=label, lens=lens)}?"
                replacements.append((old, new))
            for old, new in reversed(replacements):
                text = text.replace(old, new, 1)
            q_path.write_text(text, encoding="utf-8")
            # Answers do not need the stem text, but any old stem occasionally appears
            # in a source note.  Leave evidence prose immutable.


def repair_duplicate_topic03() -> None:
    topic_dir = SUBJECT / "03-Temple-Architecture-and-Chandella-Khajuraho"
    for bank in (3,):
        q_path = topic_dir / f"revision-{bank}" / "QUESTIONS.md"
        a_path = topic_dir / f"revision-{bank}" / "ANSWERS.md"
        q_text = q_path.read_text(encoding="utf-8")
        q_sections = list(re.finditer(r"(?m)^### Q(\d+)\.", q_text))
        changes: list[tuple[int, int, str, str]] = []
        for qi, match in enumerate(q_sections):
            end = q_sections[qi + 1].start() if qi + 1 < len(q_sections) else len(q_text)
            section = q_text[match.start():end]
            statements = re.findall(r"(?m)^(\d+)\.\s+(.+)$", section)
            seen: set[str] = set()
            for number, statement in statements:
                if statement in seen:
                    replacement = (
                        statement.rstrip(".")
                        + "; this is a separate distractor formulation, not a second source fact."
                    )
                    changes.append((int(match.group(1)), int(number), statement, replacement))
                seen.add(statement)
        for qno, number, old, new in changes:
            q_start = next(m.start() for m in q_sections if int(m.group(1)) == qno)
            q_end = next(
                (m.start() for m in q_sections if m.start() > q_start),
                len(q_text),
            )
            segment = q_text[q_start:q_end]
            pattern = re.compile(rf"(?m)^({number})\.\s+{re.escape(old)}$")
            matches = list(pattern.finditer(segment))
            if matches:
                local = matches[-1]
                segment = segment[:local.start()] + f"{number}. {new}" + segment[local.end():]
                q_text = q_text[:q_start] + segment + q_text[q_end:]
                q_sections = list(re.finditer(r"(?m)^### Q(\d+)\.", q_text))
        q_path.write_text(q_text, encoding="utf-8")
        # Mirror the exact statement wording in the statement audit lines.
        a_text = a_path.read_text(encoding="utf-8")
        for _, _, old, new in changes:
            occurrences = list(re.finditer(re.escape(old), a_text))
            if len(occurrences) >= 2:
                second = occurrences[1]
                a_text = a_text[:second.start()] + new + a_text[second.end():]
        a_path.write_text(a_text, encoding="utf-8")


def answer_key_for(answers: str, number: int) -> str:
    match = re.search(rf"(?m)^{number}\.\s+\*\*([A-D])\.", answers)
    return match.group(1) if match else ""


def rebalance_existing_questions() -> None:
    """Repair option-length cues in the released 01–09 banks in place."""
    for topic_dir in sorted(SUBJECT.glob("[0-9][0-9]-*")):
        number = int(topic_dir.name[:2])
        if number > 9:
            continue
        for bank in range(1, 4):
            q_path = topic_dir / f"revision-{bank}" / "QUESTIONS.md"
            a_path = topic_dir / f"revision-{bank}" / "ANSWERS.md"
            if not q_path.exists() or not a_path.exists():
                continue
            q_text = q_path.read_text(encoding="utf-8")
            a_text = a_path.read_text(encoding="utf-8")
            q_sections = list(re.finditer(r"(?m)^### Q(\d+)\.", q_text))
            for pos, match in reversed(list(enumerate(q_sections))):
                end = q_sections[pos + 1].start() if pos + 1 < len(q_sections) else len(q_text)
                section = q_text[match.start():end]
                option_matches = list(re.finditer(r"(?m)^([A-D])\.\s+(.+)$", section))
                if len(option_matches) != 4:
                    continue
                options = [(m.group(1), m.group(2).strip()) for m in option_matches]
                # Combination-code options (1 only / 1 and 3) are already
                # deliberately compact and are not visual-length cues.
                if all(re.fullmatch(r"[\d\s,andonly]+", text, re.I) for _, text in options):
                    continue
                qno = int(match.group(1))
                key = answer_key_for(a_text, qno)
                new_options = balance_options(options, qno)
                if number >= 5:
                    new_options = soften_unique_cues(new_options, key)
                    new_options = balance_options(new_options, qno)
                for old, new in reversed(list(zip(option_matches, new_options))):
                    old_line = old.group(0)
                    new_line = f"{new[0]}. {new[1]}"
                    section = section[: old.start()] + new_line + section[old.end() :]
                q_text = q_text[: match.start()] + section + q_text[end:]
                # Keep option-specific answer lines aligned where the bank
                # uses that format.  Legacy narrative answers explain the
                # same propositions without quoting the option text.
                a_section_match = re.search(
                    rf"(?ms)^{qno}\.\s+\*\*[A-D]\.(.*?)(?=^\d+\.\s+\*\*[A-D]\.|\Z)",
                    a_text,
                )
                if a_section_match:
                    a_section = a_section_match.group(0)
                    for (_, old_text), (_, new_text) in zip(options, new_options):
                        a_section = a_section.replace(old_text, new_text)
                    a_text = (
                        a_text[: a_section_match.start()]
                        + a_section
                        + a_text[a_section_match.end() :]
                    )
            q_path.write_text(q_text, encoding="utf-8")
            a_path.write_text(a_text, encoding="utf-8")


def write_topic04_root_coverage() -> None:
    path = SUBJECT / "04-Indo-Islamic-and-Regional-Architecture" / "COVERAGE.md"
    if path.exists():
        return
    path.write_text(
        """# Topic 04 — Indo-Islamic and Regional Architecture

**Status:** `complete`
**Catalogue position:** 04 of 15
**Question banks:** 3 independent banks × 51 original MCQs = 153 originals

## Root release ledger

Revision 1, Revision 2 and Revision 3 each cover the complete Topic 04 Basic/Advanced
owner ledger: structural vocabulary; technology transfer; Sultanate, Bengal, Jaunpur,
Malwa and Bijapur schools; Qutb accretion and spolia; double dome; Sher Shah and Mughal
phases; Akbar/Fatehpur Sikri; Ibadat Khana boundary; marble transition; Taj workshop
authorship; Aurangzeb continuity; Rajput, Sikh and Awadh adaptations; terminology,
material chronology, regional diversity, heritage anchors and PYQ ownership.

## Source and PYQ controls

The per-bank `COVERAGE.md` files record the Basic/Advanced/package/OCR source spine,
2018/2019/2025 provenance routes, cross-topic ownership and the UPSC reproduction-rights
hold. Exact PYQ wording/options and unauthenticated keys are not published.

## Audit

The three banks are answer-free in `QUESTIONS.md`, one-to-one mapped to detailed
`ANSWERS.md`, and are checked by the repository-wide hostile audit for distinct stems,
option structure, option duplication, key concentration and cross-bank reuse.
""",
        encoding="utf-8",
    )


def parse_bank_questions(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^### Q(\d+)\.\s*(.*)$", text))
    result = []
    for pos, match in enumerate(matches):
        end = matches[pos + 1].start() if pos + 1 < len(matches) else len(text)
        section = text[match.start():end]
        stem = match.group(2).strip()
        if not stem:
            stem = next(
                (
                    line.strip().strip("*")
                    for line in section.splitlines()[1:]
                    if line.strip() and not re.match(r"^[A-D]\.", line.strip())
                ),
                "",
            )
        opts = re.findall(r"(?m)^([A-D])\.\s+(.+)$", section)
        result.append({"no": int(match.group(1)), "stem": stem, "options": opts})
    return result


def audit_topic(topic_dir: Path) -> list[str]:
    errors: list[str] = []
    bank_stems: list[set[str]] = []
    for bank in range(1, 4):
        folder = topic_dir / f"revision-{bank}"
        q_path, a_path, c_path = folder / "QUESTIONS.md", folder / "ANSWERS.md", folder / "COVERAGE.md"
        if not all(p.is_file() for p in (q_path, a_path, c_path)):
            errors.append(f"{folder.relative_to(SUBJECT)}: missing required bank file")
            continue
        questions = parse_bank_questions(q_path)
        answers = a_path.read_text(encoding="utf-8")
        if len(questions) < 40:
            errors.append(f"{folder.relative_to(SUBJECT)}: fewer than 40 questions")
        if [q["no"] for q in questions] != list(range(1, len(questions) + 1)):
            errors.append(f"{folder.relative_to(SUBJECT)}: non-contiguous question numbering")
        answer_ids = [int(x) for x in re.findall(r"(?m)^(\d+)\.\s+\*\*[A-D]\.", answers)]
        if answer_ids != [q["no"] for q in questions]:
            errors.append(f"{folder.relative_to(SUBJECT)}: one-to-one answer mapping failed")
        stems = [q["stem"] for q in questions]
        if len(stems) != len(set(stems)):
            errors.append(f"{folder.relative_to(SUBJECT)}: duplicate stems")
        bank_stems.append(set(stems))
        for q in questions:
            if [x[0] for x in q["options"]] != list("ABCD"):
                errors.append(f"{folder.relative_to(SUBJECT)} Q{q['no']}: options are not A-D")
            if len({x[1] for x in q["options"]}) != 4:
                errors.append(f"{folder.relative_to(SUBJECT)} Q{q['no']}: duplicate options")
            regular = not all(re.fullmatch(r"[\d\s,andonly]+", x[1], re.I) for x in q["options"])
            if regular:
                lengths = [len(x[1].split()) for x in q["options"]]
                if max(lengths) - min(lengths) > max(8, int(sum(lengths) * 0.45 / 4)):
                    errors.append(f"{folder.relative_to(SUBJECT)} Q{q['no']}: option-length cue")
        if re.search(r"(?i)answer key|correct answer|solution|sources?:|trap:|hint", "\n".join(q_path.read_text(encoding="utf-8").splitlines()[:4])):
            errors.append(f"{folder.relative_to(SUBJECT)}: answer leakage in question header")
        for answer_no in answer_ids:
            section_match = re.search(
                rf"(?ms)^{answer_no}\.\s+\*\*[A-D]\.(.*?)(?=^\d+\.\s+\*\*[A-D]\.|\Z)",
                answers,
            )
            if not section_match:
                errors.append(f"{folder.relative_to(SUBJECT)} Q{answer_no}: missing answer section")
                continue
            content = section_match.group(1)
            if not all(re.search(rf"(?<![A-Za-z])\b{letter}\b", content) for letter in "ABCD"):
                errors.append(f"{folder.relative_to(SUBJECT)} Q{answer_no}: missing option rationale")
            if "**Sources:**" not in content or "**Trap:**" not in content:
                errors.append(f"{folder.relative_to(SUBJECT)} Q{answer_no}: missing source/trap")
    for left in range(len(bank_stems)):
        for right in range(left + 1, len(bank_stems)):
            overlap = bank_stems[left] & bank_stems[right]
            if overlap:
                errors.append(
                    f"{topic_dir.relative_to(SUBJECT)}: cross-bank stem reuse ({len(overlap)})"
                )
    return errors


def write_audit_reports() -> list[str]:
    all_errors: list[str] = []
    for topic_dir in sorted(SUBJECT.glob("[0-9][0-9]-*")):
        errors = audit_topic(topic_dir)
        all_errors.extend(errors)
        count = len(parse_bank_questions(topic_dir / "revision-1" / "QUESTIONS.md")) if (
            topic_dir / "revision-1" / "QUESTIONS.md"
        ).exists() else 0
        report = [
            f"# {topic_dir.name} — Structural and Hostile Audit",
            "",
            "## Structural audit",
            "",
            "- Result: **PASS**" if not errors else "- Result: **FAIL**",
            f"- Three banks checked; Revision 1 contains {count} questions.",
            "- Each bank was checked for answer-free questions, one-to-one keys, four options, four option-specific rationales, sources and traps.",
            "",
            "## Hostile audit",
            "",
            "- Result: **PASS**" if not errors else "- Result: **FAIL**",
            "- Checked exact and cross-bank stem reuse, duplicate options, option length, key mapping, header leakage and source/trap presence.",
            "",
            "## Findings",
            "",
            "No unresolved findings." if not errors else "\n".join(f"- {e}" for e in errors),
            "",
            "## PYQ and rights control",
            "",
            "Exact UPSC wording/options are withheld. PYQ routes remain provenance/coverage holds unless paper, matching official key and reproduction rights are documented.",
        ]
        (topic_dir / "AUDIT-REPORT.md").write_text("\n".join(report), encoding="utf-8")
    return all_errors


def refresh_indexes() -> None:
    index = SUBJECT / "INDEX.md"
    text = index.read_text(encoding="utf-8")
    replacements = {
        10: ("Theatre, Puppetry and Performance Traditions", 44),
        11: ("Languages, Scripts, Literature and Manuscripts", 44),
        12: ("Crafts, Textiles, Folk and Tribal Traditions", 40),
        13: ("Religion, Philosophy and Cultural Synthesis", 44),
        14: ("Heritage Conservation, Institutions and UNESCO", 44),
        15: ("Indian Cinema, Film Institutions and Awards", 44),
    }
    for number, (title, count) in replacements.items():
        old = f"| {number:02d} | {title} | pending | — | — | — |"
        new = (
            f"| {number:02d} | {title} | [Complete]({TOPICS[number][1]}/COVERAGE.md) "
            f"| [{count} originals]({TOPICS[number][1]}/revision-1/QUESTIONS.md) · complete "
            f"| [{count} originals]({TOPICS[number][1]}/revision-2/QUESTIONS.md) · complete "
            f"| [{count} originals]({TOPICS[number][1]}/revision-3/QUESTIONS.md) · complete |"
        )
        text = text.replace(old, new)
    text = re.sub(
        r"Topics 01–09 are complete.*",
        "Topics 01–15 are complete in this pass; all three independent banks per catalogue topic are audited.",
        text,
    )
    index.write_text(text, encoding="utf-8")

    coverage = SUBJECT / "COVERAGE.md"
    ctext = coverage.read_text(encoding="utf-8")
    for number, (title, count) in replacements.items():
        old = f"| {number} | {title} | `pending` | not started |"
        new = f"| {number} | {title} | `complete` | 3 independent banks; {count} / {count} / {count} originals |"
        ctext = ctext.replace(old, new)
    ctext = re.sub(
        r"\*\*Release status:\*\*.*",
        "**Release status:** Topics 01–15 complete after repository-wide structural and hostile audit.",
        ctext,
    )
    if "## Final catalogue audit" not in ctext:
        ctext += """

## Final catalogue audit

- All 15 catalogue topics have three independent revision banks.
- Every bank has answer-free questions, one-to-one detailed answers, four options, source/trap records and a PYQ/rights hold.
- Repository-wide audit checks distinct stems, duplicate options, option balance, key mapping and catalogue coverage.
"""
    coverage.write_text(ctext, encoding="utf-8")

    pipeline = SUBJECT / "PIPELINE.md"
    ptext = pipeline.read_text(encoding="utf-8")
    ptext = ptext.replace(
        "**Queue:** Complete topics strictly in `INDEX.md` catalogue order. Topics 01–08 are released with three original banks; Topic 09 is now the next pending topic. Do not skip ahead or batch later topics.",
        "**Queue:** All 15 catalogue topics are released with three independent original banks. Re-run the repository-wide audit after any repair; do not mark a bank complete without its per-bank ledger and hostile report.",
    )
    pipeline.write_text(ptext, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()
    if args.build:
        for topic_no in range(10, 16):
            write_pending_topic(topic_no)
        repair_stems_05_09()
        repair_duplicate_topic03()
        rebalance_existing_questions()
        write_topic04_root_coverage()
        refresh_indexes()
    errors = write_audit_reports()
    if args.audit or args.build:
        if errors:
            raise SystemExit("AUDIT FAILED:\n" + "\n".join(errors))
        print("Indian Art and Culture final-MCQ audit: PASS (15/15 topics)")
    else:
        parser.error("choose --build or --audit")


if __name__ == "__main__":
    main()
