# Mandatory Review — 2017 Prelims CSAT Paper II, Series A

**Review date:** 2026-10-05  
**Passes reviewed:** source authentication, transcription, numbering, classification, solution,
calculation, key mapping, linking and final quality  
**Reviewed artifact:** [`papers/2017/prelims-csat.md`](../papers/2017/prelims-csat.md)  
**Reviewed artifact SHA-256:** `30a9806326f46b9cc9987f8fb53969681f22b967ec821854b40a6106d36a4854`  
**Reviewer conclusion:** **PASS**

## Scope and ownership

This independent review covers the owned 2017 Prelims CSAT paper and this review record. Shared
catalogue, topic, index, routing, status, queue and central review-log files were not edited.

## Sources authenticated

| Purpose | Source | Verification |
|---|---|---|
| Official questions | `books/previous_papers_2013_2018/2017/prelims-csat.pdf` | 48 pages; cover visibly identifies **Test Booklet Series A** and paper code `AMC-D-CLYS`; archived-official source recorded in `SOURCE-VALIDATION.json`; SHA-256 `f0554f93539f5b697d17d2f2561b481a16376872b26cb25c5f04c99e59700749` |
| Official final key | `books/previous_papers_2013_2018/2017/answer-key-csat.pdf` | UPSC final-key table mirrored by IAS Exam Portal; Series A; 200 marks; `NIL` dropped; 80 scored; SHA-256 `e76315dd7e6156d986a6073bd92f89c294e8b8ffb06050784f44b26b5d7c920f` |
| Format precedent | `solved_pyqs/papers/2018/prelims-csat.md` and its review | Metadata, routes, canonical owners, exact-question backlinks, full reasoning, shortest-safe methods and explicit key provenance reconciled |

## Verification results

### 1. Completeness, order and stable identity

- Question anchors: **80**, unique and sequential from `2017-prelims-csat-q001` through
  `2017-prelims-csat-q080`.
- Solution anchors: **80**, unique and sequential.
- Every Series-A question Q1–Q80 occurs once in booklet order.
- Shared directions, all 30 passages, logic-grid premises, statements, units and 320 options are
  retained.
- Extraction-only defects were checked against the held scan; no unresolved OCR marker remains.

### 2. Official-final key mapping

- The paper contains **80** `OFFICIAL-FINAL` solution answers and no inferred, provisional or
  dropped item.
- Independent sequence comparison against the Series-A final-key table produced **0 mismatches**:

```text
1–10:   C A D B B B A C B C
11–20:  B D C B A B C C C C
21–30:  D C D A D B D C C D
31–40:  D B B B A B A C C D
41–50:  A C B A C D B A B D
51–60:  C D B A B B C A C B
61–70:  C C A C A B B C A B
71–80:  B B D B A B D C D B
```

### 3. Reasoning and arithmetic

- Full-reasoning blocks: **80**; shortest-safe-method blocks: **80**; option-elimination/trap
  blocks: **80**.
- Passage answers were re-read against passage scope, with special attention to close official-key
  calls Q2, Q10, Q27, Q34, Q44 and Q47.
- Quantitative work was independently recalculated for repeated migration, ranks, profit/loss,
  averages, percentages, clock drift/strikes, progressions, mixtures, grid counting, relative
  speed, reversible multiples, skewness, perfect powers, work rates, worst-case draws, painted
  cubes, rainfall, digit reversal, three-dimensional distance and page-digit counting.
- Enumeration checks confirm Q49's four values (`168, 259, 861, 952`) and Q73's maximum remainder
  (`94 = 1 × 49 + 45`).
- Logic arrangements and directed routes were reconstructed for Q9–Q10, Q13–Q15, Q19, Q29,
  Q40, Q50, Q55, Q59–Q60, Q69–Q72 and Q76–Q78.
- Wording-sensitive Q20, Q33 and Q34 explicitly preserve the official-final answer while warning
  against the alternative interpretation.

### 4. Metadata, routes, slugs and links

- Metadata rows: **80**; canonical-owner rows: **80**; unique slugs: **80**.
- All six CSAT topic routes resolve, all canonical Basic-owner paths resolve, every solution
  returns to its exact transcription anchor, and the paper-wise backlink resolves.
- Family distribution:

| Family | Questions |
|---:|---:|
| 01 — Reading Comprehension | 31 |
| 02 — Number Systems and Number Sense | 7 |
| 03 — Arithmetic and Commercial Math | 11 |
| 04 — Rates, Motion, Time and Geometry | 6 |
| 05 — Algebra, Inequalities and Data Sufficiency | 4 |
| 06 — Logical Reasoning, Coding, Counting and Data Interpretation | 21 |

The distribution totals **80**.

## Defects found and corrected

1. Restored the official Q44 wording lost by secondary text extraction: `less than favourable
   macroeconomic conditions` and `a collapse in the growth of productivity`.
2. Corrected extraction-only spacing in `1/3rd`, `5th`, `hope`, and option `(d) None`.
3. Corrected the Family 03 canonical-owner filename to
   `03_Arithmetic-and-Commercial-Math.md`.
4. Rechecked the official-final table directly from the scan after rejecting a conflicting
   secondary web key.

## Remaining blockers

None within the assigned paper-and-review scope. Shared integration was expressly excluded and
remains untouched.

## Final verdict

**PASS — owned content contains all 80 Series-A questions in exact order, stable three-digit IDs,
official-final key mapping, complete passage/calculation reasoning, shortest safe methods,
elimination traps, valid metadata/routes/slugs and resolving owned-scope links.**

## 2026-10-05 shared historical-merit integration addendum

The deferred shared integration is complete. Every routed anchor now uses a canonical topic-page
route, has one exact reverse link, appears in the paper/year/subject/topic indexes and concentration
metadata, and retains the paper-specific source, marks and key qualifications reviewed above. The
2017 tier contains exactly nine merit papers; qualifying Hindi and English remain correctly absent.

**Final release conclusion: PASS.**
