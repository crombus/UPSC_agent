"""Authored learner-v2 data for Disaster Management Topic 12."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://peso.gov.in/web/en/rti/rules-regulations-instructions-"
        "manuals-and-records-held-it-or-under-its-control-or-used-its — "
        "fetched 2026-09-04; PESO listed the Explosives Act, Petroleum Act, "
        "related rules and entrusted MSIHC/Chemical Accidents functions. "
        "https://www.indiacode.nic.in/ — searched 2026-09-04; direct Public "
        "Liability, Factories and Atomic Energy PDF routes returned HTTP 403, "
        "so no section-level proposition was reconstructed."
    ),
    (
        "https://cpcb.nic.in/chemical-emergency/ — fetched 2026-09-04 after "
        "redirect and returned only a thin CPCB title. "
        "https://ndma.gov.in/Man-made-Hazards/Chemical — attempted "
        "2026-09-04; the NDMA route failed at the transport layer. Chemical-"
        "response content remains at the audited owner and exam-safe level."
    ),
    (
        "https://www.aerb.gov.in/english/regulatory-facilities/nuclear-power-"
        "plants/emergency-preparedness — fetched 2026-09-04 but redirected to "
        "a thin Hindi home item. https://dae.gov.in/ — fetched 2026-09-04; "
        "DAE confirmed its Central Government atomic-energy business remit. "
        "https://ndrf.gov.in/en/about-us — fetched 2026-09-04 for the general "
        "specialised natural/man-made disaster-response role only."
    ),
    (
        "https://ndma.gov.in/sites/default/files/PDF/Guidelines/"
        "chemical-disaster.pdf — attempted 2026-09-04; transport failed. "
        "https://www.mha.gov.in/en/commoncontent/disaster-management-act-2005 "
        "— attempted 2026-09-04; MHA returned HTTP 403. No force readiness, "
        "facility vulnerability, dispersion, casualty or response outcome was inferred."
    ),
    (
        "https://nidm.gov.in/PDF/pubs/CHEMICAL%20DISASTER%20MANAGEMENT.pdf — "
        "searched 2026-09-04; the official NIDM publication route was found but "
        "not parsed into section-level legal or operational claims."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Industrial accident", "An industrial accident is an unintended event arising from an industrial process, facility, storage or transport system that can cause fire, explosion, release, injury, contamination or service disruption."),
        ("Chemical emergency", "A chemical emergency involves an actual or threatened hazardous-chemical release, fire or reaction requiring chemical-specific identification, protective action, medical management and environmental control."),
        ("Nuclear and radiological emergency", "A nuclear emergency arises from a nuclear-facility or nuclear-chain context, while a radiological emergency may involve radioactive material or exposure without a nuclear-chain event; the terms are related but not interchangeable."),
        ("CBRN category", "CBRN is the umbrella category chemical, biological, radiological and nuclear; each component has a different hazard mechanism, regulator, detection basis, protective approach and medical pathway."),
        ("Industrial life cycle", "Hazard can arise during extraction, manufacture, processing, storage, transport, use, maintenance, waste handling or disposal, so prevention must follow the material and process life cycle."),
        ("Process-safety causes", "Design error, corrosion, fatigue, loss of containment, utility failure, poor maintenance, unsafe change, human or organisational error and weak safety culture can combine rather than operate as one isolated cause."),
        ("NaTech risk", "A natural hazard can trigger a technological accident through flood, earthquake, cyclone, heat or other stresses on hazardous facilities and lifelines; natural and industrial risk therefore require joint screening."),
        ("MSIHC boundary", "The Manufacture, Storage and Import of Hazardous Chemical Rules, 1989 operate under the Environment (Protection) framework and allocate preventive information, safety-report and emergency-planning duties for covered hazardous chemicals and installations."),
        ("Chemical Accidents Rules", "The Chemical Accidents (Emergency Planning, Preparedness and Response) Rules, 1996 establish Central, State, District and Local Crisis Group architecture for chemical-accident planning, coordination and review."),
        ("Factories-law boundary", "Factories legislation supplies occupational and hazardous-process safety duties within its field, but it does not replace environmental chemical rules, off-site planning, public liability or disaster-response coordination."),
        ("Public Liability boundary", "The Public Liability Insurance Act, 1991 provides a no-fault civil-relief route for accidents involving hazardous substances; immediate relief is distinct from final damages, criminal liability or proof that prevention was adequate."),
        ("Atomic-energy boundary", "The Atomic Energy Act framework, DAE responsibilities and AERB regulatory review govern nuclear and radiological safety within their mandates; general disaster authorities do not substitute for technical regulation."),
        ("On-site plan", "The occupier's on-site emergency plan addresses foreseeable facility emergencies, internal command, alarms, shutdown or isolation, worker protection, resources, communication and coordination with outside authorities."),
        ("Off-site plan", "The off-site plan addresses consequences beyond the premises and requires the designated district or local authority to coordinate public warning, protective action, traffic, health, environment and external resources using facility information."),
        ("Role separation", "The occupier prevents and controls the source, regulators enforce specialised safety, local and district authorities protect the public, and NDRF or other specialised teams support response when requested; overlapping roles require a unified plan."),
        ("Detection and protection", "Detection, identification, monitoring, zoning of the affected area, suitable responder protection, public shelter or evacuation decisions and access control should follow authorised technical assessment without exposing operational vulnerabilities."),
        ("Decontamination and medical care", "Decontamination, triage, antidote or treatment decisions, referral, responder monitoring and longer-term health surveillance require hazard-specific protocols and trained medical leadership; generic first aid is insufficient."),
        ("Public communication", "Authorities should communicate what happened, which area and population are affected, what protective action is authorised, where care is available and what uncertainty remains, while preventing rumours and stigma."),
        ("Liability and recovery", "Recovery can require site and environmental remediation, health monitoring, livelihood restoration, investigation, disclosure, compensation or relief and regulatory correction; reopening is not itself proof of restored safety."),
        ("Preparedness-outcome firewall", "A law, licence, safety audit, on-site or off-site plan, drill, detector, team or liability mechanism proves a mandate or input; compliance, safe public protection, decontamination, compensation and reduced harm require separate evidence."),
    ]
    traps = [
        "Do not use industrial accident, chemical emergency, nuclear emergency and CBRN as synonyms.",
        "Do not merge nuclear and radiological emergencies.",
        "Do not treat CBRN as one detection, protection or medical protocol.",
        "Do not imply the Factories Act alone governs off-site chemical consequences.",
        "Do not confuse the MSIHC Rules with the Chemical Accidents Rules.",
        "Do not describe no-fault civil relief as automatic criminal guilt or full compensation.",
        "Do not shift the occupier's prevention duty to NDRF or district authorities.",
        "Do not provide harmful synthesis, dispersal, exploitation or facility-vulnerability detail.",
        "Do not assume a drill, licence, audit or plan proves compliance or readiness.",
        "Do not infer safe recovery, liability resolution or reduced harm from reopening or deployment.",
    ]
    titles = [
        "Industrial chemical nuclear radiological and CBRN distinctions",
        "Industrial life-cycle and process-safety failure chain",
        "NaTech cascading risk and critical lifelines",
        "Factories EPA MSIHC and chemical-accident legal boundaries",
        "Public Liability no-fault relief and accountability boundary",
        "Atomic Energy DAE AERB and disaster-coordination boundary",
        "On-site emergency planning and occupier responsibility",
        "Off-site planning crisis groups and public protection",
        "Regulator local authority district and specialised-response roles",
        "Detection monitoring zoning and protective decisions",
        "Decontamination triage medical referral and surveillance",
        "Public warning uncertainty rumours and trusted communication",
        "Buffer land use transport and vulnerable-population planning",
        "Investigation remediation liability and recovery",
        "PYQ synthesis preparedness and outcome firewall",
    ]
    routes = [
        "Identify the hazard class before naming a law, institution or response.",
        "Trace failure across design operation maintenance change and safety culture.",
        "Screen natural-hazard loads and cascading lifeline failure.",
        "Assign each instrument only its owner-verified field.",
        "Separate immediate no-fault relief from final liability and prevention.",
        "Preserve technical regulation and general coordination as complementary.",
        "Keep source control worker safety communication and external liaison with the occupier.",
        "Translate facility information into public warning protection health and traffic decisions.",
        "Map prevention regulation coordination and specialist response separately.",
        "State only exam-safe detection-to-protection functions and retain uncertainty.",
        "Use hazard-specific decontamination and medicine without operational recipes.",
        "Give actionable authorised public information without speculation.",
        "Protect surrounding settlements workers travellers and service-dependent groups.",
        "Continue through remediation health livelihoods investigation and corrective action.",
        "Conclude with verified compliance protection compensation and recovery evidence.",
    ]
    panels = [
        common.panel("Hazard-family matrix", "matrix", [
            "INDUSTRIAL -> facility / process / transport accident",
            "CHEMICAL -> hazardous release fire or reaction",
            "RADIOLOGICAL / NUCLEAR -> exposure / nuclear-facility context",
            "CBRN -> umbrella; mechanisms and owners remain distinct",
        ], ["Industrial accident", "Chemical emergency", "Nuclear and radiological emergency", "CBRN category"]),
        common.panel("Industrial life-cycle rail", "numbered-rail", [
            "1 DESIGN / MATERIAL SELECTION",
            "2 MANUFACTURE PROCESS STORAGE TRANSPORT",
            "3 OPERATION MAINTENANCE AND CHANGE",
            "4 WASTE DISPOSAL REMEDIATION AND LEARNING",
        ], ["Industrial life cycle", "Process-safety causes"]),
        common.panel("NaTech cascade", "causal-chain", [
            "FLOOD QUAKE CYCLONE HEAT OR LIFELINE FAILURE",
            "-> CONTAINMENT / POWER / COOLING / ACCESS STRESS",
            "-> FIRE EXPLOSION RELEASE OR CONTAMINATION",
            "-> COMPOUND PUBLIC HEALTH AND ENVIRONMENTAL EMERGENCY",
        ], ["NaTech risk"]),
        common.panel("Chemical-law boundary", "comparison-table", [
            "FACTORIES LAW -> workplace / hazardous-process field",
            "EPA + MSIHC -> covered hazardous-chemical prevention duties",
            "CHEMICAL ACCIDENTS RULES -> crisis-group preparedness / response",
            "PLI ACT -> no-fault immediate civil-relief route",
        ], ["MSIHC boundary", "Chemical Accidents Rules", "Factories-law boundary", "Public Liability boundary"]),
        common.panel("Nuclear governance boundary", "systems-map", [
            "ATOMIC ENERGY FRAMEWORK -> CENTRAL TECHNICAL DOMAIN",
            "DAE -> atomic-energy and emergency coordination role",
            "AERB -> regulatory safety review / consent functions",
            "DM AUTHORITIES / NDRF -> public coordination and specialised support",
        ], ["Atomic-energy boundary", "Role separation"]),
        common.panel("On-site plan", "process-flow", [
            "DETECT / ALARM -> INTERNAL COMMAND",
            "SOURCE CONTROL / SHUTDOWN OR ISOLATION",
            "WORKER PROTECTION + ACCOUNTING",
            "INFORM OUTSIDE AUTHORITY + REQUEST SUPPORT",
        ], ["On-site plan"]),
        common.panel("Off-site plan", "process-flow", [
            "FACILITY INFORMATION -> DISTRICT / LOCAL ASSESSMENT",
            "PUBLIC WARNING -> SHELTER / EVACUATION DECISION",
            "TRAFFIC HEALTH ENVIRONMENT AND RESOURCE COORDINATION",
            "MONITOR -> UPDATE -> RECOVERY",
        ], ["Off-site plan"]),
        common.panel("Actor-role matrix", "matrix", [
            "OCCUPIER -> prevent control disclose and support",
            "REGULATOR -> standards inspection consent enforcement",
            "LOCAL / DISTRICT -> public protective action and coordination",
            "SPECIALISED TEAMS -> technical response support",
        ], ["Role separation"]),
        common.panel("Protective-action ladder", "status-ladder", [
            "DETECT / IDENTIFY / MONITOR",
            "ASSESS AREA AND POPULATION AT RISK",
            "AUTHORISE SHELTER EVACUATION ACCESS CONTROL",
            "DECONTAMINATE TRIAGE REFER AND MONITOR",
        ], ["Detection and protection", "Decontamination and medical care"]),
        common.panel("Risk communication card", "network-map", [
            "WHAT HAPPENED + OFFICIAL UNCERTAINTY",
            "WHO / WHERE + WHAT ACTION",
            "CARE LOCATION + UPDATE CHANNEL",
            "RUMOUR CORRECTION WITHOUT STIGMA OR SPECULATION",
        ], ["Public communication"]),
        common.panel("Recovery-accountability loop", "feedback-loop", [
            "REMEDIATE SITE AND ENVIRONMENT",
            "MONITOR HEALTH + RESTORE LIVELIHOODS",
            "INVESTIGATE DISCLOSE RELIEF / COMPENSATION",
            "CORRECT DESIGN REGULATION PLAN AND LAND USE",
        ], ["Liability and recovery"]),
        common.panel("Industrial-CBRN answer spine", "answer-spine", [
            "CLASSIFY HAZARD -> TRACE LIFE-CYCLE / NATECH FAILURE",
            "ASSIGN LAW REGULATOR OCCUPIER LOCAL AUTHORITY AND RESPONSE",
            "CONNECT ON-SITE / OFF-SITE PLANS TO PUBLIC AND MEDICAL ACTION",
            "END WITH REMEDIATION LIABILITY AND VERIFIED OUTCOME",
        ], ["Preparedness-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2023", "GS-III",
            "Discuss oil-pollution impacts on marine ecosystems and India's vulnerability.",
            "Verified cross-owned adjacent route led by Environment; this topic contributes only the industrial life-cycle, response, remediation and liability lens without claiming a direct CBRN PYQ.",
            [0, 4, 5, 13, 14, 18, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, its determination and the Sendai Framework elements.",
            "Verified support route, not an industrial-emergency-specific PYQ; use process safety, NaTech screening, preparedness and recovery as bounded illustrations.",
            [4, 5, 6, 12, 13, 18, 19]),
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Discuss the shift from reactive to proactive disaster management in India.",
            "Verified adjacent governance route; on-site/off-site plans, prevention and drills illustrate proactivity without altering the printed demand.",
            [4, 5, 7, 8, 12, 13, 14, 19]),
    ]
    return common.topic(
        12, "Industrial, Chemical, Nuclear and CBRN Emergencies",
        "12_Industrial-Chemical-Nuclear-and-CBRN-Emergencies", facts, traps,
        [
            (10, "Distinguish industrial accidents, chemical emergencies, nuclear/radiological emergencies and CBRN.", [0, 1, 2, 3]),
            (10, "Explain the respective purposes of on-site and off-site emergency plans.", [12, 13, 14]),
            (15, "Analyse the legal boundaries among factories law, MSIHC Rules, Chemical Accidents Rules and public liability.", [7, 8, 9, 10]),
            (15, "Examine nuclear/radiological emergency governance through DAE, AERB, disaster authorities and specialised response.", [2, 3, 11, 14, 15, 16]),
            (20, "Design an industrial-chemical emergency framework from prevention and NaTech screening to public protection and recovery.", [0, 1, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19]),
            (20, "Critically evaluate whether dense law and preparedness plans ensure CBRN readiness and accountable outcomes.", [3, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "industrial hazards", "chemical accident", "major chemical accident",
            "CBRN", "on-site", "off-site", "MSIHC Rules",
            "Chemical Accidents", "Public Liability Insurance Act",
            "Factories Act", "Atomic Energy Act", "AERB", "DAE",
            "no fault liability", "Environmental Relief Fund",
        ],
        "No audited GS-III route directly names industrial, chemical, nuclear or CBRN emergency governance. The 2023 oil-pollution card is cross-owned adjacent context; the 2024 resilience and 2020 proactive-governance cards are explicit support routes.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered PESO's rules inventory, India Code law routes, CPCB chemical-emergency content, NDMA guidance, DAE, AERB and NDRF. Blocked, thin, redirected and transport-failed pages are recorded; no hazardous synthesis, dispersal, facility weakness, exposure zone, casualty, contamination, readiness or response outcome was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "INDUSTRIAL CHEMICAL RADIOLOGICAL NUCLEAR CBRN AND NATECH MAP",
            "LEGAL OWNER ON-SITE OFF-SITE LIABILITY AND OUTCOME FIREWALLS",
            "PREVENT DETECT PROTECT DECONTAMINATE COMMUNICATE RECOVER SPINE",
            "CURRENT INDIA-CODE PESO CPCB DAE AERB NDRF NDMA EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "CLASSIFY INDUSTRIAL CHEMICAL RADIOLOGICAL NUCLEAR OR BIOLOGICAL HAZARD",
            "TRACE LIFE-CYCLE PROCESS-SAFETY AND NATECH FAILURE",
            "ASSIGN FACTORIES EPA MSIHC CHEMICAL-ACCIDENT PLI AND ATOMIC-ENERGY FIELDS",
            "KEEP OCCUPIER REGULATOR LOCAL AUTHORITY DISTRICT AND SPECIALIST ROLES DISTINCT",
            "LINK ON-SITE SOURCE CONTROL TO OFF-SITE PUBLIC PROTECTION",
            "ADD EXAM-SAFE DETECTION DECONTAMINATION MEDICAL AND COMMUNICATION FUNCTIONS",
            "VERIFY REMEDIATION HEALTH LIABILITY COMPENSATION AND RECOVERY OUTCOMES",
        ],
    )


TOPIC_12 = _build()
