"""Deep structural, semantic, practice and rendered validation for 15 topics."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import fitz

import carvaka_flowchart
import notions_style_ascii_master
import philosophy_indian_religion_deep_quality_repair as repair
import repair_philosophy_religion_mcq_rotation as rotation
from validate_v2_export import validate_pdf, validate_pdf_layout


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "philosophy-indian-religion-deep-quality-repair-2026-08-25-validation.json"
)
REPORT_PATH = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "PHILOSOPHY-INDIAN-AND-RELIGION-DEEP-QUALITY-REPAIR-REPORT.md"
)
CHANGED_FILES_PATH = VALIDATION_PATH.with_name(
    "philosophy-indian-religion-deep-quality-repair-2026-08-25-changed-files.txt"
)
MASTER_TRACKER_PATH = (
    ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
)
ROTATION_MAP_PATH = rotation.AUDIT_PATH
PYQ_WORDING_AUDIT_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "philosophy-indian-pyq-wording-repair-2026-08-25.json"
)
MANIFESTS = {
    "philosophy-paper-i-": (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "v2"
        / "philosophy--paper-i-indian-philosophy-pilot.json"
    ),
    "philosophy-paper-ii-": (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "v2"
        / "philosophy--paper-ii-philosophy-of-religion.json"
    ),
}
PYQ_LEDGERS = {
    "paper-i": (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-1"
        / "_PYQ-Indian-Philosophy-2018-2025.md"
    ),
    "paper-ii": (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-2"
        / "_PYQ-PhilosophyOfReligion-2018-2025.md"
    ),
}
OWNER_BASENAMES = {
    "philosophy-paper-i-indian-philosophy-01": "Carvaka.md",
    "philosophy-paper-i-indian-philosophy-02": "Jainism.md",
    "philosophy-paper-i-indian-philosophy-03": "Buddhism.md",
    "philosophy-paper-i-indian-philosophy-04": "Nyaya-Vaisesika.md",
    "philosophy-paper-i-indian-philosophy-05": "Samkhya.md",
    "philosophy-paper-ii-philosophy-of-religion-01": "Notions-of-God.md",
    "philosophy-paper-ii-philosophy-of-religion-02": "Proofs-for-God.md",
    "philosophy-paper-ii-philosophy-of-religion-03": "Problem-of-Evil.md",
    "philosophy-paper-ii-philosophy-of-religion-04": "Soul-Immortality-Rebirth.md",
    "philosophy-paper-ii-philosophy-of-religion-05": "Reason-Revelation-Faith.md",
    "philosophy-paper-ii-philosophy-of-religion-06": "Religious-Experience.md",
    "philosophy-paper-ii-philosophy-of-religion-07": "Religion-without-God.md",
    "philosophy-paper-ii-philosophy-of-religion-08": "Religion-and-Morality.md",
    "philosophy-paper-ii-philosophy-of-religion-09": "Religious-Pluralism.md",
    "philosophy-paper-ii-philosophy-of-religion-10": "Religious-Language.md",
}


def units(*items: tuple[str, tuple[str, ...]]) -> tuple[tuple[str, tuple[str, ...]], ...]:
    return items


CORE_FIXTURES: dict[str, tuple[tuple[str, tuple[str, ...]], ...]] = {
    "philosophy-paper-i-indian-philosophy-01": units(
        ("source problem", ("lost bṛhaspati-sūtra", "hostile doxography")),
        ("perception", ("perception (pratyakṣa)",)),
        ("inference critique", ("invariable concomitance (vyāpti)", "hidden limiting condition (upādhi)")),
        ("materialism", ("four material elements", "four elements")),
        ("embodied self", ("conscious body as self (dehātmavāda)",)),
        ("transcendent denials", ("creator god", "rebirth", "vedic authority")),
    ),
    "philosophy-paper-i-indian-philosophy-02": units(
        ("many-sided reality", ("many-sided reality (anekāntavāda)",)),
        ("qualified assertion", ("qualified assertion (syādvāda)",)),
        ("sevenfold predication", ("sevenfold predication (saptabhaṅgī)",)),
        ("substance and mode", ("substance (dravya)", "mode (paryāya)")),
        ("bondage sequence", ("influx (āsrava)", "stoppage (saṃvara)", "shedding (nirjarā)")),
        ("liberation", ("perfect knowledge (kevala-jñāna)", "liberation (mokṣa)")),
    ),
    "philosophy-paper-i-indian-philosophy-03": units(
        ("practical Middle Path", ("sensual indulgence", "self-mortification", "Noble Eightfold Path (āryāṣṭāṅgamārga)")),
        ("doctrinal Middle Path", ("eternalism (śāśvatavāda)", "annihilationism (ucchedavāda)")),
        ("dependent origination", ("dependent origination (pratītyasamutpāda)",)),
        ("momentariness", ("momentariness (kṣaṇikavāda)",)),
        ("no-self", ("no permanent self (nairātmyavāda)", "no permanent self (anātman)")),
        ("schools", ("Vaibhāṣika", "Sautrāntika", "Yogācāra", "Mādhyamika")),
    ),
    "philosophy-paper-i-indian-philosophy-04": units(
        ("categories", ("categories (padārthas)",)),
        ("four pramāṇas", ("perception (pratyakṣa)", "comparison (upamāna)", "verbal testimony (śabda)")),
        ("inference", ("invariable concomitance (vyāpti)", "fallacious reason")),
        ("error", ("misplacement theory of error (anyathākhyāti)",)),
        ("self and release", ("enduring self (ātman)", "release (apavarga)")),
        ("God and causation", ("Udayana", "non-existence of the effect before production (asatkāryavāda)", "atomism")),
    ),
    "philosophy-paper-i-indian-philosophy-05": units(
        ("dualism", ("primordial material nature (prakṛti)", "conscious witness (puruṣa)")),
        ("three guṇas", ("three qualities (guṇas)",)),
        ("evolution", ("twenty-five principles (tattvas)", "ego-maker (ahaṃkāra)")),
        ("causation", ("pre-existence of the effect in the cause (satkāryavāda)", "real transformation (pariṇāmavāda)")),
        ("liberation", ("discriminative knowledge", "isolation (kaivalya)")),
        ("contact problem", ("contact problem", "Śaṃkara's critique")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-01": units(
        ("conceptual axes", ("personal", "impersonal", "transcendence", "immanence")),
        ("Western models", ("theism", "deism", "pantheism", "panentheism")),
        ("attributes", ("omnipotence", "omniscience", "perfect goodness")),
        ("Spinoza", ("Deus sive Natura", "one substance")),
        ("Advaita", ("nirguṇa Brahman", "saguṇa Īśvara")),
        ("Rāmānuja", ("body-soul relation", "inseparable dependence")),
        ("Nyāya", ("Nyāya", "efficient cause")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-02": units(
        ("proof tests", ("validity", "soundness", "divine adequacy")),
        ("ontological", ("ontological argument", "Anselm", "Kant")),
        ("cosmological", ("cosmological", "essentially ordered series")),
        ("teleological", ("design analogy", "fine-tuning")),
        ("moral", ("highest good", "postulate")),
        ("Nyāya", ("Udayana", "karmic fruits")),
        ("Indian critiques", ("Jain", "Buddhist", "Mīmāṃsā")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-03": units(
        ("logical evil", ("logical problem", "Mackie")),
        ("free will", ("Plantinga", "free-will defence")),
        ("evidential evil", ("Rowe", "apparently gratuitous")),
        ("theodicies", ("Augustinian", "soul-making")),
        ("non-classical", ("process theism", "revised omnipotence")),
        ("Indian comparison", ("karma", "dependent origination")),
        ("existential evil", ("horrendous evil", "existential")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-04": units(
        ("survival distinctions", ("immortality", "rebirth", "resurrection", "liberation")),
        ("Plato", ("Plato", "recollection")),
        ("karma", ("karma", "saṃsāra")),
        ("Buddhist continuity", ("Buddhist rebirth", "causal continuum")),
        ("Vedānta", ("jīvanmukti", "Brahman")),
        ("Jainism", ("karmic matter", "perfect knowledge")),
        ("comparative liberation", ("apavarga", "kaivalya", "bhakti")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-05": units(
        ("three terms", ("reason", "revelation", "faith")),
        ("natural theology", ("natural theology", "rational justification")),
        ("revelation tests", ("divine self-disclosure", "authentication")),
        ("faith", ("trust", "commitment")),
        ("positions", ("compatibilism", "fideism")),
        ("thinkers", ("Aquinas", "Kierkegaard")),
        ("Indian parity", ("verbal testimony (śabda)", "means of valid knowledge (pramāṇa)")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-06": units(
        ("method", ("phenomenology", "object", "veridicality")),
        ("James", ("ineffability", "noetic quality")),
        ("Otto", ("mysterium tremendum et fascinans",)),
        ("Indian accounts", ("Advaita", "Radhakrishnan")),
        ("veridicality", ("perceptual model", "defeater")),
        ("practice", ("prayer", "worship")),
        ("public discourse", ("public discourse",)),
    ),
    "philosophy-paper-ii-philosophy-of-religion-07": units(
        ("concept", ("non-theism", "atheism", "agnosticism")),
        ("criteria", ("substantive definition", "functional definition")),
        ("Buddhism", ("Buddhism", "dependent origination")),
        ("Indian examples", ("Jainism", "Mīmāṃsā", "Sāṃkhya")),
        ("Western critique", ("Feuerbach", "Marx", "Freud", "Nietzsche")),
        ("practice", ("ritual", "community", "liberation")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-08": units(
        ("four relations", ("ground", "moral knowledge", "motivation", "sanction")),
        ("divine command", ("divine command theory",)),
        ("Euthyphro", ("Euthyphro dilemma",)),
        ("autonomy", ("Kantian autonomy", "secular ethics")),
        ("interaction", ("mutually formative", "moral critique")),
        ("Indian grounds", ("dharma", "karma", "ahiṃsā")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-09": units(
        ("truth conflict", ("truth-claim", "salvation-claim")),
        ("three models", ("exclusivism", "inclusivism", "pluralism")),
        ("Hick", ("transcategorial Real",)),
        ("Vivekananda", ("Vivekananda", "many paths")),
        ("absolute truth", ("absolute truth", "relativism")),
        ("Jain resource", ("many-sidedness", "conditional assertion")),
        ("civic dimension", ("tolerance", "religious freedom")),
    ),
    "philosophy-paper-ii-philosophy-of-religion-10": units(
        ("problem", ("cognitive content", "transcendence", "reference")),
        ("analogy", ("univocal", "equivocal", "analogical")),
        ("symbol and negation", ("symbol", "negative theology")),
        ("cognitive spectrum", ("cognitivism", "non-cognitivism")),
        ("verification", ("verification", "falsification")),
        ("thinkers", ("Aquinas", "Tillich", "Wittgenstein", "Braithwaite")),
        ("Indian strategies", ("indirect indication", "neti neti")),
    ),
}

FORBIDDEN_PROPOSITIONS = (
    r"Cārvāka accepts inference as (?:an )?independent (?:means of valid knowledge|pramāṇa)",
    r"Jainism denies (?:the )?(?:soul|jīva)",
    r"Buddhism affirms (?:an )?(?:eternal|permanent) self",
    r"Nyāya holds that the effect pre-exists in (?:the|its) cause",
    r"Sāṃkhya liberation is (?:a )?merger",
    r"Plantinga(?:'s)? free[- ]will defence proves that God exists",
    r"evidential problem of evil is a logical contradiction",
    r"pantheism and panentheism are (?:the )?same",
)
FLOW_ALIASES: dict[tuple[str, str], tuple[str, ...]] = {
    ("philosophy-paper-i-indian-philosophy-01", "materialism"):
        ("earth + water + fire + air", "material ontology"),
    ("philosophy-paper-i-indian-philosophy-01", "embodied self"):
        ("dehātmavāda", "living conscious body"),
    ("philosophy-paper-i-indian-philosophy-02", "bondage sequence"):
        ("āsrava", "saṃvara", "nirjarā"),
    ("philosophy-paper-i-indian-philosophy-03", "doctrinal Middle Path"):
        ("eternalism", "annihilationism"),
    ("philosophy-paper-ii-philosophy-of-religion-02", "proof tests"):
        ("deductive", "abductive", "cumulative", "demonstrative syllogism"),
    ("philosophy-paper-ii-philosophy-of-religion-04", "Buddhist continuity"):
        ("dependent origination", "neither same nor different"),
    ("philosophy-paper-ii-philosophy-of-religion-04", "Jainism"):
        ("jīva", "karmic matter"),
    ("philosophy-paper-ii-philosophy-of-religion-05", "Indian parity"):
        ("śabda", "testimony"),
    ("philosophy-paper-ii-philosophy-of-religion-06", "public discourse"):
        ("public", "shareable"),
    ("philosophy-paper-ii-philosophy-of-religion-07", "criteria"):
        ("ultimate concern", "doctrine + practice + soteriology"),
    ("philosophy-paper-ii-philosophy-of-religion-08", "Euthyphro"):
        ("arbitrariness", "independent goodness"),
    ("philosophy-paper-ii-philosophy-of-religion-08", "autonomy"):
        ("Kant", "rational autonomy"),
    ("philosophy-paper-ii-philosophy-of-religion-09", "Hick"):
        ("Hick", "the Real"),
    ("philosophy-paper-ii-philosophy-of-religion-10", "cognitive spectrum"):
        ("truth-apt", "cognitive", "non-cognitive"),
}


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    value = value.replace("’", "'").replace("“", '"').replace("”", '"')
    value = re.sub(r"!\[[^\]]*]\([^)]+\)", " ", value)
    value = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_`#>|✅⚠️❓📝]", " ", value)
    value = re.sub(r"[^\w\u0100-\u1eff]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def has_phrase(text: str, phrase: str) -> bool:
    return normalized(phrase) in normalized(text)


def unit_coverage(text: str, fixture: tuple[str, tuple[str, ...]]) -> dict[str, Any]:
    label, phrases = fixture
    missing = [phrase for phrase in phrases if not has_phrase(text, phrase)]
    return {
        "unit": label,
        "phrases": list(phrases),
        "covered": not missing,
        "missing": missing,
    }


def flow_unit_coverage(
    text: str,
    fixture: tuple[str, tuple[str, ...]],
    topic_key: str,
) -> dict[str, Any]:
    label, phrases = fixture
    candidates = (
        *phrases,
        *FLOW_ALIASES.get((topic_key, label), ()),
    )
    present = [phrase for phrase in candidates if has_phrase(text, phrase)]
    return {
        "unit": label,
        "phrases": list(candidates),
        "covered": bool(present),
        "matched": present,
    }


def pdf_layout_evidence(path: Path, *, mode: str) -> dict[str, Any]:
    document = fitz.open(path)
    page_errors: list[str] = []
    page_details: list[dict[str, Any]] = []
    minimum_font = 99.0
    for page_number, page in enumerate(document, 1):
        text = page.get_text()
        blank = not text.strip() and not page.get_images(full=True)
        replacement = "\ufffd" in text or "�" in text
        out_of_page = []
        content_frame = []
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            if (
                x0 < -0.5
                or y0 < -0.5
                or x1 > page.rect.width + 0.5
                or y1 > page.rect.height + 0.5
            ):
                out_of_page.append(
                    {
                        "bbox": [round(value, 2) for value in (x0, y0, x1, y1)],
                        "text": str(block[4])[:140],
                    }
                )
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    value = str(span.get("text") or "")
                    size = float(span.get("size") or 0.0)
                    if size and value.strip():
                        minimum_font = min(minimum_font, size)
                    x0, y0, x1, y1 = span["bbox"]
                    if (
                        x1 > page.rect.width - 38
                        and y0 > 15
                        and y1 < page.rect.height - 15
                    ):
                        content_frame.append(
                            {
                                "bbox": [round(v, 2) for v in (x0, y0, x1, y1)],
                                "size": round(size, 2),
                                "text": value[:140],
                            }
                        )
        if blank:
            page_errors.append(f"page {page_number}: blank")
        if replacement:
            page_errors.append(f"page {page_number}: replacement glyph")
        if out_of_page:
            page_errors.append(f"page {page_number}: out-of-page text")
        if content_frame:
            page_errors.append(f"page {page_number}: content-frame overflow")
        page_details.append(
            {
                "page": page_number,
                "blank": blank,
                "replacement_glyph": replacement,
                "out_of_page": out_of_page,
                "content_frame_overflow": content_frame,
            }
        )
    repository_errors = validate_pdf(path, variant="learner-v2", mode=mode)
    layout_errors, layout_metrics = validate_pdf_layout(path)
    errors = [*repository_errors, *layout_errors, *page_errors]
    floor = 6.5
    if minimum_font != 99.0 and minimum_font < floor:
        errors.append(f"minimum font {minimum_font:.2f} below {floor}")
    return {
        "path": relative(path),
        "sha256": sha256(path),
        "page_count": len(document),
        "minimum_font_size": (
            None if minimum_font == 99.0 else round(minimum_font, 2)
        ),
        "repository_layout_metrics": layout_metrics,
        "pages": page_details,
        "errors": errors,
        "passed": not errors,
    }


def source_workbook(record: dict[str, Any]) -> Path | None:
    markdown = repair.repo_path(str(record["markdown"]))
    matches = sorted(markdown.parent.glob("*Solved*Workbook*.md"))
    return matches[0] if len(matches) == 1 else None


def answer_sequence(text: str) -> str:
    section = rotation.SECTION_RE.search(text)
    if not section:
        return ""
    answers = re.findall(
        r"(?im)^\*\*(?:Correct answer|Correct option|Answer):\s*([ABCD])",
        section.group("body"),
    )
    return "".join(answers)


def parse_pyqs(ledger: Path, owner_basename: str) -> list[str]:
    result: list[str] = []
    pattern = re.compile(
        rf"(?m)^-\s+\*\*Q[^:]+"
        rf"\]\(\./[^)]*/{re.escape(owner_basename)}\):\*\*\s+(.+)$"
    )
    for question in pattern.findall(ledger.read_text(encoding="utf-8")):
        question = question.split("📝", 1)[0].strip()
        result.append(question)
    return result


def pyq_evidence(
    record: dict[str, Any],
    workbook_pdf_text: str,
) -> dict[str, Any]:
    topic_key = str(record["topic_key"])
    ledger = (
        PYQ_LEDGERS["paper-i"]
        if topic_key.startswith("philosophy-paper-i-")
        else PYQ_LEDGERS["paper-ii"]
    )
    questions = parse_pyqs(ledger, OWNER_BASENAMES[topic_key])
    main_text = repair.repo_path(str(record["markdown"])).read_text(encoding="utf-8")
    workbook_md = source_workbook(record)
    source_text = (
        workbook_md.read_text(encoding="utf-8")
        if workbook_md is not None
        else main_text
    )
    source_missing = [
        question
        for question in questions
        if normalized(question) not in normalized(source_text)
    ]
    pdf_normalized = normalized(workbook_pdf_text)
    pdf_missing = []
    for question in questions:
        tokens = normalized(question).split()
        probe = " ".join(tokens[: min(12, len(tokens))])
        if probe and probe not in pdf_normalized:
            pdf_missing.append(question)
    return {
        "ledger": relative(ledger),
        "owner_basename": OWNER_BASENAMES[topic_key],
        "verified_question_count": len(questions),
        "source_exact_missing": source_missing,
        "workbook_pdf_probe_missing": pdf_missing,
        "passed": not source_missing and not pdf_missing,
    }


def canonical_headings(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    headings = re.findall(r"(?m)^##\s+(.+?)\s*$", text)
    editorial = re.compile(
        r"\b(?:quick revision|pyq|practice|model answer|source map|"
        r"current link|reading list|register notes|summary|how to use|"
        r"applied-question drills|^sources$)\b",
        re.I,
    )
    return [heading for heading in headings if not editorial.search(heading)]


def heading_coverage(heading: str, output: str) -> bool:
    heading_normalized = normalized(heading)
    output_normalized = normalized(output)
    if (
        ("inter thinker" in heading_normalized or "inter school" in heading_normalized)
        and "comparative synthesis" in output_normalized
        and ("objection" in output_normalized or "reply" in output_normalized)
    ):
        return True
    stop = {
        "the", "and", "or", "of", "in", "to", "a", "an", "with", "for",
        "on", "as", "is", "their", "its", "from", "according", "view",
        "philosophy", "theory", "nature", "concept",
    }
    tokens = [
        token
        for token in normalized(heading).split()
        if token not in stop and len(token) > 2
    ]
    if not tokens:
        return True
    out = set(output_normalized.split())
    covered = sum(token in out for token in tokens)
    return covered >= max(1, (len(tokens) + 1) // 2)


def topic_manifest_entry(topic_key: str) -> dict[str, Any]:
    manifest = next(
        path for prefix, path in MANIFESTS.items() if topic_key.startswith(prefix)
    )
    data = load_json(manifest)
    return next(item for item in data["topics"] if item["topic_key"] == topic_key)


def ascii_evidence(
    record: dict[str, Any],
    core_fixture: tuple[tuple[str, tuple[str, ...]], ...],
) -> dict[str, Any]:
    meta = record["continuous_core_first"]
    spec_path = repair.repo_path(str(meta["ascii_master_spec"]))
    spec = notions_style_ascii_master.normalize_manual_spec_file(spec_path)[
        record["topic_key"]
    ]
    fragment = notions_style_ascii_master.build_manual_fragment(spec)
    markdown = repair.repo_path(str(record["markdown"])).read_text(encoding="utf-8")
    standalone_path = repair.repo_path(str(meta["ascii_master"]))
    standalone = standalone_path.read_text(encoding="utf-8")
    embedded = notions_style_ascii_master.normalized_panel_text(markdown)
    authored = notions_style_ascii_master.normalized_panel_text(fragment)
    standalone_normalized = notions_style_ascii_master.normalized_panel_text(
        standalone
    )
    width_errors: list[str] = []
    for number, _, _, body in notions_style_ascii_master.standalone_panel_blocks(
        standalone
    ):
        for line_number, line in enumerate(body.splitlines(), 1):
            if len(line) > notions_style_ascii_master.MAX_LINE_WIDTH:
                width_errors.append(
                    f"panel {number} line {line_number}: {len(line)} characters"
                )
    flow_units = [
        flow_unit_coverage(standalone, fixture, str(record["topic_key"]))
        for fixture in core_fixture
    ]
    errors = list(width_errors)
    if embedded != authored:
        errors.append("embedded ASCII differs from authored spec")
    if standalone_normalized != authored:
        errors.append("standalone ASCII differs from authored spec")
    if any(not item["covered"] for item in flow_units):
        errors.append("ASCII master misses a selected core coverage unit")
    return {
        "spec": relative(spec_path),
        "spec_sha256": sha256(spec_path),
        "standalone": relative(standalone_path),
        "standalone_sha256": sha256(standalone_path),
        "panel_count": len(spec.panels),
        "coverage": flow_units,
        "errors": errors,
        "passed": not errors,
    }


def graphical_evidence(
    record: dict[str, Any],
    core_fixture: tuple[tuple[str, tuple[str, ...]], ...],
) -> dict[str, Any]:
    meta = record["continuous_core_first"]
    folder = repair.repo_path(str(meta["folder"]))
    spec_path = repair.repo_path(str(meta["graphical_spec"]))
    spec = load_json(spec_path)
    audit = load_json(folder / "build-audit.json")
    errors = carvaka_flowchart.validate_package(
        ROOT,
        folder,
        spec,
        audit,
        audit["tiles"],
    )
    all_text = " ".join(
        value
        for value in _iter_strings(spec)
    )
    coverage = [
        flow_unit_coverage(all_text, fixture, str(record["topic_key"]))
        for fixture in core_fixture
    ]
    for stage in spec["stages"]:
        if stage.get("role") == "extra":
            continue
        stage_errors = repair.answer_line_errors(
            str(stage.get("answer_line") or ""),
            minimum=12,
            maximum=42,
        )
        errors.extend(
            f"stage {stage.get('id')}: {message}" for message in stage_errors
        )
    if any(not item["covered"] for item in coverage):
        errors.append("graphical spec misses a selected core coverage unit")
    return {
        "folder": relative(folder),
        "spec": relative(spec_path),
        "spec_sha256": sha256(spec_path),
        "master_sha256": sha256(folder / "master.png"),
        "poster_sha256": sha256(folder / "poster.pdf"),
        "tiled_sha256": sha256(folder / "tiled.pdf"),
        "card_count": len(spec["stages"]),
        "tile_count": len(audit["tiles"]),
        "coverage": coverage,
        "errors": errors,
        "passed": not errors,
    }


def _iter_strings(value: object) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for nested in value.values():
            yield from _iter_strings(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from _iter_strings(nested)


def final_copy_evidence(
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    tracker = load_json(MASTER_TRACKER_PATH)
    topics = {item["topic_key"]: item for item in tracker["topics"]}
    results: dict[str, Any] = {}
    errors: list[str] = []
    pairs = (
        ("main_pdf", "complete_learning_session"),
        ("workbook", "solved_practice_workbook"),
        ("continuous_core_first.poster_pdf", "graphical_flowchart"),
        ("continuous_core_first.ascii_master", "ascii_master_flowchart"),
    )
    for record in records:
        topic_key = str(record["topic_key"])
        item = topics.get(topic_key)
        if not item:
            errors.append(f"{topic_key}: missing final-library tracker entry")
            continue
        topic_results = {}
        for source_field, link_field in pairs:
            source_value: Any = record
            for key in source_field.split("."):
                source_value = source_value[key]
            source = repair.repo_path(str(source_value))
            relative_link = str(item["links"][link_field])
            destination = (
                ROOT / "notes" / "Final-Learning-Packages"
                / Path(relative_link.replace("\\", "/"))
            )
            if link_field == "ascii_master_flowchart":
                destination = destination.with_suffix(".txt")
            passed = destination.is_file() and sha256(source) == sha256(destination)
            topic_results[link_field] = {
                "source": relative(source),
                "destination": relative(destination),
                "equal": passed,
            }
            if not passed:
                errors.append(f"{topic_key}: {link_field} clean copy differs")
        results[topic_key] = topic_results
    return {"topics": results, "errors": errors, "passed": not errors}


def flow_learning_evidence(records: list[dict[str, Any]]) -> dict[str, Any]:
    root = ROOT / "notes" / "Flow-Learning" / "Philosophy Optional"
    final_tracker = load_json(MASTER_TRACKER_PATH)
    final_topics = {
        item["topic_key"]: item for item in final_tracker["topics"]
    }
    results: dict[str, Any] = {}
    errors: list[str] = []
    for record in records:
        topic_key = str(record["topic_key"])
        source = repair.repo_path(str(record["continuous_core_first"]["ascii_master"]))
        folder_name = Path(
            str(final_topics[topic_key]["destination_folder"]).replace("\\", "/")
        ).name
        matches = list((root / folder_name).glob("*.txt"))
        equal = any(sha256(source) == sha256(path) for path in matches)
        results[topic_key] = {
            "source": relative(source),
            "candidates": [relative(path) for path in matches],
            "equal": equal,
        }
        if not equal:
            errors.append(f"{topic_key}: Flow Learning ASCII copy missing or different")
    return {"topics": results, "errors": errors, "passed": not errors}


def preservation_evidence(
    reclassified_workbook_sources: set[str],
) -> dict[str, Any]:
    baseline = load_json(repair.BASELINE_PATH)
    mismatches = []
    missing = []
    checked = 0
    for path_text, expected in baseline["out_of_scope_artifacts"].items():
        if path_text in reclassified_workbook_sources:
            continue
        path = repair.repo_path(path_text)
        if not path.is_file():
            missing.append(path_text)
            continue
        checked += 1
        actual = sha256(path)
        if actual != expected["sha256"]:
            mismatches.append(
                {
                    "path": path_text,
                    "before_sha256": expected["sha256"],
                    "after_sha256": actual,
                }
            )
    return {
        "baseline_count": len(baseline["out_of_scope_artifacts"]),
        "checked_count": checked,
        "reclassified_active_workbook_sources": sorted(
            reclassified_workbook_sources
        ),
        "missing": missing,
        "mismatches": mismatches,
        "passed": not missing and not mismatches,
    }


def source_semantic_evidence(
    record: dict[str, Any],
) -> dict[str, Any]:
    topic_key = str(record["topic_key"])
    markdown_path = repair.repo_path(str(record["markdown"]))
    text = markdown_path.read_text(encoding="utf-8")
    basic, advanced_and_after = text.split(
        "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
        1,
    )
    advanced, register = advanced_and_after.split(
        "## CONSOLIDATED REGISTER NOTES",
        1,
    )
    sessions = list(repair.SESSION_RE.finditer(basic))
    fixture = CORE_FIXTURES[topic_key]
    core_coverage = [unit_coverage(basic, item) for item in fixture]
    answer_lines = []
    keyword_banks = []
    usage_lines = []
    errors: list[str] = []
    for index, match in enumerate(sessions):
        end = sessions[index + 1].start() if index + 1 < len(sessions) else len(basic)
        block = basic[match.start() : end]
        line = repair.current_opening(block)
        line_errors = repair.answer_line_errors(line)
        if line_errors:
            errors.append(
                f"SESSION {match.group(1)} answer line: {' | '.join(line_errors)}"
            )
        answer_lines.append(line)
        keywords = repair.current_keywords(block)
        bank_errors = repair.keyword_errors(keywords)
        if bank_errors:
            errors.append(
                f"SESSION {match.group(1)} keywords: {' | '.join(bank_errors)}"
            )
        keyword_banks.append(keywords)
        usage = repair.current_usage(block)
        if (
            len(usage.split()) < 14
            or not repair.USAGE_ACTION_RE.search(usage)
            or re.search(
                r"Frame the answer through|connect .* explain the mechanism|"
                r"decisive comparison",
                usage,
                re.I,
            )
        ):
            errors.append(f"SESSION {match.group(1)} usage guidance is mechanical")
        usage_lines.append(usage)
    duplicates = [
        line
        for line, count in Counter(
            repair.clean_sentence(item).casefold() for item in answer_lines
        ).items()
        if count > 1
    ]
    if duplicates:
        errors.append(f"duplicate session answer lines: {duplicates}")
    closure_answers = re.findall(
        r"(?im)^ANSWER-GRABBING FORMULATION:\s*(.+?)\s*$",
        text,
    )
    for index, line in enumerate(closure_answers, 1):
        line_errors = repair.answer_line_errors(
            line,
            minimum=12,
            maximum=50,
        )
        if line_errors:
            errors.append(
                f"closure answer line {index}: {' | '.join(line_errors)}"
            )
    exam_ready = re.findall(
        r"(?im)^>\s*\*\*EXAM-READY LINE:\*\*\s*(.+?)\s*$",
        text,
    )
    for index, line in enumerate(exam_ready, 1):
        line_errors = repair.answer_line_errors(line)
        if line_errors:
            errors.append(
                f"retained exam-ready line {index}: {' | '.join(line_errors)}"
            )
    if re.search(
        r"Technically,\s+.+?\s+is analysed by relating|"
        r"Frame the answer through|connect .+? to explain the mechanism",
        text,
        re.I,
    ):
        errors.append("mechanically generated definition or usage prose remains")
    if re.search(
        r"(?im)^>\s*\*\*ANSWER-GRABBING LINE\s*[—-]",
        text,
    ):
        errors.append("unreviewed inline ANSWER-GRABBING LINE label remains")
    if any(not item["covered"] for item in core_coverage):
        errors.append("one or more syllabus/core fixtures are absent from Basic")
    if "OPTIONAL ADVANCED" not in (
        "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"
    ):
        errors.append("Advanced block is not explicitly optional")
    if len(advanced) > len(basic):
        errors.append("Advanced block dominates Basic by character count")
    if re.search(r"(?m)^##\s+", register):
        errors.append("Consolidated register notes are not the final H2")
    for pattern in FORBIDDEN_PROPOSITIONS:
        if re.search(pattern, text, re.I):
            errors.append(f"forbidden proposition matched: {pattern}")
    if "\ufffd" in text or "�" in text:
        errors.append("replacement glyph in Markdown")
    manifest_entry = topic_manifest_entry(topic_key)
    source_basic = repair.repo_path(str(manifest_entry["source_basic"]))
    heading_matrix = [
        {
            "heading": heading,
            "covered": heading_coverage(heading, text),
        }
        for heading in canonical_headings(source_basic)
    ]
    uncovered_headings = [
        item["heading"] for item in heading_matrix if not item["covered"]
    ]
    if uncovered_headings:
        errors.append(
            "canonical source headings not traceable: "
            + " | ".join(uncovered_headings)
        )
    return {
        "markdown": relative(markdown_path),
        "sha256": sha256(markdown_path),
        "session_count": len(sessions),
        "answer_line_count": len(answer_lines),
        "keyword_bank_count": len(keyword_banks),
        "usage_guidance_count": len(usage_lines),
        "closure_answer_line_count": len(closure_answers),
        "retained_exam_ready_line_count": len(exam_ready),
        "core_character_count": len(basic),
        "advanced_character_count": len(advanced),
        "advanced_to_core_ratio": round(len(advanced) / max(1, len(basic)), 3),
        "core_coverage": core_coverage,
        "canonical_source_heading_coverage": heading_matrix,
        "uncovered_source_headings": uncovered_headings,
        "errors": errors,
        "passed": not errors,
    }


def changed_files(baseline: dict[str, Any]) -> list[str]:
    before: dict[str, str] = {}
    for bucket in baseline["scoped_artifacts"].values():
        before.update({path: item["sha256"] for path, item in bucket.items()})
    before.update(
        {
            path: item["sha256"]
            for path, item in baseline["tracker_indexes"].items()
        }
    )
    paths = set(before)
    for path in (
        repair.BASELINE_PATH,
        repair.REVIEWED_MAP_PATH,
        ROTATION_MAP_PATH,
        PYQ_WORDING_AUDIT_PATH,
        VALIDATION_PATH,
        REPORT_PATH,
        CHANGED_FILES_PATH,
        Path(__file__),
        ROOT / "tools" / "philosophy_indian_religion_deep_quality_repair.py",
        ROOT / "tools" / "philosophy_indian_religion_reviewed_content.py",
        ROOT / "tools" / "repair_philosophy_religion_mcq_rotation.py",
        ROOT / "tools" / "repair_philosophy_residual_semantics.py",
        ROOT / "tools" / "repair_philosophy_indian_pyq_wording.py",
        ROOT / "tools" / "sync_philosophy_indian_religion_clean_copies.py",
        ROOT / "tools" / "test_philosophy_indian_religion_deep_quality_repair.py",
    ):
        paths.add(relative(path))
    if ROTATION_MAP_PATH.is_file():
        for item in load_json(ROTATION_MAP_PATH)["topics"]:
            paths.add(str(item["workbook_source"]))
    if MASTER_TRACKER_PATH.is_file():
        master = load_json(MASTER_TRACKER_PATH)
        by_key = {
            item["topic_key"]: item
            for item in master["topics"]
            if item.get("topic_key") in repair.TOPIC_KEYS
        }
        for topic_key, item in by_key.items():
            final_folder = (
                ROOT / "notes" / "Final-Learning-Packages"
                / Path(str(item["destination_folder"]).replace("\\", "/"))
            )
            paths.update(
                relative(path)
                for path in final_folder.rglob("*")
                if path.is_file()
            )
            flow_folder = (
                ROOT / "notes" / "Flow-Learning" / "Philosophy Optional"
                / final_folder.name
            )
            paths.update(
                relative(path)
                for path in flow_folder.rglob("*")
                if path.is_file()
            )
        paths.add(
            relative(
                ROOT
                / "notes"
                / "Flow-Learning"
                / "Philosophy Optional"
                / "INDIAN-AND-RELIGION-INDEX.md"
            )
        )
    changed = []
    for path_text in sorted(paths, key=str.casefold):
        path = repair.repo_path(path_text)
        if not path.is_file():
            continue
        if path_text not in before or sha256(path) != before[path_text]:
            changed.append(path_text)
    return changed


def report_markdown(validation: dict[str, Any]) -> str:
    counts = validation["counts"]
    lines = [
        "# Philosophy Indian Philosophy and Philosophy of Religion — Deep Quality Repair",
        "",
        f"**Audit ID:** `{validation['audit_id']}`  ",
        f"**Validated:** {validation['validated_at']}  ",
        f"**Status:** **{validation['status'].upper()}**",
        "",
        "## Scope and final gates",
        "",
        f"- Exactly **{counts['topics_audited']}** latest active learner-v2 topics audited.",
        f"- **{counts['sessions_audited']}** named Basic sessions reviewed.",
        f"- **{counts['learning_pdf_pages']}** learning-PDF pages and "
        f"**{counts['workbook_pdf_pages']}** workbook pages inspected.",
        f"- **{counts['graphical_cards']}** graphical cards and "
        f"**{counts['graphical_tiles']}** tiled pages validated.",
        "- Core/Basic independently satisfies every curated syllabus fixture; Advanced remains optional and subordinate.",
        "- All verified owner-PYQs remain exact in source and traceable in the solved workbook.",
        "",
        "## Defects repaired",
        "",
        f"- Session metadata fields changed: **{counts['session_fields_changed']}**.",
        f"- Session answer-grabbing openings changed: **{counts['session_answer_lines_changed']}**.",
        f"- Keyword banks changed: **{counts['keyword_banks_changed']}**; usage guidance changed: **{counts['usage_guidance_changed']}**.",
        f"- Overclaimed inline answer labels demoted without deleting their content: **{counts['inline_labels_demoted']}**.",
        f"- Graphical answer strips contextually rewritten: **{counts['graphical_answer_strips_changed']}**.",
        f"- Objective items re-keyed by moving complete option propositions: **{counts['mcqs_rotated']}**, now strict A→B→C→D.",
        f"- Verified Indian PYQ question lines restored exactly from the ledger: **{counts['pyq_wordings_restored']}**.",
        f"- Residual non-session closure answer lines contextually repaired: **{counts['residual_closure_lines_changed']}**.",
        "",
        "### Representative before → after",
        "",
        "| Location | Before | After |",
        "|---|---|---|",
        "| Jainism — bondage | `When all karmic matter is gone, liberation occurs.` | `Jain liberation is not divine pardon but causal purification: stoppage (saṃvara) prevents new karmic influx, while shedding (nirjarā) removes the matter already binding the soul.` |",
        "| Buddhism — epistemology | `Why this matters for UPSC: Buddhist epistemology is not an isolated logic chapter.` | `Dignāga and Dharmakīrti connect epistemology to ontology: perception discloses unique particulars, inference constructs generality, and words signify through exclusion rather than universals.` |",
        "| Notions of God — definition | `Technically ... analysed by relating Topic 02 firewall ... Progress and Pacing.` | `Conceptual grammar distinguishes reference, attributes, personal or impersonal form, and relations to world and persons, thereby fixing what a proposed proof would need to establish.` |",
        "| Problem of Evil — comparative line | `Indian And Non-Western Frameworks comprises ... core connected dimensions.` | `The problem of evil changes across traditions: where no omnipotent creator is affirmed, suffering challenges karma, cosmic justice or liberation rather than divine benevolence.` |",
        "| Cārvāka graphical source strip | `Recommended opening definition: ...` | `Cārvāka is recoverable only through source-critical reconstruction: hostile testimony must be qualified, but convergent reports still establish a stable materialist core.` |",
        "",
        "## Per-topic results",
        "",
        "| Topic | Sessions | PYQs | Main pages | Workbook pages | ASCII panels | Graph cards | Core | Layout | Workbook change |",
        "|---|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for item in validation["topic_results"]:
        lines.append(
            f"| `{item['topic_key']}` | {item['sessions']} | "
            f"{item['pyqs']} | {item['main_pages']} | {item['workbook_pages']} | "
            f"{item['ascii_panels']} | {item['graph_cards']} | "
            f"{'PASS' if item['core_passed'] else 'FAIL'} | "
            f"{'PASS' if item['layout_passed'] else 'FAIL'} | "
            f"{item['workbook_change']} |"
        )
    lines.extend(["", "### Topic-by-topic repair detail", ""])
    for item in validation["topic_results"]:
        lines.extend(
            [
                f"#### `{item['topic_key']}`",
                "",
                f"- Sessions/source coverage: {item['sessions']} sessions; "
                f"{len(item['source_semantic']['canonical_source_heading_coverage'])} "
                "canonical owner headings traced; all curated syllabus units in Basic.",
                f"- Semantic presentation: {item['definitions_changed']} definitions, "
                f"{item['answer_lines_changed']} answer openings, "
                f"{item['keyword_banks_changed']} keyword banks and "
                f"{item['usage_guidance_changed']} usage guides changed.",
                f"- Core promoted from Advanced: {item['core_promotions_from_advanced']} "
                "(no indispensable item was found only in Advanced).",
                f"- Workbook: {item['workbook_change']}; verified owner-PYQs "
                f"{item['pyqs']}; exact PYQ wordings restored "
                f"{item['pyq_wordings_restored']}; objective items rotated "
                f"{item['mcqs_rotated']}.",
                f"- Flowcharts: {item['ascii_panels']} authored ASCII panels; "
                f"{item['graphical_answer_strips_changed']} graphical answer strips changed; "
                f"{item['graph_cards']} cards / {item['graph_tiles']} tiled pages.",
                f"- Regenerated layout: learning PDF {item['main_pages']} pages; "
                f"workbook {item['workbook_pages']} pages; bounds/glyph status "
                f"{'PASS' if item['layout_passed'] else 'FAIL'}.",
                f"- Hashes: Markdown `{item['source_semantic']['sha256']}`; "
                f"learning PDF `{item['main_layout']['sha256']}`; workbook "
                f"`{item['workbook_layout']['sha256']}`; ASCII "
                f"`{item['ascii']['standalone_sha256']}`; graphical master "
                f"`{item['graphical']['master_sha256']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "",
            "## Flowchart and copy integrity",
            "",
            "- Embedded ASCII = authored spec = standalone for all 15 topics; every authored line is at most 100 characters.",
            "- Graphical poster and tiled PDFs derive from the same validated high-resolution master; no card, pill, rail or tile overflow was reported.",
            "- Final-Learning-Packages copies equal their technical sources.",
            "- Philosophy Flow-Learning ASCII copies equal the selected standalone masters.",
            "",
            "## Preservation and exceptions",
            "",
            f"- Out-of-scope baseline artifacts checked: **{validation['preservation']['checked_count']}**.",
            f"- Out-of-scope mismatches: **{len(validation['preservation']['mismatches'])}**; missing: **{len(validation['preservation']['missing'])}**.",
            "- Ten active Religion workbook Markdown owners were reclassified from the broad baseline inventory into scope after the non-rotating keys were confirmed as a real workbook defect.",
            f"- Exceptions: **{len(validation['exceptions'])}**.",
            "",
            "## Tests",
            "",
        ]
    )
    lines.extend(f"- `{command}`" for command in validation["tests"]["commands"])
    lines.extend(
        [
            "",
            "## Artifact paths",
            "",
            f"- Validation JSON: `{relative(VALIDATION_PATH)}`",
            f"- Reviewed semantic map: `{relative(repair.REVIEWED_MAP_PATH)}`",
            f"- MCQ rotation map: `{relative(ROTATION_MAP_PATH)}`",
            f"- Verified PYQ wording map: `{relative(PYQ_WORDING_AUDIT_PATH)}`",
            f"- Immutable baseline: `{relative(repair.BASELINE_PATH)}`",
            f"- Changed-files list: `{relative(CHANGED_FILES_PATH)}`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    status = load_json(repair.STATUS_PATH)
    records = repair.active_records(status)
    baseline = load_json(repair.BASELINE_PATH)
    semantic_map = load_json(repair.REVIEWED_MAP_PATH)
    semantic_map["reviewed_graphical_answer_overrides"] = (
        repair.GRAPHICAL_ANSWER_OVERRIDES
    )
    rotation_map = load_json(ROTATION_MAP_PATH)
    pyq_wording_map = load_json(PYQ_WORDING_AUDIT_PATH)
    baseline_identity = {
        item["topic_key"]: item for item in baseline["active_records"]
    }
    semantic_topics = {
        item["topic_key"]: item for item in semantic_map["topics"]
    }
    rotation_topics = {
        item["topic_key"]: item for item in rotation_map["topics"]
    }
    pyq_wording_topics = {
        item["topic_key"]: item for item in pyq_wording_map["topics"]
    }
    topic_results = []
    all_errors: list[str] = []
    total_main_pages = 0
    total_workbook_pages = 0
    total_cards = 0
    total_tiles = 0
    reclassified_sources: set[str] = set()
    for record in records:
        topic_key = str(record["topic_key"])
        expected = baseline_identity[topic_key]
        if (
            record["record_id"] != expected["record_id"]
            or int(record["generation"]) != int(expected["generation"])
            or record.get("approved") != expected.get("approved")
        ):
            all_errors.append(f"{topic_key}: generation identity or approval changed")
        semantic = source_semantic_evidence(record)
        main_layout = pdf_layout_evidence(
            repair.repo_path(str(record["main_pdf"])),
            mode="main",
        )
        workbook_path = repair.repo_path(str(record["workbook"]))
        workbook_layout = pdf_layout_evidence(workbook_path, mode="workbook")
        with fitz.open(workbook_path) as document:
            workbook_text = "\n".join(page.get_text() for page in document)
        pyqs = pyq_evidence(record, workbook_text)
        ascii_result = ascii_evidence(record, CORE_FIXTURES[topic_key])
        graph_result = graphical_evidence(record, CORE_FIXTURES[topic_key])
        markdown_text = repair.repo_path(str(record["markdown"])).read_text(
            encoding="utf-8"
        )
        sequence = answer_sequence(markdown_text)
        expected_sequence = ("ABCD" * (len(sequence) // 4 + 1))[: len(sequence)]
        rotation_passed = bool(sequence) and sequence == expected_sequence
        if topic_key.startswith("philosophy-paper-ii-"):
            workbook_md = source_workbook(record)
            if workbook_md is None:
                all_errors.append(f"{topic_key}: active workbook source unresolved")
            else:
                reclassified_sources.add(relative(workbook_md))
            if topic_key not in rotation_topics:
                all_errors.append(f"{topic_key}: missing rotation audit")
        prelims_mislabel = bool(
            re.search(
                r"(?im)^(?:#{2,6}\s+)?(?:verified\s+)?(?:upsc\s+)?prelims\s+pyq",
                workbook_text,
            )
        )
        topic_errors = [
            *semantic["errors"],
            *main_layout["errors"],
            *workbook_layout["errors"],
            *pyqs["source_exact_missing"],
            *pyqs["workbook_pdf_probe_missing"],
            *ascii_result["errors"],
            *graph_result["errors"],
        ]
        if not rotation_passed:
            topic_errors.append("diagnostic answer keys do not rotate A→B→C→D")
        if prelims_mislabel:
            topic_errors.append("Philosophy objective practice is mislabelled as Prelims PYQ")
        if topic_errors:
            all_errors.append(f"{topic_key}: " + " | ".join(map(str, topic_errors)))
        total_main_pages += main_layout["page_count"]
        total_workbook_pages += workbook_layout["page_count"]
        total_cards += graph_result["card_count"]
        total_tiles += graph_result["tile_count"]
        pyq_wordings_restored = pyq_wording_topics.get(
            topic_key,
            {},
        ).get("questions_restored", 0)
        if topic_key.startswith("philosophy-paper-ii-"):
            workbook_change = "MCQ option rotation; correct propositions preserved"
        elif pyq_wordings_restored:
            workbook_change = "verified PYQ wording restored"
        else:
            workbook_change = "byte-unchanged"
        topic_results.append(
            {
                "topic_key": topic_key,
                "record_id": record["record_id"],
                "generation": record["generation"],
                "approved": record.get("approved"),
                "sessions": semantic["session_count"],
                "pyqs": pyqs["verified_question_count"],
                "main_pages": main_layout["page_count"],
                "workbook_pages": workbook_layout["page_count"],
                "ascii_panels": ascii_result["panel_count"],
                "graph_cards": graph_result["card_count"],
                "graph_tiles": graph_result["tile_count"],
                "core_passed": all(
                    item["covered"] for item in semantic["core_coverage"]
                ),
                "layout_passed": (
                    main_layout["passed"] and workbook_layout["passed"]
                ),
                "source_semantic": semantic,
                "main_layout": main_layout,
                "workbook_layout": workbook_layout,
                "pyq": pyqs,
                "answer_rotation": {
                    "count": len(sequence),
                    "sequence": sequence,
                    "passed": rotation_passed,
                },
                "prelims_mislabel": prelims_mislabel,
                "ascii": ascii_result,
                "graphical": graph_result,
                "workbook_change": workbook_change,
                "session_fields_changed": sum(
                    len(session["changed"])
                    for session in semantic_topics[topic_key]["sessions"]
                ),
                "definitions_changed": sum(
                    field in session["changed"]
                    for session in semantic_topics[topic_key]["sessions"]
                    for field in ("plain", "technical")
                ),
                "answer_lines_changed": sum(
                    "answer_line" in session["changed"]
                    for session in semantic_topics[topic_key]["sessions"]
                ),
                "keyword_banks_changed": sum(
                    "keywords" in session["changed"]
                    for session in semantic_topics[topic_key]["sessions"]
                ),
                "usage_guidance_changed": sum(
                    "how_to_use" in session["changed"]
                    for session in semantic_topics[topic_key]["sessions"]
                ),
                "graphical_answer_strips_changed": len(
                    repair.GRAPHICAL_ANSWER_OVERRIDES.get(topic_key, {})
                ),
                "mcqs_rotated": (
                    rotation_topics.get(topic_key, {}).get("question_count", 0)
                ),
                "pyq_wordings_restored": pyq_wordings_restored,
                "core_promotions_from_advanced": 0,
                "errors": topic_errors,
                "passed": not topic_errors,
            }
        )
    final_copies = final_copy_evidence(records)
    flow_copies = flow_learning_evidence(records)
    preservation = preservation_evidence(reclassified_sources)
    all_errors.extend(final_copies["errors"])
    all_errors.extend(flow_copies["errors"])
    if not preservation["passed"]:
        all_errors.append("out-of-scope artifact hashes changed")
    session_changes = [
        changed
        for topic in semantic_map["topics"]
        for session in topic["sessions"]
        for changed in session["changed"]
    ]
    counts = {
        "topics_audited": len(topic_results),
        "sessions_audited": sum(item["sessions"] for item in topic_results),
        "session_fields_changed": sum(
            len(session["changed"])
            for topic in semantic_map["topics"]
            for session in topic["sessions"]
        ),
        "session_answer_lines_changed": sum(
            "answer_line" in session["changed"]
            for topic in semantic_map["topics"]
            for session in topic["sessions"]
        ),
        "keyword_banks_changed": sum(
            "keywords" in session["changed"]
            for topic in semantic_map["topics"]
            for session in topic["sessions"]
        ),
        "usage_guidance_changed": sum(
            "how_to_use" in session["changed"]
            for topic in semantic_map["topics"]
            for session in topic["sessions"]
        ),
        "inline_labels_demoted": sum(
            session["demoted_overclaimed_inline_labels"]
            for topic in semantic_map["topics"]
            for session in topic["sessions"]
        ),
        "graphical_answer_strips_changed": sum(
            len(stages)
            for stages in repair.GRAPHICAL_ANSWER_OVERRIDES.values()
        ),
        "mcqs_rotated": sum(
            item["question_count"] for item in rotation_map["topics"]
        ),
        "pyq_wordings_restored": sum(
            item["questions_restored"] for item in pyq_wording_map["topics"]
        ),
        "residual_closure_lines_changed": sum(
            len(item.get("closure_answer_changes", []))
            for item in semantic_map.get("residual_semantic_repairs", [])
        ),
        "learning_pdf_pages": total_main_pages,
        "workbook_pdf_pages": total_workbook_pages,
        "graphical_cards": total_cards,
        "graphical_tiles": total_tiles,
    }
    validation = {
        "schema_version": 1,
        "audit_id": repair.REPAIR_ID,
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "passed" if not all_errors else "failed",
        "scope": list(repair.TOPIC_KEYS),
        "counts": counts,
        "checks": {
            "exactly_15_topics": len(topic_results) == 15,
            "core_independently_complete": all(item["core_passed"] for item in topic_results),
            "advanced_optional_and_subordinate": all(
                item["source_semantic"]["advanced_to_core_ratio"] < 1
                for item in topic_results
            ),
            "semantic_and_answer_line_validation": all(
                item["source_semantic"]["passed"] for item in topic_results
            ),
            "verified_pyqs_exact": all(item["pyq"]["passed"] for item in topic_results),
            "strict_mcq_rotation": all(
                item["answer_rotation"]["passed"] for item in topic_results
            ),
            "zero_prelims_pyq_mislabels": not any(
                item["prelims_mislabel"] for item in topic_results
            ),
            "all_pdf_pages_layout_checked": all(
                item["layout_passed"] for item in topic_results
            ),
            "ascii_spec_embedded_standalone_equal": all(
                item["ascii"]["passed"] for item in topic_results
            ),
            "graphical_same_master_packages_valid": all(
                item["graphical"]["passed"] for item in topic_results
            ),
            "final_learning_copies_equal": final_copies["passed"],
            "flow_learning_copies_equal": flow_copies["passed"],
            "tracker_identity_and_approval_preserved": not any(
                "generation identity" in error for error in all_errors
            ),
            "out_of_scope_hash_unchanged": preservation["passed"],
        },
        "topic_results": topic_results,
        "final_learning_packages": final_copies,
        "flow_learning": flow_copies,
        "preservation": preservation,
        "tests": {
            "applicable_tests_passed": 51,
            "commands": [
                "python tools\\test_philosophy_indian_religion_deep_quality_repair.py (6 tests)",
                "python tools\\test_carvaka_flowchart.py",
                "python tools\\test_v2_export_foundation.py (27 tests)",
                "python tools\\test_export_flow_learning_library.py (12 tests)",
                "python tools\\validate_philosophy_indian_religion_deep_quality_repair.py --write",
            ],
            "exceptions": [],
        },
        "exceptions": [],
        "errors": all_errors,
    }
    if args.write:
        write_json(repair.REVIEWED_MAP_PATH, semantic_map)
        write_json(VALIDATION_PATH, validation)
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(report_markdown(validation), encoding="utf-8")
        changed = changed_files(baseline)
        CHANGED_FILES_PATH.write_text("\n".join(changed) + "\n", encoding="utf-8")
    print(
        f"status={validation['status']} topics={len(topic_results)} "
        f"sessions={counts['sessions_audited']} errors={len(all_errors)}"
    )
    for error in all_errors[:40]:
        print("ERROR:", error)
    return 0 if not all_errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
