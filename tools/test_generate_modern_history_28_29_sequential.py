"""Regression tests for Modern History learner-v2 Topics 28-29."""

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
import generate_modern_history_26_27_sequential as previous
import generate_modern_history_28_29_sequential as generator
import notions_style_ascii_master as ascii_master


def session_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
        encoding="utf-8"
    )


def workbook_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Solved-Workbook.md").read_text(
        encoding="utf-8"
    )


class ModernHistory2829GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-28", "modern-indian-history-29"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "Integration of the Princely States & the Making of the "
                "Republic",
                "The Colonial Legacy & the Foundations of the Republic",
            ],
            [config["title"] for config in generator.TOPICS],
        )
        self.assertTrue(
            all(len(config["facts"]) == 20 for config in generator.TOPICS)
        )
        self.assertTrue(
            all(
                len({label for label, _ in config["facts"]}) == 20
                for config in generator.TOPICS
            )
        )
        self.assertTrue(
            all(len(config["mains"]) == 6 for config in generator.TOPICS)
        )
        self.assertTrue(
            all(
                [item[0] for item in config["mains"]] == [10, 10, 15, 15, 20, 20]
                for config in generator.TOPICS
            )
        )
        self.assertTrue(
            all(
                len(generator.SESSION_PLANS[str(config["key"])]) == 15
                for config in generator.TOPICS
            )
        )

    def test_canonical_paths_follow_adjacent_package_convention(self) -> None:
        self.assertEqual(
            "28_Integration-of-Princely-States-and-Making-of-the-Republic_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[0]["canonical"]).name,
        )
        self.assertEqual(
            "29_Colonial-Legacy-and-Foundations-of-the-Republic_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[1]["canonical"]).name,
        )
        for config in generator.TOPICS:
            self.assertEqual(
                generator.KNOWLEDGE, Path(config["canonical"]).parent
            )

    def test_owner_files_are_the_declared_sources(self) -> None:
        for config in generator.TOPICS:
            for role in ("basic", "advanced"):
                path = Path(config[role])
                self.assertTrue(path.is_file(), str(path))
                self.assertEqual(role, path.parent.name)
            for extra in config["extra"]:
                self.assertTrue(Path(extra).is_file(), str(extra))

    def test_local_ocr_book_for_post_1947_history_is_declared(self) -> None:
        names = {path.name for path in generator.LOCAL_BOOKS}
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

    def test_mains_practice_is_solved_at_the_required_weightings(self) -> None:
        for config in generator.TOPICS:
            markdown = session_markdown(str(config["key"]))
            marks = re.findall(
                r"(?m)^### ORIGINAL MAINS \d+ - (\d+) MARKS\s*$", markdown
            )
            self.assertEqual(
                ["10", "10", "15", "15", "20", "20"], marks, config["key"]
            )
            self.assertEqual(6, markdown.count("**Model thesis:**"))
            self.assertEqual(6, markdown.count("**Evidence spine:**"))

    def test_regeneration_is_deterministic(self) -> None:
        for config in generator.TOPICS:
            first = generator.assemble(config)
            second = generator.assemble(config)
            self.assertEqual(first, second, config["key"])
            self.assertEqual(
                first[0], session_markdown(str(config["key"])), config["key"]
            )
            self.assertEqual(
                first[1], workbook_markdown(str(config["key"])), config["key"]
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

    # ---------------- Topic 28 factual safeguards ----------------

    def test_topic28_paramountcy_lapsed_and_was_not_transferred(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "lapsed when British rule ended on 15 August 1947",
            "never transferred to India or Pakistan",
            "no successor sovereign",
            "constructed by agreement",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        for forbidden in (
            "paramountcy was transferred to India",
            "paramountcy passed automatically to India",
            "paramountcy passed to the Indian Union",
        ):
            self.assertNotIn(forbidden, markdown)

    def test_topic28_state_count_uses_the_open_formulation(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        self.assertIn("more than 560", markdown)
        self.assertIn("562 and 565", markdown)
        self.assertIn("counting convention", markdown.casefold())
        self.assertNotIn("there were exactly 562 princely states", markdown)
        self.assertNotIn("there were exactly 565 princely states", markdown)

    def test_topic28_accession_formula_and_states_department(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "Defence, External Affairs and Communications",
            "27 June 1947",
            "V.P. Menon",
            "States Department",
            "never of one man acting alone",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "Patel integrated the princely states single-handedly", markdown
        )
        self.assertNotIn(
            "the Instrument of Accession transferred all subjects", markdown
        )

    def test_topic28_four_stages_are_kept_distinct(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "Accession, merger, democratisation and constitutional "
            "incorporation are four different stages",
            "merger and consolidation, which began in December 1947",
            "democratisation inside the former states",
            "constitutional incorporation",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("accession was the whole of integration", markdown)

    def test_topic28_three_hard_cases_are_compared_not_merged(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "ruler's choice, the population's composition, the state's "
            "geography and the security situation",
            "acceded to Pakistan",
            "sought independence",
            "hesitated",
            "Sheikh Abdullah",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        for forbidden in (
            "the three states posed the same problem",
            "Junagadh, Hyderabad and Kashmir were identical",
            "the three problem states were all Muslim-majority",
        ):
            self.assertNotIn(forbidden, markdown)

    def test_topic28_case_dates_and_operation_names(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "plebiscite held in Junagadh in February 1948",
            "Shah Nawaz Bhutto",
            "standstill agreement",
            "September 1948",
            "Operation Polo",
            "Tribal invaders entered Kashmir in October 1947",
            "30 December 1947",
            "contested later claims",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        for forbidden in (
            "Operation Polo was conducted in Kashmir",
            "Operation Polo relates to Kashmir",
            "Operation Polo liberated Goa",
            "the Junagadh plebiscite was held in 1947",
        ):
            self.assertNotIn(forbidden, markdown)

    def test_topic28_privy_purses_survive_the_initial_integration(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "not abolished during the initial integration",
            "asserts no amount for any purse",
            "1971",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        for forbidden in (
            "privy purses were abolished at the moment of accession",
            "privy purses ended in 1947",
        ):
            self.assertNotIn(forbidden, markdown)

    def test_topic28_independence_is_not_the_republic(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "26 November 1949",
            "26 January 1950",
            "independent on 15 August 1947 and a republic on 26 January 1950",
            "Dr Rajendra Prasad",
            "B.R. Ambedkar",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("India became a republic on 15 August 1947", markdown)
        self.assertNotIn("India became a republic in 1947", markdown)

    def test_topic28_numerical_restraint_is_explicit(self) -> None:
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "states no percentage",
            "no casualty or troop figure",
            "no audited polling figure",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        window_hits = []
        for match in re.finditer(r"(?i)plebiscite", markdown):
            window = markdown[
                max(0, match.start() - 80) : match.end() + 80
            ]
            if re.search(r"\d{1,3}(?:\.\d+)?\s*(?:per cent|%)", window):
                window_hits.append(window)
        self.assertEqual([], window_hits)

    def test_topic28_current_bridge_is_official_and_bounded(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual(
            [
                "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2184055",
                "https://culture.gov.in/commemorations/"
                "150th-birth-anniversary-sardar-vallabhbhai-patel",
            ],
            config["live_sources"],
        )
        markdown = session_markdown("modern-indian-history-28")
        required = [
            "Ministry of Culture",
            "Statue of Unity",
            "31 October 2024",
            "Rashtriya Ekta Diwas",
            "first celebrated in 2014",
            "commemorative compression",
            "nearly 40 per cent",
            "roughly a third",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic28_pyq_cards_are_verbatim_and_answer_free(self) -> None:
        topic = generator.TOPICS[0]
        cards = {(item[0], item[1]): item for item in topic["pyq_solutions"]}
        self.assertEqual(2, len(cards))
        solved = cards[("2021", "Mains GS-I Q3")]
        self.assertIn("verbatim-official-stem-verified-locally", solved[3])
        self.assertIn(
            "Assess the main administrative issues and socio-cultural "
            "problems in the integration process of Indian Princely States.",
            solved[2],
        )
        unresolved = cards[("2018-2026", "Prelims GS-I")]
        self.assertIn("unresolved-locally", unresolved[3])
        self.assertIn("no answer letter", unresolved[3])
        for card in cards.values():
            self.assertIsNone(
                re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I), card[1]
            )

    def test_topic28_verbatim_stem_matches_the_official_local_export(
        self,
    ) -> None:
        export = (
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md"
        )
        self.assertTrue(export.is_file())
        flattened = re.sub(
            r"\s+", " ", export.read_text(encoding="utf-8", errors="ignore")
        )
        self.assertIn(
            "Assess the main administrative issues and socio-cultural "
            "problems in the integration process of Indian Princely States.",
            flattened,
        )

    # ---------------- Topic 29 factual safeguards ----------------

    def test_topic29_two_inheritances_are_separated(self) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "colonial economic and administrative liabilities",
            "national-movement political assets",
            "development of underdevelopment",
            "A. Gunder Frank",
            "continuity with conversion",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("India inherited a healthy economy in 1947", markdown)
        self.assertNotIn(
            "the republic inherited a developed industrial economy", markdown
        )

    def test_topic29_franchise_contrast_is_exact(self) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "about 3 per cent of Indians could vote after 1919",
            "about 15 per cent after 1935",
            "universal adult franchise",
            "rice-bowl theory",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "universal adult franchise existed under colonial rule", markdown
        )
        self.assertNotIn("the colonial franchise was universal", markdown)

    def test_topic29_every_estimate_is_source_attributed(self) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "attributed estimate",
            "nearly 84 per cent",
            "about 92 per cent",
            "barely thirty-two years",
            "about 13 per cent",
            "about 28 per cent",
            "Rs 550 million",
            "must be attributed and never rounded",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic29_refugee_figure_is_one_directional(self) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "nearly six million",
            "one-directional",
            "not the total displacement in both directions",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        for forbidden in (
            "six million people were displaced in both directions",
            "six million is the total displacement",
            "six million was the total number displaced",
        ):
            self.assertNotIn(forbidden, markdown)

    def test_topic29_mortality_estimate_is_not_presented_as_settled(
        self,
    ) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "500,000",
            "Chandra's estimate",
            "not settled scholarship",
            "wider scholarship offers substantially different totals",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        for forbidden in (
            "the partition death toll was exactly",
            "exactly 500,000 people were killed",
            "partition mortality is settled scholarship",
            "Chandra's estimate is settled scholarship",
        ):
            self.assertNotIn(forbidden, markdown)

    def test_topic29_assassination_ban_and_pact_dates(self) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "30 January 1948",
            "Nathuram Godse",
            "banned the Rashtriya Swayamsevak Sangh",
            "July 1949",
            "loyalty to India's flag and Constitution",
            "8 April 1950",
            "Nehru-Liaquat Pact",
            "Nehru-Liaqat",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Gandhi was assassinated by a Muslim", markdown)

    def test_topic29_communist_transition_is_carefully_attributed(self) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "B.T. Ranadive",
            "February 1948",
            "Telangana",
            "Telengana",
            "mid-1951",
            "legalised",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic29_enclaves_and_the_two_operations(self) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "Pondicherry",
            "1954",
            "17 December 1961",
            "Operation Vijay",
            "Operation Polo",
            "September 1948",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        for forbidden in (
            "Goa joined India in 1947",
            "Goa was liberated in 1947",
            "Pondicherry was transferred in 1947",
            "Operation Vijay integrated Hyderabad",
            "Operation Polo liberated Goa",
        ):
            self.assertNotIn(forbidden, markdown)

    def test_topic29_founding_consensus_is_graded_not_celebrated(self) -> None:
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "founding consensus",
            "civilian control",
            "non-alignment",
            "planning",
            "secularism",
            "land reform largely unimplemented",
            "female literacy",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic29_solves_the_routed_2025_four_domain_demand(self) -> None:
        topic = generator.TOPICS[1]
        cards = {(item[0], item[1]): item for item in topic["pyq_solutions"]}
        self.assertEqual(2, len(cards))
        solved = cards[("2025", "Mains GS-I Q12")]
        self.assertIn("verbatim-official-stem-verified-locally", solved[3])
        self.assertIn(
            "Trace India's consolidation process during early phase of "
            "independence in terms of polity, economy, education and "
            "international relations.",
            solved[2],
        )
        for domain in ("polity", "economy", "education", "international"):
            self.assertIn(domain, solved[4].casefold())
        adjacent = cards[("2021", "Mains GS-I Q3")]
        self.assertIn("adjacent-owner-routed-demand", adjacent[3])
        self.assertIn("Topic 28 owner", adjacent[4])
        for card in cards.values():
            self.assertIsNone(
                re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I), card[1]
            )

    def test_topic29_verbatim_stem_matches_the_official_local_export(
        self,
    ) -> None:
        export = (
            ROOT / "knowledge-export" / "Mains PYQ" / "UPSC Mains 2025 GS Paper 1.md"
        )
        self.assertTrue(export.is_file())
        flattened = re.sub(
            r"\s+", " ", export.read_text(encoding="utf-8", errors="ignore")
        )
        self.assertIn(
            "Trace India's consolidation process during early phase of "
            "independence in terms of polity, economy, education and "
            "international relations.",
            flattened,
        )

    def test_topic29_current_bridge_is_official_and_bounded(self) -> None:
        config = generator.TOPICS[1]
        self.assertEqual(
            ["https://www.pib.gov.in/PressReleasePage.aspx?PRID=2218449"],
            config["live_sources"],
        )
        markdown = session_markdown("modern-indian-history-29")
        required = [
            "77th Republic Day",
            "26 January 2026",
            "unity in diversity",
            "counting 1950 as the first Republic Day",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertIn(
            "ceremonial parade is not a historical source",
            config["current_note"],
        )

    # ---------------- Specs, manifests and isolation ----------------

    def test_ascii_and_graphical_specs_are_exact(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        self.assertEqual(set(generator.PANEL_DATA), set(specs))
        payload = json.loads(generator.ASCII_PATH.read_text(encoding="utf-8"))
        self.assertEqual(
            "modern-indian-history-28-29-2026-08-31-sequential.json",
            generator.ASCII_PATH.name,
        )
        self.assertTrue(payload["constraints"]["manual_topic_specific"])
        self.assertTrue(payload["constraints"]["complete_embed_ready_lines"])
        self.assertTrue(payload["constraints"]["tracker_untouched"])
        self.assertEqual("2026-08-31", payload["generated_on"])
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
                        [line for line in panel.body.splitlines() if line.strip()]
                    )
                    >= 4
                    for panel in spec.panels
                ),
                key,
            )
            self.assertEqual(
                12,
                len({panel.title for panel in spec.panels}),
                key,
            )
            graph = json.loads(
                (generator.GRAPHICAL_DIR / f"{key}.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual([], carvaka_flowchart.validate_spec(graph), key)
            self.assertEqual(13, len(graph["stages"]), key)
            self.assertGreaterEqual(
                len({stage["layout"] for stage in graph["stages"]}), 4, key
            )

    def test_ascii_panels_are_authored_not_templated(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        bodies = [
            panel.body for spec in specs.values() for panel in spec.panels
        ]
        self.assertEqual(24, len(bodies))
        self.assertEqual(24, len(set(bodies)))
        for body in bodies:
            self.assertNotIn("FOCUS -> ", body)
            self.assertNotIn("EXAM USE -> use", body)
            self.assertGreaterEqual(
                len([line for line in body.splitlines() if line.strip()]), 4
            )

    def test_ascii_spec_is_registered_in_aggregate_loader(self) -> None:
        self.assertIn(
            "modern-indian-history-28-29-2026-08-31-sequential.json",
            ascii_master.MANUAL_SPEC_FILENAMES,
        )
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        self.assertEqual(
            {"modern-indian-history-28", "modern-indian-history-29"},
            set(specs),
        )
        aggregate = ascii_master.load_manual_topic_specs(
            generator.ASCII_PATH.parent
        )
        for key, spec in specs.items():
            self.assertEqual(spec, aggregate[key])

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
            self.assertEqual(
                "strict-abcd-cycle", manifest["mcq_answer_policy"]
            )
            self.assertEqual(12, manifest["ascii_panel_count"])
            self.assertEqual(13, manifest["graphical_stage_count"])
            self.assertEqual(config["live_sources"], manifest["live_sources"])
            self.assertIn(
                "books/India After Independence-1947-2000 By Bipan Chandra.pdf",
                [
                    value.replace("\\", "/")
                    for value in manifest["local_ocr_sources"]
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
                len(item.splitlines()) >= 4
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
        keys = {"modern-indian-history-28", "modern-indian-history-29"}
        self.assertEqual(keys, set(generator.TOPIC_CHRONOLOGY))
        self.assertEqual(keys, set(generator.FORBIDDEN_TOPIC_PHRASES))
        for config in generator.TOPICS:
            markdown = session_markdown(str(config["key"]))
            generator.assert_topic_safeguards(config, markdown)

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

    def test_import_does_not_mutate_topics_26_27(self) -> None:
        self.assertEqual(
            ["modern-indian-history-26", "modern-indian-history-27"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-26", "modern-indian-history-27"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(
            all(len(panels) == 12 for panels in previous.PANEL_DATA.values())
        )
        self.assertEqual(
            "modern-indian-history-26-27-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )
        self.assertNotEqual(previous.ASCII_PATH, generator.ASCII_PATH)
        generator.validate_previous_batch_untouched()

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
