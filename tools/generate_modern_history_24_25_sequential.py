"""Build Modern Indian History learner-v2 Topics 24-25.

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
import generate_modern_history_22_23_sequential as previous


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
    / "modern-indian-history-24-25-2026-08-31-sequential.json"
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
            ROOT / "knowledge-export" / "Prelims PYQ" / "2024-GS1-Set A.md",
            ROOT / "knowledge-export" / "Prelims PYQ" / "Ans-2024-GS1.md",
            ROOT / "knowledge-export" / "Prelims PYQ" / "QP-CSP-18-GS-I-C.pdf.md",
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
        24,
        "The Government of India Act 1935 & the Congress Ministries "
        "(1937\u20131939)",
        "24_Government-of-India-Act-1935-and-Congress-Ministries.md",
        "24_Government-of-India-Act-1935-and-Congress-Ministries.md",
        "24_Government-of-India-Act-1935-Congress-Ministries-1937-1939_"
        "Complete-Topic-Package.md",
        [
            "basic/22_Simon-Nehru-Report-CDM-and-RTC.md",
            "basic/23_Left-Peasant-Workers-and-States-Peoples-Movements.md",
            "basic/25_WWII-Cripps-Mission-and-Quit-India.md",
            "advanced/22_Simon-Nehru-Report-CDM-and-RTC.md",
        ],
        [
            "https://www.scobserver.in/reports/governor-and-presidents-powers-"
            "judgement-summary-special-reference-2025-advisory-opinion/",
        ],
        "The November 2025 Supreme Court Observer summary of the Presidential "
        "Reference advisory opinion on gubernatorial and presidential discretion "
        "is used only as a structurally analogous current bridge illustrating "
        "why governor-discretion questions remain a live constitutional issue. "
        "It is not cited as evidence that the Court invoked the Government of "
        "India Act, 1935, and no 1935-specific judicial reliance is claimed.",
        "The Basic and Advanced owner files were reconciled with the "
        "repository's constitutional-history OCR sources on the Simon "
        "Commission, the Round Table Conferences and the 1935 Act; the "
        "franchise figures are retained as a qualified 30-35 million / "
        "10-14 per cent range because local sources do not converge on one "
        "exact figure.",
        "The exact 2024 Prelims GS-I Q62 stem is taken from "
        "`knowledge-export/Prelims PYQ/2024-GS1-Set A.md`; its official "
        "Series-A answer is independently confirmed from "
        "`knowledge-export/Prelims PYQ/Ans-2024-GS1.md`. The exact 2018 "
        "Prelims GS-I Q38 stem is retained from `QP-CSP-18-GS-I-C.pdf.md`, "
        "but no answer letter is invented because no local official key is "
        "held for that paper.",
        [
            (
                "Constitutional lineage to the 1935 Act",
                "The Act's constitutional lineage ran from the Simon "
                "Commission's 1930 report through three Round Table "
                "Conferences between 1930 and 1932, the 1933 White Paper "
                "and the Joint Select Committee's 1934 report before the "
                "Bill received royal assent in 1935.",
            ),
            (
                "Two separable halves of the Act",
                "The Act is best read as two separable halves: an "
                "All-India Federation with dyarchy at the centre, and "
                "provincial autonomy with dyarchy abolished in the "
                "provinces; each half must be evaluated on its own footing.",
            ),
            (
                "Federation never came into force",
                "Although the All-India Federation was central to the "
                "Act's design, princely accession never reached the "
                "required threshold, so the Federation never came into "
                "force; describing the federation as having operated at "
                "any point is a factual error.",
            ),
            (
                "Dyarchy redesigned, not merely abolished",
                "The Act abolished provincial dyarchy and replaced it with "
                "provincial autonomy; central dyarchy was only proposed "
                "for the unrealised federal centre and never operated in "
                "practice.",
            ),
            (
                "Governor's discretionary powers and special responsibilities",
                "Provincial autonomy was bounded by the governor's "
                "discretionary powers and special responsibilities, which "
                "allowed a governor to override or restrain ministerial "
                "advice on named grounds such as minority protection and "
                "the prevention of grave menace to peace.",
            ),
            (
                "Section 93 takeover power",
                "Section 93 of the Act empowered a governor to take over "
                "a province's administration if constitutional machinery "
                "failed, a background reserve power that followed rather "
                "than caused the 1939 ministerial resignations.",
            ),
            (
                "Reserved subjects and residuary power",
                "Defence, External Affairs, Ecclesiastical Affairs and "
                "Tribal Areas were the four subjects formally reserved to the "
                "Governor-General at the federal level, and residuary "
                "legislative power over unlisted subjects was vested in "
                "the Governor-General rather than any legislature.",
            ),
            (
                "Franchise reform as a qualified range",
                "The 1935 Act's franchise reforms are best stated as a "
                "qualified range rather than one exact figure: estimates "
                "place the enlarged electorate at roughly 30 to 35 "
                "million voters, or roughly 10 to 14 per cent of the "
                "population depending on which denominator or source is "
                "used.",
            ),
            (
                "RBI Act 1934 versus the 1935 Act",
                "The Reserve Bank of India was established under the "
                "Reserve Bank of India Act, 1934, a separate statute "
                "enacted before the Government of India Act, 1935, so the "
                "Reserve Bank must never be described as a creation of "
                "the 1935 Act itself.",
            ),
            (
                "Federal Court and Burma separation, 1937",
                "The Federal Court of India began functioning in 1937 to "
                "interpret disputes under the Act, and Burma's separation "
                "from India, provided for by the Act, took effect in 1937 "
                "as well \u2014 parallel developments rather than causally "
                "connected events.",
            ),
            (
                "1937 election and ministry-formation timing",
                "In the elections of February 1937 Congress emerged as "
                "the largest party in most provinces. Congress ministries "
                "took office in six provinces in July 1937, the North-West "
                "Frontier Province followed later in 1937, and Assam followed "
                "in 1938, so the eight-of-eleven figure names the eventual, "
                "not the simultaneous, position.",
            ),
            (
                "NWFP and Assam in the ministry count",
                "The North-West Frontier Province is counted among the "
                "provinces where Congress formed a ministry, while "
                "Assam's Congress ministry followed only after initial "
                "coalition arrangements broke down, so its timing must "
                "not be flattened into the original seven.",
            ),
            (
                "1937 office-acceptance debate",
                "Congress's 1937 office-acceptance debate weighed the "
                "risk of legitimising a limited constitutional structure "
                "against the organisational and reformist opportunities "
                "that provincial office could deliver.",
            ),
            (
                "Achievements of Congress ministries",
                "Congress ministries expanded civil liberties, released "
                "political prisoners, advanced tenancy and debt-relief "
                "legislation, and promoted prohibition and primary "
                "education within their limited provincial powers.",
            ),
            (
                "Structural limits of Congress ministries",
                "The ministries' achievements were bounded by restricted "
                "provincial finance, landlord-weighted legislatures, "
                "governors' reserve powers, and continuing labour unrest "
                "that agrarian reform did not fully resolve.",
            ),
            (
                "1939 resignation of Congress ministries",
                "Congress ministries resigned between October and "
                "November 1939 after the Viceroy declared India a party "
                "to the war without consulting Indian political opinion, "
                "a decision addressed fully within the Second World War "
                "topic.",
            ),
            (
                "Muslim League's Deliverance Day",
                "The Muslim League observed 22 December 1939 as a "
                "Deliverance Day to mark the ministries' resignation, a "
                "response that must be read as one party reaction among "
                "several rather than a neutral national commemoration.",
            ),
            (
                "Lahore Resolution as one link in a chain",
                "The Lahore Resolution of March 1940 followed these "
                "events as one link in a longer chain of developments "
                "and must never be read as evidence of a single, simple "
                "causal path to Partition.",
            ),
            (
                "2024 Prelims GS-I Q62 as primary anchor",
                "The 2024 Prelims GS-I question on the federal scheme "
                "and reserved powers of the Government of India Act, "
                "1935 is answered from the Act's own text with a "
                "confirmed official key, and this package treats it as "
                "the primary revision anchor for the topic.",
            ),
            (
                "2018 Prelims GS-I Q38 residuary-power caution",
                "A 2018 Prelims GS-I question probes the same Act's "
                "residuary-power design, but its official answer key is "
                "not held locally, so this package states the "
                "source-backed content without asserting an unverified "
                "answer letter.",
            ),
        ],
        [
            "The All-India Federation never came into force; do not "
            "describe it as operating at any point.",
            "Provincial dyarchy was abolished, not merely modified; "
            "central dyarchy never operated because the federation was "
            "never established.",
            "Section 93 was a background reserve power that followed, "
            "not caused, the 1939 resignations.",
            "The Reserve Bank of India was created under the RBI Act, "
            "1934, not the Government of India Act, 1935.",
            "Franchise figures vary by source; state a qualified "
            "30-35 million / 10-14% range, not one exact figure.",
            "Congress ministries took office in six provinces in July 1937; "
            "NWFP followed later in 1937 and Assam in 1938, making eight the "
            "eventual, not simultaneous, total.",
            "Defence, External Affairs, Ecclesiastical Affairs and Tribal "
            "Areas were reserved central subjects; residuary power vested in "
            "the Governor-General, not any legislature.",
            "The Lahore Resolution of March 1940 was one link in a "
            "chain of developments, not a simple direct cause of "
            "Partition.",
        ],
        [
            (
                10,
                "Explain why the All-India Federation envisaged by the "
                "Government of India Act, 1935 never came into force, "
                "and distinguish this from the fate of the Act's "
                "provincial half.",
                "Princely non-accession, not any provincial failure, "
                "kept the federal centre from ever functioning, while "
                "provincial autonomy operated on its own separate "
                "footing throughout 1937-39.",
                [1, 2],
            ),
            (
                10,
                "Distinguish the governor's discretionary powers and "
                "special responsibilities from the Section 93 takeover "
                "power under the Government of India Act, 1935.",
                "The two instruments differed in scope and trigger: "
                "discretionary/special-responsibility override operated "
                "continuously on named grounds, while Section 93 was a "
                "background emergency power activated only by a "
                "breakdown of constitutional machinery.",
                [4, 5],
            ),
            (
                15,
                "Examine the case for and against Congress's 1937 "
                "decision to accept provincial office, and assess the "
                "achievements and limits of the Congress ministries of "
                "1937-39.",
                "Office acceptance traded the risk of legitimising a "
                "bounded constitutional structure for real reformist "
                "gains, producing a mixed record of civil-liberties and "
                "agrarian achievement constrained by finance, franchise "
                "and reserve powers.",
                [12, 13, 14],
            ),
            (
                15,
                "Trace the sequence from the resignation of the "
                "Congress ministries in 1939 to the Muslim League's "
                "Deliverance Day and the Lahore Resolution, without "
                "treating it as a single, simple cause of Partition.",
                "Unconsulted wartime belligerency triggered resignation, "
                "which the League marked separately, and only later did "
                "Lahore emerge as one link in a longer, multi-causal "
                "chain.",
                [15, 16, 17],
            ),
            (
                20,
                "Critically examine the constitutional architecture of "
                "the Government of India Act, 1935, with reference to "
                "the unrealised federation, the redesigned dyarchy, the "
                "reserved central subjects and the franchise reforms.",
                "The Act combined an ambitious but stillborn federal "
                "design with a genuinely operative, though "
                "governor-bounded, provincial autonomy, reserving "
                "ultimate central authority and widening, but not "
                "democratising, the franchise.",
                [2, 3, 6, 7],
            ),
            (
                20,
                "Trace the constitutional lineage of the Government of "
                "India Act, 1935 from the Simon Commission to the "
                "Lahore Resolution, evaluating both its "
                "provincial-autonomy achievements and its federal-centre "
                "limitations.",
                "A five-stage constitutional review produced an Act "
                "whose provincial half delivered genuine, if bounded, "
                "reform while its federal half never came into force, "
                "and whose 1939 wartime rupture opened, without "
                "determining, the path toward Lahore.",
                [0, 10, 15, 17],
            ),
        ],
        [
            (
                "2024",
                "Prelims GS-I Q62",
                "With reference to the Government of India Act, 1935, "
                "consider the following statements: 1. It provided for "
                "the establishment of an All India Federation based on "
                "the union of the British Indian Provinces and Princely "
                "States. 2. Defence and Foreign Affairs were kept under "
                "the control of the federal legislature. Which of the "
                "statements given above is/are correct? (a) 1 only "
                "(b) 2 only (c) Both 1 and 2 (d) Neither 1 nor 2 "
                "(2024-GS1-Set A.md)",
                "official-key-confirmed",
                "The official Series-A answer is **A - 1 only**, "
                "verified from `Ans-2024-GS1.md`. Statement 1 is "
                "correct: the Act did provide for an All-India "
                "Federation of British Indian provinces and princely "
                "states, even though that federation never came into "
                "force. Statement 2 is incorrect: Defence and External "
                "Affairs were reserved to the Governor-General, not kept "
                "under the control of the federal legislature.",
            ),
            (
                "2018",
                "Prelims GS-I Q38",
                "In the Federation established by the Government of "
                "India Act of 1935, residuary powers were given to the "
                "(a) Federal Legislature (b) Governor General "
                "(c) Provincial Legislature (d) Provincial Governors "
                "(QP-CSP-18-GS-I-C.pdf.md)",
                "official-stem-key-unavailable",
                "The source-backed answer is the Governor-General, who "
                "held residuary legislative power over unlisted subjects "
                "under the Act's federal scheme; no answer letter is "
                "asserted because no local official 2018 key is held "
                "for this paper.",
            ),
        ],
        [
            "Simon Commission's 1930 report",
            "Round Table Conferences",
            "1933 White Paper",
            "Joint Select Committee",
            "royal assent in 1935",
            "All-India Federation",
            "provincial autonomy",
            "central dyarchy",
            "Section 93",
            "Governor-General",
            "Ecclesiastical Affairs",
            "Tribal Areas",
            "roughly 30 to 35 million",
            "roughly 10 to 14 per cent",
            "Reserve Bank of India Act, 1934",
            "Federal Court of India",
            "Burma",
            "February 1937",
            "North-West Frontier Province",
            "Assam",
            "Deliverance Day",
            "Lahore Resolution",
            "Prelims GS-I Q62",
            "Prelims GS-I Q38",
        ],
    ),
    base.topic(
        25,
        "Second World War, the Cripps Mission & Quit India (1939\u20131942)",
        "25_WWII-Cripps-Mission-and-Quit-India.md",
        "25_WWII-Cripps-Mission-and-Quit-India.md",
        "25_Second-World-War-Cripps-Mission-Quit-India-1939-1942_"
        "Complete-Topic-Package.md",
        [
            "basic/24_Government-of-India-Act-1935-and-Congress-Ministries.md",
            "basic/26_Post-War-Upsurge-INA-RIN-Mutiny-Cabinet-Mission.md",
            "advanced/24_Government-of-India-Act-1935-and-Congress-Ministries.md",
            "basic/23_Left-Peasant-Workers-and-States-Peoples-Movements.md",
        ],
        [
            "https://www.insightsonindia.com/2026/08/08/the-quit-india-movement/",
        ],
        "A verified InsightsIAS current-affairs page dated 8 August 2026 on "
        "the Quit India Movement is used only as a restrained study-relevance "
        "bridge; any incidental claim of an official parliamentary or "
        "government tribute could not be independently verified against any "
        "official source, so this package treats it strictly as private-"
        "website study commentary and makes no claim about any 2026 official "
        "or parliamentary tribute.",
        "The Basic and Advanced owner files were reconciled with the "
        "repository's constitutional and political-history OCR sources for "
        "the Second World War period, the August Offer, the Cripps Mission "
        "and the Quit India Movement; the 'post-dated cheque' quotation is "
        "retained only in its shorter, better-attested form.",
        "The exact 2024 Mains GS-I Q3 stem is taken verbatim from "
        "`knowledge-export/Mains PYQ/UPSC Mains 2024 GS Paper I.md` and "
        "cross-confirmed against "
        "`_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md`. The 2021 Prelims "
        "Q43 and 2022 Prelims Q54 entries are recorded as routing-ledger "
        "demand summaries from `_PYQ-ROUTING-PRELIMS-2018-2023.md` rather "
        "than verbatim stems, and no answer letter is asserted for either "
        "because no official stem or key is held locally.",
        [
            (
                "Unconsulted belligerency, 3 September 1939",
                "The Viceroy declared war on Germany on 3 September "
                "1939; the Viceroy simultaneously declared India a "
                "belligerent without consulting any Indian political "
                "leader or elected legislature.",
            ),
            (
                "Resignation to Lahore Resolution chain",
                "Congress ministries resigned between October and "
                "November 1939 in protest; the Muslim League observed "
                "22 December 1939 as a Deliverance Day, and the Lahore "
                "Resolution of March 1940 followed as one link in a "
                "chain of connected party responses rather than one "
                "simple cause.",
            ),
            (
                "August Offer's constitution-making promise",
                "The August Offer of 8 August 1940 proposed an "
                "expanded, more representative body for post-war "
                "constitution-making and promised that minority views "
                "would be given full weight, but it did not offer an "
                "immediate national government.",
            ),
            (
                "August Offer's minority-consent veto",
                "The August Offer's constitution-making promise carried "
                "a minority-consent condition: no future constitution "
                "would be adopted without the consent of India's "
                "minorities, giving minority communities an effective "
                "veto over any post-war settlement.",
            ),
            (
                "Individual Satyagraha's October 1940 sequence",
                "Individual Satyagraha began on 17 October 1940 with "
                "Vinoba Bhave offering civil disobedience first, "
                "followed by Jawaharlal Nehru as the second satyagrahi, "
                "each individually courting arrest rather than "
                "launching mass action.",
            ),
            (
                "Individual Satyagraha's limited objective",
                "Individual Satyagraha pursued a limited anti-war "
                "free-speech objective \u2014 the right to publicly "
                "oppose India's forced participation in the war \u2014 "
                "and must not be described as a mass movement.",
            ),
            (
                "Cripps Mission arrival and proposals, March 1942",
                "Sir Stafford Cripps arrived in India in March 1942 and "
                "announced his proposals in late March 1942, offering "
                "Dominion status after the war and a constitution-making "
                "body to be convened once the war ended.",
            ),
            (
                "Cripps opt-out and non-accession clause",
                "The Cripps proposals allowed any province, or any "
                "princely state, to opt out of, or not accede to, the "
                "new Indian union that the post-war constitution-making "
                "body might create.",
            ),
            (
                "Princely nomination in the Cripps scheme",
                "Princely states would be represented in the proposed "
                "constitution-making body by members nominated by their "
                "rulers rather than by any popularly elected process.",
            ),
            (
                "British wartime control and no immediate cabinet",
                "The Cripps proposals kept defence and the general "
                "conduct of the war under British control for the "
                "war's duration and offered no immediate responsible "
                "national cabinet.",
            ),
            (
                "Multi-party rejection of the Cripps proposals",
                "Congress objected to the deferred and conditional "
                "nature of the offer, the League objected that it did "
                "not guarantee Pakistan, and Sikh, Hindu Mahasabha and "
                "some princely opinion raised separate objections, so "
                "the rejection was multi-party and not uniform in its "
                "reasoning.",
            ),
            (
                "Post-dated cheque phrase and its provenance",
                "Gandhi's remark that the offer was like a post-dated "
                "cheque is commonly quoted in its short form; the "
                "longer phrase adding a 'crashing bank' is widely "
                "repeated but its exact wording and occasion carry "
                "uncertain provenance, so this package uses only the "
                "shorter, better-attested phrase and applies it solely "
                "to the Cripps proposals, never to the August Offer.",
            ),
            (
                "Quit India's two-stage resolution",
                "The Quit India resolution was adopted in two stages: "
                "the Congress Working Committee approved it at Wardha "
                "on 14 July 1942, and the All-India Congress Committee "
                "ratified it at Bombay on 8 August 1942 \u2014 a "
                "two-stage process that should never be collapsed into "
                "a single date.",
            ),
            (
                "Operation Zero Hour timing",
                "Mass arrests under what the government called "
                "Operation Zero Hour began early on 9 August 1942, one "
                "day after, not on the same day as, the Bombay "
                "resolution.",
            ),
            (
                "Do or Die and the Gowalia Tank flag",
                "Gandhi's 8 August 1942 call to 'Do or Die' set the "
                "movement's tone, and Aruna Asaf Ali is associated with "
                "hoisting the Congress flag at Gowalia Tank in Bombay "
                "after the leadership's arrest.",
            ),
            (
                "Underground resistance networks",
                "Underground resistance included Usha Mehta's secret "
                "Congress Radio broadcasts and the clandestine "
                "organising of Jayaprakash Narayan and Ram Manohar "
                "Lohia after most senior leaders were arrested.",
            ),
            (
                "Parallel national governments",
                "Parallel national governments were declared at "
                "Ballia, at Tamluk in Midnapore as the Jatiya Sarkar, "
                "and at Satara as the Prati Sarkar, each surviving for "
                "a different duration before being suppressed or wound "
                "down.",
            ),
            (
                "Movement's social base and repression caution",
                "The movement combined student, worker and peasant "
                "participation with regional variation in intensity "
                "and included both sabotage of communication lines and "
                "Congress's own non-violent creed; repression was "
                "harsh, but this package avoids stating unsupported "
                "exact casualty or arrest totals.",
            ),
            (
                "Political alignments during Quit India",
                "The Muslim League remained aloof from or opposed the "
                "movement, the Communist Party of India followed a "
                "People's War line supporting the British war effort "
                "after June 1941, and the Hindu Mahasabha and many "
                "princely rulers stayed distant from or opposed the "
                "agitation.",
            ),
            (
                "Quit India's results and the 2024 Mains anchor",
                "Quit India was suppressed by the government within "
                "months through mass arrests and force, and it did not "
                "by itself win India's independence, but it "
                "demonstrated the depth of popular anti-colonial "
                "sentiment; a verified 2024 Mains GS-I question asks "
                "what events led to the Quit India Movement and its "
                "results, and this package treats that question as its "
                "primary anchor.",
            ),
        ],
        [
            "War was declared on 3 September 1939 and India was made a "
            "belligerent without any Indian political consultation.",
            "The August Offer promised a more representative "
            "constitution-making body and minority consent, not an "
            "immediate national government.",
            "Individual Satyagraha was a limited, individual anti-war "
            "protest beginning with Vinoba Bhave and then Nehru, not a "
            "mass movement.",
            "The Cripps proposals allowed provinces and princely states "
            "to opt out; princely representatives were nominated by "
            "rulers, not elected.",
            "Congress, the League and other groups rejected the Cripps "
            "proposals for different, not identical, reasons.",
            "The short 'post-dated cheque' phrase is well attested; the "
            "longer 'crashing bank' addition has uncertain provenance "
            "and should be used cautiously.",
            "The Quit India resolution was passed at Wardha on 14 July "
            "1942 and ratified at Bombay on 8 August 1942 \u2014 two "
            "distinct dates.",
            "Mass arrests under Operation Zero Hour began in the early hours "
            "of 9 August 1942, within hours of the Bombay resolution on the "
            "following calendar day, not simultaneously.",
        ],
        [
            (
                10,
                "Explain how India's unconsulted entry into the Second "
                "World War as a belligerent connected to the Congress "
                "ministries' resignation and the subsequent chain of "
                "party responses.",
                "Unilateral belligerency without consultation supplied "
                "the direct trigger for resignation, which the Muslim "
                "League marked separately through its own Deliverance "
                "Day before the Lahore Resolution followed months "
                "later as a connected, not identical, response.",
                [0, 1],
            ),
            (
                10,
                "Distinguish the August Offer of 1940 from the Cripps "
                "proposals of 1942 in their treatment of post-war "
                "constitution-making and immediate self-government.",
                "Both offers deferred real power to a post-war "
                "constitution-making process, but the August Offer's "
                "minority-consent condition and the Cripps opt-out and "
                "nomination clauses reveal two distinct, non-identical "
                "designs for managing minority and princely consent.",
                [2, 6],
            ),
            (
                15,
                "Critically examine why the Cripps proposals of 1942 "
                "were rejected by every major political formation in "
                "India.",
                "Deferred post-war Dominion status, an opt-out clause, "
                "ruler-nominated princely representation and continued "
                "British wartime control together gave Congress, the "
                "League and other groups distinct, non-identical "
                "grounds for rejection.",
                [7, 8, 9, 10],
            ),
            (
                15,
                "Examine the character and limited objective of "
                "Individual Satyagraha, distinguishing it clearly from "
                "a mass civil-disobedience movement.",
                "Individual Satyagraha's narrow anti-war free-speech "
                "objective and its individually selected participants "
                "mark it as a deliberately restrained campaign, "
                "distinct in scale and method from the harsh but "
                "genuinely mass repression later associated with Quit "
                "India.",
                [4, 5, 17],
            ),
            (
                20,
                "Critically examine the Cripps Mission's proposals of "
                "1942 and the reasons for their rejection by different "
                "Indian political groups.",
                "The Cripps scheme combined a genuine post-war "
                "constitutional offer with an opt-out clause, "
                "ruler-nominated princely representation and continued "
                "British wartime control, producing a multi-party "
                "rejection whose reasoning differed sharply across "
                "Congress, the League and other groups.",
                [6, 7, 8, 9, 10],
            ),
            (
                20,
                "Trace the full chain of developments from India's "
                "forced entry into the Second World War to the Quit "
                "India Movement, and evaluate the movement's immediate "
                "and long-term results.",
                "Unconsulted belligerency, the resignation-to-Lahore "
                "chain, the Cripps Mission's failure and the two-stage "
                "Quit India resolution together explain the movement's "
                "origins, while its swift suppression alongside its "
                "lasting demonstration of popular anti-colonial "
                "sentiment together define its results.",
                [0, 6, 12, 19],
            ),
        ],
        [
            (
                "2024",
                "Mains GS-I Q3",
                "What were the events that led to the Quit India "
                "Movement? Point out its results. (Answer in 150 "
                "words) [UPSC Mains 2024 GS Paper I.md]",
                "official-mains-question-verbatim-confirmed",
                "Trace unconsulted belligerency (3 September 1939), the "
                "ministries' resignation and the Lahore Resolution "
                "chain, the August Offer's limits, Individual "
                "Satyagraha, the Cripps Mission's rejection by every "
                "major group, and the two-stage Quit India resolution "
                "(Wardha 14 July, Bombay 8 August 1942) as the events; "
                "state the results as swift suppression through "
                "Operation Zero Hour without the movement alone "
                "winning independence, alongside its lasting "
                "demonstration of popular anti-colonial sentiment.",
            ),
            (
                "2021",
                "Prelims GS-I Q43",
                "Quit India Resolution adopted August 1942 AICC "
                "(routing-ledger demand summary; exact stem not held "
                "locally) [_PYQ-ROUTING-PRELIMS-2018-2023.md]",
                "official-stem-verbatim-unavailable-neutral-demand-only",
                "Use only the routed demand theme \u2014 the AICC's "
                "August 1942 ratification of the Quit India Resolution "
                "at Bombay on 8 August 1942 \u2014 for revision; no "
                "verbatim stem or answer letter is asserted because "
                "neither is held locally.",
            ),
            (
                "2022",
                "Prelims GS-I Q54",
                "Cripps Mission proposals for Indian constitution and "
                "provinces (routing-ledger demand summary; exact stem "
                "not held locally) [_PYQ-ROUTING-PRELIMS-2018-2023.md]",
                "official-stem-verbatim-unavailable-neutral-demand-only",
                "Use only the routed demand theme \u2014 the Cripps "
                "proposals' post-war constitution-making body and the "
                "province/princely-state opt-out clause \u2014 for "
                "revision; no verbatim stem or answer letter is "
                "asserted because neither is held locally.",
            ),
        ],
        [
            "3 September 1939",
            "belligerent",
            "August Offer",
            "8 August 1940",
            "minority-consent",
            "Individual Satyagraha",
            "17 October 1940",
            "Vinoba Bhave",
            "Jawaharlal Nehru",
            "Cripps",
            "March 1942",
            "opt out",
            "nominated by their rulers",
            "post-dated cheque",
            "Wardha",
            "14 July 1942",
            "Bombay",
            "8 August 1942",
            "Operation Zero Hour",
            "9 August 1942",
            "Do or Die",
            "Aruna Asaf Ali",
            "Gowalia Tank",
            "Usha Mehta",
            "Congress Radio",
            "Jayaprakash Narayan",
            "Ram Manohar Lohia",
            "Ballia",
            "Jatiya Sarkar",
            "Prati Sarkar",
            "People's War",
            "Mains GS-I Q3",
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
    "modern-indian-history-24": [
        authored_session(
            "Constitutional lineage: from Simon to royal assent",
            "The Government of India Act, 1935 was the end point of a five-"
            "stage constitutional review, not a sudden imperial gift, and "
            "every earlier stage narrowed or reshaped what the final Act "
            "could contain.",
            [
                "The Simon Commission's 1930 report opened the sequence.",
                "Three Round Table Conferences between 1930 and 1932 debated "
                "federation and communal representation.",
                "The 1933 White Paper converted RTC discussion into a draft "
                "scheme.",
                "The Joint Select Committee's 1934 report refined that "
                "scheme before the Bill received royal assent in 1935.",
            ],
            "Keep the five stages in strict order; do not compress Simon, "
            "the RTCs, the White Paper and the Joint Select Committee into "
            "one undifferentiated background.",
            "Open a constitutional-history answer on the 1935 Act with this "
            "five-stage lineage before discussing the Act's own content.",
            """SIMON REPORT (1930) -> RTCs (1930-32) -> WHITE PAPER (1933)
        -> JOINT SELECT COMMITTEE (1934) -> ROYAL ASSENT (1935)
RULE -> each stage narrowed the next; none can be skipped in a lineage answer.""",
            "The 1935 Act's constitutional lineage is the ordered sequence "
            "Simon Report, Round Table Conferences, White Paper and Joint "
            "Select Committee, ending in royal assent.",
        ),
        authored_session(
            "Two halves of the Act and the federation that never operated",
            "The 1935 Act is best analysed as two separable halves \u2014 an "
            "All-India Federation with central dyarchy, and provincial "
            "autonomy with dyarchy abolished \u2014 and only the provincial "
            "half ever became operative.",
            [
                "The federal half required princely accession above a fixed "
                "threshold of federating units and population.",
                "That threshold was never reached, so the All-India "
                "Federation never came into force at any point.",
                "The provincial half took effect in 1937 independently of "
                "the federation's fate.",
                "Treating the federation as if it operated is a direct "
                "factual error, not a simplification.",
            ],
            "Never describe the All-India Federation as having come into "
            "force, functioned, or operated \u2014 in any tense.",
            "Use the two-halves structure to answer questions that ask you "
            "to evaluate the 1935 Act 'in practice' versus 'on paper'.",
            """ACT'S TWO HALVES
|-- FEDERAL HALF -> All-India Federation + central dyarchy -> NEVER IN FORCE
`-- PROVINCIAL HALF -> provincial autonomy, dyarchy abolished -> OPERATED 1937
RULE -> federation's non-operation must never be blurred with the provincial record.""",
            "The 1935 Act's federal half, comprising the All-India "
            "Federation and central dyarchy, never came into force because "
            "princely accession never reached the required threshold.",
        ),
        authored_session(
            "Provincial dyarchy abolished, not merely modified",
            "The 1935 Act did not soften provincial dyarchy; it abolished "
            "it outright and replaced it with a new, more complete "
            "provincial autonomy.",
            [
                "Dyarchy under the 1919 Act had split provincial subjects "
                "into reserved and transferred categories.",
                "The 1935 Act ended that split for the provinces and "
                "handed the whole provincial subject list to ministers.",
                "Central dyarchy was only ever proposed for the unrealised "
                "federal centre, never for the provinces.",
                "Because the federation never came into force, central "
                "dyarchy never operated anywhere.",
            ],
            "Do not say the Act 'modified' provincial dyarchy; it abolished "
            "it, and do not describe central dyarchy as operating.",
            "Use this session to correct the common exam error of confusing "
            "provincial and central dyarchy under the 1935 Act.",
            """1919 ACT -> provincial dyarchy (reserved + transferred subjects)
1935 ACT -> provincial dyarchy ABOLISHED -> provincial autonomy begins
CENTRAL DYARCHY -> proposed only for the federal centre -> never operated.""",
            "Provincial dyarchy is the pre-1935 division of provincial "
            "subjects into reserved and transferred categories, abolished "
            "by the 1935 Act and replaced with provincial autonomy.",
        ),
        authored_session(
            "Governor's discretionary powers and special responsibilities",
            "Provincial autonomy was never unconditional self-government; "
            "governors retained discretionary powers and special "
            "responsibilities that could override or restrain ministerial "
            "advice.",
            [
                "Discretionary powers let a governor act without ministerial "
                "advice on named matters.",
                "Special responsibilities let a governor override advice on "
                "grounds such as protecting minorities or preventing grave "
                "menace to peace.",
                "These powers operated continuously through the life of "
                "each ministry, not only in a crisis.",
                "They are the structural reason provincial autonomy is "
                "called bounded rather than complete.",
            ],
            "Distinguish discretionary powers and special responsibilities, "
            "which operated continuously, from Section 93, which was an "
            "emergency takeover power.",
            "Use this session for any question on the limits of 1937-39 "
            "provincial self-government.",
            """GOVERNOR'S POWERS UNDER PROVINCIAL AUTONOMY
|-- DISCRETIONARY -> acts without ministerial advice on named subjects
`-- SPECIAL RESPONSIBILITIES -> can override advice (minorities, peace)
BOTH -> operate continuously, distinct from the emergency Section 93 power.""",
            "Discretionary powers and special responsibilities were "
            "standing governor authorities under the 1935 Act that could "
            "override or bypass ministerial advice on named grounds.",
        ),
        authored_session(
            "Section 93: the background emergency reserve power",
            "Section 93 was a distinct, narrower instrument from "
            "discretionary powers: it let a governor take over a "
            "province's administration only if constitutional machinery "
            "had actually broken down.",
            [
                "Section 93 required an actual breakdown of constitutional "
                "government, not routine policy disagreement.",
                "It remained a background reserve power throughout 1937-39, "
                "unused in the day-to-day running of Congress ministries.",
                "The 1939 resignations were triggered by unconsulted "
                "wartime belligerency, not by any Section 93 action.",
                "Section 93 followed, and did not cause, the ministries' "
                "own decision to resign.",
            ],
            "Never claim Section 93 was the direct cause of the 1939 "
            "resignations; keep the reserve power and the resignation "
            "trigger analytically separate.",
            "Use this session to answer any question that tests whether "
            "Section 93 'ended' the Congress ministries \u2014 it did not.",
            """SECTION 93 -> governor may take over administration
TRIGGER -> actual breakdown of constitutional machinery (not policy dispute)
1937-39 -> stayed a background reserve power, unused against Congress ministries
1939 RESIGNATION -> caused by unconsulted war declaration, not Section 93.""",
            "Section 93 was the 1935 Act's emergency provision letting a "
            "governor take over provincial administration on an actual "
            "breakdown of constitutional machinery.",
        ),
        authored_session(
            "Reserved central subjects and residuary power",
            "At the (unrealised) federal centre, the Act reserved four "
            "named subjects to the Governor-General and vested all "
            "residuary power in the same office, concentrating ultimate "
            "authority away from any legislature.",
            [
                "Defence, External Affairs, Ecclesiastical Affairs and "
                "Tribal Areas were the four subjects formally reserved to "
                "the Governor-General.",
                "Residuary legislative power over any subject not listed "
                "in the Act's schedules also vested in the Governor-"
                "General.",
                "No federal legislature ever exercised control over these "
                "subjects because the federation never came into force.",
                "This design is the textual basis for the 2024 Prelims "
                "Q62 statement that Defence and External Affairs were kept "
                "under Governor-General, not legislative, control.",
            ],
            "State the four reserved subjects exactly \u2014 Defence, External "
            "Affairs, Ecclesiastical Affairs and Tribal Areas \u2014 and do "
            "not add or omit any of them.",
            "Use this session directly for the 2024 Prelims Q62 pattern on "
            "the federal scheme of the 1935 Act.",
            """FEDERAL CENTRE (never in force) -> reserved to Governor-General
|-- Defence
|-- External Affairs
|-- Ecclesiastical Affairs
`-- Tribal Areas
RESIDUARY POWER -> also vested in the Governor-General, not any legislature.""",
            "Reserved subjects were Defence, External Affairs, Ecclesiastical "
            "Affairs and Tribal Areas, kept under the Governor-General's "
            "control rather than any legislature.",
        ),
        authored_session(
            "Franchise reform as a qualified range, not one exact figure",
            "The 1935 Act widened the franchise substantially, but because "
            "sources differ on the denominator, the safest exam answer "
            "states a qualified range rather than a single exact number.",
            [
                "Estimates place the enlarged electorate at roughly 30 to "
                "35 million voters.",
                "As a share of the population, estimates range from "
                "roughly 10 to 14 per cent depending on the denominator "
                "used.",
                "This remains far short of universal adult franchise.",
                "An answer asserting one precise figure without "
                "qualification risks contradicting an equally plausible "
                "alternative source figure.",
            ],
            "Always state the franchise figures as a qualified range; "
            "never present one exact figure as if it were uncontested.",
            "Use the qualified range when a question asks about the extent "
            "of franchise reform under the 1935 Act.",
            """FRANCHISE UNDER THE 1935 ACT
ELECTORATE -> roughly 30 to 35 million voters (source-dependent)
SHARE OF POPULATION -> roughly 10 to 14 per cent (denominator-dependent)
RULE -> state as a qualified range; still short of universal adult franchise.""",
            "The 1935 Act's franchise reform enlarged the electorate to a "
            "source-dependent range of roughly 30 to 35 million voters, or "
            "roughly 10 to 14 per cent of the population.",
        ),
        authored_session(
            "RBI Act 1934 versus the Government of India Act 1935",
            "The Reserve Bank of India is a frequent exam trap because its "
            "founding statute, the Reserve Bank of India Act of 1934, "
            "predates and is legally separate from the Government of "
            "India Act of 1935.",
            [
                "The Reserve Bank of India Act was enacted in 1934, one "
                "year before the Government of India Act.",
                "The Reserve Bank began operations under its own 1934 "
                "statute, independent of the 1935 constitutional scheme.",
                "No provision of the 1935 Act itself created the Reserve "
                "Bank.",
                "Confusing the two Acts is one of the most common factual "
                "errors on this topic.",
            ],
            "Never attribute the Reserve Bank of India's creation to the "
            "Government of India Act, 1935; its statute is the RBI Act, "
            "1934.",
            "Use this session as a rapid-fire fact check whenever a "
            "question lists institutions alongside the 1935 Act.",
            """1934 -> Reserve Bank of India Act -> RBI founded
1935 -> Government of India Act -> separate constitutional statute
TRAP -> never merge the two; RBI's origin is the 1934 Act, not the 1935 Act.""",
            "The Reserve Bank of India Act, 1934 is the separate statute "
            "that established the Reserve Bank of India one year before "
            "the Government of India Act, 1935.",
        ),
        authored_session(
            "Federal Court and Burma separation: parallel 1937 developments",
            "1937 saw two distinct developments enabled by the 1935 Act "
            "begin in parallel: the Federal Court started functioning, and "
            "Burma's separation from India took effect.",
            [
                "The Federal Court of India began functioning in 1937 to "
                "interpret disputes arising under the Act.",
                "Burma's separation from India, provided for in the Act, "
                "took effect in 1937 as a separate administrative "
                "development.",
                "Both developments trace to provisions of the same 1935 "
                "Act but followed independent institutional tracks.",
                "Neither event is causally connected to the other; they "
                "are parallel, not sequential.",
            ],
            "Do not describe the Federal Court's start or Burma's "
            "separation as caused by each other; they are parallel 1937 "
            "developments under the same Act.",
            "Use this session for questions that test the year 1937 across "
            "multiple institutional developments under the 1935 Act.",
            """1935 ACT PROVISIONS -> two parallel 1937 developments
|-- FEDERAL COURT OF INDIA -> begins functioning, 1937
`-- BURMA SEPARATION -> takes effect, 1937
RULE -> parallel developments, not one causing the other.""",
            "The Federal Court of India and Burma's separation from India "
            "were two distinct developments that both took effect in 1937 "
            "under provisions of the 1935 Act.",
        ),
        authored_session(
            "1937 elections, ministry timing, NWFP and Assam",
            "The February 1937 elections gave Congress the largest bloc "
            "in most provinces, but ministry formation was not "
            "simultaneous everywhere, and two provinces \u2014 the North-"
            "West Frontier Province and Assam \u2014 deserve individually "
            "named treatment within that timing.",
            [
                "Elections were held in February 1937 under the new "
                "provincial franchise; after the governor-assurance dispute, "
                "Congress ministries took office in six provinces in July "
                "1937: Madras, Bombay, United Provinces, Bihar, Central "
                "Provinces and Orissa.",
                "The North-West Frontier Province became the seventh Congress "
                "ministry later in 1937.",
                "Assam's Congress ministry followed in 1938 after initial "
                "non-Congress coalition arrangements there broke down.",
                "The commonly cited eight-of-eleven figure names the "
                "eventual, not the simultaneous, position.",
            ],
            "Do not state that Congress formed eight ministries "
            "immediately after the February 1937 elections; distinguish the "
            "six July ministries, later NWFP ministry and 1938 Assam ministry.",
            "Use this session whenever a question asks for the exact "
            "number, or the specific names, of provinces with Congress "
            "ministries in 1937.",
            """FEB 1937 -> elections; Congress largest party in most provinces
JUL 1937 -> six ministries: Madras, Bombay, UP, Bihar, CP and Orissa
LATER 1937 -> NWFP becomes the seventh Congress ministry
1938 -> Assam becomes the eighth after coalition arrangements break down
RULE -> eight is the eventual total, not one simultaneous formation.""",
            "The 1937 ministry-formation timeline is the sequence in "
            "which Congress ministries took office in six provinces in July "
            "1937, the North-West Frontier Province followed later in 1937, "
            "and Assam became the eighth in 1938.",
        ),
        authored_session(
            "The 1937 office-acceptance debate inside Congress",
            "Before any ministry could form, Congress had to resolve a "
            "genuine internal debate over whether accepting provincial "
            "office would legitimise a limited constitutional structure.",
            [
                "One position warned that taking office risked "
                "legitimising a constitution Congress had officially "
                "rejected.",
                "The opposing position argued office offered real "
                "reformist and organisational opportunities within "
                "existing limits.",
                "Congress ultimately accepted office conditionally, "
                "watching for governor interference with ministerial "
                "authority.",
                "This debate frames every subsequent evaluation of the "
                "ministries' record.",
            ],
            "Present the office-acceptance debate as a genuine two-sided "
            "argument, not as an inevitable or uncontested Congress "
            "decision.",
            "Use this session to open any answer evaluating why Congress "
            "took office in 1937 at all.",
            """OFFICE-ACCEPTANCE DEBATE, 1937
FOR -> reformist and organisational opportunity within provincial autonomy
AGAINST -> risk of legitimising a constitution Congress had rejected
OUTCOME -> conditional acceptance, watching for governor interference.""",
            "The office-acceptance debate was Congress's 1937 internal "
            "argument over whether taking provincial office would "
            "legitimise the 1935 Act's limited constitutional structure.",
        ),
        authored_session(
            "Achievements and structural limits of the Congress ministries",
            "The 1937-39 Congress ministries produced real reformist gains "
            "but operated within structural limits that kept those gains "
            "from being complete.",
            [
                "Ministries expanded civil liberties and released "
                "political prisoners.",
                "They advanced tenancy and debt-relief legislation and "
                "promoted prohibition and primary education.",
                "Their finance remained restricted, legislatures stayed "
                "landlord-weighted, and governors retained reserve powers.",
                "Labour unrest and agrarian distress were reduced but not "
                "fully resolved by these reforms.",
            ],
            "Present achievements and limits together in the same answer; "
            "neither list alone gives a balanced assessment.",
            "Use this session for any 'assess the record of the Congress "
            "ministries' style question.",
            """CONGRESS MINISTRIES, 1937-39: BALANCE SHEET
ACHIEVEMENTS -> civil liberties, prisoner release, tenancy/debt reform, prohibition, education
LIMITS -> restricted finance, landlord-weighted legislatures, governor reserve powers
RESULT -> real gains, but labour unrest and agrarian distress were not fully resolved.""",
            "The Congress ministries' record combines genuine civil-"
            "liberties and agrarian reform achievements with structural "
            "limits imposed by finance, franchise and reserve powers.",
        ),
        authored_session(
            "1939 resignation and the League's Deliverance Day",
            "The Congress ministries' term ended abruptly in 1939 when "
            "unconsulted wartime belligerency triggered resignation, which "
            "the Muslim League then marked with its own separate response.",
            [
                "Congress ministries resigned between October and "
                "November 1939.",
                "The resignations protested the Viceroy's unilateral "
                "declaration of India as a party to the war.",
                "The Muslim League observed 22 December 1939 as a "
                "Deliverance Day to mark the resignations.",
                "Deliverance Day was one party's reaction, not a neutral "
                "national commemoration.",
            ],
            "Do not describe Deliverance Day as a shared or neutral "
            "national event; it was specifically the Muslim League's "
            "response.",
            "Use this session to trace the immediate political aftermath "
            "of the 1939 resignations before moving to Lahore.",
            """OCT-NOV 1939 -> Congress ministries resign (unconsulted war declaration)
22 DEC 1939 -> Muslim League observes Deliverance Day
RULE -> Deliverance Day is the League's own response, not a neutral event.""",
            "Deliverance Day was 22 December 1939, the date on which the "
            "Muslim League marked the resignation of the Congress "
            "ministries as its own distinct political response.",
        ),
        authored_session(
            "Lahore Resolution as one link, not the whole causal chain",
            "The Lahore Resolution of March 1940 followed the 1939 "
            "resignation and Deliverance Day, but it must be read as one "
            "link in a longer, multi-causal chain rather than a simple, "
            "single cause of Partition.",
            [
                "The Lahore Resolution was adopted in March 1940, several "
                "months after Deliverance Day.",
                "It followed, rather than immediately caused, the 1939 "
                "resignation-Deliverance Day sequence.",
                "Numerous later political, wartime and negotiating "
                "developments intervened between Lahore and Partition.",
                "A simple one-cause narrative from Lahore to Partition "
                "misrepresents this complexity.",
            ],
            "Never present the Lahore Resolution as directly or solely "
            "causing Partition; treat it as one link among many.",
            "Use this session to close any answer on the 1937-40 sequence "
            "with an appropriately cautious, multi-causal conclusion.",
            """1939 RESIGNATIONS -> 22 DEC 1939 DELIVERANCE DAY -> MAR 1940 LAHORE
RULE -> Lahore is one link in a chain; never a single simple cause of Partition.""",
            "The Lahore Resolution was the League's March 1940 "
            "constitutional demand that followed the 1939 resignation and "
            "Deliverance Day sequence as one link in a longer chain.",
        ),
        authored_session(
            "PYQ anchors: confirmed 2024 key and cautious 2018 residuary recall",
            "The 1935 Act's PYQ record contains one confirmed-key anchor "
            "on the federal scheme and one source-backed but key-unheld "
            "question on residuary power, and the two must be handled "
            "with different confidence levels.",
            [
                "The 2024 Prelims GS-I question on the federal scheme and "
                "reserved powers carries a confirmed official Series-A "
                "answer.",
                "The 2018 Prelims GS-I question on residuary power is "
                "source-backed to the Governor-General but has no locally "
                "held official key.",
                "The two questions should never be treated with the same "
                "confidence level in an answer.",
                "Both draw on the same reserved-subjects and residuary-"
                "power content covered earlier in this package.",
            ],
            "State the confirmed 2024 key with confidence, but state the "
            "2018 answer only as source-backed content without asserting "
            "an unverified letter.",
            "Use this session as the final PYQ-anchored revision pass "
            "before moving to the register notes.",
            """2024 PRELIMS GS-I Q62 -> federal scheme + reserved powers -> KEY CONFIRMED
2018 PRELIMS GS-I Q38 -> residuary power -> SOURCE-BACKED, NO KEY HELD
RULE -> confidence level must match the evidence held for each question.""",
            "The topic's two PYQ anchors are the confirmed-key 2024 "
            "Prelims Q62 on the federal scheme and reserved powers, and "
            "the key-unheld 2018 Prelims Q38 on residuary power.",
        ),
    ],
    "modern-indian-history-25": [
        authored_session(
            "Unconsulted belligerency: 3 September 1939",
            "The Second World War entered Indian politics through a single "
            "unilateral act: the Viceroy declared India a belligerent on "
            "3 September 1939 without consulting any Indian political "
            "leader or elected legislature.",
            [
                "The Viceroy's declaration followed Britain's own "
                "declaration of war on Germany the same day.",
                "No Indian political party, leader or elected provincial "
                "legislature was consulted before the declaration.",
                "The absence of consultation, not the war itself, became "
                "the immediate political grievance.",
                "This single unconsulted act set the tone for Congress's "
                "response through the following months.",
            ],
            "State clearly that India was made a belligerent without "
            "consultation; do not imply any Indian legislature endorsed "
            "the declaration in advance.",
            "Open any answer on the origins of wartime political conflict "
            "with this exact unconsulted-belligerency fact.",
            """3 SEP 1939 -> Britain declares war on Germany
SAME DAY -> Viceroy declares India a belligerent
NO CONSULTATION -> no Indian party, leader or legislature consulted
EFFECT -> unconsulted declaration becomes the immediate political grievance.""",
            "Unconsulted belligerency refers to the Viceroy's 3 September "
            "1939 declaration of India as a party to the war without any "
            "prior consultation of Indian political opinion.",
        ),
        authored_session(
            "Resignation to the Lahore Resolution: the connected chain",
            "The war declaration triggered a connected chain of party "
            "responses \u2014 Congress resignation, the League's "
            "Deliverance Day, and eventually the Lahore Resolution \u2014 "
            "that must be read as linked stages, not one flattened event.",
            [
                "Congress ministries resigned between October and "
                "November 1939 in protest at the unconsulted declaration.",
                "The Muslim League observed 22 December 1939 as a "
                "Deliverance Day marking the resignations.",
                "The Lahore Resolution followed in March 1940 as a later, "
                "connected but distinct development.",
                "Each stage had its own actor and date; none should be "
                "merged into the others.",
            ],
            "Keep resignation, Deliverance Day and Lahore as three "
            "separately dated stages of one connected chain, not one "
            "single event.",
            "Use this chain to link the Second World War topic back to "
            "the Congress-ministries topic without duplicating its detail.",
            """OCT-NOV 1939 -> Congress ministries resign
22 DEC 1939 -> Muslim League Deliverance Day
MAR 1940 -> Lahore Resolution
RULE -> three connected but separately dated stages, never merged into one.""",
            "The resignation-to-Lahore chain is the linked but separately "
            "dated sequence running from the 1939 Congress resignations "
            "through Deliverance Day to the March 1940 Lahore Resolution.",
        ),
        authored_session(
            "August Offer, 1940: promise and its minority-consent veto",
            "The August Offer of 8 August 1940 promised an expanded, more "
            "representative post-war constitution-making body, but "
            "attached a minority-consent condition that functioned as an "
            "effective veto and offered no immediate national government.",
            [
                "The Offer was announced on 8 August 1940 by the "
                "colonial government.",
                "It proposed a more representative body to design a "
                "post-war constitution.",
                "It promised that no future constitution would be adopted "
                "without the consent of India's minorities.",
                "It did not offer any immediate national government during "
                "the war itself.",
            ],
            "Do not describe the August Offer as granting immediate self-"
            "government; its constitution-making promise was conditional "
            "and deferred to after the war.",
            "Use the minority-consent clause to contrast the August Offer "
            "with the Cripps proposals two years later.",
            """8 AUG 1940 -> AUGUST OFFER
PROMISE -> expanded, representative body for post-war constitution-making
CONDITION -> no constitution without minority consent (effective veto)
LIMIT -> no immediate national government offered.""",
            "The August Offer was the 8 August 1940 proposal for a more "
            "representative post-war constitution-making body, "
            "conditioned on minority consent and offering no immediate "
            "national government.",
        ),
        authored_session(
            "Individual Satyagraha: sequence and its limited objective",
            "Individual Satyagraha, beginning 17 October 1940, was a "
            "deliberately narrow campaign with a named first and second "
            "satyagrahi and a limited anti-war free-speech objective, not "
            "a mass movement.",
            [
                "Vinoba Bhave offered individual civil disobedience first, "
                "on 17 October 1940.",
                "Jawaharlal Nehru followed as the second satyagrahi.",
                "Each participant was individually selected and "
                "individually courted arrest rather than acting as part "
                "of a crowd.",
                "The campaign's objective was narrowly the right to "
                "publicly oppose India's forced participation in the war.",
            ],
            "Never describe Individual Satyagraha as a mass movement; its "
            "scale, method and objective were all deliberately limited.",
            "Use this session to contrast the restrained method of "
            "Individual Satyagraha with the mass character of Quit India.",
            """17 OCT 1940 -> Vinoba Bhave, first individual satyagrahi
NEXT -> Jawaharlal Nehru, second individual satyagrahi
METHOD -> individually selected participants court arrest one by one
OBJECTIVE -> limited anti-war free-speech right, not mass civil disobedience.""",
            "Individual Satyagraha was a campaign of individually selected "
            "protesters, beginning with Vinoba Bhave on 17 October 1940, "
            "pursuing a narrow anti-war free-speech objective.",
        ),
        authored_session(
            "Cripps Mission: arrival and the March 1942 proposals",
            "Sir Stafford Cripps arrived in India in March 1942 and "
            "announced proposals offering post-war Dominion status and a "
            "constitution-making mechanism, while deferring any change "
            "during the war itself.",
            [
                "Cripps arrived in India in March 1942 amid wartime "
                "pressure following Japan's advance.",
                "His proposals were announced in late March 1942.",
                "They offered Dominion status for India after the war "
                "ended.",
                "They proposed a constitution-making body to be convened "
                "once the war concluded, not immediately.",
            ],
            "State the Cripps proposals as a post-war promise; do not "
            "describe them as offering any immediate constitutional "
            "change during the war.",
            "Use this session to open any answer evaluating the Cripps "
            "Mission's proposals.",
            """MAR 1942 -> Cripps arrives in India
LATE MAR 1942 -> proposals announced
OFFER -> Dominion status after the war + post-war constitution-making body
LIMIT -> no change to India's status during the war itself.""",
            "The Cripps proposals were the late-March 1942 offer of "
            "post-war Dominion status and a post-war constitution-making "
            "mechanism, announced after Cripps's arrival in India that "
            "same month.",
        ),
        authored_session(
            "Cripps scheme: opt-out clause and ruler-nominated princely seats",
            "Two design features of the Cripps scheme drew heavy "
            "criticism: provinces and princely states could opt out of "
            "the future union, and princely representation would come "
            "through ruler nomination, not election.",
            [
                "Any province could opt out of the new Indian union the "
                "constitution-making body might create.",
                "Any princely state could similarly not accede to that "
                "union.",
                "Princely states would be represented in the "
                "constitution-making body by members nominated by their "
                "rulers.",
                "No popularly elected process determined princely "
                "representation under this scheme.",
            ],
            "State both features precisely: opt-out applied to provinces "
            "and princely states, while princely representation was by "
            "ruler nomination, not election.",
            "Use this session for any question testing the structural "
            "objections to the Cripps proposals.",
            """CRIPPS SCHEME: TWO CONTESTED FEATURES
|-- OPT-OUT -> any province or princely state may not join the new union
`-- PRINCELY SEATS -> members nominated by rulers, not popularly elected
EFFECT -> both features fuelled objections from different political groups.""",
            "The opt-out clause let provinces and princely states decline "
            "to join the proposed post-war Indian union, while princely "
            "representation in the constitution-making body was by "
            "ruler nomination rather than election.",
        ),
        authored_session(
            "British wartime control and the absence of an immediate cabinet",
            "Alongside its post-war promises, the Cripps scheme kept "
            "defence and the general conduct of the war firmly under "
            "British control and offered no immediate responsible "
            "national cabinet.",
            [
                "Defence and the general conduct of the war remained under "
                "British control for the duration of the war.",
                "No immediate responsible national cabinet was created by "
                "the proposals.",
                "Real executive power during the war stayed with the "
                "Viceroy and British authorities.",
                "This wartime-control feature is distinct from, and "
                "additional to, the opt-out and princely-nomination "
                "features already covered.",
            ],
            "Do not conflate the wartime-control feature with the opt-out "
            "clause; they are separate objections to the same proposals.",
            "Use this session to complete the list of Cripps-scheme "
            "features before analysing why every party rejected them.",
            """CRIPPS SCHEME: WARTIME REALITY
DEFENCE + WAR CONDUCT -> remain under British control throughout the war
NATIONAL CABINET -> none created immediately
RULE -> a separate objection from the opt-out and princely-nomination features.""",
            "British wartime control refers to the Cripps scheme's "
            "retention of defence and overall war conduct under British "
            "authority, alongside its offer of no immediate responsible "
            "national cabinet.",
        ),
        authored_session(
            "Multi-party rejection: different groups, different reasons",
            "Every major political formation rejected the Cripps "
            "proposals, but for different, not identical, reasons rooted "
            "in each group's own priorities.",
            [
                "Congress objected to the deferred, conditional nature of "
                "the offer and the absence of immediate responsible "
                "government.",
                "The Muslim League objected that the scheme did not "
                "guarantee a separate Pakistan.",
                "Sikh opinion and the Hindu Mahasabha raised separate "
                "objections rooted in minority and communal concerns.",
                "Some princely opinion objected to aspects of the "
                "proposed opt-out and accession arrangements.",
            ],
            "Never present the rejection as uniform; name each group's "
            "distinct reason separately.",
            "Use this session for any 'why did the Cripps Mission fail' "
            "question that expects differentiated party reasoning.",
            """REJECTIONS OF THE CRIPPS PROPOSALS (DISTINCT REASONS)
CONGRESS -> deferred, conditional offer; no immediate responsible government
LEAGUE -> no guarantee of a separate Pakistan
SIKH / HINDU MAHASABHA -> separate minority and communal objections
PRINCELY OPINION -> concerns over opt-out and accession arrangements.""",
            "Multi-party rejection describes how Congress, the Muslim "
            "League, Sikh and Hindu Mahasabha opinion, and some princely "
            "opinion each rejected the Cripps proposals for their own "
            "distinct reasons.",
        ),
        authored_session(
            "The 'post-dated cheque' phrase and its cautious use",
            "Gandhi's remark on the Cripps proposals is best used in its "
            "shorter, better-attested form; the longer version adding a "
            "crashing bank carries uncertain provenance and should be "
            "used only with that caveat.",
            [
                "The short phrase describing the offer as a post-dated "
                "cheque is widely and reliably quoted.",
                "A longer version adding a crashing bank is commonly "
                "repeated but its exact wording and occasion are less "
                "certain.",
                "This package therefore uses only the shorter phrase as "
                "safely attested.",
                "The phrase applies specifically to the Cripps proposals, "
                "never to the earlier August Offer.",
            ],
            "Use only the shorter post-dated cheque phrase; do not present "
            "the longer crashing-bank version as certainly authentic, and "
            "never apply the phrase to the August Offer.",
            "Use this session whenever a question invites a quotation "
            "characterising the Cripps Mission's failure.",
            """GANDHI ON THE CRIPPS PROPOSALS
SHORT PHRASE -> "post-dated cheque" -> well attested, safe to use
LONGER VERSION -> adds a crashing bank -> provenance uncertain, use cautiously
RULE -> applies to Cripps only, never to the 1940 August Offer.""",
            "The post-dated cheque phrase is Gandhi's characterisation of "
            "the Cripps proposals as a promise deferred to an uncertain "
            "future, retained here only in its shorter, better-attested "
            "form.",
        ),
        authored_session(
            "Quit India's two-stage resolution: Wardha then Bombay",
            "The Quit India resolution was not adopted on a single date; "
            "it passed through two distinct stages, first at Wardha and "
            "then at Bombay, each with its own body and date.",
            [
                "The Congress Working Committee approved the resolution "
                "at Wardha on 14 July 1942.",
                "The All-India Congress Committee ratified it at Bombay on "
                "8 August 1942.",
                "Wardha and Bombay involved different Congress bodies, not "
                "the same one meeting twice.",
                "Collapsing the two dates into one loses an exam-tested "
                "distinction.",
            ],
            "Always name both the Wardha (14 July 1942) and Bombay "
            "(8 August 1942) stages separately; never state a single date "
            "for the resolution.",
            "Use this two-stage sequence to open any answer on the "
            "immediate lead-up to Quit India.",
            """14 JUL 1942, WARDHA -> Congress Working Committee approves resolution
8 AUG 1942, BOMBAY -> All-India Congress Committee ratifies resolution
RULE -> two distinct bodies and dates; never collapse into a single date.""",
            "The two-stage Quit India resolution is the sequence in which "
            "the Congress Working Committee approved the resolution at "
            "Wardha on 14 July 1942 before the All-India Congress "
            "Committee ratified it at Bombay on 8 August 1942.",
        ),
        authored_session(
            "Operation Zero Hour: arrests the following morning",
            "The government's mass-arrest operation, referred to as "
            "Operation Zero Hour, began early on 9 August 1942, within hours "
            "of the 8 August Bombay ratification and on the following "
            "calendar day.",
            [
                "Arrests of senior Congress leaders began in the early "
                "hours of 9 August 1942.",
                "This was the following morning and calendar day after the "
                "AICC's 8 August 1942 Bombay ratification, not a full 24 "
                "hours later.",
                "The government acted pre-emptively to decapitate Congress "
                "leadership before mass mobilisation could organise.",
                "The sequence, rather than a claimed 24-hour interval, is the "
                "frequently tested precise detail.",
            ],
            "State the arrests as beginning in the early hours of 9 August "
            "1942, the following morning after the 8 August resolution.",
            "Use this exact following-morning sequence whenever a question tests the "
            "precise sequence around the Quit India resolution's passage.",
            """8 AUG 1942 -> AICC ratifies Quit India resolution at Bombay
9 AUG 1942 (early hours) -> Operation Zero Hour: mass arrests begin
INTERVAL -> within hours, on the following calendar day
RULE -> preserve the sequence without claiming a full 24-hour gap.""",
            "Operation Zero Hour was the government's mass-arrest "
            "operation against Congress leadership, beginning in the "
            "early hours of 9 August 1942, the morning after the Bombay "
            "resolution.",
        ),
        authored_session(
            "Do or Die, Gowalia Tank and the underground resistance",
            "After the leadership's arrest, the movement's public symbols "
            "and its underground continuation both trace to specific "
            "named individuals rather than an anonymous crowd.",
            [
                "Gandhi's 8 August 1942 call to 'Do or Die' set the "
                "movement's defiant tone before his own arrest.",
                "Aruna Asaf Ali is associated with hoisting the Congress "
                "flag at Gowalia Tank in Bombay after the leaders' "
                "arrest.",
                "Usha Mehta ran secret Congress Radio broadcasts to keep "
                "the movement's message alive underground.",
                "Jayaprakash Narayan and Ram Manohar Lohia organised "
                "clandestine resistance networks after most senior "
                "leaders were arrested.",
            ],
            "Name each individual precisely \u2014 Gandhi, Aruna Asaf Ali, "
            "Usha Mehta, Jayaprakash Narayan, Ram Manohar Lohia \u2014 "
            "rather than describing the underground movement generically.",
            "Use these named figures whenever a question asks for "
            "specific individuals associated with Quit India's leadership "
            "vacuum.",
            """8 AUG 1942 -> Gandhi's "Do or Die" call, before his arrest
GOWALIA TANK, BOMBAY -> Aruna Asaf Ali hoists the Congress flag
UNDERGROUND -> Usha Mehta's secret Congress Radio
UNDERGROUND -> Jayaprakash Narayan and Ram Manohar Lohia organise resistance.""",
            "The underground Quit India leadership refers to figures such "
            "as Aruna Asaf Ali at Gowalia Tank, Usha Mehta's Congress "
            "Radio, and Jayaprakash Narayan with Ram Manohar Lohia, who "
            "sustained the movement after the arrests.",
        ),
        authored_session(
            "Parallel national governments: Ballia, Tamluk and Satara",
            "In three separate localities, Quit India produced short-lived "
            "parallel national governments, each with its own name and "
            "its own distinct duration.",
            [
                "A parallel government was declared at Ballia.",
                "At Tamluk in Midnapore, the parallel government was known "
                "as the Jatiya Sarkar.",
                "At Satara, the parallel government was known as the "
                "Prati Sarkar.",
                "Each of the three survived for a different length of "
                "time before being suppressed or wound down.",
            ],
            "Name each parallel government's location and, where named, "
            "its title; do not treat all three as identical in duration or "
            "character.",
            "Use this session for any question naming specific parallel-"
            "government sites during Quit India.",
            """PARALLEL NATIONAL GOVERNMENTS DURING QUIT INDIA
BALLIA -> parallel government declared
TAMLUK (MIDNAPORE) -> Jatiya Sarkar
SATARA -> Prati Sarkar
RULE -> three distinct sites, names and durations; never treat as identical.""",
            "Parallel national governments were locally declared "
            "alternative administrations during Quit India, including "
            "Ballia, the Jatiya Sarkar at Tamluk in Midnapore, and the "
            "Prati Sarkar at Satara.",
        ),
        authored_session(
            "Social base, repression caution and political alignments",
            "Quit India drew a genuinely broad social base and regionally "
            "varied intensity, faced harsh repression that must be stated "
            "cautiously, and saw distinctly different political groups "
            "align in different ways.",
            [
                "Students, workers and peasants all participated, with "
                "intensity varying by region.",
                "The movement combined sabotage of communication lines "
                "with Congress's own official non-violent creed.",
                "Repression was harsh, but this package avoids stating "
                "unsupported exact casualty or arrest totals.",
                "The Muslim League stayed aloof from or opposed the "
                "movement, the Communist Party of India followed a "
                "People's War line after June 1941, and the Hindu "
                "Mahasabha and many princely rulers remained distant.",
            ],
            "Never assert a specific unqualified casualty or arrest "
            "figure; state repression as harsh without an invented total.",
            "Use this session to answer any question on the movement's "
            "social composition, methods or the stance of non-Congress "
            "political groups.",
            """QUIT INDIA: BASE, METHOD AND ALIGNMENTS
BASE -> students, workers, peasants; regionally variable intensity
METHOD -> sabotage alongside Congress's own non-violent creed
REPRESSION -> harsh; no unsupported exact casualty/arrest total stated
ALIGNMENTS -> League aloof/opposed; CPI People's War line; Mahasabha/princes distant.""",
            "The movement's social base and political alignments refer to "
            "its broad but regionally variable student-worker-peasant "
            "participation alongside the distinct, non-uniform stances of "
            "the League, the CPI, the Hindu Mahasabha and princely rulers.",
        ),
        authored_session(
            "Results of Quit India and the 2024 Mains anchor",
            "Quit India was suppressed within months, and it did not by "
            "itself win independence, but it demonstrated the depth of "
            "popular anti-colonial sentiment \u2014 exactly the balance a "
            "verified 2024 Mains question asks candidates to strike.",
            [
                "The government suppressed the movement within months "
                "through mass arrests and force.",
                "The movement did not by itself secure India's "
                "independence.",
                "It nonetheless demonstrated the depth and breadth of "
                "popular anti-colonial sentiment across regions and "
                "social groups.",
                "A verified 2024 Mains GS-I question asks what events led "
                "to the Quit India Movement and what its results were.",
            ],
            "State the results with both halves together: swift "
            "suppression and no immediate independence, alongside lasting "
            "demonstration of popular sentiment.",
            "Use this session as the closing anchor for any full narrative "
            "answer on the origins and results of Quit India.",
            """QUIT INDIA: RESULTS
IMMEDIATE -> suppressed within months by mass arrests and force
NOT ACHIEVED -> independence was not secured by the movement alone
LASTING SIGNIFICANCE -> demonstrated depth of popular anti-colonial sentiment
ANCHOR -> 2024 Mains GS-I Q3 asks for events leading to Quit India and its results.""",
            "The results of Quit India combine its swift government "
            "suppression within months with its lasting demonstration of "
            "popular anti-colonial sentiment, without the movement alone "
            "securing independence.",
        ),
    ],
}


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-24": [
        (
            "Constitutional lineage, Simon to royal assent",
            "timeline",
            """SIMON REPORT (1930) -> RTCs (1930-32) -> WHITE PAPER (1933)
-> JOINT SELECT COMMITTEE (1934) -> ROYAL ASSENT (1935)
INPUTS -> commission evidence + constitutional negotiation + parliamentary review
RULE -> five ordered stages; none may be skipped or reordered.""",
            ["Constitutional lineage: from Simon to royal assent"],
        ),
        (
            "Two halves of the Act, federation never in force",
            "causal-flow",
            """FEDERAL HALF -> All-India Federation + central dyarchy -> NEVER IN FORCE
PROVINCIAL HALF -> provincial autonomy, dyarchy abolished -> OPERATED 1937
ACCESSION FAILURE -> princely threshold remained unmet
RULE -> the federation's non-operation must never be blurred with the record.""",
            ["Two halves of the Act and the federation that never operated"],
        ),
        (
            "Dyarchy: abolished provincially, unrealised centrally",
            "comparison",
            """1919 ACT -> provincial dyarchy (reserved + transferred subjects)
1935 ACT -> provincial dyarchy ABOLISHED -> provincial autonomy begins
            PROVINCIAL MINISTERS -> responsible for all provincial subjects and departments
CENTRAL DYARCHY -> proposed only for the federal centre -> never operated.""",
            ["Provincial dyarchy abolished, not merely modified"],
        ),
        (
            "Governor's powers versus Section 93",
            "comparison",
            """DISCRETIONARY / SPECIAL RESPONSIBILITY -> continuous standing power
SECTION 93 -> emergency takeover only on breakdown of machinery
NORMAL AUTONOMY -> ministers govern while reserve powers remain in the background
1939 RESIGNATION -> caused by war declaration, not Section 93 action.""",
            [
                "Governor's discretionary powers and special responsibilities",
                "Section 93: the background emergency reserve power",
            ],
        ),
        (
            "Reserved subjects and residuary power",
            "institution-map",
            """RESERVED TO GOVERNOR-GENERAL
|-- Defence
|-- External Affairs
|-- Ecclesiastical Affairs
`-- Tribal Areas
RESIDUARY POWER -> also with the Governor-General, not any legislature.""",
            ["Reserved central subjects and residuary power"],
        ),
        (
            "Franchise reform as a qualified range",
            "data-table",
            """ELECTORATE -> roughly 30 to 35 million voters (source-dependent)
SHARE OF POPULATION -> roughly 10 to 14 per cent (denominator-dependent)
QUALIFICATIONS -> property, tax, income and education restrictions remained
RULE -> state as a qualified range; still short of universal adult franchise.""",
            ["Franchise reform as a qualified range, not one exact figure"],
        ),
        (
            "RBI Act 1934 versus the 1935 Act",
            "comparison",
            """1934 -> Reserve Bank of India Act -> RBI founded
1935 -> Government of India Act -> separate constitutional statute
1937 -> provincial constitutional provisions begin operating
TRAP -> RBI's origin is the 1934 Act, never the 1935 Act.""",
            ["RBI Act 1934 versus the Government of India Act 1935"],
        ),
        (
            "Federal Court and Burma: parallel 1937 tracks",
            "timeline",
            """1935 ACT PROVISIONS -> two parallel 1937 developments
FEDERAL COURT OF INDIA -> begins functioning, 1937
BURMA SEPARATION -> takes effect, 1937
RULE -> parallel, not sequential or causally connected.""",
            ["Federal Court and Burma separation: parallel 1937 developments"],
        ),
        (
            "1937 election and ministry timing, NWFP and Assam",
            "timeline",
            """FEB 1937 -> elections; Congress largest in most provinces
JUL 1937 -> six ministries: Madras, Bombay, UP, Bihar, CP and Orissa
LATER 1937 -> NWFP becomes the seventh Congress ministry
1938 -> Assam becomes the eighth after coalition arrangements break down
RULE -> eight is the eventual, not the simultaneous, total.""",
            [
                "1937 elections, ministry timing, NWFP and Assam",
            ],
        ),
        (
            "Office-acceptance debate",
            "balance-sheet",
            """FOR -> reformist and organisational opportunity within autonomy
AGAINST -> risk of legitimising a rejected constitutional structure
SAFEGUARD TEST -> Congress sought assurances against routine governor interference
OUTCOME -> conditional acceptance, watching for governor interference.""",
            ["The 1937 office-acceptance debate inside Congress"],
        ),
        (
            "Ministries' achievements and structural limits",
            "balance-sheet",
            """ACHIEVEMENTS -> civil liberties, prisoner release, tenancy/debt reform
ACHIEVEMENTS -> prohibition, primary education
LIMITS -> restricted finance, landlord legislatures, governor reserve powers
RESULT -> real gains; labour unrest and agrarian distress not fully resolved.""",
            ["Achievements and structural limits of the Congress ministries"],
        ),
        (
            "1939 resignation to Lahore, and the PYQ anchors",
            "timeline",
            """OCT-NOV 1939 -> ministries resign (unconsulted war declaration)
22 DEC 1939 -> League Deliverance Day
MAR 1940 -> Lahore Resolution -> one link in a chain, not sole cause
PYQ -> 2024 Q62 key confirmed; 2018 Q38 source-backed, no key held.""",
            [
                "1939 resignation and the League's Deliverance Day",
                "Lahore Resolution as one link, not the whole causal chain",
                "PYQ anchors: confirmed 2024 key and cautious 2018 residuary recall",
            ],
        ),
    ],
    "modern-indian-history-25": [
        (
            "Unconsulted belligerency and the response chain",
            "causal-flow",
            """3 SEP 1939 -> Viceroy declares India a belligerent, no consultation
OCT-NOV 1939 -> Congress ministries resign
22 DEC 1939 -> League Deliverance Day -> MAR 1940 -> Lahore Resolution
RULE -> three connected but separately dated stages.""",
            [
                "Unconsulted belligerency: 3 September 1939",
                "Resignation to the Lahore Resolution: the connected chain",
            ],
        ),
        (
            "August Offer: promise and minority-consent veto",
            "comparison",
            """8 AUG 1940 -> AUGUST OFFER
PROMISE -> expanded, representative post-war constitution-making body
CONDITION -> no constitution without minority consent (effective veto)
LIMIT -> no immediate national government offered.""",
            ["August Offer, 1940: promise and its minority-consent veto"],
        ),
        (
            "Individual Satyagraha: sequence and limited objective",
            "timeline",
            """17 OCT 1940 -> Vinoba Bhave, first satyagrahi
NEXT -> Jawaharlal Nehru, second satyagrahi
METHOD -> selected individuals publicly assert the right to oppose the war
OBJECTIVE -> limited anti-war free-speech right, not mass civil disobedience.""",
            ["Individual Satyagraha: sequence and its limited objective"],
        ),
        (
            "Cripps arrival and the March 1942 proposals",
            "timeline",
            """MAR 1942 -> Cripps arrives in India
LATE MAR 1942 -> proposals announced
OFFER -> Dominion status after the war + post-war constitution-making body
LIMIT -> no change to India's status during the war itself.""",
            ["Cripps Mission: arrival and the March 1942 proposals"],
        ),
        (
            "Cripps scheme: opt-out and princely nomination",
            "institution-map",
            """OPT-OUT -> any province or princely state may not join the new union
PRINCELY SEATS -> members nominated by rulers, not popularly elected
UNION DESIGN -> accession would be negotiated after the war
EFFECT -> both features fuelled objections from different political groups.""",
            ["Cripps scheme: opt-out clause and ruler-nominated princely seats"],
        ),
        (
            "British wartime control and no immediate cabinet",
            "comparison",
            """DEFENCE + WAR CONDUCT -> remain under British control throughout the war
NATIONAL CABINET -> none created immediately
EXECUTIVE GAP -> Indian leaders receive no present control over the wartime state
RULE -> a separate objection from the opt-out and princely-nomination features.""",
            ["British wartime control and the absence of an immediate cabinet"],
        ),
        (
            "Multi-party rejection of the Cripps proposals",
            "balance-sheet",
            """CONGRESS -> deferred, conditional offer; no immediate responsible government
LEAGUE -> no guarantee of a separate Pakistan
SIKH / HINDU MAHASABHA -> separate minority and communal objections
PRINCELY OPINION -> concerns over opt-out and accession arrangements.""",
            ["Multi-party rejection: different groups, different reasons"],
        ),
        (
            "Post-dated cheque phrase, cautious provenance",
            "comparison",
            """SHORT PHRASE -> "post-dated cheque" -> well attested, safe to use
LONGER VERSION -> adds a crashing bank -> provenance uncertain
REFERENCE -> the criticism concerns deferred Cripps promises
RULE -> applies to Cripps only, never to the 1940 August Offer.""",
            ["The 'post-dated cheque' phrase and its cautious use"],
        ),
        (
            "Quit India's two-stage resolution",
            "timeline",
            """14 JUL 1942, WARDHA -> Congress Working Committee approves resolution
8 AUG 1942, BOMBAY -> All-India Congress Committee ratifies resolution
POLITICAL MOVE -> committee draft becomes the national organisation's mandate
RULE -> two distinct bodies and dates; never a single date.""",
            ["Quit India's two-stage resolution: Wardha then Bombay"],
        ),
        (
            "Operation Zero Hour, the following morning after Bombay",
            "timeline",
            """8 AUG 1942 -> AICC ratifies Quit India resolution at Bombay
9 AUG 1942 (early hours) -> Operation Zero Hour: mass arrests begin
CONSEQUENCE -> central leadership is removed before an organised campaign develops
RULE -> within hours, on the following calendar day; not a full 24-hour gap.""",
            ["Operation Zero Hour: arrests the following morning"],
        ),
        (
            "Do or Die, Gowalia Tank and underground resistance",
            "institution-map",
            """8 AUG 1942 -> Gandhi's "Do or Die" call, before his arrest
GOWALIA TANK, BOMBAY -> Aruna Asaf Ali hoists the Congress flag
UNDERGROUND -> Usha Mehta's Congress Radio
UNDERGROUND -> Jayaprakash Narayan and Ram Manohar Lohia organise resistance.""",
            ["Do or Die, Gowalia Tank and the underground resistance"],
        ),
        (
            "Parallel governments, social base and results",
            "balance-sheet",
            """PARALLEL GOVERNMENTS -> Ballia; Jatiya Sarkar (Tamluk); Prati Sarkar (Satara)
BASE -> students, workers, peasants; regionally variable intensity
ALIGNMENTS -> League aloof/opposed; CPI People's War line; Mahasabha/princes distant
RESULTS -> suppressed within months; no solo independence; lasting sentiment shown.""",
            [
                "Parallel national governments: Ballia, Tamluk and Satara",
                "Social base, repression caution and political alignments",
                "Results of Quit India and the 2024 Mains anchor",
            ],
        ),
    ],
}


TOPIC_CHRONOLOGY = {
    "modern-indian-history-24": [
        "1930 report",
        "1933 White Paper",
        "1934 report",
        "royal assent in 1935",
        "Reserve Bank of India Act, 1934",
        "began functioning in 1937",
        "took effect in 1937",
        "February 1937",
        "between October and November 1939",
        "22 December 1939",
        "March 1940",
    ],
    "modern-indian-history-25": [
        "3 September 1939",
        "between October and November 1939",
        "22 December 1939",
        "March 1940",
        "8 August 1940",
        "17 October 1940",
        "March 1942",
        "late March 1942",
        "14 July 1942",
        "8 August 1942",
        "began early on 9 August 1942",
    ],
}

FORBIDDEN_TOPIC_PHRASES = {
    "modern-indian-history-24": [
        "All-India Federation came into force",
        "federation began functioning",
        "central dyarchy operated",
        "Section 93 caused the resignation",
        "Reserve Bank of India was established under the Government of India "
        "Act, 1935",
        "Congress formed ministries in eight provinces immediately",
        "Lahore Resolution directly caused Partition",
        "Deliverance Day was a neutral national event",
        "franchise was exactly",
    ],
    "modern-indian-history-25": [
        "India was consulted before",
        "August Offer gave an immediate national government",
        "Individual Satyagraha was a mass movement",
        "Cripps proposals gave immediate self-government",
        "every party rejected the Cripps proposals for the same reason",
        "Quit India resolution was adopted on a single date",
        "arrests began on the same day as the Bombay resolution",
        "one full day after ratification",
        "Quit India alone won India's independence",
        "official parliamentary tribute",
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
        "scope": "Modern Indian History learner-v2 Topics 24-25",
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
                raise ValueError(f"{key}: chronology marker missing/out of order: {marker}")
        cursor = found
    for phrase in FORBIDDEN_TOPIC_PHRASES[key]:
        if phrase.casefold() in markdown.casefold():
                raise ValueError(f"{key}: forbidden factual formulation found: {phrase}")

    if key == "modern-indian-history-24":
        strict = [
                "never came into force",
                "abolished",
                "residuary",
                "Ecclesiastical Affairs",
                "Tribal Areas",
                "roughly 30 to 35 million",
                "roughly 10 to 14 per cent",
                "Reserve Bank of India Act, 1934",
                "no answer letter is asserted",
                "structurally analogous",
                "not cited as evidence that the Court invoked",
        ]
    else:
        strict = [
                "without consulting",
                "minority consent",
                "not a mass movement",
                "opt out",
                "nominated by their rulers",
                "post-dated cheque",
                "Wardha on 14 July 1942",
                "Bombay on 8 August 1942",
                "following calendar day",
                "did not by itself win India's independence",
                "could not be independently verified",
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
