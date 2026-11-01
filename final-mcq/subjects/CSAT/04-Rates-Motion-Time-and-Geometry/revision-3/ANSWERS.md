# CSAT 04 — Revision 3: answers and explanations

Each entry gives the key, the reason, why each other option fails, the examiner trap, a shortcut and a time target. Every key was verified by computation; see `AUDIT.md`.

**R3-Q01 — B.**

- **A.** Time 450 m ÷ 20 m/s = 22.5 s, longer than R's 21.2 s.
- **B.** Correct. Time 530 m ÷ 25 m/s = 21.2 s, the least of the four.
- **C.** Time 510 m ÷ 15 m/s = 34 s, the second-slowest of the four.
- **D.** Time 480 m ÷ 12.5 m/s = 38.4 s, the longest time.

Trap: Ranking by top speed alone, or by train length alone, instead of adding the bridge length and dividing by speed.

Shortcut: Time = (train + bridge)/speed in m/s for each row.

Time target: 120 s.

**R3-Q02 — B.**

- **A.** The harmonic mean of the first and last legs alone (2 × 6 × 3 ÷ 9), which leaves out the middle leg.
- **B.** Correct. Equal distances: 1800 ÷ (600/6 + 600/6 + 600/3) = 1800 ÷ 400 = 4.5 m/s.
- **C.** The arithmetic mean of the three speeds ((6 + 6 + 3) ÷ 3 = 5); the legs take unequal times, so this is not valid.
- **D.** The speed of the first leg alone, which ignores the slower third leg.

Trap: Averaging the three speeds arithmetically even though the legs are equal in distance but not in time.

Shortcut: Equal legs: average = number of legs ÷ sum of reciprocal speeds.

Time target: 90 s.

**R3-Q03 — D.**

- **A.** Ignores the partial day and rounds to the number of full days that have elapsed before the finish.
- **B.** Counts the full days up to the finish without the final fraction of day 12.
- **C.** Rounds up to whole days, although the job finishes partway through day 12.
- **D.** Correct. After 9 days (three rotations) 93/120 is done; day 10 (X) and day 11 (Y) finish 118/120; day 12 (Z) needs 2/120 at 6/120 per day, which is 1/3 day: 11 1/3 days.

Trap: Assuming a rotation repeats exactly, so the total is a whole number of cycles.

Shortcut: Full rotations, then the remainder at the rate of the worker on the next day.

Time target: 150 s.

**R3-Q04 — D.**

- **A.** Ignores drain R after 11:00 am: the remaining 7/12 at 1/4 per hour takes 2 h 20 min, which gives 1:20 pm.
- **B.** Opens Q at 9:00 am by mistake: 9 to 11 gives 1/2, the rest at 5/36 per hour takes 3 h 36 min, giving 2:36 pm.
- **C.** Opens R at 10:00 am instead of 11:00 am, so the drain works one hour early; the tank is full at 4:00 pm.
- **D.** Correct. 9–10: 1/6. 10–11: P and Q give 1/4 per hour, total 5/12. From 11:00 the net rate is 1/4 − 1/9 = 5/36; the remaining 7/12 takes 4.2 h, so the tank is full at 3:12 pm.

Trap: Opening the valves at the wrong times, or running a drain before its opening time.

Shortcut: Track the cumulative fraction at each opening time; the net rate changes at each.

Time target: 150 s.

**R3-Q05 — B.**

- **A.** Uses a separation of 2 minutes per day, which counts only one clock's drift, not both.
- **B.** Correct. The clocks separate by 4 + 2 = 6 minutes per day; 60 ÷ 6 = 10 days.
- **C.** Uses 90 minutes as the target difference, which is not one hour.
- **D.** Doubles the one-hour target before dividing (120 ÷ 6 = 20 days).

Trap: Subtracting the two drifts when the clocks drift in opposite directions.

Shortcut: Opposite drifts add: separation per day = gain + loss.

Time target: 75 s.

**R3-Q06 — A.**

- **A.** Correct. The next joint date is after LCM(6, 8) = 24 days; 24 ≡ 3 (mod 7); Monday + 3 = Thursday.
- **B.** Assumes the events coincide after four weeks (28 days), but 28 is not a multiple of 6 or 8.
- **C.** Uses 29 days, one more than four weeks, which is not a common multiple of 6 and 8.
- **D.** Uses 23 days, one less than the least common multiple.

Trap: Using any common multiple, not the least common multiple, or miscounting the weekday offset.

Shortcut: Next joint date = LCM of the cycles; weekday shift = LCM mod 7.

Time target: 90 s.

**R3-Q07 — A.**

- **A.** Correct. 15 August 2024 to 15 August 2025 is 365 days (shift 1), and 15 August 2025 to 2026 is 365 days (shift 1); total shift 2; Thursday + 2 = Saturday.
- **B.** Counts only one ordinary-year shift from 2024 to 2026, which is one day short.
- **C.** Adds a leap-year shift for 2024 that does not lie inside the span from August 2024 to August 2026, giving a shift of 3.
- **D.** Assumes no shift at all, which ignores both years.

Trap: Counting a leap year in a span that does not contain its 29 February.

Shortcut: Shift per year: 1 ordinary, 2 when the span contains 29 February.

Time target: 75 s.

**R3-Q08 — C.**

- **A.** Uses the inner perimeter times the width (2 × (16 + 8) × 2), which double-counts the corners.
- **B.** The inner area (16 × 8 = 128 m²), which is the lawn that is not covered by the path.
- **C.** Correct. Outer area 240 m² minus inner area 16 × 8 = 128 m²: 240 − 128 = 112 m².
- **D.** Uses 18 × 8, which covers a band along only one side and the short ends.

Trap: Reporting the inner area, or using a perimeter formula for an area question.

Shortcut: Path = outer area − inner area.

Time target: 90 s.

**R3-Q09 — B.**

- **A.** Halves the sum of the coordinates (70 ÷ 2 = 35 m; 35 ÷ 5 = 7 s), mixing the path and the distance.
- **B.** Correct. Distance √(30² + 40²) = 50 m; 50 ÷ 5 = 10 s.
- **C.** Uses the path along the axes (30 + 40 = 70 m; 70 ÷ 5 = 14 s), which is not a straight flight.
- **D.** Doubles the distance (round trip, 100 m; 100 ÷ 5 = 20 s), which the question does not ask for.

Trap: Adding coordinates instead of applying Pythagoras, or doubling for a return journey that does not occur.

Shortcut: Straight-line distance first; then distance ÷ speed.

Time target: 75 s.

**R3-Q10 — A.**

- **A.** Correct. Lap times 400 s and 160 s; LCM(400, 160) = 800 s, when the walkers have completed 2 and 5 laps respectively.
- **B.** The lap time of the faster walker alone (400 ÷ 2.5 = 160 s), when the slower walker is not at the corner.
- **C.** The first meeting anywhere on the perimeter (400 ÷ (2.5 − 1)), which need not be at the corner.
- **D.** The lap time of the slower walker alone (400 ÷ 1 = 400 s), when the faster walker is not at the corner.

Trap: Using relative speed for a corner-reunion question, or looking at one walker's lap time alone.

Shortcut: Reunion at a point: LCM of lap times. Meeting anywhere: perimeter ÷ relative speed.

Time target: 150 s.

**R3-Q11 — B.**

- **A.** The joint time from the question, not B's time alone.
- **B.** Correct. A's rate = (2/3) ÷ 16 = 1/24; B's rate = 1/12 − 1/24 = 1/24; B alone takes 24 days.
- **C.** The number of days A needs for the remaining work, not B's time.
- **D.** Half of the joint time; this ignores that A and B have different rates.

Trap: Reading the 16-day remaining work as B's time.

Shortcut: Find A's rate from the remaining work; subtract from the joint rate.

Time target: 120 s.

**R3-Q12 — A.**

- **A.** Correct. Moving time 1 + 1 + 1 = 3 h; halts 20 min; total 3 1/3 h; distance 130 km; 130 ÷ (10/3) = 39 km/h.
- **B.** Ignores the halts: 130 ÷ 3 = 43 1/3 km/h.
- **C.** Uses a total distance of 135 km (a miscount), so 135 ÷ 3 = 45 km/h.
- **D.** Counts the first stage speed as the answer; 120 ÷ 3 = 40 km/h uses a wrong total distance.

Trap: Dropping the halts from the total time.

Shortcut: Include stops in the time denominator; keep the distance.

Time target: 120 s.

**R3-Q13 — D.**

- **A.** The corner count of the cuboid (8), which has three painted faces.
- **B.** The cube formula 12(n − 2) applied with n = 3, the middle side.
- **C.** Counts the edge lengths without subtracting the corners (4 × 5), so the 5-unit edges are over-counted.
- **D.** Correct. Each of the 4 edges along a dimension has (length − 2) two-face cubes: 4 × (3 + 1 + 0) = 16.

Trap: Counting edge cubes on an edge of length 2, which has no interior cube.

Shortcut: Two-face cubes: 4 × Σ(length − 2); a length of 2 contributes zero.

Time target: 105 s.

**R3-Q14 — D.**

- **A.** Uses only the 150 m train's length over one train's speed (150 ÷ 20 m/s), omitting the other train's length.
- **B.** Uses only the 250 m train's length over one train's speed (250 ÷ 20 m/s), omitting the other train's length.
- **C.** Uses 400 m over one train's speed (400 ÷ 20 m/s), omitting the second train's speed.
- **D.** Correct. Opposite directions: relative speed 144 km/h = 40 m/s; total length 150 + 250 = 400 m; 400 ÷ 40 = 10 s.

Trap: Using one train's speed or one train's length alone.

Shortcut: Opposite: relative speed = sum; distance = both lengths.

Time target: 105 s.

**R3-Q15 — D.**

- **A.** Uses 9 m/s × 4 s, which mixes the relative speed with a different time.
- **B.** Halves the distance, ignoring that A is the slower walker.
- **C.** Gives B's distance from its own start (5 × 10 = 50 m), not A's.
- **D.** Correct. They meet after 90 ÷ (4 + 5) = 10 s; A has walked 4 × 10 = 40 m.

Trap: Reporting B's distance, or dividing the separation equally.

Shortcut: Meeting time = gap ÷ sum of speeds; then A's distance = speed × time.

Time target: 75 s.

**R3-Q16 — A.**

- **A.** Correct. Each of the two orientations (the hand gap of 45° and of 315°) occurs 11 times in 12 hours.
- **B.** Counts only one of the two orientations, giving half of the true total.
- **C.** Counts one occurrence per hour, which is not the rate of this angle.
- **D.** Counts both orientations for a 24-hour day, which is the wrong period.

Trap: Assuming a non-right angle occurs only once per hour, or counting the 24-hour day.

Shortcut: Relative speed 5.5°/min: each angle ≠ 0 or 180 recurs 22 times in 12 hours.

Time target: 120 s.

**R3-Q17 — A.**

- **A.** Correct. Checking each month's 13th in 2027 gives exactly one Friday.
- **B.** Counts 2 by assuming a second month shares the same weekday pattern; no second 13th in 2027 is a Friday.
- **C.** Counts 3, the number that would need three months with 13ths on Friday; 2027 does not produce it.
- **D.** Counts the Fridays in a single month instead of the 13ths that fall on Fridays.

Trap: Assuming a fixed number of Friday 13ths per year.

Shortcut: Check each month's 13th with the weekday of 1 January plus the month offsets.

Time target: 120 s.

**R3-Q18 — B.**

- **A.** 2028 begins on a Saturday, not a Monday; 2027 begins on a Friday, and the one-day shift gives Saturday.
- **B.** Correct. 2027 begins on Friday and 2028 on Saturday (shift 1 after the ordinary year 2027, then shift 2 after the leap year 2028); 2029 begins on Monday.
- **C.** Begins on Tuesday; 2029 is Monday, so this is one day later than the first match.
- **D.** Begins on Wednesday; the first Monday start is earlier.

Trap: Applying a one-day shift after a leap year, when a leap year shifts the weekday by two.

Shortcut: Shift 1 after an ordinary year, 2 after a leap year, mod 7.

Time target: 90 s.

**R3-Q19 — C.**

- **A.** At 6:16 4/11 the minute hand is 90° from the hour hand, which is a right angle.
- **B.** At 6:49 1/11 the gap is 90° again, the second right angle, not a coincidence.
- **C.** Correct. Coincidence times are 720k/11 minutes past 12; the first after 6:00 is k = 6, at 4320/11 = 392 8/11 minutes, i.e. 6:32 8/11.
- **D.** 7:38 2/11 is the second coincidence after 6:00, so it skips the first one.

Trap: Confusing a right angle with a coincidence, or skipping to a later coincidence.

Shortcut: Coincidences every 65 5/11 minutes; take the first after 6:00.

Time target: 120 s.

**R3-Q20 — A.**

- **A.** Correct. Volume 2 × 1.5 × 1 = 3 m³ = 3000 L; 3000 ÷ 15 = 200 min.
- **B.** Converts 3 m³ as 300 litres (a decimal slip), giving 300 ÷ 15 = 20 min.
- **C.** Divides the 3000 L volume by 1.5 (the width) instead of the 15 L/min rate, giving 2000 min.
- **D.** Reads the 3000 L volume as minutes and ignores the flow rate altogether.

Trap: Dividing a volume in litres by the rate without first computing the volume.

Shortcut: Volume (L) ÷ inflow (L/min).

Time target: 90 s.

**R3-Q21 — A.**

- **A.** Correct. Displacement √(6² + 8²) = 10 km; 10 km ÷ 2 h = 5 km/h.
- **B.** Average speed: total path 14 km ÷ 2 h. It is not the average velocity.
- **C.** The displacement alone (10 km) without dividing by the time.
- **D.** The total path length alone (14 km) without dividing by the time.

Trap: Using path length for velocity, or forgetting the time divisor.

Shortcut: Average velocity = displacement ÷ time; magnitude from Pythagoras.

Time target: 90 s.

**R3-Q22 — D.**

- **A.** Applies the ratio 3 : 2 to the joint time as 10 × 6/5, which mixes rates with times.
- **B.** Gives B's time alone (2/50 per day), since B's rate is 2k.
- **C.** Repeats the joint time, which ignores that A works faster.
- **D.** Correct. Joint rate 1/10 = 5k, so k = 1/50 and A's rate is 3/50 per day; A alone takes 50/3 = 16 2/3 days.

Trap: Assigning the ratio to the times instead of the rates.

Shortcut: Rates in ratio 3 : 2 mean times in ratio 2 : 3.

Time target: 90 s.

**R3-Q23 — D.**

- **A.** Reverses the winner: B reaches 600 m at 110 s, before A's 150 s.
- **B.** Forgets B's 10-second delay (150 − 100 = 50), leaving a 50-second margin.
- **C.** Treats the 10-second delay as the margin, ignoring the speeds.
- **D.** Correct. A finishes at 600 ÷ 4 = 150 s; B finishes at 10 + 600 ÷ 6 = 110 s; B wins by 40 s.

Trap: Forgetting that the late starter's clock begins at a different moment.

Shortcut: Finish time = delay + distance ÷ speed for each runner.

Time target: 105 s.

**R3-Q24 — A.**

- **A.** Correct. Combined rate 1/12 + 1/16 = 7/48 per hour, the largest of the pair rates; time 48/7 h ≈ 6.9 h.
- **B.** Combined rate 1/12 + 1/24 = 1/8 per hour (8 h), slower than A and B.
- **C.** Combined rate 1/16 + 1/24 = 5/48 per hour (9.6 h), the slowest pair.
- **D.** Pipe C alone takes 24 hours, which is slower than every pair.

Trap: Comparing pipe times directly instead of comparing combined rates.

Shortcut: Pair rates add; the pair with the largest rate is fastest.

Time target: 90 s.

**R3-Q25 — A.**

- **A.** Correct. P takes 0.5 + 0.5 + 0.5 = 1.5 h; Q takes 0.25 + 0.5 + 1.0 = 1.75 h. P finishes 15 minutes earlier.
- **B.** Reverses the comparison: Q is the slower of the two.
- **C.** Doubles the difference by subtracting the wrong pair of totals.
- **D.** Assumes the same speeds on the same distances always produce the same time, ignoring the order.

Trap: Assuming the same speeds give the same time regardless of the segment order.

Shortcut: Long segments should meet the fast speed; compare the per-segment times.

Time target: 120 s.

**R3-Q26 — B.**

- **A.** The arithmetic mean of the three speeds (50 + 80 + 40) ÷ 3, which ignores the different durations.
- **B.** Correct. Distance 100 + 80 + 80 = 260 km; total time 5 h; 260 ÷ 5 = 52 km/h.
- **C.** Averages the two extremes of the speed range, ignoring the time spent at each speed.
- **D.** Averages the speed of the second segment with the first, ignoring the third.

Trap: Averaging the speeds without weighting each by its duration.

Shortcut: Distance = Σ speed × time; then divide by 5 h.

Time target: 90 s.

**R3-Q27 — C.**

- **A.** Counts only pairs that include A, omitting the pairs B and C and A and C.
- **B.** Counts days with at least two cleaners, including the three-cleaner days.
- **C.** Correct. Enumerating days 1 to 60 gives 14 days where exactly two cleaners are present (for example day 6: A and B; day 10: A and C; day 15: B and C); days 30 and 60 are excluded because all three work.
- **D.** Counts pairs of cleaners for each day, so days with the same pair are counted twice.

Trap: Counting days with all three working as 'exactly two', or double-counting a day with two pairs.

Shortcut: Count days by inclusion; for 60 days, the three-cleaner days are 30 and 60 only.

Time target: 150 s.

**R3-Q28 — D.**

- **A.** Uses 15 minutes instead of 10 (2 km in 15 min = 8 km/h).
- **B.** Uses 12 minutes instead of 10 (2 km in 12 min = 10 km/h).
- **C.** Uses 5 minutes instead of 10 minutes, doubling the speed.
- **D.** Correct. 5 × 400 m = 2 km in 10/60 h; speed = 2 ÷ (1/6) = 12 km/h.

Trap: Keeping time in minutes when the speed is in km/h.

Shortcut: km ÷ hours; 10 minutes = 1/6 hour.

Time target: 75 s.

**R3-Q29 — B.**

- **A.** Treats the 100 m perimeter as 1 km, a lap time of 200 s, giving 3 laps.
- **B.** Correct. The breadth is 50 − 30 = 20 m, so the perimeter of 100 m is the lap; at 5 m/s a lap takes 20 s, and 600 s ÷ 20 s = 30 laps.
- **C.** Uses a 200 m lap (doubling the perimeter), a lap time of 40 s, giving 15 laps.
- **D.** Uses 50 m as the lap length (the breadth-based sum), a lap time of 10 s, giving 60 laps.

Trap: Missing the breadth implied by the perimeter, or treating the length as the lap.

Shortcut: Breadth from perimeter; lap time = perimeter ÷ speed.

Time target: 105 s.

**R3-Q30 — A.**

- **A.** Correct. A's rate is 1.2b; combined rate 2.2b = 1/9, so b = 1/19.8 and A's rate 1.2b = 1/16.5; A alone takes 16.5 days.
- **B.** Scales the joint time by 5/3 (9 × 5/3), applying the 20% to the time instead of to the rate.
- **C.** Assumes equal rates, so A alone takes twice the joint time (9 × 2).
- **D.** Applies 20% less efficiency to A (0.8b), reversing the stated comparison.

Trap: Applying the 20% to the time instead of to the rate.

Shortcut: Rates scale with efficiency; A's time = joint time × (A+B rate)/A rate.

Time target: 120 s.

**R3-Q31 — C.**

- **A.** Divides the volume in litres by 100 (a decimal slip), giving 6 min.
- **B.** Divides by 10 instead of 40 (600 ÷ 10 = 60 min).
- **C.** Correct. Volume 1.2 × 1 × 0.5 = 0.6 m³ = 600 L; 600 ÷ 40 = 15 min.
- **D.** Uses 4 litres per minute from a decimal misreading of 40, giving 150 min.

Trap: Multiplying a dimension in metres by a rate in litres without converting the volume.

Shortcut: Volume in litres ÷ rate in litres per minute.

Time target: 90 s.

**R3-Q32 — C.**

- **A.** Uses the train's length alone (480 ÷ 40 = 12 m/s = 43.2 km/h), omitting the platform.
- **B.** Divides 800 m by 36 s, a slip from 40 s, then converts: 800/36 × 3.6 = 80 km/h.
- **C.** Correct. Distance 800 m in 40 s = 20 m/s; × 3.6 = 72 km/h.
- **D.** Leaves the speed in m/s, which is not the requested unit.

Trap: Omitting the platform length, or leaving the speed unconverted.

Shortcut: Train + platform over time; m/s × 3.6.

Time target: 90 s.

**R3-Q33 — D.**

- **A.** Counts 364 days as 363, a one-day slip, which gives Wednesday.
- **B.** Counts 365 days from 1 January to 31 December, which is one day too many.
- **C.** Counts 366 days, treating 2026 as a leap year.
- **D.** Correct. 2026 is not a leap year, so 1 January and 31 December differ by 364 days, which is 52 weeks exactly: the same weekday.

Trap: Counting 365 days from 1 January to 31 December.

Shortcut: Days from 1 Jan to 31 Dec in a non-leap year = 364 = 52 weeks.

Time target: 60 s.

**R3-Q34 — B.**

- **A.** At 3:15 the minute hand is at 90° and the hour hand at 97.5°, so the minute hand is 7.5° behind.
- **B.** Correct. Minute angle 6M, hour angle 90 + 0.5M; 6M − (90 + 0.5M) = 15 gives 5.5M = 105, so M = 19 1/11.
- **C.** At 3:20 the minute hand is at 120° and the hour hand at 100°, a gap of 20°.
- **D.** At 3:45 the minute hand is at 270° and the hour hand at 112.5°, a gap of 157.5°.

Trap: Using 6° per minute for the minute hand and forgetting the hour hand moves too.

Shortcut: Relative speed 5.5°/min; solve 5.5M = offset.

Time target: 120 s.

**R3-Q35 — B.**

- **A.** The harmonic mean of 12 and 6 (2 × 12 × 6 ÷ 18 = 8), which ignores the rest hour.
- **B.** Correct. Total distance 24 km; total time 1 h + 1 h rest + 2 h = 4 h; 24 ÷ 4 = 6 km/h.
- **C.** The arithmetic mean of 12 and 6, which is wrong when the legs are equal in distance but not in time.
- **D.** The outbound speed alone.

Trap: Leaving the rest out of the time, or taking the plain mean of the outbound and return speeds.

Shortcut: Total distance ÷ total time including rest.

Time target: 90 s.

**R3-Q36 — A.**

- **A.** Correct. Relative speed = 150 ÷ 10 = 15 m/s = 54 km/h; train speed = 54 + 6 = 60 km/h.
- **B.** Subtracts the man's speed from the relative speed (54 − 6), giving the wrong sign.
- **C.** Gives the relative speed only, forgetting that the man is moving too.
- **D.** Adds the man's speed twice (54 + 6 + 6).

Trap: Treating the relative speed as the train's speed when the observer is moving.

Shortcut: Same direction: relative = train − man, so train = relative + man.

Time target: 105 s.

**R3-Q37 — B.**

- **A.** Assumes both workers work at A's rate, so the combined rate is 2 × 1/20 = 1/10 per day.
- **B.** Correct. A's rate = 1.5/30 = 1/20 per day; B's rate = 1/30; combined 1/20 + 1/30 = 1/12; 12 days.
- **C.** 15 days: halves B's time, which is what equal efficiency would give.
- **D.** 18 days: inverts the factor (A's rate = 1/30 ÷ 1.5 = 1/45), so the combined rate is 1/45 + 1/30 = 1/18.

Trap: Multiplying the ratio on the time instead of on the rate.

Shortcut: Faster by 1.5 means rate × 1.5, so time ÷ 1.5.

Time target: 90 s.

**R3-Q38 — C.**

- **A.** Uses 35 days (a multiple of seven), which is not a common departure day for these schedules.
- **B.** Uses 37 days, one more than the LCM.
- **C.** Correct. LCM(9, 12) = 36 days; 36 ≡ 1 (mod 7); Sunday + 1 = Monday.
- **D.** Uses 38 days, two more than the LCM.

Trap: Using a multiple of seven as the LCM, or miscounting the weekday shift.

Shortcut: LCM of the cycles; weekday shift = LCM mod 7.

Time target: 90 s.

**R3-Q39 — D.**

- **A.** Divides by 100,000 instead of 10,000 in the conversion, giving a value ten times too small.
- **B.** Divides 1500 m² by 1000 instead of 10,000, a conversion slip.
- **C.** Multiplies by 100 instead of dividing (1500 × 100 = 150,000 m² = 15 ha).
- **D.** Correct. Area = (60 + 40) × 30 ÷ 2 = 1500 m²; 1500 ÷ 10,000 = 0.15 ha.

Trap: Converting square metres to hectares with the wrong factor.

Shortcut: Trapezium area first; then divide by 10,000.

Time target: 105 s.

**R3-Q40 — D.**

- **A.** Uses the floor area in square metres (12 × 8 = 96) as the tile count, one tile per square metre.
- **B.** Converts only one dimension to centimetres, so the count is 24 × 8 = 192 tiles.
- **C.** Counts every tile twice (both diagonal orientations), which is not a valid tile count.
- **D.** Correct. 1200 cm ÷ 50 = 24; 800 cm ÷ 50 = 16; 24 × 16 = 384 tiles.

Trap: Mixing metres and centimetres in the side quotients.

Shortcut: Convert to one unit; then the two side quotients multiply.

Time target: 75 s.

**R3-Q41 — B.**

- **A.** 6 km/h: applies the stream to the wrong legs (downstream 4 km/h, upstream 8 km/h), giving 6 + 3 = 9 hours.
- **B.** Correct. b = 10: upstream 8 km/h gives 3 h; downstream 12 km/h gives 2 h; total 5 h.
- **C.** 8 km/h: this is the upstream speed for b = 10, read as the still-water speed; the total time would be 3 + 2 = 5 only with b = 10.
- **D.** 12 km/h: upstream 10 km/h and downstream 14 km/h give 2.4 h + 1.71 h ≈ 4.1 h, not 5 h.

Trap: Using the stream speed as the boat's speed, or treating each leg's time as the total time.

Shortcut: Solve 24/(b−2) + 24/(b+2) = 5 by testing the candidate speeds.

Time target: 150 s.

**R3-Q42 — C.**

- **A.** Ignores the drift of the hour hand: 210° − 180° = 30°, which is the angle at 7:00 with the minute hand moved.
- **B.** Reads the minute hand as 25 minutes (150°), giving 225 − 150 = 75°.
- **C.** Correct. Hour hand 7 × 30 + 30 × 0.5 = 225°; minute hand 180°; difference 45°.
- **D.** Uses the minute hand at 90° (a quarter-hour position), giving 225 − 90 = 135°.

Trap: Forgetting the half-degree-per-minute movement of the hour hand.

Shortcut: |30H + 0.5M − 6M|.

Time target: 75 s.

**R3-Q43 — C.**

- **A.** Counts only the cubes with exactly one painted face (24).
- **B.** Counts the faces of the 24 edge cubes (2 each), a partial count.
- **C.** Correct. Each of the six large faces has 16 unit squares, all painted: 6 × 16 = 96 painted unit faces.
- **D.** Counts the 64 unit cubes, not the painted faces.

Trap: Counting cubes instead of painted faces.

Shortcut: Painted faces = 6 × n² for an n × n × n cube.

Time target: 60 s.

**R3-Q44 — D.**

- **A.** Uses 20 minutes instead of 10 minutes (18 × 1/3 = 6 km).
- **B.** Uses the faster train's distance alone (54 × 10/60 = 9 km), ignoring the slower train.
- **C.** Adds the two speeds (90 km/h × 10/60 = 15 km), which is the approaching-trains rule.
- **D.** Correct. Relative speed 54 − 36 = 18 km/h; 18 × 10/60 = 3 km.

Trap: Adding speeds for trains moving in the same direction.

Shortcut: Same direction: separation = (difference of speeds) × time.

Time target: 75 s.

**R3-Q45 — A.**

- **A.** Correct. Running time 240 ÷ 80 = 3 h; add the 15-minute halt: 3 h 15 min.
- **B.** Ignores the halt: 240 ÷ 80 = 3 h.
- **C.** Subtracts the halt from the running time instead of adding it (3 h − 15 min).
- **D.** Doubles the halt before adding it (3 h + 30 min).

Trap: Subtracting a stop from the journey time instead of adding it.

Shortcut: Total time = running time + halts.

Time target: 60 s.

**R3-Q46 — C.**

- **A.** Ignores the outlet entirely, giving the inlet's own time of 10 hours.
- **B.** Uses the outlet's emptying time as a filling time, which swaps the two rates.
- **C.** Correct. Net rate 1/10 − 1/8 = −1/40 per hour: the outlet removes water faster than the inlet adds it, so the cistern never fills.
- **D.** Treats the outlet as a second inlet: 1/10 + 1/8 = 9/40 per hour, giving 40/9 hours.

Trap: Treating an outlet as an inlet, or ignoring it.

Shortcut: Net rate ≤ 0 means the container never fills.

Time target: 75 s.

**R3-Q47 — C.**

- **A.** Holds the hour hand at 90° (3 o'clock) and ignores its drift of 20°, so |90 − 240| = 150°.
- **B.** The reflex angle (360 − 130 = 230°), which is the larger angle.
- **C.** Correct. H = 3: hour hand 90 + 20 = 110°; minute hand 240°; difference 130°, which is less than 180°.
- **D.** Reads the hour as 1 (30 + 20 = 50°), giving |50 − 240| = 190°, and then 360 − 190 = 170°.

Trap: Keeping the 24-hour hour, or forgetting the hour hand's drift.

Shortcut: H = 15 mod 12 = 3; hour angle 30H + 0.5M.

Time target: 75 s.

**R3-Q48 — C.**

- **A.** Halves the round trip twice, which uses 2.5 s of travel.
- **B.** Uses the echo time 2 s instead of 5 s (340 × 2 ÷ 1 = 680 m, mixing the round-trip factor).
- **C.** Correct. The round trip 2d covers 340 × 5 = 1700 m, so d = 850 m.
- **D.** Forgets to halve the round trip, so it reports the whole path.

Trap: Using the one-way distance as the full sound path in the echo time.

Shortcut: Echo: total path = 2 × distance.

Time target: 75 s.

**R3-Q49 — C.**

- **A.** Stops at the net 1 m per day count (12 − 2 = 10 days), forgetting that the climb on day 11 is the escape.
- **B.** Ends the count at the day on which the snail is at 10 m (the start of day 11), not at the top.
- **C.** Correct. At the start of day k the snail is at k − 1 m; on day 11 it starts at 10 m and climbs to 12 m.
- **D.** Counts one day per metre of wall, ignoring the net gain of 1 m per full day.

Trap: Stopping the count at the net gain rather than the escape day.

Shortcut: Start of day k = k − 1 m; escape when k − 1 + 2 ≥ 12.

Time target: 90 s.

**R3-Q50 — B.**

- **A.** The height after the first rebound (90 × 2/3 = 60 m).
- **B.** Correct. 90 × (2/3)² = 90 × 4/9 = 40 m.
- **C.** Uses the ratio 1/3 instead of 2/3 (90 × (1/3)² = 10 m, and 90 × 1/3 = 30 m for the first rebound), a ratio error.
- **D.** Uses a ratio of one half (90 × (1/2)² = 22.5 m) or halves the height at each step, giving 45 m after one step.

Trap: Confusing the rebound ratio with its complement.

Shortcut: Height after n rebounds: h × r^n with r = 2/3.

Time target: 60 s.

**R3-Q51 — A.**

- **A.** Correct. Total triples C(8,3) = 56 minus the collinear triples C(7,3) = 35 gives 21 triangles.
- **B.** Counts pairs of points, C(8,2) = 28, which are segments, not triangles.
- **C.** Counts only the collinear triples C(7,3) = 35, which are excluded from the count of triangles.
- **D.** Counts every triple of the eight points, including the collinear ones.

Trap: Forgetting that collinear triples are not triangles.

Shortcut: Triangles = C(n,3) minus collinear triples.

Time target: 90 s.

**R3-Q52 — C.**

- **A.** Counts only one layer of the interior columns, (n − 2)² = 4.
- **B.** Counts only two of the four interior columns (2 × 4 = 8), omitting the other two.
- **C.** Correct. The interior columns (not on any side face) are 2 × 2 = 4 per layer; with 4 layers the unpainted cubes are 4 × 4 = 16.
- **D.** Counts the cubes not on the top or bottom faces (64 − 32), which ignores the side-face paint.

Trap: Treating the top and bottom faces as painted when only the sides are.

Shortcut: Unpainted = (n−2)² × n when only the four lateral faces are painted.

Time target: 90 s.

**R3-Q53 — A.**

- **A.** Correct. Monday 22:30 to Thursday 22:30 is 72 h; Thursday 22:30 to 11:00 is 11 h 30 min earlier; 72 − 11.5 = 60.5 h.
- **B.** Treats the arrival as 10:00 on Thursday, which shortens the journey by an hour.
- **C.** Treats the arrival as 12:00 on Thursday, which lengthens the journey by an hour.
- **D.** Counts the three days and adds 30 minutes (72 + 0.5 = 72.5 h), ignoring the arrival time.

Trap: Subtracting clock times across midnight without counting the full days.

Shortcut: Days × 24 + (arrival − departure clock difference).

Time target: 75 s.

**R3-Q54 — C.**

- **A.** Concludes that the circle does not reach the square's boundary, but the radius equals the half-side, so it reaches the sides.
- **B.** Counts only one pair of opposite sides, omitting the other two.
- **C.** Correct. The radius equals the half-side 3, so the circle touches each side at its midpoint: one point per side, 4 in total.
- **D.** Counts two points per side, which requires the radius to exceed the half-side.

Trap: Counting tangency as two intersection points.

Shortcut: Radius = half-side: tangent at four midpoints.

Time target: 75 s.
