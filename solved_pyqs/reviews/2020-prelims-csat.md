# Review — 2020 Prelims CSAT Paper II, Set A

**Review date:** 2026-10-05  
**Reviewed artifact:** [`papers/2020/prelims-csat.md`](../papers/2020/prelims-csat.md)  
**Reviewed artifact SHA-256:** `e0f61633bbfff0eb10b70fcbfc42d244c38842dea2b6afc2cf3a7a61c5d9cfc7`  
**Reviewer conclusion:** **PASS**

## Scope and ownership

This was an isolated review of the 2020 CSAT paper. No shared catalogue, routing, status,
topic-owner or repository review-log file was edited.

## Sources authenticated

| Purpose | Source | Verification |
|---|---|---|
| Official questions | `books/more_previous_papers/CSP_2020_GS_Paper-2.pdf` | Paper code `HGY-D-LKUV/59A`; SHA-256 `650127032df8feab3bb4798ae18417b731d43ce633461740ad726747c7128e3c` |
| Official final key | UPSC `AnsKey-CSP-20-Paper-II-091121.pdf` | Scan identifies `CS(P)-EXAMINATION-2020`, General Studies Paper II, Set A, 80 items, nil dropped; SHA-256 `c3caeb68315b9cf52ab72f69af300d72b9403dc133e5528764ef291da4161967` |
| Canonical routing | `upsc-ai-kit/knowledge/_PYQ-ROUTING-CSAT-2018-2023.md` | All 80 neutral types and family assignments reconciled exactly |
| Canonical owners | CSAT Basic owners 01–06 | Every owner path and topic link resolves |

## Verification results

### 1. Completeness and transcription fidelity

- Questions Q1–Q80 occur exactly once and in official order.
- All 80 stems and all 320 options were checked against the official booklet.
- All 25 comprehension passages were checked for wording and attached to the correct questions:
  Q1–Q6, Q21–Q27, Q41–Q46 and Q61–Q66.
- Formula-, symbol- and table-sensitive items were visually rechecked against the scan:
  Q11, Q18, Q34, Q50, Q51, Q52, Q57 and Q74.
- Decimal points replace the booklet's centred decimal dots without changing any value.
- No unreadable-OCR placeholder, omitted figure, uncertain transcription or duplicated question remains.

### 2. Final-key authentication

- The paper contains 80 `FINAL` answers.
- The answer sequence matches the Commission's Set-A table exactly:

```text
1–10:   D A C A B C A B C A
11–20:  B B C B C C C A B C
21–30:  B A C A B C D C D C
31–40:  D A C B B D C A C D
41–50:  D B C D C D D D D C
51–60:  D D B B C A C B C A
61–70:  C C A C C B D C C B
71–80:  A B B D A D D C A B
```

- The Commission recorded **nil dropped**; the solved paper does not mark any item as dropped,
  inferred or unofficial.

### 3. Solutions and shortest safe methods

- Every question has one full reasoning block and one shortest-safe-method block.
- Arithmetic, algebra, divisibility, averages, ratios, work-rate, speed, geometry, counting,
  coding, calendar, data-sufficiency and logical-deduction calculations were independently
  recomputed.
- Formula-sensitive calculations were confirmed, including:
  - Q11 symbol equation: `⊗ = 3`;
  - Q16 constrained addition: `|A − D| = 3`;
  - Q50 negative powers: maximum `81`;
  - Q51 greatest common measure: `1 3/4 m`;
  - Q57 fractional ratio: `6:9:10`, difference `₹400`;
  - Q72 four-leg average speed: `48v/25`;
  - Q80 final-jump rule: `29` jumps.
- Reasoning questions explain the decisive constraint and, where material, why competing
  options fail.
- No shortest method relies on an unsafe approximation, answer-shape cue or unsupported trick.

### 4. Comprehension fidelity

- Every comprehension answer is justified only from its passage.
- Added prescriptions, reversed causality, unsupported absolutes and over-broad conclusions are
  explicitly rejected where they form the close-option trap.
- No solution imports outside factual knowledge to override the passage.
- Shared-passage questions retain the full passage so that every solved item remains independently
  usable.

### 5. Classification and link integrity

- Stable anchors: **80**, unique and sequential from
  `2020-prelims-csat-q01` to `2020-prelims-csat-q80`.
- Slugs: **80**, all unique.
- Metadata rows: **80**.
- Canonical-owner rows: **80**.
- Routing reconciliation: **80/80 exact matches** with the read-only routing ledger.
- Family distribution reconciles to 80:

| Family | Questions |
|---:|---:|
| 01 — Reading Comprehension | 25 |
| 02 — Number Systems and Number Sense | 17 |
| 03 — Arithmetic and Commercial Mathematics | 11 |
| 04 — Rates, Motion, Time and Geometry | 8 |
| 05 — Algebra, Inequalities and Data Sufficiency | 7 |
| 06 — Logical Reasoning, Coding, Counting and Data Interpretation | 12 |

- All six topic links and the paper-wise backlink resolve as repository-relative Markdown paths.

## Defect disposition

No material defect was found in the reviewed hash. Counts, transcription, authenticated keys,
calculations, passage-only reasoning, routes, families, slugs, anchors and links all pass.

## Final verdict

**PASS — no blocker remains in the isolated 2020 Prelims CSAT paper or this mandatory review.**

## 2026-10-05 shared release addendum

- The parent release pass normalised this paper to canonical topic pages and added exact reverse links for every stable anchor.
- Paper-wise, year, subject and topic indexes now include the paper with reconciled counts and represented marks.
- The earlier shared-integration constraint is resolved; no paper-level finding or source qualification was weakened.
- **Shared release conclusion:** **PASS — no blocker remains.**

