# Mandatory Review — 2016 Prelims CSAT Paper II, Series A

**Review date:** 2026-10-05  
**Passes reviewed:** source authentication, transcription, numbering, classification, solution,
calculation, key mapping, linking and final quality  
**Reviewed artifact:** [`papers/2016/prelims-csat.md`](../papers/2016/prelims-csat.md)  
**Reviewed artifact SHA-256:** `8656c60e4248fb5e52d0f439e90e744df0f553a96f7bb7fc0a8bc3acd050a25a`  
**Reviewer conclusion:** **PASS**

## Scope and ownership

This independent review covers the owned 2016 Prelims CSAT paper and this review record. Shared
catalogue, topic, index, routing, status, queue and central review-log files were not edited.

## Sources authenticated

| Purpose | Source | Verification |
|---|---|---|
| Official questions | `books/previous_papers_2013_2018/2016/prelims-csat.pdf` | 40 pages; validated Series-A booklet; exact archived-official capture recorded in `SOURCE-VALIDATION.json`; SHA-256 `ff128d16338395a45ac0337e42ebce7511866fad243a1c7973ef74592da2af4a` |
| Official final key | `books/previous_papers_2013_2018/2016/answer-key-csat.pdf` | Commission final-key table mirrored by IAS Exam Portal; Series A; 200 marks; 80 scored; `NIL` dropped; SHA-256 `33fed0aa9f322b047305b56f8da87376df6c783136a6222e6d534c3416332327` |
| Format precedent | `solved_pyqs/papers/2017/prelims-csat.md` and its review | Three-digit anchors, metadata, routes, canonical owners, full reasoning, shortest-safe methods and explicit key provenance followed |

## Verification results

### 1. Completeness, order and stable identity

- Question anchors: **80**, unique and sequential from `2016-prelims-csat-q001` through
  `2016-prelims-csat-q080`.
- Solution anchors: **80**, unique and sequential.
- Every Series-A item Q1–Q80 occurs once in booklet order.
- Shared directions, all passages, common logic-grid premises, statements, units and 320 options
  are retained.
- OCR residue found during comparison was corrected; no unresolved extraction marker remains.

### 2. Official-final key mapping

- The paper contains **80** `OFFICIAL-FINAL` answers and no dropped, inferred or provisional item.
- Independent comparison with the Series-A Commission table produced **0 mismatches**:

```text
1–10:   C A D D A C D D B D
11–20:  D B D C A C B B C C
21–30:  D B C A D A A D B B
31–40:  B D B B B C B C C D
41–50:  C D A D B D B B B A
51–60:  B D B A B A B A B C
61–70:  D B A A B B D B D C
71–80:  B A A B A D A D C C
```

### 3. Reasoning and arithmetic

- Full-reasoning blocks: **80**; shortest-safe-method blocks: **80**;
  option-elimination/trap blocks: **80**.
- Passage answers were checked against passage-only scope, especially official-key-sensitive Q2,
  Q5, Q23, Q33, Q41, Q48 and Q66.
- Quantitative work was recalculated for percentages, LCM, linear/quadratic equations, bridge
  scheduling, concentrations, weighted averages, work rates, displacement, mensuration,
  permutations, painted cubes, ranks, circular motion, probability and profit/loss.
- Logic grids were reconstructed for Q12, Q15–Q19, Q34–Q36 and Q54–Q56.
- Q78 explicitly records the wording tension between the literal doubled running distance
  (150 m) and the Commission's official-final option (d), 75 m, without altering the official map.

### 4. Metadata, routes, slugs and links

- Metadata rows: **80**; canonical-owner rows: **80**; unique stable slugs: **80**.
- All six relative CSAT topic routes resolve.
- All six referenced canonical Basic-owner files exist under
  `upsc-ai-kit/knowledge/CSAT/basic/`.
- Every solution links back to its exact transcription anchor and to the paper-wise index.
- Family distribution totals **80**:

| Family | Questions |
|---:|---:|
| 01 — Reading Comprehension | 27 |
| 02 — Number Systems and Number Sense | 5 |
| 03 — Arithmetic and Commercial Math | 15 |
| 04 — Rates, Motion, Time and Geometry | 10 |
| 05 — Algebra, Inequalities and Data Sufficiency | 3 |
| 06 — Logical Reasoning, Coding, Counting and Data Interpretation | 20 |

## Defects found and corrected

1. Rebuilt question anchors after detecting that numbered statements inside Q1 could be mistaken
   for question headings.
2. Corrected OCR damage in the sanitation, land-use emissions, diet, soil-carbon and food-security
   passages and restored missing opening directions.
3. Replaced conflicting secondary answer annotations with the Commission's Series-A final key,
   notably Q2, Q11, Q23, Q33, Q38, Q40, Q48, Q52, Q59, Q66, Q77 and Q78.
4. Corrected Q2 reasoning to distinguish the valid first assumption from the unsupported absolute
   second assumption.
5. Rechecked all anchor targets, route files, canonical owners, answer counts and metadata counts.

## Remaining blockers

None within the assigned paper-and-review scope.

## Final verdict

**PASS — owned content contains all 80 Series-A questions in exact order, sequential stable IDs,
official-final key mapping and provenance, complete passage/calculation reasoning, shortest safe
methods, option traps, valid metadata/routes/slugs and resolving owned-scope links.**

## 2026-10-05 shared historical-merit integration addendum

The deferred shared integration is complete. Every routed 2016 anchor now has one canonical topic-page route and one exact reverse link, appears in the year/paper/subject/topic navigation and concentration metadata, and preserves the paper-specific source, marks and provenance qualifications reviewed above.

**Final release conclusion: PASS.**
