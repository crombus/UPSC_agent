"""One-off finaliser: record publication, revalidation and unrelated failures.

Updates the Individual and State learner-v2 g2 validation manifest with the
clean-library and Flow-Learning publication results, the standalone
revalidation, the targeted test-suite result and the single known unrelated
failure that must not be repaired by this task.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "philosophy-paper-ii-socio-political-philosophy-03-learner-v2-g2-"
    "2026-08-27-validation.json"
)


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    data["clean_library_publication"] = {
        "state": "published",
        "destination": (
            "notes\\Final-Learning-Packages\\Philosophy Optional\\"
            "Philosophy Paper II \u2014 Socio-Political Philosophy\\"
            "03-Individual-and-State"
        ),
        "manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "final-four-item-library-2026-08-27-philosophy-socio-political-03-g2.json"
        ),
        "validation_manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "final-four-item-library-2026-08-27-philosophy-socio-political-03-g2"
            "-validation.json"
        ),
        "byte_identical_to_source": True,
    }
    data["flow_learning_publication"] = {
        "state": "published",
        "destination": (
            "notes\\Flow-Learning\\Philosophy Optional\\03-Individual-and-State"
        ),
        "scope": (
            "28 validated Philosophy Optional learner-v2 topics that hold an "
            "exact clean package, including this topic. The publication was "
            "scoped with an explicit topic list because Socio-Political topic "
            "01 carries a pre-existing, unrelated clean-package identity defect "
            "that this task deliberately does not repair."
        ),
        "report": (
            "notes\\Flow-Learning\\"
            "PHILOSOPHY-OPTIONAL-SOCIO-POLITICAL-03-FLOW-LEARNING-REPORT.md"
        ),
        "validation_manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "philosophy-paper-ii-socio-political-philosophy-03-flow-learning-g2"
            "-2026-08-27-validation.json"
        ),
        "ascii_txt_pdf_byte_identical_to_source_and_clean_library": True,
        "topic_count": 28,
        "total_pdf_pages": 253,
    }
    data["exhaustive_changed_files_manifest"] = (
        "upsc-ai-kit\\manifests\\exports\\"
        "philosophy-paper-ii-socio-political-philosophy-03-learner-v2-g2-"
        "2026-08-27-exhaustive-changed-files.md"
    )
    data["known_unrelated_failures"] = [
        {
            "scope": "philosophy-paper-ii-socio-political-philosophy-01",
            "symptom": (
                "tools/export_flow_learning_library.py aborts with 'no clean "
                "package matches exact tracker identity "
                "philosophy-paper-ii-socio-political-philosophy-01:learner-v2:g2"
                "/g2' when the whole Philosophy Optional subject is exported "
                "without an explicit topic list."
            ),
            "relation_to_this_topic": (
                "None. The defect predates this run and belongs to the topic-01 "
                "stricter-contract and ASCII metadata work."
            ),
            "action_taken": (
                "Not repaired, as instructed. The Flow-Learning publication was "
                "scoped to the 28 topics that do hold an exact clean package."
            ),
        },
        {
            "scope": "tools/test_v2_section_indexes.py",
            "symptom": (
                "Two intermediate runs failed in setUp with a Windows "
                "FileExistsError on the transient _test_v2_section_indexes "
                "fixture directory, because shutil.rmtree(..., "
                "ignore_errors=True) could not remove a directory still held by "
                "the operating system."
            ),
            "relation_to_this_topic": (
                "None. It is an environment-level file-locking flake on this "
                "Windows workspace, not a code defect introduced here."
            ),
            "action_taken": (
                "Not repaired. The suite passes cleanly once the stale fixture "
                "directory is removed; the final generator run and the targeted "
                "80-test run both reported OK."
            ),
        },
    ]
    data["standalone_revalidation"] = {
        "command": (
            "python tools\\validate_v2_export.py "
            "upsc-ai-kit\\knowledge\\Philosophy\\learning-sessions\\v2\\"
            "paper-ii-socio-political-philosophy\\"
            "philosophy-paper-ii-socio-political-philosophy-03_Learning-Session.md "
            "--topic-key philosophy-paper-ii-socio-political-philosophy-03 "
            "--ascii-spec upsc-ai-kit\\manifests\\retrofits\\ascii-panel-specs\\"
            "philosophy--paper-ii-socio-political-philosophy-03-ascii-2026-08-27.json "
            "--main-pdf notes\\Philosophy\\learning-session-v2\\"
            "paper-ii-socio-political-philosophy\\notes\\"
            "philosophy-paper-ii-socio-political-philosophy-03_Learning-Session_"
            "2026-08-27.pdf "
            "--workbook notes\\Philosophy\\learning-session-v2\\"
            "paper-ii-socio-political-philosophy\\workbooks\\"
            "philosophy-paper-ii-socio-political-philosophy-03_Solved-Workbook_"
            "2026-08-27.pdf "
            "--variant learner-v2 --generation 2 --refreshed-contract"
        ),
        "result": "V2 export validation passed.",
    }
    data["targeted_test_suites"] = {
        "command": (
            "python -m unittest tools.test_v2_section_indexes "
            "tools.test_v2_topic_command_catalog tools.test_v2_export_foundation "
            "tools.test_carvaka_flowchart tools.test_export_flow_learning_library"
        ),
        "tests_run": 80,
        "result": "OK",
    }
    data["rendered_visual_inspection"]["state"] = (
        "generated and inspected page by page; contact sheets, tiled pages and "
        "the master overview were reviewed for wrapping, arrow correspondence, "
        "complete matrix rows, blank/clipped pages and legacy navigation"
    )
    data["rendered_visual_inspection"]["repairs"] = [
        "Authored explicit graphical stage groups, sequences and comparison "
        "matrices for all ten core stages, replacing auto-derived fragments "
        "that split phrases mid-clause and left incomplete matrix rows."
    ]
    pending = MANIFEST.with_suffix(MANIFEST.suffix + ".pending")
    pending.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    os.replace(pending, MANIFEST)
    print(f"UPDATED: {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
