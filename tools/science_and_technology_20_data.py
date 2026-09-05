"""Authored learner-v2 data for Science and Technology Topic 20."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://mines.gov.in/admin/download/649d4212cceb01688027666.pdf - "
        "fetched 2026-09-04 from the official Ministry of Mines domain as a "
        "PDF; the repository owner's 30-mineral expert-report boundary was "
        "retained. No current reserve, resource, production, refining-share "
        "or import-dependence number was inferred from the raw PDF response."
    ),
    (
        "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2097308 - fetch "
        "attempted 2026-09-04 and returned HTTP 403. The owner-recorded "
        "29 Jan 2025 Cabinet approval and authorised NCMM envelope remain "
        "dated approval evidence only, not expenditure, capacity or outcome."
    ),
    (
        "https://www.indiacode.nic.in/bitstream/123456789/1421/1/A1957-67.pdf "
        "- fetch attempted 2026-09-04 and returned HTTP 403. The current owner "
        "remains the authority for the s.10BA, s.11D, Part D and Seventh "
        "Schedule distinctions; no legal-list count was independently updated."
    ),
    (
        "https://kabilindia.in/ - fetched 2026-09-04; substantive official "
        "text confirmed KABIL's NALCO-HCL-MECL structure, Ministry of Mines "
        "aegis and overseas identify-explore-acquire-develop-mine-process-"
        "procure mandate. It supplied no proof that any asset is producing or "
        "that physical supply has been secured."
    ),
    (
        "https://www.irel.co.in/ and https://www.irel.co.in/rare-earths - "
        "fetched/searched 2026-09-04; the official domain supported IREL's "
        "beach-sand and rare-earth context. No monazite reserve, output, "
        "separation-capacity or magnet-self-sufficiency claim was imported."
    ),
    (
        "https://moes.gov.in/schemes/deep-ocean-mission - fetch attempted "
        "2026-09-04 and returned HTTP 403; an official-domain search located "
        "Deep Ocean Mission material on polymetallic-nodule exploration. "
        "Exploration and technology testing were not converted into commercial "
        "deep-sea mining, reserve declaration or production."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2256977&reg=3&lang=1 "
        "- official-source search attempt dated 2026-09-04 located a critical-"
        "mineral recycling release. Volatile company, capacity, investment, "
        "recovery and job figures were deliberately excluded; recycling-policy "
        "existence does not prove recovered material or operating performance."
    ),
]


def _topic_20() -> dict[str, object]:
    facts = [
        ("Material-property structure", "A material's observable performance follows from composition, atomic bonding, crystal or molecular structure, microstructure, defects and processing history; strength, stiffness, toughness, hardness, conductivity, magnetism and corrosion resistance are distinct properties, so one attractive property cannot certify whole-life suitability."),
        ("Advanced composite and smart materials", "An advanced material is engineered for demanding functional performance; a composite combines a continuous matrix with a reinforcement so the constituents retain distinct roles, while a smart material changes a useful property in response to a stimulus. Carbon-fibre polymer composites offer high specific strength and stiffness, shape-memory alloys recover a programmed form after suitable stimulus, and piezoelectric materials couple mechanical stress with electrical response."),
        ("Rare earth element definition", "Rare earth elements are the 15 lanthanides plus scandium and yttrium, a defined 17-element chemical group; the name does not mean every member is geologically rare, because economic concentration, separation difficulty and usable processing capability are the tighter constraints."),
        ("Light-heavy REE distinction", "Light REEs include lanthanum, cerium, praseodymium and neodymium, whereas the owner highlights dysprosium, terbium and yttrium among heavy REEs; heavy-REE scarcity and separation concentration matter because high-temperature permanent magnets may require dysprosium or terbium, while India's monazite endowment is chiefly light-REE-rich."),
        ("Critical mineral versus rare earth", "A critical mineral is a periodically reassessed policy category based on economic, technological or strategic importance plus supply vulnerability; REEs are one defined subgroup within that wider category, while lithium, cobalt, nickel and graphite may be critical without being rare earth elements."),
        ("Permanent magnet chain", "Rare-earth permanent magnets use elements such as neodymium in motors, electronics, aerospace and defence, while the owner identifies dysprosium or terbium as important to high-temperature performance; ore occurrence is not magnet security because separation, metal and alloy production, magnet manufacture, design and recycling remain separate capabilities."),
        ("Battery-mineral chemistry boundary", "Lithium is an active charge-carrier input across lithium-ion chemistries, nickel and cobalt occur in NMC or NCA cathodes, and graphite is commonly an anode material rather than a cathode constituent; LFP uses neither nickel nor cobalt and sodium-ion avoids lithium, so a mineral-use claim must identify chemistry and electrode role."),
        ("Other named uses", "Owner-supported applications extend beyond batteries: gallium and germanium matter to high-technology electronics and semiconductors; copper supports electrical systems; rare earths serve magnets, phosphors, catalysts and specialised optics or electronics; titanium-bearing minerals are a separately named mineral-policy and geography input, while monazite links rare-earth values with thorium-bearing beach sands."),
        ("Mining-to-component chain", "Strategic capability runs through exploration, resource assessment, mine development, extraction, beneficiation, separation or refining, intermediate oxides-metals-alloys, component manufacture and end use; beneficiation upgrades ore, refining or separation produces usable chemical or metallic forms, and neither stage should be collapsed into mining."),
        ("Resource reserve production refining firewall", "A resource is a geologically identified occurrence, a reserve is the economically and legally extractable subset under stated conditions, production is material actually extracted over a period, and refining or processing converts feed into usable specifications; none of these terms proves another, and country rankings or shares require a dated owner."),
        ("Supply concentration and strategic dependency", "Vulnerability can arise at extraction, refining, separation, intermediate-material or component stages, with rare-earth dependence often tighter in the midstream and magnet manufacture than at the mine; strategic dependency is therefore exposure to concentrated capability, trade disruption, technology, finance, logistics or offtake, not merely absence of domestic ore."),
        ("Diversification overseas access and stocks", "Resilience combines domestic exploration, responsible mining, diversified suppliers and refining locations, KABIL-type overseas engagement, trade or investment partnerships, material efficiency and strategic stocks where justified; an MoU, exploration licence, overseas block or asset acquisition is an input to security, not proof of reserves, production or assured supply."),
        ("Recycling urban mining and substitution", "Urban mining recovers materials from end-of-life batteries, electronics, magnets, catalytic converters and industrial scrap; repair, reuse, design for disassembly, collection, sorting, high-quality recovery, substitution and material efficiency complement recycling, while recovered quantity, purity, economics and repeated-cycle quality require evidence rather than assumption."),
        ("Environmental and social impact chain", "Mining can remove vegetation and topsoil, fragment habitat, generate dust and noise, disturb water balances and create overburden, tailings, drainage and closure liabilities; responsible siting, cumulative assessment, consultation, pollution control, water accounting, progressive reclamation, closure finance, community and FRA due diligence, disclosure and grievance redress must accompany mineral-security policy."),
        ("Indian mission and policy boundaries", "The Ministry of Mines' expert critical-mineral assessment, the MMDR statutory Part D list and the Seventh Schedule exploration-licence list are different instruments; the National Critical Mineral Mission is a full-chain mission, but Cabinet approval, authorised outlay, scheme guideline, auction and incentive window do not establish expenditure, mine output, refining capacity or recovery."),
        ("Indian institution map", "The Ministry of Mines anchors policy; GSI surveys and explores; IBM handles mining-plan, scientific-mining and conservation functions; States grant concessions while the Centre auctions Part D minerals under the owner-recorded s.11D boundary; IREL under DAE processes monazite-related material; KABIL pursues overseas access; and MoEFCC or pollution-control institutions govern environmental and waste boundaries."),
        ("MMDR exploration and auction distinction", "The owner records s.10BA Exploration Licence as a competitively auctioned, State-granted right for reconnaissance and prospecting of Seventh Schedule minerals rather than a mining right, while s.11D places the auction of Part D concessions with the Centre although the State grants the concession and receives statutory proceeds; the three legal lists must not be merged."),
        ("Deep-ocean and offshore boundary", "MoES and NIOT's Deep Ocean Mission addresses polymetallic-nodule exploration and technology in the Central Indian Ocean Basin under an International Seabed Authority contract, while offshore mineral areas follow a legal regime separate from land mining; exploration, collector testing or an allotted area is not commercial mining, proved reserves or production."),
        ("Routed PYQ material tests", "The routed objective demands require separate handling of monazite-rare-earth-thorium-policy links, carbon-fibre strength-lightness and difficult recycling, Minerals Security Partnership and MMDR reform, electrode-specific lithium-cobalt-nickel-graphite claims, rare-earth properties and uses, and the 2026 self-reliance mission route; no answer option or letter is supplied."),
        ("Volatile number and status firewall", "Critical-mineral lists, statutory entries, reserves, resources, country rankings, production and refining shares, import dependence, auction counts, project milestones, investment, recycling capacity and recovery totals are date-sensitive; distinguish report, law, notification, approval, MoU, exploration, discovery, reserve declaration, construction, commissioning, production and verified outcome, and stop at the last dated owner."),
    ]
    traps = [
        "Do not use strength, stiffness, toughness and hardness as synonyms.",
        "Do not call every advanced material a composite or every responsive material a sensor.",
        "Do not say all rare earth elements are rare in the crust.",
        "Do not merge light REEs with heavy REEs or monazite occurrence with high-temperature magnet security.",
        "Do not call lithium, cobalt, nickel or graphite rare earth elements.",
        "Do not convert rare-earth ore or oxide into domestic permanent-magnet capability.",
        "Do not place graphite automatically in the cathode or claim every EV chemistry needs nickel and cobalt.",
        "Do not treat every critical mineral as battery-only; match the material to its function.",
        "Do not collapse beneficiation, refining, alloying and component manufacture into mining.",
        "Do not exchange resource, reserve, production, processing capacity and supply.",
        "Do not assume diversified mining removes a concentrated midstream chokepoint.",
        "Do not turn an MoU, licence, overseas block or acquisition into secured production.",
        "Do not treat recycling as costless, lossless or sufficient without collection, purity and design.",
        "Do not make mineral security override EIA, community rights, water, tailings or closure duties.",
        "Do not merge the expert list, Part D list and Seventh Schedule or update their counts from memory.",
        "Do not describe GSI as mine operator, IBM as explorer, KABIL as domestic regulator or IREL as magnet manufacturer.",
        "Do not turn an exploration licence into a mining lease or central auction into central ownership of the concession.",
        "Do not convert deep-ocean exploration or testing into commercial seabed mining.",
        "Do not infer a routed PYQ answer letter from repository coverage.",
        "Do not quote volatile reserves, production, refining, import or project-status numbers without a dated official owner.",
    ]
    titles = [
        "Material properties structure processing and performance",
        "Advanced composite smart and carbon-fibre materials",
        "Rare earth definition and light-heavy classification",
        "Critical minerals versus rare earth elements",
        "Permanent magnets REE functions and component capability",
        "Battery minerals chemistry electrode roles and substitution",
        "Semiconductor defence clean-energy and other named uses",
        "Exploration mining beneficiation refining and processing chain",
        "Resources reserves production and refining evidence boundaries",
        "Supply concentration midstream chokepoints and dependency",
        "Overseas sourcing diversification partnerships and stockpiles",
        "Recycling urban mining circular design and substitution",
        "Mining environmental social and closure safeguards",
        "Indian mission institutions law and exploration routes",
        "Deep-ocean boundary PYQs and volatile-status firewall",
    ]
    routes = [
        "Begin with the property demanded, then connect composition, structure, defects and processing to performance.",
        "Separate matrix and reinforcement from stimulus-response behaviour, then qualify carbon-fibre lifecycle claims.",
        "Define the 17-element group before distinguishing light and heavy REE supply implications.",
        "Classify chemical group, policy category and statutory list before using the word critical.",
        "Trace ore through separation, alloy and magnet manufacture to the final motor or strategic system.",
        "Name the cell chemistry and electrode before assigning lithium, cobalt, nickel or graphite.",
        "Match each named material to an owner-supported function without turning one use into a universal rule.",
        "Walk every stage from exploration to component and identify where value addition and risk change.",
        "State what each evidence term proves, and refuse to substitute a broader occurrence for an extractable reserve.",
        "Locate concentration separately at mine, refinery, intermediate and component stages.",
        "Combine domestic and overseas routes while stopping MoU, licence and asset claims at their verified rung.",
        "Move from product life extension to collection and recovery, then add substitution and quality limits.",
        "Trace mine-life hazards to siting, appraisal, operations, progressive reclamation and closure remedies.",
        "Map Ministry, GSI, IBM, States, IREL, KABIL and statutory instruments without merging mandates.",
        "Separate land, offshore and ISA-linked exploration regimes, then apply PYQ and volatile-number discipline.",
    ]
    panels = [
        panel("Property structure processing map", "causal-chain", [
            "COMPOSITION + BONDING -> intrinsic behaviour",
            "CRYSTAL / MOLECULAR STRUCTURE -> property pathways",
            "MICROSTRUCTURE + DEFECTS -> local performance",
            "PROCESSING -> changes structure and defects",
            "TEST -> strength != stiffness != toughness != hardness",
        ], [facts[0][0]]),
        panel("Advanced materials family", "branch-map", [
            "ADVANCED MATERIAL -> engineered demanding function",
            "COMPOSITE -> matrix + reinforcement",
            "CARBON-FIBRE COMPOSITE -> high specific strength/stiffness",
            "SMART MATERIAL -> stimulus-responsive property",
            "EXAMPLES -> shape-memory alloy | piezoelectric material",
        ], [facts[1][0]]),
        panel("REE classification rail", "classification-table", [
            "REE = 15 LANTHANIDES + SCANDIUM + YTTRIUM",
            "LIGHT -> La | Ce | Pr | Nd",
            "HEAVY OWNER EXAMPLES -> Dy | Tb | Y",
            "MONAZITE -> chiefly light-REE-rich Indian context",
            "TRAP -> geological occurrence != separated magnet input",
        ], [facts[2][0], facts[3][0]]),
        panel("Category firewall", "venn-boundary", [
            "CHEMICAL GROUP -> rare earth elements",
            "POLICY CATEGORY -> critical minerals",
            "STATUTORY ROUTE -> Part D",
            "EXPLORATION ROUTE -> Seventh Schedule",
            "LITHIUM / COBALT / NICKEL / GRAPHITE -> critical may be, REE no",
        ], [facts[4][0], facts[14][0], facts[16][0]]),
        panel("Permanent magnet capability ladder", "capability-ladder", [
            "ORE -> SEPARATION -> OXIDE / METAL",
            "METAL -> ALLOY -> MAGNET",
            "MAGNET -> MOTOR / ELECTRONICS / DEFENCE",
            "Nd -> magnetic performance",
            "Dy / Tb -> high-temperature qualification",
        ], [facts[5][0]]),
        panel("Battery mineral role matrix", "comparison-table", [
            "LITHIUM -> charge-carrier system input",
            "NICKEL + COBALT -> NMC / NCA cathodes",
            "GRAPHITE -> common lithium-ion anode",
            "LFP -> neither nickel nor cobalt",
            "SODIUM-ION -> avoids lithium",
        ], [facts[6][0]]),
        panel("Named application portfolio", "portfolio-wheel", [
            "GALLIUM / GERMANIUM -> high-tech electronics",
            "COPPER -> electrical systems",
            "REE -> magnets | phosphors | catalysts | specialised optics",
            "TITANIUM-BEARING MINERALS -> separate policy / geography input",
            "MONAZITE -> rare-earth values + thorium-bearing context",
        ], [facts[7][0]]),
        panel("Mine to technology value chain", "process-flow", [
            "EXPLORE -> ASSESS -> DEVELOP -> EXTRACT",
            "BENEFICIATE -> SEPARATE / REFINE",
            "OXIDE / METAL / ALLOY -> COMPONENT",
            "COMPONENT -> BATTERY / MAGNET / CHIP / SYSTEM",
            "RECYCLE -> recovered feed with purity/economic limits",
        ], [facts[8][0], facts[9][0]]),
        panel("Dependency heat map", "stage-risk-map", [
            "UPSTREAM -> geology | mine | permitting",
            "MIDSTREAM -> separation | refining | intermediate",
            "DOWNSTREAM -> cell | magnet | chip | equipment",
            "ENABLERS -> technology | finance | logistics | offtake",
            "VERDICT -> secure mine alone is partial security",
        ], [facts[10][0], facts[11][0]]),
        panel("Circular materials loop", "feedback-loop", [
            "DESIGN -> durability | repair | disassembly",
            "USE -> reuse / remanufacture",
            "COLLECT -> sort -> pre-process",
            "RECOVER -> purify -> re-enter manufacture",
            "SUBSTITUTE + EFFICIENCY -> reduce primary-material pressure",
        ], [facts[12][0]]),
        panel("Mine-life safeguard chain", "hazard-remedy-grid", [
            "SITING -> cumulative impact + consultation",
            "OPERATIONS -> dust | noise | water | tailings controls",
            "COMMUNITY -> FRA due diligence | disclosure | grievance",
            "RECLAMATION -> topsoil | stable dumps | native restoration",
            "CLOSURE -> finance + monitoring; plan != achieved outcome",
        ], [facts[13][0]]),
        panel("India institutions status and PYQ rail", "institution-status-rail", [
            "MINES -> policy | GSI -> survey/explore | IBM -> plans/conservation",
            "STATE GRANT + s.11D CENTRAL AUCTION -> distinct roles",
            "IREL / DAE -> monazite route | KABIL -> overseas route",
            "MoES / NIOT / ISA -> deep-ocean exploration boundary",
            "REPORT -> LAW -> APPROVAL -> MOU -> EXPLORATION -> PRODUCTION -> OUTCOME",
        ], [facts[14][0], facts[15][0], facts[16][0], facts[17][0], facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2022 and 2025", "Prelims GS-I",
            "Assess the routed distinctions involving monazite, rare earths, thorium, government-policy boundaries, and the properties and uses of rare earth elements.",
            "Representative routed card covering 2022 Q28 and 2025 Q81; the 2022 official key is unavailable locally and the 2025 official Set-A key is not reproduced, so no option or answer letter is asserted.",
            [2, 3, 5, 7, 15, 19],
        ),
        common.make_pyq_solution(
            facts, "2023 and 2025", "Prelims GS-I",
            "Assess carbon-fibre applications and recyclability, then classify lithium, cobalt, nickel and graphite by material and electrode role in EV batteries.",
            "Representative routed card covering 2023 Q53 and 2025 Q43; the 2023 key is unavailable locally and the 2025 official Set-A key is not reproduced, so no option or answer letter is asserted.",
            [0, 1, 6, 12, 18],
        ),
        common.make_pyq_solution(
            facts, "2025 and 2026", "Prelims GS-I",
            "Assess Minerals Security Partnership, critical-mineral and MMDR boundaries, and India's rare-earth and critical-mineral self-reliance mission.",
            "Representative routed card covering 2025 Q6 and 2026 Q95; the 2025 official Set-A key is not reproduced and the 2026 key is provisional, so no option, answer or answer letter is asserted.",
            [4, 10, 11, 14, 16, 18, 19],
        ),
    ]
    return common.topic(
        20,
        "Emerging Materials, Rare Earths and Critical Minerals",
        "20_Emerging-Materials-Rare-Earths-and-Critical-Minerals",
        facts,
        traps,
        [
            (10, "Distinguish advanced, composite and smart materials through the structure-property-processing relationship.", [0, 1]),
            (10, "Define rare earth elements and distinguish light and heavy REEs from the wider critical-minerals category.", [2, 3, 4]),
            (15, "Explain permanent magnets and battery-mineral uses while preserving chemistry, electrode and component-manufacturing boundaries.", [5, 6, 7]),
            (15, "Examine the mining-beneficiation-refining-processing chain and distinguish resources, reserves, production and refining capability.", [8, 9, 10]),
            (20, "Discuss a resilient critical-mineral strategy through diversification, overseas access, recycling, substitution and responsible mining.", [10, 11, 12, 13]),
            (20, "Critically evaluate India's critical-mineral architecture through missions, institutions, law, deep-ocean exploration, routed PYQs and the volatile-status firewall.", [14, 15, 16, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "composition", "atomic bonding", "microstructure", "defects",
            "processing history", "strength", "stiffness", "toughness",
            "hardness", "advanced material", "composite", "matrix",
            "reinforcement", "carbon-fibre", "smart material",
            "shape-memory alloy", "piezoelectric material",
            "rare earth elements", "lanthanides", "scandium", "yttrium",
            "light REEs", "heavy REEs", "lanthanum", "cerium",
            "praseodymium", "neodymium", "dysprosium", "terbium",
            "critical mineral", "strategic mineral", "permanent magnet",
            "lithium", "cobalt", "nickel",
            "graphite", "NMC", "NCA", "LFP", "sodium-ion", "gallium",
            "germanium", "copper", "titanium", "monazite", "thorium",
            "exploration", "mining", "beneficiation", "separation",
            "refining", "intermediate materials", "component manufacture",
            "resources", "reserves", "production", "supply concentration",
            "strategic dependency", "diversification", "stockpiling",
            "recycling", "urban mining", "substitution", "material efficiency",
            "tailings", "progressive reclamation", "closure finance",
            "National Critical Mineral Mission", "Ministry of Mines",
            "GSI", "IBM", "IREL", "DAE", "KABIL", "NALCO", "HCL", "MECL",
            "MMDR Act", "Part D", "s.11D", "s.10BA",
            "Exploration Licence", "Seventh Schedule",
            "Mineral Security Partnership", "MoES", "NIOT",
            "Deep Ocean Mission", "International Seabed Authority",
            "polymetallic nodules", "Battery Waste Management Rules, 2022",
            "EPR", "status firewall",
        ],
        "Audited ledgers route the 2022 monazite-rare-earth-thorium demand, the 2023 carbon-fibre demand, three 2025 demands on MSP/MMDR, EV-battery materials and REE uses, and the 2026 self-reliance mission demand to this owner. Three representative cards preserve all six routes without supplying an objective key, option or answer letter.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official-source attempts dated 2026-09-04 preserve Ministry of Mines report, KABIL mandate, IREL context, NCMM approval, MMDR and Deep Ocean Mission evidence boundaries. Volatile list counts, reserves, resources, production, refining shares, import ratios, project status, recycling performance and answer letters are not refreshed or inferred without substantive dated owner evidence.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
            "../Economy/advanced/31_Energy-Infrastructure-Economics-Power-Fuels-and-Energy-Security.md",
            "../Geography/basic/31_Mineral-Energy-Resources-World-and-India.md",
            "../Environment-and-Ecology/basic/16_Environmental-Impact-Assessment-and-NGT.md",
            "../Environment-and-Ecology/basic/15_Solid-Plastic-and-E-Waste-Rules.md",
        ],
        register_headings=(
            "MATERIAL PROPERTIES, COMPOSITES, SMART MATERIALS AND REE MAP",
            "MINING, REFINING, COMPONENT AND CIRCULARITY FIREWALLS",
            "CRITICAL-MINERAL SECURITY AND RESPONSIBLE-MINING ANSWER SPINE",
            "INDIAN INSTITUTIONS, LEGAL ROUTES, PYQS AND STATUS BOUNDARY",
        ),
        register_answer_spine=[
            "START WITH COMPOSITION BONDING STRUCTURE MICROSTRUCTURE PROCESSING AND PROPERTY",
            "DISTINGUISH ADVANCED MATERIAL COMPOSITE MATRIX REINFORCEMENT AND SMART RESPONSE",
            "DEFINE THE 17 REES AND SEPARATE LIGHT FROM HEAVY REE CONSTRAINTS",
            "DISTINGUISH REE CHEMICAL GROUP CRITICAL POLICY CATEGORY AND STATUTORY LISTS",
            "TRACE ORE SEPARATION METAL ALLOY PERMANENT MAGNET MOTOR AND RECYCLING",
            "MATCH LITHIUM COBALT NICKEL GRAPHITE AND SUBSTITUTES TO CHEMISTRY AND ELECTRODE",
            "MOVE FROM EXPLORATION MINING BENEFICIATION REFINING INTERMEDIATE TO COMPONENT",
            "SEPARATE RESOURCE RESERVE PRODUCTION REFINING CAPACITY AND SUPPLY SECURITY",
            "LOCATE DEPENDENCY AT EXTRACTION MIDSTREAM COMPONENT TECHNOLOGY FINANCE AND LOGISTICS",
            "COMBINE DIVERSIFICATION KABIL PARTNERSHIPS STOCKS EFFICIENCY SUBSTITUTION AND URBAN MINING",
            "INTERNALISE WATER LAND TAILINGS COMMUNITY RECLAMATION AND CLOSURE COSTS",
            "MAP MINES GSI IBM STATES IREL DAE KABIL MOEFCC MOES NIOT AND ISA",
            "SEPARATE EXPERT REPORT PART D SEVENTH SCHEDULE s.11D AND s.10BA",
            "STOP DEEP-OCEAN AND OVERSEAS CLAIMS AT EXPLORATION OR THE LAST VERIFIED RUNG",
            "CONCLUDE WITH FULL-CHAIN RESILIENCE RESPONSIBLE PROCESSING CIRCULARITY AND STATUS DISCIPLINE",
        ],
    )


TOPIC_20 = _topic_20()
