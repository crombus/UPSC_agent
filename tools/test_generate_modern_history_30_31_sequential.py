"""Regression tests for Modern History learner-v2 Topics 30-31."""

from __future__ import annotations

import importlib
import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_26_27_sequential as earlier
import generate_modern_history_28_29_sequential as previous
import generate_modern_history_30_31_sequential as generator
import notions_style_ascii_master as ascii_master


def session_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
        encoding="utf-8"
    )


def workbook_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Solved-Workbook.md").read_text(
        encoding="utf-8"
    )


class ModernHistory3031GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-30", "modern-indian-history-31"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "Linguistic Reorganisation of States & Regionalism "
                "(1947\u20131967)",
                "Integration of the Tribals & National Unity "
                "(1947\u20131987)",
            ],
            [config["title"] for config in generator.TOPICS],
        )
        self.assertTrue(
            all(len(config["facts"]) == 20 for config in generator.TOPICS)
        )
        self.assertTrue(
            all(len(config["traps"]) >= 12 for config in generator.TOPICS)
        )
        self.assertTrue(
            all(len(config["mains"]) == 6 for config in generator.TOPICS)
        )
        self.assertTrue(
            all(
                [item[0] for item in config["mains"]]
                == [10, 10, 15, 15, 20, 20]
                for config in generator.TOPICS
            )
        )
        self.assertTrue(
            all(
                len(generator.SESSION_PLANS[str(config["key"])]) == 15
                for config in generator.TOPICS
            )
        )

    def test_fact_labels_and_statements_are_unique_per_topic(self) -> None:
        for config in generator.TOPICS:
            labels = [label for label, _ in config["facts"]]
            statements = [statement for _, statement in config["facts"]]
            self.assertEqual(20, len(set(labels)), config["key"])
            self.assertEqual(20, len(set(statements)), config["key"])

    def test_mains_evidence_indexes_are_in_range(self) -> None:
        for config in generator.TOPICS:
            for marks, _prompt, _thesis, indexes in config["mains"]:
                self.assertIn(marks, (10, 15, 20))
                for index in indexes:
                    self.assertGreaterEqual(index, 0, config["key"])
                    self.assertLess(index, 20, config["key"])

    def test_canonical_paths_follow_adjacent_package_convention(self) -> None:
        self.assertEqual(
            "30_Linguistic-Reorganisation-of-States-and-Regionalism-"
            "1947-1967_Complete-Topic-Package.md",
            Path(generator.TOPICS[0]["canonical"]).name,
        )
        self.assertEqual(
            "31_Integration-of-the-Tribals-and-National-Unity-1947-1987_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[1]["canonical"]).name,
        )

    def test_owner_files_are_the_declared_sources(self) -> None:
        for config in generator.TOPICS:
            for role in ("basic", "advanced"):
                path = Path(config[role])
                self.assertTrue(path.is_file(), str(path))
                self.assertEqual(role, path.parent.name)
            for extra in config["extra"]:
                self.assertTrue(Path(extra).is_file(), str(extra))

    def test_post_independence_ocr_book_is_a_declared_local_source(
        self,
    ) -> None:
        names = [path.name for path in generator.LOCAL_BOOKS]
        self.assertIn(
            "India After Independence-1947-2000 By Bipan Chandra.pdf", names
        )
        self.assertTrue(all(path.is_file() for path in generator.LOCAL_BOOKS))

    def test_generated_sessions_and_workbooks_pass_contracts(self) -> None:
        for config in generator.TOPICS:
            key = str(config["key"])
            graphical_path = generator.GRAPHICAL_DIR / f"{key}.json"
            markdown = session_markdown(key)
            workbook = workbook_markdown(key)
            sessions = re.findall(
                r"(?m)^### SESSION (\d+) \u2014 (.+?) \u2014 (.+?)\s*$",
                markdown,
            )
            session_mcqs = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)
            workbook_mcqs = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", workbook)
            self.assertEqual(15, len(sessions), key)
            self.assertEqual(80, len(session_mcqs), key)
            self.assertEqual(80, len(set(session_mcqs)), key)
            self.assertEqual(80, len(workbook_mcqs), key)
            self.assertEqual(80, len(set(workbook_mcqs)), key)
            self.assertEqual(
                list("ABCD") * 20,
                re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown),
                key,
            )
            self.assertEqual(
                list("ABCD") * 20,
                re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook),
                key,
            )
            for letter in "ABCD":
                self.assertEqual(
                    20, markdown.count(f"**Answer: {letter}.**"), key
                )
                self.assertEqual(
                    20, workbook.count(f"**Answer: {letter}.**"), key
                )
            self.assertEqual(6, markdown.count("### ORIGINAL MAINS"), key)
            for marks in ("10 MARKS", "15 MARKS", "20 MARKS"):
                self.assertEqual(2, markdown.count(f"- {marks}"), key)
            self.assertEqual(15, markdown.count("#### VISUAL FIRST"), key)
            self.assertEqual(12, markdown.count("```ascii-master"), key)
            self.assertNotRegex(
                markdown, r"(?i)\b(?:todo|placeholder|lorem ipsum)\b"
            )
            self.assertNotIn("an evidence-led unit connecting", markdown)
            self.assertEqual(
                "CONSOLIDATED REGISTER NOTES",
                re.findall(r"(?m)^## (.+?)\s*$", markdown)[-1],
            )
            self.assertEqual(
                Path(config["canonical"]).read_text(encoding="utf-8"),
                markdown,
                key,
            )
            generator.self_check(
                config,
                markdown,
                workbook,
                len(sessions),
                graphical_path,
            )

    def test_learner_v2_section_order_is_exact(self) -> None:
        expected = [
            "BASIC LEARNING SESSION",
            "BASIC MCQS / REMEDIATION",
            "PYQS AND ANSWER PRACTICE",
            "OPTIONAL ADVANCED DEPTH \u2014 NOT REQUIRED FOR A CORE ANSWER",
            "CONSOLIDATED REGISTER NOTES",
        ]
        for config in generator.TOPICS:
            markdown = session_markdown(str(config["key"]))
            headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
            self.assertEqual(
                expected, [item for item in headings if item in expected]
            )

    def test_advanced_owner_depth_is_preserved(self) -> None:
        for config in generator.TOPICS:
            markdown = session_markdown(str(config["key"]))
            advanced = Path(config["advanced"]).read_text(encoding="utf-8")
            block = markdown.split(
                "## OPTIONAL ADVANCED DEPTH \u2014 NOT REQUIRED FOR A CORE "
                "ANSWER"
            )[1]
            for heading in re.findall(r"(?m)^## (.+?)\s*$", advanced):
                if "PYQ" in heading.upper():
                    continue
                self.assertIn(heading, block, config["key"])

    # ---------------- Topic 30 factual safeguards ----------------

    def test_topic30_principle_from_1921_and_timing_caution(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "in 1921 amended its own constitution",
            "reorganise its regional branches on a linguistic basis",
            "27 November 1947",
            "First things must come first",
            "only its timing became contested",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the Congress always opposed linguistic states", markdown
        )

    def test_topic30_dar_and_jvp_advised_delay_with_a_proviso(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "Linguistic Provinces Commission",
            "Justice S.K. Dar",
            "advised against the step",
            "not to incorporate the linguistic principle in the Constitution",
            "December 1948",
            "Jawaharlal Nehru, Sardar Patel and Pattabhi Sitaramayya",
            "insistent and overwhelming",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic30_sriramulu_dates_and_ocr_variant(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "Potti Sriramulu",
            "19 October 1952",
            "fifty-eight days",
            "December 1952",
            "Patti Sriramalu",
            "optical character recognition",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic30_andhra_precedes_commission_and_act(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "October 1953",
            "first linguistic state",
            "October 1955",
            "November 1956",
            "before the States Reorganisation Commission",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the States Reorganisation Commission created the first "
            "linguistic state",
            markdown,
        )

    def test_topic30_commission_members_and_refusals(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "August 1953",
            "Fazl Ali",
            "K.M. Panikkar",
            "Hridaynath Kunzru",
            "October 1955",
            "opposed the splitting of Bombay",
            "did not have a common language",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic30_act_count_and_named_transfers(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "fourteen states and six centrally administered territories",
            "Telangana",
            "Travancore-Cochin",
            "Kutch",
            "Saurashtra",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Bombay was split in 1956", markdown)
        self.assertNotIn("Haryana was created in 1956", markdown)

    def test_topic30_bombay_and_punjab_dates(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "Samyukta Maharashtra Samiti",
            "Maha Gujarat Janata Parishad",
            "C.D. Deshmukh",
            "May 1960",
            "PEPSU",
            "Punjabi Suba",
            "Chandigarh",
            "joint capital",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic30_punjab_communal_reading_is_attributed(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "Akali Dal",
            "Jan Sangh",
            "must always be attributed to the source",
            "never converted into a categorical charge",
            "the Communist Party and a section of the Congress supported",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("the Punjabi Suba demand was purely communal", markdown)
        self.assertNotIn("every supporter of Punjabi was a communalist", markdown)

    def test_topic30_official_language_levels_and_associate_caution(
        self,
    ) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "Article 343",
            "fifteen years from the commencement of the Constitution",
            "Act No. 19 of 1963",
            "10 May 1963",
            "permissive word 'may'",
            "26 January 1965",
            "over sixty lives",
            "16 December 1967",
            "205 votes to 41",
            "three-language formula",
            "not a term used in the Constitution's own text",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "English is the Constitution's associate official language",
            markdown,
        )
        self.assertNotIn(
            "the Constitution calls English the associate official language",
            markdown,
        )
        self.assertNotIn("Hindi became the sole official language in 1965", markdown)

    def test_topic30_regionalism_typology_and_graded_verdict(self) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "Shiv Sena",
            "Bal Thackeray",
            "sons of the soil",
            "accommodative",
            "Rajni Kothari",
            "cementing and integrating influence",
            "defended conclusion",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("linguistic reorganisation weakened India", markdown)

    def test_topic30_current_bridge_uses_only_official_page_claims(
        self,
    ) -> None:
        markdown = session_markdown("modern-indian-history-30")
        required = [
            "Department of Official Language",
            "31 August 2026",
            "Article 343(1)",
            "Article 343(3)",
            "Act No. 19 of 1963",
            "no departmental "
            "programme, event, budget, target or contemporary statistic",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertEqual(
            [
                "https://rajbhasha.gov.in/en/constitutional-provisions",
                "https://rajbhasha.gov.in/en/official-languages-act-1963",
            ],
            generator.TOPICS[0]["live_sources"],
        )

    def test_topic30_pyq_cards_are_routed_demand_summaries(self) -> None:
        topic = generator.TOPICS[0]
        cards = {(item[0], item[1]): item for item in topic["pyq_solutions"]}
        self.assertEqual(
            {("2018", "Mains GS-I Q12"), ("2022", "Mains GS-I Q11")},
            set(cards),
        )
        for card in cards.values():
            self.assertIn("routed-mains-demand-summary-not-verbatim", card[3])
            self.assertIn("_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md", card[2])
            self.assertIsNone(
                re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I), card[1]
            )

    # ---------------- Topic 31 factual safeguards ----------------

    def test_topic31_census_attribution_is_mandatory(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "1971 Census",
            "over 400 tribal communities",
            "nearly 38 million",
            "6.9 per cent",
            "never be presented as 1951 figures or as current data",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the 1951 Census recorded over 400 tribal communities", markdown
        )

    def test_topic31_panchsheel_label_carries_no_proclamation_year(
        self,
    ) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "Tribal Panchsheel",
            "later label",
            "no exact proclamation year",
            "own genius",
            "over-administration",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("the Tribal Panchsheel was proclaimed in", markdown)
        self.assertNotIn("the Tribal Panchsheel of 1952", markdown)

    def test_topic31_integration_not_assimilation(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "Verrier Elwin",
            "museum specimens",
            "engulfed by the masses of Indian humanity",
            "maintaining their distinct identity and culture",
            "progress in their own way",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "Nehru favoured rapid assimilation",
            generator.scannable_text(markdown),
        )
        self.assertNotIn(
            "tribal policy aimed to assimilate",
            generator.scannable_text(markdown),
        )

    def test_topic31_schedules_are_distinguished_and_restrained(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "Sixth Schedule",
            "Fifth Schedule",
            "autonomous districts",
            "district and regional councils",
            "never interchangeable",
            "belong to the Polity owner",
            "Article 46",
            "Tribal Advisory Councils",
            "Commissioner for Scheduled Castes and Scheduled Tribes",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        scanned = generator.scannable_text(markdown)
        self.assertNotIn("the Fifth Schedule governs the North-East", scanned)
        self.assertNotIn("The Fifth Schedule governs the North-East", scanned)
        self.assertNotIn("the Fifth and Sixth Schedules are the same", scanned)

    def test_topic31_north_east_chronology_is_exact(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "A.Z. Phizo",
            "in 1955 these separatists declared",
            "early 1956",
            "middle of 1957",
            "Imkongliba Ao",
            "Nagaland came into existence in 1963",
            "All Party Hill Leaders Conference",
            "state within a state",
            "Garo, Khasi and Jaintia",
            "Manipur and Tripura",
            "renamed Arunachal Pradesh",
            "March 1966",
            "Union Territory as Mizoram",
            "1986",
            "February 1987",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Nagaland was created in 1947", markdown)
        self.assertNotIn(
            "Nagaland and Mizoram were granted independence",
            generator.scannable_text(markdown),
        )

    def test_topic31_mizoram_is_the_model_not_the_universal_case(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "not every North-Eastern conflict",
            "no current security assessment",
            "the successful case rather than as the universal outcome",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "all North-Eastern conflicts were settled on this model", markdown
        )
        self.assertNotIn("the current security situation in the North-East", markdown)

    def test_topic31_arunachal_ocr_compression_is_recorded(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "renamed Arunachal Pradesh in 1972",
            "statehood in 1987",
            "compresses the naming and statehood into a single sentence",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic31_jharkhand_broadening_is_partial_and_dated(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "Jharkhand Party",
            "Jaipal Singh",
            "32 seats",
            "Chota Nagpur",
            "Santhal Parganas",
            "31.15 per cent",
            "44.67 per cent",
            "two-thirds",
            "Jharkhand Mukti Morcha",
            "Shibu Soren",
            "never shifted completely from tribal to class-based",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the Jharkhand movement was purely tribal throughout", markdown
        )

    def test_topic31_accommodation_and_delivery_are_separated(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "slow and even dismal",
            "misapplied",
            "land alienation",
            "mines and industries",
            "elite",
            "split between political accommodation that succeeded and "
            "development that did not",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("tribal integration was an unqualified success", markdown)
        self.assertNotIn(
            "the constitutional design caused tribal alienation", markdown
        )

    def test_topic31_current_bridge_is_commemorative_only(self) -> None:
        markdown = session_markdown("modern-indian-history-31")
        required = [
            "Ministry of Tribal Affairs",
            "Janjatiya Gaurav Divas",
            "15 November 2024 to 15 November 2025",
            "Jamui",
            "commemorative coin",
            "No scheme evaluation, budget figure, "
            "beneficiary count, contemporary tribal statistic or current "
            "security assessment",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertEqual(
            [
                "https://adiprasaran.tribal.gov.in/JJGV/homenew.aspx",
                "https://culture.gov.in/commemorations/"
                "150th-birth-anniversary-birsa-munda",
            ],
            generator.TOPICS[1]["live_sources"],
        )

    def test_topic31_zero_direct_pyq_audit_and_adjacent_routing(self) -> None:
        topic = generator.TOPICS[1]
        markdown = session_markdown("modern-indian-history-31")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", markdown)
        cards = {(item[0], item[1]): item for item in topic["pyq_solutions"]}
        self.assertEqual(
            {
                ("2023", "Mains GS-I Q13"),
                ("2021", "Mains GS-I Q9"),
                ("2022", "Mains GS-I Q10"),
            },
            set(cards),
        )
        for card in cards.values():
            self.assertIn("not-claimed-here", card[3])
            self.assertIsNone(
                re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I), card[1]
            )
        self.assertIn(
            "No Prelims or Mains demand in the local 2018\u20132026 routing "
            "ledgers is routed to this owner",
            markdown,
        )

    # ---------------- Specs, manifests and isolation ----------------

    def test_ascii_spec_is_registered_in_aggregate_loader(self) -> None:
        self.assertTrue(generator.ASCII_PATH.is_file())
        self.assertEqual(
            "modern-indian-history-30-31-2026-08-31-sequential.json",
            generator.ASCII_PATH.name,
        )
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        self.assertEqual(set(generator.PANEL_DATA), set(specs))
        self.assertIn(
            generator.ASCII_PATH.name, ascii_master.MANUAL_SPEC_FILENAMES
        )
        aggregate = ascii_master.load_manual_topic_specs(
            generator.ASCII_PATH.parent
        )
        for key, spec in specs.items():
            self.assertEqual(spec, aggregate[key])

    def test_ascii_and_graphical_specs_are_exact(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        payload = json.loads(generator.ASCII_PATH.read_text(encoding="utf-8"))
        self.assertEqual(
            "Modern Indian History learner-v2 Topics 30-31", payload["scope"]
        )
        self.assertEqual("2026-08-31", payload["generated_on"])
        self.assertTrue(payload["constraints"]["manual_topic_specific"])
        self.assertTrue(payload["constraints"]["complete_embed_ready_lines"])
        self.assertTrue(payload["constraints"]["tracker_untouched"])
        for key, spec in specs.items():
            self.assertEqual(12, len(spec.panels), key)
            self.assertTrue(
                all(
                    len(line) <= 100
                    for panel in spec.panels
                    for line in panel.body.splitlines()
                ),
                key,
            )
            self.assertTrue(
                all(
                    len(
                        [
                            line
                            for line in panel.body.splitlines()
                            if line.strip()
                        ]
                    )
                    >= 4
                    for panel in spec.panels
                ),
                key,
            )
            self.assertEqual(12, len({panel.title for panel in spec.panels}), key)
            graph = json.loads(
                (generator.GRAPHICAL_DIR / f"{key}.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual([], carvaka_flowchart.validate_spec(graph), key)
            self.assertEqual(13, len(graph["stages"]), key)

    def test_combined_spec_holds_twenty_four_authored_panels(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        bodies = [panel.body for spec in specs.values() for panel in spec.panels]
        titles = [panel.title for spec in specs.values() for panel in spec.panels]
        self.assertEqual(24, len(bodies))
        self.assertEqual(24, len(set(bodies)))
        self.assertEqual(24, len(set(titles)))
        for body in bodies:
            self.assertNotIn("FOCUS -> ", body)
            self.assertNotIn("EXAM USE -> use", body)
            self.assertGreaterEqual(
                len([line for line in body.splitlines() if line.strip()]), 4
            )

    def test_generation_manifests_are_tracker_free_generation_one(self) -> None:
        for config in generator.TOPICS:
            path = (
                generator.EXPORT_DIR
                / f"{config['key']}-new-topic-{generator.DATE}.json"
            )
            manifest = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(1, manifest["generation"])
            self.assertIsNone(manifest["supersedes"])
            self.assertTrue(manifest["tracker_untouched"])
            self.assertEqual("learner-v2", manifest["variant"])
            self.assertEqual("2026-08-31", manifest["generation_date"])
            self.assertEqual("Subject-Wide-Syllabus", manifest["section"])
            self.assertEqual("strict-abcd-cycle", manifest["mcq_answer_policy"])
            self.assertEqual(12, manifest["ascii_panel_count"])
            self.assertEqual(13, manifest["graphical_stage_count"])
            self.assertEqual(config["live_sources"], manifest["live_sources"])
            self.assertIn(
                "books/India After Independence-1947-2000 By Bipan "
                "Chandra.pdf",
                [
                    item.replace("\\", "/")
                    for item in manifest["local_ocr_sources"]
                ],
            )
            source = (ROOT / manifest["source_markdown"]).read_text(
                encoding="utf-8"
            )
            canonical = (ROOT / manifest["source_canonical"]).read_text(
                encoding="utf-8"
            )
            self.assertEqual(source, canonical)

    def test_authored_visual_and_definition_maps_are_complete(self) -> None:
        titles = {
            item[0]
            for plans in generator.SESSION_PLANS.values()
            for item in plans
        }
        self.assertEqual(30, len(titles))
        self.assertEqual(titles, set(generator.SESSION_VISUALS))
        self.assertEqual(titles, set(generator.SESSION_DEFINITIONS))
        self.assertEqual(30, len(set(generator.SESSION_VISUALS.values())))
        self.assertEqual(30, len(set(generator.SESSION_DEFINITIONS.values())))
        self.assertTrue(
            all(
                "KEY TERMS:" not in item
                for item in generator.SESSION_VISUALS.values()
            )
        )
        self.assertTrue(
            all(
                len(
                    [line for line in item.splitlines() if line.strip()]
                )
                >= 4
                for item in generator.SESSION_VISUALS.values()
            )
        )
        self.assertTrue(
            all(
                "an evidence-led unit" not in item
                for item in generator.SESSION_DEFINITIONS.values()
            )
        )

    def test_chronology_and_forbidden_tables_cover_both_topics(self) -> None:
        keys = {"modern-indian-history-30", "modern-indian-history-31"}
        self.assertEqual(keys, set(generator.TOPIC_CHRONOLOGY))
        self.assertEqual(keys, set(generator.FORBIDDEN_TOPIC_PHRASES))
        for config in generator.TOPICS:
            markdown = session_markdown(str(config["key"]))
            generator.assert_topic_safeguards(config, markdown)

    def test_forbidden_scan_ignores_only_owner_trap_lines(self) -> None:
        sample = "asserted claim\n- \u274c owner trap claim \u2192 correction\n"
        scanned = generator.scannable_text(sample)
        self.assertIn("asserted claim", scanned)
        self.assertNotIn("owner trap claim", scanned)

    def test_authoring_generator_has_no_finalize_or_publish_side_effects(
        self,
    ) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        forbidden_calls = [
            "markdown_learning_pdf",
            "finalize_v2_topic",
            "generate_v2_section_indexes",
            "EXPORT-PDF-STATUS.json",
            "subprocess",
        ]
        for name in forbidden_calls:
            self.assertNotIn(name, source)

    def test_import_does_not_mutate_topics_26_to_29(self) -> None:
        self.assertEqual(
            ["modern-indian-history-28", "modern-indian-history-29"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-28", "modern-indian-history-29"},
            set(previous.PANEL_DATA),
        )
        self.assertEqual(
            ["modern-indian-history-26", "modern-indian-history-27"],
            [config["key"] for config in earlier.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-26", "modern-indian-history-27"},
            set(earlier.PANEL_DATA),
        )
        self.assertTrue(
            all(len(panels) == 12 for panels in previous.PANEL_DATA.values())
        )
        self.assertTrue(
            all(len(panels) == 12 for panels in earlier.PANEL_DATA.values())
        )
        self.assertEqual(
            "modern-indian-history-28-29-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )
        self.assertEqual(
            "modern-indian-history-26-27-2026-08-31-sequential.json",
            earlier.ASCII_PATH.name,
        )
        generator.validate_previous_batch_untouched()

    def test_adjacent_topic_outputs_are_not_rewritten(self) -> None:
        for number in (26, 27, 28, 29):
            key = f"modern-indian-history-{number}"
            self.assertTrue(
                (
                    generator.SESSION_DIR / f"{key}_Learning-Session.md"
                ).is_file(),
                key,
            )
            self.assertNotIn(
                key, [str(config["key"]) for config in generator.TOPICS]
            )

    def test_import_does_not_mutate_shared_base_globals(self) -> None:
        import generate_modern_history_09_13_sequential as base

        prior_date = base.DATE
        prior_ascii_path = base.ASCII_PATH
        prior_topics = base.TOPICS
        prior_panel_data = base.PANEL_DATA
        self.assertEqual("2026-08-30", base.DATE)
        self.assertEqual(
            "modern-indian-history-09-13-2026-08-30-sequential.json",
            base.ASCII_PATH.name,
        )
        with generator.configured_base():
            self.assertEqual(generator.DATE, base.DATE)
            self.assertEqual(generator.ASCII_PATH, base.ASCII_PATH)
            self.assertEqual(generator.TOPICS, base.TOPICS)
            self.assertEqual(generator.PANEL_DATA, base.PANEL_DATA)
        self.assertEqual(prior_date, base.DATE)
        self.assertEqual(prior_ascii_path, base.ASCII_PATH)
        self.assertIs(prior_topics, base.TOPICS)
        self.assertIs(prior_panel_data, base.PANEL_DATA)

    def test_export_pdf_status_tracker_is_untouched_by_import(self) -> None:
        tracker = ROOT / "EXPORT-PDF-STATUS.json"
        before = tracker.read_bytes()
        importlib.reload(generator)
        self.assertEqual(before, tracker.read_bytes())


if __name__ == "__main__":
    unittest.main()
