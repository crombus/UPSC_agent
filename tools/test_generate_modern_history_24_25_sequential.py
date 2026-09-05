"""Regression tests for Modern History learner-v2 Topics 24-25."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_22_23_sequential as previous
import generate_modern_history_24_25_sequential as generator
import notions_style_ascii_master as ascii_master


class ModernHistory2425GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-24", "modern-indian-history-25"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "The Government of India Act 1935 & the Congress Ministries "
                "(1937\u20131939)",
                "Second World War, the Cripps Mission & Quit India "
                "(1939\u20131942)",
            ],
            [config["title"] for config in generator.TOPICS],
        )
        self.assertTrue(all(len(config["facts"]) == 20 for config in generator.TOPICS))
        self.assertTrue(all(len(config["mains"]) == 6 for config in generator.TOPICS))
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
            "24_Government-of-India-Act-1935-Congress-Ministries-1937-1939_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[0]["canonical"]).name,
        )
        self.assertEqual(
            "25_Second-World-War-Cripps-Mission-Quit-India-1939-1942_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[1]["canonical"]).name,
        )

    def test_generated_sessions_and_workbooks_pass_contracts(self) -> None:
        for config in generator.TOPICS:
            key = str(config["key"])
            session_path = generator.SESSION_DIR / f"{key}_Learning-Session.md"
            workbook_path = generator.SESSION_DIR / f"{key}_Solved-Workbook.md"
            graphical_path = generator.GRAPHICAL_DIR / f"{key}.json"
            markdown = session_path.read_text(encoding="utf-8")
            workbook = workbook_path.read_text(encoding="utf-8")
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
            self.assertEqual(20, markdown.count("**Answer: A.**"), key)
            self.assertEqual(20, markdown.count("**Answer: B.**"), key)
            self.assertEqual(20, markdown.count("**Answer: C.**"), key)
            self.assertEqual(20, markdown.count("**Answer: D.**"), key)
            self.assertEqual(6, markdown.count("### ORIGINAL MAINS"), key)
            self.assertNotRegex(markdown, r"(?i)\b(?:todo|placeholder|lorem ipsum)\b")
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

    def test_topic24_constitutional_lineage_and_federation_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-24_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "Simon Commission's 1930 report",
            "1933 White Paper",
            "Joint Select Committee's 1934 report",
            "royal assent in 1935",
            "never came into force",
            "central dyarchy never operated anywhere",
            "provincial dyarchy and replaced it with provincial autonomy",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("All-India Federation came into force", markdown)
        self.assertNotIn("federation began functioning", markdown)
        self.assertNotIn("central dyarchy operated", markdown)

    def test_topic24_governor_powers_section93_and_franchise_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-24_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "discretionary powers and special responsibilities",
            "Section 93",
            "background reserve power that followed rather",
            "Ecclesiastical Affairs",
            "Tribal Areas",
            "residuary legislative power over unlisted subjects was vested "
            "in the Governor-General",
            "roughly 30 to 35 million",
            "roughly 10 to 14 per cent",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Section 93 caused the resignation", markdown)
        self.assertNotIn("franchise was exactly", markdown)

    def test_topic24_rbi_federal_court_burma_and_ministry_timing_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-24_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "Reserve Bank of India Act, 1934",
            "must never be described as a creation of the 1935 Act itself",
            "began functioning in 1937",
            "took effect in 1937",
            "February 1937",
            "six provinces in July 1937",
            "followed later in 1937",
            "followed in 1938",
            "Assam",
            "North-West Frontier Province",
            "eight-of-eleven figure names the eventual, not the "
            "simultaneous, position",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "Reserve Bank of India was established under the Government of "
            "India Act, 1935",
            markdown,
        )
        self.assertNotIn(
            "Congress formed ministries in eight provinces immediately",
            markdown,
        )

    def test_topic24_office_debate_achievements_resignation_and_lahore_safeguards(
        self,
    ) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-24_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "office-acceptance debate",
            "risk of legitimising a limited constitutional structure",
            "expanded civil liberties, released political prisoners",
            "restricted provincial finance, landlord-weighted legislatures",
            "resigned between October and November 1939",
            "Deliverance Day",
            "one party reaction among several rather than a neutral "
            "national commemoration",
            "Lahore Resolution of March 1940",
            "one link in a longer chain of developments",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Lahore Resolution directly caused Partition", markdown)
        self.assertNotIn("Deliverance Day was a neutral national event", markdown)

    def test_topic24_official_2024_key_and_2018_caution(self) -> None:
        topic = generator.TOPICS[0]
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-24_Learning-Session.md"
        ).read_text(encoding="utf-8")
        q2024 = next(item for item in topic["pyq_solutions"] if item[0] == "2024")
        self.assertEqual("official-key-confirmed", q2024[3])
        self.assertIn("official Series-A answer is **A - 1 only**", q2024[4])
        self.assertIn("Ans-2024-GS1.md", q2024[4])
        q2018 = next(item for item in topic["pyq_solutions"] if item[0] == "2018")
        self.assertIn("key-unavailable", q2018[3])
        self.assertIsNone(re.search(r"\bAnswer:\s*[A-D]\b", q2018[4], re.I))
        self.assertIn("structurally analogous", markdown)
        self.assertIn(
            "not cited as evidence that the Court invoked the Government "
            "of India Act, 1935",
            markdown,
        )

    def test_topic25_belligerency_resignation_and_august_offer_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-25_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "3 September 1939",
            "without consulting any Indian political leader or elected "
            "legislature",
            "resigned between October and November 1939",
            "22 December 1939",
            "Lahore Resolution of March 1940",
            "8 August 1940",
            "minority consent",
            "no immediate national government",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("India was consulted before", markdown)
        self.assertNotIn(
            "August Offer gave an immediate national government", markdown
        )
        self.assertNotIn("one full day after ratification", markdown)

    def test_topic25_individual_satyagraha_and_cripps_scheme_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-25_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "17 October 1940",
            "Vinoba Bhave",
            "Jawaharlal Nehru",
            "not a mass movement",
            "Cripps arrived in India in March 1942",
            "late March 1942",
            "Dominion status after the war",
            "opt out of the new Indian union",
            "nominated by their rulers",
            "Defence and the general conduct of the war remained under "
            "British control",
            "no immediate responsible national cabinet",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Individual Satyagraha was a mass movement", markdown)
        self.assertNotIn("Cripps proposals gave immediate self-government", markdown)

    def test_topic25_multi_party_rejection_and_post_dated_cheque_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-25_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "Congress objected to the deferred",
            "League objected that it did not guarantee Pakistan",
            "Sikh, Hindu Mahasabha and some princely opinion raised "
            "separate objections",
            "post-dated cheque",
            "crashing bank",
            "uncertain provenance",
            "applies it solely to the Cripps proposals, never to the "
            "August Offer",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "every party rejected the Cripps proposals for the same reason",
            markdown,
        )

    def test_topic25_quit_india_two_stage_zero_hour_and_underground_safeguards(
        self,
    ) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-25_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "Wardha on 14 July 1942",
            "Bombay on 8 August 1942",
            "should never be collapsed into a single date",
            "began early on 9 August 1942",
            "following morning and calendar day",
            "not a full 24 hours later",
            "Do or Die",
            "Aruna Asaf Ali",
            "Gowalia Tank",
            "Usha Mehta",
            "Jayaprakash Narayan",
            "Ram Manohar Lohia",
            "Ballia",
            "Jatiya Sarkar",
            "Prati Sarkar",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Quit India resolution was adopted on a single date", markdown)
        self.assertNotIn(
            "arrests began on the same day as the Bombay resolution", markdown
        )

    def test_topic25_social_base_alignments_and_results_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-25_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "students, workers, peasants",
            "regionally variable intensity",
            "sabotage",
            "non-violent creed",
            "avoids stating unsupported exact casualty or arrest totals",
            "League stayed aloof from or opposed",
            "People's War line",
            "Hindu Mahasabha and many princely rulers",
            "suppressed by the government within months",
            "did not by itself win India's independence",
            "demonstrated the depth of popular anti-colonial sentiment",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Quit India alone won India's independence", markdown)

    def test_topic25_exact_pyqs_and_key_status(self) -> None:
        topic = generator.TOPICS[1]
        cards = {(item[0], item[1]): item for item in topic["pyq_solutions"]}
        mains2024 = cards[("2024", "Mains GS-I Q3")]
        self.assertIn(
            "What were the events that led to the Quit India Movement? "
            "Point out its results.",
            mains2024[2],
        )
        self.assertEqual(
            "official-mains-question-verbatim-confirmed", mains2024[3]
        )
        prelims2021 = cards[("2021", "Prelims GS-I Q43")]
        prelims2022 = cards[("2022", "Prelims GS-I Q54")]
        for card in (prelims2021, prelims2022):
            self.assertIn("neutral-demand-only", card[3])
            self.assertIsNone(re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I))

    def test_topic25_current_bridge_is_bounded(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-25_Learning-Session.md"
        ).read_text(encoding="utf-8")
        self.assertIn("InsightsIAS", markdown)
        self.assertIn("8 August 2026", markdown)
        self.assertIn(
            "could not be independently verified against any official "
            "source",
            markdown,
        )
        self.assertIn(
            "makes no claim about any 2026 official or parliamentary "
            "tribute",
            markdown,
        )
        self.assertNotIn("official parliamentary tribute", markdown)

    def test_ascii_and_graphical_specs_are_exact(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        self.assertEqual(set(generator.PANEL_DATA), set(specs))
        payload = json.loads(generator.ASCII_PATH.read_text(encoding="utf-8"))
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
                    len([line for line in panel.body.splitlines() if line.strip()]) >= 4
                    for panel in spec.panels
                ),
                key,
            )
            graph = json.loads(
                (generator.GRAPHICAL_DIR / f"{key}.json").read_text(encoding="utf-8")
            )
            self.assertEqual([], carvaka_flowchart.validate_spec(graph), key)
            self.assertEqual(13, len(graph["stages"]), key)

    def test_generation_manifests_are_tracker_free_generation_one(self) -> None:
        required_sources = {
            "knowledge-export\\Prelims PYQ\\2024-GS1-Set A.md",
            "knowledge-export\\Prelims PYQ\\Ans-2024-GS1.md",
            "knowledge-export\\Prelims PYQ\\QP-CSP-18-GS-I-C.pdf.md",
            "knowledge-export\\Mains PYQ\\UPSC Mains 2024 GS Paper I.md",
        }
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
            self.assertEqual("strict-abcd-cycle", manifest["mcq_answer_policy"])
            self.assertEqual(12, manifest["ascii_panel_count"])
            self.assertEqual(13, manifest["graphical_stage_count"])
            self.assertTrue(
                required_sources.issubset(set(manifest["official_question_sources"]))
            )
            source = (ROOT / manifest["source_markdown"]).read_text(encoding="utf-8")
            canonical = (ROOT / manifest["source_canonical"]).read_text(encoding="utf-8")
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
        self.assertTrue(
            all("KEY TERMS:" not in item for item in generator.SESSION_VISUALS.values())
        )
        self.assertTrue(
            all(
                "an evidence-led unit" not in item
                for item in generator.SESSION_DEFINITIONS.values()
            )
        )

    def test_ascii_master_registers_the_new_spec(self) -> None:
        self.assertIn(
            "modern-indian-history-24-25-2026-08-31-sequential.json",
            ascii_master.MANUAL_SPEC_FILENAMES,
        )

    def test_authoring_generator_has_no_finalize_or_publish_side_effects(self) -> None:
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

    def test_import_does_not_mutate_topics_22_23(self) -> None:
        self.assertEqual(
            ["modern-indian-history-22", "modern-indian-history-23"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-22", "modern-indian-history-23"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(all(len(panels) == 12 for panels in previous.PANEL_DATA.values()))
        self.assertEqual(
            "modern-indian-history-22-23-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )

    def test_import_does_not_mutate_shared_base_globals(self) -> None:
        import generate_modern_history_09_13_sequential as base

        prior_date = base.DATE
        prior_ascii_path = base.ASCII_PATH
        prior_topics = base.TOPICS
        prior_panel_data = base.PANEL_DATA
        # Importing generator must never leave configured_base() overrides
        # applied to the shared base module outside of a `with` block.
        self.assertEqual(prior_date, base.DATE)
        self.assertEqual(prior_ascii_path, base.ASCII_PATH)
        self.assertEqual(prior_topics, base.TOPICS)
        self.assertEqual(prior_panel_data, base.PANEL_DATA)
        with generator.configured_base():
            self.assertEqual(generator.DATE, base.DATE)
            self.assertEqual(generator.ASCII_PATH, base.ASCII_PATH)
            self.assertEqual(generator.TOPICS, base.TOPICS)
        # The context manager must restore every overridden global exactly.
        self.assertEqual(prior_date, base.DATE)
        self.assertEqual(prior_ascii_path, base.ASCII_PATH)
        self.assertIs(prior_topics, base.TOPICS)
        self.assertIs(prior_panel_data, base.PANEL_DATA)


if __name__ == "__main__":
    unittest.main()
