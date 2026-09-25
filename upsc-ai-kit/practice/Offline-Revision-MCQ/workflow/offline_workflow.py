from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SYSTEM_ROOT.parents[2]
INSTRUCTION_FILES = (
    REPO_ROOT / "OFFLINE-PACKAGE-AGENT-INSTRUCTIONS.md",
    SYSTEM_ROOT / "START-HERE.md",
)
WORKFLOW_DIR = SYSTEM_ROOT / "workflow"
SOURCE_REGISTRY = WORKFLOW_DIR / "SOURCE-REGISTRY.json"
CONTRACT_FILE = WORKFLOW_DIR / "VALIDATOR-INDEPENDENCE-CONTRACT.json"

GENERIC_ANCHORS = {
    "a", "an", "and", "are", "as", "at", "be", "because", "being", "by", "can",
    "does", "effect", "for", "from", "has", "have", "in", "is", "it", "many",
    "may", "nature", "not", "of", "on", "one", "or", "sankhya", "samkhya",
    "than", "that", "the", "their", "they", "this", "three", "to", "two", "was",
    "were", "what", "when", "which", "with", "within", "would",
}
DANGLING_END = re.compile(
    r"(?:\u2192|->|[:;,]|\b(?:a|an|and|as|at|because|by|for|from|if|in|of|on|or|"
    r"than|that|the|then|to|when|which|with|would|would not be))\s*$",
    re.IGNORECASE,
)
OPTION_RE = re.compile(r"^\s*(?:[-*]\s*)?([A-D])[.)]\s+(.+?)\s*$")
CASE_RE = re.compile(r"""case\(\s*["']([^"']+)["']\s*,\s*["']([^"']+)["']""")


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def resolve_topic(value: str) -> Path:
    topic = Path(value).resolve()
    if not topic.is_dir():
        raise SystemExit(f"Topic directory does not exist: {topic}")
    try:
        topic.relative_to(SYSTEM_ROOT)
    except ValueError as exc:
        raise SystemExit(f"Topic must be inside {SYSTEM_ROOT}") from exc
    return topic


def instruction_evidence() -> list[dict[str, Any]]:
    evidence = []
    for path in INSTRUCTION_FILES:
        data = path.read_bytes()
        evidence.append({
            "path": str(path),
            "sha256": sha_bytes(data),
            "bytes": len(data),
        })
    return evidence


def command_begin_pass(args: argparse.Namespace) -> int:
    topic = resolve_topic(args.topic)
    if args.time_budget_minutes <= 0 or args.tool_call_budget <= 0:
        raise SystemExit("Pass budgets must be positive integers")
    output = Path(args.output).resolve() if args.output else topic / "PASS-MANIFEST.json"
    manifest = {
        "schema_version": 2,
        "pass_id": args.pass_id,
        "pass_type": args.pass_type,
        "topic": str(topic.relative_to(SYSTEM_ROOT)).replace("\\", "/"),
        "actor": args.actor,
        "instructions_read_at_utc": now_utc(),
        "instruction_files": instruction_evidence(),
        "execution_budget": {
            "elapsed_minutes": args.time_budget_minutes,
            "tool_calls": args.tool_call_budget,
            "hard_stop_required": True,
            "silent_extension_forbidden": True,
            "maximum_complete_builds": 1,
            "maximum_complete_negative_suites": 1,
        },
        "pre_pass_attestation": {
            "coverage_ledger_frozen": args.coverage_frozen,
            "verified_pyqs_current": args.pyqs_current,
            "teaching_and_practice_surfaces_preserved": args.surfaces_preserved,
            "no_skip_or_compression": args.no_skip_compression,
            "mcq_total_coverage_derived": args.coverage_derived_mcqs,
        },
    }
    manifest["manifest_sha256"] = sha_bytes(json.dumps(
        manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8"))
    write_json(output, manifest)
    print(json.dumps({"state": "PASS_MANIFEST_RECORDED", "file": str(output)}, indent=2))
    return 0


def source_artifact_rows(topic: Path) -> list[dict[str, Any]]:
    audit_path = topic / "SOURCE-ARTIFACT-AUDIT.json"
    if not audit_path.exists():
        return []
    audit = load_json(audit_path)
    return [
        row for row in audit.get("artifacts", [])
        if str(row.get("file", "")).startswith("source-snapshots/")
    ]


def command_freeze_evidence(args: argparse.Namespace) -> int:
    topic = resolve_topic(args.topic)
    output = topic / "EVIDENCE-CACHE.json"
    rows = source_artifact_rows(topic)
    if not rows:
        raise SystemExit("SOURCE-ARTIFACT-AUDIT.json has no source-snapshot rows")
    verified = []
    for row in sorted(rows, key=lambda item: item["file"]):
        path = topic / row["file"]
        if not path.is_file():
            raise SystemExit(f"Missing cached source: {row['file']}")
        actual = {"file": row["file"], "sha256": sha_file(path), "bytes": path.stat().st_size}
        if actual["sha256"] != row.get("sha256") or actual["bytes"] != row.get("bytes"):
            raise SystemExit(f"Source audit mismatch: {row['file']}")
        verified.append(actual)
    fingerprint = sha_bytes(json.dumps(
        verified, sort_keys=True, separators=(",", ":")
    ).encode("utf-8"))
    previous = load_json(output) if output.exists() else {}
    cache_hit = previous.get("source_fingerprint") == fingerprint
    data = {
        "schema_version": 1,
        "topic": str(topic.relative_to(SYSTEM_ROOT)).replace("\\", "/"),
        "source_fingerprint": fingerprint,
        "sources": verified,
        "cache_policy": "reuse_parsed_evidence_only_while_every_source_hash_and_byte_count_match",
        "created_at_utc": previous.get("created_at_utc", now_utc()) if cache_hit else now_utc(),
        "last_verified_at_utc": now_utc(),
        "cache_hit": cache_hit,
    }
    write_json(output, data)
    print(json.dumps({"state": "EVIDENCE_CACHE_HIT" if cache_hit else "EVIDENCE_CACHE_FROZEN",
                      "file": str(output), "source_fingerprint": fingerprint}, indent=2))
    return 0


def git_changed_files(topic: Path) -> list[str]:
    rel = str(topic.relative_to(REPO_ROOT)).replace("\\", "/")
    proc = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "status", "--short", "--untracked-files=all", "--", rel],
        text=True, encoding="utf-8", capture_output=True, check=True,
    )
    return [line[3:].strip().replace("\\", "/") for line in proc.stdout.splitlines() if line.strip()]


def command_review_packet(args: argparse.Namespace) -> int:
    topic = resolve_topic(args.topic)
    validation = load_json(topic / "VALIDATION.json") if (topic / "VALIDATION.json").exists() else {}
    findings = []
    for finding in args.finding:
        path = Path(finding).resolve()
        findings.append({"file": str(path), "sha256": sha_file(path), "text": path.read_text(encoding="utf-8")})
    packet = {
        "schema_version": 1,
        "generated_at_utc": now_utc(),
        "topic": str(topic.relative_to(SYSTEM_ROOT)).replace("\\", "/"),
        "review_scope": args.scope,
        "changed_files": git_changed_files(topic),
        "rejected_findings": findings,
        "affected_obligation_ids": sorted(set(args.obligation)),
        "frozen_approved_counts": validation.get("checks", {}),
        "frozen_surfaces": sorted(set(args.frozen_surface)),
        "review_rule": "inspect_changed_risk_surfaces_only_unless_direct_evidence_contradicts_a_frozen_surface",
    }
    output = topic / "RISK-REVIEW-PACKET.json"
    write_json(output, packet)
    print(json.dumps({"state": "RISK_REVIEW_PACKET_READY", "file": str(output)}, indent=2))
    return 0


def iter_payloads(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in {
                "excluded_fragments", "excluded_coordinates", "exclusions",
                "structural_exclusions", "diagram_structural_exclusions",
            }:
                continue
            if key == "exact_payload" and (
                "\n" in child if isinstance(child, str) else False
            ):
                yield from iter_payloads(child, child_path)
                continue
            if isinstance(child, str) and key in {
                "payload", "exact_payload", "source_payload", "atomic_statement",
                "normalized_proposition", "proposition",
            }:
                yield child_path, child
            yield from iter_payloads(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_payloads(child, f"{path}[{index}]")


def iter_representation_links(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key in ("representation_links", "representations", "represented_by"):
            links = value.get(key)
            if isinstance(links, list):
                for index, link in enumerate(links):
                    if isinstance(link, dict):
                        yield f"{path}.{key}[{index}]", link
        for key, child in value.items():
            yield from iter_representation_links(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_representation_links(child, f"{path}[{index}]")


def option_length_warnings(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    warnings = []
    current = []
    question = "unknown"
    for line in path.read_text(encoding="utf-8").splitlines() + [""]:
        heading = re.match(r"^#{2,4}\s+(?:Question\s+)?(Q?\d+)", line, re.I)
        if heading:
            question = heading.group(1)
        match = OPTION_RE.match(line)
        if match:
            current.append((match.group(1), match.group(2)))
            continue
        if current and len(current) == 4:
            lengths = [max(1, len(re.findall(r"\b[\w'-]+\b", text))) for _, text in current]
            ordered = sorted(lengths)
            median = (ordered[1] + ordered[2]) / 2
            ratio = max(lengths) / max(1, median)
            if ratio > 3.2:
                warnings.append({"question": question, "lengths": lengths, "max_median_ratio": round(ratio, 3)})
        if current and not match:
            current = []
    return warnings


def command_semantic_lint(args: argparse.Namespace) -> int:
    topic = resolve_topic(args.topic)
    findings: list[dict[str, Any]] = []
    for name in ("SOURCE-PROPOSITION-INVENTORY.json", "AUTHORITY-CLASSIFICATION.json",
                 "AUTHORITY-OBLIGATION-LEDGER.json", "TESTABLE-OBLIGATIONS.json"):
        path = topic / name
        if not path.exists():
            continue
        data = load_json(path)
        for json_path, payload in iter_payloads(data):
            normalized = " ".join(payload.split())
            if normalized and DANGLING_END.search(normalized):
                findings.append({"code": "DANGLING_SEMANTIC_FRAGMENT", "file": name,
                                 "path": json_path, "sample": normalized[-160:]})
        for json_path, link in iter_representation_links(data):
            anchors = link.get("anchors") or link.get("evidence_tokens") or link.get("shared_terms") or []
            if isinstance(anchors, str):
                anchors = re.findall(r"[A-Za-z][A-Za-z-]+", anchors.lower())
            lowered = {str(item).casefold() for item in anchors}
            if lowered and lowered <= GENERIC_ANCHORS:
                findings.append({"code": "GENERIC_ONLY_REPRESENTATION_ANCHORS", "file": name,
                                 "path": json_path, "anchors": sorted(lowered)})
    for warning in option_length_warnings(topic / "MCQ-QUESTIONS.md"):
        findings.append({"code": "OPTION_LENGTH_OUTLIER", "file": "MCQ-QUESTIONS.md", **warning})
    result = {
        "schema_version": 1,
        "generated_at_utc": now_utc(),
        "topic": str(topic.relative_to(SYSTEM_ROOT)).replace("\\", "/"),
        "state": "SEMANTIC_LINT_PASS" if not findings else "SEMANTIC_LINT_FINDINGS",
        "findings": findings,
    }
    write_json(topic / "SEMANTIC-LINT.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if args.strict and findings else 0


def command_validator_contract(args: argparse.Namespace) -> int:
    topic = resolve_topic(args.topic)
    path = topic / "validate_package.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    contract = load_json(CONTRACT_FILE)
    forbidden_modules = set(contract["forbidden_modules"])
    forbidden_names = set(contract["forbidden_builder_imports"])
    findings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in forbidden_modules:
                    findings.append({"line": node.lineno, "module": alias.name, "name": "*"})
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            for alias in node.names:
                if module in forbidden_modules or (module == "build_package" and (
                    alias.name in forbidden_names or
                    any(re.search(pattern, alias.name, re.I) for pattern in contract["forbidden_name_patterns"])
                )):
                    findings.append({"line": node.lineno, "module": module, "name": alias.name})
    result = {
        "schema_version": 1,
        "topic": str(topic.relative_to(SYSTEM_ROOT)).replace("\\", "/"),
        "state": "VALIDATOR_INDEPENDENCE_PASS" if not findings else "VALIDATOR_INDEPENDENCE_FAIL",
        "findings": findings,
    }
    write_json(topic / "VALIDATOR-INDEPENDENCE.json", result)
    print(json.dumps(result, indent=2))
    return 1 if findings else 0


def discovered_negative_cases(topic: Path) -> list[dict[str, str]]:
    results_path = topic / "NEGATIVE-TEST-RESULTS.json"
    if results_path.exists():
        results = load_json(results_path).get("results", [])
        recorded = [
            {"case": str(row.get("case", "")), "expected_code": str(row.get("expected", ""))}
            for row in results
            if row.get("case") and row.get("expected")
        ]
        if recorded:
            return recorded
    runner = topic / "run_negative_tests.py"
    if not runner.exists():
        return []
    text = runner.read_text(encoding="utf-8")
    return [{"case": name, "expected_code": code} for name, code in CASE_RE.findall(text)]


def command_negative_plan(args: argparse.Namespace) -> int:
    topic = resolve_topic(args.topic)
    cases = discovered_negative_cases(topic)
    selected = []
    patterns = [re.compile(item, re.I) for item in args.invariant]
    for case in cases:
        if not patterns or any(pattern.search(case["case"]) or pattern.search(case["expected_code"])
                               for pattern in patterns):
            selected.append(case)
    plan = {
        "schema_version": 1,
        "generated_at_utc": now_utc(),
        "topic": str(topic.relative_to(SYSTEM_ROOT)).replace("\\", "/"),
        "focused_invariants": args.invariant,
        "focused_cases": selected,
        "full_suite_case_count": len(cases),
        "execution_policy": {
            "focused_during_repair": True,
            "full_suite_required_at_final_development_gate": True,
            "production_validator_required": True,
        },
    }
    write_json(topic / "NEGATIVE-TEST-PLAN.json", plan)
    print(json.dumps({"state": "NEGATIVE_TEST_PLAN_READY", "focused": len(selected),
                      "full": len(cases)}, indent=2))
    return 0


def command_register_source(args: argparse.Namespace) -> int:
    registry = load_json(SOURCE_REGISTRY)
    source_path = Path(args.file).resolve()
    entry = {
        "source_id": args.source_id,
        "topic": args.topic_name,
        "authority_role": args.role,
        "permitted_scope": args.scope,
        "path": str(source_path),
        "sha256": sha_file(source_path),
        "bytes": source_path.stat().st_size,
        "provenance": args.provenance,
        "rights": args.rights,
        "registered_at_utc": now_utc(),
    }
    existing = next((item for item in registry["sources"] if item["source_id"] == args.source_id), None)
    if existing:
        immutable_fields = ("topic", "authority_role", "permitted_scope", "path", "sha256", "bytes",
                            "provenance", "rights")
        if any(existing.get(key) != entry.get(key) for key in immutable_fields):
            raise SystemExit(
                f"Immutable source ID already exists with different evidence: {args.source_id}. "
                "Register changed evidence under a new source ID."
            )
        print(json.dumps({"state": "SOURCE_ALREADY_REGISTERED", "source": existing}, indent=2))
        return 0
    entries = list(registry["sources"])
    entries.append(entry)
    registry["sources"] = sorted(entries, key=lambda item: item["source_id"])
    registry["updated_at_utc"] = now_utc()
    write_json(SOURCE_REGISTRY, registry)
    print(json.dumps({"state": "SOURCE_REGISTERED", "source": entry}, indent=2))
    return 0


def command_sync_sources(args: argparse.Namespace) -> int:
    topic = resolve_topic(args.topic)
    registry = load_json(SOURCE_REGISTRY)
    topic_name = str(topic.relative_to(SYSTEM_ROOT)).replace("\\", "/")
    additions = []
    for row in source_artifact_rows(topic):
        rel = row["file"]
        source_path = topic / rel
        lower = rel.casefold()
        if "formal-" in lower:
            role = "formal"
        elif "canonical-" in lower:
            role = "canonical"
        elif "pyq-" in lower:
            role = "verified-pyq"
        elif "primary-" in lower or "/raw/" in lower:
            role = "user-approved-primary"
        else:
            role = "supplementary"
        source_identity = f"{topic_name}|{rel}|{row['sha256']}"
        source_id = f"src-{sha_bytes(source_identity.encode('utf-8'))[:24]}"
        entry = {
            "source_id": source_id,
            "topic": topic_name,
            "authority_role": role,
            "permitted_scope": (
                "topic-local source role only; no ownership transfer"
                if role != "user-approved-primary"
                else "topic-local user-approved primary-text obligation only"
            ),
            "path": str(source_path.resolve()),
            "sha256": row["sha256"],
            "bytes": row["bytes"],
            "provenance": f"Hash-bound package source artifact: {rel}",
            "rights": "Inherited from the recorded source artifact; verify before redistribution",
            "registered_at_utc": now_utc(),
        }
        existing = next((item for item in registry["sources"] if item["source_id"] == source_id), None)
        if existing:
            continue
        additions.append(entry)
    registry["sources"].extend(additions)
    registry["sources"] = sorted(registry["sources"], key=lambda item: item["source_id"])
    registry["updated_at_utc"] = now_utc()
    write_json(SOURCE_REGISTRY, registry)
    print(json.dumps({"state": "SOURCE_REGISTRY_SYNCED", "topic": topic_name,
                      "added": len(additions), "total": len(registry["sources"])}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Integrity-preserving offline package workflow controls")
    sub = parser.add_subparsers(dest="command", required=True)

    begin = sub.add_parser("begin-pass")
    begin.add_argument("--topic", required=True)
    begin.add_argument("--pass-id", required=True)
    begin.add_argument("--pass-type", required=True, choices=[
        "development", "focused-repair", "independent-review", "boundary-reconciliation",
        "release-validation", "commit", "push",
    ])
    begin.add_argument("--actor", default="copilot-cli")
    begin.add_argument("--output")
    begin.add_argument("--time-budget-minutes", required=True, type=int)
    begin.add_argument("--tool-call-budget", required=True, type=int)
    for flag in ("coverage-frozen", "pyqs-current", "surfaces-preserved",
                 "no-skip-compression", "coverage-derived-mcqs"):
        begin.add_argument(f"--{flag}", action="store_true", required=True)
    begin.set_defaults(func=command_begin_pass)

    cache = sub.add_parser("freeze-evidence")
    cache.add_argument("--topic", required=True)
    cache.set_defaults(func=command_freeze_evidence)

    packet = sub.add_parser("review-packet")
    packet.add_argument("--topic", required=True)
    packet.add_argument("--scope", required=True)
    packet.add_argument("--finding", action="append", default=[])
    packet.add_argument("--obligation", action="append", default=[])
    packet.add_argument("--frozen-surface", action="append", default=[])
    packet.set_defaults(func=command_review_packet)

    lint = sub.add_parser("semantic-lint")
    lint.add_argument("--topic", required=True)
    lint.add_argument("--strict", action="store_true")
    lint.set_defaults(func=command_semantic_lint)

    contract = sub.add_parser("validator-contract")
    contract.add_argument("--topic", required=True)
    contract.set_defaults(func=command_validator_contract)

    negatives = sub.add_parser("negative-plan")
    negatives.add_argument("--topic", required=True)
    negatives.add_argument("--invariant", action="append", default=[])
    negatives.set_defaults(func=command_negative_plan)

    source = sub.add_parser("register-source")
    source.add_argument("--source-id", required=True)
    source.add_argument("--topic-name", required=True)
    source.add_argument("--role", required=True)
    source.add_argument("--scope", required=True)
    source.add_argument("--file", required=True)
    source.add_argument("--provenance", required=True)
    source.add_argument("--rights", required=True)
    source.set_defaults(func=command_register_source)

    sync = sub.add_parser("sync-sources")
    sync.add_argument("--topic", required=True)
    sync.set_defaults(func=command_sync_sources)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
