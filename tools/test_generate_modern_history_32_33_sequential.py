"""Regression tests for Modern History learner-v2 Topics 32-33."""

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
import generate_modern_history_30_31_sequential as previous
import generate_modern_history_32_33_sequential as generator
import notions_style_ascii_master as ascii_master


def session_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
        encoding="utf-8"
    )


def workbook_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Solved-Workbook.md").read_text(
        encoding="utf-8"
    )


class ModernHistory3233GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-32", "modern-indian-history-33"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "The Nehru Era \u2014 Hope, Foreign Policy & Legacy",
                "Party Politics 1947\u201367: The Congress System & the "
                "Opposition",
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
            "32_The-Nehru-Era-Hope-Foreign-Policy-and-Legacy_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[0]["canonical"]).name,
        )
        self.assertEqual(
            "33_Party-Politics-1947-67-Congress-System-and-Opposition_"
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

    # ---------------- Topic 32 factual safeguards ----------------

    def test_topic32_planning_commission_is_extra_constitutional(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        required = [
            "15 March 1950",
            "extra-constitutional body",
            "must never be described as a constitutional authority",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "constitutional body created by amendment", markdown
        )

    def test_topic32_first_election_seat_vote_gap(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        required = [
            "October 1951",
            "February 1952",
            "173 million",
            "46 per cent",
            "well under half",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic32_cdp_precedes_panchayati_raj(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        required = [
            "2 October 1952",
            "Balwantrai Mehta",
            "1957 recommendation",
            "must not be treated as the same step",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic32_avadi_to_second_plan_chain(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        required = [
            "January 1955",
            "socialistic pattern of society",
            "Schedule A",
            "Schedule B",
            "Schedule C",
            "P.C. Mahalanobis",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic32_bandung_is_not_belgrade(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        required = [
            "April 1955",
            "twenty-nine Afro-Asian states",
            "September 1961",
            "founding summit of the Non-Aligned Movement",
            "Tito",
            "Nasser",
            "Sukarno",
            "Nkrumah",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Bandung founded the Non-Aligned Movement", markdown)
        self.assertNotIn("Belgrade Conference in 1955", markdown)

    def test_topic32_kerala_1957_is_ballot_not_revolution(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        required = ["1957", "E.M.S. Namboodiripad", "elected"]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic32_goa_operation_vijay_and_1962_war(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        required = [
            "December 1961",
            "Operation Vijay",
            "October-November 1962",
            "unilateral ceasefire",
            "K. Kamaraj",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Kamaraj Plan was an economic plan", markdown)

    def test_topic32_kashmir_at_un_and_nehru_death(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        required = ["January 1948", "United Nations", "27 May 1964"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Nehru died in 1963", markdown)

    def test_topic32_pyq_card_is_the_routed_2018_prelims_demand(self) -> None:
        markdown = session_markdown("modern-indian-history-32")
        self.assertIn("2018", markdown)
        self.assertIn("Prelims GS-I", markdown)
        self.assertIn("91", markdown)
        self.assertIn(
            "officially routed to the adjacent owner",
            generator.TOPICS[0]["pyq_note"],
        )
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])

    # ---------------- Topic 33 factual safeguards ----------------

    def test_topic33_dual_membership_ban_forces_socialist_exit(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        required = [
            "1948",
            "bar dual membership",
            "Congress Socialist Party",
            "independent Socialist Party was formed",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic33_tandon_nehru_sequence_is_exact(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        required = [
            "Purushottam Das Tandon",
            "1950",
            "resign in 1951",
            "Nehru himself took over",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic33_jana_sangh_and_swatantra_are_distinguished(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        required = [
            "Syama Prasad Mookerjee",
            "1951",
            "Rajagopalachari",
            "Minoo Masani",
            "N.G. Ranga",
            "1959",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "Jana Sangh and Swatantra shared the same platform", markdown
        )

    def test_topic33_kmpp_merges_into_psp_in_1952(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        required = [
            "J.B. Kripalani",
            "Praja Socialist Party",
            "1951",
            "1952",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("PSP was founded directly in 1951", markdown)

    def test_topic33_cpi_split_in_1964(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        required = ["Sino-Soviet split", "1964", "CPI(M)"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("CPI split after the 1967 election", markdown)

    def test_topic33_congress_system_is_attributed_to_kothari(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        required = [
            "Rajni Kothari",
            "party of consensus",
            "analytical label, not a Congress self-description",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "Congress described itself as the Congress system", markdown
        )

    def test_topic33_seat_vote_gap_and_1967_watershed(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        required = [
            "1952",
            "1957",
            "1962",
            "well under 50 per cent",
            "eight states",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic33_lohia_non_congressism_and_forward_bloc(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        required = [
            "Ram Manohar Lohia",
            "non-Congressism",
            "Forward Bloc",
            "1977",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic33_pyq_card_is_the_routed_2024_prelims_demand(self) -> None:
        markdown = session_markdown("modern-indian-history-33")
        self.assertIn("2024", markdown)
        self.assertIn("Prelims GS-I", markdown)
        self.assertIn("73", markdown)
        self.assertEqual([], generator.TOPICS[1]["pyq_solutions"])
        self.assertIn(
            "No Mains demand in the local 2018-2025 ledgers is routed to "
            "this owner",
            generator.TOPICS[1]["pyq_note"],
        )

    # ---------------- Specs, manifests and isolation ----------------

    def test_ascii_spec_is_valid_and_registered_in_shared_index(
        self,
    ) -> None:
        self.assertTrue(generator.ASCII_PATH.is_file())
        self.assertEqual(
            "modern-indian-history-32-33-2026-08-31-sequential.json",
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
            "Modern Indian History learner-v2 Topics 32-33", payload["scope"]
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
        keys = {"modern-indian-history-32", "modern-indian-history-33"}
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

    def test_import_does_not_mutate_topics_30_to_31(self) -> None:
        self.assertEqual(
            ["modern-indian-history-30", "modern-indian-history-31"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-30", "modern-indian-history-31"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(
            all(len(panels) == 12 for panels in previous.PANEL_DATA.values())
        )
        self.assertEqual(
            "modern-indian-history-30-31-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )
        generator.validate_previous_batch_untouched()

    def test_adjacent_topic_outputs_are_not_rewritten(self) -> None:
        for number in (28, 29, 30, 31):
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
