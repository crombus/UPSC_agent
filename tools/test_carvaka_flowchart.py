"""Regression tests for the reusable Cārvāka graphical-v2 renderer."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import carvaka_flowchart as carvaka
import polity_flowchart_case_years as case_years
import refresh_all_v2_learning_sessions as refresh


class GraphicalSpecTests(unittest.TestCase):
    def test_all_active_topics_have_explicit_valid_specs(self) -> None:
        topics = refresh.latest_validated_topics(
            refresh.load_tracker(),
            refresh.merged_overrides(),
        )
        self.assertGreater(len(topics), 0)
        paths = [
            refresh.graphical_spec_path(topic)
            for topic in topics
        ]
        self.assertTrue(all(path.is_file() for path in paths))
        for topic, path in zip(topics, paths):
            spec = carvaka.load_spec(path)
            self.assertEqual(topic.key, spec["topic_key"])
            self.assertEqual(topic.subject, spec["subject"])

    def test_flat_repeated_closure_card_contract_is_rejected(self) -> None:
        path = (
            refresh.GRAPHICAL_SPEC_DIR
            / "Geography"
            / "geography-04.json"
        )
        spec = carvaka.load_spec(path)
        broken = copy.deepcopy(spec)
        for index, stage in enumerate(broken["stages"][:-1]):
            stage["layout"] = "columns"
            stage["pills"] = [
                {"text": f"SESSION {index}", "role": "primary"},
                {"text": "CONTEXT + EXACT CORE", "role": "primary"},
                {"text": "MECHANISM", "role": "primary"},
                {"text": "CONSEQUENCE", "role": "primary"},
            ]
            stage["groups"] = [
                {
                    "heading": "CONTEXT + EXACT CORE",
                    "role": "primary",
                    "items": ["Repeated flat closure content."],
                },
                {
                    "heading": "MECHANISM / ARGUMENT",
                    "role": "primary",
                    "items": ["Repeated flat closure content."],
                },
                {
                    "heading": "CONSEQUENCE / CONTRAST",
                    "role": "primary",
                    "items": ["Repeated flat closure content."],
                },
            ]
        errors = carvaka.validate_spec(broken)
        joined = "\n".join(errors)
        self.assertIn("layout diversity is too low", joined)
        self.assertIn("pill colour roles", joined)
        self.assertIn("banned flat-renderer", joined)

    def test_required_stage_contract_is_present(self) -> None:
        path = (
            refresh.GRAPHICAL_SPEC_DIR
            / "Philosophy"
            / "philosophy-paper-i-indian-philosophy-02.json"
        )
        spec = carvaka.load_spec(path)
        stages = spec["stages"]
        core = [stage for stage in stages if stage["role"] != "extra"]
        self.assertEqual(
            [f"{index:02d}" for index in range(len(core))],
            [stage["id"] for stage in core],
        )
        self.assertEqual("synthesis", core[-1]["role"])
        self.assertEqual("E", stages[-1]["id"])
        self.assertEqual("extra", stages[-1]["role"])
        self.assertTrue(all(4 <= len(stage["pills"]) <= 10 for stage in core))
        self.assertTrue(all(2 <= len(stage["groups"]) <= 4 for stage in core))
        self.assertTrue(all(stage["answer_line"] for stage in core))


class GraphicalArtifactTests(unittest.TestCase):
    def test_immutable_reference_hashes_are_exact(self) -> None:
        self.assertEqual([], carvaka.verify_reference(ROOT))

    def test_pilot_artifacts_pass_same_master_and_rail_validation(self) -> None:
        validation = refresh.load_json(refresh.GRAPHICAL_PILOT_VALIDATION)
        self.assertEqual(4, validation["topic_count"])
        for row in validation["topics"]:
            folder = refresh.repo_path(row["paths"]["flowchart"])
            audit = refresh.load_json(folder / "build-audit.json")
            spec = carvaka.load_spec(
                refresh.repo_path(audit["spec"])
            )
            errors = carvaka.validate_package(
                ROOT,
                folder,
                spec,
                audit,
                audit["tiles"],
            )
            self.assertEqual([], errors, row["topic_key"])
            tracker = refresh.load_tracker()
            record = next(
                record
                for record in tracker["exports"]
                if isinstance(record, dict)
                and record.get("topic_key") == row["topic_key"]
                and record.get("variant") == refresh.V2_VARIANT
                and int(record.get("generation") or 0)
                == int(row["source_generation"])
            )
            markdown = refresh.repo_path(str(record["markdown"]))
            subject = refresh.record_subject(record, markdown)
            override = refresh.merged_overrides().get(row["topic_key"], {})
            source = refresh.Topic(
                key=str(record["topic_key"]),
                subject=subject,
                section=refresh.safe_folder(
                    str(
                        override.get("section")
                        or refresh.derive_section(markdown, subject)
                    )
                ),
                topic_folder=refresh.safe_folder(
                    str(
                        override.get("topic_folder")
                        or refresh.compact_topic_folder(str(record["topic_key"]))
                    )
                ),
                title=refresh.title_from_markdown(markdown),
                generation=int(record["generation"]),
                record_id=str(record["record_id"]),
                markdown=markdown,
                main_pdf=refresh.repo_path(str(record["main_pdf"])),
                workbook=refresh.repo_path(str(record["workbook"])),
                source_record=record,
            )
            old_ascii = refresh.graphical_source_ascii(source)
            pilot_ascii = folder / "ascii-master.txt"
            provenance = source.source_record.get("provenance")
            repair = (
                provenance.get("flowchart_case_year_repair")
                if isinstance(provenance, dict)
                else None
            )
            if (
                source.subject == "Polity"
                and isinstance(repair, dict)
                and repair.get("id")
                == "polity-flowchart-case-year-repair-2026-08-24"
            ):
                normalized_pilot = case_years.normalize_ascii_body(
                    source.key,
                    pilot_ascii.read_text(encoding="utf-8"),
                )
                self.assertEqual(
                    old_ascii.read_text(encoding="utf-8")
                    .replace("\r\n", "\n")
                    .rstrip(),
                    normalized_pilot.replace("\r\n", "\n").rstrip(),
                )
            else:
                self.assertEqual(
                    old_ascii.read_bytes(),
                    pilot_ascii.read_bytes(),
                )

    def test_poster_contains_exact_master_image(self) -> None:
        validation = json.loads(
            refresh.GRAPHICAL_PILOT_VALIDATION.read_text(encoding="utf-8")
        )
        folder = refresh.repo_path(validation["topics"][0]["paths"]["flowchart"])
        self.assertEqual(
            [],
            carvaka.verify_poster_identity(
                folder / "master.png",
                folder / "poster.pdf",
            ),
        )


if __name__ == "__main__":
    unittest.main()
