from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def invoke(copy: Path, release: bool = False) -> tuple[int, dict]:
    command = [sys.executable, "-B", str(copy / "validate_package.py"), "--root", str(copy), "--check-only"]
    if release:
        command.append("--release")
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(command, text=True, encoding="utf-8", capture_output=True, env=environment)
    try:
        payload = json.loads(result.stdout)
    except Exception:
        payload = {"errors": [{"code": "UNPARSEABLE", "detail": result.stdout + result.stderr}]}
    return result.returncode, payload


def prepare(path: Path) -> None:
    shutil.copytree(
        ROOT, path,
        ignore=shutil.ignore_patterns(".negative-tests-work", ".negative-debug", "__pycache__", "*.pyc"),
    )
    if not (path / "VALIDATION.json").exists():
        (path / "VALIDATION.json").write_text('{"state":"DEVELOPMENT_PASS","release_ready":false}\n', encoding="utf-8")


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def mutate_answer_sequence(copy: Path, sequence: str) -> None:
    path = copy / "MCQ-SOLUTIONS.md"
    answers = iter(sequence)
    text = re.sub(r"\*\*Answer:\s*[A-D]\.\*\*", lambda _: f"**Answer: {next(answers)}.**", path.read_text(encoding="utf-8"))
    path.write_text(text, encoding="utf-8", newline="\n")
    audit_path = copy / "MCQ-AUDIT.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    audit["answer_sequence"] = sequence
    audit["answer_counts"] = {letter: sequence.count(letter) for letter in "ABCD"}
    audit["position_policy"]["predictable_cycle_detected"] = sequence == "ABCD" * (len(sequence) // 4)
    write_json(audit_path, audit)


def main() -> int:
    work = ROOT / ".negative-tests-work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir()
    results = []

    def run_case(name: str, expected: str, mutator) -> None:
        copy = work / name
        prepare(copy)
        mutator(copy)
        code, data = invoke(copy)
        codes = [row.get("code") for row in data.get("errors", [])]
        results.append({
            "case": name, "expected": expected, "returncode": code,
            "codes": codes,
            "details": data.get("errors", []) if "UNPARSEABLE" in codes else [],
            "passed": code != 0 and expected in codes,
        })

    try:
        run_case("missing-file-fresh", "MISSING_REQUIRED_FILE", lambda copy: (copy / "README.md").unlink())

        def source_hash(copy: Path) -> None:
            path = copy / "FORMAL-COVERAGE-REVIEW.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["sources"]["formal_session"]["sha256"] = "0" * 64
            write_json(path, data)
        run_case("authoritative-source-hash-tamper", "SOURCE_HASH_MISMATCH", source_hash)

        def destination(copy: Path) -> None:
            review = json.loads((copy / "FORMAL-COVERAGE-REVIEW.json").read_text(encoding="utf-8"))
            anchor = review["decisions"][0]["destination"]["anchor"]
            path = copy / "FORMAL-SOURCE-MIRROR.md"
            token = f'<a id="{anchor}"></a>'
            path.write_text(path.read_text(encoding="utf-8").replace(token, token + "\nTAMPER", 1), encoding="utf-8")
        run_case("destination-payload-tamper", "DESTINATION_PAYLOAD_HASH_MISMATCH", destination)

        def hierarchy(copy: Path) -> None:
            path = copy / "FORMAL-COVERAGE-REVIEW.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            parent = next(row for row in data["decisions"] if row["direct_children"])
            parent["child_union_sha256"] = "0" * 64
            write_json(path, data)
        run_case("hierarchy-child-union-tamper", "CHILD_UNION_MISMATCH", hierarchy)

        def semantic(copy: Path) -> None:
            path = copy / "FORMAL-COVERAGE-REVIEW.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            row = next(row for row in data["decisions"] if row["proposition_mappings"])
            row["proposition_mappings"][0]["proposition_id"] = "prop-" + "0" * 20
            write_json(path, data)
        run_case("semantic-proposition-reference-tamper", "SEMANTIC_PROPOSITION_REFERENCE_TAMPER", semantic)

        def non_proposition_inclusion(copy: Path) -> None:
            path = copy / "FORMAL-COVERAGE-REVIEW.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            row = next(item for item in data["decisions"] if item["excluded_non_propositional_fragments"])
            fragment = row["excluded_non_propositional_fragments"][0]
            row["proposition_mappings"].append({
                "source_block_id": row["id"],
                "occurrence": len(row["proposition_mappings"]) + 1,
                "proposition_id": "prop-" + "0" * 20,
                "exact_payload_sha256": fragment["exact_payload_sha256"],
                "exact_payload": fragment["exact_payload"],
            })
            write_json(path, data)
        run_case(
            "non-propositional-option-coordinate-inclusion",
            "NON_PROPOSITION_FRAGMENT_INCLUDED",
            non_proposition_inclusion,
        )

        def mcq_option(copy: Path) -> None:
            path = copy / "MCQ-QUESTIONS.md"
            text = path.read_text(encoding="utf-8").replace("A. ", "A. TAMPERED ", 1)
            path.write_text(text, encoding="utf-8", newline="\n")
        run_case("mcq-option-tamper", "MCQ_OPTION_SOLUTION_TAMPER", mcq_option)

        def mcq_answer(copy: Path) -> None:
            path = copy / "MCQ-SOLUTIONS.md"
            text = path.read_text(encoding="utf-8")
            first = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", text)
            other = next(letter for letter in "ABCD" if letter != first.group(1))
            path.write_text(text[:first.start()] + f"**Answer: {other}.**" + text[first.end():], encoding="utf-8", newline="\n")
        run_case("mcq-answer-tamper", "MCQ_ANSWER_EXPLANATION_TAMPER", mcq_answer)

        def uncovered_cell(copy: Path) -> None:
            path = copy / "TEST-MATRIX.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            cell = data["cells"][25]
            qid = cell["mapped_question_ids"].pop()
            data["question_mappings"] = [
                row for row in data["question_mappings"]
                if not (row["question_id"] == qid and row["cell_id"] == cell["cell_id"])
            ]
            cell["coverage_status"] = "uncovered"
            write_json(path, data)
        run_case("uncovered-substantive-cell", "MCQ_CELL_BELOW_MINIMUM", uncovered_cell)

        def below_minimum(copy: Path) -> None:
            path = copy / "TEST-MATRIX.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["cells"][0]["minimum_probes"] = 3
            write_json(path, data)
        run_case("below-minimum-cell", "MCQ_CELL_BELOW_MINIMUM", below_minimum)

        def unknown_mapping(copy: Path) -> None:
            path = copy / "TEST-MATRIX.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["question_mappings"].append({
                "question_id": "Q999", "cell_id": "NV-TM-999",
                "primary_discriminator": "unknown",
            })
            write_json(path, data)
        run_case("unknown-question-cell-mapping", "MCQ_UNKNOWN_MAPPING", unknown_mapping)

        def overloaded_mapping(copy: Path) -> None:
            path = copy / "TEST-MATRIX.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            for cell in (data["cells"][0], data["cells"][1]):
                cell["mapped_question_ids"].append("Q33")
                data["question_mappings"].append({
                    "question_id": "Q33", "cell_id": cell["cell_id"],
                    "primary_discriminator": cell["primary_discriminator"],
                })
            write_json(path, data)
        run_case("overloaded-question-mapping", "MCQ_MAPPING_OVERLOADED", overloaded_mapping)

        def false_mapping(copy: Path) -> None:
            path = copy / "TEST-MATRIX.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            source, target = data["cells"][25], data["cells"][0]
            source["mapped_question_ids"].remove("Q33")
            target["mapped_question_ids"].append("Q33")
            row = next(item for item in data["question_mappings"] if item["question_id"] == "Q33")
            row["cell_id"] = target["cell_id"]
            row["primary_discriminator"] = target["primary_discriminator"]
            write_json(path, data)
        run_case("false-question-mapping", "MCQ_FALSE_MAPPING", false_mapping)

        def add_mapping(copy: Path, cell_id: str, question_id: str) -> None:
            path = copy / "TEST-MATRIX.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            cell = next(item for item in data["cells"] if item["cell_id"] == cell_id)
            cell["mapped_question_ids"].append(question_id)
            data["question_mappings"].append({
                "question_id": question_id,
                "cell_id": cell_id,
                "primary_discriminator": cell["primary_discriminator"],
            })
            write_json(path, data)

        run_case(
            "q6-falsely-claims-five-motion-taxonomy",
            "NV_FIVE_MOTIONS_FALSE_MAPPING",
            lambda copy: add_mapping(copy, "NV-TM-058", "Q6"),
        )

        def remove_cell(copy: Path, cell_id: str) -> None:
            path = copy / "TEST-MATRIX.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["cells"] = [cell for cell in data["cells"] if cell["cell_id"] != cell_id]
            data["question_mappings"] = [
                row for row in data["question_mappings"] if row["cell_id"] != cell_id
            ]
            write_json(path, data)

        run_case(
            "missing-five-motion-cell",
            "NV_FIVE_MOTIONS_CELL_MISSING",
            lambda copy: remove_cell(copy, "NV-TM-058"),
        )
        run_case(
            "q19-falsely-claims-complete-three-grid",
            "NV_THREE_GRID_FALSE_MAPPING",
            lambda copy: add_mapping(copy, "NV-TM-033", "Q19"),
        )

        def replace_in_both(copy: Path, old: str, new: str) -> None:
            for name in ("MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md"):
                path = copy / name
                path.write_text(path.read_text(encoding="utf-8").replace(old, new), encoding="utf-8", newline="\n")

        run_case(
            "q19-partial-direction-grid-semantics",
            "NV_DIRECTION_GRID_EVIDENCE_MISSING",
            lambda copy: replace_in_both(copy, "non-causal uniformity", "regular uniformity"),
        )
        run_case(
            "q23-falsely-claims-apta-authority",
            "NV_APTA_AUTHORITY_FALSE_MAPPING",
            lambda copy: add_mapping(copy, "NV-TM-040", "Q23"),
        )
        run_case(
            "q47-missing-competence-sincerity",
            "NV_APTA_COMPETENCE_SINCERITY_EVIDENCE_MISSING",
            lambda copy: replace_in_both(
                copy,
                "Āpta requires knowledge and truthful communication",
                "Āpta requires social recognition and grammatical fluency",
            ),
        )
        run_case(
            "missing-graded-evaluation-cell",
            "NV_GRADED_EVALUATION_CELL_MISSING",
            lambda copy: remove_cell(copy, "NV-TM-059"),
        )
        run_case(
            "q64-falsely-assigned-graded-evaluation",
            "NV_Q64_GRADED_EVALUATION_FORBIDDEN",
            lambda copy: add_mapping(copy, "NV-TM-059", "Q64"),
        )
        run_case(
            "q66-missing-conditional-verdict",
            "NV_GRADED_EVALUATION_EVIDENCE_MISSING",
            lambda copy: replace_in_both(
                copy,
                "the overall verdict is conditional rather than absolute and depends on accepting these primitive termini",
                "the overall verdict is final and absolute",
            ),
        )

        def keyed_discriminator_removed_but_distractors_preserved(copy: Path) -> None:
            option = "Upward movement, downward movement, contraction, expansion and locomotion."
            replacement = "The standard fivefold list given by the school."
            for name in ("MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md"):
                path = copy / name
                text = path.read_text(encoding="utf-8")
                text = text.replace(f"D. {option}", f"D. {replacement}", 1)
                if name == "MCQ-SOLUTIONS.md":
                    old_explanation = (
                        f"- **D:** Correct: {option} "
                        "It preserves the complete discriminator without importing a rival doctrine."
                    )
                    new_explanation = (
                        f"- **D:** Correct: {replacement} "
                        "It preserves the complete discriminator without importing a rival doctrine."
                    )
                    text = text.replace(old_explanation, new_explanation, 1)
                path.write_text(text, encoding="utf-8", newline="\n")
        run_case(
            "keyed-discriminator-removed-distractors-retain-tokens",
            "NV_FIVE_MOTIONS_COMPLETE_EVIDENCE_MISSING",
            keyed_discriminator_removed_but_distractors_preserved,
        )

        def legacy_contract(copy: Path) -> None:
            path = copy / "MCQ-AUDIT.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["fixed_question_count"] = 32
            write_json(path, data)
        run_case("legacy-fixed-count-contract", "MCQ_LEGACY_FIXED_COUNT_CONTRACT", legacy_contract)

        count = len(re.findall(r"^## MCQ \d+\.", (ROOT / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8"), re.M))
        run_case(
            "mcq-cycle-tamper",
            "MCQ_PREDICTABLE_CYCLE",
            lambda copy: mutate_answer_sequence(copy, ("ABCD" * ((count + 3) // 4))[:count]),
        )
        run_case("mcq-imbalance-tamper", "MCQ_POSITION_IMBALANCE", lambda copy: mutate_answer_sequence(copy, "A" * count))

        def duplicate_question(copy: Path) -> None:
            path = copy / "MCQ-QUESTIONS.md"
            text = path.read_text(encoding="utf-8")
            first = re.search(r"(^## MCQ 1\..*?)(?=^<a id=\"mcq-02\")", text, re.M | re.S).group(1)
            path.write_text(text + "\n" + first, encoding="utf-8", newline="\n")
        run_case("duplicate-question-id", "MCQ_DUPLICATE_QUESTION_ID", duplicate_question)

        def pyq_wording(copy: Path) -> None:
            path = copy / "ANSWER-WRITING-TOOLKIT.md"
            text = path.read_text(encoding="utf-8").replace(
                "According to Nyaya view of inference (Anumana), what are the characteristics",
                "According to Nyaya inference, what are the characteristics", 1,
            )
            path.write_text(text, encoding="utf-8", newline="\n")
        run_case("pyq-wording-tamper", "PYQ_WORDING_TAMPER", pyq_wording)

        def pyq_owner(copy: Path) -> None:
            path = copy / "PYQ-DEMAND-AUDIT.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["supporting_questions"][0]["ownership"] = "Nyaya-Vaisesika-primary"
            write_json(path, data)
        run_case("pyq-ownership-tamper", "PYQ_SUPPORTING_AUDIT", pyq_owner)

        def stale_markdown_artifact(copy: Path) -> None:
            path = copy / "REVISION-GUIDE.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nStale mutation.\n", encoding="utf-8")
        run_case("stale-markdown-source-artifact", "SOURCE_ARTIFACT_STALE", stale_markdown_artifact)

        copy = work / "git-release-not-staged"
        prepare(copy)
        code, data = invoke(copy, release=True)
        codes = [row.get("code") for row in data.get("errors", [])]
        results.append({
            "case": "git-release-not-staged", "expected": "GIT_RELEASE_NOT_STAGED",
            "returncode": code, "codes": codes,
            "passed": code != 0 and "GIT_RELEASE_NOT_STAGED" in codes,
        })
    finally:
        shutil.rmtree(work, ignore_errors=True)
    output = {"total": len(results), "passed": sum(row["passed"] for row in results), "results": results}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if all(row["passed"] for row in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
