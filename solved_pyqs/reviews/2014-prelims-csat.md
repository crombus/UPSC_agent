# Mandatory Review — 2014 Prelims CSAT Paper II, Series A

**Review date:** 2026-10-05  
**Passes reviewed:** source authentication, transcription, numbering, passages, arithmetic, official-key mapping, anchors, metadata and owned links  
**Reviewed artifact:** [`papers/2014/prelims-csat.md`](../papers/2014/prelims-csat.md)  
**Reviewed artifact SHA-256:** `11aa829f9d35ea04686b0f8cb26b3316acbe5d96bbba25958512d673533e50e4`  
**Reviewer conclusion:** **PASS**

## Scope and ownership

This review covers only the owned 2014 CSAT paper and this dedicated record. Per the no-shared-edits constraint, shared catalogues, topic pages, indexes, status files and the central review log were not edited.

## Sources authenticated

| Purpose | Source | Verification |
|---|---|---|
| Official questions | `books/previous_papers_2013_2018/2014/prelims-csat.pdf` | 48-page Series-A archived-official booklet; SHA-256 `07c55f63516bd9ac9f943d8648430d9974fb9ee1c658b0f8382686acb6d7bed7` |
| Official final key | `books/previous_papers_2013_2018/2014/answer-key-csat.pdf` | Commission final Series-A table; 185 marks; 74 scored; nil dropped; Q70–Q75 blank; SHA-256 `a2ae86a4afbe3d17b6566117b5f181daad5e9174e1b342401b15cb919886960b` |
| Format precedent | `solved_pyqs/papers/2015/prelims-csat.md` and its review | Three-digit anchors, separated transcription/solutions, routes, canonical owners, provenance and full/short/trap blocks followed |

## Independent verification results

### 1. Numbering, completeness and passages

- Question anchors: **80**, unique and sequential `q001`–`q080`.
- Solution anchors: **80**, unique and sequential.
- Every Series-A item occurs once in booklet order.
- All shared directions and passages were checked; Q70–Q75 remain solved but explicitly unscored.
- Graph, table, matrix, embedded-figure, route and bead items retain source-checked textual schematics.

### 2. Official-final key

- **74** scored items and **6** official blanks; no item is marked dropped.
- Q6 preserves the Commission dual answer `B,C`; Q42 preserves `B,D`.
- Independent Series-A map produced zero mismatches:

```text
1–10:  C C D B A B/C D C C B
11–20: B C B C C D B B D B
21–30: B B C B A A D B B A
31–40: C C B B C D B D C B
41–50: C B/D A D B B D C C C
51–60: D C C C C B C A B D
61–69: D D D B A D C B A
70–75: X X X X X X
76–80: C C A C B
```

### 3. Arithmetic and reasoning

- Recomputed LCM/coincidence, arithmetic progressions, sets, percentage change, equal-SP loss, aggregates, per-capita income, clocks, rates, distance, instalments and calendar items.
- Reconstructed ladder, seating, village coordinates, books, cards, routes, professions and classification puzzles.
- Passage answers were checked only against passage content.
- Ambiguity is explicit where the Commission used dual answers; no coaching answer overrides the official table.

### 4. Metadata, routes, anchors and links

- Metadata, canonical-owner and unique-slug records: **80 each**.
- Full-reasoning, shortest-safe-method and elimination/trap blocks: **80 each**.
- All reciprocal question links resolve to exact owned anchors.
- All six CSAT route files and the paper-wise backlink resolve; **160** owned relative links checked.

## Defects found and corrected

1. Restored Series-A order from the held booklet rather than another series’ ordering.
2. Removed secondary-source answer styling and answer leaks from the transcription.
3. Corrected OCR damage in passages, currency, degree notation, spacing and names.
4. Restored the omitted “growth is necessary … but not sufficient” clause.
5. Rebuilt scan-only data/figure items from held page images and corrected the Q41 stem order.
6. Corrected Q13 reasoning to match statements 2 and 3 only.
7. Preserved the official Q6/Q42 dual keys and Q70–Q75 non-scoring status.
8. Rechecked all anchors, slugs, owners, calculations and owned links after fixes.

## Remaining blockers

None within the assigned paper-and-review scope.

## Final verdict

**PASS — owned content contains all 80 Series-A questions in exact order, stable IDs, Commission-final key/provenance, passage-bound reasoning, calculations and shortest safe methods, option elimination/traps, metadata/routes/slugs and resolving owned-scope links.**
