"""Tests for the persistent four-item export library."""

from __future__ import annotations

import json
import hashlib
import os
import shutil
import sys
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import export_four_item_library as exporter


class ExportLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.scratch = TOOLS / ".test-export-four-item-library-scratch"
        if cls.scratch.exists():
            shutil.rmtree(cls.scratch)
        cls.scratch.mkdir()

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.scratch.exists():
            shutil.rmtree(cls.scratch)

    def test_latest_selection_uses_highest_generation(self) -> None:
        tracker = {
            "exports": [
                {
                    "topic_key": "sample-01",
                    "variant": "learner-v2",
                    "generation": 2,
                },
                {
                    "topic_key": "sample-01",
                    "variant": "learner-v2",
                    "generation": 4,
                },
                {
                    "topic_key": "sample-01",
                    "variant": "legacy-v1",
                    "generation": 9,
                },
            ]
        }
        selected = exporter.latest_learner_records(
            tracker, ["sample-01"]
        )
        self.assertEqual(4, selected[0]["generation"])

    def test_unknown_selected_topic_is_an_error(self) -> None:
        with self.assertRaises(exporter.ExportError):
            exporter.latest_learner_records(
                {"exports": []}, ["missing-topic"]
            )

    def test_selected_publication_cannot_overwrite_full_dated_manifest(self) -> None:
        source = Path(exporter.__file__).read_text(encoding="utf-8")
        self.assertIn("if require_all:", source)
        self.assertIn("selection_digest = hashlib.sha256", source)
        self.assertIn("selected-", source)
        self.assertIn('manifest_stem = f"final-four-item-library-{manifest_date}"', source)

    def test_human_readable_sanitization(self) -> None:
        self.assertEqual(
            "Philosophy Paper I — Indian Philosophy",
            exporter.sanitize_display_component(
                "Philosophy Paper I — Indian Philosophy"
            ),
        )
        self.assertEqual(
            "04-The-Stone-Age-Palaeolithic-and-Mesolithic",
            "04-"
            + exporter.slugify_topic(
                "The Stone Age: Palaeolithic & Mesolithic"
            ),
        )
        self.assertEqual(
            "Nyaya-Vaisesika",
            exporter.slugify_topic("Nyaya–Vaisesika"),
        )

    def test_long_topic_slug_is_bounded_and_stable(self) -> None:
        title = (
            "Provincial & Regional Kingdoms (Bengal, Gujarat, Malwa, "
            "Jaunpur, Kashmir) + bounded Ahom/Assam Prelims extension"
        )
        slug = exporter.slugify_topic(title)
        self.assertLessEqual(len(slug), exporter.MAX_TOPIC_SLUG_LENGTH)
        self.assertTrue(slug.startswith("Provincial-and-Regional"))
        self.assertTrue(slug.endswith("Ahom-Assam-Prelims-extension"))
        self.assertEqual(slug, exporter.slugify_topic(title))

    def test_canonical_destination_is_bounded_and_stable(self) -> None:
        title = (
            "Indian States & Society in the 18th Century "
            "(Marathas, Sikhs, successor states)"
        )
        kwargs = {
            "export_root": self.scratch / "canonical-root",
            "subject_folder": "Modern History",
            "section_folder": "Subject-wide Syllabus",
        }
        folder = exporter.canonical_topic_folder("02", title, **kwargs)
        self.assertEqual(
            folder,
            exporter.canonical_topic_folder("02", title, **kwargs),
        )
        for directory, filenames in exporter.TOPIC_DELIVERABLES.items():
            for filename in filenames:
                path = (
                    kwargs["export_root"]
                    / kwargs["subject_folder"]
                    / kwargs["section_folder"]
                    / folder
                    / directory
                    / filename
                )
                self.assertLessEqual(
                    len(str(path.resolve())),
                    exporter.WINDOWS_SAFE_LIBRARY_PATH_LENGTH,
                )

    def test_navigation_and_indexes_use_canonical_destination(self) -> None:
        export_root = self.scratch / "canonical-indexes"
        catalogue = exporter.CatalogueTopic(
            topic_key="modern-indian-history-02",
            title=(
                "Indian States & Society in the 18th Century "
                "(Marathas, Sikhs, successor states)"
            ),
            subject="Modern History",
            section="Subject-wide Syllabus",
            number=2,
            subject_order=1,
            section_order=1,
            topic_order=2,
        )
        subject_folder = exporter.sanitize_display_component(catalogue.subject)
        section_folder = exporter.sanitize_display_component(catalogue.section)
        selection = exporter.ExportSelection(
            record={
                "topic_key": catalogue.topic_key,
                "record_id": f"{catalogue.topic_key}:learner-v2:g2",
                "generation": 2,
            },
            catalogue=catalogue,
            subject_folder=subject_folder,
            section_folder=section_folder,
            topic_folder=exporter.canonical_topic_folder(
                "02",
                catalogue.title,
                export_root=export_root,
                subject_folder=subject_folder,
                section_folder=section_folder,
            ),
        )
        topic_dir = export_root / selection.destination_relative
        (topic_dir / "README.txt").parent.mkdir(parents=True)
        (topic_dir / "README.txt").write_text("topic", encoding="utf-8")
        for directory, filenames in exporter.TOPIC_DELIVERABLES.items():
            target = topic_dir / directory
            target.mkdir()
            for filename in filenames:
                (target / filename).write_bytes(b"x")
        navigation = exporter.navigation_topic_record(
            selection, {"status": "passed"}
        )
        expected = str(selection.destination_relative).replace("/", "\\")
        self.assertEqual(expected, navigation["destination_folder"])
        (export_root / "MASTER-TRACKER.md").write_text(
            exporter.master_tracker_markdown(export_root, [navigation]),
            encoding="utf-8",
        )
        (export_root / "CATALOGUE.md").write_text(
            exporter.catalogue_markdown(export_root, [selection]),
            encoding="utf-8",
        )
        exporter.write_subject_section_indexes(
            export_root,
            [selection],
            {selection.topic_key: navigation},
        )
        self.assertTrue(
            exporter.validate_markdown_links(export_root)["passed"]
        )

    def test_retained_essay_contract_with_generic_links_uses_generic_layout(self) -> None:
        export_root = self.scratch / "mixed-retained-navigation"
        generic_links = {
            "readme": "Essay\\Subject-wide Syllabus\\01-Test\\README.txt",
            "complete_learning_session": (
                "Essay\\Subject-wide Syllabus\\01-Test\\"
                "01-Complete-Learning-Session\\Complete-Learning-Session.pdf"
            ),
            "solved_practice_workbook": (
                "Essay\\Subject-wide Syllabus\\01-Test\\"
                "02-Solved-Practice-Workbook\\Solved-Practice-Workbook.pdf"
            ),
            "graphical_flowchart": (
                "Essay\\Subject-wide Syllabus\\01-Test\\"
                "03-Carvaka-Graphical-Flowchart\\At-a-Glance-Poster.pdf"
            ),
            "ascii_master_flowchart": (
                "Essay\\Subject-wide Syllabus\\01-Test\\"
                "04-ASCII-Master-Flowchart\\ASCII-Master-Flowchart.pdf"
            ),
        }
        topic = {
            "topic_key": "essay-01",
            "catalogue_number": 1,
            "topic_title": "Test",
            "subject": "Essay",
            "section": "Subject-wide Syllabus",
            "source_record_id": "essay-01:learner-v2:g4",
            "source_generation": 4,
            "artifact_contract": exporter.ESSAY_CONTRACT,
            "links": generic_links,
        }
        self.assertFalse(exporter.essay_navigation_links(topic))
        markdown = exporter.master_tracker_markdown(export_root, [topic])
        self.assertIn("Complete-Learning-Session.pdf", markdown)

    def test_ascii_pdf_round_trip_preserves_panels(self) -> None:
        text = (
            "ASCII MASTER FLOW — PANEL 1/2: Cārvāka starting point\n"
            "CLAIM -> TEST -> VERDICT\n"
            "   |       |\n"
            "   +-------+\n\n"
            "ASCII MASTER FLOW — PANEL 2/2: Qualified close\n"
            "Evidence — objection — reply\n"
            "No replacement glyphs.\n"
        )
        pdf_path = self.scratch / "ascii-round-trip.pdf"
        result = exporter.render_ascii_pdf(text, pdf_path)
        self.assertTrue(result["passed"])
        self.assertTrue(result["normalized_equal"])
        self.assertEqual(2, result["text_panel_count"])
        self.assertEqual(2, result["pdf_page_count"])
        self.assertGreaterEqual(result["minimum_font_size_points"], 9.0)

    def test_exact_topic_shape_rejects_extra_files(self) -> None:
        topic = self.scratch / "shape"
        topic.mkdir()
        (topic / "README.txt").write_text("test", encoding="utf-8")
        for directory, filenames in exporter.TOPIC_DELIVERABLES.items():
            target = topic / directory
            target.mkdir()
            for filename in filenames:
                (target / filename).write_bytes(b"x")
        exporter.validate_topic_shape(topic)
        (topic / "extra.txt").write_text("stale", encoding="utf-8")
        with self.assertRaises(exporter.ExportError):
            exporter.validate_topic_shape(topic)

    def test_atomic_topic_replacement_removes_short_backup(self) -> None:
        parent = self.scratch / "atomic"
        destination = parent / ("Long-Human-Readable-Topic-" + "x" * 80)
        stage = self.scratch / "stage-topic"
        destination.mkdir(parents=True)
        (destination / "version.txt").write_text("old", encoding="utf-8")
        stage.mkdir()
        (stage / "version.txt").write_text("new", encoding="utf-8")
        exporter.atomic_replace_topic(stage, destination)
        self.assertEqual(
            "new",
            (destination / "version.txt").read_text(encoding="utf-8"),
        )
        self.assertFalse(stage.exists())
        self.assertFalse(any(path.name.startswith(".old-") for path in parent.iterdir()))

    def test_atomic_replace_retries_transient_permission_error(self) -> None:
        source = self.scratch / "retry-source.txt"
        destination = self.scratch / "retry-destination.txt"
        source.write_text("new", encoding="utf-8")
        real_replace = os.replace
        calls = 0

        def flaky_replace(first: object, second: object) -> None:
            nonlocal calls
            calls += 1
            if calls == 1:
                raise PermissionError("transient lock")
            real_replace(first, second)

        with mock.patch.object(exporter.os, "replace", flaky_replace):
            exporter.replace_with_retry(source, destination)
        self.assertEqual("new", destination.read_text(encoding="utf-8"))
        self.assertEqual(2, calls)

    def test_full_publication_prunes_only_stale_topic_destinations(self) -> None:
        root = self.scratch / "prune"
        keep = root / "Subject" / "Section" / "01-Keep"
        stale = root / "Subject" / "Section" / "01-Old-Name"
        unrelated = root / "_deep-content-review" / "reviews" / "topic"
        for directory in (keep, stale, unrelated):
            directory.mkdir(parents=True)
            (directory / "README.txt").write_text("x", encoding="utf-8")
        selection = exporter.ExportSelection(
            record={"topic_key": "topic-01"},
            catalogue=exporter.CatalogueTopic(
                topic_key="topic-01",
                title="Keep",
                subject="Subject",
                section="Section",
                number=1,
                subject_order=1,
                section_order=1,
                topic_order=1,
            ),
            subject_folder="Subject",
            section_folder="Section",
            topic_folder="01-Keep",
        )
        removed = exporter.prune_stale_topic_destinations(root, [selection])
        self.assertEqual([stale], removed)
        self.assertTrue(keep.is_dir())
        self.assertFalse(stale.exists())
        self.assertTrue(unrelated.is_dir())

    def test_long_destination_file_io_exceeds_windows_max_path(self) -> None:
        base = self.scratch / "long-destination"
        artifact = (
            base
            / ("topic-" + "x" * 180)
            / "01-Complete-Learning-Session"
            / ("artifact-" + "y" * 50 + ".pdf")
        )
        payload = b"long-path-regression"
        try:
            exporter.filesystem_io_path(artifact.parent).mkdir(parents=True)
            exporter.filesystem_io_path(artifact).write_bytes(payload)
            self.assertGreater(len(str(artifact.resolve())), 260)
            if os.name == "nt":
                self.assertTrue(
                    str(exporter.filesystem_io_path(artifact)).startswith(
                        "\\\\?\\"
                    )
                )
            self.assertTrue(exporter.file_is_file(artifact))
            self.assertEqual(len(payload), exporter.file_size(artifact))
            self.assertEqual(
                hashlib.sha256(payload).hexdigest(),
                exporter.sha256_file(artifact),
            )
            totals = exporter.count_library_files(base)
            self.assertEqual(1, totals["file_count"])
            self.assertEqual(1, totals["pdf_count"])
            self.assertEqual(len(payload), totals["total_bytes"])
        finally:
            if exporter.filesystem_io_path(base).exists():
                shutil.rmtree(exporter.filesystem_io_path(base))

    def test_real_inventory_resolves_all_latest_topics(self) -> None:
        selections = exporter.resolve_selections(
            ROOT,
            ROOT / "EXPORT-PDF-STATUS.json",
            ROOT / "upsc-ai-kit/manifests/v2/topic-catalog.json",
        )
        tracker = json.loads(
            (ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8")
        )
        expected = len(
            {
                item["topic_key"]
                for item in tracker["exports"]
                if item.get("variant") == "learner-v2"
            }
        )
        self.assertEqual(expected, len(selections))
        self.assertEqual(expected, len({item.topic_key for item in selections}))
        catalogue = json.loads(
            (
                ROOT / "upsc-ai-kit/manifests/v2/topic-catalog.json"
            ).read_text(encoding="utf-8")
        )
        latest_keys = {
            item["topic_key"]
            for item in tracker["exports"]
            if item.get("variant") == "learner-v2"
        }
        expected_subjects = {
            item["subject"]["display_name"]
            for item in catalogue["topics"]
            if item["topic_key"] in latest_keys
        }
        self.assertEqual(
            expected_subjects,
            {item.catalogue.subject for item in selections},
        )
        self.assertFalse(
            any(
                exporter.FORBIDDEN_PATH_RE.search(
                    str(item.destination_relative)
                )
                for item in selections
            )
        )
        for item in selections:
            for directory, filenames in exporter.TOPIC_DELIVERABLES.items():
                for filename in filenames:
                    path = (
                        exporter.DEFAULT_EXPORT_ROOT
                        / item.destination_relative
                        / directory
                        / filename
                    )
                    self.assertLessEqual(
                        len(str(path.resolve())),
                        exporter.WINDOWS_SAFE_LIBRARY_PATH_LENGTH,
                    )


if __name__ == "__main__":
    unittest.main()
