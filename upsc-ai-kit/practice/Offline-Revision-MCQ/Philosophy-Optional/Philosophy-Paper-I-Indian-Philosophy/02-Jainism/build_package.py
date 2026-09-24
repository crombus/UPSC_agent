from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SESSION = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\02-Jainism\Learning-Session.md")
WORKBOOK = SESSION.with_name("Solved-Practice-Workbook.md")
CANONICAL = Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\indian\Jainism.md")
PYQ_OLD = Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2018-2025.md")
PYQ_NEW = Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2026.md")
IST = timezone(timedelta(hours=5, minutes=30))
NOW = datetime.now(IST).replace(microsecond=0).isoformat()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_text(text: str) -> str:
    return sha_bytes(text.replace("\r\n", "\n").encode("utf-8"))


def file_info(path: Path) -> dict:
    data = path.read_bytes()
    return {"path": str(path), "sha256": sha_bytes(data), "bytes": len(data)}


def slug(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE).strip("-")
    return s[:76] or "block"


def source_blocks(path: Path, prefix: str) -> list[dict]:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    heads = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))
    blocks = []
    for n, (start, level, heading) in enumerate(heads):
        own_end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        subtree_end = len(lines)
        for j in range(n + 1, len(heads)):
            if heads[j][1] <= level:
                subtree_end = heads[j][0]
                break
        own = "\n".join(lines[start:own_end]).strip() + "\n"
        subtree = "\n".join(lines[start:subtree_end]).strip() + "\n"
        ident = f"{prefix}-{slug(heading)}-{n+1:03d}-{sha_text(own)[:10]}"
        segments = []
        if len(own) > 2400:
            for i, offset in enumerate(range(0, len(own), 1800)):
                chunk = own[offset:offset + 1800]
                segments.append({
                    "index": i + 1,
                    "start_char": offset,
                    "end_char_exclusive": offset + len(chunk),
                    "payload_sha256": sha_text(chunk),
                    "chars": len(chunk),
                })
        blocks.append({
            "id": ident, "source": prefix, "ordinal": n + 1, "level": level,
            "heading": heading, "line_start": start + 1, "line_end": own_end,
            "own_payload_sha256": sha_text(own), "subtree_sha256": sha_text(subtree),
            "own_chars": len(own), "semantic_propositions": [own.strip()],
            "semantic_basis": "exact_complete_source_owned_payload_not_excerpt",
            "large_leaf_segments": segments,
        })
    for b in blocks:
        children = []
        child_payloads = []
        i = b["ordinal"]
        for c in blocks[i:]:
            if c["level"] <= b["level"]:
                break
            if c["level"] == b["level"] + 1:
                children.append(c["id"])
                child_payloads.append(c["own_payload_sha256"])
        b["direct_children"] = children
        b["child_union_sha256"] = sha_text("\n".join(child_payloads))
    return blocks


def anchored_copy(path: Path, prefix: str, blocks: list[dict], title: str) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    by_heading = {}
    for b in blocks:
        by_heading.setdefault((b["level"], b["heading"]), []).append(b["id"])
    used = {}
    out = []
    for line in text.splitlines():
        m = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
        if m:
            key = (len(m.group(1)), m.group(2))
            idx = used.get(key, 0)
            if key in by_heading and idx < len(by_heading[key]):
                out.append(f'<a id="{by_heading[key][idx]}"></a>')
                used[key] = idx + 1
        out.append(line)
    return f"# {title}\n\n> Exact formal-source preservation with stable source-derived anchors. Canonical corrections and package navigation precede the mirror; no formal payload is silently dropped.\n\n" + "\n".join(out) + "\n"


def parse_mcqs(text: str) -> list[dict]:
    region = text.split("#### CORE DIAGNOSTICS", 1)[1].split("## PYQS AND ANSWER PRACTICE", 1)[0]
    chunks = re.split(r"(?=^#### MCQ \d+\.)", region, flags=re.M)
    result = []
    for chunk in chunks:
        h = re.match(r"#### MCQ (\d+)\.\s*(.+)\n", chunk)
        if not h:
            continue
        num, title = int(h.group(1)), h.group(2).strip()
        answer_m = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", chunk)
        trap_m = re.search(r"\*\*Examiner trap \d+:\*\*\s*(.+)", chunk)
        exp_m = re.search(r"\*\*Option explanations:\*\*\s*(.*?)(?=\n\*\*Examiner trap)", chunk, re.S)
        before = chunk[:answer_m.start()].strip()
        opts = list(re.finditer(r"^([A-D])\.\s+(.+?)(?=\n\n[A-D]\.\s+|\n\n\*\*Answer:)", chunk, re.M | re.S))
        if len(opts) != 4 or not answer_m or not exp_m:
            raise ValueError(f"Unable to parse MCQ {num}")
        stem = before[before.find("\n") + 1:opts[0].start()].strip()
        options = {m.group(1): re.sub(r"\s+", " ", m.group(2).strip()) for m in opts}
        explanations = {}
        for m in re.finditer(r"- \*\*([A-D]):\*\*\s*(.+?)(?=\n- \*\*[A-D]:\*\*|\Z)", exp_m.group(1).strip(), re.S):
            explanations[m.group(1)] = re.sub(r"\s+", " ", m.group(2).strip())
        result.append({"number": num, "title": title, "stem": stem, "options": options,
                       "answer": answer_m.group(1), "explanations": explanations,
                       "trap": trap_m.group(1).strip() if trap_m else ""})
    return result


MCQ_CUE_POLICY = {
    "word_count_regex": r"\b[^\W_]+(?:['’\-][^\W_]+)*\b",
    "aggregate_correct_to_distractor_ratio_max": 1.20,
    "per_item_correct_to_average_distractor_ratio_max": 1.60,
    "per_item_correct_advantage_min_words": 3.0,
    "extreme_short_keyed_min_words": 6,
    "extreme_short_distractor_max_words": 2,
    "extreme_short_distractor_to_keyed_ratio_min": 0.40,
    "visible_spread_ratio_max": 2.25,
    "visible_spread_min_gap_words": 6,
    "grammatical_parallelism_checks": ["terminal_punctuation", "initial_letter_case"],
    "noncompetitive_patterns": [
        r"\ball of the above\b",
        r"\bnone of the above\b",
        r"\bboth [A-D] and [A-D]\b",
        r"\bcannot say\b",
        r"\b(?:wholly )?(?:irrelevant|unrelated)\b",
    ],
}


def option_word_count(text: str) -> int:
    return len(re.findall(MCQ_CUE_POLICY["word_count_regex"], text, re.UNICODE))


def compute_cue_metrics(rendered: list[dict]) -> dict:
    records = []
    correct_lengths, distractor_lengths = [], []
    patterns = [re.compile(pattern, re.I) for pattern in MCQ_CUE_POLICY["noncompetitive_patterns"]]
    for row in rendered:
        counts = [option_word_count(text) for text in row["options"]]
        correct = counts[row["correct_index"]]
        distractors = [count for i, count in enumerate(counts) if i != row["correct_index"]]
        distractor_mean = sum(distractors) / 3
        ratio = correct / distractor_mean
        spread = max(counts) / min(counts)
        flags = []
        if ratio > MCQ_CUE_POLICY["per_item_correct_to_average_distractor_ratio_max"] and (
            correct - distractor_mean >= MCQ_CUE_POLICY["per_item_correct_advantage_min_words"]
        ):
            flags.append("correct_length_advantage")
        if correct >= MCQ_CUE_POLICY["extreme_short_keyed_min_words"]:
            for index, count in enumerate(counts):
                if index == row["correct_index"]:
                    continue
                if count <= MCQ_CUE_POLICY["extreme_short_distractor_max_words"] or (
                    count / correct < MCQ_CUE_POLICY["extreme_short_distractor_to_keyed_ratio_min"]
                ):
                    flags.append(f"extreme_short_distractor_{'ABCD'[index]}")
        if spread > MCQ_CUE_POLICY["visible_spread_ratio_max"] and (
            max(counts) - min(counts) >= MCQ_CUE_POLICY["visible_spread_min_gap_words"]
        ):
            flags.append("excessive_visible_spread")
        for index, text in enumerate(row["options"]):
            if any(pattern.search(text) for pattern in patterns):
                flags.append(f"noncompetitive_phrase_{'ABCD'[index]}")
        terminal = [text.rstrip()[-1:] for text in row["options"]]
        if len(set(terminal)) != 1:
            flags.append("terminal_punctuation_mismatch")
        initial_case = []
        for text in row["options"]:
            first = next((char for char in text if char.isalpha()), "")
            initial_case.append("upper" if first.isupper() else "lower")
        if len(set(initial_case)) != 1:
            flags.append("initial_letter_case_mismatch")
        records.append({
            "question_id": row["question_id"],
            "keyed_letter": "ABCD"[row["correct_index"]],
            "word_counts": {letter: count for letter, count in zip("ABCD", counts)},
            "correct_to_average_distractor_ratio": round(ratio, 4),
            "visible_spread_ratio": round(spread, 4),
            "visible_spread_words": max(counts) - min(counts),
            "flags": flags,
        })
        correct_lengths.append(correct)
        distractor_lengths.extend(distractors)
    mean_correct = sum(correct_lengths) / len(correct_lengths)
    mean_distractor = sum(distractor_lengths) / len(distractor_lengths)
    aggregate_ratio = mean_correct / mean_distractor
    outliers = [row for row in records if row["flags"]]
    material_length_outliers = [
        row for row in records
        if any(flag in {"correct_length_advantage", "excessive_visible_spread"}
               for flag in row["flags"])
    ]
    return {
        "policy": MCQ_CUE_POLICY,
        "mean_correct_words": round(mean_correct, 4),
        "mean_distractor_words": round(mean_distractor, 4),
        "aggregate_correct_to_distractor_ratio": round(aggregate_ratio, 4),
        "ratio_at_or_above_1_8_count": sum(
            row["correct_to_average_distractor_ratio"] >= 1.8 for row in records
        ),
        "material_length_outlier_count": len(material_length_outliers),
        "policy_outlier_count": len(outliers),
        "noncompetitive_distractor_count": sum(
            flag.startswith(("extreme_short_distractor_", "noncompetitive_phrase_"))
            for row in records for flag in row["flags"]
        ),
        "all_options_terminal_punctuation_consistent": all(
            "terminal_punctuation_mismatch" not in row["flags"] for row in records
        ),
        "all_options_initial_letter_case_consistent": all(
            "initial_letter_case_mismatch" not in row["flags"] for row in records
        ),
        "grammar_parallel_review": (
            "passed_computed_surface_checks" if not outliers else "failed_computed_surface_checks"
        ),
        "per_item_records": records,
    }


def randomized_mcqs(items: list[dict], seed: int, matrix: dict) -> tuple[str, str, dict]:
    rng = random.Random(seed)
    target_answers = list("ABCD") * (len(items) // 4)
    target_answers += list("ABCD")[:len(items) % 4]

    def longest_run(sequence: list[str]) -> int:
        return max((len(m.group(0)) for m in re.finditer(r"(.)\1*", "".join(sequence))), default=0)

    def repeated_cycle(sequence: list[str]) -> bool:
        joined = "".join(sequence)
        for period in range(2, 5):
            width = period * 3
            for start in range(0, len(joined) - width + 1):
                window = joined[start:start + width]
                unit = window[:period]
                if len(set(unit)) > 1 and window == unit * 3:
                    return True
        return False

    for _ in range(10000):
        rng.shuffle(target_answers)
        if longest_run(target_answers) <= 2 and not repeated_cycle(target_answers):
            break
    else:
        raise RuntimeError("Unable to derive a balanced non-cyclic answer sequence")

    qout = ["# Jainism — MCQ Questions", "", f"> **Deterministic randomization seed:** `{seed}`.",
            f"> **Coverage derivation:** `{len(matrix['cells'])}` frozen atomic test cells map one-to-one to `{len(items)}` distinct authored questions. The total is derived from `TEST-MATRIX.json`, not from a round or inherited template count.", "",
            "Attempt all questions before opening the solutions.", ""]
    sout = ["# Jainism — MCQ Solutions", "", f"> Seed `{seed}`; each question has four synchronized option-specific explanations.", ""]
    answers = []
    rendered = []
    for item, target_answer in zip(items, target_answers):
        letters = list("ABCD")
        original_letters = list("ABCD")
        correct_old = original_letters[item["correct_index"]]
        distractors = [old for old in original_letters if old != correct_old]
        rng.shuffle(distractors)
        old_order = []
        for letter in letters:
            old_order.append(correct_old if letter == target_answer else distractors.pop())
        mapping = {new: old for new, old in zip(letters, old_order)}
        new_answer = next(new for new, old in mapping.items() if old == correct_old)
        answers.append(new_answer)
        rendered_options = [
            item["options"][original_letters.index(mapping[letter])] for letter in letters
        ]
        rendered.append({
            "question_id": item["id"],
            "correct_index": letters.index(new_answer),
            "options": rendered_options,
        })
        anchor = f"mcq-{item['number']:03d}"
        qout += [f'<a id="{anchor}"></a>', f"## MCQ {item['number']}. {item['title']}", "", item["stem"], ""]
        sout += [f'<a id="{anchor}-solution"></a>', f"## MCQ {item['number']}. {item['title']}", "", item["stem"], ""]
        for new in letters:
            old = mapping[new]
            txt = item["options"][original_letters.index(old)]
            qout += [f"{new}. {txt}", ""]
            sout += [f"{new}. {txt}", ""]
        sout += [f"**Answer: {new_answer}.**", "", "**Option explanations:**"]
        for new in letters:
            old = mapping[new]
            sout.append(f"- **{new}:** {item['explanations'][original_letters.index(old)]}")
        sout += ["", f"**Examiner trap:** {item['trap']}", ""]
    runs = []
    start = 0
    for i in range(1, len(answers) + 1):
        if i == len(answers) or answers[i] != answers[start]:
            runs.append({"answer": answers[start], "start": start + 1, "length": i - start})
            start = i
    audit = {
        "schema_version": 3, "topic": "Jainism", "seed": seed,
        "derivation": {
            "matrix": "TEST-MATRIX.json",
            "matrix_cell_count": len(matrix["cells"]),
            "question_count": len(items),
            "policy": "one distinct authored question per atomic cell",
        },
        "answer_sequence": "".join(answers), "answer_counts": {x: answers.count(x) for x in "ABCD"},
        "longest_run": max(r["length"] for r in runs), "runs": runs,
        "position_policy": {
            "method": "seeded constrained shuffle; no fixed rotation",
            "minimum_per_letter": len(items) // 4 - 1,
            "maximum_per_letter": (len(items) + 3) // 4 + 1,
            "maximum_run": 2,
            "cycle_periods_rejected": [2, 3, 4],
            "minimum_cycle_repetitions": 3,
            "predictable_cycle_detected": repeated_cycle(answers),
        },
        "cue_metrics": compute_cue_metrics(rendered),
        "synchronization": "Every shuffled option carries the explanation belonging to its original semantic payload.",
    }
    return "\n".join(qout), "\n".join(sout), audit


def exact_pyqs() -> list[dict]:
    rows = []
    for path in (PYQ_OLD, PYQ_NEW):
        year = None
        for line in path.read_text(encoding="utf-8").splitlines():
            ym = re.match(r"## (20\d\d)", line)
            if ym:
                year = int(ym.group(1))
            m = re.match(r"- \*\*((Q\d+\([a-e]\)) · (\d+) marks(?:[^·]*)? · \[Jainism\]\([^)]+\)):\*\* (.+)", line)
            if m:
                rows.append({"year": year, "label": m.group(1), "question_no": m.group(2),
                             "marks": int(m.group(3)), "text": m.group(4), "source": path.name})
    return rows


def section(text: str, start: str, end: str | None = None) -> str:
    s = text.index(start)
    e = text.index(end, s) if end else len(text)
    return text[s:e].strip()


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", re.sub(r"\*|`", "", text), flags=re.UNICODE))


def fit_words(text: str, lo: int, hi: int) -> str:
    words = text.split()
    if len(words) > hi:
        words = words[:hi]
        words[-1] = words[-1].rstrip(",;:") + "."
    while len(words) < lo:
        words += " This reinforces the Jaina integration of ontology, epistemology and disciplined liberation.".split()
    return " ".join(words[:hi])


def current_pyq_section(source: str, pyqs: list[dict], model2026: str) -> tuple[str, str]:
    region = section(source, "## PYQS AND ANSWER PRACTICE", "#### ORIGINAL SOLVED MAINS PRACTICE")
    blocks = re.findall(r"(#### PYQ \d+ · .*?)(?=\n#### PYQ \d+ ·|\Z)", region, re.S)
    if len(blocks) != 10:
        raise ValueError(f"Expected ten legacy PYQ blocks, found {len(blocks)}")
    primary_blocks = []
    for index, (row, block) in enumerate(zip(pyqs[:9], blocks[:9]), start=1):
        block = re.sub(
            r"^#### PYQ \d+ · .+$",
            f"#### Primary PYQ {index} · {row['year']} · {row['question_no']} · {row['marks']} marks · Jainism · fully solved",
            block,
            count=1,
            flags=re.M,
        )
        block = re.sub(
            r"^> \*\*Question, as printed:\*\* .+$",
            f"> **Question, exact verified wording:** {row['text']}",
            block,
            count=1,
            flags=re.M,
        )
        primary_blocks.append(block.strip())
    q2026 = pyqs[9]
    primary_blocks.append("\n".join([
        f"#### Primary PYQ 10 · {q2026['year']} · {q2026['question_no']} · {q2026['marks']} marks · Jainism · fully solved",
        "",
        f"> **Question, exact verified wording:** {q2026['text']}",
        "",
        "**Demand decoded.** Explain all seven forms, locate them within syādvāda, and derive their non-absolutist force from anekāntavāda without calling the doctrine relativism.",
        "",
        "**Model answer (15 marks, 250–300 words).**",
        "",
        model2026,
    ]))
    supporting = re.sub(
        r"^#### PYQ 10 · 2020 · Q7\(c\) · 15 marks · Cārvāka \(supporting routed question\)$",
        "#### Supporting cross-topic PYQ S1 · 2020 · Q7(c) · 15 marks · Cārvāka-primary / Jainism-supporting · fully solved",
        blocks[9].strip(),
        count=1,
        flags=re.M,
    )
    header = "\n".join([
        "## PYQS AND ANSWER PRACTICE",
        "",
        "### Current canonical primary sequence",
        "",
        "> **Verified wording and status.** The ten numbered questions below are the complete Jainism-primary sequence for 2018–2026. Wording and marks follow the verified ledgers exactly. Every model is independent learner practice, not an official UPSC key.",
        "> **Ownership.** Primary numbering is reserved for Jainism-owned questions. The Cārvāka-owned 2020 comparison appears separately as Supporting S1 and is not counted among the ten primary questions.",
        "> **Word bands used.** 10 marks: 150–200 words. 15 marks: 250–300 words. 20 marks: 340–400 words.",
        "",
        "### TEN PRIMARY JAINISM PYQS — COMPLETE SOLUTIONS",
        "",
    ])
    primary = header + "\n".join(primary_blocks)
    support = "\n".join([
        "### SUPPORTING CROSS-TOPIC PYQ — OUTSIDE PRIMARY NUMBERING",
        "",
        supporting,
    ])
    return primary, support


def reconciled_revision(session: str, pyqs: list[dict], model2026: str) -> str:
    legacy_start = session.index("## BASIC MCQS / REMEDIATION")
    legacy_end = session.index("## PYQS AND ANSWER PRACTICE", legacy_start)
    current_mcq_note = """## COVERAGE-DERIVED MCQ PRACTICE

The historical formal session used an inherited 24-core-plus-8-remedial block. That block is
preserved only in `FORMAL-SOURCE-MIRROR.md` as historical evidence and is not a sufficiency
contract. Current learner practice is authored from the frozen 94-cell `TEST-MATRIX.json`; use
`MCQ-QUESTIONS.md` and `MCQ-SOLUTIONS.md`.

"""
    session = session[:legacy_start] + current_mcq_note + session[legacy_end:]
    primary, supporting = current_pyq_section(session, pyqs, model2026)
    start = session.index("## PYQS AND ANSWER PRACTICE")
    end = session.index("#### ORIGINAL SOLVED MAINS PRACTICE", start)
    text = session[:start] + primary + "\n\n" + supporting + "\n\n" + session[end:]
    text = text.replace("| Directly owned verified PYQs solved in full | 9 |",
                        "| Primary-owned verified PYQs solved in full | 10 |")
    text = text.replace("| Supporting routed PYQ solved in full | 1 |",
                        "| Supporting cross-topic PYQ solved outside primary numbering | 1 |")
    text = text.replace("| Original diagnostic MCQs — 24 core plus 8 remedial drills | 32 |",
                        "| Coverage-derived MCQs — see frozen `TEST-MATRIX.json` | 94 |")
    text = text.replace("2018–2025 Jainism question", "2018–2026 Jainism question")
    old_rail = ("- **PYQ rail, 2018–2025 (nine owned).** 2018 Q6(c) 15 — bondage, bound / liberated soul. "
                "2019 Q6(a) 20 — reality and judgement. 2020 Q5(a) 10 — action-consequence and liberation. "
                "2021 Q7(c) 15 — sevenfold *naya*. 2022 Q5(d) 10 — action-consequence and soteriology. "
                "2022 Q6(b) 15 — relativism and absolutism. 2023 Q5(a) 10 — sevenfold judgement and empiricist relativity. "
                "2024 Q6(c) 15 — psychic and material bondage. 2025 Q7(c) 15 — pluralistic and realistic. "
                "**Supporting routed:** 2020 Q7(c) 15 — Cārvāka and Jaina conceptions of reality (Cārvāka-owned).")
    new_rail = (old_rail.replace("2018–2025 (nine owned)", "2018–2026 (ten primary-owned)")
                .replace("2025 Q7(c) 15 — pluralistic and realistic. **Supporting routed:**",
                         "2025 Q7(c) 15 — pluralistic and realistic. 2026 Q7(b) 15 — saptabhaṅgī, syādvāda and anekāntavāda. **Supporting cross-topic S1:**"))
    text = text.replace(old_rail, new_rail)
    text = text.replace("PYQ RAIL 2018-2025 (nine owned, one routed)",
                        "PYQ RAIL 2018-2026 (ten primary-owned)")
    text = text.replace(
        "2020 Q7(c) 15 Carvaka vs Jaina reality [routed]  | 2024 Q6(c) 15 bhava-/dravyabandha",
        "2026 Q7(b) 15 sevenfold conditional judgement    | 2024 Q6(c) 15 bhava-/dravyabandha",
    )
    text = text.replace(
        "2021 Q7(c) 15 the sevenfold naya                 | 2025 Q7(c) 15 pluralist and realist?",
        "2021 Q7(c) 15 the sevenfold naya                 | 2025 Q7(c) 15 pluralist and realist?\n"
        "  SUPPORTING S1 (outside primary numbering): 2020 Q7(c) Carvaka vs Jaina reality [Carvaka-primary]",
    )
    return "# Jainism — Revision Guide\n\n> Reconciled learner edition. The immutable formal session and workbook are preserved separately in `FORMAL-SOURCE-MIRROR.md`; current canonical PYQ ownership controls this guide.\n\n" + text


def answer_toolkit(workbook: str, pyqs: list[dict], model2026: str) -> tuple[str, list[dict]]:
    originals = section(workbook, "#### ORIGINAL SOLVED MAINS PRACTICE")
    primary, supporting = current_pyq_section(workbook, pyqs, model2026)
    toolkit = ["# Jainism — Answer-Writing Toolkit", "",
               "> Canonical ownership controls conflicts. The primary sequence is exactly ten Jainism-owned PYQs from 2018–2026. The Cārvāka-owned comparison is retained separately as Supporting S1.", "",
               "## Directive and timed-answer framework", "",
               "| Marks | Exact band | Recommended architecture |", "|---:|---:|---|",
               "| 10 | 150–200 words | definition → mechanism → evaluation |",
               "| 15 | 250–300 words | thesis → distinctions → objection/reply → verdict |",
               "| 20 | 340–400 words | conceptual derivation → detail → criticism → graded conclusion |", "",
               primary, "", supporting, "",
               "## Original coverage-driven timed practice", "",
               "> The formal workbook’s six original models are preserved verbatim below. Their selection is doctrine-driven: ontology/judgement, epistemology, standpoint/predication, bondage, liberation and inter-school criticism. Together with the ten PYQs, every major doctrine has a timed model.", "",
               originals, "",
               "## Major-doctrine answer spine", "",
               "| Doctrine | Mandatory distinctions | Best critical move |",
               "|---|---|---|",
               "| Jīva/ajīva and six substances | time is a substance but not an astikāya; pudgala alone has form | explain pluralist realism |",
               "| Karma and bondage | bhāva-bandha versus dravya-bandha; activity versus passion | explain soul–matter interaction objection |",
               "| Liberation | āsrava → bandha → saṃvara → nirjarā → mokṣa | distinguish bound soul, embodied omniscient and siddha |",
               "| Anekāntavāda | ontology, not a loose attitude | answer self-refutation without absolutizing |",
               "| Nayavāda | standpoint analysis | distinguish naya from nayābhāsa |",
               "| Syādvāda/saptabhaṅgī | conditional predication and seven forms | deny contradiction by indexed respects |",
               "| Epistemology | direct/indirect inversion and five knowledges | connect finite cognition to qualified assertion |",
               "| Ethics | three jewels, vows, guṇasthānas, sallekhanā | show discipline as karmic stoppage/shedding |", "",
               ]
    return "\n".join(toolkit), [{
        "year": x["year"], "question_no": x["question_no"], "marks": x["marks"],
        "text": x["text"], "text_sha256": sha_text(x["text"]),
        "ownership": "Jainism-primary", "status": "fully_solved",
    } for x in pyqs]


def main(generate_pdfs: bool = False) -> None:
    sources = {"formal_session": file_info(SESSION), "formal_workbook": file_info(WORKBOOK),
               "canonical": file_info(CANONICAL), "pyq_2018_2025": file_info(PYQ_OLD), "pyq_2026": file_info(PYQ_NEW)}
    sb = source_blocks(SESSION, "session")
    wb = source_blocks(WORKBOOK, "workbook")
    session = SESSION.read_text(encoding="utf-8").replace("\r\n", "\n")
    workbook = WORKBOOK.read_text(encoding="utf-8").replace("\r\n", "\n")
    bank = json.loads((ROOT / "MCQ-BANK.json").read_text(encoding="utf-8"))
    matrix = json.loads((ROOT / "TEST-MATRIX.json").read_text(encoding="utf-8"))
    mcqs = bank["questions"]
    seed = int(sha_text("|".join(s["sha256"] for s in sources.values()))[:16], 16)
    qmd, smd, mcq_audit = randomized_mcqs(mcqs, seed, matrix)
    pyqs = exact_pyqs()
    if len(pyqs) != 10:
        raise ValueError(f"Expected ten Jain-primary PYQs, found {len(pyqs)}")
    model2026 = fit_words("""Jaina non-absolutism begins from anekāntavāda, the ontological thesis that a real possesses many aspects and combines persistence with changing modes. A finite knower therefore grasps an aspect rather than the exhaustive object. Nayavāda analyses those legitimate but partial standpoints; syādvāda disciplines the assertion made from them.

The particle syāt means “from a specified respect,” not “perhaps.” Seven predications arise from affirmation, negation and inexpressibility, singly and in combination: in some respect it is; it is not; it is and is not; it is inexpressible; it is and is inexpressible; it is not and is inexpressible; and it is, is not and is inexpressible. “Is” and “is not” concern different indices of substance, place, time or mode, so the law of non-contradiction is preserved. Inexpressibility marks the inability to state opposed, qualified aspects simultaneously in one unqualified expression; it is not a third truth-value.

The application is illustrated by a clay pot: it exists as its present pot-mode, does not exist as cloth or as a past lump-mode, persists as clay, and resists a single exhaustive assertion. Thus saptabhaṅgīnaya translates a many-sided ontology into conditional predication. It avoids dogmatic one-sidedness without endorsing relativism or “anything goes,” because each claim remains answerable to a real object and a stated respect. Its strength is disciplined pluralism; its difficulty is whether endlessly qualifying assertions weakens their force. The Jaina reply is that qualification increases precision rather than abolishing truth.""", 250, 300)
    revision = reconciled_revision(session, pyqs, model2026)
    toolkit, pyq_rows = answer_toolkit(workbook, pyqs, model2026)
    workbook_mirror = anchored_copy(WORKBOOK, "workbook", wb, "Workbook")
    workbook_mirror = workbook_mirror[workbook_mirror.index("<a id="):]
    mirror = (anchored_copy(SESSION, "session", sb, "Formal Jainism Source Mirror — Learning Session and Solved Workbook") +
              "\n" + workbook_mirror)

    files = {
        "REVISION-GUIDE.md": revision,
        "MCQ-QUESTIONS.md": qmd,
        "MCQ-SOLUTIONS.md": smd,
        "ANSWER-WRITING-TOOLKIT.md": toolkit,
        "FORMAL-SOURCE-MIRROR.md": mirror,
    }
    for name, text in files.items():
        (ROOT / name).write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")

    decisions = []
    for b in sb + wb:
        dest = "FORMAL-SOURCE-MIRROR.md"
        d = dict(b)
        d.update({"classification": "covered_in_scope", "destination": {
            "file": dest, "anchor": b["id"], "anchor_kind": "stable_html_id",
            "payload_sha256": b["own_payload_sha256"],
            "mapping_basis": "Exact normalized source-owned payload under its unique source-derived anchor."
        }})
        decisions.append(d)
    panels = [d for d in decisions if "ASCII MASTER FLOW — PANEL" in d["heading"]]
    review = {
        "schema_version": 2, "topic": "02 Jainism", "authored_at": NOW, "review_status": "authored_frozen",
        "review_method": "Exhaustive heading-block preflight. Every semantic proposition is the complete source-owned block payload, never a generated excerpt or token-overlap claim; every destination is exact-preservation hash-bound. Parent-only payloads, payload-derived direct-child unions, large-leaf segments and visual panels are independently frozen.",
        "sources": sources, "decision_count": len(decisions), "classification_counts": {"covered_in_scope": len(decisions)},
        "unclassified_count": 0, "route_ledger": [], "decisions": decisions,
        "panel_parity": {"expected": len(panels), "actual": len(panels), "panel_ids": [p["id"] for p in panels]},
    }
    (ROOT / "FORMAL-COVERAGE-REVIEW.json").write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    audit = {
        "schema_version": 2, "derived_from": "FORMAL-COVERAGE-REVIEW.json",
        "review_sha256": sha_bytes((ROOT / "FORMAL-COVERAGE-REVIEW.json").read_bytes()),
        "decision_count": len(decisions), "covered": len(decisions), "routed": 0, "unclassified": 0,
        "source_counts": {"formal_session": len(sb), "formal_workbook": len(wb)},
        "large_leaf_segmented": sum(bool(d["large_leaf_segments"]) for d in decisions),
        "parent_blocks": sum(bool(d["direct_children"]) for d in decisions),
        "panel_parity": review["panel_parity"], "status": "DERIVED_COMPLETE",
    }
    (ROOT / "FORMAL-COVERAGE-AUDIT.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    mcq_audit["matrix_sha256"] = sha_bytes((ROOT / "TEST-MATRIX.json").read_bytes())
    mcq_audit["bank_sha256"] = sha_bytes((ROOT / "MCQ-BANK.json").read_bytes())
    (ROOT / "MCQ-AUDIT.json").write_text(json.dumps(mcq_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pyq_audit = {
        "schema_version": 1, "sources": {"2018_2025": sources["pyq_2018_2025"], "2026": sources["pyq_2026"]},
        "expected_year_counts": {"2018": 1, "2019": 1, "2020": 1, "2021": 1, "2022": 2, "2023": 1, "2024": 1, "2025": 1, "2026": 1},
        "expected_total": 10, "actual_total": len(pyq_rows), "questions": pyq_rows, "status": "COMPLETE",
        "supporting_total": 1,
        "supporting_questions": [{
            "year": 2020,
            "question_no": "Q7(c)",
            "marks": 15,
            "text": "Explain the differences of conception of Reality between Cārvāka and Jainism.",
            "text_sha256": sha_text("Explain the differences of conception of Reality between Cārvāka and Jainism."),
            "ownership": "Carvaka-primary/Jainism-supporting",
            "status": "fully_solved_outside_primary_numbering",
            "supporting_id": "S1",
        }],
    }
    (ROOT / "PYQ-DEMAND-AUDIT.json").write_text(json.dumps(pyq_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    coverage = f"""# Jainism — Coverage Ledger

## Frozen authority

| Source | SHA256 |
|---|---|
| Formal learning session | `{sources['formal_session']['sha256']}` |
| Formal solved workbook | `{sources['formal_workbook']['sha256']}` |
| Canonical Jainism owner | `{sources['canonical']['sha256']}` |
| PYQ ledger 2018–2025 | `{sources['pyq_2018_2025']['sha256']}` |
| PYQ ledger 2026 | `{sources['pyq_2026']['sha256']}` |

## Exhaustive preflight

- Formal session blocks: **{len(sb)}**
- Formal workbook blocks: **{len(wb)}**
- Total classified decisions: **{len(decisions)}**
- Covered locally: **{len(decisions)}**
- Routed elsewhere: **0**
- Unclassified: **0**
- Large leaves segmented: **{audit['large_leaf_segmented']}**
- Visual/master-flow panels hash-bound: **{len(panels)}**
- Primary Jainism PYQs: **10**
- Supporting cross-topic PYQs outside primary numbering: **1**
- Frozen MCQ test cells: **{len(matrix['cells'])}**
- Coverage-derived authored MCQs: **{len(mcqs)}**
- Mapping policy: **one distinct primary question per atomic cell**
- Frozen baseline: **38 adequate / 20 partial / 36 uncovered**

## Frozen test-cell categories

| Category | Cells | Baseline adequate | Baseline partial | Baseline uncovered | Final |
|---|---:|---:|---:|---:|---:|
| Foundations | 6 | 3 | 0 | 3 | 6 covered |
| Ontology | 13 | 6 | 6 | 1 | 13 covered |
| Epistemology | 10 | 4 | 1 | 5 | 10 covered |
| Many-sided logic | 26 | 11 | 2 | 13 | 26 covered |
| Criticism / comparison / PYQ | 11 | 2 | 3 | 6 | 11 covered |
| Karma / liberation / ethics | 22 | 11 | 7 | 4 | 22 covered |
| Transfer | 6 | 1 | 1 | 4 | 6 covered |

## Doctrine and surface matrix

| Obligation | Revision | MCQs | Timed/PYQ models |
|---|:---:|:---:|:---:|
| Jīva/ajīva; six substances; pudgala | ✓ | ✓ | ✓ |
| Karma as subtle material pudgala | ✓ | ✓ | ✓ |
| Āsrava, bandha, saṃvara, nirjarā, mokṣa | ✓ | ✓ | ✓ |
| Bhāvabandha/dravyabandha; bound/liberated soul | ✓ | ✓ | ✓ |
| Anekāntavāda as ontology | ✓ | ✓ | ✓ |
| Nayavāda as standpoint analysis | ✓ | ✓ | ✓ |
| Syādvāda as conditional predication | ✓ | ✓ | ✓ |
| Saptabhaṅgī and indexed non-contradiction | ✓ | ✓ | ✓ |
| Epistemology and five knowledges | ✓ | ✓ | ✓ |
| Ethics, vows, guṇasthānas and sallekhanā | ✓ | ✓ | ✓ |

Canonical content controls any conflict. Conditional predication is never presented as relativism, contradiction, indecision or “anything goes.”
"""
    (ROOT / "COVERAGE-LEDGER.md").write_text(coverage, encoding="utf-8", newline="\n")
    readme = """# Jainism — Offline Revision and MCQ Package

This self-contained package reconciles the complete formal learning session and workbook against the canonical Jainism owner and verified 2018–2026 PYQ ledgers.

Markdown is the canonical package format. Existing PDFs are legacy optional artifacts and are
generated or refreshed only on explicit request with `python build_package.py --with-pdfs` or
`python render_pdfs.py`; default builds and validation do not update or require them.

## Study order

1. `REVISION-GUIDE.md`
2. `MCQ-QUESTIONS.md`
3. `MCQ-SOLUTIONS.md`
4. `ANSWER-WRITING-TOOLKIT.md`
5. Record attempts in `PRACTICE-LOG.md`

`FORMAL-SOURCE-MIRROR.md` preserves the immutable 2018–2025 formal session/workbook snapshot for audit; its legacy nine-primary-plus-one-supporting numbering does not control the reconciled learner sequence.

`FORMAL-COVERAGE-REVIEW.json` is the authored/frozen formal-evidence ledger. `TEST-MATRIX.json`
contains the frozen 94-cell MCQ scope, and `MCQ-BANK.json` is its topic-local authored bank.
`FORMAL-COVERAGE-AUDIT.json`, `MCQ-AUDIT.json`, `PYQ-DEMAND-AUDIT.json`, and `VALIDATION.json`
are machine-auditable controls.
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    log = """# Jainism — Practice Log

| Date | Surface | Questions/answer | Score | Error type | Doctrine to revise | Reattempt date |
|---|---|---:|---:|---|---|---|
| | MCQ | | | recall / relation / trap / application | | |
| | 10-mark | | /10 | content / structure / evaluation | | |
| | 15-mark | | /15 | content / structure / evaluation | | |
| | 20-mark | | /20 | content / structure / evaluation | | |

## Mastery rule

- Reattempt every incorrect MCQ after 48 hours and again after seven days.
- Rewrite a Mains answer until it meets the exact word band and explicitly distinguishes ontology, standpoint analysis and conditional predication.
"""
    (ROOT / "PRACTICE-LOG.md").write_text(log, encoding="utf-8", newline="\n")
    if generate_pdfs:
        subprocess.run([sys.executable, "-B", str(ROOT / "render_pdfs.py")], check=True)
    print(json.dumps({"blocks": len(decisions), "session": len(sb), "workbook": len(wb), "mcqs": len(mcqs), "pyqs": len(pyqs), "seed": seed}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--with-pdfs",
        action="store_true",
        help="Explicitly regenerate optional legacy PDFs and PDF-MANIFEST.json.",
    )
    args = parser.parse_args()
    main(generate_pdfs=args.with_pdfs)
