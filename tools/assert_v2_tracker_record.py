"""Assert a finalized learner-v2 tracker record exists and remains unapproved."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record_id")
    args = parser.parse_args()

    tracker = json.loads((ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8"))
    matches = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict) and record.get("record_id") == args.record_id
    ]
    if len(matches) != 1:
        print(f"FAIL: expected exactly one {args.record_id}; found {len(matches)}.")
        return 1
    record = matches[0]
    if record.get("approved") is not False or record["approval"]["approved"] is not False:
        print(f"FAIL: {args.record_id} is not approved:false.")
        return 1
    pages: dict[str, int] = {}
    for field in ("main_pdf", "workbook", "markdown", "workbook_markdown"):
        path = ROOT / str(record[field])
        if not path.is_file():
            print(f"FAIL: missing artifact {field}: {path}")
            return 1
        if path.suffix == ".pdf":
            with fitz.open(path) as document:
                pages[field] = document.page_count
    print(
        json.dumps(
            {
                "record_id": record["record_id"],
                "variant": record["variant"],
                "generation": record["generation"],
                "supersedes": record["supersedes"],
                "approved": record["approved"],
                "pages": pages,
                "main_pdf": record["main_pdf"],
                "workbook": record["workbook"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
