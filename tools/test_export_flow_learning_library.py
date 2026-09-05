"""Targeted tests for the reusable Flow Learning exporter."""

from __future__ import annotations

import json
import hashlib
import shutil
import sys
import tempfile
import time
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import export_flow_learning_library as exporter


class FlowLearningExporterTests(unittest.TestCase):
    def setUp(self) -> None:
        short_name = hashlib.sha1(
            self._testMethodName.encode("utf-8")
        ).hexdigest()[:8]
        self.scratch = Path(
            tempfile.mkdtemp(prefix=f"flow-learning-{short_name}-")
        )

    def tearDown(self) -> None:
        if self.scratch.exists():
            for attempt in range(20):
                try:
                    shutil.rmtree(self.scratch)
                    break
                except PermissionError:
                    if attempt == 19:
                        raise
                    time.sleep(0.1)

    def _write_json(self, path: Path, data: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def _record(
        self,
        key: str,
        generation: int,
        *,
        state: str = "passed",
    ) -> dict[str, object]:
        return {
            "record_id": f"{key}:learner-v2:g{generation}",
            "topic_key": key,
            "variant": "learner-v2",
            "generation": generation,
            "validation": {"state": state},
        }

    def _repository(self) -> dict[str, Path]:
        root = self.scratch
        tracker = root / "EXPORT-PDF-STATUS.json"
        catalogue = root / "upsc-ai-kit/manifests/v2/topic-catalog.json"
        source = (
            root
            / "notes"
            / "Final-Learning-Packages"
            / "Polity"
            / "Subject-wide Syllabus"
        )
        flow = root / "notes" / "Flow-Learning"
        records = [
            self._record("polity-01", 1),
            self._record("polity-01", 2),
            self._record("polity-02", 1),
        ]
        self._write_json(tracker, {"exports": records})
        self._write_json(
            catalogue,
            {
                "topics": [
                    {
                        "topic_key": "polity-01",
                        "source_number": 1,
                        "display_title": "Historical Background",
                        "subject": {"display_name": "Polity"},
                    },
                    {
                        "topic_key": "polity-02",
                        "source_number": 2,
                        "display_title": "Making of the Constitution",
                        "subject": {"display_name": "Polity"},
                    },
                ]
            },
        )
        source.mkdir(parents=True)
        (source / "INDEX.md").write_text("# Source index\n", encoding="utf-8")
        for key, number, title, generation in (
            ("polity-01", 1, "Historical Background", 2),
            ("polity-02", 2, "Making of the Constitution", 1),
        ):
            folder_name = f"{number:02d}-{exporter.slugify_topic(title)}"
            topic = source / folder_name
            ascii_dir = topic / "04-ASCII-Master-Flowchart"
            complete_dir = topic / "01-Complete-Learning-Session"
            workbook_dir = topic / "02-Solved-Practice-Workbook"
            ascii_dir.mkdir(parents=True)
            complete_dir.mkdir()
            workbook_dir.mkdir()
            panels = []
            for panel in range(1, 9):
                lines = [
                    f"ASCII MASTER FLOW — PANEL {panel}/8: {title} stage {panel}",
                    *(
                        f"STAGE {panel} LINE {line}: CORE -> MECHANISM -> TRAP -> ANSWER"
                        for line in range(1, 11)
                    ),
                ]
                panels.append("\n".join(lines))
            text = "\n\n".join(panels) + "\n"
            (ascii_dir / "ASCII-Master-Flowchart.txt").write_text(
                text, encoding="utf-8", newline="\n"
            )
            (ascii_dir / "ASCII-Master-Flowchart.pdf").write_bytes(
                b"%PDF-flow-" + key.encode("ascii")
            )
            (complete_dir / "Complete-Learning-Session.pdf").write_bytes(
                b"%PDF-complete"
            )
            (workbook_dir / "Solved-Practice-Workbook.pdf").write_bytes(
                b"%PDF-workbook"
            )
            (topic / "README.txt").write_text(
                "FINAL LEARNING PACKAGE\n"
                f"Source record ID: {key}:learner-v2:g{generation}\n"
                f"Source generation: {generation}\n",
                encoding="utf-8",
                newline="\n",
            )
        return {
            "root": root,
            "tracker": tracker,
            "catalogue": catalogue,
            "source": source,
            "flow": flow,
        }

    def _export(
        self,
        paths: dict[str, Path],
        selected: list[str],
    ) -> dict[str, object]:
        return exporter.export_flow_library(
            root=paths["root"],
            tracker_path=paths["tracker"],
            catalogue_path=paths["catalogue"],
            source_root=paths["source"],
            export_root=paths["flow"],
            selected_keys=selected,
            validate_pdfs=False,
            case_year_evidence_path=paths["root"] / "missing-evidence.json",
            report_path=paths["flow"] / "FLOW-REPORT.md",
            validation_path=(
                paths["root"]
                / "upsc-ai-kit"
                / "manifests"
                / "exports"
                / "flow-validation.json"
            ),
        )

    def test_latest_record_resolution_uses_highest_validated_generation(self) -> None:
        tracker = {
            "exports": [
                self._record("polity-01", 2),
                self._record("polity-01", 4),
                self._record("polity-01", 5, state="failed"),
                {
                    **self._record("polity-01", 9),
                    "variant": "legacy-v1",
                },
            ]
        }
        selected = exporter.latest_validated_learner_records(
            tracker, ["polity-01"]
        )
        self.assertEqual(4, selected[0]["generation"])

    def test_unknown_selected_topic_is_rejected(self) -> None:
        with self.assertRaises(exporter.ExportError):
            exporter.latest_validated_learner_records(
                {"exports": []}, ["polity-99"]
            )

    def test_case_year_check_does_not_rewrite_or_reject_long_approved_lines(
        self,
    ) -> None:
        text = "X" * 120
        result = exporter._case_year_validation("polity-02", text)
        self.assertEqual("passed", result["status"])

    def test_deterministic_folder_and_file_naming(self) -> None:
        paths = self._repository()
        selection = exporter.resolve_selections(
            paths["root"],
            paths["tracker"],
            paths["catalogue"],
            paths["source"],
            ["polity-02"],
        )[0]
        self.assertEqual(
            "02-Making-of-the-Constitution",
            selection.destination_folder_name,
        )
        self.assertEqual(
            "02-Making-of-the-Constitution-Continuous-Flow-Learning.pdf",
            selection.output_pdf_name,
        )

    def test_long_topic_names_use_stable_bounded_output_stems(self) -> None:
        source_name = (
            "04-Weathering-Mass-Movement-Groundwater-India-"
            "Erosion-Landslides-Groundwater"
        )
        first = exporter.deterministic_output_stem(source_name)
        second = exporter.deterministic_output_stem(source_name)
        self.assertEqual(first, second)
        self.assertLessEqual(len(first), exporter.MAX_OUTPUT_STEM_LENGTH)
        self.assertTrue(first.startswith("04-"))
        self.assertTrue(first.endswith("-Continuous-Flow-Learning"))
        self.assertNotEqual(
            first,
            exporter.deterministic_output_stem(source_name + "-Variant"),
        )

    def test_subject_agnostic_resolution_uses_catalogue_subject_and_prefix(
        self,
    ) -> None:
        paths = self._repository()
        tracker = json.loads(paths["tracker"].read_text(encoding="utf-8"))
        tracker["exports"].append(
            self._record("ancient-indian-history-01", 3)
        )
        self._write_json(paths["tracker"], tracker)
        catalogue = json.loads(
            paths["catalogue"].read_text(encoding="utf-8")
        )
        catalogue["topics"].append(
            {
                "topic_key": "ancient-indian-history-01",
                "source_number": 1,
                "display_title": "Importance and Historiography",
                "subject": {"display_name": "Ancient History"},
                "section": {"name": "Subject-wide Syllabus"},
            }
        )
        self._write_json(paths["catalogue"], catalogue)
        final_root = paths["source"].parents[1]
        topic = (
            final_root
            / "Ancient History"
            / "Subject-wide Syllabus"
            / "01-Importance-and-Historiography"
        )
        ascii_dir = topic / "04-ASCII-Master-Flowchart"
        complete_dir = topic / "01-Complete-Learning-Session"
        workbook_dir = topic / "02-Solved-Practice-Workbook"
        ascii_dir.mkdir(parents=True)
        complete_dir.mkdir()
        workbook_dir.mkdir()
        (ascii_dir / "ASCII-Master-Flowchart.pdf").write_bytes(b"%PDF")
        panels = []
        for panel in range(1, 9):
            panels.append(
                "\n".join(
                    [
                        f"ASCII MASTER FLOW — PANEL {panel}/8: Ancient stage {panel}",
                        *(
                            f"STAGE {panel} LINE {line}: SOURCE -> DEBATE -> TRAP -> ANSWER"
                            for line in range(1, 11)
                        ),
                    ]
                )
            )
        (ascii_dir / "ASCII-Master-Flowchart.txt").write_text(
            "\n\n".join(panels) + "\n",
            encoding="utf-8",
        )
        (complete_dir / "Complete-Learning-Session.pdf").write_bytes(
            b"%PDF-complete"
        )
        (workbook_dir / "Solved-Practice-Workbook.pdf").write_bytes(
            b"%PDF-workbook"
        )
        (topic / "README.txt").write_text(
            "Source record ID: ancient-indian-history-01:learner-v2:g3\n"
            "Source generation: 3\n",
            encoding="utf-8",
        )
        selection = exporter.resolve_selections(
            paths["root"],
            paths["tracker"],
            paths["catalogue"],
            final_root,
            ["ancient-indian-history-01"],
            subject="Ancient History",
            topic_prefix="ancient-indian-history-",
        )[0]
        self.assertEqual("Ancient History", selection.subject)
        self.assertEqual(
            "01-Importance-and-Historiography",
            selection.source_folder_name,
        )
        flow = paths["root"] / "notes" / "Flow-Other"
        result = exporter.export_flow_library(
            root=paths["root"],
            tracker_path=paths["tracker"],
            catalogue_path=paths["catalogue"],
            source_root=final_root,
            export_root=flow,
            selected_keys=["ancient-indian-history-01"],
            validate_pdfs=False,
            case_year_evidence_path=paths["root"] / "missing-evidence.json",
            report_path=flow / "ANCIENT-REPORT.md",
            validation_path=(
                paths["root"]
                / "upsc-ai-kit"
                / "manifests"
                / "exports"
                / "ancient-validation.json"
            ),
            subject="Ancient History",
            topic_prefix="ancient-indian-history-",
        )
        self.assertEqual("Ancient History", result["scope"]["subject"])
        self.assertTrue(
            (
                flow
                / "Ancient History"
                / "01-Importance-and-Historiography"
                / "01-Importance-and-Historiography-Continuous-Flow-Learning.txt"
            ).is_file()
        )
        self.assertIn(
            "Ancient History topic index",
            (flow / "START-HERE.md").read_text(encoding="utf-8"),
        )

    def test_missing_catalogue_extended_key_uses_exact_clean_package_metadata(
        self,
    ) -> None:
        paths = self._repository()
        key = "geography-28-human-settlements-and-urbanisation"
        tracker = json.loads(paths["tracker"].read_text(encoding="utf-8"))
        tracker["exports"].append(self._record(key, 12))
        self._write_json(paths["tracker"], tracker)
        catalogue = json.loads(
            paths["catalogue"].read_text(encoding="utf-8")
        )
        catalogue["topics"].append(
            {
                "topic_key": "geography-28",
                "source_number": 28,
                "display_title": "Human Settlements and Urbanisation",
                "subject": {"display_name": "Geography"},
            }
        )
        self._write_json(paths["catalogue"], catalogue)
        final_root = paths["source"].parents[1]
        long_section = "Part B — Human Geography Extended"
        topic = (
            final_root
            / "Geography"
            / long_section
            / "28-Human-Settlements-and-Urbanisation"
        )
        ascii_dir = topic / "04-ASCII-Master-Flowchart"
        ascii_dir.mkdir(parents=True)
        (ascii_dir / "ASCII-Master-Flowchart.pdf").write_bytes(b"%PDF")
        (ascii_dir / "ASCII-Master-Flowchart.txt").write_text(
            "ASCII MASTER FLOW — PANEL 1/1: settlements\n",
            encoding="utf-8",
        )
        (topic / "README.txt").write_text(
            "FINAL LEARNING PACKAGE\n"
            "Topic: Human Settlements and Urbanisation\n"
            "Subject: Geography\n"
            f"Section: {long_section}\n"
            "Catalogue number: 28\n"
            f"Source record ID: {key}:learner-v2:g12\n"
            "Source generation: 12\n",
            encoding="utf-8",
        )
        selection = exporter.resolve_selections(
            paths["root"],
            paths["tracker"],
            paths["catalogue"],
            final_root,
            [key],
            subject="Geography",
            topic_prefix="geography-",
        )[0]
        self.assertEqual(28, selection.number)
        self.assertEqual(
            "Human Settlements and Urbanisation", selection.title
        )
        self.assertEqual(long_section, selection.section)
        self.assertEqual(
            "28-Human-Settlements-and-Urbanisation",
            selection.destination_folder_name,
        )
        self.assertEqual(
            "28-Human-Settlements-and-Urbanisation-Continuous-Flow-Learning.pdf",
            selection.output_pdf_name,
        )
        self.assertIn(
            "catalogue entry absent", selection.metadata_resolution
        )

    def test_selected_export_is_byte_equal_and_exact_shape(self) -> None:
        paths = self._repository()
        result = self._export(paths, ["polity-01"])
        topic = (
            paths["flow"] / "Polity" / "01-Historical-Background"
        )
        self.assertTrue(result["status"] == "passed")
        self.assertEqual(
            {
                "01-Historical-Background-Continuous-Flow-Learning.pdf",
                "01-Historical-Background-Continuous-Flow-Learning.txt",
                "README.txt",
            },
            {item.name for item in topic.iterdir()},
        )
        source = (
            paths["source"]
            / "01-Historical-Background"
            / "04-ASCII-Master-Flowchart"
        )
        self.assertEqual(
            (source / "ASCII-Master-Flowchart.pdf").read_bytes(),
            (
                topic
                / "01-Historical-Background-Continuous-Flow-Learning.pdf"
            ).read_bytes(),
        )
        self.assertFalse(
            (paths["flow"] / "Polity" / "02-Making-of-the-Constitution").exists()
        )

    def test_navigation_links_resolve_and_include_direct_pdf_txt_links(self) -> None:
        paths = self._repository()
        self._export(paths, ["polity-01"])
        links = exporter.validate_markdown_links(paths["flow"])
        self.assertTrue(links["passed"])
        tracker = (paths["flow"] / "TRACKER.md").read_text(encoding="utf-8")
        self.assertIn("Continuous-Flow-Learning.pdf", tracker)
        self.assertIn("Continuous-Flow-Learning.txt", tracker)
        start = (paths["flow"] / "START-HERE.md").read_text(encoding="utf-8")
        self.assertIn("does **not** replace or reduce", start)

    def test_selected_refresh_rebuilds_navigation_with_dynamic_count(self) -> None:
        paths = self._repository()
        self._export(paths, ["polity-01"])
        result = self._export(paths, ["polity-02"])
        self.assertEqual(2, result["summary"]["topic_folder_count"])
        index = (
            paths["flow"] / "Polity" / "INDEX.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Topics: **2**", index)
        self.assertIn("Historical Background", index)
        self.assertIn("Making of the Constitution", index)

    def test_tracker_and_source_library_are_not_mutated(self) -> None:
        paths = self._repository()
        tracker_before = paths["tracker"].read_bytes()
        source_before = exporter.tree_fingerprint(
            paths["source"].parent.parent
        )
        result = self._export(paths, ["polity-01"])
        self.assertEqual(tracker_before, paths["tracker"].read_bytes())
        self.assertEqual(
            source_before,
            exporter.tree_fingerprint(paths["source"].parent.parent),
        )
        self.assertTrue(result["tracker"]["unchanged"])
        self.assertTrue(result["source_packages"]["unchanged"])


if __name__ == "__main__":
    unittest.main()
