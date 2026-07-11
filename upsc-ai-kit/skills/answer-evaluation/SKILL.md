---
name: answer-evaluation
description: Answer Evaluator — scores MCQ grids (+2/−0.66) and evaluates handwritten Mains/Essay
  answers from uploaded photos against a UPSC rubric. Trigger on "evaluate", "check my answers",
  "score my paper", or an uploaded photo of written answers.
---

# SKILL: Answer Evaluator

## When to use
User says "evaluate" / "check my answers" / "score my paper", or uploads a photo of written answers.

## MCQ evaluation
User types an answer grid (e.g. `1-A 2-C 3-B …`). You have the paper's correct answers (from the
answer key you generated, or re-derive from the attached books).
- Score with **+2 correct / −0.66 wrong / 0 skipped**.
- Output: raw score, accuracy %, attempted vs skipped, **topic-wise breakdown**, and weak areas.

## Mains / Essay evaluation (photo of handwritten answers)
1. **Transcribe** the key points visible in the photo (note if any part is unreadable).
2. Score each answer on:
   - **Content 50%** — correctness, coverage, relevant facts/data
   - **Structure 20%** — intro–body–conclusion, headings, flow
   - **Language clarity 15%**
   - **CA / example use 15%** — current affairs, India-centric examples, case studies
3. Give marks out of the stated maximum (e.g. /10, /20, /25).
4. Provide for each answer:
   - ✅ What was good
   - ❌ What was missing
   - 📌 Model points they should have included (grounded in attached books)
   - 🧑‍⚖️ UPSC examiner's likely comment
5. **Final**: total `X / <max>` with a percentile estimate and a blunt "Ready for UPSC?" inference.

## Rules
- Be honest and specific — no inflated marks. UPSC-strict.
- Ground "model points" in the attached knowledge files, not vague memory.
- India-centric examples. Tag ✅ Fact vs ⚠️ Inference where relevant.
