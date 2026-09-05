"""Authored data for Environment and Ecology learner-v2 Topic 09."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import CITES_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("Trade jurisdiction", "CITES regulates international trade in listed wild fauna and flora; it does not itself regulate domestic habitat loss, domestic hunting or purely internal consumption."),
    ("Appendix I boundary", "Appendix I covers species threatened with extinction and subjects trade to particularly strict regulation, with authorization confined to exceptional circumstances; listing is not a shorthand for every domestic activity being banned."),
    ("Appendix II boundary", "Appendix II covers species that may become threatened unless trade is controlled and can also support control of specimens whose identification must be linked to listed taxa; regulated trade is not the same as unrestricted trade."),
    ("Appendix III boundary", "Appendix III begins with a Party that already regulates a species within its jurisdiction and seeks other Parties' cooperation in controlling international trade; it is not a third extinction-risk rank."),
    ("Listing versus trade ban", "An Appendix identifies the applicable international-trade control architecture; the lawful result still depends on Appendix, specimen, transaction, origin, purpose, reservation and the required permit or certificate."),
    ("Specimen discipline", "A CITES answer must identify the exact specimen or product and verify the accepted scientific name; a species name, processed derivative and shipment description cannot be treated as interchangeable evidence."),
    ("Source discipline", "Source or origin information is part of permit scrutiny, but no wild, captive-bred or artificially propagated status should be assumed without the transaction document and applicable CITES guidance."),
    ("Permit matrix", "Import, export, re-export and introduction from the sea are distinct transactions; their documents and findings vary, so an export permit cannot be used as a universal label for every CITES movement."),
    ("Non-detriment finding", "The Scientific Authority's non-detriment finding is the science gate for relevant exports and must remain distinct from the Management Authority's decision to issue a permit or certificate."),
    ("Legal-acquisition check", "Permit scrutiny also requires the applicable authority to be satisfied about lawful acquisition where the Convention and domestic implementation require it; an NDF alone is not the whole permit test."),
    ("Management Authority", "A national Management Authority administers permits and certificates; it does not replace the Scientific Authority's conservation advice or customs' border-verification role."),
    ("Scientific Authority", "A national Scientific Authority advises on whether trade is detrimental and on related scientific questions; it does not issue the trade document merely because it supplied advice."),
    ("Appendix amendment route", "Appendix I and II amendments use the Conference of the Parties voting route described in the owners, while Appendix III can be initiated unilaterally by a Party; the three routes must not be merged."),
    ("Reservation boundary", "A reservation concerns the reserving Party's treaty treatment for the specified taxon or amendment; it does not erase the listing for all Parties or automatically rewrite another country's domestic law."),
    ("Domestic implementation", "India's post-2022 Wildlife Protection Act architecture uses Schedule IV and designated CITES authorities for scheduled specimens, but a CITES decision and the applicable Indian legal update remain separate steps."),
    ("Enforcement chain", "Effective control depends on the chain from scientific finding and permit issuance to species identification, customs inspection, intelligence and cross-border cooperation; listing alone does not verify a shipment."),
    ("WCCB boundary", "WCCB supports organised wildlife-crime intelligence and enforcement coordination under the domestic statute; it is not the CITES Conference, Scientific Authority or universal permit issuer."),
    ("CITES-IUCN-CMS split", "CITES controls international trade, IUCN assesses extinction risk and CMS coordinates conservation across migratory ranges; overlap for one species never makes the three systems legally identical."),
    ("Zero-direct-PYQ audit", "The audited 2018-2026 routing ledgers contain no question directly owned by Topic 09; adjacent wildlife-law and convention concepts are taught, but no year, wording or answer key is invented."),
    ("Live-status boundary", "Official CITES pages attempted on 2026-09-03 returned HTTP 403, so the package asserts no current Party count, species Appendix placement, reservation, permit condition or COP outcome beyond repository-owned mechanics."),
]

TRAPS = [
    "Do not turn international-trade regulation into domestic habitat or hunting law.",
    "Do not describe Appendix I as an exception-free global ban on every transaction.",
    "Do not describe Appendix II as free trade merely because trade can be authorised.",
    "Do not rank Appendix III below Appendix II as an extinction-risk category.",
    "Do not treat a listing as proof that the transaction has the required documents.",
    "Do not infer specimen identity from a common name or processed-product label.",
    "Do not infer source code or captive-bred status without the document.",
    "Do not use export permit as the document for every transaction type.",
    "Do not merge the Scientific and Management Authority functions.",
    "Do not treat an NDF as the only permit condition.",
    "Do not make a CITES change automatically rewrite Schedule IV.",
    "Do not make a reservation cancel the listing for all Parties.",
    "Do not make WCCB the decision-maker for every trade document.",
    "Do not equate CITES Appendix, IUCN category and CMS Appendix.",
    "Do not invent a direct PYQ or current species listing from a failed webpage.",
]

SESSION_TITLES = [
    "CITES jurisdiction and Appendix I strict control",
    "Appendix II regulated trade",
    "Appendix III unilateral cooperation route",
    "Listing versus transaction legality",
    "Specimen identity and product discipline",
    "Source origin and transaction matrix",
    "Non-detriment finding",
    "Legal acquisition and the complete permit gate",
    "Management Authority",
    "Scientific Authority",
    "COP amendment and reservation routes",
    "India Schedule IV implementation",
    "Permit verification customs and WCCB",
    "CITES IUCN and CMS distinction",
    "Zero-direct-PYQ and live-status firewall",
]

ANSWER_ROUTES = [
    "Fix CITES at the trade border and state Appendix I control without an absolute ban.",
    "Describe authorization as regulated trade, not permission by default.",
    "Explain the unilateral cooperation-request logic without ranking extinction risk.",
    "Move from Appendix to specimen, transaction, purpose and document.",
    "Verify scientific identity before applying a listing or permit rule.",
    "Treat source as documentary evidence and name the transaction before its document.",
    "Assign the scientific trade-impact finding to the Scientific Authority.",
    "Add lawful acquisition and other applicable findings to the permit analysis.",
    "Assign permit administration to the Management Authority.",
    "Keep conservation advice separate from document issuance.",
    "Contrast COP amendment, unilateral Appendix III and taxon-specific reservation.",
    "Trace treaty status to the separate Indian legal update.",
    "Follow the permit through species identification, customs and WCCB coordination.",
    "Separate trade regulation, risk assessment and migratory-range cooperation.",
    "Close with the zero-direct-PYQ audit and failed current-status retrieval.",
]

PANELS = [
    panel("Jurisdiction firewall", "layered-rail", [
        "CITES -> international movement of listed specimens",
        "DOMESTIC HUNTING -> domestic wildlife law",
        "HABITAT LOSS -> land, forest and protected-area law",
        "LOCAL CONSUMPTION -> domestic enforcement and demand reduction",
        "RULE -> treaty scope is trade-specific, not species-protection complete",
    ], [FACTS[0][0], FACTS[17][0]]),
    panel("Appendix comparison", "comparison-table", [
        "APPENDIX I -> threatened with extinction; particularly strict trade control",
        "APPENDIX II -> trade controlled to avoid incompatible utilization",
        "APPENDIX III -> one Party seeks cooperation for a species it regulates",
        "COMMON THREAD -> international trade documents and verification",
        "NOT A LADDER -> Appendix III is not a lower extinction-risk score",
    ], [FACTS[1][0], FACTS[2][0], FACTS[3][0]]),
    panel("Listing-to-transaction gate", "decision-tree", [
        "LISTING FOUND -> verify accepted scientific name",
        "IDENTIFY -> specimen or processed product",
        "CLASSIFY -> import, export, re-export or introduction from sea",
        "CHECK -> origin, purpose, reservation and required document",
        "VERDICT -> listing alone never proves lawful or unlawful movement",
    ], [FACTS[4][0], FACTS[5][0], FACTS[7][0]]),
    panel("Specimen and source check", "process-flow", [
        "SHIPMENT LABEL -> compare with accepted taxon",
        "PART OR DERIVATIVE -> verify recognizability and listing scope",
        "SOURCE CLAIM -> inspect the transaction document",
        "NO SHORTCUT -> captive or propagated origin is not presumed",
        "OUTPUT -> source-bounded specimen identity",
    ], [FACTS[5][0], FACTS[6][0]]),
    panel("Transaction matrix", "comparison-table", [
        "IMPORT -> entry into a State",
        "EXPORT -> departure from the State of origin",
        "RE-EXPORT -> departure after prior import",
        "INTRODUCTION FROM SEA -> separate Convention transaction",
        "RULE -> required findings and documents vary by transaction",
    ], [FACTS[7][0]]),
    panel("Science-to-permit chain", "process-flow", [
        "SCIENTIFIC AUTHORITY -> assesses detriment",
        "NDF -> science gate where applicable",
        "LEGAL ACQUISITION -> separate compliance finding where required",
        "MANAGEMENT AUTHORITY -> issues permit or certificate",
        "BORDER -> document and specimen still require verification",
    ], [FACTS[8][0], FACTS[9][0], FACTS[10][0], FACTS[11][0]]),
    panel("Authority split", "authority-map", [
        "SCIENTIFIC AUTHORITY -> trade-impact advice",
        "MANAGEMENT AUTHORITY -> document administration",
        "CUSTOMS -> border control and declaration checks",
        "WCCB -> wildlife-crime intelligence and coordination",
        "NO MERGER -> each institution keeps its own decision boundary",
    ], [FACTS[10][0], FACTS[11][0], FACTS[16][0]]),
    panel("Appendix-change routes", "decision-gate", [
        "APPENDIX I OR II -> COP amendment route",
        "APPENDIX III -> unilateral Party request route",
        "RESERVATION -> specified Party and specified taxon treatment",
        "INDIAN UPDATE -> separate domestic legal step",
        "CAUTION -> proposal, adoption and domestic effect are different states",
    ], [FACTS[12][0], FACTS[13][0], FACTS[14][0]]),
    panel("India implementation bridge", "layered-rail", [
        "CITES DECISION -> international treaty plane",
        "SCHEDULE IV -> Indian scheduled-specimen plane",
        "DESIGNATED AUTHORITIES -> science and permit plane",
        "CUSTOMS AND WCCB -> enforcement plane",
        "RULE -> no automaticity across the four planes",
    ], [FACTS[14][0], FACTS[15][0], FACTS[16][0]]),
    panel("Enforcement weakest-link map", "process-flow", [
        "POPULATION EVIDENCE -> credible NDF",
        "PERMIT INTEGRITY -> authentic document",
        "SPECIES IDENTIFICATION -> correct specimen match",
        "BORDER COORDINATION -> customs and wildlife enforcement",
        "DEMAND REDUCTION -> complementary domestic response",
    ], [FACTS[8][0], FACTS[15][0]]),
    panel("Convention distinction matrix", "comparison-table", [
        "CITES -> international wildlife trade",
        "IUCN -> scientific extinction-risk assessment",
        "CMS -> migratory-range cooperation",
        "WILDLIFE ACT -> domestic legal consequences",
        "RULE -> one species may occupy all layers without merging them",
    ], [FACTS[17][0]]),
    panel("Audit and answer spine", "answer-spine", [
        "SCOPE -> international trade only",
        "APPENDIX -> I, II or III mechanics",
        "TRANSACTION -> specimen, source, purpose and document",
        "AUTHORITY -> science, permit and enforcement roles",
        "QUALIFY -> zero direct PYQ and failed current-listing retrieval",
    ], [FACTS[18][0], FACTS[19][0]]),
]

TOPIC_09 = common.topic(
    9,
    "CITES and Wildlife Trade",
    "09_CITES-and-Wildlife-Trade",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-09_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish the three CITES Appendices without treating them as one prohibition ladder.", [0, 1, 2, 3, 4]),
        (10, "Explain why specimen, source and transaction must be fixed before applying a CITES permit rule.", [5, 6, 7]),
        (15, "Explain the CITES science-to-permit chain and its institutional division of labour.", [8, 9, 10, 11, 15]),
        (15, "Distinguish COP amendments, Appendix III listing, reservations and Indian domestic implementation.", [12, 13, 14, 16]),
        (20, "Critically assess why Appendix listing alone cannot eliminate illegal wildlife trade.", [0, 4, 8, 9, 15, 16]),
        (20, "Design an India-facing answer on CITES that preserves treaty, domestic-law and evidence boundaries.", [0, 5, 7, 14, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "international trade", "Appendix I", "Appendix II", "Appendix III",
        "specimen", "source", "import", "export", "re-export",
        "introduction from the sea", "non-detriment finding",
        "Management Authority", "Scientific Authority", "reservation",
        "Schedule IV", "WCCB", "listing alone", "zero-direct-PYQ",
    ],
    (
        "Audited 2018-2026 routing ledgers contain no direct Topic 09 demand. "
        "Adjacent treaty, wildlife-law and trafficking concepts are taught as "
        "practice, but no PYQ wording, year, official option key or answer is invented."
    ),
    [],
    CITES_LIVE_SOURCE_ATTEMPTS,
    (
        "All attempted official CITES mechanics, Appendices, treaty-text and "
        "Parties pages returned HTTP 403 on 2026-09-03. No current Party count, "
        "species Appendix placement, reservation, permit condition or COP outcome "
        "was imported. MoEFCC text was used only for WCCB's domestic boundary."
    ),
    extra=[
        "basic/05_IUCN-Red-List-and-Endemism.md",
        "basic/08_Wildlife-Protection-Act-and-Schedules.md",
        "basic/10_CMS-Bonn-Convention-Migratory-Species.md",
        "advanced/08_Wildlife-Protection-Act-and-Schedules.md",
        "advanced/10_CMS-Bonn-Convention-Migratory-Species.md",
    ],
    pyq_audit_heading="TRANSPARENT ZERO-DIRECT-PYQ OWNERSHIP AUDIT",
    allow_existing_history=True,
    register_headings=(
        "APPENDIX, SPECIMEN, SOURCE AND TRANSACTION MAP",
        "PERMIT, AUTHORITY, RESERVATION AND DOMESTIC-LAW TRAPS",
        "CITES ANSWER SPINE",
        "LIVE APPENDIX, PARTY, COP AND PYQ EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "FIX THE DIRECT JURISDICTION: INTERNATIONAL TRADE",
        "IDENTIFY APPENDIX I, II OR III WITHOUT INVENTING A CURRENT LISTING",
        "VERIFY TAXON, SPECIMEN, SOURCE, PURPOSE AND TRANSACTION",
        "SEPARATE SCIENTIFIC FINDING FROM MANAGEMENT DOCUMENT",
        "TRACE CUSTOMS AND WCCB VERIFICATION",
        "SEPARATE CITES, IUCN, CMS AND INDIAN DOMESTIC LAW",
        "CONCLUDE WITH PERMIT INTEGRITY AND COMPLEMENTARY HABITAT PROTECTION",
    ],
)
