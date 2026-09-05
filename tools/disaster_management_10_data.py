"""Authored learner-v2 data for Disaster Management Topic 10."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://bhusanket.gsi.gov.in/rolesAndResponsibility.html — fetched "
        "2026-09-04; GSI described landslide susceptibility work, hazard/risk "
        "research, early-warning development and an experimental regional "
        "rainfall-threshold programme. https://ndma.gov.in/Natural-Hazards/"
        "Landslide — attempted 2026-09-04; the NDMA page failed at the "
        "transport layer. No national service-coverage claim was inferred."
    ),
    (
        "https://www.drdo.gov.in/drdo/sites/default/files/"
        "avalanche_warning_bulletin/DGRE_AWB_30-Apr-2026.pdf — fetched "
        "2026-09-04 as raw official PDF content, confirming a dated DGRE "
        "avalanche-warning bulletin exists. https://ndrf.gov.in/en/about-us — "
        "fetched 2026-09-04 only for the general specialised-response role. "
        "No bulletin level, route safety or current readiness was imported."
    ),
    (
        "https://www.nrsc.gov.in/nrscnew/resources_atlas_landslide.php — "
        "fetched 2026-09-04; NRSC described its 1998-2022 inventory, seasonal, "
        "event-based and route-wise classes, and satellite/field-validation "
        "inputs. The figures remain dated atlas metadata, not a forecast or "
        "current loss estimate."
    ),
    (
        "https://www.isro.gov.in/Landslide_Atlas_India.html — fetched "
        "2026-09-04; the official page returned only a thin atlas title. "
        "https://cwc.gov.in/ — fetched 2026-09-04 for CWC's general water-"
        "resources coordination remit, not a GLOF-warning-performance claim. "
        "https://ndma.gov.in/sites/default/files/PDF/Guidelines/"
        "Guidelines-on-Management-of-Glacial-Lake-Outburst-Floods.pdf — "
        "searched 2026-09-04; no retrievable text was obtained. GLOF measures "
        "therefore remain bounded to the canonical owner."
    ),
    (
        "https://nidm.gov.in/modules.asp — searched 2026-09-04; the official "
        "NIDM modules route was identified but supplied no hazard-specific "
        "operational status. It was retained only as a capacity-building source."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Landslide", "A landslide is gravity-driven downslope movement of rock, debris or earth; the movement class and material should be identified before assigning triggers or measures."),
        ("Rockfall", "Rockfall is the detachment and rapid fall, bounce or roll of rock from a steep face or slope, distinct from a coherent slide or channelised debris flow."),
        ("Debris flow", "A debris flow is a rapid, channelised or slope-confined mixture of water, soil, rock and organic material; intense rainfall may trigger it but rainfall is not the moving mass."),
        ("Avalanche", "An avalanche is rapid downslope movement of snow, ice and entrained material produced by snowpack instability, slope and weather conditions; it is not a landslide label for every mountain failure."),
        ("GLOF", "A Glacial Lake Outburst Flood is the sudden release of impounded glacial-lake water after failure, overtopping or displacement affecting a natural dam, producing a downstream flood rather than a snow avalanche."),
        ("Susceptibility versus hazard", "Susceptibility indicates where terrain is more likely to fail from relatively stable conditioning factors, whereas hazard adds probability, timing or intensity under triggers; neither alone equals risk."),
        ("Risk", "Risk combines the mass-movement or flood hazard with exposed people, routes, settlements, infrastructure and vulnerability or capacity, so a high-susceptibility unoccupied slope and a lower-susceptibility dense corridor can pose different risks."),
        ("Conditioning factors", "Geology, slope angle and shape, weathering, soil or rock structure, drainage, land cover, toe erosion, prior movement and human cutting or loading condition slope stability."),
        ("Triggers", "Intense or prolonged rainfall, earthquakes, snow loading or warming, freeze-thaw, erosion, excavation and slope disturbance can trigger failure, but the relevant trigger differs among landslide, avalanche and GLOF mechanisms."),
        ("Cascading risk", "Earthquake or rain can trigger landslides that block rivers; lake or blockage failure can then generate flooding, while cloudburst, debris flow and slope failure may occur in one compound mountain emergency."),
        ("GSI role", "GSI owns national landslide susceptibility, inventory, hazard/risk research and forecasting-development functions; its Bhusanket material distinguishes mapping and experimental warning work."),
        ("DGRE role", "DGRE under DRDO is the hazard-specific institutional anchor for snow and avalanche observation, assessment and warnings; its bulletin is not a GSI landslide forecast."),
        ("NRSC-ISRO role", "NRSC and ISRO provide Earth-observation inventories and mapping support for landslides and glacial or water-body monitoring; an image or atlas is decision support, not proof of safe slopes or warned communities."),
        ("Glacial-lake monitoring", "Glacial-lake risk screening requires repeated remote sensing, lake and dam-character assessment, upstream slope or ice-change observation, field validation where feasible and downstream exposure mapping."),
        ("Zoning and land use", "Susceptibility or hazard zonation should guide avoidance, conditional development, route alignment, settlement expansion, drainage, site investigation and evacuation planning rather than merely decorate a plan."),
        ("Slope and drainage measures", "Surface and subsurface drainage, controlled excavation, retaining or protective works, bioengineering and maintenance may reduce selected instability, but engineering must be site-specific and cannot guarantee every slope."),
        ("Route and settlement planning", "Mountain roads and settlements need risk-sensitive alignment and siting, spoil and drainage control, safe stoppage or closure protocols, alternative access, assembly areas and protection of critical services."),
        ("Warning and evacuation", "Effective warning connects monitoring and forecast uncertainty to authorised messages, route closure or evacuation triggers, accessible communication, safe destinations, drills and feedback."),
        ("Institutional coordination", "GSI, DGRE, NDMA, CWC, NRSC/ISRO, State and district authorities, road agencies, hydropower operators and local communities hold different information and action roles that must be pre-agreed."),
        ("Technology-outcome firewall", "A susceptibility map, satellite image, sensor, bulletin, portal, protective structure or programme proves a capability or input; prediction skill, message receipt, evacuation, route safety and reduced loss require separate dated evidence."),
    ]
    traps = [
        "Do not treat landslide, rockfall, debris flow, avalanche and GLOF as synonyms.",
        "Do not confuse intense rainfall or a cloudburst with the mass movement it may trigger.",
        "Do not equate susceptibility, hazard and risk maps.",
        "Do not assign GSI's landslide role to DGRE or DGRE's avalanche role to ISRO.",
        "Do not convert experimental forecasting into nationwide operational warning.",
        "Do not describe remote sensing as direct prediction of every failure.",
        "Do not assume retaining walls or drainage make an unsuitable site safe.",
        "Do not recommend road closure or evacuation without alternative access and safe destinations.",
        "Do not use a dynamic glacial-lake list or programme figure without its date and owner.",
        "Do not infer safe outcomes from a map, bulletin, sensor, scheme or structure.",
    ]
    titles = [
        "Landslide rockfall debris-flow avalanche and GLOF taxonomy",
        "Susceptibility hazard risk and exposure distinctions",
        "Slope conditioning factors and trigger mechanisms",
        "Rain earthquake snow and human-intervention cascades",
        "Himalaya Western Ghats and site-specific comparison",
        "GSI mapping inventory and forecasting-development role",
        "DGRE snowpack avalanche warning and route decisions",
        "NRSC ISRO Earth observation and field-validation boundary",
        "Glacial-lake dam slope and downstream monitoring chain",
        "Zoning land use settlement and carrying-capacity decisions",
        "Drainage stabilisation bioengineering and engineering limits",
        "Road route hydropower and critical-service planning",
        "Warning closure evacuation drills and accessible communication",
        "Multi-agency mandates uncertainty and local knowledge",
        "PYQ synthesis technology and outcome firewall",
    ]
    routes = [
        "Define the moving material and process before discussing management.",
        "State whether the evidence answers where, when or who may be harmed.",
        "Separate persistent conditions from the event trigger.",
        "Trace the cascade without claiming every trigger causes every outcome.",
        "Compare geology rainfall relief and intervention rather than repeating one list.",
        "Translate a map or inventory into a planning decision and preserve service status.",
        "Use snowpack-slope-weather data for avalanche decisions only.",
        "Treat satellite products as screening and decision support requiring validation.",
        "Connect lake and dam change to downstream exposure and evacuation.",
        "Make zonation alter siting construction and route choices.",
        "Evaluate site-specific works, maintenance, residual risk and avoidance.",
        "Balance connectivity and development with drainage alternatives and safe operation.",
        "Link uncertainty to pre-agreed closure or evacuation action.",
        "Assign the data owner, warning authority and local action owner.",
        "End with verified receipt evacuation access and loss evidence.",
    ]
    panels = [
        common.panel("Mountain-hazard taxonomy", "matrix", [
            "LANDSLIDE -> rock debris or earth movement",
            "ROCKFALL -> detached rock falls / bounces / rolls",
            "DEBRIS FLOW -> water-rich channelised mass",
            "AVALANCHE / GLOF -> snowpack release / lake outburst flood",
        ], ["Landslide", "Rockfall", "Debris flow", "Avalanche", "GLOF"]),
        common.panel("Susceptibility-hazard-risk ladder", "status-ladder", [
            "SUSCEPTIBILITY -> WHERE terrain may fail",
            "HAZARD -> probability timing intensity",
            "EXPOSURE + VULNERABILITY + CAPACITY",
            "RISK -> expected harm and disruption",
        ], ["Susceptibility versus hazard", "Risk"]),
        common.panel("Slope-failure mechanism", "causal-chain", [
            "CONDITIONING -> geology slope weathering drainage land use",
            "TRIGGER -> rain quake erosion cutting loading",
            "FAILURE -> slide fall or flow",
            "EXPOSURE -> route settlement service consequence",
        ], ["Conditioning factors", "Triggers"]),
        common.panel("Cascade map", "systems-map", [
            "EARTHQUAKE / RAIN -> LANDSLIDE",
            "LANDSLIDE -> RIVER BLOCKAGE",
            "BLOCKAGE OR LAKE-DAM FAILURE -> OUTBURST FLOOD",
            "CLOUD BURST -> FLASH FLOW + DEBRIS + SLOPE FAILURE",
        ], ["Cascading risk"]),
        common.panel("Institutional owner matrix", "comparison-table", [
            "GSI -> landslide maps inventory research forecast development",
            "DGRE / DRDO -> snow and avalanche warnings",
            "NRSC / ISRO -> Earth observation and inventories",
            "CWC / STATE / DISTRICT -> downstream water and public action",
        ], ["GSI role", "DGRE role", "NRSC-ISRO role", "Institutional coordination"]),
        common.panel("Glacial-lake monitoring rail", "numbered-rail", [
            "1 REPEAT SATELLITE SCREENING",
            "2 LAKE DAM SLOPE ICE AND OUTFLOW CHARACTER",
            "3 FIELD VALIDATION + DOWNSTREAM EXPOSURE",
            "4 WARNING EVACUATION AND REVIEW",
        ], ["Glacial-lake monitoring"]),
        common.panel("Zonation-to-decision bridge", "decision-tree", [
            "HIGHER SUSCEPTIBILITY / HAZARD?",
            "AVOID OR REQUIRE SITE INVESTIGATION",
            "CONTROL LAND USE DRAINAGE CUTTING LOADING",
            "MAP ROUTE CLOSURE EVACUATION AND RESIDUAL RISK",
        ], ["Zoning and land use"]),
        common.panel("Slope-measure portfolio", "layered-map", [
            "WATER -> surface / subsurface drainage",
            "GEOMETRY -> controlled excavation and toe protection",
            "MATERIAL -> retaining protection bioengineering",
            "LIMIT -> site-specific design maintenance residual risk",
        ], ["Slope and drainage measures"]),
        common.panel("Route and settlement resilience", "network-map", [
            "ALIGNMENT / SITING + SPOIL / DRAINAGE CONTROL",
            "ALTERNATIVE ACCESS + SAFE STOPPAGE / CLOSURE",
            "ASSEMBLY AREA + EVACUATION ROUTE",
            "HOSPITAL POWER TELECOM WATER CONTINUITY",
        ], ["Route and settlement planning"]),
        common.panel("Warning-to-action chain", "process-flow", [
            "MONITOR -> ASSESS -> FORECAST / BULLETIN",
            "AUTHORISE -> COMMUNICATE UNCERTAINTY",
            "CLOSE ROUTE / EVACUATE -> SAFE DESTINATION",
            "VERIFY RECEIPT ACTION AND FEEDBACK",
        ], ["Warning and evacuation"]),
        common.panel("Development-risk balance", "comparison-table", [
            "CONNECTIVITY TOURISM HYDROPOWER LIVELIHOODS",
            "VERSUS",
            "SLOPE DRAINAGE GLACIAL-LAKE AND DOWNSTREAM RISK",
            "VERDICT -> RISK-INFORMED SITING NOT BLANKET CLAIMS",
        ], ["Route and settlement planning", "Institutional coordination"]),
        common.panel("Mountain-risk answer spine", "answer-spine", [
            "CLASSIFY PROCESS -> SEPARATE CONDITION FROM TRIGGER",
            "DISTINGUISH SUSCEPTIBILITY HAZARD AND RISK",
            "ASSIGN GSI DGRE NRSC CWC AND LOCAL ACTION",
            "COMBINE ZONING DRAINAGE ROUTES WARNING EVACUATION + LIMITS",
        ], ["Technology-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2019", "GS-III",
            "Explain landslide hazard zonation mapping and its role in preparedness and mitigation.",
            "Verified direct routing: Explain · 15 marks · 250 words; the answer distinguishes susceptibility, hazard and risk and converts mapping into decisions.",
            [0, 5, 6, 7, 10, 14, 15, 17, 19]),
        common.make_pyq_solution(facts, "2021", "GS-I",
            "Differentiate causes of landslides in the Himalayan region and Western Ghats.",
            "Verified direct routing: Differentiate · 10 marks · 150 words; use a comparison of conditioning factors, rainfall, seismicity and intervention without unsupported event statistics.",
            [0, 7, 8, 9, 14, 15]),
        common.make_pyq_solution(facts, "2021", "GS-III",
            "Describe landslide causes, effects and the National Landslide Risk Management Strategy.",
            "Verified direct routing: Describe · 15 marks · 250 words; strategy use remains bounded to mapping, prevention, warning, capacity and land-use functions.",
            [0, 6, 7, 8, 10, 14, 15, 16, 17, 18, 19]),
    ]
    return common.topic(
        10, "Landslides, Avalanches and GLOF Risk",
        "10_Landslides-Avalanches-and-GLOF-Risk", facts, traps,
        [
            (10, "Distinguish landslide, rockfall, debris flow, avalanche and GLOF.", [0, 1, 2, 3, 4]),
            (10, "Differentiate landslide susceptibility, hazard and risk.", [5, 6, 10, 19]),
            (15, "Analyse conditioning factors, triggers and cascading mountain risk.", [7, 8, 9, 16]),
            (15, "Explain glacial-lake monitoring, GLOF warning and downstream evacuation.", [4, 12, 13, 17, 18, 19]),
            (20, "Evaluate zoning, drainage, slope treatment, road alignment and settlement planning for landslide risk.", [5, 6, 7, 10, 14, 15, 16, 17, 19]),
            (20, "Design a coordinated Himalayan landslide-avalanche-GLOF governance framework under uncertainty.", [0, 3, 4, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "landslide", "mass wasting", "cloudburst", "avalanche",
            "Glacial Lake Outburst Flood", "susceptibility", "hazard",
            "risk", "snowpack", "trigger", "GSI", "DGRE",
            "ISRO", "hazard zonation", "drainage",
        ],
        "All three cards are verified direct routes: 2019 landslide zonation, 2021 Himalayan-versus-Western-Ghats causes, and 2021 landslide causes/effects/National Landslide Risk Management Strategy. Avalanche and GLOF content is not misrepresented as printed in those stems.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered GSI Bhusanket roles, a dated DGRE avalanche bulletin, NRSC's Landslide Atlas, ISRO's atlas route and NDMA pages. Thin, raw-PDF and transport-failed pages are logged; no current hazard level, forecast accuracy, lake count, route status, casualty, event attribution or operational-readiness claim was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "LANDSLIDE ROCKFALL DEBRIS-FLOW AVALANCHE GLOF AND RISK MAP",
            "SUSCEPTIBILITY FORECAST INSTITUTION TECHNOLOGY AND OUTCOME FIREWALLS",
            "ZONING DRAINAGE SLOPE ROUTE SETTLEMENT WARNING EVACUATION SPINE",
            "CURRENT GSI DGRE NRSC ISRO NDMA AND UNCERTAINTY BOUNDARY",
        ),
        register_answer_spine=[
            "IDENTIFY THE MOVING MATERIAL AND HAZARD PROCESS",
            "SEPARATE CONDITIONING FACTORS FROM EVENT TRIGGERS",
            "DISTINGUISH SUSCEPTIBILITY HAZARD EXPOSURE AND RISK",
            "TRACE LANDSLIDE BLOCKAGE FLOOD AND GLOF CASCADES",
            "ASSIGN GSI DGRE NRSC ISRO CWC STATE DISTRICT AND OPERATOR ROLES",
            "COMBINE ZONING DRAINAGE SITE WORKS ROUTE AND SETTLEMENT PLANNING",
            "CONNECT WARNING TO CLOSURE EVACUATION SAFE DESTINATION AND VERIFIED OUTCOME",
        ],
    )


TOPIC_10 = _build()
