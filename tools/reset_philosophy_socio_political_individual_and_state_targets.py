"""Remove partial Individual and State learner-v2 targets before a clean re-run.

The reset is strictly scoped to Philosophy Paper II Socio-Political Philosophy
topic 03.  Topics 01-02, every legacy-v1 package and all unrelated trees are
never touched.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-27"
SECTION_KEY = "paper-ii-socio-political-philosophy"
TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-03"
GENERATION = 2

KNOWLEDGE = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
)
NOTES = ROOT / "notes" / "Philosophy" / "learning-session-v2" / SECTION_KEY
MANIFESTS = ROOT / "upsc-ai-kit" / "manifests"

TARGETS = (
    KNOWLEDGE / f"{TOPIC_KEY}_Learning-Session.md",
    KNOWLEDGE / f"{TOPIC_KEY}_Solved-Workbook.md",
    KNOWLEDGE / "assets" / TOPIC_KEY,
    NOTES / "notes" / f"{TOPIC_KEY}_Learning-Session_{GENERATION_DATE}.pdf",
    NOTES / "workbooks" / f"{TOPIC_KEY}_Solved-Workbook_{GENERATION_DATE}.pdf",
    NOTES / "validation" / TOPIC_KEY,
    ROOT / "notes" / "Philosophy" / "flowcharts" / TOPIC_KEY,
    MANIFESTS
    / "retrofits"
    / "ascii-panel-specs"
    / f"philosophy--{SECTION_KEY}-03-ascii-{GENERATION_DATE}.json",
    MANIFESTS
    / "v2"
    / f"philosophy--{SECTION_KEY}-content-specs"
    / f"{TOPIC_KEY}-g{GENERATION}.json",
    MANIFESTS
    / "v2"
    / f"philosophy--{SECTION_KEY}-graphical-specs"
    / f"{TOPIC_KEY}-g{GENERATION}.json",
    MANIFESTS
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g{GENERATION}-{GENERATION_DATE}-record.json",
    MANIFESTS
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g{GENERATION}-{GENERATION_DATE}-validation.json",
    MANIFESTS
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g{GENERATION}-{GENERATION_DATE}-changed-files.txt",
)


def main() -> int:
    for target in TARGETS:
        if target.is_dir():
            shutil.rmtree(target)
            print(f"REMOVED TREE: {target.relative_to(ROOT)}")
        elif target.is_file():
            target.unlink()
            print(f"REMOVED FILE: {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
