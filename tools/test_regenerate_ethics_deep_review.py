"""Focused tests for the Ethics immutable deep-review driver."""

from __future__ import annotations

import unittest
from pathlib import Path

import regenerate_ethics_deep_review as deep


class EthicsDeepReviewTests(unittest.TestCase):
    def test_manifest_order_and_scope_are_exact(self) -> None:
        topics = deep.topics()
        self.assertEqual(23, len(topics))
        self.assertEqual(
            [f"ethics-{number:02d}" for number in range(1, 24)],
            [topic.topic_key for topic in topics],
        )
        self.assertEqual(list(range(1, 24)), [topic.number for topic in topics])

    def test_review_controls_cover_all_twenty_three_topics(self) -> None:
        samples = {
            1: "morality is a person or community's held code",
            2: "not a substitute for enforceable justice",
            3: "manipulation hides or distorts reasons",
            4: "empathy differs from compassion",
            5: "ethical EI remains bounded",
            6: "not interchangeable slogans",
            7: "Golden Mean is not arithmetic",
            8: "care ethics relationships and dependency",
            9: "actual, potential and apparent conflicts",
            10: "different authority",
            11: "actor to a forum",
            12: "CSR expenditure is not a substitute",
            13: "contestability",
            14: "Procedural probity",
            15: "third-party procedure is not a veto",
            16: "code of ethics states aspirational",
            17: "digital-only",
            18: "economy, efficiency, effectiveness and equity",
            19: "analytical labels",
            20: "advice, inquiry, investigation, prosecution",
            21: "resignation is last resort",
            22: "fact-assumption separation",
            23: "not interchangeable morality tales",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_ethics_boundaries_and_approval(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Ethics, morality, values, law, conscience",
            "Thinker discipline",
            "Public-law boundary",
            "Case-study method",
            "source, date, reference period",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_answer_contract_is_exam_executable(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse the ethical conflict and recommend a course of action. Answer in 250 words.
**Model thesis:** Rights, duties and consequences require a safeguarded decision.
**Claim → named evidence → analysis → qualification:**
- A named Indian institution supplies the authority and review route.
**Qualified conclusion:** The decision must be lawful, proportionate and reviewable.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(1, metrics["question_count"])
        for marker in (
            "**Demand decoding:**",
            "**Detailed examiner-grade model answer:**",
            "**Executable exam-length answer / compression plan:**",
            "**Why this earns marks:**",
            "**How to improve this answer:**",
            "Fact/claim and named evidence",
            "timeline",
        ):
            self.assertIn(marker, repaired)

    def test_ascii_panels_have_one_body_unique_titles_and_controls(self) -> None:
        topic = deep.topics()[0]
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        path = deep.repo(record["markdown"])
        spec = deep.build_ascii_spec(
            topic,
            record,
            int(record["generation"]) + 100,
            path.read_text(encoding="utf-8"),
            path,
        )
        panels = spec["topics"][0]["panels"]
        titles = [str(panel["title"]).casefold() for panel in panels]
        self.assertEqual(12, len(panels))
        self.assertEqual(len(titles), len(set(titles)))
        for panel in panels:
            self.assertEqual(
                1, sum(key in panel for key in ("ascii_text", "ascii_lines"))
            )
        rendered = "\n".join(
            "\n".join(panel.get("ascii_lines", []))
            if "ascii_lines" in panel
            else str(panel["ascii_text"])
            for panel in panels
        )
        self.assertIn("MUST REMEMBER:", rendered)
        self.assertIn("CLOSE DISTINCTION:", rendered)
        self.assertIn("EVIDENCE / AUTHORITY / APPLICATION LIMIT:", rendered)

    def test_allocation_rereads_all_live_identity_stores(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation = source[source.index("def allocate(") :]
        allocation = allocation[: allocation.index("def _ethics_latest_ids")]
        self.assertIn("load(SECTION_MANIFEST)", allocation)
        inherited = Path(deep.__file__).with_name(
            "regenerate_ancient_history_deep_review.py"
        ).read_text(encoding="utf-8")
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", inherited)
        self.assertIn("return _base_allocate_iac", allocation)

    def test_inventory_is_exact_utf8_nul_safe_and_path_verified(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn('payload.endswith(b"\\0")', source)
        self.assertIn("decoded != ordered", source)
        self.assertIn("Changed-file inventory contains missing paths", source)
        self.assertNotIn("_git_changed_paths()", source[source.index("def _augment_inventory") :])

    def test_full_library_count_is_dynamic_and_identity_stable(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        republish = source[source.index("def _republish_master_library") :]
        republish = republish[: republish.index("_ethics_inherited_rewrite")]
        self.assertIn("count = len(selected_keys)", republish)
        self.assertIn("after_ids != before_ids", republish)
        self.assertNotIn("319", republish)
        self.assertNotIn("stale unrelated-failure", source)

    def test_only_existing_ethics_generator_test_is_wired(self) -> None:
        self.assertEqual(("test_generate_ethics_topic_v2",), deep.ETHICS_TEST_MODULES)


if __name__ == "__main__":
    unittest.main()
