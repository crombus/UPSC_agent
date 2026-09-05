"""Build Modern Indian History learner-v2 Topics 09-13.

The generator creates complete reusable Markdown, solved workbooks, manually
bounded ASCII/graphical specifications, and tracker-free staging manifests.
"""

from __future__ import annotations

import hashlib
import json
import re
import textwrap
from pathlib import Path

import carvaka_flowchart
import generate_modern_history_03_04_sequential as common
import generate_v2_section_indexes as section_indexes
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
    / "modern-indian-history-09-13-2026-08-30-sequential.json"
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
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "modern-indian-history--subject-wide-syllabus.json"
)
LOCAL_BOOKS = [
    ROOT
    / "books"
    / "modern india"
    / "MODERN INDIA -- BIPIN CHANDRA -- ENGLISH ##.pdf",
    ROOT
    / "books"
    / "modern india"
    / "INDIA STRUGGLE FOR INDEPENDENCE-- BIPIN C ENG.pdf",
    ROOT
    / "books"
    / "medival_history"
    / "FROM PLASY TO PARTITION -- SEKAR B -- ENGLISH.pdf",
]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Chronology.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
]
PYQ_INDEXES = [
    *common.PYQ_INDEXES,
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2026.md",
]
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]
OFFICIAL_QUESTION_SOURCES = [
    path for path in common.OFFICIAL_QUESTION_SOURCES if path.is_file()
]


def topic(
    number: int,
    title: str,
    basic: str,
    advanced: str,
    canonical: str,
    extra: list[str],
    live_sources: list[str],
    current_note: str,
    ocr_note: str,
    pyq_note: str,
    facts: list[tuple[str, str]],
    traps: list[str],
    mains: list[tuple[int, str, str, list[int]]],
    pyq_solutions: list[tuple[str, str, str, str, str]],
    required_terms: list[str],
) -> dict[str, object]:
    return {
        "number": number,
        "key": f"modern-indian-history-{number:02d}",
        "title": title,
        "basic": KNOWLEDGE / "basic" / basic,
        "advanced": KNOWLEDGE / "advanced" / advanced,
        "canonical": KNOWLEDGE / canonical,
        "extra": [KNOWLEDGE / value for value in extra],
        "live_sources": live_sources,
        "current_note": current_note,
        "ocr_note": ocr_note,
        "pyq_note": pyq_note,
        "facts": facts,
        "traps": traps,
        "mains": mains,
        "pyq_solutions": pyq_solutions,
        "required_terms": required_terms,
    }


TOPICS = [
    topic(
        9,
        "Social & Cultural Policy - Education, the Press, State & Society",
        "09_Social-and-Cultural-Policy-Education-Press.md",
        "09_Social-and-Cultural-Policy-Education-Press.md",
        "09_Social-Cultural-Policy-Education-Press-State-Society_Complete-Topic-Package.md",
        [
            "basic/08_Administrative-Organisation.md",
            "basic/10_Socio-Religious-Reform-Movements.md",
            "basic/14_Foundation-of-INC-and-Moderate-Phase.md",
            "basic/19_Gandhis-Rise-Rowlatt-and-Jallianwala.md",
        ],
        [
            "https://www.cbse.gov.in/cbsenew/documents/"
            "Press_Release_Three_lang_29062026.pdf",
        ],
        "CBSE's June 2026 press-release title on three-language-policy guidelines "
        "is used only as a present-day language-policy bridge. It does not supply "
        "evidence for colonial education, filtration theory or press legislation.",
        "OCR checks located Macaulay and the education debate around PDF page 123 "
        "and the Vernacular Press Act around pages 164 and 204 of Bipan Chandra; "
        "Sekhar Bandyopadhyay discusses the Act around PDF page 230.",
        "Six routed Prelims demands are retained. Four have source-backed demand "
        "cards; Madanapalle and Songs from Prison remain explicit local evidence "
        "gaps. The 2023 Gandhi-Tagore education demand is treated as a bounded "
        "cross-topic Mains owner.",
        [
            ("Hicky's Bengal Gazette", "Hicky's Bengal Gazette began in 1780 and is treated as India's first newspaper."),
            ("Calcutta Madrasa", "Warren Hastings founded the Calcutta Madrasa in 1781 within early Orientalist policy."),
            ("Sanskrit College at Banaras", "The Sanskrit College at Banaras was founded in 1791 as an Orientalist institution."),
            ("Fort William College", "Wellesley founded Fort William College in 1800 to train European Company civil servants in Indian languages and law."),
            ("Charter Act of 1813", "The Charter Act of 1813 assigned one lakh rupees to education and permitted missionary activity."),
            ("Macaulay's Minute", "Macaulay's Minute of 1835 advocated English-medium Western learning for higher education."),
            ("Bentinck's 1835 resolution", "Bentinck's 1835 resolution implemented the Anglicist preference in state education."),
            ("Metcalfe's press policy", "Metcalfe's 1835 press liberalisation earned him the conventional title liberator of the press."),
            ("Wood's Despatch", "Wood's Despatch of 1854 proposed grants-in-aid, education departments, teacher training, vernacular primary schooling and universities."),
            ("Presidency universities", "Universities at Calcutta, Bombay and Madras were established in 1857 as examining institutions."),
            ("Licensing Act of 1857", "The Licensing Act of 1857 marked renewed press restriction during the revolt crisis."),
            ("Vernacular Press Act", "Lytton's Vernacular Press Act of 1878 specifically targeted Indian-language newspapers."),
            ("Repeal of the Vernacular Press Act", "Ripon repealed the Vernacular Press Act in 1882 after sustained Indian criticism."),
            ("Hunter Commission", "The Hunter Commission of 1882 reviewed primary and secondary education."),
            ("Indian Universities Act", "Curzon's Indian Universities Act of 1904 increased official supervision of universities."),
            ("Sadler Commission", "The Sadler Commission of 1917 examined university education with special attention to Calcutta."),
            ("Abolition of sati", "Regulation XVII under Bentinck abolished sati in 1829 after sustained Indian reformist campaigning."),
            ("Legal action on slavery", "Colonial legislation legally addressed slavery in India in 1843, though law did not instantly erase social dependence."),
            ("Widow Remarriage Act", "The Hindu Widows' Remarriage Act of 1856 followed Vidyasagar's scriptural and public campaign."),
            ("Double-edged education", "English education served colonial staffing needs but also enabled a press, professions and nationalist political vocabulary."),
        ],
        [
            "Macaulay's Minute of 1835 and Wood's Despatch of 1854 performed different functions.",
            "Fort William College trained European civil servants, not Indian students.",
            "The Vernacular Press Act targeted Indian-language newspapers rather than all newspapers equally.",
            "Wood's Despatch recommended vernacular primary education even though implementation remained weak.",
            "Statutory social reform must be linked to Indian campaigns and to enforcement limits.",
            "Madanapalle and Songs from Prison must not be answered from unsupported local material.",
        ],
        [
            (10, "Explain why Wood's Despatch is more accurately called a system blueprint than the beginning of English education.", "The Despatch systematised institutions begun under earlier Anglicist policy; it did not originate the 1835 turn.", [4, 5, 8]),
            (10, "How did the vernacular press become a political institution under colonial rule?", "The press linked local-language publics to criticism, association and mobilisation, which explains selective repression.", [0, 7, 11, 12]),
            (15, "English education was a colonial instrument that outgrew its intention. Discuss.", "Its narrow administrative design produced wider professional, journalistic and nationalist capacities without creating mass education.", [4, 5, 8, 9, 19]),
            (15, "Evaluate the interaction between Indian reformers and the colonial state in nineteenth-century social legislation.", "Reformers supplied argument and mobilisation, the state supplied law, and custom exposed the limits of both.", [16, 17, 18, 19]),
            (20, "Analyse education, print and social legislation as the three pillars of a colonial public sphere.", "The public sphere emerged from state-created institutions but became contested through Indian appropriation, unequal access and repression.", [0, 4, 8, 11, 16, 18, 19]),
            (20, "Compare Orientalist, Anglicist and nationalist approaches to education in colonial India.", "The approaches differed over language, knowledge and political purpose, while all treated education as an instrument of social transformation.", [1, 2, 5, 8, 19]),
        ],
        [
            ("2018", "Prelims GS-I", "Wood's Despatch provisions", "solved-demand-card", "Retain grants-in-aid, Departments of Public Instruction, teacher training, vernacular primary education and the proposed university structure; do not confuse the Despatch with Macaulay's 1835 Minute."),
            ("2018", "Prelims GS-I", "Factors behind the introduction of English education", "solved-demand-card", "Connect administrative staffing, Anglicist confidence in Western knowledge, missionary and Indian reformist demand, the 1813 education grant, Macaulay's Minute and Bentinck's resolution."),
            ("2018", "Prelims GS-I", "Colonial educational institutions and founders", "solved-demand-card", "Match Calcutta Madrasa with Warren Hastings, Fort William College with Wellesley, and the 1857 presidency universities with Calcutta, Bombay and Madras."),
            ("2020", "Prelims GS-I", "Purpose of Fort William College", "solved-demand-card", "Its primary official purpose was to train European Company civil servants in Indian languages, law and administration; it was not an Indian mass-education institution."),
            ("2021", "Prelims GS-I", "Madanapalle historical significance", "open-evidence-gap", "The locally held owner records only the routed stem and no explanatory evidence. No association or answer is asserted."),
            ("2021", "Prelims GS-I", "Songs from Prison translation attribution", "open-evidence-gap", "No supporting occurrence exists in the held books or owners. No translator is named and no answer is inferred."),
            ("2023", "GS-I", "Gandhi and Tagore on education and nationalism", "bounded-model", "Both rejected alienating colonial education. Gandhi's Nai Talim centred productive work, vernacular learning and self-reliance; Tagore stressed freedom, nature, creativity and cosmopolitan humanism. Their routes differed, but both connected education with civilisational autonomy."),
        ],
        [
            "Wood's Despatch",
            "Fort William College",
            "Macaulay's Minute",
            "Vernacular Press Act",
            "downward filtration",
            "public sphere",
        ],
    ),
    topic(
        10,
        "Socio-Religious Reform Movements (Brahmo, Arya, Ramakrishna, Aligarh, etc.)",
        "10_Socio-Religious-Reform-Movements.md",
        "10_Socio-Religious-Reform-Movements.md",
        "10_Socio-Religious-Reform-Movements-Brahmo-Arya-Ramakrishna-Aligarh_Complete-Topic-Package.md",
        [
            "basic/09_Social-and-Cultural-Policy-Education-Press.md",
            "basic/14_Foundation-of-INC-and-Moderate-Phase.md",
            "basic/17_Growth-of-Communalism-and-Muslim-League.md",
            "basic/29_Colonial-Legacy-and-Foundations-of-the-Republic.md",
        ],
        [
            "https://www.pmindia.gov.in/en/news_updates/"
            "pm-addresses-the-international-arya-mahasammelan-2025-in-new-delhi/",
        ],
        "The PM India record of the International Arya Mahasammelan 2025 is used "
        "only as an official public-memory anchor for 150 years of Arya Samaj. "
        "Historical evaluation remains grounded in repository owners and OCR books.",
        "OCR checks located Brahmo Samaj around pages 129-132 and Arya Samaj "
        "around pages 221-222 of Bipan Chandra. Sekhar Bandyopadhyay discusses "
        "Brahmo around pages 169-170, Arya around page 171 and Rukhmabai around "
        "pages 254-255.",
        "The package solves the 2019 and 2021 GS-I reform demands and the 2025 "
        "Phule demand. Routed objective demands are covered by evidence cards, "
        "except Vital-Vidhvansak, which remains an explicit unsupported local gap.",
        [
            ("Atmiya Sabha", "Rammohan Roy founded the Atmiya Sabha in Calcutta in 1815 as an early reform association."),
            ("Brahmo Samaj", "Rammohan Roy founded the Brahmo Samaj in Calcutta in 1828 around monotheism, reason and social reform."),
            ("Debendranath Tagore", "Debendranath Tagore revitalised the Brahmo movement after Rammohan Roy."),
            ("Sadharan Brahmo Samaj", "The Sadharan Brahmo Samaj formed in 1878 after conflict around Keshab Chandra Sen."),
            ("Young Bengal", "Henry Vivian Derozio's Young Bengal current promoted free thought and criticism of orthodoxy."),
            ("Prarthana Samaj", "Atmaram Pandurang, M.G. Ranade and R.G. Bhandarkar shaped the Prarthana Samaj's cautious social reform."),
            ("Arya Samaj", "Dayanand Saraswati founded Arya Samaj in 1875 and called for a return to the Vedas."),
            ("Arya institutions", "Satyarth Prakash, shuddhi and DAV education are central associations of Arya Samaj."),
            ("Ramakrishna Mission", "Vivekananda founded the Ramakrishna Mission in 1897 after his 1893 Chicago address."),
            ("Satyashodhak Samaj", "Jotirao Phule founded Satyashodhak Samaj in 1873 to challenge Brahmanical domination and organise non-Brahman groups."),
            ("Phule girls' school", "Jotirao and Savitribai Phule opened a girls' school at Poona in 1851."),
            ("Bethune School and Vidyasagar", "Bethune School opened in Calcutta in 1849, and Vidyasagar served as its Secretary and advanced women's education."),
            ("Rukhmabai case", "Rukhmabai contested conjugal rights in the Bombay High Court during 1884-88 and lost the case after making child marriage a public issue."),
            ("Age of Consent Act", "The Age of Consent Act of 1891 raised the relevant age from ten to twelve amid intense controversy."),
            ("Aligarh movement", "Syed Ahmad Khan's Aligarh movement used modern education, including MAO College in 1875, to address Muslim social disadvantage."),
            ("Deoband", "The Deoband seminary was founded in 1866 and represented an orthodox educational response distinct from Aligarh."),
            ("Theosophical Society", "The Theosophical Society was founded in 1875 and shifted its headquarters to Adyar in 1882."),
            ("Community reform", "Rahnumai Mazdayasnan Sabha and Singh Sabha represent Parsi and Sikh community reform respectively."),
            ("Sri Narayana Guru", "Sri Narayana Guru pursued a spiritually framed challenge to caste hierarchy in Kerala."),
            ("Self-Respect Movement", "Periyar led the Self-Respect Movement, linking anti-Brahmanism, gender critique and social dignity in south India."),
        ],
        [
            "Reformist and revivalist are analytical tendencies, not simple progressive and conservative boxes.",
            "Ramakrishna Mission was founded by Vivekananda, not by Ramakrishna Paramhansa.",
            "Aligarh modernism and Deoband's seminary route were different responses to colonial change.",
            "Bethune School's 1849 founding and Vidyasagar's Secretary role must not be conflated.",
            "Rukhmabai lost her case; the case's significance lies in public argument and later reform pressure.",
            "Vital-Vidhvansak must remain unanswered until an authoritative supporting source is added.",
        ],
        [
            (10, "Trace the development of the Brahmo movement from Rammohan Roy to the Sadharan Brahmo Samaj.", "The movement institutionalised rational monotheism but repeatedly divided over authority, social radicalism and religious form.", [0, 1, 2, 3]),
            (10, "Distinguish the methods of Aligarh and Deoband in responding to colonial rule.", "Both addressed Muslim social crisis through education, but differed sharply over modern Western learning and religious authority.", [14, 15]),
            (15, "Was nineteenth-century Indian reform a renaissance or an elite awakening?", "Reform widened rational criticism and public action, yet its reach was uneven and corrected by anti-caste and women's agency.", [1, 4, 6, 9, 10, 18, 19]),
            (15, "Discuss Jotirao Phule's social reform efforts and writings.", "Phule converted caste from a question of custom into a structure of power and made education and organisation instruments of emancipation.", [9, 10, 18, 19]),
            (20, "Compare reformist, revivalist, anti-caste and community-specific reform streams in colonial India.", "The streams differed in authority and constituency but shared modern instruments of print, education, association and mobilisation.", [1, 5, 6, 8, 9, 14, 15, 17]),
            (20, "Examine the movement from reform for women to reform by women in nineteenth-century India.", "Male-led campaigns opened legal and educational space, while Savitribai, Rukhmabai and Pandita Ramabai shifted the debate toward agency and rights.", [10, 11, 12, 13]),
        ],
        [
            ("2018", "Prelims GS-I", "Chronology of nineteenth-century reform events", "solved-demand-card", "Use the anchor order Brahmo Samaj 1828, Satyashodhak Samaj 1873, Arya Samaj and MAO College 1875, Sadharan Brahmo 1878, and Ramakrishna Mission 1897."),
            ("2019", "Prelims GS-I", "Reform organisations and leaders", "solved-demand-card", "Match Brahmo-Rammohan Roy, Arya-Dayanand, Ramakrishna Mission-Vivekananda, Satyashodhak-Phule, and Aligarh-Syed Ahmad Khan."),
            ("2019", "GS-I", "Indian Renaissance and national identity", "model-solution", "The reform era created rational criticism, cultural self-respect, print publics and voluntary associations that fed nationalism. Its urban and upper-caste limits require correction through Phule, women's agency and regional community reform."),
            ("2020", "Prelims GS-I", "Vital-Vidhvansak and early Dalit journalism", "open-evidence-gap", "The held repository contains no supporting attribution and no official local key. No publisher is asserted."),
            ("2020", "Prelims GS-I", "Rukhmabai case", "solved-demand-card", "The case ran in the Bombay High Court in 1884-88 over conjugal rights after infant marriage. Rukhmabai lost, but the controversy strengthened pressure preceding the 1891 Age of Consent Act."),
            ("2021", "Prelims GS-I", "Bethune Female School Secretary", "solved-demand-card", "The source-backed association is Ishwar Chandra Vidyasagar as Secretary; do not misstate him as the school's founder."),
            ("2021", "GS-I", "Young Bengal and Brahmo Samaj", "model-solution", "Young Bengal used iconoclastic free thought under Derozio, while Brahmo Samaj built a durable monotheistic association under Rammohan Roy and successors. Both challenged orthodoxy, but Brahmo developed a wider institutional afterlife."),
            ("2025", "GS-I", "Jotirao Phule's efforts and writings", "model-solution", "Phule founded Satyashodhak Samaj in 1873, attacked Brahmanical control, used Gulamgiri and an alternative Aryan account, promoted girls' education with Savitribai and organised Shudra-Ati-Shudra assertion. His peasant-caste coalition also carried internal tensions."),
            ("2025", "Prelims GS-I", "Raja Rammohan Roy's thought and reform", "solved-demand-card", "Retain monotheism, reason, opposition to sati and idolatry, support for English and scientific education, Brahmo Samaj and Sambad Kaumudi."),
            ("2025", "Prelims GS-I", "Founder of the Self-Respect Movement", "solved-demand-card", "The movement is associated with E.V. Ramaswamy Naicker, Periyar, and an anti-caste, anti-Brahmanical programme of social dignity."),
        ],
        [
            "Brahmo Samaj",
            "Arya Samaj",
            "Ramakrishna Mission",
            "Satyashodhak Samaj",
            "Aligarh",
            "Rukhmabai",
            "Periyar",
        ],
    ),
    topic(
        11,
        "The Revolt of 1857",
        "11_The-Revolt-of-1857.md",
        "11_The-Revolt-of-1857.md",
        "11_The-Revolt-of-1857_Complete-Topic-Package.md",
        [
            "basic/05_British-Territorial-Expansion.md",
            "basic/07_Economic-Impact-of-British-Rule.md",
            "basic/08_Administrative-Organisation.md",
            "basic/12_Administrative-Changes-After-1858.md",
        ],
        ["https://archaeology.haryana.gov.in/node"],
        "A 2026 search found no sufficiently specific official memorial update to "
        "force into the historical narrative. The Haryana archaeology gateway is "
        "used only as a bounded public-history method link; no disputed claim about "
        "the revolt's starting point or memorial scale is imported.",
        "OCR checks located Bipan Chandra's Revolt chapter around PDF page 135 and "
        "India's Struggle for Independence around page 24. Sekhar Bandyopadhyay "
        "supports the Awadh-taluqdar restoration chain around PDF page 87.",
        "The verified 2019 GS-I recurrent-rebellions demand is solved. The 2026 "
        "Awadh-taluqdar objective demand is integrated as a source-backed demand "
        "card while its provisional answer key is not converted into an answer letter.",
        [
            ("Pre-1857 civil rebellions", "Sanyasi, Chuar, poligar and other civil rebellions show recurrent local resistance before 1857 without forming one national conspiracy."),
            ("Santhal Hool", "The Santhal Hool of 1855-56 under Sidhu and Kanhu was a distinct anti-diku and anti-colonial uprising."),
            ("Doctrine of Lapse", "Dalhousie's Doctrine of Lapse dispossessed ruling houses and deepened political hostility before 1857."),
            ("Annexation of Awadh", "Awadh was annexed in 1856 on alleged misgovernment, not through the Doctrine of Lapse."),
            ("General Service Enlistment Act", "The General Service Enlistment Act of 1856 intensified sepoy anxiety over overseas service and caste practice."),
            ("Enfield cartridge", "The greased-cartridge rumour was the immediate trigger of 1857 rather than its complete cause."),
            ("Barrackpore", "Mangal Pandey's Barrackpore episode occurred on 29 March 1857 before the main outbreak."),
            ("Meerut outbreak", "The main revolt began at Meerut on 10 May 1857 and the sepoys then moved to Delhi."),
            ("Delhi centre", "Bahadur Shah Zafar became the symbolic emperor at Delhi, while Bakht Khan was associated with rebel command."),
            ("Kanpur leadership", "Nana Saheb, Tantia Tope and Azimullah Khan are associated with the Kanpur centre."),
            ("Awadh leadership", "Begum Hazrat Mahal became a major political leader of resistance in Awadh."),
            ("Jhansi leadership", "Rani Lakshmibai led resistance at Jhansi and became a central memory of 1857."),
            ("Bihar leadership", "Kunwar Singh led the revolt in Bihar despite his advanced age."),
            ("Bareilly leadership", "Khan Bahadur Khan is associated with rebel leadership at Bareilly."),
            ("Awadh taluqdars", "British settlement displaced Awadh taluqdars before the revolt, and the post-revolt state restored their authority to secure collaboration."),
            ("North-Western Provinces auctions", "The source records 110,000 acres auctioned in the North-Western Provinces in 1853 as a bounded index of agrarian dispossession."),
            ("Uneven geography", "The revolt concentrated in north and central India while south India, much of Punjab and many western regions did not join."),
            ("British advantages", "British communications, reinforcements, resources, loyal rulers and loyal Indian troops outweighed fragmented rebel command."),
            ("Composite character", "The most defensible description is a sepoy mutiny in origin that became a wider civil and popular revolt in several regions."),
            ("Government of India Act 1858", "The Government of India Act 1858 ended Company rule and transferred authority directly to the Crown."),
        ],
        [
            "Awadh annexation rested on alleged misgovernment, not the Doctrine of Lapse.",
            "Barrackpore on 29 March preceded the main Meerut outbreak of 10 May.",
            "The cartridge was a trigger, not a sufficient causal explanation.",
            "Bahadur Shah Zafar was a symbolic head rather than an operational commander.",
            "Santhal Hool preceded and differed from the sepoy-led revolt.",
            "No single label captures the revolt's military origin, civil depth and regional limitation.",
        ],
        [
            (10, "Why did Awadh become the deepest social theatre of the Revolt of 1857?", "Annexation joined sepoy recruitment, taluqdar dispossession, peasant pressure and court decline in one region.", [3, 10, 14, 15]),
            (10, "Explain why the cartridge issue cannot by itself explain the Revolt of 1857.", "The cartridge activated accumulated political, agrarian, military and religious anxieties; it did not create them.", [2, 3, 4, 5]),
            (15, "Was the Revolt of 1857 a sepoy mutiny or a popular rebellion?", "It was military in origin, regionally popular in development and not a modern all-India national movement.", [7, 8, 9, 10, 14, 16, 18]),
            (15, "Analyse the reasons for the failure of the Revolt of 1857.", "Fragmented leadership and regional objectives faced a globally resourced empire with superior communications and Indian allies.", [16, 17, 18]),
            (20, "Examine the causes, social composition, geography and consequences of the Revolt of 1857.", "The revolt resulted from converging group grievances, acquired different regional social bases and remade colonial governance despite military defeat.", [0, 2, 3, 4, 5, 14, 16, 19]),
            (20, "Discuss the historiographical interpretations of 1857 and offer a reasoned verdict.", "Official, nationalist, restorationist and social-history readings each capture one dimension; a composite anti-colonial revolt is the best conclusion.", [0, 14, 16, 18, 19]),
        ],
        [
            ("2019", "GS-I", "1857 as the culmination of earlier recurrent rebellions", "model-solution", "Earlier civil and tribal risings established a pattern of resistance to revenue pressure, dispossession and outsider penetration. They remained local and uncoordinated, but 1857 joined sepoy networks with wider civil grievances across a larger north Indian theatre. It was a culmination in scale and convergence, not one continuous conspiracy."),
            ("2026", "Prelims GS-I", "British revenue policy toward Awadh taluqdars after annexation", "solved-demand-card", "After the 1856 settlement many taluqdars lost status and estates, helping create aristocratic resistance. Their wartime return often met peasant support, and the post-revolt Raj restored their authority as part of a new alliance. No provisional answer letter is inferred."),
        ],
        [
            "General Service Enlistment Act",
            "Awadh taluqdars",
            "Bahadur Shah Zafar",
            "Bakht Khan",
            "Kunwar Singh",
            "composite character",
        ],
    ),
    topic(
        12,
        "Administrative & Constitutional Changes after 1858 (Crown Rule; Councils Acts)",
        "12_Administrative-Changes-After-1858.md",
        "12_Administrative-Changes-After-1858.md",
        "12_Administrative-Constitutional-Changes-After-1858-Crown-Rule-Councils-Acts_Complete-Topic-Package.md",
        [
            "basic/06_Government-Structure-and-Constitutional-Development-1757-1858.md",
            "basic/08_Administrative-Organisation.md",
            "basic/11_The-Revolt-of-1857.md",
            "basic/14_Foundation-of-INC-and-Moderate-Phase.md",
        ],
        ["https://pib.gov.in/PressReleasePage.aspx?PRID=2076894"],
        "PIB's Constitution-75 campaign record is used only as a present-day "
        "constitutional-memory bridge. It does not imply continuity between colonial "
        "consultative councils and democratic responsible government.",
        "OCR checks located the Secretary of State and Council structure around PDF "
        "page 153, the Indian Councils Act 1861 around page 154, local "
        "self-government around page 157 and the 1892 Act around page 210 of Bipan Chandra.",
        "Repository routing audits assign no direct 2018-2026 PYQ to Topic 12. "
        "The package therefore records a transparent zero-direct-PYQ audit and uses "
        "only original practice plus bounded links to Topics 06, 08, 11 and 14.",
        [
            ("Government of India Act 1858", "The Government of India Act 1858 ended Company rule and abolished the Board of Control."),
            ("Secretary of State for India", "A British Cabinet minister, the Secretary of State for India controlled Indian affairs from London."),
            ("Council of India", "The Secretary of State was assisted by a fifteen-member Council of India."),
            ("Viceroy", "The Governor-General also became the Crown's Viceroy, and Canning was the first Viceroy."),
            ("Queen's Proclamation", "The 1858 Proclamation promised religious non-interference, treaty respect and formal equality in public employment."),
            ("Princes after 1858", "The Raj ended Lapse-style annexation and used treaty guarantees to turn princes into protected but subordinate allies."),
            ("Army reorganisation", "After 1857 the Raj increased the European proportion, guarded artillery and divided recruitment by region, caste and community."),
            ("Indian Councils Act 1861", "The 1861 Act restored legislative councils and permitted nominated non-official Indian members."),
            ("Portfolio system", "Canning's portfolio system assigned departmental responsibility within the executive council."),
            ("Legislative devolution", "The 1861 settlement restored limited legislative powers to Bombay and Madras and enabled new provincial councils."),
            ("Mayo's decentralisation", "Mayo's financial decentralisation from 1870 assigned selected spending responsibilities to provinces."),
            ("Ripon's Resolution", "Ripon's 1882 Resolution encouraged municipal and district boards and became a conventional landmark of local self-government."),
            ("Indian Councils Act 1892", "The 1892 Act enlarged councils and accepted an indirect election principle through recommending bodies."),
            ("Budget discussion", "The 1892 Act allowed budget discussion and questions but not executive responsibility or full budget control."),
            ("Controlled association", "The Councils Acts associated selected Indians with legislation without creating representative responsible government."),
            ("Equality gap", "Racial barriers and examination conditions frustrated the Proclamation's promise of equal public employment."),
            ("Political training", "Local bodies and councils trained Indian elites in budgets, questions, candidature and organised public argument."),
            ("Direct imperial control", "Crown rule tied Indian administration more directly to British Cabinet, parliamentary and imperial strategy."),
            ("Tighter paramountcy", "Security for princely dynasties coexisted with tighter British paramountcy and reduced external autonomy."),
            ("Administrative continuity", "The collector, police, courts and revenue priorities survived the transfer from Company to Crown."),
        ],
        [
            "Secretary of State in London and Viceroy in India were different offices.",
            "The 1861 Act used nomination rather than direct election.",
            "The 1892 Act permitted discussion but not responsible government.",
            "Decentralisation was administrative and fiscal, not colonial federalism.",
            "The Queen's Proclamation's equality clause must be tested against racial practice.",
            "Post-1858 conciliation of princes coexisted with paramountcy rather than sovereign equality.",
        ],
        [
            (10, "What changed and what continued under the Government of India Act 1858?", "Sovereignty and the London control chain changed, while the local coercive and revenue machinery largely continued.", [0, 1, 2, 3, 17, 19]),
            (10, "Why is the Indian Councils Act 1861 better described as association than representation?", "It admitted nominated Indians to deliberation while withholding election, budget power and executive responsibility.", [7, 8, 9, 14]),
            (15, "Assess the Queen's Proclamation as both a conciliatory charter and an imperial instrument.", "Its promises reassured religion, princes and public employment while rebuilding a more secure colonial alliance.", [4, 5, 15, 18]),
            (15, "Trace the constitutional movement from the Councils Act 1861 to the Councils Act 1892.", "The movement ran from nomination and legislative devolution to indirect selection, questions and budget discussion, not to responsibility.", [7, 8, 9, 12, 13, 14]),
            (20, "Analyse the constitutional, military, princely and administrative reconstruction of the Raj after 1857.", "The post-revolt state centralised imperial sovereignty while decentralising selected costs and rebuilding alliances with princes, landlords and Indian elites.", [0, 4, 5, 6, 7, 10, 11, 17, 18]),
            (20, "Did local self-government under Mayo and Ripon democratise colonial India?", "The reforms created administrative devolution and political training, but finance, official supervision and executive supremacy limited democratisation.", [10, 11, 13, 16]),
        ],
        [],
        [
            "Government of India Act 1858",
            "Secretary of State for India",
            "Council of India",
            "Indian Councils Act 1861",
            "Indian Councils Act 1892",
            "Ripon's Resolution",
        ],
    ),
    topic(
        13,
        "India and Her Neighbours (Afghanistan, Burma, Nepal, Tibet, NW Frontier)",
        "13_India-and-Her-Neighbours.md",
        "13_India-and-Her-Neighbours.md",
        "13_India-and-Her-Neighbours-Afghanistan-Burma-Nepal-Tibet-NW-Frontier_Complete-Topic-Package.md",
        [
            "basic/05_British-Territorial-Expansion.md",
            "basic/07_Economic-Impact-of-British-Rule.md",
            "basic/12_Administrative-Changes-After-1858.md",
            "basic/28_Integration-of-Princely-States.md",
        ],
        [
            "https://pib.gov.in/PressReleasePage.aspx?"
            "PRID=2282625&reg=48&lang=1",
        ],
        "PIB's record of the July 2026 India-Myanmar national-level meeting is "
        "used only as a contemporary border-security and connectivity bridge. "
        "It is not evidence for nineteenth-century annexation, treaties or boundaries.",
        "OCR checks located the Treaty of Yandabo around PDF page 172, Gandamak "
        "around page 180 and Tibet/Younghusband around pages 180-183 of Bipan "
        "Chandra. These are cross-checked against the repository owner.",
        "Repository routing audits assign no direct Modern-History PYQ to Topic 13. "
        "Geography and International Relations questions on current neighbours remain "
        "outside this owner's historical frontier-policy scope.",
        [
            ("Imperial defensive ring", "British India treated neighbouring states and frontier zones as a strategic ring around the Indian empire."),
            ("Great Game", "The Great Game describes Anglo-Russian rivalry in Central Asia that shaped British policy toward Afghanistan."),
            ("Close-border policy", "Close-border policy sought to defend settled limits without permanent advance into tribal or Afghan territory."),
            ("Forward policy", "Forward policy used missions, posts, subsidies, war and political control to pre-empt perceived rival influence."),
            ("First Anglo-Afghan War", "The First Anglo-Afghan War of 1839-42 ended in a disastrous British retreat from Kabul."),
            ("Second Anglo-Afghan War", "The Second Anglo-Afghan War of 1878-80 reflected Lytton's forward policy."),
            ("Treaty of Gandamak", "The Treaty of Gandamak of 1879 followed the Second Anglo-Afghan War and expanded British influence over Afghan external affairs."),
            ("Durand Line", "The Durand agreement of 1893 marked the Afghan frontier sphere under colonial strategic pressure."),
            ("North-West Frontier Province", "Curzon created the North-West Frontier Province in 1901 as a special frontier administration."),
            ("First Anglo-Burmese War", "The First Anglo-Burmese War of 1824-26 ended with the Treaty of Yandabo."),
            ("Second Anglo-Burmese War", "The Second Anglo-Burmese War of 1852 led to the annexation of Lower Burma under Dalhousie."),
            ("Third Anglo-Burmese War", "The Third Anglo-Burmese War of 1885 led to the annexation of Upper Burma under Dufferin."),
            ("Burma and British India", "Burma remained administratively part of British India until its separation in 1937."),
            ("Anglo-Nepalese War", "The Anglo-Nepalese War of 1814-16 ended with the Treaty of Sagauli."),
            ("Nepal settlement", "The Nepal settlement combined a British Residency, buffer-state influence and Gurkha recruitment without annexation."),
            ("Younghusband Mission", "Curzon's Younghusband Mission entered Tibet in 1904 and produced the Lhasa Convention."),
            ("Sikkim and Bhutan", "Treaties and protectorate-style influence drew Sikkim and Bhutan into the Himalayan buffer system."),
            ("Buffer versus annexation", "Afghanistan and Nepal were managed mainly as buffers, whereas Burma was conquered and annexed in stages."),
            ("Indian revenue burden", "Frontier wars and garrisons were charged to Indian revenue even when their strategic purpose was imperial."),
            ("Boundary legacy", "Independent India inherited frontier lines and administrative habits designed for empire rather than national democratic consent."),
        ],
        [
            "Yandabo belongs to Burma, Sagauli to Nepal and Gandamak to Afghanistan.",
            "The Durand Line of 1893 and the Younghusband Mission of 1904 are different theatres.",
            "Forward policy did not always mean formal annexation.",
            "Nepal remained a buffer state while Burma became a province of the empire.",
            "Burma's 1937 separation was administrative separation within empire, not independence.",
            "Historical agreements must not be presented as conclusions on current legal boundary status.",
        ],
        [
            (10, "Why did British frontier policy oscillate between close-border and forward approaches?", "Neither low-cost restraint nor expensive advance fully resolved rivalry, tribal autonomy and the problem of buffer control.", [1, 2, 3, 8]),
            (10, "Distinguish the Treaty of Yandabo, Treaty of Sagauli and Treaty of Gandamak.", "The three treaties belong to different theatres, wars and strategic outcomes and should be learned as a comparison set.", [6, 9, 13]),
            (15, "Compare British policy toward Afghanistan and Burma.", "Afghanistan was preserved as a controlled buffer against a great-power threat, while Burma was annexed where commercial and strategic expansion faced no equivalent rival.", [1, 4, 5, 6, 9, 10, 11, 17]),
            (15, "Assess Nepal's place in the British Indian frontier system.", "Nepal combined defeat, treaty dependence, diplomatic influence and military recruitment without loss of formal statehood.", [13, 14, 17]),
            (20, "Analyse the strategic, commercial and fiscal dimensions of British frontier policy.", "Security language joined rival-power fear, commercial expansion and costs imposed on Indian revenue across distinct frontier theatres.", [0, 1, 3, 9, 10, 11, 15, 18]),
            (20, "Evaluate the post-colonial legacy of colonial frontier-making in South Asia.", "The empire left boundaries and exceptional frontier institutions shaped by imperial security, requiring independent states to manage inherited mismatches.", [7, 8, 12, 15, 16, 19]),
        ],
        [],
        [
            "Great Game",
            "Treaty of Gandamak",
            "Durand Line",
            "Treaty of Yandabo",
            "Treaty of Sagauli",
            "Younghusband Mission",
        ],
    ),
]


PANEL_TYPES = [
    "timeline",
    "causal-chain",
    "comparison",
    "institution-map",
    "evidence-chain",
    "argument-map",
]


def panel_data(config: dict[str, object]) -> list[tuple[str, str, str, list[str]]]:
    panels: list[tuple[str, str, str, list[str]]] = []
    scope = {
        9: "colonial education and press",
        10: "socio-religious reform",
        11: "the 1857 revolt",
        12: "post-1858 Crown rule",
        13: "colonial frontier policy",
    }[int(config["number"])]
    for index, (label, statement) in enumerate(config["facts"][:12]):
        wrapped = textwrap.wrap(statement, width=82)
        body = "\n".join(
            [
                f"FOCUS -> {label}",
                *[f"EVIDENCE -> {line}" if i == 0 else f"            {line}" for i, line in enumerate(wrapped)],
                f"EXAM USE -> use {label} to match actor, date, mechanism and limit.",
                f"LIMIT -> do not transfer {label} to another institution or theatre.",
            ]
        )
        panels.append(
            (
                f"{label} in {scope}",
                PANEL_TYPES[index % len(PANEL_TYPES)],
                body,
                [label, str(config["title"])],
            )
        )
    return panels


PANEL_DATA = {str(config["key"]): panel_data(config) for config in TOPICS}


def split_h3(fragment: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(re.finditer(r"(?m)^### (.+?)\s*$", fragment))
    if not matches:
        return fragment, []
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(fragment)
        sections.append((match.group(1), fragment[match.end():end].strip()))
    return fragment[: matches[0].start()].strip(), sections


def session_terms(title: str, fragment: str) -> list[str]:
    terms = []
    for candidate in re.findall(r"\*\*(.+?)\*\*", fragment):
        clean = re.sub(r"[*_`]+", "", candidate).strip()
        if 2 <= len(clean) <= 38 and clean.casefold() not in {item.casefold() for item in terms}:
            terms.append(clean)
        if len(terms) == 4:
            break
    if len(terms) < 3:
        terms.extend(
            word
            for word in re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]+", title)
            if word.casefold() not in {item.casefold() for item in terms}
        )
    terms = terms[:4] or ["context", "evidence", "analysis", "verdict"]
    return terms


def session_visual(title: str, terms: list[str]) -> str:
    chain = " -> ".join(terms)
    return (
        "#### VISUAL FIRST\n\n"
        "```text\n"
        f"{title.upper()}\n"
        f"{chain}\n"
        "context -> evidence -> mechanism -> qualification -> UPSC judgement\n"
        "```\n\n"
        "*The visual fixes the subtopic's evidence-to-judgement sequence before detail.*"
    )


def session_definitions(
    title: str,
    topic_title: str,
    terms: list[str],
) -> str:
    usable = [*terms]
    for fallback in ("context", "evidence", "mechanism", "interpretation"):
        if len(usable) >= 4:
            break
        usable.append(fallback)
    return (
        "#### CONCEPT DEFINITIONS\n\n"
        f"- **Plain definition:** {title} is a learner's map within {topic_title} "
        f"that groups {usable[0]}, {usable[1]} and {usable[2]}.\n"
        f"- **Technical definition:** Technically, {title} analyses how "
        f"{usable[0]} interacts with {usable[1]} and tests that relationship "
        f"through {usable[2]} and {usable[3]}."
    )


def phase_for(number: int, total: int) -> str:
    if number <= 3:
        return "FOUNDATION"
    if number > total - 3:
        return "CORE SYNTHESIS"
    return "CORE"


def extract_teaching_and_pyqs(
    config: dict[str, object],
) -> tuple[list[str], list[str]]:
    basic = Path(config["basic"]).read_text(encoding="utf-8")
    _, sections = common.split_h2(basic)
    fragments: list[tuple[str, str]] = []
    pyqs: list[str] = []
    for title, fragment in sections:
        if "PYQ Integration" in title:
            pyqs.append(common.lower_headings(fragment))
            continue
        if title.startswith("8. Answer architecture"):
            preface, subsections = split_h3(fragment)
            preface_lines = preface.splitlines()
            if len(preface_lines) > 1 and "\n".join(preface_lines[1:]).strip():
                fragments.append(
                    (
                        "Answer architecture overview",
                        "## Answer architecture overview\n"
                        + "\n".join(preface_lines[1:]).strip(),
                    )
                )
            for subtitle, content in subsections:
                fragments.append((subtitle, f"## {subtitle}\n\n{content}"))
        else:
            fragments.append((title, fragment))

    sessions: list[str] = []
    total = len(fragments)
    for number, (raw_title, fragment) in enumerate(fragments, 1):
        title = (
            f"High-risk factual distinctions in {config['title']}"
            if raw_title == "5. UPSC Traps"
            else raw_title
        )
        lines = fragment.splitlines()
        body = "\n".join(lines[1:]).strip()
        if config["key"] == "modern-indian-history-11":
            body = body.replace(
                '- **Why the southern and western presidencies stayed out '
                '(a standard "explain the non-spread" demand):**',
                "##### Non-participation in the southern and western presidencies",
            )
        terms = session_terms(title, body)
        enhanced = (
            f"## {title}\n\n"
            + session_visual(title, terms)
            + "\n\n"
            + session_definitions(title, str(config["title"]), terms)
            + "\n\n"
            + body
            + "\n\n#### EXAM LINK\n\n"
            + "- **Prelims:** preserve the exact actor-date-institution match and eliminate category errors.\n"
            + "- **Mains:** connect evidence to mechanism, add one limitation and end with a graded verdict.\n\n"
            + "#### MINI RECAP\n\n"
            + f"- Retain the distinction expressed by **{title}**; do not reduce it to an isolated fact."
        )
        sessions.append(
            common.session_fragment(enhanced, number, phase_for(number, total))
        )

    advanced = Path(config["advanced"]).read_text(encoding="utf-8")
    _, advanced_sections = common.split_h2(advanced)
    for title, fragment in advanced_sections:
        if "PYQ Integration" in title:
            pyqs.append(common.lower_headings(fragment))
    return sessions, pyqs


def build_mcqs(config: dict[str, object]) -> str:
    facts: list[tuple[str, str]] = config["facts"]
    variants = [
        "Which statement correctly identifies {label}?",
        "Which chronology card should be filed under {label}?",
        "Which option should a candidate retain when revising {label}?",
        "Which statement avoids a common matching trap about {label}?",
    ]
    blocks: list[str] = []
    for fact_index, (label, statement) in enumerate(facts):
        for variant_index, template in enumerate(variants):
            number = fact_index * 4 + variant_index + 1
            expected = "ABCD"[(number - 1) % 4]
            wrongs = [
                facts[(fact_index + variant_index + offset) % len(facts)][1]
                for offset in (1, 2, 3)
            ]
            choices = {expected: statement}
            for letter, wrong in zip(
                [letter for letter in "ABCD" if letter != expected],
                wrongs,
            ):
                choices[letter] = wrong
            blocks.append(
                f"### Q{number}. {template.format(label=label)}\n\n"
                + "\n".join(f"{letter}. {choices[letter]}" for letter in "ABCD")
                + f"\n\n**Answer: {expected}.**\n"
                + f"**Explanation:** {statement} This distinction preserves the "
                "source-backed chronology and prevents cross-matching errors in UPSC elimination."
            )
    return "\n\n".join(blocks)


def solved_pyq_section(config: dict[str, object], pyq_blocks: list[str]) -> str:
    if pyq_blocks:
        audit = "\n\n".join(pyq_blocks)
    else:
        audit = (
            "### TRANSPARENT ZERO-DIRECT-PYQ AUDIT\n\n"
            f"{config['pyq_note']}\n\n"
            "No adjacent Geography, International Relations, Governance or Polity "
            "question is relabelled as a direct Modern History PYQ."
        )
    cards = []
    for number, (year, paper, demand, status, model) in enumerate(
        config["pyq_solutions"], 1
    ):
        cards.append(
            f"### PYQ DEMAND CARD {number} - {year} {paper}\n\n"
            f"**Demand:** {demand}\n\n"
            f"**Status:** {status}\n\n"
            f"**Model solution / safe handling:** {model}"
        )
    return audit + ("\n\n" + "\n\n".join(cards) if cards else "")


def original_mains_section(config: dict[str, object]) -> str:
    facts: list[tuple[str, str]] = config["facts"]
    blocks = []
    for number, (marks, prompt, thesis, indexes) in enumerate(config["mains"], 1):
        word_limit = {10: 150, 15: 250, 20: 300}[marks]
        evidence = "\n".join(
            f"- {facts[index][1]}" for index in indexes
        )
        blocks.append(
            f"### ORIGINAL MAINS {number} - {marks} MARKS\n\n"
            f"**Question:** {prompt} Answer in about {word_limit} words.\n\n"
            f"**Model thesis:** {thesis}\n\n"
            "**Evidence spine:**\n\n"
            f"{evidence}\n\n"
            "**Balance:** Distinguish intention from outcome, identify regional or "
            "social variation, and avoid treating a formal measure as complete implementation.\n\n"
            f"**Conclusion:** {thesis}"
        )
    return "\n\n".join(blocks)


def source_audit(config: dict[str, object]) -> str:
    return (
        "### SOURCE, PROGRESSION AND CURRENT-LINKAGE AUDIT\n\n"
        "- **Repository owners queried:** Basic and Advanced Markdown for this topic, "
        "the master chronology, syllabus map and linked Modern History owners.\n"
        f"- **OCR book evidence queried:** {config['ocr_note']}\n"
        "- **Qdrant:** not used; Markdown plus searchable local PDFs were sufficient.\n"
        f"- **PYQ integrity:** {config['pyq_note']}\n"
        f"- **Bounded live linkage:** {config['current_note']}\n"
        "- **Fact/inference rule:** historical claims are source-backed; analytical "
        "judgements are explicitly framed as interpretation and do not invent figures."
    )


def advanced_depth(config: dict[str, object]) -> str:
    advanced = Path(config["advanced"]).read_text(encoding="utf-8")
    _, sections = common.split_h2(advanced)
    retained = [
        fragment
        for title, fragment in sections
        if "PYQ" not in title.upper()
    ]
    return "\n\n".join(common.lower_headings(fragment) for fragment in retained)


def register_notes(config: dict[str, object]) -> str:
    facts = "\n".join(
        f"{number}. **{label}:** {statement}"
        for number, (label, statement) in enumerate(config["facts"], 1)
    )
    traps = "\n".join(f"- {trap}" for trap in config["traps"])
    return (
        "### COMPLETE CONSOLIDATED REGISTER NOTES\n\n"
        "#### Twenty must-know anchors\n\n"
        f"{facts}\n\n"
        "#### High-risk UPSC traps\n\n"
        f"{traps}\n\n"
        "#### Universal answer spine\n\n"
        "```text\n"
        "DEFINE SCOPE -> BUILD CHRONOLOGY -> GROUP EVIDENCE BY MECHANISM\n"
        "-> ADD A COUNTERPOINT / LIMIT -> LINK TO THE NEXT TOPIC -> GRADED VERDICT\n"
        "```\n\n"
        "#### Current-affairs boundary\n\n"
        f"{config['current_note']}\n\n"
        "#### Final revision rule\n\n"
        "Revise actor, institution, date, mechanism and limitation together. "
        "A correct isolated date without the correct causal category is not an exam-ready fact."
    )


def assemble(config: dict[str, object]) -> tuple[str, str, int]:
    sessions, pyq_blocks = extract_teaching_and_pyqs(config)
    mcqs = build_mcqs(config)
    practice = (
        solved_pyq_section(config, pyq_blocks)
        + "\n\n"
        + original_mains_section(config)
    )
    ascii_fragment = ascii_master.build_manual_fragment(
        ascii_master.normalize_manual_spec_file(ASCII_PATH)[str(config["key"])]
    )
    markdown = (
        f"# {config['title']} - Learner-v2 Complete Learning Session\n\n"
        + source_audit(config)
        + "\n\n## BASIC LEARNING SESSION\n\n"
        + "\n\n".join(sessions)
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
        + "\n\n## OPTIONAL ADVANCED DEPTH \u2014 NOT REQUIRED FOR A CORE ANSWER\n\n"
        + advanced_depth(config)
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + "### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\n\n"
        + ascii_fragment
        + "\n\n"
        + register_notes(config)
        + "\n"
    )
    workbook = (
        f"# {config['title']} - Solved Practice Workbook\n\n"
        "> Uses the same 80-question rotated bank and the same PYQ ownership rules "
        "as the complete learner-v2 session.\n\n"
        "## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
        + "\n"
    )
    return markdown, workbook, len(sessions)


def write_ascii_spec() -> None:
    topics = []
    for config in TOPICS:
        key = str(config["key"])
        panels = []
        for title, structural_type, body, references in PANEL_DATA[key]:
            if max(map(len, body.splitlines())) > 100:
                raise ValueError(f"{key}: ASCII line exceeds 100 characters.")
            panels.append(
                {
                    "title": title,
                    "structural_type": structural_type,
                    "ascii_lines": body.splitlines(),
                    "source_references": references,
                }
            )
        topics.append(
            {
                "topic_key": key,
                "display_title": config["title"],
                "source_markdown": str(Path(config["canonical"]).relative_to(ROOT)),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Modern Indian History learner-v2 Topics 09-13",
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


def write_graphical_spec(config: dict[str, object], markdown: str) -> Path:
    key = str(config["key"])
    panels = [
        {
            "title": title,
            "body": body,
            "structural_type": kind,
            "source_references": references,
        }
        for title, kind, body, references in PANEL_DATA[key]
    ]
    source_path = SESSION_DIR / f"{key}_Learning-Session.md"
    spec = carvaka_flowchart.author_topic_spec(
        topic_key=key,
        subject=SUBJECT,
        title=str(config["title"]),
        source_markdown=markdown,
        source_markdown_path=str(source_path.relative_to(ROOT)),
        ascii_spec_path=str(ASCII_PATH.relative_to(ROOT)),
        ascii_spec_sha256=hashlib.sha256(ASCII_PATH.read_bytes()).hexdigest(),
        panels=panels,
        source_generation=1,
    )
    if len(spec["stages"]) != 13:
        raise ValueError(f"{key}: graphical master must contain 13 stages.")
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
        item
        for item in catalog["topics"]
        if item.get("topic_key") == "modern-indian-history-09"
    )
    manifest = section_indexes.materialize_catalog_section_manifest(
        ROOT, catalog, target
    )
    if manifest != SECTION_MANIFEST:
        raise ValueError(f"Unexpected section manifest path: {manifest}")
    return manifest


def write_generation_spec(
    config: dict[str, object],
    source_path: Path,
    workbook_path: Path,
    graphical_path: Path,
) -> Path:
    sources = [
        Path(config["basic"]),
        Path(config["advanced"]),
        Path(config["canonical"]),
        *[Path(path) for path in config["extra"]],
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
    sources = list(dict.fromkeys(sources))
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_topic = next(
        item
        for item in catalog["topics"]
        if item.get("topic_key") == config["key"]
    )
    payload = {
        "schema_version": 1,
        "topic_key": config["key"],
        "subject": SUBJECT,
        "section": "Subject-Wide-Syllabus",
        "topic_folder": config["key"],
        "title": config["title"],
        "variant": "learner-v2",
        "generation": 1,
        "generation_date": DATE,
        "command": catalog_topic["learner_v2_command"],
        "source_markdown": str(source_path.relative_to(ROOT)),
        "workbook_markdown": str(workbook_path.relative_to(ROOT)),
        "source_basic": str(Path(config["basic"]).relative_to(ROOT)),
        "source_canonical": str(Path(config["canonical"]).relative_to(ROOT)),
        "source_advanced": str(Path(config["advanced"]).relative_to(ROOT)),
        "manifest": str(SECTION_MANIFEST.relative_to(ROOT)),
        "cross_topic_sources": [
            str(path.relative_to(ROOT))
            for path in [*COMMON_CROSS, *[Path(value) for value in config["extra"]]]
        ],
        "local_ocr_sources": [
            str(path.relative_to(ROOT)) for path in LOCAL_BOOKS
        ],
        "pyq_indexes": [str(path.relative_to(ROOT)) for path in PYQ_INDEXES],
        "official_question_sources": [
            str(path.relative_to(ROOT)) for path in OFFICIAL_QUESTION_SOURCES
        ],
        "live_sources": config["live_sources"],
        "source_files": [str(path.relative_to(ROOT)) for path in sources],
        "practice_profile": (
            "80 unique MCQ stems with substantive explanations and strict A-B-C-D "
            "rotation; routed PYQ demand cards; original solved 10, 15 and 20-mark "
            "Mains practice; final consolidated register notes."
        ),
        "pyq_status_note": config["pyq_note"],
        "current_linkage_note": config["current_note"],
        "mcq_answer_policy": "strict-abcd-cycle",
        "ascii_panel_count": 12,
        "graphical_stage_count": 13,
        "tracker_untouched": True,
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{config['key']}-new-topic-{DATE}.json"
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def self_check(
    config: dict[str, object],
    markdown: str,
    workbook: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    key = str(config["key"])
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    required = [
        "BASIC LEARNING SESSION",
        "BASIC MCQS / REMEDIATION",
        "PYQS AND ANSWER PRACTICE",
        "OPTIONAL ADVANCED DEPTH \u2014 NOT REQUIRED FOR A CORE ANSWER",
        "CONSOLIDATED REGISTER NOTES",
    ]
    if [item for item in headings if item in required] != required:
        raise ValueError(f"{key}: learner-v2 section order failed.")
    if headings[-1] != "CONSOLIDATED REGISTER NOTES":
        raise ValueError(f"{key}: register notes must be the last H2.")
    sessions = re.findall(
        r"(?m)^### SESSION (\d+) \u2014 (.+?) \u2014 (.+?)\s*$",
        markdown,
    )
    if len(sessions) != session_count or session_count < 16:
        raise ValueError(f"{key}: session count failed ({session_count}).")
    if markdown.count("#### VISUAL FIRST") != session_count:
        raise ValueError(f"{key}: every session must contain a visual.")
    common.mcq_audit(markdown, key)
    common.mcq_audit(workbook, key)
    if markdown.count("```ascii-master") != 12:
        raise ValueError(f"{key}: embedded ASCII panel count failed.")
    graphical = json.loads(graphical_path.read_text(encoding="utf-8"))
    if len(graphical["stages"]) != 13:
        raise ValueError(f"{key}: graphical stage count failed.")
    missing = [
        term
        for term in config["required_terms"]
        if term.casefold() not in markdown.casefold()
    ]
    if missing:
        raise ValueError(f"{key}: required concepts missing: {missing}")
    if Path(config["canonical"]).read_text(encoding="utf-8") != markdown:
        raise ValueError(f"{key}: reusable canonical Markdown diverged.")


def main() -> int:
    write_ascii_spec()
    write_section_manifest()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    for config in TOPICS:
        markdown, workbook, session_count = assemble(config)
        key = str(config["key"])
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        workbook_path = SESSION_DIR / f"{key}_Solved-Workbook.md"
        source_path.write_text(markdown, encoding="utf-8")
        workbook_path.write_text(workbook, encoding="utf-8")
        Path(config["canonical"]).write_text(markdown, encoding="utf-8")
        graphical_path = write_graphical_spec(config, markdown)
        write_generation_spec(config, source_path, workbook_path, graphical_path)
        self_check(
            config,
            markdown,
            workbook,
            session_count,
            graphical_path,
        )
        print(
            f"{key}: sessions={session_count}; mcqs=80 (A20/B20/C20/D20); "
            "ascii=12; graphical=13; generation=1"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
