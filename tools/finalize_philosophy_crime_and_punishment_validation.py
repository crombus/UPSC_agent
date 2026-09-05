"""One-off finaliser: record publication, revalidation and unrelated failures.

Updates the Crime and Punishment learner-v2 g2 validation manifest with the
clean-library and Flow-Learning publication results, the standalone
revalidation, the targeted test-suite result, the rendered visual inspection
outcome and the known unrelated failures that this task must not repair.
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
    / "philosophy-paper-ii-socio-political-philosophy-07-learner-v2-g2-"
    "2026-08-27-validation.json"
)


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    data["clean_library_publication"] = {
        "state": "published",
        "destination": (
            "notes\\Final-Learning-Packages\\Philosophy Optional\\"
            "Philosophy Paper II \u2014 Socio-Political Philosophy\\"
            "07-Crime-and-Punishment"
        ),
        "command": (
            "python tools\\export_four_item_library.py --topic-key "
            "philosophy-paper-ii-socio-political-philosophy-07 --manifest-date "
            "2026-08-27-philosophy-socio-political-07-g2"
        ),
        "manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "final-four-item-library-2026-08-27-philosophy-socio-political-07-g2.json"
        ),
        "validation_manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "final-four-item-library-2026-08-27-philosophy-socio-political-07-g2"
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
        "note": (
            "The export was scoped to this single topic key, so the undated "
            "shared manifest pair final-four-item-library-2026-08-27.json and "
            "its validation file were not rewritten by this run; the "
            "authoritative pair for this topic is the dated one named above."
        ),
    }
    data["flow_learning_publication"] = {
        "state": "published",
        "destination": (
            "notes\\Flow-Learning\\Philosophy Optional\\07-Crime-and-Punishment"
        ),
        "command": (
            "python tools\\export_flow_learning_library.py --subject "
            '"Philosophy Optional" --topic-prefix philosophy- --topics '
            "<32 explicit topic keys> --expected-topic-count 32 "
            "--manifest-date 2026-08-27-philosophy-socio-political-07-g2"
        ),
        "scope": (
            "32 validated Philosophy Optional learner-v2 topics that hold an "
            "exact clean package, including this topic. The publication was "
            "scoped with an explicit topic list because Socio-Political topic "
            "01 carries a pre-existing, unrelated clean-package identity "
            "defect that this task deliberately does not repair."
        ),
        "report": (
            "notes\\Flow-Learning\\"
            "PHILOSOPHY-OPTIONAL-SOCIO-POLITICAL-07-FLOW-LEARNING-REPORT.md"
        ),
        "validation_manifest": (
            "upsc-ai-kit\\manifests\\exports\\"
            "philosophy-paper-ii-socio-political-philosophy-07-flow-learning-g2"
            "-2026-08-27-validation.json"
        ),
        "ascii_txt_pdf_byte_identical_to_source_and_clean_library": True,
        "ascii_master_pdf_sha256": (
            "31c5a6dbc18f86cdd3307280e5538ef15207042c3b0815376c12ad8abe0fbb7d"
        ),
        "ascii_master_txt_sha256": (
            "2b37768da80ba00ddc6469ab67bc63b50f88a90916d9f8649e27b23c46f9b42b"
        ),
        "topic_count": 32,
        "total_pdf_pages": 295,
    }
    data["exhaustive_changed_files_manifest"] = (
        "upsc-ai-kit\\manifests\\exports\\"
        "philosophy-paper-ii-socio-political-philosophy-07-learner-v2-g2-"
        "2026-08-27-exhaustive-changed-files.md"
    )
    data["known_unrelated_failures"] = [
        {
            "scope": "philosophy-paper-ii-socio-political-philosophy-01",
            "symptom": (
                "tools/export_flow_learning_library.py and "
                "tools/export_four_item_library.py abort with "
                "'philosophy-paper-ii-socio-political-philosophy-01 g2: "
                "standalone ASCII master is not the manually authored "
                "tracker-selected artifact' when the whole Philosophy Optional "
                "subject is exported without an explicit topic list."
            ),
            "relation_to_this_topic": (
                "None. The defect predates this run and belongs to the topic-01 "
                "stricter refreshed-contract and ASCII metadata work."
            ),
            "action_taken": (
                "Not repaired, as instructed. The clean-library export was "
                "scoped to this topic key, and the Flow-Learning publication "
                "was scoped to the 32 topics that do hold an exact clean "
                "package."
            ),
        },
        {
            "scope": "tools/test_export_four_item_library.py",
            "symptom": (
                "test_real_inventory_resolves_all_latest_topics fails with the "
                "same topic-01 message; the other six tests in that module "
                "pass."
            ),
            "relation_to_this_topic": (
                "None. It is the same pre-existing topic-01 defect, reported "
                "here plainly rather than repaired."
            ),
            "action_taken": (
                "Not repaired, as instructed. The five targeted suites that do "
                "cover this topic ran clean at 84 tests."
            ),
        },
    ]
    data["standalone_revalidation"] = {
        "command": (
            "python tools\\validate_v2_export.py "
            "upsc-ai-kit\\knowledge\\Philosophy\\learning-sessions\\v2\\"
            "paper-ii-socio-political-philosophy\\"
            "philosophy-paper-ii-socio-political-philosophy-07_Learning-Session.md "
            "--topic-key philosophy-paper-ii-socio-political-philosophy-07 "
            "--ascii-spec upsc-ai-kit\\manifests\\retrofits\\ascii-panel-specs\\"
            "philosophy--paper-ii-socio-political-philosophy-07-ascii-2026-08-27.json "
            "--main-pdf notes\\Philosophy\\learning-session-v2\\"
            "paper-ii-socio-political-philosophy\\notes\\"
            "philosophy-paper-ii-socio-political-philosophy-07_Learning-Session_"
            "2026-08-27.pdf "
            "--workbook notes\\Philosophy\\learning-session-v2\\"
            "paper-ii-socio-political-philosophy\\workbooks\\"
            "philosophy-paper-ii-socio-political-philosophy-07_Solved-Workbook_"
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
        "tests_run": 84,
        "result": "OK",
        "note": (
            "84 rather than 83 because this run adds "
            "test_crime_and_punishment_uses_strict_abcd_policy to "
            "tools/test_v2_export_foundation.py."
        ),
    }
    data["rendered_visual_inspection"]["state"] = (
        "generated and inspected page by page; the main, workbook and ASCII "
        "contact sheets, the graphical master overview and every tiled crop "
        "were reviewed for wrapping, arrow correspondence, complete matrix "
        "rows, label correspondence, blank/clipped pages and legacy navigation"
    )
    data["rendered_visual_inspection"]["repairs"] = [
        "Trimmed the corruption, genocide, capital-punishment and answer-spine "
        "ASCII panels to at most thirty-one body lines each so every panel "
        "clears the landscape page frame with margin; only redundant "
        "pipe-and-arrow separator pairs were collapsed and no doctrine was "
        "deleted.",
        "Replaced dot-leader alignment runs inside the deterrence and "
        "capital-punishment panels with dash rules, because ellipsis-shaped "
        "runs are rejected as truncation markers inside master nodes.",
        "Shortened the Session 3 Kant keyword and the Session 4 Bentham "
        "keyword, and reduced the Session 8 keyword bank from ten terms to "
        "eight, so that every must-write term stays a keyword rather than a "
        "compressed prose sentence.",
        "Rewrote the Session 6 and Session 10 how-to-use-them guidance so that "
        "it names the selected terms - general justifying aim, distribution "
        "and liability, amount and severity, side-constraint, Hart, the "
        "directive decoder, the four standing debates and the graded verdict - "
        "instead of paraphrasing around them.",
        "Authored twelve explicit graphical answer lines and mechanism strips "
        "rather than reusing the ten session lines, because this topic uses "
        "twelve master panels: corruption, mass violence and genocide each "
        "carry their own stage instead of sharing one crowded card.",
        "Authored the three graphical comparison matrices explicitly - the "
        "deterrence-against-incapacitation axis grid, the three-question grid "
        "with a fails-here column, and the expressive/communicative/"
        "restorative grid with an answer-side test row - so that no matrix row "
        "is auto-derived or truncated mid-clause.",
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
