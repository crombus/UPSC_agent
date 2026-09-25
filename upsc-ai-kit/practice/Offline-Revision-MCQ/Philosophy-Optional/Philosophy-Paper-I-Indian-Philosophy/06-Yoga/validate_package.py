from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IST = timezone(timedelta(hours=5, minutes=30))
AUTHORITY_MANIFEST = "PRIMARY-SOURCE-AUTHORITY.json"
AUTHORITY_MANIFEST_SHA256 = "3fd1ecaa0596ec84b5d9016f1b120e18363e88aa523fd000c05fbee9ef11d709"
SOURCE_REGISTRY = "SOURCE-REGISTRY.json"
SOURCE_REGISTRY_SHA256 = "5699504811d12b2d2c9cce2dc3a8d1d3dbc6961665a7eefb502e1280c2a46cb5"
BASE_ARTIFACTS = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
    "COVERAGE-LEDGER.md", "FORMAL-COVERAGE-AUDIT.json", "FORMAL-COVERAGE-REVIEW.json",
    "SOURCE-PROPOSITION-INVENTORY.json", "TESTABLE-OBLIGATIONS.json", "TEST-MATRIX.json",
    "MCQ-AUDIT.json", "PYQ-DEMAND-AUDIT.json", "PRACTICE-LOG.md",
    "ANSWER-WRITING-TOOLKIT.md", "FORMAL-SOURCE-MIRROR.md",
    SOURCE_REGISTRY,
    "build_package.py", "validate_package.py", "run_negative_tests.py", "render_pdfs.py", ".gitattributes",
]
REQUIRED_STATIC = BASE_ARTIFACTS + [AUTHORITY_MANIFEST, "SOURCE-ARTIFACT-AUDIT.json", "VALIDATION.json"]
SOURCE_ORDER = ("formal_session", "formal_workbook", "canonical", "supplementary_complete", "supplementary_layered", "supplementary_workbook")
EXPECTED_SOURCE_KEYS = SOURCE_ORDER + ("pyq_2018_2025", "pyq_2026")
EXPECTED_SOURCE_ROLES = {
    "formal_session": "mandatory_formal_session",
    "formal_workbook": "mandatory_formal_workbook",
    "canonical": "mandatory_canonical_boundary_owner",
    "supplementary_complete": "supplementary_depth",
    "supplementary_layered": "supplementary_depth",
    "supplementary_workbook": "supplementary_depth",
    "pyq_2018_2025": "hash_bound_pyq_authority",
    "pyq_2026": "hash_bound_pyq_authority",
}
ANSWER_IMBALANCE_MIN_SHARE = 0.10
ANSWER_IMBALANCE_MAX_SHARE = 0.40
ANSWER_CHI_SQUARE_MAX = 11.345
KEYED_MEDIAN_RATIO_THRESHOLD = 3.2
KEYED_SPECIFICITY_DELTA_THRESHOLD = 2


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_text(text: str) -> str:
    return sha_bytes(text.replace("\r\n", "\n").encode("utf-8"))


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).casefold()


def words(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text, re.UNICODE))


def slug(text: str) -> str:
    return re.sub(r"[^\w]+", "-", re.sub(r"<[^>]+>", "", text).lower(), flags=re.UNICODE).strip("-")[:72] or "block"


def heading_blocks(path: Path, prefix: str) -> list[dict]:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    heads = []
    for i, line in enumerate(lines):
        match = re.match(r"^(#{2,4})\s+(.+?)\s*$", line)
        if match:
            heads.append((i, len(match.group(1)), match.group(2)))
    rows = []
    for idx, (start, level, heading) in enumerate(heads):
        own_end = heads[idx + 1][0] if idx + 1 < len(heads) else len(lines)
        subtree_end = len(lines)
        for later_start, later_level, _ in heads[idx + 1:]:
            if later_level <= level:
                subtree_end = later_start
                break
        payload = "\n".join(lines[start:own_end]).strip() + "\n"
        subtree = "\n".join(lines[start:subtree_end]).strip() + "\n"
        ident = f"{prefix}-{idx + 1:03d}-{slug(heading)}-{sha_text(payload)[:10]}"
        rows.append({
            "id": ident, "source": prefix, "ordinal": idx + 1, "level": level,
            "heading": heading, "line_start": start + 1, "line_end": own_end,
            "own_payload_sha256": sha_text(payload), "parent_only_body_sha256": sha_text(payload),
            "subtree_sha256": sha_text(subtree), "own_chars": len(payload), "_payload": payload,
        })
    by_id = {row["id"]: row for row in rows}
    for row in rows:
        children = []
        for candidate in rows[row["ordinal"]:]:
            if candidate["level"] <= row["level"]:
                break
            if candidate["level"] == row["level"] + 1:
                children.append(candidate["id"])
        child_evidence = [{"id": cid, "payload_sha256": by_id[cid]["own_payload_sha256"]} for cid in children]
        child_payload_union = "\n".join(by_id[cid]["_payload"] for cid in children)
        row["direct_children"] = children
        row["direct_child_union_evidence"] = child_evidence
        row["child_union_sha256"] = sha_text(child_payload_union)
        row["large_leaf_segments"] = []
        if not children and len(row["_payload"]) > 2200:
            for number, offset in enumerate(range(0, len(row["_payload"]), 1600), 1):
                chunk = row["_payload"][offset:offset + 1600]
                row["large_leaf_segments"].append({
                    "index": number, "start_char": offset, "end_char_exclusive": offset + len(chunk),
                    "chars": len(chunk), "payload_sha256": sha_text(chunk),
                })
    return rows


def structural_reason(unit: str, in_diagram: bool = False) -> str | None:
    plain = re.sub(r"[*_`>#]", "", unit.strip()).strip()
    if not plain:
        return "blank_or_fence"
    if re.match(r"^#{1,6}\s+", unit.strip()):
        return "heading_coordinate"
    if plain in {"---", "___"}:
        return "separator"
    if re.fullmatch(r"\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?", plain):
        return "table_separator"
    if re.fullmatch(r"[│┌┐└┘├┤┬┴┼─═╔╗╚╝╠╣╦╩╬+\-\s]+", plain):
        return "diagram_structural_border"
    if in_diagram:
        content = re.sub(r"[│┌┐└┘├┤┬┴┼─═╔╗╚╝╠╣╦╩╬]", " ", plain)
        content = re.sub(r"(?:--+|==+|[<>]?[-=]+>|[↑↓↔→←⇒⇄⇆]+)", " ", content)
        content = re.sub(r"\s+", " ", content).strip(" :-")
        lexical = re.findall(r"[A-Za-zĀ-ž][\wĀ-ž’'-]*", content)
        if re.search(r"[│┌┐└┘├┤┬┴┼─═╔╗╚╝╠╣╦╩╬]", plain) and len(lexical) < 4:
            return "diagram_structural_fragment"
        if re.fullmatch(r"(?:[<>]?[-=]+>|[↑↓↔→←⇒⇄⇆]|\s)+", plain):
            return "diagram_structural_connector"
        if len(lexical) < 3 or not re.search(r"[.!?;:]$", content):
            return "diagram_incomplete_fragment"
    if re.match(r"^[A-D]\.\s+", plain):
        return "mcq_option_coordinate"
    if re.fullmatch(r"(?:answer|key)\s*:?\s*[A-D].*", plain, re.I):
        return "answer_key_coordinate"
    if len(re.sub(r"[\W_]+", "", plain, flags=re.UNICODE)) < 3:
        return "symbol_fragment"
    return None


def incomplete_proposition_reason(unit: str, allow_label: bool = False) -> str | None:
    text = unit.strip()
    if not text:
        return "blank_or_fence"
    if re.match(r"^(?:[|│]\s*)?(?:→|←|⇒|↔|->|<-)\s*", text):
        return "leading_orphan_connector"
    if re.search(r"(?:→|←|⇒|↔|->|<-|[:;,]|\b(?:and|or|to|from|with|of|for|in|on|as|than|while|because))\s*$", text, re.I):
        return "dangling_connector_or_preposition"
    if text.count("`") % 2 or text.count("**") % 2 or text.count("__") % 2:
        return "unfinished_markdown_emphasis"
    if re.match(r"^\|\s*\w+", text) or re.match(r"^(?:and|or|but|because|while|whereas|which|that)\b", text, re.I):
        return "bare_continuation_clause"
    lexical = re.findall(r"[A-Za-zĀ-ž][\wĀ-ž’'-]*", re.sub(r"[*_`]", "", text))
    if not allow_label and len(lexical) < 3:
        return "incomplete_short_fragment"
    return None


def semantic_units(payload: str) -> tuple[list[str], list[dict]]:
    units, excluded, pending = [], [], []
    in_code = False

    def emit(unit: str, allow_label: bool = False) -> None:
        reason = structural_reason(unit, in_diagram=in_code)
        if not reason:
            reason = incomplete_proposition_reason(unit, allow_label=allow_label)
        (excluded if reason else units).append(
            {"exact_payload": unit, "reason": reason} if reason else unit
        )

    def flush() -> None:
        if pending:
            emit(" ".join(x.strip() for x in pending).strip())
            pending.clear()

    for line in payload.replace("\r\n", "\n").splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            excluded.append({"exact_payload": line, "reason": "fence_coordinate"})
            in_code = not in_code
            continue
        if in_code:
            flush()
            emit(stripped, allow_label=True)
            continue
        if not stripped:
            flush()
            continue
        if re.match(r"^#{1,6}\s+", stripped):
            flush()
            excluded.append({"exact_payload": line, "reason": "heading_coordinate"})
            continue
        if stripped.startswith("|"):
            flush()
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells):
                excluded.append({"exact_payload": line, "reason": "table_separator"})
            else:
                emit(" | ".join(cells), allow_label=True)
            continue
        if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", line):
            flush()
            pending.append(stripped)
            continue
        reason = structural_reason(stripped)
        if reason:
            flush()
            excluded.append({"exact_payload": stripped, "reason": reason})
        else:
            pending.append(stripped)
    flush()
    return units, [
        {"source_ordinal": i, "reason": item["reason"], "exact_payload_sha256": sha_text(item["exact_payload"]),
         "exact_payload": item["exact_payload"]}
        for i, item in enumerate(excluded, 1)
    ]


TOKEN_STOP = {
    "about", "after", "again", "against", "also", "among", "because", "being", "between",
    "could", "does", "from", "have", "into", "itself", "most", "only", "other", "rather",
    "same", "should", "statement", "than", "that", "their", "there", "these", "they", "this",
    "through", "under", "when", "where", "which", "while", "with", "would", "yoga",
}


def semantic_tokens(text: str) -> set[str]:
    folded = "".join(ch for ch in unicodedata.normalize("NFKD", norm(text)) if not unicodedata.combining(ch))
    return {
        token for token in re.findall(r"[a-z][\w’'-]{3,}", folded)
        if token not in TOKEN_STOP
    }


def anchor_group_present(text: str, group: list[str]) -> bool:
    folded = "".join(ch for ch in unicodedata.normalize("NFKD", norm(text)) if not unicodedata.combining(ch))
    return any(
        "".join(ch for ch in unicodedata.normalize("NFKD", norm(anchor)) if not unicodedata.combining(ch))
        in folded for anchor in group
    )


def conjunctive_anchor_match(text: str, groups: list[list[str]]) -> bool:
    return bool(groups) and all(anchor_group_present(text, group) for group in groups)


def panels_for_block(block: dict) -> list[dict]:
    payload = block["_payload"]
    rows = []
    for kind, pattern in (
        ("diagram", r"```[^\n]*\n.*?\n```"),
        ("table", r"(?m)(?:^\|.*\|\n){2,}"),
    ):
        for number, match in enumerate(re.finditer(pattern, payload, re.S if kind == "diagram" else 0), 1):
            panel = match.group(0).rstrip() + "\n"
            rows.append({
                "id": f"{block['id']}-{kind}-{number:03d}-{sha_text(panel)[:10]}",
                "source": block["source"], "source_block_id": block["id"], "kind": kind,
                "ordinal_within_block": number, "payload_sha256": sha_text(panel), "chars": len(panel),
                "exact_payload": panel,
            })
    return rows


def answer_statistics(sequence: str) -> dict:
    counts = Counter(sequence)
    expected = len(sequence) / 4
    chi_square = sum((counts[letter] - expected) ** 2 / expected for letter in "ABCD")
    return {
        "counts": {letter: counts[letter] for letter in "ABCD"},
        "max_run": max(len(match.group(0)) for match in re.finditer(r"(.)\1*", sequence)),
        "cycles": predictable_cycles(sequence),
        "chi_square": round(chi_square, 6),
        "min_share": min(counts[letter] for letter in "ABCD") / len(sequence),
        "max_share": max(counts[letter] for letter in "ABCD") / len(sequence),
    }


def deterministic_answer_sequence(question_ids: list[str], seed: str) -> tuple[str, int]:
    for salt in range(100000):
        sequence = "".join("ABCD"[int(sha_text(f"{seed}|{salt}|{qid}")[:16], 16) % 4] for qid in question_ids)
        stats = answer_statistics(sequence)
        if (stats["max_run"] <= 2 and not stats["cycles"]
                and stats["min_share"] >= ANSWER_IMBALANCE_MIN_SHARE
                and stats["max_share"] <= ANSWER_IMBALANCE_MAX_SHARE
                and stats["chi_square"] <= ANSWER_CHI_SQUARE_MAX
                and len(set(stats["counts"].values())) > 1):
            return sequence, salt
    raise RuntimeError("Unable to derive independent non-cyclic answer positions")


def fail(errors: list[dict], code: str, detail: str) -> None:
    errors.append({"code": code, "detail": detail})


def load_source_registry(root: Path, errors: list[dict]) -> tuple[dict[str, dict], dict[str, Path]]:
    registry_path = root / SOURCE_REGISTRY
    if not registry_path.is_file():
        fail(errors, "MISSING_REQUIRED_FILE", SOURCE_REGISTRY)
        return {}, {}
    registry_bytes = registry_path.read_bytes()
    if sha_bytes(registry_bytes) != SOURCE_REGISTRY_SHA256:
        fail(errors, "SOURCE_REGISTRY_TAMPER", SOURCE_REGISTRY)
    try:
        registry = json.loads(registry_bytes.decode("utf-8"))
    except Exception as exc:
        fail(errors, "SOURCE_REGISTRY_INVALID", str(exc))
        return {}, {}
    rows = registry.get("sources", [])
    by_key = {row.get("key"): row for row in rows if isinstance(row, dict)}
    if (
        registry.get("schema_version") != 1
        or registry.get("topic") != "06 Yoga"
        or registry.get("authority_mode") != "formal_present_canonical_boundary_controlled"
        or len(by_key) != len(rows)
        or tuple(row.get("key") for row in rows) != EXPECTED_SOURCE_KEYS
    ):
        fail(errors, "SOURCE_REGISTRY_SCHEMA", "source keys/order/topic/authority mode differ")
    for key in EXPECTED_SOURCE_KEYS:
        row = by_key.get(key, {})
        path_text = row.get("path", "")
        snapshot = row.get("snapshot", "")
        if (
            row.get("role") != EXPECTED_SOURCE_ROLES[key]
            or not row.get("scope")
            or not isinstance(path_text, str)
            or not Path(path_text).is_absolute()
            or not isinstance(snapshot, str)
            or not snapshot.startswith("source-snapshots/")
            or Path(snapshot).is_absolute()
            or not re.fullmatch(r"[0-9a-f]{64}", str(row.get("sha256", "")))
            or not isinstance(row.get("bytes"), int)
            or not isinstance(row.get("line_count"), int)
            or (key in SOURCE_ORDER and not isinstance(row.get("h2_h4_block_count"), int))
            or (key not in SOURCE_ORDER and row.get("h2_h4_block_count") is not None)
        ):
            fail(errors, "SOURCE_REGISTRY_SCHEMA", key)
    return by_key, {key: Path(row["path"]) for key, row in by_key.items() if row.get("path")}


def parse_pyq_snapshot(path: Path) -> list[dict]:
    rows, year = [], None
    pattern = re.compile(
        r"^- \*\*(Q\d+\([a-e]\)) · (\d+) marks(?:[^·]*) · "
        r"\[([^\]]+)\]\(([^)]+)\):\*\* (.+)$"
    )
    for line in path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines():
        heading = re.match(r"^## (\d{4})\b", line)
        if heading:
            year = int(heading.group(1))
            continue
        match = pattern.match(line)
        if not match or year is None:
            continue
        wording = re.split(r"\s+(?:📝|→)\s*", match.group(5), maxsplit=1)[0].strip()
        rows.append({
            "year": year,
            "question": match.group(1),
            "marks": int(match.group(2)),
            "owner": match.group(3),
            "owner_path": match.group(4),
            "exact_wording": wording,
        })
    return rows


def derive_pyq_truth(root: Path, registry: dict[str, dict], errors: list[dict]) -> tuple[list[dict], list[dict]]:
    rows = []
    for key in ("pyq_2018_2025", "pyq_2026"):
        record = registry.get(key, {})
        snapshot = root / record.get("snapshot", "")
        if snapshot.is_file():
            rows.extend(parse_pyq_snapshot(snapshot))
    primary = [row for row in rows if row["owner_path"].replace("\\", "/").endswith("/Yoga.md")]
    supporting = [
        row for row in rows
        if row["year"] == 2018 and row["question"] == "Q6(a)"
        and row["owner_path"].replace("\\", "/").endswith("/Nyaya-Vaisesika.md")
        and "Yoga philosophers" in row["exact_wording"]
    ]
    if len(primary) != 8 or len(supporting) != 1:
        fail(errors, "PYQ_SOURCE_PARSE_MISMATCH", f"primary={len(primary)} supporting={len(supporting)}")
    return primary, supporting


def primary_truth_dependency_guard(root: Path, authority: dict, errors: list[dict]) -> None:
    validator_tree = ast.parse((root / "validate_package.py").read_text(encoding="utf-8"))
    for node in ast.walk(validator_tree):
        if isinstance(node, ast.ImportFrom) and node.module == "build_package":
            imported = [alias.name for alias in node.names]
            fail(errors, "VALIDATOR_BUILDER_DEPENDENCY", ",".join(imported))
        if isinstance(node, ast.Import):
            imported = [alias.name for alias in node.names if alias.name == "build_package"]
            if imported:
                fail(errors, "VALIDATOR_BUILDER_DEPENDENCY", ",".join(imported))

    builder_text = (root / "build_package.py").read_text(encoding="utf-8")
    builder_tree = ast.parse(builder_text)
    forbidden_symbols = []
    protected_literals = {
        authority["source_identity"]["item_url"],
        authority["source_identity"]["object_url"],
        authority["source_identity"]["archive_identifier"],
        authority["source_identity"]["archive_ark"],
        authority["raw_object"]["bytes"],
        authority["raw_object"]["sha256"],
        authority["raw_object"]["line_count"],
        authority["coordinate"]["line_start"],
        authority["coordinate"]["line_end"],
        authority["payload"]["exact_text"],
        authority["payload"]["sha256"],
        authority["snapshot"]["sha256"],
        authority["authority"]["kind"],
        authority["authority"]["scope_restriction"],
        authority["doctrine"]["atomic_statement"],
    }
    for node in ast.walk(builder_tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name) and re.search(
                    r"(?:PRIMARY|II27).*(?:URL|ARK|IDENTIFIER|BYTES|SHA|LINE|COORD|PAYLOAD|SCOPE|STATEMENT|ANCHOR)",
                    target.id,
                    re.I,
                ):
                    forbidden_symbols.append(target.id)
        if isinstance(node, ast.Constant) and node.value in protected_literals:
            forbidden_symbols.append(f"literal:{repr(node.value)[:80]}")
        if isinstance(node, ast.Dict):
            for key, value in zip(node.keys, node.values):
                if (isinstance(key, ast.Constant) and key.value == "required_anchor_groups"
                        and isinstance(value, (ast.List, ast.Tuple))):
                    forbidden_symbols.append("literal:required_anchor_groups")
    if forbidden_symbols:
        fail(errors, "PRIMARY_SOURCE_TRUTH_DUPLICATED_IN_BUILDER", ",".join(sorted(set(forbidden_symbols))))


def verify_primary_authority(root: Path, errors: list[dict]) -> tuple[dict, list[str]]:
    manifest_path = root / AUTHORITY_MANIFEST
    if not manifest_path.is_file():
        return {}, []
    manifest_bytes = manifest_path.read_bytes()
    if sha_bytes(manifest_bytes) != AUTHORITY_MANIFEST_SHA256:
        fail(errors, "PRIMARY_SOURCE_AUTHORITY_MANIFEST_TAMPER", AUTHORITY_MANIFEST)
    try:
        authority = json.loads(manifest_bytes.decode("utf-8"))
    except Exception as exc:
        fail(errors, "PRIMARY_SOURCE_AUTHORITY_MANIFEST_INVALID", str(exc))
        return {}, []

    try:
        identity = authority["source_identity"]
        raw = authority["raw_object"]
        coordinate = authority["coordinate"]
        payload = authority["payload"]
        snapshot = authority["snapshot"]
        doctrine = authority["doctrine"]
        scope = authority["authority"]
        authority_files = [raw["path"], snapshot["path"]]
    except (KeyError, TypeError) as exc:
        fail(errors, "PRIMARY_SOURCE_AUTHORITY_MANIFEST_INVALID", str(exc))
        return authority, []

    raw_path = root / raw["path"]
    snapshot_path = root / snapshot["path"]
    if not raw_path.is_file():
        fail(errors, "MISSING_REQUIRED_FILE", raw["path"])
    else:
        raw_bytes = raw_path.read_bytes()
        if len(raw_bytes) != raw.get("bytes"):
            fail(errors, "PRIMARY_SOURCE_RAW_BYTES_TAMPER", f"{len(raw_bytes)} != {raw.get('bytes')}")
        if sha_bytes(raw_bytes) != raw.get("sha256"):
            fail(errors, "PRIMARY_SOURCE_RAW_SHA256_TAMPER", raw["path"])
        try:
            raw_text = raw_bytes.decode(raw.get("encoding", "utf-8")).replace("\r\n", "\n")
        except (LookupError, UnicodeDecodeError) as exc:
            fail(errors, "PRIMARY_SOURCE_RAW_DECODE_FAILURE", str(exc))
            raw_text = ""
        lines = raw_text.splitlines(keepends=True)
        if len(raw_text.splitlines()) != raw.get("line_count"):
            fail(errors, "PRIMARY_SOURCE_RAW_LINE_COUNT_TAMPER", str(len(raw_text.splitlines())))
        start, end = coordinate.get("line_start"), coordinate.get("line_end")
        extracted = "".join(lines[start - 1:end]) if (
            coordinate.get("line_numbering") == "one_based_inclusive"
            and isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= len(lines)
        ) else ""
        if extracted != payload.get("exact_text") or sha_text(extracted) != payload.get("sha256"):
            fail(errors, "PRIMARY_SOURCE_COORDINATE_OR_PAYLOAD_TAMPER", f"{start}-{end}")

    snapshot_text = ""
    if not snapshot_path.is_file():
        fail(errors, "MISSING_REQUIRED_FILE", snapshot["path"])
    else:
        snapshot_bytes = snapshot_path.read_bytes()
        if sha_bytes(snapshot_bytes) != snapshot.get("sha256"):
            fail(errors, "PRIMARY_SOURCE_SNAPSHOT_TAMPER", snapshot["path"])
        snapshot_text = snapshot_bytes.decode("utf-8").replace("\r\n", "\n")
        payload_match = re.search(r"## Exact extracted OCR payload.*?```text\n(.*?)```", snapshot_text, re.S)
        if not payload_match or payload_match.group(1) != payload.get("exact_text"):
            fail(errors, "PRIMARY_SOURCE_SNAPSHOT_PAYLOAD_TAMPER", snapshot["path"])
        if any(marker not in snapshot_text for marker in snapshot.get("required_scope_markers", [])):
            fail(errors, "PRIMARY_SOURCE_SNAPSHOT_SCOPE_TAMPER", snapshot["path"])

    metadata_ok = (
        authority.get("schema_version") == 1
        and authority.get("obligation_id") == "YG-OB-077"
        and identity.get("item_url", "").startswith("https://archive.org/details/")
        and identity.get("object_url", "").startswith("https://archive.org/download/")
        and identity.get("archive_identifier")
        and identity.get("archive_ark", "").startswith("ark:/")
        and identity.get("rights")
        and scope.get("general_authority") is False
        and scope.get("restrained_claim_only") is True
        and scope.get("forbids_enumerated_or_named_seven_stage_scheme") is True
        and doctrine.get("atomic_statement")
        and doctrine.get("required_anchor_groups")
        and conjunctive_anchor_match(doctrine["atomic_statement"], doctrine["required_anchor_groups"])
    )
    if not metadata_ok:
        fail(errors, "PRIMARY_SOURCE_AUTHORITY_SCOPE_TAMPER", AUTHORITY_MANIFEST)
    primary_truth_dependency_guard(root, authority, errors)
    return authority, authority_files


def anchor_payload(text: str, anchor: str) -> str | None:
    token = f'<a id="{anchor}"></a>'
    start = text.find(token)
    if start < 0:
        return None
    start = text.find("\n", start) + 1
    end = text.find("\n<a id=", start)
    if end < 0:
        end = len(text)
    return text[start:end].strip() + "\n"


def parse_mcqs(text: str) -> dict[int, dict]:
    result = {}
    for chunk in re.split(r"(?=^## MCQ \d+\.)", text, flags=re.M):
        head = re.match(r"## MCQ (\d+)\.\s*(.+)\n", chunk)
        if not head:
            continue
        options = {m.group(1): re.sub(r"\s+", " ", m.group(2).strip())
                   for m in re.finditer(r"^([A-D])\.\s+(.+?)(?=\n[A-D]\.\s+|\n\n\*\*Answer:|\n## |\Z)", chunk, re.M | re.S)}
        ans = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", chunk)
        stem_part = chunk[head.end():]
        first_opt = re.search(r"^[A-D]\.\s+", stem_part, re.M)
        stem = stem_part[:first_opt.start()].strip() if first_opt else stem_part.strip()
        explanations = {m.group(1): re.sub(r"\s+", " ", m.group(2).strip())
                        for m in re.finditer(r"^- \*\*([A-D]):\*\*\s*(.+)$", chunk, re.M)}
        result[int(head.group(1))] = {"title": head.group(2).strip(), "stem": stem, "options": options,
                                      "answer": ans.group(1) if ans else None, "explanations": explanations}
    return result


def predictable_cycles(sequence: str) -> list[tuple]:
    return [(period, start, sequence[start:start+period]) for period in range(2, 5)
            for start in range(len(sequence)-period*3+1)
            if len(set(sequence[start:start+period])) > 1 and sequence[start:start+period*3] == sequence[start:start+period]*3]


def sevenfold_stage_overclaim(text: str) -> bool:
    folded = norm(text)
    return bool(
        re.search(r"\b(?:enumerat(?:e|es|ed|ion)|list(?:s|ed)?|named?)\b.{0,80}\bseven\b.{0,40}\b(?:stage|grade|ground)s?\b", folded)
        or re.search(r"\bseven\b.{0,40}\b(?:named|enumerated)\b.{0,40}\b(?:stage|grade|ground)s?\b", folded)
        or re.search(r"\b(?:first|second|third|fourth|fifth|sixth|seventh)\b.{0,50}\b(?:stage|grade|ground)\b", folded)
    )


def reconstruct_option_cues(sdoc: dict[int, dict]) -> dict:
    rows, length_flags, specificity_flags, lexical_flags, format_flags = [], [], [], [], []
    markers = re.compile(r"\b(?:YS\s*\d|always|never|only|exactly|all|necessarily|immediately)\b", re.I)
    for i, q in sorted(sdoc.items()):
        counts = {letter: words(text) for letter, text in q["options"].items()}
        ordered = sorted(counts.values())
        median = (ordered[1] + ordered[2]) / 2
        keyed_count = counts[q["answer"]]
        keyed_ratio = max(keyed_count / max(1, median), median / max(1, keyed_count))
        pairwise = max(ordered) / max(1, min(ordered))
        details = {letter: len(markers.findall(text)) for letter, text in q["options"].items()}
        detail_delta = details[q["answer"]] - max(details[x] for x in "ABCD" if x != q["answer"])
        stem_terms = {x for x in re.findall(r"\b\w{7,}\b", q["stem"].casefold())
                      if x not in {"statement", "accurately", "captures", "doctrine"}}
        overlaps = {letter: len(stem_terms & set(re.findall(r"\b\w{7,}\b", text.casefold())))
                    for letter, text in q["options"].items()}
        lexical_delta = overlaps[q["answer"]] - max(overlaps[x] for x in "ABCD" if x != q["answer"])
        punctuation = {re.sub(r"\w", "", text.strip())[-1:] for text in q["options"].values()}
        qid = f"Q{i}"
        if keyed_ratio > KEYED_MEDIAN_RATIO_THRESHOLD: length_flags.append(qid)
        if detail_delta > KEYED_SPECIFICITY_DELTA_THRESHOLD: specificity_flags.append(qid)
        if lexical_delta > 2: lexical_flags.append(qid)
        if len(set(q["options"].values())) != 4 or len(punctuation) > 1: format_flags.append(qid)
        rows.append({"question_id": qid, "word_counts": counts,
                     "pairwise_max_min_ratio": round(pairwise, 3),
                     "keyed_to_median_ratio": round(keyed_ratio, 3),
                     "keyed_detail_marker_delta": detail_delta,
                     "keyed_lexical_overlap_delta": lexical_delta})
    return {
        "keyed_median_ratio_threshold": KEYED_MEDIAN_RATIO_THRESHOLD,
        "keyed_specificity_delta_threshold": KEYED_SPECIFICITY_DELTA_THRESHOLD,
        "maximum_pairwise_word_ratio": round(max(x["pairwise_max_min_ratio"] for x in rows), 3),
        "maximum_keyed_median_ratio": round(max(x["keyed_to_median_ratio"] for x in rows), 3),
        "length_flags": length_flags, "format_flags": format_flags,
        "specificity_flags": specificity_flags, "lexical_key_flags": lexical_flags,
        "questions": rows,
    }


def legacy_contract(value, path="") -> list[str]:
    hits = []
    if isinstance(value, dict):
        for key, child in value.items():
            here = f"{path}.{key}" if path else key
            if key in {"fixed_question_count", "fixed_total", "source_core", "source_remedial",
                       "answers_per_letter", "balanced_exactly", "equal_quota", "answer_quota"}:
                hits.append(here)
            hits.extend(legacy_contract(child, here))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            hits.extend(legacy_contract(child, f"{path}[{i}]") )
    elif isinstance(value, str) and re.search(
            r"\bfixed total\b|\bquestion[- ]first\b|\b24\s*\+\s*8\b|equal quotas?|"
            r"max\s*-\s*min\s*<=?\s*1|list\s*\(\s*['\"]ABCD['\"]\s*\)\s*\*",
            value, re.I):
        hits.append(path)
    return hits


def report(release: bool, checks: dict, errors: list[dict]) -> dict:
    state = "RELEASE_PASS" if release and not errors else "DEVELOPMENT_PASS" if not release and not errors else "FAIL"
    return {"schema_version": 5, "topic": "06 Yoga", "validated_at": datetime.now(IST).isoformat(timespec="seconds"),
            "mode": "release" if release else "development", "state": state,
            "release_ready": bool(release and not errors), "pdf_validation": "not_requested", "checks": checks, "errors": errors}


def validate(root: Path, release: bool) -> dict:
    errors, checks = [], {}
    for rel in REQUIRED_STATIC:
        if not (root / rel).is_file():
            fail(errors, "MISSING_REQUIRED_FILE", rel)
    if (root / "pdf").exists() or (root / "PDF-MANIFEST.json").exists() or list(root.rglob("*.pdf")):
        fail(errors, "PDF_ARTIFACT_FORBIDDEN", "PDFs, pdf/, and PDF-MANIFEST.json are prohibited")
    primary_authority, authority_files = verify_primary_authority(root, errors)
    source_registry, source_paths = load_source_registry(root, errors)
    source_snapshot_files = [row.get("snapshot", "") for row in source_registry.values()]
    required = REQUIRED_STATIC + authority_files + source_snapshot_files
    for rel in authority_files + source_snapshot_files:
        if not (root / rel).is_file() and not any(
            error["code"] == "MISSING_REQUIRED_FILE" and error["detail"] == rel for error in errors
        ):
            fail(errors, "MISSING_REQUIRED_FILE", rel)
    checks["required_files"] = len(required)
    checks["pdf_validation"] = "not_requested"
    if errors:
        return report(release, checks, errors)

    identity = primary_authority["source_identity"]
    raw_object = primary_authority["raw_object"]
    primary_coordinate = primary_authority["coordinate"]
    primary_payload = primary_authority["payload"]
    snapshot = primary_authority["snapshot"]
    doctrine = primary_authority["doctrine"]
    authority_scope = primary_authority["authority"]
    artifacts = BASE_ARTIFACTS + source_snapshot_files + [AUTHORITY_MANIFEST, raw_object["path"], snapshot["path"]]
    source_audit = load(root / "SOURCE-ARTIFACT-AUDIT.json")
    artifact_map = {x.get("file"): x for x in source_audit.get("artifacts", [])}
    if source_audit.get("status") != "CANONICAL_SOURCE_ARTIFACTS_CURRENT" or set(artifact_map) != set(artifacts):
        fail(errors, "SOURCE_ARTIFACT_AUDIT_SCHEMA", "Artifact inventory/status differs")
    for rel in artifacts:
        path, row = root / rel, artifact_map.get(rel, {})
        if not path.is_file() or row.get("sha256") != sha_bytes(path.read_bytes()) or row.get("bytes") != path.stat().st_size:
            fail(errors, "SOURCE_ARTIFACT_STALE", rel)
    primary_audit = source_audit.get("approved_primary_source", {})
    primary_snapshot = root / snapshot["path"]
    if (
        primary_audit.get("scope") != authority_scope["kind"]
        or primary_audit.get("obligation_id") != primary_authority["obligation_id"]
        or primary_audit.get("snapshot_path") != snapshot["path"]
        or not primary_snapshot.is_file()
        or primary_audit.get("snapshot_sha256") != snapshot["sha256"]
        or primary_audit.get("item_url") != identity["item_url"]
        or primary_audit.get("object_url") != identity["object_url"]
        or primary_audit.get("object_bytes") != raw_object["bytes"]
        or primary_audit.get("object_sha256") != raw_object["sha256"]
        or primary_audit.get("coordinate") != [primary_coordinate["line_start"], primary_coordinate["line_end"]]
        or primary_audit.get("payload_sha256") != primary_payload["sha256"]
    ):
        fail(errors, "YG-OB-077_PRIMARY_SOURCE_PROVENANCE_TAMPER", "source audit primary-source record differs")
    checks["source_artifacts"] = len(artifacts)

    review, audit = load(root / "FORMAL-COVERAGE-REVIEW.json"), load(root / "FORMAL-COVERAGE-AUDIT.json")
    if review.get("authority_mode") != "formal_present_canonical_boundary_controlled" or "task_authority_override" in review:
        fail(errors, "AUTHORITY_MODE_MISMATCH", str(review.get("authority_mode")))
    actual_by_source = {}
    for key in EXPECTED_SOURCE_KEYS:
        registry_row = source_registry[key]
        expected_path = source_paths[key]
        source = review.get("sources", {}).get(key, {})
        expected_review = {
            "path": registry_row["path"],
            "sha256": registry_row["sha256"],
            "bytes": registry_row["bytes"],
            "line_count": registry_row["line_count"],
            "h2_h4_block_count": registry_row["h2_h4_block_count"],
        }
        if source != expected_review:
            fail(errors, "SOURCE_IDENTITY_MISMATCH", key)
        if not expected_path.is_file():
            fail(errors, "FORMAL_SOURCE_MISSING" if key.startswith("formal_") else "SOURCE_FILE_MISSING", str(expected_path))
            continue
        source_bytes = expected_path.read_bytes()
        actual_hash = sha_bytes(source_bytes)
        if registry_row["sha256"] != actual_hash or registry_row["bytes"] != len(source_bytes):
            fail(errors, "FORMAL_SOURCE_HASH_DRIFT" if key.startswith("formal_") else "SOURCE_HASH_MISMATCH", key)
        text = expected_path.read_text(encoding="utf-8").replace("\r\n", "\n")
        if registry_row["line_count"] != len(text.splitlines()):
            fail(errors, "SOURCE_LINE_COUNT_MISMATCH", key)
        if key in SOURCE_ORDER:
            actual_by_source[key] = heading_blocks(expected_path, key)
            if registry_row["h2_h4_block_count"] != len(actual_by_source[key]):
                fail(errors, "SOURCE_BLOCK_COUNT_MISMATCH", key)
        snap = root / registry_row["snapshot"]
        if (not snap.is_file() or sha_bytes(snap.read_bytes()) != registry_row["sha256"]
                or len(snap.read_bytes()) != registry_row["bytes"]
                or snap.read_bytes() != source_bytes):
            fail(errors, "SOURCE_SNAPSHOT_STALE", key)
    checks["source_identities"] = len(source_registry)

    actual_blocks = [row for key in SOURCE_ORDER for row in actual_by_source.get(key, [])]
    expected_counts = {key: len(actual_by_source.get(key, [])) for key in SOURCE_ORDER}
    decisions = review.get("decisions", [])
    by_id = {x.get("id"): x for x in decisions}
    if len(by_id) != len(decisions):
        fail(errors, "BLOCK_ID_DUPLICATE", "duplicate stable IDs")
    if set(by_id) != {x["id"] for x in actual_blocks} or review.get("decision_count") != len(actual_blocks):
        fail(errors, "FORMAL_BLOCK_DELETION_OR_INFLATION", f"{len(decisions)} != {len(actual_blocks)}")
    if review.get("source_block_counts") != expected_counts or audit.get("source_block_counts") != expected_counts:
        fail(errors, "SOURCE_BLOCK_COUNT_MISMATCH", str(expected_counts))
    formal_count = expected_counts["formal_session"] + expected_counts["formal_workbook"]
    supplementary_count = sum(expected_counts[k] for k in SOURCE_ORDER if k.startswith("supplementary_"))
    if review.get("formal_block_count") != formal_count or review.get("canonical_block_count") != expected_counts["canonical"] or review.get("supplementary_block_count") != supplementary_count:
        fail(errors, "FORMAL_MAPPING_COUNT", "authority totals differ")
    if review.get("unclassified_count") != 0:
        fail(errors, "FORMAL_MAPPING_COUNT", "unclassified blocks remain")
    approved_primary = review.get("approved_primary_sources", [])
    if (
        len(approved_primary) != 1
        or approved_primary[0].get("scope") != authority_scope["kind"]
        or approved_primary[0].get("obligation_id") != primary_authority["obligation_id"]
        or approved_primary[0].get("snapshot_path") != snapshot["path"]
        or approved_primary[0].get("snapshot_sha256") != snapshot["sha256"]
        or approved_primary[0].get("item_url") != identity["item_url"]
        or approved_primary[0].get("object_url") != identity["object_url"]
        or approved_primary[0].get("object_bytes") != raw_object["bytes"]
        or approved_primary[0].get("object_sha256") != raw_object["sha256"]
        or approved_primary[0].get("ocr_coordinate") != [primary_coordinate["line_start"], primary_coordinate["line_end"]]
        or approved_primary[0].get("payload_sha256") != primary_payload["sha256"]
        or approved_primary[0].get("general_authority") is not authority_scope["general_authority"]
        or audit.get("approved_primary_source_obligations") != 1
        or audit.get("approved_primary_snapshot_sha256") != snapshot["sha256"]
    ):
        fail(errors, "YG-OB-077_PRIMARY_SOURCE_SCOPE_TAMPER", "formal provenance promoted or altered the narrow authority")

    mirror = (root / "FORMAL-SOURCE-MIRROR.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    learner_text = {name: (root / name).read_text(encoding="utf-8").replace("\r\n", "\n") for name in ("REVISION-GUIDE.md", "ANSWER-WRITING-TOOLKIT.md")}
    raw, unique, exclusions = 0, {}, []
    actual_panels = []
    mandatory_blocks = []
    for block in actual_blocks:
        row = by_id.get(block["id"])
        if not row:
            continue
        expected_class = ("mandatory_formal_session" if block["source"] == "formal_session" else
                          "mandatory_formal_workbook" if block["source"] == "formal_workbook" else
                          "mandatory_canonical_boundary" if block["source"] == "canonical" else "supplementary_depth")
        if row.get("classification") != expected_class or row.get("mandatory_obligation") != (expected_class != "supplementary_depth"):
            fail(errors, "BLOCK_CLASSIFICATION_TAMPER", block["id"])
        if expected_class != "supplementary_depth":
            mandatory_blocks.append(block)
        for field in ("own_payload_sha256", "parent_only_body_sha256", "subtree_sha256", "own_chars"):
            if row.get(field) != block.get(field):
                fail(errors, "BLOCK_IDENTITY_OR_HASH_MISMATCH", f"{block['id']}:{field}")
        if row.get("direct_children") != block["direct_children"] or row.get("direct_child_union_evidence") != block["direct_child_union_evidence"] or row.get("child_union_sha256") != block["child_union_sha256"]:
            fail(errors, "CHILD_UNION_MISMATCH", block["id"])
        if row.get("large_leaf_segments") != block["large_leaf_segments"]:
            fail(errors, "LARGE_LEAF_MISMATCH", block["id"])
        if block["large_leaf_segments"]:
            chunks = []
            for seg in block["large_leaf_segments"]:
                chunk = block["_payload"][seg["start_char"]:seg["end_char_exclusive"]]
                chunks.append(chunk)
                if sha_text(chunk) != seg["payload_sha256"] or len(chunk) != seg["chars"]:
                    fail(errors, "LARGE_LEAF_MISMATCH", f"{block['id']}:{seg['index']}")
            if "".join(chunks) != block["_payload"]:
                fail(errors, "LARGE_LEAF_MISMATCH", f"{block['id']}:union")
        destination = row.get("destination", {})
        payload = anchor_payload(mirror, destination.get("anchor", ""))
        if destination.get("file") != "FORMAL-SOURCE-MIRROR.md" or payload is None or sha_text(payload) != block["own_payload_sha256"] or destination.get("payload_sha256") != block["own_payload_sha256"]:
            fail(errors, "DESTINATION_PAYLOAD_HASH_MISMATCH", block["id"])
        learner = row.get("learner_destination", {})
        lpayload = anchor_payload(learner_text.get(learner.get("file"), ""), learner.get("anchor", ""))
        if lpayload is None or sha_text(lpayload) != block["own_payload_sha256"] or learner.get("payload_sha256") != block["own_payload_sha256"]:
            fail(errors, "LEARNER_PAYLOAD_MISMATCH", block["id"])
        units, excluded = semantic_units(block["_payload"])
        mappings = row.get("proposition_mappings", [])
        if any(
            structural_reason(x.get("exact_payload", ""))
            or (re.match(r"^\s*[│┌┐└┘├┤┬┴┼─═╔╗╚╝╠╣╦╩╬]", x.get("exact_payload", ""))
                and structural_reason(x.get("exact_payload", ""), in_diagram=True))
            for x in mappings
        ):
            fail(errors, "NON_PROPOSITION_FRAGMENT_INCLUDED", block["id"])
        if len(units) != len(mappings):
            fail(errors, "SEMANTIC_PROPOSITION_COUNT", block["id"])
        expected_excluded = [{"source_block_id": block["id"], **x} for x in excluded]
        if row.get("excluded_non_propositional_fragments") != expected_excluded:
            fail(errors, "EXCLUDED_FRAGMENT_ACCOUNTING_TAMPER", block["id"])
        exclusions.extend(expected_excluded)
        for i, (unit, mapping) in enumerate(zip(units, mappings), 1):
            if incomplete_proposition_reason(unit, allow_label=" | " in unit):
                fail(errors, "INCOMPLETE_RETAINED_PROPOSITION", f"{block['id']}:{i}:{unit[:80]}")
            pid = "prop-" + sha_text(norm(unit))[:20]
            if mapping != {"source_block_id": block["id"], "occurrence": i, "proposition_id": pid,
                           "exact_payload_sha256": sha_text(unit), "exact_payload": unit}:
                fail(errors, "SEMANTIC_PROPOSITION_REFERENCE_TAMPER", f"{block['id']}:{i}")
            raw += 1
            unique.setdefault(pid, unit)
        block_panels = panels_for_block(block)
        actual_panels.extend(block_panels)
        if row.get("panel_ids") != [x["id"] for x in block_panels]:
            fail(errors, "PANEL_PARITY_MISMATCH", block["id"])
    registry = {x.get("id"): x for x in review.get("proposition_registry", [])}
    if set(registry) != set(unique):
        fail(errors, "SEMANTIC_REGISTRY_MISMATCH", "registry IDs differ")
    for pid, unit in unique.items():
        expected = {"id": pid, "normalized_sha256": sha_text(norm(unit)), "exact_payload_sha256": sha_text(unit), "representative_exact_payload": unit}
        if registry.get(pid) != expected:
            fail(errors, "SEMANTIC_REGISTRY_TAMPER", pid)
    prop_counts = Counter(mapping["proposition_id"] for row in decisions for mapping in row.get("proposition_mappings", []))
    duplicate_occurrences = raw-len(unique)
    duplicate_groups = sum(count > 1 for count in prop_counts.values())
    diagram_structural_exclusions = sum(x["reason"].startswith("diagram_") for x in exclusions)
    for key, actual in (("raw_proposition_mapping_count", raw), ("unique_normalized_proposition_count", len(unique)),
                        ("duplicate_occurrences_deduplicated", duplicate_occurrences), ("duplicate_group_count", duplicate_groups),
                        ("excluded_fragment_count", len(exclusions)),
                        ("diagram_structural_exclusion_count", diagram_structural_exclusions)):
        if review.get(key) != actual:
            fail(errors, "SEMANTIC_TOTAL_MISMATCH", f"{key}:{actual}")
    panel_map = {x.get("id"): x for x in review.get("panels", [])}
    if len(panel_map) != len(actual_panels) or set(panel_map) != {x["id"] for x in actual_panels}:
        fail(errors, "PANEL_COUNT_MISMATCH", str(len(actual_panels)))
    for panel in actual_panels:
        if panel_map.get(panel["id"]) != panel:
            fail(errors, "PANEL_PARITY_MISMATCH", panel["id"])
    routes = review.get("routes", [])
    if len(routes) != 1 or routes[0].get("obligation_id") != "YG-SK-BOUNDARY-001" or routes[0].get("status") != "closed_after_serialized_reconciliation" or routes[0].get("release_blocking_for_this_package") is not False:
        fail(errors, "ROUTE_OBLIGATION_TAMPER", "Samkhya reciprocal obligation changed")
    if audit.get("review_sha256") != sha_bytes((root / "FORMAL-COVERAGE-REVIEW.json").read_bytes()):
        fail(errors, "DERIVED_AUDIT_STALE", "review hash changed")
    audit_expected = {"formal_blocks": formal_count, "canonical_blocks": expected_counts["canonical"], "supplementary_blocks": supplementary_count,
                      "decision_count": len(actual_blocks), "raw_proposition_mappings": raw, "unique_normalized_propositions": len(unique),
                      "duplicate_occurrences": duplicate_occurrences, "duplicate_groups": duplicate_groups,
                      "excluded_structural_coordinates": len(exclusions), "panels": len(actual_panels),
                      "diagram_structural_exclusions": diagram_structural_exclusions,
                      "large_leaves": sum(bool(x["large_leaf_segments"]) for x in actual_blocks),
                      "large_leaf_segments": sum(len(x["large_leaf_segments"]) for x in actual_blocks),
                      "mandatory_obligations": formal_count + expected_counts["canonical"], "supplementary_depth_rows": supplementary_count,
                      "outbound_reciprocal_obligations_due": 1}
    for key, value in audit_expected.items():
        if audit.get(key) != value:
            fail(errors, "DERIVED_AUDIT_COUNT", f"{key}:{audit.get(key)} != {value}")
    checks.update({"formal_session_blocks": expected_counts["formal_session"], "formal_workbook_blocks": expected_counts["formal_workbook"],
                   "canonical_blocks": expected_counts["canonical"], "supplementary_blocks": supplementary_count,
                   "raw_propositions": raw, "unique_propositions": len(unique), "duplicate_occurrences": duplicate_occurrences,
                   "duplicate_groups": duplicate_groups, "excluded_coordinates": len(exclusions),
                   "diagram_structural_exclusions": diagram_structural_exclusions, "panels": len(actual_panels),
                   "large_leaves": audit_expected["large_leaves"], "large_leaf_segments": audit_expected["large_leaf_segments"],
                   "route_obligations_due": 1})

    learner_files = {
        "formal_session": "REVISION-GUIDE.md", "formal_workbook": "ANSWER-WRITING-TOOLKIT.md",
        "canonical": "REVISION-GUIDE.md",
    }
    mandatory_blocks = (actual_by_source.get("formal_session", [])
                        + actual_by_source.get("formal_workbook", [])
                        + actual_by_source.get("canonical", []))
    obligations = load(root / "TESTABLE-OBLIGATIONS.json")
    source_inventory = load(root / "SOURCE-PROPOSITION-INVENTORY.json")
    expected_source_hashes = {
        key: sha_bytes(source_paths[key].read_bytes())
        for key in ("formal_session", "formal_workbook", "canonical")
        if source_paths[key].is_file()
    }
    inventory_blocks = {x.get("source_block_id"): x for x in source_inventory.get("blocks", [])}
    inventory_props = {
        (x.get("source_block_id"), x.get("proposition_occurrence")): x
        for x in source_inventory.get("propositions", [])
    }
    if (source_inventory.get("derivation_stage") != "frozen_before_question_bank"
            or source_inventory.get("source_hashes") != expected_source_hashes
            or source_inventory.get("mandatory_block_count") != len(mandatory_blocks)
            or set(inventory_blocks) != {x["id"] for x in mandatory_blocks}):
        fail(errors, "SOURCE_PROPOSITION_INVENTORY_TAMPER", "source hashes/block set/stage differs")
    for block in mandatory_blocks:
        row = inventory_blocks.get(block["id"], {})
        units, block_excluded = semantic_units(block["_payload"])
        if (row.get("exact_payload") != block["_payload"]
                or row.get("exact_payload_sha256") != block["own_payload_sha256"]
                or row.get("normalized_payload_sha256") != sha_text(norm(block["_payload"]))
                or row.get("proposition_ids") != ["prop-" + sha_text(norm(x))[:20] for x in units]
                or row.get("excluded_fragments") != [{"source_block_id": block["id"], **x} for x in block_excluded]):
            fail(errors, "SOURCE_PROPOSITION_INVENTORY_TAMPER", block["id"])
        for i, unit in enumerate(units, 1):
            prop = inventory_props.get((block["id"], i), {})
            if (prop.get("exact_payload") != unit
                    or prop.get("exact_payload_sha256") != sha_text(unit)
                    or prop.get("normalized_sha256") != sha_text(norm(unit))
                    or prop.get("proposition_id") != "prop-" + sha_text(norm(unit))[:20]):
                fail(errors, "SOURCE_PROPOSITION_INVENTORY_TAMPER", f"{block['id']}:{i}")
    expected_coordinates = {
        (block["id"], i)
        for block in mandatory_blocks
        for i, _ in enumerate(semantic_units(block["_payload"])[0], 1)
    }
    if set(inventory_props) != expected_coordinates:
        fail(errors, "SOURCE_PROPOSITION_CLASSIFICATION_INCOMPLETE",
             f"missing={len(expected_coordinates-set(inventory_props))}; extra={len(set(inventory_props)-expected_coordinates)}")
    allowed_classes = {
        "testable_atomic_obligation", "supporting_non_testable_context",
        "duplicate_normalized_obligation", "routed_boundary",
    }
    non_test_categories = {
        "example_only", "source_or_citation_only", "meta_answer_writing",
        "chronology_or_context_only", "dependent_qualification",
        "composite_split_into_atomic_ids", "repeated_implication",
    }
    first_coordinate_by_pid = {}
    classified_counts = Counter()
    represented_ids = set()
    for coordinate in sorted(inventory_props):
        row = inventory_props[coordinate]
        classification = row.get("classification")
        classified_counts[classification] += 1
        reverse = row.get("reverse_mapping", {})
        if classification not in allowed_classes or not row.get("rationale"):
            fail(errors, "OBLIGATION_CLASSIFICATION_INVALID", f"{coordinate}: class/rationale")
            continue
        pid = row.get("proposition_id")
        canonical = first_coordinate_by_pid.setdefault(pid, coordinate)
        if classification == "duplicate_normalized_obligation":
            expected_occurrence = f"{canonical[0]}:{canonical[1]}"
            if (coordinate == canonical
                    or reverse.get("canonical_proposition_id") != pid
                    or reverse.get("canonical_proposition_occurrence") != expected_occurrence):
                fail(errors, "DUPLICATE_CANONICAL_LINK_INVALID", f"{coordinate}")
        elif coordinate != canonical:
            fail(errors, "DUPLICATE_RECLASSIFIED", f"{coordinate}")
        elif classification == "testable_atomic_obligation":
            oid = reverse.get("represented_by_obligation_id")
            if (not oid or reverse.get("obligation_id") != oid
                    or reverse.get("relation") != "direct_atomic_authority"
                    or not reverse.get("doctrine_specific_reason")):
                fail(errors, "OBLIGATION_CLASSIFICATION_INVALID", f"{coordinate}: representation")
            represented_ids.add(oid)
        elif classification == "supporting_non_testable_context":
            category = reverse.get("non_testability_category")
            reason = reverse.get("independently_checkable_reason", "")
            if category not in non_test_categories or not reason or re.search(r"\b(?:unselected|not selected|generic fallback)\b", reason, re.I):
                fail(errors, "GENERIC_NON_TESTABILITY_REASON", f"{coordinate}:{category}")
            if category == "composite_split_into_atomic_ids" and not reverse.get("represented_by_obligation_ids"):
                fail(errors, "OBLIGATION_CLASSIFICATION_INVALID", f"{coordinate}: composite IDs")
        elif classification == "routed_boundary":
            if reverse.get("destination_obligation_id") != "YG-SK-BOUNDARY-001":
                fail(errors, "ROUTE_OBLIGATION_TAMPER", f"{coordinate}")
    expected_prop_counts = {key: classified_counts[key] for key in allowed_classes}
    if (source_inventory.get("complete_proposition_occurrence_count") != len(expected_coordinates)
            or source_inventory.get("proposition_classification_counts") != expected_prop_counts):
        fail(errors, "SOURCE_PROPOSITION_INVENTORY_TAMPER", "classification totals differ")

    obligation_rows = obligations.get("obligations", [])
    expected_obligation_ids = represented_ids | {"YG-OB-077"}
    actual_obligation_ids = {x.get("obligation_id") for x in obligations.get("obligations", [])}
    if expected_obligation_ids - actual_obligation_ids:
        fail(errors, "SOURCE_DERIVED_OBLIGATION_REMOVED", str(sorted(expected_obligation_ids - actual_obligation_ids)))
    expected_blocks = {x["id"] for x in mandatory_blocks}
    actual_blocks_classified = {x.get("source_block_id") for x in obligations.get("block_classifications", [])}
    actual_props = {(x.get("source_block_id"), x.get("proposition_occurrence"))
                    for x in obligations.get("proposition_classifications", [])}
    if expected_blocks != actual_blocks_classified:
        fail(errors, "OBLIGATION_BLOCK_CLASSIFICATION_OMISSION", str(len(expected_blocks - actual_blocks_classified)))
    if expected_coordinates != actual_props:
        fail(errors, "OBLIGATION_PROPOSITION_CLASSIFICATION_OMISSION", str(len(expected_coordinates - actual_props)))
    if any(x.get("classification") not in allowed_classes or not x.get("rationale") or not x.get("reverse_mapping")
           for x in obligations.get("block_classifications", []) + obligations.get("proposition_classifications", [])):
        fail(errors, "OBLIGATION_CLASSIFICATION_INVALID", "class, rationale, or reverse mapping invalid")
    if obligations.get("proposition_classifications") != source_inventory.get("propositions"):
        stripped_inventory = [
            {k: v for k, v in row.items() if k != "source_reverse_mapping"}
            for row in source_inventory.get("propositions", [])
        ]
        if obligations.get("proposition_classifications") != stripped_inventory:
            fail(errors, "OBLIGATION_INVENTORY_TAMPER", "classification copies diverge")
    if expected_obligation_ids != actual_obligation_ids:
        fail(errors, "OBLIGATION_ORPHAN_OR_OMISSION", str(expected_obligation_ids ^ actual_obligation_ids))
    obligation_by_id = {x.get("obligation_id"): x for x in obligation_rows}
    for obligation in obligation_rows:
        refs = obligation.get("authority_evidence", [])
        if len(refs) != 1:
            fail(errors, "OBLIGATION_AUTHORITY_REFERENCE_INVALID", obligation.get("obligation_id", "?"))
            continue
        ref = refs[0]
        if obligation.get("obligation_id") == "YG-OB-077":
            approved = obligations.get("approved_primary_source_obligations", [])
            approved_row = next((x for x in approved if x.get("obligation_id") == "YG-OB-077"), {})
            if (
                obligation.get("atomic_statement") != doctrine["atomic_statement"]
                or not conjunctive_anchor_match(obligation.get("atomic_statement", ""), doctrine["required_anchor_groups"])
            ):
                fail(errors, "YG-OB-077_AUTHORITY_NEAR_MATCH", "restrained II.27 claim differs")
            provenance_ok = (
                primary_snapshot.is_file()
                and ref.get("source_key") == "primary_ii27"
                and ref.get("source_path") == snapshot["path"]
                and ref.get("source_file_sha256") == raw_object["sha256"]
                and ref.get("source_file_bytes") == raw_object["bytes"]
                and ref.get("source_item_url") == identity["item_url"]
                and ref.get("source_object_url") == identity["object_url"]
                and ref.get("archive_identifier") == identity["archive_identifier"]
                and ref.get("archive_ark") == identity["archive_ark"]
                and ref.get("retrieval_date") == identity["retrieval_date"]
                and ref.get("snapshot_sha256") == snapshot["sha256"]
                and ref.get("source_block_id") == doctrine["source_block_id"]
                and ref.get("proposition_id") == doctrine["proposition_id"]
                and ref.get("line_start") == primary_coordinate["line_start"]
                and ref.get("line_end") == primary_coordinate["line_end"]
                and ref.get("source_line_count") == raw_object["line_count"]
                and ref.get("exact_payload") == primary_payload["exact_text"]
                and ref.get("exact_payload_sha256") == primary_payload["sha256"]
                and ref.get("exact_translation_excerpt") == primary_payload["exact_translation_excerpt"]
                and ref.get("normalized_sanskrit") == doctrine["normalized_sanskrit"]
                and ref.get("normalized_transliteration") == doctrine["normalized_transliteration"]
                and ref.get("required_anchor_groups") == doctrine["required_anchor_groups"]
                and ref.get("authority_kind") == authority_scope["kind"]
                and ref.get("scope_restriction") == authority_scope["scope_restriction"]
                and obligation.get("source_proposition_id") == ref.get("proposition_id")
                and obligation.get("coverage_derivation") == authority_scope["coverage_derivation"]
                and approved_row.get("authority_scope") == authority_scope["kind"]
                and approved_row.get("snapshot_path") == ref.get("source_path")
                and approved_row.get("snapshot_sha256") == ref.get("snapshot_sha256")
                and approved_row.get("source_object_url") == identity["object_url"]
                and approved_row.get("source_object_sha256") == raw_object["sha256"]
                and approved_row.get("source_object_bytes") == raw_object["bytes"]
                and approved_row.get("line_start") == primary_coordinate["line_start"]
                and approved_row.get("line_end") == primary_coordinate["line_end"]
                and approved_row.get("payload_sha256") == primary_payload["sha256"]
            )
            if not provenance_ok:
                fail(errors, "YG-OB-077_PRIMARY_SOURCE_PROVENANCE_TAMPER", "snapshot, URL, hash, coordinate, payload, or scope differs")
            if sevenfold_stage_overclaim(obligation.get("atomic_statement", "")):
                fail(errors, "YG-OB-077_SEVEN_STAGE_OVERCLAIM", "obligation invents an enumerated or named seven-stage scheme")
            continue
        source_row = next((x for x in obligations.get("proposition_classifications", [])
                           if x.get("proposition_id") == ref.get("proposition_id")
                           and x.get("source_block_id") == ref.get("source_block_id")
                           and x.get("classification") == "testable_atomic_obligation"
                           and x.get("reverse_mapping", {}).get("represented_by_obligation_id") == obligation.get("obligation_id")), None)
        if not source_row:
            reclassified = next((x for x in obligations.get("proposition_classifications", [])
                                 if x.get("proposition_id") == obligation.get("source_proposition_id")), None)
            if reclassified and reclassified.get("classification") != "testable_atomic_obligation":
                fail(errors, "EXAMINABLE_PROPOSITION_RECLASSIFIED", obligation.get("obligation_id", "?"))
            fail(errors, "OBLIGATION_REVERSE_COVERAGE_MISSING", obligation.get("obligation_id", "?"))
            continue
        source_key = ref.get("source_key")
        source_path = source_paths.get(source_key)
        lines = source_path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines() if source_path and source_path.is_file() else []
        start, end = ref.get("line_start"), ref.get("line_end")
        coordinate_text = "\n".join(lines[start-1:end]) if isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= len(lines) else ""
        authority_text = source_row["exact_payload"]
        groups = ref.get("required_anchor_groups", [])
        code = f"{obligation['obligation_id']}_AUTHORITY_NEAR_MATCH" if obligation["obligation_id"] in {"YG-OB-077", "YG-OB-078"} else "OBLIGATION_AUTHORITY_REFERENCE_IRRELEVANT"
        if (source_path is None or ref.get("source_path") != str(source_path)
                or ref.get("source_file_sha256") != sha_bytes(source_path.read_bytes())
                or not coordinate_text or norm(authority_text) not in norm(coordinate_text)
                or ref.get("exact_payload") != authority_text
                or ref.get("exact_payload_sha256") != sha_text(authority_text)
                or ref.get("normalized_sha256") != sha_text(norm(authority_text))
                or obligation.get("source_proposition_id") != ref.get("proposition_id")
                or obligation.get("atomic_statement") != authority_text
                or not conjunctive_anchor_match(authority_text, groups)):
            fail(errors, code, obligation["obligation_id"])

    if obligations.get("blocked_source_obligations") != []:
        fail(errors, "YG-OB-077_BLOCKER_STALE", "YG-OB-077 is now narrowly source-bound and must not remain blocked")
    checks.update({
        "mandatory_block_classifications": obligations.get("block_classification_counts"),
        "mandatory_proposition_classifications": obligations.get("proposition_classification_counts"),
        "atomic_obligations": len(expected_obligation_ids),
    })

    matrix, maudit = load(root / "TEST-MATRIX.json"), load(root / "MCQ-AUDIT.json")
    qdoc = parse_mcqs((root / "MCQ-QUESTIONS.md").read_text(encoding="utf-8"))
    sdoc = parse_mcqs((root / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8"))
    forbidden_contracts = legacy_contract(matrix) + legacy_contract(maudit)
    build_text = (root / "build_package.py").read_text(encoding="utf-8")
    if re.search(r"list\s*\(\s*['\"]ABCD['\"]\s*\)\s*\*|max\s*\([^)]*\)\s*-\s*min\s*\([^)]*\)\s*<=?\s*1", build_text):
        forbidden_contracts.append("build_package.py")
    if forbidden_contracts:
        fail(errors, "LEGACY_FIXED_TOTAL", str(forbidden_contracts))
    if matrix.get("historical_formal_mcqs_are_evidence_only") != 32:
        fail(errors, "FORMAL_MCQS_NOT_EVIDENCE_ONLY", "historical evidence marker changed")
    if (matrix.get("derivation_policy") != "cells_are_created_from_TESTABLE_OBLIGATIONS_before_questions_are_authored_or_mapped"
            or not str(matrix.get("question_total_policy", "")).startswith("one_probe_per_independently_derived")):
        fail(errors, "MCQ_QUESTION_FIRST_DERIVATION", "matrix does not establish obligation-first derivation")
    if matrix.get("obligation_inventory_file") != "TESTABLE-OBLIGATIONS.json" or matrix.get("obligation_inventory_sha256") != sha_bytes((root / "TESTABLE-OBLIGATIONS.json").read_bytes()):
        fail(errors, "OBLIGATION_INVENTORY_LINK_MISSING", "matrix does not hash-bind the independent inventory")
    if (matrix.get("source_classification_file") != "SOURCE-PROPOSITION-INVENTORY.json"
            or matrix.get("source_classification_sha256") != sha_bytes((root / "SOURCE-PROPOSITION-INVENTORY.json").read_bytes())):
        fail(errors, "SOURCE_CLASSIFICATION_FREEZE_MISMATCH", "question matrix is not bound to the pre-question classification artifact")
    if matrix.get("atomic_obligation_count") != len(expected_obligation_ids):
        fail(errors, "OBLIGATION_CELL_COVERAGE_MISSING", "atomic obligation count differs")
    expected_obligation_rows = obligation_rows
    expected_question_total = sum(x.get("minimum_probes", 1) for x in expected_obligation_rows)
    if (matrix.get("cell_count") != len(expected_obligation_rows)
            or matrix.get("derived_minimum_probes") != expected_question_total
            or matrix.get("question_total") != expected_question_total):
        fail(errors, "MCQ_MATRIX_TOTAL_MISMATCH", "coverage derivation differs")
    if len(qdoc) != expected_question_total or len(sdoc) != expected_question_total:
        fail(errors, "MCQ_DOCUMENT_COUNT", f"{len(qdoc)}/{len(sdoc)}")
    cell_map = {x.get("cell_id"): x for x in matrix.get("cells", [])}
    expected_cell_ids = {x["cell_id"] for x in expected_obligation_rows}
    if len(cell_map) != len(matrix.get("cells", [])) or set(cell_map) != expected_cell_ids:
        fail(errors, "MCQ_CELL_SET_MISMATCH", "cell IDs differ")
    if {x.get("obligation_id") for x in cell_map.values()} != expected_obligation_ids:
        fail(errors, "OBLIGATION_CELL_COVERAGE_MISSING", "orphan obligation or cell")
    mappings = matrix.get("question_mappings", [])
    pairs = {(x.get("question_id"), x.get("cell_id")) for x in mappings}
    if len(pairs) != len(mappings):
        fail(errors, "MCQ_REDUNDANT_MAPPING", "duplicate mapping")
    known_qids = {f"Q{i}" for i in range(1, expected_question_total + 1)}
    if any(x.get("question_id") not in known_qids or x.get("cell_id") not in cell_map for x in mappings):
        fail(errors, "MCQ_UNKNOWN_MAPPING", "unknown question/cell")
    obligation_map = {x["obligation_id"]: x for x in obligations.get("obligations", [])}
    normalized_discriminators = defaultdict(list)
    for cell in matrix.get("cells", []):
        normalized_discriminators[norm(cell.get("substantive_discriminator", ""))].append(cell.get("cell_id"))
    if any(len(ids) > 1 for ids in normalized_discriminators.values()):
        fail(errors, "MCQ_DUPLICATE_REDUNDANT_CELL", str([ids for ids in normalized_discriminators.values() if len(ids) > 1]))
    for i, obligation in enumerate(expected_obligation_rows, 1):
        qid, cid = f"Q{i}", obligation["cell_id"]
        count = sum(x.get("question_id") == qid for x in mappings)
        if count == 0:
            fail(errors, "MCQ_MISSING_MAPPING", qid)
        if count > 1:
            fail(errors, "MCQ_MAPPING_OVERLOADED", qid)
        if (qid, cid) not in pairs:
            fail(errors, "MCQ_FALSE_MAPPING", f"{qid}->{cid}")
        cell = cell_map.get(cid, {})
        if (cell.get("obligation_id") != obligation.get("obligation_id")
                or cell.get("authority_refs") != obligation.get("authority_evidence")
                or cell.get("substantive_discriminator") != obligation.get("atomic_statement")):
            fail(errors, "MCQ_AUTHORITY_REFERENCE_TAMPER", cid)
        if cell.get("mapped_question_ids") != [qid]:
            fail(errors, "MCQ_ORPHAN_CELL_OR_QUESTION", cid)
        mapping = next((x for x in mappings if x.get("question_id") == qid), {})
        if mapping.get("obligation_id") != obligation.get("obligation_id") or mapping.get("cell_id") != cid:
            fail(errors, "MCQ_FALSE_MAPPING", f"{qid}->{cid}")
        parsed = sdoc.get(i)
        if not parsed or len(parsed["options"]) != 4 or len(parsed["explanations"]) != 4:
            fail(errors, "MCQ_SOLUTION_STRUCTURE", qid)
            continue
        keyed_text = " ".join([parsed["title"], parsed["stem"], parsed["options"].get(parsed["answer"], ""), parsed["explanations"].get(parsed["answer"], "")])
        if obligation.get("obligation_id") == "YG-OB-077":
            full_question_text = " ".join(
                [parsed["title"], parsed["stem"], *parsed["options"].values(), *parsed["explanations"].values()]
            )
            if sevenfold_stage_overclaim(full_question_text):
                fail(errors, "YG-OB-077_SEVEN_STAGE_OVERCLAIM", qid)
        keyed = semantic_tokens(keyed_text)
        distractors = semantic_tokens(" ".join(v for k,v in parsed["options"].items() if k != parsed["answer"]))
        required_tokens = set().union(*(semantic_tokens(token) for token in cell.get("evidence_tokens", [])))
        required_groups = cell.get("required_anchor_groups", [])
        if not conjunctive_anchor_match(keyed_text, required_groups):
            code = f"{obligation.get('obligation_id')}_QUESTION_NEAR_MATCH" if obligation.get("obligation_id") in {"YG-OB-077", "YG-OB-078"} else "MCQ_FALSE_MAPPING"
            fail(errors, code, qid)
        elif not required_tokens <= keyed:
            fail(errors, "MCQ_DISTRACTOR_ONLY_MAPPING" if required_tokens & distractors else "MCQ_FALSE_MAPPING", qid)
        if len(cell.get("mapped_question_ids", [])) < cell.get("minimum_probes", 1):
            fail(errors, "MCQ_CELL_BELOW_MINIMUM", cid)
    for i in set(qdoc) | set(sdoc):
        q, s = qdoc.get(i), sdoc.get(i)
        if not q or not s or q["title"] != s["title"] or q["stem"] != s["stem"] or q["options"] != s["options"]:
            fail(errors, "MCQ_OPTION_SOLUTION_TAMPER", f"Q{i}")
    sequence = "".join(sdoc[i]["answer"] or "?" for i in sorted(sdoc))
    policy = maudit.get("position_policy", {})
    expected_sequence, expected_salt = deterministic_answer_sequence(
        [f"Q{i}" for i in sorted(sdoc)], policy.get("seed", ""))
    if (sequence != expected_sequence or sequence != maudit.get("answer_sequence")
            or policy.get("accepted_salt") != expected_salt):
        fail(errors, "MCQ_ANSWER_EXPLANATION_TAMPER", "answer sequence differs")
    stats = answer_statistics(sequence)
    counts = Counter(sequence)
    if (stats["counts"] != maudit.get("answer_counts")
            or stats["min_share"] < ANSWER_IMBALANCE_MIN_SHARE
            or stats["max_share"] > ANSWER_IMBALANCE_MAX_SHARE
            or stats["chi_square"] > ANSWER_CHI_SQUARE_MAX):
        fail(errors, "MCQ_ANSWER_IMBALANCE", f"{stats['counts']}; chi2={stats['chi_square']}")
    if (policy.get("method") != "independent_stable_hash_per_question"
            or policy.get("min_share") != ANSWER_IMBALANCE_MIN_SHARE
            or policy.get("max_share") != ANSWER_IMBALANCE_MAX_SHARE
            or policy.get("chi_square_max") != ANSWER_CHI_SQUARE_MAX
            or policy.get("selection_rule", "").find("equality is neither targeted") < 0):
        fail(errors, "MCQ_ANSWER_QUOTA_CONTRACT", "position policy is fixed, quota-based, or incomplete")
    max_run = stats["max_run"]
    cycles = stats["cycles"]
    if max_run > 2 or max_run != maudit.get("max_answer_run"):
        fail(errors, "MCQ_ANSWER_RUN", str(max_run))
    if cycles or maudit.get("short_cycles"):
        fail(errors, "MCQ_SHORT_CYCLE", str(cycles))
    stems = defaultdict(list)
    for i, q in sdoc.items():
        stems[norm(q["stem"])].append(i)
    if any(len(v)>1 for v in stems.values()):
        fail(errors, "MCQ_REDUNDANT_STEM", "duplicate normalized stems")
    cue_metrics = reconstruct_option_cues(sdoc)
    recorded_cues = maudit.get("option_cues", {})
    for field in ("keyed_median_ratio_threshold", "keyed_specificity_delta_threshold",
                  "maximum_pairwise_word_ratio", "maximum_keyed_median_ratio",
                  "length_flags", "format_flags", "specificity_flags", "lexical_key_flags", "questions"):
        if recorded_cues.get(field) != cue_metrics[field]:
            fail(errors, "MCQ_OPTION_CUE_AUDIT_STALE", field)
    for field, code in (
        ("length_flags", "MCQ_OPTION_LENGTH_CUE"),
        ("format_flags", "MCQ_OPTION_FORMAT_CUE"),
        ("specificity_flags", "MCQ_OPTION_SPECIFICITY_CUE"),
        ("lexical_key_flags", "MCQ_OPTION_LEXICAL_CUE"),
    ):
        if cue_metrics[field]:
            fail(errors, code, ",".join(cue_metrics[field]))
    checks.update({"matrix_cells":len(expected_obligation_rows),"mcq_total":expected_question_total,"answer_distribution":dict(counts),
                   "answer_sequence":sequence,"max_answer_run":max_run,"short_cycle_count":len(cycles),
                   "option_max_length_ratio":cue_metrics["maximum_pairwise_word_ratio"],
                   "option_max_keyed_median_ratio":cue_metrics["maximum_keyed_median_ratio"],
                   "option_cue_outliers":sum(len(cue_metrics[x]) for x in ("length_flags","format_flags","specificity_flags","lexical_key_flags"))})

    pyq = load(root / "PYQ-DEMAND-AUDIT.json")
    toolkit = (root / "ANSWER-WRITING-TOOLKIT.md").read_text(encoding="utf-8")
    expected_pyq_sources = {
        "2018_2025": {
            field: source_registry["pyq_2018_2025"][field]
            for field in ("path", "sha256", "bytes")
        },
        "2026": {
            field: source_registry["pyq_2026"][field]
            for field in ("path", "sha256", "bytes")
        },
    }
    if pyq.get("sources") != expected_pyq_sources:
        fail(errors, "PYQ_SOURCE_IDENTITY_MISMATCH", "PYQ audit sources differ from immutable registry")
    expected_primary_pyqs, expected_supporting_pyqs = derive_pyq_truth(root, source_registry, errors)
    if pyq.get("latest_repository_year") != 2026 or pyq.get("primary_count") != 8 or pyq.get("supporting_count") != 1 or pyq.get("original_count") != 6:
        fail(errors, "PYQ_COUNT_MISMATCH", "8 primary, 1 supporting, 6 originals required")
    for expected, row in zip(expected_primary_pyqs, pyq.get("primary", [])):
        year, qno, marks, wording = (
            expected["year"], expected["question"], expected["marks"], expected["exact_wording"]
        )
        if (row.get("year"), row.get("question"), row.get("marks"), row.get("exact_wording"), row.get("primary_owner")) != (year, qno, marks, wording, "Yoga"):
            fail(errors, "PYQ_EXACT_WORDING_OR_MARKS", f"{year} {qno}")
        section=re.search(rf"(?ms)^## {year} {re.escape(qno)} — {marks} marks.*?^### Model answer\s*\n+(.*?)\n+### Qualification / criticism",toolkit)
        actual_wc=words(section.group(1)) if section else 0; lo,hi={10:(150,200),15:(250,300),20:(340,400)}[marks]
        if not lo <= row.get("model_word_count",0) <= hi or actual_wc != row.get("model_word_count"):
            fail(errors,"PYQ_WORD_BAND",f"{year} {qno}:{actual_wc}")
        for field in ("demand_decoding","qualification_present","marks_rationale_present"):
            if not row.get(field): fail(errors,"PYQ_SOLUTION_COMPONENT_MISSING",f"{year} {qno}:{field}")
    supporting=pyq.get("supporting",[])
    if len(supporting)!=1 or len(expected_supporting_pyqs) != 1:
        fail(errors,"PYQ_SUPPORTING_COUNT","expected one")
    else:
        expected = expected_supporting_pyqs[0]
        year, qno, marks, wording = (
            expected["year"], expected["question"], expected["marks"], expected["exact_wording"]
        )
        row=supporting[0]
        if (row.get("year"),row.get("question"),row.get("marks"),row.get("exact_wording"),row.get("primary_owner"),row.get("supporting_owner")) != (year,qno,marks,wording,"Nyaya-Vaisesika","Yoga"):
            fail(errors,"PYQ_EXACT_WORDING_OR_MARKS","supporting 2018 Q6(a)")
        section=re.search(rf"(?ms)^### {year} {re.escape(qno)} — {marks} marks.*?^#### Model answer\s*\n+(.*?)\n+#### Qualification / criticism",toolkit)
        actual_wc=words(section.group(1)) if section else 0
        if not 340 <= row.get("model_word_count",0) <= 400 or actual_wc != row.get("model_word_count"):
            fail(errors,"PYQ_WORD_BAND",f"supporting:{actual_wc}")
        for field in ("demand_decoding","qualification_present","marks_rationale_present"):
            if not row.get(field): fail(errors,"PYQ_SOLUTION_COMPONENT_MISSING",f"supporting:{field}")
    originals=pyq.get("originals",[])
    if Counter(x.get("marks") for x in originals) != Counter({10:2,15:2,20:2}):
        fail(errors,"ORIGINAL_TIMED_SET","two per band required")
    for row in originals:
        section=re.search(rf"(?ms)^### {re.escape(row.get('id',''))} — {row.get('marks')} marks.*?\*\*Model answer:\*\*\s*\n+(.*?)\n+\*\*Qualification:\*\*",toolkit)
        actual_wc=words(section.group(1)) if section else 0; lo,hi=row.get("band",[0,0])
        if (lo,hi) != {10:(150,200),15:(250,300),20:(340,400)}.get(row.get("marks"),(0,0)) or not lo <= row.get("model_word_count",0) <= hi or actual_wc != row.get("model_word_count"):
            fail(errors,"ORIGINAL_WORD_BAND",f"{row.get('id')}:{actual_wc}")
    checks.update({"primary_pyqs":8,"supporting_pyqs":1,"original_timed_models":6,"word_bands":{"10":"150-200","15":"250-300","20":"340-400"}})

    if release:
        try:
            repo=Path(subprocess.check_output(["git","-C",str(root),"rev-parse","--show-toplevel"],text=True).strip())
            relroot=root.relative_to(repo); unstaged=[]; staged=0
            for rel in required:
                path=root/rel; relpath=(relroot/rel).as_posix()
                work_oid=subprocess.check_output(["git","-C",str(repo),"hash-object","--path",relpath,str(path)],text=True).strip()
                indexed=subprocess.run(["git","-C",str(repo),"rev-parse",f":{relpath}"],text=True,capture_output=True)
                if indexed.returncode != 0 or indexed.stdout.strip() != work_oid: unstaged.append(rel)
                else: staged += 1
            if unstaged: fail(errors,"RELEASE_NOT_STAGED",f"{len(unstaged)} package files absent/different in index")
            checks["git_normalized_staged_files"]=staged
        except Exception as exc:
            fail(errors,"RELEASE_NOT_STAGED",str(exc))
    return report(release,checks,errors)


def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("--root",type=Path,default=ROOT); parser.add_argument("--release",action="store_true"); parser.add_argument("--check-only",action="store_true")
    args=parser.parse_args(); data=validate(args.root.resolve(),args.release); print(json.dumps(data,ensure_ascii=False,indent=2))
    if not args.check_only: (args.root/"VALIDATION.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    return 0 if data["state"] in {"DEVELOPMENT_PASS","RELEASE_PASS"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
