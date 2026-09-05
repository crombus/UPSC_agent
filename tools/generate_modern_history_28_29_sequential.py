"""Build Modern Indian History learner-v2 Topics 28-29.

This authoring-only generator writes complete reusable Markdown, solved
workbooks, manual ASCII and graphical specifications, and tracker-free
generation-one manifests for the two closing post-1947 consolidation topics.
It deliberately does not render PDFs, update the tracker, regenerate indexes,
finalize generations, or publish packages.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import generate_modern_history_09_13_sequential as base
import generate_modern_history_26_27_sequential as previous


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
    / "modern-indian-history-28-29-2026-08-31-sequential.json"
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
            ROOT / "books" / "India After Independence-1947-2000 By Bipan Chandra.pdf",
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
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "UPSC Mains 2025 GS Paper 1.md",
            ROOT / "knowledge-export" / "Prelims PYQ" / "2025-GS1-Set A.md",
            ROOT / "knowledge-export" / "Prelims PYQ" / "Ans-2025-GS1.md",
        ]
    )
)
OFFICIAL_QUESTION_SOURCES = [
    path for path in OFFICIAL_QUESTION_SOURCES if path.is_file()
]

TOPIC_28_FACTS: list[tuple[str, str]] = [
    (
        "Attlee's paramountcy announcement of 20 February 1947",
        "The local OCR text of *India After Independence* records Clement "
        "Attlee's announcement of 20 February 1947 that His Majesty's "
        "Government did not intend to hand over their powers and obligations "
        "under paramountcy to any government of British India, a statement "
        "that several large princes read as a licence to claim sovereignty "
        "for themselves.",
    ),
    (
        "The divided princely response of April 1947",
        "A minority of states showed realism by joining the Constituent "
        "Assembly in April 1947 while the majority stayed away, and "
        "Travancore, Bhopal and Hyderabad publicly announced a desire for "
        "independent status, so princely opinion was already divided before "
        "any instrument was signed.",
    ),
    (
        "Jinnah's declaration of 18 June 1947",
        "M.A. Jinnah publicly declared on 18 June 1947 that the states would "
        "be independent sovereign states on the termination of paramountcy "
        "and were free to remain independent if they so desired, which "
        "encouraged the largest princes and made speed indispensable on the "
        "Indian side.",
    ),
    (
        "The States Department created on 27 June 1947",
        "Sardar Vallabhbhai Patel assumed additional charge of the newly "
        "created States Department on 27 June 1947 with V.P. Menon as its "
        "Secretary, so integration was the work of a named minister, a named "
        "secretary and a department, and never of one man acting alone.",
    ),
    (
        "The three-subject accession formula",
        "The Instrument of Accession asked acceding states to transfer only "
        "three subjects - Defence, External Affairs and Communications - a "
        "deliberately narrow demand that covered precisely what no princely "
        "state could exercise for itself while leaving internal "
        "administration untouched for the moment.",
    ),
    (
        "Paramountcy lapsed rather than being transferred",
        "British paramountcy over the princely states lapsed when British "
        "rule ended on 15 August 1947 and it was never transferred to India "
        "or Pakistan, so the Union's authority over princely India had to be "
        "constructed by agreement and pressure rather than inherited by "
        "legal succession.",
    ),
    (
        "The counting discipline of more than 560 states",
        "There were more than 560 princely states at independence, and the "
        "familiar totals of 562 and 565 differ by counting convention rather "
        "than by historical fact, so a safe answer writes more than 560 and "
        "never asserts either total as the single correct figure.",
    ),
    (
        "All but three acceded by the transfer of power",
        "Every state except Junagadh, Jammu and Kashmir and Hyderabad had "
        "acceded to India by 15 August 1947, so the three famous crisis cases "
        "were exceptions inside an overwhelmingly successful negotiation and "
        "not the normal pattern of accession.",
    ),
    (
        "Junagadh: a ruler at odds with his own people",
        "Junagadh was a small Saurashtra state surrounded by Indian territory "
        "and without geographical contiguity with Pakistan, yet its Nawab "
        "announced accession to Pakistan, its overwhelmingly Hindu population "
        "organised a movement that forced him to flee, and its Dewan Shah "
        "Nawaz Bhutto then invited the Government of India to intervene.",
    ),
    (
        "Kashmir: invasion in October 1947 before accession",
        "Tribal invaders entered Kashmir in October 1947 and pushed towards "
        "Srinagar, Maharaja Hari Singh appealed to India for military "
        "assistance, and troops were flown in only after the Instrument of "
        "Accession had been signed, so invasion preceded accession and "
        "accession preceded the airlift.",
    ),
    (
        "Sheikh Abdullah and the National Conference",
        "Kashmir's principal popular political force, the National Conference "
        "under Sheikh Abdullah, favoured accession to India and Abdullah was "
        "installed as head of the state's administration, which is why the "
        "Kashmir case cannot be reduced to a private transaction between a "
        "Maharaja and New Delhi.",
    ),
    (
        "Hyderabad's standstill agreement of November 1947",
        "The Government of India signed a standstill agreement with the Nizam "
        "of Hyderabad in November 1947 in the hope that negotiation and "
        "representative government inside the state would make merger easier, "
        "so force in Hyderabad came after, and not instead of, a documented "
        "attempt at settlement.",
    ),
    (
        "The reference to the United Nations on 30 December 1947",
        "The Government of India referred the Kashmir problem to the Security "
        "Council of the United Nations on 30 December 1947 asking for "
        "vacation of aggression, and this package records that referral and "
        "the fighting that followed without narrating any later contested "
        "political or constitutional claim.",
    ),
    (
        "The second stage of integration from December 1947",
        "The second and harder stage of full integration began in December "
        "1947, when smaller states were merged with neighbouring provinces or "
        "grouped into new unions, so accession was only the first of two "
        "distinct achievements and never the whole of integration.",
    ),
    (
        "The Junagadh plebiscite of February 1948",
        "A plebiscite held in Junagadh in February 1948 went in favour of "
        "joining India, and although the local source describes that result "
        "as overwhelming, this package states no percentage because no "
        "audited polling figure is held anywhere in the repository.",
    ),
    (
        "Operation Polo and Hyderabad in September 1948",
        "Hyderabad was integrated in September 1948 through the operation "
        "commonly called Operation Polo or the Police Action, after which the "
        "Nizam surrendered and acceded to the Indian Union, and no casualty "
        "or troop figure for that episode is asserted here.",
    ),
    (
        "Unions, mergers and the making of administrable units",
        "Large numbers of small states were consolidated into new unions such "
        "as Madhya Bharat, Rajasthan, the Patiala and East Punjab States "
        "Union, Saurashtra and Travancore-Cochin, while Mysore, Hyderabad and "
        "Jammu and Kashmir retained their original form as separate states of "
        "the Union.",
    ),
    (
        "Privy purses as a continuing cost, not an immediate abolition",
        "Rulers who surrendered power received privy purses and retained "
        "titles, succession and ceremonial privileges, and these settlements "
        "were not abolished during the initial integration; the repository "
        "owner dates their abolition to 1971, and this package asserts no "
        "amount for any purse.",
    ),
    (
        "Adoption on 26 November 1949 and commencement on 26 January 1950",
        "The Constituent Assembly, presided over by Dr Rajendra Prasad with "
        "B.R. Ambedkar chairing the Drafting Committee, adopted the "
        "Constitution on 26 November 1949 and it came into force on 26 "
        "January 1950, which is the date on which India became a republic and "
        "princely subjects became citizens.",
    ),
    (
        "The Sardar Patel 150th anniversary commemoration",
        "The Ministry of Culture records a two-year commemoration of Sardar "
        "Vallabhbhai Patel's 150th birth anniversary launched at the Statue "
        "of Unity on 31 October 2024, and a PIB Backgrounder of 30 October "
        "2025 records that Rashtriya Ekta Diwas is observed annually on 31 "
        "October and was first celebrated in 2014.",
    ),
]

TOPIC_28_TRAPS = [
    "Paramountcy lapsed; it was never transferred to India or Pakistan, and "
    "an answer that says otherwise removes the whole problem the States "
    "Department existed to solve.",
    "Write more than 560 princely states; 562 and 565 are counting "
    "conventions, not rival historical events.",
    "The Instrument of Accession covered Defence, External Affairs and "
    "Communications only; it did not transfer internal administration on the "
    "day it was signed.",
    "Accession, merger, democratisation and constitutional incorporation are "
    "four different stages; collapsing them into a single act of accession is "
    "the commonest structural error in this topic.",
    "Junagadh, Hyderabad and Kashmir differed in the ruler's choice, the "
    "population's composition, the state's geography and the security "
    "situation; treating them as one problem destroys the comparison.",
    "Operation Polo belongs to Hyderabad in September 1948; the Junagadh "
    "plebiscite belongs to February 1948; the Kashmir tribal invasion belongs "
    "to October 1947.",
    "Privy purses and princely privileges were retained at integration and "
    "were not abolished during the initial accession; do not assert any "
    "amount for any purse.",
    "India became independent on 15 August 1947 and a republic on 26 January "
    "1950; the two dates answer two different questions.",
    "Never quote a casualty figure, a troop number or a plebiscite percentage "
    "for any accession episode, because the repository holds no audited "
    "figure for any of them.",
    "Keep later constitutional and political controversies out of a history "
    "answer on accession; this owner records the historical process, not "
    "present-day disputes.",
    "Patel's achievement was institutional as well as personal; naming V.P. "
    "Menon and the States Department is part of the correct answer, not an "
    "optional embellishment.",
]

TOPIC_28_MAINS: list[tuple[int, str, str, list[int]]] = [
    (
        10,
        "Assess the significance of the lapse of British paramountcy for the "
        "integration of the princely states.",
        "The lapse of paramountcy converted integration from an inheritance "
        "into a construction project, and the speed of the Indian response "
        "between June and August 1947 is what prevented that legal vacuum "
        "from hardening into a political one.",
        [5, 0, 2, 3],
    ),
    (
        10,
        "Explain why the Instrument of Accession initially demanded only "
        "three subjects from acceding states.",
        "The instrument's narrowness was its strength: by asking only for "
        "Defence, External Affairs and Communications it demanded exactly "
        "what no state could supply for itself, which made acceptance cheap "
        "in appearance and decisive in substance.",
        [4, 3, 7, 13],
    ),
    (
        15,
        "Compare Junagadh, Hyderabad and Kashmir as three distinct failures "
        "of the accession formula rather than three versions of one problem.",
        "The three cases failed the formula in three different ways - a ruler "
        "at odds with his people, a ruler seeking sovereignty, and a ruler "
        "paralysed between two dominions - which is precisely why three "
        "different instruments were used to settle them.",
        [8, 9, 11, 14, 15],
    ),
    (
        15,
        "Trace the process by which accession in 1947 was converted into "
        "administrative and constitutional integration.",
        "Integration was a sequence and not an event: accession on three "
        "subjects, then merger and the creation of unions, then "
        "democratisation inside the former states, and finally constitutional "
        "incorporation that dissolved princely subjecthood into citizenship.",
        [13, 16, 17, 18],
    ),
    (
        20,
        "\"Integration succeeded because it asked for little at the moment "
        "when refusing anything was impossible.\" Critically examine.",
        "The sequencing thesis explains most of the outcome but not all of "
        "it: the narrow demand and the moment of maximum uncertainty carried "
        "the great majority of states, while popular movements, financial "
        "concessions and, in one case, force carried the remainder.",
        [5, 4, 7, 13, 17, 15],
    ),
    (
        20,
        "Examine how the territorial accession of 1947 was completed by the "
        "constitutional settlement of 1950.",
        "Accession created a Union of acceding states; the Constitution "
        "created a republic of citizens, and it is the second event, not the "
        "first, that made integration irreversible by removing the legal "
        "category of a prince's subject.",
        [3, 13, 16, 17, 18, 19],
    ),
]

TOPIC_28_PYQ_SOLUTIONS: list[tuple[str, str, str, str, str]] = [
    (
        "2021",
        "Mains GS-I Q3",
        "Assess the main administrative issues and socio-cultural problems in "
        "the integration process of Indian Princely States. (Answer in 150 "
        "words)",
        "verbatim-official-stem-verified-locally in the repository export of "
        "the 2021 General Studies Paper I question paper, and routed to this "
        "owner at 10 marks by the audited local Mains routing ledger",
        "Open by separating the two halves of the demand, because the "
        "directive is Assess and the examiner has named administrative issues "
        "and socio-cultural problems as distinct heads. On the administrative "
        "side, state that paramountcy lapsed rather than being transferred, "
        "so a department had to be built from nothing: Patel took additional "
        "charge of the States Department on 27 June 1947 with V.P. Menon as "
        "Secretary, and the machinery had to standardise instruments, absorb "
        "more than 560 units of wildly unequal size, merge unviable states "
        "into unions such as Madhya Bharat, Rajasthan, the Patiala and East "
        "Punjab States Union, Saurashtra and Travancore-Cochin, and then "
        "extend courts, services, revenue systems and elections into "
        "territories that had never known them. On the socio-cultural side, "
        "note the dynastic legitimacy of rulers, the survival of titles, "
        "successions and ceremonial privileges through the privy-purse "
        "settlement, the very uneven pace of democratisation inside former "
        "states, and the communal and regional sensitivities visible in "
        "Junagadh's ruler-subject mismatch and in the Razakar mobilisation in "
        "Hyderabad. Add one qualification: the process mixed persuasion, "
        "popular pressure, plebiscite and, in September 1948, force, so a "
        "single administrative narrative is inadequate. Close by grading the "
        "outcome: the administrative problem was solved quickly and the "
        "socio-cultural one slowly, which is why the Constitution's grant of "
        "a single citizenship on 26 January 1950 mattered more than any "
        "individual instrument of accession.",
    ),
    (
        "2018-2026",
        "Prelims GS-I",
        "No objective question in the audited local Prelims routing ledgers "
        "for 2018-2023, 2024-2025 or 2026 is routed to this owner.",
        "unresolved-locally; the package asserts no Prelims stem, no option "
        "set and no answer letter for this topic",
        "Treat this as a transparent zero-direct-PYQ audit rather than as a "
        "gap to be filled with an invented question. The examinable surface is "
        "nevertheless dense and matchable: paramountcy lapsed rather than "
        "being transferred; the Instrument of Accession covered Defence, "
        "External Affairs and Communications; Operation Polo is Hyderabad in "
        "September 1948; the Junagadh plebiscite is February 1948; the "
        "Kashmir tribal invasion is October 1947; the Constitution was adopted "
        "on 26 November 1949 and commenced on 26 January 1950. Revise those "
        "as matching pairs of actor, instrument, place and date, and do not "
        "relabel any adjacent Polity or International Relations question as a "
        "Modern History Prelims PYQ for this owner.",
    ),
]

TOPIC_28_REQUIRED_TERMS = [
    "paramountcy",
    "Instrument of Accession",
    "Defence, External Affairs and Communications",
    "V.P. Menon",
    "States Department",
    "more than 560",
    "Junagadh",
    "Hyderabad",
    "Operation Polo",
    "Sheikh Abdullah",
    "standstill agreement",
    "privy purses",
    "Madhya Bharat",
    "26 January 1950",
    "Rashtriya Ekta Diwas",
    "Statue of Unity",
]

TOPIC_29_FACTS: list[tuple[str, str]] = [
    (
        "Landless agricultural labour from 1871 onwards",
        "The local OCR text of *India After Independence* records that "
        "landless agricultural labourers grew from about 13 per cent of the "
        "agricultural population in 1871 to about 28 per cent by the middle "
        "of the twentieth century, and this package carries that movement "
        "strictly as the source's attributed estimate.",
    ),
    (
        "The development of underdevelopment",
        "Chandra describes the colonial economic outcome as the development "
        "of underdevelopment, a phrase he expressly attributes to A. Gunder "
        "Frank, meaning that real changes in railways, administration and "
        "education were locked inside a colonial framework that generated "
        "dependence and poverty rather than growth.",
    ),
    (
        "Stagnant agriculture and a rentier agrarian structure",
        "The same source records a decline of about 14 per cent in per capita "
        "agricultural production between 1901 and 1941 with a larger fall in "
        "foodgrains, alongside an agrarian structure dominated by landlords, "
        "moneylenders and the colonial state, and these figures are carried "
        "as the source's own attributed estimates.",
    ),
    (
        "Literacy and life expectancy at the moment of independence",
        "The source records that in 1951 nearly 84 per cent of Indians were "
        "illiterate with illiteracy at about 92 per cent among women, and "
        "that an Indian born between 1940 and 1951 could expect to live "
        "barely thirty-two years; every one of these numbers must be "
        "attributed and never rounded into a fresh claim.",
    ),
    (
        "The colonial state: authoritarian core, liberal fragments",
        "The colonial state was basically authoritarian and autocratic yet "
        "carried liberal fragments such as the rule of law, a relatively "
        "independent judiciary and limited press freedoms, and the republic "
        "inherited that apparatus of services, police, codes and district "
        "administration and had to convert an instrument of order into an "
        "instrument of development.",
    ),
    (
        "The colonial franchise of about 3 and about 15 per cent",
        "The source records that only about 3 per cent of Indians could vote "
        "after 1919 and about 15 per cent after 1935, so representative "
        "institutions did exist under colonial rule while the electorate "
        "entitled to use them remained a small fraction of the population.",
    ),
    (
        "Universal adult franchise as the republican break",
        "The republic did not widen the colonial franchise by degrees but "
        "replaced it outright with universal adult franchise, which is the "
        "sharpest single contrast available between a colonial liability and "
        "a republican choice and the fact that best answers a consolidation "
        "question.",
    ),
    (
        "The national movement as an institutional asset",
        "Against the economic liabilities stands a political asset: a tested "
        "all-India leadership including Nehru, Patel, Rajendra Prasad, "
        "Maulana Azad and Rajagopalachari, a party organised in every "
        "province, and settled commitments to democracy, civil liberties, "
        "secularism and social reform.",
    ),
    (
        "Independence on 15 August 1947 and the simultaneity of crises",
        "India became independent on 15 August 1947 and immediately faced "
        "refugee movement, communal killing, the division of the army and the "
        "treasury, princely integration and fighting in Kashmir at the same "
        "time, so the achievement of the initial years was simultaneity "
        "survived rather than any single problem solved.",
    ),
    (
        "Nearly six million refugees entering India",
        "The source records nearly six million refugees pouring into India "
        "after Partition, and this is a one-directional figure for people "
        "entering India that must never be presented as the total "
        "displacement in both directions across the new border.",
    ),
    (
        "Chandra's mortality estimate of roughly 500,000",
        "The source states that nearly 500,000 people were killed within a "
        "few months of Partition, but this is Chandra's estimate and is not "
        "settled scholarship, because wider scholarship offers substantially "
        "different totals, so the figure must always be attributed and never "
        "asserted as an agreed death toll.",
    ),
    (
        "The assets settlement of January 1948",
        "In January 1948, following a fast by Gandhi, the Government of India "
        "paid Pakistan Rs 550 million as part of the assets of Partition even "
        "while fearing how the money might be used, and this figure is "
        "carried as the source's attributed record of one specific transfer "
        "rather than as a full account of partition finance.",
    ),
    (
        "The assassination of Gandhi on 30 January 1948",
        "Gandhi was assassinated on 30 January 1948 by Nathuram Godse, "
        "described in the source as a Hindu communal fanatic, and the "
        "government immediately banned the Rashtriya Swayamsevak Sangh and "
        "arrested most of its leaders and functionaries.",
    ),
    (
        "The Communist insurrectionary turn from February 1948",
        "From February 1948 the Communist Party of India, under the line "
        "associated with B.T. Ranadive, declared independence false and "
        "turned to armed struggle, so the party that later became a "
        "parliamentary opposition first tested an insurrectionary road inside "
        "the new republic.",
    ),
    (
        "The lifting of the ban in July 1949 on stated conditions",
        "The ban on the Rashtriya Swayamsevak Sangh was lifted in July 1949 "
        "after it accepted conditions laid down by Patel as Home Minister: a "
        "written and published constitution, restriction to cultural "
        "activity, renunciation of violence and secrecy, loyalty to India's "
        "flag and Constitution, and democratic internal organisation.",
    ),
    (
        "Adoption on 26 November 1949 and commencement on 26 January 1950",
        "The Constitution was adopted on 26 November 1949 and came into force "
        "on 26 January 1950, so independence in 1947 and the republic in 1950 "
        "are two different constitutional events that must never be merged "
        "into a single date.",
    ),
    (
        "The Nehru-Liaquat Pact of 8 April 1950",
        "On 8 April 1950 the prime ministers of India and Pakistan signed the "
        "agreement known as the Nehru-Liaquat Pact, spelt Nehru-Liaqat in the "
        "local text, to secure the protection of minorities in both "
        "countries; two ministers resigned in protest and migration from East "
        "Bengal continued despite it.",
    ),
    (
        "Telangana called off by mid-1951 and the CPI legalised",
        "The Telangana armed struggle, spelt Telengana in the local text, was "
        "called off by mid-1951 as the Communist Party of India abandoned "
        "armed struggle for the parliamentary path, after which the party was "
        "legalised, its cadres were released and it was allowed to contest "
        "the first general elections.",
    ),
    (
        "Pondicherry in 1954 and Goa in December 1961",
        "The French possessions centred on Pondicherry were handed over after "
        "prolonged negotiation in 1954 and Indian troops entered Goa on the "
        "night of 17 December 1961 in the action known as Operation Vijay, so "
        "the territorial map was completed years after 1947 and Goa's "
        "Operation Vijay must never be confused with Hyderabad's Operation "
        "Polo of September 1948.",
    ),
    (
        "The republic's anniversary as a live commemorative anchor",
        "A Ministry of Defence release carried by the Press Information "
        "Bureau on 25 January 2026 records that the 77th Republic Day was "
        "celebrated on 26 January 2026 on the parade theme of unity in "
        "diversity, and the ordinal is itself a teaching device because "
        "counting 1950 as the first Republic Day is exactly what makes 2026 "
        "the seventy-seventh.",
    ),
]

TOPIC_29_TRAPS = [
    "Separate the two inheritances: the colonial economic and administrative "
    "liabilities on one side and the national movement's political assets on "
    "the other; an answer that mixes them cannot explain why a poor country "
    "sustained a democracy.",
    "The colonial franchise was about 3 per cent after 1919 and about 15 per "
    "cent after 1935; universal adult franchise was a republican decision, "
    "not a colonial inheritance.",
    "Attribute every estimate. Literacy, life expectancy, refugee numbers, "
    "partition mortality, landless labour and the assets transfer are all "
    "source-attributed figures, not audited national statistics.",
    "The figure of nearly six million refugees is one-directional movement "
    "into India; it is not the total displacement in both directions.",
    "Chandra's estimate of roughly 500,000 partition deaths is not settled "
    "scholarship; name the author and record that wider scholarship differs "
    "substantially.",
    "Gandhi was assassinated on 30 January 1948 by Nathuram Godse; the "
    "Rashtriya Swayamsevak Sangh ban followed immediately and was lifted in "
    "July 1949 on stated conditions, and these dates should be used only in "
    "the sourced form given here.",
    "The Nehru-Liaquat Pact belongs to 8 April 1950; it addressed the "
    "protection of minorities and did not end migration from East Bengal.",
    "The Communist Party of India moved from insurrection to elections; the "
    "Telangana struggle was called off by mid-1951 and the party was then "
    "legalised, so neither an unbroken parliamentary record nor a permanent "
    "insurgency is accurate.",
    "Pondicherry was transferred in 1954 and Goa was integrated in December "
    "1961; neither joined the Union in 1947.",
    "Goa's Operation Vijay of December 1961 is not Hyderabad's Operation Polo "
    "of September 1948; the two operations differ in date, adversary and "
    "constitutional character.",
    "Treat democracy, secularism, planning, civilian control of the armed "
    "forces and non-alignment as a founding consensus with both achievements "
    "and limits, rather than as either a triumph narrative or a failure "
    "narrative.",
    "The 2025 GS-I demand names four domains - polity, economy, education and "
    "international relations - and an answer that omits education or "
    "international relations has failed the directive however good its "
    "history is.",
]

TOPIC_29_MAINS: list[tuple[int, str, str, list[int]]] = [
    (
        10,
        "Explain what the Indian republic inherited from colonial rule in the "
        "economic sphere.",
        "The republic inherited underdevelopment as a structure rather than "
        "as mere poverty: a dependent and stagnant economy whose real changes "
        "in transport, administration and education were locked inside a "
        "framework that reproduced dependence.",
        [1, 2, 0, 4],
    ),
    (
        10,
        "\"The colonial franchise and universal adult suffrage belong to two "
        "different political worlds.\" Discuss.",
        "The contrast between an electorate of about 3 per cent after 1919 "
        "and about 15 per cent after 1935 and the immediate adoption of "
        "universal adult franchise is the clearest measure of how far the "
        "republic broke with the state it inherited.",
        [5, 6, 7, 15],
    ),
    (
        15,
        "Assess the challenges of the initial years of the republic and the "
        "means by which the leadership contained them.",
        "The achievement of the initial years was simultaneity survived: "
        "refugee resettlement, communal violence after Gandhi's assassination, "
        "an armed communist insurgency and a contested frontier were handled "
        "together, by a combination of secular reassurance, negotiated "
        "settlement and coercive capacity, without suspending democracy.",
        [8, 9, 12, 13, 17],
    ),
    (
        15,
        "Examine how the legacy of the national movement shaped the "
        "institutions and values of the Indian republic.",
        "India's democratic survival is best explained by institutional "
        "residue rather than by individual virtue: a movement that had "
        "already practised elections, argument and organisation for three "
        "decades supplied the legitimacy that a new and desperately poor "
        "state could not have manufactured for itself.",
        [7, 6, 4, 15],
    ),
    (
        20,
        "\"India began its republican journey with an economy of scarcity but "
        "a polity of strength.\" Critically examine.",
        "The asset-and-liability reading holds, but only if both sides are "
        "stated with their limits: the political inheritance was genuinely "
        "stabilising, while the deferral of land reform, mass education and "
        "female literacy shows that a polity of strength did not "
        "automatically convert into a society of opportunity.",
        [1, 3, 5, 7, 6, 18],
    ),
    (
        20,
        "Evaluate the founding consensus of the early republic - democracy, "
        "secularism, planning, civilian control and non-alignment - by its "
        "achievements and its limits.",
        "The founding consensus was a coherent settlement rather than a list "
        "of preferences, and it should be graded rather than celebrated: each "
        "of its five commitments was honoured institutionally and each was "
        "qualified in practice within the first decade and a half.",
        [7, 8, 14, 17, 18, 19],
    ),
]

TOPIC_29_PYQ_SOLUTIONS: list[tuple[str, str, str, str, str]] = [
    (
        "2025",
        "Mains GS-I Q12",
        "Trace India's consolidation process during early phase of "
        "independence in terms of polity, economy, education and "
        "international relations. (Answer in 250 words)",
        "verbatim-official-stem-verified-locally in the repository export of "
        "the 2025 General Studies Paper I question paper, and routed to this "
        "owner at 15 marks by the audited local Mains routing ledger",
        "The directive is Trace and the examiner has named four domains, so "
        "the structure is fixed before a word is written: one tight paragraph "
        "each for polity, economy, education and international relations, "
        "each carrying one named institution or decision and one honest "
        "limitation, and a closing sentence that links them. Open with a "
        "single-line thesis that consolidation was pursued on four fronts at "
        "once and that each front protected the others. For polity, trace the "
        "movement from a fragmented inheritance to a single constitutional "
        "order: the accession and merger of more than 560 princely states, "
        "the adoption of the Constitution on 26 November 1949 and its "
        "commencement on 26 January 1950, and above all the replacement of a "
        "colonial franchise of about 3 per cent after 1919 and about 15 per "
        "cent after 1935 by universal adult franchise; the limitation is the "
        "strong-centre bias and the unresolved regional question. For "
        "economy, trace the move from the development of underdevelopment to "
        "a state-led planned framework with a public-sector core and land "
        "reform legislation; the limitation is slow growth and land reform "
        "that was largely unimplemented. For education, begin from the "
        "source's finding that nearly 84 per cent of Indians were illiterate "
        "in 1951, with about 92 per cent illiteracy among women, and trace "
        "the deliberate state investment in universities, technical "
        "institutions and scientific research capacity; the limitation is "
        "that expansion was elite-first while primary education and female "
        "literacy lagged. For international relations, trace the choice of "
        "non-alignment and Asian solidarity by a militarily weak new state "
        "already fighting on a contested frontier, and complete the map with "
        "Pondicherry in 1954 and Goa in December 1961; the limitation is "
        "limited hard power. Close by showing the interlock: the political "
        "settlement made planning possible, planning required peace, peace "
        "was purchased by non-alignment, and education was the long-term "
        "condition of all three.",
    ),
    (
        "2021",
        "Mains GS-I Q3",
        "Assess the main administrative issues and socio-cultural problems in "
        "the integration process of Indian Princely States. (Answer in 150 "
        "words)",
        "adjacent-owner-routed-demand; the audited ledger routes this stem to "
        "the Topic 28 owner, and it is carried here only because princely "
        "integration is one of the four simultaneous crises of the initial "
        "years",
        "Do not answer this question from the colonial-legacy owner. Use it "
        "instead as the integration paragraph inside a consolidation answer: "
        "state that paramountcy lapsed rather than being transferred, that "
        "the States Department under Patel and V.P. Menon secured accession "
        "on Defence, External Affairs and Communications, and that merger, "
        "democratisation and constitutional incorporation followed. The full "
        "solved treatment, including the socio-cultural head that the "
        "examiner names separately, belongs to the Topic 28 owner and is "
        "solved there; this package neither duplicates it nor claims it.",
    ),
]

TOPIC_29_REQUIRED_TERMS = [
    "development of underdevelopment",
    "A. Gunder Frank",
    "universal adult franchise",
    "after 1919",
    "after 1935",
    "Nathuram Godse",
    "Nehru-Liaquat Pact",
    "Telangana",
    "B.T. Ranadive",
    "Pondicherry",
    "Operation Vijay",
    "Operation Polo",
    "non-alignment",
    "civilian control",
    "77th Republic Day",
    "polity, economy, education and international relations",
]

TOPICS = [
    base.topic(
        28,
        "Integration of the Princely States & the Making of the Republic",
        "28_Integration-of-Princely-States.md",
        "28_Integration-of-Princely-States.md",
        "28_Integration-of-Princely-States-and-Making-of-the-Republic_"
        "Complete-Topic-Package.md",
        [
            "basic/27_Independence-and-Partition.md",
            "advanced/27_Independence-and-Partition.md",
            "basic/23_Left-Peasant-Workers-and-States-Peoples-Movements.md",
            "basic/29_Colonial-Legacy-and-Foundations-of-the-Republic.md",
            "27_Independence-and-Partition-1946-1947_"
            "Complete-Topic-Package.md",
        ],
        [
            "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2184055",
            "https://culture.gov.in/commemorations/"
            "150th-birth-anniversary-sardar-vallabhbhai-patel",
        ],
        "Two official Government of India pages were retrieved live on 31 "
        "August 2026 and are used only as a bounded commemorative bridge. The "
        "Ministry of Culture's commemorations page records that India "
        "launched a two-year celebration of Sardar Vallabhbhai Patel's 150th "
        "birth anniversary at the Statue of Unity on 31 October 2024, with a "
        "commemorative coin and postal stamp, the book *Vallabh*, a "
        "documentary on the unification of over 560 princely states, and "
        "lectures, exhibitions, youth programmes and a virtual museum "
        "organised by the Ministry. A PIB Backgrounder titled *Rashtriya Ekta "
        "Diwas: A Pillar of National Cohesion*, posted on 30 October 2025, "
        "records that Rashtriya Ekta Diwas is observed annually on 31 October "
        "to commemorate Patel's birth anniversary, that it was first "
        "celebrated in 2014, that Ek Bharat Shreshtha Bharat was announced on "
        "31 October 2015, and that 2025 marks the 150th birth anniversary. "
        "Two disciplined cautions travel with that bridge. First, the "
        "Backgrounder's commemorative formulation that Patel integrated the "
        "states by 15 August 1947 or shortly thereafter is a commemorative "
        "compression and not a chronology, because the Junagadh plebiscite "
        "belongs to February 1948 and the Hyderabad Police Action to "
        "September 1948; the package teaches the commemorative sentence "
        "beside the documented sequence and never substitutes one for the "
        "other. Second, the Backgrounder's figure that the states covered "
        "nearly 40 per cent of India's territory and population is carried "
        "strictly as that page's own attributed estimate alongside the "
        "repository owner's phrasing of roughly a third of the "
        "subcontinent's territory, and neither proportion is asserted as "
        "settled. No claim whatever is made here about any present-day "
        "constitutional controversy.",
        "The Basic and Advanced owner files were reconciled against the "
        "repository's OCR-searchable copy of Bipan Chandra, Mridula "
        "Mukherjee and Aditya Mukherjee, *India After Independence, "
        "1947-2000*, whose accession chapter is fully text-extractable in "
        "the local file. That text supplies Attlee's paramountcy statement of "
        "20 February 1947 and Jinnah's declaration of 18 June 1947 (book PDF "
        "pages 94-95), Patel's assumption of additional charge of the newly "
        "created States Department on 27 June 1947 with V.P. Menon as "
        "Secretary and the earlier accession of some states to the "
        "Constituent Assembly in April 1947 (book PDF page 95), the "
        "three-subject appeal and the fact that all states except Junagadh, "
        "Jammu and Kashmir and Hyderabad acceded by 15 August 1947 together "
        "with the Junagadh sequence and the February 1948 plebiscite (book "
        "PDF page 96), the Kashmir invasion, the appeal for assistance, the "
        "accession and the airlift (book PDF pages 96-97), the reference to "
        "the Security Council on 30 December 1947 (book PDF page 98), the "
        "Hyderabad standstill agreement of November 1947 and the Razakar "
        "mobilisation (book PDF pages 98-99), and the September 1948 army "
        "action, the Nizam's surrender and accession, the second stage of "
        "integration from December 1947 and the new unions of Madhya Bharat, "
        "Rajasthan, the Patiala and East Punjab States Union, Saurashtra and "
        "Travancore-Cochin (book PDF page 100). Three deliberate omissions "
        "are recorded. The local text carries privy-purse amounts and a "
        "specific purse for the Nizam, but the Basic owner's factual-risk "
        "caution forbids stating privy-purse amounts and this package obeys "
        "the owner rather than the book. The same text describes the "
        "Junagadh plebiscite result as overwhelming without a percentage, so "
        "no percentage is stated. The local text's numeral for the count of "
        "states is corrupted in extraction, which is itself the strongest "
        "practical reason for the owner's rule of writing more than 560 "
        "rather than 562 or 565.",
        "The 2021 Mains GS-I Q3 stem is verbatim and locally verified: the "
        "repository export of the official 2021 General Studies Paper I "
        "carries the sentence assessing the main administrative issues and "
        "socio-cultural problems in the integration process of Indian "
        "Princely States, with the instruction to answer in 150 words, and "
        "the audited local Mains routing ledger routes it to this owner at 10 "
        "marks. No Prelims question in the audited local Prelims routing "
        "ledgers for 2018-2023, 2024-2025 or 2026 is routed to this owner, so "
        "no Prelims stem, option set or answer letter is asserted anywhere in "
        "this package.",
        TOPIC_28_FACTS,
        TOPIC_28_TRAPS,
        TOPIC_28_MAINS,
        TOPIC_28_PYQ_SOLUTIONS,
        TOPIC_28_REQUIRED_TERMS,
    ),
    base.topic(
        29,
        "The Colonial Legacy & the Foundations of the Republic",
        "29_Colonial-Legacy-and-Foundations-of-the-Republic.md",
        "29_Colonial-Legacy-and-Foundations-of-the-Republic.md",
        "29_Colonial-Legacy-and-Foundations-of-the-Republic_"
        "Complete-Topic-Package.md",
        [
            "basic/28_Integration-of-Princely-States.md",
            "advanced/28_Integration-of-Princely-States.md",
            "basic/07_Economic-Impact-of-British-Rule.md",
            "basic/30_Linguistic-Reorganisation-and-Regionalism.md",
            "26_Post-War-Upsurge-INA-RIN-Mutiny-Cabinet-Mission-1945-1946_"
            "Complete-Topic-Package.md",
        ],
        [
            "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2218449",
        ],
        "One official Government of India page was retrieved live on 31 "
        "August 2026 and is used only as a bounded commemorative bridge. A "
        "Ministry of Defence release carried by the Press Information Bureau "
        "and posted on 25 January 2026 records that the 77th Republic Day was "
        "celebrated on 26 January 2026 from Kartavya Path, that the "
        "President of India led the celebrations, that the President of the "
        "European Council and the President of the European Commission were "
        "the Chief Guests, and that the parade opened on the theme Vividata "
        "Mein Ekta - Unity in Diversity alongside 150 years of the national "
        "song. Only two things are drawn from that page. The first is the "
        "ordinal itself, which is a teaching device rather than a "
        "decoration: the parade is counted as the seventy-seventh precisely "
        "because 26 January 1950 is counted as the first, which fixes the "
        "distinction between independence in 1947 and the republic in 1950 "
        "better than any assertion could. The second is the theme of unity in "
        "diversity, which is used only to introduce the founding consensus as "
        "a historical choice. A ceremonial parade is not a historical source "
        "and nothing about the events, guests or equipment of 2026 is "
        "converted into evidence about the years 1947 to 1951; no claim is "
        "made here about any present-day constitutional or political "
        "controversy.",
        "The Basic and Advanced owner files were reconciled against the "
        "repository's OCR-searchable copy of Bipan Chandra, Mridula "
        "Mukherjee and Aditya Mukherjee, *India After Independence, "
        "1947-2000*, whose opening chapters extract cleanly in the local "
        "file. That text supplies the attribution of the phrase development "
        "of underdevelopment to A. Gunder Frank and the four basic features "
        "of the colonial structure (book PDF page 18), the fall of about 14 "
        "per cent in per capita agricultural production between 1901 and "
        "1941 and the rise of landless agricultural labourers from about 13 "
        "per cent in 1871 to about 28 per cent in 1951 (book PDF page 21), "
        "the finding that nearly 84 per cent of Indians were illiterate in "
        "1951 with about 92 per cent illiteracy among women and a life "
        "expectancy of barely thirty-two years for an Indian born between "
        "1940 and 1951 (book PDF pages 26-27), the colonial state's "
        "combination of authoritarian power with the rule of law and a "
        "relatively independent judiciary and the franchise figures of about "
        "3 per cent after 1919 and about 15 per cent after 1935 (book PDF "
        "pages 27-28), the commitment to universal adult franchise and the "
        "explicit rejection of the rice-bowl theory (book PDF page 10), the "
        "handover of Pondicherry in 1954, the entry of Indian troops into Goa "
        "on the night of 17 December 1961, the arrival of nearly six million "
        "refugees and the estimate that nearly 500,000 people were killed "
        "(book PDF page 101), the assassination of Gandhi on 30 January 1948 "
        "by Nathuram Godse, the immediate ban on the Rashtriya Swayamsevak "
        "Sangh and the lifting of that ban in July 1949 on five stated "
        "conditions accepted from Patel as Home Minister (book PDF page 104), "
        "the payment of Rs 550 million to Pakistan in January 1948 following "
        "a fast by Gandhi (book PDF page 105), the Nehru-Liaqat Pact of 8 "
        "April 1950 and the resignations it provoked (book PDF page 106), and "
        "the legalisation of the Communist Party of India once it abandoned "
        "armed struggle including in Telengana (book PDF page 108). Every "
        "quantitative claim in this package is therefore carried as an "
        "attributed estimate of that source and never as an audited national "
        "statistic, and the local text's spellings Nehru-Liaqat and Telengana "
        "are recorded beside the owner's spellings so that a candidate is not "
        "surprised by either form.",
        "The 2025 Mains GS-I Q12 stem is verbatim and locally verified: the "
        "repository export of the official 2025 General Studies Paper I "
        "carries the sentence directing the candidate to trace India's "
        "consolidation process during the early phase of independence in "
        "terms of polity, economy, education and international relations, "
        "with the instruction to answer in 250 words, and the audited local "
        "Mains routing ledger routes it to this owner at 15 marks. The 2021 "
        "Mains GS-I Q3 stem on princely-state integration is also verbatim "
        "and locally verified, but the ledger routes it to the Topic 28 "
        "owner, so it is carried here strictly as an adjacent routed demand "
        "and is not solved as though it belonged to this file. No Prelims "
        "question in the audited local Prelims routing ledgers is routed to "
        "this owner, so no Prelims stem, option set or answer letter is "
        "asserted anywhere in this package.",
        TOPIC_29_FACTS,
        TOPIC_29_TRAPS,
        TOPIC_29_MAINS,
        TOPIC_29_PYQ_SOLUTIONS,
        TOPIC_29_REQUIRED_TERMS,
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
    "modern-indian-history-28": [
        authored_session(
            "Independence was not integration: the problem the lapse created",
            "The transfer of power solved the question of who ruled British "
            "India and left open the question of who ruled princely India, "
            "because British paramountcy over the states lapsed instead of "
            "passing to a successor, and everything else in this topic is a "
            "response to that single legal fact.",
            [
                "British paramountcy over the princely states lapsed when "
                "British rule ended on 15 August 1947 and was never "
                "transferred to India or Pakistan.",
                "Lapse meant that a very large share of the subcontinent's "
                "territory and population had, in strict law, no successor "
                "sovereign on the morning after independence.",
                "The Union's authority over princely India therefore had to "
                "be constructed by agreement, leverage and, in one case, "
                "force, and could not be claimed by legal succession.",
                "That is why a separate department, a separate instrument and "
                "a separate chronology exist for the states at all: they were "
                "not covered by the settlement that partitioned British "
                "India.",
            ],
            "Never write that paramountcy passed to India; the whole topic "
            "exists because it lapsed, and an answer that transfers it has "
            "deleted the problem it is meant to analyse.",
            "Open any integration answer with the lapse, because it converts "
            "a narrative of accession into an analysis of state-building "
            "under legal vacuum.",
            """15 AUG 1947 -> BRITISH RULE ENDS
   |-- BRITISH INDIA -> partitioned; successor dominions defined by statute
   `-- PRINCELY INDIA -> PARAMOUNTCY LAPSES -> no successor sovereign in law
CONSEQUENCE -> authority must be CONSTRUCTED (agreement + leverage + force)
RULE -> lapse, not transfer; that single word generates the entire topic.""",
            "Lapse of paramountcy means the extinction, at the end of British "
            "rule, of the suzerain relationship between the Crown and the "
            "princely states, without that relationship passing to India or "
            "Pakistan by succession.",
        ),
        authored_session(
            "How many states: the discipline behind more than 560",
            "The number of princely states is a trap disguised as a fact, "
            "because the familiar totals differ by what an enumerator counts "
            "as a state rather than by any disagreement about history, and "
            "the disciplined answer refuses to choose between them.",
            [
                "There were more than 560 princely states at independence, "
                "which is the formulation both repository owners require.",
                "The rival totals of 562 and 565 reflect different counting "
                "conventions for estates, jagirs and minor holdings, not "
                "rival historical claims.",
                "The repository's local OCR text of *India After "
                "Independence* is corrupted at exactly the point where it "
                "gives the total, which is a practical demonstration of why "
                "the safe formulation exists.",
                "The Ministry of Culture's commemorations page and the PIB "
                "Backgrounder both use the open formulation of over 560 "
                "states, so the safe phrasing is also the official one.",
            ],
            "Write more than 560 princely states and add that totals vary by "
            "classification; never assert 562 or 565 as the single correct "
            "figure and never treat the two as competing events.",
            "Use the counting caution as a one-line demonstration of source "
            "discipline early in a 15 or 20-mark answer.",
            """COUNTING THE STATES
   |-- SAFE FORM -> "more than 560" (both owners; official commemorative pages)
   |-- 562 / 565 -> different CLASSIFICATION rules (estates, jagirs, minor holdings)
   |-- LOCAL OCR -> numeral corrupted in extraction -> cannot arbitrate
VERDICT -> the disagreement is about counting conventions, not about history.""",
            "The more-than-560 formulation is a deliberate counting "
            "discipline that reports the scale of princely India while "
            "refusing to arbitrate between enumeration conventions that "
            "produce totals such as 562 and 565.",
        ),
        authored_session(
            "The States Department: a minister, a secretary and a machine",
            "Integration was institutional before it was heroic, and the "
            "correct answer names three things together - Patel's political "
            "authority, V.P. Menon's operational drafting and the States "
            "Department's machinery - because removing any one of them makes "
            "the speed of 1947 inexplicable.",
            [
                "Sardar Vallabhbhai Patel assumed additional charge of the "
                "newly created States Department on 27 June 1947, seven weeks "
                "before the transfer of power.",
                "V.P. Menon served as its Secretary and supplied the "
                "drafting, negotiation and administrative sequencing that "
                "turned a political appeal into standard instruments.",
                "Patel warned Menon at the time that the situation held "
                "dangerous potentialities and that hard-earned freedom might "
                "disappear through the states' door, which fixes the urgency "
                "of the exercise.",
                "The department's method combined appeal to patriotism, a "
                "narrow legal demand and an implied warning that terms after "
                "the transfer of power would be stiffer.",
            ],
            "Do not present integration as one man's achievement; the "
            "Advanced owner explicitly rejects that reading, and naming V.P. "
            "Menon and the States Department is part of the correct answer.",
            "Use the department as the institutional evidence unit whenever "
            "the directive is Assess rather than Describe.",
            """STATES DEPARTMENT (created 27 June 1947)
   |-- POLITICAL AUTHORITY -> Sardar Vallabhbhai Patel (Home and States Minister)
   |-- OPERATIONAL DRAFTING -> V.P. Menon, Secretary
   |-- METHOD -> appeal to patriotism + narrow legal demand + implied warning
   `-- OUTPUT -> standard Instruments of Accession, standstill arrangements
RULE -> name minister, secretary and department together, or the speed is unexplained.""",
            "The States Department was the Government of India office created "
            "on 27 June 1947 under Patel with V.P. Menon as Secretary to "
            "negotiate, draft and administer the accession and later merger "
            "of the princely states.",
        ),
        authored_session(
            "The three-subject formula and why its narrowness worked",
            "The Instrument of Accession succeeded because of what it did not "
            "ask for: by demanding only Defence, External Affairs and "
            "Communications it took everything that constitutes sovereignty "
            "in practice while appearing to leave a ruler's internal world "
            "intact.",
            [
                "The instrument asked acceding states to transfer three "
                "subjects only - Defence, External Affairs and "
                "Communications.",
                "These were precisely the subjects that no princely state, "
                "however large, could actually exercise for itself once "
                "British protection was withdrawn.",
                "Internal administration, revenue, courts and succession were "
                "left with the ruler at the moment of accession, which is why "
                "signature looked like a small concession.",
                "Because the demand was uniform and narrow, it could be "
                "standardised and executed at speed across hundreds of units "
                "in a matter of weeks.",
            ],
            "Never claim that every subject passed to the Union at the moment "
            "of signature; the instrument initially covered three subjects, "
            "and the later transfer of internal authority came through merger "
            "and constitutional incorporation rather than through the "
            "instrument itself.",
            "Use the narrowness as the mechanism paragraph in any answer that "
            "asks why integration succeeded so quickly.",
            """INSTRUMENT OF ACCESSION -> three subjects only
   |-- DEFENCE            -> no state could defend itself after British withdrawal
   |-- EXTERNAL AFFAIRS   -> no state could conduct foreign relations alone
   |-- COMMUNICATIONS     -> posts, telegraphs, railways cross every boundary
   `-- LEFT WITH RULER    -> internal administration, revenue, courts, succession
MECHANISM -> ask for the impossible-to-retain; take sovereignty without seeming to.""",
            "The Instrument of Accession was the standard legal instrument by "
            "which a princely state transferred Defence, External Affairs and "
            "Communications to the Dominion of India while initially "
            "retaining internal administration.",
        ),
        authored_session(
            "Attlee and Jinnah: the encouragement the princes received",
            "Princely ambition in 1947 was not merely vanity; it rested on "
            "two public statements that appeared to license independence, and "
            "an answer that names them explains why the Indian side treated "
            "speed as a security requirement.",
            [
                "The local OCR text records Clement Attlee's announcement of "
                "20 February 1947 that His Majesty's Government did not "
                "intend to hand over their powers and obligations under "
                "paramountcy to any government of British India.",
                "M.A. Jinnah publicly declared on 18 June 1947 that the "
                "states would be independent sovereign states on the "
                "termination of paramountcy and were free to remain "
                "independent if they so desired.",
                "Attlee later qualified the British position by expressing "
                "the hope that all the states would in due course find their "
                "appropriate place with one or the other dominion.",
                "Some states nonetheless showed realism early, joining the "
                "Constituent Assembly in April 1947, while Travancore, Bhopal "
                "and Hyderabad publicly announced a desire for independent "
                "status.",
            ],
            "Present these as encouragements to a claim rather than as legal "
            "authority for it; Indian nationalist opinion never accepted that "
            "independence was an option open to a princely state.",
            "Use the two statements to justify the compressed timetable of "
            "June to August 1947 in a causal paragraph.",
            """WHY THE PRINCES HOPED
20 FEB 1947 -> Attlee: paramountcy will not be handed to any government of British India
18 JUN 1947 -> Jinnah: states become independent sovereign states on termination
LATER -> Attlee hopes all states find a place with one or the other dominion
APR 1947 -> some states join the Constituent Assembly; Travancore, Bhopal, Hyderabad refuse
RESULT -> Indian side treats speed as a security requirement, not a preference.""",
            "The princely independence claim was the contention, encouraged "
            "by the statements of February and June 1947, that the lapse of "
            "paramountcy restored sovereignty to individual rulers rather "
            "than passing it to either dominion.",
        ),
        authored_session(
            "Two pressures on the princes: their own people and Partition",
            "Accession was never a private transaction between a department "
            "and a durbar, because rulers were negotiating with New Delhi "
            "while facing organised political movements inside their own "
            "states and a partitioned subcontinent outside them.",
            [
                "The people of the states had participated in the making of "
                "the nation since the late nineteenth century and were "
                "organised under the States' Peoples' Conference, demanding a "
                "democratic order and integration with the rest of the "
                "country.",
                "The national movement had long held that political power "
                "belonged to the people of a state and not to its ruler, "
                "which denied a prince the standing to bargain about "
                "sovereignty.",
                "Patel's implied warning that he might be unable to restrain "
                "impatient peoples' movements converted internal agitation "
                "into a negotiating instrument.",
                "Partition violence made isolation dangerous for small and "
                "landlocked states, so the alternative to accession was not "
                "independence but exposure.",
            ],
            "Do not describe the princes as passive; they calculated, and the "
            "calculation included the movement in their own capitals as well "
            "as the department in Delhi.",
            "Use the two-pressures thesis to add analytical depth to an "
            "otherwise chronological accession answer.",
            """THE PRINCE'S POSITION IN 1947 -> squeezed from two sides
   ABOVE -> States Department: narrow demand now, stiffer terms later
   BELOW -> States' Peoples' Conference: democratic order, integration, agitation
   OUTSIDE -> Partition violence -> isolation is exposure, not independence
BARGAIN -> accede on three subjects and retain dignities, or face both pressures alone.""",
            "The two-pressures reading treats accession as the outcome of "
            "simultaneous bargaining with the States Department above and "
            "organised states' peoples' movements below, rather than as a "
            "purely diplomatic transaction.",
        ),
        authored_session(
            "Accession, merger, democratisation, incorporation: four stages",
            "The commonest structural error in this topic is to treat "
            "accession as the whole of integration, when the sources present "
            "at least four distinct stages, each with its own instrument, "
            "date and difficulty.",
            [
                "Stage one was accession on three subjects, executed at speed "
                "and largely complete by 15 August 1947.",
                "Stage two was merger and consolidation, which began in "
                "December 1947 and grouped unviable units into unions or "
                "attached them to neighbouring provinces.",
                "Stage three was democratisation inside the former states, "
                "which extended elections, courts, services and revenue "
                "administration and proceeded unevenly and often slowly.",
                "Stage four was constitutional incorporation, completed when "
                "the Constitution came into force and a single citizenship "
                "dissolved the legal category of a prince's subject.",
            ],
            "Never collapse the four stages into one act of accession; the "
            "Advanced owner sets out the sequence explicitly and an answer "
            "that ignores it cannot explain what happened after 1947.",
            "Use the four-stage spine as the skeleton of any process-analysis "
            "question about how integration was achieved.",
            """FOUR STAGES, FOUR INSTRUMENTS
1 ACCESSION      -> Instrument of Accession (three subjects)      -> by 15 Aug 1947
2 MERGER         -> merger agreements, unions, attachments        -> from Dec 1947
3 DEMOCRATISATION-> elections, courts, services inside old states -> uneven, slower
4 INCORPORATION  -> Constitution; single citizenship              -> 26 Jan 1950
RULE -> accession is the first stage, never the finished process.""",
            "Integration in this topic denotes the four-stage passage from "
            "accession on three subjects, through merger and democratisation, "
            "to constitutional incorporation, and not the signature of an "
            "instrument alone.",
        ),
        authored_session(
            "Junagadh: the ruler-subject mismatch and February 1948",
            "Junagadh is the case in which the accession formula failed "
            "because the ruler's choice contradicted both his population and "
            "his geography, and it was settled by counting people rather than "
            "by using force.",
            [
                "Junagadh was a small state on the Saurashtra coast, "
                "surrounded by Indian territory and without geographical "
                "contiguity with Pakistan, yet its Nawab announced accession "
                "to Pakistan.",
                "The state's overwhelmingly Hindu population organised a "
                "popular movement, forced the Nawab to flee and established a "
                "provisional government.",
                "The Dewan of Junagadh, Shah Nawaz Bhutto, then invited the "
                "Government of India to intervene, and Indian troops "
                "thereafter entered the state.",
                "A plebiscite held in February 1948 went in favour of joining "
                "India, and the local source calls the result overwhelming "
                "without stating any percentage.",
            ],
            "State the February 1948 plebiscite and state no percentage; the "
            "repository holds no audited polling figure and inventing one is "
            "the exact failure this owner is designed to prevent.",
            "Use Junagadh as the case where the principle that the people, "
            "not the ruler, decide accession was applied and vindicated.",
            """JUNAGADH -> the formula fails on RULER vs PEOPLE vs GEOGRAPHY
RULER   -> Nawab accedes to Pakistan
PEOPLE  -> overwhelmingly Hindu; popular movement; Nawab flees; provisional government
GEOGRAPHY -> Saurashtra coast, surrounded by Indian territory, non-contiguous with Pakistan
DEWAN   -> Shah Nawaz Bhutto invites Government of India to intervene
INSTRUMENT -> PLEBISCITE, FEBRUARY 1948 -> in favour of India (no percentage asserted)""",
            "The Junagadh case denotes the accession crisis produced when a "
            "ruler acceded to Pakistan against the wishes of an "
            "overwhelmingly Hindu population in a state not contiguous with "
            "Pakistan, resolved by the plebiscite of February 1948.",
        ),
        authored_session(
            "Hyderabad: standstill, Razakars and September 1948",
            "Hyderabad is the case in which negotiation was tried longest and "
            "failed, and the police action of September 1948 must therefore "
            "be presented as the end of a documented process rather than as "
            "an opening move.",
            [
                "Hyderabad was the largest state and was completely "
                "surrounded by Indian territory, and its Nizam claimed an "
                "independent status rather than acceding.",
                "The Government of India signed a standstill agreement with "
                "the Nizam in November 1947, hoping that representative "
                "government inside the state would make merger easier.",
                "Inside the state, the communal organisation Ittihad ul "
                "Muslimin and its paramilitary Razakars grew rapidly, the "
                "Hyderabad State Congress launched a satyagraha for "
                "democratisation, and a Communist-led peasant struggle "
                "developed in the Telangana region.",
                "The Indian army moved into Hyderabad in September 1948 in "
                "the operation commonly called Operation Polo or the Police "
                "Action, after which the Nizam surrendered and acceded to the "
                "Indian Union.",
            ],
            "Operation Polo is Hyderabad in September 1948; do not attach it "
            "to Kashmir or to Goa, and do not state casualty or troop figures "
            "for the operation.",
            "Use Hyderabad as the case that shows coercion was the residual "
            "instrument and not the standard one.",
            """HYDERABAD -> negotiation first, force last
NOV 1947 -> STANDSTILL AGREEMENT with the Nizam; hope of representative government
INSIDE   -> Ittihad ul Muslimin + Razakars | State Congress satyagraha | Telangana peasants
STALL    -> Nizam prolongs talks, expands armed forces, seeks sovereignty
SEP 1948 -> OPERATION POLO / POLICE ACTION -> Nizam surrenders -> accedes to the Union
LIMIT    -> no casualty figure and no troop figure is asserted anywhere here.""",
            "Operation Polo, also called the Police Action, is the Indian "
            "army operation of September 1948 that ended the Nizam of "
            "Hyderabad's claim to independent status and was followed by the "
            "state's accession.",
        ),
        authored_session(
            "Kashmir: October 1947, accession, and disciplined restraint",
            "Kashmir is the case in which the accession formula was overtaken "
            "by an invasion, and it is also the case in which examination "
            "discipline matters most, because the historical sequence is "
            "clear while much of the later argument is contested.",
            [
                "Maharaja Hari Singh had acceded to neither dominion, while "
                "the National Conference under Sheikh Abdullah, the state's "
                "principal popular force, favoured accession to India.",
                "Tribal invaders entered Kashmir in October 1947 and pushed "
                "towards Srinagar, and the Maharaja appealed to India for "
                "military assistance.",
                "Indian troops were flown to Srinagar only after the "
                "Instrument of Accession had been signed, and Sheikh Abdullah "
                "was installed as head of the state's administration.",
                "The Government of India referred the Kashmir problem to the "
                "Security Council of the United Nations on 30 December 1947, "
                "asking for vacation of aggression, and fighting continued "
                "thereafter.",
            ],
            "Record the invasion, the accession, the airlift and the "
            "reference to the United Nations, and stop there; later "
            "constitutional and political controversies are outside the "
            "historical scope of this owner.",
            "Use Kashmir as the case that shows why security, and not only "
            "law or demography, belongs in the comparison grid.",
            """KASHMIR -> strict order of events (do not reorder)
1 RULER UNDECIDED -> Hari Singh accedes to neither dominion
2 POPULAR FORCE   -> National Conference under Sheikh Abdullah favours India
3 OCTOBER 1947    -> tribal invasion advances towards Srinagar
4 APPEAL          -> Maharaja asks India for military assistance
5 ACCESSION       -> Instrument signed; Abdullah heads the administration
6 AIRLIFT         -> troops flown to Srinagar AFTER accession
7 30 DEC 1947     -> reference to the UN Security Council; fighting continues
STOP LINE -> restraint beyond this point; contested later claims are not history here.""",
            "The Kashmir accession denotes the signature of the Instrument of "
            "Accession by Maharaja Hari Singh in October 1947 following the "
            "tribal invasion and preceding the despatch of Indian troops to "
            "Srinagar.",
        ),
        authored_session(
            "The four-variable comparison engine for the three hard cases",
            "The three problem states are examined together so often that the "
            "only way to score is to compare them on fixed variables, because "
            "an answer that narrates them one after another has produced "
            "chronology where the examiner asked for analysis.",
            [
                "Variable one is the ruler's choice: Junagadh's Nawab acceded "
                "to Pakistan, Hyderabad's Nizam sought independence, and "
                "Kashmir's Maharaja hesitated between the two dominions.",
                "Variable two is the population: Junagadh was overwhelmingly "
                "Hindu under a Muslim ruler, Hyderabad was largely Hindu "
                "under the Nizam, and Kashmir was Muslim-majority under a "
                "Hindu Maharaja.",
                "Variable three is geography: Junagadh was non-contiguous "
                "with Pakistan, Hyderabad was landlocked inside India, and "
                "Kashmir bordered both dominions.",
                "Variable four is security: Junagadh faced an internal "
                "movement, Hyderabad faced Razakar violence and stalemate, "
                "and Kashmir faced an external invasion, which is why three "
                "different instruments were used.",
            ],
            "The three problem states did not pose the same problem; use the "
            "four variables explicitly, because the differences, not the "
            "similarities, are what the comparison is testing.",
            "Use the grid as the body of any Compare directive and let the "
            "instruments follow from the variables.",
            """COMPARISON GRID -> four variables, three states, three instruments
VARIABLE      | JUNAGADH            | HYDERABAD             | KASHMIR
RULER         | acceded to Pakistan | sought independence   | hesitated
POPULATION    | overwhelmingly Hindu| largely Hindu         | Muslim-majority
GEOGRAPHY     | non-contiguous      | landlocked in India   | borders both
SECURITY      | internal movement   | Razakars, stalemate   | external invasion
INSTRUMENT    | plebiscite Feb 1948 | police action Sep 1948| accession + troops + UN""",
            "The four-variable comparison engine is the analytical device "
            "that separates the three hard accession cases by the ruler's "
            "choice, the population's composition, the state's geography and "
            "the security situation.",
        ),
        authored_session(
            "Unions and mergers: making unviable states administrable",
            "The second stage of integration is the one most answers omit, "
            "and it is where the map of India was actually redrawn, because "
            "hundreds of acceding units had to be turned into provinces "
            "capable of carrying a civil service, a judiciary and an "
            "election.",
            [
                "The second stage began in December 1947 and was carried "
                "through with speed comparable to the first.",
                "Smaller states were merged with neighbouring provinces or "
                "grouped together into centrally administered areas.",
                "A large number were consolidated into new unions - Madhya "
                "Bharat, Rajasthan, the Patiala and East Punjab States Union, "
                "Saurashtra and Travancore-Cochin.",
                "Mysore, Hyderabad and Jammu and Kashmir retained their "
                "original form as separate states of the Union, so the "
                "settlement was deliberately asymmetrical rather than "
                "uniform.",
            ],
            "Do not describe the process as uniform; large states negotiated "
            "individually while small ones were grouped, and this asymmetry "
            "is the origin of much later reorganisation.",
            "Use the unions as the concrete evidence that accession alone did "
            "not produce administrable government.",
            """SECOND STAGE (from December 1947) -> making units governable
SMALL STATES -> merged into neighbouring provinces or centrally administered areas
NEW UNIONS   -> Madhya Bharat | Rajasthan | Patiala and East Punjab States Union
             -> Saurashtra | Travancore-Cochin
RETAINED FORM-> Mysore | Hyderabad | Jammu and Kashmir as separate states of the Union
CONSEQUENCE  -> an asymmetrical map that later reorganisation would have to revisit.""",
            "Merger and union formation denote the second stage of "
            "integration, in which acceded states were amalgamated into "
            "viable administrative units such as Madhya Bharat, Rajasthan, "
            "the Patiala and East Punjab States Union, Saurashtra and "
            "Travancore-Cochin.",
        ),
        authored_session(
            "Privy purses and privileges: the price carried forward",
            "Integration was purchased, not merely negotiated, and the "
            "honest answer records the price: rulers who surrendered power "
            "retained income and dignities, and those settlements survived "
            "the initial integration entirely intact.",
            [
                "Rulers of the major states received privy purses in return "
                "for surrendering power and authority, and retained titles, "
                "succession to the gaddi and ceremonial privileges.",
                "These concessions were criticised at the time and "
                "afterwards, and the Basic owner treats them as a real cost "
                "of the settlement rather than as a detail.",
                "Privy purses were not abolished during the initial "
                "integration; the Advanced owner dates their abolition to "
                "1971, decades after accession.",
                "This package states no amount for any privy purse, because "
                "the Basic owner's factual-risk caution forbids it even "
                "though the local book text carries figures.",
            ],
            "Never date the abolition of the privy purses to the accession "
            "itself, and never quote a purse amount; the safe answer names "
            "the instrument, notes the criticism and dates the abolition to "
            "1971 on the owner's authority.",
            "Use the privy purses as the counterpoint that prevents a purely "
            "heroic reading of integration.",
            """THE PRICE OF INTEGRATION
GIVEN TO RULERS -> privy purses | titles | succession to the gaddi | ceremonial privileges
TAKEN FROM RULERS -> all power and authority over the state
DURATION -> retained through the initial integration; abolition dated by the owner to 1971
DISCIPLINE -> criticism recorded; NO amount for any purse is asserted in this package
USE -> the counterpoint that stops a heroic narrative becoming an uncritical one.""",
            "Privy purses were the tax-free payments guaranteed to the rulers "
            "of major states in return for the surrender of power, retained "
            "alongside titles and ceremonial privileges and not abolished "
            "during the initial integration.",
        ),
        authored_session(
            "From acceding state to citizen: 1949 and 1950",
            "Integration was completed by constitutional means rather than "
            "administrative ones, because it was the Constitution, and not "
            "any instrument of accession, that abolished the legal category "
            "of a prince's subject.",
            [
                "The Constituent Assembly was presided over by Dr Rajendra "
                "Prasad, with B.R. Ambedkar chairing the Drafting Committee.",
                "The Constitution was adopted on 26 November 1949 and came "
                "into force on 26 January 1950.",
                "A single citizenship, a single judicial hierarchy and "
                "uniform fundamental rights dissolved the distinction between "
                "the subjects of princes and the citizens of the Union.",
                "India became independent on 15 August 1947 and a republic on "
                "26 January 1950, so the two dates answer two different "
                "questions and can never be interchanged.",
            ],
            "India did not become a republic in 1947; independence and the "
            "republic are separated by more than two years, and the "
            "distinction is examined directly at Prelims level.",
            "Use the constitutional stage as the closing move of any answer "
            "on how accession became nationhood.",
            """COMPLETION BY CONSTITUTION
CONSTITUENT ASSEMBLY -> President: Dr Rajendra Prasad | Drafting Committee: B.R. Ambedkar
26 NOV 1949 -> Constitution ADOPTED
26 JAN 1950 -> Constitution COMMENCES -> India becomes a republic
EFFECT -> single citizenship + single judicial hierarchy + uniform fundamental rights
         -> the legal category "subject of a prince" ceases to exist
CONTRAST -> INDEPENDENCE 15 Aug 1947 | REPUBLIC 26 Jan 1950 (never interchange).""",
            "Constitutional incorporation denotes the completion of "
            "integration through the adoption of the Constitution on 26 "
            "November 1949 and its commencement on 26 January 1950, which "
            "replaced princely subjecthood with a single Union citizenship.",
        ),
        authored_session(
            "Commemoration and chronology: reading Ekta Diwas as a historian",
            "The live commemorative frame around this topic is genuinely "
            "useful and genuinely dangerous, and the mature candidate uses "
            "the official record for context while holding it to the "
            "documented chronology.",
            [
                "The Ministry of Culture's commemorations page records a "
                "two-year celebration of Sardar Patel's 150th birth "
                "anniversary launched at the Statue of Unity on 31 October "
                "2024, with a commemorative coin and stamp, a book, a "
                "documentary on the unification of over 560 princely states, "
                "and lectures, exhibitions and a virtual museum.",
                "A PIB Backgrounder posted on 30 October 2025 records that "
                "Rashtriya Ekta Diwas is observed annually on 31 October, "
                "that it was first celebrated in 2014, and that Ek Bharat "
                "Shreshtha Bharat was announced on 31 October 2015.",
                "The same Backgrounder states that Patel integrated the "
                "states by 15 August 1947 or shortly thereafter, which is a "
                "commemorative compression, because the Junagadh plebiscite "
                "belongs to February 1948 and the Hyderabad Police Action to "
                "September 1948.",
                "The Backgrounder's figure that the states covered nearly 40 "
                "per cent of India's territory and population is carried "
                "strictly as that page's attributed estimate beside the "
                "repository owner's phrasing of roughly a third of the "
                "subcontinent's territory.",
            ],
            "Use official commemorative material for framing only; never let "
            "a commemorative sentence overwrite a documented date, and never "
            "convert a commemoration into a claim about present-day "
            "constitutional controversy.",
            "Use this session as the model for handling any anniversary hook "
            "in a history answer: cite the source, use the frame, keep the "
            "chronology.",
            """COMMEMORATION vs CHRONOLOGY -> use both, confuse neither
OFFICIAL RECORD -> Ministry of Culture: two-year 150th-anniversary programme from 31 Oct 2024
                -> PIB Backgrounder, 30 Oct 2025: Ekta Diwas annually on 31 October, first 2014
COMMEMORATIVE COMPRESSION -> "integrated by 15 August 1947 or shortly thereafter"
DOCUMENTED SEQUENCE       -> Junagadh plebiscite Feb 1948 | Hyderabad Police Action Sep 1948
CONTESTED PROPORTION      -> PIB "nearly 40 per cent" vs owner "roughly a third" (both attributed)
RULE -> the commemoration frames the question; the chronology answers it.""",
            "Rashtriya Ekta Diwas is the annual observance on 31 October, "
            "first celebrated in 2014, commemorating Sardar Patel's birth "
            "anniversary and his role in the political integration of the "
            "princely states.",
        ),
    ],
}

SESSION_PLANS["modern-indian-history-29"] = [
    authored_session(
        "Two inheritances: colonial liabilities against movement assets",
        "The organising idea of this topic is a balance sheet with two "
        "columns that must never be mixed: what colonial rule left behind, "
        "which was overwhelmingly a liability, and what the national movement "
        "left behind, which was overwhelmingly an asset.",
        [
            "The colonial column carries a dependent and stagnant economy, "
            "mass illiteracy, low life expectancy, a famine-prone "
            "agriculture and an administrative apparatus designed for "
            "extraction and order.",
            "The movement column carries a tested all-India leadership, a "
            "party organised in every province, and settled commitments to "
            "democracy, civil liberties, secularism and social reform.",
            "Keeping the columns apart is what allows the central question to "
            "be asked at all: how did a state this poor sustain a democracy "
            "this ambitious?",
            "Mixing the columns produces the two commonest bad answers - a "
            "colonial-modernisation story that credits the empire with "
            "Indian democracy, and a nationalist story that forgets the "
            "material starting point.",
        ],
        "Never blur colonial economic and administrative liabilities into "
        "national-movement political assets; the whole analytical value of "
        "this topic lies in keeping the two inheritances distinct.",
        "Open any colonial-legacy or consolidation answer with the two "
        "columns, then spend the body proving each side with named evidence.",
        """THE BALANCE SHEET OF 1947 -> two columns, never merged
COLONIAL LIABILITY (economic + administrative) | MOVEMENT ASSET (political)
  dependent, stagnant economy                  |  tested all-India leadership
  mass illiteracy; low life expectancy         |  party organised in every province
  famine-prone, rentier agriculture            |  democracy, civil liberties, secularism
  apparatus built for extraction and order     |  three decades of practised organisation
CENTRAL QUESTION -> how did column two carry column one without collapsing?""",
        "The two-inheritance frame is the analytical separation of the "
        "colonial economic and administrative legacy from the political and "
        "institutional legacy of the national movement, treated as distinct "
        "inputs to the republic of 1950.",
    ),
    authored_session(
        "The development of underdevelopment and its exact attribution",
        "The phrase that names the colonial economic outcome is precise, "
        "attributable and frequently misquoted, and using it correctly signals "
        "to an examiner that the candidate has read rather than absorbed the "
        "argument.",
        [
            "Chandra describes the colonial economic outcome as the "
            "development of underdevelopment and expressly attributes the "
            "phrase to A. Gunder Frank.",
            "The argument is not that nothing changed: railways, "
            "administration, education, finance and communications all "
            "developed, and several of those changes were positive in "
            "themselves.",
            "The argument is that these changes operated inside a colonial "
            "framework, so they crystallised a structure that generated "
            "poverty, dependence and subordination to Britain.",
            "India's economy was integrated with the world capitalist system "
            "in a subordinate position, exporting foodstuffs and raw "
            "materials and importing manufactures under a forced division of "
            "labour.",
        ],
        "Do not present the phrase as Chandra's coinage; attribute it to A. "
        "Gunder Frank as the source does, and do not convert it into the "
        "claim that colonial rule produced no change at all.",
        "Use the phrase once, attributed, as the thesis sentence of the "
        "economic-legacy paragraph, then prove it with the agrarian and "
        "human-development evidence.",
        """DEVELOPMENT OF UNDERDEVELOPMENT -> attribute to A. Gunder Frank (via Chandra)
CHANGE HAPPENED -> railways | administration | education | finance | communications
BUT THE FRAME    -> colonial structure -> subordinate integration with world capitalism
FORCED DIVISION  -> India exports foodstuffs and raw materials; imports manufactures
OUTCOME          -> poverty + dependence + subordination, not development
MISQUOTE TRAP    -> the claim is structural, not a denial that anything changed.""",
        "The development of underdevelopment is A. Gunder Frank's phrase, "
        "used by Chandra, for a process in which real economic change occurs "
        "inside a colonial framework and produces dependence and poverty "
        "rather than self-sustaining growth.",
    ),
    authored_session(
        "The agrarian legacy: landlessness, stagnation and rent",
        "Agriculture is where the colonial economic structure is most "
        "measurable, and the two attributed movements that matter are a "
        "falling per capita output and a rising landless labour force.",
        [
            "The source records a decline of about 14 per cent in per capita "
            "agricultural production between 1901 and 1941, with an even "
            "larger fall in per capita foodgrains.",
            "The same source records that landless agricultural labourers "
            "grew from about 13 per cent of the agricultural population in "
            "1871 to about 28 per cent by 1951.",
            "The agrarian structure was dominated by landlords, moneylenders, "
            "merchants and the colonial state, with subinfeudation, tenancy "
            "and sharecropping spreading in both zamindari and ryotwari "
            "areas.",
            "The colonial state's interest in agriculture was confined "
            "largely to collecting land revenue, while landlords and "
            "moneylenders found rack-renting and usury safer than productive "
            "investment.",
        ],
        "Attribute both movements to the source and do not extend them to "
        "other years or convert them into national averages for periods the "
        "source does not cover.",
        "Use the two attributed trends as the evidence spine whenever a "
        "question asks what the republic inherited in agriculture.",
        """AGRARIAN LEGACY -> two attributed movements plus one structure
OUTPUT   -> per capita agricultural production falls about 14% between 1901 and 1941
           (foodgrains fall further)
LABOUR   -> landless agricultural labourers rise from about 13% (1871) to about 28% (1951)
STRUCTURE-> landlords + moneylenders + merchants + colonial state
           subinfeudation, tenancy, sharecropping in zamindari AND ryotwari areas
INCENTIVE-> rack-renting and usury are safer than investment -> stagnation is rational
DISCIPLINE -> both figures are the source's estimates; attribute, never extrapolate.""",
        "The agrarian legacy denotes the combination of falling per capita "
        "agricultural output, rising landlessness and a rentier structure of "
        "landlords, moneylenders and revenue demand that the republic "
        "inherited in 1947.",
    ),
    authored_session(
        "Bodies and minds in 1951: literacy and life expectancy",
        "The human-development figures for 1951 are the most quotable "
        "evidence in this topic and the most dangerous, because they are a "
        "single author's attributed estimates and are routinely repeated as "
        "though they were audited national statistics.",
        [
            "The source records that in 1951 nearly 84 per cent of Indians "
            "were illiterate, with illiteracy at about 92 per cent among "
            "women, and that only about eight out of a hundred women were "
            "literate.",
            "The same source records that an Indian born between 1940 and "
            "1951 could expect to live barely thirty-two years.",
            "It further records an annual death rate of about 25 per thousand "
            "during 1941 to 1950 and infant mortality between 175 and 190 per "
            "thousand live births, with malaria alone affecting a quarter of "
            "the population.",
            "Colonial education neglected mass, scientific and technical "
            "instruction and almost entirely neglected the education of "
            "girls, which is why the literacy figures are a statement about "
            "policy and not only about poverty.",
        ],
        "Attribute every one of these figures to the source, keep them "
        "attached to the year the source gives, and never round them into a "
        "new and cleaner claim.",
        "Use these figures as the education-domain evidence in the 2025 "
        "four-domain consolidation answer.",
        """1951 -> THE HUMAN STARTING POINT (all figures attributed to the source)
LITERACY        -> nearly 84% illiterate | about 92% illiteracy among women
WOMEN           -> about 8 literate women in every 100
LIFE EXPECTANCY -> barely 32 years for an Indian born between 1940 and 1951
MORTALITY       -> death rate about 25 per 1,000 (1941-50); infant mortality 175-190 per 1,000
CAUSE           -> colonial neglect of mass, technical and female education, not poverty alone
RULE            -> attribute, keep the year, never round into a fresh figure.""",
        "The 1951 human-development baseline denotes the source-attributed "
        "estimates of literacy, female literacy, life expectancy and "
        "mortality that describe the population the republic began with.",
    ),
    authored_session(
        "The colonial state the republic actually inherited",
        "The republic did not build a state from nothing and did not "
        "dismantle the one it received; it inherited an apparatus designed "
        "for order and extraction and attempted to convert it into an "
        "instrument of development, and that conversion is the real content "
        "of the phrase colonial legacy.",
        [
            "The colonial state was basically authoritarian and autocratic "
            "yet carried liberal elements such as the rule of law and a "
            "relatively independent judiciary that partially checked "
            "arbitrary administration.",
            "Its laws were often repressive, were not framed by Indians "
            "through a democratic process, and left great arbitrary power "
            "with civil servants and the police.",
            "There was no separation of administrative and judicial "
            "functions, since the same officer administered a district as "
            "collector and dispensed justice as magistrate.",
            "Civil liberties of press, speech and association were extended "
            "in normal times and curtailed drastically during mass struggles, "
            "and were increasingly tampered with even in normal times after "
            "1897.",
        ],
        "Do not treat the inherited administration as neutral machinery; it "
        "carried both the rule-of-law fragment that the republic kept and the "
        "arbitrary powers that the republic had to justify keeping.",
        "Use the continuity-with-conversion thesis whenever a question asks "
        "what colonial legacy actually means in institutional terms.",
        """THE INHERITED APPARATUS -> kept, not dismantled
AUTHORITARIAN CORE -> repressive laws | wide arbitrary power with officials and police
                   -> no separation of administrative and judicial functions in the district
LIBERAL FRAGMENTS  -> rule of law | relatively independent judiciary | limited press freedom
PATTERN            -> liberties extended in calm, curtailed in mass struggle
REPUBLIC'S TASK    -> convert an apparatus of ORDER and EXTRACTION into one of DEVELOPMENT
THESIS             -> continuity with conversion, not rupture.""",
        "The inherited colonial state denotes the administrative, police, "
        "judicial and legal apparatus transferred intact in 1947, "
        "authoritarian in design yet carrying rule-of-law elements that the "
        "republic retained and repurposed.",
    ),
    authored_session(
        "About 3 per cent and about 15 per cent: the franchise refused",
        "The single most powerful fact available for a consolidation answer "
        "is the franchise contrast, because it measures exactly how far the "
        "republic broke with the state it inherited and cannot be explained "
        "by material conditions at all.",
        [
            "The source records that only about 3 per cent of Indians could "
            "vote after 1919 and about 15 per cent after 1935.",
            "Elections and legislatures were introduced under Indian "
            "pressure, but the legislatures did not enjoy much power until "
            "1935 and supreme power remained with the British even then.",
            "The colonial purpose of these reforms was to co-opt and weaken "
            "the national movement while retaining the reins of state power.",
            "The unintended effect was that Indians acquired practical "
            "experience of contesting elections and working elected organs, "
            "experience that proved useful after 1947.",
        ],
        "Universal adult franchise did not exist under colonial rule; state "
        "the two attributed percentages and the year each belongs to, and do "
        "not describe colonial reforms as democratisation.",
        "Use the franchise contrast as the opening evidence of the polity "
        "domain in the 2025 consolidation answer.",
        """FRANCHISE UNDER COLONIAL RULE -> narrow by design
AFTER 1919 -> about 3 per cent of Indians could vote
AFTER 1935 -> about 15 per cent of Indians could vote
POWER      -> legislatures weak before 1935; supreme power retained by the British
PURPOSE    -> co-opt and weaken the national movement while keeping the reins
SIDE EFFECT-> Indians gain practical experience of elections and elected organs
CONTRAST   -> the republic replaces this outright, and does not widen it by degrees.""",
        "The colonial franchise denotes the narrow statutory electorate of "
        "about 3 per cent of Indians after 1919 and about 15 per cent after "
        "1935 under legislatures that held limited power.",
    ),
    authored_session(
        "Universal adult franchise as the boldest decision of the period",
        "Adopting universal adult franchise in a society that the same "
        "sources describe as about 84 per cent illiterate was a deliberate "
        "wager rather than an obvious step, and presenting it as a wager is "
        "what converts a fact into an argument.",
        [
            "India was committed from the beginning to a democratic and civil "
            "libertarian political order with representative government based "
            "on free and fair elections on universal adult franchise.",
            "The leadership completely rejected the rice-bowl theory that the "
            "poor in an underdeveloped country cared more for a bowl of rice "
            "than for democracy.",
            "Democracy was also chosen instrumentally, as necessary for "
            "national integration in a diverse society and for bringing about "
            "social change.",
            "The state was to encroach as little as possible on rival civil "
            "sources of power such as universities, the press, trade unions, "
            "peasant organisations and professional associations.",
        ],
        "Do not call the adoption of universal franchise uncontroversial or "
        "inevitable; the sources present it as a bold and argued choice "
        "against a widely held contrary theory.",
        "Use the wager framing as the analytical high point of any answer on "
        "the foundations of the republic.",
        """THE WAGER OF UNIVERSAL ADULT FRANCHISE
STARTING CONDITION -> a population described by the source as about 84% illiterate
CONTRARY THEORY    -> the "rice-bowl theory": the poor want rice, not votes
DECISION           -> universal adult franchise at once, not a staged extension
REASONS GIVEN      -> democracy as integration | democracy as social change
                   -> minimal state encroachment on universities, press, unions, associations
FRAMING            -> a deliberate wager, not an obvious or uncontested step.""",
        "Universal adult franchise denotes the republic's immediate grant of "
        "the vote to all adult citizens, replacing rather than extending the "
        "narrow colonial electorate.",
    ),
    authored_session(
        "The national movement as an institutional, not sentimental, asset",
        "The best explanation for India's democratic survival is "
        "institutional residue rather than individual virtue, because the "
        "movement had already built the leadership, the organisation and the "
        "habits that a new state could not have manufactured for itself.",
        [
            "The prominent leaders of independent India - Nehru, Patel, "
            "Maulana Azad and Rajendra Prasad - were not associated with any "
            "one region, language, religion or caste, and the same was true "
            "of leading opponents.",
            "Congress leaders including Patel, Rajendra Prasad and "
            "Rajagopalachari were committed to democracy, civil liberties, "
            "secularism and independent economic development, differing from "
            "Nehru mainly on socialism and class analysis.",
            "The Congress leadership widened the base of the government by "
            "including distinguished non-Congressmen, and the first Nehru "
            "cabinet of fourteen included five, with B.R. Ambedkar chairing "
            "the Drafting Committee.",
            "The all-India administrative services and a national army "
            "recruited on individual merit across regions became further "
            "instruments of unity under civilian political authority.",
        ],
        "Do not reduce this to a list of great men; the asset was "
        "organisational and habitual, and the same Congress dominance that "
        "stabilised the transition later became a problem in its own right.",
        "Use this as the comparative paragraph explaining why India retained "
        "civilian and democratic government when many decolonised states did "
        "not.",
        """THE MOVEMENT'S INSTITUTIONAL RESIDUE
LEADERSHIP -> Nehru | Patel | Azad | Rajendra Prasad -> no single region, language or caste
BREADTH    -> first Nehru cabinet of fourteen includes five non-Congressmen
           -> B.R. Ambedkar chairs the Drafting Committee
ORGANISATION -> a party with structure in every province; three decades of practice
SERVICES   -> all-India services and a national army recruited on merit, under civilian control
COST LATER -> the same dominance becomes the "Congress system" whose decay is a later topic.""",
        "The movement's institutional asset denotes the leadership, "
        "organisation, accommodative practice and legitimacy that the "
        "national movement transferred to the republic, distinct from any "
        "material inheritance.",
    ),
    authored_session(
        "Simultaneity: why the initial years are one crisis, not four",
        "The achievement of 1947 to 1951 was not solving any single problem "
        "but surviving all of them at once, and an answer that sequences the "
        "crises has quietly removed the difficulty it was asked to explain.",
        [
            "India became independent on 15 August 1947 and immediately faced "
            "refugee movement, communal killing, the division of the army and "
            "the treasury, princely integration and fighting in Kashmir.",
            "The four principal threats - communal violence, the Telangana "
            "insurgency, princely-state integration and the Kashmir war - "
            "unfolded together rather than in sequence.",
            "The leadership's method combined secular reassurance, coercive "
            "capacity and reconciliation, containing riots, banning and later "
            "rehabilitating a proscribed organisation, integrating states and "
            "defeating an insurgency while keeping the party behind it legal.",
            "Simultaneity also explains institutional choices, including the "
            "constitutional preference for a strong centre and for emergency "
            "provisions.",
        ],
        "Never present the crises as sequential; the Advanced owner "
        "explicitly warns against it, and simultaneity is the analytical "
        "point that a chronological narration destroys.",
        "Use simultaneity as the thesis of any question on the challenges of "
        "the initial years.",
        """1947-51 -> FOUR PRESSURES AT ONCE (not a sequence)
        +---------------------------+
        |  COMMUNAL VIOLENCE        |
        |  TELANGANA INSURGENCY     |  ---> all live in the same months
        |  PRINCELY INTEGRATION     |
        |  KASHMIR WAR              |
        +---------------------------+
METHOD -> secular reassurance + coercive capacity + reconciliation, without suspending democracy
CONSEQUENCE -> the constitutional preference for a strong centre and emergency provisions.""",
        "Simultaneity denotes the concurrence, rather than the succession, of "
        "communal violence, insurgency, princely integration and armed "
        "conflict in the initial years of the republic.",
    ),
    authored_session(
        "Nearly six million: a one-directional figure and how to use it",
        "The refugee figure is the most commonly misused number in "
        "post-independence history, because it counts movement in one "
        "direction and is routinely quoted as though it measured total "
        "displacement across the new border.",
        [
            "The source records nearly six million refugees pouring into "
            "India after Partition, having lost everything.",
            "This is a figure for people entering India and is not the total "
            "displacement in both directions, which the source does not give "
            "in this form.",
            "By 1951 the rehabilitation of refugees from West Pakistan had "
            "been substantially completed, and most refugees from West Punjab "
            "could be resettled on land left by migrants to Pakistan.",
            "The eastern flow was structurally different: migration from East "
            "Bengal continued year after year, resettlement land was not "
            "available in the same way, and many agricultural households were "
            "pushed into a semi-urban and urban underclass.",
        ],
        "Always mark the figure as one-directional movement into India, and "
        "never describe six million as the total number displaced by "
        "Partition.",
        "Use the east-west contrast to show that rehabilitation was two "
        "different problems, not one.",
        """REFUGEE FIGURE -> read the direction before quoting the number
NEARLY SIX MILLION -> people ENTERING INDIA (one direction only)
NOT                -> total displacement across the border in both directions
WEST FLOW  -> largely a single movement in 1947; land vacated by migrants; resettled by 1951
EAST FLOW  -> continuous migration from East Bengal year after year; little land available
           -> agricultural households pushed into a semi-urban and urban underclass
RULE -> one figure, one direction, two very different rehabilitation problems.""",
        "The six-million refugee figure denotes the source's estimate of "
        "people entering India after Partition, a one-directional count and "
        "not a measure of total displacement.",
    ),
    authored_session(
        "Roughly 500,000: attribution, dispute and answer discipline",
        "Partition mortality is the clearest test of source discipline in the "
        "whole subject, because a widely quoted figure exists, it is a single "
        "author's estimate, and the wider scholarship does not agree with it.",
        [
            "The source states that nearly 500,000 people were killed in the "
            "span of a few months, alongside the destruction of property "
            "worth thousands of millions of rupees.",
            "The repository owner records explicitly that this is Chandra's "
            "estimate and that wider scholarship offers substantially "
            "different totals, so it is not settled scholarship.",
            "The correct exam behaviour is to name the author, give the "
            "estimate as an estimate, and state that other scholarship "
            "differs, in one sentence.",
            "The same discipline applies to every other figure in this topic, "
            "including literacy, life expectancy, landless labour, refugees "
            "and the assets transfer.",
        ],
        "Never present partition mortality as an agreed death toll and never "
        "state it with false precision; attribution is not a hedge here, it "
        "is the accurate description of the evidence.",
        "Use the attributed sentence as a demonstration of historiographical "
        "care in a 15 or 20-mark answer.",
        """PARTITION MORTALITY -> how to write one safe sentence
SOURCE SAYS -> nearly 500,000 killed within a few months
OWNER SAYS  -> this is Chandra's estimate; wider scholarship differs substantially
THEREFORE   -> NOT settled scholarship; NOT an agreed death toll
SAFE SENTENCE -> "Chandra estimates roughly 500,000 deaths, though other scholarship
                 offers substantially different totals."
SAME RULE FOR -> literacy | life expectancy | landless labour | refugees | assets transfer.""",
        "The 500,000 mortality estimate is Chandra's attributed figure for "
        "deaths in the months around Partition, explicitly contested by "
        "wider scholarship and therefore never to be stated as a settled "
        "total.",
    ),
    authored_session(
        "30 January 1948: assassination, ban and the conditions of 1949",
        "Gandhi's assassination is the hinge of the initial years, because it "
        "produced both the sharpest communal danger and the strongest "
        "secular consolidation, and the state's response shows how the "
        "republic combined proscription with civil-libertarian restraint.",
        [
            "Gandhi was assassinated on 30 January 1948 by Nathuram Godse, "
            "described in the source as a Hindu communal fanatic, and the "
            "shock caused communalism to retreat sharply.",
            "The government immediately banned the Rashtriya Swayamsevak "
            "Sangh and arrested most of its leaders and functionaries.",
            "The ban was lifted in July 1949 after the organisation accepted "
            "conditions laid down by Patel as Home Minister: a written and "
            "published constitution, restriction to cultural activity, "
            "renunciation of violence and secrecy, loyalty to India's flag "
            "and Constitution, and democratic internal organisation.",
            "In January 1948, following a fast by Gandhi, the Government of "
            "India paid Pakistan Rs 550 million as part of the assets of "
            "Partition even while fearing how the money might be used.",
            "The source also records Nehru's own preference, expressed in "
            "June 1949, that the fewer such bans and detentions there were "
            "the better, which is why the episode is evidence of restraint as "
            "well as of firmness.",
        ],
        "Use only the sourced dates and the sourced conditions for the ban "
        "and its lifting, and never suggest that Gandhi was killed by a "
        "member of a minority community.",
        "Use this episode to show that the founding secularism combined "
        "coercive capacity with civil-libertarian restraint.",
        """30 JANUARY 1948 AND AFTER -> firmness plus restraint
30 JAN 1948 -> Gandhi assassinated by Nathuram Godse -> communalism retreats sharply
IMMEDIATE   -> ban on the Rashtriya Swayamsevak Sangh; leaders and functionaries arrested
JAN 1948    -> after a fast by Gandhi, Rs 550 million paid to Pakistan (assets of Partition)
JULY 1949   -> ban lifted on FIVE accepted conditions laid down by Patel as Home Minister
             written constitution | cultural activity only | no violence or secrecy
             loyalty to flag and Constitution | democratic internal organisation
READING     -> proscription used, then withdrawn on terms; not permanent suppression.""",
        "The 1948 to 1949 proscription episode denotes the immediate ban on "
        "the Rashtriya Swayamsevak Sangh after Gandhi's assassination and its "
        "lifting in July 1949 on five conditions accepted from the Home "
        "Minister.",
    ),
    authored_session(
        "Insurrection to elections: the Communist transition and Telangana",
        "The Communist trajectory of 1948 to 1951 is the clearest evidence "
        "that the republic defeated an armed challenge without destroying the "
        "party that made it, and that combination is the actual content of "
        "the phrase democratic consolidation.",
        [
            "From February 1948 the Communist Party of India, under the line "
            "associated with B.T. Ranadive, declared independence false and "
            "turned to armed struggle.",
            "A Communist-led peasant struggle had developed in the Telangana "
            "region of Hyderabad state from the latter half of 1946, spelt "
            "Telengana in the local text, and it revived when peasant squads "
            "organised defence against the Razakars.",
            "The Telangana armed struggle was called off by mid-1951 as the "
            "party abandoned insurrection for the parliamentary path.",
            "Once the party gave up armed struggle and declared its intention "
            "to join the parliamentary process, it was legalised everywhere, "
            "its leaders and cadres were released, and it was allowed to "
            "contest the first general elections.",
        ],
        "Do not present the Communist Party as having always followed the "
        "parliamentary road, and do not present its suppression as "
        "permanent; the transition ran in both directions and is precisely "
        "attributable.",
        "Use this as the internal-security paragraph in any answer on the "
        "initial years, paired with the secularism paragraph.",
        """INSURRECTION -> ELECTIONS (1946-52)
LATE 1946 -> Communist-led peasant struggle in Telangana inside Hyderabad state
FEB 1948  -> B.T. Ranadive line: independence declared false; armed struggle adopted
1948-51   -> insurgency contained by the state while the political door is left open
MID-1951  -> Telangana struggle called off; parliamentary path adopted
THEN      -> party legalised; leaders and cadres released; allowed to contest elections
LESSON    -> the challenge was defeated; the party was not abolished.""",
        "The Communist transition denotes the movement of the Communist Party "
        "of India from the insurrectionary line of February 1948 and the "
        "Telangana armed struggle to the parliamentary path adopted by "
        "mid-1951.",
    ),
    authored_session(
        "Completing the map: Pondicherry, Goa, and two Operations",
        "The territorial map of the republic was not complete in 1947, and "
        "the two enclave settlements are examined both for their dates and "
        "for the operation names that candidates routinely confuse.",
        [
            "The French authorities negotiated and handed over Pondicherry "
            "and the other French possessions to India in 1954.",
            "The Portuguese refused to leave, a Goan freedom movement was "
            "suppressed, and satyagrahis marching from India were also "
            "suppressed, so the settlement was delayed for years.",
            "Indian troops entered Goa on the night of 17 December 1961 in "
            "the action known as Operation Vijay, the Governor-General "
            "surrendered without a fight, and the territorial and political "
            "integration of India was completed after more than fourteen "
            "years.",
            "Operation Vijay in Goa in December 1961 must never be confused "
            "with Operation Polo, the Hyderabad police action of September "
            "1948, since the two differ in date, adversary and "
            "constitutional character.",
        ],
        "Neither Goa nor Pondicherry joined the Union in 1947; give 1954 and "
        "December 1961, and keep Operation Vijay and Operation Polo apart.",
        "Use the enclave settlements to close the polity and international "
        "relations domains of a consolidation answer.",
        """COMPLETING THE MAP -> two settlements, two operations, no confusion
1954            -> FRENCH possessions centred on Pondicherry handed over after negotiation
17 DEC 1961     -> Indian troops enter GOA -> OPERATION VIJAY -> Governor-General surrenders
ELAPSED         -> more than fourteen years after independence
DO NOT CONFUSE  -> OPERATION VIJAY  = Goa, December 1961, Portuguese rule ended
                -> OPERATION POLO   = Hyderabad, September 1948, princely accession secured
TRAP            -> "Goa joined in 1947" is wrong by fourteen years.""",
        "Operation Vijay denotes the Indian military action beginning on the "
        "night of 17 December 1961 that ended Portuguese rule in Goa, "
        "distinct from Operation Polo, the Hyderabad police action of "
        "September 1948.",
    ),
    authored_session(
        "The four-domain answer and the seventy-seventh Republic Day",
        "This topic exists in the syllabus to be examined as a four-domain "
        "consolidation question, and the closing session solves that demand "
        "directly while using the live commemorative anchor only to fix the "
        "distinction between 1947 and 1950.",
        [
            "The routed 2025 GS-I demand asks the candidate to trace India's "
            "consolidation process during the early phase of independence in "
            "terms of polity, economy, education and international relations, "
            "in 250 words.",
            "The founding consensus that answers it has five commitments - "
            "democracy, secularism, planning, civilian control of the armed "
            "forces and non-alignment - and each must be graded by an "
            "achievement and a limit rather than celebrated.",
            "The achievements to state are territorial unification, a "
            "constitution with universal adult franchise, secularism "
            "maintained after Gandhi's assassination, an insurgency ended by "
            "political means, and civilian control preserved; the limits are "
            "slow growth, land reform largely unimplemented, primary "
            "education and female literacy neglected, and a contested "
            "frontier unresolved.",
            "A Ministry of Defence release carried by the Press Information "
            "Bureau on 25 January 2026 records the 77th Republic Day on 26 "
            "January 2026 on the parade theme of unity in diversity, and the "
            "ordinal is used here only because counting 1950 as the first "
            "Republic Day is what makes 2026 the seventy-seventh.",
        ],
        "Answer the four named domains in the order the examiner names them, "
        "give each one institution and one limitation, and treat a ceremonial "
        "parade as a framing device and never as historical evidence about "
        "the years 1947 to 1951.",
        "Use this session as the direct model for the 2025 GS-I answer and "
        "for any founding-consensus evaluation.",
        """THE FOUR-DOMAIN ENGINE (2025 GS-I demand) -> one paragraph each, in this order
POLITY    -> accession and merger | Constitution 26 Nov 1949 / 26 Jan 1950 | universal franchise
             LIMIT: strong-centre bias; regional questions unresolved
ECONOMY   -> planned, state-led framework with a public-sector core and land-reform law
             LIMIT: slow growth; land reform largely unimplemented
EDUCATION -> from about 84% illiteracy (1951) to deliberate university, technical and
             scientific investment | LIMIT: elite-first; primary and female education lag
INT. REL. -> non-alignment and Asian solidarity; map completed 1954 and December 1961
             LIMIT: limited hard power
INTERLOCK -> settlement enables planning; planning needs peace; non-alignment buys peace
ANCHOR    -> 77th Republic Day on 26 January 2026 works only because 1950 was the first.""",
        "The four-domain consolidation engine is the answer structure "
        "required by the 2025 GS-I demand, taking polity, economy, education "
        "and international relations in turn with one institution and one "
        "limitation in each.",
    ),
]

PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-28": [
        (
            "Lapse of paramountcy and the constructed Union",
            "causal-flow",
            """15 AUG 1947 -> BRITISH RULE ENDS -> paramountcy LAPSES (it is not transferred)
BRITISH INDIA -> partitioned by statute; successor dominions defined in law
PRINCELY INDIA -> no successor sovereign in law -> authority must be constructed
INSTRUMENTS USED -> agreement + leverage + popular pressure + force in one case
RULE -> lapse, not transfer; the single word that generates the whole topic.""",
            ["Independence was not integration: the problem the lapse created"],
        ),
        (
            "Counting convention: why more than 560 is the safe form",
            "data-table",
            """CLAIM              | STATUS
"more than 560"    | required formulation in both repository owners
562 / 565          | different classification rules for estates, jagirs, minor holdings
"over 560"         | the form used on official commemorative pages
local OCR numeral  | corrupted in extraction; cannot arbitrate between totals
VERDICT -> the disagreement is about enumeration conventions, not about history.""",
            ["How many states: the discipline behind more than 560"],
        ),
        (
            "The States Department as a working machine",
            "institution-map",
            """STATES DEPARTMENT (created 27 June 1947)
|-- MINISTER   -> Sardar Vallabhbhai Patel, Home and States Minister
|-- SECRETARY  -> V.P. Menon, drafting, negotiation, administrative sequencing
|-- METHOD     -> appeal to patriotism + narrow legal demand + warning of stiffer terms
`-- PRODUCT    -> standardised Instruments of Accession and standstill arrangements
NAMING RULE -> minister, secretary and department together, never one man alone.""",
            ["The States Department: a minister, a secretary and a machine"],
        ),
        (
            "Three subjects taken, everything else left behind",
            "comparison",
            """TRANSFERRED AT ACCESSION      | RETAINED BY THE RULER AT ACCESSION
Defence                       | internal administration
External Affairs              | revenue and taxation inside the state
Communications                | courts and internal justice
                              | succession, titles, ceremonial privilege
WHY IT WORKED -> the three taken were exactly the three no state could exercise alone
WHY IT LOOKED SMALL -> the ruler's visible world was untouched on the day of signature.""",
            ["The three-subject formula and why its narrowness worked"],
        ),
        (
            "The accession calendar of 1947",
            "timeline",
            """20 FEB 1947 -> Attlee: paramountcy will not be handed to any government of British India
APR 1947    -> some states join the Constituent Assembly; others announce independence hopes
18 JUN 1947 -> Jinnah: states become independent sovereign states on termination
27 JUN 1947 -> States Department created; Patel takes charge, V.P. Menon as Secretary
15 AUG 1947 -> all states except Junagadh, Jammu and Kashmir, Hyderabad have acceded
READ AS -> a seven-week campaign against a legal vacuum, not a leisurely negotiation.""",
            ["Attlee and Jinnah: the encouragement the princes received"],
        ),
        (
            "The prince squeezed from above and below",
            "balance-sheet",
            """PRESSURE FROM ABOVE -> States Department: accede narrowly now, or face stiffer terms
PRESSURE FROM BELOW -> States' Peoples' Conference: democratic order and integration
PRESSURE FROM OUTSIDE -> Partition violence makes isolation dangerous, not sovereign
DOCTRINE AGAINST HIM -> political power belongs to the people of a state, not to the ruler
BARGAIN OFFERED -> three subjects surrendered; dignities, succession and income retained
OUTCOME -> the overwhelming majority accede without force being used at all.""",
            ["Two pressures on the princes: their own people and Partition"],
        ),
        (
            "Four stages, four instruments, four difficulties",
            "timeline",
            """1 ACCESSION       -> Instrument of Accession, three subjects      -> by 15 Aug 1947
2 MERGER          -> merger agreements, unions, attachments        -> from Dec 1947
3 DEMOCRATISATION -> elections, courts, services inside old states -> uneven and slower
4 INCORPORATION   -> Constitution and single citizenship           -> 26 Jan 1950
STRUCTURAL ERROR -> treating stage one as the finished process
CORRECTION -> each stage has its own instrument, its own date and its own difficulty.""",
            ["Accession, merger, democratisation, incorporation: four stages"],
        ),
        (
            "Junagadh settled by counting people",
            "causal-flow",
            """NAWAB accedes to Pakistan -> against population and against geography
POPULATION overwhelmingly Hindu -> popular movement -> Nawab flees
PROVISIONAL GOVERNMENT formed inside the state
DEWAN Shah Nawaz Bhutto invites the Government of India to intervene
INDIAN TROOPS enter; PLEBISCITE held FEBRUARY 1948 -> result favours India
DISCIPLINE -> the source calls the result overwhelming; no percentage is asserted here.""",
            ["Junagadh: the ruler-subject mismatch and February 1948"],
        ),
        (
            "Hyderabad: negotiation exhausted before force",
            "timeline",
            """PRE-AUG 1947 -> Nizam claims independent status; state landlocked inside India
NOV 1947     -> STANDSTILL AGREEMENT signed; representative government hoped for
1947-48      -> Ittihad ul Muslimin and Razakars grow; State Congress satyagraha
             -> Communist-led peasant struggle continues in the Telangana region
JUN 1948     -> Patel presses for unqualified accession and responsible government
SEP 1948     -> OPERATION POLO / POLICE ACTION -> Nizam surrenders -> accedes to the Union
DISCIPLINE   -> no casualty figure and no troop figure is asserted for this episode.""",
            ["Hyderabad: standstill, Razakars and September 1948"],
        ),
        (
            "Kashmir: the fixed order of events",
            "timeline",
            """STEP 1 -> Maharaja Hari Singh accedes to neither dominion
STEP 2 -> National Conference under Sheikh Abdullah favours accession to India
STEP 3 -> OCTOBER 1947 tribal invasion advances towards Srinagar
STEP 4 -> Maharaja appeals to India for military assistance
STEP 5 -> Instrument of Accession signed; Sheikh Abdullah heads the administration
STEP 6 -> troops flown to Srinagar only AFTER accession
STEP 7 -> 30 DEC 1947 reference to the UN Security Council; fighting continues
STOP LINE -> restraint beyond step seven; contested later claims are not taught here.""",
            ["Kashmir: October 1947, accession, and disciplined restraint"],
        ),
        (
            "The merger map of the second stage",
            "institution-map",
            """SECOND STAGE (from December 1947) -> turning acceding units into governable provinces
|-- MERGED    -> small states attached to neighbouring provinces or centrally administered
|-- UNIONS    -> Madhya Bharat | Rajasthan | Patiala and East Punjab States Union
|             -> Saurashtra | Travancore-Cochin
`-- RETAINED  -> Mysore | Hyderabad | Jammu and Kashmir as separate states of the Union
RESULT -> a deliberately asymmetrical map that later reorganisation would revisit.""",
            ["Unions and mergers: making unviable states administrable"],
        ),
        (
            "Price paid, process completed, commemoration handled",
            "balance-sheet",
            """PRICE     -> privy purses, titles, succession, ceremonial privilege retained by rulers
          -> not abolished during initial integration; owner dates abolition to 1971
          -> no purse amount is asserted anywhere in this package
COMPLETION-> Constitution adopted 26 Nov 1949; in force 26 Jan 1950; single citizenship
          -> independence 15 Aug 1947 and republic 26 Jan 1950 answer different questions
COMMEMORATION -> Ministry of Culture two-year programme from 31 Oct 2024 at the Statue of Unity
              -> PIB Backgrounder 30 Oct 2025: Rashtriya Ekta Diwas annually on 31 October
CAUTION   -> the commemorative phrase "by 15 August 1947 or shortly thereafter" compresses
             a chronology that runs to February and September 1948.""",
            [
                "Privy purses and privileges: the price carried forward",
                "From acceding state to citizen: 1949 and 1950",
                "Commemoration and chronology: reading Ekta Diwas as a historian",
            ],
        ),
    ],
    "modern-indian-history-29": [
        (
            "The balance sheet the republic opened with",
            "comparison",
            """COLONIAL LIABILITY (economic and administrative) | MOVEMENT ASSET (political)
dependent, stagnant, famine-prone economy        | tested all-India leadership
mass illiteracy and low life expectancy          | party organised in every province
rentier agriculture, rising landlessness         | democracy, civil liberties, secularism
apparatus built for extraction and order         | three decades of practised organisation
CENTRAL QUESTION -> how did the second column carry the first without collapsing?
ERROR TO AVOID -> merging the columns and crediting the empire with Indian democracy.""",
            ["Two inheritances: colonial liabilities against movement assets"],
        ),
        (
            "How underdevelopment was developed",
            "causal-flow",
            """SUBORDINATE INTEGRATION with the world capitalist system since the 1750s
-> forced international division of labour: raw materials out, manufactures in
-> real change in railways, administration, education, finance and communications
-> but change operating INSIDE a colonial frame crystallises a dependent structure
-> poverty, dependence and subordination reproduced rather than growth generated
ATTRIBUTION -> the phrase development of underdevelopment belongs to A. Gunder Frank.""",
            ["The development of underdevelopment and its exact attribution"],
        ),
        (
            "The agrarian legacy in attributed numbers",
            "data-table",
            """MEASURE                                   | SOURCE-ATTRIBUTED VALUE
per capita agricultural production        | falls about 14% between 1901 and 1941
per capita foodgrains                     | falls further than total production
landless agricultural labourers           | about 13% in 1871 rising to about 28% by 1951
land controlled by landlords by the 1940s | reported as over 70% in the local text
STRUCTURE -> landlords, moneylenders, merchants and the colonial revenue state
INCENTIVE -> rack-renting and usury are safer than investment, so stagnation is rational.""",
            ["The agrarian legacy: landlessness, stagnation and rent"],
        ),
        (
            "The human baseline of 1951",
            "data-table",
            """MEASURE                   | SOURCE-ATTRIBUTED VALUE (1951 unless stated)
illiteracy, all Indians   | nearly 84 per cent
illiteracy, women         | about 92 per cent; about 8 literate women in every 100
life expectancy at birth  | barely 32 years for an Indian born between 1940 and 1951
death rate, 1941-50       | about 25 per 1,000 persons a year
infant mortality          | between 175 and 190 per 1,000 live births
CAUSE -> colonial neglect of mass, technical and female education, not poverty alone.""",
            ["Bodies and minds in 1951: literacy and life expectancy"],
        ),
        (
            "The state that was kept rather than dismantled",
            "institution-map",
            """INHERITED APPARATUS
|-- AUTHORITARIAN CORE -> repressive laws framed without Indian democratic consent
|                      -> wide arbitrary power with civil servants and police
|                      -> collector and district magistrate in one office
|-- LIBERAL FRAGMENTS  -> rule of law | relatively independent judiciary
|                      -> press, speech and association tolerated in calm periods
`-- REPUBLIC'S TASK    -> convert an instrument of order and extraction into one of development
THESIS -> continuity with conversion, not rupture; that conversion is the real legacy problem.""",
            ["The colonial state the republic actually inherited"],
        ),
        (
            "Three franchises, one break",
            "comparison",
            """AFTER 1919 | about 3 per cent of Indians could vote | legislatures with little power
AFTER 1935 | about 15 per cent could vote            | supreme power still with the British
REPUBLIC   | universal adult franchise               | free and fair elections by right
COLONIAL PURPOSE -> co-opt and weaken the national movement while keeping the reins
UNINTENDED EFFECT -> Indians gain practical experience of elections and elected organs
THE BREAK -> the republic replaced the colonial franchise; it did not widen it by degrees.""",
            [
                "About 3 per cent and about 15 per cent: the franchise refused",
                "Universal adult franchise as the boldest decision of the period",
            ],
        ),
        (
            "Movement assets converted into republican institutions",
            "institution-map",
            """NATIONAL MOVEMENT
|-- LEADERSHIP -> Nehru | Patel | Azad | Rajendra Prasad -> no single region or community
|-- BREADTH    -> first Nehru cabinet of fourteen includes five non-Congressmen
|              -> B.R. Ambedkar chairs the Drafting Committee
|-- HABITS     -> accommodative politics; three decades of elections, argument, organisation
`-- CONVERSION -> all-India services and a national army on merit, under civilian control
LATER COST -> the same dominance becomes the Congress system whose decay is a later topic.""",
            ["The national movement as an institutional, not sentimental, asset"],
        ),
        (
            "Four pressures in the same months",
            "balance-sheet",
            """COMMUNAL VIOLENCE        -> refugee movement, killing, minority insecurity
TELANGANA INSURGENCY     -> armed communist challenge inside the new republic
PRINCELY INTEGRATION     -> more than 560 units to accede, merge and democratise
CONTESTED FRONTIER       -> fighting and an international reference in Kashmir
PLUS -> a divided army and a divided treasury inherited on the first day
METHOD -> secular reassurance + coercive capacity + reconciliation, democracy not suspended
CONSEQUENCE -> the constitutional preference for a strong centre and emergency provisions.""",
            ["Simultaneity: why the initial years are one crisis, not four"],
        ),
        (
            "Reading the two most misused figures",
            "comparison",
            """FIGURE                | WHAT IT IS                 | WHAT IT IS NOT
nearly six million    | refugees ENTERING India    | total displacement both ways
roughly 500,000 dead  | Chandra's estimate         | settled or agreed scholarship
WEST FLOW -> largely one movement in 1947; land vacated; resettled substantially by 1951
EAST FLOW -> continuous migration from East Bengal; little land; urban underclass formed
SAFE SENTENCE -> name the author, mark the direction, record that other scholarship differs.""",
            [
                "Nearly six million: a one-directional figure and how to use it",
                "Roughly 500,000: attribution, dispute and answer discipline",
            ],
        ),
        (
            "From assassination to the lifted ban",
            "timeline",
            """JAN 1948    -> after a fast by Gandhi, Rs 550 million paid to Pakistan (assets settlement)
30 JAN 1948 -> Gandhi assassinated by Nathuram Godse -> communalism retreats sharply
IMMEDIATE   -> Rashtriya Swayamsevak Sangh banned; leaders and functionaries arrested
JUN 1949    -> Nehru records a preference for fewer bans and detentions
JULY 1949   -> ban lifted on accepted conditions: written and published constitution,
               cultural activity only, no violence or secrecy, loyalty to flag and
               Constitution, democratic internal organisation
READING     -> proscription used and then withdrawn on terms, not permanent suppression.""",
            ["30 January 1948: assassination, ban and the conditions of 1949"],
        ),
        (
            "Insurrection converted into opposition",
            "causal-flow",
            """LATE 1946 -> Communist-led peasant struggle develops in Telangana inside Hyderabad state
FEB 1948  -> B.T. Ranadive line declares independence false and adopts armed struggle
1948-51   -> insurgency contained by the state while the political door is kept open
MID-1951  -> Telangana struggle called off; the parliamentary path is adopted
THEN      -> party legalised everywhere; leaders and cadres released; elections contested
LESSON    -> the armed challenge was defeated and the party was not abolished.""",
            ["Insurrection to elections: the Communist transition and Telangana"],
        ),
        (
            "Four domains, two dates and one completed map",
            "balance-sheet",
            """POLITY    -> integration, Constitution 26 Nov 1949 / 26 Jan 1950, universal adult franchise
             LIMIT: strong-centre bias and unresolved regional questions
ECONOMY   -> planned, state-led development with a public-sector core and land-reform law
             LIMIT: slow growth and land reform largely unimplemented
EDUCATION -> from about 84 per cent illiteracy to deliberate scientific and technical investment
             LIMIT: elite-first expansion; primary and female education lag badly
INT. REL. -> non-alignment and Asian solidarity; Pondicherry 1954; Goa 17 December 1961
             LIMIT: limited hard power
TWO DATES -> independence 15 Aug 1947 | republic 26 Jan 1950; the 2026 parade is the 77th
             precisely because 1950 counts as the first
DO NOT CONFUSE -> Operation Vijay (Goa, Dec 1961) with Operation Polo (Hyderabad, Sep 1948).""",
            [
                "Completing the map: Pondicherry, Goa, and two Operations",
                "The four-domain answer and the seventy-seventh Republic Day",
            ],
        ),
    ],
}


TOPIC_CHRONOLOGY = {
    "modern-indian-history-28": [
        "20 February 1947",
        "April 1947",
        "18 June 1947",
        "27 June 1947",
        "15 August 1947",
        "October 1947",
        "November 1947",
        "30 December 1947",
        "February 1948",
        "September 1948",
        "26 November 1949",
        "26 January 1950",
        "31 October 2024",
    ],
    "modern-indian-history-29": [
        "1871",
        "between 1901 and 1941",
        "after 1919",
        "after 1935",
        "15 August 1947",
        "January 1948",
        "30 January 1948",
        "February 1948",
        "July 1949",
        "26 November 1949",
        "26 January 1950",
        "8 April 1950",
        "mid-1951",
        "1954",
        "17 December 1961",
        "26 January 2026",
    ],
}

FORBIDDEN_TOPIC_PHRASES = {
    "modern-indian-history-28": [
        "paramountcy was transferred to India",
        "paramountcy passed automatically to India",
        "paramountcy passed to the Indian Union",
        "there were exactly 562 princely states",
        "there were exactly 565 princely states",
        "all the princely states joined India automatically",
        "every princely state acceded on 15 August 1947",
        "the Instrument of Accession transferred all subjects",
        "Operation Polo was conducted in Kashmir",
        "Operation Polo relates to Kashmir",
        "Operation Vijay integrated Hyderabad",
        "Operation Polo liberated Goa",
        "privy purses were abolished at the moment of accession",
        "privy purses ended in 1947",
        "India became a republic on 15 August 1947",
        "India became a republic in 1947",
        "the three problem states were all Muslim-majority",
        "the three states posed the same problem",
        "Junagadh, Hyderabad and Kashmir were identical",
        "Patel integrated the princely states single-handedly",
        "the Junagadh plebiscite was held in 1947",
        "accession was the whole of integration",
    ],
    "modern-indian-history-29": [
        "India inherited a healthy economy in 1947",
        "universal adult franchise existed under colonial rule",
        "the colonial franchise was universal",
        "Goa joined India in 1947",
        "Goa was liberated in 1947",
        "Pondicherry was transferred in 1947",
        "Gandhi was assassinated by a Muslim",
        "the partition death toll was exactly",
        "exactly 500,000 people were killed",
        "six million people were displaced in both directions",
        "six million is the total displacement",
        "six million was the total number displaced",
        "Operation Vijay integrated Hyderabad",
        "Operation Polo liberated Goa",
        "partition mortality is settled scholarship",
        "Chandra's estimate is settled scholarship",
        "the republic inherited a developed industrial economy",
        "India became a republic on 15 August 1947",
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
        "scope": "Modern Indian History learner-v2 Topics 28-29",
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


TOPIC_28_STRICT = [
    "lapsed when British rule ended on 15 August 1947",
    "never transferred to India or Pakistan",
    "more than 560",
    "562 and 565",
    "Defence, External Affairs and Communications",
    "V.P. Menon",
    "States Department",
    "27 June 1947",
    "20 February 1947",
    "18 June 1947",
    "Accession, merger, democratisation and constitutional incorporation "
    "are four different stages",
    "ruler's choice, the population's composition, the state's geography and "
    "the security situation",
    "plebiscite held in Junagadh in February 1948",
    "Operation Polo",
    "September 1948",
    "October 1947",
    "not abolished during the initial integration",
    "asserts no amount for any purse",
    "states no percentage",
    "no casualty or troop figure",
    "26 November 1949",
    "26 January 1950",
    "Rashtriya Ekta Diwas",
    "Statue of Unity",
    "commemorative compression",
    "31 October 2024",
    "contested later claims",
    "Assess the main administrative issues and socio-cultural problems",
]

TOPIC_29_STRICT = [
    "colonial economic and administrative liabilities",
    "universal adult franchise",
    "about 3 per cent of Indians could vote after 1919",
    "about 15 per cent after 1935",
    "A. Gunder Frank",
    "one-directional",
    "not settled scholarship",
    "30 January 1948",
    "Nathuram Godse",
    "July 1949",
    "Nehru-Liaquat Pact",
    "Nehru-Liaqat",
    "8 April 1950",
    "B.T. Ranadive",
    "mid-1951",
    "Pondicherry",
    "17 December 1961",
    "Operation Vijay",
    "Operation Polo",
    "founding consensus",
    "civilian control",
    "non-alignment",
    "polity, economy, education and international relations",
    "Trace India's consolidation process during early phase of independence",
    "77th Republic Day",
    "26 January 2026",
    "attributed estimate",
    "nearly six million",
]


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

    strict = (
        TOPIC_28_STRICT
        if key == "modern-indian-history-28"
        else TOPIC_29_STRICT
    )
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
    """Topics 26-27 must remain exactly as their own generator authored them."""

    expected = ["modern-indian-history-26", "modern-indian-history-27"]
    if [config["key"] for config in previous.TOPICS] != expected:
        raise ValueError("Topics 26-27 configuration was mutated on import.")
    if set(previous.PANEL_DATA) != set(expected):
        raise ValueError("Topics 26-27 panel data was mutated on import.")
    if previous.ASCII_PATH == ASCII_PATH:
        raise ValueError("Topics 26-27 ASCII specification would be rewritten.")


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
