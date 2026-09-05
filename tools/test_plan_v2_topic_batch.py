"""Tests for deterministic learner-v2 next-topic batch planning."""

from __future__ import annotations

import json
import shutil
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_v2_section_indexes as section_indexes
import plan_v2_topic_batch as batch_planner


class TopicBatchPlannerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = ROOT / "_test_plan_v2_topic_batch"
        shutil.rmtree(self.root, ignore_errors=True)
        manifest_dir = self.root / "upsc-ai-kit" / "manifests" / "v2"
        source_dir = self.root / "upsc-ai-kit" / "knowledge" / "Test-Subject"
        manifest_dir.mkdir(parents=True)
        source_dir.mkdir(parents=True)
        self.topics = []
        manifest_topics = []
        for number in range(1, 13):
            title = (
                "Cārvāka — Sources"
                if number == 2
                else f"Topic {number:02d}"
            )
            source = source_dir / f"{number:02d}_Topic.md"
            source.write_text(f"# {title}\n", encoding="utf-8")
            relative = (
                f"upsc-ai-kit\\knowledge\\Test-Subject\\{number:02d}_Topic.md"
            )
            topic = {
                "subject": {
                    "key": "Test-Subject",
                    "display_name": "Test Subject",
                    "order": 1,
                },
                "section": {
                    "key": "unicode-section",
                    "name": "Unicode — Section",
                    "basis": "test",
                    "order": 1,
                },
                "topic_key": f"test-subject-{number:02d}",
                "topic_order": number,
                "source_number": number,
                "display_title": title,
                "learner_v2_command": (
                    "Generate learner-v2 topic: Test Subject — "
                    f"Unicode — Section — {title}"
                ),
                "source_canonical": relative,
                "discovery_status": "source-ready",
                "tracker_topic_keys": [],
            }
            self.topics.append(topic)
            manifest_topics.append(
                {
                    "topic_key": topic["topic_key"],
                    "display_title": title,
                    "syllabus_mapping": f"Test topic {number}.",
                    "source_canonical": relative,
                    "source_advanced": None,
                    "cross_topic_sources": [],
                    "verified_pyq_sources": [],
                }
            )
        self.catalog = {
            "schema_version": 1,
            "variant": "learner-v2",
            "topics": self.topics,
        }
        manifest = {
            "schema_version": 1,
            "variant": "learner-v2",
            "subject": {
                "key": "Test-Subject",
                "display_name": "Test Subject",
            },
            "section": {
                "key": "unicode-section",
                "name": "Unicode — Section",
                "scope": "official-section",
                "complete_syllabus_section": True,
                "syllabus_sources": [],
            },
            "topics": manifest_topics,
        }
        (manifest_dir / "test-subject--unicode-section.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        self.records = [
            self.make_record(1, "passed"),
            self.make_record(2, "failed"),
        ]

    def tearDown(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def make_record(
        self,
        number: int,
        validation: str,
    ) -> dict[str, object]:
        topic_key = f"test-subject-{number:02d}"
        paths = {
            "markdown": (
                f"upsc-ai-kit\\knowledge\\Test-Subject\\learning-sessions\\v2\\"
                f"unicode-section\\{topic_key}_Learning-Session.md"
            ),
            "main_pdf": (
                f"notes\\Test-Subject\\learning-session-v2\\unicode-section\\notes\\"
                f"{topic_key}_Learning-Session_2026-08-20.pdf"
            ),
            "workbook": (
                f"notes\\Test-Subject\\learning-session-v2\\unicode-section\\workbooks\\"
                f"{topic_key}_Solved-Workbook_2026-08-20.pdf"
            ),
        }
        for relative in paths.values():
            path = section_indexes.repo_path(self.root, relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("test\n", encoding="utf-8")
        return {
            "record_id": f"{topic_key}:learner-v2:g1",
            "topic_key": topic_key,
            "variant": "learner-v2",
            "generation": 1,
            **paths,
            "approved": False,
            "validation": {"state": validation},
        }

    def plan(
        self,
        *,
        count: int = 10,
        regenerate: bool = False,
        records: list[dict[str, object]] | None = None,
    ) -> dict[str, object]:
        return section_indexes.plan_catalog_topic_batch(
            self.root,
            "Test Subject",
            "unicode-section",
            count=count,
            regenerate=regenerate,
            catalog=self.catalog,
            records=self.records if records is None else records,
        )

    def test_completed_excluded_incomplete_included_and_next_ten_order(self) -> None:
        plan = self.plan()
        self.assertEqual(
            [f"test-subject-{number:02d}" for number in range(2, 12)],
            [topic["topic_key"] for topic in plan["topics"]],
        )
        self.assertEqual("incomplete", plan["topics"][0]["state"])
        self.assertTrue(plan["topics"][0]["command"].endswith("— Regenerate"))
        self.assertNotIn("test-subject-01", json.dumps(plan))

    def test_fewer_than_ten_remaining_is_capped(self) -> None:
        records = [self.make_record(number, "passed") for number in range(1, 11)]
        records.append(self.make_record(11, "failed"))
        plan = self.plan(records=records)
        self.assertEqual(
            ["test-subject-11", "test-subject-12"],
            [topic["topic_key"] for topic in plan["topics"]],
        )
        self.assertEqual(2, plan["selected_count"])

    def test_explicit_regenerate_makes_completed_topics_eligible(self) -> None:
        plan = self.plan(count=2, regenerate=True)
        self.assertEqual(
            ["test-subject-01", "test-subject-02"],
            [topic["topic_key"] for topic in plan["topics"]],
        )
        self.assertTrue(plan["batch_command"].endswith("— Regenerate"))

    def test_ambiguous_subject_fails_clearly(self) -> None:
        duplicate = json.loads(json.dumps(self.topics[0]))
        duplicate["subject"]["key"] = "Other-Subject"
        duplicate["topic_key"] = "other-subject-01"
        duplicate["learner_v2_command"] = (
            "Generate learner-v2 topic: Test Subject — Unicode — Section — Other"
        )
        with self.assertRaisesRegex(
            section_indexes.ManifestError,
            "Ambiguous catalogue subject",
        ):
            section_indexes.plan_catalog_topic_batch(
                self.root,
                "Test Subject",
                "Unicode — Section",
                catalog={
                    "schema_version": 1,
                    "variant": "learner-v2",
                    "topics": [self.topics[0], duplicate],
                },
                records=[],
            )

    def test_ambiguous_section_fails_clearly(self) -> None:
        duplicate = json.loads(json.dumps(self.topics[0]))
        duplicate["section"]["key"] = "other-section"
        duplicate["topic_key"] = "test-subject-other-01"
        duplicate["learner_v2_command"] = (
            "Generate learner-v2 topic: Test Subject — Unicode — Section — Other"
        )
        with self.assertRaisesRegex(
            section_indexes.ManifestError,
            "Ambiguous section",
        ):
            section_indexes.plan_catalog_topic_batch(
                self.root,
                "Test Subject",
                "Unicode — Section",
                catalog={
                    "schema_version": 1,
                    "variant": "learner-v2",
                    "topics": [self.topics[0], duplicate],
                },
                records=[],
            )

    def test_output_is_deterministic_unicode_safe_and_has_no_duplicates(self) -> None:
        first = self.plan()
        second = self.plan()
        self.assertEqual(first, second)
        self.assertEqual(
            batch_planner.render_plan(first),
            batch_planner.render_plan(second),
        )
        rendered = batch_planner.render_plan(first)
        self.assertIn("Cārvāka — Sources", rendered)
        keys = [topic["topic_key"] for topic in first["topics"]]
        commands = [topic["command"] for topic in first["topics"]]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(len(commands), len(set(commands)))

    def test_real_ancient_history_plan_is_empty(self) -> None:
        plan = section_indexes.plan_catalog_topic_batch(
            ROOT,
            "Ancient History",
            "Subject-wide Syllabus",
        )
        self.assertEqual(
            [],
            [topic["topic_key"] for topic in plan["topics"]],
        )


if __name__ == "__main__":
    unittest.main()
