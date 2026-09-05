"""Authored data for Environment and Ecology learner-v2 Topic 13."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import (
    AIR_POLLUTION_LIVE_SOURCE_ATTEMPTS,
    panel,
)


FACTS = [
    ("Ambient-standard boundary", "A National Ambient Air Quality Standard applies to pollutant concentration in outdoor receiving air; it is not a source-emission limit for a stack, vehicle or process."),
    ("Emission-standard boundary", "A source-emission standard controls what a specified source may release under the applicable rule or consent; compliance cannot be inferred from a city AQI category."),
    ("Concentration versus exposure", "Ambient concentration is a measured amount in air at a place and averaging period, while exposure also depends on where people are, how long they remain and the route of contact."),
    ("Pollutant versus precursor", "A pollutant may be emitted directly or formed in the atmosphere; a precursor participates in reactions that create a secondary pollutant and must not be reported as the resulting pollutant itself."),
    ("Primary and secondary pollution", "Primary pollutants are emitted from sources, whereas secondary pollutants form through atmospheric chemistry; the control pathway must therefore include both direct emissions and precursor control."),
    ("Particulate-size discipline", "PM2.5 and PM10 are aerodynamic size fractions, not chemical species; composition, source and health effect cannot be inferred from size label alone."),
    ("Photochemical-smog chain", "Photochemical smog requires precursor emissions and sunlight-driven chemistry that can form ground-level ozone and other oxidants; ozone at the surface is distinct from protective stratospheric ozone."),
    ("Acid-deposition chain", "Sulphur and nitrogen oxides can act as acid-deposition precursors after atmospheric transformation; an answer must separate precursor emission from later wet or dry deposition."),
    ("NAAQS data discipline", "Every numeric ambient standard must be tied to the notified pollutant, unit, averaging period, area applicability and compliance rule; no value is carried here from a title-only live page."),
    ("AQI communication role", "The Air Quality Index converts monitored pollutant concentrations into a public communication category; it does not replace the notified ambient standard or a source-emission standard."),
    ("AQI category boundary", "An AQI category describes the index for a stated place and time; it is not by itself a statutory finding that every pollutant met or breached every NAAQS averaging period."),
    ("CPCB and SPCB roles", "CPCB coordinates nationally and supports standards and monitoring frameworks, while SPCBs and pollution-control committees perform major consent, monitoring and enforcement functions within their jurisdictions."),
    ("Air Act and consent layer", "The Air Act provides the pollution-control framework, while consent conditions and sector-specific standards regulate sources; a prior environmental clearance is a separate project-appraisal instrument."),
    ("Monitoring representativeness", "A station measures conditions at its location and time; network density, siting, data completeness and meteorology affect whether one reading represents a neighbourhood, city or region."),
    ("Source-apportionment boundary", "Source contribution varies by city, season, pollutant, method and meteorology; no fixed vehicle, industry, dust or crop-residue share can be universalised."),
    ("NCAP programme boundary", "The National Clean Air Programme is a structural planning programme for sustained source reduction and capacity building, not a substitute for the Air Act or a source consent."),
    ("Target versus attainment", "An NCAP goal, city action plan, fund release, activity completion and measured attainment are different stages; an announced target is not an achieved concentration reduction."),
    ("Non-attainment boundary", "Non-attainment classification is based on the applicable monitoring and standards framework over a defined period; it is not the same as a city's current hourly or daily AQI."),
    ("GRAP and CAQM boundary", "GRAP is a graded episodic response for the Delhi-NCR problem, while CAQM is the statutory regional coordination institution; neither replaces long-term source reduction across India."),
    ("Audited evidence boundary", "Audited ledgers carry NCAP, WHO-guideline, photochemical-smog, acid-rain, combustion-source and cloud-seeding concepts into practice without inventing an objective key, source share, standard value or current reading."),
]

TRAPS = [
    "Do not write an ambient standard as a stack or vehicle emission limit.",
    "Do not convert concentration into personal exposure without time-location evidence.",
    "Do not call a precursor the secondary pollutant formed from it.",
    "Do not treat particulate size as chemical composition.",
    "Do not merge ground-level ozone with stratospheric ozone.",
    "Do not quote a standard without its unit and averaging period.",
    "Do not treat an AQI category as the NAAQS table.",
    "Do not infer every pollutant's compliance from one composite index.",
    "Do not exchange CPCB coordination and SPCB consent enforcement.",
    "Do not merge environmental clearance with consent to operate.",
    "Do not universalise a source-apportionment share across seasons or cities.",
    "Do not report an NCAP target or action as measured attainment.",
    "Do not equate non-attainment status with a current AQI reading.",
    "Do not treat GRAP as India's long-term national clean-air programme.",
    "Do not infer live standards or PYQ answer keys from title-only pages.",
]

SESSION_TITLES = [
    "Ambient air and source emission standards",
    "Concentration exposure and averaging period",
    "Pollutants precursors and atmospheric formation",
    "Particulate matter size and composition",
    "Photochemical smog and ground-level ozone",
    "Acid deposition and precursor control",
    "NAAQS notification and data discipline",
    "AQI communication and statutory boundary",
    "CPCB SPCB and source consent architecture",
    "Monitoring stations and representativeness",
    "Source apportionment by place and season",
    "NCAP structural programme",
    "Targets action plans and measured attainment",
    "Non-attainment GRAP and CAQM",
    "Evidence-safe exam synthesis",
]

ANSWER_ROUTES = [
    "Identify the receiving-air standard before discussing a source limit.",
    "State concentration, unit and averaging period before making an exposure inference.",
    "Trace emitted substances through atmospheric chemistry to the measured pollutant.",
    "Use size fraction only for aerodynamic classification, not composition.",
    "Write the precursor-sunlight-secondary-oxidant chain.",
    "Separate precursor control from wet and dry deposition effects.",
    "Attach every number to the exact notification and measurement convention.",
    "Use AQI for communication and NAAQS for notified ambient compliance.",
    "Assign national coordination and local consent-enforcement roles correctly.",
    "Qualify monitoring evidence by station location, completeness and meteorology.",
    "Use city-season-pollutant-specific apportionment, never a universal share.",
    "Place NCAP beside, not above or instead of, the statutory framework.",
    "Move from target to action to monitored result without skipping stages.",
    "Separate status, episodic response and regional institution.",
    "Close with verified demand ownership and explicit data limits.",
]

PANELS = [
    panel("Ambient-emission firewall", "comparison-table", [
        "AMBIENT STANDARD -> concentration in outdoor receiving air",
        "SOURCE STANDARD -> release from a named stack, vehicle or process",
        "CONSENT CONDITION -> source-specific legal control",
        "AQI -> public communication index",
        "RULE -> never substitute one instrument for another",
    ], [FACTS[0][0], FACTS[1][0], FACTS[9][0]]),
    panel("Concentration-to-exposure chain", "process-flow", [
        "MONITOR -> pollutant concentration at place and time",
        "AVERAGING PERIOD -> fixes the measurement window",
        "PERSON LOCATION -> determines contact opportunity",
        "DURATION AND ROUTE -> shape exposure",
        "HEALTH CLAIM -> needs separate epidemiological evidence",
    ], [FACTS[2][0], FACTS[8][0]]),
    panel("Pollutant formation map", "process-flow", [
        "PRIMARY EMISSION -> released directly",
        "PRECURSOR -> enters atmospheric reaction",
        "SUNLIGHT OR OXIDATION -> transformation pathway",
        "SECONDARY POLLUTANT -> formed in air",
        "CONTROL -> address direct emissions and precursors",
    ], [FACTS[3][0], FACTS[4][0]]),
    panel("PM classification gate", "decision-gate", [
        "PM2.5 OR PM10 -> aerodynamic size fraction",
        "SIZE -> affects transport and deposition",
        "COMPOSITION -> requires chemical evidence",
        "SOURCE -> requires apportionment evidence",
        "TRAP -> size label alone proves neither composition nor source",
    ], [FACTS[5][0]]),
    panel("Smog and acid-deposition matrix", "comparison-table", [
        "SMOG -> precursor emissions plus sunlight-driven chemistry",
        "SURFACE OZONE -> secondary oxidant",
        "ACID DEPOSITION -> sulphur and nitrogen precursor pathway",
        "WET OR DRY -> deposition routes",
        "RULE -> precursor is not the final atmospheric product",
    ], [FACTS[6][0], FACTS[7][0]]),
    panel("NAAQS data gate", "decision-tree", [
        "POLLUTANT -> identify exact substance or fraction",
        "UNIT -> preserve the notified unit",
        "AVERAGING PERIOD -> annual, daily or shorter only if sourced",
        "AREA AND COMPLIANCE RULE -> read notification",
        "NO TABLE -> no invented limit",
    ], [FACTS[8][0]]),
    panel("AQI statutory boundary", "comparison-table", [
        "INPUT -> monitored pollutant concentrations",
        "OUTPUT -> public-facing category",
        "NAAQS -> notified ambient standard",
        "SOURCE LIMIT -> separate emission control",
        "VERDICT -> AQI category is not either standard table",
    ], [FACTS[9][0], FACTS[10][0]]),
    panel("Institution and clearance ladder", "hierarchy", [
        "CPCB -> national coordination and framework",
        "SPCB OR PCC -> consent, monitoring and enforcement",
        "CTE OR CTO -> source-operation permission layer",
        "ENVIRONMENTAL CLEARANCE -> prior project-appraisal layer",
        "RULE -> approvals remain legally distinct",
    ], [FACTS[11][0], FACTS[12][0]]),
    panel("Monitoring evidence ladder", "layered-rail", [
        "STATION -> one location",
        "NETWORK -> spatial coverage",
        "DATA COMPLETENESS -> usable time record",
        "METEOROLOGY -> dispersion and accumulation context",
        "INFERENCE -> scale only as far as evidence supports",
    ], [FACTS[13][0]]),
    panel("Source-apportionment cube", "comparison-table", [
        "CITY -> source mix changes by location",
        "SEASON -> activity and meteorology change",
        "POLLUTANT -> PM, ozone and gases have different pathways",
        "METHOD -> model and sampling assumptions matter",
        "NO UNIVERSAL SHARE -> date and scope every estimate",
    ], [FACTS[14][0]]),
    panel("Programme-response architecture", "comparison-table", [
        "NCAP -> long-run structural planning",
        "NON-ATTAINMENT -> standards-based classification over a period",
        "GRAP -> episodic graded response",
        "CAQM -> statutory Delhi-NCR regional coordination",
        "NO SUBSTITUTION -> each serves a different function",
    ], [FACTS[15][0], FACTS[17][0], FACTS[18][0]]),
    panel("Evidence and answer spine", "answer-spine", [
        "DEFINE -> ambient, emission, concentration and exposure",
        "TRACE -> source, precursor, atmospheric formation and receptor",
        "GOVERN -> NAAQS, AQI, consent, NCAP, GRAP and CAQM",
        "MEASURE -> station, averaging period and apportionment boundary",
        "AUDIT -> target, attainment, current data and PYQ key stay distinct",
    ], [FACTS[16][0], FACTS[19][0]]),
]

TOPIC_13 = common.topic(
    13,
    "Air Pollution and CPCB Standards",
    "13_Air-Pollution-and-CPCB-Standards",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-13_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish ambient air-quality standards from source-emission standards.", [0, 1, 8]),
        (10, "Explain why AQI cannot be treated as the NAAQS compliance table.", [8, 9, 10]),
        (15, "Explain pollutant formation from primary emissions and precursors.", [3, 4, 5, 6, 7]),
        (15, "Assess monitoring and source-apportionment limits in city air policy.", [2, 13, 14]),
        (20, "Evaluate India's statutory, programme and episodic air-governance layers.", [0, 11, 12, 15, 16, 17, 18]),
        (20, "Build a source-to-exposure clean-air strategy without unsupported numbers.", [1, 2, 3, 8, 13, 14, 16, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "ambient standard", "source-emission standard", "concentration",
        "exposure", "pollutant", "precursor", "primary pollutant",
        "secondary pollutant", "PM2.5", "PM10", "photochemical smog",
        "ground-level ozone", "acid deposition", "averaging period",
        "NAAQS", "AQI", "CPCB", "SPCB", "NCAP", "GRAP", "CAQM",
    ],
    (
        "Audited ledgers route direct Mains demands on NCAP, WHO air-quality "
        "guidelines and photochemical smog, plus objective demands on biomass "
        "burning, benzene, coal combustion, sulphur and nitrogen precursors, "
        "PM-related sources and cloud seeding. Objective keys are not inferred."
    ),
    [],
    AIR_POLLUTION_LIVE_SOURCE_ATTEMPTS,
    (
        "Official CPCB air-quality and AQI paths returned title-only pages or "
        "a 404 display route on 2026-09-03. Consequently no ambient or emission "
        "standard, unit, averaging period, AQI breakpoint, live reading, source "
        "share, NCAP target or attainment figure was imported."
    ),
    extra=[
        "basic/16_Environmental-Impact-Assessment-and-NGT.md",
        "basic/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
        "advanced/16_Environmental-Impact-Assessment-and-NGT.md",
        "advanced/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
    ],
    pyq_audit_heading="AUDITED AIR-POLLUTION, NCAP, SMOG AND AQI PYQ OWNERSHIP",
    allow_existing_history=True,
    register_headings=(
        "AMBIENT, EMISSION, CONCENTRATION, EXPOSURE AND PRECURSOR MAP",
        "NAAQS, AQI, MONITORING, APPORTIONMENT AND PROGRAMME TRAPS",
        "AIR-POLLUTION GOVERNANCE ANSWER SPINE",
        "LIVE STANDARD, BREAKPOINT, SOURCE-SHARE AND PYQ EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "IDENTIFY THE RECEIVING MEDIUM, POLLUTANT AND SOURCE",
        "SEPARATE AMBIENT STANDARD FROM SOURCE-EMISSION STANDARD",
        "STATE UNIT AND AVERAGING PERIOD BEFORE USING A CONCENTRATION",
        "TRACE PRIMARY EMISSION, PRECURSOR AND SECONDARY FORMATION",
        "ASSIGN CPCB, SPCB, NCAP, GRAP AND CAQM THEIR DISTINCT ROLES",
        "DATE EVERY TARGET, APPORTIONMENT RESULT AND ATTAINMENT CLAIM",
        "CONCLUDE WITH SOURCE CONTROL, MONITORING AND EXPOSURE REDUCTION",
    ],
)
