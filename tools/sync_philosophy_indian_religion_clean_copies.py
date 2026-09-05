"""Synchronize only the 15 repaired clean-library and Flow-Learning copies."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
from pathlib import Path

import export_flow_learning_library as flow
import export_four_item_library as library
import philosophy_indian_religion_deep_quality_repair as repair


ROOT = Path(__file__).resolve().parents[1]
FINAL_ROOT = ROOT / "notes" / "Final-Learning-Packages"
FLOW_ROOT = ROOT / "notes" / "Flow-Learning" / "Philosophy Optional"
FLOW_INDEX = FLOW_ROOT / "INDIAN-AND-RELIGION-INDEX.md"


class SyncError(RuntimeError):
    """Raised when a scoped clean copy cannot be swapped safely."""


def swap_directory(stage: Path, destination: Path) -> None:
    digest = hashlib.sha256(str(destination).encode("utf-8")).hexdigest()[:12]
    backup = ROOT / ".agent-scratch" / "swap-backups" / digest
    if backup.exists():
        raise SyncError(f"Stale backup exists: {backup}")
    backup.parent.mkdir(parents=True, exist_ok=True)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        destination.rename(backup)
    try:
        stage.rename(destination)
    except Exception:
        if backup.exists():
            backup.rename(destination)
        raise
    shutil.rmtree(backup, ignore_errors=True)


def flow_readme(
    selection: library.ExportSelection,
    pdf_name: str,
    txt_name: str,
) -> str:
    return (
        "PHILOSOPHY FLOW LEARNING\n"
        "========================\n\n"
        f"Topic: {selection.catalogue.title}\n"
        f"Section: {selection.catalogue.section}\n"
        f"Source record ID: {selection.record['record_id']}\n"
        f"Source generation: {selection.record['generation']}\n"
        "Approval: Approval pending\n\n"
        f"Printable ASCII flow PDF: {pdf_name}\n"
        f"Authored ASCII flow text: {txt_name}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not args.apply:
        parser.error("Pass --apply.")
    selections = library.resolve_selections(
        ROOT,
        repair.STATUS_PATH,
        library.DEFAULT_CATALOGUE,
        selected_keys=list(repair.TOPIC_KEYS),
    )
    if len(selections) != 15:
        raise SyncError(f"Expected 15 selections, found {len(selections)}.")
    flow_rows = []
    for index, selection in enumerate(selections, 1):
        destination = FINAL_ROOT / selection.destination_relative
        stage = ROOT / ".agent-scratch" / "final-sync-stage" / f"{index:02d}"
        if stage.exists():
            shutil.rmtree(stage)
        stage.parent.mkdir(parents=True, exist_ok=True)
        try:
            library.prepare_topic_stage(
                ROOT,
                selection,
                stage,
                full_pdf_validation=True,
            )
            swap_directory(stage, destination)
        except Exception:
            shutil.rmtree(stage, ignore_errors=True)
            raise
        ascii_dir = destination / "04-ASCII-Master-Flowchart"
        source_pdf = ascii_dir / "ASCII-Master-Flowchart.pdf"
        source_txt = ascii_dir / "ASCII-Master-Flowchart.txt"
        folder_name = destination.name
        output_stem = flow.deterministic_output_stem(folder_name)
        flow_destination = FLOW_ROOT / folder_name
        flow_stage = ROOT / ".agent-scratch" / "flow-sync-stage" / f"{index:02d}"
        if flow_stage.exists():
            shutil.rmtree(flow_stage)
        flow_stage.parent.mkdir(parents=True, exist_ok=True)
        flow_stage.mkdir(parents=True)
        pdf_name = f"{output_stem}.pdf"
        txt_name = f"{output_stem}.txt"
        shutil.copy2(source_pdf, flow_stage / pdf_name)
        shutil.copy2(source_txt, flow_stage / txt_name)
        (flow_stage / "README.txt").write_text(
            flow_readme(selection, pdf_name, txt_name),
            encoding="utf-8",
            newline="\n",
        )
        swap_directory(flow_stage, flow_destination)
        flow_rows.append(
            (
                selection.catalogue.section,
                selection.catalogue.number,
                selection.catalogue.title,
                folder_name,
                pdf_name,
                txt_name,
            )
        )
    FLOW_ROOT.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Philosophy Flow Learning — Indian Philosophy and Philosophy of Religion",
        "",
        "Scoped, byte-synchronised ASCII flow copies for the 15 repaired active learner-v2 packages.",
        "",
        "| Section | No. | Topic | PDF | TXT |",
        "|---|---:|---|---|---|",
    ]
    for section, number, title, folder, pdf_name, txt_name in flow_rows:
        lines.append(
            f"| {section} | {number or ''} | {title} | "
            f"[PDF]({folder}/{pdf_name}) | [TXT]({folder}/{txt_name}) |"
        )
    FLOW_INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"final_topics={len(selections)} flow_topics={len(flow_rows)}")
    print(f"flow_index={FLOW_INDEX.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
