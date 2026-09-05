"""Build Modern Indian History learner-v2 Topics 34-35.

This authoring-only generator writes complete reusable Markdown, solved
workbooks, manual ASCII and graphical specifications, and tracker-free
generation-one manifests for the succession from Shastri to Indira Gandhi
(1964-73) and for the JP Movement and the Emergency (1973-77). It
deliberately does not render PDFs, update the tracker, regenerate indexes,
finalize generations, or publish packages.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base
import generate_modern_history_32_33_sequential as previous


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
    / "modern-indian-history-34-35-2026-08-31-sequential.json"
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
            KNOWLEDGE.parent
            / "_PYQ-ROUTING-PRELIMS-2018-2023.md",
            KNOWLEDGE.parent
            / "_PYQ-ROUTING-PRELIMS-2024-2025.md",
        ]
    )
)
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]
OFFICIAL_QUESTION_SOURCES = list(base.OFFICIAL_QUESTION_SOURCES)


TOPICS = [
    base.topic(
        34,
        "From Shastri to Indira Gandhi, 1964\u201373",
        "34_From-Shastri-to-Indira-1964-73.md",
        "34_From-Shastri-to-Indira-1964-73.md",
        "34_From-Shastri-to-Indira-Gandhi-1964-73_Complete-Topic-Package.md",
        [
            "basic/33_Party-Politics-1947-67-Congress-System-and-Opposition.md",
            "basic/35_The-JP-Movement-and-the-Emergency.md",
            "basic/38_Economy-Land-Society-and-State-A-Post-Independence-"
            "Synthesis.md",
            "33_Party-Politics-1947-67-Congress-System-and-Opposition_"
            "Complete-Topic-Package.md",
        ],
        [],
        "No verified live current-affairs item is pegged to this topic. The "
        "owner's own Current-link section frames bank nationalisation, "
        "defections and Centre-State tension as recurring analytical themes "
        "rather than as a dated news event, and that bounded, unattributed "
        "framing is preserved here rather than inventing a specific live "
        "source or date.",
        "The Basic and Advanced owner Markdown for this topic were "
        "reconciled against each other and against the folder's shared "
        "post-independence OCR source, Bipan Chandra, Mridula Mukherjee and "
        "Aditya Mukherjee, *India After Independence, 1947\u20132000*. Every "
        "date, name and institution used below already carries the owners' "
        "own \u2705 (source-backed) or \u26a0\ufe0f (inference) tagging, and "
        "that tagging is preserved rather than re-verified page by page "
        "against the raw PDF in this authoring pass.",
        "One Prelims demand is routed to this owner in the local ledgers "
        "(`_PYQ-ROUTING-PRELIMS-2018-2023.md`): the 2019 Prelims GS-I Q48 "
        "coal-sector-nationalisation-status demand, which the owner itself "
        "flags as having no supporting content in any modern-history source "
        "book held in this repository; it is embedded verbatim below with "
        "no option, answer or invented statute name, and this authoring "
        "pass preserves that explicit unsupported-gap caution rather than "
        "fabricating a resolution. No Mains demand in the local 2018-2025 "
        "ledgers is routed to this owner.",
        [
            (
                "Shastri becomes Prime Minister, June 1964",
                "Lal Bahadur Shastri became Prime Minister in June 1964 "
                "after Jawaharlal Nehru's death, and he led India through "
                "the 1965 India-Pakistan war, signed the Tashkent Declaration "
                "with Ayub Khan on 10 January 1966 and died at Tashkent in "
                "the early hours of 11 January.",
            ),
            (
                "Indira Gandhi elected Prime Minister, January 1966",
                "Indira Gandhi was elected Prime Minister in January 1966, "
                "defeating Morarji Desai by 355 votes to 169, and she was "
                "initially backed by the Congress bosses known as the "
                "'Syndicate', who expected to control her from behind the "
                "scenes.",
            ),
            (
                "The rupee devaluation, June 1966",
                "The rupee was devalued by about 35.5 per cent in June "
                "1966, a politically costly step that followed 1965-war "
                "expenditure, successive harvest failures and India's "
                "dependence on external food aid.",
            ),
            (
                "The Prime Minister's Secretariat gains weight under "
                "Shastri",
                "Under Shastri the Prime Minister's Secretariat, or PMO, "
                "gained administrative weight, an early sign of executive "
                "centralisation inside the government that deepened further "
                "under Indira Gandhi.",
            ),
            (
                "The 1967 general election: the end of easy dominance",
                "The fourth general election of 1967 slashed the Congress's "
                "Lok Sabha majority and cost it power in eight states, "
                "producing Samyukta Vidhayak Dal coalition governments and "
                "mass floor-crossing that contemporaries nicknamed 'Aya Ram "
                "Gaya Ram'.",
            ),
            (
                "The 1969 Congress split",
                "In 1969 Indira Gandhi split the Congress into Congress (R) "
                "and Congress (O), defeating the Syndicate, in a rupture "
                "that followed directly from the presidential contest and "
                "the nationalisation of 14 banks the same year.",
            ),
            (
                "The Supreme Court's 1970 rulings against the executive",
                "The Supreme Court struck down the government's first bank-"
                "nationalisation order and its order derecognising the "
                "princely rulers' privy purses in 1970, forcing the "
                "government to re-enact both measures through fresh "
                "legislation and constitutional amendment.",
            ),
            (
                "V.V. Giri elected President, 1969",
                "V.V. Giri won the 1969 presidential election as Indira "
                "Gandhi's candidate, a contest whose outcome confirmed that "
                "most Congress MPs and the AICC had sided with her against "
                "the Syndicate.",
            ),
            (
                "Privy purses abolished, 1971",
                "The privy purses of former princely rulers were formally "
                "abolished in 1971 through the 26th Constitutional "
                "Amendment, after the Supreme Court's 1970 ruling had struck "
                "down the government's original derecognition order.",
            ),
            (
                "The 1971 election and Garibi Hatao",
                "In the 1971 general election Congress (R) won 352 of 518 "
                "seats campaigning on the slogan 'Garibi Hatao', a national "
                "plebiscite that delinked the Lok Sabha verdict from state-"
                "level Congress organisation for the first time.",
            ),
            (
                "The 1971 Bangladesh war",
                "The 1971 Bangladesh war, arising from the crisis in East "
                "Pakistan and the refugee influx into India, ended in a "
                "decisive Indian victory and the creation of Bangladesh, "
                "making Indira Gandhi's authority unassailable at home.",
            ),
            (
                "Pokhran-I, May 1974",
                "India conducted its first nuclear test, Pokhran-I, in May "
                "1974, officially described at the time as a 'peaceful "
                "nuclear explosion' rather than a weapons test.",
            ),
            (
                "Comparing 1965 and 1971",
                "The 1965 war originated in Pakistani infiltration into "
                "Kashmir and ended militarily inconclusively at the "
                "Tashkent Declaration, while the 1971 war originated in the "
                "East Pakistan crisis and ended in a decisive Indian "
                "victory that created Bangladesh, a contrast that "
                "transformed India's regional standing.",
            ),
            (
                "De-institutionalisation: the hidden cost",
                "The same populist and organisational techniques that made "
                "Indira Gandhi dominant also personalised authority, split "
                "and weakened the Congress organisation, and eroded the "
                "internal checks that had once contained factional "
                "conflict, a de-institutionalisation that is the structural "
                "background to the 1973-75 crisis.",
            ),
            (
                "The mid-1960s crisis behind the devaluation",
                "The devaluation of June 1966 followed a convergence of "
                "1965-war expenditure, successive harvest failures and "
                "dependence on external food aid, and it produced a "
                "durable Indian aversion to externally pressed economic "
                "adjustment that lasted until 1991.",
            ),
            (
                "1967's three structural consequences",
                "The 1967 election's structural consequences were "
                "threefold: coalition government became normal in the "
                "states, defection became a standard political instrument "
                "eventually addressed by the 1985 Anti-Defection Act, and "
                "the Congress central leadership lost the state-level "
                "organisational machine that had underwritten its earlier "
                "dominance.",
            ),
            (
                "The institutionalised left-right cleavage after 1969",
                "The 1969 Congress split institutionalised a left-of-centre "
                "versus right-of-centre cleavage inside what had been a "
                "single dominant party, with most Members of Parliament and "
                "the AICC siding with Indira Gandhi's Congress (R).",
            ),
            (
                "The coal-sector nationalisation gap, 2019",
                "The 2019 Prelims GS-I Q48 demand on the status of coal-"
                "sector nationalisation in independent India has no "
                "supporting content in any modern-history source book held "
                "in this repository, and no nationalisation year or statute "
                "name for the coal sector may be stated from memory in this "
                "topic.",
            ),
            (
                "Resilience and cost: two historiographical readings",
                "Bipan Chandra reads Indira Gandhi's leftward turn "
                "sympathetically as a genuine, if flawed, attempt to give "
                "the poor a stake, while conceding the cost of "
                "de-institutionalisation; rival institutionalist readings "
                "foreground the erosion of party democracy that the same "
                "turn produced.",
            ),
            (
                "Continuity of numbers, discontinuity of organisation",
                "Despite the 1969 split, Congress (R) retained a "
                "comfortable Lok Sabha majority because most sitting "
                "Members of Parliament crossed over with Indira Gandhi, a "
                "numerical continuity that concealed how deeply the "
                "party's internal democracy and organisational discipline "
                "had already eroded.",
            ),
        ],
        [
            "Shastri died at Tashkent in January 1966, not in India; do "
            "not relocate his death.",
            "Bank nationalisation occurred in 1969, not 1971; privy-purse "
            "abolition occurred in 1971, not 1969; keep the two years "
            "apart.",
            "The 1967 election did not give Congress a comfortable "
            "majority; its majority was slashed and it lost eight states.",
            "Pokhran-I (May 1974) was styled a 'peaceful nuclear "
            "explosion', not a declared weapons test, and it belongs to "
            "1974, not the 1960s.",
            "The Congress system began cracking in 1967; the 1969 split "
            "completed rather than began the rupture.",
            "Bank nationalisation did not go unchallenged: the Supreme "
            "Court struck down the government's first order in 1970 before "
            "it was re-enacted.",
            "The 1971 mandate was a national plebiscite delinked from "
            "state politics, not simply a state-level verdict.",
            "Personalised leadership after 1969 de-institutionalised the "
            "Congress party; it did not strengthen party institutions.",
            "Indira Gandhi defeated Morarji Desai 355 votes to 169 in "
            "1966; do not reverse the figures or the year.",
            "The June 1966 devaluation followed war expenditure and "
            "harvest failures; it was not an isolated policy choice made "
            "in normal conditions.",
            "The 1967 election cost Congress power in eight states, a "
            "specific figure that must not be altered or approximated.",
            "V.V. Giri's 1969 presidential victory reflected support for "
            "Indira Gandhi inside Congress; it did not resolve the "
            "Syndicate dispute in the Syndicate's favour.",
            "Coal-sector nationalisation facts must never be stated from "
            "memory in this topic; the local sources do not support any "
            "year, statute or sequence for it.",
        ],
        [
            (
                10,
                "Explain how the successions of 1964 and 1966 demonstrated "
                "the resilience of Indian democracy.",
                "Two unplanned successions settled within days by party "
                "election, in the middle of a war and a food crisis, show "
                "that India's constitutional processes for replacing a "
                "leader had already been institutionalised by the mid-"
                "1960s.",
                [0, 1, 2],
            ),
            (
                10,
                "Distinguish the origins and outcomes of the 1965 and 1971 "
                "wars.",
                "The 1965 war arose from infiltration into Kashmir and "
                "ended inconclusively at Tashkent, while the 1971 war arose "
                "from the East Pakistan crisis and ended decisively with "
                "the creation of Bangladesh.",
                [1, 11, 12],
            ),
            (
                15,
                "Analyse how Indira Gandhi used the measures of 1969-71 to "
                "consolidate power over the Congress party.",
                "Bank nationalisation, the Giri presidency, privy-purse "
                "abolition and the Garibi Hatao mandate together converted "
                "an intra-party contest into unassailable national "
                "authority.",
                [5, 7, 8, 9],
            ),
            (
                15,
                "Assess the significance of the 1967 general election for "
                "the subsequent development of the Indian party system.",
                "The 1967 result normalised coalition government, made "
                "defection a standard instrument and stripped the Congress "
                "centre of the state-level machine that had underwritten "
                "its dominance.",
                [4, 15, 16],
            ),
            (
                20,
                "'Indira Gandhi's consolidation of power between 1966 and "
                "1971 rested on the erosion of institutions as much as on "
                "popular mandate.' Evaluate.",
                "Executive centralisation from Shastri's PMO onward, the "
                "1969 split, privy-purse abolition and the de-"
                "institutionalisation this produced show that mandate and "
                "institutional erosion advanced together rather than as "
                "alternatives.",
                [3, 5, 8, 13, 16],
            ),
            (
                20,
                "Trace India's political and economic trajectory from "
                "Lal Bahadur Shastri's accession in 1964 to the Pokhran "
                "test of 1974, and assess the costs of this decade's "
                "consolidation of power.",
                "A decade that opened with two successions and a "
                "devaluation closed with a nuclear test and unassailable "
                "personal authority, but the same decade's techniques left "
                "the Congress organisationally hollow, the structural "
                "background to the 1973-75 crisis.",
                [0, 2, 4, 5, 9, 11, 13],
            ),
        ],
        [],
        [
            "Lal Bahadur Shastri",
            "Tashkent Declaration",
            "Morarji Desai",
            "bank nationalisation",
            "privy purses",
            "Garibi Hatao",
            "Bangladesh war",
            "Pokhran-I",
            "Congress split",
        ],
    ),
    base.topic(
        35,
        "The JP Movement & the Emergency",
        "35_The-JP-Movement-and-the-Emergency.md",
        "35_The-JP-Movement-and-the-Emergency.md",
        "35_The-JP-Movement-and-the-Emergency_Complete-Topic-Package.md",
        [
            "basic/34_From-Shastri-to-Indira-1964-73.md",
            "basic/36_Janata-Interregnum-Indiras-Return-and-Regional-"
            "Crises.md",
            "34_From-Shastri-to-Indira-Gandhi-1964-73_Complete-Topic-"
            "Package.md",
        ],
        [],
        "One verified live current-affairs item is preserved for this "
        "topic, exactly as recorded by the owner: on 25 June 2025 the "
        "Union Cabinet adopted an official resolution commemorating fifty "
        "years since the Emergency, honouring resistance to it and "
        "reaffirming constitutional democracy (PIB, PRID 2139543); the "
        "owner does not record a URL for this press release, so none is "
        "invented here, and the bounded wording and PRID citation are "
        "preserved rather than expanded with unverified detail.",
        "The Basic and Advanced owner Markdown for this topic were "
        "reconciled against each other and against the folder's shared "
        "post-independence OCR source, Bipan Chandra, Mridula Mukherjee and "
        "Aditya Mukherjee, *India After Independence, 1947\u20132000*. Every "
        "date, name and institution used below already carries the owners' "
        "own \u2705 (source-backed) or \u26a0\ufe0f (inference) tagging, and "
        "that tagging is preserved rather than re-verified page by page "
        "against the raw PDF in this authoring pass.",
        "No Prelims or Mains demand in the local 2018-2026 routing ledgers "
        "is routed to this owner; this is a transparent zero-direct-PYQ "
        "audit rather than an omission, and the owner's own basic and "
        "advanced files carry no 'PYQ Integration' section to integrate.",
        [
            (
                "The 1972-73 economic crisis",
                "By 1973 two failed monsoons, drought and the 1973 oil "
                "shock had produced a price rise of about 22 per cent over "
                "1972-73, deepening inflation, unemployment and food "
                "scarcity that eroded Indira Gandhi's popularity after her "
                "1971 landslide.",
            ),
            (
                "Nav Nirman, Gujarat, January 1974",
                "The Nav Nirman student agitation began in Gujarat in "
                "January 1974 over rising prices and corruption, becoming "
                "the first of the student movements that grew into a "
                "nationwide protest.",
            ),
            (
                "The Bihar movement and JP's Total Revolution, March 1974",
                "The Bihar student movement erupted in March 1974 and "
                "Jayaprakash Narayan, known as JP, took its leadership, "
                "calling for 'Total Revolution' or Sampoorna Kranti against "
                "corruption and misgovernance.",
            ),
            (
                "The all-India railway strike, May 1974",
                "An all-India railway strike lasting 22 days took place in "
                "May 1974, directly challenging the government and adding "
                "an economic dimension to the political crisis building "
                "around JP's movement.",
            ),
            (
                "The Allahabad High Court judgment, 12 June 1975",
                "On 12 June 1975 the Allahabad High Court, in a judgment by "
                "Justice Jagmohanlal Sinha on Raj Narain's petition, set "
                "aside Indira Gandhi's 1971 election on grounds of electoral "
                "malpractice.",
            ),
            (
                "The Supreme Court's conditional stay, 24 June 1975",
                "On 24 June 1975 the Supreme Court, through Justice V.R. "
                "Krishna Iyer, granted Indira Gandhi a conditional stay of "
                "the Allahabad High Court's verdict, permitting her to "
                "remain Prime Minister while the appeal was pending.",
            ),
            (
                "JP's 25 June 1975 Delhi rally",
                "On 25 June 1975 Jayaprakash Narayan addressed a mass rally "
                "in Delhi and announced a countrywide programme of civil "
                "disobedience, fusing the political and legal crises on "
                "the same day.",
            ),
            (
                "The Emergency proclamation: dated 25 June, announced 26 "
                "June",
                "The national Emergency was proclaimed under Article 352 "
                "with the proclamation dated 25 June 1975, but it was only "
                "publicly announced on 26 June 1975, and opposition leaders "
                "were arrested under the Maintenance of Internal Security "
                "Act, or MISA.",
            ),
            (
                "Detentions under MISA",
                "Over 100,000 people were detained without trial under "
                "MISA during the roughly nineteen months of the Emergency, "
                "as civil liberties were suspended and the press was "
                "censored.",
            ),
            (
                "The Twenty-Point Programme and Sanjay Gandhi's four-point "
                "programme",
                "The government announced a Twenty-Point Programme on 1 "
                "July 1975 to frame the Emergency's 'positive' agenda, and "
                "Sanjay Gandhi, Indira Gandhi's son, added his own four-"
                "point programme in 1976 alongside it.",
            ),
            (
                "The 42nd Amendment, 1976",
                "The 42nd Constitutional Amendment of 1976 greatly expanded "
                "central and executive power and curtailed several "
                "safeguards on fundamental rights during the Emergency.",
            ),
            (
                "Sanjay Gandhi's extra-constitutional power and its "
                "excesses",
                "Sanjay Gandhi, holding no formal office, became an extra-"
                "constitutional power centre during the Emergency, and "
                "compulsory sterilisation and slum-demolition drives "
                "carried out under his influence were the era's worst "
                "excesses.",
            ),
            (
                "The Shah Commission",
                "The Shah Commission was later constituted to inquire into "
                "the excesses committed during the Emergency, examining "
                "abuses of power once the Emergency had ended.",
            ),
            (
                "The 1977 elections and the Emergency's end",
                "In elections called in January 1977 and held in March "
                "1977, the electorate defeated the Congress and Sanjay "
                "Gandhi, a verdict for civil liberties that ended the "
                "Emergency.",
            ),
            (
                "The 44th Amendment, 1978",
                "The 44th Constitutional Amendment of 1978, passed after "
                "the Emergency had ended, reversed many of the 42nd "
                "Amendment's provisions and rebuilt safeguards on "
                "fundamental rights.",
            ),
            (
                "The JP movement's social base",
                "The JP movement mobilised students, the middle class, "
                "traders and the intelligentsia with considerable moral "
                "authority, but it never acquired a rural or working-class "
                "base comparable to its urban strength.",
            ),
            (
                "Chandra's balanced historiography of blame",
                "Bipan Chandra's account assigns responsibility evenly: "
                "JP's extra-parliamentary call for the police and army to "
                "disobey unlawful orders risked an undemocratic outcome, "
                "while Indira Gandhi's refusal of the constitutional exit "
                "of dissolving the Lok Sabha and holding fresh elections "
                "chose an authoritarian remedy instead.",
            ),
            (
                "The causal mechanism chain",
                "The Emergency's causal chain runs from the 1971 landslide "
                "and personalised leadership, through the 1972-73 economic "
                "crisis and the student movements of 1974, to the "
                "Allahabad judgment and JP's rally of June 1975, and then "
                "to the proclamation, its instruments, its excesses and the "
                "1977 reversal.",
            ),
            (
                "What held and what failed",
                "During the Emergency the electoral machinery itself held, "
                "producing a free verdict in 1977, while Parliament, the "
                "ruling party, the constitutional amendment process and, "
                "in the detention cases, the higher judiciary's protection "
                "of personal liberty, all failed to prevent the suspension "
                "of civil rights.",
            ),
            (
                "Fifty years of the Emergency, 25 June 2025",
                "On 25 June 2025 the Union Cabinet adopted an official "
                "resolution commemorating fifty years since the Emergency, "
                "honouring resistance to it and reaffirming constitutional "
                "democracy, fixing the chronology that the proclamation was "
                "dated 25 June 1975 and publicly announced on 26 June.",
            ),
        ],
        [
            "The Emergency was declared under Article 352, a national "
            "emergency, not under Article 356.",
            "JP's movement was led mainly by students, the middle class "
            "and traders, not by workers and peasants.",
            "The 42nd Amendment (1976) was passed during the Emergency; "
            "the 44th Amendment (1978) came afterwards and reversed many "
            "of its provisions; do not conflate the two.",
            "Indira Gandhi was unseated by the Allahabad High Court in "
            "1975, not the Supreme Court; the Supreme Court granted only a "
            "conditional stay.",
            "The Emergency was ended by the 1977 electoral verdict, not "
            "by any court ruling.",
            "The proclamation is dated 25 June 1975 but was publicly "
            "announced on 26 June 1975; the two dates must not be "
            "collapsed into one.",
            "The public did not oppose the Emergency from its first day; "
            "many initially welcomed the restoration of order.",
            "Coercive sterilisation was not a marginal issue; it was among "
            "the most decisive causes of the Congress's 1977 defeat.",
            "The JP movement was not purely peaceful and constitutional; "
            "it courted extra-constitutional methods that risked an "
            "undemocratic outcome.",
            "Indira Gandhi had a constitutional exit available, dissolving "
            "the Lok Sabha and holding early elections, and chose not to "
            "take it.",
            "Do not quantify sterilisations or demolitions with specific "
            "figures; only the approximate detention figure of over "
            "100,000 is recorded in the owner sources.",
            "The Shah Commission inquired into Emergency excesses after "
            "the Emergency had ended, not during it.",
            "The Twenty-Point Programme (1975) and Sanjay Gandhi's four-"
            "point programme (1976) are two distinct agendas, not the "
            "same programme under two names.",
        ],
        [
            (
                10,
                "Examine the immediate trigger for the declaration of the "
                "Emergency in June 1975.",
                "The Allahabad High Court's verdict against Indira Gandhi "
                "personally, converted within days into a proclamation of "
                "national emergency after JP's rally raised the political "
                "stakes, shows a personal legal threat becoming a national "
                "measure.",
                [4, 5, 6],
            ),
            (
                10,
                "Assess the social base and limitations of the JP "
                "movement.",
                "The JP movement's moral authority rested on students, the "
                "middle class, traders and the intelligentsia, but its "
                "lack of a rural or working-class base explains both its "
                "capacity to destabilise the government and its inability "
                "to sustain one after 1977.",
                [1, 2, 15],
            ),
            (
                15,
                "'The Emergency was produced by the convergence of an "
                "economic crisis, a political crisis and a legal crisis, "
                "none of which alone would have sufficed.' Examine.",
                "Inflation and scarcity supplied the economic crisis, the "
                "student movements and JP's leadership supplied the "
                "political crisis, and the Allahabad judgment supplied the "
                "legal crisis, and their convergence in June 1975 explains "
                "the timing and severity of the response.",
                [0, 2, 4, 7],
            ),
            (
                15,
                "Analyse the instruments and the principal excesses of "
                "the Emergency regime, 1975-77.",
                "MISA detentions, censorship and the 42nd Amendment "
                "supplied the legal instruments, while Sanjay Gandhi's "
                "extra-constitutional authority produced the era's worst "
                "excesses in coercive sterilisation and demolitions.",
                [7, 8, 9, 10],
            ),
            (
                20,
                "'Indian democracy both failed and passed the test of the "
                "Emergency.' Discuss with reference to its causes, its "
                "conduct and its end.",
                "Parliament, the ruling party and, in the detention cases, "
                "the higher judiciary failed to prevent the suspension of "
                "liberties, while the electoral machinery itself held and "
                "delivered a decisive reversal in 1977, so the verdict must "
                "specify that it was the voters, not the institutions, who "
                "passed the test.",
                [4, 6, 12, 17, 18],
            ),
            (
                20,
                "Trace the crisis of 1972-77 from its economic origins to "
                "its electoral resolution, and evaluate what it revealed "
                "about the resilience of Indian democratic institutions.",
                "An economic crisis produced a political challenge, a "
                "court judgment made the crisis personal, a leadership "
                "without internal checks answered with a national "
                "proclamation, and the electorate's 1977 verdict, followed "
                "by the 44th Amendment's safeguards, is the clearest "
                "evidence that the underlying institutions could still be "
                "restored.",
                [0, 2, 4, 7, 10, 13, 14],
            ),
        ],
        [],
        [
            "Jayaprakash Narayan",
            "Total Revolution",
            "Allahabad High Court",
            "MISA",
            "42nd Amendment",
            "Sanjay Gandhi",
            "1977 elections",
            "Article 352",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-34": [
        (
            "Two successions in twenty months",
            "timeline",
            """SHASTRI PM -> JUNE 1964, after Nehru's death
1965 WAR -> India-Pakistan; ends at TASHKENT DECLARATION, Jan 1966
SHASTRI DIES -> Tashkent, 10 JANUARY 1966, hours after signing
INDIRA ELECTED PM -> JANUARY 1966, defeats Morarji Desai 355-169 (Syndicate-backed)""",
            [
                "Shastri's accession and the 1965 war, June 1964 to "
                "January 1966",
                "Indira Gandhi's election as Prime Minister, January 1966",
            ],
        ),
        (
            "The mid-1960s economic crisis and the 1966 devaluation",
            "causal-chain",
            """1965 WAR EXPENDITURE + HARVEST FAILURES + FOOD-AID DEPENDENCE -> fiscal strain
RUPEE DEVALUED -> JUNE 1966, by about 35.5 per cent
POLITICAL COST -> blamed on Indira Gandhi within months of taking office
LEGACY -> durable aversion to externally pressed adjustment, until 1991""",
            ["The rupee devaluation of June 1966 and its causes"],
        ),
        (
            "1967: the end of easy dominance",
            "data-table",
            """FOURTH GENERAL ELECTION -> 1967
CONGRESS -> majority SLASHED nationally; loses power in EIGHT STATES
NEW PATTERN -> Samyukta Vidhayak Dal (SVD) coalition governments
MASS DEFECTION -> "Aya Ram Gaya Ram"; about 800 legislators switch, 1967-70""",
            [
                "The 1967 general election: the end of easy dominance",
                "Coalition governments and defection politics after 1967",
            ],
        ),
        (
            "1969: the Congress split",
            "institution-map",
            """TRIGGER -> V.V. Giri presidential contest + bank nationalisation (14 banks)
SPLIT -> Congress (R), Indira Gandhi   vs   Congress (O), the Syndicate
OUTCOME -> most Congress MPs and the AICC side with Indira Gandhi
RESULT -> numbers held for Congress (R); party organisation did not""",
            [
                "The 1969 Congress split: Giri, bank nationalisation and "
                "the Syndicate's defeat",
            ],
        ),
        (
            "Courts vs the executive, 1970",
            "evidence-debate",
            """SUPREME COURT, 1970 -> strikes down FIRST bank-nationalisation order
SUPREME COURT, 1970 -> strikes down privy-purse DERECOGNITION order
GOVERNMENT RESPONSE -> re-enacts bank nationalisation via fresh legislation
GOVERNMENT RESPONSE -> abolishes privy purses via 26th Amendment, 1971""",
            ["The Supreme Court's 1970 rulings against the executive"],
        ),
        (
            "1971: privy purses and Garibi Hatao",
            "timeline",
            """PRIVY PURSES ABOLISHED -> 1971, 26th Constitutional Amendment
1971 GENERAL ELECTION -> Congress (R) wins 352 of 518 seats
SLOGAN -> "Garibi Hatao"
READ IT CORRECTLY -> a NATIONAL plebiscite, delinked from state-level Congress""",
            ["1971: privy purses abolished and the Garibi Hatao landslide"],
        ),
        (
            "The 1971 Bangladesh war",
            "causal-chain",
            """ORIGIN -> crisis in East Pakistan; refugee influx into India
OUTCOME -> decisive Indian military victory
RESULT -> creation of Bangladesh
EFFECT -> Indira Gandhi's domestic authority becomes unassailable""",
            ["The 1971 Bangladesh war and its strategic significance"],
        ),
        (
            "1965 vs 1971 compared",
            "comparison",
            """1965 WAR -> origin: Pakistani infiltration into Kashmir
1965 WAR -> outcome: militarily inconclusive; ends at Tashkent Declaration
1971 WAR -> origin: East Pakistan refugee crisis
1971 WAR -> outcome: decisive victory; creates Bangladesh""",
            ["Comparing 1965 and 1971: two wars, two outcomes"],
        ),
        (
            "Pokhran-I, May 1974",
            "timeline",
            """TEST -> Pokhran-I, MAY 1974
OFFICIAL LABEL -> "peaceful nuclear explosion", not a declared weapons test
SIGNIFICANCE -> first Indian nuclear test; inside the Garibi-Hatao-to-Emergency arc
TRAP -> do not date this test to the 1960s""",
            ["Pokhran-I, May 1974: India's first nuclear test"],
        ),
        (
            "De-institutionalisation: the hidden cost",
            "causal-chain",
            """TECHNIQUE -> populist mobilisation + personalised leadership
EFFECT ON PARTY -> Congress organisation split and weakened after 1969
EFFECT ON CHECKS -> internal factional-conflict checks eroded
LONGER EFFECT -> structural background to the 1973-75 crisis""",
            ["De-institutionalisation: the hidden cost of consolidation"],
        ),
        (
            "The coal-sector nationalisation gap, 2019: a bounded caution",
            "problem-response",
            """ROUTED DEMAND -> 2019 Prelims GS-I Q48, coal-sector nationalisation status
LOCAL SUPPORT -> NONE in any modern-history source book in this repository
RULE -> no year, statute or sequence for coal nationalisation stated from memory
ACTION -> route any full answer to the Economy or Geography owner instead""",
            ["The coal-sector nationalisation gap: a bounded caution"],
        ),
        (
            "Resilience and cost: two verdicts on 1964-73",
            "argument-map",
            """VERDICT ONE -> resilience: two successions absorbed peacefully; 1971 war won
VERDICT TWO -> cost: party de-institutionalised; internal democracy eroded
CHANDRA'S READING -> the leftward turn was genuine, if organisationally costly
SYNTHESIS -> both readings are compatible, not competing, accounts of the decade""",
            ["Resilience and cost: two verdicts on 1964-73"],
        ),
    ],
    "modern-indian-history-35": [
        (
            "The 1972-73 economic crisis",
            "causal-chain",
            """TWIN MONSOON FAILURES + 1973 OIL SHOCK -> deepening scarcity
PRICE RISE -> about 22 per cent over 1972-73
EFFECT -> inflation, unemployment, food scarcity erode Indira Gandhi's popularity
TIMING -> follows directly on the 1971 Garibi Hatao landslide""",
            ["The 1972-73 economic crisis: drought, inflation and the oil "
             "shock"],
        ),
        (
            "Nav Nirman and the Bihar movement, 1974",
            "timeline",
            """NAV NIRMAN -> Gujarat, JANUARY 1974; students protest prices and corruption
BIHAR MOVEMENT -> MARCH 1974; JP takes leadership
JP'S CALL -> "Total Revolution" / Sampoorna Kranti
SPREAD -> student unrest becomes a nationwide anti-government movement""",
            [
                "Nav Nirman: the Gujarat student agitation, January 1974",
                "The Bihar movement and JP's Total Revolution, March 1974",
            ],
        ),
        (
            "The railway strike, May 1974",
            "procedure-sequence",
            """ALL-INDIA RAILWAY STRIKE -> MAY 1974, lasting 22 days
DIRECT CHALLENGE -> to the government's authority
ADDED DIMENSION -> economic disruption layered onto the political crisis
CONTEXT -> deepens the crisis JP's movement was already building on""",
            ["The railway strike of May 1974"],
        ),
        (
            "The Allahabad High Court judgment, 12 June 1975",
            "chronology",
            """PETITIONER -> Raj Narain
JUDGE -> Justice Jagmohanlal Sinha, Allahabad High Court
DATE -> 12 JUNE 1975
RULING -> sets aside Indira Gandhi's 1971 election on electoral malpractice""",
            ["The Allahabad High Court judgment, 12 June 1975"],
        ),
        (
            "The Supreme Court's conditional stay, 24 June 1975",
            "chronology",
            """COURT -> Supreme Court, Justice V.R. Krishna Iyer
DATE -> 24 JUNE 1975
RULING -> CONDITIONAL stay of the Allahabad verdict
EFFECT -> Indira Gandhi remains Prime Minister while the appeal is pending""",
            ["The Supreme Court's conditional stay, 24 June 1975"],
        ),
        (
            "The proclamation: dated 25 June, announced 26 June",
            "chronology",
            """JP'S DELHI RALLY -> 25 JUNE 1975; calls for civil disobedience
PROCLAMATION -> Article 352, DATED 25 JUNE 1975
PUBLIC ANNOUNCEMENT -> only on 26 JUNE 1975
TRAP -> the two dates must never be collapsed into one""",
            ["JP's 25 June rally and the proclamation of Emergency"],
        ),
        (
            "Instruments of the Emergency: MISA, censorship, 42nd "
            "Amendment",
            "institution-map",
            """DETENTIONS -> under MISA; over 100,000 held without trial, ~19 months
PRESS -> censorship imposed
CONSTITUTIONAL CHANGE -> 42nd Amendment, 1976; expands central/executive power
AGENDA -> Twenty-Point Programme, 1 July 1975""",
            [
                "The Emergency's legal instruments: MISA, censorship and "
                "the 42nd Amendment",
            ],
        ),
        (
            "Sanjay Gandhi's extra-constitutional power and its excesses",
            "problem-response",
            """POSITION -> no formal office; extra-constitutional power centre
PROGRAMME -> his own four-point programme, 1976
EXCESSES -> compulsory sterilisation drives
EXCESSES -> slum-demolition drives""",
            [
                "Sanjay Gandhi's extra-constitutional power and its "
                "excesses",
            ],
        ),
        (
            "1977: the electoral reversal",
            "timeline",
            """ELECTIONS CALLED -> January 1977
ELECTIONS HELD -> March 1977
RESULT -> Congress and Sanjay Gandhi defeated
MEANING -> a verdict FOR civil liberties; ends the Emergency""",
            ["The 1977 elections and the Emergency's end"],
        ),
        (
            "What held and what failed",
            "evidence-debate",
            """HELD -> the electoral machinery itself; free verdict delivered in 1977
FAILED -> Parliament; failed to check the executive
FAILED -> the ruling party; offered no internal restraint
FAILED -> judiciary's detention jurisprudence, in the MISA cases""",
            ["What held and what failed: a balanced verdict"],
        ),
        (
            "The JP movement's social base",
            "classification",
            """BASE -> students, middle class, traders, intelligentsia
NOT THE BASE -> rural poor or the organised urban working class
STRENGTH -> moral authority sufficient to destabilise the government
LIMITATION -> no base broad enough to govern after 1977""",
            ["The JP movement's social base: strength and limitation"],
        ),
        (
            "Fifty years of the Emergency, 2025",
            "application-pyq",
            """EVENT -> Union Cabinet resolution, 25 JUNE 2025
CONTENT -> commemorates fifty years since the Emergency
FRAMING -> honours resistance; reaffirms constitutional democracy
SOURCE -> PIB, PRID 2139543 (no public URL recorded by the owner)""",
            ["Fifty years of the Emergency: the 2025 commemoration"],
        ),
    ],
}


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
    "modern-indian-history-34": [
        authored_session(
            "Shastri's accession and the 1965 war, June 1964 to January "
            "1966",
            "Lal Bahadur Shastri's short but consequential premiership "
            "opens this topic's chronology: he became Prime Minister in "
            "June 1964 after Nehru's death, led India through the 1965 "
            "war, and died at Tashkent within hours of signing the "
            "declaration that ended it.",
            [
                "Shastri became Prime Minister in June 1964, chosen "
                "through a peaceful intra-party process rather than any "
                "crisis of succession.",
                "The 1965 India-Pakistan war was fought under his "
                "leadership and ended with the Tashkent Declaration, "
                "negotiated with Ayub Khan in January 1966.",
                "Shastri died at Tashkent on 11 January 1966, only hours "
                "after signing the declaration, prompting an immediate "
                "second succession.",
            ],
            "Do not relocate Shastri's death to India or to any other "
            "date; it occurred at Tashkent on 11 January 1966.",
            "Use this session to open any 'succession and institutional "
            "resilience' Mains answer spanning 1964-66.",
            """SHASTRI PM -> JUNE 1964, after Nehru's death
1965 WAR -> India-Pakistan; ends at TASHKENT DECLARATION, Jan 1966
SHASTRI DIES -> Tashkent, 10 JANUARY 1966, hours after signing
INDIRA ELECTED PM -> JANUARY 1966, defeats Morarji Desai 355-169""",
            "Lal Bahadur Shastri is the Prime Minister who led India "
            "through the 1965 war and died at Tashkent on 11 January "
            "1966, hours after signing the declaration that ended it.",
        ),
        authored_session(
            "Indira Gandhi's election as Prime Minister, January 1966",
            "Indira Gandhi's election as Prime Minister in January 1966 "
            "completed the second unplanned succession within twenty "
            "months, and it began under the assumption, soon disproved, "
            "that the Congress bosses known as the Syndicate could "
            "control her.",
            [
                "She was elected Prime Minister in January 1966, "
                "defeating Morarji Desai by 355 votes to 169 in the "
                "Congress Parliamentary Party.",
                "The Syndicate, a group of senior Congress bosses, backed "
                "her candidacy expecting to direct her government from "
                "behind the scenes.",
                "Within three years she had defeated the same Syndicate "
                "in the 1969 split, reversing the original expectation "
                "entirely.",
            ],
            "Do not reverse the 1966 vote count; Indira Gandhi defeated "
            "Morarji Desai 355 votes to 169, not the other way round.",
            "Use the Syndicate's miscalculation to answer any Mains "
            "question on how intra-party expectations about a new leader "
            "can be overturned.",
            """CONGRESS PARLIAMENTARY PARTY VOTE -> Indira Gandhi 355, Morarji Desai 169
BACKERS -> the "Syndicate", senior Congress bosses, expecting to control her
EXPECTATION -> a pliable, Syndicate-controlled Prime Minister
OUTCOME BY 1969 -> Indira Gandhi defeats the same Syndicate in the party split""",
            "Indira Gandhi is the Prime Minister elected in January 1966 "
            "by defeating Morarji Desai 355 votes to 169, initially with "
            "Syndicate backing that she later broke free of.",
        ),
        authored_session(
            "The rupee devaluation of June 1966 and its causes",
            "The rupee devaluation of June 1966 was Indira Gandhi's first "
            "major and politically costly decision, forced by a "
            "convergence of war expenditure, harvest failure and food-aid "
            "dependence rather than chosen from a position of strength.",
            [
                "The rupee was devalued by about 35.5 per cent in June "
                "1966, only months into Indira Gandhi's premiership.",
                "The devaluation followed 1965-war expenditure and "
                "successive harvest failures that had drained foreign "
                "exchange reserves.",
                "India's dependence on external food aid at the time gave "
                "donor pressure real leverage over the decision.",
            ],
            "Do not treat the June 1966 devaluation as an isolated policy "
            "choice made in normal economic conditions; it followed a "
            "specific crisis convergence.",
            "Use this session to answer any 'balance-of-payments crisis "
            "and political cost' Mains demand for the mid-1960s.",
            """1965 WAR EXPENDITURE + HARVEST FAILURES + FOOD-AID DEPENDENCE -> strain
RUPEE DEVALUED -> JUNE 1966, by about 35.5 per cent
POLITICAL COST -> blamed on Indira Gandhi within months of taking office
LEGACY -> durable aversion to externally pressed adjustment, until 1991""",
            "The June 1966 devaluation is the roughly 35.5 per cent "
            "reduction in the rupee's value undertaken by Indira Gandhi's "
            "government under war-expenditure and harvest-failure "
            "pressure.",
        ),
        authored_session(
            "The Prime Minister's Secretariat and early executive "
            "centralisation",
            "Under Shastri the Prime Minister's Secretariat, or PMO, "
            "began gaining administrative weight, a quiet institutional "
            "change that deepened under Indira Gandhi and became one root "
            "of the executive centralisation this topic traces to 1973-75.",
            [
                "The PMO's growing administrative weight under Shastri "
                "predates and foreshadows Indira Gandhi's later "
                "centralisation of authority.",
                "This centralisation ran in parallel with, and partly "
                "explains, the personalisation of Congress leadership "
                "after 1966.",
                "The trend connects institutionally to the "
                "de-institutionalisation this topic later analyses as the "
                "hidden cost of consolidation.",
            ],
            "Do not treat PMO centralisation as beginning only with "
            "Indira Gandhi; the administrative trend is already visible "
            "under Shastri.",
            "Use this session to supply an institutional-continuity point "
            "in any 'origins of executive centralisation' Mains answer.",
            """PMO -> Prime Minister's Secretariat; gains weight under Shastri
FUNCTION -> coordinates ministries directly from the PM's office
TREND -> continues and deepens under Indira Gandhi after 1966
SIGNIFICANCE -> early institutional root of executive centralisation""",
            "The Prime Minister's Secretariat, or PMO, is the "
            "administrative office that gained coordinating weight under "
            "Shastri and continued to grow under Indira Gandhi.",
        ),
        authored_session(
            "The 1967 general election: the end of easy dominance",
            "The fourth general election of 1967 is the pivot at which "
            "the 'Congress system' of easy national dominance ended, "
            "slashing the party's majority and costing it power in eight "
            "states in a single contest.",
            [
                "The Congress's Lok Sabha majority was sharply reduced in "
                "1967, though it retained power at the centre.",
                "Congress lost power in eight states, an unprecedented "
                "reversal at the state level.",
                "The result ended the assumption, valid since 1952, that "
                "Congress dominance was effectively unchallengeable.",
            ],
            "Do not describe the 1967 result as a comfortable Congress "
            "victory; its majority was slashed and it lost eight states.",
            "Use this session to date the beginning of the Congress "
            "system's decline to 1967, distinct from its completion in "
            "the 1969 split.",
            """FOURTH GENERAL ELECTION -> 1967
CONGRESS -> majority SLASHED nationally; loses power in EIGHT STATES
NEW PATTERN -> Samyukta Vidhayak Dal (SVD) coalition governments
MASS DEFECTION -> "Aya Ram Gaya Ram"; about 800 legislators switch, 1967-70""",
            "The 1967 general election is the fourth national election, "
            "in which Congress's majority was slashed and it lost power "
            "in eight states.",
        ),
        authored_session(
            "Coalition governments and defection politics after 1967",
            "The immediate structural consequence of 1967 was the "
            "arrival of coalition government in the states and the "
            "normalisation of legislative defection as a routine "
            "political instrument.",
            [
                "Samyukta Vidhayak Dal, or SVD, coalitions formed in "
                "several states where Congress had lost its majority.",
                "Mass floor-crossing after 1967 earned the nickname 'Aya "
                "Ram Gaya Ram', with roughly 800 legislators switching "
                "sides between 1967 and 1970.",
                "This defection problem was addressed only much later, by "
                "the 1985 Anti-Defection Act, a Polity-owner detail.",
            ],
            "Do not describe defection politics as a post-1969 "
            "phenomenon; it began immediately after the 1967 election.",
            "Use this session to link the 1967 election's consequences to "
            "the later Anti-Defection Act as a cross-topic Polity bridge.",
            """SVD COALITIONS -> form in states where Congress lost its 1967 majority
DEFECTION NICKNAME -> "Aya Ram Gaya Ram"
SCALE -> about 800 legislators switch sides, 1967-70
LATER FIX -> 1985 Anti-Defection Act (a Polity-owner detail)""",
            "'Aya Ram Gaya Ram' names the mass legislative floor-crossing "
            "that followed the 1967 election, addressed only later by the "
            "1985 Anti-Defection Act.",
        ),
        authored_session(
            "The 1969 Congress split: Giri, bank nationalisation and the "
            "Syndicate's defeat",
            "The 1969 Congress split converted the Syndicate's failed "
            "attempt to control Indira Gandhi into an open rupture, "
            "triggered by the presidential contest and the nationalisation "
            "of 14 banks in the same year.",
            [
                "Indira Gandhi split the Congress into Congress (R) and "
                "Congress (O) in 1969, defeating the Syndicate.",
                "Fourteen banks were nationalised in 1969, a populist "
                "measure that sharpened the intra-party conflict.",
                "Most Congress MPs and the AICC sided with Indira Gandhi, "
                "giving Congress (R) numerical dominance despite the "
                "split.",
            ],
            "Bank nationalisation occurred in 1969, not 1971; do not "
            "confuse it with the 1971 privy-purse abolition.",
            "Use this session to answer any 'how did Indira Gandhi "
            "consolidate power' Mains demand for 1969.",
            """TRIGGER -> V.V. Giri presidential contest + bank nationalisation (14 banks)
SPLIT -> Congress (R), Indira Gandhi   vs   Congress (O), the Syndicate
OUTCOME -> most Congress MPs and the AICC side with Indira Gandhi
RESULT -> numbers held for Congress (R); party organisation did not""",
            "The 1969 Congress split is the division of the Congress "
            "party into Congress (R) under Indira Gandhi and Congress (O) "
            "under the Syndicate, following the presidential contest and "
            "bank nationalisation.",
        ),
        authored_session(
            "The Supreme Court's 1970 rulings against the executive",
            "The Supreme Court's 1970 rulings show that Indira Gandhi's "
            "populist measures did not go unchallenged: the Court struck "
            "down both the first bank-nationalisation order and the "
            "privy-purse derecognition order in the same year.",
            [
                "The Supreme Court struck down the government's first "
                "bank-nationalisation order in 1970 on constitutional "
                "grounds.",
                "The Court also struck down the government's order "
                "derecognising princely rulers' privy purses in 1970.",
                "The government responded by re-enacting bank "
                "nationalisation through fresh legislation and abolishing "
                "privy purses through the 26th Amendment in 1971.",
            ],
            "Bank nationalisation did not go unchallenged; the Supreme "
            "Court struck down the government's first order in 1970 "
            "before it was re-enacted.",
            "Use this session to answer any 'checks on executive power in "
            "the late 1960s' Mains demand with concrete judicial evidence.",
            """SUPREME COURT, 1970 -> strikes down FIRST bank-nationalisation order
SUPREME COURT, 1970 -> strikes down privy-purse DERECOGNITION order
GOVERNMENT RESPONSE -> re-enacts bank nationalisation via fresh legislation
GOVERNMENT RESPONSE -> abolishes privy purses via 26th Amendment, 1971""",
            "The Supreme Court's 1970 rulings are the two judgments that "
            "struck down the government's first bank-nationalisation "
            "order and its privy-purse derecognition order in the same "
            "year.",
        ),
        authored_session(
            "1971: privy purses abolished and the Garibi Hatao landslide",
            "1971 combined a constitutional settlement, the abolition of "
            "privy purses, with an electoral landslide on the slogan "
            "'Garibi Hatao' that converted Indira Gandhi's authority into "
            "a genuinely national mandate.",
            [
                "Privy purses were formally abolished in 1971 through the "
                "26th Constitutional Amendment, after the 1970 court "
                "setback.",
                "Congress (R) won 352 of 518 seats in the 1971 general "
                "election campaigning on 'Garibi Hatao'.",
                "The 1971 mandate delinked the national Lok Sabha verdict "
                "from state-level Congress organisational strength for "
                "the first time.",
            ],
            "Privy-purse abolition occurred in 1971, not 1969; keep the "
            "two years, and the two measures, distinct.",
            "Use the 'plebiscite' framing to answer any Mains question on "
            "why the 1971 mandate differed in character from earlier "
            "Congress victories.",
            """PRIVY PURSES ABOLISHED -> 1971, 26th Constitutional Amendment
1971 GENERAL ELECTION -> Congress (R) wins 352 of 518 seats
SLOGAN -> "Garibi Hatao"
READ IT CORRECTLY -> a NATIONAL plebiscite, delinked from state-level Congress""",
            "'Garibi Hatao' names the 1971 election slogan on which "
            "Congress (R) won 352 of 518 seats, the same year privy "
            "purses were abolished by the 26th Amendment.",
        ),
        authored_session(
            "The 1971 Bangladesh war and its strategic significance",
            "The 1971 Bangladesh war, arising from the crisis in East "
            "Pakistan, gave Indira Gandhi a decisive military victory that "
            "made her domestic authority effectively unassailable.",
            [
                "The war originated in the refugee and political crisis "
                "in East Pakistan during 1971.",
                "India's military intervention produced a decisive "
                "victory over Pakistan.",
                "The war's outcome was the creation of Bangladesh as an "
                "independent state.",
            ],
            "Do not describe the 1971 war's outcome as inconclusive; it "
            "ended in decisive victory and the creation of Bangladesh.",
            "Use this session as the strategic climax evidence in any "
            "'peak of Indira Gandhi's authority' Mains answer.",
            """ORIGIN -> crisis in East Pakistan; refugee influx into India
OUTCOME -> decisive Indian military victory
RESULT -> creation of Bangladesh
EFFECT -> Indira Gandhi's domestic authority becomes unassailable""",
            "The 1971 Bangladesh war is the conflict, arising from the "
            "East Pakistan crisis, that India won decisively, resulting "
            "in the creation of Bangladesh.",
        ),
        authored_session(
            "Comparing 1965 and 1971: two wars, two outcomes",
            "Placing the 1965 and 1971 wars side by side sharpens the "
            "topic's central contrast: an inconclusive war that preceded "
            "Shastri's death against a decisive war that made Indira "
            "Gandhi's authority unassailable.",
            [
                "The 1965 war originated in Pakistani infiltration into "
                "Kashmir and ended militarily inconclusively at Tashkent.",
                "The 1971 war originated in the East Pakistan crisis and "
                "ended decisively with the creation of Bangladesh.",
                "The contrast in outcomes explains why 1966 opened with "
                "political vulnerability while 1971-72 opened with "
                "unassailable authority.",
            ],
            "Do not treat the two wars as interchangeable evidence for "
            "the same argument; their origins and outcomes were "
            "different in kind, not just in degree.",
            "Use this comparison to answer any 'assess the impact of war "
            "on domestic political authority' Mains demand.",
            """1965 WAR -> origin: Pakistani infiltration into Kashmir
1965 WAR -> outcome: militarily inconclusive; ends at Tashkent Declaration
1971 WAR -> origin: East Pakistan refugee crisis
1971 WAR -> outcome: decisive victory; creates Bangladesh""",
            "Comparing 1965 and 1971 means contrasting an inconclusive "
            "war ending at Tashkent with a decisive war that created "
            "Bangladesh, and their opposite effects on domestic authority.",
        ),
        authored_session(
            "Pokhran-I, May 1974: India's first nuclear test",
            "Pokhran-I in May 1974 closes this topic's decade with India's "
            "first nuclear test, officially described as a 'peaceful "
            "nuclear explosion' rather than a declared weapons test.",
            [
                "India conducted its first nuclear test, Pokhran-I, in "
                "May 1974.",
                "The government officially described the test as a "
                "'peaceful nuclear explosion' at the time.",
                "The test sits chronologically inside the arc running "
                "from the 1971 landslide to the 1975 Emergency.",
            ],
            "Do not date Pokhran-I to the 1960s or describe it as a "
            "declared weapons test; it was May 1974 and officially "
            "framed as peaceful.",
            "Use this session to supply the strategic-capability point in "
            "any 'India's rise after 1971' Mains answer.",
            """TEST -> Pokhran-I, MAY 1974
OFFICIAL LABEL -> "peaceful nuclear explosion", not a declared weapons test
SIGNIFICANCE -> first Indian nuclear test; inside the Garibi-Hatao-to-Emergency arc
TRAP -> do not date this test to the 1960s""",
            "Pokhran-I is India's first nuclear test, conducted in May "
            "1974 and officially described as a peaceful nuclear "
            "explosion.",
        ),
        authored_session(
            "De-institutionalisation: the hidden cost of consolidation",
            "The same populist and organisational techniques that made "
            "Indira Gandhi dominant also personalised authority and "
            "weakened the Congress party's internal institutions, the "
            "structural background to the 1973-75 crisis this topic leads "
            "into.",
            [
                "Personalised leadership after 1969 weakened, rather than "
                "strengthened, Congress's internal party democracy.",
                "The split and the populist mandate of 1971 further "
                "eroded the checks that had once contained factional "
                "conflict.",
                "This de-institutionalisation is the structural background "
                "to the 1973-75 crisis analysed in the following topic.",
            ],
            "Personalised leadership after 1969 de-institutionalised the "
            "Congress party; it did not strengthen party institutions.",
            "Use this session as the analytical bridge connecting this "
            "topic's consolidation of power to the JP Movement and the "
            "Emergency.",
            """TECHNIQUE -> populist mobilisation + personalised leadership
EFFECT ON PARTY -> Congress organisation split and weakened after 1969
EFFECT ON CHECKS -> internal factional-conflict checks eroded
LONGER EFFECT -> structural background to the 1973-75 crisis""",
            "De-institutionalisation names the erosion of Congress's "
            "internal party checks that accompanied Indira Gandhi's "
            "personalised consolidation of power after 1969.",
        ),
        authored_session(
            "The coal-sector nationalisation gap: a bounded caution",
            "One routed Prelims demand, on the status of coal-sector "
            "nationalisation, has no supporting content in any local "
            "modern-history source, and this session states that gap "
            "transparently rather than inventing a resolution.",
            [
                "The 2019 Prelims GS-I Q48 demand asks about the status of "
                "coal-sector nationalisation in independent India.",
                "No modern-history source book held in this repository "
                "supports a year, statute or sequence for coal-sector "
                "nationalisation.",
                "The owner file explicitly recommends routing any full "
                "answer to the Economy or Geography owner instead.",
            ],
            "Never state a year, statute name or sequence for coal-sector "
            "nationalisation from memory in this topic; the local sources "
            "do not support it.",
            "Use this session only to acknowledge the routed demand "
            "exists; do not attempt a full Prelims answer from this "
            "topic's material.",
            """ROUTED DEMAND -> 2019 Prelims GS-I Q48, coal-sector nationalisation status
LOCAL SUPPORT -> NONE in any modern-history source book in this repository
RULE -> no year, statute or sequence for coal nationalisation stated from memory
ACTION -> route any full answer to the Economy or Geography owner instead""",
            "The coal-sector nationalisation gap is the routed 2019 "
            "Prelims demand that this topic's local sources cannot "
            "support with any verified year, statute or sequence.",
        ),
        authored_session(
            "Resilience and cost: two verdicts on 1964-73",
            "The decade from 1964 to 1973 supports two compatible "
            "verdicts: institutional resilience, shown by two peaceful "
            "successions and a decisive war, and organisational cost, "
            "shown by the de-institutionalisation this topic has traced.",
            [
                "The resilience reading points to two successions "
                "absorbed peacefully and a war won decisively by 1971.",
                "The cost reading points to a Congress party split, "
                "personalised and organisationally hollowed out by 1971.",
                "Bipan Chandra reads the leftward turn sympathetically "
                "while still conceding the cost of de-institutionalisation.",
            ],
            "Do not present resilience and cost as mutually exclusive "
            "verdicts; the owner's own historiography treats them as "
            "compatible readings of the same decade.",
            "Use this closing session to structure a balanced conclusion "
            "for any comprehensive Mains essay on 1964-73.",
            """VERDICT ONE -> resilience: two successions absorbed peacefully; 1971 war won
VERDICT TWO -> cost: party de-institutionalised; internal democracy eroded
CHANDRA'S READING -> the leftward turn was genuine, if organisationally costly
SYNTHESIS -> both readings are compatible, not competing, accounts of the decade""",
            "Resilience and cost together name the two compatible verdicts "
            "on 1964-73: institutional resilience shown by successful "
            "successions and war, and organisational cost shown by "
            "de-institutionalisation.",
        ),
    ],
    "modern-indian-history-35": [
        authored_session(
            "The 1972-73 economic crisis: drought, inflation and the oil "
            "shock",
            "This topic opens where the previous one closed: the 1971 "
            "landslide's popularity was rapidly eroded by an economic "
            "crisis of twin monsoon failures, drought and the 1973 oil "
            "shock, the material precondition for the movements that "
            "followed.",
            [
                "Two successive monsoon failures produced drought "
                "conditions across 1972-73.",
                "The 1973 oil shock added a further external inflationary "
                "pressure on top of the domestic harvest crisis.",
                "Prices rose by about 22 per cent over 1972-73, eroding "
                "Indira Gandhi's popularity within two years of her 1971 "
                "landslide.",
            ],
            "Do not treat the 1972-73 crisis as unrelated to the 1971 "
            "landslide; it directly explains how quickly that popularity "
            "eroded.",
            "Use this session to open any 'origins of the Emergency' "
            "Mains answer with its economic precondition.",
            """TWIN MONSOON FAILURES + 1973 OIL SHOCK -> deepening scarcity
PRICE RISE -> about 22 per cent over 1972-73
EFFECT -> inflation, unemployment, food scarcity erode Indira Gandhi's popularity
TIMING -> follows directly on the 1971 Garibi Hatao landslide""",
            "The 1972-73 economic crisis is the combination of twin "
            "monsoon failures, drought and the 1973 oil shock that "
            "produced a roughly 22 per cent price rise and eroded Indira "
            "Gandhi's post-1971 popularity.",
        ),
        authored_session(
            "Nav Nirman: the Gujarat student agitation, January 1974",
            "The Nav Nirman agitation in Gujarat, beginning in January "
            "1974, was the first of the student movements that grew out "
            "of the 1972-73 economic crisis and set the pattern later "
            "followed in Bihar.",
            [
                "The agitation began in Gujarat in January 1974 over "
                "rising prices and allegations of corruption.",
                "Students led the protest, drawing in the wider middle "
                "class rather than organised labour or the rural poor.",
                "Its success in forcing political change in Gujarat "
                "encouraged JP and others to see student mobilisation as "
                "a viable route to wider political change.",
            ],
            "Do not confuse Nav Nirman with the Bihar movement; Nav "
            "Nirman began earlier, in January 1974, and in a different "
            "state.",
            "Use this session to answer any 'origins of the JP movement' "
            "Mains demand with its precise January 1974 starting point.",
            """NAV NIRMAN -> Gujarat, JANUARY 1974; students protest prices, corruption
BIHAR MOVEMENT -> MARCH 1974; JP takes leadership
JP'S CALL -> "Total Revolution" / Sampoorna Kranti
SPREAD -> student unrest becomes a nationwide anti-government movement""",
            "Nav Nirman is the student agitation that began in Gujarat in "
            "January 1974 over prices and corruption, the first of the "
            "movements that fed into the wider crisis of 1974-75.",
        ),
        authored_session(
            "The Bihar movement and JP's Total Revolution, March 1974",
            "The Bihar student movement of March 1974 acquired national "
            "significance once Jayaprakash Narayan took its leadership and "
            "reframed it as 'Total Revolution', or Sampoorna Kranti, "
            "against corruption and misgovernance.",
            [
                "The Bihar student movement began in March 1974, initially "
                "over local grievances similar to Nav Nirman's.",
                "Jayaprakash Narayan, known as JP, assumed leadership of "
                "the movement and gave it an all-India political frame.",
                "'Total Revolution' called for sweeping change beyond "
                "electoral politics, including moral appeals to state "
                "institutions.",
            ],
            "Do not describe JP's movement as confined to Bihar; his "
            "leadership converted a state agitation into a national "
            "political challenge.",
            "Use this session to answer any 'JP's role in Indian "
            "democracy' Mains demand with the precise March 1974 starting "
            "point and the Total Revolution frame.",
            """BIHAR MOVEMENT -> begins MARCH 1974; local grievances, like Nav Nirman's
JP TAKES LEADERSHIP -> converts a state agitation into a national challenge
JP'S CALL -> "Total Revolution" / Sampoorna Kranti
SCOPE -> moral appeals to state institutions, beyond electoral politics alone""",
            "Total Revolution, or Sampoorna Kranti, is Jayaprakash "
            "Narayan's call, from March 1974, for sweeping change against "
            "corruption and misgovernance beyond ordinary electoral "
            "politics.",
        ),
        authored_session(
            "The railway strike of May 1974",
            "The all-India railway strike of May 1974, lasting 22 days, "
            "added a direct economic challenge to the government on top "
            "of the political pressure already building from the student "
            "movements.",
            [
                "The strike was all-India in scope and lasted 22 days in "
                "May 1974.",
                "It directly challenged the government's authority over "
                "essential services.",
                "Its economic disruption compounded the political crisis "
                "JP's movement was already generating.",
            ],
            "Do not treat the railway strike as separate from the "
            "political crisis of 1974; it added an economic dimension to "
            "the same building confrontation.",
            "Use this session to answer any 'economic dimensions of the "
            "pre-Emergency crisis' Mains demand.",
            """ALL-INDIA RAILWAY STRIKE -> MAY 1974, lasting 22 days
DIRECT CHALLENGE -> to the government's authority
ADDED DIMENSION -> economic disruption layered onto the political crisis
CONTEXT -> deepens the crisis JP's movement was already building on""",
            "The railway strike of May 1974 is the 22-day all-India "
            "strike that added economic disruption to the political "
            "crisis building around the JP movement.",
        ),
        authored_session(
            "The Allahabad High Court judgment, 12 June 1975",
            "The Allahabad High Court's judgment of 12 June 1975 is the "
            "legal crisis that converted a building political confrontation "
            "into an immediate personal threat to Indira Gandhi's "
            "premiership.",
            [
                "Raj Narain's petition challenged Indira Gandhi's 1971 "
                "election on grounds of electoral malpractice.",
                "Justice Jagmohanlal Sinha delivered the judgment on 12 "
                "June 1975, setting aside her election.",
                "The verdict, if it stood unmodified, would have "
                "disqualified her from the Lok Sabha and the "
                "premiership.",
            ],
            "Indira Gandhi was unseated by the Allahabad High Court, not "
            "the Supreme Court; keep the two courts and their rulings "
            "distinct.",
            "Use this session to answer any 'immediate trigger for the "
            "Emergency' Mains demand with the precise court, judge and "
            "date.",
            """PETITIONER -> Raj Narain
JUDGE -> Justice Jagmohanlal Sinha, Allahabad High Court
DATE -> 12 JUNE 1975
RULING -> sets aside Indira Gandhi's 1971 election on electoral malpractice""",
            "The Allahabad High Court judgment of 12 June 1975 is Justice "
            "Jagmohanlal Sinha's ruling, on Raj Narain's petition, that "
            "set aside Indira Gandhi's 1971 election.",
        ),
        authored_session(
            "The Supreme Court's conditional stay, 24 June 1975",
            "The Supreme Court's conditional stay of 24 June 1975 kept "
            "Indira Gandhi in office pending appeal, but only "
            "conditionally, leaving her political and legal position "
            "unresolved in the days before the Emergency.",
            [
                "Justice V.R. Krishna Iyer granted the stay on 24 June "
                "1975.",
                "The stay was conditional, permitting her to remain Prime "
                "Minister while the appeal against the Allahabad judgment "
                "was pending.",
                "The stay did not resolve the underlying legal challenge, "
                "leaving political uncertainty that fed directly into the "
                "events of the following two days.",
            ],
            "The Supreme Court granted only a conditional stay on 24 June "
            "1975; it did not overturn the Allahabad High Court's "
            "judgment.",
            "Use this session to answer any 'sequence of events before "
            "the Emergency' Mains demand with the precise 24 June date "
            "and judge.",
            """COURT -> Supreme Court, Justice V.R. Krishna Iyer
DATE -> 24 JUNE 1975
RULING -> CONDITIONAL stay of the Allahabad verdict
EFFECT -> Indira Gandhi remains Prime Minister while the appeal is pending""",
            "The Supreme Court's conditional stay of 24 June 1975 is "
            "Justice V.R. Krishna Iyer's ruling permitting Indira Gandhi "
            "to remain Prime Minister pending appeal of the Allahabad "
            "judgment.",
        ),
        authored_session(
            "JP's 25 June rally and the proclamation of Emergency",
            "JP's mass rally in Delhi on 25 June 1975 and the Emergency "
            "proclamation dated the same day converged within hours, "
            "though the proclamation was only publicly announced the "
            "following morning.",
            [
                "Jayaprakash Narayan addressed a mass rally in Delhi on 25 "
                "June 1975, calling for a countrywide programme of civil "
                "disobedience.",
                "The national Emergency was proclaimed under Article 352 "
                "with the proclamation dated 25 June 1975.",
                "The proclamation was publicly announced only on 26 June "
                "1975, and opposition leaders were arrested under MISA.",
            ],
            "The proclamation is dated 25 June 1975 but was publicly "
            "announced on 26 June 1975; the two dates must not be "
            "collapsed into one.",
            "Use the precise 25/26 June sequence to answer any 'exact "
            "chronology of the Emergency's declaration' Prelims-style "
            "demand.",
            """JP'S DELHI RALLY -> 25 JUNE 1975; calls for civil disobedience
PROCLAMATION -> Article 352, DATED 25 JUNE 1975
PUBLIC ANNOUNCEMENT -> only on 26 JUNE 1975
TRAP -> the two dates must never be collapsed into one""",
            "The Emergency proclamation is the Article 352 declaration "
            "dated 25 June 1975 but publicly announced only on 26 June "
            "1975, issued the same day as JP's Delhi rally.",
        ),
        authored_session(
            "The Emergency's legal instruments: MISA, censorship and the "
            "42nd Amendment",
            "The Emergency was enforced through a specific set of legal "
            "instruments: detentions under MISA, press censorship, and "
            "the 42nd Amendment of 1976 that expanded central and "
            "executive power.",
            [
                "Over 100,000 people were detained without trial under "
                "MISA over the roughly nineteen months of the Emergency.",
                "The press was censored, restricting reporting on "
                "detentions and government actions.",
                "The 42nd Constitutional Amendment of 1976 expanded "
                "central and executive power and curtailed several rights "
                "safeguards.",
            ],
            "Do not quantify sterilisations or demolitions with specific "
            "figures; only the approximate MISA detention figure of over "
            "100,000 is recorded in the owner sources.",
            "Use this session to answer any 'instruments of authoritarian "
            "rule during the Emergency' Mains demand.",
            """DETENTIONS -> under MISA; over 100,000 held without trial, ~19 months
PRESS -> censorship imposed
CONSTITUTIONAL CHANGE -> 42nd Amendment, 1976; expands central/executive power
AGENDA -> Twenty-Point Programme, 1 July 1975""",
            "MISA, the Maintenance of Internal Security Act, is the law "
            "under which over 100,000 people were detained without trial "
            "during the Emergency, alongside press censorship and the "
            "42nd Amendment.",
        ),
        authored_session(
            "Sanjay Gandhi's extra-constitutional power and its "
            "excesses",
            "Sanjay Gandhi, holding no formal office, became an extra-"
            "constitutional centre of power during the Emergency, and the "
            "excesses carried out under his influence, compulsory "
            "sterilisation and slum demolition, became the era's most "
            "damaging legacy.",
            [
                "Sanjay Gandhi held no formal government or party office "
                "yet exercised substantial influence over policy.",
                "He promoted his own four-point programme in 1976, "
                "alongside the government's Twenty-Point Programme.",
                "Compulsory sterilisation and slum-demolition drives "
                "carried out under his influence became the Emergency's "
                "most criticised excesses.",
            ],
            "Coercive sterilisation was not a marginal issue; it was "
            "among the most decisive causes of the Congress's 1977 "
            "defeat.",
            "Use this session to answer any 'excesses of the Emergency' "
            "Mains demand with concrete, source-backed examples.",
            """POSITION -> no formal office; extra-constitutional power centre
PROGRAMME -> his own four-point programme, 1976
EXCESSES -> compulsory sterilisation drives
EXCESSES -> slum-demolition drives""",
            "Sanjay Gandhi is Indira Gandhi's son who, holding no formal "
            "office, became an extra-constitutional power centre during "
            "the Emergency, associated with coercive sterilisation and "
            "slum-demolition excesses.",
        ),
        authored_session(
            "The Shah Commission and the reckoning with excess",
            "The Shah Commission, constituted after the Emergency ended, "
            "carried out the formal official reckoning with its "
            "excesses, examining the abuses of power that had gone "
            "uninvestigated while the Emergency itself was in force.",
            [
                "The Shah Commission was constituted after the Emergency "
                "ended, once the change of government made such an "
                "inquiry possible.",
                "It examined abuses of power, including detentions and "
                "excesses attributed to Sanjay Gandhi's circle.",
                "Its findings supplied the documentary record later cited "
                "in accounts of the Emergency's excesses.",
            ],
            "The Shah Commission inquired into Emergency excesses after "
            "the Emergency had ended, not during it.",
            "Use this session to answer any 'official reckoning with "
            "Emergency excesses' Mains demand with the correct "
            "post-Emergency timing.",
            """SANJAY GANDHI EXCESSES -> sterilisation and demolition drives, 1975-77
SHAH COMMISSION -> constituted AFTER the Emergency ended
FUNCTION -> formal inquiry into abuses of power during the Emergency
OUTCOME -> documentary record cited in later accounts of the Emergency""",
            "The Shah Commission is the official inquiry, constituted "
            "after the Emergency ended, into the abuses of power "
            "committed during it.",
        ),
        authored_session(
            "The 1977 elections and the Emergency's end",
            "The elections called in January 1977 and held in March 1977 "
            "delivered the electoral verdict that ended the Emergency, "
            "defeating both the Congress and Sanjay Gandhi personally.",
            [
                "Elections were called in January 1977 after the "
                "Emergency had lasted roughly nineteen months.",
                "Polling was held in March 1977, and the electorate "
                "defeated Congress and Sanjay Gandhi.",
                "The defeat is read as a verdict for civil liberties "
                "rather than merely an anti-incumbency result.",
            ],
            "The Emergency was ended by the 1977 electoral verdict, not "
            "by any court ruling.",
            "Use this session to answer any 'how did the Emergency end' "
            "Mains demand with the precise January-to-March 1977 "
            "sequence.",
            """ELECTIONS CALLED -> January 1977
ELECTIONS HELD -> March 1977
RESULT -> Congress and Sanjay Gandhi defeated
MEANING -> a verdict FOR civil liberties; ends the Emergency""",
            "The 1977 elections, called in January and held in March, are "
            "the polls that defeated Congress and Sanjay Gandhi and "
            "ended the Emergency.",
        ),
        authored_session(
            "The 44th Amendment, 1978: rebuilding safeguards",
            "The 44th Constitutional Amendment of 1978, passed after the "
            "Emergency had ended, reversed many of the 42nd Amendment's "
            "provisions and rebuilt safeguards on fundamental rights.",
            [
                "The 44th Amendment was passed in 1978, after the "
                "Emergency's end and the change of government.",
                "It reversed many of the 42nd Amendment's expansions of "
                "central and executive power.",
                "It restored and strengthened several safeguards on "
                "fundamental rights that had been curtailed in 1976.",
            ],
            "The 42nd Amendment (1976) was passed during the Emergency; "
            "the 44th Amendment (1978) came afterwards and reversed many "
            "of its provisions; do not conflate the two.",
            "Use this session to answer any 'constitutional correction "
            "after the Emergency' Mains demand.",
            """44TH AMENDMENT -> 1978, passed AFTER the Emergency ended
REVERSES -> many 42nd Amendment expansions of central/executive power
RESTORES -> safeguards on fundamental rights curtailed in 1976
TRAP -> do not conflate the 42nd (1976, during) and 44th (1978, after) Amendments""",
            "The 44th Amendment of 1978 is the constitutional change, "
            "passed after the Emergency ended, that reversed many 42nd "
            "Amendment provisions and rebuilt rights safeguards.",
        ),
        authored_session(
            "The JP movement's social base: strength and limitation",
            "The JP movement's social base of students, the middle class, "
            "traders and the intelligentsia gave it moral authority "
            "sufficient to destabilise the government but never a rural "
            "or working-class foundation broad enough to govern "
            "afterwards.",
            [
                "The movement mobilised students, the middle class and "
                "traders across several states.",
                "It drew significant support from the intelligentsia, "
                "lending it moral and rhetorical authority.",
                "It never acquired a rural or organised working-class "
                "base comparable to its urban strength.",
            ],
            "The JP movement was led mainly by students, the middle "
            "class and traders, not by workers and peasants.",
            "Use this session to answer any 'assess the JP movement's "
            "social composition' Mains demand.",
            """BASE -> students, middle class, traders, intelligentsia
NOT THE BASE -> rural poor or the organised urban working class
STRENGTH -> moral authority sufficient to destabilise the government
LIMITATION -> no base broad enough to govern after 1977""",
            "The JP movement's social base names its core constituency of "
            "students, the middle class, traders and the intelligentsia, "
            "distinct from the rural poor or organised labour.",
        ),
        authored_session(
            "What held and what failed: a balanced verdict",
            "A balanced verdict on the Emergency must specify precisely "
            "what held, the electoral machinery, and what failed, "
            "Parliament, the ruling party and the judiciary's protection "
            "of personal liberty in the detention cases.",
            [
                "The electoral machinery itself held, delivering a free "
                "and decisive verdict in 1977.",
                "Parliament and the ruling party failed to restrain the "
                "executive's suspension of civil liberties.",
                "The higher judiciary's detention jurisprudence, in the "
                "MISA cases, also failed to protect personal liberty "
                "during the Emergency.",
            ],
            "Do not credit 'Indian democracy' in general for the "
            "Emergency's end; specify that it was the electorate, not the "
            "other institutions, that held.",
            "Use this session to structure any 'did Indian democracy pass "
            "the test of the Emergency' Mains answer with institution-by-"
            "institution precision.",
            """HELD -> the electoral machinery itself; free verdict delivered in 1977
FAILED -> Parliament; failed to check the executive
FAILED -> the ruling party; offered no internal restraint
FAILED -> judiciary's detention jurisprudence, in the MISA cases""",
            "'What held and what failed' names the institution-by-"
            "institution verdict on the Emergency: the electoral "
            "machinery held while Parliament, the ruling party and "
            "detention jurisprudence failed.",
        ),
        authored_session(
            "Fifty years of the Emergency: the 2025 commemoration",
            "On 25 June 2025 the Union Cabinet adopted an official "
            "resolution commemorating fifty years since the Emergency, a "
            "verified live linkage that fixes this topic's chronology "
            "exactly at the proclamation's dated day.",
            [
                "The Union Cabinet's resolution was adopted on 25 June "
                "2025, exactly fifty years after the proclamation's dated "
                "day.",
                "The resolution honours resistance to the Emergency and "
                "reaffirms constitutional democracy.",
                "The source is a Press Information Bureau release, PRID "
                "2139543; the owner records no public URL for it.",
            ],
            "Do not invent a URL for this PIB release; only the PRID "
            "2139543 citation is recorded by the owner.",
            "Use this session to bridge the historical Emergency to a "
            "verified 2025 current-affairs anchor in any recent-linkage "
            "Mains or Prelims answer.",
            """EVENT -> Union Cabinet resolution, 25 JUNE 2025
CONTENT -> commemorates fifty years since the Emergency
FRAMING -> honours resistance; reaffirms constitutional democracy
SOURCE -> PIB, PRID 2139543 (no public URL recorded by the owner)""",
            "The 2025 Emergency commemoration is the Union Cabinet's 25 "
            "June 2025 resolution marking fifty years since the "
            "Emergency, cited to PIB PRID 2139543.",
        ),
    ],
}


TOPIC_CHRONOLOGY: dict[str, list[str]] = {
    "modern-indian-history-34": [
        "June 1964",
        "10 January 1966",
        "January 1966",
        "June 1966",
        "1967",
        "1969",
        "1970",
        "1971",
        "May 1974",
        "1973-75",
        "1991",
        "1985",
        "2019",
    ],
    "modern-indian-history-35": [
        "1972-73",
        "January 1974",
        "March 1974",
        "May 1974",
        "12 June 1975",
        "24 June 1975",
        "25 June 1975",
        "26 June",
        "1 July 1975",
        "1976",
        "1977",
        "1978",
        "25 June 2025",
    ],
}

FORBIDDEN_TOPIC_PHRASES: dict[str, list[str]] = {
    "modern-indian-history-34": [
        "Shastri died in Delhi",
        "bank nationalisation took place in 1971",
        "privy purses were abolished in 1969",
        "Congress won a comfortable majority in 1967",
        "Pokhran-I was a declared nuclear weapons test",
    ],
    "modern-indian-history-35": [
        "the Emergency was declared under Article 356",
        "the Supreme Court struck down Indira Gandhi's election",
        "the Emergency ended through a court verdict",
        "the JP movement drew its base from workers and peasants",
        "sterilisation figures ran into the millions",
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
        "*The visual fixes this subtopic's chronology, mechanism or "
        "boundary before the evidence.*"
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
        "scope": "Modern Indian History learner-v2 Topics 34-35",
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

    if key == "modern-indian-history-34":
        strict = [
            "Lal Bahadur Shastri",
            "Tashkent Declaration",
            "10 January 1966",
            "Morarji Desai",
            "355",
            "169",
            "35.5 per cent",
            "eight states",
            "Aya Ram Gaya Ram",
            "V.V. Giri",
            "14 banks",
            "26th Constitutional Amendment",
            "352 of 518",
            "Garibi Hatao",
            "Bangladesh",
            "Pokhran-I",
            "peaceful nuclear explosion",
            "1985 Anti-Defection Act",
            "coal-sector nationalisation",
        ]
    else:
        strict = [
            "Jayaprakash Narayan",
            "Sampoorna Kranti",
            "Nav Nirman",
            "Jagmohanlal Sinha",
            "Raj Narain",
            "V.R. Krishna Iyer",
            "Article 352",
            "26 June 1975",
            "MISA",
            "Twenty-Point Programme",
            "42nd Amendment",
            "Sanjay Gandhi",
            "Shah Commission",
            "44th Amendment",
            "PRID 2139543",
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
    """Topics 32-33 must remain exactly as their own generators authored them."""

    expected = ["modern-indian-history-32", "modern-indian-history-33"]
    if [config["key"] for config in previous.TOPICS] != expected:
        raise ValueError("Topics 32-33 configuration was mutated on import.")
    if set(previous.PANEL_DATA) != set(expected):
        raise ValueError("Topics 32-33 panel data was mutated on import.")


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
