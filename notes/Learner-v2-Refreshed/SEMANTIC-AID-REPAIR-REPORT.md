# Learner-v2 Semantic-Aid Repair Report

- Repair ID: `semantic-aid-repair-2026-08-23`
- Date: `2026-08-23`
- Root cause: generated semantic contracts read editorial classification/audit/navigation lines and previously generated aids as teaching prose; the same contaminated values then propagated into definitions, openings, keywords, guidance and closure/flowchart nodes.
- Audit: **39/40** latest learner-v2 topics were affected.
- Unaffected latest topic: `polity-01`
- Geography verification: `geography-03` required repair for three closure-node defects; `geography-04` required repair for duplicated guidance and inadequate keyword blocks.
- Approval: every new generation remains `approved: false`.

## Regenerated packages

| Topic key | Generation | Sessions | Main pages | Workbook pages |
|---|---:|---:|---:|---:|
| `ancient-indian-history-01` | g7 | 9 | 147 | 39 |
| `ancient-indian-history-02` | g7 | 30 | 94 | 19 |
| `ancient-indian-history-03` | g7 | 28 | 89 | 15 |
| `ancient-indian-history-04` | g7 | 21 | 97 | 38 |
| `ancient-indian-history-05` | g7 | 42 | 91 | 13 |
| `ancient-indian-history-06` | g7 | 42 | 82 | 14 |
| `ancient-indian-history-07` | g7 | 46 | 87 | 13 |
| `ancient-indian-history-08` | g7 | 27 | 72 | 13 |
| `ancient-indian-history-09` | g8 | 25 | 111 | 42 |
| `ancient-indian-history-10` | g8 | 35 | 148 | 64 |
| `ancient-indian-history-11` | g8 | 31 | 130 | 56 |
| `geography-01` | g7 | 24 | 62 | 16 |
| `geography-02` | g7 | 29 | 94 | 17 |
| `geography-03` | g3 | 19 | 60 | 21 |
| `geography-04` | g3 | 20 | 77 | 20 |
| `geography-28-human-settlements-and-urbanisation` | g7 | 16 | 64 | 16 |
| `geography-30-primary-economic-activities-agriculture` | g7 | 12 | 66 | 28 |
| `geography-32-industries-and-industrial-regions` | g7 | 8 | 53 | 20 |
| `philosophy-paper-i-indian-philosophy-01` | g8 | 9 | 112 | 35 |
| `philosophy-paper-i-indian-philosophy-02` | g7 | 2 | 63 | 21 |
| `philosophy-paper-i-indian-philosophy-03` | g7 | 2 | 66 | 25 |
| `philosophy-paper-i-indian-philosophy-04` | g7 | 2 | 71 | 28 |
| `philosophy-paper-i-indian-philosophy-05` | g7 | 2 | 56 | 19 |
| `philosophy-paper-ii-philosophy-of-religion-01` | g8 | 13 | 106 | 40 |
| `philosophy-paper-ii-philosophy-of-religion-02` | g7 | 10 | 105 | 40 |
| `philosophy-paper-ii-philosophy-of-religion-03` | g7 | 10 | 63 | 14 |
| `philosophy-paper-ii-philosophy-of-religion-04` | g7 | 1 | 56 | 28 |
| `philosophy-paper-ii-philosophy-of-religion-05` | g6 | 2 | 47 | 24 |
| `philosophy-paper-ii-philosophy-of-religion-06` | g6 | 2 | 45 | 21 |
| `philosophy-paper-ii-philosophy-of-religion-07` | g6 | 2 | 42 | 21 |
| `philosophy-paper-ii-philosophy-of-religion-08` | g6 | 2 | 50 | 25 |
| `philosophy-paper-ii-philosophy-of-religion-09` | g6 | 2 | 52 | 28 |
| `philosophy-paper-ii-philosophy-of-religion-10` | g6 | 2 | 56 | 31 |
| `polity-02` | g9 | 19 | 75 | 17 |
| `polity-03` | g10 | 22 | 76 | 18 |
| `polity-04` | g9 | 20 | 77 | 21 |
| `polity-05` | g9 | 15 | 55 | 14 |
| `polity-06` | g9 | 24 | 68 | 14 |
| `polity-07` | g10 | 27 | 94 | 23 |

## Validation

- Corrected semantic aids and closure nodes: PASS.
- All-latest learner-v2 semantic-quality audit after finalization: PASS.
- Substantive source preservation and predecessor byte hashes: PASS.
- Workbook answer integrity and balanced non-patterned keys: PASS.
- Main/workbook internal indexes and PDF layout/glyph checks: PASS.
- Continuous flowchart master/poster/tiled/editable/previews package: PASS.
- Tracker latest resolution and old-generation retention: PASS.
- Relevant tests passed: 78.

## Machine-readable records

- Defect audit: `upsc-ai-kit\manifests\retrofits\semantic-aid-quality-audit-2026-08-23.json`
- Validation: `upsc-ai-kit\manifests\retrofits\semantic-aid-repair-2026-08-23-validation.json`
- Changed files: `upsc-ai-kit\manifests\retrofits\semantic-aid-repair-2026-08-23-changed-files.txt`
