"""Build Modern Indian History learner-v2 Topics 16-17.

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
import generate_modern_history_14_15_sequential as previous


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
    / "modern-indian-history-16-17-2026-08-31-sequential.json"
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
OFFICIAL_QUESTION_SOURCES = list(base.OFFICIAL_QUESTION_SOURCES)


TOPICS = [
    base.topic(
        16,
        "Revolutionary Nationalism (Phase I, 1907-1917)",
        "16_Revolutionary-Nationalism-Phase-I.md",
        "16_Revolutionary-Nationalism-Phase-I.md",
        "16_Revolutionary-Nationalism-Phase-I-1907-1917_Complete-Topic-Package.md",
        [
            "basic/15_Militant-Nationalism-and-Swadeshi.md",
            "basic/18_WWI-Home-Rule-and-Lucknow-Pact.md",
            "basic/19_Gandhis-Rise-Rowlatt-and-Jallianwala.md",
            "basic/21_Swarajists-and-Revolutionaries-1920s.md",
        ],
        ["https://www.abhilekh-patal.in/"],
        "The National Archives portal is retained only as a present-day archival "
        "bridge. Claims about revolutionary networks, actions, prosecutions and "
        "wartime plans remain grounded in the repository owners and OCR books.",
        "OCR checks use Bipan Chandra's Modern India and India's Struggle for "
        "Independence for the Swadeshi aftermath, Bengal and Maharashtra cells, "
        "India House, Ghadar, wartime conspiracy, repression and strategic limits. "
        "Sekhar Bandyopadhyay supplies regional and transnational qualifications.",
        "UPSC Prelims 2022 Q53 on association with the Ghadar Party is retained as "
        "a routed verification card. The local official key is unavailable, so no "
        "answer option is inferred. No direct Mains PYQ is claimed; all six Mains "
        "questions in this package are explicitly original practice.",
        [
            (
                "Chapekar precursor",
                "In 1897 the Chapekar brothers killed plague commissioner W.C. Rand "
                "and Lieutenant Ayerst in Poona, an armed precursor to the later phase.",
            ),
            (
                "Mitra Mela and Abhinav Bharat",
                "V.D. Savarkar's Mitra Mela developed into Abhinav Bharat in 1904, "
                "linking oath-bound organisation, political education and armed action.",
            ),
            (
                "Bengal revolutionary networks",
                "Anushilan Samiti and Dacca Anushilan were related but distinct Bengal "
                "networks; Barindra Ghosh's circle and Jugantar formed another centre.",
            ),
            (
                "Revolutionary print in Bengal",
                "Jugantar was both a revolutionary network and a newspaper launched "
                "in 1906; Sandhya and Bande Mataram belonged to the wider militant press.",
            ),
            (
                "Muzaffarpur attack",
                "In April 1908 Khudiram Bose and Prafulla Chaki intended to kill "
                "Kingsford at Muzaffarpur, but the bomb killed two European women.",
            ),
            (
                "Alipore Bomb Case",
                "The Alipore Bomb Case of 1908-09 prosecuted the Maniktala circle "
                "associated with Barindra Ghosh; it followed but was not identical "
                "to the Muzaffarpur action.",
            ),
            (
                "India House",
                "Shyamji Krishna Varma founded India House in London; Savarkar later "
                "became a central organiser there but was not its founder.",
            ),
            (
                "Dhingra and Curzon-Wyllie",
                "On 1 July 1909 Madan Lal Dhingra killed Sir William Curzon-Wyllie "
                "in London, bringing India House under intensified surveillance.",
            ),
            (
                "Nasik conspiracy",
                "In December 1909 Anant Kanhere killed Collector A.M.T. Jackson at "
                "Nasik; the prosecution exposed links associated with Abhinav Bharat.",
            ),
            (
                "European propaganda network",
                "Madame Bhikaji Cama and S.R. Rana worked through Paris and European "
                "platforms; Cama's Stuttgart flag episode occurred in 1907.",
            ),
            (
                "Delhi-Hardinge conspiracy",
                "On 23 December 1912 a bomb was thrown at Viceroy Hardinge in Delhi; "
                "Rash Behari Bose and Sachin Sanyal were linked to the wider network.",
            ),
            (
                "Pacific coast groundwork",
                "Before Ghadar, Tarak Nath Das published Free Hindustan and G.D. Kumar "
                "published Swadesh Sevak among Indian migrants on the Pacific coast.",
            ),
            (
                "Hindi Association of the Pacific Coast",
                "The Hindi Association of the Pacific Coast was organised in May 1913 "
                "with Sohan Singh Bhakna as president and Lala Har Dayal as a key leader.",
            ),
            (
                "Ghadar paper and Yugantar Ashram",
                "The Ghadar paper appeared first in Urdu in late 1913, followed by a "
                "Gurmukhi edition, from the Yugantar Ashram printing centre.",
            ),
            (
                "Ghadar social base and idiom",
                "Ghadar drew heavily on Punjabi migrant workers and ex-soldiers and "
                "used a secular, republican and egalitarian anti-imperial idiom.",
            ),
            (
                "Komagata Maru",
                "The Komagata Maru episode of 1914 exposed racial exclusion and "
                "sharpened diasporic anger without requiring unsupported casualty totals.",
            ),
            (
                "February 1915 rising plan",
                "A Punjab military rising planned for 19 February 1915 was pre-empted "
                "after intelligence penetration; it was an attempted revolt, not a "
                "successful general insurrection.",
            ),
            (
                "Berlin Committee and Kabul",
                "The Berlin or Indian Independence Committee sought German assistance "
                "during the First World War and supported a provisional-government "
                "attempt at Kabul; Hindu-German conspiracy is an umbrella judicial label.",
            ),
            (
                "Singapore mutiny",
                "The Singapore mutiny began on 15 February 1915 in the wider wartime "
                "setting, but it should not be reduced to a simple Ghadar operation.",
            ),
            (
                "Repression, limits and transition",
                "The Defence of India Act 1915, Lahore prosecutions and surveillance "
                "crippled networks; Bagha Jatin died near Balasore in 1915, while "
                "Home Rule, Lucknow and Gandhi's 1917 satyagraha signalled a shift.",
            ),
        ],
        [
            "Anushilan Samiti and Jugantar overlapped in milieu but were not the "
            "same organisation.",
            "The Muzaffarpur action and the Alipore Bomb Case are connected but not "
            "identical events.",
            "Kingsford was the intended Muzaffarpur target; two European women were "
            "the actual victims.",
            "India House was founded by Shyamji Krishna Varma, not by Savarkar.",
            "Madame Cama belonged to European propaganda networks and did not found "
            "the Ghadar organisation.",
            "Ghadar was the organisation and Ghadar was also its paper; identify the "
            "party-paper distinction from context.",
            "The Singapore mutiny belongs to the wider wartime crisis and must not "
            "be described simply as a Ghadar mutiny.",
            "Do not project the later HSRA's explicit socialism backward onto Phase I.",
        ],
        [
            (
                10,
                "Why did some nationalists turn from Swadeshi mobilisation to "
                "clandestine armed action after 1907?",
                "Repression and the decline of open Swadeshi politics encouraged a "
                "vanguard strategy of exemplary action, but did not mechanically "
                "produce every revolutionary network.",
                [2, 3, 4, 5, 19],
            ),
            (
                10,
                "Distinguish the organisation, newspaper and social base of Ghadar.",
                "Ghadar joined a Pacific-coast migrant organisation, a multilingual "
                "paper and a worker-ex-soldier constituency in a secular republican "
                "programme of return and revolt.",
                [11, 12, 13, 14],
            ),
            (
                15,
                "Examine the regional diversity of early revolutionary nationalism.",
                "Bengal cells, Maharashtra's Abhinav Bharat, north Indian networks "
                "and overseas centres shared armed anti-imperialism but differed in "
                "organisation, constituency and tactical opportunity.",
                [0, 1, 2, 3, 8, 10, 11, 12],
            ),
            (
                15,
                "How did overseas networks transform Indian revolutionary politics "
                "before and during the First World War?",
                "London, Paris, the Pacific coast, Berlin and Kabul linked propaganda, "
                "migration, arms and wartime diplomacy, making Indian anti-colonialism "
                "a transnational security problem for the empire.",
                [6, 7, 9, 11, 12, 13, 15, 17],
            ),
            (
                20,
                "Assess the achievements and organisational limits of revolutionary "
                "nationalism during 1907-1917.",
                "The movement broke the psychology of submission, created martyrs and "
                "international networks, yet secrecy, informers, fragmented command "
                "and a weak mass base prevented a sustained challenge to state power.",
                [2, 4, 5, 7, 10, 14, 16, 17, 18, 19],
            ),
            (
                20,
                "Compare the revolutionary vanguard strategy with the Gandhian mass "
                "politics that emerged after 1917.",
                "Both sought courage, sacrifice and anti-colonial mobilisation, but "
                "Gandhian politics replaced secret selective violence with open, "
                "disciplined and wider non-violent participation.",
                [14, 16, 19],
            ),
        ],
        [
            (
                "2022",
                "Prelims GS-I Q53",
                "Assess the association of Barindra Kumar Ghosh, Jogesh Chandra "
                "Chatterjee and Rash Behari Bose with the Ghadar Party.",
                "open-evidence-gap",
                "The routed local question is verified, but its official answer key "
                "is unavailable locally. Preserve it as an association-check card: "
                "Barindra belongs to Bengal's revolutionary milieu, Rash Behari later "
                "worked with the wartime rising, and no option is declared from memory.",
            ),
        ],
        [
            "Anushilan Samiti",
            "Jugantar",
            "Muzaffarpur",
            "Alipore Bomb Case",
            "Shyamji Krishna Varma",
            "Curzon-Wyllie",
            "A.M.T. Jackson",
            "Yugantar Ashram",
            "Komagata Maru",
            "19 February 1915",
            "Defence of India Act 1915",
            "Singapore mutiny",
        ],
    ),
    base.topic(
        17,
        "Growth of Communalism & the Muslim League",
        "17_Growth-of-Communalism-and-Muslim-League.md",
        "17_Growth-of-Communalism-and-Muslim-League.md",
        "17_Growth-of-Communalism-and-Muslim-League_Complete-Topic-Package.md",
        [
            "basic/15_Militant-Nationalism-and-Swadeshi.md",
            "basic/18_WWI-Home-Rule-and-Lucknow-Pact.md",
            "basic/20_Non-Cooperation-and-Khilafat-Movement.md",
            "basic/22_Simon-Nehru-Report-CDM-and-RTC.md",
            "basic/27_Independence-and-Partition.md",
        ],
        ["https://elibrary.sansad.in/"],
        "Parliament Digital Library is retained only as a constitutional archive "
        "bridge. No present-day party position is used as evidence for colonial "
        "communalism or the decisions that culminated in Partition.",
        "OCR checks use Bipan Chandra's Modern India and India's Struggle for "
        "Independence for the modernist definition, constitutional incentives, "
        "League development, Congress-League relations and the 1940-47 endgame. "
        "Sekhar Bandyopadhyay supplies provincial and coalition qualifications.",
        "The verified and routed 2018 GS-I Q20 on power struggle and relative "
        "deprivation is solved as a direct Mains question. The provisional local "
        "key for 2026 Prelims Q18 is not treated as official; that demand remains "
        "a verification and evidence-gap card.",
        [
            (
                "Modern political ideology",
                "Communalism is a modern political ideology that treats religious "
                "communities as bearers of separate secular interests; it is not "
                "religious faith or timeless hostility.",
            ),
            (
                "1857 caution",
                "Shared Hindu-Muslim participation in parts of the 1857 rebellion "
                "undermines any claim that later communal division was historically "
                "automatic or politically homogeneous.",
            ),
            (
                "Colonial categorisation",
                "Census classification, patronage, constitutional categories and "
                "representation by community helped make religious identity a field "
                "of organised political claim-making.",
            ),
            (
                "Aligarh and elite loyalism",
                "From the 1870s-80s, Syed Ahmad Khan's educational project was joined "
                "in his later politics by elite loyalism and caution toward Congress.",
            ),
            (
                "Partition of Bengal",
                "The 1905 partition created divergent political responses and gave "
                "communal and regional claims greater institutional and public weight.",
            ),
            (
                "Simla Deputation",
                "On 1 October 1906 the Simla Deputation led by the Aga Khan sought "
                "separate Muslim representation from Viceroy Minto.",
            ),
            (
                "Muslim League foundation",
                "The All-India Muslim League was founded at Dhaka on 30 December 1906 "
                "by elite leaders seeking safeguards and influence within the Raj.",
            ),
            (
                "Separate electorates",
                "The Indian Councils Act 1909 introduced separate electorates for "
                "Muslims, giving community-specific electoral appeals a constitutional "
                "incentive.",
            ),
            (
                "League self-government goal",
                "In 1913 the Muslim League adopted self-government under the British "
                "Crown as an objective, enabling closer constitutional cooperation.",
            ),
            (
                "Hindu Mahasabha",
                "The All-India Hindu Mahasabha emerged in 1915; its placement within "
                "Hindu communal politics should be stated as a historical interpretation.",
            ),
            (
                "Lucknow Pact",
                "The Congress-League Lucknow Pact of 1916 achieved cooperation on "
                "reform while Congress accepted separate electorates and agreed "
                "representation safeguards.",
            ),
            (
                "Khilafat and Non-Cooperation",
                "The Khilafat-Non-Cooperation alliance of 1920-22 produced major "
                "political unity, but its breakdown did not dissolve communal "
                "organisations or local conflict.",
            ),
            (
                "Hindutva and RSS",
                "Savarkar's Hindutva appeared in 1923 and the RSS was founded in 1925; "
                "neither should be treated as representing all Hindu political opinion.",
            ),
            (
                "Nehru Report and Fourteen Points",
                "The Nehru Report of 1928 and Jinnah's Fourteen Points of 1929 exposed "
                "conflict over federation, residuary powers and minority safeguards.",
            ),
            (
                "Communal Award",
                "The Communal Award of 1932 extended community-based representation; "
                "separate electorates, reserved seats and nomination must remain "
                "analytically distinct.",
            ),
            (
                "Government of India Act 1935",
                "The Government of India Act 1935 created provincial autonomy and an "
                "electoral arena in which provincial coalitions and community claims "
                "interacted.",
            ),
            (
                "1937 elections and ministries",
                "The 1937 elections exposed the League's uneven provincial strength; "
                "Congress ministries and failed coalition bargaining later became "
                "central to competing political narratives.",
            ),
            (
                "Lahore Resolution",
                "On 23 March 1940 the League adopted the Lahore Resolution calling for "
                "independent states in Muslim-majority zones; the text did not use "
                "the word Pakistan.",
            ),
            (
                "1945-46 mandate and Cabinet Mission",
                "The 1945-46 elections strengthened the League's claim among Muslim "
                "electorates; the Cabinet Mission statement of 16 May 1946 proposed "
                "a united union with grouped provinces.",
            ),
            (
                "1946-47 endgame",
                "Direct Action Day on 16 August 1946, failed constitutional bargaining, "
                "the 3 June 1947 Plan and the Indian Independence Act led to Partition; "
                "no single actor or timeless community explains the outcome.",
            ),
        ],
        [
            "Communalism is not a synonym for religion, religiosity or a communal riot.",
            "Colonial policy institutionalised communal categories but did not alone "
            "invent every communal organisation or political choice.",
            "The Muslim League did not demand Pakistan from its foundation in 1906.",
            "Separate electorates began for Muslims in 1909, not at Lucknow in 1916.",
            "The Lahore Resolution used 'independent states' and did not use the word "
            "Pakistan.",
            "Muslims, Hindus, Congress, the League and the provinces were never "
            "internally homogeneous political blocs.",
            "Reserved seats, nomination, weightage and separate electorates are "
            "different constitutional devices.",
            "Avoid uncited casualty totals and single-cause blame for Partition.",
        ],
        [
            (
                10,
                "Why must communalism be analysed as a modern political ideology "
                "rather than as religious faith?",
                "Communalism translates religious identity into claims about secular "
                "political interests through modern organisations, representation "
                "and competition; devotion alone does not perform that work.",
                [0, 1, 2, 3],
            ),
            (
                10,
                "How did separate electorates alter the incentives of colonial "
                "constitutional politics?",
                "Separate electorates rewarded community-specific claim-making and "
                "made safeguards, weightage and recognised spokesmen recurring terms "
                "of negotiation without making later outcomes inevitable.",
                [5, 6, 7, 10, 14],
            ),
            (
                15,
                "Trace the Muslim League's evolution from elite safeguards to mass "
                "electoral mobilisation.",
                "The League moved from loyalist safeguards through constitutional "
                "cooperation and uneven provincial influence to post-1937 mobilisation "
                "and the Muslim-electorate mandate of 1945-46.",
                [6, 8, 10, 13, 16, 17, 18],
            ),
            (
                15,
                "Assess the achievements and contradictions of Congress-League unity "
                "from Lucknow to the Khilafat-Non-Cooperation phase.",
                "The alliances demonstrated that joint action was possible, but "
                "Lucknow relied on communal representation and the later coalition "
                "could not replace continuous secular organisation.",
                [10, 11],
            ),
            (
                20,
                "Why did communal politics develop differently in the United "
                "Provinces, Punjab, Bengal and the North-West Frontier Province?",
                "Provincial social structures, parties, landholding, coalition options "
                "and state institutions mediated all-India communal claims, preventing "
                "a uniform national trajectory.",
                [2, 15, 16, 18],
            ),
            (
                20,
                "Was Partition inevitable after the Lahore Resolution of 1940?",
                "The resolution changed the bargaining field but Cripps, the "
                "Gandhi-Jinnah talks, Simla and the Cabinet Mission show continuing "
                "contingency; war, elections, failed coalitions and violence narrowed "
                "the available alternatives.",
                [17, 18, 19],
            ),
        ],
        [
            (
                "2018",
                "GS-I Q20",
                "'Communalism arises either due to power struggle or relative "
                "deprivation.' Argue by giving suitable illustrations. "
                "(15 marks, 250 words)",
                "model-solution",
                "Power struggle explains how elites and organisations compete for "
                "office, representation and authority; relative deprivation explains "
                "how perceived loss against another group makes such appeals credible. "
                "Colonial electorates, scarce services and provincial coalition "
                "competition could join both mechanisms. Neither religious difference "
                "nor deprivation automatically creates communalism: political actors "
                "frame grievances, institutions reward some claims, and regional "
                "conditions shape outcomes. The two causes therefore interact rather "
                "than operate as exclusive explanations.",
            ),
            (
                "2026",
                "Prelims GS-I Q18",
                "Assess the statements concerning the Montagu-Chelmsford reforms, "
                "separate electorates and community-based political alliances.",
                "provisional-key-evidence-gap",
                "The routed demand is locally recorded and a provisional Set-A key "
                "exists, but no official final key is held. Use it only to verify the "
                "distinctions among separate electorates, reserved seats, nomination "
                "and political alliances; do not publish an answer letter.",
            ),
        ],
        [
            "modern political ideology",
            "Simla Deputation",
            "30 December 1906",
            "Indian Councils Act 1909",
            "Lucknow Pact",
            "Fourteen Points",
            "Communal Award",
            "Government of India Act 1935",
            "23 March 1940",
            "independent states",
            "Cabinet Mission",
            "regional variation",
        ],
    ),
]


SESSION_PLANS: dict[str, list[tuple[str, str, list[str], str, str]]] = {
    "modern-indian-history-16": [
        (
            "Boundary, chronology and theatre map",
            "Phase I links the armed aftermath of Swadeshi to the wartime conspiracies "
            "of 1914-15 and closes with the political transition of 1916-17.",
            [
                "The 1897 Chapekar action is a precursor, not the formal beginning of a single organisation.",
                "The principal theatres were Bengal, Maharashtra, north India, London, Paris, the Pacific coast, Berlin and Kabul.",
                "The movement combined local cells with transnational print, migration and wartime diplomacy.",
            ],
            "Do not flatten separate organisations and theatres into one central command.",
            "Open a Mains answer with period, geography, repertoire and the distinction from later HSRA politics.",
        ),
        (
            "Swadeshi repression and the armed turn",
            "The decline of open Swadeshi mobilisation created conditions in which "
            "some younger nationalists chose clandestine action and exemplary sacrifice.",
            [
                "Repression, arrests and restrictions narrowed lawful political space after 1907.",
                "Militant self-reliance and sacrifice supplied continuity with Swadeshi.",
                "Secret action was a strategic choice, not an automatic reaction shared by all nationalists.",
            ],
            "Do not explain revolutionary nationalism as temperament or as Swadeshi's total replacement.",
            "Use a condition-to-choice argument: repression mattered, but ideology and organisation mediated it.",
        ),
        (
            "Revolutionary theory, methods and social ceiling",
            "The vanguard expected selected action to break fear, inspire emulation and "
            "prepare a broader rising against colonial authority.",
            [
                "Methods included secret cells, propaganda, physical training, arms procurement and targeted attacks.",
                "Wartime plans added military revolt and foreign assistance to the repertoire.",
                "Secrecy protected planning but restricted recruitment and magnified the damage caused by informers.",
            ],
            "Heroic violence did not by itself create a mass organisation or coordinated national command.",
            "Judge the theory through intended mechanism, actual psychological effect and organisational limit.",
        ),
        (
            "Anushilan, Dacca Anushilan and Jugantar",
            "Bengal contained overlapping revolutionary milieus rather than one "
            "interchangeable organisation.",
            [
                "Anushilan Samiti and Dacca Anushilan developed connected but distinct organisational histories.",
                "Barindra Ghosh's circle, Jugantar and the Maniktala garden formed a major revolutionary centre.",
                "Jugantar the network and Jugantar the newspaper must be read from context.",
                "Sandhya and Bande Mataram widened militant political communication without becoming the same body.",
            ],
            "Anushilan is not simply another name for Jugantar.",
            "A strong answer maps organisation, publication, leader and action separately.",
        ),
        (
            "Muzaffarpur action and Alipore prosecution",
            "The April 1908 Muzaffarpur attack and the 1908-09 Alipore Bomb Case were "
            "causally linked but legally and factually distinct.",
            [
                "Khudiram Bose and Prafulla Chaki intended to attack Kingsford.",
                "The bomb instead killed two European women; intended target and actual victims must be separated.",
                "The Alipore prosecution focused on the wider Maniktala conspiracy and Barindra's circle.",
                "The trial created public memory and courtroom politics beyond the immediate attack.",
            ],
            "Never write that Kingsford was killed or that Alipore was the name of the bombing.",
            "Use the pair to show action, unintended outcome, network exposure and colonial prosecution.",
        ),
        (
            "Maharashtra, Abhinav Bharat and the Nasik case",
            "Maharashtra's current joined the Chapekar precedent to Savarkar's "
            "oath-bound organisation and the Nasik conspiracy.",
            [
                "Mitra Mela developed into Abhinav Bharat in 1904.",
                "Savarkar connected ideological writing, India House and revolutionary organisation.",
                "Anant Kanhere killed A.M.T. Jackson at Nasik in December 1909.",
                "The Nasik prosecution exposed connections without proving one all-India command.",
            ],
            "Do not merge the 1897 Poona killings, Abhinav Bharat's formation and the 1909 Nasik action.",
            "Compare regional organisation while preserving distinct chronologies.",
        ),
        (
            "India House identity and London confrontation",
            "India House gave students and exiles a London centre for political "
            "education, publishing and revolutionary contact.",
            [
                "Shyamji Krishna Varma founded India House and published the Indian Sociologist.",
                "Savarkar became a central organiser but was not the founder.",
                "Madan Lal Dhingra killed Curzon-Wyllie on 1 July 1909.",
                "The action intensified surveillance and dispersed parts of the London network.",
            ],
            "Match founder, later organiser, publication and assassination correctly.",
            "Use India House to explain how imperial centres also became anti-imperial political spaces.",
        ),
        (
            "European propaganda and diplomatic space",
            "Paris and continental Europe enabled propaganda, asylum and international "
            "visibility beyond the tighter policing of London.",
            [
                "Madame Bhikaji Cama and S.R. Rana sustained exile and publication networks.",
                "Cama displayed an Indian nationalist flag at Stuttgart in 1907.",
                "European platforms internationalised the critique of British rule.",
                "Propaganda networks should be distinguished from the later Ghadar organisation.",
            ],
            "Madame Cama did not found Ghadar.",
            "Treat flags, journals and congress platforms as political communication, not decorative biography.",
        ),
        (
            "Pacific migration before Ghadar",
            "Racial exclusion, labour migration and political print created the social "
            "and communicative infrastructure from which Ghadar emerged.",
            [
                "Punjabi workers and ex-soldiers formed a major migrant constituency on the Pacific coast.",
                "Tarak Nath Das's Free Hindustan circulated anti-colonial argument.",
                "G.D. Kumar's Swadesh Sevak linked migrant grievance with politics.",
                "The network preceded the formal Hindi Association of the Pacific Coast.",
            ],
            "Do not begin the overseas story only with the Ghadar paper in late 1913.",
            "Explain how migration, racial exclusion and print converted grievance into organisation.",
        ),
        (
            "Ghadar organisation, paper and programme",
            "Ghadar united a migrant-worker base, a printing centre and a programme of "
            "secular republican revolt.",
            [
                "The Hindi Association of the Pacific Coast was organised in May 1913.",
                "Sohan Singh Bhakna was president and Lala Har Dayal a key ideologue and organiser.",
                "Yugantar Ashram served as headquarters and printing centre.",
                "The Urdu Ghadar issue appeared first in late 1913 and a Gurmukhi edition followed.",
                "Kartar Singh Sarabha became an important young organiser.",
            ],
            "Ghadar may denote the movement and the paper; the Hindi Association was the organisational origin.",
            "Connect social base, medium, ideology and planned return rather than listing names.",
        ),
        (
            "Komagata Maru and racial exclusion",
            "The Komagata Maru episode exposed the racial boundary of imperial "
            "citizenship and sharpened anger among overseas Indians in 1914.",
            [
                "The voyage challenged exclusionary Canadian immigration practice.",
                "Its forced return became a powerful grievance within the wartime diaspora.",
                "The episode fed Ghadar mobilisation but was not created by Ghadar.",
                "The historical argument does not require disputed or unsupported casualty totals.",
            ],
            "Do not substitute an unverified casualty number for the institutional issue of exclusion.",
            "Use the incident as a bridge from diaspora grievance to wartime return and revolt planning.",
        ),
        (
            "February 1915 plan and failure funnel",
            "Ghadar activists returned during the First World War and tried to convert "
            "military discontent into a coordinated Punjab rising.",
            [
                "The planned date was shifted under pressure and the 19 February 1915 rising was pre-empted.",
                "Intelligence penetration and informers exposed the timetable and participants.",
                "Weak coordination across cantonments prevented simultaneous action.",
                "Lahore conspiracy prosecutions followed the failed plan.",
            ],
            "Describe an attempted rising, not a successful nationwide mutiny.",
            "The failure funnel is intelligence penetration plus coordination weakness plus limited mass support.",
        ),
        (
            "Berlin, Kabul and Singapore in the wartime network",
            "The war widened revolutionary strategy toward German assistance, "
            "Afghanistan and military unrest across the empire.",
            [
                "The Berlin or Indian Independence Committee sought foreign support against Britain.",
                "The Kabul provisional-government attempt aimed at diplomatic and frontier leverage.",
                "Hindu-German conspiracy is an umbrella and judicial label, not one uniform organisation.",
                "The Singapore mutiny began on 15 February 1915 but was not simply a Ghadar operation.",
            ],
            "Shared wartime context does not establish identical command or membership.",
            "Map each node by purpose: assistance, diplomacy, infiltration or military revolt.",
        ),
        (
            "Repression, law and network attrition",
            "The colonial state combined surveillance, informers, special law, trials "
            "and armed pursuit to break small clandestine networks.",
            [
                "The Defence of India Act 1915 expanded extraordinary wartime powers.",
                "Lahore conspiracy trials imposed severe punishment on the Ghadar network.",
                "Earlier Alipore and Nasik prosecutions showed the importance of conspiracy law.",
                "Bagha Jatin died after an armed encounter near Balasore in 1915.",
            ],
            "Avoid undifferentiated claims that one law caused every arrest in the phase.",
            "Show why small secret cells were especially vulnerable to penetration and exemplary prosecution.",
        ),
        (
            "Achievement, limits, Gandhian shift and PYQ route",
            "Revolutionary nationalism transformed morale, martyr memory and the "
            "geography of resistance, but did not displace the need for mass politics.",
            [
                "Its achievements were psychological defiance, sacrifice, internationalisation and pressure on the state.",
                "Its limits were fragmentation, informers, scarce resources and weak peasant-worker organisation in India.",
                "Home Rule and Lucknow in 1916 and Gandhi's 1917 satyagraha marked a move toward open mobilisation.",
                "Continuity lay in courage and sacrifice; discontinuity lay in non-violence, openness and mass discipline.",
                "UPSC 2022 Q53 remains a Ghadar association card with an unavailable local official key.",
            ],
            "Do not claim a simple causal path in which revolutionary failure automatically produced Gandhi.",
            "Conclude with a graded judgement: large symbolic impact, limited capacity to seize or hold power.",
        ),
    ],
    "modern-indian-history-17": [
        (
            "Definition ladder: religion, community and communalism",
            "Communalism begins when religious identity is converted into a claim "
            "about common secular interests and can intensify into hostility.",
            [
                "Religion and religiosity do not by themselves constitute communalism.",
                "Bipan Chandra's first stage assumes common secular interests among co-religionists.",
                "The second sees interests of communities as divergent; the third treats them as antagonistic.",
                "The stages are an attributed modernist interpretation, not a timeless law.",
            ],
            "Do not use communalism as a synonym for faith, reform or riot.",
            "Define the ideology before narrating organisations or constitutional events.",
        ),
        (
            "Precolonial caution and the 1857 counterexample",
            "Religious difference existed before colonial rule, but modern communal "
            "politics cannot be read backward as an unbroken civilisational conflict.",
            [
                "The 1857 rebellion included important zones of shared Hindu-Muslim political action.",
                "Local conflicts and religious idioms did not amount to modern electoral communalism.",
                "Modern organisations, print publics and representative institutions altered the political form.",
                "Neither Hindus nor Muslims ever acted as internally uniform blocs.",
            ],
            "Avoid both primordial hostility and a romantic claim of permanent precolonial harmony.",
            "Use continuity of difference plus discontinuity of political form as the balanced argument.",
        ),
        (
            "Colonial state and layered causation",
            "Colonial institutions interacted with social competition and political "
            "choices; no single layer alone explains communal growth.",
            [
                "Enumeration and census made communities legible administrative categories.",
                "Patronage and constitutional representation rewarded recognised spokesmen.",
                "Uneven education and scarce employment intensified elite competition.",
                "Press and associations converted grievances into organised community claims.",
                "Congress, League, provincial parties and British governments made contingent choices within this field.",
            ],
            "The British-invented-only thesis removes Indian agency and regional variation.",
            "Build a layered answer: state design plus material competition plus organised politics plus contingency.",
        ),
        (
            "Aligarh, education and elite loyalism",
            "The Aligarh movement addressed educational disadvantage, while Syed "
            "Ahmad Khan's later politics stressed loyalism and caution toward Congress.",
            [
                "Educational reform and communal politics must not be treated as identical.",
                "Uneven access to English education affected competition for offices and professions.",
                "Elite anxiety encouraged demands for safeguards and recognised representation.",
                "Muslim opinion also contained Deobandi, nationalist, regional and class alternatives.",
            ],
            "Do not make Aligarh or Syed Ahmad Khan the sole origin of Muslim politics.",
            "Explain how educational context could support, but did not predetermine, political loyalism.",
        ),
        (
            "Partition, Simla Deputation and separate electorates, 1905-09",
            "The sequence from Bengal partition to elite deputation, League formation "
            "and separate electorates institutionalised a new politics of safeguards.",
            [
                "The 1905 Bengal partition generated divergent regional and community responses.",
                "The Simla Deputation met Minto on 1 October 1906 and sought separate representation.",
                "The League was founded at Dhaka on 30 December 1906.",
                "The Indian Councils Act 1909 introduced separate electorates for Muslims.",
            ],
            "Do not collapse the deputation, League foundation and statutory concession into one event.",
            "Use chronology to show claim-making, organisation and constitutional reward.",
        ),
        (
            "Muslim League life-cycle",
            "The League changed from an elite loyalist safeguard body into a wider "
            "electoral claimant; its 1906 character cannot explain its 1946 position.",
            [
                "The early League sought safeguards and influence within colonial government.",
                "Its 1913 self-government objective enabled closer cooperation with Congress.",
                "Its position was uneven in the 1920s and weak in several provinces before 1937.",
                "After 1937 it expanded mobilisation and reframed provincial and all-India grievances.",
                "The 1945-46 elections strengthened its claim among Muslim electorates.",
            ],
            "The League did not demand Pakistan from its foundation.",
            "Periodise organisational aims, social reach and bargaining position.",
        ),
        (
            "Lucknow Pact: cooperation through a communal ledger",
            "The 1916 Pact showed that Congress-League agreement was possible while "
            "also confirming separate electorates as the currency of negotiation.",
            [
                "Congress and League supported a joint constitutional reform programme.",
                "Congress accepted separate electorates and negotiated representation safeguards.",
                "The pact widened nationalist unity during the Home Rule and wartime setting.",
                "Its tactical gain and institutional concession must be assessed together.",
            ],
            "Lucknow neither introduced separate electorates nor permanently ended communal politics.",
            "Frame it as unity on communal terms rather than as simple success or betrayal.",
        ),
        (
            "Khilafat-Non-Cooperation unity and breakdown",
            "The 1920-22 alliance achieved unusually broad joint mobilisation but did "
            "not create durable secular organisation beneath the coalition.",
            [
                "Congress connected Non-Cooperation with the Khilafat grievance.",
                "Joint action demonstrated that religiously framed issues could enter anti-colonial mobilisation.",
                "Withdrawal and the changing Turkish context weakened the alliance.",
                "Subsequent riots and organisational rivalry exposed the limits of episodic unity.",
            ],
            "Do not say that Khilafat either permanently solved or single-handedly caused communalism.",
            "Distinguish mobilisation success from long-term ideological transformation.",
        ),
        (
            "The 1920s: Hindu and Muslim communal organisations",
            "Post-Khilafat politics saw competing organisations, press campaigns and "
            "identity consolidation, but neither community became politically uniform.",
            [
                "The Hindu Mahasabha had emerged in 1915 and expanded organised Hindu claims.",
                "Savarkar's Hindutva appeared in 1923 and the RSS was founded in 1925.",
                "Muslim politics included the League, ulema, regional parties and nationalist Muslims.",
                "Local riots and elite competition varied by province and issue.",
            ],
            "Use historiographical caution rather than treating all organisations as identical.",
            "Compare shared communal logic while preserving different structures, programmes and constituencies.",
        ),
        (
            "Nehru Report and Fourteen Points",
            "The 1928-29 exchange concentrated disputes over federation, residuary "
            "powers, representation and safeguards.",
            [
                "The Nehru Report proposed a constitutional framework without separate electorates in its final design.",
                "Jinnah's Fourteen Points answered with federal and minority safeguards.",
                "The dispute reflected failed bargaining, not an already completed demand for Partition.",
                "Constitutional form and political trust interacted.",
            ],
            "Do not read the Fourteen Points as identical to the Lahore Resolution.",
            "Use a side-by-side matrix of centre, provinces, electorates and safeguards.",
        ),
        (
            "Communal Award and Government of India Act 1935",
            "The 1930s expanded representative arenas while preserving multiple forms "
            "of community and interest representation.",
            [
                "The Communal Award of 1932 extended community-based representation.",
                "Separate electorates, reserved seats, nomination and weightage are distinct devices.",
                "The Government of India Act 1935 established provincial autonomy.",
                "Provincial elections made coalition strategy and ministries decisive political tests.",
            ],
            "Do not treat every reserved or nominated seat as a separate electorate.",
            "Explain how constitutional design created incentives but did not dictate one electoral result.",
        ),
        (
            "Representation table and Hindu communal caution",
            "Communal analysis must identify organisations and incentives without "
            "assigning collective guilt to religious populations.",
            [
                "The Hindu Mahasabha and RSS belong to analyses of organised Hindu communal politics.",
                "Congress contained Hindu cultural idioms but officially claimed territorial nationalism.",
                "Muslim parties and publics remained divided by province, class, sect and strategy.",
                "The same organisation could change programme and coalition behaviour over time.",
            ],
            "Congress, Hindu society, Hindu communal organisations and all Hindus are not interchangeable.",
            "Name the organisation, period, constituency and claim instead of writing community-wide abstractions.",
        ),
        (
            "1937 elections and provincial variation",
            "The 1937 elections exposed the gap between all-India claims and provincial "
            "politics in the United Provinces, Punjab, Bengal and the NWFP.",
            [
                "The League's performance was uneven and regional parties retained major influence.",
                "The Congress-League coalition dispute in the United Provinces became politically consequential.",
                "Punjab and Bengal had agrarian, landed and coalition structures unlike the United Provinces.",
                "The North-West Frontier Province did not fit a simple League-versus-Congress binary.",
            ],
            "Do not infer uniform Muslim support for the League from its later 1945-46 mandate.",
            "Provincial comparison is the best safeguard against an all-India teleology.",
        ),
        (
            "Lahore Resolution, war and bargaining, 1940-45",
            "The Lahore Resolution changed the bargaining framework during wartime, "
            "but multiple constitutional possibilities remained under negotiation.",
            [
                "The resolution was adopted on 23 March 1940.",
                "It referred to independent states in Muslim-majority zones and did not use the word Pakistan.",
                "Cripps in 1942, Gandhi-Jinnah talks in 1944 and the Simla Conference in 1945 show continued bargaining.",
                "War altered British dependence, Congress strategy and League organisational opportunity.",
            ],
            "Do not make 1940 proof that Partition had become inevitable.",
            "Assess the resolution as a major shift whose practical meaning remained contested.",
        ),
        (
            "1945-47 endgame and historiographical matrix",
            "Electoral mandate, failed federal bargaining, violence and accelerated "
            "British withdrawal narrowed alternatives between 1945 and 1947.",
            [
                "The 1945-46 elections strengthened the League among Muslim electorates.",
                "The Cabinet Mission statement of 16 May 1946 proposed a union and provincial grouping.",
                "Direct Action Day on 16 August 1946 and subsequent violence deepened political breakdown.",
                "The 3 June Plan and Indian Independence Act implemented Partition in 1947.",
                "Bipan Chandra stresses ideology and instrumental politics; regional studies stress coalitions; Jalal-type readings stress bargaining and contingency.",
                "The verified 2018 GS-I question requires power struggle and relative deprivation to be argued together.",
            ],
            "Avoid British-only, Congress-only, League-from-1906 and timeless-hostility explanations.",
            "Conclude with multi-causality and contingency, not collective blame or uncited casualty figures.",
        ),
    ],
}


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-16": [
        (
            "Layered chronology from precursor to political transition",
            "chronology",
            """1897 CHAPEKAR -> armed precursor in Poona
1904-09 CELLS -> Abhinav Bharat, Bengal networks, London and Nasik
1912-13 EXPANSION -> Hardinge conspiracy and Pacific-coast Ghadar
1914-15 WAR -> return plan, Berlin-Kabul links and Singapore context
1915 REPRESSION -> Defence of India Act, Lahore trials and Balasore
1916-17 SHIFT -> Home Rule, Lucknow and open Gandhian satyagraha.""",
            ["Boundary, chronology and theatre map", "Repression, law and network attrition"],
        ),
        (
            "Transnational revolutionary network",
            "network-map",
            """BENGAL -> Anushilan, Dacca Anushilan, Barindra and Jugantar
MAHARASHTRA -> Mitra Mela, Abhinav Bharat and Nasik
DELHI -> Rash Behari Bose, Sachin Sanyal and Hardinge attack
LONDON / PARIS -> India House, Indian Sociologist, Cama and S.R. Rana
PACIFIC -> Free Hindustan, Swadesh Sevak, Yugantar Ashram and Ghadar
BERLIN / KABUL -> wartime assistance and provisional-government attempt.""",
            ["Boundary, chronology and theatre map", "Berlin, Kabul and Singapore in the wartime network"],
        ),
        (
            "Organisation, publication, leader and arena matrix",
            "comparison",
            """ANUSHILAN -> Bengal network; not identical to Jugantar
JUGANTAR -> network plus newspaper; context decides the meaning
INDIA HOUSE -> founded by Shyamji; Savarkar became a key organiser
GHADAR -> organisation and paper; Hindi Association was the origin
CAMA / S.R. RANA -> European propaganda, not Ghadar founders
EXAM RULE -> match actor + institution + publication + place.""",
            ["Anushilan, Dacca Anushilan and Jugantar", "India House identity and London confrontation"],
        ),
        (
            "From repression to exemplary action",
            "causal-flow",
            """SWADESHI DECLINE + REPRESSION -> impatience with open politics
SECRET CELL -> discipline, training, propaganda and arms
TARGETED ACTION -> break fear and dramatise colonial vulnerability
EXPECTED EFFECT -> public courage and wider rising
ACTUAL CEILING -> secrecy, weak mass organisation and fragmented command
VERDICT -> strategic choice with symbolic reach, not automatic succession.""",
            ["Swadeshi repression and the armed turn", "Revolutionary theory, methods and social ceiling"],
        ),
        (
            "Muzaffarpur action to Alipore prosecution",
            "procedure-sequence",
            """APR 1908 -> Khudiram Bose and Prafulla Chaki target Kingsford
ACTUAL RESULT -> two European women are killed; Kingsford survives
INVESTIGATION -> Maniktala garden and wider circle exposed
1908-09 ALIPORE -> conspiracy prosecution of Barindra-linked network
PUBLIC EFFECT -> martyr memory and courtroom politics
TRAP -> the attack and the case are connected, not identical.""",
            ["Muzaffarpur action and Alipore prosecution"],
        ),
        (
            "Abhinav Bharat and the Nasik sequence",
            "chronology",
            """1897 POONA -> Chapekar precursor
MITRA MELA -> Savarkar's early association
1904 ABHINAV BHARAT -> oath-bound revolutionary organisation
DEC 1909 NASIK -> Anant Kanhere kills A.M.T. Jackson
PROSECUTION -> links and arms networks investigated
TRAP -> keep Poona, organisation and Nasik as separate anchors.""",
            ["Maharashtra, Abhinav Bharat and the Nasik case"],
        ),
        (
            "India House identity card",
            "identity-card",
            """FOUNDER -> Shyamji Krishna Varma
PLACE -> London
PUBLICATION -> Indian Sociologist
ORGANISER -> V.D. Savarkar later became central
1 JUL 1909 -> Dhingra kills Curzon-Wyllie
OUTCOME -> surveillance intensifies and the network disperses.""",
            ["India House identity and London confrontation"],
        ),
        (
            "Ghadar print and mobilisation flow",
            "process",
            """MIGRANT GRIEVANCE -> racial exclusion and labour insecurity
EARLY PRINT -> Free Hindustan and Swadesh Sevak
MAY 1913 -> Hindi Association of the Pacific Coast
YUGANTAR ASHRAM -> headquarters and printing centre
LATE 1913 -> Urdu Ghadar first; Gurmukhi edition follows
WAR -> return to India and attempted military rising.""",
            ["Pacific migration before Ghadar", "Ghadar organisation, paper and programme"],
        ),
        (
            "Komagata Maru voyage and political effect",
            "spatial-cross-section",
            """PUNJAB / ASIA -> passengers travel toward Canada
VANCOUVER -> exclusionary immigration regime blocks landing
PACIFIC RETURN -> imperial citizenship claim is denied
BUDGE BUDGE -> coercive colonial reception after return
POLITICAL EFFECT -> diasporic anger feeds wartime mobilisation
EVIDENCE RULE -> explain exclusion; omit unsupported casualty totals.""",
            ["Komagata Maru and racial exclusion"],
        ),
        (
            "The 1915 failure funnel",
            "problem-response",
            """RETURNING ACTIVISTS -> seek support in Punjab and cantonments
PLAN -> coordinated military rising around 19 February 1915
PENETRATION -> informers reveal dates, leaders and locations
DISRUPTION -> arrests and altered plans break coordination
AFTERMATH -> Lahore conspiracy prosecutions
LIMIT -> attempted revolt never becomes a general insurrection.""",
            ["February 1915 plan and failure funnel"],
        ),
        (
            "State repression and special-law ladder",
            "institution-map",
            """SURVEILLANCE -> mail, travel, associations and informers
CONSPIRACY CASES -> Alipore, Nasik and Lahore
WARTIME POWER -> Defence of India Act 1915
ARMED PURSUIT -> Bagha Jatin dies near Balasore in 1915
NETWORK EFFECT -> small cells lose leaders and communications
POLITICAL EFFECT -> repression becomes a later nationalist grievance.""",
            ["Repression, law and network attrition"],
        ),
        (
            "Revolutionary and Gandhian strategy matrix",
            "comparison",
            """REVOLUTIONARY AGENT -> disciplined clandestine vanguard
REVOLUTIONARY METHOD -> selective violence, arms and attempted mutiny
GANDHIAN AGENT -> open, wider and disciplined public participation
GANDHIAN METHOD -> non-violent satyagraha and constructive organisation
CONTINUITY -> courage, sacrifice and refusal of political submission
VERDICT -> symbolic bridge without a deterministic causal succession.""",
            ["Achievement, limits, Gandhian shift and PYQ route"],
        ),
    ],
    "modern-indian-history-17": [
        (
            "Communalism definition ladder",
            "classification",
            """RELIGION -> faith, practice and community life
STAGE 1 -> co-religionists are said to share secular interests
STAGE 2 -> interests are said to diverge from other communities
STAGE 3 -> interests are presented as hostile and irreconcilable
POLITICAL FORM -> organisation, representation and mobilisation
RULE -> communalism is not faith, reform or riot.""",
            ["Definition ladder: religion, community and communalism"],
        ),
        (
            "Layered causation wheel",
            "causal-web",
            """COLONIAL STATE -> census, patronage and constitutional categories
MATERIAL FIELD -> uneven education, jobs and professional opportunity
ELITE ACTION -> press, associations and claims to representation
INSTITUTIONS -> electorates, weightage, safeguards and ministries
CONTINGENCY -> party choices, war, coalitions and failed negotiations
VERDICT -> interacting causes, not timeless hostility or one culprit.""",
            ["Colonial state and layered causation"],
        ),
        (
            "Constitutional rail, 1905-47",
            "chronology",
            """1905-09 -> Bengal partition, Simla, League and separate electorates
1916-19 -> Lucknow bargain and wider communal representation
1928-35 -> Nehru Report, Fourteen Points, Award and provincial autonomy
1937-40 -> elections, ministries and Lahore Resolution
1942-46 -> Cripps, Gandhi-Jinnah, Simla and Cabinet Mission
1947 -> 3 June Plan, Independence Act and Partition.""",
            ["Partition, Simla Deputation and separate electorates, 1905-09", "1945-47 endgame and historiographical matrix"],
        ),
        (
            "Muslim League life-cycle",
            "process",
            """1906 -> elite safeguards and loyalist influence within the Raj
1913 -> self-government objective
1916 -> constitutional cooperation at Lucknow
1920s -> uneven organisation and competing Muslim currents
POST-1937 -> wider mobilisation and ministry grievance narrative
1945-46 -> strong Muslim-electorate mandate; not all-Muslim unanimity.""",
            ["Muslim League life-cycle"],
        ),
        (
            "Separate-electorate incentive loop",
            "feedback-loop",
            """COMMUNITY ELECTORATE -> candidate addresses one recognised electorate
COMMUNAL CLAIM -> leader presents group-specific safeguards
STATE RECOGNITION -> recognised spokesman gains bargaining value
COMPETITION -> rival organisations intensify representative claims
NEGOTIATION -> weightage and seats become recurring demands
LOOP LIMIT -> incentives shape politics but do not predetermine Partition.""",
            ["Partition, Simla Deputation and separate electorates, 1905-09"],
        ),
        (
            "Lucknow Pact ledger",
            "balance-sheet",
            """GAIN -> Congress-League joint constitutional programme
GAIN -> temporary all-India political cooperation
CONCESSION -> Congress accepts separate electorates
BARGAIN -> representation safeguards and weightage
PARADOX -> unity is achieved through communal categories
VERDICT -> tactical advance with a long institutional shadow.""",
            ["Lucknow Pact: cooperation through a communal ledger"],
        ),
        (
            "The 1920s sequence",
            "chronology",
            """1920-22 -> Khilafat-Non-Cooperation joint mobilisation
BREAKDOWN -> coalition weakens; local conflict and rivalry grow
1923 -> Savarkar's Hindutva
1925 -> RSS founded
1928 -> Nehru Report
1929 -> Jinnah's Fourteen Points.""",
            ["Khilafat-Non-Cooperation unity and breakdown", "The 1920s: Hindu and Muslim communal organisations"],
        ),
        (
            "Nehru Report and Fourteen Points matrix",
            "comparison",
            """NEHRU REPORT -> stronger common constitutional framework
NEHRU REPORT -> no continuation of separate electorates in final design
FOURTEEN POINTS -> federal safeguards and provincial autonomy
FOURTEEN POINTS -> minority representation and residuary-power concerns
SHARED FIELD -> constitutional bargaining, not yet a settled Partition plan
TRAP -> 1929 demands are not the 1940 Lahore Resolution.""",
            ["Nehru Report and Fourteen Points"],
        ),
        (
            "Representation devices are not interchangeable",
            "comparison",
            """SEPARATE ELECTORATE -> only community voters choose community candidate
RESERVED SEAT -> a seat is set aside; electorate rules may differ
WEIGHTAGE -> representation exceeds a simple population ratio
NOMINATION -> authority appoints rather than voters elect
GROUPING -> provinces enter constitutional sections or groups
EXAM RULE -> identify mechanism before judging its political effect.""",
            ["Communal Award and Government of India Act 1935"],
        ),
        (
            "Provincial variation map",
            "regional-matrix",
            """UNITED PROVINCES -> service politics and failed coalition bargaining
PUNJAB -> landed, agrarian and Unionist coalition structures
BENGAL -> peasant, landlord, regional and communal alignments
NWFP -> strong non-League Muslim and Congress-allied politics
ALL-INDIA LEAGUE -> influence varied before post-1937 expansion
RULE -> province, class and coalition qualify every national claim.""",
            ["1937 elections and provincial variation"],
        ),
        (
            "Decision tree from Lahore to Partition",
            "decision-tree",
            """23 MAR 1940 -> Lahore Resolution changes the bargaining framework
1942-45 -> Cripps, Gandhi-Jinnah and Simla leave alternatives open
1945-46 ELECTIONS -> League claim among Muslim electorates strengthens
16 MAY 1946 -> Cabinet Mission proposes union plus grouping
16 AUG 1946 -> Direct Action and violence deepen breakdown
1947 -> 3 June Plan and Independence Act implement Partition.""",
            ["Lahore Resolution, war and bargaining, 1940-45", "1945-47 endgame and historiographical matrix"],
        ),
        (
            "Historiography and answer-writing matrix",
            "evidence-debate",
            """BIPAN CHANDRA -> modern ideology, elite interest and three stages
COLONIAL-STATE LENS -> enumeration and constitutional incentives
REGIONAL / CAMBRIDGE LENS -> coalitions, patronage and provincial elites
JALAL-TYPE LENS -> bargaining strategy and contingency
REJECT -> primordial hatred, one-cause blame and homogeneous communities
VERDICT -> multi-causal growth; contingent but increasingly constrained endgame.""",
            ["1945-47 endgame and historiographical matrix"],
        ),
    ],
}


SESSION_CORE_BY_TITLE = {
    title: core
    for plans in SESSION_PLANS.values()
    for title, core, _evidence, _caution, _exam_use in plans
}


def session_visual(title: str, _terms: list[str]) -> str:
    """Render a topic-specific conceptual visual for every authored session."""

    lowered = title.casefold()
    if "boundary, chronology" in lowered:
        diagram = (
            "1897 PRECURSOR -> 1904-09 REGIONAL CELLS -> 1912-13 EXPANSION\n"
            "        -> 1914-15 WARTIME NETWORKS -> 1916-17 POLITICAL SHIFT\n"
            "THEATRES: INDIA <-> LONDON / PARIS <-> PACIFIC <-> BERLIN / KABUL"
        )
    elif "swadeshi repression" in lowered:
        diagram = (
            "OPEN SWADESHI DECLINES + REPRESSION\n"
            "                 |\n"
            "         CLANDESTINE CHOICE\n"
            "                 |\n"
            "SECRET CELL -> EXEMPLARY ACTION -> EXPECTED WIDER COURAGE\n"
            "                 |\n"
            "        SECRECY / MASS-BASE LIMIT"
        )
    elif "revolutionary theory" in lowered:
        diagram = (
            "AGENT        METHOD                 EXPECTED EFFECT       CEILING\n"
            "vanguard -> cells + propaganda -> fear breaks      -> thin recruitment\n"
            "wartime  -> arms + mutiny plan  -> state rupture    -> informers / coordination"
        )
    elif "anushilan" in lowered:
        diagram = (
            "NAME                 FORM                    EXAM DISTINCTION\n"
            "Anushilan       -> organisational field -> not identical to Jugantar\n"
            "Dacca Anushilan -> regional network      -> preserve its own history\n"
            "Jugantar        -> network + newspaper   -> context decides meaning"
        )
    elif "muzaffarpur" in lowered:
        diagram = (
            "APR 1908 ATTACK -> KINGSFORD INTENDED -> TWO WOMEN KILLED\n"
            "        |\n"
            "MANIKTALA INVESTIGATION -> 1908-09 ALIPORE PROSECUTION\n"
            "RULE: connected action and case; never identical."
        )
    elif "maharashtra" in lowered:
        diagram = (
            "1897 CHAPEKAR PRECURSOR -> MITRA MELA -> 1904 ABHINAV BHARAT\n"
            "                                      |\n"
            "                         DEC 1909 NASIK ACTION\n"
            "RULE: keep precursor, organisation and prosecution separate."
        )
    elif "india house" in lowered:
        diagram = (
            "FOUNDER -> SHYAMJI KRISHNA VARMA\n"
            "PLACE -> LONDON | PAPER -> INDIAN SOCIOLOGIST\n"
            "LATER ORGANISER -> SAVARKAR\n"
            "1 JUL 1909 -> DHINGRA KILLS CURZON-WYLLIE -> SURVEILLANCE"
        )
    elif "european propaganda" in lowered:
        diagram = (
            "LONDON PRESSURE -> PARIS / CONTINENTAL SPACE\n"
            "                       |\n"
            "CAMA + S.R. RANA -> PRINT / ASYLUM / INTERNATIONAL PLATFORMS\n"
            "                       |\n"
            "GLOBAL VISIBILITY, NOT GHADAR ORGANISATIONAL ORIGIN"
        )
    elif "pacific migration" in lowered:
        diagram = (
            "MIGRATION + RACIAL EXCLUSION + LABOUR INSECURITY\n"
            "                       |\n"
            "FREE HINDUSTAN + SWADESH SEVAK\n"
            "                       |\n"
            "MIGRANT PUBLIC READY FOR FORMAL GHADAR ORGANISATION"
        )
    elif "ghadar organisation" in lowered:
        diagram = (
            "SOCIAL BASE -> MIGRANT WORKERS / EX-SOLDIERS\n"
            "ORGANISATION -> HINDI ASSOCIATION, MAY 1913\n"
            "CENTRE -> YUGANTAR ASHRAM | MEDIUM -> GHADAR PAPER\n"
            "PROGRAMME -> SECULAR REPUBLICAN RETURN AND REVOLT"
        )
    elif "komagata" in lowered:
        diagram = (
            "PUNJAB / ASIA -> VANCOUVER EXCLUSION -> FORCED RETURN\n"
            "                                         |\n"
            "                                 BUDGE BUDGE REPRESSION\n"
            "                                         |\n"
            "                              DIASPORA ANGER / WAR MOBILISATION"
        )
    elif "february 1915" in lowered:
        diagram = (
            "RETURNEES -> CANTONMENT CONTACT -> COORDINATED RISING PLAN\n"
            "                                   |\n"
            "INFORMERS -> DATE EXPOSED -> ARRESTS / ALTERED PLANS\n"
            "                                   |\n"
            "ATTEMPTED REVOLT, NOT A GENERAL INSURRECTION"
        )
    elif "berlin, kabul" in lowered:
        diagram = (
            "BERLIN -> FOREIGN ASSISTANCE\n"
            "KABUL  -> DIPLOMACY / PROVISIONAL GOVERNMENT ATTEMPT\n"
            "INDIA  -> INFILTRATION / RISING PLANS\n"
            "SINGAPORE -> MILITARY MUTINY IN SHARED WARTIME CONTEXT\n"
            "RULE: linked theatre does not prove one command."
        )
    elif "repression, law" in lowered:
        diagram = (
            "SURVEILLANCE -> INFORMERS -> CONSPIRACY TRIALS\n"
            "                         |\n"
            "DEFENCE OF INDIA ACT 1915 -> SPECIAL WARTIME POWER\n"
            "                         |\n"
            "LEADERS LOST + COMMUNICATIONS BROKEN + NETWORK ATTRITION"
        )
    elif "achievement, limits" in lowered:
        diagram = (
            "REVOLUTIONARY: SECRET VANGUARD -> SELECTIVE VIOLENCE / MUTINY\n"
            "GANDHIAN:      OPEN PUBLIC     -> NON-VIOLENT MASS SATYAGRAHA\n"
            "CONTINUITY: courage + sacrifice + anti-colonial refusal\n"
            "DISCONTINUITY: agent + method + scale + organisational discipline"
        )
    elif "definition ladder" in lowered:
        diagram = (
            "RELIGION / COMMUNITY LIFE\n"
            "          |\n"
            "COMMON SECULAR INTEREST -> DIVERGENT INTEREST -> HOSTILE INTEREST\n"
            "          |\n"
            "ORGANISATION + REPRESENTATION + POLITICAL MOBILISATION"
        )
    elif "precolonial caution" in lowered:
        diagram = (
            "RELIGIOUS DIFFERENCE BEFORE COLONIAL RULE\n"
            "             +\n"
            "1857 SHARED ACTION IN IMPORTANT REGIONS\n"
            "             +\n"
            "MODERN PRINT / ORGANISATION / ELECTORAL INSTITUTIONS\n"
            "             =\n"
            "DISCONTINUITY OF POLITICAL FORM, NOT TIMELESS HOSTILITY"
        )
    elif "colonial state" in lowered:
        diagram = (
            "STATE CATEGORIES + MATERIAL COMPETITION + ELITE CLAIM-MAKING\n"
            "             + CONSTITUTIONAL INCENTIVES + PARTY CHOICES\n"
            "                              |\n"
            "                    COMMUNAL POLITICAL GROWTH\n"
            "RULE: interaction, not one timeless or all-powerful cause."
        )
    elif "aligarh" in lowered:
        diagram = (
            "EDUCATIONAL DISADVANTAGE -> ALIGARH REFORM\n"
            "                              |\n"
            "LATER ELITE LOYALISM / CONGRESS CAUTION\n"
            "                              |\n"
            "SAFEGUARD CLAIMS, ALONGSIDE MANY ALTERNATIVE MUSLIM CURRENTS"
        )
    elif "partition, simla" in lowered:
        diagram = (
            "1905 BENGAL PARTITION -> 1 OCT 1906 SIMLA DEPUTATION\n"
            "        -> 30 DEC 1906 LEAGUE -> 1909 SEPARATE ELECTORATES\n"
            "CLAIM -> ORGANISATION -> CONSTITUTIONAL REWARD"
        )
    elif "league life-cycle" in lowered:
        diagram = (
            "1906 SAFEGUARDS -> 1913 SELF-GOVERNMENT -> 1916 COOPERATION\n"
            "        -> UNEVEN 1920s -> POST-1937 MOBILISATION\n"
            "        -> 1945-46 MUSLIM-ELECTORATE MANDATE\n"
            "RULE: organisational aims and reach changed over time."
        )
    elif "lucknow pact" in lowered:
        diagram = (
            "GAIN: JOINT CONSTITUTIONAL PROGRAMME + TEMPORARY UNITY\n"
            "COST: CONGRESS ACCEPTS SEPARATE ELECTORATES / SAFEGUARDS\n"
            "PARADOX: all-India cooperation negotiated through communal categories"
        )
    elif "khilafat" in lowered:
        diagram = (
            "KHILAFAT GRIEVANCE + NON-COOPERATION\n"
            "                 |\n"
            "      BROAD JOINT MOBILISATION\n"
            "                 |\n"
            "WITHDRAWAL / TURKISH CHANGE -> COALITION WEAKENS\n"
            "                 |\n"
            "LOCAL CONFLICT AND ORGANISATIONAL RIVALRY RE-EMERGE"
        )
    elif "the 1920s" in lowered:
        diagram = (
            "1920-22 KHILAFAT-NCM -> 1923 HINDUTVA -> 1925 RSS\n"
            "        -> RIOTS / ORGANISATIONAL RIVALRY -> 1928 NEHRU REPORT\n"
            "        -> 1929 FOURTEEN POINTS\n"
            "RULE: compare organisations without homogenising communities."
        )
    elif "nehru report" in lowered:
        diagram = (
            "AXIS                 NEHRU REPORT          FOURTEEN POINTS\n"
            "federation       -> common framework   | safeguards / autonomy\n"
            "electorates      -> joint direction    | minority protections\n"
            "residuary powers -> stronger centre    | provincial concern"
        )
    elif "communal award" in lowered:
        diagram = (
            "1932 COMMUNAL AWARD -> EXPANDED COMMUNITY REPRESENTATION\n"
            "1935 ACT -> PROVINCIAL AUTONOMY -> ELECTIONS / COALITIONS\n"
            "DISTINGUISH: separate electorate | reserved seat | nomination | weightage"
        )
    elif "representation table" in lowered:
        diagram = (
            "ORGANISATION / CLAIM      !=      WHOLE COMMUNITY\n"
            "HINDU MAHASABHA / RSS      !=      ALL HINDUS\n"
            "LEAGUE / OTHER MUSLIM PARTIES !=   ALL MUSLIMS\n"
            "CONGRESS TERRITORIAL CLAIM !=      EVERY MEMBER'S CULTURAL IDIOM"
        )
    elif "1937 elections" in lowered:
        diagram = (
            "UNITED PROVINCES -> OFFICE / COALITION BARGAINING\n"
            "PUNJAB           -> UNIONIST AGRARIAN COALITION\n"
            "BENGAL           -> PEASANT / LANDED / REGIONAL ALIGNMENTS\n"
            "NWFP             -> STRONG NON-LEAGUE MUSLIM POLITICS\n"
            "RULE: province and class qualify every all-India claim."
        )
    elif "lahore resolution" in lowered:
        diagram = (
            "23 MAR 1940 LAHORE RESOLUTION\n"
            "        -> 1942 CRIPPS -> 1944 GANDHI-JINNAH -> 1945 SIMLA\n"
            "ALTERNATIVES REMAIN OPEN; WAR CHANGES BARGAINING POWER."
        )
    elif "1945-47 endgame" in lowered:
        diagram = (
            "1945-46 ELECTIONS -> 16 MAY CABINET MISSION\n"
            "        -> GROUPING DISPUTE -> 16 AUG DIRECT ACTION / VIOLENCE\n"
            "        -> 3 JUNE PLAN -> INDEPENDENCE ACT / PARTITION\n"
            "INTERPRET: ideology + regions + bargaining + contingency."
        )
    else:
        raise ValueError(f"Missing topic-specific session visual: {title}")
    return (
        "#### VISUAL FIRST\n\n"
        "```text\n"
        f"{title.upper()}\n"
        f"{diagram}\n"
        "```\n\n"
        "*The visual fixes the subtopic's causal or comparative structure before the detailed evidence.*"
    )


def session_definitions(
    title: str,
    topic_title: str,
    _terms: list[str],
) -> str:
    """Write precise definitions from the authored session thesis."""

    core = SESSION_CORE_BY_TITLE[title].rstrip(".")
    lowered = title.casefold()
    if any(
        marker in lowered
        for marker in ("chronology", "sequence", "1905-09", "1940-45", "1945-47")
    ):
        technical = "a chronological evidence unit separating trigger, organisation, response and consequence"
    elif any(marker in lowered for marker in ("matrix", "distinguish", "representation table")):
        technical = "a comparison unit that holds actors and institutions to a common analytical axis"
    elif any(marker in lowered for marker in ("causation", "repression", "armed turn", "breakdown")):
        technical = "a causal unit linking conditions, political choices, mechanisms and limits"
    elif any(marker in lowered for marker in ("map", "regional", "theatre", "overseas", "migration")):
        technical = "a spatial unit showing how place, constituency and political opportunity altered the process"
    elif any(marker in lowered for marker in ("definition", "theory", "ideology", "life-cycle")):
        technical = "a conceptual unit defining the category, its mechanism and its changing political form"
    else:
        technical = "an evidence-led unit connecting actors, institutions, mechanism, outcome and qualification"
    return (
        "#### CONCEPT DEFINITIONS\n\n"
        f"- **Plain definition:** This subtopic explains how {core[0].lower() + core[1:]}.\n"
        f"- **Technical definition:** For exam use, it is {technical} within {topic_title}."
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
    """Use the dossier's editorial route while retaining owner PYQ evidence."""

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
        "scope": "Modern Indian History learner-v2 Topics 16-17",
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
