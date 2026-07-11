# UPSC AI Kit — Portable Preparation Assistant

A drop-in kit that recreates your UPSC study assistant on **Claude, ChatGPT (OpenAI), or Gemini**.
It contains the assistant's **instructions**, its **skills**, the **PDF tools**, and your
**subject knowledge** (curated basic/advanced notes + full source-book exports).

```
upsc-ai-kit/
├── README.md              ← you are here
├── system-prompt.md       ← paste as system / custom / project instructions
├── skills/                ← one folder per skill (study, exam, answer-evaluation, current-affairs)
├── tools/                 ← Python PDF generators (needs reportlab)
├── knowledge/             ← <Subject>/basic + <Subject>/advanced + _source-library (raw books)
└── guides/upload-guide.md ← detailed per-platform setup
```

---

## Quick start by platform

### 🟣 Claude (Projects + Agent Skills) — closest match
1. Create a **Project**. Paste `system-prompt.md` into *Project instructions*.
2. Add each `skills/*/SKILL.md` as a **Skill** (or attach them as Project knowledge).
3. Upload the relevant `knowledge/<Subject>/…` files for what you're studying.
4. Enable **web search** (for current affairs) and **code execution** (for PDF generation).

### 🟢 ChatGPT (Project / Custom GPT + Agent mode)
1. New **Project** (or Custom GPT). Paste `system-prompt.md` into instructions.
2. Upload the `SKILL.md` files + subject knowledge files to the Project.
3. Turn on **web browsing / Agent mode** (current affairs) and **Code Interpreter** (PDFs).

### 🔵 Gemini (Gem)
1. Create a **Gem**. Paste `system-prompt.md` as the Gem instructions.
2. Attach `SKILL.md` files + subject knowledge.
3. Google Search grounding gives live data; PDF export via Docs/Canvas (layout less exact).

See `guides/upload-guide.md` for details, file-size limits, and which files to upload when.

---

## What transfers vs. what doesn't

| Capability | In this kit? |
|---|---|
| Assistant behaviour & skills | ✅ `system-prompt.md` + `skills/` |
| Static book knowledge | ✅ `knowledge/` |
| Premium PDF layout | ✅ `tools/` (needs a platform that runs Python) |
| Live current affairs | ⚠️ needs the platform's own web/agent tool enabled |
| 107K-chunk vector retrieval | ❌ replaced by uploading per-subject files |

---

## Notes
- Attach **only the subject you're studying** — the full library exceeds any context window.
- OCR'd PYQ files: English is clean, Hindi/Devanagari is garbled (ignore the Hindi).
