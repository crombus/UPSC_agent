"""Write the exhaustive changed-files manifest for the topic 6 run.

The manifest is topic-scoped: it lists every repository-relative file created or
modified while generating, validating and publishing
``philosophy-paper-ii-socio-political-philosophy-06:learner-v2:g2``, grouped by
role, with a SHA-256 for each entry.  Compiler caches, scratch directories and
temporary swap files are excluded, and no unrelated tree is inspected or
rewritten.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-27"
SECTION_KEY = "paper-ii-socio-political-philosophy"
TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-06"
RECORD_ID = f"{TOPIC_KEY}:learner-v2:g2"
OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g2-{GENERATION_DATE}-exhaustive-changed-files.md"
)

SCAN_ROOTS = ("notes", "upsc-ai-kit", "tools")
EXCLUDED = re.compile(
    r"(?:^|\\)__pycache__(?:\\|$)|(?:^|\\)\.agent-scratch(?:\\|$)|"
    r"(?:^|\\)_test_[^\\]+(?:\\|$)|\.pending$|\.pyc$"
)

GROUPS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "Tooling (generator, content spec, reset helper, finaliser, "
        "changed-files reporter, shared validator and test)",
        re.compile(r"^tools\\"),
    ),
    (
        "Reusable learner-v2 Markdown, workbook Markdown and concept visual",
        re.compile(r"^upsc-ai-kit\\knowledge\\Philosophy\\learning-sessions\\v2\\"),
    ),
    (
        "Rendered learning and workbook PDFs",
        re.compile(
            r"^notes\\Philosophy\\learning-session-v2\\[^\\]+\\(?:notes|workbooks)\\"
        ),
    ),
    (
        "Validation artifacts, visual audit maps and rendered contact sheets",
        re.compile(r"^notes\\Philosophy\\learning-session-v2\\[^\\]+\\validation\\"),
    ),
    (
        "Section coverage, notes-PDF and workbook-PDF indexes",
        re.compile(r"^notes\\Philosophy\\learning-session-v2\\[^\\]+\\indexes\\"),
    ),
    (
        "Graphical and ASCII master-flow package",
        re.compile(r"^notes\\Philosophy\\flowcharts\\"),
    ),
    (
        "Clean Final-Learning-Packages library",
        re.compile(r"^notes\\Final-Learning-Packages\\"),
    ),
    (
        "Flow-Learning library",
        re.compile(r"^notes\\Flow-Learning\\"),
    ),
    (
        "Manifests, specs, records and export reports",
        re.compile(r"^upsc-ai-kit\\manifests\\"),
    ),
    (
        "Refreshed learning-session command indexes",
        re.compile(r"^upsc-ai-kit\\knowledge\\.*LEARNING-SESSION-COMMAND-INDEX\.md$"),
    ),
    (
        "Repository trackers and command guides",
        re.compile(r"^[^\\]+$"),
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def collect(cutoff: datetime) -> list[str]:
    found: set[str] = set()
    for name in SCAN_ROOTS:
        base = ROOT / name
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if datetime.fromtimestamp(path.stat().st_mtime) <= cutoff:
                continue
            relative = str(path.relative_to(ROOT)).replace("/", "\\")
            if EXCLUDED.search(relative) or path == OUTPUT:
                continue
            found.add(relative)
    for path in ROOT.iterdir():
        if not path.is_file():
            continue
        if datetime.fromtimestamp(path.stat().st_mtime) <= cutoff:
            continue
        relative = str(path.relative_to(ROOT)).replace("/", "\\")
        if not EXCLUDED.search(relative):
            found.add(relative)
    return sorted(found, key=str.casefold)


def group_of(relative: str) -> str:
    for label, pattern in GROUPS:
        if pattern.search(relative):
            return label
    return "Other"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        required=True,
        help="ISO timestamp; only files modified after it are reported.",
    )
    args = parser.parse_args()
    cutoff = datetime.fromisoformat(args.since)
    entries = collect(cutoff)
    grouped: dict[str, list[str]] = {}
    for relative in entries:
        grouped.setdefault(group_of(relative), []).append(relative)

    lines = [
        f"# Exhaustive changed-files manifest — {RECORD_ID}",
        "",
        "- **Topic:** Philosophy Optional — Philosophy Paper II — "
        "Socio-Political Philosophy — Humanism, Secularism and Multiculturalism",
        f"- **Record identity:** `{RECORD_ID}` (supersedes "
        f"`{TOPIC_KEY}:legacy-v1:g1`)",
        f"- **Generation date:** {GENERATION_DATE}",
        "- **Official syllabus (verbatim):** Humanism; Secularism; "
        "Multi-culturalism.",
        "- **Approval:** false, pending explicit approval of this exact generation",
        f"- **Files created or modified:** {len(entries)}",
        "",
        "Every path below is repository-relative. Compiler caches, scratch "
        "directories, transient unit-test fixtures, temporary `.pending` swap "
        "files and this manifest itself are excluded. No unrelated tree was "
        "rewritten.",
        "",
    ]
    for label, _ in GROUPS:
        items = grouped.get(label)
        if not items:
            continue
        lines.extend([f"## {label}", "", "| # | Path | SHA-256 |", "|---|---|---|"])
        for number, relative in enumerate(items, 1):
            lines.append(f"| {number} | `{relative}` | `{sha256(ROOT / relative)}` |")
        lines.append("")
    other = grouped.get("Other")
    if other:
        lines.extend(["## Other", "", "| # | Path | SHA-256 |", "|---|---|---|"])
        for number, relative in enumerate(other, 1):
            lines.append(f"| {number} | `{relative}` | `{sha256(ROOT / relative)}` |")
        lines.append("")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT.with_suffix(OUTPUT.suffix + ".pending")
    pending.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    pending.replace(OUTPUT)
    print(
        f"WROTE: {OUTPUT.relative_to(ROOT)} ({len(entries)} files across "
        f"{len(grouped)} groups)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
