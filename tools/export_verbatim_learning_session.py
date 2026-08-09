"""Export the taught learning-session text from a Copilot events.jsonl file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_events(path: Path) -> list[dict]:
    events = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


def is_session_message(content: str) -> bool:
    return (
        content.startswith("# Notions of God — Learning Roadmap")
        or content.startswith("✅ **Subtopic ")
        or content.startswith("✅ **Learning session complete:")
    )


def choice_lines(choices: list[str]) -> str:
    return "\n".join(
        f"{chr(ord('A') + index)}. {choice}"
        for index, choice in enumerate(choices)
    )


def export(events_path: Path, output_path: Path) -> None:
    sections: list[str] = []

    for event in load_events(events_path):
        event_type = event.get("type")
        data = event.get("data", {})

        if event_type == "assistant.message":
            content = data.get("content", "")
            if is_session_message(content):
                sections.append(content.strip())
            continue

        if (
            event_type == "tool.execution_start"
            and data.get("toolName") == "ask_user"
        ):
            arguments = data.get("arguments", {})
            question = str(arguments.get("question", "")).strip()
            if not question:
                continue
            choices = arguments.get("choices") or []
            if choices:
                question = f"{question}\n\n{choice_lines(choices)}"
            sections.append(question)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n---\n\n".join(sections) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("events", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    export(args.events, args.output)
    print(f"Markdown saved: {args.output}")


if __name__ == "__main__":
    main()
