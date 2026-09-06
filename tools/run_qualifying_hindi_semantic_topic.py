"""Run exactly one authoritative Qualifying Hindi semantic-completeness topic."""

from __future__ import annotations

import argparse
import json

import qualifying_hindi_semantic_runtime as runtime


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=range(1, 7), required=True)
    args = parser.parse_args()
    print(json.dumps(runtime.run_topic(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
