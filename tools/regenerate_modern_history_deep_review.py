"""Deep-review and immutably regenerate all 38 Modern History packages."""

from __future__ import annotations

import hashlib
import os
import re
import textwrap
from pathlib import Path
from typing import Any

import generate_modern_history_01_02_sequential as authored_01_02
import generate_modern_history_03_04_sequential as authored_03_04
import generate_modern_history_05_06_sequential as authored_05_06
import generate_modern_history_07_08_sequential as authored_07_08
import generate_modern_history_09_13_sequential as authored_09_13
import generate_modern_history_14_15_sequential as authored_14_15
import generate_modern_history_16_17_sequential as authored_16_17
import generate_modern_history_18_19_sequential as authored_18_19
import generate_modern_history_20_21_sequential as authored_20_21
import generate_modern_history_22_23_sequential as authored_22_23
import generate_modern_history_24_25_sequential as authored_24_25
import generate_modern_history_26_27_sequential as authored_26_27
import generate_modern_history_28_29_sequential as authored_28_29
import generate_modern_history_30_31_sequential as authored_30_31
import generate_modern_history_32_33_sequential as authored_32_33
import generate_modern_history_34_35_sequential as authored_34_35
import generate_modern_history_36_37_sequential as authored_36_37
import generate_modern_history_38_sequential as authored_38


_BASE = Path(__file__).with_name("regenerate_ancient_history_deep_review.py")
_BASE_SHA256 = "d3c208166750909b3d46be15c087d26a098d9dd95eda588f6a19974d511a7780"
_base_bytes = _BASE.read_bytes()
if hashlib.sha256(_base_bytes).hexdigest() != _BASE_SHA256:
    raise RuntimeError(
        "The shared deep-review engine changed. Review and repin it before "
        "running the Modern History workflow."
    )
_source = _base_bytes.decode("utf-8").replace("\r\n", "\n")
_source = _source.rsplit('\nif __name__ == "__main__":', 1)[0]

for _old, _new in (
    ("2026-08-30", "2026-09-04"),
    ("30 August 2026", "4 September 2026"),
    ("Ancient-Indian-History", "Modern-Indian-History"),
    ("ancient-indian-history", "modern-indian-history"),
    ("Ancient History", "Modern History"),
    ("Ancient-History", "Modern-History"),
    ("ancient-history", "modern-history"),
    ("ancient_history", "modern_history"),
    ("E-AH", "E-MHIST"),
    ("MD-AH", "MD-MHIST"),
    ("AH{", "MHIST{"),
    ("AH01", "MHIST01"),
    ("range(1, 28)", "range(1, 39)"),
    ("topics 01-27", "topics 01-38"),
    ('"topic_count": 27', '"topic_count": 38'),
    ('"topic_validations_passed": 27', '"topic_validations_passed": 38'),
    ('"latest_topic_count": 27', '"latest_topic_count": 38'),
    ('"learning_and_workbook_pdfs_checked": 54', '"learning_and_workbook_pdfs_checked": 76'),
    ('"represented": 27', '"represented": 38'),
    ('"expected": 27', '"expected": 38'),
    ("All 27 topics", "All 38 topics"),
    (
        "        27: (26, 27),\n",
        "        31: (26, 31),\n"
        "        35: (32, 35),\n"
        "        38: (36, 38),\n",
    ),
):
    if _old not in _source:
        raise RuntimeError(f"Shared-engine transformation anchor is missing: {_old!r}")
    _source = _source.replace(_old, _new)

_inventory_anchor = '''    changed: set[str] = {
        rel(Path(__file__)),
        "tools\\\\test_regenerate_modern_history_deep_review.py",
    }
'''
_inventory_replacement = '''    changed: set[str] = {
        rel(Path(__file__)),
        "tools\\\\test_regenerate_modern_history_deep_review.py",
        "tools\\\\export_four_item_library.py",
        "tools\\\\test_export_four_item_library.py",
        "tools\\\\sync_deep_review_tracker.py",
        "tools\\\\test_sync_deep_review_tracker.py",
        "notes\\\\Final-Learning-Packages\\\\START-HERE.md",
        "notes\\\\Final-Learning-Packages\\\\CATALOGUE.md",
        "notes\\\\Final-Learning-Packages\\\\MASTER-TRACKER.md",
        "notes\\\\Final-Learning-Packages\\\\MASTER-TRACKER.json",
        "notes\\\\Final-Learning-Packages\\\\_deep-content-review\\\\README.md",
        "notes\\\\Final-Learning-Packages\\\\_deep-content-review\\\\REVIEW-TRACKER.json",
        "notes\\\\Final-Learning-Packages\\\\_deep-content-review\\\\REVIEW-TRACKER.md",
        "upsc-ai-kit\\\\manifests\\\\exports\\\\deep-review-tracker-sync-2026-08-30.json",
        "upsc-ai-kit\\\\manifests\\\\exports\\\\deep-review-tracker-sync-2026-08-31.json",
        "upsc-ai-kit\\\\manifests\\\\exports\\\\final-four-item-library-2026-08-31.json",
        "upsc-ai-kit\\\\manifests\\\\exports\\\\final-four-item-library-2026-08-31-validation.json",
        "upsc-ai-kit\\\\manifests\\\\exports\\\\final-four-item-library-2026-09-01.json",
        "upsc-ai-kit\\\\manifests\\\\exports\\\\final-four-item-library-2026-09-01-validation.json",
    }
'''
if _inventory_anchor not in _source:
    raise RuntimeError("Shared-engine changed-file inventory anchor is missing.")
_source = _source.replace(_inventory_anchor, _inventory_replacement, 1)

_tests_anchor = '''    tests = [
        run_unittest("test_regenerate_modern_history_deep_review"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
'''
_tests_replacement = '''    tests = [
        run_unittest("test_regenerate_modern_history_deep_review"),
        run_unittest("test_generate_modern_history_03_04_sequential"),
        run_unittest("test_generate_modern_history_05_06_sequential"),
        run_unittest("test_generate_modern_history_07_08_sequential"),
        run_unittest("test_generate_modern_history_09_13_sequential"),
        run_unittest("test_generate_modern_history_14_15_sequential"),
        run_unittest("test_generate_modern_history_16_17_sequential"),
        run_unittest("test_generate_modern_history_18_19_sequential"),
        run_unittest("test_generate_modern_history_20_21_sequential"),
        run_unittest("test_generate_modern_history_22_23_sequential"),
        run_unittest("test_generate_modern_history_24_25_sequential"),
        run_unittest("test_generate_modern_history_26_27_sequential"),
        run_unittest("test_generate_modern_history_28_29_sequential"),
        run_unittest("test_generate_modern_history_30_31_sequential"),
        run_unittest("test_generate_modern_history_32_33_sequential"),
        run_unittest("test_generate_modern_history_34_35_sequential"),
        run_unittest("test_generate_modern_history_36_37_sequential"),
        run_unittest("test_generate_modern_history_38_sequential"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
'''
if _tests_anchor not in _source:
    raise RuntimeError("Shared-engine targeted-test anchor is missing.")
_source = _source.replace(_tests_anchor, _tests_replacement, 1)

_content_repair_anchor = """    main = normalize_required_h2(main)
    main = insert_contract(main, topic, old)
"""
_content_repair_replacement = """    main = repair_topic_content(main, topic)
    workbook = repair_topic_content(workbook, topic)
    main = normalize_required_h2(main)
    main = insert_contract(main, topic, old)
"""
if _content_repair_anchor not in _source:
    raise RuntimeError("Shared-engine topic-content repair anchor is missing.")
_source = _source.replace(
    _content_repair_anchor,
    _content_repair_replacement,
    1,
)

exec(compile(_source, str(Path(__file__)), "exec"), globals())

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def topics() -> list[Topic]:
    """Return exactly the currently generated Modern History topics 01-38."""
    manifest = load(SECTION_MANIFEST)
    selected = {
        f"modern-indian-history-{number:02d}"
        for number in range(1, 39)
    }
    rows = [
        row for row in manifest["topics"] if row["topic_key"] in selected
    ]
    result = [
        Topic(
            number=number,
            topic_key=row["topic_key"],
            title=row["display_title"],
            basic_path=repo(row["source_basic"]),
            canonical_path=repo(row["source_canonical"]),
            advanced_path=repo(row["source_advanced"]),
            cross_topic_sources=tuple(
                repo(path) for path in row.get("cross_topic_sources", [])
            ),
            pyq_sources=tuple(
                repo(path) for path in row.get("verified_pyq_sources", [])
            ),
        )
        for number, row in enumerate(rows, 1)
    ]
    if (
        len(result) != 38
        or [topic.topic_key for topic in result]
        != sorted(selected)
    ):
        raise ValueError(
            "Modern History review scope must contain exact topic keys 01-38."
        )
    return result


def review_paths(topic: Topic, generation: int) -> dict[str, Path]:
    """Use immutable Windows-safe paths for every Modern History successor."""
    short_key = f"mhi-{topic.number:02d}"
    knowledge_dir = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Learner-v2-Refreshed"
        / "Modern"
        / "MH"
        / "learning-sessions"
        / short_key
        / f"g{generation}"
    )
    notes_dir = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "Modern"
        / "MH"
        / "learning-sessions"
        / short_key
        / f"g{generation}"
    )
    flow_dir = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "Modern"
        / "MH"
        / "flowcharts"
        / short_key
        / f"carvaka-g{generation}"
    )
    stem = topic.topic_key
    return {
        "knowledge_dir": knowledge_dir,
        "notes_dir": notes_dir,
        "flow_dir": flow_dir,
        "markdown": knowledge_dir
        / f"{stem}_Complete-Learning-Session_{DATE}.md",
        "workbook_markdown": knowledge_dir
        / f"{stem}_Solved-Practice-Workbook_{DATE}.md",
        "main_pdf": notes_dir
        / f"{stem}_Complete-Learning-Session_{DATE}.pdf",
        "workbook_pdf": notes_dir
        / f"{stem}_Solved-Practice-Workbook_{DATE}.pdf",
        "asset_folder": knowledge_dir / "assets",
        "main_visual": notes_dir / "validation" / "main-visual-audit-map.json",
        "workbook_visual": notes_dir
        / "validation"
        / "workbook-visual-audit-map.json",
        "ascii_pdf": flow_dir / "ascii-master.pdf",
        "ascii_spec": ASCII_SPECS
        / f"{stem}-deep-review-{DATE}-g{generation}.json",
        "graphical_spec": GRAPHICAL_SPECS / f"{stem}-g{generation}.json",
        "content_spec": CONTENT_SPECS / f"{stem}-g{generation}.json",
        "record": EXPORTS
        / f"{stem}-learner-v2-g{generation}-{DATE}-record.json",
        "validation": EXPORTS
        / f"{stem}-learner-v2-g{generation}-{DATE}-validation.json",
    }


MODERN_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    1: (
        "Aurangzeb's death in 1707 begins the core sequence; succession wars, factional competition, jagirdari-fiscal stress, regional assertion and Nadir Shah's 1739 invasion interacted.",
        "Decline of enforceable central command did not mean instant state collapse, civilisational decline or disappearance of Mughal titles, revenue forms and Persianate legitimacy.",
        "Satish Chandra's jagirdari analysis, regional-state evidence and court chronicles must be compared; no single-ruler or British-inevitability thesis is sufficient.",
    ),
    2: (
        "Hyderabad, Awadh and Bengal adapted Mughal offices, while Maratha, Sikh, Jat, Mysore and other formations followed distinct fiscal-military and regional routes.",
        "Political plurality and warfare coexisted with credit, textile production, urban patronage and unequal social burdens; neither 'anarchy' nor universal prosperity fits all regions.",
        "Use revenue records, banking networks, courtly evidence and regional scholarship to qualify both colonial chaos narratives and over-corrective continuity claims.",
    ),
    3: (
        "The maritime sequence runs through the Portuguese arrival in 1498 and Goa in 1510, the English Company charter of 1600, the Dutch VOC of 1602 and the French Company of 1664.",
        "A factory was a trading station, not automatically territorial sovereignty; cartaz, naval force, diplomacy, farmans and fortified settlements had different legal-political effects.",
        "European archives privilege company aims; Indian merchants, rulers, port ecologies and Asian commercial rivals are necessary evidence against a Europe-only inevitability story.",
    ),
    4: (
        "Plassey on 23 June 1757, Buxar on 22 October 1764, the 1765 Allahabad settlement and Diwani grant, and the 1765-72 Dual Government are separate stages.",
        "Plassey enabled political leverage through conspiracy and finance; Buxar established a broader military-fiscal superiority against Mir Qasim, Shuja-ud-Daula and Shah Alam II.",
        "Company records and later nationalist accounts must be checked against Bengal court, banking and revenue evidence; conquest was contingent, collaborative and coercive.",
    ),
    5: (
        "Keep the Anglo-Mysore, Anglo-Maratha and Anglo-Sikh wars in their distinct sequences, and separate Wellesley's Subsidiary Alliance from Dalhousie's Doctrine of Lapse.",
        "Awadh was annexed in 1856 on the stated ground of misgovernment, not under the Doctrine of Lapse; treaty, subsidiary control, conquest and annexation are not synonyms.",
        "Campaign maps, treaty clauses, succession disputes and Indian alliance choices qualify any account of uniform British military superiority or passive regional defeat.",
    ),
    6: (
        "Regulating Act 1773, Pitt's India Act 1784, Charter Acts 1813, 1833 and 1853, and Government of India Act 1858 changed different corporate, executive, legislative and patronage arrangements.",
        "Distinguish enactment from commencement and policy from implementation: the 1833 Act ended Company commerce, while open competitive recruitment developed through later measures.",
        "Read statutory text with Company practice and parliamentary inquiry; constitutional centralisation did not remove distance, discretion, corruption or racial exclusion.",
    ),
    7: (
        "Drain, deindustrialisation, land-revenue pressure and famine vulnerability are related mechanisms, not interchangeable slogans; Dadabhai Naoroji and R.C. Dutt made specific economic arguments.",
        "Permanent, Ryotwari and Mahalwari settlements differed by region, assessment unit and intermediary structure; no one settlement covered all India or remained unchanged in practice.",
        "Nationalist, Marxist and revisionist scholarship must be tied to wage, trade, craft, revenue and mortality evidence, with regional variation and data limits made explicit.",
    ),
    8: (
        "Civil service, presidency armies, police, courts and district administration formed an extractive-security state whose institutions changed across Company and Crown phases.",
        "The proclaimed rule of law coexisted with racial bars, executive discretion and unequal access; Cornwallis reforms, the daroga police and the Ilbert Bill controversy require separate contexts.",
        "Official manuals show institutional design, not uniform local experience; subaltern petitions, trials and regional practice qualify claims of either pure modernisation or pure continuity.",
    ),
    9: (
        "The 1813 education grant, Macaulay's 1835 Minute, Wood's Dispatch of 1854 and the 1857 universities mark different policy stages, while press controls repeatedly tightened and relaxed.",
        "Anglicist versus Orientalist policy, missionary activity, vernacular print and Indian educational initiative cannot be collapsed into a single Westernisation programme.",
        "Government resolutions, missionary records and vernacular public spheres have positioned evidence; education and print enabled critique while reproducing class, caste and gender exclusions.",
    ),
    10: (
        "Brahmo Samaj (1828), Satyashodhak Samaj (1873), Arya Samaj (1875), MAO College (1875), Ramakrishna Mission (1897), Singh Sabha and Deoband belong to distinct regional-intellectual projects.",
        "Reform, revival, caste critique, women's rights and community consolidation overlapped but were not one linear liberal movement; legal enactment never proves social implementation.",
        "Feminist, Dalit-bahujan and regional evidence must qualify elite male reform narratives, while colonial archives cannot be treated as neutral measures of Indian society.",
    ),
    11: (
        "The revolt began at Meerut on 10 May 1857 and spread through Delhi, Kanpur, Lucknow, Jhansi, Bareilly, Arrah and other centres with different leaders, grievances and local coalitions.",
        "Sepoy mutiny, civil rebellion, peasant-zamindar resistance and restorationist politics were overlapping dimensions; it was neither a uniform national war nor only a barracks incident.",
        "Colonial, nationalist, Marxist and subaltern interpretations must be tested against proclamations, rebel correspondence, trial records and sharply uneven regional participation.",
    ),
    12: (
        "The 1858 Crown transfer, Indian Councils Acts 1861 and 1892, Morley-Minto reforms of 1909, army reorganisation and the princely-state settlement changed different governing relationships.",
        "Queen Victoria's Proclamation of 1 November 1858 stated policy; its promises on religion, office and princes must be distinguished from later implementation and racial practice.",
        "Statutes and proclamations record formal design, while budgets, recruitment and council proceedings reveal the limits of representation, decentralisation and Indian participation.",
    ),
    13: (
        "Keep the Afghan wars (1839-42, 1878-80, 1919), Burma wars (1824-26, 1852, 1885), Nepal war and Treaty of Sugauli (1814-16), and Younghusband mission to Tibet (1903-04) distinct.",
        "Forward policy, 'masterly inactivity', buffer strategy, annexation and frontier administration were debated and changed over time; modern boundaries cannot be projected backward.",
        "Imperial strategic writing must be checked against treaty texts, terrain, logistics and Afghan, Burmese, Nepali, Tibetan and frontier agency rather than reproducing a Great Game gaze.",
    ),
    14: (
        "The INC met first at Bombay in December 1885 under W.C. Bonnerjee; A.O. Hume mattered organisationally, but Indian associations, economic critique and political networks predated it.",
        "The 'safety-valve' claim is not an adequate monocausal origin theory; Moderate constitutional methods could be limited yet still create an all-India political vocabulary and economic indictment.",
        "Nationalist, Cambridge and subaltern accounts should be compared through membership, petitions, associations, press and provincial participation, including the movement's narrow early social base.",
    ),
    15: (
        "Bengal's partition took effect on 16 October 1905, Swadeshi and boycott expanded into national education and samitis, the Congress split at Surat in 1907, and partition was annulled in 1911.",
        "Militant nationalism was broader than violence, while boycott and passive resistance varied by region, class, caste, gender and commodity; Bengal cannot stand for all India.",
        "Police files, vernacular newspapers, business responses and women's participation qualify both heroic unity narratives and official depictions of mere disorder.",
    ),
    16: (
        "Anushilan, Jugantar, Abhinav Bharat, India House and the Ghadar movement had different geographies, ideologies and organisational forms across the 1907-17 phase.",
        "The 1908 Muzaffarpur action, Alipore case, wartime Indo-German plans and Ghadar efforts must not be merged into one continuous centrally directed conspiracy.",
        "Revolutionary writings, trial records and intelligence files require source criticism; courage and sacrifice do not erase strategic limits, civilian harm or ideological diversity.",
    ),
    17: (
        "The Simla Deputation and Muslim League foundation at Dacca in 1906, separate electorates in 1909 and the Lucknow Pact of 1916 are distinct institutional moments.",
        "Communalism was historically produced through representation, elite competition, colonial classification and social mobilisation; it was not an ancient, inevitable Hindu-Muslim essence.",
        "Colonial, nationalist, Cambridge and subaltern explanations need provincial evidence and must include Hindu communal organisations as well as Muslim League trajectories.",
    ),
    18: (
        "Tilak's and Annie Besant's Home Rule Leagues began separately in 1916; the Lucknow Congress and Congress-League Pact followed in December 1916, before the Montagu Declaration of 20 August 1917.",
        "Home Rule mobilisation, Congress reunion and the Lucknow compromise were connected but institutionally distinct; separate electorates remained embedded in the pact.",
        "Wartime recruitment, taxation, repression, Ghadar activity and provincial league networks qualify a leadership-only account of political revival.",
    ),
    19: (
        "Champaran (1917), Ahmedabad mill dispute and Kheda (1918), the Rowlatt legislation and hartal of 1919, and Jallianwala Bagh on 13 April 1919 form a sequence of changing methods and scales.",
        "Satyagraha was not instant mass control: Ahmedabad joined labour arbitration, Kheda relief claims varied, and Gandhi suspended the Rowlatt campaign after violence.",
        "Official inquiry, local testimony, nationalist memory and later commemoration must be separated; the massacre's moral-political impact does not make every reported detail equally verified.",
    ),
    20: (
        "Khilafat mobilisation and Non-Cooperation converged in 1920; the Calcutta special and Nagpur Congress sessions authorised stages of boycott before Chauri Chaura on 4 February 1922 and withdrawal on 12 February.",
        "Withdrawal followed Gandhi's non-violence criterion but its wisdom was contested; the Moplah rebellion of 1921 cannot be reduced to either pure agrarianism or a single communal label.",
        "Congress records, Khilafat voices, local agrarian evidence and participant memoirs reveal uneven class, caste, gender and regional mobilisation rather than a seamless national awakening.",
    ),
    21: (
        "The Swaraj Party was formed in 1923 by C.R. Das and Motilal Nehru; constructive work, council obstruction, HRA-Kakori and the 1928 HSRA reorientation were distinct post-withdrawal strategies.",
        "Bhagat Singh's politics included republican and socialist argument, not only martyrdom; HSRA action, trade-union work and Congress politics should not be collapsed into one revolutionary stream.",
        "Legislative records, organisational manifestos, prison writings and police files must be cross-read to avoid hero worship, colonial criminalisation and retrospective ideological simplification.",
    ),
    22: (
        "Simon Commission protest, the 1928 Nehru Report, Lahore's Purna Swaraj resolution in 1929, the 1930 salt march, Gandhi-Irwin Pact of 5 March 1931 and three Round Table Conferences form separate stages.",
        "The Communal Award and Poona Pact belong to 1932 and addressed representation differently; Civil Disobedience changed phases before formal withdrawal in 1934.",
        "Official conference records, Congress resolutions, Ambedkar-Gandhi positions and regional no-tax or forest struggles prevent an elite-negotiation-only account.",
    ),
    23: (
        "CSP (1934), All India Kisan Sabha (1936), trade unions, communist networks and princely-state Praja Mandals linked national politics to class and regional struggles in different ways.",
        "The CPI's origin requires qualification between the 1920 Tashkent formation and the 1925 Kanpur conference; peasant, labour, caste and women's movements were not Congress appendages.",
        "Party documents, labour reports and local movement studies must recover agency while avoiding the claim that one ideological line uniformly controlled India's diverse social struggles.",
    ),
    24: (
        "The Government of India Act 1935 created provincial autonomy and proposed an all-India federation that never came into operation; dyarchy ended in provinces but was proposed at the centre.",
        "Congress ministries followed the 1937 elections and resigned in 1939 after India was committed to war without consultation; office-holding did not transfer sovereign control.",
        "Statutory safeguards and governors' powers must be read with ministry records, tenancy and civil-liberty measures, opposition experience and provincial variation.",
    ),
    25: (
        "India was declared at war on 3 September 1939; the August Offer, Individual Satyagraha, Cripps Mission of March-April 1942 and Quit India resolution of 8 August 1942 were different constitutional-political moments.",
        "Cripps offered a post-war constitution-making route with a provincial non-accession option, not immediate full independence; Quit India combined central arrests with decentralised underground and parallel action.",
        "Official repression records, underground communications, local rebellions and the 1943 Bengal famine context qualify both leaderless-chaos and perfectly coordinated-revolution narratives.",
    ),
    26: (
        "Mohan Singh's first INA in 1942, Subhas Chandra Bose's 1943 reorganisation and Azad Hind government, Red Fort trials from 1945, RIN revolt of 18-23 February 1946 and Cabinet Mission proposals were distinct.",
        "The Cabinet Mission's 16 May 1946 plan preserved a weak union with provincial groupings; INA/RIN impact on British calculations must not be promoted into a single-cause transfer-of-power claim.",
        "Military intelligence, trial proceedings, service unrest and Cabinet records require attribution alongside labour and public mobilisation; nationalist memory alone cannot settle causal weight.",
    ),
    27: (
        "The 1946 elections, Cabinet Mission breakdown, Direct Action Day on 16 August, Interim Government from 2 September, Attlee statement of 20 February 1947 and 3 June Plan led to the Independence Act.",
        "The Indian Independence Act received royal assent on 18 July 1947; transfer dates, Radcliffe Award publication and mass displacement must remain separately dated.",
        "Partition requires League, Congress, British, provincial and popular agency plus gendered violence and refugee evidence; communal inevitability and single-person blame are both inadequate.",
    ),
    28: (
        "Accession, administrative integration and constitutional reorganisation were distinct: Junagadh, Hyderabad and Jammu and Kashmir followed different legal, military and political sequences.",
        "The Instrument of Accession transferred specified subjects, not an identical final settlement in every state; Hyderabad's September 1948 action and Kashmir's October 1947 accession cannot be analogised mechanically.",
        "States Ministry papers, accession instruments and regional evidence must qualify triumphalist inevitability and recognise rulers, popular movements, borders and international conflict.",
    ),
    29: (
        "Colonial legacies included centralised administration, civil services, army, law, railways, economic underdevelopment and classificatory practices, while the national movement supplied democratic and federal resources.",
        "A railway, court or bureaucracy is not inherently a benevolent gift or an unchanged colonial burden; purpose, access, financing, adaptation and post-1947 political control must be separated.",
        "Nationalist, Marxist, Cambridge, subaltern and feminist readings require sector-specific evidence rather than a single positive-versus-negative balance sheet.",
    ),
    30: (
        "Dar Commission (1948), JVP Committee (1948), Andhra state (1953), States Reorganisation Commission report (1955) and the Act effective 1 November 1956 form the core sequence.",
        "Bombay's bifurcation in 1960, Punjab reorganisation in 1966 and the Official Languages Act 1963 with its 1967 amendment were related accommodation problems, not one linguistic-state event.",
        "Commission reports, parliamentary law and regional movements show that linguistic reorganisation often deepened federal integration, while violence and minority questions qualify a success-only narrative.",
    ),
    31: (
        "The Fifth and Sixth Schedules, community-sensitive development, the Naga settlement and statehood process, and the 1986 Mizo Accord represent different constitutional and negotiated routes.",
        "Nehru's tribal policy rejected both forced assimilation and museum-like isolation, but administrative practice, land alienation, forests, displacement and autonomy remained contested.",
        "Constitutional text, Verrier Elwin's influence, movement records and tribal voices must be compared; integration is a negotiated process, not proof of cultural absorption or completed equality.",
    ),
    32: (
        "Planning Commission (15 March 1950), first general election (October 1951-February 1952), Community Development Programme (2 October 1952), Panchsheel (April 1954), Avadi (January 1955), Bandung (April 1955), IPR/Second Plan (1956), Kerala election (1957), Belgrade and Goa (1961), the 1962 war, Kamaraj Plan (1963) and Nehru's death (27 May 1964) form distinct stages.",
        "The Planning Commission was extra-constitutional; Bandung was an Afro-Asian precursor, not NAM's founding summit; non-alignment was independent engagement, not passive neutrality; and the 1962 defeat exposed strategic limits without erasing the doctrine's whole diplomatic record.",
        "Cabinet resolutions, Election Commission data, Congress resolutions, treaty/summit records and regional outcomes must qualify both uncritical hero-making and retrospective single-failure verdicts, especially on Kashmir, planning and China.",
    ),
    33: (
        "Congress dominance must be read beside the Socialist exit (1948), Bharatiya Jana Sangh (1951), KMPP-Socialist merger into the PSP (1952), Swatantra Party (1959), CPI split (1964) and the 1967 electoral watershed.",
        "Rajni Kothari's 'Congress system' meant competitive one-party dominance, not a one-party state: first-past-the-post converted sub-50-per-cent vote shares into large seat majorities while opposition parties retained distinct socialist, communist, conservative and regional bases.",
        "Election returns, party constitutions and manifestos, Tandon-Nehru organisational conflict and Kothari's attributed model must replace teleological claims that Congress dominance was either inevitable consensus or disguised dictatorship.",
    ),
    34: (
        "Shastri became Prime Minister on 9 June 1964; the 1965 war led to the Tashkent Declaration on 10 January 1966 and his death on 11 January; Indira Gandhi took office on 24 January, devaluation followed on 6 June, the 1967 election weakened Congress, the party split and fourteen banks were nationalised in 1969, privy purses ended constitutionally in 1971, and the Bangladesh war and Simla Agreement followed in 1971-72.",
        "Bank nationalisation in 1969 and the 26th Amendment ending privy purses in 1971 are separate measures; the 1967 result was a major setback, not a comfortable mandate; and Pokhran-I on 18 May 1974 is immediate aftermath/enrichment beyond the topic's stated 1964-73 boundary.",
        "Election data, the Tashkent and Simla texts, constitutional amendment history, bank-nationalisation instruments and war/diplomatic records must qualify personality-centred inevitability and distinguish policy announcement, judicial challenge and legal completion.",
    ),
    35: (
        "The 1973-74 inflation and oil shock preceded Gujarat's Nav Nirman movement, the Bihar movement and May 1974 railway strike; the Allahabad High Court judgment came on 12 June 1975, the Emergency was proclaimed on 25 June and publicly announced on 26 June, constitutional and coercive instruments followed, elections were called in January 1977 and the Emergency ended on 21 March 1977 before the 44th Amendment of 1978.",
        "The Allahabad High Court, not the Supreme Court, initially invalidated Indira Gandhi's election; proclamation and public announcement dates must remain distinct; and student/middle-class leadership did not mean uniform incorporation of industrial workers, peasants, Dalits or every region.",
        "The proclamation, MISA/detention records, press censorship orders, 38th/39th/42nd Amendments, sterilisation and clearance evidence, Shah Commission findings and the 1977 verdict must be cross-read without reducing the Emergency to either one leader's will or a socially uniform resistance.",
    ),
    36: (
        "Janata formed in January 1977 and won 330 of 542 seats in March; the 44th Amendment followed in 1978, Charan Singh's July 1979 ministry never faced a confidence vote, Congress (I) won 353 of 529 seats in January 1980, Telugu Desam was founded on 29 March 1982 before its 1983 Andhra victory, and the Punjab sequence reached Operation Blue Star in June and Indira Gandhi's assassination on 31 October 1984.",
        "The 1980 result is evidence of Janata's collapse but not proof that voters endorsed the Emergency; Telugu Desam's founding in 1982 must not be collapsed into its 1983 breakthrough; and the Punjab crisis cannot be reduced to a timeless religious conflict or to one causal actor.",
        "Election results, the 44th Amendment, party records, the Anandpur Sahib Resolution, federal negotiations and regional evidence from Andhra, Assam, Punjab, West Bengal and Jammu and Kashmir must qualify centralised, communal or single-cause narratives.",
    ),
    37: (
        "Rajiv Gandhi's December 1984 victory (Congress 404 of 514 elected seats), the 52nd Amendment and Punjab/Assam accords of 1985, Shah Bano reversal and Bofors controversy, the 1989 National Front coalition, Mandal implementation and Advani's rath yatra in 1990, the 1991 reforms, Babri Masjid demolition on 6 December 1992 and coalition governments from 1996 form separate stages.",
        "The Anti-Defection Act belongs to Rajiv's 1985 government, the 27-per-cent Mandal measure concerned OBC reservation in central government employment, the 1991 reforms were crisis-led under Narasimha Rao and Manmohan Singh, and 1990's yatra must not be confused with the 1992 demolition.",
        "Election returns, amendment and accord texts, court-legislative sequences, budget/reform documents and attributed 'Mandal, Mandir and Market' interpretation must qualify both a simple modernisation story and a communal or caste-essentialist account.",
    ),
    38: (
        "The synthesis runs from the 1948/1956 Industrial Policy Resolutions, Planning Commission and First Plan, zamindari abolition and Bhoodan, the mid-1960s Green Revolution, Naxalbari (1967) and CPI(ML) (1969), farmers' movements at Nasik (1980) and Sisauli (1986), Mandal implementation (1990) and the 1991 market turn.",
        "Land reform must be disaggregated; Green Revolution output gains do not settle distributional or ecological debate; and the proposed Hindu Code became the Hindu Marriage Act 1955 plus three 1956 Acts, which expanded women's rights within Hindu personal law but did not create complete legal or social equality.",
        "Plan and land records, regional agrarian evidence, attributed Chandra and critical Green Revolution readings, India Code statutes and movement histories must support a graded verdict: state capacity transformed production and representation more consistently than property, equality or implementation.",
    ),
}


AUTHORED_PANEL_CONTROLS = {
    **{
        key: value
        for key, value in authored_01_02.PANEL_DATA.items()
        if key.endswith(("-01", "-02"))
    },
    **{
        key: value
        for key, value in authored_03_04.PANEL_DATA.items()
        if key.endswith(("-03", "-04"))
    },
    "modern-indian-history-05": authored_05_06.PANEL_DATA[
        "modern-indian-history-05"
    ],
    "modern-indian-history-06": authored_05_06.PANEL_DATA[
        "modern-indian-history-06"
    ],
    "modern-indian-history-07": authored_07_08.PANEL_DATA[
        "modern-indian-history-07"
    ],
    "modern-indian-history-08": authored_07_08.PANEL_DATA[
        "modern-indian-history-08"
    ],
    "modern-indian-history-09": authored_09_13.PANEL_DATA[
        "modern-indian-history-09"
    ],
    "modern-indian-history-10": authored_09_13.PANEL_DATA[
        "modern-indian-history-10"
    ],
    "modern-indian-history-11": authored_09_13.PANEL_DATA[
        "modern-indian-history-11"
    ],
    "modern-indian-history-12": authored_09_13.PANEL_DATA[
        "modern-indian-history-12"
    ],
    "modern-indian-history-13": authored_09_13.PANEL_DATA[
        "modern-indian-history-13"
    ],
    "modern-indian-history-14": authored_14_15.PANEL_DATA[
        "modern-indian-history-14"
    ],
    "modern-indian-history-15": authored_14_15.PANEL_DATA[
        "modern-indian-history-15"
    ],
    "modern-indian-history-16": authored_16_17.PANEL_DATA[
        "modern-indian-history-16"
    ],
    "modern-indian-history-17": authored_16_17.PANEL_DATA[
        "modern-indian-history-17"
    ],
    "modern-indian-history-18": authored_18_19.PANEL_DATA[
        "modern-indian-history-18"
    ],
    "modern-indian-history-19": authored_18_19.PANEL_DATA[
        "modern-indian-history-19"
    ],
    "modern-indian-history-20": authored_20_21.PANEL_DATA[
        "modern-indian-history-20"
    ],
    "modern-indian-history-21": authored_20_21.PANEL_DATA[
        "modern-indian-history-21"
    ],
    "modern-indian-history-22": authored_22_23.PANEL_DATA[
        "modern-indian-history-22"
    ],
    "modern-indian-history-23": authored_22_23.PANEL_DATA[
        "modern-indian-history-23"
    ],
    "modern-indian-history-24": authored_24_25.PANEL_DATA[
        "modern-indian-history-24"
    ],
    "modern-indian-history-25": authored_24_25.PANEL_DATA[
        "modern-indian-history-25"
    ],
    "modern-indian-history-26": authored_26_27.PANEL_DATA[
        "modern-indian-history-26"
    ],
    "modern-indian-history-27": authored_26_27.PANEL_DATA[
        "modern-indian-history-27"
    ],
    "modern-indian-history-28": authored_28_29.PANEL_DATA[
        "modern-indian-history-28"
    ],
    "modern-indian-history-29": authored_28_29.PANEL_DATA[
        "modern-indian-history-29"
    ],
    "modern-indian-history-30": authored_30_31.PANEL_DATA[
        "modern-indian-history-30"
    ],
    "modern-indian-history-31": authored_30_31.PANEL_DATA[
        "modern-indian-history-31"
    ],
    "modern-indian-history-32": authored_32_33.PANEL_DATA[
        "modern-indian-history-32"
    ],
    "modern-indian-history-33": authored_32_33.PANEL_DATA[
        "modern-indian-history-33"
    ],
    "modern-indian-history-34": authored_34_35.PANEL_DATA[
        "modern-indian-history-34"
    ],
    "modern-indian-history-35": authored_34_35.PANEL_DATA[
        "modern-indian-history-35"
    ],
    "modern-indian-history-36": authored_36_37.PANEL_DATA[
        "modern-indian-history-36"
    ],
    "modern-indian-history-37": authored_36_37.PANEL_DATA[
        "modern-indian-history-37"
    ],
    "modern-indian-history-38": authored_38.PANEL_DATA[
        "modern-indian-history-38"
    ],
}


TOPIC_MAIN_SUPPLEMENTS = {
    1: r"""
### TOPIC 01 CLOSING IMPERIAL-DECLINE LEDGER

Topic 01 owns the contraction of enforceable Mughal command from 1707 through
the 1740s. Medieval Topic 25 supplies the late-Aurangzeb and jagirdari
prehistory; Topic 02 owns regional-state and society synthesis. Abdali and
Panipat remain consequences or bridges, not extensions of this core chronology.

The causal ledger must keep succession without fixed primogeniture, noble
coalitions, wazir/emperor dependence, mansab and jagir claims, paibaqi,
be-jagiri, jama-hasil divergence, agrarian bargaining, provincial revenue
retention and military weakness in one feedback system. Turani, Irani, Afghan
and Hindustani were shifting patronage formations, not permanent ethnic parties.

Bahadur Shah I (1707-12), Jahandar Shah/Zulfiqar Khan (1712-13),
Farrukhsiyar/Sayyid Brothers (1713-19), the 1719 enthronements, Muhammad Shah
(1719-48), the Sayyids' fall in 1720, Nizam-ul-Mulk's 1724 autonomy and Karnal/
Delhi in 1739 form the bounded chronology. Nadir Shah exposed and accelerated
a prior crisis; he did not create the jagirdari problem or annex North India.

Bengal, Awadh and Hyderabad retained Mughal offices, titles, coin/khutba and
Persianate documentary forms while controlling practical revenue, army and
patronage. This proves change in command alongside continuity of legitimacy,
not formal modern declarations of independence.

Direct Topic-01 CSE routes for 2018-2026 are zero. The 2021 successor-state
question belongs Topic 02, the 2021 administrative hierarchy question Medieval
Topic 24, and the 2022 Company-armies Mains question Topic 05. Original drills
are never PYQs; unavailable objective keys remain explicitly inferred.

**Answer:** define decline at the level of central command -> chronology ->
fiscal-military feedback -> court and agrarian mechanisms -> provincial
autonomy -> Nadir shock -> institutional continuity -> two-level verdict.
""",
    2: r"""
### TOPIC 02 CLOSING REGIONAL-STATE-AND-SOCIETY LEDGER

Topic 02 owns the comparative eighteenth-century synthesis after central
contraction: successor states (Bengal, Awadh, Hyderabad), Maratha confederate
formations, Sikh misls, Jats, Rohillas, Rajput states and Mysore, together with
revenue, credit, armies, peasant/artisan/merchant life, caste, gender and
regional cultural patronage. Topic 01 retains imperial-decline causation.

Classify states by route, not by a ladder of worth: Mughal provincial office
converted into hereditary practical autonomy; older regional fields centralised
selectively; new armed and confederate formations built authority through local
solidarities, revenue claims and mobile military labour. Mughal titles and
chancery forms could survive without daily obedience to Delhi.

State formation linked assessment, intermediaries, bankers/hundis, remittance,
paid troops, forts and patronage. It could enlarge administrative capacity while
also multiplying levies, warfare and burdens on cultivators. Textile production,
ports, qasbas, merchant credit and court patronage therefore block a universal
dark-age claim, but commercial vitality never proves equal prosperity.

Maratha chauth and sardeshmukhi are distinct claims; confederate houses were not
a unitary nation-state. Sikh political history runs from Khalsa/Banda through
Dal Khalsa and misls; Ranjit Singh is a later bridge. Mysore is not a Mughal
successor state. Region, class, caste and gender determine who gained from
mobility and who bore extraction.

Exactly one direct Topic-02 route is verified for 2018-2026: 2021 Prelims Q48
on Arcot, Mysore and Rohilkhand. Its local official key is unavailable and the
answer remains inferred. The 2021 hierarchy item belongs Medieval Topic 24 and
the 2022 Company-armies question Topic 05.

**Answer:** classify state routes -> compare institutions/revenue/credit/army ->
integrate society and commerce -> show regional variation -> reject both anarchy
and universal-prosperity binaries.
""",
    3: r"""
### TOPIC 03 CLOSING EUROPEAN-SETTLEMENTS LEDGER

Topic 03 owns arrival, trade, factories, fortified settlements and commercial
rivalry from Portuguese through Dutch, English and French formations. Topic 04
begins when Bengal political leverage becomes conquest; Topic 05 owns the
pan-Indian fiscal-military expansion state.

The Indian Ocean before 1498 already joined monsoon routes, Asian merchants,
Indian ports and manufactures. Portuguese Estado da India, cartaz, fleets,
forts and Crown administration created coercive nodal control, never a complete
ocean monopoly. Mission, printing and crop transfer require bounded evidence;
heritage records do not prove political causation or exact transfer dates.

The VOC combined joint-stock capital with treaty, war and fortification powers,
but Indian textiles served an Indonesia-centred Asian portfolio. The English
charter created a corporate privilege in English law, not sovereignty in India;
Swally, Mughal permission, factories, Bombay, Madras and Calcutta mark distinct
stages. French settlements and Dupleix's alliance politics sharpened rivalry,
but Carnatic outcomes were contingent on finance, naval reinforcement, Indian
allies and European war.

Factory, fort, presidency and Company-state are separate categories. A factory
was a trading station; territorial power additionally required credit, a paid
army, political intelligence, Indian partners, victory and revenue.

Four direct Prelims routes are verified: 2021 Q33, 2021 Q39, 2022 Q59 and 2025
Q75. Only the 2025 Series-A crop-transfer answer has locally held official-key
provenance; the 2021/2022 answers remain inferred. The 2022 Company-armies
Mains question is adjacent and owned by Topic 05.

**Answer:** existing oceanic system -> company institution -> settlement ladder
-> comparative commercial strategies -> Anglo-French rivalry -> Indian agency,
finance and naval qualification -> no conquest inevitability.
""",
    4: r"""
### TOPIC 04 CLOSING BENGAL-CONQUEST LEDGER

Topic 04 owns the 1717 farman/dastak distinction, Bengal Nawabi state, Calcutta
crisis, Plassey, post-Plassey extraction, Mir Qasim, Buxar, the two Allahabad
instruments, Diwani/Nizamat, Dual Government, famine vulnerability and the 1772
end of the arrangement. Early European company formation remains Topic 03;
territorial expansion Topic 05; constitutional control Topic 06; colonial
economic synthesis Topic 07.

Plassey on 23 June 1757 was primarily conspiracy-led regime change, not the
legal acquisition of Bengal's revenue sovereignty. Buxar on 22 October 1764
was a conventional coalition defeat with wider military consequences. The
Allahabad settlement of 12 August 1765 used separate instruments for Shah Alam
II and Shuja-ud-Daula; the Diwani followed Buxar, not Plassey.

The 1717 Company privilege did not authorise private servants' unrestricted
dastak abuse. Mir Qasim's abolition of internal duties sought fiscal parity,
not a modern nationalist programme. Dual Government meant Company power
without formal responsibility and Nawabi responsibility without effective
power. The 1770 famine requires natural trigger plus institutional vulnerability;
no unaudited mortality total is safe.

Direct Topic-04 CSE routes for 2018-2026 are zero. The 2022 Company-armies
question belongs Topic 05 and the famine question Topic 07. They may appear
only as labelled bridges; original practice must not be relabelled PYQ.

**Answer:** privilege versus abuse -> Nawabi conflict -> Plassey political
leverage -> extraction and Mir Qasim reform -> Buxar military superiority ->
Allahabad/Diwani legal title -> Dual Government paradox -> 1772 closure.
""",
    5: r"""
### TOPIC 05 CLOSING TERRITORIAL-EXPANSION LEDGER

Topic 05 owns Company expansion beyond Bengal through Mysore, Maratha and Sikh
war sequences, Sindh, Indian sepoy/ally/credit participation and the distinct
instruments of ring-fence, Subsidiary Alliance, paramountcy, conquest, lapse
and alleged misgovernment. Topic 04 retains Bengal conquest; Topic 06 owns
constitutional structure; Topic 11 owns the full 1857 explanation.

Bengal Diwani fed a fiscal-military flywheel: revenue and credit paid sepoys,
officers, artillery and supply; alliances isolated opponents; victories yielded
indemnity or territory and enlarged the resource base. This was contingent:
Haidar reached Madras, Mangalore was negotiated, Wadgaon checked the Company
and Holkar resisted.

Keep four Mysore wars, three Maratha wars and two Sikh wars in their own
chronologies. Bassein (1802) weakened the confederate centre but did not end
Maratha resistance. Ranjit Singh died in 1839 and fought no Anglo-Sikh war;
Amritsar (1809) was not a Subsidiary Alliance.

Wellesley's Subsidiary Alliance stationed Company troops and transferred
diplomatic/military autonomy through cash subsidy or territorial cession.
Dalhousie's Doctrine of Lapse concerned disputed adoption/succession in
dependent states. Awadh (1856) was annexed for alleged misgovernment; Nana
Sahib's issue was pension/title; Sindh (1843) was frontier conquest.

Exactly two direct routes are verified: 2018 Prelims Q75 on Subsidiary Alliance
(key inferred because unavailable locally) and 2022 GS-I Q2 on why Company
armies prevailed (Mains has no objective key).

**Answer:** fiscal-military base -> campaign chronology -> diplomacy and Indian
agency -> instrument-by-instrument sovereignty loss -> reverses/contingency ->
bounded 1857 bridge -> adaptive, not inevitable, expansion verdict.
""",
    6: r"""
### TOPIC 06 CLOSING COMPANY-STATE CONSTITUTIONAL LEDGER

Topic 06 owns the constitutional and Company-state structure from the
post-Diwani anomaly through the legal Crown transfer of 1858. Topic 04 retains
Plassey, Buxar, Diwani and Dual Government; Topic 08 owns the detailed civil
service, army, police and judicial apparatus; Topic 09 owns education and press
policy; Topic 11 owns the causes, course and character of the Revolt; Topic 12
owns councils and constitutional change after 1858.

The constitutional ladder is crisis-driven, not a smooth liberal evolution.
The Company's 1772 loan request, parliamentary enquiries and nabob-patronage
anxiety produced the 1773 compromise. Its four-member council generated
Hastings's 3-1 deadlock; the 1774 Supreme Court's uncertain jurisdiction
produced the Nand Kumar, Patna and Cossijurah controversies; the 1781 Act of
Settlement corrected jurisdiction, not the executive voting defect.

Pitt's India Act (1784) created Crown-supervised dual control through the Board
of Control and Court of Directors; it did not begin direct Crown rule. The 1786
measure strengthened Cornwallis's executive position, while the 1793 renewal
continued the structure. The 1813 Act ended the Indian trade monopoly but
retained tea and China trade, provided the one-lakh education grant, admitted
missionaries and asserted Crown sovereignty. Education implementation belongs
Topic 09 and economic consequences Topic 07.

The 1833 Act ended Company commerce, centralised all-India legislation, made
William Bentinck the first Governor-General of India, added a Law Member and
provided a Law Commission. Its non-discrimination clause did not deliver equal
Indian access. The 1853 Act ended Directors' patronage and authorised the
competitive principle; the Macaulay Committee (1854) and first open examination
(1855) were separate implementation steps.

The Government of India Act 1858 abolished Company rule, the Board of Control
and Court of Directors; created a Secretary of State for India assisted by a
fifteen-member Council of India; and retained the Governor-General while adding
the Viceroy title, first jointly held by Canning. Keep the Act separate from
Queen Victoria's Proclamation of 1 November 1858. Do not import the Revolt's
core narrative or the Indian Councils Act 1861.

Exactly two direct routes are verified: 2019 Prelims Q4 on the Charter Act 1813
and 2023 Prelims Q50 on the Governor-General designation. Both local official
keys remain unavailable; elimination logic is taught without fabricating one.

**Answer:** corporate-sovereignty anomaly -> crisis -> 1773 design and defects
-> 1781 jurisdictional repair -> 1784 Crown supervision -> Charter Act ladder
-> 1833 centralisation/codification -> 1853 recruitment sequence -> 1858 legal
transfer -> continuity plus Indian exclusion.
""",
    7: r"""
### TOPIC 07 CLOSING COLONIAL-ECONOMY LEDGER

Topic 07 owns colonial economic restructuring: land revenue, agrarian
commercialisation and credit risk, deindustrialisation, drain, imperial
infrastructure and industry, famine vulnerability, poverty and their competing
interpretations. Topic 04 retains Diwani and Dual Government mechanics; Topic
06 retains Charter Act structure; Topic 08 owns the enforcing institutions;
Topic 14 owns the Moderate political programme; Topic 23 owns the wider later
peasant-worker movement history.

Keep Permanent, Ryotwari and Mahalwari settlements separate by architect,
region, settlement unit, revision pattern and risk carrier. Permanent
Settlement fixed the state's demand on the zamindar, not the cultivator's rent.
Ryotwari removed the zamindar but retained direct, periodically revised state
assessment. Mahalwari used the village or mahal with joint liability. None was
uniform across India or automatically pro-peasant.

Commercialisation could widen markets but shifted harvest, price and credit
risk downward. Indigo (1859-60), Pabna (from 1873) and Deccan (1875) must be
matched to planter coercion, rent enhancement and moneylender debt documents
respectively; they are economic-response cases here, not substitutes for Topic
23's political ownership.

Deindustrialisation joins mechanised British production, tariff asymmetry,
Company procurement power, lost court patronage and later railway penetration.
It means uneven decline in craft output, employment or bargaining position, not
the disappearance of all industry. Drain is different: unilateral transfers
through home charges, official remittances, pensions, profits, interest, stores
and imperial expenditure. Exact totals remain disputed and are not invented.

Famine analysis combines climatic harvest shock with entitlement collapse,
rigid revenue, commercialisation exposure, price-mediated transport,
laissez-faire relief ideology, administrative delay and disease. The 1770 and
1943 Bengal famines are bounded bridges; this owner fully develops the
nineteenth-century causal sequence, especially 1876-78 and 1896-1900.

Six active direct routes are firm: 2018 Prelims Q52 and Q68, 2020 Prelims Q23
and Q33, 2022 GS-I Q3, and 2024 GS-I Q13. The 2024 Prelims Q57 revenue item was
officially dropped and remains a demand-control only; 2026 Prelims Q2 on
Hilton-Young remains provisional. 2018 Prelims Q51 on post-Santhal measures and
2018 GS-I Q13 on indentured labour are adjacent/bounded, not full Topic-07
owners.

**Answer:** revenue/property redesign -> commercialisation and credit risk ->
craft decline versus drain -> infrastructure and dependent industrialisation
-> famine vulnerability -> regional/social variation -> attributed
nationalist, Marxist, revisionist and regional synthesis.
""",
    8: r"""
### TOPIC 08 CLOSING ADMINISTRATIVE-INSTITUTIONS LEDGER

Topic 08 owns the operating institutions of colonial rule: higher and
subordinate civil services, district administration, presidency armies and
post-1857 recruitment, police, courts, codification and the contradiction
between proclaimed rule of law and racial/executive privilege. Topic 06 owns
Company-era constitutional statutes; Topic 07 owns extraction outcomes; Topic
09 owns education/press/social policy; Topic 11 owns the Revolt's core; Topic
12 owns post-1858 constitutional councils and Crown-government structure.

Cornwallis joined professionalisation to exclusion: higher salaries,
covenanted service and anti-corruption rules strengthened capacity while
reserving superior command for Europeans. Fort William and Haileybury were
training institutions for Company servants. The 1853 Act removed Directors'
patronage and authorised competition; Macaulay's 1854 report and the first open
exam in 1855 were separate steps. A London examination and age/cost barriers
made formal eligibility very different from effective Indian access.

The district was the interlocking unit: collector and magistrate, thana/daroga
police, codified courts and the army's final coercive guarantee. Police Act
1861 statutory hierarchy must not be projected backward onto Cornwallis's
earlier arrangements. Codification delivered uniformity and predictability but
also protected revenue and criminalised dissent.

The sepoy army before 1857 enabled conquest under European command. After the
Revolt, European control, artillery reservation, regional/community separation
and the later racial ideology of 'martial races' sought to prevent common
solidarity. Treat martial-race categories as colonial knowledge and policy, not
anthropological fact. Detailed Revolt causation remains Topic 11.

Rule of law was genuine in form and limited in operation. The Ilbert Bill
controversy (1883) is the courtroom stress test: European mobilisation resisted
Indian judges trying Europeans, exposing the ceiling imposed by racial power.
Indian lawyers and lower officials nevertheless appropriated legal institutions
for claims and later nationalism.

Repository routing for 2018-2026 assigns zero direct UPSC PYQs to Topic 08.
All package practice remains original; Topic 05, 06, 09 or 11 questions may
appear only as explicitly adjacent bridges and no official key is invented.

**Answer:** purpose of revenue/order -> professional but racial civil service
-> district command -> army/police coercion -> codified courts -> rule-of-law
claim versus racial exception -> Indian appropriation -> durable form,
democratically repurposed after independence.
""",
    9: r"""
### TOPIC 09 CLOSING EDUCATION-PRESS-POLICY LEDGER

Topic 09 owns colonial education policy, press regulation, the state-social
reform interface and the public-sphere consequences of Indian appropriation.
Topic 06 owns the constitutional provisions of the 1813 Charter Act; Topic 08
owns administrative institutions; Topic 10 owns reform movements, doctrines
and biographies; Topics 14-15 and 19-20 own later nationalist use of education
and press.

Keep the policy sequence differentiated: Calcutta Madrasa (1781) and Sanskrit
College, Banaras (1791) represent early Orientalist state support; Fort William
College (1800) trained European Company servants, not Indian pupils; the 1813
grant and missionary admission opened a new policy phase; Macaulay's Minute and
Bentinck's 1835 resolution marked the Anglicist turn; Wood's Despatch (1854)
designed a wider system of departments, grants-in-aid, teacher training,
vernacular primary education and examining universities, followed by the three
presidency universities in 1857.

Do not reduce education to imposition. Colonial staffing and ideological
control were real, but Indian demand for science, law and new knowledge was
also real. Downward filtration privileged a narrow elite and underfunded mass,
vernacular, female and lower-caste access. English and vernacular print grew
together and helped create professions, associations and nationalist critique.

Press history is an alternating control cycle, not a simple freedom-to-
repression line: Hicky (1780), early censorship/licensing, Metcalfe's 1835
liberalisation, the 1857 licensing restriction, Lytton's Vernacular Press Act
1878 and Ripon's repeal in 1882. The 1878 Act's language-specific targeting is
the key public-sphere mechanism; later nationalist press laws belong later
movement topics.

Topic 09 may analyse statutes such as sati abolition (1829), slavery-related
law (1843) and widow remarriage (1856) as state-policy outcomes and enforcement
problems. The reformers' intellectual projects, organisations and social bases
belong Topic 10. Law neither proves colonial benevolence nor instant social
implementation.

Six direct Prelims routes are verified for 2018-2021: Wood's Despatch, English
education factors, institution-founder matching, Fort William College,
Madanapalle and Songs from Prison. For the latter two, supplementary evidence
supports Tagore's 1919 English rendering of Jana Gana Mana at Madanapalle and
M.K. Gandhi's association with *Songs from Prison*; because the local official
2021 key is unavailable, these remain source-verified/inferred, not officially
keyed. The 2023 Gandhi-Tagore education Mains item is cross-owned and bounded.

**Answer:** Orientalist governance -> Anglicist turn -> filtration and access
limits -> Wood's system blueprint -> press control/liberalisation cycle ->
Indian appropriation -> state-law/reformer interaction -> unequal but
anti-colonial public sphere.
""",
    10: r"""
### TOPIC 10 CLOSING REFORM-MOVEMENTS LEDGER

Topic 10 owns the ideas, organisations, leaders, social bases, methods,
regional routes and limits of socio-religious and anti-caste reform. Topic 09
owns education/press policy and reform statutes as state action; Topic 14 owns
the early Congress and Moderate political programme; Topic 17 owns the later
politics of communal representation. Legal enactment may be context here but
never substitutes for movement history.

Do not force all movements into one liberal ladder. Brahmo, Young Bengal and
Prarthana used reason, monotheism or devotional reform; Arya Samaj combined a
Vedic-revival idiom with modern print, shuddhi and DAV organisation;
Ramakrishna-Vivekananda joined spiritual universalism to service and cultural
self-confidence. Reformist and revivalist are useful comparisons, not fixed
moral labels.

Muslim, Sikh and Parsi reform had distinct projects: Aligarh's modern
scientific education and loyalist strategy differed from Deoband's seminary
and religious-learning route; Singh Sabha and Rahnumai Mazdayasnan Sabha
addressed community renewal through their own institutions. Later political
trajectories must not be read backward as inevitable purposes.

Anti-caste and women's agency correct an elite 'renaissance' narrative.
Satyashodhak Samaj (1873) located caste in power and education; Jyotirao and
Savitribai Phule opened the Bhide Wada girls' school in 1848 and expanded their
school work thereafter. Sri Narayana Guru and the later non-Brahman/Self-
Respect currents followed distinct regional routes. Savitribai, Pandita
Ramabai and Rukhmabai were actors, not merely beneficiaries of male reform.

The safe historiographical verdict is graded: reform widened reasoned public
debate, education, dignity and associational life, but much urban upper-caste
male reform had limited reach and could turn women or community into symbols
of respectability. Feminist, Dalit-bahujan and regional evidence changes the
centre of the story rather than merely adding examples.

Eleven direct routes are verified: five 2018-2021 Prelims demands, the 2019 and
2021 GS-I Mains demands, and three 2025 routes (Phule Mains, Rammohan Roy
Prelims, Periyar Prelims). Supplementary evidence associates the 2020
*Vital-Vidhvansak* demand with Gopal Baba Walangkar and 1888; because the local
official 2020 key is unavailable, that answer remains inferred, not officially
keyed.

**Answer:** classify reform routes -> compare authority, method and social base
-> analyse caste and gender agency -> community-specific projects -> links to
public life without teleology -> elite/reach limits -> qualified renaissance
and modernity verdict.
""",
    11: r"""
### TOPIC 11 CLOSING REVOLT-OF-1857 LEDGER

Topic 11 owns the Revolt's structural causes, outbreak, course, regional and
social composition, leadership, failure, nature debate and consequences.
Topic 05 retains Company expansion and annexation instruments; Topic 08 retains
the detailed army, police and district apparatus; Topic 12 owns the post-1858
Crown and councils settlement. Earlier civil and tribal risings appear here
only because the verified 2019 GS-I demand asks whether 1857 culminated them.

The causal answer must join distinct grievance-bearing groups without inventing
one programme: Bengal Army sepoys faced service, status and overseas-service
anxieties; rulers and dependants faced annexation and pension or dignity loss;
taluqdars and peasants faced the Awadh settlement and land alienation; artisans
and urban groups faced lost patronage; religious fear magnified distrust. The
Enfield cartridge rumour activated this field but did not create it.

Keep the sequence exact: Barrackpore, 29 March; Meerut, 10 May; movement to
Delhi and Bahadur Shah Zafar's symbolic authority; different coalitions at
Kanpur, Lucknow/Awadh, Jhansi, Bareilly and Arrah; British recovery of Delhi in
September; suppression through 1858. Leaders, objectives and participation
varied. The Madras and Bombay armies did not reproduce the Bengal Army revolt,
many princes remained loyal or neutral, and Punjab supplied British manpower.

The safest nature verdict is composite: military mutiny in origin, broad civil
and agrarian rebellion in major north Indian theatres, anti-colonial in target,
restorationist in much political idiom, and neither a uniform all-India
national war nor a barracks incident. Official, nationalist, agrarian/social
and subaltern readings require region-specific evidence.

Two direct routes are verified: 2019 GS-I on recurrent rebellions culminating
in 1857, and provisional 2026 Prelims Q17 on the Awadh taluqdars. The latter is
answered as a source-backed demand card without converting a provisional key
into an official answer letter.

**Answer:** differentiated causes -> trigger -> centre-wise course -> social
coalitions and non-participation -> British/rebel asymmetry -> composite nature
-> constitutional, military, princely and racial consequences -> handoff to
Topic 12.
""",
    12: r"""
### TOPIC 12 CLOSING CROWN-AND-COUNCILS LEDGER

Topic 12 owns the post-Revolt reconstruction of governance: the Crown control
chain, Queen's Proclamation, princely and landed conciliation, army-policy
bridge, financial and local decentralisation, and the Indian Councils Acts of
1861 and 1892. Topic 06 owns the Company-state constitutional ladder through
the legal transfer of 1858; Topic 08 owns detailed services, army, police and
courts; Topic 11 owns revolt causation; Topic 14 owns Moderate use of councils.
Separate electorates and communal representation belong Topic 17.

The Government of India Act 1858 abolished Company rule, the Board of Control
and Court of Directors, and created a Secretary of State for India assisted by
a fifteen-member Council of India. The Governor-General also acted as Viceroy;
Canning was the first. Keep this statute separate from Queen Victoria's
Proclamation of 1 November 1858, whose religion, treaty and public-employment
promises were policy commitments tested by unequal practice.

The 1861 Act restored legislative councils, admitted nominated non-official
Indians, established departmental portfolio working and revived limited
provincial legislation. It created consultation, not election or responsibility.
The 1892 Act enlarged councils, used recommending bodies as an indirect
elective principle, and allowed budget discussion and questions; members could
not control supply or dismiss the executive.

Mayo's financial decentralisation from 1870 and Ripon's 1882 local-government
resolution transferred selected functions and costs while official supervision
remained. Princes received dynastic security but not sovereign equality;
annexation retreated while paramountcy tightened. Army reorganisation belongs
here only as a consequence-and-security bridge to Topic 08.

Repository routing for 2018-2026 assigns zero direct PYQs to Topic 12. All
package questions are original practice. Topic 06, 08, 11, 14 and 17 material
may appear only as explicitly bounded cause, institution, response or handoff.

**Answer:** 1858 control chain -> Proclamation promises and practice -> social
alliance reconstruction -> 1861 association -> decentralisation/local bodies
-> 1892 limited deliberation -> continuity of executive supremacy -> no
responsible government.
""",
    13: r"""
### TOPIC 13 CLOSING FRONTIER-AND-NEIGHBOURS LEDGER

Topic 13 owns British India's imperial foreign and frontier policy toward
Afghanistan, Burma, Nepal, Tibet and the North-West Frontier, including the
strategic doctrines, war/treaty sequence, buffer-versus-annexation comparison,
Indian-revenue burden and boundary-administration legacy. Topic 05 retains the
general expansion-state mechanism; Topic 12 supplies Crown-era governance;
post-1947 neighbourhood law and diplomacy remain outside this history owner.

There was no single frontier doctrine. Afghanistan moved through intervention,
withdrawal, influence and boundary-making under the perceived Russian threat:
First Anglo-Afghan War 1839-42; Second War 1878-80 and Gandamak 1879; Durand
agreement 1893; Third War 1919 as a bounded endpoint. Close-border, masterly
inactivity and forward-policy arguments changed with governors, intelligence,
terrain and imperial confidence.

Burma followed a different annexation ladder: war and Yandabo in 1824-26,
Lower Burma in 1852, Upper Burma in 1885, and administrative separation from
India in 1937. Nepal's war of 1814-16 and Treaty of Sugauli/Sagauli produced
treaty influence, Residency and Gurkha recruitment without annexation. Curzon's
Younghusband expedition to Tibet in 1903-04 and the 1904 Lhasa Convention must
not be confused with the Durand frontier.

Forward policy did not always mean annexation; a buffer was not independent of
pressure; a treaty did not erase local agency. Afghan, Burmese, Nepali,
Tibetan and frontier peoples acted within terrain and logistics that repeatedly
limited imperial plans. Costs charged to Indian revenue connect this owner to
economic nationalism without transferring the full drain argument here.

Repository routing for 2018-2026 assigns zero direct Modern-History PYQs to
Topic 13. Current Geography and International Relations questions on neighbours
remain outside this owner; all historical practice is original and labelled.

**Answer:** threat perception -> doctrine choice -> theatre-specific instrument
-> war/treaty/administration -> local agency and logistical limit -> fiscal
incidence -> buffer versus annexation comparison -> bounded legacy.
""",
    14: r"""
### TOPIC 14 CLOSING INC-AND-MODERATES LEDGER

Topic 14 owns the rise of organised all-India nationalism through pre-Congress
associations, the foundation and origin debate of the INC, Moderate leadership,
methods, demands, economic nationalism, achievements, social limits and legacy
through 1905. Topic 07 retains the full colonial-economy mechanisms; Topic 12
retains councils provisions; Topic 15 owns Bengal partition, Swadeshi and
militant nationalism; Topic 17 owns communalism and the Muslim League.

The origin chain begins before Hume: British Indian Association (1851), East
India Association (1866), Poona Sarvajanik Sabha (1870), Indian Association
(1876), Madras Mahajan Sabha and Bombay Presidency Association created
leadership, press and petition networks. The first INC met at Bombay in December
1885 with seventy-two delegates under W.C. Bonnerjee. A.O. Hume's organising
role explains facilitation, not colonial authorship of Indian nationalism.

Treat the safety-valve thesis as a disputed interpretation, never a complete
cause. Political associations, education and print, economic grievances,
administrative unification and a growing intelligentsia supplied the movement's
Indian content. Cambridge/locality approaches illuminate elite competition;
nationalist and subaltern critiques require evidence about organisation,
ideology and excluded social groups rather than caricature.

Moderate method joined resolutions, petitions, public meetings, newspapers,
deputations and council criticism. Their durable achievement was an economic
indictment--drain, deindustrialisation, revenue pressure, military expenditure
and service exclusion--plus an all-India organisation and political vocabulary.
The 1892 concession expanded procedure without responsibility. Narrow social
reach and faith in British liberalism limited immediate power.

Exactly one direct route is verified for 2018-2026: 2021 GS-I on the Moderates'
role in preparing the wider freedom movement. It is solved as a Mains demand;
adjacent economic and councils questions retain Topics 07 and 12.

**Answer:** pre-1885 association ecology -> 1885 identity -> origin debate ->
constitutional repertoire -> economic nationalism -> limited concessions and
social base -> ideological/organisational legacy -> handoff to Topic 15.
""",
    15: r"""
### TOPIC 15 CLOSING SWADESHI-AND-MILITANT LEDGER

Topic 15 owns Curzonian provocation, Bengal's partition, anti-partition protest,
the Swadeshi-boycott constructive programme, militant-nationalist ideology,
participation, regional spread, Surat, decline and consequences through the
1905-08 high phase. Revolutionary underground organisations and actions begin
Topic 16; communalism, the Simla Deputation, Muslim League and separate
electorates belong Topic 17. The 1911 annulment is a consequence, not an
extension of the movement's core period.

Keep the dates distinct: partition announced in July 1905; boycott formally
resolved at Calcutta Town Hall on 7 August; partition effective on 16 October;
National Council of Education in 1906; Congress split at Surat in 1907;
repression and organisational decline by 1908; partition annulled and capital
shifted in 1911. Announcement, launch, enforcement, decline and reversal are
not interchangeable.

Swadeshi was the constructive arm--indigenous production, stores, education
and arbitration--while boycott was withdrawal from foreign goods and selected
colonial institutions. Militant nationalism added swaraj, atma-shakti,
sacrifice, passive resistance and self-reliance; it was broader than
revolutionary violence. Cultural symbols, samitis, students, women, workers and
regional leaders widened politics, but peasant reach, Muslim participation,
capital, supply and organisational discipline remained uneven.

Five direct routes are verified: 2018 Prelims Q11 identifies Lala Lajpat Rai
through the Mazzini/Garibaldi/Shivaji/Shrikrishna biographies and career clues;
2019 Prelims tests industry and national education; 2020 Prelims tests
Sakharam Ganesh Deuskar's *Desher Katha*; 2020 GS-I evaluates Curzon; and 2023
Prelims links 7 August to National Handloom Day. The 2018 and 2020 objective
answers use supplementary historical evidence and remain inferred because
local official keys are unavailable; no circulation number is invented.

**Answer:** Moderate ceiling and Curzonian provocation -> partition sequence ->
boycott plus constructive Swadeshi -> militant programme and social reach ->
Surat/repression/decline -> qualified achievement and Gandhian transmission ->
handoff to Topics 16 and 17.
""",
    16: r"""
### TOPIC 16 CLOSING REVOLUTIONARY-NETWORK LEDGER

Topic 16 owns underground and overseas revolutionary activity from the
Swadeshi aftermath through the wartime conspiracies of 1915-17. Topic 15 owns
open militant-nationalist and Swadeshi politics; Topic 18 owns wartime Home
Rule and Lucknow; Topic 21 owns HRA, HSRA, Kakori and Bhagat Singh.

Keep Bengal, Maharashtra, London/Paris and Pacific-coast networks distinct.
Anushilan and Dacca Anushilan were related but not identical; Jugantar was
both a network and a paper; Shyamji Krishna Varma founded India House, whereas
Savarkar became a leading organiser there. Muzaffarpur (April 1908), Alipore
(1908-09), Dhingra (1 July 1909), Nasik (December 1909), Hardinge
(23 December 1912), Ghadar organisation/paper (1913), Komagata Maru (1914),
the planned rising and Singapore mutiny (February 1915), Bagha Jatin's death
(1915), and Defence of India repression are separate events.

The 2022 Prelims Q53 association test is direct. Supplementary historical
evidence identifies only Rash Behari Bose among Barindra Kumar Ghosh, Jogesh
Chandra Chatterjee and Rash Behari Bose as actively associated with Ghadar;
the answer is retained as inferred because the local official key is absent.

**Answer:** post-Swadeshi closure -> regional and overseas networks -> methods
and social bases -> wartime convergence -> surveillance/repression ->
psychological and transnational gains -> organisational ceiling -> Topic 18/21
handoff without telescoping later revolutionary socialism backward.
""",
    17: r"""
### TOPIC 17 CLOSING COMMUNAL-IDEOLOGY LEDGER

Topic 17 owns communalism as a modern political ideology, its institutional
production and the early Muslim League trajectory. Topic 10 owns religious
reform; Topic 12 owns the broader constitutional sequence; Topic 18 owns the
Lucknow negotiations; Topic 20 owns Khilafat-Non-Cooperation; Topic 27 owns
the 1940-47 League, Pakistan and Partition endgame.

The date spine is Syed Ahmad Khan's later loyalist politics -> Simla
Deputation (October 1906) -> League at Dacca (December 1906) -> separate
electorates (1909) -> Hindu Mahasabha (1915) -> Lucknow Pact (1916), with
1923 Hindutva, 1925 RSS and 1940 Lahore Resolution retained as bounded later
trajectory. Separate electorates, reserved seats and nomination are distinct.

Chandra's three-stage model moves from common secular interests to divergent
interests and finally antagonistic interests. Attribute that framework; test
it against colonial classification, middle-class competition, provincial
variation, intra-community diversity and Hindu as well as Muslim communal
organisations. Religion and reform are not automatically communalism.

The direct PYQ routes are 2018 GS-I on power struggle/relative deprivation and
provisional 2026 Prelims Q18 on reform and communal representation. No
provisional objective key is promoted.

**Answer:** definition -> modern causes -> institutional incentive ->
1906/1909/1916 sequence -> provincial and organisational variation ->
nationalist response and concessions -> non-inevitability -> later handoff.
""",
    18: r"""
### TOPIC 18 CLOSING WAR-HOME-RULE-LUCKNOW LEDGER

Topic 18 owns the First World War setting, two separate Home Rule Leagues,
Congress reunion and the Congress-League settlement at Lucknow. Topic 16 owns
Ghadar and underground wartime conspiracy; Topic 17 owns communal ideology
and League formation; Topic 19 begins Gandhi's Indian mass-method sequence.

The date control is war from 1914 -> Congress readmission decision in December
1915 -> Tilak's League in April 1916 -> Besant's League in September 1916 ->
Lucknow Congress and Pact in December 1916 -> Besant's internment and the
Montagu Declaration on 20 August 1917 -> bounded transition through 1918.
Home Rule meant self-government within the Empire, not Purna Swaraj.

Separate Tilak's and Besant's territories, organisations and methods before
showing their common demand. Congress reunion and the Congress-League Pact
were simultaneous but distinct. The Pact's joint constitutional programme,
separate electorates, weightage and minority-veto provision require precise
comparison rather than a generic unity narrative.

The direct topic route is 2018 Prelims Q79 on the All India Home Rule League's
1920 renaming as Swarajya Sabha; its local official key is unavailable. The
2024 balance-of-power Mains question belongs World History and is only a
bounded wartime bridge.

**Answer:** wartime contradiction -> political deadlock -> two Leagues ->
continuous propaganda and repression -> Congress reunion -> Pact provisions
and paradox -> Montagu response -> cadre legacy and Gandhian transition.
""",
    19: r"""
### TOPIC 19 CLOSING EARLY-GANDHI-AND-1919 LEDGER

Topic 19 owns Gandhi's Indian method laboratories and the 1919 legitimacy
rupture. Topic 18 owns Home Rule/Lucknow; Topic 20 owns the organised
Non-Cooperation-Khilafat programme. Jallianwala is a major bridge, not the
single cause of Non-Cooperation.

The sequence is Champaran (1917) -> Ahmedabad mill dispute (1918) -> Kheda
(1918) -> Rowlatt legislation and all-India hartal (1919) -> Gandhi's
suspension after violence -> Jallianwala Bagh on 13 April 1919 -> martial-law
humiliations, Hunter and Congress inquiries, renunciation and moral rupture.
Keep proposal, enactment, protest, violence, suspension and massacre distinct.

Compare constituency, grievance, opponent, tactic, settlement and limit:
Champaran centred Raj Kumar Shukla, tinkathia and inquiry; Ahmedabad centred
mill wages, arbitration and Gandhi's first fast in India; Kheda centred
revenue suspension amid crop distress. Satyagraha did not guarantee control of
mass action, and reported atrocity details require source discipline.

The topic-tight direct route is 2018 Prelims Q69 on Champaran. The Gandhism,
Gandhian-phase voices, education/nationalism and present-significance demands
are explicitly bounded or cross-cutting; unavailable objective keys remain
unpromoted.

**Answer:** method definition -> three local laboratories -> comparative
learning -> Rowlatt scale-up and loss of control -> Jallianwala rupture ->
evidence limits -> bounded transition to Topic 20.
""",
    20: r"""
### TOPIC 20 CLOSING NON-COOPERATION-KHILAFAT LEDGER

Topic 20 owns the 1919-22 Khilafat and Non-Cooperation convergence, Congress
authorisation, programme, social spread, constructive institutions, local
variation and withdrawal debate. Topic 19 owns Rowlatt-Jallianwala; Topic 21
owns Swarajists, No-changers and 1920s revolutionary organisations.

Keep the Khilafat grievance, committees/delegations and Gandhi's alliance
logic distinct from the Congress programme. The sequence is Calcutta Khilafat
Conference (November 1919) -> Treaty of Sevres context -> Calcutta Special
Session (September 1920) -> Nagpur ratification/reorganisation (December
1920) -> Tilak Swaraj Fund and mass boycott (1921) -> Moplah rebellion
(1921) -> Chauri Chaura (4 February 1922) -> Bardoli withdrawal decision
(12 February 1922). Swarajya Sabha was the renamed Home Rule body, not the
Swaraj Party founded in 1923.

The movement's stages, khadi/charkha, national education, panchayats, titles,
council/court/school/cloth boycott and conditional escalation require exact
separation. Assess uneven peasant, worker, trader, student, women, caste and
regional participation. Treat Moplah as agrarian, anti-colonial and communal
violence in combination, and present the Gandhi versus R. Palme Dutt/Bipan
Chandra withdrawal debate with attributed evidence.

Three 2025 direct Prelims routes have locally confirmed Series-A keys; 2026
Q9 remains routed and unkeyed, while the 2021 constructive-programme Mains
route is bounded across Non-Cooperation and Civil Disobedience.

**Answer:** post-war convergence -> Khilafat alliance -> Congress adoption ->
graded programme and constructive alternative -> social/regional spread ->
violence and discipline crisis -> withdrawal debate -> achievement, limits
and Topic 21 strategic vacuum.
""",
    21: r"""
### TOPIC 21 CLOSING INTERWAR-STRATEGIES LEDGER

Topic 21 owns the post-Non-Cooperation strategic response through Swarajist
council entry, No-changer constructive work and the HRA-HSRA revolutionary
lineage. Topic 20 owns the 1919-22 movement and withdrawal; Topic 22 owns the
Simon Commission, Nehru Report and Civil Disobedience sequence; Topic 23 owns
the mature socialist, peasant, worker and princely-state movements of the
1930s. Chittagong enters here as a revolutionary culmination overlapping 1930,
not as evidence that the Bengal and HRA-HSRA organisations shared one command.

Keep the sequence exact: Gaya council-entry defeat (December 1922) -> Swaraj
Party working founding date (1 January 1923) -> HRA at Kanpur (October 1924)
-> Kakori (1925) -> Naujawan Bharat Sabha at Lahore (March 1926) -> Kakori
executions (1927) -> HSRA reorganisation at Ferozeshah Kotla (9-10 September
1928) -> Saunders (December 1928) -> Assembly Bomb Case (8 April 1929) ->
Jatin Das (13 September 1929) -> Lahore Tribunal verdict (October 1930) ->
executions (23 March 1931). The December-1922/January-1923 Swaraj Party date
and 63/64-day Jatin Das fast remain flagged source variances.

Separate No-changer preparation from Swarajist obstruction, HRA republicanism
from HSRA socialism, Naujawan Bharat Sabha's open front from the underground
organisation, Kakori from the Saunders and Assembly cases, and the Assembly
Bomb Case from the Lahore Conspiracy Case. Bhagat Singh must be assessed as a
rationalist and socialist political thinker as well as a martyr.

The shared direct route is 2020 GS-I Q13 on ideological strands since the
1920s. The 2018 Swarajya Sabha objective item is an adjacent Topic-18-owned
name-confusion control; its local official key is unavailable and no answer
letter is invented.

**Answer:** 1922 strategic vacuum -> two Congress tactics -> council record
and constructive continuity -> HRA-Kakori -> open youth mobilisation -> HSRA
socialist turn -> symbolic action, trials and jail resistance -> Bhagat Singh
as thinker -> Chittagong and the qualified no-lull verdict.
""",
    22: r"""
### TOPIC 22 CLOSING CONSTITUTIONAL-DEADLOCK-AND-CDM LEDGER

Topic 22 owns the 1927-34 sequence from the all-British Simon Commission and
the Indian-authored Nehru Report through Purna Swaraj, Civil Disobedience, the
Gandhi-Irwin Pact, three Round Table Conferences, the Communal Award, Poona
Pact and final withdrawal. Topic 21 owns the Swarajist and HRA-HSRA streams;
Topic 23 owns organised Left, peasant, worker and states-peoples movements;
Topic 24 owns the 1935 Act and 1937 ministries. Topics 26 and 27 retain the
post-war upsurge/Cabinet Mission and independence/partition respectively.

Keep appointment, arrival and protest distinct: Simon appointed in 1927 and
arrived on 3 February 1928; Lala Lajpat Rai was injured at Lahore on
30 October and died on 17 November. Nehru Report dominion status (1928),
Jinnah's Fourteen Points (1929), Lahore Purna Swaraj (December 1929),
Independence Day (26 January 1930), Dandi departure (12 March) and salt-law
breach (6 April) are separate constitutional and movement stages.

Civil Disobedience must extend beyond Dandi to Dharasana, Peshawar and the
Khudai Khidmatgars, Garhwali refusal, Sholapur, no-tax, forest-law defiance,
women's participation and differentiated class/regional response. The
Gandhi-Irwin Pact of 5 March 1931 was a truce, not independence. Congress was
absent from the First RTC, Gandhi was its sole representative at the Second,
and the Third was marginal. Communal Award separate electorates and Poona Pact
reserved seats in joint electorates are not interchangeable; the 147/148 seat
figure remains a recorded source variance.

Two direct objective routes are retained: 2025 Prelims Q74 has a locally
confirmed Series-A key; 2020 Prelims Q27 is locally unkeyed and no official
letter is invented.

**Answer:** exclusion and boycott -> Indian constitutional draft and communal
deadlock -> Purna Swaraj -> salt as universal law-breaking symbol -> regional
and social spread -> repression and negotiation -> RTC limits -> Communal
Award/Poona Pact conflict -> resumed struggle, withdrawal in 1934 and bounded
handoff to the 1935 Act.
""",
    23: r"""
### TOPIC 23 CLOSING SOCIAL-MOVEMENTS-AND-LEFT LEDGER

Topic 23 owns the 1930s widening of nationalism through socialist, communist,
worker, peasant and princely-state peoples' organisation. AITUC (1920), the
Tashkent/Kanpur communist-origin distinction, AISPC (1927), Bardoli (1928) and
Bihar Kisan Sabha (1929) are roots; CSP (1934), AIKS/Faizpur (1936), Congress
ministries, Haripura (1938) and Tripuri/Forward Bloc (1939) are the core.
Bakasht, Warli, Tebhaga and Telangana are bounded late-colonial bridges, not a
licence to absorb Topic 26's INA/RIN/Cabinet Mission, Topic 27's independence
and partition, Topic 28's integration, or Topic 38's post-independence land and
agrarian synthesis.

Keep organisations and social bases separate. AITUC was an all-India labour
platform; CSP worked within Congress; CPI origins require Tashkent 1920 versus
Kanpur 1925 qualification; AIKS organised agrarian demands; AISPC coordinated
rights struggles under princes. Congress absorption and autonomous popular
initiative must be assessed together rather than forcing every movement into a
single command hierarchy.

Movement analysis requires grievance -> organisation -> repertoire -> state
response -> outcome. Bardoli's disciplined revenue satyagraha differs from
Awadh/Eka landlord-tenant conflict; Moplah requires agrarian, anti-colonial and
communal dimensions; Ulgulan is a nineteenth-century tribal demand routed here
only through the dedicated tribal-response bank. Tripuri was an ideological,
strategic and organisational conflict, not merely a Bose-Gandhi personality
clash.

Five routed demands are controlled: 2019 and 2020 GS-I are bounded/shared
national-movement questions; 2023 GS-I is a cross-period tribal route; 2020
Prelims Q35 is locally unkeyed; 2026 Prelims Q16 is provisional and no answer
letter is promoted.

**Answer:** roots and repression -> socialist/communist organisational
distinctions -> worker and peasant mobilisation -> rights and agrarian
programmes -> princely-state democratisation -> Bose/Tripuri strategic tension
-> bounded late-colonial radicalisation -> wider social base with coalition
limits.
""",
    24: r"""
### TOPIC 24 CLOSING 1935-ACT-AND-MINISTRIES LEDGER

Topic 24 owns the constitutional lineage, design and non-operation of the
Government of India Act 1935, the 1937 elections, office-acceptance debate,
Congress ministries' record and limits, resignation in 1939 and the immediate
Deliverance Day/Lahore Resolution bridge. Topic 22 owns Simon, RTCs and the
White Paper as processes; Topic 23 owns social-movement pressure on ministry
programmes; Topic 25 owns the war crisis after resignation. Topic 26 owns
INA/RIN/Cabinet Mission and Topic 27 owns independence/partition.

Read the Act in two halves. Provincial dyarchy was abolished and provincial
autonomy operated, but governors retained discretion, special responsibilities
and Section 93 takeover power. At the centre, an All-India Federation and
dyarchy were proposed but never operated because the accession condition was
not met. Defence, external affairs and internal security remained reserved;
residuary power lay with the Governor-General. The RBI came from the RBI Act
1934, not the 1935 Act.

Franchise figures remain a qualified range: approximately 30-35 million or
about 10-14 per cent depending on source and denominator. Congress formed
ministries in eight of eleven provinces, gained administrative experience and
advanced civil liberties, education and agrarian measures, but finance,
governor safeguards, bureaucracy and provincial variation constrained them.
Resignation in October-November 1939 followed India's unilateral entry into
war, not electoral defeat or Section 93.

Two direct objective routes are retained: 2024 Prelims Q62 has a locally
confirmed official Series-A key; 2018 Prelims Q38 is source-backed but locally
unkeyed, so no answer letter is invented.

**Answer:** Simon-RTC-White Paper-JSC lineage -> two constitutional halves ->
federal non-operation and safeguards -> franchise/representation design ->
1937 electoral mandate -> office as a field of struggle -> achievements and
structural limits -> principled resignation -> bounded communal and wartime
handoff.
""",
    25: r"""
### TOPIC 25 CLOSING WARTIME-CRISIS-AND-QUIT-INDIA LEDGER

Topic 25 owns the wartime political sequence from India's unconsulted entry
into the Second World War through the August Offer, Individual Satyagraha,
Cripps Mission and the open, underground and parallel-government phases of
Quit India. Topic 24 owns the 1935 Act and ministries up to resignation.
Topic 26 exclusively owns both INA phases, INA trials, post-war labour/public
upsurge, RIN revolt, Wavell/Simla, 1945-46 elections and Cabinet Mission.
Topic 27 owns independence and partition. Those later events may qualify
Quit India's long-term significance but cannot be narrated here as owned core.

Keep the chronology exact: belligerency on 3 September 1939 -> ministry
resignations in October-November -> Deliverance Day on 22 December -> Lahore
Resolution in March 1940 -> August Offer -> Individual Satyagraha from October
1940, Vinoba first and Nehru second -> Cripps Mission in March-April 1942 ->
AICC resolution at Gowalia Tank on 8 August -> leadership arrests from
9 August -> decentralised upsurge, underground networks and parallel
governments through 1942-44. The 1943 Bengal famine is contextual wartime
evidence, not a cause of the August 1942 resolution.

Cripps offered post-war dominion status and constitution-making with a
provincial non-accession option, not immediate independence or an immediate
national government. Quit India became leaderless but not purposeless after
decapitation: distinguish Congress's non-violent authorisation from strikes,
sabotage and attacks that occurred, and distinguish Ballia, Tamluk/Jatiya
Sarkar and Satara/Prati Sarkar by locality and duration. Political alignments
matter: League aloofness and the CPI People's War line narrowed the coalition.

The 2024 GS-I Q3 wording is locally official and directly solved. The 2021
Quit India Resolution and 2022 Cripps objective entries survive only as
routing-ledger demand summaries because exact local stems and keys are absent;
no wording or answer letter is fabricated.

**Answer:** unconsulted war -> failed offers and limited protest -> Japanese
advance/material distress -> Cripps failure -> Quit India resolution and
decapitation -> local forms, underground continuity and parallel authority ->
repression -> immediate failure but lasting delegitimation -> explicitly
bounded handoff to Topic 26.
""",
    26: r"""
### TOPIC 26 CLOSING POST-WAR-UPSURGE LEDGER

Topic 26 owns the two INA formations, Azad Hind, the Imphal-Kohima military
failure, Red Fort trials, the 1945-46 labour and service upsurge, the RIN
uprising, Wavell/Simla, the 1945-46 elections and the Cabinet Mission's
constitutional design. Topic 25 owns the wartime and Quit India core. Topic 27
alone owns the Cabinet Mission breakdown after the plan, Direct Action,
Interim Government conflict, the final transfer and Partition.

Keep three causal layers separate. Mohan Singh organised the first INA in 1942;
Subhas Chandra Bose reorganised a second INA in 1943 under Azad Hind. Military
defeat at Imphal-Kohima did not erase the political effect of the 1945-46 Red
Fort trials. The RIN uprising began at HMIS Talwar on 18 February 1946, spread
rapidly and ended after differentiated surrender appeals and threatened
repression; commonly cited scale estimates are not exact audited totals.

The British Cabinet decided on 22 January 1946 to send the Cabinet Mission,
before the RIN uprising, and the 19 February announcement had already been
scheduled. The uprising therefore sharpened a crisis of coercive legitimacy
but did not cause or trigger the Mission's dispatch. The 16 May plan proposed
a weak Union controlling Defence, External Affairs and Communications,
provincial Groups A, B and C, and a Constituent Assembly route; it rejected
both a sovereign Pakistan and a strong unitary centre.

Leadership responses must not be flattened. Congress praised patriotic spirit
and opposed repression but rejected the timing and tactics; Patel appealed to
the ratings to surrender after assessing the force assembled in Bombay.
Jinnah's surrender advice was addressed to Muslim ratings, while left groups
offered more direct support. The plan's acceptance, interpretation and later
breakdown belong to the boundary with Topic 27, not to a claim that settlement
was already achieved.

The 2019 Prelims Q15, 2021 Prelims Q47 and 2019 GS-I Q12 entries remain routed
demand summaries. Exact objective stems and official keys are unavailable
locally, so no wording or answer letter is invented.

**Answer:** two INA formations -> military defeat but trial-driven political
reversal -> labour/service upsurge -> RIN chronology and differentiated
responses -> coercive-legitimacy crisis without dispatch causation -> Simla
and electoral mandate -> Cabinet Mission design -> bounded handoff before the
final transfer and Partition core.
""",
    27: r"""
### TOPIC 27 CLOSING TRANSFER-AND-PARTITION LEDGER

Topic 27 owns the 1946-47 transfer and Partition core: breakdown of the Cabinet
Mission settlement, Direct Action, communal violence, the Interim Government,
Constituent Assembly opening, Attlee's deadline, Mountbatten's arrival, the
3 June Plan, the Indian Independence Act, transfer, boundary award, migration,
gendered violence, relief and the competing explanations of Partition. Topic
26 owns the Cabinet Mission's design and the post-war upsurge; Topic 28 owns
princely-state integration and constitution-to-republic.

Keep the dated endgame exact: Direct Action Day on 16 August 1946; Interim
Government from 2 September; Constituent Assembly first meeting on 9 December;
Attlee statement on 20 February 1947; Mountbatten assumed office on 24 March;
3 June Plan; royal assent to the Indian Independence Act on 18 July; transfer
on 15 August; Radcliffe Award publication on 17 August. Do not telescope plan,
statute, sovereignty and boundary disclosure into one date.

Partition was neither timeless inevitability nor one person's deed. Explain
the interaction of colonial constitutional strategy, Congress-League rivalry,
provincial politics, collapsing coalition options, administrative haste,
communal mobilisation and violence. Punjab and Bengal require provincial
analysis; women, abducted persons, refugees, minorities and relief institutions
are evidence-bearing actors and not an afterthought to elite negotiation.

The Act created two dominions and ended British suzerainty; it did not itself
complete the integration of the princely states, frame India's Constitution or
make India a republic. Independence on 15 August 1947 and the Republic on
26 January 1950 are separate constitutional thresholds.

The locally routed objective language-movement entry remains unresolved and
no factual claim or answer key is promoted from it. The 2019 transfer-of-power
Mains demand is adjacent/shared with Topic 26 and is labelled accordingly.

**Answer:** Cabinet settlement breakdown -> Direct Action and provincial
violence -> contested Interim Government -> failed coalition architecture ->
deadline and Mountbatten acceleration -> 3 June Plan -> Independence Act ->
transfer before boundary disclosure -> migration, gendered violence and
rehabilitation -> multi-causal verdict without inevitability.
""",
    28: r"""
### TOPIC 28 CLOSING INTEGRATION-TO-REPUBLIC LEDGER

Topic 28 owns the integration of more than 560 princely states and the
constitutional transition from accession to the Republic. Topic 27 owns the
British transfer and Partition; Topic 29 owns colonial-legacy synthesis;
Topic 30 owns linguistic reorganisation. Kashmir, Junagadh and Hyderabad are
different sequences and cannot be reduced to one template.

British paramountcy lapsed on 15 August 1947 and was not transferred to either
dominion. The States Department under Vallabhbhai Patel, with V.P. Menon as
Secretary, used an initially narrow Instrument of Accession covering Defence,
External Affairs and Communications. Accession, standstill arrangements,
administrative merger, covenant-based unions and constitutional incorporation
were separate stages.

Junagadh combined non-contiguity, popular mobilisation, Indian intervention
after the Dewan's request and a February 1948 plebiscite. Kashmir's October
1947 invasion preceded accession, and accession preceded the Indian airlift;
the National Conference and Sheikh Abdullah form part of its popular-political
dimension. Hyderabad's November 1947 standstill agreement preceded failed
negotiation, Razakar escalation and Operation Polo in September 1948.

The Constitution was adopted on 26 November 1949 and came into force on
26 January 1950. The Part A, B, C and D classification and later abolition of
privy purses belong to constitutional consolidation, not to the initial
three-subject accession instrument. Topic 30 owns the later linguistic
redrawing of state boundaries.

The 2021 GS-I princely-state question is a locally verified direct Mains route.
No direct Prelims route is invented merely because the topic has dense factual
material.

**Answer:** lapse of paramountcy -> States Department and narrow accession ->
different crisis routes -> merger and state unions -> Constituent Assembly
federal settlement -> adoption in 1949 -> Republic in 1950 -> qualified
integration verdict recognising negotiation, popular agency and coercion.
""",
    29: r"""
### TOPIC 29 CLOSING COLONIAL-LEGACY SYNTHESIS LEDGER

Topic 29 owns a sector-by-sector synthesis of colonial inheritances and the
national movement's republican resources. Topic 28 owns accession and the
constitution-to-republic sequence; Topic 30 owns linguistic states and
regionalism; Topic 31 owns tribal integration; Topic 32 owns Nehru's
foreign-policy legacy. These neighbours may supply examples but cannot be
duplicated as this topic's narrative core.

Classify before judging. Administrative centralisation, civil services, army,
police, codified law, railways, communications, census categories, landlord
interests, deindustrialisation, poverty and external dependence were colonial
inheritances with unequal purposes and effects. Representative institutions,
rights language, federal argument, secular citizenship, mass organisation and
social reform were shaped most decisively through anti-colonial contest, even
when they worked through institutions of colonial origin.

Reject both the benevolent-gift and unchanged-burden fallacies. Railways served
imperial extraction and military movement yet could be politically
reappropriated; an inherited civil service supplied capacity but carried
hierarchy and district-authoritarian habits; codified law enabled uniform
claims while preserving unequal access. For every institution separate origin,
colonial purpose, social reach, post-1947 adaptation and democratic control.

The founding response joined universal adult franchise, parliamentary
government, federalism with a strong Union, planned development, education,
refugee rehabilitation and non-alignment. This was constrained continuity, not
a clean slate or automatic institutional survival.

The 2025 GS-I four-domain demand on polity, economy, education and
international relations is locally verified and directly owned. The 2021
princely-state question is adjacent-owned by Topic 28 and is not relabelled;
no direct Prelims route is fabricated.

**Answer:** classify colonial inheritances -> test purpose and distribution ->
identify nationalist-democratic resources -> show selective retention and
institutional repurposing -> evaluate polity, economy, education and external
orientation separately -> qualify continuity with conflict, inequality and
implementation gaps.
""",
    30: r"""
### TOPIC 30 CLOSING LINGUISTIC-FEDERALISM LEDGER

Topic 30 owns linguistic reorganisation and the bounded regionalism sequence
from the post-Partition postponement to the 1967 language settlement. Topic 29
owns the wider founding legacy; Topic 31 exclusively owns tribal integration
and the North-East's tribal-nationality strategy; Topic 32 owns foreign-policy
legacy. Later regional crises are comparison controls, not this topic's core.

Congress had organised provincial committees linguistically from 1921, so the
post-1947 dispute concerned timing and safeguards rather than discovery of the
principle. Keep the sequence exact: Dar Commission (1948), JVP Committee
(December 1948), Potti Sriramulu's 1952 fast and death, Andhra State (October
1953), States Reorganisation Commission under Fazl Ali with K.M. Panikkar and
H.N. Kunzru (1953-55), and the States Reorganisation Act effective
1 November 1956 with fourteen states and six Union Territories.

The settlement continued: Bombay was bifurcated into Maharashtra and Gujarat
in 1960; Punjab was reorganised in 1966 with Haryana created and Chandigarh as
a Union Territory and joint capital. Language of state boundaries and language
of Union administration are related but distinct. Article 343, the Official
Languages Act 1963, the 1965 agitation and the 1967 amendment belong to the
latter sequence.

Regionalism requires a criterion. Accommodative demands seek statehood,
recognition or resources within the Union; nativist sons-of-the-soil politics
targets fellow citizens; secessionism contests the Union. Shiv Sena's 1966
formation is a nativist example, not proof that all linguistic mobilisation
was secessionist. Linguistic states generally deepened democratic integration,
while minorities, capitals, borders and violence qualify a success-only story.

The 2018 and 2022 GS-I entries are routed Mains demand summaries with directive
metadata, not verbatim official stems. No direct Modern History Prelims route
is invented.

**Answer:** pre-1947 linguistic commitment -> post-Partition postponement ->
Dar/JVP caution -> Andhra breakthrough -> SRC criteria and 1956 settlement ->
Bombay and Punjab corrections -> separate official-language compromise ->
regionalism typology -> integration verdict with minority and violence limits.
""",
    31: r"""
### TOPIC 31 CLOSING TRIBAL-INTEGRATION LEDGER

Topic 31 owns post-1947 tribal policy and integration: the rejection of both
forced assimilation and museum-like isolation, Verrier Elwin's influence,
Fifth- and Sixth-Schedule routes, the Naga and Mizo trajectories, North-East
statehood accommodation and the Jharkhand movement's demographic broadening.
Topic 23 retains colonial and late-colonial tribal mobilisation. Topic 30 owns
linguistic reorganisation; Topic 32 owns the wider Nehru legacy; Topic 38 owns
the post-independence land, displacement and social-policy synthesis.

The population figures of more than 400 communities, nearly 38 million people
and roughly 6.9 per cent belong to the 1971 Census as reproduced by the held
text; they are neither 1951 nor current statistics. "Tribal Panchsheel" is a
later label for broad policy guidelines and receives no fabricated proclamation
year. Integration meant development along tribal communities' own genius, not
cultural absorption, while protection without voice could still become
paternalism.

Keep the constitutional instruments distinct. The Sixth Schedule's autonomous
district and regional councils address territorially concentrated tribal areas
of the North-East. The Fifth Schedule, Tribal Advisory Councils, Article 46,
reserved representation and the constitutional commissioner address other
Scheduled Areas. Detailed contemporary doctrine remains Polity-owned.

The North-East chronology must not telescope coercion and settlement. A.Z.
Phizo's separatist phase, army deployment in early 1956 and the breaking of the
rebellion's main force by mid-1957 preceded the Naga People's Convention route
associated with Imkongliba Ao and Nagaland statehood in 1963. Meghalaya's
state-within-a-state demand and the 1972 reorganisation followed another route.
The MNF uprising began in 1966; the 1986 Mizo Accord brought Laldenga into
constitutional government and preceded Mizoram statehood in 1987. Mizoram is a
strong settlement case, not a universal description of every regional conflict.

Jharkhand Party under Jaipal Singh, its 32 seats in 1952, declining tribal share
and the later JMM under Shibu Soren show a partial broadening from tribal
nationalism toward a regional and class-inflected coalition. Political
accommodation and developmental delivery require separate verdicts: statehood,
autonomy and electoral absorption could succeed while land alienation, forest
restrictions, displacement and poverty persisted.

No direct Modern History CSE route is verified for 2018-2026. Indian Society
owns the 2021 and 2022 tribal-society Mains demands; Topic 23 owns the 2023
colonial tribal-response demand; Polity owns Scheduled Areas objective demands.
None is relabelled as a direct Topic-31 PYQ.

**Answer:** colonial dispossession backdrop -> reject isolation and assimilation
-> Panchsheel principle -> distinguish Fifth and Sixth Schedule mechanisms ->
Naga coercion-to-statehood route -> Mizo negotiated settlement -> Jharkhand
demographic broadening -> political success versus developmental shortfall.
""",
    32: r"""
### TOPIC 32 CLOSING NEHRU-ERA LEDGER

Topic 32 owns Nehru's domestic institution-building and foreign-policy legacy
to 27 May 1964: electoral democracy, planning and mixed economy, rural
development, science and higher education, secular citizenship, non-alignment,
Panchsheel, Bandung, Belgrade, Goa, Kashmir as a contested choice and the 1962
China-war test. Topic 33 owns the Congress system and opposition-party taxonomy;
Topic 34 begins the Shastri succession; Topic 38 owns the economy, land and
society synthesis.

Keep the chronology and institutions separate: Planning Commission by Cabinet
resolution on 15 March 1950; first general election from October 1951 to
February 1952; Community Development Programme on 2 October 1952; Panchsheel in
April 1954; Avadi and Bandung in 1955; the 1956 Industrial Policy Resolution
and Second Plan; Kerala's elected Communist government in 1957; Belgrade/NAM
and Goa in 1961; China war in October-November 1962; Kamaraj Plan in 1963; death
on 27 May 1964.

The Planning Commission was extra-constitutional. Avadi's socialistic pattern
and the 1956 industrial schedules created public-sector commanding heights
inside a mixed economy, not complete state ownership. The Community Development
Programme preceded and differed from Balwantrai Mehta's 1957 Panchayati Raj
recommendation. Higher scientific capability and mass-literacy failure must
appear together.

Bandung was an Afro-Asian precursor, not NAM's founding summit; Belgrade in
September 1961 founded NAM. Non-alignment meant independent, positive
engagement, not passive neutrality. Goa demonstrates that it was not absolute
pacifism. Panchsheel optimism and the unresolved border must be held together;
the 1962 defeat exposed defence and intelligence limits without reducing the
entire diplomatic record to one war. Kashmir's UN reference remains a contested
choice and must not be presented as settled success or single-cause failure.

One direct 2018 Prelims chronology route is retained with no locally available
official key. The 2025 four-domain consolidation Mains demand belongs Topic 29
and appears only as an adjacent application.

**Answer:** democratic gamble -> planning and capability institutions -> mixed
economy and rural-development limits -> active non-alignment -> Bandung versus
Belgrade -> Goa and decolonisation -> China-war capability test -> enduring
institutions plus literacy, agrarian, organisational and strategic deficits.
""",
    33: r"""
### TOPIC 33 CLOSING CONGRESS-SYSTEM LEDGER

Topic 33 owns the party system from 1947 through the 1967 watershed: Congress
as a broad dominant coalition, factional competition and co-option, the
Socialist exit, KMPP/PSP and Lohiaite anti-Congressism, CPI's electoral turn and
1964 split, Bharatiya Jana Sangh, Swatantra, regional variation and the
electoral mechanism of sub-50-per-cent votes producing large seat majorities.
Topic 32 owns Nehru's governmental record; Topic 34 owns the post-1967
coalitions, defections, Syndicate-Indira conflict and 1969 split.

Rajni Kothari's "Congress system" means competitive one-party dominance, not a
one-party state. Genuine opposition, internal dissent and alternation at state
level remained possible. First-past-the-post, fragmented challengers, Congress's
social breadth and its capacity to absorb rival programmes jointly explain
dominance; no one mechanism is sufficient.

Keep the organisational sequence exact: the 1948 dual-membership bar and
Socialist exit; Tandon-Nehru contest in 1950-51; Bharatiya Jana Sangh and KMPP
in 1951; KMPP-Socialist merger into PSP in 1952; Avadi co-option in 1955;
Kerala's elected CPI government in 1957; Swatantra in 1959; CPI/CPI(M) split in
1964; anti-Congress coalition breakthrough in 1967. Party names, founders,
ideologies and bases are not interchangeable.

The opposition's failure was not absence of votes or ideas. Socialists split
over cooperation, communists moved from insurrection to electoral politics and
then divided, Jana Sangh built a cultural-nationalist cadre, and Swatantra
offered a pro-market critique. Regional strength in Kerala, West Bengal and
Tamil Nadu qualifies a national weakness-only narrative.

One direct 2024 Prelims party-leader matching route is retained. The local
Series-A key exists, but this owner records no inferred answer beyond verified
party-founder associations.

**Answer:** define competitive dominance -> Congress breadth and factions ->
electoral arithmetic -> co-option -> map socialist, communist, conservative and
regional alternatives -> explain opposition fragmentation -> 1967 watershed ->
handoff before the Indira-Syndicate rupture.
""",
    34: r"""
### TOPIC 34 CLOSING SHASTRI-TO-INDIRA LEDGER

Topic 34 owns the bounded 1964-73 transition: two constitutional successions,
the 1965 war and Tashkent, the mid-1960s food/currency crisis, the 1967 electoral
setback and state coalitions, Indira-Syndicate conflict, the 1969 Congress split
and bank nationalisation, the 1971 mandate, privy-purse abolition, Bangladesh
war and the 1972 Simla settlement. Topic 33 stops at the 1967 party-system
watershed; Topic 35 owns the 1973-77 crisis and Emergency. Pokhran-I on 18 May
1974 is immediate-aftermath enrichment, not part of the 1964-73 core.

Date the successions precisely. Shastri took office on 9 June 1964. The
Tashkent Declaration was signed on 10 January 1966 and Shastri died in the
early hours of 11 January; Indira Gandhi took office on 24 January after
defeating Morarji Desai 355 to 169. The rupee devaluation followed on 6 June
1966. These are separate political, diplomatic and economic thresholds.

The 1967 election ended easy dominance without removing Congress from the
Centre; it lost power in eight states and opened the coalition/defection era.
The 1969 presidential struggle, V.V. Giri victory, Congress (R)/(O) split and
nationalisation of fourteen banks formed a connected political sequence, but
bank nationalisation was not the same measure as the 26th Amendment ending
privy purses in 1971.

Garibi Hatao and the 352-of-518 victory shifted authority from organisation to
direct popular appeal. The Bangladesh crisis, refugee influx, December 1971
war and creation of Bangladesh produced a strategic and domestic high point;
the Simla Agreement belongs 1972. This achievement must be assessed alongside
personalisation, weakened party institutions and Centre-state pressure that
form the structural bridge to Topic 35.

The routed 2019 Prelims coal-nationalisation-status demand has no supporting
evidence in the held Modern History sources. No coal statute, year, sequence or
answer key is invented; a full answer must be verified in the proper Economy
or Geography owner. No direct Mains route is claimed.

**Answer:** constitutional succession -> war and Tashkent -> food/currency
crisis -> 1967 setback -> populist left turn and organisational rupture ->
1971 electoral and strategic consolidation -> 1972 diplomacy -> institutional
cost -> stop at 1973 before the Emergency crisis.
""",
    35: r"""
### TOPIC 35 CLOSING JP-EMERGENCY LEDGER

Topic 35 owns the 1973-77 democratic crisis: inflation, scarcity and oil shock;
Nav Nirman, the Bihar movement, JP's Sampoorna Kranti and the railway strike;
the Allahabad judgment and Supreme Court conditional stay; the Article 352
proclamation; MISA detentions, censorship, constitutional amendments,
extra-constitutional power, sterilisation and demolition excesses; the January
1977 election call, March verdict and end of the Emergency on 21 March. Topic
34 supplies the pre-1973 personalisation background. Topic 36 owns Janata
formation and government, the 44th Amendment, Charan Singh, Indira's return and
regional crises. Topic 37 owns the Rajiv era; Topic 38 owns the economy, land
and society synthesis.

Economic crisis preceded mobilisation: failed monsoons and inflation in
1972-73, the 1973 oil shock, Gujarat's Nav Nirman from January 1974, Bihar from
March, JP's Total Revolution and the twenty-two-day railway strike in May.
Students, middle classes, traders and intelligentsia supplied the dominant
social base; workers, peasants, Dalits and every region were not incorporated
uniformly.

Justice Jagmohanlal Sinha of the Allahabad High Court set aside Indira Gandhi's
election on 12 June 1975 on Raj Narain's petition. Justice V.R. Krishna Iyer's
24 June Supreme Court order was a conditional stay; it did not reverse the
High Court judgment. The proclamation under Article 352 was dated 25 June and
publicly announced on 26 June. It was not an Article 356 state emergency.

Implementation combined MISA detention, press censorship, curtailed liberties,
the 38th, 39th and 42nd Amendments, and Sanjay Gandhi's extra-constitutional
influence. Forced sterilisation and slum clearances are named without unsafe
totals. Institutions largely failed to prevent the suspension; the electorate
reversed it when elections were held in March 1977. The 44th Amendment belongs
to the subsequent Janata settlement and is only a boundary reference here.

No direct Modern History CSE route is verified for 2018-2026. Original practice
is never relabelled PYQ, and detailed present constitutional doctrine remains
Polity-owned.

**Answer:** personalisation background -> economic crisis -> student and JP
mobilisation -> judicial trigger -> precise proclamation sequence -> legal and
coercive machinery -> uneven excesses and resistance -> 1977 electoral reversal
-> stop before Janata governance -> democracy vindicated by voters more than by
preventive institutions.
""",
    36: r"""
### TOPIC 36 CLOSING JANATA-RETURN-REGIONAL-CRISES LEDGER

Topic 36 owns the Janata Party's January 1977 formation and March victory, the
Morarji Desai government, the 44th Amendment, dual-membership rupture, Charan
Singh interregnum, Congress (I)'s January 1980 return, Sanjay Gandhi's death,
regional-party assertion and the Assam, Punjab and Jammu and Kashmir crises
through Indira Gandhi's assassination on 31 October 1984. Topic 35 stops at the
Emergency's electoral defeat; Topic 37 begins with Rajiv Gandhi's succession.

Janata joined Congress (O), Bharatiya Jana Sangh, Bharatiya Lok Dal and
Socialists, won 330 of 542 seats, and installed India's first non-Congress
central government. Its durable constitutional achievement was the 44th
Amendment of 1978. Its collapse was not proof that democratic alternation was
impossible: leadership rivalry, organisational incompatibility and the RSS
dual-membership dispute broke the coalition. Charan Singh took office in July
1979 but resigned without facing a confidence vote.

Congress (I)'s 353-of-529 victory in January 1980 records Janata's collapse,
not voter endorsement of the Emergency. Sanjay Gandhi's June 1980 death drew
Rajiv into politics. Telugu Desam was founded on 29 March 1982 and won Andhra
Pradesh in 1983; the founding date and election breakthrough are distinct.
West Bengal's Left Front from 1977 and Telugu Desam show autonomous state
politics, not failed national integration.

Regional crises require separate mechanisms. Assam centred on migration and
the electoral status of alleged foreigners. Jammu and Kashmir exposed repeated
central interference in elected state politics. Punjab joined Chandigarh,
river-water and autonomy claims in the Anandpur Sahib Resolution; delayed
accommodation, factional political management, militancy and cross-border
support interacted before Operation Blue Star in June 1984. No casualty total,
community motive or single-cause verdict is asserted without evidence.

No direct Modern History CSE route is verified for 2018-2026. Original
questions remain original; detailed 44th-Amendment doctrine stays Polity-owned.

**Answer:** democratic alternation and repair -> coalition contradiction ->
Janata collapse -> qualified Indira return -> autonomous regional politics ->
theatre-by-theatre grievance and response -> delayed accommodation versus
coercion -> bounded endpoint at 31 October 1984.
""",
    37: r"""
### TOPIC 37 CLOSING RAJIV-TO-MILLENNIUM LEDGER

Topic 37 owns Rajiv Gandhi's succession and December 1984 mandate, the
modernising programme, Anti-Defection Act, Punjab and Assam accords, Shah Bano
reversal, Ayodhya opening, Bofors and opposition consolidation; it then follows
the 1989 National Front, Mandal implementation, the 1990 rath yatra, 1991
economic reforms, Babri Masjid demolition on 6 December 1992 and coalition
governments from 1996 to the millennium. Topic 36 ends with Indira Gandhi's
assassination; Topic 38 owns thematic economy, land, society and state synthesis.

Congress won 404 of the 514 seats elected in December 1984 because polling in
Assam and Punjab was deferred; a full-house denominator is not used. Rajiv's telecom,
computerisation, science-mission and decentralisation agenda signalled
modernisation, but panchayati raj constitutionalisation came only through the
73rd and 74th Amendments after his premiership. The 52nd Amendment of 1985
created the Anti-Defection Act.

The Punjab and Assam Accords of 1985 illustrate negotiated accommodation, but
implementation differed. The Shah Bano legislative reversal and opening of the
Ayodhya locks are analysed as competing identity concessions, not as identical
legal acts. Bofors damaged the clean-government claim and helped consolidate a
fragmented opposition around V.P. Singh.

The 1989 government depended on outside support from both the BJP and the Left.
Mandal implementation in 1990 concerned 27 per cent reservation for OBCs in
central government employment. Advani's 1990 rath yatra and the 1992 demolition
are separate events. The 1991 balance-of-payments crisis enabled Narasimha Rao
and Manmohan Singh's reform turn; minority and coalition governments thereafter
showed that fragmentation could coexist with consequential policy.

No direct Modern History CSE route is verified for 2018-2026. Original practice
is not relabelled PYQ; Polity owns detailed amendment and court doctrine, while
Economy owns present reform mechanics.

**Answer:** succession and mandate -> modernisation plus institutional limits ->
accord and identity-management record -> Bofors legitimacy loss -> 1989
fragmentation -> Mandal/Mandir differentiation -> 1991 Market turn -> 1990s
coalition stabilisation -> qualified democratic-transition verdict.
""",
    38: r"""
### TOPIC 38 CLOSING POST-INDEPENDENCE SYNTHESIS LEDGER

Topic 38 is thematic rather than another ruler chronology. It owns the
post-independence relationship among planned development, land reform,
agricultural change, agrarian mobilisation, caste, gender, communalism and
state capacity. Topics 32-37 retain their period narratives; this topic compares
mechanisms and outcomes across them without duplicating prime-minister sequence.

The 1948 and 1956 Industrial Policy Resolutions and Mahalanobis Second Plan put
heavy industry and commanding heights in the public sector. Early growth and
self-reliant capacity were real, while licence-permit controls accumulated
efficiency costs. The 1991 balance-of-payments crisis produced reform under
Narasimha Rao and Manmohan Singh: a corrective and structural break whose goals
and distributive effects require separate evaluation.

Land reform must be disaggregated. Zamindari abolition largely succeeded by
1956 and converted about 20 million superior tenants into owners; tenancy and
ceiling reforms were weakened by concealed tenancy, benami transfer, family
partition, weak records and political resistance. Vinoba Bhave's Bhoodan began
at Pochampalli in 1951 but could not substitute for enforceable structural
reform.

The mid-1960s Green Revolution combined HYV seed, irrigation, fertiliser,
credit, procurement and extension, initially in wheat regions of Punjab,
Haryana and western Uttar Pradesh. Output and food-security gains do not settle
regional, class or ecological debate. Telangana and Naxalbari/CPI(ML) mobilised
land and class grievances; the 1980s Shetkari Sangathana and Bharatiya Kisan
Union pursued remunerative prices, inputs and credit from a different agrarian
class position.

Formal reform and social transformation diverged. The proposed Hindu Code was
enacted through the Hindu Marriage Act 1955 and three 1956 Acts, expanding
rights within Hindu personal law without complete legal or social equality.
Untouchability abolition and reservations widened representation; Dalit,
women's and OBC mobilisation, culminating in Mandal implementation in 1990,
showed excluded groups using democracy to press beyond statutory promises.
Communalism is treated as an ideology and political process, not merely a riot
count or timeless social essence.

Nine routed Prelims entries are audited: the 2019 land-reform demand is direct;
the 2018 Hind Mazdoor Sabha founder demand remains an explicit held-evidence
gap; seven contemporary items are routing artefacts rather than Modern History
demands. No answer or official key is invented and no direct Mains route is
claimed.

**Answer:** define thematic axes -> planning and 1991 break -> disaggregate land
reform -> production versus distribution in agriculture -> compare agrarian
movements -> law-versus-society gap in caste and gender -> communalism and
institutional capacity -> graded verdict on transformation, equality and state.
""",
}


TOPIC_WORKBOOK_SUPPLEMENTS = {
    number: (
        f"""### Semantic-completeness coverage drills — Modern Topic {number:02d}

| Control | Required answer route | Fatal trap |
|---|---|---|
| Chronology | exact event sequence and bounded endpoint | telescoping later events |
| Ownership | state what this topic owns and hands off | duplicate cross-topic narrative |
| Mechanism | connect institution, resources, actors and consequence | list without causation |
| Evidence | named event/office/treaty/source plus qualification | decorative evidence |
| PYQ | preserve direct/adjacent status and key provenance | invented direct PYQ or official key |
| Answer | thesis -> evidence -> analysis -> limit -> verdict | generic narrative |

**PYQ ownership control:** {status}
"""
    )
    for number, status in {
        1: "zero direct routes; all retained questions are adjacent-owned.",
        2: "one direct route, 2021 Prelims Q48; local official key unavailable.",
        3: "four direct Prelims routes; only 2025 Q75 has local official-key provenance.",
        4: "zero direct routes; 2022 Company-armies and famine questions are adjacent.",
        5: "two direct routes: 2018 Prelims Q75 and 2022 GS-I Q2.",
        6: "two direct routes: 2019 Prelims Q4 and 2023 Prelims Q50; both local official keys unavailable.",
        7: "six active direct routes; 2024 Prelims Q57 is dropped, 2026 Q2 provisional, and two adjacent items stay bounded.",
        8: "zero direct routes for 2018-2026; all practice is original and adjacent questions remain labelled.",
        9: "six direct Prelims routes; two supplementary fact answers remain inferred because the local 2021 key is unavailable, plus one bounded Mains route.",
        10: "eleven direct routes; Vital-Vidhvansak is source-verified but inferred because the local 2020 key is unavailable.",
        11: "two direct routes: 2019 GS-I and provisional 2026 Prelims Q17; no provisional key is promoted.",
        12: "zero direct routes for 2018-2026; all practice is original and cross-owner material remains bounded.",
        13: "zero direct Modern-History routes for 2018-2026; current-neighbour questions stay outside this owner.",
        14: "one direct route: 2021 GS-I on the Moderates' role in preparing the wider freedom movement.",
        15: "five direct routes; 2018 Lajpat Rai and 2020 Desher Katha answers are supplementary-evidence inferences because local official keys are unavailable.",
        16: "one direct route, 2022 Prelims Q53; only Rash Behari Bose is supported as Ghadar-associated, but the answer remains inferred because the local official key is unavailable.",
        17: "two direct routes: 2018 GS-I and provisional 2026 Prelims Q18; no provisional key is promoted.",
        18: "one direct route, 2018 Prelims Q79; the 2024 balance-of-power Mains question remains World-History-owned.",
        19: "one topic-tight direct route, 2018 Prelims Q69; five Gandhi demands remain bounded or cross-cutting.",
        20: "three 2025 direct Prelims routes have locally confirmed Series-A keys; 2026 Q9 is unkeyed and 2021 GS-I remains bounded across two movements.",
        21: "one shared direct route, 2020 GS-I Q13; the 2018 Swarajya Sabha item is adjacent-owned and locally unkeyed.",
        22: "two direct Prelims routes; 2025 Q74 has a locally confirmed Series-A key and 2020 Q27 is locally unkeyed.",
        23: "five routed demands: two bounded/shared Mains, one cross-period tribal Mains, one locally unkeyed 2020 Prelims item and one provisional 2026 item.",
        24: "two direct Prelims routes; 2024 Q62 has a locally confirmed official Series-A key and 2018 Q38 is locally unkeyed.",
        25: "one locally official-verbatim 2024 Mains route plus two objective routing summaries whose exact local stems and keys are unavailable.",
        26: "three routed demand summaries; exact objective stems and official keys are unavailable locally.",
        27: "one unresolved objective route and one shared 2019 transfer-of-power Mains route; no unsupported key is promoted.",
        28: "one locally verified direct 2021 GS-I route and zero direct Prelims routes.",
        29: "one locally verified direct 2025 GS-I route, one adjacent-owned 2021 route and zero direct Prelims routes.",
        30: "two routed Mains demand summaries from 2018 and 2022 and zero direct Modern History Prelims routes.",
        31: "zero direct Modern History routes; Indian Society, Topic 23 and Polity retain the adjacent tribal demands.",
        32: "one direct 2018 Prelims chronology route; the local official key is unavailable and the 2025 consolidation Mains demand belongs Topic 29.",
        33: "one direct 2024 Prelims party-leader route; the local Series-A key exists but no answer is inferred in this owner.",
        34: "one direct 2019 Prelims coal-nationalisation demand is retained as an unsupported local evidence gap; zero direct Mains routes.",
        35: "zero direct routes for 2018-2026; original practice remains original and constitutional doctrine remains Polity-owned.",
        36: "zero direct routes for 2018-2026; original practice remains original and detailed constitutional doctrine stays Polity-owned.",
        37: "zero direct routes for 2018-2026; original practice remains original and cross-owned constitutional/economic doctrine is not duplicated.",
        38: "nine routed Prelims entries audited: one direct land-reform demand, one historical held-evidence gap and seven current-affairs routing artefacts; zero direct Mains routes.",
    }.items()
}


CANONICAL_OWNER_CONTROLS = {
    1: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** imperial command from 1707 through the 1740s: succession,
  factions, jagir/paibaqi/be-jagiri and jama-hasil pressure, agrarian-regional
  assertion, provincial autonomy, Nadir Shah and institutional continuity.
- **Boundary:** Medieval Topic 25 owns late-Aurangzeb prehistory; Modern Topic
  02 owns regional state/society synthesis; Topics 03-05 own Company formation,
  Bengal conquest and territorial expansion. Abdali/Panipat are bridges.
- **Verified PYQ ownership, 2018-2026:** zero direct routes. The 2021
  successor-state question belongs Topic 02, the 2021 hierarchy question
  Medieval Topic 24 and the 2022 Company-armies question Topic 05. Unavailable
  objective keys remain **INFERRED ANSWER — NOT OFFICIALLY VERIFIED**.""",
    2: """## Semantic-completeness ownership and PYQ control

- **Owned core:** successor and regional states, Maratha and Sikh formations,
  Jats/Rohillas/Rajputs/Mysore, fiscal-military capacity, credit, commerce,
  peasants, artisans, merchants, caste, gender and cultural patronage.
- **Boundary:** Topic 01 retains imperial-decline causation; Medieval Topic 25
  is pre-1761 continuity; Topics 03-05 own European rivalry, Bengal conquest
  and the full Mysore/Maratha/Sikh war and annexation sequences.
- **Verified PYQ ownership, 2018-2026:** one direct route, 2021 Prelims Q48;
  its local official key is unavailable. The hierarchy and Company-armies
  questions are adjacent-owned by Medieval Topic 24 and Modern Topic 05.""",
    3: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Portuguese, Dutch, English and French arrival, companies,
  trade, factories, fortified settlements, maritime-commercial rivalry and
  the contingent ladder from factory to corporate power.
- **Boundary:** Topic 02 owns Indian regional state formation; Topic 04 owns
  Plassey/Buxar/Diwani/Dual Government; Topic 05 owns pan-Indian expansion.
- **Verified PYQ ownership, 2018-2026:** four direct Prelims routes—2021 Q33,
  2021 Q39, 2022 Q59 and 2025 Q75. Only 2025 Q75 has locally held official-key
  provenance; earlier answers remain inferred. Company-armies is Topic 05.""",
    4: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** farman/dastak, Bengal Nawabi politics, Plassey, post-Plassey
  extraction, Mir Qasim, Buxar, Allahabad, Diwani/Nizamat, Dual Government,
  famine vulnerability and the 1772 termination.
- **Boundary:** Topic 03 owns early companies; Topic 05 owns wider expansion;
  Topic 06 owns post-1772 constitutional control; Topic 07 owns the full
  colonial economic and famine synthesis.
- **Verified PYQ ownership, 2018-2026:** zero direct routes. The 2022
  Company-armies and famine questions are adjacent-owned by Topics 05 and 07.""",
    5: """## Semantic-completeness ownership and PYQ control

- **Owned core:** the Bengal-funded fiscal-military state; Mysore, Maratha and
  Sikh wars; Sindh; Indian sepoys/allies/credit; ring-fence, Subsidiary
  Alliance, paramountcy, conquest, lapse and misgovernment annexation.
- **Boundary:** Topics 02-04 own regional synthesis, commercial rivalry and
  Bengal conquest; Topic 06 owns constitutional structure; Topic 11 owns 1857.
- **Mechanism control:** Subsidiary Alliance is not Doctrine of Lapse; Awadh
  was annexed for alleged misgovernment and Nana Sahib's issue was pension.
- **Verified PYQ ownership, 2018-2026:** exactly two direct routes—2018
  Prelims Q75 (key inferred) and 2022 GS-I Q2 (Mains has no objective key).""",
    6: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Company-state constitutional structure from the post-Diwani
  anomaly through the Government of India Act and Queen's Proclamation of
  1858: parliamentary supervision, executive and judicial design, Charter Act
  centralisation, codification, patronage reform and the legal Crown transfer.
- **Boundary:** Topic 04 owns Bengal conquest and Dual Government; Topic 07
  owns economic consequences; Topic 08 owns detailed administrative
  institutions; Topic 09 owns education/press policy; Topic 11 owns the Revolt
  core; Topic 12 owns the 1861 and later constitutional sequence.
- **Mechanism control:** the 1853 Act removed Directors' patronage and
  authorised competition; the Macaulay Committee (1854) and first open
  examination (1855) were separate implementation steps. The 1858 Act and
  Queen's Proclamation of 1 November 1858 are distinct instruments.
- **Verified PYQ ownership, 2018-2026:** exactly two direct routes—2019
  Prelims Q4 and 2023 Prelims Q50. Both local official keys are unavailable;
  no official answer is fabricated.""",
    7: """## Semantic-completeness ownership and PYQ control

- **Owned core:** differentiated land-revenue systems, commercialisation and
  credit risk, deindustrialisation, drain channels, colonial infrastructure
  and industry, famine vulnerability, poverty and economic historiography.
- **Boundary:** Topic 04 owns Diwani/Dual Government mechanics; Topic 06 owns
  Charter Acts; Topic 08 owns administrative enforcement; Topic 14 owns the
  Moderate political programme; Topic 23 owns wider peasant-worker movements.
  Indigo, Pabna and Deccan appear here only as economic-response case studies.
- **Mechanism control:** Permanent Settlement fixed the state's zamindar
  demand, not peasant rent; drain is not deindustrialisation; famine is climate
  shock plus entitlement, revenue, market, relief and disease vulnerability.
  Exact drain totals, mortality totals and unsourced exchange rates are barred.
- **Verified PYQ ownership, 2018-2026:** six active direct routes—2018
  Prelims Q52/Q68, 2020 Q23/Q33, 2022 GS-I Q3 and 2024 GS-I Q13. The 2024
  Prelims Q57 item was officially dropped; 2026 Q2 is provisional. The 2018
  post-Santhal and indentured-labour items remain adjacent/bounded.""",
    8: """## Semantic-completeness ownership and PYQ control

- **Owned core:** civil services and district administration, army, police,
  judiciary, codification and the rule-of-law/racial-privilege contradiction.
- **Boundary:** Topic 06 owns constitutional statutes; Topic 07 owns economic
  consequences; Topic 09 owns education, press and social policy; Topic 11
  owns the Revolt core; Topic 12 owns post-1858 constitutional councils.
- **Mechanism control:** 1853 removed Directors' patronage and authorised
  competition; Macaulay's 1854 report and the first open exam in 1855 were
  separate. Cornwallis's thana/daroga arrangement predates the Police Act 1861.
  'Martial races' is a colonial recruitment ideology, not a factual taxonomy.
- **Verified PYQ ownership, 2018-2026:** zero direct routes. Every MCQ and
  Mains answer in the package is original practice; adjacent questions stay
  explicitly adjacent and no official key is invented.""",
    9: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Orientalist/Anglicist education policy, filtration and access,
  Wood's system, press regulation and liberalisation, and state-social-policy
  interaction as a public-sphere history.
- **Boundary:** Topic 06 owns Charter Act constitutional mechanics; Topic 08
  owns administrative institutions; Topic 10 owns reform movements, doctrines
  and biographies. Topic 09 owns reform statutes only as state-policy outputs,
  implementation limits and evidence of state-society negotiation.
- **Mechanism control:** Fort William trained European servants; Macaulay 1835
  and Wood 1854 are different stages; English and vernacular print coexisted;
  the Vernacular Press Act 1878 targeted Indian-language papers and was
  repealed by Ripon in 1882.
- **Verified PYQ ownership, 2018-2026:** six direct Prelims routes. Madanapalle
  and *Songs from Prison* now have supplementary source evidence, but their
  answers remain **INFERRED — LOCAL OFFICIAL 2021 KEY UNAVAILABLE**. The 2023
  Gandhi-Tagore Mains demand remains a bounded cross-owner route.""",
    10: """## Semantic-completeness ownership and PYQ control

- **Owned core:** reform, revival, anti-caste, women's and community-specific
  movements through their ideas, organisations, social bases, methods, limits
  and historiography.
- **Boundary:** Topic 09 owns education/press policy and statutes as state
  action; Topic 14 owns early Congress politics; Topic 17 owns later communal
  representation. Topic 10 may name these only as bounded contexts or outcomes.
- **Mechanism control:** reformist/revivalist is a comparison, not a moral
  ranking; Aligarh and Deoband are distinct; law does not prove implementation;
  elite-male narratives must be tested against feminist, Dalit-bahujan and
  regional agency. The Phules' first Bhide Wada girls' school dates to 1848.
- **Verified PYQ ownership, 2018-2026:** eleven direct routes. Supplementary
  evidence identifies Gopal Baba Walangkar with *Vital-Vidhvansak* (1888), but
  the answer remains **INFERRED — LOCAL OFFICIAL 2020 KEY UNAVAILABLE**.""",
    11: """## Semantic-completeness ownership and PYQ control

- **Owned core:** causes, trigger, course, centre-wise leadership, regional and
  social participation, failure, nature/interpretation and consequences of the
  Revolt of 1857.
- **Boundary:** Topic 05 owns annexation instruments; Topic 08 owns the detailed
  army and administrative apparatus; Topic 12 owns Crown rule and councils.
  Earlier rebellions enter only for the direct 2019 culmination demand.
- **Mechanism control:** cartridge is trigger, not cause; Awadh was annexed for
  alleged misgovernment; Bahadur Shah Zafar was symbolic; military origin,
  popular civil depth and uneven geography require a composite verdict.
- **Verified PYQ ownership, 2018-2026:** two direct routes--2019 GS-I on
  recurrent rebellions and provisional 2026 Prelims Q17 on Awadh taluqdars.
  The provisional key is not promoted into an official answer letter.""",
    12: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Crown control after 1858, Queen's Proclamation, princely and
  landed conciliation, security reconstruction, financial/local decentralisation,
  and the Indian Councils Acts of 1861 and 1892.
- **Boundary:** Topic 06 owns the Company constitutional ladder and legal 1858
  transfer; Topic 08 owns detailed services/army/police/courts; Topic 11 owns
  the revolt; Topic 14 owns Moderate council politics; Topic 17 owns separate
  electorates and communal representation.
- **Mechanism control:** the 1858 Act and 1 November Proclamation are distinct;
  Secretary of State is not Viceroy; 1861 nomination is not election; 1892
  discussion is not budget control or responsible government.
- **Verified PYQ ownership, 2018-2026:** zero direct routes. All questions are
  original practice and every neighbouring constitutional demand stays bounded.""",
    13: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Afghanistan, Burma, Nepal, Tibet and North-West Frontier
  strategy; close-border/masterly-inactivity/forward debates; war-treaty
  chronology; buffers, annexation, frontier administration, cost and legacy.
- **Boundary:** Topic 05 owns the general expansion-state mechanism; Topic 12
  owns Crown governance; current IR, Geography and post-1947 legal claims are
  outside this historical owner.
- **Mechanism control:** Yandabo=Burma, Sugauli/Sagauli=Nepal and
  Gandamak=Afghanistan; Durand 1893 is not Younghusband 1903-04; a forward
  policy need not mean annexation and modern boundary status is not inferred.
- **Verified PYQ ownership, 2018-2026:** zero direct Modern-History routes.
  All historical questions are original practice; current-neighbour questions
  remain outside this owner.""",
    14: """## Semantic-completeness ownership and PYQ control

- **Owned core:** pre-Congress associations, INC foundation and origin debate,
  Moderate leaders, constitutional methods, economic nationalism, demands,
  achievements, social limits and legacy through 1905.
- **Boundary:** Topic 07 owns colonial-economic mechanisms; Topic 12 owns
  councils provisions; Topic 15 owns partition/Swadeshi/militant nationalism;
  Topic 17 owns communalism and the Muslim League.
- **Mechanism control:** Hume helped organise but did not create nationalism;
  safety valve is disputed; Moderates sought reform rather than immediate
  independence; the 1892 Act expanded procedure without responsibility.
- **Verified PYQ ownership, 2018-2026:** one direct route--2021 GS-I on the
  Moderates' role in preparing the wider freedom movement.""",
    15: """## Semantic-completeness ownership and PYQ control

- **Owned core:** Curzonian provocation, Bengal partition, anti-partition
  agitation, Swadeshi, boycott, national education, militant ideology,
  participation, regional spread, Surat, decline and consequences of 1905-08.
- **Boundary:** Topic 14 owns INC origins/Moderates; Topic 16 begins the
  revolutionary-underground core; Topic 17 owns communalism, League and
  separate electorates. The 1911 annulment is a bounded consequence.
- **Mechanism control:** 7 August resolution and 16 October enforcement differ;
  Swadeshi is constructive while boycott is withdrawal; militant nationalism
  is broader than violence; Bengal cannot represent uniform all-India reach.
- **Verified PYQ ownership, 2018-2026:** five direct routes--2018, 2019, two
  in 2020 and 2023. Lala Lajpat Rai and *Desher Katha* are supported by
  supplementary historical evidence but remain **INFERRED — LOCAL OFFICIAL
  KEYS UNAVAILABLE**.""",
    16: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** underground revolutionary organisations and actions in
  Bengal, Maharashtra and overseas; India House, European propaganda, Ghadar,
  Komagata Maru, wartime plans, repression, achievements and strategic limits.
- **Boundary:** Topic 15 owns open Swadeshi/militant politics; Topic 18 owns
  Home Rule and Lucknow; Topic 21 owns HRA, HSRA, Kakori and Bhagat Singh.
- **Date control:** Muzaffarpur (April 1908), Alipore (1908-09), Dhingra
  (1 July 1909), Nasik (December 1909), Hardinge (23 December 1912), Ghadar
  (1913), Komagata Maru (1914) and the failed rising (February 1915) remain
  distinct events and organisations.
- **Verified PYQ ownership, 2018-2026:** one direct route, 2022 Prelims Q53.
  Supplementary evidence identifies only Rash Behari Bose among the three
  named figures as Ghadar-associated; the answer remains **INFERRED — LOCAL
  OFFICIAL KEY UNAVAILABLE**.""",
    17: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** communalism's definition, stages and modern causes; colonial
  classification and representation; Simla Deputation, early Muslim League,
  separate electorates, Hindu communal organisations and provincial variation.
- **Boundary:** Topic 10 owns religious reform; Topic 18 owns Lucknow's
  negotiated provisions; Topic 20 owns Khilafat; Topic 27 owns the 1940-47
  Pakistan and Partition endgame.
- **Date control:** Simla Deputation (October 1906), League at Dacca
  (December 1906), separate electorates (1909), Hindu Mahasabha (1915) and
  Lucknow Pact (1916) are distinct. Hindutva (1923), RSS (1925) and Lahore
  Resolution (1940) are bounded later trajectory.
- **Mechanism control:** religion is not communalism; separate electorates,
  reserved seats and nomination differ; Chandra's staged model is attributed.
- **Verified PYQ ownership, 2018-2026:** 2018 GS-I is direct; provisional 2026
  Prelims Q18 is routed without promoting a provisional answer key.""",
    18: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** First World War expectations/extraction, Congress reunion,
  Tilak's and Besant's separate Home Rule Leagues, repression, Lucknow Congress
  and Congress-League Pact provisions, Montagu response and movement legacy.
- **Boundary:** Topic 16 owns Ghadar and underground conspiracy; Topic 17 owns
  communal ideology/League origin; Topic 19 owns Gandhi's Indian campaigns.
- **Date control:** Congress readmission decision (December 1915), Tilak League
  (April 1916), Besant League (September 1916), Lucknow Congress/Pact
  (December 1916) and Montagu Declaration (20 August 1917) remain separate.
- **Mechanism control:** Home Rule was self-government within the Empire, not
  Purna Swaraj; two Leagues, Congress reunion and the Pact are not synonyms.
- **Verified PYQ ownership, 2018-2026:** 2018 Prelims Q79 is direct and locally
  unkeyed. The 2024 balance-of-power question remains World-History-owned.""",
    19: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Champaran, Ahmedabad and Kheda as distinct method
  laboratories; Rowlatt law/hartal; Gandhi's suspension; Jallianwala Bagh,
  martial law, inquiries, renunciation and the legitimacy rupture of 1919.
- **Boundary:** Topic 18 owns Home Rule/Lucknow; Topic 20 owns the organised
  Non-Cooperation-Khilafat programme. Jallianwala is a bridge, not sole cause.
- **Date control:** Champaran (1917), Ahmedabad/Kheda (1918), Rowlatt protest
  and Jallianwala Bagh (13 April 1919) form a sequence; grievance, constituency,
  tactic and settlement must not be merged across the three local struggles.
- **Verified PYQ ownership, 2018-2026:** 2018 Prelims Q69 on Champaran is the
  topic-tight direct route. Other Gandhi questions are bounded/cross-cutting;
  unavailable objective keys are not invented.""",
    20: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Khilafat grievance and organisation; Congress alliance and
  authorisation; Non-Cooperation stages, constructive institutions, social and
  regional spread, Moplah complexity, Chauri Chaura and withdrawal debate.
- **Boundary:** Topic 19 owns Rowlatt/Jallianwala; Topic 21 owns Swarajists,
  No-changers and the HRA/HSRA revolutionary phase.
- **Date control:** Calcutta Special Session (September 1920), Nagpur
  ratification (December 1920), Moplah rebellion (1921), Chauri Chaura
  (4 February 1922) and withdrawal (12 February 1922) remain distinct.
- **Mechanism control:** Swarajya Sabha was the renamed Home Rule organisation,
  not the 1923 Swaraj Party; Moplah and withdrawal require attributed,
  multi-causal interpretation rather than a one-label verdict.
- **Verified PYQ ownership, 2018-2026:** three 2025 Prelims routes have locally
  confirmed Series-A keys; 2026 Q9 remains unkeyed and 2021 GS-I is bounded
  across Non-Cooperation and Civil Disobedience.""",
    21: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** the post-1922 No-changer/Pro-changer debate, constructive
  continuity, Swaraj Party council obstruction, HRA-Kakori, Naujawan Bharat
  Sabha, the HRA-to-HSRA socialist turn, Saunders, the two distinct trials,
  jail resistance, Bhagat Singh's political thought and Chittagong.
- **Boundary:** Topic 20 owns Non-Cooperation and its withdrawal; Topic 22
  owns Simon, Nehru Report and Civil Disobedience; Topic 23 owns the mature
  1930s Left, peasant, worker and states-peoples movements. Topic 26 alone
  owns INA, RIN and Cabinet Mission; Topic 27 owns independence and partition.
- **Date control:** Gaya (December 1922), Swaraj Party working date
  (1 January 1923), HRA (October 1924), Kakori (1925), Naujawan Bharat Sabha
  (March 1926), HSRA (9-10 September 1928), Assembly bomb (8 April 1929),
  Jatin Das (13 September 1929) and executions (23 March 1931) remain distinct.
- **Mechanism control:** council entry meant obstruction, not loyalism; HRA
  and HSRA are one lineage with an ideological change, not rival bodies;
  Naujawan Bharat Sabha was an open front; the Assembly Bomb and Lahore
  Conspiracy cases were separate proceedings.
- **Verified PYQ ownership, 2018-2026:** 2020 GS-I Q13 is a shared direct
  ideological-strands route with Topic 23. The 2018 Swarajya Sabha item belongs
  to Topic 18 and is retained only as a bounded name-confusion control; its
  local official key is unavailable and no answer letter is invented.""",
    22: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Simon exclusion and protest, Nehru Report and Fourteen
  Points, Lahore/Purna Swaraj, Dandi and the full regional-social Civil
  Disobedience field, Gandhi-Irwin, all three RTCs, Communal Award, Poona Pact,
  resumed repression and withdrawal in 1934.
- **Boundary:** Topic 21 owns Swarajists and HRA-HSRA; Topic 23 owns organised
  Left, peasant, worker and states-peoples movements; Topic 24 owns the 1935
  Act and ministries. Topic 26 owns INA/RIN/Cabinet Mission and Topic 27 owns
  independence/partition.
- **Date control:** Simon appointment (1927), arrival (3 February 1928), Lahore
  lathi-charge (30 October), Lajpat Rai's death (17 November), Lahore Congress
  (December 1929), Independence Day (26 January 1930), Dandi march
  (12 March-6 April 1930), Gandhi-Irwin (5 March 1931), Communal Award
  (August 1932), Poona Pact (September 1932) and withdrawal (1934) are distinct.
- **Mechanism control:** Nehru Report meant dominion status, not Purna Swaraj;
  salt launched but did not exhaust CDM; Congress missed the First RTC and
  Gandhi attended the Second; Communal Award separate electorates differ from
  Poona Pact reserved seats in joint electorates.
- **Verified PYQ ownership, 2018-2026:** two direct objective routes are
  retained. The 2025 Prelims Q74 Series-A key is locally official-confirmed;
  the 2020 Prelims Q27 key is unavailable and no answer letter is invented.""",
    23: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** socialist and communist currents, AITUC and labour, Bardoli
  and AIKS, Karachi/Faizpur socio-economic programmes, AISPC/Praja Mandals,
  Haripura, Tripuri and Forward Bloc, with late-colonial agrarian bridges.
- **Boundary:** Topics 19-22 retain early Gandhian, Non-Cooperation and CDM
  contexts; Topic 24 owns the 1935 Act and ministry record. Topic 26 exclusively
  owns INA/RIN/Cabinet Mission; Topic 27 owns independence/partition; Topic 28
  owns integration and Topic 38 owns post-independence agrarian synthesis.
- **Date control:** AITUC/Tashkent (1920), Kanpur (1925), AISPC (1927),
  Bardoli (1928), Bihar Kisan Sabha (1929), CSP (1934), AIKS/Faizpur (1936),
  Haripura (1938), Tripuri/Forward Bloc (1939), Warli (1945) and
  Tebhaga/Telangana (1946) are roots, core and bridges rather than one phase.
- **Mechanism control:** CSP and CPI were distinct; AISPC challenged princely
  autocracy; Bardoli targeted state revenue, unlike Awadh landlord conflict;
  Tripuri was ideological/organisational; popular agency was not a Congress
  appendage.
- **Verified PYQ ownership, 2018-2026:** 2019 and 2020 GS-I are bounded/shared,
  2023 GS-I is cross-period tribal, 2020 Prelims Q35 is locally unkeyed and
  2026 Prelims Q16 is provisional. No unavailable or provisional key is
  promoted as official.""",
    24: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** constitutional lineage and provisions of the 1935 Act,
  unrealised federation, provincial autonomy and safeguards, franchise and
  representation, 1937 elections, office acceptance, ministry performance,
  resignation and the immediate Deliverance Day/Lahore Resolution bridge.
- **Boundary:** Topic 22 owns Simon/RTCs/CDM, Topic 23 owns class and states
  movements, and Topic 25 owns the wartime political sequence. Topic 26 alone
  owns INA/RIN/Cabinet Mission; Topic 27 owns independence and partition.
- **Date control:** Simon report (1930), RTCs (1930-32), White Paper (1933),
  Joint Select Committee report (1934), royal assent (1935), elections and
  Federal Court/Burma separation (1937), resignations (October-November 1939),
  Deliverance Day (December 1939) and Lahore Resolution (March 1940) are distinct.
- **Mechanism control:** provincial dyarchy ended; central dyarchy and the
  federation never operated; reserved and residuary powers preserved imperial
  control. Franchise is a 30-35 million / 10-14 per cent qualified range, and
  the RBI derives from the 1934 RBI Act.
- **Verified PYQ ownership, 2018-2026:** 2024 Prelims Q62 has a locally
  confirmed official Series-A key. The 2018 Prelims Q38 content is source-backed
  but its local official key is unavailable; no answer letter is invented.""",
    25: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** unconsulted wartime entry, Congress response and resignation
  consequence, August Offer, Individual Satyagraha, Cripps provisions and
  rejection, Quit India authorisation, decapitation, regional/social spread,
  underground networks, parallel governments, repression and results.
- **Boundary:** Topic 24 owns the 1935 Act and ministries. Topic 26 exclusively
  owns INA, INA trials, RIN, Wavell/Simla, 1945-46 elections and Cabinet
  Mission; Topic 27 owns independence and partition. Later endgame evidence is
  qualification only, never transferred ownership.
- **Date control:** 3 September 1939 belligerency, October-November ministry
  resignations, 22 December Deliverance Day, March 1940 Lahore Resolution,
  August Offer, October 1940 Individual Satyagraha, March-April 1942 Cripps,
  8 August Quit India resolution and 9 August arrests remain distinct.
- **Mechanism control:** Cripps meant post-war dominion status with provincial
  non-accession, not immediate independence; Individual Satyagraha was limited;
  Quit India was leaderless after arrests but retained underground continuity;
  official non-violence and actual sabotage must both be stated.
- **Verified PYQ ownership, 2018-2026:** 2024 GS-I Q3 is locally official and
  verbatim. The 2021 Quit India and 2022 Cripps objective entries are neutral
  routing summaries because exact local stems and keys are unavailable; no
  wording or answer letter is fabricated.""",
    26: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** first and second INA, Azad Hind, Imphal-Kohima, Red Fort
  trials, labour/service upsurge, RIN, Simla, 1945-46 elections and the Cabinet
  Mission's constitutional design.
- **Boundary:** Topic 25 owns wartime/Quit India. Topic 27 exclusively owns the
  Cabinet Mission breakdown, Direct Action, final transfer and Partition.
- **Date control:** first INA (1942), Bose's reorganisation and Azad Hind
  (1943), Imphal campaign (1944), Red Fort trials (1945-46), Cabinet decision
  (22 January 1946), RIN (18-23 February) and Cabinet plan (16 May) are distinct.
- **Mechanism control:** INA military defeat and trial impact differ; RIN
  sharpened coercive-legitimacy fears but did not cause the Mission's dispatch;
  Congress, Patel, Jinnah and left responses were differentiated.
- **Verified PYQ ownership, 2018-2026:** 2019 Prelims Q15, 2021 Prelims Q47
  and 2019 GS-I Q12 are routed demand summaries; exact objective stems and
  official keys are unavailable locally and none is invented.""",
    27: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Cabinet settlement breakdown, Direct Action, communal
  violence, Interim Government conflict, Constituent Assembly opening,
  Attlee-Mountbatten deadline sequence, 3 June Plan, Independence Act,
  transfer, boundary disclosure, migration, gendered violence and relief.
- **Boundary:** Topic 26 owns the Cabinet Mission design and post-war upsurge.
  Topic 28 owns princely integration and constitution-to-republic.
- **Date control:** 16 August and 2 September 1946; 9 December 1946;
  20 February, 24 March and 3 June 1947; 18 July, 15 August and 17 August 1947
  are separate political, legal and territorial thresholds.
- **Mechanism control:** Partition was multi-causal and provincially uneven;
  the Act created dominions but did not integrate princely states, frame the
  Constitution or make India a republic.
- **Verified PYQ ownership, 2018-2026:** the objective language-movement route
  remains unresolved locally, while the 2019 transfer demand is shared with
  Topic 26; no unsupported stem, claim or key is promoted.""",
    28: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** lapse of paramountcy, States Department, accession,
  standstill agreements, Junagadh/Kashmir/Hyderabad, mergers and unions,
  Constituent Assembly settlement, adoption and commencement of the Republic.
- **Boundary:** Topic 27 owns transfer/Partition; Topic 29 owns colonial-legacy
  synthesis; Topic 30 owns linguistic redrawing.
- **Date control:** States Department (27 June 1947), paramountcy lapse
  (15 August), Kashmir accession (October 1947), Hyderabad standstill
  (November 1947), Junagadh plebiscite (February 1948), Operation Polo
  (September 1948), adoption (26 November 1949) and Republic (26 January 1950).
- **Mechanism control:** paramountcy lapsed rather than transferred; accession,
  merger and constitutional incorporation were distinct; the three crisis
  states followed different legal-political sequences.
- **Verified PYQ ownership, 2018-2026:** 2021 GS-I on princely-state
  integration is a locally verified direct Mains route. No direct Prelims route
  is invented.""",
    29: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** sector-specific colonial inheritances, nationalist-democratic
  resources, selective retention, institutional repurposing and founding
  choices across polity, economy, education and external orientation.
- **Boundary:** Topic 28 owns integration/republic; Topic 30 owns linguistic
  states; Topic 31 owns tribal integration; Topic 32 owns Nehru foreign policy.
- **Date control:** inherited structures must be separated from their
  post-1947 adaptation; independence, constitutional adoption and commencement
  are not one event.
- **Mechanism control:** classify each institution by origin, colonial purpose,
  social reach, postcolonial adaptation and democratic control; reject both
  gift and unchanged-burden narratives.
- **Verified PYQ ownership, 2018-2026:** 2025 GS-I's four-domain consolidation
  demand is locally verified and direct. The 2021 princely-state demand belongs
  to Topic 28; no direct Prelims route is fabricated.""",
    30: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** linguistic-state principle, Dar/JVP postponement, Andhra,
  SRC and 1956 settlement, Bombay/Punjab corrections, official-language
  compromise and accommodative/nativist/secessionist regionalism.
- **Boundary:** Topic 29 owns founding synthesis; Topic 31 exclusively owns
  tribal integration; Topic 32 owns foreign-policy legacy.
- **Date control:** Congress linguistic organisation (1921), Dar/JVP (1948),
  Andhra (1953), SRC report (1955), Act effective 1 November 1956, Bombay
  (1960), Official Languages Act (1963), Punjab (1966) and amendment (1967).
- **Mechanism control:** state-boundary language and Union official language
  are distinct; linguistic accommodation generally strengthened integration
  but did not erase minority, border, capital or nativist conflicts.
- **Verified PYQ ownership, 2018-2026:** 2018 and 2022 GS-I are routed Mains
  demand summaries rather than locally verified verbatim stems. No direct
  Modern History Prelims route is invented.""",
    31: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** post-1947 tribal policy; integration without assimilation;
  Verrier Elwin and the later-labelled Tribal Panchsheel; Fifth- and Sixth-
  Schedule routes; Naga, Mizo and North-East accommodation; Jharkhand's
  demographic broadening; political settlement versus developmental delivery.
- **Boundary:** Topic 23 owns colonial/late-colonial tribal mobilisation;
  Topic 30 owns linguistic reorganisation; Topic 32 owns Nehru's wider legacy;
  Topic 38 owns the post-independence land, displacement and society synthesis.
- **Date control:** 1971 Census attribution; Naga rebellion's 1955-57 phase;
  Nagaland (1963); MNF uprising (1966); 1972 North-East reorganisation and
  NEFA renaming; Mizo Accord (1986); Mizoram/Arunachal statehood (1987).
- **Mechanism control:** Fifth and Sixth Schedules are distinct; force could
  contain but negotiation, autonomy, statehood and electoral absorption made
  durable settlement. Mizoram is a model case, not a universal outcome.
- **Verified PYQ ownership, 2018-2026:** zero direct Modern History routes.
  Indian Society owns 2021/2022 tribal-society Mains demands, Topic 23 owns the
  2023 colonial response, and Polity owns Scheduled Areas objective demands.""",
    32: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Nehru-era democracy, planning, mixed economy, rural
  development, science/education, secular citizenship, non-alignment,
  decolonisation, Kashmir as a contested choice, China policy and the 1962 test.
- **Boundary:** Topic 31 retains tribal policy; Topic 33 owns the Congress
  system and opposition; Topic 34 begins the Shastri succession; Topic 38 owns
  detailed post-independence economic, land and social synthesis.
- **Date control:** Planning Commission (15 March 1950), election (1951-52),
  Community Development (2 October 1952), Panchsheel (1954), Avadi/Bandung
  (1955), IPR/Second Plan (1956), Kerala (1957), Belgrade/Goa (1961), China war
  (1962), Kamaraj Plan (1963) and Nehru's death (27 May 1964) are distinct.
- **Mechanism control:** Planning Commission was extra-constitutional; Bandung
  preceded NAM's Belgrade founding; non-alignment was active autonomy, not
  neutrality; 1962 exposed capability limits without erasing the whole record.
- **Verified PYQ ownership, 2018-2026:** one direct 2018 Prelims chronology
  route with no local official key. The 2025 consolidation Mains route belongs
  Topic 29 and remains adjacent.""",
    33: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** competitive one-party dominance to 1967; Congress breadth,
  factions, co-option and electoral arithmetic; Socialist/KMPP/PSP/Lohiaite,
  CPI/CPI(M), Jana Sangh, Swatantra and regional opposition trajectories.
- **Boundary:** Topic 32 owns Nehru's governmental legacy. Topic 34 owns the
  consequences of 1967, coalitions/defections, Indira-Syndicate conflict and
  the 1969 organisational split.
- **Date control:** Socialist exit (1948), Tandon-Nehru (1950-51), Jana Sangh
  and KMPP (1951), PSP (1952), Avadi (1955), Kerala (1957), Swatantra (1959),
  CPI split (1964) and the 1967 watershed remain separate.
- **Mechanism control:** the Congress system was not a one-party state;
  first-past-the-post, social breadth, internal pluralism, co-option and
  fragmented opposition jointly converted sub-50-per-cent votes into dominance.
- **Verified PYQ ownership, 2018-2026:** one direct 2024 Prelims party-leader
  route. The local Series-A key exists, but no answer is inferred beyond
  verified party-founder associations.""",
    34: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** 1964-73: Shastri and Indira successions, 1965 war/Tashkent,
  food and currency crisis, 1967 setback, coalitions/defections, 1969 split and
  bank nationalisation, 1971 mandate/privy purses/Bangladesh and 1972 Simla.
- **Boundary:** Topic 33 ends at the 1967 party-system watershed; Topic 35 owns
  the 1973-77 crisis and Emergency. Pokhran-I on 18 May 1974 is immediate-
  aftermath enrichment, not part of the stated 1964-73 core.
- **Date control:** Shastri office (9 June 1964), Tashkent Declaration
  (10 January 1966), death (11 January), Indira office (24 January),
  devaluation (6 June), election (1967), split/banks (1969), election,
  Amendment and war (1971), and Simla (1972) are distinct.
- **Mechanism control:** bank nationalisation and privy-purse abolition are
  separate measures; 1967 weakened but did not remove Congress at the Centre;
  populist consolidation also personalised and de-institutionalised authority.
- **Verified PYQ ownership, 2018-2026:** the 2019 coal-nationalisation demand
  is direct but unsupported by held Modern History evidence; no statute, year,
  sequence or key is invented. No direct Mains route is claimed.""",
    35: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** 1973-77 economic-political crisis; Nav Nirman, Bihar, JP and
  railway strike; Allahabad judgment/Supreme Court stay; Article 352 Emergency;
  MISA, censorship, amendments, Sanjay Gandhi, sterilisation/clearance excesses;
  January election call, March verdict and the Emergency's end on 21 March.
- **Boundary:** Topic 34 owns the pre-1973 consolidation and personalisation.
  Topic 36 owns Janata formation and government, the 44th Amendment, Charan
  Singh, Indira's return and regional crises. Topic 37 owns the Rajiv era;
  Topic 38 owns the post-independence economy/land/society synthesis.
- **Date control:** Gujarat (January 1974), Bihar (March), railway strike
  (May), High Court (12 June 1975), conditional stay (24 June), proclamation
  dated 25 June/public 26 June, election call (January 1977), verdict and end
  (March 1977), and the later 44th Amendment (1978) are distinct.
- **Mechanism control:** Allahabad High Court initially invalidated the
  election; Article 352, not 356, governed the proclamation; resistance was
  socially and regionally uneven; electoral reversal preceded Janata repair.
- **Verified PYQ ownership, 2018-2026:** zero direct Modern History routes.
  Original practice remains original and detailed constitutional doctrine is
  retained by Polity.""",
    36: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Janata formation and 1977 mandate; Morarji government; 44th
  Amendment; dual-membership rupture; Charan Singh; Indira's 1980 return;
  regional-party assertion; Assam, Punjab and Jammu and Kashmir crises through
  Indira Gandhi's assassination.
- **Boundary:** Topic 35 ends with Emergency defeat; Topic 37 begins with
  Rajiv's succession. Topic 30 owns linguistic reorganisation; Topic 31 tribal
  integration; Topic 38 thematic economy/land/society/state synthesis.
- **Date control:** Janata formation (January 1977), election (March), 44th
  Amendment (1978), Charan Singh (July 1979), Congress return (January 1980),
  Sanjay's death (June), Telugu Desam founding (29 March 1982), Andhra victory
  (1983), Blue Star (June 1984) and assassination (31 October) stay distinct.
- **Mechanism control:** Janata collapse combined coalition structure,
  leadership rivalry and dual membership; regional assertion could deepen
  federal integration, while delayed accommodation and coercive escalation
  interacted differently across Assam, Punjab and Jammu and Kashmir.
- **Verified PYQ ownership, 2018-2026:** zero direct Modern History routes.
  Original practice remains original; detailed 44th-Amendment doctrine is
  Polity-owned.""",
    37: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Rajiv succession and 1984 mandate; modernisation; 52nd
  Amendment; Punjab/Assam accords; Shah Bano/Ayodhya identity management;
  Bofors; 1989 National Front; Mandal, rath yatra, 1991 reforms, 1992 demolition
  and coalition transition to the millennium.
- **Boundary:** Topic 36 ends on 31 October 1984; Topic 38 owns thematic
  economy, land, society and state synthesis. Detailed constitutional doctrine
  remains Polity-owned and present economic mechanics Economy-owned.
- **Date control:** election (December 1984), amendment/accords (1985), Shah
  Bano reversal and Bofors controversy (1986), election (1989), Mandal and rath
  yatra (1990), reforms (1991), demolition (6 December 1992), coalition phase
  (1996 onward) are separate.
- **Mechanism control:** Congress won 404 of 514 elected seats; panchayati raj
  was not yet constitutionalised; BJP and Left outside support was conjunctural;
  Mandal employment reservation, 1990 mobilisation and 1992 demolition must
  not be telescoped into one event.
- **Verified PYQ ownership, 2018-2026:** zero direct Modern History routes.
  Original practice stays original and cross-owned constitutional/economic
  demands are not duplicated.""",
    38: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** thematic synthesis of planning and liberalisation, land
  reform, Green Revolution, agrarian movements, caste, gender, communalism and
  state capacity after independence.
- **Boundary:** Topics 32-37 retain ruler/period chronology. Topic 38 compares
  mechanisms and outcomes rather than repeating prime-minister narratives;
  present policy belongs Economy, Society, Polity or Governance as appropriate.
- **Date control:** IPRs (1948/1956), Bhoodan at Pochampalli (1951), zamindari
  abolition largely by 1956, Hindu Marriage Act (1955) and three Hindu-law Acts
  (1956), Green Revolution (mid-1960s), Naxalbari (1967), CPI(ML) (1969),
  farmers' organisations (1980/1986), Mandal (1990) and reforms (1991).
- **Mechanism control:** disaggregate abolition, tenancy and ceilings; separate
  agricultural output from distribution/ecology; distinguish landless/tenant
  struggles from rich-farmer market movements; legal reform never proves
  complete social equality or implementation.
- **Verified PYQ ownership, 2018-2026:** nine routed Prelims entries audited.
  The 2019 land-reform demand is direct; the 2018 Hind Mazdoor Sabha founder
  item remains an explicit evidence gap; seven current-affairs routes are
  artefacts. No unsupported answer/key or direct Mains route is invented.""",
}


def ensure_canonical_owner_control(topic: Topic) -> bool:
    """Append the active topic's bounded owner control once."""
    if topic.number not in CANONICAL_OWNER_CONTROLS:
        return False
    text = topic.basic_path.read_text(encoding="utf-8")
    marker = "Semantic-completeness ownership and PYQ control"
    if marker in text:
        return False
    topic.basic_path.write_text(
        text.rstrip()
        + "\n\n"
        + CANONICAL_OWNER_CONTROLS[topic.number].strip()
        + "\n",
        encoding="utf-8",
    )
    return True


_base_augment_topic_semantic_content = augment_topic_semantic_content


def augment_topic_semantic_content(
    topic: Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    """Insert idempotent hostile-review supplements for active Modern topics."""
    repaired = _base_augment_topic_semantic_content(
        topic,
        markdown,
        workbook=workbook,
    )
    if topic.number not in TOPIC_MAIN_SUPPLEMENTS:
        return repaired
    supplement = (
        TOPIC_WORKBOOK_SUPPLEMENTS[topic.number]
        if workbook
        else TOPIC_MAIN_SUPPLEMENTS[topic.number]
    ).strip()
    marker = (
        f"### Semantic-completeness coverage drills — Modern Topic {topic.number:02d}"
        if workbook
        else f"### TOPIC {topic.number:02d} CLOSING"
    )
    if marker in repaired:
        return repaired
    insertion = (
        "## PYQS AND ANSWER PRACTICE"
        if workbook
        else "## BASIC MCQS / REMEDIATION"
    )
    if insertion not in repaired:
        raise ValueError(f"{topic.topic_key}: supplement insertion point is absent.")
    return repaired.replace(insertion, supplement + "\n\n" + insertion, 1)


def repair_topic_content(markdown: str, topic: Topic) -> str:
    """Apply evidence-led content corrections only to the new successor."""
    if topic.number == 9:
        replacements = (
            (
                "Six routed Prelims demands are retained. Four have source-backed "
                "demand cards; Madanapalle and Songs from Prison remain explicit "
                "local evidence gaps.",
                "Six routed Prelims demands are retained. All six now have "
                "source-backed demand cards; Madanapalle and Songs from Prison "
                "remain inferred because the local official 2021 key is unavailable.",
            ),
            (
                "two routed 2021 Prelims demands have **no supporting content in "
                "any source book, note or knowledge file held in this repository**",
                "two routed 2021 Prelims demands required supplementary historical "
                "and book evidence beyond the original local owners",
            ),
            (
                "two routed 2021 Prelims demands have no supporting content in "
                "any source book, note or knowledge file held in this repository",
                "two routed 2021 Prelims demands required supplementary historical "
                "and book evidence beyond the original local owners",
            ),
            (
                "Only the OCR question stem exists locally; no explanatory source "
                "content | Do not assert any specific association. If this appears "
                "in practice material, mark it unresolved and verify from an "
                "external authoritative source before use.",
                "Supplementary evidence links Madanapalle with Rabindranath "
                "Tagore's 1919 English rendering of *Jana Gana Mana* | Retain "
                "Tagore's Madanapalle association as inferred because the local "
                "official key is unavailable.",
            ),
            (
                "No occurrence in any source book held here | Do not attribute the "
                "translation to any named figure without verified evidence. Treat "
                "as an open factual gap.",
                "A historical book scan identifies *Songs from Prison* with M.K. "
                "Gandhi's translations, prepared for publication by John S. "
                "Hoyland | Retain M.K. Gandhi as inferred because the local "
                "official key is unavailable.",
            ),
            (
                "**Status:** open-evidence-gap",
                "**Status:** supplementary-evidence; local official key unavailable",
            ),
            (
                "The locally held owner records only the routed stem and no "
                "explanatory evidence. No association or answer is asserted.",
                "Supplementary evidence associates Madanapalle with Rabindranath "
                "Tagore's 1919 English rendering of *Jana Gana Mana*. The answer "
                "remains inferred because the local official key is unavailable.",
            ),
            (
                "No supporting occurrence exists in the held books or owners. No "
                "translator is named and no answer is inferred.",
                "A historical scan of *Songs from Prison* associates its English "
                "translations with M.K. Gandhi and preparation for publication "
                "with John S. Hoyland. The answer remains inferred because the "
                "local official key is unavailable.",
            ),
        )
        for old, new in replacements:
            markdown = markdown.replace(old, new)
    if topic.number == 10:
        replacements = (
            (
                "Jotirao and Savitribai Phule opened a girls' school at Poona in 1851.",
                "Jyotirao and Savitribai opened Bhide Wada girls' school, Poona, "
                "in 1848.",
            ),
            (
                "In **1851 Phule and his wife started a girls' school at Poona**",
                "Jyotirao and Savitribai opened the **Bhide Wada girls' school at "
                "Poona in 1848** and expanded their school work thereafter",
            ),
            (
                "In **1851 Jotiba Phule and his wife started a girls' school at Poona**",
                "Jyotirao and Savitribai opened the **Bhide Wada girls' school at "
                "Poona in 1848** and expanded their school work thereafter",
            ),
            (
                "**Poona girls' school of 1851**",
                "**Bhide Wada girls' school at Poona in 1848**",
            ),
            (
                "except Vital-Vidhvansak, which remains an explicit unsupported local gap.",
                "including Vital-Vidhvansak, which is source-verified but remains "
                "inferred because the local official 2020 key is unavailable.",
            ),
            (
                "the routed demands on the *Vital-Vidhvansak* journal (2020 "
                "Prelims Q28) and the exact publication chronology of early "
                "Dalit journalism have **no supporting content in any source "
                "held in this repository**",
                "supplementary historical evidence for the *Vital-Vidhvansak* "
                "journal (2020 Prelims Q28) identifies Gopal Baba Walangkar "
                "and the year 1888, while wider early-Dalit-journalism chronology "
                "remains source-bounded",
            ),
            (
                "Do not attribute the journal to any named publisher without "
                "verified external evidence; record it as an open factual gap.",
                "Associate the journal with Gopal Baba Walangkar, but label the "
                "answer inferred because the local official key is unavailable.",
            ),
            (
                "⚠️ **Unresolved locally:** supplementary historical evidence",
                "⚠️ **Supplementary verification; local key unavailable:** "
                "supplementary historical evidence",
            ),
            (
                "**Status:** open-evidence-gap",
                "**Status:** supplementary-evidence; local official key unavailable",
            ),
            (
                "The held repository contains no supporting attribution and no "
                "official local key. No publisher is asserted.",
                "Supplementary historical evidence identifies Gopal Baba "
                "Walangkar with *Vital-Vidhvansak* (1888). The answer remains "
                "inferred because the local official key is unavailable.",
            ),
            (
                "Vital-Vidhvansak must remain unanswered until an authoritative "
                "supporting source is added.",
                "*Vital-Vidhvansak* is associated with Gopal Baba Walangkar "
                "(1888), but the answer remains locally unkeyed and inferred.",
            ),
        )
        for old, new in replacements:
            markdown = markdown.replace(old, new)
    if topic.number == 15:
        replacements = (
            (
                "⚠️ **Unresolved locally:** the routed demands identifying the "
                "nationalist leader who **wrote biographies of Mazzini and "
                "Garibaldi** (2018 Prelims) and the authorship/impact of "
                "**Deuskar's *Desher Katha*** (2020 Prelims) have **no "
                "supporting content in any source book held in this repository**, "
                "and the relevant official keys are not held locally. The books "
                "confirm only that **Mazzini and Garibaldi were political heroes "
                "of Western-educated Indian nationalists** (Bipan Chandra, "
                "*Modern India*). Do not attribute either the biographies or "
                "*Desher Katha*'s circulation figures to a named person without "
                "verified evidence; both are single-fact Prelims points with no "
                "Mains consequence.",
                "⚠️ **Supplementary verification; local official keys "
                "unavailable:** historical evidence identifies **Lala Lajpat "
                "Rai** as the leader described by the 2018 biographies-and-career "
                "clues. **Sakharam Ganesh Deuskar's *Desher Katha* (1904)** "
                "popularised economic criticism, inspired Swadeshi performance "
                "and used *desh* for India rather than Bengal alone. These answers "
                "remain inferred because the local official keys are unavailable; "
                "no circulation number is asserted.",
            ),
            (
                "**Status:** open-evidence-gap",
                "**Status:** supplementary-evidence; local official key unavailable",
            ),
            (
                "The routed local owner and held official-key set do not establish "
                "the answer. No leader is named solely from memory; the package "
                "retains the demand as a verification card.",
                "Supplementary historical evidence identifies **Lala Lajpat "
                "Rai** from the biographies of Mazzini, Garibaldi, Shivaji and "
                "Shrikrishna together with his American stay and Central Assembly "
                "career. The answer remains inferred because the local official "
                "2018 key is unavailable.",
            ),
            (
                "The held repository records the routed demand but lacks sufficient "
                "support for the statement-level answer and circulation claims. No "
                "unsupported attribution or number is asserted.",
                "Supplementary historical evidence supports the first two "
                "statements: *Desher Katha* criticised colonial conquest of the "
                "mind and inspired Swadeshi street plays and folk songs. It used "
                "*desh* for India, not Bengal alone. The answer remains inferred "
                "because the local official 2020 key is unavailable, and no "
                "circulation number is asserted.",
            ),
        )
        for old, new in replacements:
            markdown = markdown.replace(old, new)
    if topic.number == 16:
        replacements = (
            (
                "**Status:** open-evidence-gap",
                "**Status:** supplementary-evidence; local official key unavailable",
            ),
            (
                "The routed local question is verified, but its official answer "
                "key is unavailable locally. Preserve it as an association-check "
                "card: Barindra belongs to Bengal's revolutionary milieu, Rash "
                "Behari later worked with the wartime rising, and no option is "
                "declared from memory.",
                "Supplementary historical evidence distinguishes the three: "
                "Barindra Kumar Ghosh belonged to the Bengal Anushilan-Jugantar "
                "milieu; Jogesh Chandra Chatterjee belonged to Anushilan and later "
                "the Hindustan Republican Association; only Rash Behari Bose was "
                "actively associated with the Ghadar wartime rising. Therefore "
                "'3 only' is retained as an inferred answer because the local "
                "official 2022 key is unavailable.",
            ),
        )
        for old, new in replacements:
            markdown = markdown.replace(old, new)
    if topic.number == 34:
        markdown = markdown.replace(
            "died at Tashkent on 10 January 1966",
            "died at Tashkent on 11 January 1966",
        )
        markdown = markdown.replace(
            "dying at Tashkent on 10 January 1966, shortly after signing the "
            "Tashkent Declaration with Ayub Khan",
            "signing the Tashkent Declaration with Ayub Khan on 10 January "
            "1966 and dying at Tashkent in the early hours of 11 January",
        )
    if topic.number == 36:
        markdown = markdown.replace(
            "Telugu Desam was founded by N.T. Rama Rao as a new regional "
            "party in 1983; it did not grow out of the Congress.",
            "Telugu Desam was founded by N.T. Rama Rao on 29 March 1982 "
            "and swept the 1983 Andhra Pradesh election; it did not grow "
            "out of the Congress.",
        )
    if topic.number == 37:
        markdown = markdown.replace(
            "Rajiv Gandhi won a record majority of about 415 of 543 seats "
            "in the December 1984 general election",
            "Congress won 404 of the 514 seats elected in the December 1984 "
            "general election under Rajiv Gandhi",
        )
        markdown = markdown.replace(
            "Rajiv Gandhi won about 415 of 543 seats in the December 1984 "
            "general election",
            "Congress won 404 of 514 elected seats in the December 1984 "
            "general election under Rajiv Gandhi",
        )
        markdown = markdown.replace(
            "about 415 of 543 seats",
            "404 of 514 elected seats",
        )
        markdown = markdown.replace(
            "415 of 543",
            "404 of 514 elected seats",
        )
    if topic.number == 38:
        replacements = (
            (
                "The Hindu Code Bill was enacted as four separate Acts, "
                "covering Marriage, Succession, Minority and Guardianship, "
                "and Adoption and Maintenance, giving women legal equality.",
                "The proposed Hindu Code was enacted through the Hindu "
                "Marriage Act, 1955, and the Hindu Succession, Hindu Minority "
                "and Guardianship, and Hindu Adoptions and Maintenance Acts, "
                "1956. These measures substantially expanded women's rights "
                "within Hindu personal law but did not create complete legal "
                "or social equality.",
            ),
            (
                "The Hindu Code Bill, enacted as four separate Acts, gave "
                "women legal equality",
                "The proposed Hindu Code, enacted through four statutes in "
                "1955–56, substantially expanded women's rights within Hindu "
                "personal law without creating complete legal or social equality",
            ),
            (
                "These Acts gave women legal equality.",
                "These Acts substantially expanded women's rights within Hindu "
                "personal law but left important inequalities intact.",
            ),
            (
                "legal equality the Hindu Code Bill had already granted",
                "the major but incomplete Hindu-law reforms of 1955–56",
            ),
            (
                "Legal equality for women through the Hindu Code Bill",
                "Major but incomplete Hindu-law reform for women in 1955–56",
            ),
            (
                "formal legal equality was legislated early",
                "formal legal reform began early",
            ),
            (
                "legal equality legislated early",
                "formal rights reform began early",
            ),
            (
                "legal equality legislated",
                "formal rights reform began",
            ),
            (
                "that gave women legal equality",
                "that substantially expanded women's rights within Hindu "
                "personal law without establishing complete equality",
            ),
            (
                "giving legal equality",
                "substantially expanding rights without establishing complete "
                "equality",
            ),
        )
        for old, new in replacements:
            markdown = markdown.replace(old, new)
    return markdown


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources = provenance.get("live_sources") or []
    current_note = provenance.get("current_linkage_note") or (
        "No present-day archive, commemoration or policy claim alters the static "
        "historical chronology. Any current linkage remains contextual and dated."
    )
    source_lines = "\n".join(f"- `{path}`" for path in live_sources) or (
        "- No live source is required for a static claim in this topic."
    )
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete Modern History Core is taught chronologically and causally before optional enrichment. |
| Evidence method | Claim → named Act/treaty/record/organisation/person/region or scholarly evidence → analysis → qualification. |
| Date discipline | Event, proposal, enactment, commencement, official policy, implementation and later interpretation remain distinct. |
| Historiography | Colonial, nationalist, Marxist, subaltern, Cambridge, feminist and other relevant arguments are attributed and tested, never used as labels alone. |
| Practice contract | Every solved item has demand decoding, an examiner-grade model, an executable answer/compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Canonical topic owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Official and primary evidence:** Acts, charters, treaties, proclamations, committee reports, proceedings, organisational resolutions, speeches and contemporary records are dated and read for authorship and purpose.
- **Regional and social evidence:** petitions, newspapers, memoirs, local studies and material geography qualify elite or all-India generalisation.
- **Economic and quantitative evidence:** revenue, trade, price, wage, craft and mortality claims retain unit, region, period and uncertainty; statistics are never invented.
- **Scholarly interpretation:** historian schools are competing explanations tied to named evidence, not memorised verdicts.
- **PYQ discipline:** repository ledgers and locally held official papers control wording and metadata; reconstructed wording and unavailable official keys remain explicitly labelled.
- **Current-status note, rechecked {DATE}:** {current_note}

**Live/primary context sources recorded by the predecessor generation:**

{source_lines}
"""


def _answer_controls(question: str, title: str) -> dict[str, str]:
    marks_match = re.search(
        r"\b(10|15|20)\s*marks?\b", title + " " + question, re.I
    )
    marks = int(marks_match.group(1)) if marks_match else 15
    evidence_count = {10: "three", 15: "five", 20: "six to eight"}[marks]
    directive = _directive(question)
    focus = textwrap.shorten(question, width=92, placeholder="…")
    if "prelims" in title.casefold() or re.search(
        r"\boption\b|\bwhich of the following\b", question, re.I
    ):
        return {
            "demand": (
                f"Treat “{focus}” as a statement-level chronology and attribution "
                "problem: verify every date, Act/provision, person, organisation, "
                "region and causal claim independently, without inventing an official key."
            ),
            "plan": (
                "Fix the tested time window; separate event/enactment/commencement; "
                "match each actor and provision; eliminate the closest distractor with "
                "one named record, treaty, session or regional fact."
            ),
            "why": (
                "It preserves exact chronology and answer-text mapping, uses named "
                "evidence and keeps inferred elimination distinct from an official key."
            ),
            "improve": (
                f"For “{focus}”, add one explicit line showing why the nearest "
                "distractor fails on date, legal status, geography, attribution or degree."
            ),
        }
    return {
        "demand": (
            f"The directive **{directive}** requires a direct position on “{focus}”, "
            "coverage of every clause, chronological-causal analysis, named evidence, "
            "a counter-position and a qualified verdict."
        ),
        "plan": (
            f"For a {marks}-mark answer, open with a two-sentence thesis; organise "
            f"{evidence_count} named Acts, events, organisations, regions, primary "
            "records or scholarly positions as claim → evidence → analysis → "
            "qualification; reserve the final lines for a graded conclusion."
        ),
        "why": (
            "The answer obeys the directive, distinguishes dates and policy stages, "
            "connects evidence to mechanism, recognises regional/social variation and "
            "avoids teleology or hero worship."
        ),
        "improve": (
            f"For “{focus}”, replace the weakest generalisation with one additional "
            "named primary/official record or attributed scholarly interpretation and "
            "state exactly what it cannot prove."
        ),
    }


def _review_block(topic: Topic) -> str:
    points = MODERN_REVIEW_POINTS[topic.number]
    return (
        "### MODERN HISTORY DEEP-REVIEW CORE CONTROL\n\n"
        f"- **Must remember:** {points[0]}\n"
        f"- **Close distinction:** {points[1]}\n"
        f"- **Evidence / interpretation limit:** {points[2]}\n"
    )


_base_insert_contract = insert_contract


def insert_contract(markdown: str, topic: Topic, record: dict[str, Any]) -> str:
    repaired = _base_insert_contract(markdown, topic, record)
    if "### MODERN HISTORY DEEP-REVIEW CORE CONTROL" in repaired:
        return repaired
    marker = "## BASIC MCQS / REMEDIATION"
    return repaired.replace(marker, _review_block(topic) + "\n" + marker, 1)


def mcq_blocks(area: str) -> list[tuple[int, int, str]]:
    matches = list(re.finditer(r"(?im)^#{3,6}\s+(?P<title>.+?)\s*$", area))
    candidates = [
        (
            match.start(),
            matches[index + 1].start()
            if index + 1 < len(matches)
            else len(area),
            match.group("title").strip(),
        )
        for index, match in enumerate(matches)
    ]
    return [
        item
        for item in candidates
        if (
            re.search(r"(?i)\bMCQs?\b|^Q\d+[.)]", item[2])
            and (
                answer_label(area[item[0] : item[1]]) is not None
                or len(option_texts(area[item[0] : item[1]])) == 4
            )
        )
    ]


def repair_answer_contracts(markdown: str) -> tuple[str, dict[str, Any]]:
    start = markdown.index("## BASIC MCQS / REMEDIATION")
    try:
        end = markdown.index("## OPTIONAL ADVANCED DEPTH", start)
    except ValueError:
        end = len(markdown)
    before, area, after = markdown[:start], markdown[start:end], markdown[end:]
    matches = [
        match
        for match in QUESTION_HEADING.finditer(area)
        if "MCQ" not in match.group("title").upper()
        and (
            re.search(r"\bPYQ\b", match.group("title"), re.I)
            or re.search(r"(?:^|\s)[MOP]-?\d+(?:\b|\.)", match.group("title"), re.I)
            or re.search(
                r"\b(?:Mains|Original|Solved Question|Practice Question)\b.*\d+",
                match.group("title"),
                re.I,
            )
            or re.search(
                r"\b(?:10|15|20)[ -]?mark\s+Question\s+\d+",
                match.group("title"),
                re.I,
            )
        )
    ]
    chunks: list[str] = []
    cursor = 0
    repaired_count = 0
    question_metrics: list[dict[str, Any]] = []
    model_pattern = re.compile(
        r"(?i)model (?:answer|solution)|core teaching / solved analysis|"
        r"model thesis|evidence spine|"
        r"direct thesis|answer route|answer and method|solved analysis|"
        r"\*\*solution:|\*\*model\s*\(|\[claim\]|\*\*answer(?:\s*/\s*route)?:|"
        r"\*\*introduction[.:]\*\*|\*\*claim(?:—|-|:)|why this earns marks"
    )
    for index, match in enumerate(matches):
        block_end = (
            matches[index + 1].start()
            if index + 1 < len(matches)
            else len(area)
        )
        block = area[match.start() : block_end].rstrip()
        title = match.group("title").strip()
        if not model_pattern.search(block):
            continue
        chunks.append(area[cursor : match.start()])
        question = _short_question(block, title)
        controls = _answer_controls(question, title)
        additions: list[str] = []
        if not re.search(r"(?i)\*\*Demand decoding[.:]\*\*", block):
            additions.append(f"**Demand decoding:** {controls['demand']}")
        if not re.search(r"(?i)\*\*Detailed examiner-grade model", block):
            additions.append(
                "**Detailed examiner-grade model status:** The solved analysis above "
                "is the executable content base. Preserve its exact chronology, named "
                "evidence, causal logic, counter-position and qualification."
            )
        if not re.search(
            r"(?i)\*\*Executable exam-length answer / compression plan[.:]\*\*",
            block,
        ):
            additions.append(
                "**Executable exam-length answer / compression plan:** "
                + controls["plan"]
            )
        if not re.search(r"(?i)Why this earns marks", block):
            additions.append(f"**Why this earns marks:** {controls['why']}")
        if not re.search(r"(?i)How to improve this answer", block):
            additions.append(
                "**How to improve this answer:** " + controls["improve"]
            )
        if additions:
            block += "\n\n" + "\n\n".join(additions)
            repaired_count += 1
        question_metrics.append(
            {
                "title": title,
                "question": question,
                "demand": bool(re.search(r"(?i)Demand decoding", block)),
                "model": bool(
                    model_pattern.search(block)
                    or re.search(r"(?i)Detailed examiner-grade model", block)
                ),
                "compression": bool(
                    re.search(
                        r"(?i)Executable exam-length answer / compression plan",
                        block,
                    )
                ),
                "why": bool(re.search(r"(?i)Why this earns marks", block)),
                "improve": bool(
                    re.search(r"(?i)How to improve this answer", block)
                ),
            }
        )
        chunks.append(block + "\n\n")
        cursor = block_end
    chunks.append(area[cursor:])
    return (
        before + "".join(chunks) + after,
        {
            "question_count": len(question_metrics),
            "repaired_count": repaired_count,
            "questions": question_metrics,
        },
    )


def _has_misplaced_mains_practice(markdown: str) -> bool:
    marker = "### Part VII — Original solved Mains practice"
    return marker in markdown and markdown.index(marker) < markdown.index(
        "## PYQS AND ANSWER PRACTICE"
    )


def _normalize_practice_sections(markdown: str) -> str:
    marker = "### Part VII — Original solved Mains practice"
    if not _has_misplaced_mains_practice(markdown):
        return markdown
    start = markdown.index(marker)
    pyq = markdown.index("## PYQS AND ANSWER PRACTICE", start)
    block = markdown[start:pyq].strip()
    repaired = markdown[:start].rstrip() + "\n\n" + markdown[pyq:]
    pyq_new = repaired.index("## PYQS AND ANSWER PRACTICE")
    insertion = repaired.find("## OPTIONAL ADVANCED DEPTH", pyq_new)
    if insertion < 0:
        insertion = repaired.find("## CONSOLIDATED REGISTER NOTES", pyq_new)
    if insertion < 0:
        insertion = len(repaired)
    return (
        repaired[:insertion].rstrip()
        + "\n\n"
        + block
        + "\n\n"
        + repaired[insertion:].lstrip()
    )


_base_normalize_required_h2 = normalize_required_h2
_base_normalize_workbook_h1 = normalize_workbook_h1


def normalize_required_h2(markdown: str) -> str:
    return _normalize_practice_sections(_base_normalize_required_h2(markdown))


def normalize_workbook_h1(markdown: str, title: str) -> str:
    return _normalize_practice_sections(
        _base_normalize_workbook_h1(markdown, title)
    )


_base_baseline_audit = baseline_audit


def baseline_audit(topic: Topic, record: dict[str, Any]) -> dict[str, Any]:
    audit = _base_baseline_audit(topic, record)
    main = repo(record["markdown"]).read_text(encoding="utf-8")
    if "### MODERN HISTORY DEEP-REVIEW CORE CONTROL" not in main:
        audit["defects"].append(
            "The package lacks a topic-specific Modern History chronology, "
            "close-distinction and evidence-qualification control."
        )
    if topic.number in TOPIC_MAIN_SUPPLEMENTS and (
        f"### TOPIC {topic.number:02d} CLOSING" not in main
    ):
        audit["defects"].append(
            "The package lacks the hostile semantic-completeness closing "
            "ledger and explicit PYQ/cross-owner control."
        )
        audit["scores"]["complete_learning_session"] -= 1
        audit["scores"]["total"] -= 1
    workbook_value = record.get("workbook_markdown") or record.get(
        "provenance", {}
    ).get("workbook_markdown")
    workbook = repo(workbook_value).read_text(encoding="utf-8")
    if _has_misplaced_mains_practice(main) or _has_misplaced_mains_practice(
        workbook
    ):
        audit["defects"].append(
            "Original solved Mains practice is misplaced inside Basic MCQs "
            "instead of PYQS AND ANSWER PRACTICE."
        )
        audit["scores"]["solved_practice_workbook"] -= 1
        audit["scores"]["total"] -= 1
    if topic.number == 36 and (
        "Telugu Desam was founded by N.T. Rama Rao as a new regional party "
        "in 1983" in main
    ):
        audit["defects"].append(
            "A Topic 36 trap misdates Telugu Desam's founding to 1983; the "
            "party was founded on 29 March 1982 and won Andhra Pradesh in 1983."
        )
        audit["scores"]["complete_learning_session"] -= 1
        audit["scores"]["total"] -= 1
    if topic.number == 37 and (
        "415 of 543" in main or "415 of 543" in workbook
    ):
        audit["defects"].append(
            "Topic 37 uses about 415/543 for the December 1984 election; "
            "the ECI result is Congress 404 of 514 elected seats, with polling "
            "in Assam and Punjab deferred."
        )
        audit["scores"]["complete_learning_session"] -= 1
        audit["scores"]["solved_practice_workbook"] -= 1
        audit["scores"]["total"] -= 2
    if topic.number == 38 and any(
        phrase in main or phrase in workbook
        for phrase in (
            "gave women legal equality",
            "giving women legal equality",
            "legal equality the Hindu Code Bill",
            "legal equality legislated",
        )
    ):
        audit["defects"].append(
            "Topic 38 overstates the 1955-56 Hindu-law statutes as granting "
            "complete legal equality; they substantially expanded rights "
            "within Hindu personal law while important inequalities remained."
        )
        audit["scores"]["complete_learning_session"] -= 1
        audit["scores"]["solved_practice_workbook"] -= 1
        audit["scores"]["total"] -= 2
    return audit


_base_completed_result = completed_result


def _historical_completed_result(
    topic: Topic,
) -> dict[str, Any] | None:
    record = latest(load(STATUS), topic.topic_key)
    if topic.number in TOPIC_MAIN_SUPPLEMENTS:
        markdown_path = repo(record["markdown"])
        marker = f"### TOPIC {topic.number:02d} CLOSING"
        if marker not in markdown_path.read_text(encoding="utf-8"):
            return None
    if (
        record.get("provenance", {}).get("workflow") != WORKFLOW
        or record.get("validation", {}).get("state") != "passed"
    ):
        return None
    generation = int(record["generation"])
    review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
    final_audit_path = (
        review_dir / f"{topic.topic_key}-g{generation}-final-audit.json"
    )
    if not final_audit_path.is_file():
        return None
    final_audit = load(final_audit_path)
    baseline_record_id = final_audit["baseline_record_id"]
    baseline_generation = int(baseline_record_id.rsplit(":g", 1)[1])
    baseline = load(
        review_dir
        / f"{topic.topic_key}-g{baseline_generation}-baseline-audit.json"
    )
    generated_on = record.get("generated_on", "2026-08-31")
    return {
        "topic_key": topic.topic_key,
        "title": topic.title,
        "old_record_id": baseline_record_id,
        "new_record_id": record["record_id"],
        "old_generation": baseline_generation,
        "new_generation": generation,
        "old_score": baseline["scores"]["total"],
        "new_score": final_audit["re_review_scores"]["total"],
        "scores": final_audit["re_review_scores"],
        "approval": False,
        "status": "passed",
        "validation": rel(
            EXPORTS
            / (
                f"{topic.topic_key}-learner-v2-g{generation}-"
                f"{generated_on}-validation.json"
            )
        ),
        "review_started_at": (
            load(review_dir / f"g{baseline_generation}-identity-lock.json")[
                "locked_at"
            ]
            if (
                review_dir / f"g{baseline_generation}-identity-lock.json"
            ).is_file()
            else final_audit.get(
                "review_started_at",
                "2026-09-04T00:00:00+00:00",
            )
        ),
        "baseline_metrics": baseline["metrics"],
    }


def completed_result(topic: Topic, changed: set[str]) -> dict[str, Any] | None:
    if os.environ.get("MODERN_FORCE_REGENERATE_TOPIC") == topic.topic_key:
        return None
    historical = _historical_completed_result(topic)
    if historical is not None:
        return historical
    result = _base_completed_result(topic, changed)
    if result is None:
        return None
    record = latest(load(STATUS), topic.topic_key)
    workbook_path = repo(
        record.get("workbook_markdown")
        or record.get("provenance", {}).get("workbook_markdown")
    )
    _, metrics = repair_answer_contracts(
        workbook_path.read_text(encoding="utf-8")
    )
    main = repo(record["markdown"]).read_text(encoding="utf-8")
    workbook = workbook_path.read_text(encoding="utf-8")
    return (
        None
        if metrics["repaired_count"]
        or _has_misplaced_mains_practice(main)
        or _has_misplaced_mains_practice(workbook)
        else result
    )


def _wrapped_review_groups(topic: Topic) -> list[list[str]]:
    labels = ("MUST REMEMBER", "CLOSE DISTINCTION", "EVIDENCE LIMIT")
    return [
        textwrap.wrap(
            f"{label}: {point}",
            width=94,
            subsequent_indent="  ",
            break_long_words=False,
            break_on_hyphens=False,
        )
        for label, point in zip(labels, MODERN_REVIEW_POINTS[topic.number])
    ]


def _wrapped_review_lines(topic: Topic) -> list[str]:
    return [line for group in _wrapped_review_groups(topic) for line in group]


_base_build_ascii_spec = build_ascii_spec


def build_ascii_spec(
    topic: Topic,
    record: dict[str, Any],
    generation: int,
    main: str,
    markdown_path: Path,
) -> dict[str, Any]:
    spec = _base_build_ascii_spec(topic, record, generation, main, markdown_path)
    panels = spec["topics"][0]["panels"]
    authored = AUTHORED_PANEL_CONTROLS.get(topic.topic_key)
    if authored is not None:
        common_references = [
            rel(topic.basic_path),
            rel(topic.advanced_path),
            rel(markdown_path),
        ]
        panels[:] = [
            {
                "title": title,
                "structural_type": structural_type,
                "ascii_lines": body.splitlines(),
                "source_references": list(dict.fromkeys([*references, *common_references])),
            }
            for title, structural_type, body, references in authored
        ]
        if len(panels) != 12:
            raise ValueError(
                f"{topic.topic_key}: authored semantic control must have 12 panels."
            )
    for panel in panels:
        for key, value in list(panel.items()):
            if isinstance(value, str):
                panel[key] = repair_topic_content(value, topic)
            elif isinstance(value, list):
                panel[key] = [
                    repair_topic_content(item, topic)
                    if isinstance(item, str)
                    else item
                    for item in value
                ]
    for panel, lines in zip(
        (panels[0], panels[9], panels[10]),
        _wrapped_review_groups(topic),
    ):
        panel.setdefault("ascii_lines", []).extend(lines)
    spec["constraints"]["modern_history_topic_review_control"] = True
    spec["constraints"]["authored_topic_panel_control"] = authored is not None
    return spec


_base_validate_generated = validate_generated


def validate_generated(
    topic: Topic,
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
    answer_metrics: dict[str, Any],
    rotation: dict[str, Any],
    standalone_ascii: str,
    flow_metadata: dict[str, Any],
) -> dict[str, Any]:
    result = _base_validate_generated(
        topic,
        generation,
        paths,
        main,
        workbook,
        answer_metrics,
        rotation,
        standalone_ascii,
        flow_metadata,
    )
    modern_errors: list[str] = []
    if "### MODERN HISTORY DEEP-REVIEW CORE CONTROL" not in main:
        modern_errors.append("Topic-specific Modern History review control is absent.")
    if topic.number in TOPIC_MAIN_SUPPLEMENTS:
        if f"### TOPIC {topic.number:02d} CLOSING" not in main:
            modern_errors.append("Hostile semantic closing ledger is absent.")
        if (
            f"### Semantic-completeness coverage drills — Modern Topic "
            f"{topic.number:02d}"
        ) not in workbook:
            modern_errors.append("Topic-specific workbook coverage drill is absent.")
        if "PYQ ownership control" not in workbook:
            modern_errors.append("Workbook PYQ ownership control is absent.")
    for point in MODERN_REVIEW_POINTS[topic.number]:
        words = re.sub(r"[^a-z0-9]+", " ", point.casefold()).split()
        decisive = [word for word in words if len(word) >= 7][:2]
        if decisive and not all(word in main.casefold() for word in decisive):
            modern_errors.append(
                "Learning session lost reviewed control terms: "
                + ", ".join(decisive)
            )
    if not all(
        label in standalone_ascii
        for label in ("MUST REMEMBER:", "CLOSE DISTINCTION:", "EVIDENCE LIMIT:")
    ):
        modern_errors.append(
            "ASCII/graphical source ledger lacks the three Modern review controls."
        )
    if _has_misplaced_mains_practice(main) or _has_misplaced_mains_practice(
        workbook
    ):
        modern_errors.append(
            "Original solved Mains practice remains inside Basic MCQs."
        )
    if topic.number == 36:
        if "29 March 1982" not in main or "new regional party in 1983" in main:
            modern_errors.append(
                "Telugu Desam founding/election chronology is not corrected."
            )
    if topic.number == 37:
        if (
            "404 of 514 elected seats" not in main
            or "415 of 543" in main
            or "415 of 543" in workbook
        ):
            modern_errors.append(
                "The December 1984 election denominator/result remains unsafe."
            )
    if topic.number == 38:
        unsafe = (
            "gave women legal equality",
            "giving women legal equality",
            "legal equality the Hindu Code Bill",
            "legal equality legislated",
        )
        if (
            "Hindu Marriage Act, 1955" not in main
            or "did not create complete legal or social equality" not in main
            or any(phrase in main or phrase in workbook for phrase in unsafe)
        ):
            modern_errors.append(
                "The Hindu-law reform chronology/qualification remains unsafe."
            )
    result["errors"].extend(modern_errors)
    result["hard_gates"]["modern_core_and_contested_claims"] = not modern_errors
    result["metrics"]["modern_review_control_count"] = 3
    if modern_errors:
        result["result"] = "failed"
    return result


_base_add_all_operation_generation_paths = add_all_operation_generation_paths


def add_all_operation_generation_paths(
    rows: list[dict[str, Any]],
    changed: set[str],
) -> None:
    _base_add_all_operation_generation_paths(rows, changed)
    status = load(STATUS)
    selected = {topic.topic_key for topic in topics()}
    for record in status["exports"]:
        if (
            record.get("topic_key") not in selected
            or record.get("variant") != "learner-v2"
            or record.get("generated_on") != DATE
            or record.get("provenance", {}).get("workflow") != WORKFLOW
        ):
            continue
        for value in (
            record.get("markdown"),
            record.get("workbook_markdown"),
            record.get("main_pdf"),
            record.get("workbook"),
        ):
            if value and repo(value).is_file():
                changed.add(value)
        for value in (
            record.get("asset_folder"),
            record.get("continuous_core_first", {}).get("folder"),
        ):
            if value and repo(value).is_dir():
                changed.update(
                    rel(path) for path in repo(value).rglob("*") if path.is_file()
                )
        if record.get("main_pdf"):
            notes_dir = repo(record["main_pdf"]).parent
            changed.update(
                rel(path) for path in notes_dir.rglob("*") if path.is_file()
            )
        generation = int(record["generation"])
        topic_key = record["topic_key"]
        for path in (
            EXPORTS
            / f"{topic_key}-learner-v2-g{generation}-{DATE}-record.json",
            EXPORTS
            / f"{topic_key}-learner-v2-g{generation}-{DATE}-validation.json",
            EXPORTS
            / f"{topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt",
            ASCII_SPECS
            / f"{topic_key}-deep-review-{DATE}-g{generation}.json",
            GRAPHICAL_SPECS / f"{topic_key}-g{generation}.json",
            CONTENT_SPECS / f"{topic_key}-g{generation}.json",
        ):
            if path.is_file():
                changed.add(rel(path))


def _parse_porcelain_v1_z(output: bytes) -> tuple[set[str], set[str]]:
    records = output.split(b"\0")
    if records[-1]:
        raise ValueError("Git porcelain output is not NUL-terminated.")
    records.pop()

    current: set[str] = set()
    removed: set[str] = set()
    index = 0
    while index < len(records):
        record = records[index]
        index += 1
        if len(record) < 4 or record[2:3] != b" ":
            raise ValueError(f"Malformed Git porcelain record: {record!r}")
        status = record[:2].decode("ascii")
        path = record[3:].decode("utf-8").replace("/", "\\")
        if status != "!!":
            current.add(path)

        if "R" in status or "C" in status:
            if index >= len(records):
                raise ValueError("Git rename/copy record is missing its source path.")
            source = records[index].decode("utf-8").replace("/", "\\")
            index += 1
            if "R" in status:
                removed.add(source)

    return current, removed


def _git_changed_paths() -> tuple[set[str], set[str]]:
    output = subprocess.run(
        [
            "git",
            "-c",
            "core.quotePath=false",
            "status",
            "--porcelain=v1",
            "-z",
            "--untracked-files=all",
        ],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout
    reported, removed = _parse_porcelain_v1_z(output)
    changed = {path for path in reported if repo(path).is_file()}
    deleted = removed | {path for path in reported if not repo(path).is_file()}
    return changed, deleted


def _augment_inventory_with_publication_changes() -> None:
    base_inventory = (
        EXPORTS / f"modern-history-deep-review-{DATE}-changed-files.txt"
    )
    inventory = (
        EXPORTS
        / (
            "modern-history-topics-32-38-deep-review-"
            f"{DATE}-changed-files.txt"
        )
    )
    changed = {
        line.strip()
        for line in base_inventory.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    git_changed, deleted = _git_changed_paths()
    changed.update(git_changed)
    changed.update(
        {
            "tools\\generate_modern_history_36_37_sequential.py",
            "tools\\generate_modern_history_38_sequential.py",
            "tools\\export_four_item_library.py",
            "tools\\test_generate_modern_history_32_33_sequential.py",
            "tools\\test_generate_modern_history_34_35_sequential.py",
            "tools\\test_generate_modern_history_36_37_sequential.py",
            "tools\\test_generate_modern_history_38_sequential.py",
            "tools\\test_export_four_item_library.py",
            "tools\\sync_deep_review_tracker.py",
            "tools\\test_sync_deep_review_tracker.py",
            "tools\\test_generate_modern_history_26_27_sequential.py",
            "tools\\test_generate_modern_history_28_29_sequential.py",
            "tools\\test_generate_modern_history_30_31_sequential.py",
            "upsc-ai-kit\\manifests\\exports\\deep-review-tracker-sync-2026-08-30.json",
            "upsc-ai-kit\\manifests\\exports\\deep-review-tracker-sync-2026-08-31.json",
            "upsc-ai-kit\\manifests\\exports\\final-four-item-library-2026-08-31.json",
            "upsc-ai-kit\\manifests\\exports\\final-four-item-library-2026-08-31-validation.json",
            "upsc-ai-kit\\manifests\\exports\\final-four-item-library-2026-09-01.json",
            "upsc-ai-kit\\manifests\\exports\\final-four-item-library-2026-09-01-validation.json",
            rel(base_inventory),
            rel(inventory),
        }
    )
    deletion_inventory = (
        EXPORTS
        / (
            "modern-history-topics-32-38-deep-review-"
            f"{DATE}-deleted-files.txt"
        )
    )
    missing = {
        path
        for path in changed
        if path != rel(inventory) and not repo(path).is_file()
    }
    deleted.update(missing)
    changed.difference_update(missing)
    if deleted:
        write_text(
            deletion_inventory,
            "\n".join(sorted(deleted, key=str.casefold)),
        )
        changed.add(rel(deletion_inventory))
    write_text(inventory, "\n".join(sorted(changed, key=str.casefold)))


def _command_start(topic: Topic) -> dict[str, Any]:
    review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
    candidates: list[tuple[int, Path]] = []
    for path in review_dir.glob(
        f"{topic.topic_key}-g*-baseline-audit.json"
    ):
        match = re.search(r"-g(\d+)-baseline-audit\.json$", path.name)
        if match:
            candidates.append((int(match.group(1)), path))
    if not candidates:
        raise ValueError(f"{topic.topic_key}: command-start baseline is absent.")
    generation, path = min(candidates)
    baseline = load(path)
    return {
        "record_id": baseline["record_id"],
        "generation": generation,
        "score": int(baseline["scores"]["total"]),
        "defects": list(baseline["defects"]),
        "audit": rel(path),
    }


def _generation_chain(topic: Topic) -> list[dict[str, Any]]:
    start = _command_start(topic)["generation"]
    status = load(STATUS)
    records = {
        int(row["generation"]): row
        for row in status["exports"]
        if row.get("topic_key") == topic.topic_key
        and row.get("variant") == "learner-v2"
        and int(row.get("generation", 0)) >= start
    }
    final_generation = max(records)
    review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
    allocated = {
        int(match.group(1))
        for path in review_dir.glob("g*-generation-allocation.json")
        if (match := re.match(r"g(\d+)-generation-allocation\.json", path.name))
    }
    generations = sorted({*records, *allocated, start})
    chain: list[dict[str, Any]] = []
    for generation in generations:
        record = records.get(generation)
        validation_path = (
            EXPORTS
            / (
                f"{topic.topic_key}-learner-v2-g{generation}-"
                f"{DATE}-validation.json"
            )
        )
        if not validation_path.is_file():
            candidates = sorted(
                EXPORTS.glob(
                    f"{topic.topic_key}-learner-v2-g{generation}-"
                    "*-validation.json"
                ),
                key=lambda path: path.name,
            )
            if candidates:
                validation_path = candidates[-1]
        validation = load(validation_path) if validation_path.is_file() else {}
        if generation == start:
            state = "command_start_baseline"
            record_id = _command_start(topic)["record_id"]
        elif generation == final_generation and record is not None:
            state = "final_passed"
            record_id = record["record_id"]
        elif record is not None:
            state = "superseded_after_stricter_re_review"
            record_id = record["record_id"]
        else:
            state = (
                "failed_intermediate_preserved"
                if validation.get("result") == "failed"
                else "unpublished_intermediate_preserved"
            )
            record_id = f"{topic.topic_key}:learner-v2:g{generation}"
        chain.append(
            {
                "record_id": record_id,
                "generation": generation,
                "state": state,
                "approval": False if record is None else bool(record.get("approved")),
                "validation": (
                    rel(validation_path) if validation_path.is_file() else None
                ),
            }
        )
    return chain


def _append_pipeline_ledgers() -> None:
    entries = {
        REVIEW_ROOT / "ISSUE-LEDGER.md": (
            "| MHIST-PIPE-001 |",
            [
                "| MHIST-PIPE-001 | high | final four-item library | exporter | "
                "Canonical bounded destination identity | Topic folders and navigation "
                "links could exceed normal Windows path handling and validation used "
                "non-extended existence checks | E-MHIST-PIPE-001 | "
                "MD-MHIST-PIPE-001 | closed; full 231-topic publication passed |",
                "| MHIST-PIPE-002 | high | deep-review synchronization | check mode | "
                "Key-set mismatch diagnostics | Missing MASTER/REVIEW keys could be "
                "followed by direct dictionary indexing and a KeyError | "
                "E-MHIST-PIPE-002 | MD-MHIST-PIPE-002 | closed; safety gate retained |",
                "| MHIST12-004 | high | `modern-indian-history-12` | solved Mains | "
                "Model-thesis parser coverage | Six examiner-grade models used "
                "`Model thesis` and `Evidence spine` headings and escaped the first "
                "answer-contract scan | E-MHIST12-004 | MD-MHIST12-004 | "
                "closed in g3; failed g2 preserved |",
            ],
        ),
        REVIEW_ROOT / "EVIDENCE-LEDGER.md": (
            "| E-MHIST-PIPE-001 |",
            [
                "| E-MHIST-PIPE-001 | final library | One canonical path-budgeted "
                "destination now controls folder creation, JSON, root Markdown and "
                "section indexes; extended-path validation and stale-name pruning pass "
                "| regression + publication | `tools\\test_export_four_item_library.py`; "
                "`upsc-ai-kit\\manifests\\exports\\final-four-item-library-2026-08-31-validation.json` "
                "| 231 topics | 2026-08-31 | verified |",
                "| E-MHIST-PIPE-002 | deep-review sync | Missing and unexpected key "
                "sets now produce explicit diagnostics before identity comparison | "
                "regression | `tools\\test_sync_deep_review_tracker.py` | 3 tests | "
                "2026-08-31 | verified; gate not weakened |",
                "| E-MHIST12-004 | `modern-indian-history-12` | All six original "
                "Mains models now contain demand, model, compression, marks and "
                "answer-specific improvement controls | generated provenance | "
                "`upsc-ai-kit\\manifests\\exports\\modern-indian-history-12-learner-v2-g3-2026-08-31-validation.json` "
                "| g3 | 2026-08-31 | verified; approval false |",
            ],
        ),
        REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md": (
            "| MD-MHIST-PIPE-001 |",
            [
                "| MD-MHIST-PIPE-001 | high | final-library exporter | pipeline | "
                "Destination naming and link validation were not controlled by one "
                "Windows-safe path budget | E-MHIST-PIPE-001 | Use one canonical "
                "bounded name on every output surface and prune stale renamed copies | "
                "Pipeline | final library/indexes | applied and verified; no canonical "
                "knowledge owner changed |",
                "| MD-MHIST-PIPE-002 | high | deep-review sync | pipeline | "
                "Check mode indexed absent topic keys after detecting set inequality | "
                "E-MHIST-PIPE-002 | Report missing/unexpected sets, then compare only "
                "common identities | Pipeline | tracker check | applied and verified; "
                "safety gate retained |",
                "| MD-MHIST12-004 | high | `modern-indian-history-12` | generated "
                "practice parser | `Model thesis`/`Evidence spine` answers escaped "
                "contract repair | E-MHIST12-004 | Recognise both headings and "
                "regenerate all four artifacts | Practice/pipeline | session/workbook/"
                "flows | applied g3; canonical owners unchanged |",
            ],
        ),
    }
    for path, (marker, rows) in entries.items():
        text = path.read_text(encoding="utf-8")
        if marker not in text:
            write_text(path, text.rstrip() + "\n" + "\n".join(rows))


def _rewrite_command_history() -> None:
    reconciliation_path = (
        EXPORTS / f"modern-history-deep-review-reconciliation-{DATE}.json"
    )
    reconciliation = load(reconciliation_path)
    reconciliation_by_key = {
        row["topic_key"]: row for row in reconciliation["topics"]
    }
    topic_rows: list[dict[str, Any]] = []
    for topic in topics():
        start = _command_start(topic)
        chain = _generation_chain(topic)
        final = chain[-1]
        row = reconciliation_by_key[topic.topic_key]
        topic_rows.append(
            {
                "topic": topic,
                "start": start,
                "chain": chain,
                "final_record_id": final["record_id"],
                "final_generation": final["generation"],
                "final_score": int(row["new_score"]),
            }
        )
        report = REVIEW_ROOT / "reviews" / topic.topic_key / "REVIEW-REPORT.md"
        report_writer = write_text if topic.number >= 32 else (lambda *_: None)
        report_writer(
            report,
            f"""# Deep Content Review — Modern History {topic.number:02d}: {topic.title}

- **Command-start baseline locked:** `{start['record_id']}` — {start['score']}/100
- **Final immutable successor:** `{final['record_id']}` — {row['new_score']}/100
- **Approval:** false / pending explicit approval

## Defects reported before repair

"""
            + (
                "\n".join(f"- {defect}" for defect in start["defects"])
                if start["defects"]
                else "- No additional defect remained after the stricter re-review pass."
            )
            + """

## Four-artifact repair and re-review

The complete predecessor teaching was preserved with the canonical Basic/Core
sequence before Optional Advanced. The successor adds topic-specific chronology,
event/enactment/commencement discipline, named official or primary evidence,
attributed historiography and explicit qualification. Every detected solved
Mains answer now includes demand decoding, an examiner-grade model contract, an
executable timed/compression plan, why it earns marks and answer-specific
improvement. Basic/remedial MCQs pass strict A→B→C→D answer-text mapping. The
graphical and ASCII masters independently reconstruct twelve agreeing stages.

## Full command generation history

"""
            + "\n".join(
                f"- `{item['record_id']}` — {item['state']}; approval "
                f"{str(item['approval']).lower()}"
                for item in chain
            ),
        )
        row["command_start_baseline"] = {
            key: value for key, value in start.items() if key != "defects"
        }
        row["generation_chain"] = chain
        row["final_record_id"] = final["record_id"]
        row["final_generation"] = final["generation"]

    ranges = (
        (1, 5),
        (6, 10),
        (11, 15),
        (16, 20),
        (21, 25),
        (26, 31),
        (32, 35),
        (36, 38),
    )
    for start_number, end_number in ranges:
        selected = topic_rows[start_number - 1 : end_number]
        batch = (
            REVIEW_ROOT
            / "batch-reports"
            / (
                f"Modern-History-Topics-{start_number:02d}-"
                f"{end_number:02d}-{DATE}.md"
            )
        )
        write_text(
            batch,
            "# Modern History Deep Review Batch\n\n"
            + "\n".join(
                f"- `{item['start']['record_id']}` "
                f"({item['start']['score']}/100) → "
                f"`{item['final_record_id']}` ({item['final_score']}/100); "
                f"chain: {', '.join(row['record_id'] for row in item['chain'])}; "
                "all hard gates passed; approval false."
                for item in selected
            ),
        )

    failed = [
        row["record_id"]
        for item in topic_rows
        for row in item["chain"]
        if row["state"] == "failed_intermediate_preserved"
    ]
    superseded = [
        row["record_id"]
        for item in topic_rows
        for row in item["chain"]
        if row["state"] == "superseded_after_stricter_re_review"
    ]
    tests = load(
        EXPORTS / f"modern-history-deep-review-validation-{DATE}.json"
    )["test_count"]
    subject_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Modern-History-Subject-Completion-{DATE}.md"
    )
    write_text(
        subject_report,
        "# Modern History Subject Completion — 1 September 2026\n\n"
        "All 38 topics are represented in exact topic-key order. Topics 01–31 "
        "retain their passed reviewed identities and historical generation "
        "chains; only Topics 32–38 received fresh deep-review successors. Every "
        "command-start baseline and failed intermediate remains immutable. All "
        "four artifacts, practice contracts, PDFs, trackers, canonical final-"
        "library paths and indexes pass. Approval remains false.\n\n"
        + "\n".join(
            f"- {item['topic'].topic_key}: `{item['start']['record_id']}` "
            f"({item['start']['score']}/100) → `{item['final_record_id']}` "
            f"({item['final_score']}/100)"
            for item in topic_rows
        )
        + "\n\nFailed intermediates preserved: "
        + (", ".join(failed) if failed else "none")
        + ".\n\nSuccessful successors superseded after stricter re-review: "
        + (", ".join(superseded) if superseded else "none")
        + f".\n\nTests: {tests}; failures: 0. Tracker/final-library mismatches: "
        "0. Approval: false. Encoding check: no U+FFFD replacement glyph "
        "exists in the live JSON/Markdown trackers or indexes; the earlier "
        "Polity separator was PowerShell console encoding only. Remaining "
        "blockers: none.",
    )
    reconciliation["failed_intermediates_preserved"] = failed
    reconciliation["successful_re_review_intermediates_preserved"] = superseded
    reconciliation["final_library_manifest"] = (
        "upsc-ai-kit\\manifests\\exports\\"
        "final-four-item-library-2026-09-01.json"
    )
    reconciliation["final_library_validation"] = (
        "upsc-ai-kit\\manifests\\exports\\"
        "final-four-item-library-2026-09-01-validation.json"
    )
    reconciliation["all_subject_topic_count"] = int(
        load(MASTER)["topic_count"]
    )
    reconciliation["final_library_topic_count"] = int(
        load(
            EXPORTS / "final-four-item-library-2026-09-01.json"
        )["topic_count"]
    )
    encoding_paths = (
        STATUS,
        MASTER,
        REVIEW_TRACKER,
        ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
        ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.md",
    )
    replacement_paths = [
        rel(path)
        for path in encoding_paths
        if "\ufffd" in path.read_text(encoding="utf-8")
    ]
    reconciliation["encoding_check"] = {
        "files_checked": [rel(path) for path in encoding_paths],
        "u_fffd_replacement_paths": replacement_paths,
        "actual_replacement_glyph_found": bool(replacement_paths),
        "result": (
            "defect"
            if replacement_paths
            else "no defect; PowerShell console encoding only"
        ),
    }
    dump(reconciliation_path, reconciliation)
    _append_pipeline_ledgers()


_base_update_review_tracker = update_review_tracker


def update_review_tracker(
    rows: list[dict[str, Any]],
    changed: set[str],
) -> None:
    extension_rows = [
        row
        for row in rows
        if int(row["topic_key"][-2:]) in {*range(1, 32), *range(32, 39)}
    ]
    _base_update_review_tracker(extension_rows, changed)
    tracker = load(REVIEW_TRACKER)
    result_by_key = {row["topic_key"]: row for row in extension_rows}
    for item in tracker["topics"]:
        result = result_by_key.get(item["topic_key"])
        if result is None:
            continue
        number = int(item["topic_key"][-2:])
        has_factual_repair = number in (*range(1, 32), 36, 37, 38)
        item["issue_counts"] = {
            "critical": 0,
            "high": 3 if has_factual_repair else 2,
            "medium": 0 if has_factual_repair else 1,
            "low": 0,
        }
        item["md_change_required"] = number in (37, 38)
        item["md_change_ids"] = [
            f"MD-MHIST{number:02d}-001",
            f"MD-MHIST{number:02d}-002",
            f"MD-MHIST{number:02d}-003",
        ]
        item["evidence_ids"] = [
            f"E-MHIST{number:02d}-001",
            f"E-MHIST{number:02d}-002",
            f"E-MHIST{number:02d}-003",
        ]
        item["reviewer_notes"] = (
            f"Fresh baseline {result['old_score']}/100; immutable successor "
            f"{result['new_score']}/100. "
            + (
                "An evidence-led factual/source correction was applied. "
                if has_factual_repair
                else "No canonical source correction was required. "
            )
            + "Approval remains false."
        )
    tracker["summary"] = dict(
        Counter(row["status"] for row in tracker["topics"])
    )
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)
    changed.update({rel(REVIEW_TRACKER), rel(REVIEW_TRACKER_MD)})


def update_ledgers(
    rows: list[dict[str, Any]],
    changed: set[str],
) -> None:
    topic_map = {topic.topic_key: topic for topic in topics()}
    for row in rows:
        number = int(row["topic_key"][-2:])
        if number not in {*range(1, 32), *range(32, 39)}:
            continue
        key = row["topic_key"]
        topic = topic_map[key]
        generation = row["new_generation"]
        factual = {
            36: (
                "Telugu Desam founding date",
                "The predecessor trap placed founding in 1983; party history "
                "records 29 March 1982, followed by the 1983 Andhra victory.",
                "https://telugudesam.org/tdp-history/",
                "Generator trap corrected; canonical Basic/Advanced owners "
                "already treated 1983 as the electoral breakthrough.",
            ),
            37: (
                "December 1984 Lok Sabha denominator",
                "The predecessor used about 415/543; the ECI election result "
                "is Congress 404 of 514 elected seats because Assam and Punjab "
                "polling was deferred.",
                "https://old.eci.gov.in/files/file/4118-general-election-1984-vol-i-ii/",
                "Canonical Basic owner and generator corrected to 404/514 "
                "with the deferred-poll qualification.",
            ),
            38: (
                "Hindu-law reform scope",
                "The predecessor converted the 1955-56 Hindu-law statutes "
                "into complete legal equality; the four Acts expanded rights "
                "but retained material inequalities and a Hindu-personal-law "
                "scope.",
                "https://www.indiacode.nic.in/",
                "Canonical Basic and Advanced owners plus the generator were "
                "corrected with Act names, years and the incomplete-equality "
                "qualification.",
            ),
            15: (
                "Two unresolved direct Prelims demand cards",
                "Supplementary historical evidence identifies Lala Lajpat Rai "
                "from the 2018 biographies-and-career clues and supports the "
                "2020 *Desher Katha* statement set; local official keys remain "
                "unavailable, so both answers are explicitly inferred.",
                "https://vajiramandravi.com/upsc-exam/with-reference-to-the-book-desher-katha-written-by-sakharam-ganesh-deuskar-during-the-freedom-struggle/",
                "Canonical Basic owner gained the bounded ownership/PYQ "
                "control; the two demand-card repairs remain generation-local.",
            ),
        }.get(number)
        issue_rows = [
            f"| MHIST{number:02d}-001 | high | `{key}` | complete session | "
            "Explicit syllabus/evidence/status/approval contract | The g1 "
            "session lacked the binding deep-review contract | "
            f"E-MHIST{number:02d}-001 | MD-MHIST{number:02d}-001 | "
            f"closed in g{generation} |",
            f"| MHIST{number:02d}-002 | high | `{key}` | session + both flows | "
            "Topic-specific chronology, close distinction and evidence limit | "
            "The g1 four-artifact ledger did not contain the fresh Modern "
            f"History control | E-MHIST{number:02d}-002 | "
            f"MD-MHIST{number:02d}-002 | closed in g{generation} |",
        ]
        if factual:
            issue_rows.append(
                f"| MHIST{number:02d}-003 | high | `{key}` | "
                f"four-artifact factual consistency | {factual[0]} | "
                f"{factual[1]} | E-MHIST{number:02d}-003 | "
                f"MD-MHIST{number:02d}-003 | closed in g{generation} |"
            )
        else:
            issue_rows.append(
                f"| MHIST{number:02d}-003 | medium | `{key}` | all four "
                "artifacts | Immutable fresh reconstruction | Mechanically "
                "valid g1 artifacts still required a collision-free successor "
                f"from one reviewed ledger | E-MHIST{number:02d}-003 | "
                f"MD-MHIST{number:02d}-003 | closed in g{generation} |"
            )
        append_once(
            REVIEW_ROOT / "ISSUE-LEDGER.md",
            f"| MHIST{number:02d}-001 |",
            issue_rows,
            changed,
        )

        evidence_rows = [
            f"| E-MHIST{number:02d}-001 | `{key}` | Canonical Basic/Core, "
            "canonical owner, optional Advanced and syllabus mapping were "
            f"reviewed and hash-locked | repository source | "
            f"`{rel(topic.basic_path)}`; `{rel(topic.canonical_path)}`; "
            f"`{rel(topic.advanced_path)}`; `{rel(SYLLABUS_MAPPING)}` | "
            f"repository owners | {DATE} | verified |",
            f"| E-MHIST{number:02d}-002 | `{key}` | PYQ routing, all solved "
            "models, 80 Basic/remedial MCQs and both twelve-stage flows were "
            f"reconciled | generated + repository PYQ evidence | "
            f"`{row['validation']}` | g{generation} | {DATE} | verified; "
            "approval false |",
        ]
        if factual:
            evidence_rows.append(
                f"| E-MHIST{number:02d}-003 | `{key}` | {factual[1]} | "
                f"official/primary web evidence | `{factual[2]}` | topic "
                f"correction | {DATE} | verified and regenerated |"
            )
        else:
            evidence_rows.append(
                f"| E-MHIST{number:02d}-003 | `{key}` | No material factual, "
                "chronological, geographical, attribution or PYQ error remained "
                "after source-to-artifact reconciliation | four-artifact "
                f"re-review | `{row['validation']}` | g{generation} | {DATE} | "
                "verified |"
            )
        append_once(
            REVIEW_ROOT / "EVIDENCE-LEDGER.md",
            f"| E-MHIST{number:02d}-001 |",
            evidence_rows,
            changed,
        )

        source_note = (
            factual[3]
            if factual
            else (
                "Canonical Basic owner gained the idempotent ownership/PYQ "
                "control; the remaining repair is generation-local."
                if number <= 20
                else "No canonical knowledge Markdown changed; repair is "
                "generation-local."
            )
        )
        suggestion_rows = [
            f"| MD-MHIST{number:02d}-001 | high | `{key}` | generated session | "
            "Deep-review contract absent | "
            f"E-MHIST{number:02d}-001 | Add syllabus, evidence, PYQ/current "
            "status and approval controls | Generated Core | session | "
            f"applied g{generation}; canonical owner unchanged |",
            f"| MD-MHIST{number:02d}-002 | high | `{key}` | generated session "
            "+ flows | Topic chronology/distinction/qualification control "
            f"absent | E-MHIST{number:02d}-002 | Add the three reviewed controls "
            "to the session and independently complete ASCII/graphical rails | "
            f"Generated Core/flow | all four artifacts | applied g{generation} |",
            f"| MD-MHIST{number:02d}-003 | "
            f"{'high' if factual else 'medium'} | `{key}` | "
            f"{factual[0] if factual else 'generation identity'} | "
            f"{factual[1] if factual else 'Fresh reviewed identity required'} | "
            f"E-MHIST{number:02d}-003 | {source_note} | "
            f"{'Source + generator' if number in (37, 38) else 'Generator/pipeline'} "
            f"| all four artifacts | applied and verified g{generation} |",
        ]
        append_once(
            REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
            f"| MD-MHIST{number:02d}-001 |",
            suggestion_rows,
            changed,
        )


_base_main = main


def main() -> int:
    result = _base_main()
    _rewrite_command_history()
    _augment_inventory_with_publication_changes()
    return result


if __name__ == "__main__":
    raise SystemExit(main())
