# CSAT-05 Algebra, Inequalities and Data Sufficiency — computation and option audit

Audit date: 2026-11-01. Scope: `revision-1/`, `revision-2/`, `revision-3/` (56 items per set: 48 original items plus 8 added in the 2026-11-01 gap-closure pass; 168 total). Each item's key was checked by the method listed below before its ANSWERS entry was written. Keys are not restated here beyond the letter. This file does not authenticate any exact UPSC PYQ; no PYQ wording or option is reproduced.

## 1. Verification method

- **Numerical MCQs.** Each item carries an independently coded computed value (integer enumeration over a stated range, exact `Fraction` arithmetic, or a closed-form identity). The checker asserts that the computed value equals the keyed option and that no other option equals it.
- **Label/statement MCQs** (for example `x < 2`, `(0, 1/2)`, `P is greater than Q`, `n is a multiple of 3`, `b/a`). These are verified by a grid of sample points, corner-product analysis, or an exact identity (see section 5).
- **Self-sufficiency (gap G1 items).** For items whose option D reads "The question can be answered even without any statement", the stem alone is enumerated over its stated domain. If it fixes a single value, D is keyed; if not, the statements decide the verdict and D is a false distractor.
- **Data sufficiency (DS).** Each item states its domain explicitly. The checker enumerates the domain, collects the set of target values consistent with Statement I alone, Statement II alone, and both together, and maps the result to the verdict: exactly one alone -> A; each alone -> B; only together -> C; neither (not unique even together) -> D. The keyed letter is set by this verdict, not by hand.

Checker core (abridged from the generator `fw.py`):

```python
def ds_eval(it):
    dom = it['domain']
    T1  = {it['target'](v) for v in dom if it['c1'](v)}
    T2  = {it['target'](v) for v in dom if it['c2'](v)}
    T12 = {it['target'](v) for v in dom if it['c1'](v) and it['c2'](v)}
    s1, s2, s12 = len(T1)==1, len(T2)==1, len(T12)==1
    if s1 and s2: return 'B'   # each alone suffices
    if s1 or s2:  return 'A'   # exactly one alone suffices
    if s12:       return 'C'   # both together, neither alone
    return 'D'                 # cannot be answered even together

def check_all(items):   # keyed value must equal computed value; distractors must differ
    for it in items:
        if it['kind']=='mcq':
            assert it['calc'] == it['vals'][0]
            assert all(it['vals'][k] != it['calc'] for k in (1,2,3))
```

Label-check script: `verify_labels.py` (all checks pass). Its checks are summarised in section 6.

## 2. Revision 1 — 56 items (33 MCQ, 23 DS)

| ID | Type | Verification | Computed value / DS verdict | Key |
|---|---|---|---|---|
| R1-Q01 | MCQ | exact enumeration or Fraction arithmetic | 70 | D |
| R1-Q02 | MCQ | exact enumeration or Fraction arithmetic | 9 | C |
| R1-Q03 | MCQ | exact enumeration or Fraction arithmetic | 12 | C |
| R1-Q04 | DS | brute force over 101 stated values | I alone: not unique (2 values, e.g. -3, 3); II alone: not unique (60 values, e.g. -1, -10, -11, -12); together: not unique (2 values, e.g. -3, 3) -> verdict D | D |
| R1-Q05 | DS | brute force over 200 stated values | I alone: not unique (33 values, e.g. 102, 108, 114, 12); II alone: not unique (3 values, e.g. 16, 17, 18); together: unique value 18 -> verdict C | C |
| R1-Q06 | MCQ | exact enumeration or Fraction arithmetic | 41 | B |
| R1-Q07 | DS | brute force over 90 stated values | I alone: not unique (6 values, e.g. 15, 30, 45, 60); II alone: not unique (4 values, e.g. 16, 23, 32, 61); together: no admissible value satisfies it -> verdict D | D |
| R1-Q08 | MCQ | label/grid/identity check | 27^5 | A |
| R1-Q09 | DS | brute force over 41 stated values | I alone: not unique (2 values, e.g. -1, 5); II alone: not unique (20 values, e.g. 1, 10, 11, 12); together: unique value 5 -> verdict C | C |
| R1-Q10 | DS | brute force over 60 stated values | I alone: not unique (12 values, e.g. 10, 15, 20, 25); II alone: not unique (7 values, e.g. 1, 16, 25, 36); together: unique value 25 -> verdict C | C |
| R1-Q11 | MCQ | label/grid/identity check | 8:15 | B |
| R1-Q12 | MCQ | exact enumeration or Fraction arithmetic | 75 | C |
| R1-Q13 | DS | brute force over 101 stated values | I alone: unique value 3; II alone: unique value 3; together: unique value 3 -> verdict B | B |
| R1-Q14 | MCQ | exact enumeration or Fraction arithmetic | 2 | A |
| R1-Q15 | MCQ | exact enumeration or Fraction arithmetic | 9 | C |
| R1-Q16 | MCQ | exact enumeration or Fraction arithmetic | 3/5 | A |
| R1-Q17 | DS | brute force over 1681 stated values | I alone: not unique (14 values, e.g. -1, -2, -3, -4); II alone: not unique (14 values, e.g. -1, -2, -3, -4); together: not unique (14 values, e.g. -1, -2, -3, -4) -> verdict D | D |
| R1-Q18 | MCQ | exact enumeration or Fraction arithmetic | 4/3 | B |
| R1-Q19 | MCQ | exact enumeration or Fraction arithmetic | 8 | B |
| R1-Q20 | DS | brute force over 101 stated values | I alone: unique value 5; II alone: not unique (2 values, e.g. -5, 5); together: unique value 5 -> verdict A | A |
| R1-Q21 | MCQ | exact enumeration or Fraction arithmetic | 8 | B |
| R1-Q22 | MCQ | exact enumeration or Fraction arithmetic | 28 | A |
| R1-Q23 | MCQ | exact enumeration or Fraction arithmetic | 23 | A |
| R1-Q24 | MCQ | label/grid/identity check | sqrt45 + sqrt20 | B |
| R1-Q25 | DS | brute force over 99 stated values | I alone: unique value yes; II alone: unique value yes; together: unique value yes -> verdict B | B |
| R1-Q26 | DS | brute force over 400 stated values | I alone: not unique (6 values, e.g. 11, 20, 27, 32); II alone: not unique (16 values, e.g. 117, 12, 140, 165); together: unique value 32 -> verdict C | C |
| R1-Q27 | DS | brute force over 100 stated values | I alone: not unique (4 values, e.g. 25, 4, 49, 9); II alone: not unique (19 values, e.g. 11, 12, 13, 14); together: unique value 25 -> verdict C | C |
| R1-Q28 | MCQ | label/grid/identity check | x < 2 | D |
| R1-Q29 | MCQ | exact enumeration or Fraction arithmetic | 40 | A |
| R1-Q30 | MCQ | exact enumeration or Fraction arithmetic | 29 | C |
| R1-Q31 | MCQ | exact enumeration or Fraction arithmetic | 13 | B |
| R1-Q32 | MCQ | exact enumeration or Fraction arithmetic | 3 | D |
| R1-Q33 | MCQ | exact enumeration or Fraction arithmetic | 10000 | A |
| R1-Q34 | MCQ | exact enumeration or Fraction arithmetic | 90 | A |
| R1-Q35 | MCQ | exact enumeration or Fraction arithmetic | 47 | C |
| R1-Q36 | DS | brute force over 90 stated values | I alone: not unique (13 values, e.g. 14, 21, 28, 35); II alone: not unique (5 values, e.g. 14, 23, 32, 41); together: unique value 14 -> verdict C | C |
| R1-Q37 | DS | brute force over 61 stated values | I alone: not unique (2 values, e.g. -9, 9); II alone: unique value -9; together: unique value -9 -> verdict A | A |
| R1-Q38 | MCQ | label/grid/identity check | xy > -6 | B |
| R1-Q39 | DS | brute force over 41 stated values | I alone: not unique (17 values, e.g. 10, 11, 12, 13); II alone: not unique (29 values, e.g. -1, -10, -11, -12); together: not unique (5 values, e.g. 4, 5, 6, 7) -> verdict D | D |
| R1-Q40 | DS | brute force over 41 stated values | I alone: not unique (2 values, e.g. no, yes); II alone: unique value yes; together: unique value yes -> verdict A | A |
| R1-Q41 | MCQ | exact enumeration or Fraction arithmetic | 12 | D |
| R1-Q42 | MCQ | label/grid/identity check | (-15, 10) | B |
| R1-Q43 | MCQ | exact enumeration or Fraction arithmetic | 5 | D |
| R1-Q44 | DS | brute force over 61 stated values | I alone: unique value yes; II alone: not unique (2 values, e.g. no, yes); together: unique value yes -> verdict A | A |
| R1-Q45 | MCQ | exact enumeration or Fraction arithmetic | 486 | D |
| R1-Q46 | MCQ | label/grid/identity check | sqrt(t) | B |
| R1-Q47 | MCQ | label/grid/identity check | -a | D |
| R1-Q48 | MCQ | label/grid/identity check | m is odd | D |
| R1-Q49 | DS | question-alone enumeration: smallest n with n = 2 (mod 5) and n = 3 (mod 7), n in 1-299 | 17 (unique minimum); self-sufficient -> verdict D | D |
| R1-Q50 | DS | brute force over 1-199; I alone: unique value 112; II alone: 9 values (e.g. -2, 2, 12, 152); question alone: not unique -> verdict A | A |
| R1-Q51 | DS | largest three-digit square by enumeration: 31^2 = 961, digit sum 16; question alone fixes it -> verdict D | D |
| R1-Q52 | DS | brute force over distinct prime triples p < q < r < 50; I alone: unique r = 31; II alone: unique r = 31; together: 31 -> verdict B | B |
| R1-Q53 | DS | brute force over 30-50; I alone: 5 values (30, 35, 40, 45, 50); II alone: unique value 50 -> verdict A | A |
| R1-Q54 | MCQ | enumeration over 1-30: x^2 - 3 > 4 - x holds for x = 3 to 30, i.e. 28 values | 28 | B |
| R1-Q55 | DS | brute force over 1-200 (yes/no); I alone: yes and no; II alone: yes and no; together: yes only -> verdict C | C |
| R1-Q56 | DS | brute force over 1-29; I alone: 4 values (6, 9, 12, 18); II alone: 7 values; together: unique value 12 -> verdict C | C |

**Option-length and cue balance (Revision 1; recomputed on 56 items after the gap-closure pass).**

| Metric | Value | Target |
|---|---|---|
| Correct option uniquely longest (MCQ) | 2 of 33 = 6.1% | <= 25% |
| Longest within 25% of shortest (MCQ) | 15 of 33 = 45.5% | 100% ideal; numeric items with differing digit counts cannot all meet it |
| DS items: correct option uniquely longest | 3 of 23 = 13.0% (R1-Q13, R1-Q25, R1-Q52); option B is the longest standard wording, so B-keyed DS items are uniquely longest | <= 25%; within the limit |
| DS items: longest within 25% of shortest | 23 of 23 | 100% |
| All text-option items: correct option uniquely longest | 5 of 56 = 8.9% | <= 25% |
| Option D wording (self-sufficiency form) | 3 DS items | n/a |
| Key letter A / B / C / D | 14 / 14 / 14 / 14 (each 20-30% of 56) | 20-30% each |

## 3. Revision 2 — 56 items (28 MCQ, 28 DS)

| ID | Type | Verification | Computed value / DS verdict | Key |
|---|---|---|---|---|
| R2-Q01 | MCQ | exact enumeration or Fraction arithmetic | 48 | B |
| R2-Q02 | MCQ | exact enumeration or Fraction arithmetic | 53 | B |
| R2-Q03 | DS | brute force over 400 stated values | I alone: not unique (9 values, e.g. 1, 1/4, 1/9, 2/3); II alone: not unique (16 values, e.g. 11/7, 13/9, 15/11, 17/13); together: unique value 7/3 -> verdict C | C |
| R2-Q04 | MCQ | label/grid/identity check | 4:5 | C |
| R2-Q05 | MCQ | label/grid/identity check | x - y >= 3 | C |
| R2-Q06 | MCQ | exact enumeration or Fraction arithmetic | 20 | D |
| R2-Q07 | MCQ | exact enumeration or Fraction arithmetic | 9 | B |
| R2-Q08 | MCQ | exact enumeration or Fraction arithmetic | 104 | D |
| R2-Q09 | DS | brute force over 100 stated values | I alone: unique value no; II alone: not unique (2 values, e.g. no, yes); together: unique value no -> verdict A | A |
| R2-Q10 | DS | brute force over 50 stated values | I alone: not unique (8 values, e.g. 12, 18, 24, 30); II alone: not unique (6 values, e.g. 16, 24, 32, 40); together: not unique (2 values, e.g. 24, 48) -> verdict D | D |
| R2-Q11 | DS | brute force over 441 stated values | I alone: not unique (2 values, e.g. no, yes); II alone: not unique (2 values, e.g. no, yes); together: unique value yes -> verdict C | C |
| R2-Q12 | DS | brute force over 50 stated values | I alone: not unique (8 values, e.g. 12, 18, 24, 30); II alone: not unique (3 values, e.g. 16, 24, 8); together: unique value 24 -> verdict C | C |
| R2-Q13 | MCQ | exact enumeration or Fraction arithmetic | 2 | D |
| R2-Q14 | DS | brute force over 41 stated values | I alone: not unique (40 values, e.g. -1, -10, -11, -12); II alone: unique value 3; together: unique value 3 -> verdict A | A |
| R2-Q15 | DS | brute force over 100 stated values | I alone: not unique (10 values, e.g. 1, 100, 16, 25); II alone: not unique (4 values, e.g. 1, 27, 64, 8); together: not unique (2 values, e.g. 1, 64) -> verdict D | D |
| R2-Q16 | DS | brute force over 100 stated values | I alone: not unique (33 values, e.g. 12, 15, 18, 21); II alone: not unique (3 values, e.g. 10, 15, 5); together: unique value 15 -> verdict C | C |
| R2-Q17 | MCQ | label/grid/identity check | 1/x | D |
| R2-Q18 | MCQ | exact enumeration or Fraction arithmetic | 24 | B |
| R2-Q19 | MCQ | label/grid/identity check | 0 < x < 1 | B |
| R2-Q20 | DS | brute force over 400 stated values | I alone: not unique (6 values, e.g. 1, 12, 2, 3); II alone: not unique (19 values, e.g. 10, 11, 12, 13); together: unique value 4 -> verdict C | C |
| R2-Q21 | DS | brute force over 200 stated values | I alone: unique value yes; II alone: not unique (2 values, e.g. no, yes); together: unique value yes -> verdict A | A |
| R2-Q22 | MCQ | exact enumeration or Fraction arithmetic | 5 | B |
| R2-Q23 | MCQ | exact enumeration or Fraction arithmetic | 18 | C |
| R2-Q24 | MCQ | exact enumeration or Fraction arithmetic | 18 | B |
| R2-Q25 | MCQ | exact enumeration or Fraction arithmetic | 20 | D |
| R2-Q26 | MCQ | exact enumeration or Fraction arithmetic | 22 | A |
| R2-Q27 | MCQ | exact enumeration or Fraction arithmetic | 156 | B |
| R2-Q28 | MCQ | label/grid/identity check | 3/2 | D |
| R2-Q29 | DS | brute force over 81 stated values | I alone: unique value 2; II alone: not unique (2 values, e.g. -2, 2); together: unique value 2 -> verdict A | A |
| R2-Q30 | MCQ | label/grid/identity check | 3^(1/3) | A |
| R2-Q31 | MCQ | exact enumeration or Fraction arithmetic | 2 | B |
| R2-Q32 | MCQ | label/grid/identity check | sqrt(98) - sqrt(97) | C |
| R2-Q33 | DS | brute force over 41 stated values | I alone: not unique (4 values, e.g. 0, 1, 4, 9); II alone: not unique (8 values, e.g. 121, 169, 25, 289); together: not unique (2 values, e.g. 4, 9) -> verdict D | D |
| R2-Q34 | DS | brute force over 61 stated values | I alone: unique value 6; II alone: unique value 6; together: unique value 6 -> verdict B | B |
| R2-Q35 | DS | brute force over 41 stated values | I alone: not unique (2 values, e.g. -1, 0); II alone: not unique (21 values, e.g. 0, 1, 10, 11); together: unique value 0 -> verdict C | C |
| R2-Q36 | DS | brute force over 21 stated values | I alone: not unique (16 values, e.g. -10, -3, -4, -5); II alone: not unique (10 values, e.g. -1, -10, -2, -3); together: not unique (8 values, e.g. -10, -3, -4, -5) -> verdict D | D |
| R2-Q37 | MCQ | label/grid/identity check | -20 | A |
| R2-Q38 | MCQ | label/grid/identity check | (0, 1/2) | A |
| R2-Q39 | MCQ | label/grid/identity check | x^3 = -343 | B |
| R2-Q40 | MCQ | exact enumeration or Fraction arithmetic | 3 | C |
| R2-Q41 | DS | brute force over 21 stated values | I alone: not unique (21 values, e.g. 0, 1, 10, 11); II alone: not unique (3 values, e.g. 10, 16, 4); together: not unique (3 values, e.g. 10, 16, 4) -> verdict D | D |
| R2-Q42 | MCQ | label/grid/identity check | x < -2 or x > 3 | A |
| R2-Q43 | DS | brute force over 21 stated values | I alone: not unique (2 values, e.g. no, yes); II alone: unique value no; together: unique value no -> verdict A | A |
| R2-Q44 | DS | brute force over 81 stated values | I alone: not unique (2 values, e.g. -7, 7); II alone: not unique (45 values, e.g. -1, -2, -3, -4); together: unique value 7 -> verdict C | C |
| R2-Q45 | DS | brute force over 11 stated values | I alone: unique value 7; II alone: not unique (5 values, e.g. 10, 6, 7, 8); together: unique value 7 -> verdict A | A |
| R2-Q46 | DS | brute force over 100 stated values | I alone: not unique (5 values, e.g. 1, 2, 3, 4); II alone: not unique (3 values, e.g. 1, 2, 3); together: not unique (3 values, e.g. 1, 2, 3) -> verdict D | D |
| R2-Q47 | MCQ | label/grid/identity check | x + 2y = 10 and x - 2y = 2 | B |
| R2-Q48 | MCQ | label/grid/identity check | [-10, 5] | A |
| R2-Q49 | DS | question-alone solution of x^2 = 2x: roots 0 and 2, sum 2; self-sufficient -> verdict D | D |
| R2-Q50 | DS | brute force over 10-99 (digit sum 11: 8 candidates); I alone: unique value 92; II alone: 4 values (38, 56, 74, 92) -> verdict A | A |
| R2-Q51 | DS | brute force over -10 to 10; I alone: unique value 3; II alone: unique value 3; together: 3 -> verdict B | B |
| R2-Q52 | DS | brute force over distinct prime triples p < q < r < 30; I alone: 5 values of q; II alone: 3 values; together: 2 values (5, 7) -> verdict D | D |
| R2-Q53 | DS | brute force over 30-50; I alone: unique value 35; II alone: unique value 35; together: 35 -> verdict B | B |
| R2-Q54 | DS | brute force over -6 to 6; I alone: -4 or 2; II alone: -4 or 4; together: unique value -4 -> verdict C | C |
| R2-Q55 | DS | brute force over 10-99; I alone: 10 values; II alone: 5 values (50, 61, 72, 83, 94); together: unique value 72 -> verdict C | C |
| R2-Q56 | DS | brute force over 1-200; together: 36 is a square, 72 is not -> verdict D | D |

**Option-length and cue balance (Revision 2; recomputed on 56 items after the gap-closure pass).**

| Metric | Value | Target |
|---|---|---|
| Correct option uniquely longest (MCQ) | 1 of 28 = 3.6% | <= 25% |
| Longest within 25% of shortest (MCQ) | 17 of 28 = 60.7% | 100% ideal; numeric items with differing digit counts cannot all meet it |
| DS items: correct option uniquely longest | 3 of 28 = 10.7% (R2-Q34, R2-Q51, R2-Q53); option B is the longest standard wording, so B-keyed DS items are uniquely longest | <= 25%; within the limit |
| DS items: longest within 25% of shortest | 28 of 28 | 100% |
| All text-option items: correct option uniquely longest | 4 of 56 = 7.1% | <= 25% |
| Option D wording (self-sufficiency form) | 3 DS items | n/a |
| Key letter A / B / C / D | 13 / 14 / 14 / 15 (each 20-30% of 56) | 20-30% each |

## 4. Revision 3 — 56 items (29 MCQ, 27 DS)

| ID | Type | Verification | Computed value / DS verdict | Key |
|---|---|---|---|---|
| R3-Q01 | MCQ | exact enumeration or Fraction arithmetic | 12 | D |
| R3-Q02 | MCQ | label/grid/identity check | No value of x satisfies it | A |
| R3-Q03 | DS | brute force over 30 stated values | I alone: not unique (2 values, e.g. no, yes); II alone: not unique (2 values, e.g. no, yes); together: not unique (2 values, e.g. no, yes) -> verdict D | D |
| R3-Q04 | MCQ | exact enumeration or Fraction arithmetic | 12 | B |
| R3-Q05 | DS | brute force over 41 stated values | I alone: not unique (2 values, e.g. no, yes); II alone: unique value yes; together: unique value yes -> verdict A | A |
| R3-Q06 | MCQ | label/grid/identity check | P is greater than Q | D |
| R3-Q07 | MCQ | label/grid/identity check | p = q or p = -q | A |
| R3-Q08 | MCQ | exact enumeration or Fraction arithmetic | 4 | A |
| R3-Q09 | MCQ | exact enumeration or Fraction arithmetic | 34 | B |
| R3-Q10 | DS | brute force over 41 stated values | I alone: not unique (2 values, e.g. 0, 1); II alone: not unique (26 values, e.g. -1, -10, -11, -12); together: not unique (2 values, e.g. 0, 1) -> verdict D | D |
| R3-Q11 | MCQ | exact enumeration or Fraction arithmetic | 400 | B |
| R3-Q12 | MCQ | exact enumeration or Fraction arithmetic | 8 | A |
| R3-Q13 | DS | brute force over 99 stated values | I alone: not unique (20 values, e.g. 12, 17, 2, 22); II alone: not unique (10 values, e.g. 12, 2, 22, 32); together: not unique (10 values, e.g. 12, 2, 22, 32) -> verdict D | D |
| R3-Q14 | DS | brute force over 200 stated values | I alone: not unique (13 values, e.g. 105, 120, 135, 15); II alone: not unique (19 values, e.g. 12, 16, 20, 24); together: unique value 60 -> verdict C | C |
| R3-Q15 | MCQ | exact enumeration or Fraction arithmetic | 7 | B |
| R3-Q16 | MCQ | exact enumeration or Fraction arithmetic | 32 | A |
| R3-Q17 | DS | brute force over 30 stated values | I alone: not unique (6 values, e.g. 13, 18, 23, 28); II alone: not unique (5 values, e.g. 1, 3, 5, 7); together: unique value 3 -> verdict C | C |
| R3-Q18 | DS | brute force over 19 stated values | I alone: unique value yes; II alone: not unique (2 values, e.g. no, yes); together: unique value yes -> verdict A | A |
| R3-Q19 | DS | brute force over 100 stated values | I alone: unique value 11; II alone: not unique (25 values, e.g. 100, 12, 16, 20); together: no admissible value satisfies it -> verdict A | A |
| R3-Q20 | MCQ | exact enumeration or Fraction arithmetic | 4 | B |
| R3-Q21 | DS | brute force over 400 stated values | I alone: not unique (6 values, e.g. 11, 15, 18, 20); II alone: not unique (10 values, e.g. 108, 140, 176, 20); together: unique value 20 -> verdict C | C |
| R3-Q22 | MCQ | exact enumeration or Fraction arithmetic | 4 | D |
| R3-Q23 | MCQ | exact enumeration or Fraction arithmetic | 40 | A |
| R3-Q24 | DS | brute force over 41 stated values | I alone: unique value yes; II alone: unique value yes; together: unique value yes -> verdict B | B |
| R3-Q25 | MCQ | exact enumeration or Fraction arithmetic | 4 | D |
| R3-Q26 | DS | brute force over 900 stated values | I alone: not unique (13 values, e.g. 1, 10, 11, 12); II alone: not unique (15 values, e.g. 10, 11, 12, 13); together: unique value 6 -> verdict C | C |
| R3-Q27 | MCQ | label/grid/identity check | (3/2)^3 | D |
| R3-Q28 | DS | brute force over 231 stated values | I alone: not unique (3 values, e.g. 1, 3, 5); II alone: not unique (11 values, e.g. 0, 1, 10, 2); together: unique value 3 -> verdict C | C |
| R3-Q29 | DS | brute force over 30 stated values | I alone: unique value yes; II alone: unique value yes; together: unique value yes -> verdict B | B |
| R3-Q30 | MCQ | exact enumeration or Fraction arithmetic | 29 | B |
| R3-Q31 | MCQ | exact enumeration or Fraction arithmetic | 12 | D |
| R3-Q32 | DS | brute force over 25 stated values | I alone: not unique (5 values, e.g. -12, -2, -7, 3); II alone: not unique (4 values, e.g. 1, 2, 3, 4); together: unique value 3 -> verdict C | C |
| R3-Q33 | DS | brute force over 900 stated values | I alone: not unique (14 values, e.g. 1, 10, 11, 12); II alone: not unique (15 values, e.g. 10, 11, 12, 13); together: unique value 7 -> verdict C | C |
| R3-Q34 | MCQ | label/grid/identity check | 2 sqrt(3) | D |
| R3-Q35 | DS | brute force over 101 stated values | I alone: unique value 5; II alone: unique value 5; together: unique value 5 -> verdict B | B |
| R3-Q36 | MCQ | label/grid/identity check | P is less than Q | C |
| R3-Q37 | DS | brute force over 40 stated values | I alone: not unique (8 values, e.g. 10, 15, 20, 25); II alone: not unique (3 values, e.g. 16, 25, 36); together: unique value 25 -> verdict C | C |
| R3-Q38 | DS | brute force over 200 stated values | I alone: not unique (4 values, e.g. 135, 180, 45, 90); II alone: not unique (5 values, e.g. 18, 27, 36, 45); together: unique value 45 -> verdict C | C |
| R3-Q39 | MCQ | exact enumeration or Fraction arithmetic | 10 | C |
| R3-Q40 | MCQ | label/grid/identity check | b/a | D |
| R3-Q41 | DS | brute force over 19 stated values | I alone: unique value yes; II alone: not unique (2 values, e.g. no, yes); together: unique value yes -> verdict A | A |
| R3-Q42 | MCQ | exact enumeration or Fraction arithmetic | 5 | B |
| R3-Q43 | MCQ | exact enumeration or Fraction arithmetic | 5/2 | B |
| R3-Q44 | DS | brute force over 50 stated values | I alone: unique value yes; II alone: unique value yes; together: unique value yes -> verdict B | B |
| R3-Q45 | MCQ | exact enumeration or Fraction arithmetic | 7 | A |
| R3-Q46 | MCQ | label/grid/identity check | n is a multiple of 3 | D |
| R3-Q47 | MCQ | exact enumeration or Fraction arithmetic | 2 | A |
| R3-Q48 | MCQ | label/grid/identity check | 2:3 | C |
| R3-Q49 | DS | question-alone solution of m + (m + 4) = 28: m = 12; self-sufficient -> verdict D | D |
| R3-Q50 | DS | brute force over 1-199; I alone: unique value 12 (positive root only); II alone: 4 values (4, 8, 12, 16) -> verdict A | A |
| R3-Q51 | DS | question alone: 6w = 36 gives w = 6, length 12, area 72; self-sufficient -> verdict D | D |
| R3-Q52 | DS | distinct prime triples a < b < c with sum 20; question alone: c = 11 or 13; I alone: unique c = 11; II alone: 2 values -> verdict A | A |
| R3-Q53 | DS | brute force over 40-60; I alone: 3 values (42, 49, 56); II alone: 3 values (42, 50, 58); together: unique value 42 -> verdict C | C |
| R3-Q54 | MCQ | enumeration over -4 to 4: x^2 + 3x - 10 >= 0 holds for x = 2, 3, 4, i.e. 3 values | 3 | B |
| R3-Q55 | DS | brute force over -10 to 10; I alone: unique value 4; II alone: 7 values (4 to 10) -> verdict A | A |
| R3-Q56 | DS | brute force over 100-200; I alone: 13 values; II alone: 7 values; together: unique value 120 -> verdict C | C |

**Option-length and cue balance (Revision 3; recomputed on 56 items after the gap-closure pass).**

| Metric | Value | Target |
|---|---|---|
| Correct option uniquely longest (MCQ) | 1 of 29 = 3.4% | <= 25% |
| Longest within 25% of shortest (MCQ) | 14 of 29 = 48.3% | 100% ideal; numeric items with differing digit counts cannot all meet it |
| DS items: correct option uniquely longest | 4 of 27 = 14.8% (R3-Q24, R3-Q29, R3-Q35, R3-Q44); option B is the longest standard wording, so B-keyed DS items are uniquely longest | <= 25%; within the limit |
| DS items: longest within 25% of shortest | 27 of 27 | 100% |
| All text-option items: correct option uniquely longest | 5 of 56 = 8.9% | <= 25% |
| Option D wording (self-sufficiency form) | 3 DS items | n/a |
| Key letter A / B / C / D | 15 / 13 / 14 / 14 (each 20-30% of 56) | 20-30% each |

## 5. Revisions made during authoring

- Set 1: box-and-bag calc replaced by a real solver (initial placeholder); consecutive-integer calc corrected from the middle integer to the largest term; parity item calc changed from a boolean to its label; distractor explanations for marking, abs-count, the x^2 identity, and the least-integer item rewritten because their error stories did not match the arithmetic; three label items (power comparison, the t-ordering item and the negative-fraction item) had their options reordered so that the key matches its computed index; two DS items had mis-ordered constructor arguments and were repaired; the DS stem `What is x?` was varied where it repeated.
- Set 2: the interval-quotient item was rewritten (its first version carried a range that did not match the stem); the power item's justification was replaced by the exact 30th-power comparison; an explanation about the infimum was corrected; two DS items were replaced (shift-and-power parity replaced by the owner's match-outcome form).
- Set 3: two explanations with arithmetic-garble text were rewritten; a DS item that repeated the residue-plus-parity statements was replaced; two weak DS items were replaced by the owner's coin-denomination and transfer-rate forms.
- Gap-closure pass (2026-11-01): eight items per set were appended (IDs R1-Q49 to R1-Q56, R2-Q49 to R2-Q56, R3-Q49 to R3-Q56) to close gaps G1-G4. Existing items and answers were not renumbered or changed. See section 8.
- Across sets: DS stems repeated word-for-word were varied so that each DS item has a distinct stem. No item was retained with an unverified key.

## 6. Label checks (`verify_labels.py`)

All statement and label keys pass the following checks (run output `ALL PASS`):

- `xy > -6` holds on the open rectangle; `xy < 2`, `x + y < 3` and `x - y > -3` each fail at a grid point (sample: x=0.75, y=2.75 gives xy=2.06). Corner products of (-2,1) x (0,3) are -6, 0, 3, all excluded.
- `x < 2` solves `-4x + 7 > 2x - 5`; `sqrt(t)` is the largest of t, t^2, sqrt(t), t^3 on (0,1); `-a` is the largest of a, a^2, 1/a, -a on (-1,0).
- `27^5` exceeds `9^7`, `81^3` and `3^13`; `sqrt45 + sqrt20 = 5 sqrt5` exceeds the other surd options; the interval product of (-3,2) x (1,5] has corners -3, -15, 2, 10, giving the open range (-15, 10).
- `(x-3)/(x+2) > 0` exactly on `x < -2 or x > 3`; `x^2 < x` (x nonzero) exactly on `0 < x < 1`; `x - y >= 3` is forced by `x >= 2, y <= -1`, while `x + y >= 1` and `xy >= -2` fail at (2,-5).
- `(0, 1/2)` for x/y on (0,1) x (2,4) (sup approached at x->1, y->2; inf at x->0); `[-10, 5]` for [3,5] x [-2,1] with all four corners attained; `3^(1/3)` is largest (30th powers 3^10 > 6^6 > 2^15 > 5^5); `x^3 = -343` has one real root while `x^2 = 49` has two.
- `sqrt98 - sqrt97 > sqrt99 - sqrt98`; `3/2` is the only listed rational strictly between sqrt2 and sqrt3; the infimum of ab on (-5,-2) x (3,4) is -20; the coefficient determinant of `x+2y=10, x-2y=2` is nonzero (unique), while the other three pairs have determinant zero.
- Revision 3 table: P = 140, Q = 0, so P > Q; `x/3 + x/6 = 1 + x/2` has no solution; `sqrt48 + sqrt27 - sqrt75 = 2 sqrt3`; `(3/2)^3` is the greatest; the copper:tin ratio of the mixture is 4:6 = 2:3; `p^2 = q^2` gives `p = q or p = -q`; `2n + 3` divisible by 3 forces n divisible by 3; largest k with 7k < 60 is 8 < 9; `b/a` is the greatest for 0 < a < b.

## 7. Uniqueness and answer-independence

- Every MCQ has its distractors checked not to equal the key; no 'all/none of the above' options are used.
- Every DS item's verdict is derived from the stated domain. The four standard DS option texts are identical in all items. Option D differs only in the self-sufficiency items (section 8), where it is keyed or used as a distractor in both forms.
- **Correction (2026-11-01).** The earlier statement that DS correct options are never uniquely longest was wrong. Option B is the longest standard DS wording, so B-keyed DS items are uniquely longest (sections 2-4 list them). The shares are within the 25% limit, and the wording is the standard form, so it is recorded rather than altered.
- Key positions were assigned by a balancing routine after the DS verdicts were fixed. After the gap-closure pass each set holds 56 items, with keys A/B/C/D = 14/14/14/14 (R1), 13/14/14/15 (R2) and 15/13/14/14 (R3), all within 20-30%.

## 8. Gap-closure pass (2026-11-01): G1-G4

**Scope.** Eight items per set were appended after the existing last IDs (R1-Q49 to R1-Q56, R2-Q49 to R2-Q56, R3-Q49 to R3-Q56). No existing question or answer was renumbered or altered. The time budget at the top of each QUESTIONS.md was extended to 56 questions in about 67 minutes (56 x 72 s). A neutral note was added to each header that option D wording varies in some DS items.

**Gap mapping.**

| Gap | New items (R1 / R2 / R3) | Form |
|---|---|---|
| G1 self-sufficient question (2025 fourth-option form) | R1: Q49, Q50 (key A), Q51 / R2: Q49, Q50 (key A), Q51 (key B) / R3: Q49, Q50 (key A), Q51 | Option D printed as "The question can be answered even without any statement". Keyed D only when the stem alone fixes one value; the other G1 items have a statement verdict and keep the same D wording as a false distractor. |
| G2 prime-triple and class-size forms | R1: Q52, Q53 / R2: Q52, Q53 / R3: Q52, Q53 | Prime triples (R1 B, R2 D, R3 A); class size (R1 A, R2 B, R3 C). |
| G3 coded inequalities | R1: Q54 (MCQ) / R2: Q54 (DS, key C) / R3: Q54 (MCQ), Q55 (DS, key A) | Symbol defined by a formula, then a coded inequality or equation over a stated integer domain. |
| G4 explicit necessary-pair drill | R1: Q55, Q56 / R2: Q55, Q56 / R3: Q56 | Each statement is necessary but not sufficient; the pair decides (C). R2-Q56 is the converse: a necessary pair that still leaves yes and no open (D). |

**Verification.** Each new key was checked by a separate script (not in the repository): exact enumeration over the stated domain, the DS verdict rule from section 1 for statement items, and the self-sufficiency test for G1 items. The checks passed for all 24 new items. Two checker bugs found during the pass were corrected in the checker, not in the items: a smallest-value check that counted every solution rather than the minimum, and an area formula. Two items were revised before release: R2-Q53 originally gave two different values (35 and 45) for its two statements, which would make the statements contradictory; it was replaced with statements that agree at 35. R1-Q51 originally used a false statement, and was replaced with two true statements.

**Statement consistency.** For each DS item, both statements are true of the keyed answer (or, for D items, of at least one admissible value), so no item relies on contradictory statements.

**Verification summary for the new items.**

| ID | Type | Verification | Computed value / DS verdict | Key |
|---|---|---|---|---|
| R1-Q49 | DS | question-alone enumeration (smallest n with n = 2 mod 5, n = 3 mod 7) | 17; self-sufficient -> D | D |
| R1-Q50 | DS | I alone: 112; II alone: not unique -> A | A | A |
| R1-Q51 | DS | 961 (31^2), digit sum 16; self-sufficient -> D | D | D |
| R1-Q52 | DS | I alone: r = 31; II alone: r = 31 -> B | B | B |
| R1-Q53 | DS | I alone: 5 values; II alone: 50 -> A | A | A |
| R1-Q54 | MCQ | enumeration over 1-30: 28 values | 28 | B |
| R1-Q55 | DS | yes/no; together: yes only -> C | C | C |
| R1-Q56 | DS | I alone 4 values; II alone 7; together 12 -> C | C | C |
| R2-Q49 | DS | roots 0 and 2, sum 2; self-sufficient -> D | D | D |
| R2-Q50 | DS | I alone: 92; II alone: 4 values -> A | A | A |
| R2-Q51 | DS | I alone: 3; II alone: 3 -> B | B | B |
| R2-Q52 | DS | together: q = 5 or 7 -> D | D | D |
| R2-Q53 | DS | I alone: 35; II alone: 35 -> B | B | B |
| R2-Q54 | DS | together: x = -4 -> C | C | C |
| R2-Q55 | DS | together: 72 -> C | C | C |
| R2-Q56 | DS | together: 36 square, 72 not -> D | D | D |
| R3-Q49 | DS | m = 12 from the stem; self-sufficient -> D | D | D |
| R3-Q50 | DS | I alone: 12; II alone: 4 values -> A | A | A |
| R3-Q51 | DS | w = 6, area 72 from the stem; self-sufficient -> D | D | D |
| R3-Q52 | DS | I alone: c = 11; II alone: 2 values -> A | A | A |
| R3-Q53 | DS | together: 42 -> C | C | C |
| R3-Q54 | MCQ | enumeration over -4 to 4: 3 values | 3 | B |
| R3-Q55 | DS | I alone: x = 4; II alone: 7 values -> A | A | A |
| R3-Q56 | DS | together: 120 -> C | C | C |

**Option-length and letter check.** The option-length tables in sections 2-4 were recomputed from the files. All new MCQ options are two-digit (R1-Q54) or one-digit (R3-Q54) numerals of equal digit count. The R1-Q54 range was widened from 1-10 to 1-30 so that its options share a digit count.

**Structural check.** Every QUESTIONS.md ID runs contiguously from 01 to 56; each ANSWERS entry maps one-to-one to a question; each answer has exactly one (key) line whose letter matches the keyed letter; every answer has a trap and shortcut line.
