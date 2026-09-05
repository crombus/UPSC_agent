"""Remove partial Sovereignty learner-v2 generation targets before a clean re-run.

The reset is strictly scoped to Philosophy Paper II Socio-Political Philosophy
topic 02.  Topic 01 artifacts, every legacy-v1 package and all unrelated trees
are never touched.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-27"
SECTION_KEY = "paper-ii-socio-political-philosophy"
TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-02"
GENERATION = 2

TARGETS = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
    / f"{TOPIC_KEY}_Learning-Session.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
    / f"{TOPIC_KEY}_Solved-Workbook.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
    / "assets"
    / TOPIC_KEY,
    ROOT
    / "notes"
    / "Philosophy"
    / "learning-session-v2"
    / SECTION_KEY
    / "notes"
    / f"{TOPIC_KEY}_Learning-Session_{GENERATION_DATE}.pdf",
    ROOT
    / "notes"
    / "Philosophy"
    / "learning-session-v2"
    / SECTION_KEY
    / "workbooks"
    / f"{TOPIC_KEY}_Solved-Workbook_{GENERATION_DATE}.pdf",
    ROOT
    / "notes"
    / "Philosophy"
    / "learning-session-v2"
    / SECTION_KEY
    / "validation"
    / TOPIC_KEY,
    ROOT / "notes" / "Philosophy" / "flowcharts" / TOPIC_KEY,
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / f"philosophy--{SECTION_KEY}-02-ascii-{GENERATION_DATE}.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / f"philosophy--{SECTION_KEY}-content-specs"
    / f"{TOPIC_KEY}-g{GENERATION}.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / f"philosophy--{SECTION_KEY}-graphical-specs"
    / f"{TOPIC_KEY}-g{GENERATION}.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g{GENERATION}-{GENERATION_DATE}-record.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g{GENERATION}-{GENERATION_DATE}-validation.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
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
