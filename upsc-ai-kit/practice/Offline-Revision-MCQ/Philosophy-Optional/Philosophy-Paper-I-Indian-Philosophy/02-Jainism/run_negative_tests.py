from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VALIDATOR = ROOT / "validate_package.py"
CASES = [
    ("missing-required", "README.md", None, "MISSING_REQUIRED_FILE"),
    ("destination-tamper", "FORMAL-SOURCE-MIRROR.md", ("anchor_append",), "DESTINATION_PAYLOAD_HASH_MISMATCH"),
    ("source-hash-tamper", "FORMAL-COVERAGE-REVIEW.json", ("replace", "de8b2c8fde2819b60c7a7f6a983300651082394fd6a434b5c832d6af3c2b6c90", "0" * 64), "SOURCE_HASH_MISMATCH"),
    ("semantic-excerpt-tamper", "FORMAL-COVERAGE-REVIEW.json", ("semantic_excerpt",), "SEMANTIC_PROPOSITION_QUALITY"),
    ("child-union-tamper", "FORMAL-COVERAGE-REVIEW.json", ("child_union",), "CHILD_UNION_MISMATCH"),
    ("segment-hash-tamper", "FORMAL-COVERAGE-REVIEW.json", ("segment_hash",), "LARGE_LEAF_SEGMENT_HASH"),
    ("mcq-mismatch", "MCQ-SOLUTIONS.md", ("replace", "## MCQ 1.", "## MCQ 1X."), "MCQ_SOLUTION_OPTIONS_MISMATCH"),
    ("mcq-severe-imbalance", "MCQ-SOLUTIONS.md", ("answer_sequence", "A" * 32), "MCQ_POSITION_IMBALANCE"),
    ("mcq-predictable-cycle", "MCQ-SOLUTIONS.md", ("answer_sequence", "ABCD" * 8), "MCQ_PREDICTABLE_CYCLE"),
    ("pyq-mutation", "ANSWER-WRITING-TOOLKIT.md", ("replace_all", "How do the Jaina philosophers explain 'bondage'?", "How do Jainas explain bondage?"), "PYQ_TEXT_MUTATION"),
    ("stale-pdf", "REVISION-GUIDE.md", ("append", "\nStale mutation.\n"), "STALE_PDF_OR_MANIFEST"),
]


def invoke(copy: Path, release: bool = False) -> tuple[int, dict]:
    cmd = [sys.executable, "-B", str(copy / "validate_package.py"), "--root", str(copy), "--check-only"]
    if release:
        cmd.append("--release")
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    p = subprocess.run(cmd, text=True, capture_output=True, env=env)
    try:
        data = json.loads(p.stdout)
    except Exception:
        data = {"errors": [{"code": "UNPARSEABLE", "detail": p.stdout + p.stderr}]}
    return p.returncode, data


def prepare(copy: Path) -> None:
    shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".negative-tests-work", "__pycache__", "*.pyc"))
    validation = copy / "VALIDATION.json"
    if not validation.exists():
        validation.write_text('{"state":"DEVELOPMENT_PASS","release_ready":false}\n', encoding="utf-8")


def main() -> int:
    work = ROOT / ".negative-tests-work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir()
    results = []
    try:
        for name, rel, mutation, expected in CASES:
            copy = work / name
            prepare(copy)
            target = copy / rel
            if mutation is None:
                target.unlink()
            else:
                text = target.read_text(encoding="utf-8")
                if mutation[0] == "replace":
                    text = text.replace(mutation[1], mutation[2], 1)
                elif mutation[0] == "replace_all":
                    text = text.replace(mutation[1], mutation[2])
                elif mutation[0] == "anchor_append":
                    review = json.loads((copy / "FORMAL-COVERAGE-REVIEW.json").read_text(encoding="utf-8"))
                    anchor = review["decisions"][0]["destination"]["anchor"]
                    token = f'<a id="{anchor}"></a>'
                    text = text.replace(token, token + "\nTAMPERED PAYLOAD", 1)
                elif mutation[0] == "semantic_excerpt":
                    review = json.loads(text)
                    review["decisions"][0]["semantic_propositions"] = ["Generic extracted claim."]
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "child_union":
                    review = json.loads(text)
                    parent = next(d for d in review["decisions"] if d["direct_children"])
                    parent["child_union_sha256"] = "0" * 64
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "segment_hash":
                    review = json.loads(text)
                    leaf = next(d for d in review["decisions"] if d["large_leaf_segments"])
                    leaf["large_leaf_segments"][0]["payload_sha256"] = "0" * 64
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "answer_sequence":
                    answers = iter(mutation[1])
                    text = re.sub(
                        r"\*\*Answer:\s*[A-D]\.\*\*",
                        lambda _: f"**Answer: {next(answers)}.**",
                        text,
                    )
                    audit_path = copy / "MCQ-AUDIT.json"
                    audit = json.loads(audit_path.read_text(encoding="utf-8"))
                    audit["answer_sequence"] = mutation[1]
                    audit["answer_counts"] = {letter: mutation[1].count(letter) for letter in "ABCD"}
                    audit["position_policy"]["predictable_cycle_detected"] = mutation[1] == "ABCD" * 8
                    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                else:
                    text += mutation[1]
                target.write_text(text, encoding="utf-8", newline="\n")
            rc, data = invoke(copy)
            codes = [e.get("code") for e in data.get("errors", [])]
            ok = rc != 0 and expected in codes
            results.append({"case": name, "expected": expected, "returncode": rc, "codes": codes, "passed": ok})
        copy = work / "release-not-staged"
        prepare(copy)
        rc, data = invoke(copy, release=True)
        codes = [e.get("code") for e in data.get("errors", [])]
        results.append({"case": "release-not-staged", "expected": "GIT_RELEASE_NOT_STAGED", "returncode": rc,
                        "codes": codes, "passed": rc != 0 and "GIT_RELEASE_NOT_STAGED" in codes})
    finally:
        shutil.rmtree(work, ignore_errors=True)
    out = {"total": len(results), "passed": sum(x["passed"] for x in results), "results": results}
    print(json.dumps(out, indent=2))
    return 0 if all(x["passed"] for x in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
