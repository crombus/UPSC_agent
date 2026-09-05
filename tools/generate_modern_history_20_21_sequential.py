"""Build Modern Indian History learner-v2 Topics 20-21.

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
import generate_modern_history_18_19_sequential as previous


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
    / "modern-indian-history-20-21-2026-08-31-sequential.json"
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
            ROOT / "knowledge-export" / "Prelims PYQ" / "2025-GS1-Set A.md",
            ROOT / "knowledge-export" / "Prelims PYQ" / "Ans-2025-GS1.md",
            ROOT / "books" / "prelima_question_paper_answers" / "2025-GS1-Set A.pdf",
            ROOT / "books" / "prelima_question_paper_answers" / "Ans-2025-GS1.pdf",
            ROOT / "knowledge-export" / "Prelims PYQ" / "2026-GS1-Set A.md",
            ROOT
            / "knowledge-export"
            / "Prelims PYQ"
            / "Ans-2026-GS1-Provisional.md",
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md",
            ROOT / "knowledge-export" / "Mains PYQ" / "Gen_St_P1.pdf.md",
            ROOT / "knowledge-export" / "Prelims PYQ" / "QP-CSP-18-GS-I-C.pdf.md",
        ]
    )
)
OFFICIAL_QUESTION_SOURCES = [
    path for path in OFFICIAL_QUESTION_SOURCES if path.is_file()
]


TOPICS = [
    base.topic(
        20,
        "Non-Cooperation & the Khilafat Movement (1919\u20131922)",
        "20_Non-Cooperation-and-Khilafat-Movement.md",
        "20_Non-Cooperation-and-Khilafat-Movement.md",
        "20_Non-Cooperation-Khilafat-Movement_Complete-Topic-Package.md",
        [
            "basic/19_Gandhis-Rise-Rowlatt-and-Jallianwala.md",
            "basic/21_Swarajists-and-Revolutionaries-1920s.md",
            "basic/22_Simon-Nehru-Report-CDM-and-RTC.md",
            "advanced/19_Gandhis-Rise-Rowlatt-and-Jallianwala.md",
        ],
        [
            "https://www.gandhiheritageportal.org/",
            "https://www.gujaratvidyapith.edu.in/news/72nd-padvidaan-2026",
            "https://indianexpress.com/article/cities/ahmedabad/"
            "gujarat-vidyapith-mahatma-gandhi-amit-shah-india-path-"
            "punarnirman-modi-government-10852889/",
        ],
        "Gujarat Vidyapith held its 72nd convocation (Padvidaan) on 27 "
        "August 2026 at Ahmedabad, with Union Home Minister Amit Shah as "
        "chief guest and Governor Acharya Devvrat presiding as Chancellor; "
        "the address invoked Gandhi's educational philosophy (hands, heart "
        "and mind; his eleven vows and seven social sins) for the roughly "
        "900 graduating students. This is retained only as a live "
        "Gandhi institution-building and public-memory bridge for the "
        "constructive-programme institutions named in this package. "
        "Gujarat Vidyapith was founded in 1920, so 2026 marks its "
        "106th year, not a centenary; this package does not describe the "
        "2026 convocation as a centenary of the institution's founding, "
        "and the bridge supplies no new fact about the 1919-1922 "
        "Non-Cooperation and Khilafat sequence itself.",
        "OCR-based verification for this pass relies on the repository's "
        "already-authored Basic and Advanced Markdown owners for Non-Cooperation "
        "and Khilafat, themselves grounded in Bipin Chandra's Modern India "
        "(Chapter XV) and India's Struggle for Independence. This authoring pass "
        "does not re-open the source PDFs to assert new page numbers beyond what "
        "those owners already state, to avoid citing an unverified page reference. "
        "One exception was made to verify the withdrawal-historiography debate: "
        "`knowledge-export/History/INDIA STRUGGLE FOR INDEPENDENCE-- BIPIN C "
        "ENG.md` (around lines 8062-8230) was re-opened and confirms R. Palme "
        "Dutt's *India Today* class-protection thesis (that Gandhi withdrew to "
        "shield propertied landlord-capitalist interests from a radicalising "
        "peasantry) alongside Bipin Chandra's own rebuttal (that the Chauri "
        "Chaura crowd showed no anti-property intent, that agrarian unrest was "
        "already ebbing by late 1921, and that withdrawal pre-empted government "
        "repression rather than protected property). The same OCR page records "
        "the incident one calendar day earlier than this package's verified "
        "date; that internal figure is superseded here using the Prime "
        "Minister's official centenary-linked commemorative material and "
        "Sekhar Bandyopadhyay's Plassey to Partition (OCR p.305), both of "
        "which independently confirm 4 February 1922, while the 12 February "
        "1922 Bardoli withdrawal date is unaffected and confirmed in the same "
        "source.",
        "Four 2025 Prelims GS-I demands (Q12, Q20, Q71, Q73) and one 2026 "
        "Prelims GS-I demand (Q9) are routed to this topic. The 2025 "
        "Series-A answer key is confirmed directly from the local official "
        "answer-key PDF (`books/prelima_question_paper_answers/"
        "Ans-2025-GS1.pdf`, page 1, header 'CS(P)-2025 Series A'), not from "
        "the garbled Markdown/OCR export: Q12 = C, Q20 = C, Q71 = B and "
        "Q73 = B. The 2026 Set-A key remains explicitly provisional, so no "
        "answer is recorded or inferred for Q9. The 2021 GS-I Mains demand "
        "on Gandhi's constructive programmes is solved as a bounded model, "
        "with its Civil Disobedience Movement portion cross-referenced "
        "rather than invented here. 'Sedition has become my religion' "
        "(2025 Q71, confirmed key B = the Dandi Salt Law breach) is "
        "explicitly out of scope for this topic's core content and is "
        "routed only as a trap; it belongs to the 1930 Dandi phase.",
        [
            (
                "Post-1919 convergence",
                "By 1920 wartime economic distress, Rowlatt-Jallianwala anger and "
                "the emerging Khilafat question converged to make an all-India "
                "mass movement politically possible for the first time.",
            ),
            (
                "Khilafat anxiety",
                "Indian Muslims feared harsh Allied treatment of the Ottoman "
                "Sultan-Caliph after the First World War and the Treaty of "
                "Sevres, feeding the Khilafat agitation.",
            ),
            (
                "Khilafat leadership",
                "Khilafat leadership included Maulana Mohammad Ali, Shaukat Ali, "
                "Maulana Azad, Hakim Ajmal Khan and Hasrat Mohani, with a "
                "Khilafat Committee already active before the November 1919 "
                "Delhi conference.",
            ),
            (
                "Delhi Khilafat Conference",
                "The All-India Khilafat Conference at Delhi in November 1919 "
                "threatened withdrawal of cooperation if Khilafat demands were "
                "rejected.",
            ),
            (
                "Gandhi's alliance logic",
                "Gandhi linked the Khilafat issue to Swaraj to build Hindu-Muslim "
                "unity and widen anti-British mobilisation beyond a narrow "
                "political class.",
            ),
            (
                "Calcutta Special Session",
                "The Calcutta Special Session of September 1920 adopted the "
                "Non-Cooperation programme.",
            ),
            (
                "Nagpur ratification and reorganisation",
                "The Nagpur Congress of December 1920 ratified Non-Cooperation "
                "and reorganised Congress with linguistic provincial committees, "
                "an AICC and a stronger Working Committee.",
            ),
            (
                "Escalation ladder",
                "The programme escalated through renunciation of titles, "
                "boycott of schools, courts and councils, economic boycott of "
                "foreign cloth, constructive work, and a final planned stage of "
                "mass civil disobedience and tax refusal.",
            ),
            (
                "Urban participants",
                "Students left institutions, lawyers suspended practice, "
                "traders boycotted foreign cloth, and women joined picketing "
                "and khadi work, widening the movement's social base.",
            ),
            (
                "National institutions",
                "The boycott phase produced durable national institutions "
                "including Jamia Millia Islamia, Kashi Vidyapith, Gujarat "
                "Vidyapith and Bihar Vidyapith.",
            ),
            (
                "Constructive programme",
                "The constructive programme of khadi, charkha, swadeshi, "
                "national education, panchayats and Hindu-Muslim unity built an "
                "alternative moral economy alongside boycott.",
            ),
            (
                "Prince of Wales boycott",
                "The 1921 visit of the Prince of Wales was met with a boycott "
                "and hartal that intensified repression and arrests across the "
                "country.",
            ),
            (
                "Eka movement",
                "The Eka, or unity, movement in the United Provinces protested "
                "rent generally fifty per cent above the recorded rent, the "
                "oppression of thekedars, and share-rents, developing its own "
                "leadership under Madari Pasi and other leaders who did not "
                "accept Congress-Khilafat non-violent discipline.",
            ),
            (
                "Eka's cross-class base and end",
                "Eka included many small zamindars alongside tenants and was "
                "suppressed by severe official repression by March 1922, "
                "marking its autonomy from Congress control.",
            ),
            (
                "Malabar Mappila rebellion",
                "The Mappila rebellion in Malabar from August 1921 grew from "
                "grievances over tenure security, renewal fees and high rents, "
                "gaining early impetus from the Malabar District Congress "
                "Conference at Manjeri in April 1920, but later acquired a "
                "communal character that damaged the Khilafat-Congress "
                "alliance.",
            ),
            (
                "Bardoli escalation plan",
                "Gandhi announced that mass civil disobedience and tax refusal "
                "would begin selectively in Bardoli taluqa of Surat district, "
                "with the rest of the country maintaining discipline so "
                "attention could concentrate there.",
            ),
            (
                "Chauri Chaura",
                "On 4 February 1922 a Congress-Khilafat procession at Chauri "
                "Chaura in Gorakhpur district clashed with police, then "
                "attacked and burned the police station, killing twenty-two "
                "policemen.",
            ),
            (
                "Withdrawal and Bardoli resolution",
                "Gandhi persuaded the Congress Working Committee to ratify "
                "withdrawal of Non-Cooperation on 12 February 1922 in the "
                "resolution known as the Bardoli resolution, named for the "
                "place where escalation had been planned.",
            ),
            (
                "Gandhi's arrest and Caliphate abolition",
                "Gandhi was arrested in March 1922 and sentenced to six years' "
                "imprisonment, and the Caliphate was abolished by Mustafa Kemal "
                "in 1924, ending the Khilafat issue.",
            ),
            (
                "Achievements, limits and consequences",
                "Non-Cooperation was the first genuinely all-India mass "
                "movement and left a reorganised Congress and durable "
                "institutions, but boycott proved reversible, Hindu-Muslim "
                "unity proved fragile after 1924, and the withdrawal opened the "
                "Swarajist-No-changer debate and a revolutionary drift among "
                "younger activists. The withdrawal itself remains a directly "
                "sourced historiographical debate: R. Palme Dutt's class-"
                "protection thesis in India Today reads it as Gandhi shielding "
                "propertied landlord-capitalist interests from a "
                "radicalising peasantry, while Bipin Chandra's own rebuttal "
                "counters that the Chauri Chaura crowd showed no anti-"
                "property intent, that agrarian unrest was already ebbing by "
                "late 1921, and that withdrawal pre-empted repression rather "
                "than protected property.",
            ),
        ],
        [
            "Khilafat was a political-religious mobilisation on the Ottoman "
            "Caliphate question, not a Hindu movement.",
            "A Khilafat Committee predates the November 1919 Delhi Conference; "
            "do not treat the Conference as the movement's origin.",
            "Non-Cooperation was adopted at Calcutta (September 1920) and "
            "ratified at Nagpur (December 1920); do not merge the two sessions.",
            "The escalation ladder's fifth stage (mass civil disobedience and "
            "tax refusal) was announced for Bardoli and never launched.",
            "Do not describe the boycott of councils, schools and courts as "
            "total; it was partial and later reversed by the Swarajists in "
            "1923.",
            "The Eka movement was autonomous of Congress control under Madari "
            "Pasi's leadership, not a Congress-directed campaign.",
            "The Malabar rebellion drew impetus from the Manjeri conference of "
            "April 1920 but later acquired a communal character; do not treat "
            "it as communal from the start or as purely nationalist "
            "throughout.",
            "This package uses 4 February 1922 as the verified date of the "
            "Chauri Chaura incident; the withdrawal followed on 12 February "
            "1922.",
            "Chauri Chaura occurred in Gorakhpur district, United Provinces, "
            "not Punjab or Bihar.",
            "The Bardoli resolution is named for the place where escalation "
            "was planned, not for a settlement reached at Bardoli in 1922.",
            "The official 2025 Prelims GS-I Series-A key identifies Madan "
            "Mohan Malaviya and Krishna Kant Malaviya as the legal defenders "
            "of the Chauri Chaura accused. Use this as the confirmed exam "
            "answer while noting that no source book held here independently "
            "corroborates the attribution.",
            "'Sedition has become my religion' belongs to the 1930 Dandi "
            "phase, not to Non-Cooperation; do not misplace this statement "
            "here. The 2025 Q71 confirmed official key is B (the Dandi "
            "Salt Law breach), verified directly from "
            "`books/prelima_question_paper_answers/Ans-2025-GS1.pdf` page 1 "
            "(Series A); this question and answer remain routed away from "
            "this topic's core content.",
            "Bipin Chandra's own India's Struggle for Independence prints "
            "the Chauri Chaura incident one day earlier than this package's "
            "verified date; that source-book figure is overridden here using "
            "official PIB/PM centenary-linked material and Sekhar "
            "Bandyopadhyay's Plassey to Partition (OCR p.305), both "
            "independently confirming 4 February 1922, so do not revert to "
            "the source book's uncorrected figure.",
            "Do not call the August 2026 Gujarat Vidyapith convocation a "
            "centenary; the institution was founded in 1920, so 2026 is its "
            "106th year, and the convocation is used only as a live "
            "Gandhi institution-building bridge, not as a dated anniversary "
            "claim.",
        ],
        [
            (
                10,
                "Why did the Khilafat issue give Gandhi a workable platform "
                "for Hindu-Muslim unity in 1920?",
                "Khilafat offered an emotionally resonant, genuinely popular "
                "anti-imperial cause among Indian Muslims, and Gandhi's link to "
                "Swaraj converted a religious grievance into shared national "
                "action, though its foundation outside Indian control made the "
                "unity structurally fragile.",
                [1, 2, 3, 4],
            ),
            (
                10,
                "Distinguish the boycott programme from the constructive "
                "programme of Non-Cooperation.",
                "The boycott programme was visible and nationwide but "
                "reversible within two years, while the constructive programme "
                "of khadi, education and unity work built durable institutions "
                "and cadre that outlasted the movement's withdrawal.",
                [7, 9, 10],
            ),
            (
                15,
                "Assess the Eka movement and the Malabar rebellion as evidence "
                "of popular initiative beyond the Congress programme.",
                "Both show local agrarian mobilisation adopting the moral "
                "vocabulary of the national movement while developing "
                "leadership and trajectories independent of Congress-Khilafat "
                "discipline, with Malabar's later communal turn qualifying any "
                "simple nationalist reading.",
                [12, 13, 14],
            ),
            (
                15,
                "Was Gandhi's withdrawal after Chauri Chaura a strategic "
                "necessity or a lost opportunity? Examine.",
                "Judged by Gandhi's own premises the withdrawal was obligatory "
                "once mass violence broke non-violent discipline; judged by "
                "momentum it was costly, though Bardoli's planned escalation "
                "remained untested rather than defeated. R. Palme Dutt's "
                "class-protection thesis reads the withdrawal as shielding "
                "propertied interests from a radicalising peasantry, but "
                "Bipin Chandra's rebuttal shows the Chauri Chaura crowd had no "
                "anti-property intent and that agrarian unrest was already "
                "ebbing, making a discipline-based reading more defensible.",
                [15, 16, 17, 18],
            ),
            (
                20,
                "Critically evaluate Non-Cooperation as both India's first "
                "mass movement and a fragile experiment in Hindu-Muslim "
                "unity.",
                "The movement mobilised an unprecedented social base and "
                "reorganised Congress permanently, but its unity rested on an "
                "issue decided abroad, and the Caliphate's 1924 abolition "
                "exposed that dependence within two years of the alliance's "
                "peak.",
                [0, 4, 6, 9, 18, 19],
            ),
            (
                20,
                "Trace the sequence from the post-1919 convergence to the "
                "1922 withdrawal and identify what the movement achieved and "
                "left unresolved.",
                "Wartime distress, Rowlatt-Jallianwala anger and Khilafat "
                "converged into Calcutta and Nagpur's decisions, escalated "
                "through a staged programme, and were withdrawn at Chauri "
                "Chaura before the final confrontation was tested, leaving "
                "durable institutions but an unresolved constitutional "
                "conflict.",
                [0, 5, 6, 7, 16, 17, 19],
            ),
        ],
        [
            (
                "2025",
                "Prelims GS-I Q12",
                "Consider four subjects with regard to the Non-Cooperation "
                "Programme (boycott of law courts and foreign cloth; "
                "observance of strict non-violence; retention of titles and "
                "honours without public use; establishment of panchayats for "
                "settling disputes) and identify how many were parts of the "
                "programme.",
                "official-key-confirmed",
                "Official Series-A key: **C**, verified directly from "
                "`books/prelima_question_paper_answers/Ans-2025-GS1.pdf` "
                "page 1 (header 'CS(P)-2025 Series A'), not from the "
                "garbled Markdown/OCR export. Use the escalation ladder to "
                "reason to the same option: boycott of law courts and "
                "foreign cloth belonged to the boycott stages, and "
                "panchayats for settling disputes belonged to the "
                "constructive programme; strict non-violence was an "
                "insisted method rather than a listed programme item in the "
                "same institutional sense, and retention of titles without "
                "public use contradicts the programme, which required "
                "surrender of titles.",
            ),
            (
                "2025",
                "Prelims GS-I Q20",
                "Assess two statements on the Non-Cooperation Movement: that "
                "Congress declared attainment of Swaraj by all legitimate and "
                "peaceful means as its objective, and that implementation was "
                "staged, moving to civil disobedience and non-payment of taxes "
                "only if Swaraj did not come within a year and government "
                "resorted to repression.",
                "official-key-confirmed",
                "Official Series-A key: **C**, verified directly from "
                "`books/prelima_question_paper_answers/Ans-2025-GS1.pdf` "
                "page 1 (header 'CS(P)-2025 Series A'), not from the "
                "garbled Markdown/OCR export. Both statements match this "
                "package's own record of the declared objective and the "
                "conditional final escalation stage, consistent with the "
                "confirmed key.",
            ),
            (
                "2025",
                "Prelims GS-I Q73",
                "Official Set-A wording (verbatim, "
                "`knowledge-export/Prelims PYQ/2025-GS1-Set A.md`, line 3119 "
                "onward): 'Who provided legal defence to the people arrested "
                "in the aftermath of Chauri Chaura incident? (a) C. R. Das "
                "(b) Madan Mohan Malaviya and Krishna Kant (c) Dr. Saifuddin "
                "Kitchlew and Khwaja Hasan Nizami (d) M. A. Jinnah.'",
                "official-key-confirmed",
                "Official Series-A key: **B** (Madan Mohan Malaviya and "
                "Krishna Kant Malaviya), verified directly from "
                "`books/prelima_question_paper_answers/Ans-2025-GS1.pdf` "
                "page 1 (header 'CS(P)-2025 Series A'), not from the "
                "garbled Markdown/OCR export whose Series A block previously "
                "appeared to break off with no key rows. No source book held "
                "in this repository otherwise records who led the legal "
                "defence of the Chauri Chaura accused, so this option is "
                "presented strictly as the confirmed official key rather "
                "than as independently corroborated historical narrative; "
                "the owning Basic Markdown records the same bounded "
                "distinction. What is otherwise verified and "
                "usable is the incident, the twenty-two policemen killed, "
                "the withdrawal decision and the Bardoli resolution.",
            ),
            (
                "2026",
                "Prelims GS-I Q9",
                "Distinguish the Eka Movement from the Bardoli Satyagraha on "
                "relation to Congress, social composition, grievance and "
                "organisation.",
                "routed-key-unavailable",
                "Eka grew out of Congress-Khilafat contact but developed its "
                "own low-caste leadership under Madari Pasi with diminishing "
                "nationalist contact, while the 1928 Bardoli Satyagraha was a "
                "tightly disciplined, Congress-organised no-tax satyagraha "
                "under Vallabhbhai Patel; grievance and organisation also "
                "differed sharply. The locally held 2026 Set-A key is "
                "explicitly provisional, so no option or answer is recorded or "
                "inferred.",
            ),
            (
                "2021",
                "GS-I Q12",
                "Official wording (verbatim, `knowledge-export/Mains PYQ/"
                "QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md`): 'Bring out the "
                "constructive programmes of Mahatma Gandhi during "
                "Non-Cooperation Movement and Civil Disobedience Movement. "
                "(Answer in 250 words)'.",
                "bounded-model",
                "For the Non-Cooperation Movement, cover khadi, charkha, "
                "swadeshi, national schools (Jamia Millia Islamia, Kashi "
                "Vidyapith, Gujarat Vidyapith, Bihar Vidyapith), panchayats "
                "for dispute settlement, Hindu-Muslim unity and temperance; "
                "the Civil Disobedience Movement's constructive programme "
                "belongs analytically to the later 1930s topic and should be "
                "cross-referenced there rather than invented in this "
                "package.",
            ),
        ],
        [
            "Khilafat Committee",
            "Maulana Mohammad Ali",
            "Shaukat Ali",
            "Maulana Azad",
            "Hakim Ajmal Khan",
            "Calcutta",
            "Nagpur",
            "Jamia Millia Islamia",
            "Kashi Vidyapith",
            "Gujarat Vidyapith",
            "Bihar Vidyapith",
            "Prince of Wales",
            "Madari Pasi",
            "thekedars",
            "Manjeri",
            "Bardoli",
            "Chauri Chaura",
            "Bardoli resolution",
            "Mustafa Kemal",
            "twenty-two",
        ],
    ),
    base.topic(
        21,
        "Swarajists, Constructive Work & Revolutionaries of the 1920s "
        "(HSRA, Bhagat Singh)",
        "21_Swarajists-and-Revolutionaries-1920s.md",
        "21_Swarajists-and-Revolutionaries-1920s.md",
        "21_Swarajists-Constructive-Work-Revolutionaries-1920s_Complete-Topic-Package.md",
        [
            "basic/20_Non-Cooperation-and-Khilafat-Movement.md",
            "basic/22_Simon-Nehru-Report-CDM-and-RTC.md",
            "basic/23_Left-Peasant-Workers-and-States-Peoples-Movements.md",
            "advanced/20_Non-Cooperation-and-Khilafat-Movement.md",
        ],
        [
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2154621&reg=3&lang=2",
            "https://ddnews.gov.in/en/delhi-cm-rekha-gupta-unveils-bhagat-"
            "singh-statue-inaugurates-restored-historic-courtroom-on-"
            "shaheed-diwas/",
        ],
        "The Prime Minister's 9 August 2025 centenary tribute to the Kakori "
        "Train Action (PIB, PRID 2154621) is retained only as a public-memory "
        "bridge for the HRA's Kakori case. It does not supply new dates, "
        "casualty figures or sentencing details beyond what this package "
        "already verifies, and it does not extend to the later HSRA, Assembly "
        "Bomb or Lahore Conspiracy Case sequence. A second, separate bridge: "
        "on Shaheed Diwas, 23 March 2026 (the 95th anniversary of the 1931 "
        "executions), Delhi Chief Minister Rekha Gupta unveiled a Bhagat "
        "Singh statue and inaugurated a restored historic courtroom at the "
        "Registrar Cooperative Society office on Parliament Street, New "
        "Delhi. This courtroom is the site where Bhagat Singh and "
        "Batukeshwar Dutt were tried specifically for the Central Assembly "
        "bomb action; this package links the site only to the Assembly Bomb "
        "Case, not to the separate Lahore Conspiracy Case tribunal. Business "
        "Today's coverage was directly fetched for this event; the PIB press "
        "release page was inaccessible during this authoring pass, so "
        "ddnews.gov.in is retained as the directly verified corroborating "
        "link.",
        "OCR-based verification for this pass relies on the repository's "
        "already-authored Basic and Advanced Markdown owners for Swarajists "
        "and revolutionaries, themselves grounded in Bipin Chandra's Modern "
        "India (Chapter XV) and India's Struggle for Independence. The "
        "Naujawan Bharat Sabha, the Lahore Conspiracy Case tribunal timeline "
        "and Jatin Das's hunger strike are not covered in these local owners "
        "and are added here from independently verified public-record "
        "sources, clearly labelled as such rather than presented as "
        "repository-book facts. HRA's Kanpur founding location, the HSRA's "
        "Ferozeshah Kotla renaming site, and Jatin Das's fast-length variance "
        "(63 versus 64 days) are likewise independently verified additions, "
        "not repository-book facts.",
        "No routed Prelims objective demand for this topic was found in the "
        "repository's PYQ routing ledgers at the time of authoring, other "
        "than one thematically adjacent 2018 GS-I demand (Q79, Series C, "
        "`knowledge-export/Prelims PYQ/QP-CSP-18-GS-I-C.pdf.md`) on the "
        "renaming of a body to 'Swarajya Sabha' in 1920; no answer-key file "
        "for that series is held locally, so no option or letter is recorded "
        "or inferred for it. The 2020 "
        "GS-I Mains demand on the ideological strands of the national "
        "movement since the 1920s is solved as a bounded, cross-cutting "
        "model shared with the Left/Peasant topic.",
        [
            (
                "1922 strategic vacuum",
                "Gandhi's withdrawal of Non-Cooperation in February 1922 left "
                "Congress without an agreed method and opened a debate over "
                "the next phase of the struggle.",
            ),
            (
                "No-changer position",
                "No-changers argued for continued constructive work such as "
                "khadi, national education, Hindu-Muslim unity and removal of "
                "untouchability as preparation for future struggle.",
            ),
            (
                "Pro-changer position and Swaraj Party founding",
                "Pro-changers led by C.R. Das and Motilal Nehru pressed their "
                "council-entry proposal at the Congress session at Gaya in "
                "December 1922, where it was rejected, prompting them to "
                "found the Swaraj Party. This package retains 1 January 1923 "
                "as the Party's working founding date, while noting that "
                "some compact sources instead date the founding to December "
                "1922 itself; this source variance is flagged rather than "
                "silently resolved.",
            ),
            (
                "Council-entry logic",
                "Swarajists argued that entering councils would prevent "
                "political passivity and publicly expose the limits of "
                "dyarchy rather than legitimise it.",
            ),
            (
                "Swarajist 1923 performance",
                "The Swarajists performed strongly in the 1923 elections and "
                "used their position to expose the structural weaknesses of "
                "dyarchy and the budgetary settlement.",
            ),
            (
                "Swarajist decline",
                "C.R. Das's death in 1925 and the gradual erosion of "
                "obstruction as ministries and patronage drew some members in "
                "reduced Swarajist momentum through the later 1920s.",
            ),
            (
                "Continuity to 1930",
                "Both No-changer and Swarajist wings remained within Congress "
                "and reassembled their methods and personnel for the 1930 "
                "Civil Disobedience Movement.",
            ),
            (
                "HRA formation",
                "The Hindustan Republican Association was founded at Kanpur "
                "in October 1924 by leaders including Sachindranath Sanyal, "
                "Ram Prasad Bismil and Jogesh Chatterjee with a republican "
                "revolutionary programme aimed at armed overthrow of "
                "colonial rule.",
            ),
            (
                "Kakori conspiracy",
                "The Kakori train action of 1925 aimed to raise funds for "
                "revolutionary activity, and Bismil, Ashfaqulla Khan, Roshan "
                "Singh and Rajendra Lahiri were executed in 1927 after the "
                "case.",
            ),
            (
                "Naujawan Bharat Sabha",
                "The Naujawan Bharat Sabha was founded in March 1926 in "
                "Lahore with Bhagat Singh as a leading organiser, mobilising "
                "youth toward socialist and anti-imperialist politics as an "
                "open, legal public front, organisationally distinct from "
                "the underground HRA/HSRA network it fed ahead of the "
                "HSRA's formation.",
            ),
            (
                "HRA to HSRA",
                "The HRA was reorganised as the Hindustan Socialist "
                "Republican Association at Ferozeshah Kotla, Delhi, on 9-10 "
                "September 1928, adding an explicit socialist and "
                "anti-imperialist orientation under leaders including "
                "Bhagat Singh, Chandrashekhar Azad, Sukhdev and Bhagwati "
                "Charan Vohra. HRA and HSRA are one continuous "
                "organisational lineage under a new name and programme, not "
                "two rival bodies; 'Association' and 'Army' are variant "
                "source labels for the same body, not separate names.",
            ),
            (
                "Lala Lajpat Rai and Saunders",
                "Lala Lajpat Rai died from injuries sustained during a "
                "lathi-charge on an anti-Simon Commission protest, and HSRA "
                "revolutionaries killed the police officer Saunders in "
                "December 1928 in retaliation.",
            ),
            (
                "Assembly bomb",
                "On 8 April 1929 Bhagat Singh and Batukeshwar Dutt threw "
                "bombs in the Central Legislative Assembly, deliberately "
                "designed to be non-lethal and symbolic, intended to make the "
                "deaf hear rather than to kill. This bombing was tried as a "
                "separate Sessions Court proceeding, the Assembly Bomb Case, "
                "in which Bhagat Singh and Batukeshwar Dutt received life "
                "imprisonment.",
            ),
            (
                "Lahore Conspiracy Case",
                "Evidence from the Assembly Bomb Case and the Saunders "
                "killing together fed a separate, later proceeding, the "
                "Lahore Conspiracy Case, whose Special Tribunal sentenced "
                "Bhagat Singh, Sukhdev and Rajguru to death in October 1930; "
                "the Assembly Bomb Case and the Lahore Conspiracy Case are "
                "two distinct legal proceedings with different courts and "
                "sentences, not one undifferentiated trial.",
            ),
            (
                "Jatin Das and the jail hunger strike",
                "Jatin Das died on 13 September 1929 after a sustained "
                "hunger strike in Lahore Central Jail demanding better "
                "treatment for political prisoners during the Lahore "
                "Conspiracy Case trial. The fast's length is reported as 63 "
                "days in most accounts and as 64 days in some others; this "
                "package retains both durations as an open source variance "
                "rather than asserting one as definitively correct.",
            ),
            (
                "Bhagat Singh as political thinker",
                "Bhagat Singh's later writings show a rationalist, atheist "
                "and socialist political position that framed the enemy as "
                "both imperialism and class exploitation, not only a "
                "personal call to martyrdom.",
            ),
            (
                "Execution",
                "Bhagat Singh, Sukhdev and Rajguru were executed on 23 March "
                "1931 after the Lahore Conspiracy Case verdict.",
            ),
            (
                "Chittagong Armoury Raid",
                "The Chittagong Armoury Raid of 1930 in Bengal was led by "
                "Surya Sen and included women revolutionaries, representing "
                "an attempted seizure of a locality rather than an "
                "individual action; the Chittagong stream was organisationally "
                "separate from the Punjab-United Provinces HRA/HSRA network, "
                "sharing revolutionary aims but not a common command "
                "structure.",
            ),
            (
                "HRA-HSRA distinction",
                "Kakori belongs to the HRA phase associated with Bismil and "
                "Ashfaqulla Khan, while the Assembly bomb, Saunders and the "
                "Lahore Conspiracy Case belong to the later HSRA phase "
                "associated with Bhagat Singh; the two must not be merged.",
            ),
            (
                "Four streams of the 1920s",
                "The 1920s produced four parallel streams - Swarajist council "
                "politics, No-changer constructive work, HRA-HSRA "
                "revolutionary action and an emerging left/labour current - "
                "whose combined legacy shaped the movement that resumed in "
                "1930.",
            ),
        ],
        [
            "Swarajists remained within the Congress fold; council-entry was "
            "a tactic of obstruction, not accommodation with colonial rule.",
            "No-changers and Pro-changers were tactical streams, not a "
            "permanent organisational split.",
            "Kakori (1925) belongs to the HRA phase and is associated with "
            "Bismil and Ashfaqulla Khan, not with Bhagat Singh.",
            "HSRA (1928) is a socialist reorganisation of HRA, not merely a "
            "renamed identical body.",
            "The Assembly bomb of 8 April 1929 was deliberately non-lethal "
            "and symbolic; do not describe it as an attempt at mass killing.",
            "Naujawan Bharat Sabha (March 1926) precedes and feeds into the "
            "1928 HSRA reorganisation; do not treat the two as the same "
            "organisation founded on the same date.",
            "Saunders was killed in December 1928 to avenge Lala Lajpat "
            "Rai's injuries from a lathi-charge, not as part of the Kakori "
            "case.",
            "Jatin Das died on 13 September 1929 after a hunger strike in "
            "Lahore Central Jail during the Lahore Conspiracy Case trial; do "
            "not confuse this case with the Assembly Bomb case as a single "
            "undifferentiated proceeding.",
            "The Lahore Conspiracy Case Special Tribunal delivered its "
            "verdict in October 1930; the executions of Bhagat Singh, "
            "Sukhdev and Rajguru followed on 23 March 1931.",
            "Chittagong Armoury Raid (1930) is in Bengal under Surya Sen, "
            "not in Punjab.",
            "Do not quote Bhagat Singh's writings verbatim; describe his "
            "rationalist, atheist and socialist position analytically.",
            "Present Bhagat Singh's legacy through his political ideas as "
            "well as his martyrdom; avoid a purely sentimental account.",
            "'Swarajya Sabha' (the All-India Home Rule League renamed in "
            "1920) is a distinct body from the 'Swaraj Party' founded by "
            "C.R. Das and Motilal Nehru in 1922-23; do not conflate the two "
            "similarly named entities.",
            "The Swaraj Party's council-entry proposal was rejected at "
            "Congress's Gaya session in December 1922; whether the Party's "
            "founding date is best given as December 1922 or 1 January 1923 "
            "is a source variance this package flags rather than resolves.",
            "HRA was founded at Kanpur in October 1924 and renamed HSRA at "
            "Ferozeshah Kotla, Delhi, on 9-10 September 1928; the two names "
            "mark one continuous organisational lineage, not rival bodies.",
            "The Delhi restoration of the Parliament Street courtroom "
            "(Shaheed Diwas 2026) marks the Assembly Bomb Case trial site "
            "only; do not extend this current-affairs bridge to the "
            "separate Lahore Conspiracy Case proceeding.",
        ],
        [
            (
                10,
                "Why was the Swarajist-No-changer split a tactical division "
                "rather than a break in the national movement?",
                "Both No-changers and Pro-changers accepted Swaraj as the "
                "goal and remained within Congress; they differed only over "
                "whether constructive work or council-entry was the better "
                "method after 1922.",
                [0, 1, 2, 3],
            ),
            (
                10,
                "Distinguish the HRA and HSRA phases of revolutionary "
                "nationalism in the 1920s.",
                "HRA (1924) pursued a republican overthrow associated with "
                "Kakori, Sanyal and Bismil, while HSRA (1928) added an "
                "explicit socialist orientation under Bhagat Singh and Azad; "
                "the two phases and their cases must not be merged.",
                [7, 8, 10, 17],
            ),
            (
                15,
                "Assess the Swarajist experiment in the legislatures between "
                "1923 and the later 1920s.",
                "Council-entry exposed dyarchy's structural weakness through "
                "obstruction and demonstration rather than legislative "
                "victory, but C.R. Das's 1925 death and later patronage "
                "politics eroded its momentum.",
                [2, 3, 4, 5],
            ),
            (
                15,
                "Discuss the ideological evolution from HRA republicanism to "
                "HSRA socialism and its significance.",
                "The 1928 reorganisation, prepared partly through the "
                "Naujawan Bharat Sabha's youth mobilisation, added an "
                "explicit anti-imperialist and anti-capitalist theory, making "
                "socialism a mainstream vocabulary of Indian revolutionary "
                "politics.",
                [7, 9, 10, 12, 15],
            ),
            (
                20,
                "Evaluate Bhagat Singh's political significance as a "
                "rationalist and socialist thinker rather than only a "
                "martyr.",
                "His prison writings and the Assembly bomb's deliberately "
                "symbolic, non-lethal design show a reasoned political "
                "strategy targeting both imperialism and class exploitation, "
                "which the Lahore Conspiracy Case, the jail hunger strike and "
                "his 1931 execution should not reduce to sentiment alone.",
                [10, 12, 13, 14, 15, 16],
            ),
            (
                20,
                "Was the 1920s a lull in the national movement? Examine "
                "using the Swarajist, constructive, revolutionary and Bengal "
                "streams.",
                "Council obstruction, rural constructive work, HRA-HSRA "
                "revolutionary politics and the 1930 Chittagong Raid together "
                "show the decade built the organisation, arguments and cadre "
                "the 1930 movement required, rather than marking an empty "
                "gap.",
                [1, 4, 6, 17, 19],
            ),
        ],
        [
            (
                "2020",
                "GS-I Q13",
                "Official wording (verbatim, `knowledge-export/Mains PYQ/"
                "Gen_St_P1.pdf.md`): 'Since the decade of the 1920s, the "
                "national movement acquired various ideological strands and "
                "thereby expanded its social base. Discuss. (Answer in 250 "
                "words)'.",
                "bounded-model",
                "Organise the answer around the Swarajist constitutional "
                "strand, the Gandhian No-changer/constructive strand, the "
                "HRA-HSRA revolutionary-socialist strand, and the emerging "
                "left/labour strand; each widened the movement's social base "
                "differently, and the shared institutional home was Congress "
                "even where methods diverged sharply.",
            ),
            (
                "2018",
                "Prelims GS-I Q79 (Series C)",
                "Official wording (verbatim, `knowledge-export/Prelims PYQ/"
                "QP-CSP-18-GS-I-C.pdf.md`): 'In 1920, which of the following "
                "changed its name to \"Swarajya Sabha\"? (a) All India Home "
                "Rule League (b) Hindu Mahasabha (c) South Indian Liberal "
                "Federation (d) The Servants of India Society.'",
                "open-evidence-gap-key-unavailable",
                "No paired official answer-key file for this 2018 Series-C "
                "paper is held locally, so no option or letter is selected "
                "or inferred here. The question's exam value for this topic "
                "is the trap it sets: 'Swarajya Sabha' is the 1920 renaming "
                "of a pre-existing Home Rule-era body, and must not be "
                "confused with the unrelated 'Swaraj Party' that C.R. Das "
                "and Motilal Nehru founded in 1922-23; this package keeps "
                "the two distinct rather than merging them.",
            ),
        ],
        [
            "Swaraj Party",
            "C.R. Das",
            "Motilal Nehru",
            "No-changers",
            "Gaya",
            "Hindustan Republican Association",
            "Kanpur",
            "Sachindranath Sanyal",
            "Ram Prasad Bismil",
            "Kakori",
            "Naujawan Bharat Sabha",
            "Hindustan Socialist Republican Association",
            "Ferozeshah Kotla",
            "Chandrashekhar Azad",
            "Saunders",
            "Lala Lajpat Rai",
            "Central Legislative Assembly",
            "Lahore Conspiracy Case",
            "Jatin Das",
            "Chittagong",
            "Surya Sen",
            "Swarajya Sabha",
        ],
    ),
]


SESSION_PLANS: dict[str, list[tuple[str, str, list[str], str, str]]] = {
    "modern-indian-history-20": [
        (
            "Setting: wartime distress, Rowlatt-Jallianwala anger and "
            "Khilafat emergence",
            "By 1920 several separate grievances converged into one "
            "political mood: wartime economic distress and the "
            "reform-repression contradiction from Rowlatt and Jallianwala "
            "Bagh, and the emerging Khilafat question over the Ottoman "
            "Caliph's post-war treatment, together made a mass anti-British "
            "movement politically possible for the first time.",
            [
                "Wartime price rises, recruitment pressure and continuing "
                "coercive powers had already discredited the promise of "
                "gradual reform.",
                "Rowlatt's exceptional powers and the Jallianwala Bagh "
                "massacre of April 1919 had destroyed confidence in imperial "
                "justice.",
                "Indian Muslims feared harsh Allied treatment of the Ottoman "
                "Sultan-Caliph after the First World War and the Treaty of "
                "Sevres, feeding the Khilafat agitation.",
                "A Khilafat Committee was already active before the "
                "securely dated All-India Khilafat Conference at Delhi in "
                "November 1919.",
            ],
            "Do not read Non-Cooperation as caused by a single event; it "
            "drew on wartime distress, Rowlatt-Jallianwala anger and the "
            "Khilafat question together.",
            "Open a 15/20-mark answer on Non-Cooperation with this "
            "three-strand convergence before naming the Calcutta and Nagpur "
            "decisions.",
        ),
        (
            "Khilafat aims, leadership and the Delhi Conference",
            "The Khilafat movement was a political mobilisation on a "
            "religious question: it sought to defend the Ottoman Caliph's "
            "temporal and religious authority, and its organised leadership "
            "pre-dated and then used the November 1919 Delhi Conference to "
            "threaten withdrawal of cooperation.",
            [
                "Khilafat leadership included Maulana Mohammad Ali and "
                "Shaukat Ali (the Ali Brothers), Maulana Azad, Hakim Ajmal "
                "Khan and Hasrat Mohani.",
                "The All-India Khilafat Conference at Delhi in November "
                "1919 threatened withdrawal of cooperation if Khilafat "
                "demands were rejected.",
                "A Khilafat Committee already existed before this "
                "Conference; the Conference should not be mistaken for the "
                "movement's founding moment.",
                "The issue was political-religious, not a Hindu religious "
                "campaign, and not confined to a single region.",
            ],
            "Do not describe Khilafat as a Hindu movement or as purely "
            "religious; it was a Muslim political mobilisation on an "
            "international religious-political question.",
            "Use named leaders and the Delhi Conference to answer any "
            "demand asking for Khilafat's aims, leadership or organisation.",
        ),
        (
            "Gandhi's alliance logic for Khilafat-Congress unity",
            "Gandhi linked the Khilafat grievance to the domestic demand "
            "for Swaraj because it offered an emotionally resonant, "
            "genuinely popular anti-imperial cause among Indian Muslims, and "
            "joining it to Congress's programme promised the deepest "
            "Hindu-Muslim political cooperation of the colonial period.",
            [
                "Gandhi treated Khilafat as a moral opportunity to build "
                "unity and widen mobilisation beyond the educated political "
                "class.",
                "The alliance was tactical and principled at once: Gandhi "
                "believed supporting a genuine Muslim grievance was owed "
                "regardless of its political usefulness.",
                "The alliance rested on an issue decided by Turkish and "
                "international politics, not by Indian nationalists.",
                "This structural dependence made the unity powerful in "
                "1920-21 but vulnerable to events outside India's control.",
            ],
            "Do not treat Khilafat-NCM unity as guaranteed or permanent; "
            "assess both its strength and its structural fragility "
            "together.",
            "This session supplies the 'basis of alliance' step in any "
            "Khilafat-unity evaluation answer.",
        ),
        (
            "Calcutta Special Session: adopting Non-Cooperation",
            "The Calcutta Special Session of September 1920 formally "
            "adopted the Non-Cooperation programme, converting the "
            "convergence of Khilafat, Rowlatt-Jallianwala anger and wartime "
            "distress into an organised national campaign of withdrawal of "
            "cooperation from the colonial state.",
            [
                "The Session took place in September 1920, ahead of the "
                "regular annual Congress session.",
                "Adoption at Calcutta made Non-Cooperation the Congress's "
                "own programme rather than only Gandhi's personal campaign.",
                "The decision required later ratification, which came at "
                "Nagpur in December 1920.",
                "Adoption at a Special Session reflected the urgency created "
                "by the Khilafat and Punjab grievances.",
            ],
            "Calcutta adopted the programme; do not confuse this with "
            "Nagpur's later ratification and reorganisation.",
            "State Calcutta (September 1920) and Nagpur (December 1920) as "
            "two distinct, dated steps in any chronology answer.",
        ),
        (
            "Nagpur Congress: ratification and mass reorganisation",
            "The Nagpur Congress of December 1920 not only ratified the "
            "Non-Cooperation programme but also reorganised the Congress "
            "itself into a mass-political organisation with linguistic "
            "provincial committees, an All India Congress Committee and a "
            "stronger Working Committee, supported by a low membership fee.",
            [
                "Linguistic provincial congress committees aligned the "
                "organisation with the units in which Indians actually spoke "
                "and organised.",
                "The All India Congress Committee (AICC) and a stronger "
                "Working Committee gave Congress continuous, not just "
                "annual, leadership capacity.",
                "A low membership fee opened Congress membership beyond "
                "professional and propertied classes.",
                "This reorganisation, not only the boycott, is the "
                "movement's most durable institutional legacy.",
            ],
            "Do not describe Nagpur as passing only a political resolution; "
            "its organisational reforms are equally examinable.",
            "Use Nagpur's reorganisation to answer 'organisational "
            "transformation' or 'most durable achievement' demands.",
        ),
        (
            "The programme's escalation ladder",
            "Non-Cooperation was designed as a graded escalation ladder, "
            "moving from symbolic renunciation through institutional boycott "
            "and economic boycott to a constructive programme, with a final "
            "planned stage of mass civil disobedience and tax refusal that "
            "was never reached.",
            [
                "Stage 1 was the surrender of titles and honorary offices.",
                "Stage 2 was boycott of schools and colleges, law courts, "
                "legislative councils and official functions.",
                "Stage 3 was economic boycott of foreign cloth and goods, "
                "and picketing of liquor shops.",
                "Stage 4 was the constructive programme; Stage 5, mass civil "
                "disobedience and tax refusal, was announced for Bardoli but "
                "never launched.",
            ],
            "Present the five stages as a ladder in order; do not present "
            "the movement as a single undifferentiated boycott.",
            "Use the exact five-stage ladder to answer 'components and "
            "stages of Non-Cooperation' demands, including the 2025 Prelims "
            "routed demand on its components.",
        ),
        (
            "Urban mobilisation: students, lawyers, traders and women",
            "Non-Cooperation's boycott stage drew in social groups well "
            "beyond the educated political elite that had led earlier "
            "constitutional agitation: students left schools and colleges, "
            "lawyers suspended court practice, traders boycotted foreign "
            "cloth, and women joined picketing and khadi work.",
            [
                "Student withdrawal from government schools and colleges "
                "gave the boycott its most visible early symbol.",
                "Lawyers who suspended practice included prominent Congress "
                "leaders as well as local practitioners.",
                "Traders' boycott of foreign cloth linked the economic and "
                "political dimensions of the campaign.",
                "Women's participation in picketing and khadi work widened "
                "the movement's social base beyond earlier agitations.",
            ],
            "Do not describe Non-Cooperation as only an elite council "
            "boycott; its social base was genuinely broad, even if "
            "participation was uneven.",
            "Name these four groups explicitly when a question asks how "
            "Non-Cooperation became a mass movement.",
        ),
        (
            "Constructive programme and national institutions",
            "Alongside boycott, Gandhi's constructive programme of khadi, "
            "charkha, swadeshi, national education, panchayats and "
            "Hindu-Muslim unity built durable institutions and a rural cadre "
            "that outlasted the boycott's reversal.",
            [
                "National educational institutions founded in this phase "
                "include Jamia Millia Islamia, Kashi Vidyapith, Gujarat "
                "Vidyapith and Bihar Vidyapith.",
                "Khadi and charkha work built an alternative economic "
                "practice around swadeshi.",
                "Panchayats for settling disputes offered an alternative to "
                "colonial courts.",
                "This programme proved more durable than the boycott, which "
                "the Swarajists formally reversed in 1923.",
            ],
            "Do not quantify the constructive programme's reach with "
            "unverified numbers; argue from the named institutions and "
            "durability contrast instead.",
            "Use the boycott-versus-constructive-programme durability "
            "contrast to answer 'which mattered more' demands.",
        ),
        (
            "Prince of Wales boycott and repression",
            "The 1921 visit of the Prince of Wales was met with a hartal "
            "and boycott that intensified official repression, testing how "
            "far the movement could escalate popular participation while "
            "Gandhi still withheld authorisation for mass civil "
            "disobedience.",
            [
                "The Prince of Wales's 1921 visit became a focal point for "
                "coordinated boycott and hartal.",
                "Government repression, arrests and prosecutions intensified "
                "through 1921 in response.",
                "Rising repression widened sympathy and participation "
                "without yet reaching the final escalation stage.",
                "Gandhi continued to hold back mass civil disobedience "
                "despite mounting pressure to escalate.",
            ],
            "Do not treat the Prince of Wales boycott as the movement's "
            "final stage; it remained within the boycott and repression "
            "dynamic short of Bardoli's planned escalation.",
            "Use this episode to show how repression and popular energy "
            "interacted without prematurely authorising mass civil "
            "disobedience.",
        ),
        (
            "The Eka movement in the United Provinces",
            "The Eka, or unity, movement in the United Provinces shows "
            "peasants adopting the moral vocabulary of the national "
            "movement while organising around their own agrarian grievances "
            "and developing leadership independent of Congress and Khilafat "
            "discipline.",
            [
                "Grievances included rent generally fifty per cent above "
                "the recorded rent, the oppression of thekedars to whom "
                "rent-collection was farmed out, and share-rents.",
                "Ganges-oath meetings bound peasants to pay only the "
                "recorded rent, on time, and to refuse forced labour and "
                "ejection.",
                "Madari Pasi and other low-caste leaders led the movement "
                "and did not accept Congress-Khilafat non-violent "
                "discipline, so its contact with nationalist leadership "
                "diminished.",
                "Unlike the earlier Kisan Sabha, which rested mainly on "
                "tenants, Eka included many small zamindars disenchanted "
                "with the revenue demand.",
            ],
            "Do not describe Eka as a Congress-directed movement; its "
            "defining feature is autonomy from Congress control, ended by "
            "severe repression by March 1922.",
            "Use Eka as the strongest single evidence unit for the "
            "'popular initiative beyond the Congress programme' demand.",
        ),
        (
            "The Malabar Mappila rebellion and its communal turn",
            "The Mappila rebellion in Malabar, beginning in August 1921, "
            "grew from agrarian grievances over tenure and rents and gained "
            "early impetus from the Malabar District Congress Conference at "
            "Manjeri in April 1920, but it progressively acquired a communal "
            "character that damaged the wider Khilafat-Congress alliance.",
            [
                "Grievances concerned lack of security of tenure, renewal "
                "fees, high rents and other landlord exactions.",
                "The Malabar District Congress Conference at Manjeri in "
                "April 1920 gave the movement early nationalist impetus.",
                "As the rebellion progressed it acquired a communal "
                "character, straining the Hindu-Muslim unity built around "
                "Khilafat.",
                "This trajectory shows local mobilisation escaping the "
                "national frame and being reshaped by local social "
                "divisions.",
            ],
            "Do not present Malabar as communal from its origin or as "
            "purely nationalist throughout; trace the shift honestly.",
            "Use Malabar's trajectory to qualify any answer that treats "
            "Khilafat-era Hindu-Muslim unity as uniformly stable.",
        ),
        (
            "Bardoli and the planned mass civil disobedience",
            "Gandhi announced that the final escalation stage, mass civil "
            "disobedience and tax refusal, would begin selectively in "
            "Bardoli taluqa of Surat district, with the rest of the country "
            "maintaining discipline so attention could concentrate there, "
            "converting Bardoli into the symbolic threshold of the whole "
            "movement.",
            [
                "The plan concentrated escalation in one taluqa rather than "
                "launching it nationwide at once.",
                "Bardoli was chosen precisely because it could be closely "
                "organised and disciplined.",
                "The plan was never launched because Chauri Chaura "
                "intervened before the escalation date.",
                "Bardoli itself waited until 1928 for its own no-tax "
                "satyagraha under Vallabhbhai Patel, a distinct later "
                "campaign.",
            ],
            "Do not confuse the 1922 Bardoli escalation plan with the 1928 "
            "Bardoli Satyagraha; they are six years and one organisational "
            "logic apart.",
            "Use the Bardoli plan to explain exactly why the escalation "
            "ladder's fifth stage remained untested.",
        ),
        (
            "Chauri Chaura and the withdrawal",
            "On 4 February 1922 a Congress-Khilafat procession at Chauri "
            "Chaura in Gorakhpur district clashed with police and then "
            "attacked and burned the police station, killing twenty-two "
            "policemen; Gandhi responded by persuading the Congress Working "
            "Committee to ratify withdrawal of Non-Cooperation on 12 "
            "February 1922 in what became known as the Bardoli resolution.",
            [
                "The violence at Chauri Chaura directly contradicted the "
                "movement's foundational commitment to non-violent "
                "discipline.",
                "Gandhi withdrew the movement because of this violence, not "
                "because the movement itself was weak.",
                "The withdrawal resolution is named the Bardoli resolution "
                "because it was passed where mass civil disobedience was to "
                "have begun.",
                "Gandhi was arrested in March 1922 and sentenced to six "
                "years' imprisonment.",
            ],
            "This package uses 4 February 1922 as the verified date of "
            "Chauri Chaura, consistent with independently checked public "
            "records; treat 12 February 1922 as the separate withdrawal "
            "date.",
            "Use Gandhi's own reasoning plus the critics' case to answer "
            "'necessity or lost opportunity' demands on the withdrawal.",
        ),
        (
            "Achievements and limits of Non-Cooperation",
            "Non-Cooperation was India's first genuinely all-India mass "
            "movement and left a reorganised Congress and durable "
            "constructive institutions, but its boycott programme proved "
            "reversible and it never reached the fifth, most confrontational "
            "stage of the escalation ladder.",
            [
                "Achievement: unprecedented participation of students, "
                "lawyers, traders, peasants and women in one national "
                "campaign.",
                "Achievement: Nagpur's reorganisation and the constructive "
                "programme's institutions survived the movement's "
                "withdrawal.",
                "Limit: the Swarajists formally reversed the council "
                "boycott in 1923, showing how reversible that stage was.",
                "Limit: the movement was withdrawn precisely at the point "
                "where it would have moved from symbolic to fiscal "
                "confrontation.",
            ],
            "Give a graded verdict; do not call the movement either a "
            "simple failure or a simple success.",
            "Use the achievement/limit pairing to structure any 'evaluate "
            "Non-Cooperation' 15- or 20-mark answer.",
        ),
        (
            "Consequences: fragile unity and the bridge to the 1920s",
            "Non-Cooperation's withdrawal opened a strategic debate that "
            "split Congress between Swarajists and No-changers, pushed some "
            "younger activists toward revolutionary politics, and coincided "
            "with the slow unravelling of Khilafat-based Hindu-Muslim unity, "
            "completed when the Caliphate was abolished in 1924.",
            [
                "The withdrawal debate produced the Swarajist and "
                "No-changer positions within Congress, covered in the next "
                "topic.",
                "Some younger activists, disillusioned with the withdrawal, "
                "drifted toward revolutionary and later socialist politics.",
                "The Khilafat alliance's foundation outside Indian control "
                "was exposed when Mustafa Kemal abolished the Caliphate in "
                "1924.",
                "These threads carry directly into the Swarajist, "
                "constructive and revolutionary streams of the 1920s.",
            ],
            "Do not make Chauri Chaura the single cause of the 1920s "
            "political fragmentation; treat it as one trigger among "
            "several.",
            "Use this session as the explicit bridge sentence connecting "
            "Non-Cooperation's end to the next topic's Swarajist and "
            "revolutionary streams.",
        ),
    ],
    "modern-indian-history-21": [
        (
            "The 1922 strategic vacuum and the No-changer/Pro-changer "
            "debate",
            "Gandhi's February 1922 withdrawal of Non-Cooperation left "
            "Congress without an agreed method for continuing the struggle, "
            "opening a debate between No-changers, who wanted to continue "
            "constructive work, and Pro-changers, who wanted to enter the "
            "legislatures.",
            [
                "The withdrawal removed the movement's central activity "
                "without resolving how nationalist energy should now be "
                "organised.",
                "No-changers argued for continued constructive work: "
                "khadi, national education, Hindu-Muslim unity and removal "
                "of untouchability.",
                "Pro-changers, led by C.R. Das and Motilal Nehru, argued "
                "for entering legislative councils to obstruct government "
                "from within.",
                "Both positions remained within Congress; the debate was "
                "over method, not over the goal of Swaraj.",
            ],
            "Do not present the 1922-23 debate as a break with "
            "nationalism; both sides accepted the same ultimate objective.",
            "Open any 'was the split anti-national?' answer by stating "
            "that both wings stayed inside Congress.",
        ),
        (
            "No-changers and constructive work after withdrawal",
            "No-changers continued the Gandhian constructive programme "
            "through the mid-1920s, treating khadi, national schools, "
            "Hindu-Muslim unity and anti-untouchability work as preparation "
            "for a future mass struggle rather than passivity.",
            [
                "Constructive work kept a cadre of full-time workers in "
                "continuous contact with rural India between national "
                "campaigns.",
                "Khadi, charkha and swadeshi work continued the economic "
                "dimension of the earlier boycott's constructive stage.",
                "Anti-untouchability and Hindu-Muslim unity work addressed "
                "social reform alongside political preparation.",
                "This continuity supplied the social base the 1930 Civil "
                "Disobedience Movement later used.",
            ],
            "Do not call constructive work politically passive; assess it "
            "as preparation, while conceding it did not directly confront "
            "colonial authority.",
            "Use No-changer continuity to answer 'was the 1920s a lull?' "
            "demands.",
        ),
        (
            "Swaraj Party formation and council-entry logic",
            "C.R. Das and Motilal Nehru pressed a council-entry proposal at "
            "Congress's Gaya session in December 1922, and after its "
            "rejection there founded the Swaraj Party on the argument that "
            "entering the legislative councils and obstructing government "
            "from within would prevent political passivity and publicly "
            "expose the emptiness of dyarchy rather than legitimise "
            "colonial rule.",
            [
                "The Swaraj Party's declared method was council-entry "
                "followed by obstruction, not cooperation.",
                "The logic answered critics who feared council-entry meant "
                "accepting the 1919 reforms.",
                "C.R. Das and Motilal Nehru led the new party while "
                "remaining within the wider Congress fold.",
                "This package uses 1 January 1923 as the Party's working "
                "founding date, though the proposal's Gaya rejection in "
                "December 1922 leads some compact sources to date the "
                "founding itself to December 1922 - a flagged source "
                "variance, not a resolved fact.",
            ],
            "Council-entry was a tactic of obstruction; do not describe "
            "Swarajists as constitutional loyalists who accepted colonial "
            "rule.",
            "State the founding date, founders and council-entry logic "
            "together whenever a question asks about the Swaraj Party's "
            "formation, and flag the Gaya/January source variance rather "
            "than silently picking one date.",
        ),
        (
            "Swarajist achievements in the 1923 legislatures",
            "The Swarajists performed strongly in the 1923 elections and "
            "used their legislative position to obstruct budgets and expose "
            "the structural weaknesses of dyarchy, converting an abstract "
            "nationalist critique of the 1919 reforms into a demonstrated "
            "legislative fact.",
            [
                "Strong 1923 election results gave Swarajists a real "
                "legislative presence.",
                "Obstruction targeted budgets and government motions to "
                "expose dyarchy's limits.",
                "The demonstration effect mattered as much as any specific "
                "legislative victory.",
                "This record answers 'assess the Swarajist experiment' "
                "demands directly.",
            ],
            "Do not state specific Swarajist seat numbers or vote shares "
            "without a verified figure; argue from the qualitative record "
            "instead.",
            "Use the 'exposed but could not change dyarchy' formulation as "
            "the core Swarajist verdict.",
        ),
        (
            "Swarajist decline after 1925",
            "C.R. Das's death in 1925 removed the Swaraj Party's principal "
            "leader, and as the later 1920s progressed, ministries, "
            "patronage and factional politics gradually drew some members "
            "away from disciplined obstruction, reducing the Party's "
            "momentum.",
            [
                "C.R. Das's 1925 death weakened Swarajist leadership "
                "continuity.",
                "Motilal Nehru continued association with the Party and "
                "later constitutional debates.",
                "Ministerial office and patronage opportunities diluted "
                "obstruction's discipline over time.",
                "Decline does not erase the Party's earlier demonstration "
                "effect against dyarchy.",
            ],
            "Present decline as gradual erosion, not a sudden collapse of "
            "the Swarajist project.",
            "Use this session to balance the achievement account with a "
            "factual account of decline.",
        ),
        (
            "Continuity: both wings reassemble for 1930",
            "Despite their apparent rupture, the Swarajist and No-changer "
            "wings both remained within Congress and reassembled their "
            "methods and personnel for the 1930 Civil Disobedience "
            "Movement, so the 1920s should be read as continuity rather "
            "than an empty gap.",
            [
                "Swarajist obstruction demonstrated dyarchy's emptiness, an "
                "argument reused in the case for Purna Swaraj.",
                "No-changer constructive work supplied the rural cadre the "
                "1930 movement needed.",
                "Congress's organisational reforms from Nagpur persisted "
                "through the 1920s into 1930.",
                "This continuity thesis directly answers 'was the 1920s a "
                "period of decline?' demands.",
            ],
            "Do not describe the 1920s as a trough between two Gandhian "
            "movements; state explicitly what carried forward.",
            "Use this session as the bridge sentence between the "
            "constitutional stream and the 1930 movement.",
        ),
        (
            "HRA formation and the republican programme",
            "The Hindustan Republican Association was founded at Kanpur in "
            "October 1924 by leaders including Sachindranath Sanyal, Ram "
            "Prasad Bismil and Jogesh Chatterjee with a republican "
            "revolutionary programme aimed at the armed overthrow of "
            "colonial rule, reviving armed politics after 1922 had "
            "discredited non-violence for a section of the young.",
            [
                "HRA's founders included Sachindranath Sanyal, Ram Prasad "
                "Bismil and Jogesh Chatterjee.",
                "It was founded at Kanpur in October 1924.",
                "Its aim was an armed overthrow of colonial rule and the "
                "establishment of a republican India.",
                "The organisation needed funds and recruits, which led "
                "directly to the 1925 Kakori action.",
            ],
            "Do not treat HRA and the later HSRA as identical; HRA's 1924 "
            "programme is republican, not yet explicitly socialist.",
            "Use HRA's Kanpur founding, date and aim together whenever a "
            "question asks about revolutionary revival after 1922.",
        ),
        (
            "Kakori conspiracy and the 1927 executions",
            "The Kakori train action of 1925 aimed to raise funds for "
            "HRA's revolutionary activity, and the resulting Kakori "
            "conspiracy case led to the 1927 execution of Ram Prasad "
            "Bismil, Ashfaqulla Khan, Roshan Singh and Rajendra Lahiri, "
            "creating the first mass martyr cult of the interwar "
            "revolutionary period.",
            [
                "Kakori (1925) was a fund-raising train action, not a case "
                "involving Bhagat Singh.",
                "Bismil, Ashfaqulla Khan, Roshan Singh and Rajendra Lahiri "
                "were executed in 1927 after the case.",
                "The trial and executions publicised revolutionary "
                "sacrifice and expanded recruitment appeal.",
                "Kakori belongs to the HRA phase of revolutionary "
                "nationalism, distinct from the later HSRA phase.",
            ],
            "Do not place Bhagat Singh in the Kakori case; his major cases "
            "are Saunders, the Assembly Bomb and the Lahore Conspiracy "
            "Case.",
            "State the four executed names and the HRA/Kakori link "
            "whenever a question tests this sequence.",
        ),
        (
            "Naujawan Bharat Sabha and youth mobilisation",
            "The Naujawan Bharat Sabha, founded in March 1926 in Lahore "
            "with Bhagat Singh as a leading organiser, mobilised youth, "
            "workers and peasants toward socialist and anti-imperialist "
            "politics as an open, legal public front - organisationally "
            "distinct from the underground HRA/HSRA network - forming an "
            "ideological bridge between the Kakori-era HRA and the 1928 "
            "socialist reorganisation as HSRA.",
            [
                "The Sabha was founded in Lahore in March 1926.",
                "Bhagat Singh was a leading organiser of the Sabha alongside "
                "other future HSRA revolutionaries.",
                "It operated as an open, legal front distinct from the "
                "underground HRA/HSRA network it fed.",
                "The Sabha's activity precedes and feeds into HRA's 1928 "
                "reorganisation as HSRA.",
            ],
            "Do not treat the Naujawan Bharat Sabha and HSRA as the same "
            "organisation founded on the same date; the Sabha (1926, open "
            "front) precedes and feeds the underground HSRA (1928).",
            "Use the Sabha to answer questions on the social and "
            "ideological preparation behind the HRA-to-HSRA transition.",
        ),
        (
            "HRA's reorganisation as HSRA: the socialist turn",
            "On 9-10 September 1928, at Ferozeshah Kotla in Delhi, the HRA "
            "was reorganised as the Hindustan Socialist Republican "
            "Association under leaders including Bhagat Singh, "
            "Chandrashekhar Azad, Sukhdev and Bhagwati Charan Vohra, marking "
            "a change in theory as much as name: the movement now named "
            "both imperialism and class exploitation as its enemy. HRA and "
            "HSRA are one continuous organisational lineage, not rival "
            "bodies, and 'Association' and 'Army' are variant source "
            "labels for the same body.",
            [
                "The new name explicitly added 'Socialist' to the "
                "organisation's identity.",
                "The renaming meeting was held at Ferozeshah Kotla, Delhi, "
                "on 9-10 September 1928.",
                "Prominent HSRA leaders included Bhagat Singh, "
                "Chandrashekhar Azad, Sukhdev and Bhagwati Charan Vohra.",
                "This turn made socialism a mainstream vocabulary of Indian "
                "revolutionary anti-colonialism.",
            ],
            "Describe the 1928 change as an ideological turn; do not call "
            "HSRA merely a renamed HRA, and do not treat HRA and HSRA as "
            "two rival organisations.",
            "Use this session to answer 'ideological evolution from HRA to "
            "HSRA' demands directly.",
        ),
        (
            "Lala Lajpat Rai, Saunders and the road to the Assembly bomb",
            "Lala Lajpat Rai died from injuries sustained during a "
            "lathi-charge on an anti-Simon Commission protest, and HSRA "
            "revolutionaries killed the police officer Saunders in December "
            "1928 in retaliation, an act that sharpened confrontation with "
            "the state ahead of the 1929 Assembly bomb action.",
            [
                "Lala Lajpat Rai was injured during a protest against the "
                "Simon Commission, whose composition and reception belong "
                "to the next topic.",
                "His injuries contributed to his death, which HSRA treated "
                "as an unavenged wrong.",
                "Saunders was killed in December 1928 by HSRA "
                "revolutionaries in retaliation.",
                "This episode escalated HSRA's confrontation with colonial "
                "authority just before the Assembly bomb action.",
            ],
            "Do not conflate the Saunders case with the Kakori case; "
            "Saunders belongs to the later HSRA phase.",
            "Use this causal chain to explain why HSRA moved from "
            "Kakori-era fund-raising toward direct confrontation.",
        ),
        (
            "The Assembly bomb: symbolic and non-lethal intent",
            "On 8 April 1929 Bhagat Singh and Batukeshwar Dutt threw bombs "
            "in the Central Legislative Assembly, deliberately designed to "
            "be non-lethal and symbolic, intended, in their own political "
            "language, 'to make the deaf hear', and both accepted arrest to "
            "use the ensuing trial as a public platform. This bombing was "
            "tried separately as the Assembly Bomb Case in the Sessions "
            "Court, which sentenced both men to life imprisonment - a "
            "distinct proceeding from the later Lahore Conspiracy Case.",
            [
                "The action targeted the Assembly chamber during a "
                "sitting, not a crowd of civilians.",
                "The bombs were designed to avoid indiscriminate killing, "
                "unlike an assassination attempt.",
                "Bhagat Singh and Dutt did not attempt to escape, choosing "
                "arrest and trial deliberately.",
                "The Assembly Bomb Case (Sessions Court, life imprisonment) "
                "is a separate proceeding from the later Lahore Conspiracy "
                "Case (Special Tribunal, death sentence).",
            ],
            "Do not describe the Assembly bomb as an attempt at mass "
            "killing; its intent was symbolic and non-lethal by design. Do "
            "not merge the Assembly Bomb Case with the Lahore Conspiracy "
            "Case into one undifferentiated trial.",
            "Use the deliberate non-lethal design and voluntary arrest "
            "together to answer questions on the Assembly action's "
            "significance, and keep its Sessions Court verdict distinct "
            "from the Lahore Conspiracy Case's later Special Tribunal "
            "verdict.",
        ),
        (
            "Lahore Conspiracy Case, the jail hunger strike and Jatin Das",
            "Evidence from the Assembly Bomb Case and the Saunders killing "
            "together fed the separate, later Lahore Conspiracy Case, "
            "during which political prisoners including Jatin Das undertook "
            "a hunger strike demanding better prison treatment; Jatin Das "
            "died on 13 September 1929 after a sustained hunger strike in "
            "Lahore Central Jail reported as 63 days in most accounts and "
            "64 days in some others, and the Special Tribunal later "
            "sentenced Bhagat Singh, Sukhdev and Rajguru to death in "
            "October 1930.",
            [
                "The Lahore Conspiracy Case tried Bhagat Singh, Sukhdev, "
                "Rajguru and other HSRA members, and is a distinct "
                "proceeding from the earlier Assembly Bomb Case.",
                "Prisoners undertook a hunger strike demanding treatment "
                "appropriate to political prisoners, not ordinary "
                "criminals.",
                "Jatin Das died on 13 September 1929 after the hunger "
                "strike, its length reported as 63 or 64 days depending on "
                "the source, becoming a widely mourned martyr figure.",
                "The Special Tribunal's death sentence followed later, in "
                "October 1930.",
            ],
            "Keep the jail hunger strike and Jatin Das's death (1929) "
            "distinct from the Tribunal's verdict (1930) and the execution "
            "(1931); keep this case distinct from the earlier Assembly "
            "Bomb Case; and retain both the 63-day and 64-day fast figures "
            "as an open source variance rather than asserting one.",
            "Sequence hunger strike, verdict and execution correctly when "
            "answering on the Lahore Conspiracy Case.",
        ),
        (
            "Bhagat Singh as rationalist political thinker and the 1931 "
            "execution",
            "Bhagat Singh's later writings and prison conduct show a "
            "rationalist, atheist and socialist political position that "
            "named both imperialism and class exploitation as the "
            "movement's targets, so his legacy should be read as a "
            "political thinker as well as a martyr; he, Sukhdev and Rajguru "
            "were executed on 23 March 1931 after the Lahore Conspiracy Case "
            "verdict.",
            [
                "Bhagat Singh's prison writings reflect a rationalist and "
                "explicitly socialist political outlook.",
                "His politics named imperialism and class exploitation "
                "together as the object of struggle.",
                "Bhagat Singh, Sukhdev and Rajguru were executed on 23 "
                "March 1931 at Lahore.",
                "Historiography has moved from a romantic-martyr reading "
                "toward recognising his ideological and analytical "
                "contribution.",
            ],
            "Do not quote Bhagat Singh's writings verbatim; describe his "
            "rationalist, atheist and socialist position analytically.",
            "Use the thinker-not-only-martyr framing directly for "
            "'evaluate Bhagat Singh as a political thinker' demands.",
        ),
        (
            "Chittagong and the plural revolutionary field of the 1920s",
            "The Chittagong Armoury Raid of 1930 in Bengal, led by Surya "
            "Sen and including women revolutionaries, represents an "
            "attempted seizure of a locality rather than an individual "
            "action, showing that revolutionary nationalism in the 1920s "
            "was regionally plural, spanning Punjab, the United Provinces "
            "and Bengal, and not confined to one figure or one province. "
            "The Chittagong stream was organisationally separate from the "
            "Punjab-United Provinces HRA/HSRA network, sharing "
            "revolutionary aims but not a common command structure.",
            [
                "The Chittagong Armoury Raid occurred in 1930 in Bengal "
                "under Surya Sen's leadership.",
                "Women revolutionaries participated in the Chittagong "
                "action, widening the standard picture of revolutionary "
                "nationalism.",
                "Chittagong's ambition to seize a locality distinguishes it "
                "from the individual actions typical of HRA and HSRA "
                "elsewhere.",
                "Chittagong was organisationally separate from the "
                "Punjab-United Provinces HRA/HSRA network, not a regional "
                "branch of it.",
            ],
            "Chittagong belongs to Bengal under Surya Sen and overlaps "
            "chronologically with 1930 Civil Disobedience, covered fully in "
            "the next topic; do not relocate it to Punjab or treat it as an "
            "HSRA action or organisational branch.",
            "Close a 20-mark 'was the 1920s a lull' answer by naming all "
            "four streams, including Chittagong, in one graded verdict.",
        ),
    ],
}


SESSION_VISUALS = {
    "Setting: wartime distress, Rowlatt-Jallianwala anger and Khilafat "
    "emergence": """1919 -> wartime distress + Rowlatt Act + Jallianwala Bagh harden opinion
NOV 1919 -> All-India Khilafat Conference at Delhi threatens non-cooperation
1920 -> Gandhi links Khilafat to Swaraj to build Hindu-Muslim unity
SEP 1920 -> Calcutta Special Session adopts Non-Cooperation
DEC 1920 -> Nagpur Congress ratifies the programme and reorganises Congress""",
    "Khilafat aims, leadership and the Delhi Conference": """ISSUE -> defence of the Ottoman Sultan-Caliph after WWI and Treaty of Sevres
LEADERS -> Mohammad Ali, Shaukat Ali, Azad, Hakim Ajmal Khan, Hasrat Mohani
COMMITTEE -> Khilafat Committee active before the Nov 1919 Delhi Conference
NOV 1919 -> Delhi Conference threatens withdrawal of cooperation
RULE -> a political-religious mobilisation, not a Hindu movement""",
    "Gandhi's alliance logic for Khilafat-Congress unity": """KHILAFAT GRIEVANCE -> emotionally resonant anti-imperial issue for Muslims
GANDHI'S LINK -> ties Khilafat to Swaraj as a joint national demand
EFFECT -> widens anti-British mobilisation beyond a narrow political class
RISK -> unity rests on an international issue India does not control
LATER -> 1924 abolition of the Caliphate exposes this fragility""",
    "Calcutta Special Session: adopting Non-Cooperation": """SEP 1920 CALCUTTA SPECIAL SESSION -> adopts Non-Cooperation programme
STATUS -> becomes Congress's own programme, not only Gandhi's campaign
NEXT STEP -> ratification still required
DEC 1920 -> Nagpur ratifies
RULE -> Calcutta adopted; Nagpur ratified; do not merge the two""",
    "Nagpur Congress: ratification and mass reorganisation": """DEC 1920 NAGPUR -> ratifies Non-Cooperation programme
REORGANISATION -> linguistic provincial committees + AICC + Working Committee
FEE -> low membership fee widens Congress beyond professional classes
EFFECT -> Congress becomes a continuous mass organisation
RULE -> Nagpur is reorganisation, not only a political resolution""",
    "The programme's escalation ladder": """STAGE 1 -> surrender of titles and honorary offices
STAGE 2 -> boycott of schools, courts, councils and official functions
STAGE 3 -> economic boycott of foreign cloth; picketing of liquor shops
STAGE 4 -> constructive programme: khadi, charkha, swadeshi, education
STAGE 5 -> mass civil disobedience and tax refusal; planned, never launched""",
    "Urban mobilisation: students, lawyers, traders and women": """STUDENTS -> leave schools and colleges
LAWYERS -> suspend court practice
TRADERS -> boycott foreign cloth
WOMEN -> join picketing and khadi work
EFFECT -> a genuinely widened, though uneven, social base""",
    "Constructive programme and national institutions": """PROGRAMME -> khadi, charkha, swadeshi, national education, panchayats, unity
INSTITUTIONS -> Jamia Millia Islamia, Kashi Vidyapith, Gujarat Vidyapith, Bihar Vidyapith
FUNCTION -> alternative moral economy alongside boycott
DURABILITY -> institutions and cadre survive after boycott is reversed
LATER USE -> this cadre and network reappear in the 1930 campaign""",
    "Prince of Wales boycott and repression": """1921 PRINCE OF WALES VISIT -> met with hartal and boycott
GOVERNMENT RESPONSE -> arrests and repression intensify
REPRESSION -> widens sympathy and participation
PARTICIPATION -> movement approaches its escalation ceiling
CEILING -> Gandhi still withholds the final mass civil disobedience stage""",
    "The Eka movement in the United Provinces": """GRIEVANCE -> rent ~50% above recorded rent; thekedars; share-rents
RITUAL -> Ganges-oath meetings bind peasants to pay recorded rent on time
LEADERSHIP -> Madari Pasi, outside Congress-Khilafat discipline
BASE -> tenants plus many small zamindars
END -> severe official repression closes the movement by March 1922""",
    "The Malabar Mappila rebellion and its communal turn": """APR 1920 -> Malabar District Congress Conference at Manjeri gives impetus
GRIEVANCE -> insecure tenure, renewal fees, high rents, landlord exactions
AUG 1921 -> Mappila rebellion begins in Malabar
SHIFT -> local mobilisation later acquires a communal character
EFFECT -> damages the wider Khilafat-Congress alliance""",
    "Bardoli and the planned mass civil disobedience": """PLAN -> mass civil disobedience announced for Bardoli taluqa, Surat district
LOGIC -> concentrate escalation in one disciplined taluqa
STATUS -> never launched; Chauri Chaura intervenes first
LATER -> Bardoli's own no-tax satyagraha under Patel waits until 1928
RULE -> the 1922 plan and the 1928 satyagraha are distinct events""",
    "Chauri Chaura and the withdrawal": """4 FEB 1922 -> Chauri Chaura procession clashes with police, Gorakhpur district
OUTCOME -> police station burnt; twenty-two policemen killed
12 FEB 1922 -> Working Committee ratifies withdrawal: the Bardoli resolution
MAR 1922 -> Gandhi arrested and sentenced to six years' imprisonment
RULE -> violence caused withdrawal; weakness of the movement did not""",
    "Achievements and limits of Non-Cooperation": """GAIN -> first genuinely all-India mass movement; reorganised Congress
GAIN -> durable institutions, khadi network and trained rural cadre
COST -> boycott proved reversible; Swarajists reverse it in 1923
COST -> the escalation ladder's final stage was never tested
VERDICT -> graded assessment, not simple success or failure""",
    "Consequences: fragile unity and the bridge to the 1920s": """1922 WITHDRAWAL -> Swarajist-No-changer debate opens
DRIFT -> some younger activists turn toward revolutionary politics
1924 -> Caliphate abolished; Khilafat unity's foundation disappears
BRIDGE -> these threads carry into the Swarajist and revolutionary 1920s
NEXT TOPIC -> Swarajists, constructive work and revolutionaries (topic 21)""",
    "The 1922 strategic vacuum and the No-changer/Pro-changer debate": """FEB 1922 -> Non-Cooperation withdrawn; Congress faces a strategic vacuum
1922 -> No-changer versus Pro-changer debate opens over the next method
1 JAN 1923 -> Swaraj Party founded by C.R. Das and Motilal Nehru
1923 -> Swarajists enter legislatures on a council-entry, obstruction platform
1924 -> Hindustan Republican Association founded with a republican programme""",
    "No-changers and constructive work after withdrawal": """METHOD -> khadi, national schools, Hindu-Muslim unity, anti-untouchability
AIM -> preparation for a future mass struggle, not passivity
EFFECT -> continuous rural contact and a trained cadre of workers
LIMIT -> politically quietist; no direct confrontation with the state
LEGACY -> this cadre supplies the 1930 movement's social base""",
    "Swaraj Party formation and council-entry logic": """DEC 1922 GAYA -> council-entry proposal rejected by Congress
1 JAN 1923 (WORKING DATE) -> Swaraj Party founded by C.R. Das and Motilal Nehru
METHOD -> council-entry followed by disciplined obstruction
NOTE -> some compact sources date founding to Dec 1922 itself; variance flagged
RULE -> obstruction is a tactic, not constitutional loyalism""",
    "Swarajist achievements in the 1923 legislatures": """1923 ELECTIONS -> strong Swarajist performance
METHOD -> obstruct budgets and government motions
EFFECT -> exposes the structural weakness of dyarchy
VALUE -> demonstration matters as much as any single legislative win
CAUTION -> do not state unverified seat numbers or vote shares""",
    "Swarajist decline after 1925": """1925 -> C.R. Das dies; Swarajist leadership weakens
LATER 1920s -> ministries and patronage erode obstruction's discipline
CONTINUITY -> Motilal Nehru continues into later constitutional debates
VERDICT -> gradual erosion, not sudden collapse
BALANCE -> decline does not erase the earlier demonstration effect""",
    "Continuity: both wings reassemble for 1930": """SWARAJISTS -> exposed dyarchy's emptiness; argument reused for Purna Swaraj
NO-CHANGERS -> built rural cadre and constructive institutions
NAGPUR REFORMS -> persist through the 1920s
1930 -> both wings and organisational reforms reassemble for CDM
VERDICT -> continuity, not an empty gap between two movements""",
    "HRA formation and the republican programme": """OCT 1924, KANPUR -> Hindustan Republican Association founded
LEADERS -> Sachindranath Sanyal, Ram Prasad Bismil, Jogesh Chatterjee
AIM -> armed overthrow of colonial rule; a republican India
METHOD -> underground organisation and fund-raising for revolutionary action
CONTEXT -> revives after 1922 discredited non-violence for some youth""",
    "Kakori conspiracy and the 1927 executions": """1925 -> Kakori train action raises funds for revolutionary activity
CASE -> Kakori conspiracy case tried against HRA revolutionaries
1927 -> Bismil, Ashfaqulla Khan, Roshan Singh, Rajendra Lahiri executed
EFFECT -> first mass martyr cult of the interwar revolutionary period
RULE -> Kakori is HRA; do not place Bhagat Singh in this case""",
    "Naujawan Bharat Sabha and youth mobilisation": """MARCH 1926, LAHORE -> Naujawan Bharat Sabha founded
ROLE -> Bhagat Singh a leading organiser among its founders
FRONT -> open, legal front, distinct from the underground HRA/HSRA network
IDEOLOGY -> socialist and secular political education
BRIDGE -> feeds personnel and ideas into the 1928 HSRA reorganisation""",
    "HRA's reorganisation as HSRA: the socialist turn": """9-10 SEP 1928, FEROZESHAH KOTLA DELHI -> HRA renamed HSRA
LEADERS -> Bhagat Singh, Chandrashekhar Azad, Sukhdev, Bhagwati Charan Vohra
CHANGE -> explicit socialist and anti-imperialist ideology, not just a new name
LINEAGE -> one continuous body under a new name, not two rival organisations
EFFECT -> socialism becomes a mainstream revolutionary vocabulary""",
    "Lala Lajpat Rai, Saunders and the road to the Assembly bomb": """SIMON COMMISSION PROTEST -> lathi-charge injures Lala Lajpat Rai
INJURIES -> contribute to his death
HSRA RESPONSE -> plans retaliation against the officer held responsible
DEC 1928 -> Saunders killed by HSRA revolutionaries
EFFECT -> sharpens confrontation ahead of the 1929 Assembly action""",
    "The Assembly bomb: symbolic and non-lethal intent": """8 APRIL 1929 -> Bhagat Singh and Batukeshwar Dutt act in the Assembly
METHOD -> bombs designed to be non-lethal; leaflets and slogans follow
INTENT -> 'to make the deaf hear', not to kill
CHOICE -> both accept arrest rather than flee
CASE -> tried separately as Assembly Bomb Case; life imprisonment (Sessions Court)""",
    "Lahore Conspiracy Case, the jail hunger strike and Jatin Das": """CASE -> Lahore Conspiracy Case tries Bhagat Singh, Sukhdev, Rajguru (separate from Assembly Bomb Case)
DEMAND -> hunger strike for treatment as political prisoners
13 SEP 1929 -> Jatin Das dies after a jail hunger strike (63 or 64 days, source variance)
OCT 1930 -> Special Tribunal sentences the three to death
23 MAR 1931 -> the three are executed at Lahore""",
    "Bhagat Singh as rationalist political thinker and the 1931 "
    "execution": """POSITION -> rationalist, atheist and socialist political thought
ENEMY -> imperialism and class exploitation named together
METHOD -> courtroom and public trial used as political theatre
LEGACY -> political thinker as well as martyr
23 MAR 1931 -> executed with Sukhdev and Rajguru at Lahore""",
    "Chittagong and the plural revolutionary field of the 1920s": """1930 -> Chittagong Armoury Raid led by Surya Sen in Bengal
PARTICIPANTS -> included women revolutionaries
AMBITION -> attempted seizure of a locality, not an individual action
REGIONS -> Punjab, United Provinces and Bengal, not one province
VERDICT -> the 1920s were organisationally and ideologically dense""",
}


SESSION_DEFINITIONS = {
    "Setting: wartime distress, Rowlatt-Jallianwala anger and Khilafat "
    "emergence": "The 1919-20 convergence is the joint effect of wartime "
    "distress, the Rowlatt-Jallianwala reform-repression contradiction and "
    "the emerging Khilafat question, together making Non-Cooperation "
    "politically possible.",
    "Khilafat aims, leadership and the Delhi Conference": "The Khilafat "
    "movement was a political mobilisation defending the Ottoman "
    "Sultan-Caliph's authority, organised under named leaders and given "
    "public form at the November 1919 Delhi Conference.",
    "Gandhi's alliance logic for Khilafat-Congress unity": "Gandhi's "
    "alliance logic is the deliberate linking of the Khilafat grievance to "
    "the Swaraj demand to build Hindu-Muslim political unity, accepting "
    "the risk that the alliance's foundation lay outside India's control.",
    "Calcutta Special Session: adopting Non-Cooperation": "The Calcutta "
    "Special Session was the September 1920 Congress meeting that formally "
    "adopted the Non-Cooperation programme, distinct from its later Nagpur "
    "ratification.",
    "Nagpur Congress: ratification and mass reorganisation": "Nagpur's "
    "ratification is the December 1920 Congress decision that both "
    "confirmed Non-Cooperation and reorganised Congress into a mass "
    "political organisation.",
    "The programme's escalation ladder": "The escalation ladder is the "
    "programme's graded sequence from renunciation through boycott and "
    "constructive work to a final, never-launched stage of mass civil "
    "disobedience and tax refusal.",
    "Urban mobilisation: students, lawyers, traders and women": "Urban "
    "mobilisation names the specific social groups, students, lawyers, "
    "traders and women, whose participation widened the boycott's social "
    "base beyond the earlier educated political class.",
    "Constructive programme and national institutions": "The constructive "
    "programme is Gandhi's parallel-institution strategy of khadi, "
    "education, panchayats and unity work, whose institutions outlasted "
    "the boycott's later reversal.",
    "Prince of Wales boycott and repression": "The Prince of Wales boycott "
    "is the 1921 hartal and boycott of the royal visit, whose repression "
    "tested but did not exceed the movement's self-imposed escalation "
    "limit.",
    "The Eka movement in the United Provinces": "The Eka movement is a "
    "United Provinces peasant campaign against excess rent and thekedar "
    "oppression that adopted nationalist moral language while organising "
    "under its own, non-Congress leadership.",
    "The Malabar Mappila rebellion and its communal turn": "The Malabar "
    "rebellion is an agrarian movement that began with nationalist impetus "
    "from the Manjeri conference and later shifted toward a communal "
    "character, straining Khilafat-era unity.",
    "Bardoli and the planned mass civil disobedience": "The Bardoli plan "
    "is Gandhi's announced but never launched design to concentrate the "
    "programme's final escalation stage in one disciplined taluqa.",
    "Chauri Chaura and the withdrawal": "Chauri Chaura is the 4 February "
    "1922 violent clash whose breach of non-violent discipline led Gandhi "
    "to secure the Working Committee's 12 February 1922 withdrawal "
    "resolution.",
    "Achievements and limits of Non-Cooperation": "A graded verdict on "
    "Non-Cooperation weighs its unprecedented mass mobilisation and "
    "durable institutions against its reversible boycott and untested "
    "final stage.",
    "Consequences: fragile unity and the bridge to the 1920s": "The "
    "post-withdrawal consequence chain links Non-Cooperation's end to the "
    "Swarajist-No-changer debate, revolutionary drift and the Caliphate's "
    "1924 abolition.",
    "The 1922 strategic vacuum and the No-changer/Pro-changer debate": "The "
    "1922 strategic vacuum is Congress's post-withdrawal need to choose a "
    "new method, resolved through the No-changer/Pro-changer debate rather "
    "than an organisational split.",
    "No-changers and constructive work after withdrawal": "No-changer "
    "continuity is the sustained pursuit of Gandhian constructive work as "
    "preparation for future struggle, rather than a passive retreat from "
    "politics.",
    "Swaraj Party formation and council-entry logic": "Council-entry logic "
    "is the Swarajist argument that entering the legislatures to obstruct "
    "government exposes colonial reform's limits rather than legitimising "
    "colonial rule.",
    "Swarajist achievements in the 1923 legislatures": "The Swarajist "
    "record is the demonstrated legislative fact that an elected Indian "
    "majority could obstruct dyarchy without being able to govern under "
    "it.",
    "Swarajist decline after 1925": "Swarajist decline is the gradual, "
    "post-1925 erosion of obstruction's discipline through leadership loss "
    "and the pull of ministerial patronage.",
    "Continuity: both wings reassemble for 1930": "Continuity names the "
    "process by which Swarajist and No-changer methods and personnel "
    "carried forward into the 1930 Civil Disobedience Movement.",
    "HRA formation and the republican programme": "The republican "
    "programme is HRA's October 1924 Kanpur-founded aim of an armed "
    "overthrow of colonial rule to establish a republican India, distinct "
    "from HSRA's later socialist programme.",
    "Kakori conspiracy and the 1927 executions": "The Kakori conspiracy is "
    "the 1925 HRA fund-raising train action and its 1927 trial and "
    "executions, the interwar period's first mass revolutionary martyr "
    "cult.",
    "Naujawan Bharat Sabha and youth mobilisation": "The Naujawan Bharat "
    "Sabha is the March 1926 Lahore youth organisation, an open legal "
    "front distinct from the underground HRA/HSRA network, that mobilised "
    "socialist and anti-imperialist politics ahead of HSRA's formal 1928 "
    "reorganisation.",
    "HRA's reorganisation as HSRA: the socialist turn": "The socialist "
    "turn is HRA's reorganisation as HSRA at Ferozeshah Kotla, Delhi, on "
    "9-10 September 1928 - one continuous organisational lineage under a "
    "new name, not a rival body - which added an explicit anti-imperialist "
    "and anti-capitalist ideology to the earlier republican programme.",
    "Lala Lajpat Rai, Saunders and the road to the Assembly bomb": "This "
    "causal chain links Lala Lajpat Rai's death from protest injuries to "
    "HSRA's retaliatory killing of Saunders and the sharpened confrontation "
    "before the Assembly bomb.",
    "The Assembly bomb: symbolic and non-lethal intent": "The Assembly "
    "bomb is the 8 April 1929 deliberately non-lethal, symbolic action, "
    "tried separately as the Assembly Bomb Case in the Sessions Court "
    "(life imprisonment), intended to publicise revolutionary politics "
    "through voluntary arrest and trial.",
    "Lahore Conspiracy Case, the jail hunger strike and Jatin Das": "The "
    "Lahore Conspiracy Case is a separate, later Special Tribunal "
    "proceeding from the Assembly Bomb Case, during which the jail "
    "hunger strike and Jatin Das's 1929 death (reported as 63 or 64 days) "
    "occurred, distinct from the 1930 verdict and 1931 execution.",
    "Bhagat Singh as rationalist political thinker and the 1931 "
    "execution": "Bhagat Singh's political thought is his rationalist, "
    "atheist and socialist position naming imperialism and class "
    "exploitation together, distinct from a purely sentimental martyr "
    "reading.",
    "Chittagong and the plural revolutionary field of the 1920s": "The "
    "plural revolutionary field names the regional and organisational "
    "diversity of 1920s revolutionary nationalism, from Punjab and the "
    "United Provinces to the Chittagong Armoury Raid in Bengal.",
}


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-20": [
        (
            "Convergence chronology",
            "chronology",
            """1919 -> wartime distress, Rowlatt Act and Jallianwala Bagh harden nationalist opinion
NOV 1919 -> All-India Khilafat Conference at Delhi threatens non-cooperation
1920 -> Gandhi links Khilafat to Swaraj to build Hindu-Muslim unity
SEP 1920 -> Calcutta Special Session adopts Non-Cooperation
DEC 1920 -> Nagpur Congress ratifies the programme and reorganises Congress.""",
            [
                "Setting: wartime distress, Rowlatt-Jallianwala anger and "
                "Khilafat emergence",
            ],
        ),
        (
            "Khilafat leadership and demand",
            "list",
            """ISSUE -> defence of the Ottoman Sultan-Caliph after WWI and the Treaty of Sevres
LEADERS -> Maulana Mohammad Ali, Shaukat Ali, Maulana Azad, Hakim Ajmal Khan, Hasrat Mohani
COMMITTEE -> a Khilafat Committee existed before the Nov 1919 Delhi Conference
NOV 1919 -> All-India Khilafat Conference threatens withdrawal of cooperation
RULE -> a political-religious mobilisation, not a Hindu movement.""",
            ["Khilafat aims, leadership and the Delhi Conference"],
        ),
        (
            "Gandhi's unity logic",
            "causal-flow",
            """KHILAFAT GRIEVANCE -> emotionally resonant anti-imperial issue for Indian Muslims
GANDHI'S LINK -> ties Khilafat to Swaraj as a joint national demand
EFFECT -> widens anti-British mobilisation beyond a narrow political class
RISK -> unity rests on an international issue India does not control
LATER -> 1924 abolition of the Caliphate exposes this fragility.""",
            ["Gandhi's alliance logic for Khilafat-Congress unity"],
        ),
        (
            "Calcutta-to-Nagpur double decision",
            "chronology",
            """SEP 1920 CALCUTTA SPECIAL SESSION -> adopts Non-Cooperation programme
DEC 1920 NAGPUR CONGRESS -> ratifies the programme
REORGANISATION -> linguistic provincial committees, AICC, stronger Working Committee
EFFECT -> low membership fee widens the Congress beyond professional classes
RULE -> Calcutta adopted; Nagpur ratified and reorganised; do not merge the two.""",
            [
                "Calcutta Special Session: adopting Non-Cooperation",
                "Nagpur Congress: ratification and mass reorganisation",
            ],
        ),
        (
            "Escalation ladder",
            "process",
            """STAGE 1 -> surrender of titles and honorary offices
STAGE 2 -> boycott of schools, colleges, law courts, councils and official functions
STAGE 3 -> economic boycott of foreign cloth; picketing of liquor shops
STAGE 4 -> constructive programme: khadi, charkha, swadeshi, national education
STAGE 5 -> mass civil disobedience and tax refusal, planned for Bardoli, never launched.""",
            ["The programme's escalation ladder"],
        ),
        (
            "Urban actors matrix",
            "comparison",
            """GROUP          ACTION                              EFFECT
students       leave schools and colleges          visible break with state education
lawyers        suspend court practice              symbolic rejection of colonial law
traders        boycott foreign cloth               economic pressure and khadi demand
women          picketing and khadi/charkha work    widened the movement's social base.""",
            ["Urban mobilisation: students, lawyers, traders and women"],
        ),
        (
            "Constructive programme and institutions",
            "process",
            """PROGRAMME -> khadi, charkha, swadeshi, national education, panchayats, unity
INSTITUTIONS -> Jamia Millia Islamia, Kashi Vidyapith, Gujarat Vidyapith, Bihar Vidyapith
FUNCTION -> alternative moral economy alongside the boycott programme
DURABILITY -> institutions and cadre survive after boycott is reversed
LATER USE -> this cadre and network re-appear in the 1930 campaign.""",
            ["Constructive programme and national institutions"],
        ),
        (
            "Prince of Wales boycott and repression feedback",
            "feedback-loop",
            """1921 PRINCE OF WALES VISIT -> met with hartal and boycott
GOVERNMENT RESPONSE -> arrests and repression intensify
REPRESSION -> widens sympathy and participation
PARTICIPATION -> movement approaches its escalation ceiling
CEILING -> Gandhi still withholds the final mass civil disobedience stage.""",
            ["Prince of Wales boycott and repression"],
        ),
        (
            "Eka movement anatomy",
            "process",
            """GRIEVANCE -> rent about fifty per cent above the recorded rent; thekedars; share-rents
RITUAL -> Ganges-oath meetings bind peasants to pay recorded rent on time
LEADERSHIP -> Madari Pasi and other local leaders, outside Congress-Khilafat discipline
BASE -> tenants plus many small zamindars aggrieved by revenue demand
END -> severe official repression closes the movement by March 1922.""",
            ["The Eka movement in the United Provinces"],
        ),
        (
            "Malabar trajectory",
            "causal-flow",
            """APR 1920 -> Malabar District Congress Conference at Manjeri gives early impetus
GRIEVANCE -> insecure tenure, renewal fees, high rents under landlord exactions
AUG 1921 -> Mappila rebellion begins in Malabar
SHIFT -> local mobilisation later acquires a communal character
EFFECT -> damages the wider Khilafat-Congress alliance; not communal from the start.""",
            ["The Malabar Mappila rebellion and its communal turn"],
        ),
        (
            "Bardoli plan to Chauri Chaura to withdrawal",
            "causal-flow",
            """PLAN -> mass civil disobedience announced for Bardoli taluqa, Surat district
4 FEB 1922 -> Chauri Chaura procession clashes with police in Gorakhpur district
OUTCOME -> police station burnt; twenty-two policemen killed
12 FEB 1922 -> Working Committee ratifies withdrawal: the Bardoli resolution
MAR 1922 -> Gandhi arrested and sentenced to six years' imprisonment.""",
            [
                "Bardoli and the planned mass civil disobedience",
                "Chauri Chaura and the withdrawal",
            ],
        ),
        (
            "Balance sheet and 1920s bridge",
            "balance-sheet",
            """GAIN -> first genuinely all-India mass movement; reorganised Congress
GAIN -> durable institutions, khadi network and trained rural cadre
COST -> boycott proved reversible; council boycott reversed by Swarajists in 1923
COST -> Khilafat unity proved fragile; Caliphate abolished in 1924
DEBATE -> Palme Dutt: shielded property; Bipin Chandra: no anti-property intent
BRIDGE -> withdrawal opens the Swarajist-No-changer debate and a revolutionary drift.""",
            [
                "Achievements and limits of Non-Cooperation",
                "Consequences: fragile unity and the bridge to the 1920s",
            ],
        ),
    ],
    "modern-indian-history-21": [
        (
            "Post-1922 debate chronology",
            "chronology",
            """FEB 1922 -> Non-Cooperation withdrawn; Congress faces a strategic vacuum
1922 -> No-changer versus Pro-changer debate opens over the next method
DEC 1922 GAYA -> council-entry proposal rejected; some sources date founding here
1 JAN 1923 (WORKING DATE) -> Swaraj Party founded by C.R. Das and Motilal Nehru
NOTE -> Swarajya Sabha (1920, ex-Home Rule League) is a different, older body
OCT 1924, KANPUR -> Hindustan Republican Association founded with a republican programme.""",
            [
                "The 1922 strategic vacuum and the No-changer/Pro-changer "
                "debate",
            ],
        ),
        (
            "No-changer vs Swarajist comparison",
            "comparison",
            """AXIS         NO-CHANGERS                     SWARAJISTS
method       khadi, schools, unity work      council-entry and obstruction
arena        villages, local institutions    legislatures and budgets
aim          preparation before struggle     exposing dyarchy from within
leaders      Gandhian constructive workers   C.R. Das and Motilal Nehru
rule -> both remained within Congress; this was a tactical, not a national, split.""",
            [
                "No-changers and constructive work after withdrawal",
                "Swaraj Party formation and council-entry logic",
            ],
        ),
        (
            "Swarajist rise-and-decline arc",
            "causal-flow",
            """1 JAN 1923 -> Swaraj Party founded for council-entry and obstruction
1923 ELECTIONS -> strong Swarajist performance in the legislatures
EFFECT -> exposes the structural weakness of dyarchy and the budget settlement
1925 -> C.R. Das's death weakens Swarajist leadership and momentum
LATER 1920s -> ministries and patronage erode obstruction's returns over time.""",
            [
                "Swarajist achievements in the 1923 legislatures",
                "Swarajist decline after 1925",
                "Continuity: both wings reassemble for 1930",
            ],
        ),
        (
            "HRA formation and republican programme",
            "process",
            """OCT 1924, KANPUR -> Hindustan Republican Association founded
LEADERS -> Sachindranath Sanyal, Ram Prasad Bismil, Jogesh Chatterjee
AIM -> armed overthrow of colonial rule and a republican India
METHOD -> underground organisation and fund-raising for revolutionary action
CONTEXT -> revives after the 1922 withdrawal discredited non-violence for some youth.""",
            ["HRA formation and the republican programme"],
        ),
        (
            "Kakori-to-executions sequence",
            "chronology",
            """1925 -> Kakori train action raises funds for revolutionary activity
CASE -> Kakori conspiracy case tried against HRA revolutionaries
1927 -> Bismil, Ashfaqulla Khan, Roshan Singh and Rajendra Lahiri executed
EFFECT -> first mass martyr cult of the interwar revolutionary period
RULE -> Kakori is HRA; do not place Bhagat Singh in this case.""",
            ["Kakori conspiracy and the 1927 executions"],
        ),
        (
            "Naujawan Bharat Sabha bridge",
            "process",
            """MARCH 1926, LAHORE -> Naujawan Bharat Sabha founded
ROLE -> Bhagat Singh a leading organiser among its founders
FRONT -> open, legal front, organisationally distinct from underground HRA/HSRA
IDEOLOGY -> socialist and secular political education, ahead of a formal party turn
BRIDGE -> feeds personnel and ideas into the 1928 HSRA reorganisation.""",
            ["Naujawan Bharat Sabha and youth mobilisation"],
        ),
        (
            "HRA to HSRA ideological turn",
            "comparison",
            """AXIS          HRA (from Oct 1924, Kanpur)       HSRA (from Sep 1928, Ferozeshah Kotla)
programme     republican overthrow             socialist republican overthrow
leaders       Sanyal, Bismil, Chatterjee        Bhagat Singh, Azad, Sukhdev, Vohra
case          Kakori conspiracy (1925)          Saunders, Assembly Bomb, Lahore case
turn -> one lineage renamed, not rival bodies; adds anti-imperialist, anti-capitalist theory.""",
            ["HRA's reorganisation as HSRA: the socialist turn"],
        ),
        (
            "Lajpat Rai to Saunders causal chain",
            "causal-flow",
            """SIMON COMMISSION PROTEST -> lathi-charge injures Lala Lajpat Rai
INJURIES -> contribute to his death
HSRA RESPONSE -> plans retaliation against the officer held responsible
DEC 1928 -> Saunders killed by HSRA revolutionaries
EFFECT -> sharpens confrontation ahead of the 1929 Assembly action.""",
            ["Lala Lajpat Rai, Saunders and the road to the Assembly bomb"],
        ),
        (
            "Assembly bomb symbolic logic",
            "process",
            """8 APRIL 1929 -> Bhagat Singh and Batukeshwar Dutt act in the Assembly
METHOD -> bombs designed to be non-lethal; leaflets and slogans follow
INTENT -> "to make the deaf hear", not to kill
CHOICE -> both accept arrest rather than flee, turning the trial into a platform
CASE -> separate Assembly Bomb Case, Sessions Court: life imprisonment for both.""",
            ["The Assembly bomb: symbolic and non-lethal intent"],
        ),
        (
            "Lahore Conspiracy Case and jail resistance",
            "accountability-map",
            """CASE -> Lahore Conspiracy Case (separate from Assembly Bomb Case) tries Singh, Sukhdev, Rajguru
DEMAND -> hunger strike for better treatment of political prisoners
13 SEP 1929 -> Jatin Das dies after a jail hunger strike (63 or 64 days, sources vary)
OCT 1930 -> Special Tribunal sentences Bhagat Singh, Sukhdev and Rajguru to death
23 MAR 1931 -> the three are executed at Lahore.""",
            ["Lahore Conspiracy Case, the jail hunger strike and Jatin Das"],
        ),
        (
            "Bhagat Singh's thought and martyrdom",
            "concept-map",
            """POSITION -> rationalist, atheist and socialist political thought
ENEMY -> defined as both imperialism and class exploitation
METHOD -> courtroom and public trial used as political theatre
LEGACY -> political thinker as well as martyr; do not reduce him to sentiment alone
CAUTION -> describe his position analytically; do not quote his writings verbatim.""",
            [
                "Bhagat Singh as rationalist political thinker and the 1931 "
                "execution",
            ],
        ),
        (
            "Four streams balance sheet incl. Chittagong",
            "balance-sheet",
            """STREAM 1 -> Swarajists expose dyarchy from inside the legislatures
STREAM 2 -> No-changers build khadi, schools and rural cadre
STREAM 3 -> HRA-HSRA supply martyr tradition and socialist vocabulary
STREAM 4 -> 1930 Chittagong Armoury Raid, Surya Sen, women revolutionaries in Bengal
VERDICT -> the 1920s were not a lull; they built what 1930 required.""",
            ["Chittagong and the plural revolutionary field of the 1920s"],
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
        "scope": "Modern Indian History learner-v2 Topics 20-21",
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
