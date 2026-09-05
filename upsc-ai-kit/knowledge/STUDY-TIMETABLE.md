# UPSC Integrated Study Timetable

> **Cycle start:** Monday, 17 August 2026  
> **Target:** Complete first learning/revision of the knowledge base, generate/update personal notes, and enter a Prelims-dominant phase by April 2027.
> **Calendar caution:** The 2027 UPSC examination dates are not assumed here. Shift Weeks 35-42 so that the final six to eight weeks fall immediately before the officially notified Prelims date.
> **Topic links:** Use [`STUDY-INDEX.md`](STUDY-INDEX.md) for every Core, Advanced, learning-session and notes-PDF link.
> **Progress tracker:** Tick completed work in [`STUDY-SCHEDULE-CHECKLIST.md`](STUDY-SCHEDULE-CHECKLIST.md).

## 1. What is actually left

The syllabus architecture is complete and no official clause is unowned. GS/CSAT/Essay question-level routing is complete for 2018-2026, and Philosophy Optional has its 2018-2025 PYQ banks. The remaining work is personal execution:

1. complete each learning session;
2. practise recall and PYQs;
3. write answers under time;
4. generate/update the topic notes PDF;
5. revise through a fixed 1-7-30 cycle;
6. build current-affairs examples from newspapers and magazines.

## 2. Full-time daily timetable (Monday-Saturday)

| Time | Work | Exact output |
|---|---|---|
| 06:30-07:15 | Newspaper | One page of syllabus-tagged notes: issue, fact, static link, Prelims trap, Mains use |
| 07:15-08:00 | Current-affairs system | Monday-Thursday: Vajiram Recitals; Friday: official-source verification; Saturday: MCQs, Mains examples and backlog |
| 09:00-11:00 | Static Topic A | Core file + active recall + routed PYQs |
| 11:15-12:45 | Static Topic B | Core; Advanced only after Core is secure |
| 14:00-15:30 | Philosophy Optional | Doctrine/argument/comparison/PYQ according to optional track below |
| 16:00-17:00 | Revision | Day-1/Day-7/Day-30 queues |
| 17:00-18:00 | Answer writing | Task specified in the daily answer-writing table |
| 20:30-21:15 | MCQs/CSAT/language | Alternate according to the weekly pattern |
| 21:15-21:30 | Note control | Update topic checklist and PDF-note backlog |

### Four-hour compressed version

Keep, in order: 45-minute newspaper, 100-minute static topic, 60-minute Optional, 35-minute revision, 40-minute answer/MCQ. Do not remove revision or answer writing to preserve extra reading.

## 3. Daily answer-writing pattern

| Day | Mandatory writing |
|---|---|
| Monday | One GS 10-marker, 7 minutes, 150 words, from Topic A |
| Tuesday | One GS 15-marker, 11 minutes, 250 words, from Topic B |
| Wednesday | One Philosophy Optional 10/15-marker from the week's doctrine |
| Thursday | Two GS questions: one static PYQ and one current-linked probable question |
| Friday | Alternate weekly: one Ethics case study / one 1,000-word Essay |
| Saturday | Sectional test: 5 GS answers in 60 minutes, followed by self-review |
| Sunday | Rewrite the weakest answer and add missing examples to the notes PDF |

**Minimum weekly output:** 10 GS answers, 2 Optional answers, one Ethics case or Essay, one rewritten answer, and one objective test.

## 4. Revision and notes-production rule

For every topic:

```text
Day 0: learning session + Core + PYQs
Day 1: 10-minute closed-book recall
Day 7: one-page reconstruction + 10 MCQs or one written answer
Day 30: mixed revision + PYQ retest
Then: update the topic notes PDF and re-run the study-index builder
```

Run after any notes generation:

```powershell
python tools\build_study_index.py
```

## 5. Newspaper: what to study

### Read

- **GS-II:** Supreme Court/constitutional issues, Parliament, federalism, governance reforms, welfare design, international relations.
- **GS-III:** inflation, banking, employment, agriculture, infrastructure, energy, environment, science, cyber/security and disasters.
- **GS-I:** society, demography, urbanisation, cultural/heritage developments and geography-linked events.
- **Ethics/Essay:** one usable real example of integrity, leadership, conflict, technology or social change.

### Skip or heavily limit

- routine party allegations and campaign speeches;
- local crime without a governance/rights dimension;
- celebrity coverage;
- market-price movement without a policy/economic concept;
- sports results unless linked to institutions, governance or a direct PYQ-type current fact.

### Daily current-affairs note format

| Field | Write |
|---|---|
| Trigger | Headline and date |
| Fact | Only source-supported fact |
| Static owner | Exact subject/topic |
| Prelims | One distinction or trap |
| Mains | One argument/example |
| Action | Add to existing topic PDF, not a disconnected scrapbook |

### Current-affairs source rule

- Use **Vajiram & Ravi The Recitals** as the single base monthly compilation.
- Do not read another complete monthly magazine alongside it.
- Verify only important figures, laws, schemes and statements that will be quoted in an answer.
- Use official supplements selectively:
  - **PIB:** major schemes, Cabinet decisions and reports;
  - **PRS:** Bills, Acts and parliamentary developments;
  - **RBI, Economic Survey and Union Budget:** economy and official data;
  - **MEA:** bilateral relations, agreements and international groupings;
  - **MoEFCC/Down To Earth:** environment gaps and case studies;
  - **ISRO/DST:** important science and technology developments.
- Yojana and Kurukshetra are theme supplements, not compulsory cover-to-cover monthly reading.
- Recitals provides no practice layer. Convert it into weekly MCQs and Mains material.

## 6. Vajiram Recitals and supplementary-source timetable

| Slot | Source / task | Exact output |
|---|---|---|
| Monday-Thursday | Vajiram Recitals, approximately 6-8 pages/day | Finish 25-30 pages/week; tag each useful item as Prelims, Mains or both |
| Friday | PIB/PRS/RBI/MEA/MoEFCC/ISRO verification | Verify only answer-worthy figures, legal provisions, scheme design and official positions |
| Saturday | Practice conversion | 5-8 MCQs, two Mains question outlines and one diagram/table from the week's Recitals reading |
| Every Sunday | Weekly CA consolidation | Merge useful material into subject-wise notes; remove duplicates and retain the source month/date |
| Fourth Sunday | Monthly Recitals closure | Complete the issue, revise Editor's Cut items, update maps/places and create a one-page monthly recall sheet |
| Last working day | Publication-lag scan | Cover developments after the magazine cut-off through PIB, PRS, MEA and one reliable newspaper |
| Budget/Survey season | Union Budget + Economic Survey | Concepts, evidence, policy direction and Mains-ready examples |
| Final 2-3 months before Prelims | Vision PT365 | Revision and gap-check only; do not restart full monthly-magazine reading |
| After Prelims | Vision Mains365, selectively | Add analytical dimensions, examples and answer-writing value to weak GS themes |
| Weak-theme requirement only | Yojana, Kurukshetra or Down To Earth | Read only the relevant theme/article; extract examples, challenges and reforms |

Cap Recitals and supplementary work at **four hours per week**. Do not create a separate
month-wise scrapbook: merge every retained item into its static subject/topic owner.

## 7. Weekly Sunday control

| Duration | Task |
|---:|---|
| 90 min | 50 topic-linked Prelims MCQs |
| 60 min | Four GS Mains answers |
| 45 min | Two Philosophy answers/outlines |
| 60 min | Vajiram Recitals consolidation, official verification and publication-lag scan |
| 60 min | Notes PDF update and index regeneration |
| 45 min | Backlog and next-week planning |

Every fourth Sunday replaces the 50-MCQ test with a 100-question mixed test and replaces four GS answers with a half-length Mains sectional.

## 8. Philosophy Optional parallel track

Philosophy runs **90 minutes daily, Monday-Saturday**, parallel to the GS topic listed below.

| Weeks | Optional focus | Writing |
|---|---|---|
| 1-5 | Paper I Western Philosophy | 2 philosopher-specific answers/week |
| 6-10 | Paper I Indian Philosophy | 2 school/comparison answers/week |
| 11-14 | Paper II Socio-Political Philosophy | 2 concept/application answers/week |
| 15-18 | Paper II Philosophy of Religion | 2 argument/criticism answers/week |
| 19-22 | Paper I full revision + 2018-2025 PYQs | One 5-question sectional/week |
| 23-26 | Paper II full revision + 2018-2025 PYQs | One 5-question sectional/week |
| 27-34 | Alternating full Paper I/Paper II tests | One full test every two weeks |
| 35-42 | Maintenance during Prelims phase | Two 30-minute revision slots + one answer/week |

## 9. Forty-two-week integrated cycle

Topic numbers refer to the linked rows in [`STUDY-INDEX.md`](STUDY-INDEX.md). Complete Core first; use Advanced for Mains depth after the day's Core recall.

| Week | Dates | Static study and notes production | Answer writing / objective practice |
|---:|---|---|---|
| 1 | 17-23 Aug 2026 | [Polity](STUDY-INDEX.md#polity) 01-16: historical background, Constitution, rights, DPSP, duties, amendment/basic structure | FR/DPSP 10-marker; basic-structure 15-marker; 100 Polity MCQs |
| 2 | 24-30 Aug | Polity 17-33: executive, Parliament, judiciary and federalism | Parliament/judiciary PYQs; one federal dispute answer; 100 MCQs |
| 3 | 31 Aug-6 Sep | Polity 34-49: local bodies, elections, constitutional/statutory bodies and consolidated regulatory architecture | Bodies comparison table; 5-answer GS-II sectional; revise Weeks 1-2 |
| 4 | 7-13 Sep | [Economy](STUDY-INDEX.md#economy) 01-16: national income, development, inflation, RBI, banking, external sector, budget and agriculture foundations | GDP/inflation answer; monetary-policy answer; 75 Economy MCQs |
| 5 | 14-20 Sep | Economy 17-31: industry, infrastructure, labour, trade, digital/climate economy, agritech, subsidies, missions, animal rearing, energy | Subsidy/energy 15-markers; agriculture MCQs; update Economy CA notes |
| 6 | 21-27 Sep | [Geography](STUDY-INDEX.md#geography) 01-19: geomorphology, climatology, oceans and world climates | Two diagrams daily; monsoon/cyclone answer; 75 map/concept MCQs |
| 7 | 28 Sep-4 Oct | Geography 20-37: resources, population, settlements, India, transport, hazards and contemporary issues | India map test; urbanisation/industry answer; revise Week 6 |
| 8 | 5-11 Oct | [Environment](STUDY-INDEX.md#environment-and-ecology) 01-14: ecology, biodiversity, species, protected areas, conventions and forests | Species/convention MCQs; biodiversity 15-marker |
| 9 | 12-18 Oct | Environment 15-28 + [Disaster Management](STUDY-INDEX.md#disaster-management) 01-05 | Climate/EIA/energy answers; disaster risk framework; 100 mixed MCQs |
| 10 | 19-25 Oct | [Ancient History](STUDY-INDEX.md#ancient-indian-history) 01-14 | Timeline/map recall; Harappan/Buddhism answers; 100 history MCQs |
| 11 | 26 Oct-1 Nov | Ancient 15-27 + [Art and Culture](STUDY-INDEX.md#indian-art-and-culture) 01-05 | Chola PYQ; architecture comparison; visual identification MCQs |
| 12 | 2-8 Nov | [Medieval History](STUDY-INDEX.md#medieval-indian-history) 01-13 | Sultanate administration/Bhakti answer; chronology MCQs |
| 13 | 9-15 Nov | Medieval 14-25 + Art and Culture 06-10 | Mughal/Vijayanagara answer; music/dance/theatre distinctions |
| 14 | 16-22 Nov | [Modern History](STUDY-INDEX.md#modern-indian-history) 01-19 | 1857/moderates/Swadeshi answers; chronology and acts MCQs |
| 15 | 23-29 Nov | Modern 20-38 + Art and Culture 11-15 | Gandhian phase/constitutional development answers; cinema/heritage facts |
| 16 | 30 Nov-6 Dec | [Indian Society](STUDY-INDEX.md#indian-society) 01-15 + [Social Justice](STUDY-INDEX.md#social-justice) 01-08 | Caste/women/urbanisation answers; one society sectional |
| 17 | 7-13 Dec | Social Justice 09-17 + [Governance](STUDY-INDEX.md#governance) 01-08 | Welfare targeting and e-governance answers; scheme-institution table |
| 18 | 14-20 Dec | Governance 09-16 + [International Relations](STUDY-INDEX.md#international-relations) 01-06 | Civil services/regulators answer; neighbourhood/major-power answer |
| 19 | 21-27 Dec | IR 07-12 + [World History](STUDY-INDEX.md#world-history) 01-10 | Groupings/UN answer; revolution/imperialism comparative answer |
| 20 | 28 Dec-3 Jan | World History 11-21 + [Political Theory](STUDY-INDEX.md#political-theory) 01-08 | World wars/decolonisation answer; liberty/equality framework |
| 21 | 4-10 Jan 2027 | Political Theory 09-23 | Justice, rights, democracy and ideology comparison; use only as GS/Essay enrichment |
| 22 | 11-17 Jan | [Science and Technology](STUDY-INDEX.md#science-and-technology) 01-13 | Space/quantum/AI/semiconductor answers; 100 science MCQs |
| 23 | 18-24 Jan | Science and Technology 14-26 + [Internal Security](STUDY-INDEX.md#internal-security) 01-06 | Biotech/computing answer; border/extremism/security answers |
| 24 | 25-31 Jan | Internal Security 07-12 + Disaster Management 06-18 | Cyber/FATF/maritime answers; hazard-specific answer frameworks |
| 25 | 1-7 Feb | [Ethics](STUDY-INDEX.md#ethics) 01-12 | Five definitions/day; two mini cases; one full case-study set |
| 26 | 8-14 Feb | Ethics 13-23 + [Essay](STUDY-INDEX.md#essay) 01-08 | Probity/corruption cases; one philosophical essay |
| 27 | 15-21 Feb | Essay 09-16 + [Qualifying English](STUDY-INDEX.md#qualifying-english) + [Qualifying Hindi](STUDY-INDEX.md#qualifying-hindi) | One full essay; both foundation language tests; précis/translation drill |
| 28 | 22-28 Feb | [CSAT](STUDY-INDEX.md#csat) 01-08 + complete backlog closure | Two timed CSAT sections; one full language mock; all missing topic PDFs listed |
| 29 | 1-7 Mar | GS-I consolidation: History, Culture, Society, Geography | 10 GS-I answers + 100 mixed MCQs + one map test |
| 30 | 8-14 Mar | GS-II consolidation: Polity, Governance, Social Justice, IR | 10 GS-II answers + one half paper + institutions revision |
| 31 | 15-21 Mar | GS-III consolidation: Economy, Agriculture, S&T | 10 GS-III answers + 100 MCQs |
| 32 | 22-28 Mar | GS-III consolidation: Environment, Security, Disaster | 10 GS-III answers + one half paper + 100 MCQs |
| 33 | 29 Mar-4 Apr | GS-IV + Essay consolidation | Two Ethics case sets; one full GS-IV; one full Essay |
| 34 | 5-11 Apr | Philosophy full consolidation + language/CSAT safety check | One Optional Paper I, one Paper II, one CSAT and one language sectional |
| 35 | 12-18 Apr | Prelims revision 1: Polity + Modern History | Two 100-question tests; error-log revision |
| 36 | 19-25 Apr | Prelims revision 1: Ancient/Medieval/Culture + Geography | Two 100-question tests; maps and chronology |
| 37 | 26 Apr-2 May | Prelims revision 1: Economy + Agriculture | Two 100-question tests; Budget/Survey concepts |
| 38 | 3-9 May | Prelims revision 1: Environment + Science | Two 100-question tests; species/conventions/technology |
| 39 | 10-16 May | Current affairs revision: Vajiram subject-wise notes + PT365 gap-check for the last 12 months | Three CA-heavy tests; revise only errors, maps, schemes and source-backed facts |
| 40 | 17-23 May | Full-syllabus mixed revision + CSAT | Three GS mocks + two CSAT papers |
| 41 | 24-30 May | Weak-area repair from test error logs | Two GS mocks; no new source; formula/map/fact sheets |
| 42 | 31 May-6 Jun | Final calm revision window | Two early-week mocks only; then light revision, sleep and logistics |

## 10. Completion rule for a topic

A topic is **not complete** merely because it was read. Mark it complete only when all are done:

- [ ] Core read and recalled without looking
- [ ] Advanced read where Mains/Optional relevant
- [ ] Routed PYQs attempted
- [ ] Prelims MCQs completed where applicable
- [ ] One Mains/Optional answer written
- [ ] Learning-session note completed
- [ ] Notes PDF generated or updated
- [ ] Day-1 and Day-7 revision completed
- [ ] Day-30 revision scheduled
