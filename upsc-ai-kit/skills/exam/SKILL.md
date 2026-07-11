---
name: exam
description: Exam Generator — produces print-ready UPSC papers (MCQ + CSAT + Mains + Essay) with
  ZERO answers in the paper, grounded in attached books + latest current affairs. Trigger on
  "generate exam", "test me", "exam paper", "Bundle".
---

# SKILL: Exam Generator

## When to use
User gives topics and says "generate exam" / "test me" / "exam paper" / `Bundle`.

## Format (2 papers, ~2 hours)
**Paper 1 — Objective (100 MCQ):**
- 80 GS: **60 Current Affairs + 40 Static** (of the 100 overall, keep this 60:40 CA:static tilt)
- 20 **CSAT** — Hard level (UPSC-PYQ difficulty or harder; NOT basic arithmetic)
- Marking: **+2.00 correct / −0.66 wrong / 0 skipped**

**Paper 2 — Descriptive:**
- 2 × 10-mark Mains (attempt 1) — 150 words
- 2 × 20-mark Mains (attempt 1) — 250 words
- 1 Essay from 2–3 choices (different domains) — 1000–1200 words. Philosophy essay optional/random.

> Content weighting: give preference to **latest (past-week) current affairs (~60%)** over older
> material (~40%), but always keep a static portion. Topics may overlap — generate regardless.

## HARD rules (question paper)
- **ZERO answers, hints, or explanations anywhere.** No answer key in the paper.
- Each MCQ: stem + 4 options (A/B/C/D). Anti-bias: rotate correct option across A→B→C→D.
- 10-mark: directive word (Examine/Discuss/Analyse) + "Answer in 150 words."
- 20-mark: directive + context + "Answer in 250 words."
- Essay: 2 choices from different domains + "Write an essay in 1000–1200 words."
- Continuous serial Q numbers across all sections; print-ready.

## Grounding rules
- **Static/book MCQs → must come from the attached books** (`knowledge/_source-library/…` or
  curated notes), never from unverified memory. Every factual claim traces to a book.
- **CA MCQs → ground in the topic's latest news** (use web search if enabled). Even when the user
  gives CA topics, also search around them — the user may have missed items.
- **CA MCQs must test concept + geography + institution + data**, NOT ceremony trivia (signing
  dates, venue names, who represented whom).
- Calibrate CSAT/Mains difficulty & style against attached PYQ sets.

## MCQ verification (before writing each MCQ)
1. Does the stem/options give away the answer? Fix.
2. Chronological-ordering questions: strip all years/dates from options — use only event/conflict names.
3. Statement-based: verify each statement independently before marking correct/incorrect.

## PDF generation
Build a Python `DATA` dict and run:
- Paper:      `python tools/upsc_exam_pdf.py data.py ExamPaper_<topics>_<date>_QP.pdf`
- Answer key: `python tools/upsc_answer_key_pdf.py ak_data.py ExamPaper_<topics>_<date>_AK.pdf`
  (answer key is a SEPARATE file — never inside the paper.)

`DATA` schema (exam paper): dict with `title`, `date`, `max_marks`, `time`, `topics`,
`instructions` (list), `sections` (list). Each section: `name`, `marks_text`, `instruction`, then
either `parts` (MCQ) or `questions` (Mains/Essay).
- MCQ question: `no`, `text`, `options` (4), optional `statements` + `stem_tail`, optional `table`.
- Mains question: `no`, `type:"mains"`, `text`, `meta` (GS paper + marks + word count).

`Bundle` = full mock across GS1+GS2+GS3+CSAT in one go.
If no Python tool is available, output the paper as clean Markdown with the same rules.
