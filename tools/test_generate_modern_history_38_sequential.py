"""Regression tests for Modern History learner-v2 Topic 38."""

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
import generate_modern_history_36_37_sequential as previous
import generate_modern_history_38_sequential as generator
import notions_style_ascii_master as ascii_master


def session_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
        encoding="utf-8"
    )


def workbook_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Solved-Workbook.md").read_text(
        encoding="utf-8"
    )


class ModernHistory38GeneratorTests(unittest.TestCase):
    def test_one_new_topic_is_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-38"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "Economy, Land, Society & State: A Post-Independence "
                "Synthesis"
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
            "38_Economy-Land-Society-and-State-A-Post-Independence-"
            "Synthesis_Complete-Topic-Package.md",
            Path(generator.TOPICS[0]["canonical"]).name,
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

    # ---------------- Topic 38 factual safeguards ----------------

    def test_topic38_economic_model_and_break_are_dated(self) -> None:
        markdown = session_markdown("modern-indian-history-38")
        required = [
            "Industrial Policy Resolutions",
            "Mahalanobis",
            "licence-permit raj",
            "Narasimha Rao",
            "Manmohan Singh",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "economic liberalisation began under Rajiv Gandhi", markdown
        )

    def test_topic38_land_reform_is_disaggregated(self) -> None:
        markdown = session_markdown("modern-indian-history-38")
        required = ["Zamindari abolition", "20 million", "Bhoodan", "Vinoba Bhave", "Pochampalli"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "all land reforms succeeded equally in post-independence "
            "India",
            markdown,
        )

    def test_topic38_green_revolution_debate_is_balanced(self) -> None:
        markdown = session_markdown("modern-indian-history-38")
        required = ["Green Revolution", "mid-1960s", "Punjab", "Haryana"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the Green Revolution widened inequality everywhere it "
            "reached",
            markdown,
        )

    def test_topic38_agrarian_struggle_sequence_is_dated(self) -> None:
        markdown = session_markdown("modern-indian-history-38")
        required = [
            "Naxalbari",
            "CPI(ML)",
            "Sharad Joshi",
            "Mahendra Singh Tikait",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "the Naxalbari uprising took place in the 1970s", markdown
        )

    def test_topic38_hindu_code_bill_is_four_acts(self) -> None:
        markdown = session_markdown("modern-indian-history-38")
        required = ["Hindu Code Bill", "Mandal Commission"]
        for phrase in required:
            self.assertIn(phrase, markdown)
        fact_text = "\n".join(
            statement for _label, statement in generator.TOPICS[0]["facts"]
        )
        self.assertIn("Hindu Marriage Act, 1955", fact_text)
        self.assertIn("did not create complete legal or social equality", fact_text)
        self.assertNotIn(
            "the Hindu Code Bill was enacted as a single unified code",
            markdown,
        )

    def test_topic38_synthesis_threads_and_institutional_decay(self) -> None:
        markdown = session_markdown("modern-indian-history-38")
        required = ["1905", "1857", "1975-77", "1969", "1985"]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic38_pyq_reconciliation_is_transparent(self) -> None:
        config = generator.TOPICS[0]
        self.assertEqual([], config["pyq_solutions"])
        self.assertIn("Hind Mazdoor Sabha", config["pyq_note"])
        self.assertIn("land-reforms legislation", config["pyq_note"])
        markdown = session_markdown("modern-indian-history-38")
        self.assertIn("Hind Mazdoor Sabha", markdown)
        self.assertIn("land-reforms legislation", markdown)
        self.assertIn("PYQ Integration", markdown)
        self.assertIn("Exercise Mitra Shakti", markdown)

    # ---------------- Specs, manifests and isolation ----------------

    def test_ascii_spec_is_valid_and_registered_in_shared_index(
        self,
    ) -> None:
        self.assertTrue(generator.ASCII_PATH.is_file())
        self.assertEqual(
            "modern-indian-history-38-2026-08-31-sequential.json",
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
            "Modern Indian History learner-v2 Topic 38", payload["scope"]
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

    def test_spec_holds_twelve_authored_panels(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        bodies = [
            panel.body for spec in specs.values() for panel in spec.panels
        ]
        titles = [
            panel.title for spec in specs.values() for panel in spec.panels
        ]
        self.assertEqual(12, len(bodies))
        self.assertEqual(12, len(set(bodies)))
        self.assertEqual(12, len(set(titles)))
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
        self.assertEqual(15, len(titles))
        self.assertEqual(titles, set(generator.SESSION_VISUALS))
        self.assertEqual(titles, set(generator.SESSION_DEFINITIONS))
        self.assertEqual(15, len(set(generator.SESSION_VISUALS.values())))
        self.assertEqual(
            15, len(set(generator.SESSION_DEFINITIONS.values()))
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

    def test_chronology_and_forbidden_tables_cover_the_topic(self) -> None:
        keys = {"modern-indian-history-38"}
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

    def test_import_does_not_mutate_topics_36_to_37(self) -> None:
        self.assertEqual(
            ["modern-indian-history-36", "modern-indian-history-37"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-36", "modern-indian-history-37"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(
            all(len(panels) == 12 for panels in previous.PANEL_DATA.values())
        )
        self.assertEqual(
            "modern-indian-history-36-37-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )
        generator.validate_previous_batch_untouched()

    def test_adjacent_topic_outputs_are_not_rewritten(self) -> None:
        for number in (32, 33, 34, 35, 36, 37):
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
