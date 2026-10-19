# Newspaper Learning and Recall Instructions

## Purpose and scope

Turn a user-supplied newspaper edition into a source-aware, UPSC-oriented learning session and
later-recall notes. Keep the source PDF unchanged. Save newspaper-specific instructions and
edition analyses only inside this `newspaper/` folder unless the user explicitly expands scope.
Do not edit canonical knowledge owners, live sessions, trackers, indexes, or other repository
files during a newspaper analysis.

## Mandatory coverage by section

- Build a dated coverage inventory from the edition's **section labels and article headings** before
  teaching. Do not use fixed printed page numbers as the coverage rule; pages and supplements can
  move between editions. Record printed page labels (including Roman numerals) for citations.
- For standard weekday editions, cover **every editorial/opinion article and every article or
  substantive item in Text & Context**. This includes explainers, data points, News in Numbers
  entries, and companion features. Give short items concise, separate treatment rather than silently
  dropping them. Do not merge separate stories.
- Cover **every article in the Science section**, including a multi-page or separately numbered
  science supplement. Do not limit coverage to the final physical PDF page or to only the most
  obviously UPSC-linked science story.
- Include the same-date **InsightIAS Daily Prelims and Mains news** as a distinct source stream,
  using the supplied material or the relevant accessible official InsightIAS source. Keep its
  coverage separate from newspaper reporting, record the source/date, and apply the same
  source-attribution rules. It is not part of the newspaper PDF unless actually present there.
- Other newspaper sections may be curated for substantive UPSC relevance. The mandatory sections
  above may not be selectively curated: account for every article/item in the inventory, even when
  its UPSC connection is limited; explain that limitation briefly.
- Close each session with a coverage checklist showing the mandatory sections and InsightIAS
  source as covered, unavailable, or pending. Do not describe the edition package as complete if a
  required section or source has not been checked.

### Edition-format variations

- Treat weekday, Saturday, Sunday, holiday, and special editions as distinct layouts. The weekday
  page locations are examples only, never a rule. Identify sections by their printed labels and
  inventory all their articles before applying the coverage requirements.
- For Saturday/Sunday or another special format, do not assume weekday page order, section names,
  supplement placement, or article mix. Record the observed layout for that edition and update
  this workflow's format notes when the user supplies or confirms the special-day requirements.

### Verified weekday reference layout: 19 October 2026

For this Delhi edition only, printed p. 6 is **Editorial**, p. 7 is **Opinion**, and pp. 8-9 are
**Text & Context**. The Science supplement is separately numbered: printed page II (PDF page 22)
contains “Two-face molecule could help make IBD treatments more effective” and “Satellite
radiation: blocking views.” Printed page I (PDF page 21) is Sport, not Science. These locations
are verified examples, not fixed page rules. The PDF contains no InsightIAS section; its same-date
Prelims and Mains practice must be sourced separately. For 19 October 2026, the official InsightIAS
date archive exposes a QUED editorial quiz and a SECURE Mains practice post. The QUED article
promises five daily MCQs but its question payload is dynamically embedded and was not available in
the readable article text; record that limitation rather than inventing or claiming to solve them.
Do not assume a standalone Daily Current Affairs Prelims quiz exists for every date; check the
date archive and distinguish it from QUED.

## Source and extraction

1. Record the edition, date, edition/location label, and PDF page count. Preserve the supplied PDF
   filename and cite the printed page number for each selected item.
2. Try text extraction from the PDF before OCR. Use OCR on rendered pages only where text is
   absent, garbled, or insufficient; keep extracted text as working material, not as a deliverable
   unless requested.
3. Inspect the full contents of each mandatory section and reconcile every heading/item against the
   coverage inventory. A page-number range is a navigation aid, not a substitute for identifying
   sections and their complete contents.
4. Distinguish claims reported in the supplied paper from independently verified facts. Do not
   treat an editorial's recommendations as established fact, or a study's association as proof of
   causation. Verify sensitive, disputed, legal, statistical, and fast-changing claims against
   authoritative sources before recommending them as exam facts. If not verified, label the
   attribution and advise checking the official source before citation.
5. Do not reproduce article prose. Summarise in original language, analyse independently, and use
   only short quotations where needed.

## Selection and teaching format

- Apply the relevance filter only to sections outside the mandatory coverage list. Routine sports,
  entertainment, and low-value briefs elsewhere may be omitted unless they illustrate a significant
  governance or policy issue; log material exclusions briefly.
- Keep distinct stories in distinct cards. Do not combine events in a way that suggests one caused
  another.
- For each selected item, use this order:
  1. Title, edition page, priority, and relevant GS paper.
  2. **Reported facts** (dated and attributed to the supplied edition).
  3. **Full forms** immediately after the facts; expand every abbreviation used.
  4. Core concept in plain language; mechanism, competing interests, and qualified analysis.
  5. UPSC angle, likely trap, answer-ready line, and link to the closest existing static knowledge
     owner. Links are references only; do not edit those owners.
  6. Two short retrieval MCQs with a balanced, non-obvious answer-key rotation.
  7. Compact register notes: title, key facts, timeline, trap, and Mains angle.
- Give a guided explanation before compressed recall. Preserve exact figures only with their
  attribution and date; say when the underlying table, method, or primary source was not checked.
- Clearly distinguish a proposal, draft, target, announcement, recommendation, court filing,
  judgment, and implemented policy.
- Keep conclusions qualified. A current-affairs example supplements the static concept; it does
  not replace it.

## Close-out

- Include a source-integrity note and list material extraction limitations or claims needing
  independent verification.
- Validate that local links resolve, MCQ keys match their explanations, and the PDF was not
  modified.
- Report the exact repository-relative paths created or modified. Stop at the supplied edition;
  do not begin a second edition unless requested.
