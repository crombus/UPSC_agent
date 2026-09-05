"""Targeted tests for the Political Theory learner-v2 generator."""

from __future__ import annotations

import re
import unittest

import generate_political_theory_topic_v2 as generator
import markdown_learning_pdf


class PoliticalTheoryGeneratorTests(unittest.TestCase):
    def test_all_configured_topics_preserve_structure_and_sources(self) -> None:
        for topic in generator.TOPICS.values():
            with self.subTest(topic=topic.topic_key):
                main, workbook, metadata = generator.build_documents(topic, 2)
                self.assertEqual([], generator.validate_documents(topic, main, workbook))
                self.assertEqual(10, metadata["session_count"])
                self.assertEqual(48, metadata["mcq_count"])
                self.assertNotRegex(main, r"(?i)\bProgress\s+\d+\s*/\s*\d+")
                self.assertEqual(
                    [
                        "BASIC LEARNING SESSION",
                        "BASIC MCQS / REMEDIATION",
                        "PYQS AND ANSWER PRACTICE",
                        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                        "CONSOLIDATED REGISTER NOTES",
                    ],
                    re.findall(r"(?m)^##\s+(.+?)\s*$", main),
                )
                practices = re.findall(
                    r"(?s)^#### Original Mains Practice \d+ — (\d+) marks.*?"
                    r"\*\*Model solution\*\*\s*(.*?)"
                    r"(?=^#### Original Mains Practice|\Z)",
                    main.split(
                        "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                        1,
                    )[0],
                    re.MULTILINE,
                )
                self.assertEqual(6, len(practices))
                minimums = {10: 120, 15: 175, 20: 230}
                for marks_text, answer in practices:
                    marks = int(marks_text)
                    answer = answer.split("**Why this earns marks:**", 1)[0]
                    word_count = len(re.findall(r"\b[\w'-]+\b", answer))
                    self.assertGreaterEqual(word_count, minimums[marks])
                    self.assertLessEqual(word_count, 330)

    def test_pyq_ownership_boundaries(self) -> None:
        for number in (1, 2):
            main, _, _ = generator.build_documents(generator.TOPICS[number], 2)
            self.assertIn("No directly owned verified UPSC PYQ", main)
            self.assertNotIn("#### Solved PYQ", main)

        topic_three, _, _ = generator.build_documents(generator.TOPICS[3], 2)
        self.assertIn("Cross-application ownership note", topic_three)
        self.assertIn("R. Nozick", topic_three)
        self.assertIn("J.S. Mill", topic_three)

    def test_topic_five_keeps_conservatism_in_core(self) -> None:
        main, _, _ = generator.build_documents(generator.TOPICS[5], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        self.assertIn("22.1 One-screen map", core)
        self.assertIn("22.12 Answer architecture links", core)
        self.assertIn("SESSION 10 — Conservatism III", core)

    def test_standard_flowchart_source_is_exporter_compatible(self) -> None:
        topic = generator.TOPICS[1]
        main, _, _ = generator.build_documents(topic, 3)
        owner = topic.basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(topic, 3)
        spec = generator.make_ascii_spec(
            topic,
            main,
            owner,
            3,
            paths["markdown"],
        )
        manual = spec["topics"][0]
        self.assertEqual(12, len(manual["panels"]))
        self.assertTrue(all(panel["lines"] for panel in manual["panels"]))
        self.assertTrue(
            all(
                len(line) <= 100
                for panel in manual["panels"]
                for line in panel["lines"]
            )
        )
        self.assertEqual(
            "carvaka-continuous-at-a-glance-graphical-v2",
            generator.carvaka_flowchart.RENDERER_NAME,
        )
        self.assertRegex(
            "manual-authored-political-theory-twelve-panel-spec",
            r"^manual-authored-[A-Za-z0-9-]+-spec$",
        )

    def test_feminism_preserves_extensions_and_pyq_ownership(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[6], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "Marxist feminism, reconstructed separately from socialist feminism",
            "Carole Pateman and Susan Moller Okin",
            "Judith Butler and performativity",
            "Intersectionality (Kimberlé Crenshaw)",
            "Two objection–reply chains",
            "#### 15. Cautious Indian application",
            "#### 16. Executable answer architecture",
        ):
            self.assertEqual(1, core.count(marker), marker)
        self.assertIn("UN News, 6 March 2026", main)
        self.assertIn("primary owner is Gender Discrimination", workbook)
        self.assertEqual(3, len(re.findall(r"(?m)^#### PYQ \d+\b", workbook)))

    def test_nature_of_politics_preserves_communitarian_distinctions(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[7], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "Alasdair MacIntyre — tradition and practices",
            "Charles Taylor — dialogical self and recognition",
            "Michael Sandel — critique of the unencumbered self",
            "#### 14. Precursors: Rousseau and T.H. Green",
            "#### 15. Communitarian objections to liberalism and liberal replies",
            "#### 16. Cautious Indian application",
            "#### 17. Executable answer architecture",
        ):
            self.assertEqual(1, core.count(marker), marker)
        self.assertIn("PIB, 27 July 2026", main)
        self.assertIn("No directly owned verified UPSC PYQ", workbook)
        self.assertNotRegex(workbook, r"(?m)^#### (?:Solved )?PYQ \d+\b")
        self.assertNotIn("associated with **Evidence/mechanism**", workbook)
        for marker in (
            "Alasdair MacIntyre — mechanism",
            "Charles Taylor — mechanism",
            "Michael Sandel — mechanism",
        ):
            self.assertIn(marker, workbook)

    def test_approaches_preserves_tenets_and_all_five_models(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[8], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "#### 13. Behaviouralism's eight commonly taught tenets",
            "#### 14. Post-behaviouralism: relevance and action",
            "1. **David Easton — systems analysis**",
            "2. **Gabriel Almond — structural-functional approach**",
            "3. **Karl Deutsch — communication/cybernetic approach**",
            "4. **Decision-making approach**",
            "5. **Marxian approach**",
            "#### 16. Comparing the five models and their limitations",
            "#### 17. Two objection–reply chains",
            "#### 18. Cautious Indian application",
            "#### 19. Executable answer architecture",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[8].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertIn("Election Commission of India/PIB, 8 May 2026", main)
        self.assertIn("No directly owned verified UPSC PYQ", workbook)

    def test_interdisciplinary_topic_preserves_extended_disciplines(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[9], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "#### 13. Extending the discipline list",
            "Political anthropology",
            "Law/jurisprudence as a data source",
            "Political geography",
            "#### 14. Borrowed models and the limits of reductionism",
            "#### 15. Two objection–reply chains",
            "#### 16. Cautious Indian application",
            "#### 17. Executable answer architecture",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[9].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertNotIn(
            "associated with **Reductionism, named precisely**",
            workbook,
        )
        self.assertIn("pairing recorded for **Economic reductionism**", workbook)
        self.assertIn("MoSPI/PIB, 29 June 2026", main)
        self.assertIn("No directly owned verified UPSC PYQ", workbook)
        owner = generator.TOPICS[9].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[9], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[9],
            main,
            owner,
            2,
            paths["markdown"],
        )
        manual = spec["topics"][0]
        joined = "\n".join(
            line
            for panel in manual["panels"]
            for line in panel["lines"]
        )
        self.assertNotIn("cannot be grasped by.", joined)
        self.assertIn(
            "ideal-state speculation or formal institutions alone",
            joined,
        )
        self.assertTrue(
            all(
                len(line) <= 100
                for panel in manual["panels"]
                for line in panel["lines"]
            )
        )

    def test_state_civil_society_topic_preserves_all_extensions(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[10], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "State vs Government vs Society vs Nation",
            "Secularism and multiculturalism: the missing state-diversity bridge",
            "Robert Putnam — social capital",
            "Jean Cohen and Andrew Arato — civil society and political theory",
            "Herbert Marcuse — critique, and a counterpoint",
            "#### 14. Two objection–reply chains",
            "#### 15. Cautious Indian application",
            "#### 16. Executable answer architecture",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[10].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertIn("MEA, 16 June 2026", main)
        self.assertIn(
            "primary owner is Philosophy Paper II — Humanism, Secularism and Multiculturalism",
            workbook,
        )
        self.assertEqual(5, len(re.findall(r"(?m)^#### Solved PYQ \d+\b", workbook)))
        self.assertNotIn("-> The second\n", main)
        self.assertNotIn("-> Its own feminist\n", main)
        owner = generator.TOPICS[10].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[10], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[10],
            main,
            owner,
            2,
            paths["markdown"],
        )
        panels = spec["topics"][0]["panels"]
        panel_four = "\n".join(panels[3]["lines"])
        joined = "\n".join(
            line for panel in panels for line in panel["lines"]
        )
        self.assertIn("Laski", panel_four)
        compact = re.sub(r"\s+", " ", joined)
        for complete_fact in (
            "state what is necessary but insufficient",
            "A religiously HOMOGENEOUS society can still need secular protection",
        ):
            self.assertIn(complete_fact, compact)

    def test_sovereignty_topic_preserves_answer_engine_and_caution(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[11], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "#### A. Thesis statements",
            "#### B. Directive decoder",
            "#### C. Argument reconstruction",
            "#### D. Five+ named evidence units",
            "#### E. Claim → evidence → significance → limit",
            "#### F. Mark-scaled architecture",
            "#### G. Cautious Indian application",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[11].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertIn("PIB, 30 June 2026", main)
        self.assertIn(
            "primary owner is Philosophy Paper II — Sovereignty",
            workbook,
        )
        self.assertEqual(4, len(re.findall(r"(?m)^#### Solved PYQ \d+\b", workbook)))
        self.assertEqual(
            ["1", "2", "3", "4"],
            re.findall(r"(?m)^#### Solved PYQ (\d+)\b", workbook),
        )
        self.assertIn("not traceable", workbook)
        self.assertIn("more reliably associated with Lord Palmerston", workbook)
        self.assertNotIn(
            "states the\nstructural logic of Kautilya's *mandala*",
            workbook,
        )

    def test_globalisation_topic_preserves_complete_answer_engine(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[12], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "#### A. Thesis statements",
            "#### B. Directive decoder",
            "#### C. Argument reconstruction",
            "#### D. Five+ named evidence units",
            "#### E. Claim → evidence → significance → limit",
            "#### F. Mark-scaled architecture",
            "#### G. Cautious Indian application",
            "#### H. Quotation/proposition micro-method",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[12].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertIn("PIB, 15 July 2026", main)
        self.assertIn("No directly owned verified UPSC PYQ", workbook)
        self.assertNotRegex(workbook, r"(?m)^#### (?:Solved )?PYQ \d+\b")
        self.assertIn("Loan conditionality is different", core)
        self.assertIn(
            "consented but often unequal external constraint, not as delegation",
            core,
        )
        self.assertNotIn(
            "an example of **delegated** sovereignty",
            core,
        )
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated "
            "with this source-grounded statement",
            workbook,
        )
        self.assertIn("### COMPLETE TOPIC CHECKLIST", main)
        self.assertIn("### THREE GLOBALISATION POSITIONS", main)
        self.assertIn("### EMBEDDED TWELVE-PANEL ASCII REVISION ATLAS", main)
        question_nine = re.search(
            r"(?s)^#### MCQ 9\s+(.*?)(?=^---$)",
            workbook,
            re.MULTILINE,
        ).group(1)
        self.assertNotIn(
            "process vs globalization as policy",
            question_nine.casefold(),
        )
        nkrumah_mcqs = re.search(
            r"(?s)^#### MCQ 39\s+(.*?)(?=^#### MCQ 41\b)",
            workbook,
            re.MULTILINE,
        ).group(1)
        self.assertIn("popularised and systematised", nkrumah_mcqs)
        self.assertNotIn('"coined" neo-colonialism', nkrumah_mcqs)
        for marker in (
            "Nkrumah's 1965",
            "OPEC (1960)",
            "NATO (1949) and the Warsaw Pact (1955)",
            "Non-alignment under Nehru, Nasser and Tito",
        ):
            self.assertIn(marker, core)
        owner = generator.TOPICS[12].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[12], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[12],
            main,
            owner,
            2,
            paths["markdown"],
        )
        joined = "\n".join(
            line
            for panel in spec["topics"][0]["panels"]
            for line in panel["lines"]
        )
        for marker in (
            "Said distinguishes imperialism from colonialism",
            "Reject the claim that globalisation has made sovereignty disappear",
            "OPEC 1960 shows coalition-based resistance",
            "India's 1991 crisis",
            "No directly owned verified UPSC PYQ",
        ):
            self.assertIn(marker, joined)
        self.assertNotIn("📰", joined)
        self.assertNotIn("SYNTHESIS ->", joined)
        self.assertIn("VERDICT ->", joined)

    def test_state_perspectives_preserves_all_thinker_blocks(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[13], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "**Aristotle:**",
            "**Burke and Hegel:**",
            "**Hobbes, Locke, Rousseau:**",
            "**Adam Smith, Bentham, James Mill, Spencer, Nozick:**",
            "**J.S. Mill, T.H. Green, Hobhouse, Laski, Maclver:**",
            "**Marx, Engels, Lenin, Gramsci, Miliband, Poulantzas:**",
            "**Miliband vs Poulantzas — the instrumentalist/structuralist debate, reconstructed:**",
            "**MacIntyre, Sandel, Walzer, Taylor:**",
            "**Gandhi:**",
            "**Kate Millett and Zillah Eisenstein — distinguished, not merged:**",
            "**Duguit, Laski, Maclver, Dahl and Lindblom:**",
            "#### A. Thesis statements",
            "#### B. Directive decoder",
            "#### C. Argument reconstruction",
            "#### D. Five+ named evidence units",
            "#### E. Claim → evidence → significance → limit",
            "#### F. Mark-scaled architecture",
            "#### G. Cautious Indian application",
            "#### H. Quotation/proposition micro-method",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[13].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertIn("PIB, 1-2 July 2026", main)
        self.assertIn("PRID=2280427", main)
        self.assertIn("No directly owned verified UPSC PYQ", workbook)
        self.assertNotRegex(workbook, r"(?m)^#### (?:Solved )?PYQ \d+\b")
        self.assertNotRegex(workbook, r"(?m)^[A-D]\.\s+,")
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated "
            "with this source-grounded statement",
            workbook,
        )
        self.assertIn("### EMBEDDED TWELVE-PANEL ASCII REVISION ATLAS", main)
        self.assertIn("### COMPLETE TEN-PERSPECTIVE GRID", main)
        self.assertIn("### SIX-TEST ANSWER GRID", main)
        self.assertTrue(markdown_learning_pdf.STYLES["h4"].keepWithNext)
        self.assertTrue(markdown_learning_pdf.STYLES["mcq_stem"].keepWithNext)
        six_test_answer = re.search(
            r"(?s)\*\*Question:\*\* Evaluate diverse perspectives on the state "
            r"through origin, purpose, liberty, inequality, civil society and route "
            r"to change\..*?\*\*Model solution\*\*(.*?)"
            r"(?=^#### Original Mains Practice|\Z)",
            main,
            re.MULTILINE,
        ).group(1)
        self.assertIn("On inequality", six_test_answer)
        self.assertIn("On civil society", six_test_answer)
        self.assertIn("Their purposes diverge", six_test_answer)
        practices = re.findall(
            r"(?s)^#### Original Mains Practice ([34]) — 15 marks.*?"
            r"\*\*Model solution\*\*\s*(.*?)"
            r"(?=^#### Original Mains Practice|\Z)",
            main.split(
                "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                1,
            )[0],
            re.MULTILINE,
        )
        self.assertEqual(2, len(practices))
        for _, answer in practices:
            answer = answer.split("**Why this earns marks:**", 1)[0]
            word_count = len(re.findall(r"\b[\w'-]+\b", answer))
            self.assertGreaterEqual(word_count, 175)
            self.assertLessEqual(word_count, 220)
        owner = generator.TOPICS[13].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[13], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[13],
            main,
            owner,
            2,
            paths["markdown"],
        )
        joined = "\n".join(
            line
            for panel in spec["topics"][0]["panels"]
            for line in panel["lines"]
        )
        for marker in (
            "Aristotle, Burke and Hegel",
            "Miliband argues instrumental capture",
            "Millett and Eisenstein",
            "six-test grid",
            "e-Governance conference",
            "No directly owned verified UPSC PYQ",
        ):
            self.assertIn(marker, joined)
        self.assertNotIn("SYNTHESIS ->", joined)
        self.assertIn("VERDICT ->", joined)
        forbidden_by_mcq = {
            11: "criticize the atomistic liberal self",
            29: "the state is like an organism",
            31: "artificial device created by agreement",
            33: "the state is a necessary evil",
            35: "create conditions for moral freedom",
            37: "the state arises with private property",
            43: "morally inferior to self-rule",
            45: "the state regulates power in both public and intimate life",
            47: "the state is not the sole centre of power",
        }
        for number, forbidden in forbidden_by_mcq.items():
            block = re.search(
                rf"(?s)^#### MCQ {number}\s+(.*?)(?=^---$)",
                workbook,
                re.MULTILINE,
            ).group(1)
            self.assertNotIn(forbidden, block, f"MCQ {number}")
        mcq_twenty_nine = re.search(
            r"(?s)^#### MCQ 29\s+(.*?)(?=^---$)",
            workbook,
            re.MULTILINE,
        ).group(1)
        self.assertNotIn(
            "organic/idealist thought treats the state as ethically exalted",
            mcq_twenty_nine,
        )
        debate_block = re.search(
            r"(?s)^#### MCQ 39\s+(.*?)(?=^---$)",
            workbook,
            re.MULTILINE,
        ).group(1)
        self.assertIn("Poulantzas", debate_block)

    def test_obligation_law_topic_preserves_debates_and_pyq_boundary(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[14], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "Austin, Kelsen and Hart within legal positivism; Dworkin as a major interpretivist critic",
            "#### A. Thesis statements",
            "#### B. Directive decoder",
            "#### C. Argument reconstruction",
            "#### D. Five+ named evidence units",
            "#### E. Claim → evidence → significance → limit",
            "#### F. Mark-scaled architecture",
            "#### G. Cautious Indian application",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[14].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertIn("Department of Justice/PIB, 29 March 2026", main)
        self.assertIn(
            "primary owner is Philosophy Paper II — Crime and Punishment",
            workbook,
        )
        self.assertEqual(4, len(re.findall(r"(?m)^#### Solved PYQ \d+\b", workbook)))
        for question in (
            "What are the moral justifications of capital punishment?",
            "while punishing a juvenile",
            "capital punishment as an effective deterrent",
            "right to life be absolute",
        ):
            self.assertIn(question, workbook)
        self.assertNotIn("Legal positivism from Austin to Dworkin", core)
        self.assertIn("not as four versions of one doctrine", core)
        self.assertIn("not merely a later positivist refinement", core)
        self.assertIn(
            "forward-looking treatment aimed at rehabilitation and return to "
            "law-abiding life",
            workbook,
        )
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated "
            "with this source-grounded statement",
            workbook,
        )
        self.assertIn("### CIVIL-DISOBEDIENCE TEST", main)
        self.assertIn("### PUNISHMENT AND RULE-OF-LAW GRID", main)
        self.assertIn("### EMBEDDED TWELVE-PANEL ASCII REVISION ATLAS", main)
        owner = generator.TOPICS[14].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[14], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[14],
            main,
            owner,
            2,
            paths["markdown"],
        )
        joined = "\n".join(
            line
            for panel in spec["topics"][0]["panels"]
            for line in panel["lines"]
        )
        for marker in (
            "Dworkin is an interpretivist critic",
            "Tele-Law consultation",
            "Primary ownership remains Philosophy Paper II - Crime and Punishment",
        ):
            self.assertIn(marker, joined)
        self.assertNotIn("SYNTHESIS ->", joined)

    def test_power_topic_preserves_digital_extension_and_cautions(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[15], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "#### A. Thesis statements",
            "#### B. Directive decoder",
            "#### C. Argument reconstruction",
            "#### D. Five+ named evidence units",
            "#### E. Claim → evidence → significance → limit",
            "#### F. Mark-scaled architecture",
            "#### G. Cautious Indian application",
            "#### 14.1 Why this belongs in the power file, not the technology file",
            "#### 14.10 Answer architecture",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[15].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertIn("PIB, 19 February 2026", main)
        self.assertIn("M.A.N.A.V.", main)
        self.assertIn("PRID=2230282", main)
        self.assertNotIn("PRID=2230090", main)
        self.assertIn("No directly owned verified UPSC PYQ", workbook)
        self.assertNotRegex(workbook, r"(?m)^#### (?:Solved )?PYQ \d+\b")
        self.assertNotRegex(workbook, r"(?m)^[A-D]\.\s+,")
        self.assertNotRegex(
            workbook,
            r"(?m)^[A-D]\.\s+Feminist theory of power — reconstructed accurately$",
        )
        self.assertRegex(workbook, r"(?m)^[A-D]\.\s+Feminist theory of power$")
        self.assertRegex(workbook, r"(?m)^A\.\s+.+\n\nB\.\s+.+\n\nC\.\s+.+\n\nD\.\s+.+$")
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated "
            "with this source-grounded statement",
            workbook,
        )
        self.assertNotIn("rules out Pareto's and Mosca's", core)
        self.assertNotIn("predicts permanent elite entrenchment", core)
        self.assertIn("leaders may turn over while organisation remains oligarchic", core)
        self.assertIn("presented as a hypothesis, not a finding", core)
        self.assertNotIn(
            'sovereignty\'s "formally consensual but substantively unequal" delegation',
            core,
        )
        self.assertIn(
            "without relabelling conditionality as delegation",
            core,
        )
        self.assertIn("### THREE-DIMENSIONAL POWER LADDER", main)
        self.assertIn("### DIGITAL-POWER TEST", main)
        practices = re.findall(
            r"(?s)^#### Original Mains Practice \d+ — \d+ marks.*?"
            r"\*\*Model solution\*\*(.*?)"
            r"(?=^#### Original Mains Practice|\Z)",
            workbook,
            re.MULTILINE,
        )
        self.assertEqual(6, len(practices))
        self.assertTrue(all(len(answer.split()) >= 120 for answer in practices))
        owner = generator.TOPICS[15].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[15], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[15],
            main,
            owner,
            2,
            paths["markdown"],
        )
        joined = "\n".join(
            line
            for panel in spec["topics"][0]["panels"]
            for line in panel["lines"]
        )
        for marker in (
            "Elite turnover can coexist with oligarchy",
            "M.A.N.A.V. vision",
            "No directly owned verified UPSC PYQ",
        ):
            self.assertIn(marker, joined)
        self.assertNotIn("SYNTHESIS ->", joined)

    def test_citizenship_topic_preserves_critiques_and_membership_boundaries(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[16], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "## 12. Named evidence units: significance and limits (extended thinkers)",
            "## 13. Feminist, postcolonial and migration critiques (three distinct strands)",
            "## 14. Citizenship, legal nationality and national identity",
            "## 15. Objection and reply chains",
            "## 19. Executable answer architecture (10/15/20-mark blueprints)",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[16].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated "
            "with this source-grounded statement",
            workbook,
        )
        self.assertIn("Election Commission of India", main)
        self.assertIn("ECI/PN/108/2026", main)
        self.assertIn("document?id=17504", main)
        self.assertIn(
            "primary owner is Philosophy Paper II - Individual and State",
            workbook,
        )
        self.assertEqual(1, len(re.findall(r"(?m)^#### Solved PYQ \d+\b", workbook)))
        for marker in (
            "Do rights make citizens accountable to the State?",
            "under the 1954 Convention",
            "long-term foreign residents",
            "His surveillance analysis is developed separately",
            "not a universal chronology",
        ):
            self.assertIn(marker, main)
        self.assertIn("### MIGRATION AND MEMBERSHIP", main)
        self.assertIn("### CRITIQUE GRID", main)
        owner = generator.TOPICS[16].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[16], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[16],
            main,
            owner,
            2,
            paths["markdown"],
        )
        joined = re.sub(
            r"\s+",
            " ",
            "\n".join(
                line
                for panel in spec["topics"][0]["panels"]
                for line in panel["lines"]
            ),
        )
        for marker in (
            "Statelessness means no state considers the person its national",
            "ECI literacy anchor illustrates civic capability",
            "Primary ownership remains Philosophy Paper II - Individual and State",
        ):
            self.assertIn(marker, joined)

    def test_rights_topic_preserves_obligation_enforcement_and_pyq_boundaries(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[17], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "## 12. Named evidence units: natural, legal, historical and ideal rights compared",
            "## 13. Civil liberties vs democratic rights (deepened, with objection-reply)",
            "## 14. Universality vs cultural relativism",
            "## 15. Generations of rights: non-linear caution",
            "## 16. Status, enforcement and application",
            "## 19. Executable answer architecture (10/15/20-mark blueprints)",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[17].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated "
            "with this source-grounded statement",
            workbook,
        )
        self.assertIn("NHRC, 19 June 2026", main)
        self.assertIn("allegation", main)
        self.assertIn("not cited as an adjudicated finding", main)
        self.assertIn(
            "nhrc,-india-takes-suo-motu-cognizance-of-the-reported-illegal-"
            "confinement-of-a-minor-boy",
            main,
        )
        self.assertIn(
            "primary owner is Philosophy Paper II - Individual and State",
            workbook,
        )
        self.assertEqual(7, len(re.findall(r"(?m)^#### Solved PYQ \d+\b", workbook)))
        for marker in (
            "Hohfeld's vocabulary distinguishes claim-rights",
            "minimal anti-redistributive state",
            "non-derogable rights",
            "Horizontal effect",
            "progressive realisation",
            "immediate non-discrimination",
        ):
            self.assertIn(marker, main)
        self.assertIn("### INTERNATIONAL AND CONSTITUTIONAL BOUNDARIES", main)
        self.assertIn("### GENERATIONS AND INDIVISIBILITY", main)
        owner = generator.TOPICS[17].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[17], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[17],
            main,
            owner,
            2,
            paths["markdown"],
        )
        joined = re.sub(
            r"\s+",
            " ",
            "\n".join(
                line
                for panel in spec["topics"][0]["panels"]
                for line in panel["lines"]
            ),
        )
        for marker in (
            "Hohfeld separates claim, liberty, power and immunity",
            "NHRC detention case is an allegation",
            "Seven rights PYQs are cross-applied",
        ):
            self.assertIn(marker, joined)

    def test_justice_topic_preserves_categories_priorities_and_pyq_ownership(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[19], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "## 12. Aristotle: distributive and corrective justice (named evidence unit)",
            "## 13. Procedural-justice positions: Hayek, Friedman and Nozick",
            "## 14. Distributive criteria: merit, need and desert",
            "## 15. Rawls: procedural-substantive bridge",
            "## 16. Feminist, capability and recognition links",
            "## 21. Executable answer architecture",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[19].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated "
            "with this source-grounded statement",
            workbook,
        )
        self.assertNotIn(
            "Which option is the exact canonical pairing recorded for",
            workbook,
        )
        self.assertIn(
            "A scholarship board must allocate limited places",
            workbook,
        )
        self.assertNotIn("closure of classes remains a real cost", workbook)
        self.assertIn(
            "limited movement by aptitude is conceptually possible",
            workbook,
        )
        self.assertIn("National Overseas Scholarship", main)
        self.assertIn("applicable from 2026-27", main)
        self.assertIn("https://socialjustice.gov.in/schemes/28", main)
        self.assertEqual(
            13,
            len(re.findall(r"(?m)^#### (?:Solved )?PYQ \d+\b", workbook)),
        )
        for owner in (
            "Social and Political Ideals",
            "Crime and Punishment",
            "Development and Social Progress",
            "Gender Discrimination",
            "Caste Discrimination: Gandhi and Ambedkar",
        ):
            self.assertIn(
                f"Primary owner:** Philosophy Paper II - {owner}",
                workbook,
            )
        for marker in (
            "chapter frame, not an exhaustive definition",
            "Mill develops a utilitarian account of justice",
            "hierarchical functional differentiation",
            "not be presented as one of Aristotle's own coordinate criteria",
            "historical, entitlement-based and unpatterned",
            "derive **two principles**",
            "comparative, realization-focused method",
            "parity of participation",
            "better framed through substantive equality",
        ):
            self.assertIn(marker, main)
        practices = re.findall(
            r"(?s)^#### Original Mains Practice \d+ — \d+ marks.*?"
            r"\*\*Model solution\*\*(.*?)"
            r"(?=^#### Original Mains Practice|\Z)",
            workbook,
            re.MULTILINE,
        )
        self.assertEqual(6, len(practices))
        self.assertTrue(all(len(answer.split()) >= 120 for answer in practices))
        owner = generator.TOPICS[19].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[19], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[19],
            main,
            owner,
            2,
            paths["markdown"],
        )
        joined = re.sub(
            r"\s+",
            " ",
            "\n".join(
                line
                for panel in spec["topics"][0]["panels"]
                for line in panel["lines"]
            ),
        )
        for marker in (
            "Rawls states two lexically ordered principles",
            "Fraser joins redistribution and recognition",
            "Thirteen cross-applied PYQs retain five distinct Philosophy owners",
        ):
            self.assertIn(marker, joined)

    def test_liberty_equality_property_preserves_republican_and_property_boundaries(self) -> None:
        main, workbook, _ = generator.build_documents(generator.TOPICS[18], 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "## 12. Berlin, MacCallum and Taylor",
            "## 13. Property as power and \"functionless property\"",
            "## 14. Nozick's entitlement theory",
            "## 15. Liberty, equality and property: synthesis",
            "## 22. Republican liberty as non-domination",
            "### 22.1 Why a third family at all",
            "### 22.8 Evidence units and answer architecture",
        ):
            self.assertEqual(1, core.count(marker), marker)
        for label in generator.TOPICS[18].mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated "
            "with this source-grounded statement",
            workbook,
        )
        self.assertIn("NAKSHA", main)
        self.assertIn("2 July 2026", main)
        self.assertIn("16 July to 14 August 2026", main)
        self.assertIn("https://dolr.gov.in/en/about-naksha/", main)
        self.assertEqual(
            22,
            len(re.findall(r"(?m)^#### (?:Solved )?PYQ \d+\b", workbook)),
        )
        for owner in (
            "Social and Political Ideals",
            "Sovereignty",
            "Individual and State",
            "Forms of Government",
            "Political Ideologies",
            "Gender Discrimination",
        ):
            self.assertIn(
                f"Primary owner:** Philosophy Paper II - {owner}",
                workbook,
            )
        for marker in (
            "offence, dislike and the person's own good are insufficient",
            "Equality of opportunity vs equality of outcome",
            "hypothetical auction and insurance",
            "leaving \"enough and as good\"",
            "external embodiment through which free will",
            "seriously under-specified",
            "Proposed synthesis, not a shared canonical doctrine",
            "reverse discrimination is an objection",
            "should not call the slave free simpliciter",
            "Philosophy Optional practice may use different paper-specific",
        ):
            self.assertIn(marker, main)
        practices = re.findall(
            r"(?s)^#### Original Mains Practice \d+ — \d+ marks.*?"
            r"\*\*Model solution\*\*(.*?)"
            r"(?=^#### Original Mains Practice|\Z)",
            workbook,
            re.MULTILINE,
        )
        self.assertEqual(6, len(practices))
        self.assertTrue(all(len(answer.split()) >= 120 for answer in practices))
        owner = generator.TOPICS[18].basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(generator.TOPICS[18], 2)
        spec = generator.make_ascii_spec(
            generator.TOPICS[18],
            main,
            owner,
            2,
            paths["markdown"],
        )
        joined = re.sub(
            r"\s+",
            " ",
            "\n".join(
                line
                for panel in spec["topics"][0]["panels"]
                for line in panel["lines"]
            ),
        )
        for marker in (
            "Rawls orders liberty, fair opportunity and the difference principle",
            "The benevolent master leaves some options unobstructed",
            "Twenty-two PYQs remain cross-applied under six Philosophy owners",
        ):
            self.assertIn(marker, joined)

    def test_diverse_justice_preserves_boundaries_and_contextual_practice(self) -> None:
        topic = generator.TOPICS[20]
        main, workbook, _ = generator.build_documents(topic, 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "## 18. Canonical MCQ concept ledger",
            "recognition-language here is an analytical bridge",
            "Postcolonial and global justice are routed out",
            "Rectification principle",
        ):
            self.assertIn(marker, core)
        self.assertIn("Antyodaya in Action", main)
        self.assertEqual(
            6,
            len(re.findall(r"(?m)^#### (?:Solved )?PYQ \d+\b", workbook)),
        )
        self.assertNotIn(
            "Which option is the exact canonical pairing recorded for",
            workbook,
        )
        self.assertNotIn("Which canonical pairing", workbook)
        first_mcq = workbook.split("#### MCQ 2", 1)[0]
        self.assertIn("hypothetical starting point", first_mcq)
        self.assertIn("parties lack knowledge", first_mcq)
        self.assertNotIn("> non-transferable", workbook)
        for label in topic.mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)

    def test_common_good_preserves_plurality_and_owner_routes(self) -> None:
        topic = generator.TOPICS[21]
        main, workbook, _ = generator.build_documents(topic, 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "## 18. Canonical MCQ ledger, supplementary bridges and PYQ routing",
            "Group-rights objection",
            "Constitutional-morality objection",
            "MacIntyrean practices",
        ):
            self.assertIn(marker, core)
        self.assertIn("National Cooperation Policy 2025", main)
        self.assertEqual(
            6,
            len(re.findall(r"(?m)^#### (?:Solved )?PYQ \d+\b", workbook)),
        )
        for owner in (
            "Forms of Government",
            "Humanism, Secularism and Multiculturalism",
            "Development and Social Progress",
            "Caste Discrimination: Gandhi and Ambedkar",
        ):
            self.assertIn(
                f"Primary owner:** Philosophy Paper II - {owner}",
                workbook,
            )
        self.assertNotIn(
            "Which concept, thinker or distinction is correctly associated",
            workbook,
        )
        self.assertNotIn("Which canonical pairing", workbook)
        self.assertNotIn("Which statement gives", workbook)
        practices = re.findall(
            r"(?s)^#### Original Mains Practice \d+ — (\d+) marks.*?"
            r"\*\*Model solution\*\*\s*(.*?)"
            r"(?=^#### Original Mains Practice|\Z)",
            main.split(
                "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                1,
            )[0],
            re.MULTILINE,
        )
        expected_ranges = ((120, 170), (120, 170), (175, 250), (175, 250), (230, 330), (230, 330))
        for (_, answer), (minimum, maximum) in zip(practices, expected_ranges):
            answer = answer.split("**Why this earns marks:**", 1)[0]
            word_count = len(re.findall(r"\b[\w'-]+\b", answer))
            self.assertGreaterEqual(word_count, minimum)
            self.assertLessEqual(word_count, maximum)
        first_mcq = workbook.split("#### MCQ 2", 1)[0]
        self.assertIn("empirically discoverable convergence", first_mcq)
        self.assertIn("continuing accommodation of disagreement", first_mcq)

    def test_democracy_representation_preserves_system_distinctions(self) -> None:
        topic = generator.TOPICS[22]
        main, workbook, _ = generator.build_documents(topic, 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        for marker in (
            "First-Past-The-Post (FPTP) / plurality",
            "Majoritarian systems",
            "Indian liberal-democratic capsule",
            "Forward boundary",
        ):
            self.assertIn(marker, core)
        self.assertIn("National Voters' Day", main)
        self.assertEqual(
            8,
            len(re.findall(r"(?m)^#### (?:Solved )?PYQ \d+\b", workbook)),
        )
        self.assertNotIn(
            "Which option is the exact canonical pairing recorded for",
            workbook,
        )
        self.assertNotIn("Which canonical pairing", workbook)
        first_mcq = workbook.split("#### MCQ 2", 1)[0]
        self.assertIn("representative system combining popular authorization", first_mcq)
        self.assertIn("one person, one vote", first_mcq)
        self.assertNotIn("Concurrent majority — John C.\n", workbook)
        self.assertIn(
            "Calhoun requires the concurrence of each major social section",
            workbook,
        )
        self.assertIn(
            "Lijphart combines grand coalition, mutual veto, proportionality",
            workbook,
        )
        for label in topic.mcq_priority_labels:
            self.assertIn(f"**{label}**", workbook)

    def test_contemporary_democracy_places_extensions_after_practice(self) -> None:
        topic = generator.TOPICS[23]
        main, workbook, _ = generator.build_documents(topic, 2)
        core = main.split("## BASIC MCQS / REMEDIATION", 1)[0]
        advanced = main.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1]
        for marker in (
            "## 21. Populism: an answer-ready module",
            "## 22. Ecological political theory",
            "## 23. Digital democracy",
            "## 24. Democratisation, democratic backsliding and social movements",
        ):
            self.assertNotIn(marker, core)
            self.assertIn(marker, advanced)
        self.assertIn("India AI Impact Summit 2026", main)
        self.assertEqual(
            12,
            len(re.findall(r"(?m)^#### (?:Solved )?PYQ \d+\b", workbook)),
        )
        for label in (
            "Populism",
            "Ecological political theory",
            "Democratisation",
            "Democratic backsliding",
            "Social movements",
        ):
            self.assertIn(f"**{label}**", workbook)
        self.assertNotIn("Which canonical pairing", workbook)
        self.assertNotIn("is reconstructed in full in §21", workbook)
        self.assertNotIn("is reconstructed in §22", workbook)
        self.assertNotIn("Environmental facts, policy and data belong", workbook)
        self.assertIn("Populism is a thin-centred ideology", workbook)
        self.assertIn(
            "Ecological political theory challenges productivism",
            workbook,
        )
        first_mcq = workbook.split("#### MCQ 2", 1)[0]
        self.assertIn("bargaining among relatively autonomous groups", first_mcq)
        self.assertIn("active citizen involvement", first_mcq)
        owner = topic.basic_path.read_text(encoding="utf-8")
        paths = generator.paths_for(topic, 2)
        spec = generator.make_ascii_spec(topic, main, owner, 2, paths["markdown"])
        panels = spec["topics"][0]["panels"]
        self.assertEqual(12, len(panels))
        self.assertTrue(
            all(len(line) <= 100 for panel in panels for line in panel["lines"])
        )
        self.assertTrue(
            any(
                "Schumpeter treats democracy as competition among leadership teams."
                in line
                for line in panels[2]["lines"]
            )
        )
        self.assertTrue(
            any(
                "Revolution is abrupt structural rupture; evolution is cumulative gradual change."
                in line
                for line in panels[3]["lines"]
            )
        )
        self.assertTrue(
            any(
                "Dependency treats underdevelopment as historically produced, not merely delayed."
                in line
                for line in panels[8]["lines"]
            )
        )

    def test_every_solved_item_has_exam_execution_controls(self) -> None:
        for topic in generator.TOPICS.values():
            with self.subTest(topic=topic.topic_key):
                main, workbook, _ = generator.build_documents(topic, 2)
                self.assertIn("### DEEP-REVIEW LEARNING CONTRACT", main)
                items = generator.practice_question_blocks(
                    main.split("## PYQS AND ANSWER PRACTICE", 1)[1].split(
                        "## OPTIONAL ADVANCED DEPTH", 1
                    )[0]
                )
                self.assertGreaterEqual(len(items), 6)
                self.assertEqual(
                    len(items),
                    workbook.count("**Demand decoding:**"),
                )
                self.assertEqual(
                    len(items),
                    workbook.count("**Executable exam-length plan:**"),
                )
                self.assertEqual(
                    len(items),
                    len(re.findall(r"Why this earns marks", workbook, re.I)),
                )
                self.assertEqual(
                    len(items),
                    workbook.count("**How to improve this answer:**"),
                )
                for title, block in items:
                    self.assertRegex(
                        block,
                        r"(?i)\*\*Model (?:solution|answer)\*\*",
                        title,
                    )

    def test_cross_applied_ambedkar_model_is_marks_worthy(self) -> None:
        for number in (19, 21):
            with self.subTest(topic=number):
                _, workbook, _ = generator.build_documents(
                    generator.TOPICS[number],
                    2,
                )
                block = next(
                    block
                    for title, block in generator.practice_question_blocks(workbook)
                    if "annihilation of caste" in block.casefold()
                )
                model = block.split("**Model solution**", 1)[1].split(
                    "**Why this earns marks:**", 1
                )[0]
                self.assertGreaterEqual(len(re.findall(r"\b[\w'-]+\b", model)), 175)
                for marker in (
                    "Annihilation of Caste",
                    "graded inequality",
                    "endogamy",
                    "social democracy",
                    "liberty, equality and fraternity",
                ):
                    self.assertIn(marker, model)

    def test_fresh_ascii_specs_have_no_dangling_sentence_fragments(self) -> None:
        dangling = re.compile(
            r"\b(?:and|or|of|to|from|with|through|into|for|the|a|an|its|"
            r"their|than|as|by|in|on)\.$",
            re.I,
        )
        for topic in generator.TOPICS.values():
            with self.subTest(topic=topic.topic_key):
                main, _, _ = generator.build_documents(topic, 2)
                spec = generator.make_ascii_spec(
                    topic,
                    main,
                    topic.basic_path.read_text(encoding="utf-8"),
                    2,
                    generator.paths_for(topic, 2)["markdown"],
                )
                lines = [
                    line.strip()
                    for panel in spec["topics"][0]["panels"]
                    for line in panel["lines"]
                ]
                self.assertFalse([line for line in lines if dangling.search(line)])


if __name__ == "__main__":
    unittest.main()
