"""Regression tests for Modern History learner-v2 Topics 22-23."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_20_21_sequential as previous
import generate_modern_history_22_23_sequential as generator
import notions_style_ascii_master as ascii_master


class ModernHistory2223GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-22", "modern-indian-history-23"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "Simon Commission, Nehru Report, Civil Disobedience & Round "
                "Table Conferences (1927\u20131934)",
                "Left, Peasant, Workers' & States' Peoples' Movements (1930s)",
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
            "22_Simon-Commission-Nehru-Report-Civil-Disobedience-"
            "Round-Table-Conferences_Complete-Topic-Package.md",
            Path(generator.TOPICS[0]["canonical"]).name,
        )
        self.assertEqual(
            "23_Left-Peasant-Workers-States-Peoples-Movements-1930s_"
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
            generator.self_check(
                config,
                markdown,
                workbook,
                len(sessions),
                graphical_path,
            )

    def test_topic22_chronology_and_constitutional_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-22_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "appointed in 1927",
            "3 February 1928",
            "30 October 1928",
            "17 November 1928",
            "Dominion Status",
            "qualified minority reservations",
            "Jinnah's Fourteen Points",
            "one-year Dominion ultimatum",
            "Irwin's 31 October 1929 declaration",
            "Delhi Manifesto",
            "Purna Swaraj",
            "26 January 1930",
            "12 March 1930",
            "6 April 1930",
            "78 chosen followers",
            "about 385/388 km",
            "some historical sources state 240 miles",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Nehru Report demanded complete independence", markdown)
        self.assertNotIn("Simon Commission included Indian", markdown)

    def test_topic22_regional_pact_and_rtc_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-22_Learning-Session.md"
        ).read_text(encoding="utf-8")
        for phrase in [
            "Vedaranyam",
            "Payyannur",
            "sibirams",
            "Khudai Khidmatgars",
            "Garhwali soldiers refused to fire",
            "Dharasana",
            "Sarojini Naidu",
            "Sholapur",
            "Muslim participation was uneven",
            "Congress was absent from the First RTC",
            "Gandhi attended the Second RTC as sole Congress representative",
            "Congress was absent from the limited Third RTC",
            "5 March 1931",
            "no inquiry into police excesses",
            "Fundamental Rights and the National Economic Programme",
        ]:
            self.assertIn(phrase, markdown)

    def test_topic22_poona_pact_is_balanced_and_number_is_qualified(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-22_Learning-Session.md"
        ).read_text(encoding="utf-8")
        for phrase in [
            "20 September 1932",
            "24 September 1932",
            "reserved seats in joint electorates",
            "Gandhi feared separate electorates",
            "Ambedkar feared joint electorates",
            "coercive bargaining context",
            "local Bipan Chandra OCR gives 147",
            "148 is the widespread convention",
            "early April 1934",
        ]:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Poona Pact accepted separate electorates", markdown)

    def test_topic22_official_2025_key_and_current_bridge(self) -> None:
        topic = generator.TOPICS[0]
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-22_Learning-Session.md"
        ).read_text(encoding="utf-8")
        card = next(item for item in topic["pyq_solutions"] if item[0] == "2025")
        self.assertEqual("official-key-confirmed", card[3])
        self.assertIn("Series-A answer is **A - The Poona Pact**", card[4])
        self.assertIn("Ans-2025-GS1.pdf", card[4])
        q2020 = next(item for item in topic["pyq_solutions"] if item[0] == "2020")
        self.assertIn("key-unavailable", q2020[3])
        self.assertIsNone(re.search(r"\bAnswer:\s*[A-D]\b", q2020[4], re.I))
        self.assertIn("96th calendar anniversary", markdown)
        self.assertIn("National Salt Satyagraha Memorial", markdown)
        self.assertNotIn("2026 minister tribute", markdown)

    def test_topic23_scope_and_organisation_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-23_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "AITUC was founded in 1920",
            "Lala Lajpat Rai as its first president",
            "Tashkent 1920 identifies an international/emigre initiative",
            "Kanpur 1925 an all-India organisation inside India",
            "Workers' and Peasants' Parties",
            "Meerut Conspiracy Case of 1929-33",
            "avoids a precise accused count",
            "Bombay in October 1934",
            "J.P. Narayan",
            "Acharya Narendra Dev",
            "Ram Manohar Lohia",
            "Minoo Masani",
            "CSP and CPI had interactions, but they were not the same organisation",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("CSP and CPI were identical", markdown)

    def test_topic23_kisan_ministry_and_social_content_safeguards(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-23_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "Bihar Provincial Kisan Sabha",
            "founded by Swami Sahajanand Saraswati in 1929",
            "Lucknow in April 1936",
            "Sahajanand Saraswati as president",
            "N.G. Ranga as general secretary",
            "Kisan Manifesto",
            "Faizpur in December 1936",
            "Sub-tenants of occupancy tenants",
            "Agricultural labourers",
            "Karachi 1931",
            "National Planning Committee in 1938",
            "Congress remained broad, multi-class",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertIn(
            '"Left influence" does not mean Congress became communist',
            markdown,
        )

    def test_topic23_states_bose_and_period_boundaries(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-23_Learning-Session.md"
        ).read_text(encoding="utf-8")
        required = [
            "first AISPC convention in December 1927",
            "Balwantrai Mehta",
            "Maniklal Kothari",
            "G.R. Abhayankar",
            "princely autocracy",
            "Praja Mandals",
            "Rajkot",
            "Haripura in 1938",
            "Tripuri in 1939",
            "formed the Forward Bloc in 1939",
            "institutional and ideological crisis",
            "Ulgulan of 1899-1900",
            "Warli belongs to 1945",
            "Tebhaga in 1946",
            "Punnapra-Vayalar occurred in Travancore in 1946",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("first AISPC convention in 1936", markdown)

    def test_topic23_exact_pyqs_and_provisional_key_boundary(self) -> None:
        topic = generator.TOPICS[1]
        cards = {(item[0], item[1]): item for item in topic["pyq_solutions"]}
        self.assertIn(
            "Many voices had strengthened and enriched the nationalist movement "
            "during the Gandhian phase. Elaborate. (Answer in 250 words)",
            cards[("2019", "GS-I Q11")][2],
        )
        self.assertIn(
            "Since the decade of the 1920s, the national movement acquired "
            "various ideological strands and thereby expanded its social base. "
            "Discuss. (Answer in 250 words)",
            cards[("2020", "GS-I Q13")][2],
        )
        self.assertIn(
            "How did the colonial rule affect the tribals in India and what was "
            "the tribal response to the colonial oppression? (Answer in 250 words)",
            cards[("2023", "GS-I Q13")][2],
        )
        ulgulan = next(item for item in topic["pyq_solutions"] if item[1] == "Prelims GS-I Q35")
        forward = next(item for item in topic["pyq_solutions"] if item[1] == "Prelims GS-I Q16")
        self.assertIsNone(re.search(r"\bAnswer:\s*[A-D]\b", ulgulan[4], re.I))
        self.assertIn("provisional-key-no-answer-letter", forward[3])
        self.assertIsNone(re.search(r"\bAnswer:\s*[A-D]\b", forward[4], re.I))

    def test_topic23_current_bridge_is_bounded(self) -> None:
        markdown = (
            generator.SESSION_DIR
            / "modern-indian-history-23_Learning-Session.md"
        ).read_text(encoding="utf-8")
        self.assertIn("1 July 2026", markdown)
        self.assertIn("organisational-lineage", markdown)
        self.assertIn("kept separate from the history of the 1930s", markdown)
        self.assertNotIn("Arabian Post", markdown)

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
            graph = json.loads(
                (generator.GRAPHICAL_DIR / f"{key}.json").read_text(encoding="utf-8")
            )
            self.assertEqual([], carvaka_flowchart.validate_spec(graph), key)
            self.assertEqual(13, len(graph["stages"]), key)

    def test_generation_manifests_are_tracker_free_generation_one(self) -> None:
        required_sources = {
            "knowledge-export\\Prelims PYQ\\2025-GS1-Set A.md",
            "books\\prelima_question_paper_answers\\Ans-2025-GS1.pdf",
            "knowledge-export\\Prelims PYQ\\2026-GS1-Set A.md",
            "knowledge-export\\Prelims PYQ\\Ans-2026-GS1-Provisional.md",
            "knowledge-export\\Prelims PYQ\\CSP_2020_GS_Paper-1.pdf.md",
            "knowledge-export\\Mains PYQ\\QP-CSM19-GeneralStudies-I.pdf.md",
            "knowledge-export\\Mains PYQ\\Gen_St_P1.pdf.md",
            "knowledge-export\\Mains PYQ\\QP-CSM-23-GENERAL-STUDIES-PAPER-I-180923.pdf.md",
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
        self.assertTrue(all("KEY TERMS:" not in item for item in generator.SESSION_VISUALS.values()))
        self.assertTrue(
            all(
                "an evidence-led unit" not in item
                for item in generator.SESSION_DEFINITIONS.values()
            )
        )

    def test_ascii_master_registers_the_new_spec(self) -> None:
        self.assertIn(
            "modern-indian-history-22-23-2026-08-31-sequential.json",
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

    def test_import_does_not_mutate_topics_20_21(self) -> None:
        self.assertEqual(
            ["modern-indian-history-20", "modern-indian-history-21"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-20", "modern-indian-history-21"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(all(len(panels) == 12 for panels in previous.PANEL_DATA.values()))
        self.assertEqual(
            "modern-indian-history-20-21-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )


if __name__ == "__main__":
    unittest.main()
