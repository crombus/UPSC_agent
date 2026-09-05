"""Build Modern Indian History learner-v2 Topics 14-15.

This authoring generator writes complete reusable Markdown, solved workbooks,
manual ASCII and graphical specifications, and tracker-free staging manifests.
It deliberately leaves PDF rendering, tracker finalization, and publication to
the shared refresh/export pipeline.
"""

from __future__ import annotations

import hashlib
import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base


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
    / "modern-indian-history-14-15-2026-08-31-sequential.json"
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
OFFICIAL_QUESTION_SOURCES = [
    *base.OFFICIAL_QUESTION_SOURCES,
    ROOT
    / "knowledge-export"
    / "Mains PYQ"
    / "QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md",
    ROOT / "books" / "more_previous_papers" / "QP-CSP-18-GS-I-C.pdf",
    ROOT / "_ocr_2019_gs1.txt",
    ROOT / "books" / "more_previous_papers" / "CSP_2020_GS_Paper-1.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP_CS_Pre_Exam_2023_280523.pdf",
]
OFFICIAL_QUESTION_SOURCES = [
    path for path in dict.fromkeys(OFFICIAL_QUESTION_SOURCES) if path.is_file()
]


TOPICS = [
    base.topic(
        14,
        "Foundation of the INC & the Moderate Phase (1885-1905)",
        "14_Foundation-of-INC-and-Moderate-Phase.md",
        "14_Foundation-of-INC-and-Moderate-Phase.md",
        "14_Foundation-of-INC-and-Moderate-Phase_Complete-Topic-Package.md",
        [
            "basic/07_Economic-Impact-of-British-Rule.md",
            "basic/09_Social-and-Cultural-Policy-Education-Press.md",
            "basic/12_Administrative-Changes-After-1858.md",
            "basic/15_Militant-Nationalism-and-Swadeshi.md",
        ],
        ["https://elibrary.sansad.in/"],
        "A 2026 live search found no topic-tight official commemoration that "
        "improves the historical explanation. Parliament Digital Library is "
        "retained only as a present-day archive bridge for representative "
        "politics; no contemporary party claim is imported into the history.",
        "OCR checks use Bipan Chandra's Modern India chapter on the nationalist "
        "movement and India's Struggle for Independence chapters on the "
        "foundation of the Congress, Moderate politics and economic nationalism. "
        "Sekhar Bandyopadhyay is used for the political-association and public-"
        "sphere context.",
        "The verified 2021 GS-I question on the Moderates' role in preparing the "
        "wider freedom movement is solved. No adjacent economic-history or "
        "constitutional question is relabelled as a direct Topic 14 PYQ.",
        [
            (
                "British Indian Association",
                "The British Indian Association was formed in Bengal in 1851 and "
                "represented an early elite form of organised political articulation.",
            ),
            (
                "East India Association",
                "Dadabhai Naoroji founded the East India Association in London in "
                "1866 to place Indian questions before British public opinion.",
            ),
            (
                "Poona Sarvajanik Sabha",
                "The Poona Sarvajanik Sabha emerged in 1870 as an important western-"
                "India forum claiming to represent public interests.",
            ),
            (
                "Indian Association",
                "Surendranath Banerjea and Ananda Mohan Bose founded the Indian "
                "Association in 1876 and pursued broader political mobilisation.",
            ),
            (
                "Madras Mahajan Sabha",
                "The Madras Mahajan Sabha became a major pre-Congress political "
                "association in the Madras Presidency and helped develop regional "
                "public work before the all-India platform.",
            ),
            (
                "Bombay Presidency Association",
                "The Bombay Presidency Association became an important western-India "
                "pre-Congress body within the network that preceded the national "
                "organisation.",
            ),
            (
                "First INC session",
                "The first Indian National Congress session met at Bombay in December "
                "1885 with seventy-two delegates.",
            ),
            (
                "A.O. Hume",
                "A.O. Hume helped organise the Congress, but his role does not make "
                "Indian nationalism a colonial creation.",
            ),
            (
                "W.C. Bonnerjee",
                "W.C. Bonnerjee presided over the first Indian National Congress "
                "session at Bombay in 1885.",
            ),
            (
                "Safety-valve debate",
                "The safety-valve explanation is a disputed interpretation; the "
                "Congress arose from accumulated Indian associations, grievances and "
                "national consciousness.",
            ),
            (
                "Moderate leadership",
                "Naoroji, Gokhale, Pherozeshah Mehta, Ranade, R.C. Dutt, Tyabji, "
                "Banerjea and Bonnerjee were prominent Moderate leaders.",
            ),
            (
                "Constitutional agitation",
                "Moderates used petitions, resolutions, public meetings, newspapers, "
                "legislative criticism and deputations rather than mass civil "
                "disobedience.",
            ),
            (
                "Drain theory",
                "Dadabhai Naoroji's drain critique linked Indian poverty to the "
                "unrequited transfer of resources under colonial rule.",
            ),
            (
                "Economic nationalism",
                "Moderate economic criticism joined the drain, deindustrialisation, "
                "land-revenue pressure, high military expenditure and discriminatory "
                "trade and service policies.",
            ),
            (
                "Indianisation of services",
                "Moderates demanded greater Indian entry into higher administration "
                "and simultaneous civil-service examinations in India and Britain.",
            ),
            (
                "Legislative councils",
                "Moderates demanded enlarged councils, an elective principle, budget "
                "scrutiny and greater Indian representation.",
            ),
            (
                "Civil liberties",
                "Freedom of speech, press and association formed a durable part of "
                "Moderate criticism of colonial government.",
            ),
            (
                "Indian Councils Act 1892",
                "The Indian Councils Act 1892 enlarged councils and allowed limited "
                "budget discussion and questions without responsible government.",
            ),
            (
                "Political education",
                "Annual sessions, newspapers and council speeches created a shared "
                "all-India grievance vocabulary and trained a national political class.",
            ),
            (
                "Moderate limitation and legacy",
                "The Moderates had a narrow social base and excessive faith in British "
                "liberalism, yet built the organisation and critique inherited by "
                "later mass nationalism.",
            ),
        ],
        [
            "Hume's organisational role must not be converted into proof that the "
            "Congress was solely a British safety valve.",
            "The first Congress session was at Bombay in 1885 under W.C. Bonnerjee, "
            "not at Calcutta under Dadabhai Naoroji.",
            "Moderates demanded constitutional reform and administrative "
            "Indianisation, not complete independence during this phase.",
            "The 1892 Act allowed limited budget discussion and questions, not "
            "responsible government or an elected majority.",
            "Petition, prayer and protest and political mendicancy are later labels, "
            "not complete descriptions of Moderate political education.",
            "A narrow social base limits the Moderates' reach without erasing their "
            "economic and organisational contribution.",
        ],
        [
            (
                10,
                "How did pre-Congress political associations prepare the ground for "
                "the Indian National Congress?",
                "Provincial associations created leaders, publicity networks and a "
                "constitutional repertoire that the Congress scaled into an all-India "
                "platform.",
                [0, 1, 2, 3, 4, 5, 6],
            ),
            (
                10,
                "Why is the safety-valve theory an inadequate explanation of the "
                "foundation of the Congress?",
                "Hume helped with organisation, but accumulated Indian political work "
                "and common colonial grievances supplied the movement's causation and "
                "historical direction.",
                [6, 7, 8, 9],
            ),
            (
                15,
                "Explain how Moderate economic nationalism converted poverty into a "
                "political indictment of colonial rule.",
                "The drain and linked critiques showed poverty as a policy-produced "
                "feature of empire rather than an accidental social condition.",
                [12, 13, 14, 15, 18],
            ),
            (
                15,
                "To what extent did constitutional agitation strengthen the early "
                "national movement?",
                "It trained a national public and secured limited procedural openings, "
                "but colonial executive supremacy exposed its structural ceiling.",
                [11, 15, 16, 17, 18, 19],
            ),
            (
                20,
                "Assess the achievements and limitations of the Moderate phase of the "
                "Indian National Congress.",
                "Measured by immediate transfer of power the Moderates achieved little; "
                "measured by political organisation, economic critique and national "
                "education, they created the base of later freedom struggle.",
                [6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            ),
            (
                20,
                "Were Moderate and militant nationalism a rupture or successive stages "
                "of one anti-colonial development?",
                "Militants rejected Moderate methods and faith in British justice while "
                "retaining the economic critique, Congress platform and national "
                "vocabulary built before 1905.",
                [10, 11, 12, 13, 18, 19],
            ),
        ],
        [
            (
                "2021",
                "GS-I",
                "To what extent did the role of the Moderates prepare a base for the "
                "wider freedom movement? Comment. (15 marks, 250 words)",
                "model-solution",
                "The Moderates unified provincial political work through an annual "
                "Congress, trained public opinion through press and council debate, "
                "created the economic indictment of colonialism through the drain "
                "theory, defended civil liberties and normalised representative "
                "demands. Their narrow social base and faith in British justice limited "
                "immediate gains, but later nationalists inherited their organisation, "
                "leaders and critique. They prepared a base intellectually and "
                "institutionally even where they failed to transfer power.",
            ),
        ],
        [
            "A.O. Hume",
            "W.C. Bonnerjee",
            "safety-valve",
            "drain theory",
            "Indian Councils Act 1892",
            "simultaneous ICS examination",
        ],
    ),
    base.topic(
        15,
        "Militant Nationalism, Swadeshi & the Partition of Bengal (1905-1908)",
        "15_Militant-Nationalism-and-Swadeshi.md",
        "15_Militant-Nationalism-and-Swadeshi.md",
        "15_Militant-Nationalism-Swadeshi-Partition-of-Bengal_Complete-Topic-Package.md",
        [
            "basic/14_Foundation-of-INC-and-Moderate-Phase.md",
            "basic/16_Revolutionary-Nationalism-Phase-I.md",
            "basic/17_Growth-of-Communalism-and-Muslim-League.md",
            "basic/20_Non-Cooperation-and-Khilafat-Movement.md",
        ],
        [
            "https://culture.gov.in/events/nationwide-commemoration-150-years-"
            "vande-mataram-be-inaugurated-prime-minister-shri-narendra",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2186984",
        ],
        "The Ministry of Culture's year-long Vande Mataram commemoration from "
        "7 November 2025 to 7 November 2026 is used only as an official public-"
        "memory bridge. Historical claims about the 1905 anti-partition and "
        "Swadeshi mobilisation remain grounded in the repository and OCR books.",
        "OCR checks use Bipan Chandra's Modern India and India's Struggle for "
        "Independence chapters on Curzon, Bengal partition, Swadeshi, boycott, "
        "national education, passive resistance and the Surat split. Sekhar "
        "Bandyopadhyay supplies regional and social-base qualifications.",
        "The verified 2020 GS-I Curzon question and four routed 2018-2023 "
        "Prelims demands are integrated. Where the local books or official local "
        "key do not support a named attribution, the workbook preserves an "
        "explicit evidence gap rather than inventing an answer.",
        [
            (
                "Calcutta Corporation Act",
                "Curzon's Calcutta Corporation Act of 1899 reduced elected Indian "
                "influence and symbolised an anti-representative official turn.",
            ),
            (
                "Indian Universities Act",
                "The Indian Universities Act of 1904 increased official supervision "
                "over universities and intensified nationalist distrust of Curzon.",
            ),
            (
                "Causes of militant nationalism",
                "Moderate limitations, colonial repression, economic distress, cultural "
                "self-assertion and Asian victories encouraged militant nationalism.",
            ),
            (
                "Partition announcement",
                "Curzon's partition of Bengal was announced in July 1905 and was "
                "presented officially as an administrative reorganisation.",
            ),
            (
                "Divide-and-rule reading",
                "Nationalists interpreted Bengal partition as a political attempt to "
                "divide a growing Bengali public and weaken anti-colonial mobilisation.",
            ),
            (
                "Boycott Resolution",
                "A mass meeting at Calcutta Town Hall adopted the Boycott Resolution "
                "on 7 August 1905, a key launch point of the Swadeshi movement.",
            ),
            (
                "Partition takes effect",
                "The partition took effect on 16 October 1905, which was marked by "
                "hartals, processions, mourning and public solidarity rituals.",
            ),
            (
                "Swadeshi",
                "Swadeshi promoted indigenous goods, enterprise and self-reliance as "
                "both an economic programme and a political discipline.",
            ),
            (
                "Boycott",
                "Boycott rejected foreign goods and, in more militant programmes, "
                "extended toward official schools, courts and functions where feasible.",
            ),
            (
                "National education",
                "The National Council of Education was founded in 1906, and Bengal "
                "National College was associated with Aurobindo Ghosh.",
            ),
            (
                "Samitis and cultural mobilisation",
                "Samitis, songs, festivals, processions and Vande Mataram carried "
                "anti-partition politics beyond petitions into everyday public action.",
            ),
            (
                "Lal-Bal-Pal",
                "Lal-Bal-Pal refers to Lala Lajpat Rai, Bal Gangadhar Tilak and Bipin "
                "Chandra Pal, leading symbols of assertive nationalism.",
            ),
            (
                "Congress programme, 1905-06",
                "The Banaras Congress of 1905 supported Swadeshi and Bengal boycott; "
                "the Calcutta Congress of 1906 under Dadabhai Naoroji adopted a "
                "compromise programme of self-government, Swadeshi, boycott and "
                "national education.",
            ),
            (
                "Passive resistance",
                "The militant programme used passive resistance, self-help and "
                "withdrawal of cooperation to reduce dependence on colonial institutions.",
            ),
            (
                "Regional spread",
                "Swadeshi spread beyond Bengal through Tilak in Maharashtra, Lajpat "
                "Rai and Ajit Singh in Punjab, and V.O. Chidambaram Pillai in Madras, "
                "but intensity and social reach varied.",
            ),
            (
                "Social reach",
                "Students, women, urban middle classes and selected workers and rural "
                "groups participated, while peasant and Muslim participation remained "
                "uneven.",
            ),
            (
                "Surat Split",
                "The Congress split at Surat in 1907 over leadership, methods and "
                "control between Moderate and militant currents.",
            ),
            (
                "Repression and decline",
                "Bans, arrests, prosecutions, deportations, press restrictions and "
                "Congress division weakened the open Swadeshi movement after 1907.",
            ),
            (
                "Annulment and reorganisation",
                "Annulment and the transfer of the imperial capital to Delhi were "
                "announced in 1911; the 1912 reorganisation reunited Bengali-speaking "
                "areas but separately arranged Bihar-Orissa and Assam.",
            ),
            (
                "Long-term legacy",
                "Swadeshi made boycott, constructive work, national education, self-"
                "reliance and emotionally resonant mobilisation part of later politics.",
            ),
        ],
        [
            "The 7 August 1905 Boycott Resolution, 16 October implementation and "
            "1911 annulment are different chronological anchors.",
            "Swadeshi meant constructive indigenous production; boycott meant "
            "withdrawal from foreign goods or colonial institutions.",
            "The Surat split occurred in 1907 after Swadeshi began; it did not cause "
            "the anti-partition movement.",
            "Annulment in 1911 and reorganisation in 1912 did not simply restore the "
            "entire pre-1905 province or leave Calcutta as the imperial capital.",
            "Militant nationalists radicalised the Moderate economic critique rather "
            "than discarding it.",
            "Vande Mataram's mobilising power and Hindu-inflected idiom should both be "
            "assessed without reducing the movement to one cultural symbol.",
        ],
        [
            (
                10,
                "Why did Curzon's policies accelerate militant nationalism?",
                "Curzon joined administrative centralisation and cultural arrogance "
                "with a partition perceived as political division, turning Moderate "
                "disillusion into an active programme.",
                [0, 1, 2, 3, 4],
            ),
            (
                10,
                "Distinguish Swadeshi from boycott in the anti-partition movement.",
                "Boycott withdrew consumption and cooperation, while Swadeshi built "
                "indigenous production, education and self-reliance; the two were "
                "negative and constructive arms of one strategy.",
                [5, 7, 8, 9, 13],
            ),
            (
                15,
                "How did the Partition of Bengal transform the methods of Indian "
                "nationalism?",
                "A concrete grievance shifted politics from annual petitioning toward "
                "boycott, constructive work, cultural mobilisation and passive "
                "resistance.",
                [3, 4, 5, 6, 7, 8, 9, 10, 13],
            ),
            (
                15,
                "Assess the social and regional reach of the Swadeshi movement.",
                "Swadeshi widened participation and travelled beyond Bengal, but its "
                "urban concentration, regional variation and uneven peasant-Muslim "
                "participation limited durable mass consolidation.",
                [10, 11, 12, 14, 15, 17],
            ),
            (
                20,
                "Evaluate the achievements and limitations of the Swadeshi movement.",
                "Swadeshi reversed a major decision and transformed nationalist "
                "technique, but repression, organisational division and social "
                "narrowness prevented sustained mass politics.",
                [5, 7, 8, 9, 10, 14, 15, 16, 17, 18, 19],
            ),
            (
                20,
                "Was Swadeshi a precursor to Gandhian mass nationalism?",
                "Swadeshi supplied boycott, passive resistance, self-reliance and "
                "constructive work; Gandhi later added village-scale organisation, "
                "disciplined non-violence and broader social inclusion.",
                [7, 8, 9, 10, 13, 14, 15, 19],
            ),
        ],
        [
            (
                "2018",
                "Prelims GS-I",
                "He wrote biographies of Mazzini, Garibaldi, Shivaji and Shrikrishna; "
                "stayed in America for some time; and was also elected to the Central "
                "Assembly. Identify the leader from Aurobindo Ghosh, Bipin Chandra "
                "Pal, Lala Lajpat Rai and Motilal Nehru.",
                "open-evidence-gap",
                "The routed local owner and held official-key set do not establish the "
                "answer. No leader is named solely from memory; the package retains the "
                "demand as a verification card.",
            ),
            (
                "2019",
                "Prelims GS-I",
                "With reference to the Swadeshi Movement, assess whether it revived "
                "indigenous artisan crafts and industries and whether the National "
                "Council of Education was established as part of the movement.",
                "solved-demand-card",
                "Retain indigenous enterprise, swadeshi stores and national education, "
                "including the National Council of Education in 1906 and Bengal "
                "National College. Do not reduce Swadeshi to foreign-cloth bonfires.",
            ),
            (
                "2020",
                "Prelims GS-I",
                "For Sakharam Ganesh Deuskar's Desher Katha, assess the statements on "
                "the colonial state's hypnotic conquest of the mind, inspiration for "
                "Swadeshi street plays and folk songs, and whether 'desh' referred "
                "specifically to Bengal.",
                "open-evidence-gap",
                "The held repository records the routed demand but lacks sufficient "
                "support for the statement-level answer and circulation claims. No "
                "unsupported attribution or number is asserted.",
            ),
            (
                "2020",
                "GS-I",
                "Evaluate the policies of Lord Curzon and their long term implications "
                "on the national movement. (10 marks, 150 words)",
                "model-solution",
                "Curzon strengthened official control through municipal and university "
                "measures and partitioned Bengal in 1905. The policies discredited "
                "faith in incremental reform, united anti-partition protest and "
                "generated boycott, Swadeshi, national education and militant "
                "nationalism. Repression and division narrowed the movement, but the "
                "long-term result was a transformed nationalist repertoire.",
            ),
            (
                "2023",
                "Prelims GS-I",
                "Statement-I: 7th August is declared as National Handloom Day. "
                "Statement-II: It was in 1905 that the Swadeshi Movement was launched "
                "on the same day. Assess the assertion-explanation relationship.",
                "solved-demand-card",
                "National Handloom Day is observed on 7 August, matching the Calcutta "
                "Town Hall Boycott Resolution of 7 August 1905. Keep this date distinct "
                "from 16 October, when partition took effect.",
            ),
        ],
        [
            "Calcutta Town Hall",
            "National Council of Education",
            "Lal-Bal-Pal",
            "Aurobindo Ghosh",
            "Surat Split",
            "Vande Mataram",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-14": [
        (
            "Associations converged into an all-India platform",
            "chronology",
            """1851 BRITISH INDIAN ASSOCIATION -> elite articulation in Bengal
1866 EAST INDIA ASSOCIATION -> Indian claims before British opinion
1870 POONA SARVAJANIK SABHA -> public representation in western India
1876 INDIAN ASSOCIATION -> broader political mobilisation
1884-85 MADRAS / BOMBAY BODIES -> regional networks ready for Congress
DEC 1885 INC -> one annual all-India platform, not a political beginning from zero.""",
            ["Mini-timeline", "Pre-1885 groundwork"],
        ),
        (
            "The first Congress session identity card",
            "identity-card",
            """PLACE -> Bombay
DATE -> December 1885
DELEGATES -> 72
PRESIDENT -> W.C. Bonnerjee
ORGANISER -> A.O. Hume helped convene
EXAM LIMIT -> organiser does not equal creator of Indian nationalism.""",
            ["Foundation and the safety-valve controversy", "Must-Know Facts"],
        ),
        (
            "Safety valve versus national movement",
            "argument-tree",
            """SAFETY-VALVE CLAIM -> Hume channelled dangerous discontent
PROBLEM 1 -> motive of one organiser cannot explain a social movement
PROBLEM 2 -> associations, press and grievances existed before 1885
NATIONAL-MOVEMENT THESIS -> Indian forces supplied cause and content
BALANCED VERDICT -> Hume explains facilitation, not historical ownership.""",
            ["Foundation and the safety-valve controversy", "Qualified thesis options"],
        ),
        (
            "Moderate constitutional repertoire",
            "process",
            """GRIEVANCE -> resolution at annual Congress
RESOLUTION -> petition, memorial and press campaign
PUBLICITY -> meetings, newspapers and British deputations
INSTITUTION -> legislative question and budget criticism
PURPOSE -> educate Indian opinion and pressure imperial liberalism
CEILING -> the colonial executive retained decisive power.""",
            ["Constitutional method", "Mechanism - how petitioning built a nation"],
        ),
        (
            "Economic nationalism made poverty political",
            "causal-web",
            """DRAIN -> resources transferred without equivalent return
DEINDUSTRIALISATION -> older production weakened under dependent trade
REVENUE PRESSURE -> cultivators carried fiscal risk
MILITARY COST -> Indian revenues financed imperial priorities
SERVICE EXCLUSION -> salaries and authority remained racially unequal
CONCLUSION -> poverty became an indictment of colonial structure.""",
            ["Economic nationalism - the intellectual achievement", "Drain theory"],
        ),
        (
            "Demand map of the Moderates",
            "comparison",
            """COUNCILS -> enlargement, elective principle, questions and budgets
SERVICES -> Indianisation and simultaneous ICS examinations
FINANCE -> lower military spending and scrutiny of home charges
RIGHTS -> speech, press and association
ADMINISTRATION -> accountability and racial equality
BOUNDARY -> reform of empire, not immediate complete independence.""",
            ["Key classification / data", "Moderate demands"],
        ),
        (
            "Indian Councils Act 1892: gain and ceiling",
            "balance-sheet",
            """GAIN -> enlarged legislative councils
GAIN -> indirect election-like recommending bodies
GAIN -> budget discussion and questions
NO GAIN -> elected majority
NO GAIN -> executive responsibility or budget control
VERDICT -> procedure expanded while colonial power remained intact.""",
            ["Concrete institutional gains", "Factual-risk cautions"],
        ),
        (
            "Annual Congress as political education",
            "feedback-loop",
            """ANNUAL SESSION -> leaders compare regional grievances
COMMON LANGUAGE -> rights, economy, representation and accountability
PRESS REPRODUCTION -> arguments reach provincial publics
COUNCIL PRACTICE -> evidence, questions and budget criticism improve
NEW PUBLIC -> Indians imagine a shared political community
LOOP -> public pressure strengthens the next annual session.""",
            ["Political education", "Mechanism - how petitioning built a nation"],
        ),
        (
            "The social-base paradox",
            "two-sided",
            """STRENGTH -> educated lawyers, journalists and teachers mastered print and law
STRENGTH -> presidency-town networks enabled all-India coordination
LIMIT -> peasants, workers, women and many lower castes remained outside
LIMIT -> English and institutional politics restricted access
RESULT -> strong argument and weak mass reach
NEXT PHASE -> boycott sought mobilisation beyond the petitioning elite.""",
            ["Social base and its consequences", "Counter-evidence, balance and variation"],
        ),
        (
            "Achievement depends on the measuring scale",
            "evaluation-matrix",
            """POWER TRANSFER -> LOW: no responsible government
PROCEDURAL OPENING -> LIMITED: 1892 councils
ECONOMIC CRITIQUE -> HIGH: colonial exploitation exposed
ORGANISATION -> HIGH: enduring all-India platform
POLITICAL EDUCATION -> HIGH: trained leaders and public opinion
VERDICT -> immediate failure coexisted with foundational success.""",
            ["Evaluation of Moderates", "Verdict scaffolds"],
        ),
        (
            "Moderates to militants: continuity and rupture",
            "bridge",
            """CONTINUITY -> drain critique and colonial economic indictment
CONTINUITY -> Congress as the national organisational arena
CONTINUITY -> civil liberties and representative claims
RUPTURE -> faith in British justice declined
RUPTURE -> petition yielded to boycott, self-reliance and passive resistance
1905 -> limitation of one method generated the next repertoire.""",
            ["Why Extremism followed", "Continuity/rupture"],
        ),
        (
            "Moderate answer-writing spine",
            "answer-spine",
            """DEFINE -> constitutional nationalism with an educated middle-class base
ORIGIN -> pre-1885 associations plus common colonial grievances
METHOD -> petition, press, councils and deputations
ACHIEVEMENT -> organisation, economic critique and political education
LIMIT -> narrow reach, loyalist faith and limited concessions
VERDICT -> failed to gain power, succeeded in making later struggle possible.""",
            ["Mark-scaled structure", "Verdict scaffolds"],
        ),
    ],
    "modern-indian-history-15": [
        (
            "Curzon's measures formed a provocation chain",
            "chronology",
            """1899 CALCUTTA CORPORATION ACT -> reduced elected Indian influence
1904 UNIVERSITIES ACT -> tighter official supervision
JUL 1905 PARTITION ANNOUNCED -> administrative claim, political distrust
7 AUG 1905 BOYCOTT RESOLUTION -> organised anti-partition technique
16 OCT 1905 PARTITION EFFECTIVE -> public mourning and mass mobilisation
RESULT -> Moderate frustration became militant self-assertion.""",
            ["Mini-timeline", "Causes of Extremism"],
        ),
        (
            "Three dates that must not be merged",
            "date-card",
            """JULY 1905 -> partition announced
7 AUGUST 1905 -> Calcutta Town Hall Boycott Resolution
16 OCTOBER 1905 -> partition took effect
1907 -> Surat split
1911-12 -> annulment announced, capital shifted and provinces reorganised
EXAM RULE -> identify announcement, movement launch, enforcement and reversal.""",
            ["The 1905 sequence and the 7 August anchor", "Factual-risk cautions"],
        ),
        (
            "Administrative pretext versus political reading",
            "argument-tree",
            """OFFICIAL CASE -> Bengal was too large for efficient administration
NATIONALIST READING -> division targeted a growing political public
EASTERN PROVINCE -> communal and regional boundaries gained political weight
POPULAR RESPONSE -> partition became evidence of divide and rule
ANALYTICAL RULE -> distinguish stated rationale, perceived intent and outcome.""",
            ["Partition politics", "Anti-partition core"],
        ),
        (
            "Swadeshi and boycott were complementary",
            "comparison",
            """BOYCOTT / NEGATIVE ARM -> refuse foreign goods and selected institutions
SWADESHI / CONSTRUCTIVE ARM -> produce, buy and organise indigenous alternatives
SHARED PURPOSE -> self-reliance plus pressure on colonial authority
ECONOMIC EFFECT -> selected local falls in imported-goods sales
LIMIT -> supply, capital and participation varied across region and class.""",
            ["Effectiveness of boycott", "Constructive programme"],
        ),
        (
            "The constructive programme built institutions",
            "institution-map",
            """INDUSTRY -> indigenous production, stores and investment
EDUCATION -> National Council of Education, 1906
COLLEGE -> Bengal National College and Aurobindo Ghosh
ARBITRATION -> alternatives to colonial legal dependence
SAMITIS -> local organisation, service and physical culture
LEGACY -> protest joined durable capacity-building.""",
            ["Constructive programme - industry and education", "Programme"],
        ),
        (
            "Cultural mobilisation widened and narrowed politics",
            "two-sided",
            """WIDENED -> songs, festivals, processions and Vande Mataram
WIDENED -> politics entered schools, homes, streets and marketplaces
WIDENED -> students and women gained visible roles
NARROWED -> Hindu-inflected symbols could limit Muslim participation
ANALYSIS -> mobilisation and exclusion can arise from the same idiom
CAUTION -> cultural symbolism was not the movement's whole programme.""",
            ["Cultural mobilisation and its ambivalence", "Social reach"],
        ),
        (
            "Militant nationalism was a programme, not a mood",
            "concept-map",
            """SWARAJ -> political objective and moral self-rule
ATMA-SHAKTI -> confidence, sacrifice and self-reliance
BOYCOTT -> economic and institutional withdrawal
PASSIVE RESISTANCE -> non-cooperation with unjust authority
NATIONAL EDUCATION -> autonomous minds and institutions
LEADERSHIP -> Tilak, Lajpat Rai, B.C. Pal and Aurobindo.""",
            ["Extremism was a new ideology of active self-reliance", "Leadership"],
        ),
        (
            "Regional spread was uneven",
            "regional-matrix",
            """BENGAL -> anti-partition core, samitis, education and cultural action
MAHARASHTRA -> Tilak's assertive political idiom and boycott support
PUNJAB -> Lajpat Rai and agrarian-political discontent
MADRAS -> public meetings, press and Swadeshi support
ALL-INDIA CLAIM -> technique travelled
LIMIT -> intensity, leadership and social coalition differed by region.""",
            ["Regional spread", "Counter-evidence, balance and variation"],
        ),
        (
            "Participation expanded but did not become fully mass",
            "social-pyramid",
            """VISIBLE CORE -> students, professionals and urban middle classes
NEW PARTICIPANTS -> women, selected workers and rural groups
LOCAL ORGANISERS -> samitis and cultural networks
THIN REACH -> much of the peasantry and labour remained outside
UNEQUAL INCLUSION -> Muslim participation varied and often weakened
VERDICT -> wider than Moderate politics, narrower than Gandhian mobilisation.""",
            ["Social reach", "Incomplete-mass-politics thesis"],
        ),
        (
            "Congress compromise gave way to the Surat rupture",
            "conflict-map",
            """BANARAS 1905 -> Congress accepted Swadeshi and Bengal boycott
CALCUTTA 1906 -> Naoroji bridged swaraj, boycott, Swadeshi and education
DISPUTE -> scope, passive resistance and control of organisation
1907 SURAT -> physical breakdown and formal split
STATE ADVANTAGE -> divided opposition faced intensified repression
LESSON -> movement technique requires an organisation able to contain debate.""",
            ["Repression and the Surat split", "Two-currents thesis"],
        ),
        (
            "Decline and legacy moved in opposite directions",
            "balance-sheet",
            """DECLINE -> repression, arrests, deportation and press controls
DECLINE -> Surat split and limited rural organisation
DECLINE -> boycott fatigue and uneven indigenous supply
LEGACY -> self-reliance, national education and constructive work
LEGACY -> boycott and passive resistance became normal nationalist tools
VERDICT -> short organisational high tide, long strategic afterlife.""",
            ["Achievement-and-limitation ledger", "Transmission to Gandhian politics"],
        ),
        (
            "Swadeshi answer-writing spine",
            "answer-spine",
            """TRIGGER -> Curzonian reaction and Bengal partition
CAUSES -> Moderate limits, distress, repression and Asian self-confidence
METHODS -> boycott, Swadeshi, education, samitis and passive resistance
REACH -> students, women, regions and selected workers/rural groups
LIMITS -> repression, division, social narrowness and communal tension
VERDICT -> failed to sustain peak mobilisation, transformed nationalist grammar.""",
            ["Mark-scaled structure", "Verdict scaffolds"],
        ),
    ],
}


def session_visual(title: str, terms: list[str]) -> str:
    """Create a concept-appropriate visual instead of a repeated generic chain."""

    lowered = title.casefold()
    if "mini-timeline" in lowered:
        diagram = (
            "PRECONDITION -> ORGANISING EVENT -> POLITICAL RESPONSE\n"
            "-> INSTITUTIONAL CHANGE -> NEXT NATIONALIST PHASE"
        )
    elif "snapshot" in lowered:
        diagram = (
            "HISTORICAL CONTEXT\n"
            "      |\n"
            "CORE IDEA -> ACTORS -> METHOD -> OUTCOME\n"
            "      |\n"
            "QUALIFICATION / LIMIT"
        )
    elif "classification" in lowered or "ledger" in lowered:
        diagram = (
            "DIMENSION        EVIDENCE        MECHANISM        LIMIT\n"
            "political   ->   institution -> pressure      -> colonial ceiling\n"
            "economic    ->   critique    -> delegitimation -> uneven reach\n"
            "social      ->   participants-> mobilisation   -> exclusion"
        )
    elif "study links" in lowered:
        diagram = (
            "EARLIER OWNER -> PRESENT TOPIC -> NEXT OWNER\n"
            "precondition -> core mechanism -> consequence\n"
            "EXAM RULE: borrow context, preserve each topic's boundary."
        )
    elif "must-know" in lowered:
        diagram = (
            "ACTOR + DATE + INSTITUTION + PURPOSE\n"
            "                |\n"
            "         PRELIMS IDENTITY CARD\n"
            "                |\n"
            "      REMOVE THE NEAREST FALSE MATCH"
        )
    elif "high-risk" in lowered or "factual-risk" in lowered:
        diagram = (
            "TEMPTING CLAIM -> SOURCE CHECK -> CORRECT DISTINCTION\n"
            "wrong date     -> chronology   -> exact event\n"
            "wrong actor    -> institution  -> verified association\n"
            "overclaim      -> scope limit  -> qualified conclusion"
        )
    elif "current link" in lowered:
        diagram = (
            "VERIFIED CURRENT ANCHOR\n"
            "          |\n"
            "PUBLIC MEMORY / INSTITUTIONAL BRIDGE\n"
            "          |\n"
            "HISTORICAL CLAIMS REMAIN SOURCE-BOUND"
        )
    elif "mains angles" in lowered:
        diagram = (
            "CAUSE QUESTION -> explain mechanism\n"
            "METHOD QUESTION -> compare repertoire\n"
            "EVALUATION QUESTION -> achievement + limit\n"
            "LEGACY QUESTION -> continuity + change"
        )
    elif "demand and directive" in lowered:
        diagram = (
            "DIRECTIVE -> TASK\n"
            "EXPLAIN   -> causal chain\n"
            "ASSESS    -> evidence on both sides\n"
            "COMPARE   -> common axis + difference\n"
            "COMMENT   -> concise thesis + qualification"
        )
    elif "qualified thesis" in lowered:
        diagram = (
            "CLAIM\n"
            "  + strongest evidence\n"
            "  + explicit limitation\n"
            "  = QUALIFIED THESIS"
        )
    elif "mark-scaled" in lowered:
        diagram = (
            "10 MARKS -> thesis + 3 evidence units + limit\n"
            "15 MARKS -> dimensions + counterpoint + verdict\n"
            "20 MARKS -> chronology + mechanisms + variation + legacy"
        )
    elif "named evidence" in lowered:
        diagram = (
            "CLAIM -> NAMED ACTOR / ACT / EVENT -> SIGNIFICANCE\n"
            "                                      |\n"
            "                              LIMIT / CAUTION\n"
            "                                      |\n"
            "                              EXAM-READY PARAGRAPH"
        )
    elif "mechanism" in lowered or "transmission" in lowered:
        diagram = (
            "CONDITION -> ACTION -> RESPONSE -> POLITICAL LEARNING\n"
            "     ^                                      |\n"
            "     +--------- NEXT-PHASE FEEDBACK --------+"
        )
    elif "counter-evidence" in lowered:
        diagram = (
            "MAIN CLAIM -> SUPPORTING EVIDENCE\n"
            "     |\n"
            "COUNTER-EVIDENCE -> REGIONAL / SOCIAL VARIATION\n"
            "     |\n"
            "GRADED, NON-ABSOLUTE JUDGEMENT"
        )
    elif "verdict" in lowered:
        diagram = (
            "IMMEDIATE OUTCOME + STRUCTURAL LEGACY - DOCUMENTED LIMIT\n"
            "                         |\n"
            "                    FINAL VERDICT"
        )
    else:
        cleaned = [term.strip(" :") for term in terms[:4]]
        diagram = " -> ".join(cleaned) + "\ncontext -> mechanism -> outcome -> limit"
    return (
        "#### VISUAL FIRST\n\n"
        "```text\n"
        f"{title.upper()}\n"
        f"{diagram}\n"
        "```\n\n"
        "*The visual fixes the subtopic's structure before the detailed evidence.*"
    )


def session_definitions(
    title: str,
    topic_title: str,
    terms: list[str],
) -> str:
    """Supply exam-use definitions that explain purpose rather than repeat labels."""

    lowered = title.casefold()
    if "mini-timeline" in lowered:
        plain = "the chronological spine that prevents announcement, action and consequence from being merged"
        technical = "a sequence of dated turning points used to test causation and periodisation"
    elif "snapshot" in lowered:
        plain = "the shortest statement of the topic's central historical change"
        technical = "a framing proposition linking context, actors, methods, outcomes and limits"
    elif "classification" in lowered or "ledger" in lowered:
        plain = "a comparison of the topic's political, economic, institutional and social dimensions"
        technical = "an analytical matrix that places evidence under a common axis before evaluation"
    elif "study links" in lowered:
        plain = "the boundary map connecting this topic to its preconditions and consequences"
        technical = "cross-topic routing that imports context without transferring claims to the wrong owner"
    elif "must-know" in lowered:
        plain = "the minimum actor-date-institution set required for accurate recall"
        technical = "a Prelims identity bank designed for statement matching and elimination"
    elif "high-risk" in lowered or "factual-risk" in lowered:
        plain = "the correction sheet for the topic's nearest and most tempting false statements"
        technical = "a set of source-bounded distinctions controlling chronology, attribution and scope"
    elif "current link" in lowered:
        plain = "a bounded bridge between verified present-day public memory and the historical topic"
        technical = "contextual linkage that cannot serve as evidence for nineteenth- or twentieth-century claims"
    elif "mains angles" in lowered:
        plain = "the recurring ways UPSC can convert the topic into an analytical question"
        technical = "a demand map covering causation, method, evaluation, comparison and legacy"
    elif "answer architecture" in lowered:
        plain = "the ordered plan for turning evidence into a complete UPSC answer"
        technical = "a mark-scaled structure joining thesis, dimensions, counterpoint and graded verdict"
    elif "demand and directive" in lowered:
        plain = "a guide to what each command word requires the answer to do"
        technical = "directive-sensitive routing from question demand to evidence and judgement"
    elif "qualified thesis" in lowered:
        plain = "a central claim that states both historical significance and limitation"
        technical = "an arguable proposition calibrated by counter-evidence rather than an absolute claim"
    elif "mark-scaled" in lowered:
        plain = "the adjustment of structure and evidence load to the marks and word limit"
        technical = "progressive expansion from compact causation to multidimensional evaluation"
    elif "named evidence" in lowered:
        plain = "the actor, date, institution or event that proves an analytical claim"
        technical = "a claim-evidence-significance-limit unit capable of becoming one Mains paragraph"
    elif "mechanism" in lowered or "transmission" in lowered:
        plain = "the causal process explaining how one political condition produced another"
        technical = "a linked sequence of condition, action, response, learning and later inheritance"
    elif "counter-evidence" in lowered:
        plain = "the evidence that prevents the main argument from becoming universal or heroic"
        technical = "regional, social and institutional variation used to qualify causal claims"
    elif "verdict" in lowered:
        plain = "the final weighing of immediate result, structural legacy and documented limit"
        technical = "a graded judgement that answers the directive without repeating the introduction"
    else:
        anchors = ", ".join(term.strip(" :") for term in terms[:3])
        plain = f"the part of {topic_title} organised around {anchors}"
        technical = "an evidence-led unit connecting context, mechanism, outcome and qualification"
    return (
        "#### CONCEPT DEFINITIONS\n\n"
        f"- **Plain definition:** {title} is {plain}.\n"
        f"- **Technical definition:** For exam use, it is {technical}."
    )


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
}


@contextmanager
def configured_base() -> Iterator[None]:
    """Use shared generation helpers without leaking module-global overrides."""

    previous = {name: getattr(base, name) for name in _BASE_OVERRIDES}
    try:
        for name, value in _BASE_OVERRIDES.items():
            setattr(base, name, value)
        yield
    finally:
        for name, value in previous.items():
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
        "scope": "Modern Indian History learner-v2 Topics 14-15",
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


def self_check(
    config: dict[str, object],
    markdown: str,
    workbook: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    with configured_base():
        base.self_check(
            config,
            markdown,
            workbook,
            session_count,
            graphical_path,
        )


def main() -> int:
    write_ascii_spec()
    with configured_base():
        base.write_section_manifest()
        SESSION_DIR.mkdir(parents=True, exist_ok=True)
        for config in TOPICS:
            markdown, workbook, session_count = base.assemble(config)
            key = str(config["key"])
            source_path = SESSION_DIR / f"{key}_Learning-Session.md"
            workbook_path = SESSION_DIR / f"{key}_Solved-Workbook.md"
            source_path.write_text(markdown, encoding="utf-8")
            workbook_path.write_text(workbook, encoding="utf-8")
            Path(config["canonical"]).write_text(markdown, encoding="utf-8")
            graphical_path = base.write_graphical_spec(config, markdown)
            base.write_generation_spec(
                config,
                source_path,
                workbook_path,
                graphical_path,
            )
            base.self_check(
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
