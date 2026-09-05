"""Print the consolidated proof table for the Social Justice 13-17 batch."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BATCH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "social-justice-13-17-sequential-batch-2026-09-02-completion.json"
)


def main() -> int:
    payload = json.loads(BATCH.read_text(encoding="utf-8"))
    header = (
        f"{'topic':18}{'gates':7}{'facts':6}{'sess':5}{'vis':4}{'mcq':5}"
        f"{'A/B/C/D':12}{'mains':24}{'ascii':6}{'stg':4}{'notes':6}{'wb':4}"
        f"{'reg-last':9}"
    )
    print(header)
    for topic in payload["topics"]:
        metrics = topic["metrics"]
        distribution = metrics["mcq_answer_distribution"]
        gates = f"{topic['hard_gates_passed']}/{topic['hard_gates_total']}"
        keys = "/".join(str(distribution[letter]) for letter in "ABCD")
        print(
            f"{topic['topic_key']:18}{gates:7}"
            f"{metrics['fact_anchor_count']:<6}"
            f"{metrics['learner_session_count']:<5}"
            f"{metrics['visual_first_count']:<4}"
            f"{metrics['mcq_count']:<5}{keys:12}"
            f"{str(metrics['original_mains_weights']):24}"
            f"{metrics['ascii_panel_count']:<6}"
            f"{metrics['graphical_stage_count']:<4}"
            f"{metrics['main_pdf_pages']:<6}"
            f"{metrics['workbook_pdf_pages']:<4}"
            f"{str(metrics['register_notes_last']):9}"
        )
    print()
    for topic in payload["topics"]:
        metrics = topic["metrics"]
        print(
            f"{topic['topic_key']}: final H2 = {metrics['h2_sequence'][-1]}; "
            f"unique stems = {metrics['mcq_unique_stem_count']}; "
            f"workbook mirrors = {metrics['workbook_mcq_count']}; "
            f"approved = {topic['approved']}; result = {topic['result']}"
        )
    print()
    print("shared ASCII coverage:", json.dumps(payload["shared_ascii_coverage"]))
    print("aggregate:", json.dumps(payload["aggregate"]))
    print("batch result:", payload["result"], "errors:", payload["errors"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
