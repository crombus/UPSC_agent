from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def prepare(path: Path) -> None:
    shutil.copytree(ROOT, path, ignore=shutil.ignore_patterns(".negative-tests-work", "__pycache__", "*.pyc"))


def invoke(copy: Path, release=False) -> tuple[int, dict]:
    cmd = [sys.executable, "-B", str(copy / "validate_package.py"), "--root", str(copy), "--check-only"]
    if release:
        cmd.append("--release")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
    proc = subprocess.run(cmd, text=True, encoding="utf-8", capture_output=True, env=env)
    try:
        data = json.loads(proc.stdout)
    except Exception:
        data = {"errors": [{"code": "UNPARSEABLE", "detail": proc.stdout + proc.stderr}]}
    return proc.returncode, data


def refresh_artifact_hash(copy: Path, rel: str) -> None:
    audit = copy / "SOURCE-ARTIFACT-AUDIT.json"
    data = json.loads(audit.read_text(encoding="utf-8"))
    path = copy / rel
    row = next(x for x in data["artifacts"] if x["file"] == rel)
    row["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    row["bytes"] = path.stat().st_size
    write_json(audit, data)


def main() -> int:
    work = ROOT / ".negative-tests-work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir()
    results = []

    def case(name, expected, mutate, release=False, nonmutating=False):
        copy = work / name
        prepare(copy)
        mutate(copy)
        before = {str(p.relative_to(copy)): p.read_bytes() for p in copy.rglob("*") if p.is_file()}
        code, data = invoke(copy, release)
        after = {str(p.relative_to(copy)): p.read_bytes() for p in copy.rglob("*") if p.is_file()}
        codes = [x.get("code") for x in data.get("errors", [])]
        unchanged = before == after
        results.append({
            "case": name, "expected": expected, "returncode": code, "codes": codes,
            "nonmutating": (not nonmutating or unchanged),
            "passed": code != 0 and expected in codes and (not nonmutating or unchanged),
        })

    def rebuilt_baseline_case(name, mutate):
        copy = work / name
        prepare(copy)
        mutate(copy)
        code, data = invoke(copy)
        results.append({
            "case": name, "expected": "DEVELOPMENT_PASS", "returncode": code,
            "codes": [x.get("code") for x in data.get("errors", [])],
            "nonmutating": True,
            "passed": code == 0 and data.get("state") == "DEVELOPMENT_PASS",
        })

    noop = lambda _: None
    try:
        case("missing-file-stale-success", "MISSING_REQUIRED_FILE", lambda c: (c / "README.md").unlink())

        def source_identity(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); d["sources"]["formal_session"]["path"]="C:\\fake.md"; write_json(p,d)
        case("formal-source-path-identity", "SOURCE_IDENTITY_MISMATCH", source_identity)

        def source_hash(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); d["sources"]["formal_session"]["sha256"]="0"*64; write_json(p,d)
        case("formal-source-hash-drift", "SOURCE_IDENTITY_MISMATCH", source_hash)

        def missing_formal(c):
            build=c/"build_package.py"
            text=build.read_text(encoding="utf-8")
            old=r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\06-Yoga\Learning-Session.md"
            new=r"C:\missing-formal-Yoga-Learning-Session.md"
            build.write_text(text.replace(old,new,1),encoding="utf-8",newline="\n")
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); d["sources"]["formal_session"]["path"]=new; write_json(p,d)
        case("formal-source-removal", "SOURCE_IDENTITY_MISMATCH", missing_formal)

        case("source-snapshot-staleness", "SOURCE_SNAPSHOT_STALE",
             lambda c:(c/"source-snapshots"/"formal-Learning-Session.md").write_text("tamper\n",encoding="utf-8"))

        def coordinated_source_registry_tamper(c):
            replacement = "C:\\coordinated-tamper\\Learning-Session.md"
            builder = c/"build_package.py"
            builder.write_text(
                builder.read_text(encoding="utf-8").replace(
                    r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\06-Yoga\Learning-Session.md",
                    replacement,
                    1,
                ),
                encoding="utf-8",
                newline="\n",
            )
            snapshot_rel = "source-snapshots/formal-Learning-Session.md"
            snapshot = c/snapshot_rel
            snapshot.write_text(snapshot.read_text(encoding="utf-8") + "\ncoordinated source tamper\n",
                                encoding="utf-8", newline="\n")
            digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
            registry = c/"SOURCE-REGISTRY.json"
            registry_data = json.loads(registry.read_text(encoding="utf-8"))
            row = next(x for x in registry_data["sources"] if x["key"] == "formal_session")
            row.update(path=replacement, sha256=digest, bytes=snapshot.stat().st_size,
                       line_count=len(snapshot.read_text(encoding="utf-8").splitlines()))
            write_json(registry, registry_data)
            review = c/"FORMAL-COVERAGE-REVIEW.json"
            review_data = json.loads(review.read_text(encoding="utf-8"))
            review_data["sources"]["formal_session"].update(
                path=replacement, sha256=digest, bytes=snapshot.stat().st_size,
                line_count=len(snapshot.read_text(encoding="utf-8").splitlines()),
            )
            write_json(review, review_data)
            for rel in ("build_package.py", "SOURCE-REGISTRY.json", snapshot_rel, "FORMAL-COVERAGE-REVIEW.json"):
                refresh_artifact_hash(c, rel)
        case("coordinated-builder-source-registry-snapshot-tamper",
             "SOURCE_REGISTRY_TAMPER", coordinated_source_registry_tamper)

        case("primary-snapshot-deletion", "MISSING_REQUIRED_FILE",
             lambda c:(c/"source-snapshots"/"primary-patanjali-yoga-sutra-ii-27-vivekananda-1896.md").unlink())

        def primary_snapshot_tamper(c):
            rel="source-snapshots/primary-patanjali-yoga-sutra-ii-27-vivekananda-1896.md"
            p=c/rel; p.write_text(p.read_text(encoding="utf-8").replace("sevenfold highest ground","sevenfold altered ground",1),encoding="utf-8",newline="\n")
            refresh_artifact_hash(c,rel)
        case("primary-snapshot-byte-hash-tamper", "PRIMARY_SOURCE_SNAPSHOT_TAMPER", primary_snapshot_tamper)

        def add_builder_truth(c, declaration):
            p=c/"build_package.py"
            p.write_text(p.read_text(encoding="utf-8")+"\n"+declaration+"\n",encoding="utf-8",newline="\n")
        case("builder-ii27-url-constant", "PRIMARY_SOURCE_TRUTH_DUPLICATED_IN_BUILDER",
             lambda c:add_builder_truth(c,'PRIMARY_II27_ITEM_URL = "https://example.invalid/ii27"'))
        case("builder-ii27-hash-constant", "PRIMARY_SOURCE_TRUTH_DUPLICATED_IN_BUILDER",
             lambda c:add_builder_truth(c,'PRIMARY_II27_OBJECT_SHA256 = "0" * 64'))
        case("builder-ii27-coordinate-constant", "PRIMARY_SOURCE_TRUTH_DUPLICATED_IN_BUILDER",
             lambda c:add_builder_truth(c,"PRIMARY_II27_LINE_START = 1"))
        case("builder-ii27-payload-constant", "PRIMARY_SOURCE_TRUTH_DUPLICATED_IN_BUILDER",
             lambda c:add_builder_truth(c,'PRIMARY_II27_OCR_PAYLOAD = "tampered"'))
        case("builder-ii27-scope-constant", "PRIMARY_SOURCE_TRUTH_DUPLICATED_IN_BUILDER",
             lambda c:add_builder_truth(c,'PRIMARY_II27_SCOPE = "general"'))

        def coordinated_builder_artifact_tamper(c):
            add_builder_truth(c, 'PRIMARY_II27_OBJECT_SHA256 = "f" * 64')
            wrong="f"*64
            p=c/"SOURCE-ARTIFACT-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8"))
            d["approved_primary_source"]["object_sha256"]=wrong; write_json(p,d)
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8"))
            d["approved_primary_sources"][0]["object_sha256"]=wrong; write_json(p,d)
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8"))
            ob=next(x for x in d["obligations"] if x["obligation_id"]=="YG-OB-077")
            ob["authority_evidence"][0]["source_file_sha256"]=wrong
            d["approved_primary_source_obligations"][0]["source_object_sha256"]=wrong
            write_json(p,d)
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8"))
            next(x for x in d["cells"] if x["obligation_id"]=="YG-OB-077")["authority_refs"]=ob["authority_evidence"]
            write_json(p,d)
            for rel in ("build_package.py","FORMAL-COVERAGE-REVIEW.json","TESTABLE-OBLIGATIONS.json","TEST-MATRIX.json"):
                refresh_artifact_hash(c,rel)
        case("coordinated-builder-generated-provenance-tamper",
             "PRIMARY_SOURCE_TRUTH_DUPLICATED_IN_BUILDER", coordinated_builder_artifact_tamper)

        def mutate_recorded_primary(c, field, value):
            p=c/"SOURCE-ARTIFACT-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8"))
            d["approved_primary_source"][field]=value; write_json(p,d)
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8"))
            review_field={"object_bytes":"object_bytes","object_sha256":"object_sha256"}[field]
            d["approved_primary_sources"][0][review_field]=value; write_json(p,d)
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8"))
            ob=next(x for x in d["obligations"] if x["obligation_id"]=="YG-OB-077")
            ref_field={"object_bytes":"source_file_bytes","object_sha256":"source_file_sha256"}[field]
            approved_field={"object_bytes":"source_object_bytes","object_sha256":"source_object_sha256"}[field]
            ob["authority_evidence"][0][ref_field]=value
            d["approved_primary_source_obligations"][0][approved_field]=value
            write_json(p,d)
            p=c/"TEST-MATRIX.json"; matrix=json.loads(p.read_text(encoding="utf-8"))
            next(x for x in matrix["cells"] if x["obligation_id"]=="YG-OB-077")["authority_refs"]=ob["authority_evidence"]
            write_json(p,matrix)
            for rel in ("FORMAL-COVERAGE-REVIEW.json","TESTABLE-OBLIGATIONS.json","TEST-MATRIX.json"):
                refresh_artifact_hash(c,rel)
        case("recorded-primary-object-byte-length-tamper", "YG-OB-077_PRIMARY_SOURCE_PROVENANCE_TAMPER",
             lambda c:mutate_recorded_primary(c,"object_bytes",197941))
        case("recorded-primary-object-sha-tamper", "YG-OB-077_PRIMARY_SOURCE_PROVENANCE_TAMPER",
             lambda c:mutate_recorded_primary(c,"object_sha256","0"*64))

        def raw_object_tamper(c):
            rel="source-snapshots/raw/PatanjaliYogaSutraSwamiVivekanandaSanEng_djvu.txt"
            p=c/rel; data=bytearray(p.read_bytes()); data[0]^=1; p.write_bytes(data); refresh_artifact_hash(c,rel)
        case("primary-raw-object-byte-tamper", "PRIMARY_SOURCE_RAW_SHA256_TAMPER", raw_object_tamper)

        def manifest_coordinate_tamper(c):
            rel="PRIMARY-SOURCE-AUTHORITY.json"; p=c/rel; d=json.loads(p.read_text(encoding="utf-8"))
            d["coordinate"]["line_start"]=3500; d["coordinate"]["line_end"]=3504
            write_json(p,d); refresh_artifact_hash(c,rel)
        case("primary-manifest-coordinate-tamper", "PRIMARY_SOURCE_AUTHORITY_MANIFEST_TAMPER", manifest_coordinate_tamper)

        def snapshot_scope_tamper(c):
            rel="source-snapshots/primary-patanjali-yoga-sutra-ii-27-vivekananda-1896.md"
            p=c/rel; text=p.read_text(encoding="utf-8")
            p.write_text(text.replace("It is not general formal or canonical authority","It is general formal and canonical authority",1),
                         encoding="utf-8",newline="\n")
            refresh_artifact_hash(c,rel)
        case("primary-snapshot-scope-tamper", "PRIMARY_SOURCE_SNAPSHOT_TAMPER", snapshot_scope_tamper)

        def mutate_primary_records(c, mutate):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8"))
            ob=next(x for x in d["obligations"] if x["obligation_id"]=="YG-OB-077")
            mutate(ob["authority_evidence"][0], d["approved_primary_source_obligations"][0])
            write_json(p,d); refresh_artifact_hash(c,"TESTABLE-OBLIGATIONS.json")
            m=c/"TEST-MATRIX.json"; md=json.loads(m.read_text(encoding="utf-8"))
            cell=next(x for x in md["cells"] if x["obligation_id"]=="YG-OB-077")
            cell["authority_refs"]=ob["authority_evidence"]; write_json(m,md); refresh_artifact_hash(c,"TEST-MATRIX.json")

        case("primary-wrong-sutra-ocr-coordinate", "YG-OB-077_PRIMARY_SOURCE_PROVENANCE_TAMPER",
             lambda c:mutate_primary_records(c,lambda ref,row:(ref.update(line_start=3500,line_end=3504),row.update(line_start=3500,line_end=3504))))
        case("primary-object-url-tamper", "YG-OB-077_PRIMARY_SOURCE_PROVENANCE_TAMPER",
             lambda c:mutate_primary_records(c,lambda ref,row:(ref.update(source_object_url="https://archive.org/download/wrong/object.txt"),row.update(source_object_url="https://archive.org/download/wrong/object.txt"))))

        def primary_scope_tamper(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8"))
            d["approved_primary_sources"][0]["scope"]="general_formal_authority"
            d["approved_primary_sources"][0]["general_authority"]=True
            write_json(p,d); refresh_artifact_hash(c,"FORMAL-COVERAGE-REVIEW.json")
        case("primary-provenance-scope-tamper", "YG-OB-077_PRIMARY_SOURCE_SCOPE_TAMPER", primary_scope_tamper)

        def delete_block(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); d["decisions"].pop(0); d["decision_count"]-=1; write_json(p,d)
        case("formal-block-deletion", "FORMAL_BLOCK_DELETION_OR_INFLATION", delete_block)

        def block(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); d["decisions"][0]["own_payload_sha256"]="0"*64; write_json(p,d)
        case("canonical-block-payload", "BLOCK_IDENTITY_OR_HASH_MISMATCH", block)

        def mirror(c):
            p=c/"FORMAL-SOURCE-MIRROR.md"; t=p.read_text(encoding="utf-8"); a=re.search(r'<a id="canonical-[^"]+"></a>',t).group(0); p.write_text(t.replace(a,a+"\nTAMPER",1),encoding="utf-8",newline="\n")
        case("destination-payload", "DESTINATION_PAYLOAD_HASH_MISMATCH", mirror)

        def learner(c):
            p=c/"REVISION-GUIDE.md"; t=p.read_text(encoding="utf-8"); a=re.search(r'<a id="canonical-[^"]+"></a>',t).group(0); p.write_text(t.replace(a,a+"\nTAMPER",1),encoding="utf-8",newline="\n")
        case("learner-payload", "LEARNER_PAYLOAD_MISMATCH", learner)

        def structural(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); row=next(x for x in d["decisions"] if x["excluded_non_propositional_fragments"]); item=row["excluded_non_propositional_fragments"][0]; row["proposition_mappings"].append({"source_block_id":row["id"],"occurrence":999,"proposition_id":"prop-"+"0"*20,"exact_payload_sha256":item["exact_payload_sha256"],"exact_payload":item["exact_payload"]}); write_json(p,d)
        case("semantic-structural-inflation", "NON_PROPOSITION_FRAGMENT_INCLUDED", structural)

        def diagram_fragment(c, fragment):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8"))
            row=next(x for x in d["decisions"] if x["source"]=="formal_session")
            row["proposition_mappings"].append({"source_block_id":row["id"],"occurrence":999,
                "proposition_id":"prop-"+sha(fragment)[:20],"exact_payload_sha256":sha(fragment),"exact_payload":fragment})
            write_json(p,d)
        case("diagram-connector-inflation", "NON_PROPOSITION_FRAGMENT_INCLUDED", lambda c:diagram_fragment(c,"│ evolution"))
        case("diagram-border-inflation", "NON_PROPOSITION_FRAGMENT_INCLUDED", lambda c:diagram_fragment(c,"└──────────────┘"))
        case("diagram-incomplete-fragment-inflation", "NON_PROPOSITION_FRAGMENT_INCLUDED", lambda c:diagram_fragment(c,"│ shared foundation"))

        def hierarchy(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); row=next(x for x in d["decisions"] if x["direct_children"]); row["child_union_sha256"]="0"*64; write_json(p,d)
        case("hierarchy-child-union", "CHILD_UNION_MISMATCH", hierarchy)

        def panel(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); d["panels"][0]["payload_sha256"]="0"*64; write_json(p,d)
        case("panel-parity", "PANEL_PARITY_MISMATCH", panel)

        def leaf(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); row=next(x for x in d["decisions"] if x["large_leaf_segments"]); row["large_leaf_segments"][0]["payload_sha256"]="0"*64; write_json(p,d)
        case("large-leaf-segment", "LARGE_LEAF_MISMATCH", leaf)

        def route(c):
            p=c/"FORMAL-COVERAGE-REVIEW.json"; d=json.loads(p.read_text(encoding="utf-8")); d["routes"][0]["obligation_id"]="tampered"; write_json(p,d)
        case("route-obligation", "ROUTE_OBLIGATION_TAMPER", route)

        case("obligation-inventory-omission", "MISSING_REQUIRED_FILE", lambda c:(c/"TESTABLE-OBLIGATIONS.json").unlink())

        def block_classification_omission(c):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8")); d["block_classifications"].pop(); write_json(p,d)
        case("obligation-block-classification-omission", "OBLIGATION_BLOCK_CLASSIFICATION_OMISSION", block_classification_omission)

        def proposition_classification_omission(c):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8")); d["proposition_classifications"].pop(); write_json(p,d)
        case("obligation-proposition-classification-omission", "OBLIGATION_PROPOSITION_CLASSIFICATION_OMISSION", proposition_classification_omission)

        def remove_real_obligation(c):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8"))
            d["obligations"]=[x for x in d["obligations"] if x["obligation_id"]!="YG-OB-001"]
            d["atomic_obligation_count"]-=1; write_json(p,d); refresh_artifact_hash(c,"TESTABLE-OBLIGATIONS.json")
        case("copied-package-source-obligation-removal", "SOURCE_DERIVED_OBLIGATION_REMOVED", remove_real_obligation)

        def reclassify_examinable(c):
            for rel, key in (("TESTABLE-OBLIGATIONS.json","proposition_classifications"),
                             ("SOURCE-PROPOSITION-INVENTORY.json","propositions")):
                p=c/rel; d=json.loads(p.read_text(encoding="utf-8"))
                row=next(x for x in d[key] if x["classification"]=="testable_atomic_obligation")
                row["classification"]="supporting_non_testable_context"
                row["rationale"]="Supporting non-testable context: malicious undercoverage mutation."
                write_json(p,d); refresh_artifact_hash(c,rel)
        case("copied-package-examinable-reclassified", "EXAMINABLE_PROPOSITION_RECLASSIFIED", reclassify_examinable)

        def remove_real_source_row(c):
            p=c/"SOURCE-PROPOSITION-INVENTORY.json"; d=json.loads(p.read_text(encoding="utf-8"))
            d["propositions"].pop(next(i for i,x in enumerate(d["propositions"]) if x["classification"]=="testable_atomic_obligation"))
            d["complete_proposition_occurrence_count"]-=1
            write_json(p,d); refresh_artifact_hash(c,"SOURCE-PROPOSITION-INVENTORY.json")
        case("copied-package-real-examinable-source-row-removed",
             "SOURCE_PROPOSITION_CLASSIFICATION_INCOMPLETE", remove_real_source_row)

        def reverse_coverage_omission(c):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8"))
            row=next(x for x in d["proposition_classifications"] if x["classification"]=="testable_atomic_obligation")
            row["reverse_mapping"]={}; write_json(p,d)
        case("obligation-reverse-coverage-omission", "OBLIGATION_CLASSIFICATION_INVALID", reverse_coverage_omission)

        def unrelated_representation(c):
            for rel, key in (("TESTABLE-OBLIGATIONS.json","proposition_classifications"),
                             ("SOURCE-PROPOSITION-INVENTORY.json","propositions")):
                p=c/rel; d=json.loads(p.read_text(encoding="utf-8"))
                row=next(x for x in d[key] if x["classification"]=="testable_atomic_obligation")
                row["reverse_mapping"]["represented_by_obligation_id"]="YG-OB-052"
                row["reverse_mapping"]["obligation_id"]="YG-OB-052"
                write_json(p,d); refresh_artifact_hash(c,rel)
        case("copied-package-plausible-unrelated-representation",
             "OBLIGATION_REVERSE_COVERAGE_MISSING", unrelated_representation)

        def orphan_obligation(c):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8")); d["obligations"].append(dict(d["obligations"][0],obligation_id="YG-OB-999",cell_id="YG-TM-999")); write_json(p,d)
        case("orphan-obligation", "OBLIGATION_ORPHAN_OR_OMISSION", orphan_obligation)

        def irrelevant_authority(c):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8"))
            d["obligations"][0]["authority_evidence"]=d["obligations"][24]["authority_evidence"]
            write_json(p,d)
        case("irrelevant-authority-loose-substring", "OBLIGATION_REVERSE_COVERAGE_MISSING", irrelevant_authority)

        def missing_mapping(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["question_mappings"]=[x for x in d["question_mappings"] if x["question_id"]!="Q1"]; write_json(p,d)
        case("missing-mcq-mapping", "MCQ_MISSING_MAPPING", missing_mapping)

        def remove_mapped_question(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8"))
            d["question_mappings"]=[x for x in d["question_mappings"] if x["question_id"]!="Q1"]
            d["cells"][0]["mapped_question_ids"]=[]; write_json(p,d); refresh_artifact_hash(c,"TEST-MATRIX.json")
        case("copied-package-mapped-question-removal", "MCQ_MISSING_MAPPING", remove_mapped_question)

        def split_continuation(c):
            p=c/"SOURCE-PROPOSITION-INVENTORY.json"; d=json.loads(p.read_text(encoding="utf-8"))
            row=next(x for x in d["propositions"] if x["source_block_id"].startswith("formal_session-033-")
                     and "threefold constitution" in x["exact_payload"])
            row["exact_payload"]=row["exact_payload"].replace(" functioning as one field.","")
            row["exact_payload_sha256"]=sha(row["exact_payload"]); row["normalized_sha256"]=sha(" ".join(row["exact_payload"].strip().lower().split()))
            write_json(p,d); refresh_artifact_hash(c,"SOURCE-PROPOSITION-INVENTORY.json")
        case("copied-package-hard-wrap-continuation-removed", "SOURCE_PROPOSITION_INVENTORY_TAMPER", split_continuation)

        def unfinished_connector(c):
            p=c/"SOURCE-PROPOSITION-INVENTORY.json"; d=json.loads(p.read_text(encoding="utf-8"))
            row=d["propositions"][0]; row["exact_payload"]="unfinished doctrine →"
            row["exact_payload_sha256"]=sha(row["exact_payload"]); row["normalized_sha256"]=sha(row["exact_payload"].lower())
            write_json(p,d); refresh_artifact_hash(c,"SOURCE-PROPOSITION-INVENTORY.json")
        case("copied-package-unfinished-connector", "SOURCE_PROPOSITION_INVENTORY_TAMPER", unfinished_connector)

        def unfinished_emphasis(c):
            p=c/"SOURCE-PROPOSITION-INVENTORY.json"; d=json.loads(p.read_text(encoding="utf-8"))
            row=d["propositions"][0]; row["exact_payload"]="**unfinished doctrinal proposition"
            row["exact_payload_sha256"]=sha(row["exact_payload"]); row["normalized_sha256"]=sha(row["exact_payload"].lower())
            write_json(p,d); refresh_artifact_hash(c,"SOURCE-PROPOSITION-INVENTORY.json")
        case("copied-package-unfinished-emphasis", "SOURCE_PROPOSITION_INVENTORY_TAMPER", unfinished_emphasis)

        def near_match_authority(c, oid, generic):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8"))
            ob=next((x for x in d["obligations"] if x["obligation_id"]==oid),None)
            if ob is None:
                ob=dict(d["obligations"][0],obligation_id=oid,source_proposition_id="synthetic-near-match")
                ob["authority_evidence"]=[dict(ob["authority_evidence"][0],proposition_id="synthetic-near-match")]
                d["obligations"].append(ob)
            ob["atomic_statement"]=generic
            ref=ob["authority_evidence"][0]; ref["exact_payload"]=generic
            ref["exact_payload_sha256"]=sha(generic); ref["normalized_sha256"]=sha(" ".join(generic.lower().split()))
            write_json(p,d); refresh_artifact_hash(c,"TESTABLE-OBLIGATIONS.json")
            m=c/"TEST-MATRIX.json"; md=json.loads(m.read_text(encoding="utf-8"))
            cell=next((x for x in md["cells"] if x["obligation_id"]==oid),None)
            if cell:
                cell["authority_refs"]=ob["authority_evidence"]
                write_json(m,md); refresh_artifact_hash(c,"TEST-MATRIX.json")
        case("yg-ob-077-plausible-near-match", "YG-OB-077_AUTHORITY_NEAR_MATCH",
             lambda c:near_match_authority(c,"YG-OB-077","Discriminative knowledge culminates in samādhi and liberation."))
        case("yg-ob-078-plausible-near-match", "YG-OB-078_AUTHORITY_NEAR_MATCH",
             lambda c:near_match_authority(c,"YG-OB-078","Samādhi and karma are discussed near the culmination of Yoga practice."))

        def obligation_overclaim(c):
            p=c/"TESTABLE-OBLIGATIONS.json"; d=json.loads(p.read_text(encoding="utf-8"))
            ob=next(x for x in d["obligations"] if x["obligation_id"]=="YG-OB-077")
            ob["atomic_statement"]="Yoga Sūtra II.27 enumerates seven named stages of culminating prajñā."
            write_json(p,d); refresh_artifact_hash(c,"TESTABLE-OBLIGATIONS.json")
            m=c/"TEST-MATRIX.json"; md=json.loads(m.read_text(encoding="utf-8"))
            cell=next(x for x in md["cells"] if x["obligation_id"]=="YG-OB-077")
            cell["substantive_discriminator"]=ob["atomic_statement"]
            write_json(m,md); refresh_artifact_hash(c,"TEST-MATRIX.json")
        case("primary-obligation-seven-stage-overclaim", "YG-OB-077_SEVEN_STAGE_OVERCLAIM", obligation_overclaim)

        def question_overclaim(c):
            for name in ("MCQ-QUESTIONS.md","MCQ-SOLUTIONS.md"):
                p=c/name; t=p.read_text(encoding="utf-8")
                t=t.replace(
                    "Which statement most accurately captures the Yoga doctrine of yoga sūtra ii.27 sevenfold culminating knowledge?",
                    "Which statement enumerates seven named stages in the Yoga doctrine of Yoga Sūtra II.27?",
                    1,
                )
                p.write_text(t,encoding="utf-8",newline="\n")
        case("primary-question-seven-stage-overclaim", "YG-OB-077_SEVEN_STAGE_OVERCLAIM", question_overclaim)

        def false_mapping(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["question_mappings"][0]["cell_id"]="YG-TM-002"; write_json(p,d)
        case("false-mcq-mapping", "MCQ_FALSE_MAPPING", false_mapping)

        def overloaded(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["question_mappings"] += [{"question_id":"Q1","cell_id":"YG-TM-002"},{"question_id":"Q1","cell_id":"YG-TM-003"}]; write_json(p,d)
        case("overloaded-mcq-mapping", "MCQ_MAPPING_OVERLOADED", overloaded)

        def distractor(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["cells"][0]["evidence_tokens"]=["bodily flexibility"]; write_json(p,d)
        case("distractor-only-mapping", "MCQ_DISTRACTOR_ONLY_MAPPING", distractor)

        def redundant_map(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["question_mappings"].append(dict(d["question_mappings"][0])); write_json(p,d)
        case("redundant-mcq-mapping", "MCQ_REDUNDANT_MAPPING", redundant_map)

        def orphan_cell(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["cells"].append(dict(d["cells"][0],cell_id="YG-TM-999",obligation_id="YG-OB-999",mapped_question_ids=[])); d["cell_count"]+=1; write_json(p,d)
        case("orphan-cell", "MCQ_CELL_SET_MISMATCH", orphan_cell)

        def orphan_question(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["question_mappings"].pop(); write_json(p,d)
        case("orphan-question", "MCQ_MISSING_MAPPING", orphan_question)

        def duplicate_cell(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["cells"][1]["substantive_discriminator"]=d["cells"][0]["substantive_discriminator"]; write_json(p,d)
        case("duplicate-redundant-cell", "MCQ_DUPLICATE_REDUNDANT_CELL", duplicate_cell)

        def fixed(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["fixed_question_count"]=32; write_json(p,d)
        case("legacy-fixed-total", "LEGACY_FIXED_TOTAL", fixed)

        def question_first(c):
            p=c/"TEST-MATRIX.json"; d=json.loads(p.read_text(encoding="utf-8")); d["derivation_policy"]="questions_first_then_cells"; write_json(p,d)
        case("question-first-derivation", "MCQ_QUESTION_FIRST_DERIVATION", question_first)

        def quota_contract(c):
            p=c/"MCQ-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8")); d["position_policy"]["answer_quota"]={"A":21,"B":20,"C":20,"D":20}; write_json(p,d)
        case("answer-quota-contract", "LEGACY_FIXED_TOTAL", quota_contract)

        def answers(c, sequence):
            p=c/"MCQ-SOLUTIONS.md"; it=iter(sequence); p.write_text(re.sub(r"\*\*Answer:\s*[A-D]\.\*\*",lambda _:f"**Answer: {next(it)}.**",p.read_text(encoding="utf-8")),encoding="utf-8",newline="\n")
            a=c/"MCQ-AUDIT.json"; d=json.loads(a.read_text(encoding="utf-8")); d["answer_sequence"]=sequence; d["answer_counts"]={x:sequence.count(x) for x in "ABCD"}; d["max_answer_run"]=max(len(m.group(0)) for m in re.finditer(r"(.)\1*",sequence)); write_json(a,d)
        n=len(re.findall(r"\*\*Answer:\s*[A-D]\.\*\*",(ROOT/"MCQ-SOLUTIONS.md").read_text(encoding="utf-8")))
        case("answer-run", "MCQ_ANSWER_RUN", lambda c:answers(c,"A"*n))
        case("answer-imbalance", "MCQ_ANSWER_IMBALANCE", lambda c:answers(c,"A"*(n-30)+"B"*10+"C"*10+"D"*10))
        case("answer-short-cycle", "MCQ_SHORT_CYCLE", lambda c:answers(c,("ABCD"*(n//4))+"ABCD"[:n%4]))

        def rebuild_with_ordinary_unequal(c):
            p=c/"build_package.py"; t=p.read_text(encoding="utf-8")
            t=t.replace('ANSWER_SEED = "Yoga|independent-per-question-position|2026-09-24"',
                        'ANSWER_SEED = "Yoga|ordinary-non-equal-acceptance|2026-09-24"',1)
            p.write_text(t,encoding="utf-8",newline="\n")
            proc=subprocess.run([sys.executable,"-B",str(p)],cwd=c,text=True,capture_output=True,
                                env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",PYTHONIOENCODING="utf-8"))
            if proc.returncode: raise RuntimeError(proc.stdout+proc.stderr)
        rebuilt_baseline_case("ordinary-non-equal-distribution-accepted", rebuild_with_ordinary_unequal)

        def option_length(c):
            for name in ("MCQ-QUESTIONS.md","MCQ-SOLUTIONS.md"):
                p=c/name; t=p.read_text(encoding="utf-8"); t=re.sub(r"(?m)^A\..+$","A. Yoga.",t,count=1); p.write_text(t,encoding="utf-8",newline="\n")
        case("option-length-cue", "MCQ_OPTION_LENGTH_CUE", option_length)

        def option_edit(c, transform):
            for name in ("MCQ-QUESTIONS.md","MCQ-SOLUTIONS.md"):
                p=c/name; p.write_text(transform(p.read_text(encoding="utf-8")),encoding="utf-8",newline="\n")
        case("option-format-cue", "MCQ_OPTION_FORMAT_CUE",
             lambda c:option_edit(c,lambda t:t.replace("Yoga is restraint of citta's modifications so the seer abides in its own nature.","Yoga is restraint of citta's modifications so the seer abides in its own nature!",1)))
        case("option-specificity-cue", "MCQ_OPTION_SPECIFICITY_CUE",
             lambda c:option_edit(c,lambda t:t.replace("Yoga is restraint of citta's modifications so the seer abides in its own nature.","YS 1.2 always and only exactly defines Yoga as restraint of citta's modifications so the seer abides in its own nature.",1)))
        case("option-lexical-cue", "MCQ_OPTION_LEXICAL_CUE",
             lambda c:option_edit(c,lambda t:t.replace("Which statement most accurately captures the Yoga doctrine of yoga as citta-vṛtti-nirodha?","Which statement most accurately captures transcendentalization phenomenologicality soteriologicality in the Yoga doctrine of yoga as citta-vṛtti-nirodha?",1).replace("Yoga is restraint of citta's modifications so the seer abides in its own nature.","Transcendentalization, phenomenologicality and soteriologicality describe Yoga as restraint of citta's modifications so the seer abides in its own nature.",1)))

        def mutate_later_question(c):
            old = "The distinction tracks object-support, residual saṃskāra in asamprajñāta, and its further restraint in nirbīja."
            new = "The distinction tracks posture, breath control, sensory withdrawal, and ritual recitation as equivalent stages."
            for name in ("MCQ-QUESTIONS.md","MCQ-SOLUTIONS.md"):
                p=c/name; t=p.read_text(encoding="utf-8")
                chunks=re.split(r"(?=^## MCQ 68\.)",t,flags=re.M)
                p.write_text(chunks[0]+chunks[1].replace(old,new),encoding="utf-8",newline="\n")
        case("copied-package-later-question-definition-mutated",
             "MCQ_FALSE_MAPPING", mutate_later_question)

        def redundant_stem(c):
            for name in ("MCQ-QUESTIONS.md","MCQ-SOLUTIONS.md"):
                p=c/name; t=p.read_text(encoding="utf-8"); stems=re.findall(r"Which statement most accurately captures[^\n]+",t); p.write_text(t.replace(stems[1],stems[0],1),encoding="utf-8",newline="\n")
        case("redundant-stem", "MCQ_REDUNDANT_STEM", redundant_stem)

        def pyq_wording(c):
            p=c/"PYQ-DEMAND-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8")); d["primary"][0]["exact_wording"]="altered"; write_json(p,d)
        case("pyq-wording-ownership", "PYQ_EXACT_WORDING_OR_MARKS", pyq_wording)

        def coordinated_builder_pyq_artifact_tamper(c):
            original = "How would Yoga philosophy comprehend the Citta-levels of a Scientist, a God-realized Devotee and a Self-realized Yogi? Justify your answer."
            altered = "How would Yoga philosophy classify three altered states? Justify your answer."
            builder = c/"build_package.py"
            builder.write_text(builder.read_text(encoding="utf-8").replace(original, altered, 1),
                               encoding="utf-8", newline="\n")
            snapshot_rel = "source-snapshots/pyq-2018-2025.md"
            snapshot = c/snapshot_rel
            snapshot.write_text(snapshot.read_text(encoding="utf-8").replace(original, altered, 1),
                                encoding="utf-8", newline="\n")
            digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
            registry = c/"SOURCE-REGISTRY.json"
            registry_data = json.loads(registry.read_text(encoding="utf-8"))
            registry_row = next(x for x in registry_data["sources"] if x["key"] == "pyq_2018_2025")
            registry_row.update(sha256=digest, bytes=snapshot.stat().st_size,
                                line_count=len(snapshot.read_text(encoding="utf-8").splitlines()))
            write_json(registry, registry_data)
            review = c/"FORMAL-COVERAGE-REVIEW.json"
            review_data = json.loads(review.read_text(encoding="utf-8"))
            review_data["sources"]["pyq_2018_2025"].update(
                sha256=digest, bytes=snapshot.stat().st_size,
                line_count=len(snapshot.read_text(encoding="utf-8").splitlines()),
            )
            write_json(review, review_data)
            audit = c/"PYQ-DEMAND-AUDIT.json"
            audit_data = json.loads(audit.read_text(encoding="utf-8"))
            audit_data["sources"]["2018_2025"].update(sha256=digest, bytes=snapshot.stat().st_size)
            audit_data["primary"][0]["exact_wording"] = altered
            write_json(audit, audit_data)
            for rel in ("build_package.py", "SOURCE-REGISTRY.json", snapshot_rel,
                        "FORMAL-COVERAGE-REVIEW.json", "PYQ-DEMAND-AUDIT.json"):
                refresh_artifact_hash(c, rel)
        case("coordinated-builder-pyq-snapshot-audit-tamper",
             "SOURCE_REGISTRY_TAMPER", coordinated_builder_pyq_artifact_tamper)

        def pyq_marks(c):
            p=c/"PYQ-DEMAND-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8")); d["primary"][0]["marks"]=10; write_json(p,d)
        case("pyq-marks", "PYQ_EXACT_WORDING_OR_MARKS", pyq_marks)

        def pyq_owner(c):
            p=c/"PYQ-DEMAND-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8")); d["primary"][0]["primary_owner"]="Samkhya"; write_json(p,d)
        case("pyq-ownership", "PYQ_EXACT_WORDING_OR_MARKS", pyq_owner)

        def pyq_component(c):
            p=c/"PYQ-DEMAND-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8")); d["primary"][0]["qualification_present"]=False; write_json(p,d)
        case("pyq-components", "PYQ_SOLUTION_COMPONENT_MISSING", pyq_component)

        def pyq_band(c):
            p=c/"PYQ-DEMAND-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8")); d["primary"][0]["model_word_count"]=149; write_json(p,d)
        case("pyq-word-band", "PYQ_WORD_BAND", pyq_band)

        def original_band(c):
            p=c/"PYQ-DEMAND-AUDIT.json"; d=json.loads(p.read_text(encoding="utf-8")); d["originals"][0]["model_word_count"]=149; write_json(p,d)
        case("original-word-band", "ORIGINAL_WORD_BAND", original_band)

        case("stale-source-artifact-audit", "SOURCE_ARTIFACT_STALE", lambda c:(c/"README.md").write_text((c/"README.md").read_text(encoding="utf-8")+"\nstale\n",encoding="utf-8"))
        case("markdown-only-pdf-file", "PDF_ARTIFACT_FORBIDDEN", lambda c:(c/"forbidden.pdf").write_bytes(b"%PDF"))
        case("markdown-only-pdf-directory", "PDF_ARTIFACT_FORBIDDEN", lambda c:(c/"pdf").mkdir())
        case("release-not-staged-clean-nonmutating", "RELEASE_NOT_STAGED", noop, release=True, nonmutating=True)
        case("release-mixed-state-nonmutating", "RELEASE_NOT_STAGED", lambda c:(c/"PRACTICE-LOG.md").write_text((c/"PRACTICE-LOG.md").read_text(encoding="utf-8")+"\nlocal mixed-state probe\n",encoding="utf-8"), release=True, nonmutating=True)
    finally:
        summary = {"schema_version": 3, "test_count": len(results), "passed_count": sum(x["passed"] for x in results),
                   "failed_count": sum(not x["passed"] for x in results), "results": results}
        (ROOT/"NEGATIVE-TEST-RESULTS.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
        if work.exists():
            shutil.rmtree(work)
    print(json.dumps(summary,ensure_ascii=True,indent=2))
    return 0 if summary["failed_count"]==0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
