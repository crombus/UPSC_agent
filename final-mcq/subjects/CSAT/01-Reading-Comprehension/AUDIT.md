# csat-01 — Reading Comprehension: audit record (2026-11-01 option-balance and difficulty pass)

**Scope and status.** This record covers the 2026-11-01 author-only pass over the three revision banks (`revision-1/`, `revision-2/`, `revision-3/`). It records the option-length and letter audit, the key checks, and every changed question ID. **No second reviewer has checked these texts.** The 2026-10-01 independent recheck in `COVERAGE.md` applies only to the earlier texts and is not claimed for the changed items. Topic status remains `in_progress` (see `COVERAGE.md`).

## 1. Method

- **Option-length metric.** For each item, the character length of each of the four option strings was measured. A key is *uniquely longest* when its length is the strict maximum. The ratio is max length ÷ min length. Statement-combination options (for example “1 only”) have inherently short strings, so their ratio is reported but treated as a known limitation (section 6).
- **Letter metric.** Count of keys per letter per set; a sequence check for adjacent repeats.
- **Key verification.** Statement-combination items were checked by a truth table: each statement's truth value is fixed by a quoted passage sentence, the expected combination is derived from those values, and it is matched to the option text and the `ANSWERS.md` key. Every other key was re-derived by hand from the passage sentence cited in its `ANSWERS.md` entry. No numerical content exists in these passages, so no arithmetic check applies.
- **Structural checks.** Each set has one ID per question and one answer entry per ID, in the same order; each question has exactly four options; `QUESTIONS.md` contains no key, rationale or placeholder text (the only hits for “correct” are the time-budget scoring note, a stem word and the option “correctly”).

### Truth-table check (statement-combination items)

```python
# verify_statements.py (summary of the check run on 2026-11-01)
TRUTH = {
  "revision-1": {"R1-Q06": {1: True,  2: True,  3: True},
                 "R1-Q21": {1: True,  2: False, 3: False}},
  "revision-2": {"R2-Q09": {1: True,  2: True,  3: True},
                 "R2-Q20": {1: True,  2: False, 3: True}},
  "revision-3": {"R3-Q09": {1: True,  2: False, 3: True},
                 "R3-Q24": {1: True,  2: True,  3: True}},
}
# combo_text(): all three supported -> "1, 2 and 3"; one -> "k only"; two -> "i and j only".
# PASS if the option text for the expected combination sits at the ANSWERS key letter and the four options are distinct.
```

| Item | Statement truth values (passage anchor) | Expected combination | Letter in file | ANSWERS key | Result |
|---|---|---|---|---|---|
| R1-Q06 | 1 T (“held for review”), 2 T (“stock record must also be checked”), 3 T (“no method for repairing”) | 1, 2 and 3 | A | A | PASS |
| R1-Q21 | 1 T (“could identify the place”), 2 F (“every error should be displayed” disclaimed), 3 F (sale not reported) | 1 only | C | C | PASS |
| R2-Q09 | 1 T (diverging readings), 2 T (refusal of sufficiency), 3 T (vents “possible modifier”) | 1, 2 and 3 | C | C | PASS |
| R2-Q20 | 1 T (three mornings), 2 F (bridge closed after both gauges fell), 3 T (mark records open bridge) | 1 and 3 only | D | D | PASS |
| R3-Q09 | 1 T (advances help buy materials), 2 F (advance not sufficient), 3 T (record delays before promising) | 1 and 3 only | A | A | PASS |
| R3-Q24 | 1 T (less stove time, leisure not established), 2 T (necessary but not enough), 3 T (input vs wider result) | 1, 2 and 3 | C | C | PASS |

Result: **6/6 PASS**; a key that failed the check would have been reported here.

## 2. Before and after: option-length and letter balance

Before = `git HEAD` version; after = this pass. “Uniquely longest” is the brief's primary defect metric.

| Set | Items | Uniquely longest (before) | Uniquely longest (after) | Uniquely shortest (before → after) | Ratio > 1.25 (before → after) | Keys A/B/C/D (before) | Keys A/B/C/D (after) |
|---|---|---|---|---|---|---|---|
| R1 | 24 | 7 (29.2%) | **0 (0.0%)** | 5 → 2 | 7 → 3 | 6/6/5/7 | **6/6/6/6** (25% each) |
| R2 | 25 | 6 (24.0%) | **0 (0.0%)** | 5 → 6 | 6 → 1 | 4/7/7/7 | **6/6/7/6** (24/24/28/24%) |
| R3 | 25 | 12 (48.0%) | **0 (0.0%)** | 3 → 2 | 5 → 3 | 6/6/6/7 | **6/6/6/7** (24/24/24/28%) |

Letter sequences after this pass (no adjacent repeats in any set):

- R1: `ACBDCADBCABDACBDACDBCADB`
- R2: `ACBDCADBCADBACBDACBDCABCD`
- R3: `CADBADBCADBCDABCADBCADBCD`

Residual length exceptions after this pass (listed for transparency, not hidden):

- **Ratio > 1.25 from statement lists:** R1-Q06 (2.00), R1-Q21 (2.00), R2-Q20 (2.00). The shortest option is “1 only”, so the spread is inherent to the combination format.
- **Ratio > 1.25, text options:** R1-Q09 (1.254), R3-Q07 (1.26), R3-Q14 (1.26), R3-Q25 (1.31).
- **Uniquely shortest correct option (not a brief defect; recorded):** R1-Q17, R1-Q18, R2-Q01, R2-Q07, R2-Q09, R2-Q10, R2-Q18, R2-Q21, R3-Q21, R3-Q24. Most margins are 1–10 characters, and no correct option is uniquely longest in any set.

## 3. Changed-ID log

Categories: **Replaced** = new stem and options, same passage (or a new original passage), with a new item type. **Reworked** = options rewritten for length or closer distractors; the key meaning is kept. **Re-lettered** = option text and stem unchanged, only the key letter moved. **Unchanged** = no change in text or letter.

**Revision 1 (24 items; 3 replaced, 16 reworked, 5 re-lettered only, 0 unchanged)**

- Replaced: R1-Q11 (was a stated-detail item on Passage VI; now a strengthener), R1-Q15 (was a textual discriminator on Passage VII; now the archivist's position), R1-Q24 (was a textual discriminator on Passage X; now a weakener of the office's map proposal).
- Reworked: R1-Q01, R1-Q03, R1-Q04, R1-Q07 (tone item rewritten with closer paraphrases), R1-Q08 (phrase-meaning distractors made close), R1-Q09, R1-Q10, R1-Q12, R1-Q13, R1-Q14, R1-Q16, R1-Q17, R1-Q18, R1-Q19, R1-Q20 (distractors made close), R1-Q22.
- Re-lettered only: R1-Q02, R1-Q05, R1-Q06, R1-Q21, R1-Q23.

**Revision 2 (25 items; 5 replaced, 9 reworked, 7 re-lettered only, 4 unchanged)**

- Replaced: R2-Q01 (was a consistency item on Passage I; now a conclusion about the notice's second-day provision), R2-Q12 (was a manager's-reason item on Passage VI; now a weakener of the fabric-training proposal), R2-Q13 (was a stated-detail item on Passage VII; now the clerks' agreed test with close paraphrases), R2-Q15 (was a textual discriminator on Passage I; now a weakener of the first officer's claim), R2-Q25 (was a textual discriminator on Passage X; now a consistency item with the caretakers' stance).
- Reworked: R2-Q02, R2-Q03, R2-Q05, R2-Q07 (tone item with closer paraphrases), R2-Q10, R2-Q11, R2-Q17, R2-Q18, R2-Q23.
- Re-lettered only: R2-Q06, R2-Q09, R2-Q16, R2-Q19, R2-Q20, R2-Q21, R2-Q22.
- Unchanged: R2-Q04, R2-Q08, R2-Q14, R2-Q24.

**Revision 3 (25 items; 3 replaced, 15 reworked, 6 re-lettered only, 1 unchanged)**

- Replaced: R3-Q11 (was a stated-detail item on Passage VI; now the principle behind the refusal to grade), R3-Q15 (was a textual discriminator on Passage VII; now a weakener of the councillor's claim), R3-Q25 (was a textual discriminator on Passage X; now a weakener of the coordination proposal).
- Reworked: R3-Q01, R3-Q02, R3-Q06, R3-Q07 (tone item with closer paraphrases), R3-Q08 (purpose distractors made close), R3-Q10, R3-Q12, R3-Q13, R3-Q14, R3-Q16 (phrase-meaning distractors made close), R3-Q17, R3-Q18, R3-Q19, R3-Q21, R3-Q23.
- Re-lettered only: R3-Q03, R3-Q05, R3-Q09, R3-Q20, R3-Q22, R3-Q24.
- Unchanged: R3-Q04.

**Difficulty pass.** Six items per set (about 25%) were replaced or reworked toward harder inference, assumption, strengthen/weaken and close-paraphrase tone items, with the textual-discriminator items retired. The passages were not changed; no new passage was added, so all passages remain original and within the existing word ranges.

## 4. Per-item verification for replaced items

Each entry records the passage sentence that fixes the key. Reworked items keep their key meaning, and each option's failure reason is written in the matching `ANSWERS.md` entry.

| ID | Key's anchoring sentence (passage) | Why the distractors fail |
|---|---|---|
| R1-Q11 | “When two readings disagree, staff inspect both locations” and “intended to identify variation” (Passage VI) | A: depth, not location; B (key): unflagged variation found; C: whole-field irrigation, the rejected practice; D: sensor replacement, unrelated |
| R1-Q15 | “needed a way to locate the meeting before studying it” (archivist, Passage VII) | A: replacement, not stated; C: withdrawal, which the reviewer opposes; D: no-check citation, which the reviewer demands checking |
| R1-Q24 | “did not test whether a named path remained open after dark” (Passage X, Passage 1) | A and C: need for a map (strengthen); D: universal identification (strengthen) |
| R2-Q01 | “an eligible grower who finds no space may seek entry on a different day; it does not promise space” (Passage I) | B: guarantee not stated; C: list does not decide bays; D: notice concerns eligible growers only |
| R2-Q12 | “provided the discarded pieces resemble the cloth the workers will actually handle” (Passage VI) | Different weight and weave break the resemblance condition (key); A, C, D strengthen the proposal |
| R2-Q13 | “retain personal assistance while testing whether a stable written list reduced omitted attachments” (Passage VII) | B: drops personal help; C: tests translation, not the list; D: “eliminates” overreaches |
| R2-Q15 | “a pass also requires available unloading space”; “a list cannot predict available space” (Passage I) | A: irrelevant; C: strengthens; D: agreement is irrelevant to predictive sufficiency |
| R2-Q25 | “maintaining the newly opened space”; litter's source “did not estimate” (Passage 2) | A: locking rejected; B: shade's effect not shown; C: source not estimated |
| R3-Q11 | “would turn a point of entry into a standard that allowed only one way of looking” (Passage VI) | A: opposite reasoning; C: refuses conditional grading too; D: not drawn in the passage |
| R3-Q15 | “Trees grew in two stretches” and the wall-side heat (Passage VII); the key finding shows benefit on the non-wall stretch | A: other wards; C: walking times; D: restates the councillor's premise |
| R3-Q25 | “reliable deliveries were necessary … yet not enough by themselves” (Passage 2) | A: strengthens space coordination; B, C: irrelevant to coordination |

## 5. Format and related revisions

- **Format.** Question headings were changed from `**ID.**` to `### ID` to match the binding uniform format in `final-mcq/INSTRUCTIONS.md`. Each `QUESTIONS.md` now carries a time budget (about 72 seconds per question) and the scoring note (+2.5 correct, −0.83 wrong, 0 skipped). Each `ANSWERS.md` entry now ends with a shortcut and a time target.

## 6. Limits of this record

- **Author-only.** Nothing in this file is an independent confirmation of the keys or of the difficulty.
- **Statement-list lengths.** Combination options are short by construction; the 2.00 ratios are not closed by padding.
- **Uniquely shortest** correct options remain in ten items, mostly by 1–10 characters; they are recorded, not treated as a brief defect.
- **Difficulty.** The brief's “at least 40% of questions need two or more steps or a trap” is a judgement; the rewritten items were built as two-step or trap items, but no calibration against learner performance exists.
- **Official-PYQ hold.** Unchanged: no exact UPSC item or key is reproduced or verified here (see `COVERAGE.md`).
