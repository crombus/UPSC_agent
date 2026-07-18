# Rates, Motion, Time and Geometry - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Basic numeracy / general mental ability.
> **Core skill:** time-and-work, pipes, speed-distance, trains/boats, clocks, calendars and mensuration -
> all as **rate x time** or a **geometric measure**.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: `advanced/04_Rates-Motion-Time-and-Geometry.md`.*

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

| Family | Formula |
|---|---|
| ✅ **Work** | If A finishes in `a` days, rate `= 1/a`; combined rate = sum of rates; time = 1/combined. |
| ✅ **Pipes** | Fillers add (+1/time), drains subtract (-1/time). |
| ✅ **Speed** | `Speed = Distance / Time`; `km/h x 5/18 = m/s`. |
| ✅ **Trains** | Cross a pole: length/speed. Cross a platform: `(length + platform)/speed`. |
| ✅ **Relative speed** | Opposite directions add speeds; same direction subtract. |
| ✅ **Clock angle** | Angle `= |30H - 5.5M|` degrees. |
| ✅ **Calendar** | Odd days decide the weekday; a non-leap year shifts the weekday by 1, a leap year by 2. |
| ✅ **Mensuration** | Rectangle: area `= l x b`, perimeter `= 2(l + b)`, diagonal `= sqrt(l^2 + b^2)`. Cube: volume `= a^3`, surface `= 6a^2`. |

> 🔑 **Unit reflex:** convert `km/h` to `m/s` with `x 5/18` **before** touching train/length problems -
> half of all motion errors are unit slips.

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
- ⚠️ The clock formula gives an angle; if it exceeds 180, take `360 - angle` for the smaller angle.

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

### 📝 Example D (clock)

**Angle between the hands at 4:20.** `|30 x 4 - 5.5 x 20| = |120 - 110| =` **10 degrees.**
*(Verified.)*

### 📝 Example E (mensuration)

**Rectangle 8 x 6.** Area `= 48`, perimeter `= 28`, diagonal `= sqrt(64 + 36) =` **10.** *(Verified.)*

## 6. Must-Know facts

- ✅ `km/h x 5/18 = m/s`; `m/s x 18/5 = km/h`.
- ✅ The clock hands **coincide 11 times** every 12 hours (22 times a day), not 12.
- ✅ 100 years contain **5 odd days**; 400 years contain **0** (the weekday pattern repeats every 400
  years).
- ✅ Cube side doubled -> surface x4, volume x8.
- ✅ For same-direction motion, the **faster catches the slower** at the difference of speeds.

## 7. Common traps

- ❌ Adding times instead of rates for "working together". -> Add **rates**, then invert.
- ❌ Forgetting the train's **own length** when crossing a platform/bridge. -> Add both lengths.
- ❌ Using `30H` alone for the clock angle. -> Include the minute term `-5.5M`.
- ❌ Assuming hands coincide 12 times in 12 hours. -> They coincide **11** times.
- ❌ Averaging two speeds by a plain mean for a round trip. -> Use the harmonic mean
  `2 x s1 x s2 / (s1 + s2)`.

## 8. Quick checks

- ✅ Can you convert 90 km/h to m/s in one step? (25 m/s.)
- ✅ Can you write the combined rate for two workers instantly?
- ✅ Can you state the clock angle formula without hesitation?

## 9. Mini-drill (with answers and explanations)

1. A is twice as fast as B; together they finish in 8 days. How long does A alone take?
2. A 150 m train crosses a 350 m bridge in 20 s. Find its speed.
3. Two 3x3x3 painted cubes: how many of the 27 unit cubes have **exactly two** painted faces?
4. If 15 August 2024 (a leap year) is a Thursday, what day is 15 August 2025?
5. Between 4 and 5 o'clock, at what minute do the hands coincide?

**Answers.**

1. **12 days.** A's rate `= 2B`; combined `= 3B = 1/8` -> `B = 1/24`, `A = 1/12`. *(Verified: 1/12 +
   1/24 = 1/8.)*
2. **25 m/s (90 km/h).** `(150 + 350)/20 = 25 m/s`. *(Verified.)*
3. **12.** Exactly-two-face cubes lie on edges: `12 x (3 - 2) = 12`. *(Verified.)*
4. **Friday.** 15 Aug 2024 -> 15 Aug 2025 spans 365 days (Feb 2025 is non-leap); `365 mod 7 = 1` ->
   Thursday + 1 = Friday. *(Verified.)*
5. **21 and 9/11 minutes (about 4:21:49).** Coincidence minute `= 60H/11 = 240/11 ≈ 21.82`.
   *(Verified.)*

## 10. Study links

- ✅ Advanced companion: `advanced/04_Rates-Motion-Time-and-Geometry.md` - alternate-day work,
  boats/streams, circular tracks, and cube-cutting counts.
- ✅ `03_Arithmetic-and-Commercial-Math.md` (basic) - ratios/averages feed speed and work.
- ✅ `02_Number-Systems-and-Number-Sense.md` (basic) - odd-days counting is modular arithmetic.
