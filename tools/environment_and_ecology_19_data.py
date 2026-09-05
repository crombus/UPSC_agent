"""Authored data for Environment and Ecology learner-v2 Topic 19."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import UNFCCC_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("UNFCCC convention identity", "The UNFCCC is the framework convention that establishes the climate objective, principles, institutions and continuing negotiation process; it is distinct from later protocols, agreements and COP decisions."),
    ("COP-CMP-CMA boundary", "The COP is the Convention's supreme body, while the CMP and CMA are meetings of Parties to the Kyoto Protocol and Paris Agreement respectively; their decisions must be attributed to the correct governing body."),
    ("Treaty-status sequence", "Adoption, signature, ratification or accession, entry into force and domestic implementation are separate legal or political stages; completion of one stage does not prove another."),
    ("Kyoto Protocol identity", "The Kyoto Protocol operationalised the Convention through quantified commitments for the covered developed-country group during commitment periods; it did not impose the same target architecture on every Party."),
    ("Annex I historical boundary", "Annex I is a Convention grouping used in the historical Kyoto architecture; any claim about Annex obligations must identify the instrument, period and obligation rather than project the label onto every Paris duty."),
    ("Non-Annex Kyoto boundary", "Developing non-Annex I Parties did not receive Kyoto-style quantified emission-limitation or reduction commitments, although they had other Convention and Protocol roles."),
    ("Kyoto mechanisms", "International emissions trading, Joint Implementation and the Clean Development Mechanism are distinct Kyoto mechanisms with different participants and project or unit pathways."),
    ("Doha Amendment status", "The Doha Amendment concerns Kyoto's second commitment period and has its own adoption and entry-into-force history; amendment adoption and operative legal status are not interchangeable."),
    ("Paris Agreement identity", "The Paris Agreement is an agreement under the Convention built around universal participation, nationally determined contributions, transparency, stocktaking and successive cycles."),
    ("NDC boundary", "An NDC is nationally determined and communicated by a Party; the Paris Agreement does not itself assign one identical substantive numerical target to all Parties."),
    ("Procedure-ambition distinction", "Paris creates legally binding procedural duties such as preparing, communicating and maintaining successive NDCs and pursuing domestic measures, while the substantive level of each Party's mitigation ambition remains nationally determined."),
    ("Progression and cycle", "Successive NDCs are expected to represent progression and highest possible ambition within the Agreement's cycle; this standard does not prescribe one universal percentage increase."),
    ("Transparency-outcome boundary", "Reporting, technical review and multilateral consideration improve transparency and accountability, but a submitted report or reviewed inventory is not proof that a target was achieved."),
    ("Global Stocktake boundary", "The Global Stocktake assesses collective progress toward the Agreement's purposes and informs later national action; it is not a country-specific compliance verdict or a replacement NDC."),
    ("CBDR-RC continuity", "Common but differentiated responsibilities and respective capabilities remains an equity principle, applied in light of different national circumstances; Paris universality did not erase differentiation."),
    ("Article 6 architecture", "Article 6.2 cooperative approaches, the Article 6.4 mechanism and Article 6.8 non-market approaches are distinct pathways; authorisation, accounting and delivery claims must not be merged."),
    ("Mitigation-adaptation-loss boundary", "Mitigation limits climate change, adaptation manages actual or expected impacts, and loss and damage concerns harms that remain; finance labels and institutions must preserve these distinctions."),
    ("Decision-pledge-delivery distinction", "An adopted COP or CMA decision, a Party announcement, a voluntary pledge, a finance goal, a contribution and verified disbursement are different facts with different legal and evidentiary status."),
    ("Treaty-decision hierarchy", "The Convention, Protocol, Agreement, amendment, COP or CMA decision, rulebook guidance and national instrument have different legal functions; a later decision implements but does not silently rewrite treaty text."),
    ("Current-outcome evidence boundary", "A presidency proposal, negotiating draft, roadmap, action-agenda release and adopted decision are not equivalent; current COP outcomes, Party counts, finance claims and NDC status require the final official source."),
]

TRAPS = [
    "Do not merge the UNFCCC convention with the Kyoto Protocol or Paris Agreement.",
    "Do not attribute a CMP or CMA decision generically to the COP without precision.",
    "Do not merge adoption, signature, ratification and entry into force.",
    "Do not say Kyoto imposed identical binding targets on every country.",
    "Do not use Annex and non-Annex labels without the instrument and historical context.",
    "Do not merge CDM, Joint Implementation and international emissions trading.",
    "Do not treat amendment adoption as entry into force.",
    "Do not say Paris assigns the same substantive numerical target to all Parties.",
    "Do not merge legally binding procedural duties with nationally determined ambition.",
    "Do not turn progression into a mandatory universal percentage.",
    "Do not treat transparency reporting as proof of target achievement.",
    "Do not treat the Global Stocktake as a national compliance verdict.",
    "Do not say Paris abolished CBDR-RC.",
    "Do not merge Article 6.2, 6.4 and 6.8.",
    "Do not merge mitigation, adaptation and loss and damage.",
    "Do not call a finance goal or pledge verified delivery.",
    "Do not convert a proposal, roadmap or draft into an adopted COP outcome.",
]

SESSION_TITLES = [
    "UNFCCC convention and COP CMP CMA framework",
    "Adoption signature ratification and entry into force",
    "Kyoto Protocol commitment architecture",
    "Annex I historical boundary",
    "Non-Annex Kyoto commitment boundary",
    "Kyoto mechanisms and Doha Amendment status",
    "Paris Agreement universal architecture",
    "Nationally Determined Contribution boundary",
    "Legally binding procedure and nationally determined ambition",
    "NDC progression and successive cycle",
    "Transparency framework and Global Stocktake",
    "CBDR-RC differentiation and equity",
    "Article 6 cooperative architecture",
    "Mitigation adaptation loss and decision-delivery distinctions",
    "Treaty decision pledge delivery and current-outcome audit",
]

ANSWER_ROUTES = [
    "Start with the Convention as framework and place every later instrument beneath it.",
    "Attribute each decision to COP, CMP or CMA and the relevant instrument.",
    "Use a legal-status timeline before claiming an instrument became operative.",
    "Define Kyoto by covered group, commitment period and quantified commitment architecture.",
    "Use Annex terminology only with its treaty and historical function.",
    "Compare each Kyoto mechanism by participants, unit and transaction pathway.",
    "Separate amendment text, ratification threshold, entry into force and period covered.",
    "Explain universal participation through nationally determined contributions.",
    "List procedural duties separately from the self-determined target level.",
    "Connect progression, highest possible ambition and successive communication without inventing a rate.",
    "Treat transparency as evidence infrastructure rather than an achievement certificate.",
    "Use the stocktake for collective progress and subsequent national updating.",
    "Apply differentiation through responsibility, capability and national circumstances.",
    "Separate Article 6 pathways and then distinguish mitigation, adaptation and residual harm.",
    "Close by ranking treaty text, adopted decision, announcement, finance goal and delivery evidence.",
]

PANELS = [
    panel("Climate-treaty hierarchy", "hierarchy", [
        "UNFCCC -> framework convention, principles and institutions",
        "KYOTO PROTOCOL -> commitment-period instrument under Convention",
        "PARIS AGREEMENT -> universal NDC-cycle agreement",
        "COP CMP CMA DECISIONS -> implementation and governance",
        "NATIONAL INSTRUMENTS -> domestic communication and action",
    ], [FACTS[0][0], FACTS[3][0], FACTS[8][0], FACTS[18][0]]),
    panel("Governing-body matrix", "comparison-table", [
        "COP -> Parties to the Convention",
        "CMP -> Parties to the Kyoto Protocol",
        "CMA -> Parties to the Paris Agreement",
        "DECISION LABEL -> identifies the governing body and session",
        "RULE -> never detach a decision from its instrument",
    ], [FACTS[1][0]]),
    panel("Legal-status ladder", "timeline", [
        "ADOPTION -> text agreed by the competent conference",
        "SIGNATURE -> political authentication where applicable",
        "RATIFICATION OR ACCESSION -> consent to be bound",
        "ENTRY INTO FORCE -> treaty conditions satisfied",
        "IMPLEMENTATION -> domestic and international operation",
    ], [FACTS[2][0], FACTS[7][0]]),
    panel("Kyoto coverage map", "comparison-table", [
        "ANNEX I COVERED GROUP -> quantified commitment architecture",
        "NON-ANNEX I -> no Kyoto-style quantified commitment",
        "COMMITMENT PERIOD -> time-bounded obligation",
        "CBDR-RC -> developed-country lead in historical design",
        "BOUNDARY -> do not project Kyoto's binary onto every Paris duty",
    ], [FACTS[3][0], FACTS[4][0], FACTS[5][0], FACTS[14][0]]),
    panel("Kyoto mechanism matrix", "comparison-table", [
        "EMISSIONS TRADING -> unit transfer across covered entities",
        "JOINT IMPLEMENTATION -> project pathway within Annex I setting",
        "CDM -> project pathway hosted in a developing country",
        "ACCOUNTING -> mechanism-specific units and rules",
        "NO MERGER -> participation and credit origins differ",
    ], [FACTS[6][0]]),
    panel("Kyoto-to-Paris replacement logic", "process-flow", [
        "KYOTO -> top-down quantified commitments for covered group",
        "PARTICIPATION LIMIT -> narrower substantive target coverage",
        "PARIS -> nationally determined contributions by all Parties",
        "TRANSPARENCY PLUS CYCLE -> iterative accountability design",
        "TRADE-OFF -> universality does not guarantee adequacy",
    ], [FACTS[3][0], FACTS[8][0], FACTS[9][0]]),
    panel("Paris obligation split", "comparison-table", [
        "PROCEDURE -> prepare, communicate and maintain successive NDCs",
        "DOMESTIC MEASURES -> pursue implementation action",
        "SUBSTANTIVE NUMBER -> nationally determined",
        "PROGRESSION -> next contribution expected to advance ambition",
        "NO UNIVERSAL CUT -> Agreement does not assign one percentage",
    ], [FACTS[9][0], FACTS[10][0], FACTS[11][0]]),
    panel("Transparency-to-stocktake rail", "process-flow", [
        "NATIONAL REPORTING -> inventory and progress information",
        "TECHNICAL REVIEW -> methods and consistency examined",
        "MULTILATERAL CONSIDERATION -> transparency dialogue",
        "GLOBAL STOCKTAKE -> collective progress assessment",
        "NEXT NDC -> nationally determined response informed by cycle",
    ], [FACTS[12][0], FACTS[13][0]]),
    panel("Differentiation compass", "layered-rail", [
        "COMMON RESPONSIBILITY -> all Parties participate",
        "DIFFERENTIATED RESPONSIBILITY -> historical and contextual equity",
        "CAPABILITY -> resources and institutional capacity matter",
        "NATIONAL CIRCUMSTANCES -> Paris application is contextual",
        "FINANCE AND TECHNOLOGY -> distinct support questions",
    ], [FACTS[14][0]]),
    panel("Article 6 fork", "decision-tree", [
        "6.2 -> cooperative approaches and transferred outcomes",
        "6.4 -> central mechanism under Paris governance",
        "6.8 -> non-market approaches",
        "ACCOUNTING -> authorisation and double-counting safeguards",
        "OUTCOME CLAIM -> requires verified delivery evidence",
    ], [FACTS[15][0]]),
    panel("Response-and-finance matrix", "comparison-table", [
        "MITIGATION -> limit sources or enhance sinks",
        "ADAPTATION -> reduce vulnerability and manage impacts",
        "LOSS AND DAMAGE -> residual harms",
        "GOAL OR PLEDGE -> stated commitment",
        "DELIVERY -> verified contribution or disbursement",
    ], [FACTS[16][0], FACTS[17][0]]),
    panel("Treaty answer spine", "answer-spine", [
        "IDENTIFY -> Convention, Protocol, Agreement or decision",
        "DATE -> adoption, ratification and entry into force separately",
        "COMPARE -> coverage, obligation, cycle and mechanism",
        "EVALUATE -> transparency, equity, finance and delivery",
        "AUDIT -> final adopted text, not draft or roadmap",
    ], [FACTS[18][0], FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2021", "GS-III",
        "Describe major COP26 outcomes and India's climate commitments at Glasgow.",
        "Verified routed Mains demand; India's target details are cross-owned by Topic 20.",
        [0, 1, 8, 9, 10, 14, 17, 19],
    ),
    common.make_pyq_solution(
        FACTS, "2022", "GS-III",
        "Discuss Kyoto Protocol measures while explaining global-warming greenhouse-gas effects.",
        "Verified routed Mains demand; physical science is cross-owned by Topic 17.",
        [0, 3, 4, 5, 6, 7, 14, 18],
    ),
    common.make_pyq_solution(
        FACTS, "2025", "GS-III",
        "Review India's Paris commitments, COP26 strengthening and updated NDC.",
        "Verified routed Mains demand; domestic targets are cross-owned by Topic 20.",
        [8, 9, 10, 11, 12, 13, 17, 19],
    ),
]

TOPIC_19 = common.topic(
    19,
    "UNFCCC COP Kyoto Paris Agreement",
    "19_UNFCCC-COP-Kyoto-Paris-Agreement",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-19_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Differentiate the UNFCCC, Kyoto Protocol and Paris Agreement.", [0, 3, 8]),
        (10, "Distinguish adoption, ratification, entry into force and implementation.", [2, 7, 18]),
        (15, "Compare Kyoto's commitment architecture with Paris NDCs.", [3, 4, 5, 8, 9, 10]),
        (15, "Explain the Paris progression, transparency and Global Stocktake cycle.", [11, 12, 13]),
        (20, "Evaluate differentiation, Article 6 and the response-finance architecture.", [14, 15, 16, 17]),
        (20, "Build a legally disciplined answer on climate-treaty evolution and current COP outcomes.", [0, 1, 2, 6, 8, 10, 13, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "UNFCCC", "Convention", "COP", "CMP", "CMA", "Kyoto Protocol",
        "Paris Agreement", "adoption", "signature", "ratification",
        "entry into force", "Annex I", "non-Annex I",
        "Clean Development Mechanism", "Joint Implementation",
        "international emissions trading", "Doha Amendment",
        "Nationally Determined Contribution", "procedural duties",
        "nationally determined", "progression", "transparency",
        "Global Stocktake", "CBDR-RC", "Article 6.2", "Article 6.4",
        "Article 6.8", "mitigation", "adaptation", "loss and damage",
        "adopted decision", "verified delivery",
    ],
    (
        "Audited ledgers route verified Mains demands on COP26, Kyoto measures, "
        "clean energy in international fora and India's Paris-to-updated-NDC "
        "progression, plus objective demands on climate initiatives and COP28 "
        "health declarations. The package records the demands without inventing "
        "a key, Party position, COP outcome or official model answer."
    ),
    PYQ_SOLUTIONS,
    UNFCCC_LIVE_SOURCE_ATTEMPTS,
    (
        "Direct UNFCCC retrieval was repeatedly blocked by Incapsula. Official "
        "search discovery located treaty-status, COP29 NCQG and COP30 package "
        "pages, but proposals, roadmaps and action-agenda releases were not "
        "converted into adopted decisions. No Party count, finance delivery, "
        "post-2025 NDC status or unverified COP outcome was asserted."
    ),
    extra=[
        "basic/17_Climate-Change-Science-Greenhouse-Effect.md",
        "basic/18_IPCC-Assessment-Reports.md",
        "basic/20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS.md",
        "basic/21_Carbon-Markets-CCUS-and-Direct-Air-Capture.md",
        "advanced/18_IPCC-Assessment-Reports.md",
        "advanced/20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS.md",
        "advanced/21_Carbon-Markets-CCUS-and-Direct-Air-Capture.md",
    ],
    pyq_audit_heading="AUDITED UNFCCC, KYOTO, PARIS, COP AND INDIA-COMMITMENT PYQ OWNERSHIP",
    register_headings=(
        "CONVENTION, KYOTO, PARIS, GOVERNING-BODY AND STATUS MAP",
        "ANNEX, PROCEDURE, NDC, STOCKTAKE, ARTICLE 6 AND FINANCE TRAPS",
        "CLIMATE-TREATY ANSWER SPINE",
        "LIVE COP DECISION, PARTY, NDC, FINANCE AND DELIVERY EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "IDENTIFY THE CONVENTION, PROTOCOL, AGREEMENT OR IMPLEMENTING DECISION",
        "SEPARATE ADOPTION, SIGNATURE, RATIFICATION AND ENTRY INTO FORCE",
        "COMPARE KYOTO COVERAGE WITH PARIS UNIVERSAL NDC PARTICIPATION",
        "SEPARATE PROCEDURAL DUTIES FROM NATIONALLY DETERMINED AMBITION",
        "TRACE TRANSPARENCY, GLOBAL STOCKTAKE AND SUCCESSIVE NDC CYCLE",
        "APPLY CBDR-RC AND DISTINGUISH ARTICLE 6 PATHWAYS",
        "CONCLUDE WITH ADOPTED TEXT, PLEDGE, GOAL AND DELIVERY DISCIPLINE",
    ],
)
