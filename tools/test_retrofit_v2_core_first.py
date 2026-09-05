"""Focused tests for the preservation-safe continuous core-first retrofit."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import retrofit_v2_core_first as retrofit


SOURCE = """# Test

## BASIC LEARNING SESSION

### 1. First doctrinal move

> **ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM:** The first doctrine accepts direct evidence and rejects an unsupported universal claim.

The doctrine is a rule for valid reasoning because the claimed universal relation cannot be tested in every case.

> 🔑 Trap: practical success is not the same as certainty.

### 2. Institutional consequence

The Act creates dual control: one body supervises public affairs whereas another retains commercial management.

The direct consequence is divided authority rather than a transfer of all functions.

## BASIC MCQS / REMEDIATION

### Practice

Question bank.

## PYQS AND ANSWER PRACTICE

### PYQ

Practice.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

### Advanced

Enrichment.

## CONSOLIDATED REGISTER NOTES

Final notes.
"""


METADATA_SOURCE = """# Test

## BASIC LEARNING SESSION

### Source audit, syllabus boundary and package counts

This is production bookkeeping and must stay in the full Markdown.

### Official live-status decision

This is a publication check and must not become a learning stage.

### Answer-line control register

This is a package QA register.

### 01. Corporate rule before constitutional regulation

The Company exercised corporate power before Parliament established statutory control.

### 02. Regulating Act 1773

The Act created a statutory intervention in Company administration.

## BASIC MCQS / REMEDIATION

Practice.

## PYQS AND ANSWER PRACTICE

Practice.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

Advanced.

## CONSOLIDATED REGISTER NOTES

Notes.
"""


H4_FALLBACK_SOURCE = """# Test

## BASIC LEARNING SESSION

### Source-complete coverage ledger

Publication bookkeeping stays in the full Markdown.

### Learning route

Navigation is not a teaching stage.

#### LAYER 2 - CORE UPSC

Navigation shell.

#### 1. Exact doctrine

The doctrine means that direct evidence alone establishes the claim.

It rejects universal inference because an unobserved relation is not proved.

#### 2. Institutional consequence

The Act creates divided control between public supervision and commercial management.

The consequence is dual authority, not a complete transfer of functions.

## BASIC MCQS / REMEDIATION

Practice.
"""


class ClosureFlowTests(unittest.TestCase):
    def test_retrofit_derives_a_complete_closure_per_basic_h3(self) -> None:
        updated, closures = retrofit.retrofit_markdown(SOURCE)
        self.assertEqual(2, len(closures))
        self.assertEqual(2, updated.count("```closure-flow"))
        self.assertIn("KEY TERMS / DEFINITIONS:", updated)
        self.assertIn("MECHANISM / ARGUMENT:", updated)
        self.assertIn("CONSEQUENCE / CONTRAST:", updated)
        self.assertIn("UPSC TRAP / ANSWER-USE:", updated)
        self.assertIn("ANSWER-GRABBING FORMULATION:", updated)
        self.assertEqual([], retrofit.validate_closure_placement(updated))
        self.assertIn("unsupported universal claim", closures[0].answer)

    def test_closures_are_derived_from_source_text(self) -> None:
        _, closures = retrofit.retrofit_markdown(SOURCE)
        source_normalized = retrofit.clean_text(SOURCE)
        for closure in closures:
            for value in (
                closure.terms,
                closure.mechanism,
                closure.consequence,
                closure.trap.removeprefix("Answer-use: "),
                closure.answer,
            ):
                self.assertIn(retrofit.clean_text(value), source_normalized)

    def test_production_metadata_is_preserved_but_never_becomes_a_stage(self) -> None:
        updated, closures = retrofit.retrofit_markdown(METADATA_SOURCE)
        self.assertIn("Source audit, syllabus boundary and package counts", updated)
        self.assertIn("Official live-status decision", updated)
        self.assertIn("Answer-line control register", updated)
        self.assertEqual(
            [
                "Corporate rule before constitutional regulation",
                "Regulating Act 1773",
            ],
            [closure.title for closure in closures],
        )
        self.assertNotIn("SUBTOPIC: Source audit", updated)
        self.assertNotIn("SUBTOPIC: Official live-status decision", updated)
        self.assertNotIn("SUBTOPIC: Answer-line control register", updated)

    def test_meta_classifier_covers_generic_production_vocabulary(self) -> None:
        samples = (
            "Source order and syllabus boundary",
            "Package counts and preservation ledger",
            "Regeneration ledger",
            "Live-source decision and validation",
            "Answer-line control register",
            "GS-II answer architecture",
            "Generation notes, asset paths and manifest routing",
            "Eighth-edition integration: doctrine routing and Part XVI boundary",
            "README / PYQ ledger and ownership record",
            "UPSC relevance and answer-worthiness audit",
            "Source-complete coverage ledger and answer-worthiness labels",
            "Representative source ledger",
            "Contemporary scholarly anchor",
            "Contemporary-anchor discipline",
            "Learning route",
            "Learning road map",
            "Visual gateway — identify the relation before arguing",
            "Metric discipline — never merge the denominators",
            "Master learning roadmap",
        )
        self.assertTrue(all(retrofit.is_production_meta_stage(value) for value in samples))
        self.assertFalse(
            retrofit.is_production_meta_stage(
                "Pitt's India Act 1784 and dual control"
            )
        )
        self.assertFalse(
            retrofit.is_production_meta_stage(
                "Eightfold Path, Middle Way and ethical discipline"
            )
        )
        self.assertFalse(
            retrofit.is_production_meta_stage(
                "Bias, Silence, Preservation and the Ethics of Inference"
            )
        )

    def test_h4_fallback_uses_deep_teaching_units_when_h3_is_scaffolding(self) -> None:
        updated, closures = retrofit.retrofit_markdown(H4_FALLBACK_SOURCE)
        self.assertEqual(
            ["Exact doctrine", "Institutional consequence"],
            [closure.title for closure in closures],
        )
        self.assertNotIn("SUBTOPIC: Learning route", updated)
        self.assertNotIn("SUBTOPIC: LAYER 2", updated)
        self.assertEqual([], retrofit.validate_closure_placement(updated))

    def test_answer_architecture_is_scaffolding(self) -> None:
        self.assertTrue(
            retrofit.is_learner_scaffold_stage("GS-II answer architecture")
        )

    def test_polity_07_places_articles_12_and_13_before_property_transition(self) -> None:
        topic = next(
            item
            for item in retrofit.completed_latest_topics(
                retrofit.load_tracker(), include_retrofits=True, subject="Polity"
            )
            if item.key == "polity-07"
        )
        titles = [
            closure.title
            for closure in retrofit.closure_blocks(
                topic.markdown.read_text(encoding="utf-8")
            )
        ]
        article_12 = next(
            index for index, title in enumerate(titles)
            if title.casefold().startswith("article 12")
        )
        article_13 = next(
            index for index, title in enumerate(titles)
            if title.casefold().startswith("article 13")
        )
        property_transition = next(
            index for index, title in enumerate(titles)
            if title.casefold().startswith("right to property")
        )
        self.assertLess(article_12, property_transition)
        self.assertLess(article_13, property_transition)

    def test_tiling_has_overlap_and_ends_at_master_bottom(self) -> None:
        closures = [
            retrofit.Closure(
                title=f"Stage {number}",
                terms="Exact term is defined by the source.",
                mechanism="A source-described mechanism links cause and result.",
                consequence="The source gives a direct contrast.",
                trap="The source warns against a close-option error.",
                answer="A source-derived answer formulation remains visible.",
            )
            for number in range(1, 8)
        ]
        fonts = {
            "heading": retrofit.font(retrofit.FONT_BOLD, 52),
            "body": retrofit.font(retrofit.FONT_REGULAR, 31),
            "label": retrofit.font(retrofit.FONT_BOLD, 26),
            "answer": retrofit.font(retrofit.FONT_BOLD, 30),
            "stage": retrofit.font(retrofit.FONT_BOLD, 42),
            "tiny": retrofit.font(retrofit.FONT_BOLD, 22),
        }
        probe = retrofit.Image.new("RGB", (retrofit.MASTER_WIDTH, 100), retrofit.NAVY)
        heights = [retrofit.card_height(retrofit.ImageDraw.Draw(probe), item, fonts) for item in closures]
        stages = retrofit.stage_ranges(closures, heights)
        self.assertEqual(1, stages[0][0])
        self.assertEqual(7, stages[-1][0])
        self.assertTrue(all(right[1] > left[2] for left, right in zip(stages, stages[1:])))


if __name__ == "__main__":
    unittest.main()
