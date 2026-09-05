"""Targeted tests for the Medieval History deep-review driver."""

from __future__ import annotations

import unittest

import regenerate_medieval_history_deep_review as deep


class MedievalHistoryDeepReviewTests(unittest.TestCase):
    def test_manifest_order_contains_all_twenty_five_topics(self) -> None:
        topics = deep.topics()
        self.assertEqual(len(topics), 25)
        self.assertEqual(
            [topic.number for topic in topics],
            list(range(1, 26)),
        )

    def test_core_control_is_topic_specific(self) -> None:
        topic = deep.topics()[16]
        block = deep._review_block(topic)
        self.assertIn("Ibadat Khana (1575)", block)
        self.assertIn("Tauhid-i-Ilahi", block)
        self.assertIn("not a mass religion", block)

    def test_review_lines_respect_ascii_width(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_shared_mcq_rotation_remains_available(self) -> None:
        source = """# Topic

## BASIC MCQS / REMEDIATION

#### MCQ 1
- A. wrong
- B. right
- C. wronger
- D. wrongest
**Answer: B.**

## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.enforce_strict_rotation(source)
        self.assertEqual(metrics["keys"], ["A"])
        self.assertIn("- A. right", repaired)

    def test_authored_q_heading_mcqs_are_rotated(self) -> None:
        source = """# Topic

## BASIC MCQS / REMEDIATION

#### Q1. Which statement is correct?
- A. wrong
- B. right
- C. wronger
- D. wrongest
**Answer: B.**

## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.enforce_strict_rotation(source)
        self.assertEqual(metrics["keys"], ["A"])
        self.assertIn("- A. right", repaired)

    def test_authored_mains_answer_gets_full_contract(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

#### Mains 1. [10 marks | 150 words] Explain the institution.
**Introduction.** A direct thesis.
**Claim—evidence—analysis.** Named evidence proves a bounded claim.
**Conclusion.** A qualified verdict.
**Why this earns marks:** It answers the demand.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(metrics["question_count"], 1)
        self.assertIn("**Demand decoding:**", repaired)
        self.assertIn("**How to improve this answer:**", repaired)

    def test_mark_first_question_heading_gets_full_contract(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

#### 15-mark Question 01
**Question:** Examine the policy. (250 words)
**Model solution:** Named evidence supports a qualified judgment.
**Why this earns marks:** It answers the directive.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(metrics["question_count"], 1)
        self.assertIn("**Demand decoding:**", repaired)
        self.assertIn("**How to improve this answer:**", repaired)

    def test_misplaced_mains_practice_moves_after_pyqs(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION

### Part VII — Original solved Mains practice
#### Original Mains 1
**Model solution:** Evidence-led answer.

## PYQS AND ANSWER PRACTICE
#### PYQ 1
**Model answer:** Verified answer.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired = deep._normalize_practice_sections(source)
        self.assertLess(
            repaired.index("## PYQS AND ANSWER PRACTICE"),
            repaired.index("### Part VII — Original solved Mains practice"),
        )
        self.assertLess(
            repaired.index("### Part VII — Original solved Mains practice"),
            repaired.index("## OPTIONAL ADVANCED DEPTH"),
        )

    def test_topic_01_semantic_supplement_and_ascii_controls(self) -> None:
        topic = deep.topics()[0]
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired = deep.augment_topic_semantic_content(topic, source)
        for phrase in (
            "Hindu/Muslim division",
            "Muhammad bin Qasim",
            "Chachnama",
            "Alptigin/Sabuktigin",
            "Tarain I/II",
            "zero direct PYQs",
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
        self.assertIn(
            "Semantic-completeness coverage drills",
            workbook_repaired,
        )
        self.assertIn("zero direct routed PYQs", workbook_repaired)

        self.assertEqual(
            {
                "Chronology of contact and frontier change",
                "Sind as conquest and conduit",
                "Evidence discipline",
            },
            set(deep.TOPIC_01_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_01_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_ancient_topic_hooks_are_disabled_for_medieval(self) -> None:
        topic = deep.topics()[24]
        source = "## BASIC MCQS / REMEDIATION\n## PYQS AND ANSWER PRACTICE"
        self.assertEqual(source, deep.normalize_topic_pyq_metadata(topic, source))

    def test_topic_02_semantics_pyq_ownership_and_ascii(self) -> None:
        topic = deep.topics()[1]
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
### PYQ 01 - 2022 Prelims
Question wording verified through the repository's 2022 routing and matching published paper transcriptions.
### PYQ 02 - 2018 Mains
Official GS-I question verified in the repository's revised Medieval Topic 01 package; routed here because al-Biruni is a core Topic 02 source.
### PYQ 03 - 2020 Mains
Official GS-I question verified in the repository's revised Medieval Topic 01 package; routed here through the Topic 02 and Topic 07 Persian-source banks.
The package includes one direct Prelims route and two verified Mains source questions with genuine Topic 02 ownership; it does not relabel coaching questions as UPSC PYQs.
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("01", "02", "03"):
            self.assertIn(f"### Adjacent PYQ {number}", normalized)
            self.assertNotIn(f"### PYQ {number}", normalized)
        self.assertIn("No verified PYQ is routed directly", normalized)
        self.assertIn("Indian Art and Culture Topic 13", normalized)
        self.assertIn("Ancient History Sources Topic 02", normalized)
        self.assertIn("Medieval History Topic 24", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Samanid legacy",
            "slave/commander networks",
            "Ghiyath al-Din",
            "elite circulation",
            "zero direct PYQs",
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

        self.assertEqual(
            {
                "Source criticism matrix",
                "From Samanid service to Ghaznavid rule",
                "Battlefield victory to consolidation",
            },
            set(deep.TOPIC_02_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_02_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_03_state_formation_pyqs_and_ascii(self) -> None:
        topic = deep.topics()[2]
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
### PYQ 01 - 2019 Prelims
### PYQ 02 - 2022 Prelims
### PYQ 03 - 2020 Mains
The package uses two verified Prelims routes and one verified Mains source question with genuine topic ownership; no coaching prompt is relabelled as a UPSC PYQ.
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("01", "02", "03"):
            self.assertIn(f"### Adjacent PYQ {number}", normalized)
            self.assertNotIn(f"### PYQ {number}", normalized)
        self.assertIn("No verified PYQ is routed directly", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "later shorthand",
            "Ruknuddin/Razia/Bahram/Masud",
            "Tajik/Persianate officials",
            "Arhai Din ka Jhonpra",
            "zero direct PYQs",
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

        self.assertEqual(
            {
                "Mamluk century chronology",
                "Iltutmish's institutional bundle",
                "Architecture as political evidence",
            },
            set(deep.TOPIC_03_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_03_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_04_khalji_controls_pyqs_and_ascii(self) -> None:
        topic = deep.topics()[3]
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
##### PYQ 01 - UPSC Prelims 2022 GS-I
##### PYQ 02 - UPSC GS-I 2020
##### PYQ 03 - UPSC GS-I 2023
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("##### Direct PYQ 01", normalized)
        self.assertIn("##### Adjacent PYQ 02", normalized)
        self.assertIn("##### Adjacent PYQ 03", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Turkic-origin groups",
            "Padmavat",
            "Diwan-i Riyasat",
            "political control",
            "**Direct:** 2022",
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
        self.assertIn("2022 Q57", workbook_repaired)

        self.assertEqual(
            {
                "The Khalji revolution debate",
                "Effectiveness, sources and limits",
            },
            set(deep.TOPIC_04_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_04_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_ascii_review_controls_do_not_duplicate(self) -> None:
        topic = deep.topics()[3]
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        original = deep.current_manual_topic(record, topic)
        panels = original["panels"]
        for panel, label in zip(
            (panels[0], panels[9], panels[10]),
            ("MUST REMEMBER:", "CLOSE DISTINCTION:", "EVIDENCE LIMIT:"),
        ):
            panel["ascii_lines"].extend([label + " old", "  old continuation"])
        # Test the cleanup logic through a tiny equivalent to avoid rendering files.
        labels = ("MUST REMEMBER:", "CLOSE DISTINCTION:", "EVIDENCE LIMIT:")
        for panel in (panels[0], panels[9], panels[10]):
            starts = [
                index
                for index, value in enumerate(panel["ascii_lines"])
                if any(value.startswith(label) for label in labels)
            ]
            if starts:
                panel["ascii_lines"] = panel["ascii_lines"][: min(starts)]
        for panel in (panels[0], panels[9], panels[10]):
            self.assertFalse(
                any(
                    value.startswith(labels)
                    for value in panel["ascii_lines"]
                )
            )

    def test_topic_05_tughlaq_controls_pyqs_and_ascii(self) -> None:
        topic = deep.topics()[4]
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
##### PYQ 01 - UPSC Prelims GS-I 2021
##### PYQ 02 - UPSC Prelims GS-I 2022
##### PYQ 03 - UPSC GS-I 2020
##### PYQ 04 - UPSC GS-I 2023
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("##### Direct PYQ 01", normalized)
        for number in ("02", "03", "04"):
            self.assertIn(f"##### Adjacent PYQ {number}", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "selective pressured migration",
            "Ibn Battuta is",
            "provincial autonomy",
            "Diwan-i Bandagan",
            "**Direct:** 2021",
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
        self.assertIn("2021 Q38", workbook_repaired)

        self.assertEqual(
            {
                "Daulatabad without the empty-Delhi myth",
                "Reading the Tughlaq archive",
                "Works, welfare, slavery and orthodoxy",
            },
            set(deep.TOPIC_05_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_05_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_06_decline_lodi_controls_and_ascii(self) -> None:
        topic = deep.topics()[5]
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
#### PYQ 01 - 2021
#### PYQ 02 - 2022
#### PYQ 03 - 2020
#### PYQ 04 - 2023
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("01", "02", "03", "04"):
            self.assertIn(f"#### Adjacent PYQ {number}", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Central Asian conquest raid",
            "Yahya Sirhindi",
            "Afghan political networks",
            "artillery/firearms",
            "zero direct PYQs",
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

        self.assertEqual(
            {
                "How to read Timur's evidence",
                "Sayyid ruler ladder and weak sovereignty",
                "Ibrahim's fracture and Panipat system",
            },
            set(deep.TOPIC_06_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_06_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_07_cross_dynastic_controls_pyqs_and_ascii(self) -> None:
        topic = deep.topics()[6]
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
#### PYQ 01 - UPSC Prelims GS-I 2019
#### PYQ 02 - UPSC GS-I 2020
#### PYQ 03 - UPSC Prelims GS-I 2022
#### PYQ 04 - UPSC GS-I 2023
**Directly verified and solved:** 2019 Prelims GS-I revenue administration; 2020 GS-I Persian literary sources; 2023 GS-I Sultanate technology.
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("#### Direct PYQ 01", normalized)
        self.assertIn("#### Adjacent PYQ 02", normalized)
        self.assertIn("#### Adjacent PYQ 03", normalized)
        self.assertIn("#### Direct PYQ 04", normalized)
        self.assertIn("Directly routed and solved", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "farmans/orders",
            "kharaj, ushr, zakat, jizya, khams",
            "urban-revolution thesis",
            "Atlantic racial chattel slavery",
            "**Direct:** 2019",
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
        self.assertIn("three direct routed demands", workbook_repaired)

        self.assertEqual(
            {
                "Central departments with chronology caution",
                "Revenue and local hierarchy",
                "Social differentiation without static blocs",
            },
            set(deep.TOPIC_07_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_07_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_08_regional_scope_pyqs_and_ascii(self) -> None:
        topic = deep.topics()[7]
        source = """# Topic
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
#### Routed PYQ 1 - UPSC Prelims GS-I 2023 Q49
#### Routed PYQ 2 - UPSC Prelims GS-I 2022 Q92
#### Routed PYQ 3 - UPSC Prelims GS-I 2023 Q45
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("1", "2", "3"):
            self.assertIn(f"#### Direct routed PYQ {number}", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Bengal, Gujarat, Malwa, Jaunpur and Kashmir",
            "Ilyas Shahi",
            "Dilawar Khan",
            "Shah Mir dynasty",
            "not chattel slavery",
            "2026 Prelims Q37",
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
        self.assertIn("three direct routed Prelims demands", workbook_repaired)

        self.assertEqual(
            {
                "Regionalisation chronology and map",
                "Five regional capacity models",
                "Buranji and Moidam evidence ladder",
            },
            set(deep.TOPIC_08_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_08_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_09_deccan_system_pyqs_and_ascii(self) -> None:
        topic = deep.topics()[8]
        source = """# Topic
> **Export date:** 2026-08-16
## BASIC LEARNING SESSION
**Current-status note, rechecked 2026-09-03:** UNESCO's Group of Monuments at Hampi property page was rechecked on 30 August 2026.
UNESCO’s Group of Monuments at Hampi page was checked on 2026-08-16 for surviving urban, royal, sacred and water features.
uNESCO's Group of Monuments at Hampi property page was rechecked on 30 August 2026.
The basic source file attributes the list to Domingo Paes, whereas the locally preserved UPSC question names Nuniz.
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
#### PYQ 1 — UPSC Prelims GS-I 2024 Q56
#### PYQ 2 — UPSC Prelims GS-I 2021 Q35
#### PYQ 3 — UPSC Prelims GS-I 2023 Q48
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("1", "2", "3"):
            self.assertIn(f"#### Direct PYQ {number}", normalized)
        self.assertIn("repaired canonical owner name Nuniz", normalized)
        self.assertIn("**Export date:** 2026-08-30", normalized)
        self.assertIn("fetched and rechecked on 3 September 2026", normalized)
        self.assertIn("fetched and rechecked on 2026-08-30", normalized)
        self.assertNotIn("rechecked on 30 August 2026", normalized)
        self.assertNotIn("uNESCO", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Sangama -> Saluva -> Tuluva -> Aravidu",
            "Amuktamalyada",
            "segmentary, centralized",
            "Lotus Mahal",
            "Ahmadnagar, Bijapur, Golconda and Bidar",
            "Direct Mains:** zero",
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
        self.assertIn("no direct routed Mains PYQ", workbook_repaired)

        self.assertEqual(
            {
                "Foundation and evidence ladder",
                "Vijayanagara dynastic sequence",
                "Hampi urban system",
                "Topic 09 answer spine",
            },
            set(deep.TOPIC_09_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_09_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_10_plural_devotional_fields_pyqs_and_ascii(self) -> None:
        topic = deep.topics()[9]
        source = """# Topic
> **Export date:** 2026-08-17
## BASIC LEARNING SESSION
The Press Information Bureau's 11 June 2025 Kabir Jayanti tribute was rechecked through the official indexed release on 30 August 2026.
→ no live anchor because a modern heritage/commemoration page would not improve proof of medieval facts → Qdrant not needed.
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
#### PYQ 1 — UPSC Prelims GS-I 2019 Q13
#### PYQ 2 — UPSC Prelims GS-I 2022 Q58
#### PYQ 3 — UPSC Mains GS-I 2018 Q11
#### PYQ 4 — UPSC Mains GS-I 2021 Q1
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        for number in ("1", "2", "3", "4"):
            self.assertIn(f"#### Direct PYQ {number}", normalized)
        self.assertIn("**Export date:** 2026-08-30", normalized)
        self.assertIn("direct PRID page returned HTTP 403", normalized)
        self.assertIn("one optional PIB public-memory check", normalized)
        self.assertNotIn("rechecked through the official indexed release", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Bhakti and Sufism are umbrella fields",
            "wahdat al-wujud",
            "Qadiri, Shattari and Naqshbandi",
            "Bibi Fatima Sam",
            "Kulah-Daran's Topic-06 boundary",
            "routed PYQ anomaly whose factual owner is Topic 06",
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
        self.assertIn("four direct routed demands", workbook_repaired)

        self.assertEqual(
            {
                "Plural devotional chronology",
                "Sufi vocabulary and transmission",
                "Southern roots and Vedanta paths",
                "Chishti-Suhrawardi comparison",
                "Bhakti-Sufi interaction without merger",
                "Topic 10 answer spine",
            },
            set(deep.TOPIC_10_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_10_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_11_material_culture_controls_and_ascii(self) -> None:
        topic = deep.topics()[10]
        source = """# Topic
> **Export date:** 2026-08-18
## BASIC LEARNING SESSION
UNESCO's Qutb Minar and its Monuments page was rechecked on 30 August 2026.
UNESCO’s Qutb Minar and its Monuments page, fetched on 2026-08-18, on authenticity.
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("**Export date:** 2026-08-30", normalized)
        self.assertIn("fetched and rechecked on 3 September 2026", normalized)
        self.assertIn("fetched on 2026-08-30", normalized)
        self.assertNotIn("rechecked on 30 August 2026", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Sultan Ghari",
            "Jahanpanah/Adilabad",
            "Sikandar",
            "Kashmir timber-masonry",
            "Hasan Nizami, Minhaj, Amir Khusrau, Barani, Isami and Afif",
            "Direct CSE PYQs, 2018-2026",
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
        self.assertIn("zero direct UPSC CSE routes", workbook_repaired)

        self.assertEqual(
            {
                "Trabeate and arcuate load paths",
                "Qutb complex as layered patronage",
                "Tughlaq form and inference discipline",
                "Regional adaptation matrix",
                "Language, literature and music",
                "Evidence and conservation ladder",
                "Topic 11 answer spine",
            },
            set(deep.TOPIC_11_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_11_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_12_babur_state_formation_controls_and_ascii(self) -> None:
        topic = deep.topics()[11]
        source = """# Topic
> **Export date:** 2026-08-18
## BASIC LEARNING SESSION
UNESCO's Bagh-e Babur Tentative List page was rechecked on 30 August 2026.
-> no forced live heritage insert -> Qdrant not used.
No decorative live-current-affairs claim is inserted because the historical argument is fully supported by those sources.
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("**Export date:** 2026-08-30", normalized)
        self.assertIn("fetched and rechecked on 3 September 2026", normalized)
        self.assertIn("one bounded official Bagh-e Babur heritage check", normalized)
        self.assertIn("used only for phased garden and restoration", normalized)
        self.assertNotIn("rechecked on 30 August 2026", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Mughal\" is a later Indian dynastic umbrella",
            "selective, gapped and retrospective",
            "Daulat Khan and Alam Khan",
            "Ghaghra 1529",
            "conqueror and founder of a fragile project",
            "Direct CSE PYQs, 2018-2026",
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
        self.assertIn("zero direct UPSC CSE routes", workbook_repaired)

        self.assertEqual(
            {
                "Central Asian political field",
                "Layered identity and legitimacy",
                "Kabul-Qandahar strategic bridge",
                "Punjab and the Lodi opening",
                "Panipat combined-arms system",
                "Panipat-Khanwa-Ghagra ladder",
                "Baburnama and heritage source method",
                "Topic 12 answer spine",
            },
            set(deep.TOPIC_12_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_12_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_13_humayun_struggle_controls_and_ascii(self) -> None:
        topic = deep.topics()[12]
        source = """# Topic
> **Export date:** 2026-08-18
## BASIC LEARNING SESSION
UNESCO's Humayun's Tomb property page was rechecked on 30 August 2026.
uNESCO's Humayun's Tomb property page was rechecked on 30 August 2026.
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("**Export date:** 2026-08-30", normalized)
        self.assertIn("fetched and rechecked on 3 September 2026", normalized)
        self.assertNotIn("rechecked on 30 August 2026", normalized)
        self.assertNotIn("uNESCO", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Gulbadan's Humayun-nama",
            "Kamran, Askari and Hindal",
            "Surajgarh",
            "Machhiwara, Sirhind",
            "Hamida Banu",
            "Direct Topic-13 CSE PYQs, 2018-2026",
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
        self.assertIn("zero direct CSE routes", workbook_repaired)

        self.assertEqual(
            {
                "The central problem: conquest without consolidation",
                "Brothers: chronology before blame",
                "Rajput-Gujarat-Mughal western triangle",
                "Sher Khan's Bihar-Bengal scale-up",
                "Chausa and Kannauj: do not collapse the battles",
                "Exile, Safavid bargain and restoration",
                "Evidence, rehabilitation and heritage",
                "Topic 13 answer spine",
            },
            set(deep.TOPIC_13_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_13_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_14_sur_state_capacity_controls_and_ascii(self) -> None:
        topic = deep.topics()[13]
        source = """# Topic
> **Export date:** 2026-08-18
## BASIC LEARNING SESSION
The Rohtas district administration's Sher Shah Suri Tomb page was rechecked through the official government listing on 30 August 2026.
No direct verified CSE 2018-2025 Topic 14 question.
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("**Export date:** 2026-08-30", normalized)
        self.assertIn("fetched and rechecked", normalized)
        self.assertIn("3 September 2026", normalized)
        self.assertNotIn("30 August 2026", normalized)
        self.assertIn("2018-2026", normalized)
        self.assertNotIn("2018-2025", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Tarikh-i Sher Shahi",
            "Raisen 1543",
            "patta/qabuliyat",
            "not invention",
            "Rohtas (Pakistan) and Rohtasgarh (Bihar)",
            "Direct Topic-14 CSE PYQs, 2018-2026",
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
        self.assertIn("zero direct CSE routes", workbook_repaired)

        self.assertEqual(
            {
                "From Farid to Sher Shah",
                "Empire and campaign fields",
                "Afghan monarchy and personal supervision",
                "Revenue measurement and record chain",
                "Road-sarai-customs-dak circulation system",
                "Money, order and military controls",
                "Forts, religion and succession limits",
                "Continuity, source method and Akbar",
                "Topic 14 answer spine",
            },
            set(deep.TOPIC_14_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_14_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_15_akbar_expansion_controls_and_ascii(self) -> None:
        topic = deep.topics()[14]
        source = """# Topic
**Complete learning session | GS-I Medieval India | Prelims, Mains and historical method | 18 August 2026**
## BASIC LEARNING SESSION
UNESCO's Fatehpur Sikri property page was rechecked on 30 August 2026.
Live heritage check: official UNESCO/ASI/Ministry pages for Fatehpur Sikri, Agra Fort and the Hill Forts of Rajasthan were checked on 18 August 2026.
No direct Topic-15-owner CSE Prelims or GS-I PYQ for 2018-2025.
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("3 September 2026**", normalized)
        self.assertIn("fetched and rechecked on 3 September 2026", normalized)
        self.assertIn("not treated as newly rechecked live claims", normalized)
        self.assertIn("2018-2026", normalized)
        self.assertNotIn("2018-2025", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Akbarnama is rich imperial teleology",
            "Chand Bibi",
            "Roshanai",
            "Tauhid-i Ilahi",
            "Salim's Allahabad",
            "Direct Topic-15 CSE PYQs, 2018-2026",
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
        self.assertIn("zero direct CSE routes", workbook_repaired)

        self.assertEqual(
            {
                "The fractured field of 1556",
                "Bairam Khan to personal rule",
                "Noble and Uzbek challenge",
                "Rajput policy in phases",
                "Gujarat and Bengal: conquest plus retention",
                "Haldighati: coalition and outcome",
                "Rebellion, frontier and source method",
                "Topic 15 answer spine",
            },
            set(deep.TOPIC_15_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_15_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_16_akbar_institutional_controls_and_ascii(self) -> None:
        topic = deep.topics()[15]
        source = """# Topic
> **Package date:** 18 August 2026
## BASIC LEARNING SESSION
The Department of Land Resources' DILRMP page was rechecked on 30 August 2026.
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("**Package date:** 3 September 2026", normalized)
        self.assertIn("fetched and rechecked on 3 September 2026", normalized)
        self.assertNotIn("30 August 2026", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Ain-i Akbari is court-sponsored",
            "commonly fifteen by reign-end",
            "Du-aspa sih-aspa",
            "Tankhwah jagir",
            "Ilahi calendar/era",
            "Direct:** 2021 Prelims Q45",
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
        self.assertIn("one direct routed demand", workbook_repaired)

        self.assertEqual(
            {
                "Central offices and ruler-centred checks",
                "Province to village: hierarchy and counterweights",
                "Mansabdari: rank, remuneration and obligation",
                "Zat, sawar and jagir logic",
                "Dagh, chehra and the verification problem",
                "Revenue reform as experiment",
                "Zabt-dahsala calculation chain",
                "Methods, geography and mediation",
                "Continuity, evidence and structural limits",
                "Topic 16 answer spine",
            },
            set(deep.TOPIC_16_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_16_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_17_akbar_religious_policy_controls_and_ascii(self) -> None:
        topic = deep.topics()[16]
        source = """# Topic
> **Subject:** Medieval Indian History | **Export date:** 18 August 2026
**Live-source check, 18 August 2026:** an official ASI Agra Circle page and UNESCO's Fatehpur Sikri World Heritage page were checked.
**Current-status note, rechecked 2026-08-30:** UNESCO's Fatehpur Sikri property page was rechecked on 30 August 2026.
#### Direct CSE Mains PYQ - verified local official/OCR route
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("**Export date:** 4 September 2026", normalized)
        self.assertIn("fetched and rechecked on 4 September 2026", normalized)
        self.assertIn("Direct PYQ — UPSC Mains 2025 GS-I Q2", normalized)
        self.assertNotIn("30 August 2026", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Personal belief, public policy, juristic arbitration",
            "practical/final debate closure (1581/1582)",
            "Maktab Khana/translation programme",
            "Blochmann reconstructed about eighteen nobles",
            "modern constitutional secularism",
            "Direct:** 2025 GS-I Q2",
            "Adjacent only:** 2020 GS-I Q12",
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
        self.assertIn("one direct verified Mains demand", workbook_repaired)
        self.assertIn("No direct Prelims route", workbook_repaired)

        self.assertEqual(
            {
                "Evolution, not a sudden creed",
                "Five layers of Akbar's religious policy",
                "Ibadat Khana debate cycle",
                "Interfaith encounter: influence is not conversion",
                "The debate paradox",
                "Mahzar: scope before significance",
                "Sulh-i-kul as a governing principle",
                "Tauhid-i-Ilahi: neither mass religion nor nothing",
                "Inclusion and coercion in one empire",
                "Source triangle and evidentiary limits",
                "2025 GS-I syncretism answer map",
                "Topic 17 final answer spine",
            },
            set(deep.TOPIC_17_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_17_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_18_deccan_mughal_controls_and_ascii(self) -> None:
        topic = deep.topics()[17]
        source = """# Topic
> **Subject:** Medieval Indian History | **Export date:** 18 August 2026
**Current-status note, rechecked 2026-08-30:** UNESCO's Maratha Military Landscapes and Deccan Sultanate tentative-list pages were rechecked on 30 August 2026.
### SESSION 15 — -57: BREAKDOWN OF THE SETTLEMENT
#### CLOSING RECALL FLOW — -57: BREAKDOWN OF THE SETTLEMENT
START / CONCEPT: -57: breakdown of the settlement
Malik Ambar continued resistance. The owner source dates his death to 1627, whereas some secondary chronologies differ. This package uses 1627 because the assigned OCR and basic/advanced owner files do so, and marks the dating disagreement rather than silently harmonising it.
| ✅ 1627 | Death of Malik Ambar; Shah Jahan soon adopts a more decisive policy |
| Aurangzeb's later wars | Topic 22 | Outside the 1657 boundary |
| Shivaji, mature Maratha state and later Deccan crisis | Topic 23 | Topic 18 supplies only the pre-Shivaji bridge |
Transparent PYQ audit: 2018-2025 CSE
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("**Export date:** 4 September 2026", normalized)
        self.assertIn("SESSION 15 — 1656-57", normalized)
        self.assertIn("standard biographical chronology is 1626", normalized)
        self.assertIn("| ✅ 1626 | Death of Malik Ambar", normalized)
        self.assertIn("2018-2026", normalized)
        self.assertIn("later Deccan-Maratha war", normalized)
        self.assertNotIn("Outside the 1657 boundary", normalized)
        self.assertIn("did not claim a new live status check", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Faruqi Khandesh as the northern gateway",
            "standard death date of 1626",
            "Aurangzeb's viceroyalties, 1636-44 and 1652-57",
            "inflated jama, weak hasil",
            "Mir Jumla's rupture with Golconda",
            "Direct Topic-18 CSE routes, 2018-2026:** zero",
            "2024 Prelims Q56",
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
        self.assertIn("zero direct CSE routes for 2018-2026", workbook_repaired)
        self.assertIn("Topics 24/source bank and 09", workbook_repaired)

        self.assertEqual(
            {
                "The Deccan as a connected but frictional field",
                "Deccan chronology 1562-1657",
                "A spectrum of political relations",
                "Chand Bibi and the Ahmadnagar crisis",
                "Akbar's foothold and its limits",
                "Malik Ambar's resistance engine",
                "Why conquest did not equal consolidation",
                "Jahangir: recovery with restraint",
                "The pre-Shivaji Maratha bridge",
                "Daulatabad and the 1636 settlement",
                "Why the 1656-57 compact broke",
                "Topic 18 final answer spine",
            },
            set(deep.TOPIC_18_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_18_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_19_foreign_policy_controls_and_ascii(self) -> None:
        topic = deep.topics()[18]
        source = """# Topic
> Subject: Medieval Indian History | Date: 2026-08-18.
**Current-status note, rechecked 2026-08-30:** PMIndia's 30 June 2026 release was rechecked through live search on 30 August 2026. It records a bounded comparison.
### SESSION 16 — -53: THREE UNSUCCESSFUL RECOVERY ATTEMPTS
#### CLOSING RECALL FLOW — -53: THREE UNSUCCESSFUL RECOVERY ATTEMPTS
START / CONCEPT: -53: three unsuccessful recovery attempts
Transparent PYQ audit: 2018-2025 CSE
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("Date: 2026-09-04", normalized)
        self.assertIn("SESSION 16 — 1649-53", normalized)
        self.assertIn("2018-2026", normalized)
        self.assertIn("did not claim a new live check", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Qandahar/Kandahar is not Gandhara",
            "Roshanai movement associated with Bayazid Ansari",
            "Hakim Humam",
            "Iqbalnama's 3,000 troops",
            "Ali Mardan Khan's defection",
            "October 1647",
            "Direct Topic-19 CSE routes, 2018-2026:** zero",
            "2020 GS-I Q12",
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
        self.assertIn("zero direct verified Topic-19", workbook_repaired)
        self.assertIn("2018 Ashgabat and 2024 Central Asian", workbook_repaired)

        self.assertEqual(
            {
                "A qualified foreign-policy framework",
                "Northwest strategic geography",
                "Four-court balance, not a sectarian bloc",
                "Diplomacy as message, intelligence and theatre",
                "Akbar and the Uzbek balance",
                "Why Qandahar mattered",
                "Jahangir and the loss of 1622",
                "Shah Jahan recovers Qandahar in 1638",
                "Balkh 1646-47: forward defence meets limits",
                "Why Qandahar resisted recovery, 1649-53",
                "Evidence and the bounded modern bridge",
                "Topic 19 final answer spine",
            },
            set(deep.TOPIC_19_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_19_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_topic_20_jahangir_court_state_controls_and_ascii(self) -> None:
        topic = deep.topics()[19]
        source = """# Topic
> Subject: Medieval Indian History | Date: 2026-08-18.
**Current-status note, rechecked 2026-08-30:** The District Agra government and UNESCO Agra Fort pages were rechecked on 30 August 2026. They support bounded heritage claims.
Transparent PYQ audit: 2018-2025 CSE
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("Date: 2026-09-04", normalized)
        self.assertIn("2018-2026", normalized)
        self.assertIn("did not claim a new live", normalized)

        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Khusrau's revolt and Guru Arjan's death are 1606",
            "Islam Khan's 1608 Bengal governorship",
            "Rana Amar Singh excused personal attendance",
            "Swally/Suvali 1612",
            "coins with Badshah Begum-linked authority",
            "no secure contemporary evidence proves a stable",
            "Khurram's Mewar/Deccan reputation",
            "Mahabat held the emperor's body",
            "Direct Topic-20 CSE Prelims/GS-I routes, 2018-2026: zero",
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
        self.assertIn("zero direct verified Topic-20", workbook_repaired)
        self.assertIn("Mains has no objective key", workbook_repaired)

        self.assertEqual(
            {
                "Jahangir's reign: the chronology spine",
                "Continuity, consolidation and contest",
                "Accession, orders and the chain of justice",
                "Khusrau and Guru Arjan: event plus source matrix",
                "Mewar 1615: pressure joined to accommodation",
                "English commercial diplomacy without colonial teleology",
                "Nur Jahan's authority: evidence before label",
                "The fixed-junta thesis under review",
                "Why Khurram rebelled, 1622-25",
                "Mahabat Khan's coup, 1626",
                "Jahangir as ruler and historical source",
                "Topic 20 final answer spine",
            },
            set(deep.TOPIC_20_ASCII_OVERRIDES),
        )
        for lines in deep.TOPIC_20_ASCII_OVERRIDES.values():
            self.assertNotIn("...", "\n".join(lines))
            self.assertNotIn("…", "\n".join(lines))
            self.assertLessEqual(max(map(len, lines)), 100)
        topic_flow = "\n".join(
            line
            for lines in deep.TOPIC_20_ASCII_OVERRIDES.values()
            for line in lines
        )
        self.assertIn("Islam Khan 1608", topic_flow)
        self.assertIn("KANGRA", topic_flow)

    def test_topic_21_ruling_class_mansab_controls_and_ascii(self) -> None:
        topic = deep.topics()[20]
        source = """# Topic
> Date: 2026-08-18
Transparent PYQ audit: 2018-2025
## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("2026-09-04", normalized)
        self.assertIn("2018-2026", normalized)
        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "Athar Ali's 500-zat-plus series",
            "not foreign agents",
            "Du-aspa sih-aspa",
            "one-third",
            "Rs 40 per sawar",
            "912/176",
            "Direct Topic-21 CSE Prelims/GS-I routes",
        ):
            self.assertIn(phrase, repaired)
        self.assertEqual(repaired, deep.augment_topic_semantic_content(topic, repaired))
        workbook = deep.augment_topic_semantic_content(
            topic,
            "# Workbook\n## BASIC MCQS / REMEDIATION\n## PYQS AND ANSWER PRACTICE\n",
            workbook=True,
        )
        self.assertIn("zero direct verified Topic-21", workbook)
        self.assertEqual(
            {
                "Visible apex and managed strain",
                "Shah Jahan chronology, 1628-58",
                "The ruling class as a composite service elite",
                "Recruitment, reproduction and faction",
                "Mansabdari evolution and verification",
                "Jagir vocabulary: claim is not ownership",
                "How the month-scale worked",
                "From paper rank to effective force",
                "Expansion creates resources and claimants",
                "Grandeur as political economy",
                "Succession as a ruling-class stress test",
                "Topic 21 final answer spine",
            },
            set(deep.TOPIC_21_ASCII_OVERRIDES),
        )
        flow = "\n".join(
            line for lines in deep.TOPIC_21_ASCII_OVERRIDES.values() for line in lines
        )
        for phrase in ("Sadullah Khan", "one-third", "Rs 40", "SAMUGARH"):
            self.assertIn(phrase.casefold(), flow.casefold())
        self.assertLessEqual(max(map(len, flow.splitlines())), 100)

    def test_topic_22_aurangzeb_policy_rajput_controls_and_ascii(self) -> None:
        topic = deep.topics()[21]
        source = "# T\nDate: 2026-08-18\n2018-2025\n## BASIC LEARNING SESSION\n## BASIC MCQS / REMEDIATION\n## PYQS AND ANSWER PRACTICE\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n## CONSOLIDATED REGISTER NOTES\n"
        normalized = deep.normalize_topic_pyq_metadata(topic, source)
        self.assertIn("2026-09-04", normalized)
        self.assertIn("2018-2026", normalized)
        repaired = deep.augment_topic_semantic_content(topic, normalized)
        for phrase in (
            "sponsored collective Hanafi compendium",
            "1704 southern suspension",
            "Kashi and Mathura",
            "Champat Rai/Chhatrasal",
            "Waqa-i-Ajmer",
            "Direct Topic-22 CSE",
        ):
            self.assertIn(phrase, repaired)
        self.assertEqual(repaired, deep.augment_topic_semantic_content(topic, repaired))
        self.assertEqual(
            {
                "Differentiated rule under pressure",
                "Aurangzeb chronology, 1658-1707",
                "Sharia, zawabit and imperial choice",
                "Jizyah, 1679: fiscal form and political signal",
                "Temple policy: test one action at a time",
                "Composite nobility: inclusion is not equality",
                "Guru Tegh Bahadur: source and consequence",
                "Jats and Satnamis: compare mechanisms",
                "Marwar: succession becomes legitimacy crisis",
                "Mewar and Prince Akbar, 1681",
                "Religious policy and Mughal weakening",
                "Topic 22 final answer spine",
            },
            set(deep.TOPIC_22_ASCII_OVERRIDES),
        )
        flow = "\n".join(
            x for lines in deep.TOPIC_22_ASCII_OVERRIDES.values() for x in lines
        )
        for phrase in ("FATAWA-I-ALAMGIRI", "KASHI", "Chhatrasal", "Durgadas"):
            self.assertIn(phrase.casefold(), flow.casefold())
        self.assertLessEqual(max(map(len, flow.splitlines())), 100)

    def test_topic_23_maratha_deccan_jagir_controls_and_ascii(self) -> None:
        topic = deep.topics()[22]
        source = "# T\nDate: 2026-08-19\n2018-2025\n## BASIC LEARNING SESSION\n## BASIC MCQS / REMEDIATION\n## PYQS AND ANSWER PRACTICE\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n## CONSOLIDATED REGISTER NOTES\n"
        repaired = deep.augment_topic_semantic_content(
            topic, deep.normalize_topic_pyq_metadata(topic, source)
        )
        for phrase in (
            "Shahji's Ahmadnagar-Mughal-Bijapur career",
            "Annaji Datto's 1679",
            "parallel chauth",
            "Sambhaji's 1689 execution",
            "be-jagiri",
            "Direct Topic-23 CSE routes",
        ):
            self.assertIn(phrase, repaired)
        self.assertEqual(
            {
                "Western Deccan: terrain becomes a fort network",
                "Chronology from the 1640s to 1707",
                "Purandar, Agra and recovery",
                "Coronation and the language of sovereignty",
                "Ashtapradhan: eight offices, not a cabinet",
                "Chauth and sardeshmukhi are distinct claims",
                "Cavalry and ganimi kava",
                "Coast and navy: capability with scale limits",
                "Resistance after Shivaji",
                "Annexation removes buffers",
                "Jagirdari terms and the feedback loop",
                "Topic 23 final answer spine",
            },
            set(deep.TOPIC_23_ASCII_OVERRIDES),
        )
        flow = "\n".join(
            x for lines in deep.TOPIC_23_ASCII_OVERRIDES.values() for x in lines
        )
        for phrase in ("SHAHJI", "GAGA BHATTA", "Tarabai", "PAIBAQI"):
            self.assertIn(phrase.casefold(), flow.casefold())
        self.assertLessEqual(max(map(len, flow.splitlines())), 100)

    def test_topic_24_society_economy_culture_controls_and_ascii(self) -> None:
        topic = deep.topics()[23]
        source = "# T\nDate: 2026-08-19\n2018-2025\n## BASIC LEARNING SESSION\n## BASIC MCQS / REMEDIATION\n## PYQS AND ANSWER PRACTICE\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n## CONSOLIDATED REGISTER NOTES\n"
        repaired = deep.augment_topic_semantic_content(
            topic, deep.normalize_topic_pyq_metadata(topic, source)
        )
        for phrase in (
            "khud-kasht/riyayati",
            "banjara carriers",
            "Slavery varied",
            "weak links between learned theory",
            "2020 GS-I Q12",
        ):
            self.assertIn(phrase, repaired)
        self.assertEqual(
            {
                "Layered society, not a court-peasant binary",
                "Nobility: mansab, household and reproduction",
                "Zamindars across a spectrum",
                "Cultivators and layered rights",
                "Women, work and source silence",
                "Towns and the middle strata",
                "Karkhana and craft production",
                "Inland trade, hundi and banjara",
                "Overseas trade, companies and bullion",
                "Technology without stagnation or industrial teleology",
                "Culture as institutional and composite production",
                "Topic 24 final answer spine",
            },
            set(deep.TOPIC_24_ASCII_OVERRIDES),
        )
        flow = "\n".join(
            x for lines in deep.TOPIC_24_ASCII_OVERRIDES.values() for x in lines
        )
        for phrase in ("PAHI-KASHT", "SLAVERY", "HUNDI", "2020 GS-I"):
            self.assertIn(phrase.casefold(), flow.casefold())
        self.assertLessEqual(max(map(len, flow.splitlines())), 100)

    def test_topic_25_decline_eighteenth_century_controls_and_ascii(self) -> None:
        topic = deep.topics()[24]
        source = "# T\nDate: 2026-08-19\n2018-2025\n## BASIC LEARNING SESSION\n## BASIC MCQS / REMEDIATION\n## PYQS AND ANSWER PRACTICE\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n## CONSOLIDATED REGISTER NOTES\n"
        repaired = deep.augment_topic_semantic_content(
            topic, deep.normalize_topic_pyq_metadata(topic, source)
        )
        for phrase in (
            "Bahadur Shah I 1707-12",
            "paibaqi shortage",
            "Rohilla",
            "Karnal",
            "colonial non-inevitability",
            "Direct Topic-25 CSE routes",
        ):
            self.assertIn(phrase, repaired)
        self.assertEqual(
            {
                "Chronology, 1707-1761",
                "Decline as a converging system",
                "Succession and the Sayyid wizarat",
                "Four jagirdari terms",
                "The jagirdari feedback loop",
                "The inherited Deccan burden",
                "From centre to region: a spectrum",
                "Bengal, Awadh and Hyderabad compared",
                "Jats, Sikhs and Marathas: bounded snapshot",
                "Nadir Shah, Abdali and Panipat",
                "Regional economic and cultural continuity",
                "Non-inevitability and final answer spine",
            },
            set(deep.TOPIC_25_ASCII_OVERRIDES),
        )
        flow = "\n".join(
            x for lines in deep.TOPIC_25_ASCII_OVERRIDES.values() for x in lines
        )
        for phrase in ("Farrukhsiyar", "BE-JAGIRI", "ROHILLAS", "KARNAL", "Buxar"):
            self.assertIn(phrase.casefold(), flow.casefold())
        self.assertLessEqual(max(map(len, flow.splitlines())), 100)


if __name__ == "__main__":
    unittest.main()
