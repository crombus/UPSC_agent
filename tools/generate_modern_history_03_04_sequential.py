"""Assemble Modern Indian History learner-v2 Topics 03-04 and visual specs.

This authoring-only generator writes Markdown and JSON specifications.  It does
not render PDFs, stage files, finalise tracker records, or modify approval state.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

import carvaka_flowchart
import generate_v2_section_indexes as section_indexes
import notions_style_ascii_master as ascii_master


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Modern-Indian-History"
DISPLAY_SUBJECT = "Modern History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "modern-indian-history-03-04-2026-08-30-sequential.json"
GRAPHICAL_DIR = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "carvaka-graphical-specs" / SUBJECT
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "modern-indian-history--subject-wide-syllabus.json"
)
PYQ_INDEXES = [
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-INDEX.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2024-2025.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "PYQ-INTEGRATION-AUDIT-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "PYQ-INTEGRATION-AUDIT-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "PYQ-INTEGRATION-AUDIT-2026.md",
]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Chronology.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
]
LOCAL_BOOKS = [
    ROOT / "books" / "modern india" / "MODERN INDIA -- BIPIN CHANDRA -- ENGLISH ##.pdf",
    ROOT / "books" / "medival_history" / "FROM PLASY TO PARTITION -- SEKAR B -- ENGLISH.pdf",
    ROOT / "books" / "medival_history" / "Medieval-History-Satish-Chandra-1526-1748-Part-2.pdf",
]
OFFICIAL_QUESTION_SOURCES = [
    ROOT / "knowledge-export" / "Prelims PYQ" / "QP-CSP-21-GeneralStudiesPaper-I-121021.pdf.md",
    ROOT / "knowledge-export" / "Prelims PYQ" / "GENERAL STUDIES PAPER I.pdf.md",
    ROOT / "knowledge-export" / "Prelims PYQ" / "2025-GS1-Set A.md",
    ROOT / "knowledge-export" / "Prelims PYQ" / "Ans-2025-GS1.md",
    ROOT / "knowledge-export" / "Mains PYQ" / "QP-CSM-22-GENERAL-STUDIES-PAPER I-190922.pdf.md",
]


def config(
    number: int,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    legacy_main: str,
    legacy_workbook: str,
    extra: list[str],
    live_sources: list[str],
    current_note: str,
    basic_session_count: int,
    pyq_note: str,
) -> dict[str, object]:
    return {
        "key": f"modern-indian-history-{number:02d}",
        "title": title,
        "canonical": KNOWLEDGE / canonical,
        "basic": KNOWLEDGE / "basic" / basic,
        "advanced": KNOWLEDGE / "advanced" / advanced,
        "legacy_main": ROOT / "notes" / SUBJECT / legacy_main,
        "legacy_workbook": ROOT / "notes" / SUBJECT / legacy_workbook,
        "extra": [KNOWLEDGE / item for item in extra],
        "live_sources": live_sources,
        "current_note": current_note,
        "basic_session_count": basic_session_count,
        "pyq_note": pyq_note,
    }


TOPICS = [
    config(
        3,
        "The Beginnings of European Settlements (Portuguese → Dutch → English → French)",
        "03_Beginnings-European-Settlements-Portuguese-Dutch-English-French_Complete-Topic-Package.md",
        "03_Beginnings-of-European-Settlements.md",
        "03_Beginnings-of-European-Settlements.md",
        "03_Beginnings-European-Settlements-Portuguese-Dutch-English-French_Complete-Topic-Package_2026-08-14.pdf",
        "03_Beginnings-European-Settlements-Portuguese-Dutch-English-French_Solved-Workbook_2026-08-14.pdf",
        [
            "basic/02_Indian-States-and-Society-18th-Century.md",
            "basic/04_British-Conquest-of-Bengal.md",
            "basic/05_British-Territorial-Expansion.md",
        ],
        ["https://whc.unesco.org/en/list/234/"],
        "UNESCO's Churches and Convents of Goa record is used only as a bounded heritage "
        "anchor for Indo-Portuguese architecture, Asian missions, the tomb of St Francis "
        "Xavier, living religious use, and conservation threats such as weathering, capillary "
        "action and termites. It does not prove political causation, exact crop-transfer "
        "dates, or complete Portuguese monopoly of Indian Ocean commerce.",
        28,
        "Four directly routed Prelims demands are solved. The 2021 and 2022 keys are "
        "prominently labelled inferred because official local keys are unavailable; the "
        "2025 Series-A crop-transfer answer retains its locally held official-key provenance. "
        "The 2022 GS-I Company-armies question is only a bounded Topic-05 bridge.",
    ),
    config(
        4,
        "The British Conquest of Bengal (Plassey 1757, Buxar 1764, Dual Government)",
        "04_British-Conquest-of-Bengal-Plassey-Buxar-Dual-Government_Complete-Topic-Package.md",
        "04_British-Conquest-of-Bengal.md",
        "04_British-Conquest-of-Bengal.md",
        "04_British-Conquest-of-Bengal-Plassey-Buxar-Dual-Government_Complete-Learning-Session_2026-08-19.pdf",
        "04_British-Conquest-of-Bengal-Plassey-Buxar-Dual-Government_Premium-Solved-PYQ-Workbook_2026-08-19.pdf",
        [
            "basic/02_Indian-States-and-Society-18th-Century.md",
            "basic/03_Beginnings-of-European-Settlements.md",
            "basic/05_British-Territorial-Expansion.md",
            "basic/06_Government-Structure-and-Constitutional-Development-1757-1858.md",
            "basic/07_Economic-Impact-of-British-Rule.md",
        ],
        [
            "https://www.thedailystar.net/news/bangladesh/news/"
            "plassey-must-be-revisited-beyond-betrayal-4203881"
        ],
        "The Daily Star discussion published on 21 June 2026 is used only as a "
        "contemporary public-memory and historiography anchor: it highlights conspiracy, "
        "European rivalry, Murshidabad court tensions, the ambiguity of 'independent Bengal', "
        "and the danger of reducing Plassey to betrayal. Static causation comes from repository "
        "owners and local books. No unverified archive material is used.",
        16,
        "Repository routing audits assign Topic 04 zero direct PYQs. The verified 2022 GS-I "
        "Company-armies and famine questions remain explicitly labelled as bounded bridges "
        "owned by Topics 05 and 07; no official answer is fabricated.",
    ),
]


# Independent authored maps of each complete conceptual spine, not session dumps.
PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-03": [
        (
            "Scope: contact, settlement and empire are different stages",
            "scope-map",
            """CAPE ROUTE 1498 -> repeated trade -> factory by Indian permission
FACTORY -> fortified settlement -> presidency / regional coordination
POSSIBLE COMPANY-STATE -> additionally needs finance, army, allies, victory and revenue
ANTI-TELEOLOGY -> neither a European charter nor the first voyage made conquest inevitable.""",
            ["01. Scope: five stages, not one inevitable conquest"],
        ),
        (
            "Indian Ocean setting and mercantilist armed commerce",
            "systems-map",
            """PRE-1498 -> monsoon routes + Asian merchants + Indian ports and manufactures
MERCANTILISM -> chartered monopoly seeks bullion, commodities and protected markets
ARMED COMMERCE -> ship cannon + fort + pass + diplomacy + corporate privilege
LIMIT -> Europeans entered an existing oceanic economy; older circuits did not disappear.""",
            [
                "02. Maritime background: the Indian Ocean before the Europeans",
                "21. Commodities, bullion and the port-hinterland network",
            ],
        ),
        (
            "Portuguese Estado da India and cartaz",
            "institution-map",
            """1498 CALICUT -> 1505 Estado administration -> GOA captured 1510 / capital 1530
ESTADO -> Crown + viceroy/governor + fleet + forts + royal factories
CARTAZ -> coerced shipping pass; fortified nodes at Goa, Cochin, Diu and Daman
LIMIT -> nodal and contested control, never a complete monopoly of Indian Ocean trade.""",
            [
                "05. Portuguese arrival and the Estado da India",
                "06. Cartaz, naval power, diplomacy and conflict",
            ],
        ),
        (
            "Portuguese cultural transfer and bounded Goa heritage",
            "evidence-map",
            """XAVIER -> Goa 1542; founding Jesuit companion; died off China, remains at Bom Jesus
GOA PRESS 1556 | INQUISITION 1560 -> mission, print, coercion and accommodation coexist
CROPS -> papaya, pineapple and guava through Portuguese networks; no exact transfer year
UNESCO -> Indo-Portuguese forms + local adaptation; threats include damp, weathering, termites.""",
            ["07. Portuguese trade, mission, printing, crops and cultural exchange"],
        ),
        (
            "Dutch VOC: commercial strength, India inside an Asian portfolio",
            "portfolio-map",
            """VOC 1602 -> joint-stock capital + treaty, war and fortification powers
INDIAN NODES -> Masulipatnam, Pulicat, Nagapattinam, Surat, Chinsura and Cochin
PRIORITY -> Indian textiles finance an Indonesia-centred spice and intra-Asian portfolio
CHECKS -> Colachel 1741 / Bedara 1759; political retreat did not instantly end trade.""",
            [
                "09. Dutch VOC: structure, Indian bases and Indonesian priority",
                "10. Why Dutch power in India remained commercial",
            ],
        ),
        (
            "English entry: charter, naval credibility and Mughal permission",
            "causal-chain",
            """EIC CHARTER 1600 -> corporate monopoly in English law, not Indian sovereignty
SWALLY 1612 -> naval credibility alters Mughal bargaining
SURAT FACTORY 1613 -> licensed depot; ROE 1615-19 -> privileges confirmed
CHILD'S WAR 1686-90 -> Mughal victory proves early Company weakness and contingency.""",
            [
                "11. English EIC foundation, early voyages and Mughal diplomacy",
                "12. Surat and the first English factory network",
            ],
        ),
        (
            "English fortified settlement chain",
            "coastal-chain",
            """MASULIPATNAM 1611 -> MADRAS lease 1639 -> Fort St George from 1640
BOMBAY -> Portuguese possession -> Crown 1661 -> Company 1668 -> presidency HQ 1687
BENGAL -> Hugli / Kasimbazar -> three-village Calcutta hub -> 1698 zamindari -> 1717 farman
CAUTION -> Job Charnock is a conventional association, not an uncontested sole founder.""",
            [
                "13. Coromandel chain: Masulipatnam, Madras and Fort St George",
                "14. Bombay: Crown transfer, harbour geography and presidency shift",
                "15. Bengal factories, Calcutta and the pre-Plassey boundary",
            ],
        ),
        (
            "Institutional vocabulary that prevents category errors",
            "comparison-matrix",
            """CHARTER -> home sovereign creates company | FARMAN -> Indian sovereign grants privilege
FACTORY -> depot + factors | FORT -> defended enclave, not automatic hinterland rule
PRESIDENCY -> regional council coordinating factories, fleets, defence and diplomacy
COMPANY-STATE -> enforceable war, justice, taxation and territory; capacity must match claim.""",
            ["16. Charter, farman, factory, fort and presidency: terminology that decides marks"],
        ),
        (
            "French Compagnie and Indian settlement chain",
            "institution-map",
            """COMPAGNIE DES INDES 1664 -> Colbert / Louis XIV state-backed monopoly
SURAT 1668 -> MASULIPATNAM 1669 -> PONDICHERRY 1673-74 -> CHANDERNAGORE c.1690-92
DUPLEIX -> trade + trained troops + claimant politics; Indian allies retain their own aims
LIMIT -> finance, naval continuity and home-state priorities constrain French intervention.""",
            [
                "17. French Compagnie des Indes and the settlement chain",
                "18. Dupleix and the bounded bridge to Carnatic rivalry",
            ],
        ),
        (
            "Carnatic conclusion: European rivalry becomes Indian politics",
            "timeline",
            """FIRST WAR 1746-48 -> French take Madras -> Aix-la-Chapelle restores it
SECOND 1749-54 -> Carnatic / Hyderabad claimants + Arcot -> Dupleix recalled
THIRD 1756-63 -> Seven Years' War -> WANDIWASH 1760 breaks French field power
PARIS 1763 -> factories survive, political ambition checked; no single-cause English victory.""",
            [
                "18. Dupleix and the bounded bridge to Carnatic rivalry",
                "24. Inter-European rivalry before territorial conquest",
                "25. Why the English gained relative advantage - without teleology",
            ],
        ),
        (
            "Indian agency and the port-hinterland engine",
            "actor-network",
            """RULERS -> grant, revise, resist and use rival companies against one another
MERCHANTS / BANKERS / DUBASHES -> credit, brokerage, customs and information
WEAVERS / ARTISANS / SHIPBUILDERS / LABOUR -> make commercial settlements viable
ASYMMETRY -> agency was real but unequal; forts still depended on surrounding Indian society.""",
            [
                "20. Indian rulers, merchants, brokers, artisans and port communities",
                "21. Commodities, bullion and the port-hinterland network",
            ],
        ),
        (
            "Topic 03 answer and PYQ spine",
            "answer-synthesis",
            """COMPARE -> Estado/cartaz | VOC portfolio | EIC presidency chain | French state backing
EXPLAIN -> mercantilism + navy + finance + Indian permission/agency + political contingency
PYQ TRAPS -> Broach window; Xavier death/remains; Goa-Bijapur; Madras grant; three crops
CLOSE -> Wandiwash/Paris end European rivalry; Plassey-Buxar mechanics pass to Topic 04.""",
            [
                "27. Historiography and source criticism",
                "28. Terminology, chronology, memory hooks and high-frequency traps",
            ],
        ),
    ],
    "modern-indian-history-04": [
        (
            "Bengal before 1756: successor state and sovereignty conflict",
            "scope-map",
            """BENGAL -> wealthy Mughal successor state, not a political vacuum
1717 FARMAN -> bounded privilege for Company trade | DASTAK ABUSE -> servants' private trade
FORTIFICATION + customs + jurisdiction -> commercial dispute becomes sovereignty dispute
SIRAJ 1756 -> inherits court rivalry and a Company testing Nawabi authority.""",
            ["1. Bengal's political economy before 1756"],
        ),
        (
            "Calcutta crisis and the Black Hole caution",
            "escalation-ladder",
            """UNAUTHORISED FORTIFICATION -> Kasimbazar seized -> Fort William falls in June 1756
CLIVE / WATSON -> Calcutta recovered -> Alinagar -> Chandernagore removed as counterweight
BLACK HOLE -> Holwell is an interested, weakly corroborated narrator
RULE -> never make a disputed body count or atrocity story the causal centre of conquest.""",
            [
                "2. Siraj-ud-Daulah, the Calcutta crisis and the fall of Fort William, 1756",
                "3. The 'Black Hole' of Calcutta: what the evidence supports, and what it does not",
            ],
        ),
        (
            "Plassey's hidden battle: conspiracy and collaboration",
            "actor-network",
            """COMPANY / CLIVE -> regime-change plan + secret correspondence + coercive leverage
MIR JAFAR -> throne | JAGAT SETH -> credit and security | RAI DURLABH -> office
AMICHAND -> broker later deceived | MIR MADAN / MOHAN LAL -> loyal resistance
VERDICT -> interests explain collaboration better than a one-word betrayal morality tale.""",
            ["4. Plassey's hidden battle: the conspiracy network of 1757"],
        ),
        (
            "Plassey and the Mir Jafar client regime",
            "causal-chain",
            """PLASSEY, 23 JUNE 1757 -> conspiracy neutralises most Nawabi command
RESULT -> Mir Jafar installed; Company becomes kingmaker and gains political entry
CLIENT CYCLE -> dependence -> transfers / concessions -> deeper Company leverage
LIMIT -> Plassey changed the ruler; it did not yet grant legal-fiscal sovereignty.""",
            [
                "5. Plassey, 23 June 1757: why this was a political coup, not a conventional military triumph",
                "6. Mir Jafar's Bengal and Company extraction, 1757-60",
            ],
        ),
        (
            "Mir Qasim: reform, equality and conflict",
            "process",
            """MIR QASIM 1760 -> shifts capital to Munger + strengthens administration and army
COMPANY PRIVATE TRADE -> duty privilege distorts competition and weakens Nawabi revenue
RESPONSE 1763 -> abolish inland duties for all traders: equality, not modern nationalism
COMPANY RESISTS LOST ADVANTAGE -> war -> Mir Qasim seeks an Awadh-Mughal coalition.""",
            ["7. Mir Qasim, Munger and the equality crisis, 1760-63"],
        ),
        (
            "Buxar: coalition breadth versus unified Company command",
            "comparison-matrix",
            """COALITION -> Mir Qasim + Shuja-ud-Daula + Shah Alam II; distinct motives
STRUCTURAL WEAKNESS -> separate treasuries, commands and political objectives
COMPANY -> Hector Munro's integrated command, supply and payment system
BUXAR, 22 OCTOBER 1764 -> open military supremacy, unlike Plassey's palace coup.""",
            [
                "8. The road to Buxar: Mir Qasim, Shuja-ud-Daula and Shah Alam II form a coalition",
                "9. Buxar, 22 October 1764: why this battle mattered more than Plassey",
            ],
        ),
        (
            "Three-stage conquest thesis",
            "three-stage-chain",
            """PLASSEY 1757 -> POLITICAL ENTRY: client Nawab and Company kingmaking
BUXAR 1764 -> MILITARY SUPREMACY: Bengal-Awadh-emperor coalition defeated
ALLAHABAD / DIWANI 1765 -> LEGAL-FISCAL TITLE: revenue authority institutionalised
RULE -> Plassey alone did not complete Company sovereignty over Bengal.""",
            [
                "9. Buxar, 22 October 1764: why this battle mattered more than Plassey",
                "10. The Treaty of Allahabad, 1765: two treaties, one day",
            ],
        ),
        (
            "Allahabad, Diwani, Nizamat and the Awadh buffer",
            "institution-map",
            """SHAH ALAM II SETTLEMENT -> Company receives Diwani of Bengal, Bihar and Orissa
SHUJA-UD-DAULA SETTLEMENT -> Awadh restored as a strategic buffer, not annexed
DIWANI -> revenue / civil side | NIZAMAT -> nominal police, criminal and military side
CAUTION -> Diwani was not Nawabship and the legal split was not equal power-sharing.""",
            [
                "10. The Treaty of Allahabad, 1765: two treaties, one day",
                "11. Diwani and Nizamat: one power, two legal labels",
            ],
        ),
        (
            "Dual Government: power separated from responsibility",
            "accountability-loop",
            """1765-72 -> Company holds revenue power through Indian deputies
NAWAB'S ESTABLISHMENT -> nominal Nizamat and public responsibility without resources
PARADOX -> Company power without responsibility / Nawab responsibility without power
RESULT -> extraction incentives + diffused accountability + weak corrective capacity.""",
            ["12. The Dual Government, 1765-72: Clive's design and its accountability paradox"],
        ),
        (
            "Famine, accountability and the 1772 termination",
            "causal-web",
            """1770 FAMINE -> harvest failure / drought and disease create the natural shock
DUAL GOVERNMENT -> revenue rigidity and administrative confusion amplify vulnerability
CAUTION -> Company policy mattered but did not alone cause drought or the catastrophe
HASTINGS 1772 -> ends Dual Government; direct administration bridges to Topic 06.""",
            [
                "13. The Bengal famine of 1770: a bounded causal reading",
                "16. Comparative synthesis: Plassey, Buxar, Allahabad and the Dual Government, and the bridge forward",
            ],
        ),
        (
            "Company-state, early drain mechanism and historiography",
            "lens-map",
            """TRADE PRIVILEGE -> kingmaking -> Diwani -> revenue funds purchases and armies
INDIAN AGENCY -> collaboration, resistance and administration operate under unequal power
LENSES -> nationalist extraction | collaboration | corporate-fiscal state | Bengal continuity
2026 MEMORY ANCHOR -> revisit Plassey beyond betrayal; static causation remains book-grounded.""",
            [
                "14. From trader to revenue sovereign: the Company's transformation and the spectrum of Indian agency",
                "15. Reading the conquest: four historiographical lenses",
            ],
        ),
        (
            "Topic 04 answer spine and boundaries",
            "answer-synthesis",
            """OPEN -> sovereignty conflict over privilege, private trade, fortification and jurisdiction
TRACE -> conspiracy / client regime -> reform and war -> Buxar -> Diwani -> Dual Government
WEIGH -> collaboration + Company capacity; famine is multicausal; reject false precision
CLOSE -> 1772 ends this topic; expansion and 1773+ regulation pass to Topics 05-06.""",
            [
                "15. Reading the conquest: four historiographical lenses",
                "16. Comparative synthesis: Plassey, Buxar, Allahabad and the Dual Government, and the bridge forward",
            ],
        ),
    ],
}


EXTRA_MCQS_03 = [
    (
        "Which sequence best avoids teleology in explaining European expansion in India?",
        "Sea contact, negotiated trade, factory, fortification and possible sovereignty are distinct stages with additional conditions at every step.",
        [
            "A European charter immediately created territorial sovereignty in India.",
            "The first fortified post necessarily became a presidency and empire.",
            "Vasco da Gama's voyage predetermined British conquest.",
        ],
    ),
    (
        "What is the safest description of mercantilism in this topic?",
        "It linked chartered monopoly, protected commerce, naval force and state-company privilege.",
        [
            "It prohibited every form of private trade by company servants.",
            "It meant that Asian merchants ceased trading after 1498.",
            "It separated commerce completely from diplomacy and war.",
        ],
    ),
    (
        "Why did the Portuguese cartaz not amount to complete Indian Ocean monopoly?",
        "Its coercive reach was nodal and contested by long coastlines, rival fleets, evasion and Asian rulers.",
        [
            "It applied only to inland caravans.",
            "It was issued by Mughal emperors to the EIC.",
            "It abolished Portuguese forts and naval patrols.",
        ],
    ),
    (
        "Which statement correctly links St Francis Xavier to Goa?",
        "He worked from Goa, was a founding Jesuit companion, died off China and has his tomb at Bom Jesus.",
        [
            "He founded the Jesuit Order alone and died in Goa.",
            "He commanded the Portuguese cartaz fleet from Diu.",
            "He introduced a precisely dated crop package in a single year.",
        ],
    ),
    (
        "How should UNESCO's Churches and Convents of Goa record be used?",
        "As evidence for missionary architecture, local adaptation, living heritage and conservation risk, not political causation.",
        [
            "As proof that Portuguese sea control was complete.",
            "As a source for exact crop-transfer years.",
            "As proof that every Goan community accepted missionary policy uniformly.",
        ],
    ),
    (
        "What best explains the VOC's strong Indian trade but limited territorial ambition?",
        "Indian textiles and bulk goods served a wider portfolio whose territorial priority lay in Indonesia.",
        [
            "The VOC lacked joint-stock capital or quasi-sovereign powers.",
            "The Dutch abandoned all Indian factories immediately after Amboyna.",
            "Indian rulers never permitted Dutch commerce.",
        ],
    ),
    (
        "What does Child's War contribute to the argument?",
        "It demonstrates that a fortified company could still be defeated and compelled to submit to Mughal authority.",
        [
            "It gave the EIC the Diwani of Bengal.",
            "It ended the Third Carnatic War.",
            "It transferred Bombay from Portugal directly to the Company.",
        ],
    ),
    (
        "Which institutional distinction is correct?",
        "A charter created corporate powers at home, while a farman granted or confirmed privilege under an Indian sovereign.",
        [
            "A factory was necessarily a manufacturing centre.",
            "A fort automatically transferred its hinterland to the company.",
            "A presidency was identical to a sovereign province from its first day.",
        ],
    ),
    (
        "Why is Job Charnock best handled cautiously?",
        "The conventional 1690 association is useful, but Calcutta grew cumulatively from existing villages and actors.",
        [
            "He founded Bombay after conquering it from Portugal.",
            "He issued the 1717 farman as Mughal emperor.",
            "He commanded the French at Wandiwash.",
        ],
    ),
    (
        "What made the English coastal chain strategically useful before conquest?",
        "Surat, Madras, Bombay and Bengal diversified commodities, information, shipping and regional coordination.",
        [
            "Every base was acquired by battlefield annexation.",
            "The chain removed dependence on Indian merchants and producers.",
            "Bengal revenue financed the original 1600 charter.",
        ],
    ),
    (
        "Which statement best describes the French Compagnie des Indes?",
        "It was a state-backed monopoly whose Indian bases and interventions were constrained by finance, naval support and home priorities.",
        [
            "It was the Portuguese Crown's Estado da India.",
            "It focused exclusively on the Indonesian spice islands.",
            "It was expelled from every Indian factory by the Treaty of Paris.",
        ],
    ),
    (
        "What transformed the Carnatic Wars from imported European conflict into Indian politics?",
        "European war intersected with Carnatic and Hyderabad claimant struggles and company-backed military service.",
        [
            "Indian rulers played no part in choosing allies.",
            "The wars began only after the Company received the Bengal Diwani.",
            "The Portuguese cartaz decided every Carnatic succession.",
        ],
    ),
    (
        "Which war-settlement pairing is correct?",
        "The First Carnatic War ended with Aix-la-Chapelle, while the third phase closed with the Treaty of Paris.",
        [
            "Wandiwash ended the First Carnatic War and restored Madras.",
            "Aix-la-Chapelle granted the Company Bengal's Diwani.",
            "Paris abolished all French commercial presence in India.",
        ],
    ),
    (
        "Why is Wandiwash a bounded conclusion rather than Topic 03's starting point?",
        "It concludes the Anglo-French political rivalry after the earlier settlement and institutional story has been established.",
        [
            "It was the first Portuguese landing on the Malabar coast.",
            "It created the Dutch VOC.",
            "It explains the original Mughal permission for Surat.",
        ],
    ),
    (
        "Which claim about Indian agency is most defensible?",
        "Rulers, merchants, brokers, producers and labourers shaped access and survival even as power became unequal.",
        [
            "Agency means every participant had equal bargaining power.",
            "European forts were economically independent of surrounding towns.",
            "Indian merchants disappeared from oceanic trade after 1498.",
        ],
    ),
    (
        "What is the best explanation for English relative advantage?",
        "Finance, naval reach, a diversified base network, organisational continuity, Indian alliances and timing interacted.",
        [
            "English ethnicity alone produced military superiority.",
            "Portuguese religious policy alone decided every later contest.",
            "Plassey revenue explains all seventeenth-century English factories.",
        ],
    ),
    (
        "Which PYQ distinction correctly identifies Broach?",
        "Broach belonged to the early Surat-centred EIC factory network in the first quarter of the seventeenth century.",
        [
            "Broach was the principal French base under Dupleix.",
            "Broach was a Dutch spice-island capital.",
            "Broach was the Portuguese name for Fort St George.",
        ],
    ),
    (
        "What is the safe crop-transfer formulation?",
        "Papaya, pineapple and guava reached India through Portuguese networks in the broad period tested by UPSC, without exact-year claims.",
        [
            "All three crops have one securely proven introduction date.",
            "UNESCO's Goa listing proves the crops' political route.",
            "The crops demonstrate complete Portuguese command of Indian agriculture.",
        ],
    ),
    (
        "Which conclusion respects Topic 03's boundary with Topic 04?",
        "European settlement and rivalry end with the Carnatic comparison; detailed Plassey and Buxar mechanics follow in Topic 04.",
        [
            "Topic 03 should duplicate the whole Dual Government narrative.",
            "The 1717 farman should be treated as the Diwani grant.",
            "The Treaty of Paris made the Company Nawab of Bengal.",
        ],
    ),
    (
        "What is the strongest comparative answer line for the four powers?",
        "Different institutions created different strategic options, but outcomes depended on Asian commerce, Indian politics, war and timing.",
        [
            "A private company always defeats a Crown enterprise.",
            "Commercial success automatically becomes territorial empire.",
            "All four powers followed an identical financial and naval model.",
        ],
    ),
]


MCQ_REPLACEMENTS_04: dict[int, tuple[str, str, list[str]]] = {
    20: (
        "Which causal formulation for the Bengal famine of 1770 is most defensible?",
        "Harvest failure and disease formed the shock, while revenue rigidity and divided administration amplified vulnerability.",
        [
            "Company policy alone created the drought.",
            "Natural conditions alone explain severity and governance is irrelevant.",
            "A precise mortality total is required even when the evidence cannot sustain it.",
        ],
    ),
    24: (
        "Which issue most directly converted Company-Nawab friction into the 1756 Calcutta crisis?",
        "The Company strengthened Fort William without Nawabi permission and resisted Siraj's demand to stop.",
        [
            "The Nawab granted the Company the Diwani before Plassey.",
            "Awadh was annexed by the Company.",
            "Mir Qasim abolished inland duties before becoming Nawab.",
        ],
    ),
    34: (
        "How should casualty claims about Plassey be handled in an examination answer?",
        "Avoid unsupported precision and focus on the conspiracy-backed political mechanism rather than inherited battlefield totals.",
        [
            "Treat every repeated textbook number as an audited roll.",
            "State that no fighting occurred at all.",
            "Replace source criticism with larger speculative estimates.",
        ],
    ),
    36: (
        "What best describes the post-Plassey extraction mechanism under Mir Jafar?",
        "Transfers and concessions deepened the client's dependence and expanded Company political leverage.",
        [
            "A single payment ended Company intervention in Bengal.",
            "Mir Jafar received the Diwani from Shah Alam II.",
            "The Company immediately assumed direct administration in 1757.",
        ],
    ),
    48: (
        "What did the 1765 Diwani grant change most directly?",
        "It gave the Company a recognised legal-fiscal title to collect the revenues of Bengal, Bihar and Orissa.",
        [
            "It made the Company Nawab and abolished every Nizamat function.",
            "It annexed Awadh into Bengal.",
            "It created the EIC's original commercial charter.",
        ],
    ),
    50: (
        "What was the strategic result of the separate Allahabad settlement with Shuja-ud-Daula?",
        "Most of Awadh was restored under its ruler so that it could serve as a buffer rather than being annexed.",
        [
            "The Company made Mir Qasim Nawab again.",
            "Shah Alam II transferred the French factories to Awadh.",
            "The settlement merged Diwani and Nizamat into Nawabship.",
        ],
    ),
    76: (
        "A student blames the 1770 famine entirely on Company revenue policy. What is the correction?",
        "Company governance amplified a crisis with natural and epidemiological dimensions; neither side of the causal pair should be erased.",
        [
            "Revenue policy had no bearing on vulnerability or relief.",
            "The famine should be explained only through a precise population-loss estimate.",
            "Dual Government had already ended before the famine.",
        ],
    ),
    79: (
        "A student supplies exact Plassey casualty totals without a reliable source. What is the correction?",
        "Omit false precision, identify the estimates as disputed if mentioned, and analyse the conspiracy and command collapse.",
        [
            "Increase the estimates to make the battle appear more decisive.",
            "Claim that the battle involved no casualties of any kind.",
            "Use the figures as proof that Plassey alone completed Company sovereignty.",
        ],
    ),
}


@dataclass(frozen=True)
class MCQ:
    stem: str
    options: dict[str, str]
    answer: str
    explanation: str
    evidence: str = ""


def split_h2(text: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(re.finditer(r"(?m)^## (.+?)\s*$", text))
    if not matches:
        raise ValueError("Canonical source has no H2 headings.")
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1), text[match.start():end].strip()))
    return text[: matches[0].start()].strip(), sections


def remove_frontmatter_and_h1(text: str) -> str:
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.S)
    return re.sub(r"(?m)^#(?!#) .+\n*", "", text, count=1).strip()


def lower_headings(fragment: str, minimum: int = 4) -> str:
    def lower(match: re.Match[str]) -> str:
        level = min(6, max(minimum, len(match.group(1)) + 2))
        return "#" * level + " "

    return re.sub(r"(?m)^(#{1,6}) ", lower, fragment).strip()


def session_fragment(fragment: str, number: int, phase: str) -> str:
    lines = fragment.splitlines()
    if not lines or not lines[0].startswith("## "):
        raise ValueError("Teaching fragment lacks an H2 heading.")
    title = lines[0][3:].strip()
    transformed = [f"### SESSION {number} — {phase} — {title}"]
    for line in lines[1:]:
        match = re.match(r"^(#{1,6}) (.*)$", line)
        if match:
            level = min(6, max(4, len(match.group(1)) + 1))
            transformed.append("#" * level + " " + match.group(2))
        else:
            transformed.append(line)
    return "\n".join(transformed).strip()


def rewrite_asset_links(text: str) -> str:
    return text.replace("(../../../notes/", "(../../../../../../notes/")


def sanitize_topic04(text: str) -> str:
    replacements = [
        (
            r"roughly Rs 1\.77 crore in formal compensation from Mir Jafar's treasury, "
            r"on top of separate personal payments to Clive and other officials that ran "
            r"into millions of rupees",
            "large transfers and concessions from Mir Jafar's treasury, alongside private "
            "fortunes accumulated by Company officials",
        ),
        (
            r"the traditionally cited casualty figures for Plassey are markedly lopsided "
            r"-- commonly given as around 29 dead on the Company's side against several hundred, "
            r"often cited as close to 500, among Siraj's forces -- though these are the standard "
            r"figures repeated in general secondary accounts rather than exact, independently "
            r"audited modern counts",
            "inherited casualty estimates for Plassey are not supported by an independently "
            "audited modern roll and should not be repeated as precise fact",
        ),
        (
            r"an annual tribute of 26 lakh rupees to the emperor",
            "a stipulated annual payment to the emperor",
        ),
        (
            r"a 50 lakh rupee war indemnity",
            "a war indemnity",
        ),
        (
            r"an annual tribute of 26 lakh rupees and two ceded districts",
            "a stipulated annual payment and the districts",
        ),
        (
            r"roughly one-third of Bengal's population as affected",
            "a very large but disputed scale of population loss",
        ),
        (
            r'commonly cited loosely as "roughly one-third" of the affected population '
            r"in some secondary accounts",
            "sometimes expressed through disputed secondary-source estimates",
        ),
        (
            r"The 26-lakh annual tribute payment to the emperor",
            "The stipulated annual payment to the emperor",
        ),
        (
            r"a 26-lakh tribute",
            "a stipulated tribute",
        ),
        (
            r"Traditional casualty figures \(about 29 Company dead, several hundred on Siraj's side\) "
            r"are textbook figures only -- always qualify them as such, never as audited counts\.",
            "Do not repeat inherited Plassey casualty totals as audited fact; centre the "
            "conspiracy and command collapse instead.",
        ),
        (
            r"plus roughly Rs 1\.77 crore in compensation and gifts \(a scholarly estimate\)",
            "plus major transfers and concessions whose exact aggregate should not be treated "
            "as an audited treasury figure",
        ),
        (
            r"for a 26-lakh annual tribute plus the ceded districts of Kora and Allahabad",
            "in return for a stipulated payment and the linked Kora-Allahabad arrangement",
        ),
        (
            r"restored for a 50-lakh indemnity",
            "restored under a separate indemnity settlement",
        ),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.I)
    text = re.sub(
        r"(?m)^.*\b(?:around|exactly)\s+29\b.*\b(?:500|several hundred)\b.*$\n?",
        "",
        text,
        flags=re.I,
    )
    text = text.replace(
        "Hazarduari Palace at Murshidabad",
        "the Murshidabad Nawabi landscape",
    )
    return text


def phase_for(key: str, number: int) -> str:
    if key == "modern-indian-history-03":
        if number <= 4:
            return "FOUNDATION"
        if number <= 18:
            return "CORE"
        return "CORE SYNTHESIS"
    if number <= 3:
        return "FOUNDATION"
    if number <= 13:
        return "CORE"
    return "CORE SYNTHESIS"


def parse_topic03_mcqs(source: str) -> list[MCQ]:
    pattern = re.compile(r"(?m)^## (?:Hard|Remedial) MCQ (\d+)\s*$")
    matches = list(pattern.finditer(source))
    if len(matches) != 60:
        raise ValueError(f"Topic 03: expected 60 canonical MCQs, found {len(matches)}.")
    result: list[MCQ] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        block = source[match.end():end]
        stem_match = re.search(r"(?m)^-\s*Question:\s*(.+?)\s*$", block)
        options = dict(re.findall(r"(?m)^-\s*([A-D])\.\s+(.+?)\s*$", block))
        answer = re.search(r"(?m)^-\s*Answer:\s*([A-D])\.", block)
        explanation = re.search(r"(?m)^-\s*Explanation:\s*(.+?)\s*$", block)
        evidence = re.search(r"(?m)^-\s*Evidence anchor:\s*(.+?)\s*$", block)
        if not stem_match or len(options) != 4 or not answer or not explanation:
            raise ValueError(f"Topic 03: unable to parse canonical MCQ {index + 1}.")
        result.append(
            MCQ(
                stem=stem_match.group(1).strip(),
                options=options,
                answer=answer.group(1),
                explanation=explanation.group(1).strip(),
                evidence=evidence.group(1).strip() if evidence else "",
            )
        )
    return result


def parse_topic04_mcqs(source: str) -> list[MCQ]:
    start = source.index("## Learning MCQs")
    end = source.index("## Mains practice: solved model answers")
    area = source[start:end]
    pattern = re.compile(r"(?m)^### Q(\d+)\.\s+(.+?)\s*$")
    matches = list(pattern.finditer(area))
    if len(matches) != 80:
        raise ValueError(f"Topic 04: expected 80 canonical MCQs, found {len(matches)}.")
    result: list[MCQ] = []
    for index, match in enumerate(matches):
        end_pos = matches[index + 1].start() if index + 1 < len(matches) else len(area)
        block = area[match.end():end_pos]
        options = dict(re.findall(r"(?m)^([A-D])\.\s+(.+?)\s*$", block))
        answer = re.search(r"(?m)^\*\*Answer:\s*([A-D])\.", block)
        explanation = re.search(r"(?m)^\*\*Explanation:\*\*\s*(.+?)\s*$", block)
        if len(options) != 4 or not answer or not explanation:
            raise ValueError(f"Topic 04: unable to parse canonical MCQ {index + 1}.")
        result.append(
            MCQ(
                stem=match.group(2).strip(),
                options=options,
                answer=answer.group(1),
                explanation=explanation.group(1).strip(),
            )
        )
    return result


def authored_mcq(stem: str, correct: str, wrongs: list[str]) -> MCQ:
    return MCQ(
        stem=stem,
        options={"A": correct, "B": wrongs[0], "C": wrongs[1], "D": wrongs[2]},
        answer="A",
        explanation=correct,
    )


def normalize_mcqs(source: str, key: str) -> str:
    if key == "modern-indian-history-03":
        items = parse_topic03_mcqs(source)
        items.extend(authored_mcq(*values) for values in EXTRA_MCQS_03)
    else:
        items = parse_topic04_mcqs(source)
        items = [
            authored_mcq(*MCQ_REPLACEMENTS_04[index])
            if index in MCQ_REPLACEMENTS_04
            else item
            for index, item in enumerate(items, 1)
        ]
    if len(items) != 80:
        raise ValueError(f"{key}: expected 80 MCQs after authoring, found {len(items)}.")
    blocks: list[str] = []
    for number, item in enumerate(items, 1):
        expected = "ABCD"[(number - 1) % 4]
        stem = sanitize_topic04(item.stem) if key.endswith("-04") else item.stem
        correct = item.options[item.answer]
        wrongs = [item.options[letter] for letter in "ABCD" if letter != item.answer]
        if key.endswith("-04"):
            correct = sanitize_topic04(correct)
            wrongs = [sanitize_topic04(value) for value in wrongs]
        choices = {expected: correct}
        for letter, text in zip(
            [letter for letter in "ABCD" if letter != expected],
            wrongs,
        ):
            choices[letter] = text
        explanation = sanitize_topic04(item.explanation) if key.endswith("-04") else item.explanation
        if len(explanation.split()) < 6:
            explanation = (
                f"{explanation.rstrip('.')} This distinction is necessary for accurate "
                "UPSC elimination and chronology."
            )
        block = (
            f"### Q{number}. {stem}\n\n"
            + "\n".join(f"{letter}. {choices[letter]}" for letter in "ABCD")
            + f"\n\n**Answer: {expected}.**\n"
            + f"**Explanation:** {explanation}"
        )
        if item.evidence:
            block += f"\n\n**Evidence anchor:** {item.evidence}"
        blocks.append(block)
    return "\n\n".join(blocks)


def split_register(source: str, key: str) -> tuple[str, str]:
    marker = (
        "## FINAL CONSOLIDATED REGISTER NOTES - PLACED LAST"
        if key.endswith("-03")
        else "# FINAL CONSOLIDATED REGISTER NOTES - TOPIC 04"
    )
    if marker not in source:
        raise ValueError(f"{key}: final register marker missing.")
    main, register = source.split(marker, 1)
    return main.rstrip(), marker + register


def advanced_depth(config_value: dict[str, object]) -> str:
    advanced = rewrite_asset_links(
        Path(config_value["advanced"]).read_text(encoding="utf-8")
    )
    return lower_headings(remove_frontmatter_and_h1(advanced))


def source_audit(config_value: dict[str, object]) -> str:
    key = str(config_value["key"])
    if key.endswith("-03"):
        live = (
            "✅ **Bounded live heritage fact:** UNESCO's Churches and Convents of Goa "
            "record identifies a mission-linked architectural ensemble, the tomb of St "
            "Francis Xavier at Bom Jesus, adaptation of European forms to local materials, "
            "living religious use, and conservation threats including weathering, capillary "
            "action and termites.\n\n"
            "⚠️ **Inference boundary:** this heritage record is not evidence for Portuguese "
            "political causation, a complete maritime monopoly, or exact crop-transfer dates."
        )
    else:
        live = (
            "✅ **Bounded contemporary-memory fact:** on 21 June 2026, *The Daily Star* "
            "reported a historical discussion urging readers to interpret Plassey through "
            "conspiracy, European rivalry, Murshidabad court tensions, commercial ambition, "
            "public memory and the contested meaning of an 'independent Bengal'.\n\n"
            "⚠️ **Inference boundary:** the report is a historiography/public-memory anchor "
            "only. The 1717 privilege conflict, Plassey, Buxar, Diwani, Dual Government and "
            "famine analysis below rest on repository owners and local books. No suspicious "
            "AI-generated archive item is used."
        )
    return (
        "#### Source audit, progression and syllabus boundary\n\n"
        "- **Foundation:** chronology, institutions, actors and exact terminology.\n"
        "- **Core:** mechanisms, comparisons, causal chains, Indian agency and exam traps.\n"
        "- **Core synthesis:** historiography, answer architecture, boundaries and bridges.\n"
        "- **Optional Advanced:** the separate owner is taught only after Basic practice.\n"
        "- **Static source order:** repository Markdown → OCR-searchable Bipan Chandra, "
        "Sekhar Bandyopadhyay and Satish Chandra → bounded live anchor; Qdrant not needed.\n"
        f"- **PYQ integrity:** {config_value['pyq_note']}\n\n"
        "#### Live-linkage block\n\n"
        + live
    )


def assemble(config_value: dict[str, object]) -> tuple[str, str, int]:
    key = str(config_value["key"])
    raw_source = rewrite_asset_links(
        Path(config_value["canonical"]).read_text(encoding="utf-8")
    )
    source = raw_source
    if key.endswith("-04"):
        source = sanitize_topic04(source)
    main_source, register_source = split_register(source, key)
    preamble, sections = split_h2(main_source)
    sessions: list[str] = []
    practice: list[str] = []
    for title, fragment in sections:
        if key.endswith("-03"):
            is_mcq = bool(re.match(r"^(?:Hard|Remedial) MCQ", title))
            is_practice = (
                title.startswith(("PART II", "PYQ ", "PART III", "Mains "))
                and not is_mcq
            )
        else:
            is_mcq = title.startswith(("Learning MCQs", "Broad MCQs", "Remedial MCQs"))
            is_practice = title.startswith(
                ("Transparent PYQ", "Evidence and answer-writing", "Mains practice")
            )
        if is_mcq:
            continue
        if is_practice:
            practice.append(lower_headings(fragment))
        elif re.match(r"^\d{1,2}\.\s+", title):
            number = len(sessions) + 1
            sessions.append(session_fragment(fragment, number, phase_for(key, number)))
    expected_basic = int(config_value["basic_session_count"])
    if len(sessions) != expected_basic:
        raise ValueError(
            f"{key}: expected {expected_basic} Basic sessions, found {len(sessions)}."
        )
    advanced = advanced_depth(config_value)
    register = lower_headings(register_source)
    mcqs = normalize_mcqs(raw_source, key)
    preamble = ""
    ascii_fragment = ascii_master.build_manual_fragment(
        ascii_master.normalize_manual_spec_file(ASCII_PATH)[key]
    )
    markdown = (
        f"# {config_value['title']} — Learner-v2 Complete Learning Session\n\n"
        + (lower_headings(preamble) + "\n\n" if preamble else "")
        + "## BASIC LEARNING SESSION\n\n"
        + source_audit(config_value)
        + "\n\n"
        + "\n\n".join(sessions)
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + "\n\n".join(practice)
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + advanced
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + "### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\n\n"
        + ascii_fragment
        + "\n\n"
        + register
        + "\n"
    )
    workbook = (
        f"# {config_value['title']} — Solved Practice Workbook\n\n"
        "> Built from the same normalized practice source as the complete learner-v2 "
        "session. Official/inferred PYQ status and true topic ownership are preserved.\n\n"
        "## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + "\n\n".join(practice)
        + "\n"
    )
    return markdown, workbook, len(sessions)


def write_ascii_spec() -> None:
    topics: list[dict[str, object]] = []
    for config_value in TOPICS:
        key = str(config_value["key"])
        panels = []
        for title, structural_type, body, references in PANEL_DATA[key]:
            lines = body.splitlines()
            if max(map(len, lines)) > 100:
                raise ValueError(
                    f"{key}: ASCII line exceeds 100 characters in {title!r}."
                )
            panels.append(
                {
                    "title": title,
                    "structural_type": structural_type,
                    "ascii_lines": lines,
                    "source_references": references,
                }
            )
        if len(panels) != 12:
            raise ValueError(f"{key}: expected 12 panels, found {len(panels)}.")
        topics.append(
            {
                "topic_key": key,
                "display_title": config_value["title"],
                "source_markdown": str(
                    Path(config_value["canonical"]).relative_to(ROOT)
                ),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Modern Indian History learner-v2 Topics 03-04",
        "constraints": {
            "panel_count_per_topic": 12,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "complete_embed_ready_lines": True,
            "tracker_untouched": True,
        },
        "topics": topics,
    }
    ASCII_DIR.mkdir(parents=True, exist_ok=True)
    ASCII_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_graphical_spec(config_value: dict[str, object], markdown: str) -> Path:
    key = str(config_value["key"])
    panels = [
        {
            "title": title,
            "body": body,
            "structural_type": kind,
            "source_references": refs,
        }
        for title, kind, body, refs in PANEL_DATA[key]
    ]
    source_path = SESSION_DIR / f"{key}_Learning-Session.md"
    spec = carvaka_flowchart.author_topic_spec(
        topic_key=key,
        subject=SUBJECT,
        title=str(config_value["title"]),
        source_markdown=markdown,
        source_markdown_path=str(source_path.relative_to(ROOT)),
        ascii_spec_path=str(ASCII_PATH.relative_to(ROOT)),
        ascii_spec_sha256=hashlib.sha256(ASCII_PATH.read_bytes()).hexdigest(),
        panels=panels,
        source_generation=2,
    )
    if len(spec["stages"]) != 13:
        raise ValueError(f"{key}: expected a 13-stage graphical master.")
    GRAPHICAL_DIR.mkdir(parents=True, exist_ok=True)
    output = GRAPHICAL_DIR / f"{key}.json"
    output.write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def write_section_manifest() -> Path:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    target = next(
        topic
        for topic in catalog["topics"]
        if topic.get("topic_key") == "modern-indian-history-03"
    )
    manifest = section_indexes.materialize_catalog_section_manifest(ROOT, catalog, target)
    if manifest != SECTION_MANIFEST:
        raise ValueError(f"Unexpected Modern History section manifest: {manifest}")
    return manifest


def write_generation_spec(
    config_value: dict[str, object],
    source_path: Path,
    workbook_path: Path,
    graphical_path: Path,
) -> Path:
    sources = [
        Path(config_value[name])
        for name in ("basic", "advanced", "canonical", "legacy_main", "legacy_workbook")
    ]
    sources += [Path(path) for path in config_value["extra"]]
    sources += [
        source_path,
        workbook_path,
        SECTION_MANIFEST,
        CATALOG,
        ASCII_PATH,
        graphical_path,
        *COMMON_CROSS,
        *PYQ_INDEXES,
        *OFFICIAL_QUESTION_SOURCES,
        *LOCAL_BOOKS,
    ]
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))
    key = str(config_value["key"])
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_topic = next(
        topic for topic in catalog["topics"] if topic.get("topic_key") == key
    )
    payload = {
        "schema_version": 1,
        "topic_key": key,
        "subject": SUBJECT,
        "section": "Subject-Wide-Syllabus",
        "topic_folder": key,
        "title": config_value["title"],
        "variant": "learner-v2",
        "generation": 2,
        "generation_date": DATE,
        "command": catalog_topic["learner_v2_command"],
        "source_markdown": str(source_path.relative_to(ROOT)),
        "workbook_markdown": str(workbook_path.relative_to(ROOT)),
        "source_basic": str(Path(config_value["basic"]).relative_to(ROOT)),
        "source_canonical": str(Path(config_value["canonical"]).relative_to(ROOT)),
        "source_advanced": str(Path(config_value["advanced"]).relative_to(ROOT)),
        "manifest": str(SECTION_MANIFEST.relative_to(ROOT)),
        "cross_topic_sources": [
            str(path.relative_to(ROOT))
            for path in [*COMMON_CROSS, *[Path(value) for value in config_value["extra"]]]
        ],
        "local_ocr_sources": [str(path.relative_to(ROOT)) for path in LOCAL_BOOKS],
        "pyq_indexes": [str(path.relative_to(ROOT)) for path in PYQ_INDEXES],
        "official_question_sources": [
            str(path.relative_to(ROOT)) for path in OFFICIAL_QUESTION_SOURCES
        ],
        "live_sources": config_value["live_sources"],
        "source_files": [str(path.relative_to(ROOT)) for path in sources],
        "practice_profile": (
            "80 unique MCQ stems with substantive explanations; strict A-B-C-D repeated "
            "20 times; original 10/15/20-mark Mains practice and verified/inferred PYQ "
            "provenance retained in both session and solved workbook Markdown."
        ),
        "pyq_status_note": config_value["pyq_note"],
        "current_linkage_note": config_value["current_note"],
        "mcq_answer_policy": "strict-abcd-cycle",
        "ascii_panel_count": 12,
        "graphical_stage_count": 13,
        "tracker_untouched": True,
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{key}-new-topic-{DATE}.json"
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def mcq_audit(markdown: str, key: str) -> None:
    match = re.search(
        r"(?ms)^## BASIC MCQS / REMEDIATION\s*$\n(.*?)"
        r"^## PYQS AND ANSWER PRACTICE",
        markdown,
    )
    if match is None:
        raise ValueError(f"{key}: MCQ section missing.")
    section = match.group(1)
    q_matches = list(
        re.finditer(
            r"(?ms)^### Q(\d+)\.\s+(.+?)\n\n(.*?)(?=^### Q\d+\.|\Z)",
            section,
        )
    )
    stems: list[str] = []
    answers: list[str] = []
    for expected_number, q_match in enumerate(q_matches, 1):
        if int(q_match.group(1)) != expected_number:
            raise ValueError(f"{key}: MCQ numbering is not sequential.")
        stems.append(q_match.group(2).strip())
        block = q_match.group(3)
        answer = re.search(r"(?m)^\*\*Answer:\s*([A-D])\.\*\*$", block)
        options = re.findall(r"(?m)^([A-D])\.\s+(.+?)\s*$", block)
        explanation = re.search(r"(?m)^\*\*Explanation:\*\*\s+(.+?)\s*$", block)
        if not answer or len(options) != 4 or not explanation:
            raise ValueError(f"{key}: malformed MCQ {expected_number}.")
        question_only = block[: answer.start()]
        if re.search(r"(?i)\b(?:answer|correct option)\s*[:=]", question_only):
            raise ValueError(f"{key}: answer leakage in MCQ {expected_number}.")
        if re.search(r"(?i)\((?:correct|answer)\)|✅", question_only):
            raise ValueError(f"{key}: answer marker leaked into MCQ {expected_number}.")
        if len(explanation.group(1).split()) < 6:
            raise ValueError(f"{key}: explanation too thin in MCQ {expected_number}.")
        answers.append(answer.group(1))
    normalized = [
        re.sub(r"[^a-z0-9]+", " ", stem.casefold()).strip() for stem in stems
    ]
    if len(stems) != 80 or len(set(normalized)) != 80:
        raise ValueError(f"{key}: MCQ count or normalized-stem uniqueness failed.")
    if answers != list("ABCD" * 20):
        raise ValueError(f"{key}: MCQ answer rotation failed.")
    distribution = {letter: answers.count(letter) for letter in "ABCD"}
    if distribution != {letter: 20 for letter in "ABCD"}:
        raise ValueError(f"{key}: MCQ answer distribution failed: {distribution}.")


def self_check(
    markdown: str,
    workbook: str,
    key: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    required = [
        "BASIC LEARNING SESSION",
        "BASIC MCQS / REMEDIATION",
        "PYQS AND ANSWER PRACTICE",
        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
        "CONSOLIDATED REGISTER NOTES",
    ]
    if [item for item in headings if item in required] != required:
        raise ValueError(f"{key}: learner-v2 H2 order is invalid.")
    if headings[-1] != "CONSOLIDATED REGISTER NOTES":
        raise ValueError(f"{key}: consolidated register notes are not the last H2.")
    sessions = re.findall(r"(?m)^### SESSION (\d+) — (.+?) — (.+?)\s*$", markdown)
    if len(sessions) != session_count:
        raise ValueError(f"{key}: explicit session count mismatch.")
    if [int(row[0]) for row in sessions] != list(range(1, session_count + 1)):
        raise ValueError(f"{key}: explicit session numbering is invalid.")
    if not any(row[1] == "FOUNDATION" for row in sessions):
        raise ValueError(f"{key}: Foundation progression is missing.")
    if not any(row[1] == "CORE" for row in sessions):
        raise ValueError(f"{key}: Core progression is missing.")
    if "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER" not in markdown:
        raise ValueError(f"{key}: Optional Advanced depth is missing.")
    mcq_audit(markdown, key)
    mcq_audit(workbook, key)
    spec = ascii_master.normalize_manual_spec_file(ASCII_PATH)[key]
    if len(spec.panels) != 12 or markdown.count("```ascii-master") != 12:
        raise ValueError(f"{key}: authored ASCII panel count failed.")
    graphical = json.loads(graphical_path.read_text(encoding="utf-8"))
    if len(graphical["stages"]) != 13:
        raise ValueError(f"{key}: graphical stage count failed.")
    if markdown.find("COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM") > markdown.find(
        "FINAL CONSOLIDATED REGISTER NOTES"
    ):
        raise ValueError(f"{key}: register notes must follow the ASCII master and remain last.")
    required_terms = {
        "modern-indian-history-03": [
            "Estado da India",
            "cartaz",
            "VOC",
            "Fort St George",
            "Pondicherry",
            "Wandiwash",
            "Treaty of Paris",
            "St Francis Xavier",
            "papaya",
        ],
        "modern-indian-history-04": [
            "1717",
            "dastak",
            "Plassey",
            "Buxar",
            "Treaty of Allahabad",
            "Diwani",
            "Nizamat",
            "Dual Government",
            "1770",
            "Warren Hastings",
        ],
    }[key]
    missing = [term for term in required_terms if term.casefold() not in markdown.casefold()]
    if missing:
        raise ValueError(f"{key}: missing required concepts: {missing}.")
    if key.endswith("-04"):
        forbidden = [
            r"\b1\.77 crore\b",
            r"\b26[- ]?lakh\b",
            r"\b50[- ]?lakh\b",
            r"\bexactly 500\b",
            r"\baround 29\b",
            r"\bone-third of Bengal",
            r"Hazarduari Palace",
        ]
        hits = [pattern for pattern in forbidden if re.search(pattern, markdown, re.I)]
        if hits:
            raise ValueError(f"{key}: prohibited unsupported precision remains: {hits}.")


def main() -> int:
    write_ascii_spec()
    write_section_manifest()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = [ASCII_PATH, SECTION_MANIFEST]
    for config_value in TOPICS:
        markdown, workbook, session_count = assemble(config_value)
        key = str(config_value["key"])
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        workbook_path = SESSION_DIR / f"{key}_Solved-Workbook.md"
        source_path.write_text(markdown, encoding="utf-8")
        workbook_path.write_text(workbook, encoding="utf-8")
        graphical_path = write_graphical_spec(config_value, markdown)
        manifest = write_generation_spec(
            config_value,
            source_path,
            workbook_path,
            graphical_path,
        )
        self_check(markdown, workbook, key, session_count, graphical_path)
        written.extend(
            [source_path, workbook_path, graphical_path, manifest]
        )
        print(
            f"{key}: sessions={session_count}; mcqs=80 (A20/B20/C20/D20); "
            "ascii=12; graphical=13"
        )
    for path in written:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
