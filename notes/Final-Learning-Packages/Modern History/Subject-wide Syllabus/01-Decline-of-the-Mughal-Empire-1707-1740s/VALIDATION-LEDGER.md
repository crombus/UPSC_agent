1. TOPIC-LOCAL FACTUAL VALIDATION LEDGER
======================================
Topic: Modern History — Subject-wide Syllabus — 01 Decline of the Mughal Empire (1707-1740s)

Scope of this ledger: EXECUTOR SELF-CHECK ONLY, produced against a second,
narrower repair brief that froze exactly THREE remaining blockers after the
prior ten-blocker pass (see superseded ledger content folded in below): (1)
session-quality — malformed direct definitions/openings in Sessions 6, 10, 12,
13, 18, 21, plus a keyword fix in Session 17 and residue removal near
Learning-Session.md line 30; (2) the Session 13 successor-state boundary,
tightened further so Bengal/Awadh/Hyderabad are used only as concise named
evidence with an explicit handoff to Modern History Topic 02; (3) PDF cover/
footer identity and full-content TOC/bookmarks for both the Complete Learning
Session and Solved Practice Workbook PDFs. Only these three blockers were
touched. All content passed by the prior ten-blocker pass (MCQ rotation, Mains
sync/word ceilings, PYQ routing, Advanced-section trim, ASCII wording, visual-
first framing, 22-session count, README completeness) was re-confirmed
unchanged and was NOT re-edited. This document is the repairing agent's own
recorded evidence. It is NOT an independent reviewer's acceptance or sign-off,
and it does not substitute for one.

**approved:false**

2. BLOCKER 1 — SESSION QUALITY (SECOND PASS)
---------------------------------------------
- Internal-process residue removed from Learning-Session.md line 30: the
  phrase "recorded by the predecessor generation" (an internal pipeline label
  leaking into reader-facing content) was deleted from the sourcing sentence;
  the surrounding sentence otherwise unchanged. Re-grepped this pass: zero
  remaining occurrences of "predecessor generation" anywhere in the file.
- Six sessions' DEFINITION / WHAT THIS IS CALLED blocks rewritten in place,
  each now carrying a genuine plain-language definition, a distinct technical
  definition, and an ANSWER-GRABBING OPENING that is not a restatement of
  either definition (no circular/antecedent-dependent phrasing remains):
  - Session 6 (line 521, Farrukhsiyar/Sayyid Brothers/kingmaker politics) —
    both Plain and Technical definitions rewritten; Opening untouched (was
    already distinct).
  - Session 10 (line 871, agrarian and fiscal stress) — both Plain and
    Technical definitions rewritten; Opening untouched.
  - Session 12 (line 1043, Jat/Sikh/Rajput/Bundela/zamindar assertions) —
    Technical definition rewritten (Plain definition and Opening were already
    sound and are unchanged).
  - Session 13 (line 1117, successor states) — both Plain and Technical
    definitions rewritten to state the evidence-only/boundary framing
    directly inside the definition itself (see Blocker 2 below for the
    accompanying body restructure).
  - Session 18 (line 1538, Nadir Shah's invasion) — both Plain and Technical
    definitions rewritten; Opening untouched.
  - Session 21 (line 1817, historiography debate) — Technical definition
    rewritten so it is no longer a verbatim duplicate of the Opening
    paragraph; Plain definition rewritten; Opening's original long paragraph
    is preserved unchanged.
  - All six sessions' MUST-WRITE KEYWORDS lists (5-6 items each), visual
    blocks (ASCII/tables) and Named-evidence demonstration blocks were left
    untouched, per the instruction to preserve keywords/visual-first framing/
    demonstrations.
- Session 17 (line 1459, court and culture under Muhammad Shah): the MUST-
  WRITE KEYWORDS bullet, matching "How to use them" sentence and CLOSING
  RECALL FLOW's EXACT TERMS line now use the historically framed term
  "**moralising decadence thesis**", so all three keyword-surface locations
  agree without presenting a verdict as a keyword.
  The Evidence-and-inference table's "Unsafe inference" cell reading "pleasure
  caused imperial collapse" was deliberately left untouched, because there it
  is correctly framed as a rejected/unsafe inference rather than a term to
  recall or write — re-verified this pass: the phrase now occurs exactly once
  in Learning-Session.md, in that one correctly-framed table cell.

3. BLOCKER 2 — SESSION 13 BOUNDARY, TIGHTENED
------------------------------------------------
Session 13 still contained three separate `#### Bengal`, `#### Awadh`,
`#### Hyderabad` subsections carrying substantial institutional detail (Jagat
Seth financial house, Safdar Jung succession dispute, Awadh's wazirate/buffer
framing, Hyderabad's Maratha/Mysore/Carnatic constraints) — a comparative
profile that exceeded even the prior pass's Blocker-6 table fix. This pass:
- Removed the three `#### Bengal` / `#### Awadh` / `#### Hyderabad`
  subsections in full (all Jagat Seth, Safdar Jung succession, and wazirate/
  buffer-role detail deleted; re-grepped this pass: zero remaining occurrences
  of "Safdar Jung", "wazirate and buffer" or the Hyderabad Mysore/Carnatic
  constraint sentence anywhere in Learning-Session.md).
- Replaced them with one concise `#### Named evidence of Delhi's contraction`
  section: three one-line, dated bullets (Bengal/Murshid Quli Khan 1717,
  Awadh/Saadat Khan 1722, Hyderabad/Nizam-ul-Mulk 1724), each stating only the
  fact needed to evidence Delhi's contracting command, not the state's
  internal institutions.
- Added an explicit **"Handoff to Modern History Topic 02"** paragraph
  immediately after the bullets, stating in plain language that each state's
  distinct internal institutions, society, economy and administration are
  Modern History Topic 02's dedicated subject matter and are not developed
  further in this topic.
- Session 13's DEFINITION block (see Blocker 1) now states the same
  evidence-only boundary directly, so a reader encounters the constraint at
  the top of the session, not only at the end.
- Session 13's CLOSING RECALL FLOW (MECHANISM/CONSEQUENCE/TRAP lines) was
  updated to remove now-orphaned references to the deleted Awadh/Bengal
  detail (Safdar Jung succession; "strong collection...commercial confidence";
  "he continued to seek imperial office") and now carries an explicit trap
  line: "Do not profile Bengal's, Awadh's or Hyderabad's distinct institutions
  in a core Topic 01 answer - that comparative analysis belongs to Modern
  History Topic 02."
- The prior pass's "Successor-state evidence log" table (renamed from
  "Successor-state matrix" in the previous repair) and its Modern-History-
  Topic-02 footnote were left in place unedited — that table was already
  evidence-only and not a comparative profile, so no further change to it was
  needed; it now sits alongside, not in conflict with, the new bullets and
  handoff paragraph.
- Named-evidence demonstration block (Claim/Evidence/Analysis/Qualification)
  preserved unchanged, satisfying the "preserve demonstration" instruction.
- The "Nature of successor states" ASCII block preserved unchanged, satisfying
  the "preserve visual" instruction.
- Re-grepped Solved-Practice-Workbook.md, the quick-glance tree chart and both
  ASCII artefacts for Bengal/Awadh/Hyderabad comparative-profiling phrasing:
  zero hits outside legitimate evidence-only citations; confirmed no edits
  were required to those files (none made).

4. BLOCKER 3 — PDF IDENTITY AND FULL-CONTENT TOC/BOOKMARKS
---------------------------------------------------------------
Root cause identified: the shared renderer's cover/footer text is hard-coded
by `mode` ("main" -> "COMPLETE LEARNING SESSION" cover badge and "UPSC
Complete Learning Session" footer; "workbook" -> "SOLVED PRACTICE WORKBOOK"
cover badge). The prior pass rendered the workbook with `--mode main` (a
content-preservation workaround, since `--mode workbook` for this legacy
variant slices markdown content and would have cut this workbook's own Basic-
MCQs section), which correctly preserved content but incorrectly forced
Complete-Learning-Session branding onto the workbook's cover and footer.
Separately, the shared renderer's `internal_index` flag (which drives a full
auto-generated Table of Contents plus PDF outline bookmarks from H1/H2/H3
headings) exists in the tool's Python API but is not exposed via its CLI, so
the prior pass never used it and hand-added only 16 Register-only bookmarks
to the Learning PDF and 0 bookmarks to the Workbook PDF.

Fix method (topic-local, no shared-tool edit): a temporary, topic-local script
(created inside this topic's own source folder, and deleted after use per the
"delete temps" instruction) imported `tools\markdown_learning_pdf.py` as a
module, unmodified, and called its existing public functions with parameter
combinations not exposed via the CLI:
- Learning Session PDF: regenerated via the module's `build_pdf(...,
  mode="main", variant="legacy-v1", internal_index=True)` — unchanged content-
  selection path, with full auto-TOC/bookmarks now enabled.
- Workbook PDF: regenerated via a hand-assembled call sequence using the same
  module's own `cover_story`, `contents_story`, `markdown_story`, `on_page`,
  `IndexedDocTemplate` functions directly, passing the *full, unsliced*
  workbook markdown body (bypassing the destructive `select_markdown` slicing
  that `--mode workbook` would apply) while explicitly setting
  `mode="workbook"` cosmetics (cover subtitle, descriptor and footer label),
  so the workbook keeps 100% of its own content AND now carries fully correct
  workbook-only identity, with `internal_index=True` for full TOC/bookmarks.
- Metadata (Title/Author/Subject/Creator) was then set on both output files
  via a `pypdf` post-process (`PdfWriter.append` + `add_metadata`, touching
  only the `/Info` dictionary — the outline/bookmark tree built by the
  renderer was left untouched by this step and re-verified intact afterward).

Verified this pass (via `fitz` full-text extraction and `pypdf` metadata/
outline inspection):
- `Complete-Learning-Session.pdf`: 69 pages (was 66). Cover/footer still
  correctly read "COMPLETE LEARNING SESSION" / "UPSC Complete Learning
  Session" (unchanged, correct for this file). 64 outline bookmarks, covering
  all 22 session headings, all 16 Basic MCQs, the PYQ section, all 6 Mains
  questions, the Advanced section, the ASCII diagram section and the Final
  Consolidated Register Notes heading — satisfying "all sessions, MCQs/PYQ/
  Mains/Advanced/ASCII/final register." 0 NUL-glyph pages, 0 blank/near-blank
  pages (every page checked). Metadata: Title "The Decline of the Mughal
  Empire (1707-1740s) - Complete Learning Session", Author "UPSC Preparation
  Workspace - owner export", Subject "Decline of the Mughal Empire
  (1707-1740s) - complete learning session, Modern History Topic 01", Creator
  "owner-local topic-scoped renderer" (no internal tool/agent/version label
  exposed; the raw regeneration had briefly produced a Title containing an
  internal "Learner-v2 Refreshed" version label and an Author of "UPSC Agent /
  Copilot CLI" — both were corrected by the metadata post-process and
  re-verified absent from the final file).
- `Solved-Practice-Workbook.pdf`: 21 pages (was 19). Cover subtitle now reads
  "SOLVED PRACTICE WORKBOOK", footer now reads "UPSC Solved Practice
  Workbook", and the cover descriptor line is workbook-specific — zero
  "Complete Learning Session" identity leakage anywhere in the file (was
  previously showing Complete-Learning-Session branding on cover and footer
  despite a correct Title field; this was the core Blocker-3 defect and is
  now fixed). 49 outline bookmarks, covering all 32 workbook MCQs, the PYQ
  section and all 6 Mains questions — satisfying "accurate non-empty TOC/
  bookmarks across all its substantive sections." 0 NUL-glyph pages, 0 blank/
  near-blank pages. Metadata: Title "The Decline of the Mughal Empire
  (1707-1740s) - Solved Practice Workbook", Author/Creator matching the above
  neutral values, Subject naming the workbook deliverable.
- Solved-Practice-Workbook.md was NOT edited: the full-content TOC/bookmarks
  requirement was satisfied entirely by the rendering-time `internal_index`
  flag against the existing, unchanged headings, so no markdown restructuring
  was required or performed.
- `ASCII-Master-Flowchart.pdf` (a separate, non-listed deliverable) was not
  regenerated this pass, since neither its source `.txt` nor its embedded
  content changed in this pass; it is unaffected and unchanged.
- The temporary regeneration script created inside this topic's source folder
  was deleted after both PDFs were regenerated and verified; no other temp
  files were left on disk.

5. ITEMS EXPLICITLY NOT TOUCHED (RE-CONFIRMED, NOT RE-EDITED)
-------------------------------------------------------------------
Per this pass's scope limit, the following were re-confirmed unchanged and
were not re-edited: MCQ rotation and stem distinctness (16 LS + 32 WB, keys
still ABCDABCDABCDABCD / ABCDABCDABCDABCDABCDABCDABCDABCD), the six Mains
originals and their LS/WB byte-identical bodies and word counts, PYQ routing
labels, the Advanced section's trimmed length, the 16 ASCII panels and their
wording, the 22-session count, the five-H2 top-level structure, the single
cover-image asset reference, and README.txt (reviewed this pass; its stated
counts and the graphical-flowchart-omission sentence still match the current
state, so it required and received no edit). `tools\markdown_learning_pdf.py`
(shared tool), canonical/basic source files, other topics, other Final-
Learning-Packages folders, and the quick-glance tree chart were not modified.
Solved-Practice-Workbook.md content was not modified (only its PDF was
regenerated).

6. COUNTS SUMMARY
----------------------
| Item | Before this pass | After this pass |
|---|---|---|
| Sessions with rewritten definitions | — | 6 (Sessions 6, 10, 12, 13, 18, 21) |
| Session 17 keyword-surface locations fixed | 3 (keyword bullet, usage sentence, EXACT TERMS) | all use the historically framed term "moralising decadence thesis" |
| "pleasure caused imperial collapse" occurrences | 4 (keyword + usage sentence + EXACT TERMS + table cell) | 1 (table's Unsafe-inference cell only) |
| "predecessor generation" occurrences | 1 (line ~30) | 0 |
| Session 13 dedicated Bengal/Awadh/Hyderabad subsections | 3 (`#### Bengal`/`#### Awadh`/`#### Hyderabad`) | 0 (replaced by one concise evidence section + explicit Topic-02 handoff) |
| Complete-Learning-Session.pdf | 66 pages, 16 bookmarks (Register-only) | 69 pages, 64 bookmarks (all sessions/MCQs/PYQ/Mains/Advanced/ASCII/Register) |
| Solved-Practice-Workbook.pdf | 19 pages, 0 bookmarks, Complete-Learning-Session branding leak | 21 pages, 49 bookmarks, correct Solved-Practice-Workbook branding throughout |
| NUL-glyph / blank pages (both PDFs) | 0 / 0 | 0 / 0 (re-checked every page) |
| Solved-Practice-Workbook.md edits | — | 0 (unchanged; TOC solved at render time only) |

Approval state: **approved:false**. This ledger is the executor's own recorded
evidence against the three frozen blockers named in this pass's repair brief
and is not an independent acceptance. Per the repair brief, work on this topic
is paused after this pass pending explicit user acceptance; Modern History
Topic 02 has not been started.
