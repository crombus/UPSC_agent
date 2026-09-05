"""Build Modern Indian History learner-v2 Topics 26-27.

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
import generate_modern_history_24_25_sequential as previous


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
    / "modern-indian-history-26-27-2026-08-31-sequential.json"
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
            ROOT
            / "knowledge-export"
            / "Prelims PYQ"
            / "QP-CSP-21-GeneralStudiesPaper-I-121021.pdf.md",
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
        26,
        "Post-War Upsurge: INA, RIN Mutiny & the Cabinet Mission "
        "(1945\u20131946)",
        "26_Post-War-Upsurge-INA-RIN-Mutiny-Cabinet-Mission.md",
        "26_Post-War-Upsurge-INA-RIN-Mutiny-Cabinet-Mission.md",
        "26_Post-War-Upsurge-INA-RIN-Mutiny-Cabinet-Mission-1945-1946_"
        "Complete-Topic-Package.md",
        [
            "basic/25_WWII-Cripps-Mission-and-Quit-India.md",
            "advanced/25_WWII-Cripps-Mission-and-Quit-India.md",
            "basic/27_Independence-and-Partition.md",
            "basic/17_Growth-of-Communalism-and-Muslim-League.md",
            "25_Second-World-War-Cripps-Mission-Quit-India-1939-1942_"
            "Complete-Topic-Package.md",
        ],
        [
            "https://dce.visionias.in/upsc-daily-news-summary/article/"
            "2026-08-17/the-indian-express/history/"
            "how-a-naval-mutiny-hastened-indias-independence",
        ],
        "A VisionIAS daily-news summary dated 17 August 2026, summarising an "
        "Indian Express article on the Royal Indian Navy uprising in the "
        "eightieth year since February 1946, is used only as a non-official "
        "study and current-affairs bridge. It is a private study-portal "
        "summary of a newspaper article, not a government commemoration, and "
        "this package makes no claim that any official or governmental "
        "commemoration of the RIN uprising took place in 2026. The scale "
        "figures that summary repeats \u2014 roughly 20,000 ratings, 78 ships "
        "and 20 shore establishments \u2014 are carried strictly as commonly "
        "cited estimates, and the popular attribution of a decisive judgement "
        "to Clement Attlee that appears there is recorded as a claim of that "
        "summary rather than as independently verified evidence. The "
        "headline framing of that article, that a naval mutiny hastened "
        "India's independence, is likewise a journalistic formulation and "
        "must never be converted into a claim of dispatch causation, because "
        "the uprising did not cause or trigger the dispatch of the Cabinet "
        "Mission, a decision the British Cabinet had already taken on 22 "
        "January 1946.",
        "The Basic and Advanced owner files were reconciled with the "
        "repository's Modern History OCR sources \u2014 Bipan Chandra's "
        "*Modern India*, *India's Struggle for Independence, 1857\u20131947* "
        "and *From Plassey to Partition* \u2014 for the INA, the Red Fort "
        "trials, the post-war upsurge, the 1944\u201345 negotiations, the "
        "1945\u201346 elections and the Cabinet Mission. INA recruitment "
        "strength is retained only as an attributed estimate, and the RIN "
        "scale figures are carried strictly as commonly cited estimates "
        "because the local Basic owner explicitly cautions against asserting "
        "ship numbers as settled fact. The local Bipan Chandra text of "
        "*India's Struggle for Independence* (book PDF page 512) states "
        "expressly that the decision to send the Cabinet Mission was taken by "
        "the British Cabinet on 22 January 1946 and that the announcement of "
        "19 February 1946 had been slated a week earlier, and it rejects R.P. "
        "Dutt's attribution of the mission's dispatch to the RIN revolt as "
        "untenable; that finding is carried into this package as a "
        "non-negotiable safeguard. The same text (book PDF pages 511 and "
        "514) records that the Congress lauded the spirit of the people and "
        "condemned the repression but did not officially support these "
        "struggles because it felt their tactics and timing were wrong, that "
        "Vallabhbhai Patel asked the ratings to surrender because he saw the "
        "British mobilisation for repression in Bombay and wrote to Nehru on "
        "22 February 1946 about the overpowering naval and military force "
        "gathered there, and that Jinnah's advice to surrender was addressed "
        "to Muslim ratings alone while the remaining ratings turned to the "
        "Congress and the Socialists; leadership responses are therefore "
        "presented as differentiated and never flattened into uniform "
        "support or one identical appeal.",
        "No verbatim official stem is asserted for this topic. The 2019 "
        "Prelims GS-I Q15 and 2021 Prelims GS-I Q47 entries are routed "
        "demand summaries taken from `_PYQ-ROUTING-PRELIMS-2018-2023.md`; the "
        "local 2021 Prelims paper export is an unusable OCR scan and no "
        "official 2018\u20132023 Prelims key is held, so no answer letter is "
        "asserted. The 2019 Mains GS-I Q12 entry is a routed demand summary "
        "with directive metadata from "
        "`_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md` and is not "
        "presented as a verbatim official stem.",
        [
            (
                "First INA of 1942 under Mohan Singh",
                "The first Indian National Army was raised in 1942 from "
                "Indian prisoners of war captured in Malaya and Singapore, "
                "with Mohan Singh as its military organiser and Japanese "
                "support behind it; this first experiment had effectively "
                "collapsed by early 1943 when Mohan Singh pressed for allied "
                "rather than subsidiary status and was removed and arrested.",
            ),
            (
                "Rash Behari Bose's political role",
                "Rash Behari Bose, the veteran revolutionary long resident in "
                "Japan, supplied the first INA's political cover through the "
                "Indian Independence League and its Tokyo and Bangkok "
                "conferences; his contribution was political sponsorship, "
                "organisation and negotiation, and he was not a field "
                "commander of the INA in Burma or Manipur.",
            ),
            (
                "Bose's reorganisation and Azad Hind, 1943",
                "Subhas Chandra Bose reached Southeast Asia in May 1943, "
                "revived and reorganised a second and much larger INA, and in "
                "October 1943 proclaimed the Provisional Government of Azad "
                "Hind at Singapore as supreme commander with the slogans "
                "'Dilli Chalo' and 'Give me blood and I will give you "
                "freedom'; the 1942 army under Mohan Singh and the 1943 army "
                "under Bose must never be treated as one continuous force.",
            ),
            (
                "Azad Hind symbols and the Rani of Jhansi Regiment",
                "The Rani of Jhansi Regiment, associated with Lakshmi Sahgal, "
                "symbolised women's participation in militant nationalism, "
                "and the Andaman and Nicobar islands were renamed Shaheed and "
                "Swaraj under the Azad Hind setup; these are symbolic and "
                "organisational facts about a claimant government, not "
                "evidence of military success.",
            ),
            (
                "Imphal-Kohima and the military verdict",
                "The Imphal campaign was launched on 8 March 1944 alongside "
                "Japanese forces and the INA's advance was broken at "
                "Imphal-Kohima; the INA's military record was one of defeat, "
                "and no answer may claim that the INA defeated British forces "
                "in the field or that it secured India's freedom by arms.",
            ),
            (
                "C.R. Formula, April 1944",
                "In April 1944 C. Rajagopalachari proposed the C.R. Formula, "
                "under which a post-war commission would demarcate contiguous "
                "districts of absolute Muslim majority where a plebiscite of "
                "the adult population would decide on Pakistan, with mutual "
                "arrangements for essential services and implementation "
                "deferred until after the full transfer of power; it was "
                "Rajagopalachari's personal initiative and not an official "
                "Congress offer.",
            ),
            (
                "Gandhi-Jinnah talks, September 1944",
                "Gandhi opened talks with Jinnah on the basis of that formula "
                "in July 1944, and the Gandhi-Jinnah talks broke down in "
                "September 1944 on what Gandhi himself described as a "
                "difference of perspective between separation within the "
                "family and Jinnah's demand for complete dissolution with "
                "sovereignty.",
            ),
            (
                "Wavell's Simla Conference of 1945",
                "Wavell, who had replaced Linlithgow as Viceroy in 1943, "
                "convened the Simla Conference of 25 June - 14 July 1945 to "
                "create an entirely Indian Executive Council; it broke down "
                "on Jinnah's demand for parity and his claim that the Muslim "
                "League alone could nominate every Muslim member, a claim the "
                "Congress refused while Maulana Abul Kalam Azad was its "
                "president.",
            ),
            (
                "Bose's officially reported death, August 1945",
                "Subhas Chandra Bose was officially reported to have died in "
                "an air crash in August 1945, and no account of his death "
                "beyond that official report may be asserted; the INA's "
                "post-war political impact therefore ran through the Red Fort "
                "trials rather than through his continued leadership.",
            ),
            (
                "The first Red Fort trial and its three defendants",
                "The first and most prominent INA trial at the Red Fort in "
                "1945-46 tried Shah Nawaz Khan, Prem Sahgal (also spelt "
                "Sehgal) and Gurbaksh Singh Dhillon together \u2014 a Muslim, "
                "a Hindu and a Sikh \u2014 and the defence was conducted by "
                "Bhulabhai Desai, Tej Bahadur Sapru, K.N. Katju, Jawaharlal "
                "Nehru and Asaf Ali, with the Congress running an INA Relief "
                "and Enquiry Committee.",
            ),
            (
                "Sentences remitted, not carried out",
                "The three officers were convicted of waging war against the "
                "King and sentenced to transportation for life, but the "
                "Commander-in-Chief remitted the sentences and the officers "
                "were released; the sentences of the first Red Fort trial "
                "were not carried out, and no officer tried in that case was "
                "executed.",
            ),
            (
                "Political effect inside a multi-causal endgame",
                "The INA's decisive effect was political rather than "
                "military: the trials made prosecution look like the "
                "punishment of patriotism and forced the government to "
                "abandon the wider prosecutions, but INA and RIN pressure "
                "must be weighed together with post-war British wartime "
                "exhaustion, four decades of mass nationalism, economic "
                "depletion, international decolonisation pressure and "
                "constitutional deadlock.",
            ),
            (
                "Elections of the winter of 1945-46",
                "In the elections of the winter of 1945-46 the Congress won "
                "over 90 per cent of the general seats provincially and 80.9 "
                "per cent of the general-constituency votes, while the Muslim "
                "League took 74.7 per cent of the votes cast in Muslim "
                "constituencies; because the poll was fought on separate "
                "electorates with an electorate of about 10 per cent of the "
                "population, it produced a representative mandate and was not "
                "a plebiscite that made Partition automatically inevitable.",
            ),
            (
                "Mission decided 22 January 1946, uprising began 18 February",
                "The British Cabinet took the decision to send the Cabinet "
                "Mission on 22 January 1946, almost a month before the Royal "
                "Indian Navy uprising began on 18 February 1946 at HMIS "
                "Talwar in Bombay out of demobilisation anxiety, poor rations "
                "and service conditions, racial insult and a set of demands "
                "that included better conditions, non-victimisation of "
                "strikers and free trials for INA detainees, and Attlee's "
                "House of Commons announcement of 19 February 1946 had "
                "already been slated a week earlier; the uprising therefore "
                "did not cause or trigger the dispatch of the Cabinet "
                "Mission, and on the repository's local Bipan Chandra text "
                "the immediate dispatch-causation claim is explicitly "
                "untenable even though the uprising remains central to the "
                "wider crisis of coercive legitimacy.",
            ),
            (
                "Scale of the uprising as commonly cited estimates",
                "The uprising spread from Bombay to other naval stations and, "
                "on commonly cited estimates that are source-dependent rather "
                "than settled, involved roughly 20,000 ratings, 78 ships and "
                "20 shore establishments; the repository's own Basic owner "
                "cautions against asserting ship numbers as fixed fact, so "
                "these figures must always be presented as commonly cited "
                "estimates and never as a verified count.",
            ),
            (
                "Short-lived, urban and service-centred",
                "The uprising was serious but short-lived, concentrated in "
                "urban naval stations and the service population, and it was "
                "surrendered within days; it was not a Congress-led "
                "nationwide revolution and it did not by itself end British "
                "rule in India.",
            ),
            (
                "Divided political responses to the uprising",
                "Political responses were differentiated rather than uniform: "
                "the Congress lauded the spirit of the people and condemned "
                "the government's repression but did not officially support "
                "the struggle because it judged the tactics and the timing "
                "wrong, Vallabhbhai Patel asked the ratings to surrender "
                "because he saw the overwhelming British mobilisation for "
                "repression in Bombay and wrote to Nehru on 22 February 1946 "
                "that the assembled naval and military force could "
                "exterminate them altogether, Muhammad Ali Jinnah's advice "
                "to surrender was addressed to Muslim ratings alone rather "
                "than to every rating, and organised sympathy strikes by "
                "workers and students in Bombay with support from communist "
                "and left organisations gave the uprising a civilian "
                "dimension, so no answer may claim that every national leader "
                "backed it or that one undifferentiated appeal was made to "
                "all ratings.",
            ),
            (
                "Cabinet Mission's long-term plan of 16 May 1946",
                "The Cabinet Mission of Pethick-Lawrence, Stafford Cripps and "
                "A.V. Alexander published its long-term constitutional plan "
                "on 16 May 1946: it rejected a sovereign Pakistan and "
                "proposed a united three-tier scheme of a Union, groups of "
                "provinces and provinces, in which the Union would deal with "
                "foreign affairs, defence and communications and would have "
                "the power to raise the finances required for those subjects.",
            ),
            (
                "Sections A, B and C and the separate 16 June proposal",
                "Under that plan the provinces were placed in three sections "
                "\u2014 Section A comprising Madras, Bombay, the United "
                "Provinces, Bihar, the Central Provinces and Orissa; Section "
                "B comprising Punjab, the North-West Frontier Province, Sind "
                "and British Baluchistan; and Section C comprising Bengal and "
                "Assam \u2014 so grouping was not Partition but a federal "
                "device inside a single union, and the Mission's separate "
                "interim-government proposal of 16 June 1946 is a different "
                "document from the 16 May long-term plan.",
            ),
            (
                "Incompatible readings and the endgame to December 1946",
                "Both parties used the plan on incompatible readings: the "
                "League announced acceptance on 6 June 1946 in so far as "
                "compulsory grouping implied the basis of Pakistan, Nehru's "
                "All-India Congress Committee statement of 7 July 1946 "
                "asserted that the Congress was bound only to enter the "
                "Constituent Assembly, and Jinnah withdrew the League's "
                "acceptance on 29 July 1946 after that constitutional "
                "dispute; Direct Action Day followed on 16 August 1946, the "
                "Interim Government was formed on 2 September 1946 with "
                "Congress members alone, the League joined it on 26 October "
                "1946, His Majesty's Government conceded the League's "
                "compulsory-grouping reading on 6 December 1946, and the "
                "Constituent Assembly met for the first time on 9 December "
                "1946 with the League boycotting it.",
            ),
        ],
        [
            "The 1942 INA under Mohan Singh and the 1943 INA reorganised by "
            "Subhas Chandra Bose are two distinct formations; never merge "
            "them into one continuous army.",
            "Rash Behari Bose's role was political and organisational "
            "leadership of the Indian Independence League; he must not be "
            "flattened into a field commander.",
            "The INA failed militarily at Imphal-Kohima; its decisive effect "
            "came through the Red Fort trials, and it did not secure India's "
            "freedom by arms.",
            "The first Red Fort trial ended in convictions whose sentences "
            "were remitted and the officers released; do not say they were "
            "executed.",
            "The RIN uprising began on 18 February 1946 at HMIS Talwar in "
            "Bombay; it was short-lived, urban and service-centred, not a "
            "Congress-led nationwide revolution, and it did not cause or "
            "trigger the dispatch of the Cabinet Mission, which the British "
            "Cabinet had already decided to send on 22 January 1946.",
            "The Congress did not officially support the RIN struggle because "
            "it judged the tactics and the timing wrong, Patel asked the "
            "ratings to surrender in view of the overwhelming British "
            "mobilisation for repression, and Jinnah's advice to surrender "
            "was addressed to Muslim ratings alone; do not claim uniform "
            "national-leadership support or one identical appeal to all "
            "ratings, and differentiate organised civilian and workers' "
            "sympathy and left support.",
            "Scale figures of roughly 20,000 ratings, 78 ships and 20 shore "
            "establishments are commonly cited estimates, not settled counts.",
            "The Cabinet Mission's long-term plan of 16 May 1946 and its "
            "interim-government proposal of 16 June 1946 are separate "
            "documents with separate contents.",
            "The Cabinet Mission rejected a sovereign Pakistan while "
            "proposing a united three-tier scheme; grouping was a federal "
            "device, not Partition.",
            "Congress and the League accepted and used the plan on "
            "incompatible readings, and the League withdrew its acceptance on "
            "29 July 1946 after the constitutional dispute; avoid a "
            "simplistic one-cause account of the failure.",
            "The 1945-46 elections were fought on separate electorates and a "
            "restricted franchise; they created a representative mandate, not "
            "a plebiscite that made Partition automatic.",
            "INA and RIN mattered to British confidence in the coercive "
            "apparatus, but they must be weighed with wartime exhaustion, "
            "long mass nationalism, economic and international pressures and "
            "constitutional deadlock.",
        ],
        [
            (
                10,
                "Distinguish the first Indian National Army raised in 1942 "
                "under Mohan Singh from the army reorganised by Subhas "
                "Chandra Bose in 1943, and state precisely what Rash Behari "
                "Bose contributed.",
                "Two successive formations with different leaderships, dates "
                "and purposes are joined only by a political umbrella that "
                "Rash Behari Bose supplied and then handed over, so the INA "
                "story is a succession, not a single continuous army.",
                [0, 1, 2],
            ),
            (
                10,
                "Explain why the Indian National Army's military failure at "
                "Imphal-Kohima was fully compatible with a major political "
                "effect through the Red Fort trials.",
                "A defeated army became politically decisive because the "
                "state chose to prosecute its officers, converting a military "
                "verdict into a public trial of nationalism that the "
                "government could not sustain.",
                [4, 9, 10],
            ),
            (
                15,
                "Examine the significance of the Royal Indian Navy uprising "
                "of February 1946, distinguishing carefully what it revealed "
                "from what it achieved.",
                "The uprising revealed that the loyalty of the armed services "
                "could no longer be assumed, but it achieved no political "
                "settlement, remained urban and service-centred, was "
                "surrendered within days and did not cause or trigger the "
                "dispatch of the Cabinet Mission that the British Cabinet had "
                "already decided upon on 22 January 1946.",
                [13, 14, 15, 16],
            ),
            (
                15,
                "Distinguish the Cabinet Mission's long-term plan of 16 May "
                "1946 from its interim-government proposal of 16 June 1946, "
                "and explain why grouping was not the same thing as "
                "Partition.",
                "The Mission produced two separate documents with two "
                "separate functions, and its grouping device was a federal "
                "arrangement inside one union rather than a route to two "
                "sovereign states.",
                [17, 18, 19],
            ),
            (
                20,
                "Critically examine why the Cabinet Mission scheme failed "
                "between June and December 1946, avoiding any single-cause "
                "explanation of the breakdown.",
                "Failure was produced by a deliberately ambiguous grouping "
                "clause, two mandates certified in mutually exclusive "
                "electorates, incompatible constitutional goals and a "
                "collapse of trust after Direct Action, so no single cause "
                "carries the explanation.",
                [12, 17, 18, 19],
            ),
            (
                20,
                "Assess the contribution of the post-war upsurge of 1945-46 "
                "to the British decision to transfer power, weighing it "
                "against wartime exhaustion, mass nationalism and "
                "constitutional deadlock.",
                "The upsurge mattered because it put the reliability of the "
                "coercive apparatus in question at the decisive moment, but "
                "it operated alongside exhaustion, decades of mass "
                "nationalism and deadlock rather than replacing them.",
                [10, 11, 15, 19],
            ),
        ],
        [
            (
                "2019",
                "Prelims GS-I Q15",
                "Indian National Movement leaders and organizational "
                "positions \u2014 recorded as a routed demand summary from "
                "`_PYQ-ROUTING-PRELIMS-2018-2023.md`, not as a verbatim "
                "official stem.",
                "routed-demand-summary-official-stem-and-key-unavailable",
                "The safe handling is to master leader-to-organisation "
                "matching within this owner without asserting an answer "
                "letter: Mohan Singh organised the first INA of 1942; Rash "
                "Behari Bose led the Indian Independence League and was not a "
                "field commander; Subhas Chandra Bose headed the Provisional "
                "Government of Azad Hind from October 1943; Lakshmi Sahgal is "
                "associated with the Rani of Jhansi Regiment; C. "
                "Rajagopalachari authored the C.R. Formula of April 1944; and "
                "Maulana Abul Kalam Azad was Congress president at Simla in "
                "1945. No option letter is asserted because no official "
                "2018-2023 Prelims key is held locally.",
            ),
            (
                "2021",
                "Prelims GS-I Q47",
                "Indian National Army officers in colonial Indian history "
                "\u2014 recorded as a routed demand summary from "
                "`_PYQ-ROUTING-PRELIMS-2018-2023.md`; the local 2021 paper "
                "export is an unusable OCR scan, so no verbatim stem is "
                "reproduced.",
                "routed-demand-summary-official-stem-and-key-unavailable",
                "The source-backed content this demand requires is the first "
                "Red Fort trial of Shah Nawaz Khan, Prem Sahgal (also spelt "
                "Sehgal) and Gurbaksh Singh Dhillon, tried together as a "
                "Muslim, a Hindu and a Sikh; the defence team of Bhulabhai "
                "Desai, Tej Bahadur Sapru, K.N. Katju, Jawaharlal Nehru and "
                "Asaf Ali; and the outcome in which the convictions stood but "
                "the sentences were remitted and the officers released. No "
                "option letter is asserted because no official key is held "
                "locally.",
            ),
            (
                "2019",
                "Mains GS-I Q12",
                "British imperial power and the transfer of power in the "
                "1940s \u2014 Assess, 15 marks, 250 words, recorded as a "
                "routed demand summary with directive metadata from "
                "`_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md` rather than "
                "as a verbatim official stem.",
                "routed-mains-demand-summary-not-verbatim",
                "A 250-word assessment should open with the claim that the "
                "decisive change between 1942 and 1946 lay in the reliability "
                "of the instruments of rule rather than in nationalist "
                "strength; evidence it with the Red Fort trials of 1945-46, "
                "the RIN uprising that began on 18 February 1946 at HMIS "
                "Talwar, and the two electoral mandates of the winter of "
                "1945-46; qualify it by recording that the uprising was "
                "short-lived and service-centred, that the Congress withheld "
                "official support because it judged the tactics and timing "
                "wrong while Patel asked the ratings to surrender and "
                "Jinnah's surrender advice was addressed to Muslim ratings "
                "alone, and by recording that "
                "the uprising did not cause or trigger the dispatch of the "
                "Cabinet Mission, whose despatch the British Cabinet had "
                "settled on 22 January 1946; and close by weighing "
                "wartime exhaustion, economic depletion, international "
                "decolonisation pressure and the constitutional deadlock of "
                "the Cabinet Mission alongside the upsurge.",
            ),
        ],
        [
            "Mohan Singh",
            "Rash Behari Bose",
            "Indian Independence League",
            "Provisional Government of Azad Hind",
            "Dilli Chalo",
            "Rani of Jhansi Regiment",
            "Lakshmi Sahgal",
            "Shaheed",
            "Swaraj",
            "Imphal-Kohima",
            "C.R. Formula",
            "Gandhi-Jinnah talks",
            "Simla Conference",
            "Wavell",
            "Maulana Abul Kalam Azad",
            "Shah Nawaz Khan",
            "Prem Sahgal",
            "Sehgal",
            "Gurbaksh Singh Dhillon",
            "Bhulabhai Desai",
            "HMIS Talwar",
            "18 February 1946",
            "22 January 1946",
            "19 February 1946",
            "dispatch-causation claim",
            "Pethick-Lawrence",
            "Stafford Cripps",
            "A.V. Alexander",
            "British Baluchistan",
            "Direct Action Day",
            "Interim Government",
            "Constituent Assembly",
            "Prelims GS-I Q47",
            "Mains GS-I Q12",
        ],
    ),
    base.topic(
        27,
        "Independence & Partition (1946\u20131947)",
        "27_Independence-and-Partition.md",
        "27_Independence-and-Partition.md",
        "27_Independence-and-Partition-1946-1947_Complete-Topic-Package.md",
        [
            "basic/26_Post-War-Upsurge-INA-RIN-Mutiny-Cabinet-Mission.md",
            "advanced/26_Post-War-Upsurge-INA-RIN-Mutiny-Cabinet-Mission.md",
            "basic/28_Integration-of-Princely-States.md",
            "basic/17_Growth-of-Communalism-and-Muslim-League.md",
            "25_Second-World-War-Cripps-Mission-Quit-India-1939-1942_"
            "Complete-Topic-Package.md",
        ],
        [
            "https://culture.gov.in/events/"
            "ministry-culture-marks-partition-horrors-remembrance-day-2026-"
            "across-delhi-amritsar-and",
        ],
        "The Ministry of Culture's own event page records that Partition "
        "Horrors Remembrance Day was observed on 13 and 14 August 2026 "
        "through commemorative programmes in Delhi, Amritsar and Kolkata, "
        "along with observances organised across States and Union "
        "Territories, and that these included exhibitions, documentaries, "
        "survivor testimonies, cultural programmes and silent marches paying "
        "homage to the victims and survivors of Partition. Only claims "
        "directly supported by that page are used here: no casualty figure, "
        "no comparative claim and no political interpretation is drawn from "
        "it, and the observance is treated as evidence of official public "
        "remembrance rather than as historical evidence about 1947 itself.",
        "The Basic and Advanced owner files were reconciled with the "
        "repository's Modern History OCR sources \u2014 Bipan Chandra's "
        "*Modern India*, *India's Struggle for Independence, 1857\u20131947* "
        "and Sekhar Bandyopadhyay's *From Plassey to Partition* \u2014 for "
        "the collapse of the Cabinet Mission scheme, Direct Action Day, the "
        "3 June Plan, the Indian Independence Act and the boundary awards. "
        "Displacement is retained only as the owners' broad 10 to 15 million "
        "estimate, and death tolls are left unquantified because the local "
        "sources treat them as contested.",
        "The only demand routed to this owner in the local ledgers is 2021 "
        "Prelims GS-I Q50 on International Mother Language Day and the Bangla "
        "language movement, which the Basic owner itself records as "
        "unresolved locally; no date, event or UNESCO designation is asserted "
        "for it. The 2019 Mains GS-I Q12 transfer-of-power demand is routed "
        "in `_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md` to the adjacent "
        "Topic 26 owner and is carried here only as a shared endgame demand, "
        "clearly labelled as such. No official answer key is held for either "
        "entry, and no paraphrase is claimed to be verbatim.",
        [
            (
                "Cabinet Mission attempted unity",
                "The Cabinet Mission of 1946 rejected a sovereign Pakistan "
                "and proposed a united three-tier scheme of Union, groups and "
                "provinces; it attempted to preserve unity and did not "
                "partition India, so Partition must be explained by the "
                "collapse of that scheme and by what followed it rather than "
                "by the Mission itself.",
            ),
            (
                "Direct Action Day, 16 August 1946",
                "Direct Action Day on 16 August 1946 was a Muslim League "
                "political call issued after the constitutional deadlock; in "
                "Calcutta it was followed by the killings remembered as the "
                "Great Calcutta Killings, and the political call, the "
                "Calcutta violence and the later regional violence are three "
                "separable things that a careful answer keeps distinct.",
            ),
            (
                "Regional violence of 1946-47 without collective guilt",
                "Communal violence spread through Noakhali, Bihar and the "
                "Punjab in 1946-47 in reciprocal waves driven by "
                "organisations, local leaderships, rumour and armed bands; "
                "agency must be assigned to those organisations and "
                "leaderships and never to whole communities, and no religious "
                "community may be described as collectively guilty.",
            ),
            (
                "Attlee's statement of 20 February 1947",
                "Attlee announced on 20 February 1947 that Britain would "
                "transfer power to responsible Indian hands not later than "
                "June 1948, an announcement that must be distinguished from "
                "his earlier statement of 15 March 1946 that a minority would "
                "not be allowed to place a veto on the progress of the "
                "majority.",
            ),
            (
                "Mountbatten as the last Viceroy",
                "Lord Mountbatten arrived in March 1947 as the last Viceroy "
                "and converted the June 1948 outer limit into a far shorter "
                "timetable; the acceleration is an analytical fact about how "
                "Partition was executed and about the disorder that followed, "
                "not an explanation of why Partition was chosen.",
            ),
            (
                "The 3 June Plan as a political plan",
                "The Mountbatten Plan announced on 3 June 1947 was a "
                "political plan: it accepted Partition and provided for the "
                "division of Punjab and Bengal, referendums in the North-West "
                "Frontier Province and Sylhet, and boundary commissions; it "
                "was not an Act of Parliament and did not by itself transfer "
                "power.",
            ),
            (
                "Assembly votes divided Punjab and Bengal",
                "The decision to divide Punjab and Bengal was taken by "
                "separate votes of the notional Hindu-majority and "
                "Muslim-majority halves of each provincial legislative "
                "assembly, a legislative mechanism entirely distinct from a "
                "popular referendum.",
            ),
            (
                "Referendums in the North-West Frontier Province and Sylhet",
                "The North-West Frontier Province and the Sylhet district of "
                "Assam decided their future by referendum under the 3 June "
                "Plan, and both results took them into Pakistan; the "
                "Congress-aligned boycott of the North-West Frontier Province "
                "poll is standard knowledge rather than a claim drawn from "
                "the local owner files, and the referendum route applied only "
                "to these two cases.",
            ),
            (
                "Indian Independence Act: assent and commencement",
                "The Indian Independence Act received Royal Assent on 18 July "
                "1947 and legally created the two independent dominions of "
                "India and Pakistan from 15 August 1947; Pakistan's later "
                "observance of 14 August as its national day is a separate "
                "commemorative fact and must never be presented as the Act's "
                "date of commencement.",
            ),
            (
                "The lapse of British paramountcy",
                "The Act provided that British paramountcy over the princely "
                "states would lapse; paramountcy lapsed and did not pass "
                "wholesale to India or to Pakistan, which is precisely why "
                "accession had to be negotiated state by state rather than "
                "inherited automatically.",
            ),
            (
                "Two Radcliffe boundary commissions",
                "Two separate boundary commissions, one for Punjab and one "
                "for Bengal, were chaired by Cyril Radcliffe, a British "
                "lawyer with no prior Indian experience; each commission had "
                "an equal number of Congress-nominated and League-nominated "
                "judges, so when those members divided the decisions fell to "
                "the chairman.",
            ),
            (
                "Radcliffe awards published on 17 August 1947",
                "The Radcliffe awards were published on 17 August 1947, after "
                "the transfer of power, so people in many border districts "
                "did not know which state they were in when independence "
                "came; that delay aggravated uncertainty and flight, but the "
                "award alone did not cause all the violence, which had begun "
                "long before the line was drawn.",
            ),
            (
                "Three instruments, three functions",
                "The three instruments of 1947 performed different functions "
                "and were separated in time and authority: the 3 June Plan "
                "was the political decision, the Indian Independence Act was "
                "the legal enactment, and the two Radcliffe awards were the "
                "boundary mechanism.",
            ),
            (
                "Congress acceptance as reluctant pragmatism",
                "Congress acceptance of Partition was reluctant and "
                "pragmatic rather than programmatic: it followed the "
                "constitutional deadlock of 1946, escalating violence and the "
                "leadership's judgement that a weak centre with compulsory "
                "grouping would produce an ungovernable state, and it must "
                "never be presented as long-standing Congress policy.",
            ),
            (
                "Partition was not inevitable in 1906, 1940 or 1946",
                "Partition was not made inevitable by the founding of the "
                "Muslim League in 1906, by the Lahore Resolution of 1940 or "
                "by the elections of 1945-46; it is best explained as "
                "cumulative structure plus contingent decisions, and both "
                "parties accepted the Cabinet Mission scheme in some form in "
                "June and July 1946, after the electoral verdict.",
            ),
            (
                "No single-villain explanation",
                "No single-villain explanation survives scrutiny: colonial "
                "constitutional engineering from the separate electorates of "
                "1909 onwards and the hasty withdrawal of 1947, the Muslim "
                "League's strategy after 1940, Congress calculations about a "
                "strong centre, communal organisations on every side, mass "
                "fear and violence, and distinct regional dynamics in Punjab, "
                "Bengal and the United Provinces each carry part of the "
                "explanation.",
            ),
            (
                "Displacement as a broad estimate, deaths contested",
                "Displacement across the new border is commonly estimated at "
                "around 10 to 15 million people, and that figure may be used "
                "only as a broad estimate; death tolls are contested across a "
                "wide range and must not be stated with false precision in "
                "any answer.",
            ),
            (
                "Gandhi in Calcutta, not celebrating in Delhi",
                "At independence Gandhi was in Calcutta and Bengal working "
                "for communal peace, not celebrating in Delhi, while "
                "Jawaharlal Nehru delivered the 'Tryst with Destiny' speech "
                "in the Constituent Assembly; the contrast between the two "
                "locations is itself the clearest statement of what that "
                "moment meant.",
            ),
            (
                "Three simultaneous registers of independence",
                "Legal transfer, political triumph and humanitarian "
                "catastrophe are analytically simultaneous: the same weeks "
                "produced an unprecedented constitutional transfer in the "
                "colonial world, the fulfilment of a mass national movement, "
                "and mass displacement and killing that the transfer's speed "
                "and its unpoliced boundary directly aggravated.",
            ),
            (
                "Aftermath, institutions and public remembrance",
                "Partition's aftermath became the new state's first "
                "administrative test \u2014 refugee rehabilitation, a divided "
                "army, civil service and treasury, disrupted rivers, railways "
                "and trade, and minority questions on both sides \u2014 and "
                "it strengthened the constitutional case for a strong centre "
                "and for secularism as a state commitment; the Ministry of "
                "Culture's observance of Partition Horrors Remembrance Day on "
                "13 and 14 August 2026 in Delhi, Amritsar and Kolkata, with "
                "exhibitions, documentaries, survivor testimonies and silent "
                "marches, is this package's only current-affairs anchor.",
            ),
        ],
        [
            "The Cabinet Mission attempted to preserve unity and did not "
            "partition India; Partition followed the collapse of its scheme.",
            "Direct Action Day was 16 August 1946; keep the political call, "
            "the Calcutta killings and the later regional violence "
            "analytically separate.",
            "Assign responsibility for communal violence to organisations, "
            "leaderships and armed bands, never to whole communities as "
            "collective guilt.",
            "Attlee's statement of 20 February 1947 set a transfer deadline "
            "of not later than June 1948; do not confuse it with his 15 March "
            "1946 statement on the minority veto.",
            "The 3 June Plan is the political plan, the Indian Independence "
            "Act is the legal enactment, and the two Radcliffe awards are the "
            "boundary mechanism.",
            "Punjab and Bengal were divided by assembly votes, while the "
            "North-West Frontier Province and Sylhet used referendums; these "
            "are different mechanisms.",
            "The Indian Independence Act received Royal Assent on 18 July "
            "1947 and created the dominions from 15 August 1947; do not "
            "conflate Pakistan's later 14 August national-day observance with "
            "the Act's commencement.",
            "The Radcliffe awards were published on 17 August 1947, after the "
            "transfer; explain the resulting uncertainty without claiming the "
            "award alone caused all the violence.",
            "British paramountcy lapsed; it did not pass wholesale to India, "
            "which is why accession had to be negotiated.",
            "Congress acceptance of Partition was reluctant and pragmatic, "
            "tied to deadlock, violence and a preference for a workable "
            "strong centre; it was not long-standing Congress policy.",
            "Partition was not inevitable in 1906, 1940 or 1946; explain it "
            "through cumulative structure plus contingent decisions, and "
            "refuse a single-villain account.",
            "State displacement only as the broad 10 to 15 million estimate "
            "and never quantify deaths; Gandhi was in Calcutta and Bengal, "
            "not celebrating in Delhi.",
        ],
        [
            (
                10,
                "Distinguish the functions of the 3 June Plan, the Indian "
                "Independence Act and the two Radcliffe awards in the "
                "transfer of power of 1947.",
                "Three different acts of authority \u2014 a political "
                "decision, a legal enactment and a boundary determination "
                "\u2014 were separated in time and authority, and that "
                "separation is itself part of the explanation of the disorder "
                "of August 1947.",
                [5, 8, 11, 12],
            ),
            (
                10,
                "Explain why the Cabinet Mission cannot be described as the "
                "instrument that partitioned India.",
                "The Mission rejected a sovereign Pakistan and offered a "
                "united three-tier union, so Partition must be traced to the "
                "collapse of that scheme and the decisions that followed it.",
                [0, 1, 14],
            ),
            (
                15,
                "Examine the mechanisms through which Partition was actually "
                "carried out in 1947, distinguishing assembly votes, "
                "referendums and boundary commissions.",
                "Partition was executed through three distinct procedures, "
                "each with its own constituency and legal character, and "
                "conflating them produces both factual error and a false "
                "picture of how consent was measured.",
                [6, 7, 10, 11],
            ),
            (
                15,
                "Assess Congress's acceptance of Partition in 1947 as a "
                "reluctant and pragmatic decision rather than a long-standing "
                "policy.",
                "Acceptance followed deadlock, violence and a judgement about "
                "governability, so it is best read as a constrained choice "
                "made late rather than as a programme pursued early.",
                [0, 13, 14, 15],
            ),
            (
                20,
                "Critically examine the claim that Partition was inevitable, "
                "using cumulative structure and contingent decisions rather "
                "than a single-villain explanation.",
                "Four decades of communal representation made Partition "
                "possible and a chain of datable decisions in 1946 and 1947 "
                "made it actual, so inevitability is an interpretive claim "
                "rather than a demonstrated fact.",
                [0, 13, 14, 15],
            ),
            (
                20,
                "Discuss why independence and Partition must be assessed "
                "together as legal transfer, political triumph and "
                "humanitarian catastrophe.",
                "The same weeks delivered an unprecedented constitutional "
                "transfer, the fulfilment of a mass movement and a "
                "displacement crisis, and an answer that records only one "
                "register has answered only part of the question.",
                [11, 16, 17, 18],
            ),
        ],
        [
            (
                "2021",
                "Prelims GS-I Q50",
                "International Mother Language Day and the Bangla language "
                "movement \u2014 recorded as a routed demand summary from "
                "`_PYQ-ROUTING-PRELIMS-2018-2023.md`, which the Basic owner "
                "itself flags as unresolved in the locally held sources.",
                "routed-demand-unresolved-locally-no-claim-asserted",
                "This package deliberately asserts nothing about this demand. "
                "The subject matter concerns post-1947 East Pakistan and "
                "later Bangladesh and has no supporting content in the source "
                "books held here, so no date, event, commemorative "
                "designation or option letter is stated. The honest handling "
                "is to record the gap, keep the 1946-47 owner's scope intact, "
                "and treat this as a single-fact Prelims point to be closed "
                "from a verified official source when one is held.",
            ),
            (
                "2019",
                "Mains GS-I Q12",
                "British imperial power and the transfer of power in the "
                "1940s \u2014 Assess, 15 marks, 250 words; routed in "
                "`_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md` to the "
                "adjacent Topic 26 owner and carried here only as a shared "
                "endgame demand, not as a demand owned by this topic.",
                "adjacent-owner-routed-demand-shared-endgame-not-verbatim",
                "For the 1947 half of this shared demand, assess the transfer "
                "through its instruments and their timing: Attlee's statement "
                "of 20 February 1947 set the June 1948 outer limit, "
                "Mountbatten compressed it, the 3 June Plan supplied the "
                "political decision, the Indian Independence Act received "
                "Royal Assent on 18 July 1947 and created the dominions from "
                "15 August 1947, and the Radcliffe awards were published on "
                "17 August 1947. Qualify the assessment by noting that "
                "paramountcy lapsed rather than passing wholesale to India, "
                "and close with the two registers of triumph and catastrophe. "
                "No answer key is claimed and no wording here is presented as "
                "the official stem.",
            ),
        ],
        [
            "Cabinet Mission",
            "Direct Action Day",
            "Great Calcutta Killings",
            "Noakhali",
            "Bihar",
            "Punjab",
            "Attlee",
            "20 February 1947",
            "June 1948",
            "Mountbatten",
            "3 June Plan",
            "North-West Frontier Province",
            "Sylhet",
            "Indian Independence Act",
            "Royal Assent",
            "18 July 1947",
            "15 August 1947",
            "paramountcy",
            "Cyril Radcliffe",
            "17 August 1947",
            "Tryst with Destiny",
            "Calcutta",
            "10 to 15 million",
            "Partition Horrors Remembrance Day",
            "Ministry of Culture",
            "Prelims GS-I Q50",
            "Mains GS-I Q12",
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
    "modern-indian-history-26": [
        authored_session(
            "Two Indian National Armies: 1942 under Mohan Singh, 1943 under Bose",
            "There were two successive Indian National Armies, and confusing "
            "them is the commonest factual error in this topic: the first was "
            "raised in 1942 under Mohan Singh and had effectively collapsed "
            "by early 1943, while the second was reorganised by Subhas "
            "Chandra Bose from May 1943 on a wholly different political "
            "footing.",
            [
                "The first INA was raised in 1942 from Indian prisoners of "
                "war captured in Malaya and Singapore, with Japanese support "
                "and Mohan Singh as its military organiser.",
                "Mohan Singh pressed for allied rather than subsidiary status "
                "for the force and was removed and arrested, so the first "
                "experiment had effectively collapsed by early 1943.",
                "Subhas Chandra Bose reached Southeast Asia in May 1943 and "
                "reorganised a second, larger and politically directed army "
                "under a claimant government.",
                "The two formations differ in date, leadership, size and "
                "political purpose, so a single continuous account of 'the "
                "INA' is factually wrong.",
            ],
            "Never merge the 1942 army under Mohan Singh with the 1943 army "
            "reorganised by Subhas Chandra Bose; name the year and the leader "
            "every time you use the abbreviation INA.",
            "Open any INA answer by separating the 1942 and 1943 formations "
            "before you discuss the Imphal campaign or the Red Fort trials.",
            """1942 -> FIRST INA -> Mohan Singh + Indian POWs (Malaya, Singapore) + Japanese support
EARLY 1943 -> first INA collapses; Mohan Singh removed and arrested over subsidiary status
MAY 1943 -> Subhas Chandra Bose reaches Southeast Asia
OCT 1943 -> SECOND INA under Azad Hind -> larger, politically directed, claimant government
RULE -> two armies, two dates, two leaderships; never one continuous force.""",
            "The 'first INA' is the 1942 force organised from Indian "
            "prisoners of war under Mohan Singh, a formation distinct from "
            "the second INA that Subhas Chandra Bose reorganised from May "
            "1943.",
        ),
        authored_session(
            "Rash Behari Bose: political cover, not field command",
            "Rash Behari Bose supplied the first INA's political legitimacy "
            "and civilian umbrella through the Indian Independence League, "
            "and flattening him into a battlefield commander erases the "
            "difference between the movement's political and military wings.",
            [
                "Rash Behari Bose was a veteran revolutionary of the "
                "Ghadr-era conspiracies who had lived in Japan since the "
                "First World War years.",
                "He convened and presided over the Indian Independence "
                "League's Tokyo and Bangkok conferences, which gave the "
                "prisoner-of-war army a civilian political roof.",
                "He handed the leadership of the Indian Independence League "
                "and of the INA to Subhas Chandra Bose in 1943.",
                "His contribution was political sponsorship, organisation and "
                "negotiation with the Japanese authorities, not command of "
                "troops in Burma or Manipur.",
            ],
            "Rash Behari Bose was not a field commander of the INA; describe "
            "his role as political and organisational leadership of the "
            "Indian Independence League.",
            "Use this distinction whenever a question asks who 'led' the INA, "
            "because the accurate answer separates political sponsorship from "
            "military command.",
            """INDIAN INDEPENDENCE LEAGUE  (political roof over the POW army)
|-- RASH BEHARI BOSE -> convenes Tokyo and Bangkok conferences; negotiates with Japan
|-- HANDOVER 1943 -> League and INA leadership pass to Subhas Chandra Bose
`-- FIELD COMMAND -> Mohan Singh (1942), then Bose's INA officers (1943-45)
RULE -> political sponsorship and field command are two different offices.""",
            "Rash Behari Bose's role was the political and organisational "
            "sponsorship of the INA through the Indian Independence League, "
            "and not field command of its troops.",
        ),
        authored_session(
            "Azad Hind: provisional government, army and symbols",
            "Bose's real achievement was to convert a body of prisoners into "
            "a claimant government with an army, a cabinet, foreign "
            "recognition and a territorial claim, and the symbols that follow "
            "from that are examinable in their own right.",
            [
                "In October 1943 Bose proclaimed the Provisional Government "
                "of Azad Hind at Singapore and became its supreme commander.",
                "The slogans 'Dilli Chalo' and 'Give me blood and I will give "
                "you freedom' belong to this reorganised phase, not to the "
                "1942 force.",
                "The Rani of Jhansi Regiment, associated with Lakshmi Sahgal, "
                "marked women's participation in militant nationalism.",
                "The Andaman and Nicobar islands were renamed Shaheed and "
                "Swaraj under the Azad Hind setup.",
            ],
            "Treat these as symbolic and organisational facts about a "
            "claimant government; recognition came from Japan and its allies, "
            "and none of them is evidence of military success.",
            "Use the Azad Hind symbols to explain why the post-war trials "
            "could not be treated as ordinary courts-martial.",
            """PROVISIONAL GOVERNMENT OF AZAD HIND (Singapore, October 1943)
|-- SUPREME COMMANDER -> Subhas Chandra Bose | SLOGANS -> "Dilli Chalo"
|-- ARMY -> reorganised INA | WOMEN'S UNIT -> Rani of Jhansi Regiment (Lakshmi Sahgal)
|-- TERRITORY CLAIMED -> Andaman and Nicobar renamed Shaheed and Swaraj
RULE -> a claimant government's symbols, not a record of battlefield success.""",
            "Azad Hind was the provisional government proclaimed by Subhas "
            "Chandra Bose at Singapore in October 1943, with its own supreme "
            "commander, army, symbols and claimed territory.",
        ),
        authored_session(
            "Imphal-Kohima: state the military verdict plainly",
            "The INA's military record was defeat: the campaign launched on "
            "8 March 1944 was broken at Imphal-Kohima, and an answer that "
            "softens this loses the very contrast on which the topic's "
            "argument depends.",
            [
                "The Imphal campaign was launched on 8 March 1944 alongside "
                "Japanese forces, with Delhi as its declared objective.",
                "The advance was broken at Imphal and Kohima, and the retreat "
                "through Burma destroyed the force as a fighting formation.",
                "Supply failure, monsoon conditions and Allied air power "
                "decided the campaign; the outcome was military, not a "
                "verdict on Indian nationalism.",
                "Bose was officially reported to have died in an air crash in "
                "August 1945, and no account of his death beyond that "
                "official report may be asserted.",
            ],
            "Do not soften the military verdict; the INA lost its campaign, "
            "and its political effect must be argued from the trials rather "
            "than from the battlefield.",
            "Use the plain statement of defeat as the opening premise of the "
            "'defeat produced political victory' argument.",
            """8 MAR 1944 -> Imphal campaign launched with Japanese forces -> objective: Delhi
IMPHAL + KOHIMA -> advance broken; retreat through Burma destroys the formation
CAUSES -> supply failure + monsoon + Allied air power (military, not political)
AUG 1945 -> Bose officially reported dead in an air crash; nothing beyond the report
RULE -> the military verdict is defeat; the political verdict comes later.""",
            "Imphal-Kohima names the 1944 battles at which the INA's advance "
            "into India was broken, fixing the army's military record as one "
            "of defeat.",
        ),
        authored_session(
            "The first Red Fort trial and its cross-communal symbolism",
            "The first and most prominent Red Fort trial mattered because of "
            "who was in the dock: a Muslim, a Hindu and a Sikh tried together "
            "turned a prosecution into an unintended demonstration of "
            "national unity at the exact moment communal politics was "
            "hardening.",
            [
                "The trial in 1945-46 tried Shah Nawaz Khan, Prem Sahgal "
                "(also spelt Sehgal) and Gurbaksh Singh Dhillon together.",
                "Their cross-communal composition was seized on by nationalist "
                "opinion precisely because communal negotiation had just "
                "failed at Simla.",
                "The defence was conducted by Bhulabhai Desai, Tej Bahadur "
                "Sapru, K.N. Katju, Jawaharlal Nehru and Asaf Ali.",
                "The Congress organised an INA Relief and Enquiry Committee "
                "and made the INA cause an election plank in the winter "
                "campaign.",
            ],
            "Name all three defendants and record the spelling variant Prem "
            "Sahgal or Sehgal; the cross-communal point collapses if only one "
            "or two names are given.",
            "Use the composition of the accused as the evidence that supports "
            "any claim about the trials producing brief cross-communal "
            "solidarity.",
            """RED FORT TRIAL (1945-46) -> three officers tried together
|-- SHAH NAWAZ KHAN (Muslim) | PREM SAHGAL / SEHGAL (Hindu) | G.S. DHILLON (Sikh)
|-- DEFENCE -> Bhulabhai Desai, Tej Bahadur Sapru, K.N. Katju, Nehru, Asaf Ali
|-- CONGRESS -> INA Relief and Enquiry Committee; INA becomes an election plank
EFFECT -> prosecution reads as punishment of patriotism across three communities.""",
            "The first Red Fort trial is the 1945-46 joint court-martial of "
            "Shah Nawaz Khan, Prem Sahgal (Sehgal) and Gurbaksh Singh Dhillon "
            "for waging war against the King.",
        ),
        authored_session(
            "What actually happened to the Red Fort sentences",
            "The outcome is a precise fact that candidates routinely get "
            "wrong: the convictions stood, but the sentences were remitted "
            "and the officers walked free, which is exactly why the trials "
            "count as a government retreat.",
            [
                "The three officers were convicted of waging war against the "
                "King and sentenced to transportation for life.",
                "The Commander-in-Chief remitted those sentences and the "
                "officers were released.",
                "The Commander-in-Chief recorded that general opinion in the "
                "army favoured leniency, and the Governor of the North-West "
                "Frontier Province urged abandoning the trials.",
                "The wider programme of prosecutions was abandoned, so the "
                "sentences of the first Red Fort trial were not carried out "
                "and no officer tried in that case was executed.",
            ],
            "Never write that the Red Fort defendants were executed; the "
            "convictions were recorded, the sentences remitted and the "
            "prosecutions abandoned.",
            "Use the remission as the concrete evidence that the state could "
            "no longer enforce military discipline against national opinion.",
            """CONVICTION -> waging war against the King -> transportation for life
REMISSION -> Commander-in-Chief remits the sentences -> officers released
PRESSURE -> army opinion favours leniency; NWFP Governor urges abandonment
RESULT -> wider prosecutions abandoned; the sentences were not carried out
RULE -> a government retreat, not an execution.""",
            "Remission here means the Commander-in-Chief's cancellation of "
            "the transportation sentences imposed in the first Red Fort "
            "trial, leaving the convictions on record but the officers free.",
        ),
        authored_session(
            "Weighing INA and RIN inside a multi-causal endgame",
            "INA and RIN pressure mattered because they put the loyalty of "
            "the coercive apparatus in question at the decisive moment, but "
            "they must be weighed alongside other causes rather than "
            "substituted for them.",
            [
                "The Raj had always governed through Indian soldiers, police "
                "and officials, so doubt about their reliability struck at "
                "the basis of rule itself.",
                "Post-war British wartime exhaustion, economic depletion and "
                "a Labour government made a long coercive campaign "
                "unaffordable.",
                "Four decades of mass nationalism, from 1920-22 through "
                "1930-34 to 1942, had already made government by consent "
                "impossible.",
                "International decolonisation pressure and the constitutional "
                "deadlock of 1946 completed the picture, so the upsurge "
                "sharpened the endgame without deciding it alone.",
            ],
            "Do not claim that the INA, the RIN uprising or the two together "
            "won India's freedom; rank the causes explicitly, give the "
            "collaboration collapse its weight without inflating it, and "
            "never convert influence on British confidence into a claim that "
            "the uprising produced a specific constitutional initiative such "
            "as the Cabinet Mission.",
            "Use this weighting paragraph in any 'why did the British leave' "
            "answer, and state your ranking before you list evidence.",
            """WHY THE BRITISH LEFT -> ranked, not listed
|-- COLLABORATION COLLAPSE -> services, police, armed forces no longer reliable
|-- WARTIME EXHAUSTION -> economic depletion, demobilisation, Labour government
|-- MASS NATIONALISM -> 1920-22, 1930-34, 1942 -> consent already impossible
|-- INTERNATIONAL + DEADLOCK -> decolonisation climate; 1946 constitutional impasse
CHRONOLOGY GUARD -> Mission dispatch decided 22 Jan 1946, before the 18 Feb strike
RULE -> INA and RIN sharpen the timing; they do not replace the other causes.""",
            "The multi-causal endgame is the ranked explanation of British "
            "withdrawal in which collaboration collapse, wartime exhaustion, "
            "mass nationalism, international pressure and constitutional "
            "deadlock all operate together.",
        ),
        authored_session(
            "Failed negotiations of 1944-45: C.R. Formula, Gandhi-Jinnah, Simla",
            "Every scheme between 1944 and 1945 failed at the same point, "
            "which was not the quantum of self-government but the question of "
            "who was entitled to represent Indian Muslims.",
            [
                "The C.R. Formula of April 1944 offered a plebiscite of the "
                "adult population in contiguous Muslim-majority districts "
                "after the transfer of power, with joint essential services.",
                "It was C. Rajagopalachari's personal initiative and not an "
                "official Congress offer, and the Gandhi-Jinnah talks on that "
                "basis broke down in September 1944.",
                "The Simla Conference of 25 June - 14 July 1945, convened by "
                "Wavell, offered an entirely Indian Executive Council with "
                "parity between caste Hindus and Muslims.",
                "Simla collapsed on Jinnah's claim that the Muslim League "
                "alone could nominate every Muslim member, which the Congress "
                "refused while Maulana Abul Kalam Azad was its president.",
            ],
            "Do not say Simla failed because the Congress rejected an Indian "
            "executive; it accepted the framework and refused a monopoly of "
            "Muslim nominations.",
            "Use this three-stage failure to explain why the electoral "
            "verdict of 1945-46 mattered so much to the bargaining that "
            "followed.",
            """APR 1944 -> C.R. FORMULA -> plebiscite in contiguous Muslim-majority districts
             -> deferred until after transfer of power; not an official Congress offer
SEP 1944 -> GANDHI-JINNAH TALKS BREAK DOWN -> separation within the family vs sovereignty
25 JUN - 14 JUL 1945 -> SIMLA CONFERENCE (Wavell) -> all-Indian Executive Council
BREAKDOWN -> League claims a monopoly of Muslim nominations; Azad is Congress president.""",
            "The 1944-45 negotiations are the linked failures of the C.R. "
            "Formula, the Gandhi-Jinnah talks and the Simla Conference, all "
            "of which foundered on the question of Muslim representation.",
        ),
        authored_session(
            "Elections of the winter of 1945-46: mandate, not plebiscite",
            "The elections converted the Pakistan demand from a contested "
            "elite assertion into a certified representative mandate, and "
            "they did so under separate electorates and a restricted "
            "franchise that make the word plebiscite inaccurate.",
            [
                "The Congress won over 90 per cent of the general seats "
                "provincially and 80.9 per cent of the general-constituency "
                "votes across India.",
                "The Muslim League took 74.7 per cent of the votes cast in "
                "Muslim constituencies, sweeping the separate Muslim seats.",
                "The electorate was heavily restricted, at about 10 per cent "
                "of the population, and voting was by separate electorates.",
                "No boundary, constitution or population arrangement appeared "
                "on any ballot, so the verdict certified representation "
                "without settling territory.",
            ],
            "State the result as a representative mandate under separate "
            "electorates and a restricted franchise; it was not a plebiscite "
            "that made Partition automatically inevitable.",
            "Use the mandate-not-inevitability formulation whenever a "
            "question asks whether the 1945-46 elections made Partition "
            "certain.",
            """WINTER 1945-46 ELECTIONS -> two mandates in two separate electorates
|-- CONGRESS -> over 90% of general seats; 80.9% of general-constituency votes
|-- MUSLIM LEAGUE -> 74.7% of votes cast in Muslim constituencies
|-- FRANCHISE -> about 10% of the population; separate electorates
LIMIT -> no boundary, constitution or population question was on any ballot
RULE -> mandate, not plebiscite; representation was settled, territory was not.""",
            "The 1945-46 verdict is the pair of electoral mandates won by the "
            "Congress in general constituencies and by the Muslim League in "
            "Muslim constituencies under separate electorates.",
        ),
        authored_session(
            "18 February 1946: how the Royal Indian Navy uprising began",
            "The uprising had a precise date, a precise place and concrete "
            "service grievances, and an answer that begins with generalities "
            "about nationalism loses the evidence that makes it persuasive.",
            [
                "The uprising began on 18 February 1946 at HMIS Talwar in "
                "Bombay, a signals training establishment.",
                "Its immediate grievances were demobilisation anxiety, poor "
                "rations and service conditions, and racial insult by "
                "officers.",
                "The ratings' demands included better conditions, "
                "non-victimisation of strikers, and free trials for INA "
                "detainees.",
                "The naval demands therefore ran directly into the political "
                "atmosphere created by the Red Fort trials of the previous "
                "months.",
            ],
            "Anchor the uprising to 18 February 1946 and HMIS Talwar, Bombay; "
            "a vague 'February 1946 in Bombay' loses the examinable detail, "
            "and the exact date also matters because the Cabinet Mission's "
            "dispatch had already been decided on 22 January 1946.",
            "Use the demand for free INA trials to connect this session "
            "directly to the Red Fort sessions rather than treating the two "
            "episodes as unrelated.",
            """18 FEB 1946 -> HMIS TALWAR, BOMBAY -> ratings' uprising begins
GRIEVANCES -> demobilisation anxiety | rations and service conditions | racial insult
DEMANDS -> better conditions | non-victimisation of strikers | free trials for INA men
LINK -> naval grievance meets the political charge of the Red Fort trials
ALREADY DECIDED -> 22 JAN 1946 Cabinet resolves to send the Cabinet Mission
RULE -> fix the date and the establishment before any interpretation.""",
            "The Royal Indian Navy uprising is the ratings' revolt that began "
            "on 18 February 1946 at HMIS Talwar in Bombay over service "
            "grievances and INA-related demands.",
        ),
        authored_session(
            "Scale of the uprising: commonly cited estimates, carefully qualified",
            "The familiar scale figures are useful but must be presented "
            "honestly as commonly cited estimates, because the repository's "
            "own Basic owner warns against asserting ship numbers as settled "
            "fact.",
            [
                "Commonly cited estimates place the uprising's spread at "
                "roughly 20,000 ratings, 78 ships and 20 shore "
                "establishments.",
                "These figures are source-dependent and circulate mainly "
                "through study summaries rather than through a single "
                "authoritative count.",
                "The local Basic owner explicitly cautions against stating "
                "the number of ships involved as a fixed fact.",
                "The safe formulation is to give the figures with the phrase "
                "'commonly cited estimates' attached, or to describe the "
                "spread qualitatively instead.",
            ],
            "Never present roughly 20,000 ratings, 78 ships or 20 shore "
            "establishments as a verified count; always mark them as commonly "
            "cited estimates.",
            "Use the qualified figures to demonstrate scale in a Mains answer "
            "while showing the examiner that you know the evidential status "
            "of your numbers.",
            """COMMONLY CITED ESTIMATES (source-dependent, not a verified count)
|-- RATINGS -> roughly 20,000        |-- SHIPS -> roughly 78
|-- SHORE ESTABLISHMENTS -> roughly 20
OWNER CAUTION -> the local Basic owner warns against asserting ship numbers
RULE -> attach the qualifier or describe the spread qualitatively instead.""",
            "A commonly cited estimate is a figure that circulates widely "
            "across secondary summaries without a single authoritative count "
            "behind it, and which must therefore be labelled when used.",
        ),
        authored_session(
            "Why the uprising was not a nationwide revolution",
            "The uprising was serious and alarming to the government, but it "
            "was bounded in time, place and social base, and describing it as "
            "a revolution misstates both its character and its outcome.",
            [
                "It was short-lived and was surrendered within days rather "
                "than developing into a sustained campaign.",
                "It was concentrated in urban naval stations and the service "
                "population, with no rural base comparable to earlier mass "
                "movements.",
                "It was not directed by the Congress and it was not a "
                "Congress-led nationwide revolution.",
                "It did not by itself end British rule, and it did not cause "
                "or trigger the dispatch of the Cabinet Mission: the British "
                "Cabinet decided to send the mission on 22 January 1946 and "
                "Attlee's Commons announcement of 19 February 1946 had been "
                "slated a week earlier, so the decision preceded the strike "
                "that began on 18 February 1946.",
            ],
            "Do not describe the uprising as a nationalist-directed "
            "insurrection, as the immediate cause of British withdrawal, or "
            "as the reason the Cabinet Mission was sent; the dispatch "
            "decision of 22 January 1946 predates the uprising, so the "
            "dispatch-causation claim is explicitly untenable, and the "
            "separate suggestion attributed to P.S. Gupta in the Advanced "
            "owner concerns the wider INA agitation of 1945-46 and is "
            "recorded there as an attributed position rather than as "
            "settled fact.",
            "Use the what-it-revealed versus what-it-achieved split as the "
            "structural spine of any RIN significance answer, and use the "
            "22 January chronology as the sentence that shows an examiner "
            "you can date a decision rather than assume a causal link.",
            """WHAT IT REVEALED                | WHAT IT ACHIEVED
--------------------------------|-----------------------------------------------
loyalty of services in doubt    | no constitutional settlement
security doctrine of 1858 failing | surrender within days
urban solidarity with servicemen | no rural or nationwide extension
CHRONOLOGY TEST -> 22 JAN 1946 decision -> 18 FEB 1946 strike -> 19 FEB 1946 statement
RULE -> serious and revealing, but short-lived, urban and service-centred, and
        it did not cause or trigger the dispatch of the Cabinet Mission.""",
            "Service-centred means confined largely to serving naval "
            "personnel and their urban sympathisers, in contrast to the "
            "cross-class and rural reach of the earlier mass movements.",
        ),
        authored_session(
            "Divided political responses to the uprising",
            "Political responses to the uprising were differentiated rather "
            "than uniform, and the difference between party leaderships and "
            "organised civilian sympathy is itself examinable.",
            [
                "The Congress lauded the spirit of the people and condemned "
                "the repression, but it did not officially support the "
                "struggle because it judged the tactics and the timing wrong; "
                "Vallabhbhai Patel asked the ratings to surrender because he "
                "saw the overwhelming British mobilisation for repression in "
                "Bombay, writing to Nehru on 22 February 1946 that the naval "
                "and military force assembled there could exterminate them "
                "altogether.",
                "Muhammad Ali Jinnah's advice to surrender was addressed to "
                "Muslim ratings alone, who had gone to the League for "
                "guidance while the rest of the ratings went to the Congress "
                "and the Socialists, so the two appeals were neither "
                "identical nor addressed to the same audience.",
                "Organised sympathy strikes by workers and students in Bombay "
                "gave the uprising a civilian dimension it did not create "
                "for itself, and communist and other left organisations "
                "supported the ratings more directly than the major national "
                "parties did, although communists also joined Congressmen in "
                "urging crowds to disperse once repression was under way.",
                "The government responded with force, and the episode ended "
                "through negotiation and persuasion rather than through "
                "victory on either side.",
            ],
            "Do not claim that all national leaders supported the uprising, "
            "and do not flatten the two surrender appeals into one "
            "undifferentiated call to every rating: the Congress withheld "
            "official support on grounds of tactics and timing, Patel's "
            "appeal answered the scale of British repression in Bombay, and "
            "Jinnah's advice in the local book account was addressed to "
            "Muslim ratings alone. Differentiate party appeals for surrender, "
            "organised civilian and workers' sympathy, and left support.",
            "Use the differentiated response to explain why the uprising "
            "produced political alarm without producing a political "
            "settlement.",
            """RESPONSES TO THE UPRISING -> differentiated, not uniform
|-- CONGRESS -> lauds the spirit, condemns repression, withholds official support
|          -> reason given: tactics and timing judged wrong
|-- PATEL -> asks the ratings to surrender before overwhelming British mobilisation
|-- JINNAH -> surrender advice addressed to MUSLIM RATINGS ALONE, not to all ratings
|-- WORKERS and STUDENTS (Bombay) -> sympathy strikes; civilian dimension
|-- COMMUNIST and LEFT GROUPS -> direct support, yet also peace work once troops moved
|-- GOVERNMENT -> force, then negotiation and persuasion
RULE -> record the split and the different audiences; never claim uniform backing
        or one identical appeal to every rating.""",
            "The divided response is the contrast between senior party "
            "leaders who urged surrender, on different grounds and to "
            "different audiences, and the organised workers', student "
            "and left support that sustained the uprising's civilian side.",
        ),
        authored_session(
            "Cabinet Mission: the 16 May plan and the 16 June proposal",
            "The Cabinet Mission produced two separate documents a month "
            "apart, and merging them destroys the distinction between a "
            "long-term constitutional scheme and a short-term "
            "interim-government offer.",
            [
                "The Mission consisted of Pethick-Lawrence, Stafford Cripps "
                "and A.V. Alexander.",
                "Its long-term plan of 16 May 1946 rejected a sovereign "
                "Pakistan and proposed a three-tier scheme of Union, groups "
                "and provinces.",
                "The Union was to deal with foreign affairs, defence and "
                "communications, and to have the power to raise the finances "
                "required for those subjects.",
                "The separate proposal of 16 June 1946 concerned the "
                "composition of an interim government and is a different "
                "document with different contents.",
            ],
            "Keep 16 May 1946 and 16 June 1946 apart; the first is the "
            "long-term constitutional plan and the second is the "
            "interim-government proposal.",
            "Use the two-document structure whenever a question asks what the "
            "Cabinet Mission proposed, so that the constitutional and "
            "executive offers are not confused.",
            """CABINET MISSION 1946 -> Pethick-Lawrence | Stafford Cripps | A.V. Alexander
16 MAY 1946 -> LONG-TERM PLAN -> sovereign Pakistan rejected; three-tier union
    UNION SUBJECTS -> foreign affairs, defence, communications
                   -> plus power to raise the finances required for those subjects
16 JUN 1946 -> SEPARATE INTERIM-GOVERNMENT PROPOSAL -> a different document
RULE -> one mission, two dated documents; never merge them.""",
            "The Cabinet Mission's long-term plan is the constitutional "
            "scheme of 16 May 1946, distinct from the interim-government "
            "proposal it issued separately on 16 June 1946.",
        ),
        authored_session(
            "Groups, incompatible readings and the endgame to 9 December 1946",
            "The grouping device was a federal arrangement inside one union, "
            "and the scheme collapsed because two parties used the same text "
            "on incompatible readings while trust drained away between June "
            "and December 1946.",
            [
                "Section A comprised Madras, Bombay, the United Provinces, "
                "Bihar, the Central Provinces and Orissa; Section B comprised "
                "Punjab, the North-West Frontier Province, Sind and British "
                "Baluchistan; Section C comprised Bengal and Assam.",
                "The League accepted on 6 June 1946 reading grouping as "
                "compulsory, while Nehru's statement of 7 July 1946 asserted "
                "that the Congress was bound only to enter the Constituent "
                "Assembly.",
                "Jinnah withdrew the League's acceptance on 29 July 1946, "
                "Direct Action Day followed on 16 August 1946, and the "
                "Interim Government was formed on 2 September 1946 with "
                "Congress members alone.",
                "The League joined the Interim Government on 26 October 1946, "
                "His Majesty's Government conceded the compulsory-grouping "
                "reading on 6 December 1946, and the Constituent Assembly "
                "first met on 9 December 1946 with the League boycotting it.",
            ],
            "Record that the local Basic owner lists Section B as Punjab, the "
            "North-West Frontier Province and Sind, while the Mission's "
            "Section B also included British Baluchistan; and never reduce "
            "the collapse to one cause, since the ambiguity was resolved in "
            "the League's favour in December 1946 and the scheme still "
            "failed.",
            "Use this dated chain as the causal spine for any question on why "
            "the last united-India settlement broke down.",
            """SECTIONS -> A: Madras, Bombay, United Provinces, Bihar, Central Provinces, Orissa
          -> B: Punjab, North-West Frontier Province, Sind, British Baluchistan
          -> C: Bengal, Assam        (grouping = federal device inside one union)
6 JUN -> League accepts (grouping read as compulsory) | 7 JUL -> Nehru's AICC statement
29 JUL -> League withdraws | 16 AUG -> Direct Action Day | 2 SEP -> Interim Government
26 OCT -> League joins | 6 DEC -> HMG concedes grouping reading
9 DEC 1946 -> Constituent Assembly first meets; League boycotts
RULE -> incompatible readings plus incompatible goals; no single cause.""",
            "Grouping is the Cabinet Mission device placing provinces in "
            "Sections A, B and C to settle group constitutions inside one "
            "union, and it is not the same thing as Partition.",
        ),
    ],
}

SESSION_PLANS["modern-indian-history-27"] = [
    authored_session(
        "The Cabinet Mission attempted unity and did not partition India",
        "Partition is often misattributed to the Cabinet Mission, but the "
        "Mission rejected a sovereign Pakistan and offered a united "
        "three-tier scheme, so the causal story must begin with the collapse "
        "of that offer rather than with the offer itself.",
        [
            "The Mission's plan of 1946 proposed a Union, groups of "
            "provinces and provinces, with a deliberately weak centre.",
            "It rejected a sovereign Pakistan on administrative, economic "
            "and strategic grounds.",
            "Both parties accepted the scheme in some form in June and July "
            "1946, so a united settlement remained constitutionally "
            "available after the elections.",
            "Partition followed the collapse of that scheme through "
            "incompatible interpretations, withdrawal of acceptance and the "
            "breakdown of trust.",
        ],
        "Never write that the Mission itself carried out a partition of "
        "India; it attempted unity and did not partition India, and its "
        "grouping device was a federal arrangement.",
        "Open a causes-of-Partition answer by clearing this misattribution, "
        "because it sets up the contingency argument that follows.",
        """CABINET MISSION 1946 -> UNITY ATTEMPT, NOT A PARTITION INSTRUMENT
|-- REJECTED -> a sovereign Pakistan
|-- PROPOSED -> Union + groups of provinces + provinces (weak centre)
|-- ACCEPTED (in some form) -> by both parties in June and July 1946
COLLAPSE -> incompatible readings -> withdrawal -> loss of trust -> Partition
RULE -> the Mission is where unity was last available, not where it ended.""",
        "The Cabinet Mission scheme is the 1946 three-tier proposal of "
        "Union, groups and provinces that rejected a sovereign Pakistan and "
        "sought to preserve a single Indian union.",
    ),
    authored_session(
        "Direct Action Day, 16 August 1946: call, killings and consequences",
        "Direct Action Day must be handled as three separable things: a "
        "political call, the Calcutta killings that followed it, and the "
        "wider regional violence of the following months.",
        [
            "The Muslim League issued the Direct Action call for 16 August "
            "1946 after the constitutional deadlock and its own withdrawal "
            "of acceptance.",
            "In Calcutta the day was followed by mass killings remembered as "
            "the Great Calcutta Killings.",
            "The violence spread later to other regions, but each episode "
            "had its own local actors, triggers and sequence.",
            "Direct Action preceded the Congress-only Interim Government of "
            "September 1946, so it cannot be described as a reaction to that "
            "ministry.",
        ],
        "Keep the political call, the Calcutta killings and the later "
        "regional violence analytically distinct, and do not attribute the "
        "violence to any community as such.",
        "Use the three-part separation to write about 1946 violence without "
        "sliding into either apologetics or collective blame.",
        """16 AUG 1946 -> DIRECT ACTION DAY -> three separable things
|-- POLITICAL CALL -> Muslim League, after deadlock and its own withdrawal
|-- CALCUTTA -> mass killings remembered as the Great Calcutta Killings
|-- LATER REGIONAL VIOLENCE -> separate local actors, triggers and sequences
ORDER -> Direct Action precedes the Congress-only Interim Government (2 Sep 1946)
RULE -> separate call, killings and spread; assign agency to actors, not communities.""",
        "Direct Action Day is the Muslim League's political call for 16 "
        "August 1946, distinct from the Calcutta killings that followed it "
        "and from the later regional violence.",
    ),
    authored_session(
        "The spread of violence in 1946-47 without collective guilt",
        "Communal violence in 1946-47 was organised, reciprocal and "
        "regionally specific, and the discipline an answer must show is to "
        "assign agency to organisations and leaderships rather than to whole "
        "communities.",
        [
            "Violence moved through Noakhali, Bihar and the Punjab in "
            "reciprocal waves during 1946-47.",
            "Local organisations, armed bands, rumour and the collapse of "
            "policing drove each episode.",
            "Regional experience differed sharply: Punjab and Bengal "
            "experienced territorial division and mass violence, while other "
            "provinces experienced a political settlement and a minority "
            "question.",
            "Attributing violence to a religious community as such is both "
            "historically false and analytically useless, since it explains "
            "no particular episode.",
        ],
        "Assign responsibility to named organisations, leaderships and local "
        "actors, and never to whole communities; regional variation must be "
        "stated rather than averaged away.",
        "Use the regional-variation point to avoid a single national "
        "narrative of Partition violence in any 15 or 20-mark answer.",
        """1946-47 VIOLENCE -> reciprocal waves, regionally specific
|-- NOAKHALI -> BIHAR -> PUNJAB (each with its own actors and triggers)
|-- DRIVERS -> organisations, armed bands, rumour, collapse of policing
|-- REGIONAL SPLIT -> Punjab and Bengal: territorial division and mass violence
                   -> elsewhere: political settlement and a minority question
RULE -> agency belongs to organisations and leaderships, never to whole communities.""",
        "Reciprocal communal violence describes the retaliatory sequence of "
        "attacks across Noakhali, Bihar and Punjab in 1946-47, driven by "
        "organisations and local actors rather than by undifferentiated "
        "communities.",
    ),
    authored_session(
        "Attlee's statement of 20 February 1947 and the June 1948 deadline",
        "The February 1947 announcement changed the question from whether "
        "Britain would leave to how fast it could go, and it must be kept "
        "separate from Attlee's earlier statement about the minority veto.",
        [
            "On 20 February 1947 Attlee announced that Britain would "
            "transfer power to responsible Indian hands not later than June "
            "1948.",
            "The earlier statement of 15 March 1946 had said instead that a "
            "minority would not be allowed to place a veto on the progress "
            "of the majority.",
            "The 1946 statement is about the League's veto and preceded the "
            "Cabinet Mission; the 1947 statement sets the withdrawal "
            "deadline.",
            "A fixed outer limit turned every negotiating position into a "
            "race against a published date.",
        ],
        "Do not conflate the two Attlee statements; one addresses the "
        "minority veto in March 1946, the other sets the June 1948 deadline "
        "in February 1947.",
        "Use the deadline as the hinge between the constitutional deadlock "
        "of 1946 and the accelerated partition mechanics of 1947.",
        """TWO ATTLEE STATEMENTS -> do not conflate
|-- 15 MAR 1946 -> "a minority will not be allowed to place a veto" -> pre-Mission
`-- 20 FEB 1947 -> transfer of power to responsible Indian hands, not later than June 1948
EFFECT -> a published outer limit converts negotiation into a race against a date
RULE -> one is about the veto, the other is about the deadline.""",
        "Attlee's statement of 20 February 1947 is the announcement of a "
        "fixed outer limit of June 1948 for the transfer of power to "
        "responsible Indian hands.",
    ),
    authored_session(
        "Mountbatten as last Viceroy and the accelerated timetable",
        "Mountbatten's arrival in March 1947 compressed the timetable "
        "drastically, and that compression explains a great deal about how "
        "Partition was executed without explaining why Partition was chosen.",
        [
            "Lord Mountbatten arrived in March 1947 as the last Viceroy of "
            "India.",
            "He converted the June 1948 outer limit into a far shorter "
            "timetable culminating in August 1947.",
            "The compression left administrative, military and boundary "
            "arrangements incomplete when power was transferred.",
            "Acceleration is therefore an analytical fact about execution "
            "and disorder, not a substitute for a causal account of the "
            "decision to partition.",
        ],
        "Do not let the haste argument become the whole explanation; haste "
        "worsened the violence and disorder, but the decision to partition "
        "had other and older causes.",
        "Use the acceleration point in the consequences section of an "
        "answer, not in the causes section.",
        """MAR 1947 -> MOUNTBATTEN ARRIVES AS LAST VICEROY
DEADLINE -> June 1948 outer limit compressed to August 1947
CONSEQUENCE -> administrative, military and boundary arrangements left incomplete
ANALYTICAL PLACE -> explains execution and disorder, not the choice to partition
RULE -> haste belongs in consequences, not in causes.""",
        "The accelerated timetable is Mountbatten's compression of the "
        "published June 1948 deadline into a transfer completed in August "
        "1947.",
    ),
    authored_session(
        "The 3 June Plan as a political plan, not an Act",
        "The 3 June Plan is a political decision document: it set the terms "
        "on which Partition and transfer would proceed, and it is not the "
        "statute that transferred power.",
        [
            "The Mountbatten Plan was announced on 3 June 1947 and accepted "
            "Partition in principle.",
            "It provided for the division of Punjab and Bengal, referendums "
            "in the North-West Frontier Province and Sylhet, and boundary "
            "commissions.",
            "It was not an Act of Parliament and did not by itself transfer "
            "power or create any dominion.",
            "The legal transfer required a separate enactment at Westminster "
            "which followed in July 1947.",
        ],
        "Never describe the 3 June Plan as legislation or say that Parliament "
        "passed the Mountbatten Plan; the plan is political and the Act is "
        "legal.",
        "Use the plan-versus-Act distinction as the first line of any "
        "instruments question, before you describe either document.",
        """3 JUNE 1947 -> MOUNTBATTEN PLAN -> a POLITICAL plan
|-- ACCEPTS -> Partition in principle
|-- PROVIDES FOR -> division of Punjab and Bengal
|                -> referendums in the North-West Frontier Province and Sylhet
|                -> boundary commissions
LIMIT -> not an Act of Parliament; transfers no power by itself
RULE -> the political decision precedes the legal enactment of July 1947.""",
        "The 3 June Plan is the political plan announced by Mountbatten in "
        "1947 that accepted Partition and set out the procedures by which it "
        "would be carried out.",
    ),
    authored_session(
        "Three partition mechanisms: assembly votes, referendums, commissions",
        "Partition was executed through three procedurally different "
        "mechanisms, and conflating them produces both factual error and a "
        "false picture of how consent was measured.",
        [
            "Punjab and Bengal were divided by separate votes of the "
            "notional Hindu-majority and Muslim-majority halves of each "
            "provincial legislative assembly.",
            "The North-West Frontier Province and the Sylhet district of "
            "Assam decided by referendum, and both results took them into "
            "Pakistan.",
            "The Congress-aligned boycott of the North-West Frontier "
            "Province poll is standard knowledge rather than a claim taken "
            "from the local owner files, and should be flagged as such.",
            "Boundary commissions then drew the actual lines, a technical "
            "task distinct from both the legislative and the referendum "
            "routes.",
        ],
        "Do not describe Punjab and Bengal as partitioned by referendum, and "
        "do not describe the North-West Frontier Province or Sylhet as "
        "divided by assembly vote.",
        "Use the three-mechanism map for any question that asks how, rather "
        "than why, Partition was carried out.",
        """HOW PARTITION WAS CARRIED OUT -> three different procedures
|-- ASSEMBLY VOTES -> Punjab and Bengal, by the two notional halves of each assembly
|-- REFERENDUMS -> North-West Frontier Province and Sylhet district of Assam
|                -> both results took them into Pakistan
`-- BOUNDARY COMMISSIONS -> technical line-drawing, separate from both routes
RULE -> match the province to its mechanism; never swap them.""",
        "The three partition mechanisms are the provincial assembly votes "
        "for Punjab and Bengal, the referendums in the North-West Frontier "
        "Province and Sylhet, and the boundary commissions.",
    ),
    authored_session(
        "The Indian Independence Act: Royal Assent and commencement",
        "The Act is the legal instrument of transfer, and its two dates "
        "must be stated separately: it received Royal Assent on 18 July 1947 "
        "and it created the dominions from 15 August 1947.",
        [
            "The Indian Independence Act received Royal Assent on 18 July "
            "1947 at Westminster.",
            "It legally created the two independent dominions of India and "
            "Pakistan from 15 August 1947.",
            "It provided for the lapse of British paramountcy over the "
            "princely states.",
            "Assent and commencement are different legal events, and an "
            "answer that gives only 'July 1947' loses the second half of the "
            "distinction.",
        ],
        "Distinguish the Royal Assent of 18 July 1947 from the commencement "
        "of the two dominions on 15 August 1947; the Act followed and did "
        "not precede the political plan.",
        "Use both dates in any instruments answer, because examiners test "
        "assent and commencement separately.",
        """INDIAN INDEPENDENCE ACT -> the LEGAL enactment
|-- ROYAL ASSENT -> 18 July 1947 (Westminster)
|-- COMMENCEMENT -> two dominions, India and Pakistan, from 15 August 1947
|-- ALSO PROVIDES -> lapse of British paramountcy over the princely states
SEQUENCE -> 3 June political plan -> 18 July assent -> 15 August commencement
RULE -> assent and commencement are separate legal events.""",
        "The Indian Independence Act is the Westminster statute that "
        "received Royal Assent on 18 July 1947 and created the dominions of "
        "India and Pakistan from 15 August 1947.",
    ),
    authored_session(
        "14 August and 15 August: what the Act actually provides",
        "A common error conflates Pakistan's later national-day observance "
        "on 14 August with the legal commencement of the Act, and the two "
        "must be kept apart because only one of them is a statutory fact.",
        [
            "The Act created both dominions from 15 August 1947, and that is "
            "the date the statute names.",
            "Pakistan's observance of 14 August as its national day is a "
            "later commemorative practice, not the Act's commencement date.",
            "Mountbatten attended the Karachi ceremony on 14 August and the "
            "Delhi transfer on 15 August, which is an administrative fact "
            "about ceremonies rather than about the statute.",
            "An answer that says the Act came into force on different dates "
            "for the two dominions has misread the enactment.",
        ],
        "Do not present 14 August as the Act's commencement for Pakistan; "
        "the statute created both dominions from 15 August 1947 and the "
        "14 August observance is a separate commemorative fact.",
        "Use this precision in Prelims-style elimination, where the "
        "commencement date is a favourite close-option trap.",
        """WHAT THE STATUTE SAYS      | WHAT COMMEMORATION SAYS
---------------------------|-------------------------------------------------
both dominions from        | Pakistan observes 14 August as its national day
15 August 1947             | ceremonies at Karachi (14th) and Delhi (15th)
RULE -> statutory commencement is one date; commemorative observance is another.""",
        "Commencement is the date from which a statute takes legal effect, "
        "which for the Indian Independence Act is 15 August 1947 for both "
        "dominions.",
    ),
    authored_session(
        "The lapse of British paramountcy",
        "Paramountcy lapsed rather than transferring, and that single verb "
        "created the entire princely-states problem that the next topic "
        "resolves.",
        [
            "British paramountcy over the princely states lapsed under the "
            "Act rather than passing to either successor dominion.",
            "Paramountcy therefore did not pass wholesale to India, and no "
            "automatic inheritance of suzerainty occurred.",
            "Each state's relationship with a dominion had to be created "
            "afresh through accession or agreement.",
            "The lapse is a legal fact about the Act, and the accession "
            "process that followed belongs to the integration topic.",
        ],
        "Never write that suzerainty over the princely states was inherited "
        "automatically by either dominion; paramountcy lapsed, which is "
        "precisely why accession had to be negotiated state by state.",
        "Use the lapse as the bridge sentence connecting this topic to the "
        "integration of the princely states.",
        """PARAMOUNTCY -> LAPSED (it did not transfer)
|-- NOT INHERITED -> neither dominion succeeded to suzerainty automatically
|-- CONSEQUENCE -> each state's relationship had to be created afresh
|-- ROUTE -> accession or agreement, negotiated state by state
RULE -> "lapsed" is the operative verb; "transferred" is the error.""",
        "Paramountcy was the Crown's suzerain relationship with the princely "
        "states, and its lapse under the Act meant it ended rather than "
        "passing to either dominion.",
    ),
    authored_session(
        "Two Radcliffe commissions and the awards of 17 August 1947",
        "There were two boundary commissions, not one, and their awards were "
        "published on 17 August 1947, after the transfer of power, which "
        "produced administrative uncertainty without being the sole cause of "
        "the violence.",
        [
            "Two separate commissions, one for Punjab and one for Bengal, "
            "were chaired by Cyril Radcliffe, a British lawyer with no prior "
            "Indian experience.",
            "Each commission had an equal number of Congress-nominated and "
            "League-nominated judges, so when they divided the decisions "
            "fell to the chairman.",
            "The awards were published on 17 August 1947, after the transfer "
            "of power on 15 August.",
            "Many people in border districts therefore did not know which "
            "state they were in at independence, although large-scale "
            "violence had begun long before any line was drawn.",
        ],
        "Do not describe Radcliffe as an Indian leader, do not speak of a "
        "single commission, and do not claim that the award alone caused the "
        "violence.",
        "Use the publication date to explain administrative uncertainty "
        "while keeping the causes of violence multi-factorial.",
        """BOUNDARY MECHANISM -> two commissions, one chairman
|-- PUNJAB COMMISSION | BENGAL COMMISSION -> chaired by Cyril Radcliffe
|-- COMPOSITION -> equal Congress-nominated and League-nominated judges
|-- DEADLOCK -> members divide -> decisions fall to the chairman
15 AUG 1947 -> transfer of power | 17 AUG 1947 -> awards published
CONSEQUENCE -> border districts uncertain; violence already under way before the line.""",
        "The Radcliffe awards are the boundary decisions of the two 1947 "
        "commissions for Punjab and Bengal, published on 17 August 1947 "
        "after the transfer of power.",
    ),
    authored_session(
        "Congress acceptance of Partition as reluctant pragmatism",
        "Congress acceptance was a constrained choice made late, under "
        "deadlock and violence, and it must never be presented either as "
        "enthusiasm or as a long-standing policy.",
        [
            "Acceptance followed the constitutional deadlock of 1946 and the "
            "failure of the last united-India scheme.",
            "Escalating communal violence made the prospect of prolonged "
            "paralysis appear more dangerous than division.",
            "The leadership judged that a weak centre with compulsory "
            "grouping would produce an ungovernable state, and preferred a "
            "workable strong centre.",
            "The willingness to contemplate separation had appeared as early "
            "as the C.R. Formula of 1944, so acceptance was not sudden, but "
            "it was never a Congress programme.",
        ],
        "Do not present Congress acceptance as enthusiasm or as long-standing "
        "policy; describe it as reluctant and pragmatic, tied to deadlock, "
        "violence and governability.",
        "Use the reluctant-pragmatism formulation in any responsibility "
        "question, because it avoids both apologetics and accusation.",
        """CONGRESS ACCEPTANCE -> reluctant and pragmatic, not programmatic
|-- TRIGGER -> constitutional deadlock of 1946; last unity scheme collapses
|-- PRESSURE -> escalating communal violence; fear of prolonged paralysis
|-- CALCULATION -> weak centre + compulsory grouping = ungovernable state
|-- PRECEDENT -> C.R. Formula 1944 shows the idea was not new in 1947
RULE -> a constrained late choice, never a long-standing Congress policy.""",
        "Reluctant pragmatism describes Congress's 1947 acceptance of "
        "Partition as a constrained choice forced by deadlock, violence and "
        "a judgement about governability.",
    ),
    authored_session(
        "Was Partition inevitable? Cumulative structure and contingency",
        "Inevitability is an interpretive claim rather than a demonstrated "
        "fact, and the strongest answer combines four decades of cumulative "
        "structure with a short chain of contingent, datable decisions.",
        [
            "Cumulative structure means the organisation of political "
            "representation around religious community from the separate "
            "electorates of 1909 onwards.",
            "Contingency means the specific decisions of 1946 and 1947 that "
            "closed each remaining option in turn.",
            "Partition was not made inevitable by the founding of the Muslim "
            "League in 1906, by the Lahore Resolution of 1940 or by the "
            "elections of 1945-46.",
            "Both parties accepted the Cabinet Mission scheme in some form "
            "in June and July 1946, after the electoral verdict, so unity "
            "survived the verdict by more than a year.",
        ],
        "Do not assert that Partition was inevitable from any single date; "
        "state which options remained open, and identify precisely when each "
        "closed.",
        "Use structure-plus-contingency as the standard architecture for "
        "every 'was Partition inevitable' question.",
        """WAS PARTITION INEVITABLE? -> structure + contingency, not a single date
|-- STRUCTURE -> representation organised by community from 1909 onwards
|-- CONTINGENCY -> dated decisions of 1946-47 that closed each option
|-- NOT INEVITABLE FROM -> 1906 (League founded) | 1940 (Lahore) | 1945-46 (elections)
|-- EVIDENCE -> both parties accepted the Mission scheme in June-July 1946
RULE -> name the option, name the date it closed, then judge.""",
        "Cumulative structure plus contingent decision is the explanatory "
        "frame in which long-run communal representation made Partition "
        "possible while specific 1946-47 choices made it actual.",
    ),
    authored_session(
        "Responsibility without a single villain",
        "A responsibility question is best answered by refusing single-actor "
        "blame and specifying each actor's contribution together with the "
        "constraint under which it acted.",
        [
            "Colonial constitutional engineering created and repeatedly "
            "extended communal representation, and the hasty withdrawal of "
            "1947 worsened the disorder.",
            "The Muslim League converted minority safeguards into a claim to "
            "separate nationhood after 1940 and used its 1946 mandate to "
            "make that claim unrefusable.",
            "Congress accepted separate electorates in 1916, underestimated "
            "the League after 1937, and accepted Partition in 1947 to secure "
            "a workable centre.",
            "Communal organisations on every side hardened boundaries and "
            "legitimised violence, while mass fear and distinct regional "
            "dynamics did the rest.",
        ],
        "Refuse single-villain explanations, and assign agency to "
        "organisations and leaderships rather than to religious communities.",
        "Use this actor-by-actor grid whenever a question asks who was "
        "responsible for Partition.",
        """RESPONSIBILITY -> contribution + constraint, actor by actor
|-- BRITISH POLICY -> communal representation from 1909; hasty 1947 withdrawal
|-- MUSLIM LEAGUE -> safeguards become nationhood after 1940; 1946 mandate
|-- CONGRESS -> 1916 acceptance of separate electorates; 1937 miscalculation; 1947 choice
|-- COMMUNAL ORGANISATIONS -> hardened boundaries, legitimised violence
|-- MASS FEAR + REGIONAL DYNAMICS -> Punjab, Bengal, United Provinces differ
RULE -> no single villain; agency belongs to organisations, not communities.""",
        "The no-single-villain rule is the requirement that responsibility "
        "for Partition be distributed across colonial policy, party "
        "strategies, communal organisations and mass dynamics.",
    ),
    authored_session(
        "Two registers: legal transfer, political triumph, humanitarian catastrophe",
        "The final judgement of this topic is that three descriptions of the "
        "same weeks are simultaneously true, and an answer that records only "
        "one of them has answered only part of the question.",
        [
            "The legal register is an unprecedented constitutional transfer "
            "in the colonial world, completed by statute.",
            "The political register is the fulfilment of a mass national "
            "movement, marked by Nehru's 'Tryst with Destiny' speech in the "
            "Constituent Assembly.",
            "The humanitarian register is displacement commonly estimated at "
            "around 10 to 15 million, with contested death tolls that must "
            "not be stated with false precision.",
            "Gandhi was in Calcutta and Bengal working for communal peace, "
            "not celebrating in Delhi, and the aftermath became the new "
            "state's first administrative test, remembered officially "
            "through the Ministry of Culture's Partition Horrors Remembrance "
            "Day observance on 13 and 14 August 2026.",
        ],
        "State displacement only as the broad 10 to 15 million estimate, "
        "never quantify deaths, and never place Gandhi in Delhi celebrating "
        "independence.",
        "Close any 20-mark answer with the three simultaneous registers "
        "rather than with a one-sided verdict.",
        """THREE SIMULTANEOUS REGISTERS OF INDEPENDENCE
|-- LEGAL -> unprecedented constitutional transfer, completed by statute
|-- POLITICAL -> fulfilment of a mass movement; Nehru's "Tryst with Destiny"
|-- HUMANITARIAN -> displacement around 10 to 15 million (broad estimate)
|                -> death tolls contested; never state a precise figure
LOCATION -> Gandhi in Calcutta and Bengal for communal peace, not celebrating in Delhi
REMEMBRANCE -> Partition Horrors Remembrance Day, 13 and 14 August 2026
RULE -> all three registers are true at once; record all three.""",
        "The three registers are the simultaneous legal, political and "
        "humanitarian descriptions of independence and Partition, none of "
        "which cancels the others.",
    ),
]

PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-26": [
        (
            "Two Indian National Armies, 1942 and 1943",
            "timeline",
            """1942 -> FIRST INA -> Mohan Singh + Indian POWs (Malaya, Singapore) + Japanese support
EARLY 1943 -> first INA collapses; Mohan Singh removed and arrested over subsidiary status
MAY 1943 -> Subhas Chandra Bose reaches Southeast Asia and reorganises the force
OCT 1943 -> SECOND INA under Azad Hind -> larger, politically directed, claimant government
RULE -> two armies, two dates, two leaderships; never one continuous force.""",
            ["Two Indian National Armies: 1942 under Mohan Singh, 1943 under Bose"],
        ),
        (
            "Rash Behari Bose: political cover, not field command",
            "institution-map",
            """INDIAN INDEPENDENCE LEAGUE  (political roof over the prisoner-of-war army)
|-- RASH BEHARI BOSE -> convenes Tokyo and Bangkok conferences; negotiates with Japan
|-- HANDOVER 1943 -> League and INA leadership pass to Subhas Chandra Bose
`-- FIELD COMMAND -> Mohan Singh (1942), then Bose's INA officers (1943-45)
RULE -> political sponsorship and field command are two different offices.""",
            ["Rash Behari Bose: political cover, not field command"],
        ),
        (
            "Azad Hind: government, army and symbols",
            "institution-map",
            """PROVISIONAL GOVERNMENT OF AZAD HIND (Singapore, October 1943)
|-- SUPREME COMMANDER -> Subhas Chandra Bose | SLOGAN -> "Dilli Chalo"
|-- ARMY -> reorganised INA | WOMEN'S UNIT -> Rani of Jhansi Regiment (Lakshmi Sahgal)
|-- TERRITORY CLAIMED -> Andaman and Nicobar renamed Shaheed and Swaraj
RULE -> a claimant government's symbols, not a record of battlefield success.""",
            ["Azad Hind: provisional government, army and symbols"],
        ),
        (
            "Imphal-Kohima and the military verdict",
            "causal-flow",
            """8 MAR 1944 -> Imphal campaign launched with Japanese forces -> objective: Delhi
IMPHAL + KOHIMA -> advance broken; retreat through Burma destroys the formation
CAUSES -> supply failure + monsoon + Allied air power (military, not political)
AUG 1945 -> Bose officially reported dead in an air crash; nothing beyond the report
RULE -> the military verdict is defeat; the political verdict comes later.""",
            ["Imphal-Kohima: state the military verdict plainly"],
        ),
        (
            "Red Fort trial: three defendants, one message",
            "comparison",
            """RED FORT TRIAL (1945-46) -> three officers tried together
|-- SHAH NAWAZ KHAN (Muslim) | PREM SAHGAL / SEHGAL (Hindu) | G.S. DHILLON (Sikh)
|-- DEFENCE -> Bhulabhai Desai, Tej Bahadur Sapru, K.N. Katju, Nehru, Asaf Ali
|-- CONGRESS -> INA Relief and Enquiry Committee; INA becomes an election plank
EFFECT -> prosecution reads as punishment of patriotism across three communities.""",
            ["The first Red Fort trial and its cross-communal symbolism"],
        ),
        (
            "What actually happened to the sentences",
            "causal-flow",
            """CONVICTION -> waging war against the King -> transportation for life
REMISSION -> Commander-in-Chief remits the sentences -> officers released
PRESSURE -> army opinion favours leniency; NWFP Governor urges abandonment
RESULT -> wider prosecutions abandoned; the sentences were not carried out
RULE -> a government retreat, not an execution.""",
            ["What actually happened to the Red Fort sentences"],
        ),
        (
            "Weighing INA and RIN inside a multi-causal endgame",
            "balance-sheet",
            """WHY THE BRITISH LEFT -> ranked, not listed
|-- COLLABORATION COLLAPSE -> services, police, armed forces no longer reliable
|-- WARTIME EXHAUSTION -> economic depletion, demobilisation, Labour government
|-- MASS NATIONALISM -> 1920-22, 1930-34, 1942 -> consent already impossible
|-- INTERNATIONAL + DEADLOCK -> decolonisation climate; 1946 constitutional impasse
CHRONOLOGY GUARD -> Mission dispatch decided 22 Jan 1946, before the 18 Feb strike
RULE -> INA and RIN sharpen the timing; they do not replace the other causes.""",
            ["Weighing INA and RIN inside a multi-causal endgame"],
        ),
        (
            "Failed negotiations of 1944-45",
            "timeline",
            """APR 1944 -> C.R. FORMULA -> plebiscite in contiguous Muslim-majority districts
             -> deferred until after transfer of power; not an official Congress offer
SEP 1944 -> GANDHI-JINNAH TALKS BREAK DOWN -> separation within the family vs sovereignty
25 JUN - 14 JUL 1945 -> SIMLA CONFERENCE (Wavell) -> all-Indian Executive Council
BREAKDOWN -> League claims a monopoly of Muslim nominations; Azad is Congress president.""",
            [
                "Failed negotiations of 1944-45: C.R. Formula, Gandhi-Jinnah, Simla"
            ],
        ),
        (
            "Elections of winter 1945-46: mandate, not plebiscite",
            "data-table",
            """WINTER 1945-46 ELECTIONS -> two mandates in two separate electorates
|-- CONGRESS -> over 90% of general seats; 80.9% of general-constituency votes
|-- MUSLIM LEAGUE -> 74.7% of votes cast in Muslim constituencies
|-- FRANCHISE -> about 10% of the population; separate electorates
LIMIT -> no boundary, constitution or population question was on any ballot
RULE -> mandate, not plebiscite; representation was settled, territory was not.""",
            ["Elections of the winter of 1945-46: mandate, not plebiscite"],
        ),
        (
            "RIN uprising: 18 February 1946 and its limits",
            "timeline",
            """18 FEB 1946 -> HMIS TALWAR, BOMBAY -> ratings' uprising begins
GRIEVANCES -> demobilisation anxiety, rations and service conditions, racial insult
DEMANDS -> better conditions, non-victimisation of strikers, free trials for INA men
SCALE -> commonly cited estimates: roughly 20,000 ratings, 78 ships, 20 shore stations
LIMITS -> short-lived, urban, service-centred; surrendered within days
RESPONSES -> Congress withholds official support (tactics and timing judged wrong)
          -> Patel urges surrender before overwhelming British mobilisation in Bombay
          -> Jinnah's surrender advice addressed to Muslim ratings alone
          -> workers, students and the left supply the civilian sympathy
DISPATCH -> 22 JAN 1946 Cabinet decides to send the Mission (before the uprising)
         -> Attlee's 19 FEB 1946 Commons announcement had been slated a week earlier
RULE -> the uprising did not cause or trigger the dispatch of the Cabinet Mission.""",
            [
                "18 February 1946: how the Royal Indian Navy uprising began",
                "Scale of the uprising: commonly cited estimates, carefully qualified",
                "Why the uprising was not a nationwide revolution",
                "Divided political responses to the uprising",
            ],
        ),
        (
            "Cabinet Mission: 16 May plan and 16 June proposal",
            "comparison",
            """CABINET MISSION 1946 -> Pethick-Lawrence | Stafford Cripps | A.V. Alexander
16 MAY 1946 -> LONG-TERM PLAN -> sovereign Pakistan rejected; three-tier union
    UNION SUBJECTS -> foreign affairs, defence, communications
                   -> plus power to raise the finances required for those subjects
16 JUN 1946 -> SEPARATE INTERIM-GOVERNMENT PROPOSAL -> a different document
RULE -> one mission, two dated documents; never merge them.""",
            ["Cabinet Mission: the 16 May plan and the 16 June proposal"],
        ),
        (
            "Sections A, B and C and the endgame to 9 December 1946",
            "institution-map",
            """SECTIONS -> A: Madras, Bombay, United Provinces, Bihar, Central Provinces, Orissa
          -> B: Punjab, North-West Frontier Province, Sind, British Baluchistan
          -> C: Bengal, Assam        (grouping = federal device inside one union)
6 JUN -> League accepts (grouping read as compulsory) | 7 JUL -> Nehru's AICC statement
29 JUL -> League withdraws | 16 AUG -> Direct Action Day | 2 SEP -> Interim Government
26 OCT -> League joins | 6 DEC -> HMG concedes the compulsory-grouping reading
9 DEC 1946 -> Constituent Assembly first meets; League boycotts
RULE -> incompatible readings plus incompatible goals; no single cause of failure.""",
            [
                "Groups, incompatible readings and the endgame to 9 December 1946"
            ],
        ),
    ],
    "modern-indian-history-27": [
        (
            "Cabinet Mission attempted unity",
            "causal-flow",
            """CABINET MISSION 1946 -> UNITY ATTEMPT, NOT A PARTITION INSTRUMENT
|-- REJECTED -> a sovereign Pakistan
|-- PROPOSED -> Union + groups of provinces + provinces (weak centre)
|-- ACCEPTED (in some form) -> by both parties in June and July 1946
COLLAPSE -> incompatible readings -> withdrawal -> loss of trust -> Partition
RULE -> the Mission is where unity was last available, not where it ended.""",
            ["The Cabinet Mission attempted unity and did not partition India"],
        ),
        (
            "Direct Action Day: call, killings, consequences",
            "timeline",
            """16 AUG 1946 -> DIRECT ACTION DAY -> three separable things
|-- POLITICAL CALL -> Muslim League, after deadlock and its own withdrawal
|-- CALCUTTA -> mass killings remembered as the Great Calcutta Killings
|-- LATER REGIONAL VIOLENCE -> separate local actors, triggers and sequences
ORDER -> Direct Action precedes the Congress-only Interim Government (2 Sep 1946)
RULE -> separate call, killings and spread; assign agency to actors, not communities.""",
            [
                "Direct Action Day, 16 August 1946: call, killings and consequences"
            ],
        ),
        (
            "Violence of 1946-47 without collective guilt",
            "balance-sheet",
            """1946-47 VIOLENCE -> reciprocal waves, regionally specific
|-- NOAKHALI -> BIHAR -> PUNJAB (each with its own actors and triggers)
|-- DRIVERS -> organisations, armed bands, rumour, collapse of policing
|-- REGIONAL SPLIT -> Punjab and Bengal: territorial division and mass violence
                   -> elsewhere: political settlement and a minority question
RULE -> agency belongs to organisations and leaderships, never to whole communities.""",
            ["The spread of violence in 1946-47 without collective guilt"],
        ),
        (
            "Two Attlee statements, one deadline",
            "comparison",
            """TWO ATTLEE STATEMENTS -> do not conflate
|-- 15 MAR 1946 -> "a minority will not be allowed to place a veto" -> pre-Mission
`-- 20 FEB 1947 -> transfer to responsible Indian hands, not later than June 1948
EFFECT -> a published outer limit converts negotiation into a race against a date
RULE -> one is about the veto, the other is about the deadline.""",
            [
                "Attlee's statement of 20 February 1947 and the June 1948 deadline"
            ],
        ),
        (
            "Mountbatten and the accelerated timetable",
            "timeline",
            """MAR 1947 -> MOUNTBATTEN ARRIVES AS LAST VICEROY
DEADLINE -> June 1948 outer limit compressed to August 1947
CONSEQUENCE -> administrative, military and boundary arrangements left incomplete
ANALYTICAL PLACE -> explains execution and disorder, not the choice to partition
RULE -> haste belongs in consequences, not in causes.""",
            ["Mountbatten as last Viceroy and the accelerated timetable"],
        ),
        (
            "3 June Plan: a political plan, not an Act",
            "institution-map",
            """3 JUNE 1947 -> MOUNTBATTEN PLAN -> a POLITICAL plan
|-- ACCEPTS -> Partition in principle
|-- PROVIDES FOR -> division of Punjab and Bengal
|                -> referendums in the North-West Frontier Province and Sylhet
|                -> boundary commissions
LIMIT -> not an Act of Parliament; transfers no power by itself
RULE -> the political decision precedes the legal enactment of July 1947.""",
            ["The 3 June Plan as a political plan, not an Act"],
        ),
        (
            "Three partition mechanisms",
            "comparison",
            """HOW PARTITION WAS CARRIED OUT -> three different procedures
|-- ASSEMBLY VOTES -> Punjab and Bengal, by the two notional halves of each assembly
|-- REFERENDUMS -> North-West Frontier Province and Sylhet district of Assam
|                -> both results took them into Pakistan
`-- BOUNDARY COMMISSIONS -> technical line-drawing, separate from both routes
RULE -> match the province to its mechanism; never swap them.""",
            [
                "Three partition mechanisms: assembly votes, referendums, commissions"
            ],
        ),
        (
            "Indian Independence Act: assent and commencement",
            "timeline",
            """INDIAN INDEPENDENCE ACT -> the LEGAL enactment
|-- ROYAL ASSENT -> 18 July 1947 (Westminster)
|-- COMMENCEMENT -> two dominions, India and Pakistan, from 15 August 1947
|-- ALSO PROVIDES -> lapse of British paramountcy over the princely states
SEQUENCE -> 3 June political plan -> 18 July assent -> 15 August commencement
RULE -> assent and commencement are separate legal events.""",
            ["The Indian Independence Act: Royal Assent and commencement"],
        ),
        (
            "Statutory commencement versus commemorative observance",
            "comparison",
            """WHAT THE STATUTE SAYS      | WHAT COMMEMORATION SAYS
---------------------------|-------------------------------------------------
both dominions created     | Pakistan observes 14 August as its national day
from 15 August 1947        | ceremonies at Karachi (14th) and Delhi (15th)
RULE -> statutory commencement is one date; commemorative observance is another.""",
            ["14 August and 15 August: what the Act actually provides"],
        ),
        (
            "The lapse of paramountcy",
            "causal-flow",
            """PARAMOUNTCY -> LAPSED (it did not transfer)
|-- NOT INHERITED -> neither dominion succeeded to suzerainty automatically
|-- CONSEQUENCE -> each state's relationship had to be created afresh
|-- ROUTE -> accession or agreement, negotiated state by state
RULE -> "lapsed" is the operative verb; "transferred" is the error.""",
            ["The lapse of British paramountcy"],
        ),
        (
            "Radcliffe: two commissions, awards of 17 August",
            "timeline",
            """BOUNDARY MECHANISM -> two commissions, one chairman
|-- PUNJAB COMMISSION | BENGAL COMMISSION -> chaired by Cyril Radcliffe
|-- COMPOSITION -> equal Congress-nominated and League-nominated judges
|-- DEADLOCK -> members divide -> decisions fall to the chairman
15 AUG 1947 -> transfer of power | 17 AUG 1947 -> awards published
CONSEQUENCE -> border districts uncertain; violence already under way before the line.""",
            ["Two Radcliffe commissions and the awards of 17 August 1947"],
        ),
        (
            "Responsibility, contingency and the three registers",
            "balance-sheet",
            """CONGRESS ACCEPTANCE -> reluctant and pragmatic; deadlock, violence, governability
INEVITABILITY -> structure (1909 onwards) + contingency (dated 1946-47 decisions)
RESPONSIBILITY -> British policy | Muslim League | Congress | communal organisations
               -> mass fear and regional dynamics; no single villain
THREE REGISTERS -> legal transfer | political triumph | humanitarian catastrophe
HUMAN COST -> displacement around 10 to 15 million (broad estimate); deaths contested
GANDHI -> in Calcutta and Bengal for communal peace, not celebrating in Delhi
RULE -> record all three registers; a one-sided verdict answers only part.""",
            [
                "Congress acceptance of Partition as reluctant pragmatism",
                "Was Partition inevitable? Cumulative structure and contingency",
                "Responsibility without a single villain",
                "Two registers: legal transfer, political triumph, humanitarian catastrophe",
            ],
        ),
    ],
}


TOPIC_CHRONOLOGY = {
    "modern-indian-history-26": [
        "1942",
        "May 1943",
        "October 1943",
        "8 March 1944",
        "April 1944",
        "September 1944",
        "25 June - 14 July 1945",
        "August 1945",
        "winter of 1945-46",
        "22 January 1946",
        "18 February 1946",
        "19 February 1946",
        "16 May 1946",
        "16 June 1946",
        "29 July 1946",
        "16 August 1946",
        "2 September 1946",
        "26 October 1946",
        "9 December 1946",
    ],
    "modern-indian-history-27": [
        "1946",
        "16 August 1946",
        "1946-47",
        "20 February 1947",
        "March 1947",
        "3 June 1947",
        "18 July 1947",
        "15 August 1947",
        "17 August 1947",
        "13 and 14 August 2026",
    ],
}

FORBIDDEN_TOPIC_PHRASES = {
    "modern-indian-history-26": [
        "INA won India's independence",
        "INA alone won India's independence",
        "Rash Behari Bose commanded the INA",
        "the Red Fort officers were executed",
        "RIN uprising was a Congress-led",
        "all national leaders supported the RIN",
        "Congress officially supported the RIN",
        "Congress officially supported the uprising",
        "Congress officially backed the RIN",
        "every national leader supported the uprising",
        "Jinnah appealed to all the ratings",
        "Jinnah asked all the ratings",
        "Jinnah's advice was addressed to all ratings",
        "Patel and Jinnah made the same appeal",
        "Patel and Jinnah issued identical appeals",
        "Cabinet Mission accepted the demand for Pakistan",
        "Cabinet Mission conceded Pakistan",
        "grouping was Partition",
        "elections were a plebiscite",
        "exactly 78 ships",
        "the first INA and Bose's INA are the same force",
        "caused the dispatch of the Cabinet Mission",
        "triggered the dispatch of the Cabinet Mission",
        "forced the British to send the Cabinet Mission",
        "compelled the British to send the Cabinet Mission",
        "Cabinet Mission was sent because of the RIN",
        "Cabinet Mission was a response to the RIN",
        "Cabinet Mission was announced in response to the naval",
        "uprising brought the Cabinet Mission",
        "naval strike produced the Cabinet Mission",
        "Cabinet Mission was despatched because of the RIN",
    ],
    "modern-indian-history-27": [
        "Cabinet Mission partitioned India",
        "the Cabinet Mission divided India",
        "Partition became inevitable in 1906",
        "Congress consistently supported Partition",
        "paramountcy passed automatically to India",
        "paramountcy was transferred to India",
        "Gandhi celebrated independence in Delhi",
        "the Act came into force on 14 August",
        "Mountbatten Plan was passed by Parliament",
        "British haste was the sole cause of Partition",
        "death toll was exactly",
        "Radcliffe alone caused",
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
        "scope": "Modern Indian History learner-v2 Topics 26-27",
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
    cursor = -1
    for marker in TOPIC_CHRONOLOGY[key]:
        found = fact_text.find(marker, cursor + 1)
        if found < 0:
            raise ValueError(
                f"{key}: chronology marker missing/out of order: {marker}"
            )
        cursor = found
    for phrase in FORBIDDEN_TOPIC_PHRASES[key]:
        if phrase.casefold() in markdown.casefold():
            raise ValueError(
                f"{key}: forbidden factual formulation found: {phrase}"
            )

    if key == "modern-indian-history-26":
        strict = [
            "Mohan Singh",
            "Rash Behari Bose",
            "not a field commander",
            "Imphal-Kohima",
            "Shah Nawaz Khan",
            "Prem Sahgal (also spelt Sehgal)",
            "Gurbaksh Singh Dhillon",
            "were not carried out",
            "18 February 1946",
            "HMIS Talwar",
            "22 January 1946",
            "19 February 1946",
            "did not cause or trigger the dispatch of the Cabinet Mission",
            "dispatch-causation claim is explicitly untenable",
            "crisis of coercive legitimacy",
            "not a Congress-led nationwide revolution",
            "did not officially support the struggle",
            "addressed to Muslim ratings alone",
            "tactics and the timing wrong",
            "commonly cited estimates",
            "16 May 1946",
            "16 June 1946",
            "Pethick-Lawrence",
            "A.V. Alexander",
            "finances required for those subjects",
            "British Baluchistan",
            "rejected a sovereign Pakistan",
            "grouping was not Partition",
            "29 July 1946",
            "2 September 1946",
            "26 October 1946",
            "9 December 1946",
            "not a plebiscite",
            "wartime exhaustion",
            "non-official study and current-affairs bridge",
        ]
    else:
        strict = [
            "did not partition India",
            "Great Calcutta Killings",
            "never to whole communities",
            "20 February 1947",
            "not later than June 1948",
            "last Viceroy",
            "3 June Plan",
            "Royal Assent on 18 July 1947",
            "15 August 1947",
            "14 August",
            "did not pass wholesale to India",
            "referendums in the North-West Frontier Province and Sylhet",
            "Two separate boundary commissions",
            "17 August 1947",
            "reluctant and pragmatic",
            "not made inevitable",
            "No single-villain explanation",
            "around 10 to 15 million",
            "must not be stated with false precision",
            "not celebrating in Delhi",
            "analytically simultaneous",
            "Ministry of Culture",
            "13 and 14 August 2026",
        ]
    missing = [
        phrase for phrase in strict if phrase.casefold() not in markdown.casefold()
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
    """Topics 24-25 must remain exactly as their own generator authored them."""

    expected = ["modern-indian-history-24", "modern-indian-history-25"]
    if [config["key"] for config in previous.TOPICS] != expected:
        raise ValueError("Topics 24-25 configuration was mutated on import.")
    if set(previous.PANEL_DATA) != set(expected):
        raise ValueError("Topics 24-25 panel data was mutated on import.")


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
