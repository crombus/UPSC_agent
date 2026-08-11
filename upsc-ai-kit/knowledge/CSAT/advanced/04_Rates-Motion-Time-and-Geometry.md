# Rates, Motion, Time and Geometry - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Basic numeracy / general mental ability.
> **Core skill:** alternate-day work, boats/streams, circular-track meetings, moving-object crossings,
> clock coincidences and cube-cutting counts.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/04_Rates-Motion-Time-and-Geometry.md).*

---

## 1. Architecture

```text
   MULTI-BODY RATE / MOTION PROBLEM
        |
   define each body's RATE or SPEED
        |
   +------------------+---------------------+
   |                  |                     |
 CYCLE work         RELATIVE motion       GEOMETRY count
 (alternate days)   (add/subtract speed)  (cube layers, diagonals)
        |
   solve one cycle / one relative rate, then scale
```

**Analytical claim:** rate and relative-motion items reduce to a **net rate** (per cycle or
relative), after which they become a division. Cube-cutting items are different: they use geometric
layer/face-count formulas.

## 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Alternate-day work** | Sum a full A+B cycle, count whole cycles, finish the remainder day by day. | Track who works on the final partial day - **who starts changes the answer**. |
| ✅ **Boats/streams** | Downstream `= b + s`, upstream `= b - s` (`b` = still-water, `s` = stream). | `b > s` for forward motion. |
| ✅ **Circular track** | Same direction meet time `= L/(v1 - v2)`; opposite `= L/(v1 + v2)`. | Same start point and constant speeds. "Meet **anywhere**" - meeting at the **start** is a different, LCM-based question. |
| ✅ **Moving-object crossing** | Time = combined length / **relative** speed. | Add speeds if opposite, subtract if same direction. |
| ✅ **Multi-segment average speed** | `total distance / total time` - never the mean of the segment speeds. | Two journeys with the **same** speeds over the **same** distances can still take different times if the speeds are attached to different segments. |
| ✅ **Clock right angle** | `\|30H - 5.5M\| = 90` (or `270`). | 22 right angles per 12 hours; solutions outside `0 <= M < 60` belong to the next hour. |
| ✅ **Cube cut into n^3** | 3-face `= 8`; 2-face `= 12(n-2)`; 1-face `= 6(n-2)^2`; 0-face `= (n-2)^3`. | `n >= 2`; the four counts sum to `n^3`. |

## 3. Harder methods (worked)

### 📝 Method 1 - alternate-day work

**A alone in 10 days, B alone in 15; they work on alternate days, A first. Total time?** One A+B cycle
`= 1/10 + 1/15 = 1/6` per 2 days. After 10 days (5 cycles) = `5/6` done. Day 11 (A) adds `1/10` ->
`14/15`. Day 12 (B) adds `1/15` -> finished. **Total = 12 days.** *(Verified: 5/6 -> 0.9333 -> 1.0.)*

### 📝 Method 2 - circular track

**A track is 400 m; two runners at 5 m/s and 3 m/s from the same point.** Same direction meet time `=
400/(5 - 3) =` **200 s.** Opposite directions `= 400/(5 + 3) =` **50 s.** *(Verified.)*

### 📝 Method 3 - moving-object crossing

**A 200 m train at 90 km/h (= 25 m/s) overtakes a man running 5 m/s in the same direction.** Relative
speed `= 25 - 5 = 20 m/s`; time `= 200/20 =` **10 s.** *(Verified.)*

### 📝 Method 4 - who starts decides the finish (alternate-day escalation)

**A alone in 12 days, B alone in 18; they work on alternate days.** One cycle `= 1/12 + 1/18 = 5/36`
per 2 days, so 7 cycles (14 days) complete `35/36` either way. The **remaining `1/36` is done by
whoever's turn day 15 is**:

| Starter | Day-15 worker | Rate on day 15 | Extra time | **Total** |
|---|---|---|---|---|
| A first | A | `1/12 = 3/36` per day | `(1/36)/(3/36) = 1/3` day | **14 1/3 days** |
| B first | B | `1/18 = 2/36` per day | `(1/36)/(2/36) = 1/2` day | **14 1/2 days** |

*(Verified by day-by-day simulation: `43/3` and `29/2`.)*

- 🔑 **Escalation rule:** whenever a cycle repeats, the answer is decided by the **remainder**, not the
  cycle. Never divide total work by the cycle rate and stop.

### 📝 Method 5 - same speeds, different times (the segment-ordering trap)

**A walks 2 km at 4 km/h, then 3 km at 6 km/h, then 4 km at 8 km/h. B walks the same three distances
at 8, 6 and 4 km/h respectively.** Same total distance (9 km) and the same **set** of speeds:

- A: `2/4 + 3/6 + 4/8 = 0.5 + 0.5 + 0.5 = 1.5 h = 90 min`.
- B: `2/8 + 3/6 + 4/4 = 0.25 + 0.5 + 1.0 = 1.75 h = 105 min`.
- **A finishes 15 minutes earlier.** *(Verified.)*

- 🔑 **Why:** time is `distance/speed`, so a **slow speed on a long segment** dominates. Pairing the
  fastest speed with the longest segment always wins. The audited 2026 Set-A paper uses exactly this
  shape - two riders, the same three speeds, the segment order swapped.

## 4. Time-saving techniques (safe conditions)

- ⚠️ **Net-rate-per-cycle** for alternate work. *Safe once you handle the final partial day
  explicitly.*
- ⚠️ **Relative speed** turns two moving bodies into one. *Safe when motion is along the same line or a
  common track.*
- ⚠️ **Cube-layer formulas** give all four face-counts instantly. *Safe for a solid cube cut into equal
  unit cubes with `n >= 2`.*
- ⚠️ **Harmonic mean** `2 s1 s2/(s1+s2)` for equal-distance round trips. *Safe only when the two legs
  cover the same distance;* for three or more segments, or unequal distances, fall back to
  `total distance / total time`.
- ⚠️ **Rearrangement check** for segment-ordering comparisons: with a fixed set of distances and a
  fixed set of speeds, total time is smallest when the **longest** distance is paired with the
  **fastest** speed. *Safe for any number of segments - it lets you rank two travellers without
  computing either time in full.*

## 5. Boundary cases

- ⚠️ Alternate-day problems can finish **mid-cycle**; never just divide total work by the cycle rate.
  **Who starts changes the total** (Method 4) even though the cycle rate is identical.
- ⚠️ On a circular track, "meet at the starting point" differs from "meet anywhere" - the latter uses
  the relative-speed formula above; the former needs the LCM of the individual lap times.
- ⚠️ Cube formulas assume a **fully painted** solid cube; a hollow or partially painted cube breaks
  them. For `n = 2` the 1-face and 0-face counts are correctly **zero**.
- ⚠️ A clock right-angle equation has **two** roots per hour; discard any root with `M >= 60` - it
  belongs to the next hour.
- ⚠️ Average speed and average velocity differ whenever the path reverses; a closed round trip has
  a positive average speed and **zero** average velocity.

## 6. Advanced traps

- ❌ Dividing total work by the cycle rate and ignoring the partial final day. -> Finish day by day.
- ❌ Assuming the alternate-day total is the same whoever starts. -> The **remainder** is done at the
  starter's-turn rate; recompute.
- ❌ Using still-water speed for downstream/upstream. -> Add/subtract the stream speed.
- ❌ Adding speeds for same-direction overtaking. -> **Subtract** for same direction; add only for
  opposite.
- ❌ Averaging the segment speeds of a multi-leg journey. -> `total distance / total time`.
- ❌ Reporting the distance travelled when the stem asked how far the object is **from the start**.
  -> That is displacement.
- ❌ Forgetting that an `n^3` cube has `(n-2)^3` fully unpainted inner cubes. -> Use the layer formula
  and check the four counts sum to `n^3`.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Partial-day work | A | Simulate the last cycle explicitly. |
| Relative-speed sign | C | Write "opposite = add, same = subtract" each time. |
| Unit conversion | X | Convert to m/s before any length problem. |
| Cube face-count | C | Memorise the four-count formula; check the sum equals n^3. |

## 8. Advanced drill (with full solutions)

> ⚠️ These items are **new** - they do not repeat Methods 1-5 above or the Foundation file.

1. A boat's still-water speed is 10 km/h and the stream is 2 km/h. Time for a 48 km each-way round
   trip.
2. A 120 m train at 54 km/h and a 180 m train at 36 km/h move towards each other on parallel tracks.
   How long do they take to cross each other completely?
3. A painted cube is cut into `5 x 5 x 5 = 125` unit cubes. How many have 0, 1, 2 and 3 painted faces?
4. At what time just after 3 o'clock are the hands of a clock at right angles?
5. Two runners on a 400 m circular track run at 8 m/s and 5 m/s in the **same** direction from the
   same point. When do they first meet **anywhere**, and when do they first meet **at the starting
   point**?
6. A cyclist rides 15 km uphill at 10 km/h and returns down the same road at 30 km/h. Find the average
   speed for the whole trip, and the average **velocity**.

**Solutions.**

1. **10 hours.** Downstream 12 km/h -> `48/12 = 4 h`; upstream 8 km/h -> `48/8 = 6 h`; total `10 h`.
   *(Verified.)*
2. **12 s.** Opposite directions, so **add**: relative speed `= 90 km/h = 90 x 5/18 = 25 m/s`. The
   crossing covers **both** lengths: `(120 + 180)/25 = 300/25 = 12 s`. *(Verified.)* ⚠️ Subtracting
   the speeds (the same-direction rule) would give 5 m/s and 60 s - a fivefold error.
3. **3-face 8, 2-face 36, 1-face 54, 0-face 27.** `12(5-2) = 36`, `6(5-2)^2 = 54`, `(5-2)^3 = 27`,
   corners `= 8`; sum `= 8 + 36 + 54 + 27 = 125`. *(Verified - always check the sum equals `n^3`.)*
4. **32 and 8/11 minutes past 3 (about 3:32:44).** With `M` minutes past 3, the gap is
   `|30 x 3 - 5.5M| = |90 - 5.5M|`. Setting it to 90 gives `M = 0` (the hands are already at 90° at
   exactly 3:00) or `5.5M = 180`, i.e. `M = 360/11 = 32 8/11`. The other root, `|90 - 5.5M| = 270`,
   gives `M = 720/11 ≈ 65.45`, which is past 4 o'clock. *(Verified.)*
5. **Anywhere: `400/3 ≈ 133.3 s`. At the starting point: `400 s`.** Meeting *anywhere* uses the
   relative speed: `400/(8 - 5) = 400/3 s`. Meeting *at the start* needs both to have completed whole
   laps: lap times are `400/8 = 50 s` and `400/5 = 80 s`, so the first common moment is
   `LCM(50, 80) = 400 s`. *(Verified.)* ⚠️ These are **different questions with different answers** -
   exactly the boundary case flagged in Section 5.
6. **Average speed 15 km/h; average velocity 0.** Total distance `= 30 km`; total time
   `= 15/10 + 15/30 = 1.5 + 0.5 = 2 h`; `30/2 = 15 km/h`, which is the harmonic mean
   `2 x 10 x 30/(10 + 30) = 600/40 = 15` because the legs are equal in distance. The plain mean, 20,
   is wrong. The **displacement** is zero (he is back at the start), so the average **velocity** is
   **0**. *(Verified.)*

## 9. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ This family is relatively stable in the audited sample: 7/80 in 2024, 6/80 in 2025, and a
  provisional 8/80 in 2026. Broad competence still beats specialising.
- ⚠️ Recurring shapes: **time-work / pipes**, **speed-distance and trains/boats**, **clocks
  (coincidence/angle)**, **calendars (odd days)**, and **cube-cutting / mensuration counts**.
- ⚠️ Two shapes worth rehearsing because the audited 2026 paper uses both: a **segment-ordering
  comparison** (two travellers, the same speeds, different segment order - Method 5) and a
  **forward/backward step item** where the **net displacement**, not the path length, is asked.
- ⚠️ The papers reward the **rate-per-cycle** and **relative-speed** reductions; brute simulation is
  the time trap.

## 10. Study links

- ✅ [Foundation companion](../basic/04_Rates-Motion-Time-and-Geometry.md).
- ✅ [Arithmetic and Commercial Math](./03_Arithmetic-and-Commercial-Math.md) - averages/ratios underpin average speed.
- ✅ [Logical Reasoning, Coding, Counting and DI](./06_Logical-Reasoning-Coding-Counting-and-DI.md) - cube counts overlap with
  combinatorial counting.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2021, 2022, 2023
- **Paper(s):** CSAT
- **Routed question demands:** 45

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | CSAT | 5 | Velocity-time distance ratio | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 6 | Train crossing time | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 35 | Painted-cube face geometry | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 40 | Circular track speed ratio | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 58 | Inscribed triangle count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 59 | Calendar date sequence | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 60 | Rectangle diagonal geometry | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 12 | Calendar day determination | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 16 | Race distance inference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 30 | Right-triangle distance | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 35 | LCM cycle coincidence | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 36 | Race start scaling | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 49 | Fast clock time correction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 57 | Path displacement distance | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 59 | Calendar year repeat | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 20 | Calendar day calculation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 31 | Compass direction tracking | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 38 | Cube volume density ratio | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 71 | Combined work-rate fraction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 72 | Multi-leg average speed | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 73 | Circle-square intersection count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 74 | Upstream-downstream speed ratio | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 80 | Jump-sequence well climb | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 16 | Bounce count sequence | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 18 | Direction-distance path | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 20 | Net displacement direction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 29 | Two walkers meeting point | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 48 | Calendar day calculation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 57 | Clock-hand angle timing | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 63 | Collinear-points ratio count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 68 | Volume unit conversion | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 75 | LCM calendar meeting day | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 80 | Work-rate remaining days | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 6 | Direction distance tracking | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 7 | Calendar day finding | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 15 | Circular track overtaking | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 35 | Time unit total conversion | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 46 | Clock route time comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 57 | Work rate comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 59 | Rectangle cut feasibility | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 68 | Clock hand coincidence | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 20 | Cyclic work-rate schedule | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 49 | Day-of-week calculation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 50 | Periodic signal synchronisation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 67 | Tile packing maximum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Velocity-time distance ratio
- Train crossing time
- Painted-cube face geometry
- Circular track speed ratio
- Inscribed triangle count
- Calendar date sequence
- Rectangle diagonal geometry
- Calendar day determination
- Race distance inference
- Right-triangle distance
- LCM cycle coincidence
- Race start scaling
- Fast clock time correction
- Path displacement distance
- Calendar year repeat
- Calendar day calculation
- Compass direction tracking
- Cube volume density ratio
- Combined work-rate fraction
- Multi-leg average speed
- Circle-square intersection count
- Upstream-downstream speed ratio
- Jump-sequence well climb
- Bounce count sequence
- Direction-distance path
- Net displacement direction
- Two walkers meeting point
- Clock-hand angle timing
- Collinear-points ratio count
- Volume unit conversion
- LCM calendar meeting day
- Work-rate remaining days
- Direction distance tracking
- Calendar day finding
- Circular track overtaking
- Time unit total conversion
- Clock route time comparison
- Work rate comparison
- Rectangle cut feasibility
- Clock hand coincidence
- Cyclic work-rate schedule
- Day-of-week calculation
- Periodic signal synchronisation
- Tile packing maximum

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
