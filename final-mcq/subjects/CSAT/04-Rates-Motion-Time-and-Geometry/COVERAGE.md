# csat-04 — Rates, Motion, Time and Geometry: source and coverage ledger

**Status: complete.** Three original banks (`revision-1` 56 items, `revision-2` 56 items, `revision-3` 54 items), this ledger and [`AUDIT.md`](AUDIT.md) are present. Every key was verified by computation and recorded in `AUDIT.md`. Rows marked **partial** in §3 are covered by a neighbouring form rather than the exact PYQ-demand form; the lead should downgrade the status if that is not acceptable.

## 1. Sources

- **Basic owner:** `upsc-ai-kit/knowledge/CSAT/basic/04_Rates-Motion-Time-and-Geometry.md` — §§1–10 (visual model, formulas, method, conditions, worked examples, must-know facts, traps, quick checks, mini-drill, timed transfer), the 2018–2023, 2024–2025 and 2026 PYQ demand tables, and the semantic-completeness closure (2026-09-06).
- **Advanced owner:** `upsc-ai-kit/knowledge/CSAT/advanced/04_Rates-Motion-Time-and-Geometry.md` — §§1–10 (architecture, alternate-day work, circular track, moving-object crossing, segment-ordering rearrangement, clock right angles, cube counts, calendar Method 6, tile feasibility, advanced drill, PYQ-pattern notes).
- **Boundaries used:** commercial ratios and averages from Topic 03; algebraic comparison from Topic 05; spatial direction puzzles from Topic 06; integer and digit properties from Topic 02.
- **PYQ use:** the owners' routed demand families (2018–2026) were used only as neutral skill labels. No UPSC wording, option set or answer key was reproduced or used. Original items were authored for every family.

## 2. Set inventory

| Set | Items | Time budget (about 72 s per item) | Scoring | Verified by |
|---|---|---|---|---|
| `revision-1/` | 56 | about 67 minutes | +2.5 correct, −0.83 wrong, 0 skipped | `AUDIT.md` §2.1 |
| `revision-2/` | 56 | about 67 minutes | as above | `AUDIT.md` §2.2 |
| `revision-3/` | 54 | about 65 minutes | as above | `AUDIT.md` §2.3 |

Revision 1 is full coverage with mostly direct and two-step items. Revision 2 adds cross-links (for example average speed with unequal times, clock angles with the 24-hour hour, pipes with a delayed drain, painted cubes with two painted faces and unpainted sides). Revision 3 is application and mixed framing (timetables, schedules, tables, brute-force counts, and story contexts such as relays, late starters and cisterns).

## 3. Owner-row ledger

Each row names the owner technique or trap and the item IDs in each set. `—` means the row is not separately set in that revision.

| # | Owner technique / named trap (owner section) | R1 | R2 | R3 | Status |
|---|---|---|---|---|---|
| 1 | Rate model: quantity = rate × time; work rates add only when simultaneous (Basic §§1–2, §4; semantic closure step 2) | Q14, Q15, Q16 | Q06, Q25 | Q11, Q22, Q37 | covered |
| 2 | Work: time = 1 ÷ combined rate; efficiency scales the rate, not the time (Basic §2) | Q14, Q15, Q16 | Q06, Q25 | Q22, Q30, Q37 | covered |
| 3 | Alternate-day work, the remainder decides the finish and who starts changes the total (Advanced §§2, 3 Method 1 and 4, §5) | Q17 | Q26 | Q03 | covered |
| 4 | Pipes: fillers add, drains subtract; net rate ≤ 0 never fills (Basic §2) | Q19, Q20, Q46 | Q07, Q27, Q47 | Q04, Q24, Q46 | covered |
| 5 | Unit conversion km/h ↔ m/s (× 5/18); volume and time unit conversion (Basic §2, §4, §10 table; Advanced PYQ notes) | Q01, Q08, Q40, Q53 | Q31, Q32, Q53 | Q28, Q31, Q32, Q40, Q53 | covered |
| 6 | Average speed = total distance ÷ total time; harmonic mean only for equal distances; arithmetic only for equal times (Basic §§2, 4, 5 Example F, 7) | Q02, Q03, Q10, Q44 | Q03, Q37, Q42 | Q02, Q12, Q26, Q35 | covered |
| 7 | Speed vs velocity; distance vs displacement; path reversal (Basic §2.1; Advanced §6; 2026 forward/backward step demand) | Q04, Q43 | Q24 | Q21 | covered |
| 8 | Trains: crossing a pole uses the train's own length; crossing a platform or bridge adds the object's length (Basic §§2, 5 Example C) | Q07, Q08 | Q45 | Q01, Q32 | covered |
| 9 | Relative speed: opposite directions add, same direction subtract, objects on the same line (Basic §§2, 4) | Q05, Q06 | Q01, Q04, Q21 | Q14, Q36, Q44 | covered |
| 10 | Moving-object crossing with both lengths and a changed reference (Advanced Method 3 and drill 2) | Q05, Q06, Q08 | Q04, Q45 | Q14, Q23 | covered |
| 11 | Boats and streams: b + s downstream, b − s upstream, b > s; stream reversal trap; boat round trips (Basic §2, Example C.1; Advanced §2) | Q09, Q10 | Q02, Q19, Q34 | Q41 | covered |
| 12 | Circular track: meeting anywhere uses L ÷ relative speed (Basic §2; Advanced Method 2) | Q11 | Q56 (catch-up) | Q15 (walkers) | covered |
| 13 | Circular track: start-point reunion uses the LCM of commensurable lap times; not the relative-speed time (Basic §§4–5; Advanced §5 boundary, drill 5) | Q12 | Q05 | Q10 | covered |
| 14 | Races: head start and late start change the finish time, not only the margin (Basic §5 extension; PYQ race-distance family) | Q13 | Q18 | Q23 | covered |
| 15 | Clock angle |30H − 5.5M|, H taken mod 12, smaller angle ≤ 180° (Basic §§2, 4, 7) | Q21, Q47 | Q10, Q46 | Q42, Q47 | covered |
| 16 | Clock coincidences: 11 per 12 h, every 65 5/11 min (Basic §6) | Q22 | — (Q44 is the straight-angle form) | Q19 | covered |
| 17 | Clock right angles: 22 per 12 h, 44 per day; two roots per hour; roots at or above 60 min belong to the next hour (Basic §6; Advanced §§2, 5) | Q23, Q42 | Q11, Q28 | Q34 (same equation, 15° offset) | partial in R3 (no right-angle-time item) |
| 18 | Clock opposite (180°) and 45° angle counts; straight-angle time after 12 (Advanced §§2, 5 as relative-speed equations) | — | Q39, Q44 | Q16 | covered |
| 19 | Clock gain and loss over days (PYQ fast-clock family) | Q24 | Q36 | Q05 | covered |
| 20 | Calendar: odd days; non-leap year = 1, leap year = 2 only when 29 Feb lies in the span; century rule; 100 years = 5 odd days; 400 years = 0 (Basic §2, §4; Advanced Method 6) | Q25, Q26, Q27 | Q08, Q09, Q12, Q20, Q29, Q35 | Q07, Q18, Q33, Q38 | covered; the 400-year zero is tested only as a distractor (R1-Q27 option A) |
| 21 | Calendar: periodic events and their weekday (LCM of cycles, weekday = LCM mod 7) (PYQ periodic-signal and calendar-meeting families) | — | — | Q06, Q38 | covered (R3 only; the R1/R2 calendar items do not use an LCM) |
| 22 | Mensuration: rectangle (area, perimeter, diagonal), triangle, trapezium, circle, cuboid, cube, cylinder, cone, sphere (Basic §2, §5 Example E) | Q28, Q29, Q30, Q31, Q32, Q33, Q34 | Q13, Q14, Q22, Q23, Q30, Q43 | Q08, Q39 | covered |
| 23 | Pythagoras and coordinate distance; the right triangle's altitude (Basic §5 transfer; semantic closure step 10 'properties before coordinates') | Q38, Q39, Q43 | Q23, Q24, Q33 | Q09, Q21 | covered |
| 24 | Cube-cutting counts for an n × n × n cube: 8, 12(n−2), 6(n−2)², (n−2)³, summing to n³ (Basic §5 Foundation; Advanced §2, drill 3) | Q35, Q36, Q41 | Q15, Q16, Q38 | Q13, Q43 | covered; the sum check is stated in the ANSWERS, not as its own item |
| 25 | Boundary of the cube formula: partly painted or hollow solids (Advanced §5) | Q52 | Q52 | Q52 | covered |
| 26 | Tile packing: whole tiles only, check both orientations, unit conversion first, rotation rule (Basic §§4, 5 Example E.1; Advanced §3 Method 6, drill 8) | Q37 | Q17 | Q40 | covered |
| 27 | Advanced segment-ordering: same distances and speeds, different pairing gives different times (Advanced Method 5, §4 rearrangement check; 2026 demand) | Q55 | Q55 | Q25 | covered |
| 28 | Multi-segment average speed with a halt, a rest or three equal legs (Advanced §2 average speed, drill 6) | Q44 | Q42, Q37 | Q12, Q26, Q35 | covered |
| 29 | Sound-distance relative rate (owner 2026 demand list) | Q48 | Q48 | Q48 | covered |
| 30 | Jump-sequence well climb (owner 2018–2023 demand list) | Q49 | Q49 | Q49 | covered |
| 31 | Bounce count sequence (owner 2018–2023 demand list) | Q50 (height after n rebounds) | Q50 (height after n rebounds) | Q50 (height after n rebounds) | partial: height, not count of bounces |
| 32 | Collinear-points and inscribed-triangle counts (owner 2018–2023 demand list) | Q51 (collinear) | Q51 (points on a circle) | Q51 (collinear) | partial: triangle counts; the ratio form is not set |
| 33 | Circle–square intersection count (owner 2018–2023 demand list) | Q54 | Q54 | Q54 | covered |
| 34 | Time unit total conversion (owner 2022 demand list) | Q53 | Q53 | Q53 (timetable duration) | covered |
| 35 | Two walkers, meeting point or catch-up (owner 2021 demand list) | Q56 | Q56 | Q15 | covered |
| 36 | Compass and direction tracking, net displacement (owner 2019–2021 demand lists) | Q04, Q43 | Q24 | Q21 | covered |
| 37 | Work-rate remaining days and combined fractions (owner 2020–2021 demand lists) | Q16 | Q25 | Q11 | covered |
| 38 | Speed and time ratio; velocity-time segment DI (owner 2018 demand list) | Q45 | Q34 | Q26 | covered |
| 39 | Clock hand angle timing, time correction, route time comparison (owner 2019, 2021, 2022 lists) | Q21, Q24, Q42 | Q10, Q36 | Q42, Q34 | partial: route time comparison appears as R3-Q25 (segment order) only in R3 |
| 40 | Cyclic work schedules and rotating workers (owner 2023 list) | Q17 | Q26 | Q03 | covered |
| 41 | Long-span calendar weekday and same-weekday years (owner 2024 list; Advanced Method 6) | Q26 | Q20, Q35 | Q33, Q18 | covered |
| 42 | Painted cube and painted cuboid counts for exactly one, two or three faces (owner PYQ families 2018–2025) | Q35, Q36, Q41 | Q15, Q16, Q38 | Q13, Q43 | covered |
| 43 | Relative speed in a non-collinear (perpendicular) setting; Pythagoras on the resultant (boundary of Basic §4) | Q43 | Q33 | — | covered in R1 and R2; R3 has no perpendicular item |

## 4. Partial and analogue rows

These rows are covered by a neighbouring form, not by the exact owner demand. They are listed so that a reader can see what is still thin:

- **Row 17 (right-angle times):** R1 covers the time of the first right angle after a given time (Q42) and the count (Q23). R2 covers the first right angle after 4 o'clock (Q11). R3 uses the same equation in a 15° offset item (Q34) and has no right-angle-time item of its own.
- **Row 31 (bounce count):** all three revisions ask for the height after n rebounds. None asks how many bounces occur before a threshold. A count-of-bounces item would be the exact form.
- **Row 32 (collinear and inscribed counts):** triangle counts only. The collinear-point ratio form is not set.
- **Row 39 (route comparison):** R3-Q25 is the only route-order comparison. R1 and R2 use the same skill through Q55 (pairing swap).
- **Row 20 (400-year cycle):** the zero-odd-day fact appears only as a distractor (R1-Q27, option A).
- **Row 21 (periodic calendar):** LCM weekday items are in R3 only.
- **Row 5 and row 34 (volume and time units):** covered by unit items per set, with the conversions stated in the ANSWERS.

Owner rows that are not covered: none are open. The owner's 'hollow or partially painted' boundary is covered by Q52 in each set.

## 5. Difficulty and balance

- Every item carries at least one named distractor route (see `ANSWERS.md`). Most R1 items (about 80%) need two or more steps or a close-option distinction; R2 and R3 are almost entirely multi-step.
- Single-formula warm-ups are kept deliberately few: R1 Q23, Q28, Q30, Q33, Q34, Q38, Q40, Q43, Q45, Q53; R2 Q12, Q15, Q16, Q28, Q38, Q52, Q53; R3 Q17, Q33, Q43, Q53, Q54.
- Answer letters: each letter holds 20–30% of keys in every set (see `AUDIT.md` §4).
- Option-length: the correct option is uniquely longest in 11% or less of items in each set. The 1.25× spread target is not met in about 40–50% of items; this is recorded as a soft deviation in `AUDIT.md` §5.

## 6. Cross-set distinctness

Some clock, painted-cube and calendar templates recur across the three revisions (for example the 24-hour clock angle in R1-Q47, R2-Q46 and R3-Q47). These are different instances with different numbers, distractors and framings. No revision reuses another revision's numbers for the same question. The R1 and R2 segment-ordering items use different speeds and distances.

## 7. Open items

- No owner row is open.
- The soft length-spread deviation (§5) and the partial rows (§4) are recorded here and in `AUDIT.md`.
- No second human reviewer has checked the keys; this is the main remaining risk before the banks are used as a live test.

