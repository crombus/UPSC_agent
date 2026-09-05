"""Targeted tests for the 38-topic Modern History deep-review driver."""

from __future__ import annotations

import unittest

import regenerate_modern_history_deep_review as deep


class ModernHistoryDeepReviewTests(unittest.TestCase):
    def test_manifest_order_contains_all_thirty_eight_topics(self) -> None:
        topics = deep.topics()
        self.assertEqual(38, len(topics))
        self.assertEqual(list(range(1, 39)), [topic.number for topic in topics])

    def test_topic_controls_cover_exact_chronology(self) -> None:
        decline = deep._review_block(deep.topics()[0])
        self.assertIn("1707", decline)
        self.assertIn("1739", decline)
        bengal = deep._review_block(deep.topics()[3])
        self.assertIn("23 June 1757", bengal)
        self.assertIn("22 October 1764", bengal)
        self.assertIn("1765-72 Dual Government", bengal)
        transfer = deep._review_block(deep.topics()[26])
        self.assertIn("18 July 1947", transfer)
        self.assertIn("Radcliffe Award", transfer)
        nehru = deep._review_block(deep.topics()[31])
        self.assertIn("15 March 1950", nehru)
        emergency = deep._review_block(deep.topics()[34])
        self.assertIn("12 June 1975", emergency)
        rajiv = deep._review_block(deep.topics()[36])
        self.assertIn("404 of 514", rajiv)
        home_rule = deep._review_block(deep.topics()[17])
        self.assertIn("20 August 1917", home_rule)
        gandhi = deep._review_block(deep.topics()[18])
        self.assertIn("13 April 1919", gandhi)
        non_cooperation = deep._review_block(deep.topics()[19])
        self.assertIn("4 February 1922", non_cooperation)
        self.assertIn("12 February", non_cooperation)
        self.assertNotIn("5 February 1922", non_cooperation)

    def test_topics_01_35_have_idempotent_semantic_supplements(self) -> None:
        for topic in deep.topics()[:35]:
            source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
            once = deep.augment_topic_semantic_content(topic, source)
            twice = deep.augment_topic_semantic_content(topic, once)
            self.assertEqual(once, twice)
            self.assertIn(f"### TOPIC {topic.number:02d} CLOSING", once)
            workbook = deep.augment_topic_semantic_content(
                topic,
                source,
                workbook=True,
            )
            self.assertIn("PYQ ownership control", workbook)

    def test_topics_01_38_use_exact_twelve_authored_panel_controls(self) -> None:
        for topic in deep.topics():
            controls = deep.AUTHORED_PANEL_CONTROLS[topic.topic_key]
            self.assertEqual(12, len(controls))
            self.assertTrue(
                all(
                    max(map(len, body.splitlines())) <= 100
                    for _, _, body, _ in controls
                )
            )

    def test_topics_01_38_define_canonical_owner_repairs(self) -> None:
        for topic in deep.topics():
            text = deep.CANONICAL_OWNER_CONTROLS[topic.number]
            self.assertIn("Semantic-completeness ownership and PYQ control", text)
            self.assertIn("Verified PYQ ownership, 2018-2026", text)
        for topic in deep.topics()[15:]:
            self.assertIn(
                "Date control",
                deep.CANONICAL_OWNER_CONTROLS[topic.number],
            )

    def test_topics_11_15_enforce_requested_cross_owner_boundaries(self) -> None:
        controls = deep.CANONICAL_OWNER_CONTROLS
        self.assertIn("Topic 12 owns Crown rule", controls[11])
        self.assertIn("Topic 17 owns separate", controls[12])
        self.assertIn("current IR, Geography", controls[13])
        self.assertIn("Topic 15 owns partition", controls[14])
        self.assertIn("Topic 16 begins the", controls[15])
        self.assertIn("Topic 17 owns communalism", controls[15])
        self.assertIn("Topic 21 owns HRA", controls[16])
        self.assertIn("Topic 27 owns", controls[17])
        self.assertIn("Topic 16 owns Ghadar", controls[18])
        self.assertIn("Topic 20 owns", controls[19])
        self.assertIn("Topic 21 owns Swarajists", controls[20])
        self.assertIn("Topic 26 alone", controls[21])
        self.assertIn("Topic 27 owns", controls[21])
        self.assertIn("Topic 26 owns INA", controls[22])
        self.assertIn("Topic 27 owns", controls[22])
        self.assertIn("Topic 26 exclusively", controls[23])
        self.assertIn("Topic 27 owns", controls[23])
        self.assertIn("Topic 26 alone", controls[24])
        self.assertIn("Topic 27 owns", controls[24])
        self.assertIn("Topic 26 exclusively", controls[25])
        self.assertIn("Topic 27 owns", controls[25])
        self.assertIn("Topic 27 exclusively owns", controls[26])
        self.assertIn("Topic 28 owns", controls[27])
        self.assertIn("Topic 30 owns", controls[28])
        self.assertIn("Topic 32 owns", controls[29])
        self.assertIn("Topic 31 exclusively owns", controls[30])
        self.assertIn("Topic 36 owns Janata", controls[35])
        self.assertIn("Topic 37 owns the Rajiv", controls[35])
        self.assertIn("Topic 38 owns", controls[35])

    def test_contested_topics_are_qualified(self) -> None:
        revolt = deep._review_block(deep.topics()[10])
        self.assertIn("neither a uniform national war", revolt)
        communalism = deep._review_block(deep.topics()[16])
        self.assertIn("not an ancient, inevitable", communalism)
        partition = deep._review_block(deep.topics()[26])
        self.assertIn("single-person blame", partition)

    def test_review_lines_respect_ascii_width(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_long_output_paths_remain_windows_safe(self) -> None:
        for topic in deep.topics():
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_mcq_rotation_preserves_correct_answer_text(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION

#### MCQ 1
- A. wrong
- B. correct chronology
- C. wronger
- D. wrongest
**Answer: B.**

## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.enforce_strict_rotation(source)
        self.assertEqual(["A"], metrics["keys"])
        self.assertIn("- A. correct chronology", repaired)

    def test_mark_first_mains_gets_full_contract(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

#### 15-mark Question 01
**Question:** Examine the constitutional change. (250 words)
**Model solution:** The 1935 Act created provincial autonomy but its federation never operated.
**Why this earns marks:** It answers the directive.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(1, metrics["question_count"])
        self.assertIn("**Demand decoding:**", repaired)
        self.assertIn("**How to improve this answer:**", repaired)

    def test_model_thesis_answer_gets_full_contract(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 - 10 MARKS
**Question:** What changed under the Government of India Act 1858?
**Model thesis:** Sovereignty changed while district machinery continued.
**Evidence spine:**
- The Act ended Company rule.
**Conclusion:** Change and continuity coexisted.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(1, metrics["question_count"])
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

    def test_source_contract_requires_date_and_historiography_discipline(self) -> None:
        topic = deep.topics()[0]
        contract = deep.source_contract(topic, {"provenance": {}})
        self.assertIn("Event, proposal, enactment, commencement", contract)
        self.assertIn("Colonial, nationalist, Marxist, subaltern", contract)
        self.assertIn("approved: false", contract)

    def test_topic36_foundation_date_is_repaired_only_in_successor_text(self) -> None:
        source = (
            "Telugu Desam was founded by N.T. Rama Rao as a new regional "
            "party in 1983; it did not grow out of the Congress."
        )
        repaired = deep.repair_topic_content(source, deep.topics()[35])
        self.assertIn("29 March 1982", repaired)
        self.assertIn("1983 Andhra Pradesh election", repaired)

    def test_topic09_supplementary_pyq_gaps_are_closed_in_successor(self) -> None:
        source = (
            "**Status:** open-evidence-gap\n"
            "The locally held owner records only the routed stem and no "
            "explanatory evidence. No association or answer is asserted.\n"
            "No supporting occurrence exists in the held books or owners. No "
            "translator is named and no answer is inferred."
        )
        repaired = deep.repair_topic_content(source, deep.topics()[8])
        self.assertIn("Rabindranath Tagore", repaired)
        self.assertIn("M.K. Gandhi", repaired)
        self.assertNotIn("open-evidence-gap", repaired)

    def test_topic10_phule_and_vital_facts_are_repaired(self) -> None:
        source = (
            "Jotirao and Savitribai Phule opened a girls' school at Poona in 1851.\n"
            "**Status:** open-evidence-gap\n"
            "The held repository contains no supporting attribution and no "
            "official local key. No publisher is asserted."
        )
        repaired = deep.repair_topic_content(source, deep.topics()[9])
        self.assertIn("Bhide Wada", repaired)
        self.assertIn("1848", repaired)
        self.assertIn("Gopal Baba Walangkar", repaired)
        self.assertNotIn("open-evidence-gap", repaired)

    def test_topic15_supplementary_pyq_gaps_are_closed(self) -> None:
        source = (
            "**Status:** open-evidence-gap\n"
            "The routed local owner and held official-key set do not establish "
            "the answer. No leader is named solely from memory; the package "
            "retains the demand as a verification card.\n"
            "The held repository records the routed demand but lacks sufficient "
            "support for the statement-level answer and circulation claims. No "
            "unsupported attribution or number is asserted."
        )
        repaired = deep.repair_topic_content(source, deep.topics()[14])
        self.assertIn("Lala Lajpat Rai", repaired)
        self.assertIn("India, not Bengal alone", repaired)
        self.assertNotIn("open-evidence-gap", repaired)

    def test_topic16_ghadar_pyq_gap_is_closed_without_fabricating_key(self) -> None:
        source = (
            "**Status:** open-evidence-gap\n"
            "The routed local question is verified, but its official answer "
            "key is unavailable locally. Preserve it as an association-check "
            "card: Barindra belongs to Bengal's revolutionary milieu, Rash "
            "Behari later worked with the wartime rising, and no option is "
            "declared from memory."
        )
        repaired = deep.repair_topic_content(source, deep.topics()[15])
        self.assertIn("only Rash Behari Bose", repaired)
        self.assertIn("'3 only'", repaired)
        self.assertIn("inferred answer", repaired)
        self.assertNotIn("open-evidence-gap", repaired)

    def test_topic37_election_denominator_is_repaired(self) -> None:
        source = (
            "Rajiv Gandhi won a record majority of about 415 of 543 seats "
            "in the December 1984 general election."
        )
        repaired = deep.repair_topic_content(source, deep.topics()[36])
        self.assertIn("404 of the 514 seats elected", repaired)
        self.assertNotIn("415 of 543", repaired)

    def test_topic34_tashkent_death_date_is_repaired(self) -> None:
        source = (
            "Shastri signed the Tashkent Declaration and died at Tashkent on "
            "10 January 1966."
        )
        repaired = deep.repair_topic_content(source, deep.topics()[33])
        self.assertIn("died at Tashkent on 11 January 1966", repaired)
        self.assertNotIn("died at Tashkent on 10 January 1966", repaired)

    def test_topic38_hindu_law_equality_claim_is_qualified(self) -> None:
        source = (
            "The Hindu Code Bill was enacted as four separate Acts, covering "
            "Marriage, Succession, Minority and Guardianship, and Adoption "
            "and Maintenance, giving women legal equality."
        )
        repaired = deep.repair_topic_content(source, deep.topics()[37])
        self.assertIn("Hindu Marriage Act, 1955", repaired)
        self.assertIn("did not create complete legal or social equality", repaired)
        self.assertNotIn("giving women legal equality", repaired)

    def test_historical_topics_remain_immutable_reuses(self) -> None:
        result = deep._historical_completed_result(deep.topics()[0])
        self.assertIsNotNone(result)
        assert result is not None
        latest = deep.latest(deep.load(deep.STATUS), "modern-indian-history-01")
        self.assertEqual(latest["record_id"], result["new_record_id"])
        self.assertEqual(int(latest["generation"]), result["new_generation"])

    def test_porcelain_parser_preserves_unicode_and_spaces(self) -> None:
        output = (
            " M notes/Final-Learning-Packages/Geography/"
            "Part A — Physical Geography/session file.pdf\0"
            "?? notes/History/new file with spaces.md\0"
        ).encode("utf-8")
        current, removed = deep._parse_porcelain_v1_z(output)
        self.assertEqual(
            {
                "notes\\Final-Learning-Packages\\Geography\\"
                "Part A — Physical Geography\\session file.pdf",
                "notes\\History\\new file with spaces.md",
            },
            current,
        )
        self.assertEqual(set(), removed)

    def test_porcelain_parser_handles_statuses_renames_and_copies(self) -> None:
        output = (
            "A  notes/History/added file.md\0"
            "R  notes/History/renamed — destination.md\0"
            "notes/History/original name.md\0"
            "C  notes/History/copied destination.md\0"
            "notes/History/copied source.md\0"
            " D notes/History/deleted file.md\0"
        ).encode("utf-8")
        current, removed = deep._parse_porcelain_v1_z(output)
        self.assertEqual(
            {
                "notes\\History\\added file.md",
                "notes\\History\\renamed — destination.md",
                "notes\\History\\copied destination.md",
                "notes\\History\\deleted file.md",
            },
            current,
        )
        self.assertEqual(
            {"notes\\History\\original name.md"},
            removed,
        )


if __name__ == "__main__":
    unittest.main()
