from __future__ import annotations

import json
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def remove_tree(path: Path) -> None:
    def force_remove(func, target, _):
        os.chmod(target, stat.S_IWRITE)
        func(target)
    if path.exists():
        shutil.rmtree(path, onerror=force_remove)


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def prepare(path: Path) -> None:
    shutil.copytree(ROOT, path, ignore=shutil.ignore_patterns(".negative-tests-work", "__pycache__", "*.pyc"))


def invoke(copy: Path, release: bool = False) -> tuple[int, dict]:
    cmd = [sys.executable, "-B", str(copy / "validate_package.py"), "--root", str(copy), "--check-only"]
    if release:
        cmd.append("--release")
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    proc = subprocess.run(cmd, text=True, encoding="utf-8", capture_output=True, env=env)
    try:
        data = json.loads(proc.stdout)
    except Exception:
        data = {"errors": [{"code": "UNPARSEABLE", "detail": proc.stdout + proc.stderr}]}
    return proc.returncode, data


def main() -> int:
    work = ROOT / ".negative-tests-work"
    remove_tree(work)
    work.mkdir()
    results = []

    def case(name: str, expected: str, mutate, release: bool = False, nonmutating: bool = False) -> None:
        copy = work / name
        prepare(copy)
        mutate(copy)
        validation = copy / "VALIDATION.json"
        before = validation.read_bytes() if validation.exists() else None
        code, data = invoke(copy, release)
        after = validation.read_bytes() if validation.exists() else None
        codes = [x.get("code") for x in data.get("errors", [])]
        passed = code != 0 and expected in codes and (not nonmutating or before == after)
        results.append({"case": name, "expected": expected, "returncode": code,
                        "codes": codes, "details": data.get("errors", []),
                        "nonmutating": not nonmutating or before == after, "passed": passed})

    def noop(_: Path) -> None:
        return

    try:
        case("missing-file-stale-success", "MISSING_REQUIRED_FILE", lambda c: (c / "README.md").unlink())

        def source_identity(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["sources"]["canonical"]["path"] = str(c / "fake.md"); write_json(p, d)
        case("source-identity", "SOURCE_IDENTITY_MISMATCH", source_identity)

        def source_hash(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["sources"]["canonical"]["sha256"] = "0" * 64; write_json(p, d)
        case("source-hash", "SOURCE_HASH_MISMATCH", source_hash)

        def formal_path(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["formal_authorities"]["formal_session"]["path"] = str(c / "wrong" / "Learning-Session.md")
            write_json(p, d)
        case("formal-exact-topic-path", "FORMAL_EXACT_PATH_MISMATCH", formal_path)

        def formal_hash(c: Path) -> None:
            p = c / "build_package.py"; t = p.read_text(encoding="utf-8")
            t = t.replace('"sha256": "f847272fd032151fda3be9aa36267134ab32b51743792111ca1e8e8cfa66928c"',
                          '"sha256": "' + "0" * 64 + '"', 1)
            p.write_text(t, encoding="utf-8", newline="\n")
        case("formal-exact-hash", "SOURCE_ARTIFACT_STALE", formal_hash)

        def formal_line_count(c: Path) -> None:
            p = c / "build_package.py"; t = p.read_text(encoding="utf-8")
            t = t.replace('"lines": 5194', '"lines": 5193', 1); p.write_text(t, encoding="utf-8", newline="\n")
        case("formal-line-identity", "SOURCE_ARTIFACT_STALE", formal_line_count)

        def formal_title(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["formal_authorities"]["formal_workbook"]["actual_title"] = "Wrong title"; write_json(p, d)
        case("formal-title-identity", "FORMAL_TITLE_IDENTITY", formal_title)

        def formal_missing(c: Path) -> None:
            p = c / "build_package.py"; t = p.read_text(encoding="utf-8")
            old = r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\05-Samkhya\Learning-Session.md"
            missing = str(c / "bound-formal" / "Learning-Session.md")
            t = t.replace(old, missing, 1); p.write_text(t, encoding="utf-8", newline="\n")
            review = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(review.read_text(encoding="utf-8"))
            d["sources"]["formal_session"]["path"] = missing
            d["formal_authorities"]["formal_session"]["path"] = missing
            write_json(review, d)
        case("missing-formal-file", "SOURCE_IDENTITY_MISMATCH", formal_missing)

        case("source-snapshot", "SOURCE_SNAPSHOT_STALE",
             lambda c: (c / "source-snapshots" / "canonical-Samkhya.md").write_text("tamper\n", encoding="utf-8"))
        case("formal-session-snapshot", "SOURCE_SNAPSHOT_STALE",
             lambda c: (c / "source-snapshots" / "formal-Learning-Session.md").write_text("tamper\n", encoding="utf-8"))
        case("formal-workbook-snapshot", "SOURCE_SNAPSHOT_STALE",
             lambda c: (c / "source-snapshots" / "formal-Solved-Practice-Workbook.md").write_text("tamper\n", encoding="utf-8"))

        def block_hash(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["decisions"][0]["own_payload_sha256"] = "0" * 64; write_json(p, d)
        case("block-identity-hash", "BLOCK_IDENTITY_OR_HASH_MISMATCH", block_hash)

        def workbook_block_hash(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["decisions"] if x["source"] == "formal_workbook")
            row["own_payload_sha256"] = "1" * 64; write_json(p, d)
        case("formal-workbook-block-identity", "BLOCK_IDENTITY_OR_HASH_MISMATCH", workbook_block_hash)

        def decision_validation_status(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["decisions"][0]["validation_result"] = False; write_json(p, d)
        case("decision-validation-status", "DECISION_VALIDATION_STATUS", decision_validation_status)

        def destination(c: Path) -> None:
            p = c / "FORMAL-SOURCE-MIRROR.md"; t = p.read_text(encoding="utf-8")
            first = re.search(r'<a id="canonical-[^"]+"></a>', t).group(0)
            p.write_text(t.replace(first, first + "\nTAMPER", 1), encoding="utf-8", newline="\n")
        case("destination-payload", "DESTINATION_PAYLOAD_HASH_MISMATCH", destination)

        def learner(c: Path) -> None:
            p = c / "REVISION-GUIDE.md"; t = p.read_text(encoding="utf-8")
            first = re.search(r'<a id="canonical-[^"]+"></a>', t).group(0)
            p.write_text(t.replace(first, first + "\nTAMPER", 1), encoding="utf-8", newline="\n")
        case("learner-payload", "LEARNER_FORMAL_PAYLOAD_MISMATCH", learner)

        def hierarchy(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["decisions"] if x["direct_children"])
            row["child_union_sha256"] = "0" * 64; write_json(p, d)
        case("hierarchy-child-union", "CHILD_UNION_MISMATCH", hierarchy)

        def large_leaf(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["decisions"] if x["large_leaf_segments"])
            row["large_leaf_segments"][0]["payload_sha256"] = "0" * 64; write_json(p, d)
        case("large-leaf", "LARGE_LEAF_MISMATCH", large_leaf)

        def panel(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["panels"] if x["id"].startswith("canonical-"))
            row["payload_sha256"] = "0" * 64; write_json(p, d)
        case("panel-parity", "PANEL_PARITY_MISMATCH", panel)

        def formal_panel(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["panels"] if x["id"].startswith("formal_session-"))
            row["payload_sha256"] = "2" * 64; write_json(p, d)
        case("formal-panel-parity", "PANEL_PARITY_MISMATCH", formal_panel)

        def panel_validation_status(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["panels"][0]["validation_result"] = "failed"; write_json(p, d)
        case("panel-validation-status", "PANEL_VALIDATION_STATUS", panel_validation_status)

        def special_inventory_status(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["special_inventories"]["advanced_modules"][0]["validation_result"] = None; write_json(p, d)
        case("special-inventory-validation-status", "SPECIAL_INVENTORY_VALIDATION_STATUS", special_inventory_status)

        def formal_structure(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["advanced_modules"] = 0; d["register_sections"] = 0; d["workbook_diagnostics"] = 0
            write_json(p, d)
        case("advanced-register-diagnostic-identity", "FORMAL_STRUCTURAL_IDENTITY", formal_structure)

        def structural_inflation(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["decisions"] if x["excluded_non_propositional_fragments"])
            item = {"exact_payload_sha256": "0" * 64, "exact_payload": "## injected structural heading"}
            row["proposition_mappings"].append({"source_block_id": row["id"], "occurrence": 999,
                                                "proposition_id": "prop-" + "0" * 20,
                                                "exact_payload_sha256": item["exact_payload_sha256"],
                                                "exact_payload": item["exact_payload"]})
            write_json(p, d)
        case("structural-proposition-inflation", "NON_PROPOSITION_FRAGMENT_INCLUDED", structural_inflation)

        def table_header_inflation(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(
                row for row in d["decisions"]
                if any(item.get("reason") == "table_header_scaffolding"
                       for item in row["excluded_non_propositional_fragments"])
            )
            header = next(item for item in row["excluded_non_propositional_fragments"]
                          if item["reason"] == "table_header_scaffolding")
            row["proposition_mappings"].append({
                "source_block_id": row["id"], "occurrence": len(row["proposition_mappings"]) + 1,
                "proposition_id": "prop-" + "0" * 20,
                "exact_payload_sha256": header["exact_payload_sha256"],
                "exact_payload": header["exact_payload"],
            })
            write_json(p, d)
        case("table-header-proposition-inflation", "TABLE_HEADER_STRUCTURAL_INFLATION", table_header_inflation)

        def visual_label_inflation(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(
                row for row in d["decisions"]
                if any(item.get("reason") == "visual_label_coordinate"
                       for item in row["excluded_non_propositional_fragments"])
            )
            item = next(item for item in row["excluded_non_propositional_fragments"]
                        if item["reason"] == "visual_label_coordinate")
            row["proposition_mappings"].append({
                "source_block_id": row["id"], "occurrence": len(row["proposition_mappings"]) + 1,
                "proposition_id": "prop-" + "1" * 20,
                "exact_payload_sha256": item["exact_payload_sha256"],
                "exact_payload": item["exact_payload"],
            })
            write_json(p, d)
        case("uppercase-visual-label-proposition-inflation",
             "VISUAL_LABEL_PROPOSITION_INFLATION", visual_label_inflation)

        def package_count_inflation(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(
                row for row in d["decisions"]
                if any(item.get("reason") == "package_composition_metadata"
                       for item in row["excluded_non_propositional_fragments"])
            )
            item = next(item for item in row["excluded_non_propositional_fragments"]
                        if item["reason"] == "package_composition_metadata")
            row["proposition_mappings"].append({
                "source_block_id": row["id"], "occurrence": len(row["proposition_mappings"]) + 1,
                "proposition_id": "prop-" + "2" * 20,
                "exact_payload_sha256": item["exact_payload_sha256"],
                "exact_payload": item["exact_payload"],
            })
            write_json(p, d)
        case("package-count-metadata-proposition-inflation",
             "PACKAGE_COMPOSITION_PROPOSITION_INFLATION", package_count_inflation)

        def structural_class_inflation(c: Path, reason: str) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(
                row for row in d["decisions"]
                if any(item.get("reason") == reason for item in row["excluded_non_propositional_fragments"])
            )
            item = next(item for item in row["excluded_non_propositional_fragments"] if item["reason"] == reason)
            row["proposition_mappings"].append({
                "source_block_id": row["id"],
                "occurrence": len(row["proposition_mappings"]) + 1,
                "proposition_id": "prop-" + item["exact_payload_sha256"][:20],
                "exact_payload_sha256": item["exact_payload_sha256"],
                "exact_payload": item["exact_payload"],
            })
            write_json(p, d)

        case("boundary-caption-proposition-inflation", "BOUNDARY_CAPTION_STRUCTURAL_INFLATION",
             lambda c: structural_class_inflation(c, "boundary_caption_coordinate"))
        case("panel-label-proposition-inflation", "PANEL_LABEL_STRUCTURAL_INFLATION",
             lambda c: structural_class_inflation(c, "panel_label_coordinate"))
        case("diagram-heading-proposition-inflation", "DIAGRAM_HEADING_STRUCTURAL_INFLATION",
             lambda c: structural_class_inflation(c, "diagram_heading_coordinate"))
        case("parenthetical-routing-proposition-inflation", "PARENTHETICAL_ROUTING_STRUCTURAL_INFLATION",
             lambda c: structural_class_inflation(c, "parenthetical_routing_instruction"))

        def proposition(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["decisions"] if x["proposition_mappings"])
            row["proposition_mappings"][0]["proposition_id"] = "prop-" + "f" * 20; write_json(p, d)
        case("proposition-reference", "SEMANTIC_PROPOSITION_REFERENCE_TAMPER", proposition)

        def source_specific(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["source_proposition_breakdown"]["formal_workbook"]["raw_mappings"] -= 1; write_json(p, d)
        case("source-specific-proposition-omission", "SOURCE_SPECIFIC_PROPOSITION_OMISSION", source_specific)

        def proposition_sample(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["source_proposition_breakdown"]["formal_session"]["deterministic_payload_samples"][0]["payload"] = "tamper"
            write_json(p, d)
        case("source-proposition-sample", "SOURCE_PROPOSITION_SAMPLE_TAMPER", proposition_sample)

        def exclusion_reason_total(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            first = next(iter(d["excluded_fragment_reason_counts"]))
            d["excluded_fragment_reason_counts"][first] += 1; write_json(p, d)
        case("excluded-reason-count-consistency", "EXCLUDED_REASON_COUNT_MISMATCH", exclusion_reason_total)

        def excluded_fragment_hash(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["decisions"] if x["excluded_non_propositional_fragments"])
            row["excluded_non_propositional_fragments"][0]["exact_payload_sha256"] = "0" * 64
            write_json(p, d)
        case("excluded-fragment-hash-binding", "EXCLUDED_FRAGMENT_HASH_MISMATCH", excluded_fragment_hash)

        def source_global_total(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["source_proposition_breakdown"]["formal_session"]["excluded_structural_coordinates"] += 1
            write_json(p, d)
        case("source-global-total-consistency", "SOURCE_GLOBAL_TOTAL_MISMATCH", source_global_total)

        def duplicate_total(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["duplicate_occurrences_deduplicated"] += 1; write_json(p, d)
        case("duplicate-total-consistency", "DUPLICATE_ACCOUNTING_MISMATCH", duplicate_total)

        def obligation_omission(c: Path) -> None:
            p = c / "AUTHORITY-OBLIGATION-LEDGER.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["obligations"].pop(0); d["obligation_count"] -= 1; write_json(p, d)
        case("obligation-omission", "OBLIGATION_OMISSION", obligation_omission)

        def obligation_hash(c: Path) -> None:
            p = c / "AUTHORITY-OBLIGATION-LEDGER.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["obligations"][0]["source_payload_hashes"]["block_sha256"] = "0" * 64; write_json(p, d)
        case("obligation-hash-drift", "OBLIGATION_HASH_DRIFT", obligation_hash)

        def obligation_rule_id(c: Path) -> None:
            p = c / "AUTHORITY-OBLIGATION-LEDGER.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["obligations"] if x["classification"] == "testable_atomic")
            row["classification_rule_id"] = "SK-TR-TAMPERED"; write_json(p, d)
        case("testability-rule-id-tamper", "OBLIGATION_RULE_ID_DRIFT", obligation_rule_id)

        def obligation_rule_rationale(c: Path) -> None:
            p = c / "AUTHORITY-OBLIGATION-LEDGER.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["obligations"] if x["classification"] == "testable_atomic")
            row["classification_rationale"] = "question overlap decides testability"; write_json(p, d)
        case("authority-selection-rationale-tamper", "OBLIGATION_RULE_RATIONALE_DRIFT", obligation_rule_rationale)

        def obligation_rule_hash(c: Path) -> None:
            p = c / "AUTHORITY-OBLIGATION-LEDGER.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["obligations"] if x["classification"] == "testable_atomic")
            row["classification_rule_hash"] = "0" * 64; write_json(p, d)
        case("authority-selection-rule-hash-tamper", "OBLIGATION_RULE_HASH_DRIFT", obligation_rule_hash)

        def obligation_block(c: Path) -> None:
            p = c / "AUTHORITY-OBLIGATION-LEDGER.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["obligations"] if x["authority_block_ids"])
            row["authority_block_ids"] = ["invalid-block"]; write_json(p, d)
        case("invalid-obligation-authority-block", "OBLIGATION_AUTHORITY_BLOCK_REFERENCE_INVALID", obligation_block)

        def obligation_prop(c: Path) -> None:
            p = c / "AUTHORITY-OBLIGATION-LEDGER.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["obligations"] if x["proposition_ids"])
            row["proposition_ids"] = ["prop-" + "f" * 20]; write_json(p, d)
        case("invalid-obligation-proposition", "OBLIGATION_PROPOSITION_REFERENCE_INVALID", obligation_prop)

        def missing_mapping(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            oid = d["question_mappings"][0]["obligation_ids"][0]
            d["question_mappings"] = [x for x in d["question_mappings"] if oid not in x["obligation_ids"]]
            for cell in d["cells"]:
                if oid in cell["obligation_ids"]:
                    cell["mapped_question_ids"] = []
            write_json(p, d)
        case("missing-testable-reverse-coverage", "TESTABLE_OBLIGATION_REVERSE_COVERAGE_MISSING", missing_mapping)

        def false_mapping(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["question_mappings"][0]["mapping_anchors"][0]["doctrine_specific_terms"] = ["generic", "overlap"]; write_json(p, d)
        case("false-mcq-mapping", "MCQ_SEMANTIC_AUTHORITY_MISMATCH", false_mapping)

        def map_non_testable(c: Path, classification: str) -> None:
            lp = c / "AUTHORITY-OBLIGATION-LEDGER.json"; ledger = json.loads(lp.read_text(encoding="utf-8"))
            oid = next(x["obligation_id"] for x in ledger["obligations"] if x["classification"] == classification)
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["question_mappings"][0]["obligation_ids"] = [oid]; write_json(p, d)
        case("supporting-obligation-mapped-to-mcq", "NON_TESTABLE_OBLIGATION_MAPPED",
             lambda c: map_non_testable(c, "supporting_non_testable_context"))
        case("routed-obligation-mapped-to-mcq", "NON_TESTABLE_OBLIGATION_MAPPED",
             lambda c: map_non_testable(c, "routed_boundary"))

        def supporting_overlap_cannot_promote(c: Path) -> None:
            lp = c / "AUTHORITY-OBLIGATION-LEDGER.json"; ledger = json.loads(lp.read_text(encoding="utf-8"))
            supporting = next(x for x in ledger["obligations"] if x["classification"] == "supporting_non_testable_context"
                              and x["proposition_ids"])
            injected = "independently classified supporting context"
            for name in ("MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md"):
                p = c / name; text = p.read_text(encoding="utf-8")
                text = text.replace("Which statement best preserves historical source control?",
                                    f"Which statement follows this supporting context? {injected}", 1)
                p.write_text(text, encoding="utf-8", newline="\n")
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["question_mappings"][0]["obligation_ids"] = [supporting["obligation_id"]]
            d["question_mappings"][0]["keyed_evidence_terms"] = ["supporting"]
            write_json(p, d)
        case("question-overlap-cannot-promote-supporting", "NON_TESTABLE_OBLIGATION_MAPPED",
             supporting_overlap_cannot_promote)

        def delete_authored_question(c: Path) -> None:
            for name in ("MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md"):
                p = c / name; text = p.read_text(encoding="utf-8")
                text = re.sub(r"(?ms)^## MCQ 1\..*?(?=^## MCQ 2\.)", "", text, count=1)
                p.write_text(text, encoding="utf-8", newline="\n")
        case("question-deletion-cannot-demote-obligation", "MCQ_DOCUMENT_COUNT", delete_authored_question)

        def orphan_cell(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = dict(d["cells"][0]); row["cell_id"] = "SK-TM-ORPHAN"; d["cells"].append(row); write_json(p, d)
        case("orphan-cell", "ORPHAN_CELL", orphan_cell)

        def orphan_question(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = dict(d["question_mappings"][0]); row["question_id"] = "Q999"; d["question_mappings"].append(row); write_json(p, d)
        case("orphan-question", "ORPHAN_QUESTION", orphan_question)

        def cell_obligation_mismatch(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["cells"][0]["obligation_ids"] = d["cells"][1]["obligation_ids"]; write_json(p, d)
        case("cell-obligation-mismatch", "CELL_OBLIGATION_MISMATCH", cell_obligation_mismatch)

        def claimed_cell_cannot_change_inventory(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            original = d["question_mappings"][0]["obligation_ids"]
            other = next(x for x in d["cells"] if x["obligation_ids"] != original)
            d["question_mappings"][0]["cell_id"] = other["cell_id"]; write_json(p, d)
        case("question-claimed-cell-cannot-change-inventory", "QUESTION_OBLIGATION_MISMATCH",
             claimed_cell_cannot_change_inventory)

        def question_authority_mismatch(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["question_mappings"][0]["authority_refs"][0]["block_sha256"] = "0" * 64; write_json(p, d)
        case("question-authority-mismatch", "QUESTION_AUTHORITY_MISMATCH", question_authority_mismatch)

        def overloaded(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            for cid in (d["cells"][1]["cell_id"], d["cells"][2]["cell_id"]):
                next(x for x in d["cells"] if x["cell_id"] == cid)["mapped_question_ids"].append("Q1")
                d["question_mappings"].append({"question_id": "Q1", "cell_id": cid,
                                               "primary_discriminator": "tamper",
                                               "evidence_scope": "title_stem_keyed_option_keyed_explanation_only"})
            write_json(p, d)
        case("overloaded-mcq-mapping", "MCQ_MAPPING_OVERLOADED", overloaded)

        def duplicate_mapping(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["question_mappings"].append(dict(d["question_mappings"][0])); write_json(p, d)
        case("redundant-mcq-mapping", "MCQ_REDUNDANT_MAPPING", duplicate_mapping)

        def redundant(c: Path) -> None:
            p = c / "MCQ-SOLUTIONS.md"; t = p.read_text(encoding="utf-8")
            stems = re.findall(r"(?m)^## MCQ \d+\..+\n\n(.+)$", t)
            t = t.replace(stems[1], stems[0], 1); p.write_text(t, encoding="utf-8", newline="\n")
            q = c / "MCQ-QUESTIONS.md"; u = q.read_text(encoding="utf-8")
            u = u.replace(stems[1], stems[0], 1); q.write_text(u, encoding="utf-8", newline="\n")
        case("redundant-mcq-stem", "MCQ_REDUNDANT_STEM", redundant)

        def distractor_only(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["question_mappings"] if x["question_id"] == "Q1")
            row["mapping_anchors"][0]["doctrine_specific_terms"] = ["yoga", "cosmology"]
            write_json(p, d)
        case("distractor-only-mapping", "MCQ_SEMANTIC_AUTHORITY_MISMATCH", distractor_only)

        def legacy(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["fixed_question_count"] = 32; write_json(p, d)
        case("legacy-fixed-total", "LEGACY_FIXED_TOTAL", legacy)

        def matrix_total(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["question_total"] -= 1; write_json(p, d)
        case("derived-total-tamper", "MCQ_MATRIX_TOTAL_MISMATCH", matrix_total)

        def classification_generic(c: Path) -> None:
            p = c / "AUTHORITY-CLASSIFICATION.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["rows"] if x["classification"] == "supporting_non_testable_context"
                       and x["proposition_ids"])
            row["substantive_category"] = "generic"; write_json(p, d)
        case("generic-classification-fallback", "CLASSIFICATION_GENERIC_FALLBACK", classification_generic)

        def represented_row(c: Path) -> tuple[Path, dict, dict]:
            p = c / "AUTHORITY-CLASSIFICATION.json"; d = json.loads(p.read_text(encoding="utf-8"))
            row = next(x for x in d["rows"] if x.get("classification_predicate", {}).get("represented_by_obligation_ids"))
            return p, d, row

        def delete_representation_ids(c: Path) -> None:
            p, d, row = represented_row(c)
            row["classification_predicate"].pop("represented_by_obligation_ids")
            write_json(p, d)
        case("supporting-representation-ids-deleted", "CLASSIFICATION_SOURCE_ONLY_MISMATCH", delete_representation_ids)

        def swap_representation_ids(c: Path) -> None:
            p, d, row = represented_row(c)
            wrong = next(x["obligation_id"] for x in d["rows"]
                         if x["classification"] == "testable_atomic"
                         and x["obligation_id"] not in row["classification_predicate"]["represented_by_obligation_ids"])
            row["classification_predicate"]["represented_by_obligation_ids"] = [wrong]
            write_json(p, d)
        case("supporting-representation-wrong-id", "CLASSIFICATION_SOURCE_ONLY_MISMATCH", swap_representation_ids)

        def unsupported_supporting_rationale(c: Path) -> None:
            p, d, row = represented_row(c)
            row["classification_rationale"] = "Generic supporting context."
            write_json(p, d)
        case("unsupported-supporting-rationale", "CLASSIFICATION_SOURCE_ONLY_MISMATCH", unsupported_supporting_rationale)

        def unsupported_supporting_category(c: Path) -> None:
            p, d, row = represented_row(c)
            row["substantive_category"] = "concise_doctrinal_context"
            write_json(p, d)
        case("unsupported-supporting-category", "CLASSIFICATION_SOURCE_ONLY_MISMATCH", unsupported_supporting_category)

        def generic_only_unrelated_representation(c: Path) -> None:
            p, d, row = represented_row(c)
            wrong = next(x for x in d["rows"] if x["classification"] == "testable_atomic"
                         and x["obligation_id"] not in row["classification_predicate"]["represented_by_obligation_ids"])
            row["classification_predicate"] = {
                "represented_by_obligation_ids": [wrong["obligation_id"]],
                "relation_type": "entailed_by",
                "doctrine_specific_anchors": [{
                    "obligation_id": wrong["obligation_id"],
                    "shared_doctrine_terms": ["within", "they"],
                }],
            }
            write_json(p, d)
        case("generic-only-unrelated-representation", "SUPPORTING_SEMANTIC_RELATION_INVALID",
             generic_only_unrelated_representation)

        def comparative_only_unrelated_representation(c: Path) -> None:
            p, d, row = represented_row(c)
            wrong = next(x for x in d["rows"] if x["classification"] == "testable_atomic"
                         and x["obligation_id"] not in row["classification_predicate"]["represented_by_obligation_ids"])
            row["classification_predicate"] = {
                "represented_by_obligation_ids": [wrong["obligation_id"]],
                "relation_type": "entailed_by",
                "doctrine_specific_anchors": [{
                    "obligation_id": wrong["obligation_id"],
                    "shared_doctrine_terms": ["rather", "than"],
                }],
            }
            write_json(p, d)
        case("comparative-only-unrelated-representation", "SUPPORTING_SEMANTIC_RELATION_INVALID",
             comparative_only_unrelated_representation)

        def omit_composite_component(c: Path) -> None:
            p, d, row = represented_row(c)
            if row["classification_predicate"].get("relation_type") != "composite_split":
                row = next(x for x in d["rows"]
                           if x.get("classification_predicate", {}).get("relation_type") == "composite_split")
            row["classification_predicate"]["components"].pop()
            write_json(p, d)
        case("omitted-composite-component", "SUPPORTING_COMPOSITE_COMPONENT_MISSING",
             omit_composite_component)

        def dangling_source_fragment(c: Path) -> None:
            p = c / "FORMAL-COVERAGE-REVIEW.json"
            data = json.loads(p.read_text(encoding="utf-8"))
            mapping = next(
                mapping for row in data["decisions"] for mapping in row["proposition_mappings"]
                if "many disconnected ultimates" in mapping["exact_payload"]
            )
            mapping["exact_payload"] = "if the source were many disconnected ultimates, the cosmos would not be"
            mapping["exact_payload_sha256"] = __import__("hashlib").sha256(
                mapping["exact_payload"].encode("utf-8")
            ).hexdigest()
            write_json(p, data)
        case("dangling-source-proposition", "INCOMPLETE_SOURCE_PAYLOAD", dangling_source_fragment)

        named_hashes = {'SK-OBL-0019D13AF3773281': 'ebf1cd762bf6791adc7c4595f3593207d5f79e13cdd11305457ec55487d6e205', 'SK-OBL-00B4D506865F8507': '2ae67e9612bf522b3fba7ee2f76d13879bae27f785b1ff134d4f6b10c3090051', 'SK-OBL-01EBB56AC1E9DFF1': '89e2d1b23a4f02f3c18c576f7c8b08b800c4205d0c727dd8850c24755ae64e45', 'SK-OBL-0CBB34936D886BC3': '539f9c01d36a6fa56ab8b0fb581c53c2f78ac28dae7b389a1a35c67fa232473b', 'SK-OBL-52CD91D237B07371': 'db2b035c9963e1be312de56a07d45e754f419644898157df64339fe7355df87a'}
        for named_oid in (
            "SK-OBL-0CBB34936D886BC3", "SK-OBL-01EBB56AC1E9DFF1",
            "SK-OBL-52CD91D237B07371", "SK-OBL-0019D13AF3773281",
            "SK-OBL-00B4D506865F8507",
        ):
            def misclassify_named(c: Path, oid: str = named_oid) -> None:
                p = c / "AUTHORITY-CLASSIFICATION.json"; d = json.loads(p.read_text(encoding="utf-8"))
                row = next(x for x in d["rows"] if x["obligation_id"] == oid or x.get("normalized_semantic_hash") == named_hashes[oid])
                row["classification"] = "routed_boundary"
                write_json(p, d)
            case("misclassify-" + named_oid.lower(), "OBLIGATION_CLASSIFICATION_INVALID", misclassify_named)

        def semantic_authority_swap(c: Path) -> None:
            p = c / "TEST-MATRIX.json"; d = json.loads(p.read_text(encoding="utf-8"))
            source = next(x for x in d["question_mappings"] if len(x["obligation_ids"]) == 1)
            other = next(x for x in d["cells"] if len(x["obligation_ids"]) == 1
                         and x["obligation_ids"] != source["obligation_ids"])
            old_cid = source["cell_id"]
            source["obligation_ids"] = list(other["obligation_ids"])
            source["authority_refs"] = list(other["authority_refs"])
            source["mapping_anchors"] = [{
                "obligation_id": other["obligation_ids"][0],
                "doctrine_specific_terms": ["samkhya", "explains"],
            }]
            cell = next(x for x in d["cells"] if x["cell_id"] == old_cid)
            cell["obligation_ids"] = list(other["obligation_ids"])
            cell["authority_refs"] = list(other["authority_refs"])
            new_cid = "SK-CELL-" + other["obligation_ids"][0].removeprefix("SK-OBL-") + "-" + __import__("hashlib").sha256(cell["probe_mode"].encode()).hexdigest()[:10].upper()
            cell["cell_id"] = new_cid
            source["cell_id"] = new_cid
            write_json(p, d)
        case("hash-valid-semantic-authority-swap", "MCQ_SEMANTIC_AUTHORITY_MISMATCH", semantic_authority_swap)

        def classification_handle(c: Path) -> None:
            p = c / "AUTHORITY-CLASSIFICATION.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["rows"][0]["classification_rationale"] += " SK-TM-001"; write_json(p, d)
        case("classification-authoring-handle-leak", "CLASSIFICATION_AUTHORING_HANDLE_LEAK", classification_handle)

        def classification_title(c: Path) -> None:
            matrix = json.loads((c / "TEST-MATRIX.json").read_text(encoding="utf-8"))
            leaked_title = matrix["cells"][0]["title"]
            p = c / "AUTHORITY-CLASSIFICATION.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["rows"][0]["classification_rationale"] += " " + leaked_title
            write_json(p, d)
        case("classification-authored-title-leak", "CLASSIFICATION_AUTHORING_TITLE_LEAK", classification_title)

        def classification_drift(c: Path) -> None:
            p = c / "AUTHORITY-CLASSIFICATION.json"; d = json.loads(p.read_text(encoding="utf-8"))
            current = d["rows"][0]["classification"]
            d["rows"][0]["classification"] = (
                "testable_atomic" if current != "testable_atomic" else "supporting_non_testable_context"
            )
            write_json(p, d)
        case("classification-mutation-source-fixed", "CLASSIFICATION_HASH_DRIFT", classification_drift)

        def validator_coupling(c: Path) -> None:
            p = c / "validate_package.py"; text = p.read_text(encoding="utf-8")
            p.write_text(text.replace("import argparse", "import argparse\nimport build_package", 1),
                         encoding="utf-8", newline="\n")
        case("validator-builder-coupling-import", "VALIDATOR_BUILDER_COUPLING", validator_coupling)

        def builder_classification_rule(c: Path) -> None:
            p = c / "build_package.py"; text = p.read_text(encoding="utf-8")
            text = text.replace("SK-TR-001|formal_session", "SK-TR-001|canonical", 1)
            p.write_text(text, encoding="utf-8", newline="\n")
        case("altered-builder-classification-rules", "SOURCE_ARTIFACT_STALE", builder_classification_rule)

        def builder_probe_binding(c: Path) -> None:
            p = c / "build_package.py"; text = p.read_text(encoding="utf-8")
            text = text.replace("SK-TM-014|SK-TR-001", "SK-TM-014|SK-TR-002", 1)
            p.write_text(text, encoding="utf-8", newline="\n")
        case("altered-builder-probe-bindings", "SOURCE_ARTIFACT_STALE", builder_probe_binding)

        def generated_question_tamper(c: Path) -> None:
            for name in ("MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md"):
                p = c / name; text = p.read_text(encoding="utf-8")
                p.write_text(text.replace("Which statement best preserves historical source control?",
                                          "Which altered statement preserves historical source control?", 1),
                             encoding="utf-8", newline="\n")
        case("generated-question-set-tamper", "GENERATED_QUESTION_SET_TAMPER", generated_question_tamper)

        def draw_field(c: Path, field: str, value) -> None:
            p = c / "MCQ-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            current = d["question_draws"][0].get(field)
            d["question_draws"][0][field] = ("B" if current == "A" else "A") if value == "other-letter" else value
            write_json(p, d)
        case("answer-raw-draw-tamper", "ANSWER_RAW_DRAW_TAMPER",
             lambda c: draw_field(c, "raw_draw", "other-letter"))
        case("answer-final-placement-tamper", "ANSWER_FINAL_PLACEMENT_TAMPER",
             lambda c: draw_field(c, "final_placement", "other-letter"))
        case("answer-rejection-log-tamper", "ANSWER_REJECTION_LOG_TAMPER",
             lambda c: draw_field(c, "rejection_log", [{"attempt": 99}]))
        case("answer-draw-hash-tamper", "ANSWER_DRAW_HASH_TAMPER",
             lambda c: draw_field(c, "draw_hash", "0" * 64))

        def quota_contract(c: Path) -> None:
            p = c / "MCQ-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["target_distribution"] = {"A": 17, "B": 17, "C": 17, "D": 16}; write_json(p, d)
        case("answer-quota-target-contract", "ANSWER_QUOTA_CONTRACT", quota_contract)

        def option_length(c: Path) -> None:
            for name in ("MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md"):
                p = c / name; t = p.read_text(encoding="utf-8")
                p.write_text(t.replace("A. Kapila’s complete root text is the extant classical manual.",
                                       "A. Kapila.", 1), encoding="utf-8", newline="\n")
        case("option-length-cue", "MCQ_OPTION_LENGTH_CUE", option_length)

        def cue_field(c: Path, field: str) -> None:
            p = c / "MCQ-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["option_cues"][field] = 1; write_json(p, d)
        case("option-format-cue", "MCQ_OPTION_FORMAT_CUE", lambda c: cue_field(c, "format_mismatches"))
        case("option-specificity-cue", "MCQ_OPTION_SPECIFICITY_CUE", lambda c: cue_field(c, "specificity_flags"))
        case("option-lexical-cue", "MCQ_OPTION_LEXICAL_CUE", lambda c: cue_field(c, "lexical_key_flags"))

        def explanation_boilerplate(c: Path) -> None:
            p = c / "MCQ-SOLUTIONS.md"
            text = p.read_text(encoding="utf-8")
            replacement = "Incorrect because this repeats a generic wrong-option explanation without identifying the doctrinal error."
            changed = 0

            def replace_chunk(match: re.Match) -> str:
                nonlocal changed
                chunk = match.group(0)
                answer_match = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", chunk)
                if not answer_match:
                    return chunk
                answer = answer_match.group(1)

                def replace_line(line: re.Match) -> str:
                    nonlocal changed
                    if changed >= 4 or line.group(1) == answer:
                        return line.group(0)
                    changed += 1
                    return f"- **{line.group(1)}:** {replacement}"

                return re.sub(
                    r"^- \*\*([A-D]):\*\*\s*(.+)$",
                    replace_line,
                    chunk,
                    flags=re.M,
                )

            text = re.sub(r"(?ms)^## MCQ \d+\..*?(?=^## MCQ \d+\.|\Z)", replace_chunk, text)
            p.write_text(text, encoding="utf-8", newline="\n")
        case("wrong-explanation-boilerplate", "MCQ_WRONG_EXPLANATION_BOILERPLATE", explanation_boilerplate)

        def trap_boilerplate(c: Path) -> None:
            p = c / "MCQ-SOLUTIONS.md"
            text = p.read_text(encoding="utf-8")
            generic = "**Examiner trap:** This repeated trap does not identify the misconception tested by the question."
            text = re.sub(r"^\*\*Examiner trap:\*\*.+$", generic, text, count=4, flags=re.M)
            p.write_text(text, encoding="utf-8", newline="\n")
        case("examiner-trap-boilerplate", "MCQ_EXAMINER_TRAP_BOILERPLATE", trap_boilerplate)

        def pyq_wording(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["primary"][0]["exact_wording"] = "Altered wording"; write_json(p, d)
        case("pyq-exact-wording", "PYQ_EXACT_WORDING_OR_MARKS", pyq_wording)

        def formal_pyq_corpus(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["formal_pre_2026_corpus"]["primary_count"] = 13; write_json(p, d)
        case("formal-pyq-primary-routed-split", "PYQ_FORMAL_CORPUS_OWNERSHIP", formal_pyq_corpus)

        def pyq_marks(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["primary"][8]["marks_display"] = "20 marks"; write_json(p, d)
        case("pyq-2024-split-marks", "PYQ_EXACT_WORDING_OR_MARKS", pyq_marks)

        def pyq_component(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["primary"][0]["qualification_present"] = False; write_json(p, d)
        case("pyq-missing-component", "PYQ_SOLUTION_COMPONENT_MISSING", pyq_component)

        def pyq_validation_status(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            del d["primary"][0]["validation_result"]; write_json(p, d)
        case("formal-pyq-validation-status", "SPECIAL_INVENTORY_VALIDATION_STATUS", pyq_validation_status)

        def pyq_band(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["primary"][0]["model_word_count"] = 149; write_json(p, d)
        case("pyq-word-band", "PYQ_WORD_BAND", pyq_band)

        def routed_owner(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["supporting"][0]["primary_owner_is_samkhya"] = True; write_json(p, d)
        case("routed-pyq-ownership", "PYQ_ROUTED_OWNERSHIP", routed_owner)

        def originals(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["originals"] = d["originals"][:-1]; write_json(p, d)
        case("six-originals", "ORIGINAL_TIMED_SET", originals)

        def original_band(c: Path) -> None:
            p = c / "PYQ-DEMAND-AUDIT.json"; d = json.loads(p.read_text(encoding="utf-8"))
            d["originals"][0]["model_word_count"] = 149; write_json(p, d)
        case("original-word-band", "ORIGINAL_WORD_BAND", original_band)

        def stale(c: Path) -> None:
            p = c / "README.md"; p.write_text(p.read_text(encoding="utf-8") + "\nstale\n", encoding="utf-8")
        case("source-artifact-staleness", "SOURCE_ARTIFACT_STALE", stale)

        case("release-not-staged-nonmutating", "RELEASE_NOT_STAGED", noop, release=True, nonmutating=True)

        def mixed_stage(c: Path) -> None:
            subprocess.run(["git", "init", "-q", str(c)], check=True)
            subprocess.run(["git", "-C", str(c), "config", "user.email", "negative@test.invalid"], check=True)
            subprocess.run(["git", "-C", str(c), "config", "user.name", "Negative Test"], check=True)
            subprocess.run(["git", "-C", str(c), "add", "."], check=True)
            p = c / "README.md"
            p.write_text(p.read_text(encoding="utf-8") + "\nmixed unstaged change\n", encoding="utf-8", newline="\n")
        case("release-mixed-clean-staged-normalized", "RELEASE_NOT_STAGED", mixed_stage,
             release=True, nonmutating=True)
    finally:
        summary = {"schema_version": 2, "test_count": len(results),
                   "passed_count": sum(x["passed"] for x in results),
                   "failed_count": sum(not x["passed"] for x in results), "results": results}
        (ROOT / "NEGATIVE-TEST-RESULTS.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                                                        encoding="utf-8", newline="\n")
        remove_tree(work)
    print(json.dumps(summary, ensure_ascii=True, indent=2))
    return 0 if summary["failed_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
