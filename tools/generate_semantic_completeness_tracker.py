"""Generate and maintain the crash-resumable knowledge completeness tracker."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
REVIEW_DIR = ROOT / "upsc-ai-kit" / "manifests" / "reviews"
STATE_PATH = REVIEW_DIR / "knowledge-semantic-completeness-status.json"
TRACKER_PATH = ROOT / "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md"
PLAN_PATH = ROOT / "KNOWLEDGE-SEMANTIC-COMPLETENESS-PLAN.md"

GOAL = (
    "No gaps, no missing data, no missing topic, and no missing subject. "
    "Every catalogue topic must pass a hostile semantic-completeness review."
)

ALLOWED_STATUSES = (
    "pending",
    "in_progress",
    "changes_required",
    "repair_in_progress",
    "revalidation_pending",
    "passed",
    "blocked",
)

CHECK_NAMES = (
    "literal_syllabus",
    "implied_prerequisites",
    "textbook_taxonomy",
    "pyq_demands",
    "hostile_absence_search",
    "canonical_owner",
    "cross_owner_boundaries",
    "answer_architecture",
    "factual_verification",
    "dependent_artifacts",
)

SUBJECT_PRIORITY = {"Philosophy": 0}
PHILOSOPHY_SECTION_PRIORITY = {
    "paper-i-indian-philosophy": 0,
    "paper-i-western-philosophy": 1,
    "paper-ii-socio-political-philosophy": 2,
    "paper-ii-philosophy-of-religion": 3,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def subject_sort_key(topic: dict) -> tuple[int, int, str]:
    subject = topic["subject"]
    return (
        SUBJECT_PRIORITY.get(subject["key"], 1),
        int(subject["order"]),
        subject["key"],
    )


def topic_sort_key(topic: dict) -> tuple:
    subject = topic["subject"]
    section = topic["section"]
    if subject["key"] == "Philosophy":
        section_order = PHILOSOPHY_SECTION_PRIORITY.get(
            section["key"], int(section["order"]) + 10
        )
    else:
        section_order = int(section["order"])
    return (
        *subject_sort_key(topic),
        section_order,
        int(topic["topic_order"]),
        topic["topic_key"],
    )


def new_topic_state(topic: dict, global_order: int) -> dict:
    subject = topic["subject"]
    section = topic["section"]
    return {
        "global_order": global_order,
        "subject_key": subject["key"],
        "subject": subject["display_name"],
        "section_key": section["key"],
        "section": section["name"],
        "topic_key": topic["topic_key"],
        "topic_order": topic["topic_order"],
        "title": topic["display_title"],
        "source_basic": topic["source_basic"],
        "source_canonical": topic["source_canonical"],
        "source_advanced": topic["source_advanced"],
        "syllabus_sources": topic["syllabus_sources"],
        "index_sources": topic["index_sources"],
        "status": "pending",
        "checks": {name: "pending" for name in CHECK_NAMES},
        "gap_counts": {
            "missing_topics": 0,
            "missing_data": 0,
            "missing_concepts": 0,
            "missing_pyq_demands": 0,
            "misowned_content": 0,
            "factual_risks": 0,
        },
        "findings": [],
        "files_changed": [],
        "reviewed_at": None,
        "completed_at": None,
        "next_action": "Build the four-ledger coverage matrix and run hostile absence search.",
        "command": (
            "Review semantic completeness topic: "
            f"{subject['display_name']} — {section['name']} — {topic['display_title']}"
        ),
    }


def merge_topic_state(fresh: dict, previous: dict | None) -> dict:
    if previous is None:
        return fresh
    preserved = (
        "status",
        "checks",
        "gap_counts",
        "findings",
        "files_changed",
        "reviewed_at",
        "completed_at",
        "next_action",
    )
    for field in preserved:
        if field in previous:
            fresh[field] = previous[field]
    fresh["checks"] = {
        name: fresh["checks"].get(name, "pending") for name in CHECK_NAMES
    }
    if fresh["status"] not in ALLOWED_STATUSES:
        raise ValueError(
            f"Invalid status for {fresh['topic_key']}: {fresh['status']}"
        )
    return fresh


def load_previous_topics() -> dict[str, dict]:
    if not STATE_PATH.exists():
        return {}
    state = read_json(STATE_PATH)
    return {topic["topic_key"]: topic for topic in state.get("topics", [])}


def subject_command(subject: str) -> str:
    return (
        f"Run semantic-completeness review: {subject} — "
        "all topics sequentially"
    )


def derive_subjects(topics: list[dict]) -> list[dict]:
    subjects: list[dict] = []
    seen: dict[str, dict] = {}
    for topic in topics:
        key = topic["subject_key"]
        if key not in seen:
            row = {
                "order": len(subjects) + 1,
                "subject_key": key,
                "subject": topic["subject"],
                "status": "pending",
                "topic_count": 0,
                "passed": 0,
                "next_topic_key": None,
                "next_topic": None,
                "command": subject_command(topic["subject"]),
            }
            seen[key] = row
            subjects.append(row)
        row = seen[key]
        row["topic_count"] += 1
        if topic["status"] == "passed":
            row["passed"] += 1
        elif row["next_topic_key"] is None:
            row["next_topic_key"] = topic["topic_key"]
            row["next_topic"] = topic["title"]

    for row in subjects:
        subject_topics = [
            topic for topic in topics if topic["subject_key"] == row["subject_key"]
        ]
        statuses = {topic["status"] for topic in subject_topics}
        if statuses == {"passed"}:
            row["status"] = "passed"
        elif "blocked" in statuses:
            row["status"] = "blocked"
        elif statuses & {
            "in_progress",
            "changes_required",
            "repair_in_progress",
            "revalidation_pending",
        }:
            row["status"] = "in_progress"
        else:
            row["status"] = "pending"
    return subjects


def build_state(catalog: dict) -> dict:
    if catalog["statistics"]["ambiguous_or_unresolved_entries"] != 0:
        raise ValueError("Topic catalogue contains unresolved entries.")
    previous = load_previous_topics()
    ordered = sorted(catalog["topics"], key=topic_sort_key)
    topics = [
        merge_topic_state(new_topic_state(topic, index), previous.get(topic["topic_key"]))
        for index, topic in enumerate(ordered, 1)
    ]
    if len(topics) != catalog["statistics"]["topics"]:
        raise ValueError("Topic count does not match catalogue statistics.")
    if len({topic["topic_key"] for topic in topics}) != len(topics):
        raise ValueError("Duplicate topic keys found in semantic review state.")

    subjects = derive_subjects(topics)
    if len(subjects) != catalog["statistics"]["subjects"]:
        raise ValueError("Subject count does not match catalogue statistics.")

    status_counts = Counter(topic["status"] for topic in topics)
    next_topic = next((topic for topic in topics if topic["status"] != "passed"), None)
    active_subject = next(
        (subject for subject in subjects if subject["status"] != "passed"), None
    )
    return {
        "$schema": "knowledge-semantic-completeness-status-v1",
        "schema_version": 1,
        "generated_at": now_iso(),
        "goal": GOAL,
        "catalog": {
            "path": str(CATALOG.relative_to(ROOT)).replace("/", "\\"),
            "sha256": sha256(CATALOG),
            "subjects": catalog["statistics"]["subjects"],
            "sections": catalog["statistics"]["sections"],
            "topics": catalog["statistics"]["topics"],
            "unresolved": catalog["statistics"]["ambiguous_or_unresolved_entries"],
        },
        "policy": {
            "execution": "Exactly one subject and one topic may be active at a time.",
            "subject_order": "Philosophy first; remaining subjects follow catalogue order.",
            "philosophy_order": (
                "Indian Philosophy, Western Philosophy, Socio-Political Philosophy, "
                "Philosophy of Religion."
            ),
            "pass_gate": (
                "All ten checks must pass; every finding must be repaired, explicitly "
                "cross-owned, or documented as a verified non-gap."
            ),
            "source_order": [
                "Official syllabus and repository syllabus maps",
                "Canonical Basic Markdown owner",
                "Standard textbook taxonomy from OCR-searchable local PDFs",
                "Complete verified PYQ corpus",
                "Cross-topic and Advanced owners",
                "Live sources for current or changeable facts",
            ],
        },
        "commands": {
            "resume": (
                "Resume semantic-completeness review from "
                "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md"
            ),
            "status": "Show semantic-completeness review status",
            "next_topic": "Review next semantic-completeness topic",
            "refresh_shell": "python tools\\generate_semantic_completeness_tracker.py",
        },
        "statistics": {
            "subjects": len(subjects),
            "topics": len(topics),
            "status_counts": {
                status: status_counts.get(status, 0) for status in ALLOWED_STATUSES
            },
        },
        "active_subject": active_subject,
        "next_topic": next_topic,
        "subjects": subjects,
        "topics": topics,
    }


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_plan(state: dict) -> str:
    return f"""# Knowledge Semantic-Completeness Review Plan

> **Goal:** {GOAL}
>
> Authoritative state: `upsc-ai-kit\\manifests\\reviews\\knowledge-semantic-completeness-status.json`
>
> Human tracker: `KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md`

## Non-negotiable execution policy

1. Review exactly one subject at a time.
2. Within that subject, review exactly one topic at a time in tracker order.
3. Do not open the next topic until the current topic is passed or explicitly blocked.
4. Do not open the next subject until every topic in the current subject is passed.
5. Existing audit, export or PDF validation is evidence only; it is never proof of semantic completeness.
6. Repair the canonical knowledge owner before regenerating any dependent learning session, workbook, flowchart or PDF.
7. Preserve unrelated working-tree changes and commit only explicitly requested scopes.

## Completeness model

Every topic must be checked against four independently constructed ledgers:

1. **Literal syllabus ledger** — every noun, qualifier, relationship and directive in the official syllabus.
2. **Implied-prerequisite ledger** — concepts without which the printed syllabus cannot be understood or answered.
3. **Textbook-taxonomy ledger** — standard subtopics, classifications, debates, exceptions and terminology from local OCR-searchable books.
4. **PYQ-demand ledger** — every verified Prelims, Mains, CSAT or Philosophy Optional demand routed to the topic.

The hostile review must then search for what is absent rather than merely confirming what is present.

## Ten mandatory topic checks

| Check | Pass requirement |
|---|---|
| Literal syllabus | Every printed term and relationship is substantively taught |
| Implied prerequisites | No indispensable bridge doctrine or background mechanism is absent |
| Textbook taxonomy | Standard classifications, stages, schools, thinkers and exceptions are represented |
| PYQ demands | Every routed demand can be answered from the canonical owner |
| Hostile absence search | Synonyms and likely missing families were actively searched |
| Canonical owner | Basic/Core file contains all marks-essential material |
| Cross-owner boundaries | Cross-owned material has an explicit owner and usable link |
| Answer architecture | Definition, mechanism, evidence, objections, replies and verdict are executable |
| Factual verification | Changeable claims are current, sourced and correctly qualified |
| Dependent artifacts | Sessions, workbooks, diagrams and exports agree with the repaired owner |

## Topic workflow

```text
Freeze current state
        ↓
Read syllabus and owner
        ↓
Build four ledgers independently
        ↓
Run hostile absence search
        ↓
Record confirmed gaps and ownership conflicts
        ↓
Repair canonical Basic/Core owner
        ↓
Revalidate PYQs, arguments, facts and answer architecture
        ↓
Regenerate dependent artifacts only if required
        ↓
Update JSON state and regenerate tracker
        ↓
Pass topic → unlock next topic
```

## Subject completion gate

A subject passes only when:

- its topic count exactly matches the catalogue;
- every topic has passed all ten checks;
- no unresolved syllabus term, prerequisite, textbook family or PYQ remains;
- no marks-essential material exists only in Advanced;
- all cross-owned material has a named owner;
- factual-risk and gap ledgers contain no unhandled item;
- changed dependent artifacts have been regenerated and validated;
- the subject report lists all reviewed topics, findings and changed files.

## Crash recovery

1. Start Copilot in the repository root.
2. Send:

   `Resume semantic-completeness review from KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md`

3. The agent must read the Markdown tracker and machine-readable JSON before taking action.
4. The first non-passed topic in JSON is the only permitted next topic.
5. After every topic status change, run:

   `python tools\\generate_semantic_completeness_tracker.py`

6. Never reconstruct progress from conversation memory alone.

## State meanings

| Status | Meaning |
|---|---|
| `pending` | Not yet reviewed under this semantic standard |
| `in_progress` | Four-ledger and hostile review is active |
| `changes_required` | Confirmed gaps exist |
| `repair_in_progress` | Canonical owner is being repaired |
| `revalidation_pending` | Repair complete; gates not yet rerun |
| `passed` | All ten checks passed and findings resolved |
| `blocked` | Verification cannot continue; reason must be recorded |
"""


def render_tracker(state: dict) -> str:
    counts = state["statistics"]["status_counts"]
    active = state["active_subject"]
    next_topic = state["next_topic"]
    lines = [
        "# Knowledge Semantic-Completeness Review Tracker",
        "",
        f"> **Goal:** {GOAL}",
        ">",
        "> Machine-readable state: "
        "`upsc-ai-kit\\manifests\\reviews\\knowledge-semantic-completeness-status.json`",
        ">",
        "> Detailed method: `KNOWLEDGE-SEMANTIC-COMPLETENESS-PLAN.md`",
        "",
        "## Resume after interruption",
        "",
        "Copy and send this exact command:",
        "",
        "`Resume semantic-completeness review from "
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md`",
        "",
        "The agent must read this tracker and the JSON state, then continue from the "
        "first non-passed topic. Conversation history is not authoritative.",
        "",
        "## Current state",
        "",
        f"- Subjects: **{state['statistics']['subjects']}**",
        f"- Topics: **{state['statistics']['topics']}**",
        f"- Pending: **{counts['pending']}**",
        f"- In progress: **{counts['in_progress']}**",
        f"- Changes required: **{counts['changes_required']}**",
        f"- Repair in progress: **{counts['repair_in_progress']}**",
        f"- Revalidation pending: **{counts['revalidation_pending']}**",
        f"- Passed: **{counts['passed']}**",
        f"- Blocked: **{counts['blocked']}**",
        (
            f"- Active subject: **{active['subject']}**"
            if active
            else "- Active subject: **All subjects passed**"
        ),
        (
            f"- Next topic: **{next_topic['subject']} — {next_topic['section']} — "
            f"{next_topic['title']}** (`{next_topic['topic_key']}`)"
            if next_topic
            else "- Next topic: **None**"
        ),
        "",
        "## Quick commands",
        "",
        "- Status: `Show semantic-completeness review status`",
        "- Next topic only: `Review next semantic-completeness topic`",
        "- Resume: `Resume semantic-completeness review from "
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md`",
        "- Refresh tracker: `python tools\\generate_semantic_completeness_tracker.py`",
        "",
        "## Subject order and copy-ready commands",
        "",
        "| Order | Subject | Topics | Passed | Status | Next topic | Copy-ready command |",
        "|---:|---|---:|---:|---|---|---|",
    ]
    for subject in state["subjects"]:
        lines.append(
            "| {order} | {subject} | {topic_count} | {passed} | {status} | "
            "{next_topic} | `{command}` |".format(
                order=subject["order"],
                subject=markdown_escape(subject["subject"]),
                topic_count=subject["topic_count"],
                passed=subject["passed"],
                status=subject["status"],
                next_topic=markdown_escape(subject["next_topic"] or "Complete"),
                command=markdown_escape(subject["command"]),
            )
        )

    lines.extend(
        [
            "",
            "## Complete topic queue",
            "",
            "Use one exact topic command at a time. A later row remains locked until "
            "every earlier row in its subject has passed.",
            "",
            "| # | Subject | Section | Topic key and title | Status | Next action | "
            "Copy-ready command |",
            "|---:|---|---|---|---|---|---|",
        ]
    )
    for topic in state["topics"]:
        lines.append(
            "| {global_order} | {subject} | {section} | `{topic_key}` — {title} | "
            "{status} | {next_action} | `{command}` |".format(
                global_order=topic["global_order"],
                subject=markdown_escape(topic["subject"]),
                section=markdown_escape(topic["section"]),
                topic_key=topic["topic_key"],
                title=markdown_escape(topic["title"]),
                status=topic["status"],
                next_action=markdown_escape(topic["next_action"]),
                command=markdown_escape(topic["command"]),
            )
        )
    lines.extend(
        [
            "",
            "## Per-topic completion record",
            "",
            "Detailed check states, findings, gap counts, timestamps and changed files "
            "are stored under each topic in the machine-readable JSON. This Markdown "
            "file is regenerated from that state and must not become a competing source "
            "of truth.",
            "",
        ]
    )
    return "\n".join(lines)


def update_topic(
    state: dict,
    topic_key: str,
    status: str,
    note: str | None,
    changed_files: list[str],
) -> None:
    if status not in ALLOWED_STATUSES:
        raise ValueError(f"Status must be one of: {', '.join(ALLOWED_STATUSES)}")
    topic = next(
        (candidate for candidate in state["topics"] if candidate["topic_key"] == topic_key),
        None,
    )
    if topic is None:
        raise ValueError(f"Unknown topic key: {topic_key}")
    previous_status = topic["status"]
    topic["status"] = status
    topic["reviewed_at"] = topic["reviewed_at"] or now_iso()
    if status == "passed":
        for check in topic["checks"]:
            topic["checks"][check] = "passed"
        topic["completed_at"] = now_iso()
        topic["next_action"] = "Complete."
    else:
        topic["completed_at"] = None
        if previous_status == "passed":
            for check in topic["checks"]:
                topic["checks"][check] = "pending"
        if status == "blocked":
            topic["next_action"] = note or "Resolve documented blocker."
        elif note:
            topic["next_action"] = note
    if note:
        topic["findings"].append(
            {"recorded_at": now_iso(), "status": status, "note": note}
        )
    for path in changed_files:
        if path not in topic["files_changed"]:
            topic["files_changed"].append(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic-key")
    parser.add_argument("--status", choices=ALLOWED_STATUSES)
    parser.add_argument("--note")
    parser.add_argument("--changed-file", action="append", default=[])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    catalog = read_json(CATALOG)
    state = build_state(catalog)
    if args.topic_key or args.status:
        if not args.topic_key or not args.status:
            raise ValueError("--topic-key and --status must be supplied together.")
        update_topic(
            state,
            args.topic_key,
            args.status,
            args.note,
            args.changed_file,
        )
        previous = {topic["topic_key"]: topic for topic in state["topics"]}
        ordered = sorted(catalog["topics"], key=topic_sort_key)
        state = build_state(catalog)
        state["topics"] = [
            merge_topic_state(new_topic_state(topic, index), previous[topic["topic_key"]])
            for index, topic in enumerate(ordered, 1)
        ]
        state["subjects"] = derive_subjects(state["topics"])
        state["statistics"]["status_counts"] = {
            status: Counter(topic["status"] for topic in state["topics"]).get(status, 0)
            for status in ALLOWED_STATUSES
        }
        state["active_subject"] = next(
            (subject for subject in state["subjects"] if subject["status"] != "passed"),
            None,
        )
        state["next_topic"] = next(
            (topic for topic in state["topics"] if topic["status"] != "passed"),
            None,
        )

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    PLAN_PATH.write_text(render_plan(state), encoding="utf-8")
    TRACKER_PATH.write_text(render_tracker(state), encoding="utf-8")
    print(
        f"Generated {TRACKER_PATH.relative_to(ROOT)} with "
        f"{state['statistics']['subjects']} subjects and "
        f"{state['statistics']['topics']} topics."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
