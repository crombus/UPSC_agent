"""Regression tests for Modern History learner-v2 Topics 26-27."""

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
import generate_modern_history_24_25_sequential as previous
import generate_modern_history_26_27_sequential as generator
import notions_style_ascii_master as ascii_master


def session_markdown(key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
        encoding="utf-8"
    )


class ModernHistory2627GeneratorTests(unittest.TestCase):
    def test_two_new_topics_are_configured(self) -> None:
        self.assertEqual(
            ["modern-indian-history-26", "modern-indian-history-27"],
            [config["key"] for config in generator.TOPICS],
        )
        self.assertEqual(
            [
                "Post-War Upsurge: INA, RIN Mutiny & the Cabinet Mission "
                "(1945\u20131946)",
                "Independence & Partition (1946\u20131947)",
            ],
            [config["title"] for config in generator.TOPICS],
        )
        self.assertTrue(
            all(len(config["facts"]) == 20 for config in generator.TOPICS)
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
            "26_Post-War-Upsurge-INA-RIN-Mutiny-Cabinet-Mission-1945-1946_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[0]["canonical"]).name,
        )
        self.assertEqual(
            "27_Independence-and-Partition-1946-1947_"
            "Complete-Topic-Package.md",
            Path(generator.TOPICS[1]["canonical"]).name,
        )

    def test_owner_files_are_the_declared_sources(self) -> None:
        for config in generator.TOPICS:
            for role in ("basic", "advanced"):
                path = Path(config[role])
                self.assertTrue(path.is_file(), str(path))
                self.assertEqual(role, path.parent.name)

    def test_generated_sessions_and_workbooks_pass_contracts(self) -> None:
        for config in generator.TOPICS:
            key = str(config["key"])
            workbook_path = generator.SESSION_DIR / f"{key}_Solved-Workbook.md"
            graphical_path = generator.GRAPHICAL_DIR / f"{key}.json"
            markdown = session_markdown(key)
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

    # ---------------- Topic 26 factual safeguards ----------------

    def test_topic26_two_inas_and_rash_behari_bose_role(self) -> None:
        markdown = session_markdown("modern-indian-history-26")
        required = [
            "raised in 1942 from Indian prisoners of war",
            "Mohan Singh",
            "collapsed by early 1943",
            "reached Southeast Asia in May 1943",
            "October 1943 proclaimed the Provisional Government of Azad Hind",
            "Indian Independence League",
            "not a field commander",
            "must never be treated as one continuous force",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Rash Behari Bose commanded the INA", markdown)
        self.assertNotIn(
            "the first INA and Bose's INA are the same force", markdown
        )

    def test_topic26_military_failure_versus_trial_effect(self) -> None:
        markdown = session_markdown("modern-indian-history-26")
        required = [
            "Imphal campaign was launched on 8 March 1944",
            "Imphal-Kohima",
            "military record was one of defeat",
            "decisive effect was political rather than military",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("INA won India's independence", markdown)
        self.assertNotIn("INA alone won India's independence", markdown)

    def test_topic26_red_fort_trial_names_and_sentences(self) -> None:
        markdown = session_markdown("modern-indian-history-26")
        required = [
            "Shah Nawaz Khan",
            "Prem Sahgal (also spelt Sehgal)",
            "Gurbaksh Singh Dhillon",
            "a Muslim, a Hindu and a Sikh",
            "Bhulabhai Desai",
            "remitted the sentences",
            "were not carried out",
            "no officer tried in that case was executed",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("the Red Fort officers were executed", markdown)

    def test_topic26_rin_start_scale_and_limits(self) -> None:
        markdown = session_markdown("modern-indian-history-26")
        required = [
            "began on 18 February 1946 at HMIS Talwar in Bombay",
            "commonly cited estimates",
            "roughly 20,000 ratings, 78 ships and 20 shore establishments",
            "cautions against asserting ship numbers",
            "short-lived",
            "not a Congress-led nationwide revolution",
            "did not by itself end British rule",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("exactly 78 ships", markdown)
        self.assertNotIn("RIN uprising was a Congress-led", markdown)

    def test_topic26_rin_did_not_cause_the_cabinet_mission_dispatch(
        self,
    ) -> None:
        """Bipan Chandra, book PDF p. 512: the dispatch decision preceded the
        uprising, so dispatch causation is untenable."""

        key = "modern-indian-history-26"
        markdown = session_markdown(key)
        workbook = (
            generator.SESSION_DIR / f"{key}_Solved-Workbook.md"
        ).read_text(encoding="utf-8")
        canonical = Path(generator.TOPICS[0]["canonical"]).read_text(
            encoding="utf-8"
        )
        ascii_spec = generator.ASCII_PATH.read_text(encoding="utf-8")
        graphical = (generator.GRAPHICAL_DIR / f"{key}.json").read_text(
            encoding="utf-8"
        )

        required = [
            "22 January 1946",
            "19 February 1946",
            "did not cause or trigger the dispatch of the Cabinet Mission",
            "dispatch-causation claim is explicitly untenable",
            "crisis of coercive legitimacy",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown, phrase)
            self.assertIn(phrase, canonical, phrase)
        self.assertIn("22 January 1946", workbook)
        self.assertIn(
            "did not cause or trigger the dispatch of the Cabinet Mission",
            workbook,
        )

        for spec_text in (ascii_spec, graphical):
            self.assertIn("22 JAN 1946", spec_text)
            self.assertIn(
                "did not cause or trigger the dispatch of the Cabinet "
                "Mission",
                spec_text,
            )

        banned = [
            "caused the dispatch of the Cabinet Mission",
            "triggered the dispatch of the Cabinet Mission",
            "forced the British to send the Cabinet Mission",
            "compelled the British to send the Cabinet Mission",
            "Cabinet Mission was sent because of the RIN",
            "Cabinet Mission was a response to the RIN",
            "Cabinet Mission was announced in response to the naval",
            "uprising brought the Cabinet Mission",
            "naval strike produced the Cabinet Mission",
            "Cabinet Mission was despatched because of the RIN",
        ]
        for phrase in banned:
            self.assertIn(phrase, generator.FORBIDDEN_TOPIC_PHRASES[key])
            for text in (markdown, workbook, canonical, ascii_spec, graphical):
                self.assertNotIn(phrase.casefold(), text.casefold(), phrase)

    def test_topic26_dispatch_chronology_is_ordered_and_enforced(self) -> None:
        key = "modern-indian-history-26"
        chronology = generator.TOPIC_CHRONOLOGY[key]
        for marker in ("22 January 1946", "18 February 1946", "19 February 1946"):
            self.assertIn(marker, chronology)
        self.assertLess(
            chronology.index("22 January 1946"),
            chronology.index("18 February 1946"),
        )
        self.assertLess(
            chronology.index("18 February 1946"),
            chronology.index("19 February 1946"),
        )

        config = generator.TOPICS[0]
        fact_text = "\n".join(
            statement for _, statement in config["facts"]
        )
        cursor = -1
        for marker in chronology:
            found = fact_text.find(marker, cursor + 1)
            self.assertGreaterEqual(found, 0, marker)
            cursor = found

        markdown = session_markdown(key)
        self.assertIsNone(
            generator.assert_topic_safeguards(config, markdown)
        )
        with self.assertRaises(ValueError):
            generator.assert_topic_safeguards(
                config,
                markdown
                + "\nThe RIN uprising triggered the dispatch of the Cabinet "
                "Mission.\n",
            )
        with self.assertRaises(ValueError):
            generator.assert_topic_safeguards(
                config,
                markdown.replace(
                    "did not cause or trigger the dispatch of the Cabinet "
                    "Mission",
                    "shaped the political atmosphere",
                ),
            )

    def test_topic26_dispatch_safeguard_is_taught_and_traps_are_updated(
        self,
    ) -> None:
        key = "modern-indian-history-26"
        markdown = session_markdown(key)
        self.assertIn(
            "CHRONOLOGY TEST -> 22 JAN 1946 decision -> 18 FEB 1946 strike",
            markdown,
        )
        self.assertIn(
            "ALREADY DECIDED -> 22 JAN 1946 Cabinet resolves to send the "
            "Cabinet Mission",
            markdown,
        )
        self.assertIn(
            "P.S. Gupta in the Advanced owner concerns the wider INA "
            "agitation",
            markdown,
        )
        self.assertIn("book PDF page 512", markdown)
        traps = generator.TOPICS[0]["traps"]
        self.assertTrue(
            any(
                "did not cause or trigger the dispatch of the Cabinet "
                "Mission" in trap
                and "22 January 1946" in trap
                for trap in traps
            )
        )
        self.assertTrue(
            any(
                "22 January 1946" in str(term)
                for term in generator.TOPICS[0]["required_terms"]
            )
        )

    def test_topic26_divided_leadership_response(self) -> None:
        markdown = session_markdown("modern-indian-history-26")
        required = [
            "did not officially support the struggle",
            "Vallabhbhai Patel asked the ratings to surrender",
            "addressed to Muslim ratings alone",
            "sympathy strikes by workers and students",
            "communist and left organisations",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("all national leaders supported the RIN", markdown)

    def test_topic26_leadership_responses_are_not_flattened(self) -> None:
        """Bipan Chandra, book PDF pp. 511 and 514: Congress withheld official
        support on tactics and timing, Patel answered British repression, and
        Jinnah's advice went to Muslim ratings alone."""

        key = "modern-indian-history-26"
        markdown = session_markdown(key)
        workbook = (
            generator.SESSION_DIR / f"{key}_Solved-Workbook.md"
        ).read_text(encoding="utf-8")
        canonical = Path(generator.TOPICS[0]["canonical"]).read_text(
            encoding="utf-8"
        )
        ascii_spec = generator.ASCII_PATH.read_text(encoding="utf-8")
        graphical = (generator.GRAPHICAL_DIR / f"{key}.json").read_text(
            encoding="utf-8"
        )

        required = [
            "did not officially support the struggle",
            "tactics and the timing wrong",
            "overwhelming British mobilisation for repression",
            "22 February 1946",
            "addressed to Muslim ratings alone",
            "the rest of the ratings went to the Congress",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown, phrase)
            self.assertIn(phrase, canonical, phrase)
        for phrase in (
            "did not officially support the struggle",
            "addressed to Muslim ratings alone",
        ):
            self.assertIn(phrase, workbook, phrase)

        for spec_text in (ascii_spec, graphical):
            self.assertIn(
                "Congress withholds official support", spec_text
            )
            self.assertIn(
                "surrender advice addressed to Muslim ratings alone",
                spec_text,
            )

        banned = [
            "Congress officially supported the RIN",
            "Congress officially supported the uprising",
            "Congress officially backed the RIN",
            "every national leader supported the uprising",
            "Jinnah appealed to all the ratings",
            "Jinnah asked all the ratings",
            "Jinnah's advice was addressed to all ratings",
            "Patel and Jinnah made the same appeal",
            "Patel and Jinnah issued identical appeals",
        ]
        for phrase in banned:
            self.assertIn(phrase, generator.FORBIDDEN_TOPIC_PHRASES[key])
            for text in (markdown, workbook, canonical, ascii_spec, graphical):
                self.assertNotIn(phrase.casefold(), text.casefold(), phrase)

        config = generator.TOPICS[0]
        with self.assertRaises(ValueError):
            generator.assert_topic_safeguards(
                config,
                markdown
                + "\nPatel and Jinnah made the same appeal to the ratings.\n",
            )
        with self.assertRaises(ValueError):
            generator.assert_topic_safeguards(
                config,
                re.sub(
                    "addressed to Muslim ratings alone",
                    "addressed to the ratings",
                    markdown,
                    flags=re.IGNORECASE,
                ),
            )
        self.assertTrue(
            any(
                "did not officially support the RIN struggle" in trap
                and "Muslim ratings alone" in trap
                for trap in config["traps"]
            )
        )
        self.assertIn("book PDF pages 511 and 514", markdown)

    def test_topic26_cabinet_mission_documents_and_groups(self) -> None:
        markdown = session_markdown("modern-indian-history-26")
        required = [
            "Pethick-Lawrence, Stafford Cripps and A.V. Alexander",
            "long-term constitutional plan on 16 May 1946",
            "rejected a sovereign Pakistan",
            "foreign affairs, defence and communications",
            "finances required for those subjects",
            "Section A comprising Madras, Bombay, the United Provinces, "
            "Bihar, the Central Provinces and Orissa",
            "Section B comprising Punjab, the North-West Frontier Province, "
            "Sind and British Baluchistan",
            "Section C comprising Bengal and Assam",
            "grouping was not Partition",
            "interim-government proposal of 16 June 1946",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn(
            "Cabinet Mission accepted the demand for Pakistan", markdown
        )
        self.assertNotIn("grouping was Partition", markdown)

    def test_topic26_endgame_chain_and_election_qualification(self) -> None:
        markdown = session_markdown("modern-indian-history-26")
        required = [
            "acceptance on 6 June 1946",
            "7 July 1946",
            "withdrew the League's acceptance on 29 July 1946",
            "Direct Action Day followed on 16 August 1946",
            "Interim Government was formed on 2 September 1946",
            "League joined it on 26 October 1946",
            "6 December 1946",
            "Constituent Assembly met for the first time on 9 December 1946",
            "separate electorates",
            "about 10 per cent of the population",
            "was not a plebiscite",
            "wartime exhaustion",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("elections were a plebiscite", markdown)

    def test_topic26_pyq_cards_assert_no_answer_letters(self) -> None:
        topic = generator.TOPICS[0]
        cards = {(item[0], item[1]): item for item in topic["pyq_solutions"]}
        self.assertEqual(3, len(cards))
        for card in cards.values():
            self.assertIn("routed", card[3])
            self.assertIsNone(
                re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I), card[1]
            )
        self.assertIn(("2019", "Prelims GS-I Q15"), cards)
        self.assertIn(("2021", "Prelims GS-I Q47"), cards)
        self.assertIn(("2019", "Mains GS-I Q12"), cards)
        self.assertIn(
            "not as a verbatim official stem",
            cards[("2019", "Prelims GS-I Q15")][2],
        )

    def test_topic26_current_bridge_is_bounded_and_non_official(self) -> None:
        markdown = session_markdown("modern-indian-history-26")
        required = [
            "VisionIAS",
            "17 August 2026",
            "non-official study and current-affairs bridge",
            "not a government commemoration",
            "makes no claim that any official or governmental commemoration",
            "commonly cited estimates",
            "rather than as independently verified evidence",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    # ---------------- Topic 27 factual safeguards ----------------

    def test_topic27_mission_and_direct_action_boundaries(self) -> None:
        markdown = session_markdown("modern-indian-history-27")
        required = [
            "did not partition India",
            "Direct Action Day on 16 August 1946",
            "Great Calcutta Killings",
            "three separable things",
            "Noakhali, Bihar and the Punjab",
            "never to whole communities",
            "collectively guilty",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Cabinet Mission partitioned India", markdown)
        self.assertNotIn("the Cabinet Mission divided India", markdown)

    def test_topic27_attlee_and_mountbatten(self) -> None:
        markdown = session_markdown("modern-indian-history-27")
        required = [
            "Attlee announced on 20 February 1947",
            "not later than June 1948",
            "15 March 1946",
            "arrived in March 1947 as the last Viceroy",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic27_three_instruments_and_mechanisms(self) -> None:
        markdown = session_markdown("modern-indian-history-27")
        required = [
            "Mountbatten Plan announced on 3 June 1947 was a political plan",
            "was not an Act of Parliament",
            "separate votes of the notional Hindu-majority and "
            "Muslim-majority halves",
            "referendums in the North-West Frontier Province and Sylhet",
            "Two separate boundary commissions",
            "Cyril Radcliffe",
            "3 June Plan was the political decision",
            "Indian Independence Act was the legal enactment",
            "Radcliffe awards were the boundary mechanism",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Mountbatten Plan was passed by Parliament", markdown)

    def test_topic27_act_dates_and_paramountcy(self) -> None:
        markdown = session_markdown("modern-indian-history-27")
        required = [
            "Royal Assent on 18 July 1947",
            "from 15 August 1947",
            "observance of 14 August as its national day",
            "must never be presented as the Act's date of commencement",
            "paramountcy lapsed and did not pass wholesale to India",
            "negotiated state by state",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("the Act came into force on 14 August", markdown)
        self.assertNotIn("paramountcy passed automatically to India", markdown)
        self.assertNotIn("paramountcy was transferred to India", markdown)

    def test_topic27_radcliffe_publication_and_violence_caution(self) -> None:
        markdown = session_markdown("modern-indian-history-27")
        required = [
            "published on 17 August 1947",
            "after the transfer of power",
            "did not know which state they were in",
            "the award alone did not cause all the violence",
            "begun long before the line was drawn",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Radcliffe alone caused", markdown)

    def test_topic27_congress_acceptance_and_inevitability(self) -> None:
        markdown = session_markdown("modern-indian-history-27")
        required = [
            "reluctant and pragmatic rather than programmatic",
            "never be presented as long-standing Congress policy",
            "was not made inevitable by the founding of the Muslim League "
            "in 1906",
            "Lahore Resolution of 1940",
            "cumulative structure plus contingent decisions",
            "No single-villain explanation",
            "hasty withdrawal of 1947",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("Congress consistently supported Partition", markdown)
        self.assertNotIn("Partition became inevitable in 1906", markdown)
        self.assertNotIn(
            "British haste was the sole cause of Partition", markdown
        )

    def test_topic27_numerical_discipline_gandhi_and_registers(self) -> None:
        markdown = session_markdown("modern-indian-history-27")
        required = [
            "around 10 to 15 million",
            "broad estimate",
            "must not be stated with false precision",
            "Gandhi was in Calcutta and Bengal working for communal peace",
            "not celebrating in Delhi",
            "Tryst with Destiny",
            "analytically simultaneous",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)
        self.assertNotIn("death toll was exactly", markdown)
        self.assertNotIn("Gandhi celebrated independence in Delhi", markdown)

    def test_topic27_current_bridge_uses_only_page_supported_claims(
        self,
    ) -> None:
        markdown = session_markdown("modern-indian-history-27")
        required = [
            "Ministry of Culture",
            "Partition Horrors Remembrance Day",
            "13 and 14 August 2026",
            "Delhi, Amritsar and Kolkata",
            "survivor testimonies",
            "silent marches",
            "no casualty figure",
        ]
        for phrase in required:
            self.assertIn(phrase, markdown)

    def test_topic27_pyq_cards_record_unresolved_and_adjacent_routing(
        self,
    ) -> None:
        topic = generator.TOPICS[1]
        cards = {(item[0], item[1]): item for item in topic["pyq_solutions"]}
        self.assertEqual(2, len(cards))
        unresolved = cards[("2021", "Prelims GS-I Q50")]
        self.assertIn("unresolved-locally", unresolved[3])
        self.assertIn("asserts nothing about this demand", unresolved[4])
        shared = cards[("2019", "Mains GS-I Q12")]
        self.assertIn("adjacent-owner-routed-demand", shared[3])
        self.assertIn("Topic 26 owner", shared[2])
        for card in cards.values():
            self.assertIsNone(
                re.search(r"\bAnswer:\s*[A-D]\b", card[4], re.I), card[1]
            )

    # ---------------- Specs, manifests and isolation ----------------

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

    def test_ascii_panels_are_authored_not_templated(self) -> None:
        specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
        bodies = [
            panel.body for spec in specs.values() for panel in spec.panels
        ]
        self.assertEqual(24, len(bodies))
        self.assertEqual(24, len(set(bodies)))
        for body in bodies:
            self.assertNotIn("FOCUS -> ", body)
            self.assertNotIn(
                "EXAM USE -> use", body
            )  # templated 09-13 panel shape
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
            self.assertEqual(
                config["live_sources"], manifest["live_sources"]
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
        self.assertEqual(
            30, len(set(generator.SESSION_VISUALS.values()))
        )
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
        keys = {"modern-indian-history-26", "modern-indian-history-27"}
        self.assertEqual(keys, set(generator.TOPIC_CHRONOLOGY))
        self.assertEqual(keys, set(generator.FORBIDDEN_TOPIC_PHRASES))
        for config in generator.TOPICS:
            markdown = session_markdown(str(config["key"]))
            generator.assert_topic_safeguards(config, markdown)

    def test_ascii_master_registers_the_new_spec(self) -> None:
        self.assertIn(
            "modern-indian-history-26-27-2026-08-31-sequential.json",
            ascii_master.MANUAL_SPEC_FILENAMES,
        )

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

    def test_import_does_not_mutate_topics_24_25(self) -> None:
        self.assertEqual(
            ["modern-indian-history-24", "modern-indian-history-25"],
            [config["key"] for config in previous.TOPICS],
        )
        self.assertEqual(
            {"modern-indian-history-24", "modern-indian-history-25"},
            set(previous.PANEL_DATA),
        )
        self.assertTrue(
            all(len(panels) == 12 for panels in previous.PANEL_DATA.values())
        )
        self.assertEqual(
            "modern-indian-history-24-25-2026-08-31-sequential.json",
            previous.ASCII_PATH.name,
        )
        generator.validate_previous_batch_untouched()

    def test_import_does_not_mutate_shared_base_globals(self) -> None:
        import generate_modern_history_09_13_sequential as base

        prior_date = base.DATE
        prior_ascii_path = base.ASCII_PATH
        prior_topics = base.TOPICS
        prior_panel_data = base.PANEL_DATA
        # Importing generator must never leave configured_base() overrides
        # applied to the shared base module outside of a `with` block.
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
        # The context manager must restore every overridden global exactly.
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
