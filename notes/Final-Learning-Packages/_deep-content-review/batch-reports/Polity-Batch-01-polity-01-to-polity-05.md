# Polity Deep-Review Batch 01 — polity-01 to polity-05

**Published:** 28 August 2026  
**Scope:** Polity → Subject-wide Syllabus, topics 1–5  
**Batch result:** 5/5 passed substantive re-review; package approval remains separate and false.

## Identity and score summary

| Topic | Title | Baseline identity / score | Final identity / score | Immutable intermediates | Review | Approved |
|---|---|---:|---:|---|---|---|
| `polity-01` | Historical Background | `polity-01:learner-v2:g14` — 80 | `polity-01:learner-v2:g16` — 96 | g15 | passed | false |
| `polity-02` | Making of the Constitution | `polity-02:learner-v2:g14` — 78 | `polity-02:learner-v2:g17` — 97 | g15, g16 | passed | false |
| `polity-03` | Salient Features | `polity-03:learner-v2:g15` — 66 | `polity-03:learner-v2:g18` — 98 | g16, g17 | passed | false |
| `polity-04` | Preamble | `polity-04:learner-v2:g14` — 68 | `polity-04:learner-v2:g18` — 98 | g15, g16, g17 | passed | false |
| `polity-05` | Union and Territory | `polity-05:learner-v2:g14` — 70 | `polity-05:learner-v2:g17` — 98 | g15, g16 | passed | false |

## Recurring issue patterns

- Stale generation identity, titles, source anchors, hashes or in-place-repair metadata.
- Non-strict MCQ key order despite superficially balanced A/B/C/D totals.
- Paraphrased or incomplete PYQ wording, marks/word limits and weak demand decoding.
- Generic model-answer feedback instead of answer-specific, executable improvement.
- Core compression in graphical/ASCII flows, especially PYQ routes and 10/15/20-mark answer spines.
- Brittle constitutional/historical statements presented without doctrinal, temporal or source qualification.
- Prose mutation introduced during semantic extraction or long-form answer-key parsing.

## Systemic pipeline fixes

- Repaired both generation-time and validation-time parsers for long-form bold answer keys.
- Enforced exact graphical source-heading anchors and fresh immutable provenance.
- Added semantic prose-integrity checks to catch malformed quotation/full-stop output.
- Updated strict A→B→C→D audits without global prose mutation.
- Expanded manual ASCII panel totals and aligned graphical/ASCII source ledgers.
- Required re-reading the finalized tracker before each successor allocation and preserved every failed intermediate.

## Artifact and validation summary

- All 20 required final artifacts passed: five learning sessions, five solved workbooks, five graphical masters and five ASCII masters.
- Final topic scores: **96, 97, 98, 98, 98**; mean **97.4/100**.
- Final exports passed page, blank-page, near-empty-page, clipping, replacement-glyph, hash/provenance, MCQ-rotation and cross-artifact controls.
- Exact topic reports, staged records, generation validations and changed-file manifests remain under `reviews\polity-01` through `reviews\polity-05`.

## Immutable review history

- `polity-01`: g14 → g15 → **g16**.
- `polity-02`: g14 → g15 → g16 → **g17**.
- `polity-03`: g15 → g16 → g17 → **g18**.
- `polity-04`: g14 → g15 → g16 → g17 → **g18**.
- `polity-05`: g14 → g15 → g16 → **g17**.

No reviewed generation was overwritten or deleted.

## Approval and next queue

- **Approval:** all five remain `Approval pending`; review pass does not approve a package.
- **Next queue item:** `polity-06:learner-v2:g14` — **Citizenship**.
