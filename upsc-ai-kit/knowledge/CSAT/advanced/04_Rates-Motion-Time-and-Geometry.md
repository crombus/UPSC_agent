# Rates, Motion, Time and Geometry - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Basic numeracy / general mental ability.
> **Core skill:** alternate-day work, boats/streams, circular-track meetings, moving-object crossings,
> clock coincidences and cube-cutting counts.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: `basic/04_Rates-Motion-Time-and-Geometry.md`.*

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

**Analytical claim:** every multi-body item reduces to **one net rate** (per cycle or relative), after
which it is a single division.

## 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Alternate-day work** | Sum a full A+B cycle, count whole cycles, finish the remainder day by day. | Track who works on the final partial day. |
| ✅ **Boats/streams** | Downstream `= b + s`, upstream `= b - s` (`b` = still-water, `s` = stream). | `b > s` for forward motion. |
| ✅ **Circular track** | Same direction meet time `= L/(v1 - v2)`; opposite `= L/(v1 + v2)`. | Same start point and constant speeds. |
| ✅ **Moving-object crossing** | Time = combined length / **relative** speed. | Add speeds if opposite, subtract if same direction. |
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

## 4. Time-saving techniques (safe conditions)

- ⚠️ **Net-rate-per-cycle** for alternate work. *Safe once you handle the final partial day
  explicitly.*
- ⚠️ **Relative speed** turns two moving bodies into one. *Safe when motion is along the same line or a
  common track.*
- ⚠️ **Cube-layer formulas** give all four face-counts instantly. *Safe for a solid cube cut into equal
  unit cubes with `n >= 2`.*
- ⚠️ **Harmonic mean** `2 s1 s2/(s1+s2)` for equal-distance round trips. *Safe only when the two legs
  cover the same distance.*

## 5. Boundary cases

- ⚠️ Alternate-day problems can finish **mid-cycle**; never just divide total work by the cycle rate.
- ⚠️ On a circular track, "meet at the starting point" differs from "meet anywhere" - the latter uses
  the relative-speed formula above.
- ⚠️ Cube formulas assume a **fully painted** solid cube; a hollow or partially painted cube breaks
  them.

## 6. Advanced traps

- ❌ Dividing total work by the cycle rate and ignoring the partial final day. -> Finish day by day.
- ❌ Using still-water speed for downstream/upstream. -> Add/subtract the stream speed.
- ❌ Adding speeds for same-direction overtaking. -> **Subtract** for same direction.
- ❌ Forgetting that `n^3` cube has `(n-2)^3` fully unpainted inner cubes. -> Use the layer formula.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Partial-day work | A | Simulate the last cycle explicitly. |
| Relative-speed sign | C | Write "opposite = add, same = subtract" each time. |
| Unit conversion | X | Convert to m/s before any length problem. |
| Cube face-count | C | Memorise the four-count formula; check the sum equals n^3. |

## 8. Advanced drill (with full solutions)

1. A can do a job in 10 days, B in 15; they work alternately with A starting. When is it finished?
2. A boat's still-water speed is 10 km/h and the stream is 2 km/h. Time for a 48 km each-way round
   trip.
3. A cube is painted and cut into 4x4x4 = 64 unit cubes. How many have 0, 1, 2, 3 painted faces?
4. Two runners on a 400 m circular track at 5 m/s and 3 m/s start together, opposite directions. First
   meeting time?
5. A 200 m train at 90 km/h overtakes a man running 5 m/s in the same direction. Time to pass him.

**Solutions.**

1. **12 days.** Cycle rate `1/6` per 2 days; finishes on day 12 (see Method 1). *(Verified.)*
2. **10 hours.** Downstream 12 km/h -> `48/12 = 4 h`; upstream 8 km/h -> `48/8 = 6 h`; total `10 h`.
   *(Verified.)*
3. **0-face 8, 1-face 24, 2-face 24, 3-face 8.** `(4-2)^3 = 8`, `6(4-2)^2 = 24`, `12(4-2) = 24`,
   corners `= 8`; sum `= 64`. *(Verified.)*
4. **50 s.** `400/(5 + 3) = 50`. *(Verified.)*
5. **10 s.** Relative `25 - 5 = 20 m/s`; `200/20 = 10`. *(Verified.)*

## 9. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ This family's weight **swings by year** - light in some papers, heavy in others (e.g., the 2026
  paper leaned toward motion/geometry). Broad competence beats specialising.
- ⚠️ Recurring shapes: **time-work / pipes**, **speed-distance and trains/boats**, **clocks
  (coincidence/angle)**, **calendars (odd days)**, and **cube-cutting / mensuration counts**.
- ⚠️ The papers reward the **rate-per-cycle** and **relative-speed** reductions; brute simulation is
  the time trap.

## 10. Study links

- ✅ Foundation companion: `basic/04_Rates-Motion-Time-and-Geometry.md`.
- ✅ `advanced/03_Arithmetic-and-Commercial-Math.md` - averages/ratios underpin average speed.
- ✅ `advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md` - cube counts overlap with
  combinatorial counting.
