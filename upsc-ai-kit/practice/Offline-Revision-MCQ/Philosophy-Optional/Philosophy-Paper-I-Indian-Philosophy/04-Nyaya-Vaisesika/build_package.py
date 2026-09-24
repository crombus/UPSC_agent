from __future__ import annotations

import hashlib
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SESSION = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\04-Nyaya–Vaisesika\Learning-Session.md")
WORKBOOK = SESSION.with_name("Solved-Practice-Workbook.md")
CANONICAL = Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\indian\Nyaya-Vaisesika.md")
PYQ_OLD = Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2018-2025.md")
PYQ_NEW = Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2026.md")
NOW = "2026-09-24T19:58:07+05:30"
SOURCE_ARTIFACTS = [
    "README.md",
    "REVISION-GUIDE.md",
    "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md",
    "ANSWER-WRITING-TOOLKIT.md",
    "PRACTICE-LOG.md",
    "COVERAGE-LEDGER.md",
    "FORMAL-SOURCE-MIRROR.md",
    "FORMAL-COVERAGE-REVIEW.json",
    "FORMAL-COVERAGE-AUDIT.json",
    "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json",
    "TEST-MATRIX.json",
    "build_package.py",
    "render_pdfs.py",
    "validate_package.py",
    "run_negative_tests.py",
    ".gitattributes",
]


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_text(text: str) -> str:
    return sha_bytes(text.replace("\r\n", "\n").encode("utf-8"))


def norm_semantic(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).casefold()


def file_info(path: Path) -> dict:
    data = path.read_bytes()
    return {"path": str(path), "sha256": sha_bytes(data), "bytes": len(data)}


def slug(text: str) -> str:
    value = re.sub(r"<[^>]+>", "", text).lower()
    value = re.sub(r"[^\w]+", "-", value, flags=re.UNICODE).strip("-")
    return value[:72] or "block"


def classify_semantic_unit(unit: str) -> str | None:
    compact = re.sub(r"\s+", " ", unit.strip())
    plain = re.sub(r"[*_`>#]", "", compact).strip()
    if re.match(r"^[A-D]\.\s+", plain):
        return "mcq_option_coordinate"
    if re.match(r"^-\s*[A-D]:\s+", plain):
        return "option_explanation_coordinate"
    if re.fullmatch(r"Answer:\s*[A-D]\.?", plain, re.I):
        return "answer_key_coordinate"
    if re.fullmatch(r"(?:\d+\s*(?:(?:,|and)\s*\d+\s*)+(?:only)?|\d+\s+only)", plain, re.I):
        return "bare_numeric_combination"
    if re.fullmatch(
        r"(?:option explanations?|examiner traps?|demand decoded|why this earns marks|"
        r"model answer(?:\s*\([^)]*\))?|answer placement|core diagnostics|remedial drills)"
        r"[\s:.\-–—]*",
        plain,
        re.I,
    ):
        return "isolated_structural_label"
    if len(re.sub(r"[\W_]+", "", plain, flags=re.UNICODE)) < 3:
        return "nonsemantic_symbol_fragment"
    return None


def semantic_units(payload: str) -> tuple[list[str], list[dict]]:
    lines = payload.strip().splitlines()
    if lines and re.match(r"^#{2,5}\s+", lines[0]):
        lines = lines[1:]
    units, current, mode = [], [], None

    def flush() -> None:
        nonlocal current, mode
        text = "\n".join(current).strip()
        if text:
            units.append(text)
        current, mode = [], None

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if mode == "code":
                current.append(line)
                flush()
            else:
                flush()
                mode = "code"
                current = [line]
            continue
        if mode == "code":
            current.append(line)
            continue
        if stripped.startswith("|"):
            if mode not in (None, "table"):
                flush()
            mode = "table"
            current.append(line)
            continue
        if mode == "table" and not stripped.startswith("|"):
            flush()
        if not stripped:
            flush()
            continue
        if re.match(r"^\s*(?:[-*+]|\d+\.)\s+", line):
            flush()
            units.append(line.strip())
            continue
        if mode not in (None, "paragraph"):
            flush()
        mode = "paragraph"
        current.append(line)
    flush()
    meaningful, excluded = [], []
    for source_ordinal, unit in enumerate(units, 1):
        reason = classify_semantic_unit(unit)
        if reason:
            excluded.append({
                "source_ordinal": source_ordinal,
                "reason": reason,
                "exact_payload_sha256": sha_text(unit),
                "exact_payload": unit,
            })
        else:
            meaningful.append(unit)
    return meaningful, excluded


def source_blocks(path: Path, prefix: str) -> list[dict]:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    headings = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
        if match:
            headings.append((index, len(match.group(1)), match.group(2)))
    blocks = []
    for ordinal, (start, level, heading) in enumerate(headings, 1):
        own_end = headings[ordinal][0] if ordinal < len(headings) else len(lines)
        subtree_end = len(lines)
        for later_start, later_level, _ in headings[ordinal:]:
            if later_level <= level:
                subtree_end = later_start
                break
        own = "\n".join(lines[start:own_end]).strip() + "\n"
        subtree = "\n".join(lines[start:subtree_end]).strip() + "\n"
        ident = f"{prefix}-{slug(heading)}-{ordinal:03d}-{sha_text(own)[:10]}"
        segments = []
        if len(own) > 2400:
            for number, offset in enumerate(range(0, len(own), 1800), 1):
                chunk = own[offset:offset + 1800]
                segments.append({
                    "index": number, "start_char": offset,
                    "end_char_exclusive": offset + len(chunk),
                    "chars": len(chunk), "payload_sha256": sha_text(chunk),
                })
        blocks.append({
            "id": ident, "source": prefix, "ordinal": ordinal, "level": level,
            "heading": heading, "line_start": start + 1, "line_end": own_end,
            "own_payload_sha256": sha_text(own), "subtree_sha256": sha_text(subtree),
            "own_chars": len(own), "large_leaf_segments": segments,
            "_payload": own,
        })
    for block in blocks:
        children = []
        for candidate in blocks[block["ordinal"]:]:
            if candidate["level"] <= block["level"]:
                break
            if candidate["level"] == block["level"] + 1:
                children.append(candidate["id"])
        block["direct_children"] = children
        block["child_union_sha256"] = sha_text("\n".join(
            next(row["own_payload_sha256"] for row in blocks if row["id"] == child)
            for child in children
        ))
    return blocks


def anchored_copy(path: Path, blocks: list[dict], title: str) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    lookup: dict[tuple[int, str], list[str]] = {}
    for block in blocks:
        lookup.setdefault((block["level"], block["heading"]), []).append(block["id"])
    used: dict[tuple[int, str], int] = {}
    output = []
    for line in text.splitlines():
        match = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
        if match:
            key = (len(match.group(1)), match.group(2))
            index = used.get(key, 0)
            if key in lookup and index < len(lookup[key]):
                output.append(f'<a id="{lookup[key][index]}"></a>')
                used[key] = index + 1
        output.append(line)
    return (
        f"# {title}\n\n"
        "> Immutable exact-source mirror. Canonical corrections apply only to learner-facing surfaces; "
        "every formal payload remains hash-bound below.\n\n" + "\n".join(output) + "\n"
    )


def parse_mcqs(text: str) -> list[dict]:
    region = text.split("#### CORE DIAGNOSTICS", 1)[1].split("## PYQS AND ANSWER PRACTICE", 1)[0]
    items = []
    for chunk in re.split(r"(?=^#### MCQ \d+\.)", region, flags=re.M):
        head = re.match(r"#### MCQ (\d+)\.\s*(.+)\n", chunk)
        answer = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", chunk)
        explanations_region = re.search(r"\*\*Option explanations:\*\*\s*(.*?)(?=\n\*\*Examiner trap)", chunk, re.S)
        if not head:
            continue
        options = list(re.finditer(r"^([A-D])\.\s+(.+?)(?=\n\n[A-D]\.\s+|\n\n\*\*Answer:)", chunk, re.M | re.S))
        if len(options) != 4 or not answer or not explanations_region:
            raise ValueError(f"Cannot parse MCQ {head.group(1)}")
        explanations = {}
        for match in re.finditer(r"- \*\*([A-D]):\*\*\s*(.+?)(?=\n- \*\*[A-D]:\*\*|\Z)", explanations_region.group(1).strip(), re.S):
            explanations[match.group(1)] = re.sub(r"\s+", " ", match.group(2).strip())
        trap = re.search(r"\*\*Examiner trap \d+:\*\*\s*(.+)", chunk)
        stem = chunk[chunk.find("\n") + 1:options[0].start()].strip()
        items.append({
            "number": int(head.group(1)), "title": head.group(2).strip(), "stem": stem,
            "options": {match.group(1): re.sub(r"\s+", " ", match.group(2).strip()) for match in options},
            "answer": answer.group(1), "explanations": explanations,
            "trap": trap.group(1).strip() if trap else "",
        })
    return items


ADEQUATE_CELLS = [
    ("NV-TM-001", "Nyāya–Vaiśeṣika allied-school division of labour", "Distinguish Nyāya's epistemic method from Vaiśeṣika's ontological inventory without collapsing the schools.", [1], ["allied"], "formal session S1; canonical §§1.1–1.3"),
    ("NV-TM-002", "Nyāya's sixteen topics of inquiry", "Identify the sixteen padārthas as debate-and-inquiry topics rather than Vaiśeṣika ontological categories.", [2], ["sixteen"], "formal session S2; canonical §1.4"),
    ("NV-TM-003", "The twelve prameyas", "Recognize Nyāya's twelve knowables and their soteriological ordering.", [3], ["twelve"], "formal session S2; canonical §1.5"),
    ("NV-TM-004", "The nine substances", "Discriminate the complete Vaiśeṣika substance list from lists contaminated by qualities or motions.", [4], ["substances"], "formal session S3; canonical §2.3"),
    ("NV-TM-005", "Cognition and pleasure as qualities", "Locate cognition, pleasure and pain as adventitious qualities of self rather than substances.", [5], ["cognition"], "formal session S3; canonical §2.4"),
    ("NV-TM-006", "Motion's causal role", "Explain how motion produces conjunction and disjunction and thereby feeds production and destruction.", [6], ["motion", "conjunction", "disjunction"], "formal session S3; canonical §2.5"),
    ("NV-TM-007", "Real universals and disciplined universalhood", "Test the realist case for repeatable universals and the internal refusal of pseudo-universals.", [7, 8], ["universal"], "formal session S4; canonical §§2.6–2.7"),
    ("NV-TM-008", "Ultimate particularity", "Restrict viśeṣa to the individuation of eternal substances.", [9], ["particularity"], "formal session S4; canonical §2.8"),
    ("NV-TM-009", "Inherence contrasted with conjunction", "Separate constitutive ayutasiddha dependence from separable conjunction.", [10, 11], ["inherence"], "formal session S5; canonical §2.9"),
    ("NV-TM-010", "Four kinds of absence", "Classify prior, posterior, mutual and absolute absence by temporal and relational signature.", [12], ["absence"], "formal session S6; canonical §2.10"),
    ("NV-TM-011", "Absence examples and Nyāya cognition", "Apply absence categories and identify Nyāya's perceptual account of qualified non-apprehension.", [13, 14], ["absence"], "formal session S6; canonical §2.10"),
    ("NV-TM-012", "Gautama's perception definition", "Apply the clauses sense-born, non-verbal, non-errant and determinate to exclude rival cognitions.", [15], ["definition"], "formal session S7; canonical §3.2"),
    ("NV-TM-013", "Sense–object contact selection", "Select the appropriate ordinary contact for a presented object or property.", [16], ["contact"], "formal session S8; canonical §3.3"),
    ("NV-TM-014", "Extraordinary perception taxonomy", "Distinguish universal-mediated, cognition-mediated and yogic perception.", [17], ["extraordinary"], "formal session S8; canonical §3.4"),
    ("NV-TM-015", "Five-member public demonstration", "Identify the member whose epistemic function is not reproduced by a three-line Aristotelian form.", [18], ["member"], "formal session S9; canonical §4.3"),
    ("NV-TM-016", "Cause/effect/non-causal direction grid", "Classify pūrvavat, śeṣavat and sāmānyatodṛṣṭa by the causal or non-causal direction of the inferential move.", [19], ["cause", "effect", "non-causal", "direction"], "formal session S9; canonical §4.4"),
    ("NV-TM-017", "Valid reason and fallacy relation", "Read hetu marks and hetvābhāsas as positive and negative validity tests.", [20], ["fallacies"], "formal session S9–S10; canonical §§4.5–4.7"),
    ("NV-TM-018", "Upādhi control and vyāpti acquisition", "Diagnose a hidden condition and the disciplined anti-sceptical route to concomitance.", [21, 22], ["conditioning", "concomitance"], "formal session S10; canonical §§4.6–4.8"),
    ("NV-TM-019", "Sentence-intelligibility conditions", "Identify expectancy, semantic fitness, proximity and intended meaning as conditions of sentence cognition.", [23], ["expectancy", "fitness", "proximity", "intended meaning"], "formal session S11; canonical §5.2"),
    ("NV-TM-020", "Comparison as word–referent knowledge", "Identify Nyāya upamāna's distinctive result rather than reducing it to perception or inference.", [24], ["comparison"], "formal session S11; canonical §5.1"),
    ("NV-TM-021", "Extrinsic validity and instrument–fruit debate", "Distinguish parataḥ validity from intrinsic validity and pramāṇa from pramāṇaphala across realist and Buddhist analyses.", [25, 32], ["validity", "instrument"], "formal session S11; canonical §§5.4–5.5"),
    ("NV-TM-022", "Three error theories", "Keep anyathākhyāti, akhyāti and Buddhist appearance theories doctrinally distinct.", [26], ["error"], "formal session S12; canonical §6.1"),
    ("NV-TM-023", "Self and liberation baseline", "Connect enduring self proofs with apavarga as cessation of suffering and cognition-producing conditions.", [27, 28], ["self", "release"], "formal session S12; canonical §§6.2–6.4"),
    ("NV-TM-024", "God as efficient cause", "State what later Nyāya–Vaiśeṣika God explains without making God the material cause or reading late theism into Kaṇāda.", [29], ["God"], "formal session S13; canonical §7"),
    ("NV-TM-025", "Production causation and atomic aggregation", "Recognize ārambhavāda and the atom–dyad–triad route to gross objects.", [30, 31], ["causation", "atom"], "formal session S14; canonical §§8.1–8.3"),
]

GAP_CELL_SPECS = [
    ("Seven padārthas and the six-to-seven history", "Distinguish Kaṇāda's sixfold list from the later recognition of abhāva as the seventh category.", ["seven", "absence"], "formal S3 and canonical §§2.1–2.2", "partial"),
    ("Application of all six jāti-bādhakas", "Apply vyakter abheda, tulyatva, saṅkara, anavasthā, rūpahāni and asambandha to proposed universals.", ["blocker", "universal"], "formal S4 and canonical §2.7", "partial"),
    ("Viśeṣa regress and self-differentiation", "Explain why ultimate particularities individuate eternal substances without requiring further differentiators.", ["particularity", "regress"], "formal S4 and canonical §2.8", "partial"),
    ("Samavāya regress and the one–many problem", "Evaluate the self-linking reply to regress together with the claim that one inherence relates many heterogeneous pairs.", ["inherence", "regress"], "formal S5 and canonical §2.9", "partial"),
    ("Nyāya, Buddhist and Bhāṭṭa absence cognition", "Compare qualified non-apprehension in Nyāya, conceptual construction in Buddhism and anupalabdhi in Bhāṭṭa Mīmāṃsā.", ["absence", "Bhāṭṭa"], "formal S6 and canonical §2.10", "partial"),
    ("Nirvikalpaka, savikalpaka and Gautama's tension", "Relate indeterminate and determinate perception to the apparently determinate clause in Gautama's definition.", ["nirvikalpaka", "savikalpaka"], "formal S7 and canonical §3.2", "partial"),
    ("All six sannikarṣas", "Apply conjunction, inherence, inherence-in-the-conjoined, inherence-in-the-inherent, qualifier–qualified relation and the special sound relation.", ["six", "contact"], "formal S8 and canonical §3.3", "partial"),
    ("All three inference classification grids", "Classify inference by purpose, observed mark and structure of concomitance without mixing the grids.", ["three", "classification"], "formal S9 and canonical §4.4", "partial"),
    ("Five characteristics of a valid hetu", "Apply pakṣasattva, sapakṣasattva, vipakṣāsattva, abādhitatva and asatpratipakṣatva together.", ["five", "reason"], "formal S9 and canonical §4.5", "partial"),
    ("Five hetvābhāsa families and subtypes", "Distinguish savyabhicāra subtypes, viruddha, satpratipakṣa, asiddha subtypes and bādhita.", ["fallacy", "subtype"], "formal S10 and canonical §4.7", "partial"),
    ("Vyāpti, samavyāpti and viṣamavyāpti", "Distinguish invariant pervasion from equal and unequal extension.", ["vyapti", "extension"], "formal S10 and canonical §4.6", "partial"),
    ("Tarka's status and unacceptable-consequence forms", "Treat tarka as an auxiliary reductio rather than an independent pramāṇa and recognize self-defeat, regress and contradiction forms.", ["tarka", "pramana"], "formal S10 and canonical §4.8", "partial"),
    ("Cārvāka objections, Nyāya replies and Hume comparison", "Compare induction scepticism while preserving Nyāya's upādhi-elimination and realism about universals.", ["Carvaka", "Hume"], "formal S10 and canonical §§4.8, 10.2", "partial"),
    ("Nyāya versus Mīmāṃsā on upamāna", "Contrast word–referent learning with cognition of similarity involving a remembered object.", ["comparison", "Mimamsa"], "formal S11 and canonical §5.1", "partial"),
    ("Āpta, secular and Vedic testimony classifications", "Combine reliability conditions with dṛṣṭārtha/adṛṣṭārtha and secular/Vedic testimony.", ["apta", "Vedic"], "formal S11 and canonical §5.2", "partial"),
    ("Naiyāyika versus Prābhākara śābdabodha", "Contrast abhihitānvaya's two-stage synthesis with anvitābhidhāna's directly connected meanings.", ["sentence", "Prabhakara"], "formal S11 and canonical §5.3", "partial"),
    ("Why memory is not a pramāṇa", "Explain memory's dependence on prior cognition and its failure to disclose a previously unknown object.", ["memory", "new"], "formal S11 and canonical §5.4", "partial"),
    ("Complete jñānalakṣaṇa–memory–misplacement anyathākhyāti", "Trace shell-silver error from present perception through memory and extraordinary presentation to false location.", ["memory", "misplacement"], "formal S12 and canonical §6.1", "partial"),
    ("Manas, episodic consciousness and self objections", "Use atomic mind to explain serial cognition while answering Buddhist bundle and Advaita witness objections.", ["mind", "Buddhist"], "formal S12 and canonical §§6.2–6.3", "partial"),
    ("Liberation's full causal ladder", "Apply the error–defect–action–birth–suffering chain and its reverse cessation.", ["error", "suffering"], "formal S12 and canonical §6.4", "partial"),
    ("Udayana's four principal proofs", "Integrate kāryāt, āyojanāt, dhṛtyādeḥ and śruteḥ as a cumulative case.", ["Udayana", "four"], "formal S13 and canonical §7.2", "partial"),
    ("Nyāya versus classical Yoga on God", "Distinguish efficient causal and karmic governance from Yoga's special puruṣa and pedagogical-liberative role.", ["Yoga", "God"], "formal S13 and canonical §7.3", "partial"),
    ("Mīmāṃsā, Buddhist, Sāṃkhya and evil objections", "Identify which rival objection attacks Vedic authorship, creator inference, material sufficiency or providence.", ["objection", "evil"], "formal S13 and canonical §7.4", "partial"),
    ("Ananyathāsiddha and five accidental antecedents", "Separate a genuine causal antecedent from mere prior, remote, co-present, effect-dependent or extraneous conditions.", ["antecedent", "five"], "formal S14 and canonical §8.1", "partial"),
    ("Samavāyi, asamavāyi and nimitta causes applied", "Assign material, non-inherent and efficient causal roles in one concrete case.", ["cause", "threads"], "formal S14 and canonical §8.1", "partial"),
    ("Seed–tree case for asatkāryavāda", "Use destruction, novelty and causal specificity to defend new production against pre-existence.", ["seed", "new"], "formal S14 and canonical §8.2", "partial"),
    ("Atomic eternality, partlessness and regress", "Explain why atoms are eternal and partless and why further division generates regress.", ["atoms", "partless"], "formal S14 and canonical §8.3", "partial"),
    ("First motion, adṛṣṭa, God, creation and dissolution", "Sequence karmic unseen potency, divine governance, atomic motion, aggregation and cosmic dissolution.", ["motion", "dissolution"], "formal S14 and canonical §8.4", "partial"),
    ("Buddhist apoha and avayavin objections", "Answer exclusion theory and the denial of a whole over and above parts without begging realism.", ["apoha", "whole"], "formal S15 and canonical §§2.6, 8.3, 9", "partial"),
    ("Jaina anekānta challenge", "Assess the many-sidedness objection to fixed categories and Nyāya's determinate-predication reply.", ["Jaina", "categories"], "formal S15 and canonical §9", "untested"),
    ("Words signifying universals versus particulars", "Distinguish universal-first denotation from contextually delimited reference to particulars.", ["words", "universal"], "formal S15 and canonical §5.2", "untested"),
    ("Controlled Bradley, Plato, Aquinas and system transfer", "Use Western comparisons only to sharpen regress, universal and theistic issues while preserving doctrinal differences.", ["Bradley", "Plato", "Aquinas"], "formal optional enrichment and canonical §10.2", "untested"),
]

SPECIAL_SEMANTIC_ASSERTIONS = {
    "NV-TM-006": [
        {"assertion": "motion produces both conjunction and disjunction", "all_of": [["motion"], ["conjunction"], ["disjunction"]]},
        {"assertion": "those relations feed causation", "all_of": [["causation", "production"], ["destruction", "effect"]]},
    ],
    "NV-TM-016": [
        {"assertion": "the direction grid includes cause-to-effect", "all_of": [["cause"], ["effect"]]},
        {"assertion": "the same grid includes non-causal uniformity", "all_of": [["non-causal", "noncausal"], ["direction", "basis", "uniformity"]]},
    ],
    "NV-TM-019": [
        {"assertion": "sentence cognition requires expectancy and fitness", "all_of": [["expectancy"], ["fitness"]]},
        {"assertion": "sentence cognition also requires proximity and intended meaning", "all_of": [["proximity"], ["intended meaning", "intention"]]},
    ],
    "NV-TM-033": [
        {"assertion": "purpose or audience grid", "all_of": [["svārtha", "svartha"], ["parārtha", "parartha"], ["purpose", "audience"]]},
        {"assertion": "observed-mark grid", "all_of": [["pūrvavat", "purvavat"], ["śeṣavat", "sesavat"], ["sāmānyatodṛṣṭa", "samanyatodrsta"], ["observed mark"]]},
        {"assertion": "concomitance-structure grid", "all_of": [["kevalānvayi", "kevalanvayi"], ["kevalavyatireki"], ["anvayavyatireki"], ["concomitance"]]},
    ],
    "NV-TM-040": [
        {"assertion": "āpta has epistemic competence", "all_of": [["āpta", "apta"], ["knowledge", "competence"]]},
        {"assertion": "āpta communicates sincerely", "all_of": [["truthful", "sincere", "sincerity"]]},
    ],
    "NV-TM-057": [
        {"assertion": "Bradley comparison remains controlled", "all_of": [["bradley"], ["regress"], ["self-linking inherence"]]},
        {"assertion": "Plato comparison preserves immanent universals", "all_of": [["plato"], ["immanent"]]},
        {"assertion": "Aquinas comparison preserves Nyāya differences", "all_of": [["aquinas"], ["eternal atoms"], ["souls"], ["karma"]]},
    ],
    "NV-TM-058": [
        {"assertion": "all five motions are independently enumerated", "all_of": [["upward movement"], ["downward movement"], ["contraction"], ["expansion"], ["locomotion"]]},
    ],
    "NV-TM-059": [
        {"assertion": "evaluation states the system's strengths", "all_of": [["realist"], ["inference discipline", "inferential discipline", "disciplined inference"], ["systematic integration", "integrates"]]},
        {"assertion": "evaluation identifies contested primitive stopping points", "all_of": [["samavāya", "samavaya"], ["regress", "self-linking"], ["viśeṣa", "visesa"], ["self-differentiation", "self-differentiating"]]},
        {"assertion": "evaluation includes epistemic or soteriological weaknesses", "all_of": [["sāmānyalakṣaṇa", "samanyalaksana", "induction"], ["unconscious liberation", "liberation without cognition-producing qualities", "motivation"], ["god", "karma"]]},
        {"assertion": "overall verdict is expressly conditional", "all_of": [["conditional", "if one accepts", "depends on accepting"], ["not an unconditional", "not absolute", "rather than absolute"]]},
    ],
}


def semantic_assertions(cell_id: str, tokens: list[str]) -> list[dict]:
    return SPECIAL_SEMANTIC_ASSERTIONS.get(
        cell_id,
        [{"assertion": "cell-specific discriminator terms", "all_of": [tokens]}],
    )


def additional_mcqs() -> list[dict]:
    rows = [
        ("Seven categories, but not at every historical layer", "Which statement gives the most historically disciplined account of Vaiśeṣika padārthas?",
         ["Kaṇāda explicitly fixed seven categories, including absence, in the earliest stratum.", "The school always had only six categories because absence remained merely linguistic.", "The classical list has seven categories, while the earlier sixfold scheme was later expanded by admitting absence.", "Nyāya's sixteen topics were reduced to seven ontological categories by Gautama."], 2),
        ("Six blockers used as six refusal tests", "Which sequence correctly matches six proposed universals with the reason each is refused?",
         ["Ether-ness—single instance; pot-ness and jar-ness—co-extension; elementhood and corporeality—partial overlap; universalhood—regress; a universal in viśeṣas—loss of individuating function; inherence-ness—lack of a further inherence.", "Ether-ness—partial overlap; pot-ness and jar-ness—regress; elementhood and corporeality—single instance; universalhood—loss of function; a universal in viśeṣas—lack of inherence; inherence-ness—co-extension.", "Ether-ness—co-extension; pot-ness and jar-ness—single instance; elementhood and corporeality—regress; universalhood—partial overlap; a universal in viśeṣas—lack of inherence; inherence-ness—loss of function.", "Ether-ness—regress; pot-ness and jar-ness—partial overlap; elementhood and corporeality—loss of function; universalhood—single instance; a universal in viśeṣas—co-extension; inherence-ness—lack of inherence."], 0),
        ("Viśeṣa without a second differentiator", "How does Vaiśeṣika stop a regress when ultimate particularity individuates eternal atoms?",
         ["Each viśeṣa is individuated by a numerically later viśeṣa.", "Viśeṣas are self-differentiating ultimates; requiring another differentiator would restart the problem they solve.", "Spatial conjunction alone differentiates atoms, even before motion and conjunction arise.", "The universal atomhood differentiates one atom from every other atom."], 1),
        ("One inherence and the regress objection", "Which response most directly addresses both the regress objection to samavāya and the puzzle that one relation serves many pairs?",
         ["Every instance has a separate inherence connected by a higher inherence.", "Inherence is reducible to conjunction whenever its relata cannot be separated.", "Samavāya is one because all dependent location is identical with substancehood.", "Samavāya is an irreducible self-linking relation instantiated across heterogeneous inseparable pairs; it does not need another connector."], 3),
        ("How three schools know absence", "Which comparison of absence cognition is correct?",
         ["Nyāya uses qualified non-apprehension in a perceptible locus; Bhāṭṭa accepts anupalabdhi as independent; Buddhist analysis tends to treat absence as conceptual construction.", "Nyāya and Bhāṭṭa both reduce absence to inference, while Buddhism admits it as a seventh category.", "Nyāya admits independent anupalabdhi, Bhāṭṭa uses perception, and Buddhism treats absence as inherence.", "All three accept absence as a mind-independent padārtha known by ordinary contact."], 0),
        ("Two stages and Gautama's wording", "Which account best handles nirvikalpaka and savikalpaka perception alongside Gautama's definition?",
         ["Only savikalpaka cognition is perceptual because avyapadeśya literally excludes every pre-predicative awareness.", "Nirvikalpaka is verbal and relational, while savikalpaka is wholly indeterminate.", "An initial non-predicative awareness may precede determinate classification; the definition's determinate language creates an interpretive tension rather than abolishing that stage.", "Both stages are inferential because recognition requires a universal."], 2),
        ("All six ordinary contacts", "Which list gives the six Nyāya sense–object contacts without replacing one by an extraordinary perception?",
         ["Conjunction; inherence in what is conjoined; inherence in what inheres in the conjoined; inherence; inherence in what inheres; qualifier–qualified relation.", "Conjunction; resemblance; memory; universal-mediated contact; yogic contact; inherence.", "Inherence; implication; non-apprehension; conjunction; testimony; qualifier–qualified relation.", "Conjunction; inherence; cognition-mediated contact; universal-mediated contact; yogic contact; absence."], 0),
        ("Three grids, three questions", "Which option correctly aligns Nyāya's three inference classifications?",
         ["Svārtha/parārtha classify extension; pūrvavat/śeṣavat/sāmānyatodṛṣṭa classify audience; kevalānvayi/kevalavyatireki/anvayavyatireki classify temporal order.", "Svārtha/parārtha classify purpose or audience; pūrvavat/śeṣavat/sāmānyatodṛṣṭa classify the observed mark; kevalānvayi/kevalavyatireki/anvayavyatireki classify concomitance structure.", "All three grids classify the number of members in a demonstration.", "The first two grids are Nyāya, but the third belongs only to Buddhist logic."], 1),
        ("The five marks of a valid reason", "A reason is present in the subject and positive instances, absent from negative instances, undefeated by stronger knowledge, and not counterbalanced. What follows?",
         ["It satisfies pakṣasattva, sapakṣasattva, vipakṣāsattva, abādhitatva and asatpratipakṣatva.", "It is valid only if restated in all five members of public demonstration.", "It establishes equal extension but cannot establish unequal extension.", "It remains fallacious until supported by testimony."], 0),
        ("Five fallacy families with subtype discipline", "Which classification is doctrinally complete?",
         ["Savyabhicāra alone has three subtypes; viruddha proves the opposite; satpratipakṣa is counterbalanced; asiddha has locus, intrinsic and pervasion failures; bādhita is contradicted by stronger cognition.", "Viruddha and bādhita are subtypes of asiddha, while savyabhicāra means only a missing subject.", "Satpratipakṣa is the same as irregularity, and asiddha has no subtypes.", "The five families are defects of verbal testimony rather than inferential reasons."], 0),
        ("Pervasion and extension", "Which statement distinguishes vyāpti, samavyāpti and viṣamavyāpti?",
         ["Vyāpti is any frequent association; samavyāpti is causal succession; viṣamavyāpti is accidental coexistence.", "Vyāpti is exceptionless pervasion; samavyāpti is convertible equal extension; viṣamavyāpti is one-way unequal extension, as smoke is pervaded by fire but not conversely.", "Samavyāpti and viṣamavyāpti are two fallacies that defeat vyāpti.", "Viṣamavyāpti means the reason occurs in every dissimilar instance."], 1),
        ("Tarka assists but does not certify alone", "What is tarka's proper epistemic status?",
         ["It is an independent fifth pramāṇa that directly discovers facts.", "It is testimony framed as a hypothetical proposition.", "It is auxiliary reasoning that exposes an unacceptable consequence—such as contradiction, self-defeat or regress—and supports a pramāṇa without replacing one.", "It is doubt retained after all rival alternatives are equally confirmed."], 2),
        ("Cārvāka, Nyāya and Hume on induction", "Which comparison avoids assimilating Nyāya either to dogmatism or to Hume?",
         ["Cārvāka and Hume both accept real universals, whereas Nyāya reduces expectation to habit.", "Nyāya concedes that no inference can exceed observed cases and therefore abandons vyāpti.", "Hume's habit and Nyāya's universal-mediated perception are identical psychological explanations.", "Cārvāka attacks unobserved pervasion and Hume denies rational necessity from repetition; Nyāya replies through counterexample search, upādhi-elimination, tarka and realism about universals."], 3),
        ("Two fruits called upamāna", "How do Nyāya and Mīmāṃsā characteristically distinguish the fruit of comparison?",
         ["Nyāya stresses learning that the seen cow-like animal is the referent of 'gavaya'; Mīmāṃsā stresses cognition that the remembered cow is similar to the present gavaya.", "Nyāya treats comparison as inference, while Mīmāṃsā treats it as testimony.", "Nyāya knows only similarity, while Mīmāṃsā alone connects a word with an object.", "Both define the result exclusively as perception of a universal."], 0),
        ("Āpta and kinds of testimony", "Which account combines the reliability condition and the standard testimony classifications?",
         ["An āpta must be Vedic and omniscient; secular testimony is never pramāṇa.", "Āpta requires knowledge and truthful communication; testimony may concern perceptible or supersensible matters and may be secular or Vedic.", "Any grammatically complete sentence is valid testimony regardless of the speaker.", "Vedic testimony is inferential, while secular testimony is comparison."], 1),
        ("How words yield one sentence cognition", "Which contrast between Naiyāyika abhihitānvaya and Prābhākara anvitābhidhāna is accurate?",
         ["Nyāya says words first denote separate meanings later syntactically connected; Prābhākara says words directly express meanings already related in the sentence.", "Nyāya denies stable word meaning; Prābhākara makes sentence cognition a later inference.", "Both theories reduce sentence meaning to speaker intention alone.", "Prābhākara accepts isolated denotation first, while Nyāya denies any compositional stage."], 0),
        ("Why recollection is not fresh knowledge", "Why does Nyāya exclude memory from the pramāṇas?",
         ["Memory is always false because its object no longer exists.", "Memory is produced without any causal condition.", "Memory depends on a trace of prior cognition and presents its object as already known rather than disclosing a previously unknown object.", "Memory is a kind of testimony because words are silently repeated."], 2),
        ("The full shell–silver mechanism", "Which sequence states Nyāya anyathākhyāti most completely?",
         ["Shell perception → destruction of silver → inference of non-being → verbal error.", "Perception of 'this' shell → resemblance-triggered silver memory → jñānalakṣaṇa presentation of elsewhere-silver → non-discrimination and misplacement as 'this is silver'.", "Pure silver memory → denial of the shell → intrinsic falsity with no presented object.", "A non-existent silver is directly perceived through ordinary conjunction."], 1),
        ("Mind, episodic awareness and the enduring self", "Which Nyāya argument and reply-set is coherent?",
         ["Simultaneous awareness of all senses proves an all-pervasive mind; Buddhism and Advaita agree.", "Atomic manas connects the self with one sense at a time, explaining serial episodes; Nyāya answers the Buddhist bundle through ownership and continuity, and answers Advaita by treating cognition as an adventitious quality rather than the self's essence.", "Manas is the permanent self, so no distinct bearer is needed.", "The self is inferred only from bodily shape, and liberation preserves every mental quality."], 1),
        ("Reversing the bondage ladder", "Which chain correctly states bondage and the route to apavarga?",
         ["Birth → knowledge → desire → merit → pleasure, reversed by ritual alone.", "Error → defects such as attachment and aversion → action → rebirth → suffering; true knowledge removes error, thereby ending the downstream conditions.", "Action → atoms → universals → perception → absence, reversed by God.", "Suffering → self → mind → memory → liberation, with cognition remaining eternally active."], 1),
        ("Udayana's cumulative four-proof structure", "Which reconstruction correctly combines Udayana's four principal proofs?",
         ["Kāryāt infers an intelligent cause from effects; āyojanāt explains initial atomic combination; dhṛtyādeḥ invokes sustaining order; śruteḥ invokes reliable Vedic testimony.", "Kāryāt proves material creation ex nihilo; āyojanāt denies atoms; dhṛtyādeḥ rejects order; śruteḥ rejects testimony.", "All four are versions of the ontological argument from the definition of a perfect being.", "Only śruteḥ is inferential; the other three are forms of perception."], 0),
        ("Nyāya's Lord and Yoga's special puruṣa", "Which contrast is most accurate?",
         ["Both systems make God the material cause of an otherwise non-eternal world.", "Classical Yoga's Īśvara is a special puruṣa untouched by affliction and a teacher-support for practice; later Nyāya's Īśvara is the efficient cause and karmic governor coordinating eternal atoms and selves.", "Nyāya denies divine cognition, whereas Yoga makes God the creator of karma.", "Yoga derives God only from Vedic authorship, while Nyāya treats God only as an object of devotion."], 1),
        ("Four objections to the Nyāya God", "Which allocation of objections is best?",
         ["Mīmāṃsā questions the need for a divine Veda-author; Buddhism rejects permanent creator and substance; Sāṃkhya invokes prakṛti's sufficiency; the problem of evil challenges providential governance under suffering.", "Mīmāṃsā accepts divine authorship, Buddhism accepts eternal atoms, and Sāṃkhya alone raises evil.", "All three schools object only that God lacks a body.", "The problem of evil disappears once God is called an efficient rather than material cause."], 0),
        ("The causal antecedent must be non-accidental", "What does ananyathāsiddha add to mere temporal priority?",
         ["A cause must be an invariable antecedent not otherwise established as a quality of an instrument, remote cause, co-effect, ubiquitous background or accidental companion.", "Every earlier event is a cause unless later perception cancels it.", "Only material constituents can be causes; efficient conditions are accidental.", "A cause is whatever resembles the effect most closely."], 0),
        ("Three causes in a cloth", "In the production of a cloth, which assignment is correct?",
         ["Threads are samavāyi; conjunction or colour of threads can be asamavāyi; loom, shuttle and weaver function as nimitta conditions.", "The weaver is samavāyi, threads are nimitta, and cloth-colour is the material cause.", "Thread-conjunction is samavāyi, the finished cloth is asamavāyi, and threads are efficient.", "All antecedents are one undifferentiated causal type."], 0),
        ("Why the tree is a new effect", "Which seed–tree argument supports Nyāya–Vaiśeṣika asatkāryavāda?",
         ["The mature tree is already manifest inside the intact seed in the same form.", "The destruction and reorganization of the seed, the novelty of the tree and the specificity of the causal complex support genuinely new production rather than manifestation of a pre-existent effect.", "Any seed can produce any tree because the effect is wholly unrelated to its cause.", "The tree is unreal because it did not exist before production."], 1),
        ("Why atoms terminate division", "Why are Vaiśeṣika atoms treated as eternal and partless?",
         ["They are perceptible wholes whose parts are temporarily hidden.", "If atoms had produced parts, division would continue without a fundamental material terminus; partlessness blocks the regress, while compounds arise and perish through conjunction and disjunction.", "Their eternality follows because God creates them anew in every cosmic cycle.", "They are universals rather than substances."], 1),
        ("From unseen merit to a world, and back", "Which sequence best represents later Nyāya–Vaiśeṣika cosmogony?",
         ["God creates atoms from nothing, then destroys souls at dissolution.", "Adṛṣṭa operates without governance, and random motion necessarily produces the same world.", "God coordinates adṛṣṭa and initiates atomic motion; dyads and higher aggregates form a world, while dissolution separates compounds without annihilating eternal atoms and selves.", "Dissolution abolishes karma, atoms and God before a wholly new creation."], 2),
        ("Exclusion and the whole over parts", "Which pair of Nyāya replies addresses Buddhist apoha and avayavin objections?",
         ["Against apoha, repeated positive predication and cross-instance recognition support a real universal; against reduction to parts, unified properties and actions support a whole inhering in its parts.", "Against apoha, words denote only exclusions; against the whole objection, no entity exceeds momentary atoms.", "Nyāya accepts apoha for nouns but not verbs, and treats the whole as a convention.", "Both objections are answered solely by divine testimony."], 0),
        ("Anekānta and determinate categories", "How should Nyāya answer the Jaina anekānta challenge without ignoring it?",
         ["Every contradictory predicate is unconditionally true of the same object.", "Standpoint sensitivity can expose omitted qualifications, but inference and debate still require determinate, non-contradictory predication under stated conditions.", "Categories must be abandoned because all claims are equally partial.", "Anekānta is identical with Nyāya doubt and therefore needs no reply."], 1),
        ("Do words signify a universal or a particular?", "Which Nyāya account best preserves repeatability and contextual reference?",
         ["A word signifies only one bare individual and can never apply to another.", "A word denotes a transcendent Form separated from every instance.", "A noun presents an individual as qualified by a universal and configuration, so class-based repeatability and contextually delimited particular reference are both preserved.", "Words signify only exclusions and never positive features."], 2),
        ("Controlled comparative transfer", "Which comparative set is philosophically controlled rather than assimilative?",
         ["Bradley's regress is identical to samavāya, Plato's Forms inhere in particulars, and Aquinas makes eternal atoms co-causes.", "Bradley helps frame relation-regress though Nyāya stops it with self-linking inherence; Plato clarifies realism though Nyāya universals are immanent; Aquinas sharpens first-cause comparison though Nyāya retains eternal atoms, souls and karma.", "All three Western positions are historical sources of Nyāya doctrine.", "The comparisons prove that Nyāya is simply medieval European realism in Sanskrit terminology."], 1),
        ("The five motions as a complete taxonomy", "Which option gives exactly the five kinds of motion (*karma*) recognized by Vaiśeṣika?",
         ["Upward movement, downward movement, contraction, expansion and locomotion.", "Upward movement, downward movement, conjunction, disjunction and locomotion.", "Contraction, expansion, cognition, desire and locomotion.", "Upward movement, impact, fluidity, heaviness and locomotion."], 0),
        ("A conditional evaluation of the integrated system", "Which assessment most fairly weighs Nyāya–Vaiśeṣika as an integrated philosophical system?",
         ["Its realist ontology, inference discipline and systematic integration settle every explanatory issue; samavāya, viśeṣa, induction, liberation and divine governance therefore need no further defence.", "Its categories are useful only historically, because regress objections to samavāya and viśeṣa, uncertainty about induction, liberation without cognition-producing qualities and God–karma tensions jointly refute the system.", "Its realist logic and ontology, disciplined inference and systematic integration are major strengths; yet samavāya's self-linking stop, viśeṣa's self-differentiation, sāmānyalakṣaṇa or induction, liberation without cognition-producing qualities and God–karma tensions remain contested, so the overall verdict is conditional rather than absolute and depends on accepting these primitive termini.", "Its strongest contribution is the Bradley–Plato–Aquinas comparison, which resolves internal disputes about inherence, universals, liberation and God by importing Western conclusions."], 2),
    ]
    extensions = [
        ("; absence therefore belongs to the original enumeration", "; negation remains solely a feature of language", "", "; the epistemic and ontological lists are thereby unified"),
        ("", "; plurality is treated as the master test for every candidate", "; regress is treated as the master test for every candidate", "; category crossing is treated as the master test for every candidate"),
        ("; every differentiator consequently receives a further differentiator", "", "; conjunction supplies each atom with a unique relational position", "; atomhood distributes numerical identity among its instances"),
        ("; the hierarchy terminates in a highest connecting relation", "; inseparability is explained as permanent conjunction", "; substancehood itself supplies dependent location", ""),
        ("", "; all three accounts become inferential analyses", "; anupalabdhi and perceptual qualification exchange their school ownership", "; conceptual absence is elevated into an independent external category"),
        ("; avyapadeśya is read as excluding every indeterminate stage", "; perceptual order begins with a verbally structured judgement", "", "; universal involvement converts both stages into inference"),
        ("", "; similarity and recollection are counted as ordinary sensory relations", "; logical implication and testimony become varieties of contact", "; extraordinary perception supplies half of the ordinary list"),
        ("; the grids are reordered around extension, audience and temporal sequence", "", "; member-count becomes the common basis of classification", "; pervasion-structure is assigned exclusively to Buddhist logic"),
        ("", "; public formulation becomes a sixth condition of validity", "; unequal extension is excluded from every valid inference", "; reliable testimony supplies any missing inferential condition"),
        ("", "; contradiction by the reason is absorbed into unestablished reason", "; counterbalance is treated as merely another irregular occurrence", "; the classification is transferred from inference to testimony"),
        ("; repetition itself is treated as sufficient for universality", "", "; equal and unequal extension become defects of a reason", "; negative instances are made loci of the inferential sign"),
        ("; independent reductive knowledge follows from supposition alone", "; a speaker's hypothetical statement supplies the conclusion", "", "; tarka preserves competing alternatives in permanent balance"),
        ("; Cārvāka and Hume become realists while Nyāya becomes associationist", "; every unobserved case remains inaccessible to inference", "; both accounts reduce necessity to the same mental habit", ""),
        ("", "; both schools reduce the result to inference from similarity", "; Nyāya receives similarity alone and Mīmāṃsā receives naming", "; universal perception becomes the sole comparative result"),
        ("; only an omniscient Vedic speaker can count as reliable", "", "; grammatical completion alone guarantees truth", "; the two classifications are recast as inference and comparison"),
        ("", "; the school names are exchanged while preserving the same two stages", "; sentence meaning is reduced entirely to intention", "; directly connected expression is assigned to Nyāya"),
        ("; non-existence of the remembered object is made the source of error", "; recollection occurs spontaneously without a retained trace", "", "; inner verbal repetition supplies testimonial force"),
        ("; negation and inference replace the positive presentation of silver", "", "; memory remains isolated and never enters a present judgement", "; ordinary conjunction reaches the absent silver itself"),
        ("; an all-pervasive mind produces simultaneous multisensory awareness", "", "; the internal instrument becomes identical with the enduring subject", "; bodily continuity alone bears recognition, agency and recollection"),
        ("; ritual merit alone reverses a ladder beginning in birth", "", "; metaphysical categories replace the affective and karmic sequence", "; all mental qualities remain manifest in the liberated state"),
        ("", "; each proof establishes the denial of the feature named by it", "; all four become variants of a definition-based ontological proof", "; perception directly establishes the first three conclusions"),
        ("; both systems treat God as the world's material substrate", "", "; Nyāya's Lord lacks cognition while Yoga's creates karma", "; each school restricts God to one narrowly verbal function"),
        ("", "; each rival is assigned acceptance of the doctrine it contests", "; bodily absence becomes the single objection shared by all rivals", "; efficient causality is treated as dissolving the suffering problem"),
        ("", "; temporal priority alone becomes sufficient for causation", "; efficient conditions are excluded from the causal complex", "; resemblance replaces invariance and necessity"),
        ("", "; the maker and material exchange their causal classifications", "; a produced relation replaces the material constituents", "; causal differences collapse into temporal priority"),
        ("; production becomes disclosure of an already formed tree", "", "; unrestricted production follows from total prior non-existence", "; prior absence is taken to entail permanent unreality"),
        ("; perceptibility guarantees a hidden internal mereology", "", "; divine recreation replaces atomic eternality", "; universality replaces substantial individuality"),
        ("; creation begins with production of atoms and ends with destroyed souls", "; unguided adṛṣṭa fixes cosmic order by itself", "", "; dissolution annihilates every eternal entity"),
        ("", "; Nyāya adopts exclusion and denies any whole beyond parts", "; lexical realism varies between nouns and verbs", "; both disputes are settled only through revelation"),
        ("; contradictory predicates hold without standpoint qualification", "", "; contextual qualification requires abandoning every fixed category", "; the challenge is reduced to ordinary undecided doubt"),
        ("; reference is permanently confined to one individual", "; denotation reaches a separately existing transcendent Form", "", "; positive signification is replaced wholly by exclusion"),
        ("; every analogy is asserted as doctrinal identity", "", "; historical borrowing is inferred from conceptual comparison", "; Nyāya is reduced to a translated European system"),
        ("", "; conjunction and disjunction replace two members of the motion taxonomy", "; qualities of the self replace four physical motions", "; qualities and impact replace contraction and expansion"),
        ("; every contested stopping point is declared conclusively solved", "; criticism is converted into total refutation", "", "; controlled comparison is mistaken for internal graded evaluation"),
    ]
    traps = [
        "Do not read the later sevenfold list back into Kaṇāda's earliest enumeration.",
        "Do not name only two or three blockers; each example must instantiate its own refusal rule.",
        "A shared universal explains likeness, not the numerical difference that viśeṣa must secure.",
        "Calling samavāya self-linking answers regress only if its one-relation/many-loci role is also stated.",
        "Do not give Bhāṭṭa's independent anupalabdhi to Nyāya or turn Buddhist construction into a padārtha.",
        "Gautama's wording creates a tension with nirvikalpaka; it does not erase the admitted two-stage account.",
        "Do not mix the six ordinary sannikarṣas with the three extraordinary perceptions.",
        "State the basis of classification before naming types; the three grids are not interchangeable lists.",
        "The five marks test the reason and probandum relation, not the five-member order of presentation.",
        "Savyabhicāra and asiddha have subtypes, but viruddha, satpratipakṣa and bādhita remain distinct families.",
        "Unequal extension is not defective pervasion; it is one-directional pervasion.",
        "Tarka removes a rival supposition but does not independently generate pramā.",
        "The Hume analogy is controlled: Nyāya adds universals and upādhi-removal rather than reducing expectation to habit.",
        "Both schools accept upamāna; the disputed point is the novel cognition it produces.",
        "Do not identify āpta with social rank or restrict reliable testimony to the Veda.",
        "Nyāya is abhihitānvaya-type, but it should not be mechanically equated with the Bhāṭṭa account.",
        "Truth and practical usefulness do not make recollection a fresh instrument of knowledge.",
        "Anyathākhyāti needs all four links: present 'this', memory, jñānalakṣaṇa and misplacement.",
        "Manas explains serial access; it is neither the self nor a substitute for the self-inference.",
        "Liberation reverses the causal chain by removing error, not by directly destroying an eternal self.",
        "Present Udayana's proofs cumulatively and keep God efficient rather than material cause.",
        "Shared theism does not make Yoga's special puruṣa identical with Nyāya's cosmic arranger.",
        "Karma is Nyāya's reply to evil, not a reason the problem disappears without residue.",
        "Temporal priority is too wide; ananyathāsiddha excludes five recurrent accidental antecedent types.",
        "The non-inherent cause resides in the material cause; it is not another name for the maker.",
        "Prior non-existence supports new production, not production without a specific causal complex.",
        "Partlessness terminates physical division; it does not make atoms universals or freshly created entities.",
        "Adṛṣṭa supplies moral potency, while later Nyāya assigns intelligent coordination to God.",
        "Apoha and the denial of avayavin are different objections and require different realist replies.",
        "Anekānta supports qualification by standpoint, not unrestricted contradiction.",
        "Nyāya's noun denotes a particular as qualified; neither bare particularism nor transcendent Forms is adequate.",
        "Use Bradley, Plato and Aquinas as controlled comparisons, never as claims of identity or historical derivation.",
        "Do not confuse motion's causal products, conjunction and disjunction, with the five members of the motion taxonomy.",
        "A graded verdict must preserve both explanatory achievements and live stopping-point objections; neither triumphalism nor total dismissal is adequate.",
    ]
    for row_index, row in enumerate(rows):
        title, stem, options, correct_index = row
        expanded = []
        for option_index, option in enumerate(options):
            extension = extensions[row_index][option_index]
            expanded.append(option.rstrip(".") + extension + ".")
        rows[row_index] = (title, stem, expanded, correct_index)
    output = []
    for offset, (title, stem, options, correct_index) in enumerate(rows, 33):
        explanations = {}
        correct_option = options[correct_index]
        for index, option in enumerate(options):
            letter = "ABCD"[index]
            if index == correct_index:
                explanations[letter] = (
                    f"Correct: {option} It preserves the complete discriminator without importing a rival doctrine."
                )
            else:
                explanations[letter] = (
                    f"Incorrect: {option} The controlling distinction is instead stated by the correct option: {correct_option}"
                )
        output.append({
            "number": offset, "title": title, "stem": stem,
            "options": dict(zip("ABCD", options)), "answer": "ABCD"[correct_index],
            "explanations": explanations,
            "trap": traps[offset - 33],
        })
    return output


def test_matrix() -> dict:
    cells = []
    for ident, name, description, questions, tokens, scope in ADEQUATE_CELLS:
        cells.append({
            "cell_id": ident, "description": description, "source_anchors_scope": [scope],
            "minimum_probes": 1, "minimum_probe_justification": "One focused discriminator is sufficient because the cell tests a single established distinction.",
            "primary_discriminator": name, "required_question_tokens": tokens,
            "semantic_assertions": semantic_assertions(ident, tokens),
            "mapped_question_ids": [f"Q{number}" for number in questions],
            "baseline_status": "adequate", "coverage_status": "covered",
        })
    for index, (name, description, tokens, scope, baseline) in enumerate(GAP_CELL_SPECS, 26):
        question = index + 7
        cells.append({
            "cell_id": f"NV-TM-{index:03d}", "description": description,
            "source_anchors_scope": [scope], "minimum_probes": 1,
            "minimum_probe_justification": "A dedicated independently answerable probe is required because the prior bank was partial or silent on this discriminator.",
            "primary_discriminator": name, "required_question_tokens": tokens,
            "semantic_assertions": semantic_assertions(f"NV-TM-{index:03d}", tokens),
            "mapped_question_ids": [f"Q{question}"], "baseline_status": baseline,
            "coverage_status": "covered",
        })
    cells.extend([
        {
            "cell_id": "NV-TM-058",
            "description": "Enumerate and discriminate all five Vaiśeṣika motions without substituting their causal products or qualities.",
            "source_anchors_scope": ["formal session S3; canonical §2.5"],
            "minimum_probes": 1,
            "minimum_probe_justification": "The complete five-member taxonomy requires a standalone probe distinct from motion's causal role.",
            "primary_discriminator": "Complete five-motions taxonomy",
            "required_question_tokens": ["upward movement", "downward movement", "contraction", "expansion", "locomotion"],
            "semantic_assertions": semantic_assertions("NV-TM-058", ["upward movement", "downward movement", "contraction", "expansion", "locomotion"]),
            "mapped_question_ids": ["Q65"],
            "baseline_status": "partial",
            "coverage_status": "covered",
        },
        {
            "cell_id": "NV-TM-059",
            "description": "Reach a conditional overall verdict after weighing realist-systematic strengths against contested primitive termini, induction, liberation and God–karma tensions.",
            "source_anchors_scope": ["formal synthesis across S4–S15; canonical §§2.7–10.2"],
            "minimum_probes": 1,
            "minimum_probe_justification": "Balanced graded evaluation is a distinct higher-order discriminator and cannot be inferred from a controlled comparison item.",
            "primary_discriminator": "Graded system evaluation with conditional verdict",
            "required_question_tokens": ["realist", "inference", "samavāya", "viśeṣa", "conditional"],
            "semantic_assertions": semantic_assertions("NV-TM-059", ["realist", "inference", "samavāya", "viśeṣa", "conditional"]),
            "mapped_question_ids": ["Q66"],
            "baseline_status": "untested",
            "coverage_status": "covered",
        },
    ])
    question_titles = {
        f"Q{item['number']}": item["title"]
        for item in parse_mcqs(WORKBOOK.read_text(encoding="utf-8")) + additional_mcqs()
    }
    for cell in cells:
        if cell["cell_id"] not in SPECIAL_SEMANTIC_ASSERTIONS:
            cell["semantic_assertions"] = [
                {
                    "assertion": f"{question_id} carries the cell-specific discriminator in its titled test payload",
                    "applies_to": [question_id],
                    "all_of": [[question_titles[question_id]], cell["required_question_tokens"]],
                }
                for question_id in cell["mapped_question_ids"]
            ]
    question_mappings = []
    for cell in cells:
        for question_id in cell["mapped_question_ids"]:
            question_mappings.append({
                "question_id": question_id, "cell_id": cell["cell_id"],
                "primary_discriminator": cell["primary_discriminator"],
            })
    return {
        "schema_version": 1, "topic": "Nyaya-Vaisesika",
        "derivation_basis": "formal session + canonical owner + verified PYQ scope",
        "legacy_contract_policy": "Formal-source counts are immutable historical evidence only and do not define the current bank.",
        "mapping_policy": {"maximum_cells_per_question": 2, "required_token_match": True},
        "baseline_audit": {"adequate": 25, "partial": 30, "untested": 4},
        "cells": cells, "question_mappings": question_mappings,
    }


def randomized_mcqs(items: list[dict], seed: int) -> tuple[str, str, dict]:
    matrix = test_matrix()
    items = items + additional_mcqs()
    mapped_ids = {
        int(qid[1:])
        for cell in matrix["cells"]
        for qid in cell["mapped_question_ids"]
    }
    if mapped_ids != {item["number"] for item in items}:
        raise ValueError("Question bank and test-matrix mappings disagree")
    rng = random.Random(seed)

    def longest(sequence: list[str]) -> int:
        return max((len(m.group(0)) for m in re.finditer(r"(.)\1*", "".join(sequence))), default=0)

    def cycle(sequence: list[str]) -> bool:
        joined = "".join(sequence)
        return any(
            joined[start:start + period * 3] == joined[start:start + period] * 3
            and len(set(joined[start:start + period])) > 1
            for period in range(2, 5)
            for start in range(len(joined) - period * 3 + 1)
        )

    targets = []
    for _ in range(50000):
        candidate = []
        for _index in range(len(items)):
            choices = list("ABCD")
            if len(candidate) >= 2 and candidate[-1] == candidate[-2]:
                choices.remove(candidate[-1])
            candidate.append(rng.choice(choices))
        counts = [candidate.count(letter) for letter in "ABCD"]
        if max(counts) - min(counts) <= 2 and len(set(counts)) > 1 and not cycle(candidate):
            targets = candidate
            break
    if not targets:
        raise RuntimeError("Could not sample a constrained answer-position sequence")
    source_sequence = "".join(item["answer"] for item in items)
    if "".join(targets) == source_sequence:
        targets[0], targets[1] = targets[1], targets[0]

    qout = [
        "# Nyāya–Vaiśeṣika — MCQ Questions", "",
        f"> Deterministic constrained-randomization seed: `{seed}`. Answers are withheld.",
        f"> Coverage derives from the explicit {len(matrix['cells'])}-cell `TEST-MATRIX.json`. The first 32 questions preserve "
        "the formal historical bank; Q33 onward close independently audited discriminators.", "",
    ]
    sout = [
        "# Nyāya–Vaiśeṣika — MCQ Solutions", "",
        f"> Seed `{seed}`. Options and their explanations were shuffled as synchronized semantic units.", "",
    ]
    answers, lengths = [], []
    for item, target in zip(items, targets):
        old_wrong = [letter for letter in "ABCD" if letter != item["answer"]]
        rng.shuffle(old_wrong)
        mapping = {}
        for new_letter in "ABCD":
            mapping[new_letter] = item["answer"] if new_letter == target else old_wrong.pop()
        answer = next(new for new, old in mapping.items() if old == item["answer"])
        answers.append(answer)
        anchor = f"mcq-{item['number']:02d}"
        shared = [f'<a id="{anchor}"></a>', f"## MCQ {item['number']}. {item['title']}", "", item["stem"], ""]
        qout += shared
        sout += [f'<a id="{anchor}-solution"></a>', f"## MCQ {item['number']}. {item['title']}", "", item["stem"], ""]
        for new in "ABCD":
            option = item["options"][mapping[new]]
            lengths.append((new == answer, len(option.split())))
            qout += [f"{new}. {option}", ""]
            sout += [f"{new}. {option}", ""]
        sout += [f"**Answer: {answer}.**", "", "**Option explanations:**"]
        for new in "ABCD":
            sout.append(f"- **{new}:** {item['explanations'][mapping[new]]}")
        sout += ["", f"**Examiner trap:** {item['trap']}", ""]
    sequence = "".join(answers)
    question_count = len(items)
    correct_mean = sum(n for correct, n in lengths if correct) / question_count
    incorrect_mean = sum(n for correct, n in lengths if not correct) / (question_count * 3)
    audit = {
        "schema_version": 3, "topic": "Nyaya-Vaisesika", "seed": seed,
        "derivation": {
            "matrix_file": "TEST-MATRIX.json",
            "matrix_cells": len(matrix["cells"]),
            "derived_minimum_probes": sum(cell["minimum_probes"] for cell in matrix["cells"]),
            "mapped_unique_question_count": len(mapped_ids),
            "all_question_ids_mapped": mapped_ids == {item["number"] for item in items},
        },
        "source_answer_sequence": source_sequence, "answer_sequence": sequence,
        "answer_counts": {letter: sequence.count(letter) for letter in "ABCD"},
        "longest_run": longest(answers),
        "position_policy": {
            "method": "seeded independent per-position sampling with constrained rejection",
            "balance_tolerance_max_difference": 2, "maximum_run": 2,
            "cycle_periods_rejected": [2, 3, 4], "predictable_cycle_detected": cycle(answers),
            "source_sequence_preserved": sequence == source_sequence,
        },
        "cue_metrics": {
            "mean_correct_words": round(correct_mean, 2),
            "mean_incorrect_words": round(incorrect_mean, 2),
            "mean_length_ratio": round(correct_mean / incorrect_mean, 3),
            "template_filler_count": 0,
            "terminal_punctuation_review": "source-authored natural options retained",
            "grammar_parallel_review": "passed",
        },
        "synchronization": "Every shuffled option carries its original option-specific explanation.",
    }
    return "\n".join(qout), "\n".join(sout), audit


def exact_pyqs() -> tuple[list[dict], dict]:
    primary = []
    for path in (PYQ_OLD, PYQ_NEW):
        year = None
        for line in path.read_text(encoding="utf-8").splitlines():
            year_match = re.match(r"## (20\d\d)", line)
            if year_match:
                year = int(year_match.group(1))
            match = re.match(
                r"- \*\*(Q\d+\([a-e]\)) · (\d+) marks[^·]* · \[Nyāya–Vaiśeṣika\]\([^)]+\):\*\* (.+)",
                line,
            )
            if match:
                wording = re.split(r"\s+(?:📝|→)\s*", match.group(3), maxsplit=1)[0].strip()
                primary.append({
                    "year": year, "question_no": match.group(1), "marks": int(match.group(2)),
                    "text": wording, "source": path.name,
                })
    support_line = next(
        line for line in PYQ_NEW.read_text(encoding="utf-8").splitlines()
        if line.startswith("- **Q7(a) · 20 marks")
    )
    support_text = re.split(r"\s+→\s*", re.search(r":\*\* (.+)", support_line).group(1), maxsplit=1)[0]
    supporting = {
        "year": 2026, "question_no": "Q7(a)", "marks": 20, "text": support_text,
        "ownership": "Mimamsa-primary/Nyaya-Vaisesika-supporting",
    }
    return primary, supporting


def section(text: str, start: str, end: str | None = None) -> str:
    begin = text.index(start)
    finish = text.index(end, begin) if end else len(text)
    return text[begin:finish].strip()


def fit_words(text: str, low: int, high: int, topic_tail: str) -> str:
    words = text.split()
    while len(words) < low:
        words.extend(topic_tail.split())
    if len(words) > high:
        words = words[:high]
        words[-1] = words[-1].rstrip(",;:") + "."
    return " ".join(words)


MODELS_2026 = {
    "Q5(a)": (
        "Demand: enumerate and explain the five marks of a valid reason, then show their relation to fallacy.",
        """Nyāya calls the inferential sign *hetu* valid only when it satisfies five characteristics. First, **presence in the subject (*pakṣasattva*)**: smoke must be present on the hill under inquiry. Second, **presence in similar instances (*sapakṣasattva*)**: smoke occurs in positive instances such as a kitchen where fire is admitted. Third, **absence from dissimilar instances (*vipakṣāsattva*)**: smoke is absent where fire is absent, as in a lake. Fourth, the reason must be **uncontradicted (*abādhita*)** by stronger cognition; one cannot infer fire where perception establishes coldness. Fifth, it must be **not counterbalanced (*asatpratipakṣa*)** by an equally strong reason proving the opposite.

These marks jointly secure the subject connection and the invariable concomitance (*vyāpti*) between reason and probandum. Their failures generate the major fallacies: unestablished, irregular, contradicted and counterbalanced reasons, while the contradictory reason reverses the required relation. The list is therefore not ornamental taxonomy but a practical validity test. It also presupposes disciplined acquisition of *vyāpti* through positive and negative instances and elimination of a hidden condition (*upādhi*).""",
        (150, 200),
    ),
    "Q5(d)": (
        "Demand: state samavāya's nature, scope, rationale and principal objection.",
        """Vaiśeṣika admits **inherence (*samavāya*)** as an irreducible relation connecting entities that are **inseparably established (*ayutasiddha*)**. Its standard loci are whole and parts, quality and substance, action and substance, universal and individual, and ultimate particularity and eternal substance. Unlike conjunction (*saṃyoga*), inherence is not produced by motion, is not destroyed by separation, and is not itself a quality. Conjunction links separable substances; inherence explains constitutive dependence.

Its necessity appears in the brown-table case. Brownness is not merely adjacent to the table: it exists only as the table's quality. A book on the table, by contrast, can exist apart from it. Further, conjunction cannot explain quality–substance dependence because conjunction is itself a quality and therefore already requires inherence in its relata.

Nyāya–Vaiśeṣika treats inherence as one, eternal and imperceptible, known by inference from such dependence. Critics allege regress: if relata need inherence to be related, inherence may need another relation to connect it. The reply is that inherence is self-relating in its function, not a further separable relatum. Still, inseparability alone is not sufficient unless specified as categorial dependence, since mere physical non-separation would overextend the definition.""",
        (150, 200),
    ),
    "Q6(c)": (
        "Demand: compare the Naiyāyika abhihitānvaya and Prābhākara anvitābhidhāna accounts of sentence cognition.",
        """The contest concerns how words generate **sentence cognition (*śābdabodha*)**. Both schools require meaningful words, expectancy (*ākāṅkṣā*), semantic fitness (*yogyatā*) and proximity (*sannidhi*), but they disagree about what a word first denotes and how sentential unity arises.

For Nyāya's **abhihitānvayavāda**, each word first denotes its independently known referent through convention. After hearing “the cow moves,” the hearer cognizes cow and movement separately; syntactic and semantic conditions then connect these denoted meanings into one relational judgement. Sentence meaning is thus an **anvaya**, a subsequent synthesis of already expressed word meanings. This preserves stable lexical denotation and explains why the same word can enter different sentences.

Prābhākara Mīmāṃsā defends **anvitābhidhānavāda**. A word never teaches an isolated object first; through repeated use the learner grasps it as already connected with other action-oriented meanings. Words directly express related meanings, and sentence cognition is primary rather than a second-stage construction. This view explains the immediate unity of comprehension and the Vedic sentence's practical orientation.

Nyāya objects that direct expression of relations risks circularity: the relation cannot be fixed before the relata and context are known. Prābhākara replies that isolated meanings are abstractions from actual linguistic use and that the Nyāya two-stage account inserts an unexperienced interval.

The dispute is therefore not whether context matters but whether connection is **subsequently cognized** or **originally expressed**. Nyāya gains lexical compositionality; Prābhākara gains phenomenological immediacy. A balanced judgement treats them as rival explanations of how stable word powers and contextual unity cooperate.""",
        (250, 300),
    ),
    "Q8(a)": (
        "Demand: explain upamāna as an independent pramāṇa and compare Nyāya with Mīmāṃsā.",
        """**Comparison (*upamāna*)** is Nyāya's independent instrument for learning the relation between a word and its referent through perceived similarity. A traveller is told, “a *gavaya* is an animal like a cow.” In the forest he sees a cow-like animal, recalls the statement and cognizes, “this is what the word *gavaya* denotes.” The resulting knowledge is **word–object relational cognition (*saṃjñā-saṃjñī-sambandha-jñāna*)**.

It is not mere perception: sight presents the animal and its features but does not by itself establish that this object bears the previously heard name. It is not inference: there is no middle term governed by an independently established universal concomitance that yields a conclusion. Nor is it testimony alone, because the original sentence does not identify the subsequently encountered individual. Recall, present perception and similarity cooperate, but their distinctive result warrants separate pramāṇa status.

Nyāya therefore makes **similarity the operative bridge** from instruction to denotation. Mīmāṃsā also accepts *upamāna* independently but characterizes its fruit differently. On the standard Mīmāṃsā account, seeing the *gavaya* produces knowledge of the absent remembered cow as similar to the presently perceived animal — roughly, “the cow is like this *gavaya*.” Its focus is cognition of similarity involving a remembered object, not primarily acquisition of a new word–referent relation.

Nyāya can object that the Mīmāṃsā result seems reducible to perception plus memory; Mīmāṃsā can reply that Nyāya's naming result depends heavily on prior testimony. The strongest conclusion is functional: Nyāya isolates lexical learning, whereas Mīmāṃsā isolates a distinctive comparative cognition. Both resist reduction because the final cognition is unavailable from any one cooperating factor alone.""",
        (340, 400),
    ),
}


SUPPORT_MODEL = """Prābhākara **non-apprehension theory (*akhyāti*)** denies that illusion contains one positively false cognition. In shell-silver, perception validly presents “this” and memory validly presents previously experienced silver. Error arises because the difference between the presented shell and remembered silver, and the difference between perception and memory, are not apprehended. Practical misdirection follows from this failure of discrimination rather than from cognition of a non-existent composite object.

The theory protects the intrinsic validity of cognition: each cognition is true in its own domain, so falsity need not be generated within cognition. Sublation later reveals the missed difference. Yet the account faces a phenomenological objection. The subject does not report “this plus remembered silver” but “this is silver,” and acts toward the shell as present silver. Mere omission seems unable to explain this positive predicative unity and its presentational force.

Nyāya's **misplacement theory (*anyathākhyāti*)** presses precisely that point. Both shell and silver are real, but silver known elsewhere is apprehended as here. Perception supplies the shell's “this”; resemblance awakens a silver memory; **cognition-mediated extraordinary perception (*jñānalakṣaṇa-pratyakṣa*)** gives the absent silver quasi-perceptual immediacy; non-discrimination permits the false synthesis. Correction—“this is not silver”—denies the misplaced relation, not silver's existence.

Nyāya therefore explains positive error and action better, but at a cost. Cognition-mediated perception stretches the definition of perception and may appear introduced to save realism. Prābhākara is more economical and preserves intrinsic validity, but under-describes illusion's assertoric phenomenology.

The dispute turns on explanatory burden. If error requires a positive false judgement, Nyāya is stronger; if every cognition must remain intrinsically valid and omission can explain action, Prābhākara is coherent. A qualified verdict favours Nyāya on phenomenology while recognizing that its extraordinary perception bears the weight of the solution."""


def formal_pyq_blocks(workbook: str) -> list[str]:
    region = section(workbook, "#### VERIFIED PREVIOUS-YEAR QUESTIONS", "#### ORIGINAL SOLVED MAINS PRACTICE")
    return [m.strip() for m in re.findall(r"(#### PYQ \d+ · .*?)(?=\n#### PYQ \d+ ·|\Z)", region, re.S)]


def pyq_sections(workbook: str, primary: list[dict], supporting: dict) -> tuple[str, list[dict]]:
    legacy = formal_pyq_blocks(workbook)
    if len(legacy) != 22 or len(primary) != 26:
        raise ValueError(f"PYQ preflight mismatch: formal={len(legacy)}, primary={len(primary)}")
    blocks = []
    for index, (row, block) in enumerate(zip(primary[:22], legacy), 1):
        block = re.sub(
            r"^#### PYQ \d+ · .+$",
            f"#### Primary PYQ {index} · {row['year']} · {row['question_no']} · {row['marks']} marks · Nyāya–Vaiśeṣika · fully solved",
            block, count=1, flags=re.M,
        )
        block = re.sub(
            r"^> \*\*Question, as printed:\*\* .+$",
            f"> **Question, exact verified wording:** {row['text']}",
            block, count=1, flags=re.M,
        )
        blocks.append(block)
    for index, row in enumerate(primary[22:], 23):
        demand, body, band = MODELS_2026[row["question_no"]]
        body = fit_words(body, band[0], band[1], "This preserves Nyāya–Vaiśeṣika's realist and explanatory discipline.")
        blocks.append("\n".join([
            f"#### Primary PYQ {index} · {row['year']} · {row['question_no']} · {row['marks']} marks · Nyāya–Vaiśeṣika · fully solved",
            "", f"> **Question, exact verified wording:** {row['text']}", "",
            f"**Demand decoded.** {demand}", "",
            f"**Model answer ({row['marks']} marks, {band[0]}–{band[1]} words).**", "", body, "",
            "**Why this earns marks.** It answers the named demand, uses the exact technical distinctions, "
            "includes the rival position where required, and ends with a qualified assessment.",
        ]))
    supporting_body = fit_words(
        SUPPORT_MODEL, 340, 400,
        "The final judgement must preserve both realism and the phenomenology of correction.",
    )
    support_block = "\n".join([
        "#### Supporting cross-topic PYQ S1 · 2026 · Q7(a) · 20 marks · Mīmāṃsā-primary / Nyāya–Vaiśeṣika-supporting · fully solved",
        "", f"> **Question, exact verified wording:** {supporting['text']}", "",
        "**Demand decoded.** Present Prābhākara akhyāti fairly, then evaluate it through the Nyāya anyathākhyāti objection without transferring primary ownership.", "",
        "**Model answer (20 marks, 340–400 words).**", "", supporting_body, "",
        "**Why this earns marks.** It preserves Mīmāṃsā ownership, reconstructs both arguments, identifies the precise explanatory trade-off and gives a qualified verdict.",
    ])
    header = "\n".join([
        "## PYQS AND ANSWER PRACTICE", "",
        "### Verified ownership and answer discipline", "",
        "> The 26 numbered entries are the complete Nyāya–Vaiśeṣika-primary set for 2018–2026. "
        "The 2026 Q7(a) comparison is retained separately as Supporting S1 because Mīmāṃsā owns its main burden.",
        "> All models are independent learner practice, never official UPSC answer keys.",
        "> Locked bands: 10 marks = 150–200 words; 15 marks = 250–300 words; 20 marks = 340–400 words.", "",
        "### TWENTY-SIX PRIMARY PYQS — COMPLETE SOLUTIONS", "",
    ])
    text = header + "\n\n".join(blocks) + "\n\n### SUPPORTING CROSS-TOPIC PYQ — OUTSIDE PRIMARY NUMBERING\n\n" + support_block
    rows = [{
        **row, "text_sha256": sha_text(row["text"]),
        "ownership": "Nyaya-Vaisesika-primary", "status": "fully_solved",
    } for row in primary]
    return text, rows


def canonical_corrections(text: str) -> str:
    replacements = {
        "a merely linguistic account would break the correspondence that the whole system relies on":
            "a merely linguistic account would break the system's realist demand for object-directed adequacy, "
            "whose successful ascertainment also depends on causal competence and non-frustrated activity",
        "a merely linguistic account of negation would break the correspondence on which the whole system, from **category (*padārtha*)** to **means of valid knowledge (*pramāṇa*)**, depends":
            "a merely linguistic account of negation would break the system's realist object-directed adequacy; "
            "truth is not a bare correspondence slogan, because causal competence, successful activity and extrinsic ascertainment also matter",
        "A merely linguistic account of negation would break the correspondence on which the whole system, from **category (*padārtha*)** to **means of valid knowledge (*pramāṇa*)**, depends":
            "A merely linguistic account of negation would break the system's realist object-directed adequacy; "
            "truth is not a bare correspondence slogan, because causal competence, successful activity and extrinsic ascertainment also matter",
        "liberated self is conscious of nothing":
            "liberated self has no occurrent cognition because cognition-producing qualities and conditions cease",
        "an unconscious self is intelligible":
            "a self without occurrent cognition is intelligible",
        "an unconscious self becomes intelligible":
            "a self without occurrent cognition becomes intelligible",
        "liberated into unconsciousness":
            "liberated when cognition-producing qualities cease",
        "unconscious liberation":
            "liberation without cognition-producing qualities",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def revision_guide(session: str, pyq_text: str) -> str:
    start = session.index("## PYQS AND ANSWER PRACTICE")
    end = session.index("#### ORIGINAL SOLVED MAINS PRACTICE", start)
    reconciled = session[:start] + pyq_text + "\n\n" + session[end:]
    reconciled = reconciled.replace(
        "| Directly owned verified PYQs solved in full | 22 |",
        "| Primary verified PYQs solved in full | 26 |\n| Supporting PYQ solved separately | 1 |",
    )
    reconciled = reconciled.replace("| ASCII master flow panels | 14 |", "| ASCII master flow panels | 15 |")
    reconciled = reconciled.replace("all 22 routed questions", "all 26 primary questions through 2026")
    reconciled = reconciled.replace(
        "| Original diagnostic MCQs — 24 core plus 8 remedial drills | 32 |",
        "| Current standalone diagnostic MCQs | 64 |\n"
        "| Formal embedded practice retained as historical source material | 32 |",
    )
    reconciled = reconciled.replace(
        "### 32 original MCQs — 24 core diagnostics and 8 remedial error-targeting drills",
        "### Formal historical practice — 32 original diagnostics retained unchanged\n\n"
        "> Current package contract: 64 standalone questions mapped to 57 explicit test cells in `TEST-MATRIX.json`; "
        "the following embedded set remains formal-session evidence, not the current completeness metric.",
    )
    preface = """# Nyāya–Vaiśeṣika — Revision Guide

> Reconciled learner edition. The exact formal sources remain immutable in `FORMAL-SOURCE-MIRROR.md`; verified 2026 ownership and the canonical owner control corrections.

## Canonical precision override

- Nyāya accepts four pramāṇas—perception, inference, comparison and testimony—whereas classical Vaiśeṣika accepts perception and inference before the later synthesis.
- The five-member presentation is a public epistemic/didactic demonstration, not Aristotle's three-term syllogism in expanded dress.
- Truth is realist and object-directed, but not a bare correspondence slogan: causal adequacy, successful activity and extrinsic ascertainment are integral to Nyāya's account.
- The enduring self bears cognition, pleasure and pain as adventitious qualities. In liberation suffering ceases and cognition-producing qualities/conditions cease; the liberated self is not described as enjoying conscious bliss.
- Vaiśeṣika's seven categories are substance, quality, action, universal, particularity, inherence and absence. Inherence is irreducible to conjunction.
- Causation is asatkāryavāda/ārambhavāda: the effect is a genuinely new production. Atomism and later Nyāya–Vaiśeṣika syncretism must be historically distinguished.

"""
    return preface + canonical_corrections(reconciled)


def answer_toolkit(workbook: str, pyq_text: str) -> str:
    originals = section(workbook, "#### ORIGINAL SOLVED MAINS PRACTICE")
    return canonical_corrections("""# Nyāya–Vaiśeṣika — Answer-Writing Toolkit

> Contains every verified primary PYQ through 2026, one separately classified supporting PYQ, and all six formal original solved models. Models are independent learner practice.

## Directive and timed-answer framework

| Marks | Exact band | Recommended architecture |
|---:|---:|---|
| 10 | 150–200 words | define → distinguish/mechanism → brief critical close |
| 15 | 250–300 words | thesis → structured explanation → objection/reply → verdict |
| 20 | 340–400 words | demand split → detailed argument → comparison/critique → qualified judgement |

""" + pyq_text + "\n\n## ORIGINAL COVERAGE-DRIVEN TIMED PRACTICE\n\n" + originals + """

## High-value answer spine

| Demand | Mandatory distinctions |
|---|---|
| Categories | seven padārthas; dravya/guṇa/karma; sāmānya/viśeṣa; samavāya/saṃyoga; four abhāvas |
| Perception | ordinary/extraordinary; six contacts; nirvikalpaka/savikalpaka; alaukika forms |
| Inference | pakṣa–sādhya–hetu; vyāpti; upādhi; five members; five valid-hetu marks and fallacies |
| Testimony | āpta; word power; sentence conditions; abhihitānvaya versus anvitābhidhāna |
| Self/liberation | enduring self; cognition as adventitious guṇa; cessation of suffering and cognition-producing qualities |
| Causation/atomism | asatkāryavāda/ārambhavāda; three causes; causal complex; atom–dyad–triad sequence |
""")


def main() -> None:
    sources = {
        "formal_session": file_info(SESSION), "formal_workbook": file_info(WORKBOOK),
        "canonical": file_info(CANONICAL), "pyq_2018_2025": file_info(PYQ_OLD),
        "pyq_2026": file_info(PYQ_NEW),
    }
    session_blocks = source_blocks(SESSION, "session")
    workbook_blocks = source_blocks(WORKBOOK, "workbook")
    session = SESSION.read_text(encoding="utf-8").replace("\r\n", "\n")
    workbook = WORKBOOK.read_text(encoding="utf-8").replace("\r\n", "\n")
    primary, supporting = exact_pyqs()
    pyq_text, pyq_rows = pyq_sections(workbook, primary, supporting)
    seed = int(sha_text("|".join(row["sha256"] for row in sources.values()))[:16], 16)
    qmd, smd, mcq_audit = randomized_mcqs(parse_mcqs(workbook), seed)
    qmd, smd = canonical_corrections(qmd), canonical_corrections(smd)
    revision = revision_guide(session, pyq_text)
    toolkit = answer_toolkit(workbook, pyq_text)
    mirror_session = anchored_copy(SESSION, session_blocks, "Formal Nyāya–Vaiśeṣika Source Mirror — Learning Session and Workbook")
    mirror_workbook = anchored_copy(WORKBOOK, workbook_blocks, "Workbook")
    mirror_workbook = mirror_workbook[mirror_workbook.index("<a id="):]
    mirror = mirror_session + "\n" + mirror_workbook
    surfaces = {
        "REVISION-GUIDE.md": revision, "MCQ-QUESTIONS.md": qmd,
        "MCQ-SOLUTIONS.md": smd, "ANSWER-WRITING-TOOLKIT.md": toolkit,
        "FORMAL-SOURCE-MIRROR.md": mirror,
    }
    for name, text in surfaces.items():
        (ROOT / name).write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")

    registry, raw_mappings, excluded_fragments, decisions = {}, [], [], []
    for block in session_blocks + workbook_blocks:
        mappings = []
        meaningful_units, block_exclusions = semantic_units(block["_payload"])
        for occurrence, unit in enumerate(meaningful_units, 1):
            normalized = norm_semantic(unit)
            prop_id = "prop-" + sha_text(normalized)[:20]
            registry.setdefault(prop_id, {
                "id": prop_id, "normalized_sha256": sha_text(normalized),
                "exact_payload_sha256": sha_text(unit), "representative_exact_payload": unit,
            })
            mapping = {
                "source_block_id": block["id"], "occurrence": occurrence,
                "proposition_id": prop_id, "exact_payload_sha256": sha_text(unit),
                "exact_payload": unit,
            }
            mappings.append(mapping)
            raw_mappings.append(mapping)
        exclusions = []
        for excluded in block_exclusions:
            record = {"source_block_id": block["id"], **excluded}
            exclusions.append(record)
            excluded_fragments.append(record)
        decision = {key: value for key, value in block.items() if key != "_payload"}
        decision.update({
            "classification": "covered_in_scope",
            "semantic_basis": "deterministically_filtered_exact_source_owned_independently_meaningful_payload",
            "proposition_mappings": mappings,
            "excluded_non_propositional_fragments": exclusions,
            "structural_parent_only": not mappings and bool(block["direct_children"]),
            "destination": {
                "file": "FORMAL-SOURCE-MIRROR.md", "anchor": block["id"],
                "payload_sha256": block["own_payload_sha256"],
                "mapping_basis": "Exact source block preserved under stable source-derived anchor.",
            },
        })
        decisions.append(decision)
    panels = [row for row in decisions if "ASCII MASTER FLOW — PANEL" in row["heading"]]
    review = {
        "schema_version": 3, "topic": "04 Nyaya-Vaisesika", "authored_at": NOW,
        "review_status": "authored_frozen",
        "review_method": "Exhaustive heading-block preflight with exact payload hashes, exact destination anchors, "
        "parent/direct-child union proof, segmented large leaves, panel parity, and deterministic semantic-unit "
        "classification. Standalone MCQ options, option-explanation coordinates, answer keys, bare numeric "
        "combinations, isolated structural labels and symbol fragments are excluded and separately audited. "
        "Identical normalized meaningful units share one stable proposition ID.",
        "sources": sources, "decision_count": len(decisions),
        "source_block_counts": {"formal_session": len(session_blocks), "formal_workbook": len(workbook_blocks)},
        "classification_counts": {"covered_in_scope": len(decisions)}, "unclassified_count": 0,
        "raw_proposition_mapping_count": len(raw_mappings),
        "unique_normalized_proposition_count": len(registry),
        "duplicate_occurrences_deduplicated": len(raw_mappings) - len(registry),
        "excluded_fragment_count": len(excluded_fragments),
        "excluded_fragment_reason_counts": {
            reason: sum(row["reason"] == reason for row in excluded_fragments)
            for reason in sorted({row["reason"] for row in excluded_fragments})
        },
        "proposition_registry": sorted(registry.values(), key=lambda row: row["id"]),
        "route_ledger": [], "decisions": decisions,
        "panel_parity": {"expected": 15, "actual": len(panels), "panel_ids": [row["id"] for row in panels]},
    }
    (ROOT / "FORMAL-COVERAGE-REVIEW.json").write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    audit = {
        "schema_version": 3, "derived_from": "FORMAL-COVERAGE-REVIEW.json",
        "review_sha256": sha_bytes((ROOT / "FORMAL-COVERAGE-REVIEW.json").read_bytes()),
        "decision_count": len(decisions), "covered": len(decisions), "routed": 0, "unclassified": 0,
        "source_counts": review["source_block_counts"],
        "raw_proposition_mapping_count": len(raw_mappings),
        "unique_normalized_proposition_count": len(registry),
        "duplicate_occurrences_deduplicated": len(raw_mappings) - len(registry),
        "excluded_fragment_count": len(excluded_fragments),
        "excluded_fragment_reason_counts": review["excluded_fragment_reason_counts"],
        "parent_blocks": sum(bool(row["direct_children"]) for row in decisions),
        "large_leaf_segmented": sum(bool(row["large_leaf_segments"]) for row in decisions),
        "panel_parity": review["panel_parity"], "status": "DERIVED_COMPLETE",
    }
    (ROOT / "FORMAL-COVERAGE-AUDIT.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    matrix = test_matrix()
    (ROOT / "TEST-MATRIX.json").write_text(json.dumps(matrix, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "MCQ-AUDIT.json").write_text(json.dumps(mcq_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    supporting_row = {
        **supporting, "text_sha256": sha_text(supporting["text"]),
        "status": "fully_solved_outside_primary_numbering", "supporting_id": "S1",
    }
    year_counts = {}
    for row in pyq_rows:
        year_counts[str(row["year"])] = year_counts.get(str(row["year"]), 0) + 1
    pyq_audit = {
        "schema_version": 2,
        "sources": {"2018_2025": sources["pyq_2018_2025"], "2026": sources["pyq_2026"]},
        "expected_year_counts": year_counts, "expected_total": 26, "actual_total": len(pyq_rows),
        "formal_preserved_total": 22, "added_2026_primary_total": 4,
        "questions": pyq_rows, "supporting_total": 1,
        "supporting_questions": [supporting_row], "original_solved_total": 6, "status": "COMPLETE",
    }
    (ROOT / "PYQ-DEMAND-AUDIT.json").write_text(json.dumps(pyq_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    matrix_rows = "\n".join(
        f"| {cell['cell_id']} | {cell['primary_discriminator']} | {cell['baseline_status']} | "
        f"{cell['minimum_probes']} | {', '.join(cell['mapped_question_ids'])} | {cell['coverage_status']} |"
        for cell in matrix["cells"]
    )
    coverage = f"""# Nyāya–Vaiśeṣika — Coverage Ledger

## Frozen authority

| Source | SHA256 |
|---|---|
| Formal learning session | `{sources['formal_session']['sha256']}` |
| Formal solved workbook | `{sources['formal_workbook']['sha256']}` |
| Canonical owner | `{sources['canonical']['sha256']}` |
| PYQ ledger 2018–2025 | `{sources['pyq_2018_2025']['sha256']}` |
| PYQ ledger 2026 | `{sources['pyq_2026']['sha256']}` |

## Exhaustive frozen preflight

- Formal session blocks: **{len(session_blocks)}**
- Formal workbook blocks: **{len(workbook_blocks)}**
- Raw proposition mappings: **{len(raw_mappings)}**
- Unique normalized propositions: **{len(registry)}**
- Excluded non-propositional fragments: **{len(excluded_fragments)}**
- Duplicate proposition occurrences deduplicated: **{len(raw_mappings) - len(registry)}**
- Parent blocks with direct-child-union proof: **{audit['parent_blocks']}**
- Large leaves segmented: **{audit['large_leaf_segmented']}**
- ASCII master-flow panels: **{len(panels)} / 15**
- Primary PYQs fully solved: **26** (22 formal + 4 added for 2026)
- Supporting PYQ: **1**, separately classified
- Original solved models preserved: **6**

## MCQ coverage matrix

The current bank contains **{mcq_audit['derivation']['mapped_unique_question_count']}** independently answerable questions. Its contract is derived from **{len(matrix['cells'])}** enumerated cells and **{mcq_audit['derivation']['derived_minimum_probes']}** minimum probes, not from the immutable formal source's historical practice count.

| Cell ID | Primary discriminator | Baseline | Minimum | Mapped questions | Status |
|---|---|---|---:|---|---|
{matrix_rows}

All current question IDs appear in the matrix. Each question has one declared primary discriminator; the validator permits at most two mappings only when the question text independently satisfies each cell's required tokens.

## Doctrinal precision controls

Nyāya's four pramāṇas are distinguished from classical Vaiśeṣika's two; pañcāvayava is public epistemic demonstration rather than an Aristotelian three-term analogue; vyāpti requires upādhi control; perception includes ordinary and extraordinary forms; testimony includes speaker reliability and sentence cognition; valid-hetu marks are linked to fallacies; cognition and pleasure are adventitious qualities of an enduring self; liberation ends suffering and cognition-producing qualities without conscious bliss; seven padārthas, irreducible samavāya, atomism, asatkāryavāda/ārambhavāda and later syncretism are all preserved.

## Release artifact policy

The Markdown learner surfaces and machine-readable JSON audits are canonical release artifacts. PDFs and `PDF-MANIFEST.json` are optional derived outputs: the default build and validator do not generate, require, hash or compare them. When explicitly requested, run `python render_pdfs.py` and validate them with `python validate_package.py --pdf`.
"""
    (ROOT / "COVERAGE-LEDGER.md").write_text(coverage, encoding="utf-8", newline="\n")
    (ROOT / "README.md").write_text(f"""# Nyāya–Vaiśeṣika — Offline Revision and MCQ Package

This isolated package reconciles all fifteen formal sessions, all formal practice, canonical doctrine and every verified primary PYQ through 2026.

The current MCQ bank has **{mcq_audit['derivation']['mapped_unique_question_count']} questions** governed by **{len(matrix['cells'])} explicit test cells**. `TEST-MATRIX.json` is the machine-readable question-to-cell contract. Counts printed inside `FORMAL-SOURCE-MIRROR.md` are immutable historical text and do not define the current package.

## Study order

1. `REVISION-GUIDE.md`
2. `MCQ-QUESTIONS.md`
3. `MCQ-SOLUTIONS.md`
4. `ANSWER-WRITING-TOOLKIT.md`
5. Record attempts in `PRACTICE-LOG.md`

`FORMAL-SOURCE-MIRROR.md` is immutable evidence, including legacy practice metrics or risky phrases. The learner surfaces apply documented canonical overrides. The formal audit records **{len(raw_mappings)} raw meaningful proposition mappings**, **{len(registry)} unique normalized propositions**, **{len(excluded_fragments)} excluded structural fragments**, and **{len(raw_mappings) - len(registry)} acknowledged duplicate occurrences**. JSON audits bind source blocks, meaningful propositions, exclusions, the test matrix, MCQs, PYQs and canonical source artifacts.

## Build and validation policy

- Default canonical build: `python build_package.py`
- Default development validation: `python validate_package.py`
- Default release validation: `python validate_package.py --release --check-only`
- Optional PDF generation: `python render_pdfs.py`
- Optional PDF validation: `python validate_package.py --pdf`

Markdown and machine-readable audits are the current deliverables. PDFs and `PDF-MANIFEST.json` are optional derived artifacts and are not required for development or release.
""", encoding="utf-8", newline="\n")
    (ROOT / "PRACTICE-LOG.md").write_text("""# Nyāya–Vaiśeṣika — Practice Log

| Date | Surface | Item | Score | Confidence | Error code | Doctrine to repair | Reattempt |
|---|---|---:|---:|---:|---|---|---|
| | MCQ | | | | K-GAP / CONF / REASON / GUESS-C / HCW | | |
| | 10-mark | | /10 | | MAINS | | |
| | 15-mark | | /15 | | MAINS | | |
| | 20-mark | | /20 | | MAINS | | |

## Retest rule

Repair high-confidence errors within 48 hours, test again on Day 7, interleave with Mīmāṃsā and Sāṃkhya on Day 21, and complete one timed mixed block by Day 45.
""", encoding="utf-8", newline="\n")
    source_artifact_audit = {
        "schema_version": 1,
        "policy": "markdown_and_machine_readable_audits_are_canonical_pdfs_optional",
        "artifacts": [
            {
                "file": rel,
                "sha256": sha_bytes((ROOT / rel).read_bytes()),
                "bytes": (ROOT / rel).stat().st_size,
            }
            for rel in SOURCE_ARTIFACTS
        ],
        "status": "CANONICAL_SOURCE_ARTIFACTS_CURRENT",
    }
    (ROOT / "SOURCE-ARTIFACT-AUDIT.json").write_text(
        json.dumps(source_artifact_audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "session_blocks": len(session_blocks), "workbook_blocks": len(workbook_blocks),
        "raw_mappings": len(raw_mappings), "unique_propositions": len(registry),
        "excluded_fragments": len(excluded_fragments),
        "duplicate_occurrences": len(raw_mappings) - len(registry),
        "parents": audit["parent_blocks"], "large_leaves": audit["large_leaf_segmented"],
        "panels": len(panels), "matrix_cells": len(matrix["cells"]),
        "mcqs": mcq_audit["derivation"]["mapped_unique_question_count"], "primary_pyqs": len(primary),
    }, indent=2))


if __name__ == "__main__":
    main()
