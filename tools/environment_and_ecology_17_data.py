"""Authored data for Environment and Ecology learner-v2 Topic 17."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import (
    CLIMATE_SCIENCE_LIVE_SOURCE_ATTEMPTS,
    panel,
)


FACTS = [
    ("Natural greenhouse effect", "The natural greenhouse effect is a life-enabling energy-balance process in which greenhouse gases absorb and re-emit part of Earth's outgoing longwave radiation; it is not the anthropogenic problem to be eliminated."),
    ("Enhanced anthropogenic forcing", "Current climate concern arises from human activities increasing greenhouse-gas concentrations and other forcing agents, thereby altering the climate system beyond the natural greenhouse effect."),
    ("Shortwave-longwave distinction", "Incoming solar energy is predominantly shortwave, whereas the warmed surface emits longwave infrared radiation; greenhouse gases interact with the outgoing longwave part of this energy flow."),
    ("Emission-concentration distinction", "An emission is a flow released during a period, while atmospheric concentration is the resulting abundance after sources, sinks, chemistry and lifetime act; the two quantities are related but not interchangeable."),
    ("Stock-flow distinction", "Long-lived greenhouse gases create a stock problem because accumulated past and present emissions influence concentration; lowering an annual flow does not by itself remove the existing atmospheric stock."),
    ("Forcing-feedback distinction", "Radiative forcing is an imposed change to the climate system's energy balance, while a feedback is a response triggered by climate change that amplifies or dampens the initial change."),
    ("Feedback sign", "A positive climate feedback amplifies an initial change and a negative feedback dampens it; positive and negative describe direction, not whether the outcome is desirable."),
    ("Water-vapour boundary", "Water vapour is a major greenhouse gas and generally operates as a feedback in contemporary warming because atmospheric moisture responds strongly to temperature; it is not a substitute for tracing the initiating anthropogenic forcing."),
    ("Aerosol-black-carbon boundary", "Many aerosols exert a cooling influence through scattering and cloud effects, while black carbon absorbs radiation and can reduce snow or ice albedo; 'aerosol' does not imply one universal forcing sign."),
    ("GWP time horizon", "Global Warming Potential compares integrated radiative influence relative to carbon dioxide over a specified time horizon; a GWP claim without its horizon is incomplete."),
    ("Potency-lifetime distinction", "Heat-trapping potency per unit mass and atmospheric persistence are different properties; a short-lived strong forcer and a long-lived cumulative gas require different mitigation reasoning."),
    ("Weather-climate distinction", "Weather describes short-period atmospheric conditions, whereas climate concerns statistical patterns over longer periods; one unusual season or event does not alone establish a climate trend."),
    ("Variability-trend distinction", "Natural variability can raise or lower conditions around a long-term trend, so short-term fluctuation neither proves nor disproves the underlying climate tendency."),
    ("Detection-attribution distinction", "Detection asks whether an observed change is distinguishable from expected variability, while attribution evaluates the relative contributions of human and natural drivers using multiple lines of evidence."),
    ("Event-attribution boundary", "Event attribution estimates how human-caused climate change altered the probability or intensity of a defined event class; it does not justify saying that every individual disaster was caused solely by climate change."),
    ("Observation-projection distinction", "An observation describes measured past or present change, whereas a model projection is a conditional statement about a future pathway under specified assumptions."),
    ("Scenario-not-forecast", "A climate scenario is a coherent conditional pathway used to explore possible futures; it is not an unconditional prediction that a particular future will occur."),
    ("Mitigation-adaptation distinction", "Mitigation addresses sources or enhances sinks to limit climate change, whereas adaptation adjusts human or natural systems to actual or expected impacts; neither term is a synonym for all climate action."),
    ("Sink-source and gross-net", "A sink absorbs more of a substance than it releases over the stated boundary and period, while a source releases more; gross removals, gross emissions and net balance must be kept separate."),
    ("Impact and evidence boundary", "Ocean acidification follows carbon-dioxide uptake and chemistry, while warming and sea-level impacts involve additional mechanisms; global findings, India-specific evidence, observed attribution and future projections must be cited at their proper scale."),
]

TRAPS = [
    "Do not describe the natural greenhouse effect itself as the human-caused problem.",
    "Do not merge an emissions flow with an atmospheric concentration or accumulated stock.",
    "Do not call a feedback an external forcing or treat positive as beneficial.",
    "Do not present water vapour as the initiating anthropogenic driver without qualification.",
    "Do not assign every aerosol the same warming or cooling sign.",
    "Do not quote GWP without its assessment basis and time horizon.",
    "Do not confuse potency per unit mass with atmospheric lifetime or cumulative importance.",
    "Do not use one weather event as proof or disproof of a climate trend.",
    "Do not convert event-attribution probability into sole-cause language.",
    "Do not present an observation as a projection or a scenario as a forecast.",
    "Do not merge mitigation with adaptation.",
    "Do not merge gross emissions, gross removals and a net balance.",
    "Do not downscale a global finding into an India-specific number without an Indian source.",
    "Do not invent a temperature, forcing, concentration, emissions or carbon-budget value.",
    "Do not detach calibrated confidence or likelihood wording from its cited assessment.",
]

SESSION_TITLES = [
    "Natural greenhouse effect and anthropogenic enhancement",
    "Shortwave longwave and planetary energy balance",
    "Emissions and concentrations",
    "Atmospheric stocks and emissions flows",
    "Radiative forcing and feedback distinction",
    "Feedback sign and water-vapour role",
    "Aerosols black carbon and forcing diversity",
    "GWP horizon and comparison metric",
    "Potency and atmospheric lifetime",
    "Weather and climate distinction",
    "Variability detection and attribution",
    "Event attribution without sole-cause claims",
    "Observed change versus model projection",
    "Scenarios mitigation and adaptation boundaries",
    "Sinks sources gross net impacts and evidence synthesis",
]

ANSWER_ROUTES = [
    "Open by preserving the natural process and identifying the human enhancement.",
    "Trace incoming shortwave, surface warming and outgoing longwave before naming gases.",
    "State the unit, period and reservoir before moving from emissions to concentration.",
    "Explain why reducing a flow and reducing an accumulated atmospheric stock are different tasks.",
    "Identify the imposed forcing first and the climate-system feedback second.",
    "Name the feedback sign and separate water vapour from the initiating forcing.",
    "Separate scattering aerosols, absorbing particles and spatially uneven effects.",
    "Pair every GWP comparison with its stated time horizon.",
    "Keep potency per unit mass separate from atmospheric persistence.",
    "Use long-term statistics for climate rather than one weather event.",
    "Retain natural variability while testing detection and competing drivers.",
    "Describe altered event probability or intensity, not a single exclusive cause.",
    "Label measured history and conditional future output separately.",
    "Separate scenario, mitigation and adaptation before selecting a response.",
    "Close with gross-net accounting, impact mechanism, scale and evidence limits.",
]

PANELS = [
    panel("Greenhouse-effect firewall", "comparison-table", [
        "NATURAL EFFECT -> absorbs and re-emits outgoing longwave radiation",
        "FUNCTION -> maintains a habitable energy balance",
        "HUMAN ENHANCEMENT -> raises concentrations and net forcing",
        "CLIMATE RESPONSE -> warming plus wider system changes",
        "EXAM RULE -> preserve the natural-versus-enhanced distinction",
    ], [FACTS[0][0], FACTS[1][0], FACTS[2][0]]),
    panel("Energy-balance rail", "process-flow", [
        "SUN -> incoming predominantly shortwave energy",
        "SURFACE -> absorbs part and warms",
        "EARTH -> emits outgoing longwave infrared energy",
        "GREENHOUSE GASES -> absorb and re-emit part of longwave flow",
        "IMBALANCE -> forcing changes energy retained by the climate system",
    ], [FACTS[2][0], FACTS[5][0]]),
    panel("Emission-to-concentration ledger", "layered-rail", [
        "ACTIVITY -> emissions flow during a stated period",
        "ATMOSPHERE -> concentration after sources and sinks interact",
        "ACCUMULATION -> long-lived gases build an atmospheric stock",
        "FLOW CUT -> slows addition but does not erase the stock",
        "REMOVAL -> changes the stock only within a stated boundary",
    ], [FACTS[3][0], FACTS[4][0], FACTS[18][0]]),
    panel("Forcing-feedback fork", "decision-tree", [
        "EXTERNAL OR IMPOSED ENERGY CHANGE -> radiative forcing",
        "CLIMATE RESPONSE TRIGGERED -> feedback",
        "AMPLIFIES INITIAL CHANGE -> positive feedback",
        "DAMPENS INITIAL CHANGE -> negative feedback",
        "SIGN -> direction of response, never moral value",
    ], [FACTS[5][0], FACTS[6][0]]),
    panel("Water and particle matrix", "comparison-table", [
        "WATER VAPOUR -> greenhouse gas commonly acting as feedback",
        "SULPHATE-LIKE AEROSOLS -> often cooling influence",
        "BLACK CARBON -> absorbing warming influence",
        "SNOW OR ICE DEPOSITION -> can lower albedo",
        "BOUNDARY -> agent, location and mechanism determine the sign",
    ], [FACTS[7][0], FACTS[8][0]]),
    panel("Gas comparison gate", "comparison-table", [
        "GWP -> relative integrated influence over a named horizon",
        "POTENCY -> effect per unit mass under the metric",
        "LIFETIME -> persistence in the atmosphere",
        "EMISSION SCALE -> quantity released",
        "POLICY -> near-term and cumulative levers are not identical",
    ], [FACTS[9][0], FACTS[10][0]]),
    panel("Weather-to-climate ladder", "hierarchy", [
        "EVENT -> individual weather occurrence",
        "SEASON OR YEAR -> short-period variability",
        "DISTRIBUTION -> frequency, intensity and pattern",
        "LONGER RECORD -> climate trend assessment",
        "RULE -> fluctuation around a trend is not trend reversal",
    ], [FACTS[11][0], FACTS[12][0]]),
    panel("Attribution evidence chain", "process-flow", [
        "OBSERVATION -> define the measured change",
        "DETECTION -> distinguish signal from expected variability",
        "DRIVERS -> compare human and natural influences",
        "MODELS PLUS PHYSICS PLUS RECORDS -> converging evidence",
        "ATTRIBUTION -> qualified contribution, not slogan causation",
    ], [FACTS[13][0], FACTS[14][0]]),
    panel("Event-claim firewall", "decision-gate", [
        "DEFINE EVENT CLASS -> place, duration and metric",
        "COMPARE WORLDS -> with and without human influence",
        "ESTIMATE CHANGE -> probability or intensity",
        "RETAIN OTHER DRIVERS -> exposure, vulnerability and variability",
        "NO SOLE CAUSE -> disaster impact is multi-causal",
    ], [FACTS[14][0]]),
    panel("Observation-projection matrix", "comparison-table", [
        "OBSERVATION -> measured past or present",
        "ATTRIBUTION -> explanation of observed change",
        "SCENARIO -> conditional assumptions",
        "PROJECTION -> modelled response under a scenario",
        "FORECAST -> different claim with a prediction horizon",
    ], [FACTS[15][0], FACTS[16][0]]),
    panel("Climate-response fork", "decision-tree", [
        "SOURCE REDUCTION -> mitigation",
        "SINK ENHANCEMENT -> mitigation with accounting boundary",
        "EXPOSURE OR VULNERABILITY REDUCTION -> adaptation",
        "RESIDUAL HARM -> separate loss-and-damage question",
        "PORTFOLIO -> mitigation and adaptation are complementary",
    ], [FACTS[17][0], FACTS[18][0]]),
    panel("Science answer spine", "answer-spine", [
        "DEFINE -> natural effect, human enhancement and energy flow",
        "ACCOUNT -> emissions, concentrations, stock and net balance",
        "EXPLAIN -> forcing, feedback and gas-specific properties",
        "EVALUATE -> trend, detection, attribution and projection",
        "QUALIFY -> scale, scenario, confidence and no invented figures",
    ], [FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2022", "GS-III",
        "Discuss global-warming greenhouse-gas effects before linking measures under Kyoto.",
        "Verified routed Mains demand; treaty measures are cross-owned by Topic 19.",
        [0, 1, 3, 5, 9, 17],
    ),
    common.make_pyq_solution(
        FACTS, "2023", "GS-I",
        "Discuss consequences of climate change for food security in tropical countries.",
        "Verified routed Mains demand; no official model answer is claimed.",
        [11, 12, 13, 15, 17, 19],
    ),
    common.make_pyq_solution(
        FACTS, "2025", "GS-I",
        "Discuss climate change and sea-level rise affecting island nations.",
        "Verified routed Mains demand; no local projection figure is inferred.",
        [13, 15, 16, 17, 19],
    ),
]

TOPIC_17 = common.topic(
    17,
    "Climate Change Science Greenhouse Effect",
    "17_Climate-Change-Science-Greenhouse-Effect",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-17_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish the natural greenhouse effect from enhanced anthropogenic forcing.", [0, 1, 2]),
        (10, "Differentiate emissions, concentrations, stocks and flows in climate accounting.", [3, 4, 18]),
        (15, "Explain radiative forcing, feedbacks and gas-specific climate metrics.", [5, 6, 7, 8, 9, 10]),
        (15, "Distinguish climate trend, detection, attribution and event attribution.", [11, 12, 13, 14]),
        (20, "Evaluate how climate science should translate into mitigation and adaptation policy.", [1, 3, 5, 9, 10, 15, 16, 17]),
        (20, "Build an evidence-safe climate-change answer from mechanism to impacts.", [0, 2, 4, 6, 8, 12, 14, 15, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "natural greenhouse effect", "enhanced anthropogenic forcing",
        "shortwave", "longwave", "emission", "concentration", "stock",
        "flow", "radiative forcing", "feedback", "water vapour",
        "aerosol", "black carbon", "Global Warming Potential",
        "time horizon", "weather", "climate trend", "detection",
        "attribution", "scenario", "projection", "mitigation",
        "adaptation", "gross removals", "net balance", "ocean acidification",
    ],
    (
        "Audited ledgers route objective demands on carbon fertilisation, "
        "geoengineering, methane hydrates, agricultural gases, rice practices, "
        "cement emissions and India's carbon-dioxide profile, plus verified Mains "
        "demands on greenhouse-gas effects, tropical food security and island "
        "sea-level risk. Objective keys are not inferred."
    ),
    PYQ_SOLUTIONS,
    CLIMATE_SCIENCE_LIVE_SOURCE_ATTEMPTS,
    (
        "Official IPCC retrieval substantively supported only broad observed-versus-"
        "future and action distinctions; the AR6 landing page was title-only, an "
        "IPCC fact-sheet URL returned 404 and AR7 material was treated as process, "
        "not findings. No temperature, anomaly, forcing, GWP, emissions, "
        "concentration, budget, scenario or projection number was imported."
    ),
    extra=[
        "basic/02_Biogeochemical-Cycles-and-Ecological-Pyramids.md",
        "basic/13_Air-Pollution-and-CPCB-Standards.md",
        "basic/18_IPCC-Assessment-Reports.md",
        "basic/19_UNFCCC-COP-Kyoto-Paris-Agreement.md",
        "advanced/02_Biogeochemical-Cycles-and-Ecological-Pyramids.md",
        "advanced/13_Air-Pollution-and-CPCB-Standards.md",
    ],
    pyq_audit_heading="AUDITED CLIMATE-SCIENCE, ATTRIBUTION, IMPACT AND RESPONSE PYQ OWNERSHIP",
    allow_existing_history=True,
    register_headings=(
        "GREENHOUSE EFFECT, ENERGY BALANCE, EMISSIONS AND STOCK-FLOW MAP",
        "FORCING, FEEDBACK, METRIC, ATTRIBUTION AND SCENARIO TRAPS",
        "CLIMATE-SCIENCE ANSWER SPINE",
        "LIVE FIGURE, CONFIDENCE, PROJECTION AND SCALE EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "DISTINGUISH THE NATURAL GREENHOUSE EFFECT FROM HUMAN ENHANCEMENT",
        "TRACE SHORTWAVE INPUT, LONGWAVE OUTPUT AND RADIATIVE FORCING",
        "SEPARATE EMISSIONS FLOW, CONCENTRATION AND ACCUMULATED STOCK",
        "SEPARATE FORCING FROM FEEDBACK AND NAME THE FEEDBACK SIGN",
        "DISTINGUISH WEATHER VARIABILITY, CLIMATE TREND AND ATTRIBUTION",
        "LABEL OBSERVATION, SCENARIO AND CONDITIONAL PROJECTION",
        "CLOSE WITH MITIGATION, ADAPTATION, SCALE AND EVIDENCE LIMITS",
    ],
)
