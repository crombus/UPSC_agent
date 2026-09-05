"""One-off finaliser: record publication, revalidation and unrelated failures.

Updates the Forms of Government learner-v2 g2 validation manifest with the
clean-library and Flow-Learning publication results, the standalone
revalidation, the targeted test-suite result and the known unrelated failures
that this task must not repair.
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
    / "philosophy-paper-ii-socio-political-philosophy-04-learner-v2-g2-"
    "2026-08-27-validation.json"
)


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    data["clean_library_publication"] = {
        "state": "published",
        "destination": (
            "notes\\Final-Learning-Packages\\Philosophy Optional\\"
            "Philosophy Paper II \u2014 Socio-Political Philosophy\\"
            "04-Forms-of-Government"
        ),
        "manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "final-four-item-library-2026-08-27-philosophy-socio-political-04-g2.json"
        ),
        "validation_manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "final-four-item-library-2026-08-27-philosophy-socio-political-04-g2"
            "-validation.json"
        ),
        "byte_identical_to_source": True,
        "items": [
            "01-Complete-Learning-Session\\Complete-Learning-Session.pdf",
            "02-Solved-Practice-Workbook\\Solved-Practice-Workbook.pdf",
            "03-Carvaka-Graphical-Flowchart\\At-a-Glance-Poster.pdf",
            "03-Carvaka-Graphical-Flowchart\\High-Resolution-Master.png",
            "03-Carvaka-Graphical-Flowchart\\Printable-Tiled-Version.pdf",
            "04-ASCII-Master-Flowchart\\ASCII-Master-Flowchart.pdf",
            "04-ASCII-Master-Flowchart\\ASCII-Master-Flowchart.txt",
        ],
    }
    data["flow_learning_publication"] = {
        "state": "published",
        "destination": (
            "notes\\Flow-Learning\\Philosophy Optional\\04-Forms-of-Government"
        ),
        "scope": (
            "29 validated Philosophy Optional learner-v2 topics that hold an "
            "exact clean package, including this topic. The publication was "
            "scoped with an explicit topic list because Socio-Political topic "
            "01 carries a pre-existing, unrelated clean-package identity defect "
            "that this task deliberately does not repair."
        ),
        "report": (
            "notes\\Flow-Learning\\"
            "PHILOSOPHY-OPTIONAL-SOCIO-POLITICAL-04-FLOW-LEARNING-REPORT.md"
        ),
        "validation_manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "philosophy-paper-ii-socio-political-philosophy-04-flow-learning-g2"
            "-2026-08-27-validation.json"
        ),
        "ascii_txt_pdf_byte_identical_to_source_and_clean_library": True,
        "topic_count": 29,
        "total_pdf_pages": 263,
    }
    data["exhaustive_changed_files_manifest"] = (
        "upsc-ai-kit\\manifests\\exports\\"
        "philosophy-paper-ii-socio-political-philosophy-04-learner-v2-g2-"
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
                "scoped to the 29 topics that do hold an exact clean package."
            ),
        },
        {
            "scope": "tools/test_export_four_item_library.py",
            "symptom": (
                "test_real_inventory_resolves_all_latest_topics fails with "
                "'philosophy-paper-ii-socio-political-philosophy-01 g2: "
                "standalone ASCII master is not the manually authored "
                "tracker-selected artifact.'"
            ),
            "relation_to_this_topic": (
                "None. It is the same pre-existing topic-01 stricter "
                "refreshed-contract and ASCII metadata defect, reported here "
                "plainly rather than repaired."
            ),
            "action_taken": (
                "Not repaired, as instructed. The five targeted suites that do "
                "cover this topic ran clean at 81 tests."
            ),
        },
    ]
    data["standalone_revalidation"] = {
        "command": (
            "python tools\\validate_v2_export.py "
            "upsc-ai-kit\\knowledge\\Philosophy\\learning-sessions\\v2\\"
            "paper-ii-socio-political-philosophy\\"
            "philosophy-paper-ii-socio-political-philosophy-04_Learning-Session.md "
            "--topic-key philosophy-paper-ii-socio-political-philosophy-04 "
            "--ascii-spec upsc-ai-kit\\manifests\\retrofits\\ascii-panel-specs\\"
            "philosophy--paper-ii-socio-political-philosophy-04-ascii-2026-08-27.json "
            "--main-pdf notes\\Philosophy\\learning-session-v2\\"
            "paper-ii-socio-political-philosophy\\notes\\"
            "philosophy-paper-ii-socio-political-philosophy-04_Learning-Session_"
            "2026-08-27.pdf "
            "--workbook notes\\Philosophy\\learning-session-v2\\"
            "paper-ii-socio-political-philosophy\\workbooks\\"
            "philosophy-paper-ii-socio-political-philosophy-04_Solved-Workbook_"
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
        "tests_run": 81,
        "result": "OK",
    }
    data["rendered_visual_inspection"]["state"] = (
        "generated and inspected page by page; the main, workbook and ASCII "
        "contact sheets, the graphical master overview and the tiled crops were "
        "reviewed for wrapping, arrow correspondence, complete matrix rows, "
        "blank/clipped pages and legacy navigation"
    )
    data["rendered_visual_inspection"]["repairs"] = [
        "Trimmed the populism, territorial-design and answer-spine ASCII panels "
        "so that every panel clears the landscape ASCII page frame with margin "
        "rather than filling it exactly.",
        "Authored explicit graphical stage groups, sequences and the three "
        "comparison matrices (Aristotle's six-fold grid, the two monarchies and "
        "the Weberian authority typology) so that no matrix row is auto-derived "
        "or truncated mid-clause.",
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
