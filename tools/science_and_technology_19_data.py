"""Authored learner-v2 data for Science and Technology Topic 19."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.civilaviation.gov.in/ministry-documents/rules/drones-"
        "rules-2021-dated-25-august-2021 - attempted 2026-09-04; the official "
        "MoCA page returned HTTP 403 through the live fetch tool. Rule "
        "propositions are therefore retained only where supported by the "
        "audited Basic and Advanced owners; no current consolidated-rule "
        "claim was inferred."
    ),
    (
        "https://egazette.gov.in/WriteReadData/2021/229221.pdf - fetched "
        "2026-09-04 from the official e-Gazette domain as raw PDF bytes. The "
        "retrieval confirms the dated official document exists, but raw bytes "
        "were not treated as machine-readable proof of a provision absent "
        "from the repository owners."
    ),
    (
        "https://digitalsky.dgca.gov.in/ - fetched 2026-09-04; it redirected "
        "to the official AAI Digital Sky endpoint and returned only the "
        "welcome surface. Portal accessibility was not converted into proof "
        "of a permission, registration, operative rule or air-traffic service."
    ),
    (
        "https://digitalsky.aai.aero/faq - fetched 2026-09-04; the official "
        "endpoint returned only 'Welcome to DigitalSky' through the live "
        "tool. Detailed registration, certification, airspace and permission "
        "claims remain bounded by the audited owners."
    ),
    (
        "https://www.civilaviation.gov.in/sites/default/files/2024-04/"
        "Drone%20%28Amendment%29%20Rules%2C%202023.pdf - attempted "
        "2026-09-04; the official PDF returned HTTP 403 through the live "
        "fetch tool. The amendment is retained as dated owner evidence only, "
        "not as a verified consolidated current text."
    ),
    (
        "https://www.civilaviation.gov.in/ministry-documents/notifications/"
        "pli-scheme-drones-and-drone-components-0 - attempted 2026-09-04; "
        "the official MoCA page returned HTTP 403. The existence and purpose "
        "of the manufacturing-support route remain owner-bounded; no outlay, "
        "beneficiary, production, sales or completion figure was imported."
    ),
    (
        "https://lakhpatididi.gov.in/power_to_empower/namo-drone-didi/ - "
        "attempted 2026-09-04; the official scheme page returned HTTP 502. "
        "The repository owner's dated scheme proposition is not extended into "
        "continuation, utilisation, deployment, income or service outcomes."
    ),
]


def _topic_19() -> dict[str, object]:
    facts = [
        (
            "UAV-UAS-RPAS-drone boundary",
            "A UAV is the aircraft itself; a UAS combines the aircraft, remote pilot station, command-and-control links and associated elements; an RPAS is a UAS with a remote pilot in command and is therefore explicitly non-autonomous, while 'drone' is a colloquial umbrella rather than a precise regulatory category.",
        ),
        (
            "Integrated UAS component stack",
            "A useful UAS joins airframe, power source, propulsion, flight-control electronics, navigation sensors, communication links, ground or remote pilot station and payload; capability and certification concern the integrated operating system rather than the airframe alone.",
        ),
        (
            "Flight-stabilisation and control chain",
            "Propulsion creates thrust, control surfaces or rotor-speed changes alter attitude and motion, inertial and other sensors report vehicle state, and the flight controller repeatedly compares sensed state with the commanded path; stable flight therefore depends on a closed control loop, not merely a motor and battery.",
        ),
        (
            "Navigation-command-link boundary",
            "Navigation estimates position, velocity, attitude and route from onboard sensors and available positioning inputs, while the command-and-control link carries pilot commands, telemetry or mission updates; navigation and communication support each other but are not the same subsystem, and loss-of-link behaviour requires a designed failsafe.",
        ),
        (
            "Payload-mission-capability link",
            "A payload is the mission device or material carried beyond the flying platform, such as an imaging sensor, mapping instrument, sprayer or delivery load; payload mass, power demand, data rate and integration affect endurance and control, so one platform label cannot establish every mission capability.",
        ),
        (
            "Multirotor-fixed-wing-hybrid categories",
            "Multirotors use several rotors and suit hover and confined-area work; fixed-wing UAVs generate lift from forward motion and suit wider-area coverage but ordinarily need a launch and recovery solution; hybrid VTOL designs combine vertical take-off or landing with wing-borne cruise at the cost of added integration complexity.",
        ),
        (
            "Remote operation-automation-autonomy boundary",
            "Teleoperation keeps a human in direct remote control, automation executes a pre-programmed sequence in a structured setting, and autonomy uses sensing, onboard logic and feedback to select actions toward a goal with reduced direct control; an unmanned aircraft is not automatically autonomous.",
        ),
        (
            "Robotics sensing-actuation-control loop",
            "Robotics connects sensors that perceive state or environment, a controller that interprets inputs and selects commands, actuators that create physical action, and feedback that corrects subsequent action; aerial robotics adds flight dynamics, navigation, communication and airspace constraints to this loop.",
        ),
        (
            "AI-enabled autonomy boundary",
            "Computer vision or other AI can assist perception, classification, route choice and decision support, but an AI output is not itself lawful authority, safe flight or accountable deployment; training data, validation, human oversight, ground truth and defined fallback behaviour remain necessary.",
        ),
        (
            "Drone-swarm coordination",
            "A drone swarm involves multiple aircraft coordinating through communication, localisation and distributed or autonomous control rules; many drones merely flying nearby do not form a swarm, and resilience depends on network design, sensing, task allocation and behaviour under link or member failure.",
        ),
        (
            "VLOS-BVLOS operating boundary",
            "VLOS keeps the aircraft within the remote pilot's unaided visual line of sight, whereas BVLOS operates beyond that visual envelope and demands stronger communication, navigation, detect-and-avoid, contingency and airspace-assurance arrangements; an authorised experiment is not general permission for routine BVLOS service.",
        ),
        (
            "Counter-UAS and electronic-countermeasure layers",
            "Counter-UAS separates detection, identification, tracking, decision and mitigation; radar, radio-frequency, acoustic or optical sensing may contribute, while jamming or spoofing are electronic countermeasures rather than universal solutions, can affect legitimate systems and belong to a security mandate distinct from DGCA civil-safety regulation.",
        ),
        (
            "Civilian application and evidence boundary",
            "Drones can support crop monitoring or spraying, volcanic observation, wildlife research, surveying, infrastructure inspection, disaster assessment, logistics pilots and public administration by improving access or local observation; imagery still requires permissions, trained interpretation, field verification and sector-specific safeguards.",
        ),
        (
            "Safety-reliability-liability chain",
            "Safe operation links airworthiness, maintenance, pilot or operator competence, weather assessment, route and payload limits, geofencing or other safeguards, command-link resilience, failsafes and incident response; when control is shared among operator, software, manufacturer and service provider, liability must follow evidence about the failed function rather than the word 'autonomous' alone.",
        ),
        (
            "Privacy-data-cybersecurity boundary",
            "Persistent aerial observation can collect personal, geospatial and operational data, while command, navigation and payload links can face interception, spoofing, jamming or malicious access; registration or a permission portal does not by itself establish purpose limitation, data security, lawful surveillance or cyber resilience.",
        ),
        (
            "Drone Rules category spine",
            "The audited owners preserve maximum all-up-weight categories of nano up to 250 g, micro above 250 g to 2 kg, small above 2 kg to 25 kg, medium above 25 kg to 150 kg and large above 150 kg; category is a regulatory risk proxy, not proof of payload, range, autonomy or mission approval.",
        ),
        (
            "Digital Sky-airspace-institution boundary",
            "MoCA anchors policy and notification, DGCA civil regulation and certification, AAI airspace and air-traffic services, and BCAS aviation security; Digital Sky supports registration, identification, permissions and compliance workflows and publishes the green-yellow-red airspace map, but is not itself an air-traffic-control system.",
        ),
        (
            "Certification-registration-pilot-status ladder",
            "Type certification where required evaluates the approved aircraft type, a Unique Identification Number identifies an aircraft, and an RPC through a DGCA-authorised RPTO addresses remote-pilot competence where required; type certificate, registration, pilot credential, airspace permission and lawful mission approval are separate conditions.",
        ),
        (
            "Dual-use and industrial-policy boundary",
            "Civil drones, military UAVs, loitering munitions and counter-UAS share enabling technologies but follow distinct civil-regulatory, defence-procurement and security routes; the owners identify drone-and-component PLI and the complete-drone import restriction with stated exceptions as industrial-policy instruments, not proof of indigenous capability or operational deployment.",
        ),
        (
            "Approval-to-deployment firewall",
            "Rule notification, amendment, portal access, type certification, registration, pilot certification, trial authorisation, scheme approval, manufacturing incentive, procurement, delivery, operational deployment and verified outcome are separate evidence rungs; none establishes performance range, sales, approval, field use, safety record or public benefit beyond its own dated status.",
        ),
    ]
    traps = [
        "Do not use UAV, UAS, RPAS and drone as exact synonyms.",
        "Do not call every unmanned or remotely piloted aircraft autonomous.",
        "Do not reduce UAS capability to the airframe while omitting links, software, navigation and payload.",
        "Do not merge navigation, command-and-control communication and payload-data links.",
        "Do not infer range, endurance or payload from multirotor, fixed-wing or hybrid labels.",
        "Do not call several nearby drones a swarm without coordination and control rules.",
        "Do not treat a BVLOS experiment or sandbox authorisation as routine nationwide permission.",
        "Do not present jamming or spoofing as a universal or consequence-free counter-UAS response.",
        "Do not confuse DGCA civil safety, AAI airspace services, BCAS security and Digital Sky workflows.",
        "Do not turn type certification, UIN or RPC into mission or airspace approval.",
        "Do not infer current legal provisions from an accessible portal when the consolidated rule text is unverified.",
        "Do not treat drone imagery or AI classification as ground truth or lawful final decision.",
        "Do not claim a registration platform automatically solves privacy, data protection or cybersecurity.",
        "Do not bring civil drones, military UAVs and loitering munitions under one undifferentiated policy track.",
        "Do not convert a rule, scheme, trial, incentive, procurement or delivery into deployment or verified outcome.",
    ]
    titles = [
        "UAV UAS RPAS drone and integrated-system taxonomy",
        "Airframe propulsion power flight controller and stabilisation",
        "Navigation communication command link failsafes and payloads",
        "Multirotor fixed-wing and hybrid VTOL capability categories",
        "Teleoperation automation autonomy and meaningful human control",
        "Robotics sensors controllers actuators and feedback",
        "AI perception decision support validation and autonomy limits",
        "Drone swarms communication localisation and distributed coordination",
        "VLOS BVLOS detect-and-avoid and operating assurance",
        "Counter-UAS detection identification and electronic countermeasures",
        "Civilian applications field verification and sector safeguards",
        "Safety reliability weather maintenance and liability",
        "Privacy geospatial data cybersecurity and surveillance boundaries",
        "Drone Rules categories Digital Sky airspace and institutions",
        "Certification industrial policy PYQs and deployment firewall",
    ]
    routes = [
        "Define the aircraft, complete system, remotely piloted subset and colloquial label before analysing capability.",
        "Trace thrust, attitude sensing, controller correction and actuation as a closed flight-control loop.",
        "Separate position estimation, command telemetry, contingency behaviour and mission payload integration.",
        "Compare hover, coverage, launch-recovery and integration trade-offs without inventing performance values.",
        "Locate the human in the control chain and distinguish fixed automation from action-selecting autonomy.",
        "Explain perception, control, actuation and feedback before applying robotics logic to an aerial platform.",
        "Treat AI as a bounded subsystem requiring validated data, oversight, fallback and accountable authority.",
        "Move from multiple aircraft to communications, localisation, task allocation and failure-resilient coordination.",
        "Contrast visual oversight with beyond-line-of-sight assurance and stop at the last authorised status rung.",
        "Build a detect-identify-track-decide-mitigate chain and qualify electronic interference and mandates.",
        "Link access and observation benefits to interpretation, field verification, permissions and sector safeguards.",
        "Join engineering reliability, operator discipline, conditions, incident response and function-specific liability.",
        "Separate lawful collection, purpose, storage and access from link security and navigation integrity.",
        "Map weight classes, colour-coded airspace, Digital Sky, MoCA, DGCA, AAI and BCAS without mandate drift.",
        "Separate certification, registration, credential, permission, incentive, procurement, deployment and outcome.",
    ]
    panels = [
        panel("Aircraft-to-system terminology ladder", "definition-ladder", [
            "UAV -> aircraft only",
            "UAS -> aircraft + remote station + C2 + associated elements",
            "RPAS -> remotely piloted UAS; pilot in command",
            "DRONE -> colloquial umbrella",
            "RULE -> unmanned does not mean autonomous",
        ], [facts[0][0], facts[6][0]]),
        panel("Integrated UAS architecture", "systems-stack", [
            "AIRFRAME + POWER + PROPULSION",
            "FLIGHT CONTROLLER + NAVIGATION SENSORS",
            "COMMAND / TELEMETRY / PAYLOAD-DATA LINKS",
            "REMOTE PILOT STATION OR ONBOARD LOGIC",
            "PAYLOAD -> mission capability",
        ], [facts[1][0], facts[3][0], facts[4][0]]),
        panel("Flight-control feedback loop", "feedback-loop", [
            "COMMAND / PATH -> desired state",
            "IMU / SENSORS -> measured state",
            "CONTROLLER -> compare + correct",
            "ROTORS / CONTROL SURFACES -> physical response",
            "NEW STATE -> sensed again",
        ], [facts[2][0], facts[7][0]]),
        panel("Platform category comparison", "comparison-matrix", [
            "MULTIROTOR -> hover + confined operation | rotor-borne flight",
            "FIXED-WING -> wider-area coverage | launch/recovery need",
            "HYBRID VTOL -> vertical access + wing cruise | integration complexity",
            "PAYLOAD CHANGES -> mass + power + data + control burden",
            "NO LABEL -> universal range/endurance guarantee",
        ], [facts[4][0], facts[5][0]]),
        panel("Human-control continuum", "control-continuum", [
            "TELEOPERATION -> human directly commands",
            "AUTOMATION -> fixed sequence",
            "AUTONOMY -> senses and selects actions",
            "AI SUBSYSTEM -> perception/decision support, not legal authority",
            "ACCOUNTABILITY -> human oversight + defined fallback",
        ], [facts[6][0], facts[8][0], facts[13][0]]),
        panel("Swarm coordination mesh", "network-mesh", [
            "MEMBERS -> multiple aircraft",
            "LOCALISATION -> self and neighbour state",
            "COMMUNICATION -> shared task/state information",
            "CONTROL RULES -> allocation + formation + adaptation",
            "FAILURE TEST -> link loss or member loss",
        ], [facts[9][0]]),
        panel("VLOS to BVLOS assurance bridge", "risk-bridge", [
            "VLOS -> pilot maintains unaided visual contact",
            "BVLOS -> aircraft beyond visual envelope",
            "BRIDGE -> reliable C2 + navigation + detect-and-avoid",
            "CONTINGENCY -> lost link + diversion + termination logic",
            "STATUS -> trial authorisation != routine permission",
        ], [facts[10][0], facts[19][0]]),
        panel("Counter-UAS decision funnel", "decision-funnel", [
            "DETECT -> radar | RF | acoustic | optical",
            "IDENTIFY / TRACK -> classify and maintain picture",
            "DECIDE -> authority + proportionality + surroundings",
            "MITIGATE -> electronic | capture | other authorised response",
            "LIMIT -> jamming/spoofing can affect legitimate systems",
        ], [facts[11][0], facts[14][0]]),
        panel("Civilian application evidence grid", "application-grid", [
            "AGRICULTURE -> monitor / map / spray",
            "SCIENCE -> volcano / wildlife observation",
            "GOVERNANCE -> survey / inspection / disaster assessment",
            "LOGISTICS -> pilot or authorised mission, not blanket service",
            "EVIDENCE -> imagery + interpretation + field verification",
        ], [facts[12][0]]),
        panel("Safety privacy and liability shield", "layered-shield", [
            "ENGINEERING -> airworthiness + maintenance + failsafes",
            "OPERATIONS -> pilot + weather + route + payload discipline",
            "DATA -> purpose + access + retention + geospatial sensitivity",
            "CYBER -> C2/navigation/payload-link resilience",
            "LIABILITY -> trace operator/software/manufacturer function",
        ], [facts[13][0], facts[14][0]]),
        panel("Indian governance responsibility map", "institution-map", [
            "MOCA -> policy / notification",
            "DGCA -> civil regulation / certification",
            "AAI / ATC -> airspace and traffic services",
            "BCAS -> aviation security",
            "DIGITAL SKY -> workflow platform, not ATC",
        ], [facts[15][0], facts[16][0], facts[17][0]]),
        panel("Approval-to-outcome status rail", "status-rail", [
            "RULE / AMENDMENT -> legal text",
            "TYPE CERTIFICATE / UIN / RPC -> distinct compliance conditions",
            "TRIAL / SCHEME / INCENTIVE -> authorised or supported route",
            "PROCUREMENT / DELIVERY -> not operational deployment",
            "DEPLOYMENT -> not verified safety, scale or outcome",
        ], [facts[17][0], facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts,
            "2020",
            "Prelims GS-I",
            "Assess the routed statements on drone applications in agriculture, volcanic observation and wildlife research.",
            "The official objective key is unavailable locally. The card preserves the technical and farmer-economy cross-route and does not assert an option, answer letter or automatic replacement of field verification.",
            [4, 12, 14],
        ),
        common.make_pyq_solution(
            facts,
            "2025",
            "Prelims GS-I",
            "Assess the routed capabilities and limitations of different Unmanned Aerial Vehicle categories.",
            "The official Set-A key is available locally but is not reproduced. The route compares platform architecture and mission fit without inventing range, endurance, payload or objective answers.",
            [1, 4, 5, 6],
        ),
        common.make_pyq_solution(
            facts,
            "2023 and 2026",
            "GS-III and Prelims GS-I",
            "Analyse adversarial UAV threats across Indian borders and assess drone-swarm communication, autonomous coordination and electronic-countermeasure distinctions.",
            "This representative card combines the audited 2023 Mains cross-route with the 2026 provisional-key objective route. No provisional answer is inferred; the model separates threat vector, swarm coordination, layered detection and authorised mitigation.",
            [9, 11, 13, 14, 18, 19],
        ),
    ]
    return common.topic(
        19,
        "Drones, UAVs and Robotics Policy",
        "19_Drones-UAVs-and-Robotics-Policy",
        facts,
        traps,
        [
            (10, "Distinguish UAV, UAS, RPAS and drone, and explain why unmanned does not mean autonomous.", [0, 1, 6]),
            (10, "Explain the sensing-control-actuation loop and its application to stable drone flight.", [2, 3, 7]),
            (15, "Compare multirotor, fixed-wing and hybrid VTOL UAVs through mission and payload trade-offs.", [4, 5, 12]),
            (15, "Examine VLOS, BVLOS, drone-swarm coordination and AI-enabled autonomy as distinct operating challenges.", [6, 8, 9, 10]),
            (20, "Discuss counter-UAS architecture and the safety, privacy, cybersecurity and liability challenges of dual-use drones.", [11, 13, 14, 18]),
            (20, "Critically evaluate India's civil-drone ecosystem through the Drone Rules, Digital Sky, certification, institutions, civilian applications and the approval-to-deployment boundary.", [12, 15, 16, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "UAV", "UAS", "RPAS", "drone", "remote pilot station",
            "command-and-control link", "C2 link", "airframe", "propulsion",
            "flight controller", "inertial", "navigation", "telemetry",
            "failsafe", "payload", "multirotor", "fixed-wing", "hybrid VTOL",
            "teleoperation", "automation", "autonomy", "sensor", "controller",
            "actuator", "feedback loop", "computer vision", "human oversight",
            "ground truth", "drone swarm", "distributed",
            "localisation", "task allocation", "VLOS", "BVLOS",
            "detect-and-avoid", "counter-UAS", "radar", "radio-frequency",
            "jamming", "spoofing", "electronic countermeasure",
            "agriculture", "volcanic observation", "wildlife research",
            "surveying", "disaster assessment", "logistics", "airworthiness",
            "geofencing", "privacy", "geospatial data", "cybersecurity",
            "liability", "Drone Rules, 2021", "nano", "micro", "small",
            "medium", "large", "maximum all-up weight", "Digital Sky",
            "green-yellow-red", "MoCA", "DGCA", "AAI",
            "ATC", "BCAS", "type certification", "Unique Identification Number",
            "Remote Pilot Certificate", "RPTO", "PLI", "dual-use technology",
            "loitering munition", "approval-to-deployment",
        ],
        (
            "Audited ledgers route the 2020 Prelims applications demand, the "
            "2025 Prelims UAV-capabilities demand and the 2026 provisional-key "
            "swarm-coordination and electronic-countermeasure demand directly "
            "to this owner. Relevant cross-routes include the 2023 GS-III "
            "adversarial-UAV border question and the 2025 GS-I AI-drones-GIS "
            "planning question. Three representative cards preserve the core "
            "and security routes without inventing any objective answer key."
        ),
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        (
            "Official MoCA, e-Gazette, Digital Sky and Namo Drone Didi source "
            "attempts were made on 2026-09-04. The e-Gazette PDF and Digital "
            "Sky welcome surface were retrievable; several official pages "
            "returned HTTP 403 or 502. Consequently, exact rule, amendment, "
            "scheme and certification propositions remain owner-bounded, and "
            "no performance range, approval, deployment, sales, production, "
            "service continuation or objective answer key is asserted."
        ),
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
            "basic/06_Defence-RandD-DRDO-and-Missile-Systems.md",
            "advanced/06_Defence-RandD-DRDO-and-Missile-Systems.md",
            "basic/07_Defence-Indigenization-Atmanirbhar-and-Procurement.md",
            "advanced/07_Defence-Indigenization-Atmanirbhar-and-Procurement.md",
            "basic/09_Artificial-Intelligence-Governance-and-IndiaAI.md",
            "../Economy/basic/27_Digital-Agriculture-Agritech-and-e-Technology-for-Farmers.md",
            "../Internal-Security/basic/06_Border-Management-and-Border-Area-Development.md",
        ],
        register_headings=(
            "UAV SYSTEM, FLIGHT-CONTROL AND PLATFORM-CATEGORY MAP",
            "ROBOTICS, AUTONOMY, SWARM AND BVLOS CONTROL SPINE",
            "APPLICATION, COUNTER-UAS, SAFETY AND RIGHTS FIREWALLS",
            "INDIAN DRONE GOVERNANCE, PYQ ROUTES AND DEPLOYMENT BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE UAV UAS RPAS AND DRONE BEFORE USING THE TERMS",
            "MAP AIRFRAME POWER PROPULSION FLIGHT CONTROL NAVIGATION C2 AND PAYLOAD",
            "TRACE SENSING CONTROLLER ACTUATION FEEDBACK AND LOST-LINK FAILSAFE",
            "COMPARE MULTIROTOR FIXED-WING AND HYBRID VTOL WITHOUT INVENTING PERFORMANCE",
            "SEPARATE TELEOPERATION AUTOMATION AUTONOMY AI ASSISTANCE AND LEGAL AUTHORITY",
            "BUILD SWARM COORDINATION FROM COMMUNICATION LOCALISATION TASKING AND RESILIENCE",
            "DISTINGUISH VLOS BVLOS EXPERIMENTAL AUTHORISATION AND ROUTINE PERMISSION",
            "TRACE COUNTER-UAS FROM DETECTION TO IDENTIFICATION DECISION AND MITIGATION",
            "QUALIFY JAMMING SPOOFING PRIVACY DATA CYBERSECURITY SAFETY AND LIABILITY",
            "USE AGRICULTURE SCIENCE SURVEY DISASTER AND LOGISTICS WITH FIELD VERIFICATION",
            "MAP WEIGHT CLASSES DIGITAL SKY MOCA DGCA AAI ATC AND BCAS",
            "SEPARATE TYPE CERTIFICATE UIN RPC RPTO AIRSPACE AND MISSION CONDITIONS",
            "KEEP CIVIL DRONES MILITARY UAVS LOITERING MUNITIONS AND PROCUREMENT DISTINCT",
            "CONCLUDE AT THE LAST VERIFIED RULE-TO-DEPLOYMENT EVIDENCE RUNG",
        ],
    )


TOPIC_19 = _topic_19()
