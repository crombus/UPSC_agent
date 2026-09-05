"""Build Modern Indian History learner-v2 Topics 32-33.

This authoring-only generator writes complete reusable Markdown, solved
workbooks, manual ASCII and graphical specifications, and tracker-free
generation-one manifests for the Nehru Era (hope, foreign policy and legacy)
and for party politics between 1947 and 1967 (the Congress system and the
opposition). It deliberately does not render PDFs, update the tracker,
regenerate indexes, finalize generations, or publish packages.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base
import generate_modern_history_30_31_sequential as previous


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
    / "modern-indian-history-32-33-2026-08-31-sequential.json"
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
            / "_PYQ-ROUTING-PRELIMS-2024-2025.md",
        ]
    )
)
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]
OFFICIAL_QUESTION_SOURCES = list(base.OFFICIAL_QUESTION_SOURCES)


TOPICS = [
    base.topic(
        32,
        "The Nehru Era \u2014 Hope, Foreign Policy & Legacy",
        "32_The-Nehru-Era-Hope-Foreign-Policy-and-Legacy.md",
        "32_The-Nehru-Era-Hope-Foreign-Policy-and-Legacy.md",
        "32_The-Nehru-Era-Hope-Foreign-Policy-and-Legacy_"
        "Complete-Topic-Package.md",
        [
            "basic/29_Colonial-Legacy-and-Foundations-of-the-Republic.md",
            "basic/33_Party-Politics-1947-67-Congress-System-and-Opposition.md",
            "basic/38_Economy-Land-Society-and-State-A-Post-Independence-"
            "Synthesis.md",
            "30_Linguistic-Reorganisation-of-States-and-Regionalism-1947-1967_"
            "Complete-Topic-Package.md",
        ],
        [],
        "No verified live current-affairs item is pegged to this topic. The "
        "owner's own Current-link section frames the Nehru era's institutions "
        "(planning, non-alignment, parliamentary democracy) as evergreen exam "
        "themes rather than as a dated news event, and that bounded, "
        "unattributed framing is preserved here rather than inventing a "
        "specific live source or date.",
        "The Basic and Advanced owner Markdown for this topic were "
        "reconciled against each other and against the folder's shared "
        "post-independence OCR source, Bipan Chandra, Mridula Mukherjee and "
        "Aditya Mukherjee, *India After Independence, 1947\u20132000*. Every "
        "date, name and institution used below already carries the owners' "
        "own \u2705 (source-backed) or \u26a0\ufe0f (inference) tagging, and "
        "that tagging is preserved rather than re-verified page by page "
        "against the raw PDF in this authoring pass.",
        "One Prelims demand is routed to this owner in the local ledgers "
        "(`_PYQ-ROUTING-PRELIMS-2018-2023.md`): the 2018 Prelims GS-I Q91 "
        "chronological-sequence question on post-independence India, which "
        "is embedded verbatim below with no option or answer inferred. The "
        "2025 GS-I Mains question on India's early consolidation is officially "
        "routed to the adjacent owner `basic/29_Colonial-Legacy-and-"
        "Foundations-of-the-Republic.md` in `_PYQ-ROUTING-MAINS-GS1-GS2-"
        "ESSAY-2024-2025.md`; it is referenced here only as an adjacent "
        "cross-topic application and is not claimed as an owned Mains demand "
        "of this topic.",
        [
            (
                "Planning Commission, 15 March 1950",
                "The Planning Commission was set up by a Cabinet resolution "
                "on 15 March 1950 with the Prime Minister as its ex officio "
                "chairman; it was an extra-constitutional body charged with "
                "assessing the country's resources and formulating Five Year "
                "Plans, and it must never be described as a constitutional "
                "authority.",
            ),
            (
                "First general election, 1951-52",
                "India's first general election was held between October "
                "1951 and February 1952 on universal adult franchise, with "
                "an electorate of roughly 173 million and a turnout of about "
                "46 per cent; Congress won a large parliamentary majority "
                "although its national vote share stayed well under half.",
            ),
            (
                "Community Development Programme, 1952",
                "The Community Development Programme was launched on 2 "
                "October 1952 to pursue rural reconstruction through "
                "block-level administration and local participation; it "
                "preceded the Balwantrai Mehta Committee's 1957 recommendation "
                "of Panchayati Raj and must not be treated as the same step.",
            ),
            (
                "Avadi session and the socialistic pattern, 1955",
                "At its Avadi session in January 1955 the Congress adopted "
                "the 'socialistic pattern of society' as its declared goal, "
                "meaning an expanding, dominant public sector inside a mixed "
                "economy rather than full state ownership of the means of "
                "production.",
            ),
            (
                "Industrial Policy Resolution, 1956",
                "The Industrial Policy Resolution of 1956 superseded the "
                "1948 Resolution and divided industry into Schedule A "
                "(exclusive state responsibility), Schedule B (state-led with "
                "private participation) and Schedule C (left to private "
                "enterprise), giving the public sector the economy's "
                "'commanding heights'.",
            ),
            (
                "Second Five Year Plan, 1956-61",
                "The Second Five Year Plan (1956-61), associated with P.C. "
                "Mahalanobis, prioritised heavy industry and capital-goods "
                "capacity; the emphasis built a substantial industrial base "
                "but left agricultural investment comparatively neglected, "
                "feeding into the food shortfalls of the mid-1960s.",
            ),
            (
                "Panchsheel, April 1954",
                "The Five Principles of Peaceful Coexistence, or Panchsheel, "
                "were signed with China in April 1954 alongside an agreement "
                "on Tibet; the friendship rhetoric this produced, captured in "
                "the slogan 'Hindi-Chini Bhai Bhai', preceded the same "
                "relationship's collapse into the October-November 1962 "
                "border war.",
            ),
            (
                "Bandung Conference, April 1955",
                "The Bandung Conference of April 1955 brought together "
                "twenty-nine Afro-Asian states around anti-colonialism and "
                "peaceful coexistence, with Nehru a leading voice alongside "
                "Sukarno, Nasser and Zhou Enlai; it was a precursor Afro-Asian "
                "gathering and not the founding summit of the Non-Aligned "
                "Movement.",
            ),
            (
                "Belgrade Conference and the founding of NAM, 1961",
                "The Belgrade Conference of September 1961 was the founding "
                "summit of the Non-Aligned Movement, with Nehru, Tito, Nasser, "
                "Sukarno and Nkrumah among its principal founders; "
                "non-alignment was framed as independent, positive engagement "
                "rather than passive neutrality.",
            ),
            (
                "Kerala, 1957: a communist government by ballot",
                "In the 1957 Kerala state election, held after the 1956 "
                "States Reorganisation, the Communist Party of India won and "
                "E.M.S. Namboodiripad became Chief Minister, an early instance "
                "anywhere of a communist government elected through the "
                "ballot rather than installed by revolution.",
            ),
            (
                "Goa, December 1961",
                "Goa, Daman and Diu remained under Portuguese rule after "
                "1947; when repeated diplomatic efforts for a peaceful "
                "transfer failed, Indian armed forces carried out Operation "
                "Vijay in December 1961, ending Portuguese rule within days "
                "and integrating the territories into the Union.",
            ),
            (
                "The Sino-Indian War, October-November 1962",
                "The Sino-Indian War of October-November 1962 along the "
                "Himalayan frontier produced Indian reverses in NEFA and "
                "Ladakh before China declared a unilateral ceasefire; the war "
                "exposed gaps in defence preparedness and forced a "
                "reassessment of the practical limits of non-alignment.",
            ),
            (
                "The Kamaraj Plan, 1963",
                "The Kamaraj Plan of 1963, proposed by K. Kamaraj, had senior "
                "Congress ministers and chief ministers resign their "
                "government posts to devote themselves to party organisational "
                "work; it was an organisational manoeuvre, not an economic "
                "plan, and must not be confused with the Five Year Plans.",
            ),
            (
                "Kashmir referred to the United Nations, 1948",
                "Nehru referred the Kashmir dispute to the United Nations in "
                "January 1948, leading to a ceasefire line by January 1949; "
                "the decision remains a debated element of his diplomatic "
                "legacy and should be presented as a contested choice rather "
                "than an unproblematic success.",
            ),
            (
                "Nehru's death and institutional legacy, 27 May 1964",
                "Jawaharlal Nehru died on 27 May 1964, after nearly "
                "seventeen years as Prime Minister; his institutional legacy "
                "of planning, parliamentary democracy, secularism and "
                "non-alignment endured, even as 1962 had already exposed the "
                "limits of strategic optimism built on Panchsheel and Bandung.",
            ),
            (
                "Congress dominance and 'one-party dominance', 1952-62",
                "Across the 1952, 1957 and 1962 general elections Congress "
                "won comfortable parliamentary majorities while its national "
                "vote share stayed well under 50 per cent, a first-past-the-"
                "post effect compounded by a fragmented opposition; this "
                "pattern is analysed in depth as the 'Congress system' in the "
                "companion party-politics topic.",
            ),
            (
                "Non-alignment as doctrine, not neutrality",
                "Nehru repeatedly distinguished non-alignment from passive "
                "neutrality: it meant judging each international question on "
                "its merits and engaging independently rather than joining "
                "either Cold War bloc, a doctrine formalised at Belgrade in "
                "1961 but articulated by Nehru from the late 1940s onward.",
            ),
            (
                "States Reorganisation, 1956, under Nehru",
                "The States Reorganisation Act of November 1956, enacted "
                "during Nehru's premiership, redrew India's internal map "
                "substantially on linguistic lines; its detailed chronology "
                "and consequences belong to the dedicated linguistic-"
                "reorganisation topic and are only cross-referenced here.",
            ),
            (
                "Hindi-Chini Bhai Bhai and the trap of hindsight",
                "The friendship slogan 'Hindi-Chini Bhai Bhai' popularised "
                "after 1954 must not be read backward as if the unresolved "
                "border dispute did not exist; the optimism of 1954-55 and "
                "the war of 1962 both belong to the same relationship and "
                "must be held together, not treated as contradictory facts.",
            ),
            (
                "Assessing the Nehru era: achievement and misjudgement",
                "A defensible verdict on the Nehru era holds together real "
                "institutional achievement, parliamentary democracy "
                "sustained, planning launched and non-alignment established, "
                "with the exposed strategic misjudgement of 1962, without "
                "letting either fact cancel the other.",
            ),
        ],
        [
            "Panchsheel (1954) and Bandung (1955) are distinct events; "
            "neither is the founding summit of the Non-Aligned Movement, "
            "which was founded at Belgrade in 1961.",
            "The Planning Commission was created by a Cabinet resolution, "
            "not by a constitutional amendment or Article.",
            "The Kamaraj Plan (1963) was an organisational manoeuvre inside "
            "Congress, not one of the Five Year Plans.",
            "The Community Development Programme (1952) predates and is "
            "distinct from the Panchayati Raj recommendations of 1957.",
            "Congress's parliamentary majorities of 1952, 1957 and 1962 "
            "rested on a vote share well under 50 per cent; do not equate a "
            "seat majority with a majority of votes cast.",
            "The Sino-Indian War ended with a unilaterally declared Chinese "
            "ceasefire, not a negotiated Indian victory.",
            "Nehru died on 27 May 1964; do not round this to 'mid-1964' or "
            "confuse it with the Kamaraj Plan's 1963 date.",
            "Goa was integrated through a military action (Operation Vijay, "
            "December 1961), unlike the largely negotiated accession of most "
            "princely states.",
            "'Congress system' or 'one-party dominance' is Rajni Kothari's "
            "analytical term; it is examined in the companion party-politics "
            "topic and should be attributed there, not asserted as a "
            "Congress self-description.",
            "Non-alignment is independent engagement on the merits of each "
            "question, not passive neutrality or non-involvement.",
            "Kerala's 1957 CPI government came to power by election, not by "
            "an insurrection; its later dismissal under Article 356 is a "
            "Polity-owner detail, not part of this topic's core claim.",
            "The Second Five Year Plan's heavy-industry emphasis is a "
            "documented investment priority; do not credit it with an "
            "agriculture-first strategy or state specific growth figures for "
            "it beyond what the owner records.",
        ],
        [
            (
                10,
                "Explain why the Planning Commission of 1950 is best "
                "described as an extra-constitutional instrument of economic "
                "coordination.",
                "The Commission was created by Cabinet resolution with the "
                "Prime Minister as chairman, giving planning administrative "
                "reach without constitutional status, which explains both "
                "its authority and its later criticism as unaccountable.",
                [0, 3, 4],
            ),
            (
                10,
                "Distinguish non-alignment from neutrality with reference "
                "to India's foreign policy between 1947 and 1961.",
                "Non-alignment meant independent, case-by-case engagement "
                "with international questions, formalised at Belgrade in "
                "1961, rather than a passive refusal to take positions.",
                [7, 8, 16],
            ),
            (
                15,
                "'Panchsheel and Bandung reflected an optimism that the war "
                "of 1962 exposed as premature.' Examine.",
                "The friendship diplomacy of 1954-55 built an Asian-"
                "solidarity narrative that the Sino-Indian border war of "
                "1962 revealed to have outrun India's actual strategic "
                "preparedness.",
                [6, 7, 11, 18],
            ),
            (
                15,
                "Discuss the significance of the 1957 Kerala election for "
                "assessing the depth of Nehruvian parliamentary democracy.",
                "A ballot-won communist state government functioning inside "
                "a Congress-dominated Centre is strong evidence that "
                "electoral competition, not merely single-party rule, was "
                "genuinely permitted under Nehru.",
                [9, 15],
            ),
            (
                20,
                "'Nehru's legacy combines durable institutional achievement "
                "with an exposed strategic misjudgement.' Evaluate.",
                "Parliamentary democracy, planning and non-alignment endured "
                "as institutions even as the 1962 war demonstrated the "
                "practical limits of the optimism built into non-alignment "
                "and border diplomacy.",
                [8, 11, 14, 15, 19],
            ),
            (
                20,
                "Trace the evolution of India's economic model under Nehru "
                "from the Planning Commission to the Second Five Year Plan "
                "and assess its long-term consequences.",
                "Cabinet-resolution planning, the socialistic pattern of "
                "1955 and the Industrial Policy Resolution of 1956 built a "
                "public-sector-led, heavy-industry economy whose "
                "agricultural neglect and later inefficiency required "
                "correction well beyond this period.",
                [0, 3, 4, 5],
            ),
        ],
        [],
        [
            "Planning Commission",
            "Panchsheel",
            "Bandung",
            "Belgrade",
            "Non-Aligned Movement",
            "Second Five Year Plan",
            "Kerala",
            "Goa",
            "Kamaraj Plan",
        ],
    ),
    base.topic(
        33,
        "Party Politics 1947\u201367: The Congress System & the Opposition",
        "33_Party-Politics-1947-67-Congress-System-and-Opposition.md",
        "33_Party-Politics-1947-67-Congress-System-and-Opposition.md",
        "33_Party-Politics-1947-67-Congress-System-and-Opposition_"
        "Complete-Topic-Package.md",
        [
            "basic/32_The-Nehru-Era-Hope-Foreign-Policy-and-Legacy.md",
            "basic/34_From-Shastri-to-Indira-1964-73.md",
            "basic/36_Janata-Interregnum-Indiras-Return-and-Regional-Crises.md",
            "32_The-Nehru-Era-Hope-Foreign-Policy-and-Legacy_"
            "Complete-Topic-Package.md",
        ],
        [],
        "No verified live current-affairs item is pegged to this topic. The "
        "owner's own material treats the Congress system and party "
        "fragmentation as an evergreen analytical theme rather than a dated "
        "news event, and that bounded framing is preserved rather than "
        "inventing a specific live source or date.",
        "The Basic and Advanced owner Markdown for this topic were "
        "reconciled against each other and against the folder's shared "
        "post-independence OCR source, Bipan Chandra, Mridula Mukherjee and "
        "Aditya Mukherjee, *India After Independence, 1947\u20132000*. Every "
        "date, name and institution used below already carries the owners' "
        "own \u2705 (source-backed) or \u26a0\ufe0f (inference) tagging, and "
        "that tagging is preserved rather than re-verified page by page "
        "against the raw PDF in this authoring pass.",
        "One Prelims demand is routed to this owner in the local ledgers "
        "(`_PYQ-ROUTING-PRELIMS-2024-2025.md`): the 2024 Prelims GS-I Q73 "
        "party-leader matching question (Jana Sangh, Socialist Party, CFD, "
        "Swatantra), which is embedded verbatim below with no option or "
        "answer inferred. No Mains demand in the local 2018-2025 ledgers is "
        "routed to this owner.",
        [
            (
                "The 1948 ban on dual party membership",
                "Congress amended its own constitution in 1948 to bar dual "
                "membership, targeting Congress Socialist Party members who "
                "sat inside Congress while also belonging to a separate "
                "organisation; forced to choose, most Socialist leaders left "
                "Congress and an independent Socialist Party was formed.",
            ),
            (
                "The Tandon-Nehru contest, 1950-51",
                "Purushottam Das Tandon defeated the Nehru-backed candidate "
                "for the Congress presidency in 1950; friction between "
                "Tandon's conservative leanings and Nehru's secular line led "
                "Tandon to resign in 1951, after which Nehru himself took "
                "over the party presidency.",
            ),
            (
                "The Bharatiya Jana Sangh, 1951",
                "The Bharatiya Jana Sangh was founded in 1951 by Syama "
                "Prasad Mookerjee, who had earlier resigned from Nehru's "
                "cabinet; the party had organisational links to the RSS "
                "network and stood for a Hindu-nationalist cultural-political "
                "line opposed to Congress's secular, planning-led model.",
            ),
            (
                "KMPP into the Praja Socialist Party, 1951-52",
                "J.B. Kripalani founded the Kisan Mazdoor Praja Party (KMPP) "
                "in 1951; in 1952 it merged with the Socialist Party to form "
                "the Praja Socialist Party (PSP), which itself split and "
                "re-formed repeatedly through the 1950s and 1960s.",
            ),
            (
                "The Swatantra Party, 1959",
                "The Swatantra Party was founded in 1959 by C. "
                "Rajagopalachari, Minoo Masani and N.G. Ranga on an "
                "economically conservative, free-market, anti-collectivisation "
                "platform directly opposed to Congress's 'socialistic "
                "pattern', and it became one of the larger non-Congress "
                "parliamentary parties by the 1960s.",
            ),
            (
                "The 1964 split in the Communist Party of India",
                "Ideological strain over the Sino-Soviet split and over "
                "differing responses to the 1962 border war split the "
                "Communist Party of India in 1964 into the CPI and the new "
                "CPI(M), leaving the organised Left divided rather than "
                "unified for the rest of the decade.",
            ),
            (
                "Rajni Kothari's 'Congress system'",
                "The political scientist Rajni Kothari coined the "
                "analytical term 'Congress system' to describe Congress as a "
                "'party of consensus' that absorbed internal factions, "
                "casting opposition parties as parties of 'pressure' rather "
                "than credible alternative governments; this is an "
                "analytical label, not a Congress self-description.",
            ),
            (
                "Seat majorities on a minority vote share",
                "In the 1952, 1957 and 1962 general elections Congress won "
                "comfortable parliamentary seat majorities while its "
                "national vote share stayed well under 50 per cent, a "
                "consequence of first-past-the-post arithmetic operating on "
                "a fragmented opposition rather than of majority consent "
                "alone.",
            ),
            (
                "The Socialist Party, 1948, and its founders",
                "The independent Socialist Party formed after the 1948 "
                "Congress exit was led by figures including Jayaprakash "
                "Narayan and Acharya Narendra Deva, giving India's "
                "non-Communist Left its first organised party distinct from "
                "Congress.",
            ),
            (
                "The CPI's 1948 Ranadive line and the Telangana uprising",
                "Between 1948 and 1951 the Communist Party of India pursued "
                "an insurrectionary line associated with B.T. Ranadive and "
                "tied to the armed Telangana peasant uprising, before "
                "abandoning armed struggle for parliamentary participation "
                "by 1951.",
            ),
            (
                "The DMK, founded 1949",
                "The Dravida Munnetra Kazhagam (DMK) was founded in 1949 by "
                "C.N. Annadurai as a Dravidian, anti-Hindi regional "
                "opposition party in Madras state, and it went on to form "
                "the state's first non-Congress government after the 1967 "
                "general election.",
            ),
            (
                "Congress's centralised ticket distribution",
                "Through the 1950s and 1960s the Congress high command and "
                "its state units controlled nomination and ticket "
                "distribution centrally, a mechanism that let the party "
                "manage internal factional competition without it spilling "
                "into separate parties as often as it might otherwise have "
                "done.",
            ),
            (
                "Multi-member and reserved constituencies, 1952 and 1957",
                "The 1952 and 1957 general elections used a mix of "
                "single-member and two-member constituencies, the latter "
                "reserved for Scheduled Castes or Scheduled Tribes, a "
                "structural feature of the era's electoral system distinct "
                "from the uniform single-member constituencies used from "
                "1962 onward.",
            ),
            (
                "Right-of-Congress parliamentary growth by 1962",
                "By the 1962 general election the Jana Sangh and the "
                "Swatantra Party had each secured a small but growing "
                "number of Lok Sabha seats, evidence that right-of-Congress "
                "opposition was gaining a parliamentary foothold even while "
                "Congress retained its overall majority.",
            ),
            (
                "Ram Manohar Lohia and 'non-Congressism'",
                "The Socialist leader Ram Manohar Lohia argued for "
                "'non-Congressism', a strategy of opposition unity against "
                "Congress even across ideological differences; the doctrine "
                "had little practical electoral effect before 1967 but "
                "prefigured the logic later used to build the Janata "
                "coalition of 1977.",
            ),
            (
                "Smaller Left formations: RSP and Forward Bloc",
                "The Revolutionary Socialist Party (RSP) and the Forward "
                "Bloc, strongest in Bengal and Kerala, added further "
                "plurality to a Left landscape that, alongside the CPI and "
                "CPI(M), was never a single unified bloc between 1947 and "
                "1967.",
            ),
            (
                "Congress as an umbrella organisation",
                "Congress functioned as a broad umbrella rather than an "
                "ideologically narrow party, holding Nehruvian planners, "
                "conservative traditionalists and regional bosses inside one "
                "organisation, so that much factional competition occurred "
                "inside Congress rather than between separate parties.",
            ),
            (
                "The rise of state-level 'Syndicate' bosses",
                "By the mid-1960s powerful state-level Congress leaders, "
                "later referred to as the 'Syndicate', had become "
                "organisationally decisive inside the party; this internal "
                "factional structure shapes the 1966 succession contest "
                "examined in the following topic.",
            ),
            (
                "Ideological range of the non-Congress opposition",
                "Between 1947 and 1967 the non-Congress opposition spanned "
                "the Hindu-nationalist Jana Sangh, the free-market "
                "Swatantra Party, several Socialist formations and a divided "
                "Communist movement, a genuine ideological range that could "
                "not translate into a single alternative to Congress before "
                "1967.",
            ),
            (
                "1967: the watershed foreshadowed",
                "The steady decline in Congress's vote share through 1952, "
                "1957 and 1962, together with two decades of splits, mergers "
                "and new party formations described in this topic, "
                "foreshadowed the 1967 general election, in which Congress "
                "lost power in eight states for the first time.",
            ),
        ],
        [
            "The Jana Sangh (1951) and the Swatantra Party (1959) are "
            "ideologically different right-of-Congress formations; do not "
            "conflate their founding dates or platforms.",
            "The Kisan Mazdoor Praja Party (1951) merged into the Praja "
            "Socialist Party in 1952; keep the sequence in that order.",
            "The Communist Party of India split in 1964, before the 1967 "
            "election, not after it.",
            "'Congress system' is Rajni Kothari's analytical term; always "
            "attribute it to Kothari and never present it as Congress's own "
            "description of itself.",
            "Tandon became Congress president in 1950 and resigned in 1951, "
            "after which Nehru took over; do not reverse this order.",
            "Congress's parliamentary majorities in the 1950s and early "
            "1960s rested on a vote share well under 50 per cent; a seat "
            "majority is not the same claim as a vote majority.",
            "The Socialists left Congress in 1948 because of the ban on "
            "dual membership, not primarily because of a sudden ideological "
            "rupture.",
            "Swatantra's free-market platform is the economic opposite of "
            "the Jana Sangh's cultural-nationalist platform; do not treat "
            "'right-of-Congress' as one ideological bloc.",
            "1967, not 1962, is the watershed election in which Congress "
            "actually lost power in several states.",
            "The CPI abandoned insurrectionary tactics for parliamentary "
            "participation by 1951, before the Sino-Soviet split of the "
            "early 1960s; do not date its turn to parliamentary politics to "
            "the 1964 split.",
            "The DMK was founded in 1949, well before the 1967 election in "
            "which it first formed a state government; founding and first "
            "victory are eighteen years apart, not simultaneous.",
            "Congress's centralised control of ticket distribution managed "
            "factional competition inside the party; it did not eliminate "
            "factional competition altogether.",
        ],
        [
            (
                10,
                "How did the 1948 ban on dual party membership shape the "
                "later development of India's opposition parties?",
                "By forcing Socialists out of Congress, the 1948 ban "
                "started the non-Communist Left's independent, and "
                "recurrently fragmented, organisational history outside the "
                "ruling party.",
                [0, 3, 8, 9],
            ),
            (
                10,
                "Distinguish the ideological platforms of the Jana Sangh "
                "and the Swatantra Party.",
                "The Jana Sangh's Hindu-nationalist cultural politics and "
                "Swatantra's free-market economic conservatism opposed "
                "Congress from different directions and should never be "
                "treated as a single ideological bloc.",
                [2, 4],
            ),
            (
                15,
                "Rajni Kothari's 'Congress system' explains one-party "
                "dominance without denying genuine political competition. "
                "Examine.",
                "Kothari's model shows factional competition occurring "
                "mainly inside Congress, with opposition parties acting as "
                "pressure groups rather than alternative governments, which "
                "is compatible with real, if bounded, competition.",
                [6, 7, 11, 12],
            ),
            (
                15,
                "Account for the instability of the non-Communist Left "
                "between 1948 and 1964.",
                "Repeated splits and mergers, from the 1948 Socialist exit "
                "through the KMPP-PSP merger to continual PSP divisions, "
                "show an ideological family unable to settle its "
                "organisational form.",
                [0, 3, 8, 9, 10],
            ),
            (
                20,
                "'Congress's parliamentary dominance between 1952 and 1967 "
                "rested on electoral arithmetic more than on political "
                "consensus.' Evaluate.",
                "First-past-the-post seat majorities on a minority vote "
                "share, combined with a fragmented opposition, better "
                "explain Congress dominance than any claim of near-universal "
                "political consensus.",
                [7, 12, 13, 14],
            ),
            (
                20,
                "Trace the fragmentation of India's opposition political "
                "landscape from 1948 to 1967 and assess its consequences "
                "for the 1967 general election.",
                "Two decades of bans, splits, mergers and new formations "
                "left a genuinely plural but disunited opposition whose "
                "slow consolidation, alongside Congress's declining vote "
                "share, produced the 1967 watershed.",
                [0, 2, 4, 5, 9, 14],
            ),
        ],
        [],
        [
            "Jana Sangh",
            "Swatantra Party",
            "Praja Socialist Party",
            "Congress system",
            "Rajni Kothari",
            "CPI(M)",
            "dual membership",
            "1967",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-32": [
        (
            "Planning without a constitutional mandate",
            "institution-map",
            """PLANNING COMMISSION -> CABINET RESOLUTION, 15 MARCH 1950 (not constitutional)
CHAIRMAN -> Prime Minister Jawaharlal Nehru, ex officio
MANDATE -> assess resources -> formulate Five Year Plans -> allocate priorities
FIRST PLAN 1951-56 -> agriculture and irrigation priority; modest, largely on track
TRAP -> extra-constitutional body; never call it a constitutional authority""",
            [
                "Planning without a constitutional mandate",
                "The 1951-52 general election and the shape of dominance",
            ],
        ),
        (
            "The 1951-52 general election",
            "data-table",
            """FIRST GENERAL ELECTION -> OCT 1951 to FEB 1952, staggered polling
ELECTORATE -> about 173 million voters; universal adult franchise, first time
TURNOUT -> roughly 46 per cent
RESULT -> big SEAT majority for Congress on a vote share WELL UNDER 50 per cent
READ IT CORRECTLY -> majority of SEATS, not majority of VOTES cast nationally""",
            ["The 1951-52 general election and the shape of dominance"],
        ),
        (
            "Community Development, 1952, before Panchayati Raj, 1957",
            "timeline",
            """COMMUNITY DEVELOPMENT PROGRAMME -> launched 2 OCTOBER 1952
AIM -> rural reconstruction through block-level administration + local participation
LATER STEP -> Balwantrai Mehta Committee, 1957, recommends Panchayati Raj
SEQUENCE -> CDP (1952) COMES BEFORE Panchayati Raj recommendations (1957)
TRAP -> do not treat CDP and Panchayati Raj as the same 1952 initiative""",
            ["Community Development and the promise of rural transformation"],
        ),
        (
            "Avadi, 1955, to the Second Plan, 1956-61",
            "causal-chain",
            """AVADI SESSION -> Indian National Congress, JANUARY 1955, near Madras
RESOLUTION -> adopts "SOCIALISTIC PATTERN OF SOCIETY" as its goal
MEANING -> mixed economy, dominant/expanding public sector, NOT full socialism
1956 -> INDUSTRIAL POLICY RESOLUTION gives it legal/administrative form
1956-61 -> SECOND FIVE YEAR PLAN (Mahalanobis) operationalises it in investment""",
            [
                "Avadi, 1955, and the socialistic pattern of society",
                "The Industrial Policy Resolution of 1956",
                "The Mahalanobis Second Plan: heavy industry over agriculture",
            ],
        ),
        (
            "The Industrial Policy Resolution, 1956: three schedules",
            "data-table",
            """INDUSTRIAL POLICY RESOLUTION -> 1956, supersedes the 1948 Resolution
+------------+------------------------------------------+
| SCHEDULE A | exclusive state responsibility            |
| SCHEDULE B | state-led, with private participation     |
| SCHEDULE C | left to private enterprise                |
+------------+------------------------------------------+
EFFECT -> "commanding heights" of the economy reserved for the public sector""",
            ["The Industrial Policy Resolution of 1956"],
        ),
        (
            "The Mahalanobis Second Plan and its neglected half",
            "comparison",
            """SECOND FIVE YEAR PLAN -> 1956-61, architect P.C. MAHALANOBIS
PRIORITISED -> heavy industry, capital goods ("machines that make machines")
BUILT -> a substantial domestic industrial base over the plan period
NEGLECTED -> agricultural investment, comparatively
CONSEQUENCE -> feeds into the food shortfalls of the mid-1960s (topic 34)""",
            ["The Mahalanobis Second Plan: heavy industry over agriculture"],
        ),
        (
            "Panchsheel, 1954, to the 1962 war",
            "timeline",
            """APRIL 1954 -> PANCHSHEEL signed with China, with a Tibet agreement
AFTER 1954 -> "Hindi-Chini Bhai Bhai" friendship rhetoric popularised
OCT-NOV 1962 -> the SAME relationship collapses into the Sino-Indian War
TRAP -> do not read 1954-55 optimism backward as if the border dispute did not exist""",
            [
                "Panchsheel, 1954, and its later collapse",
                "The Sino-Indian War, 1962: from Bhai Bhai to ceasefire",
            ],
        ),
        (
            "Bandung, 1955, is not Belgrade, 1961: precursor to doctrine",
            "comparison",
            """BANDUNG CONFERENCE -> APRIL 1955, Indonesia; 29 Afro-Asian states
ROLE -> precursor Afro-Asian gathering; NEHRU a leading voice
NOT THE SAME AS -> BELGRADE CONFERENCE, SEPTEMBER 1961
BELGRADE -> the actual FOUNDING SUMMIT of the Non-Aligned Movement
FOUNDERS AT BELGRADE -> Nehru, Tito, Nasser, Sukarno, Nkrumah
DOCTRINE THAT FOLLOWS -> judge each question on its merits; engage INDEPENDENTLY
NOT THIS -> passive neutrality or simple non-involvement
TRAP -> "non-alignment" and "neutrality" are NOT interchangeable terms""",
            [
                "Bandung, 1955: Afro-Asian solidarity before Belgrade",
                "Belgrade, 1961: the founding of the Non-Aligned Movement",
            ],
        ),
        (
            "Kerala, 1957: ballot, not revolution",
            "evidence-chain",
            """KERALA STATE ELECTION -> 1957, first after the 1956 States Reorganisation
RESULT -> Communist Party of India wins; E.M.S. NAMBOODIRIPAD, Chief Minister
SIGNIFICANCE -> among the earliest instances anywhere of an elected communist government
LATER (Polity owner, not here) -> Centre dismisses the ministry under Article 356
BOUNDARY -> this session stops at the 1957 election and its democratic significance""",
            ["Kerala, 1957: a communist government elected by ballot"],
        ),
        (
            "Goa, December 1961: diplomacy, then Operation Vijay",
            "causal-chain",
            """GOA, DAMAN AND DIU -> remained under Portuguese rule after 1947
STEP 1 -> repeated Indian diplomatic efforts for a peaceful transfer
STEP 2 -> diplomacy fails
STEP 3 -> OPERATION VIJAY, DECEMBER 1961: Indian armed forces move in
OUTCOME -> Portuguese rule ends within days; territories integrated into the Union""",
            ["Goa, December 1961: Operation Vijay"],
        ),
        (
            "1962: the pivot the whole topic turns on",
            "causal-chain",
            """OCT-NOV 1962 -> SINO-INDIAN WAR along the Himalayan frontier
COURSE -> Indian reverses in NEFA and Ladakh
END -> China declares a UNILATERAL CEASEFIRE (not a negotiated settlement)
EXPOSES -> gaps in defence preparedness; limits of non-alignment's optimism
1963 -> KAMARAJ PLAN: Congress responds organisationally, not economically""",
            [
                "The Sino-Indian War, 1962: from Bhai Bhai to ceasefire",
                "The Kamaraj Plan, 1963: reviving the party organisation",
            ],
        ),
        (
            "Nehru's legacy: institutions and lessons held together",
            "argument-map",
            """27 MAY 1964 -> Nehru dies, after nearly seventeen years as Prime Minister
ENDURING -> parliamentary democracy, planning, secularism, non-alignment
ALREADY TESTED -> 1962 exposed the limits of Panchsheel/Bandung-era optimism
UNRESOLVED, DEBATED -> the 1948 Kashmir referral to the United Nations
VERDICT -> real institutional achievement PAIRED WITH an exposed misjudgement""",
            [
                "Kashmir at the United Nations, 1948: a debated choice",
                "Nehru's legacy, 1964: institutions and lessons held together",
            ],
        ),
    ],
    "modern-indian-history-33": [
        (
            "The 1948 ban on dual party membership",
            "causal-chain",
            """CONGRESS CONSTITUTION -> amended 1948: BARS DUAL PARTY MEMBERSHIP
TARGET -> Congress Socialist Party (CSP) members inside Congress
FORCED CHOICE -> remain in Congress OR join an independent socialist party
RESULT -> most CSP leaders exit; an INDEPENDENT SOCIALIST PARTY is formed
CONSEQUENCE -> the non-Communist Left's long history OUTSIDE Congress begins""",
            ["The 1948 ban on dual party membership"],
        ),
        (
            "The Tandon-Nehru contest, 1950-51",
            "timeline",
            """1950 -> CONGRESS PRESIDENTIAL CONTEST: Tandon defeats the Nehru-backed candidate
1950-51 -> friction: Tandon's conservative-Hindu leanings vs Nehru's secular line
1951 -> TANDON RESIGNS the Congress presidency
1951 -> NEHRU HIMSELF then takes over as Congress president
TRAP -> do not reverse this order or compress it into a single year""",
            ["The Tandon-Nehru contest, 1950-51"],
        ),
        (
            "Jana Sangh, 1951, is not Swatantra, 1959",
            "comparison",
            """BHARATIYA JANA SANGH -> founded 1951, founder SYAMA PRASAD MOOKERJEE
LINK -> organisational links to the RSS network (state this carefully)
PLATFORM -> Hindu-nationalist cultural-political line
SWATANTRA PARTY -> founded 1959, founders RAJAGOPALACHARI / MASANI / RANGA
PLATFORM -> free-market, anti-collectivisation -> a DIFFERENT right-of-Congress line""",
            [
                "The Bharatiya Jana Sangh, 1951",
                "The Swatantra Party, 1959",
            ],
        ),
        (
            "KMPP, 1951, into the Praja Socialist Party, 1952",
            "timeline",
            """1951 -> KISAN MAZDOOR PRAJA PARTY (KMPP) founded, led by J.B. KRIPALANI
1952 -> KMPP MERGES WITH THE SOCIALIST PARTY
1952 -> PRAJA SOCIALIST PARTY (PSP) formed as a result
AFTER 1952 -> the PSP itself splits and re-forms repeatedly through the 1950s-60s""",
            ["KMPP into the Praja Socialist Party, 1951-52"],
        ),
        (
            "The 1964 split in the Communist Party of India",
            "causal-chain",
            """EARLY 1960s -> ideological strain: the Sino-Soviet split
SHARPENED BY -> differing responses to the 1962 border war
1964 -> THE COMMUNIST PARTY OF INDIA SPLITS
RESULT -> CPI (one stream) and the new CPI(M)
CONSEQUENCE -> the organised Left enters the mid-1960s divided, not unified""",
            ["The 1964 split in the Communist Party of India"],
        ),
        (
            "Rajni Kothari's 'Congress system'",
            "argument-map",
            """RAJNI KOTHARI -> political scientist, coins the term "CONGRESS SYSTEM"
CLAIM -> Congress functions as a "PARTY OF CONSENSUS", absorbing factions internally
OPPOSITION ROLE -> parties of "PRESSURE", not alternative-government contenders
ATTRIBUTION -> Kothari's analytical term, NOT a Congress self-description
BOUNDARY -> use only as an analytical lens on the evidence, never as fact-by-itself""",
            ["Rajni Kothari's 'Congress system'"],
        ),
        (
            "Seat majorities on a minority vote share",
            "data-table",
            """+-------+------------------------+---------------------------+
| YEAR  | CONGRESS SEAT RESULT    | CONGRESS NATIONAL VOTE    |
+-------+------------------------+---------------------------+
| 1952  | comfortable majority    | well under 50 per cent    |
| 1957  | comfortable majority    | well under 50 per cent    |
| 1962  | comfortable majority    | well under 50 per cent    |
+-------+------------------------+---------------------------+
MECHANISM -> first-past-the-post arithmetic acting on a fragmented opposition""",
            ["Seat majorities on a minority vote share"],
        ),
        (
            "The plural, fragmented Indian Left",
            "comparison",
            """CPI -> pro-Soviet stream after the 1964 split
CPI(M) -> the new formation after the 1964 split
RSP / FORWARD BLOC -> smaller formations, strongest in Bengal and Kerala
KERALA, 1957 -> the era's clearest Left electoral success (topic 32)
READ IT CORRECTLY -> "the Left" was NEVER a single unified bloc, 1947-67""",
            ["Smaller left formations and the plural Left"],
        ),
        (
            "Congress as an umbrella, not a narrow party",
            "institution-map",
            """CONGRESS ORGANISATION -> a broad UMBRELLA
CONTAINS -> Nehruvian planners + conservative traditionalists + regional bosses
MECHANISM -> factional competition happens INSIDE Congress, not mainly between parties
BY THE MID-1960s -> state-level "SYNDICATE" bosses become organisationally decisive
LINK FORWARD -> this factionalism shapes the 1966 succession contest (topic 34)""",
            [
                "Congress as an umbrella organisation",
                "The rise of state-level 'Syndicate' bosses",
            ],
        ),
        (
            "Lohia's 'non-Congressism': a doctrine ahead of its time",
            "causal-chain",
            """RAM MANOHAR LOHIA -> leading Socialist figure, critic of Congress dominance
DOCTRINE -> "NON-CONGRESSISM": unite the opposition against Congress, despite ideology
1947-67 -> little practical electoral effect
1977 -> the SAME logic underlies the Janata coalition (topic 36)
TRAP -> do not claim non-Congressism succeeded electorally within this topic's period""",
            ["Ram Manohar Lohia and 'non-Congressism'"],
        ),
        (
            "The opposition's ideological range, 1947-67",
            "data-table",
            """+------------------+---------------------------------------------+
| PARTY/STREAM     | CORE POSITION                                |
+------------------+---------------------------------------------+
| Jana Sangh (1951) | Hindu-nationalist cultural politics          |
| Swatantra (1959)  | free-market economic conservatism            |
| PSP and streams   | non-Communist socialist politics             |
| CPI / CPI(M)      | organised communism, split from 1964         |
+------------------+---------------------------------------------+
PROBLEM -> real range, but FRAGMENTED, not unified, before 1967""",
            ["The ideological range of the non-Congress opposition"],
        ),
        (
            "1967: the watershed this whole topic foreshadows",
            "timeline",
            """1948-1964 -> ban, splits, mergers, new parties reshape the opposition
1952 / 1957 / 1962 -> Congress SEAT majority stays large; VOTE SHARE keeps declining
1964 -> CPI splits into CPI/CPI(M)
1967 -> for the FIRST TIME, Congress loses power in EIGHT STATES
READ THE THREAD -> 1967 is the payoff of two decades of party-system change""",
            ["1967: the watershed foreshadowed"],
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
    "modern-indian-history-32": [
        authored_session(
            "Planning without a constitutional mandate",
            "The Planning Commission of 1950 is the starting institution of "
            "this topic: it gave the state a permanent machinery for "
            "economic coordination without ever being written into the "
            "Constitution.",
            [
                "The Commission was created by a Cabinet resolution on 15 "
                "March 1950, not by a constitutional amendment or article.",
                "The Prime Minister served as its ex officio chairman, "
                "fusing political authority with technical planning.",
                "Its mandate was to assess national resources and formulate "
                "Five Year Plans allocating investment priorities.",
            ],
            "Never call the Planning Commission a constitutional body; it "
            "was an executive creation that could be, and eventually was, "
            "replaced by executive order alone (NITI Aayog, a Polity-owner "
            "detail).",
            "Use this session to answer any 'basis of planning' question by "
            "naming the 1950 Cabinet resolution rather than a constitutional "
            "article.",
            """PLANNING COMMISSION -> CABINET RESOLUTION, 15 MARCH 1950 (not constitutional)
CHAIRMAN -> Prime Minister, ex officio
MANDATE -> assess resources -> formulate Five Year Plans -> allocate priorities
TRAP -> extra-constitutional body; never call it a constitutional authority""",
            "The Planning Commission is the executive body, created by "
            "Cabinet resolution on 15 March 1950 with the Prime Minister as "
            "chairman, that assessed national resources and formulated "
            "India's Five Year Plans.",
        ),
        authored_session(
            "The 1951-52 general election and the shape of dominance",
            "India's first general election converted universal adult "
            "franchise from a constitutional promise into a working "
            "institution, and it set the electoral pattern, large seat "
            "majorities on a modest vote share, that would define the next "
            "decade and a half.",
            [
                "Polling ran from October 1951 to February 1952 across a "
                "staggered schedule, with an electorate of about 173 "
                "million.",
                "Turnout was roughly 46 per cent, a large-scale exercise "
                "without precedent anywhere at that time.",
                "Congress won a comfortable parliamentary majority although "
                "its national vote share remained well under 50 per cent.",
            ],
            "Keep 'majority of seats' and 'majority of votes' analytically "
            "separate; conflating them is the most common Prelims trap on "
            "this election.",
            "Use the vote-share gap to answer any 'was Congress dominance "
            "consensual' Mains demand together with the party-politics "
            "topic's seat-versus-vote analysis.",
            """FIRST GENERAL ELECTION -> OCT 1951 to FEB 1952, staggered polling
ELECTORATE -> about 173 million; universal adult franchise, first time
TURNOUT -> roughly 46 per cent
RESULT -> big SEAT majority for Congress on a vote share WELL UNDER 50 per cent""",
            "The 1951-52 general election is India's first exercise of "
            "universal adult franchise, held in stages from October 1951 to "
            "February 1952, in which Congress won a large parliamentary "
            "majority on a modest national vote share.",
        ),
        authored_session(
            "Community Development and the promise of rural transformation",
            "The Community Development Programme was the Nehru era's first "
            "systematic attempt to reach rural India through administration "
            "rather than through land reform alone, and its 1952 launch must "
            "be kept chronologically distinct from the later Panchayati Raj "
            "recommendation.",
            [
                "The Programme was launched on 2 October 1952 to pursue "
                "rural reconstruction through block-level administration and "
                "local participation.",
                "It preceded the Balwantrai Mehta Committee's 1957 "
                "recommendation that local self-government be organised as "
                "Panchayati Raj.",
                "The two steps are related but distinct: administrative "
                "block development first, elected local government second.",
            ],
            "Do not describe the 1952 Community Development Programme and "
            "1957 Panchayati Raj recommendation as a single 1952 initiative.",
            "Use the 1952-to-1957 sequence to answer any question asking "
            "for the origin of India's rural local-government architecture.",
            """COMMUNITY DEVELOPMENT PROGRAMME -> launched 2 OCTOBER 1952
AIM -> rural reconstruction via block-level administration + local participation
LATER STEP -> Balwantrai Mehta Committee, 1957, recommends Panchayati Raj
TRAP -> do not treat the 1952 Programme and 1957 recommendation as one event""",
            "The Community Development Programme is the rural-reconstruction "
            "initiative launched on 2 October 1952 that organised "
            "development through block-level administration ahead of the "
            "later, separate Panchayati Raj recommendation of 1957.",
        ),
        authored_session(
            "Avadi, 1955, and the socialistic pattern of society",
            "At Avadi, Congress converted a decade of planning rhetoric into "
            "a formal party goal, giving the Second Plan's heavy-industry "
            "emphasis and the 1956 Industrial Policy Resolution their "
            "ideological label.",
            [
                "The Avadi session of January 1955 adopted the 'socialistic "
                "pattern of society' as Congress's declared goal.",
                "The phrase meant an expanding, dominant public sector inside "
                "a continuing mixed economy, not full state ownership.",
                "The goal was operationalised almost immediately through the "
                "Second Plan (1956-61) and the Industrial Policy Resolution "
                "of 1956.",
            ],
            "Do not read 'socialistic pattern' as a claim to full "
            "socialism; the private sector continued to exist throughout.",
            "Use Avadi to date the ideological label precisely when a "
            "question asks when Congress formally adopted its economic goal.",
            """AVADI SESSION -> Indian National Congress, JANUARY 1955, near Madras
RESOLUTION -> adopts "SOCIALISTIC PATTERN OF SOCIETY" as its goal
MEANING -> mixed economy, dominant/expanding public sector, NOT full socialism
FOLLOWS INTO -> Second Plan (1956-61) and Industrial Policy Resolution (1956)""",
            "The 'socialistic pattern of society' is the goal Congress "
            "adopted at its Avadi session in January 1955, committing the "
            "party to an expanding public sector inside a continuing mixed "
            "economy.",
        ),
        authored_session(
            "The Industrial Policy Resolution of 1956",
            "The 1956 Resolution gave Avadi's goal legal and administrative "
            "form, sorting industry into three schedules and handing the "
            "public sector the economy's commanding heights.",
            [
                "The Resolution superseded the 1948 Industrial Policy "
                "Resolution.",
                "Schedule A reserved sectors exclusively for the state; "
                "Schedule B allowed state-led activity with private "
                "participation; Schedule C was left to private enterprise.",
                "The design gave the public sector the 'commanding heights' "
                "of heavy industry and infrastructure.",
            ],
            "Keep the three schedules (A, B, C) distinct; a question naming "
            "a sector is usually testing which schedule it fell into.",
            "Use the schedule structure to answer any question on how "
            "public- and private-sector roles were formally divided after "
            "1956.",
            """INDUSTRIAL POLICY RESOLUTION -> 1956, supersedes the 1948 Resolution
SCHEDULE A -> exclusive state responsibility (heavy industry, key sectors)
SCHEDULE B -> state-led with private participation
SCHEDULE C -> left to private enterprise
EFFECT -> "commanding heights" of the economy reserved for the public sector""",
            "The Industrial Policy Resolution of 1956 is the policy "
            "instrument that divided industry into three schedules and gave "
            "the public sector the economy's commanding heights.",
        ),
        authored_session(
            "The Mahalanobis Second Plan: heavy industry over agriculture",
            "The Second Plan converted the socialistic pattern into an "
            "investment strategy, and its heavy-industry priority is the "
            "single fact most often tested alongside its neglected "
            "counterpart, agriculture.",
            [
                "The Second Five Year Plan (1956-61) is associated with "
                "P.C. Mahalanobis and prioritised heavy industry and "
                "capital-goods capacity.",
                "The strategy built a substantial domestic industrial base "
                "over the plan period.",
                "Agricultural investment was comparatively neglected, "
                "feeding into the food shortfalls of the mid-1960s.",
            ],
            "Do not credit the Second Plan with an agriculture-first "
            "strategy, and do not state specific growth figures beyond what "
            "the owner records.",
            "Use the heavy-industry-versus-agriculture contrast to answer "
            "any 'assess the Second Plan' Mains demand with a graded, not a "
            "purely celebratory, verdict.",
            """SECOND FIVE YEAR PLAN -> 1956-61, architect P.C. MAHALANOBIS
PRIORITY -> heavy industry and capital goods ("machines that make machines")
RESULT -> substantial industrial base built; agriculture comparatively neglected
CONSEQUENCE -> feeds into the food shortfalls of the mid-1960s (topic 34)""",
            "The Mahalanobis Second Plan (1956-61) is the Five Year Plan "
            "that prioritised heavy industry and capital-goods capacity over "
            "agricultural investment.",
        ),
        authored_session(
            "Panchsheel, 1954, and its later collapse",
            "Panchsheel is the diplomatic starting point of the Nehru era's "
            "China relationship, and this session deliberately holds its "
            "1954 optimism and its 1962 collapse together rather than "
            "letting one erase the other.",
            [
                "The Five Principles of Peaceful Coexistence, or Panchsheel, "
                "were signed with China in April 1954 alongside an agreement "
                "on Tibet.",
                "The friendship rhetoric that followed is captured in the "
                "slogan 'Hindi-Chini Bhai Bhai'.",
                "The same relationship deteriorated into the "
                "October-November 1962 border war within less than a "
                "decade.",
            ],
            "Do not read 1954-55 optimism backward as if the unresolved "
            "border dispute did not already exist.",
            "Use the 1954-to-1962 arc to answer any question testing "
            "whether India's China policy under Nehru was naive or merely "
            "unlucky.",
            """PANCHSHEEL -> Five Principles of Peaceful Coexistence, signed with China, APRIL 1954
CONTEXT -> Sino-Indian agreement on Tibet trade and intercourse
SLOGAN -> "Hindi-Chini Bhai Bhai" popularises friendship rhetoric after 1954
LATER -> the same relationship deteriorates into the OCT-NOV 1962 war""",
            "Panchsheel is the set of Five Principles of Peaceful "
            "Coexistence signed with China in April 1954 alongside an "
            "agreement on Tibet, the diplomatic starting point of a "
            "relationship that later produced the 1962 war.",
        ),
        authored_session(
            "Bandung, 1955: Afro-Asian solidarity before Belgrade",
            "Bandung is frequently confused with the founding of the "
            "Non-Aligned Movement; this session fixes it instead as a "
            "precursor Afro-Asian gathering distinct from Belgrade in 1961.",
            [
                "The Bandung Conference of April 1955 brought together "
                "twenty-nine Afro-Asian states around anti-colonialism and "
                "peaceful coexistence.",
                "Nehru was a leading voice at Bandung alongside Sukarno, "
                "Nasser and Zhou Enlai.",
                "Bandung was a precursor Afro-Asian conference, not the "
                "founding summit of the Non-Aligned Movement, which came "
                "later at Belgrade in 1961.",
            ],
            "Never call Bandung the founding conference of the Non-Aligned "
            "Movement; that status belongs only to Belgrade, 1961.",
            "Use the Bandung-then-Belgrade sequence to answer any question "
            "asking which conference actually founded the Non-Aligned "
            "Movement.",
            """BANDUNG CONFERENCE -> APRIL 1955, Indonesia; 29 Afro-Asian states
THEME -> anti-colonialism, racial equality, peaceful coexistence
NEHRU'S ROLE -> leading voice alongside Sukarno, Nasser, Zhou Enlai
RELATION TO NAM -> a PRECURSOR gathering, NOT the founding summit
NEXT STEP -> Belgrade, 1961, formally founds the Non-Aligned Movement""",
            "The Bandung Conference of April 1955 is the Afro-Asian gathering "
            "on anti-colonialism and peaceful coexistence that preceded, but "
            "did not itself found, the Non-Aligned Movement.",
        ),
        authored_session(
            "Belgrade, 1961: the founding of the Non-Aligned Movement",
            "Belgrade is the precise founding moment this topic needs "
            "candidates to name, and it also fixes non-alignment's real "
            "meaning as independent engagement rather than passive "
            "neutrality.",
            [
                "The Belgrade Conference of September 1961 was the founding "
                "summit of the Non-Aligned Movement.",
                "Nehru, Tito, Nasser, Sukarno and Nkrumah were among its "
                "principal founders.",
                "Non-alignment was framed as independent, positive "
                "engagement on the merits of each question, not passive "
                "neutrality or non-involvement.",
            ],
            "Do not describe non-alignment as simple neutrality; it is an "
            "active, case-by-case doctrine of engagement.",
            "Use Belgrade's founder list and doctrine statement together "
            "whenever a question asks for the origin or meaning of "
            "non-alignment.",
            """BELGRADE CONFERENCE -> SEPTEMBER 1961, founding summit of the NON-ALIGNED MOVEMENT
FOUNDERS -> Nehru (India), Tito (Yugoslavia), Nasser (Egypt), Sukarno (Indonesia), Nkrumah (Ghana)
DOCTRINE -> independent engagement, NOT passive neutrality
DISTINCT FROM -> Bandung 1955, a preparatory Afro-Asian conference only""",
            "The Belgrade Conference of September 1961 is the founding "
            "summit of the Non-Aligned Movement, at which Nehru, Tito, "
            "Nasser, Sukarno and Nkrumah defined non-alignment as "
            "independent engagement rather than passive neutrality.",
        ),
        authored_session(
            "Kerala, 1957: a communist government elected by ballot",
            "Kerala's 1957 election is the clearest evidence this topic "
            "offers that Nehru's parliamentary democracy tolerated genuine "
            "alternation, not merely permitted opposition to exist on "
            "paper.",
            [
                "The 1957 Kerala state election, the first after the 1956 "
                "States Reorganisation, was won by the Communist Party of "
                "India.",
                "E.M.S. Namboodiripad became Chief Minister, an early "
                "instance anywhere of a communist government elected "
                "through the ballot.",
                "The government functioned initially before its later "
                "dismissal under Article 356, a detail that belongs to the "
                "Polity owner rather than to this topic's core claim.",
            ],
            "Do not extend this session into the details of the later "
            "Article 356 dismissal; keep the claim bounded to the 1957 "
            "election and its democratic significance.",
            "Use Kerala 1957 to answer any question testing whether "
            "Congress dominance was compatible with real electoral "
            "competition at the state level.",
            """KERALA STATE ELECTION -> 1957, first election after the 1956 States Reorganisation
RESULT -> Communist Party of India wins; E.M.S. NAMBOODIRIPAD becomes Chief Minister
SIGNIFICANCE -> among the earliest instances anywhere of a communist government via ballot
LATER (Polity owner) -> Centre later dismisses the ministry under Article 356""",
            "Kerala 1957 refers to the state election in which the "
            "Communist Party of India, under E.M.S. Namboodiripad, formed a "
            "government through the ballot, an early instance anywhere of "
            "an elected communist government.",
        ),
        authored_session(
            "Goa, December 1961: Operation Vijay",
            "Goa's integration is the one episode in this topic settled by "
            "military rather than negotiated means, and that distinction is "
            "itself the exam-relevant point.",
            [
                "Goa, Daman and Diu remained under Portuguese rule after "
                "1947 despite repeated Indian diplomatic efforts for a "
                "peaceful transfer.",
                "Indian armed forces carried out Operation Vijay in December "
                "1961 after diplomacy failed.",
                "Portuguese rule ended within days, and the territories were "
                "integrated into the Union.",
            ],
            "Do not describe Goa's integration using the same largely "
            "negotiated framework used for most princely-state accessions; "
            "this was a military action.",
            "Use the diplomacy-first-then-military-action sequence to "
            "answer any question on how Goa differed from the general "
            "pattern of post-1947 territorial integration.",
            """GOA, DAMAN AND DIU -> remained under Portuguese rule after 1947
DIPLOMACY FIRST -> repeated Indian efforts for a peaceful transfer fail
OPERATION VIJAY -> DECEMBER 1961, Indian armed forces move in
OUTCOME -> Portuguese rule ends within days; territories integrated into the Union""",
            "Operation Vijay is the December 1961 Indian military action "
            "that ended Portuguese rule in Goa, Daman and Diu after "
            "diplomatic efforts for a peaceful transfer had failed.",
        ),
        authored_session(
            "The Sino-Indian War, 1962: from Bhai Bhai to ceasefire",
            "This session is the pivot of the entire topic: it is where "
            "Panchsheel's optimism, the Second Plan's priorities and "
            "non-alignment's doctrine are all tested at once by a single "
            "military event.",
            [
                "The Sino-Indian War of October-November 1962 was fought "
                "along the Himalayan frontier.",
                "Indian forces suffered reverses in NEFA and Ladakh before "
                "China declared a unilateral ceasefire.",
                "The war exposed gaps in defence preparedness and forced a "
                "reassessment of the practical limits of non-alignment.",
            ],
            "Do not describe the war's end as a negotiated Indian victory; "
            "the ceasefire was declared unilaterally by China.",
            "Use 1962 as the hinge event whenever a question asks what "
            "exposed the limits of Nehru-era diplomacy and defence policy.",
            """SINO-INDIAN WAR -> OCTOBER-NOVEMBER 1962, along the Himalayan frontier
COURSE -> Indian reverses in NEFA and Ladakh
END -> China declares a UNILATERAL CEASEFIRE (not a negotiated settlement)
CONSEQUENCE -> exposes gaps in defence preparedness; reassesses non-alignment's limits""",
            "The Sino-Indian War of October-November 1962 is the border "
            "conflict, ended by a unilateral Chinese ceasefire, that exposed "
            "gaps in India's defence preparedness and the practical limits "
            "of non-alignment.",
        ),
        authored_session(
            "The Kamaraj Plan, 1963: reviving the party organisation",
            "The Kamaraj Plan shows Congress responding organisationally to "
            "the strain of 1962, and it is one of the most commonly "
            "mislabelled facts in this topic because of its name.",
            [
                "The Kamaraj Plan of 1963 was proposed by K. Kamaraj.",
                "It had senior Congress ministers and chief ministers resign "
                "their government posts to devote themselves to party "
                "organisational work.",
                "It was an organisational manoeuvre inside Congress, not an "
                "economic plan, and must not be confused with the Five Year "
                "Plans.",
            ],
            "Never classify the Kamaraj Plan alongside the First, Second or "
            "Third Five Year Plans; its subject is party organisation, not "
            "the economy.",
            "Use the Kamaraj Plan to answer any question on how Congress "
            "tried to renew itself organisationally in the early 1960s.",
            """KAMARAJ PLAN -> 1963, proposed by K. KAMARAJ
MECHANISM -> senior ministers and chief ministers RESIGN government posts
PURPOSE -> devote themselves to Congress PARTY organisational work
TRAP -> an organisational manoeuvre, NOT one of the Five Year Plans""",
            "The Kamaraj Plan of 1963 is K. Kamaraj's proposal that senior "
            "Congress ministers resign their government posts to strengthen "
            "the party's organisational work.",
        ),
        authored_session(
            "Kashmir at the United Nations, 1948: a debated choice",
            "This session treats Nehru's most contested diplomatic decision "
            "with appropriate restraint, stating only the referral and its "
            "immediate sequel rather than adjudicating the wider dispute.",
            [
                "Nehru referred the Kashmir dispute to the United Nations "
                "in January 1948.",
                "A ceasefire line was established by January 1949.",
                "The decision remains a debated element of Nehru's "
                "diplomatic legacy and should be presented as contested "
                "rather than as an unproblematic success.",
            ],
            "Do not present the 1948 UN referral as either an obvious "
            "success or an obvious failure; state the fact and its "
            "contested status without adjudicating the merits.",
            "Use this session only to answer the narrow factual question of "
            "when and how Kashmir reached the United Nations, not broader "
            "Kashmir-policy questions that belong elsewhere.",
            """KASHMIR AT THE UNITED NATIONS -> Nehru refers the dispute, JANUARY 1948
SEQUEL -> a ceasefire line is established by JANUARY 1949
STATUS -> a DEBATED element of Nehru's diplomatic legacy
BOUNDARY -> state the referral and its date; do not adjudicate the wider dispute""",
            "The 1948 Kashmir referral is Nehru's decision to bring the "
            "Kashmir dispute before the United Nations in January 1948, "
            "leading to a ceasefire line by January 1949 and remaining a "
            "debated element of his legacy.",
        ),
        authored_session(
            "Nehru's legacy, 1964: institutions and lessons held together",
            "The closing session states the graded verdict this whole "
            "topic has been building toward: real institutions endured "
            "alongside a real, exposed misjudgement, and neither fact "
            "should be allowed to cancel the other.",
            [
                "Jawaharlal Nehru died on 27 May 1964, after nearly "
                "seventeen years as Prime Minister.",
                "His institutional legacy of planning, parliamentary "
                "democracy, secularism and non-alignment endured beyond his "
                "death.",
                "The optimism built into Panchsheel, Bandung and "
                "non-alignment had already been tested, and found wanting in "
                "part, by the 1962 war.",
            ],
            "Do not let 1962's exposed misjudgement erase the genuine "
            "institutional achievement, or let the institutional achievement "
            "excuse the misjudgement; state both together.",
            "Use this session to close any 20-mark 'assess Nehru's legacy' "
            "answer with a graded, evidence-based verdict rather than a "
            "purely celebratory or purely critical one.",
            """NEHRU'S DEATH -> 27 MAY 1964, after nearly seventeen years as Prime Minister
ENDURING -> parliamentary democracy, planning, secularism, non-alignment
ALREADY TESTED -> 1962 exposed limits of Panchsheel/Bandung-era optimism
VERDICT -> real institutional achievement PAIRED WITH an exposed strategic misjudgement""",
            "Nehru's legacy, closed by his death on 27 May 1964, combines "
            "the enduring institutions of planning, parliamentary democracy "
            "and non-alignment with the strategic misjudgement that the 1962 "
            "war exposed.",
        ),
    ],
    "modern-indian-history-33": [
        authored_session(
            "Congress's dominant position at Independence, 1947",
            "This orientation session states the starting condition the "
            "whole topic explains: Congress inherited a uniquely dominant, "
            "broad-based organisational position in 1947, and everything "
            "that follows is about how party politics operated inside and "
            "against that dominance through 1967.",
            [
                "Congress entered independence as the only truly all-India "
                "party, with a mass organisational network built across "
                "decades of the freedom movement.",
                "No rival party in 1947 had comparable organisational "
                "reach, cadre strength or claim to the freedom struggle's "
                "legacy.",
                "This dominance set the terms on which every subsequent "
                "split, ban, merger and new party of 1948-1967 had to "
                "compete.",
            ],
            "Do not treat 1947 Congress dominance as permanent or "
            "uncontested; the rest of this topic traces how it was "
            "contested from within and without.",
            "Use this session to open any answer on Congress dominance or "
            "the post-1947 party system by first stating the 1947 starting "
            "condition.",
            """1947 -> CONGRESS the only truly ALL-INDIA party, mass organisation
LEGACY -> decades of freedom-movement organisational reach and cadre strength
NO RIVAL -> no other 1947 party had comparable reach or nationalist legacy
CONSEQUENCE -> every 1948-1967 split, ban, merger, new party competes against this
FRAME -> this topic traces contestation of dominance, not permanent dominance""",
            "Congress's 1947 dominant position is its unmatched all-India "
            "organisational reach and freedom-movement legacy at "
            "independence, the starting condition against which every "
            "later split, ban, merger and new party in this topic is read.",
        ),
        authored_session(
            "The 1948 ban on dual party membership",
            "This session opens the topic at its true starting point: a "
            "Congress constitutional rule, not an external event, that "
            "created India's independent non-Communist Left.",
            [
                "Congress amended its own constitution in 1948 to bar dual "
                "party membership.",
                "The rule targeted Congress Socialist Party members who sat "
                "inside Congress while belonging to a separate organisation.",
                "Forced to choose, most Socialist leaders left Congress and "
                "an independent Socialist Party was formed.",
            ],
            "Do not describe the 1948 Socialist exit as a spontaneous "
            "ideological break; it followed directly from the dual-"
            "membership ban.",
            "Use this session to answer any question on the origin of "
            "India's independent Socialist party tradition.",
            """CONGRESS CONSTITUTION -> amended 1948: BARS DUAL PARTY MEMBERSHIP
TARGET -> Congress Socialist Party (CSP) members inside Congress
FORCED CHOICE -> remain in Congress OR join an independent socialist party
RESULT -> most CSP leaders exit; an INDEPENDENT SOCIALIST PARTY is formed""",
            "The 1948 dual-membership ban is the Congress constitutional "
            "amendment that forced Congress Socialist Party members to "
            "choose between Congress and an independent party, producing "
            "the Socialist exit of 1948.",
        ),
        authored_session(
            "The Tandon-Nehru contest, 1950-51",
            "This session traces Congress's own internal leadership contest "
            "to show that factional competition operated inside the party "
            "even at its highest level.",
            [
                "Purushottam Das Tandon defeated the Nehru-backed candidate "
                "for the Congress presidency in 1950.",
                "Friction between Tandon's conservative-Hindu leanings and "
                "Nehru's secular line grew through 1950-51.",
                "Tandon resigned the Congress presidency in 1951, after "
                "which Nehru himself took over the post.",
            ],
            "Keep the sequence exact: Tandon wins in 1950, resigns in 1951, "
            "then Nehru takes over; do not reverse or compress this order.",
            "Use this contest to answer any question on internal ideological "
            "tension inside Congress in its first years of power.",
            """CONGRESS PRESIDENTIAL CONTEST -> 1950
WINNER -> PURUSHOTTAM DAS TANDON defeats the Nehru-backed candidate
FRICTION -> Tandon's conservative-Hindu leanings clash with Nehru's secular line
1951 -> TANDON RESIGNS; NEHRU HIMSELF then takes over as Congress president""",
            "The Tandon-Nehru contest refers to Purushottam Das Tandon's "
            "1950 election as Congress president, his 1951 resignation "
            "amid friction with Nehru, and Nehru's subsequent assumption of "
            "the post.",
        ),
        authored_session(
            "The Bharatiya Jana Sangh, 1951",
            "The Jana Sangh's founding introduces the Hindu-nationalist "
            "strand of opposition politics, and this session fixes its "
            "founder, date and organisational link precisely.",
            [
                "The Bharatiya Jana Sangh was founded in 1951.",
                "Its founder, Syama Prasad Mookerjee, had earlier resigned "
                "from Nehru's cabinet.",
                "The party had organisational links to the RSS network and "
                "stood for a Hindu-nationalist cultural-political line "
                "opposed to Congress's secular, planning-led model.",
            ],
            "Do not confuse the Jana Sangh (1951, Mookerjee) with the "
            "Swatantra Party (1959, Rajagopalachari); they are different "
            "right-of-Congress formations with different platforms.",
            "Use this session to answer any question naming the founder or "
            "founding year of the Jana Sangh.",
            """BHARATIYA JANA SANGH -> founded 1951
FOUNDER -> SYAMA PRASAD MOOKERJEE (resigned from Nehru's cabinet)
LINK -> organisational links to the RSS network (state this carefully)
PLATFORM -> Hindu-nationalist cultural-political line, opposed to Congress's model""",
            "The Bharatiya Jana Sangh is the party founded in 1951 by Syama "
            "Prasad Mookerjee on a Hindu-nationalist cultural-political "
            "platform, organisationally linked to the RSS network.",
        ),
        authored_session(
            "KMPP into the Praja Socialist Party, 1951-52",
            "This session tracks the non-Communist Left's first major "
            "merger, establishing the pattern of instability that recurs "
            "throughout the rest of the topic.",
            [
                "J.B. Kripalani founded the Kisan Mazdoor Praja Party "
                "(KMPP) in 1951.",
                "In 1952 the KMPP merged with the Socialist Party.",
                "The merger created the Praja Socialist Party (PSP), which "
                "itself split and re-formed repeatedly through the 1950s "
                "and 1960s.",
            ],
            "Keep the sequence exact: KMPP founded 1951, merger and PSP "
            "formed 1952; do not present PSP as founded directly in 1951.",
            "Use this merger to answer any question on the organisational "
            "instability of India's non-Communist Left before 1967.",
            """KISAN MAZDOOR PRAJA PARTY (KMPP) -> founded 1951, led by J.B. KRIPALANI
1952 -> KMPP MERGES WITH THE SOCIALIST PARTY
RESULT -> PRAJA SOCIALIST PARTY (PSP) formed, 1952
INSTABILITY -> the PSP itself splits and re-forms repeatedly through the 1950s-60s""",
            "The Praja Socialist Party (PSP) is the party formed in 1952 "
            "from the merger of J.B. Kripalani's 1951 Kisan Mazdoor Praja "
            "Party with the Socialist Party.",
        ),
        authored_session(
            "The Swatantra Party, 1959",
            "Swatantra's founding introduces the free-market strand of "
            "opposition politics, deliberately positioned opposite the "
            "Jana Sangh's cultural platform and opposite Congress's "
            "socialistic pattern.",
            [
                "The Swatantra Party was founded in 1959.",
                "Its founders were C. Rajagopalachari, Minoo Masani and "
                "N.G. Ranga.",
                "Its economically conservative, free-market, anti-"
                "collectivisation platform directly opposed Congress's "
                "'socialistic pattern', and it became one of the larger "
                "non-Congress parliamentary parties by the 1960s.",
            ],
            "Do not group Swatantra with the Jana Sangh as a single "
            "'right-wing bloc'; their platforms differ in kind, not only in "
            "degree.",
            "Use Swatantra's founders and platform to answer any question "
            "distinguishing economically conservative from culturally "
            "conservative opposition parties.",
            """SWATANTRA PARTY -> founded 1959
FOUNDERS -> C. RAJAGOPALACHARI, MINOO MASANI, N.G. RANGA
PLATFORM -> free-market, anti-collectivisation, opposed the "socialistic pattern"
POSITION -> becomes one of the larger non-Congress parliamentary parties by the 1960s""",
            "The Swatantra Party is the free-market, anti-collectivisation "
            "party founded in 1959 by C. Rajagopalachari, Minoo Masani and "
            "N.G. Ranga in opposition to Congress's socialistic pattern.",
        ),
        authored_session(
            "The 1964 split in the Communist Party of India",
            "This session shows that party fragmentation was not confined "
            "to the non-Communist Left; the organised Communist movement "
            "split too, on both ideological and strategic grounds.",
            [
                "Ideological strain over the Sino-Soviet split ran through "
                "the Communist Party of India in the early 1960s.",
                "Differing responses to the 1962 border war sharpened this "
                "strain.",
                "The party split in 1964 into the CPI and the new CPI(M), "
                "leaving the organised Left divided for the rest of the "
                "decade.",
            ],
            "Date the split precisely to 1964, before the 1967 election, "
            "not as a later or simultaneous event.",
            "Use this split to answer any question on the fragmentation of "
            "the Indian Left in the 1960s.",
            """COMMUNIST PARTY OF INDIA -> internal strain through the early 1960s
FAULT LINES -> the Sino-Soviet split; differing responses to the 1962 border war
1964 -> THE PARTY SPLITS
RESULT -> CPI (one stream) and CPI(M) (the new formation)""",
            "The 1964 CPI split is the division of the Communist Party of "
            "India into the CPI and CPI(M), driven by the Sino-Soviet split "
            "and differing responses to the 1962 war.",
        ),
        authored_session(
            "Rajni Kothari's 'Congress system'",
            "This session names the analytical framework the whole topic "
            "has been building evidence for, and it is careful to attribute "
            "the framework to its author rather than to Congress itself.",
            [
                "The political scientist Rajni Kothari coined the term "
                "'Congress system'.",
                "Kothari described Congress as a 'party of consensus' that "
                "absorbed internal factions rather than losing them to "
                "separate parties.",
                "Opposition parties, in this model, acted as parties of "
                "'pressure', influencing Congress factions rather than "
                "forming credible alternative governments.",
            ],
            "Always attribute 'Congress system' and 'party of consensus' to "
            "Rajni Kothari; never present these as Congress's own "
            "description of itself.",
            "Use Kothari's framework to answer any question asking for an "
            "analytical model of Congress dominance between 1952 and 1967.",
            """RAJNI KOTHARI -> political scientist, coins the term "CONGRESS SYSTEM"
CLAIM -> Congress functions as a "PARTY OF CONSENSUS", absorbing factions internally
OPPOSITION ROLE -> parties of "PRESSURE", not alternative-government contenders
ATTRIBUTION -> Kothari's analytical term, NOT a Congress self-description""",
            "The 'Congress system' is Rajni Kothari's analytical term for a "
            "Congress functioning as a party of consensus that absorbed "
            "internal factions while opposition parties acted mainly as "
            "parties of pressure.",
        ),
        authored_session(
            "Seat majorities on a minority vote share",
            "This session supplies the arithmetic evidence behind Kothari's "
            "model, distinguishing Congress's seat dominance from any claim "
            "of majority political consent.",
            [
                "In the 1952, 1957 and 1962 general elections Congress won "
                "comfortable parliamentary seat majorities.",
                "Its national vote share stayed well under 50 per cent in "
                "each of these elections.",
                "The gap reflects first-past-the-post arithmetic operating "
                "on a fragmented opposition, not majority consent alone.",
            ],
            "Never equate a Congress seat majority with a Congress vote "
            "majority; the two figures moved very differently across these "
            "elections.",
            "Use this seat-versus-vote gap as the core evidence for any "
            "'was Congress dominance consensual' Mains answer.",
            """1952 / 1957 / 1962 ELECTIONS -> comfortable Congress SEAT majorities each time
VOTE SHARE -> stays WELL UNDER 50 per cent in each election
MECHANISM -> first-past-the-post arithmetic + a FRAGMENTED OPPOSITION
INFERENCE -> Congress dominance rested on electoral arithmetic, not consent alone""",
            "The seat-vote gap describes how Congress won comfortable "
            "parliamentary seat majorities in 1952, 1957 and 1962 while its "
            "national vote share stayed well under 50 per cent.",
        ),
        authored_session(
            "Smaller left formations and the plural Left",
            "This session widens the picture of the organised Left beyond "
            "the CPI/CPI(M) split, showing a genuinely plural rather than "
            "monolithic Left landscape.",
            [
                "The Revolutionary Socialist Party (RSP) and the Forward "
                "Bloc were smaller Left formations active mainly in Bengal "
                "and Kerala.",
                "Alongside the CPI and CPI(M), they added further plurality "
                "to the Left's organisational landscape.",
                "The Indian Left of 1947-67 was never a single unified "
                "bloc, a pattern that mirrors the fragmentation seen across "
                "the non-Communist opposition.",
            ],
            "Do not describe 'the Left' in this period as a single party or "
            "a single coherent bloc.",
            "Use RSP and Forward Bloc as supporting evidence whenever a "
            "question asks about the plurality of the Indian Left before "
            "1967.",
            """SMALLER LEFT FORMATIONS -> Revolutionary Socialist Party (RSP), Forward Bloc
BASE -> strongest in Bengal and Kerala, alongside the CPI/CPI(M)
ROLE -> add to a genuinely PLURAL, though fragmented, opposition landscape
NOT A MONOLITH -> the Indian Left of 1947-67 was NEVER a single unified bloc""",
            "RSP and Forward Bloc are smaller Left party formations, "
            "strongest in Bengal and Kerala, whose existence alongside the "
            "CPI and CPI(M) shows the plurality of India's organised Left "
            "before 1967.",
        ),
        authored_session(
            "Congress as an umbrella organisation",
            "This session explains the mechanism behind Kothari's model: "
            "Congress absorbed ideological range internally rather than "
            "expelling it to separate parties.",
            [
                "Congress functioned as a broad umbrella rather than an "
                "ideologically narrow party.",
                "Nehruvian planners, conservative traditionalists and "
                "regional bosses coexisted inside the same organisation.",
                "Much factional competition therefore occurred inside "
                "Congress rather than between separate parties.",
            ],
            "Do not describe Congress in this period as ideologically "
            "uniform; its breadth is precisely why factional competition "
            "occurred inside it.",
            "Use this umbrella model to explain why India's party system "
            "looked like one-party dominance while containing real internal "
            "competition.",
            """CONGRESS ORGANISATION -> a broad UMBRELLA, not an ideologically narrow party
INTERNAL FACTIONS -> Nehruvian planners, conservative traditionalists, regional bosses
MECHANISM -> factional competition happens INSIDE Congress, not mainly between parties
LINK FORWARD -> this internal factionalism shapes the 1966 succession (topic 34)""",
            "Congress as an umbrella organisation describes a party broad "
            "enough to hold Nehruvian planners, conservative traditionalists "
            "and regional bosses together, so that factional competition "
            "occurred mainly inside the party.",
        ),
        authored_session(
            "The rise of state-level 'Syndicate' bosses",
            "This session names the organisational feature that becomes "
            "decisive in the topic immediately following this one: the "
            "state-level power brokers later called the 'Syndicate'.",
            [
                "By the mid-1960s powerful state-level Congress leaders had "
                "become organisationally decisive inside the party.",
                "These leaders were later referred to collectively as the "
                "'Syndicate'.",
                "Their internal factional structure shapes the 1966 "
                "succession contest examined in the following topic.",
            ],
            "Do not name specific Syndicate leaders or 1966 succession "
            "details here; that belongs to the following topic.",
            "Use the Syndicate's rise to bridge from this topic's internal-"
            "factionalism analysis into the 1966 succession crisis.",
            """MID-1960s -> powerful STATE-LEVEL Congress leaders become decisive
LATER LABEL -> collectively referred to as the "SYNDICATE"
ROLE -> internal factional power brokers inside the Congress organisation
LINK FORWARD -> shapes the 1966 succession contest (topic 34)""",
            "The 'Syndicate' is the later label for the powerful state-level "
            "Congress leaders who became organisationally decisive by the "
            "mid-1960s and shaped the 1966 succession.",
        ),
        authored_session(
            "Ram Manohar Lohia and 'non-Congressism'",
            "This session introduces the strategic idea that eventually "
            "outlives the period this topic covers, connecting 1947-67 "
            "party politics to the much later Janata coalition.",
            [
                "The Socialist leader Ram Manohar Lohia argued for "
                "'non-Congressism'.",
                "The doctrine called for opposition unity against Congress "
                "even across ideological differences.",
                "It had little practical electoral effect before 1967 but "
                "prefigured the logic later used to build the Janata "
                "coalition of 1977.",
            ],
            "Do not claim non-Congressism achieved practical electoral "
            "success within this topic's own 1947-67 period.",
            "Use Lohia's doctrine to bridge forward to any question on the "
            "ideological logic behind the 1977 Janata coalition.",
            """RAM MANOHAR LOHIA -> leading Socialist figure, critic of Congress dominance
DOCTRINE -> "NON-CONGRESSISM": opposition unity against Congress, despite ideology
EARLY YEARS -> little practical electoral effect before 1967
LATER PAYOFF -> the same logic underlies the Janata coalition of 1977 (topic 36)""",
            "'Non-Congressism' is Ram Manohar Lohia's doctrine calling for "
            "ideologically diverse opposition parties to unite electorally "
            "against Congress, a logic with little effect before 1967 but "
            "later used to build the 1977 Janata coalition.",
        ),
        authored_session(
            "The ideological range of the non-Congress opposition",
            "This session pulls together the full ideological spread this "
            "topic has surveyed, to show why that spread could not, on its "
            "own, translate into an alternative government before 1967.",
            [
                "Between 1947 and 1967 the non-Congress opposition spanned "
                "the Hindu-nationalist Jana Sangh, the free-market "
                "Swatantra Party, several Socialist formations and a "
                "divided Communist movement.",
                "This was a genuine ideological range, not a marginal or "
                "token opposition.",
                "That range could not translate into a single alternative "
                "to Congress before 1967 because of its own internal "
                "fragmentation.",
            ],
            "Do not present the pre-1967 opposition as weak because it "
            "lacked ideas; present it as fragmented despite having real "
            "ideological range.",
            "Use this synthesis to answer any question asking why a diverse "
            "opposition still failed to unseat Congress before 1967.",
            """1947-1967 OPPOSITION -> Jana Sangh + Swatantra + Socialists (PSP etc.) + CPI/CPI(M)
CHARACTER -> a genuine ideological RANGE, not a marginal opposition
PROBLEM -> this range remained FRAGMENTED, not unified, before 1967
CONSEQUENCE -> could not translate into a single alternative to Congress""",
            "The ideological range of the non-Congress opposition refers to "
            "the genuine but fragmented spread of Jana Sangh, Swatantra, "
            "Socialist and Communist parties active between 1947 and 1967.",
        ),
        authored_session(
            "1967: the watershed foreshadowed",
            "The closing session states the payoff of the whole topic: two "
            "decades of party-system change, read together with declining "
            "Congress vote shares, foreshadow 1967 rather than making it a "
            "sudden surprise.",
            [
                "Congress's vote share declined steadily through the 1952, "
                "1957 and 1962 general elections.",
                "Two decades of splits, mergers and new party formations "
                "are described across this topic.",
                "Together these trends foreshadowed the 1967 general "
                "election, in which Congress lost power in eight states for "
                "the first time.",
            ],
            "Do not present 1967 as a sudden, unexplained event; it is the "
            "cumulative outcome of the party-system changes traced across "
            "this topic.",
            "Use this session to close any 20-mark answer tracing party-"
            "system fragmentation from 1948 to its 1967 consequences.",
            """THROUGH 1948-1964 -> ban, splits, mergers, new parties reshape opposition
BY 1962 -> Congress SEAT majority stays large; VOTE SHARE keeps declining
1967 -> for the FIRST TIME, Congress loses power in eight states
READ THE THREAD -> 1967 is the payoff of two decades of party-system change""",
            "The 1967 watershed is the general election in which Congress "
            "lost power in eight states for the first time, the cumulative "
            "outcome of the party-system fragmentation and declining vote "
            "share traced across this topic.",
        ),
    ],
}


TOPIC_CHRONOLOGY: dict[str, list[str]] = {
    "modern-indian-history-32": [
        "15 March 1950",
        "2 October 1952",
        "January 1955",
        "1956",
        "April 1954",
        "April 1955",
        "September 1961",
        "1957",
        "December 1961",
        "October-November 1962",
        "1963",
        "27 May 1964",
    ],
    "modern-indian-history-33": [
        "1948",
        "1950",
        "1951",
        "1952",
        "1959",
        "1964",
    ],
}

FORBIDDEN_TOPIC_PHRASES: dict[str, list[str]] = {
    "modern-indian-history-32": [
        "Bandung founded the Non-Aligned Movement",
        "Belgrade Conference in 1955",
        "Kamaraj Plan was an economic plan",
        "Nehru died in 1963",
        "constitutional body created by amendment",
    ],
    "modern-indian-history-33": [
        "Jana Sangh and Swatantra shared the same platform",
        "PSP was founded directly in 1951",
        "Congress described itself as the Congress system",
        "CPI split after the 1967 election",
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
        "scope": "Modern Indian History learner-v2 Topics 32-33",
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

    if key == "modern-indian-history-32":
        strict = [
            "15 March 1950",
            "173 million",
            "2 October 1952",
            "Balwantrai Mehta",
            "socialistic pattern of society",
            "Schedule A",
            "Schedule B",
            "Schedule C",
            "P.C. Mahalanobis",
            "Panchsheel",
            "Hindi-Chini Bhai Bhai",
            "twenty-nine Afro-Asian states",
            "Belgrade",
            "Tito",
            "Nasser",
            "Sukarno",
            "Nkrumah",
            "E.M.S. Namboodiripad",
            "Operation Vijay",
            "unilateral ceasefire",
            "K. Kamaraj",
            "January 1948",
            "27 May 1964",
        ]
    else:
        strict = [
            "dual membership",
            "Purushottam Das Tandon",
            "Syama Prasad Mookerjee",
            "J.B. Kripalani",
            "Praja Socialist Party",
            "Rajagopalachari",
            "Minoo Masani",
            "N.G. Ranga",
            "CPI(M)",
            "Rajni Kothari",
            "party of consensus",
            "Forward Bloc",
            "Ram Manohar Lohia",
            "non-Congressism",
            "eight states",
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
    """Topics 30-31 must remain exactly as their own generators authored them."""

    expected = ["modern-indian-history-30", "modern-indian-history-31"]
    if [config["key"] for config in previous.TOPICS] != expected:
        raise ValueError("Topics 30-31 configuration was mutated on import.")
    if set(previous.PANEL_DATA) != set(expected):
        raise ValueError("Topics 30-31 panel data was mutated on import.")


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
