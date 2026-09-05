"""Remove partial topic-11 learner-v2 generation targets before a clean re-run."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Paper-I-Western-Philosophy"
    / "learning-sessions"
    / "topic-11",
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Paper-I-Western-Philosophy"
    / "learning-sessions"
    / "topic-11",
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Paper-I-Western-Philosophy"
    / "flowcharts"
    / "topic-11",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "philosophy--paper-i-western-philosophy-11-ascii-2026-08-27.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-i-western-philosophy-content-specs"
    / "philosophy-paper-i-western-philosophy-11-g2.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-i-western-philosophy-graphical-specs"
    / "philosophy-paper-i-western-philosophy-11-g2.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "philosophy-paper-i-western-philosophy-11-learner-v2-g2-2026-08-27-record.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "philosophy-paper-i-western-philosophy-11-learner-v2-g2-2026-08-27-validation.json",
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "philosophy-paper-i-western-philosophy-11-learner-v2-g2-2026-08-27-changed-files.txt",
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
