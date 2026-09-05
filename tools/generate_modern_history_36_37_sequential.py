"""Build Modern Indian History learner-v2 Topics 36-37.

This authoring-only generator writes complete reusable Markdown, solved
workbooks, manual ASCII and graphical specifications, and tracker-free
generation-one manifests for the Janata interregnum, Indira Gandhi's return
and the regional crises of the 1980s (Topic 36), and for the Rajiv years and
the run-up to the millennium (Topic 37). It deliberately does not render
PDFs, update the tracker, regenerate indexes, finalize generations, or
publish packages.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base
import generate_modern_history_34_35_sequential as previous


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
    / "modern-indian-history-36-37-2026-08-31-sequential.json"
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
        36,
        "Janata Interregnum, Indira's Return & Regional Crises",
        "36_Janata-Interregnum-Indiras-Return-and-Regional-Crises.md",
        "36_Janata-Interregnum-Indiras-Return-and-Regional-Crises.md",
        "36_Janata-Interregnum-Indiras-Return-and-Regional-Crises_Complete-"
        "Topic-Package.md",
        [
            "basic/35_The-JP-Movement-and-the-Emergency.md",
            "basic/37_The-Rajiv-Years-and-Run-up-to-the-Millennium.md",
            "basic/30_Linguistic-Reorganisation-and-Regionalism.md",
            "35_The-JP-Movement-and-the-Emergency_Complete-Topic-Package.md",
        ],
        [],
        "No verified live current-affairs item is pegged to this topic. The "
        "owner's own Current-link section frames regional parties, "
        "federalism and internal security as a recurring analytical theme "
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
        "No Prelims or Mains demand in the local 2018-2026 routing ledgers "
        "is routed to this owner; this is a transparent zero-direct-PYQ "
        "audit rather than an omission, and the owner's own basic and "
        "advanced files carry no 'PYQ Integration' section to integrate.",
        [
            (
                "The Janata Party's formation, January 1977",
                "The Janata Party was formed in January 1977 as a merger of "
                "Congress (O), the Jana Sangh, the Bharatiya Lok Dal and the "
                "Socialists, uniting the anti-Emergency opposition into a "
                "single electoral front.",
            ),
            (
                "The 1977 election and Morarji Desai's government",
                "The Janata Party won the March 1977 general election with "
                "330 of 542 seats, and Morarji Desai became Prime Minister "
                "of India's first non-Congress government at the Centre.",
            ),
            (
                "The 'dual membership' rupture, 1979",
                "Janata disintegrated by 1979 over the 'dual membership' "
                "controversy, the question of whether Jana Sangh members "
                "inside the party could retain their separate membership of "
                "the Rashtriya Swayamsevak Sangh, compounded by personal "
                "rivalries among Morarji Desai, Charan Singh and Jagjivan "
                "Ram.",
            ),
            (
                "Charan Singh's caretaker government, July 1979",
                "Charan Singh headed a caretaker government from July 1979, "
                "after Morarji Desai resigned, without ever facing "
                "Parliament for a vote of confidence.",
            ),
            (
                "Indira Gandhi's return, January 1980",
                "Indira Gandhi returned to power in January 1980 when "
                "Congress (I) won 353 of 529 seats, a scale of victory that "
                "reflected Janata's collapse rather than a fresh positive "
                "mandate for her.",
            ),
            (
                "Sanjay Gandhi's death, June 1980",
                "Sanjay Gandhi died in an air crash in June 1980, an event "
                "that brought his elder brother Rajiv Gandhi into active "
                "politics.",
            ),
            (
                "Telugu Desam's breakthrough, 1983",
                "N.T. Rama Rao, a Telugu film star, founded the Telugu "
                "Desam Party and swept the 1983 Andhra Pradesh state "
                "election on a platform of Telugu self-respect and "
                "resentment of central interference.",
            ),
            (
                "The Left Front's West Bengal, from 1977",
                "The Left Front, led by the Communist Party of India "
                "(Marxist) under Jyoti Basu, formed the government of West "
                "Bengal in 1977 and governed the state continuously "
                "thereafter, building a durable agrarian-reformist regime.",
            ),
            (
                "The Assam Movement",
                "The Assam Movement, led by the All Assam Students' Union, "
                "mobilised mass agitation on the question of illegal "
                "migration and 'foreigners', an issue the Centre struggled "
                "to contain through the early 1980s.",
            ),
            (
                "Jammu and Kashmir: the Abdullah pattern",
                "In Jammu and Kashmir the politics of the Abdullah family, "
                "first Sheikh Abdullah and then his son Farooq Abdullah, "
                "played out against a recurring pattern of central "
                "interference with elected state governments.",
            ),
            (
                "The Anandpur Sahib Resolution",
                "Akali demands in Punjab were codified in the Anandpur "
                "Sahib Resolution, which combined a territorial claim over "
                "Chandigarh, a demand for a fairer share of river waters, "
                "and a call for greater state autonomy within the federal "
                "structure.",
            ),
            (
                "The rise of Bhindranwale and militancy",
                "Once the Anandpur Sahib Resolution's federal-economic "
                "demands went unsettled, the vacated political space was "
                "filled by the rise of Jarnail Singh Bhindranwale and armed "
                "militancy in Punjab.",
            ),
            (
                "Operation Blue Star, June 1984",
                "Operation Blue Star, the Indian Army's operation against "
                "militants entrenched in the Golden Temple complex at "
                "Amritsar, took place in June 1984.",
            ),
            (
                "Indira Gandhi's assassination, 31 October 1984",
                "Indira Gandhi was assassinated on 31 October 1984, months "
                "after Operation Blue Star and years after the Emergency "
                "had already ended.",
            ),
            (
                "The 44th Amendment, 1978: Janata's achievement",
                "Janata's own durable achievement, the 44th Constitutional "
                "Amendment of 1978, reversed many Emergency-era provisions "
                "and restored civil-liberties safeguards, a credit due "
                "before assessing the government's later collapse.",
            ),
            (
                "Regional assertion as a consequence, not a failure, of "
                "integration",
                "Bipan Chandra's advanced reading treats the regional "
                "assertion of the 1980s not as a failure of national "
                "integration but as its consequence: state politics became "
                "genuinely autonomous, as caste, class, language and "
                "regional pride produced durable regional parties the "
                "Centre could not dislodge.",
            ),
            (
                "The comparative pattern across theatres",
                "Across Assam, Punjab, Andhra Pradesh, West Bengal and "
                "Jammu and Kashmir, demands pursued through elections were "
                "absorbed into competitive federal politics, while demands "
                "pursued outside elections after negotiation failed "
                "escalated toward crisis.",
            ),
            (
                "Three historiographical readings of the Punjab crisis",
                "A political-management reading blames central mishandling "
                "of legitimate federal-economic demands; a "
                "national-security reading foregrounds cross-border support "
                "for militancy; a federalist reading blames the erosion of "
                "state autonomy and the misuse of Article 356; Chandra "
                "privileges the political-management thesis while noting "
                "all three.",
            ),
            (
                "The delayed-accommodation thesis",
                "The delayed-accommodation argument holds that the eventual "
                "settlements of Punjab and Assam, reached only in 1985 "
                "through their respective accords, resembled what could "
                "have been negotiated earlier, so that the intervening "
                "violence measured the cost of postponement rather than the "
                "absence of a workable settlement.",
            ),
            (
                "The restraint rule for this owner",
                "This owner records the demands, dates, actions and "
                "outcomes of the Punjab, Assam and Jammu and Kashmir crises "
                "with strict restraint: it does not state casualty "
                "figures, does not characterise or assign motives to any "
                "community, and does not extend the Punjab narrative "
                "beyond the assassination of 31 October 1984, leaving the "
                "1985 accords to the following topic.",
            ),
        ],
        [
            "Janata's collapse followed the 1979 dual-membership rupture "
            "over RSS ties, not simply personality clashes among Desai, "
            "Charan Singh and Jagjivan Ram.",
            "Charan Singh never won a general election as Janata's leader; "
            "he headed only a caretaker government from July 1979 and "
            "never faced Parliament for a confidence vote.",
            "Telugu Desam was founded by N.T. Rama Rao on 29 March 1982 "
            "and swept the 1983 Andhra Pradesh election; it did not grow "
            "out of the Congress.",
            "Operation Blue Star took place in June 1984, not 1983; do not "
            "misdate it.",
            "Indira Gandhi was assassinated on 31 October 1984, years "
            "after the Emergency ended, not during it.",
            "The Punjab crisis began with federal-economic Akali demands "
            "in the Anandpur Sahib Resolution that were mismanaged; it was "
            "not a purely religious dispute from the outset.",
            "The Assam Movement was a mass agitation over migration and "
            "identity led by the All Assam Students' Union, not a routine "
            "law-and-order episode.",
            "Indira Gandhi's 1980 return (353 of 529) reflected Janata's "
            "collapse rather than a fresh positive mandate for her; do not "
            "read it as an endorsement of the Emergency.",
            "Janata won 330 of 542 seats in March 1977; do not alter this "
            "figure or its date.",
            "The Janata Party was formed in January 1977 and won the "
            "general election in March 1977; do not conflate the two "
            "dates.",
            "Do not state casualty figures for Operation Blue Star or any "
            "Punjab-related episode in this topic.",
            "Do not assign motives or characterise any community in "
            "describing the Punjab, Assam or Jammu and Kashmir crises.",
            "The 1985 Punjab and Assam accords belong to the following "
            "topic on the Rajiv years; do not narrate them here as part of "
            "this topic's account.",
        ],
        [
            (
                10,
                "Why did the Janata experiment of 1977-1980 fail? Analyse "
                "its internal contradictions.",
                "Janata proved that a coalition united only by "
                "anti-Indira, anti-Emergency sentiment could win power but "
                "not exercise it: absent a shared programme, a single "
                "leader or a common organisational culture, the "
                "dual-membership dispute supplied the fault line on which "
                "the government collapsed by 1979.",
                [0, 1, 2, 3],
            ),
            (
                10,
                "Discuss the sources and forms of regional political "
                "assertion in India during the 1980s, with examples.",
                "State-specific social coalitions of caste, language and "
                "regional pride, most visibly in Andhra Pradesh's Telugu "
                "Desam and West Bengal's Left Front, produced durable "
                "regional parties that the Centre could not dislodge, "
                "converting regional identity into an independent "
                "electoral resource.",
                [6, 7, 8, 9, 15],
            ),
            (
                15,
                "Trace the causes and consequences of the Punjab crisis up "
                "to October 1984.",
                "A negotiable federal-economic demand, the Anandpur Sahib "
                "Resolution, was not settled while it remained negotiable; "
                "the vacated political space was filled by militancy, and "
                "the resulting operation against the Golden Temple was "
                "followed within months by Indira Gandhi's assassination.",
                [10, 11, 12, 13],
            ),
            (
                15,
                "Compare the central government's handling of the regional "
                "crises in Punjab, Assam, Andhra Pradesh and West Bengal in "
                "the late 1970s and 1980s.",
                "Demands pursued electorally, as in Andhra Pradesh and West "
                "Bengal, were absorbed into competitive federal politics, "
                "while demands pursued outside elections after negotiation "
                "failed, as in Punjab and Assam, escalated toward crisis "
                "before eventual accords in 1985.",
                [6, 7, 8, 10, 16, 18],
            ),
            (
                20,
                "'Anti-Congressism was sufficient to win an election and "
                "insufficient to sustain a government.' Evaluate this "
                "statement with reference to the Janata interregnum and "
                "Indira Gandhi's return to power.",
                "The scale of Janata's 1977 victory and the scale of its "
                "1979 collapse both testify to a coalition defined only by "
                "what it opposed; Indira Gandhi's 1980 return, in turn, "
                "measured the public's verdict on that failure rather than "
                "a renewed personal mandate, together demonstrating that a "
                "negative coalition can capture office but not govern.",
                [0, 1, 2, 3, 4, 7],
            ),
            (
                20,
                "Trace India's political trajectory from the formation of "
                "the Janata Party in January 1977 to Indira Gandhi's "
                "assassination in October 1984, and assess whether the "
                "regional assertions of this period represented a crisis "
                "for, or a maturing of, Indian federalism.",
                "A decade that opened with the first non-Congress "
                "government at the Centre and closed with the "
                "assassination of a sitting Prime Minister was, at the "
                "state level, less a story of national disintegration "
                "than of state politics becoming genuinely autonomous; "
                "where that autonomy was accommodated it deepened "
                "federalism, and where it was resisted, as in Punjab, it "
                "produced the era's gravest crisis.",
                [0, 1, 4, 6, 7, 10, 12, 13, 15, 16],
            ),
        ],
        [],
        [
            "Janata Party",
            "Morarji Desai",
            "Charan Singh",
            "Indira Gandhi",
            "Telugu Desam",
            "Anandpur Sahib Resolution",
            "Operation Blue Star",
            "Bhindranwale",
            "Assam Movement",
        ],
    ),
    base.topic(
        37,
        "The Rajiv Years & the Run-up to the Millennium",
        "37_The-Rajiv-Years-and-Run-up-to-the-Millennium.md",
        "37_The-Rajiv-Years-and-Run-up-to-the-Millennium.md",
        "37_The-Rajiv-Years-and-Run-up-to-the-Millennium_Complete-Topic-"
        "Package.md",
        [
            "basic/36_Janata-Interregnum-Indiras-Return-and-Regional-"
            "Crises.md",
            "basic/38_Economy-Land-Society-and-State-A-Post-Independence-"
            "Synthesis.md",
            "36_Janata-Interregnum-Indiras-Return-and-Regional-Crises_"
            "Complete-Topic-Package.md",
        ],
        [],
        "No verified live current-affairs item is pegged to this topic. The "
        "owner's own Current-link section frames coalition politics, OBC "
        "reservation and the 1991 reforms as recurring analytical themes "
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
        "No Prelims or Mains demand in the local 2018-2026 routing ledgers "
        "is routed to this owner; this is a transparent zero-direct-PYQ "
        "audit rather than an omission, and the owner's own basic and "
        "advanced files carry no 'PYQ Integration' section to integrate.",
        [
            (
                "Rajiv Gandhi's 1984 mandate",
                "Congress won 404 of the 514 seats elected in the December "
                "1984 general election under Rajiv Gandhi, the largest "
                "mandate in Indian electoral history to that point.",
            ),
            (
                "The modernising agenda",
                "Rajiv Gandhi's government pushed a modernising agenda of "
                "telecommunications, computerisation, science and "
                "technology missions, panchayati raj and education reform, "
                "prefiguring the economic opening of 1991.",
            ),
            (
                "The Anti-Defection Act, 1985",
                "The Anti-Defection Act, the 52nd Constitutional Amendment, "
                "was passed in 1985 under Rajiv Gandhi, addressing the mass "
                "floor-crossing that had become routine after the 1967 "
                "election.",
            ),
            (
                "The 1985 accords",
                "Rajiv Gandhi signed the Punjab accord with Harchand Singh "
                "Longowal, and separate Assam and Mizoram accords, all in "
                "1985, settling regional crises inherited from the previous "
                "decade through negotiation rather than force.",
            ),
            (
                "The Shah Bano reversal, 1985-86",
                "The Shah Bano case of 1985 and its legislative reversal in "
                "1986, which overturned a Supreme Court maintenance ruling "
                "under conservative religious pressure, alienated liberal "
                "opinion and minority-rights advocates.",
            ),
            (
                "The Ayodhya shrine opening",
                "The opening of the locks of the disputed Ayodhya shrine, "
                "intended by the government to balance the Shah Bano "
                "reversal, instead alienated the other community and "
                "energised Hindu mobilisation.",
            ),
            (
                "The Bofors scandal, 1987",
                "The Bofors arms-deal scandal broke in 1987, destroying "
                "Rajiv Gandhi's 'Mr Clean' image and converting his own "
                "anti-corruption plank against his government.",
            ),
            (
                "V.P. Singh's exit and the National Front",
                "V.P. Singh broke away from the Congress, formed the Jan "
                "Morcha in 1987 and then the Janata Dal and National Front "
                "in 1988, uniting the opposition around an anti-corruption "
                "platform.",
            ),
            (
                "The 1989 election: fragmentation",
                "In the 1989 general election Congress fell from its 1984 "
                "record to about 197 seats, the BJP rose from 2 to 86 "
                "seats, and V.P. Singh formed a National Front minority "
                "government supported from outside by both the BJP and the "
                "Left.",
            ),
            (
                "The Mandal Commission, 1990",
                "V.P. Singh's government implemented the Mandal "
                "Commission's recommendation of 27 per cent reservation for "
                "Other Backward Classes in central government employment in "
                "1990, taking total reservation toward roughly 49.5 per "
                "cent together with the existing Scheduled Caste and "
                "Scheduled Tribe quotas, and triggering nationwide "
                "agitation.",
            ),
            (
                "Advani's rath yatra, 1990",
                "L.K. Advani's rath yatra in 1990 intensified the Ayodhya "
                "mobilisation as a parallel, competing axis of political "
                "appeal to the Mandal reservation announcement.",
            ),
            (
                "1991: the economic break",
                "The Narasimha Rao government took office in 1991 and "
                "launched economic liberalisation, with Manmohan Singh as "
                "Finance Minister, in response to a balance-of-payments "
                "crisis.",
            ),
            (
                "Rajiv Gandhi's assassination, 1991",
                "Rajiv Gandhi was assassinated in 1991, during the general "
                "election campaign that brought the Narasimha Rao "
                "government to office.",
            ),
            (
                "The Babri Masjid demolition, 6 December 1992",
                "The Babri Masjid at Ayodhya was demolished on 6 December "
                "1992, the culmination of the mobilisation begun by the "
                "1990 rath yatra.",
            ),
            (
                "Mandal and Mandir as crossing cleavages",
                "Mandal, organised around caste, and Mandir, organised "
                "around religion, were competing mobilisations of the same "
                "electorate along different, crossing axes, and because "
                "neither cleavage could produce a stable national majority "
                "on its own, coalition government became the structural "
                "outcome of the decade.",
            ),
            (
                "The coalition decade, 1996-99",
                "The 1990s closed with a short BJP government under Atal "
                "Bihari Vajpayee in 1996, the United Front governments of "
                "H.D. Deve Gowda and then I.K. Gujral, and the National "
                "Democratic Alliance (NDA) under Vajpayee formed in 1998 "
                "and consolidated after the 1999 election.",
            ),
            (
                "Chandra's 'Mandal, Mandir and Market' synthesis",
                "Bipan Chandra's synthesis reads 1989 to 1992 as the "
                "simultaneous convergence of three forces, OBC assertion, "
                "Hindutva mobilisation and economic liberalisation, that "
                "together dismantled the Nehruvian political-economic "
                "consensus.",
            ),
            (
                "The democratic-deepening counter-reading",
                "Critics of a purely declinist reading of the period argue "
                "that it instead deepened democracy, bringing subordinated "
                "castes, regional forces and market energies into the "
                "political mainstream and replacing an elite consensus "
                "with genuine competition.",
            ),
            (
                "The three-transitions thesis",
                "Between 1989 and 1999 India underwent three simultaneous "
                "transitions: from single-party majority to coalition "
                "government, from state-led planning to a liberalised "
                "economy, and from a Congress-centred cross-class "
                "consensus to politics organised around caste and "
                "religious identity.",
            ),
            (
                "The panchayati raj caution",
                "Rajiv Gandhi's panchayati raj initiative of the mid-1980s "
                "was a policy beginning rather than a completed "
                "constitutional reform, since panchayati raj bodies did "
                "not acquire constitutional status until the 73rd and "
                "74th Amendments of the early 1990s.",
            ),
        ],
        [
            "The Anti-Defection Act was the 52nd Constitutional Amendment "
            "of 1985 under Rajiv Gandhi, not a measure of V.P. Singh's "
            "government.",
            "Economic liberalisation began in 1991 under Narasimha Rao, "
            "not under Rajiv Gandhi.",
            "The Mandal quota was 27 per cent for OBCs within the overall "
            "reservation ceiling, not 50 per cent.",
            "The Babri Masjid was demolished on 6 December 1992, not in "
            "1990; 1990 was the year of the rath yatra.",
            "Vajpayee led a short government in 1996 before the NDA "
            "government of 1998-99; he did not become Prime Minister only "
            "in 1998.",
            "The National Front had outside support from both the BJP and "
            "the Left, not from the Left alone.",
            "Rajiv Gandhi began the modernising shift that the 1991 "
            "reforms later completed; he was not anti-reform.",
            "The Shah Bano reversal and the Ayodhya shrine opening were "
            "both identity misjudgements that damaged Rajiv Gandhi with "
            "both communities; they were not unrelated to his decline.",
            "Panchayati raj did not acquire constitutional status under "
            "Rajiv Gandhi; that came only with the 73rd and 74th "
            "Amendments of the early 1990s.",
            "Congress won 404 of 514 elected seats in December 1984 under "
            "Rajiv Gandhi; do not convert this into 415 of the full 543-seat "
            "House because polling in Assam and Punjab was deferred.",
            "Congress fell to about 197 seats in the 1989 election; do not "
            "assume it retained its 1984 strength.",
            "The 1991 reforms were enabled by a balance-of-payments crisis "
            "and a minority government acting under compulsion, not by a "
            "prior political consensus.",
            "Coalition governments after 1989 became the normal form of "
            "national governance for the rest of the decade, not a "
            "temporary aberration.",
        ],
        [
            (
                10,
                "Discuss the achievements and limitations of Rajiv "
                "Gandhi's modernising agenda between 1984 and 1989.",
                "Rajiv Gandhi's technological and administrative agenda, "
                "and the negotiated 1985 accords, were real achievements, "
                "but the same years' identity misjudgements and the Bofors "
                "scandal destroyed the political capital needed to sustain "
                "them.",
                [0, 1, 2, 3, 19],
            ),
            (
                10,
                "Examine the causes of the fragmentation of the "
                "Congress-dominated party system by 1989.",
                "The Shah Bano reversal and the Ayodhya shrine opening "
                "alienated both communities they were meant to conciliate, "
                "and the Bofors scandal converted Rajiv Gandhi's own "
                "anti-corruption idiom into the platform on which V.P. "
                "Singh's opposition defeated Congress in 1989.",
                [4, 5, 6, 7, 8],
            ),
            (
                15,
                "'Mandal and Mandir reshaped Indian politics after "
                "1989.' Discuss.",
                "The Mandal Commission's 1990 reservation decision and "
                "Advani's rath yatra of the same year mobilised the same "
                "electorate along crossing axes of caste and religion, and "
                "because neither cleavage produced a durable national "
                "majority on its own, coalition government became the "
                "structural, not incidental, outcome.",
                [9, 10, 13, 14],
            ),
            (
                15,
                "Assess the significance of 1991 as a turning point in "
                "India's political economy.",
                "1991 was decisive because it was involuntary: a "
                "balance-of-payments crisis suspended the political veto "
                "that had blocked economic reform for three decades, "
                "permitting a minority government to act where consensus "
                "had never existed.",
                [11, 12, 16, 18],
            ),
            (
                20,
                "'Rajiv Gandhi modernised the economy's aspirations but "
                "destabilised the polity's secular-federal balance.' "
                "Critically examine.",
                "Rajiv Gandhi's technocratic agenda and the 1985 accords "
                "addressed real developmental and federal deficits, but "
                "the twin identity concessions of 1985-86 and the Bofors "
                "scandal converted a record mandate into a fragmented "
                "party system within five years, a paradox this owner "
                "resolves by crediting the substantive achievements while "
                "holding the political judgement to account.",
                [0, 1, 3, 4, 5, 6, 7],
            ),
            (
                20,
                "Trace the transformation of Indian politics between 1984 "
                "and 1999, and evaluate whether this period represented a "
                "crisis of the Nehruvian consensus or its democratic "
                "deepening.",
                "Between the record mandate of 1984 and the consolidated "
                "NDA government of 1999, India underwent three "
                "simultaneous transitions, from single-party majority to "
                "coalition, from planning to markets, and from a "
                "cross-class consensus to identity-based competition, a "
                "movement that a purely declinist reading treats as crisis "
                "and a rival reading treats as the deepening of "
                "democratic competition.",
                [8, 9, 10, 11, 13, 15, 16, 17, 18],
            ),
        ],
        [],
        [
            "Rajiv Gandhi",
            "Anti-Defection Act",
            "Shah Bano",
            "Bofors",
            "V.P. Singh",
            "Mandal Commission",
            "rath yatra",
            "Narasimha Rao",
            "Vajpayee",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-36": [
        (
            "Janata's rise and fall, 1977-1980",
            "timeline",
            """JANATA PARTY FORMED -> JANUARY 1977 (Congress-O + Jana Sangh + BLD + Socialists)
ELECTION WON -> MARCH 1977 (330 of 542); MORARJI DESAI becomes PM
COLLAPSE -> 1979, over the "dual membership" (Jana Sangh-RSS) dispute
CARETAKER -> CHARAN SINGH, from JULY 1979, no confidence vote faced""",
            ["Janata's formation, rise and collapse, 1977-1980"],
        ),
        (
            "The dual-membership fault line",
            "cause-effect",
            """QUESTION -> can a Jana Sangh member also belong to the RSS?
JANATA'S ANSWER -> never agreed upon inside the governing coalition
CONSEQUENCE -> Jana Sangh faction exits; government loses its majority
LESSON -> a negative-unity coalition needs one positive, shared answer""",
            ["The dual-membership dispute as Janata's structural fault line"],
        ),
        (
            "Indira's return, January 1980",
            "timeline",
            """JANATA COLLAPSES -> 1979, Charan Singh caretaker, no confidence vote
ELECTION -> JANUARY 1980; CONGRESS (I) wins 353 of 529 seats
READING -> a verdict on JANATA'S FAILURE, not a fresh mandate for Indira
AFTERMATH -> SANJAY GANDHI dies, JUNE 1980; RAJIV GANDHI enters politics""",
            ["Indira Gandhi's return to power in 1980"],
        ),
        (
            "Regional parties on the map",
            "comparison",
            """TAMIL NADU -> DMK / AIADMK dominance
ANDHRA PRADESH -> TELUGU DESAM (N.T. RAMA RAO), sweeps 1983
WEST BENGAL -> LEFT FRONT (JYOTI BASU), governing continuously from 1977
JAMMU AND KASHMIR -> Abdullah family politics vs central interference""",
            ["Regional parties in the 1980s"],
        ),
        (
            "The Assam Movement",
            "cause-effect",
            """LED BY -> All Assam Students' Union (AASU)
GRIEVANCE -> illegal migration and the "foreigner" question
FORM -> mass agitation, not a law-and-order episode
CENTRE'S RESPONSE -> struggled to contain it through the early 1980s""",
            ["The Assam Movement"],
        ),
        (
            "Jammu and Kashmir: the Abdullah pattern",
            "cause-effect",
            """LEADERSHIP -> Sheikh Abdullah, then his son Farooq Abdullah
PATTERN -> elected state governments face repeated central interference
EFFECT -> corrodes democratic legitimacy at the state level
RESTRAINT -> this owner records the pattern; it avoids present-day politics""",
            ["Jammu and Kashmir: the Abdullah leadership pattern"],
        ),
        (
            "The Anandpur Sahib Resolution's demands",
            "classification",
            """TERRITORIAL -> a claim over Chandigarh
ECONOMIC -> a fairer share of river waters
FEDERAL -> a demand for greater state autonomy
STATUS AT FRAMING -> a negotiable federal-economic charter""",
            ["The Anandpur Sahib Resolution"],
        ),
        (
            "The Punjab escalation ladder",
            "escalation-flow",
            """STEP 1 -> Anandpur Sahib Resolution's demands go unsettled
STEP 2 -> the negotiable political space is vacated
STEP 3 -> BHINDRANWALE and militancy rise to fill it
STEP 4 -> OPERATION BLUE STAR, June 1984, Golden Temple, Amritsar""",
            ["The Punjab crisis: escalation from demand to operation"],
        ),
        (
            "Operation Blue Star and its aftermath",
            "timeline",
            """OPERATION BLUE STAR -> JUNE 1984, Golden Temple complex, Amritsar
INTERVAL -> several months of continued tension
ASSASSINATION -> INDIRA GANDHI, 31 OCTOBER 1984
RESTRAINT -> no casualty figures or community characterisation here""",
            ["Operation Blue Star and Indira Gandhi's assassination"],
        ),
        (
            "Comparative engine: five theatres of regional crisis",
            "comparison-table",
            """THEATRE      | ACTOR               | ROUTE                   | OUTCOME
PUNJAB       | Akali Dal/militants | negotiation -> force    | Accord, 1985
ASSAM        | AASU                | agitation -> negotiation| Accord, 1985
ANDHRA/WB    | Telugu Desam/Left   | elections               | absorbed""",
            ["Comparative engine across regional crises"],
        ),
        (
            "Three historiographical readings of the 1980s",
            "comparison",
            """POLITICAL-MANAGEMENT -> blames mishandling of federal-economic demands
NATIONAL-SECURITY -> foregrounds cross-border support for militancy
FEDERALIST -> blames erosion of state autonomy, misuse of Article 356
CHANDRA'S CHOICE -> privileges the political-management reading""",
            ["Three historiographical readings of the Punjab crisis"],
        ),
        (
            "The delayed-accommodation thesis",
            "argument-tree",
            """CLAIM -> the 1985 accords resembled what could have been agreed earlier
EVIDENCE -> the Mizo Accord precedent settled a similar demand
CONSEQUENCE -> the years in between measure the cost of postponement
LIMIT -> settlement analysis belongs to the following topic, basic/37""",
            ["The delayed-accommodation thesis"],
        ),
    ],
    "modern-indian-history-37": [
        (
            "The 1984 mandate and modernising agenda",
            "timeline",
            """MANDATE -> DECEMBER 1984; CONGRESS wins 404 of 514 elected seats under RAJIV GANDHI
AGENDA -> telecom, computerisation, science missions, panchayati raj
CAUTION -> panchayati raj not yet constitutional; that comes in the 1990s
SIGNIFICANCE -> the largest mandate in Indian electoral history to date""",
            ["Rajiv Gandhi's 1984 mandate and modernising agenda"],
        ),
        (
            "The 1985 accords and the Anti-Defection Act",
            "timeline",
            """PUNJAB ACCORD -> Rajiv Gandhi and Harchand Singh Longowal, 1985
ASSAM AND MIZORAM ACCORDS -> also settled in 1985
ANTI-DEFECTION ACT -> 52nd Constitutional Amendment, 1985
EFFECT -> three inherited regional crises addressed by negotiation""",
            ["The 1985 accords and the Anti-Defection Act"],
        ),
        (
            "The twin identity concessions",
            "cause-effect",
            """CONCESSION 1 -> Shah Bano reversal, 1985-86, conservative pressure
CONCESSION 2 -> Ayodhya shrine opening, meant to balance concession 1
RESULT -> both communities alienated, not balanced
LESSON -> symbolic concessions to two sides do not cancel; they mobilise both""",
            ["The Shah Bano reversal and the Ayodhya shrine opening"],
        ),
        (
            "Bofors and the exit of V.P. Singh",
            "cause-effect",
            """BOFORS SCANDAL -> breaks in 1987; wrecks Rajiv Gandhi's "Mr Clean" image
V.P. SINGH -> exits Congress; forms the JAN MORCHA, 1987
NEXT STEP -> JANATA DAL / NATIONAL FRONT formed, 1988
OUTCOME -> Congress's own clean-government idiom turned against it""",
            ["Bofors and V.P. Singh's exit"],
        ),
        (
            "1989: fragmentation of the party system",
            "comparison",
            """CONGRESS -> falls from the 1984 record to about 197 seats
BJP -> rises from 2 seats (1984) to 86 seats (1989)
GOVERNMENT -> V.P. Singh's National Front, a MINORITY government
SUPPORT -> from OUTSIDE, by both the BJP and the Left""",
            ["The 1989 election and party-system fragmentation"],
        ),
        (
            "Mandal, 1990: the caste axis",
            "classification",
            """COMMISSION -> Mandal Commission recommendations implemented, 1990
QUOTA -> 27 per cent reservation for OBCs in central government jobs
TOTAL -> reservation moves toward about 49.5 per cent with SC/ST quotas
EFFECT -> nationwide agitation; OBC identity becomes an organised bloc""",
            ["The Mandal Commission, 1990"],
        ),
        (
            "Mandir, 1990: the religious axis",
            "timeline",
            """MOBILISATION -> Advani's rath yatra, 1990, intensifies Ayodhya agitation
PARALLEL -> runs alongside, and competes with, the Mandal announcement
CULMINATION -> Babri Masjid demolished, 6 DECEMBER 1992
EFFECT -> Hindutva mobilisation becomes a national electoral force""",
            ["Advani's rath yatra and the Babri Masjid demolition"],
        ),
        (
            "System-change engine: 1984 to 1999",
            "flow",
            """1984 -> single-party record majority
1985-89 -> identity misjudgements plus Bofors erode support; 1989 fragments
1990 -> Mandal (caste) and Mandir (religion) mobilise differently
1991-99 -> crisis-led reform, then coalition government as the normal form""",
            ["The system-change engine, 1984-1999"],
        ),
        (
            "1991: the economic break",
            "cause-effect",
            """GOVERNMENT -> Narasimha Rao takes office, 1991
POLICY -> economic liberalisation, Manmohan Singh as Finance Minister
TRIGGER -> a balance-of-payments crisis, not a prior political consensus
CONCURRENT -> Rajiv Gandhi assassinated during the same election campaign""",
            ["1991: the economic break"],
        ),
        (
            "The coalition decade, 1996-99",
            "timeline",
            """1996 -> a short BJP government under Atal Bihari Vajpayee
1996-98 -> United Front governments, Deve Gowda then Gujral
1998 -> National Democratic Alliance (NDA) formed, under Vajpayee
1999 -> the NDA consolidated after the general election""",
            ["The coalition decade, 1996-1999"],
        ),
        (
            "Comparative cleavages: Mandal versus Mandir",
            "comparison-table",
            """AXIS      | MANDAL              | MANDIR
CLEAVAGE  | caste                | religion
YEAR      | 1990                 | 1990 (yatra), 1992 (demolition)
RESULT    | crossing lines; neither yields a national majority alone""",
            ["Comparative cleavages: Mandal versus Mandir"],
        ),
        (
            "Three-transitions thesis",
            "argument-tree",
            """TRANSITION 1 -> single-party majority to coalition government
TRANSITION 2 -> state-led planning to a liberalised economy
TRANSITION 3 -> Congress cross-class consensus to caste/religious identity
VERDICT -> the interaction of the three explains the decade best""",
            ["The three-transitions thesis, 1989-1999"],
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
    if title in SESSION_VISUALS or title in SESSION_DEFINITIONS:
        raise ValueError(f"Duplicate authored session title: {title}")
    SESSION_VISUALS[title] = visual
    SESSION_DEFINITIONS[title] = definition
    return (title, core, evidence, caution, exam_use)


SESSION_PLANS: dict[str, list[tuple[str, str, list[str], str, str]]] = {
    "modern-indian-history-36": [
        authored_session(
            "Janata's formation and the 1977 mandate",
            "Janata's formation in January 1977 united the anti-Emergency "
            "opposition into one electoral front, and within weeks that "
            "front converted a shared grievance into India's first "
            "non-Congress government at the Centre.",
            [
                "The Janata Party was formed in January 1977 by merging "
                "Congress (O), the Jana Sangh, the Bharatiya Lok Dal and "
                "the Socialists.",
                "The merged party won 330 of 542 seats in the March 1977 "
                "general election.",
                "Morarji Desai became Prime Minister, heading India's "
                "first non-Congress government at the Centre.",
            ],
            "Do not conflate the party's January 1977 formation with its "
            "March 1977 election victory; they are two separate, "
            "sequential events.",
            "Use this session to open any answer on the political "
            "consequences of the Emergency or on India's first "
            "non-Congress government.",
            """JANATA PARTY -> formed JANUARY 1977 (Congress-O+Jana Sangh+BLD+Socialists)
ELECTION -> MARCH 1977; wins 330 of 542 seats
GOVERNMENT -> MORARJI DESAI becomes Prime Minister
SIGNIFICANCE -> India's first non-Congress government at the Centre""",
            "The Janata Party is the January 1977 merger of Congress (O), "
            "the Jana Sangh, the Bharatiya Lok Dal and the Socialists that "
            "won the March 1977 general election and formed India's first "
            "non-Congress government at the Centre under Morarji Desai.",
        ),
        authored_session(
            "Morarji Desai's government and its record",
            "Morarji Desai's government, despite its short life, delivered "
            "one durable constitutional achievement, the 44th "
            "Constitutional Amendment of 1978, which reversed many "
            "Emergency-era provisions and restored civil-liberties "
            "safeguards.",
            [
                "The 44th Constitutional Amendment was enacted in 1978 "
                "under the Janata government.",
                "It reversed several Emergency-era provisions and restored "
                "civil-liberties safeguards.",
                "This achievement is credited to the government even "
                "though its own internal coalition later collapsed.",
            ],
            "Do not let the government's later collapse erase its 44th "
            "Constitutional Amendment achievement; both facts belong in a "
            "balanced answer.",
            "Use this session to answer any Mains question that asks you "
            "to both credit and critique the Janata government.",
            """44TH CONSTITUTIONAL AMENDMENT -> enacted 1978, under the JANATA government
EFFECT -> reverses several Emergency-era provisions
EFFECT -> restores civil-liberties safeguards
BALANCE -> a durable achievement despite the coalition's later collapse""",
            "The 44th Constitutional Amendment, 1978, is Janata's durable "
            "achievement that reversed Emergency-era provisions and "
            "restored civil-liberties safeguards, distinct from and prior "
            "to the coalition's own 1979 collapse.",
        ),
        authored_session(
            "The dual-membership rupture and Janata's collapse, 1979",
            "Janata disintegrated in 1979 over the dual-membership "
            "dispute, whether Jana Sangh members could simultaneously "
            "belong to the RSS, a fault line sharpened by personal "
            "rivalry among Morarji Desai, Charan Singh and Jagjivan Ram.",
            [
                "The dispute asked whether Jana Sangh members inside "
                "Janata could retain separate membership of the RSS.",
                "This unresolved question, compounded by rivalry among "
                "Morarji Desai, Charan Singh and Jagjivan Ram, split the "
                "coalition by 1979.",
                "The rupture proved that shared opposition to Indira "
                "Gandhi and the Emergency was not, by itself, a governing "
                "programme.",
            ],
            "Do not reduce Janata's 1979 collapse to personality clashes "
            "alone; the dual-membership dispute was the structural "
            "trigger.",
            "Use this session for any Mains question analysing why "
            "negative-unity coalitions struggle to govern.",
            """DISPUTE -> can a Jana Sangh member also belong to the RSS?
COMPOUNDING FACTOR -> rivalry: Morarji Desai vs Charan Singh vs Jagjivan Ram
OUTCOME -> Janata splits, 1979
LESSON -> anti-Emergency unity was not a governing programme""",
            "The dual-membership dispute is the unresolved 1979 question "
            "of whether Jana Sangh members inside Janata could also belong "
            "to the RSS, the structural trigger of the coalition's "
            "collapse.",
        ),
        authored_session(
            "Charan Singh's caretaker interlude",
            "Charan Singh's premiership from July 1979 was a caretaker "
            "interlude rather than a mandate: he never faced Parliament "
            "for a vote of confidence and never won a general election as "
            "Janata's leader.",
            [
                "Charan Singh became Prime Minister in July 1979, after "
                "Morarji Desai's resignation.",
                "His government never faced Parliament for a vote of "
                "confidence.",
                "He never won a general election as Janata's leader; his "
                "premiership had no electoral mandate.",
            ],
            "Do not describe Charan Singh's premiership as an elected "
            "mandate; it was an unconfirmed caretaker arrangement.",
            "Use this session to distinguish caretaker governments from "
            "mandated ones in any comparative Mains answer.",
            """CHARAN SINGH -> becomes PM, JULY 1979, after Desai's resignation
CONFIDENCE VOTE -> never faced in Parliament
ELECTION -> never won as Janata's leader
STATUS -> caretaker interlude, not a mandate""",
            "Charan Singh's caretaker government, from July 1979, is the "
            "unconfirmed premiership that never faced a parliamentary "
            "confidence vote and never won a general election.",
        ),
        authored_session(
            "Indira Gandhi's return to power, January 1980",
            "Indira Gandhi's return to power in January 1980, on the "
            "scale of 353 of 529 seats, measured the public's verdict on "
            "Janata's failure rather than a fresh, positive endorsement of "
            "her own record.",
            [
                "Congress (I) won 353 of 529 seats in the January 1980 "
                "general election.",
                "This scale of victory reflected Janata's collapse rather "
                "than a renewed personal mandate for Indira Gandhi.",
                "Her return followed directly from Charan Singh's "
                "caretaker premiership, which never faced Parliament.",
            ],
            "Do not read the 1980 result as public endorsement of the "
            "Emergency; it was a verdict on Janata's governing failure.",
            "Use this session to answer questions on how coalition "
            "failure, not renewed popularity, restored Indira Gandhi.",
            """JANATA COLLAPSE -> 1979
ELECTION -> JANUARY 1980; CONGRESS (I) wins 353 of 529 seats
READING -> a verdict on Janata's failure
NOT -> a fresh, positive endorsement of Indira Gandhi or the Emergency""",
            "Indira Gandhi's January 1980 return to power is her Congress "
            "(I)'s 353-of-529-seat victory, read as a verdict on Janata's "
            "failure rather than a renewed personal mandate.",
        ),
        authored_session(
            "Sanjay Gandhi's death and Rajiv Gandhi's entry",
            "Sanjay Gandhi's death in an air crash in June 1980 removed "
            "Indira Gandhi's political heir apparent and brought his "
            "elder brother Rajiv Gandhi into active politics, a "
            "transition this topic notes without extending into Rajiv's "
            "own later premiership.",
            [
                "Sanjay Gandhi died in an air crash in June 1980, only "
                "months into Indira Gandhi's return to power.",
                "His death opened a succession question inside the "
                "Congress and the Gandhi family.",
                "Rajiv Gandhi entered active politics following his "
                "brother's death, a development this topic records but "
                "does not narrate further.",
            ],
            "Do not extend this topic's account into Rajiv Gandhi's own "
            "premiership; that belongs to the following topic.",
            "Use this session to mark the precise transition point "
            "between this topic and the following one on Rajiv Gandhi.",
            """JUNE 1980 -> Sanjay Gandhi dies in an air crash
CONSEQUENCE -> succession question opens inside the Congress
ENTRY -> Rajiv Gandhi enters active politics
BOUNDARY -> his own premiership belongs to the following topic""",
            "Sanjay Gandhi's death, June 1980, is the air-crash fatality "
            "that opened the succession question bringing Rajiv Gandhi "
            "into active politics, a transition this topic notes but does "
            "not narrate beyond.",
        ),
        authored_session(
            "The rise of Telugu Desam in Andhra Pradesh",
            "N.T. Rama Rao's Telugu Desam Party, founded and swept to "
            "power within a single year, demonstrated how regional "
            "self-respect and resentment of central interference could "
            "convert a film star's popularity into a durable regional "
            "party.",
            [
                "N.T. Rama Rao, a Telugu film star, founded the Telugu "
                "Desam Party.",
                "The party swept the 1983 Andhra Pradesh state election.",
                "Its platform combined Telugu self-respect with "
                "resentment of central interference in state politics.",
            ],
            "Do not describe Telugu Desam as a Congress splinter; it was "
            "a newly founded regional party.",
            "Use this session for any Mains question on the rise of "
            "regional parties as an independent electoral force.",
            """FOUNDER -> N.T. Rama Rao, a Telugu film star
PARTY -> Telugu Desam, newly founded
ELECTION -> sweeps the 1983 Andhra Pradesh state election
PLATFORM -> Telugu self-respect + resentment of central interference""",
            "The Telugu Desam Party is N.T. Rama Rao's newly founded "
            "regional party that swept the 1983 Andhra Pradesh election "
            "on a platform of Telugu self-respect and resistance to "
            "central interference.",
        ),
        authored_session(
            "The Left Front's West Bengal",
            "The Left Front, led by the Communist Party of India "
            "(Marxist) under Jyoti Basu, formed the government of West "
            "Bengal in 1977 and governed continuously thereafter, "
            "building the era's most durable agrarian-reformist regional "
            "regime.",
            [
                "The Left Front took office in West Bengal in 1977 under "
                "the CPI(M)'s Jyoti Basu.",
                "It governed the state continuously from that point "
                "onward.",
                "Its durability rested on an agrarian-reformist regime "
                "distinct from the Centre's own policy line.",
            ],
            "Do not confuse the Left Front's continuous West Bengal rule "
            "with a national-level Left government; its power was "
            "state-specific.",
            "Use this session to contrast durable, programmatic regional "
            "rule with the volatility of national coalition politics.",
            """LEFT FRONT -> takes office in WEST BENGAL, 1977
LEADER -> Jyoti Basu, CPI(M)
DURATION -> governs continuously thereafter
BASIS -> an agrarian-reformist regional regime""",
            "The Left Front is the CPI(M)-led coalition under Jyoti Basu "
            "that took office in West Bengal in 1977 and governed "
            "continuously thereafter through an agrarian-reformist "
            "programme.",
        ),
        authored_session(
            "The Assam Movement",
            "The Assam Movement, led by the All Assam Students' Union, "
            "mobilised sustained mass agitation on the question of "
            "illegal migration and 'foreigners', an issue the Centre "
            "struggled to contain through the early 1980s.",
            [
                "The All Assam Students' Union led the Assam Movement.",
                "Its central grievance was illegal migration and the "
                "'foreigner' question in the state.",
                "The Centre struggled to contain the agitation through "
                "the early 1980s, before its eventual 1985 accord.",
            ],
            "Do not describe the Assam Movement as a routine "
            "law-and-order episode; it was a sustained mass political "
            "agitation.",
            "Use this session to answer questions on migration-driven "
            "regional agitation and the limits of central authority.",
            """LED BY -> All Assam Students' Union (AASU)
GRIEVANCE -> illegal migration and the "foreigner" question
FORM -> sustained mass agitation
CENTRE'S POSITION -> struggled to contain it through the early 1980s""",
            "The Assam Movement is the AASU-led mass agitation over "
            "illegal migration and the 'foreigner' question that the "
            "Centre struggled to contain through the early 1980s.",
        ),
        authored_session(
            "Jammu and Kashmir: the Abdullah pattern",
            "Jammu and Kashmir's politics through this period followed a "
            "recurring pattern: elected governments led first by Sheikh "
            "Abdullah and then by his son Farooq Abdullah repeatedly "
            "faced central interference, corroding state-level "
            "democratic legitimacy.",
            [
                "Sheikh Abdullah and then Farooq Abdullah led Jammu and "
                "Kashmir's elected politics in this period.",
                "Their governments repeatedly faced central interference "
                "despite their electoral standing.",
                "This recurring pattern is recorded here strictly as a "
                "description of federal practice, without extending into "
                "present-day politics.",
            ],
            "Do not extend this account of the Abdullah pattern beyond "
            "the federal-interference description into any present-day "
            "political controversy.",
            "Use this session for a restrained factual answer on federal "
            "interference with elected state governments.",
            """LEADERSHIP -> Sheikh Abdullah, then son Farooq Abdullah
PATTERN -> elected state governments face central interference
EFFECT -> corrodes state-level democratic legitimacy
RESTRAINT -> recorded as federal practice, not present-day politics""",
            "The Abdullah pattern is the recurring 1970s-80s sequence in "
            "which the elected Jammu and Kashmir governments of Sheikh "
            "Abdullah and then Farooq Abdullah faced repeated central "
            "interference.",
        ),
        authored_session(
            "The Anandpur Sahib Resolution's demands",
            "The Anandpur Sahib Resolution codified Akali demands into a "
            "negotiable federal-economic charter, combining a territorial "
            "claim over Chandigarh, a call for a fairer river-waters "
            "share, and a request for greater state autonomy.",
            [
                "The Resolution claimed Chandigarh as a territorial "
                "demand.",
                "It sought a fairer share of river waters for Punjab.",
                "It called for greater state autonomy within the federal "
                "structure.",
            ],
            "Do not describe the Anandpur Sahib Resolution as a religious "
            "or secessionist charter at the point it was framed; it was "
            "a negotiable federal-economic document.",
            "Use this session to open any answer on the Punjab crisis's "
            "federal-economic origins.",
            """TERRITORIAL DEMAND -> Chandigarh
ECONOMIC DEMAND -> a fairer share of river waters
FEDERAL DEMAND -> greater state autonomy
CHARACTER AT FRAMING -> a negotiable federal-economic charter""",
            "The Anandpur Sahib Resolution is the Akali charter combining "
            "a Chandigarh territorial claim, a river-waters demand and a "
            "state-autonomy demand, framed as a negotiable "
            "federal-economic document.",
        ),
        authored_session(
            "The rise of Bhindranwale and militancy",
            "Once the Anandpur Sahib Resolution's demands went unsettled "
            "through ordinary negotiation, the vacated political space in "
            "Punjab was filled by the rise of Jarnail Singh Bhindranwale "
            "and armed militancy.",
            [
                "The Resolution's federal-economic demands remained "
                "unsettled through negotiation.",
                "Jarnail Singh Bhindranwale rose within the resulting "
                "vacated political space.",
                "His rise marked the shift from negotiable politics "
                "toward armed militancy in Punjab.",
            ],
            "Do not present Bhindranwale's rise as the crisis's origin; "
            "it followed the prior failure to settle the Resolution's "
            "negotiable demands.",
            "Use this session to trace the sequence from unsettled "
            "demand to militancy in any Punjab-crisis answer.",
            """STEP 1 -> Anandpur Sahib demands remain unsettled
STEP 2 -> the negotiable political space is vacated
STEP 3 -> Bhindranwale rises within that vacated space
STEP 4 -> armed militancy replaces negotiable politics""",
            "The rise of Bhindranwale is the shift from unsettled "
            "negotiable Akali demands to armed militancy in Punjab, "
            "filling the political space negotiation had failed to "
            "occupy.",
        ),
        authored_session(
            "Operation Blue Star and Indira Gandhi's assassination",
            "Operation Blue Star, the Army's June 1984 operation against "
            "militants entrenched in the Golden Temple complex, was "
            "followed within months by Indira Gandhi's assassination on "
            "31 October 1984, closing this topic's chronology.",
            [
                "Operation Blue Star took place in June 1984 against "
                "militants entrenched at the Golden Temple complex, "
                "Amritsar.",
                "Indira Gandhi was assassinated on 31 October 1984.",
                "This topic records neither casualty figures nor any "
                "community characterisation for either event.",
            ],
            "Do not state casualty figures or characterise any community "
            "when describing Operation Blue Star or the assassination.",
            "Use this session to close any Mains answer tracing the "
            "Punjab crisis to its October 1984 turning point, with "
            "restraint on unverified detail.",
            """OPERATION BLUE STAR -> JUNE 1984, Golden Temple complex, Amritsar
INTERVAL -> several months of continued tension
ASSASSINATION -> INDIRA GANDHI, 31 OCTOBER 1984
RESTRAINT -> no casualty figures, no community characterisation here""",
            "Operation Blue Star and Indira Gandhi's assassination are "
            "the June and 31 October 1984 events closing this topic's "
            "Punjab chronology, recorded here without casualty figures or "
            "community characterisation.",
        ),
        authored_session(
            "Comparative reading: five theatres of regional assertion",
            "Across Assam, Punjab, Andhra Pradesh, West Bengal and Jammu "
            "and Kashmir, demands pursued through elections were absorbed "
            "into competitive federal politics, while demands pursued "
            "outside elections after negotiation failed escalated toward "
            "crisis.",
            [
                "Andhra Pradesh's Telugu Desam and West Bengal's Left "
                "Front pursued their demands through elections and were "
                "absorbed into federal politics.",
                "Punjab's and Assam's demands, when negotiation failed, "
                "escalated toward crisis before their eventual 1985 "
                "accords.",
                "Jammu and Kashmir's Abdullah-led politics sits between "
                "these poles, electorally legitimate yet repeatedly "
                "subject to central interference.",
            ],
            "Do not treat all five theatres as identical; the "
            "comparative pattern lies in the route each demand took, "
            "electoral or otherwise, not in a single shared outcome.",
            "Use this session for any comparative Mains answer on "
            "regional assertion across multiple states in the 1980s.",
            """ELECTORAL ROUTE -> Andhra Pradesh, West Bengal: demands absorbed
NEGOTIATION-FAILURE ROUTE -> Punjab, Assam: demands escalate toward crisis
INTERFERENCE ROUTE -> Jammu and Kashmir: legitimate, yet interfered with
PATTERN -> the route taken, not the state, explains the outcome""",
            "The comparative reading of five regional theatres shows "
            "that the route a demand took, electoral absorption versus "
            "negotiation-failure escalation, explains its outcome more "
            "than the state itself.",
        ),
        authored_session(
            "Historiographical debates and the delayed-accommodation "
            "thesis",
            "Three historiographical readings dispute the Punjab crisis's "
            "cause, political mismanagement, national security, or "
            "federalist erosion, while the delayed-accommodation thesis "
            "argues that the 1985 accords resembled what could have been "
            "settled earlier, measuring the intervening years as the cost "
            "of postponement.",
            [
                "The political-management reading blames central "
                "mishandling of a negotiable federal-economic demand; "
                "Bipan Chandra privileges this reading.",
                "The national-security and federalist readings foreground "
                "cross-border militant support and the erosion of state "
                "autonomy respectively.",
                "The delayed-accommodation thesis holds that the 1985 "
                "accords resembled an earlier-available settlement, so "
                "the interval measured postponement's cost.",
            ],
            "Do not present only one historiographical reading as "
            "settled fact; this topic records all three while noting "
            "which one the owner privileges.",
            "Use this session to close a Mains answer with a "
            "historiographical evaluation of the Punjab crisis's causes.",
            """READING 1 -> political-management: mishandling of a negotiable demand
READING 2 -> national-security: cross-border militant support
READING 3 -> federalist: erosion of state autonomy
DELAYED-ACCOMMODATION -> 1985 accords resembled an earlier-available deal""",
            "The delayed-accommodation thesis argues that the 1985 "
            "Punjab and Assam accords resembled settlements available "
            "earlier, so the intervening years measured the cost of "
            "postponed negotiation rather than the absence of a workable "
            "deal.",
        ),
    ],
    "modern-indian-history-37": [
        authored_session(
            "Rajiv Gandhi's 1984 mandate and modernising agenda",
            "Rajiv Gandhi's record December 1984 mandate opened a "
            "modernising agenda of telecommunications, computerisation, "
            "science missions and panchayati raj, though panchayati raj "
            "itself would not acquire constitutional status until the "
            "1990s.",
            [
                "Congress won 404 of 514 elected seats in the December 1984 "
                "general election under Rajiv Gandhi, the largest mandate in Indian "
                "electoral history to that point.",
                "His government pushed telecommunications, "
                "computerisation and science and technology missions as "
                "modernising priorities.",
                "His panchayati raj initiative was a policy beginning; "
                "constitutional status came only later, with the 73rd "
                "and 74th Amendments.",
            ],
            "Do not describe panchayati raj as constitutionally "
            "established under Rajiv Gandhi; that came only with the "
            "73rd and 74th Amendments of the early 1990s.",
            "Use this session to open any answer crediting Rajiv "
            "Gandhi's technocratic agenda while noting its "
            "incompleteness.",
            """MANDATE -> DECEMBER 1984; Congress wins 404 of 514 elected seats, a record
AGENDA -> telecom, computerisation, science missions, panchayati raj
CAUTION -> panchayati raj not yet constitutional under Rajiv Gandhi
LATER COMPLETION -> 73rd and 74th Amendments, early 1990s""",
            "Rajiv Gandhi's 1984 mandate is his record December 1984 "
            "election victory that opened a modernising agenda whose "
            "panchayati raj component reached constitutional status only "
            "later, under the 73rd and 74th Amendments.",
        ),
        authored_session(
            "The Anti-Defection Act, 1985",
            "The Anti-Defection Act, the 52nd Constitutional Amendment "
            "of 1985, addressed the mass floor-crossing that had become "
            "routine Indian political practice since the 1967 election.",
            [
                "The Act is the 52nd Constitutional Amendment, passed in "
                "1985 under Rajiv Gandhi.",
                "It targeted the routine floor-crossing that had "
                "characterised Indian politics since 1967.",
                "It is a Rajiv Gandhi-era reform, not a measure of any "
                "later government.",
            ],
            "Do not attribute the Anti-Defection Act to V.P. Singh's "
            "government; it was passed in 1985 under Rajiv Gandhi.",
            "Use this session to answer any question on constitutional "
            "responses to political defection.",
            """ACT -> Anti-Defection Act, the 52ND CONSTITUTIONAL AMENDMENT
YEAR -> 1985, under RAJIV GANDHI
TARGET -> routine floor-crossing since the 1967 election
NOT -> a V.P. Singh-era measure""",
            "The Anti-Defection Act, the 52nd Constitutional Amendment of "
            "1985 under Rajiv Gandhi, addressed the routine "
            "floor-crossing that had characterised Indian politics since "
            "1967.",
        ),
        authored_session(
            "The 1985 accords: Punjab, Assam and Mizoram",
            "Rajiv Gandhi settled three regional crises inherited from "
            "the previous decade through negotiation in a single year, "
            "1985: the Punjab accord with Harchand Singh Longowal, and "
            "separate Assam and Mizoram accords.",
            [
                "The Punjab accord was signed with Harchand Singh "
                "Longowal in 1985.",
                "Separate Assam and Mizoram accords were also concluded "
                "in 1985.",
                "All three accords settled crises inherited from the "
                "previous, Janata-Indira decade through negotiation "
                "rather than force.",
            ],
            "Do not credit these 1985 accords to any government other "
            "than Rajiv Gandhi's, and do not conflate the three separate "
            "agreements into one.",
            "Use this session to answer any question on Rajiv Gandhi's "
            "record of negotiated federal settlement.",
            """PUNJAB ACCORD -> Rajiv Gandhi and Harchand Singh Longowal, 1985
ASSAM ACCORD -> concluded 1985
MIZORAM ACCORD -> concluded 1985
METHOD -> negotiation, settling crises inherited from the prior decade""",
            "The 1985 accords are the three separate Punjab, Assam and "
            "Mizoram settlements Rajiv Gandhi concluded through "
            "negotiation, resolving regional crises inherited from the "
            "prior decade.",
        ),
        authored_session(
            "The Shah Bano case and its reversal",
            "The 1985 Shah Bano case and its 1986 legislative reversal, "
            "which overturned a Supreme Court maintenance ruling under "
            "conservative religious pressure, alienated liberal opinion "
            "and minority-rights advocates.",
            [
                "The Shah Bano case was decided by the Supreme Court in "
                "1985, granting maintenance.",
                "The ruling was legislatively reversed in 1986 under "
                "conservative religious pressure.",
                "The reversal alienated liberal opinion and "
                "minority-rights advocates.",
            ],
            "Do not describe the Shah Bano reversal as a judicial "
            "decision; it was a legislative reversal of a prior Supreme "
            "Court ruling.",
            "Use this session to answer any question on the political "
            "costs of identity-driven legislative reversal.",
            """SHAH BANO CASE -> Supreme Court maintenance ruling, 1985
REVERSAL -> legislative, 1986, under conservative religious pressure
EFFECT -> alienates liberal opinion and minority-rights advocates
NATURE -> a legislative act, not a judicial one""",
            "The Shah Bano reversal is the 1986 legislative overturning "
            "of a 1985 Supreme Court maintenance ruling, undertaken under "
            "conservative religious pressure and alienating liberal and "
            "minority-rights opinion.",
        ),
        authored_session(
            "The Ayodhya shrine opening",
            "The opening of the locks of the disputed Ayodhya shrine, "
            "intended by the government to balance the Shah Bano "
            "reversal, instead alienated the other community and "
            "energised Hindu mobilisation rather than restoring balance.",
            [
                "The government opened the locks of the disputed Ayodhya "
                "shrine after the Shah Bano reversal.",
                "The intention was to balance the prior concession to "
                "conservative Muslim opinion.",
                "The effect was to alienate the other community and "
                "energise Hindu mobilisation, not to achieve balance.",
            ],
            "Do not describe the Ayodhya shrine opening as a successful "
            "balancing act; it alienated both communities rather than "
            "reconciling them.",
            "Use this session to answer any question on the failure of "
            "symbolic identity concessions to cancel each other out.",
            """ACTION -> locks of the disputed Ayodhya shrine opened
INTENT -> balance the prior Shah Bano reversal
RESULT -> the other community is alienated instead
LESSON -> symbolic concessions to two sides do not cancel; they mobilise""",
            "The Ayodhya shrine opening is the government's action "
            "intended to balance the Shah Bano reversal that instead "
            "alienated the other community and energised Hindu "
            "mobilisation.",
        ),
        authored_session(
            "The Bofors scandal and its political fallout",
            "The 1987 Bofors arms-deal scandal destroyed Rajiv Gandhi's "
            "'Mr Clean' image, converting his own anti-corruption idiom "
            "into the platform his opponents used against his "
            "government.",
            [
                "The Bofors scandal broke in 1987 over an arms-deal "
                "commission controversy.",
                "It destroyed Rajiv Gandhi's 'Mr Clean' public image.",
                "His government's own anti-corruption idiom became the "
                "platform opponents used against it.",
            ],
            "Do not date the Bofors scandal to any year other than 1987, "
            "and do not describe it as unrelated to Rajiv Gandhi's "
            "declining popularity.",
            "Use this session to answer any question on how a "
            "corruption scandal converts a leader's own idiom against "
            "him.",
            """SCANDAL -> Bofors arms-deal controversy, breaks in 1987
IMAGE COST -> destroys Rajiv Gandhi's "Mr Clean" reputation
IRONY -> his own anti-corruption idiom turned against his government
CONSEQUENCE -> fuels the opposition that unseats Congress in 1989""",
            "The Bofors scandal is the 1987 arms-deal controversy that "
            "destroyed Rajiv Gandhi's 'Mr Clean' image and converted his "
            "own anti-corruption idiom into the platform used against his "
            "government.",
        ),
        authored_session(
            "V.P. Singh's exit and the National Front",
            "V.P. Singh's break from the Congress in 1987 and the "
            "subsequent formation of the Janata Dal and National Front in "
            "1988 united the opposition around a single anti-corruption "
            "platform against Bofors.",
            [
                "V.P. Singh left the Congress and formed the Jan Morcha "
                "in 1987.",
                "The Janata Dal and National Front followed in 1988, "
                "uniting the opposition.",
                "The unifying platform was anti-corruption, built "
                "directly on the Bofors controversy.",
            ],
            "Do not conflate the Jan Morcha (1987) with the Janata Dal "
            "and National Front (1988); they are sequential, not "
            "simultaneous, formations.",
            "Use this session to answer any question on how a corruption "
            "scandal can consolidate a fragmented opposition.",
            """1987 -> V.P. Singh exits Congress, forms the JAN MORCHA
1988 -> JANATA DAL and NATIONAL FRONT formed
PLATFORM -> anti-corruption, built on the Bofors controversy
EFFECT -> unites a previously fragmented opposition""",
            "V.P. Singh's exit is his 1987 break from Congress via the "
            "Jan Morcha, followed by the 1988 formation of the Janata Dal "
            "and National Front on an anti-corruption platform.",
        ),
        authored_session(
            "The 1989 election and party-system fragmentation",
            "The 1989 election fragmented the party system decisively: "
            "Congress fell from its 1984 record to about 197 seats, the "
            "BJP rose from 2 to 86 seats, and V.P. Singh's National Front "
            "formed a minority government with outside support from both "
            "the BJP and the Left.",
            [
                "Congress fell from its 1984 record to about 197 seats "
                "in 1989.",
                "The BJP rose from 2 seats in 1984 to 86 seats in 1989.",
                "V.P. Singh's National Front formed a minority "
                "government, supported from outside by both the BJP and "
                "the Left.",
            ],
            "Do not describe the National Front's outside support as "
            "coming from the Left alone; it came from both the BJP and "
            "the Left.",
            "Use this session to answer any question on the structural "
            "fragmentation of India's party system after 1989.",
            """CONGRESS -> falls from the 1984 record to about 197 seats
BJP -> rises from 2 seats (1984) to 86 seats (1989)
GOVERNMENT -> V.P. Singh's National Front, a MINORITY government
SUPPORT -> from outside, by BOTH the BJP and the Left""",
            "The 1989 election is the contest that fragmented the party "
            "system, reducing Congress to about 197 seats, raising the "
            "BJP to 86, and installing V.P. Singh's minority National "
            "Front government with outside support from both the BJP and "
            "the Left.",
        ),
        authored_session(
            "The Mandal Commission, 1990",
            "V.P. Singh's government implemented the Mandal Commission's "
            "recommendation of 27 per cent OBC reservation in 1990, "
            "taking total reservation toward roughly 49.5 per cent and "
            "triggering nationwide agitation.",
            [
                "The Mandal Commission's recommendation of 27 per cent "
                "reservation for OBCs in central government employment "
                "was implemented in 1990.",
                "Total reservation, combined with existing SC/ST quotas, "
                "moved toward roughly 49.5 per cent.",
                "The decision triggered nationwide agitation and "
                "organised OBC identity as a political bloc.",
            ],
            "Do not state the Mandal quota as 50 per cent for OBCs alone; "
            "it was 27 per cent for OBCs, within a combined total of "
            "about 49.5 per cent.",
            "Use this session to answer any question on caste-based "
            "reservation policy and its 1990 implementation.",
            """COMMISSION -> Mandal Commission recommendation implemented, 1990
QUOTA -> 27 per cent reservation for OBCs, central government jobs
TOTAL -> about 49.5 per cent combined with existing SC/ST quotas
EFFECT -> nationwide agitation; OBC identity organised as a political bloc""",
            "The Mandal Commission's 1990 implementation is V.P. Singh "
            "government's grant of 27 per cent OBC reservation in "
            "central jobs, taking total reservation to about 49.5 per "
            "cent and triggering nationwide agitation.",
        ),
        authored_session(
            "Advani's rath yatra and the Ayodhya mobilisation",
            "L.K. Advani's rath yatra in 1990 ran as a parallel, "
            "competing mobilisation to the Mandal announcement, "
            "intensifying the Ayodhya agitation along a religious axis "
            "distinct from Mandal's caste axis.",
            [
                "L.K. Advani undertook the rath yatra in 1990.",
                "It intensified the Ayodhya mobilisation as a "
                "religious-axis campaign.",
                "It ran parallel to, and in competition with, the "
                "same-year Mandal announcement.",
            ],
            "Do not date the Babri Masjid demolition to the same year as "
            "the rath yatra; the yatra was in 1990, the demolition "
            "followed on 6 December 1992.",
            "Use this session to answer any question on the "
            "simultaneous but distinct caste and religious mobilisations "
            "of 1990.",
            """MOBILISATION -> Advani's rath yatra, 1990
AXIS -> religious, intensifying the Ayodhya agitation
PARALLEL -> runs alongside the same-year Mandal (caste-axis) announcement
LATER OUTCOME -> Babri Masjid demolished, 6 December 1992""",
            "Advani's rath yatra, 1990, is the religious-axis "
            "mobilisation intensifying the Ayodhya agitation in parallel "
            "with, and distinct from, the same-year caste-axis Mandal "
            "announcement.",
        ),
        authored_session(
            "1991: the economic break and the Rao government",
            "The Narasimha Rao government's 1991 launch of economic "
            "liberalisation, with Manmohan Singh as Finance Minister, was "
            "compelled by a balance-of-payments crisis rather than a "
            "pre-existing political consensus for reform.",
            [
                "The Narasimha Rao government took office in 1991 and "
                "launched economic liberalisation.",
                "Manmohan Singh served as Finance Minister and led the "
                "reform programme.",
                "The reform was compelled by a balance-of-payments "
                "crisis, not by prior political agreement.",
            ],
            "Do not credit the 1991 reforms to any prior government's "
            "design; they were a crisis-compelled break led by the "
            "incoming Rao government.",
            "Use this session to answer any question on the "
            "political-economy conditions that enable reform under "
            "crisis.",
            """GOVERNMENT -> Narasimha Rao takes office, 1991
POLICY -> economic liberalisation launched
FINANCE MINISTER -> Manmohan Singh
TRIGGER -> a balance-of-payments crisis, not a prior consensus""",
            "The 1991 economic break is the Narasimha Rao government's "
            "crisis-compelled launch of economic liberalisation under "
            "Finance Minister Manmohan Singh, triggered by a "
            "balance-of-payments crisis rather than a pre-existing "
            "consensus.",
        ),
        authored_session(
            "Rajiv Gandhi's assassination, 1991",
            "Rajiv Gandhi was assassinated in 1991 during the very "
            "general election campaign that would bring the Narasimha "
            "Rao government to office, an event this topic records "
            "without further elaboration of its circumstances.",
            [
                "Rajiv Gandhi was assassinated in 1991.",
                "The assassination occurred during the general election "
                "campaign that preceded the Narasimha Rao government.",
                "This topic records the fact and its timing without "
                "further elaboration of circumstances.",
            ],
            "Do not elaborate on the circumstances of the assassination "
            "beyond its 1991 date and its place within the election "
            "campaign preceding the Rao government.",
            "Use this session only to mark the chronological fact and "
            "its proximity to the 1991 transition, not for detailed "
            "narrative.",
            """EVENT -> Rajiv Gandhi assassinated in 1991
CONTEXT -> during the general election campaign
CONSEQUENCE -> precedes the incoming Narasimha Rao government
RESTRAINT -> no further elaboration of circumstances here""",
            "Rajiv Gandhi's assassination in 1991 is the fatal event "
            "during the general election campaign that preceded the "
            "Narasimha Rao government, recorded here without further "
            "elaboration of circumstances.",
        ),
        authored_session(
            "The Babri Masjid demolition, 1992",
            "The Babri Masjid at Ayodhya was demolished on 6 December "
            "1992, the culmination of the mobilisation begun by the 1990 "
            "rath yatra, and a defining rupture of the decade's "
            "religious-axis politics.",
            [
                "The Babri Masjid was demolished on 6 December 1992.",
                "This event was the culmination of the mobilisation begun "
                "by the 1990 rath yatra.",
                "It marked a defining rupture in the decade's "
                "religious-axis politics.",
            ],
            "Do not date the Babri Masjid demolition to 1990; the yatra "
            "was 1990, the demolition was 6 December 1992.",
            "Use this session to close any answer on the religious-axis "
            "mobilisation trajectory from 1990 to 1992.",
            """EVENT -> Babri Masjid demolished, 6 DECEMBER 1992
ORIGIN -> culmination of the mobilisation begun by the 1990 rath yatra
SIGNIFICANCE -> a defining rupture of religious-axis politics
DO NOT CONFUSE -> yatra (1990) with demolition (1992)""",
            "The Babri Masjid demolition, 6 December 1992, is the "
            "culmination of the religious-axis mobilisation begun by the "
            "1990 rath yatra, a defining rupture of the decade's "
            "politics.",
        ),
        authored_session(
            "The coalition decade, 1996-99",
            "The 1990s closed with a decade-defining pattern of "
            "coalition government: a short 1996 BJP government under "
            "Vajpayee, the United Front governments of Deve Gowda and "
            "Gujral, and the NDA formed in 1998 and consolidated after "
            "the 1999 election.",
            [
                "Atal Bihari Vajpayee led a short BJP government in "
                "1996.",
                "The United Front governed under H.D. Deve Gowda and "
                "then I.K. Gujral through 1996-98.",
                "The National Democratic Alliance was formed in 1998 "
                "under Vajpayee and consolidated after the 1999 "
                "election.",
            ],
            "Do not describe Vajpayee's premiership as beginning only in "
            "1998; he first led a short government in 1996.",
            "Use this session to answer any question establishing "
            "coalition government as the decade's normal form.",
            """1996 -> short BJP government, Atal Bihari Vajpayee
1996-98 -> UNITED FRONT: Deve Gowda, then Gujral
1998 -> NATIONAL DEMOCRATIC ALLIANCE formed, under Vajpayee
1999 -> NDA consolidated after the general election""",
            "The coalition decade, 1996-99, is the sequence of the short "
            "1996 Vajpayee government, the Deve Gowda and Gujral United "
            "Front governments, and the NDA formed in 1998 and "
            "consolidated in 1999.",
        ),
        authored_session(
            "Synthesis: Mandal, Mandir and Market",
            "Bipan Chandra's synthesis reads 1989 to 1992 as the "
            "simultaneous convergence of OBC assertion, Hindutva "
            "mobilisation and economic liberalisation, three forces that "
            "together dismantled the Nehruvian consensus and, in a rival "
            "reading, deepened democratic competition instead.",
            [
                "The three forces, Mandal (caste), Mandir (religion) and "
                "Market (economic liberalisation), converged between "
                "1989 and 1992.",
                "Chandra's reading treats this convergence as "
                "dismantling the Nehruvian political-economic consensus.",
                "A rival, democratic-deepening reading treats the same "
                "convergence as widening political participation rather "
                "than eroding it.",
            ],
            "Do not present the declinist reading as the only "
            "interpretation; this topic records both the declinist and "
            "the democratic-deepening readings.",
            "Use this session to close any Mains answer with a balanced "
            "historiographical evaluation of the 1989-1999 "
            "transformation.",
            """MANDAL -> caste-axis assertion, 1990
MANDIR -> religious-axis mobilisation, 1990-92
MARKET -> economic liberalisation, from 1991
TWO READINGS -> Nehruvian-consensus decline vs democratic deepening""",
            "The Mandal-Mandir-Market synthesis is Bipan Chandra's "
            "reading of the 1989-1992 convergence of caste assertion, "
            "religious mobilisation and economic liberalisation as "
            "jointly dismantling the Nehruvian consensus, against a "
            "rival democratic-deepening interpretation.",
        ),
    ],
}


TOPIC_CHRONOLOGY: dict[str, list[str]] = {
    "modern-indian-history-36": [
        "January 1977",
        "March 1977",
        "1979",
        "July 1979",
        "January 1980",
        "June 1980",
        "1983",
        "1977",
        "June 1984",
        "31 October 1984",
        "1985",
    ],
    "modern-indian-history-37": [
        "December 1984",
        "52nd Constitutional Amendment",
        "Assam and Mizoram accords",
        "Shah Bano case of 1985",
        "1987",
        "1988",
        "1989",
        "1990",
        "rath yatra in 1990",
        "1991",
        "assassinated in 1991",
        "6 December 1992",
        "1996",
    ],
}

FORBIDDEN_TOPIC_PHRASES: dict[str, list[str]] = {
    "modern-indian-history-36": [
        "Operation Blue Star took place in 1983",
        "Charan Singh won a general election as Janata's leader",
        "Indira Gandhi's 1980 return reflected a fresh positive mandate "
        "for the Emergency",
        "Telugu Desam grew out of the Congress",
        "the Punjab crisis began as a purely religious dispute",
    ],
    "modern-indian-history-37": [
        "the Anti-Defection Act was passed under V.P. Singh",
        "economic liberalisation began under Rajiv Gandhi",
        "the Mandal Commission recommended 50 per cent reservation for "
        "OBCs",
        "the Babri Masjid was demolished in 1990",
        "the National Front had outside support only from the Left",
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
        "scope": "Modern Indian History learner-v2 Topics 36-37",
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

    if key == "modern-indian-history-36":
        strict = [
            "Janata Party",
            "Morarji Desai",
            "dual membership",
            "Charan Singh",
            "353 of 529",
            "Sanjay Gandhi",
            "Telugu Desam",
            "N.T. Rama Rao",
            "Left Front",
            "Jyoti Basu",
            "Assam Movement",
            "All Assam Students' Union",
            "Sheikh Abdullah",
            "Farooq Abdullah",
            "Anandpur Sahib Resolution",
            "Bhindranwale",
            "Operation Blue Star",
            "31 October 1984",
            "44th Constitutional Amendment",
        ]
    else:
        strict = [
            "Rajiv Gandhi",
            "Anti-Defection Act",
            "52nd Constitutional Amendment",
            "Harchand Singh Longowal",
            "Shah Bano",
            "Ayodhya",
            "Bofors",
            "V.P. Singh",
            "Jan Morcha",
            "Janata Dal",
            "National Front",
            "Mandal Commission",
            "27 per cent",
            "rath yatra",
            "6 December 1992",
            "Narasimha Rao",
            "Manmohan Singh",
            "Vajpayee",
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
    """Topics 34-35 must remain exactly as their own generators authored them."""

    expected = ["modern-indian-history-34", "modern-indian-history-35"]
    if [config["key"] for config in previous.TOPICS] != expected:
        raise ValueError("Topics 34-35 configuration was mutated on import.")
    if set(previous.PANEL_DATA) != set(expected):
        raise ValueError("Topics 34-35 panel data was mutated on import.")


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
