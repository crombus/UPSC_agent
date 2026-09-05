"""Assemble Modern Indian History learner-v2 Topics 05-06 and visual specs.

This authoring-only generator writes Markdown and JSON specifications. It does
not render PDFs, stage files, finalise tracker records, or modify approval state.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_modern_history_03_04_sequential as base
import notions_style_ascii_master as ascii_master


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Modern-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "modern-indian-history-05-06-2026-08-30-sequential.json"
)
GRAPHICAL_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / SUBJECT
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "modern-indian-history--subject-wide-syllabus.json"
)


def topic_config(
    number: int,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    legacy_main: str,
    legacy_workbook: str,
    extra: list[Path],
    live_sources: list[str],
    current_note: str,
    session_count: int,
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
        "extra": extra,
        "live_sources": live_sources,
        "current_note": current_note,
        "basic_session_count": session_count,
        "pyq_note": pyq_note,
    }


TOPICS = [
    topic_config(
        5,
        "British Territorial Expansion (Mysore, Marathas, Sikhs; Subsidiary Alliance & Lapse)",
        "05_British-Territorial-Expansion-Mysore-Marathas-Sikhs-Subsidiary-Alliance-Lapse_Complete-Topic-Package.md",
        "05_British-Territorial-Expansion.md",
        "05_British-Territorial-Expansion.md",
        "05_British-Territorial-Expansion-Mysore-Marathas-Sikhs-Subsidiary-Alliance-Lapse_Complete-Learning-Session_2026-08-19.pdf",
        "05_British-Territorial-Expansion-Mysore-Marathas-Sikhs-Subsidiary-Alliance-Lapse_Premium-Solved-PYQ-Workbook_2026-08-19.pdf",
        [
            KNOWLEDGE / "basic" / "02_Indian-States-and-Society-18th-Century.md",
            KNOWLEDGE / "basic" / "04_British-Conquest-of-Bengal.md",
            KNOWLEDGE
            / "basic"
            / "06_Government-Structure-and-Constitutional-Development-1757-1858.md",
            KNOWLEDGE / "basic" / "11_The-Revolt-of-1857.md",
        ],
        [
            "https://asi.nic.in/HQ/tenders/?p=12",
            "https://asi.nic.in/admin/jobsvacancie/download/42",
        ],
        "ASI's 2025-26 Srirangapatna sub-circle maintenance tender and Bangalore "
        "Circle museum-building expression of interest establish an official, current "
        "heritage-management link for Tipu-era sites. They are used only for heritage "
        "continuity, not as evidence for eighteenth-century military causation.",
        26,
        "The verified 2018 Prelims Subsidiary Alliance demand is retained with its "
        "locally unavailable official key clearly labelled. The verified 2022 GS-I "
        "Company-armies question is this topic's direct Mains owner and is solved in full.",
    ),
    topic_config(
        6,
        "Structure of Government & Constitutional Development, 1757-1858",
        "06_Structure-of-Government-and-Constitutional-Development-1757-1858_Complete-Topic-Package.md",
        "06_Government-Structure-and-Constitutional-Development-1757-1858.md",
        "06_Government-Structure-and-Constitutional-Development-1757-1858.md",
        "06_Structure-of-Government-and-Constitutional-Development-1757-1858_Complete-Learning-Session_2026-08-19.pdf",
        "06_Structure-of-Government-and-Constitutional-Development-1757-1858_Premium-Solved-PYQ-Workbook_2026-08-19.pdf",
        [
            KNOWLEDGE / "basic" / "04_British-Conquest-of-Bengal.md",
            KNOWLEDGE / "basic" / "05_British-Territorial-Expansion.md",
            KNOWLEDGE / "basic" / "08_Administrative-Organisation.md",
            KNOWLEDGE / "basic" / "12_Administrative-Changes-After-1858.md",
            ROOT
            / "knowledge-export"
            / "Indian Polity"
            / "Indian Polity by M Laxmikant.md",
        ],
        ["https://pib.gov.in/PressReleasePage.aspx?PRID=2194656"],
        "PIB's Constitution Day 2025 account is used as a bounded constitutional-heritage "
        "anchor for public engagement with constitutional values. It does not project "
        "democratic intent onto the Company-era acts, which created imperial control "
        "without Indian representation.",
        16,
        "The verified 2019 and 2023 Prelims demands on the Charter Act of 1813 and "
        "the Governor-General designation are retained. Their official local keys are "
        "unavailable, so the package teaches elimination logic without fabricating a key.",
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-05": [
        (
            "Expansion was a ladder, not one method",
            "strategy-map",
            """RING-FENCE -> friendly buffer protects Company territory
SUBSIDIARY ALLIANCE -> ruler survives but loses army, diplomacy and fiscal autonomy
PARAMOUNTCY -> Company claims a superior right to arbitrate Indian-state conduct
ANNEXATION -> conquest, lapse or alleged misgovernment brings direct administration.""",
            [
                "1. From commercial-fiscal base to military-fiscal state: ring-fence, buffer, subsidiary dependency, paramountcy, annexation",
                "26. Comparative synthesis: Mysore vs Maratha vs Sikh; war vs alliance vs lapse vs misgovernance",
            ],
        ),
        (
            "The Company fiscal-military flywheel",
            "causal-cycle",
            """BENGAL DIWANI -> predictable revenue and credit
REVENUE -> salaried sepoys + officers + artillery + supply
ARMY + INDIAN ALLIES -> serial victory against isolated opponents
VICTORY -> indemnity / ceded territory -> more revenue -> a larger military machine.""",
            [
                "3. Why Company armies prevailed I: Bengal revenue, the sepoy army, officers, artillery and logistics",
                "4. Why Company armies prevailed II: credit and supply, maritime reinforcement, diplomacy, serial isolation, Indian allies and recruits -- and the Company's own reverses",
            ],
        ),
        (
            "Mysore resistance and four-war sequence",
            "timeline",
            """1767-69 FIRST -> Treaty of Madras; Haidar forces a negotiated peace
1780-84 SECOND -> Haidar dies 1782; Treaty of Mangalore restores conquests
1790-92 THIRD -> anti-Tipu coalition; Treaty of Seringapatam cuts Mysore
1799 FOURTH -> Tipu dies; Wodeyars restored under subsidiary dependence.""",
            [
                "5. Mysore's state capacity: Haidar Ali's rise, army reform and Tipu's \"military fiscalism\"",
                "6. Four Anglo-Mysore Wars: alliances, treaties, Madras/Mangalore/Seringapatam",
                "8. The 1799 settlement: Seringapatam, Wodeyar restoration, subsidiary control, and why resistance failed",
            ],
        ),
        (
            "Tipu: reform, diplomacy and bounded interpretation",
            "evidence-map",
            """STATE CAPACITY -> direct revenue, army reform, state commerce and strategic ports
DIPLOMACY -> Ottoman, Afghan and French contacts sought counterweights to Company power
LIMIT -> outreach did not create a dependable anti-British coalition
SAFE VERDICT -> real reform and resistance, neither caricature nor modern nation-state myth.""",
            [
                "5. Mysore's state capacity: Haidar Ali's rise, army reform and Tipu's \"military fiscalism\"",
                "7. Malabar, Travancore and Tipu's diplomacy: the French connection without myth",
            ],
        ),
        (
            "Maratha confederacy and the cohesion problem",
            "hierarchy",
            """PESHWA at Pune -> nominal confederate centre
SCINDIA | HOLKAR | BHONSLE | GAEKWAD -> regional houses with separate interests
STRENGTH -> reach, cavalry, revenue claims and experienced commanders
WEAKNESS -> no durable common command; Company bargains and fights one house at a time.""",
            [
                "9. The Maratha confederacy: structure, five houses, and the cost of a headless polity",
            ],
        ),
        (
            "Three Anglo-Maratha Wars",
            "timeline",
            """1775-82 FIRST -> Raghunath Rao crisis -> Wadgaon reverse -> Treaty of Salbai
1802 BASSEIN -> Peshwa accepts subsidiary terms after Holkar's victory
1803-05 SECOND -> Scindia and Bhonsle defeated; Holkar resists and settlement follows
1817-18 THIRD -> Peshwaship abolished; Baji Rao II pensioned at Bithur.""",
            [
                "10. First Anglo-Maratha War: Raghunath Rao, Surat, Purandar, Wadgaon, Salbai",
                "11. Treaty of Bassein, 1802: the turning point",
                "12. Second Anglo-Maratha War: Assaye, Delhi, Laswari, and Holkar's resistance",
                "13. Third Anglo-Maratha War: Pindaris, 1817-18, Baji Rao II, and the end of the Peshwaship",
            ],
        ),
        (
            "Subsidiary Alliance dismantled sovereignty",
            "mechanism-map",
            """BRITISH FORCE STATIONED -> ruler pays cash or cedes revenue territory
RESIDENT AT COURT -> continuous political leverage
NO INDEPENDENT WAR / DIPLOMACY / EUROPEAN EMPLOYMENT -> external sovereignty removed
RESULT -> protection without capacity; ruler bears blame for a state Britain constrains.""",
            [
                "14. Precedents and Wellesley's systematisation: the exact core clauses",
                "16. Sovereignty eroded: dependency, the Resident, and the responsibility paradox",
            ],
        ),
        (
            "Alliance case sequence and consequences",
            "timeline",
            """HYDERABAD 1798/1800 -> French-trained force removed; dependence deepens
MYSORE 1799 -> restored Wodeyar state enters subsidiary control
AWADH 1801 -> territorial cession substitutes for enlarged subsidy
BASSEIN 1802 -> Peshwa's acceptance transforms a Maratha civil conflict into Company war.""",
            [
                "15. The case sequence: Hyderabad 1798, Mysore 1799, Awadh 1801, Bassein 1802 and after",
            ],
        ),
        (
            "Sindh and the northwest strategic corridor",
            "frontier-map",
            """INDUS COMMERCE + AFGHAN FRONTIER ANXIETY -> rising Company attention
1832 COMMERCIAL OPENING -> river navigation without military transport
1839 PRESSURE -> subsidiary obligations linked to the Afghan campaign
1843 MIANI + DABO -> Napier defeats the Amirs; Sindh is annexed.""",
            [
                "17. Sindh: commercial and strategic context, and Napier's 1843 annexation",
            ],
        ),
        (
            "Sikh strength, succession crisis and two wars",
            "timeline",
            """RANJIT SINGH -> consolidated Punjab + modernised Khalsa army
AMRITSAR 1809 -> Sutlej boundary stabilises Company-Sikh relations
POST-1839 -> court faction, rapid succession and army politicisation
1845-46 FIRST -> Lahore/Bhyrowal | 1848-49 SECOND -> Gujrat -> Punjab annexed.""",
            [
                "18. Ranjit Singh's state, the Khalsa army, and the Treaty of Amritsar, 1809",
                "19. Post-1839 succession crisis: factional instability after Ranjit Singh",
                "20. First Anglo-Sikh War: Mudki to Sobraon, Lahore, and Bhyrowal",
                "21. Second Anglo-Sikh War: the Multan trigger, Chillianwala, Gujrat, and 1849 annexation",
            ],
        ),
        (
            "Lapse, title denial and misgovernment are distinct",
            "comparison",
            """LAPSE -> adopted heir not recognised -> Satara, Jhansi and Nagpur annexed
TITLE / PENSION DENIAL -> Nana Sahib's pension claim is not a territorial lapse case
MISGOVERNMENT -> Awadh annexed in 1856 despite a recognised ruling dynasty
EXAM RULE -> identify the legal pretext before naming the annexation policy.""",
            [
                "22. The Doctrine of Lapse: principles, paramountcy, and the verified cases",
                "23. Awadh, 1856: misgovernance, explicitly NOT Lapse",
            ],
        ),
        (
            "Comparative answer spine and 1857 bridge",
            "synthesis",
            """MYSORE -> centralised reform but diplomatic isolation
MARATHAS -> wide confederate power but fractured command
SIKHS -> strong army and state under Ranjit Singh; destabilised after 1839
1857 BRIDGE -> dispossessed rulers, taluqdars and soldiers add grievances, not one cause.""",
            [
                "24. Dispossession and the road to 1857: a bounded bridge, not a monocausal claim",
                "25. Historiography: four lenses on British territorial expansion",
                "26. Comparative synthesis: Mysore vs Maratha vs Sikh; war vs alliance vs lapse vs misgovernance",
            ],
        ),
    ],
    "modern-indian-history-06": [
        (
            "The Company-state constitutional problem",
            "problem-map",
            """LONDON COMPANY -> shareholders, directors, trade and patronage
INDIAN SOVEREIGN -> revenue, war, justice and legislation after Diwani
CONTRADICTION -> private profit joined to public coercive power
PARLIAMENTARY RESPONSE -> regulate, supervise, centralise and finally transfer rule.""",
            [
                "1. A private corporation as revenue, war and justice authority",
                "2. The crisis that forced Parliament to act, 1770-73: fiscal, political, and patronage -- not humanitarian",
            ],
        ),
        (
            "Regulating Act 1773: first framework",
            "institution-map",
            """GOVERNOR-GENERAL OF BENGAL + COUNCIL OF FOUR -> Warren Hastings first
BOMBAY / MADRAS -> subordinated in war and peace, with practical ambiguities
SUPREME COURT AT CALCUTTA -> begins 1774 under Crown-appointed judges
DIRECTORS REPORT TO MINISTRY -> oversight begins, but Company rule continues.""",
            [
                "3. The Regulating Act, 1773: institutions on paper",
            ],
        ),
        (
            "Why the 1773 design malfunctioned",
            "failure-map",
            """COUNCIL ARITHMETIC -> Francis-Clavering-Monson majority can outvote Hastings
JURISDICTIONAL OVERLAP -> Supreme Court clashes with Company revenue and civil courts
CASES -> Nand Kumar, Patna and Cossijurah expose uncertainty
LESSON -> constitutional repair follows administrative conflict, not a smooth master plan.""",
            [
                "4. Why the Regulating Act failed in practice: the Hastings-Council deadlock",
                "5. The Supreme Court and jurisdictional conflict: Nand Kumar, Patna, Cossijurah",
            ],
        ),
        (
            "Amending Act 1781: targeted jurisdictional repair",
            "before-after",
            """BEFORE -> official acts and revenue matters exposed to disputed Court reach
1781 -> official public acts exempted; revenue jurisdiction excluded
PERSONAL LAW -> Hindu and Muslim law to guide relevant cases
LIMIT -> corrected Court-executive conflict, not the Council voting problem.""",
            [
                "6. The Amending Act (Act of Settlement), 1781: precise corrections, not a general fix",
            ],
        ),
        (
            "Pitt's India Act 1784: dual control in Britain",
            "institution-map",
            """COURT OF DIRECTORS -> commerce, appointments and routine Company administration
BOARD OF CONTROL -> Crown-supervised political, military and revenue direction
INDIA -> stronger Bengal control over presidencies and smaller executive council
VERDICT -> supervision without immediate Crown takeover.""",
            [
                "7. Pitt's India Act, 1784: Board of Control, dual government, and stronger central command",
            ],
        ),
        (
            "Executive consolidation, 1786-1793",
            "timeline",
            """1786 -> Cornwallis may override council in special cases and serve as commander
1793 -> override power generalised to future governors-general and governors
1793 -> Company monopoly renewed for twenty years
DIRECTION -> stronger personal executive within a still Company-run constitution.""",
            [
                "8. The Act of 1786 and Charter Act, 1793: executive authority and continuity",
            ],
        ),
        (
            "Charter Act 1813: partial commercial opening",
            "comparison",
            """ENDED -> Company monopoly over Indian trade
RETAINED -> tea monopoly and trade with China
ADDED -> Crown sovereignty claim, missionary entry and education provision
MEANING -> British industrial access expands while the Company remains territorial ruler.""",
            [
                "9. Charter Act, 1813: free trade, missions, education, and a partial opening",
            ],
        ),
        (
            "Charter Act 1833: all-India centralisation",
            "institution-map",
            """GG OF BENGAL -> GOVERNOR-GENERAL OF INDIA; William Bentinck first
PRESIDENCY LEGISLATURES -> legislative power centralised in the Government of India
LAW MEMBER + LAW COMMISSION -> Macaulay and codification drive
COMPANY COMMERCE ENDS -> corporation becomes a purely administrative agency.""",
            [
                "10. Charter Act, 1833: all-India centralisation, the Law Member, and codification",
            ],
        ),
        (
            "The 1833 equality promise and practice gap",
            "dialectic",
            """STATUTORY LANGUAGE -> Indians not to be excluded from Company office by identity
INSTITUTIONAL REALITY -> patronage and racial barriers remain
EXAM DISTINCTION -> 1833 voices open eligibility; it does not create the 1853 exam
ANALYTICAL USE -> liberal language coexists with an unrepresentative imperial state.""",
            [
                "11. Charter Act, 1833: the non-discrimination promise and the practice gap",
            ],
        ),
        (
            "Charter Act 1853: legislature and recruitment",
            "process-map",
            """EXECUTIVE COUNCIL -> legislative members added for a distinct law-making function
CENTRAL LEGISLATIVE COUNCIL -> procedure resembles a small official parliament
OPEN COMPETITION -> civil-service recruitment principle implemented through later rules
LIMIT -> London examination and access barriers make formal openness unequal in practice.""",
            [
                "12. Charter Act, 1853: legislative-executive separation and the civil-service reform sequence, 1833-1855",
            ],
        ),
        (
            "Government of India Act 1858: transfer, not reinvention",
            "before-after",
            """ABOLISHED -> Company rule, Court of Directors and Board of Control
CREATED -> Secretary of State for India assisted by an India Council
INDIA -> Governor-General also becomes Viceroy; Canning first
CONTINUITY -> central executive, councils, codes and bureaucracy largely survive transfer.""",
            [
                "13. The Government of India Act, 1858: transfer to the Crown, Secretary of State, India Council, and Viceroy",
            ],
        ),
        (
            "Constitutional ladder, 1773-1858",
            "timeline",
            """1773 OVERSIGHT -> 1781 JURISDICTIONAL REPAIR -> 1784 CROWN SUPERVISION
1813 MONOPOLY BREACH -> 1833 CENTRAL GOVERNMENT + CODIFICATION
1853 LEGISLATIVE SPECIALISATION + COMPETITIVE RECRUITMENT
1858 CROWN RULE -> sovereign changes; colonial centralisation remains.""",
            [
                "14. Institutional themes across 1773-1858: centralisation, codification, bureaucracy, and exclusion",
                "15. Historiography of the Company-state: three readings and a defensible synthesis",
                "16. Comparative synthesis: the constitutional ladder, provision-to-effect table, and answer architecture",
            ],
        ),
    ],
}


def split_register(source: str, key: str) -> tuple[str, str]:
    number = key.rsplit("-", 1)[-1]
    marker = f"# FINAL CONSOLIDATED REGISTER NOTES - TOPIC {number}"
    if marker not in source:
        raise ValueError(f"{key}: final register marker missing.")
    main, register = source.split(marker, 1)
    return main.rstrip(), marker + register


def phase_for(key: str, number: int) -> str:
    if key.endswith("-05"):
        if number <= 4:
            return "FOUNDATION"
        if number <= 23:
            return "CORE"
        return "CORE SYNTHESIS"
    if number <= 2:
        return "FOUNDATION"
    if number <= 13:
        return "CORE"
    return "CORE SYNTHESIS"


def source_audit(config_value: dict[str, object]) -> str:
    key = str(config_value["key"])
    if key.endswith("-05"):
        live = (
            "✅ **Bounded official heritage fact:** ASI's 2025-26 tender list includes "
            "maintenance under the Srirangapatna sub-circle, and the Bangalore Circle "
            "issued an expression of interest concerning a museum building at the Tipu "
            "Sultan Museum, Daria Daulat Bagh.\n\n"
            "⚠️ **Inference boundary:** these records establish present heritage management "
            "only. They do not prove any claim about the causes, strength or outcome of the "
            "Anglo-Mysore Wars."
        )
    else:
        live = (
            "✅ **Bounded official constitutional-heritage fact:** PIB's Constitution Day "
            "2025 account records national public engagement with constitutional values "
            "and multilingual access to the Constitution.\n\n"
            "⚠️ **Inference boundary:** this is a public-heritage bridge, not evidence that "
            "the Company-era statutes were democratic. The 1773-1858 acts centralised "
            "imperial control while excluding Indians from effective representation."
        )
    return (
        "#### Source audit, progression and syllabus boundary\n\n"
        "- **Foundation:** chronology, institutions, actors and exact terminology.\n"
        "- **Core:** mechanisms, comparisons, causal chains, Indian agency and exam traps.\n"
        "- **Core synthesis:** historiography, answer architecture, boundaries and bridges.\n"
        "- **Optional Advanced:** the separate owner is taught only after Basic practice.\n"
        "- **Static source order:** repository Markdown -> OCR-searchable Bipan Chandra, "
        "Sekhar Bandyopadhyay and constitutional reference material -> bounded live "
        "official anchor; Qdrant not needed.\n"
        f"- **PYQ integrity:** {config_value['pyq_note']}\n\n"
        "#### Live-linkage block\n\n"
        + live
    )


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
        "scope": "Modern Indian History learner-v2 Topics 05-06",
        "constraints": {
            "panel_count_per_topic": 12,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "complete_embed_ready_lines": True,
            "tracker_untouched": True,
        },
        "topics": topics,
    }
    ASCII_PATH.parent.mkdir(parents=True, exist_ok=True)
    ASCII_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


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
    base.mcq_audit(markdown, key)
    base.mcq_audit(workbook, key)
    spec = ascii_master.normalize_manual_spec_file(ASCII_PATH)[key]
    if len(spec.panels) != 12 or markdown.count("```ascii-master") != 12:
        raise ValueError(f"{key}: authored ASCII panel count failed.")
    graphical = json.loads(graphical_path.read_text(encoding="utf-8"))
    if len(graphical["stages"]) != 13:
        raise ValueError(f"{key}: graphical stage count failed.")
    required_terms = {
        "modern-indian-history-05": [
            "Treaty of Mangalore",
            "Treaty of Bassein",
            "Treaty of Salbai",
            "Subsidiary Alliance",
            "Doctrine of Lapse",
            "Ranjit Singh",
            "Punjab",
            "Awadh",
            "paramountcy",
        ],
        "modern-indian-history-06": [
            "Regulating Act",
            "Supreme Court",
            "Pitt's India Act",
            "Board of Control",
            "Charter Act, 1813",
            "Charter Act, 1833",
            "Charter Act, 1853",
            "Government of India Act, 1858",
            "Secretary of State",
            "Viceroy",
        ],
    }[key]
    missing = [term for term in required_terms if term.casefold() not in markdown.casefold()]
    if missing:
        raise ValueError(f"{key}: missing required concepts: {missing}.")


def configure_base() -> None:
    base.DATE = DATE
    base.TOPICS = TOPICS
    base.PANEL_DATA = PANEL_DATA
    base.ASCII_PATH = ASCII_PATH
    base.SESSION_DIR = SESSION_DIR
    base.GRAPHICAL_DIR = GRAPHICAL_DIR
    base.EXPORT_DIR = EXPORT_DIR
    base.MCQ_REPLACEMENTS_04 = {}
    base.split_register = split_register
    base.phase_for = phase_for
    base.source_audit = source_audit


def main() -> int:
    configure_base()
    write_ascii_spec()
    base.write_section_manifest()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = [ASCII_PATH, SECTION_MANIFEST]
    for config_value in TOPICS:
        markdown, workbook, session_count = base.assemble(config_value)
        key = str(config_value["key"])
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        workbook_path = SESSION_DIR / f"{key}_Solved-Workbook.md"
        source_path.write_text(markdown, encoding="utf-8")
        workbook_path.write_text(workbook, encoding="utf-8")
        graphical_path = base.write_graphical_spec(config_value, markdown)
        manifest = base.write_generation_spec(
            config_value,
            source_path,
            workbook_path,
            graphical_path,
        )
        self_check(markdown, workbook, key, session_count, graphical_path)
        written.extend([source_path, workbook_path, graphical_path, manifest])
        print(
            f"{key}: sessions={session_count}; mcqs=80 (A20/B20/C20/D20); "
            "ascii=12; graphical=13"
        )
    for path in written:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
