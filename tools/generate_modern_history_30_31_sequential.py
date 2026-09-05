"""Build Modern Indian History learner-v2 Topics 30-31.

This authoring-only generator writes complete reusable Markdown, solved
workbooks, manual ASCII and graphical specifications, and tracker-free
generation-one manifests for the linguistic reorganisation of the states and
for the integration of the tribals. It deliberately does not render PDFs,
update the tracker, regenerate indexes, finalize generations, or publish
packages.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base
import generate_modern_history_26_27_sequential as earlier
import generate_modern_history_28_29_sequential as previous


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
    / "modern-indian-history-30-31-2026-08-31-sequential.json"
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
LOCAL_BOOKS = list(
    dict.fromkeys(
        [
            *base.LOCAL_BOOKS,
            ROOT
            / "books"
            / "India After Independence-1947-2000 By Bipan Chandra.pdf",
        ]
    )
)
LOCAL_BOOKS = [path for path in LOCAL_BOOKS if path.is_file()]
COMMON_CROSS = list(base.COMMON_CROSS)
PYQ_INDEXES = list(
    dict.fromkeys(
        [
            *base.PYQ_INDEXES,
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
        ]
    )
)
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]
OFFICIAL_QUESTION_SOURCES = list(
    dict.fromkeys(
        [
            *base.OFFICIAL_QUESTION_SOURCES,
            ROOT / "knowledge-export" / "Prelims PYQ" / "2024-GS1-Set A.md",
            ROOT / "knowledge-export" / "Prelims PYQ" / "Ans-2024-GS1.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "UPSC Mains 2024 GS Paper I.md",
        ]
    )
)
OFFICIAL_QUESTION_SOURCES = [
    path for path in OFFICIAL_QUESTION_SOURCES if path.is_file()
]


TOPICS = [
    base.topic(
        30,
        "Linguistic Reorganisation of States & Regionalism "
        "(1947\u20131967)",
        "30_Linguistic-Reorganisation-and-Regionalism.md",
        "30_Linguistic-Reorganisation-and-Regionalism.md",
        "30_Linguistic-Reorganisation-of-States-and-Regionalism-1947-1967_"
        "Complete-Topic-Package.md",
        [
            "basic/29_Colonial-Legacy-and-Foundations-of-the-Republic.md",
            "advanced/29_Colonial-Legacy-and-Foundations-of-the-Republic.md",
            "basic/31_Integration-of-the-Tribals-and-National-Unity.md",
            "basic/36_Janata-Interregnum-Indiras-Return-and-Regional-Crises.md",
            "27_Independence-and-Partition-1946-1947_"
            "Complete-Topic-Package.md",
        ],
        [
            "https://rajbhasha.gov.in/en/constitutional-provisions",
            "https://rajbhasha.gov.in/en/official-languages-act-1963",
        ],
        "The bounded live linkage for this topic is official. On 31 August "
        "2026 the Department of Official Language of the Ministry of Home "
        "Affairs was consulted directly at `rajbhasha.gov.in`, and only "
        "claims that its own published pages support are used here. Its "
        "reproduction of Part XVII of the Constitution records that Article "
        "343(1) makes Hindi in Devanagari script the official language of "
        "the Union, that Article 343(2) allowed English to continue for all "
        "official purposes of the Union for fifteen years from the "
        "commencement of the Constitution, and that Article 343(3) permits "
        "Parliament to provide by law for the use of English after that "
        "period; that reproduced constitutional text nowhere uses the phrase "
        "'associate official language'. Its reproduction of the Official "
        "Languages Act, 1963 records the Act as Act No. 19 of 1963 dated 10 "
        "May 1963, records that section 3 was to come into force on the "
        "26th day of January 1965, and records the operative words that the "
        "English language 'may ... continue to be used in addition to Hindi' "
        "for all the official purposes of the Union for which it was being "
        "used and for the transaction of business in Parliament. Nothing "
        "beyond those published pages is asserted: no departmental "
        "programme, event, budget, target or contemporary statistic is drawn "
        "from the visit, and the living statutory machinery is used only to "
        "show that the historical settlement this topic studies is still the "
        "operative one.",
        "The Basic and Advanced owner files were reconciled with the "
        "repository's post-independence OCR source, Bipan Chandra, Mridula "
        "Mukherjee and Aditya Mukherjee, *India After Independence, "
        "1947\u20132000*, chapters 7 to 10, alongside the Modern History OCR "
        "sources used by the adjacent packages. The local text (book PDF "
        "page 127) records that Congress undertook political mobilisation in "
        "the mother tongue after 1919 and in 1921 amended its constitution "
        "to reorganise its regional branches on a linguistic basis; (page "
        "128) that the Constituent Assembly appointed the Linguistic "
        "Provinces Commission under Justice S.K. Dar in 1948, that the "
        "Commission advised against the step, that the Assembly then decided "
        "not to incorporate the linguistic principle in the Constitution, "
        "and that the JVP Committee of December 1948 comprised Jawaharlal "
        "Nehru, Sardar Patel and Pattabhi Sitaramayya; (page 129) that the "
        "Andhra demand was held up by the dispute over Madras city, that the "
        "fast unto death began on 19 October 1952 and ended in death after "
        "fifty-eight days, that Andhra came into existence in October 1953, "
        "and that the States Reorganization Commission was appointed in "
        "August 1953 with Justice Fazl Ali, K.M. Panikkar and Hridaynath "
        "Kunzru; (page 130) that the Commission reported in October 1955, "
        "opposed the splitting of Bombay and Punjab, and that the States "
        "Reorganization Act was passed in November 1956 providing for "
        "fourteen states and six centrally administered territories; (pages "
        "130\u2013131) that eighty people were killed in police firings in "
        "Bombay city in January 1956, that sixteen were killed and two "
        "hundred injured in Gujarat, that C.D. Deshmukh resigned, and that "
        "bifurcation was finally agreed in May 1960; (pages 131\u2013132) "
        "that the Punjabi Suba issue assumed communal overtones through "
        "Akali Dal and Jan Sangh mobilisation and that Punjab was divided in "
        "1966 with Chandigarh made a Union Territory serving as joint "
        "capital; (pages 121\u2013125) that the Presidential order of April "
        "1960 used the phrase 'associate official language', that Nehru gave "
        "his assurance in Parliament on 7 August 1959, that the Official "
        "Languages Act of 1963 used the permissive word 'may', that the "
        "agitation around 26 January 1965 cost over sixty lives, and that "
        "the Lok Sabha adopted the amending bill on 16 December 1967 by 205 "
        "votes to 41; and (pages 165\u2013166) that the Shiv Sena was "
        "founded in 1966 under Bal Thackeray on a 'sons of the soil' "
        "platform. The local text renders Potti Sriramulu's name through "
        "optical character recognition as 'Patti Sriramalu'; the owner "
        "spelling is retained and the OCR variant is recorded rather than "
        "silently corrected or silently adopted.",
        "Two Mains demands are routed to this owner in the local ledgers, "
        "both from `_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md`: 2018 "
        "GS-I Q12 on the formation of new states and the economy of India, "
        "and 2022 GS-I Q11 on the political and administrative "
        "reorganization of states and territories. Both are recorded as "
        "routed demand summaries with directive metadata rather than as "
        "verbatim official stems, and no option letter, mark award or "
        "official model answer is asserted for either. No Prelims demand in "
        "the local 2018\u20132026 ledgers is routed to this owner, and no "
        "adjacent Polity, Governance or Indian Society question is "
        "relabelled as a Modern History PYQ for this topic.",
        [
            (
                "Colonial provinces and the administrative case for language",
                "Provincial boundaries in pre-1947 India had been drawn in a "
                "haphazard manner as the British conquest proceeded for "
                "nearly a hundred years, with no heed paid to linguistic or "
                "cultural cohesion, so that most provinces were multilingual "
                "and multicultural while the interspersed princely states "
                "added a further element of heterogeneity; the case for "
                "linguistic states was administrative before it was "
                "sentimental, because mass literacy, democratic politics and "
                "judicial activity can only reach ordinary people through "
                "the mother tongue.",
            ),
            (
                "Congress linguistic commitment from 1921",
                "With the involvement of the masses in the national movement "
                "after 1919 the Congress undertook political mobilisation in "
                "the mother tongue and in 1921 amended its own constitution "
                "to reorganise its regional branches on a linguistic basis, "
                "and it committed itself repeatedly thereafter to redrawing "
                "provincial boundaries on linguistic lines, so that the "
                "principle was long settled and only its timing became "
                "contested after Partition.",
            ),
            (
                "Nehru's post-Partition timing caution",
                "Speaking on the linguistic question Nehru stated on 27 "
                "November 1947 that 'First things must come first and the "
                "first thing is the security and stability of India', "
                "because Partition had produced administrative, economic and "
                "political dislocation alongside a war-like situation over "
                "Kashmir; the leadership remained committed to linguistic "
                "states in principle and merely accorded the redrawing of "
                "the map a low priority, which is a judgement about "
                "sequencing and never a repudiation of the principle.",
            ),
            (
                "Dar Commission of 1948 and the Constituent Assembly",
                "The Constituent Assembly appointed in 1948 the Linguistic "
                "Provinces Commission headed by Justice S.K. Dar to enquire "
                "into the desirability of linguistic provinces; the Dar "
                "Commission advised against the step at that time because it "
                "might threaten national unity and prove administratively "
                "inconvenient, and the Constituent Assembly consequently "
                "decided not to incorporate the linguistic principle in the "
                "Constitution.",
            ),
            (
                "JVP Committee of December 1948 and its conditional opening",
                "To answer continuing public dissatisfaction, especially in "
                "the South, the Congress appointed in December 1948 the JVP "
                "Committee of Jawaharlal Nehru, Sardar Patel and Pattabhi "
                "Sitaramayya, then Congress president; it also advised "
                "against creating linguistic states for the time being on "
                "grounds of unity, national security and economic "
                "development, but it laid down the opening that where a "
                "demand was insistent and overwhelming and the other "
                "language groups involved were agreeable, a new state could "
                "be created.",
            ),
            (
                "The Andhra demand and the Madras-city deadlock",
                "The demand for a separate Andhra state for Telugu speakers "
                "had been popular for nearly half a century and enjoyed the "
                "support of all political parties, and the JVP accepted that "
                "a strong case existed for forming Andhra out of the Madras "
                "Presidency because the leadership of Tamil Nadu was "
                "agreeable; the demand was nevertheless not conceded "
                "immediately because the two sides could not agree on which "
                "state should take Madras city, so the obstacle was a "
                "territorial capital dispute rather than the linguistic "
                "principle itself.",
            ),
            (
                "Potti Sriramulu's fast from 19 October 1952",
                "Potti Sriramulu, a popular freedom fighter, undertook a "
                "fast unto death on 19 October 1952 over the demand for a "
                "separate Andhra state; the repository's local Bipan Chandra "
                "text renders his name through optical character recognition "
                "as 'Patti Sriramalu', and that OCR variant is recorded here "
                "rather than adopted, with the owner spelling retained.",
            ),
            (
                "Death in December 1952 after fifty-eight days",
                "Sriramulu expired in December 1952 after fifty-eight days "
                "of fasting, and his death was followed by three days of "
                "rioting, demonstrations, hartals and violence all over "
                "Andhra, after which the government immediately gave in and "
                "conceded the demand for a separate state.",
            ),
            (
                "Andhra in October 1953, before any commission generalised "
                "the principle",
                "Andhra finally came into existence in October 1953 as the "
                "first linguistic state, and this is the topic's decisive "
                "sequencing fact: the concession was extracted by agitation "
                "and martyrdom before the States Reorganisation Commission "
                "had reported and before any general statute existed, so the "
                "Commission generalised a principle that popular pressure "
                "had already imposed.",
            ),
            (
                "The States Reorganisation Commission and its report of "
                "October 1955",
                "Nehru appointed the States Reorganisation Commission in "
                "August 1953, with Justice Fazl Ali as chairman and K.M. "
                "Panikkar and Hridaynath Kunzru as members, to examine "
                "objectively and dispassionately the entire question of the "
                "reorganisation of the states; the Commission worked for two "
                "years amid meetings, demonstrations, agitations and hunger "
                "strikes, recorded its distress at what it called a kind of "
                "border warfare between old comrades-in-arms, and submitted "
                "its report in October 1955.",
            ),
            (
                "What the Commission endorsed and what it refused",
                "The Commission recognised the linguistic principle for the "
                "most part while insisting that due consideration be given "
                "to administrative and economic factors, but it opposed the "
                "splitting of Bombay and Punjab and it rejected the demand "
                "for a separate Jharkhand state on the ground that the "
                "region did not have a common language, so the settlement it "
                "produced was general in scope and deliberately incomplete "
                "at its two hardest points.",
            ),
            (
                "States Reorganisation Act of November 1956",
                "The States Reorganisation Act was passed by Parliament in "
                "November 1956 and provided for fourteen states and six "
                "centrally administered territories: the Telangana area of "
                "Hyderabad state was transferred to Andhra, Kerala was "
                "created by merging the Malabar district of the old Madras "
                "Presidency with Travancore-Cochin, certain Kannada-speaking "
                "areas were added to Mysore, and Bombay state was enlarged "
                "by merging Kutch, Saurashtra and the Marathi-speaking areas "
                "of Hyderabad with it.",
            ),
            (
                "Bombay: agitation, casualties and bifurcation in May 1960",
                "The strongest reaction against the report and the Act came "
                "from Maharashtra, where eighty people were killed in police "
                "firings in Bombay city in January 1956 while the broad-"
                "based Samyukta Maharashtra Samiti and the Maha Gujarat "
                "Janata Parishad led rival movements, C.D. Deshmukh resigned "
                "from the Union Cabinet and sixteen persons were killed and "
                "two hundred injured in police firings in Gujarat; after the "
                "Bombay Congress scraped through the 1957 elections and "
                "Indira Gandhi as Congress president reopened the question "
                "with the support of President S. Radhakrishnan, the "
                "government agreed in May 1960 to bifurcate Bombay into "
                "Maharashtra and Gujarat, with Bombay city included in "
                "Maharashtra and Ahmedabad made the capital of Gujarat.",
            ),
            (
                "The Union's official language and the 'associate official "
                "language' caution",
                "The Department of Official Language's own reproduction of "
                "Part XVII, consulted live on 31 August 2026, records that "
                "Article 343(1) makes Hindi in Devanagari script the "
                "official language of the Union, that Article 343(2) allowed "
                "English to continue for all official purposes of the Union "
                "for fifteen years from the commencement of the "
                "Constitution, and that Article 343(3) permits Parliament to "
                "provide by law for the use of English thereafter; the "
                "phrase 'associate official language' entered Indian usage "
                "through the Presidential order of April 1960 and the "
                "settlement later legislated, and it is not a term used in "
                "the Constitution's own text, so English must never be "
                "described as the Constitution's formally designated "
                "associate language.",
            ),
            (
                "The Official Languages Act, 1963 and its permissive verb",
                "Nehru assured Parliament on 7 August 1959 that he would "
                "have English as an alternate language as long as the people "
                "required it and would leave the decision to the non-Hindi-"
                "knowing people rather than to the Hindi-knowing people, and "
                "in pursuance of those assurances the Official Languages "
                "Act, 1963 \u2014 Act No. 19 of 1963, dated 10 May 1963 on "
                "the Department of Official Language's published text \u2014 "
                "provided that the English language may continue to be used "
                "in addition to Hindi for all the official purposes of the "
                "Union for which it was being used and for the transaction "
                "of business in Parliament; non-Hindi groups criticised the "
                "permissive word 'may' in place of 'shall' and did not "
                "regard the Act as a statutory guarantee.",
            ),
            (
                "The anti-Hindi agitation of 26 January 1965",
                "Section 3 of the 1963 Act was to come into force on 26 "
                "January 1965, and as that date approached a "
                "fear psychosis gripped the non-Hindi areas and especially "
                "Tamil Nadu: the Dravida Munnetra Kazhagam organised the "
                "Madras State Anti-Hindi Conference on 17 January which "
                "called for observing the day as a day of mourning, students "
                "apprehensive about the all-India services raised the slogan "
                "'Hindi never, English ever', the agitation ran for about "
                "two months and took a toll of over sixty lives through "
                "police firings, and the Tamil ministers C. Subramaniam and "
                "Alagesan resigned from the Union Cabinet.",
            ),
            (
                "Punjab reorganised in 1966 with Chandigarh as a shared "
                "capital",
                "The states of PEPSU had been merged with Punjab in 1956, "
                "leaving a trilingual state of Punjabi, Hindi and Pahari "
                "speakers in which the demand for a Punjabi Suba was pressed "
                "and was refused by the States Reorganisation Commission on "
                "the ground that it would solve neither the language nor the "
                "communal problem; in 1966 Punjab was divided into the "
                "Punjabi-speaking state of Punjab and the Hindi-speaking "
                "state of Haryana, the Pahari-speaking district of Kangra "
                "and part of Hoshiarpur were merged with Himachal Pradesh, "
                "and the newly built city of Chandigarh was made a Union "
                "Territory serving as the joint capital of both states.",
            ),
            (
                "The attributed communal reading of the Punjabi Suba demand",
                "In the repository's local Bipan Chandra text the Punjabi "
                "Suba issue assumed communal overtones because the Akali Dal "
                "and the Jan Sangh used the linguistic question to promote "
                "communal politics, and Nehru and a majority of Punjab "
                "Congressmen judged the demand to be a communal demand for a "
                "Sikh-majority state dressed up as a language plea; this "
                "reading must always be attributed to the source and never "
                "converted into a categorical charge against every supporter "
                "of Punjabi or into a claim that the linguistic issue was "
                "itself communal, and the Communist Party and a section of "
                "the Congress supported the demand.",
            ),
            (
                "The Shiv Sena of 1966 and nativist 'sons of the soil' "
                "politics",
                "The Shiv Sena was founded in 1966 under the leadership of "
                "Bal Thackeray, demanded that preference in jobs and small "
                "businesses be given to Maharashtrians defined as those "
                "whose mother tongue was Marathi under the slogan "
                "'Maharashtra for the Maharashtrians', and organised violent "
                "action against South Indians in Bombay city in 1969 before "
                "shifting its ideological base; militant anti-migrant 'sons "
                "of the soil' movements were also centred in urban Assam, "
                "Telangana, Karnataka, Maharashtra and Orissa, and they mark "
                "the exact point at which regional identity turns inward "
                "against fellow citizens instead of outward towards the "
                "Union.",
            ),
            (
                "The amending Act of 16 December 1967 and indefinite "
                "bilingualism",
                "The Congress Working Committee announced the steps that "
                "were to form the basis of a central enactment embodying the "
                "agitators' major demands, the enactment was delayed by the "
                "Indo-Pak war of 1965, and Indira Gandhi moved the amending "
                "bill on 27 November which the Lok Sabha adopted on 16 "
                "December 1967 by 205 votes to 41; it gave unambiguous legal "
                "fortification to Nehru's assurances by providing that "
                "English would continue in addition to Hindi for official "
                "work at the Centre and for communication with non-Hindi "
                "states for as long as the non-Hindi states wanted it, "
                "producing a virtually indefinite bilingualism, while "
                "Parliament also resolved that public service examinations "
                "be held in Hindi, English and the regional languages and "
                "the states were to adopt a three-language formula.",
            ),
        ],
        [
            "Andhra (October 1953) came before the States Reorganisation "
            "Commission's report (October 1955) and before the Act "
            "(November 1956); never credit the Commission with creating the "
            "first linguistic state.",
            "The Dar Commission of 1948 and the JVP Committee of December "
            "1948 both advised against immediate linguistic states; do not "
            "present the founding leadership as having always favoured them, "
            "and do not present the 1948 caution as prejudice.",
            "The Congress had accepted the linguistic principle since 1921, "
            "so the post-1947 hesitation was about timing and sequencing, "
            "not about principle.",
            "Bombay was bifurcated in May 1960 and Punjab was reorganised in "
            "1966; neither happened in 1956, and the Commission had "
            "expressly opposed splitting both.",
            "Chandigarh was made a Union Territory serving as the joint "
            "capital of Punjab and Haryana; it was not given to either state.",
            "English continued for Union official purposes by statute under "
            "the Official Languages Act, 1963 and by the political "
            "settlement that followed the agitation of 26 January 1965, "
            "legislated unambiguously by the amending Act adopted on 16 "
            "December 1967; Hindi did not become the sole official language "
            "in 1965.",
            "The phrase 'associate official language' entered usage through "
            "the Presidential order of April 1960 and the settlement later "
            "legislated; it is not a term used in the Constitution's own "
            "text, and English must never be described as the Constitution's "
            "formally designated associate language.",
            "The communal reading of the Punjabi Suba demand is the source's "
            "attributed analysis of Akali Dal and Jan Sangh mobilisation; it "
            "must never be converted into a categorical charge against every "
            "supporter of Punjabi or into a claim that the linguistic issue "
            "was itself communal.",
            "Accommodative regional identity, which asks the Union for "
            "statehood, recognition or a resource share, is analytically "
            "different from nativist 'sons of the soil' politics directed "
            "against fellow citizens and from secessionist politics directed "
            "against the Union itself.",
            "Reorganisation did not resolve every linguistic conflict: "
            "boundary disputes, linguistic minorities inside the new states, "
            "water and resource sharing and occasional linguistic chauvinism "
            "persisted, so the verdict must be graded rather than "
            "celebratory.",
            "The claim that reorganisation strengthened rather than weakened "
            "unity is the source's argued and evidenced position, associated "
            "with Rajni Kothari's formulation that language proved a "
            "cementing and integrating influence; present it as a defended "
            "conclusion, not as a self-evident fact.",
            "The North-East was reorganised on tribal and ethnic rather than "
            "linguistic lines, so the linguistic template must not be "
            "transferred wholesale to the tribal-integration owner.",
        ],
        [
            (
                10,
                "Explain why the founding leadership deferred linguistic "
                "reorganisation between 1947 and 1948 although the Congress "
                "had accepted the linguistic principle since 1921.",
                "The deferral was a judgement about sequencing under "
                "post-Partition stress rather than a repudiation of a "
                "principle the Congress had already applied to its own "
                "organisation in 1921.",
                [1, 2, 3, 4],
            ),
            (
                10,
                "State precisely why the creation of Andhra in October 1953 "
                "and not the States Reorganisation Act of November 1956 is "
                "the decisive sequencing fact of this topic.",
                "Andhra was conceded to agitation and martyrdom before any "
                "commission had reported, so the statutory settlement "
                "generalised a principle that popular pressure had already "
                "imposed.",
                [6, 7, 8, 9],
            ),
            (
                15,
                "Examine how the States Reorganisation Commission converted "
                "an agitational victory into a general statutory settlement, "
                "and identify what that settlement deliberately left "
                "unfinished.",
                "The Commission's achievement was to make a general, "
                "commission-based and statutory route available so that no "
                "later demand required a death fast, while its refusal to "
                "split Bombay and Punjab left the two hardest cases to a "
                "further decade of agitation.",
                [9, 10, 11, 12],
            ),
            (
                15,
                "Assess India's official-language settlement between 1959 "
                "and 1967, distinguishing the constitutional position from "
                "the statutory and political settlement.",
                "The Constitution set a fifteen-year horizon and left "
                "Parliament free to extend the use of English, and the "
                "extension was achieved by statute in 1963, forced into "
                "political clarity by the agitation of 26 January 1965, and "
                "given unambiguous legal fortification by the amending Act "
                "adopted on 16 December 1967.",
                [13, 14, 15, 19],
            ),
            (
                20,
                "Critically examine the proposition that linguistic "
                "reorganisation strengthened rather than weakened Indian "
                "unity, avoiding a celebratory account.",
                "Reorganisation strengthened unity because it separated "
                "cultural recognition from political sovereignty and made "
                "administration and democracy legible to citizens, but the "
                "verdict must be graded because linguistic minorities, "
                "boundary disputes and nativist politics survived the "
                "settlement.",
                [0, 11, 12, 18],
            ),
            (
                20,
                "Distinguish accommodative regional identity from nativist "
                "and secessionist regionalism with post-1947 evidence, and "
                "explain why the criterion you use is the right one.",
                "The decisive criterion is the direction of the demand: "
                "claims addressed to the Union for statehood or status were "
                "absorbed and became a source of federal legitimacy, while "
                "claims addressed against fellow citizens or against the "
                "Union itself could not be accommodated on the same terms.",
                [16, 17, 18, 19],
            ),
        ],
        [
            (
                "2018",
                "Mains GS-I Q12",
                "Formation of new states and the economy of India \u2014 "
                "Discuss, 15 marks, 250 words, recorded as a routed demand "
                "summary with directive metadata from "
                "`_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md` rather than "
                "as a verbatim official stem.",
                "routed-mains-demand-summary-not-verbatim",
                "A 250-word discussion should open by refusing the easy "
                "assumption that new states are primarily an economic "
                "instrument: the reorganisation of 1953 to 1966 was driven "
                "by language and administrative legibility, and the "
                "Commission was expressly required to give due consideration "
                "to administrative and economic factors alongside the "
                "linguistic principle. Evidence the economic dimension "
                "carefully with what this owner supports \u2014 the "
                "consolidation of coherent state units after November 1956, "
                "the creation of homogeneous units that could be "
                "administered in a medium the population understood, and the "
                "source's finding that reorganisation did not weaken the "
                "federal structure or paralyse the Centre and that hardly "
                "any complaint of language-based discrimination arose in "
                "raising or spending resources. Qualify with the residual "
                "problems the same source records: disputes over inter-state "
                "boundaries, the sharing of waters, power and surplus food, "
                "and the position of linguistic minorities. Conclude that "
                "new states served economic development mainly by making "
                "administration and participation work, and that no economic "
                "figure, growth rate or investment claim may be invented for "
                "this demand because this owner supplies none.",
            ),
            (
                "2022",
                "Mains GS-I Q11",
                "Political and administrative reorganization of states and "
                "territories \u2014 Discuss with examples, 15 marks, 250 "
                "words, recorded as a routed demand summary with directive "
                "metadata from "
                "`_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md` rather than "
                "as a verbatim official stem.",
                "routed-mains-demand-summary-not-verbatim",
                "The directive asks for examples, so the answer must be a "
                "dated sequence rather than a theme: the Dar Commission of "
                "1948 and the JVP Committee of December 1948 advising delay; "
                "Potti Sriramulu's fast from 19 October 1952 and his death "
                "in December 1952 after fifty-eight days; Andhra in October "
                "1953 as the first linguistic state; the Commission of "
                "Justice Fazl Ali, K.M. Panikkar and Hridaynath Kunzru "
                "reporting in October 1955; the States Reorganisation Act of "
                "November 1956 with fourteen states and six centrally "
                "administered territories; the bifurcation of Bombay in May "
                "1960; and the division of Punjab in 1966 with Chandigarh as "
                "a Union Territory serving as joint capital. Add the "
                "administrative rather than merely political register by "
                "noting the transfer of Telangana to Andhra, the merger of "
                "Malabar with Travancore-Cochin to create Kerala, and the "
                "enlargement of Bombay with Kutch and Saurashtra. Close with "
                "the graded verdict that the reorganisation was a process of "
                "democratic accommodation completed in stages, not a single "
                "1956 event, and record that the North-East was later "
                "reorganised on tribal and ethnic rather than linguistic "
                "lines. No mark award, examiner comment or official model "
                "answer is asserted.",
            ),
        ],
        [
            "1921",
            "27 November 1947",
            "Linguistic Provinces Commission",
            "Justice S.K. Dar",
            "JVP Committee",
            "Pattabhi Sitaramayya",
            "Madras city",
            "Potti Sriramulu",
            "Patti Sriramalu",
            "19 October 1952",
            "fifty-eight days",
            "October 1953",
            "Fazl Ali",
            "K.M. Panikkar",
            "Hridaynath Kunzru",
            "October 1955",
            "November 1956",
            "fourteen states and six centrally administered territories",
            "Telangana",
            "Travancore-Cochin",
            "Samyukta Maharashtra Samiti",
            "Maha Gujarat Janata Parishad",
            "C.D. Deshmukh",
            "May 1960",
            "Article 343",
            "associate official language",
            "Official Languages Act, 1963",
            "26 January 1965",
            "Hindi never, English ever",
            "C. Subramaniam",
            "PEPSU",
            "Punjabi Suba",
            "Chandigarh",
            "Akali Dal",
            "Jan Sangh",
            "Shiv Sena",
            "Bal Thackeray",
            "sons of the soil",
            "16 December 1967",
            "three-language formula",
            "Rajni Kothari",
            "Department of Official Language",
            "Mains GS-I Q12",
            "Mains GS-I Q11",
        ],
    ),
    base.topic(
        31,
        "Integration of the Tribals & National Unity (1947\u20131987)",
        "31_Integration-of-the-Tribals-and-National-Unity.md",
        "31_Integration-of-the-Tribals-and-National-Unity.md",
        "31_Integration-of-the-Tribals-and-National-Unity-1947-1987_"
        "Complete-Topic-Package.md",
        [
            "basic/30_Linguistic-Reorganisation-and-Regionalism.md",
            "advanced/30_Linguistic-Reorganisation-and-Regionalism.md",
            "basic/29_Colonial-Legacy-and-Foundations-of-the-Republic.md",
            "basic/23_Left-Peasant-Workers-and-States-Peoples-Movements.md",
            "advanced/38_Economy-Land-Society-and-State-A-Post-Independence-"
            "Synthesis.md",
        ],
        [
            "https://adiprasaran.tribal.gov.in/JJGV/homenew.aspx",
            "https://culture.gov.in/commemorations/"
            "150th-birth-anniversary-birsa-munda",
        ],
        "The bounded live linkage for this topic is official and "
        "commemorative only. On 31 August 2026 the Ministry of Tribal "
        "Affairs' own Janjatiya Gaurav Varsh portal was consulted, and it "
        "records that the Government of India designated 15 November as "
        "Janjatiya Gaurav Divas in 2021 to commemorate the birth anniversary "
        "of the tribal freedom fighter Bhagwan Birsa Munda, and that a "
        "year-long Janjatiya Gaurav Varsh ran from 15 November 2024 to 15 "
        "November 2025. The Ministry of Culture's commemorations page for "
        "the 150th birth anniversary of Birsa Munda, consulted on the same "
        "date, records that the anniversary celebrations were inaugurated on "
        "15 November 2024 at Jamui in Bihar and that a commemorative coin "
        "and a postal stamp were released. Only those page-supported claims "
        "are used. Birsa Munda's rebellion belongs to the colonial period "
        "and not to this post-1947 owner, so the observance is carried "
        "strictly as evidence of official public remembrance and as a "
        "memory-and-recognition hook that must be paired with the "
        "post-Independence record of land, forest, autonomy and "
        "implementation outcomes. No scheme evaluation, budget figure, "
        "beneficiary count, contemporary tribal statistic or current "
        "security assessment is drawn from either page, and nothing in this "
        "package treats a commemoration as historical evidence about the "
        "integration policy of the 1950s to the 1980s.",
        "The Basic and Advanced owner files were reconciled with the "
        "repository's post-independence OCR source, Bipan Chandra, Mridula "
        "Mukherjee and Aditya Mukherjee, *India After Independence, "
        "1947\u20132000*, chapters 7 and 9. The local text (book PDF page "
        "137) records that the 1971 census counted over 400 tribal "
        "communities numbering nearly 38 million people and constituting "
        "nearly 6.9 per cent of the Indian population, that the greatest "
        "concentrations were in Madhya Pradesh, Bihar, Orissa, north-eastern "
        "India, West Bengal, Maharashtra, Gujarat and Rajasthan, and that "
        "except in the North-East tribal communities were minorities in "
        "their home states; (pages 137\u2013138) that colonialism eroded "
        "tribal isolation through money-lenders, traders, revenue farmers "
        "and middlemen and through forest laws that forbade shifting "
        "cultivation, producing the Santhal uprising and Birsa Munda's Munda "
        "rebellion; (pages 138\u2013140) that Nehru rejected both the "
        "museum-specimen and the assimilationist approaches and laid down "
        "five broad guidelines \u2014 development along the lines of their "
        "own genius, respect for tribal rights in land and forest, "
        "encouragement of tribal languages, administration through tribal "
        "personnel, and no over-administration; (pages 140\u2013141) that "
        "Article 46, gubernatorial responsibility, reserved seats, Tribal "
        "Advisory Councils and a Commissioner for Scheduled Castes and "
        "Scheduled Tribes formed the protective machinery; (pages "
        "141\u2013142) that progress was nevertheless slow and even dismal "
        "because of weak execution, ineffective Tribal Advisory Councils, "
        "misapplied funds, land alienation, mining and industrial expansion "
        "and curtailed forest access; (pages 143\u2013145) that the Sixth "
        "Schedule applied to the tribal areas of Assam through autonomous "
        "districts and district and regional councils and that NEFA was "
        "created in 1948 out of the border areas of Assam as a separately "
        "administered Union Territory; (pages 146\u2013148) that the All "
        "Party Hill Leaders Conference formed in 1960, that Meghalaya was "
        "carved out in 1969 as a state within a state and became a separate "
        "state in 1972 when Manipur and Tripura were simultaneously granted "
        "statehood, that Naga separatists under A.Z. Phizo declared an "
        "independent government in 1955, that the army was sent in early "
        "1956, that the back of the armed rebellion was broken by the middle "
        "of 1957, that moderate leaders headed by Dr Imkongliba Ao "
        "negotiated, and that the state of Nagaland came into existence in "
        "1963; (pages 148\u2013149) that the Mizo National Front under "
        "Laldenga declared independence and proclaimed a military uprising "
        "in March 1966, that Mizoram was given Union Territory status in "
        "1973, that a settlement was reached in 1986 and that a government "
        "with Laldenga as chief minister was formed in the new state of "
        "Mizoram in February 1987; and (pages 149\u2013152) that the "
        "Jharkhand Party was founded in 1950 under Jaipal Singh, won 32 "
        "seats in 1952 and fell to 25 in 1957 and 20 in 1962, that the "
        "States Reorganization Commission of 1955 rejected a Jharkhand state "
        "for want of a common language, that Scheduled Tribes were 31.15 per "
        "cent of Chota Nagpur and 44.67 per cent of the Santhal Parganas in "
        "1951 and 30.94 and 36.22 per cent respectively in 1971 so that "
        "nearly two-thirds of the region was non-tribal, and that the "
        "Jharkhand Mukti Morcha formed in late 1972 with Shibu Soren "
        "emerging as its leader and recast the demand in regional terms. The "
        "local text compresses the Arunachal Pradesh sequence into a single "
        "sentence about naming and statehood in 1987; the owner's dating of "
        "the renaming to 1972 and statehood to 1987 is retained and the "
        "compression in the OCR source is recorded rather than silently "
        "reconciled.",
        "No Prelims or Mains demand in the local 2018\u20132026 routing "
        "ledgers is routed to this owner. The tribal demands that do appear "
        "belong elsewhere and are not relabelled: 2021 Mains GS-I Q9 and "
        "2022 Mains GS-I Q10 are routed to the Indian Society tribe-and-"
        "tribal-society owner, 2023 Mains GS-I Q13 on colonial rule and the "
        "tribal response is routed to the Modern History owner on Left, "
        "peasant, workers' and states' peoples' movements, and the Fifth and "
        "Sixth Schedule Prelims demands of 2019, 2022, 2023, 2024, 2025 and "
        "2026 are routed to the Polity scheduled-and-tribal-areas owner. No "
        "option letter, official stem or key is asserted for any of them, "
        "and no adjacent Polity, Social Justice, Governance or Indian "
        "Society question is presented as a direct Modern History PYQ for "
        "this topic.",
        [
            (
                "Scale of the tribal population on the 1971 Census",
                "The 1971 Census recorded over 400 tribal communities "
                "numbering nearly 38 million people and constituting nearly "
                "6.9 per cent of the Indian population, with the greatest "
                "concentrations in Madhya Pradesh, Bihar, Orissa, north-"
                "eastern India, West Bengal, Maharashtra, Gujarat and "
                "Rajasthan; these figures must always carry the 1971 Census "
                "attribution and must never be presented as 1951 figures or "
                "as current data, and no contemporary tribal statistic may "
                "be substituted for them.",
            ),
            (
                "A minority everywhere except in the North-East",
                "Except in the North-East the tribal communities "
                "constituted minorities in their own home states, and this "
                "single demographic asymmetry explains why the republic "
                "needed two different constitutional instruments: "
                "self-government where a community was territorially "
                "dominant, and protective regulation where it was a "
                "dispersed minority among non-tribal neighbours.",
            ),
            (
                "Colonial erosion of tribal isolation",
                "Colonialism brought a radical transformation as the "
                "tribals' relative isolation was eroded by the penetration "
                "of market forces and by integration into British and "
                "princely administrations, and money-lenders, traders, "
                "revenue farmers, middlemen and petty officials invaded "
                "tribal areas until families were engulfed in debt and lost "
                "their land to outsiders, many being reduced to "
                "agricultural labourers, sharecroppers and rack-rented "
                "tenants while belated legislation against land alienation "
                "failed to halt the process.",
            ),
            (
                "Forest law and the tradition of revolt",
                "To conserve forests and to facilitate their commercial "
                "exploitation the colonial authorities brought large tracts "
                "under forest laws that forbade shifting cultivation and "
                "severely restricted tribal use of the forest and access to "
                "its products, and the combination of land loss, "
                "indebtedness, exploitation by middlemen and extortion by "
                "police and forest officials produced a series of "
                "nineteenth- and twentieth-century uprisings including the "
                "Santhal uprising and the Munda rebellion led by Birsa "
                "Munda, and drew tribal people into the national and peasant "
                "movements.",
            ),
            (
                "Verrier Elwin and integration without imposition",
                "Verrier Elwin, who lived nearly all his life among the "
                "tribal people of central and north-eastern India, was one "
                "of the formative influences on the new government's "
                "policies and recorded that under British rule tribal people "
                "suffered oppression and exploitation as merchants and "
                "liquor-vendors cajoled, tricked and swindled them until "
                "their broad acres dwindled; his influence underwrote a "
                "policy of integration without imposition rather than a "
                "policy of rescue or of tutelage.",
            ),
            (
                "The two approaches Nehru rejected",
                "Two approaches were on offer \u2014 leaving the tribal "
                "people alone and uncontaminated by outside influences, and "
                "assimilating them as completely and quickly as possible "
                "into the surrounding society \u2014 and Nehru rejected "
                "both: he called the first the treatment of tribal people as "
                "museum specimens to be observed and written about, which "
                "was to insult them and was in any case impossible because "
                "penetration had gone too far, and he rejected the second "
                "because being engulfed by the masses of Indian humanity "
                "would destroy the tribals' social and cultural identity and "
                "let unscrupulous outsiders take possession of their land "
                "and forests.",
            ),
            (
                "Integration with identity and the two parameters",
                "Nehru's alternative was integration: making the tribal "
                "people an integral part of the Indian nation while "
                "maintaining their distinct identity and culture, on two "
                "parameters that had to be held together \u2014 the tribal "
                "areas have to progress, and they have to progress in their "
                "own way \u2014 with progress meaning something other than "
                "an attempt merely to duplicate what existed elsewhere in "
                "India and with whatever changes were needed to be worked "
                "out by the tribals themselves.",
            ),
            (
                "The five guidelines later labelled the Tribal Panchsheel",
                "Nehru laid down five broad guidelines for government "
                "policy: tribal people should develop along the lines of "
                "their own genius with no imposition or compulsion from "
                "outside and no superiority complex among non-tribals; "
                "tribal rights in land and forest should be respected and no "
                "outsider should be able to take possession of tribal land; "
                "tribal languages should be encouraged and the conditions "
                "for their flourishing safeguarded; administration should "
                "rely on the tribal people themselves with administrators "
                "recruited and trained from among them and as few outsiders "
                "as possible; and there should be no over-administration of "
                "tribal areas. 'Tribal Panchsheel' is a later label for "
                "these guidelines and no exact proclamation year may be "
                "attached to it.",
            ),
            (
                "Article 46 and the protective machinery",
                "The Constitution gave the policy shape by directing under "
                "Article 46 that the state promote with special care the "
                "educational and economic interests of the tribal people and "
                "protect them from social injustice and all forms of "
                "exploitation; governors of states containing tribal areas "
                "received a special responsibility including the power to "
                "modify central and state laws in their application to those "
                "areas and to frame regulations protecting tribal land "
                "rights and guarding against money-lenders, full political "
                "rights were extended, seats in the legislatures and posts "
                "in the services were reserved for the Scheduled Tribes, "
                "Tribal Advisory Councils were provided for in all states "
                "containing tribal areas, and a Commissioner for Scheduled "
                "Castes and Scheduled Tribes was appointed by the President "
                "to investigate whether the safeguards were being observed.",
            ),
            (
                "Fifth Schedule and Sixth Schedule as different instruments",
                "The Sixth Schedule applied to the tribal areas of Assam and "
                "offered a fair degree of self-government through autonomous "
                "districts and district and regional councils exercising "
                "some legislative and judicial functions within the "
                "jurisdiction of the legislature and Parliament, while the "
                "Fifth Schedule together with Tribal Advisory Councils, "
                "Article 46 and reservations covered the other Scheduled "
                "Areas where tribal communities were dispersed minorities; "
                "the two Schedules answer two different demographic "
                "problems, they are never interchangeable, and their "
                "detailed provisions belong to the Polity owner rather than "
                "to this historical one.",
            ),
            (
                "The implementation shortfall behind constitutional intent",
                "In spite of the constitutional safeguards the tribals' "
                "progress and welfare was slow and even dismal outside the "
                "North-East, because well-intentioned measures were weakly "
                "executed, central and state policies diverged, Tribal "
                "Advisory Councils did not function effectively, funds "
                "allocated for tribal welfare went unspent or were "
                "misapplied, laws against transfer of land to outsiders were "
                "evaded, the rapid extension of mines and industries "
                "displaced communities, deforestation and curtailed forest "
                "access destroyed livelihoods, and an emerging tribal elite "
                "captured much of what development did occur; the honest "
                "verdict is therefore split between political accommodation "
                "that succeeded and development that did not.",
            ),
            (
                "Why the North-East was a different problem",
                "The tribes of north-eastern India, consisting of over a "
                "hundred groups speaking a wide variety of languages, "
                "differed from tribal communities elsewhere because they "
                "formed the overwhelming majority in the areas they "
                "inhabited, because British administration had given their "
                "areas a separate status inside Assam and excluded plains "
                "outsiders from acquiring land, and because they had almost "
                "no political or cultural contact with the national "
                "movement, so that the common bonds forged in the "
                "anti-imperialist struggle had little purchase there and "
                "some missionaries and other foreigners even promoted "
                "sentiment for separate states immediately after "
                "independence.",
            ),
            (
                "NEFA from 1948 and the Sixth Schedule in practice",
                "The North-East Frontier Agency was created in 1948 out of "
                "the border areas of Assam as a Union Territory outside the "
                "jurisdiction of Assam and placed under a special "
                "administration manned by a specially recruited cadre asked "
                "to implement development without disturbing the social and "
                "cultural pattern of life, and it was there that the "
                "Nehru-Elwin policy was implemented best; the objective of "
                "the Sixth Schedule was likewise to enable tribal people to "
                "live according to their own ways, with the Government of "
                "India willing to amend the provisions further to promote "
                "autonomy while refusing to countenance secession or "
                "violence.",
            ),
            (
                "The Naga declaration of 1955 and the two-track response",
                "A section of the Naga leadership opposed integration and "
                "rose in rebellion under A.Z. Phizo demanding complete "
                "independence, and in 1955 these separatists declared the "
                "formation of an independent government and launched a "
                "violent insurrection; the Government of India answered on "
                "two tracks at once, refusing absolutely to concede "
                "secession or to negotiate with those who would not abandon "
                "independence and armed rebellion, while simultaneously "
                "offering a large degree of cultural and administrative "
                "autonomy to moderate, non-violent and non-secessionist Naga "
                "leaders.",
            ),
            (
                "From the army in early 1956 to Nagaland in 1963",
                "The army was sent to Nagaland in early 1956 to restore "
                "peace and order, the back of the armed rebellion was broken "
                "by the middle of 1957, moderate Naga leaders headed by Dr "
                "Imkongliba Ao then came to the fore and negotiated for a "
                "state within the Indian union, and through a series of "
                "intermediate steps the state of Nagaland came into "
                "existence in 1963, after which politics in Nagaland "
                "followed the pattern of other states of the union; the "
                "sequence is coercion followed by political accommodation, "
                "never coercion alone and never accommodation alone.",
            ),
            (
                "The hill-state demand, the language trigger and Meghalaya "
                "in 1969",
                "Resentment against the Assam government mounted among the "
                "hill tribes, who feared assimilation by what they saw as a "
                "policy of Assamization, and the demand for a separate hill "
                "state gained decisive strength when Assamese leaders moved "
                "in 1960 to make Assamese the sole official language of the "
                "state; the hill parties merged into the All Party Hill "
                "Leaders Conference in 1960, the Assam Official Language Act "
                "provoked hartals, demonstrations and a major agitation, the "
                "advocates of a separate state won overwhelmingly in the "
                "tribal areas in the 1962 elections and boycotted the "
                "Assembly, and in 1969 a constitutional amendment carved out "
                "Meghalaya as a state within a state with complete autonomy "
                "except for law and order.",
            ),
            (
                "The reorganisation of the North-East in 1972",
                "As part of the reorganisation of the North-East in 1972, "
                "Meghalaya became a separate state incorporating the Garo, "
                "Khasi and Jaintia tribes, the Union Territories of Manipur "
                "and Tripura were simultaneously granted statehood, and NEFA "
                "was renamed Arunachal Pradesh; the transition to statehood "
                "in the cases of Meghalaya, Manipur, Tripura and Arunachal "
                "Pradesh was on the owners' account quite smooth, and "
                "Arunachal Pradesh itself attained statehood in 1987.",
            ),
            (
                "The Mizo uprising, Union Territory in 1973 and statehood in "
                "February 1987",
                "Unhappiness with the Assam government's relief measures "
                "during the famine of 1959 and the passage of the Act in "
                "1961 making Assamese the official language of the state led "
                "to the formation of the Mizo National Front under Laldenga, "
                "which contested elections while building a military wing "
                "trained and armed from outside; in March 1966 the Front "
                "declared independence, proclaimed a military uprising and "
                "attacked military and civilian targets, the insurrection "
                "was crushed within a few weeks by massive counter-"
                "insurgency measures although stray guerrilla activity "
                "continued, and in 1973, after less extremist Mizo leaders "
                "had scaled the demand down to a separate state within the "
                "union, the Mizo district was separated from Assam and given "
                "the status of a Union Territory as Mizoram. A settlement "
                "was finally arrived at in 1986 under which Laldenga and the "
                "Front agreed to abandon underground violent activity, "
                "surrender with their arms and re-enter the constitutional "
                "political stream while the Government of India granted full "
                "statehood with guarantees for culture, tradition and land "
                "laws, and a government with Laldenga as chief minister was "
                "formed in the new state of Mizoram in February 1987; "
                "Mizoram is the model case of an insurgency ending with its "
                "leader as elected head of a new state, and it must be "
                "presented as the successful case rather than as the "
                "universal outcome, because not every North-Eastern conflict "
                "was settled on this model and no current security "
                "assessment belongs in a historical answer.",
            ),
            (
                "The Jharkhand Party from 1950 and its 32 seats in 1952",
                "The Jharkhand Party was founded in 1950 under the "
                "leadership of the Oxford-educated Jaipal Singh to demand a "
                "separate tribal state incorporating Chota Nagpur and the "
                "Santhal Parganas of south Bihar together with contiguous "
                "tribal areas of Madhya Pradesh, Orissa and West Bengal; it "
                "won 32 seats in the 1952 elections and emerged as the main "
                "opposition party in the Bihar Assembly, then fell to 25 "
                "seats in 1957 and 20 seats in 1962, and the States "
                "Reorganization Commission of 1955 rejected the demand on "
                "the ground that the region did not have a common language "
                "while the central government held that tribals being a "
                "minority there could not claim a state of their own.",
            ),
            (
                "The demographic turn to a regional demand",
                "Scheduled Tribes formed 31.15 per cent of the population of "
                "Chota Nagpur and 44.67 per cent of the Santhal Parganas in "
                "1951 and 30.94 and 36.22 per cent respectively in 1971, so "
                "that nearly two-thirds of Jharkhand's population in 1971 "
                "was non-tribal; the Jharkhand Party had already tried to "
                "give its demand a regional character by opening membership "
                "to non-tribals, Jaipal Singh and much of the leadership "
                "joined the Congress in 1963, and the Jharkhand Mukti Morcha "
                "formed in late 1972 with Shibu Soren emerging as its leader "
                "recast the demand as a regional one on behalf of the "
                "peasants and workers of the region, although the movement "
                "never shifted completely from tribal to class-based "
                "regional politics because it was built around tribal "
                "identity and tribal demands.",
            ),
        ],
        [
            "The population figures of over 400 communities, nearly 38 "
            "million people and nearly 6.9 per cent are from the 1971 "
            "Census; never present them as 1951 figures, as current data or "
            "as an unattributed constant.",
            "'Tribal Panchsheel' is a later label for five broad guidelines; "
            "do not attach an exact proclamation year to it or convert it "
            "into a dated document.",
            "Nehru's policy was neither isolation nor assimilation but "
            "integration with a preserved identity; do not describe it as a "
            "programme of assimilation into a mainstream culture.",
            "The Sixth Schedule governs the tribal areas of the North-East "
            "through autonomous district and regional councils and the Fifth "
            "Schedule governs other Scheduled Areas; the two must never be "
            "treated as interchangeable, and detailed provisions belong to "
            "the Polity owner.",
            "Nagaland became a state in 1963 after the rebellion declared in "
            "1955 was contained; it was not created in 1947 and it was not "
            "granted independence.",
            "The Mizo sequence runs uprising in March 1966, Union Territory "
            "in 1973, Accord in 1986 and statehood with Laldenga as chief "
            "minister in February 1987; do not compress or reorder it.",
            "NEFA was renamed Arunachal Pradesh in 1972 and attained "
            "statehood in 1987, while Meghalaya, Manipur and Tripura belong "
            "to the reorganisation of 1972; the local OCR source compresses "
            "the Arunachal sequence and that compression must be recorded "
            "rather than copied.",
            "Mizoram is the model case of insurgency converted into "
            "constitutional politics, not the universal outcome; do not "
            "imply that every North-Eastern conflict was resolved "
            "identically, and do not add any current security assessment to "
            "a historical answer.",
            "The Jharkhand Party of 1950 under Jaipal Singh won 32 seats in "
            "1952; the movement broadened into a regional demand because "
            "tribals were a local minority, and the Jharkhand Mukti Morcha "
            "under Shibu Soren came later.",
            "The broadening of the Jharkhand demand was never complete: the "
            "movement remained built around tribal identity and tribal "
            "demands, so describe a partial and contested turn rather than a "
            "clean conversion into class politics.",
            "Separate the political success of accommodation from the "
            "developmental failure of implementation: land alienation, "
            "displacement by mines and industry, curtailed forest access and "
            "elite capture persisted alongside statehood and autonomy.",
            "Do not add contemporary tribal statistics, scheme names, budget "
            "figures or beneficiary counts to this historical owner; the "
            "official commemorations cited here are evidence of public "
            "remembrance only.",
        ],
        [
            (
                10,
                "Explain why Indian tribal policy after 1947 rejected both "
                "isolation and assimilation, and state what it put in their "
                "place.",
                "Both alternatives were rejected for stated reasons \u2014 "
                "isolation was insulting and by then impossible, "
                "assimilation would destroy identity and expose land and "
                "forest to outsiders \u2014 and the replacement was "
                "integration on two parameters that had to be held together.",
                [4, 5, 6, 7],
            ),
            (
                10,
                "Distinguish the constitutional instruments applied to the "
                "tribal areas of the North-East from those applied to other "
                "Scheduled Areas, and explain what makes the distinction "
                "necessary.",
                "The distinction is demographic before it is legal: "
                "self-government is available where a community is "
                "territorially dominant, and protective regulation is the "
                "only available instrument where it is a dispersed minority.",
                [1, 8, 9, 11],
            ),
            (
                15,
                "Examine the movement from insurgency to accommodation in "
                "the North-East using the Naga and Mizo trajectories, and "
                "state carefully what the pattern does not prove.",
                "Both trajectories run grievance to armed challenge to "
                "military containment to negotiated autonomy inside the "
                "Union, and the pattern proves that accommodation produced "
                "durable settlements in these cases without proving that "
                "every North-Eastern conflict was resolved identically.",
                [13, 14, 17, 16],
            ),
            (
                15,
                "Analyse the evolution of the Jharkhand movement from a "
                "tribal demand into a regional one, and assess how complete "
                "that conversion was.",
                "The movement broadened because its own constituency had "
                "shrunk to a minority in the territory it claimed, but the "
                "conversion remained partial because the movement stayed "
                "built around tribal identity and tribal demands.",
                [18, 19, 10, 9],
            ),
            (
                20,
                "Critically assess the record of tribal integration between "
                "1947 and 1987, separating political accommodation from "
                "developmental delivery.",
                "The record splits: no tribal region seceded, autonomy and "
                "statehood were extended and insurgent leaderships entered "
                "constitutional politics, while land alienation, "
                "displacement, curtailed forest access and elite capture "
                "meant that the promise of progress in their own way was "
                "honoured constitutionally more than materially.",
                [7, 10, 17, 0],
            ),
            (
                20,
                "Assess why the North-East required a distinct integration "
                "strategy, and evaluate how far the strategy adopted "
                "answered that distinctiveness.",
                "The North-East was distinct in demography, in colonial "
                "administrative history and in its detachment from the "
                "national movement, and the strategy answered that "
                "distinctiveness with autonomy, reorganisation and statehood "
                "rather than with the linguistic template applied elsewhere, "
                "although the settlements arrived only after long periods of "
                "militarised administration.",
                [11, 12, 15, 16],
            ),
        ],
        [
            (
                "2023",
                "Mains GS-I Q13",
                "Colonial rule and the tribals and the tribal response "
                "\u2014 How did and What was, 15 marks, 250 words. The local "
                "ledger `_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md` "
                "routes this demand to the Modern History owner on Left, "
                "peasant, workers' and states' peoples' movements, not to "
                "this post-Independence owner.",
                "adjacent-owner-routed-demand-not-claimed-here",
                "This card exists to prevent a false ownership claim. The "
                "demand's colonial half belongs to the owning topic, and "
                "this owner may legitimately supply only its own "
                "background: that colonialism eroded tribal isolation "
                "through money-lenders, traders, revenue farmers and "
                "middlemen, that forest laws forbade shifting cultivation "
                "and restricted access to forest produce, and that the "
                "resulting dispossession produced the Santhal uprising and "
                "the Munda rebellion led by Birsa Munda and drew tribal "
                "people into the national and peasant movements. Anything "
                "this owner adds beyond that background must be flagged as "
                "post-1947 continuation rather than as an answer to the "
                "colonial demand, and no option letter, mark award or "
                "official model answer is asserted.",
            ),
            (
                "2021",
                "Mains GS-I Q9",
                "Uniqueness of tribal knowledge systems against mainstream "
                "systems \u2014 Examine, 10 marks, 150 words. The local "
                "ledger routes this demand to the Indian Society "
                "tribe-and-tribal-society owner and not to this owner.",
                "adjacent-subject-routed-demand-not-claimed-here",
                "The safe handling is to recognise that this is a society "
                "demand about knowledge systems, not a history demand about "
                "integration policy. The only defensible contribution from "
                "this owner is the policy premise that Nehru's guidelines "
                "required development along the lines of the tribals' own "
                "genius, that tribal languages should be encouraged and the "
                "conditions for their flourishing safeguarded, and that "
                "administration should work through the tribals' own social "
                "and cultural institutions rather than over-administer them. "
                "No sociological classification, ethnographic claim, "
                "statistic or scheme is imported here, and no answer letter "
                "is asserted.",
            ),
            (
                "2022",
                "Mains GS-I Q10",
                "Tribal diversity and treatment as a single category "
                "\u2014 In which specific contexts, 10 marks, 150 words. The "
                "local ledger routes this demand to the Indian Society "
                "tribe-and-tribal-society owner and not to this owner.",
                "adjacent-subject-routed-demand-not-claimed-here",
                "The historical contribution this owner can defensibly make "
                "is the demonstration that Indian policy itself refused a "
                "single category: over 400 communities on the 1971 Census "
                "lived under two distinct constitutional regimes because "
                "they were territorially dominant in the North-East and "
                "dispersed minorities elsewhere, which is precisely why the "
                "Sixth Schedule and the Fifth Schedule exist as separate "
                "instruments, and why the Naga, Mizo and Jharkhand "
                "trajectories diverged so sharply. That is a design "
                "observation, not a sociological typology; the typology "
                "belongs to the owning Indian Society topic, and no answer "
                "letter is asserted.",
            ),
        ],
        [
            "1971 Census",
            "over 400 tribal communities",
            "nearly 38 million",
            "6.9 per cent",
            "Verrier Elwin",
            "museum specimens",
            "own genius",
            "Tribal Panchsheel",
            "over-administration",
            "Article 46",
            "Tribal Advisory Councils",
            "Commissioner for Scheduled Castes and Scheduled Tribes",
            "Sixth Schedule",
            "Fifth Schedule",
            "NEFA",
            "A.Z. Phizo",
            "early 1956",
            "middle of 1957",
            "Imkongliba Ao",
            "Nagaland",
            "All Party Hill Leaders Conference",
            "Assamization",
            "Meghalaya",
            "Garo, Khasi and Jaintia",
            "Arunachal Pradesh",
            "Mizo National Front",
            "Laldenga",
            "March 1966",
            "February 1987",
            "Jharkhand Party",
            "Jaipal Singh",
            "32 seats",
            "Chota Nagpur",
            "Santhal Parganas",
            "Jharkhand Mukti Morcha",
            "Shibu Soren",
            "Janjatiya Gaurav Divas",
            "Ministry of Tribal Affairs",
            "Mains GS-I Q13",
            "Mains GS-I Q9",
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
    "modern-indian-history-30": [
        authored_session(
            "Why colonial provinces made no linguistic sense",
            "The starting condition of this topic is an inherited map that "
            "nobody had designed: provincial boundaries had accumulated over "
            "nearly a hundred years of conquest, so the administrative case "
            "for redrawing them on language was practical long before it "
            "became emotive.",
            [
                "Boundaries in pre-1947 India had been drawn haphazardly as "
                "the British conquest proceeded, with no heed paid to "
                "linguistic or cultural cohesion, so most provinces were "
                "multilingual and multicultural.",
                "The interspersed princely states added a further element of "
                "heterogeneity, so the map was not merely untidy but "
                "administratively incoherent.",
                "Language is closely tied to culture and custom, and the "
                "spread of mass literacy can occur only through the medium "
                "of the mother tongue.",
                "Democracy becomes real to ordinary people only when "
                "politics, administration and judicial activity are "
                "conducted in a language they understand, which requires "
                "states organised around a predominant language.",
            ],
            "Open with the administrative argument, not with sentiment: the "
            "colonial map failed a test of governability before it failed a "
            "test of identity.",
            "Use this opening to convert any 'linguistic states' question "
            "from a culture question into a state-capacity question, which "
            "is what earns analytical marks.",
            """INHERITED COLONIAL MAP  ->  drawn over ~100 years of conquest, not designed
|-- NO TEST APPLIED -> linguistic or cultural cohesion never a criterion
|-- RESULT -> most provinces multilingual + multicultural; princely states add heterogeneity
|-- CONSEQUENCE -> education, courts and administration run in a language most people lack
`-- THEREFORE -> the case for linguistic states is ADMINISTRATIVE first, emotive second""",
            "A linguistic state, in this topic, is an administrative unit "
            "whose boundaries are drawn so that a predominant language can "
            "serve as the medium of education, administration and judicial "
            "activity; it is not a claim to sovereignty for a language "
            "community.",
        ),
        authored_session(
            "The 1921 commitment and the post-Partition pause",
            "The Congress had accepted the linguistic principle for itself "
            "in 1921, so what changed after 1947 was not the principle but "
            "the leadership's judgement about timing, and reading the pause "
            "as a reversal of principle is the commonest analytical error "
            "here.",
            [
                "With mass involvement in the national movement after 1919 "
                "the Congress mobilised in the mother tongue and in 1921 "
                "amended its own constitution to reorganise its regional "
                "branches on a linguistic basis.",
                "The Congress committed itself repeatedly thereafter to "
                "redrawing provincial boundaries on linguistic lines, so "
                "free India was widely assumed to be going to do the same.",
                "Partition produced administrative, economic and political "
                "dislocation, and independence arrived immediately after the "
                "War with law-and-order and economic emergencies and a "
                "war-like situation over Kashmir.",
                "Nehru stated on 27 November 1947 that 'First things must "
                "come first and the first thing is the security and "
                "stability of India', and the leadership accordingly gave "
                "the redrawing of the map a low priority while remaining "
                "committed to it.",
            ],
            "Never write that the leadership opposed linguistic states in "
            "principle; the 1921 commitment stands, and the post-1947 "
            "position was a sequencing judgement taken under measurable "
            "stress.",
            "This distinction supplies the whole 'why did caution give way "
            "to acceptance' answer, because a reversal of timing needs a "
            "different explanation from a reversal of belief.",
            """1921  ->  CONGRESS AMENDS ITS OWN CONSTITUTION -> regional branches on linguistic basis
      ->  repeated commitments to redraw provincial boundaries on language
1947  ->  PARTITION SHOCK -> dislocation + economic crisis + Kashmir + law and order
27 NOV 1947 -> NEHRU: "First things must come first ... security and stability of India"
NET EFFECT -> PRINCIPLE UNCHANGED, PRIORITY LOWERED -> a timing decision, not a reversal""",
            "The post-Partition pause is the deliberate lowering of priority "
            "for boundary redrawing between 1947 and 1952 by a leadership "
            "that continued to accept the linguistic principle it had "
            "applied to its own organisation in 1921.",
        ),
        authored_session(
            "Dar Commission 1948 and the JVP Committee of December 1948",
            "Two considered bodies advised delay within a single year, and "
            "the second of them wrote the opening through which the whole "
            "later settlement eventually passed, so these are not two "
            "identical refusals.",
            [
                "The Constituent Assembly appointed in 1948 the Linguistic "
                "Provinces Commission headed by Justice S.K. Dar to enquire "
                "into the desirability of linguistic provinces.",
                "The Dar Commission advised against the step at that time "
                "because it might threaten national unity and be "
                "administratively inconvenient, and the Constituent Assembly "
                "then decided not to incorporate the linguistic principle in "
                "the Constitution.",
                "Public opinion, especially in the South, was not satisfied, "
                "so in December 1948 the Congress appointed the JVP "
                "Committee of Jawaharlal Nehru, Sardar Patel and Pattabhi "
                "Sitaramayya to examine the question afresh.",
                "The JVP Committee also advised against linguistic states "
                "for the time being on grounds of unity, national security "
                "and economic development, but it laid down that where a "
                "demand was insistent and overwhelming and other language "
                "groups were agreeable, a new state could be created.",
            ],
            "Do not treat the Dar and JVP conclusions as prejudice, and do "
            "not miss the JVP proviso: the same report that counselled delay "
            "supplied the conditional route later used for Andhra.",
            "In a 15-mark answer this pair proves that the eventual policy "
            "was adopted against the considered advice of the founding "
            "leadership, which is the strongest available evidence for the "
            "accommodation argument.",
            """1948  CONSTITUENT ASSEMBLY -> LINGUISTIC PROVINCES COMMISSION (Justice S.K. Dar)
      VERDICT -> advise against now: risk to unity + administrative inconvenience
      EFFECT  -> linguistic principle NOT written into the Constitution
DEC 1948  CONGRESS -> JVP COMMITTEE (Nehru | Patel | Pattabhi Sitaramayya)
      VERDICT -> delay again: unity, security, economic development
      PROVISO -> "insistent and overwhelming demand + other groups agreeable" = a state may be made
KEY -> the refusal carried its own escape clause; Andhra later walks through it""",
            "The JVP proviso is the conditional opening recorded in the "
            "December 1948 report that a new state could be created where "
            "the demand was insistent and overwhelming and the other "
            "language groups involved were agreeable.",
        ),
        authored_session(
            "The Andhra demand and the Madras-city deadlock",
            "Andhra was not blocked by the linguistic principle but by a "
            "capital city, and noticing that converts the case from a story "
            "about language into a story about territory and assets.",
            [
                "The demand for a separate Andhra state for Telugu speakers "
                "had been popular for nearly half a century and had the "
                "support of all political parties.",
                "The JVP accepted that a strong case existed for forming "
                "Andhra out of the Madras Presidency, particularly because "
                "the leadership of Tamil Nadu was agreeable to it.",
                "The demand was not conceded immediately because the two "
                "sides could not agree on which state should take Madras "
                "city, with Andhra leaders unwilling to concede it.",
                "The obstacle was therefore a dispute over a city and its "
                "assets rather than a dispute about whether Telugu speakers "
                "deserved a state.",
            ],
            "State the blocking cause precisely: the JVP proviso was "
            "satisfied on language and failed on the capital, which is why "
            "the concession required an agitation rather than an argument.",
            "Use this to explain why later cases such as Bombay in 1960 and "
            "Chandigarh in 1966 also turned on capitals, showing a repeated "
            "structural obstacle rather than a series of accidents.",
            """ANDHRA DEMAND  ->  Telugu state out of the Madras Presidency
|-- AGE OF DEMAND -> popular for nearly half a century; all-party support
|-- JVP TEST PART 1 -> demand insistent and overwhelming            .......... PASSED
|-- JVP TEST PART 2 -> other language group agreeable (Tamil Nadu)  .......... PASSED
`-- BLOCKING ISSUE  -> WHICH STATE TAKES MADRAS CITY?               .......... UNRESOLVED
PATTERN TO CARRY FORWARD -> capitals, not languages, are what stall reorganisation""",
            "The Madras-city deadlock is the unresolved question of which "
            "successor state would take the capital city, which held up the "
            "Andhra concession although the linguistic conditions laid down "
            "by the JVP Committee had been met.",
        ),
        authored_session(
            "Potti Sriramulu: the fast of 19 October 1952 and its aftermath",
            "A single fast unto death converted a stalled administrative "
            "question into an unavoidable political one, and the exact dates "
            "and duration are the examinable core of this session.",
            [
                "Potti Sriramulu, a popular freedom fighter, undertook a "
                "fast unto death on 19 October 1952 over the demand for a "
                "separate Andhra state.",
                "He expired in December 1952 after fifty-eight days of "
                "fasting.",
                "His death was followed by three days of rioting, "
                "demonstrations, hartals and violence all over Andhra.",
                "The government immediately gave in and conceded the demand "
                "for a separate state of Andhra, so the causal chain runs "
                "martyrdom to disorder to concession.",
            ],
            "Fix all three numbers together \u2014 19 October 1952, "
            "fifty-eight days, December 1952 \u2014 because partial recall "
            "of this sequence is the most common factual failure in the "
            "topic.",
            "In an answer, use this as the pivot sentence that separates the "
            "period of official delay from the period of forced "
            "institutionalisation.",
            """19 OCT 1952  ->  POTTI SRIRAMULU BEGINS FAST UNTO DEATH (separate Andhra)
      |
      v  fifty-eight days
DEC 1952     ->  DEATH
      |
      v
AFTERMATH    ->  three days of rioting, demonstrations, hartals, violence across Andhra
      |
      v
GOVERNMENT   ->  immediately gives in and concedes a separate Andhra state
OCR NOTE     ->  local book text renders the name as "Patti Sriramalu"; owner spelling kept""",
            "Potti Sriramulu is the freedom fighter whose fast unto death "
            "from 19 October 1952 and death in December 1952 after "
            "fifty-eight days forced the concession of the first linguistic "
            "state; the local OCR text renders the name as 'Patti "
            "Sriramalu'.",
        ),
        authored_session(
            "Andhra in October 1953: agitation before commission",
            "Andhra came into existence in October 1953, which means the "
            "first linguistic state was created before any commission had "
            "generalised the principle and before any general statute "
            "existed \u2014 the single sequencing fact that most Prelims "
            "traps in this topic exploit.",
            [
                "Andhra finally came into existence in October 1953 as the "
                "first linguistic state.",
                "The States Reorganisation Commission submitted its report "
                "only in October 1955, two years later.",
                "The States Reorganisation Act followed in November 1956, "
                "three years after Andhra.",
                "The success of the Andhra struggle encouraged other "
                "linguistic groups to agitate for their own states or for "
                "boundary rectification, which is why a general enquiry then "
                "became unavoidable.",
            ],
            "Never credit the States Reorganisation Commission with creating "
            "the first linguistic state; the Commission generalised a "
            "principle that agitation had already imposed.",
            "Open any chronology-based answer with this ordering, because an "
            "examiner can see immediately whether a candidate has the "
            "sequence right.",
            """TIMELINE LOCK  ->  read left to right and never reorder
OCT 1953  ANDHRA CREATED .................. first linguistic state
OCT 1955  SRC REPORT ...................... principle generalised
NOV 1956  STATES REORGANISATION ACT ....... settlement enacted
MAY 1960  BOMBAY BIFURCATED ............... first unfinished case closed
1966      PUNJAB REORGANISED .............. second unfinished case closed
TRAP -> any statement placing the Commission before Andhra is factually wrong""",
            "The Andhra precedence rule is the fixed ordering in which the "
            "creation of Andhra in October 1953 precedes the States "
            "Reorganisation Commission's report of October 1955 and the "
            "States Reorganisation Act of November 1956.",
        ),
        authored_session(
            "The States Reorganisation Commission: members, method and "
            "report",
            "Nehru's answer to an agitation he could not stop was to "
            "institutionalise the question, and the Commission's "
            "composition, working conditions and reporting date are all "
            "separately examinable.",
            [
                "Nehru appointed the States Reorganisation Commission in "
                "August 1953 to examine objectively and dispassionately the "
                "entire question of the reorganisation of the states of the "
                "union.",
                "Its members were Justice Fazl Ali as chairman with K.M. "
                "Panikkar and Hridaynath Kunzru.",
                "Throughout two years of work the Commission faced meetings, "
                "demonstrations, agitations and hunger strikes, and recorded "
                "its distress at what it described as a kind of border "
                "warfare in which old comrades-in-arms were pitted against "
                "one another.",
                "The Commission submitted its report in October 1955.",
            ],
            "Name all three members and both dates; writing 'the SRC' "
            "without the chairman, the two members and the October 1955 "
            "report date leaves the answer unverifiable.",
            "Use the Commission's own recorded distress as evidence that the "
            "reorganisation process was genuinely dangerous, which "
            "strengthens rather than weakens the later accommodation "
            "verdict.",
            """STATES REORGANISATION COMMISSION  (appointed August 1953)
+----------------------+--------------------------+----------------------------+
| CHAIRMAN             | MEMBER                   | MEMBER                     |
| Justice Fazl Ali     | K.M. Panikkar            | Hridaynath Kunzru          |
+----------------------+--------------------------+----------------------------+
MANDATE  -> examine "objectively and dispassionately" the whole reorganisation question
CONDITIONS -> two years of meetings, demonstrations, agitations, hunger strikes
COMMISSION'S OWN WORDS -> "a kind of border warfare" among old comrades-in-arms
REPORT   -> submitted OCTOBER 1955""",
            "The States Reorganisation Commission is the three-member body "
            "appointed in August 1953 under Justice Fazl Ali with K.M. "
            "Panikkar and Hridaynath Kunzru which reported in October 1955 "
            "on the whole question of reorganising the states.",
        ),
        authored_session(
            "What the Commission endorsed and what it refused",
            "The Commission's refusals matter as much as its endorsement, "
            "because the two cases it declined to settle became the two "
            "agitations of the next decade and the demand it rejected "
            "outright reappears in the tribal-integration owner.",
            [
                "The Commission recognised the linguistic principle for the "
                "most part while laying down that due consideration should "
                "be given to administrative and economic factors.",
                "It opposed the splitting of Bombay and of Punjab, so "
                "neither bilingual case was settled by the report.",
                "It rejected the demand for a separate Jharkhand state on "
                "the ground that the region did not have a common language, "
                "which is where the linguistic criterion collides with a "
                "tribal demand.",
                "Its recommendations were accepted with certain "
                "modifications and were quickly implemented, so the general "
                "settlement was adopted while the hard cases were left open.",
            ],
            "State the two refusals explicitly; an answer that reverses them "
            "and has the Commission proposing those two splits has inverted "
            "the record.",
            "This session supplies the bridge to Bombay in 1960, to Punjab "
            "in 1966 and to the tribal owner, so use it whenever a question "
            "asks what reorganisation left unfinished.",
            """COMMISSION'S OUTPUT  ->  one endorsement, three refusals
ENDORSED  -> the linguistic principle "for the most part", with due weight to
             administrative and economic factors
REFUSED 1 -> splitting BOMBAY        -> reopens as agitation -> settled MAY 1960
REFUSED 2 -> splitting PUNJAB        -> reopens as agitation -> settled 1966
REFUSED 3 -> a separate JHARKHAND    -> ground: the region had no common language
LESSON -> a linguistic criterion cannot settle bilingual capitals or tribal demands""",
            "The Commission's refusals are its explicit declines to split "
            "the bilingual states of Bombay and Punjab and its rejection of "
            "a separate Jharkhand state for want of a common language.",
        ),
        authored_session(
            "The States Reorganisation Act of November 1956 and its content",
            "The Act is examined not as a slogan but as a list, and the "
            "specific transfers it made are what distinguish a prepared "
            "answer from a vague one.",
            [
                "The States Reorganisation Act was passed by Parliament in "
                "November 1956 and provided for fourteen states and six "
                "centrally administered territories.",
                "The Telangana area of Hyderabad state was transferred to "
                "Andhra.",
                "Kerala was created by merging the Malabar district of the "
                "old Madras Presidency with Travancore-Cochin, and certain "
                "Kannada-speaking areas of Bombay, Madras, Hyderabad and "
                "Coorg were added to Mysore.",
                "Bombay state was enlarged by merging Kutch and Saurashtra "
                "and the Marathi-speaking areas of Hyderabad with it, which "
                "is precisely why the Bombay question then exploded.",
            ],
            "Quote the count exactly as fourteen states and six centrally "
            "administered territories, and remember that the Act enlarged "
            "Bombay rather than dividing it.",
            "Use the specific transfers as the 'examples' that a "
            "'discuss with examples' directive demands, instead of repeating "
            "the headline count twice.",
            """STATES REORGANISATION ACT  ->  passed by Parliament, NOVEMBER 1956
OUTPUT COUNT -> FOURTEEN STATES + SIX CENTRALLY ADMINISTERED TERRITORIES
TRANSFERS ->
  Telangana (Hyderabad) .............................. to ANDHRA
  Malabar (old Madras Presidency) + Travancore-Cochin  = KERALA created
  Kannada areas of Bombay/Madras/Hyderabad/Coorg ..... to MYSORE
  Kutch + Saurashtra + Marathi areas of Hyderabad .... merged INTO BOMBAY (enlarged)
CONSEQUENCE -> enlarging Bombay instead of dividing it detonates the Maharashtra crisis""",
            "The States Reorganisation Act, 1956 is the November 1956 "
            "statute that generalised the linguistic principle by providing "
            "for fourteen states and six centrally administered territories "
            "and by executing named territorial transfers.",
        ),
        authored_session(
            "Bombay: the first unfinished case, settled in May 1960",
            "Bombay shows what a reorganisation costs when a capital city is "
            "at stake: four years of agitation, two sets of police firings, "
            "a cabinet resignation and a reversal of the government's own "
            "decision.",
            [
                "The strongest reaction against the report and the Act came "
                "from Maharashtra, where eighty people were killed in police "
                "firings in Bombay city in January 1956.",
                "The broad-based Samyukta Maharashtra Samiti and the Maha "
                "Gujarat Janata Parishad led the movements in the two parts "
                "of the state, and C.D. Deshmukh resigned from the Union "
                "Cabinet on the question while sixteen persons were killed "
                "and two hundred injured in police firings in Gujarat.",
                "The government first decided in June 1956 to divide Bombay "
                "with the city as a separate centrally administered unit, "
                "then reverted in July to a bilingual greater Bombay, and "
                "both moves were opposed in Maharashtra and Gujarat alike.",
                "After the Bombay Congress scraped through the 1957 "
                "elections and Indira Gandhi as Congress president reopened "
                "the question with the support of President S. "
                "Radhakrishnan, the government agreed in May 1960 to "
                "bifurcate the state, with Bombay city included in "
                "Maharashtra and Ahmedabad made the capital of Gujarat.",
            ],
            "Bombay was not split in 1956; it was enlarged in 1956 and "
            "bifurcated in May 1960 after the government had twice changed "
            "its own position.",
            "Use Bombay as the case that disproves any account of "
            "reorganisation as a single tidy 1956 event.",
            """BOMBAY: FOUR YEARS OF UNSETTLED SETTLEMENT
JAN 1956 -> 80 killed in police firings, Bombay city; Samyukta Maharashtra Samiti and
            Maha Gujarat Janata Parishad lead rival movements; 16 killed, 200 injured in Gujarat
JUN 1956 -> government decides: split, with the city a separate centrally administered unit
JUL 1956 -> government reverts: bilingual greater Bombay        [opposed on BOTH sides]
1956     -> C.D. Deshmukh resigns from the Union Cabinet
1957     -> Bombay Congress scrapes through the elections
1959-60  -> Indira Gandhi as Congress president reopens it; President S. Radhakrishnan supports
MAY 1960 -> BIFURCATION: Maharashtra (with Bombay city) + Gujarat (capital Ahmedabad)""",
            "The Bombay case is the four-year contest between the Samyukta "
            "Maharashtra Samiti and the Maha Gujarat Janata Parishad over "
            "the division of the enlarged bilingual state and the fate of "
            "Bombay city, settled by bifurcation in May 1960.",
        ),
        authored_session(
            "Punjab 1966: the second unfinished case and Chandigarh",
            "Punjab is the case where the linguistic criterion could not "
            "operate on its own, and the shared-capital device adopted in "
            "1966 is the clearest evidence that language alone could not "
            "settle it.",
            [
                "The states of PEPSU had been merged with Punjab in 1956, "
                "leaving a trilingual state of Punjabi, Hindi and Pahari "
                "speakers.",
                "The demand for a Punjabi Suba was pressed in the "
                "Punjabi-speaking part of the state, and the States "
                "Reorganisation Commission refused it on the ground that it "
                "would solve neither the language nor the communal problem.",
                "In 1966 Punjab was divided into the Punjabi-speaking state "
                "of Punjab and the Hindi-speaking state of Haryana, and the "
                "Pahari-speaking district of Kangra and part of Hoshiarpur "
                "were merged with Himachal Pradesh.",
                "Chandigarh, the newly built city and capital of the united "
                "state, was made a Union Territory and was to serve as the "
                "joint capital of Punjab and Haryana.",
            ],
            "Haryana was created in 1966 and not in 1956, and Chandigarh was "
            "given to neither state but made a Union Territory serving as "
            "the joint capital of both.",
            "Use the shared-capital device as the concrete proof of the "
            "argument that language could not settle a question in which a "
            "capital city and an overlapping identity were both at stake.",
            """PUNJAB: WHY LANGUAGE ALONE COULD NOT SETTLE IT
1956  PEPSU merged into Punjab -> TRILINGUAL state: Punjabi | Hindi | Pahari
      SRC refuses a Punjabi Suba -> "solves neither the language nor the communal problem"
1966  DIVISION EXECUTED:
        Punjabi-speaking .................. PUNJAB
        Hindi-speaking .................... HARYANA          (created 1966, NOT 1956)
        Pahari-speaking Kangra + part of Hoshiarpur ... to HIMACHAL PRADESH
        CHANDIGARH ....................... UNION TERRITORY = JOINT capital of both
READ THE DEVICE -> a shared capital is what you build when one criterion cannot decide""",
            "The Chandigarh arrangement is the 1966 device by which the "
            "newly built capital of the undivided state was constituted a "
            "Union Territory serving as the joint capital of Punjab and "
            "Haryana instead of being allotted to either successor state.",
        ),
        authored_session(
            "The attributed communal reading of the Punjabi Suba demand",
            "This session exists to teach attribution discipline: the "
            "communal reading of the Punjab demand is a sourced analysis of "
            "particular mobilisations, and converting it into a categorical "
            "judgement about Punjabi speakers is both unfair and "
            "examinationally unsafe.",
            [
                "In the repository's local Bipan Chandra text the Punjabi "
                "Suba issue assumed communal overtones because the Akali Dal "
                "and the Jan Sangh used the linguistic question to promote "
                "communal politics.",
                "On that account Hindu communalists opposed the demand by "
                "denying that Punjabi was their mother tongue, while Sikh "
                "communalists advanced it as a Sikh demand for a Sikh state, "
                "claiming Punjabi in Gurmukhi as a Sikh language.",
                "Nehru and a majority of Punjab Congressmen judged the "
                "demand to be a communal demand for a Sikh-majority state "
                "dressed up as a language plea, and refused to accept any "
                "state created on religious grounds.",
                "The same account records that the Communist Party and a "
                "section of the Congress supported the demand, which is why "
                "the analysis must be attributed to particular mobilisations "
                "and never generalised to every supporter of Punjabi.",
            ],
            "Attribute this analysis to the source and to the named parties; "
            "never write a categorical claim that the linguistic demand was "
            "itself communal or that every supporter of Punjabi was acting "
            "communally.",
            "Attribution of contested judgement is a graded skill: in a "
            "20-mark answer, writing 'in Chandra's account' before this "
            "claim is worth more than the claim itself.",
            """ATTRIBUTION DISCIPLINE  ->  who says what, about whom
SOURCE CLAIM (local Bipan Chandra text):
   the Punjabi Suba issue "assumed communal overtones"
WHOSE MOBILISATION -> AKALI DAL (demand framed as a Sikh state, Gurmukhi as a Sikh language)
                   -> JAN SANGH (opposition by denying Punjabi as mother tongue)
LEADERSHIP READING -> Nehru + most Punjab Congressmen: a communal demand "dressed up as a
                      language plea"; no state on religious grounds
COUNTER-EVIDENCE   -> Communist Party and a section of Congress supported the demand
RULE -> attribute to named actors; do not generalise to all Punjabi speakers""",
            "The attributed communal reading is the source's analysis that "
            "particular Akali Dal and Jan Sangh mobilisations gave the "
            "Punjabi Suba demand communal overtones, an analysis that must "
            "be reported with its attribution and never generalised.",
        ),
        authored_session(
            "The Union's official language: constitutional text and the Act "
            "of 1963",
            "The official-language question is the second great act of "
            "accommodation in this topic, and it is decided at three "
            "distinct levels \u2014 constitutional text, statute and "
            "political settlement \u2014 which must never be merged.",
            [
                "The Department of Official Language's own reproduction of "
                "Part XVII, consulted live on 31 August 2026, records that "
                "Article 343(1) makes Hindi in Devanagari script the "
                "official language of the Union.",
                "The same text records that Article 343(2) allowed English "
                "to continue for all official purposes of the Union for "
                "fifteen years from the commencement of the Constitution, "
                "and that Article 343(3) permits Parliament to provide by "
                "law for the use of English after that period.",
                "Nehru assured Parliament on 7 August 1959 that he would "
                "have English as an alternate language as long as the people "
                "required it and would leave the decision to the "
                "non-Hindi-knowing people, and repeated the assurance on 4 "
                "September 1959.",
                "The Official Languages Act, 1963 \u2014 Act No. 19 of 1963, "
                "dated 10 May 1963 on that department's published text "
                "\u2014 provided that the English language may continue to "
                "be used in addition to Hindi, and non-Hindi groups "
                "criticised the permissive 'may' in place of 'shall' as "
                "falling short of a statutory guarantee.",
            ],
            "The phrase 'associate official language' entered Indian usage "
            "through the Presidential order of April 1960 and the settlement "
            "later legislated; it is not a term used in the Constitution's "
            "own text, and English must never be described as the "
            "Constitution's formally designated associate language.",
            "Separating the three levels is what makes a language-policy "
            "answer analytical: the Constitution set a horizon, the statute "
            "extended it, and politics made the extension credible.",
            """THREE LEVELS OF THE OFFICIAL-LANGUAGE SETTLEMENT  ->  never merge them
LEVEL 1  CONSTITUTIONAL TEXT (Part XVII, as published by the Department of Official Language)
         Art 343(1) Hindi in Devanagari = official language of the Union
         Art 343(2) English continues for ALL Union official purposes for FIFTEEN YEARS
         Art 343(3) Parliament MAY provide by law for English after that period
LEVEL 2  STATUTE -> Official Languages Act, 1963 (Act No. 19 of 1963, 10 May 1963)
         operative words: English "may ... continue to be used in addition to Hindi"
         criticism -> "may" not "shall" -> read as no guarantee by non-Hindi groups
LEVEL 3  POLITICS -> Nehru's assurances of 7 August and 4 September 1959
CAUTION  "associate official language" comes from the April 1960 Presidential order and
         the later settlement; it is NOT a phrase in the Constitution's own text""",
            "The official-language settlement is the three-level "
            "arrangement by which Article 343 fixed a fifteen-year horizon "
            "and left Parliament free to extend English, the Official "
            "Languages Act, 1963 exercised that power in permissive terms, "
            "and political assurances supplied the credibility the statute "
            "lacked.",
        ),
        authored_session(
            "26 January 1965 and the settlement legislated on 16 December "
            "1967",
            "The crisis and its resolution complete the accommodation: an "
            "agitation with a measurable human cost forced a settlement that "
            "was then given unambiguous statutory form, and the three-"
            "language formula dates from that resolution.",
            [
                "Section 3 of the 1963 Act was to come into force on 26 "
                "January 1965 \u2014 the 26th day of January 1965 in the "
                "Act's own words \u2014 and as that date approached a "
                "fear psychosis gripped the non-Hindi areas and especially "
                "Tamil Nadu.",
                "The Dravida Munnetra Kazhagam organised the Madras State "
                "Anti-Hindi Conference on 17 January calling for the day to "
                "be observed as a day of mourning, students raised the "
                "slogan 'Hindi never, English ever', the agitation ran about "
                "two months and took a toll of over sixty lives through "
                "police firings, and the Tamil ministers C. Subramaniam and "
                "Alagesan resigned from the Union Cabinet.",
                "The Congress Working Committee announced the steps that "
                "were to form the basis of a central enactment embodying the "
                "concessions, and the enactment was delayed by the Indo-Pak "
                "war of 1965.",
                "Indira Gandhi moved the amending bill on 27 November and "
                "the Lok Sabha adopted it on 16 December 1967 by 205 votes "
                "to 41, providing that English would continue in addition to "
                "Hindi for official work at the Centre and for communication "
                "with non-Hindi states for as long as the non-Hindi states "
                "wanted it; Parliament also resolved that public service "
                "examinations be held in Hindi, English and the regional "
                "languages, and the states were to adopt a three-language "
                "formula.",
            ],
            "Do not write that 1965 imposed Hindi nationwide: the crisis "
            "produced the opposite result, and the settlement was legislated "
            "unambiguously only on 16 December 1967.",
            "This is the strongest single piece of evidence for the "
            "accommodation thesis, because the Union conceded on the one "
            "issue capable of turning language politics into a question of "
            "exit.",
            """CRISIS AND SETTLEMENT  ->  1965 to 1967
26 JAN 1965  section 3 of the 1963 Act due to come into force -> fear psychosis, Tamil Nadu
17 JAN 1965  DMK Madras State Anti-Hindi Conference -> "day of mourning"
FEB 1965     student agitation; slogan "Hindi never, English ever"; ~2 months
COST         over sixty lives through police firings
RESIGNATIONS C. Subramaniam and Alagesan leave the Union Cabinet
1965         Congress Working Committee announces the basis of a central enactment
             enactment delayed by the Indo-Pak war of 1965
27 NOV 1967  Indira Gandhi moves the amending bill
16 DEC 1967  LOK SABHA ADOPTS IT, 205 to 41 -> English continues as long as non-Hindi
             states want it -> virtually indefinite bilingualism + three-language formula""",
            "The settlement of 1967 is the amending Act adopted by the Lok "
            "Sabha on 16 December 1967 by 205 votes to 41, which made the "
            "continuance of English depend on the will of the non-Hindi "
            "states and thereby converted a permissive statute into a "
            "credible guarantee.",
        ),
        authored_session(
            "Regionalism: accommodative, nativist, secessionist \u2014 and "
            "the graded verdict",
            "The topic closes with a typology and a verdict, and the "
            "typology has to be built on a defensible criterion rather than "
            "on a list of examples: the decisive question is whom the demand "
            "is directed against.",
            [
                "Accommodative regionalism directs its demand at the Union "
                "and asks for statehood, recognition or a share of "
                "resources, as in Andhra in 1953, Maharashtra and Gujarat in "
                "1960 and Haryana in 1966, and the federal system absorbed "
                "all of them.",
                "Nativist regionalism directs its demand against fellow "
                "citizens: the Shiv Sena, founded in 1966 under Bal "
                "Thackeray, demanded preference in jobs and small businesses "
                "for Maharashtrians defined by mother tongue and organised "
                "violence against South Indians in Bombay city in 1969, and "
                "similar anti-migrant movements were centred in urban Assam, "
                "Telangana, Karnataka, Maharashtra and Orissa.",
                "The source's own verdict, echoing Rajni Kothari, is that "
                "language proved a cementing and integrating influence and "
                "that reorganisation rationalised the political map without "
                "seriously weakening unity, creating units administrable in "
                "a medium the population understood.",
                "The same source records the residual costs: disputes over "
                "inter-state boundaries, over the sharing of waters, power "
                "and surplus food, the position of linguistic minorities "
                "inside the reorganised states, and occasional linguistic "
                "chauvinism.",
            ],
            "Present the strengthening-of-unity claim as the source's "
            "argued and evidenced position rather than as a self-evident "
            "fact, and always attach the residual costs before the verdict "
            "sentence.",
            "This session is the closing paragraph of every 20-mark answer "
            "on this topic: criterion, cases on each side, argued verdict, "
            "residual costs.",
            """REGIONALISM TYPOLOGY  ->  criterion = WHOM IS THE DEMAND DIRECTED AGAINST?
+---------------------+-------------------------------+-----------------------------+
| DIRECTED AT         | THE UNION                     | FELLOW CITIZENS             |
| CHARACTER           | accommodative                 | nativist / "sons of soil"   |
| DEMAND              | statehood, recognition, share | exclusion of migrants       |
| METHOD              | agitation, elections, statute | coercion against residents  |
| CASES               | Andhra 1953; Maharashtra and  | Shiv Sena 1966, Bombay 1969 |
|                     | Gujarat 1960; Haryana 1966    | anti-migrant movements in   |
|                     |                               | Assam, Telangana, Karnataka,|
|                     |                               | Maharashtra, Orissa         |
| OUTCOME             | absorbed; federal legitimacy  | citizenship guarantees hurt |
+---------------------+-------------------------------+-----------------------------+
ARGUED VERDICT (Kothari) -> language became "a cementing and integrating influence"
RESIDUAL COSTS -> boundary disputes | water, power, surplus food | linguistic minorities""",
            "Accommodative regionalism is a demand addressed to the Union "
            "for statehood, recognition or a share of resources, while "
            "nativist regionalism is a demand addressed against fellow "
            "citizens for their exclusion from jobs, residence or business "
            "within a state.",
        ),
    ],
    "modern-indian-history-31": [
        authored_session(
            "Who and how many: the 1971 Census baseline",
            "Every claim in this topic rests on a demographic baseline that "
            "must be attributed, because the difference between a "
            "territorially dominant community and a dispersed minority "
            "decides which constitutional instrument applies.",
            [
                "The 1971 Census recorded over 400 tribal communities "
                "numbering nearly 38 million people and constituting nearly "
                "6.9 per cent of the Indian population.",
                "The greatest concentrations were in Madhya Pradesh, Bihar, "
                "Orissa, north-eastern India, West Bengal, Maharashtra, "
                "Gujarat and Rajasthan.",
                "Except in the North-East, tribal communities constituted "
                "minorities in their own home states, and they lived mostly "
                "in hills and forest areas.",
                "The task of integration was described as extremely complex "
                "precisely because of the varied conditions, languages and "
                "distinct cultures involved, so no single policy instrument "
                "could serve every case.",
            ],
            "Always attach the 1971 Census attribution to these figures; "
            "they must never be presented as 1951 figures or as current "
            "data, and no contemporary tribal statistic may be substituted "
            "for them.",
            "Open a tribal-policy answer with the attributed baseline and "
            "the dominance-versus-dispersal asymmetry, because that "
            "asymmetry is what the rest of the answer explains.",
            """DEMOGRAPHIC BASELINE  ->  ALWAYS ATTRIBUTED TO THE 1971 CENSUS
   over 400 tribal communities | nearly 38 million people | nearly 6.9 per cent of India
CONCENTRATIONS -> Madhya Pradesh | Bihar | Orissa | north-eastern India | West Bengal
                  Maharashtra | Gujarat | Rajasthan
DECISIVE SPLIT ->
   NORTH-EAST ............ tribal communities are the OVERWHELMING MAJORITY locally
   EVERYWHERE ELSE ....... tribal communities are MINORITIES in their own home states
RULE -> never restate these figures as 1951 data, as current data, or without attribution""",
            "The 1971 Census baseline is the attributed demographic "
            "statement of over 400 tribal communities, nearly 38 million "
            "people and nearly 6.9 per cent of the population on which this "
            "topic's policy analysis rests.",
        ),
        authored_session(
            "Colonial dispossession: money-lenders, land and forest law",
            "Post-independence policy was framed against a specific "
            "inherited harm, and naming the mechanism of that harm is what "
            "makes the later protective machinery intelligible rather than "
            "paternalistic.",
            [
                "Colonialism brought a radical transformation as relative "
                "isolation was eroded by the penetration of market forces "
                "and by integration into British and princely "
                "administrations.",
                "Money-lenders, traders, revenue farmers, middlemen and "
                "petty officials invaded tribal areas and disrupted the "
                "traditional way of life, so families were engulfed in debt "
                "and lost land to outsiders, many being reduced to "
                "agricultural labourers, sharecroppers and rack-rented "
                "tenants, and belated anti-alienation legislation failed to "
                "halt the process.",
                "To conserve forests and to facilitate commercial "
                "exploitation the colonial authorities brought large tracts "
                "under forest laws that forbade shifting cultivation and "
                "severely restricted the use of forests and access to forest "
                "products.",
                "The combination produced a series of nineteenth- and "
                "twentieth-century uprisings, including the Santhal uprising "
                "and the Munda rebellion led by Birsa Munda, and drew tribal "
                "people into the national and peasant movements in Orissa, "
                "Bihar, West Bengal, Andhra, Maharashtra and Gujarat.",
            ],
            "Name the mechanism rather than gesturing at 'exploitation': "
            "debt, land alienation, forest law and official extortion are "
            "four separable causes that each generated a distinct "
            "post-independence remedy.",
            "Use this session whenever a question asks why the republic's "
            "instinct towards tribal communities was protective, because it "
            "supplies the causal answer instead of a moral one.",
            """COLONIAL MECHANISM OF DISPOSSESSION  ->  four separable causes
1 MARKET PENETRATION -> money-lenders, traders, revenue farmers, middlemen, petty officials
2 DEBT AND LAND LOSS -> families engulfed in debt -> land passes to outsiders
                     -> status falls to agricultural labourer / sharecropper / rack-rented tenant
3 FOREST LAW         -> large tracts brought under regulation -> shifting cultivation forbidden
                     -> use of forest and access to forest produce severely restricted
4 OFFICIAL EXTORTION -> police, forest officials, other officers
   |
   v
REVOLT TRADITION -> Santhal uprising | Munda rebellion led by Birsa Munda
   -> and participation in national and peasant movements across six provinces
NOTE -> belated anti-alienation legislation did NOT halt the process""",
            "Colonial dispossession, in this owner, is the combined "
            "operation of market penetration, indebtedness and land "
            "alienation, restrictive forest law and official extortion that "
            "eroded tribal control of land and forest and produced a century "
            "of revolt.",
        ),
        authored_session(
            "Verrier Elwin and the making of the policy",
            "Policy was made with an intellectual influence attached to it, "
            "and naming that influence is examinable in its own right "
            "because it explains why the policy was framed as integration "
            "without imposition rather than as rescue.",
            [
                "Verrier Elwin lived nearly all his life among the tribal "
                "people of central and north-eastern India and was one of "
                "the formative influences in the evolution of the new "
                "government's policies towards the tribes.",
                "He described the colonial record in terms of merchants and "
                "liquor-vendors cajoling, tricking and swindling tribal "
                "people in their ignorance and simplicity until their broad "
                "acres dwindled and they sank into poverty.",
                "Nehru was himself the main influence in shaping the "
                "government's attitude, and framed the first problem as "
                "inspiring confidence so that tribal people would feel at "
                "one with India and realise they had an honoured place in "
                "it.",
                "On that framing India was to signify not only a protecting "
                "force but a liberating one, which is why the resulting "
                "policy is described as integration without imposition "
                "rather than as protection alone.",
            ],
            "Do not reduce Elwin to a slogan: his contribution was "
            "ethnographic evidence about what contact had already done, "
            "which is what made the isolationist option untenable in "
            "practice.",
            "Cite Elwin by name whenever an answer explains why the policy "
            "avoided both isolation and assimilation, because the "
            "attribution shows the policy had an evidentiary basis.",
            """WHO SHAPED THE POLICY, AND WITH WHAT EVIDENCE
VERRIER ELWIN -> lived nearly all his life among tribal people of central and NE India
              -> "one of the formative influences" on the new government's tribal policy
              -> his testimony: merchants and liquor-vendors "cajoling, tricking, swindling"
                 until "their broad acres dwindled"
JAWAHARLAL NEHRU -> "the main influence in shaping the government's attitude"
              -> first problem: "to inspire them with confidence and to make them feel at
                 one with India ... an honoured place in it"
              -> India must signify "not only a protecting force but a liberating one"
RESULT -> a policy of INTEGRATION WITHOUT IMPOSITION, not rescue and not tutelage""",
            "Integration without imposition is the policy formula, "
            "associated with Verrier Elwin's influence, under which the "
            "state accepts responsibility to protect and develop tribal "
            "communities while refusing to impose external forms of life "
            "upon them.",
        ),
        authored_session(
            "The two approaches Nehru rejected",
            "The Panchsheel is best taught as a rejection before it is "
            "taught as a list, because both rejected options were live "
            "positions with named defects, and stating those defects is what "
            "turns a description into an argument.",
            [
                "The first approach was to leave the tribal people alone, "
                "uncontaminated by modern influences, and let them stay more "
                "or less as they were.",
                "Nehru rejected it because treating tribal people as museum "
                "specimens to be observed and written about was to insult "
                "them, and because isolation was in any case impossible "
                "since penetration by the outside world had already gone too "
                "far.",
                "The second approach was to assimilate them completely and "
                "as quickly as possible into the surrounding society, "
                "treating the disappearance of the tribal way of life as "
                "upliftment.",
                "Nehru rejected that too because being engulfed by the "
                "masses of Indian humanity would mean the loss of social and "
                "cultural identity, and because if normal factors were "
                "allowed to operate unscrupulous outsiders would take "
                "possession of tribal lands and forests.",
            ],
            "Give each rejected option its own stated defect: the "
            "isolationist option fails on insult and impossibility, the "
            "assimilationist option fails on identity loss and on the "
            "predictable capture of land and forest.",
            "A 10-mark answer on the Panchsheel is complete if it names both "
            "rejected options with their defects and then names the "
            "replacement, so this session alone can carry that question.",
            """TWO OPTIONS REJECTED, EACH FOR A STATED REASON
OPTION A: LEAVE THEM ALONE (no-change / isolation)
   defect 1 -> treats tribal people "as museum specimens to be observed and written about"
               = "to insult them"
   defect 2 -> impossible in any case: penetration by the outside world had gone too far
OPTION B: ASSIMILATE THEM FAST (disappearance welcomed as "upliftment")
   defect 1 -> "engulfed by the masses of Indian humanity" -> loss of social and cultural identity
   defect 2 -> if normal factors operate, unscrupulous outsiders take tribal land and forest
   |
   v
REPLACEMENT -> INTEGRATION WITH A PRESERVED DISTINCT IDENTITY""",
            "The rejected extremes are the isolationist no-change position, "
            "faulted as insulting and impracticable, and the assimilationist "
            "position, faulted for destroying identity and for exposing "
            "tribal land and forest to outsiders.",
        ),
        authored_session(
            "Integration with identity: the two parameters",
            "The replacement policy is stated as two parameters that must be "
            "held together, and every later judgement in this topic is a "
            "test of whether both were honoured at once.",
            [
                "Nehru favoured integrating the tribal people in Indian "
                "society and making them an integral part of the Indian "
                "nation while maintaining their distinct identity and "
                "culture.",
                "The two basic parameters were that the tribal areas have to "
                "progress, and that they have to progress in their own way.",
                "Progress did not mean an attempt merely to duplicate what "
                "existed in other parts of India, and whatever was good "
                "elsewhere would be adopted by them gradually.",
                "Whatever changes were needed were to be worked out by the "
                "tribals themselves, which converts consultation from a "
                "courtesy into a design requirement.",
            ],
            "Never describe the policy as assimilation into a mainstream "
            "culture; it is integration with a preserved distinct identity, "
            "and the two parameters are joint conditions rather than "
            "alternatives.",
            "Use the two parameters as the marking scheme of your own "
            "answer: political accommodation satisfies the second parameter, "
            "developmental failure violates the first.",
            """THE TWO PARAMETERS  ->  joint conditions, never alternatives
   +-------------------------------+-------------------------------------+
   | PARAMETER 1                   | PARAMETER 2                         |
   | "the tribal areas have to     | "they have to progress in their     |
   |  progress"                    |  own way"                           |
   +-------------------------------+-------------------------------------+
   | rules out museum isolation    | rules out forced assimilation       |
   | tests DEVELOPMENT delivery    | tests IDENTITY preservation         |
   +-------------------------------+-------------------------------------+
QUALIFIERS -> progress is not "merely to duplicate what we have got in other parts of India"
           -> whatever changes are needed are "worked out by the tribals themselves"
USE AS A MARKING SCHEME -> political accommodation satisfies 2; developmental failure breaks 1""",
            "The two parameters are the paired conditions that tribal areas "
            "must progress and must progress in their own way, which "
            "together define integration with a preserved identity and "
            "supply the standard against which the policy's record is "
            "judged.",
        ),
        authored_session(
            "The five guidelines later labelled the Tribal Panchsheel",
            "The five guidelines are the operational content of the policy, "
            "and the label attached to them is a later convenience that must "
            "not be converted into a dated proclamation.",
            [
                "First, tribal people should develop along the lines of "
                "their own genius, with no imposition or compulsion from "
                "outside and no superiority complex among non-tribals, who "
                "were to be understood as having an equal contribution to "
                "make.",
                "Second, tribal rights in land and forests should be "
                "respected, no outsider should be able to take possession of "
                "tribal land, and the incursion of the market economy had to "
                "be strictly controlled and regulated; third, tribal "
                "languages must be given all possible support and the "
                "conditions in which they can flourish must be safeguarded.",
                "Fourth, for administration reliance should be placed on the "
                "tribal people themselves, with administrators recruited "
                "from among them and trained, and as few outsiders as "
                "possible introduced and those carefully chosen; fifth, "
                "there should be no over-administration of tribal areas, "
                "which were to be administered and developed through the "
                "tribals' own social and cultural institutions.",
                "Nehru's approach rested in turn on nationalist practice "
                "since the nineteen-twenties, when Gandhi set up ashrams in "
                "tribal areas and promoted constructive work, and was "
                "supported after independence by Rajendra Prasad, the first "
                "President of India.",
            ],
            "'Tribal Panchsheel' is a later label for these five broad "
            "guidelines, and no exact proclamation year may be attached to "
            "it or asserted as the date of a dated document.",
            "In an answer, list the five guidelines as instruments and then "
            "test each against the record, because the guidelines double as "
            "an evaluation checklist.",
            """FIVE GUIDELINES  ->  later labelled "Tribal Panchsheel" (a LABEL, not a dated decree)
1 OWN GENIUS       -> develop along their own lines; no imposition, no compulsion
                      no superiority complex; an EQUAL contribution to the common culture
2 LAND AND FOREST  -> tribal rights respected; no outsider to take possession of tribal land
                      market incursion strictly controlled and regulated
3 LANGUAGES        -> "all possible support"; conditions for flourishing safeguarded
4 TRIBAL PERSONNEL -> administrators recruited and trained from among the tribal people
                      as few outsiders as possible, and those carefully chosen
5 NO OVER-ADMIN    -> administer and develop through their own social and cultural institutions
ROOTS -> nationalist practice from the 1920s (Gandhi's ashrams, constructive work)
      -> supported after independence by Rajendra Prasad, first President of India
CAUTION -> do NOT assign an exact proclamation year to the label""",
            "The Tribal Panchsheel is the later label given to Nehru's five "
            "broad guidelines on tribal policy \u2014 own genius, land and "
            "forest rights, tribal languages, tribal personnel in "
            "administration, and no over-administration \u2014 and it is not "
            "the title of a dated proclamation.",
        ),
        authored_session(
            "Article 46 and the protective machinery",
            "The Constitution converted the policy into enforceable "
            "machinery, and the machinery has four distinct components that "
            "are frequently collapsed into a single vague reference to "
            "'safeguards'.",
            [
                "A beginning was made in the Constitution itself, which "
                "directed under Article 46 that the state promote with "
                "special care the educational and economic interests of the "
                "tribal people and protect them from social injustice and "
                "all forms of exploitation.",
                "Governors of states in which tribal areas were situated "
                "were given a special responsibility to protect tribal "
                "interests, including the power to modify central and state "
                "laws in their application to tribal areas and to frame "
                "regulations protecting the right to land and guarding "
                "against money-lenders.",
                "Full political rights were extended, and seats in the "
                "legislatures and positions in the administrative services "
                "were reserved for the Scheduled Tribes as for the Scheduled "
                "Castes.",
                "Tribal Advisory Councils were provided for in all states "
                "containing tribal areas, and a Commissioner for Scheduled "
                "Castes and Scheduled Tribes was appointed by the President "
                "to investigate whether the safeguards provided were being "
                "observed.",
            ],
            "Name the four components separately \u2014 the directive under "
            "Article 46, gubernatorial power, reservation and political "
            "rights, and the advisory and investigative bodies \u2014 "
            "because a single word like 'safeguards' earns nothing.",
            "Use the investigative component when you write the critical "
            "paragraph, since it is the Commissioner's own reporting that "
            "documents the implementation failure.",
            """PROTECTIVE MACHINERY  ->  four components, never one word
A DIRECTIVE      -> ARTICLE 46: promote with special care the educational and economic
                    interests of tribal people; protect from social injustice and all
                    forms of exploitation
B GUBERNATORIAL  -> special responsibility of Governors of states with tribal areas
                    power to MODIFY central and state laws in their application there
                    power to frame regulations on land rights and against money-lenders
C POLITICAL      -> full political rights; reserved seats in legislatures
                    reserved positions in the administrative services (as for SCs)
D ADVISORY AND   -> TRIBAL ADVISORY COUNCILS in all states containing tribal areas
  INVESTIGATIVE     COMMISSIONER FOR SCHEDULED CASTES AND SCHEDULED TRIBES, appointed by
                    the President, to investigate whether safeguards were observed
NOTE -> component D is what later DOCUMENTS the failure of components A to C""",
            "The protective machinery is the constitutional package of the "
            "Article 46 directive, special gubernatorial responsibility over "
            "tribal areas, reserved seats and services, Tribal Advisory "
            "Councils and a Commissioner for Scheduled Castes and Scheduled "
            "Tribes.",
        ),
        authored_session(
            "Fifth Schedule and Sixth Schedule: two problems, two "
            "instruments",
            "The two Schedules are not two versions of the same thing; they "
            "answer two different demographic situations, and the design "
            "insight is that self-government requires territorial dominance "
            "while dispersal leaves only protective regulation available.",
            [
                "The Sixth Schedule applied to the tribal areas of Assam and "
                "offered a fair degree of self-government by providing for "
                "autonomous districts and for district and regional councils "
                "exercising some legislative and judicial functions within "
                "the overall jurisdiction of the legislature and Parliament.",
                "Its stated objective was to enable tribal people to live "
                "according to their own ways, and the Government of India "
                "expressed willingness to amend the constitutional "
                "provisions further to promote autonomy if that were found "
                "necessary.",
                "The Fifth Schedule, together with Tribal Advisory Councils, "
                "Article 46, reserved seats and the Commissioner, covered "
                "the other Scheduled Areas, where tribal communities were "
                "dispersed minorities among non-tribal neighbours.",
                "The willingness to extend autonomy was expressly bounded: "
                "Nehru clarified that it did not mean the government would "
                "countenance secession or independence for any area or "
                "region, or tolerate violence in the promotion of any "
                "demand.",
            ],
            "The two Schedules are never interchangeable, the Sixth Schedule "
            "and not the Fifth governs the North-Eastern tribal areas, and "
            "the detailed provisions of either belong to the Polity owner "
            "rather than to this historical treatment.",
            "This distinction converts a listing question into a design "
            "question, which is exactly what a 'constitutional design' "
            "directive rewards.",
            """TWO DEMOGRAPHIC SITUATIONS  ->  TWO CONSTITUTIONAL INSTRUMENTS
+----------------------------------+----------------------------------------+
| SITUATION: locally DOMINANT      | SITUATION: dispersed MINORITY          |
| (tribal areas of Assam / NE)     | (other Scheduled Areas)                |
+----------------------------------+----------------------------------------+
| INSTRUMENT: SIXTH SCHEDULE       | INSTRUMENT: FIFTH SCHEDULE + machinery |
| autonomous districts             | Tribal Advisory Councils               |
| district and regional councils   | Article 46 directive                   |
| some legislative and judicial    | reserved seats and services            |
| functions, within the overall    | Commissioner for SCs and STs           |
| jurisdiction of the legislature  |                                        |
| and Parliament                   |                                        |
+----------------------------------+----------------------------------------+
LOGIC -> self-government needs territorial dominance; dispersal leaves only regulation
BOUND -> more autonomy was offered, but NEVER secession, independence, or tolerated violence""",
            "The Sixth Schedule is the instrument of tribal self-government "
            "through autonomous districts and district and regional councils "
            "in the tribal areas of the North-East, while the Fifth Schedule "
            "is the instrument of protective regulation in the other "
            "Scheduled Areas where tribal communities are dispersed "
            "minorities.",
        ),
        authored_session(
            "The implementation shortfall behind constitutional intent",
            "The mandatory critical paragraph of this topic rests on a "
            "specific finding: the design was sound and the execution was "
            "not, and the failure had named and separable causes.",
            [
                "In spite of the constitutional safeguards and the efforts "
                "of the central and state governments, progress and welfare "
                "were very slow and even dismal, and except in the "
                "North-East tribal people remained poor, indebted, landless "
                "and often unemployed.",
                "The problem lay in weak execution of well-intentioned "
                "measures, in divergence between central and state policy, "
                "in Tribal Advisory Councils that did not function "
                "effectively, and in funds that went unspent, produced no "
                "corresponding results or were misappropriated.",
                "Laws preventing transfer of land to outsiders continued to "
                "be evaded, the rapid extension of mines and industries "
                "worsened conditions, deforestation proceeded through the "
                "cooperation of officials with forest contractors, and "
                "traditional rights of access to the forest were "
                "continuously curtailed.",
                "Tribal society also developed class differences, and the "
                "major gains in education, administrative employment, "
                "economy and political patronage were reaped by a small and "
                "growing tribal elite, while positive developments in "
                "literacy, reservations, Panchayati Raj and repeated "
                "elections increased political participation.",
            ],
            "Attribute the failure to implementation, neglect, capture and "
            "corruption rather than to constitutional design, and keep the "
            "verdict split rather than uniformly negative.",
            "The split verdict \u2014 political accommodation succeeded, "
            "developmental delivery did not \u2014 is the single most "
            "reusable conclusion in this topic.",
            """WHERE THE POLICY FAILED  ->  execution, not design
CAUSE 1 EXECUTION -> weak implementation of well-intentioned measures
CAUSE 2 FEDERAL   -> divergence between central policy and state practice
CAUSE 3 BODIES    -> Tribal Advisory Councils did not function effectively
CAUSE 4 MONEY     -> funds unspent | spent without results | misappropriated
CAUSE 5 LAW       -> anti-alienation laws evaded -> land alienation and eviction continue
CAUSE 6 PROJECTS  -> rapid extension of mines and industries; deforestation; forest access curtailed
CAUSE 7 CAPTURE   -> a small tribal elite reaps the gains as class differences emerge
BUT ALSO -> literacy, reservations, Panchayati Raj and repeated elections raised participation
SPLIT VERDICT -> ACCOMMODATION SUCCEEDED | DELIVERY DID NOT""",
            "The implementation shortfall is the documented gap between "
            "constitutional intent and material outcome, attributed to weak "
            "execution, federal divergence, ineffective advisory bodies, "
            "misapplied funds, evaded land law, displacement by projects and "
            "elite capture rather than to the constitutional design.",
        ),
        authored_session(
            "Why the North-East was a different problem",
            "The North-East required a distinct strategy for three "
            "cumulative reasons, and stating all three is what separates a "
            "prepared answer from a geographical observation.",
            [
                "The tribes of north-eastern India consisted of over a "
                "hundred groups speaking a wide variety of languages and "
                "living in the hill tracts of Assam.",
                "They constituted the overwhelming majority of the "
                "population in most areas they inhabited, and non-tribals "
                "had not penetrated those areas to any significant extent.",
                "British policy in the late nineteenth century gave the "
                "tribal areas a separate administrative status inside the "
                "Assam province, left the socio-political structure "
                "undisturbed and deliberately excluded outsiders from "
                "acquiring land, so tribal communities there suffered little "
                "loss of land, while missionaries were permitted and "
                "encouraged to establish schools, hospitals and churches.",
                "There was a virtual absence of political or cultural "
                "contact with the political life of the rest of India, so "
                "the common bonds forged in the anti-imperialist struggle "
                "had little purchase, and some missionaries and other "
                "foreigners promoted sentiment for separate and independent "
                "states immediately after independence.",
            ],
            "Give all three reasons \u2014 local demographic dominance, a "
            "separate colonial administrative history that prevented land "
            "loss, and detachment from the national movement \u2014 because "
            "any one alone under-explains the difference.",
            "This session answers the 'why did the North-East need a "
            "distinct strategy' demand directly and supplies the premise for "
            "both the Naga and Mizo trajectories.",
            """THREE CUMULATIVE REASONS THE NORTH-EAST WAS DIFFERENT
REASON 1 DEMOGRAPHY -> over a hundred groups, wide variety of languages, hill tracts of Assam
                    -> the OVERWHELMING MAJORITY in most areas they inhabited
                    -> non-tribals had not penetrated to any significant extent
REASON 2 COLONIAL ADMINISTRATION
                    -> separate administrative status inside the Assam province
                    -> socio-political structure left undisturbed
                    -> plainsmen barred from acquiring land -> LITTLE LOSS OF LAND
                    -> missionaries permitted and encouraged: schools, hospitals, churches
REASON 3 DETACHMENT FROM THE NATIONAL MOVEMENT
                    -> "virtual absence of any political or cultural contact"
                    -> the anti-imperialist bond that unified India had little purchase here
                    -> some missionaries and foreigners promoted separatist sentiment after 1947
CONSEQUENCE -> the linguistic template used elsewhere could not be transferred here""",
            "The North-Eastern distinctiveness is the cumulative effect of "
            "local tribal demographic dominance, a separate colonial "
            "administrative regime that excluded outsiders from acquiring "
            "land, and near-total detachment from the national movement.",
        ),
        authored_session(
            "NEFA from 1948 and the Sixth Schedule in practice",
            "One administrative experiment shows the policy working as "
            "designed, and it is worth teaching because it is the control "
            "case against which the conflict cases are judged.",
            [
                "The North-East Frontier Agency was created in 1948 out of "
                "the border areas of Assam and established as a Union "
                "Territory outside the jurisdiction of Assam under a special "
                "administration.",
                "In NEFA, the administration was manned from the beginning "
                "by a special cadre of officers asked to implement specially "
                "designed developmental policies without disturbing the "
                "social and cultural pattern of the life of the people.",
                "The policies associated with Nehru and Verrier Elwin were "
                "implemented best of all in that territory, and an observer "
                "writing in 1967 described a measure of isolation combined "
                "with a sympathetic and imaginative administration as having "
                "created a situation unparalleled elsewhere in India.",
                "The Sixth Schedule was a parallel autonomy instrument for "
                "Assam's tribal areas, using autonomous district and regional "
                "councils; it did not make NEFA a Sixth Schedule territory.",
                "NEFA was renamed Arunachal Pradesh in 1972 and attained "
                "statehood in 1987; the repository's local OCR text "
                "compresses the naming and statehood into a single sentence "
                "about 1987, and that compression is recorded here rather "
                "than copied.",
            ],
            "Keep the two Arunachal dates distinct \u2014 renaming in 1972 "
            "and statehood in 1987 \u2014 and record that the local OCR "
            "source compresses them instead of silently reconciling the "
            "difference.",
            "Use NEFA as the control case: it shows that where the policy "
            "was administered as designed, no insurgency-to-accommodation "
            "cycle was required at all.",
            """NEFA AS THE CONTROL CASE  ->  the policy administered as designed
1948   NORTH-EAST FRONTIER AGENCY created out of the border areas of Assam
       status -> UNION TERRITORY, OUTSIDE the jurisdiction of Assam, special administration
CADRE  -> a special cadre of officers, asked to develop WITHOUT disturbing social and
          cultural patterns of life
RESULT -> Nehru's and Verrier Elwin's policies "implemented best of all" here
          a 1967 observer: "a situation unparalleled in other parts of India"
1972   RENAMED ARUNACHAL PRADESH
1987   STATEHOOD
OCR CAVEAT -> the local book text compresses naming + statehood into one 1987 sentence;
              the owner's 1972/1987 split is retained and the compression is recorded""",
            "NEFA from 1948 was a specially administered Union Territory "
            "outside Assam's jurisdiction; separately, the Sixth Schedule "
            "provided autonomous councils in Assam's tribal areas, so the "
            "two instruments must not be treated as one jurisdiction.",
        ),
        authored_session(
            "Nagaland: the 1955 declaration, the army in early 1956 and "
            "statehood in 1963",
            "The Naga case establishes the template for every later "
            "North-Eastern settlement, and the template is explicitly "
            "two-track rather than either coercive or conciliatory alone.",
            [
                "A section of the Naga leadership opposed integration and "
                "rose in rebellion under A.Z. Phizo demanding separation and "
                "complete independence, and in 1955 these separatists "
                "declared the formation of an independent government and "
                "launched a violent insurrection.",
                "On one track the Government of India made clear it would "
                "firmly oppose the secessionist demand and would not "
                "tolerate recourse to violence, following a policy of "
                "suppression and non-negotiation towards a violent "
                "secessionist movement, and the army was sent in early 1956 "
                "to restore peace and order.",
                "On the other track Nehru judged that total physical "
                "suppression was neither possible nor desirable because the "
                "objective had to be conciliation, so he was willing to go a "
                "long way to grant a large degree of autonomy and carried on "
                "prolonged negotiations with moderate, non-violent and "
                "non-secessionist Naga leaders.",
                "Once the back of the armed rebellion was broken by the "
                "middle of 1957 the moderate leaders headed by Dr "
                "Imkongliba Ao came to the fore and negotiated for a state "
                "within the Indian union, and through a series of "
                "intermediate steps the state of Nagaland came into "
                "existence in 1963.",
            ],
            "Nagaland became a state in 1963 and was not created in 1947, "
            "and neither Nagaland nor Mizoram was ever granted independence; "
            "the concession was always autonomy or statehood within the "
            "Union.",
            "Present the two tracks as simultaneous rather than sequential, "
            "because the analytical point is that refusal of secession is "
            "what made the offer of autonomy credible.",
            """THE NAGA TEMPLATE  ->  two tracks running at the same time
                    +-------------------------------------------+
1955  PHIZO-LED SEPARATISTS declare an "independent government" and launch insurrection
                    |
      +-------------+-------------------------------+
      |                                             |
TRACK 1: REFUSE                              TRACK 2: OFFER
  secession firmly opposed                     a large degree of autonomy
  no negotiation with those who keep           prolonged negotiation with moderate,
  the independence demand and arms             non-violent, non-secessionist leaders
  EARLY 1956 -> army sent to restore order     conciliation is the stated objective
      |                                             |
      +-------------+-------------------------------+
                    |
MID-1957  back of the armed rebellion broken -> moderates under Dr Imkongliba Ao come forward
1963      STATE OF NAGALAND created WITHIN the Indian union (never independence)""",
            "The two-track policy is the simultaneous combination of "
            "absolute refusal of secession and armed rebellion with an open "
            "offer of large autonomy to non-secessionist leaders, which "
            "produced the state of Nagaland in 1963.",
        ),
        authored_session(
            "From a language trigger to the reorganisation of 1972",
            "The Meghalaya sequence shows that language policy inside a "
            "state, and not only insurgency, could drive reorganisation, "
            "which is the direct bridge between this owner and the "
            "linguistic-reorganisation owner.",
            [
                "The hill tribes of Assam had no cultural affinity with the "
                "Assamese and Bengali residents of the plains and feared "
                "losing their identity to what they saw, with some "
                "justification, as a policy of Assamization.",
                "The demand for a separate hill state gained decisive "
                "strength when Assamese leaders moved in 1960 towards making "
                "Assamese the sole official language of the state; various "
                "hill parties merged into the All Party Hill Leaders "
                "Conference in 1960, and the Assam Official Language Act "
                "produced hartals, demonstrations and a major agitation.",
                "In the 1962 elections the overwhelming majority of Assembly "
                "seats from the tribal areas were won by advocates of a "
                "separate state, who boycotted the Assembly, and after "
                "prolonged negotiation a constitutional amendment in 1969 "
                "carved out Meghalaya as a state within a state, with "
                "complete autonomy except for law and order and shared High "
                "Court, Public Service Commission and Governor.",
                "As part of the reorganisation of the North-East in 1972 "
                "Meghalaya became a separate state incorporating the Garo, "
                "Khasi and Jaintia tribes, the Union Territories of Manipur "
                "and Tripura were simultaneously granted statehood, and NEFA "
                "was renamed Arunachal Pradesh.",
            ],
            "Do not compress this into a single 1972 event: the trigger was "
            "a state language act, the intermediate device was the 1969 "
            "state within a state, and full statehood followed in 1972.",
            "Use this sequence when a question asks how language politics "
            "and tribal politics interacted, because it is the one case "
            "where both owners meet directly.",
            """LANGUAGE TRIGGER TO STATEHOOD  ->  the Meghalaya sequence
GRIEVANCE  -> hill tribes have no cultural affinity with Assamese and Bengali plainsmen
           -> fear of "Assamization"; resentment at attitudes of non-tribal officials
1960       -> Assamese leaders move to make Assamese the SOLE official language of the state
1960       -> hill parties merge into the ALL PARTY HILL LEADERS CONFERENCE
           -> Assam Official Language Act -> hartals, demonstrations, major agitation
1962       -> separate-state advocates sweep the tribal-area Assembly seats -> boycott
1969       -> constitutional amendment: MEGHALAYA as "a state within a state"
              complete autonomy EXCEPT law and order; shared High Court, PSC, Governor
1972       -> NORTH-EAST REORGANISATION
              MEGHALAYA separate state (Garo, Khasi, Jaintia)
              MANIPUR and TRIPURA granted statehood
              NEFA renamed ARUNACHAL PRADESH""",
            "The 1972 reorganisation of the North-East is the settlement "
            "that made Meghalaya a separate state, granted statehood to "
            "Manipur and Tripura and renamed NEFA as Arunachal Pradesh, "
            "reached after a hill-state demand triggered by state language "
            "policy.",
        ),
        authored_session(
            "Mizoram: March 1966, Union Territory in 1973, Accord in 1986, "
            "statehood in February 1987",
            "Mizoram is the model case of the accommodation strategy, and it "
            "must be taught with all four dates because the value of the "
            "case lies in the length of the road from uprising to chief "
            "ministership.",
            [
                "Unhappiness with the Assam government's relief measures "
                "during the famine of 1959 and the passage of the Act in "
                "1961 making Assamese the official language of the state led "
                "to the formation of the Mizo National Front with Laldenga "
                "as president, which contested elections while building a "
                "military wing armed and trained from outside.",
                "In March 1966 the Front declared independence from India, "
                "proclaimed a military uprising and attacked military and "
                "civilian targets; immediate and massive counter-insurgency "
                "measures crushed the insurrection within a few weeks, "
                "though stray guerrilla activity continued and hard-core "
                "leaders escaped abroad.",
                "In 1973, after less extremist Mizo leaders had scaled the "
                "demand down to a separate state within the Indian union, "
                "the Mizo district was separated from Assam and given the "
                "status of a Union Territory as Mizoram, and renewed "
                "insurgency in the late seventies was again contained.",
                "A settlement was arrived at in 1986 under which Laldenga "
                "and the Front agreed to abandon underground violence, "
                "surrender with their arms and re-enter constitutional "
                "politics while the Government of India granted full "
                "statehood with guarantees for culture, tradition and land "
                "laws, and a government with Laldenga as chief minister was "
                "formed in the new state of Mizoram in February 1987.",
            ],
            "Present Mizoram as the successful case rather than as the "
            "universal outcome: not every North-Eastern conflict was settled "
            "on this model, and no current security assessment belongs in a "
            "historical answer.",
            "Use the four dates as the spine of any 'insurgency to "
            "accommodation' answer, and close on the fact that the insurgent "
            "president became the elected chief minister.",
            """MIZORAM  ->  the longest road from uprising to chief ministership
1959      famine relief failure under the Assam government -> grievance
1961      Act making Assamese the official language of the state -> trigger
          -> MIZO NATIONAL FRONT formed, LALDENGA president
          -> contests elections WHILE building an externally armed and trained military wing
MAR 1966  declares independence, proclaims a military uprising, attacks military and civilian
          targets -> crushed within a few weeks by massive counter-insurgency
          -> stray guerrilla activity continues; hard-core leadership escapes abroad
1973      demand scaled down to a state within the union -> Mizo district separated from Assam
          -> MIZORAM constituted a UNION TERRITORY   [renewed insurgency later contained]
1986      ACCORD -> arms surrendered, underground activity abandoned, re-entry into
          constitutional politics; full statehood granted with culture, tradition, land-law guarantees
FEB 1987  LALDENGA SWORN IN AS CHIEF MINISTER of the new state of Mizoram
CAUTION   the model case, NOT the universal outcome""",
            "The Mizo Accord of 1986 is the negotiated settlement under "
            "which the Mizo National Front abandoned armed struggle and "
            "surrendered its arms in exchange for full statehood with "
            "cultural and land-law guarantees, followed by Laldenga's "
            "assumption of the chief ministership in February 1987.",
        ),
        authored_session(
            "Jharkhand: from a tribal state to a regional demand",
            "The Jharkhand movement is the topic's clearest case of a "
            "movement changing its identity claim in response to demographic "
            "reality, and the change must be described as partial and "
            "contested rather than as a clean conversion.",
            [
                "The Jharkhand Party was founded in 1950 under the "
                "leadership of the Oxford-educated Jaipal Singh to demand a "
                "separate tribal state incorporating Chota Nagpur and the "
                "Santhal Parganas of south Bihar with contiguous tribal "
                "areas of Madhya Pradesh, Orissa and West Bengal; it won 32 "
                "seats in 1952 and became the main opposition party in the "
                "Bihar Assembly, then fell to 25 seats in 1957 and 20 in "
                "1962.",
                "Scheduled Tribes were 31.15 per cent of Chota Nagpur and "
                "44.67 per cent of the Santhal Parganas in 1951, and 30.94 "
                "and 36.22 per cent respectively in 1971, so nearly "
                "two-thirds of the region's population in 1971 was "
                "non-tribal, which meant that a state demanded for tribal "
                "predominance would not deliver it.",
                "The States Reorganization Commission of 1955 rejected the "
                "demand because the region did not have a common language "
                "and the central government held that tribals being a "
                "minority there could not claim a state of their own, and in "
                "1963 Jaipal Singh and a major part of the leadership joined "
                "the Congress.",
                "The Jharkhand Mukti Morcha, formed in late 1972 with Shibu "
                "Soren emerging as its leader, recast the demand as a "
                "regional one on behalf of the peasants and workers of the "
                "region, but the movement found it difficult to shift "
                "completely from tribal to class-based regional politics "
                "because it was built around tribal identity and tribal "
                "demands.",
            ],
            "Describe the broadening as partial: the movement remained built "
            "around tribal identity, reservation policy kept tribal and "
            "non-tribal interests in tension, and tribal society itself was "
            "not homogeneous.",
            "Use Jharkhand as the transferable analytical point for any "
            "identity-politics question: an identity claim adapts to "
            "demography or it loses electoral viability.",
            """JHARKHAND  ->  an identity claim colliding with its own demography
1950   JHARKHAND PARTY founded; leader JAIPAL SINGH (Oxford-educated)
       demand -> Chota Nagpur + Santhal Parganas + contiguous tribal areas of MP, Orissa, WB
1952   32 SEATS -> main opposition party in the Bihar Assembly
1957   25 seats        1962   20 seats                 [electoral decline sets in]
DEMOGRAPHIC TRAP ->
       Scheduled Tribes, Chota Nagpur ...... 31.15% (1951) ....... 30.94% (1971)
       Scheduled Tribes, Santhal Parganas .. 44.67% (1951) ....... 36.22% (1971)
       => nearly TWO-THIRDS of the region non-tribal in 1971
1955   SRC rejects a Jharkhand state -> "the region did not have a common language"
       Centre adds -> a minority cannot claim a state of its own
1963   Jaipal Singh and much of the leadership join the Congress
1972   JHARKHAND MUKTI MORCHA formed; SHIBU SOREN emerges as leader
       demand recast as REGIONAL, on behalf of the peasants and workers of the region
LIMIT  the shift was never complete: the movement stayed built on tribal identity""",
            "The Jharkhand demographic turn is the partial recasting of an "
            "exclusively tribal statehood demand into a regional one, forced "
            "by the fact that tribal communities were a minority in the "
            "territory claimed, and never completed because the movement "
            "remained built on tribal identity.",
        ),
    ],
}
PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-30": [
        (
            "Inherited map, the 1921 commitment and the 1947 pause",
            "argument-map",
            """STARTING CONDITION -> a map accumulated over ~100 years of conquest, never designed
|-- NO COHESION TEST -> most provinces multilingual; princely states add heterogeneity
|-- ADMINISTRATIVE COST -> education, courts and politics run in an alien language
1921 -> CONGRESS AMENDS ITS OWN CONSTITUTION: regional branches on a linguistic basis
1947 -> PARTITION DISLOCATION + Kashmir + economic and law-and-order emergencies
27 NOV 1947 -> NEHRU PRIORITY: security and stability of India must come first
READ IT CORRECTLY -> PRINCIPLE UNCHANGED SINCE 1921; ONLY THE PRIORITY WAS LOWERED""",
            [
                "Why colonial provinces made no linguistic sense",
                "The 1921 commitment and the post-Partition pause",
            ],
        ),
        (
            "Dar 1948, JVP December 1948 and the escape clause",
            "institution-map",
            """1948  CONSTITUENT ASSEMBLY -> LINGUISTIC PROVINCES COMMISSION (Justice S.K. Dar)
      |-- finding -> advise against now: risk to unity, administrative inconvenience
      `-- effect  -> the linguistic principle is NOT written into the Constitution
DEC 1948  CONGRESS -> JVP COMMITTEE
      |-- members -> Jawaharlal Nehru | Sardar Patel | Pattabhi Sitaramayya
      |-- finding -> delay again: unity, national security, economic development
      `-- PROVISO -> demand "insistent and overwhelming" + other language groups agreeable
                     => a new state MAY be created
CONSEQUENCE -> the refusal carries its own escape clause, and Andhra later uses it""",
            [
                "Dar Commission 1948 and the JVP Committee of December 1948",
            ],
        ),
        (
            "Andhra: a capital city, not a language, blocks the demand",
            "evidence-chain",
            """DEMAND -> a Telugu state carved out of the Madras Presidency
AGE    -> popular for nearly half a century; supported by all political parties
JVP TEST 1 -> is the demand insistent and overwhelming? -> PASSED
JVP TEST 2 -> are the other language groups agreeable (Tamil Nadu)? -> PASSED
BLOCKER    -> WHICH SUCCESSOR STATE TAKES MADRAS CITY? -> UNRESOLVED
INFERENCE  -> the obstacle is territorial and fiscal, not linguistic
CARRY FORWARD -> Bombay city (1956-60) and Chandigarh (1966) repeat the same obstacle""",
            ["The Andhra demand and the Madras-city deadlock"],
        ),
        (
            "Sriramulu: fast, death and immediate concession",
            "causal-chain",
            """19 OCT 1952 -> POTTI SRIRAMULU BEGINS A FAST UNTO DEATH for a separate Andhra
      v  (fifty-eight days)
DEC 1952    -> DEATH
      v
AFTERMATH   -> three days of rioting, demonstrations, hartals and violence across Andhra
      v
GOVERNMENT  -> "immediately gave in" and concedes a separate state of Andhra
NUMBERS TO FIX TOGETHER -> 19 October 1952 | fifty-eight days | December 1952
OCR NOTE -> the local book text renders the name "Patti Sriramalu"; owner spelling retained""",
            ["Potti Sriramulu: the fast of 19 October 1952 and its aftermath"],
        ),
        (
            "Sequencing lock: agitation precedes commission and statute",
            "timeline",
            """OCT 1953  ANDHRA CREATED -> the FIRST linguistic state
OCT 1955  SRC REPORT SUBMITTED -> the principle generalised
NOV 1956  STATES REORGANISATION ACT -> the settlement enacted
MAY 1960  BOMBAY BIFURCATED -> first refused case closed
1966      PUNJAB DIVIDED; HARYANA CREATED -> second refused case closed
16 DEC 1967  AMENDING ACT ADOPTED -> language settlement legislated
TRAP -> any statement that places the Commission or the Act before Andhra is wrong""",
            ["Andhra in October 1953: agitation before commission"],
        ),
        (
            "The Commission: three members, two years, one report",
            "institution-map",
            """STATES REORGANISATION COMMISSION -> appointed AUGUST 1953 by Nehru
+---------------------------+---------------------------+---------------------------+
| CHAIRMAN                  | MEMBER                    | MEMBER                    |
| Justice Fazl Ali          | K.M. Panikkar             | Hridaynath Kunzru         |
+---------------------------+---------------------------+---------------------------+
MANDATE    -> examine "objectively and dispassionately" the whole reorganisation question
CONDITIONS -> two years of meetings, demonstrations, agitations and hunger strikes
ITS OWN WORDS -> "a kind of border warfare" among old comrades-in-arms in the freedom struggle
REPORT     -> submitted OCTOBER 1955""",
            [
                "The States Reorganisation Commission: members, method and "
                "report",
            ],
        ),
        (
            "One endorsement and three refusals",
            "comparison",
            """ENDORSED  -> the linguistic principle "for the most part"
             qualified by due consideration for administrative and economic factors
REFUSED 1 -> splitting BOMBAY -> reopens as agitation -> settled MAY 1960
REFUSED 2 -> splitting PUNJAB -> reopens as agitation -> settled 1966
REFUSED 3 -> separate JHARKHAND -> region lacked one common language
             the Centre adds: a local minority cannot claim a state of its own
IMPLEMENTATION -> recommendations accepted with modifications and quickly implemented
LESSON -> a linguistic criterion cannot settle bilingual capitals or tribal demands""",
            ["What the Commission endorsed and what it refused"],
        ),
        (
            "The Act of November 1956: the count and the transfers",
            "data-table",
            """STATES REORGANISATION ACT -> passed by Parliament, NOVEMBER 1956
HEADLINE COUNT -> FOURTEEN STATES + SIX CENTRALLY ADMINISTERED TERRITORIES
+----------------------------------------------+--------------------------------------+
| TERRITORY MOVED                              | DESTINATION / RESULT                 |
+----------------------------------------------+--------------------------------------+
| Telangana area of Hyderabad state            | transferred to ANDHRA                |
| Malabar district (old Madras Presidency)     | merged with Travancore-Cochin        |
|   + Travancore-Cochin                        |   => KERALA created                  |
| Kannada areas of Bombay, Madras, Hyderabad,  | added to MYSORE                      |
|   Coorg                                      |                                      |
| Kutch, Saurashtra, Marathi areas of Hyderabad| merged INTO BOMBAY (state enlarged)  |
+----------------------------------------------+--------------------------------------+
CONSEQUENCE -> enlarging Bombay rather than dividing it detonates the Maharashtra crisis""",
            [
                "The States Reorganisation Act of November 1956 and its "
                "content",
            ],
        ),
        (
            "Bombay 1956 to 1960: what a capital city costs",
            "causal-chain",
            """JAN 1956 -> 80 killed in police firings in Bombay city
            Samyukta Maharashtra Samiti and Maha Gujarat Janata Parishad lead rival movements
            16 killed and 200 injured in police firings in Gujarat
1956     -> C.D. Deshmukh resigns from the Union Cabinet on the question
JUN 1956 -> government decides to divide, with the city a separate administered unit
JUL 1956 -> government REVERTS to a bilingual greater Bombay -> opposed on BOTH sides
1957     -> the Bombay Congress scrapes through the elections
1959-60  -> Indira Gandhi as Congress president reopens it; President S. Radhakrishnan supports
MAY 1960 -> BIFURCATION: Maharashtra (with Bombay city) + Gujarat (capital Ahmedabad)""",
            ["Bombay: the first unfinished case, settled in May 1960"],
        ),
        (
            "Punjab 1966: a shared capital and an attributed reading",
            "comparison",
            """1956 -> PEPSU merged into Punjab -> a TRILINGUAL state: Punjabi | Hindi | Pahari
        SRC refuses a Punjabi Suba: it would solve "neither the language nor the communal problem"
1966 -> DIVISION EXECUTED
        Punjabi-speaking -> PUNJAB
        Hindi-speaking -> HARYANA        (created 1966, NOT 1956)
        Kangra + part of Hoshiarpur . to HIMACHAL PRADESH
        CHANDIGARH -> UNION TERRITORY, JOINT capital of both states
ATTRIBUTED READING (local Bipan Chandra text, report it with its attribution):
        the issue "assumed communal overtones" through AKALI DAL and JAN SANGH mobilisation
        Nehru and most Punjab Congressmen: a communal demand "dressed up as a language plea"
        COUNTER-EVIDENCE -> the Communist Party and a section of Congress supported it
RULE -> never generalise the charge to every supporter of Punjabi""",
            [
                "Punjab 1966: the second unfinished case and Chandigarh",
                "The attributed communal reading of the Punjabi Suba demand",
            ],
        ),
        (
            "The language settlement at three levels and its 1967 vote",
            "evidence-chain",
            """LEVEL 1 CONSTITUTIONAL TEXT (Part XVII, Department of Official Language publication)
        Art 343(1) Hindi in Devanagari = official language of the Union
        Art 343(2) English continues for ALL Union official purposes for FIFTEEN YEARS
        Art 343(3) Parliament MAY provide by law for English after that period
LEVEL 2 STATUTE -> Official Languages Act, 1963 (Act No. 19 of 1963, 10 May 1963)
        section 3 to come into force on 26 JANUARY 1965
        statutory rule -> English may continue to be used in addition to Hindi
        criticism -> "may", not "shall" -> read as no statutory guarantee
LEVEL 3 POLITICS -> Nehru's assurances, 7 August and 4 September 1959
        26 JAN 1965 crisis -> DMK conference of 17 January; "Hindi never, English ever"
        cost -> over sixty lives; C. Subramaniam and Alagesan resign from the Union Cabinet
        16 DEC 1967 -> Lok Sabha adopts the amending bill 205 to 41 -> indefinite bilingualism
                       + three-language formula for the states
CAUTION -> "associate official language" comes from the April 1960 Presidential order and the
           later settlement; it is not a phrase in the Constitution's own text""",
            [
                "The Union's official language: constitutional text and the "
                "Act of 1963",
                "26 January 1965 and the settlement legislated on 16 "
                "December 1967",
            ],
        ),
        (
            "Regionalism typology and the graded verdict",
            "balance-sheet",
            """CRITERION -> WHOM IS THE DEMAND DIRECTED AGAINST?
+---------------------+-------------------------------+------------------------------+
| DIRECTED AT         | THE UNION                     | FELLOW CITIZENS              |
| CHARACTER           | accommodative                 | nativist, "sons of the soil" |
| DEMAND              | statehood, recognition, share | exclusion of migrants        |
| METHOD              | agitation, elections, statute | coercion against residents   |
| CASES               | Andhra 1953; Maharashtra and  | Shiv Sena 1966 (Bal          |
|                     | Gujarat 1960; Haryana 1966    | Thackeray); Bombay 1969;     |
|                     |                               | anti-migrant movements in    |
|                     |                               | Assam, Telangana, Karnataka, |
|                     |                               | Maharashtra, Orissa          |
| OUTCOME             | absorbed; federal legitimacy  | citizenship guarantees hurt  |
+---------------------+-------------------------------+------------------------------+
ARGUED VERDICT (Rajni Kothari) -> language proved "a cementing and integrating influence"
RESIDUAL COSTS -> inter-state boundary disputes | sharing of waters, power, surplus food
               -> linguistic minorities inside the reorganised states | linguistic chauvinism
STATE IT AS -> a defended conclusion supported by evidence, never as a self-evident fact""",
            [
                "Regionalism: accommodative, nativist, secessionist \u2014 "
                "and the graded verdict",
            ],
        ),
    ],
    "modern-indian-history-31": [
        (
            "The 1971 Census baseline and the decisive asymmetry",
            "data-table",
            """ATTRIBUTED BASELINE -> THE 1971 CENSUS (never 1951, never current data)
        over 400 tribal communities | nearly 38 million people | nearly 6.9 per cent of India
CONCENTRATIONS -> Madhya Pradesh | Bihar | Orissa | north-eastern India | West Bengal
               -> Maharashtra | Gujarat | Rajasthan
+--------------------------------+-----------------------------------------------+
| NORTH-EAST                     | EVERYWHERE ELSE                               |
| overwhelming local majority    | minorities in their own home states           |
| self-government is possible    | only protective regulation is available       |
+--------------------------------+-----------------------------------------------+
WHY IT MATTERS -> this asymmetry, not sentiment, dictates which Schedule applies""",
            ["Who and how many: the 1971 Census baseline"],
        ),
        (
            "Colonial dispossession and the revolt tradition",
            "causal-chain",
            """1 MARKET PENETRATION -> money-lenders, traders, revenue farmers, middlemen, petty officials
2 DEBT AND LAND LOSS -> families engulfed in debt -> land passes to outsiders
                     -> reduced to agricultural labourers, sharecroppers, rack-rented tenants
                     -> belated anti-alienation legislation FAILS to halt the process
3 FOREST LAW         -> large tracts regulated for conservation and commercial exploitation
                     -> shifting cultivation forbidden; access to forest produce restricted
4 OFFICIAL EXTORTION -> police, forest officials and other government officers
      v
REVOLT TRADITION -> Santhal uprising | Munda rebellion led by Birsa Munda
      v
PARTICIPATION -> national and peasant movements in Orissa, Bihar, West Bengal, Andhra,
                 Maharashtra and Gujarat
THIS IS THE HARM -> the post-1947 protective machinery is a reply to these four causes""",
            ["Colonial dispossession: money-lenders, land and forest law"],
        ),
        (
            "Two options rejected, one policy adopted",
            "argument-map",
            """INFLUENCES -> VERRIER ELWIN (lived among tribal people; "formative influence" on policy)
           -> JAWAHARLAL NEHRU ("the main influence in shaping the government's attitude")
OPTION A: LEAVE THEM ALONE
   defect 1 -> treated "as museum specimens to be observed and written about" = "to insult them"
   defect 2 -> impossible anyway; penetration by the outside world had gone too far
OPTION B: ASSIMILATE THEM QUICKLY
   defect 1 -> "engulfed by the masses of Indian humanity" -> loss of social and cultural identity
   defect 2 -> unscrupulous outsiders would take possession of tribal lands and forests
      v
ADOPTED -> INTEGRATION WITH A PRESERVED DISTINCT IDENTITY
FRAMING -> India must signify "not only a protecting force but a liberating one\"""",
            [
                "Verrier Elwin and the making of the policy",
                "The two approaches Nehru rejected",
            ],
        ),
        (
            "The two parameters as a marking scheme",
            "comparison",
            """+----------------------------------+----------------------------------------------+
| PARAMETER 1                      | PARAMETER 2                                  |
| "the tribal areas have to        | "they have to progress in their own way"     |
|  progress"                       |                                              |
+----------------------------------+----------------------------------------------+
| rules out museum isolation       | rules out forced assimilation                |
| tests DEVELOPMENT DELIVERY       | tests IDENTITY PRESERVATION                  |
+----------------------------------+----------------------------------------------+
QUALIFIER 1 -> progress is not "merely to duplicate what we have got in other parts of India"
QUALIFIER 2 -> whatever changes are needed are "worked out by the tribals themselves"
USE IT -> political accommodation satisfies parameter 2; developmental failure breaks parameter 1
=> the honest verdict on this topic is a SPLIT verdict, and this panel is why""",
            ["Integration with identity: the two parameters"],
        ),
        (
            "The five guidelines and the label caution",
            "institution-map",
            """FIVE BROAD GUIDELINES -> later labelled "Tribal Panchsheel" (a LABEL, not a dated decree)
1 OWN GENIUS       -> develop along their own lines; no imposition, no compulsion
                   -> non-tribals to hold no superiority complex; an EQUAL contribution
2 LAND AND FOREST  -> tribal rights respected; no outsider to take possession of tribal land
                   -> market incursion strictly controlled and regulated
3 LANGUAGES        -> "all possible support"; conditions for flourishing safeguarded
4 TRIBAL PERSONNEL -> administrators recruited and trained from among tribal people
                   -> as few outsiders as possible, and those carefully chosen
5 NO OVER-ADMIN    -> develop through their own social and cultural institutions
ROOTS -> nationalist constructive work from the 1920s; Gandhi's ashrams in tribal areas
      -> supported after independence by Rajendra Prasad, first President of India
CAUTION -> do NOT attach an exact proclamation year to the label""",
            ["The five guidelines later labelled the Tribal Panchsheel"],
        ),
        (
            "Article 46 and the four-part protective machinery",
            "institution-map",
            """A DIRECTIVE -> ARTICLE 46: promote with special care the educational and economic interests
               of the tribal people; protect from social injustice and all forms of exploitation
B GUBERNATORIAL -> special responsibility of Governors of states containing tribal areas
               -> power to MODIFY central and state laws in their application there
               -> power to frame regulations on land rights and against money-lenders
C POLITICAL -> full political rights extended
            -> reserved seats in the legislatures and reserved posts in the services
D ADVISORY AND INVESTIGATIVE
            -> TRIBAL ADVISORY COUNCILS in all states containing tribal areas
            -> COMMISSIONER FOR SCHEDULED CASTES AND SCHEDULED TRIBES, appointed by the
               President, to investigate whether the safeguards were being observed
NOTE -> component D is what later DOCUMENTS the failure of components A to C""",
            ["Article 46 and the protective machinery"],
        ),
        (
            "Fifth Schedule and Sixth Schedule: a design matrix",
            "comparison",
            """+-----------------------------------+---------------------------------------------+
| SITUATION: LOCALLY DOMINANT       | SITUATION: DISPERSED MINORITY               |
| tribal areas of Assam / North-East| other Scheduled Areas                       |
+-----------------------------------+---------------------------------------------+
| INSTRUMENT: SIXTH SCHEDULE        | INSTRUMENT: FIFTH SCHEDULE + machinery      |
| autonomous districts              | Tribal Advisory Councils                    |
| district and regional councils    | Article 46 directive                        |
| some legislative and judicial     | reserved seats and services                 |
| functions, within the overall     | Commissioner for Scheduled Castes and       |
| jurisdiction of the legislature   | Scheduled Tribes                            |
| and Parliament                    |                                             |
+-----------------------------------+---------------------------------------------+
STATED OBJECTIVE -> enable tribal people "to live according to their own ways"
OFFER -> the Government of India was willing to amend the provisions to widen autonomy
BOUND -> but never secession, never independence, never tolerated violence
RULE -> the two Schedules are NEVER interchangeable; details belong to the Polity owner""",
            [
                "Fifth Schedule and Sixth Schedule: two problems, two "
                "instruments",
            ],
        ),
        (
            "Where the policy failed: execution, not design",
            "balance-sheet",
            """FAILURES                                   | GAINS
1 weak execution of well-intentioned       | literacy and education spread
  measures                                 | reservations in services and higher education
2 divergence between central and state     | Panchayati Raj and repeated elections
  policy                                   | rising political participation and
3 Tribal Advisory Councils ineffective     |   representation
4 funds unspent, unproductive or           | demands for a greater share in national
  misappropriated                          |   economic development
5 anti-alienation laws evaded -> land loss |
6 mines, industries and deforestation      |
  displace and dispossess                  |
7 a small tribal elite captures the gains  |
OUTSIDE THE NORTH-EAST -> tribal people remained poor, indebted, landless, often unemployed
SPLIT VERDICT -> POLITICAL ACCOMMODATION SUCCEEDED | DEVELOPMENTAL DELIVERY DID NOT
ATTRIBUTION -> the failure is attributed to implementation and neglect, not to the design""",
            ["The implementation shortfall behind constitutional intent"],
        ),
        (
            "Why the North-East differed, and the NEFA control case",
            "evidence-chain",
            """REASON 1 DEMOGRAPHY -> over a hundred groups; overwhelming local majority
                    -> non-tribals had not penetrated to any significant extent
REASON 2 COLONIAL ADMINISTRATION -> separate administrative status inside Assam province
                    -> socio-political structure undisturbed; plainsmen barred from buying land
                    -> LITTLE LOSS OF LAND; missionaries permitted: schools, hospitals, churches
REASON 3 DETACHMENT -> "virtual absence of any political or cultural contact" with Indian
                    political life; the anti-imperialist bond had little purchase here
                    -> some missionaries and foreigners promoted separatist sentiment after 1947
CONTROL CASE -> NEFA created 1948 out of the border areas of Assam
             -> a Union Territory OUTSIDE Assam's jurisdiction, special cadre of officers
             -> develop WITHOUT disturbing social and cultural patterns of life
             -> Nehru's and Elwin's policies "implemented best of all" here
             -> RENAMED ARUNACHAL PRADESH 1972; STATEHOOD 1987
OCR CAVEAT -> the local book compresses naming and statehood into one 1987 sentence""",
            [
                "Why the North-East was a different problem",
                "NEFA from 1948 and the Sixth Schedule in practice",
            ],
        ),
        (
            "The Naga two-track template, 1955 to 1963",
            "causal-chain",
            """1955 -> Phizo-led separatists declare an "independent government"; violent insurrection
        |
        +--- TRACK 1: REFUSE ------------------+--- TRACK 2: OFFER --------------------+
        |  secession firmly opposed            |  a large degree of autonomy           |
        |  no negotiation while independence   |  prolonged negotiation with moderate, |
        |  and arms are retained               |  non-violent, non-secessionist leaders|
        |  EARLY 1956 -> army sent to restore  |  conciliation is the stated objective |
        |  peace and order                     |                                       |
        +--------------------------------------+---------------------------------------+
        v
MID-1957 -> the back of the armed rebellion is broken
        v
MODERATES -> Dr Imkongliba Ao and others come forward and negotiate for a state in the union
        v
1963 -> THE STATE OF NAGALAND COMES INTO EXISTENCE (within the Union, never independence)
AFTER -> politics in Nagaland follows the pattern of other states of the union""",
            [
                "Nagaland: the 1955 declaration, the army in early 1956 and "
                "statehood in 1963",
            ],
        ),
        (
            "A language trigger becomes the reorganisation of 1972",
            "timeline",
            """GRIEVANCE -> hill tribes have no cultural affinity with Assamese and Bengali plainsmen
          -> fear of "Assamization"; resentment at the attitudes of non-tribal officials
1960 -> Assamese leaders move to make Assamese the SOLE official language of the state
1960 -> hill parties merge into the ALL PARTY HILL LEADERS CONFERENCE; separate state demanded
     -> the Assam Official Language Act triggers hartals, demonstrations, a major agitation
1962 -> separate-state advocates sweep the tribal-area Assembly seats and boycott the Assembly
1969 -> constitutional amendment: MEGHALAYA as "a state within a state"
     -> complete autonomy EXCEPT law and order; shared High Court, Public Service Commission,
        Governor
1972 -> REORGANISATION OF THE NORTH-EAST
        MEGHALAYA becomes a separate state (Garo, Khasi and Jaintia tribes)
        MANIPUR and TRIPURA are simultaneously granted statehood
        NEFA is renamed ARUNACHAL PRADESH (statehood follows in 1987)
BRIDGE -> this is where language politics and tribal politics meet directly""",
            ["From a language trigger to the reorganisation of 1972"],
        ),
        (
            "Mizoram and Jharkhand: two endings, two lessons",
            "comparison",
            """MIZORAM -> the accommodation model, over twenty-one years
  1959 famine relief failure | 1961 Assamese made the state's official language -> grievance
  MIZO NATIONAL FRONT formed, LALDENGA president; elections contested, military wing built
  MAR 1966 independence declared, military uprising, attacks -> crushed within a few weeks
  1973 demand scaled down to a state within the union -> MIZORAM constituted a UNION TERRITORY
  1986 ACCORD -> arms surrendered, underground activity abandoned, full statehood granted
  FEB 1987 LALDENGA SWORN IN AS CHIEF MINISTER
  CAUTION -> the model case, NOT the universal outcome; no current security claim belongs here
JHARKHAND -> the demography model, an identity claim that outgrew its own base
  1950 JHARKHAND PARTY founded by JAIPAL SINGH | 1952 32 SEATS, main opposition in Bihar
  1957 25 seats | 1962 20 seats -> electoral decline
  Scheduled Tribes: Chota Nagpur 31.15% (1951) -> 30.94% (1971)
                    Santhal Parganas 44.67% (1951) -> 36.22% (1971)
  => nearly TWO-THIRDS of the region non-tribal in 1971
  1955 SRC refuses a Jharkhand state: "the region did not have a common language"
  1963 Jaipal Singh and much of the leadership join the Congress
  1972 JHARKHAND MUKTI MORCHA formed; SHIBU SOREN emerges; demand recast as REGIONAL
  LIMIT -> the shift was never complete; the movement stayed built on tribal identity""",
            [
                "Mizoram: March 1966, Union Territory in 1973, Accord in "
                "1986, statehood in February 1987",
                "Jharkhand: from a tribal state to a regional demand",
            ],
        ),
    ],
}


TOPIC_CHRONOLOGY = {
    "modern-indian-history-30": [
        "1921",
        "27 November 1947",
        "1948",
        "December 1948",
        "19 October 1952",
        "December 1952",
        "October 1953",
        "October 1955",
        "November 1956",
        "May 1960",
        "1963",
        "26 January 1965",
        "1966",
        "16 December 1967",
    ],
    "modern-indian-history-31": [
        "1948",
        "1955",
        "early 1956",
        "1957",
        "1963",
        "1969",
        "1972",
        "1973",
        "1986",
        "1987",
    ],
}

FORBIDDEN_TOPIC_PHRASES = {
    "modern-indian-history-30": [
        "the States Reorganisation Commission created the first linguistic "
        "state",
        "the SRC created the first linguistic state",
        "Andhra was created after the States Reorganisation Commission "
        "reported",
        "Bombay was split in 1956",
        "Bombay was bifurcated in 1956",
        "Haryana was created in 1956",
        "Punjab was reorganised in 1956",
        "the leadership always favoured linguistic states",
        "the Congress always opposed linguistic states",
        "the Commission recommended splitting Bombay and Punjab",
        "Hindi replaced English as the sole official language",
        "Hindi became the sole official language in 1965",
        "the 1965 agitation imposed Hindi",
        "English is the Constitution's associate official language",
        "the Constitution calls English the associate official language",
        "the Constitution designates English as the associate official "
        "language",
        "associate official language under Article 343",
        "linguistic reorganisation weakened India",
        "linguistic reorganisation weakened Indian unity",
        "the Punjabi Suba demand was purely communal",
        "every supporter of Punjabi was a communalist",
        "Punjab's reorganisation was purely linguistic",
        "regional inequality drove widespread separatism",
        "reorganisation was a single 1956 event",
        "the Shiv Sena was founded in 1960",
        "Chandigarh was given to Punjab alone",
        "Chandigarh was given to Haryana alone",
    ],
    "modern-indian-history-31": [
        "tribal policy aimed to assimilate",
        "Nehru favoured rapid assimilation",
        "Nehru favoured assimilation of the tribes",
        "the policy sought assimilation into the mainstream",
        "Nagaland was created in 1947",
        "Nagaland became a state in 1947",
        "Nagaland and Mizoram were granted independence",
        "the Fifth and Sixth Schedules are the same",
        "the Fifth Schedule governs the North-East",
        "the Sixth Schedule governs the other Scheduled Areas",
        "the Jharkhand movement was purely tribal throughout",
        "the Jharkhand movement remained exclusively tribal",
        "Mizoram's insurgency was never settled",
        "the 1951 Census recorded over 400 tribal communities",
        "according to the 1951 Census, over 400",
        "the Tribal Panchsheel was proclaimed in",
        "the Tribal Panchsheel of 1952",
        "the Tribal Panchsheel was announced in 1952",
        "all North-Eastern conflicts were settled on this model",
        "the whole North-East was settled on this model",
        "all North-Eastern insurgencies ended identically",
        "tribal alienation flowed from a flawed Constitution",
        "the constitutional design caused tribal alienation",
        "the current security situation in the North-East",
        "tribal integration was an unqualified success",
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
        f"- **Topic boundary:** Apply this definition only within "
        f"{topic_title}; retain the named actor, institution, date and "
        "chronological role."
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
            if len([line for line in body.splitlines() if line.strip()]) < 4:
                raise ValueError(
                    f"{key}: ASCII panel needs four nonblank body lines."
                )
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
        "scope": "Modern Indian History learner-v2 Topics 30-31",
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


def scannable_text(markdown: str) -> str:
    """Drop owner trap lines that quote a wrong formulation in order to reject it.

    The owners' UPSC-trap tables state the incorrect claim verbatim on a line
    marked with the cross glyph and then correct it. Those lines are preserved
    verbatim in the Optional Advanced Depth block, so a forbidden-formulation
    scan must ignore them and still police every asserted sentence.
    """

    return "\n".join(
        line for line in markdown.splitlines() if "\u274c" not in line
    )


def assert_topic_safeguards(config: dict[str, object], markdown: str) -> None:
    """Enforce chronology and high-risk factual boundaries for each topic."""

    key = str(config["key"])
    fact_text = "\n".join(statement for _, statement in config["facts"])
    cursor = -1
    for marker in TOPIC_CHRONOLOGY[key]:
        found = fact_text.find(marker, cursor + 1)
        if found < 0:
            raise ValueError(
                f"{key}: chronology marker missing/out of order: {marker}"
            )
        cursor = found
    for phrase in FORBIDDEN_TOPIC_PHRASES[key]:
        if phrase.casefold() in scannable_text(markdown).casefold():
            raise ValueError(
                f"{key}: forbidden factual formulation found: {phrase}"
            )

    if key == "modern-indian-history-30":
        strict = [
            "in 1921 amended its own constitution",
            "27 November 1947",
            "Linguistic Provinces Commission",
            "Justice S.K. Dar",
            "not to incorporate the linguistic principle in the Constitution",
            "December 1948",
            "Pattabhi Sitaramayya",
            "insistent and overwhelming",
            "Madras city",
            "19 October 1952",
            "fifty-eight days",
            "October 1953",
            "first linguistic state",
            "Fazl Ali",
            "K.M. Panikkar",
            "Hridaynath Kunzru",
            "October 1955",
            "opposed the splitting of Bombay",
            "did not have a common language",
            "November 1956",
            "fourteen states and six centrally administered territories",
            "Travancore-Cochin",
            "May 1960",
            "Article 343",
            "not a term used in the Constitution's own text",
            "Act No. 19 of 1963",
            "26 January 1965",
            "over sixty lives",
            "PEPSU",
            "joint capital",
            "must always be attributed to the source",
            "sons of the soil",
            "16 December 1967",
            "three-language formula",
            "Department of Official Language",
            "Patti Sriramalu",
            "cementing and integrating influence",
            "Rajni Kothari",
        ]
    else:
        strict = [
            "1971 Census",
            "over 400 tribal communities",
            "nearly 38 million",
            "6.9 per cent",
            "never be presented as 1951 figures or as current data",
            "Verrier Elwin",
            "museum specimens",
            "engulfed by the masses of Indian humanity",
            "progress in their own way",
            "own genius",
            "over-administration",
            "later label",
            "no exact proclamation year",
            "Article 46",
            "Tribal Advisory Councils",
            "Commissioner for Scheduled Castes and Scheduled Tribes",
            "Sixth Schedule",
            "Fifth Schedule",
            "never interchangeable",
            "belong to the Polity owner",
            "A.Z. Phizo",
            "early 1956",
            "middle of 1957",
            "Imkongliba Ao",
            "Nagaland came into existence in 1963",
            "All Party Hill Leaders Conference",
            "Assamization",
            "state within a state",
            "Garo, Khasi and Jaintia",
            "renamed Arunachal Pradesh",
            "March 1966",
            "February 1987",
            "not every North-Eastern conflict",
            "no current security assessment",
            "Jaipal Singh",
            "32 seats",
            "two-thirds",
            "Shibu Soren",
            "Janjatiya Gaurav Divas",
            "Ministry of Tribal Affairs",
        ]
    missing = [
        phrase
        for phrase in strict
        if phrase.casefold() not in markdown.casefold()
    ]
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
        raise ValueError(
            f"{key}: expected exactly 15 sessions, got {session_count}."
        )
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
        raise FileNotFoundError(
            f"Missing existing section manifest: {SECTION_MANIFEST}"
        )
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_keys = {item.get("topic_key") for item in catalog["topics"]}
    missing = [
        config["key"] for config in TOPICS if config["key"] not in catalog_keys
    ]
    if missing:
        raise ValueError(f"Topics missing from existing catalog: {missing}")


def validate_previous_batch_untouched() -> None:
    """Topics 26-29 must remain exactly as their own generators authored them."""

    expected = ["modern-indian-history-28", "modern-indian-history-29"]
    if [config["key"] for config in previous.TOPICS] != expected:
        raise ValueError("Topics 28-29 configuration was mutated on import.")
    if set(previous.PANEL_DATA) != set(expected):
        raise ValueError("Topics 28-29 panel data was mutated on import.")
    earlier_expected = ["modern-indian-history-26", "modern-indian-history-27"]
    if [config["key"] for config in earlier.TOPICS] != earlier_expected:
        raise ValueError("Topics 26-27 configuration was mutated on import.")
    if set(earlier.PANEL_DATA) != set(earlier_expected):
        raise ValueError("Topics 26-27 panel data was mutated on import.")


def main() -> int:
    validate_existing_section_contract()
    validate_previous_batch_untouched()
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
