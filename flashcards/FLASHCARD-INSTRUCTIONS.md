# Flashcard Production Instructions (saved 2026-11-01)

Authoritative workflow for the `flashcards\` folder. Subject progress is tracked in
`FLASHCARD-SUBJECT-INDEX.md`. Scope of work: `flashcards\` only, reading from
`upsc-ai-kit\knowledge\<Subject>\` (read-only). Quick-glance and live-session folders are untouched.

## 1. Output
- One Markdown file per subject: `flashcards\<Subject>.md` (Polity, Economy, Internal-Security and
  Disaster-Management are already done).
- Subjects are produced **strictly one after another**, in the order in `FLASHCARD-SUBJECT-INDEX.md`,
  without pausing between subjects. Within one subject, work may be split across parallel agents
  by owner-file range; the subject is finished (merged, validated, indexed) before the next begins.
- **No compression, no skipping.** Every examinable item in the subject's `basic\` and `advanced\`
  owner files (and its revision chart / master framework) gets its own card.

## 2. Card format (all subjects)
```
### Flashcard <PFX>-<nnnn> — <Title>
**Front:** <what is asked>
**Definition (learn):** <crisp definition / what the item is>
**Breakdown:**
- <classification / components / mechanism / numbers / chronology>
**Key facts / Dates / Data:** <exact references; years; names; figures; source tags>
**Links:** <related cards by ID; related Articles / Acts / chapters>
**Trap:** <examiner trap / close-option distinction / PYQ route>
**Mains hook:** <how it is asked and a qualified conclusion>
**Back:** *"<original mnemonic or one-line recall>"*
```
- **Front** is the question side; **Definition/Breakdown** is what to learn; **Back** is the
  mnemonic or shorter sentence (user's original spec).
- Mnemonics are original, short, accurate and never contradict the content. For lists use a
  letter-code or phrase.
- IDs are unique per subject: `<PFX>-<agent-block><seq>` e.g. `GEO-1001`; cross-references must
  resolve inside the same file.

## 3. Accuracy rules
- **Verify, never fabricate.** Order of grounding: (1) repository Markdown owners; (2) pages that
  can be fetched (Wikipedia, Wikisource Constitution text, PRS, UN/WHO/IMF/UNDRR/CDRI etc.);
  (3) standard knowledge flagged ⚠️. WebSearch and curl do not work; many `.gov.in` sites return
  403/404 — try once, move on.
- Confirmed from a source → `(✅ <source>)`. Unverified or memory-only → `⚠️`. Owner-only →
  `(✅ owner NN)`. Never invent a year, figure, section number, toll or case holding.
- Time-varying facts (rankings, outlays, counts, status of schemes) only with an as-of date from the
  owner or a fetched dated source; otherwise omit or ⚠️.
- Owner/Wikipedia conflicts are flagged inside the card, not silently resolved.
- India-centric examples; English-first terminology.
- **Philosophy only:** English term first with the Sanskrit/Pali IAST term in parentheses.

## 4. Card selection (my judgement per subject)
Cards are chosen to maximise recall value:
- **Entities** — Acts, Articles, commissions, committees, institutions, schemes, missions, treaties,
  conventions, indices, organisations (year, parent body, mandate, key provisions, amendments).
- **Concepts and processes** — definitions, mechanisms, causal chains, classifications,
  comparisons, formulas/thresholds.
- **Facts-in-place** (Geography, History, Culture) — location/feature/date/ruler/event cards with
  cause → course → consequence → significance.
- **Thinkers and doctrines** (Ethics, Philosophy, Political Theory, Society) — thinker, work, core
  claim, objection, reply, contrast pair.
- **Traps** — close-option pairs, common confusions, PYQ patterns inside the relevant card.
Per-subject focus is listed in `FLASHCARD-SUBJECT-INDEX.md`.

## 5. Per-subject workflow
1. Enumerate owner files and split them into balanced owner-file ranges (by word count).
2. Brief each agent with the rules above plus the subject's card focus; each writes one fragment
   under `/tmp/flashcards_build/<subject>_<part>.md` with a unique ID block.
3. Merge fragments in owner order with a file header into `flashcards\<Subject>.md`.
4. Validate: no duplicate IDs, no dangling cross-references, every owner file represented,
   count of cards and ⚠️/✅ tags recorded.
5. Update `FLASHCARD-SUBJECT-INDEX.md` (status, file, card count, ⚠️ count) and continue to the
   next subject.
6. Optional later: a separate verification pass per subject (Polity and Economy have had two).

## 6. Delivery
`git apply` patch generation and upload steps are in the session history; generate a fresh patch
with `git diff --no-index -- /dev/null flashcards/<file>.md` per file. Commit and push only on
the user's explicit instruction.
