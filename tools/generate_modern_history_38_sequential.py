"""Build Modern Indian History learner-v2 Topic 38.

This authoring-only generator writes complete reusable Markdown, a solved
workbook, a manual ASCII specification, a graphical specification, and a
tracker-free generation-one manifest for the post-independence synthesis
topic covering the economy, land, agriculture, caste, gender, communalism
and the institutions of the state (Topic 38). It deliberately does not
render PDFs, update the tracker, regenerate indexes, finalize generations,
or publish packages.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base
import generate_modern_history_36_37_sequential as previous


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
    / "modern-indian-history-38-2026-08-31-sequential.json"
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
        38,
        "Economy, Land, Society & State: A Post-Independence Synthesis",
        "38_Economy-Land-Society-and-State-A-Post-Independence-Synthesis.md",
        "38_Economy-Land-Society-and-State-A-Post-Independence-Synthesis.md",
        "38_Economy-Land-Society-and-State-A-Post-Independence-Synthesis_"
        "Complete-Topic-Package.md",
        [
            "basic/32_The-Nehru-Era-Hope-Foreign-Policy-and-Legacy.md",
            "basic/37_The-Rajiv-Years-and-Run-up-to-the-Millennium.md",
            "37_The-Rajiv-Years-and-Run-up-to-the-Millennium_Complete-Topic-"
            "Package.md",
        ],
        [],
        "No verified live current-affairs item is pegged to this topic. The "
        "owner's own Current-link section frames farm policy, OBC/Dalit "
        "politics, women's rights and state capacity as recurring "
        "analytical themes rather than as a dated news event, and that "
        "bounded, unattributed framing is preserved here rather than "
        "inventing a specific live source or date.",
        "The Basic and Advanced owner Markdown for this topic were "
        "reconciled against each other and against the folder's shared "
        "post-independence OCR source, Bipan Chandra, Mridula Mukherjee and "
        "Aditya Mukherjee, *India After Independence, 1947\u20132000*. Every "
        "date, name and institution used below already carries the owners' "
        "own \u2705 (source-backed) or \u26a0\ufe0f (inference) tagging, and "
        "that tagging is preserved rather than re-verified page by page "
        "against the raw PDF in this authoring pass.",
        "This owner carries nine routed Prelims demands across its own "
        "'2024-2025' and '2018-2023' PYQ Integration blocks "
        "(`_PYQ-ROUTING-PRELIMS-2024-2025.md`, "
        "`_PYQ-ROUTING-PRELIMS-2018-2023.md`), and both blocks are embedded "
        "verbatim below rather than re-solved. Seven of the nine are "
        "contemporary current-affairs items with no modern-history content "
        "and no supporting material in this repository's source books "
        "(Exercise Mitra Shakti-2023, the Gandhi Peace Prize jury, the "
        "first Kho Kho World Cup, the 45th Chess Olympiad records, the "
        "Laureus World Sports Awards, the Tokyo 2020 Olympics motto and new "
        "sports, and the ICC World Test Championship finalist criteria); "
        "these are routing artefacts, not history demands, and this "
        "authoring pass does not answer them or treat them as gaps in this "
        "topic. Of the remaining two, the 2019 Prelims GS-I Q2 demand on "
        "land-reforms legislation in post-independence India is a genuine "
        "history demand covered by this topic's land-reform bank, while "
        "the 2018 Prelims GS-I Q70 demand on the founders of the Hind "
        "Mazdoor Sabha (1948) is historical but unattested in the local "
        "source books and is recorded as an explicit single-fact gap "
        "rather than guessed. No Mains demand in the local 2018-2025 "
        "ledgers is routed to this owner.",
        [
            (
                "The economic model: IPRs and the Mahalanobis strategy, "
                "1948-56",
                "The Industrial Policy Resolutions of 1948 and 1956, "
                "together with the Mahalanobis-designed Second Plan of "
                "1956, gave the public sector the 'commanding heights' of "
                "the economy, especially in heavy industry.",
            ),
            (
                "Growth and the licence-permit raj",
                "Growth of about 4 per cent a year to the mid-1960s far "
                "exceeded the colonial rate, but a maze of licences and "
                "controls, the 'licence-permit raj', throttled efficiency.",
            ),
            (
                "Zamindari abolition, largely by 1956",
                "Zamindari abolition was largely complete by 1956 and made "
                "about 20 million superior tenants into owners, succeeding "
                "because it targeted a politically weak class with strong "
                "political backing behind the reform.",
            ),
            (
                "Tenancy and ceiling reform, largely failed",
                "Tenancy and ceiling legislation largely failed because "
                "oral and concealed tenancies were poorly recorded and "
                "evasion through benami transfers and family partition was "
                "common, since the rural classes targeted were the state's "
                "own political base.",
            ),
            (
                "Bhoodan could not substitute for structural reform",
                "The Bhoodan movement, led by Vinoba Bhave and begun at "
                "Pochampalli in 1951, could not substitute for structural "
                "land reform because much of the donated land was never "
                "effectively distributed.",
            ),
            (
                "The Green Revolution's HYV package, mid-1960s",
                "The Green Revolution's high-yielding-variety seed package, "
                "introduced from the mid-1960s, was initially concentrated "
                "in Punjab, Haryana and western Uttar Pradesh and in wheat "
                "cultivation.",
            ),
            (
                "The Green Revolution debate: diffusion versus inequality",
                "Bipan Chandra argues that the Green Revolution later "
                "spread to rice regions and other states, that its "
                "technology was broadly scale-neutral, and that early "
                "predictions of general class polarisation were "
                "overstated, while critics continue to stress unequal "
                "access, regional lags and ecological costs.",
            ),
            (
                "Naxalbari, 1967, and CPI(ML), 1969",
                "The Naxalbari uprising of 1967 launched the Naxalite "
                "movement, and the CPI(ML) was formed in 1969, following "
                "the earlier Telangana agrarian struggle.",
            ),
            (
                "The farmers' movements of the 1980s",
                "The rich-farmer movements of the 1980s, Sharad Joshi's "
                "Shetkari Sangathana at Nasik in 1980 and Mahendra Singh "
                "Tikait's Bharatiya Kisan Union at Sisauli in 1986, "
                "pursued market demands of prices, inputs and credit, a "
                "class content opposed to the landless and tenant "
                "struggles of Naxalbari and Telangana.",
            ),
            (
                "The Hindu Code Bill",
                "The proposed Hindu Code was enacted through the Hindu "
                "Marriage Act, 1955, and the Hindu Succession, Hindu "
                "Minority and Guardianship, and Hindu Adoptions and "
                "Maintenance Acts, 1956. These measures substantially "
                "expanded women's rights within Hindu personal law but did "
                "not create complete legal or social equality.",
            ),
            (
                "The women's movement, 1970s-90s",
                "A new women's movement from the 1970s to the 1990s took "
                "up dowry, rape and domestic violence, building on the "
                "major but incomplete Hindu-law reforms of 1955–56.",
            ),
            (
                "Caste: from Ambedkar to Mandal, 1990",
                "Untouchability was abolished and reservations extended, "
                "and caste became central to politics along a trajectory "
                "running from Ambedkar through the Dalit Panthers and the "
                "BSP to the Mandal Commission's implementation in 1990.",
            ),
            (
                "Communalism: revival and endemism",
                "Communalism revived from the 1960s and turned endemic "
                "after the late 1970s, and is analysed as an ideology "
                "rather than merely a sequence of riots.",
            ),
            (
                "1991 economic liberalisation",
                "A balance-of-payments crisis in 1991 forced economic "
                "liberalisation under Narasimha Rao and Manmohan Singh, a "
                "corrective to the earlier control raj rather than an "
                "abandonment of the model's original goals.",
            ),
            (
                "The self-reliance thread's changing content",
                "The idea of self-reliance runs continuously from the "
                "Swadeshi movement of 1905 through Gandhian khadi, "
                "nationalist fiscal demands, Nehruvian capital-goods "
                "capacity and licence-era insulation, to food "
                "self-reliance from the mid-1960s and finally to post-1991 "
                "competitiveness, with its content changing at each "
                "stage.",
            ),
            (
                "The agrarian distress-regime change thread",
                "Agrarian distress produced regime change only when it "
                "coincided with a political crisis of legitimacy, as in "
                "1857, 1967 and 1975-77, and produced remedial legislation "
                "or localised revolt alone when it did not, as after 1879.",
            ),
            (
                "The law-versus-society synthesis engine",
                "A recurring law-versus-society gap runs through this "
                "topic: formal legal reform began early for tenants, Dalits "
                "and women, but its scope and enforcement differed sharply; "
                "social transformation lagged, and excluded groups organised "
                "politically rather than remaining content with legislation.",
            ),
            (
                "Institutional decay amid democratic survival",
                "Bipan Chandra documents a 'crisis of governability': the "
                "decline of Parliament from the late 1960s, the erosion of "
                "the Cabinet by a dominant Prime Minister's Office from "
                "1969, defection politics curbed only by the 1985 "
                "Anti-Defection Act, and a delay-ridden judiciary and "
                "unreformed bureaucracy and police, even as democracy "
                "itself endured and deepened.",
            ),
            (
                "The land-reforms PYQ demand, 2019: a covered demand",
                "The 2019 Prelims GS-I Q2 demand on land-reforms "
                "legislation in post-independence India is a genuine "
                "history demand and is covered by this topic's "
                "land-reform bank.",
            ),
            (
                "The Hind Mazdoor Sabha gap and the current-affairs "
                "routing artefacts",
                "The 2018 Prelims GS-I Q70 demand on the founders of the "
                "Hind Mazdoor Sabha, 1948, is historical but unattested in "
                "the local source books and is recorded as an explicit "
                "single-fact gap, while seven further routed demands, "
                "Exercise Mitra Shakti-2023, the Gandhi Peace Prize jury, "
                "the first Kho Kho World Cup, the 45th Chess Olympiad "
                "records, the Laureus World Sports Awards, the Tokyo 2020 "
                "Olympics motto and new sports, and the ICC World Test "
                "Championship finalist criteria, are contemporary "
                "current-affairs routing artefacts with no modern-history "
                "content and are not answered from this topic.",
            ),
        ],
        [
            "Do not lump all land reform together: zamindari abolition "
            "succeeded; tenancy and ceiling reform largely failed.",
            "Bhoodan did not redistribute most donated land; treat it as "
            "a moral gesture, not a structural reform.",
            "The Green Revolution was not uniformly beneficial nor "
            "uniformly harmful; state both the diffusion argument and the "
            "inequality critique.",
            "Naxalbari occurred in 1967, not the 1970s; the CPI(ML) was "
            "formed in 1969.",
            "Do not merge the 1980s rich-farmer movements with "
            "Naxalbari-type struggles; their class content is opposed.",
            "The Hindu Code Bill is four separate Acts, not one unified "
            "code.",
            "Liberalisation began in 1991 under Narasimha Rao, not under "
            "Rajiv Gandhi.",
            "The roughly 4 per cent growth figure applies only to the "
            "period up to the mid-1960s; do not extend it to later "
            "decades.",
            "Do not fabricate a nationalisation year or statute name for "
            "any sector beyond what the source states; treat unsupported "
            "PYQ demands as bounded gaps instead.",
            "Agrarian distress alone rarely produced regime change; it "
            "required a coinciding political crisis of legitimacy.",
            "Communalism is analysed here as an ideology, not merely as a "
            "sequence of riots.",
            "Do not treat the seven current-affairs PYQ routing "
            "artefacts in this owner as history gaps; they belong to a "
            "current-affairs owner.",
            "Self-reliance's content changed at each historical stage; do "
            "not treat it as one unchanging idea across 1905-1991.",
        ],
        [
            (
                10,
                "Examine why zamindari abolition succeeded while tenancy "
                "and ceiling reform largely failed in post-independence "
                "India.",
                "Zamindari abolition succeeded because it targeted a "
                "politically weak intermediary class with strong "
                "political backing, while tenancy and ceiling reform "
                "failed because they required the state to act against "
                "the very rural classes on whose support it depended, "
                "compounded by poorly recorded oral tenancies and "
                "widespread evasion.",
                [2, 3, 4],
            ),
            (
                10,
                "Assess the social consequences of the Green Revolution.",
                "The Green Revolution secured food self-sufficiency from "
                "an initial concentration in Punjab, Haryana and western "
                "Uttar Pradesh; a balanced assessment states both "
                "Chandra's diffusion-and-scale-neutrality argument and the "
                "critics' evidence of unequal access, regional lag and "
                "ecological cost, rather than asserting either alone.",
                [5, 6],
            ),
            (
                15,
                "Trace the transformation of caste and gender relations "
                "in India since 1947.",
                "Major but incomplete Hindu-law reform for women in "
                "1955–56 and the legal abolition of untouchability for "
                "Dalits both "
                "preceded social change; the resulting law-versus-society "
                "gap converted both into political movements, running "
                "from the 1970s-90s women's movement to the Ambedkar-to-"
                "Mandal caste trajectory, with communalism's parallel "
                "revival marking the same period's limits.",
                [9, 10, 11, 12],
            ),
            (
                15,
                "'Agrarian distress produced regime change only when it "
                "coincided with a political crisis of legitimacy.' "
                "Discuss with reference to India's post-independence "
                "history.",
                "Agrarian distress by itself produced remedial legislation "
                "or localised revolt, as after 1879; it produced regime "
                "change only where it coincided with a crisis of "
                "legitimacy, as in 1857's annexation crisis, 1967's "
                "post-Nehru succession and devaluation, and 1975-77's "
                "discredited mandate, a pattern this topic's own Naxalbari "
                "and 1991 evidence corroborates from a different angle.",
                [15, 7, 13],
            ),
            (
                20,
                "How did India's economic model evolve from planning to "
                "liberalisation? Assess whether 1991 represented a "
                "correction or a repudiation of the Nehruvian model.",
                "Planning built the public-sector commanding heights and "
                "growth well above the colonial rate that the Nehruvian "
                "model promised, and it was undone by its own "
                "licence-permit raj; the 1991 balance-of-payments crisis "
                "and the reforms it forced are best read, on the "
                "institutional-decay evidence and the self-reliance "
                "thread's earlier redefinitions, as a correction of "
                "excess dirigisme rather than a repudiation of the "
                "model's original goals.",
                [0, 1, 13, 14, 17],
            ),
            (
                20,
                "'Independent India transformed its economy and its "
                "politics far more than its social structure.' Critically "
                "examine this verdict with reference to land, "
                "agriculture, caste, gender and the institutions of the "
                "state since 1947.",
                "The economy moved decisively from planning to "
                "liberalisation and politics moved from a Congress "
                "consensus to a genuinely federal, multi-party system, "
                "while land reform stalled at zamindari abolition, the "
                "Green Revolution's benefits stayed contested, and caste, "
                "gender and communal relations show law-versus-society "
                "gaps that outlasted both the economic and the political "
                "transformations, even as democratic institutions endured "
                "despite their own documented decay.",
                [0, 2, 3, 5, 6, 9, 10, 11, 12, 16, 17],
            ),
        ],
        [],
        [
            "Industrial Policy Resolutions",
            "Mahalanobis",
            "licence-permit raj",
            "Zamindari abolition",
            "20 million",
            "Bhoodan",
            "Vinoba Bhave",
            "Pochampalli",
            "Naxalbari",
            "CPI(ML)",
            "Sharad Joshi",
            "Mahendra Singh Tikait",
            "Hindu Code Bill",
            "Mandal Commission",
            "Narasimha Rao",
            "Manmohan Singh",
            "Hind Mazdoor Sabha",
            "land-reforms legislation",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-38": [
        (
            "The economic model's rise and break, 1948-91",
            "timeline",
            """IPR 1948/1956 + MAHALANOBIS PLAN -> public sector "commanding heights"
GROWTH -> about 4% a year to the mid-1960s, but LICENCE-PERMIT RAJ throttles it
1991 -> balance-of-payments crisis forces LIBERALISATION (Rao-Manmohan Singh)
READING -> a CORRECTION of excess dirigisme, not a repudiation of the model""",
            ["The economic model's rise and break, 1948-91"],
        ),
        (
            "Land reform disaggregated: zamindari vs tenancy vs ceiling",
            "comparison-table",
            """COMPONENT   | OUTCOME           | WHY
ZAMINDARI   | LARGELY SUCCEEDED | politically weak class, clear target
TENANCY     | LARGELY FAILED    | oral tenancies poorly recorded, evasion
CEILING     | LARGELY FAILED    | targeted the state's own political base""",
            ["Land reform disaggregated"],
        ),
        (
            "Bhoodan: gesture, not structural reform",
            "cause-effect",
            """MOVEMENT -> Bhoodan, led by Vinoba Bhave
BEGAN -> Pochampalli, 1951
METHOD -> voluntary land donation
LIMIT -> much donated land never effectively distributed; no structural reform""",
            ["Bhoodan and its limits"],
        ),
        (
            "The Green Revolution's contested verdict",
            "comparison",
            """CHANDRA'S READING -> diffusion to rice regions; scale-neutral technology
CRITICS' READING -> unequal access, regional lag, ecological cost
INITIAL CONCENTRATION -> Punjab, Haryana, western UP; wheat; mid-1960s
RULE -> state BOTH readings; do not assert either alone as settled""",
            ["The Green Revolution debate"],
        ),
        (
            "Agrarian struggle: three moments, three classes",
            "comparison-table",
            """TELANGANA (1946-47) -> landless and tenant struggle, at the moment of transfer
NAXALBARI (1967) -> launches Naxalite movement; CPI(ML) formed 1969
1980s FARMERS' MOVEMENTS -> Nasik (1980), Sisauli (1986); market demands
CLASS SHIFT -> from landless struggle to surplus-farmer market demands""",
            ["Agrarian struggle across three moments"],
        ),
        (
            "Law-versus-society: caste, gender and communalism",
            "comparison",
            """CASTE -> untouchability abolished; Ambedkar to Dalit Panthers, BSP, Mandal 1990
GENDER -> Hindu Code Bill (four Acts); women's movement, 1970s-90s
COMMUNALISM -> revived from the 1960s; endemic after the late 1970s; an ideology
COMMON PATTERN -> formal rights reform begins early; scope and social transformation lag""",
            ["The law-versus-society gap across caste, gender and communalism"],
        ),
        (
            "The synthesis engine: state capacity to political organisation",
            "flow",
            """STATE CAPACITY inherited from the colonial order
   -> deployed for planning and heavy industry (achieved)
   -> withheld from rural property (tenancy/ceiling reform fails)
   -> technology substituted for reform in agriculture (Green Revolution)
   -> formal rights reform begins; scope/enforcement lag; excluded groups organise""",
            ["The synthesis engine"],
        ),
        (
            "Thread 1: self-reliance's changing content, 1905-1991",
            "timeline",
            """SWADESHI (1905) -> boycott + indigenous enterprise
GANDHIAN (1920-47) -> khadi, moral self-reliance
PLANNING (1948-66) -> capital-goods capacity, IPR/Mahalanobis
1991 ONWARD -> self-reliance redefined as competitiveness""",
            ["Thread 1: the changing content of self-reliance"],
        ),
        (
            "Thread 2: agrarian distress and regime change",
            "comparison-table",
            """MOMENT     | DISTRESS                  | OUTCOME
1857       | taluqdar dispossession    | Revolt; taluqdars later restored
1967       | two harvest failures      | Congress loses eight states
1975-77    | drought, oil shock        | JP movement, Emergency, 1977 defeat""",
            ["Thread 2: agrarian distress and regime change"],
        ),
        (
            "Institutions in decay, democracy enduring",
            "cause-effect",
            """PARLIAMENT -> declining role from the late 1960s
CABINET -> eroded by a dominant PMO, from 1969
DEFECTION -> routine floor-crossing, curbed only by the 1985 Anti-Defection Act
YET -> democracy itself survived and deepened through this institutional decay""",
            ["Institutional decay amid democratic survival"],
        ),
        (
            "PYQ reconciliation: 9 routed demands, three categories",
            "classification",
            """9 ROUTED PRELIMS DEMANDS in this owner's local ledgers
CATEGORY 1 -> 7 current-affairs routing artefacts (NOT history; not answered)
CATEGORY 2 -> 1 covered history demand: land-reforms legislation, 2019
CATEGORY 3 -> 1 bounded gap: Hind Mazdoor Sabha founders, 1948, unattested""",
            ["The PYQ reconciliation"],
        ),
        (
            "Verdict scaffolds: three graded readings",
            "argument-tree",
            """MODEL VERDICT -> planning built the economy India needed; 1991 corrected it
LAND VERDICT -> reform worked as far as the state's political base allowed
SYNTHESIS VERDICT -> economy and politics transformed; social hierarchy least
USE -> pick the verdict matching the question's specific demand""",
            ["Verdict scaffolds for synthesis answers"],
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
    "modern-indian-history-38": [
        authored_session(
            "The economic model: from planning to the licence-permit raj",
            "India's economic model combined the Industrial Policy "
            "Resolutions of 1948 and 1956 with the Mahalanobis-designed "
            "Second Plan of 1956, giving the public sector commanding "
            "heights in heavy industry, and it achieved growth well above "
            "the colonial rate before its own controls became a drag on "
            "efficiency.",
            [
                "The Industrial Policy Resolutions of 1948 and 1956, and "
                "the Mahalanobis Second Plan of 1956, gave the public "
                "sector the 'commanding heights', especially in heavy "
                "industry.",
                "Growth of about 4 per cent a year to the mid-1960s far "
                "exceeded the colonial rate.",
                "A maze of licences and controls, the 'licence-permit "
                "raj', throttled efficiency even as the model delivered "
                "structural transformation.",
            ],
            "Do not extend the roughly 4 per cent growth figure beyond "
            "the mid-1960s period it describes.",
            "Use this session to open any answer assessing whether "
            "planning was a success or a failure.",
            """IPR 1948/1956 + MAHALANOBIS PLAN (1956) -> public sector "commanding heights"
GROWTH -> about 4% a year to the mid-1960s, exceeding the colonial rate
DRAG -> the "licence-permit raj": licences and controls throttle efficiency
CAUTION -> the ~4% figure applies only to the period up to the mid-1960s""",
            "The licence-permit raj is the maze of licences and controls "
            "that protected inefficiency and throttled competition even as "
            "the Industrial Policy Resolutions and the Mahalanobis Second "
            "Plan delivered growth above the colonial rate to the "
            "mid-1960s.",
        ),
        authored_session(
            "Zamindari abolition: why it succeeded",
            "Zamindari abolition, largely complete by 1956, made about 20 "
            "million superior tenants into owners, succeeding because it "
            "targeted a politically weak class with strong political "
            "backing behind the reform.",
            [
                "Zamindari abolition was largely complete by 1956.",
                "About 20 million superior tenants became owners as a "
                "result.",
                "The reform succeeded because the intermediaries it "
                "targeted were a politically weak class, unlike the "
                "beneficiaries of later, failed reforms.",
            ],
            "Do not describe zamindari abolition as incomplete or as a "
            "failure; it is this topic's clearest land-reform success.",
            "Use this session to answer the 'why did zamindari succeed' "
            "half of any disaggregated land-reform question.",
            """REFORM -> zamindari abolition, largely complete by 1956
BENEFICIARIES -> about 20 million superior tenants become owners
WHY IT SUCCEEDED -> targeted a politically weak class (intermediaries)
CONTRAST -> tenancy and ceiling reform, which targeted the state's own base""",
            "Zamindari abolition is the land reform, largely complete by "
            "1956, that made about 20 million superior tenants into "
            "owners by targeting the politically weak intermediary "
            "class.",
        ),
        authored_session(
            "Tenancy and ceiling reform: why they failed",
            "Tenancy and ceiling legislation largely failed because oral "
            "and concealed tenancies were poorly recorded and evasion "
            "through benami transfers and family partition was common, "
            "since these reforms targeted the state's own rural political "
            "base rather than a weak intermediary class.",
            [
                "Oral and concealed tenancies were poorly recorded, "
                "making tenancy reform difficult to enforce.",
                "Ceiling legislation was evaded through benami transfers "
                "and family partition.",
                "Both reforms targeted the rural classes on whose "
                "support the state's own political base depended.",
            ],
            "Do not lump tenancy and ceiling failure together with "
            "zamindari abolition's success; assess each component "
            "separately.",
            "Use this session to answer the 'why did tenancy and ceiling "
            "reform fail' half of any disaggregated land-reform "
            "question.",
            """TENANCY REFORM -> undermined by poorly recorded oral/concealed tenancies
CEILING LEGISLATION -> evaded via benami transfers and family partition
WHY -> both targeted the state's own rural political base
CONTRAST -> zamindari abolition, which targeted a politically weak class""",
            "Tenancy and ceiling reform are the land-reform components "
            "that largely failed because they targeted the state's own "
            "rural political base and were evaded through poor records, "
            "benami transfers and family partition.",
        ),
        authored_session(
            "Bhoodan: a gesture, not a structural reform",
            "The Bhoodan movement, led by Vinoba Bhave and begun at "
            "Pochampalli in 1951, could not substitute for structural "
            "land reform because much of the donated land was never "
            "effectively distributed.",
            [
                "Vinoba Bhave led the Bhoodan movement.",
                "It began at Pochampalli in 1951.",
                "Much of the land donated through Bhoodan was never "
                "effectively distributed to the landless.",
            ],
            "Do not treat Bhoodan as equivalent to structural land "
            "reform; it was a voluntary gesture that could not reallocate "
            "land at scale.",
            "Use this session to answer any question distinguishing "
            "voluntary movements from structural legislative reform.",
            """MOVEMENT -> Bhoodan, led by Vinoba Bhave
BEGAN -> Pochampalli, 1951
METHOD -> voluntary land donation
LIMIT -> much donated land never effectively distributed; no structural reform""",
            "Bhoodan is Vinoba Bhave's voluntary land-donation movement, "
            "begun at Pochampalli in 1951, whose failure to distribute "
            "most donated land shows it could not substitute for "
            "structural land reform.",
        ),
        authored_session(
            "The Green Revolution's package and its initial geography",
            "The Green Revolution's high-yielding-variety seed package, "
            "introduced from the mid-1960s, was initially concentrated in "
            "Punjab, Haryana and western Uttar Pradesh and in wheat "
            "cultivation.",
            [
                "The HYV seed package was introduced from the "
                "mid-1960s.",
                "Its initial concentration was in Punjab, Haryana and "
                "western Uttar Pradesh.",
                "Its initial crop focus was wheat.",
            ],
            "Do not describe the Green Revolution's initial geography as "
            "national; it began narrowly concentrated before any later "
            "spread.",
            "Use this session to open any answer on the Green "
            "Revolution's origins before addressing its later, contested "
            "spread.",
            """PACKAGE -> HYV seeds, introduced from the mid-1960s
INITIAL GEOGRAPHY -> Punjab, Haryana, western Uttar Pradesh
INITIAL CROP -> wheat
NEXT QUESTION -> did this concentration spread or entrench inequality?""",
            "The Green Revolution's HYV package is the high-yielding-"
            "variety seed technology introduced from the mid-1960s, "
            "initially concentrated in Punjab, Haryana and western Uttar "
            "Pradesh and in wheat.",
        ),
        authored_session(
            "The Green Revolution debate: diffusion versus inequality",
            "Bipan Chandra argues that the Green Revolution later spread "
            "to rice regions and other states, that its technology was "
            "broadly scale-neutral, and that early predictions of general "
            "class polarisation were overstated, while critics continue "
            "to stress unequal access, regional lags and ecological "
            "costs.",
            [
                "Chandra argues the Green Revolution later spread to "
                "rice regions and other states.",
                "Chandra argues the technology was broadly scale-neutral, "
                "not favouring only large farmers.",
                "Critics continue to stress unequal access, regional "
                "lags and ecological costs.",
            ],
            "Do not state only one side of the Green Revolution debate "
            "as settled fact; this topic requires both Chandra's "
            "diffusion argument and the critics' inequality critique.",
            "Use this session to answer any 'critically examine' "
            "question on the Green Revolution's social consequences.",
            """CHANDRA'S READING -> diffusion to rice regions; broadly scale-neutral technology
CRITICS' READING -> unequal access, regional lags, ecological costs
BOTH REQUIRED -> a balanced answer states both readings, not one alone
ERROR -> asserting either reading alone is a factual-discipline failure""",
            "The Green Revolution debate is the contested assessment "
            "between Chandra's diffusion-and-scale-neutrality reading and "
            "the critics' unequal-access-and-ecological-cost reading, "
            "both of which a balanced answer must state.",
        ),
        authored_session(
            "Agrarian struggle from Naxalbari to the 1980s farmers' "
            "movements",
            "The Naxalbari uprising of 1967 launched the Naxalite "
            "movement, with the CPI(ML) formed in 1969, while the "
            "rich-farmer movements of the 1980s, Nasik in 1980 and "
            "Sisauli in 1986, pursued opposed market demands of prices, "
            "inputs and credit.",
            [
                "The Naxalbari uprising of 1967 launched the Naxalite "
                "movement, and the CPI(ML) was formed in 1969.",
                "Sharad Joshi's Shetkari Sangathana began at Nasik in "
                "1980.",
                "Mahendra Singh Tikait's Bharatiya Kisan Union organised "
                "at Sisauli in 1986, pursuing market demands opposed to "
                "Naxalbari's landless struggle.",
            ],
            "Do not merge Naxalbari-type struggles with the 1980s "
            "farmers' movements; they represent opposed rural class "
            "interests.",
            "Use this session to answer any question tracing the "
            "changing class content of agrarian struggle after 1947.",
            """NAXALBARI (1967) -> launches the Naxalite movement; CPI(ML) formed 1969
NASIK (1980) -> Sharad Joshi's Shetkari Sangathana; market demands
SISAULI (1986) -> Mahendra Singh Tikait's Bharatiya Kisan Union
CLASS SHIFT -> landless struggle (1967) to surplus-farmer demands (1980s)""",
            "The agrarian-struggle sequence runs from the 1967 Naxalbari "
            "uprising, launching the Naxalite movement, to the opposed "
            "market-demand movements of Nasik (1980) and Sisauli (1986), "
            "marking a shift in rural class content.",
        ),
        authored_session(
            "The Hindu Code Bill and the women's movement",
            "The proposed Hindu Code was enacted through four statutes in "
            "1955–56. They substantially expanded women's rights within "
            "Hindu personal law without creating complete legal or social "
            "equality; a new women's movement from the 1970s to the 1990s "
            "then took up dowry, rape and domestic violence.",
            [
                "The four statutes were the Hindu Marriage Act, 1955, and "
                "the Hindu Succession, Hindu Minority and Guardianship, and "
                "Hindu Adoptions and Maintenance Acts, 1956.",
                "They substantially expanded women's rights within Hindu "
                "personal law but left important inequalities intact.",
                "A new women's movement from the 1970s to the 1990s took "
                "up dowry, rape and domestic violence.",
            ],
            "Do not describe the Hindu Code Bill as a single unified "
            "code; it was enacted as four separate Acts.",
            "Use this session to answer any question on the legal and "
            "political trajectory of gender reform since 1947.",
            """PROPOSED HINDU CODE -> enacted through FOUR statutes in 1955-56
ACTS -> Marriage (1955); Succession, Minority & Guardianship, Adoptions & Maintenance (1956)
EFFECT -> major rights expansion within Hindu personal law, not complete equality
WOMEN'S MOVEMENT -> 1970s-1990s, takes up dowry, rape, domestic violence
NOT -> a single unified code""",
            "The Hindu-law reform package comprises the Hindu Marriage Act, "
            "1955, and three 1956 Acts on succession, minority and "
            "guardianship, and adoptions and maintenance; it expanded "
            "women's rights without establishing complete equality.",
        ),
        authored_session(
            "Caste politics: from Ambedkar to Mandal",
            "Untouchability was abolished and reservations extended, and "
            "caste became central to Indian politics along a trajectory "
            "running from Ambedkar through the Dalit Panthers and the "
            "BSP to the Mandal Commission's implementation in 1990.",
            [
                "Untouchability was abolished and reservations were "
                "extended.",
                "The political trajectory runs from Ambedkar through the "
                "Dalit Panthers to the BSP.",
                "The Mandal Commission's recommendations were implemented "
                "in 1990, making caste central to national politics.",
            ],
            "Do not treat Mandal's 1990 implementation as the starting "
            "point of caste politics; it is the culmination of a "
            "trajectory running back to Ambedkar.",
            "Use this session to answer any question tracing the "
            "political trajectory of caste since independence.",
            """LEGAL BASE -> untouchability abolished; reservations extended
TRAJECTORY -> Ambedkar -> Dalit Panthers -> BSP -> Mandal Commission, 1990
EFFECT -> caste becomes central to national politics
NOT -> a starting point in 1990; it is a culmination""",
            "The caste-politics trajectory runs from the legal abolition "
            "of untouchability and Ambedkar's leadership through the "
            "Dalit Panthers and the BSP to the Mandal Commission's 1990 "
            "implementation, which made caste central to national "
            "politics.",
        ),
        authored_session(
            "Communalism as ideology",
            "Communalism revived from the 1960s and turned endemic after "
            "the late 1970s, and this topic analyses it as an ideology "
            "rather than merely a sequence of riots.",
            [
                "Communalism revived from the 1960s.",
                "It turned endemic after the late 1970s.",
                "This topic treats communalism as an ideology, with "
                "violence as a symptom rather than the whole "
                "phenomenon.",
            ],
            "Do not reduce communalism to a law-and-order problem; this "
            "topic requires treating it as an ideology.",
            "Use this session to answer any question asking you to "
            "analyse communalism beyond its violent episodes.",
            """REVIVAL -> from the 1960s
ENDEMIC -> after the late 1970s
FRAMING -> an ideology, not merely a sequence of riots
IMPLICATION -> violence is a symptom of the ideology, not the whole of it""",
            "Communalism, in this topic's framing, is the ideology that "
            "revived from the 1960s and turned endemic after the late "
            "1970s, of which riots are a symptom rather than the whole "
            "phenomenon.",
        ),
        authored_session(
            "1991: liberalisation as correction",
            "A balance-of-payments crisis in 1991 forced economic "
            "liberalisation under Narasimha Rao and Manmohan Singh, a "
            "change this topic frames as a correction of excessive "
            "dirigisme rather than an abandonment of the model's "
            "original goals.",
            [
                "A balance-of-payments crisis in 1991 forced economic "
                "liberalisation.",
                "Narasimha Rao and Manmohan Singh led the reform.",
                "The reform is framed as a correction of the control raj, "
                "retaining the original goals of growth, self-reliance "
                "and poverty removal while changing the instruments.",
            ],
            "Do not describe 1991 as a repudiation of the Nehruvian "
            "model; this topic frames it as a correction of its later "
            "excess.",
            "Use this session to answer any question on whether 1991 "
            "represented continuity or rupture in India's economic "
            "policy.",
            """TRIGGER -> balance-of-payments crisis, 1991
LEADERSHIP -> Narasimha Rao and Manmohan Singh
FRAMING -> a correction of dirigiste excess, not a repudiation of the model
CONTINUITY -> growth, self-reliance and poverty removal remain the goals""",
            "The 1991 reforms are the Narasimha-Rao-and-Manmohan-Singh-led "
            "liberalisation, forced by a balance-of-payments crisis and "
            "framed here as a correction of dirigiste excess rather than "
            "an abandonment of the original developmental goals.",
        ),
        authored_session(
            "Thread 1: self-reliance's changing content, 1905-1991",
            "The idea of self-reliance runs continuously from the 1905 "
            "Swadeshi movement through Gandhian khadi, nationalist fiscal "
            "demands, Nehruvian capital-goods capacity and licence-era "
            "insulation to post-1965 food self-reliance and finally "
            "post-1991 competitiveness, with its content changing at "
            "every stage.",
            [
                "Self-reliance began with the 1905 Swadeshi movement's "
                "boycott and indigenous enterprise.",
                "It was redefined successively as Gandhian khadi, "
                "nationalist fiscal autonomy, Nehruvian capital-goods "
                "capacity, and licence-era insulation.",
                "It was redefined again as food self-reliance from the "
                "mid-1960s and finally as competitiveness after 1991.",
            ],
            "Do not treat self-reliance as one unchanging idea across "
            "1905 to 1991; its content changed at every stage, each "
            "following the demonstrated failure of the previous one.",
            "Use this session to answer any long-duration question "
            "tracing a single concept's changing content across Indian "
            "history.",
            """1905 SWADESHI -> boycott + indigenous enterprise
1920-47 GANDHIAN -> khadi, moral self-reliance
1948-66 PLANNING -> capital-goods capacity (IPR/Mahalanobis)
1991 ONWARD -> self-reliance redefined as competitiveness""",
            "Thread 1 traces self-reliance's continuous word but changing "
            "content from the 1905 Swadeshi movement through Gandhian, "
            "nationalist, planning-era and licence-era redefinitions to "
            "post-1991 competitiveness.",
        ),
        authored_session(
            "Thread 2: agrarian distress and regime change",
            "Agrarian distress produced regime change only when it "
            "coincided with a political crisis of legitimacy, as in "
            "1857, 1967 and 1975-77, and produced remedial legislation or "
            "localised revolt alone when it did not.",
            [
                "In 1857, agrarian distress coincided with the crisis of "
                "annexation and contributed to the Revolt.",
                "In 1967, two harvest failures coincided with a "
                "post-Nehru succession crisis, and Congress lost eight "
                "states.",
                "In 1975-77, drought and the oil shock coincided with a "
                "discredited mandate, contributing to the JP movement, "
                "the Emergency and the 1977 defeat.",
            ],
            "Do not treat agrarian distress alone as sufficient to "
            "produce regime change; the coinciding political-legitimacy "
            "crisis is the necessary second condition.",
            "Use this session to answer any question on the relationship "
            "between economic distress and political change in Indian "
            "history.",
            """1857 -> distress + crisis of annexation -> the Revolt
1967 -> harvest failures + succession crisis -> Congress loses eight states
1975-77 -> drought, oil shock + discredited mandate -> Emergency, 1977 defeat
RULE -> distress alone yields remedial legislation, not regime change""",
            "Thread 2 is the pattern by which agrarian distress produced "
            "regime change only when it coincided with a political "
            "crisis of legitimacy, as in 1857, 1967 and 1975-77, rather "
            "than through economic distress alone.",
        ),
        authored_session(
            "The synthesis engine and institutional decay",
            "State capacity inherited from the colonial order was "
            "deployed for planning but withheld from rural property, and "
            "while democracy itself endured, Parliament, the Cabinet, "
            "defection controls and the judiciary all show a documented "
            "institutional decay alongside that endurance.",
            [
                "State capacity was deployed for planning and heavy "
                "industry, but withheld from acting against rural "
                "property in tenancy and ceiling reform.",
                "Parliament's role declined from the late 1960s, and the "
                "Cabinet was eroded by a dominant Prime Minister's Office "
                "from 1969.",
                "Defection politics were curbed only by the 1985 "
                "Anti-Defection Act, and the judiciary and bureaucracy "
                "remained delay-ridden and unreformed.",
            ],
            "Do not conclude that institutional decay meant democracy "
            "collapsed; this topic states that democracy survived and "
            "deepened despite this decay.",
            "Use this session to answer any question on the relationship "
            "between institutional decay and democratic survival in "
            "India.",
            """STATE CAPACITY -> deployed for planning; withheld from rural property
PARLIAMENT -> declining role from the late 1960s
CABINET -> eroded by a dominant PMO, from 1969
DEFECTION -> curbed only by the 1985 Anti-Defection Act; democracy still endures""",
            "The synthesis engine and institutional decay together "
            "describe how state capacity was deployed selectively and "
            "how Parliament, the Cabinet and defection controls decayed "
            "even as Indian democracy itself endured and deepened.",
        ),
        authored_session(
            "The PYQ reconciliation: covered demand and bounded gap",
            "This owner carries nine routed Prelims demands, of which "
            "the 2019 land-reforms-legislation demand is a genuine "
            "history demand this topic covers, the 2018 Hind Mazdoor "
            "Sabha founders demand is an explicit, unattested gap, and "
            "the remaining seven are current-affairs routing artefacts "
            "outside this topic's scope.",
            [
                "The 2019 Prelims GS-I Q2 demand on land-reforms "
                "legislation in post-independence India is covered by "
                "this topic's land-reform bank.",
                "The 2018 Prelims GS-I Q70 demand on the founders of the "
                "Hind Mazdoor Sabha, 1948, is historical but unattested "
                "in the local source books and is recorded as an "
                "explicit single-fact gap.",
                "The remaining seven routed demands are contemporary "
                "current-affairs items with no modern-history content and "
                "are not answered from this topic.",
            ],
            "Do not treat the seven current-affairs routing artefacts as "
            "gaps in this topic, and do not guess the founders of the "
            "Hind Mazdoor Sabha from memory.",
            "Use this session only to state the reconciliation "
            "transparently; route the current-affairs artefacts to a "
            "current-affairs owner and leave the Hind Mazdoor Sabha "
            "founders as an open gap.",
            """9 ROUTED PRELIMS DEMANDS in this owner's local ledgers
COVERED -> land-reforms legislation, 2019 Prelims GS-I Q2
BOUNDED GAP -> Hind Mazdoor Sabha founders, 1948, 2018 Prelims GS-I Q70
OUT OF SCOPE -> 7 current-affairs routing artefacts, not history demands""",
            "The PYQ reconciliation is this owner's transparent "
            "accounting of nine routed Prelims demands into one covered "
            "history demand, one bounded unattested gap, and seven "
            "out-of-scope current-affairs routing artefacts.",
        ),
    ],
}


TOPIC_CHRONOLOGY: dict[str, list[str]] = {
    "modern-indian-history-38": [
        "1948",
        "1956",
        "mid-1960s",
        "1956",
        "Pochampalli in 1951",
        "mid-1960s",
        "1967",
        "1969",
        "1980",
        "1986",
        "1990",
        "1991",
        "1905",
        "1857",
        "1975-77",
        "1969",
        "1985",
        "2019",
        "2018",
    ],
}

FORBIDDEN_TOPIC_PHRASES: dict[str, list[str]] = {
    "modern-indian-history-38": [
        "all land reforms succeeded equally in post-independence India",
        "the Green Revolution widened inequality everywhere it reached",
        "the Naxalbari uprising took place in the 1970s",
        "economic liberalisation began under Rajiv Gandhi",
        "the Hindu Code Bill was enacted as a single unified code",
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
        "scope": "Modern Indian History learner-v2 Topic 38",
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

    strict = [
        "Industrial Policy Resolutions",
        "Mahalanobis",
        "licence-permit raj",
        "Zamindari abolition",
        "20 million",
        "Bhoodan",
        "Vinoba Bhave",
        "Pochampalli",
        "Naxalbari",
        "CPI(ML)",
        "Sharad Joshi",
        "Mahendra Singh Tikait",
        "Hindu Code Bill",
        "Mandal Commission",
        "Narasimha Rao",
        "Manmohan Singh",
        "Hind Mazdoor Sabha",
        "land-reforms legislation",
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
    """Topics 36-37 must remain exactly as their own generators authored them."""

    expected = ["modern-indian-history-36", "modern-indian-history-37"]
    if [config["key"] for config in previous.TOPICS] != expected:
        raise ValueError("Topics 36-37 configuration was mutated on import.")
    if set(previous.PANEL_DATA) != set(expected):
        raise ValueError("Topics 36-37 panel data was mutated on import.")


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
