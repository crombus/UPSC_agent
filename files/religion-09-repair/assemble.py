"""Assemble Learning-Session.md and Solved-Practice-Workbook.md for Philosophy of Religion 09."""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent

TOPIC = ROOT / "learning_package_final" / "Philosophy-Optional" / \
    "Philosophy-Paper-II-\u2014-Philosophy-of-Religion" / \
    "09-Religious-Pluralism-and-Absolute-Truth"

parts = [
    "part-00-front.md",
    "part-01-sessions-01-04.md",
    "part-02-sessions-05-09.md",
    "part-03-sessions-10-13.md",
    "part-04-sessions-14-16.md",
    "part-05-sessions-17-21.md",
]
mcq_parts = ["part-06-mcq-01-12.md", "part-07-mcq-13-32.md"]
pyq = (BASE / "part-08-pyq.md").read_text(encoding="utf-8")
adv = (BASE / "part-09-advanced-register.md").read_text(encoding="utf-8")
ascii_txt = (BASE / "ASCII-Master-Flowchart.txt").read_text(encoding="utf-8")


def embed_ascii(raw):
    """Turn the flat ASCII master into fenced Markdown panels."""
    chunks = re.split(r"^(ASCII MASTER FLOW \u2014 PANEL \d+/31: .+)$", raw, flags=re.M)
    out = ["### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM", ""]
    for i in range(1, len(chunks), 2):
        heading = chunks[i].strip()
        body = chunks[i + 1].strip("\n")
        out.append(f"#### {heading}")
        out.append("")
        out.append("```ascii-master")
        out.append(body)
        out.append("```")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


session_body = "\n".join((BASE / p).read_text(encoding="utf-8").rstrip("\n") for p in parts)
mcq_body = "\n".join((BASE / p).read_text(encoding="utf-8").rstrip("\n") for p in mcq_parts)

session = "\n\n".join([
    session_body,
    mcq_body,
    pyq.rstrip("\n"),
    adv.rstrip("\n"),
    "---",
    embed_ascii(ascii_txt).rstrip("\n"),
]) + "\n"

(TOPIC / "Learning-Session.md").write_text(session, encoding="utf-8")
print("Learning-Session.md bytes:", (TOPIC / "Learning-Session.md").stat().st_size)

WORKBOOK_FRONT = """---
title: "Religious Pluralism and the Problem of Absolute Truth \u2014 Solved Practice Workbook"
topic_key: philosophy-paper-ii-philosophy-of-religion-09
variant: learner-v2
---
# Religious Pluralism and the Problem of Absolute Truth \u2014 Solved Practice Workbook

> **Philosophy Optional \u00b7 Philosophy Paper II \u2014 Philosophy of Religion \u00b7 Topic 09**
> A standalone practice document. It is designed to be worked without the learning session open beside it, and it repeats no teaching prose.

### How to use this workbook

Attempt every item before reading its key. The correct option position was fixed **independently for each question** by a randomised, length-balanced assignment: there is no rotation, no repeating cycle and no adjacent repetition to exploit, and each of the four positions carries exactly eight answers across the thirty-two diagnostics. Every option carries a question-specific explanation, and every question carries a unique examiner trap. The previous-year questions reproduce the official printed wording exactly; **the model answers are independent learner practice and are never official UPSC keys.**

### What is inside

| Part | Content | Count |
|---|---|---:|
| 1 | Core diagnostic MCQs | 24 |
| 2 | Remedial diagnostic MCQs | 8 |
| \u2014 | Question-specific option explanations | 128 |
| \u2014 | Unique examiner traps | 32 |
| 3 | Verified previous-year questions, fully solved | 12 |
| 4 | Original solved Mains models (2 \u00d7 10, 2 \u00d7 15, 2 \u00d7 20) | 6 |
| 5 | Question-shaped timed-paper compression plan | 12 rows |

### Marking and timing conventions

- Word bands: 10 marks \u2248 150 words \u00b7 15 marks \u2248 250 words \u00b7 20 marks \u2248 350 words.
- Every model answer follows **claim \u2192 named evidence \u2192 analysis \u2192 qualification**.
- Every model answer closes with a decided verdict, and the twenty-mark models additionally name the **defeater** that would change that verdict.
- **Standing penalties in this clause:** defining pluralism as "all religions say the same thing"; merging inclusivism with pluralism; presenting exclusivism only as bigotry; citing *ekaṃ sat* without its native context or its bridging argument; quoting *extra ecclesiam nulla salus* as Cyprian's own words; omitting the 1965 qualification; treating "tolerance" as one thing; answering the conflict-history stem with a list of wars; and citing Huntington as a finding rather than as a thesis under sustained criticism.

### Terminology rule

English-first throughout. The English concept leads; the accurate Sanskrit, Pali, Greek, German or Latin term follows in parentheses.

### Self-scoring table

| Band | Diagnostics correct (of 32) | What the Mains attempts show |
|---|---:|---|
| Weak | 0\u201314 | "All religions lead to the same God"; the triad named but not distinguished |
| Average | 15\u201320 | Triad distinguished; Hick and Vivekananda present; exclusivism shown only as bigotry |
| Good | 21\u201325 | Truth, salvation, access and coexistence separated; one objection answered |
| Strong | 26\u201329 | Plantinga stated and met; RV 1.164.46 and Cyprian handled correctly; many-sidedness used as a logic |
| Top | 30\u201332 | All the above, plus one discriminating distinction and an explicit acknowledgement of hard contradictions |

### Trap census

The thirty-two examiner traps below are distinct and non-repeating. Twelve of them correspond directly to the owner's printed trap list; the remaining twenty are answer-execution faults observed in this clause's directives.

### Independence note

Every model answer, original question, diagnostic item and option explanation in this workbook is **independent learner practice**. None reproduces an official mark scheme. Only the twelve previous-year questions are reproduced verbatim, from the audited repository ledger, and they are reproduced for practice routing.
"""

workbook = "\n\n".join([
    WORKBOOK_FRONT.rstrip("\n"),
    mcq_body,
    pyq.rstrip("\n"),
]) + "\n"

(TOPIC / "Solved-Practice-Workbook.md").write_text(workbook, encoding="utf-8")
print("Solved-Practice-Workbook.md bytes:",
      (TOPIC / "Solved-Practice-Workbook.md").stat().st_size)

PKG = ROOT / "notes" / "Final-Learning-Packages" / "Philosophy Optional" / \
    "Philosophy Paper II \u2014 Philosophy of Religion" / "09-Religious-7556c0ef-Truth"
(PKG / "04-ASCII-Master-Flowchart" / "ASCII-Master-Flowchart.txt").write_text(
    ascii_txt, encoding="utf-8")
print("ASCII-Master-Flowchart.txt bytes:",
      (PKG / "04-ASCII-Master-Flowchart" / "ASCII-Master-Flowchart.txt").stat().st_size)
