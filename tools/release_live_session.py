"""Fail-fast release automation for one validated live-session topic."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from validate_live_session import ROOT, ValidationFailure, validate


TRAILERS = [
    "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>",
    "Copilot-Session: 997f5bd4-ce48-4df1-8d71-68989c4ce262",
]


def matching_index_rows(index_raw: str, topic: Path, index: Path) -> list[str]:
    root_relative = topic.relative_to(ROOT).as_posix()
    index_relative = topic.relative_to(index.parent).as_posix()
    accepted_links = {f"({root_relative})", f"({index_relative})"}
    return [
        line
        for line in index_raw.splitlines()
        if any(link in line for link in accepted_links)
    ]


def run(*args: str, capture: bool = False) -> str:
    completed = subprocess.run(
        list(args),
        cwd=ROOT,
        capture_output=capture,
        text=True,
        check=False,
    )
    if completed.returncode:
        output = (completed.stdout or "") + (completed.stderr or "")
        raise ValidationFailure(f"`{' '.join(args)}` failed:\n{output}")
    return (completed.stdout or "").strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", type=Path)
    parser.add_argument("--index", type=Path, default=Path("live_sessions/INDEX.md"))
    parser.add_argument("--commit-title", required=True)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Commit and push. Without this flag, perform a release preflight only.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        topic = (
            (ROOT / args.topic).resolve()
            if not args.topic.is_absolute()
            else args.topic.resolve()
        )
        index = (
            (ROOT / args.index).resolve()
            if not args.index.is_absolute()
            else args.index.resolve()
        )
        try:
            topic.relative_to(ROOT)
            index.relative_to(ROOT)
        except ValueError as error:
            raise ValidationFailure(
                "topic and index paths must be inside the repository"
            ) from error
        result = validate(topic)
        topic_rel = topic.relative_to(ROOT).as_posix()
        index_rel = index.relative_to(ROOT).as_posix()
        index_raw = index.read_text(encoding="utf-8")
        matching_rows = matching_index_rows(index_raw, topic, index)
        if len(matching_rows) != 1:
            raise ValidationFailure(
                f"index must contain exactly one row linking ({topic_rel})"
            )
        row = matching_rows[0]
        if f"`{result.sha256[:12]}`" not in row:
            raise ValidationFailure("index row does not contain current 12-character hash")
        if f"| {result.words:,} |" not in row:
            raise ValidationFailure("index row does not contain current word count")

        staged_before = run("git", "diff", "--cached", "--name-only", capture=True)
        if staged_before:
            raise ValidationFailure(
                "release requires an empty staging area; found:\n" + staged_before
            )
        run("git", "diff", "--check", "--", topic_rel, index_rel)
        print(
            f"PREFLIGHT PASS: {topic_rel} | {result.words:,} words | "
            f"{result.sha256[:12]}"
        )
        if not args.execute:
            print("DRY RUN: pass --execute to stage, commit, push and verify parity.")
            return 0

        branch = args.branch or run(
            "git", "branch", "--show-current", capture=True
        )
        if not branch:
            raise ValidationFailure("cannot release from detached HEAD")
        run("git", "add", "--", topic_rel, index_rel)
        staged_after = set(
            filter(
                None,
                run("git", "diff", "--cached", "--name-only", capture=True).splitlines(),
            )
        )
        expected = {topic_rel, index_rel}
        if staged_after != expected:
            raise ValidationFailure(
                f"staged files must be exactly {sorted(expected)}, found "
                f"{sorted(staged_after)}"
            )
        run("git", "diff", "--cached", "--check")
        commit_args = ["git", "commit", "-m", args.commit_title]
        for trailer in TRAILERS:
            commit_args.extend(["-m", trailer])
        run(*commit_args)
        run("git", "push", args.remote, branch)
        run("git", "fetch", args.remote, branch, "--quiet")
        parity = run(
            "git",
            "rev-list",
            "--left-right",
            "--count",
            f"HEAD...{args.remote}/{branch}",
            capture=True,
        )
        if parity.split() != ["0", "0"]:
            raise ValidationFailure(f"remote parity is not 0/0: {parity}")
        commit = run("git", "rev-parse", "--short=9", "HEAD", capture=True)
        print(f"RELEASED: {commit} | parity 0/0")
        return 0
    except (OSError, UnicodeError, subprocess.SubprocessError, ValidationFailure) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
