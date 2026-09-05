"""Focused tests for learner-v2 section manifests and separate indexes."""

from __future__ import annotations

import json
import re
import shutil
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_v2_section_indexes as section_indexes


class SectionIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = ROOT / "_test_v2_section_indexes"
        shutil.rmtree(self.root, ignore_errors=True)
        subject = self.root / "upsc-ai-kit" / "knowledge" / "Test-Subject"
        (subject / "basic").mkdir(parents=True)
        (subject / "advanced").mkdir(parents=True)
        for number, title in (
            (1, "Planned Topic"),
            (2, "Generated Topic"),
            (3, "Approved Topic"),
            (4, "Incomplete Topic"),
        ):
            (subject / "basic" / f"{number:02d}_{title.replace(' ', '-')}.md").write_text(
                f"# {title}\n", encoding="utf-8"
            )
            (subject / "advanced" / f"{number:02d}_{title.replace(' ', '-')}.md").write_text(
                f"# {title} Advanced\n", encoding="utf-8"
            )

        self.manifest_path = (
            self.root
            / "upsc-ai-kit"
            / "manifests"
            / "v2"
            / "test-subject--test-section.json"
        )
        self.manifest_path.parent.mkdir(parents=True)
        topics = []
        for number, title in (
            (1, "Planned Topic"),
            (2, "Generated Topic"),
            (3, "Cārvāka — Approved Topic"),
            (4, "Incomplete Topic"),
        ):
            topics.append(
                {
                    "topic_key": f"test-subject-{number:02d}",
                    "display_title": title,
                    "syllabus_mapping": f"Official test clause {number}.",
                    "source_basic": (
                        "upsc-ai-kit\\knowledge\\Test-Subject\\basic\\"
                        f"{number:02d}_{('Approved Topic' if number == 3 else title).replace(' ', '-').replace('Cārvāka-—-', '')}.md"
                    ),
                    "source_canonical": (
                        "upsc-ai-kit\\knowledge\\Test-Subject\\basic\\"
                        f"{number:02d}_{('Approved Topic' if number == 3 else title).replace(' ', '-').replace('Cārvāka-—-', '')}.md"
                    ),
                    "source_advanced": (
                        "upsc-ai-kit\\knowledge\\Test-Subject\\advanced\\"
                        f"{number:02d}_{('Approved Topic' if number == 3 else title).replace(' ', '-').replace('Cārvāka-—-', '')}.md"
                    ),
                    "cross_topic_sources": [],
                    "verified_pyq_sources": [],
                }
            )
        manifest = {
            "schema_version": 1,
            "variant": "learner-v2",
            "subject": {
                "key": "Test-Subject",
                "display_name": "Test Subject",
            },
            "section": {
                "key": "test-section",
                "name": "Cārvāka Test Section",
                "scope": "official-section",
                "complete_syllabus_section": True,
                "syllabus_sources": [],
            },
            "topics": topics,
        }
        self.manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        exports = []
        for number, is_approved in ((2, False), (3, True), (4, False)):
            topic_key = f"test-subject-{number:02d}"
            markdown = (
                "upsc-ai-kit\\knowledge\\Test-Subject\\learning-sessions\\v2\\"
                f"test-section\\{topic_key}_Learning-Session.md"
            )
            notes = (
                "notes\\Test-Subject\\learning-session-v2\\test-section\\notes\\"
                f"{topic_key}_Learning-Session_2026-08-20.pdf"
            )
            workbook = (
                "notes\\Test-Subject\\learning-session-v2\\test-section\\workbooks\\"
                f"{topic_key}_Solved-Workbook_2026-08-20.pdf"
            )
            for relative in (markdown, notes):
                path = section_indexes.repo_path(self.root, relative)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("test\n", encoding="utf-8")
            if number != 4:
                path = section_indexes.repo_path(self.root, workbook)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("test\n", encoding="utf-8")
            exports.append(
                {
                    "record_id": f"{topic_key}:learner-v2:g1",
                    "topic_key": topic_key,
                    "variant": "learner-v2",
                    "generation": 1,
                    "supersedes": None,
                    "main_pdf": notes,
                    "workbook": workbook,
                    "markdown": markdown,
                    "approved": is_approved,
                    "approval": {
                        "approved": is_approved,
                        "approved_on": "2026-08-20" if is_approved else None,
                        "scope": f"{topic_key}:learner-v2:g1",
                    },
                    "validation": {
                        "state": "passed" if number != 4 else "failed"
                    },
                }
            )
        (self.root / "EXPORT-PDF-STATUS.json").write_text(
            json.dumps(
                {"schema_version": 2, "exports": exports},
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def generate(self) -> dict[str, Path]:
        return section_indexes.generate_section_indexes(
            self.root,
            self.manifest_path,
        )

    def test_planned_generated_approved_and_incomplete_are_independent(self) -> None:
        outputs = self.generate()
        coverage = outputs["coverage"].read_text(encoding="utf-8")
        self.assertIn("1 approved · 1 generated/unapproved · 1 incomplete · 1 planned", coverage)
        self.assertRegex(coverage, r"`test-subject-01`.*\| planned \| not generated")
        self.assertRegex(
            coverage,
            r"`test-subject-02`.*\| generated \| pending explicit topic approval",
        )
        self.assertRegex(coverage, r"`test-subject-03`.*\| approved \| approved")
        self.assertRegex(coverage, r"`test-subject-04`.*\| incomplete \| pending")

    def test_notes_and_workbook_indexes_are_strictly_separate(self) -> None:
        outputs = self.generate()
        notes = outputs["notes"].read_text(encoding="utf-8")
        workbooks = outputs["workbooks"].read_text(encoding="utf-8")
        self.assertNotIn("_Solved-Workbook_", notes)
        self.assertNotIn("\\workbooks\\", notes)
        self.assertNotIn("_Learning-Session_2026-08-20.pdf", workbooks)
        self.assertNotIn("\\notes\\", workbooks)

    def test_rerun_is_deterministic_and_has_no_duplicate_rows(self) -> None:
        outputs = self.generate()
        first = {name: path.read_bytes() for name, path in outputs.items()}
        outputs = self.generate()
        second = {name: path.read_bytes() for name, path in outputs.items()}
        self.assertEqual(first, second)
        coverage = second["coverage"].decode("utf-8")
        for number in range(1, 5):
            row = f"| {number} | `test-subject-{number:02d}` |"
            self.assertEqual(1, coverage.count(row))

    def test_unicode_title_is_preserved_as_utf8(self) -> None:
        outputs = self.generate()
        coverage = outputs["coverage"].read_text(encoding="utf-8")
        self.assertIn("Cārvāka — Approved Topic", coverage)

    def test_root_command_guide_is_human_facing_and_complete(self) -> None:
        outputs = self.generate()
        guide_path = outputs["command_guide"]
        self.assertEqual(
            self.root / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
            guide_path,
        )
        guide = guide_path.read_text(encoding="utf-8")
        self.assertTrue(
            guide.startswith(
                "# Learner-v2 Subject/Section Command Index\n\n"
                "## Use\n"
            )
        )
        self.assertIn(
            "For a bounded automatic run, paste the section's **Next 10** command.",
            guide,
        )
        self.assertIn(
            "Every `Generate learner-v2 topic: ...` command creates four integrated outputs:",
            guide,
        )
        self.assertIn(
            "Every completed teaching subtopic in the learning PDF also ends",
            guide,
        )
        self.assertIn("## Detailed reference — optional", guide)
        self.assertIn("authoritative human-facing file", guide)
        self.assertIn(
            "Do not construct a command from a placeholder template.",
            guide,
        )
        self.assertIn("full-section command remains available", guide)
        self.assertIn("Topic states in manifest order", guide)
        self.assertIn("machine-readable plans", guide)
        self.assertIn("Cārvāka Test Section", guide)
        self.assertIn("| Full | 4 |", guide)
        self.assertIn("TOPIC-COVERAGE-INDEX.md", guide)
        self.assertIn("NOTES-PDF-INDEX.md", guide)
        self.assertIn("WORKBOOK-PDF-INDEX.md", guide)
        self.assertIn(
            "Generate learner-v2 section: Test Subject — Cārvāka Test Section",
            guide,
        )
        self.assertIn(
            "Generate learner-v2 section: Test Subject — Cārvāka Test Section — Generate index only",
            guide,
        )
        self.assertIn(
            "Generate learner-v2 section: Test Subject — Cārvāka Test Section — Start from topic Planned Topic",
            guide,
        )
        self.assertIn(
            "Generate next 10 learner-v2 topics: Test Subject — Cārvāka Test Section",
            guide,
        )
        self.assertEqual(3, guide.count("```text"))

    def test_quick_commands_are_state_aware_manifest_ordered_and_unicode(self) -> None:
        guide = self.generate()["command_guide"].read_text(encoding="utf-8")
        pending_commands = [
            "Generate learner-v2 topic: Test Subject — Cārvāka Test Section — Planned Topic",
            "Generate learner-v2 topic: Test Subject — Cārvāka Test Section — Incomplete Topic — Regenerate",
        ]
        completed_commands = [
            "Generate learner-v2 topic: Test Subject — Cārvāka Test Section — Generated Topic — Regenerate",
            "Generate learner-v2 topic: Test Subject — Cārvāka Test Section — Cārvāka — Approved Topic — Regenerate",
        ]
        match = re.search(
            r"#### Pending / incomplete queue — 2 topics\n\n```text\n"
            r"(?P<commands>.*?)\n```",
            guide,
            re.DOTALL,
        )
        self.assertIsNotNone(match)
        self.assertEqual(pending_commands, match.group("commands").splitlines())
        completed_match = re.search(
            r"#### Optional completed-topic regeneration\n\n```text\n"
            r"(?P<commands>.*?)\n```",
            guide,
            re.DOTALL,
        )
        self.assertIsNotNone(completed_match)
        self.assertEqual(
            completed_commands,
            completed_match.group("commands").splitlines(),
        )
        for command in [*pending_commands, *completed_commands]:
            self.assertEqual(1, guide.count(command))
        self.assertNotIn(pending_commands[0] + " — Regenerate", guide)
        self.assertIn("✅ DONE — Generated Topic", guide)
        self.assertIn("✅ DONE — Cārvāka — Approved Topic", guide)

    def test_command_states_are_adjacent_and_use_public_state_labels(self) -> None:
        guide = self.generate()["command_guide"].read_text(encoding="utf-8")
        self.assertIn("**planned — not generated**", guide)
        self.assertIn("**generated — completed, unapproved**", guide)
        self.assertIn("**approved — completed, approved**", guide)
        self.assertIn(
            "**generated — incomplete or validation failed; "
            "regeneration/finalisation required**",
            guide,
        )

    def test_command_guide_has_no_duplicate_copy_paste_commands(self) -> None:
        guide = self.generate()["command_guide"].read_text(encoding="utf-8")
        blocks = re.findall(r"```text\n(.*?)\n```", guide, re.DOTALL)
        commands = [
            command
            for block in blocks
            for command in block.splitlines()
        ]
        self.assertTrue(commands)
        self.assertTrue(
            all(
                command.startswith("Generate learner-v2 topic: ")
                or command.startswith("Generate next 10 learner-v2 topics: ")
                for command in commands
            )
        )
        self.assertEqual(len(commands), len(set(commands)))

    def test_command_guide_scans_new_valid_manifests_and_is_deterministic(self) -> None:
        self.generate()
        first = (self.root / section_indexes.COMMAND_GUIDE_FILE).read_bytes()
        second_manifest = json.loads(
            self.manifest_path.read_text(encoding="utf-8")
        )
        second_manifest["subject"]["display_name"] = "Ānvikṣikī"
        second_manifest["section"] = {
            "key": "second-section",
            "name": "Second Section",
            "scope": "pilot",
            "complete_syllabus_section": False,
            "syllabus_sources": [],
        }
        second_manifest["topics"] = [second_manifest["topics"][0]]
        second_path = self.manifest_path.with_name(
            "test-subject--second-section.json"
        )
        second_path.write_text(
            json.dumps(second_manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        guide_path = section_indexes.generate_command_guide(self.root)
        updated = guide_path.read_bytes()
        self.assertNotEqual(first, updated)
        self.assertIn("Ānvikṣikī", updated.decode("utf-8"))
        self.assertIn(
            "Generate next 10 learner-v2 topics: Ānvikṣikī — Second Section",
            updated.decode("utf-8"),
        )
        self.assertIn(
            "Generate learner-v2 topic: Ānvikṣikī — Second Section — Planned Topic",
            updated.decode("utf-8"),
        )
        self.assertLess(
            updated.decode("utf-8").index("### Test Subject — Cārvāka Test Section"),
            updated.decode("utf-8").index("### Ānvikṣikī — Second Section"),
        )
        section_indexes.generate_command_guide(self.root)
        self.assertEqual(updated, guide_path.read_bytes())

    def test_current_pilot_copy_paste_commands_are_exact(self) -> None:
        guide = section_indexes.render_command_guide(
            ROOT,
            section_indexes.registered_manifests(ROOT),
            section_indexes.load_tracker(ROOT / "EXPORT-PDF-STATUS.json"),
        )
        all_commands = [
            command
            for block in re.findall(r"```text\n(.*?)\n```", guide, re.DOTALL)
            for command in block.splitlines()
        ]
        commands = [
            command
            for command in all_commands
            if command.startswith("Generate learner-v2 topic: ")
        ]
        self.assertEqual(516, len(commands))
        self.assertEqual(516, len(set(commands)))
        self.assertEqual(len(all_commands), len(set(all_commands)))
        self.assertEqual(
            27,
            sum(
                command.startswith("Generate next 10 learner-v2 topics: ")
                for command in all_commands
            ),
        )
        for expected in (
            "Generate learner-v2 topic: Geography — Part B — Human, Economic and Regional Geography — Human Settlements and Urbanisation — Regenerate",
            "Generate learner-v2 topic: Geography — Part B — Human, Economic and Regional Geography — Primary Economic Activities: Agriculture — Regenerate",
            "Generate learner-v2 topic: Geography — Part B — Human, Economic and Regional Geography — Industries and Industrial Regions — Regenerate",
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper I — Indian Philosophy — Carvaka — Regenerate",
        ):
            self.assertIn(expected, commands)

    def test_all_ancient_topics_are_done_and_queue_is_empty(self) -> None:
        guide = section_indexes.render_command_guide(
            ROOT,
            section_indexes.registered_manifests(ROOT),
            section_indexes.load_tracker(ROOT / "EXPORT-PDF-STATUS.json"),
        )
        ancient = guide[
            guide.index('<a id="subject-ancient-history"></a>'):
            guide.index('<a id="subject-medieval-history"></a>')
        ]
        for title in (
            "Importance & Historiography of Ancient India",
            "Sources of Ancient Indian History",
            "Mahajanapadas & Rise of Magadha",
            "From Ancient to Medieval: Social Change & Legacy",
            "Imperial Cholas: State, Society, Economy & Maritime Power",
        ):
            self.assertIn(f"✅ DONE — {title}", ancient)
        self.assertIn(
            "Generate next 10 learner-v2 topics: Ancient History — "
            "Subject-wide Syllabus",
            ancient,
        )
        self.assertIn(
            "#### Pending / incomplete queue — 0 topics\n\n"
            "No planned or incomplete topics remain.",
            ancient,
        )

    def test_ambiguous_discovery_requires_explicit_manifest(self) -> None:
        with self.assertRaises(section_indexes.AmbiguousDiscoveryError):
            section_indexes.build_discovered_manifest(
                self.root,
                "Test-Subject",
                "unclear-subsection",
                "Unclear Subsection",
            )

    def test_table_range_discovery_expands_all_owned_topics(self) -> None:
        readme = (
            self.root
            / "upsc-ai-kit"
            / "knowledge"
            / "Test-Subject"
            / "README.md"
        )
        readme.write_text(
            "## Part A — Test Range\n\n"
            "| # | Topic |\n"
            "|---|---|\n"
            "| 01-04 | Test topics |\n",
            encoding="utf-8",
        )
        manifest = section_indexes.build_discovered_manifest(
            self.root,
            "Test-Subject",
            "test-range",
            "Part A — Test Range",
        )
        self.assertEqual(4, len(manifest["topics"]))

    def test_registered_sections_resolve_latest_paths_and_scope(self) -> None:
        sections = (
            (
                ROOT
                / "upsc-ai-kit"
                / "manifests"
                / "v2"
                / "geography--human-economic-geography-pilot.json",
                "notes\\Learner-v2-Refreshed\\Geography\\GEO\\learning-sessions\\geo-28\\",
                "not a claim that the complete syllabus section is covered",
            ),
            (
                ROOT
                / "upsc-ai-kit"
                / "manifests"
                / "v2"
                / "philosophy--paper-i-indian-philosophy-pilot.json",
                "notes\\Philosophy\\learning-session-v2\\paper-i-indian-philosophy\\notes\\",
                "**Complete official section:** yes",
            ),
        )
        for manifest, expected, scope_statement in sections:
            outputs = section_indexes.generate_section_indexes(ROOT, manifest)
            coverage = outputs["coverage"].read_text(encoding="utf-8")
            self.assertIn(expected, coverage)
            self.assertIn(scope_statement, coverage)


if __name__ == "__main__":
    unittest.main()
