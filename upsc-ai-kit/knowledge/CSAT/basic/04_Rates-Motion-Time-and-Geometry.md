# Rates, Motion, Time and Geometry - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Basic numeracy / general mental ability.
> **Core skill:** time-and-work, pipes, speed-distance, trains/boats, clocks, calendars and mensuration -
> all as **rate x time** or a **geometric measure**.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Advanced Drill](../advanced/04_Rates-Motion-Time-and-Geometry.md).*

---

## 1. Visual foundation

```text
   "RATE x TIME = QUANTITY"  is the master template
        |
   +-------------+--------------+--------------+
   |             |              |              |
 WORK          MOTION         CLOCK/CAL      SHAPE
 1/days rate   speed          angle/odd-days perimeter/area/
 add rates     distance/time  fixed formulas volume/cube-cuts
```

**Core proposition:** work, pipes and motion are the **same equation** (`rate x time = amount`);
clocks, calendars and mensuration are **fixed-formula** families.

## 2. Essential formulas

| Family | Formula | Edge condition |
|---|---|---|
| ✅ **Work** | If A finishes in `a` days, rate `= 1/a`; combined rate = sum of rates; time = 1/combined. | Rates add only for **simultaneous** work. |
| ✅ **Pipes** | Fillers add (+1/time), drains subtract (-1/time). | If the net rate is `<= 0` the tank never fills. |
| ✅ **Speed** | `Speed = Distance / Time`; `km/h x 5/18 = m/s`. | Speed uses **path length travelled**, never net displacement. |
| ✅ **Average speed** | `Total distance / total time`. For two **equal-distance** legs this is the harmonic mean `2 s1 s2/(s1 + s2)`. | The harmonic form fails for unequal distances - go back to total/total. |
| ✅ **Trains** | Cross a pole: length/speed. Cross a platform: `(length + platform)/speed`. | Always include the train's **own** length. |
| ✅ **Boats/streams** | Downstream speed `= b+s`; upstream speed `= b-s`. | `b` is still-water speed and must exceed stream speed for upstream progress. |
| ✅ **Relative speed** | Opposite directions add speeds; same direction subtract. | Requires motion along the **same line/track**. |
| ✅ **Circular track** | First meeting anywhere: `L/(v₁+v₂)` opposite directions, `L/|v₁-v₂|` same direction. | Same start point and constant speeds. A start-point reunion requires both runners to complete whole laps; use an LCM only for commensurable lap times. |
| ✅ **Clock angle** | Angle `= \|30H - 5.5M\|` degrees. | `H` is the hour on a **12-hour** dial (use `H mod 12`, so 14:00 -> H = 2); if the result exceeds 180, the smaller angle is `360 - angle`. |
| ✅ **Calendar** | Odd days decide the weekday; a non-leap year shifts the weekday by 1, a leap year by 2. | A Gregorian year is leap iff divisible by 4, **except** a century must also be divisible by 400; count a `+2` shift only when the span contains 29 February. |
| ✅ **Mensuration** | Rectangle: area `= l x b`, perimeter `= 2(l + b)`, diagonal `= sqrt(l^2 + b^2)`. Triangle: area `= bh/2`; trapezium with parallel sides `a,b`: area `= (a+b)h/2`; circle: area `= πr^2`, circumference `= 2πr`. Cuboid: volume `= lbh`, surface `= 2(lb+bh+hl)`; cube: volume `= a^3`, surface `= 6a^2`; right circular cylinder: volume `= πr^2h`; right circular cone: volume `= πr^2h/3`; sphere: volume `= 4πr^3/3`. | Keep every length in one unit. Area is in square units and volume in cubic units. In a trapezium, `h` is perpendicular to the parallel sides; cylinder/cone formulas require the radius and perpendicular height. Use `π = 22/7` only when the data permit it. |

> 🔑 **Unit reflex:** convert `km/h` to `m/s` with `x 5/18` **before** touching train/length problems -
> half of all motion errors are unit slips.

### 2.1 Speed vs velocity - distance vs displacement

| Quantity | Definition | Uses |
|---|---|---|
| ✅ **Distance** | Total **path length** covered, always `>= 0` and never decreasing. | Fuel, fare, time-taken, average speed. |
| ✅ **Displacement** | **Net** change of position, with direction; can be zero after a round trip. | "How far is he from the start?", forward-and-back step items. |
| ✅ **Speed** | `distance / time` - a magnitude only. | Every "average speed" question in this paper. |
| ✅ **Velocity** | `displacement / time` - carries a direction. | Items asking for net position or bearing. |

- ⚠️ **The audited papers exploit this.** The 2026 Set-A paper contains a forward/backward step item
  in which a toy makes a fixed number of jumps of two different lengths and ends a stated distance
  **forward**: the total path covered and the net advance are completely different numbers, and only
  the net advance is asked. Read whether the stem wants **how far travelled** or **how far from the
  start**.
- 🔑 **Test:** if the object ever reverses, the two answers differ. If it never reverses, they coincide.

## 3. Method

1. Identify the family (work / motion / clock / calendar / shape).
2. Write **rates** (for work/motion) or plug the **fixed formula** (clock/calendar/shape).
3. For "together" or "relative" problems, **add or subtract rates/speeds** first, then invert.
4. Verify units and magnitude (time positive; distance sensible; angle ≤ 180 typically taken as the
   smaller angle).

## 4. Conditions to respect

- ⚠️ Add work-rates only when workers **work simultaneously**; for alternate-day work, sum one full
  cycle first.
- ⚠️ Relative speed **adds** for opposite directions and **subtracts** for the same direction - and
  the objects must be moving along the **same line** for the simple rule.
- ⚠️ For a circular track, read **“meet anywhere”** versus **“meet at the starting point”**. The
  latter is a common-whole-laps condition, not the relative-speed meeting time.
- ⚠️ The clock formula takes `H` on a **12-hour dial** and gives an angle; if it exceeds 180, take
  `360 - angle` for the smaller angle.
- ⚠️ **Average speed is never the plain mean of the speeds** unless the **times** are equal. For equal
  **distances** use the harmonic mean; otherwise compute total distance over total time.
- ⚠️ Distinguish **distance travelled** from **displacement** before writing any equation (Section 2.1).
- ⚠️ For a calendar question, test the **year first**: 2000 is leap, but 1900 and 2100 are not.
- ⚠️ In tile-packing, divide the available dimensions by the tile dimensions in a single orientation;
  rotate only if the stem permits it, and take whole tiles only.

## 5. Original solved examples

### 📝 Example A (work)

**A finishes a job in 12 days, B in 18. Together?** Combined rate `= 1/12 + 1/18 = 5/36`; time `=
36/5 =` **7.2 days.** *(Verified.)*

### 📝 Example B (pipes)

**Pipe A fills a tank in 6 h, B in 8 h. Together?** `1/6 + 1/8 = 7/24` -> time `= 24/7 ≈` **3.43 h.**
*(Verified.)* If instead A fills in 4 h and a drain empties in 6 h: `1/4 - 1/6 = 1/12` -> **12 h.**

### 📝 Example C (train)

**A 120 m train at 72 km/h (= 20 m/s).** Crosses a pole: `120/20 =` **6 s.** Crosses a 180 m platform:
`(120 + 180)/20 =` **15 s.** *(Verified.)*

### 📝 Example C.1 (boat and circular track)

A boat has still-water speed 10 km/h and stream speed 2 km/h. Its downstream and upstream speeds are
**12 km/h** and **8 km/h** respectively; reversing the signs is the standard trap.

On a 400 m track, runners at 5 m/s and 3 m/s starting together meet in the same direction after
`400/|5-3| =` **200 s**. Opposite-direction meeting would be `400/(5+3) = 50 s`. *(Verified.)*

### 📝 Example D (clock)

**Angle between the hands at 4:20.** `|30 x 4 - 5.5 x 20| = |120 - 110| =` **10 degrees.**
*(Verified.)* At **2:50** the same formula gives `|60 - 275| = 215`, which is more than 180, so the
smaller angle is `360 - 215 =` **145 degrees.** *(Verified.)*

### 📝 Example E (mensuration)

**Rectangle 8 x 6.** Area `= 48`, perimeter `= 28`, diagonal `= sqrt(64 + 36) =` **10.** *(Verified.)*

**Geometry transfer.** A right triangle has legs 6 cm and 8 cm. Its hypotenuse is
`sqrt(6^2 + 8^2) = 10 cm`; its area is `6 x 8 / 2 = 24 cm²`. A circle of radius 7 cm has area
`(22/7) x 7² = 154 cm²`. *(Verified.)* Use Pythagoras only after identifying a right angle.

**Mensuration transfer.** A trapezium with parallel sides 8 cm and
12 cm and perpendicular height 5 cm has area
`(8 + 12) x 5 / 2 = 50 cm²`. A right circular cylinder of radius
3 cm and height 10 cm has volume `π x 3² x 10 = 90π cm³`;
the cone with the same base and height has one-third of that volume,
`30π cm³`. A sphere of radius 3 cm has volume
`4π x 3³ / 3 = 36π cm³`. *(Verified.)*

### 📝 Example E.1 (tile packing)

**How many 20 cm by 10 cm tiles fit in a 1 m by 80 cm rectangle without cutting?** Convert first:
`1 m = 100 cm`. Along the sides, `100/20 = 5` and `80/10 = 8`, hence **40 tiles**. *(Verified.)*
The calculation would be invalid if the dimensions were mixed or cutting were allowed.

### 📝 Foundation cube count (needed before the drill)

For a **fully painted solid** `n x n x n` cube cut along all grid planes:

| Location | Count | Why |
|---|---:|---|
| Corners: 3 painted faces | `8` | A cube has eight corners. |
| Edge interiors: exactly 2 faces | `12(n-2)` | Twelve edges, with `n-2` non-corner cubes each. |
| Face interiors: exactly 1 face | `6(n-2)^2` | Six faces, excluding edges. |
| Inner cubes: 0 faces | `(n-2)^3` | Remove one painted layer from each side. |

These counts require integer `n >= 2`, a solid cube, and paint on all six outer faces. They sum to
`n³`; that is the check before using them in the mini-drill. The Advanced companion extends, rather
than supplies, this foundation.

### 📝 Example F (distance vs displacement, and average speed)

**A cyclist rides 12 km east in 30 min, then 12 km back west in 20 min.**

- **Distance** covered `= 24 km`; **displacement** `= 0` (he is back where he started).
- **Average speed** `= 24 km / (50/60 h) =` **28.8 km/h**.
- **Average velocity** `= 0 / time =` **0**.
- The plain mean of the leg speeds (24 and 36 km/h) is 30 - **wrong**. The harmonic mean
  `2 x 24 x 36 / (24 + 36) = 1728/60 =` **28.8**, which matches, because the two legs are equal in
  **distance**. *(Verified.)*

## 6. Must-Know facts

- ✅ `km/h x 5/18 = m/s`; `m/s x 18/5 = km/h`.
- ✅ The clock hands **coincide 11 times** every 12 hours (22 times a day), not 12 - once every
  `720/11 = 65 5/11` minutes.
- ✅ The hands are at **right angles 22 times** in 12 hours (44 times a day).
- ✅ 100 years contain **5 odd days**; 400 years contain **0** (the weekday pattern repeats every 400
  years).
- ✅ A Gregorian century year is leap only when divisible by 400: 2000 is leap; 1900 and 2100 are not.
- ✅ Cube side doubled -> surface x4, volume x8.
- ✅ In a fully painted `n x n x n` cube, exactly-two-face cubes are `12(n-2)`; for `3 x 3 x 3`, that
  is 12.
- ✅ For same-direction motion, the **faster catches the slower** at the difference of speeds.
- ✅ **Displacement is never greater than distance**, and they are equal only when the motion never
  reverses.

## 7. Common traps

- ❌ Adding times instead of rates for "working together". -> Add **rates**, then invert.
- ❌ Forgetting the train's **own length** when crossing a platform/bridge. -> Add both lengths.
- ❌ Using `30H` alone for the clock angle. -> Include the minute term `-5.5M`.
- ❌ Feeding a 24-hour hour into the clock formula. -> Use `H mod 12` (17:40 -> H = 5).
- ❌ Assuming hands coincide 12 times in 12 hours. -> They coincide **11** times.
- ❌ Averaging two speeds by a plain mean for a round trip. -> Use the harmonic mean
  `2 x s1 x s2 / (s1 + s2)`, and only when the two legs are **equal in distance**.
- ❌ Answering with the **distance covered** when the stem asks how far the object ends up **from the
  start**. -> That is displacement.
- ❌ Assuming a leap-year span always shifts the weekday by 2. -> Only if 29 February falls inside it.
- ❌ Calling every year divisible by 4 a leap year. -> Apply the century/400 exception before counting
  odd days.
- ❌ Treating a tile-area quotient as a packing count when side lengths do not fit. -> Check both
  dimensions and whether rotation/cutting is allowed.

## 8. Quick checks

- ✅ Can you convert 90 km/h to m/s in one step? (25 m/s.)
- ✅ Can you write the combined rate for two workers instantly?
- ✅ Can you state the clock angle formula without hesitation - including the `H mod 12` rule?
- ✅ Can you say, for a there-and-back trip, what the displacement is without computing anything? (Zero.)

## 9. Mini-drill (with answers and explanations)

1. A is twice as fast as B; together they finish in 8 days. How long does A alone take?
2. A 150 m train crosses a 350 m bridge in 20 s. Find its speed.
3. A 3x3x3 painted cube is cut into 27 unit cubes. How many have **exactly two** painted faces?
4. If 15 August 2024 (a leap year) is a Thursday, what day is 15 August 2025?
5. Between 4 and 5 o'clock, at what minute do the hands coincide?
6. A grasshopper makes 20 hops in a straight line: each forward hop is 6 cm, each backward hop is
   4 cm, and it ends up 40 cm ahead of its start. How many forward hops did it make, and what total
   distance did it cover?
7. A car covers 60 km at 30 km/h and the next 60 km at 60 km/h. Find its average speed.

**Answers.**

1. **12 days.** A's rate `= 2B`; combined `= 3B = 1/8` -> `B = 1/24`, `A = 1/12`. *(Verified: 1/12 +
   1/24 = 1/8.)*
2. **25 m/s (90 km/h).** `(150 + 350)/20 = 25 m/s`. *(Verified.)*
3. **12.** Exactly-two-face cubes lie on edges: `12 x (3 - 2) = 12`. *(Verified.)*
4. **Friday.** 15 Aug 2024 -> 15 Aug 2025 spans 365 days (Feb 2025 is non-leap); `365 mod 7 = 1` ->
   Thursday + 1 = Friday. *(Verified.)*
5. **21 and 9/11 minutes (about 4:21:49).** Coincidence minute `= 60H/11 = 240/11 ≈ 21.82`.
   *(Verified.)*
6. **12 forward hops; 104 cm of distance covered.** Let `f` forward and `b = 20 - f` backward.
   **Displacement:** `6f - 4(20 - f) = 40` -> `10f - 80 = 40` -> `f = 12`, so `b = 8`.
   **Distance (path length):** `6 x 12 + 4 x 8 = 72 + 32 =` **104 cm**, while the displacement is only
   **40 cm**. *(Verified: `72 - 32 = 40`.)*
   ⚠️ Two different correct numbers from one motion - read which the stem wants.
7. **40 km/h.** Total distance `120 km`; total time `60/30 + 60/60 = 2 + 1 = 3 h`; `120/3 = 40`.
   The plain mean of 30 and 60 is 45 - **wrong**. The harmonic mean applies here because the legs are
   equal in distance: `2 x 30 x 60/(30 + 60) = 3600/90 = 40`. *(Verified.)*

## 10. Timed transfer, diagnosis and retry gate

**Set a 90-second ceiling per item.** Park an item at the ceiling; in a qualifying paper, a clean
next question is worth more than a heroic calculation.

1. If 1 March 2100 is Monday, what day is 1 March 2101?
2. A `4 x 5 x 6` cm cuboid is painted on every outer face and cut into 1 cm cubes. How many cubes
   have exactly three painted faces?
3. A `10 m x 8 m` floor is tiled by `2 m x 1 m` tiles without cutting. How many tiles are required?
4. A 180 m train at 54 km/h crosses a pole. Find the time.
5. A boat travels 24 km downstream and 24 km upstream at still-water speed 8 km/h in a 2 km/h stream.
   Find the total time.
6. Two runners at 7 m/s and 3 m/s start together on a 200 m track in the same direction. When do they
   first meet anywhere?

**Answers.** 1. **Tuesday**: 2100 is not leap, so the span has 365 days. 2. **8**: every cuboid has
eight corners. 3. **40**. 4. **12 s**: `54 km/h = 15 m/s`, then `180/15`. 5. **6.4 h**:
`24/10 + 24/6 = 2.4 + 4`. 6. **50 s**: `200/|7-3|`.

| If you missed because... | Code | Repair before retry |
|---|---|---|
| You counted 2100 as leap | C/R | Write `÷4; century -> ÷400` above the calendar. |
| You used area alone for tiles | A | Draw the two side quotients before multiplying. |
| You confused cube faces/corners | C | Rebuild the four-row cube table and check its total. |
| You left speed in km/h | X | Put every train speed in m/s before division. |

**Retry gate:** redo the six items after a 20-minute gap. Continue only at **6/6 within nine minutes**
and with no unresolved C or R error; otherwise redo the matching worked method, then retry a fresh
six-item set.

## 11. Study links

- ✅ [Optional Advanced companion](../advanced/04_Rates-Motion-Time-and-Geometry.md) - alternate-day
  work, multi-segment comparisons, and harder cube/circular cases. Core above is sufficient to
  practise the basic paper forms.
- ✅ [Arithmetic and Commercial Math](./03_Arithmetic-and-Commercial-Math.md) - ratios/averages feed speed and work.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - odd-days counting is modular arithmetic.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
## 2026 PYQ Integration

> **Status:** 2026 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2026.md`.
> **Answer-key rule:** The 2026 Prelims and CSAT Set-A keys held locally are **provisional**; no option or answer is recorded or inferred in this integration.

- **Year represented:** 2026
- **Paper(s):** CSAT
- **Routed question demands:** 8

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2026 | CSAT | 13 | Net displacement with jumps | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 20 | Relative-speed train crossing | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 24 | Cube-cutting sequence count | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 37 | Circular-track relative motion | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 41 | Sound-distance relative rate | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 50 | Multi-segment speed comparison | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 68 | Rectangular-tile area count | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 69 | Train-accident relative rate | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Net displacement with jumps
- Relative-speed train crossing
- Cube-cutting sequence count
- Circular-track relative motion
- Sound-distance relative rate
- Multi-segment speed comparison
- Rectangular-tile area count
- Train-accident relative rate

> This block integrates the 2026 examinable demand and paper metadata. It is kept separate from the 2018-2023 and 2024-2025 blocks and does not convert a provisionally-keyed, answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2026 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->
## Recent PYQ Integration (2024-2025)

> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2024-2025.md`.
> **Answer-key rule:** The official 2024-2025 Prelims Set-A keys are present in the repository and CSAT Set-A keys are supplied; even so, no option or answer is recorded or inferred in this integration.

- **Years represented:** 2024, 2025
- **Paper(s):** CSAT
- **Routed question demands:** 13

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2024 | CSAT | 5 | Cube partition cuts | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 7 | Work-rate scaling | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 8 | Alternating-worker schedule | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 30 | Metric-unit conversion | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 37 | Clock-hand coincidence | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 38 | Calendar repetition | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 40 | Clock-hand angle | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 9 | Run-rate time relation | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 15 | Painted-cube partition | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 37 | Circular-track encounters | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 39 | Overtaking relative speed | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 45 | Pipes-and-cistern rate | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 59 | Fractional work rates | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Cube partition cuts
- Work-rate scaling
- Alternating-worker schedule
- Metric-unit conversion
- Clock-hand coincidence
- Calendar repetition
- Clock-hand angle
- Run-rate time relation
- Painted-cube partition
- Circular-track encounters
- Overtaking relative speed
- Pipes-and-cistern rate
- Fractional work rates

> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->

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
