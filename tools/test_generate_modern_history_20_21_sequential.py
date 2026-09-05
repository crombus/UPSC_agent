"""Regression tests for Modern History learner-v2 Topics 20-21."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart
import generate_modern_history_18_19_sequential as previous
import generate_modern_history_20_21_sequential as generator
import notions_style_ascii_master as ascii_master


class ModernHistory2021GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-20", "modern-indian-history-21"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "Non-Cooperation & the Khilafat Movement (1919\u20131922)",
                "Swarajists, Constructive Work & Revolutionaries of the "
                "1920s (HSRA, Bhagat Singh)",
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
            self.assertEqual(6, markdown.count("### ORIGINAL MAINS"), key)
            self.assertNotIn(" is the part of ", markdown, key)
            self.assertNotIn(" -> and -> ", markdown, key)
            self.assertNotIn("an evidence-led unit connecting", markdown, key)
            self.assertNotIn("Missing topic-specific session visual", markdown, key)
            generator.self_check(
                config,
                markdown,
                workbook,
                len(sessions),
                graphical_path,
            )

    def test_chauri_chaura_date_is_corrected(self) -> None:
        key = "modern-indian-history-20"
        topic20 = next(
            config for config in generator.TOPICS if config["key"] == key
        )
        markdown = (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
            encoding="utf-8"
        )
        workbook = (generator.SESSION_DIR / f"{key}_Solved-Workbook.md").read_text(
            encoding="utf-8"
        )
        canonical = Path(topic20["canonical"]).read_text(encoding="utf-8")
        basic_owner = Path(topic20["basic"]).read_text(encoding="utf-8")
        advanced_owner = Path(topic20["advanced"]).read_text(encoding="utf-8")
        for label, text in (
            ("generated learning session", markdown),
            ("generated solved workbook", workbook),
            ("generated canonical package", canonical),
            ("basic source owner", basic_owner),
            ("advanced source owner", advanced_owner),
        ):
            self.assertIn("4 February 1922", text, label)
            self.assertIn("12 February 1922", text, label)
            self.assertNotIn("5 February 1922", text, label)

    def test_topic20_withdrawal_debate_and_current_bridge_reconciled(self) -> None:
        key = "modern-indian-history-20"
        topic20 = next(
            config for config in generator.TOPICS if config["key"] == key
        )
        markdown = (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
            encoding="utf-8"
        )
        canonical = Path(topic20["canonical"]).read_text(encoding="utf-8")
        for label, text in (
            ("generated learning session", markdown),
            ("generated canonical package", canonical),
        ):
            self.assertIn("Palme Dutt", text, label)
            self.assertIn("Bipin Chandra", text, label)
            self.assertIn("Gujarat Vidyapith", text, label)
            self.assertIn("106th year", text, label)
            self.assertNotIn("centenary of Gujarat Vidyapith", text, label)
            self.assertNotIn("Gujarat Vidyapith centenary", text, label)

    def test_topic20_2025_prelims_official_key_reconciled(self) -> None:
        key = "modern-indian-history-20"
        topic20 = next(
            config for config in generator.TOPICS if config["key"] == key
        )
        markdown = (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
            encoding="utf-8"
        )
        canonical = Path(topic20["canonical"]).read_text(encoding="utf-8")
        pdf_path = (
            ROOT / "books" / "prelima_question_paper_answers" / "Ans-2025-GS1.pdf"
        )
        self.assertTrue(pdf_path.is_file())
        self.assertIn(pdf_path, generator.OFFICIAL_QUESTION_SOURCES)
        for label, text in (
            ("generated learning session", markdown),
            ("generated canonical package", canonical),
        ):
            # Confirmed directly from the local official PDF, not the
            # garbled Markdown/OCR export.
            self.assertIn("Ans-2025-GS1.pdf", text, label)
            self.assertIn("Series A", text, label)
            self.assertIn("Krishna Kant Malaviya", text, label)
            self.assertNotIn("remains an open local gap", text, label)
            self.assertNotIn("unresolved narrative gap is unchanged", text, label)
        workbook = (
            generator.SESSION_DIR / f"{key}_Solved-Workbook.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Krishna Kant Malaviya", workbook)
        self.assertNotIn("unresolved narrative gap is unchanged", workbook)
        confirmed_cards = {
            card[1]: card
            for card in topic20["pyq_solutions"]
            if card[3] == "official-key-confirmed"
        }
        self.assertEqual(
            {"Prelims GS-I Q12", "Prelims GS-I Q20", "Prelims GS-I Q73"},
            set(confirmed_cards),
        )
        self.assertIn("**C**", confirmed_cards["Prelims GS-I Q12"][4])
        self.assertIn("**C**", confirmed_cards["Prelims GS-I Q20"][4])
        self.assertIn("**B**", confirmed_cards["Prelims GS-I Q73"][4])
        self.assertIn(
            "Madan Mohan Malaviya", confirmed_cards["Prelims GS-I Q73"][4]
        )
        # Q71 ("Sedition has become my religion") stays routed away from this
        # topic's core content; its confirmed key (B, Dandi Salt Law) is
        # surfaced only as a trap, never as a Topic 20 pyq_solutions card.
        self.assertNotIn(
            "Prelims GS-I Q71",
            {card[1] for card in topic20["pyq_solutions"]},
        )
        self.assertIn("Q71", markdown)
        self.assertIn("Dandi Salt Law", markdown)

    def test_hra_hsra_and_kakori_are_not_merged(self) -> None:
        key = "modern-indian-history-21"
        markdown = (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "do not place bhagat singh in the kakori case", markdown.casefold()
        )
        self.assertIn("Naujawan Bharat Sabha", markdown)
        self.assertIn("Jatin Das", markdown)
        self.assertIn("Lahore Conspiracy Case", markdown)

    def test_topic21_reconciled_dossier_facts(self) -> None:
        key = "modern-indian-history-21"
        topic21 = next(
            config for config in generator.TOPICS if config["key"] == key
        )
        markdown = (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
            encoding="utf-8"
        )
        canonical = Path(topic21["canonical"]).read_text(encoding="utf-8")
        for label, text in (
            ("generated learning session", markdown),
            ("generated canonical package", canonical),
        ):
            # HRA/HSRA location and date specificity, one lineage not rivals.
            self.assertIn("Kanpur", text, label)
            self.assertIn("October 1924", text, label)
            self.assertIn("Ferozeshah Kotla", text, label)
            self.assertIn("9-10 September 1928", text, label)
            self.assertIn("not rival bodies", text, label)
            # Swaraj Party Gaya/December 1922 vs 1 January 1923 variance.
            self.assertIn("Gaya", text, label)
            self.assertIn("December 1922", text, label)
            self.assertIn("1 January 1923", text, label)
            # Swarajya Sabha vs Swaraj Party trap.
            self.assertIn("Swarajya Sabha", text, label)
            # Jatin Das fast-length source variance.
            self.assertIn("63", text, label)
            self.assertIn("64", text, label)
            # Assembly Bomb Case vs Lahore Conspiracy Case as separate proceedings.
            self.assertIn("Assembly Bomb Case", text, label)
            self.assertIn("life imprisonment", text, label)
            # Chittagong organisational separateness.
            self.assertIn("organisationally separate", text, label)
        # Current-affairs bridge: Shaheed Diwas 2026, Parliament Street courtroom
        # bounded to the Assembly Bomb Case trial site only.
        self.assertIn("23 March 2026", markdown)
        self.assertIn("Parliament Street", markdown)
        self.assertIn("95th anniversary", markdown)
        bridge_match = re.search(
            r"Parliament Street[^.]*\.", markdown
        )
        self.assertIsNotNone(bridge_match)
        self.assertNotIn("Lahore Conspiracy Case", bridge_match.group(0))
        # 2018 Swarajya Sabha PYQ card carries no invented answer letter.
        q79 = next(
            card for card in topic21["pyq_solutions"] if card[0] == "2018"
        )
        self.assertIsNone(re.search(r"\bAnswer:\s*[A-D]\b", q79[4], re.I))

    def test_official_question_inventory_and_routed_cards(self) -> None:
        names = {path.name for path in generator.OFFICIAL_QUESTION_SOURCES}
        self.assertTrue(
            {
                "2025-GS1-Set A.md",
                "Ans-2025-GS1.md",
                "2025-GS1-Set A.pdf",
                "Ans-2025-GS1.pdf",
                "2026-GS1-Set A.md",
                "Ans-2026-GS1-Provisional.md",
                "QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md",
                "Gen_St_P1.pdf.md",
                "QP-CSP-18-GS-I-C.pdf.md",
            }.issubset(names)
        )
        topic20 = generator.TOPICS[0]
        topic21 = generator.TOPICS[1]
        self.assertEqual(
            {"2025", "2026", "2021"},
            {card[0] for card in topic20["pyq_solutions"]},
        )
        self.assertEqual(
            {"2020", "2018"},
            {card[0] for card in topic21["pyq_solutions"]},
        )
        unkeyed_cards = [
            card for card in topic20["pyq_solutions"] if "key-unavailable" in card[3]
        ]
        self.assertEqual(1, len(unkeyed_cards))
        self.assertTrue(
            all(
                re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I) is None
                for card in unkeyed_cards
            )
        )
        # 2025 Series-A official key, independently confirmed from the local
        # PDF answer key (not the garbled Markdown/OCR export): Q12=C, Q20=C,
        # Q73=B.
        confirmed_cards = {
            card[1]: card
            for card in topic20["pyq_solutions"]
            if card[3] == "official-key-confirmed"
        }
        self.assertEqual(
            {"Prelims GS-I Q12", "Prelims GS-I Q20", "Prelims GS-I Q73"},
            set(confirmed_cards),
        )
        self.assertIn("**C**", confirmed_cards["Prelims GS-I Q12"][4])
        self.assertIn("**C**", confirmed_cards["Prelims GS-I Q20"][4])
        self.assertIn("**B**", confirmed_cards["Prelims GS-I Q73"][4])
        self.assertIn("Malaviya", confirmed_cards["Prelims GS-I Q73"][4])
        for card in confirmed_cards.values():
            self.assertIn("Ans-2025-GS1.pdf", card[4])
        self.assertEqual(2, len(topic21["pyq_solutions"]))
        q13_2020 = next(
            card for card in topic21["pyq_solutions"] if card[0] == "2020"
        )
        q79_2018 = next(
            card for card in topic21["pyq_solutions"] if card[0] == "2018"
        )
        self.assertEqual("bounded-model", q13_2020[3])
        self.assertIn("open-evidence-gap-key-unavailable", q79_2018[3])
        self.assertIsNone(
            re.search(r"\bAnswer:\s*[A-D]\b", q79_2018[4], re.I)
        )
        self.assertIn("Swarajya Sabha", q79_2018[2])

    def test_mains_pyq_exact_official_wording_and_provenance(self) -> None:
        source_names = {path.name for path in generator.OFFICIAL_QUESTION_SOURCES}
        self.assertIn("QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md", source_names)
        self.assertIn("Gen_St_P1.pdf.md", source_names)
        gs1_2021 = (
            ROOT
            / "knowledge-export"
            / "Mains PYQ"
            / "QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md"
        )
        gen_st_2020 = ROOT / "knowledge-export" / "Mains PYQ" / "Gen_St_P1.pdf.md"
        self.assertIn(gs1_2021, generator.OFFICIAL_QUESTION_SOURCES)
        self.assertIn(gen_st_2020, generator.OFFICIAL_QUESTION_SOURCES)

        topic20 = generator.TOPICS[0]
        topic21 = generator.TOPICS[1]
        q12 = next(
            card for card in topic20["pyq_solutions"] if card[1] == "GS-I Q12"
        )
        q13 = next(
            card for card in topic21["pyq_solutions"] if card[1] == "GS-I Q13"
        )
        self.assertIn(
            "Bring out the constructive programmes of Mahatma Gandhi during "
            "Non-Cooperation Movement and Civil Disobedience Movement. "
            "(Answer in 250 words)",
            q12[2],
        )
        self.assertIn(
            "Since the decade of the 1920s, the national movement acquired "
            "various ideological strands and thereby expanded its social "
            "base. Discuss. (Answer in 250 words)",
            q13[2],
        )
        self.assertIn("QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md", q12[2])
        self.assertIn("Gen_St_P1.pdf.md", q13[2])

    def test_ascii_and_graphical_specs_are_exact(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        self.assertEqual(set(generator.PANEL_DATA), set(specs))
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
                (generator.GRAPHICAL_DIR / f"{key}.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual([], carvaka_flowchart.validate_spec(graph), key)
            self.assertEqual(13, len(graph["stages"]), key)

    def test_generation_manifests_are_tracker_free_generation_one(self) -> None:
        required_question_sources = {
            "knowledge-export\\Prelims PYQ\\2025-GS1-Set A.md",
            "knowledge-export\\Prelims PYQ\\Ans-2025-GS1.md",
            "knowledge-export\\Prelims PYQ\\2026-GS1-Set A.md",
            "knowledge-export\\Prelims PYQ\\Ans-2026-GS1-Provisional.md",
            "knowledge-export\\Mains PYQ\\QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf.md",
            "knowledge-export\\Mains PYQ\\Gen_St_P1.pdf.md",
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
                required_question_sources.issubset(
                    set(manifest["official_question_sources"])
                )
            )
            self.assertTrue((ROOT / manifest["source_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["workbook_markdown"]).is_file())
            self.assertTrue((ROOT / manifest["source_canonical"]).is_file())

    def test_authored_visual_and_definition_maps_are_complete(self) -> None:
        titles = {
            item[0]
            for plans in generator.SESSION_PLANS.values()
            for item in plans
        }
        self.assertEqual(titles, set(generator.SESSION_VISUALS))
        self.assertEqual(titles, set(generator.SESSION_DEFINITIONS))
        self.assertTrue(
            all("KEY TERMS:" not in visual for visual in generator.SESSION_VISUALS.values())
        )
        self.assertTrue(
            all(
                "an evidence-led unit" not in definition
                for definition in generator.SESSION_DEFINITIONS.values()
            )
        )

    def test_import_does_not_mutate_topics_18_19(self) -> None:
        self.assertEqual(
            ["modern-indian-history-18", "modern-indian-history-19"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            [
                "First World War, the Home Rule League & the Lucknow Pact "
                "(1914\u20131918)",
                "Gandhi's Rise: Champaran, Kheda, Ahmedabad; Rowlatt & "
                "Jallianwala Bagh (1917\u20131919)",
            ],
            [config["title"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-18", "modern-indian-history-19"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(all(len(panels) == 12 for panels in previous.PANEL_DATA.values()))
        self.assertEqual(
            "modern-indian-history-18-19-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )


if __name__ == "__main__":
    unittest.main()
