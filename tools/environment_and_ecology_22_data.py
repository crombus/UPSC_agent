"""Authored data for Environment and Ecology learner-v2 Topic 22."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import panel


FACTS = [
    ("Treaty-scope map", "CBD addresses biodiversity, Basel controls transboundary movements and disposal of covered wastes, Stockholm controls persistent organic pollutants, and the Vienna-Montreal regime protects the ozone layer through substance controls; their scopes must not be merged."),
    ("Treaty-status sequence", "Adoption, signature, ratification or accession, entry into force, amendment acceptance and domestic implementation are separate stages; a COP decision is not automatically a treaty amendment."),
    ("CBD three objectives", "The Convention on Biological Diversity combines conservation, sustainable use and fair and equitable sharing of benefits arising from genetic-resource utilisation; conservation alone is incomplete."),
    ("CBD convention-protocol boundary", "The CBD is the parent convention, while the Cartagena Protocol addresses biosafety and living modified organisms and the Nagoya Protocol addresses access and benefit-sharing; protocol participation and obligations require separate status checks."),
    ("Cartagena biosafety pathway", "The Cartagena Protocol governs safe transfer, handling and use of living modified organisms with transboundary-movement procedures; it is not a general hazardous-waste or pesticide treaty."),
    ("Nagoya ABS pathway", "The Nagoya Protocol concerns access to genetic resources, prior informed consent or mutually agreed terms as applicable, and fair benefit-sharing; it must not be confused with biosafety approval."),
    ("CBD COP framework boundary", "A global biodiversity framework or COP decision guides collective implementation under the CBD, but adoption of a target does not prove national legal incorporation, finance or achieved ecological outcome."),
    ("Basel PIC mechanism", "The Basel Convention controls covered transboundary waste movements through prior informed consent and environmentally sound management duties; the original Convention is not an undifferentiated ban on all waste trade."),
    ("Basel Ban Amendment boundary", "The Basel Ban Amendment is a later strengthening with its own scope and entry-into-force history; it must be distinguished from the Convention's general consent-based movement control."),
    ("Basel waste-listing boundary", "Hazardous, other, plastic and electronic waste claims depend on the applicable annex, amendment, contamination condition and national rule; a material name alone does not settle treaty control."),
    ("Rotterdam cluster distinction", "The Rotterdam Convention applies prior informed consent to trade in listed hazardous chemicals and pesticides and is jointly administered with Basel and Stockholm, but administrative clustering does not merge treaty scopes."),
    ("Stockholm POP identity", "Stockholm targets chemicals characterised by persistence, bioaccumulation, adverse effects and long-range environmental transport; toxicity alone does not establish a POP listing."),
    ("Stockholm annex functions", "Stockholm Annex A concerns elimination, Annex B restriction and Annex C unintentional production, subject to treaty-specific exemptions or measures; annex placement must be source-dated."),
    ("POPRC-to-COP sequence", "Scientific review by the Persistent Organic Pollutants Review Committee precedes a Conference of the Parties listing decision; nomination, recommendation, adoption and entry into force are distinct statuses."),
    ("Vienna-Montreal hierarchy", "The Vienna Convention is the framework convention for ozone-layer protection, while the Montreal Protocol is the operative substance-control protocol under it."),
    ("Montreal control object", "The Montreal Protocol controls production and consumption of listed ozone-depleting substances through differentiated schedules and adjustments or amendments; it is not a generic greenhouse-gas treaty."),
    ("Kigali HFC boundary", "The Kigali Amendment phases down hydrofluorocarbons because of climate impact even though HFCs do not deplete ozone; phase-down is not phase-out and Kigali status must be checked separately."),
    ("Montreal implementation support", "The Multilateral Fund and treaty institutions support developing-country implementation, but a finance mechanism or approved project does not itself prove national compliance or atmospheric recovery."),
    ("Decision-obligation boundary", "A proposed listing, review recommendation, draft decision, adopted COP decision, treaty amendment and domestic notification have different legal effects and must be cited at the correct level."),
    ("Current evidence boundary", "Party counts, ratification status, current annex listings, COP outcomes, fund figures, national obligations and implementation results require the relevant secretariat or official national source and date."),
]

TRAPS = [
    "Do not merge the four conventions' environmental objects.",
    "Do not merge adoption, ratification and entry into force.",
    "Do not reduce the CBD to conservation alone.",
    "Do not call Cartagena and Nagoya standalone unrelated conventions.",
    "Do not call Cartagena a hazardous-waste treaty.",
    "Do not call Nagoya a biosafety approval system.",
    "Do not treat a CBD framework target as achieved domestic conservation.",
    "Do not say the original Basel Convention bans all waste trade.",
    "Do not merge the Basel Ban Amendment with the Convention's original PIC rule.",
    "Do not infer waste-control status from a material name alone.",
    "Do not merge Rotterdam's chemical-trade scope with Stockholm's POP controls.",
    "Do not define a POP by toxicity alone.",
    "Do not swap Stockholm Annex A, B and C functions.",
    "Do not turn a POPRC recommendation into an adopted listing.",
    "Do not call Montreal a standalone framework convention.",
    "Do not call every greenhouse gas a Montreal-controlled substance.",
    "Do not call HFCs ozone-depleting or Kigali a phase-out.",
    "Do not treat funding approval as compliance or recovery proof.",
    "Do not merge COP decisions, amendments and domestic notifications.",
    "Do not invent party counts, listings, obligations, outcomes or fund figures.",
]

SESSION_TITLES = [
    "Four-treaty scope and legal-status map",
    "CBD three objectives",
    "CBD parent convention and protocol boundary",
    "Cartagena biosafety protocol",
    "Nagoya access and benefit-sharing protocol",
    "CBD COP delivery boundary and Basel PIC introduction",
    "Basel Ban Amendment boundary",
    "Basel waste-listing boundary",
    "Rotterdam within the BRS cluster",
    "Stockholm POP criteria and treaty purpose",
    "Stockholm annex functions and POPRC listing sequence",
    "Vienna Convention and Montreal Protocol hierarchy",
    "Montreal production and consumption controls",
    "Kigali HFC phase-down and implementation support",
    "Treaty decision listing obligation and current evidence audit",
]

ANSWER_ROUTES = [
    "Begin with a four-row environmental object and mechanism comparison.",
    "Use a legal-status timeline before attributing any obligation.",
    "State all three CBD objectives and separate the parent convention from protocols.",
    "Define Cartagena by living modified organisms and biosafety procedures.",
    "Define Nagoya by access, consent or terms and benefit-sharing.",
    "Separate collective CBD targets from national law, finance and outcomes.",
    "Trace Basel notification, consent, movement and environmentally sound management.",
    "Identify the amendment, waste category and legal status precisely.",
    "Use Rotterdam only for listed chemical and pesticide trade consent.",
    "Apply persistence, bioaccumulation, effects and long-range transport together.",
    "Match Annex A, B and C to their distinct control functions.",
    "Separate nomination, scientific recommendation, COP adoption and operative status.",
    "Place the Montreal Protocol under the Vienna framework.",
    "Distinguish ozone-depleting substances, HFC climate control, schedules and finance.",
    "Close with secretariat-dated evidence and domestic implementation status.",
]

PANELS = [
    panel("Convention scope compass", "comparison-table", [
        "CBD -> biodiversity conservation use and benefit-sharing",
        "BASEL -> transboundary waste movement and disposal",
        "STOCKHOLM -> persistent organic pollutant controls",
        "VIENNA MONTREAL -> ozone-layer substance regime",
        "RULE -> environmental object determines the mechanism",
    ], [FACTS[0][0]]),
    panel("Treaty legal-status ladder", "timeline", [
        "ADOPTION -> text agreed",
        "SIGNATURE -> authentication where applicable",
        "RATIFICATION OR ACCESSION -> consent to be bound",
        "ENTRY INTO FORCE -> operative under treaty conditions",
        "DOMESTIC IMPLEMENTATION -> separate national legal step",
    ], [FACTS[1][0], FACTS[18][0]]),
    panel("CBD family tree", "hierarchy", [
        "CBD -> parent biodiversity convention",
        "OBJECTIVE 1 -> conservation",
        "OBJECTIVE 2 -> sustainable use",
        "OBJECTIVE 3 -> fair and equitable benefit-sharing",
        "PROTOCOLS -> Cartagena biosafety and Nagoya ABS",
    ], [FACTS[2][0], FACTS[3][0]]),
    panel("CBD protocol firewall", "comparison-table", [
        "CARTAGENA -> living modified organisms and biosafety",
        "NAGOYA -> genetic-resource access and benefit-sharing",
        "AIA OR TRANSBOUNDARY PROCEDURE -> Cartagena context",
        "PIC AND MUTUALLY AGREED TERMS -> Nagoya context",
        "STATUS -> participation checked separately for each protocol",
    ], [FACTS[4][0], FACTS[5][0]]),
    panel("CBD delivery chain", "process-flow", [
        "CONVENTION OBJECTIVES -> permanent treaty frame",
        "COP FRAMEWORK OR DECISION -> collective direction",
        "NATIONAL STRATEGY AND LAW -> domestic translation",
        "FINANCE AND IMPLEMENTATION -> activity evidence",
        "ECOLOGICAL OUTCOME -> separate measured result",
    ], [FACTS[6][0]]),
    panel("Basel movement-control rail", "process-flow", [
        "WASTE CLASSIFICATION -> annex and national rule",
        "EXPORT NOTIFICATION -> proposed movement disclosed",
        "PRIOR INFORMED CONSENT -> importing state decision",
        "MOVEMENT AND DISPOSAL -> environmentally sound management",
        "BAN AMENDMENT -> separate stronger legal layer",
    ], [FACTS[7][0], FACTS[8][0], FACTS[9][0]]),
    panel("BRS cluster matrix", "comparison-table", [
        "BASEL -> waste movement",
        "ROTTERDAM -> listed chemical and pesticide trade",
        "STOCKHOLM -> POP production use release and disposal controls",
        "JOINT ADMINISTRATION -> operational coordination",
        "NO MERGER -> three treaty objects and obligations remain distinct",
    ], [FACTS[10][0], FACTS[0][0]]),
    panel("POPs classification board", "comparison-table", [
        "PERSISTENCE -> resists degradation",
        "BIOACCUMULATION -> builds in organisms and food webs",
        "ADVERSE EFFECTS -> human or ecological harm",
        "LONG RANGE TRANSPORT -> crosses boundaries",
        "LISTING -> scientific review plus COP decision",
    ], [FACTS[11][0], FACTS[13][0]]),
    panel("Stockholm annex map", "comparison-table", [
        "ANNEX A -> elimination",
        "ANNEX B -> restriction",
        "ANNEX C -> unintentional production",
        "EXEMPTION OR ACCEPTABLE PURPOSE -> treaty-specific condition",
        "DATE RULE -> current placement needs official list",
    ], [FACTS[12][0]]),
    panel("POPRC decision sequence", "timeline", [
        "NOMINATION -> chemical proposed",
        "SCREENING -> treaty criteria examined",
        "RISK PROFILE AND EVALUATION -> scientific review",
        "POPRC RECOMMENDATION -> advice, not final listing",
        "COP DECISION -> legal listing step subject to treaty rules",
    ], [FACTS[13][0], FACTS[18][0]]),
    panel("Ozone treaty hierarchy", "hierarchy", [
        "VIENNA CONVENTION -> framework cooperation",
        "MONTREAL PROTOCOL -> operative substance controls",
        "SCHEDULES -> production and consumption phase-out",
        "MULTILATERAL FUND -> developing-country implementation support",
        "KIGALI -> HFC phase-down for climate impact",
    ], [FACTS[14][0], FACTS[15][0], FACTS[16][0], FACTS[17][0]]),
    panel("Convention answer spine", "answer-spine", [
        "IDENTIFY -> treaty environmental object",
        "PLACE -> convention protocol amendment or COP decision",
        "TRACE -> consent listing schedule finance and national law",
        "DISTINGUISH -> proposal adoption entry into force and outcome",
        "VERIFY -> current party listing obligation and fund status",
    ], [FACTS[18][0], FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2018", "GS-III",
        "Discuss biodiversity variation in India and the Biological Diversity Act.",
        "Verified routed demand; domestic biodiversity governance is cross-owned by Topic 04.",
        [2, 3, 5, 6, 19],
    ),
]

LIVE_SOURCES = [
    "https://www.cbd.int/convention/text — attempted 2026-09-03; the official CBD page returned raw HTML metadata and was not text-mined for obligations, protocol status or Party counts.",
    "https://www.cbd.int/abs/text/default.shtml — attempted 2026-09-03; the official page returned only an Access and Benefit-sharing title, so no Nagoya obligation or status claim was imported.",
    "https://www.basel.int/TheConvention/Overview/tabid/1271/Default.aspx — attempted 2026-09-03; official retrieval failed at transport level, so no waste listing, amendment status or Party count was imported.",
    "https://www.pops.int/TheConvention/Overview/tabid/3351/Default.aspx — attempted 2026-09-03; official retrieval failed at transport level, so no current POP listing or COP outcome was imported.",
    "https://ozone.unep.org/treaties/montreal-protocol — attempted 2026-09-03; substantive official text confirmed the Protocol's ozone purpose, production-and-consumption phase-out and Kigali HFC phase-down, without supplying a current national compliance result.",
]

TOPIC_22 = common.topic(
    22,
    "Multilateral Environmental Conventions (CBD, Basel, Stockholm, Montreal)",
    "22_Multilateral-Environmental-Conventions-CBD-Basel-Stockholm-Montreal",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-22_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Differentiate the CBD, Basel, Stockholm and Vienna-Montreal regimes.", [0, 2, 7, 11, 14, 15]),
        (10, "Distinguish the Cartagena and Nagoya Protocols.", [3, 4, 5]),
        (15, "Explain Basel's PIC system and Ban Amendment boundary.", [7, 8, 9, 10]),
        (15, "Explain Stockholm POP listing and annex controls.", [11, 12, 13, 18]),
        (20, "Assess why the Montreal architecture is institutionally distinctive.", [14, 15, 16, 17, 18]),
        (20, "Build a status-disciplined comparative answer on the four treaty systems.", [0, 1, 3, 6, 8, 10, 13, 16, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "Convention on Biological Diversity", "conservation", "sustainable use",
        "benefit-sharing", "Cartagena Protocol", "living modified organisms",
        "Nagoya Protocol", "access and benefit-sharing", "Basel Convention",
        "prior informed consent", "Ban Amendment", "Rotterdam Convention",
        "Stockholm Convention", "persistent organic pollutants", "Annex A",
        "Annex B", "Annex C", "POPs Review Committee", "Vienna Convention",
        "Montreal Protocol", "production", "consumption", "Multilateral Fund",
        "Kigali Amendment", "hydrofluorocarbons", "phase-down",
        "adoption", "ratification", "entry into force", "COP decision",
    ],
    (
        "Audited ledgers route biodiversity, ABS, HFC and hazardous-chemical "
        "demands to this comparative owner. Unavailable or provisional objective "
        "keys are not inferred, and treaty names are not treated as answers."
    ),
    PYQ_SOLUTIONS,
    LIVE_SOURCES,
    (
        "The Ozone Secretariat supplied substantive high-level treaty text; CBD "
        "retrieval was thin or raw, and Basel and Stockholm retrieval failed. "
        "No Party count, current annex listing, COP outcome, amendment acceptance, "
        "fund figure, national obligation or implementation result is asserted."
    ),
    extra=[
        "basic/04_Biodiversity-Levels-and-Hotspots.md",
        "basic/09_CITES-and-Wildlife-Trade.md",
        "basic/15_Solid-Plastic-and-E-Waste-Rules.md",
        "basic/17_Climate-Change-Science-Greenhouse-Effect.md",
        "advanced/04_Biodiversity-Levels-and-Hotspots.md",
        "advanced/09_CITES-and-Wildlife-Trade.md",
        "advanced/15_Solid-Plastic-and-E-Waste-Rules.md",
    ],
    pyq_audit_heading="AUDITED CBD, BIOSAFETY, ABS, WASTE, POP AND OZONE PYQ OWNERSHIP",
    register_headings=(
        "FOUR-TREATY SCOPE, PROTOCOL AND MECHANISM MAP",
        "STATUS, ANNEX, LISTING, AMENDMENT AND OBLIGATION TRAPS",
        "MULTILATERAL-CONVENTION ANSWER SPINE",
        "LIVE PARTY, LISTING, COP, FUND AND DOMESTIC-IMPLEMENTATION EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "MATCH CBD BASEL STOCKHOLM AND MONTREAL TO THEIR DISTINCT OBJECTS",
        "SEPARATE PARENT CONVENTION PROTOCOL AMENDMENT AND COP DECISION",
        "DISTINGUISH CARTAGENA BIOSAFETY FROM NAGOYA BENEFIT-SHARING",
        "TRACE BASEL PIC AND STOCKHOLM SCIENTIFIC LISTING",
        "PLACE MONTREAL UNDER VIENNA AND KIGALI UNDER MONTREAL",
        "SEPARATE ADOPTION RATIFICATION ENTRY INTO FORCE AND DOMESTIC LAW",
        "CONCLUDE WITH SECRETARIAT-DATED LISTING OBLIGATION FUND AND OUTCOME EVIDENCE",
    ],
    allow_existing_history=True,
)
