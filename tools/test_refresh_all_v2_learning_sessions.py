"""Targeted tests for the reusable learner-v2 refreshed migration pipeline."""

from __future__ import annotations

import copy
import inspect
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import refresh_all_v2_learning_sessions as refresh
import validate_v2_export as validator


SAMPLE = """---
title: Test Topic
topic_key: test-topic
---
# Test Topic

## BASIC LEARNING SESSION

### Source audit, syllabus boundary and package counts

This publication metadata must remain outside the numbered teaching sequence.

### 01. First doctrine

> **ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM:** The first doctrine treats direct evidence as the controlling standard.

The first doctrine is a model of disciplined evidence because it rejects an unsupported universal claim.

**Mains route:** Define the evidentiary standard, explain the mechanism and qualify the conclusion.

### 02. Second institution

The Regulation Act 1900 creates divided authority between a supervising body and an operating body.

The institutional consequence is controlled autonomy rather than complete independence.

## BASIC MCQS / REMEDIATION

### Objective checks

#### Q1
Which is correct?
- A. Correct one
- B. Wrong two
- C. Wrong three
- D. Wrong four
**Answer: A.** Explanation.

#### Q2
Which is correct?
- A. Wrong one
- B. Correct two
- C. Wrong three
- D. Wrong four
**Answer: B.** Explanation.

#### Q3
Which is correct?
- A. Wrong one
- B. Wrong two
- C. Correct three
- D. Wrong four
**Answer: C.** Explanation.

#### Q4
Which is correct?
- A. Wrong one
- B. Wrong two
- C. Wrong three
- D. Correct four
**Answer: D.** Explanation.

#### Q5
Which is correct?
- A. Correct five
- B. Wrong two
- C. Wrong three
- D. Wrong four
**Answer: A.** Explanation.

#### Q6
Which is correct?
- A. Wrong one
- B. Correct six
- C. Wrong three
- D. Wrong four
**Answer: B.** Explanation.

#### Q7
Which is correct?
- A. Wrong one
- B. Wrong two
- C. Correct seven
- D. Wrong four
**Answer: C.** Explanation.

#### Q8
Which is correct?
- A. Wrong one
- B. Wrong two
- C. Wrong three
- D. Correct eight
**Answer: D.** Explanation.

## PYQS AND ANSWER PRACTICE

### Solved practice

Preserved answer practice.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

### Advanced refinement

Optional enrichment cannot be the only location of a core concept.

## CONSOLIDATED REGISTER NOTES

### Compressed register

Final revision.
"""

BIG_BANG_BODY = """
**Classification: CORE PRELIMS + CORE MAINS**

![Universe, stars and Solar-System formation](assets/02_cosmos-stars-solar-system.png)

*The visual connects cosmological origin to star and planetary formation without confusing their
different scales.*

[FACT] Current NASA cosmology places the observable universe's history at about **13.8 billion
years**. The exam-safe formulation is an **extremely hot, dense early state followed by expansion
and cooling**. “Explosion” is misleading if it suggests matter flying from a centre into empty
space.

| Evidence | What it shows | Safe limitation |
|---|---|---|
| Expansion/redshift | Distant-galaxy light is redshifted; large-scale space is expanding | It is not ordinary motion from one terrestrial centre |
| Cosmic microwave background (CMB) | Relic radiation from the epoch when the universe became transparent | It is not light from the first stars |
| Light-element abundance | Early-universe nucleosynthesis predicts much hydrogen/helium and traces of light elements | Avoid unsupported percentage precision |

> **UPSC trap:** Big Bang ≠ a bomb exploding at one point in pre-existing empty space.

> **ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM** The Big Bang denotes the expansion and cooling of an extremely hot, dense early universe about 13.8 billion years ago, not an explosion from one point into pre-existing empty space.
"""


def fake_topic() -> refresh.Topic:
    return refresh.Topic(
        key="test-topic",
        subject="Test-Subject",
        section="Test-Section",
        topic_folder="Test-Topic",
        title="Test Topic",
        generation=2,
        record_id="test-topic:learner-v2:g2",
        markdown=ROOT / "AGENTS.md",
        main_pdf=ROOT / "AGENTS.md",
        workbook=ROOT / "AGENTS.md",
        source_record={},
    )


def authored_topic(topic_key: str) -> refresh.Topic:
    spec = refresh.manual_ascii_topic_spec(topic_key)
    if spec is None:
        raise AssertionError(f"Missing test manual spec: {topic_key}")
    topic = fake_topic()
    return refresh.Topic(
        key=topic_key,
        subject=topic.subject,
        section=topic.section,
        topic_folder=topic_key,
        title=spec.title,
        generation=topic.generation,
        record_id=f"{topic_key}:learner-v2:g2",
        markdown=topic.markdown,
        main_pdf=topic.main_pdf,
        workbook=topic.workbook,
        source_record={},
    )


class InventoryTests(unittest.TestCase):
    def test_latest_validated_inventory_and_pilot_are_deterministic(self) -> None:
        tracker = refresh.load_tracker()
        topics = refresh.latest_validated_topics(
            tracker,
            refresh.load_overrides(),
        )
        expected = {
            str(record["topic_key"])
            for record in tracker["exports"]
            if isinstance(record, dict)
            and record.get("variant") == refresh.V2_VARIANT
            and isinstance(record.get("validation"), dict)
            and record["validation"].get("state") == "passed"
        }
        self.assertEqual(expected, {topic.key for topic in topics})
        self.assertEqual(
            [
                "philosophy-paper-ii-philosophy-of-religion-01",
                "polity-01",
                "ancient-indian-history-01",
            ],
            [topic.key for topic in refresh.pilot_topics(topics)],
        )

    def test_generation_is_one_above_every_existing_variant_generation(self) -> None:
        tracker = {
            "exports": [
                {"topic_key": "x", "variant": "learner-v2", "generation": 2},
                {"topic_key": "x", "variant": "learner-v2", "generation": 5},
                {"topic_key": "x", "variant": "legacy-v1", "generation": 20},
            ]
        }
        self.assertEqual(6, refresh.next_generation(tracker, "x"))

    def test_new_topic_generation_continues_after_legacy_identity(self) -> None:
        tracker = {
            "exports": [
                {"topic_key": "x", "variant": "legacy-v1", "generation": 1},
                {"topic_key": "other", "variant": "learner-v2", "generation": 9},
            ]
        }
        self.assertEqual(2, refresh.next_new_topic_generation(tracker, "x"))

    def test_learner_first_topic_starts_at_generation_one(self) -> None:
        self.assertEqual(
            1,
            refresh.next_new_topic_generation({"exports": []}, "learner-first"),
        )

    def test_learner_first_record_has_no_synthetic_predecessor(self) -> None:
        topic = refresh.Topic(
            key="learner-first",
            subject="Test-Subject",
            section="Test-Section",
            topic_folder="learner-first",
            title="Learner First",
            generation=0,
            record_id="",
            markdown=ROOT / "AGENTS.md",
            main_pdf=ROOT / "AGENTS.md",
            workbook=ROOT / "AGENTS.md",
            source_record={},
        )
        paths = refresh.output_paths(
            topic,
            1,
            generation_date="2026-08-30",
        )
        record = refresh.new_topic_record_for(
            topic,
            1,
            "2026-08-30",
            paths,
            {},
            {},
            {"command": "Generate learner-first topic"},
            {},
        )
        self.assertIsNone(record["supersedes"])
        self.assertIsNone(record["provenance"]["superseded_v1"])

    def test_required_graphical_pilots_are_fixed_and_tracker_safe(self) -> None:
        self.assertEqual(
            (
                "geography-04",
                "philosophy-paper-i-indian-philosophy-02",
                "polity-07",
                "ancient-indian-history-06",
            ),
            refresh.GRAPHICAL_PILOT_KEYS,
        )
        source = inspect.getsource(refresh.flowchart_package)
        self.assertIn("graphical.render_package", source)
        self.assertNotIn("visual.render_master", source)


class SessionContractTests(unittest.TestCase):
    def test_generic_sessionizer_preserves_meta_and_adds_complete_contract(self) -> None:
        transformed = refresh.sessionize(
            SAMPLE,
            fake_topic(),
            {},
        )
        self.assertIn("### Source audit, syllabus boundary", transformed)
        self.assertIn("### SESSION 1 — FIRST DOCTRINE", transformed)
        self.assertIn("### SESSION 2 — SECOND INSTITUTION", transformed)
        self.assertEqual(
            2,
            transformed.count("#### DEFINITION / WHAT THIS IS CALLED"),
        )
        self.assertEqual(2, transformed.count("#### CLOSING RECALL FLOW"))

    def test_explicit_session_keeps_nested_content_in_major_session(self) -> None:
        source = SAMPLE.replace(
            "### 01. First doctrine",
            "### SESSION 1 — FIRST DOCTRINE",
        ).replace(
            "### 02. Second institution",
            "### Nested comparison",
        )
        transformed = refresh.sessionize(source, fake_topic(), {})
        self.assertIn("### SESSION 1 — FIRST DOCTRINE", transformed)
        self.assertIn("#### Nested comparison", transformed)

    def test_ascii_master_is_added_inside_final_register(self) -> None:
        topic = authored_topic("geography-01")
        transformed = refresh.sessionize(SAMPLE, topic, {})
        transformed, _ = refresh.rebalance_mcqs(transformed, "test-topic")
        transformed, ascii_text = refresh.ensure_ascii_master(
            transformed,
            topic,
            require_manual=True,
        )
        self.assertIn("COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM", transformed)
        self.assertTrue(
            ascii_text.startswith("#### ASCII MASTER FLOW — PANEL 1/8:")
        )
        self.assertEqual(8, ascii_text.count("```ascii-master"))
        self.assertLess(
            transformed.index("## CONSOLIDATED REGISTER NOTES"),
            transformed.index("### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM"),
        )

    def test_linear_session_card_dump_is_rejected(self) -> None:
        old = """#### ASCII MASTER FLOW — PANEL 1/6: Linear dump

```ascii-master
Test Topic — COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM
START / CENTRAL QUESTION
        |
        v
+-- SESSION 01: FIRST DOCTRINE
|   DEFINITION / TERMS : first doctrine
|   MECHANISM / ARGUMENT: evidence
|   CONSEQUENCE / CONTRAST: conclusion
|   TRAP / ANSWER-USE: avoid error
|   EXAM OPENING: opening
+--
```
"""
        errors = validator.validate_ascii_master_text(old)
        self.assertTrue(
            any("+-- SESSION linear dump" in error for error in errors),
            errors,
        )

    def test_notions_style_reference_is_accepted(self) -> None:
        reference = (
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Philosophy"
            / "Philosophy-of-Religion"
            / "learning-sessions"
            / "Notions-of-God"
            / "Notions-of-God_Uncompressed-Complete-Learning-Session_2026-08-22.md"
        )
        fragment = refresh.ascii_master.extract_reference_fragment(
            reference.read_text(encoding="utf-8")
        )
        self.assertEqual([], validator.validate_ascii_master_text(fragment))

    def test_duplicate_panel_titles_are_rejected(self) -> None:
        topic = authored_topic("geography-01")
        transformed = refresh.sessionize(SAMPLE, topic, {})
        transformed, _ = refresh.rebalance_mcqs(transformed, "test-topic")
        transformed, fragment = refresh.ensure_ascii_master(
            transformed,
            topic,
            require_manual=True,
        )
        blocks = refresh.ascii_master.panel_blocks(fragment)
        duplicate = fragment.replace(blocks[1][2], blocks[0][2], 1)
        errors = validator.validate_ascii_master_text(duplicate)
        self.assertTrue(any("titles must be unique" in error for error in errors))

    def test_big_bang_metadata_never_enters_semantic_aids(self) -> None:
        contract = refresh.semantic_contract(
            "Big Bang: hot dense beginning, expansion and evidence",
            BIG_BANG_BODY,
        )
        self.assertTrue(contract["plain"].startswith("The Big Bang denotes"))
        self.assertIn("hot, dense early state", contract["technical"])
        self.assertEqual(contract["plain"], contract["opening"])
        self.assertIn("Cosmic microwave background (CMB)", contract["keywords"])
        self.assertIn("Expansion/redshift", contract["keywords"])
        self.assertGreaterEqual(len(contract["keywords"]), 4)
        self.assertLessEqual(len(contract["keywords"]), 8)
        self.assertNotIn("Classification: CORE", str(contract))
        self.assertNotIn(". The exam-safe", str(contract))
        self.assertNotIn("UPSC trap", contract["keywords"])
        self.assertNotEqual(contract["opening"], contract["how"])
        self.assertIn("connect", contract["how"])

        rendered = refresh.session_block(
            2,
            "Big Bang: hot dense beginning, expansion and evidence",
            BIG_BANG_BODY,
        )
        self.assertIn(
            "**Classification: CORE PRELIMS + CORE MAINS**",
            rendered,
        )
        aid_prefix = rendered.split(
            "**Classification: CORE PRELIMS + CORE MAINS**",
            1,
        )[0]
        self.assertNotIn("Classification: CORE", aid_prefix)

    def test_legitimate_conceptual_classification_is_not_globally_removed(self) -> None:
        body = """
Classification of volcanoes is based on form, eruption style and activity status.
**Shield volcanoes**, **stratovolcanoes**, **lava domes** and **activity status**
describe different volcanic groupings.
> **ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM:** A volcanic classification is useful only when its criterion is stated explicitly.
"""
        cleaned = refresh.clean_semantic_source(body)
        self.assertIn("Classification of volcanoes is based", cleaned)
        contract = refresh.semantic_contract(
            "Classification of volcanoes",
            body,
        )
        self.assertIn("Classification of volcanoes", contract["plain"])


class ManualAsciiSpecTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spec_dir = (
            ROOT
            / "upsc-ai-kit"
            / "manifests"
            / "retrofits"
            / "ascii-panel-specs"
        )

    def test_all_manual_schemas_load_without_rewriting(self) -> None:
        expected = {
            "ancient-indian-history-2026-08-23.json": (11, 102),
            "ancient-indian-history-2026-08-29-sequential.json": (5, 60),
            "ancient-indian-history-17-21-2026-08-29-sequential.json": (5, 60),
            "ancient-indian-history-22-23-2026-08-30-sequential.json": (2, 24),
            "ancient-indian-history-24-25-2026-08-30-sequential.json": (2, 24),
            "ancient-indian-history-26-27-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-01-02-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-03-04-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-05-06-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-07-08-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-09-10-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-11-12-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-13-14-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-15-16-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-17-18-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-19-20-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-21-22-2026-08-30-sequential.json": (2, 24),
            "medieval-indian-history-23-25-2026-08-30-sequential.json": (3, 36),
            "modern-indian-history-01-02-2026-08-30-sequential.json": (2, 24),
            "modern-indian-history-03-04-2026-08-30-sequential.json": (2, 24),
            "modern-indian-history-05-06-2026-08-30-sequential.json": (2, 24),
            "modern-indian-history-07-08-2026-08-30-sequential.json": (2, 24),
            "modern-indian-history-09-13-2026-08-30-sequential.json": (5, 60),
            "modern-indian-history-14-15-2026-08-31-sequential.json": (2, 24),
            "modern-indian-history-16-17-2026-08-31-sequential.json": (2, 24),
            "modern-indian-history-18-19-2026-08-31-sequential.json": (2, 24),
            "modern-indian-history-20-21-2026-08-31-sequential.json": (2, 24),
            "modern-indian-history-22-23-2026-08-31-sequential.json": (2, 24),
            "modern-indian-history-24-25-2026-08-31-sequential.json": (2, 24),
            "world-history-01-02-2026-09-01-sequential.json": (2, 24),
            "world-history-03-04-2026-09-01-sequential.json": (2, 24),
            "world-history-05-2026-09-01-sequential.json": (1, 12),
            "world-history-06-07-2026-09-01-sequential.json": (2, 24),
            "world-history-08-09-2026-09-01-sequential.json": (2, 24),
            "world-history-10-2026-09-01-sequential.json": (1, 12),
            "world-history-11-12-2026-09-01-sequential.json": (2, 24),
            "world-history-13-14-2026-09-01-sequential.json": (2, 24),
            "world-history-15-2026-09-01-sequential.json": (1, 12),
            "world-history-16-17-2026-09-01-sequential.json": (2, 24),
            "world-history-18-2026-09-01-sequential.json": (1, 12),
            "world-history-19-20-2026-09-01-sequential.json": (2, 24),
            "world-history-21-2026-09-01-sequential.json": (1, 12),
            "indian-art-and-culture-01-02-2026-09-01-sequential.json": (2, 24),
            "indian-art-and-culture-03-04-2026-09-01-sequential.json": (2, 24),
            "indian-art-and-culture-05-2026-09-01-sequential.json": (1, 12),
            "indian-art-and-culture-06-07-2026-09-01-sequential.json": (2, 24),
            "indian-art-and-culture-08-09-2026-09-01-sequential.json": (2, 24),
            "indian-art-and-culture-10-2026-09-01-sequential.json": (1, 12),
            "indian-art-and-culture-11-12-2026-09-01-sequential.json": (2, 24),
            "indian-art-and-culture-13-14-2026-09-01-sequential.json": (2, 24),
            "indian-art-and-culture-15-2026-09-01-sequential.json": (1, 12),
            "geography-05-06-2026-09-01-sequential.json": (2, 24),
            "geography-07-08-2026-09-01-sequential.json": (2, 24),
            "geography-09-2026-09-01-sequential.json": (1, 12),
            "geography-10-11-2026-09-01-sequential.json": (2, 24),
            "geography-12-13-2026-09-01-sequential.json": (2, 24),
            "geography-14-2026-09-01-sequential.json": (1, 12),
            "geography-15-16-2026-09-01-sequential.json": (2, 24),
            "geography-17-18-2026-09-01-sequential.json": (2, 24),
            "geography-19-2026-09-01-sequential.json": (1, 12),
            "geography-31-2026-09-01-sequential.json": (1, 12),
            "geography-33-2026-09-01-sequential.json": (1, 12),
            "geography-34-2026-09-01-sequential.json": (1, 12),
            "geography-35-2026-09-01-sequential.json": (1, 12),
            "geography-36-2026-09-01-sequential.json": (1, 12),
            "geography-37-2026-09-01-sequential.json": (1, 12),
            "indian-society-01-2026-09-02-sequential.json": (1, 12),
            "indian-society-02-2026-09-02-sequential.json": (1, 12),
            "indian-society-03-2026-09-02-sequential.json": (1, 12),
            "indian-society-04-2026-09-02-sequential.json": (1, 12),
            "indian-society-05-2026-09-02-sequential.json": (1, 12),
            "indian-society-06-2026-09-02-sequential.json": (1, 12),
            "indian-society-07-2026-09-02-sequential.json": (1, 12),
            "indian-society-08-2026-09-02-sequential.json": (1, 12),
            "indian-society-09-2026-09-02-sequential.json": (1, 12),
            "indian-society-10-2026-09-02-sequential.json": (1, 12),
            "geography-2026-08-23.json": (7, 56),
            "philosophy-2026-08-23.json": (15, 122),
            "polity-2026-08-23.json": (7, 76),
            "polity-2026-08-24-sequential-batch.json": (5, 56),
            "polity-13-2026-08-24-sequential.json": (1, 12),
            "polity-14-2026-08-24-sequential.json": (1, 12),
            "polity-15-2026-08-24-sequential.json": (1, 12),
            "polity-16-2026-08-24-sequential.json": (1, 12),
            "polity-17-2026-08-24-sequential.json": (1, 12),
            "polity-18-2026-08-24-sequential.json": (1, 12),
            "polity-19-2026-08-24-sequential.json": (1, 12),
            "polity-20-2026-08-24-sequential.json": (1, 12),
            "polity-21-2026-08-24-sequential.json": (1, 12),
            "polity-22-2026-08-24-sequential.json": (1, 12),
        }
        for filename, (topic_count, panel_count) in expected.items():
            specs = refresh.ascii_master.normalize_manual_spec_file(
                self.spec_dir / filename
            )
            self.assertEqual(topic_count, len(specs), filename)
            self.assertEqual(
                panel_count,
                sum(len(spec.panels) for spec in specs.values()),
                filename,
            )

    def test_manual_coverage_matches_registered_authored_topics(self) -> None:
        specs = refresh.manual_ascii_specs()
        required = [
            self.spec_dir / filename
            for filename in refresh.ascii_master.MANUAL_SPEC_FILENAMES
        ]
        required_names = {path.name.casefold() for path in required}
        optional = [
            path
            for path in sorted(self.spec_dir.glob("polity-*-sequential.json"))
            if path.name.casefold() not in required_names
        ]
        expected: dict[str, object] = {}
        for path in [*required, *optional]:
            for topic_key, spec in (
                refresh.ascii_master.normalize_manual_spec_file(path).items()
            ):
                self.assertNotIn(topic_key, expected, topic_key)
                expected[topic_key] = spec
        self.assertEqual(set(expected), set(specs))
        self.assertEqual(
            sum(len(spec.panels) for spec in expected.values()),
            sum(len(spec.panels) for spec in specs.values()),
        )
        self.assertEqual(
            [],
            refresh.ascii_master.manual_spec_integrity_errors(ROOT, specs),
        )

    def test_embedded_panels_equal_manual_spec_exactly(self) -> None:
        topic = authored_topic("geography-04")
        transformed = refresh.sessionize(SAMPLE, topic, {})
        transformed, _ = refresh.rebalance_mcqs(transformed, topic.key)
        transformed, fragment = refresh.ensure_ascii_master(
            transformed,
            topic,
            require_manual=True,
        )
        embedded = re.search(
            r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
            transformed,
        )
        self.assertIsNotNone(embedded)
        expected = refresh.ascii_master.build_manual_fragment(
            refresh.manual_ascii_topic_spec(topic.key)
        )
        self.assertEqual(
            refresh.ascii_master.normalized_panel_text(expected),
            refresh.ascii_master.normalized_panel_text(embedded.group(1)),
        )
        self.assertEqual([], validator.validate_ascii_master_text(
            fragment,
            topic_key=topic.key,
        ))

    def test_standalone_plain_text_equals_manual_spec_exactly(self) -> None:
        spec = refresh.manual_ascii_topic_spec(
            "philosophy-paper-i-indian-philosophy-02"
        )
        fragment = refresh.ascii_master.build_manual_fragment(spec)
        standalone = refresh.ascii_master.standalone_panel_text(fragment)
        self.assertNotIn("```", standalone)
        self.assertEqual(
            refresh.ascii_master.normalized_panel_text(fragment),
            refresh.ascii_master.normalized_panel_text(standalone),
        )
        self.assertEqual(
            [],
            validator.validate_ascii_master_text(
                fragment,
                topic_key=spec.topic_key,
                standalone_text=standalone,
            ),
        )
        broken = standalone.replace(spec.panels[0].body.splitlines()[0], "BROKEN", 1)
        errors = validator.validate_ascii_master_text(
            fragment,
            topic_key=spec.topic_key,
            standalone_text=broken,
        )
        self.assertTrue(any("manual spec" in error for error in errors), errors)

    def test_flawed_geography_04_generic_example_is_rejected(self) -> None:
        spec = refresh.manual_ascii_topic_spec("geography-04")
        fragment = refresh.ascii_master.build_manual_fragment(spec)
        flawed = "\n".join(
            [
                "WEATHERING AND MASS MOVEMENT — CONCEPTUAL ATLAS",
                "How should the complete structure of weathering",
                "be defined, related, compared and evaluated?",
                "          |",
                "AXIS 1: How should the complete structure be grouped?",
                "KEY TERMS: ZONE / LAYER A",
                "          |",
                "CAUSE / CONDITION 1: unrelated grouping…",
                "KEY TERMS: repeated scaffold",
                "          v",
                "TRUNCATED GENERIC RESULT",
            ]
        )
        broken = fragment.replace(spec.panels[0].body, flawed, 1)
        errors = validator.validate_ascii_master_text(
            broken,
            topic_key=spec.topic_key,
        )
        joined = "\n".join(errors)
        self.assertIn("generic central wording", joined)
        self.assertIn("placeholder", joined)
        self.assertIn("truncation ellipses", joined)
        self.assertIn("KEY TERMS", joined)
        self.assertIn("manual spec", joined)

    def test_representative_authored_specs_are_accepted(self) -> None:
        keys = (
            "geography-01",
            "philosophy-paper-i-indian-philosophy-02",
            "polity-01",
            "ancient-indian-history-06",
            "ancient-indian-history-10",
        )
        for key in keys:
            spec = refresh.manual_ascii_topic_spec(key)
            fragment = refresh.ascii_master.build_manual_fragment(spec)
            standalone = refresh.ascii_master.standalone_panel_text(fragment)
            self.assertEqual(
                [],
                validator.validate_ascii_master_text(
                    fragment,
                    topic_key=key,
                    standalone_text=standalone,
                ),
                key,
            )


class McqTests(unittest.TestCase):
    def test_all_topic_keys_use_required_abcd_cycle(self) -> None:
        first = refresh.target_answer_keys("test-topic", 44)
        second = refresh.target_answer_keys("test-topic", 44)
        self.assertEqual(first, second)
        self.assertEqual(list("ABCD") * 11, first)

    def test_sequential_polity_keys_use_required_abcd_cycle(self) -> None:
        keys = refresh.target_answer_keys("polity-13", 10)
        self.assertEqual(list("ABCDABCDAB"), keys)
        transformed, audit = refresh.rebalance_mcqs(SAMPLE, "polity-13")
        self.assertEqual(list("ABCDABCD"), validator.extract_mcq_answer_keys(transformed))
        self.assertTrue(audit["all_correct_option_texts_preserved"])
        self.assertEqual(
            [],
            validator.answer_key_pattern_errors(
                transformed,
                topic_key="polity-13",
            ),
        )

    def test_rebalancing_preserves_correct_option_content(self) -> None:
        transformed, audit = refresh.rebalance_mcqs(SAMPLE, "test-topic")
        self.assertEqual(8, audit["question_count"])
        self.assertTrue(audit["all_correct_option_texts_preserved"])
        self.assertEqual(
            refresh.target_answer_keys("test-topic", 8),
            validator.extract_mcq_answer_keys(transformed),
        )
        self.assertEqual(
            [],
            validator.answer_key_pattern_errors(
                transformed,
                topic_key="test-topic",
            ),
        )

    def test_rotation_note_does_not_gain_double_punctuation(self) -> None:
        source = SAMPLE.replace(
            "## BASIC MCQS / REMEDIATION",
            "## BASIC MCQS / REMEDIATION\n\n"
            "> Correct options rotate strictly A -> B -> C -> D, repeated twice.",
        )
        transformed, _ = refresh.rebalance_mcqs(source, "test-topic")
        self.assertIn(
            "Answer placement follows strict A → B → C → D rotation, repeated twice.",
            transformed,
        )
        self.assertNotIn("rotation.,", transformed)

    def test_rotation_note_repairs_mutated_letter_sequence(self) -> None:
        source = SAMPLE.replace(
            "## BASIC MCQS / REMEDIATION",
            "## BASIC MCQS / REMEDIATION\n\n"
            "> Correct options rotate strictly A -> A -> B -> D, repeated twice.",
        )
        transformed, _ = refresh.rebalance_mcqs(source, "test-topic")
        self.assertIn(
            "Answer placement follows strict A → B → C → D rotation, repeated twice.",
            transformed,
        )
        self.assertNotIn("A → A → B → D", transformed)

    def test_validator_extracts_bold_answers_with_option_text(self) -> None:
        markdown = """## BASIC MCQS / REMEDIATION
**Answer: (a) 1, 2 and 3.**
**Answer: (b) 2 only.**
**Answer: (c) Both statements are correct.**
**Answer: (d) Neither statement is correct.**
## PYQS AND ANSWER PRACTICE
"""
        self.assertEqual(
            list("ABCD"),
            validator.extract_mcq_answer_keys(markdown),
        )
        self.assertEqual(
            [],
            validator.answer_key_pattern_errors(markdown),
        )

    def test_option_relabelling_does_not_rewrite_ordinary_prose(self) -> None:
        line = "A theory may compare option B without making A an option reference."
        mapping = {"A": "D", "B": "C", "C": "B", "D": "A"}
        self.assertEqual(
            "A theory may compare option C without making A an option reference.",
            refresh.update_explanation_labels(line, mapping),
        )


class ValidatorTests(unittest.TestCase):
    def test_refreshed_paths_are_accepted(self) -> None:
        source = (
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Learner-v2-Refreshed"
            / "Polity"
            / "Subject-Wide-Syllabus"
            / "learning-sessions"
            / "Historical-Background"
            / "Historical-Background_Complete-Learning-Session_2026-08-22.md"
        )
        main = (
            ROOT
            / "notes"
            / "Learner-v2-Refreshed"
            / "Polity"
            / "Subject-Wide-Syllabus"
            / "learning-sessions"
            / "Historical-Background"
            / "Historical-Background_Complete-Learning-Session_2026-08-22.pdf"
        )
        workbook = main.with_name(
            "Historical-Background_Solved-Practice-Workbook_2026-08-22.pdf"
        )
        self.assertEqual(
            [],
            validator.validate_v2_paths(
                ROOT,
                source,
                main,
                "polity-01",
                "main",
            ),
        )
        self.assertEqual(
            [],
            validator.validate_v2_paths(
                ROOT,
                source,
                workbook,
                "polity-01",
                "workbook",
            ),
        )

    def test_full_refreshed_markdown_contract_passes(self) -> None:
        topic = authored_topic("geography-01")
        transformed = refresh.sessionize(SAMPLE, topic, {})
        transformed, _ = refresh.rebalance_mcqs(transformed, "test-topic")
        transformed, _ = refresh.ensure_ascii_master(
            transformed,
            topic,
            require_manual=True,
        )
        self.assertEqual(
            [],
            validator.validate_refreshed_markdown_text(
                transformed,
                topic_key=topic.key,
            ),
        )

    def test_workbook_extractor_replaces_learning_session_title(self) -> None:
        topic = authored_topic("geography-01")
        transformed = refresh.sessionize(SAMPLE, topic, {})
        transformed = re.sub(
            r"(?m)^# .+$",
            "# Test Topic — Complete Learning Session",
            transformed,
            count=1,
        )
        workbook = validator.extract_v2_workbook_markdown(transformed)
        self.assertEqual(
            "# Test Topic — Solved Practice Workbook",
            workbook.splitlines()[0],
        )

    def test_explicit_mcq_answer_text_must_match_selected_option(self) -> None:
        broken = SAMPLE.replace(
            "**Answer: C.** Explanation.",
            "**Answer: C. Wrong four**",
            1,
        )
        self.assertEqual(
            [
                "MCQ 3 answer text does not match option C: "
                "'Wrong four' != 'Correct three'."
            ],
            validator.mcq_answer_text_errors(broken),
        )

    def test_validator_rejects_exact_old_big_bang_malformation(self) -> None:
        transformed = refresh.sessionize(SAMPLE, fake_topic(), {})
        transformed, _ = refresh.rebalance_mcqs(transformed, "test-topic")
        transformed, _ = refresh.ensure_ascii_master(
            transformed,
            fake_topic(),
        )
        malformed = """#### DEFINITION / WHAT THIS IS CALLED

**Plain-language definition:** Classification: CORE PRELIMS + CORE MAINS

**Technical definition:** The exam-safe formulation is an

#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM

> Classification: CORE PRELIMS + CORE MAINS

#### MUST-WRITE KEYWORDS

- **Classification: CORE PRELIMS + CORE MAINS**
- **. The exam-safe formulation is an**
- **UPSC trap**
- **Big Bang: hot dense beginning, expansion and evidence**

**How to use them:** Classification: CORE PRELIMS + CORE MAINS
"""
        broken = re.sub(
            r"(?ims)####\s+DEFINITION / WHAT THIS IS CALLED\s*.*?"
            r"^\*\*How to use them:\*\*.*?$",
            malformed.strip(),
            transformed,
            count=1,
        )
        errors = validator.validate_refreshed_markdown_text(
            broken,
            topic_key="test-topic",
        )
        joined = "\n".join(errors)
        self.assertIn("editorial classification metadata", joined)
        self.assertIn("malformed '. The' sentence fragment", joined)
        self.assertIn("generic or bare label", joined)


class DeepContentQualityTests(unittest.TestCase):
    def complete_sample(self) -> str:
        transformed = refresh.sessionize(SAMPLE, fake_topic(), {})
        transformed, _ = refresh.rebalance_mcqs(transformed, "test-topic")
        transformed, _ = refresh.ensure_ascii_master(
            transformed,
            fake_topic(),
        )
        return transformed

    def reasons(self, markdown: str, *, topic_key: str = "test-topic") -> str:
        audit = validator.deep_content_quality_audit_text(
            markdown,
            topic_key=topic_key,
        )
        return "\n".join(str(item["reason"]) for item in audit["defects"])

    def test_caption_as_definition_is_rejected(self) -> None:
        broken = self.complete_sample().replace(
            "**Plain-language definition:** The first doctrine",
            "**Plain-language definition:** Caption: Original deterministic schematic prepared for this package; labels are source-checked. The first doctrine",
            1,
        )
        self.assertIn("caption", self.reasons(broken))

    def test_news_as_definition_is_rejected(self) -> None:
        broken = re.sub(
            r"(\*\*Plain-language definition:\*\*)[^\n]+",
            (
                r"\1 Religion News Service reported on 26 May 2026 that "
                "researchers presented an AI ethics study in Athens."
            ),
            self.complete_sample(),
            count=1,
        )
        self.assertIn("dated news or event", self.reasons(broken))

    def test_consequence_as_definition_is_rejected(self) -> None:
        broken = re.sub(
            r"(\*\*Plain-language definition:\*\*)[^\n]+",
            (
                r"\1 A giant star possesses more fuel but consumes it much "
                "faster; therefore larger means longer-lived is usually false."
            ),
            self.complete_sample(),
            count=1,
        )
        self.assertIn(
            "plain definition is merely an example, comparison or consequence",
            self.reasons(broken),
        )

    def test_identical_closure_nodes_are_rejected(self) -> None:
        same = "The first doctrine uses direct evidence as its controlling standard."
        broken = self.complete_sample()
        for label in (
            "MECHANISM / ARGUMENT",
            "CONSEQUENCE / CONTRAST",
            "UPSC TRAP / ANSWER-USE",
            "ANSWER-GRABBING FORMULATION",
        ):
            broken = re.sub(
                rf"({re.escape(label)}:)[^\n]+",
                rf"\1 {same}",
                broken,
                count=1,
            )
        self.assertIn("closure nodes must be distinct", self.reasons(broken))

    def test_metadata_keywords_are_rejected(self) -> None:
        replacement = """#### MUST-WRITE KEYWORDS

- **February**
- **2026**
- **Do**
- **Search finding**

**How to use them:** Connect February with 2026, then use Do and Search finding."""
        broken = re.sub(
            r"(?ims)^####\s+MUST-WRITE KEYWORDS\s*$.*?"
            r"^\*\*How to use them:\*\*[^\n]*$",
            replacement,
            self.complete_sample(),
            count=1,
        )
        reasons = self.reasons(broken)
        self.assertIn("month or year alone", reasons)
        self.assertIn("generic or bare label", reasons)

    def test_undersegmented_philosophy_package_is_rejected(self) -> None:
        reasons = self.reasons(
            self.complete_sample(),
            topic_key="philosophy-paper-i-test",
        )
        self.assertIn(
            "fewer than seven searchable major sessions",
            reasons,
        )

    def test_current_anchor_remains_body_but_not_definition(self) -> None:
        body = """
✅ Fact: Religion News Service reported on 26 May 2026 that researchers discussed multi-faith AI bias.

Reason, revelation and faith are distinct grounds on which religious belief may claim authority.
Reason offers publicly assessable inference, revelation claims disclosure, and faith adds committed trust.
The three sources can cooperate, but none automatically validates every religious claim.
> **UPSC trap:** Do not equate faith with evidence-free belief.
"""
        rendered = refresh.session_block(
            1,
            "Reason, revelation and faith",
            body,
        )
        self.assertIn("Religion News Service reported", rendered)
        aid_prefix = rendered.split("✅ Fact:", 1)[0]
        self.assertNotIn("Religion News Service", aid_prefix)
        self.assertIn("distinct grounds", aid_prefix)


class FinalizeTests(unittest.TestCase):
    def test_upsert_refuses_existing_identity(self) -> None:
        tracker = {
            "schema_version": 2,
            "exports": [
                {
                    "topic_key": "x",
                    "variant": "learner-v2",
                    "generation": 2,
                }
            ],
        }
        record = copy.deepcopy(tracker["exports"][0])
        with self.assertRaises(refresh.RefreshError):
            refresh.upsert_records(tracker, [record])


if __name__ == "__main__":
    unittest.main()

