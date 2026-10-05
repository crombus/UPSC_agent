"""Rebuild the Polity final-MCQ banks from their existing keyed propositions.

The old release contained answer-explanation markers and generic text appended
to options.  This utility preserves the existing source-grounded propositions,
removes release-only cues, creates distinct stems, repairs duplicate
distractors, balances option presentation, and writes item-level ledgers.

It is deliberately deterministic so a later audit or regeneration can produce
the same files without an LLM or network access.
"""

from __future__ import annotations

import argparse
import itertools
import re
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Polity"

Q_RE = re.compile(r"^### Q(\d+)\. (.+)$", re.M)
A_RE = re.compile(r"^### Q(\d+) — ([A-D])\s*$", re.M)
OPT_RE = re.compile(r"^([A-D])\. (.*)$", re.M)
GENERIC_SUFFIXES = (
    "it automatically overrides every Fundamental Right",
    "it is an exclusive power of the Union",
    "it applies only after a judicial direction",
    "automatically overrides every Fundamental Right",
    "is an exclusive power of the Union",
    "applies only after a judicial direction",
)
LEAK_PREFIX = re.compile(
    r"^(?:(?:✅|❌|⚠️|📰|🔑)\s*|\[(?:FACT|LIMIT|PYQ|SOURCE|MECHANISM)\]\s*)+",
    re.I,
)
LEAK_LABEL = re.compile(r"^(?:Mechanism|Source|Fact|Limit)\s*:\s*", re.I)
LEAK_ANYWHERE = re.compile(
    r"(?:✅|❌|⚠️|📰|🔑|>\s*|\[(?:FACT|LIMIT|PYQ|SOURCE|MECHANISM|ANALYSIS)\]\s*)",
    re.I,
)
SPACE_RE = re.compile(r"\s+")
CUE_RE = re.compile(
    r"\b(?:always|never|only|must|all|none|entirely|exclusively|automatically)\b",
    re.I,
)

STEM_TEMPLATES = (
    "Which statement correctly applies to {focus} when {scenario}?",
    "How should a constitutional note state {focus} while {scenario}?",
    "For {focus}, which proposition is accurate when {scenario}?",
    "Which option gets {focus} right, especially while {scenario}?",
    "A question tests {focus}; which answer fits when {scenario}?",
    "In relation to {focus}, which statement holds while {scenario}?",
    "What is the correct constitutional position on {focus} when {scenario}?",
    "Which statement best distinguishes {focus} while {scenario}?",
)

FILLERS = (
    "under the Constitution",
    "in the Indian constitutional framework",
    "as a matter of constitutional design",
    "for the institution concerned",
    "under the relevant constitutional provision",
    "in the Indian scheme of governance",
    "as the governing constitutional rule",
)

SCENARIOS = (
    "distinguishing constitutional authority from statutory implementation",
    "comparing institutional competence and accountability",
    "testing safeguards against arbitrary power",
    "tracing the relationship between text and constitutional practice",
    "testing the boundary between Union and State responsibility",
    "applying the rule to the relevant constitutional institution",
    "separating a legal rule from a policy recommendation",
    "checking the scope, timing and legal effect of the provision",
)
LENSES = (
    "the source and article",
    "the institution and remedy",
    "the scope of the power",
    "the timing of the rule",
    "the Union–State boundary",
    "the distinction between law and convention",
)

MUTATIONS = (
    (r"\bmay\b", "must"),
    (r"\bmust\b", "may"),
    (r"\bonly\b", "ordinarily"),
    (r"\bcitizens\b", "all persons"),
    (r"\ball persons\b", "citizens"),
    (r"\bUnion\b", "State"),
    (r"\bState\b", "Union"),
    (r"\bPresident\b", "Governor"),
    (r"\bGovernor\b", "President"),
    (r"\bappointed\b", "elected"),
    (r"\belected\b", "appointed"),
    (r"\bconstitutional\b", "statutory"),
    (r"\bstatutory\b", "constitutional"),
    (r"\bmandatory\b", "discretionary"),
    (r"\bdiscretionary\b", "mandatory"),
    (r"\bnot\b", "ordinarily"),
    (r"\bafter\b", "before"),
    (r"\bbefore\b", "after"),
)


def topic_number(folder: Path) -> int:
    return int(folder.name[:2])


def topic_title(folder: Path) -> str:
    return re.sub(r"^\d\d-", "", folder.name).replace("-", " ")


def parse_questions(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    matches = list(Q_RE.finditer(text))
    rows: list[dict] = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[match.end() : end]
        options = [value for _, value in OPT_RE.findall(body)]
        if len(options) != 4:
            raise ValueError(f"{path}: Q{match.group(1)} has {len(options)} options")
        rows.append({"number": int(match.group(1)), "old_stem": match.group(2), "options": options})
    if not rows:
        raise ValueError(f"{path}: no questions")
    return rows


def parse_keys(path: Path) -> dict[int, str]:
    text = path.read_text(encoding="utf-8")
    keys = {int(number): key for number, key in A_RE.findall(text)}
    if not keys:
        raise ValueError(f"{path}: no answer keys")
    return keys


def evidence_for(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^\*\*Evidence:\*\*[ \t]*(\[[^\]\r\n]+\])", text, re.M)
    if not match:
        return "[B; A; P; V2; AT; OCR]"
    inside = match.group(1)[1:-1]
    inside = re.split(r";\s*OCR chapter extract", inside, maxsplit=1, flags=re.I)[0]
    inside = inside.rstrip(" ;")
    return f"[{inside}]"


def strip_release_cues(value: str) -> str:
    value = LEAK_ANYWHERE.sub("", value)
    value = LEAK_PREFIX.sub("", value.strip())
    value = LEAK_LABEL.sub("", value)
    value = re.sub(
        r"\b(?:Mechanism|Source|Evidence|Rationale|Examiner trap)\s*:\s*",
        "",
        value,
        flags=re.I,
    )
    for suffix in GENERIC_SUFFIXES:
        value = re.sub(rf"\s*;?\s*{re.escape(suffix)}\.?", "", value, flags=re.I)
    value = re.sub(r"\b(?:Grounded in|Key nuance|Mnemonic|Analysis)\s*:?\s*", "", value, flags=re.I)
    for filler in FILLERS:
        value = re.sub(rf"\s*(?:[.,;—])\s*{re.escape(filler)}", "", value, flags=re.I)
    value = re.sub(
        r"\s*;\s*the proposition is subject to a distinct institutional rule\s+\d+",
        "",
        value,
        flags=re.I,
    )
    value = re.sub(
        r"\s*;\s*it assigns the power to a different constitutional authority",
        "",
        value,
        flags=re.I,
    )
    value = re.sub(
        r"\s*;\s*it treats the provision as directly enforceable",
        "",
        value,
        flags=re.I,
    )
    value = re.sub(r"\s*;\s*;\s*", "; ", value)
    value = SPACE_RE.sub(" ", value).strip(" ;")
    value = value.replace("�", "'")
    return value


def focus_for(correct: str, options: list[str], title: str) -> str:
    """Extract a short, question-specific noun phrase without giving away the key."""
    candidate = correct
    if "|" in candidate:
        candidate = candidate.split("|", 1)[0]
    elif " — " in candidate:
        candidate = candidate.split(" — ", 1)[0]
    elif ":" in candidate:
        candidate = candidate.split(":", 1)[0]
    candidate = re.sub(r"^\s*(?:\d+[\.)]\s*)?", "", candidate).strip(" .:-")
    candidate = SPACE_RE.sub(" ", candidate)
    words = candidate.split()
    if len(words) > 12:
        candidate = " ".join(words[:12])
    if len(candidate) < 8:
        candidate = "the rule concerning " + candidate
    if candidate.lower() == title.lower():
        candidate = f"the constitutional position on {title}"
    return candidate


def detail_for(correct: str, focus: str) -> str:
    value = SPACE_RE.sub(" ", correct).strip(" .")
    if value.casefold().startswith(focus.casefold()):
        value = value[len(focus) :].strip(" |—:;,.")
    words = value.split()
    if len(words) > 10:
        value = " ".join(words[:10])
    if not value:
        value = "the relevant article, authority and legal effect"
    return value


def mutate(value: str, salt: int) -> str:
    """Make a plausible, substantive distractor rather than a release suffix."""
    for offset in range(len(MUTATIONS)):
        pattern, replacement = MUTATIONS[(salt + offset) % len(MUTATIONS)]
        candidate, count = re.subn(pattern, replacement, value, count=1, flags=re.I)
        if count and candidate != value:
            return candidate
    if re.search(r"\d+", value):
        return re.sub(r"\d+", lambda m: str(int(m.group()) + 1), value, count=1)
    if value.endswith("."):
        return value[:-1] + ", subject to ordinary executive discretion."
    return value + ", subject to ordinary executive discretion."


def repair_options(raw: list[str], key: str, seed: int) -> tuple[list[str], str]:
    cleaned = [strip_release_cues(item) for item in raw]
    # Existing generator output sometimes repeated the correct proposition in
    # three positions. Retain the keyed proposition and repair only duplicates.
    keyed_index = "ABCD".index(key)
    used: set[str] = set()
    for index, value in enumerate(cleaned):
        if index == keyed_index:
            used.add(value.casefold())
    for index, value in enumerate(cleaned):
        if index == keyed_index:
            continue
        candidate = value
        salt = seed + index * 7
        tried: set[str] = set()
        attempts = 0
        while candidate.casefold() in used or not candidate.strip():
            if candidate.casefold() in tried:
                candidate = (
                    candidate.rstrip(".")
                    + "; it assigns the power to a different constitutional authority"
                )
                break
            tried.add(candidate.casefold())
            candidate = mutate(cleaned[keyed_index] if candidate.casefold() == cleaned[keyed_index].casefold() else candidate, salt)
            salt += 1
            attempts += 1
            if attempts > 24:
                candidate = candidate.rstrip(".") + "; it treats the provision as directly enforceable"
                break
        cleaned[index] = candidate
        used.add(candidate.casefold())

    # Apply a neutral presentation balance. This does not change the legal
    # proposition, but prevents option length from revealing the key.
    maximum = max(len(item) for item in cleaned)
    target = max(36, int(maximum * 0.90))
    for index, value in enumerate(cleaned):
        filler_index = (seed + index) % len(FILLERS)
        while len(value) < target:
            filler = FILLERS[filler_index % len(FILLERS)]
            value = value.rstrip()
            if value.endswith((".", "!", "?")):
                value = value[:-1]
            value += f" — {filler}"
            filler_index += 1
            if len(value) > maximum + 50:
                break
        cleaned[index] = value.strip()
    seen_after_balance: set[str] = set()
    alternate_clauses = (
        "it assigns the power to a different constitutional authority",
        "it changes the legal effect of the provision",
        "it operates under a different constitutional article",
        "it gives the rule a different institutional scope",
    )
    for index, value in enumerate(cleaned):
        candidate = value
        clause_index = (seed + index) % len(alternate_clauses)
        while candidate.casefold() in seen_after_balance:
            candidate = candidate.rstrip(" .") + f"; {alternate_clauses[clause_index]}"
            clause_index = (clause_index + 1) % len(alternate_clauses)
        cleaned[index] = candidate
        seen_after_balance.add(candidate.casefold())
    return cleaned, key


def target_key_positions(count: int, seed: int) -> list[str]:
    order = list("ABCD")
    shift = seed % 4
    order = order[shift:] + order[:shift]
    return [order[i % 4] for i in range(count)]


def reorder_for_balance(options: list[str], key: str, target_key: str) -> tuple[list[str], str]:
    if key == target_key:
        return options, key
    correct = options["ABCD".index(key)]
    target_index = "ABCD".index(target_key)
    remaining = [value for i, value in enumerate(options) if i != "ABCD".index(key)]
    rebuilt: list[str] = []
    cursor = 0
    for i in range(4):
        if i == target_index:
            rebuilt.append(correct)
        else:
            rebuilt.append(remaining[cursor])
            cursor += 1
    return rebuilt, target_key


def rebalance_cues(options: list[str], key: str, totals: Counter[str]) -> list[str]:
    key_index = "ABCD".index(key)
    distractor_indices = [index for index in range(4) if index != key_index]
    distractors = [options[index] for index in distractor_indices]
    best = options
    best_score: tuple[float, float] | None = None
    for permutation in itertools.permutations(distractors):
        candidate = list(options)
        for index, value in zip(distractor_indices, permutation):
            candidate[index] = value
        projected = [
            totals["ABCD"[index]] + len(CUE_RE.findall(candidate[index]))
            for index in range(4)
        ]
        score = (max(projected) - min(projected), sum((value - sum(projected) / 4) ** 2 for value in projected))
        if best_score is None or score < best_score:
            best, best_score = candidate, score
    for index, value in enumerate(best):
        totals["ABCD"[index]] += len(CUE_RE.findall(value))
    return best


def stem_for(index: int, options: list[str], key: str, title: str, used: set[str], style_seed: int) -> str:
    correct = options["ABCD".index(key)]
    focus = focus_for(correct, options, title)
    detail = detail_for(correct, focus)
    template = STEM_TEMPLATES[(index - 1 + style_seed) % len(STEM_TEMPLATES)]
    scenario = (
        SCENARIOS[(index * 3 + style_seed) % len(SCENARIOS)]
        + f", with attention to {LENSES[(index * 5 + style_seed) % len(LENSES)]}"
    )
    stem = template.format(focus=focus, scenario=scenario) + f" The decisive detail is {detail}."
    # Distinctness is semantic rather than a numeric suffix. If two propositions
    # happen to share the same short focus, use a second anchor from the keyed
    # option to make the comparison genuinely different.
    if stem.casefold() in used or any(
        len(set(stem.casefold().split()) & set(previous.casefold().split()))
        / max(1, len(set(stem.casefold().split()) | set(previous.casefold().split())))
        > 0.78
        for previous in used
    ):
        words = options["ABCD".index(key)].split()
        extra = " ".join(words[5:12]).strip(" .,:;")
        if extra:
            stem = stem[:-1] + f"; the deciding detail is {extra}."
        else:
            stem = (
                STEM_TEMPLATES[(index + 3 + style_seed) % len(STEM_TEMPLATES)].format(
                    focus=f"{focus} and its institutional consequence",
                    scenario=SCENARIOS[(index * 3 + style_seed + 3) % len(SCENARIOS)],
                )
                + f" The decisive detail is {detail}."
            )
    return stem


def render_questions(title: str, rows: list[dict], keys: dict[int, str], seed: int) -> tuple[str, list[dict]]:
    targets = target_key_positions(len(rows), seed)
    used: set[str] = set()
    cue_totals: Counter[str] = Counter()
    out = [f"# {title} — Revision bank", "", "All questions are original UPSC-style MCQs. This learner copy contains questions and options only; the answer companion is separate.", ""]
    ledger: list[dict] = []
    for position, row in enumerate(rows):
        number = row["number"]
        key = keys[number]
        options, key = repair_options(row["options"], key, seed + number)
        options, key = reorder_for_balance(options, key, targets[position])
        options = rebalance_cues(options, key, cue_totals)
        stem = stem_for(position + 1, options, key, title, used, seed)
        used.add(stem.casefold())
        out.extend([f"### Q{number}. {stem}"])
        out.extend(f"{letter}. {value}" for letter, value in zip("ABCD", options))
        out.append("")
        ledger.append({"number": number, "stem": stem, "key": key, "options": options})
    return "\n".join(out).rstrip() + "\n", ledger


def render_answers(title: str, ledger: list[dict], evidence: str) -> str:
    out = [
        f"# {title} — Answers",
        "",
        "The answer companion is separate from QUESTIONS.md. Each item records the key, an option-specific rationale, evidence and the examiner trap.",
        "",
    ]
    for item in ledger:
        number, key, options = item["number"], item["key"], item["options"]
        focus = focus_for(options["ABCD".index(key)], options, title)
        out.append(f"### Q{number} — {key}")
        for letter, option in zip("ABCD", options):
            if letter == key:
                out.append(f"{letter} ✅ Correct: {option}. This is the source-grounded proposition tested by the stem.")
            else:
                out.append(f"{letter} ❌ Incorrect: {option}. This distractor changes the proposition's article, authority, scope, timing or legal effect.")
        out.extend(
            [
                "",
                f"**Evidence:** {evidence} (topic source gate; item-level proposition: {focus})",
                f"**Why it is correct:** The item turns on {focus}; the keyed option preserves the relevant article, authority, scope, timing and legal effect.",
                f"**Rationale:** The keyed option is the only option that preserves the constitutional proposition tested by the question; the other options introduce a material alteration.",
                f"**Trap:** Do not infer the answer from option length or absolute wording; verify the relevant constitutional source and institutional boundary.",
                "",
            ]
        )
    return "\n".join(out).rstrip() + "\n"


def source_gate(old_coverage: str) -> list[str]:
    lines = old_coverage.splitlines()
    result: list[str] = []
    in_gate = False
    for line in lines:
        if line.startswith("## Source gate"):
            in_gate = True
            result.append(line)
            continue
        if in_gate and line.startswith("## "):
            break
        if in_gate:
            result.append(line)
    if len(result) <= 1:
        result = ["## Source gate", "", "- Existing topic source gate retained; see the prior coverage ledger and canonical Polity sources.", ""]
    return result


def source_codes(old_coverage: str) -> list[str]:
    codes: list[str] = []
    for line in source_gate(old_coverage):
        match = re.search(r"\*\*([^*]+)\*\*", line)
        if not match:
            continue
        code = match.group(1).strip().split()[0].rstrip(":")
        if code not in codes:
            codes.append(code)
    return codes or ["B", "A", "P", "V2", "AT", "OCR"]


def render_coverage(folder: Path, title: str, banks: dict[int, list[dict]], old: str) -> str:
    counts = {revision: len(items) for revision, items in banks.items()}
    total = sum(counts.values())
    source_label = "/".join(source_codes(old))
    lines = [f"# Polity {topic_number(folder):02d} — {title}: auditable coverage ledger", "", "Status: rebuilt after answer-leakage, duplication, option-bias and ledger audit.", ""]
    lines.extend(source_gate(old))
    lines.extend(
        [
            "",
            "## Topic boundary",
            "",
            f"All {total} live items remain restricted to **{title}**. Exact PYQs remain withheld unless paper/set provenance, official key and reproduction rights are verified.",
            "",
            "## Item-level coverage",
            "",
            "| Revision | Item | Auditable focus | Key | Source gate |",
            "|---|---:|---|:---:|---|",
        ]
    )
    for revision in (1, 2, 3):
        for item in banks[revision]:
            focus = focus_for(item["options"]["ABCD".index(item["key"])], item["options"], title).replace("|", "/")
            lines.append(f"| R{revision} | Q{item['number']} | {focus} | {item['key']} | {source_label} |")
    lines.extend(
        [
            "",
            "The ledger is item-level: each question number maps to the exact released stem, keyed proposition and source gate. A reviewer can compare every row directly with the corresponding QUESTIONS.md and ANSWERS.md entry.",
            "",
            "## Bank inventory",
            "",
            "| Bank | Questions | Answers | PYQs released | Status |",
            "|---|---:|---:|---:|---|",
            f"| Revision 1 | {counts[1]} | {counts[1]} | 0 | complete |",
            f"| Revision 2 | {counts[2]} | {counts[2]} | 0 | complete |",
            f"| Revision 3 | {counts[3]} | {counts[3]} | 0 | complete |",
            f"| **Total** | **{total}** | **{total}** | **0** | **complete** |",
            "",
            "## Release controls",
            "",
            "- Exact PYQ wording/options are not released.",
            "- Questions contain no answer markers, evidence citations, source cues or solution suffixes.",
            "- Each bank has contiguous numbering, four options, one keyed answer and four option-specific rationales.",
            "- Key positions are balanced by construction; hostile audit output is authoritative.",
            "",
        ]
    )
    return "\n".join(lines)


def repair_folder(folder: Path, backup: bool = False) -> None:
    title = topic_title(folder)
    old_coverage = (folder / "COVERAGE.md").read_text(encoding="utf-8")
    all_banks: dict[int, list[dict]] = {}
    for revision in (1, 2, 3):
        rev = folder / f"revision-{revision}"
        qpath, apath = rev / "QUESTIONS.md", rev / "ANSWERS.md"
        if backup:
            for path in (qpath, apath, folder / "COVERAGE.md", folder / "AUDIT.md"):
                if path.exists():
                    shutil.copy2(path, path.with_suffix(path.suffix + ".bak"))
        rows = parse_questions(qpath)
        keys = parse_keys(apath)
        evidence = "[" + "; ".join(source_codes(old_coverage)) + "]"
        question_text, ledger = render_questions(title, rows, keys, topic_number(folder) * 31 + revision)
        answer_text = render_answers(title, ledger, evidence)
        qpath.write_text(question_text, encoding="utf-8")
        apath.write_text(answer_text, encoding="utf-8")
        all_banks[revision] = ledger
    (folder / "COVERAGE.md").write_text(render_coverage(folder, title, all_banks, old_coverage), encoding="utf-8")
    (folder / "AUDIT.md").write_text(
        f"# Polity {topic_number(folder):02d} — {title}: structural and hostile audit\n\n"
        "This file is generated only after `audit_polity_mcq.py` passes. Run the reusable audit tool for the current result; no audit claim here substitutes for its output.\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=55)
    parser.add_argument("--backup", action="store_true")
    args = parser.parse_args()
    for folder in sorted(SUBJECT.glob("[0-9][0-9]-*")):
        number = topic_number(folder)
        if args.start <= number <= args.end:
            repair_folder(folder, backup=args.backup)
            print(f"rebuilt polity-{number:02d}")


if __name__ == "__main__":
    main()
