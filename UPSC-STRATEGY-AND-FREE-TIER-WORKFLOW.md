# UPSC Strategy, Daily Timetable & Free-Tier AI Workflow

> **Authoritative study, revision, and token-economy operating guide.**
> Target: UPSC CSE Exam Cycle (Philosophy Optional).
> Saved on: 2026-10-21.

---

## 1. Free-Tier "Zero-Waste" AI Operation Matrix

When operating on free-tier limits, AI must be treated as an analytical evaluator and synthesizer of last resort, **not** as a reader, runner, or general viewer.

| Component | Working Mode | AI Token Cost | Operational Directive |
| :--- | :--- | :--- | :--- |
| **MCQ Practice & Recall** | **Offline (Local)** | **0 tokens** | Run questions in [`final-mcq/`](final-mcq/) directly in VS Code / Markdown. Solve on paper or scratchpad. Verify against `ANSWERS.md`. |
| **Reading Core Knowledge & Sessions** | **Offline (Local)** | **0 tokens** | Read canonical markdown in [`upsc-ai-kit/knowledge/`](upsc-ai-kit/knowledge/) and [`live_sessions/`](live_sessions/) locally. |
| **PYQ Solving** | **Offline (Self-practice)** | **0 tokens** | Read questions in [`solved_pyqs/`](solved_pyqs/). Write answers independently before checking solutions. |
| **Newspaper & InsightsIAS** | **Hybrid / Web** | **Minimal** | Read The Hindu and InsightsIAS directly. Copy only 1–2 dense, conceptual articles into prompts when extraction is needed. |
| **Missing Quick-Glance Charts** | **AI Targeted** | **Selective** | Execute `Continue Quick-Glance Atlas` one topic at a time to complete pending syllabus nodes. |
| **Mains Answer Evaluation** | **AI Targeted** | **High-Leverage** | Submit completed answers for strict UPSC examiner-grade critique: **claim → named evidence → analysis → qualification**. |
| **External Web Fallback** | **Manual Copy/Paste** | **0 API tokens** | When daily API quotas are reached, copy raw text/prompts into web-based AI tools (ChatGPT, Claude, Gemini web, DeepSeek) for analysis. |

---

## 2. Philosophy Optional & Core Timetable (Exam Year Focus)

### Current Tracker Milestone
- **Indian Philosophy (Paper 1, Section A):** Cārvāka, Jainism, Buddhism, Nyāya-Vaiśeṣika, Sāṃkhya, Yoga, and Mīmāṃsā are completed.
- **Immediate Pending Spine:** **Vedānta** (Śaṅkara Advaita, Rāmānuja Viśiṣṭādvaita, Madhva Dvaita) and **Śrī Aurobindo** (Integral Yoga, Evolution).
- **Subsequent Blocks:** Western Philosophy (Paper 1, Section B), followed by Philosophy of Religion and Socio-Political Philosophy (Paper 2).

### Strategic Timeline

```
+-------------------------------------------------------+---------------------------------------+
| Phase 1: Mains & Optional Freeze                      | Phase 2: Prelims Hyper-Focus          |
| (October 2026 – January 31, 2027)                     | (February 1 – May 2027)               |
+-------------------------------------------------------+---------------------------------------+
| * Finish Vedānta + Aurobindo + Western Philosophy.    | * Transition 80% time to Prelims GS.  |
| * Complete Paper 2 (Socio-Political & Religion).     | * Execute final-mcq 3-pass cycles.    |
| * Complete GS core static subjects (Polity, Economy). | * CSAT baseline mocks & error audits. |
| * 1 Mains PYQ answer written daily.                   | * 1 hr/day active recall for Optional.|
+-------------------------------------------------------+---------------------------------------+
```

### The 50-30-20 Daily Routine

- **50% of Study Time (3.5 – 4.0 Hours) — Philosophy Optional:**
  - Complete syllabus coverage of remaining thinkers.
  - Mandatory English-first terminology with Sanskrit/Pali glosses in parentheses: e.g., *dependent origination (pratītyasamutpāda)*.
  - Solve 1 timed PYQ daily (10 or 15 marks).
- **30% of Study Time (2.5 – 3.0 Hours) — Core GS Static:**
  - Progress through remaining Economy and Polity modules as tracked in [`UPSC-PROGRESS-TRACKER.md`](UPSC-PROGRESS-TRACKER.md).
- **20% of Study Time (1.5 – 2.0 Hours) — Daily Retrieval & Current Affairs:**
  - 30 minutes: Focused newspaper + InsightsIAS high-yield extraction.
  - 45–60 minutes: One 25–30 question block from [`final-mcq/`](final-mcq/).

---

## 3. Solved PYQs vs Knowledge Gaps: The "Need-to-Know" Protocol

> **Core Principle:** Do **not** conduct large, speculative knowledge audits upfront. This triggers the "collector's fallacy" (polishing notes rather than building retrieval memory) and consumes unnecessary tokens.

### Backward-Engineering Workflow:
1. **Anchor on PYQs First:** Open the topic folder in [`solved_pyqs/topics/`](solved_pyqs/topics) covering 2013 to present.
2. **Audit Against Demands:** Check whether your existing [`live_sessions/`](live_sessions/) or [`upsc-ai-kit/knowledge/`](upsc-ai-kit/knowledge/) file contains the exact doctrines, arguments, criticisms, and evidence needed to answer those specific questions.
3. **Targeted Patching Only:**
   - If your notes provide sufficient basis for an examiner-grade 10/15/20-mark answer: **mark the topic complete and move on**.
   - If an examinable dimension is absent (e.g., Rāmānuja's *Aprathaksiddhi* or an obscure criticism): patch **only** that specific subtopic into the knowledge file.

---

## 4. `final-mcq` 3-Pass Spaced Repetition Protocol

All question banks in [`final-mcq/subjects/`](final-mcq/subjects/) and [`final-mcq/current-affairs/`](final-mcq/current-affairs/) should be practiced offline without AI overhead.

1. **Pass 1 (`revision-1`):**
   - Solve questions immediately following topic study under strict exam timing (approx. 50–60 seconds per question).
   - Grade against `ANSWERS.md`.
   - Classify every answer into:
     - `C` = Confidently Correct (do not revisit).
     - `G` = Lucky Guess / Intuition (concept shaky).
     - `E` = Factual or Conceptual Error.
2. **Pass 2 (`revision-2`):**
   - 7 to 10 days later, attempt **only** items marked `G` and `E`.
   - Log the precise failure reason in your error log (e.g., misread negative directive, confused statutory vs constitutional body).
3. **Pass 3 (`revision-3`):**
   - 30 days later, execute a rapid diagnostic run across mixed topics.

---

## 5. Newspaper & InsightsIAS Streamlining

Full PDF editions (15–20 MB) consume massive context windows if passed directly to AI models. Streamline current affairs with zero token waste:

1. **10-Minute Manual Skim:**
   - Limit reading in *The Hindu* to:
     - **Editorial Page** (lead article + 2 short editorials).
     - **Op-Ed Page** (central analytical column).
     - **Text & Context** (data points and explainers).
     - **Science Supplement** (weekly).
   - Ignore regional crime, political mudslinging, and administrative routine news.
2. **InsightsIAS Integration:**
   - Read the InsightsIAS Daily Current Affairs / SECURE initiative online.
   - Use their structured GS-1, 2, 3, 4 classification directly rather than asking AI to re-classify news.
3. **Minimal Token Extraction Prompt:**
   - When encountering a deeply technical or complex legal issue in Text & Context, copy only the plain text of that single article into an AI prompt:
   ```text
   Act as a UPSC examiner. Extract from the text above:
   1. Core constitutional/statutory/economic issue.
   2. 3 sharp arguments in favor.
   3. 3 sharp arguments against/challenges.
   4. High-yield data points, committee names, or case precedents.
   5. One balanced forward-looking conclusion sentence.
   ```
   - Save the output directly into your topic register notes.

---

## 6. External Free-Tier Web AI Fallback Routine

If local IDE/CLI daily token limits are exhausted:
1. Open the relevant file locally in VS Code.
2. Copy the relevant topic text or question into clipboard.
3. Open a free web AI interface (Gemini, Claude, ChatGPT, DeepSeek).
4. Paste the text with your structured prompt to continue uninterrupted.
5. Paste the final evaluated answer or summary back into your local markdown file.
