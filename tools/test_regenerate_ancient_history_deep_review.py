"""Targeted tests for the Ancient History deep-review driver."""

from __future__ import annotations

import unittest

import regenerate_ancient_history_deep_review as deep


class AncientHistoryDeepReviewTests(unittest.TestCase):
    def test_rotates_bullet_mcqs_to_abcd(self) -> None:
        source = """# Topic

## BASIC MCQS / REMEDIATION

#### MCQ 1
- A. wrong one
- B. correct one
- C. wrong two
- D. wrong three
**Answer: B.** explanation

#### MCQ 2
- A. wrong one
- B. wrong two
- C. correct two
- D. wrong three
**Answer: C.** explanation

## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.enforce_strict_rotation(source)
        self.assertEqual(metrics["keys"], ["A", "B"])
        self.assertIn("- A. correct one", repaired)
        self.assertIn("- B. correct two", repaired)

    def test_rotates_table_mcq_and_embedded_summary(self) -> None:
        source = """# Topic

## BASIC MCQS / REMEDIATION

### Hard MCQ 01 - evidence
| Option | Choice |
| --- | --- |
| A | wrong |
| B | right |
| C | wronger |
| D | wrongest |
- OPTIONS: A. wrong | B. right | C. wronger | D. wrongest
- CORRECT ANSWER: B - right

## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.enforce_strict_rotation(source)
        self.assertEqual(metrics["keys"], ["A"])
        self.assertIn("| A | right |", repaired)
        self.assertIn("- CORRECT ANSWER: A - right", repaired)

    def test_answer_contracts_are_added(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### Original Mains 01 - 10 marks
**Question:** Discuss the evidence.
**Model answer:** Named evidence supports a qualified conclusion.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(metrics["question_count"], 1)
        self.assertIn("**Demand decoding:**", repaired)
        self.assertIn("**Detailed examiner-grade model status:**", repaired)
        self.assertIn(
            "**Executable exam-length answer / compression plan:**",
            repaired,
        )
        self.assertIn("**Why this earns marks:**", repaired)
        self.assertIn("**How to improve this answer:**", repaired)

    def test_answer_contract_repair_is_idempotent(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### Original Mains 01 - 10 marks
**Question:** Discuss the evidence.
**Model answer:** Named evidence supports a qualified conclusion.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        once, _ = deep.repair_answer_contracts(source)
        twice, _ = deep.repair_answer_contracts(once)
        self.assertEqual(once, twice)

    def test_ascii_replacement_preserves_final_h2(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES

### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM

#### ASCII MASTER FLOW — PANEL 1/1: old
```ascii-master
OLD
```
"""
        repaired = deep.replace_ascii_fragment(
            source,
            """#### ASCII MASTER FLOW — PANEL 1/1: new

```ascii-master
NEW
```""",
        )
        self.assertIn("NEW", repaired)
        self.assertNotIn("OLD", repaired)
        self.assertEqual(
            deep.h2_order_errors(repaired),
            [],
        )

    def test_h2_order_detects_nonfinal_register_notes(self) -> None:
        source = "\n".join(f"## {heading}" for heading in deep.H2_ORDER)
        self.assertEqual(deep.h2_order_errors(source), [])
        self.assertTrue(
            deep.h2_order_errors(source + "\n## EXTRA SECTION")
        )

    def test_answer_controls_distinguish_prelims(self) -> None:
        controls = deep._answer_controls(
            "Which of the following sites is correctly matched?",
            "Verified Prelims PYQ",
        )
        self.assertIn("statement independently", controls["demand"])
        self.assertIn("distractor", controls["improve"])

    def test_supplemental_body_respects_width(self) -> None:
        body = deep.wrapped_body(
            "Evidence ladder",
            [
                "A very long evidence sentence that must be wrapped without losing "
                "its source-limitation logic or creating an unreadable ASCII panel."
            ],
            "Use qualified claims.",
        )
        self.assertLessEqual(max(map(len, body.splitlines())), 102)

    def test_topic_01_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-01"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_02_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-02"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_03_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-03"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_04_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-04"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_05_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-05"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_06_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-06"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_07_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-07"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_08_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-08"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_09_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-09"]
        self.assertEqual(
            {
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
                "Integrated answer spine and qualified conclusion",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_10_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-10"]
        self.assertEqual(
            {
                "Jainism-Buddhism comparison and answer spine",
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_10_pyq_number_matches_authoritative_route(self) -> None:
        topic = deep.Topic(
            number=10,
            topic_key="ancient-indian-history-10",
            title="Jainism and Buddhism",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        repaired = deep.normalize_topic_pyq_metadata(
            topic,
            "#### Prelims PYQ - 2026 GS-I Q5\nMemory hook: 2026 Q5.",
        )
        self.assertIn("2026 GS-I Q3", repaired)
        self.assertIn("2026 Q3", repaired)
        self.assertNotIn("Q5", repaired)

    def test_topic_11_manual_panel_repairs_are_complete(self) -> None:
        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-11"]
        self.assertEqual(
            {
                "Mahajanapada-Magadha answer architecture",
                "Evidence ladder and confidence control",
                "Examiner traps and contested boundaries",
            },
            set(overrides),
        )
        for lines in overrides.values():
            rendered = "\n".join(lines)
            self.assertNotIn("...", rendered)
            self.assertNotIn("…", rendered)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_13_unrouted_pyq_label_is_repaired(self) -> None:
        topic = deep.Topic(
            number=13,
            topic_key="ancient-indian-history-13",
            title="State & Varna Society in the Age of the Buddha",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        source = (
            "### Verified Prelims PYQ - 2026 printed Q3: Pali coin evidence\n"
            "- VERIFIED QUESTION: local official Set-A paper; the paper itself "
            "prints this as Q3 although a repository routing ledger misnumbers it."
        )
        repaired = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("Verified unrouted Prelims practice", repaired)
        self.assertIn("does not assign this demand to Topic 13", repaired)
        self.assertNotIn("Verified Prelims PYQ", repaired)
        self.assertNotIn("routing ledger misnumbers it", repaired)

    def test_topic_16_adjacent_pyqs_are_labelled(self) -> None:
        topic = deep.Topic(
            number=16,
            topic_key="ancient-indian-history-16",
            title="Central Asian Contacts",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        source = (
            "### PYQ 02 - 2020 Prelims GS-I Q22: Mahayana schools\n"
            "### PYQ 03 - 2023 Prelims GS-I Q46: Milinda-panha attribution"
        )
        repaired = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("### Adjacent PYQ 02", repaired)
        self.assertIn("### Adjacent PYQ 03", repaired)
        self.assertNotIn("### PYQ 02", repaired)
        self.assertNotIn("### PYQ 03", repaired)

    def test_topic_17_all_pyqs_are_labelled_adjacent(self) -> None:
        topic = deep.Topic(
            number=17,
            topic_key="ancient-indian-history-17",
            title="The Satavahanas & the Deccan",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        source = "\n".join(
            (
                "### PYQ 01 - 2026 Prelims GS-I Q13: Amaravati Stupa",
                "### PYQ 02 - 2023 Prelims GS-I Q41: Dhanyakataka",
                "### PYQ 03 - 2020 GS-I Mains Q1: rock-cut architecture",
                "### PYQ 04 - 2023 Prelims GS-I Q42: stupa origin and function",
            )
        )
        repaired = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("01", "02", "03", "04"):
            self.assertIn(f"### Adjacent PYQ {number}", repaired)
            self.assertNotIn(f"### PYQ {number}", repaired)

    def test_topic_21_cross_owned_pyqs_are_labelled_adjacent(self) -> None:
        topic = deep.Topic(
            number=21,
            topic_key="ancient-indian-history-21",
            title="Life & Culture in the Gupta Age",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        source = "\n".join(
            (
                "### Verified PYQ 2 - Prelims 2020 Q36 (literature bridge)",
                "### Verified PYQ 4 - GS-I Mains 2022 Q12 (cross-owned)",
                "### Verified PYQ 5 - Prelims 2025 Q15 (cross-owned official key)",
            )
        )
        repaired = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("2", "4", "5"):
            self.assertIn(f"### Adjacent PYQ {number}", repaired)
            self.assertNotIn(f"### Verified PYQ {number}", repaired)

    def test_topic_23_semantic_supplements_and_corrections(self) -> None:
        topic = deep.Topic(
            number=23,
            topic_key="ancient-indian-history-23",
            title="Peninsular India",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        main = """# Topic

## BASIC LEARNING SESSION
Upinder says the eastern Chalukya line survived till 999 CE, when Rajaraja Chola conquered Vengi.
The Badami Chalukyas were overthrown in AD 757.
Queen Lokmahadevi and Trilok Mahadevi were patrons.

## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired = deep.augment_topic_semantic_content(topic, main)
        for phrase in (
            "Tanks, wells and channels",
            "*devadana*",
            "Indian-feudalism interpretation",
            "Segmentary-state heuristic",
            "Peasantization/agrarian-expansion approach",
            "Brahmana migration",
            "Kannada epigraphic expression",
            "Kubja Vishnuvardhana",
            "Lokamahadevi",
            "Trailokyamahadevi",
            "around AD 753",
        ):
            self.assertIn(phrase, repaired)
        self.assertNotIn("conquered Vengi", repaired)
        self.assertNotIn("AD 757", repaired)
        self.assertEqual(
            repaired,
            deep.augment_topic_semantic_content(topic, repaired),
        )
        legacy = """# Topic
## BASIC LEARNING SESSION
### SESSION 23 — CLOSING ABSENCE REPAIR: WATER, GRANT FORMS, INTERMEDIARIES AND STATE DEBATE
old invalid session supplement
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        upgraded = deep.augment_topic_semantic_content(topic, legacy)
        self.assertNotIn("### SESSION 23", upgraded)
        self.assertEqual(upgraded.count("### CLOSING SEMANTIC LEDGER A"), 1)

        workbook = """# Workbook

## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
"""
        workbook_repaired = deep.augment_topic_semantic_content(
            topic,
            workbook,
            workbook=True,
        )
        self.assertIn("Semantic-completeness coverage drills", workbook_repaired)
        self.assertIn("Lokamahadevi/Virupaksha", workbook_repaired)
        self.assertIn("*brahmadeya*, *agrahara* and *devadana*", workbook_repaired)

    def test_topic_24_semantic_supplements_and_chronology(self) -> None:
        topic = deep.Topic(
            number=24,
            topic_key="ancient-indian-history-24",
            title="Developments in Philosophy",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        main = """# Topic

## BASIC LEARNING SESSION
In Sharma's chronology, the Brahma Sutra belongs around the 2nd century CE, though exact dating remains debated.

## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired = deep.augment_topic_semantic_content(topic, main)
        for phrase in (
            "Buddhist canons",
            "Jain canons",
            "monastic archaeology",
            "Gupta centuries",
            "Gargi and Maitreyi",
            "Pali, Prakrit and Tamil",
            "Kumarila and Prabhakara",
            "2nd century BC",
        ):
            self.assertIn(phrase, repaired)
        self.assertNotIn("2nd century CE", repaired)
        self.assertEqual(
            repaired,
            deep.augment_topic_semantic_content(topic, repaired),
        )

        workbook = """# Workbook
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
"""
        workbook_repaired = deep.augment_topic_semantic_content(
            topic,
            workbook,
            workbook=True,
        )
        self.assertIn("Semantic-completeness coverage drills", workbook_repaired)
        self.assertIn("2024 Q58", workbook_repaired)
        self.assertIn("2022 Q56", workbook_repaired)

        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-24"]
        self.assertEqual(
            {
                "Chronology and evidence discipline",
                "Institutions, language and answer spine",
            },
            set(overrides),
        )
        for lines in overrides.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_25_uses_adjacent_pyqs_and_connected_history(self) -> None:
        topic = deep.Topic(
            number=25,
            topic_key="ancient-indian-history-25",
            title="Cultural Interaction with Asian Countries",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
### Verified PYQ 4 - Prelims GS-I 2024 Q64 (exact wording)
The repository treats this as a secure, locally verified owner-route question.
### Verified PYQ 5 - Prelims GS-I 2025 Q15 (exact wording)
repository Topic 20 already records the answer as officially keyed locally.
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("### Adjacent PYQ 4", normalized)
        self.assertIn("### Adjacent PYQ 5", normalized)
        self.assertNotIn("### Verified PYQ 4", normalized)
        self.assertNotIn("### Verified PYQ 5", normalized)
        self.assertIn("authoritative owner route is Topic 10", normalized)
        self.assertIn("authoritative owner route is Topic 20", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Chinese travel accounts",
            "Kumarajiva",
            "Sailendra/Borobudur",
            "Monsoon navigation",
            "zero direct PYQs",
            "formed communities",
        ):
            self.assertIn(phrase, repaired)
        self.assertEqual(
            repaired,
            deep.augment_topic_semantic_content(topic, repaired),
        )

        workbook = """# Workbook
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
"""
        workbook_repaired = deep.augment_topic_semantic_content(
            topic,
            workbook,
            workbook=True,
        )
        self.assertIn("Semantic-completeness coverage drills", workbook_repaired)
        self.assertIn("none is routed directly to Topic 25", workbook_repaired)

        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-25"]
        self.assertEqual(
            {
                "Carriers and media",
                "Southeast Asian localisation",
                "Trade, political idioms and reciprocity",
            },
            set(overrides),
        )
        for lines in overrides.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_26_uses_transition_models_and_adjacent_pyqs(self) -> None:
        topic = deep.Topic(
            number=26,
            topic_key="ancient-indian-history-26",
            title="From Ancient to Medieval",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
### Verified PYQ 1 - cross-owned
Topic 26 uses the question as a direct legacy bridge.
### Routed PYQ 5 - chronology
It is a direct Topic 26 chronology discriminator:
### Verified PYQ 7 - Buddhism
Audited local route already preserved in Topic 25.
### Adjacent PYQ 8 - architecture
### Routed PYQ 9 - north
### Routed PYQ 10 - places
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("1", "5", "7", "8", "9", "10"):
            self.assertIn(f"### Adjacent PYQ {number}", normalized)
        self.assertNotIn("### Verified PYQ", normalized)
        self.assertNotIn("### Routed PYQ", normalized)
        self.assertNotIn("direct legacy bridge", normalized)
        self.assertIn("authoritative owner route is Topic 10", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Colonial Hindu/Muslim/British division",
            "labour (vishti)",
            "zero direct PYQs",
            "Forest/hill frontiers",
            "Incoming peoples",
        ):
            self.assertIn(phrase, repaired)
        self.assertEqual(
            repaired,
            deep.augment_topic_semantic_content(topic, repaired),
        )

        workbook = """# Workbook
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
"""
        workbook_repaired = deep.augment_topic_semantic_content(
            topic,
            workbook,
            workbook=True,
        )
        self.assertIn("Semantic-completeness coverage drills", workbook_repaired)
        self.assertIn("none is routed", workbook_repaired)

        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-26"]
        self.assertEqual(
            {
                "A multitrack transition, not one date",
                "Land grant: charter to ground effects",
                "Evidence-led synthesis answer spine",
            },
            set(overrides),
        )
        for lines in overrides.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_27_chola_supplement_and_visual_controls(self) -> None:
        topic = deep.Topic(
            number=27,
            topic_key="ancient-indian-history-27",
            title="Imperial Cholas",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired = deep.augment_topic_semantic_content(topic, source)
        for phrase in (
            "Sri Lankan/Chinese account",
            "Vijayalaya-Aditya I",
            "Mandalam, valanadu, nadu, kurram",
            "dependent/servile relations",
            "Southeast Asian colonization",
            "Four routed PYQ anchors",
        ):
            self.assertIn(phrase, repaired)
        self.assertEqual(
            repaired,
            deep.augment_topic_semantic_content(topic, repaired),
        )

        workbook = """# Workbook
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
"""
        workbook_repaired = deep.augment_topic_semantic_content(
            topic,
            workbook,
            workbook=True,
        )
        self.assertIn("Semantic-completeness coverage drills", workbook_repaired)
        self.assertIn("2024 GS-I Q11", workbook_repaired)
        self.assertIn("2025 Q16", workbook_repaired)

        overrides = deep.ASCII_PANEL_LINE_OVERRIDES["ancient-indian-history-27"]
        self.assertEqual(
            {
                "State hierarchy and local institutions",
                "Land, revenue and social differentiation",
            },
            set(overrides),
        )
        for lines in overrides.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_current_status_date_is_refreshed_for_successor(self) -> None:
        original = deep.DATE
        try:
            deep.DATE = "2026-09-03"
            refreshed = deep.refresh_current_status_date(
                "- **Current-status note, rechecked 2026-08-30:** None used."
            )
        finally:
            deep.DATE = original
        self.assertIn("rechecked 2026-09-03", refreshed)
        self.assertNotIn("rechecked 2026-08-30", refreshed)

    def test_topic_02_invalid_mcq_audit_is_removed(self) -> None:
        topic = deep.Topic(
            number=2,
            topic_key="ancient-indian-history-02",
            title="Sources",
            basic_path=deep.ROOT / "AGENTS.md",
            canonical_path=deep.ROOT / "AGENTS.md",
            advanced_path=deep.ROOT / "AGENTS.md",
            cross_topic_sources=(),
            pyq_sources=(),
        )
        source = """## BASIC MCQS / REMEDIATION
#### MCQ 1
A. correct
B. wrong
C. wrong
D. wrong
**Answer: A.**
<!-- BEGIN ANSWER-WORTHINESS AUDIT: MCQS -->
#### Audit MCQ 41
A. repeated
B. repeated
C. repeated
D. repeated
**Answer: D.**
<!-- END ANSWER-WORTHINESS AUDIT: MCQS -->
## PYQS AND ANSWER PRACTICE
"""
        repaired = deep.remove_invalid_topic_mcq_audits(topic, source)
        self.assertIn("#### MCQ 1", repaired)
        self.assertNotIn("Audit MCQ 41", repaired)
        self.assertNotIn("ANSWER-WORTHINESS AUDIT", repaired)


if __name__ == "__main__":
    unittest.main()
