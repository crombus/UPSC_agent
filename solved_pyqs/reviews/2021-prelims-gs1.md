# Review — 2021 Prelims GS-I Set A

**Review date:** 2026-10-05  
**Scope:** `solved_pyqs/papers/2021/prelims-gs1.md`  
**Conclusion:** **PASS**

## Sources reviewed

- Official local Set-A booklet:
  `books/more_previous_papers/QP-CSP-21-GeneralStudiesPaper-I-121021.pdf`
- Booklet SHA-256:
  `932A5F61B0F623A731C8210645089B70DE2C404489565F446BC0766BD27B2325`
- UPSC answer-key listing: <https://upsc.gov.in/examinations/answer-key>
- Commission endpoint:
  <https://upsc.gov.in/sites/default/files/ANS-CSP-21-GS-I-engl-010622.pdf>
  (currently returns the Commission JavaScript shell in this environment)
- Surviving mirror of the Commission-released four-series scan:
  <https://iasexamportal.com/sites/default/files/upsc-csp-2021-answer-key-gs-paper-1.pdf>
- Key-scan SHA-256:
  `B69CCEAFD3BCF5AFD50F0A6F7B5D49CEB0EC83A8777A641F48CA92D6738BDF83`
- Routing ledger:
  `upsc-ai-kit/knowledge/_PYQ-ROUTING-PRELIMS-2018-2023.md`
- All linked canonical Basic owners and the named primary/canonical evidence families

## Official-key provenance review

**PASS.** The retrieved four-page scan identifies `CIVIL SERVICES (P)-2021`, General Studies
Paper-I, Series A-D, 100 questions, one dropped question and 99 questions taken for scoring. Its
metadata records an HP scan created on 30 May 2022 and modified on 7 June 2022. The official local
booklet cover prints Series A and code `BXC-U-FTHI`; therefore the Series-A sheet controls.

The Series-A sheet was read directly. All recorded outcomes reconcile to it. Q80 is
**DROPPED (X)**, and the paper does not substitute an inferred or coaching answer.

## 100/100 reconciliation

- Official printed questions: **100**
- Questions reproduced: **100**
- Printed order: **Q1-Q100, continuous**
- Stable anchors: **100 unique**
- A-D options reproduced: **400**
- Answer/status blocks: **100/100**
- Official-final outcomes: **100** (**99 scored; Q80 dropped**)
- Evidence anchors: **100/100**
- Confidence and ambiguity blocks: **100/100**
- Primary classifications and proposed slugs: **100/100**
- Unique proposed slugs: **100**
- Canonical-owner links: **102 across 100 questions**
- Canonical-owner links resolving locally: **102/102**
- Cross-routed questions preserved: **2**
- Official Series-A distribution:
  **A=22, B=31, C=22, D=24, X=1**

## Wording and option review

**PASS — 100/100.** Every stem, numbered statement/pair and A-D option was checked against the
English pages of the 48-page official local Set-A booklet. A normalized token-coverage comparison
was run question-by-question against all 21 English question pages. The two lowest OCR-coverage
items, Q36 and Q50, were manually checked against printed pages 19 and 23 and matched exactly.

This pass corrected one source-fidelity defect in Q78: the transcription now preserves the
booklet's printed spelling, **“N. Gopalaswamy Iyengar Committee”**, rather than silently
normalizing the name. No replacement character, bilingual-column intrusion or page furniture
remains.

## Key, evidence and ambiguity review

**PASS — 100/100.** All 99 scored answers match the official-final Series-A sheet. Q80 alone is
marked `X`; its learning analysis is explicitly separated from the official scoring outcome.

Every question contains statement or option evaluation, elimination logic, an examiner trap, a
named evidence family, answer provenance, confidence and ambiguity treatment. The official sheet
controls close secondary-source conflicts, including Q2, Q25, Q53, Q78, Q81 and Q88. Their
reasoning was checked for consistency with the official outcome and the applicable statutory,
constitutional, geographical or scientific evidence. No unresolved material ambiguity remains
for a scored question.

## Route, slug and anchor review

**PASS — 100/100.** Every question has one stable `2021-prelims-gs1-qNN` anchor, the routing
ledger's primary subject and neutral subtopic, resolving canonical Basic-owner link(s), a narrow
proposed slug and a paper-index backlink. All 403 repository-relative Markdown links in the paper
resolve locally. Anchor duplicates, slug duplicates and missing canonical owners are zero.

No shared catalogue, topic, status or review-log file was edited in this expressly owned pass.

## Mechanical checks

- Question headings: **100/100**
- Stable anchors: **100/100**; duplicates: **0**
- Answer blocks: **100/100**
- Provenance blocks: **100/100**
- Option labels: **A=100, B=100, C=100, D=100**
- Official-key reconciliation mismatches: **0**
- Q80 dropped markers: **1 controlling answer marker**
- Canonical-owner links missing: **0**
- Broken repository-relative Markdown links: **0**
- Duplicate proposed slugs: **0**
- Replacement characters/OCR residue: **0**

## Defects found and corrected

1. **Q78 source fidelity:** restored the exact booklet spelling
   `N. Gopalaswamy Iyengar Committee`.

## Remaining blockers

None within the expressly owned paper-and-review scope.

## Reviewer conclusion

**PASS — release-grade within the owned scope; 100/100 exact Set-A questions/options,
authenticated official-final outcomes, Q80 drop handling, evidence, ambiguity, routes, slugs and
unique anchors reviewed.**

## Shared release integration — 2026-10-05

- Canonical primary routes were normalized against the released corpus taxonomy.
- Exact reverse links were added to shared topic pages and all four catalogues.
- Anchor, link, count, marks, duplicate, TODO/OCR and provenance checks passed.
- **Remaining blockers:** None.
- **Release conclusion:** **PASS — Complete.**
