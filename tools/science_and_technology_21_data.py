"""Authored learner-v2 data for Science and Technology Topic 21."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.bipm.org/en/measurement-units - fetched 2026-09-04; "
        "the official BIPM page confirmed the seven SI base units and examples "
        "of derived-unit relations. It was used only for unit and dimensional "
        "discipline, not to infer instrument accuracy or calibration status."
    ),
    (
        "https://www.nobelprize.org/prizes/physics/2023/press-release/ - "
        "fetched 2026-09-04; the official release confirmed the 3 October 2023 "
        "award for experimental methods generating attosecond light pulses to "
        "study electron dynamics. Potential applications were not converted "
        "into deployed diagnostic or electronics outcomes."
    ),
    (
        "https://www.nobelprize.org/prizes/physics/2024/press-release/ - "
        "fetched 2026-09-04; the official release confirmed the 8 October 2024 "
        "award for physics-enabled foundations of machine learning. It was "
        "retained as a dated physics-to-AI bridge, not evidence of a particular "
        "Indian programme, model performance or deployment result."
    ),
    (
        "https://ism.gov.in/schemes/semicon2.0/index - fetched 2026-09-04; "
        "the official India Semiconductor Mission page exposed design-support "
        "and semiconductor-ecosystem provisions. A scheme provision was not "
        "rewritten as a fabricated chip, operating facility or measured output."
    ),
    (
        "https://ism.gov.in/semicon-india-2026 - fetched 2026-09-04; the "
        "official page listed SEMICON India 2026 for 17-19 September 2026 and "
        "the theme 'Silicon to Systems : Building the Ecosystem'. Because that "
        "date was still future on retrieval, the listing was not presented as "
        "a completed event or as proof of manufacturing capability."
    ),
]


def _topic_21() -> dict[str, object]:
    facts = [
        ("SI units and dimensional boundary", "The SI uses metre, kilogram, second, ampere, kelvin, mole and candela as base units; derived units express products of powers of base units, including hertz as inverse second, joule as kilogram metre squared per second squared and watt as kilogram metre squared per second cubed. Dimensional analysis can test consistency but cannot prove that a physical equation, measurement or causal claim is correct; a light-year is a unit of distance, not time."),
        ("Motion acceleration and measurement", "Distance and speed are scalars, while displacement, velocity and acceleration require direction; an accelerometer senses acceleration and can support motion, tilt, free-fall or crash detection, but a sensor reading still requires calibration, orientation and system interpretation."),
        ("Force momentum impulse and Newton laws", "Newton's first law defines inertia, the second links net force to the rate of change of momentum and becomes F = ma for constant mass, and the third pairs equal and opposite forces on different bodies; impulse equals change in momentum and explains why increasing stopping time can reduce average force."),
        ("Work energy and power", "Work transfers energy when force has a displacement component along its direction; the work-energy theorem links net work to change in kinetic energy, while power is the rate of doing work or transferring energy. Force, energy and power therefore have different dimensions and cannot be interchanged."),
        ("Gravitation circular motion and orbits", "Gravity supplies the centripetal acceleration of an orbiting body; orbital weightlessness is continuous free fall, not absence of gravity. The Basic owner gives Earth's escape velocity as approximately 11.2 km/s and a geostationary orbit as approximately 35,786 km above the equator with one sidereal-day period; escape velocity is independent of projectile mass, while polar or sun-synchronous orbits occupy a different plane and application class."),
        ("Pressure buoyancy and fluid principles", "Pressure is force per unit area; Pascal's law transmits applied pressure in a confined fluid, Archimedes' principle links buoyant force to the weight of displaced fluid, and Bernoulli's principle relates pressure and flow under its assumptions. Surface tension shapes droplets and capillarity supports liquid rise in narrow spaces; a pressure cooker raises boiling temperature by raising pressure, whereas lower atmospheric pressure lowers boiling temperature at altitude."),
        ("Heat temperature specific and latent heat", "Temperature describes thermal state and is not heat; heat is energy transferred because of a temperature difference. Specific heat compares energy required for a temperature rise, while latent heat is absorbed or released during a phase change without a temperature change."),
        ("Thermodynamics and heat transfer", "Conduction, convection and radiation are distinct heat-transfer modes, and radiation needs no material medium. The first law applies energy conservation to thermal systems; the second law fixes spontaneous heat flow from hotter to colder bodies and rules out a perfectly efficient heat engine. An ideal black body absorbs and emits across wavelengths, and hotter bodies shift peak emission toward shorter wavelengths."),
        ("Wave relation and sound", "A wave transfers energy without net transport of matter, with speed equal to frequency multiplied by wavelength. Sound is mechanical and travels fastest in solids and slowest in gases; frequency primarily sets pitch, amplitude affects loudness, Doppler shift follows relative motion, and resonance amplifies forced oscillation near natural frequency. Infrasound is below 20 Hz, audible sound spans about 20 Hz to 20 kHz and ultrasound is above 20 kHz; ultrasound must not be confused with supersonic motion, while echo and reverberation differ by time separation."),
        ("Electromagnetic spectrum and communication boundary", "In increasing frequency the electromagnetic spectrum runs radio, microwave, infrared, visible, ultraviolet, X-rays and gamma rays; all travel at light speed in vacuum but interact differently with matter. Microwaves, infrared thermal sensing and ionising X-ray or gamma uses require band-specific treatment; radar uses radio waves, visible-light communication uses modulated visible light, and short-range wireless labels require technology-specific range and protocol evidence."),
        ("Reflection mirrors and image logic", "Reflection obeys equality of incidence and reflection angles; plane, concave and convex mirrors form images according to geometry and object position. Mirror action is reflection, so it must not be explained through the refraction mechanism used by lenses."),
        ("Refraction total internal reflection and lenses", "Refraction follows a change in light speed across a boundary while frequency remains unchanged; total internal reflection requires travel from denser to rarer medium beyond the critical angle and underpins optical fibres. Convex and concave lenses converge and diverge respectively, with myopia corrected by a concave lens, hypermetropia by a convex lens, presbyopia commonly by bifocals and astigmatism by cylindrical lenses. Dispersion separates colours, Rayleigh scattering favours shorter wavelengths, Mie scattering acts with larger particles and the Tyndall effect reveals colloids."),
        ("Current voltage resistance and Ohm boundary", "Electric current is charge flow per unit time, potential difference is work per unit charge and resistance opposes current. Ohm's law V = IR applies under stated physical conditions to ohmic conductors, so it is not a universal description of every material or device."),
        ("Circuits electrical power and safety", "Series branches share current and parallel branches share voltage; domestic loads are connected in parallel. Electrical power can be written VI under the relevant circuit conditions, transmission loss rises with I squared R, and fuse or MCB protection and earthing perform different safety functions. Below a critical temperature, superconductors show zero electrical resistance and the Meissner effect, supporting specialised magnets rather than ordinary room-temperature wiring claims."),
        ("Magnetism induction motors generators and transformers", "Changing magnetic flux induces an emf; generators convert mechanical to electrical energy, motors convert electrical to mechanical energy, and transformers use mutual induction to change AC voltage. A steady DC supply does not provide the changing flux needed for ordinary transformer action."),
        ("Atomic quantum photoelectric and Bose boundary", "Atomic and quantum physics require discrete states and particle-wave behaviour beyond classical mechanics; the photoelectric effect requires light above a threshold frequency, while Bose-Einstein statistics applies to indistinguishable integer-spin particles that may share a quantum state. Antimatter, neutrinos and the Higgs field are distinct modern-physics concepts; none should be reduced to brightness, treated as interchangeable or extended to every particle."),
        ("Nuclear radioactivity fission and fusion", "Alpha radiation is a helium nucleus, beta commonly involves an electron or positron, and gamma is electromagnetic radiation; alpha is strongly ionising but weakly penetrating relative to gamma, whose penetration is much greater. Half-life is a nuclear decay property unaffected by ordinary temperature or pressure and supports radioisotope dating such as carbon-14, while fission splits heavy nuclei and fusion joins light nuclei."),
        ("Relativity gravitational waves and astronomy", "Special relativity sets light speed as the information-speed limit and relates mass and energy, while general relativity describes gravitation through spacetime geometry and predicts effects including gravitational waves. A gravitational-wave observation or black-hole merger inference depends on instruments and analysis; Cepheids, nebulae and pulsars are distinct astronomical objects or phenomena."),
        ("Semiconductors LEDs lasers radar and VLC", "Pentavalent doping produces n-type material with electrons as majority carriers, trivalent doping produces p-type material with holes as majority carriers, and a p-n junction enables rectification, LEDs and photovoltaic behaviour. A bipolar transistor uses base current while a MOSFET uses an insulated gate field to control conduction; lasers rely on stimulated emission, coherence, near-monochromaticity and directionality, radar uses radio waves, and VLC uses visible light. No device label alone establishes efficiency, range or suitability."),
        ("Metrology recorder and status firewall", "CSIR-NPL anchors measurement standards and metrology; CSIR-CEERI supports electronics and device research, while ISM, the National Quantum Mission and the DAE or BARC ecosystem connect physics to policy and application. Accelerometers, radar and crash-survivable flight recorders perform different sensing, detection or preservation functions, and underwater recovery adds a separate location problem. A standard, laboratory result, announced scheme, scheduled event, detected signal, calibrated reading, operational device and verified public outcome are separate evidence rungs."),
    ]
    traps = [
        "Do not treat dimensional consistency as proof that an equation or claim is physically correct.",
        "Do not merge distance with displacement, speed with velocity or sensor output with a verified event.",
        "Do not place Newton's third-law force pair on the same body.",
        "Do not use work, energy and power as synonyms.",
        "Do not explain orbital weightlessness as absence of gravity or make escape velocity depend on projectile mass.",
        "Do not reverse the pressure-cooker and high-altitude boiling effects.",
        "Do not confuse temperature with heat or sensible heat with latent heat.",
        "Do not claim radiation heat transfer needs a material medium or that a heat engine can be perfectly efficient.",
        "Do not merge pitch with loudness, ultrasound with supersonic motion or sound with an electromagnetic wave.",
        "Do not reorder the electromagnetic spectrum or label every wireless system as radar.",
        "Do not explain a mirror through refraction or a lens through reflection alone.",
        "Do not claim refraction changes frequency across an ordinary stationary boundary.",
        "Do not say current is consumed as a substance or apply Ohm's law without its conditions.",
        "Do not claim a steady DC supply can be stepped by an ordinary transformer.",
        "Do not convert a standard, award, scheduled event, detected signal or scheme provision into an operational outcome.",
    ]
    titles = [
        "SI units dimensions motion vectors and accelerometers",
        "Newton laws momentum impulse and collision safety",
        "Work energy power and dimensional distinctions",
        "Gravitation circular motion satellites and orbital weightlessness",
        "Pressure buoyancy fluid flow and pressure cookers",
        "Heat temperature phase change and thermodynamic laws",
        "Waves sound Doppler resonance and ultrasound",
        "Electromagnetic spectrum radar VLC and wireless boundaries",
        "Reflection mirrors and image formation",
        "Refraction total internal reflection lenses and vision",
        "Current voltage resistance circuits power and electrical safety",
        "Magnetism induction motors generators and transformers",
        "Atomic quantum photoelectric effect and Bose-Einstein statistics",
        "Nuclear radiation relativity gravitational waves and astronomy",
        "Semiconductors LEDs lasers instruments metrology and status",
    ]
    routes = [
        "Name the quantity, scalar or vector character, SI unit and dimensional limit before interpreting an accelerometer reading.",
        "Trace external net force to momentum change and use impulse to explain a safety application.",
        "Separate energy transferred from the rate of transfer and test units without treating dimensions as proof.",
        "Identify gravity as centripetal cause, classify the orbit and preserve the free-fall boundary.",
        "Choose Pascal, Archimedes or Bernoulli only after fixing pressure, displacement and flow assumptions.",
        "Separate thermal state, energy transfer, phase change, transfer mode and thermodynamic direction.",
        "Fix medium, frequency, wavelength, amplitude and relative motion before selecting a sound application.",
        "Locate the radiation band and mechanism before asserting range, penetration or communication use.",
        "Draw the incident and reflected rays before classifying mirror image behaviour.",
        "Trace speed change, ray bending and lens type before linking the optical correction or fibre application.",
        "Move from charge and potential difference to resistance, topology, power and distinct safety devices.",
        "Require changing magnetic flux, then separate motor, generator and transformer energy conversion.",
        "Distinguish classical, quantum and statistical claims before linking the principle to a device or research field.",
        "Classify radiation or relativistic evidence, then state the instrument and observational limitation.",
        "Move from material and junction physics to device, measurement institution and the last verified capability rung.",
    ]
    panels = [
        panel("Quantity unit and vector decision tree", "decision-tree", [
            "QUANTITY -> scalar or vector?",
            "UNIT -> base or derived SI?",
            "DIMENSION -> consistency check only",
            "INSTRUMENT -> calibration + orientation + uncertainty",
            "LIGHT-YEAR -> distance, never time",
        ], [facts[0][0], facts[1][0]]),
        panel("Mechanics cause-and-rate rail", "cause-rate-rail", [
            "NET FORCE -> momentum change",
            "IMPULSE -> force x time -> change in momentum",
            "FORCE + DISPLACEMENT -> work",
            "NET WORK -> kinetic-energy change",
            "POWER -> work or energy per time",
        ], [facts[2][0], facts[3][0]]),
        panel("Orbit and free-fall map", "orbit-map", [
            "GRAVITY -> centripetal acceleration",
            "ORBIT -> continuous free fall",
            "GEOSTATIONARY -> equatorial + matching rotation period",
            "POLAR / SUN-SYNCHRONOUS -> near-polar low-orbit family",
            "ESCAPE VELOCITY -> central body's mass and radius",
        ], [facts[4][0]]),
        panel("Fluid-principle selection matrix", "selection-matrix", [
            "PASCAL -> confined-fluid pressure transmission",
            "ARCHIMEDES -> displaced-fluid weight and upthrust",
            "BERNOULLI -> pressure-flow relation under assumptions",
            "PRESSURE COOKER -> pressure up, boiling temperature up",
            "ALTITUDE -> pressure down, boiling temperature down",
        ], [facts[5][0]]),
        panel("Thermal state and transfer ladder", "thermal-ladder", [
            "TEMPERATURE -> thermal state",
            "HEAT -> transfer due to temperature difference",
            "SPECIFIC HEAT -> temperature-change requirement",
            "LATENT HEAT -> phase change without temperature change",
            "CONDUCTION | CONVECTION | RADIATION -> distinct routes",
        ], [facts[6][0], facts[7][0]]),
        panel("Wave sound and spectrum bands", "banded-spectrum", [
            "WAVE -> speed = frequency x wavelength",
            "SOUND -> medium required",
            "INFRASOUND | AUDIBLE | ULTRASOUND -> frequency classes",
            "RADIO -> MICROWAVE -> IR -> VISIBLE -> UV -> X-RAY -> GAMMA",
            "RADAR / VLC -> different electromagnetic bands",
        ], [facts[8][0], facts[9][0]]),
        panel("Mirror lens and fibre ray logic", "ray-logic", [
            "MIRROR -> reflection",
            "LENS -> refraction",
            "CONVEX LENS -> converging",
            "CONCAVE LENS -> diverging",
            "DENSER TO RARER + CRITICAL ANGLE -> total internal reflection",
        ], [facts[10][0], facts[11][0]]),
        panel("Circuit topology and safety board", "circuit-board", [
            "VOLTAGE -> work per charge",
            "CURRENT -> charge per time",
            "RESISTANCE -> opposition to current",
            "SERIES -> common current | PARALLEL -> common voltage",
            "FUSE / MCB -> overload | EARTHING -> shock protection",
        ], [facts[12][0], facts[13][0]]),
        panel("Electromagnetic conversion loop", "conversion-loop", [
            "CHANGING FLUX -> induced emf",
            "GENERATOR -> mechanical to electrical",
            "TRANSFORMER -> AC voltage conversion",
            "MOTOR -> electrical to mechanical",
            "STEADY DC -> no ordinary transformer action",
        ], [facts[14][0]]),
        panel("Quantum and nuclear split panel", "split-panel", [
            "PHOTOELECTRIC -> threshold frequency",
            "BOSE-EINSTEIN -> integer-spin bosons may share state",
            "ALPHA | BETA | GAMMA -> different matter/radiation classes",
            "HALF-LIFE -> nuclear decay clock",
            "FISSION != FUSION",
        ], [facts[15][0], facts[16][0]]),
        panel("Relativity observation evidence chain", "evidence-chain", [
            "RELATIVITY -> spacetime prediction",
            "GRAVITATIONAL WAVE -> instrument signal",
            "ANALYSIS -> source inference",
            "CEPHEID | NEBULA | PULSAR -> distinct astronomy labels",
            "OBSERVATION -> bounded claim, not omniscience",
        ], [facts[17][0]]),
        panel("Device to verified-status staircase", "status-staircase", [
            "MATERIAL -> DOPING -> JUNCTION -> DEVICE",
            "LED | LASER | RADAR | VLC -> mechanism-specific use",
            "STANDARD / SCHEME -> enabling instrument",
            "TEST / SCHEDULE -> not operation",
            "CALIBRATED OUTPUT -> not automatically verified public outcome",
        ], [facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018-2023", "Prelims GS-I",
            "Assess the routed distinctions involving pressure-cooker physics, light-year measurement, accelerometer functions, astronomical objects, VLC, wireless classification and gravitational-wave observations.",
            "Representative historical objective card spanning routed physics concepts; official 2018-2023 keys are unavailable locally, so no option, answer letter or objective key is asserted.",
            [0, 1, 5, 9, 17],
        ),
        common.make_pyq_solution(
            facts, "2024 and 2026", "Prelims GS-I",
            "Assess the routed uses and boundaries of radar, aircraft black-box recorders, underwater detection and crash-survivable memory.",
            "Representative recent objective card covering 2024 Q34 and 2026 Q44; the 2024 official key and provisional 2026 key are not reproduced, and no answer is inferred.",
            [9, 19],
        ),
        common.make_pyq_solution(
            facts, "2018 and 2021", "GS-III",
            "Discuss the contribution of Bose-Einstein statistics to physics and explain the everyday-life impact of the blue LED invention recognised by the 2014 Nobel Prize.",
            "Representative routed Mains card covering 2018 Q5 at 10 marks and 2021 Q16 at 15 marks; it supplies an evidence-bounded answer route, not an official model answer.",
            [15, 18],
        ),
    ]
    return common.topic(
        21,
        "General Science: Physics Fundamentals",
        "21_General-Science-Physics-Fundamentals",
        facts,
        traps,
        [
            (10, "Distinguish SI units, dimensions, scalar-vector quantities and measurement limits.", [0, 1]),
            (10, "Explain how Newton's laws, momentum, impulse, work, energy and power illuminate everyday technology.", [2, 3]),
            (15, "Analyse gravitation, orbital motion, pressure, buoyancy and fluid principles through applications and traps.", [4, 5]),
            (15, "Discuss heat, thermodynamics, waves, sound and optics as linked but distinct physical systems.", [6, 7, 8, 10, 11]),
            (20, "Examine how electricity, magnetism and the electromagnetic spectrum underpin power, communication and safety systems.", [9, 12, 13, 14]),
            (20, "Evaluate how atomic, nuclear and relativistic physics becomes technology through semiconductors, radiation, instruments and evidence-status discipline.", [15, 16, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "SI", "base unit", "derived unit", "dimension", "light-year",
            "scalar", "vector", "displacement", "velocity", "acceleration",
            "accelerometer", "inertia", "momentum", "impulse", "Newton's laws",
            "work-energy theorem", "kinetic energy", "energy", "power",
            "centripetal force", "escape velocity", "geostationary orbit",
            "polar or sun-synchronous orbits", "weightlessness", "pressure", "Pascal's law",
            "Archimedes' principle", "Bernoulli's principle", "buoyancy",
            "specific heat", "latent heat", "conduction", "convection",
            "radiation", "thermodynamics", "temperature difference",
            "frequency", "wavelength", "amplitude", "Doppler effect",
            "resonance", "infrasound", "ultrasound", "reflection", "refraction",
            "total internal reflection", "critical angle", "convex lens",
            "concave lens", "myopia", "hypermetropia", "electromagnetic spectrum",
            "radar", "VLC", "electric current",
            "potential difference", "resistance", "Ohm's law", "electrical power",
            "Series branches", "parallel branches", "earthing", "electromagnetic induction",
            "motor", "generator", "transformer", "AC voltage",
            "photoelectric effect", "Bose-Einstein statistics", "alpha radiation",
            "beta radiation", "gamma radiation", "half-life", "fission", "fusion",
            "special relativity", "general relativity", "gravitational waves",
            "Cepheid", "nebula", "pulsar", "semiconductor", "doping", "p-n junction",
            "LED", "laser", "stimulated emission", "CSIR-NPL", "metrology",
            "black-box recorder", "verified public outcome",
        ],
        "Audited ledgers route eleven Prelims demands from 2018-2026 and two GS-III demands from 2018 and 2021 to this owner: relativity predictions; gravitational waves and black-hole merger; VLC; pressure-cooker physics; sodium lamps versus LEDs; light-year measurement; short-range wireless classification; accelerometers; Cepheids, nebulae and pulsars; radar uses; aircraft black-box recorders and underwater detection; Bose-Einstein statistics; and blue-LED impact. Three representative cards preserve the historical, recent and Mains routes without reproducing or inferring any objective answer key.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official-source retrieval on 2026-09-04 preserved SI measurement discipline, the dated 2023 and 2024 Nobel physics anchors, an official semiconductor-scheme page and the still-future SEMICON India 2026 listing. No constant, instrument accuracy, experiment outcome, manufacturing output, event completion, deployment result or PYQ key was invented.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        ],
        register_headings=(
            "MEASUREMENT, MECHANICS, GRAVITY AND FLUIDS RAPID MAP",
            "THERMAL, WAVE AND OPTICS PRINCIPLE-TO-APPLICATION GRID",
            "ELECTRICITY, MAGNETISM AND MODERN-PHYSICS FIREWALLS",
            "ROUTED PYQ, INSTRUMENT AND VERIFIED-STATUS ANSWER SPINE",
        ),
        register_answer_spine=[
            "NAME THE QUANTITY SI UNIT DIMENSION AND SCALAR-VECTOR CHARACTER",
            "TRACE FORCE TO MOMENTUM IMPULSE WORK ENERGY AND POWER WITHOUT MERGING THEM",
            "EXPLAIN ORBITS AS GRAVITATIONAL FREE FALL AND CLASSIFY THE ORBIT",
            "SELECT PASCAL ARCHIMEDES OR BERNOULLI ONLY AFTER FIXING THE FLUID CONDITION",
            "SEPARATE TEMPERATURE HEAT SPECIFIC HEAT LATENT HEAT AND TRANSFER MODES",
            "FIX MEDIUM FREQUENCY WAVELENGTH AMPLITUDE AND DOPPLER CONDITIONS",
            "DISTINGUISH REFLECTION REFRACTION TOTAL INTERNAL REFLECTION MIRRORS AND LENSES",
            "MOVE FROM CURRENT VOLTAGE RESISTANCE AND POWER TO CIRCUIT TOPOLOGY AND SAFETY",
            "REQUIRE CHANGING MAGNETIC FLUX FOR GENERATORS AND TRANSFORMERS",
            "CLASSIFY PHOTOELECTRIC QUANTUM NUCLEAR AND RELATIVISTIC CLAIMS PRECISELY",
            "LINK SEMICONDUCTOR LED LASER RADAR VLC AND RECORDERS TO THEIR ACTUAL MECHANISMS",
            "STOP AT THE LAST VERIFIED STANDARD TEST SIGNAL SCHEDULE OPERATION OR OUTCOME RUNG",
        ],
    )


TOPIC_21 = _topic_21()
