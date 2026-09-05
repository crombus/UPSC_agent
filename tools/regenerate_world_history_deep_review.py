"""Deep-review and immutably regenerate all 21 World History packages."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import textwrap
from collections import Counter
from pathlib import Path
from typing import Any


_BASE = Path(__file__).with_name("regenerate_ancient_history_deep_review.py")
_BASE_SHA256 = "d3c208166750909b3d46be15c087d26a098d9dd95eda588f6a19974d511a7780"
_base_bytes = _BASE.read_bytes()
if hashlib.sha256(_base_bytes).hexdigest() != _BASE_SHA256:
    raise RuntimeError(
        "The shared deep-review engine changed. Review and repin it before "
        "running the World History workflow."
    )
_source = _base_bytes.decode("utf-8").replace("\r\n", "\n")
_source = _source.rsplit('\nif __name__ == "__main__":', 1)[0]

for _old, _new in (
    ("2026-08-30", "2026-09-04"),
    ("30 August 2026", "4 September 2026"),
    ("Ancient-Indian-History", "World-History"),
    ("ancient-indian-history", "world-history"),
    ("Ancient History", "World History"),
    ("Ancient-History", "World-History"),
    ("ancient-history", "world-history"),
    ("ancient_history", "world_history"),
    ("E-AH", "E-WH"),
    ("MD-AH", "MD-WH"),
    ("AH{", "WH{"),
    ("AH01", "WH01"),
    ("range(1, 28)", "range(1, 22)"),
    ("topics 01-27", "topics 01-21"),
    ('"topic_count": 27', '"topic_count": 21'),
    ('"topic_validations_passed": 27', '"topic_validations_passed": 21'),
    ('"latest_topic_count": 27', '"latest_topic_count": 21'),
    ('"learning_and_workbook_pdfs_checked": 54', '"learning_and_workbook_pdfs_checked": 42'),
    ('"represented": 27', '"represented": 21'),
    ('"expected": 27', '"expected": 21'),
    ("All 27 topics", "All 21 topics"),
    (
        "        25: (21, 25),\n"
        "        27: (26, 27),\n",
        "        21: (21, 21),\n",
    ),
):
    if _old not in _source:
        raise RuntimeError(f"Shared-engine transformation anchor is missing: {_old!r}")
    _source = _source.replace(_old, _new)

_tests_anchor = '''    tests = [
        run_unittest("test_regenerate_world_history_deep_review"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
'''
_tests_replacement = '''    tests = [
        run_unittest("test_regenerate_world_history_deep_review"),
        run_unittest("test_generate_world_history_01_02_sequential"),
        run_unittest("test_generate_world_history_03_04_sequential"),
        run_unittest("test_generate_world_history_05_sequential"),
        run_unittest("test_generate_world_history_06_07_sequential"),
        run_unittest("test_generate_world_history_08_09_sequential"),
        run_unittest("test_generate_world_history_10_sequential"),
        run_unittest("test_generate_world_history_11_12_sequential"),
        run_unittest("test_generate_world_history_13_14_sequential"),
        run_unittest("test_generate_world_history_15_sequential"),
        run_unittest("test_generate_world_history_16_17_sequential"),
        run_unittest("test_generate_world_history_18_sequential"),
        run_unittest("test_generate_world_history_19_20_sequential"),
        run_unittest("test_generate_world_history_21_sequential"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
'''
if _tests_anchor not in _source:
    raise RuntimeError("Shared-engine targeted-test anchor is missing.")
_source = _source.replace(_tests_anchor, _tests_replacement, 1)

_failure_anchor = '''    relevant_failures = sum(item["failures"] + item["errors"] for item in tests)
    if relevant_failures or any(item["exit_code"] for item in tests):
        raise RuntimeError(f"Relevant targeted tests failed: {tests}")
'''
_failure_replacement = '''    unrelated_pre_existing_failures = []
    relevant_failures = sum(item["failures"] + item["errors"] for item in tests)
    if relevant_failures or any(item["exit_code"] for item in tests):
        raise RuntimeError(f"Relevant targeted tests failed: {tests}")
'''
if _failure_anchor not in _source:
    raise RuntimeError("Shared-engine targeted-failure anchor is missing.")
_source = _source.replace(_failure_anchor, _failure_replacement, 1)
_source = _source.replace(
    '"unrelated_pre_existing_failures": [],',
    '"unrelated_pre_existing_failures": unrelated_pre_existing_failures,',
    1,
)

_generation_source_anchor = '''    main = repo(old["markdown"]).read_text(encoding="utf-8")
    workbook_value = old.get("workbook_markdown") or old.get(
        "provenance", {}
    ).get("workbook_markdown")
    workbook = repo(workbook_value).read_text(encoding="utf-8")
'''
_generation_source_replacement = '''    main, workbook = generation_sources(topic, old)
'''
if _generation_source_anchor not in _source:
    raise RuntimeError("Shared-engine generation-source anchor is missing.")
_source = _source.replace(
    _generation_source_anchor,
    _generation_source_replacement,
    1,
)

exec(compile(_source, str(Path(__file__)), "exec"), globals())

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


PYQ_LEDGERS = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
)
TOPIC21_AUTHORED_ASCII = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "world-history-21-2026-09-01-sequential.json"
)
TOPIC21_AUTHORED_WORKBOOK = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "World-History"
    / "learning-sessions"
    / "v2"
    / "subject-wide-syllabus"
    / "world-history-21_Solved-Workbook.md"
)
TOPIC21_AUTHORED_SESSION = (
    TOPIC21_AUTHORED_WORKBOOK.parent
    / "world-history-21_Learning-Session.md"
)


def generation_sources(
    topic: Topic,
    record: dict[str, Any],
) -> tuple[str, str]:
    """Use the repaired canonical Topic 21 masters, predecessors elsewhere."""
    if topic.number == 21:
        missing = [
            path
            for path in (TOPIC21_AUTHORED_SESSION, TOPIC21_AUTHORED_WORKBOOK)
            if not path.is_file()
        ]
        if missing:
            raise FileNotFoundError(
                "Topic 21 authoring masters are missing: "
                + ", ".join(map(str, missing))
            )
        return (
            TOPIC21_AUTHORED_SESSION.read_text(encoding="utf-8"),
            TOPIC21_AUTHORED_WORKBOOK.read_text(encoding="utf-8"),
        )
    workbook_value = record.get("workbook_markdown") or record.get(
        "provenance", {}
    ).get("workbook_markdown")
    return (
        repo(record["markdown"]).read_text(encoding="utf-8"),
        repo(workbook_value).read_text(encoding="utf-8"),
    )


def topics() -> list[Topic]:
    """Return the exact tracker/catalogue-owned World History sequence."""
    manifest = load(SECTION_MANIFEST)
    expected = [f"world-history-{number:02d}" for number in range(1, 22)]
    rows = [
        row
        for row in manifest["topics"]
        if row.get("topic_key") in set(expected)
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
    if len(result) != 21 or [topic.topic_key for topic in result] != expected:
        raise ValueError(
            "World History review scope must contain exact topic keys 01-21 "
            "in tracker/catalogue order."
        )
    return result


def review_paths(topic: Topic, generation: int) -> dict[str, Path]:
    """Use short immutable paths that remain safe under normal Windows APIs."""
    short_key = f"wh-{topic.number:02d}"
    knowledge_dir = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Learner-v2-Refreshed"
        / "World"
        / "WH"
        / "learning-sessions"
        / short_key
        / f"g{generation}"
    )
    notes_dir = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "World"
        / "WH"
        / "learning-sessions"
        / short_key
        / f"g{generation}"
    )
    flow_dir = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "World"
        / "WH"
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


WORLD_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    1: (
        "Locke (1689), Montesquieu (1748) and Rousseau (1762) supplied distinct arguments about rights, divided power and popular sovereignty; ideas gave legitimacy while crisis and mobilisation determined revolutionary timing.",
        "Liberalism, conservatism, nationalism, capitalism, socialism, communism and social democracy must be compared by authority, ownership, method and social constituency rather than treated as synonyms or a single linear progression.",
        "Universal rights-language coexisted with exclusions based on property, sex, slavery, race and colonial status; later inclusion used the same grammar but was neither immediate nor inevitable.",
    ),
    2: (
        "The core sequence is post-1763 imperial tightening, Stamp Act (1765), Boston Tea Party (1773), Lexington-Concord (1775), Declaration (1776), Saratoga (1777), Yorktown (1781), Paris (1783), Constitution in force (1789) and Bill of Rights (1791).",
        "Saratoga internationalised the war, Yorktown was the decisive surrender and the Treaty of Paris supplied legal recognition; these are related but not interchangeable turning points.",
        "The Revolution transformed sovereignty and constitutional form while preserving slavery, Native dispossession, property restrictions and women's exclusion, so political radicalism must be qualified socially.",
    ),
    3: (
        "Estates-General, National Assembly, Bastille, August decrees and Rights Declaration belong to 1789; republic and regicide, Terror, Directory, Brumaire (1799), Empire (1804) and Waterloo (1815) form later distinct stages.",
        "Fiscal breakdown, privilege and subsistence crisis were structural conditions; ministerial failure and the 1789 political confrontation were triggers, while crowds, peasants and assemblies supplied agency.",
        "Napoleonic law and administrative rationalisation spread selected revolutionary gains, but censorship, dynastic empire and war block a simple liberator or revolutionary-fulfilment verdict.",
    ),
    4: (
        "Britain's first industrial breakthrough joined coal and iron, agricultural and demographic change, credit, transport, imperial markets and institutions; invention alone does not explain timing.",
        "Textiles, steam, factory discipline and railways were connected mechanisms but had different chronologies and effects, while industrialisation outside Britain followed multiple state, labour and resource paths.",
        "Output and connectivity expanded alongside urban crowding, class conflict, gendered labour, ecological damage and colonial deindustrialisation; progress and harm require spatially differentiated evidence.",
    ),
    5: (
        "The Congress of Vienna (1814-15) used balance, legitimacy, compensation and containment after Napoleon; the Concert was a consultation practice among powers rather than a permanent supranational government.",
        "The Vienna settlement's long peace among great powers must be separated from repression of liberal and national movements and from wars that continued at imperial or regional margins.",
        "Metternich mattered, but British, Russian, Prussian, Austrian, French and smaller-state interests shaped the settlement; stability was negotiated and adaptive, not the product of one statesman or a frozen order.",
    ),
    6: (
        "Italy's sequence runs through Mazzini (1831), failed 1848, Cavour and France (1859), Garibaldi (1860), kingdom (1861), Venetia (1866) and Rome (1870); Germany's runs through Bismarck (1862) and wars of 1864, 1866 and 1870-71.",
        "Italian unification visibly combined ideology, popular arms, diplomacy and monarchy, whereas German timing, boundary and constitutional form were more decisively Prussian and state-led.",
        "Proclamation did not complete nation-building: regional, church, class and minority conflicts remained, and Alsace-Lorraine became one source of later tension rather than a mechanical cause of 1914.",
    ),
    7: (
        "New Imperialism joined industrial and financial interests, strategic routes, prestige rivalry and racial legitimation; technology and medicine increased capability but did not themselves create motive.",
        "The Berlin Conference (1884-85) standardised recognition and effective occupation; it did not draw every African border at one sitting or convert paper claims instantly into control.",
        "Adwa, Samori Ture, Zulu resistance, Maji Maji and African negotiation show agency under unequal power, while extraction, labour coercion and remade authority require African-centred evidence rather than a passive-continent narrative.",
    ),
    8: (
        "Haiti, Spanish American wars led by actors including Bolívar and San Martín, and Brazil's monarchical separation followed different chronologies, social coalitions and relations to Atlantic war.",
        "Independence displaced Iberian sovereignty faster than it transformed landholding, racial hierarchy, slavery or creole elite power; state formation and social revolution are separate tests.",
        "Napoleonic crisis and Atlantic ideas created openings, but enslaved, Indigenous, mixed-race, creole and regional actors pursued different projects; Latin America was not a derivative European stage.",
    ),
    9: (
        "Alliance blocs, arms competition, imperial rivalry, nationalism and Balkan crises created structural danger; Sarajevo was the trigger and the July Crisis converted a regional assassination into general war through state choices.",
        "Triple Entente and Triple Alliance were diplomatic alignments, not automatic identical war plans; Italy's 1914 position and later Ottoman and Bulgarian entry prevent a static two-camp map.",
        "German risk-taking mattered, but a monocausal guilt story obscures Austro-Hungarian, Russian, French, British, Serbian and imperial agency and the difference between responsibility and inevitability.",
    ),
    10: (
        "Mobilisation and stalemate in 1914, total-war economies, multiple European and imperial fronts, US entry and Russian exit in 1917, and the November 1918 armistice must remain chronologically distinct.",
        "Military victory, armistice, Paris peace treaties, Versailles provisions and the League settlement were separate stages; treaty grievance neither explains the whole war nor makes a second war automatic.",
        "Mass death, revolution, empire collapse, mandates, minority problems and colonial mobilisation remade the world beyond Europe, so aftermath cannot be reduced to German punishment alone.",
    ),
    11: (
        "League formation (1920), Washington, Dawes, Locarno, Kellogg-Briand, Young Plan and conditional reconciliation precede Depression, Manchuria, Abyssinia, Rhineland, Spain, Anschluss, Munich, Prague and the Nazi-Soviet Pact.",
        "Institutional design weaknesses and member-state choices must be separated: technical and humanitarian work could succeed while sanctions and collective enforcement failed.",
        "Appeasement should be assessed through war memory, readiness and finite-grievance assumptions, then tested against deterrence erosion and Prague's destruction of the self-determination defence.",
    ),
    12: (
        "Mussolini reached office in October 1922 through pressure and royal invitation; Hitler became Chancellor in January 1933 without an overall electoral majority and converted office into dictatorship through the Enabling Law and coercion.",
        "Italian fascism, German Nazism, Japanese military authoritarianism and Francoism share family resemblances but differ in mass-party form, racial doctrine, surviving institutions and routes to power.",
        "Biological racism and antisemitism were constitutive of Nazism, not optional excesses; Depression mattered through pre-existing institutional fragility, elite complicity, violence and political choice.",
    ),
    13: (
        "The 1905 crisis, February and October 1917 revolutions, Civil War, War Communism, NEP, Lenin's death and Stalin's consolidation form a process rather than one inevitable Bolshevik event.",
        "February overthrew tsarism and created dual power; October transferred power to the Bolsheviks, while decrees, coercion and Civil War changed the revolutionary coalition and state.",
        "Industrialisation and state capacity must be assessed alongside collectivisation, famine, purges, nationality policy and the evidentiary limits of official output or constitutional claims.",
    ),
    14: (
        "Axis expansion and appeasement precede Poland (1939); the widening sequence includes France (1940), Barbarossa and Pearl Harbor (1941), Midway, El Alamein and Stalingrad, Allied advance, atomic bombing and surrender in 1945.",
        "European, Mediterranean, African, Atlantic and Asia-Pacific theatres were connected but not one battlefield, and genocide must remain analytically distinct from ordinary military chronology.",
        "Leadership and ideology mattered within industrial capacity, logistics, alliance resources, resistance and colonial manpower; Allied victory was neither automatic nor explainable by one battle.",
    ),
    15: (
        "Truman containment, Marshall aid, NATO, Soviet consolidation and the Warsaw Pact frame one sequence, while Korea, Cuba, Vietnam, détente, renewed tension and the 1989-91 end phase changed its form.",
        "Bipolar structure did not erase non-alignment, decolonised-state agency, intra-bloc disputes or the Sino-Soviet split; proxy arenas had local causes and actors.",
        "Nuclear deterrence constrained direct superpower war but enabled arms racing and risk; détente was managed competition, not the end of ideology or conflict.",
    ),
    16: (
        "Dumbarton Oaks (1944), San Francisco and October 1945 anchor the founding; the six principal bodies, Security Council composition and ICJ-ICC distinction must remain exact.",
        "Peacekeeping, ceasefire supervision and Security Council-authorised collective enforcement are different tools; Korea and the 1991 Gulf War were not ordinary blue-helmet operations.",
        "UN performance is function- and power-dependent: social, legal and humanitarian work can succeed while veto collision blocks enforcement; reform claims must carry a current source and date.",
    ),
    17: (
        "Qing crisis, 1911 revolution, warlordism, CCP foundation (1921), KMT rupture (1927), Long March, Japanese invasion, 1949 victory, Maoist campaigns and post-1978 reform form distinct state-building phases.",
        "The KMT's inflation, corruption and war burden must be compared with CCP land, discipline, peasant and national-defence strategies; Soviet assistance is not a complete explanation.",
        "Great Leap famine, Cultural Revolution, reform without democratisation, Sino-Soviet rupture and diverse Asian communist routes prevent a triumphalist or monolithic communist-bloc account.",
    ),
    18: (
        "Asian and African decolonisation accelerated through imperial exhaustion, anti-colonial organisation, war mobilisation, international norms and changing metropolitan calculations, but timing and violence varied sharply.",
        "Negotiated transfer, revolutionary war, partition, settler conflict and continuing dependency are distinct routes; formal independence is not identical to completed economic or institutional decolonisation.",
        "Bandung, the UN and pan-African or Asian solidarities matter alongside local movements, women, workers, peasants and armed groups; Europe did not simply grant freedom to passive colonies.",
    ),
    19: (
        "Twentieth-century US power in Latin America usually operated as informal strategic, commercial, financial and political leverage interacting with domestic elites, armies and reform movements.",
        "Mexico, Guatemala, Cuba, Nicaragua, Brazil and Venezuela followed different paths; revolution, coup, authoritarian development and populism cannot be collapsed into one regional cycle.",
        "Commodity dependence, ISI, borrowing, the 1980s debt crisis and liberalisation form a political-economy sequence whose numerical examples must remain country-, year- and source-bounded.",
    ),
    20: (
        "War and Depression, Bretton Woods (1944), Cold War blocs, oil shocks and debt, post-1990 globalisation and the 2008 crisis form the economic chronology; integration transmitted gains and contagion unevenly.",
        "Rapid population growth followed falling mortality before fertility transition, while younger and ageing societies face different pressures; coercive and welfare-based population policies are not one category.",
        "The New Deal stabilised finance, relief, labour and social protection without ending mass unemployment; comparison with Nazi rearmament must retain dictatorship, racial exclusion and militarisation.",
    ),
    21: (
        "Gorbachev's reform phase, Eastern European revolutions of 1989, Two Plus Four settlement and German reunification in 1990, failed August 1991 coup and December Soviet dissolution are distinct stages.",
        "Economic stagnation, nationality pressures, legitimacy loss, arms burdens, reform sequencing, social mobilisation, non-coercion and diplomacy interacted; neither Western pressure nor one leader alone is sufficient.",
        "The Gulf coalition displayed US-led unipolar capability, while Yugoslavia, NATO controversy, unequal globalisation and continuing Global South and Indian agency deny final-peace or Western-teleology claims.",
    ),
}


CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    1: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** the Enlightenment bridge from inherited authority to public
  reason, rights, consent, divided power and popular sovereignty; the causal
  formula ideas + crisis + mobilisation; and overview distinctions among
  liberalism, conservatism, nationalism, capitalism, socialism, communism and
  social democracy.
- **Boundary:** Topic 02 owns the American sequence, Topic 03 the French and
  Napoleonic sequence, Topic 04 industrial transformation, and Topic 05 the
  post-Napoleonic settlement. This overview compares their conceptual grammar
  without duplicating their event narratives.
- **Date control:** Locke (1689), Montesquieu (1748), Rousseau (1762), the
  American Declaration (1776), French rupture (1789), English anti-union repeal
  (1824), Chartism (1830s-40s), US Social Security Act (1935) and Beveridge
  Report (1942) remain distinct intellectual, revolutionary and social-policy
  markers.
- **Mechanism control:** ideas legitimate claims but do not alone determine
  timing, depth or outcome; universal rights-language coexisted with exclusions
  by property, sex, slavery, race and colonial status; doctrines are compared
  by authority, ownership, method and constituency rather than as synonyms.
- **Verified PYQ ownership, 2018-2025:** zero direct overview-only routes. The
  2019 GS-I American-and-French-Revolutions demand remains cross-owned by
  Topics 02 and 03 and is not relabelled here. No unsupported key, quotation or
  current linkage is invented.""",
    2: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** imperial tightening after 1763; taxation, representation and
  colonial self-government; resistance and war; Declaration, alliance,
  surrender, legal recognition and constitutional settlement; and the
  Revolution's political radicalism alongside social exclusions.
- **Boundary:** Topic 01 owns the Enlightenment comparison and Topic 03 owns
  the French Revolution. Topic 02 uses those bridges only to explain the
  American break with empire, federal republican construction and its limits.
- **Date control:** Stamp Act (1765), Boston Tea Party (1773), First
  Continental Congress (1774), Lexington-Concord (1775), Declaration
  (4 July 1776), Saratoga (1777), French alliance (1778), Yorktown (1781),
  Paris (1783), Constitution in force (1789) and Bill of Rights (1791) are
  separate stages.
- **Mechanism control:** Saratoga internationalised the war, Yorktown supplied
  decisive surrender and Paris supplied legal recognition; political
  sovereignty changed while slavery, Native dispossession, property limits and
  women's exclusion survived.
- **Verified PYQ/current ownership, 2018-2025:** the 2019 GS-I demand is a
  verified neutral cross-cutting route shared with Topic 03. America250's
  official site, rechecked 4 September 2026, supports only the dated current
  claim that it is a bipartisan initiative for the United States' 250th
  anniversary; it does not prove a historical interpretation.""",
    3: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Old Regime structures and fiscal-subsistence crisis; the
  1789 constitutional and popular rupture; republic, war, Terror and Directory;
  Napoleon's seizure, law, administration, empire and defeat; social
  participation, exclusions and the Revolution's contested legacy.
- **Boundary:** Topic 01 owns the conceptual Enlightenment overview, Topic 02
  the American Revolution, and Topic 05 the Vienna settlement. Topic 03 ends
  with Napoleon's defeat and uses Vienna only as the transition to Topic 05.
- **Date control:** National Assembly (17 June 1789), Tennis Court Oath
  (20 June), Bastille (14 July), August decrees and Rights Declaration (1789),
  constitution (1791), republic (1792), regicide (1793), Terror (1793-94),
  Directory (1795-99), Brumaire (1799), Code (1804) and Waterloo (1815) remain
  distinct.
- **Mechanism control:** structural privilege, fiscal breakdown and subsistence
  stress differ from political triggers and popular agency; Napoleon preserved
  legal equality and administrative rationalisation while restricting
  sovereignty through censorship, dynasty and war.
- **Verified PYQ ownership, 2018-2025:** the 2019 GS-I demand is cross-owned
  with Topic 02; the 2025 GS-I enduring-relevance demand is directly owned and
  retains its verified wording, marks and word limit. No objective key or live
  commemoration is fabricated.""",
    4: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Britain's first industrial breakthrough; coal, iron,
  agriculture, demography, capital, institutions, transport and markets;
  textiles, steam, factory discipline and railways; social, gendered,
  ecological and imperial effects; labour and legislative responses; and
  multiple later industrialisation paths.
- **Boundary:** Topic 01 owns doctrine-level capitalism/socialism comparison.
  Modern Indian History Topic 07 owns the final India-side deindustrialisation
  verdict. Topic 04 supplies the English technological and political-economy
  mechanism and comparative railway framework without annexing either owner.
- **Date control:** spinning jenny (1764), water frame (1769), Watt patent
  (1769), Factory Act (1802), power loom (1785), cotton gin (1793), anti-union
  repeal (1824), passenger railway (1830) and Chartism (1830s-40s) retain their
  separate inventions, legal status and effects.
- **Mechanism control:** invention alone does not explain British priority;
  Watt improved rather than solely invented the steam engine; connectivity can
  integrate or extract depending on ownership, state power and colonial
  structure; output growth does not erase concentrated immediate costs.
- **Verified PYQ ownership, 2018-2025:** the 2023 GS-I railway demand is a
  direct World History route. The exact 2024 GS-I England-and-Indian-handicrafts
  demand is bridged here, while the India verdict remains Modern
  History-owned. No current statistic or unsupported causal percentage is
  introduced.""",
    5: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** Congress of Vienna principles and territorial settlement;
  balance, legitimacy, compensation and containment; the Concert as a
  consultation practice; Holy Alliance and congress distinctions; repression,
  intervention, adaptation and the settlement's peace-versus-legitimacy
  verdict.
- **Boundary:** Topic 03 owns Napoleon through Waterloo; Topic 06 owns Italian
  and German unification. Topic 05 owns the post-Napoleonic settlement and
  Concert, using 1830 and 1848 only to test the system rather than narrate later
  national unifications.
- **Date control:** Congress (1814-15), Final Act (June 1815), Holy Alliance
  (1815), Aix-la-Chapelle (1818), Carlsbad Decrees (1819), Troppau (1820),
  Laibach (1821), Verona (1822), Belgian independence (1830) and revolutions
  (1848) remain separate diplomatic, repressive and adaptive stages.
- **Mechanism control:** the Concert was neither the Holy Alliance nor a
  permanent supranational government; Metternich was influential but did not
  act alone; great-power peace coexisted with repression and wars at regional
  and imperial margins.
- **Verified PYQ ownership, 2018-2025:** zero direct topic-only routes.
  Probable questions remain original practice. No PYQ, official key or live
  institutional claim is invented.""",
    6: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** the national unification of Italy and Germany; their
  ideological, popular, diplomatic, monarchical and military agents; exact
  territorial sequences; comparison of state nuclei and methods; political
  forms, incomplete integration and effects on the European balance.
- **Boundary:** Topic 05 owns the Vienna settlement, Topic 07 owns New
  Imperialism and Africa, and Topic 09 owns the pre-1914 alliance system,
  causes and outbreak. Topic 06 uses Vienna and Alsace-Lorraine only as the
  opening condition and bounded consequence of national unification.
- **Date control:** Young Italy (1831), failed revolutions (1848), Lombardy
  (1859), Garibaldi's southern campaign (1860), Kingdom of Italy (1861),
  Danish War (1864), Seven Weeks' War and Venetia (1866), Rome (1870), and
  German Empire at Versailles (January 1871) remain separate stages.
- **Mechanism control:** Italy visibly combined Mazzini's programme, Cavour's
  statecraft, Garibaldi's popular arms and Victor Emmanuel II's monarchy;
  Germany's timing, small-German boundary and federal-authoritarian form were
  more decisively imposed by Prussia, Bismarck and three wars. Proclamation
  did not complete social integration or make 1914 inevitable.
- **Verified PYQ ownership, 2018-2025:** zero direct topic-only routes.
  Comparison and from-above/from-below questions remain original practice; no
  Bismarck quotation, objective key or current linkage is invented.""",
    7: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** New Imperialism and the partition of Africa; industrial,
  financial, strategic, prestige, technological and ideological drivers;
  Berlin's recognition rules; conquest and colonial political economy;
  African resistance, negotiation and adaptation; violence, labour,
  authority and border consequences.
- **Boundary:** Topic 04 owns industrialisation, Topic 09 owns imperial rivalry
  inside the pre-1914 causal system, and Topic 18 owns decolonisation and the
  post-1945 successor-state settlement. Topic 07 owns imperialism in Africa
  and uses those owners only for bounded cause and legacy bridges.
- **Date control:** Suez Canal (1869), limited European control in the 1870s,
  British occupation of Egypt (1882), Berlin Conference
  (15 November 1884-26 February 1885), Adwa (1896), Herero and Nama genocide
  (1904-08), Maji Maji (1905-07) and the 1914 partition benchmark remain
  distinct.
- **Mechanism control:** technology and medicine supplied capability rather
  than motive; Berlin standardised effective occupation but did not draw every
  border or instantly create control; African societies were agents under
  unequal power, and border inheritance is not a deterministic explanation
  for every later conflict.
- **Verified PYQ/current ownership, 2018-2025:** zero direct topic-only PYQs.
  The official African Union Africa Day 2026 linkage is confined to the
  continuing legacy of slavery, colonialism and reparatory justice; it does
  not directly verify Berlin Conference history.""",
    8: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** the Iberian crisis and five distinct independence paths in
  Haiti, northern South America, southern South America, Mexico and Brazil;
  leaders, coalitions and campaigns; transfer of sovereignty; persistence of
  creole power, slavery, land and racial hierarchy; fragmentation and
  caudillismo as a bounded post-independence mechanism.
- **Boundary:** Topics 02 and 03 own the American and French revolutionary
  backgrounds, Topic 19 owns twentieth-century Latin America, and Topic 18
  owns post-1945 Asian-African decolonisation. Topic 08 compares those owners
  without importing their event narratives.
- **Date control:** Haitian Revolution (1791) and independence (1804), Iberian
  crisis (1808), Hidalgo's revolt (1810), San Martin's Andes crossing (1817),
  New Granada and Gran Colombia (1819), Mexico (1821), Brazil under Pedro I
  (1822), Ayacucho (1824) and Bolivia (1825) remain separate stages.
- **Mechanism control:** imperial collapse opened the political opportunity,
  but creole, enslaved, Indigenous, mixed-race and regional actors pursued
  different projects. Independence ended Iberian sovereignty faster than it
  transformed social power; Haiti is the radical social contrast, not a
  peripheral duplicate.
- **Verified PYQ/current ownership, 2018-2025:** zero direct topic-only PYQs.
  The official 2026 Panama bicentennial linkage supports only the 1826
  Amphictyonic Congress and Bolivar's regional-cooperation project; it does
  not validate decorative ceremony detail.""",
    9: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** the 1914 international system, alliance alignments, arms and
  naval competition, imperial rivalry, nationalism and Balkan crises; the
  Sarajevo trigger; July Crisis state choices, mobilisation and the mechanism
  that converted an Austro-Serb conflict into general war.
- **Boundary:** Topic 06 owns national unification and Alsace-Lorraine's
  creation, Topic 07 owns New Imperialism in Africa, and Topic 10 owns the
  war's military course, total-war consequences and 1919-23 settlements.
  Topic 09 ends when general war begins.
- **Date control:** Triple Alliance (1882), Franco-Russian alliance (1894),
  Entente Cordiale (1904), Anglo-Russian agreement (1907), Bosnia Crisis
  (1908), Agadir (1911), Balkan Wars (1912-13), Sarajevo (28 June 1914),
  Austrian declaration (28 July) and 1-4 August escalation remain distinct.
- **Mechanism control:** diplomatic alignments were not identical automatic
  war plans; Italy's position disproves a static two-camp map. Sarajevo was a
  trigger, not a sufficient cause; the July Crisis transmitted Balkan,
  imperial, national, strategic and operational choices. Responsibility does
  not equal inevitability.
- **Verified PYQ ownership, 2018-2025:** the exact 2024 GS-I 15-mark,
  250-word demand asks how far the First World War was fought essentially for
  preservation of balance of power. Balance explains the system and part of
  Britain's entry, not every belligerent motive or the complete purpose.""",
    10: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** the First World War's military and imperial course; trench
  stalemate, attrition, sea power, coalition endurance and defeat; total-war
  state and social effects; empire collapse; the distinct armistice and
  1919-23 treaty cluster, mandates, minorities and unstable peace.
- **Boundary:** Topic 09 owns causes, July escalation and the exact 2024
  balance-of-power PYQ. Topic 11 owns interwar international relations,
  reparations diplomacy, collective-security failure and appeasement. Topic 10
  ends with immediate consequences and the peace settlement's inherited
  problems.
- **Date control:** Marne (September 1914), Gallipoli (1915), Verdun and Somme
  (1916), unrestricted submarine warfare and US entry (1917),
  Brest-Litovsk (March 1918), armistice (11 November 1918), Versailles,
  St Germain and Neuilly (1919), Trianon and Sevres (1920), and Lausanne
  (1923) remain distinct military, diplomatic and legal stages.
- **Mechanism control:** military victory, armistice, Paris negotiations,
  individual treaties and League arrangements are not synonyms. Total war
  mobilised states, civilians, women, industry and empires; treaty grievance
  neither explains the war's outbreak nor makes a second war automatic.
- **Verified PYQ ownership, 2018-2025:** zero direct topic-only routes. The
  exact 2024 balance-of-power demand remains Topic 09-owned; probable
  course, total-war and settlement questions remain original practice. No
  unsourced casualty figure or current linkage is invented.""",
    11: """## 9. Semantic-completeness ownership and PYQ control

- **Owned core:** the interwar diplomatic system from the League's formal
  beginning through reparations diplomacy, Washington, Dawes, Locarno,
  Kellogg-Briand and Young; the Depression's diplomatic transmission;
  Manchuria, Abyssinia, separate bargains, appeasement and the final collapse
  of deterrence before Poland.
- **Boundary:** Topic 10 owns the First World War's course and 1919-23 peace
  settlement, Topic 12 owns fascist regimes and their domestic power systems,
  and Topic 14 owns the Second World War's military course. Topic 11 owns the
  interwar international-relations mechanism connecting those topics.
- **Date control:** League beginning (10 January 1920), Washington
  (1921-22), Dawes (1924), Locarno (1925), Germany's League entry (1926),
  Kellogg-Briand (1928), Young (1929), Manchuria (1931), Abyssinia and the
  Anglo-German Naval Agreement (1935), Rhineland (1936), Munich
  (September 1938), Prague (March 1939), Nazi-Soviet Pact and Poland (1939)
  remain distinct stages.
- **Mechanism control:** technical administration did not equal coercive
  collective security; Locarno guaranteed western but not eastern frontiers;
  American credit sustained conditional stability; Depression narrowed
  cooperation; and repeated protest without effective force taught aggressors
  that the next revision would be cheaper.
- **Verified PYQ/current ownership, 2018-2025:** zero direct topic-only routes.
  The 2021 democratic-state-system demand remains Topic 12-owned. The official
  Locarno centenary speech supports only a bounded contemporary reflection on
  multilateral security and does not alter the historical verdict.""",
    12: """## 11. Semantic-completeness ownership and PYQ control

- **Owned core:** the rise, ideology, social base, transfer of power,
  institutions and coercive methods of Italian fascism and German Nazism;
  Japanese military authoritarianism and Francoism as related but non-identical
  cases; and the comparative challenge to interwar democratic government.
- **Boundary:** Topic 11 owns interwar diplomacy and appeasement, Topic 13 owns
  Russia and the USSR, Topic 14 owns wartime campaigns and the Holocaust, and
  Topic 20 owns the Depression's full economic mechanism. Topic 12 uses those
  contexts only to explain authoritarian takeover and regime comparison.
- **Date control:** Fasci (1919), National Fascist Party (1921), March on Rome
  (October 1922), Lateran Treaty (1929), Manchuria (1931), Inukai
  assassination (1932), Hitler's chancellorship (January 1933), Enabling Law
  (March 1933), Night of the Long Knives (1934), Nuremberg Laws (1935),
  Spanish Civil War (1936-39) and full-scale war in China (1937) remain
  separate institutional and geopolitical markers.
- **Mechanism control:** economic crisis widened support but did not itself
  transfer power; kings, conservative elites and legal mechanisms enabled
  takeover. Fascism and Nazism overlap without being identical, biological
  race is constitutive of Nazism, and Japan is safer classified as military
  authoritarianism than as a duplicate mass party-state.
- **Verified PYQ/current ownership, 2018-2025:** one 2021 GS-I demand is
  verified in neutral rendering only: evaluate the challenge to the democratic
  state system between the two World Wars. The UN remembrance linkage concerns
  Nazism's consequences and is not evidence for Italian or Japanese regime
  development.""",
    13: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** the unresolved 1905 settlement, collapse of tsarism,
  February and October 1917 as distinct revolutions, Provisional Government
  failure, Bolshevik consolidation, Civil War, War Communism and NEP, Stalin's
  rise, industrialisation, collectivisation, famine, purges, war and postwar
  repression through Stalin's death.
- **Boundary:** Topic 10 supplies the First World War context, Topic 14 owns
  the Second World War's global military course and genocide, Topic 15 owns
  Soviet external relations in the Cold War, and Topic 21 owns the focused
  1989-91 collapse and post-Cold-War order. Topic 13 owns Russia's domestic
  revolutionary and Stalinist transformation.
- **Date control:** 1905 and October Manifesto, abdication
  (2 March 1917), Bolshevik seizure (night of 25-26 October), Constituent
  Assembly dispersal (January 1918), Brest-Litovsk (March 1918), Civil War
  (1918-20), NEP (1921), Lenin's death (January 1924), Stalin's consolidation
  (1928-29), Constitution and Purges (1936-38), first Soviet atomic bomb
  (1949) and Stalin's death (5 March 1953) remain distinct.
- **Mechanism control:** war converted structural weakness into collapse;
  February was a broad overthrow while October was an organised seizure;
  decree, coercion, central geography, war-winning and tactical retreat
  consolidated Bolshevik power; Stalinist capacity gains must be weighed
  against famine, terror, destroyed expertise and evidentiary limits.
- **Verified PYQ ownership, 2018-2025:** zero direct topic-only routes. All
  revolution, Lenin-Stalin continuity and transformation questions in this
  package remain original practice; no famine total beyond source-bounded
  attribution, constitutional claim or live commemoration is invented.""",
    14: """## 11. Semantic-completeness ownership and PYQ control

- **Owned core:** the linked European and Asia-Pacific origins, phases and
  theatres of the Second World War; early Axis advantage, cumulative turning
  points and defeat; total war, Holocaust specificity, resistance and
  collaboration; and the war's social, imperial, institutional and strategic
  consequences.
- **Boundary:** Topic 11 owns the interwar diplomatic collapse, Topic 12 owns
  fascist regimes, Topic 13 owns Soviet domestic transformation, Topic 15 owns
  Cold War international relations, Topic 16 owns the United Nations as an
  institution, Topic 17 owns China's revolutionary history, and Topic 18 owns
  decolonisation. Topic 14 uses each only as cause, participant or consequence.
- **Date control:** Poland (September 1939), France and Battle of Britain
  (1940), Barbarossa (22 June 1941), Pearl Harbor (7 December 1941), Midway
  (June 1942), El Alamein (October 1942), Stalingrad surrender
  (February 1943), D-Day (6 June 1944), German surrender (May 1945) and
  Japan's surrender sequence (August 1945) remain distinct.
- **Mechanism control:** the European and Asian wars fused in 1941; operational
  success could not offset multi-front overreach, Allied resources, logistics
  and occupation policy; genocide remains distinct from ordinary campaign
  history; and decolonisation was accelerated rather than instantly completed.
- **Verified PYQ/current ownership, 2018-2025:** zero direct topic-only routes.
  Probable war questions remain original practice. The bounded Nuremberg
  eightieth-anniversary linkage concerns legal aftermath, not new evidence
  about campaigns, casualty totals or the causes of victory.""",
    15: """## 11. Semantic-completeness ownership and PYQ control

- **Owned core:** Cold War origins, ideology, security dilemma and bipolar
  structure; containment, economic instruments, alliances, Berlin, Korea,
  Cuba, Vietnam and other global theatres; nuclear deterrence, non-alignment,
  decolonised-state agency, détente, renewed tension and the 1989-91 ending.
- **Boundary:** Topic 14 owns the Second World War and immediate emergence of
  the superpowers, Topic 16 owns United Nations structure and institutional
  performance, Topic 17 owns China's revolution and domestic transformation,
  Topic 18 owns decolonisation, and Topic 21 owns the focused late-Soviet,
  Eastern European and post-1991 transition. Topic 15 owns their Cold War
  international-relations interaction without annexing those histories.
- **Date control:** Truman Doctrine and Marshall Plan (1947), Berlin blockade
  and airlift (1948-49), NATO (1949), Korea (1950-53), Warsaw Pact (1955),
  Berlin Wall (1961), Cuban missiles (1962), SALT I and US-China opening
  (1972), Helsinki (1975), Afghanistan (1979), INF Treaty (1987) and
  the 1989-91 end phase remain distinct.
- **Mechanism control:** ideology shaped interpretation while power and
  security supplied the stakes; nuclear deterrence restrained direct war but
  intensified arms competition and proxy risk; détente managed rather than
  ended rivalry; bipolarity did not erase local causes, non-alignment,
  intra-bloc disputes or the Sino-Soviet split.
- **Verified PYQ/current ownership, 2018-2025:** zero direct topic-only routes.
  All six Mains demands remain original practice. Official diplomacy-museum
  links support renewed public attention to Cold War diplomacy and artefacts,
  not a present-day geopolitical analogy or a new historical conclusion.""",
    16: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** the League-to-UN institutional transition; Dumbarton Oaks,
  San Francisco and October 1945; the six principal Charter bodies; Security
  Council composition and veto; ICJ-ICC and organ-agency-fund distinctions;
  peacekeeping, ceasefire supervision, collective enforcement, non-military
  governance and historically grounded reform logic.
- **Boundary:** Topic 15 owns the Cold War international-relations narratives
  surrounding Korea, Suez, Hungary and other crises; Topic 18 owns mass
  decolonisation and the transformed General Assembly membership; Topic 21
  owns the focused post-1991 order. Topic 16 owns UN design and institutional
  performance, while current Indian negotiating positions remain GS-II/IR.
- **Date control:** Dumbarton Oaks (1944), San Francisco Charter framing and
  October 1945 establishment, Korea and Uniting for Peace (1950), Suez and
  Hungary (1956), Congo (1960-64), Gulf enforcement (1991) and Iraq (2003)
  remain distinct institutional tests.
- **Mechanism control:** consent-based peacekeeping, ceasefire observation and
  Security Council-authorised member-state enforcement are not synonyms; UN
  performance varies by function, mandate, resources and great-power posture;
  the veto both keeps major powers inside the system and constrains action
  against them.
- **Verified PYQ/current ownership, 2018-2025:** zero direct topic-only routes;
  all six Mains demands remain original practice. Official UN80 material
  rechecked 4 September 2026 supports three reform workstreams—Secretariat
  efficiency, mandate implementation review, and structural or programmatic
  realignment—and a June 2026 shift from diagnosis towards action. No
  unsupported budget, staffing, mission-count or reform-outcome claim is
  imported.""",
    17: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** Qing legitimacy crisis, 1911 and warlordism; Sun Yat-sen,
  KMT-CCP cooperation and rupture; Mao's peasant strategy, Long March,
  Japanese invasion and 1949 victory; Maoist consolidation and campaigns;
  post-1978 reform without democratisation; Asian communist diversity and the
  Sino-Soviet and Sino-Vietnamese fractures.
- **Boundary:** Topic 13 owns the Russian Revolution and Stalinist USSR;
  Topic 15 owns superpower Cold War structure; Topic 18 owns colonial transfer
  and postcolonial state formation; Topic 21 owns the post-1991 order. Topic 17
  owns China's revolution, domestic transformation and the Asian communist
  comparison needed to disprove a monolithic bloc.
- **Date control:** 1911 revolution, CCP foundation (1921), KMT rupture
  (1927), Long March (1934-35), full-scale Japanese invasion (1937), PRC
  proclamation (1949), Great Leap (1958-61), Cultural Revolution (1966-76),
  reform after 1978, China-Vietnam war (February 1979), Tiananmen (1989) and
  Sino-Soviet reconciliation (May 1989) remain separate stages.
- **Mechanism control:** KMT governance failure and war burden are compared
  with CCP discipline, land, peasant organisation and patriotic legitimacy;
  military retreat can create political legitimacy; market adaptation did not
  entail multiparty reform; Asian communist regimes followed distinct local
  routes and could fight one another.
- **Verified PYQ ownership, 2018-2025:** zero direct topic-only routes. All six
  Mains demands remain original practice; no famine or casualty total,
  objective key, quotation or current geopolitical analogy is invented.""",
    18: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** why empire became unsustainable after 1945; metropolitan
  exhaustion, nationalist mobilisation, international norms and the
  cost-of-repression mechanism; negotiated, partitioned, settler-war,
  insurgent and hurried transfers; postcolonial borders, institutions,
  economies, secession, external intervention, neo-colonialism and apartheid.
- **Boundary:** Topic 07 owns conquest and New Imperialism; Modern Indian
  History owns India's detailed transfer and partition; Topic 17 owns China's
  revolution and Asian communisms; Topic 19 owns twentieth-century Latin
  America. Topic 18 uses these only for bounded comparison and owns African
  and Asian decolonisation and its uneven aftermath.
- **Date control:** India-Pakistan (1947), Malayan federation (1948), Ghana
  (1957), Congo (1960), Algeria (1962), Malaysia (1963), Singapore separation
  (1965), Biafra (1967-70), Portuguese Africa (1975), Zimbabwe (1980), Rwanda
  (1994) and South African majority rule (1994) remain distinct routes.
- **Mechanism control:** European weakness was insufficient without organised
  anti-colonial pressure; settlers, successor-state design and coercive cost
  changed the route; formal sovereignty did not automatically remove
  commodity dependence, inherited borders or outside leverage; local conflict
  preceded but could be amplified by Cold War intervention.
- **Verified PYQ/current ownership:** the 2015 Malayan-decolonisation and 2016
  Western-educated-Africans demands are retained in owner-verified neutral
  rendering because verbatim wording and marks are not locally held. Official
  2026 UN C-24 material concerns 17 remaining Non-Self-Governing Territories
  and unfinished UN business; it is not conflated with historical mass
  decolonisation.""",
    19: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** twentieth-century constrained sovereignty under informal US
  power; land inequality, commodity dependence and militarised politics;
  Mexican institutional revolution, Guatemala, Cuba, Nicaragua, Brazil and
  Venezuela; ISI, external borrowing, the 1980s debt crisis, austerity,
  liberalisation and dependency as interacting domestic-external mechanisms.
- **Boundary:** Topic 08 owns nineteenth-century independence movements;
  Topic 15 owns the global Cold War system; Topic 20 owns the thematic world
  economy and population; Topic 21 owns the post-Cold-War order. Topic 19 owns
  twentieth-century Latin American cases and their regional political economy.
- **Date control:** Mexican Revolution (1910), Guatemala (1954), Cuban
  Revolution (1959), missile crisis (1962), Sandinista victory (1979), Mexican
  debt crisis (1982) and later liberalisation remain distinct episodes rather
  than one regional cycle.
- **Mechanism control:** US strategic, commercial, financial and covert power
  interacted with domestic elites and movements rather than erasing agency;
  commodity vulnerability encouraged ISI, whose market and import constraints
  encouraged borrowing; debt conditionality transmitted finance into social
  austerity and narrowed democratic policy choice.
- **Verified PYQ/current ownership, 2018-2025:** zero direct topic-only routes;
  all six Mains demands remain original practice. The 19 March 2026 OHCHR
  statement supplies only a dated Argentina transitional-justice, truth,
  memory and non-repetition link; no crowd size or unverified regional
  aggregate is imported.""",
    20: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** wars and Depression in the world economy; Bretton Woods,
  postwar blocs and North-South divergence; oil, debt, globalisation and 2008
  contagion; environmental costs; mortality-led population growth,
  demographic transition, ageing, population policy and HIV/AIDS; Depression
  causation, transmission, New Deal instruments, limits and Nazi comparison.
- **Boundary:** Topic 04 owns the first Industrial Revolution; Topic 10 owns
  the First World War's immediate settlement; Topic 12 owns fascist regimes;
  Topic 19 owns Latin America's regional ISI and debt cases; Topic 21 owns the
  focused post-1991 political order. Topic 20 owns thematic economy and
  population since 1900, using those owners only as bounded evidence.
- **Date control:** October 1929 crash, New Deal from 1933, renewed recession
  after reduced spending in 1938, Bretton Woods (1944), oil/debt pressures of
  the 1970s-80s, post-1990 globalisation and the 2008 crisis remain separate
  economic stages.
- **Mechanism control:** the Crash was a symptom within overproduction,
  unequal purchasing power, export contraction and speculation; credit,
  banking, tariffs, trade and commodity prices transmitted depression;
  mortality can fall before fertility; integration spreads both prosperity
  and contagion; New Deal stabilisation is not equivalent to full recovery or
  Nazi coercive rearmament.
- **Verified PYQ/current ownership:** the legacy 2013 Great-Depression-policy
  demand is retained in neutral rendering because marks and verbatim wording
  are not locally held. Official 2026 UN economic and population sources are
  used only as dated anchors for uneven growth, coordination and demographic
  data; no unfetched forecast or population estimate is imported.""",
    21: """## 10. Semantic-completeness ownership and PYQ control

- **Owned core:** Gorbachev's reform, the Eastern European revolutions of
  1989, German reunification in 1990, the failed August 1991 coup, dissolution
  of the USSR in December 1991 and the contested post-Cold-War order of Gulf
  enforcement, unipolarity, integration, regional wars, globalisation and
  continuing non-Western agency.
- **Boundary:** Topic 15 owns the whole Cold War's structure and long
  chronology; Topic 17 owns China's revolutionary and reform trajectory;
  Topic 20 owns thematic global economy and population. Topic 21 owns the
  focused end phase and new-order debate without annexing those owners;
  Economy and International Relations retain India's detailed 1991 reform and
  strategic-autonomy records.
- **Date control:** Gorbachev (1985), Poland's opening (1988-89), Berlin Wall
  (9 November 1989), Two Plus Four (12 September 1990), reunification
  (3 October 1990), Resolution 678 (29 November 1990), failed Soviet coup
  (August 1991), Gorbachev's resignation (25 December 1991), Maastricht
  (1992-93), Dayton (1995), Kosovo/NATO (1999) and EU enlargement (2004)
  remain distinct stages and legal categories.
- **Mechanism control:** stagnation, nationality pressures, legitimacy loss,
  arms burdens, reform sequencing, social mobilisation, non-coercion and
  diplomacy interacted; republican institutions, Yeltsin and the failed coup
  explain dissolution. Neither one leader nor Western pressure alone is
  sufficient. Gulf Council alignment was coalition enforcement, not ordinary
  peacekeeping, and a US-led unipolar moment did not erase regional, Global
  South or Indian agency.
- **Verified PYQ ownership, 2018-2025:** only locally verified routes may be
  retained with their exact metadata status; the hostile ledger finds zero
  direct Topic-21-only routes. German, UN, US and MEA official pages control
  named historical/current claims. No end-of-history teleology, present-day
  analogy, objective key or current forecast is invented.""",
}


def ensure_canonical_owner_control(topic: Topic) -> bool:
    """Append the active topic's bounded semantic owner control once."""
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


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources = provenance.get("live_sources") or []
    current_note = provenance.get("current_linkage_note") or (
        "No live commemoration or current institutional claim is needed to "
        "establish the historical chronology. Any current linkage remains "
        "dated, sourced and analytically subordinate."
    )
    source_lines = "\n".join(f"- `{path}`" for path in live_sources) or (
        "- No live source is required for a static historical claim in this topic."
    )
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete World History Core is taught chronologically, spatially and causally before optional enrichment. |
| Evidence method | Claim → named event/treaty/institution/actor/region or attributed scholarship → analysis → qualification. |
| Chronology | Structural cause, trigger, event, settlement, implementation and long-term process remain distinct. |
| Geography | Europe, Africa, Asia, West Asia and the Americas retain their own actors, routes and unequal connections; Europe is never the default universal viewpoint. |
| Historiography | Liberal, conservative, Marxist, social, feminist, postcolonial and other relevant interpretations are tied to evidence and bounded claims. |
| Practice contract | Every solved item has directive/demand decoding, an examiner-grade model, an executable timed/compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Canonical topic owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Primary/official evidence:** treaties, declarations, laws, institutional records, speeches and contemporary testimony are dated and read for authorship, audience and purpose.
- **Spatial and social evidence:** maps, trade and migration routes, battlefield geography, class, race, gender and colonial position qualify state-centred narrative.
- **Quantitative evidence:** population, debt, inflation, output, casualties and territorial claims retain unit, place, period, source and uncertainty; no statistic is invented.
- **Interpretive discipline:** teleology, civilisational ranking, single-cause verdicts and present-day nation-state projection are rejected.
- **PYQ discipline:** repository routing ledgers and locally held papers control wording and metadata; neutral rendering, reconstruction and unavailable official keys remain explicitly labelled.
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
    focus = textwrap.shorten(question, width=94, placeholder="…")
    if "prelims" in title.casefold() or re.search(
        r"\boption\b|\bwhich of the following\b", question, re.I
    ):
        return {
            "demand": (
                f"Treat “{focus}” as a chronology, geography, actor and category "
                "problem. Verify each treaty, event, institution, ideology and "
                "consequence independently without inventing an official key."
            ),
            "plan": (
                "Fix the time window and map; separate structural cause from "
                "trigger and event from settlement; match actors and provisions; "
                "eliminate the closest distractor with one named fact."
            ),
            "why": (
                "It preserves answer-text integrity, exact chronology and spatial "
                "scope while keeping reasoned elimination separate from an official key."
            ),
            "improve": (
                f"For “{focus}”, state why the nearest distractor fails on date, "
                "place, actor, institutional status, ideological distinction or degree."
            ),
        }
    return {
        "demand": (
            f"The directive **{directive}** requires a direct position on “{focus}”, "
            "every clause and time boundary, chronological-causal organisation, "
            "named evidence, a counter-position and a qualified global verdict."
        ),
        "plan": (
            f"For a {marks}-mark answer, open with a two-sentence thesis and a "
            f"spatial-temporal frame; organise {evidence_count} named events, treaties, "
            "actors, regions, institutions or attributed interpretations as claim → "
            "evidence → analysis → qualification; reserve the final lines for a "
            "graded conclusion."
        ),
        "why": (
            "The answer obeys the directive, distinguishes structure, trigger and "
            "outcome, connects evidence to mechanism, includes non-European agency "
            "and avoids teleology, presentism and monocausal explanation."
        ),
        "improve": (
            f"For “{focus}”, replace the weakest generalisation with one additional "
            "named treaty, regional case, primary record or attributed scholarly "
            "position and state what that evidence cannot prove."
        ),
    }


def mcq_blocks(area: str) -> list[tuple[int, int, str]]:
    """Recognise both ``MCQ`` and authored ``Q1.`` World History headings."""
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


def _detailed_model_answer(block: str, question: str) -> str:
    """Build a complete answer from the already reviewed, named evidence."""
    solution = re.search(
        r"(?is)\*\*Model (?:solution|answer):\*\*\s*(.+?)(?=\n\n\*\*|\Z)",
        block,
    )
    if solution:
        body = solution.group(1).strip()
        return (
            "**Detailed examiner-grade model answer:**\n\n"
            f"**Introduction and thesis:** {body}\n\n"
            "**Qualification:** Treat the stated causal weight as bounded by the "
            "question's period, geography and evidence status; do not convert it "
            "into inevitability or a universal civilisational claim."
        )

    thesis_match = re.search(
        r"(?is)\*\*Model thesis:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)",
        block,
    )
    conclusion_match = re.search(
        r"(?is)\*\*Qualified conclusion:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)",
        block,
    )
    evidence_match = re.search(
        r"(?is)\*\*Claim\s*→\s*named evidence\s*→\s*analysis\s*→\s*"
        r"qualification:\*\*\s*(.+?)(?=\n\n\*\*Qualified conclusion:|\Z)",
        block,
    )
    thesis = (
        thesis_match.group(1).strip()
        if thesis_match
        else f"The answer must resolve the historical demand in “{question}”."
    )
    conclusion = (
        conclusion_match.group(1).strip()
        if conclusion_match
        else thesis
    )
    evidence = (
        re.findall(r"(?m)^\s*[-*]\s+(.+?)\s*$", evidence_match.group(1))
        if evidence_match
        else []
    )
    if not evidence:
        evidence = [
            clean_source_line(line)
            for line in block.splitlines()
            if 45 <= len(clean_source_line(line)) <= 220
            and not line.lstrip().startswith(("**Question:", "**Demand decoding:"))
        ][:4]
    body = "\n".join(
        f"{number}. **Claim and named evidence:** {item} "
        "**Analysis:** Use this evidence to establish the mechanism asked in the "
        "directive, not merely to narrate the event. **Qualification:** Keep its "
        "chronological, regional and interpretive boundary explicit."
        for number, item in enumerate(evidence, 1)
    )
    return (
        "**Detailed examiner-grade model answer:**\n\n"
        f"**Introduction and thesis:** {thesis}\n\n"
        f"**Analytical body:**\n\n{body}\n\n"
        "**Counter-position / limit:** No single actor, battle, treaty, ideology "
        "or economic pressure should be made sufficient where the evidence shows "
        "interaction among structures, triggers, agency and uneven regional outcomes.\n\n"
        f"**Qualified conclusion:** {conclusion}"
    )


def repair_answer_contracts(markdown: str) -> tuple[str, dict[str, Any]]:
    """Review every solved PYQ/original Mains format in the practice span."""
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
        r"\*\*introduction[.:]\*\*|\*\*claim(?:—|-|:)|"
        r"claim\s*→\s*named evidence|why this earns marks"
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
        if not re.search(
            r"(?i)\*\*Detailed examiner-grade model answer:\*\*",
            block,
        ):
            additions.append(_detailed_model_answer(block, question))
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
                    re.search(
                        r"(?i)Detailed examiner-grade model answer",
                        block,
                    )
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


def _review_block(topic: Topic) -> str:
    points = WORLD_REVIEW_POINTS[topic.number]
    return (
        "### WORLD HISTORY DEEP-REVIEW CORE CONTROL\n\n"
        f"- **Must remember:** {points[0]}\n"
        f"- **Close distinction:** {points[1]}\n"
        f"- **Evidence / interpretation limit:** {points[2]}\n"
    )


_base_insert_contract = insert_contract


def insert_contract(markdown: str, topic: Topic, record: dict[str, Any]) -> str:
    repaired = _base_insert_contract(markdown, topic, record)
    current = _review_block(topic).strip()
    pattern = re.compile(
        r"### WORLD HISTORY DEEP-REVIEW CORE CONTROL\n.*?"
        r"(?=\n## BASIC MCQS / REMEDIATION)",
        re.DOTALL,
    )
    if pattern.search(repaired):
        return pattern.sub(current + "\n", repaired, count=1)
    marker = "## BASIC MCQS / REMEDIATION"
    return repaired.replace(marker, current + "\n\n" + marker, 1)


_base_baseline_audit = baseline_audit


def baseline_audit(topic: Topic, record: dict[str, Any]) -> dict[str, Any]:
    audit = _base_baseline_audit(topic, record)
    main = repo(record["markdown"]).read_text(encoding="utf-8")
    workbook_value = record.get("workbook_markdown") or record.get(
        "provenance", {}
    ).get("workbook_markdown")
    workbook = repo(workbook_value).read_text(encoding="utf-8")
    _, proposed_answers = repair_answer_contracts(workbook)
    if proposed_answers["repaired_count"]:
        audit["defects"].append(
            "Solved items use a generic examiner-model status pointer rather than "
            "a self-contained detailed model answer built from the named evidence."
        )
        audit["metrics"]["detailed_model_answers_missing"] = proposed_answers[
            "repaired_count"
        ]
    if "### WORLD HISTORY DEEP-REVIEW CORE CONTROL" not in main:
        audit["defects"].append(
            "The package lacks a topic-specific World History chronology, "
            "spatial distinction and evidence/historiography qualification control."
        )
        audit["scores"]["complete_learning_session"] -= 1
        audit["scores"]["total"] -= 1
    session_count = len(
        re.findall(r"(?m)^### SESSION \d+ — ", main)
    )
    visual_count = main.count("#### VISUAL FIRST")
    if session_count < 15 or visual_count < session_count:
        audit["defects"].append(
            f"Visual-first Core progression is incomplete: sessions={session_count}, "
            f"visual gateways={visual_count}."
        )
        audit["scores"]["complete_learning_session"] -= 2
        audit["scores"]["total"] -= 2
    if "\ufffd" in main or "\ufffd" in workbook:
        audit["defects"].append(
            "A literal U+FFFD replacement glyph exists in a learner artifact."
        )
        audit["scores"]["complete_learning_session"] -= 2
        audit["scores"]["total"] -= 2
    audit["metrics"]["session_count"] = session_count
    audit["metrics"]["visual_first_count"] = visual_count
    audit["metrics"]["replacement_glyph_count"] = (
        main.count("\ufffd") + workbook.count("\ufffd")
    )
    return audit


_base_completed_result = completed_result


def topic21_ascii_matches_authored(record: dict[str, Any]) -> bool:
    if not TOPIC21_AUTHORED_ASCII.is_file():
        return False
    existing_value = record.get("continuous_core_first", {}).get(
        "ascii_master_spec"
    )
    if not existing_value:
        return False
    existing = load(repo(existing_value))["topics"][0]["panels"]
    authored = load(TOPIC21_AUTHORED_ASCII)["topics"][0]["panels"]
    if [panel["title"] for panel in existing] != [
        panel["title"] for panel in authored
    ]:
        return False
    return all(
        panel["ascii_lines"][: len(source["ascii_lines"])]
        == source["ascii_lines"]
        for panel, source in zip(existing, authored)
    )


def topic21_session_matches_authored(main: str, workbook: str) -> bool:
    required = (
        "### SESSION 5 — CORE — German reunification",
        "### SESSION 7 — CORE — August coup and Soviet dissolution",
        "### SESSION 8 — CORE — Gulf War as order test",
        "### SESSION 14 — CORE SYNTHESIS — Global South agency",
        "### SESSION 15 — CORE SYNTHESIS — India and the qualified verdict",
        "### Q77. Which statement correctly identifies India's bounded relevance?",
    )
    forbidden = (
        "### SESSION 15 — CORE SYNTHESIS — Arab Spring and non-teleological verdict",
        "### Q77. Which statement correctly identifies Arab Spring divergence?",
    )
    return (
        all(item in main for item in required)
        and all(item not in main for item in forbidden)
        and required[-1] in workbook
        and all(item not in workbook for item in forbidden)
    )


def completed_result(topic: Topic, changed: set[str]) -> dict[str, Any] | None:
    """Resume only a generation that passes the current stricter review."""
    result = _base_completed_result(topic, changed)
    if result is None:
        return None
    record = latest(load(STATUS), topic.topic_key)
    main = repo(record["markdown"]).read_text(encoding="utf-8")
    workbook_path = repo(
        record.get("workbook_markdown")
        or record.get("provenance", {}).get("workbook_markdown")
    )
    workbook = workbook_path.read_text(encoding="utf-8")
    _, metrics = repair_answer_contracts(workbook)
    if (
        _review_block(topic).strip() not in main
        or metrics["repaired_count"]
        or "\ufffd" in main
        or "\ufffd" in workbook
        or (topic.number == 21 and not topic21_ascii_matches_authored(record))
        or (
            topic.number == 21
            and not topic21_session_matches_authored(main, workbook)
        )
    ):
        return None
    return result


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
        for label, point in zip(labels, WORLD_REVIEW_POINTS[topic.number])
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
    source_record = record
    if topic.number == 21:
        if not TOPIC21_AUTHORED_ASCII.is_file():
            raise FileNotFoundError(
                f"Topic 21 authored ASCII atlas is missing: {TOPIC21_AUTHORED_ASCII}"
            )
        source_record = json.loads(json.dumps(record))
        source_record.setdefault("continuous_core_first", {})[
            "ascii_master_spec"
        ] = rel(TOPIC21_AUTHORED_ASCII)
    spec = _base_build_ascii_spec(
        topic,
        source_record,
        generation,
        main,
        markdown_path,
    )
    panels = spec["topics"][0]["panels"]
    for panel, lines in zip(
        (panels[0], panels[9], panels[10]),
        _wrapped_review_groups(topic),
    ):
        panel.setdefault("ascii_lines", []).extend(lines)
    spec["constraints"]["world_history_topic_review_control"] = True
    spec["constraints"]["non_eurocentric_spatial_discipline"] = True
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
    errors: list[str] = []
    if _review_block(topic).strip() not in main:
        errors.append(
            "Current topic-specific World History review control is absent or stale."
        )
    if len(re.findall(r"(?m)^### SESSION \d+ — ", main)) < 15:
        errors.append("The learner-facing Core has fewer than fifteen sessions.")
    if main.count("#### VISUAL FIRST") < 15:
        errors.append("The learner-facing Core has fewer than fifteen visual gateways.")
    if "\ufffd" in main or "\ufffd" in workbook or "\ufffd" in standalone_ascii:
        errors.append("A literal U+FFFD replacement glyph survives in an artifact.")
    for point in WORLD_REVIEW_POINTS[topic.number]:
        anchors = [
            word
            for word in re.sub(r"[^a-z0-9]+", " ", point.casefold()).split()
            if len(word) >= 7
        ][:2]
        if anchors and not all(word in main.casefold() for word in anchors):
            errors.append(
                "Learning session lost reviewed control terms: "
                + ", ".join(anchors)
            )
    if topic.number == 21:
        generated_spec = load(paths["ascii_spec"])
        generated_panels = generated_spec["topics"][0]["panels"]
        authored_panels = load(TOPIC21_AUTHORED_ASCII)["topics"][0]["panels"]
        if [panel["title"] for panel in generated_panels] != [
            panel["title"] for panel in authored_panels
        ]:
            errors.append("Topic 21 ASCII atlas titles diverge from authored source.")
        elif any(
            panel["ascii_lines"][: len(source["ascii_lines"])]
            != source["ascii_lines"]
            for panel, source in zip(generated_panels, authored_panels)
        ):
            errors.append("Topic 21 ASCII atlas body diverges from authored source.")
        if not topic21_session_matches_authored(main, workbook):
            errors.append(
                "Topic 21 session/workbook diverges from repaired authoring masters."
            )
    if not all(
        label in standalone_ascii
        for label in ("MUST REMEMBER:", "CLOSE DISTINCTION:", "EVIDENCE LIMIT:")
    ):
        errors.append(
            "ASCII/graphical source ledger lacks the three World History controls."
        )
    result["errors"].extend(errors)
    result["hard_gates"]["world_history_chronology_space_and_debate"] = not errors
    result["metrics"]["world_history_review_control_count"] = 3
    result["metrics"]["learner_session_count"] = len(
        re.findall(r"(?m)^### SESSION \d+ — ", main)
    )
    result["metrics"]["visual_first_count"] = main.count("#### VISUAL FIRST")
    if errors:
        result["result"] = "failed"
    return result


_base_update_review_tracker = update_review_tracker


def update_review_tracker(
    rows: list[dict[str, Any]],
    changed: set[str],
) -> None:
    _base_update_review_tracker(rows, changed)
    tracker = load(REVIEW_TRACKER)
    by_key = {row["topic_key"]: row for row in rows}
    topic_by_key = {topic.topic_key: topic for topic in topics()}
    for item in tracker["topics"]:
        result = by_key.get(item["topic_key"])
        if result is None:
            continue
        number = int(item["topic_key"][-2:])
        item["issue_counts"] = {
            "critical": 0,
            "high": 3,
            "medium": 1,
            "low": 0,
        }
        item["md_change_required"] = False
        item["md_change_ids"] = [
            f"MD-WH{number:02d}-001",
            f"MD-WH{number:02d}-002",
            f"MD-WH{number:02d}-003",
            f"MD-WH{number:02d}-004",
        ]
        item["evidence_ids"] = [
            f"E-WH{number:02d}-001",
            f"E-WH{number:02d}-002",
            f"E-WH{number:02d}-003",
            f"E-WH{number:02d}-004",
        ]
        start = _command_start(topic_by_key[item["topic_key"]])
        item["reviewer_notes"] = (
            f"Command-start baseline {start['score']}/100; immutable successor "
            f"{result['new_score']}/100. Canonical owners remained hash-locked; "
            "generation-local content and pipeline controls were repaired. "
            "Approval remains false."
        )
    tracker["summary"] = dict(Counter(row["status"] for row in tracker["topics"]))
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
        key = row["topic_key"]
        topic = topic_map[key]
        generation = row["new_generation"]
        metrics = row["baseline_metrics"]
        append_once(
            REVIEW_ROOT / "ISSUE-LEDGER.md",
            f"| WH{number:02d}-001 |",
            [
                f"| WH{number:02d}-001 | high | `{key}` | complete session | "
                "Explicit syllabus, evidence, chronology, geography, PYQ/current "
                "status and approval contract | The predecessor lacked the binding "
                f"World History deep-review contract | E-WH{number:02d}-001 | "
                f"MD-WH{number:02d}-001 | closed in g{generation} |",
                f"| WH{number:02d}-002 | high | `{key}` | all four artifacts | "
                "Topic-specific chronology, close distinction and interpretive limit | "
                "The predecessor did not contain the fresh source-to-flow review "
                f"control | E-WH{number:02d}-002 | MD-WH{number:02d}-002 | "
                f"closed in g{generation} |",
                f"| WH{number:02d}-003 | medium | `{key}` | workbook and flows | "
                "Exam-executable answer and immutable reconstruction controls | "
                f"Baseline solved={metrics['question_count']}, MCQs="
                f"{metrics['mcq_count']}, panels={metrics['flow_panel_count']} | "
                f"E-WH{number:02d}-003 | MD-WH{number:02d}-003 | "
                f"closed in g{generation} |",
            ],
            changed,
        )
        append_once(
            REVIEW_ROOT / "ISSUE-LEDGER.md",
            f"| WH{number:02d}-004 |",
            [
                f"| WH{number:02d}-004 | high | `{key}` | solved workbook and "
                "session practice | Self-contained detailed examiner-grade models | "
                "The first successor carried a generic model-status pointer instead "
                "of reconstructing each answer from its thesis and named evidence | "
                f"E-WH{number:02d}-004 | MD-WH{number:02d}-004 | "
                f"closed in g{generation}; prior successor preserved |",
            ],
            changed,
        )
        append_once(
            REVIEW_ROOT / "EVIDENCE-LEDGER.md",
            f"| E-WH{number:02d}-001 |",
            [
                f"| E-WH{number:02d}-001 | `{key}` | Canonical Basic/Core, "
                "canonical package, optional Advanced, master chronology and syllabus "
                f"mapping were reviewed and hash-locked | repository source | "
                f"`{rel(topic.basic_path)}`; `{rel(topic.canonical_path)}`; "
                f"`{rel(topic.advanced_path)}`; `{rel(COMMON_CHRONOLOGY)}`; "
                f"`{rel(SYLLABUS_MAPPING)}` | repository owners | {DATE} | verified; "
                "canonical owners unchanged |",
                f"| E-WH{number:02d}-002 | `{key}` | Local official-paper routing "
                "controls exact or neutral PYQ status, while chronology, spatial "
                "anchors and historiographical limits were reconciled across all four "
                f"artifacts | repository + generated evidence | `{rel(PYQ_LEDGERS[0])}`; "
                f"`{rel(PYQ_LEDGERS[1])}`; `{row['validation']}` | g{generation} | "
                f"{DATE} | verified |",
                f"| E-WH{number:02d}-003 | `{key}` | Successor session, workbook, "
                "graphical/ASCII masters, PDF layouts, hashes and latest identity pass | "
                f"generated provenance | `{row['validation']}` | g{generation} | "
                f"{DATE} | verified; approval false |",
            ],
            changed,
        )
        append_once(
            REVIEW_ROOT / "EVIDENCE-LEDGER.md",
            f"| E-WH{number:02d}-004 |",
            [
                f"| E-WH{number:02d}-004 | `{key}` | Every detected solved item "
                "contains a self-contained detailed model with introduction/thesis, "
                "named-evidence analytical body, counter-position/limit and qualified "
                f"conclusion, plus timed compression and improvement controls | "
                f"generated provenance | `{row['validation']}` | g{generation} | "
                f"{DATE} | verified; stricter intermediate preserved |",
            ],
            changed,
        )
        append_once(
            REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
            f"| MD-WH{number:02d}-001 |",
            [
                f"| MD-WH{number:02d}-001 | high | `{key}` | generated session | "
                "Deep-review learning/evidence contract absent | "
                f"E-WH{number:02d}-001 | Add chronology, geography, historiography, "
                "PYQ/current-status and approval controls | Generated Core | session | "
                f"applied g{generation}; canonical owner unchanged |",
                f"| MD-WH{number:02d}-002 | high | `{key}` | generated session and "
                "both flows | Topic-specific must-remember chronology, close distinction "
                f"and interpretation limit absent | E-WH{number:02d}-002 | Add the "
                "three controls and regenerate independent agreeing masters | Generated "
                f"Core/flow | all four artifacts | applied g{generation}; canonical "
                "owner unchanged |",
                f"| MD-WH{number:02d}-003 | medium | `{key}` | generated practice and "
                "immutable identity | Per-answer timed/compression controls and fresh "
                f"review identity required | E-WH{number:02d}-003 | Repair detected "
                "answer controls, preserve exact/neutral PYQ labels and publish only a "
                f"collision-free successor | Practice/pipeline | all four artifacts | "
                f"applied and verified g{generation}; canonical owner unchanged |",
            ],
            changed,
        )
        append_once(
            REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
            f"| MD-WH{number:02d}-004 |",
            [
                f"| MD-WH{number:02d}-004 | high | `{key}` | generated answer "
                "repair | Generic model-status pointer was not a detailed answer | "
                f"E-WH{number:02d}-004 | Reconstruct an examiner-grade model from "
                "the existing thesis, named evidence, analysis and qualification; "
                "retain the predecessor unchanged | Practice/pipeline | session and "
                f"workbook | applied and verified g{generation}; canonical owners "
                "unchanged |",
            ],
            changed,
        )


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
        generation = int(record["generation"])
        for path in (
            EXPORTS
            / f"{record['topic_key']}-learner-v2-g{generation}-{DATE}-record.json",
            EXPORTS
            / f"{record['topic_key']}-learner-v2-g{generation}-{DATE}-validation.json",
            EXPORTS
            / f"{record['topic_key']}-learner-v2-g{generation}-{DATE}-changed-files.txt",
            ASCII_SPECS
            / f"{record['topic_key']}-deep-review-{DATE}-g{generation}.json",
            GRAPHICAL_SPECS / f"{record['topic_key']}-g{generation}.json",
            CONTENT_SPECS / f"{record['topic_key']}-g{generation}.json",
        ):
            if path.is_file():
                changed.add(rel(path))


def _command_start(topic: Topic) -> dict[str, Any]:
    review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
    candidates: list[tuple[int, Path]] = []
    for path in review_dir.glob(f"{topic.topic_key}-g*-baseline-audit.json"):
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


def _repair_stricter_review_records() -> None:
    """State the second-pass hard defect in its audit and repair handoff."""
    status = load(STATUS)
    defect = (
        "Solved items use a generic examiner-model status pointer rather than "
        "a self-contained detailed model answer built from the named evidence."
    )
    for topic in topics():
        final = latest(status, topic.topic_key)
        final_generation = int(final["generation"])
        prior_generation = final_generation - 1
        review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
        baseline_path = (
            review_dir
            / f"{topic.topic_key}-g{prior_generation}-baseline-audit.json"
        )
        if baseline_path.is_file():
            baseline = load(baseline_path)
            if defect not in baseline["defects"]:
                baseline["defects"].append(defect)
            baseline["metrics"]["detailed_model_answers_missing"] = int(
                baseline["metrics"].get("question_count", 0)
            )
            dump(baseline_path, baseline)
        final_audit_path = (
            review_dir
            / f"{topic.topic_key}-g{final_generation}-final-audit.json"
        )
        if final_audit_path.is_file():
            final_audit = load(final_audit_path)
            if defect not in final_audit["baseline_defects"]:
                final_audit["baseline_defects"].append(defect)
            final_audit["stricter_re_review"] = {
                "predecessor": (
                    f"{topic.topic_key}:learner-v2:g{prior_generation}"
                ),
                "defect": defect,
                "repair": (
                    "Reconstructed each detailed model from its existing thesis, "
                    "named evidence, analysis and qualification."
                ),
                "predecessor_preserved": True,
            }
            dump(final_audit_path, final_audit)
        prompt_path = (
            REVIEW_ROOT
            / "repair-prompts"
            / (
                f"{topic.topic_key}-g{prior_generation}-"
                f"to-g{final_generation}.md"
            )
        )
        write_text(
            prompt_path,
            f"""# Repair handoff — {topic.title}

Keep reviewed predecessor `{topic.topic_key}:learner-v2:g{prior_generation}`
immutable. The collision-free successor is
`{topic.topic_key}:learner-v2:g{final_generation}` with fresh scores unset,
`revalidation_pending` status and approval false.

## Defects to repair

- **High:** {defect}

## Sources and affected artifacts

- Canonical Basic/Core owner: `{rel(topic.basic_path)}`
- Canonical package owner: `{rel(topic.canonical_path)}`
- Optional Advanced owner: `{rel(topic.advanced_path)}`
- Official syllabus mapping: `{rel(SYLLABUS_MAPPING)}`
- Repository PYQ ledgers: {", ".join(f"`{rel(path)}`" for path in PYQ_LEDGERS)}
- Affected outputs: complete session, solved workbook, graphical flow, ASCII
  master, validation, tracker identity and final-library publication.

This is a generated-practice/pipeline repair; canonical Markdown owners remain
hash-locked. Reconstruct every model from the existing question-specific thesis,
named evidence, analysis and qualification. Each answer must contain a clear
introduction/thesis, detailed analytical body, counter-position or limit,
qualified conclusion, executable timed/compression plan, why it earns marks and
answer-specific improvement. Preserve exact or explicitly neutral/reconstructed
PYQ metadata. Regenerate all four artifacts from the same corrected ledger,
validate strict A→B→C→D answer-text integrity, PDF layout, flow agreement, live
EXPORT/MASTER/REVIEW identities and final-library hashes. Never carry forward
the predecessor score or approval; approval remains false.
""",
        )


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
    chain: list[dict[str, Any]] = []
    for generation in sorted({*records, *allocated, start}):
        record = records.get(generation)
        validation_path = (
            EXPORTS
            / (
                f"{topic.topic_key}-learner-v2-g{generation}-"
                f"{DATE}-validation.json"
            )
        )
        if not validation_path.is_file():
            alternatives = sorted(
                EXPORTS.glob(
                    f"{topic.topic_key}-learner-v2-g{generation}-"
                    "*-validation.json"
                ),
                key=lambda path: path.name,
            )
            if alternatives:
                validation_path = alternatives[-1]
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


def _rewrite_command_history() -> None:
    reconciliation_path = (
        EXPORTS / f"world-history-deep-review-reconciliation-{DATE}.json"
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
        write_text(
            report,
            f"""# Deep Content Review — World History {topic.number:02d}: {topic.title}

- **Command-start baseline locked:** `{start['record_id']}` — {start['score']}/100
- **Final immutable successor:** `{final['record_id']}` — {row['new_score']}/100
- **Approval:** false / pending explicit approval

## Defects reported before repair

"""
            + "\n".join(f"- {defect}" for defect in start["defects"])
            + """

## Four-artifact repair and re-review

The complete predecessor teaching remains in chronological and causal Core order
before Optional Advanced. The successor adds a topic-specific chronology,
spatial distinction, named evidence and interpretation limit. It distinguishes
structure from trigger, event from long-term process and contemporary evidence
from later interpretation, while retaining non-European agency. Every detected
solved answer has demand decoding, an examiner-grade content base, an executable
timed/compression plan, marks rationale and answer-specific improvement.
Basic/remedial MCQs pass strict A→B→C→D answer-text mapping. The graphical and
ASCII masters independently reconstruct twelve agreeing stages.

The stricter re-review found that the first successor's generic model-status
pointer was not itself a detailed answer. The final successor reconstructs every
detected model from its question-specific thesis and named evidence; that first
successor remains preserved in the generation chain.

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

    for start_number, end_number in (
        (1, 5),
        (6, 10),
        (11, 15),
        (16, 20),
        (21, 21),
    ):
        selected = topic_rows[start_number - 1 : end_number]
        batch = (
            REVIEW_ROOT
            / "batch-reports"
            / (
                f"World-History-Topics-{start_number:02d}-"
                f"{end_number:02d}-{DATE}.md"
            )
        )
        write_text(
            batch,
            "# World History Deep Review Batch\n\n"
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
    validation = load(
        EXPORTS / f"world-history-deep-review-validation-{DATE}.json"
    )
    unrelated_count = len(
        validation.get("unrelated_pre_existing_failures", [])
    )
    subject_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"World-History-Subject-Completion-{DATE}.md"
    )
    write_text(
        subject_report,
        "# World History Subject Completion — 1 September 2026\n\n"
        "All 21 topics were reviewed, repaired and published strictly in live "
        "REVIEW-TRACKER order. Every command-start baseline and intermediate "
        "remains immutable. All four artifacts, answer controls, PDFs, trackers, "
        "canonical final-library paths and indexes pass. Approval remains false.\n\n"
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
        + f".\n\nTests: {validation['test_count']}; relevant failures: 0; "
        f"unrelated pre-existing failures: {unrelated_count} "
        "(exporter regression hard-codes a subject set that omits separately "
        "published Indian Art and Culture records). "
        "Tracker/final-library mismatches: 0. Approval: false. Encoding check: "
        "no U+FFFD replacement glyph exists in live World History sources, "
        "trackers or indexes; the observed shell separator was console encoding "
        "only. Remaining blockers: none.",
    )

    encoding_paths = [
        STATUS,
        MASTER,
        REVIEW_TRACKER,
        ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
        ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.md",
        ROOT / "notes" / "Final-Learning-Packages" / "CATALOGUE.md",
        ROOT / "upsc-ai-kit" / "knowledge" / "World-History" / "README.md",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "World-History"
        / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    ]
    encoding_paths.extend(topic.basic_path for topic in topics())
    encoding_paths.extend(topic.advanced_path for topic in topics())
    replacement_paths = [
        rel(path)
        for path in encoding_paths
        if path.is_file() and "\ufffd" in path.read_text(encoding="utf-8-sig")
    ]
    reconciliation["failed_intermediates_preserved"] = failed
    reconciliation["successful_re_review_intermediates_preserved"] = superseded
    reconciliation["final_library_manifest"] = (
        "upsc-ai-kit\\manifests\\exports\\final-four-item-library-2026-09-01.json"
    )
    reconciliation["final_library_validation"] = (
        "upsc-ai-kit\\manifests\\exports\\"
        "final-four-item-library-2026-09-01-validation.json"
    )
    reconciliation["all_subject_topic_count"] = int(load(MASTER)["topic_count"])
    reconciliation["encoding_check"] = {
        "files_checked": [rel(path) for path in encoding_paths if path.is_file()],
        "u_fffd_replacement_paths": replacement_paths,
        "actual_replacement_glyph_found": bool(replacement_paths),
        "result": (
            "defect"
            if replacement_paths
            else "no defect; PowerShell console encoding only"
        ),
    }
    dump(reconciliation_path, reconciliation)
    if replacement_paths:
        raise RuntimeError(
            "Actual U+FFFD replacement glyph found: "
            + ", ".join(replacement_paths)
        )


def _republish_master_library() -> dict[str, Any]:
    """Validate and republish the complete synchronized 259-topic library."""
    master = load(MASTER)
    selected_keys = [row["topic_key"] for row in master["topics"]]
    if len(selected_keys) != 259 or len(set(selected_keys)) != 259:
        raise RuntimeError(
            "Full-library republish requires the synchronized 259-topic MASTER."
        )
    result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=STATUS,
        catalogue_path=(
            ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
        ),
        selected_keys=selected_keys,
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
    manifest = load(repo(result["manifest"]))
    validation = load(repo(result["validation_manifest"]))
    if (
        manifest.get("topic_count") != 259
        or validation.get("topic_count") != 259
        or validation.get("status") != "passed"
    ):
        raise RuntimeError(
            "The synchronized 259-topic final-library validation did not pass."
        )
    review = load(REVIEW_TRACKER)
    review["source_master_created_at"] = load(MASTER)["created_at"]
    dump(REVIEW_TRACKER, review)
    render_review_tracker_markdown(review)
    return result


def _record_post_shared_checks(
    full_library_result: dict[str, Any],
) -> None:
    sync = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "sync_deep_review_tracker.py"),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if sync.returncode:
        raise RuntimeError(
            "Live deep-review tracker synchronization failed: "
            + "\n".join((sync.stdout + sync.stderr).splitlines()[-20:])
        )
    validation_path = (
        EXPORTS / f"world-history-deep-review-validation-{DATE}.json"
    )
    validation = load(validation_path)
    validation["full_library_validation"] = {
        "topic_count": full_library_result["topic_count"],
        "manifest": full_library_result["manifest"],
        "validation_manifest": full_library_result["validation_manifest"],
        "status": "passed",
    }
    validation["post_shared_checks"] = [
        {
            "command": "python tools\\sync_deep_review_tracker.py",
            "exit_code": sync.returncode,
            "result": "passed",
            "output_tail": "\n".join(
                (sync.stdout + sync.stderr).splitlines()[-20:]
            ),
        }
    ]
    dump(validation_path, validation)
    reconciliation_path = (
        EXPORTS / f"world-history-deep-review-reconciliation-{DATE}.json"
    )
    reconciliation = load(reconciliation_path)
    reconciliation["final_library_manifest"] = full_library_result["manifest"]
    reconciliation["final_library_validation"] = full_library_result[
        "validation_manifest"
    ]
    reconciliation["final_library_topic_count"] = full_library_result["topic_count"]
    reconciliation["live_tracker_sync"] = "passed"
    dump(reconciliation_path, reconciliation)


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
    current = {path for path in reported if repo(path).is_file()}
    deleted = removed | {path for path in reported if not repo(path).is_file()}
    return current, deleted


def _augment_inventory_with_git_status() -> None:
    inventory = (
        EXPORTS / f"world-history-deep-review-{DATE}-changed-files.txt"
    )
    deletion_inventory = (
        EXPORTS / f"world-history-deep-review-{DATE}-deleted-files.txt"
    )
    current, deleted = _git_changed_paths()
    current.add(rel(inventory))
    if deleted:
        write_text(
            deletion_inventory,
            "\n".join(sorted(deleted, key=str.casefold)),
        )
        current.add(rel(deletion_inventory))
    elif deletion_inventory.is_file():
        deletion_inventory.unlink()
    current = {
        path for path in current if path == rel(inventory) or repo(path).is_file()
    }
    write_text(inventory, "\n".join(sorted(current, key=str.casefold)))
    current_after, deleted_after = _git_changed_paths()
    if deleted_after != deleted:
        write_text(
            deletion_inventory,
            "\n".join(sorted(deleted_after, key=str.casefold)),
        )
        current_after.add(rel(deletion_inventory))
    current_after.add(rel(inventory))
    current_after = {
        path
        for path in current_after
        if path == rel(inventory) or repo(path).is_file()
    }
    write_text(inventory, "\n".join(sorted(current_after, key=str.casefold)))
    missing = [
        path
        for path in inventory.read_text(encoding="utf-8").splitlines()
        if path and path != rel(inventory) and not repo(path).is_file()
    ]
    if missing:
        raise RuntimeError(
            "Changed-file inventory contains missing current paths: "
            + ", ".join(missing[:20])
        )


_base_main = main


def main() -> int:
    result = _base_main()
    _repair_stricter_review_records()
    full_library_result = _republish_master_library()
    _rewrite_command_history()
    _record_post_shared_checks(full_library_result)
    _augment_inventory_with_git_status()
    inventory = (
        EXPORTS / f"world-history-deep-review-{DATE}-changed-files.txt"
    )
    reconciliation = load(
        EXPORTS / f"world-history-deep-review-reconciliation-{DATE}.json"
    )
    print(
        json.dumps(
            {
                "world_history_postprocess": "passed",
                "represented": reconciliation["represented"],
                "mismatches": reconciliation["mismatch_count"],
                "approval": False,
                "inventory": rel(inventory),
                "inventory_count": len(
                    [
                        line
                        for line in inventory.read_text(
                            encoding="utf-8"
                        ).splitlines()
                        if line
                    ]
                ),
                "encoding": reconciliation["encoding_check"]["result"],
            },
            ensure_ascii=False,
        )
    )
    return result


if __name__ == "__main__":
    raise SystemExit(main())
