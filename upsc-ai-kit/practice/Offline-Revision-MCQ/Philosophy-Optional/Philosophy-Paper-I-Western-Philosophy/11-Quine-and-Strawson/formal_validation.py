from __future__ import annotations

import copy
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path


TOPIC = Path(__file__).resolve().parent
REPO = TOPIC.parents[4]
FORMAL_ROOT = Path(
    r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final"
)
SOURCE_DIR = (
    FORMAL_ROOT
    / "Philosophy-Optional/Philosophy-Paper-I-—-Western-Philosophy/11-Quine-and-Strawson"
)
SOURCES = {
    "session": SOURCE_DIR / "Learning-Session.md",
    "workbook": SOURCE_DIR / "Solved-Practice-Workbook.md",
}
REVIEW = TOPIC / "FORMAL-COVERAGE-REVIEW.json"
AUDIT = TOPIC / "FORMAL-COVERAGE-AUDIT.json"
EXPECTED_PANELS = 42
EXPECTED_CLAIM_COUNT = 559
TARGET_MALFORMED_CLAIM_FAMILIES = (
    "standalone_subordinate_because",
    "elliptical_attribution_unresolved_pronoun",
)
EXPECTED_OBLIGATIONS = {
    "T11-ROUTE-T03-EMPIRICISM",
    "T11-ROUTE-T04-KANT-GENERAL",
    "T11-ROUTE-T04-BOUNDS-OF-SENSE",
    "T11-ROUTE-T06-DESCRIPTIONS",
    "T11-ROUTE-T07-POSITIVISM",
    "T11-ROUTE-T08-LATER-WITTGENSTEIN",
    "T11-ROUTE-P2-SOUL",
}
ALLOWED_CLASSIFICATIONS = {
    "covered_in_scope",
    "genuine_in_scope_omission",
    "routed_to_canonical_owner",
    "excluded_doubt_only_non_formal_enrichment",
}
ALLOWED_OBLIGATION_STATUSES = {"closed", "pending_external_serialization"}
FORBIDDEN_BROAD_ANCHORS = {"11. COMPLETE FORMAL ASCII MASTER FLOW — 42 PANELS"}
MALFORMED_CLAIM_PATTERNS = {
    "placeholder": r"source assigns a specific doctrinal or practice function",
    "old_review_template": r"records this reviewed proposition",
    "generic_relation_template": r"establishes the relation among",
    "split_synonymy": r"\bs\s+ynonym",
    "broken_case_the": r"\btHE\b",
    "ascii_rule_fragment": r"[-=]{4,}",
    "ascii_pipe_fragment": r"\|",
    "visual_token_fragment": r"\bvisual\s+(?:token|gateway)\b",
    "standalone_subordinate_because": r"(?i)^\s*because\b",
    "elliptical_attribution_unresolved_pronoun": (
        r"(?i)^\s*(?:[^\w\s]+\s*)?[a-z][a-z.'-]*"
        r"(?:\s+[a-z][a-z.'-]*)*\s*:\s*applied\b[^.;]*\bit\b"
    ),
}


def normalise(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.casefold().replace("’", "'")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9' -]+", " ", value)).strip()


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", normalise(value)).strip("-")[:64]


def extract_blocks() -> list[dict]:
    rows = []
    for source_code, path in SOURCES.items():
        text = path.read_text(encoding="utf-8")
        headings = list(re.finditer(r"(?m)^(#{2,5})\s+(.+?)\s*$", text))
        stack = []
        local = []
        for index, match in enumerate(headings):
            level = len(match.group(1))
            heading = match.group(2).strip()
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            while stack and stack[-1][0] >= level:
                stack.pop()
            children = []
            probe = index + 1
            while probe < len(headings) and len(headings[probe].group(1)) > level:
                if len(headings[probe].group(1)) == level + 1:
                    children.append(probe)
                probe += 1
            block_text = text[match.start():end].strip()
            block_hash = hashlib.sha256(
                unicodedata.normalize("NFC", block_text).encode()
            ).hexdigest()
            local.append(
                {
                    "id": (
                        f"{source_code}-{index + 1:03d}-{slug(heading)}-"
                        f"{block_hash[:10]}"
                    ),
                    "source_code": source_code,
                    "source_file": str(path),
                    "source_line": text.count("\n", 0, match.start()) + 1,
                    "heading_level": level,
                    "source_heading": heading,
                    "ancestor_headings": [item[1] for item in stack],
                    "block_text": block_text,
                    "body_text": text[match.end():end].strip(),
                    "source_block_sha256": block_hash,
                    "child_indexes": children,
                }
            )
            stack.append((level, heading))
        for row in local:
            row["child_ids"] = [local[index]["id"] for index in row.pop("child_indexes")]
        rows.extend(local)
    return rows


def distributed_segments(body_text: str) -> list[dict]:
    lines = [line for line in body_text.splitlines() if line.strip()]
    tokens = body_text.split()
    if len(lines) < 60 and len(tokens) < 400:
        return []
    if len(lines) >= 60:
        units, separator = lines, "\n"
    else:
        units, separator = tokens, " "
    boundaries = (0, len(units) // 3, 2 * len(units) // 3, len(units))
    return [
        {
            "label": label,
            "text": separator.join(units[boundaries[index] : boundaries[index + 1]]),
        }
        for index, label in enumerate(("beginning", "middle", "end"))
    ]


def extract_panels(text: str) -> list[dict]:
    markers = list(
        re.finditer(r"(?m)^ASCII MASTER FLOW - PANEL (\d+)/42: (.+)$", text)
    )
    rows = []
    for index, marker in enumerate(markers):
        end = (
            markers[index + 1].start()
            if index + 1 < len(markers)
            else text.find("END OF ASCII MASTER FLOW DIAGRAM", marker.end())
        )
        payload = text[marker.start() : end].rstrip()
        rows.append(
            {
                "number": int(marker.group(1)),
                "label": marker.group(2).strip(),
                "payload": payload,
                "sha256": hashlib.sha256(
                    unicodedata.normalize("NFC", payload).encode()
                ).hexdigest(),
            }
        )
    return rows


def bounded_destination(destination: dict) -> str:
    path = TOPIC / destination.get("file", "")
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    anchor = destination.get("anchor", "")
    if destination.get("anchor_kind") == "panel_marker":
        start = text.find(anchor)
        if start < 0:
            return ""
        following = re.search(
            r"(?m)^ASCII MASTER FLOW - PANEL \d+/42:",
            text[start + len(anchor) :],
        )
        end = (
            start + len(anchor) + following.start()
            if following
            else text.find("END OF ASCII MASTER FLOW DIAGRAM", start)
        )
        return text[start : end if end >= 0 else len(text)]
    match = re.search(rf"(?m)^#{{1,5}}\s+{re.escape(anchor)}\s*$", text)
    if not match:
        return ""
    current_level = len(re.match(r"^#+", match.group(0)).group(0))
    following_pattern = (
        rf"(?m)^#{{1,{current_level}}}\s+"
        if destination.get("include_descendants")
        else r"(?m)^#{1,5}\s+"
    )
    following = re.search(following_pattern, text[match.end() :])
    end = match.end() + following.start() if following else len(text)
    return text[match.start() : end]


def _witnesses_pass(witnesses: list[str], source: str, destination: str) -> bool:
    return (
        len(witnesses) >= 3
        and all(normalise(term) in normalise(source) for term in witnesses)
        and all(normalise(term) in normalise(destination) for term in witnesses)
    )


def recursive_descendants(block_id: str, block_map: dict[str, dict]) -> list[str]:
    result = []
    for child_id in block_map[block_id]["child_ids"]:
        result.append(child_id)
        result.extend(recursive_descendants(child_id, block_map))
    return result


def semantic_key_failures(key: dict, claim: str) -> list[str]:
    required = {"subject", "predicate", "object", "polarity", "role", "claim_sha256"}
    failures = []
    if set(key) != required or any(not str(key.get(name, "")).strip() for name in required):
        failures.append("semantic key is incomplete")
    expected_hash = hashlib.sha256(normalise(claim).encode()).hexdigest()
    if key.get("claim_sha256") != expected_hash:
        failures.append("semantic key claim hash mismatch")
    return failures


def claim_family_failures(claim: str) -> list[str]:
    failures = [
        name
        for name, pattern in MALFORMED_CLAIM_PATTERNS.items()
        if re.search(pattern, claim)
    ]
    if claim.count('"') % 2 or claim.count("“") != claim.count("”"):
        failures.append("unbalanced_quotation")
    if re.match(r"^\s*(?:[-*•]|\d+[.)])\s*(?:·\s*)?", claim):
        failures.append("list_fragment_non_proposition")
    return failures


def destination_audit_rows(path: Path) -> dict[str, dict]:
    if not path.is_file():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = {
        row.get("id"): row
        for row in payload.get("rows", payload.get("canonical_rows", []))
        if row.get("id")
    }
    rows.update(
        {
            row.get("id"): row
            for row in payload.get("inbound_obligations", [])
            if row.get("id")
        }
    )
    canonical_review = payload.get("canonical_review_file")
    if canonical_review:
        review_path = path.parent / canonical_review
        if review_path.is_file():
            review = json.loads(review_path.read_text(encoding="utf-8"))
            rows.update(
                {
                    row.get("id"): row
                    for row in review.get("inbound_obligations", [])
                    if row.get("id")
                }
            )
    return rows


def validate_obligations(
    review: dict,
    decisions: dict[str, dict],
    mode: str = "development",
    destination_validation_overrides: dict[str, dict] | None = None,
) -> dict:
    failures = []
    codes = set()
    release_blocking = []
    destination_modes = {}
    obligations = review.get("external_obligations", [])
    obligation_map = {row.get("id"): row for row in obligations if row.get("id")}
    if set(obligation_map) != EXPECTED_OBLIGATIONS:
        codes.add("external_obligation_set_mismatch")
        failures.append({"reason": "external obligation set mismatch"})
    linked = Counter()
    for decision in decisions.values():
        classification = decision.get("classification")
        route_links = decision.get("route_links", [])
        if classification not in ALLOWED_CLASSIFICATIONS:
            codes.add("invalid_classification")
            failures.append({"id": decision.get("id"), "reason": "invalid classification"})
        if classification == "routed_to_canonical_owner" and not route_links:
            codes.add("routed_decision_missing_link")
            failures.append({"id": decision.get("id"), "reason": "routed decision missing route link"})
        if classification != "routed_to_canonical_owner" and route_links:
            codes.add("non_routed_decision_has_link")
            failures.append({"id": decision.get("id"), "reason": "non-routed decision has route link"})
        for link in route_links:
            obligation = obligation_map.get(link.get("obligation_id"))
            if not obligation:
                codes.add("route_link_unknown_obligation")
                failures.append({"id": decision.get("id"), "reason": "route link references unknown obligation"})
                continue
            linked[obligation["id"]] += 1
            expected = {
                "owner": obligation.get("owner"),
                "status": obligation.get("status"),
                "release_blocking": obligation.get("release_blocking"),
            }
            actual = {name: link.get(name) for name in expected}
            if actual != expected:
                codes.add("route_link_field_mismatch")
                failures.append({"id": decision.get("id"), "reason": "route link field mismatch"})
    for obligation_id, obligation in obligation_map.items():
        status = obligation.get("status")
        if status not in ALLOWED_OBLIGATION_STATUSES:
            codes.add("external_obligation_status_mismatch")
            failures.append({"obligation": obligation_id, "reason": "invalid obligation status"})
        if not obligation.get("owner") or not obligation.get("concepts"):
            codes.add("obligation_owner_or_concepts_missing")
            failures.append({"obligation": obligation_id, "reason": "owner or concepts missing"})
        source_ids = obligation.get("source_decision_ids", [])
        if not source_ids or any(source_id not in decisions for source_id in source_ids):
            codes.add("obligation_source_binding_missing")
            failures.append({"obligation": obligation_id, "reason": "source decision binding missing"})
        if linked[obligation_id] != len(source_ids):
            codes.add("obligation_link_count_mismatch")
            failures.append({"obligation": obligation_id, "reason": "route link count mismatch"})
        canonical = Path(obligation.get("canonical_owner_path", ""))
        if not canonical.is_file():
            codes.add("canonical_owner_missing")
            failures.append({"obligation": obligation_id, "reason": "canonical owner missing"})
        recorded_release_blocking = obligation.get("release_blocking")
        if recorded_release_blocking != (status == "pending_external_serialization"):
            codes.add("release_blocking_status_mismatch")
            failures.append({"obligation": obligation_id, "reason": "release-blocking/status mismatch"})
        if status == "closed":
            package = Path(obligation.get("destination_package_path", ""))
            validator = Path(obligation.get("destination_validator_path", ""))
            validation_path = Path(obligation.get("destination_validation_path", ""))
            audit_path = Path(obligation.get("destination_audit_path", ""))
            if not package.is_dir() or not validator.is_file() or not validation_path.is_file() or not audit_path.is_file():
                codes.add("closed_destination_artifact_missing")
                failures.append({"obligation": obligation_id, "reason": "closed destination artifact missing"})
                continue
            validation_payload = (
                destination_validation_overrides.get(str(validation_path))
                if destination_validation_overrides
                and str(validation_path) in destination_validation_overrides
                else json.loads(validation_path.read_text(encoding="utf-8"))
            )
            validation_result = validation_payload.get("result")
            development_valid = validation_result in obligation.get(
                "destination_validation_accepted_results", []
            )
            release_valid = (
                validation_result == "RELEASE_PASS"
                and validation_payload.get("release_ready") is True
                and validation_payload.get("checks", {})
                .get("release_integrity", {})
                .get("pass")
                is True
            )
            release_probe = None
            if (
                mode == "precommit"
                and destination_validation_overrides is None
                and obligation.get("require_current_destination_evidence") is True
            ):
                completed = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        str(validator),
                        "--mode",
                        "precommit",
                    ],
                    cwd=package,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=600,
                )
                release_probe = {
                    "exit_code": completed.returncode,
                    "release_pass_observed": "RELEASE_PASS:" in completed.stdout,
                }
                release_valid = (
                    completed.returncode == 0
                    and release_probe["release_pass_observed"]
                )
            current_validation_sha256 = hashlib.sha256(
                validation_path.read_bytes()
            ).hexdigest()
            current_audit_sha256 = hashlib.sha256(
                audit_path.read_bytes()
            ).hexdigest()
            audit_rows = destination_audit_rows(audit_path)
            inbound_ids = obligation.get("destination_inbound_ids", [])
            inbound_payload = [
                audit_rows[inbound_id]
                for inbound_id in inbound_ids
                if inbound_id in audit_rows
            ]
            current_inbound_rows_sha256 = hashlib.sha256(
                json.dumps(
                    inbound_payload,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest()
            destination_modes[obligation_id] = {
                "validation_result": validation_result,
                "development_valid": development_valid,
                "release_valid": release_valid,
                "release_probe": release_probe,
                "validation_sha256": current_validation_sha256,
                "audit_sha256": current_audit_sha256,
                "inbound_rows_sha256": current_inbound_rows_sha256,
            }
            if not development_valid:
                codes.add("closed_destination_validation_failed")
                failures.append({"obligation": obligation_id, "reason": "closed destination validation result is not accepted"})
            if obligation.get("require_current_destination_evidence") is True:
                evidence_fields = {
                    "destination_validation_sha256": current_validation_sha256,
                    "destination_validated_at": validation_payload.get("validated_at"),
                    "destination_audit_sha256": current_audit_sha256,
                    "destination_inbound_rows_sha256": current_inbound_rows_sha256,
                }
                for field, current_value in evidence_fields.items():
                    if obligation.get(field) != current_value:
                        codes.add("closed_destination_evidence_stale")
                        failures.append(
                            {
                                "obligation": obligation_id,
                                "reason": f"stale destination evidence: {field}",
                            }
                        )
            if (
                mode == "precommit"
                and obligation.get("require_current_destination_evidence") is True
                and not release_valid
            ):
                codes.add("closed_destination_release_not_ready")
                failures.append(
                    {
                        "obligation": obligation_id,
                        "reason": "closed destination has development evidence but lacks RELEASE_PASS/current-index integrity",
                    }
                )
                release_blocking.append(obligation_id)
            if not inbound_ids or any(inbound_id not in audit_rows for inbound_id in inbound_ids):
                codes.add("closed_destination_inbound_id_missing")
                failures.append({"obligation": obligation_id, "reason": "closed destination inbound ID missing"})
            evidence_text = " ".join(
                json.dumps(audit_rows[inbound_id], ensure_ascii=False)
                for inbound_id in inbound_ids
                if inbound_id in audit_rows
            )
            evidence_text += " " + canonical.read_text(encoding="utf-8")
            for evidence_file in (
                package / "REVISION-GUIDE.md",
                package / "COVERAGE-LEDGER.md",
                package / "ANSWER-WRITING-TOOLKIT.md",
            ):
                if evidence_file.is_file():
                    evidence_text += " " + evidence_file.read_text(encoding="utf-8")
            for concept in obligation.get("concepts", []):
                significant = [
                    token for token in normalise(concept).split() if len(token) >= 5
                ]
                if significant and not any(token in normalise(evidence_text) for token in significant):
                    codes.add("closed_destination_concept_evidence_missing")
                    failures.append({"obligation": obligation_id, "reason": f"destination evidence missing concept: {concept}"})
        else:
            release_blocking.append(obligation_id)
            if obligation.get("destination_inbound_ids"):
                codes.add("pending_obligation_claims_inbound_closure")
                failures.append({"obligation": obligation_id, "reason": "pending obligation claims inbound closure"})
            if obligation.get("destination_package_path") is not None:
                codes.add("pending_obligation_claims_existing_package")
                failures.append({"obligation": obligation_id, "reason": "pending obligation claims existing destination package"})
    local = review.get("local_bounded_enrichments", [])
    if len(local) != 1 or local[0].get("id") != "T11-LOCAL-STRA-REACTIVE":
        codes.add("local_reactive_disposition_missing")
        failures.append({"reason": "local reactive-attitudes disposition missing"})
    elif local[0].get("external_obligation") is not False:
        codes.add("local_reactive_marked_external")
        failures.append({"reason": "reactive attitudes incorrectly marked external"})
    else:
        for evidence in local[0].get("package_evidence", []):
            if not _witnesses_pass(
                evidence.get("witnesses", []),
                bounded_destination(
                    {
                        "file": evidence.get("file"),
                        "anchor": evidence.get("anchor"),
                        "anchor_kind": "heading",
                        "include_descendants": evidence.get(
                            "include_descendants", False
                        ),
                    }
                ),
                bounded_destination(
                    {
                        "file": evidence.get("file"),
                        "anchor": evidence.get("anchor"),
                        "anchor_kind": "heading",
                        "include_descendants": evidence.get(
                            "include_descendants", False
                        ),
                    }
                ),
            ):
                codes.add("local_reactive_evidence_missing")
                failures.append({"reason": "local reactive-attitudes evidence missing"})
    return {
        "obligations": obligations,
        "pending": sorted(
            row["id"]
            for row in obligations
            if row.get("status") == "pending_external_serialization"
        ),
        "closed": sorted(row["id"] for row in obligations if row.get("status") == "closed"),
        "release_blocking": sorted(set(release_blocking)),
        "destination_modes": destination_modes,
        "failure_codes": sorted(codes),
        "failures": failures,
        "pass": not failures,
    }


def validate_review(
    review: dict,
    blocks: list[dict],
    mode: str = "development",
    destination_validation_overrides: dict[str, dict] | None = None,
) -> dict:
    failures = []
    codes = set()
    expected = {row["id"]: row for row in blocks}
    decisions = {row.get("id"): row for row in review.get("decisions", [])}
    if review.get("schema_version") != 2:
        codes.add("review_schema_mismatch")
        failures.append({"reason": "review schema mismatch"})
    if set(decisions) != set(expected):
        codes.add("formal_block_set_mismatch")
        failures.append({"reason": "formal block set mismatch"})
    claims = []
    claim_family_counts = Counter()
    scanned_claim_count = 0
    destinations_seen = []

    def scan_claim(value: str) -> list[str]:
        nonlocal scanned_claim_count
        scanned_claim_count += 1
        families = claim_family_failures(value)
        claim_family_counts.update(families)
        return families

    for block_id, block in expected.items():
        decision = decisions.get(block_id)
        if not decision:
            continue
        if decision.get("source_block_sha256") != block["source_block_sha256"]:
            codes.add("stale_source_hash")
            failures.append({"id": block_id, "reason": "stale source hash"})
        segments = (
            distributed_segments(block["body_text"]) if not block["child_ids"] else []
        )
        expected_mode = (
            "structural_umbrella"
            if block["child_ids"]
            else "large_leaf_distributed"
            if segments
            else "leaf_full_block"
        )
        if decision.get("coverage_mode") != expected_mode:
            codes.add("coverage_mode_mismatch")
            failures.append({"id": block_id, "reason": "coverage mode mismatch"})
        umbrella = decision.get("structural_umbrella")
        if block["child_ids"] and (
            not umbrella or umbrella.get("direct_child_ids") != block["child_ids"]
        ):
            codes.add("structural_child_union_mismatch")
            failures.append({"id": block_id, "reason": "structural child union mismatch"})
        if not block["child_ids"] and umbrella is not None:
            codes.add("leaf_declares_umbrella")
            failures.append({"id": block_id, "reason": "leaf declares umbrella"})
        umbrella = umbrella or {}
        claim = normalise(decision.get("semantic_claim", ""))
        if len(claim.split()) < 10 or claim in {
            "this block covers the topic",
            "the topic is covered",
            "coverage is complete",
        }:
            codes.add("generic_semantic_claim")
            failures.append({"id": block_id, "reason": "generic semantic claim"})
        malformed = scan_claim(decision.get("semantic_claim", ""))
        if malformed:
            codes.add("malformed_semantic_claim")
            failures.append(
                {"id": block_id, "reason": "malformed semantic claim", "families": malformed}
            )
        key_failures = semantic_key_failures(
            decision.get("semantic_key", {}), decision.get("semantic_claim", "")
        )
        if key_failures:
            codes.add("semantic_key_failure")
            failures.append(
                {"id": block_id, "reason": "semantic key failure", "details": key_failures}
            )
        claims.append(claim)
        destinations = decision.get("package_destinations", [])
        if not destinations:
            codes.add("missing_destination")
            failures.append({"id": block_id, "reason": "missing destination"})
        for destination in destinations:
            if destination.get("anchor") in FORBIDDEN_BROAD_ANCHORS:
                codes.add("whole_atlas_generic_binding")
                failures.append({"id": block_id, "reason": "whole-atlas generic binding"})
            destination_text = bounded_destination(destination)
            if not destination_text:
                codes.add("destination_anchor_absent")
                failures.append({"id": block_id, "reason": "destination anchor absent"})
            if not block["child_ids"] and not _witnesses_pass(
                destination.get("witnesses", []),
                " ".join(block["ancestor_headings"])
                + " "
                + block["source_heading"]
                + " "
                + block["block_text"],
                destination_text,
            ):
                codes.add("source_destination_correspondence_failure")
                failures.append(
                    {"id": block_id, "reason": "source/destination correspondence failure"}
                )
            if (
                not block["child_ids"]
                and set(destination.get("concept_witnesses", []))
                != set(destination.get("witnesses", [])[:4])
            ):
                codes.add("concept_correspondence_failure")
                failures.append({"id": block_id, "reason": "concept correspondence failure"})
            destinations_seen.append(
                (block_id, destination.get("file"), destination.get("anchor"))
            )
        actual_segments = decision.get("distributed_units", [])
        if segments:
            if [row.get("label") for row in actual_segments] != [
                "beginning",
                "middle",
                "end",
            ]:
                codes.add("large_leaf_segment_mismatch")
                failures.append({"id": block_id, "reason": "large leaf segment mismatch"})
            for expected_segment, actual_segment in zip(segments, actual_segments):
                segment_hash = hashlib.sha256(
                    unicodedata.normalize("NFC", expected_segment["text"]).encode()
                ).hexdigest()
                if actual_segment.get("source_sha256") != segment_hash:
                    codes.add("large_leaf_segment_hash_mismatch")
                    failures.append({"id": block_id, "reason": "large leaf hash mismatch"})
                destination = actual_segment.get("destination", {})
                unit_claim = actual_segment.get("semantic_claim", "")
                claims.append(normalise(unit_claim))
                malformed_unit = scan_claim(unit_claim)
                if len(normalise(unit_claim).split()) < 10 or malformed_unit:
                    codes.add("malformed_large_leaf_claim")
                    failures.append(
                        {
                            "id": block_id,
                            "reason": "malformed large-leaf claim",
                            "segment": expected_segment["label"],
                            "families": malformed_unit,
                        }
                    )
                unit_key_failures = semantic_key_failures(
                    actual_segment.get("semantic_key", {}), unit_claim
                )
                if unit_key_failures:
                    codes.add("large_leaf_semantic_key_failure")
                    failures.append(
                        {
                            "id": block_id,
                            "reason": "large-leaf semantic key failure",
                            "segment": expected_segment["label"],
                        }
                    )
                if not _witnesses_pass(
                    destination.get("witnesses", []),
                    expected_segment["text"],
                    bounded_destination(destination),
                ):
                    codes.add("large_leaf_correspondence_failure")
                    failures.append(
                        {"id": block_id, "reason": "large leaf correspondence failure"}
                    )
        elif actual_segments:
            codes.add("unexpected_distributed_units")
            failures.append({"id": block_id, "reason": "unexpected distributed units"})
        if block["child_ids"]:
            expected_descendants = recursive_descendants(block_id, expected)
            parent_body = block["body_text"]
            if umbrella.get("recursive_descendant_ids") != expected_descendants:
                codes.add("recursive_child_union_mismatch")
                failures.append({"id": block_id, "reason": "recursive child union mismatch"})
            if bool(parent_body) != bool(umbrella.get("parent_only_body_required")):
                codes.add("parent_only_body_requirement_mismatch")
                failures.append({"id": block_id, "reason": "parent-only body requirement mismatch"})
            if parent_body:
                expected_hash = hashlib.sha256(parent_body.encode()).hexdigest()
                if umbrella.get("parent_only_body_sha256") != expected_hash:
                    codes.add("parent_only_body_hash_mismatch")
                    failures.append({"id": block_id, "reason": "parent-only body hash mismatch"})
                parent_claim = umbrella.get("parent_only_semantic_claim", "")
                claims.append(normalise(parent_claim))
                malformed_parent = scan_claim(parent_claim)
                if len(normalise(parent_claim).split()) < 10 or malformed_parent:
                    codes.add("parent_only_semantic_claim_failure")
                    failures.append({"id": block_id, "reason": "parent-only semantic claim failure"})
                if semantic_key_failures(
                    umbrella.get("parent_only_semantic_key", {}), parent_claim
                ):
                    codes.add("parent_only_semantic_key_failure")
                    failures.append({"id": block_id, "reason": "parent-only semantic key failure"})
                parent_destination = umbrella.get("parent_only_destination") or {}
                if not _witnesses_pass(
                    parent_destination.get("witnesses", []),
                    parent_body,
                    bounded_destination(parent_destination),
                ):
                    codes.add("parent_only_correspondence_failure")
                    failures.append({"id": block_id, "reason": "parent-only correspondence failure"})
            elif any(
                umbrella.get(name)
                for name in (
                    "parent_only_body_sha256",
                    "parent_only_semantic_claim",
                    "parent_only_semantic_key",
                    "parent_only_source_witnesses",
                    "parent_only_destination",
                )
            ):
                codes.add("empty_parent_declares_body_evidence")
                failures.append({"id": block_id, "reason": "empty parent declares body evidence"})
    source_panels = extract_panels(SOURCES["session"].read_text(encoding="utf-8"))
    destination_panels = extract_panels(
        (TOPIC / "REVISION-GUIDE.md").read_text(encoding="utf-8")
    )
    reviewed_panels = review.get("panels", [])
    if any(
        len(rows) != EXPECTED_PANELS
        for rows in (source_panels, destination_panels, reviewed_panels)
    ):
        codes.add("panel_count_mismatch")
        failures.append({"reason": "panel count mismatch"})
    source_order = [(row["number"], row["label"]) for row in source_panels]
    destination_order = [(row["number"], row["label"]) for row in destination_panels]
    review_order = [(row.get("number"), row.get("label")) for row in reviewed_panels]
    if source_order != destination_order or source_order != review_order:
        codes.add("panel_order_or_label_mismatch")
        failures.append({"reason": "panel order or label mismatch"})
    for source, destination, reviewed in zip(
        source_panels, destination_panels, reviewed_panels
    ):
        if (
            source["sha256"] != destination["sha256"]
            or reviewed.get("source_payload_sha256") != source["sha256"]
            or reviewed.get("destination_payload_sha256") != destination["sha256"]
        ):
            codes.add("panel_payload_mismatch")
            failures.append({"panel": source["number"], "reason": "panel payload mismatch"})
        if len(reviewed.get("witnesses", [])) < 3:
            codes.add("panel_witness_failure")
            failures.append({"panel": source["number"], "reason": "panel witness failure"})
        elif not _witnesses_pass(
            reviewed.get("witnesses", []), source["payload"], destination["payload"]
        ):
            codes.add("panel_correspondence_failure")
            failures.append(
                {"panel": source["number"], "reason": "panel correspondence failure"}
            )
        panel_claim = reviewed.get("semantic_claim", "")
        claims.append(normalise(panel_claim))
        malformed_panel = scan_claim(panel_claim)
        if len(normalise(panel_claim).split()) < 10 or malformed_panel:
            codes.add("malformed_panel_claim")
            failures.append(
                {
                    "panel": source["number"],
                    "reason": "malformed panel claim",
                    "families": malformed_panel,
                }
            )
        if semantic_key_failures(reviewed.get("semantic_key", {}), panel_claim):
            codes.add("panel_semantic_key_failure")
            failures.append(
                {"panel": source["number"], "reason": "panel semantic key failure"}
            )
    if scanned_claim_count != EXPECTED_CLAIM_COUNT:
        codes.add("semantic_claim_scan_count_mismatch")
        failures.append(
            {
                "reason": "semantic claim scan count mismatch",
                "expected": EXPECTED_CLAIM_COUNT,
                "actual": scanned_claim_count,
            }
        )
    target_family_counts = {
        name: claim_family_counts[name]
        for name in TARGET_MALFORMED_CLAIM_FAMILIES
    }
    duplicates = [
        claim for claim, count in Counter(claims).items() if claim and count > 1
    ]
    if duplicates:
        codes.add("duplicate_semantic_claim")
        failures.append({"reason": "duplicate semantic claim", "count": len(duplicates)})
    routing = validate_obligations(
        review,
        decisions,
        mode=mode,
        destination_validation_overrides=destination_validation_overrides,
    )
    codes.update(routing["failure_codes"])
    failures.extend(routing["failures"])
    return {
        "formal_block_count": len(blocks),
        "decision_count": len(decisions),
        "structural_umbrellas": sum(bool(row["child_ids"]) for row in blocks),
        "leaf_blocks": sum(not row["child_ids"] for row in blocks),
        "large_leaf_blocks": sum(
            not row["child_ids"] and bool(distributed_segments(row["body_text"]))
            for row in blocks
        ),
        "distributed_units": sum(
            len(distributed_segments(row["body_text"])) if not row["child_ids"] else 0
            for row in blocks
        ),
        "panel_count": len(source_panels),
        "semantic_claim_scan": {
            "claim_count": scanned_claim_count,
            "expected_claim_count": EXPECTED_CLAIM_COUNT,
            "target_family_counts": target_family_counts,
            "all_malformed_family_counts": dict(sorted(claim_family_counts.items())),
            "pass": (
                scanned_claim_count == EXPECTED_CLAIM_COUNT
                and not claim_family_counts
            ),
        },
        "external_obligation_count": len(routing["obligations"]),
        "external_obligations_pending": routing["pending"],
        "external_obligations_closed": routing["closed"],
        "external_obligations_release_blocking": routing["release_blocking"],
        "external_destination_modes": routing["destination_modes"],
        "classification_counts": dict(
            Counter(row.get("classification") for row in decisions.values())
        ),
        "duplicate_destination_bindings": [
            list(pair)
            for pair, count in Counter(destinations_seen).items()
            if count > 1
        ],
        "failure_codes": sorted(codes),
        "failures": failures,
        "pass": not failures,
    }


def negative_tests(review: dict, blocks: list[dict]) -> dict:
    tests = []

    def run(
        name: str,
        mutation,
        expected: str,
        mode: str = "development",
        destination_validation_overrides: dict[str, dict] | None = None,
    ) -> None:
        candidate = copy.deepcopy(review)
        mutation(candidate)
        result = validate_review(
            candidate,
            blocks,
            mode=mode,
            destination_validation_overrides=destination_validation_overrides,
        )
        tests.append(
            {
                "name": name,
                "expected_failure_code": expected,
                "actual_failure_codes": result["failure_codes"],
                "rejected": expected in result["failure_codes"],
                "pass": expected in result["failure_codes"],
            }
        )

    run("formal block removed", lambda row: row["decisions"].pop(), "formal_block_set_mismatch")
    run(
        "source hash stale",
        lambda row: row["decisions"][0].__setitem__("source_block_sha256", "0" * 64),
        "stale_source_hash",
    )
    umbrella = next(
        index
        for index, row in enumerate(review["decisions"])
        if row.get("structural_umbrella")
    )
    run(
        "structural child removed",
        lambda row: row["decisions"][umbrella]["structural_umbrella"][
            "direct_child_ids"
        ].pop(),
        "structural_child_union_mismatch",
    )
    run(
        "recursive structural descendant removed",
        lambda row: row["decisions"][umbrella]["structural_umbrella"][
            "recursive_descendant_ids"
        ].pop(),
        "recursive_child_union_mismatch",
    )
    parent_body = next(
        index
        for index, row in enumerate(review["decisions"])
        if (row.get("structural_umbrella") or {}).get("parent_only_body_required")
    )
    run(
        "parent-only body hash changed",
        lambda row: row["decisions"][parent_body]["structural_umbrella"].__setitem__(
            "parent_only_body_sha256", "0" * 64
        ),
        "parent_only_body_hash_mismatch",
    )
    run(
        "parent-only semantic proposition removed",
        lambda row: row["decisions"][parent_body]["structural_umbrella"].__setitem__(
            "parent_only_semantic_claim", "This block covers the topic."
        ),
        "parent_only_semantic_claim_failure",
    )
    large = next(
        index for index, row in enumerate(review["decisions"]) if row.get("distributed_units")
    )
    run(
        "large leaf end removed",
        lambda row: row["decisions"][large]["distributed_units"].pop(),
        "large_leaf_segment_mismatch",
    )
    run(
        "generic semantic claim",
        lambda row: row["decisions"][1].__setitem__(
            "semantic_claim", "This block covers the topic."
        ),
        "generic_semantic_claim",
    )
    run(
        "semantic claim duplicated",
        lambda row: row["decisions"][1].__setitem__(
            "semantic_claim", row["decisions"][0]["semantic_claim"]
        ),
        "duplicate_semantic_claim",
    )
    run(
        "whole-atlas generic binding",
        lambda row: row["decisions"][1]["package_destinations"][0].__setitem__(
            "anchor", "11. COMPLETE FORMAL ASCII MASTER FLOW — 42 PANELS"
        ),
        "whole_atlas_generic_binding",
    )
    for name, malformed in (
        ("malformed split synonymy", "The claim relies on s ynonymy as evidence."),
        ("malformed case token", "The claim says tHE doctrine is complete."),
        ("malformed visual token", "The visual gateway token covers the doctrine."),
    ):
        run(
            name,
            lambda row, value=malformed: row["decisions"][large][
                "distributed_units"
            ][0].__setitem__(
                "semantic_claim",
                value,
            ),
            "malformed_large_leaf_claim",
        )
    run(
        "unbalanced quotation",
        lambda row: row["decisions"][1].__setitem__(
            "semantic_claim",
            'Quine rejects "sentence-by-sentence reductionism while preserving empiricism.',
        ),
        "malformed_semantic_claim",
    )
    run(
        "numbered list-fragment non-proposition",
        lambda row: row["decisions"][1].__setitem__(
            "semantic_claim",
            "3) · reconstruction detached from use and induction.",
        ),
        "malformed_semantic_claim",
    )
    run(
        "standalone subordinate Because clause",
        lambda row: row["decisions"][1].__setitem__(
            "semantic_claim",
            "Because the supporting premise remains dependent on an unstated main clause.",
        ),
        "malformed_semantic_claim",
    )
    run(
        "elliptical attribution with unresolved pronoun",
        lambda row: row["decisions"][1].__setitem__(
            "semantic_claim",
            "Searle and Evans: applied reflexively it entails an indeterminate result.",
        ),
        "malformed_semantic_claim",
    )
    routed = next(
        index
        for index, row in enumerate(review["decisions"])
        if row.get("classification") == "routed_to_canonical_owner"
    )
    run(
        "classification enum changed",
        lambda row: row["decisions"][routed].__setitem__(
            "classification", "route_elsewhere"
        ),
        "invalid_classification",
    )
    run(
        "routed row link removed",
        lambda row: row["decisions"][routed].__setitem__("route_links", []),
        "routed_decision_missing_link",
    )
    run("panel removed", lambda row: row["panels"].pop(), "panel_count_mismatch")
    run(
        "panel order swapped",
        lambda row: row["panels"].__setitem__(
            slice(0, 2), list(reversed(row["panels"][:2]))
        ),
        "panel_order_or_label_mismatch",
    )
    run(
        "panel semantic claim malformed",
        lambda row: row["panels"][0].__setitem__(
            "semantic_claim", "The panel says tHE visual token is sufficient."
        ),
        "malformed_panel_claim",
    )
    run(
        "panel payload hash changed",
        lambda row: row["panels"][0].__setitem__(
            "destination_payload_sha256", "0" * 64
        ),
        "panel_payload_mismatch",
    )
    run(
        "external obligation removed",
        lambda row: row["external_obligations"].pop(),
        "external_obligation_set_mismatch",
    )
    closed = next(
        index
        for index, row in enumerate(review["external_obligations"])
        if row.get("status") == "closed"
    )
    run(
        "route owner changed",
        lambda row: row["external_obligations"][closed].__setitem__(
            "owner", "Wrong owner"
        ),
        "route_link_field_mismatch",
    )
    run(
        "route status invalid",
        lambda row: row["external_obligations"][closed].__setitem__(
            "status", "assumed_closed"
        ),
        "external_obligation_status_mismatch",
    )
    run(
        "route destination missing",
        lambda row: row["external_obligations"][closed].__setitem__(
            "destination_package_path", r"C:\missing-topic-package"
        ),
        "closed_destination_artifact_missing",
    )
    run(
        "route concept unsupported",
        lambda row: row["external_obligations"][closed].__setitem__(
            "concepts", ["xylophonic zephyrous"]
        ),
        "closed_destination_concept_evidence_missing",
    )
    soul = next(
        index
        for index, row in enumerate(review["external_obligations"])
        if row.get("id") == "T11-ROUTE-P2-SOUL"
    )
    soul_validation_path = review["external_obligations"][soul][
        "destination_validation_path"
    ]
    run(
        "development-only Soul destination cannot satisfy release",
        lambda row: None,
        "closed_destination_release_not_ready",
        mode="precommit",
        destination_validation_overrides={
            soul_validation_path: {
                "result": "DEVELOPMENT_PASS",
                "release_ready": False,
                "checks": {"release_integrity": {"pass": False}},
            }
        },
    )
    run(
        "route inbound ID removed",
        lambda row: row["external_obligations"][closed].__setitem__(
            "destination_inbound_ids", []
        ),
        "closed_destination_inbound_id_missing",
    )
    return {
        "tests": tests,
        "passed": sum(row["pass"] for row in tests),
        "failed": sum(not row["pass"] for row in tests),
        "all_negative_tests_pass": all(row["pass"] for row in tests),
    }


def build_audit(mode: str = "development") -> dict:
    blocks = extract_blocks()
    review = json.loads(REVIEW.read_text(encoding="utf-8"))
    validation = validate_review(review, blocks, mode=mode)
    production = (
        negative_tests(review, blocks)
        if validation["pass"]
        else {
            "tests": [],
            "passed": 0,
            "failed": 1,
            "all_negative_tests_pass": False,
            "reason": "baseline review must pass before mutation testing",
        }
    )
    decisions = {row["id"]: row for row in review.get("decisions", [])}
    rows = []
    for block in blocks:
        decision = decisions.get(block["id"], {})
        rows.append(
            {
                "id": block["id"],
                "source_file": block["source_file"],
                "source_line": block["source_line"],
                "heading_level": block["heading_level"],
                "source_heading": block["source_heading"],
                "ancestor_headings": block["ancestor_headings"],
                "source_block_sha256": block["source_block_sha256"],
                "classification": decision.get("classification"),
                "coverage_mode": decision.get("coverage_mode"),
                "semantic_claim": decision.get("semantic_claim"),
                "semantic_key": decision.get("semantic_key"),
                "package_destinations": decision.get("package_destinations", []),
                "structural_umbrella": decision.get("structural_umbrella"),
                "large_leaf_detection": {
                    "is_large_leaf": (
                        not block["child_ids"]
                        and bool(distributed_segments(block["body_text"]))
                    ),
                    "distributed_units": [
                        row["label"]
                        for row in (
                            distributed_segments(block["body_text"])
                            if not block["child_ids"]
                            else []
                        )
                    ],
                },
                "distributed_proposition_inventory": decision.get(
                    "distributed_units", []
                ),
                "route_links": decision.get("route_links", []),
                "validation_result": "pass" if block["id"] in decisions else "fail",
            }
        )
    return {
        "schema_version": 1,
        "topic": "11 Quine and Strawson",
        "validation_mode": mode,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "formal_block_definition": (
            "Every level-2 through level-5 heading in the authoritative completed "
            "session and workbook. Structural parents retain their child union, large "
            "leaves retain beginning/middle/end segments, and the master flow is also "
            "checked as forty-two ordered bounded panels. Extraction never authors decisions."
        ),
        "source_files": {
            code: {
                "path": str(path),
                "bytes": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
            for code, path in SOURCES.items()
        },
        "review_decision_layer": {
            "path": REVIEW.name,
            "sha256": hashlib.sha256(REVIEW.read_bytes()).hexdigest(),
            "decision_count": len(review.get("decisions", [])),
            "refresh_mutates_review_layer": False,
        },
        "summary": validation,
        "coverage_negative_tests": production,
        "panel_parity": review.get("panels", []),
        "external_obligations": review.get("external_obligations", []),
        "release_blocked_by_external_obligations": bool(
            validation.get("external_obligations_release_blocking")
        ),
        "blocks": rows,
        "pass": validation["pass"] and production["all_negative_tests_pass"],
    }


def refresh_audit(mode: str = "development") -> dict:
    review_hash = hashlib.sha256(REVIEW.read_bytes()).hexdigest()
    payload = build_audit(mode=mode)
    AUDIT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    if hashlib.sha256(REVIEW.read_bytes()).hexdigest() != review_hash:
        raise RuntimeError("audit refresh mutated authored review decisions")
    return payload


def validate_audit(mode: str = "development") -> dict:
    if not REVIEW.is_file() or not AUDIT.is_file():
        return {"pass": False, "reason": "formal review or audit missing"}
    expected = build_audit(mode=mode)
    recorded = json.loads(AUDIT.read_text(encoding="utf-8"))
    keys = (
        "source_files",
        "review_decision_layer",
        "coverage_negative_tests",
        "panel_parity",
        "external_obligations",
        "release_blocked_by_external_obligations",
        "blocks",
        "pass",
    )
    recorded_summary = copy.deepcopy(recorded.get("summary", {}))
    expected_summary = copy.deepcopy(expected.get("summary", {}))
    recorded_summary.pop("external_destination_modes", None)
    expected_summary.pop("external_destination_modes", None)
    parity = (
        recorded_summary == expected_summary
        and all(recorded.get(key) == expected.get(key) for key in keys)
    )
    return {
        "formal_block_count": expected["summary"]["formal_block_count"],
        "structural_umbrellas": expected["summary"]["structural_umbrellas"],
        "large_leaf_blocks": expected["summary"]["large_leaf_blocks"],
        "distributed_units": expected["summary"]["distributed_units"],
        "panel_count": expected["summary"]["panel_count"],
        "semantic_claim_scan": expected["summary"]["semantic_claim_scan"],
        "external_obligations_pending": expected["summary"][
            "external_obligations_pending"
        ],
        "external_obligations_release_blocking": expected["summary"][
            "external_obligations_release_blocking"
        ],
        "external_destination_modes": expected["summary"][
            "external_destination_modes"
        ],
        "recorded_matches_current_sources_review_and_destinations": parity,
        "review_validation": expected["summary"],
        "coverage_negative_tests": expected["coverage_negative_tests"],
        "release_blocked_by_external_obligations": expected[
            "release_blocked_by_external_obligations"
        ],
        "pass": expected["pass"] and parity,
    }
