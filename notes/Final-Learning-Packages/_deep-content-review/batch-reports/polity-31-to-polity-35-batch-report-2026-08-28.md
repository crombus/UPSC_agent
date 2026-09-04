# Polity deep-review batch report — polity-31 to polity-35

**Published:** 28 August 2026  
**Approval state:** every package remains unapproved; review pass is not package approval.

## Identities, scores and preserved generations

| Topic | Final identity | Score | Preserved history |
|---|---|---:|---|
| `polity-31` — National Commissions SC ST BC | `polity-31:learner-v2:g3` | 98/100 |  |
| `polity-32` — CAG | `polity-32:learner-v2:g4` | 98/100 |  |
| `polity-33` — Attorney General and Advocate General | `polity-33:learner-v2:g5` | 98/100 |  |
| `polity-34` — NITI Aayog | `polity-34:learner-v2:g4` | 98/100 | g2 (72, changes_suggested), g3 (95, failed_manual_review_prose_integrity), g4 (98, passed) |
| `polity-35` — NHRC and SHRC | `polity-35:learner-v2:g5` | 98/100 | g2 (76, changes_suggested), g3 (94, failed_manual_review_prose_integrity), g4 (97, failed_manual_review_acronym_integrity), g5 (98, passed) |

## Recurring issue and fix patterns

- Corrected constitutional/statutory source, appointment, tenure, removal, jurisdiction and enforcement overstatements against primary legal texts.
- Replaced volatile officeholder/count claims with dated-source controls or omitted them where unnecessary.
- Completed Core before Optional Advanced and added answer-specific Why/How guidance with executable compression.
- Expanded compressed nine-stage flows to twelve agreeing graphical/ASCII Core stages.
- Enforced strict `ABCD x12` rotation while preserving option text and explanation prose.
- Preserved technically valid generations that failed manual prose/acronym/ASCII review; no generation was overwritten.

## Validation

- Every final generation passed all seven hard gates and four-artifact reconciliation.
- Targeted generator suite: **38 passed** for each final cycle.
- Final Markdown checks found no ellipsis placeholders, replacement glyphs or malformed acronyms.
- Complete rendered ASCII masters were checked at <=100 columns.
- Locked baseline hashes outside mutable final-library destinations showed zero mismatches.

## Final exports

- `polity-31`: `Polity\Subject-wide Syllabus\31-National-Commissions-SC-ST-BC`
- `polity-32`: `Polity\Subject-wide Syllabus\32-CAG`
- `polity-33`: `Polity\Subject-wide Syllabus\33-Attorney-General-and-Advocate-General`
- `polity-34`: `Polity\Subject-wide Syllabus\34-NITI-Aayog`
- `polity-35`: `Polity\Subject-wide Syllabus\35-NHRC-and-SHRC`
