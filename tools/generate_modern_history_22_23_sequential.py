"""Build Modern Indian History learner-v2 Topics 22-23.

This authoring-only generator writes complete reusable Markdown, solved
workbooks, manual ASCII and graphical specifications, and tracker-free
generation-one manifests. It deliberately does not render PDFs, update the
tracker, regenerate indexes, finalize generations, or publish packages.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base
import generate_modern_history_20_21_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-31"
SUBJECT = "Modern-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "modern-indian-history-22-23-2026-08-31-sequential.json"
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
LOCAL_BOOKS = list(base.LOCAL_BOOKS)
COMMON_CROSS = list(base.COMMON_CROSS)
PYQ_INDEXES = list(base.PYQ_INDEXES)
OFFICIAL_QUESTION_SOURCES = list(
    dict.fromkeys(
        [
            *base.OFFICIAL_QUESTION_SOURCES,
            ROOT / "knowledge-export" / "Prelims PYQ" / "2025-GS1-Set A.md",
            ROOT
            / "books"
            / "prelima_question_paper_answers"
            / "Ans-2025-GS1.pdf",
            ROOT / "knowledge-export" / "Prelims PYQ" / "2026-GS1-Set A.md",
            ROOT
            / "knowledge-export"
            / "Prelims PYQ"
            / "Ans-2026-GS1-Provisional.md",
            ROOT
            / "knowledge-export"
            / "Prelims PYQ"
            / "CSP_2020_GS_Paper-1.pdf.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "QP-CSM19-GeneralStudies-I.pdf.md",
            ROOT / "knowledge-export" / "Mains PYQ" / "Gen_St_P1.pdf.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "QP-CSM-23-GENERAL-STUDIES-PAPER-I-180923.pdf.md",
        ]
    )
)
OFFICIAL_QUESTION_SOURCES = [
    path for path in OFFICIAL_QUESTION_SOURCES if path.is_file()
]


TOPICS = [
    base.topic(
        22,
        "Simon Commission, Nehru Report, Civil Disobedience & Round Table "
        "Conferences (1927\u20131934)",
        "22_Simon-Nehru-Report-CDM-and-RTC.md",
        "22_Simon-Nehru-Report-CDM-and-RTC.md",
        "22_Simon-Commission-Nehru-Report-Civil-Disobedience-"
        "Round-Table-Conferences_Complete-Topic-Package.md",
        [
            "basic/20_Non-Cooperation-and-Khilafat-Movement.md",
            "basic/21_Swarajists-and-Revolutionaries-1920s.md",
            "basic/24_Government-of-India-Act-1935-and-Congress-Ministries.md",
            "advanced/20_Non-Cooperation-and-Khilafat-Movement.md",
        ],
        [
            "https://aspirant.academy/en/current-affairs/"
            "046d2fba-ef0f-53ac-96ca-fede9b88f790",
            "https://cbcindia.gov.in/outreachactivities/"
            "the-national-salt-satyagraha-memorial-dandi-gujarat/",
        ],
        "The 12 March 2026 date was the 96th calendar anniversary of the "
        "Dandi March's departure. The anniversary is used only as a restrained "
        "public-memory bridge. The Central Bureau of Communication page on the "
        "National Salt Satyagraha Memorial at Dandi supplies official static "
        "memorial context; no claim is made that a Prime Minister, Vice-President "
        "or minister issued an independently verified 2026 tribute.",
        "The Basic and Advanced owners were reconciled with the repository OCR "
        "of Bipan Chandra's Modern India and India's Struggle for Independence. "
        "The route is stated as about 385/388 km; historical sources that render "
        "it as 240 miles are explicitly identified as a source variation. The "
        "local Bipan Chandra OCR's 147-seat Poona Pact figure is not silently "
        "preferred over the widespread 148 convention.",
        "The exact 2025 Prelims GS-I Q74 stem is taken from "
        "`knowledge-export/Prelims PYQ/2025-GS1-Set A.md`; its official Series-A "
        "answer A (Poona Pact) is independently confirmed from "
        "`books/prelima_question_paper_answers/Ans-2025-GS1.pdf`. The exact 2020 "
        "Gandhi-Irwin Pact stem is retained from the local official-paper OCR, "
        "but no answer letter is invented because no local official key is held.",
        [
            (
                "Simon Commission appointment and composition",
                "The Simon Commission was appointed in 1927 as an all-British "
                "statutory commission with no Indian member.",
            ),
            (
                "Simon Commission arrival",
                "The Commission arrived on 3 February 1928 and met hartals, "
                "black flags and the slogan 'Simon Go Back'.",
            ),
            (
                "Lala Lajpat Rai chronology",
                "The Lahore lathi-charge occurred on 30 October 1928; Lala "
                "Lajpat Rai died on 17 November 1928.",
            ),
            (
                "Nehru Report design",
                "The 1928 Motilal Nehru committee proposed Dominion Status, "
                "responsible government, rights, joint electorates and qualified "
                "minority reservations rather than a simple end to safeguards.",
            ),
            (
                "Jinnah's Fourteen Points",
                "Jinnah's Fourteen Points followed in 1929 after the Nehru "
                "Report compromise failed to settle minority representation.",
            ),
            (
                "Calcutta ultimatum",
                "The Calcutta Congress of December 1928 gave Britain one year "
                "to concede Dominion Status before Congress moved to complete "
                "independence and civil disobedience.",
            ),
            (
                "Irwin Declaration and Delhi Manifesto",
                "Irwin's 31 October 1929 declaration described Dominion Status "
                "as the natural issue of constitutional progress; the Delhi "
                "Manifesto demanded an implementing, not merely debating, RTC.",
            ),
            (
                "Lahore and the pledge",
                "The Lahore Congress adopted Purna Swaraj in December 1929, "
                "followed by the Independence Pledge on 26 January 1930.",
            ),
            (
                "Dandi March chronology",
                "Gandhi left Sabarmati with 78 chosen followers on 12 March "
                "1930 and broke the salt law at Dandi on 6 April 1930.",
            ),
            (
                "Dandi distance caution",
                "The Dandi route is safest stated as about 385/388 km; some "
                "historical sources render it as 240 miles, so false exactness "
                "must be avoided.",
            ),
            (
                "Regional salt marches",
                "Rajagopalachari led the Vedaranyam march, Kelappan led the "
                "Payyannur march, and Andhra activists organised sibirams.",
            ),
            (
                "Frontier and army refusal",
                "Peshawar mobilisation centred on the Khudai Khidmatgars, while "
                "Garhwali soldiers refused to fire on demonstrators.",
            ),
            (
                "Dharasana and Sholapur",
                "Sarojini Naidu led the Dharasana phase after Gandhi's arrest, "
                "while Sholapur saw a severe temporary breakdown of authority.",
            ),
            (
                "Participation pattern",
                "Women entered picketing and salt-making prominently; Muslim "
                "participation was uneven, with the NWFP a major exception.",
            ),
            (
                "Round Table Conference sequence",
                "Congress was absent from the First RTC (November 1930-January "
                "1931); Gandhi was sole Congress representative at the Second; "
                "Congress was absent from the limited Third RTC.",
            ),
            (
                "Gandhi-Irwin Pact",
                "The 5 March 1931 Pact suspended CDM for RTC participation and "
                "secured bounded concessions on non-violent prisoners, unsold "
                "confiscated land, uncollected fines, salt and peaceful picketing, "
                "but no inquiry into police excesses.",
            ),
            (
                "Karachi Congress",
                "Karachi ratified the Pact and adopted Fundamental Rights and "
                "the National Economic Programme, defining social content for "
                "Swaraj.",
            ),
            (
                "Communal Award and fast",
                "The Communal Award extended separate electorates to the "
                "Depressed Classes; Gandhi's Yeravda fast began on 20 September "
                "1932.",
            ),
            (
                "Poona Pact settlement and number caution",
                "The Poona Pact of 24 September 1932 substituted reserved seats "
                "in joint electorates for separate electorates; the local Bipan "
                "Chandra OCR gives 147 provincial seats while 148 is the "
                "widespread convention, so the total is identified as disputed.",
            ),
            (
                "Resumption and withdrawal",
                "CDM resumed under intensive repression after the Second RTC "
                "and was withdrawn in early April 1934.",
            ),
        ],
        [
            "Nehru Report meant Dominion Status, not Purna Swaraj.",
            "Joint electorates did not mean the Nehru Report rejected every "
            "minority safeguard; it retained qualified reservations.",
            "First RTC: Congress absent; Second RTC: Gandhi sole Congress "
            "representative; Third RTC: Congress absent and limited in importance.",
            "Gandhi-Irwin was a tactical truce, not a transfer-of-power settlement.",
            "Communal Award and Poona Pact are distinct constitutional devices.",
            "Poona Pact representation must be assessed without flattening either "
            "Gandhi's integration argument or Ambedkar's independent-voice claim.",
            "Do not state the 147/148 provincial-seat total as uncontested.",
            "CDM was regionally diverse and socially uneven, not only the Dandi walk.",
        ],
        [
            (
                10,
                "Explain how the Simon Commission boycott radicalised the "
                "constitutional debate by 1929.",
                "Exclusion delegitimised reform from above, while the Nehru "
                "Report's unresolved minority bargain narrowed the space for "
                "Dominion compromise.",
                [0, 1, 2, 3, 4],
            ),
            (
                10,
                "Why was salt an unusually effective instrument of civil "
                "disobedience?",
                "Salt joined universality, a clear law-breaking act and low-cost "
                "participation to a moral attack on colonial monopoly.",
                [8, 9, 10, 13],
            ),
            (
                15,
                "Civil Disobedience was much wider than the Dandi March. Discuss.",
                "Dandi supplied the symbol, but regional marches, Frontier "
                "mobilisation, army refusal, Dharasana, Sholapur, women and "
                "varied rural action supplied the movement's national depth.",
                [8, 10, 11, 12, 13],
            ),
            (
                15,
                "Assess the Gandhi-Irwin Pact as a strategic settlement.",
                "The Pact recognised Congress as an indispensable negotiating "
                "force and secured bounded relief, but left coercive power, "
                "police accountability and independence untouched.",
                [14, 15, 16, 19],
            ),
            (
                20,
                "Trace the constitutional and mass-political sequence from the "
                "Simon Commission to the withdrawal of CDM.",
                "The period formed a single escalation cycle: exclusion, Indian "
                "constitution-making, Purna Swaraj, mass illegality, negotiation, "
                "representation conflict, repression and strategic withdrawal.",
                [0, 3, 4, 5, 6, 7, 8, 14, 15, 17, 18, 19],
            ),
            (
                20,
                "Critically examine the Gandhi-Ambedkar disagreement and the "
                "Poona Pact's representational compromise.",
                "A balanced answer must hold together Gandhi's fear of permanent "
                "social separation, Ambedkar's demand for autonomous political "
                "voice, the coercive fast context and the Pact's joint-electorate "
                "reservation design.",
                [17, 18],
            ),
        ],
        [
            (
                "2025",
                "Prelims GS-I Q74",
                "Subsequent to which one of the following events, Gandhiji, who "
                "consistently opposed untouchability and appealed for its "
                "eradication from all spheres, decided to include the upliftment "
                "of 'Harijans' in his political and social programme? "
                "(2025-GS1-Set A.md)",
                "official-key-confirmed",
                "The official Series-A answer is **A - The Poona Pact**, verified "
                "directly from `Ans-2025-GS1.pdf`. The package links the answer "
                "to the post-Communal-Award fast, Pact and Harijan-work sequence.",
            ),
            (
                "2020",
                "Prelims GS-I Q27",
                "The Gandhi-Irwin Pact included which of the following? "
                "1. Invitation to Congress to participate in the Round Table "
                "Conference; 2. Withdrawal of Ordinances promulgated in "
                "connection with the Civil Disobedience Movement; 3. Acceptance "
                "of Gandhiji's suggestion for enquiry into police excesses; "
                "4. Release of only those prisoners who were not charged with "
                "violence. (CSP_2020_GS_Paper-1.pdf.md)",
                "official-stem-key-unavailable",
                "Statements 1, 2 and 4 are retained by the source-backed Pact "
                "balance; statement 3 is excluded because the inquiry demand was "
                "refused. No answer letter is asserted without a held official key.",
            ),
        ],
        [
            "3 February 1928",
            "30 October 1928",
            "17 November 1928",
            "Dominion Status",
            "qualified minority reservations",
            "Delhi Manifesto",
            "Purna Swaraj",
            "78 chosen followers",
            "385/388 km",
            "Vedaranyam",
            "Payyannur",
            "sibirams",
            "Khudai Khidmatgars",
            "Garhwali",
            "Dharasana",
            "Sarojini Naidu",
            "Gandhi-Irwin Pact",
            "Fundamental Rights",
            "20 September 1932",
            "24 September 1932",
            "147",
            "148",
            "early April 1934",
            "96th calendar anniversary",
            "National Salt Satyagraha Memorial",
        ],
    ),
    base.topic(
        23,
        "Left, Peasant, Workers' & States' Peoples' Movements (1930s)",
        "23_Left-Peasant-Workers-and-States-Peoples-Movements.md",
        "23_Left-Peasant-Workers-and-States-Peoples-Movements.md",
        "23_Left-Peasant-Workers-States-Peoples-Movements-1930s_"
        "Complete-Topic-Package.md",
        [
            "basic/20_Non-Cooperation-and-Khilafat-Movement.md",
            "basic/22_Simon-Nehru-Report-CDM-and-RTC.md",
            "basic/24_Government-of-India-Act-1935-and-Congress-Ministries.md",
            "basic/28_Integration-of-Princely-States.md",
        ],
        [
            "https://www.thehindu.com/news/national/"
            "farm-workers-unions-activists-announce-protest-from-july-1-"
            "for-vb-g-ram-g-repeal/article71113860.ece",
        ],
        "The Hindu report on farm-worker organisations announcing an "
        "indefinite countrywide protest from 1 July 2026 over rural-employment "
        "policy is used only as an organisational-lineage and labour-rights "
        "bridge. Contemporary policy claims are kept separate from the history "
        "of the 1930s; no unrelated secondary strike claim is used.",
        "The Basic and Advanced owners were reconciled with the repository OCR "
        "of India's Struggle for Independence. Tashkent 1920 is identified as "
        "the international/emigre communist formation and Kanpur 1925 as the "
        "all-India organisation formed inside India. The AISPC first convention "
        "is fixed to December 1927, with the source spelling G.R. Abhayankar.",
        "Exact local official-paper wording is retained for the 2019, 2020 and "
        "2023 GS-I questions. The 2020 Ulgulan objective stem is retained from "
        "the local official-paper OCR without an answer letter because no local "
        "official key is held. The 2026 Forward Bloc stem is explicitly "
        "provisional and receives no answer letter.",
        [
            (
                "AITUC foundation",
                "The All India Trade Union Congress was founded in 1920, with "
                "Lala Lajpat Rai as its first president.",
            ),
            (
                "Communist formation chronology",
                "Tashkent 1920 marks an international/emigre communist formation, "
                "while Kanpur 1925 marks the all-India organisation formed inside "
                "India; both dates require qualification.",
            ),
            (
                "Workers' and Peasants' Parties",
                "Workers' and Peasants' Parties linked labour, communist and "
                "Congress-left activity before the intensified repression of 1929.",
            ),
            (
                "Meerut Conspiracy Case",
                "The Meerut Conspiracy Case ran from 1929 to 1933 against "
                "communist and trade-union activists; the package avoids an "
                "unreconciled precise accused count.",
            ),
            (
                "Bihar Provincial Kisan Sabha",
                "Swami Sahajanand Saraswati founded the Bihar Provincial Kisan "
                "Sabha in 1929.",
            ),
            (
                "Karachi social programme",
                "Karachi 1931 joined civil liberties to labour protection and a "
                "National Economic Programme.",
            ),
            (
                "Congress Socialist Party",
                "The CSP formed within Congress at Bombay in October 1934 under "
                "J.P. Narayan, Acharya Narendra Dev, Ram Manohar Lohia and Minoo "
                "Masani; it was not identical with the CPI.",
            ),
            (
                "All-India Kisan Congress",
                "The All-India Kisan Congress, later AIKS, met at Lucknow in "
                "April 1936 with Sahajanand Saraswati as president and N.G. Ranga "
                "as general secretary.",
            ),
            (
                "Faizpur agrarian programme",
                "The December 1936 Faizpur setting connected the Kisan Manifesto "
                "to rent-revenue reduction, debt relief, tenure, labour and "
                "peasant-union demands.",
            ),
            (
                "Congress Ministries' limits",
                "Congress ministries of 1937-39 passed reforms but structural and "
                "franchise limits left sub-tenants and agricultural labourers "
                "especially weakly protected.",
            ),
            (
                "National Planning Committee",
                "The National Planning Committee of 1938 extended the Karachi-"
                "Faizpur chain from rights and agrarian demands toward planned "
                "economic transformation.",
            ),
            (
                "AISPC founding",
                "The first AISPC convention met in December 1927; Balwantrai "
                "Mehta, Maniklal Kothari and G.R. Abhayankar were central to it.",
            ),
            (
                "Praja Mandal target",
                "Praja Mandals and States' Peoples' Movements opposed princely "
                "autocracy and denial of rights, not British provincial ministries.",
            ),
            (
                "1938-39 princely-state awakening",
                "The 1938-39 awakening included Rajkot and other princely-state "
                "struggles and pushed Congress from restraint toward closer "
                "identification without making later integration inevitable.",
            ),
            (
                "Haripura-Tripuri-Forward Bloc",
                "Bose's Haripura presidency in 1938, Tripuri re-election and "
                "institutional crisis in 1939, resignation and Forward Bloc "
                "formation in 1939 form one sequence.",
            ),
            (
                "Congress remained broad",
                "Left influence changed nationalism's social content and "
                "commitments, but Congress remained a broad, multi-class coalition "
                "rather than becoming communist.",
            ),
            (
                "Birsa genealogy",
                "Birsa Munda's Ulgulan belongs to 1899-1900 and supplies a "
                "genealogy of tribal anti-colonial politics, not a 1930s event.",
            ),
            (
                "Roots before the 1930s",
                "Eka, Bardoli, AITUC, early communist organisation and AISPC are "
                "roots that explain the 1930s, not events to be redated into it.",
            ),
            (
                "Late-colonial consequences",
                "Warli (1945), Tebhaga, Telangana and Punnapra-Vayalar (1946) are "
                "late-colonial consequences or bridges, not the central 1930s phase.",
            ),
            (
                "Organisational-lineage current bridge",
                "The reported 1 July 2026 farm-worker protest is used only to "
                "illustrate organisational lineage and labour-rights vocabulary, "
                "not as evidence about 1930s events.",
            ),
        ],
        [
            "AITUC is 1920; AIKS is 1936.",
            "CPI chronology needs both Tashkent 1920 and Kanpur 1925 qualified.",
            "CSP was formed within Congress and was not identical with CPI.",
            "AISPC's first convention was December 1927, not 1936.",
            "States' Peoples' Movements challenged princely autocracy.",
            "Tripuri was institutional and ideological, not merely personal.",
            "Birsa Ulgulan is 1899-1900 background; Warli, Tebhaga, Telangana and "
            "Punnapra-Vayalar are later bridges.",
            "Left influence widened Congress commitments without making Congress "
            "a communist party.",
        ],
        [
            (
                10,
                "Distinguish the organisational roles of AITUC, CSP and AIKS.",
                "The three bodies organised different constituencies and occupied "
                "different relations to Congress: labour federation, socialist "
                "current within Congress and all-India peasant platform.",
                [0, 6, 7],
            ),
            (
                10,
                "Why must CPI formation be explained through both 1920 and 1925?",
                "The two dates identify different sites and organisational "
                "moments: international/emigre formation at Tashkent and an "
                "all-India organisation inside India at Kanpur.",
                [1, 2, 3],
            ),
            (
                15,
                "Explain how peasant organisation changed the Congress's social "
                "programme during the 1930s.",
                "Provincial kisan organisation, AIKS and the Kisan Manifesto "
                "pressed agrarian demands into Faizpur, while ministry outcomes "
                "revealed class and franchise limits.",
                [4, 5, 7, 8, 9],
            ),
            (
                15,
                "Assess States' Peoples' Movements as a democratic extension of "
                "Indian nationalism.",
                "AISPC and Praja Mandals carried rights claims into princely India, "
                "challenged autocracy and altered Congress policy, while later "
                "integration remained contingent rather than predetermined.",
                [11, 12, 13],
            ),
            (
                20,
                "The 1930s changed the social content of nationalism without "
                "turning Congress into a communist party. Discuss.",
                "Left, labour and peasant pressure institutionalised rights, "
                "agrarian reform and planning inside a broad anti-imperialist "
                "coalition whose class compromises remained visible.",
                [0, 1, 3, 5, 6, 7, 8, 9, 10, 15],
            ),
            (
                20,
                "Analyse the roots, core phase and late-colonial consequences of "
                "peasant, worker and states' peoples' mobilisation.",
                "Chronological discipline separates pre-1930 roots from the "
                "1930s organisational core and the radical 1945-46 bridge, while "
                "showing the mechanisms connecting them.",
                [17, 0, 2, 4, 7, 11, 13, 18],
            ),
        ],
        [
            (
                "2019",
                "GS-I Q11",
                "Many voices had strengthened and enriched the nationalist "
                "movement during the Gandhian phase. Elaborate. (Answer in 250 "
                "words) [QP-CSM19-GeneralStudies-I.pdf.md]",
                "official-wording-bounded-model",
                "Organise the answer by Gandhian mass politics, socialist and "
                "communist currents, peasants, workers, women, tribals and "
                "princely-state subjects; explain enrichment without erasing "
                "autonomous agendas or Congress's coalition limits.",
            ),
            (
                "2020",
                "GS-I Q13",
                "Since the decade of the 1920s, the national movement acquired "
                "various ideological strands and thereby expanded its social "
                "base. Discuss. (Answer in 250 words) [Gen_St_P1.pdf.md]",
                "official-wording-bounded-model",
                "Use communist, socialist, revolutionary, peasant, labour and "
                "states' peoples' strands, then show their institutional effect "
                "on Karachi, Faizpur and planning while retaining a graded verdict.",
            ),
            (
                "2023",
                "GS-I Q13",
                "How did the colonial rule affect the tribals in India and what "
                "was the tribal response to the colonial oppression? (Answer in "
                "250 words) [QP-CSM-23-GENERAL-STUDIES-PAPER-I-180923.pdf.md]",
                "official-wording-cross-topic-model",
                "This topic uses Birsa's Ulgulan only as genealogy. A full answer "
                "must range across land alienation, forest restrictions, forced "
                "labour, dikus, cultural intrusion and regionally varied tribal "
                "responses rather than forcing them into the 1930s.",
            ),
            (
                "2020",
                "Prelims GS-I Q35",
                "With reference to the history of India, 'Ulgulan' or the Great "
                "Tumult is the description of which of the following events? "
                "(CSP_2020_GS_Paper-1.pdf.md)",
                "official-stem-key-unavailable",
                "The source-backed identification is Birsa Munda's revolt of "
                "1899-1900, but no answer letter is asserted because a local "
                "official 2020 key is unavailable.",
            ),
            (
                "2026",
                "Prelims GS-I Q16",
                "Which of the following factors contributed to the formation of "
                "the Forward Bloc by Subhas Chandra Bose in 1939? "
                "(2026-GS1-Set A.md)",
                "provisional-key-no-answer-letter",
                "Use the stem only to revise the Tripuri institutional alignment. "
                "The held 2026 key is provisional, so this package records no "
                "answer letter and makes no independent key inference.",
            ),
        ],
        [
            "Lala Lajpat Rai",
            "Tashkent 1920",
            "Kanpur 1925",
            "Workers' and Peasants' Parties",
            "Meerut Conspiracy Case",
            "Bombay in October 1934",
            "J.P. Narayan",
            "Acharya Narendra Dev",
            "Ram Manohar Lohia",
            "Minoo Masani",
            "Bihar Provincial Kisan Sabha",
            "Lucknow in April 1936",
            "Sahajanand Saraswati",
            "N.G. Ranga",
            "Kisan Manifesto",
            "Faizpur",
            "National Planning Committee",
            "sub-tenants",
            "agricultural labourers",
            "December 1927",
            "G.R. Abhayankar",
            "Praja Mandals",
            "princely autocracy",
            "Rajkot",
            "Haripura",
            "Tripuri",
            "Forward Bloc",
            "multi-class coalition",
            "Ulgulan",
            "1899-1900",
            "Warli (1945)",
            "Tebhaga",
            "Telangana",
            "Punnapra-Vayalar",
            "1 July 2026",
        ],
    ),
]


SESSION_VISUALS: dict[str, str] = {}
SESSION_DEFINITIONS: dict[str, str] = {}


def authored_session(
    title: str,
    core: str,
    evidence: list[str],
    caution: str,
    exam_use: str,
    visual: str,
    definition: str,
) -> tuple[str, str, list[str], str, str]:
    """Register one fully authored session without permitting fallback prose."""

    if title in SESSION_VISUALS or title in SESSION_DEFINITIONS:
        raise ValueError(f"Duplicate authored session title: {title}")
    SESSION_VISUALS[title] = visual
    SESSION_DEFINITIONS[title] = definition
    return title, core, evidence, caution, exam_use


SESSION_PLANS: dict[str, list[tuple[str, str, list[str], str, str]]] = {
    "modern-indian-history-22": [
        authored_session(
            "Simon Commission: exclusion becomes a mass issue",
            "The Simon Commission converted a scheduled constitutional review "
            "into a legitimacy crisis because Britain appointed an all-British "
            "body in 1927 to judge India's constitutional future.",
            [
                "The commission had no Indian member.",
                "Its arrival on 3 February 1928 met hartals, black flags and "
                "'Simon Go Back' demonstrations.",
                "The boycott crossed important party boundaries even though "
                "Indian political opinion was not perfectly uniform.",
                "Exclusion linked constitutional criticism to street mobilisation.",
            ],
            "Keep appointment in 1927 distinct from arrival on 3 February 1928.",
            "Open a constitutional-deadlock answer with exclusion as the mechanism "
            "that joined elite and mass protest.",
            """1927 -> all-British statutory commission appointed
NO INDIAN MEMBER -> constitutional review loses representative legitimacy
3 FEB 1928 -> arrival meets hartals + black flags + "Simon Go Back"
POLITICAL EFFECT -> constitutional protest becomes a national mass issue""",
            "The Simon crisis was a legitimacy crisis created when an imperial "
            "government excluded Indians from the statutory review of India's "
            "own constitutional system.",
        ),
        authored_session(
            "Lala Lajpat Rai: exact protest chronology and political afterlife",
            "The Lahore protest became a martyrdom narrative only through a "
            "precise two-date sequence: the lathi-charge on 30 October 1928 and "
            "Lala Lajpat Rai's death on 17 November 1928.",
            [
                "Rai led an anti-Simon demonstration at Lahore.",
                "Police used lathis on 30 October 1928.",
                "Rai died on 17 November 1928 after the injuries.",
                "Revolutionary retaliation against Saunders belongs to the "
                "subsequent HSRA chain, not to the Simon Commission itself.",
            ],
            "Do not collapse injury and death into one date or call Saunders a "
            "member of the Commission.",
            "Use the two-date chain as evidence for the interaction between mass "
            "protest and revolutionary politics.",
            """30 OCT 1928 -> Lahore anti-Simon protest -> police lathi-charge
17 NOV 1928 -> Lala Lajpat Rai dies
POLITICAL AFTERLIFE -> HSRA plans retaliation
DEC 1928 -> Saunders killed; a connected consequence, not the same event""",
            "The Lajpat Rai chronology is a causal bridge from anti-Simon mass "
            "protest to HSRA retaliation, while preserving distinct actors and dates.",
        ),
        authored_session(
            "Nehru Report: an Indian constitutional design",
            "The Nehru Report was not simply an anti-Simon protest document; it "
            "was an Indian attempt to design responsible government under "
            "Dominion Status while balancing rights and minority representation.",
            [
                "Motilal Nehru chaired the All-Parties committee.",
                "The report proposed responsible government and enforceable rights.",
                "It preferred joint electorates but retained qualified minority "
                "reservations where minorities required protection.",
                "Its Dominion framework separated it from Lahore's later Purna "
                "Swaraj position.",
            ],
            "Do not equate joint electorates with abolition of every minority safeguard.",
            "Assess the Report as both a constitution-making milestone and a failed "
            "inter-communal bargain.",
            """NEHRU REPORT (1928)
|-- status -> Dominion Status
|-- government -> responsible executive
|-- rights -> constitutional guarantees
`-- representation -> joint electorates + qualified minority reservations
LIMIT -> neither complete independence nor a settled communal compromise""",
            "The Nehru Report was an Indian constitutional draft combining "
            "Dominion Status, responsible government, rights and a qualified "
            "joint-electorate minority formula.",
        ),
        authored_session(
            "Minority deadlock and Jinnah's Fourteen Points",
            "Jinnah's Fourteen Points of 1929 emerged after proposed amendments "
            "failed to reconcile Muslim representation demands with the Nehru "
            "Report's constitutional structure.",
            [
                "The disagreement concerned representation at the Centre and in "
                "Punjab and Bengal, residuary powers and separate electorates.",
                "The Fourteen Points followed the 1928 report; they did not precede it.",
                "The Hindu Mahasabha and other interests also constrained compromise.",
                "The deadlock exposed competing constitutional securities inside "
                "the anti-colonial field.",
            ],
            "Do not narrate the deadlock as a two-person disagreement detached "
            "from institutional and provincial interests.",
            "Use the episode to show why anti-imperial agreement did not automatically "
            "produce agreement on the future polity.",
            """NEHRU REPORT FORMULA
       ↓ contested on representation + residuary powers
JINNAH'S CALCUTTA AMENDMENTS -> rejected
       ↓
FOURTEEN POINTS (1929)
RESULT -> anti-colonial unity does not settle minority constitutional security""",
            "The minority deadlock was a conflict over the institutional location "
            "of security, representation and federal power in a future Indian state.",
        ),
        authored_session(
            "Calcutta ultimatum, Irwin Declaration and Delhi Manifesto",
            "Between December 1928 and December 1929, Congress moved from a "
            "one-year Dominion ultimatum to rejecting vague imperial assurances "
            "that did not commit an RTC to implement Dominion Status.",
            [
                "Calcutta Congress gave Britain one year from December 1928.",
                "Irwin's 31 October 1929 declaration called Dominion Status the "
                "natural issue of constitutional progress.",
                "The Delhi Manifesto asked that the RTC implement rather than "
                "merely debate the objective.",
                "Failure to secure assurance cleared the path to Lahore.",
            ],
            "Do not omit the one-year ultimatum or treat Irwin's wording as an "
            "immediate grant of Dominion Status.",
            "This is the causal bridge required between the Nehru Report and Purna Swaraj.",
            """DEC 1928 CALCUTTA -> one-year Dominion ultimatum
31 OCT 1929 IRWIN -> Dominion as "natural issue"; RTC promised
DELHI MANIFESTO -> RTC must implement, not merely discuss
NO BINDING ASSURANCE -> Dominion middle ground collapses
DEC 1929 -> Lahore adopts Purna Swaraj""",
            "The 1928-29 ultimatum sequence tested whether imperial language would "
            "be converted into a binding transfer programme and found it insufficient.",
        ),
        authored_session(
            "Lahore Congress, Purna Swaraj and the 26 January pledge",
            "The Lahore Congress transformed complete independence from a radical "
            "pressure into the Congress goal, then converted it into a public "
            "pledge observed on 26 January 1930.",
            [
                "Jawaharlal Nehru presided at Lahore in December 1929.",
                "Congress adopted Purna Swaraj, not Dominion Status.",
                "The tricolour was hoisted on the banks of the Ravi.",
                "26 January 1930 was observed as nationalist Independence Day.",
            ],
            "Keep the December 1929 resolution, 26 January pledge and March 1930 "
            "movement launch as three distinct steps.",
            "Use Lahore as the ideological hinge between constitutional deadlock "
            "and civil disobedience.",
            """DEC 1929 LAHORE -> PURNA SWARAJ ADOPTED
        ↓ public translation
26 JAN 1930 -> INDEPENDENCE PLEDGE
        ↓ strategic translation
12 MAR 1930 -> DANDI MARCH BEGINS
RULE -> goal, pledge and campaign are related but separately dated""",
            "Purna Swaraj was the Congress goal adopted at Lahore and publicly "
            "ritualised through the 26 January pledge before civil disobedience began.",
        ),
        authored_session(
            "Why salt: universality, legality and participation",
            "Salt supplied a rare combination of universal consumption, visible "
            "colonial monopoly, simple law-breaking and participation open to "
            "people excluded from elite constitutional politics.",
            [
                "The tax and monopoly touched rich and poor consumers.",
                "Making or collecting salt created a clear civil breach without "
                "requiring weapons or specialised organisation.",
                "The issue enabled women and local groups to enter action through "
                "manufacture, sale, picketing and boycott.",
                "Its economic scale was less important than its legal and moral symbolism.",
            ],
            "Do not claim salt manufacture alone threatened the colonial economy.",
            "Explain symbol choice through mechanism rather than describing it as "
            "Gandhi's intuition.",
            """UNIVERSAL NECESSITY + COLONIAL MONOPOLY
                ↓
SIMPLE, VISIBLE AND REPEATABLE BREACH OF LAW
                ↓
LOW ENTRY BARRIER FOR REGIONS, CLASSES AND WOMEN
                ↓
MORAL LEGIBILITY + MASS POLITICAL PARTICIPATION""",
            "The salt strategy converted an everyday necessity into a repeatable "
            "act of law-breaking whose moral visibility exceeded its direct economic effect.",
        ),
        authored_session(
            "Dandi March: dates, followers and distance discipline",
            "The march ran from 12 March to 6 April 1930: Gandhi began with 78 "
            "chosen followers and broke the salt law at Dandi after a route best "
            "stated as about 385/388 km.",
            [
                "The starting point was Sabarmati Ashram.",
                "The initial group numbered 78 chosen followers; crowds grew en route.",
                "The salt law was broken on 6 April 1930.",
                "Some historical sources state 240 miles; the package flags that "
                "variation instead of presenting competing conversions as exact.",
            ],
            "Do not turn the initial 78 into the total number who accompanied the "
            "march at every stage.",
            "A Prelims answer must preserve dates, initial party and route wording together.",
            """12 MAR 1930 -> SABARMATI -> Gandhi + 78 chosen followers
ROUTE -> about 385/388 km; some historical sources state 240 miles
VILLAGE STAGES -> speeches + recruitment + public discipline
6 APR 1930 -> DANDI -> salt law broken -> national signal""",
            "The Dandi March was a staged mobilisation from Sabarmati to Dandi, "
            "with a fixed initial cadre, expanding public participation and a "
            "deliberately visible terminal breach.",
        ),
        authored_session(
            "Regional spread: coast, Andhra, forests and local repertoires",
            "Civil Disobedience became national because regions translated the "
            "salt signal into locally workable marches, camps, boycotts, revenue "
            "resistance and forest-law defiance.",
            [
                "Rajagopalachari led the Vedaranyam march in Tamil country.",
                "Kelappan led the Payyannur march in Malabar.",
                "Andhra organisers used sibirams as disciplined mobilisation camps.",
                "Inland regions adapted civil disobedience to revenue and forest restrictions.",
            ],
            "Do not describe every regional action as a literal repetition of Dandi.",
            "Use regional adaptation to prove that national scale depended on local repertoires.",
            """DANDI SIGNAL
|-- Vedaranyam -> Rajagopalachari
|-- Payyannur -> Kelappan
|-- Andhra -> sibirams / mobilisation camps
|-- inland agrarian zones -> revenue resistance
`-- forest regions -> forest-law defiance
NATIONAL MOVEMENT = COMMON LEGITIMACY + REGIONAL REPERTOIRES""",
            "Regionalisation was the process by which a common civil-disobedience "
            "principle was translated into locally relevant forms of colonial law-breaking.",
        ),
        authored_session(
            "Peshawar, Khudai Khidmatgars and Garhwali refusal",
            "The Frontier theatre demonstrated organisational depth and strain "
            "inside the coercive apparatus: Khudai Khidmatgar mobilisation "
            "sustained Peshawar protest while Garhwali soldiers refused to fire.",
            [
                "Khan Abdul Ghaffar Khan's prior organising made non-violent "
                "Frontier mobilisation possible.",
                "The Khudai Khidmatgars connected national civil disobedience to "
                "local agrarian and political grievances.",
                "Peshawar demonstrations followed arrests in April 1930.",
                "The Garhwali refusal mattered because the army was a core colonial instrument.",
            ],
            "Do not explain Frontier participation through stereotypes about "
            "religion or martial character.",
            "Use organisation, grievance and army refusal as evidence of movement depth.",
            """PRIOR MASS WORK -> KHAN ABDUL GHAFFAR KHAN
        ↓
KHUDAI KHIDMATGARS -> disciplined non-violent organisation
        ↓
APRIL 1930 PESHAWAR MASS MOBILISATION
        ↓
GARHWALI SOLDIERS REFUSE TO FIRE -> coercive apparatus strained""",
            "The Frontier case shows that national calls became durable where "
            "prior local organisation connected them to local grievances and discipline.",
        ),
        authored_session(
            "Dharasana, Sholapur, women and uneven participation",
            "Dharasana made non-violent suffering internationally visible, "
            "Sholapur revealed how quickly authority could fracture, and women's "
            "participation widened the repertoire even as Muslim participation "
            "remained uneven outside the Frontier.",
            [
                "Sarojini Naidu led the Dharasana phase after Gandhi's arrest.",
                "Publicised lathi violence at Dharasana strengthened moral pressure.",
                "Sholapur workers and crowds produced a temporary breakdown of authority.",
                "Women joined salt-making and picketing; participation varied by "
                "region and community.",
            ],
            "Do not use one region's participation pattern as a national average.",
            "A social-base answer needs both expansion and unevenness.",
            """DHARASANA -> Sarojini Naidu -> disciplined suffering -> global publicity
SHOLAPUR -> worker-crowd action -> temporary authority breakdown
WOMEN -> salt-making + picketing + boycott visibility
MUSLIM PARTICIPATION -> uneven; NWFP is a major exception
VERDICT -> wide movement, differentiated social geography""",
            "The movement's social geography combined visible widening with "
            "uneven regional and community participation rather than uniform mobilisation.",
        ),
        authored_session(
            "First RTC and the Gandhi-Irwin Pact balance",
            "The failure of a First RTC without Congress created the setting for "
            "the 5 March 1931 Pact, a tactical exchange of movement suspension "
            "and RTC participation for bounded administrative concessions.",
            [
                "Congress was absent from the First RTC, November 1930-January 1931.",
                "The Pact covered non-violent political prisoners, uncollected "
                "fines and unsold confiscated land.",
                "It permitted bounded coastal salt-making and peaceful picketing.",
                "The government refused an inquiry into police excesses.",
            ],
            "Do not add independence, universal prisoner release or police inquiry "
            "to the government's concessions.",
            "Evaluate the Pact by listing what each side gave and what remained withheld.",
            """FIRST RTC WITHOUT CONGRESS -> legitimacy and implementation gap
5 MAR 1931 PACT
CONGRESS GIVES -> suspends CDM + attends Second RTC
GOVERNMENT GIVES -> bounded release/restoration/salt/picketing concessions
REFUSAL -> no police-excess inquiry; no independence settlement""",
            "The Gandhi-Irwin Pact was a tactical truce exchanging Congress's "
            "movement leverage for bounded relief and entry into negotiation.",
        ),
        authored_session(
            "Karachi, Second RTC and renewed repression",
            "Karachi gave the truce social content through Fundamental Rights and "
            "a National Economic Programme, but the Second RTC deadlocked and "
            "Congress returned to a movement environment transformed by repression.",
            [
                "Karachi ratified the Pact in March 1931.",
                "Its rights and economic resolutions described what Swaraj should "
                "mean for citizens, workers and peasants.",
                "Gandhi attended the Second RTC as sole Congress representative.",
                "After deadlock, CDM resumed under ordinances, arrests and broad repression.",
            ],
            "Do not reduce Karachi to Pact ratification or claim the Second RTC "
            "granted Congress's constitutional demand.",
            "Connect political negotiation to the social definition of Swaraj and "
            "then to renewed coercion.",
            """MARCH 1931 KARACHI
|-- ratifies Gandhi-Irwin Pact
`-- Fundamental Rights + National Economic Programme
SECOND RTC -> Gandhi sole Congress representative -> deadlock
RETURN -> arrests + ordinances + renewed repression
CDM RESUMES -> weaker organisational room, sharper coercion""",
            "Karachi connected a tactical political truce to a substantive social "
            "vision of Swaraj before imperial deadlock reopened confrontation.",
        ),
        authored_session(
            "Communal Award, Gandhi-Ambedkar debate and Poona Pact",
            "The 1932 representation crisis opposed two serious political fears: "
            "Gandhi feared separate electorates would harden untouchability into "
            "permanent social separation, while Ambedkar feared joint electorates "
            "would deny Depressed Classes an independent political voice.",
            [
                "The Communal Award extended separate electorates to Depressed Classes.",
                "Gandhi's Yeravda fast began on 20 September 1932.",
                "The Poona Pact was concluded on 24 September 1932.",
                "It substituted reserved seats in joint electorates; the fast "
                "created a coercive bargaining context that a balanced answer must name.",
            ],
            "Do not describe the settlement as full agreement or flatten either "
            "side into bad faith.",
            "Build the answer as representation problem, rival safeguards, coercive "
            "context, institutional compromise and unresolved legacy.",
            """COMMUNAL AWARD -> separate electorates for Depressed Classes
GANDHI -> fears permanent social separation
AMBEDKAR -> seeks independent political voice
20 SEP 1932 -> Gandhi's fast begins in Yeravda
24 SEP 1932 -> POONA PACT
DESIGN -> reserved seats in joint electorates; disagreement persists""",
            "The Gandhi-Ambedkar debate concerned which electoral institution "
            "could secure dignity and representation without reproducing social domination.",
        ),
        authored_session(
            "Poona seat-number caution, Third RTC and CDM withdrawal",
            "The end phase requires evidentiary restraint: Poona's provincial "
            "seat total varies between the local OCR's 147 and the widespread "
            "148 convention, the Third RTC had limited importance without "
            "Congress, and CDM ended under repression in early April 1934.",
            [
                "The package identifies the 147/148 variation rather than silently "
                "choosing one total.",
                "Congress was absent from the Third RTC.",
                "The Third RTC was largely formal and should not be overstated.",
                "CDM's withdrawal in early April 1934 followed a repressed and "
                "declining resumed phase, not an immediate post-Pact ending.",
            ],
            "Do not state a disputed seat total as uncontested or make the Third "
            "RTC the decisive constitutional settlement.",
            "End a period answer with a qualified verdict on transformed political "
            "consciousness despite limited immediate concession.",
            """POONA PACT NUMBER -> local OCR 147 | widespread convention 148
RULE -> attribute the variation; do not present false certainty
THIRD RTC -> Congress absent -> limited/formal significance
1932-34 -> resumed CDM under repression
EARLY APRIL 1934 -> withdrawal
VERDICT -> no immediate freedom, durable legitimacy shift""",
            "The end-phase verdict separates disputed quantitative detail, weak "
            "constitutional conferencing and the strategic closure of a repressed movement.",
        ),
    ],
    "modern-indian-history-23": [
        authored_session(
            "Scope map: roots, 1930s core and late-colonial bridges",
            "Chronology is the organising discipline for this topic: pre-1930 "
            "organisations are roots, the 1930s are the core phase, and 1945-46 "
            "movements are consequences or late-colonial bridges.",
            [
                "AITUC, early communist organisation, Bardoli and AISPC precede the 1930s.",
                "CSP, AIKS, Faizpur, ministries, planning and Praja Mandal awakening "
                "form the core 1930s sequence.",
                "Warli, Tebhaga, Telangana and Punnapra-Vayalar belong to 1945-46.",
                "Birsa Ulgulan in 1899-1900 is a deeper tribal genealogy.",
            ],
            "Do not pull every agrarian or tribal movement into the 1930s.",
            "Begin broad answers with a roots-core-consequences periodisation.",
            """ROOTS -> AITUC 1920 | Tashkent 1920 | Kanpur 1925 | AISPC 1927
        | Bardoli 1928 | Bihar Kisan Sabha 1929
CORE -> CSP 1934 | AIKS + Faizpur 1936 | Ministries 1937-39 | NPC 1938
BRIDGES -> Warli 1945 | Tebhaga/Telangana/Punnapra-Vayalar 1946
GENEALOGY -> Birsa Ulgulan 1899-1900""",
            "The topic is a periodised study of how earlier organisations enabled "
            "the 1930s social turn and later movements radicalised its unresolved demands.",
        ),
        authored_session(
            "AITUC and the labour constituency",
            "AITUC made industrial labour visible as an organised all-India "
            "constituency from 1920, with Lala Lajpat Rai as first president, "
            "before the socialist consolidation of the 1930s.",
            [
                "AITUC was founded in 1920.",
                "Lala Lajpat Rai was its first president.",
                "Textile and railway action connected workplace demands to anti-imperial politics.",
                "Trade union strength remained concentrated in selected industrial centres.",
            ],
            "Do not confuse AITUC's 1920 labour role with AIKS's 1936 peasant role.",
            "Use AITUC to show that social-base expansion began before the CSP and AIKS.",
            """1920 -> AITUC FOUNDED
FIRST PRESIDENT -> LALA LAJPAT RAI
BASE -> industrial workers; especially organised urban centres
METHOD -> unions + strikes + political representation
LIMIT -> geographically concentrated, not the whole Indian workforce""",
            "AITUC was an all-India trade-union platform that organised industrial "
            "labour as a distinct political constituency within anti-colonial India.",
        ),
        authored_session(
            "Communist chronology: Tashkent, Kanpur and WPP",
            "Communist formation cannot be compressed into one unexplained date: "
            "Tashkent 1920 identifies an international/emigre initiative, Kanpur "
            "1925 an all-India organisation inside India, and Workers' and "
            "Peasants' Parties a later open political form.",
            [
                "M.N. Roy is associated with the Tashkent formation.",
                "Kanpur 1925 marks organisation within India.",
                "Workers' and Peasants' Parties linked labour and peasant work to "
                "Congress-left activity.",
                "These currents were not identical to the later CSP.",
            ],
            "Never write only 'CPI founded in 1925' without qualifying the 1920 history.",
            "A strong answer distinguishes location, organisational form and political arena.",
            """TASHKENT 1920 -> international/emigre communist formation
KANPUR 1925 -> all-India organisation formed inside India
WPP -> open workers-peasants political activity in the late 1920s
CSP 1934 -> separate socialist current within Congress
RULE -> related left histories, not one interchangeable organisation""",
            "The two-date CPI chronology distinguishes an international founding "
            "initiative from the later all-India organisational formation inside India.",
        ),
        authored_session(
            "Meerut Conspiracy Case: repression and publicity",
            "The Meerut Conspiracy Case of 1929-33 sought to disable communist "
            "and trade-union networks, yet its extended public trial also exposed "
            "a wider audience to socialist and labour politics.",
            [
                "The case began with arrests in 1929 and lasted to 1933.",
                "It targeted communist and trade-union organisers.",
                "The package avoids a precise accused count because held sources "
                "and summaries require reconciliation.",
                "Repression could weaken organisations while publicising their ideas.",
            ],
            "Do not turn an unreconciled accused count into a memorised fact.",
            "Use Meerut as a repression-publicity paradox rather than a bare case name.",
            """COLONIAL AIM -> disable communist + trade-union organisation
1929 ARRESTS -> prolonged MEERUT TRIAL -> 1933
DIRECT EFFECT -> leadership disruption + imprisonment
PARADOXICAL EFFECT -> national publicity for labour and socialist arguments
EVIDENCE RULE -> avoid unreconciled precise accused counts""",
            "Meerut was a colonial conspiracy prosecution whose political effect "
            "combined organisational repression with unintended ideological publicity.",
        ),
        authored_session(
            "Congress Socialist Party inside Congress",
            "The CSP formed at Bombay in October 1934 to radicalise the national "
            "movement from within Congress, not to create an organisation identical "
            "with the CPI.",
            [
                "Key leaders included J.P. Narayan and Acharya Narendra Dev.",
                "Ram Manohar Lohia and Minoo Masani were also central.",
                "Members agreed that the anti-imperialist national struggle remained primary.",
                "The inside-Congress choice preserved coalition breadth but constrained class autonomy.",
            ],
            "CSP and CPI had interactions, but they were not the same organisation.",
            "Use organisational location to explain both CSP influence and its limits.",
            """BOMBAY, OCTOBER 1934 -> CSP FORMED WITHIN CONGRESS
LEADERS -> J.P. Narayan | Narendra Dev | Lohia | Minoo Masani
STRATEGY -> radicalise the national platform from inside
GAIN -> access to Congress mass legitimacy
LIMIT -> socialist programme operates within a broad multi-class coalition""",
            "The CSP was an organised socialist current inside Congress that "
            "combined commitment to national unity with pressure for social transformation.",
        ),
        authored_session(
            "Bihar Kisan Sabha to AIKS: leadership and Kisan Manifesto",
            "The Bihar Provincial Kisan Sabha, founded by Swami Sahajanand "
            "Saraswati in 1929, supplied a provincial base for the All-India "
            "Kisan Congress at Lucknow in April 1936, with Sahajanand as president "
            "and N.G. Ranga as general secretary.",
            [
                "The Bihar founding year was 1929, not 1936.",
                "Sahajanand linked tenancy, rent, illegal levies, zamindari and "
                "later Bakasht questions.",
                "The organisation later used the name All India Kisan Sabha.",
                "Its founding meeting coincided with the Congress's Lucknow setting.",
                "The Kisan Manifesto carried demands into the Congress arena.",
                "Leadership linked Bihar mobilisation to Ranga's Andhra agrarian work.",
            ],
            "Do not call AIKS the beginning of organised peasant politics or swap "
            "Sahajanand's presidency and Ranga's secretaryship.",
            "Use the provincial-to-national ladder and retain place, month, year "
            "and offices together.",
            """1929 -> BIHAR PROVINCIAL KISAN SABHA -> SAHAJANAND
APRIL 1936 -> LUCKNOW -> ALL-INDIA KISAN CONGRESS
PRESIDENT -> SAHAJANAND SARASWATI
GENERAL SECRETARY -> N.G. RANGA
PROGRAMME -> KISAN MANIFESTO
EFFECT -> provincial peasant organisations gain an all-India coordinating platform""",
            "The provincial-to-national kisan ladder connected Sahajanand's 1929 "
            "Bihar organisation to the 1936 all-India coordinating platform.",
        ),
        authored_session(
            "Faizpur and the agrarian programme",
            "Faizpur in December 1936 translated organised peasant pressure into "
            "a Congress agrarian programme addressing rent and revenue, debt, "
            "feudal dues, tenure, labour and union rights.",
            [
                "The second all-India kisan session met alongside the Congress setting.",
                "The programme included substantial rent-revenue reduction and debt relief.",
                "It demanded abolition of feudal dues and greater security of tenure.",
                "Agricultural labour and peasant unions entered the programme explicitly.",
            ],
            "Do not reduce Faizpur to venue symbolism; retain its programme content.",
            "Use Faizpur as institutional proof that class demands changed Congress commitments.",
            """KISAN MANIFESTO
        ↓ enters Congress debate
FAIZPUR, DECEMBER 1936
|-- reduce rent/revenue
|-- debt relief + end feudal dues
|-- security of tenure
`-- living wage + peasant-union recognition
RESULT -> agrarian question becomes a national programme""",
            "The Faizpur agrarian programme was the Congress-level translation "
            "of organised peasant demands into commitments on rents, debt, tenure and labour.",
        ),
        authored_session(
            "Karachi-Faizpur-planning social-content chain",
            "Karachi 1931, Faizpur 1936 and the National Planning Committee in "
            "1938 form a chain through which civil rights, labour protection, "
            "agrarian reform and planning entered Congress commitments.",
            [
                "Karachi linked political liberties to an economic programme.",
                "Faizpur specified agrarian demands.",
                "The National Planning Committee extended social content into "
                "planned development.",
                "Left influence was larger ideologically than its organisational numbers.",
            ],
            "Do not conclude from this chain that a communist organisation "
            "captured Congress.",
            "This three-stage chain is the strongest evidence for agenda transformation.",
            """KARACHI 1931 -> RIGHTS + LABOUR + NATIONAL ECONOMIC PROGRAMME
        ↓
FAIZPUR 1936 -> AGRARIAN PROGRAMME
        ↓
NATIONAL PLANNING COMMITTEE 1938 -> PLANNED TRANSFORMATION
VERDICT -> social content widens; Congress remains broad and multi-class""",
            "The social-content chain is the staged institutional adoption of "
            "rights, agrarian reform and planning within a broad nationalist coalition.",
        ),
        authored_session(
            "Congress Ministries: achievements and structural limits",
            "The Congress ministries of 1937-39 made reform possible but also "
            "exposed the limits imposed by provincial powers, landlord interests, "
            "restricted franchise and uneven mobilisation.",
            [
                "Tenancy and labour measures varied across provinces.",
                "Sub-tenants of occupancy tenants were often outside effective protection.",
                "Agricultural labourers had limited organisation and voting power.",
                "Office demonstrated the gap between programme and implementable coalition policy.",
            ],
            "Do not judge the ministries as either complete betrayal or complete fulfilment.",
            "Use named excluded groups to convert a general limitation into evidence.",
            """1937-39 CONGRESS MINISTRIES
PROMISE -> Karachi + Faizpur social commitments
ACTION -> provincial tenancy/labour reforms, uneven by region
GAPS -> sub-tenants + agricultural labourers
STRUCTURAL LIMITS -> restricted franchise + landlord weight + limited powers
VERDICT -> partial reform exposes coalition constraints""",
            "The ministry gap was the distance between a radicalising programme "
            "and provincial implementation constrained by law, franchise and coalition interests.",
        ),
        authored_session(
            "AISPC origins and the princely-state political field",
            "The first AISPC convention in December 1927 coordinated political "
            "workers from princely states, where the immediate target was princely "
            "autocracy and denial of rights rather than British provincial ministries.",
            [
                "Balwantrai Mehta, Maniklal Kothari and G.R. Abhayankar were central.",
                "Praja Mandals had already emerged in several states.",
                "Paramountcy insulated princes while imperial power structured the wider system.",
                "The Congress initially urged state peoples to rely on their own strength.",
            ],
            "Ignore the OCR anomaly that moves the first AISPC convention to 1936.",
            "Define the distinct political field before discussing Congress intervention.",
            """PRINCELY STATE SYSTEM -> autocracy under imperial paramountcy
LOCAL RESPONSE -> PRAJA MANDALS / STATES' PEOPLE'S CONFERENCES
DECEMBER 1927 -> FIRST AISPC CONVENTION
ORGANISERS -> Balwantrai Mehta | Maniklal Kothari | G.R. Abhayankar
TARGET -> responsible government and rights inside princely states""",
            "AISPC was the coordinating platform for democratic movements inside "
            "princely India, a political field distinct from British provincial government.",
        ),
        authored_session(
            "Praja Mandals, Rajkot and changing Congress policy",
            "The 1938-39 awakening and Rajkot struggle pushed Congress from a "
            "policy of organisational restraint toward closer identification with "
            "states' peoples, without making 1947 integration automatic.",
            [
                "Praja Mandals expanded across several princely states in 1938-39.",
                "Rajkot drew Patel, Kasturba Gandhi and Gandhi into a direct test.",
                "Haripura in 1938 reiterated caution even as pressure for involvement grew.",
                "The movements created democratic cadre and legitimacy relevant to "
                "later integration, but did not predetermine accession outcomes.",
            ],
            "Do not call these movements campaigns against elected British Indian ministries.",
            "Use Rajkot to explain a policy transition rather than a sudden total reversal.",
            """1938 HARIPURA -> Congress still stresses restraint
1938-39 -> PRAJA MANDAL AWAKENING ACROSS STATES
RAJKOT -> direct intervention tests the old boundary
POLICY SHIFT -> closer Congress identification with states' peoples
LATER RELEVANCE -> democratic base for integration, not deterministic inevitability""",
            "The Rajkot transition was a shift from cautious sympathy to closer "
            "national identification as princely-state mobilisation acquired mass force.",
        ),
        authored_session(
            "Haripura, Tripuri and the Forward Bloc",
            "The Bose sequence was an institutional and ideological crisis over "
            "presidential authority, Working Committee control, planning and "
            "anti-imperialist strategy on the eve of war, not merely a personality clash.",
            [
                "Bose was Congress president at Haripura in 1938.",
                "He won re-election at Tripuri in 1939 against Gandhian opposition.",
                "The Working Committee conflict made formal electoral victory "
                "insufficient for organisational control.",
                "Bose resigned and formed the Forward Bloc in 1939.",
            ],
            "Do not place Forward Bloc before Tripuri or treat the crisis as only personal.",
            "Use the sequence to analyse the Congress constitution and strategic disagreement.",
            """HARIPURA 1938 -> BOSE PRESIDENCY + PLANNING EMPHASIS
TRIPURI 1939 -> re-election against Gandhian preference
INSTITUTIONAL QUESTION -> president versus Working Committee authority
STRATEGIC QUESTION -> timing and form of anti-imperialist confrontation
RESIGNATION -> FORWARD BLOC, 1939""",
            "The Tripuri crisis tested whether an elected Congress president could "
            "govern without the confidence of the Working Committee and Gandhian core.",
        ),
        authored_session(
            "Birsa Ulgulan as genealogy, not 1930s chronology",
            "Birsa Munda's Ulgulan of 1899-1900 belongs to the genealogy of tribal "
            "anti-colonial politics: land alienation, dikus and colonial power "
            "combined with a religious-political idiom.",
            [
                "Ulgulan means the Great Tumult in the official 2020 stem.",
                "The movement occurred in Chota Nagpur in 1899-1900.",
                "Its targets included exploitative intermediaries and British rule.",
                "It must not be redated into the 1930s merely because the PYQ is "
                "routed to a social-movements owner.",
            ],
            "Do not invent a 2020 answer letter without a held official key.",
            "Use Birsa as genealogy and route a full tribal answer beyond this topic.",
            """LAND ALIENATION + DIKUS + COLONIAL RULE
        ↓
BIRSA'S RELIGIOUS-POLITICAL MOBILISATION
        ↓
ULGULAN, 1899-1900, CHOTA NAGPUR
        ↓
ANTI-RAJ HORIZON
BOUNDARY -> genealogy for Topic 23, not a 1930s event""",
            "Ulgulan was Birsa Munda's 1899-1900 tribal revolt linking local land "
            "and outsider grievances to an explicitly anti-colonial political horizon.",
        ),
        authored_session(
            "Late-colonial agrarian bridges after the 1930s",
            "Warli, Tebhaga, Telangana and Punnapra-Vayalar show how unresolved "
            "questions of labour, sharecropping, landlord power and princely rule "
            "radicalised in 1945-46, but they are consequences rather than the "
            "topic's core decade.",
            [
                "Warli belongs to 1945.",
                "Tebhaga in 1946 demanded two-thirds of produce for Bengal sharecroppers.",
                "Telangana from 1946 opposed landlord oppression under Hyderabad's Nizam.",
                "Punnapra-Vayalar occurred in Travancore in 1946.",
            ],
            "Do not use these later struggles to erase the organisational work of the 1930s.",
            "Close the chronology by showing radicalisation without collapsing periods.",
            """1930s ORGANISATION -> unresolved land, labour and autocracy questions
1945 -> WARLI labour/forced-labour bridge
1946 -> TEBHAGA sharecroppers demand two-thirds
1946 -> TELANGANA anti-landlord struggle under Hyderabad
1946 -> PUNNAPRA-VAYALAR in Travancore
RULE -> consequences/bridges, not the central 1930s phase""",
            "The late-colonial bridge is the post-1930s radicalisation of agrarian "
            "and labour conflicts through class organisation and weakening state authority.",
        ),
        authored_session(
            "Synthesis: social transformation within a broad coalition",
            "The Left's decisive achievement was to change the social content and "
            "commitments of nationalism through organisations and pressure from "
            "below; its decisive limit was that Congress remained broad, multi-class "
            "and committed to coalition unity.",
            [
                "Labour organisation made workers a named political constituency.",
                "Kisan organisation moved agrarian demands into Congress programmes.",
                "States' peoples widened the territorial meaning of nationalism.",
                "CSP, Bose and planning changed debate without establishing a single "
                "left command over Congress.",
            ],
            "Do not equate ideological influence with communist capture.",
            "End with a graded verdict that links widened commitments to implementation limits.",
            """PRESSURE FROM BELOW
|-- workers -> AITUC + trade unions
|-- peasants -> provincial sabhas + AIKS
|-- princely-state subjects -> Praja Mandals + AISPC
`-- socialist-left -> CSP + Bose + planning
CONGRESS RESPONSE -> wider social programme
LIMIT -> broad multi-class coalition, uneven implementation""",
            "Agenda transformation means that organised social constituencies "
            "altered Congress commitments even though no single left organisation "
            "captured the nationalist coalition.",
        ),
    ],
}


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-22": [
        (
            "Simon exclusion and boycott",
            "causal-flow",
            """1927 -> all-British Simon Commission appointed; no Indian member
3 FEB 1928 -> arrival -> hartals + black flags + "Simon Go Back"
POLITICAL RESPONSE -> boycott converts constitutional exclusion into mass protest
EFFECT -> constitutional exclusion becomes a national legitimacy crisis.""",
            ["Simon Commission: exclusion becomes a mass issue"],
        ),
        (
            "Lajpat Rai exact chronology",
            "timeline",
            """30 OCT 1928 -> Lahore lathi-charge during anti-Simon protest
17 NOV 1928 -> Lala Lajpat Rai dies
POLITICAL AFTERLIFE -> the death intensifies anti-colonial anger
DEC 1928 -> Saunders retaliation belongs to the later HSRA chain.""",
            ["Lala Lajpat Rai: exact protest chronology and political afterlife"],
        ),
        (
            "Nehru Report constitutional matrix",
            "comparison",
            """STATUS -> Dominion Status, not complete independence
GOVERNMENT -> responsible executive | RIGHTS -> constitutional guarantees
ELECTION -> joint electorates + qualified minority reservations
LIMIT -> constitution-making milestone; communal settlement incomplete.""",
            ["Nehru Report: an Indian constitutional design"],
        ),
        (
            "From Calcutta to Lahore",
            "timeline",
            """DEC 1928 -> Calcutta gives a one-year Dominion ultimatum
31 OCT 1929 -> Irwin Declaration | Delhi Manifesto seeks implementation
DEC 1929 -> Lahore adopts Purna Swaraj
26 JAN 1930 -> Independence Pledge.""",
            ["Calcutta ultimatum, Irwin Declaration and Delhi Manifesto"],
        ),
        (
            "Dandi march exact-data rail",
            "timeline",
            """12 MAR 1930 -> Sabarmati -> Gandhi + 78 chosen followers
ROUTE -> about 385/388 km; some historical sources state 240 miles
6 APR 1930 -> Dandi -> salt law broken
RULE -> initial party is not the total crowd throughout the march.""",
            ["Dandi March: dates, followers and distance discipline"],
        ),
        (
            "Regional civil-disobedience map",
            "institution-map",
            """VEDARANYAM -> Rajagopalachari | PAYYANNUR -> Kelappan
ANDHRA -> sibirams | PESHAWAR -> Khudai Khidmatgars
GARHWALI -> refusal to fire | DHARASANA -> Sarojini Naidu
SHOLAPUR -> temporary breakdown of authority.""",
            ["Regional spread: coast, Andhra, forests and local repertoires"],
        ),
        (
            "Participation and variation",
            "balance-sheet",
            """WOMEN -> salt-making + picketing + boycott visibility
MUSLIM PARTICIPATION -> uneven; NWFP is the major exception
REGIONAL FORMS -> salt + revenue + forest + worker action
VERDICT -> wide movement, not uniform social geography.""",
            ["Dharasana, Sholapur, women and uneven participation"],
        ),
        (
            "Gandhi-Irwin concession balance",
            "comparison",
            """CONGRESS -> suspends CDM + agrees to Second RTC
GOVERNMENT -> bounded release, restoration, salt and picketing concessions
REFUSED -> inquiry into police excesses
5 MAR 1931 -> tactical truce, not independence.""",
            ["First RTC and the Gandhi-Irwin Pact balance"],
        ),
        (
            "Round Table Conference sequence",
            "timeline",
            """FIRST RTC, NOV 1930-JAN 1931 -> Congress absent
SECOND RTC, 1931 -> Gandhi sole Congress representative -> deadlock
THIRD RTC, 1932 -> Congress absent; limited/formal importance
RESULT -> conferencing cannot replace political leverage.""",
            ["Karachi, Second RTC and renewed repression"],
        ),
        (
            "Karachi social-content bridge",
            "concept-map",
            """KARACHI, MARCH 1931
|-- ratifies Gandhi-Irwin Pact
|-- Fundamental Rights
`-- National Economic Programme
USE -> shows what Swaraj should mean socially and economically.""",
            ["Karachi, Second RTC and renewed repression"],
        ),
        (
            "Communal Award to Poona Pact",
            "replacement-diagram",
            """COMMUNAL AWARD -> separate electorates for Depressed Classes
20 SEP 1932 -> Gandhi's fast begins
24 SEP 1932 -> Poona Pact
REPLACEMENT -> reserved seats in joint electorates
DEBATE -> integration versus independent political voice; coercive context.""",
            ["Communal Award, Gandhi-Ambedkar debate and Poona Pact"],
        ),
        (
            "Disputed number and movement closure",
            "accountability-map",
            """POONA PROVINCIAL SEATS -> local OCR 147 | widespread convention 148
RULE -> attribute variation; never present the total as uncontested
1932-34 -> CDM resumes under repression
EARLY APRIL 1934 -> movement withdrawn.""",
            ["Poona seat-number caution, Third RTC and CDM withdrawal"],
        ),
    ],
    "modern-indian-history-23": [
        (
            "Roots-core-bridges chronology",
            "timeline",
            """ROOTS -> AITUC 1920 | Kanpur 1925 | AISPC 1927 | Bihar Sabha 1929
CORE -> CSP 1934 | AIKS/Faizpur 1936 | Ministries 1937-39 | NPC 1938
BRIDGES -> Warli 1945 | Tebhaga/Telangana/Punnapra-Vayalar 1946
GENEALOGY -> Birsa Ulgulan 1899-1900.""",
            ["Scope map: roots, 1930s core and late-colonial bridges"],
        ),
        (
            "AITUC versus AIKS",
            "comparison",
            """AITUC -> 1920 -> industrial labour -> Lala Lajpat Rai first president
AIKS -> 1936 -> peasant coordination -> Sahajanand + N.G. Ranga
COMMON -> organised social constituencies enter nationalist politics
TRAP -> never swap dates, bases or offices.""",
            ["AITUC and the labour constituency"],
        ),
        (
            "Two-date communist chronology",
            "timeline",
            """TASHKENT 1920 -> international/emigre communist formation
KANPUR 1925 -> all-India organisation formed inside India
WPP -> open workers-peasants activity
CSP 1934 -> distinct socialist current within Congress.""",
            ["Communist chronology: Tashkent, Kanpur and WPP"],
        ),
        (
            "Meerut repression-publicity paradox",
            "causal-flow",
            """1929 -> arrests target communist and trade-union networks
1929-33 -> prolonged Meerut Conspiracy Case
DIRECT -> disruption + imprisonment
PARADOX -> socialist and labour arguments gain national publicity
RULE -> avoid unreconciled accused counts.""",
            ["Meerut Conspiracy Case: repression and publicity"],
        ),
        (
            "CSP inside-Congress map",
            "institution-map",
            """BOMBAY, OCTOBER 1934 -> CSP formed within Congress
LEADERS -> J.P. Narayan | Narendra Dev | Lohia | Minoo Masani
METHOD -> radicalise Congress from inside
TRAP -> CSP and CPI are not identical.""",
            ["Congress Socialist Party inside Congress"],
        ),
        (
            "Kisan organisation ladder",
            "timeline",
            """1929 -> Bihar Provincial Kisan Sabha -> Sahajanand Saraswati
APRIL 1936 -> All-India Kisan Congress at Lucknow
OFFICES -> Sahajanand president | N.G. Ranga general secretary
PROGRAMME -> Kisan Manifesto -> Faizpur agrarian demands.""",
            ["Bihar Kisan Sabha to AIKS: leadership and Kisan Manifesto"],
        ),
        (
            "Karachi-Faizpur-planning chain",
            "causal-flow",
            """KARACHI 1931 -> rights + labour + economic programme
FAIZPUR 1936 -> rent, debt, tenure and agricultural-labour demands
NPC 1938 -> planned economic transformation
VERDICT -> social content widens; Congress remains multi-class.""",
            ["Karachi-Faizpur-planning social-content chain"],
        ),
        (
            "Congress ministry gap",
            "balance-sheet",
            """ACHIEVEMENT -> provincial tenancy and labour reforms
GAP -> sub-tenants and agricultural labourers remain weakly protected
LIMITS -> restricted franchise + landlord weight + provincial powers
VERDICT -> partial implementation, neither fulfilment nor simple betrayal.""",
            ["Congress Ministries: achievements and structural limits"],
        ),
        (
            "AISPC and Praja Mandal field",
            "institution-map",
            """DECEMBER 1927 -> first AISPC convention
ORGANISERS -> Balwantrai Mehta | Maniklal Kothari | G.R. Abhayankar
UNITS -> Praja Mandals in princely states
TARGET -> princely autocracy and denial of rights, not British ministries.""",
            ["AISPC origins and the princely-state political field"],
        ),
        (
            "Rajkot policy transition",
            "process",
            """HARIPURA 1938 -> Congress reiterates restraint
1938-39 -> Praja Mandal awakening expands
RAJKOT -> old non-intervention boundary is directly tested
SHIFT -> closer identification
LIMIT -> later integration was enabled, not predetermined.""",
            ["Praja Mandals, Rajkot and changing Congress policy"],
        ),
        (
            "Bose institutional sequence",
            "timeline",
            """HARIPURA 1938 -> Bose president
TRIPURI 1939 -> re-elected against Gandhian preference
CRISIS -> presidency versus Working Committee authority + strategy
RESIGNATION -> Forward Bloc formed in 1939.""",
            ["Haripura, Tripuri and the Forward Bloc"],
        ),
        (
            "Genealogy and late bridges",
            "boundary-map",
            """1899-1900 -> Birsa Ulgulan: tribal anti-colonial genealogy
1945 -> Warli | 1946 -> Tebhaga, Telangana, Punnapra-Vayalar
CORE 1930s -> organisation, programme, ministries, princely-state awakening
RULE -> preserve chronology while explaining connection.""",
            ["Late-colonial agrarian bridges after the 1930s"],
        ),
    ],
}


TOPIC_CHRONOLOGY = {
    "modern-indian-history-22": [
        "appointed in 1927",
        "3 February 1928",
        "30 October 1928",
        "17 November 1928",
        "December 1928",
        "31 October 1929",
        "December 1929",
        "26 January 1930",
        "12 March 1930",
        "6 April 1930",
        "5 March 1931",
        "20 September 1932",
        "24 September 1932",
        "early April 1934",
    ],
    "modern-indian-history-23": [
        "AITUC 1920",
        "Kanpur 1925",
        "AISPC 1927",
        "Bihar Kisan Sabha 1929",
        "CSP 1934",
        "AIKS + Faizpur 1936",
        "Ministries 1937-39",
        "NPC 1938",
        "Warli 1945",
        "Tebhaga/Telangana/Punnapra-Vayalar 1946",
    ],
}

FORBIDDEN_TOPIC_PHRASES = {
    "modern-indian-history-22": [
        "Simon Commission included Indian",
        "Nehru Report demanded complete independence",
        "Gandhi attended the First RTC",
        "Poona Pact accepted separate electorates",
        "2026 minister tribute",
    ],
    "modern-indian-history-23": [
        "first AISPC convention in 1936",
        "CSP and CPI were identical",
        "Arabian Post",
        "Warli (1930",
        "Tebhaga (1930",
    ],
}


def session_visual(title: str, _terms: list[str]) -> str:
    """Render a manually authored, topic-specific teaching visual."""

    if title not in SESSION_VISUALS:
        raise ValueError(f"Missing topic-specific session visual: {title}")
    return (
        "#### VISUAL FIRST\n\n"
        "```text\n"
        f"{title.upper()}\n"
        f"{SESSION_VISUALS[title]}\n"
        "```\n\n"
        "*The visual fixes this subtopic's chronology, mechanism or boundary "
        "before the evidence.*"
    )


def session_definitions(
    title: str,
    topic_title: str,
    _terms: list[str],
) -> str:
    """Return an authored definition; generic fallbacks are forbidden."""

    if title not in SESSION_DEFINITIONS:
        raise ValueError(f"Missing authored definition: {title}")
    return (
        "#### CONCEPT DEFINITIONS\n\n"
        f"- **Precise definition:** {SESSION_DEFINITIONS[title]}\n"
        f"- **Topic boundary:** Apply this definition only within {topic_title}; "
        "retain the named actor, institution, date and chronological role."
    )


def phase_for(number: int) -> str:
    if number <= 3:
        return "FOUNDATION"
    if number >= 13:
        return "CORE SYNTHESIS"
    return "CORE"


def extract_teaching_and_pyqs(
    config: dict[str, object],
) -> tuple[list[str], list[str]]:
    """Use the authored route while retaining owner PYQ evidence."""

    sessions = []
    for number, (title, core, evidence, caution, exam_use) in enumerate(
        SESSION_PLANS[str(config["key"])], 1
    ):
        evidence_text = "\n".join(f"- {item}" for item in evidence)
        terms = base.session_terms(title, core + "\n" + evidence_text)
        fragment = (
            f"## {title}\n\n"
            + session_visual(title, terms)
            + "\n\n"
            + session_definitions(title, str(config["title"]), terms)
            + "\n\n#### CORE EXPLANATION\n\n"
            + core
            + "\n\n#### EVIDENCE AND MECHANISM\n\n"
            + evidence_text
            + "\n\n#### EXAMINER CAUTION\n\n- "
            + caution
            + "\n\n#### EXAM LINK\n\n"
            + f"- **Prelims:** {caution}\n"
            + f"- **Mains:** {exam_use}\n\n"
            + "#### MINI RECAP\n\n"
            + f"- **Core claim:** {core}\n"
            + f"- **Use:** {exam_use}"
        )
        sessions.append(
            base.common.session_fragment(fragment, number, phase_for(number))
        )

    pyq_blocks = []
    for owner in (Path(config["basic"]), Path(config["advanced"])):
        text = owner.read_text(encoding="utf-8")
        _, sections = base.common.split_h2(text)
        for title, fragment in sections:
            if "PYQ Integration" in title:
                pyq_blocks.append(base.common.lower_headings(fragment))
    return sessions, pyq_blocks


_BASE_OVERRIDES = {
    "DATE": DATE,
    "SUBJECT": SUBJECT,
    "KNOWLEDGE": KNOWLEDGE,
    "SESSION_DIR": SESSION_DIR,
    "ASCII_PATH": ASCII_PATH,
    "GRAPHICAL_DIR": GRAPHICAL_DIR,
    "EXPORT_DIR": EXPORT_DIR,
    "CATALOG": CATALOG,
    "SECTION_MANIFEST": SECTION_MANIFEST,
    "LOCAL_BOOKS": LOCAL_BOOKS,
    "COMMON_CROSS": COMMON_CROSS,
    "PYQ_INDEXES": PYQ_INDEXES,
    "OFFICIAL_QUESTION_SOURCES": OFFICIAL_QUESTION_SOURCES,
    "TOPICS": TOPICS,
    "PANEL_DATA": PANEL_DATA,
    "session_visual": session_visual,
    "session_definitions": session_definitions,
    "extract_teaching_and_pyqs": extract_teaching_and_pyqs,
}


@contextmanager
def configured_base() -> Iterator[None]:
    """Use shared generation helpers without leaking module-global overrides."""

    prior = {name: getattr(base, name) for name in _BASE_OVERRIDES}
    try:
        for name, value in _BASE_OVERRIDES.items():
            setattr(base, name, value)
        yield
    finally:
        for name, value in prior.items():
            setattr(base, name, value)


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
                "source_markdown": str(
                    Path(config["canonical"]).relative_to(ROOT)
                ),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Modern Indian History learner-v2 Topics 22-23",
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


def assemble(config: dict[str, object]) -> tuple[str, str, int]:
    with configured_base():
        return base.assemble(config)


def add_generation_one_metadata(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["supersedes"] = None
    payload["tracker_untouched"] = True
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def assert_topic_safeguards(config: dict[str, object], markdown: str) -> None:
    """Enforce chronology and high-risk factual boundaries for each topic."""

    key = str(config["key"])
    fact_text = "\n".join(statement for _, statement in config["facts"])
    chronology_text = (
        SESSION_VISUALS["Scope map: roots, 1930s core and late-colonial bridges"]
        if key == "modern-indian-history-23"
        else fact_text
    )
    cursor = -1
    for marker in TOPIC_CHRONOLOGY[key]:
        found = chronology_text.find(marker, cursor + 1)
        if found < 0:
            raise ValueError(f"{key}: chronology marker missing/out of order: {marker}")
        cursor = found
    for phrase in FORBIDDEN_TOPIC_PHRASES[key]:
        if phrase.casefold() in markdown.casefold():
            raise ValueError(f"{key}: forbidden factual formulation found: {phrase}")

    if key == "modern-indian-history-22":
        strict = [
            "Gandhi was sole Congress representative at the Second",
            "reserved seats in joint electorates",
            "local Bipan Chandra OCR gives 147",
            "148 is the widespread convention",
            "official Series-A answer is **A - The Poona Pact**",
            "no answer letter is asserted without a held official key",
            "96th calendar anniversary",
            "National Salt Satyagraha Memorial",
        ]
    else:
        strict = [
            "Tashkent 1920 identifies an international/emigre initiative",
            "Kanpur 1925 an all-India organisation inside India",
            "first AISPC convention in December 1927",
            "G.R. Abhayankar",
            "sub-tenants and agricultural labourers",
            "broad, multi-class",
            "The held 2026 key is provisional",
            "records no answer letter",
            "1 July 2026",
        ]
    missing = [phrase for phrase in strict if phrase.casefold() not in markdown.casefold()]
    if missing:
        raise ValueError(f"{key}: strict safeguard text missing: {missing}")


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
    if len(sessions) != session_count or session_count != 15:
        raise ValueError(f"{key}: expected exactly 15 sessions, got {session_count}.")
    if markdown.count("#### VISUAL FIRST") != 15:
        raise ValueError(f"{key}: every learner session must contain a visual.")
    if len(config["facts"]) != 20 or len(config["mains"]) != 6:
        raise ValueError(f"{key}: facts or original Mains contract failed.")
    if [item[0] for item in config["mains"]] != [10, 10, 15, 15, 20, 20]:
        raise ValueError(f"{key}: original Mains weighting failed.")
    if markdown.count("### ORIGINAL MAINS") != 6:
        raise ValueError(f"{key}: original Mains prompt count failed.")
    generic = [
        " is the part of ",
        " -> and -> ",
        "an evidence-led unit connecting",
        "Missing topic-specific session visual",
        "TODO",
        "PLACEHOLDER",
        "lorem ipsum",
    ]
    if any(phrase.casefold() in markdown.casefold() for phrase in generic):
        raise ValueError(f"{key}: generic or placeholder prose detected.")
    base.common.mcq_audit(markdown, key)
    base.common.mcq_audit(workbook, key)
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
    assert_topic_safeguards(config, markdown)
    if Path(config["canonical"]).read_text(encoding="utf-8") != markdown:
        raise ValueError(f"{key}: reusable canonical Markdown diverged.")


def validate_existing_section_contract() -> None:
    if not SECTION_MANIFEST.is_file():
        raise FileNotFoundError(f"Missing existing section manifest: {SECTION_MANIFEST}")
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_keys = {item.get("topic_key") for item in catalog["topics"]}
    missing = [config["key"] for config in TOPICS if config["key"] not in catalog_keys]
    if missing:
        raise ValueError(f"Topics missing from existing catalog: {missing}")


def main() -> int:
    validate_existing_section_contract()
    write_ascii_spec()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    with configured_base():
        for config in TOPICS:
            markdown, workbook, session_count = base.assemble(config)
            key = str(config["key"])
            source_path = SESSION_DIR / f"{key}_Learning-Session.md"
            workbook_path = SESSION_DIR / f"{key}_Solved-Workbook.md"
            source_path.write_text(markdown, encoding="utf-8")
            workbook_path.write_text(workbook, encoding="utf-8")
            Path(config["canonical"]).write_text(markdown, encoding="utf-8")
            graphical_path = base.write_graphical_spec(config, markdown)
            generation_path = base.write_generation_spec(
                config,
                source_path,
                workbook_path,
                graphical_path,
            )
            add_generation_one_metadata(generation_path)
            self_check(
                config,
                markdown,
                workbook,
                session_count,
                graphical_path,
            )
            print(
                f"{key}: sessions={session_count}; mcqs=80 "
                "(A20/B20/C20/D20); ascii=12; graphical=13; generation=1"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
