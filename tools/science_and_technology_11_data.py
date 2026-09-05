"""Authored learner-v2 data for Science and Technology Topic 11."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


SEMICONDUCTOR_LIVE_ATTEMPTS = [
    (
        "https://ism.gov.in/schemes/semicon2.0/index — attempted 2026-09-04; "
        "the official owner record supports Cabinet approval of Semicon 2.0 "
        "on 15 July 2026, its Rs 1,27,500 crore outlay and its ecosystem "
        "emphasis on design, machines and materials, fabs, ATMP/OSAT, R&D and "
        "talent. Approval and outlay were not rewritten as disbursement, "
        "capacity created or commercial production."
    ),
    (
        "https://ism.gov.in/notifications/press-release and official ISM "
        "scheme-guideline pages — attempted 2026-09-04; the source owners "
        "record dated approvals, agreements, groundbreakings, inaugurations, "
        "chip presentation and amended guidelines. Each verb is preserved; "
        "no aggregate project total, node size, yield or sales claim is added."
    ),
    (
        "https://ism.gov.in/semicon-india-2026 — attempted 2026-09-04; the "
        "official owner record lists SEMICON India 2026 for 17-19 September "
        "2026. On the attempt date the event remained scheduled, so no event "
        "completion, announcement outcome or participation total is inferred."
    ),
]


def _topic_11() -> dict[str, object]:
    facts = [
        ("Value-chain boundary", "The semiconductor chain runs from design and intellectual property through wafer fabrication, assembly, testing and packaging to boards, modules and finished electronics; strength at one stage does not establish control of every stage."),
        ("Fabless-foundry-IDM boundary", "A fabless firm designs chips and outsources wafer manufacture, a foundry manufactures to customers' designs, and an integrated device manufacturer designs and fabricates its own products; a fab is the plant and is not itself a business-model synonym."),
        ("Front-end-back-end boundary", "Wafer fabrication is the front-end creation of transistor and interconnect layers, while ATMP or OSAT is the back-end assembly, testing, marking and packaging of diced dies; packaging capacity is not wafer-fabrication capacity."),
        ("ATMP-OSAT boundary", "ATMP names assembly, testing, marking and packaging process steps, whereas OSAT names the outsourced service model that performs such back-end work; the terms overlap operationally but are not identical."),
        ("Process-node boundary", "A process node is now largely a generation label associated with density and performance rather than a literal transistor dimension; mature nodes remain strategically useful for automotive, industrial, power and defence applications."),
        ("DUV-EUV boundary", "Deep-ultraviolet lithography supports mature and mid-range manufacturing, while extreme-ultraviolet lithography is a leading-edge chokepoint concentrated in one global supplier and exposed to export controls; a smaller-node claim requires an explicit official source."),
        ("Advanced-packaging boundary", "Chiplets, 2.5D and 3D integration, through-silicon vias and heterogeneous integration can improve system performance without leading-edge lithography, making advanced packaging a capability route rather than a trivial final assembly step."),
        ("Compound-photonics boundary", "Compound semiconductors such as GaN, GaAs, InP and SiC combine multiple elements for power, radio-frequency or optoelectronic uses, while silicon photonics is a silicon platform for optical interconnects and is not a compound semiconductor."),
        ("EDA-design-IP boundary", "Electronic Design Automation tools support architecture, verification, layout and tape-out, while reusable design intellectual property supplies circuit blocks; design capability can exist without domestic wafer fabrication and still retain external tool-chain dependencies."),
        ("Utility-yield boundary", "A competitive fab needs ultra-clean facilities, reliable power, ultra-pure water, specialty gases and chemicals, process control, sustained yield learning and customer qualification; inauguration alone proves none of these operating outcomes."),
        ("ISM-institution boundary", "India Semiconductor Mission is the MeitY-linked implementing agency for semiconductor and display ecosystem schemes; it is distinct from the Semicon India scheme package and from separate electronics-manufacturing incentives."),
        ("Semicon-one architecture", "Semicon India 1.0 has a Rs 76,000 crore umbrella covering semiconductor fabs, display fabs, compound-semiconductor or silicon-photonics or sensor fabs plus ATMP-OSAT, and Design Linked Incentive support."),
        ("DLI-boundary", "Design Linked Incentive supports domestic chip design, design infrastructure, startups and productisation; it is not a direct wafer-fab subsidy and does not establish fabrication self-reliance."),
        ("Semicon-two boundary", "Semicon 2.0 was approved by the Union Cabinet on 15 July 2026 with a Rs 1,27,500 crore outlay and an official ecosystem emphasis spanning design, machines and materials, more fabs, ATMP or OSAT, research and development, and talent."),
        ("Electronics-incentive boundary", "SPECS and electronics or IT-hardware PLI instruments complement semiconductor policy through component and downstream manufacturing incentives, but they are separate from ISM and cannot be merged into one scheme."),
        ("Facility-status boundary", "Official semiconductor evidence must preserve the ladder of approval, fiscal-support agreement, groundbreaking, inauguration, demonstrated output, customer qualification and commercial supply; no earlier rung proves a later one."),
        ("Official-location boundary", "Official 2024 material identifies a Dholera fab and OSAT or ATMP units at Morigaon and Sanand, while the 5 May 2026 official update identifies Crystal Matrix's integrated compound-semiconductor fabrication plus ATMP project in Dholera and Suchi Semicon's OSAT unit in Surat."),
        ("Commissioning-evidence boundary", "Official records identify Micron ATMP at Sanand as inaugurated on 28 February 2026, Kaynes Semicon at Sanand on 31 March 2026 and CG Semi OSAT at Sanand on 4 July 2026; these verbs do not establish node, yield or commercial-scale sale."),
        ("Processor-fabrication boundary", "The audited owner identifies DHRUV64 as a homegrown 1.0-GHz, 64-bit dual-core microprocessor linked to India's RISC-V and processor-IP effort, but a processor design headline does not prove domestic fabrication, volume production or deployed capability."),
        ("Volatile-claim boundary", "Project counts, node sizes, capacities, yields, investment realised, commissioning, commercial output and event outcomes require a dated official source; the provisional 2026 questions and keys supply demands, not answer letters or independent proof of their propositions."),
    ]
    traps = [
        "Do not collapse design, fabrication and ATMP/OSAT into one stage.",
        "Do not use fab, foundry, IDM and fabless as synonyms.",
        "Do not call packaging a wafer fab or dismiss advanced packaging as trivial.",
        "Do not equate ATMP process steps with the OSAT business model.",
        "Do not treat a node label as a literal dimension or automatic strategic superiority.",
        "Do not assign a node size without an explicit dated official source.",
        "Do not call silicon photonics a compound semiconductor.",
        "Do not convert design strength into fabrication self-reliance.",
        "Do not merge ISM, Semicon India, DLI, SPECS and PLI.",
        "Do not convert approval, agreement, groundbreaking or inauguration into commercial supply.",
        "Do not infer yield, customer qualification or ecosystem maturity from a facility milestone.",
        "Do not invent an aggregate project total, production figure or objective answer key.",
    ]
    titles = [
        "Semiconductor value chain from design to device",
        "Fab fabless foundry and IDM business models",
        "Front-end fabrication and back-end ATMP OSAT",
        "Wafer process lithography and node economics",
        "Advanced packaging chiplets and heterogeneous integration",
        "Compound semiconductors and silicon photonics",
        "EDA design IP verification and tape-out",
        "Utilities yield learning and customer qualification",
        "MeitY ISM and Semicon India institutional map",
        "Semicon India 1.0 four-scheme architecture",
        "DLI design support and productisation boundary",
        "Semicon 2.0 ecosystem pillars and approval status",
        "SPECS PLI and downstream electronics demand",
        "Facility locations and milestone-status ladder",
        "DHRUV64 provisional PYQs and volatile-claim audit",
    ]
    routes = [
        "Draw the complete design-to-device chain before judging self-reliance.",
        "Classify the plant and the firm's business model separately.",
        "Compare what is created before and after wafer dicing.",
        "Link manufacturing generation to tools, demand and official evidence.",
        "Explain system-level gains without claiming leading-edge fabrication.",
        "Separate material physics from policy grouping.",
        "Trace blueprint creation and external design-tool dependencies.",
        "Show why a building needs repeatable process performance.",
        "Name ministry, implementing agency and scheme package distinctly.",
        "Present all four programme channels without merging incentives.",
        "Keep design support outside the fab-subsidy category.",
        "Use the six ecosystem pillars and preserve approved status.",
        "Connect demand pull without institutional conflation.",
        "Pair every location with its exact official milestone verb.",
        "Answer routed demands without importing a provisional key.",
    ]
    panels = [
        panel("Design-to-device rail", "process-flow", [
            "DESIGN / IP / EDA -> architecture, verification and tape-out",
            "FOUNDRY / FAB -> transistor and interconnect layers on wafer",
            "DICING -> wafer becomes individual dies",
            "ATMP / OSAT -> assemble, test, mark and package",
            "BOARD / MODULE / DEVICE -> downstream electronics integration",
        ], [facts[0][0], facts[2][0], facts[8][0]]),
        panel("Semiconductor business-model matrix", "comparison-table", [
            "FAB -> physical wafer-manufacturing plant",
            "FABLESS -> designs and outsources wafer manufacture",
            "FOUNDRY -> manufactures to customers' designs",
            "IDM -> designs and fabricates its own products",
            "RULE -> plant type and firm model answer different questions",
        ], [facts[1][0]]),
        panel("Front-end versus back-end", "comparison-table", [
            "FRONT END -> deposition, lithography, etching, doping, metallisation",
            "OUTPUT -> processed wafer containing dies",
            "BACK END -> bonding, encapsulation, testing, marking, packaging",
            "ATMP -> process description; OSAT -> outsourced service model",
            "TRAP -> back-end capacity is not front-end fabrication",
        ], [facts[2][0], facts[3][0]]),
        panel("Node and lithography ladder", "status-ladder", [
            "MATURE / MID-RANGE -> broad automotive, industrial and power uses",
            "DUV -> mature and mid-range lithography route",
            "LEADING EDGE -> rising complexity and capital intensity",
            "EUV -> concentrated equipment and export-control chokepoint",
            "RULE -> verify every project-specific node claim officially",
        ], [facts[4][0], facts[5][0]]),
        panel("Advanced integration map", "systems-map", [
            "CHIPLETS -> specialised dies combined as one system",
            "2.5D / 3D -> denser package-level integration",
            "THROUGH-SILICON VIAS -> vertical interconnect route",
            "HETEROGENEOUS INTEGRATION -> combine unlike functions or processes",
            "INSIGHT -> performance gains need not begin with smaller lithography",
        ], [facts[6][0]]),
        panel("Materials taxonomy", "branch-map", [
            "COMPOUND SEMICONDUCTORS -> GaN / GaAs / InP / SiC",
            "POWER / RF / OPTOELECTRONICS -> application families",
            "SILICON PHOTONICS -> silicon optical-interconnect platform",
            "POLICY GROUPING -> may place unlike technologies together",
            "RULE -> scheme nomenclature does not change material physics",
        ], [facts[7][0]]),
        panel("Fab viability chain", "causal-chain", [
            "RELIABLE POWER + ULTRA-PURE WATER -> stable processing",
            "GASES + CHEMICALS + EQUIPMENT -> controlled process steps",
            "REPEATED RUNS -> yield learning",
            "RELIABILITY EVIDENCE -> customer qualification",
            "OUTCOME -> inauguration alone is not competitive production",
        ], [facts[9][0], facts[15][0]]),
        panel("Institution and scheme map", "institution-map", [
            "MeitY -> parent ministry",
            "ISM -> implementing agency",
            "SEMICON INDIA -> scheme package",
            "DLI -> design-focused channel",
            "SPECS / PLI -> separate complementary electronics incentives",
        ], [facts[10][0], facts[12][0], facts[14][0]]),
        panel("Semicon 1.0 to 2.0", "timeline", [
            "SEMICON INDIA 1.0 -> Rs 76,000 crore umbrella",
            "FOUR CHANNELS -> fabs, displays, compound/sensor/ATMP, DLI",
            "15 JUL 2026 -> Semicon 2.0 Cabinet approval",
            "SEMICON 2.0 -> Rs 1,27,500 crore approved outlay",
            "SIX PILLARS -> design, tools/materials, fabs, back end, R&D, talent",
        ], [facts[11][0], facts[13][0]]),
        panel("Facility evidence map", "institution-map", [
            "DHOLERA -> fab; later named compound-fab plus ATMP approval",
            "MORIGAON -> officially identified OSAT / ATMP location",
            "SANAND -> officially identified back-end cluster and inaugurations",
            "SURAT -> Suchi Semicon OSAT approval",
            "RULE -> location must travel with project and status verb",
        ], [facts[16][0], facts[17][0]]),
        panel("Status firewall", "status-ladder", [
            "APPROVED -> policy permission and support decision",
            "AGREEMENT / GROUNDBREAKING -> financing or construction milestone",
            "INAUGURATED / PRESENTED -> physical or demonstration milestone",
            "QUALIFIED COMMERCIAL SUPPLY -> separate operating evidence",
            "RULE -> never skip a rung or invent production",
        ], [facts[15][0], facts[17][0], facts[19][0]]),
        panel("PYQ answer spine", "answer-spine", [
            "DEFINE -> value chain, fab models and ATMP / OSAT",
            "MAP -> ISM, four Semicon 1.0 channels and Semicon 2.0 pillars",
            "ANALYSE -> tools, utilities, talent, yield and qualification",
            "EVIDENCE -> DHRUV64 and facilities with exact status verbs",
            "QUALIFY -> no project total, node, commercial output or answer key",
        ], [facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2025", "GS-III",
            "Analyse challenges faced by India's semiconductor industry and mention the salient features of the India Semiconductor Mission.",
            "Audited routed Mains demand; the card covers the complete value chain, ISM architecture and implementation constraints without treating later developments as part of the original official model answer.",
            [0, 5, 9, 10, 11, 12, 13, 15, 19],
        ),
        common.make_pyq_solution(
            facts, "2026", "Prelims GS-I",
            "Assess DHRUV64 processor, DIR-V programme and indigenous computing-capability statements.",
            "Provisional routed objective concept; DHRUV64's audited processor description is retained, but the unverified DIR-V ordinal proposition and answer letter are not asserted.",
            [8, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2026", "Prelims GS-I",
            "Match Indian semiconductor projects or plants with their announced state-level locations.",
            "Provisional routed objective concept; official location and status distinctions are taught without inferring an answer letter, aggregate project count or commercial production.",
            [15, 16, 17, 19],
        ),
    ]
    return common.topic(
        11, "Semiconductor Mission and Electronics Manufacturing",
        "11_Semiconductor-Mission-and-Electronics-Manufacturing", facts, traps,
        [
            (10, "Distinguish semiconductor design, wafer fabrication and ATMP or OSAT.", [0, 2, 3, 8]),
            (10, "Differentiate a fab, foundry, fabless company and integrated device manufacturer.", [1]),
            (15, "Explain why advanced packaging and compound semiconductors can form a strategic capability route for India.", [6, 7, 9]),
            (15, "Describe the institutional and scheme architecture of India's semiconductor mission.", [10, 11, 12, 13, 14]),
            (20, "Analyse the challenges faced by India's semiconductor industry and the response of the India Semiconductor Mission.", [0, 5, 8, 9, 10, 11, 12, 13, 15, 19]),
            (20, "Evaluate India's semiconductor strategy through value-chain depth, facility status, electronics demand and selective resilience.", [0, 4, 6, 7, 9, 14, 15, 16, 17, 19]),
        ],
        titles, routes, panels,
        [
            "semiconductor value chain", "chip design", "EDA tools", "tape-out",
            "fabless", "foundry", "IDM", "wafer fabrication", "process node",
            "DUV", "EUV", "ATMP", "OSAT", "advanced packaging", "chiplets",
            "compound semiconductor", "silicon photonics", "India Semiconductor Mission",
            "MeitY", "Semicon India 1.0", "Semicon 2.0", "Design Linked Incentive",
            "SPECS", "PLI", "yield", "customer qualification", "DHRUV64",
        ],
        "Audited ledgers route the 2025 GS-III semiconductor-challenges and India Semiconductor Mission demand plus provisional 2026 processor and plant-location concepts here. The cards preserve official verbs and do not invent an answer letter, project total, node size or commercial-production claim.",
        pyqs, SEMICONDUCTOR_LIVE_ATTEMPTS,
        "Official ISM facts already preserved by the Basic and Advanced owners were re-attempted on 2026-09-04. Semicon 2.0 remains an approved programme; notification, guideline and facility entries retain their dated milestone verbs; SEMICON India 2026 remained scheduled for 17-19 September 2026 on the attempt date.",
        extra=["00_Master-Framework.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "SEMICONDUCTOR VALUE CHAIN AND BUSINESS MODELS",
            "INDIA MISSION ARCHITECTURE AND ECOSYSTEM PILLARS",
            "FACILITY STATUS, PYQ AND CLAIM FIREWALLS",
            "SEMICONDUCTOR ANSWER-WRITING SPINE",
        ),
        register_answer_spine=[
            "DRAW DESIGN IP EDA FABRICATION ATMP OSAT AND DEVICE CHAIN",
            "SEPARATE FAB FOUNDRY FABLESS IDM AND ATMP OSAT",
            "EXPLAIN NODES DUV EUV ADVANCED PACKAGING AND COMPOUND MATERIALS",
            "MAP MeitY ISM SEMICON INDIA DLI SPECS AND PLI",
            "PRESENT SEMICON 1.0 FOUR CHANNELS AND SEMICON 2.0 SIX PILLARS",
            "TEST POWER WATER TOOLS MATERIALS TALENT YIELD AND QUALIFICATION",
            "PAIR EVERY PROJECT LOCATION WITH ITS EXACT STATUS VERB",
            "CONCLUDE ON LAYERED CAPABILITY AND SELECTIVE RESILIENCE",
        ],
    )


TOPIC_11 = _topic_11()
