# Deep Content Review — Medieval History 23: The Marathas, Shivaji & Aurangzeb's Deccan; Jagirdari Crisis

- **Status:** the seven frozen ledger defects below (user-issued, this pass) are
  repaired. This report **supersedes** the immediately-preceding version of this
  file, which claimed "nine frozen acceptance blockers surgically repaired" and
  implied a clean final state; that claim was itself inaccurate for several
  artifacts (workbook cover tagline, workbook register-notes/index, ASCII title
  clipping, graphical approval/generation/master-row metadata, README page/panel
  counts). Those earlier "g4" figures and closure claims for the affected items
  are **historical and superseded** by the facts in this report.
- **Approved:** false — executor self-check only, pending independent human
  review. Nothing in this report should be read as independent acceptance.
- **Prior records:** all prior `medieval-indian-history-23-*` audit/lock/recheck
  JSON files and the previous `REVIEW-REPORT.md` narrative in this folder are left
  unedited as a historical record; nothing in this pass altered them.

## Seven frozen ledger items — closure evidence (this pass)

1. **Workbook cover tagline fixed.** Page 1 of `Solved-Practice-Workbook.pdf`
   previously showed the shared renderer's hardcoded default tagline
   ("UPSC complete learning session | Foundation to advanced | Concepts,
   evidence, practice and answer writing") under "SOLVED PRACTICE WORKBOOK" —
   copied from the Learning Session PDF, not workbook-specific. Rebuilt via the
   shared `tools/markdown_learning_pdf.py` `build_pdf()` public API (not
   edited) passing an explicit, workbook-specific `cover_descriptor`
   ("UPSC solved practice workbook | Foundation to advanced | MCQs, PYQs and
   model Mains answers for exam application") and `footer_label`
   ("UPSC Solved Practice Workbook"). Verified: page 1 text now reads the new
   descriptor; the phrase "complete learning session" no longer appears
   anywhere in the PDF; the running footer is "UPSC Solved Practice Workbook"
   throughout, distinct from the Learning Session PDF's own footer.
2. **Workbook register notes / index restored.** The shared renderer's
   `select_markdown()` (legacy variant, `mode="workbook"`) truncates any
   workbook markdown at a "register notes" heading — a heuristic written for
   combined-document workflows that incorrectly clipped Topic 23's own
   standalone `## CONSOLIDATED REGISTER NOTES (WORKBOOK SUMMARY)` section
   (`Solved-Practice-Workbook.md:587-605`), so it was absent from the PDF's
   text, table of contents and PyMuPDF bookmarks. Rebuilt with a local,
   process-scoped monkeypatch of `select_markdown` (in effect only for this
   one build call; `markdown_learning_pdf.py` itself was not edited on disk;
   every other topic's build is unaffected) that returns the workbook markdown
   unchanged for `mode="workbook"`. Verified: PDF now has **17 pages** (was
   16) and **11 TOC/bookmark entries** (was 9), the new final entry being
   "CONSOLIDATED REGISTER NOTES (WORKBOOK SUMMARY)" at page 17; full-text
   extraction (53,650 characters, was 50,058) confirms the section's content
   is present; 0 blank/near-empty pages.
3. **ASCII master flowchart PDF rebuilt; clipping/sync fixed.** The previous
   PDF truncated its 103-character title line at "...JAGIRDARI CRI" (omitting
   "SIS (16 panels)") and its total extractable text (10,374 chars) was ~30
   chars short of the canonical standalone `.txt` (10,404-char body, sha256
   `b0eb3c6a61881d525322c2be073fcc9932c95d8d2b92f70014ab227a2ed31f30` for the
   full 10,413-char file including fence markers — the `.txt` and the fenced
   block embedded in `Learning-Session.md` remain byte-identical and were not
   touched). Rebuilt with a fresh, Topic-23-local ReportLab Platypus script
   (`Preformatted` blocks in Courier 8.3pt inside `KeepTogether` groups, so no
   panel splits across a page, on normal-size A4 portrait pages) reading
   directly from the untouched `.txt`. Verified: the full 103-character title
   line is present in the PDF's extracted text with no truncation; every
   non-blank source line's stripped content is verifiably present verbatim in
   the PDF extract (0 missing lines); PDF is now 3 pages with 8/6/2 panels and
   4,541/5,040/808 extractable characters per page (10,389 total — the
   15-character gap versus the 10,404-char source body is Preformatted-to-text
   whitespace/line-join behaviour at panel boundaries, not lost content); 0
   blank pages.
4. **Graphical artifacts' internal workflow metadata removed.** The shared
   `tools/carvaka_flowchart.py` unconditionally bakes an amber
   "Approval: FALSE • Pending user review • source generation g4 ..." status
   line plus an "APPROVAL / REVIEW" legend chip into every freshly rendered
   master canvas (`author_topic_spec`/`render_master`, no parameter to
   suppress it), and unconditionally draws "same master rows N-M of H" into
   every tiled-PDF tile footer (`build_tiled`, likewise no suppressing
   parameter). Fixed without invoking those two functions (which would have
   re-baked the same forbidden text) and without editing the tool: the
   already-rendered `High-Resolution-Master.png` was redacted in place
   (Pillow, exact pixel box x:795-4670/y:295-420, filled with the surrounding
   header colour; verified 6,029 amber px inside the box pre-redaction and 0
   amber px inside it post-redaction, with 0 amber px in the surrounding
   strips both before and after, confirming no bleed into the legitimate
   "PRIMARY CORE FLOW"/"SUBORDINATE EXTRA" legend chips); `build_poster()` and
   `build_tiled()` (public API, not edited) were then called fresh against the
   redacted master with identical dimensions/title, reproducing byte-identical
   tile crop geometry (rows 0-3234/2196-5430/4391-7625/6586-9820/8782-12016,
   overlaps 1038/1039/1039/1038 px against the renderer's 330px floor) to the
   previously validated build; each tile PDF's footer was then further
   redacted (PyMuPDF `add_redact_annot`/`apply_redactions`) to remove only the
   "same master rows N-M of H " clause, leaving "`<title>` • TILE n/5 •
   continues below"/"end". Previews and the contact sheet were regenerated
   fresh via `render_previews()`. Verified: full-text scan of all 5 tiled
   pages for "Approval", "generation g" and "master rows" returns no hits;
   direct pixel-crop inspection of the redacted header region shows a clean,
   uniform fill with no visible seam; the substantive rail and both remaining
   legend chips are unchanged. See `03-Graphical-Flowchart/VALIDATION-REPORT.txt`
   (rewritten this pass) for full figures.
5. **README corrected to actual output metrics.** `README.txt` previously
   claimed a "6-page print set" for the tiled PDF and "one panel per page" for
   the ASCII PDF. The tiled PDF has always been 5 pages (unchanged by this
   pass); the ASCII PDF is now 3 pages holding 16 panels (8/6/2 per page,
   item 3 above). `README.txt` lines 16-19 rewritten to state "5-page print
   set" and "16 panels across 3 normal pages" respectively; no other README
   wording changed.
6. **This report and `03-Graphical-Flowchart/VALIDATION-REPORT.txt` rewritten**
   with current, post-repair facts only, after items 1-5 above were completed.
   PDF metadata neutralised locally (PyMuPDF `set_metadata` + `saveIncr`, no
   shared-tool edit): `Complete-Learning-Session.pdf` and
   `Solved-Practice-Workbook.pdf` previously had `Author: "UPSC Agent /
   Copilot CLI"`; both now have `Author: ""` (Title/Creator/Producer left as
   the renderer's existing generic values — Title is descriptive topic text,
   Creator was already `(unspecified)`, Producer is the standard ReportLab
   signature). `ASCII-Master-Flowchart.pdf` was rebuilt this pass with
   `Author: ""` from the start. `At-a-Glance-Poster.pdf` and
   `Printable-Tiled-Version.pdf` already had `Author: "anonymous"` before this
   pass and needed no metadata change. Current metadata, verified this pass:

   | PDF | Pages | Author | Title |
   |---|---:|---|---|
   | Complete-Learning-Session.pdf | 70 | `""` | Medieval History Topic 23 - ... - Learning Session |
   | Solved-Practice-Workbook.pdf | 17 | `""` | Medieval History Topic 23 - ... - Solved Practice Workbook |
   | ASCII-Master-Flowchart.pdf | 3 | `""` | ASCII Master Flow -- Topic 23: ... |
   | At-a-Glance-Poster.pdf | 1 | `anonymous` | THE MARATHAS, SHIVAJI AND AURANGZEB'S DECCAN; THE JAGIRDARI CRISIS |
   | Printable-Tiled-Version.pdf | 5 | `anonymous` | ... — tiled |

   Historical claims in the immediately-preceding version of this report and
   of the graphical validation report that stated these items were already
   correct are explicitly marked **superseded** by this table and by item 4
   above, rather than silently overwritten. `approved: false` throughout —
   this remains an executor self-check, never an independent acceptance.
7. **Tracker-disclosure statement corrected.** The immediately-preceding
   version of this report did not mention `MASTER-TRACKER.md` at all, and the
   preceding graphical validation report claimed "no prior artifact outside
   Topic 23's own graphical/ASCII/PDF/Markdown deliverables was touched" —
   which, taken literally, omitted the one file the user had explicitly
   permitted to be touched. For the record: the user separately, explicitly
   permitted a **one-row path update** to Topic 23's existing row in
   `notes/Final-Learning-Packages/MASTER-TRACKER.md` (row 23) in an earlier
   pass, before this repair. That row's four asset links already point at the
   current folder names (`.../23-The-Marathas-Shivaji-and-Aurangzebs-Deccan-Jagirdari-Crisis/...`,
   graphical subfolder `03-Graphical-Flowchart`, no opaque hash, no "Carvaka"
   naming) — i.e. the permitted one-row link update is already reflected and
   the corresponding old/renamed folder is absent from the repository. This
   pass made **no further edit** to `MASTER-TRACKER.md`; the diff between the
   tracker's current state and its state before that one permitted update is
   limited to Topic 23's single row, and no other row or tracker-wide content
   was ever touched. This disclosure does not extend to, and makes no claim
   about, any other topic's tracker row.

## Post-repair artifact facts

- Files changed this pass (all under this Topic 23 package only):
  - `02-Solved-Practice-Workbook/Solved-Practice-Workbook.pdf` (regenerated —
    items 1, 2, 6)
  - `04-ASCII-Master-Flowchart/ASCII-Master-Flowchart.pdf` (regenerated — item 3)
  - `03-Graphical-Flowchart/High-Resolution-Master.png` (in-place pixel
    redaction — item 4)
  - `03-Graphical-Flowchart/At-a-Glance-Poster.pdf` (regenerated — item 4)
  - `03-Graphical-Flowchart/Printable-Tiled-Version.pdf` (regenerated +
    footer redaction — item 4)
  - `03-Graphical-Flowchart/Contact-Sheet.png` and `03-Graphical-Flowchart/previews/*.png`
    (regenerated — item 4)
  - `03-Graphical-Flowchart/VALIDATION-REPORT.txt` (rewritten — items 4, 6)
  - `README.txt` (lines 16-19 corrected — item 5)
  - `01-Complete-Learning-Session/Complete-Learning-Session.pdf` (Author
    metadata neutralised only — item 6)
  - `_deep-content-review/reviews/medieval-indian-history-23/REVIEW-REPORT.md`
    (this file — items 6, 7)
  - No owner Markdown source file was edited this pass (both
    `Learning-Session.md` and `Solved-Practice-Workbook.md` were already
    correct and complete; only their rendered PDFs needed fixing).
  - No shared tool under `tools/` was edited. No file under Topic 24 or any
    other topic was touched. `MASTER-TRACKER.md` was not further edited (see
    item 7).
- Complete Learning Session PDF: 70 pages, 23 TOC/bookmark entries, 137,543
  extractable characters, 0 blank pages, `Author: ""` (only change this pass).
- Solved Practice Workbook PDF: 17 pages, 11 TOC/bookmark entries, 53,650
  extractable characters, 0 blank pages, workbook-specific cover tagline and
  footer, register notes present and bookmarked, `Author: ""`.
- ASCII Master Flowchart: standalone `.txt` unchanged (10,413 chars incl.
  fence markers); PDF rebuilt, 3 pages, 16 panels (8/6/2), full title present,
  no clipped/missing substantive lines, `Author: ""`.
- Graphical Flowchart: master/poster/tiled/previews/contact sheet regenerated
  per item 4; stage content, rail and both remaining legend chips unchanged;
  full details in `03-Graphical-Flowchart/VALIDATION-REPORT.txt`.

## Known limitations

- This report reflects the executor's own checks against locally generated
  files only; it is not an independent-reviewer acceptance.
- Items outside the seven-item frozen ledger (passed content, MCQs, Basic
  coverage, and visuals beyond the exact defects listed) were deliberately not
  revisited in this pass, per the user's explicit scope instruction.
- The tracker disclosure in item 7 is limited to Topic 23's own row; it makes
  no claim about the tracker's state for any other topic.

## Completion record (this repair pass)

- Validated after regeneration: PyMuPDF page/TOC/character/blank-page checks
  on all five Topic 23 PDFs; full-text scan of the tiled PDF for forbidden
  workflow phrases (none found); pixel-level before/after redaction check on
  the master PNG; tile-overlap and crop-geometry re-check against the
  previously validated figures (unchanged); README wording cross-checked
  against the regenerated ASCII/tiled page counts.
- **Approved: false.**
