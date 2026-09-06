---
title: "Rates-Motion-Time-and-Geometry — CSAT Learner-v2 Semantic Successor"
topic_key: csat-04
---

# Rates-Motion-Time-and-Geometry — Complete CSAT Learning Session

**Identity:** `csat-04:learner-v2:g1`  
**Generation date:** 2026-09-06  
**Approval:** false  
**Official syllabus anchor:** Basic numeracy and general mental ability at Class X level.

| Source | SHA-256 at generation |
|---|---|
| `upsc-ai-kit\knowledge\CSAT\basic\04_Rates-Motion-Time-and-Geometry.md` | `5de683879bab3ffad56f2998e92effef79949e7902f4caadadaab6e3c0791b75` |
| `upsc-ai-kit\knowledge\CSAT\advanced\04_Rates-Motion-Time-and-Geometry.md` | `e8eded82a583d79c3550851662fa1c13a53540a0f9b18e7c2420f12179d42a4f` |
| `upsc-ai-kit\knowledge\CSAT\00_Master-Framework.md` | `aaa2016904629d268db79a5798150ef8b9a1386fd1edb2ec737062f2cc9e3fcf` |
| `upsc-ai-kit\knowledge\CSAT\OFFICIAL-UPSC-SYLLABUS-MAPPING.md` | `80dd81eb9ccd7e977570eb86cac69418178dc665d981094c6438a95ca4b8b8a8` |
| `upsc-ai-kit\knowledge\CSAT\00_Question-Audit-Ledger.md` | `fbecba6a750ae88aba541dd1ef1379e6e73841ac7a4285b99bec8fd59bea7e6f` |

The canonical Basic owner is taught first. Optional Advanced material is isolated after practice.
All official-PYQ references preserve the repository's supplied/provisional key labels; no unavailable
wording, official explanation or official key is invented.

## BASIC LEARNING SESSION

### Twelve-panel ASCII master flow

```text
+----------------------------------------------------------------------------------+
| PANEL 01 — RATE MODEL                                                            |
| Quantity equals rate multiplied by time.                                         |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 02 — TIME AND WORK                                                         |
| Add work rates, not completion times.                                            |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 03 — PIPES AND LEAKS                                                       |
| Treat filling positive and emptying negative.                                    |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 04 — SPEED AND DISTANCE                                                    |
| Match units before using distance equals speed times time.                       |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 05 — RELATIVE MOTION                                                       |
| Add opposite-direction speeds and subtract same-direction speeds.                |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 06 — TRAINS AND BOATS                                                      |
| Include object length and current speed correctly.                               |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 07 — RACES AND TRACKS                                                      |
| Use relative distance on linear or circular paths.                               |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 08 — CLOCKS                                                                |
| Use the 5.5-degree-per-minute relative hand speed.                               |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 09 — CALENDARS                                                             |
| Reduce day shifts modulo seven and handle leap-year rules.                       |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 10 — GEOMETRY                                                              |
| Use properties before coordinates or formulas.                                   |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 11 — MENSURATION                                                           |
| Distinguish length, area and volume units.                                       |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 12 — VERIFICATION                                                          |
| Check dimensions, magnitude, endpoints and physical possibility.                 |
+----------------------------------------------------------------------------------+
```

### Canonical Basic owner

### Rates, Motion, Time and Geometry - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Basic numeracy / general mental ability.
> **Core skill:** time-and-work, pipes, speed-distance, trains/boats, clocks, calendars and mensuration -
> all as **rate x time** or a **geometric measure**.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Advanced Drill](../advanced/04_Rates-Motion-Time-and-Geometry.md).*

---

### 1. Visual foundation

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

### 2. Essential formulas

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

#### 2.1 Speed vs velocity - distance vs displacement

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

### 3. Method

1. Identify the family (work / motion / clock / calendar / shape).
2. Write **rates** (for work/motion) or plug the **fixed formula** (clock/calendar/shape).
3. For "together" or "relative" problems, **add or subtract rates/speeds** first, then invert.
4. Verify units and magnitude (time positive; distance sensible; angle ≤ 180 typically taken as the
   smaller angle).

### 4. Conditions to respect

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

### 5. Original solved examples

#### 📝 Example A (work)

**A finishes a job in 12 days, B in 18. Together?** Combined rate `= 1/12 + 1/18 = 5/36`; time `=
36/5 =` **7.2 days.** *(Verified.)*

#### 📝 Example B (pipes)

**Pipe A fills a tank in 6 h, B in 8 h. Together?** `1/6 + 1/8 = 7/24` -> time `= 24/7 ≈` **3.43 h.**
*(Verified.)* If instead A fills in 4 h and a drain empties in 6 h: `1/4 - 1/6 = 1/12` -> **12 h.**

#### 📝 Example C (train)

**A 120 m train at 72 km/h (= 20 m/s).** Crosses a pole: `120/20 =` **6 s.** Crosses a 180 m platform:
`(120 + 180)/20 =` **15 s.** *(Verified.)*

#### 📝 Example C.1 (boat and circular track)

A boat has still-water speed 10 km/h and stream speed 2 km/h. Its downstream and upstream speeds are
**12 km/h** and **8 km/h** respectively; reversing the signs is the standard trap.

On a 400 m track, runners at 5 m/s and 3 m/s starting together meet in the same direction after
`400/|5-3| =` **200 s**. Opposite-direction meeting would be `400/(5+3) = 50 s`. *(Verified.)*

#### 📝 Example D (clock)

**Angle between the hands at 4:20.** `|30 x 4 - 5.5 x 20| = |120 - 110| =` **10 degrees.**
*(Verified.)* At **2:50** the same formula gives `|60 - 275| = 215`, which is more than 180, so the
smaller angle is `360 - 215 =` **145 degrees.** *(Verified.)*

#### 📝 Example E (mensuration)

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

#### 📝 Example E.1 (tile packing)

**How many 20 cm by 10 cm tiles fit in a 1 m by 80 cm rectangle without cutting?** Convert first:
`1 m = 100 cm`. Along the sides, `100/20 = 5` and `80/10 = 8`, hence **40 tiles**. *(Verified.)*
The calculation would be invalid if the dimensions were mixed or cutting were allowed.

#### 📝 Foundation cube count (needed before the drill)

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

#### 📝 Example F (distance vs displacement, and average speed)

**A cyclist rides 12 km east in 30 min, then 12 km back west in 20 min.**

- **Distance** covered `= 24 km`; **displacement** `= 0` (he is back where he started).
- **Average speed** `= 24 km / (50/60 h) =` **28.8 km/h**.
- **Average velocity** `= 0 / time =` **0**.
- The plain mean of the leg speeds (24 and 36 km/h) is 30 - **wrong**. The harmonic mean
  `2 x 24 x 36 / (24 + 36) = 1728/60 =` **28.8**, which matches, because the two legs are equal in
  **distance**. *(Verified.)*

### 6. Must-Know facts

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

### 7. Common traps

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

### 8. Quick checks

- ✅ Can you convert 90 km/h to m/s in one step? (25 m/s.)
- ✅ Can you write the combined rate for two workers instantly?
- ✅ Can you state the clock angle formula without hesitation - including the `H mod 12` rule?
- ✅ Can you say, for a there-and-back trip, what the displacement is without computing anything? (Zero.)

### 9. Mini-drill (with answers and explanations)

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

### 10. Timed transfer, diagnosis and retry gate

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

### 11. Study links

- ✅ [Optional Advanced companion](../advanced/04_Rates-Motion-Time-and-Geometry.md) - alternate-day
  work, multi-segment comparisons, and harder cube/circular cases. Core above is sufficient to
  practise the basic paper forms.
- ✅ [Arithmetic and Commercial Math](./03_Arithmetic-and-Commercial-Math.md) - ratios/averages feed speed and work.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - odd-days counting is modular arithmetic.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
### 2026 PYQ Integration

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

#### What this owner must now support

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
### Recent PYQ Integration (2024-2025)

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

#### What this owner must now support

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
### Historical PYQ Integration (2018-2023)

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

#### What this owner must now support

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

---

### Semantic-completeness closure — 2026-09-06

#### Literal syllabus and canonical ownership

- **Literal clause:** Basic numeracy and general mental ability at Class X level.
- **Canonical scope:** Owns time-work, pipes, speed-distance, relative speed, trains, boats, races, clocks, calendars, elementary geometry, mensuration and unit conversion.
- **Cross-topic boundary:** Commercial arithmetic belongs to Topic 03; algebraic comparison and sufficiency to Topic 05; spatial direction puzzles to Topic 06.

#### Complete learner route

1. **Rate model:** Quantity equals rate multiplied by time.
2. **Time and work:** Add work rates, not completion times.
3. **Pipes and leaks:** Treat filling positive and emptying negative.
4. **Speed and distance:** Match units before using distance equals speed times time.
5. **Relative motion:** Add opposite-direction speeds and subtract same-direction speeds.
6. **Trains and boats:** Include object length and current speed correctly.
7. **Races and tracks:** Use relative distance on linear or circular paths.
8. **Clocks:** Use the 5.5-degree-per-minute relative hand speed.
9. **Calendars:** Reduce day shifts modulo seven and handle leap-year rules.
10. **Geometry:** Use properties before coordinates or formulas.
11. **Mensuration:** Distinguish length, area and volume units.
12. **Verification:** Check dimensions, magnitude, endpoints and physical possibility.

#### Verification and hostile-query gate

Rate equations retain units. Geometry formulas are derived or decomposed, and generated solutions are checked dimensionally and by direct substitution.

The hostile absence search explicitly tested these families and close-option terms:
**time and work; pipes; relative speed; train; boat; clock; calendar; mensuration**. A shortcut is usable only when its stated condition survives; otherwise return to
the first-principles representation. Every worked answer must finish with an independent check:
passage support, substitution, enumeration, units, bounds, reverse operation or option elimination.

#### Difficulty and timed progression

1. Foundation: recognise the family and state the governing definition or relation.
2. Core: solve a direct item with a visible representation and one verification.
3. Advanced: combine two mechanisms, test edge cases and reject close distractors.
4. Timed: use classify → extract → represent → execute → verify → decide.
5. Remediation: log the error as concept, application, calculation, reading, passage, time or guess;
   return to the owning subtopic before retesting.

## BASIC MCQS / REMEDIATION

### Diagnostic and core set

### Q1. Practice variant 1: A finishes a job in 12 days and B in 18 days. Working together, about how many days do they take (nearest day)?

A. 7
B. 8
C. 6
D. 9

**Correct answer: A.** Add work rates 1/d1 + 1/d2, then invert.


### Q2. Practice variant 1: A pipe fills a tank in 10 hours and a leak empties it in 20 hours. How many hours together (nearest hour)?

A. 21
B. 20
C. 19
D. 22

**Correct answer: B.** Net rate equals fill rate minus leak rate.


### Q3. Practice variant 1: A vehicle travels at 45 km/h for 4 hours. What distance does it cover?

A. 181
B. 179
C. 180
D. 182

**Correct answer: C.** Distance = speed x time after matching units.


### Q4. Practice variant 1: A train 120 m long crosses a pole at 54 km/h. How many seconds does it take?

A. 9
B. 7
C. 10
D. 8

**Correct answer: D.** Convert km/h to m/s, then time = train length/speed.


### Q5. Practice variant 1: A boat moves at 12 km/h in still water and the stream is 2 km/h. What is its downstream speed?

A. 14
B. 15
C. 13
D. 16

**Correct answer: A.** Downstream speed equals still-water speed plus stream speed.


### Q6. Practice variant 1: What is the smaller angle between clock hands at 2:20?

A. 51
B. 50
C. 49
D. 52

**Correct answer: B.** Hour hand angle is 30h+0.5m; minute hand angle is 6m.


### Q7. Practice variant 1: If today is Monday, what weekday is it after 100 days?

A. Tuesday
B. Thursday
C. Wednesday
D. Friday

**Correct answer: C.** Weekdays repeat modulo seven.


### Q8. Practice variant 1: What is the area in square metres of a rectangle 12 m by 8 m?

A. 97
B. 95
C. 98
D. 96

**Correct answer: D.** Rectangle area = length x breadth; the unit is squared.


### Q9. Practice variant 2: A finishes a job in 13 days and B in 19 days. Working together, about how many days do they take (nearest day)?

A. 8
B. 9
C. 7
D. 10

**Correct answer: A.** Add work rates 1/d1 + 1/d2, then invert.


### Q10. Practice variant 2: A pipe fills a tank in 11 hours and a leak empties it in 22 hours. How many hours together (nearest hour)?

A. 23
B. 22
C. 21
D. 24

**Correct answer: B.** Net rate equals fill rate minus leak rate.


### Q11. Practice variant 2: A vehicle travels at 50 km/h for 4 hours. What distance does it cover?

A. 201
B. 199
C. 200
D. 202

**Correct answer: C.** Distance = speed x time after matching units.


### Q12. Practice variant 2: A train 130 m long crosses a pole at 54 km/h. How many seconds does it take?

A. 10
B. 8
C. 11
D. 9

**Correct answer: D.** Convert km/h to m/s, then time = train length/speed.


### Q13. Practice variant 2: A boat moves at 13 km/h in still water and the stream is 2 km/h. What is its downstream speed?

A. 15
B. 16
C. 14
D. 17

**Correct answer: A.** Downstream speed equals still-water speed plus stream speed.


### Q14. Practice variant 2: What is the smaller angle between clock hands at 3:20?

A. 21
B. 20
C. 19
D. 22

**Correct answer: B.** Hour hand angle is 30h+0.5m; minute hand angle is 6m.


### Q15. Practice variant 2: If today is Monday, what weekday is it after 101 days?

A. Tuesday
B. Wednesday
C. Thursday
D. Friday

**Correct answer: C.** Weekdays repeat modulo seven.


### Q16. Practice variant 2: What is the area in square metres of a rectangle 13 m by 9 m?

A. 118
B. 116
C. 119
D. 117

**Correct answer: D.** Rectangle area = length x breadth; the unit is squared.


### Remediation protocol

1. Recompute without options.
2. Name the failed rule or passage phrase.
3. Reject every distractor for a specific reason.
4. Retry with altered numbers, wording or constraints.
5. Advance only after two consecutive correct answers under the time ceiling.

## PYQS AND ANSWER PRACTICE

### Verified 2024-2026 Set-A demand and key ledger

| Year | Q | Neutral verified demand | Key status | Solution architecture |
|---:|---:|---|---|---|
| 2024 | 5 | Cube partition cuts | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 7 | Work-rate scaling | C (supplied) | Add rates and invert the net rate. |
| 2024 | 8 | Alternating-worker schedule | C (supplied) | Add rates and invert the net rate. |
| 2024 | 30 | Metric-unit conversion | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 37 | Clock-hand coincidence | A (supplied) | Use relative angular speed. |
| 2024 | 38 | Calendar repetition | C (supplied) | Reduce the day shift modulo seven. |
| 2024 | 40 | Clock-hand angle | C (supplied) | Use relative angular speed. |
| 2025 | 9 | Run-rate time relation | D (supplied) | Draw a labelled generation graph. |
| 2025 | 15 | Painted-cube partition | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 37 | Circular-track encounters | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 39 | Overtaking relative speed | C (supplied) | Use relative speed after unit conversion. |
| 2025 | 45 | Pipes-and-cistern rate | D (supplied) | Assign positive fill and negative empty rates. |
| 2025 | 59 | Fractional work rates | B (supplied) | Add rates and invert the net rate. |
| 2026 | 13 | Net displacement with jumps | D (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 20 | Relative-speed train crossing | C (provisional) | Use relative speed after unit conversion. |
| 2026 | 24 | Cube-cutting sequence count | A (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 37 | Circular-track relative motion | A (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 41 | Sound-distance relative rate | C (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 50 | Multi-segment speed comparison | D (provisional) | Use relative speed after unit conversion. |
| 2026 | 68 | Rectangular-tile area count | A (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 69 | Train-accident relative rate | A (provisional) | Use the total crossing length. |

> The table is a non-verbatim routing audit. It records the locally checked Set-A key letter and a
> valid solving route, but does not pretend that UPSC publishes model solutions. The separate
> workbook supplies original solved equivalents for every mechanism.

### Timed mixed transfer

### Q33. Practice variant 5: A finishes a job in 16 days and B in 22 days. Working together, about how many days do they take (nearest day)?

A. 9
B. 10
C. 8
D. 11

**Correct answer: A.** Add work rates 1/d1 + 1/d2, then invert.


### Q34. Practice variant 5: A pipe fills a tank in 14 hours and a leak empties it in 28 hours. How many hours together (nearest hour)?

A. 29
B. 28
C. 27
D. 30

**Correct answer: B.** Net rate equals fill rate minus leak rate.


### Q35. Practice variant 5: A vehicle travels at 65 km/h for 4 hours. What distance does it cover?

A. 261
B. 259
C. 260
D. 262

**Correct answer: C.** Distance = speed x time after matching units.


### Q36. Practice variant 5: A train 160 m long crosses a pole at 54 km/h. How many seconds does it take?

A. 12
B. 10
C. 13
D. 11

**Correct answer: D.** Convert km/h to m/s, then time = train length/speed.


### Q37. Practice variant 5: A boat moves at 16 km/h in still water and the stream is 2 km/h. What is its downstream speed?

A. 18
B. 19
C. 17
D. 20

**Correct answer: A.** Downstream speed equals still-water speed plus stream speed.


### Q38. Practice variant 5: What is the smaller angle between clock hands at 6:20?

A. 71
B. 70
C. 69
D. 72

**Correct answer: B.** Hour hand angle is 30h+0.5m; minute hand angle is 6m.


### Q39. Practice variant 5: If today is Monday, what weekday is it after 104 days?

A. Tuesday
B. Wednesday
C. Sunday
D. Thursday

**Correct answer: C.** Weekdays repeat modulo seven.


### Q40. Practice variant 5: What is the area in square metres of a rectangle 16 m by 12 m?

A. 193
B. 191
C. 194
D. 192

**Correct answer: D.** Rectangle area = length x breadth; the unit is squared.


## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

### Rates, Motion, Time and Geometry - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Basic numeracy / general mental ability.
> **Core skill:** alternate-day work, boats/streams, circular-track meetings, moving-object crossings,
> clock coincidences and cube-cutting counts.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/04_Rates-Motion-Time-and-Geometry.md).*

---

### 1. Architecture

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

### 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Alternate-day work** | Sum a full A+B cycle, count whole cycles, finish the remainder day by day. | Track who works on the final partial day - **who starts changes the answer**. |
| ✅ **Boats/streams** | Downstream `= b + s`, upstream `= b - s` (`b` = still-water, `s` = stream). | `b > s` for forward motion. |
| ✅ **Circular track** | Same direction meet time `= L/|v1 - v2|`; opposite `= L/(v1 + v2)`. | Same start point and constant speeds. A start-point reunion needs `t/LapTime1` and `t/LapTime2` both integral; use an LCM only when the lap times are commensurable. |
| ✅ **Moving-object crossing** | Time = combined length / **relative** speed. | Add speeds if opposite, subtract if same direction. |
| ✅ **Multi-segment average speed** | `total distance / total time` - never the mean of the segment speeds. | Two journeys with the **same** speeds over the **same** distances can still take different times if the speeds are attached to different segments. |
| ✅ **Clock right angle** | `\|30H - 5.5M\| = 90` (or `270`). | 22 right angles per 12 hours; solutions outside `0 <= M < 60` belong to the next hour. |
| ✅ **Cube cut into n^3** | 3-face `= 8`; 2-face `= 12(n-2)`; 1-face `= 6(n-2)^2`; 0-face `= (n-2)^3`. | Integer `n >= 2`, a solid cube, equal cuts, and paint on all six faces; the four counts sum to `n^3`. |

### 3. Harder methods (worked)

#### 📝 Method 1 - alternate-day work

**A alone in 10 days, B alone in 15; they work on alternate days, A first. Total time?** One A+B cycle
`= 1/10 + 1/15 = 1/6` per 2 days. After 10 days (5 cycles) = `5/6` done. Day 11 (A) adds `1/10` ->
`14/15`. Day 12 (B) adds `1/15` -> finished. **Total = 12 days.** *(Verified: 5/6 -> 0.9333 -> 1.0.)*

#### 📝 Method 2 - circular track

**A track is 400 m; two runners at 5 m/s and 3 m/s from the same point.** Same direction meet time `=
400/(5 - 3) =` **200 s.** Opposite directions `= 400/(5 + 3) =` **50 s.** *(Verified.)*

#### 📝 Method 3 - moving-object crossing

**A 200 m train at 90 km/h (= 25 m/s) overtakes a man running 5 m/s in the same direction.** Relative
speed `= 25 - 5 = 20 m/s`; time `= 200/20 =` **10 s.** *(Verified.)*

#### 📝 Method 4 - who starts decides the finish (alternate-day escalation)

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

#### 📝 Method 5 - same speeds, different times (the segment-ordering trap)

**A walks 2 km at 4 km/h, then 3 km at 6 km/h, then 4 km at 8 km/h. B walks the same three distances
at 8, 6 and 4 km/h respectively.** Same total distance (9 km) and the same **set** of speeds:

- A: `2/4 + 3/6 + 4/8 = 0.5 + 0.5 + 0.5 = 1.5 h = 90 min`.
- B: `2/8 + 3/6 + 4/4 = 0.25 + 0.5 + 1.0 = 1.75 h = 105 min`.
- **A finishes 15 minutes earlier.** *(Verified.)*

- 🔑 **Why:** time is `distance/speed`, so a **slow speed on a long segment** dominates. Pairing the
  fastest speed with the longest segment always wins. The audited 2026 Set-A paper uses exactly this
  shape - two riders, the same three speeds, the segment order swapped.

#### 📝 Method 6 - calendar and dimensional geometry under pressure

**Calendar.** What weekday is 1 March 2101 if 1 March 2100 is Monday? Year 2100 is a century not
divisible by 400, so it is **not leap**. The interval has 365 days, or one odd day: **Tuesday**.
Do not treat “divisible by 4” as the whole Gregorian test.

**Tile feasibility.** A `9 m x 7 m` rectangle is to be covered by `3 m x 1 m` tiles, with rotation
allowed and no cutting. With the 3 m side along 9 m, the count is `3 x 7 = 21`; after rotation,
`7/3` is not integral, so that orientation fails. Therefore **21 tiles** is feasible only in the
first orientation. State the orientation, not merely `area/tile area`.

### 4. Time-saving techniques (safe conditions)

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

### 5. Boundary cases

- ⚠️ Alternate-day problems can finish **mid-cycle**; never just divide total work by the cycle rate.
  **Who starts changes the total** (Method 4) even though the cycle rate is identical.
- ⚠️ On a circular track, "meet at the starting point" differs from "meet anywhere" - the latter uses
  relative speed. For a start-point reunion, solve for a common multiple of the lap times; an LCM is
  valid only when those times are commensurable. Otherwise a finite reunion need not exist.
- ⚠️ Cube formulas assume a **fully painted** solid cube; a hollow or partially painted cube breaks
  them. For `n = 2` the 1-face and 0-face counts are correctly **zero**.
- ⚠️ A clock right-angle equation has **two** roots per hour; discard any root with `M >= 60` - it
  belongs to the next hour.
- ⚠️ Average speed and average velocity differ whenever the path reverses; a closed round trip has
  a positive average speed and **zero** average velocity.

### 6. Advanced traps

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

### 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Partial-day work | A | Simulate the last cycle explicitly. |
| Relative-speed sign | C | Write "opposite = add, same = subtract" each time. |
| Unit conversion | X | Convert to m/s before any length problem. |
| Cube face-count | C | Memorise the four-count formula; check the sum equals n^3. |
| Calendar century rule | R | Test divisibility by 4, then the 100/400 exception. |
| Tile/geometry feasibility | A | Check side quotients and stated rotation/cutting conditions, not area alone. |

### 8. Advanced drill (with full solutions)

> ⚠️ These items are **new** - they do not repeat Methods 1-6 above or the Foundation file.

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
7. If 1 January 2099 is Friday, what weekday is 1 January 2100? What extra check is required before
   moving to 2101?
8. A `12 m x 9 m` floor is covered by `3 m x 2 m` tiles without cutting. Is the stated orientation
   feasible, and how many tiles are needed if rotation is allowed?

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

7. **Saturday.** 2099 is non-leap, so the one-year shift is one day. Before moving from 2100 to
   2101, check the century rule: 2100 is not divisible by 400 and is therefore non-leap.
8. **The stated orientation is not feasible; rotated, 18 tiles.** `9/2` is not integral, but on
   rotation `12/2 = 6` and `9/3 = 3`, so `6 x 3 = 18`. *(Verified.)*

### 9. Timed transfer and retry gate

Attempt the eight drills in **12 minutes**. For every error, label it C, A, X, R, or T using the
table above. Retry only the missed family after rebuilding its diagram/equation. Move on only after
at least **7/8**, with no unit, century-rule, or condition error; otherwise repeat the matching
method and take a fresh equivalent set.

### 10. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ This family is relatively stable in the audited sample: 7/80 in 2024, 6/80 in 2025, and a
  provisional 8/80 in 2026. Broad competence still beats specialising.
- ⚠️ Recurring shapes: **time-work / pipes**, **speed-distance and trains/boats**, **clocks
  (coincidence/angle)**, **calendars (odd days)**, and **cube-cutting / mensuration counts**.
- ⚠️ Two shapes worth rehearsing because the audited 2026 paper uses both: a **segment-ordering
  comparison** (two travellers, the same speeds, different segment order - Method 5) and a
  **forward/backward step item** where the **net displacement**, not the path length, is asked.
- ⚠️ The papers reward the **rate-per-cycle** and **relative-speed** reductions; brute simulation is
  the time trap.

### 11. Study links

- ✅ [Foundation companion](../basic/04_Rates-Motion-Time-and-Geometry.md).
- ✅ [Arithmetic and Commercial Math](./03_Arithmetic-and-Commercial-Math.md) - averages/ratios underpin average speed.
- ✅ [Logical Reasoning, Coding, Counting and DI](./06_Logical-Reasoning-Coding-Counting-and-DI.md) - cube counts overlap with
  combinatorial counting.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
### Historical PYQ Integration (2018-2023)

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

#### What this owner must now support

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

## CONSOLIDATED REGISTER NOTES

### Complete revision spine

- **Rate model:** Quantity equals rate multiplied by time.
- **Time and work:** Add work rates, not completion times.
- **Pipes and leaks:** Treat filling positive and emptying negative.
- **Speed and distance:** Match units before using distance equals speed times time.
- **Relative motion:** Add opposite-direction speeds and subtract same-direction speeds.
- **Trains and boats:** Include object length and current speed correctly.
- **Races and tracks:** Use relative distance on linear or circular paths.
- **Clocks:** Use the 5.5-degree-per-minute relative hand speed.
- **Calendars:** Reduce day shifts modulo seven and handle leap-year rules.
- **Geometry:** Use properties before coordinates or formulas.
- **Mensuration:** Distinguish length, area and volume units.
- **Verification:** Check dimensions, magnitude, endpoints and physical possibility.

### Ownership and close-option firewall

- **Own here:** Owns time-work, pipes, speed-distance, relative speed, trains, boats, races, clocks, calendars, elementary geometry, mensuration and unit conversion.
- **Do not duplicate:** Commercial arithmetic belongs to Topic 03; algebraic comparison and sufficiency to Topic 05; spatial direction puzzles to Topic 06.
- **Verification:** Rate equations retain units. Geometry formulas are derived or decomposed, and generated solutions are checked dimensionally and by direct substitution.

### Timed answer route

`CLASSIFY → EXTRACT → REPRESENT → EXECUTE → VERIFY → DECIDE`

- Use estimation or option elimination only after preserving the governing condition.
- A blank costs zero; a rushed unsupported answer also consumes time and may attract negative marks.
- For every error, record concept/application/calculation/reading/passage/time/guess, repair the
  owner, and retry a new item rather than memorising the old option.

