"""Regression tests for Modern History learner-v2 Topics 34-35."""

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
import generate_modern_history_32_33_sequential as previous
import generate_modern_history_34_35_sequential as generator
import notions_style_ascii_master as ascii_master


def session_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
        encoding="utf-8"
    )


def workbook_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Solved-Workbook.md").read_text(
        encoding="utf-8"
    )


class ModernHistory3435GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-34", "modern-indian-history-35"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "From Shastri to Indira Gandhi, 1964\u201373",
                "The JP Movement & the Emergency",
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
            "34_From-Shastri-to-Indira-Gandhi-1964-73_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[0]["canonical"]).name,
        )
        self.assertEqual(
            "35_The-JP-Movement-and-the-Emergency_Complete-Topic-Package.md",
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

    # ---------------- Topic 34 factual safeguards ----------------

    def test_topic34_two_successions_are_dated_precisely(self) -> None:
        markdown = session_markdown("modern-indian-history-34")
        required = [
            "June 1964",
            "10 January 1966",
            "Tashkent",
            "January 1966",
            "Morarji Desai",
            "355",
            "169",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Shastri died in Delhi", markdown)

    def test_topic34_devaluation_year_and_causes(self) -> None:
        markdown = session_markdown("modern-indian-history-34")
        required = ["June 1966", "35.5 per cent", "harvest failures"]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic34_1967_election_is_not_a_comfortable_win(self) -> None:
        markdown = session_markdown("modern-indian-history-34")
        required = ["1967", "eight states", "Aya Ram Gaya Ram"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "Congress won a comfortable majority in 1967", markdown
        )

    def test_topic34_bank_nationalisation_and_privy_purse_years_are_kept_apart(
        self,
    ) -> None:
        markdown = session_markdown("modern-indian-history-34")
        required = [
            "1969",
            "14 banks",
            "V.V. Giri",
            "1970",
            "26th Constitutional Amendment",
            "352 of 518",
            "Garibi Hatao",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "bank nationalisation took place in 1971", markdown
        )
        self.assertNotIn(
            "privy purses were abolished in 1969", markdown
        )

    def test_topic34_bangladesh_war_and_pokhran_are_dated_precisely(
        self,
    ) -> None:
        markdown = session_markdown("modern-indian-history-34")
        required = ["Bangladesh", "Pokhran-I", "May 1974", "peaceful nuclear explosion"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "Pokhran-I was a declared nuclear weapons test", markdown
        )

    def test_topic34_coal_gap_is_transparent_not_fabricated(self) -> None:
        markdown = session_markdown("modern-indian-history-34")
        required = [
            "2019",
            "coal-sector nationalisation",
            "no supporting content",
            "must never be stated from memory",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertIn(
            "having no supporting content in any modern-history source "
            "book",
            generator.TOPICS[0]["pyq_note"],
        )

    # ---------------- Topic 35 factual safeguards ----------------

    def test_topic35_economic_crisis_precedes_student_movements(self) -> None:
        markdown = session_markdown("modern-indian-history-35")
        required = [
            "1972-73",
            "oil shock",
            "22 per cent",
            "January 1974",
            "March 1974",
            "Sampoorna Kranti",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic35_allahabad_hc_not_supreme_court_unseated_indira(
        self,
    ) -> None:
        markdown = session_markdown("modern-indian-history-35")
        required = [
            "Jagmohanlal Sinha",
            "12 June 1975",
            "Raj Narain",
            "V.R. Krishna Iyer",
            "24 June 1975",
            "conditional stay",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the Supreme Court struck down Indira Gandhi's election",
            markdown,
        )

    def test_topic35_proclamation_dating_trap_is_preserved(self) -> None:
        markdown = session_markdown("modern-indian-history-35")
        required = ["Article 352", "25 June 1975", "26 June 1975"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the Emergency was declared under Article 356", markdown
        )

    def test_topic35_instruments_and_excesses_are_specific(self) -> None:
        markdown = session_markdown("modern-indian-history-35")
        required = [
            "MISA",
            "100,000",
            "Twenty-Point Programme",
            "42nd Amendment",
            "Sanjay Gandhi",
            "Shah Commission",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("sterilisation figures ran into the millions", markdown)

    def test_topic35_1977_and_44th_amendment_are_distinguished(self) -> None:
        markdown = session_markdown("modern-indian-history-35")
        required = ["January 1977", "March 1977", "44th Amendment", "1978"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the Emergency ended through a court verdict", markdown
        )

    def test_topic35_social_base_excludes_workers_and_peasants(self) -> None:
        markdown = session_markdown("modern-indian-history-35")
        required = ["students", "middle class", "traders", "intelligentsia"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the JP movement drew its base from workers and peasants",
            markdown,
        )

    def test_topic35_zero_pyq_audit_is_transparent(self) -> None:
        self.assertEqual([], generator.TOPICS[1]["pyq_solutions"])
        self.assertIn(
            "No Prelims or Mains demand in the local 2018-2026 routing "
            "ledgers is routed to this owner",
            generator.TOPICS[1]["pyq_note"],
        )

    def test_topic35_pib_current_note_is_preserved_verbatim(self) -> None:
        markdown = session_markdown("modern-indian-history-35")
        required = [
            "25 June 2025",
            "Union Cabinet",
            "fifty years",
            "PRID 2139543",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertIn("PRID 2139543", generator.TOPICS[1]["current_note"])

    # ---------------- Specs, manifests and isolation ----------------

    def test_ascii_spec_is_valid_and_registered_in_shared_index(
        self,
    ) -> None:
        self.assertTrue(generator.ASCII_PATH.is_file())
        self.assertEqual(
            "modern-indian-history-34-35-2026-08-31-sequential.json",
            generator.ASCII_PATH.name,
        )
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        self.assertEqual(set(generator.PANEL_DATA), set(specs))
        self.assertIn(
            generator.ASCII_PATH.name, ascii_master.MANUAL_SPEC_FILENAMES
        )

    def test_ascii_and_graphical_specs_are_exact(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        payload = json.loads(generator.ASCII_PATH.read_text(encoding="utf-8"))
        self.assertEqual(
            "Modern Indian History learner-v2 Topics 34-35", payload["scope"]
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
            self.assertEqual(
                12, len({panel.title for panel in spec.panels}), key
            )
            graph = json.loads(
                (generator.GRAPHICAL_DIR / f"{key}.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual([], carvaka_flowchart.validate_spec(graph), key)
            self.assertEqual(13, len(graph["stages"]), key)
            self.assertFalse(graph["status"]["approved"], key)

    def test_combined_spec_holds_twenty_four_authored_panels(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        bodies = [
            panel.body for spec in specs.values() for panel in spec.panels
        ]
        titles = [
            panel.title for spec in specs.values() for panel in spec.panels
        ]
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
            self.assertEqual(
                "strict-abcd-cycle", manifest["mcq_answer_policy"]
            )
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
        self.assertEqual(
            30, len(set(generator.SESSION_DEFINITIONS.values()))
        )
        self.assertTrue(
            all(
                "KEY TERMS:" not in item
                for item in generator.SESSION_VISUALS.values()
            )
        )
        self.assertTrue(
            all(
                len([line for line in item.splitlines() if line.strip()])
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
        keys = {"modern-indian-history-34", "modern-indian-history-35"}
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

    def test_import_does_not_mutate_topics_32_to_33(self) -> None:
        self.assertEqual(
            ["modern-indian-history-32", "modern-indian-history-33"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-32", "modern-indian-history-33"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(
            all(len(panels) == 12 for panels in previous.PANEL_DATA.values())
        )
        self.assertEqual(
            "modern-indian-history-32-33-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )
        generator.validate_previous_batch_untouched()

    def test_adjacent_topic_outputs_are_not_rewritten(self) -> None:
        for number in (30, 31, 32, 33):
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
