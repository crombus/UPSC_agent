# Mandatory Review — 2018 Prelims GS-I

**Date:** 2026-10-05  
**Passes reviewed:** inventory, transcription, classification, solution, evidence, linking, and final quality  
**Files reviewed:** `solved_pyqs/papers/2018/prelims-gs1.md`  
**Reviewer conclusion:** **PASS**

## Source and key verification

- Held question paper: `books/more_previous_papers/QP-CSP-18-GS-I-C.pdf`
  - SHA-256: `658DDEC60EF69C6DF5695E5F0BEEC92375DC7CC8144C442CBC7A1F1F8333538D`
  - 48 pages; printed code `CYRF-F-TXLI`.
  - Visual cover/footer verification proves it is **Series A** despite the filename suffix `-C`.
- Held final key: `books/previous_papers_2013_2018/2018/answer-key-gs1.pdf`
  - SHA-256: `E1AE9EF3406E37C4B126C543970580903B7F0887BFFC1330F796B29316C048E5`
  - Series-A sheet: 200 marks, 00 dropped items, 100 scored items.
- Automated validation read every displayed answer and compared the complete 100-letter
  sequence against the manually transcribed Series-A grid. Mismatches: **0**.

## Validation results

| Check | Result |
|---|---:|
| Stable anchors | 100, unique, sequential Q1-Q100 |
| Official questions | 100 |
| A-D choices | 400 |
| Official-final answers | 100 |
| Option-by-option checks | 400 |
| Primary classifications | 100 |
| Canonical slugs | 100 |
| Canonical-owner links | 106 links; 76 unique targets |
| Missing canonical-owner targets | 0 |
| Elimination/trap sections | 100 |
| Ambiguity/provenance records | 100 |
| Structural validation errors | 0 |

## Defects found and corrected

1. Corrected the misleading source filename assumption: the held booklet is Series A, not C.
2. Repaired OCR/layout loss in Q2, Q3, Q9, Q21, Q25, Q36, and Q95 against the held scan.
3. Corrected Q1's chronology by separating 1969 recognition from the 1977 statutory
   salary-and-allowance framework.
4. Completed thirteen analyses that had ended at an extraction boundary.
5. Verified all routes against the 2018 routing ledger and all owner paths on disk.

## Scope and blockers

- Shared catalogues, topic files, status files, and the central review log were intentionally not
  edited because this assignment expressly limits ownership to the paper and this review.
- No blocker remains within the two-file assigned scope.
