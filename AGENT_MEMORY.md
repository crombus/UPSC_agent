# UPSC Agent — Saved Instructions & Memory

> **Portable single source of truth** for all rules, preferences, workflows, and verified
> facts that @pulkitkundra has asked the agent to "save".
> Whenever the user says **"save"**, the agent does BOTH: (1) stores a Copilot memory, and
> (2) appends/updates the rule here so it survives across sessions, machines, and other apps.
>
> _Last updated: 2026-06-22_

---

## 0. How "save" works (meta-rule)

- When the user says **"save" / "save instructions" / "remember"**, persist the rule in **two** places:
  1. **Copilot memory** (`store_memory`, user scope).
  2. **This file** (`AGENT_MEMORY.md`) under the correct section, so it is portable and reusable
     in future sessions or other applications.
- Keep entries concise, grouped by topic, and dated when material changes.

---

## 1. Core principles (highest priority)

- **Verify before stating.** Never present unverified training-knowledge facts as ground truth.
  Use `web_search` for CA/recent facts; use Qdrant for book facts. If uncertain, say so.
  Wrong data in UPSC prep is worse than no data — this rule overrides convenience.
- **No fabrication.** Never guess %, ₹, years, targets, counts, or scheme names.
- **Tag everything:** ✅ Fact = directly from fetched/retrieved source · ⚠️ Inference = analytical.
- **Source priority:** (1) user-uploaded PDFs/snippets → (2) live `web_fetch` → (3) Qdrant books →
  (4) training knowledge (label as ⚠️ Inference).
- **India-centric examples** always.

---

## 2. Qdrant / book grounding

- **Start Qdrant first — always**, before any teaching, CA analysis, MCQ, or exam generation.
  ```
  docker start qdrant-upsc
  ```
  Full run command if the container does not exist:
  ```
  docker run -d --name qdrant-upsc -p 6333:6333 ^
    -v "C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\vectordb\static:/qdrant/storage" ^
    qdrant/qdrant
  ```
  First query has ~2 min embedding warmup. Never skip this step.
- **Query books** for context before answering teaching questions or generating exams:
  ```
  python tools/query_books.py "<topic>" --subject "<Subject>" --limit 5
  ```
  `--subject` is an **exact-match** filter — the string must match the stored tag precisely.
- If the DB is unavailable/empty, fall back to training knowledge + `web_search` silently.

### Subject tags (exact strings)
Indian Polity · Economy · History · Geography · Ethics · International Relations ·
Internal Security · Disaster Management · Current Affairs
**PYQ tags:** `Prelims PYQ` · `CSAT PYQ` · `Mains PYQ` · `Philosophy PYQ`

---

## 3. Exam generation

### Format v2 (current, locked)
- **Paper 1 — 100 MCQs:**
  - 80 GS = **48 Current Affairs** + **32 Static**
  - 20 **CSAT (Hard)** — calibrated to real UPSC PYQ difficulty (query `--subject "CSAT PYQ"`).
- **Paper 2:** 2 × 10-mark + 2 × 20-mark Mains (user attempts 1 of each pair) + **Essay (1 of 3)**.
- Philosophy essay: optional / random — not every paper.
- Difficulty will scale up slowly over time.

### Sourcing rules
- **Book/static questions come from Qdrant** (genuine book content) — never hallucinated.
- **For CA sections, also `web_search`** around the user's given topics — they may have missed items.
- **Recency weighting 40:60** → 40% older/static (> 1 week), 60% past-week content.
- Reserve a portion for **static topics** even in CA-heavy papers.
- Generate the exam for **whatever topics the user gives**, even if some overlap.

### MCQ verification step (run BEFORE finalizing every MCQ)
1. Does the question text or options accidentally give away the answer? (Fix if so.)
2. Chronological-ordering questions: **strip all years/dates** from option text — use event/conflict
   names only.
3. Statement-based questions: verify **each statement independently** before marking correct/incorrect.
- **Anti-bias:** rotate the correct option A→B→C→D; never repeat the same option consecutively.
- CA MCQs must test **concept + geography + institution + data** — NOT ceremony details
  (signing dates, venues, who represented whom). Concept-level facts = higher UPSC probability.
- When a topic was covered in the current session's CA analysis, use **session-verified CA data first**;
  training knowledge is fallback only.
- **Marking:** MCQ = +2.00 correct / −0.66 wrong / 0 skipped.

### PDF workflow
- Build data `.py` → `python tools/upsc_exam_pdf.py <data.py> <out.pdf>` → delete the data `.py`.
- Papers → `exams/papers/..._QP.pdf` · Answer keys → `exams/answer-keys/..._AK.pdf`.
- **Set matching:** prelims QPs are **Set A only**; `Ans-*` files hold all sets → map Set A → Set A column.

---

## 4. Current Affairs analysis

- **Sources are for DISCOVERY only** (what news happened on a date). ALL UPSC analysis
  (relevance, dimension shift, traps, mains angle) must be the agent's own — never copied from
  coaching-site analysis.
- **Source fetch methods:**
  - Vision IAS — JS-rendered + paywalled → use `web_search "visionias topics YYYY-MM-DD"` (no direct fetch).
  - Vajiram — `vajiramandravi.com/current-affairs/upsc-prelims-current-affairs/YYYY/MM/DD/` (direct fetch OK).
  - MEA — JS-rendered → `web_search site:mea.gov.in "DD Month YYYY"` (no direct fetch).
  - PIB — `web_fetch pib.gov.in/indexd.aspx?reg=3&lang=1`.
  - GKToday `/current-affairs/june-DD-YYYY/` returns 404 — avoid.
- **Per-item deep-analysis order:** FACTS → **📘 FULL FORMS** (dedicated section, every abbreviation
  expanded, placed right after FACTS) → ORIGIN → … → traps → mains angle → static link.
- **After EVERY CA item:** include (1) **MCQ loop** (2–3 MCQs, anti-bias rotation) and
  (2) **Register Notes** (title, facts, timeline, traps, mains angle). Both mandatory per item.
- **Medium-item format:** Title + GS paper + news trigger + 4–5 key facts + 1 UPSC trap +
  Mains angle (1 line) + static link. Not just 2-line summaries.
- **Export PDF** must include ALL items: HIGH (full deep analysis), MEDIUM (expanded summary +
  GS angle + key facts + 1 trap), LOW (2–3 line note + GS paper). Never export only HIGH.
- **Never conflate distinct news items.** Each separate event = its **own card/section** in CA
  analysis, deep-dives, and Export/Notes PDFs. Never merge two stories into one card, and never
  phrase them so one event appears to **cause or be the subject of** another — even words like
  "separately"/"simultaneously" inside one shared card still mislead. One news item → one card.

---

## 5. Guided Tutor & Notes

- **Static notes follow strict chapter sequence** — never skip or start mid-book:
  - RS Sharma Ancient History from **Ch-1** onwards.
  - GC Leong / Geography from **Ch-1** onwards.
  - Track completed chapters; always continue from the next pending chapter.
- Teach **visually first** (≥1 diagram/table/flowchart per subtopic), text second.
- One subtopic per response; never auto-advance — wait for a navigation command.

### 5a. AI-kit knowledge files (output format & location — IMPORTANT)

- Subject study notes are authored as **Markdown `.md`**, saved under
  `upsc-ai-kit/knowledge/<Subject>/basic/` and `upsc-ai-kit/knowledge/<Subject>/advanced/`.
  **NOT** PDFs — these are portable knowledge for **Claude / Gemini / OpenAI**, consumed alongside
  `system-prompt.md` + `skills/` + `tools/`. (PDFs in `notes/` are a separate, optional deliverable.)
- Format = the Polity kit style: `#` title with `— MUST-DO`/`— ADVANCED`, blockquote header
  (Subject · Tier · GS Paper · "Grounded in" · ✅/⚠️/📰 legend · `*Companion:*`), numbered `##`
  sections, Markdown tables, `> 🔑 Trap:` callouts, **Must-Know Facts**, **UPSC Traps**,
  **📰 Current link**, **Mains angles**. File naming `NN_Topic-Name.md`.
- **Accuracy & completeness are paramount; never drop or fabricate facts. Must-Do tier is the
  priority and must be exhaustive.**
- **Geography tier mapping:** `basic/` (Must-Do) = **Majid Husain "Indian & World Geography" + GC
  Leong + CA anchor**; `advanced/` = **Dr. D.R. Khullar + Majid Husain India geography + extra
  distinct CA**. **Both tiers must carry a current-affairs anchor.** (Khullar = optional-level depth.)

---

## 6. Study tracking (dates & methods)

- **Start dates:** CA daily = **6 June 2026** · MCQ daily practice = **9 June 2026** ·
  Mains answer writing (1/day) = **9 June 2026** · Essay (1/week, Sunday) = **9 June 2026**.
- **Daily Mains (20 min):** 2 min read+directive, 2 min outline, 12 min write, 4 min self-evaluate on
  Content /3 · Structure /2 · Multidimensionality /3 · Language /2 = **/10**.
- **Essay (weekly, Sunday):** 3 stages — Deconstruct (5 min: hidden assumption, both sides, verdict) →
  Build Spine (10 min: narrative arc, not a point list) → Write with philosophy (optional edge:
  Rawls, Sen, biocentrism, etc.).

---

## 7. Ingestion (adding new PDFs)

- Drop PDF in the correct subfolder of `books/`; run `python ingestion/ingest.py`.
  Already-ingested files are skipped via checkpoint (`vectordb/static/checkpoint.json`).
- **Folder-aware subject tagging** (`ingest.py` → `infer_subject`):
  - `books/mains/` → `Mains PYQ`
  - `books/philosophy_optional*/` → `Philosophy PYQ`
  - `books/prelim*/` → `CSAT PYQ` if "csat" in filename, else `Prelims PYQ`
  - else → fall back to `SUBJECT_KEYWORDS` filename matching.
- **OCR caveat:** scanned bilingual PYQs are OCR'd **English-only** → Hindi/Devanagari comes out
  garbled. Use the clean English half; ignore garbled Hindi when querying these PYQs.

---

## 8. Verified facts & corrections

- **JPN Bird Sanctuary** = Jai Prakash Narayan Bird Sanctuary (a.k.a. **Surha Tal**), **Ballia district, UP**.
  India's **100th Ramsar site**, announced **5 June 2026** (World Environment Day).
  NOT Jagdishpur–Phulhar–Nawabganj.
- **Jagdishpur (Sultanpur), Phulhar (Bahraich), Nawabganj (Unnao)** are **three separate** Ramsar sites
  in UP — do **not** call them a single "JPN complex".
- **Misri vs First Secretary (The Hindu, 20 June 2026) — KEEP SEPARATE (two distinct stories):**
  1. **Parliamentary Standing Committee on External Affairs** (Chair: **Shashi Tharoor**) questioned
     **Foreign Secretary Vikram Misri** on the government's Pakistan **engagement** policy
     (people-to-people ties, SCO summit, Track-II) — trigger was **RSS advocacy** for keeping the
     window open; meeting was a pre-tour briefing before the panel's J&K/Ladakh study tour (Jun 22–25).
  2. **First Secretary Anupama Singh** (India's UN Permanent Mission) called Pakistan a
     **"Frankenstein state"** at the UN (rebutting Pakistan + OIC on J&K).
  The panel did **NOT** question Misri about the First Secretary's UN remark. Do not link them.
