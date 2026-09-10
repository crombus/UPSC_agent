# Economy 02 - Growth, Development, HDI, IHDI and MPI

## Quick-Glance Tree Chart

```text
CORE CONCEPT
Growth = sustained real quantitative expansion
  -> development = structural change + distribution + capabilities + sustainability
  -> growth supplies resources; jobs, institutions and services govern conversion
  -> real GDP != real GDP per capita != development
  |
  v
MEASUREMENT TIMELINE
1990 first United Nations Development Programme (UNDP)
     Human Development Report and Human Development Index (HDI)
2010 global Multidimensional Poverty Index (MPI) introduced by
     Oxford Poverty and Human Development Initiative (OPHI) + UNDP
2018 global MPI revision aligned five indicators more closely with SDGs
17 July 2023 NITI National MPI Progress Review
  -> compares NFHS-4 (2015-16) with NFHS-5 (2019-21)
2025 UNDP technical notes used here; current-source check 9 September 2026
  |
  v
HDI DECODER
Purpose -> average human-development achievement
3 dimensions / 4 indicators:
  Health -> life expectancy at birth
  Education -> expected years schooling + mean years schooling (age 25+)
  Living standard -> gross national income (GNI) per capita,
                     constant 2021 purchasing power parity (PPP) dollars
2025 goalposts:
  LE 20-85 | EYS 0-18 | MYS 0-15 | GNIpc 100-75,000
Linear dimension index = (actual-min)/(max-min)
Education = arithmetic mean of EYS and MYS indices
Income = [ln(actual)-ln(100)]/[ln(75,000)-ln(100)]
HDI = (Health x Education x Income)^(1/3)
Why -> logarithm captures diminishing income contribution;
       geometric mean penalises imbalance
Read carefully -> value != rank; report year != data year
  |
  v
IHDI
Same 3 dimensions; inequality is NOT a fourth dimension
Atkinson-type loss Ax in each dimension
Ix* = (1-Ax) x Ix
IHDI = (Health* x Education* x Income*)^(1/3)
Loss = 1-IHDI/HDI
Perfect equality -> IHDI = HDI; otherwise IHDI < HDI
Limit -> not association-sensitive across same individuals
  |
  v
GLOBAL MPI
Institutions -> Oxford Poverty and Human Development Initiative (OPHI)
                + United Nations Development Programme (UNDP)
Method -> Alkire-Foster
Health 1/3:
  nutrition 1/6 | child mortality 1/6
Education 1/3:
  years schooling 1/6 | school attendance 1/6
Living standards 1/3:
  fuel | sanitation | water | electricity | housing | assets, each 1/18
Dual cutoff:
  indicator deprivation -> weighted score c
  c >= 1/3 MPI poor
  current global vulnerable: 1/5 to below 1/3
  current global severe: c >= 1/2
H = incidence = poor population share
A = intensity = poor people's average deprivation share
MPI = H x A
  |
  v
INDIA NATIONAL MPI
Nodal publisher -> National Institution for Transforming India (NITI Aayog)
Data -> National Family Health Survey (NFHS) household microdata;
        national, State/Union Territory and district use
12 indicators, not global 10:
  Health -> nutrition 1/6; mortality 1/12; maternal health 1/12
  Education -> MYS 1/6; attendance 1/6
  Living -> fuel, sanitation, water, electricity, housing, assets,
            bank account, each 1/21
2023 report facts:
  NFHS-4 2015-16 headcount 24.85%
  NFHS-5 2019-21 headcount 14.96%
  report estimate: 13.5 crore exited multidimensional poverty
Never call these 2023 observations.
  |
  v
COMPARISON / LIMITATIONS
Income poverty -> monetary command below a line
MPI -> selected direct and overlapping household deprivation
HDI -> average achievement | IHDI -> inequality-adjusted achievement
Global MPI != India national MPI
Limits -> weights/cutoffs, threshold sensitivity, household-level
          intra-household blindness, survey lag, missing service quality
Use complements, not substitutes.
  |
  v
TRAPS
nominal growth != real growth
per-capita average != distribution
HDI rank != HDI value
GNIpc PPP != GDPpc
IHDI loss != poverty rate
H != A
equal dimensions != equal indicator weights
expenditure != access != quality != outcome
  |
  v
ANSWER SPINE
Define -> choose/decode measure -> state formula and institution
-> attach report year + data year -> give named evidence
-> explain productivity/jobs/services/distribution/environment mechanism
-> qualify averages, cutoffs, household unit, lag and causation
-> conclude: productive inclusion + capabilities + resilience
```
