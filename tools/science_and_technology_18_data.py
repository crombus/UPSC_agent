"""Authored learner-v2 data for Science and Technology Topic 18."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://pmedrive.heavyindustries.gov.in/ - fetched 2026-09-04; "
        "substantive MHI portal text confirmed PM E-DRIVE, Gazette "
        "notification S.O. 4259(E), the original implementation window and "
        "the subsuming of EMPS-2024. The portal text was not used to infer "
        "vehicle sales, charging counts, disbursal, segment success or later "
        "operational status."
    ),
    (
        "https://pmedrive.heavyindustries.gov.in/docs/policy_document/"
        "257594.pdf - fetched 2026-09-04 as an official PDF; the notification "
        "was retained as dated scheme evidence only. No deployment outcome, "
        "market share or beneficiary total was inferred."
    ),
    (
        "https://pmedrive.heavyindustries.gov.in/docs/policy_document/"
        "Extension%20of%20Scheme%20till%2031%2003%202028%20dated%2007%2008%"
        "202025.pdf - fetched 2026-09-04 as an official PDF; it preserved the "
        "owner's extension-notification boundary without converting a scheme "
        "extension into vehicle deployment or infrastructure completion."
    ),
    (
        "https://pmedrive.heavyindustries.gov.in/docs/policy_document/"
        "2026-03-27%20e-rickshaw%20%26%20e-2w%20extension%20notification.pdf "
        "- fetched 2026-09-04 as an official PDF; segment-wise notification "
        "evidence was located, but no target attainment, sales or continuing "
        "eligibility proposition beyond the repository owners was imported."
    ),
    (
        "https://heavyindustries.gov.in/en/pli-scheme-national-programme-"
        "advanced-chemistry-cell-acc-battery-storage - fetched 2026-09-04; "
        "the official page confirmed the ACC battery-storage PLI programme "
        "title. Announced manufacturing support was not rewritten as "
        "installed, commissioned or operating cell capacity."
    ),
    (
        "https://www.bis.gov.in/ev-charging-infrastructure-and-standards-an-"
        "overview/?lang=en - fetched 2026-09-04; the official page confirmed "
        "an EV charging-infrastructure and standards overview. It supplied no "
        "claim about universal connector interoperability, charger rollout or "
        "field compliance."
    ),
    (
        "https://mnre.gov.in/en/notice/scheme-guidelines-for-implementation-"
        "of-pilot-projects-for-use-of-hydrogen-in-the-transport-sector-under-"
        "the-national-green-hydrogen-mission-nghm/ - fetched 2026-09-04; the "
        "official notice confirmed transport-sector green-hydrogen pilot "
        "guidelines. A pilot guideline was not presented as commercial FCEV "
        "deployment, refuelling availability or green-hydrogen supply."
    ),
    (
        "https://cpcb.nic.in/uploads/hwmd/Battery-WasteManagementRules-2022."
        "pdf - fetched 2026-09-04 from the official CPCB domain as a PDF; it "
        "preserved the Battery Waste Management Rules, 2022 and EPR legal "
        "anchor. No collection, recycling or material-recovery outcome was "
        "inferred from the existence of the rules."
    ),
]


def _topic_18() -> dict[str, object]:
    facts = [
        ("BEV-HEV-PHEV-FCEV boundary", "A BEV stores all traction energy in a rechargeable battery; an HEV combines an engine with a non-plug-in electric system charged by the engine and regenerative braking; a PHEV adds external charging and usable electric-only operation; an FCEV remains electric-drive but generates onboard electricity electrochemically from hydrogen."),
        ("Cell-module-pack hierarchy", "A cell is the basic electrochemical unit, a module groups and mechanically manages multiple cells, and a pack integrates modules or cells with enclosure, electrical connections, sensing, cooling, protection and control; announced cell capacity is not automatically assembled pack output or deployed vehicle stock."),
        ("Electrochemical core", "A lithium-ion cell contains an anode, cathode, electrolyte and separator: during discharge lithium ions move through the electrolyte from anode toward cathode while electrons travel through the external circuit, and charging drives the reverse process using external electrical energy."),
        ("Lithium-ion chemistry boundary", "NMC and NCA cathodes use nickel and cobalt and are associated with higher energy-density designs, whereas LFP uses lithium iron phosphate, avoids nickel and cobalt and offers a different cost, density and thermal-stability trade-off; chemistry names must not be treated as identical mineral bills."),
        ("Next-generation chemistry status", "Sodium-ion substitutes sodium for lithium and changes resource and energy-density trade-offs, while solid-state designs replace liquid or gel electrolyte with a solid electrolyte; the owners treat automotive-scale solid-state deployment as pre-commercial and do not establish Indian fleet deployment for either pathway."),
        ("Energy-power density distinction", "Energy density measures stored energy per unit mass or volume and shapes range and weight, whereas power density measures how rapidly energy can be delivered or accepted and shapes acceleration, regenerative braking and fast-charge capability; neither metric alone establishes battery quality or vehicle performance."),
        ("Charging level and AC-DC boundary", "AC charging supplies alternating current to the vehicle, where an onboard charger converts it to DC for the battery; DC fast charging performs conversion outside the vehicle and supplies regulated DC to the pack, while charging level describes power and use context rather than a universal connector or speed guarantee."),
        ("Charging standards and interoperability", "Safe charging requires compatible connectors, communication, protection, earthing and electrical installation; Ministry of Power guidelines, BIS standards, CEA electrical-safety regulation and MoRTH or CMVR vehicle approval are distinct layers, and a published standard does not prove universal interoperability or field compliance."),
        ("Battery-management system", "A BMS monitors cell voltage, current and temperature, estimates operating state, balances cells and enforces charge-discharge limits; it manages the pack within design limits but cannot repair damaged cells, eliminate every fault or substitute for sound cell selection and pack engineering."),
        ("Thermal-management system", "Thermal management removes or redistributes heat and keeps cells within a suitable and reasonably uniform temperature band during operation and charging; cooling architecture, sensing, pack layout and ambient conditions jointly affect safety, charging acceptance and degradation."),
        ("Cycle-life and degradation boundary", "Cycle life counts usable charge-discharge cycles under stated conditions, while calendar ageing occurs with time even without full cycling; temperature, high state of charge, deep cycling, charge rate and cell imbalance can accelerate capacity loss or resistance growth, so no universal battery-life figure should be inferred."),
        ("Thermal-runaway safety chain", "Thermal runaway is self-heating that can accelerate into venting, fire or propagation when heat generation outruns removal; prevention and containment require cell quality, BMS limits, thermal design, mechanical and electrical protection, testing, safe charging and emergency-response discipline rather than blaming lithium alone."),
        ("Fuel-cell and hydrogen boundary", "A PEM fuel cell combines hydrogen and oxygen electrochemically to generate electricity for an electric motor, with water and heat as direct vehicle exhaust products; hydrogen production, compression, transport, storage and vehicle manufacture remain inside lifecycle assessment, and an FCEV is not a combustion-engine hydrogen vehicle."),
        ("Alternative-fuel portfolio", "Ethanol blends and flex-fuel vehicles, biodiesel, compressed bio-gas under the SATAT ecosystem, CNG or LNG and hydrogen diversify transport energy pathways; hydrogen-enriched CNG remains a combustion fuel blend and must not be confused with a hydrogen fuel cell."),
        ("Tailpipe-lifecycle-grid boundary", "BEVs have zero tailpipe exhaust, but lifecycle emissions depend on material extraction and processing, cell and vehicle manufacture, electricity grid mix, utilisation, maintenance, reuse and end-of-life treatment; electrification and grid decarbonisation are complementary rather than interchangeable claims."),
        ("Critical-mineral and chemistry link", "Battery supply risk is chemistry-specific: lithium, graphite, nickel and cobalt requirements vary across cell designs, LFP avoids nickel and cobalt, and sodium-ion changes the lithium dependence; mineral security therefore requires diversified sourcing, processing, substitution, efficient design and circular recovery."),
        ("Recycling and EPR boundary", "The Battery Waste Management Rules, 2022 create an Extended Producer Responsibility framework for collection, recycling and material recovery across battery categories; the legal obligation does not itself prove collection performance, recycling efficiency, recovered quantity or safe informal-sector integration."),
        ("Indian policy-instrument stack", "PM E-DRIVE is a clean-mobility demand and ecosystem instrument, PLI-Auto and PLI-ACC address domestic manufacturing, PM-eBus Sewa concerns urban bus deployment through a separate institutional route, and National Green Hydrogen Mission transport guidelines cover pilots; these instruments solve different market and technology constraints."),
        ("Indian institution and standards map", "MHI anchors PM E-DRIVE and automotive or ACC manufacturing support, MoRTH governs vehicle approval and safety under the road-transport framework, Ministry of Power, BIS, CEA and BEE have distinct charging or electricity roles, MoHUA anchors PM-eBus Sewa, MNRE covers green-hydrogen pilots, MoPNG covers fuel diversification, and MoEFCC anchors battery-waste rules."),
        ("Announcement-to-deployment firewall", "Cabinet approval, Gazette notification, scheme extension, guideline issue, standard publication, capacity award, plant commissioning, charger installation, vehicle sale, safe operation and verified environmental outcome are separate evidence rungs; no subsidy amount, target, sales total, charger count, battery performance or operational status should cross those boundaries without a dated owner."),
    ]
    traps = [
        "Do not call every electric-drive vehicle a BEV.",
        "Do not merge HEV and PHEV; only the PHEV has external charging and usable electric-only operation.",
        "Do not describe an FCEV as a non-electric vehicle or as hydrogen combustion.",
        "Do not merge cell, module, pack and announced manufacturing capacity.",
        "Do not reverse discharge ion and electron paths or omit the separator.",
        "Do not treat NMC, NCA and LFP as having the same mineral and safety profile.",
        "Do not use energy density and power density as synonyms.",
        "Do not equate AC or DC charging with one universal connector, speed or interoperability outcome.",
        "Do not claim a BMS or cooling system makes cell failure impossible.",
        "Do not quote a universal cycle life, charging time, range or degradation rate.",
        "Do not reduce thermal runaway to lithium alone or confuse prevention with propagation control.",
        "Do not turn water at an FCEV tailpipe into a zero-lifecycle-emission claim.",
        "Do not confuse hydrogen-enriched CNG, green hydrogen and fuel-cell propulsion.",
        "Do not treat zero tailpipe emissions as zero lifecycle emissions regardless of grid mix.",
        "Do not convert a policy announcement, standard, target or award into deployed and safely operating infrastructure.",
    ]
    titles = [
        "BEV HEV PHEV and FCEV powertrain taxonomy",
        "Battery cell module pack and electrochemical architecture",
        "Anode cathode electrolyte separator and charge-discharge flow",
        "NMC NCA LFP sodium-ion and solid-state chemistry choices",
        "Energy density power density and vehicle trade-offs",
        "AC charging DC fast charging levels and conversion",
        "Charging connectors communication standards and safety roles",
        "BMS cell balancing state limits and protection",
        "Thermal management degradation and cycle-life controls",
        "Thermal runaway propagation testing and emergency safety",
        "PEM fuel cells hydrogen storage and lifecycle boundary",
        "Ethanol biodiesel CBG gas fuels and hydrogen-enriched CNG",
        "Tailpipe lifecycle grid mix and segment-wise decarbonisation",
        "Critical minerals recycling EPR and circular batteries",
        "Indian missions incentives standards PYQs and deployment firewall",
    ]
    routes = [
        "Classify the powertrain by where traction electricity originates and whether external charging is possible.",
        "Move from electrochemical cell to controlled pack without treating manufacturing announcements as deployment.",
        "Trace ions through the electrolyte and electrons through the external circuit in the correct discharge direction.",
        "Compare chemistry by cathode materials, resource exposure, thermal behaviour and bounded maturity.",
        "Separate stored-energy capability from rate capability before linking either to vehicle use.",
        "Locate AC-DC conversion and distinguish charging context from connector and speed claims.",
        "Map technical interface, communication, installation and institutional safety responsibilities separately.",
        "Explain monitoring, balancing and protective limits without promising fault elimination.",
        "Connect temperature and operating conditions to calendar ageing, cycle ageing and resistance growth.",
        "Trace initiation, self-heating and propagation before listing prevention, containment and response.",
        "Follow hydrogen from production and storage through PEM conversion to direct exhaust and lifecycle qualification.",
        "Classify each fuel by feedstock, conversion pathway, engine or fuel-cell use and emissions boundary.",
        "Evaluate carbon benefits across manufacture, grid, use, reuse and end-of-life rather than tailpipe alone.",
        "Link chemistry-specific minerals to sourcing, substitution, recovery, recycling and producer responsibility.",
        "Separate demand support, manufacturing, standards, pilots and bus deployment, then stop at the last verified rung.",
    ]
    panels = [
        panel("Powertrain source-of-electricity map", "branch-map", [
            "BEV -> battery stores all traction electricity",
            "HEV -> engine + regenerative braking charge non-plug-in battery",
            "PHEV -> external plug + engine backup",
            "FCEV -> hydrogen fuel cell generates onboard electricity",
            "TEST -> where does traction electricity originate?",
        ], [facts[0][0]]),
        panel("Cell to pack systems hierarchy", "nested-hierarchy", [
            "CELL -> electrochemical unit",
            "MODULE -> grouped cells + mechanical integration",
            "PACK -> modules/cells + enclosure + busbars + sensing",
            "CONTROL -> BMS + contactors + protection",
            "THERMAL -> cooling/heating + propagation barriers",
        ], [facts[1][0], facts[8][0], facts[9][0]]),
        panel("Lithium-ion discharge rail", "process-flow", [
            "ANODE -> releases Li+ during discharge",
            "ELECTROLYTE -> carries ions",
            "SEPARATOR -> blocks direct electronic contact",
            "CATHODE -> receives Li+ during discharge",
            "EXTERNAL CIRCUIT -> electrons power motor",
        ], [facts[2][0]]),
        panel("Battery chemistry decision matrix", "comparison-table", [
            "NMC / NCA -> nickel-cobalt exposure; higher-density designs",
            "LFP -> no nickel or cobalt; different density/safety trade-off",
            "SODIUM-ION -> changes lithium dependence",
            "SOLID-STATE -> solid electrolyte; pre-commercial boundary",
            "RULE -> chemistry decides mineral bill and engineering trade-off",
        ], [facts[3][0], facts[4][0], facts[15][0]]),
        panel("Energy and power axes", "two-axis-map", [
            "ENERGY DENSITY -> how much energy per mass/volume",
            "POWER DENSITY -> how quickly energy is delivered/accepted",
            "RANGE / WEIGHT -> energy axis",
            "ACCELERATION / REGEN / FAST CHARGE -> power axis",
            "TRAP -> one metric cannot certify whole-pack performance",
        ], [facts[5][0]]),
        panel("AC and DC charging conversion map", "conversion-flow", [
            "GRID AC -> vehicle onboard charger -> regulated battery DC",
            "GRID AC -> offboard fast charger -> regulated battery DC",
            "LEVEL -> power and use context",
            "CONNECTOR -> physical/electrical interface",
            "PROTOCOL -> communication and control",
        ], [facts[6][0], facts[7][0]]),
        panel("Charging governance institution map", "institution-map", [
            "MINISTRY OF POWER -> charging guidelines",
            "BIS -> connector and safety standards",
            "CEA -> electricity-system and electrical safety regulation",
            "MORTH / CMVR -> vehicle approval and safety",
            "BEE -> efficiency role",
        ], [facts[7][0], facts[18][0]]),
        panel("BMS and thermal-control loop", "feedback-loop", [
            "SENSE -> voltage | current | temperature",
            "ESTIMATE -> operating state and imbalance",
            "ACT -> balance | limit | isolate",
            "COOL / HEAT -> keep cells in suitable band",
            "FEEDBACK -> safer operation and slower degradation, not immunity",
        ], [facts[8][0], facts[9][0], facts[10][0]]),
        panel("Degradation and safety fault tree", "fault-tree", [
            "HEAT / HIGH SOC / DEEP CYCLING / HIGH RATE -> ageing pressure",
            "DEFECT / ABUSE / SHORT -> local heat generation",
            "SELF-HEATING > HEAT REMOVAL -> thermal runaway",
            "CELL EVENT -> possible module/pack propagation",
            "RESPONSE -> prevent + detect + contain + emergency action",
        ], [facts[10][0], facts[11][0]]),
        panel("Hydrogen mobility chain", "lifecycle-chain", [
            "PRODUCTION ROUTE -> green / blue / grey label",
            "COMPRESSION / TRANSPORT / STORAGE -> upstream burden",
            "PEM FUEL CELL -> electrochemical electricity",
            "ELECTRIC MOTOR -> traction",
            "DIRECT EXHAUST -> water + heat; lifecycle remains wider",
        ], [facts[12][0]]),
        panel("Alternative-fuel portfolio", "portfolio-wheel", [
            "ETHANOL / FLEX-FUEL -> petrol-blend engine pathway",
            "BIODIESEL -> diesel-blend pathway",
            "CBG / SATAT -> purified biogas pathway",
            "CNG / LNG / HCNG -> gaseous combustion fuels",
            "HYDROGEN FUEL CELL -> electrochemical electric-drive pathway",
        ], [facts[13][0]]),
        panel("India transition and evidence ladder", "status-ladder", [
            "TAILPIPE -> GRID -> MANUFACTURE -> END OF LIFE",
            "MINERALS -> CHEMISTRY -> RECYCLING / EPR",
            "PM E-DRIVE -> demand/ecosystem instrument",
            "PLI-AUTO / PLI-ACC / PM-eBUS SEWA / NGHM PILOTS -> distinct routes",
            "APPROVAL -> NOTIFICATION -> AWARD -> COMMISSIONING -> DEPLOYMENT -> OUTCOME",
        ], [facts[14][0], facts[15][0], facts[16][0], facts[17][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2019 and 2024", "Prelims GS-I",
            "Assess the routed distinctions between hydrogen-enriched CNG used in public transport and a fuel-cell electric vehicle whose direct exhaust includes water vapour.",
            "Representative routed card covering 2019 Q43 and 2024 Q37; the 2019 key is unavailable locally and the 2024 official Set-A key is not reproduced, so no option or answer letter is asserted.",
            [12, 13, 14],
        ),
        common.make_pyq_solution(
            facts, "2025", "Prelims GS-I",
            "Assess the routed statements distinguishing battery-electric, hydrogen fuel-cell and hybrid vehicle architectures.",
            "Verified routed demand covering 2025 Q41; the official Set-A key is available locally but no option, answer letter or objective answer key is reproduced.",
            [0, 6, 12],
        ),
        common.make_pyq_solution(
            facts, "2023", "GS-III",
            "Discuss how electric vehicles contribute to carbon-emission reduction and identify their wider benefits.",
            "Verified routed Mains demand, 15 marks and 250 words; the model route begins with tailpipe benefits, widens to grid and lifecycle conditions, and adds industrial, energy-security, urban-air and circularity dimensions without inventing deployment results.",
            [0, 14, 15, 16, 17, 19],
        ),
    ]
    return common.topic(
        18,
        "Electric Vehicles, Batteries and Alternative Fuels",
        "18_Electric-Vehicles-Batteries-and-Alternative-Fuels",
        facts,
        traps,
        [
            (10, "Distinguish BEV, HEV, PHEV and FCEV architectures.", [0, 12]),
            (10, "Explain a lithium-ion battery from cell electrochemistry to module and pack integration.", [1, 2, 8]),
            (15, "Compare lithium-ion chemistries and distinguish energy density from power density.", [3, 4, 5, 15]),
            (15, "Examine EV charging, BMS, thermal management, degradation and safety as one engineering system.", [6, 7, 8, 9, 10, 11]),
            (20, "Discuss the role of fuel cells, hydrogen and alternative fuels in a segment-wise clean-mobility transition.", [0, 12, 13, 14]),
            (20, "Critically evaluate India's electric-mobility strategy through lifecycle emissions, critical minerals, recycling, institutions and the announcement-to-deployment boundary.", [14, 15, 16, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "BEV", "HEV", "PHEV", "FCEV", "regenerative braking",
            "cell", "module", "pack", "anode", "cathode", "electrolyte",
            "separator", "NMC", "NCA", "LFP", "sodium-ion",
            "solid-state battery", "energy density", "power density",
            "AC charging", "DC fast charging", "onboard charger",
            "interoperability", "BMS", "cell balancing",
            "thermal management", "cycle life", "calendar ageing",
            "thermal runaway", "PEM fuel cell", "hydrogen-enriched CNG",
            "E20", "flex-fuel vehicle", "biodiesel", "CBG", "SATAT",
            "grid mix", "lifecycle emissions", "critical minerals",
            "Battery Waste Management Rules, 2022",
            "Extended Producer Responsibility", "PM E-DRIVE", "PLI-Auto",
            "PLI-ACC", "PM-eBus Sewa", "National Green Hydrogen Mission",
            "Ministry of Heavy Industries", "MoRTH", "Ministry of Power",
            "BIS", "CEA", "BEE", "MoHUA", "MNRE", "MoPNG", "MoEFCC",
            "announcement-to-deployment",
        ],
        "Audited ledgers route the 2019 hydrogen-enriched-CNG objective demand, the 2024 FCEV-exhaust objective demand, the 2025 alternative-powertrain objective demand and the 2023 GS-III electric-vehicle carbon-reduction question to this owner. Three representative cards preserve all four routes; no objective answer key or option letter is supplied.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official-source attempts on 2026-09-04 preserve the PM E-DRIVE notification and extension ladder, ACC manufacturing-policy title, BIS charging-standards role, MNRE transport-pilot boundary and Battery Waste Management Rules, 2022. Announcements, guidelines, standards and legal duties are not converted into sales, charger counts, operating capacity, battery performance or environmental outcomes.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        ],
        register_headings=(
            "POWERTRAIN, CELL CHEMISTRY AND CHARGING MAP",
            "BATTERY CONTROL, DEGRADATION AND SAFETY FIREWALLS",
            "CLEAN-MOBILITY LIFECYCLE AND FUEL-CHOICE ANSWER SPINE",
            "INDIAN INSTRUMENTS, PYQ ROUTES AND DEPLOYMENT BOUNDARY",
        ),
        register_answer_spine=[
            "CLASSIFY BEV HEV PHEV AND FCEV BY ENERGY SOURCE AND PLUG-IN CAPABILITY",
            "MOVE FROM ANODE CATHODE ELECTROLYTE SEPARATOR TO CELL MODULE AND PACK",
            "COMPARE NMC NCA LFP SODIUM-ION AND SOLID-STATE WITHOUT INVENTING PERFORMANCE",
            "SEPARATE ENERGY DENSITY POWER DENSITY AC CHARGING DC CHARGING AND INTEROPERABILITY",
            "TRACE BMS THERMAL MANAGEMENT CYCLE AGEING CALENDAR AGEING AND THERMAL RUNAWAY",
            "DISTINGUISH PEM FUEL CELLS HYDROGEN-ENRICHED CNG ETHANOL BIODIESEL CBG AND GAS FUELS",
            "TEST TAILPIPE CLAIMS AGAINST GRID MIX MANUFACTURE MINERALS REUSE RECYCLING AND EPR",
            "MAP MHI MORTH POWER BIS CEA BEE MOHUA MNRE MOPNG AND MOEFCC",
            "SEPARATE PM E-DRIVE PLI-AUTO PLI-ACC PM-eBUS SEWA AND NGHM PILOT FUNCTIONS",
            "CONCLUDE SEGMENT-WISE AND STOP AT THE LAST VERIFIED ANNOUNCEMENT-TO-DEPLOYMENT RUNG",
        ],
    )


TOPIC_18 = _topic_18()
