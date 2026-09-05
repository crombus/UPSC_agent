"""Build Modern Indian History learner-v2 Topics 18-19.

This authoring generator writes complete reusable Markdown, solved workbooks,
manual ASCII and graphical specifications, and tracker-free generation-one
manifests. It deliberately does not render PDFs, update trackers, regenerate
indexes, or publish final packages.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base
import generate_modern_history_16_17_sequential as previous


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
    / "modern-indian-history-18-19-2026-08-31-sequential.json"
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
            ROOT
            / "knowledge-export"
            / "Prelims PYQ"
            / "QP-CSP-18-GS-I-C.pdf.md",
            ROOT
            / "knowledge-export"
            / "Prelims PYQ"
            / "CSP_2020_GS_Paper-1.pdf.md",
            ROOT
            / "knowledge-export"
            / "Prelims PYQ"
            / "csp-p1.pdf.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "GENERAL-STUDIES-PAPER-I.pdf.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "QP-CSM19-GeneralStudies-I.pdf.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "QP-CSM-23-GENERAL-STUDIES-PAPER-I-180923.pdf.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "UPSC Mains 2024 GS Paper I.md",
            ROOT
            / "knowledge-export"
            / "Prelims PYQ"
            / "2026-GS1-Set A.md",
        ]
    )
)
OFFICIAL_QUESTION_SOURCES = [
    path for path in OFFICIAL_QUESTION_SOURCES if path.is_file()
]


TOPICS = [
    base.topic(
        18,
        "First World War, the Home Rule League & the Lucknow Pact (1914–1918)",
        "18_WWI-Home-Rule-and-Lucknow-Pact.md",
        "18_WWI-Home-Rule-and-Lucknow-Pact.md",
        "18_First-World-War-Home-Rule-League-Lucknow-Pact_Complete-Topic-Package.md",
        [
            "basic/15_Militant-Nationalism-and-Swadeshi.md",
            "basic/17_Growth-of-Communalism-and-Muslim-League.md",
            "basic/19_Gandhis-Rise-Rowlatt-and-Jallianwala.md",
            "basic/20_Non-Cooperation-and-Khilafat-Movement.md",
        ],
        [
            "https://www.cwgc.org/our-work/news/"
            "thousands-of-indian-first-world-war-soldiers-commemorated-after-"
            "historical-omission/",
            "https://www.constitutionofindia.net/historical-constitution/"
            "the-congress-league-scheme-1916-inc-aiml/",
        ],
        "A 2026 Commonwealth War Graves Commission report records that 9,909 "
        "previously uncommemorated Indian Army servicemen were added to its "
        "records after the Punjab Registers project. This is used only as a "
        "public-memory bridge; it does not quantify wartime extraction or prove "
        "a nationalist causal claim.",
        "OCR checks use Bipan Chandra's India's Struggle for Independence, "
        "printed pages 141-152, and Modern India, approximately pages 254-258, "
        "for the two Leagues, repression, Lucknow and the transition. Sekhar "
        "Bandyopadhyay, especially pages 286-288 and the adjacent Home Rule "
        "discussion, supplies wartime-economic and regional qualification. The "
        "Congress-League Scheme transcription supplies the Pact's exact provisions.",
        "UPSC Prelims 2018 Q79 on the All India Home Rule League's 1920 "
        "renaming as Swarajya Sabha is retained as a routed demand card. The "
        "official answer key is unavailable locally, so no answer letter is inferred.",
        [
            (
                "Wartime loyalty and expectation",
                "At the First World War's outbreak, leading Indian nationalists "
                "supported Britain while expecting meaningful constitutional advance.",
            ),
            (
                "Wartime extraction",
                "India supplied soldiers, money and materials, while taxation, war "
                "loans, recruitment pressure, shortages and rising prices widened "
                "hardship, even as selected industries and traders gained wartime opportunities.",
            ),
            (
                "Democratic contradiction",
                "British wartime language about liberty and democracy sharpened the "
                "contradiction between imperial claims and colonial subjection.",
            ),
            (
                "Congress deadlock",
                "The Surat split and subsequent repression had weakened continuous "
                "Congress agitation before the wartime effort at reunion.",
            ),
            (
                "Moderate-Extremist reunion",
                "Congress authorised readmission of the Extremist current in December "
                "1915; the Lucknow Congress of December 1916 publicly consummated reunion.",
            ),
            (
                "Tilak's Home Rule League",
                "Tilak launched his Home Rule League in April 1916, working mainly "
                "in Maharashtra excluding Bombay city, Karnataka, the Central "
                "Provinces and Berar.",
            ),
            (
                "Besant's Home Rule League",
                "Annie Besant launched a separate Home Rule League in September 1916 "
                "from Adyar, with activity across most areas outside Tilak's zone, "
                "including Bombay city.",
            ),
            (
                "Besant's associates and press",
                "George Arundale, B.P. Wadia and C.P. Ramaswami Aiyar were prominent "
                "associates; New India and Commonweal supported Besant's propaganda.",
            ),
            (
                "Home Rule demand",
                "The Leagues demanded self-government within the British Empire on "
                "the Home Rule model, not immediate complete independence.",
            ),
            (
                "Home Rule methods",
                "Branches, lectures, pamphlets, newspapers, libraries and political "
                "classes made agitation continuous beyond annual Congress sessions.",
            ),
            (
                "Government repression",
                "Tilak faced security proceedings and territorial exclusion, students "
                "faced restrictions, and Annie Besant, B.P. Wadia and George Arundale "
                "were interned in June 1917, widening the civil-liberty issue.",
            ),
            (
                "Besant's Congress presidency",
                "After release from internment, Annie Besant became Congress president "
                "in 1917, marking the movement's political prestige.",
            ),
            (
                "Lucknow double unity",
                "Under Congress president Ambica Charan Mazumdar, Lucknow produced "
                "Congress reunion and a Congress-League agreement shaped by leaders "
                "including Tilak, Besant and Jinnah, despite Malaviya's opposition.",
            ),
            (
                "Joint constitutional demands",
                "The Scheme proposed four-fifths elected legislatures, a 150-member "
                "Imperial Legislative Council, greater Indian control, provincial "
                "fiscal authority and increased Indianisation of the executive.",
            ),
            (
                "Separate electorates",
                "Congress accepted separate electorates for Muslims at Lucknow; the "
                "device had already entered statute through the 1909 reforms.",
            ),
            (
                "Weightage and provincial ratios",
                "The Pact fixed Muslim shares at Punjab 50%, Bengal 40%, Bombay "
                "one-third, United Provinces 30%, Bihar 25%, and Central Provinces "
                "and Madras 15% each; one-third of elected Indian central members "
                "were to be Muslim.",
            ),
            (
                "Lucknow contradiction",
                "The Pact achieved real cooperation while making religious community "
                "an institutional unit of bargaining and protecting a community when "
                "three-fourths of its members opposed a measure affecting it.",
            ),
            (
                "Montagu Declaration",
                "The declaration of 20 August 1917 promised increasing Indian "
                "association and gradual responsible government, not immediate transfer.",
            ),
            (
                "Decline and absorption",
                "In 1918 moderate withdrawal, divisions over reform proposals, "
                "Besant's vacillation and Tilak's departure for England weakened the "
                "Leagues; Gandhi subsequently inherited parts of their political network.",
            ),
            (
                "Council safeguard mechanism",
                "Under the Pact, a measure affecting a community could not proceed "
                "when three-fourths of that community's council members opposed it, "
                "showing how political unity was mediated through communal safeguards.",
            ),
        ],
        [
            "Tilak's and Besant's Home Rule Leagues were separate organisations with "
            "different zones, not one jointly founded body.",
            "Home Rule meant self-government within the Empire, not Purna Swaraj.",
            "Lucknow achieved two forms of unity: Moderate-Extremist reunion and "
            "Congress-League cooperation.",
            "Separate electorates began in 1909; Congress accepted rather than invented "
            "them at Lucknow.",
            "Weightage and separate electorates are distinct devices; use the verified "
            "Pact ratios rather than approximations.",
            "The Montagu Declaration promised gradual responsible government, not its "
            "immediate grant.",
            "Home Rule's decline does not erase its role in cadre formation and political education.",
            "The CWGC figure is a 2026 commemoration fact, not a wartime extraction statistic.",
        ],
        [
            (
                10,
                "Why did the First World War convert nationalist loyalty into a demand "
                "for constitutional reward?",
                "Wartime support created an expectation of political reciprocity, while "
                "material pressure and imperial democratic rhetoric made continued "
                "subjection harder to defend.",
                [0, 1, 2, 17],
            ),
            (
                10,
                "Distinguish Tilak's and Annie Besant's Home Rule Leagues.",
                "They shared the demand for self-government and methods of political "
                "education, but remained separate bodies with different launch dates, "
                "territorial fields and organisational networks.",
                [5, 6, 7, 8, 9],
            ),
            (
                15,
                "Assess the Home Rule movement as an organisational bridge to "
                "Gandhian mass politics.",
                "The Leagues normalised continuous propaganda, branches and local "
                "activism through mainly educated and professional leadership, with "
                "uneven rural penetration; their demand remained narrower than later satyagraha.",
                [5, 6, 8, 9, 10, 18],
            ),
            (
                15,
                "Why is the Lucknow Session of 1916 described as an achievement of "
                "double unity?",
                "Lucknow repaired the Congress split and enabled a joint Congress-League "
                "scheme, but its unity depended on a contested communal-representation bargain.",
                [4, 12, 13, 14, 15, 16],
            ),
            (
                20,
                "Critically examine the Lucknow Pact as both a nationalist advance "
                "and a constitutional contradiction.",
                "The Pact concentrated anti-colonial bargaining power through a common "
                "programme, while separate electorates and negotiated weightage "
                "institutionalised community as the medium of representation.",
                [12, 13, 14, 15, 16],
            ),
            (
                20,
                "Trace the sequence from wartime mobilisation to the Montagu "
                "Declaration and the transition toward Gandhian politics.",
                "War generated expectation and pressure; Home Rule organised public "
                "demand; Lucknow widened unity; the bounded 1917 promise failed to "
                "settle the issue and activists entered a new mass-political phase.",
                [0, 1, 2, 9, 10, 12, 17, 18],
            ),
        ],
        [
            (
                "2018",
                "Prelims GS-I Q79",
                "Identify the organisation that changed its name to Swarajya Sabha in 1920.",
                "routed-key-unavailable",
                "The official question source records the All India Home Rule League "
                "among the options and the repository routing records its renaming as "
                "Swarajya Sabha. Because the official key is unavailable locally, no "
                "answer letter is published or inferred.",
            ),
            (
                "2024",
                "GS-I Q12",
                "How far is it correct to say that the First World War was fought "
                "essentially for the preservation of the balance of power?",
                "cross-cutting-world-history-model",
                "Treat balance of power as a major structural cause, then qualify it "
                "through alliance commitments, imperial rivalry, nationalism, arms "
                "competition and the July Crisis. Use it only to frame India's "
                "imperial war setting, not as a direct Home Rule question.",
            ),
        ],
        [
            "April 1916",
            "September 1916",
            "Bombay city",
            "George Arundale",
            "B.P. Wadia",
            "C.P. Ramaswami Aiyar",
            "New India",
            "Commonweal",
            "self-government within the British Empire",
            "June 1917",
            "Ambica Charan Mazumdar",
            "Jinnah",
            "double unity",
            "separate electorates",
            "weightage",
            "three-fourths",
            "20 August 1917",
            "9,909",
            "Punjab Registers",
            "Swarajya Sabha",
        ],
    ),
    base.topic(
        19,
        "Gandhi's Rise: Champaran, Kheda, Ahmedabad; Rowlatt & Jallianwala Bagh (1917–1919)",
        "19_Gandhis-Rise-Rowlatt-and-Jallianwala.md",
        "19_Gandhis-Rise-Rowlatt-and-Jallianwala.md",
        "19_Gandhis-Rise-Champaran-Kheda-Ahmedabad-Rowlatt-Jallianwala_Complete-Topic-Package.md",
        [
            "basic/07_Economic-Impact-of-British-Rule.md",
            "basic/18_WWI-Home-Rule-and-Lucknow-Pact.md",
            "basic/20_Non-Cooperation-and-Khilafat-Movement.md",
            "advanced/20_Non-Cooperation-and-Khilafat-Movement.md",
        ],
        [
            "https://www.pmindia.gov.in/en/news_updates/"
            "pm-pays-homage-to-the-martyrs-of-jallianwala-bagh-2/",
            "https://www.mkgandhi.org/autobio/chap147.php",
            "https://www.mkgandhi.org/autobio/chap161.php",
            "https://archive.org/details/rowlatt-act-proceedings-scanned-copy",
            "https://archive.org/details/dli.csl.209",
            "https://archive.org/details/reportofcommissi01indi",
        ],
        "The Prime Minister's 13 April 2026 official homage is retained only as "
        "a public-memory bridge for Jallianwala Bagh, liberty, justice and dignity. "
        "It does not replace historical evidence or supply disputed casualty totals.",
        "OCR checks use Bipan Chandra's India's Struggle for Independence around "
        "the Champaran, Ahmedabad, Kheda and Rowlatt chapters and Modern India for "
        "the 1919 transition. Sekhar Bandyopadhyay supplies wartime distress, the "
        "Ahmedabad relationship and wider political qualification. Gandhi's "
        "autobiography, the Rowlatt proceedings, Hunter report and Congress Punjab "
        "Inquiry are retained as primary or official documentary anchors.",
        "Routed demands include 2018 Prelims Q69 on Champaran, 2019 Prelims Q14 "
        "on Gandhi-linked events, 2020 Prelims Q14 on Gandhism and Marxism, "
        "2018 GS-I on Gandhi's thought, 2019 GS-I on many voices in the Gandhian "
        "phase and 2023 GS-I on Gandhi and Tagore. Missing Prelims keys are not inferred.",
        [
            (
                "South African formation",
                "Between 1893 and 1914 Gandhi developed satyagraha and institutions "
                "of disciplined community action in South Africa.",
            ),
            (
                "Return and Gokhale",
                "Gandhi returned to India in 1915 and followed Gopal Krishna Gokhale's "
                "advice to study Indian conditions before leading major campaigns.",
            ),
            (
                "Satyagraha",
                "Satyagraha joined truth, non-violence, voluntary self-suffering, "
                "openness and disciplined refusal of an unjust demand.",
            ),
            (
                "Champaran invitation",
                "Raj Kumar Shukla persistently brought Gandhi to Champaran in 1917, "
                "showing that local agency preceded national intervention.",
            ),
            (
                "Tinkathia grievance",
                "Champaran cultivators challenged tinkathia, which required indigo "
                "cultivation on 3/20 of a tenant's holding, and planter demands "
                "associated with release from that system.",
            ),
            (
                "Champaran inquiry and settlement",
                "Gandhi's team recorded about 8,000 cultivator statements; an official "
                "inquiry led to a 25% refund of illegal dues, while later abolition "
                "of tinkathia must be kept distinct from that refund.",
            ),
            (
                "Ahmedabad dispute",
                "In the 1918 Ahmedabad plague-bonus dispute, workers initially sought "
                "50%, owners offered 20%, and Gandhi supported a 35% wage increase.",
            ),
            (
                "Sarabhai relationship",
                "Anasuya Sarabhai supported the workers, while her brother Ambalal "
                "Sarabhai was a leading mill owner and Gandhi's associate.",
            ),
            (
                "Ahmedabad fast and arbitration",
                "After a twenty-one-day strike, Gandhi's three-day fast, his first in "
                "an Indian struggle, reinforced the pledge and pressed the dispute "
                "toward arbitration; sources differ on the final percentage outcome.",
            ),
            (
                "Kheda revenue issue",
                "The 1918 Kheda campaign sought suspension of land revenue where "
                "assessed produce was four annas or less, one-quarter of normal, under "
                "the government's own rules.",
            ),
            (
                "Kheda leadership",
                "Vallabhbhai Patel and Indulal Yagnik helped organise Kheda, showing "
                "that Gandhian action depended on local and regional leadership.",
            ),
            (
                "Kheda limit",
                "Kheda used a collective pledge so better-off cultivators would protect "
                "poorer neighbours from selective collection; attachment risks and "
                "a limited official retreat made the outcome partial rather than total.",
            ),
            (
                "Rowlatt Committee, Bills and Act",
                "Two Rowlatt Bills were introduced, but only one became the Anarchical "
                "and Revolutionary Crimes Act, 1919, on 18 March; it continued "
                "exceptional procedures and detention powers into peace.",
            ),
            (
                "Satyagraha Sabha",
                "Gandhi founded the Satyagraha Sabha in Bombay in February 1919, whose "
                "members pledged civil disobedience of the Rowlatt law.",
            ),
            (
                "Hartal and date correction",
                "The all-India hartal was observed on 6 April 1919; Delhi acted on the "
                "earlier date of 30 March, revealing communication and control problems.",
            ),
            (
                "Himalayan miscalculation",
                "Gandhi suspended the agitation on 18 April after violence exposed "
                "inadequate discipline and later described the premature call for "
                "mass civil disobedience as a Himalayan miscalculation.",
            ),
            (
                "Punjab arrests",
                "On 10 April Saifuddin Kitchlew and Satyapal were arrested and removed "
                "from Amritsar; firing on protestors and attacks on Europeans and "
                "property followed within a deeper wartime coercive setting.",
            ),
            (
                "Jallianwala Bagh",
                "On 13 April 1919 Brigadier-General Reginald Dyer ordered troops to "
                "fire without warning or an order to disperse on an unarmed gathering "
                "inside Jallianwala Bagh; he was not Lieutenant-Governor Michael O'Dwyer.",
            ),
            (
                "Martial law and inquiries",
                "Formal martial law followed the massacre and included humiliating "
                "punishments such as the crawling order in a specific Amritsar lane; "
                "the Hunter Committee and Congress Punjab Inquiry diverged sharply.",
            ),
            (
                "Moral repudiation and transition",
                "Tagore renounced his knighthood in 1919 and Gandhi returned the "
                "Kaiser-i-Hind medal in 1920; at the December 1919 Amritsar Congress "
                "Gandhi still treated the reforms as a workable basis, so the later "
                "turn to Non-Cooperation must remain multi-causal.",
            ),
        ],
        [
            "South Africa supplied a tested method, but its setting and scale were not identical to India.",
            "Champaran joined local agency to Gandhi's method; Raj Kumar Shukla must not disappear.",
            "Champaran concerned indigo and tinkathia; Ahmedabad concerned mill wages; "
            "Kheda concerned land-revenue remission.",
            "Ahmedabad's fast was Gandhi's first in India; Champaran was not a hunger-strike campaign.",
            "Kheda sought suspension under the four-anna rule, not abolition of land revenue.",
            "Two Rowlatt Bills were introduced, but only one became Act XI of 1919.",
            "The 6 April hartal and Delhi's action on 30 March must be distinguished.",
            "Do not publish a Jallianwala casualty total; official and Indian estimates diverge.",
            "The crawling order was a specific martial-law humiliation, not a description of all Punjab.",
            "Reginald Dyer ordered the firing; Michael O'Dwyer was Punjab's Lieutenant-Governor.",
            "Tagore's renunciation was in 1919; Gandhi returned Kaiser-i-Hind in 1920.",
            "Jallianwala contributed to Non-Cooperation alongside Khilafat, post-war distress "
            "and dissatisfaction with reforms; avoid monocausal history.",
        ],
        [
            (
                10,
                "Why was Champaran a methodological turning point in India's national movement?",
                "Champaran joined local peasant initiative, public inquiry, principled "
                "law-breaking and negotiated redress, giving Gandhi Indian credibility "
                "without yet becoming an all-India anti-state campaign.",
                [3, 4, 5],
            ),
            (
                10,
                "Compare Gandhi's roles in the Ahmedabad and Kheda struggles of 1918.",
                "Ahmedabad tested mediation, worker discipline, fasting and arbitration "
                "in an industrial dispute; Kheda tested organised revenue refusal and "
                "regional cadre leadership against the state.",
                [6, 7, 8, 9, 10, 11],
            ),
            (
                15,
                "Champaran, Ahmedabad and Kheda were laboratories of satyagraha rather "
                "than repetitions of one formula. Discuss.",
                "The three campaigns shared disciplined non-violence and fact-based "
                "negotiation but differed in constituency, grievance, opponent, tactic "
                "and settlement, allowing Gandhi to test a transferable repertoire.",
                [2, 3, 4, 5, 6, 8, 9, 10, 11],
            ),
            (
                15,
                "How did the Rowlatt agitation reveal both the reach and the limits of "
                "Gandhi's early all-India leadership?",
                "The Satyagraha Sabha and hartal displayed nationwide moral appeal, "
                "while date confusion, violence and withdrawal showed that popularity "
                "had outrun organisational discipline.",
                [12, 13, 14, 15],
            ),
            (
                20,
                "Analyse the political significance of Jallianwala Bagh and the Punjab "
                "martial-law regime without reducing nationalism to one event.",
                "The massacre, humiliating martial-law measures, contested inquiries "
                "and renunciation of honours destroyed confidence in imperial justice, "
                "but operated alongside wartime pressure, Rowlatt and Khilafat.",
                [16, 17, 18, 19],
            ),
            (
                20,
                "Explain Gandhi's rise between 1915 and 1919 as an interaction of "
                "method, local agency, organisation and colonial response.",
                "Gandhi adapted a South African method through local Indian campaigns, "
                "built credibility with regional collaborators, attempted national "
                "mobilisation and learned from repression and uncontrolled violence.",
                [0, 1, 2, 3, 7, 10, 13, 15, 17, 19],
            ),
        ],
        [
            (
                "2018",
                "Prelims GS-I Q69",
                "Identify the significant aspect of the Champaran Satyagraha.",
                "routed-key-unavailable",
                "Retain the official stem as a significance and close-option "
                "distinction card. Use the Champaran sessions to compare local agency, "
                "agrarian grievance, inquiry and national political significance, but "
                "do not select or publish an answer option without the official key.",
            ),
            (
                "2020",
                "Prelims GS-I Q14",
                "Identify a common point between Gandhism and Marxism.",
                "routed-key-unavailable",
                "Retain the official stem as a comparison demand. Review possible common "
                "ground and differences in class struggle, violence, property and the "
                "state, but do not select or publish an answer option without the "
                "official key.",
            ),
            (
                "2019",
                "Prelims GS-I Q14",
                "Assess statements linking Gandhi with indentured labour, wartime "
                "politics and later Civil Disobedience events.",
                "cross-cutting-routed-key-unavailable",
                "Use this as a chronology and association card extending beyond "
                "1917-19. The local official question is present, but no answer "
                "letter is inferred because the official key is unavailable.",
            ),
            (
                "2018",
                "GS-I",
                "Throw light on the significance of Mahatma Gandhi's thoughts in the present times.",
                "bounded-model",
                "Organise the answer around non-violence, means-and-ends, dignity of "
                "labour, decentralisation, trusteeship and ethical public action; apply "
                "each principle to a present problem and qualify tensions of scale and power.",
            ),
            (
                "2019",
                "GS-I Q11",
                "Many voices had strengthened and enriched the nationalist movement "
                "during the Gandhian phase. Elaborate.",
                "cross-cutting-bounded-model",
                "Treat Gandhi's leadership as a framework within which peasants, "
                "workers, women, socialists, regional organisers and marginalised "
                "groups acted with their own interests and political languages.",
            ),
            (
                "2023",
                "GS-I",
                "What was the difference between Mahatma Gandhi and Rabindranath Tagore "
                "in their approach towards education and nationalism?",
                "cross-cutting-bounded-model",
                "Both criticised alienating colonial education. Gandhi stressed "
                "productive work, vernacular learning and self-reliance; Tagore stressed "
                "freedom, nature, creativity and cosmopolitan humanism. Avoid turning "
                "difference into absolute opposition.",
            ),
        ],
        [
            "Raj Kumar Shukla",
            "tinkathia",
            "Anasuya Sarabhai",
            "Ambalal Sarabhai",
            "first fast",
            "arbitration",
            "Indulal Yagnik",
            "Satyagraha Sabha",
            "6 April 1919",
            "Himalayan miscalculation",
            "Saifuddin Kitchlew",
            "Satya Pal",
            "13 April 1919",
            "crawling order",
            "Hunter Committee",
            "Kaiser-i-Hind",
        ],
    ),
]


SESSION_PLANS: dict[str, list[tuple[str, str, list[str], str, str]]] = {
    "modern-indian-history-18": [
        (
            "War, chronology and the transition problem",
            "The period 1914-18 links wartime loyalty and extraction to Home Rule, "
            "Lucknow unity, a bounded imperial promise and the threshold of Gandhian politics.",
            [
                "Tilak's June 1914 release and Congress's December 1915 readmission decision precede the two separate Leagues of 1916.",
                "Lucknow in December 1916 publicly consummates Congress reunion and Congress-League bargaining.",
                "Tilak's 1916-17 security and exclusion proceedings and the June 1917 internments precede the Montagu Declaration.",
                "The July 1918 reform proposals and Tilak's late-1918 departure for England help explain organisational decline.",
            ],
            "Do not read every event as an inevitable step toward Gandhi or independence.",
            "Use a chronological thesis that identifies both continuity and changing political scale.",
        ),
        (
            "Wartime loyalty, extraction and expectation",
            "Indian wartime support created a claim to constitutional reciprocity, "
            "while coercive extraction made loyalism increasingly difficult to sustain.",
            [
                "The Raj drew soldiers, money and materials from India for an imperial war.",
                "Recruitment pressure, taxes, war loans, shortages and price rises distributed costs unequally.",
                "Selected industries and traders also gained from import disruption and wartime demand.",
                "Nationalist support was political and conditional rather than proof of permanent consent.",
            ],
            "Avoid unsupported troop, revenue, inflation or casualty totals.",
            "Build the mechanism as contribution plus expectation minus adequate reward.",
        ),
        (
            "The democratic contradiction of empire",
            "Wartime claims about democracy and liberty supplied nationalists with a "
            "language for exposing the contradiction of colonial government.",
            [
                "The ideological claim did not by itself create agitation; material pressure and organisation mattered.",
                "Self-government became a more legitimate public demand during the imperial crisis.",
                "The war internationalised political vocabulary without granting self-determination to India.",
            ],
            "Do not treat European wartime rhetoric as a binding promise already made to India.",
            "Use ideology as an enabling argument joined to pressure, organisation and political choice.",
        ),
        (
            "Congress deadlock and Moderate-Extremist reunion",
            "Home Rule developed against the weakness left by Surat, repression and "
            "intermittent Congress politics, making reunion a condition of wider action.",
            [
                "Tilak's June 1914 release strengthened the campaign for readmission.",
                "Congress authorised readmission in December 1915 as resistance to reunion weakened.",
                "The Lucknow Congress publicly consummated cooperation without erasing ideological differences.",
            ],
            "Reunion was a negotiated political repair, not proof that the Surat conflict had never mattered.",
            "Explain why organisational unity enlarged leverage under wartime conditions.",
        ),
        (
            "Tilak's Home Rule League",
            "Tilak's April 1916 League converted constitutional self-government into "
            "a sustained regional campaign through vernacular communication and local organisation.",
            [
                "Its principal field covered Maharashtra excluding Bombay city, Karnataka, the Central Provinces and Berar.",
                "Meetings, tours, pamphlets and local branches carried politics beyond Congress sessions.",
                "Tilak defended a broad territorial nationalism rather than a secret revolutionary programme.",
            ],
            "Do not merge Tilak's League with Besant's organisation or label it a clandestine society.",
            "Match founder, date, zone, method and constitutional demand.",
        ),
        (
            "Annie Besant's Home Rule League",
            "Besant's September 1916 League used Theosophical, journalistic and "
            "political networks to extend Home Rule across most areas outside Tilak's zone.",
            [
                "Adyar and Madras were central organisational anchors.",
                "George Arundale, B.P. Wadia and C.P. Ramaswami Aiyar were important associates.",
                "New India and Commonweal connected public argument to branch-building and lectures.",
                "Her field included Bombay city and most areas outside Tilak's assigned zone.",
            ],
            "Besant's League was separate from Tilak's even when the two cooperated.",
            "Use organisation, territorial complementarity, associates and press as one evidence cluster.",
        ),
        (
            "Two Leagues, territorial division and shared demand",
            "The two Leagues divided fields of work to reduce rivalry while sharing "
            "the demand for Home Rule within the Empire.",
            [
                "Tilak concentrated in Maharashtra excluding Bombay city, Karnataka, the Central Provinces and Berar.",
                "Besant worked through a wider all-India field that included Bombay city.",
                "Both treated political education and recurring local activity as organisational necessities.",
                "Neither made immediate complete independence its formal demand.",
            ],
            "Territorial complementarity did not make the Leagues one organisation.",
            "A comparison answer should use the same axes: launch, area, network, medium and demand.",
        ),
        (
            "Political education, press and branch methods",
            "Home Rule's organisational novelty lay in continuous political education "
            "through print, speech, local branches and repeat contact.",
            [
                "Pamphlets simplified constitutional demands for wider audiences.",
                "Newspapers and lecture tours sustained attention between annual Congress meetings.",
                "Libraries, discussion circles and branches created local workers, though reach remained socially uneven.",
            ],
            "Do not equate a wider public sphere with full peasant-worker mass mobilisation.",
            "Use method to explain why a limited demand could have a larger organisational legacy.",
        ),
        (
            "Repression and Besant's internment",
            "Government repression transformed Home Rule from a constitutional demand "
            "into a civil-liberty issue and enlarged sympathy for Besant.",
            [
                "Tilak faced security proceedings in 1916 and later exclusion from Punjab and Delhi.",
                "Students faced restrictions, and Besant was subjected to territorial restraint in November 1916.",
                "Annie Besant, B.P. Wadia and George Arundale were interned in June 1917.",
                "Protest over internment widened support, and her later Congress presidency marked enhanced prestige.",
            ],
            "Repression stimulated sympathy but did not by itself create every later nationalist gain.",
            "Show the feedback loop from restriction to publicity, coalition and political cost.",
        ),
        (
            "Lucknow Session and double unity",
            "The December 1916 Lucknow Session achieved two settlements at once: "
            "Moderate-Extremist reunion and Congress-League constitutional cooperation.",
            [
                "Ambica Charan Mazumdar presided over the Congress session.",
                "Tilak and Besant promoted rapprochement, while Jinnah helped bridge the two organisations.",
                "Malaviya opposed the communal-representation bargain.",
                "The two forms of unity had different actors, histories and institutional consequences.",
            ],
            "Do not reduce double unity to a vague slogan of Hindu-Muslim harmony.",
            "State each unity separately before assessing their combined bargaining value.",
        ),
        (
            "The Pact's joint constitutional programme",
            "The Lucknow Pact sought wider representation and Indian authority through "
            "a common programme that increased pressure on the colonial state.",
            [
                "The Scheme proposed four-fifths elected members in provincial and Imperial legislatures.",
                "It proposed a 150-member Imperial Legislative Council and one-third Muslim representation among elected Indian members.",
                "It sought provincial fiscal authority, greater Indian participation in the executive and reduced Secretary-of-State control.",
                "The agreement made inter-organisational bargaining more credible during wartime.",
                "Its constitutional content remained short of sovereignty or immediate responsible government.",
            ],
            "Do not project the later demand for complete independence into the 1916 programme.",
            "Distinguish common demand, bargaining leverage and the limits of the constitutional horizon.",
        ),
        (
            "Separate electorates, weightage and provincial logic",
            "The Pact organised Muslim representation through separate electorates and "
            "negotiated provincial weightage, making community a constitutional category.",
            [
                "Separate electorates had already been introduced under the 1909 reforms.",
                "Weightage concerns the share of representation, not the identity of the electorate.",
                "The verified shares were Punjab 50%, Bengal 40%, Bombay one-third, United Provinces 30%, Bihar 25%, and 15% each in the Central Provinces and Madras.",
                "At the centre, one-third of elected Indian members were to be Muslim.",
            ],
            "Never confuse separate electorate, reserved representation and weightage; attribute the ratios to the 1916 Scheme.",
            "Explain the institutional mechanism before evaluating its political consequences.",
        ),
        (
            "Significance and contradiction of Lucknow",
            "Lucknow concentrated nationalist pressure while embedding a communal "
            "representation bargain whose tactical gain and long-term risk must be held together.",
            [
                "The common programme demonstrated that Congress-League cooperation was possible.",
                "The Pact also recognised political communities through negotiated representation.",
                "A measure affecting a community could be blocked when three-fourths of that community's council members opposed it.",
                "Later communal outcomes were not inevitable, but the institutional precedent mattered.",
            ],
            "Avoid both celebratory unity without cost and deterministic claims that the Pact caused Partition.",
            "Use a two-column evaluation: immediate leverage against institutional contradiction.",
        ),
        (
            "Montagu Declaration as a bounded sequel",
            "The declaration of 20 August 1917 acknowledged responsible government as "
            "a gradual imperial objective without conceding immediate popular sovereignty.",
            [
                "It followed wartime need, Home Rule pressure and wider nationalist unity.",
                "Increasing Indian association and gradual responsible government were the stated direction.",
                "Executive discretion, gradualism and imperial membership bounded the promise.",
            ],
            "Do not describe the Declaration as responsible government granted in 1917.",
            "Present it as a constitutional ratchet and an inadequate response, not a complete settlement.",
        ),
        (
            "Decline, absorption, public memory and PYQ route",
            "Home Rule declined as a separate movement but transferred cadres, methods "
            "and expectations into the Gandhian phase; its wartime setting also survives in public memory.",
            [
                "Moderate withdrawal after Besant's release and the reform promise narrowed the agitation.",
                "Divisions over the July 1918 reform proposals and Besant's vacillation weakened unity.",
                "Tilak's late-1918 departure for England deprived the movement of a principal organiser.",
                "Branch work and political education later remained useful to Congress mobilisation under Gandhi.",
                "The 2018 Q79 renaming card is retained without inventing an official key.",
                "The 2026 CWGC report adds 9,909 previously uncommemorated servicemen after the Punjab Registers project.",
            ],
            "Use the CWGC report only for memory and archival recovery, not as proof of Home Rule causation.",
            "Conclude with a bridge thesis: organisational absorption can coexist with historical significance.",
        ),
    ],
    "modern-indian-history-19": [
        (
            "South Africa, return in 1915 and Gokhale's counsel",
            "Gandhi entered Indian politics with a tested South African method but "
            "deliberately studied Indian conditions after returning in 1915.",
            [
                "South Africa supplied experience of racial law, association, negotiation and disciplined resistance.",
                "Gokhale advised Gandhi to travel and understand India before initiating large campaigns.",
                "The Indian setting required adaptation rather than mechanical transfer.",
            ],
            "Do not narrate South Africa as identical in constituency, law or scale to India.",
            "Use it as bounded formation, followed by observation and adaptation.",
        ),
        (
            "Satyagraha principles and political mechanism",
            "Satyagraha made truthful, open and non-violent law-breaking effective "
            "through discipline, voluntary suffering and an appeal to public legitimacy.",
            [
                "The satyagrahi accepted punishment rather than coercing an opponent through violence.",
                "Investigation and negotiation preceded escalation in Gandhi's early Indian campaigns.",
                "Non-violence required organisation and restraint; it was not mere passivity.",
            ],
            "Do not translate satyagraha as passive resistance or as moral feeling without organisation.",
            "Explain the mechanism linking self-suffering, legitimacy, participation and bargaining pressure.",
        ),
        (
            "Champaran: Raj Kumar Shukla, tinkathia and local agency",
            "Champaran began from a specific indigo grievance and the persistence of "
            "local actors who brought Gandhi into an existing agrarian conflict.",
            [
                "Raj Kumar Shukla pressed Gandhi to visit Champaran in 1917.",
                "Tinkathia required indigo cultivation on 3/20 of a tenant's holding.",
                "Planter demands around release from indigo obligations intensified the dispute.",
                "Gandhi defied an order to leave, and volunteers recorded about 8,000 cultivator statements.",
                "An official inquiry led to a 25% refund; later abolition of tinkathia was a separate outcome.",
            ],
            "Do not erase peasant and local initiative by presenting Gandhi as the source of the grievance.",
            "Open with local agency, then distinguish grievance, inquiry, refund and later abolition.",
        ),
        (
            "Wartime hardship and the reform-repression contradiction",
            "Gandhi's rise occurred amid wartime inflation, scarcity, epidemic distress "
            "and the contradiction between reform promises and continuing coercion.",
            [
                "Consumers, workers and many peasants faced rising prices and falling real purchasing power.",
                "Scarcity and epidemic distress widened social vulnerability, though some industries gained.",
                "The 1917 promise of gradual responsible government raised political expectations.",
                "Rowlatt coercion in 1919 made reform and repression appear simultaneously.",
            ],
            "Do not reduce Gandhi's rise to charisma or Jallianwala alone.",
            "Use social strain plus political expectation plus coercive breach as the national setting.",
        ),
        (
            "Ahmedabad: plague bonus, wages and the Sarabhai relationship",
            "The Ahmedabad dispute joined a plague-bonus and wage conflict to a dense "
            "relationship among workers, Anasuya Sarabhai, Ambalal Sarabhai and Gandhi.",
            [
                "Workers initially sought a 50% increase, owners offered 20%, and Gandhi supported 35%.",
                "Anasuya Sarabhai supported labour organisation.",
                "Her brother Ambalal Sarabhai was a leading mill owner and Gandhi's associate.",
                "The family relationship illustrates cross-class mediation without erasing conflict.",
            ],
            "Do not turn personal friendship or kinship into proof that labour and capital interests were identical.",
            "Use the relationship to analyse mediation, access and the ethical pressure available to Gandhi.",
        ),
        (
            "Ahmedabad: first Indian fast, pledge and arbitration",
            "Gandhi's first fast in an Indian struggle sought to reinforce worker "
            "discipline and move a stalled dispute toward arbitration.",
            [
                "The strike depended on a pledge and continued non-violent discipline.",
                "The strike lasted twenty-one days and Gandhi's fast lasted three days.",
                "The fast placed moral pressure on a relationship in which Gandhi knew leading mill owners.",
                "Arbitration supplied an institutional route out of confrontation.",
                "Bipan's 35% and Sekhar's 27.5% outcome figures are retained as a source discrepancy.",
            ],
            "A fast can create moral coercion; do not describe it as a neutral substitute for bargaining.",
            "Evaluate both organisational effect and ethical ambiguity.",
        ),
        (
            "Kheda: crop failure, revenue remission and leadership",
            "Kheda applied satyagraha to the colonial state's revenue demand when "
            "cultivators claimed crop conditions justified suspension or remission.",
            [
                "The demand invoked the rule permitting suspension when assessed produce was four annas or less.",
                "Vallabhbhai Patel and Indulal Yagnik helped organise villages and sustain communication.",
                "The pledge bound better-off cultivators to protect poorer neighbours from selective collection.",
                "Attachment risk and selective recovery made the settlement limited and uneven.",
            ],
            "Do not describe Kheda as an abolition-of-land-revenue movement or a complete victory.",
            "Connect the four-anna threshold, pledge, attachment risk, cadre work and selective relief.",
        ),
        (
            "Comparative anatomy of Champaran, Ahmedabad and Kheda",
            "The three campaigns shared disciplined negotiation but differed in social "
            "base, grievance, opponent, pressure technique and settlement.",
            [
                "Champaran involved cultivators against planter coercion and centred inquiry.",
                "Ahmedabad involved industrial workers and owners, with fasting and arbitration.",
                "Kheda involved cultivators against state revenue collection and organised withholding.",
                "Together they built credibility without constituting a single uniform model.",
            ],
            "Do not force one tactic or one type of victory onto all three campaigns.",
            "A comparison matrix is stronger than three disconnected narratives.",
        ),
        (
            "Rowlatt Committee, Bills and Act",
            "Two Rowlatt Bills attempted to continue extraordinary wartime powers "
            "into peace; only one became Act XI of 1919 on 18 March.",
            [
                "The committee examined revolutionary activity and recommended continued coercive powers.",
                "The enacted measure enabled detention and exceptional procedures outside ordinary safeguards.",
                "Its timing after wartime sacrifice and the 1917 reform promise intensified the sense of betrayal.",
            ],
            "Do not convert two introduced Bills into two enacted Acts or confuse Rowlatt with constitutional reform.",
            "Frame the issue as emergency power normalised after the emergency.",
        ),
        (
            "Satyagraha Sabha, 6 April hartal and Delhi mismatch",
            "The Satyagraha Sabha organised pledged resistance, while the hartal "
            "revealed both Gandhi's all-India reach and weak communications control.",
            [
                "Gandhi founded the Sabha in Bombay in February 1919.",
                "Its members pledged to disobey the Rowlatt law and accept punishment.",
                "The final all-India hartal date was 6 April 1919.",
                "Delhi observed the earlier announced date of 30 March, exposing coordination risk.",
            ],
            "Do not erase the date mismatch or present the hartal as uniformly controlled.",
            "Use organisation, pledge, communication and mobilisation as separate analytical layers.",
        ),
        (
            "Violence and the Himalayan miscalculation",
            "Violence during the agitation showed that moral appeal could mobilise "
            "faster than disciplined non-violence could be organised.",
            [
                "Disturbances and attacks broke Gandhi's intended method in several places.",
                "Gandhi suspended the agitation on 18 April rather than treating any mobilisation as success.",
                "His Himalayan-miscalculation judgement became a lesson about training and control.",
            ],
            "Do not treat withdrawal as proof that the agitation had no political reach.",
            "Balance nationwide resonance against the organisational failure to regulate action.",
        ),
        (
            "Punjab context and the arrests of Kitchlew and Satya Pal",
            "Amritsar's crisis developed within Punjab's wartime recruitment, coercion "
            "and political repression, then sharpened with the removal of local leaders.",
            [
                "Punjab bore intense wartime administrative and recruitment pressure.",
                "Saifuddin Kitchlew and Satya Pal were prominent local leaders.",
                "Their arrest and removal from Amritsar on 10 April intensified protest.",
                "Firing on protestors and attacks on Europeans and property followed.",
            ],
            "Do not begin the Punjab story only at the moment Dyer entered Jallianwala Bagh.",
            "Establish structural pressure, local leadership and immediate trigger before the massacre.",
        ),
        (
            "Jallianwala Bagh: enclosed space, Dyer and firing",
            "On 13 April 1919 Dyer used organised military fire against an unarmed "
            "gathering in an enclosed site, making colonial violence nationally legible.",
            [
                "The gathering occurred at Jallianwala Bagh in Amritsar on Baisakhi.",
                "Restricted exits and the enclosed ground magnified the danger.",
                "Brigadier-General Reginald Dyer ordered firing without warning or first ordering dispersal.",
                "Reginald Dyer must not be confused with Lieutenant-Governor Michael O'Dwyer.",
                "Official and Indian casualty estimates diverge, so this package states no total.",
            ],
            "Do not invent casualty totals or state that every exit was literally sealed by troops.",
            "Use date, place, spatial vulnerability, command decision and evidentiary caution.",
        ),
        (
            "Martial law, crawling order and competing inquiries",
            "The massacre preceded formal martial law, whose later humiliations were "
            "followed by official and nationalist investigations with divergent judgements.",
            [
                "Formal martial law was proclaimed after 13 April and extended coercive controls beyond the Bagh.",
                "The crawling order applied to a specific Amritsar lane and must be described with that qualification.",
                "The Hunter Committee was appointed in October 1919; its majority and Indian minority differed.",
                "The Congress Punjab Inquiry produced a more severe assessment of responsibility and repression.",
                "Reports and Dyer's formal consequences largely belong to 1920.",
            ],
            "Do not generalise the crawling order to all Punjab or treat Hunter as a shared national verdict.",
            "Separate event, martial-law regime, official inquiry and Indian counter-inquiry.",
        ),
        (
            "Moral repudiation, consequences and Non-Cooperation bridge",
            "Punjab wrongs accelerated the withdrawal of moral consent and helped make "
            "Non-Cooperation credible, without alone causing the 1920 movement.",
            [
                "Tagore renounced his knighthood in 1919.",
                "Gandhi returned the Kaiser-i-Hind medal in 1920.",
                "At the December 1919 Amritsar Congress, Gandhi still treated the reforms as a workable basis despite defects.",
                "C.R. Das favoured rejection, and the session reached a compromise.",
                "Rowlatt and Punjab joined Khilafat, post-war distress and disappointment with reforms.",
                "The routed 2018 and 2020 Prelims cards retain no inferred answer letters.",
                "The 2018 and 2023 GS-I demands extend Gandhian thought into present and educational debates.",
            ],
            "Do not make Jallianwala the single cause of Non-Cooperation or merge the dates of renunciation.",
            "Conclude with a multi-causal bridge from local credibility to national withdrawal of cooperation.",
        ),
    ],
}


SESSION_VISUALS = {
    "War, chronology and the transition problem": """JUN 1914 TILAK RELEASE -> DEC 1915 READMISSION AUTHORISED
APR-SEP 1916 TWO LEAGUES -> DEC 1916 LUCKNOW
1917 SECURITY / INTERNMENT -> 20 AUG DECLARATION
JUL-LATE 1918 REFORM DIVISION + TILAK ABROAD -> DECLINE""",
    "Wartime loyalty, extraction and expectation": """INDIAN SUPPORT -> soldiers + money + materials
        |                         |
 EXPECTED REFORM          TAX / LOAN / RECRUITMENT / SHORTAGE
        |                         |
        +---- reciprocity gap ----+ -> ASSERTIVE POLITICAL DEMAND""",
    "The democratic contradiction of empire": """BRITISH WAR CLAIM: liberty / democracy
                    versus
INDIAN CONDITION: colonial subjection / coercive extraction
                    |
        NATIONALIST ARGUMENT FOR SELF-GOVERNMENT""",
    "Congress deadlock and Moderate-Extremist reunion": """1907 SURAT SPLIT -> REPRESSION + WEAK CONTINUOUS ACTION
JUN 1914 TILAK RELEASE -> DEC 1915 READMISSION AUTHORISED
                           |
DEC 1916 LUCKNOW -> PUBLIC REUNION WITHOUT IDEOLOGICAL UNIFORMITY""",
    "Tilak's Home Rule League": """APRIL 1916 | TILAK
ZONE -> Maharashtra except Bombay city + Karnataka + C.P. + Berar
METHOD -> vernacular tours + pamphlets + meetings + branches
DEMAND -> constitutional Home Rule; not secret revolutionary action""",
    "Annie Besant's Home Rule League": """SEPTEMBER 1916 | ADYAR / MADRAS
NETWORK -> Besant + Arundale + Wadia + C.P. Ramaswami Aiyar
PRESS -> New India + Commonweal
FIELD -> most regions outside Tilak's zone, including Bombay city""",
    "Two Leagues, territorial division and shared demand": """AXIS          TILAK LEAGUE             BESANT LEAGUE
launch        April 1916              September 1916
field         west / central          wider complementary area
network       regional-vernacular     press / Theosophical links
shared goal   self-government within the British Empire""",
    "Political education, press and branch methods": """NEWSPAPER -> PAMPHLET -> LECTURE -> LOCAL BRANCH
     |             |            |             |
 public claim   simple case   repeat contact   local worker
     +------------- CONTINUOUS POLITICAL EDUCATION -------------+""",
    "Repression and Besant's internment": """TILAK SECURITY CASE / EXCLUSION + STUDENT RESTRICTIONS
                         |
NOV 1916 RESTRAINT -> JUN 1917 BESANT, WADIA, ARUNDALE INTERNED
                         |
PROTEST -> RELEASE + BESANT'S 1917 CONGRESS PRESIDENCY""",
    "Lucknow Session and double unity": """DECEMBER 1916 | PRESIDENT: AMBICA CHARAN MAZUMDAR
      +----------------------+----------------------+
      |                                             |
CONGRESS REUNION                              CONGRESS-LEAGUE PACT
Moderate + Extremist                    Tilak / Besant / Jinnah bridge
      +---------------- DOUBLE UNITY ---------------+""",
    "The Pact's joint constitutional programme": """COMMON PLATFORM
   -> four-fifths elected legislatures
   -> 150-member Imperial Council
   -> provincial finance + Indianised executives
BOUNDARY -> neither sovereignty nor immediate responsible government""",
    "Separate electorates, weightage and provincial logic": """MUSLIM SHARES -> Punjab 50 | Bengal 40 | Bombay 1/3 | U.P. 30
                 Bihar 25 | C.P. 15 | Madras 15
CENTRE -> one-third of elected Indian members
SAFEGUARD -> three-fourths community opposition blocks a measure
RULE -> electorate, weightage and veto are different mechanisms""",
    "Significance and contradiction of Lucknow": """IMMEDIATE GAIN                 INSTITUTIONAL COST
joint bargaining power     |     community-coded representation
temporary cooperation      |     separate electorate accepted
                  GRADED VERDICT
real nationalist advance without deterministic Partition claim""",
    "Montagu Declaration as a bounded sequel": """PRESSURE: war + Home Rule + Lucknow
                    |
20 AUG 1917 -> gradual responsible government announced
                    |
BOUNDARIES -> gradualism + executive control + Empire retained""",
    "Decline, absorption, public memory and PYQ route": """1918 -> MODERATE EXIT + REFORM DIVISION + BESANT VACILLATION
TILAK IN ENGLAND -> principal organiser absent
BRANCHES + CADRES -> later Gandhian mass-political bridge
2018 Q79 -> Swarajya Sabha route; no inferred answer letter
2026 CWGC -> 9,909 names added to records; memory bridge only""",
    "South Africa, return in 1915 and Gokhale's counsel": """1893-1914 SOUTH AFRICA -> tested satyagraha repertoire
1915 RETURN -> GOKHALE'S COUNSEL -> travel / observe / learn
INDIAN ADAPTATION -> local grievance + local leadership + disciplined action""",
    "Satyagraha principles and political mechanism": """TRUTH + OPENNESS + NON-VIOLENCE + SELF-SUFFERING
                         |
                  DISCIPLINED REFUSAL
                         |
PUBLIC LEGITIMACY -> COST OF REPRESSION -> NEGOTIATION""",
    "Champaran: Raj Kumar Shukla, tinkathia and local agency": """LOCAL GRIEVANCE -> TINKATHIA = 3/20 OF HOLDING
LOCAL AGENT -> RAJ KUMAR SHUKLA
                         |
GANDHI INVITED -> OPEN DEFIANCE -> ABOUT 8,000 STATEMENTS
                         |
OFFICIAL INQUIRY -> 25% REFUND -> LATER TINKATHIA ABOLITION""",
    "Wartime hardship and the reform-repression contradiction": """WAR PRESSURE -> prices + scarcity + declining real purchasing power
EPIDEMIC DISTRESS -> wider social vulnerability
1917 REFORM PROMISE -> political expectation rises
1919 ROWLATT -> exceptional coercion continues
RESULT -> material strain and political betrayal reinforce each other""",
    "Ahmedabad: plague bonus, wages and the Sarabhai relationship": """WORKERS SEEK 50% <- plague-bonus dispute -> OWNERS OFFER 20%
   |                                         |
ANASUYA SARABHAI                       AMBALAL SARABHAI
   +----------- GANDHI SUPPORTS 35% ----------+
KINSHIP / FRIENDSHIP ENABLE ACCESS; THEY DO NOT ERASE CONFLICT""",
    "Ahmedabad: first Indian fast, pledge and arbitration": """WORKER PLEDGE -> 21-DAY STRIKE -> STALEMATE
                                      |
                      GANDHI'S THREE-DAY FAST
                                      |
                               ARBITRATION ROUTE
SOURCE CAUTION -> final award reported as 35% or 27.5%""",
    "Kheda: crop failure, revenue remission and leadership": """CROP FAILURE -> FOUR ANNAS OR LESS -> SUSPENSION CLAIM
                         |
PATEL + INDULAL YAGNIK -> VILLAGE ORGANISATION
                         |
PLEDGE + ATTACHMENT RISK -> SELECTIVE / LIMITED RELIEF""",
    "Comparative anatomy of Champaran, Ahmedabad and Kheda": """CAMPAIGN     BASE          OPPONENT       MAIN METHOD
Champaran   cultivators   planters       inquiry + defiance
Ahmedabad   mill workers  mill owners    pledge + fast + arbitration
Kheda       cultivators   revenue state  organised withholding
COMMON -> discipline and negotiation | DIFFERENCE -> grievance and leverage""",
    "Rowlatt Committee, Bills and Act": """WARTIME EMERGENCY POWERS
          | committee recommends continuation
          v
TWO BILLS -> ONE BECOMES ACT XI ON 18 MARCH 1919
          |
DETENTION / EXCEPTIONAL PROCEDURE IN PEACETIME
          |
REFORM EXPECTATION + REPRESSION -> BETRAYAL FRAME""",
    "Satyagraha Sabha, 6 April hartal and Delhi mismatch": """FEB 1919 SATYAGRAHA SABHA -> pledge to disobey
DATE CHANGES -> DELHI ACTS ON 30 MARCH
6 APRIL -> ALL-INDIA HARTAL
RESULT -> national reach + communication / discipline problem""",
    "Violence and the Himalayan miscalculation": """MORAL APPEAL -> RAPID MOBILISATION
                         |
             ORGANISATION LAGS BEHIND
                         |
VIOLENCE -> 18 APRIL SUSPENSION -> 'HIMALAYAN MISCALCULATION'
LESSON -> train discipline before mass civil disobedience""",
    "Punjab context and the arrests of Kitchlew and Satya Pal": """WARTIME PUNJAB -> recruitment + coercion + repression
                              |
LOCAL LEADERS -> KITCHLEW + SATYAPAL
                              |
10 APRIL ARREST / REMOVAL -> FIRING, ATTACKS AND ESCALATION""",
    "Jallianwala Bagh: enclosed space, Dyer and firing": """13 APRIL 1919 | BAISAKHI | AMRITSAR
GATHERING -> ENCLOSED BAGH / RESTRICTED EXITS
                         |
REGINALD DYER -> NO WARNING / NO DISPERSAL ORDER -> FIRING
IDENTITY RULE -> DYER IS NOT LIEUTENANT-GOVERNOR MICHAEL O'DWYER
EVIDENCE RULE -> no disputed casualty total""",
    "Martial law, crawling order and competing inquiries": """13 APRIL MASSACRE -> FORMAL MARTIAL LAW FOLLOWS
                     |
specific Amritsar crawling order + other humiliations
                     |
HUNTER MAJORITY / INDIAN MINORITY <-> CONGRESS PUNJAB INQUIRY
                     |
          DIVERGENT JUDGEMENTS, MAINLY REPORTED IN 1920""",
    "Moral repudiation, consequences and Non-Cooperation bridge": """1919 TAGORE -> renounces knighthood
DEC 1919 AMRITSAR CONGRESS -> GANDHI / C.R. DAS DIFFER; COMPROMISE
1920 GANDHI -> returns Kaiser-i-Hind
PUNJAB WRONGS + KHILAFAT + DISTRESS + REFORM DISAPPOINTMENT
                         |
                 NON-COOPERATION BECOMES CREDIBLE""",
}


SESSION_DEFINITIONS = {
    "War, chronology and the transition problem": "A transition sequence linking imperial war, revived constitutional agitation, negotiated unity and an incomplete official response.",
    "Wartime loyalty, extraction and expectation": "Wartime reciprocity is the political expectation that extraordinary colonial support should produce a meaningful constitutional return.",
    "The democratic contradiction of empire": "The democratic contradiction is the gap between Britain's stated defence of liberty and its denial of self-government to colonial subjects.",
    "Congress deadlock and Moderate-Extremist reunion": "Congress reunion was the negotiated restoration of cooperation between currents divided at Surat, not the disappearance of their differences.",
    "Tilak's Home Rule League": "Tilak's League was the separately organised April 1916 constitutional campaign in Maharashtra except Bombay city, Karnataka, the Central Provinces and Berar.",
    "Annie Besant's Home Rule League": "Besant's League was the separately organised September 1916 campaign using Adyar, press and associational networks across the complementary field, including Bombay city.",
    "Two Leagues, territorial division and shared demand": "Territorial division means coordinated but distinct spheres of work under a shared Home Rule objective.",
    "Political education, press and branch methods": "Continuous agitation is recurring local political communication between annual national meetings.",
    "Repression and Besant's internment": "Internment is executive confinement without an ordinary criminal conviction, used here to restrict nationalist organisation.",
    "Lucknow Session and double unity": "Double unity means Congress internal reunion plus Congress-League constitutional cooperation at the same session.",
    "The Pact's joint constitutional programme": "A joint constitutional programme is a negotiated set of reform demands publicly advanced by separate political organisations.",
    "Separate electorates, weightage and provincial logic": "Separate electorate defines the voting body; weightage adjusts representation relative to population or political bargain.",
    "Significance and contradiction of Lucknow": "The Lucknow contradiction is that anti-colonial unity was strengthened through community-specific constitutional representation.",
    "Montagu Declaration as a bounded sequel": "A bounded concession recognises a direction of reform while limiting its pace, scope and transfer of authority.",
    "Decline, absorption, public memory and PYQ route": "Organisational absorption occurs when a movement loses separate momentum but transfers personnel, methods and demands into a successor phase.",
    "South Africa, return in 1915 and Gokhale's counsel": "Political adaptation is the transfer of a tested method into a new setting after observing its different laws, constituencies and grievances.",
    "Satyagraha principles and political mechanism": "Satyagraha is open, disciplined non-violent resistance grounded in truth and voluntary acceptance of suffering.",
    "Champaran: Raj Kumar Shukla, tinkathia and local agency": "Tinkathia required indigo cultivation on 3/20 of a tenant's holding; investigative satyagraha converted that local grievance into documented public negotiation.",
    "Wartime hardship and the reform-repression contradiction": "The reform-repression contradiction is the coexistence of rising constitutional expectations with continuing economic distress and exceptional coercion.",
    "Ahmedabad: plague bonus, wages and the Sarabhai relationship": "The Ahmedabad dispute was an industrial wage conflict shaped by the withdrawal or adjustment of a plague-related bonus.",
    "Ahmedabad: first Indian fast, pledge and arbitration": "Arbitration submits a dispute to an accepted adjudicatory process; the fast added moral pressure to reach that route.",
    "Kheda: crop failure, revenue remission and leadership": "Revenue remission or suspension is relief from collection under stated conditions, not abolition of the land-revenue system.",
    "Comparative anatomy of Champaran, Ahmedabad and Kheda": "Comparative anatomy tests campaigns on common axes: constituency, grievance, opponent, tactic, settlement and limitation.",
    "Rowlatt Committee, Bills and Act": "Post-war emergency normalisation is the continuation of exceptional wartime coercion after the emergency has ended; two Bills were introduced but only one became Act XI of 1919.",
    "Satyagraha Sabha, 6 April hartal and Delhi mismatch": "A hartal is a coordinated suspension of ordinary public and commercial activity used as political protest.",
    "Violence and the Himalayan miscalculation": "Himalayan miscalculation names Gandhi's judgement that mass civil disobedience had been called before adequate non-violent discipline existed.",
    "Punjab context and the arrests of Kitchlew and Satya Pal": "An immediate trigger is the proximate act that activates deeper structural tension; here it was the removal of local leaders amid wartime coercion.",
    "Jallianwala Bagh: enclosed space, Dyer and firing": "The massacre was commanded military firing on an unarmed gathering in a spatially confined public ground.",
    "Martial law, crawling order and competing inquiries": "Martial-law humiliation denotes punitive controls imposed on civilians beyond ordinary process, while inquiry divergence reflects contested accountability.",
    "Moral repudiation, consequences and Non-Cooperation bridge": "Withdrawal of moral consent is the public rejection of honours and cooperation once imperial authority is judged illegitimate.",
}


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-18": [
        (
            "Wartime-to-transition chronology",
            "chronology",
            """JUN 1914 -> Tilak released; wartime support and extraction begin
DEC 1915 -> Congress authorises Extremist readmission
APR-SEP 1916 -> Tilak and Besant create separate Leagues
DEC 1916 -> Lucknow publicly consummates double unity and Pact
1917 -> security action, internments and bounded Montagu promise
1918 -> reform division and Tilak's absence weaken the movement.""",
            ["War, chronology and the transition problem"],
        ),
        (
            "Loyalty, extraction and reciprocity gap",
            "causal-flow",
            """SUPPORT -> soldiers, money and materials
EXPECTATION -> constitutional reward after wartime loyalty
PRESSURE -> taxes, loans, recruitment, shortages and price rises
OFFSET -> selected industries and traders gain wartime opportunities
CONTRADICTION -> imperial liberty language versus colonial rule
GAP -> sacrifice is not matched by adequate political power
RESULT -> demand shifts from hopeful support to organised pressure.""",
            ["Wartime loyalty, extraction and expectation", "The democratic contradiction of empire"],
        ),
        (
            "Congress repair before renewed agitation",
            "problem-response",
            """1907 SURAT -> divided Congress
            JUN 1914 -> Tilak released
            DEC 1915 -> Congress authorises readmission
            WAR -> increases need for a united constitutional front
            DEC 1916 -> public reunion at Lucknow
LIMIT -> reunion restores cooperation, not ideological uniformity.""",
            ["Congress deadlock and Moderate-Extremist reunion"],
        ),
        (
            "Two Home Rule Leagues identity matrix",
            "comparison",
            """AXIS       TILAK                     BESANT
launch     April 1916                September 1916
field      Maharashtra except        most other areas,
           Bombay; Karnataka; C.P.    including Bombay city
network    regional workers          Arundale, Wadia, Ramaswami Aiyar
rule       separate organisations; shared constitutional demand.""",
            ["Tilak's Home Rule League", "Annie Besant's Home Rule League"],
        ),
        (
            "Home Rule demand and method",
            "process",
            """GOAL -> self-government within the British Empire
NOT GOAL -> immediate complete independence
PRESS -> New India, Commonweal and wider political journalism
CONTACT -> tours, lectures, pamphlets and public meetings
ORGANISATION -> branches, libraries and political classes
EFFECT -> continuous political education beyond annual sessions.""",
            ["Two Leagues, territorial division and shared demand", "Political education, press and branch methods"],
        ),
        (
            "Repression feedback loop",
            "feedback-loop",
            """            LEAGUE EXPANSION -> security cases, exclusions and student restrictions
            NOV 1916 -> Besant restricted
            JUNE 1917 -> Besant, Wadia and Arundale interned
            INTERNMENT -> civil-liberty protest and wider sympathy
RELEASE -> movement prestige rises
1917 -> Besant becomes Congress president.""",
            ["Repression and Besant's internment"],
        ),
        (
            "Lucknow double-unity map",
            "split-rail",
            """PRESIDENT -> Ambica Charan Mazumdar
TRACK A -> Moderates + Tilak's current achieve Congress reunion
TRACK B -> Congress + League adopt a joint constitutional scheme
BRIDGES -> Tilak, Besant and Jinnah; Malaviya dissents
MERGER POINT -> stronger wartime bargaining platform
CAUTION -> the two settlements carried different institutional costs.""",
            ["Lucknow Session and double unity"],
        ),
        (
            "Joint demand and constitutional ceiling",
            "boundary-map",
            """LEGISLATURES -> four-fifths elected
IMPERIAL COUNCIL -> proposed strength of 150
EXECUTIVE -> greater Indian participation
PROVINCES -> wider fiscal and internal authority
CEILING -> no immediate responsible government or sovereignty
VALUE -> common platform increases bargaining credibility.""",
            ["The Pact's joint constitutional programme"],
        ),
        (
            "Representation devices and provincial logic",
            "comparison",
            """PUNJAB 50 | BENGAL 40 | BOMBAY 1/3 | U.P. 30
BIHAR 25 | C.P. 15 | MADRAS 15
CENTRE -> one-third of elected Indian members
SAFEGUARD -> three-fourths community opposition blocks a measure
1909 -> separate electorates statutory; 1916 -> Congress accepts them
RULE -> electorate, weightage and veto are distinct mechanisms.""",
            ["Separate electorates, weightage and provincial logic"],
        ),
        (
            "Lucknow balance sheet",
            "balance-sheet",
            """GAIN -> Congress reunion
GAIN -> Congress-League common reform platform
GAIN -> concentrated pressure during wartime
COST -> communal category becomes a bargaining unit
COST -> separate electorates receive Congress acceptance
VERDICT -> real tactical advance with a durable contradiction.""",
            ["Significance and contradiction of Lucknow"],
        ),
        (
            "Montagu Declaration boundary ladder",
            "institution-map",
            """PRESSURE -> war needs + Home Rule + Lucknow unity
20 AUG 1917 -> responsible government stated as an objective
METHOD -> increasing Indian association
PACE -> gradual development
BOUNDARY -> executive discretion and imperial membership remain
SEQUEL -> promise opens, but does not settle, constitutional conflict.""",
            ["Montagu Declaration as a bounded sequel"],
        ),
        (
            "Absorption, memory and examination bridge",
            "transition-map",
            """            1918 DECLINE -> moderate exit + reform division + Besant vacillation
            TILAK ABROAD -> principal organiser absent
            TRANSFER -> cadres, branches and propaganda habits later aid Congress
            2018 Q79 -> 1920 Swarajya Sabha renaming route; key unavailable
            2026 CWGC -> Punjab Registers recover omitted servicemen
            VERIFIED FIGURE -> 9,909 names added to CWGC records
BOUNDARY -> commemoration evidence, not nationalist causal proof.""",
            ["Decline, absorption, public memory and PYQ route"],
        ),
    ],
    "modern-indian-history-19": [
        (
            "Formation-to-national-leadership chronology",
            "chronology",
            """1893-1914 -> South African formation of satyagraha
1915 -> return to India and Gokhale's counsel
1917 -> Champaran
1918 -> Ahmedabad and Kheda
FEB-APR 1919 -> Satyagraha Sabha and Rowlatt hartal
13 APR 1919 -> Jallianwala; repression reshapes national politics.""",
            ["South Africa, return in 1915 and Gokhale's counsel"],
        ),
        (
            "Satyagraha mechanism",
            "causal-flow",
            """TRUTH -> grievance must survive factual inquiry
OPENNESS -> law-breaking is declared, not concealed
NON-VIOLENCE -> opponent is pressured without physical injury
SELF-SUFFERING -> satyagrahi accepts punishment
DISCIPLINE -> organisation controls participation
POLITICAL EFFECT -> repression loses legitimacy; negotiation opens.""",
            ["Satyagraha principles and political mechanism"],
        ),
        (
            "Champaran local-agency chain",
            "process",
            """TINKATHIA = 3/20 / PLANTER PRESSURE -> cultivator grievance
RAJ KUMAR SHUKLA -> persistent local invitation
GANDHI ARRIVES -> about 8,000 statements
ORDER TO LEAVE -> open refusal and acceptance of legal risk
OFFICIAL INQUIRY -> 25% refund -> later tinkathia abolition
SIGNIFICANCE -> local peasant issue enters national politics.""",
            ["Champaran: Raj Kumar Shukla, tinkathia and local agency"],
        ),
        (
            "Ahmedabad relationship and dispute map",
            "relationship-map",
            """WORKERS SEEK 50% -> plague-bonus and wage claim
ANASUYA SARABHAI -> labour organisation
OWNERS OFFER 20% -> Gandhi supports 35%
AMBALAL SARABHAI -> mill owner and Gandhi associate
SIBLING LINK -> access and mediation across opposing interests
CAUTION -> relationship does not erase class conflict.""",
            ["Ahmedabad: plague bonus, wages and the Sarabhai relationship"],
        ),
        (
            "Ahmedabad pressure-to-arbitration sequence",
            "procedure-sequence",
            """DISPUTE -> worker pledge and 21-day strike
STALEMATE -> discipline becomes fragile
GANDHI FASTS THREE DAYS -> first fast in an Indian struggle
MORAL PRESSURE -> workers and owners face reputational cost
ARBITRATION -> institutional settlement route
SOURCE GAP -> outcome reported as 35% or 27.5%; preserve dispute.""",
            ["Ahmedabad: first Indian fast, pledge and arbitration"],
        ),
        (
            "Kheda remission campaign",
            "process",
            """CROP FAILURE -> four annas or less under revenue rules
DEMAND -> suspend collection
PATEL + INDULAL YAGNIK -> village-level organisation
PLEDGE -> better-off protect poorer cultivators
ATTACHMENT RISK -> property pressure and selective recovery
RELIEF -> bounded and uneven; not abolition of taxation.""",
            ["Kheda: crop failure, revenue remission and leadership"],
        ),
        (
            "Three local laboratories",
            "split-rail",
            """CHAMPARAN -> cultivators / planters / indigo / inquiry plus defiance
AHMEDABAD -> mill workers / mill owners / wage-bonus / fast plus arbitration
KHEDA -> cultivators / revenue state / crop assessment / organised withholding
COMMON -> disciplined collective action opens negotiation
DIFFERENCE -> grievance, opponent and leverage structure vary
RULE -> treat the campaigns as laboratories, not identical templates.""",
            ["Comparative anatomy of Champaran, Ahmedabad and Kheda"],
        ),
        (
            "Rowlatt emergency-power carryover",
            "institution-map",
            """WAR -> inflation, scarcity, epidemic distress and coercive power
1917 PROMISE -> reform expectation rises
COMMITTEE -> recommends continued anti-revolutionary powers
TWO BILLS -> one becomes Act XI on 18 March 1919
RIGHTS EFFECT -> detention and reduced ordinary safeguards
POLITICAL EFFECT -> post-war betrayal frame
TRAP -> not the Montagu-Chelmsford constitutional reform scheme.""",
            ["Wartime hardship and the reform-repression contradiction", "Rowlatt Committee, Bills and Act"],
        ),
        (
            "Sabha, hartal and communication gap",
            "communication-flow",
            """FEB 1919 -> Satyagraha Sabha in Bombay
PLEDGE -> civil disobedience plus acceptance of punishment
DATE CHANGE -> message does not travel uniformly
DELHI -> acts on 30 March
6 APRIL -> final all-India hartal
LESSON -> reach exceeded communication and discipline capacity.""",
            ["Satyagraha Sabha, 6 April hartal and Delhi mismatch"],
        ),
        (
            "The Himalayan-miscalculation feedback",
            "feedback-loop",
            """ALL-INDIA APPEAL -> rapid mobilisation
RAPID SCALE -> uneven training
UNEVEN TRAINING -> violence
VIOLENCE -> suspension on 18 April
SELF-CRITIQUE -> Himalayan miscalculation
LATER RULE -> disciplined organisation must precede mass action.""",
            ["Violence and the Himalayan miscalculation"],
        ),
        (
            "Punjab trigger-to-massacre sequence",
            "causal-flow",
            """WARTIME PUNJAB -> recruitment pressure and repression
            LOCAL POLITICS -> Kitchlew and Satyapal
            10 APRIL ARREST / REMOVAL -> firing, attacks and confrontation
13 APRIL -> gathering at Jallianwala Bagh
            REGINALD DYER -> no warning / dispersal order; not Michael O'Dwyer
EVIDENCE RULE -> no disputed casualty total.""",
            ["Punjab context and the arrests of Kitchlew and Satya Pal", "Jallianwala Bagh: enclosed space, Dyer and firing"],
        ),
        (
            "Martial law, inquiry and moral rupture",
            "accountability-map",
            """13 APRIL MASSACRE -> formal martial law follows
SPECIFIC ABUSE -> crawling order in a particular Amritsar lane
OFFICIAL ROUTE -> Hunter majority and Indian minority
INDIAN ROUTE -> Congress Punjab Inquiry
MORAL RESPONSE -> Tagore 1919; Gandhi returns medal in 1920
DEC 1919 CONGRESS -> Gandhi / C.R. Das compromise on reforms
TRANSITION -> consent recedes; Non-Cooperation later becomes credible.""",
            ["Martial law, crawling order and competing inquiries", "Moral repudiation, consequences and Non-Cooperation bridge"],
        ),
    ],
}


def session_visual(title: str, _terms: list[str]) -> str:
    """Render an explicitly authored, topic-specific visual."""

    if title not in SESSION_VISUALS:
        raise ValueError(f"Missing topic-specific session visual: {title}")
    return (
        "#### VISUAL FIRST\n\n"
        "```text\n"
        f"{title.upper()}\n"
        f"{SESSION_VISUALS[title]}\n"
        "```\n\n"
        "*The visual fixes this subtopic's chronology, mechanism or comparison before the evidence.*"
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
        "preserve the named actors, date and institutional setting."
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
    """Use the authored session route while retaining owner PYQ evidence."""

    key = str(config["key"])
    sessions = []
    for number, (title, core, evidence, caution, exam_use) in enumerate(
        SESSION_PLANS[key], 1
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
        "scope": "Modern Indian History learner-v2 Topics 18-19",
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
    if markdown.count("### ORIGINAL MAINS") != 6:
        raise ValueError(f"{key}: original Mains prompt count failed.")
    if " is the part of " in markdown or " -> and -> " in markdown:
        raise ValueError(f"{key}: generic inherited prose detected.")
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
