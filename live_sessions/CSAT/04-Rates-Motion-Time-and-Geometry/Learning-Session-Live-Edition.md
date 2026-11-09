# Rates, Motion, Time and Geometry - Learning Session Live Edition

**Paper:** CSAT (Civil Services Preliminary Examination, Paper II) | **Format:** four-option objective items only; there is no Mains component in this paper | **Practice in this session:** multiple choice, answered in a separate block after each item

This session teaches the arithmetic of rate, motion, time and geometry that the paper uses. Almost every item in this family asks you to turn a story into one equation: a rate multiplied by a time, a speed relative to another speed, a fixed formula for a clock or a calendar, or a length, area or count for a shape. You will learn to name the quantity that stays fixed, to notice when a shortcut has stopped being valid, and to check the answer by a second route before you choose an option.

Work through the lessons in order. Each one builds on the previous one, and each ends with a short set of original items that test the method and the common failure, not the memory of a term. Attempt each item before you open its explanation.

Your personal target is a learning goal, not an official cut-off. The timed-set section explains how to use it.

## Roadmap

| # | Lesson | Stage | Depends on | Practice items |
|---:|---|---|---|---:|
| 1 | Rate model: combined work, pipes, cycles, bounces, rest rules and proportion | Foundation | Basic fractions | 4 |
| 2 | Speed, average speed, displacement, compass directions, trains, boats and schedules | Foundation to Core | Lesson 1 | 3 |
| 3 | Relative motion: lines, circular tracks, races, passings and sound | Core | Lesson 2 | 4 |
| 4 | Clocks and calendars | Core | Lesson 1 (cycles) | 4 |
| 5 | Geometry: Pythagoras, angles, circles, coordinates, ratios on a line and right-triangle ratios | Core and Class X trigonometry | Basic arithmetic of squares and roots | 4 |
| 6 | Plane and solid mensuration: areas, circles, solids and probability by area | Core | Lesson 5 | 4 |
| 7 | Cube counts, tiling, cuts and units | Core | Lessons 1 and 6 | 4 |

After the seven lessons come cumulative items 28 to 39, each of which joins methods from two lessons, followed by the timed-set routine, remediation, the master method maps, the consolidated register notes, the coverage matrix and the source ledger.

---

## Lesson 1 - Rate model: combined work, pipes, cycles and net climbs

Progress: Lesson 1 of 7 | Stage: Foundation | Subtopic: Rate model: combined work, pipes, cycles and net climbs

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: one equation behind work, pipes and climbs

```text
                 RATE x TIME = AMOUNT
                         |
        +----------------+----------------+
        |                |                |
      WORK             PIPES            CLIMBS
  rate = 1/days    fillers +1/time    climb by day,
  workers ADD      drains  -1/time    slide by night
  if simultaneous  net <= 0 -> the    net per day-night
  time = 1/sum     tank never fills   final day: no slide
```

Read the diagram from the top. Every item in this lesson gives you an amount, a rate for each agent, and a question about time. The only real decisions are the sign of each rate and whether the agents work at the same moment.

### Plain intuition

Think of a job as a full bar of one unit. A worker who would finish the job alone in 8 days fills one-eighth of the bar each day. That fraction is the worker's rate. If two workers are at the same job on the same day, their daily fractions add, because both pour into one bar. The time is never added to time. Adding 8 days to 24 days would say the pair is slower than either worker, which is absurd.

A pipe is the same idea with a sign. A filling pipe adds to the tank, a draining pipe removes from it. The net rate decides everything. If the outflow matches or beats the inflow, the tank never fills, however long you wait.

### Doctrine: the three definitions

- **Rate.** If an agent does the whole job in T time, its rate is 1/T of the job per unit time.
- **Amount.** Rate multiplied by time gives the amount done. This single equation covers work, filling and climbing.
- **Combined rate.** For agents working at the same time, the combined rate is the sum of their signed rates. The time is the reciprocal of that sum, provided the sum is positive.

### Shortcut 1: combined work

- **Rule.** Two simultaneous workers finish in time 1/(1/T1 + 1/T2).
- **Failure condition.** The rule fails when the workers are not on the job together, or when they block each other. A shared tool, a room that holds only one person, or a worker who leaves halfway each change the answer.
- **Worked example.** A finishes alone in 8 days and B alone in 24 days. Together they do 1/8 + 1/24 = 4/24 = 1/6 of the job each day, so the job takes 6 days.

### Shortcut 2: pipes, fillers and drains

- **Rule.** Write each filler as +1/time and each drain as -1/time, add the signed rates, then invert the sum.
- **Failure condition.** If the net rate is zero or negative, the tank never fills. Inverting a negative number is the most common slip in this family.
- **Worked example.** A pipe fills a tank in 6 hours and a drain empties it in 12 hours. The net rate is 1/6 - 1/12 = 1/12 of the tank per hour, so the tank fills in 12 hours. If the drain instead empties it in 4 hours, the net rate is 1/6 - 1/4 = -1/12. The tank never fills.

**Basic worked checks (Examples A and B).** Combined work: A finishes in 12 days and B in 18 days, so together they do 1/12 + 1/18 = 5/36 of the job a day and finish in 36/5 = 7.2 days. Pipes: a pipe that fills a tank in 6 hours and another in 8 hours give 1/6 + 1/8 = 7/24 of the tank an hour, so they fill it in 24/7, about 3.43 hours. A fill of 4 hours with a drain of 6 hours gives 1/4 - 1/6 = 1/12, so the tank fills in 12 hours. Failure condition: the times are never added; the rates are.

### Shortcut 3: alternate days and cycles (Advanced Methods 1 and 4)

- **Rule.** When the workers take turns, add the rates of one full cycle, count the complete cycles, and finish the remainder one day at a time. The worker whose turn falls on the remainder day decides how long the remainder takes.
- **Failure condition.** Dividing the total job by the cycle rate and stopping there ignores the partial day. Also, changing who starts changes the total whenever the remainder falls on a turn of one of them.
- **Worked example.** A finishes alone in 6 days and B alone in 9 days, and they alternate, A first. One cycle of two days does 1/6 + 1/9 = 5/18. Three cycles, six days, give 15/18 = 5/6. On day 7 A works and adds 1/6, which finishes the job exactly at the end of day 7. If B had started, day 7 would add only 1/9, leaving 1/18. Day 8 is A's turn, and A needs one-third of that day to finish, so the total is 7 1/3 days.

- **Escalation (Advanced).** When a cycle repeats, the answer is decided by the remainder. A alone in 12 days and B alone in 18 days take 5/36 per two-day cycle, so seven cycles do 35/36 in 14 days either way. The last 1/36 is done by whoever works on day 15: if A starts, A works day 15 at 1/12 per day and the job takes 14 1/3 days; if B starts, B works day 15 at 1/18 per day and the job takes 14 1/2 days. Never divide the total by the cycle rate and stop.

### Shortcut 4: a climb with slips and the final step

- **Rule.** Let the climb by day be c, the slide by night be s, and the height be H. After n - 1 full day-night cycles the position is (n - 1)(c - s). On day n the climber climbs c and does not slide again if the top has been reached. So the top is reached on the first day n with (n - 1)(c - s) + c >= H.
- **Failure condition.** Dividing H by the net climb c - s and rounding up is wrong because the final climb is not followed by a slide. The rule also fails when c <= s, since the climber never gains height.
- **Worked example.** A climber gains 6 cm by day and slides 2 cm by night, aiming for a height of 18 cm. Dividing gives 18/4 = 4.5, which rounds up to 5 days. The correct count: after three nights the climber is at 12 cm; on day 4 the climb of 6 cm reaches 18 cm, so the answer is 4 days.

### Shortcut 5: consumption rate and a changing group

- **Rule.** A store is people times days. When the group size changes, first find how much is left at the change, then divide the remainder by the new daily consumption.
- **Failure condition.** Scaling the remaining days by the old ratio of people to food is wrong. The remaining amount is fixed; only the rate changes.
- **Worked example.** A garrison holds food for 1,000 soldiers for 30 days, which is 30,000 soldier-days. After 10 days 10,000 soldier-days have been used and 20,000 remain. When 1,000 more soldiers join, the group eats 2,000 per day, so the food lasts 20,000 / 2,000 = 10 more days.

**Run rate and overs.** The same product rule covers run rate. Runs scored equal the run rate times the overs, so 120 runs in 20 overs is a run rate of 6. Scoring the same 120 runs at 8 runs an over takes 120/8 = 15 overs. A higher rate and fewer overs are two sides of one product, and the total is the quantity that stays fixed.

### Shortcut 6: geometric decay and a bounce count

- **Rule.** When each bounce reaches a fixed fraction r of the previous height, the rebound heights form a geometric sequence: h, hr, hr squared, and so on. Count landings, not rebounds. The first drop is a landing, and each rebound that actually happens ends in another landing. A rebound that would fall below the stated threshold does not happen.
- **Failure condition.** Counting only the rebounds drops the first landing. Stopping at the first height below half the drop is a different rule from the one stated. Counting the rebound that falls below the threshold adds a bounce the ball never makes.
- **Worked example.** A ball is dropped from 2 m, and each bounce reaches three-quarters of the height it fell from. It stops bouncing once a rebound would be below 0.5 m. The rebounds are 1.5 m, 1.125 m, 0.84375 m and 0.6328125 m. The next rebound would be 0.474609375 m, which is below 0.5 m, so it does not happen. The landings are the drop plus the four rebounds: 5 landings. The rule is therefore: landings = 1 + number of rebounds at or above the threshold.

### Shortcut 7: an hour-by-hour rest rule

- **Rule.** Work through the hours one at a time. In each hour exactly one named worker works, and no worker may work in two consecutive hours. Track the fraction done after each hour. In the final hour, the worker on duty needs only the fraction still missing, so that hour takes (missing fraction) divided by that worker's hourly rate. The finishing time is the full hours before it plus that fraction of an hour.
- **Failure condition.** Adding all the hourly rates into one hour ignores that only one person works in each hour. Rounding the last partial hour up to a whole hour overstates the time. A schedule that gives one worker two consecutive hours breaks the stated rest.
- **Worked example.** A needs 4 hours alone, and B and C each need 6 hours alone. Take the schedule A, B, A, B, A. After four hours the work done is 1/4 + 1/6 + 1/4 + 1/6 = 5/6. The fifth hour belongs to A, who does 1/4 per hour. The missing 1/6 takes (1/6) divided by (1/4) = 2/3 of an hour. The job ends at 4 hours plus 2/3 of an hour, which is 4 hours 40 minutes. A search over every schedule that keeps the rest rule confirms that no schedule finishes earlier.

### Shortcut 8: proportion of men and days, and a change in daily use

- **Rule.** For the same work at the same rate per person, men multiplied by days is constant. Doubling the men halves the days. When a stock is used at a daily rate that rises by a percentage p, the number of days the stock lasts is divided by (1 + p) in decimal form.
- **Failure condition.** The product rule needs the same rate of work per person. A percentage increase in use reduces the days by a factor, not by the same percentage: raising the daily use by 20 per cent does not cut the days by 20 per cent.
- **Worked example.** Twelve men finish a job in 10 days, so the work is 120 man-days, and 6 men need 120 divided by 6 = 20 days. A tank of petrol lasts 12 days. If the daily use rises by 20 per cent, the tank lasts 12 divided by 1.2 = 10 days. The wrong answer 12 times 0.8 = 9.6 days applies the percentage to the days instead of to the use.


### The strongest wrong method and the reply

The tempting wrong method for joint work is to average the two times. With times of 8 and 24 days, the average is 16 days, which seems to suggest that the pair takes longer than the fast worker alone. The reply is direct. Together they do more each day than the faster worker does alone, so the pair must finish sooner than 8 days. The average of two times is not the time for joint work, because time is not additive across agents working in parallel.

A second wrong method treats every worker as independent when the stem says they interfere. The reply is to read the stem for blocking words such as one at a time, or a shared channel, before adding any rates.

A third wrong method, for a rest rule, adds all the hourly rates and reads the answer as one hour. The reply is that the rule limits each hour to one worker, so the rates can only be used in turn.

### UPSC application

Items in this family usually combine one of three moves: two workers on one job, a filler and a drain on one tank, or a pattern of turns that repeats. Name the rate of each agent with its sign, decide whether the agents work simultaneously, and check the net rate before inverting. For cycles, always check the day on which the job ends. For climbs, decide whether the top is reached on a climbing day or after a slide, because that is where the final-step rule matters.

### Revision points

- Rate is the fraction of a job done per unit time; a job of one unit done in T time has rate 1/T.
- Rates add when the agents work simultaneously. Times never add or average.
- A filler is positive and a drain is negative; invert only the net rate.
- A net rate of zero or less means the tank never fills.
- Alternate-day work is decided by complete cycles plus a remainder that depends on whose turn it is.
- Changing who starts changes the total when the remainder falls on a turn.
- A climb is decided by the first day on which the climb alone reaches the top.
- A consumption problem keeps the remaining amount fixed and changes only the daily use.
- Run rate times overs gives runs; a higher rate for fewer overs keeps the total fixed.
- Check the interference condition before adding any two rates.
- A bounce count is the drop plus each rebound at or above the threshold; the rebound below it does not happen.
- An hour-by-hour rest rule allows one worker an hour and no worker twice running; the last hour takes the missing fraction.
- Men times days is constant for the same work; a rise of p in daily use divides the days by 1 + p.

Working on the job is the first step in this family. The next question is how a body moves through space, which needs a different quantity: speed is distance per unit time, not amount per unit time. The same rate-times-time equation carries over, but the amount is now a length, and the distance a body covers does not always equal how far it finishes from where it started.

### Retrieval before the practice

1. A tank has two pipes: one fills it in 10 hours and one empties it in 15 hours. Both are open. How long does the tank take to fill?
   *Answer: the net rate is 1/10 - 1/15 = 1/30 of the tank per hour, so it takes 30 hours.*
2. Why must the day of the remainder be identified in an alternate-day problem?
   *Answer: the remainder is done at the rate of whichever worker's turn falls on that day, and that rate differs between the workers.*
3. A climber gains 5 cm by day, slides 4 cm by night and needs to reach 9 cm. How many days?
   *Answer: after one night the climber is at 1 cm; on day 2 the climb of 5 cm reaches 6 cm, not 9. Recheck: (n - 1)(5 - 4) + 5 >= 9 gives n - 1 >= 4, so n = 5 days.*

### Practice

**MCQ 1**

A pipe P fills an empty tank in 12 minutes, a pipe Q fills it in 20 minutes, and a drain R empties a full tank in 15 minutes. All three are opened together on an empty tank. How long does the tank take to fill?

- A. 15 minutes
- B. 7 1/2 minutes
- C. 16 minutes
- D. 5 minutes

**MCQ 1 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The signed net rate is 1/12 + 1/20 - 1/15 = 5/60 + 3/60 - 4/60 = 4/60 = 1/15 of the tank per minute, so the tank fills in 15 minutes.
- **B — Incorrect:** Leaves out the drain. The two fillers alone give 1/12 + 1/20 = 2/15 of the tank per minute, which fills it in 7 and a half minutes. The drain must reduce the net rate.
- **C — Incorrect:** Averages the two filling times, (12 + 20)/2 = 16. Filling times are not combined by averaging; the rates add.
- **D — Incorrect:** Treats the drain as a third filler and adds its rate: 1/12 + 1/20 + 1/15 = 1/5 of the tank per minute, which gives 5 minutes. A drain subtracts from the net rate.

**MCQ 2**

Worker X alone finishes a job in 8 days and worker Y alone in 12 days. They work on alternate days, with X on day 1, Y on day 2, X on day 3, and so on. A worker who works on a day does that day's full share until the job ends. How long does the job take?

- A. 9 days
- B. 9 1/2 days
- C. 9 2/3 days
- D. 10 days

**MCQ 2 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Counts only the whole days. Four full cycles of two days do 4 times (1/8 + 1/12) = 5/6 of the job in 8 days; the job is not finished at the end of day 9, when 1/24 remains.
- **B — Correct:** Four cycles do 5/6 in 8 days. On day 9, X does 1/8 and the job has 1/24 left. On day 10, Y does 1/12 per day, so the last 1/24 takes half of day 10. The job ends 9 and a half days after the start.
- **C — Incorrect:** Starts the alternation with Y and gets the remainder on the wrong day. With Y first, day 9 is Y's and leaves 1/12, which day 10 (X's) finishes after two-thirds of a day. The stem gives X the first day.
- **D — Incorrect:** Counts day 10 as a whole day, so the job seems to end at the end of that day. Only half of day 10 is needed, because 1/24 remains and Y does 1/12 of the job per day.

**MCQ 3**

A ball is dropped from a height of 2.7 m. Each time it rebounds, it reaches two-thirds of the height it fell from. What is its height after it has rebounded three times?

- A. 1.8 m
- B. 1.2 m
- C. 0.8 m
- D. 0.6 m

**MCQ 3 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Stops after one rebound: 2.7 times 2/3 = 1.8 m. The question asks for the height after three rebounds.
- **B — Incorrect:** Stops after two rebounds: 2.7 times 4/9 = 1.2 m, so the third rebound has been left out.
- **C — Correct:** Three rebounds multiply the height by 2/3 each time: 2.7 times 8/27 = 0.8 m.
- **D — Incorrect:** Multiplies by 2/9 once instead of by 2/3 three times; 2.7 times 2/9 = 0.6 m.

**MCQ 4**

Worker P alone finishes a job in 3 hours and worker Q alone in 5 hours. Only one of them works in each hour, and neither works in two consecutive hours. They alternate from the first hour, with P first. How long does the job take?

- A. 3 hours
- B. 4 hours
- C. 3 2/5 hours
- D. 3 2/3 hours

**MCQ 4 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Gives P's time alone. P cannot work every hour, and Q's share is still missing at the end of hour 3.
- **B — Incorrect:** Rounds the finish up to the end of hour 4. The job ends during hour 4, after 2/3 of that hour.
- **C — Incorrect:** Uses P's rate of 1/3 per hour for Q's last hour: 2/15 divided by 1/3 is 2/5 of an hour, which is the wrong worker's rate.
- **D — Correct:** P does 1/3 in hour 1, Q does 1/5 in hour 2 and P does 1/3 in hour 3, so 13/15 is done. The last 2/15 is Q's, at 1/5 per hour, which takes 2/3 of hour 4. The job ends at 3 2/3 hours.

---

## Lesson 2 - Speed, average speed, displacement, trains, boats and schedules

Progress: Lesson 2 of 7 | Stage: Foundation to Core | Subtopic: Speed, average speed, displacement, trains, boats and schedules

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: two quantities that look alike but are not

```text
                   A MOVING BODY
                        |
      +-----------------+------------------+
      |                                    |
   PATH TRAVELLED                    NET CHANGE OF POSITION
   distance: add every leg           displacement: add with signs
   always >= 0, never falls          zero after a round trip
      |                                    |
   speed = distance / time           velocity = displacement / time
   (every "average speed" item)      (net position, bearing)
```

The left branch answers "how much ground has been covered". The right branch answers "where is the body now, compared with where it started". Most mistakes in this lesson come from answering the other branch's question.

### Plain intuition

Speed is simply how much path you cover in one hour. An average speed is the speed you would need, held steady for the whole trip, to cover the same path in the same total time. It is therefore a ratio of two totals: the total path and the total time. It is not the average of the speeds you used, because each speed lasted a different length of time, or covered a different length of path.

Consider a walk that is partly quick and partly slow. If you spend much longer on the slow stretch, the trip's average speed sits close to the slow speed. Time, not the list of speeds, controls the average.

### Doctrine: the working definitions

- **Speed** is distance divided by time: a magnitude, always zero or positive.
- **Average speed** is total distance divided by total time.
- **Displacement** is the straight change of position from start to finish, with its direction. A body that returns to its start has zero displacement.
- **Average velocity** is displacement divided by total time. It can be zero while the average speed is positive.

### Shortcut 1: average speed as total over total

- **Rule.** Add all the distances and divide by the sum of all the times. Use this whenever the stem gives different distances for each leg.
- **Failure condition.** Averaging the leg speeds directly is wrong unless each leg took the same time. A plain mean of speeds is correct only for equal times.
- **Worked example.** A cyclist covers 20 km at 40 km/h and then 60 km at 30 km/h. The times are 0.5 h and 2 h, so the total is 80 km in 2.5 h. The average speed is 32 km/h. The plain mean of 40 and 30 is 35, which is wrong because the second leg lasted much longer.

### Shortcut 2: harmonic mean only for equal distances (Advanced time-saving form)

- **Rule.** When two legs cover the same distance d at speeds a and b, the average speed is the harmonic mean 2ab/(a + b). Both legs have the same length, so the total time is d/a + d/b and the total distance is 2d.
- **Failure condition.** The formula fails as soon as the distances differ, or when there are three or more legs with unequal lengths. Return to total over total.
- **Worked example.** A journey of 40 km at 40 km/h and a return of 40 km at 80 km/h gives 2(40)(80)/(40 + 80) = 6400/120 = 53 1/3 km/h. Check: the total is 80 km in 1 + 1/2 = 1.5 h, which is 53 1/3 km/h.

### Shortcut 3: segment order and the rearrangement rule (Advanced)

- **Rule.** With a fixed set of distances and a fixed set of speeds, the total time is smallest when the longest distance is travelled at the fastest speed. Pairing the largest distance with the largest speed is the sorted pairing, and it gives the minimum total time.
- **Failure condition.** The rule compares the sorted pairing with any other pairing. It does not rank two arbitrary pairings against each other; for that, compute both totals.
- **Worked example.** A traveller covers 1 km at 2 km/h and then 3 km at 6 km/h, taking 1/2 + 1/2 = 1 hour. A second traveller covers the same distances at the same speeds in the reverse pairing, 1 km at 6 km/h and 3 km at 2 km/h, taking 1/6 + 3/2 = 5/3 hours. The first pairing is the sorted one, and it is faster.

### Shortcut 4: distance and displacement

- **Rule.** Distance is the sum of all the leg lengths. Displacement is the sum of the same legs with opposite directions given opposite signs.
- **Failure condition.** When the body never reverses, distance and displacement are equal. When it reverses, they differ, and the stem decides which one is asked.
- **Worked example.** A toy jumps 4 cm forward and 3 cm back at each jump, making 10 jumps in all, and finishes 12 cm ahead of its start. If f jumps are forward, 4f - 3(10 - f) = 12 gives 7f = 42, so f = 6 forward and 4 back. The path travelled is 6 x 4 + 4 x 3 = 36 cm; the displacement is 12 cm.

**Basic and Advanced cyclist checks (Example F; drill item 6).** A cyclist rides 12 km east in 30 minutes and 12 km back west in 20 minutes. The distance is 24 km and the displacement is 0, so the average velocity is 0. The average speed is 24 divided by 5/6 = 28.8 km/h; the plain mean of 24 and 36 km/h, which is 30, is wrong. A cyclist who rides 15 km uphill at 10 km/h and returns at 30 km/h spends 1.5 + 0.5 = 2 hours on 30 km, so the average speed is 15 km/h, and the average velocity is again 0.

### Shortcut 5: trains and the length that must be covered

- **Rule.** Start from the total length that must pass the reference point. A train passing a pole covers its own length. A train crossing a platform or bridge covers the train's length plus the platform's length. Divide by the relevant speed, converted to metres per second when the lengths are in metres.
- **Failure condition.** Using only the train's length when the platform is involved, or using the sum of speeds for a train overtaking another in the same direction.
- **Worked example.** A 100 m train travels at 90 km/h, which is 25 m/s. It passes a pole in 100/25 = 4 s and crosses a 150 m platform in 250/25 = 10 s. Two trains moving towards each other, of lengths 150 m and 100 m at speeds 72 km/h and 36 km/h, need 250 m to pass completely and close at 108 km/h, which is 30 m/s. They pass in 250/30 = 25/3 s.

- **Overtaking example (Advanced).** A 200 m train at 90 km/h, which is 25 m/s, overtakes a man running at 5 m/s in the same direction. The relative speed is 25 - 5 = 20 m/s, so the train takes 200/20 = 10 seconds to pass him. The man is a moving object, so his speed is subtracted, not added.

**Basic and Advanced train checks (Example C; drill item 2).** A 120 m train at 72 km/h, which is 20 m/s, crosses a pole in 120/20 = 6 seconds and crosses a 180 m platform in 300/20 = 15 seconds. Two trains of 120 m at 54 km/h and 180 m at 36 km/h that move towards each other on parallel tracks add their speeds, 90 km/h = 25 m/s, and cover both lengths: (120 + 180)/25 = 12 seconds. Subtracting the speeds would be a fivefold error.

### Shortcut 6: boats and streams

- **Rule.** Downstream speed is still-water speed b plus stream speed s. Upstream speed is b minus s. Time equals distance divided by the speed in that direction.
- **Failure condition.** Upstream progress needs b greater than s. If b is equal to or less than s, the boat makes no forward progress upstream.
- **Worked example.** A boat with still-water speed 9 km/h in a stream of 3 km/h covers 36 km downstream at 12 km/h, which takes 3 hours, and 36 km upstream at 6 km/h, which takes 6 hours. The round trip is 9 hours.

**Advanced boat check (drill item 1).** A boat with still-water speed 10 km/h in a 2 km/h stream covers 48 km downstream at 12 km/h, which takes 4 hours, and 48 km upstream at 8 km/h, which takes 6 hours. The round trip takes 10 hours. **Basic boat check (Example C.1).** The same boat has speeds of 12 km/h downstream and 8 km/h upstream; reversing the signs is the standard trap.

### Shortcut 7: timetables and schedules

- **Rule.** The number of vehicles needed to keep one service running at a fixed interval is the round-trip time, including the layover, divided by the interval between departures, rounded up.
- **Failure condition.** Rounding down or leaving out the layover gives too few vehicles.
- **Worked example.** A train's round trip, including turnaround, takes 60 hours, and a departure leaves each end every 24 hours. 60/24 = 2.5, so three trains are needed.

### Shortcut 8: reading a velocity-time graph

- **Rule.** The area under a velocity-time graph is the distance travelled. Average speed is that area divided by the total time.
- **Failure condition.** Reading the height of the graph as the distance is wrong; the height is a speed, and only the area is a distance.
- **Worked example.** A body speeds up uniformly from 0 to 20 m/s in 10 s, then holds 20 m/s for 5 s. The distance is 1/2 x 10 x 20 + 20 x 5 = 200 m over 15 s, an average speed of 40/3 m/s.

### Shortcut 9: solving for an unknown speed

- **Rule.** Let the unknown speed be v. Write each leg's time as its distance divided by its speed in terms of v, add the times to the stated total (or set the difference of the two times to the stated difference), clear the denominators and solve the resulting quadratic. Keep only the root that gives a positive speed.
- **Failure condition.** Writing the unknown as a time instead of a speed, or using the original speed on a leg that was run at the changed speed, gives the equation for a different journey. A negative root is never a speed.
- **Worked example.** A journey of 20 km at speed v and then 40 km at speed v + 10 takes 4 hours. So 20/v + 40/(v + 10) = 4. Multiply by v(v + 10): 20(v + 10) + 40v = 4v(v + 10), which simplifies to v squared - 5v - 50 = 0, or (v - 10)(v + 5) = 0. The root v = 10 km/h is the speed, and the check is 20/10 + 40/20 = 2 + 2 = 4 hours. The root -5 is rejected.
- **Second example, with a slowdown.** A train covers 600 km. In one run, it meets an accident after 100 km and then runs 200 km at half speed and the remaining 300 km at a quarter of its speed. In the other run, the defect comes at 100 km and the accident comes 200 km later. Both runs are split at the same points, so the first run takes 100/v + 200/(v/2) + 300/(v/4) = 1700/v hours and the second takes 100/v + 200/(v/4) + 300/(v/2) = 1500/v hours. The first run takes 200/v hours longer. If it takes 4 hours longer, then 200/v = 4, so v = 50 km/h. The equation comes from the difference, which removes the common part of the journey.

### Shortcut 10: compass direction of a net displacement

- **Rule.** Split each leg into an east-west part and a north-south part. Add the eastward parts with sign (west negative) and the northward parts with sign (south negative). The net displacement has these two components, its length is the square root of the sum of their squares, and its direction is read from the two components, not assumed.
- **Failure condition.** Reporting the direction of the last leg, or assuming 45 degrees whenever the path turns, gives the wrong bearing. A right turn or a left turn changes the sign of the component it turns against, so the heading must be tracked after each turn.
- **Worked example.** A walker goes 30 m east, turns left and goes 40 m north. The net components are 30 m east and 40 m north. The length is sqrt(30 squared + 40 squared) = 50 m. The direction is arctan(40/30), about 53 degrees north of east. It is not 45 degrees, because the components are unequal.

### The strongest wrong method and the reply

The most tempting wrong method is to average the speeds of the legs of a journey whenever the stem asks for an average. The reply is that an average speed is a rate over the whole trip, so the total path must be divided by the total time. A second wrong method takes a round trip as having average velocity equal to average speed. The reply is that a round trip has zero displacement, so its average velocity is zero even when its average speed is large.

**Advanced traps (labelled Advanced).** Averaging the segment speeds of a multi-leg journey is wrong; use total distance over total time. Reporting the distance travelled when the stem asks how far the object is from its start is wrong; that is displacement. For a boat, the still-water speed is not the downstream or upstream speed, and the stream must be added or subtracted.

### UPSC application

Read the stem's verb before you calculate. "How far did it travel" and "how far is it from the starting point" are different questions. "Average speed" needs total over total. "Time to cross" needs the full length that must pass the reference point. A boat question needs two speeds, one for each direction, and a train question needs the lengths of every object involved.

### Revision points

- Speed is path per time; displacement is net change of position.
- Average speed equals total distance divided by total time.
- The plain mean of speeds is right only when the legs take equal time.
- The harmonic mean 2ab/(a + b) is right only when the legs cover equal distances.
- The longest distance at the fastest speed gives the minimum total time for a fixed set of legs.
- A round trip has zero displacement and a positive average speed.
- A train crossing a platform covers the sum of its length and the platform's length.
- Two trains passing in opposite directions add their speeds; overtaking adds their lengths and subtracts their speeds.
- Downstream adds the stream speed; upstream subtracts it and needs still-water speed to exceed it.
- The number of vehicles on a timetable is the round-trip time divided by the departure interval, rounded up.
- The area under a velocity-time graph is the distance.
- An unknown speed comes from the equation written in v; keep the positive root.
- The direction of a net displacement comes from its two components, not from a default 45 degrees.

The idea of speed is now in place for a single body. When two bodies move at once, the question changes: each body's speed matters only in comparison with the other's. The same kind of arithmetic therefore reappears, but the speed that matters is the speed of one body measured against the other.

### Retrieval before the practice

1. A train of length 180 m passes a pole in 12 s. What is its speed in metres per second?
   *Answer: 180/12 = 15 m/s.*
2. Two equal-distance legs run at 30 km/h and 50 km/h. What is the average speed?
   *Answer: the harmonic mean 2(30)(50)/(30 + 50) = 3000/80 = 37.5 km/h.*
3. A body returns to its starting point after a 30 m walk out and back. What is its displacement?
   *Answer: zero; the distance is 60 m.*

### Practice

**MCQ 5**

A van travels 30 km at an average speed of 15 km/h and then 60 km at an average speed of 20 km/h, without stopping. What is its average speed over the whole 90 km journey, in km/h?

- A. 18
- B. 17 1/2
- C. 17 1/7
- D. 18 1/3

**MCQ 5 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The times are 30/15 = 2 hours and 60/20 = 3 hours, a total of 5 hours. Total distance 90 km divided by 5 hours is 18 km/h.
- **B — Incorrect:** Takes the plain mean of the two speeds, (15 + 20)/2 = 17 1/2. The plain mean is valid only when the legs take equal time, and here the legs take 2 and 3 hours.
- **C — Incorrect:** Applies the harmonic form, 2 times 15 times 20 divided by (15 + 20) = 17 1/7. That form is valid only for legs of equal distance, and here the legs are 30 km and 60 km.
- **D — Incorrect:** Weights each speed by its distance, (30 times 15 + 60 times 20)/90 = 18 1/3. That is not an average speed, because average speed needs time weights.

**MCQ 6**

A 120 km trip at speed v takes 2 hours longer than the same trip at speed v + 10 km/h. What is v, in km/h?

- A. 12
- B. 20
- C. 30
- D. 45

**MCQ 6 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Sets 120/v equal to the speed increase of 10 km/h, which mixes a time with a speed. The stem gives a difference between the two times of 2 hours.
- **B — Correct:** Check: 120/20 - 120/30 = 6 - 4 = 2 hours. The difference of the times for the two speeds is the stated 2 hours, and the root is positive.
- **C — Incorrect:** At 30 km/h the 120 km trip takes 4 hours and at 40 km/h it takes 3 hours, a difference of only 1 hour, not 2. The speed v + 10 is taken as the original speed, which describes a different trip from the stated one.
- **D — Incorrect:** Substitutes 45 km/h without forming the equation: 120/45 - 120/55 is about 0.48 hours, not 2 hours. A value must satisfy the stated difference.

**MCQ 7**

A walker goes 24 m due east, turns left and walks 10 m due north. In which direction, from the starting point, is the walker now?

- A. north-east, by 45 degrees
- B. north of west, by about 23 degrees
- C. north of east, by about 23 degrees
- D. south of east, by about 67 degrees

**MCQ 7 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Assumes the net displacement is at 45 degrees whenever the path turns. The components are 24 m and 10 m, which are unequal, so the bearing is not 45 degrees.
- **B — Incorrect:** Reverses the east component: the walker went east, not west. The bearing is north of east, not north of west.
- **C — Correct:** The net displacement is 24 m east and 10 m north. Its angle north of east is arctan(10/24), about 23 degrees, and it is in the north-east quadrant. A turn to the left from east points north.
- **D — Incorrect:** Swaps the components and gives the angle from the wrong axis. The 23-degree bearing is measured from the east direction, and the south answer is in the wrong quadrant.

---

## Lesson 3 - Relative motion: lines, circular tracks, races and sound

Progress: Lesson 3 of 7 | Stage: Core | Subtopic: Relative motion: lines, circular tracks, races and sound

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: watch one body from the other

```text
   TWO BODIES ON ONE LINE                   TWO BODIES ON ONE TRACK
   A ->          <- B   (opposite)          start together, same way
   gap closes at v(A) + v(B)                A ->  ring of length L
                                            gap grows and shrinks by lap
   A ->  slower   B ->  faster  (same)      faster gains one lap per
   gap closes at v(B) - v(A)                L / |vA - vB| seconds
```

Imagine you are sitting on one of the bodies. The other body's motion, as you see it, is its speed relative to you. On a single line you either add the two speeds or subtract them, depending on whether the bodies approach each other or chase each other. On a circle the same comparison tells you how often one overtakes the other.

### Plain intuition

Two runners on a straight road who approach each other close the gap at the sum of their speeds. Two runners on the same road in the same direction close the gap only at the difference of their speeds, because the faster one is also moving away from the slower one's position at its own speed. The time to meet is always the gap divided by the rate at which the gap changes, and that rate is the relative speed.

### Doctrine: the relative-speed rule

For two bodies on the same straight line:

- **Opposite directions:** the gap closes at vA + vB.
- **Same direction:** the gap changes at |vA - vB|.
- **Time to meet or to catch up:** the gap divided by that rate.

### Part A - Motion on one line

### Shortcut 1: meeting and catching up on a line (Advanced time-saving form)

- **Rule.** Use the sum for opposite directions and the difference for the same direction.
- **Failure condition.** The rule holds only when both bodies move along the same line or road. Bodies moving at right angles do not close a gap at the simple sum or difference.
- **Worked example.** Two cyclists 40 km apart ride towards each other at 12 km/h and 8 km/h; the gap closes at 20 km/h, so they meet after 2 hours. A runner 60 m behind another, at 15 m/s against 9 m/s, catches up after 60/6 = 10 seconds.

### Part B - Circular tracks

### Shortcut 2: the first meeting on a circular track (Advanced)

- **Rule.** Two runners starting from the same point on a track of length L meet first anywhere in the same direction after L/|vA - vB|, and in opposite directions after L/(vA + vB).
- **Failure condition.** The formula assumes the same starting point and constant speeds. An offset start or a change of speed changes the first meeting.
- **Worked example.** On a 600 m track, runners at 8 m/s and 5 m/s start together in the same direction. They first meet anywhere after 600/3 = 200 seconds, when the faster runner has gained one lap.

### Shortcut 3: meeting at the starting point (Advanced)

- **Rule.** A meeting at the start point requires each runner to complete a whole number of laps at the same moment. Find the lap times, then the smallest time that is a whole-number multiple of each. When the lap times are whole-number related, that time is the least common multiple of the lap times.
- **Failure condition.** Using the relative-speed time for a start-point reunion is wrong. If the lap times are not commensurable, a common whole-lap moment may not exist at all.
- **Worked example.** On the same 600 m track, the lap times are 600/8 = 75 seconds and 600/5 = 120 seconds. The first common moment at the start point is the least common multiple, 600 seconds. Check: after 600 seconds one runner has completed 8 laps and the other 5. The first meeting anywhere, at 200 seconds, is not at the start point, because 200/75 is not a whole number.

**Advanced track check (drill item 5).** On a 400 m track, runners at 8 m/s and 5 m/s start from one point in the same direction. They first meet anywhere after 400/3, about 133.3 seconds, but they meet at the starting point only when both have completed whole laps, which needs 400 seconds, the least common multiple of 50 and 80. These are different questions with different answers.

### Shortcut 4: counting overtakes

- **Rule.** In the same direction, the faster runner passes the slower one every L/|vA - vB| seconds. In a time T, count the completed intervals, which is the whole part of T divided by that interval.
- **Failure condition.** Counting the starting moment as an overtaking, or rounding a fractional count upward, gives too many passes.
- **Worked example.** On a 300 m track, runners at 9 m/s and 6 m/s start together in the same direction. The faster one passes every 300/3 = 100 seconds. In 450 seconds, the passes occur at 100, 200, 300 and 400 seconds, so there are four.

### Shortcut 5: meetings in opposite directions over a period

- **Rule.** Opposite runners meet every L/(vA + vB) seconds from a common start. In a period T, the number of meetings is the whole part of T divided by that interval.
- **Failure condition.** Using the difference of speeds, or the wrong period, gives the wrong count.
- **Worked example.** On a 360 m track, runners at 5 m/s and 4 m/s start together in opposite directions. They meet every 360/9 = 40 seconds. In three minutes, the meetings occur at 40, 80, 120 and 160 seconds, so there are four.

### Part C - Races and head starts

### Shortcut 6: races with a head start

- **Rule.** If A gives B a head start of h metres in a race of length D, and both finish together, then vA : vB = D : (D - h).
- **Failure condition.** The ratio is inverted if you write the speed of the slower runner first. A head start given in time, rather than distance, needs a different conversion.
- **Worked example.** In a 300 m race, A gives B a head start of 20 m. Both finish together, so vA : vB = 300 : 280 = 15 : 14. A runs 15 units for every 14 that B runs.

### Shortcut 7: equal distance, equal time, and proportion

- **Rule.** For a fixed distance, time is inversely proportional to speed. For a fixed speed, distance is proportional to time.
- **Failure condition.** The inverse relation is wrong when the distance changes between the two cases.
- **Worked example.** Walking at 4 km/h and driving at 16 km/h over the same distance, the drive takes one quarter of the walking time.

### Shortcut 8: arrivals at two speeds

- **Rule.** If the same journey at two speeds arrives at different times, the difference in arrival times equals d/v1 - d/v2. Solve for d.
- **Failure condition.** Mixing minutes with hours before dividing gives a wrong distance.
- **Worked example.** At 4 km/h a walker reaches the office 8 minutes later than at 6 km/h. The difference is d/4 - d/6 = d/12, which equals 8 minutes or 2/15 hour, so d = 24/15 = 1.6 km.

### Part D - Sound, passings and changes

### Shortcut 9: sound

- **Rule.** Sound takes distance divided by its speed to arrive. The event happened earlier than the arrival by that travel time.
- **Failure condition.** Adding the travel time to the arrival time, instead of subtracting it, reverses the answer. When the source moves, the timing refers to the moment the sound was emitted.
- **Worked example.** Sound travels 330 m/s. A bang heard at 3:15:30 pm came from 1650 m away, so it travelled for 5 seconds and happened at 3:15:25 pm.

### Shortcut 10: a head start in angle on a circular track

- **Rule.** Measure each runner's position as an angle from the start, in the direction of running. If B starts a angle theta ahead of A in the same direction, and A reaches a point after turning through angle a, then at that moment B has turned through a - theta. The speed ratio is the two turned angles, a : (a - theta).
- **Failure condition.** The rule needs both runners in the same direction and a stated point of meeting. Adding the offset instead of subtracting it reverses the sign of the answer.
- **Worked example.** B is 60 degrees ahead of A, both running the same way. A meets B at the point diametrically opposite the start, after turning through 180 degrees. In that time B has turned through 180 - 60 = 120 degrees. The speed ratio is 180 : 120 = 3 : 2.

### Shortcut 11: a known distance as a fraction of the whole

- **Rule.** If a known distance k is a fraction p of the whole race, the race is k divided by p. Check the result by finding the remaining distance and its fraction.
- **Failure condition.** Reading the percentage as the fraction still to be run, or dividing by the complement, gives a race length that does not match the stated fraction.
- **Worked example.** A runner has covered 9 km, which is 60 per cent of the race. The race is 9 divided by 0.6 = 15 km. The remaining 6 km is 40 per cent of 15 km, which confirms the result.

### Shortcut 12: composing two head starts through a common base

- **Rule.** Express both rivals against one common runner. If X gives Y a head start of h1 and gives Z a head start of h2 in a race of length D, then when X runs D, Y runs D minus h1 and Z runs D minus h2. When Y runs D, Z runs (D minus h2) times D divided by (D minus h1). The head start Y must give Z is D minus that distance.
- **Failure condition.** Subtracting the two head starts (h1 minus h2) does not give the head start between Y and Z. The composition must go through the common base, because each head start is a ratio of distances, not a fixed amount.
- **Worked example.** In a 1000 m race, X gives Y 200 m and gives Z 400 m. When X runs 1000 m, Y runs 800 m and Z runs 600 m. When Y runs 1000 m, Z runs 600 times 1000 divided by 800, which is 750 m. So Y gives Z a start of 250 m.

### Shortcut 13: an unknown length from two passings

- **Rule.** A train passes a person walking in its own direction at relative speed V minus u, and a person walking towards it at relative speed V plus u. Both passings cover the same length L of train. So (V - u) times t1 equals (V + u) times t2, which equals L. Solve the two equations for V and then for L.
- **Failure condition.** Using the train's speed V alone for a passing where the person moves, or treating the two passings as covering different lengths, gives an equation for a different train. The same length must appear in both equations.
- **Worked example.** A man walking at 2 m/s in the same direction as a train is passed in 30 seconds. A man walking at 2 m/s towards the train is passed in 6 seconds. So (V - 2) times 30 = (V + 2) times 6, which gives 24V = 72 and V = 3 m/s. The length is (3 - 2) times 30 = 30 m. The check is (3 + 2) times 6 = 30 m.

### Shortcut 14: a second leg that starts when the first ends

- **Rule.** When the second signal starts only at the arrival of the first, its travel time is added to the chain of times. Work backwards from the last reception to the event: each leg's travel time is subtracted from the moment its signal was received.
- **Failure condition.** Starting the second leg at the event instead of at the first reception, or reading the second reception as the moment of the event, shifts the answer by the whole length of the chain.
- **Worked example.** A sound travels 250 m/s. A drone flies at 25 m/s from the camp to the spot of an explosion, takes a picture and returns the picture at once. A second drone starts when the first picture arrives and flies the same distance; its picture arrives 2 minutes after the first. The second flight takes 120 seconds, so the distance is 25 times 120 = 3000 m. The sound takes 3000 divided by 250 = 12 seconds. The first picture arrived at 6:00:00 pm, so the first drone left the camp 120 seconds earlier, at 5:58:00 pm, when the sound arrived. The explosion was 12 seconds before that, at 5:57:48 pm.

### Shortcut 15: a change of direction on a track

- **Rule.** Split the motion at the instant the direction changes. Before it, the runners meet when their difference in rounds is a whole number, measured from their common start. After it, they meet by the same test, but starting from the positions reached at the change. The change instant and the stopping instant are each counted once, and the stopping instant counts only if it is a meeting.
- **Failure condition.** Restarting the count as if the runners began together at the change, or counting the change instant in both phases, gives the wrong total.
- **Worked example.** X runs 2 rounds per minute and Y runs 1 round per minute in the same direction for 2 minutes. Then Y reverses at 2 rounds per minute, and X keeps going until he has run 8 rounds. Before the change, X minus Y is t rounds, so they meet at t = 1 and t = 2 minutes, and the second is the change instant. After the change, with s minutes since then, X is at 4 + 2s and Y is at 2 - 2s rounds. So X minus Y is 2 + 4s rounds, a whole number whenever 4s is a whole number. That gives s = 1/4, 1/2, and so on up to s = 2, the stopping instant: eight meetings. The total is 2 + 8 = 10.

### The strongest wrong method and the reply

The tempting wrong method is to add speeds whenever two bodies move, as if they always approach. The reply is that the sum applies only when they approach along one line. Chasing bodies gap at the difference. A second wrong method takes the first meeting on a circle as the moment they meet at the start. The reply is that a meeting at the start needs whole laps for both runners, which is a different condition.

**Advanced traps (labelled Advanced).** Adding speeds for same-direction overtaking is wrong: subtract for the same direction and add only for opposite directions. A start-point reunion is not a relative-speed meeting: it needs both runners to complete whole laps.

### UPSC application

Read the stem for three things: whether the motion is along one line or round a closed track, whether the bodies start together, and what is asked: the first meeting, the count of meetings, the point where they meet or the moment both return to the start. Race ratios and time-distance comparisons follow the same proportion logic and often need only one line of working.

### Revision points

- On one line, opposite motion adds speeds and same-direction motion subtracts them.
- The meeting time is the gap divided by the relative speed.
- On a circular track, the first same-direction meeting is L divided by the speed difference.
- A meeting at the start point needs whole laps for both runners, so use the least common multiple of the lap times.
- Overtakes and meetings are counted by the whole part of the period divided by the interval; the start moment is not counted.
- A head start of h in a race of D gives speeds in the ratio D : (D - h).
- For a fixed distance, time falls as speed rises.
- A difference in arrival times at two speeds gives the distance through d/v1 - d/v2.
- Sound takes distance divided by its speed; the event is earlier than the reception by that time.
- An offset start on a circle gives the speed ratio a : (a - offset).
- A known distance that is a fraction p of the race gives the race as the distance divided by p.
- Two head starts combine through a common base, not by subtracting them.
- An unknown length follows from a same-direction and an opposite-direction passing.
- A second leg adds its travel time to the chain; the second flight starts at the first reception.
- A change of direction splits the count into phases; the change and stop instants are each counted once.

The relative-speed idea has one further use, which connects motion to a different kind of cycle. Two hands on a clock move at different constant speeds, so the angle between them changes like the gap between two runners on a circle. The clock is therefore the same relative-motion problem in a different unit, and the next lesson applies it along with the calendar.

### Retrieval before the practice

1. Two runners on a 400 m track start together in the same direction at 8 m/s and 6 m/s. When do they first meet anywhere?
   *Answer: 400/2 = 200 seconds.*
2. A runner is 30 m ahead of another and both run in the same direction, the front runner at 5 m/s and the rear one at 7 m/s. How long until the rear runner catches up?
   *Answer: 30/2 = 15 seconds.*
3. Why does a start-point reunion not use the relative-speed formula?
   *Answer: it requires both runners to finish whole laps at the same moment, which is a least-common-multiple condition, not a gap condition.*

### Practice

**MCQ 8**

On a circular track, runner A starts behind runner B, who is 50 degrees ahead of A, and both run the same way. A meets B at the point that A reaches after turning through 330 degrees. What is the ratio of A's speed to B's speed?

- A. 28 : 33
- B. 33 : 23
- C. 33 : 38
- D. 33 : 28

**MCQ 8 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Inverts the ratio. A turns through the larger angle, so A's speed is the larger term.
- **B — Incorrect:** Subtracts the offset twice: B turns through 330 minus 100 = 230 degrees, which gives 33 : 23.
- **C — Incorrect:** Adds the offset instead of subtracting it: B turns through 330 plus 50 = 380 degrees, which is not the angle B turns.
- **D — Correct:** B turns through 330 minus 50 = 280 degrees. The ratio is 330 : 280 = 33 : 28.

**MCQ 9**

A train passes a man walking at 3 m/s in the same direction as the train in 40 seconds. It passes a man walking at 1 m/s towards it in 8 seconds. How long is the train, in metres?

- A. 40 m
- B. 160 m
- C. 120 m
- D. 32 m

**MCQ 9 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Let the train's speed be V. (V - 3) times 40 = (V + 1) times 8 gives V = 4 m/s, and the length is (4 - 3) times 40 = 40 m. The check is (4 + 1) times 8 = 40 m.
- **B — Incorrect:** Uses the train's speed for the same-direction passing: 4 times 40 = 160 m. The man moves in the same direction, so the relative speed is 4 minus 3.
- **C — Incorrect:** Uses the man's speed as the relative speed for the same-direction passing: 3 times 40 = 120 m.
- **D — Incorrect:** Uses the train's speed with the opposite-direction time: 4 times 8 = 32 m. The opposite passing gives the length through (V + 1) times 8, not V times 8.

**MCQ 10**

A sensor hears a bang 6 seconds after it sees the flash of the same explosion. Light arrives at once, and sound travels at 330 m/s. How far is the explosion from the sensor, in metres?

- A. 2040 m
- B. 1980 m
- C. 990 m
- D. 55 m

**MCQ 10 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Uses 340 m/s for sound. The stem gives 330 m/s, so 6 times 340 = 2040 m is the product of the wrong speed.
- **B — Correct:** Distance is speed times time: 330 times 6 = 1980 m. The flash arrives at once, so all the 6 seconds belong to the sound.
- **C — Incorrect:** Halves the time, so the sound is counted as if it travelled out and back. The sound travels one way from the explosion to the sensor.
- **D — Incorrect:** Divides the speed by the time, 330 divided by 6 = 55. Speed multiplied by time gives distance; the division is the reverse operation.

**MCQ 11**

Runner X runs 3 rounds per minute and runner Y runs 1 round per minute, both in the same direction from the same start, at the same moment. After 2 minutes, Y stops for good. They stop when X has completed 9 rounds, and a meeting at that instant counts. How many times do they meet after the start?

- A. 6
- B. 4
- C. 7
- D. 3

**MCQ 11 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Omits the meeting at the stopping instant. The stem says that a meeting at the stop counts, and at that moment X and Y are at the same point.
- **B — Incorrect:** Counts only the meetings before Y stops: X minus Y is 2t rounds, a whole number at t = 0.5, 1, 1.5 and 2 minutes.
- **C — Correct:** Before Y stops, X minus Y is 2t rounds, which is whole at 0.5, 1, 1.5 and 2 minutes: four meetings. After it, Y is at 2 rounds and X is at 6 + 3s rounds, so X minus Y is 4 + 3s, whole at s = 1/3, 2/3 and 1: three meetings. The total is seven.
- **D — Incorrect:** Counts only the meetings after Y stops, when X passes the stopped Y. The meetings before the stop are also after the start.

---

## Lesson 4 - Clocks and calendars

Progress: Lesson 4 of 7 | Stage: Core | Subtopic: Clocks and calendars

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the clock as a relative-motion problem

```text
   12 o'clock = 0 degrees, clockwise
   minute hand: 6 degrees per minute
   hour hand:   0.5 degrees per minute (30 per hour)
   gap between them grows at 5.5 degrees per minute

        12                       the angle between hands
     11    1                     = |30 x H - 5.5 x M|
   10        2                   H on a 12-hour dial (H mod 12)
    9    o    3                  larger than 180?  take 360 - angle
     8        4
        7   6 5

   CALENDAR: weekday(next date) = weekday(date) + days between, mod 7
```

On the clock dial, the minute hand gains on the hour hand at 5.5 degrees per minute. A reading of the clock is therefore a question about relative motion, just as in the last lesson. The same mod-7 arithmetic gives the weekday of a date, because a week is a cycle of seven days.

### Plain intuition

The hour hand moves slowly, the minute hand quickly. Each minute, the minute hand gains 5.5 degrees on the hour hand. The gap between the hands, measured from the hour hand, therefore changes steadily, and the hands coincide, or are at right angles, at regular intervals. Coincidences are not a single event each hour; they recur at a fixed interval of about 65 minutes.

A calendar works like a dial with seven positions. Each ordinary day moves the weekday forward by one place, and a week returns to the same weekday. The question about a year is therefore a question about how many days have passed, counted modulo seven.

### Doctrine: the clock formula

For time H hours and M minutes, the angle between the hands is |30H - 5.5M| degrees, with H taken on a twelve-hour dial, so H mod 12. The formula gives the angle measured one way round. The angle the hands make is the smaller of that value and 360 minus it, so an answer above 180 degrees is replaced by 360 minus itself.

### Part A - Clock angles and coincidences

### Shortcut 1: the angle between the hands

- **Rule.** Use H = hour mod 12, compute |30H - 5.5M|, and if the result exceeds 180, report 360 minus it.
- **Failure condition.** Using a 24-hour hour, such as 15 for 3 pm, or forgetting the minute term, gives a wrong answer. An answer above 180 is never the angle the hands make.
- **Worked example.** At 3:40, H = 3 and the angle is |90 - 220| = 130 degrees. At 9:15, the angle is |270 - 82.5| = 187.5 degrees, which exceeds 180, so the smaller angle is 360 - 187.5 = 172.5 degrees.

**Basic worked check (Example D).** At 4:20 the angle is |120 - 110| = 10 degrees. At 2:50 the formula gives |60 - 275| = 215 degrees, which is more than 180, so the smaller angle is 360 - 215 = 145 degrees.

### Shortcut 2: how often the hands coincide

- **Rule.** The hands coincide at minutes 720k/11 after 12 o'clock for k = 0, 1, ..., 10. That is eleven times in twelve hours and twenty-two times in a day.
- **Failure condition.** Taking twelve coincidences per twelve hours, on the assumption that the twelfth falls at the end of the cycle, double-counts the start-of-cycle moment.
- **Worked example.** The first coincidence after 12 o'clock is at 720/11 = 65 5/11 minutes, so at about 1:05:27. Between 3 pm and 9 pm there are six coincidences, for k = 3 to 8.

### Shortcut 3: right angles and straight lines

- **Rule.** The hands are at right angles 22 times in twelve hours, when the angle is 90 or 270 degrees. They are in a straight line 11 times in twelve hours, when the angle is 180 degrees.
- **Failure condition.** Confusing right angles with coincidences. The right-angle count is twice the coincidence count.
- **Worked example.** At exactly 3:00 the hands are at right angles, and the next right angle is at 3:32 8/11 minutes, which is about 3:32:44.

### Part B - Clock drift and striking clocks

### Shortcut 4: clocks that gain or lose

- **Rule.** The error after a time is the gain per unit time multiplied by the elapsed time. A clock shows the same time as the true time again only when the accumulated error is a whole number of full dials.
- **Failure condition.** Mixing hours of elapsed time with minutes of gain per day is a common unit slip.
- **Worked example.** A clock that gains 6 minutes every 24 hours gains 6 x 5 = 30 minutes in 120 hours, five days.

### Part C - Calendars and same-calendar years

### Shortcut 5: odd days and the leap-year shift

- **Rule.** The weekday moves forward by the number of days between two dates, modulo seven. Over one year the shift is 1 when the span contains no 29 February and 2 when it does.
- **Failure condition.** Adding 2 for every leap year, even when the span does not reach 29 February, is wrong. Equally wrong is adding 1 for a leap year that lies entirely inside the span.
- **Worked example.** A date in 1 December 2027 is a Wednesday. The span to 1 December 2028 contains 29 February 2028, so the shift is 2, and 1 December 2028 is a Friday.

### Shortcut 6: the century rule (Advanced)

- **Rule.** A year divisible by 4 is leap, except that a century year is leap only when it is divisible by 400. So 2000 is leap, while 1900 and 2100 are not.
- **Failure condition.** Writing "every hundred years contains five odd days" is not a fixed fact. The count depends on the century span: 1901 to 2000 contains 6 odd days, 2001 to 2100 contains 5, and 400 years contain 0.
- **Worked example.** 1 March 2100 is a Monday. The span to 1 March 2101 contains no 29 February, because 2100 is not leap, so the shift is 1 and 1 March 2101 is a Tuesday.

**Advanced calendar check (drill item 7; Advanced Method 6).** If 1 January 2099 is a Friday, 2099 is not a leap year, so 1 January 2100 is a Saturday. Before moving to 2101, test the century rule: 2100 is not divisible by 400, so it is not leap, and 1 January 2101 is a Sunday.

### Shortcut 7: meetings that repeat at intervals

- **Rule.** Two periodic events meet at the least common multiple of their periods. The weekday of the next meeting is the weekday of the first meeting moved forward by that LCM, modulo seven.
- **Failure condition.** Using the sum or the product of the periods instead of the LCM gives the wrong day.
- **Worked example.** One visitor comes every 6 days and another every 8 days. They meet every LCM(6, 8) = 24 days. Since 24 mod 7 = 3, a meeting on Sunday is followed by the next joint meeting on Wednesday.

### Shortcut 8: which weekdays occur five times in a month

- **Rule.** A month of 28 days has four of each weekday. The extra days of a longer month are the first days of that month, so a 31-day month starting on a Saturday has five Saturdays, five Sundays and five Mondays.
- **Failure condition.** The shortcut depends on the length of the month and on the weekday of its first day, so both must be known before counting.
- **Worked example.** In a 31-day month that starts on a Saturday, Saturday, Sunday and Monday each occur five times, and Tuesday to Friday occur four times.

### Shortcut 9: striking clocks

- **Rule.** A clock that strikes once at 1 o'clock, twice at 2 o'clock and so on strikes 1 + 2 + ... + 12 = 78 times in twelve hours. A run of n strikes has n - 1 intervals between its first and last strike, so the run lasts (n - 1) times the interval.
- **Failure condition.** Using the number of strikes as the number of intervals adds one interval too many. Two runs separated by a pause must be timed separately.
- **Worked example.** If a run of 3 strikes takes 4 seconds from the first strike to the last, each interval is 2 seconds. A run of 5 strikes then takes 4 x 2 = 8 seconds.

### Shortcut 10: right angles at the boundary of an hour (Advanced)

- **Rule.** The hands are at right angles when |30H - 5.5M| is 90 or 270 degrees. For a given hour, solve for M, keep the roots with 0 less than or equal to M less than 60, and let a root with M of 60 or more belong to the next hour. Each hour carries at most two right-angle roots, and the boundary root decides which hour it counts in.
- **Failure condition.** Counting every root of the equation as belonging to the hour in which it was solved. A root with M of 60 or more is already a moment of the next hour, so counting it in both hours double-counts it.
- **Worked example.** From 3 o'clock, the equation |90 - 5.5M| = 90 has the roots M = 0 and M = 360/11 = 32 8/11 minutes, which is 3:32:44. The equation |90 - 5.5M| = 270 has the root M = 720/11 = 65 5/11 minutes. That root is past 60 minutes, so it is the right angle at 4:05:27 and belongs to the next hour.

### Shortcut 11: the same calendar in another year

- **Rule.** Two years have the same calendar when they begin on the same weekday and have the same leap status, both common or both leap. Find the weekday of 1 January of each year and compare. The first year after a given year with the same calendar is the first year that matches both tests.
- **Failure condition.** Matching only the weekday of 1 January ignores the leap status. Two years can start on the same weekday and still differ in February.
- **Worked example.** 2003 begins on a Wednesday and is a common year. 2014 also begins on a Wednesday and is common, so 2014 has the same calendar as 2003. The year 2008 is a leap year beginning on a Tuesday, so it does not match 2003 on either test.

### Part D - Sequences, powers and windows

### Shortcut 12: a date sequence with a constant gap

- **Rule.** Add the constant gap in days to each date, counting every calendar day. A leap day, 29 February, is counted when it falls inside the interval.
- **Failure condition.** Ignoring 29 February in a leap year gives every later date one day too early. Counting the first date as day one shifts the whole sequence by one day.
- **Worked example.** Take 20 January 2000 and a gap of 35 days. The next date is 24 February 2000: 11 days reach 31 January, and 24 more reach 24 February. The one after is 30 March 2000, because 5 days reach 29 February and 30 more reach 30 March. The following term is 4 May 2000, since 1 day reaches 31 March, 30 more reach 30 April, and 4 more reach 4 May.

### Shortcut 13: a large power of days and the weekday

- **Rule.** A number of days D after a weekday is reduced modulo 7. A power of a number is reduced by finding the period of its residues modulo 7. For a power of 2, the residues are 2, 4, 1, which repeat every 3 powers, so 2 to the power n has the residue of 2 to the power (n modulo 3).
- **Failure condition.** Reducing the exponent modulo 7 instead of modulo the period of the residues gives the wrong residue. The period of the residues, not 7, decides the cycle.
- **Worked example.** Find the weekday 2 to the power 100 days after a Monday. Since 2 cubed is 8, which leaves residue 1 modulo 7, the residue of 2 to the power 100 is the residue of 2 to the power (100 modulo 3), which is 2 to the power 1, so the residue is 2. Monday moved forward by 2 days is Wednesday.

### Shortcut 14: coincidences inside a window

- **Rule.** Two or more periodic events coincide at the least common multiple of their periods. Count the multiples of that least common multiple inside the window, and exclude the starting moment. If the window ends exactly at a coincidence, count it once.
- **Failure condition.** Using the sum or the product of the periods instead of the least common multiple gives the wrong interval. Counting the starting moment as a coincidence adds one more.
- **Worked example.** Three signals repeat every 60, 80 and 100 seconds and start together. Their least common multiple is 1200 seconds, which is 20 minutes. Within the following hour, the coincidences fall at 1200, 2400 and 3600 seconds, so there are three, the last at the end of the hour.

### The strongest wrong method and the reply

The tempting wrong method for the clock is to read the hour and minute hands as two independent numbers and subtract them. The reply is that the hour hand moves between the numbers as the minutes pass, so its position must include 0.5 degrees per minute. A second wrong method treats every year divisible by 4 as leap. The reply is that 1900 and 2100 are not leap, so the test must include the century exception before any odd days are counted.

### UPSC application

Read a clock item for three things: the hour on a twelve-hour dial, the minute, and the question asked, which may be an angle, a count of coincidences or right angles, or a time when the angle first takes a given value. Read a calendar item for the reference date, the date asked for, and whether 29 February falls in between. Periodic-meeting items need the LCM first and the weekday shift second.

### Revision points

- The angle between the hands is |30H - 5.5M| with H taken on a twelve-hour dial.
- An angle above 180 degrees is replaced by 360 minus itself.
- The hands coincide eleven times in twelve hours and twenty-two times in a day.
- A clock's error is its rate times the elapsed time.
- The weekday shift over a year is 1 in a common year and 2 when 29 February lies in the span.
- A century year is leap only when divisible by 400.
- The odd days in a century depend on the span: 6 for 1901 to 2000, 5 for 2001 to 2100, and 0 for 400 years.
- Periodic meetings occur at the LCM of the periods, and the weekday moves by the LCM modulo seven.
- A month's surplus days are its first days, so the weekdays that occur five times are fixed by the first day.
- A run of n strikes has n minus one intervals; a clock that strikes at each hour from one to twelve strikes 78 times in twelve hours.
- A right-angle root with M of 60 or more belongs to the next hour.
- Two years share a calendar only when the weekday of 1 January and the leap status both match.
- A constant gap of days counts every calendar day, including 29 February inside the interval.
- A large power's weekday uses the period of its residues modulo 7, not the exponent modulo 7.
- Coincidences in a window fall at multiples of the least common multiple of the periods.

The calendar and the clock both reduce a question to a count of cycles plus a remainder. The next lesson applies the same habit to shapes. There the remainder is a geometric relation, a right angle or a similar figure, and it is usually the step that the stem tests most often.

### Retrieval before the practice

1. A clock shows 2:30. What is the angle between the hands?
   *Answer: |30 x 2 - 5.5 x 30| = |60 - 165| = 105 degrees, which is below 180.*
2. Why is 1900 not a leap year, while 2000 is?
   *Answer: a century is leap only when divisible by 400; 1900 is not, and 2000 is.*
3. Which weekday is 14 February of a year if 14 February of the previous year was a Thursday and 29 February lies between the two dates?
   *Answer: the shift is 2 because 29 February lies in the span, so Thursday moves forward two places to Saturday.*

### Practice

**MCQ 12**

Which is the first year after 2010 that has the same calendar as 2010?

- A. 2011
- B. 2016
- C. 2022
- D. 2021

**MCQ 12 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 2011 begins one weekday later than 2010, so it does not share 2010's calendar.
- **B — Incorrect:** 2016 begins on the same weekday as 2010, but it is a leap year, so February differs. The two tests must both agree.
- **C — Incorrect:** 2022 begins one day after 2021 and two days after 2020, so it differs from 2010 in weekday.
- **D — Correct:** 2010 begins on a Friday and is a common year. 2021 also begins on a Friday and is common, so its calendar is the same.

**MCQ 13**

A clock strikes once at 1 o'clock, twice at 2 o'clock, and so on up to 12 o'clock. How many times does it strike in one full day of 24 hours?

- A. 156
- B. 78
- C. 144
- D. 180

**MCQ 13 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** A 12-hour cycle has 1 + 2 + ... + 12 = 78 strikes, and a day has two such cycles: 2 times 78 = 156 strikes.
- **B — Incorrect:** Counts only one 12-hour cycle, 78 strikes, and forgets the second cycle of the day.
- **C — Incorrect:** Assumes each of the twelve hours strikes twelve times: 12 times 12 = 144. The strikes at each hour equal the hour number.
- **D — Incorrect:** Counts the noon and midnight strikes a second time: each of those two strikes is 12 strikes, so 156 + 24 = 180. Only the 24 extra strikes are added, not twelve.

**MCQ 14**

Starting from a Monday, what weekday is reached after 3 to the power 20 days?

- A. Tuesday
- B. Wednesday
- C. Thursday
- D. Sunday

**MCQ 14 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Reduces the exponent modulo seven instead of the period of the powers of 3. Since 20 modulo 7 is 6, 3 to the power 6 leaves residue 1, and Monday moved forward by 1 day is Tuesday.
- **B — Correct:** The powers of 3 modulo 7 are 3, 2, 6, 4, 5, 1, repeating every 6. Since 20 modulo 6 is 2, the residue of 3 to the power 20 is 2. Monday moved forward by 2 days is Wednesday.
- **C — Incorrect:** Uses only one power, 3 days after Monday, which is Thursday. The exponent is not applied to the cycle at all.
- **D — Incorrect:** Uses the day count modulo seven without the power: 20 modulo 7 is 6, and Monday moved forward by 6 days is Sunday.


**MCQ 15**

At 7:45, what is the smaller angle between the hour hand and the minute hand, in degrees?

- A. 112.5
- B. 15
- C. 37.5
- D. 150

**MCQ 15 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Drops the hour term: 5.5 x 45 = 247.5 and 360 minus 247.5 = 112.5. The hour hand's position matters.
- **B — Incorrect:** Uses 5 degrees per minute for the minute hand: |210 - 225| = 15. The minute hand moves 6 degrees a minute, and the hour hand 0.5 degrees a minute.
- **C — Correct:** The hour hand is at 7 x 30 + 0.5 x 45 = 232.5 degrees and the minute hand at 270 degrees. The difference is 37.5 degrees, which is below 180.
- **D — Incorrect:** Places the minute hand at 12: the angle is 210 degrees, and its smaller form is 150. The minute hand has moved 45 minutes.

---

## Lesson 5 - Geometry: Pythagoras, angles, circles, similarity, coordinates and right-triangle ratios

Progress: Lesson 5 of 7 | Stage: Core and Class X trigonometry | Subtopic: Geometry: Pythagoras, angles, circles, similarity, coordinates and right-triangle ratios

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: a right angle is the key that unlocks the formulas

```text
                 RIGHT ANGLE IDENTIFIED?
                 /                    \
              YES                      NO
               |                        |
     Pythagoras: c^2 = a^2 + b^2    do not use Pythagoras;
     tan = opposite / adjacent      look for parallel lines,
     sin, cos from the hypotenuse   equal angles, or similar shapes
               |
     diameter as one side? -> the third vertex on the circle
                              is a right angle

   SIMILAR FIGURES: lengths x k, areas x k^2, volumes x k^3
   COORDINATES:     straight-line distance = sqrt(dx^2 + dy^2)
```

The diagram sorts the geometry into two questions. First, is there a right angle? If yes, the Pythagorean and trigonometric relations are available. If not, the figure must be read through its parallel lines, equal angles or similarity. Most errors in this lesson come from applying a right-angle formula to a triangle that has no right angle.

### Plain intuition

A right angle is the only angle that makes two perpendicular lengths and a diagonal behave like the sides of a square. Pythagoras says that the area of the square on the diagonal equals the sum of the areas of the squares on the two shorter sides. The result depends on the right angle, not on the sizes of the sides. A triangle with sides 3, 4 and 5 is right-angled; one with sides 3, 4 and 4.5 is not.

Similar figures are the same shape at a different size. If every length is multiplied by k, every area is multiplied by k squared, and every volume by k cubed. Area grows faster than length because it is two-dimensional.

### Doctrine: the working relations

- **Pythagoras.** In a right-angled triangle with legs a and b and hypotenuse c, c squared equals a squared plus b squared.
- **Parallel and perpendicular lines.** A transversal makes equal corresponding angles with two parallel lines. A line perpendicular to one of two parallel lines is perpendicular to the other. Two lines perpendicular to the same line are parallel to each other.
- **Angles in a triangle.** The three angles sum to 180 degrees.
- **Circle.** An angle in a semicircle is a right angle. A triangle whose side is a diameter and whose third vertex lies on the circle is right-angled at that vertex.
- **Similarity.** Similar triangles have equal angles and proportional sides. Their areas are in the ratio of the squares of the sides.
- **Coordinates.** The distance between (x1, y1) and (x2, y2) is the square root of (x2 - x1) squared plus (y2 - y1) squared.

### Shortcut 1: Pythagoras, but only after the right angle

- **Rule.** Identify the right angle, then take the hypotenuse as the longest side and square-root the sum of the squares of the two others.
- **Failure condition.** Using the formula on a triangle with no marked right angle is unsafe. Subtracting squares gives a leg only when the hypotenuse is known.
- **Worked example.** A ladder 15 m long stands on the ground with its foot 9 m from a vertical wall. The wall and the ground meet at a right angle, so the height is sqrt(15 squared - 9 squared) = sqrt(225 - 81) = 12 m.

### Shortcut 2: diagonals of rectangles and boxes

- **Rule.** The diagonal of a rectangle with sides l and b is sqrt(l squared + b squared). The space diagonal of a box with edges x, y and z is sqrt(x squared + y squared + z squared).
- **Failure condition.** Taking the sum of the sides, or using only two of the three edges of a box, gives a wrong length.
- **Worked example.** A rectangle of sides 8 and 6 has diagonal 10. A box with edges 2, 3 and 6 has space diagonal sqrt(4 + 9 + 36) = 7.

### Shortcut 3: parallel and perpendicular lines

- **Rule.** Angles made by a transversal with parallel lines are equal in the corresponding positions. Perpendicularity passes from one of two parallel lines to the other.
- **Failure condition.** Assuming two lines are parallel just because they look parallel, or because they are both perpendicular to a line that is not drawn, is unsafe.
- **Worked example.** Line X is perpendicular to line Y and parallel to line Z. Then Z is perpendicular to Y, because a parallel of X inherits X's angle with Y.

### Shortcut 4: the right angle in a semicircle

- **Rule.** If AB is a diameter and C is any other point on the circle, the angle ACB is 90 degrees.
- **Failure condition.** The rule needs the side to be a diameter through the centre. If AB is an ordinary chord, the angle at C changes with the position of C.
- **Worked example.** Six points are equally spaced on a circle. Each of the three diameters, joined to any of the other four points, gives a right triangle, so there are 3 x 4 = 12 right triangles with a diameter as one side.

### Shortcut 5: similar triangles and scaling

- **Rule.** For a scale factor k, lengths multiply by k, areas by k squared and volumes by k cubed.
- **Failure condition.** The scaling rule holds only for similar figures. Two figures with the same area, or with one pair of equal sides, are not related by a scale factor.
- **Worked example.** The 3, 4, 5 right triangle, of area 6, scaled by 4 gives sides 12, 16 and 20 and an area of 4 squared times 6 = 96.

### Shortcut 6: distance on a plane and on a grid

- **Rule.** The straight-line distance between two points is the square root of the sum of the squared coordinate differences.
- **Failure condition.** Routes that must follow streets or grid lines are not straight. Their length is the sum of the moves, not the straight-line distance.
- **Worked example.** From (-2, 1) to (4, 9) the straight-line distance is sqrt(36 + 64) = 10. Walking along a grid from (0, 0) to (3, 4) takes 3 + 4 = 7 blocks, while the straight-line distance is 5.

### Shortcut 7: right-triangle ratios (Class X trigonometry)

- **Rule.** In a right triangle with angle theta, sin theta = opposite/hypotenuse, cos theta = adjacent/hypotenuse, and tan theta = opposite/adjacent. Also sin squared theta + cos squared theta = 1 and tan theta = sin theta / cos theta.
- **Failure condition.** Using tan when the hypotenuse is given, or mixing up which side is opposite, reverses the answer. The ratios apply only to a right-angled triangle.
- **Worked example.** A 10 m ladder makes an angle of 60 degrees with the ground. Its height is 10 sin 60 degrees = 10 x sqrt(3)/2 = 5 sqrt(3), about 8.66 m, and its foot is 10 cos 60 degrees = 5 m from the wall.

Standard values for the angles that appear most often are: at 30 degrees, sin = 1/2, cos = sqrt(3)/2 and tan = 1/sqrt(3); at 45 degrees, sin = cos = 1/sqrt(2) and tan = 1; at 60 degrees, sin = sqrt(3)/2, cos = 1/2 and tan = sqrt(3).

### Shortcut 8: how many points a circle and a polygon share

- **Rule.** A straight line meets a circle in 0, 1 or 2 points. Each side of a convex polygon lies on such a line and is a segment of it, so each side meets the circle in at most two points. The maximum count is therefore twice the number of sides, and it is reached only when every side cuts the circle twice inside the segment. The minimum is 0, when the circle lies apart from the polygon.
- **Failure condition.** Counting only the vertices, or assuming each side meets the circle once, undercounts. A tangent side gives one point, and a secant gives two.
- **Worked example.** Take a regular hexagon with side s. Its apothem is about 0.87 s and its circumradius is s. A circle centred at the hexagon's centre with radius 0.9 s cuts each side twice, inside the segment, so the count is 12, which is twice the six sides. A circle through the six vertices meets the hexagon only at its six vertices, so the count is 6.

### Shortcut 9: collinear points from coordinates

- **Rule.** Three points are on one line when the slope from one point to the second equals the slope from the same point to the third. For points P, Q and R, the test is (Qx minus Px) times (Ry minus Py) equal to (Qy minus Py) times (Rx minus Px). Use the differences from one shared point.
- **Failure condition.** Comparing slopes of two pairs that share no point proves nothing. The two slopes must share one of the three points.
- **Worked example.** Take P(1, 1), Q(2, 3) and R(3, 5). The slope from P to Q is (3 - 1)/(2 - 1) = 2, and the slope from P to R is (5 - 1)/(3 - 1) = 2. The three points are on one line.

### Shortcut 10: a point dividing a line in a given ratio

- **Rule.** Let PQ = m and QR = n, in the same unit. Three points on a line have three possible orders, and each order fixes PR. If Q lies between P and R, PR = m + n. If P lies between Q and R, PR = n - m, which needs n greater than m. If R lies between P and Q, PR = m - n, which needs m greater than n. The number of values of the ratio PQ : PR is therefore 2 when m differs from n, and 1 when they are equal.
- **Failure condition.** Taking only the order in which the points are written gives one value and misses the case in which the middle point is an end point. Equal parts give only one value, because the two other orders are impossible.
- **Worked example.** Let PQ : QR = 2 : 7. If Q is between P and R, PR = 9 and PQ : PR = 2 : 9. If P is between Q and R, PR = 7 - 2 = 5 and PQ : PR = 2 : 5. So there are two values of PQ : PR.

### Shortcut 11: equilateral triangles on a circle

- **Rule.** An equilateral triangle inscribed in a circle has its vertices a third of a turn apart. With n equally spaced points on the circle, and 3 dividing n, each triangle uses three points spaced n divided by 3 places apart. Each starting point gives one triangle, and the starting points repeat after n divided by 3 steps, so there are n divided by 3 triangles.
- **Failure condition.** Counting every set of three points gives the number of all triangles, most of which are not equilateral. If 3 does not divide n, no equilateral triangle has its vertices among the points.
- **Worked example.** Take 18 equally spaced points. The triangles use points i, i + 6 and i + 12 for i = 0 to 5, so there are 6 equilateral triangles.

### The strongest wrong method and the reply

The tempting wrong method is to apply Pythagoras to any triangle with three known sides. The reply is that the relation c squared = a squared + b squared holds only for a right angle, so the first step is always to test whether the angle is right. A second wrong method assumes that a line which looks perpendicular is perpendicular. The reply is that the stem must give the right angle, or it must follow from parallel lines and equal angles.

### UPSC application

For geometry items, first name the figure and mark every right angle, parallel line or equal angle the stem gives. Then choose the one relation that uses them. Counting items, such as the number of right triangles on a circle, need the semicircle rule before any counting. Similarity items need the scale factor and the square rule for areas. Coordinate items need the straight-line distance only when the path is straight.

### Revision points

- Pythagoras applies only when the right angle is identified.
- The sum of squares of the legs equals the square of the hypotenuse.
- A rectangle diagonal is the square root of the sum of squares of its two sides.
- A box diagonal uses all three edges.
- A line perpendicular to one of two parallel lines is perpendicular to both.
- The angle in a semicircle is a right angle, and only a diameter gives this result.
- Scaling by k multiplies lengths by k, areas by k squared and volumes by k cubed.
- Grid routes add their blocks; they are not straight-line distances.
- Sin, cos and tan are ratios of sides in a right triangle, and sin squared plus cos squared is one.
- The standard values at 30, 45 and 60 degrees appear in almost every trigonometry item.
- A line meets a circle in at most two points, so a polygon with n sides meets it in at most 2n.
- Collinearity is tested by equal slopes that share one point.
- A point dividing a line in a ratio has one value for each order of the points.
- Equilateral triangles on n equally spaced points number n divided by 3 when 3 divides n.

The geometry of this lesson is about lengths and angles of plane figures. The next lesson turns the same plane figures into areas, circles and solids.

### Retrieval before the practice

1. A right triangle has legs 6 and 8. What is its hypotenuse?
   *Answer: sqrt(36 + 64) = 10.*
2. A triangle is similar to another with sides in ratio 3 : 1. What is the ratio of their areas?
   *Answer: 9 : 1, because area scales by the square of the scale factor.*
3. A point is at (1, 1) and another at (4, 5). What is the straight-line distance, and what is the grid distance?
   *Answer: the straight-line distance is sqrt(9 + 16) = 5; the grid distance is 3 + 4 = 7.*

### Practice

**MCQ 16**

What is the greatest possible number of points that the sides of a triangle and a circle can have in common?

- A. 3
- B. 2
- C. 4
- D. 6

**MCQ 16 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Counts one common point for each side, which is the number of sides. Each side can meet the circle twice, so each side can give two points.
- **B — Incorrect:** Treats the whole triangle as one straight line. A line meets a circle in at most two points, but the triangle has three sides.
- **C — Incorrect:** Counts two points for each of two sides and forgets the third side. Each of the three sides can meet the circle twice.
- **D — Correct:** Each of the three sides meets the circle in at most two points, so the greatest count is 3 times 2 = 6.

**MCQ 17**

Four points have coordinates A (0, 0), B (2, 1), C (4, 2) and D (1, 3). Which three of them lie on one straight line?

- A. A, B and C
- B. A, B and D
- C. A, C and D
- D. B, C and D

**MCQ 17 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The slope from A to B is 1/2 and the slope from A to C is 2/4 = 1/2, so A, B and C lie on one line.
- **B — Incorrect:** The slope from A to B is 1/2, but the slope from A to D is 3, so D is not on the line through A and B.
- **C — Incorrect:** The slope from A to C is 1/2, but the slope from A to D is 3, so D is not on the line through A and C.
- **D — Incorrect:** The slope from B to C is 1/2 but from B to D is -2, so the three points are not collinear.

**MCQ 18**

Three points P, Q and R lie on a straight line with PQ : QR = 2 : 3. What is the greatest possible value of PR divided by QR?

- A. 1/3
- B. 5/3
- C. 3/5
- D. 2/3

**MCQ 18 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** The order with P between Q and R gives PR = 3 minus 2 = 1 unit, so the value is 1/3. That is the smaller of the two values, not the greatest.
- **B — Correct:** With Q between P and R, PR = 2 + 3 = 5 units, so PR divided by QR is 5/3. This is the greater of the two possible values.
- **C — Incorrect:** Inverts the quotient: QR divided by PR is 3/5, which is not the quantity the stem asks for.
- **D — Incorrect:** Repeats the given ratio of PQ to QR, which is 2/3. The question asks for PR divided by QR, not PQ divided by QR.

**MCQ 19**

From a point 20 m from the foot of a tower, the angle of elevation of the top of the tower is 45 degrees. What is the height of the tower, in metres?

- A. 20 sqrt(2)
- B. 40
- C. 20
- D. 10

**MCQ 19 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Uses the hypotenuse as the height: 20 divided by cos 45 degrees = 20 sqrt(2) m. The line of sight is longer than the height.
- **B — Incorrect:** Doubles the distance, giving 40 m. The tangent of 45 degrees is 1, so the height equals the distance.
- **C — Correct:** The height is opposite the 45-degree angle and the distance is adjacent, so height = 20 tan 45 degrees = 20 x 1 = 20 m.
- **D — Incorrect:** Halves the distance, giving 10 m. The tangent of 45 degrees is 1, not 1/2.

---

---
## Lesson 6 - Plane and solid mensuration

Progress: Lesson 6 of 7 | Stage: Core | Subtopic: Plane and solid mensuration

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: one dimension, two dimensions, three dimensions

```text
   LENGTH (units)           AREA (square units)          VOLUME (cubic units)
   -------------------      ------------------------     ----------------------
   perimeter                rectangle    l x b           cuboid     l x b x h
   circumference            triangle     (base x h)/2    cube       a cubed
   side, diagonal           trapezium    (a+b) x h / 2   cylinder   pi r^2 h
                            circle       pi r^2          cone       pi r^2 h / 3
                                                         sphere     4 pi r^3 / 3

   SURFACE (square units):  cube 6a^2;  cuboid 2(lb + bh + hl)
   SCALING:  length x k,  area x k^2,  volume x k^3
```

Read the table by dimension first. A length is a single measurement, an area is a measurement multiplied by a measurement, and a volume is a measurement multiplied by two more. The unit of the answer follows the dimension, and most mistakes in this lesson come from giving an area in linear units or a volume in square units.

### Plain intuition

An area counts how many unit squares cover a flat figure. A rectangle is the simplest case: put l squares in each row and b rows, and the count is l times b. A triangle is half of a rectangle with the same base and height, because a diagonal cuts the rectangle into two equal triangles. A circle is not built from squares, so its area needs the constant pi, the ratio of a circle's circumference to its diameter.

A volume counts unit cubes filling a solid. A box of length l, breadth b and height h holds l times b times h cubes. Cylinders, cones and spheres do not fill with whole cubes, so their formulas are derived from the box and the circle. The cone takes one-third of the cylinder with the same base and height, and the sphere is a rounder shape whose volume is 4 pi r cubed over 3.

### Doctrine: the working formulas

- **Rectangle.** Area is length times breadth; perimeter is 2 times (length plus breadth); diagonal is the square root of length squared plus breadth squared.
- **Triangle.** Area is one half of base times perpendicular height. The height is perpendicular to the chosen base, not the slanted side.
- **Trapezium.** With parallel sides a and b and perpendicular height h, area is (a + b) times h divided by 2.
- **Circle.** Area is pi times r squared; circumference is 2 pi r. Diameter is twice the radius.
- **Cuboid and cube.** Volume of a cuboid is l times b times h; its surface is 2(lb + bh + hl). A cube of side a has volume a cubed and surface 6a squared.
- **Cylinder, cone and sphere.** Cylinder volume is pi r squared h. Cone volume is one-third of pi r squared h. Sphere volume is 4 pi r cubed over 3.
- **Scaling.** When every length is multiplied by k, areas are multiplied by k squared and volumes by k cubed.

### Shortcut 1: rectangle, triangle and trapezium

- **Rule.** Use the formula for the figure's area in the stated unit, and check that the height used is perpendicular to the base.
- **Failure condition.** Using a slanted side as the height of a triangle, or a non-perpendicular distance in a trapezium, gives an area that is too large. Perimeter is a length, not an area.
- **Worked example.** A rectangle of 8 by 6 has area 48, perimeter 2(8 + 6) = 28 and diagonal sqrt(64 + 36) = 10. A right triangle with legs 6 and 8 has area 6 times 8 divided by 2 = 24, and its hypotenuse is 10. A trapezium with parallel sides 8 and 12 and perpendicular height 5 has area (8 + 12) times 5 divided by 2 = 50.

### Shortcut 2: circles and the value of pi

- **Rule.** A circle of radius r has area pi r squared and circumference 2 pi r. Use pi = 22/7 when the radius is a multiple of 7, because then pi r squared and 2 pi r are whole numbers. Otherwise use the value the stem gives, or leave pi in the answer.
- **Failure condition.** Using 22/7 with a radius that is not a multiple of 7 gives an approximate answer that the stem may not accept. Using the diameter where the radius is needed, or the circumference where the area is asked, gives an answer that is off by a factor of two or more.
- **Worked example.** A circle of radius 7 cm has area 22/7 times 49 = 154 square cm and circumference 2 times 22/7 times 7 = 44 cm. A circle of radius 14 cm has area 22/7 times 196 = 616 square cm, which shows that a radius that is a multiple of 7 keeps the arithmetic exact.

### Shortcut 3: volumes and surfaces of solids

- **Rule.** Use the box formula for a cuboid, a cube's formulas for a cube, and the cylinder, cone and sphere formulas for round solids. A cube whose side is doubled has its surface multiplied by four and its volume by eight.
- **Failure condition.** Using a radius where the stem gives a diameter, or using the cone's volume formula for a cylinder, gives a result that is three times too large or too small. Surfaces are square units and volumes are cubic units.
- **Worked example.** A cylinder with radius 3 cm and height 10 cm has volume pi times 9 times 10 = 90 pi cubic cm, and the cone with the same base and height has 30 pi cubic cm. A sphere of radius 3 cm has volume 4 pi times 27 divided by 3 = 36 pi cubic cm. A cube of side 2 units has surface 6 times 4 = 24 square units, and a cube of side 4 units has surface 96, four times as large.

### Shortcut 4: a closed cube from a rectangular sheet

- **Rule.** A closed cube of side s has surface 6s squared. Equate that surface to the area of the sheet, which uses the whole sheet with no overlap and no spare piece, and solve for s.
- **Failure condition.** Using the volume formula instead of the surface formula, or leaving the sheet's area in the wrong unit, gives a side that is far too large. The square root must be taken after dividing by 6.
- **Worked example.** A sheet of 15 cm by 10 cm has area 150 square cm. A closed cube uses 6s squared = 150, so s squared = 25 and s = 5 cm.

### Shortcut 5: similar solids, volume and density

- **Rule.** For similar solids with a length ratio k, volumes are in the ratio k cubed. Mass equals density times volume, so when the density is the same, mass is in the ratio k cubed too.
- **Failure condition.** Using k squared for volume, which is the rule for areas, or assuming the density changes when the stem keeps the metal the same, gives a wrong ratio.
- **Worked example.** Two cubes of the same metal have sides in the ratio 2 : 1. Their volumes are in the ratio 8 : 1, and so are their masses, because the density is the same for both cubes.

### Shortcut 6: area as probability

- **Rule.** When a point is chosen at random on a target and every part of the target is equally likely to be hit, the probability that the point falls in a region equals the area of the region divided by the area of the whole target.
- **Failure condition.** Dividing the radius of the region by the radius of the target, or the diameters, gives a ratio of lengths, not of areas. The area ratio is the square of the length ratio for concentric circles.
- **Worked example.** A round target has diameter 2 m, so its radius is 1 m. A red circle at its centre has radius 0.3 m. The probability is 0.3 squared divided by 1 squared = 0.09. Using the length ratio 0.3 instead would give 0.3, which is wrong.

### Shortcut 7: a tank that is partly filled by a cylinder

- **Rule.** Compare the two volumes in one unit. The part of the cuboidal tank still holding water is the volume of the tank minus the volume poured into the cylinder, divided by the tank's total volume.
- **Failure condition.** Mixing units, such as cubic metres with litres, or dividing by the cylinder's volume instead of the tank's, gives a fraction that does not describe the tank. A cylinder that holds more than the tank cannot be filled from it.
- **Worked example.** A tank measures 10 m by 4 m by 3 m, so its volume is 120 cubic m. A cylinder of radius 3 m and height 4 m, using pi = 3, takes 108 cubic m. Water left is 120 minus 108 = 12 cubic m, which is 12 divided by 120, one-tenth of the tank.

### The strongest wrong method and the reply

The tempting wrong method is to use the wrong dimension: an area in place of a volume, or a radius in place of a diameter. The reply is that the dimension of the answer names the formula. A square unit asks for an area, a cubic unit asks for a volume, and a circle needs the radius before any formula is applied.

A second wrong method takes the slanted side of a triangle as its height. The reply is that the height must be perpendicular to the base, so the sides of a right triangle are the easiest bases and heights.

### UPSC application

Read the stem for the dimension of the answer first. For area, choose the plane formula and confirm the height is perpendicular. For volume and surface, use the solid's formula and count its faces or its radius. For circles, look for a radius that is a multiple of 7, because that is where 22/7 gives an exact answer. For probability, convert the question into a ratio of areas before any arithmetic.

### Revision points

- An area is in square units, a volume in cubic units, and a length in linear units.
- A triangle's area is one half of base times perpendicular height.
- A trapezium's area is the average of the parallel sides times the perpendicular height.
- A circle's area is pi r squared, and its circumference is 2 pi r.
- Use pi = 22/7 for an exact answer when the radius is a multiple of 7.
- A cube has surface 6a squared and volume a cubed; a cuboid has surface 2(lb + bh + hl).
- A cylinder's volume is pi r squared h; the cone takes one-third of it; a sphere's volume is 4 pi r cubed over 3.
- Doubling a cube's side multiplies its surface by four and its volume by eight.
- A closed cube from a sheet has surface 6s squared equal to the sheet's area.
- Similar solids have volumes in the ratio k cubed; mass follows volume when the density is the same.
- The probability of a region equals its area divided by the whole target's area.
- A tank's remaining fraction is taken in one unit and divided by the tank's own volume.

The solids in this lesson are counted and cut in the next lesson. There the shape's surface and volume are the basis for counting cubes, tiling a floor with tiles, and converting units, so the formulas here are the starting point for those counts.

### Retrieval before the practice

1. A triangle has base 10 cm and perpendicular height 6 cm. What is its area?
   *Answer: 10 times 6 divided by 2 = 30 square cm.*
2. A sphere has radius 3 cm. What is its volume in terms of pi?
   *Answer: 4 pi times 27 divided by 3 = 36 pi cubic cm.*
3. A cube of side 3 units is doubled to side 6 units. By what factor does its volume grow?
   *Answer: eight, because the volume is the cube of the side, and 2 cubed is 8.*

### Practice

**MCQ 20**

A circle has radius 21 cm. Using pi = 22/7, what is its area in square centimetres?

- A. 693
- B. 132
- C. 2772
- D. 1386

**MCQ 20 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Takes half the area, which is the area of a semicircle of the same radius. The full circle has the whole area pi r squared.
- **B — Incorrect:** Reports the circumference, 2 times 22/7 times 21 = 132 cm. The question asks for area, which is a square measure.
- **C — Incorrect:** Multiplies pi by the radius and the diameter, 22/7 times 21 times 42 = 2772. The area uses the radius twice, so the diameter is not part of the formula.
- **D — Correct:** The area is 22/7 times 21 squared = 22/7 times 441 = 1386 square cm. The radius is a multiple of 7, so the value of pi is exact.

**MCQ 21**

A cone has a base radius of 6 cm and a height of 9 cm. What is its volume, in cubic cm, in terms of pi?

- A. 108 pi
- B. 324 pi
- C. 216 pi
- D. 36 pi

**MCQ 21 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The volume is one-third of pi r squared h = pi times 36 times 9 divided by 3 = 108 pi cubic cm.
- **B — Incorrect:** Gives the cylinder with the same base and height, pi times 36 times 9 = 324 pi. The cone takes one-third of that.
- **C — Incorrect:** Uses r cubed in place of r squared and drops both the height and the one-third: pi times 6 cubed = 216 pi. The volume of a cone needs the height and the one-third.
- **D — Incorrect:** Uses only the radius squared, pi times 36 = 36 pi, and leaves out the height.

**MCQ 22**

A round target has diameter 4 m. A circular red region at its centre has radius 0.5 m. An arrow lands at a random point of the target. What is the probability that it lands in the red region?

- A. 0.25
- B. 0.0625
- C. 0.125
- D. 0.03125

**MCQ 22 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Divides the red radius by the target's radius, 0.5 divided by 2 = 1/4 = 0.25. Probability is a ratio of areas, so the lengths must be squared.
- **B — Correct:** The probability is an area ratio. The red area is pi times 0.5 squared and the target area is pi times 2 squared, so the ratio is 0.25 divided by 4 = 1/16 = 0.0625.
- **C — Incorrect:** Divides the red radius by the target's diameter, 0.5 divided by 4 = 1/8 = 0.125. The two lengths must be of the same kind before any ratio is taken.
- **D — Incorrect:** Halves the red area, 0.125 divided by 4 = 1/32 = 0.03125. The red region is a full circle, so its whole area belongs in the numerator.

**MCQ 23**

A cuboidal tank measures 20 m by 10 m by 5 m and is full of water. A cylinder of radius 7 m and height 4 m is filled completely from it, using pi = 22/7. What fraction of the tank's water is left?

- A. 77/125
- B. 48/77
- C. 48/125
- D. 423/500

**MCQ 23 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Reports the share used, 616 divided by 1000, which is 77/125. The question asks for the share left.
- **B — Incorrect:** Divides the water left by the cylinder's volume, 384 divided by 616 = 48/77. The fraction must be taken of the tank's volume.
- **C — Correct:** The cylinder holds 22/7 times 49 times 4 = 616 cubic m. The tank holds 1000 cubic m, so 1000 minus 616 = 384 cubic m remain, which is 384/1000 = 48/125 of the tank.
- **D — Incorrect:** Uses the diameter as the radius, so the cylinder holds 22/7 times 3.5 squared times 4 = 154 cubic m. The radius is 7 m, not 3.5 m.

---

## Lesson 7 - Cube counts, tiling, cuts and units

Progress: Lesson 7 of 7 | Stage: Core | Subtopic: Cube counts, tiling, cuts and units

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: a painted cube as layers

```text
   A 4 x 4 x 4 cube, all six outer faces painted, cut into 64 unit cubes

   layer by how many faces are painted (corners, edges, faces, inside)

   corner cubes ........ 3 painted faces ....  8   (one per corner)
   edge cubes .......... 2 painted faces ....  12 x (4 - 2) = 24
   face-centre cubes ... 1 painted face .....   6 x (4 - 2)^2 = 24
   inner cubes ......... no painted face ....  (4 - 2)^3 = 8
                                             -----
                                              64 = 4^3   (the check)
```

Read the cube as three nested layers. The outer shell carries the paint; the cubes inside it carry none. Each count is a layer of the shell, and the four counts must always add to the total number of unit cubes.

### Plain intuition

A cube cut into small identical cubes has a shell of painted pieces and a core of unpainted pieces. A small cube on a corner touches three painted faces, one on an edge touches two, one on a face touches one, and one inside touches none. The count of each type depends only on how many of the side's unit positions lie in the middle, after removing the outer unit at each end.

Tiling is a different question. It asks whether a rectangle can be covered without gaps and without cutting, which depends on dimensions and on the orientation of each tile. A count of tiles from area alone answers only half the question.

### Doctrine: the formulas

- **Cube of side n, cut into unit cubes, outer faces painted.** Corner cubes 8; cubes with exactly two painted faces 12(n - 2); exactly one painted face 6(n - 2) squared; no painted face (n - 2) cubed. The sum is n cubed, for n at least 2.
- **Cuboid of sides a, b and c, cut into unit cubes.** Corners 8; two painted faces 4(a - 2) + 4(b - 2) + 4(c - 2); one painted face 2[(a - 2)(b - 2) + (b - 2)(c - 2) + (a - 2)(c - 2)]; no painted face (a - 2)(b - 2)(c - 2). The sum is abc.

### Shortcut 1: cube layers (Advanced cube counts)

- **Rule.** Use the four layer formulas for a solid cube with every outer face painted, and check that the four counts add to n cubed.
- **Failure condition.** The formulas fail if some faces are unpainted, if the cube is hollow, or if the cut is not into equal unit cubes. With n = 2 every cube is a corner, so the one-face and no-face counts are zero.
- **Worked example.** For a 4 x 4 x 4 cube the counts are 8, 24, 24 and 8, which add to 64.

**Advanced cube check (drill item 3).** A cube cut into 5 by 5 by 5 unit cubes has 8 corner cubes, 12 times 3 = 36 two-face cubes, 6 times 3 squared = 54 one-face cubes and 3 cubed = 27 unpainted cubes. The four counts add to 125, the check that every cube is counted once.

### Shortcut 2: cuboid face counts

- **Rule.** Apply the cuboid formulas, using a - 2, b - 2 and c - 2 for the interior length along each edge.
- **Failure condition.** Using the full side lengths instead of the reduced ones overcounts the painted faces.
- **Worked example.** A 3 x 4 x 5 cuboid gives 8 corners; 4(1) + 4(2) + 4(3) = 24 two-face cubes; 2[1 x 2 + 2 x 3 + 1 x 3] = 22 one-face cubes; and 1 x 2 x 3 = 6 unpainted cubes. The four counts add to 60, which equals 3 x 4 x 5.

### Shortcut 3: single-orientation tiling (Advanced feasibility) is sufficient, not necessary

- **Rule.** If a rectangle's sides can be split into whole multiples of the tile's sides in one orientation, the tiling exists. If no single orientation fits, a mixed tiling may still exist, so test by splitting the rectangle into strips.
- **Failure condition.** A failed single orientation does not prove that tiling is impossible. The test is sufficient, not necessary.
- **Worked example.** A 5 x 6 rectangle is covered by 2 x 3 tiles. Neither orientation fits, because 5 is not a multiple of 2 or 3 in the required way. Yet split the 5-side as 2 + 3: a 2 x 6 strip takes two tiles laid 2 by 3, and a 3 x 6 strip takes three tiles laid 3 by 2. The total is five tiles, so the mixed tiling exists.

- **Further tiling examples.** A floor of 9 m by 7 m covered by 3 m by 1 m tiles, rotation allowed: with the 3 m side along the 9 m side the count is 3 times 7 = 21 tiles, but the other orientation needs 7 divided by 3 along the 7 m side, which is not whole, so that orientation fails and only the first is feasible. A tile of 20 cm by 10 cm laid in a 1 m by 80 cm rectangle, without cutting: convert to 100 cm by 80 cm first, then 100/20 = 5 and 80/10 = 8, so 40 tiles fit. The conversion must come before the division.

**Advanced tiling check (drill item 8; Advanced Method 6).** A 12 m by 9 m floor is covered by 3 m by 2 m tiles without cutting. In the stated orientation, 3 m along 12 m gives 4 tiles, but 9 divided by 2 is not whole, so the floor is not covered exactly. Rotated, 2 m along 12 m gives 6 and 3 m along 9 m gives 3, so 6 times 3 = 18 tiles fit exactly.

### Shortcut 4: the count of tiles

- **Rule.** When a tiling exists without cutting, the number of tiles is the rectangle's area divided by the tile's area.
- **Failure condition.** Dividing the areas is wrong when no exact tiling exists, and wrong when the stem forbids rotation but the arrangement needs it.
- **Worked example.** A 5 x 6 rectangle needs 30 / 6 = 5 tiles of size 2 by 3.

### Shortcut 5: units and conversions

- **Rule.** Convert every quantity to one unit before calculating. Speed in km/h becomes m/s by multiplying by 5/18. One cubic metre equals 1000 litres; one litre equals 1000 cubic centimetres, which is 1000 millilitres.
- **Failure condition.** Forgetting to convert, or using the factor the wrong way round, gives an answer off by a factor of about 3.6 for speeds and by 1000 for volumes.
- **Worked example.** A speed of 72 km/h is 72 x 5/18 = 20 m/s. A tank of 2 cubic metres holds 2000 litres, or 2 000 000 millilitres.

### Shortcut 6: gaps between posts

- **Rule.** Along a straight line with equal spacing, the number of gaps is one less than the number of posts. Around a closed loop, the number of gaps equals the number of posts.
- **Failure condition.** Using the number of posts as the number of gaps adds one gap too many.
- **Worked example.** Eleven posts along a straight fence have ten gaps. If each gap is 4 m, the fence from the first post to the last is 40 m.

### Shortcut 7: fixed perimeter and maximum area

- **Rule.** When the two sides of a rectangle have a fixed sum, the area is greatest when the sides are equal, which is a square.
- **Failure condition.** The rule fails when one side is fixed. Then the best rectangle uses the fixed side and the other side is chosen as the free variable.
- **Worked example.** With a perimeter of 40 m, the sides add to 20 m. The area is largest at 10 by 10, which is 100 square metres. If one side is fixed at 12 m, the other is 8 m and the area is 96 square metres.

### Shortcut 8: pieces made by cuts

- **Rule.** Cuts made in three perpendicular directions, with a, b and c cuts, divide a block into (a + 1)(b + 1)(c + 1) pieces. The least number of cuts for a given count of pieces comes from factorising that count into three factors, one more than the cuts in each direction, as close together as possible.
- **Failure condition.** The product counts pieces, and the pieces are identical only when the cuts in each direction are equally spaced. Plane cuts that are not all in three perpendicular directions do not follow the product. Planes in general position divide space into at most 1 + n + n(n - 1)/2 + n(n - 1)(n - 2)/6 pieces, so three planes give at most 8 and four give at most 15.
- **Worked example.** A block cut once in one direction, twice in a second and once in a third gives 2 x 3 x 2 = 12 pieces. For 24 identical pieces, the factors 2, 3 and 4 need 1 + 2 + 3 = 6 cuts, fewer than any other factorisation.

### Shortcut 9: the strip extremes of a tiling

- **Rule.** Tiles of width equal to the strip's width lie end to end along the length. If the strip has length L and the tiles have lengths l1, l2 and so on, the number of each tile is a whole number satisfying the sum of lengths equal to L. List every whole-number solution, count the tiles in each, and take the largest and the smallest counts.
- **Failure condition.** Taking the largest tile for the maximum and the smallest for the minimum does not work when the lengths do not fit exactly. A solution must use whole tiles and cover the length exactly, with no overlap and no gap.
- **Worked example.** A strip 3 units wide and 20 units long is covered by tiles 3 by 2 and 3 by 5, laid along its length. The solutions of 2a + 5b = 20 are (a, b) = (10, 0), (5, 2) and (0, 4). The tile counts are 10, 7 and 4. The maximum count is 10 and the minimum is 4, so the difference is 6. With three tile lengths the same listing runs over three counts: fix the number of the longest tiles, solve the remaining length for the other two sizes, and record the total number of tiles for every solution.
- **Three tile sizes (original example).** A strip 15 units long is covered exactly by tiles of length 2, 3 and 5, laid along the strip. The solutions of 2a + 3b + 5c = 15 are (a, b, c) = (0, 0, 3), (0, 5, 0), (1, 1, 2), (2, 2, 1), (3, 3, 0), (5, 0, 1) and (6, 1, 0). Their totals are 3, 5, 4, 5, 6, 6 and 7 tiles. The maximum is 7 and the minimum is 3, so the difference is 4. The method for two sizes extends to three: fix the number of one size, solve the remaining length for the other two, and total each solution.

### Shortcut 10: the most whole tiles on a floor

- **Rule.** Two bounds decide the answer. The area bound is the floor's area divided by the tile's area, rounded down, and it is reached only if a real arrangement exists. The single-orientation count is the floor's sides divided by the tile's sides in one orientation, rounded down for each side, multiplied together. The maximum is found by splitting the floor into strips, counting the whole tiles in each strip in its best orientation, and comparing the splits.
- **Failure condition.** The area bound is not always reached, because the tiles cannot always fit, and a single orientation may leave large gaps. Counting the leftover area as tiles is wrong.
- **Worked example.** A 5 by 3 floor is covered by 2 by 1 tiles. The area bound is 15 divided by 2 = 7.5, so at most 7 tiles fit. The single orientation with the 2 along the 5 side gives (5 divided by 2, rounded down) times 3 = 6 tiles, and the other orientation gives 5 tiles. Seven tiles are possible: a 3 by 4 part holds 6 tiles, laid 2 along the 4 side, and a 3 by 1 column holds one more tile, with one unit cell left over.

### Shortcut 11: equal squares and equal triangles from a rectangle

- **Rule.** Squares of equal size can tile a rectangle only if their side divides both sides of the rectangle. A rectangle is split into equal triangles by diagonals of equal sub-rectangles, and each triangle has area one half of the base times the height of its sub-rectangle.
- **Failure condition.** Dividing the area by the number of pieces does not prove that equal pieces can be cut. The area test is necessary, but the arrangement is needed too.
- **Worked example.** A rectangle of 12 cm by 4 cm can be cut into three squares of side 4 cm, because 4 divides both 12 and 4. It cannot be cut into four equal squares, because their side would have to divide both 12 and 4 and make four squares, which no such side does. Each 4 cm square cut along a diagonal gives two triangles of area 8 square cm, so the rectangle splits into six equal triangles of that area.

### Shortcut 12: a time in units of x

- **Rule.** A quantity written as x of each unit is a linear expression in x. Its coefficient is the sum of each unit's size in the smallest unit, so x hours, x minutes and x seconds give the coefficient 3600 + 60 + 1 = 3661 seconds per x.
- **Failure condition.** Adding the numbers of the units (x plus x plus x) or using the same conversion for each unit gives the wrong coefficient. Each unit needs its own factor.
- **Worked example.** The total seconds in x hours, x minutes and x seconds is 3600x + 60x + x = 3661x. The coefficient of x is 3661, and for x = 2 the total is 7322 seconds.

### The strongest wrong method and the reply

The tempting wrong method for tiling is to check the single orientation the stem draws and call the whole question settled. The reply is that the stem may allow rotation, and a mixed arrangement may succeed where neither orientation alone does. The converse error is equally dangerous: a quotient of areas is not a count when the sides cannot be fitted. The reply is to test the dimensions before dividing.

A second wrong method takes the number of posts as the number of gaps. The reply is that a straight line has one gap fewer than its posts, and a loop has the same number.

### UPSC application

Cube items usually ask for one of the four counts, so compute n and then choose the layer formula the stem asks for, checking the total. Tiling items ask whether something is possible, how many tiles are needed, or the maximum number that fits; test the dimensions and the orientation rule the stem allows. Unit items reward a conversion done first and a sense check afterwards. Fixed-perimeter items ask for the largest or smallest area, and the square is the answer only when the sides are free.

### Revision points

- A painted n-cube has 8 corners, 12(n - 2) two-face cubes, 6(n - 2) squared one-face cubes and (n - 2) cubed unpainted cubes.
- The four counts for an n-cube always add to n cubed.
- For a cuboid, use a - 2, b - 2 and c - 2 for the interior edge lengths.
- A single orientation that fits proves a tiling; a failed orientation proves nothing.
- A tiling count is the area divided by the tile area only when the tiling exists.
- Speed in km/h becomes m/s by multiplying by 5/18.
- One cubic metre is 1000 litres, and one litre is 1000 millilitres.
- Posts on a straight line have one gap fewer; a closed loop has equal posts and gaps.
- With a fixed sum of sides, the area is largest at the square, unless one side is fixed.
- Trapezium area is the average of the parallel sides times the height; cone volume is one-third of the cylinder.
- Cuts in three perpendicular directions give (a + 1)(b + 1)(c + 1) pieces; the least cuts for a count come from a factorisation.
- A strip's tile counts come from the integer solutions of the length equation.
- A floor's area bound is reached only when a real arrangement exists.
- Equal squares tile a rectangle only if their side divides both sides; equal triangles need the area test and a construction.
- A quantity given in units of x has the coefficient equal to the sum of the unit sizes in seconds.

This is the last of the seven lessons on the rate, motion, time and geometry family. Each lesson has built one habit: name the fixed quantity, check the condition under which a shortcut holds, and verify the answer by a second route. The practice that follows applies those habits to the mixed items that appear in the cumulative set.

### Retrieval before the practice

1. How many unit cubes in a 5 x 5 x 5 solid painted cube have no painted face?
   *Answer: (5 - 2) cubed = 27.*
2. A rectangle is 3 by 4 metres and the tile is 1 by 3 metres. Can it be tiled without cutting, and how many tiles are needed?
   *Answer: yes. Lay each tile with its 3-metre side across the 3-metre width, one tile per 1-metre row. Four rows give 4 tiles, which matches the area 12 divided by the tile area 3.*
3. A fence has 6 posts on a straight line, spaced 5 m apart. How long is the fence?
   *Answer: five gaps of 5 m, so 25 m.*

### Practice

**MCQ 24**

A strip 22 units long is to be covered exactly, without cutting, by tiles of length 4 units and tiles of length 5 units, laid end to end along the strip. What is the least number of tiles that can cover the strip?

- A. 4
- B. 6
- C. 22
- D. 5

**MCQ 24 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Divides the length by the longer tile, 22 divided by 5, rounded down to 4. Four tiles cover at most 20 units, so four cannot cover the strip exactly.
- **B — Incorrect:** Divides the length by the shorter tile, 22 divided by 4, rounded up to 6. Six tiles of length 4 would cover 24 units, which is more than the strip, so they cannot be laid exactly.
- **C — Incorrect:** Counts one tile for each unit of length. Tiles are longer than one unit, so the count is far smaller than the length.
- **D — Correct:** The exact covers are the solutions in whole numbers of 4a + 5b = 22. The only solution is a = 3 and b = 2, which is 3 + 2 = 5 tiles. No other pair works: b must be 2 more than a multiple of 4, and 5 times 6 is already more than 22.


**MCQ 25**

A rectangular floor 7 metres by 3 metres is covered by tiles 2 metres by 1 metre, laid without cutting or overlap. What is the largest number of whole tiles that can be laid?

- A. 10
- B. 9
- C. 7
- D. 8

**MCQ 25 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The area bound is 21/2 = 10.5, so at most 10 tiles fit. Ten are possible: a 3 by 6 part holds 9 tiles with 2 metres along the 6 metre side, and a 3 by 1 column holds one more tile across its width.
- **B — Incorrect:** Uses the single orientation with the 2 metre side along the 7 metre side: (7 divided by 2, rounded down) times 3 = 9 tiles. A mixed arrangement does better.
- **C — Incorrect:** Uses the other single orientation: 7 times (3 divided by 2, rounded down) = 7 tiles.
- **D — Incorrect:** Takes the 9 tiles of the single orientation and removes one for the leftover strip, which is wrong: that strip can hold a tile.

**MCQ 26**

A cuboid of sides 4, 5 and 6 units is painted on all six outer faces and cut into unit cubes. How many unit cubes have exactly one painted face?

- A. 36
- B. 52
- C. 24
- D. 60

**MCQ 26 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Gives the two-face count, 4 times (2 + 3 + 4) = 36, which counts the cubes on edges.
- **B — Correct:** The one-face count is 2 times [(4 - 2)(5 - 2) + (5 - 2)(6 - 2) + (4 - 2)(6 - 2)] = 2 times (6 + 12 + 8) = 52.
- **C — Incorrect:** Gives the unpainted count, (2)(3)(4) = 24, which lies inside the block.
- **D — Incorrect:** Takes half of the 120 unit cubes, which is not a painted-face count.

**MCQ 27**

A floor 10 metres by 6 metres is covered by tiles 4 metres by 1 metre. The tiles may not be rotated, and none may be cut. What is the largest number of whole tiles that can be laid?

- A. 15
- B. 10
- C. 12
- D. 16

**MCQ 27 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Gives the area bound, 60 divided by 4 = 15. A bound is not reached when the tiles do not fit exactly.
- **B — Incorrect:** Counts the tiles as if they were rotated: 10 divided by 1 = 10 along the 10 m side, and 6 divided by 4 gives one tile across. The stem forbids rotation, so this arrangement is not allowed.
- **C — Correct:** With the 4 metre side along the 10 metre side, 10 divided by 4 gives 2 tiles across, and the 6 metre side gives 6 rows of 1 metre. The count is 2 times 6 = 12.
- **D — Incorrect:** Rounds the 6 metre side up to 8 metres, then counts 2 times 8 = 16 tiles, which covers floor that does not exist.

---

# VERIFIED PYQ LINKAGE AND ANSWER APPROACHES

This section links every Prelims CSAT question from 2013 to 2026 that belongs to rates, motion, time and geometry. Each linked question is taught in a lesson part of this file, and each link opens the question-level entry of its year file. Items whose method belongs to a neighbouring topic are shown inline under their year, each marked with its neighbouring topic. Nothing here reproduces a question, an option, a letter or a worked solution, and no answer key appears in this section.

Three points govern how to use the list.

1. **Type before you calculate.** The label in bold names the family of the question as the stem presents it. Identify the family first; it tells you which lesson part applies.
2. **Demand and format.** The format says whether the item is a single answer, a statement set or a diagram choice. A statement set needs each statement tested on its own before the codes are read.
3. **The approach is a route, not a result.** It names the test to run. Run the test on the numbers in the stem and check the result by a second route.

The 2026 paper is provisional, so its entries record the method only and make no claim about any option. The 2018 entries are typed from the verified booklet transcription in the solved paper library; their approaches name the method the stem tests.

## 2013

- [Q35](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q035) — **R2 Same-direction overtaking on one road**. Format: single answer. Demand and approach: Relative speed is the difference of the speeds; time is the gap divided by that difference. Teaching home: Lesson 3, Shortcut 1.
- [Q36](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q036) — **S1 Two-part journey with an unknown original speed**. Format: single answer. Demand and approach: Write each leg's time as distance over speed, set the total time, and solve after clearing denominators. Teaching home: Lesson 2, Shortcut 9.
- [Q47](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q047) — **W3 Men and days in inverse relation (diagram choice)**. Format: diagram choice. Demand and approach: Find the graph whose product of workers and days is constant; this is a ratio-and-proportion relation. Teaching home: Lesson 1, Shortcut 8.
- [Q49](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q049) — **S1 Maximum average speed from a payment and fuel table**. Format: single answer. Demand and approach: Average speed is total distance over total time for each car; per-trip rates are not averaged. Teaching home: Lesson 2, Shortcut 1.
- [Q64](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q064) — **E1 Food supply after a change in the number of people**. Format: single answer. Demand and approach: Track the remaining amount at the moment of change, then divide by the new daily use. Teaching home: Lesson 1, Shortcut 5.
- [Q65](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q065) — **E1 Daily petrol use raised by a percentage (tank lasts)**. Format: single answer. Demand and approach: Compute the new daily use as a multiple of the old; divide the full tank by it. Teaching home: Lesson 1, Shortcut 8.
- [Q66](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q066) — **S2 Walking and driving times over one distance**. Format: single answer. Demand and approach: Call the one-way distance x; write each time as x over speed; solve from the two totals. Teaching home: Lesson 3, Shortcut 7.

## 2014

- [Q10](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q010) — **Z1 Six villages placed by directions and distances**. Format: single answer. Demand and approach: Place the points on a grid from the stated offsets, then test which three are collinear. Teaching home: Lesson 5, Shortcut 9.
- [Q12](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q012) — **K1 Hands lie one above the other again after a start time**. Format: single answer. Demand and approach: The relative hand speed is 5.5 degrees per minute; find the first later overlap within the window. Teaching home: Lesson 4, Shortcut 1.
- [Q50](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q050) — **S2 Early and late arrival at two walking speeds**. Format: single answer. Demand and approach: The difference of arrival times equals distance times the difference of the reciprocal speeds; solve for distance. Teaching home: Lesson 3, Shortcut 8.
- [Q68](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q068) — **G1 Shortest distance from two perpendicular displacements**. Format: single answer. Demand and approach: Net displacement from perpendicular legs uses the right-angle length rule. Teaching home: Lesson 5, Shortcut 1.
- [Q69](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q069) — **R1 Two cars approaching from two places with a common start time**. Format: single answer. Demand and approach: Gap divided by the summed speeds gives the travel time; add it to the start time. Teaching home: Lesson 3, Shortcut 1.
- [Q76](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q076) — **L1 Weekday of a date counted from a reference day**. Format: single answer. Demand and approach: Weekday arithmetic modulo seven from a stated reference day. The method belongs to a neighbouring topic; not taught in this file.

## 2015

- [Q33](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q033) — **D1 Two walkers turning left and right after equal legs**. Format: single answer. Demand and approach: Track each walker's net position leg by leg, then test each statement against the positions. The method belongs to a neighbouring topic; not taught in this file.
- [Q34](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q034) — **S2 Race speed ratio from the gap at a finish**. Format: single answer. Demand and approach: The speed ratio is the race length over the distance covered by the trailing runner when the leader finishes. Teaching home: Lesson 3, Shortcut 6.
- [Q53](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q053) — **W1 Two pipes filling one tank together**. Format: single answer. Demand and approach: Add the two filling rates and invert the sum. The method belongs to a neighbouring topic; not taught in this file.
- [Q68](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q068) — **K1 Minute hand ahead of the hour hand by a fixed amount**. Format: single answer. Demand and approach: Use the relative rate of 5.5 degrees per minute; solve for the minute within the hour. Teaching home: Lesson 4, Shortcut 1.
- [Q71](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q071) — **S1 Round-trip average speed on two different speeds**. Format: single answer. Demand and approach: Total distance over total time; the two legs have equal distances, so the harmonic form applies. Teaching home: Lesson 2, Shortcut 2.
- [Q76](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q076) — **G2 Lines perpendicular and parallel in a plane**. Format: single answer. Demand and approach: Apply the parallel and perpendicular rules to each line pair; reject any pair the rules do not support. Teaching home: Lesson 5, Shortcut 3.

## 2016

- [Q9](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q009) — **D1 Grid route and a second route back to the start**. Format: single answer. Demand and approach: After the first legs, the return must cancel the net displacement; check each option's net. Teaching home: Lesson 2, Shortcut 4.
- [Q38](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q038) — **X1 Shuttle trains for a round trip**. Format: single answer. Demand and approach: Round-trip time divided by the departure interval, rounded up. Teaching home: Lesson 2, Shortcut 7.
- [Q39](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q039) — **M1 Closed cube made from a rectangular sheet**. Format: single answer. Demand and approach: The surface of a cube of side s is 6s squared; equate it to the sheet's area. Teaching home: Lesson 6, Shortcut 4.
- [Q49](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q049) — **G1 Hill climb in two diagonal directions**. Format: single answer. Demand and approach: The two legs meet at a right angle; apply the right-angle length rule. Teaching home: Lesson 5, Shortcut 1.
- [Q50](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q050) — **M1 Rectangle area under a fixed sum of sides**. Format: single answer. Demand and approach: For a fixed sum of sides the area is largest when the sides are equal; test the bound. The method belongs to a neighbouring topic; not taught in this file.
- [Q57](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q057) — **G1 Broken tree trunk whose top touches the ground**. Format: single answer. Demand and approach: The broken part, the ground distance and the stump form a right triangle; apply Pythagoras. Teaching home: Lesson 5, Shortcut 1.
- [Q58](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q058) — **D1 Net walk after four legs**. Format: single answer. Demand and approach: Find the net east-west and north-south totals, then the straight-line length from them. Teaching home: Lesson 2, Shortcut 4.
- [Q59](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q059) — **Q1 Small cubes with one painted face after slicing a painted cube**. Format: single answer. Demand and approach: Count the face-centre cubes of the reduced cube with the layer formula. Teaching home: Lesson 7, Shortcut 1.
- [Q73](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q073) — **M1 Water left after filling a cylinder from a rectangular tank**. Format: single answer. Demand and approach: Compare the two volumes in one unit and subtract the volume used. Teaching home: Lesson 6, Shortcut 7.
- [Q75](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q075) — **C1 Meetings of two walkers on a circular park inside a time window**. Format: single answer. Demand and approach: The meeting interval comes from the relative rate; count the meetings that fall inside the window. Teaching home: Lesson 3, Shortcut 4.
- [Q78](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q078) — **D1 Apple-collection race: total path of repeated out-and-back trips**. Format: single answer. Demand and approach: Each trip is out and back, so add every leg's length; the net position is not the answer. The method belongs to a neighbouring topic; not taught in this file.
- [Q79](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q079) — **P1 Archery target: probability of a red-region hit**. Format: single answer. Demand and approach: The probability is the area of the red region over the area of the target. Teaching home: Lesson 6, Shortcut 6.

## 2017

- [Q11](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q011) — **L1 Minimum working days in a month with fixed holidays**. Format: single answer. Demand and approach: Count the holidays in each possible month structure and take the smallest working count. The method belongs to a neighbouring topic; not taught in this file.
- [Q16](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q016) — **N1 Three pillars climbed with slips; shortest pillar**. Format: single answer. Demand and approach: Use the final-step rule: the height after the nights already passed, plus the climb of the final day, must reach the pillar height. Teaching home: Lesson 1, Shortcut 4.
- [Q31](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q031) — **K2 Two watches gaining and losing; identical again**. Format: single answer. Demand and approach: Find the relative drift per day; the watches agree again when the relative drift makes one full dial. Teaching home: Lesson 4, Shortcut 4.
- [Q33](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q033) — **K2 Clock striking once, twice and so on; time for a span of strikes**. Format: single answer. Demand and approach: Count the intervals between strikes in each run; a run of n strikes has n minus one intervals. Teaching home: Lesson 4, Shortcut 9.
- [Q39](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q039) — **R2 Freight and express trains on one route: meeting point**. Format: single answer. Demand and approach: Start the faster train with the head start in distance; time to close the gap; distance from the origin is speed times time. Teaching home: Lesson 3, Shortcut 1.
- [Q58](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q058) — **Q1 Unpainted small cubes after slicing a painted cube**. Format: single answer. Demand and approach: The inner unpainted cubes of an n-cube are (n minus two) cubed. Teaching home: Lesson 7, Shortcut 1.
- [Q75](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q075) — **G1 Distance of a fly from a ceiling in a room corner**. Format: single answer. Demand and approach: Three perpendicular distances from the corner; the three-dimensional right-angle rule gives the distance from the corner. Teaching home: Lesson 5, Shortcut 2.

## 2018

- [Q5](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q05) — **Y1 Velocity-time distance ratio**. Format: single answer. Demand and approach: Distance is the area under the velocity-time graph over the interval; compare the two areas with the same time axis. Teaching home: Lesson 2, Shortcut 8.
- [Q6](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q06) — **R3 Train crossing time**. Format: single answer. Demand and approach: The train covers its own length past a point; divide its length by its speed in metres per second. Teaching home: Lesson 2, Shortcut 5.
- [Q35](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q35) — **Q1 Painted-cube face geometry**. Format: single answer. Demand and approach: Count the cubes with exactly two painted faces of an n-cube: 12 times (n minus 2), with the cube side from the stem. Teaching home: Lesson 7, Shortcut 1.
- [Q40](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q40) — **C1 Circular-track speed ratio**. Format: single answer. Demand and approach: Position on a circle is an angle from the start; the ratio of speeds is the ratio of the angles turned, with the offset subtracted. Teaching home: Lesson 3, Shortcut 10.
- [Q58](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q58) — **G2 Inscribed triangles on a circle**. Format: single answer. Demand and approach: Equilateral triangles inscribed in a circle use points spaced a third of a turn apart; count the starting points that repeat. Teaching home: Lesson 5, Shortcut 11.
- [Q59](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q59) — **L1 Calendar date sequence**. Format: single answer. Demand and approach: Add the constant gap in days to each date, counting 29 February when it lies inside the interval. Teaching home: Lesson 4, Shortcut 12.
- [Q60](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q60) — **G1 Rectangle diagonal geometry**. Format: single answer. Demand and approach: The square side follows from the diagonal of the rectangle of squares; the area is the side squared. Teaching home: Lesson 5, Shortcut 2.

## 2019

- [Q10](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q10) — **Q1 Painted cube with two sizes of pieces and colour pairs**. Format: single answer. Demand and approach: Fix the partition of the big cube into pieces, then count the pieces with exactly one painted face. The method belongs to a neighbouring topic; not taught in this file.
- [Q12](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q12) — **L1 Weekday of the fifth occurrence in two months**. Format: single answer. Demand and approach: Count the weekdays of each month, identify the weekday of the fifth occurrence, then shift to the target date. Teaching home: Lesson 4, Shortcut 8.
- [Q16](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q16) — **S2 Race distance from a progress percentage**. Format: single answer. Demand and approach: Turn the percentage into a fraction; the distance is the known part divided by that fraction. Teaching home: Lesson 3, Shortcut 11.
- [Q30](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q30) — **G1 Two towns in perpendicular directions from a common point**. Format: single answer. Demand and approach: The two distances from the common point are perpendicular legs; apply the right-angle length rule. Teaching home: Lesson 5, Shortcut 1.
- [Q35](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q35) — **L2 Periodic joint swimming on alternate day counts**. Format: single answer. Demand and approach: Least common multiple of the two periods, then the calendar day of the next joint swim. Teaching home: Lesson 4, Shortcut 14.
- [Q36](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q36) — **S2 Race start scaling with three runners**. Format: single answer. Demand and approach: Compose the head-start ratios so that each runner's speed is compared with the same base. Teaching home: Lesson 3, Shortcut 12.
- [Q49](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q49) — **K2 Fast wall clock and the correct time**. Format: single answer. Demand and approach: Gain rate times elapsed time gives the excess; subtract it from the displayed time. Teaching home: Lesson 4, Shortcut 4.
- [Q57](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q57) — **D1 Walk with left and right turns: shortest distance between two offices**. Format: single answer. Demand and approach: Sum the signed legs along each axis to get the net position; the straight-line length follows from the net. Teaching home: Lesson 2, Shortcut 4.
- [Q59](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q59) — **L1 Year that has the same calendar as a given year**. Format: single answer. Demand and approach: Match the leap pattern and the weekday shift across the span of years. Teaching home: Lesson 4, Shortcut 11.

## 2020

- [Q20](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q20) — **L1 Weekday relation between two dates in a year**. Format: single answer. Demand and approach: Count the odd days between the dates and test the leap-year condition for the span. Teaching home: Lesson 4, Shortcut 5.
- [Q31](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q31) — **Z1 Direction after a walk with turns**. Format: single answer. Demand and approach: Add the legs with their signs to get the east-west and north-south components; the direction follows from those components. Teaching home: Lesson 2, Shortcut 10.
- [Q38](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q38) — **M1 Volume and mass of two similar metal cubes**. Format: single answer. Demand and approach: Volume scales with the cube of the side ratio; density is mass over volume. Teaching home: Lesson 6, Shortcut 5.
- [Q71](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q71) — **W1 Combined work fraction of two workers over days**. Format: single answer. Demand and approach: Rates add; the fraction done is the combined rate times the days. Teaching home: Lesson 1, Shortcut 1.
- [Q72](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q72) — **S1 Multi-leg average speed over legs of changing speed**. Format: single answer. Demand and approach: Equal distances on each leg call for the harmonic form; otherwise use total over total. Teaching home: Lesson 2, Shortcut 2.
- [Q73](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q73) — **G2 Square and circle intersection statements**. Format: single answer. Demand and approach: Count the points a circle can share with the sides of a square, at most two per side; test each statement against the minimum and the maximum of that count. Teaching home: Lesson 5, Shortcut 8.
- [Q74](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q74) — **B1 Upstream and downstream time ratio of a boat**. Format: single answer. Demand and approach: Downstream speed is b plus s and upstream is b minus s; equal distances give the ratio of times. Teaching home: Lesson 2, Shortcut 6.
- [Q80](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q80) — **N1 Frog climbing a well with slips**. Format: single answer. Demand and approach: Use the final-step rule: the top is reached on the first day the climb alone reaches it. Teaching home: Lesson 1, Shortcut 4.

## 2021

- [Q16](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q16) — **N1 Ball bounces to a stopping height**. Format: single answer. Demand and approach: Each bounce keeps a fixed fraction of the previous height; count bounces until the threshold stops them. Teaching home: Lesson 1, Shortcut 6.
- [Q18](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q18) — **D1 Direction and distance path to a bank**. Format: single answer. Demand and approach: Net displacement from the turning legs; the shortest distance is the straight line between the two points. Teaching home: Lesson 2, Shortcut 4.
- [Q20](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q20) — **D1 Direction from the start after north, south and east legs**. Format: single answer. Demand and approach: Find the net components and compare the angle with the 45-degree line. Teaching home: Lesson 2, Shortcut 10.
- [Q29](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q29) — **R1 Two walkers moving towards each other with hourly speeds**. Format: statement format. Demand and approach: Cumulative distance per hour; they meet when the two totals reach the separation. Test each statement. Teaching home: Lesson 3, Shortcut 1.
- [Q48](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q48) — **L1 Weekday of a distant date**. Format: single answer. Demand and approach: Weekday shift modulo seven across the span, with the leap-year test. Teaching home: Lesson 4, Shortcut 5.
- [Q57](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q57) — **K1 Clock angle equal to a straight line in a time window**. Format: single answer. Demand and approach: Use the angle formula and test which time in the window gives 180 degrees. Teaching home: Lesson 4, Shortcut 1.
- [Q63](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q63) — **A1 Points on a straight line in a given ratio**. Format: single answer. Demand and approach: List the orders of the three points on the line; each order fixes one value of the ratio, and the number of values is counted. Teaching home: Lesson 5, Shortcut 10.
- [Q68](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q68) — **M2 Volume of a cubical vessel of water in millilitres**. Format: single answer. Demand and approach: One cubic metre is 1000 litres and one litre is 1000 millilitres. Teaching home: Lesson 7, Shortcut 5.
- [Q75](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q75) — **L2 Weekday of the next joint visit of three periodic visitors**. Format: single answer. Demand and approach: Least common multiple of the three periods, then the weekday shift. Teaching home: Lesson 4, Shortcut 7.
- [Q80](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q80) — **W1 Work remaining after a quantity increase**. Format: single answer. Demand and approach: Remaining fraction times the new total, divided by the rate. Teaching home: Lesson 1, Shortcut 5.

## 2022

- [Q6](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q06) — **D1 Two friends' paths after turns: distance apart**. Format: single answer. Demand and approach: Net displacement of each runner; combine the perpendicular components by the right-angle rule. Teaching home: Lesson 2, Shortcut 4.
- [Q7](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q07) — **L1 Sunday dates in a month of a distant year**. Format: single answer. Demand and approach: Weekday of the first day of the month, then add multiples of seven. Teaching home: Lesson 4, Shortcut 5.
- [Q15](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q15) — **C1 Overtakes on a circular course with a speed ratio**. Format: single answer. Demand and approach: Relative speed and laps gained; count the overtakes inside the race distance. Teaching home: Lesson 3, Shortcut 2.
- [Q26](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q26) — **M2 Distance between five consecutive equally spaced plants on a road**. Format: single answer. Demand and approach: Gaps equal plants minus one; convert the road length to metres first. The method belongs to a neighbouring topic; not taught in this file.
- [Q35](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q35) — **M2 Total seconds in weeks, days, hours, minutes and seconds**. Format: single answer. Demand and approach: Convert each unit to seconds and collect the coefficient of x. Teaching home: Lesson 7, Shortcut 12.
- [Q46](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q46) — **K2 Clock route time against a village clock**. Format: single answer. Demand and approach: Travel time from the two clock readings; the offset is the difference between the clocks. Teaching home: Lesson 4, Shortcut 4.
- [Q56](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q56) — **G2 Right-angled triangles from equally spaced points on a circle**. Format: single answer. Demand and approach: A diameter used as one side fixes the right angle; count the third points for each diameter. The method belongs to a neighbouring topic; not taught in this file.
- [Q57](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q57) — **W1 Work-rate comparison of men and women**. Format: single answer. Demand and approach: Give each person a rate in one common unit; compare the total work done. Teaching home: Lesson 1, Shortcut 1.
- [Q59](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q59) — **T1 Cutting a rectangle into squares and equal-area triangles: statements**. Format: statement format. Demand and approach: Check the side divisibility and the area condition for each statement. Teaching home: Lesson 7, Shortcut 11.
- [Q68](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q68) — **K1 Hand coincidences within a minute: statements**. Format: statement format. Demand and approach: Coincidence times are fixed by the relative rate; test whether each interval contains one. Teaching home: Lesson 4, Shortcut 2.

## 2023

- [Q18](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q18) — **Q1 Interior cubes of a cubical block**. Format: single answer. Demand and approach: Interior cubes are (n minus two) cubed for an n-cube block. The method belongs to a neighbouring topic; not taught in this file.
- [Q20](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q20) — **W2 Cyclic schedule of three workers: statements**. Format: statement format. Demand and approach: Find the rate of one full cycle and test whether the job ends on the stated day or after the stated days. Teaching home: Lesson 1, Shortcut 3.
- [Q30](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q30) — **G2 Triangles from points on the sides of a square**. Format: single answer. Demand and approach: A counting item on boundary points; the method is taught outside this session. The method belongs to a neighbouring topic; not taught in this file.
- [Q49](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q49) — **L1 Weekday after a very large number of days**. Format: single answer. Demand and approach: Reduce the base modulo seven: 10 leaves residue 3, whose powers repeat with period 6, so reduce the exponent modulo 6 and then shift the weekday. Teaching home: Lesson 4, Shortcut 13.
- [Q50](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q50) — **L2 Simultaneous signal changes from periodic cycles**. Format: single answer. Demand and approach: Least common multiple of the full cycle lengths, then the clock time of that common instant. Teaching home: Lesson 4, Shortcut 14.
- [Q67](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q67) — **T1 Maximum number of rectangular tiles on a floor**. Format: single answer. Demand and approach: Test both single orientations and the area bound, then search mixed splits of the floor into strips; keep whole tiles only and compare the totals. Teaching home: Lesson 7, Shortcut 10.
- [Q79](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q79) — **Q1 Painted cuboid with colour pairs: statements**. Format: statement format. Demand and approach: Count cubes with two faces of named colours and test each statement against those counts. The method belongs to a neighbouring topic; not taught in this file.

## 2024

- [Q5](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q05) — **Least cuts for an identical-piece count**. Format: single answer. Demand and approach: Pieces equal the product of (cuts in each direction plus one); factorise 64 into three factors. Teaching home: Lesson 7, Shortcut 8.
- [Q7](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q07) — **W1 Men needed for a changed completion time**. Format: single answer. Demand and approach: Men times days is constant; the percentage change follows from the ratio of the days. Teaching home: Lesson 1, Shortcut 8.
- [Q8](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q08) — **W2 Alternating three-worker schedule, hour by hour**. Format: single answer. Demand and approach: Simulate the hourly rule, keeping each worker out for one hour after working. Teaching home: Lesson 1, Shortcut 7.
- [Q30](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q30) — **M2 Metric-unit conversion statements**. Format: statement format. Demand and approach: Check each conversion against the metric definitions. Teaching home: Lesson 7, Shortcut 5.
- [Q37](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q37) — **K1 Hand coincidences between two times on one day**. Format: single answer. Demand and approach: Coincidence times are fixed by the relative rate; count those inside the window. Teaching home: Lesson 4, Shortcut 2.
- [Q38](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q38) — **L1 Year with the same calendar as a given year**. Format: single answer. Demand and approach: Check the leap pattern and the weekday shift across the years. Teaching home: Lesson 4, Shortcut 11.
- [Q40](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q40) — **K1 Angle between the hands at a given time**. Format: single answer. Demand and approach: Use the clock angle formula with the hour taken on a twelve-hour dial. Teaching home: Lesson 4, Shortcut 1.

## 2025

- [Q9](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q09) — **RT Run rate and overs with percentage changes**. Format: single answer. Demand and approach: Runs equal rate times overs; set up the equal-score equation and solve. Teaching home: Lesson 1, run-rate paragraph.
- [Q15](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q15) — **Least cuts for an equal-piece count: statements**. Format: statement format. Demand and approach: Factorise 60 into three factors, each one more than the cuts in that direction; choose the factorisation with the fewest cuts and test each statement against it. Teaching home: Lesson 7, Shortcuts 1 and 8.
- [Q17](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q17) — **E1 Fuel cost and mileage: distance adjustment**. Format: single answer. Demand and approach: Cost per kilometre is price over mileage; keep the spending fixed and solve for the distance. The method belongs to a neighbouring topic; not taught in this file.
- [Q37](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q37) — **C1 Encounters of two walkers on a circular track from a common start**. Format: single answer. Demand and approach: Relative laps per hour; count the crossings in the interval. Teaching home: Lesson 3, Shortcut 2.
- [Q39](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q39) — **R2 Tram passing two walkers: length of the tram**. Format: single answer. Demand and approach: Length equals relative speed times passing time for each walker; the two lengths are equal. Teaching home: Lesson 3, Shortcut 13.
- [Q45](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q45) — **W1 Pipes and a cistern with changed numbers and openings**. Format: single answer. Demand and approach: Find the rate of one pipe in each set, then combine the open pipes. Teaching home: Lesson 1, Shortcut 2.
- [Q59](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q59) — **W1 Fractional work rates with three workers who quit**. Format: single answer. Demand and approach: Rate per worker as a fraction of the job per day; the work left after quitting is the remainder. Teaching home: Lesson 1, Shortcut 1.

## 2026

- [Q13](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q13) — **D1 Forward and backward jumps with a net advance**. Format: single answer. Demand and approach: Two equations: the number of jumps and the net advance; solve for the forward count. Teaching home: Lesson 2, Shortcut 4.
- [Q20](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q20) — **R3 Train crossing a person in two directions**. Format: single answer. Demand and approach: Relative speed in each direction; the crossing covers the train's length. Teaching home: Lesson 2, Shortcut 5.
- [Q24](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q24) — **Q2 Pieces after cuts with an identical-pieces condition**. Format: single answer. Demand and approach: Enumerate the possible piece counts for each cut and keep the stated condition. Teaching home: Lesson 7, Shortcut 8.
- [Q37](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q37) — **C1 Runners who change direction on a circular track**. Format: single answer. Demand and approach: Laps completed by each runner before and after the change of direction; count the meetings in each phase and the change once. Teaching home: Lesson 3, Shortcut 15.
- [Q41](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q41) — **R4 Sound and drone timings for an explosion**. Format: single answer. Demand and approach: Subtract the sound travel time from the reception time; add the drone travel time for the second picture. Teaching home: Lesson 3, Shortcut 14.
- [Q50](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q50) — **S1 Two journeys over segments with stated speeds**. Format: single answer. Demand and approach: Segment times for each traveller, then the total time for each; compare the totals. Teaching home: Lesson 2, Shortcut 3.
- [Q56](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q56) — **D1 Turning legs and the minimum distance from the start**. Format: single answer. Demand and approach: Net components along the axes, then the straight-line length; the direction follows from the net. The method belongs to a neighbouring topic; not taught in this file.
- [Q68](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q68) — **T1 Tiling a long strip with three tile sizes**. Format: single answer. Demand and approach: Solve the length equation in whole numbers for the three tile sizes, total the tiles for each solution, and take the extremes of that total. Teaching home: Lesson 7, Shortcut 9.
- [Q69](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q69) — **S1 Train slowed by an accident and a defect: original speed**. Format: single answer. Demand and approach: Write the journey time with the changed speeds as an equation in the original speed. Teaching home: Lesson 2, Shortcut 9.

# CUMULATIVE MCQS

These cumulative items each join methods from different lessons, so that the stem can be answered only by combining them. They are numbered on from the last lesson item. Items 28 to 33 combine methods already practised once in a lesson; items 34 to 39 join families that the lessons do not join on their own. Answer each item before you open its explanation.

**MCQ 28**

*Joins Lesson 6 (sheet and solid) and Lesson 7 (cube counts).*

A rectangular sheet 14 cm by 21 cm is folded into a closed cube, with no overlap and no spare piece. The cube is painted on all six outer faces and cut into unit cubes. How many unit cubes have exactly one painted face?

- A. 60
- B. 125
- C. 25
- D. 150

**MCQ 28 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Gives the two-face count, 12 times (7 - 2) = 60, which counts the cubes on edges.
- **B — Incorrect:** Gives the unpainted count, (7 - 2) cubed = 125, which lies inside the cube.
- **C — Incorrect:** Takes only one face's interior, (7 - 2) squared = 25, and forgets the other five faces.
- **D — Correct:** The sheet area 294 equals 6 times s squared, so s squared is 49 and s = 7. The one-face count is 6 times (7 - 2) squared = 6 times 25 = 150.


**MCQ 29**

*Joins Lesson 2 (net displacement) and Lesson 5 (Pythagoras).*

A walker goes 9 km due east in 2 hours and then 12 km due north in 4 hours. What is the magnitude of the walker's average velocity over the whole walk, in km per hour?

- A. 2 1/2
- B. 3 3/4
- C. 3 1/2
- D. 2

**MCQ 29 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The net displacement is sqrt(9 squared + 12 squared) = 15 km, from the right-angle rule, and the total time is 6 hours. The average velocity is 15/6 = 2.5 km/h.
- **B — Incorrect:** Takes the plain mean of the two leg speeds, (4.5 + 3)/2 = 3.75. The legs take different times, so the plain mean is not an average over the whole walk.
- **C — Incorrect:** Divides the total path, 21 km, by the total time, 6 hours, which gives the average speed. Average velocity uses the net displacement.
- **D — Incorrect:** Divides only the northward leg, 12 km, by the total time. The eastward 9 km also changes the net position, so it must enter the displacement.

**MCQ 30**

*Joins Lesson 3 (head starts) and Lesson 2 (time as distance over speed).*

In a 300 m race, A gives B a head start of 40 m. B runs at a steady 5 m/s, and A and B finish at the same moment. How many seconds does B take to finish the race?

- A. 48
- B. 52
- C. 60
- D. 68

**MCQ 30 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Removes the head start twice, so B runs 240 m at 5 m/s, which gives 48 seconds. The head start is removed once, from the distance that B must run.
- **B — Correct:** B runs 300 - 40 = 260 m at 5 m/s, which takes 52 seconds. A also takes 52 seconds, because both finish together.
- **C — Incorrect:** Ignores the head start and divides the whole 300 m by 5 m/s, which gives 60 seconds. B starts 40 m ahead of the line, so the distance is shorter.
- **D — Incorrect:** Adds the head start to the race, so B runs 340 m, which gives 68 seconds. The head start shortens B's distance; it does not lengthen the race.

**MCQ 31**

*Joins Lesson 1 (alternate-day work) and Lesson 4 (weekday counting).*

Worker A alone finishes a job in 4 days and worker B alone in 6 days. They work on alternate days, with A on day 1 (a Monday), B on day 2, A on day 3, and so on. On which weekday does the job end?

- A. Thursday
- B. Saturday
- C. Friday
- D. Sunday

**MCQ 31 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Stops at the end of day 4, after two full cycles. Those cycles do 5/6 of the job, and the remaining 1/6 is still to be done on day 5.
- **B — Incorrect:** Counts day 6 as the day the job ends. Day 5 is A's day and A finishes the remaining 1/6 within it, so day 6 is not needed.
- **C — Correct:** Two full cycles do 5/6 by the end of day 4. On day 5, A does 1/4 per day, so the last 1/6 takes two-thirds of day 5. Day 5 is a Friday, counting from Monday as day 1.
- **D — Incorrect:** Counts seven days, as if the job were finished at the end of a week. The job needs only the first part of day 5.

**MCQ 32**

*Joins Lesson 5 (face diagonal) and Lesson 7 (cube counts).*

A cube has a face diagonal of length sqrt(72) units. It is painted on all six outer faces and then cut into unit cubes. How many unit cubes have no painted face?

- A. 16
- B. 4
- C. 96
- D. 64

**MCQ 32 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Uses (n - 2) squared, the number of inner cubes on one face. Unpainted cubes fill the whole inner block, not one of its faces.
- **B — Incorrect:** Uses the linear count n - 2 = 4 as the number of unpainted cubes. Unpainted cubes fill a block in three dimensions, so the count is a cube.
- **C — Incorrect:** Reports the one-face count, 6(n - 2) squared = 96. Those cubes carry one paint mark, and they do not have no painted face.
- **D — Correct:** The face diagonal of a cube of side s is s times sqrt(2). So s times sqrt(2) = sqrt(72) gives s = 6. The unpainted cubes number (6 - 2) cubed = 64.

**MCQ 33**

*Joins Lesson 2 (speed) and Lesson 7 (unit conversion).*

A 160 m train runs at 36 km/h and crosses a bridge 240 m long. How many seconds pass from the moment the front of the train reaches the bridge until the rear of the train leaves the bridge?

- A. 40 seconds
- B. 16 seconds
- C. 24 seconds
- D. 11 1/9 seconds

**MCQ 33 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** 36 km/h is 36 times 5/18 = 10 m/s. The distance is 160 + 240 = 400 m, which takes 400/10 = 40 seconds.
- **B — Incorrect:** Uses only the train's length, 160 divided by 10 m/s, which is 16 seconds. The train must also travel the whole length of the bridge.
- **C — Incorrect:** Uses only the bridge's length, 240 divided by 10 m/s, which is 24 seconds. The train's own length also has to pass the bridge.
- **D — Incorrect:** Uses 36 as metres per second without converting from km/h, giving 400/36 = 11 1/9 seconds. The unit conversion must be done first.

**MCQ 34**

*Joins Lesson 2 (bus frequencies) and Lesson 4 (least common multiple).*

Bus line X leaves a stop every 12 minutes and bus line Y every 18 minutes. Both leave together at 7:00 am. How many times do they leave together after 7:00 am, up to and including 10:00 am?

- A. 6
- B. 5
- C. 10
- D. 15

**MCQ 34 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Counts 7:00 am itself, which is the starting moment and is not counted as a later departure.
- **B — Correct:** The joint departures repeat every LCM(12, 18) = 36 minutes. Within 180 minutes after 7:00 am they leave together at 36, 72, 108, 144 and 180 minutes: five times.
- **C — Incorrect:** Counts every departure of line Y in the window, 180/18 = 10, instead of the joint departures.
- **D — Incorrect:** Counts every departure of line X in the window, 180/12 = 15, instead of the joint departures.

**MCQ 35**

*Joins Lesson 6 (volume) and Lesson 7 (cutting into identical pieces).*

A block 12 cm by 8 cm by 6 cm is cut, with cuts parallel to its faces, into identical cubes of side 2 cm. How many cubes are obtained?

- A. 144
- B. 36
- C. 72
- D. 48

**MCQ 35 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Divides the volume by 4, using the area of a 2 cm square instead of the volume of a 2 cm cube: 144.
- **B — Incorrect:** Divides the volume by 16, treating a 2 cm cube as having the volume of a 4 cm square: 36.
- **C — Correct:** The block's volume is 12 x 8 x 6 = 576 cubic cm, and each 2 cm cube has volume 8 cubic cm. So 576 divided by 8 = 72 cubes. The same answer follows from 6 by 4 by 3 cubes along the three edges.
- **D — Incorrect:** Divides the volume by the edge 12 cm alone: 48 pieces. The cubes must fit in all three directions.

**MCQ 36**

*Joins Lesson 6 (perimeter) and Lesson 7 (posts along a boundary).*

Posts stand at every 5 metres around the fence of a rectangular pen 20 metres by 15 metres, with a post at each corner. How many posts are needed?

- A. 7
- B. 15
- C. 13
- D. 14

**MCQ 36 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Uses half the perimeter, 35 divided by 5 = 7, which counts only one side of the fence.
- **B — Incorrect:** Adds a post for the closing corner, 15 posts: a closed loop already has its corner post in the count of gaps.
- **C — Incorrect:** Subtracts one from the gaps, 14 - 1 = 13, as if the fence were a straight line of posts. A straight fence with 14 gaps needs 15 posts, and a closed loop has as many posts as gaps, so 13 is not a valid count.
- **D — Correct:** The perimeter is 2(20 + 15) = 70 m. Around a closed loop the posts equal the gaps, so 70 divided by 5 = 14 posts.

**MCQ 37**

*Joins Lesson 5 (right angle in a semicircle) and Lesson 6 (area of a triangle).*

A diameter AB of a circle has length 14 cm, and C is a point on the circle other than A and B. What is the largest possible area of triangle ABC, in square cm?

- A. 49
- B. 154
- C. 77
- D. 98

**MCQ 37 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Angle ACB is a right angle, because AB is a diameter. Taking AB as the base, the height is at most the radius 7 cm, so the area is at most one half of 14 times 7 = 49 square cm.
- **B — Incorrect:** Gives the area of the whole circle, 22/7 times 49 = 154 square cm, which is not a triangle.
- **C — Incorrect:** Gives the area of a semicircle, 77 square cm, which is larger than any triangle on this diameter.
- **D — Incorrect:** Takes the diameter as the height, 1/2 times 14 times 14 = 98 square cm, but the height cannot exceed the radius.

**MCQ 38**

*Joins Lesson 5 (similar figures) and Lesson 7 (equal squares).*

Two rectangles are similar. The first is 24 cm by 16 cm and is tiled exactly by identical squares of the largest possible side. The second is scaled so that every length is 1.5 times the first. What is the side of the largest identical squares that tile the second rectangle, in cm?

- A. 8
- B. 12
- C. 16/3
- D. 16

**MCQ 38 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Keeps the old side of 8 cm, which ignores the scaling of the rectangle.
- **B — Correct:** The largest square side for the first rectangle is the highest common factor of 24 and 16, which is 8 cm. Every length scales by 1.5, so the square side scales by 1.5 too: 8 times 1.5 = 12 cm.
- **C — Incorrect:** Divides the square side by the scale factor, 8 divided by 1.5 = 16/3, which is not the scaled side.
- **D — Incorrect:** Takes the shorter side of the first rectangle, 16 cm, as the new square side, which is the wrong quantity.

**MCQ 39**

*Joins Lesson 2 (boat speeds) and Lesson 3 (relative motion).*

A boat has a still-water speed of 8 km/h and the stream runs at 2 km/h. The boat travels downstream and passes a log floating with the stream at point P. How many minutes later is the boat 4 km ahead of the log?

- A. 24 minutes
- B. 40 minutes
- C. 30 minutes
- D. 120 minutes

**MCQ 39 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Uses the downstream speed, 10 km/h, relative to the bank: 4 divided by 10 hours is 24 minutes. The log is moving with the stream too.
- **B — Incorrect:** Uses the upstream speed, 6 km/h: 4 divided by 6 hours is 40 minutes. The boat is going downstream, so its speed is not the upstream speed.
- **C — Correct:** The log moves with the stream, so the boat's speed relative to the log is its still-water speed, 8 km/h, whatever the stream does. Four kilometres at 8 km/h takes half an hour, which is 30 minutes.
- **D — Incorrect:** Uses the stream speed, 2 km/h: 4 divided by 2 hours is 120 minutes. The stream does not change the speed relative to the log.


# TIMED-SET PRACTICE AND SCORING RUBRIC

The paper's items are answered in a fixed total time, so practice needs a pace as well as accuracy. The budgets below are working plans for this session's practice. They are not official cut-offs, and no time standard is stated here as fact.

## Time budgets by item type

| Item type | Budget | Lesson |
|---|---:|---|
| Combined work, pipes, net climb | 60 seconds | 1 |
| Alternate-day work and cycles, rest-rule schedules | 90 seconds | 1 |
| Geometric decay, consumption and proportion | 60 seconds | 1 |
| Average speed, total over total, unknown speed | 60 seconds | 2 |
| Compass direction, displacement | 45 seconds | 2 |
| Circular track: meetings, offset starts, change of direction | 90 seconds | 3 |
| Race with a head start, unknown length from passings | 60 seconds | 3 |
| Sound, second legs | 60 seconds | 3 |
| Clock angle, right angles at the hour boundary | 60 seconds | 4 |
| Weekday shift, same calendar, date sequences, large powers | 75 seconds | 4 |
| Pythagoras, diagonals, collinear points, ratios on a line | 60 seconds | 5 |
| Circles, polygons, equilateral triangles | 60 seconds | 5 |
| Circle and cylinder formulas, probability by area | 75 seconds | 6 |
| Cube layers and cuboid counts | 60 seconds | 7 |
| Tiling, strips, cuts and equal-area pieces | 90 seconds | 7 |
| Units, gaps between posts, time-unit totals | 45 seconds | 7 |
| Cumulative items (two methods) | 120 seconds | cumulative |

## Three-pass control routine

1. **Pass one.** Read the stem once. Name the family and the fixed or conserved quantity in the first 15 seconds. If the method is clear and the budget allows, solve now. Skip anything that needs a second decision.
2. **Pass two.** Return to the skipped items. Write one equation, one count or one cycle sum. Check it by a second route: reverse the process, recount, or test the sign and the units.
3. **Pass three.** Items still open get elimination only. Remove every option that breaks the units, the sign, the direction or the physical limit. Choose from what remains only when the expected value of the choice is positive, as set out below.

## Guessing and the expected value

The paper's scoring scheme, as recorded in this session's framework, rewards each correct item and deducts one-third of that value for each wrong item. The current notification should be checked before relying on the figures. Under that scheme the expected value of a guess depends on how many options remain.

- A blind guess among four options has expected value 1/4 - (1/3)(3/4) = 0. Guess blind only when no reasoning is possible and time is spent.
- After one option is eliminated, a guess among three has expected value 1/3 - (1/3)(2/3) = 1/9 of one correct item. A guess is worth making.
- After two options remain, the expected value is 1/2 - (1/3)(1/2) = 1/3 of one correct item.

## Practice sets and pace

- **Practice scale.** Score each practice item as one point if it is correct and zero otherwise, and record the error code for each wrong item. Practice sets are not scored with negative marks, so that the method can be drilled without the risk of a guess.
- **Timed set.** A timed set is any eight consecutive numbered items from the list, taken in order. Set 1 is items 1 to 8, set 2 is items 9 to 16, set 3 is items 17 to 24, and the remaining lesson items 25 to 27 are timed with the cumulative items, and the cumulative items 28 to 39 form a twelve-item set that is timed at 120 seconds each.
- **Pace.** Eight items in 12 minutes is an average of one and a half minutes an item. This is a pace for learning, not a standard of the paper.
- **Personal target.** For a timed set of eight items this session uses seven correct within 12 minutes. This is your personal target, not an official cut-off. A set missed below it repeats after the matching remediation, not after more practice of the same kind.

## Error codes for post-test analysis

| Code | Meaning |
|---|---|
| U | Unit slip: km/h not converted, minutes and hours mixed, centimetres and metres mixed, cubic metres read as litres |
| S | Sign or direction slip: adding where the rule subtracts, reversing downstream and upstream, reversing the ratio |
| C | Condition missed: simultaneity, same start point, rest rule, leap-year span, orientation, right angle, diameter |
| D | Distance and displacement confused, or path length read as net position |
| F | Formula applied outside its condition: harmonic mean on unequal legs, Pythagoras without a right angle, plain mean of times |
| K | Counting slip: off-by-one gaps, coincidences miscounted, cube layers miscounted, rebounds miscounted |
| T | Correct method, too slow for the budget |
| G | Guess taken with no reasoning |

## Scoring a practice set

Record each item with its code, count the correct items, and compare with the personal target. Use the code to choose the remediation item below, redo that item, and only then return to a timed set.

# REMEDIATION

Use this section after any practice set or timed set. Choose the error code from the post-test analysis, read the repair, redo the named item from the lesson practice before the next timed set, and then return to the set. The retry gates are personal learning targets, not official standards.

| Code | Recurring miss | Repair before retrying | Re-solve with | Retry gate (personal) |
|---|---|---|---|---|
| U | A unit was not converted before the calculation | Write every quantity with its unit on the page, then convert once, before any division | Item 33 (km/h to m/s) and item 35 (centimetres to cubic units) | Two correct conversions in a row, each with its unit written |
| S | Speeds added or subtracted the wrong way; ratio inverted | Write "opposite: add, same way: subtract" and "faster: larger part of the ratio" before the arithmetic | Item 8 (offset on a circle), item 10 (sound distance) and item 30 (head start) | Two correct direction statements before any calculation |
| C | A condition was missed: simultaneity, rest rule, leap span, orientation, right angle, diameter | Write the condition as a question before the method: "together or alternate?", "does the rest rule apply?", "is 29 February in the span?", "is there a right angle?" | Item 2 (alternate cycles), item 14 (large powers and weekdays), item 25 (floor and orientation) | One correct condition check on each of two new items |
| D | Path length given as the net position, or net position given as the path | Write "path: add the legs" and "net: add the legs with signs" side by side, then choose the one the stem names | Item 7 (compass direction) and item 29 (average velocity) | Two items answered with the stem's named quantity in the first line |
| F | A formula applied outside its condition: harmonic mean on unequal legs, plain mean of times, Pythagoras without a right angle | Before each average or length formula, state its condition in one line and check it against the stem | Item 5 (average speed forms), item 20 (circle area) and item 22 (probability by area) | Two conditions stated correctly before the formula |
| K | Counting slip: off-by-one gaps, coincidences miscounted, cube layers miscounted, rebounds miscounted | Write the count as completed intervals, landings or layers, list the first two values, and check the total against the sum of its parts | Item 3 (rebound height), item 11 (meetings after a stop) and item 13 (strikes) | One count checked by the sum of its parts on each of two new items |
| T | The method was right but the item took too long | Use the three-pass routine; after the budget, switch to elimination and record the time | Repeat the same family in the next timed set within the budget | Time budget met on two items in a row |
| G | A guess was made with no reasoning | Stop at the first point where no step can be justified; eliminate, then decide by the expected value in the timed-set section | Item 4 (rest rule, step by step) and item 17 (collinear points, slope by slope) | Every guess in the next set carries a stated reason |

## If you missed a lesson item

Each lesson's failure conditions are the usual causes of a wrong option. If an item was missed, read the explanation of the option you chose, identify the named method it represents, and return to the lesson's shortcut that states that method's failure condition.

- **Lesson 1 (items 1 to 4).** The wrong option ignores the drain, averages times, applies a percentage to the days, forgets the rest rule or the partial day. Return to the net rate, the landing rule, the hour-by-hour rule and the proportion rule.
- **Lesson 2 (items 5 to 7).** The wrong option uses a plain mean, a harmonic mean on unequal legs, a speed where a time is needed, or a 45-degree bearing. Return to total over total, the unknown-speed quadratic and the compass components.
- **Lesson 3 (items 8 to 11).** The wrong option adds speeds on one line, subtracts them on a circle in the wrong direction, drops the offset or the passing length, or ignores the change of direction. Return to the relative-speed rule, the offset rule and the phase rule.
- **Lesson 4 (items 12 to 15).** The wrong option forgets the leap year, applies the weekday shift without the period of the residues, drops a right angle at the hour boundary, or counts the window incorrectly. Return to the calendar, power and window rules.
- **Lesson 5 (items 16 to 19).** The wrong option counts one common point for each side of a shape, treats a side as meeting the circle once, reads a ratio on a line as having a single value, or drops the right angle before using Pythagoras or the trigonometric ratio. Return to the line-and-circle count, the collinearity test by shared slope, the order-of-points rule for ratios and the right-angle identification step. Retry prompt: name the points or sides first, then state the count or ratio that the order and the right angle allow.
- **Lesson 6 (items 20 to 23).** The wrong option uses the radius where a diameter is given, takes a length ratio where an area ratio is needed, halves a volume that should not be halved, or leaves out the one-third in a cone. Return to the dimension test, the area-ratio rule for probability, the cone formula and the tank-fraction rule. Retry prompt: write the dimension of the answer before the formula, and check the unit once more after the arithmetic.
- **Lesson 7 (items 24 to 27).** The wrong option takes the area bound as the answer, counts a strip with the wrong number of tile lengths, leaves out the 29 February or the rotation rule in a tile count, or forgets that edge cubes carry two painted faces. Return to the strip-cover equation, the construction test for the area bound, the orientation rule and the cube-layer counts. Retry prompt: list the solutions or orientations first, then count the cubes or tiles in each.

## Cumulative items

If a cumulative item was missed, name the two lessons it joins, redo the lesson item in each of them, and only then retry the cumulative item. The two methods must be applied in the order the stem presents them: first the one that produces a number, then the one that interprets it.

# MASTER METHOD MAPS

Each map starts from the question the stem asks and ends at one relation. Use the first map whose first question matches the stem. Each map is a route for choosing a method, and each leaf names the condition that must hold before the relation is used.

```text
MAP 1 - WHAT IS THE RATE? (work, pipes, climbs, consumption, run rate, decay)
  stem asks for a time, a fraction of a job, or a remaining amount
     |
     +-- agents work at the same time ......... rates ADD; time = 1 / sum
     +-- one agent fills, another drains ...... signed rates; net <= 0 never fills
     +-- agents take turns ..................... sum one cycle; count whole cycles;
     |                                             the remainder day decides
     +-- one worker per hour, no rest twice .... simulate; last hour = missing / rate
     +-- a climb with a slide each night ....... (n - 1)(climb - slide) + climb >= height
     +-- a fraction repeats each bounce ........ count landings; rebounds >= threshold
     +-- a group size changes .................. remaining amount / new daily use
     +-- men times days, or a percentage use ... product constant; days / (1 + p)
     +-- runs, overs and a run rate ............ runs = rate x overs
```

```text
MAP 2 - ON ONE LINE OR ON A TRACK? (relative motion, races, sound)
  two bodies move
     |
     +-- one straight line, approaching ........ gap / (vA + vB)
     +-- one straight line, same direction ..... gap / |vA - vB|
     +-- circular track, first meeting anywhere  L / |vA - vB| (same way)
     |                                             L / (vA + vB) (opposite)
     +-- circular track, meeting at the start ... least common multiple of lap times
     +-- circular track, offset start ........... ratio a : (a - offset)
     +-- direction changes during the run ....... phases; count the change once
     +-- passes or meetings in a period ......... whole part of (period / interval)
     +-- race with a head start h over D ........ vA : vB = D : (D - h)
     +-- two head starts ........................ compose through a common base
     +-- length from two passings ............... (V - u) t1 = (V + u) t2 = L
     +-- sound heard at a time .................. event = arrival - distance / sound speed
     +-- second leg after the first ............. add its travel time to the chain
```

```text
MAP 3 - WHICH AVERAGE OR DISTANCE? (speed, displacement, trains, boats, schedules)
  stem asks for a speed, a distance, a displacement or a count of vehicles
     |
     +-- average speed over legs ............... total distance / total time
     |        equal distances only ............. 2ab / (a + b)
     +-- unknown speed in a journey ............. write times in v; solve the quadratic
     +-- path travelled ........................ add every leg's length
     +-- net position, or distance from start .. add the legs with their signs
     +-- compass direction of the net position . components; arctan of the ratio
     +-- train crossing a pole or platform ..... (train length + object length) / speed
     +-- boat ................................... downstream b + s; upstream b - s (b > s)
     +-- vehicles on a timetable ................ round-trip time / interval, rounded up
     +-- distance under a velocity-time graph .. the area under the graph
```

```text
MAP 4 - WHICH CLOCK OR CALENDAR RULE? (angles, coincidences, drift, weekdays)
  stem asks about hands, a clock's error, a date or a weekday
     |
     +-- angle between the hands ............... |30H - 5.5M|, H mod 12; if > 180, 360 - angle
     +-- hands together ........................ 720k/11 minutes after 12; 11 per 12 h
     +-- hands at right angles ................. 22 per 12 h; M >= 60 belongs to the next hour
     +-- clock gains or loses .................. rate x elapsed time
     +-- striking clock .......................... intervals = strikes - 1 in each run
     +-- weekday after a date .................. days between, mod 7
     |        span contains 29 February ........ shift 2; otherwise 1
     |        century year ...................... leap only if divisible by 400
     +-- same calendar in another year .......... same 1 January weekday and leap status
     +-- date sequence with a gap ............... add the gap; count 29 February inside
     +-- large power and weekday ................ residues repeat with their own period
     +-- periodic meetings with a weekday ...... LCM of periods, then the weekday shift
     +-- coincidences inside a window ........... LCM multiples in the window
     +-- weekdays that occur five times ........ the surplus days of the month
```

```text
MAP 5 - WHICH SHAPE RELATION? (geometry and Class X trigonometry)
  stem names a figure
     |
     +-- a right angle is given or follows ..... c^2 = a^2 + b^2 (only then)
     +-- a diameter is a side ................... the third vertex on the circle is a right angle
     +-- parallel and perpendicular lines ...... transversal equal angles; perpendicularity passes
     +-- two similar figures .................... lengths x k; areas x k^2; volumes x k^3
     +-- two points on a plane .................. sqrt(dx^2 + dy^2); a grid route adds blocks
     +-- collinear points ....................... equal slopes from one shared point
     +-- a ratio on a line ...................... list the orders; each order fixes one value
     +-- a line and a circle .................... at most 2 points per side or line
     +-- equally spaced points on a circle ...... equilateral triangles = points / 3
     +-- three-dimensional box .................. sqrt(x^2 + y^2 + z^2)
     +-- right triangle with an angle theta ..... sin = opp/hyp; cos = adj/hyp; tan = opp/adj
```

```text
MAP 6 - WHICH MEASURE? (plane and solid mensuration)
  stem asks for an area, a volume, a surface or a probability
     |
     +-- area of a rectangle, triangle, trapezium  l x b; bh/2; (a + b) h / 2
     +-- circle area and circumference ........... pi r^2; 2 pi r; pi = 22/7 when r is a multiple of 7
     +-- cube, cuboid and surface ................ 6a^2; 2(lb + bh + hl); volume a^3, lbh
     +-- cylinder, cone, sphere .................. pi r^2 h; one-third of it; 4 pi r^3 / 3
     +-- closed cube from a sheet ................ 6s^2 = sheet area
     +-- similar solids and density .............. volume x k^3; mass = density x volume
     +-- probability by area ..................... area of region / area of target
     +-- a tank partly filled by a solid ......... (tank - solid) / tank, one unit
```

```text
MAP 7 - WHICH COUNT, FIT OR UNIT? (cubes, tiling, cuts, units)
  stem asks for a count, a fit, a volume or a conversion
     |
     +-- painted solid cube, side n ............ corners 8; 12(n-2); 6(n-2)^2; (n-2)^3
     +-- painted cuboid a x b x c .............. the same four counts with a-2, b-2, c-2
     +-- pieces from cuts ....................... (a+1)(b+1)(c+1); least cuts from a factorisation
     +-- tiling without cutting ................. test single orientation (sufficient, not necessary)
     |        mixed orientation may still fit .. split a side into whole multiples
     |        tile count ......................... area / tile area, only when the tiling exists
     +-- a strip of one width .................... integer solutions of the length equation
     +-- a floor with the most whole tiles ...... area bound, then a construction
     +-- equal squares or equal triangles ........ side divides both sides; area test, then cut
     +-- gaps between equal posts ............... straight line: posts - 1; closed loop: posts
     +-- speed in km/h to m/s .................... multiply by 5/18
     +-- volume in cubic metres to litres ........ multiply by 1000
     +-- time in units of x ...................... coefficient = sum of unit sizes in seconds
     +-- fixed sum of two sides, maximise area ... equal sides (square) unless one side is fixed
```

## Using the maps

- Read the stem's first noun and choose the map. If two maps seem to apply, the map whose quantity is asked for in the question wins: a question about a time is a Map 1 or Map 2 question even if a figure is drawn.
- Each leaf is a relation with a condition. Write the condition on the page before the relation, not after the arithmetic.
- When a leaf's condition is not satisfied, do not use the relation. Return to the first-principles method of the lesson that owns the map: total over total, the cycle sum, the net position, the layer count, the phase count or the direct geometric check.

# COMPLETE CONSOLIDATED REGISTER NOTES

These notes consolidate the whole session. They are compressed for recall, so each line states a rule, the condition under which the rule holds, and the form in which it fails. Every figure in the table was computed in exact arithmetic before it was written.

## Exam shortcut cheat-sheet with failure conditions

| # | Shortcut | Holds only when | Fails when | Checked figure | Lesson |
|---:|---|---|---|---|---:|
| 1 | Combined work: rates add, invert the sum | Workers work at the same time, without blocking | They take turns, or they interfere | 1/8 + 1/24 gives 6 days | 1 |
| 2 | Pipes: signed net rate | Each pipe's sign is set by fill or drain | The net rate is zero or negative: the tank never fills | Fill 6 h, drain 4 h: never fills | 1 |
| 3 | Alternate days: whole cycles plus the remainder | Turns repeat in a fixed order | The remainder is taken as a whole cycle, or the starter is ignored | A 6 days, B 9 days: 7 days if A starts, 7 1/3 if B starts | 1 |
| 4 | Climb with a slide: the final-step rule | Each night's slide is smaller than the day's climb | Height divided by net climb, rounded up | Climb 6, slide 2, height 18: 4 days, not 5 | 1 |
| 5 | Consumption: remaining amount over new use | The daily use changes at a stated moment | Remaining days scaled by the old ratio | 20,000 units at 2,000 a day: 10 days | 1 |
| 6 | Bounce landings: rebounds at or above the threshold | The rebound rule is the stated threshold | Rebound below the threshold is counted | Drop 2 m, 3/4, threshold 0.5 m: 5 landings | 1 |
| 7 | Hour-by-hour rest rule | One worker an hour, never twice running | Rates added into one hour; partial hour rounded up | A 4 h, B 6 h, C 6 h: 4 h 40 min | 1 |
| 8 | Men times days; percentage use | Same work at the same rate | Percentage applied to days | 12 men, 10 days: 6 men, 20 days; 12 days at +20 per cent: 10 days | 1 |
| 9 | Average speed: total over total | Always, whenever distances and times are known | Plain mean of speeds, unless the legs take equal time | 30 km at 15 and 60 km at 20: 18 km/h | 2 |
| 10 | Equal-distance harmonic mean | Legs cover equal distances | Distances differ | 40 km at 40 and 40 km at 80: 53 1/3 km/h | 2 |
| 11 | Segment order: sorted pairing is fastest | Compare the sorted pairing with another pairing | Ranking two arbitrary pairings without computing both | Distances 1 and 3 with speeds 2 and 6: 1 h, against 5/3 h | 2 |
| 12 | Net displacement versus path | Stem names the quantity | The body never reverses, so the two coincide | 4 forward and 3 back, 10 jumps, net 12: path 36 | 2 |
| 13 | Unknown speed: quadratic in v | Times written as distance over speed | Negative root taken; unknown written as time | 20 km at v and 40 km at v + 10 in 4 h: v = 10 | 2 |
| 14 | Compass: components then arctan | Components added with sign | Bearing taken as 45 degrees | 24 m east, 10 m north: about 23 degrees north of east | 2 |
| 15 | Train crossing: both lengths | Crossing a platform, bridge or another train | Only the train's length is used | 100 m at 90 km/h: pole 4 s, 150 m platform 10 s | 2 |
| 16 | Trains passing: difference of speeds with lengths | Same direction, overtaking | Speeds are added | 200 m train at 25 m/s overtakes a man at 5 m/s: 10 s | 2 |
| 17 | Boat: b + s and b - s | Still-water speed exceeds the stream | b is not greater than s | b = 9, s = 3, 36 km each way: 9 h | 2 |
| 18 | Timetable: round trip over interval, rounded up | Layover included | Rounded down, or layover left out | 60 h trip, 24 h interval: 3 vehicles | 2 |
| 19 | Velocity graph: area is distance | The graph is velocity against time | The height is read as distance | 0 to 20 m/s in 10 s, then 5 s at 20: 200 m | 2 |
| 20 | Relative speed on one line | Motion along one straight line | Bodies move at right angles | Gap 60 m, speeds 15 and 9 (same way): 10 s | 3 |
| 21 | First meeting on a circle, same way | Same start, constant speeds | Offset starts, changing speeds | L = 600, speeds 8 and 5: 200 s | 3 |
| 22 | Offset start on a circle: a : (a - offset) | Same direction; stated meeting point | Offset added instead of subtracted | B 60 degrees ahead, meeting at 180 degrees: 3 : 2 | 3 |
| 23 | Meeting at the start point: LCM of lap times | Both runners complete whole laps | Lap times are not commensurable; the relative-speed time is used | Lap times 75 and 120 s: 600 s | 3 |
| 24 | Passes in a period: whole part of period over interval | Start moment not counted | Start counted, or a fraction rounded up | L = 300, speeds 9 and 6: 4 passes in 450 s | 3 |
| 25 | Head start: vA : vB = D : (D - h) | Both finish together | Head start given in time; ratio inverted | D = 300, h = 20: 15 : 14 | 3 |
| 26 | Two head starts through a base | Both ratios in one race | Subtracting the head starts | 1000 m, 200 and 400 m starts: 250 m | 3 |
| 27 | Length from two passings | Same length in both passings | Train speed used for the man's direction | Man at 2 m/s, passings 30 s and 6 s: 30 m | 3 |
| 28 | Arrival-time difference | The same journey at two speeds | Minutes and hours mixed | Difference 8 min at 4 and 6 km/h: 1.6 km | 3 |
| 29 | Sound: event earlier by distance over speed | Source fixed, sound speed known | Travel time added to arrival | 1650 m at 330 m/s: 5 s before arrival | 3 |
| 30 | Second leg from the first reception | Second signal starts at the first arrival | Second leg started at the event | 25 m/s, 120 s extra: 3000 m; explosion 10 s before | 3 |
| 31 | Change of direction: phases | Each phase has its own rule | Change instant counted twice | X 2 and Y 1 per minute, reversal at 2 min, X at 8 rounds: 10 | 3 |
| 32 | Clock angle: |30H - 5.5M|, H mod 12 | H on a twelve-hour dial | 24-hour hour used; minute term dropped | 10:20 gives 170; 9:15 gives 172.5 | 4 |
| 33 | Hand coincidence: 720k/11 minutes | Counted over the window | Twelve per twelve hours assumed | 11 per 12 h; 6 between 3 pm and 9 pm | 4 |
| 34 | Right angles and the hour boundary | Root with M of 60 or more is the next hour | Root counted in both hours | 3:32 and 8/11 minutes; 4:05:27 is next hour | 4 |
| 35 | Clock error: rate times elapsed time | Constant rate | Hours and minutes mixed | 6 min per day: 30 min in 120 h | 4 |
| 36 | Weekday shift: days between mod 7 | Span known | 2 added for every leap year | 1 Dec 2027 Wed gives 1 Dec 2028 Fri | 4 |
| 37 | Century rule | Divisibility by 400 for century years | Every 100 years assumed to hold 5 odd days | 1901 to 2000: 6; 2001 to 2100: 5; 400 years: 0 | 4 |
| 38 | Same calendar: weekday and leap status | Both tests match | Weekday only | 2003 and 2014 both start on Wednesday, both common | 4 |
| 39 | Date sequence with a gap | Every calendar day counted | 29 February ignored | 14 February 2000 plus 42 days: 27 March 2000 | 4 |
| 40 | Large power: residue period | Period of residues found | Exponent reduced modulo 7 | 2 to the power 100 days after Monday: Wednesday | 4 |
| 41 | Periodic meetings: LCM then weekday | Periods are whole numbers | Sum or product used | Periods 6 and 8: LCM 24, shift 3 | 4 |
| 42 | Coincidences in a window: LCM multiples | Start moment not counted | Start counted | Periods 60, 80, 100 s: LCM 1200 s, three in an hour | 4 |
| 43 | Striking clock: intervals are strikes minus one | A run stands alone | Strikes counted as intervals | Run of 3 in 4 s: interval 2 s; run of 5 takes 8 s | 4 |
| 44 | Five occurrences: surplus days of the month | Month length and first day known | Month length or first day unknown | 31 days from Saturday: Sat, Sun, Mon five times | 4 |
| 45 | Pythagoras | A right angle is identified | No right angle | Legs 15 and 9 give 12 | 5 |
| 46 | Rectangle and box diagonal | Rectangle or box, all edges known | Two of three box edges used | Box 2, 3, 6 gives 7 | 5 |
| 47 | Angle in a semicircle | The side is a diameter | Chord rather than diameter | 6 equally spaced points: 3 x 4 = 12 right triangles | 5 |
| 48 | Similar figures: area scales by k squared | Figures are similar | Figures are not similar | 3, 4, 5 triangle scaled by 4: area 96 | 5 |
| 49 | Plane distance: root of squared differences | Straight path | Grid route, which adds blocks | (-2, 1) to (4, 9): straight 10; grid 6 + 8 = 14. (0, 0) to (3, 4): grid 7, straight 5 | 5 |
| 50 | Right-triangle ratios (Class X) | Right angle, angle named | Wrong side named as opposite or adjacent | 10 m ladder at 60 degrees: 5 sqrt(3) m high | 5 |
| 51 | Line and circle intersections | At most two per line or side | Vertices counted instead; side counted once | Hexagon and circle: at most 12 | 5 |
| 52 | Collinear points: equal slopes sharing a point | Shared point | Two unrelated slopes compared | (0,0), (2,1), (4,2): collinear | 5 |
| 53 | Ratio on a line: one value per order | Each order of the three points | Only one order considered | PQ : QR = 2 : 7 gives 2 : 9 and 2 : 5 | 5 |
| 54 | Equilateral triangles on equally spaced points | 3 divides the number of points | Counting every triple of points | 18 points: 6 triangles | 5 |
| 55 | Plane and solid formulas | Dimension of the answer names the formula | Area and volume mixed | Triangle 10 by 6: 30; sphere radius 3: 36 pi | 6 |
| 56 | Circle: pi = 22/7 when r is a multiple of 7 | Radius a multiple of 7 | Diameter used for radius | Radius 7: area 154; circumference 44 | 6 |
| 57 | Cube side doubled | Surface and volume laws | Length factor used for area | Surface x4, volume x8 | 6 |
| 58 | Closed cube from sheet: 6s squared | Whole sheet used | Volume formula used | 15 by 10 sheet: side 5 | 6 |
| 59 | Similar solids: k cubed; mass follows volume | Same density | k squared used for volume | Sides 2 : 1: volumes 8 : 1 | 6 |
| 60 | Probability by area | Equally likely points | Length ratio used | Red radius 0.3 m in a 1 m radius: 0.09 | 6 |
| 61 | Tank partly filled by a solid | One unit; tank volume in denominator | Volumes in mixed units | Tank 10 x 4 x 3, cylinder 62.8 m cubed: 57.2/120 | 6 |
| 62 | Painted cube layers | Outer faces painted, unit cubes | Faces unpainted, hollow, or unequal cuts | n = 4: 8, 24, 24, 8 (sum 64) | 7 |
| 63 | Painted cuboid layers | Outer faces painted, unit cubes | Full sides used in place of a - 2 and the others | 3 x 4 x 5: 8, 24, 22, 6 (sum 60) | 7 |
| 64 | Tiling: single orientation is sufficient, not necessary | Sides are whole multiples of a tile side | Failure taken as proof of impossibility | 5 x 6 with 2 x 3: 5 tiles in mixed orientation | 7 |
| 65 | Tile count: area over tile area | An exact tiling exists | No exact tiling | 7 x 6 with 2 x 3: 7 tiles | 7 |
| 66 | Strip extremes: integer solutions | Whole tiles covering the length exactly | Largest and smallest tiles used directly | 3 by 20 with 2 and 5: 10 and 4, difference 6 | 7 |
| 67 | Floor maximum: area bound and construction | A construction reaches the bound | Area bound taken as the answer | 5 by 3 with 2 by 1: 7 tiles, bound 7.5 | 7 |
| 68 | Equal squares and triangles | Side divides both sides; area test | Area alone taken as proof | 12 by 4: three squares; six triangles of area 8 | 7 |
| 69 | Time in units of x | Each unit's seconds | Units added as x plus x | 3600x + 60x + x = 3661x | 7 |
| 70 | Pieces from cuts: (a+1)(b+1)(c+1) | Cuts in three perpendicular directions | Non-perpendicular or unequal cuts | 1, 2, 1 cuts: 12 pieces | 7 |
| 71 | Least cuts for a count: factorisation | Pieces are identical; cuts equally spaced | Factors not balanced | 24 pieces: 2, 3, 4 gives 6 cuts | 7 |
| 72 | Gaps between posts | Equal spacing | Posts counted as gaps on a line | 11 posts give 10 gaps | 7 |
| 73 | Unit conversion: km/h times 5/18 | Speed in km/h to m/s | Factor reversed or omitted | 72 km/h is 20 m/s | 7 |
| 74 | Volume: 1 cubic metre is 1000 litres | Volume in litres asked | Litres mistaken for cubic centimetres | 2 m cubed is 2000 L | 7 |
| 75 | Fixed perimeter maximum | Both sides free | One side fixed | Perimeter 40: 100 at 10 by 10; side 12 fixed: 96 | 7 |

## Revision recall by subtopic

### Rates and work

- Rate is the fraction of a job done per unit time; rates add for simultaneous workers and times never add.
- A filler is positive and a drain negative; a net rate of zero or less means the tank never fills.
- Alternate-day work: sum one cycle, count whole cycles, and finish the remainder on the day that falls to the worker whose turn it is.
- A rest rule allows one worker an hour and no worker twice running; the last hour takes the missing fraction divided by that worker's hourly rate.
- A climb with slides ends on the first day the climb alone reaches the top; the final climb is not followed by a slide.
- A bounce count is the drop plus each rebound at or above the threshold.
- A consumption item keeps the remaining amount fixed and changes only the daily use; men times days is constant for the same work.

### Speed, distance and displacement

- Speed is path per time; average speed is total distance over total time.
- The plain mean of speeds is right only for equal times; the harmonic mean only for equal distances.
- An unknown speed comes from the equation in v; keep the positive root.
- The sorted pairing of distances and speeds gives the minimum total time, and two arbitrary pairings must be computed in full.
- Distance is the sum of the legs; displacement is the signed sum, and a round trip has zero displacement.
- Average velocity is displacement over time; it can be zero while the average speed is positive.
- The compass direction of a net displacement comes from its two components, not from a default 45 degrees.
- The area under a velocity-time graph is the distance.

### Trains, boats and schedules

- A train crossing a pole covers its length; a crossing of a platform or a bridge covers both lengths.
- Trains passing in opposite directions add their speeds; overtaking adds the lengths and subtracts the speeds.
- Two passings with the same length give the train's speed and its length through (V - u) t1 = (V + u) t2.
- Downstream adds the stream speed; upstream subtracts it and needs still-water speed to exceed it.
- The number of vehicles on a timetable is the round-trip time over the interval, rounded up, with the layover included.

### Relative motion, races and sound

- On one line, opposite motion adds speeds and same-direction motion subtracts them; the meeting time is the gap over that rate.
- On a circular track, the first same-direction meeting is L over the speed difference; the first opposite meeting is L over the sum.
- An offset start on a circle gives the speed ratio a : (a - offset).
- A meeting at the start needs whole laps for both runners: take the least common multiple of the lap times.
- Passes and meetings in a period are counted by the whole part of the period over the interval; the start is not counted.
- A change of direction splits the count into phases; the change and stop instants are each counted once.
- A head start h in a race of length D gives speeds in the ratio D : (D - h); two head starts compose through a common base.
- For a fixed distance, time falls as speed rises; equal distances at two speeds give the time difference through d over v1 minus d over v2.
- Sound takes distance over its speed; the event is earlier than the arrival by that time, and a second leg adds its travel time to the chain.

### Clocks

- The angle between the hands is |30H - 5.5M| with H on a twelve-hour dial; an angle above 180 degrees is replaced by 360 minus itself.
- The hands coincide at 720k/11 minutes after twelve for k from 0 to 10: eleven times in twelve hours, twenty-two in a day.
- The hands are at right angles twenty-two times in twelve hours; a root with M of 60 or more belongs to the next hour.
- A clock's error is its rate times the elapsed time; a clock that gains 6 minutes a day is 30 minutes fast after five days.
- A striking clock's run of n strikes has n minus one intervals; the strikes at one to twelve total 78 in twelve hours.

### Calendars

- The weekday moves by the days between two dates, modulo seven; the shift over a year is 1, or 2 when 29 February is in the span.
- A century is leap only when divisible by 400; the odd days of a century span depend on the span: 6 for 1901 to 2000, 5 for 2001 to 2100, and 0 for 400 years.
- Two years share a calendar only when the weekday of 1 January and the leap status both match.
- A date sequence with a constant gap counts every calendar day, including 29 February inside the interval.
- A large power's weekday uses the period of its residues modulo 7, not the exponent modulo 7.
- Periodic meetings occur at the LCM of the periods, and the weekday moves by that LCM modulo seven.
- The weekdays that occur five times in a month are the weekdays of its surplus days, the first days of the month.

### Geometry and Class X trigonometry

- Pythagoras applies only after a right angle is identified: the hypotenuse squared is the sum of the other two squares.
- A rectangle's diagonal is the root of the sum of its squares; a box's space diagonal uses all three edges.
- A line perpendicular to one of two parallel lines is perpendicular to the other; two lines perpendicular to the same line are parallel.
- The angle in a semicircle is a right angle, and only a diameter as a side fixes the right angle.
- A line meets a circle in at most two points, so a polygon with n sides meets it in at most 2n.
- Collinear points share equal slopes from one common point; a ratio on a line has one value for each order of the points.
- Equilateral triangles on n equally spaced points number n divided by 3 when 3 divides n.
- Similar figures scale lengths by k, areas by k squared and volumes by k cubed.
- The straight-line distance between two points is the root of the sum of squared coordinate differences; grid routes add their blocks.
- In a right triangle, sin is opposite over hypotenuse, cos is adjacent over hypotenuse, and tan is opposite over adjacent; sin squared plus cos squared is one.
- Standard values: at 30 degrees, sin is 1/2 and cos is root 3 over 2; at 45 degrees, sin and cos are 1 over root 2; at 60 degrees, sin is root 3 over 2 and cos is 1/2. The tangents are 1 over root 3, 1 and root 3.

### Mensuration, cubes, tiling and units

- Triangle area is one half of base times perpendicular height; the trapezium's area is the average of the parallel sides times the height.
- A circle's area is pi r squared and its circumference 2 pi r; use pi = 22/7 for an exact answer when r is a multiple of 7.
- A cube has surface 6a squared and volume a cubed; a cuboid has surface 2(lb + bh + hl) and volume lbh.
- A cylinder's volume is pi r squared h; the cone takes one-third of it; a sphere's volume is 4 pi r cubed over 3.
- A closed cube from a sheet has surface 6s squared equal to the sheet's area.
- Similar solids have volumes in the ratio k cubed; mass follows volume when the density is the same.
- The probability of a region equals its area divided by the whole target's area.
- A painted n-cube has 8 corners, 12(n - 2) two-face cubes, 6(n - 2) squared one-face cubes and (n - 2) cubed unpainted cubes, which add to n cubed.
- A cuboid's counts use a - 2, b - 2 and c - 2 for the interior edge lengths, and add to abc.
- A single orientation that fits proves a tiling; a failed orientation proves nothing, since a mixed tiling can exist.
- A tile count is the area over the tile area, only when the tiling exists; the area bound is reached only if a construction exists.
- Equal squares tile a rectangle only if their side divides both sides; equal triangles need the area test and a construction.
- Cuts in three perpendicular directions give (a + 1)(b + 1)(c + 1) pieces; the least cuts for a count come from a balanced factorisation.
- Posts on a straight line have one gap fewer than posts; a closed loop has as many gaps as posts.
- Speed in km/h becomes m/s by multiplying by 5/18; one cubic metre is 1000 litres.
- Time in units of x has the coefficient equal to the sum of the unit sizes in seconds.
- With a fixed sum of sides, the area is largest at the square, unless one side is fixed.

## Formula reference

- Rate: 1 / time for one whole job; combined rate is the signed sum.
- Speed: distance / time; average speed: total distance / total time.
- Harmonic mean for equal distances: 2ab / (a + b).
- Relative speed: sum for opposite, difference for same direction.
- Clock angle: |30H - 5.5M|, reduced by 360 when above 180.
- Pythagoras: c squared = a squared + b squared, for a right angle only.
- Triangle: bh/2. Circle: pi r squared; 2 pi r. Cylinder: pi r squared h. Cone: one-third of the cylinder. Sphere: 4 pi r cubed / 3.
- Painted n-cube: 8, 12(n - 2), 6(n - 2) squared, (n - 2) cubed.

# COVERAGE MATRIX

Every unit of the basic and advanced owners is listed with the lesson part that teaches it. The practice column names the item that tests the unit, or says that the unit is taught by a worked check and carries no item. Items 1 to 27 are lesson items and items 28 to 39 are cumulative items. Each practice cell names an item that tests the unit in its row, or says "worked check (no item)". Where an item tests only part of a unit, the cell says which part.

| Unit (owner) | Taught in | Practice | Linked past questions (family codes) |
|---|---|---|---|
| Rate times time equals amount (Basic section 1) | Lesson 1, visual | Items 1, 2 | W, N, E and RT entries |
| Combined work: rates add; time = 1 / sum (Basic section 2) | Lesson 1, Shortcut 1; Basic Example A | Item 1 | W1 (2020 Q71; 2021 Q80; 2022 Q57; 2025 Q59) |
| Pipes: fillers and drains; net rate of zero or less (Basic Example B) | Lesson 1, Shortcut 2 | Item 1 | W1 (2025 Q45) |
| Alternate-day work and cycles; who starts (Advanced Methods 1 and 4) | Lesson 1, Shortcut 3 | Items 2, 31 | W2 (2023 Q20) |
| Hour-by-hour rest rule | Lesson 1, Shortcut 7 | Item 4 | W2 (2024 Q8) |
| Climb with slips and the final-step rule | Lesson 1, Shortcut 4 | Worked check (no item) | N1 (2017 Q16; 2020 Q80) |
| Geometric decay (height after rebounds) and the landing rule | Lesson 1, Shortcut 6 | Item 3 (height after three rebounds); landing count worked check | N1 (2021 Q16) |
| Consumption and changed group; men times days; percentage use | Lesson 1, Shortcuts 5 and 8 | Worked check (no item) | E1 (2013 Q64; 2013 Q65); W1 (2013 Q47; 2024 Q7) |
| Run rate and overs | Lesson 1, run-rate paragraph | Worked check (no item) | RT (2025 Q9) |
| Speed as distance over time; average speed as total over total (Basic section 2, Example F) | Lesson 2, Shortcut 1 | Items 5, 29 | S1 (2013 Q49; 2015 Q71; 2020 Q72) |
| Harmonic mean for equal distances | Lesson 2, Shortcut 2 | Item 5 | S1 (2020 Q72) |
| Segment order and the rearrangement rule (Advanced Method 5) | Lesson 2, Shortcut 3 | Worked check (no item) | S1 (2026 Q50) |
| Distance and displacement; reversals | Lesson 2, Shortcut 4 (cyclist, Advanced drill item 6, with its velocity) | Items 29 | D1 (2016 Q9; 2016 Q58; 2019 Q57; 2021 Q18; 2021 Q20; 2022 Q6; 2026 Q13) |
| Unknown speed: solving the quadratic | Lesson 2, Shortcut 9 | Item 6 | S2 (2013 Q36); L2 (2026 Q69) |
| Compass direction of the net displacement | Lesson 2, Shortcut 10 | Item 7 | D1 (2020 Q31) |
| Trains: pole, platform, opposite (Advanced drill item 2) and overtaking (Advanced Method 3) | Lesson 2, Shortcut 5 | Item 33 (train crossing a bridge, with unit conversion) | R3 (2018 Q6; 2026 Q20) |
| Boats and streams (Advanced drill item 1) | Lesson 2, Shortcut 6 | Item 39 | B1 (2020 Q74) |
| Timetables and vehicles needed | Lesson 2, Shortcut 7 | Worked check (no item); item 34 tests joint departures only | X1 (2016 Q38) |
| Velocity-time graph as distance | Lesson 2, Shortcut 8 | Worked check (no item) | Y1 (2018 Q5) |
| Relative speed on one line | Lesson 3, Shortcut 1 | Item 9 | R1 (2014 Q69; 2021 Q29); R2 (2013 Q35; 2017 Q39; 2025 Q39) |
| First meeting on a circular track (Advanced Method 2) | Lesson 3, Shortcut 2 | Worked check (no item) | C1 (2022 Q15; 2025 Q37) |
| Meeting at the start point (Advanced drill item 5) | Lesson 3, Shortcut 3 | Worked check (no item) | C1 (no separate family item) |
| Passes and meetings in a period | Lesson 3, Shortcuts 4 and 5 | Worked check (no item) | C1 (2016 Q75) |
| Race with a head start | Lesson 3, Shortcut 6 | Item 30 | S2 (2015 Q34) |
| Equal distance: time inverse to speed | Lesson 3, Shortcut 7 | Worked check (no item) | S2 (2013 Q66) |
| Arrival-time difference at two speeds (Basic Example, distance from times) | Lesson 3, Shortcut 8 | Worked check (no item) | S2 (2014 Q50) |
| Sound and event time | Lesson 3, Shortcut 9 | Item 10 | R4 (2026 Q41) |
| Offset start on a circle | Lesson 3, Shortcut 10 | Item 8 | C1 (2018 Q40) |
| Progress fraction of a race | Lesson 3, Shortcut 11 | Worked check (no item) | S2 (2019 Q16) |
| Composing two head starts through a base | Lesson 3, Shortcut 12 | Worked check (no item) | S2 (2019 Q36) |
| Length from two passings | Lesson 3, Shortcut 13 | Item 9 | R2 (2025 Q39) |
| Second leg after the first arrival | Lesson 3, Shortcut 14 | Worked check (no item) | R4 (2026 Q41) |
| Change of direction on a track (stop variant tested) | Lesson 3, Shortcut 15 | Item 11 | C1 (2026 Q37) |
| Clock angle with H on a twelve-hour dial (Basic Example D) | Lesson 4, Shortcut 1 | Item 15 | K1 (2014 Q12; 2015 Q68; 2021 Q57; 2024 Q40) |
| Hand coincidences: 11 per twelve hours (Advanced drill item 3 counts) | Lesson 4, Shortcut 2 | Worked check (no item) | K1 (2022 Q68; 2024 Q37) |
| Right angles and the hour boundary (Advanced, drill item 4) | Lesson 4, Shortcut 10 | Worked check (no item) | K1 |
| Clock drift | Lesson 4, Shortcut 4 | Worked check (no item) | K2 (2017 Q31; 2019 Q49; 2022 Q46) |
| Striking clocks | Lesson 4, Shortcut 9 | Item 13 | K2 (2017 Q33) |
| Odd days and the leap-year span | Lesson 4, Shortcut 5 | Worked check (no item) | L1 (2019 Q59; 2021 Q48; 2024 Q38) |
| Same calendar in another year (Advanced sweep) | Lesson 4, Shortcut 11 | Item 12 | L1 (2019 Q59; 2024 Q38) |
| Century rule and 1 January 2099 (Advanced drill item 7, Advanced Method 6) | Lesson 4, Shortcut 6 | Worked check (no item) | L1 (2018 Q59; 2022 Q7) |
| Date sequences with a constant gap | Lesson 4, Shortcut 12 | Worked check (no item) | L1 (2018 Q59) |
| Large powers and weekday residues | Lesson 4, Shortcut 13 | Item 14 | L1 (2023 Q49) |
| Periodic meetings: least common multiple of the periods | Lesson 4, Shortcut 7 | Item 34 (least common multiple only); weekday shift after it worked check | L2 (2021 Q75) |
| Coincidences inside a window (signals) | Lesson 4, Shortcut 14 | Worked check (no item) | L2 (2019 Q35; 2023 Q50) |
| Weekdays that occur five times | Lesson 4, Shortcut 8 | Worked check (no item) | L1 (2019 Q12) |
| Pythagoras, after a right angle (triangle legs) | Lesson 5, Shortcut 1 | Worked check (no item); the square-face diagonal in item 32 uses the same rule | G1 (2016 Q49; 2016 Q57; 2018 Q60; 2019 Q30; 2014 Q68) |
| Rectangle diagonal (box diagonal: worked check) | Lesson 5, Shortcut 2 | Item 32 (the diagonal of a cube face; no box diagonal is tested) | G1 (2017 Q75; 2018 Q60) |
| Parallel and perpendicular lines | Lesson 5, Shortcut 3 | Worked check (no item) | G2 (2015 Q76) |
| Angle in a semicircle; diameter triangles | Lesson 5, Shortcut 4 | Item 37 | G2 (2018 Q58; 2022 Q56) |
| Lines and circles: at most two per side (Advanced-style count) | Lesson 5, Shortcut 8 | Item 16 | G2 (2020 Q73) |
| Collinear points from coordinates | Lesson 5, Shortcut 9 | Item 17 | G1 (2014 Q10) |
| Ratio on a line | Lesson 5, Shortcut 10 | Item 18 | A1 (2021 Q63) |
| Equilateral triangles on equally spaced points | Lesson 5, Shortcut 11 | Worked check (no item) | G2 (2018 Q58) |
| Similar figures: scale rules | Lesson 5, Shortcut 5 | Item 38 | Volume row (2020 Q38) |
| Coordinates and straight-line distance | Lesson 5, Shortcut 6 | Worked check (no item) | No family item in the library |
| Class X right-triangle ratios | Lesson 5, Shortcut 7 | Item 19 | No family item in the library |
| Triangle area (Basic section 2) | Lesson 6, Shortcut 1 | Item 37 | M1 (no family item in the library) |
| Circle area, circumference, pi = 22/7 | Lesson 6, Shortcut 2 | Item 20 | M1 (2016 Q73) |
| Cube, cuboid, cylinder, cone and sphere volumes and surfaces | Lesson 6, Shortcut 3 | Item 21 (cone), item 23 (cylinder); sphere and surface formulas worked check | M1 (2016 Q73) |
| Closed cube from a sheet | Lesson 6, Shortcut 4 | Item 28 | M1 (2016 Q39) |
| Similar solids and density | Lesson 6, Shortcut 5 | Worked check (no item) | M1 (2020 Q38) |
| Probability by area | Lesson 6, Shortcut 6 | Item 22 | P1 (2016 Q79) |
| Tank partly filled by a solid | Lesson 6, Shortcut 7 | Item 23 | M1 (2016 Q73) |
| Painted cube: layer counts (Basic cube table) | Lesson 7, Shortcut 1 | Items 28, 32 | Q1 (2016 Q59; 2017 Q58; 2018 Q35; 2025 Q15) |
| Painted cuboid counts (Basic cube table) | Lesson 7, Shortcut 2 | Item 26 | Q1 (2023 Q79) |
| Single-orientation tiling: sufficient, not necessary (Advanced Method 6 tile) | Lesson 7, Shortcut 3 | Item 27 | T1 (2022 Q59; 2023 Q67) |
| Tile count without rotation (whole tiles in one orientation); Advanced drill item 8 | Lesson 7, Shortcut 4 | Item 27; the area bound is not tested by an item | T1 (2022 Q59) |
| Strip cover: exact cover and minimum count with two tile lengths | Lesson 7, Shortcut 9 | Item 24; three-size extremes worked check | T1 (2026 Q68) |
| Floor maximum: area bound and construction | Lesson 7, Shortcut 10 | Item 25 | T1 (2023 Q67) |
| Equal squares (side divides both sides); equal triangles worked check | Lesson 7, Shortcut 11 | Item 38 (equal squares with a scale factor) | T1 (2022 Q59) |
| Unit conversion: km/h and m/s | Lesson 7, Shortcut 5 | Item 33 | M2 (2024 Q30) |
| Volume units: cubic metres and litres | Lesson 7, Shortcut 5 | Worked check (no item) | M2 (2021 Q68) |
| Time-unit totals in units of x | Lesson 7, Shortcut 12 | Worked check (no item) | M2 (2022 Q35) |
| Fence posts and gaps; closed loops | Lesson 7, Shortcut 6 | Items 36 | M2 (2022 Q26) |
| Fixed perimeter and maximum area | Lesson 7, Shortcut 7 | Worked check (no item) | M1 (2016 Q50) |
| Pieces made by cuts; least cuts | Lesson 7, Shortcut 8 | Item 35 (pieces from one block); least-cut factorisation worked check | Q2 (2024 Q5; 2026 Q24); Q1 (2025 Q15) |
| Cumulative joins | Cumulative section | Items 28 to 39 | Joins two or more lessons |

Units with no practice item are taught in prose with a worked check. They are listed here so that a learner knows where the method lives; the remediation section names the lesson part to return to.

# SOURCE LEDGER

## SOURCE-MANIFEST GATE

| Category | Status | Evidence or reason |
|---|---|---|
| Canonical markdown | checked | upsc-ai-kit/knowledge/CSAT/basic/04_Rates-Motion-Time-and-Geometry.md read in full (sections 1 to 11, formulas, Examples A to F, the cube-count table, the mini-drill and the generated PYQ blocks); used for every unit taught in Lessons 1 to 7 |
| Final learner package | not relevant | Permanently excluded from all live-session work by the permanent live-session source exclusion in live_sessions/LIVE-SESSION-GENERATION-RULES.md; not opened, cited or used |
| Layered/complete session | not available | No other non-excluded layered or complete session for CSAT topic 04 was opened or used; this file is the only live session in its folder |
| Solved workbook | not relevant | Permanently excluded from all live-session work by the permanent live-session source exclusion in live_sessions/LIVE-SESSION-GENERATION-RULES.md; the solved_pyqs library is a different category and is recorded under PYQs through 2026 for the coverage check |
| Advanced dossier | checked | upsc-ai-kit/knowledge/CSAT/advanced/04_Rates-Motion-Time-and-Geometry.md read in full (sections 1 to 11, Methods 1 to 6, time-saving conditions, boundary cases, advanced traps, error analysis, the eight-item drill and its solutions and the generated PYQ block); Advanced units taught in Lessons 1 to 4 and 6 to 7 |
| OCR books | not relevant | The aptitude paper is taught from the canonical owners and the verified PYQ ledgers; the books folder holds only previous-paper scans, and no unit needed book evidence |
| PYQs through 2026 | checked | Routing ledgers upsc-ai-kit/knowledge/_PYQ-ROUTING-CSAT-2018-2023.md, _PYQ-ROUTING-CSAT-2024-2025.md and _PYQ-ROUTING-CSAT-2026.md searched for topic 04 rows (45, 13 and 8 rows: 66 in total for 2018 to 2026). For 2013 to 2017 the solved library's topic routing was used, because no ledger covers those years. Stems for 2018 were read from the verified booklet transcription and for 2019 to 2026 from the solved paper library's question entries, to type approaches; no key, answer letter, option explanation or solution was copied |
| Official live sources | not relevant | Aptitude paper with no current-affairs component; the pre-teach checklists record CA search: not applicable (aptitude paper) and CA found: not applicable |

## Routing reconciliation

Items that the routing sources assign to another topic are not taught in this file. Each is cross-linked in the verified PYQ section with its owner. The 98 items routed to Topic 04 are all taught in a lesson part of this file.

| Year and question | Routed to | Source |
|---|---|---|
| 2014 Q76 | Topic 02 | solved library topic routing |
| 2015 Q33 | Topic 06 | solved library topic routing |
| 2015 Q53 | Topic 03 | solved library topic routing |
| 2016 Q50 | Topic 05 | solved library topic routing |
| 2016 Q78 | Topic 03 | solved library topic routing |
| 2017 Q11 | Topic 03 | solved library topic routing |
| 2019 Q10 | Topic 06 | _PYQ-ROUTING-CSAT-2018-2023.md |
| 2022 Q26 | Topic 03 | _PYQ-ROUTING-CSAT-2018-2023.md |
| 2022 Q56 | Topic 06 | _PYQ-ROUTING-CSAT-2018-2023.md |
| 2023 Q18 | Topic 06 | _PYQ-ROUTING-CSAT-2018-2023.md |
| 2023 Q30 | Topic 06 | _PYQ-ROUTING-CSAT-2018-2023.md |
| 2023 Q79 | Topic 06 | _PYQ-ROUTING-CSAT-2018-2023.md |
| 2025 Q17 | Topic 03 | _PYQ-ROUTING-CSAT-2024-2025.md |
| 2026 Q56 | Topic 06 | _PYQ-ROUTING-CSAT-2026.md |
