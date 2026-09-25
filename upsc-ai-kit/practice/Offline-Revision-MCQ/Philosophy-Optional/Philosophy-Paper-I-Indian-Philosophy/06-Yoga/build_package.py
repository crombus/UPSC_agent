from __future__ import annotations

import hashlib
import json
import re
import shutil
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOW = "2026-09-24T22:41:48+05:30"

SOURCES = {
    "formal_session": Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\06-Yoga\Learning-Session.md"),
    "formal_workbook": Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\06-Yoga\Solved-Practice-Workbook.md"),
    "canonical": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\indian\Yoga.md"),
    "supplementary_complete": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\_learning-sessions\06_Yoga-Complete-Learning-Session.md"),
    "supplementary_layered": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\Indian-Philosophy\learning-sessions\Yoga\Yoga_Layered-Complete-Learning-Session_2026-08-18.md"),
    "supplementary_workbook": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\Indian-Philosophy\learning-sessions\Yoga\Yoga_Layered-Solved-Practice-Workbook_2026-08-18.md"),
    "pyq_2018_2025": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2018-2025.md"),
    "pyq_2026": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2026.md"),
}

EXPECTED_SOURCE_IDENTITIES = {
    "formal_session": {"sha256": "888ce731bfcccc8045ebe94614e682e237b954792d881797d04316ab239be36b", "lines": 5608, "blocks": 311},
    "formal_workbook": {"sha256": "d4ab2ab7fa5d205c806ed56fb29adc4713cd1f8bdc9a366c020457ebcc10fcad", "lines": 1166, "blocks": 53},
}

SNAPSHOT_NAMES = {
    "formal_session": "formal-Learning-Session.md",
    "formal_workbook": "formal-Solved-Practice-Workbook.md",
    "canonical": "canonical-Yoga.md",
    "supplementary_complete": "supplementary-complete-session.md",
    "supplementary_layered": "supplementary-layered-session.md",
    "supplementary_workbook": "supplementary-solved-workbook.md",
    "pyq_2018_2025": "pyq-2018-2025.md",
    "pyq_2026": "pyq-2026.md",
}

ARTIFACTS = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
    "COVERAGE-LEDGER.md", "FORMAL-COVERAGE-AUDIT.json", "FORMAL-COVERAGE-REVIEW.json",
    "SOURCE-PROPOSITION-INVENTORY.json", "TESTABLE-OBLIGATIONS.json", "TEST-MATRIX.json",
    "MCQ-AUDIT.json", "PYQ-DEMAND-AUDIT.json", "PRACTICE-LOG.md",
    "ANSWER-WRITING-TOOLKIT.md", "FORMAL-SOURCE-MIRROR.md",
    *[f"source-snapshots/{name}" for name in SNAPSHOT_NAMES.values()],
    "SOURCE-REGISTRY.json",
    "build_package.py", "validate_package.py", "run_negative_tests.py", "render_pdfs.py", ".gitattributes",
]


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


def file_info(path: Path) -> dict:
    return {"path": str(path), "sha256": sha_bytes(path.read_bytes()), "bytes": path.stat().st_size}


def load_primary_authority() -> dict:
    return json.loads((ROOT / "PRIMARY-SOURCE-AUTHORITY.json").read_text(encoding="utf-8"))


def source_artifact_paths(primary_authority: dict) -> list[str]:
    return ARTIFACTS + [
        "PRIMARY-SOURCE-AUTHORITY.json",
        primary_authority["raw_object"]["path"],
        primary_authority["snapshot"]["path"],
    ]


def heading_blocks(path: Path, prefix: str) -> list[dict]:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    heads = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{2,4})\s+(.+?)\s*$", line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))
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
        s = line.strip()
        if s.startswith("```"):
            flush()
            excluded.append({"exact_payload": line, "reason": "fence_coordinate"})
            in_code = not in_code
            continue
        if in_code:
            flush()
            emit(s, allow_label=True)
            continue
        if not s:
            flush()
            continue
        if re.match(r"^#{1,6}\s+", s):
            flush()
            excluded.append({"exact_payload": line, "reason": "heading_coordinate"})
            continue
        if s.startswith("|"):
            flush()
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c or "") for c in cells):
                excluded.append({"exact_payload": line, "reason": "table_separator"})
            else:
                emit(" | ".join(cells), allow_label=True)
            continue
        if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", line):
            flush()
            pending.append(s)
            continue
        reason = structural_reason(s)
        if reason:
            flush()
            excluded.append({"exact_payload": s, "reason": reason})
        else:
            # Indented, hard-wrapped, numbered-list, and arrow-chain continuations
            # belong to the preceding semantic unit until a real boundary occurs.
            pending.append(s)
    flush()
    return units, [
        {"source_ordinal": i, "reason": item["reason"], "exact_payload_sha256": sha_text(item["exact_payload"]),
         "exact_payload": item["exact_payload"]}
        for i, item in enumerate(excluded, 1)
    ]


def extract_panels(path: Path, prefix: str) -> list[dict]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    panels = []
    for i, m in enumerate(re.finditer(r"```[^\n]*\n.*?\n```", text, re.S), 1):
        payload = m.group(0)
        panels.append({"id": f"{prefix}-diagram-{i:03d}-{sha_text(payload)[:10]}", "kind": "diagram",
                       "payload_sha256": sha_text(payload), "chars": len(payload), "_payload": payload})
    for i, m in enumerate(re.finditer(r"(?m)(?:^\|.*\|\n){2,}", text), 1):
        payload = m.group(0).rstrip() + "\n"
        panels.append({"id": f"{prefix}-table-{i:03d}-{sha_text(payload)[:10]}", "kind": "table",
                       "payload_sha256": sha_text(payload), "chars": len(payload), "_payload": payload})
    return panels


def anchored_source(path: Path, blocks: list[dict]) -> str:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    by_line = {row["line_start"]: row["id"] for row in blocks}
    out = []
    for n, line in enumerate(lines, 1):
        if n in by_line:
            out.append(f'<a id="{by_line[n]}"></a>')
        out.append(line)
    return "\n".join(out) + "\n"


SUPPLEMENTARY_SELECTORS = [
    ("supplementary_complete", "CURRENT LINKAGE - PUBLIC YOGA"),
    ("supplementary_layered", "Advanced reflection problem"),
    ("supplementary_layered", "Advanced transformation and continuity"),
    ("supplementary_layered", "Advanced moral psychology"),
    ("supplementary_layered", "Advanced interpretive control"),
    ("supplementary_layered", "Advanced necessity and redundancy"),
    ("supplementary_layered", "Advanced realist and interaction debates"),
    ("supplementary_layered", "Advanced system assessment"),
    ("supplementary_workbook", "Workbook Use Guide"),
]


PYQS = [
    (2019, "Q7(b)", 15, "How would Yoga philosophy comprehend the Citta-levels of a Scientist, a God-realized Devotee and a Self-realized Yogi? Justify your answer.", "citta_levels"),
    (2020, "Q5(b)", 10, "Explain the difference between Samprajñāta Samādhi and Asamprajñāta Samādhi.", "samadhi_difference"),
    (2021, "Q6(a)", 20, "Explain with reference to Yoga Philosophy, the nature of kleśas. How does the removal of these lead to kaivalya?", "klesa_kaivalya"),
    (2022, "Q5(c)", 10, "Discuss the nature and different stages of Samādhi as per Pātañjala yoga and examine the role of Īśvara in it.", "samadhi_isvara"),
    (2023, "Q7(c)", 15, "Explain Citta and its modifications in the philosophy of Yoga. Why does Yoga philosophy prescribe cessation of modifications of Citta? Give reasons in support of your answer.", "citta_vrtti"),
    (2024, "Q7(b)", 15, "“So long as there are changes and modifications in citta, the self is reflected therein, and, in the absence of discriminative knowledge, identifies itself with them.” Present an appraisal of Yoga Soteriology in the light of the above statement.", "reflection"),
    (2025, "Q7(b)", 15, "Explain the nature of God and its role in Kaivalya in yoga philosophy.", "isvara"),
    (2026, "Q5(e)", 10, "Explain, as per Yoga philosophy, the nature of Samadhi with special reference to the difference between Samprajnata Samadhi and Asamprajnata Samadhi.", "samadhi_2026"),
]

SUPPORTING_PYQS = [
    (2018, "Q6(a)", 20, "How do the Naiyāyikas prove the existence of God? Do the Yoga philosophers prove God in the same way? If yes, how? And if no, why? Give reasons for your answer.",
     "Primary owner: Nyāya–Vaiśeṣika. Yoga is a supporting comparison because its Īśvara is a puruṣa-viśeṣa and contemplative aid, not Nyāya's creator inferred through the same proof-set."),
]

DEMANDS = {
    "citta_levels": "Apply all five citta-bhūmis, justify the three classifications, and distinguish worldly concentration from yogic one-pointedness.",
    "samadhi_difference": "Define both states, identify object-support and saṃskāra-śeṣa, and avoid equating asamprajñāta automatically with nirbīja.",
    "klesa_kaivalya": "Explain five kleśas, four states, karmic causation, attenuation and burning, viveka-khyāti and the transition to kaivalya.",
    "samadhi_isvara": "Give the stages with exact YS 1.17/1.42–44 control and assess Īśvara-praṇidhāna as aid rather than divine grant.",
    "citta_vrtti": "Define citta, enumerate five vṛttis and explain nirodha through reflection, misidentification, abhyāsa and vairāgya.",
    "reflection": "Appraise the complete reflection-based soteriology, including its dualist presupposition, practice, strengths and interaction objection.",
    "isvara": "Define puruṣa-viśeṣa, state untouchedness and teacherhood, explain praṇava and practical role, and deny creator/granter importation.",
    "samadhi_2026": "Explain samādhi and sharply distinguish samprajñāta from asamprajñāta, adding the sabīja/nirbīja and residual-seed qualification.",
}


MODEL_COMPONENTS = {
    "citta_levels": [
        "Yoga treats citta as the sattva-predominant mind-complex of buddhi, ahaṃkāra and manas, not as puruṣa. Vyāsa's commentarial scheme distinguishes kṣipta, mūḍha, vikṣipta, ekāgra and niruddha according to guṇa-dominance and fitness for restraint.",
        "Kṣipta is rajasic dispersion; mūḍha is tamasic torpor; vikṣipta permits intermittent concentration but remains unstable. Ekāgra is sustained one-pointedness, while niruddha is the complete restraint of modifications.",
        "The scientist is best placed in vikṣipta when intense outward inquiry alternates with ordinary distraction and remains attached to empirical ends. Intellectual concentration alone is not yogic integration.",
        "A God-realized devotee is ekāgra because devotion to Īśvara supplies one stable support and subordinates rival impulses. The self-realized yogi is niruddha because the vṛtti-stream has been restrained and discriminative knowledge has matured.",
        "The classification is functional, not a ranking of social worth. A scientist may cultivate ekāgratā, and devotion without stable attention may remain vikṣipta. The answer therefore turns on the actual structure of citta, not occupational labels.",
    ],
    "samadhi_difference": [
        "Samādhi is the culmination of concentrated citta in which the object shines with minimal subjective interference. Samprajñāta samādhi remains cognitively supported: YS 1.17 characterizes it through vitarka, vicāra, ānanda and asmitā, and YS 1.46 calls object-supported absorptions sabīja.",
        "Asamprajñāta samādhi is preceded by practice of cessation. Active cognitive modifications stop, but YS 1.18 explicitly says saṃskāra-śeṣa: residual impressions remain.",
        "Therefore the difference concerns continuing object-cognition versus cessation with latent residue. Asamprajñāta is not sleep, because sleep is itself a vṛtti and lacks disciplined discriminative preparation.",
        "Nor should asamprajñāta be equated without qualification with nirbīja. YS 1.51 calls absorption seedless only when even the residual impression born of truth-bearing insight is restrained.",
    ],
    "klesa_kaivalya": [
        "Yoga diagnoses bondage through five kleśas: avidyā, asmitā, rāga, dveṣa and abhiniveśa. Avidyā mistakes the non-eternal, impure, painful and non-self for their opposites; it is the field from which egoity, attachment, aversion and clinging to life arise.",
        "Each affliction may be prasupta, dormant; tanu, attenuated; vicchinna, interrupted; or udāra, active. Dormancy and temporary suppression are not destruction. Kriyā-yoga—tapas, svādhyāya and Īśvara-praṇidhāna—thins gross affliction, while meditation reaches subtle seeds.",
        "The causal chain is kleśa to karma, saṃskāra and vāsanā, then karmāśaya, vipāka and renewed birth. Fruition shapes jāti, āyus and bhoga. Because ordinary action is coloured by affliction, even apparently successful conduct can replenish the store.",
        "Aṣṭāṅga discipline reorganizes the whole person. Yama and niyama purify motive; posture, breath and sensory withdrawal reduce disturbance; dhāraṇā, dhyāna and samādhi form saṃyama and make citta transparent.",
        "Stable samādhi produces viveka-khyāti, discriminating puruṣa from prakṛti. Para-vairāgya removes attachment even to sattvic knowledge and powers; dharmamegha-samādhi culminates the process. The burnt-seed image means destroyed kleśas retain no capacity to germinate into future bondage.",
        "Kaivalya is consequently not a gift or a newly manufactured state. It is pratiprasava of the guṇas for that puruṣa and svarūpa-pratiṣṭhā, consciousness abiding in its own nature.",
        "A criticism remains: if puruṣa is eternally inactive and pure, bondage seems to belong only to unconscious citta. Yoga replies that bondage is misidentification through reflection, not a real modification of puruṣa, although the relation of two independent principles remains debated.",
    ],
    "samadhi_isvara": [
        "Pātañjala Yoga understands samādhi as progressively purified absorption. Samprajñāta retains an object-support and is characterized in YS 1.17 by vitarka, vicāra, ānanda and asmitā. YS 1.42–44 separately distinguishes savitarkā, nirvitarkā, savicārā and nirvicārā samāpattis; the two lists must not be conflated.",
        "Asamprajñāta follows practice of cessation and leaves saṃskāra as residue. Nirbīja is the further condition in which even that seed is restrained. Ṛtambharā prajñā is truth-bearing yogic perception that blocks lower impressions before its own trace ceases.",
        "Īśvara is puruṣa-viśeṣa, untouched by kleśa, karma, vipāka and āśaya. Meditation on praṇava and Īśvara-praṇidhāna stabilizes attention and counters obstacles.",
        "Yet Īśvara is not the Nyāya creator and does not grant kaivalya by fiat. His role is instrumental: an unsurpassed teacher, model and contemplative support; discriminative realization remains indispensable.",
    ],
    "citta_vrtti": [
        "Citta is Yoga's unified internal instrument comprising buddhi, ahaṃkāra and manas. It is prakṛtic and insentient, yet its sattva-predominance lets it reflect puruṣa and take the form of objects.",
        "Its five vṛttis are pramāṇa, viparyaya, vikalpa, nidrā and smṛti. Every type may be kliṣṭa when coloured by affliction or akliṣṭa when it advances discrimination. Even valid cognition remains a modification.",
        "Nirodha is prescribed because the seer mistakes reflected mental forms for its own states: 'I know', 'I desire' and 'I suffer'. Restraint therefore reveals rather than destroys consciousness.",
        "Abhyāsa supplies continuous stabilization, while vairāgya withdraws thirst for seen and promised objects. Para-vairāgya finally renounces even guṇic knowledge and meditative attainment.",
        "The doctrine is stronger than suppression psychology: Yoga first substitutes non-afflicted for afflicted cognition and only then stills the therapeutic vṛttis. Its difficulty is explaining how inactive puruṣa and material citta enter the reflection relation.",
    ],
    "reflection": [
        "The statement condenses Yoga's soteriology. Citta is a subtle, sattva-predominant product of prakṛti; puruṣa is changeless consciousness. Citta becomes coloured by objects and illuminated by the witness, like a crystal appearing red beside a flower.",
        "Bondage begins when reflected consciousness is appropriated through asmitā. Changing cognitions, memories, pleasures and fears are then asserted as the self's own states. Avidyā sustains this confusion and generates rāga, dveṣa, abhiniveśa and karma.",
        "Yoga therefore defines itself as citta-vṛtti-nirodha. Abhyāsa and vairāgya steady and detach the mind; kriyā-yoga attenuates afflictions; the eight limbs discipline conduct, body, senses and attention. Samādhi makes citta transparent enough for viveka-khyāti.",
        "The path is gradual rather than annihilative. Akliṣṭa vṛttis oppose afflicted ones; truth-bearing insight leaves a purifying saṃskāra; even this final seed is later restrained. Para-vairāgya prevents attachment to insight and siddhis.",
        "When discrimination is uninterrupted, dharmamegha-samādhi leads to pratiprasava and kaivalya. The guṇas cease functioning for the liberated puruṣa, which abides in its own nature.",
        "The account integrates ethics, habit, attention and liberation with unusual precision. Buddhist momentarism challenges the enduring citta-substrate, Advaita challenges plural puruṣas, and Nyāya questions contentless consciousness.",
        "Its deepest vulnerability is interaction: mere proximity describes but may not fully explain reflection between ontologically distinct principles. Still, as a phenomenology of misidentification and disciplined deconditioning, the model remains powerful.",
    ],
    "isvara": [
        "Yoga defines Īśvara as puruṣa-viśeṣa, a special conscious principle untouched by kleśa, karma, vipāka and āśaya. In him lies the unsurpassed seed of omniscience; being unconditioned by time, he is teacher even of the ancients.",
        "Praṇava, OṂ, designates Īśvara. Repetition with contemplation and Īśvara-praṇidhāna gathers the mind, weakens egoic appropriation and helps remove obstacles to samādhi. The doctrine therefore has an explicitly practical and pedagogic function.",
        "Īśvara also serves as the perfect model of freedom from afflictive and karmic conditioning. Devotion is both a niyama and an independent route conducive to absorption.",
        "However, classical Yoga does not primarily make Īśvara the material cause or Nyāya-style efficient creator. Prakṛti remains the source of evolution. Nor does God distribute kaivalya as an external reward; viveka-khyāti is decisive.",
        "The strength of this limited theism is that it preserves Sāṃkhya ontology while adding devotion, humility and a stable contemplative support. Its weakness is possible redundancy: if discrimination liberates, why posit God?",
        "Yoga replies that an optional but unsurpassed aid need not be the metaphysical cause of liberation. Thus Īśvara is instrumentally powerful without being constitutively necessary to kaivalya.",
    ],
    "samadhi_2026": [
        "Samādhi is the concentrated transparency of citta in which its object becomes dominant and discursiveness subsides. It completes dhāraṇā and dhyāna and is soteriologically valuable because it prepares discriminative knowledge.",
        "Samprajñāta is object-supported cognitive absorption. YS 1.17 names vitarka, vicāra, ānanda and asmitā as its factors. The separate samāpatti analysis distinguishes savitarkā and nirvitarkā for gross objects, and savicārā and nirvicārā for subtle objects.",
        "Asamprajñāta is the 'other' samādhi produced through practice of cessation. No ordinary object-cognition remains, but YS 1.18 retains saṃskāra-śeṣa, a residue of impressions.",
        "Hence asamprajñāta is not sleep and is not automatically identical with nirbīja. Seedless absorption occurs only when even the final purifying saṃskāra is restrained. The distinction prevents temporary blankness from being mistaken for liberation.",
    ],
}

COMMON_SENTENCES = [
    "The doctrinal sequence should always be connected to the final purpose of discriminating the seer from the seen.",
    "This qualification prevents a meditative stage from being mistaken for kaivalya itself.",
    "The strongest answer combines exact classification, causal explanation and one controlled objection.",
    "Yoga's practical vocabulary remains intelligible only within its puruṣa-prakṛti dualism.",
    "Accordingly, the conclusion must distinguish psychological quiet from irreversible soteriological freedom.",
]


def model_text(key: str, marks: int) -> str:
    lo, hi = {10: (150, 200), 15: (250, 300), 20: (340, 400)}[marks]
    parts = list(MODEL_COMPONENTS[key])
    text = "\n\n".join(parts)
    i = 0
    while words(text) < lo:
        text += " " + COMMON_SENTENCES[i % len(COMMON_SENTENCES)]
        i += 1
    if words(text) > hi:
        sentences = re.split(r"(?<=[.!?])\s+", text)
        kept = []
        for sentence in sentences:
            if words(" ".join(kept + [sentence])) <= hi:
                kept.append(sentence)
        text = " ".join(kept)
    assert lo <= words(text) <= hi, (key, marks, words(text))
    return text


ORIGINALS = [
    ("OR-10A", 10, "Distinguish YS 1.17's account of samprajñāta from the samāpatti classification in YS 1.42–1.44.", "samadhi_difference"),
    ("OR-10B", 10, "Explain why siddhis are attainments and yet obstacles in Pātañjala Yoga.", "samadhi_isvara"),
    ("OR-15A", 15, "Analyse abhyāsa, lower vairāgya and para-vairāgya as a graded discipline of nirodha.", "citta_vrtti"),
    ("OR-15B", 15, "Evaluate Yoga's account of Īśvara as a non-creator and non-granter of kaivalya.", "isvara"),
    ("OR-20A", 20, "Critically examine the Yoga account of karma, saṃskāra, vāsanā, karmāśaya and rebirth.", "klesa_kaivalya"),
    ("OR-20B", 20, "Compare Yoga with Buddhist momentariness, Yogācāra, Advaita and Nyāya on mind, self and liberation.", "reflection"),
]


QUESTION_DEFINITION_ROWS = [
    ("identity", "Yoga as citta-vṛtti-nirodha", "Yoga is restraint of citta's modifications so the seer abides in its own nature.", "Yoga is primarily bodily flexibility.", "Yoga is union of an individual soul with a creator.", "Yoga is suppression of consciousness itself."),
    ("texts", "Four pādas and textual ownership", "Samādhi, Sādhana, Vibhūti and Kaivalya are the four pādas of the Yoga Sūtra.", "The four pādas are four kinds of pramāṇa.", "Vyāsa composed a fifth canonical pāda.", "The pādas reproduce the four Vedas."),
    ("boundary", "Samkhya-Yoga boundary", "Yoga borrows the puruṣa-prakṛti bridge but owns citta-discipline and samādhi.", "Yoga owns the exhaustive twenty-five-tattva proof sequence.", "Samkhya owns Yoga's eight-limbed discipline.", "The two systems have unrelated ontologies."),
    ("citta", "Citta constitution", "Citta functionally includes buddhi, ahaṃkāra and manas.", "Citta is identical only with atomic manas.", "Citta is a fourth independent conscious substance.", "Citta is another name for puruṣa."),
    ("reflection", "Reflective citta", "Citta is insentient but appears conscious by reflecting puruṣa.", "Puruṣa becomes materially modified inside citta.", "Objects are produced by the witness's reflection.", "Citta is self-luminous independently of puruṣa."),
    ("misidentification", "Asmitā and bondage", "Bondage arises when the seer is confused with the instrument of seeing.", "Bondage is a real alteration in puruṣa.", "Bondage results only from bodily weakness.", "Bondage is imposed by Īśvara."),
    ("bhumi-k", "Kṣipta", "Kṣipta is the rajasic, scattered condition of citta.", "Kṣipta is the final restrained condition.", "Kṣipta is sattvic one-pointedness.", "Kṣipta is tamasic sleep alone."),
    ("bhumi-m", "Mūḍha", "Mūḍha is the tamasic, dull condition of citta.", "Mūḍha is refined yogic perception.", "Mūḍha is the devotee's one-pointed state.", "Mūḍha is the cessation of all seeds."),
    ("bhumi-v", "Vikṣipta", "Vikṣipta permits intermittent focus but remains unstable.", "Vikṣipta is permanent liberation.", "Vikṣipta means complete sensory withdrawal.", "Vikṣipta is identical with niruddha."),
    ("bhumi-e", "Ekāgra", "Ekāgra is sustained one-pointedness fit for yogic practice.", "Ekāgra is compulsive outward scattering.", "Ekāgra is unconscious torpor.", "Ekāgra abolishes every saṃskāra."),
    ("bhumi-n", "Niruddha", "Niruddha is the condition in which modifications are restrained.", "Niruddha is ordinary intellectual concentration.", "Niruddha is the active expression of kleśas.", "Niruddha is verbal construction."),
    ("vrtti-list", "Five vṛttis", "Pramāṇa, viparyaya, vikalpa, nidrā and smṛti are the five vṛttis.", "Desire, anger, greed, delusion and pride are the five vṛttis.", "Yama, niyama, āsana, prāṇāyāma and pratyāhāra are the five vṛttis.", "Birth, lifespan, experience, action and fruition are the five vṛttis."),
    ("klista", "Kliṣṭa and akliṣṭa", "Any vṛtti-type may bind or aid release according to its afflictive colouring.", "Only false cognition can ever be afflicted.", "Every valid cognition is already liberation.", "Kliṣṭa and akliṣṭa are four states of kleśa."),
    ("pramana", "Three pramāṇas", "Yoga accepts perception, inference and authoritative testimony.", "Yoga accepts perception alone.", "Yoga accepts six independent pramāṇas.", "Yoga rejects inference during ordinary inquiry."),
    ("sleep", "Nidrā", "Sleep is a positive vṛtti grounded in absence-content and evidenced by recollection.", "Sleep is identical with seedless samādhi.", "Sleep destroys every latent impression.", "Sleep is not a mental state at all."),
    ("abhyasa", "Abhyāsa", "Abhyāsa is sustained effort to remain stable in restraint.", "Abhyāsa means devotion without repeated discipline.", "Abhyāsa is attachment to subtle objects.", "Abhyāsa is the fruition of past karma."),
    ("vairagya", "Lower vairāgya", "Lower vairāgya masters thirst for seen and scripturally promised objects.", "Lower vairāgya rejects only painful objects.", "Lower vairāgya is omniscience.", "Lower vairāgya is involution of the guṇas."),
    ("para", "Para-vairāgya", "Para-vairāgya renounces even attachment to guṇas, insight and powers.", "Para-vairāgya seeks increasingly subtle siddhis.", "Para-vairāgya is mere social withdrawal.", "Para-vairāgya is a creator's grace."),
    ("klesa-list", "Five kleśas", "Avidyā, asmitā, rāga, dveṣa and abhiniveśa are the five kleśas.", "Pramāṇa, viparyaya, vikalpa, nidrā and smṛti are the five kleśas.", "Jāti, āyus, bhoga, karma and vipāka are the five kleśas.", "Dhāraṇā, dhyāna, samādhi, prajñā and kaivalya are the five kleśas."),
    ("avidya", "Avidyā", "Avidyā mistakes the non-eternal, impure, painful and non-self for their opposites.", "Avidyā is only absence of textual information.", "Avidyā is identical with memory.", "Avidyā is produced by kaivalya."),
    ("states", "Four kleśa states", "Prasupta, tanu, vicchinna and udāra are the four kleśa states.", "Sabīja, nirbīja, gross and subtle are the four kleśa states.", "Birth, life, experience and death are the four kleśa states.", "Truth, non-violence, purity and contentment are the four kleśa states."),
    ("kriya", "Kriyā-yoga", "Tapas, svādhyāya and Īśvara-praṇidhāna constitute kriyā-yoga.", "Yama, āsana and samādhi constitute kriyā-yoga.", "Inference, testimony and perception constitute kriyā-yoga.", "Rāga, dveṣa and abhiniveśa constitute kriyā-yoga."),
    ("karma-chain", "Karmic chain", "Kleśa-coloured action leaves saṃskāra and karmāśaya that ripen as vipāka and rebirth.", "Vipāka creates an untouched puruṣa.", "Karmāśaya belongs to Īśvara.", "Rebirth occurs without dispositions or action."),
    ("vipaka", "Threefold vipāka", "Vipāka is expressed through birth, lifespan and experience.", "Vipāka is expressed through three pramāṇas.", "Vipāka is expressed through three guṇas only.", "Vipāka is identical with saṃyama."),
    ("karma-types", "Four karma types", "White, black, mixed and neither-white-nor-black distinguish karmic action.", "Gross, subtle, joyful and egoic distinguish karmic action.", "Dormant, attenuated, interrupted and active distinguish karmic action.", "Perception, inference, testimony and absence distinguish karmic action."),
    ("yamas", "Five yamas", "Non-violence, truthfulness, non-stealing, disciplined sexuality and non-possessiveness are yamas.", "Purity, contentment, austerity, study and surrender are yamas.", "Posture, breath, withdrawal, concentration and meditation are yamas.", "Friendliness, compassion, joy, equanimity and faith are yamas."),
    ("niyamas", "Five niyamas", "Purity, contentment, austerity, study and surrender to Īśvara are niyamas.", "Non-violence, truthfulness, non-stealing, chastity and non-possession are niyamas.", "Birth, lifespan, experience, merit and demerit are niyamas.", "Gross, subtle, blissful, egoic and seedless are niyamas."),
    ("pratipaksa", "Pratipakṣa-bhāvana", "Pratipakṣa-bhāvana counters harmful thoughts by cultivating their opposites.", "Pratipakṣa-bhāvana suppresses breath indefinitely.", "Pratipakṣa-bhāvana seeks extraordinary powers.", "Pratipakṣa-bhāvana proves a creator God."),
    ("outer-inner", "Bahiranga and antaranga", "The first five limbs are external relative to dhāraṇā, dhyāna and samādhi.", "Only yama is external and all other limbs are internal.", "All eight limbs are merely physical.", "Samādhi is external while posture is internal."),
    ("pratyahara", "Pratyāhāra", "Pratyāhāra withdraws senses from compulsive dependence on their objects.", "Pratyāhāra destroys the sense capacities.", "Pratyāhāra is identical with inference.", "Pratyāhāra grants kaivalya without meditation."),
    ("samyama", "Saṃyama", "Dhāraṇā, dhyāna and samādhi jointly constitute saṃyama.", "Yama, niyama and āsana jointly constitute saṃyama.", "Tapas, study and surrender jointly constitute saṃyama.", "Perception, inference and testimony jointly constitute saṃyama."),
    ("ys117", "YS 1.17", "Vitarka, vicāra, ānanda and asmitā characterize samprajñāta samādhi.", "Savitarka, nirvitarka, savicāra and nirvicāra are the exact YS 1.17 list.", "Yama, niyama, āsana and breath characterize samprajñāta.", "Prasupta, tanu, vicchinna and udāra characterize samprajñāta."),
    ("samapatti", "YS 1.42–1.44", "Savitarkā/nirvitarkā concern gross objects, while savicārā/nirvicārā concern subtle objects.", "All four terms are states of kleśa.", "All four terms are kinds of moral action.", "All four terms describe the four pādas."),
    ("sabija", "Sabīja", "Sabīja in YS 1.46 means that an object-support remains.", "Sabīja means all karma has been destroyed.", "Sabīja is a synonym for kaivalya.", "Sabīja denotes sleep without dreams."),
    ("asamprajnata", "Asamprajñāta", "Asamprajñāta stops active vṛttis while saṃskāra-śeṣa may remain.", "Asamprajñāta necessarily has a gross object.", "Asamprajñāta is ordinary sleep.", "Asamprajñāta is identical with the first limb."),
    ("nirbija", "Nirbīja", "Nirbīja arises when even the final residual saṃskāra is restrained.", "Nirbīja simply means absence of a gross object.", "Nirbīja retains every afflictive seed.", "Nirbīja is another name for savitarkā."),
    ("two-seeds", "Two meanings of seed", "Sabīja's object-support and nirbīja's residual saṃskāra are distinct senses of seed.", "Both uses mean only a physical seed.", "Both uses mean the creator God.", "The texts never use seed language for samādhi."),
    ("rtambhara", "Ṛtambharā prajñā", "Ṛtambharā is truth-bearing yogic perception arising from nirvicāra clarity.", "Ṛtambharā is a fourth independent pramāṇa.", "Ṛtambharā is verbal construction without an object.", "Ṛtambharā permanently replaces kaivalya."),
    ("routes", "Bhava and upāya routes", "Bhava-pratyaya is condition-based, while upāya-pratyaya uses faith, energy, memory, samādhi and wisdom.", "Both routes are two additional pramāṇas.", "Both routes are creator proofs.", "Both routes are the first two yamas."),
    ("parinamas", "Three citta-pariṇāmas", "Nirodha, samādhi and ekāgratā transformations describe the trained continuity of citta.", "Birth, life and experience are citta-pariṇāmas.", "Gross, subtle and causal bodies are citta-pariṇāmas.", "Three creator acts are citta-pariṇāmas."),
    ("dharmin", "Dharma-lakṣaṇa-avasthā", "Property, temporal character and condition transform in a persisting prakṛtic substrate.", "The three changes occur in immutable puruṣa.", "The doctrine denies all continuity.", "The doctrine is Advaita's apparent transformation."),
    ("siddhi", "Siddhis", "Siddhis may be attainments outwardly yet obstacles when appropriated in samādhi.", "Siddhis are identical with kaivalya.", "Every siddhi proves moral perfection.", "Yoga requires public display of siddhis."),
    ("isvara-def", "Īśvara definition", "Īśvara is a special puruṣa untouched by affliction, action, fruition and deposit.", "Īśvara is the material cause called prakṛti.", "Īśvara is the only puruṣa.", "Īśvara is a momentary cognition."),
    ("pranava", "Praṇava and teacher", "OṂ designates Īśvara, the timeless teacher with unsurpassed omniscience.", "OṂ denotes the twenty-five tattvas collectively.", "Īśvara learns from embodied teachers.", "Praṇava replaces ethical discipline."),
    ("noncreator", "Non-creator control", "Patañjali chiefly presents Īśvara as contemplative support rather than Nyāya's creator.", "Yoga makes Īśvara the material substance of the world.", "Yoga proves God only through atom-combination.", "Yoga treats Īśvara as karmically bound."),
    ("nongranter", "Non-granter control", "Īśvara aids the path but kaivalya depends on discriminative realization.", "Īśvara grants arbitrary liberation irrespective of citta.", "Īśvara absorbs every puruṣa into himself.", "Īśvara replaces viveka-khyāti."),
    ("yogic-perception", "Yogic perception", "Yogic cognition perfects perception and does not add a fourth pramāṇa.", "Yogic cognition is testimony alone.", "Yogic cognition is always conceptual construction.", "Yogic cognition abolishes objects by imagining them."),
    ("samkhya-continuity", "Continuity with Sāṃkhya", "Yoga retains plural puruṣas, prakṛti and real transformation.", "Yoga replaces prakṛti with Brahman.", "Yoga denies all guṇas.", "Yoga accepts only a single self."),
    ("samkhya-difference", "Difference from Sāṃkhya", "Yoga adds systematic citta-discipline, samādhi and Īśvara-praṇidhāna.", "Yoga rejects discrimination as liberating.", "Yoga denies the puruṣa-prakṛti distinction.", "Yoga makes ritual the sole means."),
    ("buddhist", "Buddhist momentariness", "Yoga requires a continuing citta-substrate for saṃskāra and graded practice.", "Yoga accepts only disconnected mental flashes.", "Buddhism and Yoga both affirm an eternal puruṣa.", "Momentariness is Yoga's account of kaivalya."),
    ("yogacara", "Yogācāra comparison", "Yoga defends object, citta and puruṣa as distinct against cognition-only reduction.", "Yoga says objects depend on one private mind.", "Yoga reduces puruṣa to an external object.", "Yoga denies that citta can be known."),
    ("advaita", "Advaita comparison", "Yoga teaches isolation of many puruṣas, not identity with one Brahman.", "Yoga teaches non-dual identity with Brahman.", "Advaita and Yoga share the same creator proof.", "Both deny real change in the mental field."),
    ("nyaya", "Nyāya comparison", "Yoga accepts three pramāṇas and a non-creator special puruṣa; Nyāya accepts four pramāṇas and a creator God.", "Yoga accepts four pramāṇas and a creator special puruṣa; Nyāya accepts three and rejects God.", "Yoga and Nyāya both accept three pramāṇas and treat God only as a contemplative aid.", "Yoga accepts perception alone, whereas Nyāya accepts testimony alone and denies inference."),
    ("dharmamegha", "Dharmamegha", "Dharmamegha-samādhi follows non-attachment even to discriminative knowledge and powers.", "Dharmamegha is an early posture exercise.", "Dharmamegha is a creator's reward.", "Dharmamegha restores afflictive seeds."),
    ("viveka", "Viveka-khyāti", "Viveka-khyāti continuously discriminates puruṣa from prakṛti.", "Viveka-khyāti merges puruṣa into prakṛti.", "Viveka-khyāti is sensory pleasure.", "Viveka-khyāti is ritual merit."),
    ("pratiprasava", "Pratiprasava", "Pratiprasava is the involution of guṇic effects when their purpose for puruṣa is complete.", "Pratiprasava is creation from nothing.", "Pratiprasava is divine forgiveness.", "Pratiprasava is ordinary sleep."),
    ("kaivalya", "Kaivalya", "Kaivalya is isolation and self-abidance of puruṣa, not union or annihilation.", "Kaivalya is merger into Brahman.", "Kaivalya is extinction of consciousness.", "Kaivalya is acquisition of every siddhi."),
    ("crit-interaction", "Interaction criticism", "Mere proximity protects puruṣa from change but leaves a residual explanatory problem.", "Yoga says puruṣa physically pushes prakṛti.", "Yoga denies any relation between experience and citta.", "The criticism is solved by calling citta conscious."),
    ("crit-negative", "Negative liberation criticism", "Svarūpa-pratiṣṭhā supplies Yoga's positive account of liberated self-abidance.", "Yoga concedes that liberation is unconsciousness.", "Yoga defines liberation as bodily immortality.", "Yoga treats suffering as eternally necessary."),
    ("ethics", "Ethical application", "Yama and niyama reduce the afflictive turbulence that can corrupt meditation.", "Ethics becomes unnecessary after learning posture.", "Meditative power guarantees moral purity.", "Yoga permits contextual abandonment of non-violence."),
    ("psychology", "Psychological application", "Yoga links attention, habit, memory and latent disposition in a trainable causal system.", "Yoga rejects all habitual continuity.", "Yoga treats emotion as belonging to puruṣa.", "Yoga limits practice to bodily flexibility."),
    ("pyq2019", "2019 PYQ discriminator", "Functionally, the scientist may be vikṣipta, the one-pointed devotee ekāgra, and the fully restrained yogi niruddha.", "Functionally, the scientist is niruddha, the one-pointed devotee mūḍha, and the restrained yogi merely vikṣipta.", "Functionally, all three are ekāgra because occupational labels alone establish stable one-pointedness and spiritual attainment.", "Functionally, all three are niruddha because intellectual concentration, devotion, and restraint are equivalent final conditions."),
    ("pyq2020", "2020 PYQ discriminator", "Samprajñāta retains cognitive support; asamprajñāta stops it while residual impressions may remain.", "The terms differ only by posture.", "Asamprajñāta is always sleep.", "Samprajñāta is already kaivalya."),
    ("pyq2021", "2021 PYQ discriminator", "Removal of kleśas interrupts karmic fertility and allows discrimination to culminate in kaivalya.", "Kleśas are removed by intellectual information alone.", "Kaivalya requires stronger attachment.", "Karma disappears while kleśas remain active."),
    ("pyq2022", "2022 PYQ discriminator", "Īśvara aids samādhi through surrender and praṇava but does not replace viveka.", "Īśvara grants absorption arbitrarily.", "Īśvara is the gross object in every samādhi.", "Īśvara makes practice unnecessary."),
    ("pyq2023", "2023 PYQ discriminator", "Cessation is prescribed because identification with citta's five modifications sustains bondage.", "Cessation is prescribed because every modification physically alters and eventually destroys puruṣa.", "Cessation is prescribed only for false cognition; valid cognition and memory cannot sustain bondage.", "Cessation is prescribed because memory is external to citta and therefore cannot be disciplined."),
    ("pyq2024", "2024 PYQ discriminator", "Reflection explains apparent bondage without literal modification of puruṣa, though interaction remains contestable.", "Reflection proves puruṣa materially changes.", "Reflection makes citta intrinsically conscious.", "Reflection eliminates the need for practice."),
    ("pyq2025", "2025 PYQ discriminator", "God is a special puruṣa and practical contemplative aid, not the creator or external granter of kaivalya.", "God is prakṛti itself and creates the plurality of puruṣas before granting them liberation.", "God is the sole puruṣa and directly absorbs every finite mind into himself at liberation.", "God is a karmically perfected teacher who attains kaivalya through the same afflictions as practitioners."),
    ("pyq2026", "2026 PYQ discriminator", "The distinction tracks object-support, residual saṃskāra in asamprajñāta, and its further restraint in nirbīja.", "The distinction tracks ethical vows, bodily posture in asamprajñāta, and sensory withdrawal in nirbīja.", "The distinction treats both states as sleep, with nirbīja retaining the stronger residual impressions.", "The distinction places nirbīja before samprajñāta and makes object-support the mark of final liberation."),
]

QUESTION_DEFINITION_ROWS += [
    ("antarayas", "Nine obstacles", "Illness, inertia, doubt, carelessness, laziness, non-abstinence, false perception, failure to attain a stage and instability are the nine obstacles.", "The nine obstacles are identical with the five kleśas and four karma types.", "Only bodily illness counts as an obstacle to Yoga.", "The obstacles disappear merely by knowing their names."),
    ("symptoms", "Four obstacle symptoms", "Pain, despair, bodily unsteadiness and disturbed inhalation-exhalation accompany mental distraction.", "The four symptoms are stages of samprajñāta samādhi.", "They are the four states of avidyā.", "They prove that every breathing exercise is harmful."),
    ("attitudes", "Four social attitudes", "Friendliness, compassion, appreciative joy and equanimity calm citta toward happiness, suffering, virtue and vice.", "The four attitudes replace all eight limbs.", "They are creator proofs rather than affective disciplines.", "Equanimity means indifference to all suffering."),
    ("mahavrata", "Yama as universal great vow", "The yamas are a universal great vow unrestricted by class, place, time or circumstance.", "The yamas bind only renunciants in forests.", "Each yama may be ignored when inconvenient.", "The yamas are merely preparatory postures."),
    ("asana", "Āsana", "Āsana is a steady and easeful posture perfected through relaxation of effort and contemplation of the infinite.", "Āsana is an athletic display requiring strain.", "Āsana alone produces final discriminative knowledge.", "Āsana is identical with sensory withdrawal."),
    ("pranayama", "Prāṇāyāma", "Prāṇāyāma regulates inhalation, exhalation and retention after posture becomes stable.", "Prāṇāyāma abolishes puruṣa through breath retention.", "Prāṇāyāma is one of Yoga's three pramāṇas.", "Prāṇāyāma precedes ethical discipline in the canonical limb order."),
    ("dharana-dhyana", "Dhāraṇā and dhyāna", "Dhāraṇā binds citta to a locus, while dhyāna is the uninterrupted flow of similar cognition toward it.", "Dhāraṇā is effortless liberation and dhyāna is bodily posture.", "Both terms denote the same five moral vows.", "Dhyāna disperses attention among many objects."),
    ("vitarka-badha", "Vitarka-bādhana", "When contrary thoughts obstruct the vows, pratipakṣa-bhāvana recalls their painful consequences and cultivates the opposite disposition.", "Contrary thoughts are strengthened until they exhaust themselves.", "The method proves that moral actions have no consequences.", "The method is restricted to disputes about inference."),
    ("gunas-purpose", "Guṇas and puruṣa-purpose", "The guṇas evolve for experience and liberation, then cease their service when discriminative purpose is fulfilled.", "The guṇas are conscious agents seeking their own liberation.", "Puruṣa is a product of the guṇas.", "Kaivalya requires permanent continuation of guṇic activity for the liberated seer."),
    ("sevenfold-insight", "Yoga Sūtra II.27 sevenfold culminating knowledge", "Yoga Sūtra II.27 characterizes culminating prajñā as reaching a sevenfold highest or final ground.", "The sūtra characterizes culminating knowledge as a single bodily posture.", "The sevenfold ground is identical with the five citta-bhūmis.", "The sūtra makes public display of seven siddhis compulsory."),
    ("dharma-megha-function", "Dharmamegha and karmic exhaustion", "Dharmamegha-samādhi removes the remaining afflictive and karmic covering as discrimination becomes uninterrupted.", "Dharmamegha revives dormant afflictions for further experience.", "Dharmamegha is merely a rain-producing supernatural power.", "Dharmamegha substitutes divine pardon for discriminative knowledge."),
    ("drastr-drshya", "Seer and seen distinction", "Puruṣa is the immutable seer, while citta and its objects belong to the mutable seen.", "Puruṣa is one more changing state of citta.", "Objects are transformations of the immutable seer.", "The seer-seen distinction disappears before discriminative knowledge."),
    ("kaivalya-double", "Kaivalya's double description", "Kaivalya is both the guṇas' cessation of service and consciousness established in its own nature.", "Kaivalya is only the guṇas' physical destruction.", "Kaivalya is absorption of all puruṣas into Īśvara.", "Kaivalya leaves citta permanently active for enjoyment."),
    ("smrti-definition", "Smṛti as non-loss", "Smṛti is the non-loss and re-presentation of a previously experienced object.", "Smṛti is fresh perception without any prior impression.", "Smṛti is the complete restraint of all mental seeds.", "Smṛti belongs to immutable puruṣa rather than citta."),
]

# These supplementary-only teaching points remain in the learner guide but do not become mandatory
# test obligations when no proposition in the 521 mandatory blocks independently supports them.
QUESTION_DEFINITION_ROWS = [
    row for row in QUESTION_DEFINITION_ROWS if row[0] not in {"pratipaksa", "vitarka-badha"}
]


ANSWER_SEED = "Yoga|independent-per-question-position|2026-09-24"
ANSWER_IMBALANCE_MIN_SHARE = 0.10
ANSWER_IMBALANCE_MAX_SHARE = 0.40
ANSWER_CHI_SQUARE_MAX = 11.345
KEYED_MEDIAN_RATIO_THRESHOLD = 3.2
KEYED_SPECIFICITY_DELTA_THRESHOLD = 2


def predictable_cycles(sequence: str) -> list[tuple[int, int, str]]:
    return [(period, start, sequence[start:start + period])
            for period in range(2, 5)
            for start in range(len(sequence) - period * 3 + 1)
            if len(set(sequence[start:start + period])) > 1
            and sequence[start:start + period * 3] == sequence[start:start + period] * 3]


def answer_statistics(sequence: str) -> dict:
    counts = Counter(sequence)
    expected = len(sequence) / 4
    chi_square = sum((counts[letter] - expected) ** 2 / expected for letter in "ABCD")
    return {
        "counts": {letter: counts[letter] for letter in "ABCD"},
        "max_run": max(len(m.group(0)) for m in re.finditer(r"(.)\1*", sequence)),
        "cycles": predictable_cycles(sequence),
        "chi_square": round(chi_square, 6),
        "min_share": min(counts[letter] for letter in "ABCD") / len(sequence),
        "max_share": max(counts[letter] for letter in "ABCD") / len(sequence),
    }


def deterministic_answer_sequence(question_ids: list[str], seed: str = ANSWER_SEED) -> tuple[str, int]:
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


def option_cue_metrics(bank: list[dict]) -> dict:
    rows, length_flags, specificity_flags, lexical_flags, format_flags = [], [], [], [], []
    markers = re.compile(r"\b(?:YS\s*\d|always|never|only|exactly|all|necessarily|immediately)\b", re.I)
    for index, q in enumerate(bank, 1):
        counts = {letter: words(text) for letter, text in q["options"].items()}
        ordered = sorted(counts.values())
        median = (ordered[1] + ordered[2]) / 2
        keyed_count = counts[q["answer"]]
        keyed_median_ratio = max(keyed_count / max(1, median), median / max(1, keyed_count))
        pairwise_ratio = max(ordered) / max(1, min(ordered))
        detail_counts = {letter: len(markers.findall(text)) for letter, text in q["options"].items()}
        keyed_detail_delta = detail_counts[q["answer"]] - max(
            detail_counts[letter] for letter in "ABCD" if letter != q["answer"])
        stem_terms = {x for x in re.findall(r"\b\w{7,}\b", q["stem"].casefold())
                      if x not in {"statement", "accurately", "captures", "doctrine"}}
        overlap = {letter: len(stem_terms & set(re.findall(r"\b\w{7,}\b", text.casefold())))
                   for letter, text in q["options"].items()}
        keyed_lexical_delta = overlap[q["answer"]] - max(
            overlap[letter] for letter in "ABCD" if letter != q["answer"])
        punctuation = {re.sub(r"\w", "", text.strip())[-1:] for text in q["options"].values()}
        if keyed_median_ratio > KEYED_MEDIAN_RATIO_THRESHOLD:
            length_flags.append(q["id"])
        if keyed_detail_delta > KEYED_SPECIFICITY_DELTA_THRESHOLD:
            specificity_flags.append(q["id"])
        if keyed_lexical_delta > 2:
            lexical_flags.append(q["id"])
        if len(set(q["options"].values())) != 4 or len(punctuation) > 1:
            format_flags.append(q["id"])
        rows.append({
            "question_id": q["id"], "word_counts": counts,
            "pairwise_max_min_ratio": round(pairwise_ratio, 3),
            "keyed_to_median_ratio": round(keyed_median_ratio, 3),
            "keyed_detail_marker_delta": keyed_detail_delta,
            "keyed_lexical_overlap_delta": keyed_lexical_delta,
        })
    return {
        "policy": (
            "A keyed option is a conspicuous length cue when its word count differs from the within-question "
            f"median by a factor greater than {KEYED_MEDIAN_RATIO_THRESHOLD}; detail-marker and lexical-overlap "
            "deltas independently detect keyed specificity. Pairwise max/min is reported, not used alone, "
            "because an implausibly terse distractor is not a keyed-answer cue."
        ),
        "keyed_median_ratio_threshold": KEYED_MEDIAN_RATIO_THRESHOLD,
        "keyed_specificity_delta_threshold": KEYED_SPECIFICITY_DELTA_THRESHOLD,
        "maximum_pairwise_word_ratio": round(max(row["pairwise_max_min_ratio"] for row in rows), 3),
        "maximum_keyed_median_ratio": round(max(row["keyed_to_median_ratio"] for row in rows), 3),
        "length_flags": length_flags, "format_flags": format_flags,
        "specificity_flags": specificity_flags, "lexical_key_flags": lexical_flags,
        "questions": rows,
    }


SOURCE_ATOMIC_SELECTIONS = """
YG-OB-001|identity|prop-e57bb0fe5c5acdc39d59
YG-OB-002|texts|prop-c558018e253b0c9ba939
YG-OB-003|boundary|prop-7f37721556882ca0565e
YG-OB-004|citta|prop-68fe0e2a4ff2eae9c539
YG-OB-005|reflection|prop-b219eeb0f5189f9efaeb
YG-OB-006|misidentification|prop-af3cd9cdeaad12bbc1e8
YG-OB-007|bhumi-k|prop-33f369edff19000ddba8
YG-OB-008|bhumi-m|prop-5a59ed1240bd7b302845
YG-OB-009|bhumi-v|prop-b6b2cf82d01751ee3811
YG-OB-010|bhumi-e|prop-a8403b8d781f6b636b83
YG-OB-011|bhumi-n|prop-78b33b8b41f2fb017c05
YG-OB-012|vrtti-list|prop-8de20ce74f437a987597
YG-OB-013|klista|prop-e2858cd09ccef6c23cd8
YG-OB-014|pramana|prop-bc1a0bbda09f315be0cd
YG-OB-015|sleep|prop-f32b269081f7395840e2
YG-OB-016|abhyasa|prop-4c4b67e1ae7152468911
YG-OB-017|vairagya|prop-3dad356285f7fe50f613
YG-OB-018|para|prop-f45f450501a281755208
YG-OB-019|klesa-list|prop-4bf9877fcec42ed6386a
YG-OB-020|avidya|prop-146bfe6a3e6f7f2d2979
YG-OB-021|states|prop-e52400627c3adf644796
YG-OB-022|kriya|prop-84e1b7a5b9d5c3e5c9be
YG-OB-023|karma-chain|prop-982dcf5f00fdf9740f22
YG-OB-024|vipaka|prop-e3ac6f4257c24e73c65d
YG-OB-025|karma-types|prop-ec7a024925f4f70afab5
YG-OB-026|yamas|prop-6727d8aef942e55fb075
YG-OB-027|niyamas|prop-396e37a0ec0fe26ca56e
YG-OB-028|outer-inner|prop-021fe5c9db7de121cea0
YG-OB-029|pratyahara|prop-adf6ac5d78994daf3b50
YG-OB-030|samyama|prop-35798a7a9697d75aa9b1
YG-OB-031|ys117|prop-de7b6bce4bf0f395d164
YG-OB-032|samapatti|prop-9fcccedd236bd61f2252
YG-OB-033|sabija|prop-4cc85287737fcea916b9
YG-OB-034|asamprajnata|prop-cf70d91201c3c9b8094e
YG-OB-035|nirbija|prop-6d0c67796b4fdd98dd69
YG-OB-036|two-seeds|prop-a196b9e9b1b7a1089e86
YG-OB-037|rtambhara|prop-2b76455a112530b84bb6
YG-OB-038|routes|prop-5ef61b4e6f08b6e48147
YG-OB-039|parinamas|prop-8b2b4bcb435af08d56e9
YG-OB-040|dharmin|prop-0a1d81ceb45de6745a7d
YG-OB-041|siddhi|prop-7318a784b85afbd0b718
YG-OB-042|isvara-def|prop-61eee4a0d82f23e76c3b
YG-OB-043|pranava|prop-c99e39340ef8f6bbadce
YG-OB-044|noncreator|prop-d1f881a5982237d78719
YG-OB-045|nongranter|prop-3cf91afac1c6d4f9bf8c
YG-OB-046|yogic-perception|prop-30cbbb874e3a5c689239
YG-OB-047|samkhya-continuity|prop-2e523346cbad48d25fcb
YG-OB-048|samkhya-difference|prop-43ca0695c633a9501135
YG-OB-049|buddhist|prop-d798ed1e6bdc52ef0dc4
YG-OB-050|yogacara|prop-b2e9aefc12f3c92fc97e
YG-OB-051|advaita|prop-669faf937c64ced98d76
YG-OB-052|nyaya|prop-c621121343dfebaaf998
YG-OB-053|dharmamegha|prop-803981d56a8fd96962df
YG-OB-054|viveka|prop-203b4ce11087f81adfbc
YG-OB-055|pratiprasava|prop-fe48c08d6fee0329ee45
YG-OB-056|kaivalya|prop-ddbd94770c33dc421ea6
YG-OB-057|crit-interaction|prop-1009874db8c59782c6d2
YG-OB-058|crit-negative|prop-fe438e0a2ad68c949218
YG-OB-059|ethics|prop-79450ce1407d8d7a920b
YG-OB-060|psychology|prop-445a9994907457b38fe5
YG-OB-061|pyq2019|prop-5ffc560cb5cc00a3f4bc
YG-OB-062|pyq2020|prop-03d5b047d9e8b75d1b95
YG-OB-063|pyq2021|prop-b52b0809f92ee7c6a7e6
YG-OB-064|pyq2022|prop-9a4b33499deb65f4b0fb
YG-OB-065|pyq2023|prop-261be9364ed9403b5a73
YG-OB-066|pyq2024|prop-a3cfc5c63b1e00b4ccad
YG-OB-067|pyq2025|prop-e9cf573d6d210f806da7
YG-OB-068|pyq2026|prop-805f8a4406592f8e8b49
YG-OB-069|antarayas|prop-af2da4deb56209933288
YG-OB-070|symptoms|prop-19888939b0f964d76ffb
YG-OB-071|attitudes|prop-13973d06c4e0f1e6de18
YG-OB-072|mahavrata|prop-6521df2ed561caf8f412
YG-OB-073|asana|prop-92b7eabb322ab44d9bf4
YG-OB-074|pranayama|prop-33497012446e65aab049
YG-OB-075|dharana-dhyana|prop-d81ded5d21fd0b2b84d6
YG-OB-076|gunas-purpose|prop-eb345204a16c2a9f537e
YG-OB-078|dharma-megha-function|prop-254c248f8bbbc00c7fd1
YG-OB-079|drastr-drshya|prop-19ab2c76f271be6bf627
YG-OB-080|kaivalya-double|prop-e3149276e3666674bb7c
YG-OB-081|smrti-definition|prop-ecb8c86444116a2a1974
""".strip()


def source_atomic_selections() -> list[dict]:
    return [
        {"obligation_id": oid, "category": category, "proposition_id": proposition_id}
        for oid, category, proposition_id in
        (line.split("|") for line in SOURCE_ATOMIC_SELECTIONS.splitlines())
    ]


def question_definitions() -> dict[str, dict]:
    rows = {}
    for i, (category, title, correct, w1, w2, w3) in enumerate(QUESTION_DEFINITION_ROWS, 1):
        oid = f"YG-OB-{i:03d}"
        rows[oid] = {
            "category": category, "title": title, "correct": correct,
            "distractors": [w1, w2, w3],
        }
    return rows


def build_qbank(obligations: list[dict], answer_sequence: str) -> list[dict]:
    assert len(answer_sequence) == len(obligations)
    definitions = question_definitions()
    bank = []
    for i, obligation in enumerate(obligations, 1):
        definition = definitions[obligation["obligation_id"]]
        title, correct = definition["title"], definition["correct"]
        answer = answer_sequence[i - 1]
        wrongs = iter(definition["distractors"])
        options = {letter: correct if letter == answer else next(wrongs) for letter in "ABCD"}
        explanations = {
            letter: (f"Correct. {correct}" if letter == answer
                     else f"Incorrect. {text} The controlling proposition is: {correct}")
            for letter, text in options.items()
        }
        bank.append({
            "id": f"Q{i}", "obligation_id": obligation["obligation_id"], "cell_id": f"YG-TM-{i:03d}", "title": title,
            "stem": f"Which statement most accurately captures the Yoga doctrine of {title.lower()}?",
            "options": options, "answer": answer, "explanations": explanations,
            "tokens": [correct.split()[0], "Yoga" if "Yoga" in correct else correct.split()[-1].rstrip(".")],
            "category": obligation["category"],
        })
    return bank


QBANK: list[dict] = []
CELLS: list[tuple] = []
ANSWER_SEQUENCE = ""
ANSWER_SALT = 0


def select_supplementary() -> list[dict]:
    selected = []
    for source_key in ("supplementary_complete", "supplementary_layered", "supplementary_workbook"):
        selected.extend(heading_blocks(SOURCES[source_key], source_key))
    return selected


def proposition_rows(block: dict) -> tuple[list[dict], list[dict]]:
    units, excluded = semantic_units(block["_payload"])
    mappings = []
    for i, unit in enumerate(units, 1):
        mappings.append({
            "source_block_id": block["id"], "occurrence": i,
            "proposition_id": "prop-" + sha_text(norm(unit))[:20],
            "exact_payload_sha256": sha_text(unit), "exact_payload": unit,
        })
    return mappings, [{"source_block_id": block["id"], **x} for x in excluded]


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


def required_anchor_groups(obligation: dict, authority_text: str) -> list[list[str]]:
    authority_tokens = semantic_tokens(authority_text)
    if obligation["obligation_id"] == "YG-OB-078":
        return [
            ["dharmamegha", "cloud-of-dharma"],
            ["affliction", "afflictions", "klesa"],
            ["binding action", "karma", "karmic"],
            ["cease", "cessation", "end"],
        ]
    anchors = [[token] for token in sorted(authority_tokens, key=lambda x: (-len(x), x))[:3]]
    if len(anchors) < 2:
        raise RuntimeError(f"Insufficient concept-specific authority anchors for {obligation['obligation_id']}")
    return anchors


def conjunctive_anchor_match(text: str, groups: list[list[str]]) -> bool:
    return bool(groups) and all(anchor_group_present(text, group) for group in groups)


def proposition_obligation_score(proposition: str, obligation: dict) -> tuple[float, int]:
    prop_tokens = semantic_tokens(proposition)
    obligation_tokens = semantic_tokens(obligation["atomic_statement"])
    overlap = len(prop_tokens & obligation_tokens)
    if not prop_tokens or not obligation_tokens:
        return 0.0, 0
    return overlap / len(obligation_tokens) + overlap / len(prop_tokens), overlap


def authority_match_is_relevant(proposition: str, obligation: dict, groups: list[list[str]] | None = None) -> bool:
    return conjunctive_anchor_match(
        proposition,
        groups if groups is not None else required_anchor_groups(obligation, proposition),
    )


def locate_source_lines(source_key: str, payload: str) -> tuple[int, int]:
    lines = SOURCES[source_key].read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    target = norm(payload)
    matches = []
    for start in range(len(lines)):
        for end in range(start + 1, min(len(lines), start + 20) + 1):
            candidate = norm("\n".join(lines[start:end]))
            if target in candidate:
                matches.append((end - start, start + 1, end))
                break
            if len(candidate) > len(target) * 2 + 200:
                break
    if matches:
        _, start, end = min(matches)
        return start, end
    raise RuntimeError(f"Cannot locate source coordinate for {source_key}: {payload[:80]}")


def primary_ii27_obligation(primary_authority: dict) -> dict:
    identity = primary_authority["source_identity"]
    raw = primary_authority["raw_object"]
    coordinate = primary_authority["coordinate"]
    payload = primary_authority["payload"]
    snapshot = primary_authority["snapshot"]
    doctrine = primary_authority["doctrine"]
    authority = primary_authority["authority"]
    evidence = {
        "source_key": "primary_ii27",
        "source_path": snapshot["path"],
        "source_file_sha256": raw["sha256"],
        "source_file_bytes": raw["bytes"],
        "source_item_url": identity["item_url"],
        "source_object_url": identity["object_url"],
        "archive_identifier": identity["archive_identifier"],
        "archive_ark": identity["archive_ark"],
        "retrieval_date": identity["retrieval_date"],
        "snapshot_sha256": snapshot["sha256"],
        "source_block_id": doctrine["source_block_id"],
        "proposition_id": doctrine["proposition_id"],
        "exact_payload": payload["exact_text"],
        "exact_payload_sha256": payload["sha256"],
        "normalized_sha256": sha_text(norm(doctrine["atomic_statement"])),
        "line_start": coordinate["line_start"],
        "line_end": coordinate["line_end"],
        "source_line_count": raw["line_count"],
        "exact_translation_excerpt": payload["exact_translation_excerpt"],
        "normalized_sanskrit": doctrine["normalized_sanskrit"],
        "normalized_transliteration": doctrine["normalized_transliteration"],
        "required_anchor_groups": doctrine["required_anchor_groups"],
        "authority_kind": authority["kind"],
        "scope_restriction": authority["scope_restriction"],
    }
    return {
        "obligation_id": primary_authority["obligation_id"],
        "category": doctrine["category"],
        "atomic_statement": doctrine["atomic_statement"],
        "source_proposition_id": evidence["proposition_id"],
        "rationale": (
            "The user-approved primary-text snapshot directly supports only the restrained "
            "Yoga Sūtra II.27 sevenfold-highest/final-ground claim."
        ),
        "minimum_probes": 1,
        "cell_id": "YG-TM-077",
        "authority_evidence": [evidence],
        "coverage_derivation": authority["coverage_derivation"],
    }


def independent_non_testability(occurrence: dict, block: dict) -> tuple[str, str]:
    lower = norm(occurrence["exact_payload"])
    if re.search(r"\b(?:source|citation|bibliograph|copyright|prepared from|edition|page)\b", lower):
        return "source_or_citation_only", "Bibliographic, source, or citation metadata does not state an independently testable Yoga doctrine."
    if re.search(r"\b(?:how to write|examiner|answer|revision|roadmap|session|question|marks?|word limit|practice)\b", lower):
        return "meta_answer_writing", "Answer-writing, revision, navigation, or practice instruction is pedagogical metadata rather than doctrine."
    if re.search(r"\b(?:example|analogy|illustrat|for instance|scientist|devotee|case study)\b", lower):
        return "example_only", "The row is an illustration or application of a doctrine classified elsewhere, not a new atomic doctrine."
    if re.search(r"\b(?:century|chronolog|histor|traditional|later commentator|date|authorship)\b", lower):
        return "chronology_or_context_only", "The row supplies historical or contextual framing without a separate doctrinal discriminator."
    if re.search(r"\b(?:therefore|thus|accordingly|in short|recap|hence|implies|follows)\b", lower):
        return "repeated_implication", "The row restates an implication of already extracted source propositions and adds no independent atomic claim."
    return "dependent_qualification", (
        f"The row qualifies or develops the source discussion under '{block['heading']}' and is not independently atomic "
        "without that surrounding doctrinal context."
    )


def build_obligation_inventory(
    mandatory_blocks: list[dict], learner_files: dict[str, str], primary_authority: dict
) -> dict:
    occurrences = []
    block_by_id = {block["id"]: block for block in mandatory_blocks}
    for block in mandatory_blocks:
        mappings, _excluded = proposition_rows(block)
        for mapping in mappings:
            occurrences.append({**mapping, "source": block["source"], "heading": block["heading"]})

    first_by_prop = {}
    for occurrence in occurrences:
        first_by_prop.setdefault(occurrence["proposition_id"], occurrence)
    selections = source_atomic_selections()
    selected_by_pid = {row["proposition_id"]: row for row in selections}
    if len(selected_by_pid) != len(selections):
        raise RuntimeError("Duplicate source proposition selected for multiple obligations")
    absent = [row for row in selections if row["proposition_id"] not in first_by_prop]
    if absent:
        raise RuntimeError(f"Selected source propositions absent: {absent}")
    assigned_prop_to_obligation = {
        row["proposition_id"]: row["obligation_id"] for row in selections
    }
    obligation_evidence = {}
    obligations = []
    for sequence, selection in enumerate(selections, 1):
        chosen = first_by_prop[selection["proposition_id"]]
        block = block_by_id[chosen["source_block_id"]]
        obligation = {
            "obligation_id": selection["obligation_id"],
            "category": selection["category"],
            "atomic_statement": chosen["exact_payload"],
            "source_proposition_id": chosen["proposition_id"],
            "rationale": "The exact mandatory-source proposition independently states one examinable Yoga distinction.",
            "minimum_probes": 1,
        }
        groups = required_anchor_groups(obligation, chosen["exact_payload"])
        line_start, line_end = locate_source_lines(chosen["source"], chosen["exact_payload"])
        evidence = {
            "source_key": chosen["source"],
            "source_path": str(SOURCES[chosen["source"]]),
            "source_file_sha256": sha_bytes(SOURCES[chosen["source"]].read_bytes()),
            "source_block_id": chosen["source_block_id"],
            "proposition_id": chosen["proposition_id"],
            "exact_payload": chosen["exact_payload"],
            "exact_payload_sha256": chosen["exact_payload_sha256"],
            "normalized_sha256": sha_text(norm(chosen["exact_payload"])),
            "line_start": line_start,
            "line_end": line_end,
            "required_anchor_groups": groups,
            "authority_kind": "mandatory_source_proposition",
        }
        obligation_evidence[obligation["obligation_id"]] = evidence
        obligations.append({
            **obligation,
            "cell_id": f"YG-TM-{sequence:03d}",
            "authority_evidence": [evidence],
            "coverage_derivation": "independent_mandatory_proposition_inventory_before_question_authoring",
        })
    obligations.append(primary_ii27_obligation(primary_authority))
    obligations.sort(key=lambda row: int(row["obligation_id"].rsplit("-", 1)[1]))
    for sequence, obligation in enumerate(obligations, 1):
        obligation["cell_id"] = f"YG-TM-{sequence:03d}"

    first_seen = set()
    proposition_classifications = []
    classifications_by_block = {}
    for occurrence in occurrences:
        pid = occurrence["proposition_id"]
        block = block_by_id[occurrence["source_block_id"]]
        destination = {
            "file": learner_files[block["source"]],
            "anchor": block["id"],
            "payload_sha256": block["own_payload_sha256"],
        }
        if pid in first_seen:
            classification = "duplicate_normalized_obligation"
            rationale = f"Normalized duplicate of canonical proposition {pid}; retained only as an occurrence-level audit trail."
            reverse = {
                "canonical_proposition_id": pid,
                "canonical_proposition_occurrence": first_by_prop[pid]["source_block_id"] + f":{first_by_prop[pid]['occurrence']}",
            }
        elif pid in assigned_prop_to_obligation:
            classification = "testable_atomic_obligation"
            oid = assigned_prop_to_obligation[pid]
            rationale = "This complete proposition directly states one source-derived atomic examinable obligation."
            reverse = {
                "represented_by_obligation_id": oid,
                "obligation_id": oid,
                "relation": "direct_atomic_authority",
                "doctrine_specific_reason": f"Exact mandatory-source wording establishes the {selected_by_pid[pid]['category']} discriminator.",
            }
        elif re.search(r"(?:twenty[- ]five|25)[- ]tattva|full (?:sāṃkhya|samkhya).*(?:evolution|causation|proof)", norm(occurrence["exact_payload"])):
            classification = "routed_boundary"
            rationale = "The proposition belongs to the bounded Sāṃkhya owner rather than Yoga's citta, discipline, samādhi, Īśvara, or kaivalya use."
            reverse = {"destination_obligation_id": "YG-SK-BOUNDARY-001", "destination_topic": "05-Samkhya"}
        else:
            classification = "supporting_non_testable_context"
            category, reason = independent_non_testability(occurrence, block)
            rationale = reason
            reverse = {
                "non_testability_category": category,
                "independently_checkable_reason": reason,
                "destination_evidence": destination,
            }
        first_seen.add(pid)
        row = {
            "source_block_id": occurrence["source_block_id"],
            "proposition_occurrence": occurrence["occurrence"],
            "proposition_id": pid,
            "exact_payload": occurrence["exact_payload"],
            "exact_payload_sha256": occurrence["exact_payload_sha256"],
            "normalized_sha256": sha_text(norm(occurrence["exact_payload"])),
            "classification": classification,
            "rationale": rationale,
            "reverse_mapping": reverse,
        }
        proposition_classifications.append(row)
        classifications_by_block.setdefault(block["id"], []).append(row)

    block_classifications = []
    cell_by_obligation = {row["obligation_id"]: row["cell_id"] for row in obligations}
    for block in mandatory_blocks:
        rows = classifications_by_block.get(block["id"], [])
        atomic = sorted({x["reverse_mapping"]["represented_by_obligation_id"] for x in rows
                         if x["classification"] == "testable_atomic_obligation"})
        kinds = {x["classification"] for x in rows}
        if atomic:
            classification = "testable_atomic_obligation"
            reverse = {"obligation_ids": atomic, "cell_ids": [cell_by_obligation[x] for x in atomic]}
            rationale = "At least one proposition in this mandatory block is the controlling evidence for an atomic test obligation."
        elif kinds and kinds <= {"duplicate_normalized_obligation"}:
            classification = "duplicate_normalized_obligation"
            reverse = {"proposition_occurrences": [f"{x['source_block_id']}:{x['proposition_occurrence']}" for x in rows]}
            rationale = "Every meaningful proposition in this block duplicates a normalized proposition classified at its first occurrence."
        elif "routed_boundary" in kinds and kinds <= {"routed_boundary", "duplicate_normalized_obligation"}:
            classification = "routed_boundary"
            reverse = {"destination_obligation_id": "YG-SK-BOUNDARY-001", "destination_topic": "05-Samkhya"}
            rationale = "The block's independent content is owned by the bounded Sāṃkhya destination."
        else:
            classification = "supporting_non_testable_context"
            reverse = {"destination_evidence": {
                "file": learner_files[block["source"]], "anchor": block["id"],
                "payload_sha256": block["own_payload_sha256"],
            }}
            rationale = "The block is preserved as teaching/revision evidence but introduces no separate atomic MCQ discriminator."
        block_classifications.append({
            "source_block_id": block["id"], "classification": classification,
            "rationale": rationale, "reverse_mapping": reverse,
        })

    proposition_counts = Counter(x["classification"] for x in proposition_classifications)
    block_counts = Counter(x["classification"] for x in block_classifications)
    return {
        "schema_version": 1,
        "topic": "06 Yoga",
        "derivation_order": [
            "parse_521_mandatory_blocks",
            "extract_and_normalize_meaningful_propositions",
            "classify_every_block_and_proposition_exactly_once",
            "derive_atomic_obligations",
            "build_cells_from_obligations",
            "author_and_map_questions_last",
        ],
        "mandatory_block_count": len(mandatory_blocks),
        "mandatory_proposition_occurrence_count": len(proposition_classifications),
        "block_classification_counts": {key: block_counts[key] for key in (
            "testable_atomic_obligation", "supporting_non_testable_context",
            "duplicate_normalized_obligation", "routed_boundary")},
        "proposition_classification_counts": {key: proposition_counts[key] for key in (
            "testable_atomic_obligation", "supporting_non_testable_context",
            "duplicate_normalized_obligation", "routed_boundary")},
        "atomic_obligation_count": len(obligations),
        "approved_primary_source_obligations": [{
            "obligation_id": primary_authority["obligation_id"],
            "authority_scope": primary_authority["authority"]["kind"],
            "snapshot_path": primary_authority["snapshot"]["path"],
            "snapshot_sha256": primary_authority["snapshot"]["sha256"],
            "source_object_url": primary_authority["source_identity"]["object_url"],
            "source_object_sha256": primary_authority["raw_object"]["sha256"],
            "source_object_bytes": primary_authority["raw_object"]["bytes"],
            "line_start": primary_authority["coordinate"]["line_start"],
            "line_end": primary_authority["coordinate"]["line_end"],
            "payload_sha256": primary_authority["payload"]["sha256"],
        }],
        "blocked_source_obligations": [],
        "obligations": obligations,
        "block_classifications": block_classifications,
        "proposition_classifications": proposition_classifications,
    }


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def render_mcqs(solutions: bool) -> str:
    title = "# Yoga MCQ Solutions" if solutions else "# Yoga MCQ Questions"
    out = [title, "", f"Coverage-derived bank: **{len(QBANK)} questions from {len(CELLS)} atomic cells**.", ""]
    for i, q in enumerate(QBANK, 1):
        out += [f"## MCQ {i}. {q['title']}", "", q["stem"], ""]
        out += [f"{letter}. {q['options'][letter]}" for letter in "ABCD"]
        if solutions:
            out += ["", f"**Answer: {q['answer']}.**", ""]
            out += [f"- **{letter}:** {q['explanations'][letter]}" for letter in "ABCD"]
            out += ["", f"**Test cell:** `{q['cell_id']}`"]
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_toolkit() -> tuple[str, dict]:
    out = [
        "# Yoga Answer-Writing Toolkit", "",
        "> These are independent learner-practice models, not official UPSC answer keys.", "",
        "## Demand map", "",
        "Use exact Sanskrit categories, explain the causal mechanism, add one live objection and close with a qualified verdict. "
        "For comparison questions, state Yoga's position before introducing the rival.", "",
        "## Reusable answer visuals", "",
        "```text",
        "avidyā → asmitā/rāga/dveṣa/abhiniveśa → karma → saṃskāra/vāsanā",
        "       → karmāśaya → vipāka (jāti, āyus, bhoga) → rebirth",
        "       ↘ kriyā-yoga + aṣṭāṅga + samādhi + viveka-khyāti → kaivalya",
        "```", "",
        "| Marks | Target words | Answer move |",
        "|---:|---:|---|",
        "| 10 | 150–200 | definition → exact distinction/list → qualification |",
        "| 15 | 250–300 | doctrine → mechanism → comparison/criticism → verdict |",
        "| 20 | 340–400 | full exposition → causal therapy → objection/reply → evaluation |", "",
    ]
    primary = []
    for year, qno, marks, wording, key in PYQS:
        model = model_text(key, marks)
        out += [
            f"## {year} {qno} — {marks} marks", "",
            f"**Exact verified wording:** {wording}", "",
            f"**Demand decoding:** {DEMANDS[key]}", "",
            "### Model answer", "", model, "",
            "### Qualification / criticism", "",
            "The conclusion is deliberately qualified: Yoga's practical and phenomenological coherence does not by itself eliminate the dualist interaction problem or justify importing later creator-theology.", "",
            "### Why this earns marks", "",
            f"The model answers every clause, uses exact technical distinctions, supplies causal reasoning, includes criticism and remains within the {marks}-mark word band.", "",
        ]
        primary.append({
            "year": year, "question": qno, "marks": marks, "exact_wording": wording,
            "demand_decoding": DEMANDS[key], "model_word_count": words(model),
            "qualification_present": True, "marks_rationale_present": True,
            "primary_owner": "Yoga",
        })
    out += ["## Supporting / cross-linked PYQ", ""]
    supporting = []
    for year, qno, marks, wording, note in SUPPORTING_PYQS:
        model = model_text("isvara", marks)
        demand = "Explain Nyāya's creator proofs first, then compare Yoga's puruṣa-viśeṣa, praṇava, teacherhood and contemplative function without transferring primary ownership."
        out += [
            f"### {year} {qno} — {marks} marks", "", f"**Exact verified wording:** {wording}", "",
            f"**Ownership:** {note}", "", f"**Demand decoding:** {demand}", "", "#### Model answer", "", model, "",
            "#### Qualification / criticism", "", "Yoga's limited theism is not established through the same atom-combination and efficient-cause proof-set as Nyāya; its soteriological usefulness does not prove metaphysical necessity.", "",
            "#### Why this earns marks", "", "The response keeps Nyāya as primary owner, states Yoga independently, compares proof and function, and closes with a qualified judgement within the 20-mark band.", "",
        ]
        supporting.append({"year": year, "question": qno, "marks": marks, "exact_wording": wording, "ownership": note,
                           "demand_decoding": demand, "model_word_count": words(model), "qualification_present": True,
                           "marks_rationale_present": True, "primary_owner": "Nyaya-Vaisesika", "supporting_owner": "Yoga"})
    out += ["## Original timed practice — six complete models", ""]
    originals = []
    for oid, marks, wording, key in ORIGINALS:
        model = model_text(key, marks)
        out += [f"### {oid} — {marks} marks", "", f"**Question:** {wording}", "", "**Model answer:**", "", model, "",
                "**Qualification:** Apply the comparison only after establishing Yoga's own categories and preserve the canonical boundary with Sāṃkhya.", ""]
        originals.append({"id": oid, "marks": marks, "question": wording, "band": list({10:(150,200),15:(250,300),20:(340,400)}[marks]),
                          "model_word_count": words(model)})
    out += [
        "## Introductions and conclusions", "",
        "- **Definition opening:** begin with *yogaś-citta-vṛtti-nirodhaḥ* and identify the demanded mechanism.",
        "- **System opening:** locate Yoga as a practical-soteriological development of Sāṃkhya dualism with Īśvara.",
        "- **Critical close:** grade Yoga as strong in disciplined psychology but vulnerable at puruṣa-prakṛti interaction.",
        "- **Comparative close:** state precisely that kaivalya is isolation, not Advaitic identity, Nyāya pain-cessation alone or Buddhist non-self.", "",
        "## Writing endurance", "",
        "Move from oral recall to a five-minute skeleton, then one pain-free timed answer. Stop if pain, numbness, tingling, swelling or weakness increases.", "",
    ]
    return "\n".join(out).rstrip() + "\n", {"primary": primary, "supporting": supporting, "originals": originals}


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


def derive_authority_refs(q: dict, blocks: list[dict]) -> list[dict]:
    terms = {x.casefold() for x in re.findall(r"[A-Za-zĀ-ž]{4,}", q["title"] + " " + q["category"])}
    ranked = []
    for block in blocks:
        hay = norm(block["heading"] + " " + block["_payload"])
        score = sum(term in hay for term in terms)
        if score:
            ranked.append((score, -block["ordinal"], block))
    if not ranked:
        ranked = [(1, 0, blocks[0])]
    ranked.sort(reverse=True, key=lambda row: (row[0], row[1]))
    return [{"source_block_id": row[2]["id"], "source": row[2]["source"],
             "payload_sha256": row[2]["own_payload_sha256"]} for row in ranked[:2]]


def main() -> None:
    global QBANK, CELLS, ANSWER_SEQUENCE, ANSWER_SALT
    primary_authority = load_primary_authority()
    for key, source in SOURCES.items():
        if not source.is_file():
            raise FileNotFoundError(source)
        if key in EXPECTED_SOURCE_IDENTITIES:
            expected = EXPECTED_SOURCE_IDENTITIES[key]
            text = source.read_text(encoding="utf-8").replace("\r\n", "\n")
            blocks = heading_blocks(source, key)
            if sha_bytes(source.read_bytes()) != expected["sha256"] or len(text.splitlines()) != expected["lines"] or len(blocks) != expected["blocks"]:
                raise RuntimeError(f"Formal source identity drift: {key}")

    snapshots = ROOT / "source-snapshots"
    snapshots.mkdir(exist_ok=True)
    for key, name in SNAPSHOT_NAMES.items():
        shutil.copyfile(SOURCES[key], snapshots / name)

    source_blocks = {key: heading_blocks(path, key) for key, path in SOURCES.items() if key not in {"pyq_2018_2025", "pyq_2026"}}
    formal_session = source_blocks["formal_session"]
    formal_workbook = source_blocks["formal_workbook"]
    canonical = source_blocks["canonical"]
    supplementary = source_blocks["supplementary_complete"] + source_blocks["supplementary_layered"] + source_blocks["supplementary_workbook"]
    all_blocks = formal_session + formal_workbook + canonical + supplementary

    classifications = {
        "formal_session": "mandatory_formal_session",
        "formal_workbook": "mandatory_formal_workbook",
        "canonical": "mandatory_canonical_boundary",
        "supplementary_complete": "supplementary_depth",
        "supplementary_layered": "supplementary_depth",
        "supplementary_workbook": "supplementary_depth",
    }
    learner_files = {
        "formal_session": "REVISION-GUIDE.md", "formal_workbook": "ANSWER-WRITING-TOOLKIT.md",
        "canonical": "REVISION-GUIDE.md", "supplementary_complete": "REVISION-GUIDE.md",
        "supplementary_layered": "REVISION-GUIDE.md", "supplementary_workbook": "REVISION-GUIDE.md",
    }

    anchored = {key: anchored_source(SOURCES[key], blocks) for key, blocks in source_blocks.items()}
    mirror_parts = ["# Yoga — Exact Anchored Authority and Depth Mirror", "",
                    "> Formal session/workbook are mandatory; canonical Yoga controls topic boundaries; supplementary sources add depth only.", ""]
    for key in ("formal_session", "formal_workbook", "canonical", "supplementary_complete", "supplementary_layered", "supplementary_workbook"):
        mirror_parts += [f"# Source: {key}", "", anchored[key], f'<a id="{key}-source-end"></a>', ""]
    mirror = "\n".join(mirror_parts).rstrip() + "\n"

    revision = """# Yoga — Complete Offline Revision Guide

> Provenance: `formal_present_canonical_boundary_controlled`. The exact formal session is preserved first. Canonical Yoga follows as the controlling ownership boundary. Supplementary sessions/workbook are depth-only and create no duplicate mandatory obligation rows.

## Package roadmap

1. Complete the formal learning sequence, including remediation, PYQs, advanced depth and register notes.
2. Use canonical material to control Yoga/Sāṃkhya ownership and doctrinal precision.
3. Use supplementary material only for additional depth, comparisons and answer transfer.
4. Test the complete matrix in `MCQ-QUESTIONS.md`, then study keyed explanations.
5. Write all primary/supporting PYQs and original timed answers from `ANSWER-WRITING-TOOLKIT.md`.

## Topic 05 boundary and reciprocal obligation

`YG-SK-BOUNDARY-001` is closed after serialized reconciliation with Topic 05. Sāṃkhya retains ownership of the exhaustive twenty-five-tattva evolution, proofs of puruṣa/prakṛti and full causation theory; Yoga owns its citta, discipline, samādhi, Īśvara and kaivalya use. The cross-link does not duplicate or transfer ownership.

# Mandatory formal learning session — exact anchored source

""" + anchored["formal_session"] + '\n<a id="formal_session-source-end"></a>\n# Canonical boundary owner — exact anchored source\n\n' + anchored["canonical"] + \
        '\n<a id="canonical-source-end"></a>\n# Supplementary depth — complete session\n\n' + anchored["supplementary_complete"] + \
        '\n<a id="supplementary_complete-source-end"></a>\n# Supplementary depth — layered session\n\n' + anchored["supplementary_layered"] + \
        '\n<a id="supplementary_layered-source-end"></a>\n# Supplementary depth — layered workbook\n\n' + anchored["supplementary_workbook"] + \
        '\n<a id="supplementary_workbook-source-end"></a>\n'

    generated_toolkit, practice_data = render_toolkit()
    toolkit = generated_toolkit + "\n# Mandatory formal solved-practice workbook — exact anchored source\n\n" + anchored["formal_workbook"] + \
        '\n<a id="formal_workbook-source-end"></a>\n'

    (ROOT / "FORMAL-SOURCE-MIRROR.md").write_text(mirror, encoding="utf-8", newline="\n")
    (ROOT / "REVISION-GUIDE.md").write_text(revision.rstrip() + "\n", encoding="utf-8", newline="\n")
    (ROOT / "ANSWER-WRITING-TOOLKIT.md").write_text(toolkit.rstrip() + "\n", encoding="utf-8", newline="\n")

    registry, raw_mappings, excluded_fragments, decisions, panels = {}, [], [], [], []
    for block in all_blocks:
        mappings, exclusions = proposition_rows(block)
        for mapping in mappings:
            registry.setdefault(mapping["proposition_id"], {
                "id": mapping["proposition_id"], "normalized_sha256": sha_text(norm(mapping["exact_payload"])),
                "exact_payload_sha256": mapping["exact_payload_sha256"], "representative_exact_payload": mapping["exact_payload"],
            })
        raw_mappings.extend(mappings)
        excluded_fragments.extend(exclusions)
        block_panels = panels_for_block(block)
        panels.extend(block_panels)
        classification = classifications[block["source"]]
        decision = {k: v for k, v in block.items() if k != "_payload"}
        decision.update({
            "classification": classification,
            "mandatory_obligation": classification != "supplementary_depth",
            "semantic_basis": "deterministically_filtered_exact_source_owned_independently_meaningful_payload",
            "proposition_mappings": mappings,
            "excluded_non_propositional_fragments": exclusions,
            "structural_parent_only": not mappings and bool(block["direct_children"]),
            "panel_ids": [x["id"] for x in block_panels],
            "destination": {"file": "FORMAL-SOURCE-MIRROR.md", "anchor": block["id"], "payload_sha256": block["own_payload_sha256"]},
            "learner_destination": {"file": learner_files[block["source"]], "anchor": block["id"], "payload_sha256": block["own_payload_sha256"]},
            "validation_result": "mapped_and_hash_bound",
        })
        decisions.append(decision)

    prop_counts = Counter(x["proposition_id"] for x in raw_mappings)
    duplicate_groups = sum(count > 1 for count in prop_counts.values())
    diagram_structural_exclusions = sum(x["reason"].startswith("diagram_") for x in excluded_fragments)
    source_counts = {key: len(source_blocks[key]) for key in source_blocks}
    classification_counts = Counter(row["classification"] for row in decisions)
    large_by_source = {key: sum(bool(row["large_leaf_segments"]) for row in source_blocks[key]) for key in source_blocks}
    segments_by_source = {key: sum(len(row["large_leaf_segments"]) for row in source_blocks[key]) for key in source_blocks}
    panel_by_source = Counter(row["source"] for row in panels)
    review = {
        "schema_version": 5, "topic": "06 Yoga", "authority_mode": "formal_present_canonical_boundary_controlled",
        "authored_at": NOW, "review_status": "authored_frozen",
        "review_method": "Exact H2-H4 exhaustive preflight across mandatory formal session/workbook and canonical boundary owner, with depth-only supplementary blocks; stable source-derived IDs; exact parent-only payload hashes; direct-child payload unions; segmented large leaves; table/diagram panel evidence; normalized semantic proposition registry and independent structural exclusions.",
        "sources": {key: {**file_info(path), "line_count": len(path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()),
                          "h2_h4_block_count": len(source_blocks[key]) if key in source_blocks else None}
                    for key, path in SOURCES.items()},
        "source_block_counts": source_counts, "formal_block_count": len(formal_session) + len(formal_workbook),
        "canonical_block_count": len(canonical), "supplementary_block_count": len(supplementary),
        "decision_count": len(decisions), "classification_counts": dict(classification_counts), "unclassified_count": 0,
        "raw_proposition_mapping_count": len(raw_mappings), "unique_normalized_proposition_count": len(registry),
        "duplicate_occurrences_deduplicated": len(raw_mappings) - len(registry), "duplicate_group_count": duplicate_groups,
        "excluded_fragment_count": len(excluded_fragments),
        "diagram_structural_exclusion_count": diagram_structural_exclusions,
        "excluded_fragment_reason_counts": dict(Counter(x["reason"] for x in excluded_fragments)),
        "proposition_registry": sorted(registry.values(), key=lambda row: row["id"]),
        "panel_count": len(panels), "panel_counts_by_source": dict(panel_by_source),
        "large_leaf_count": sum(large_by_source.values()), "large_leaf_counts_by_source": large_by_source,
        "large_leaf_segment_count": sum(segments_by_source.values()), "large_leaf_segment_counts_by_source": segments_by_source,
        "panels": panels, "decisions": decisions,
        "approved_primary_sources": [{
            "scope": primary_authority["authority"]["kind"],
            "obligation_id": primary_authority["obligation_id"],
            "snapshot_path": primary_authority["snapshot"]["path"],
            "snapshot_sha256": primary_authority["snapshot"]["sha256"],
            "item_url": primary_authority["source_identity"]["item_url"],
            "object_url": primary_authority["source_identity"]["object_url"],
            "object_bytes": primary_authority["raw_object"]["bytes"],
            "object_sha256": primary_authority["raw_object"]["sha256"],
            "ocr_coordinate": [
                primary_authority["coordinate"]["line_start"],
                primary_authority["coordinate"]["line_end"],
            ],
            "payload_sha256": primary_authority["payload"]["sha256"],
            "general_authority": primary_authority["authority"]["general_authority"],
        }],
        "routes": [{
            "obligation_id": "YG-SK-BOUNDARY-001", "direction": "outbound_reciprocal", "destination_topic": "05-Samkhya",
            "status": "closed_after_serialized_reconciliation", "source_owner": "Yoga",
            "requirement": "Preserve Sāṃkhya ownership of full 25-tattva evolution, proofs and causation; Yoga owns only the citta/path bridge.",
            "release_blocking_for_this_package": False, "development_disposition": "pass_after_cross_topic_reconciliation",
        }], "inbound_obligations": [],
    }
    write_json(ROOT / "FORMAL-COVERAGE-REVIEW.json", review)
    review_hash = sha_bytes((ROOT / "FORMAL-COVERAGE-REVIEW.json").read_bytes())
    audit = {
        "schema_version": 5, "topic": "06 Yoga", "authority_mode": review["authority_mode"], "status": "COMPLETE",
        "derived_from": "FORMAL-COVERAGE-REVIEW.json", "review_sha256": review_hash,
        "source_block_counts": source_counts, "formal_blocks": review["formal_block_count"], "canonical_blocks": len(canonical),
        "supplementary_blocks": len(supplementary), "decision_count": len(decisions), "unclassified": 0,
        "raw_proposition_mappings": len(raw_mappings), "unique_normalized_propositions": len(registry),
        "duplicate_occurrences": len(raw_mappings)-len(registry), "duplicate_groups": duplicate_groups,
        "excluded_structural_coordinates": len(excluded_fragments), "excluded_fragment_reason_counts": review["excluded_fragment_reason_counts"],
        "diagram_structural_exclusions": diagram_structural_exclusions,
        "panels": len(panels), "panel_counts_by_source": dict(panel_by_source),
        "large_leaves": review["large_leaf_count"], "large_leaf_counts_by_source": large_by_source,
        "large_leaf_segments": review["large_leaf_segment_count"], "large_leaf_segment_counts_by_source": segments_by_source,
        "mandatory_obligations": len(formal_session)+len(formal_workbook)+len(canonical),
        "approved_primary_source_obligations": 1,
        "approved_primary_snapshot_sha256": primary_authority["snapshot"]["sha256"],
        "supplementary_depth_rows": len(supplementary), "inbound_obligations_due": 0,
        "outbound_reciprocal_obligations_due": 1,
    }
    write_json(ROOT / "FORMAL-COVERAGE-AUDIT.json", audit)

    mandatory_blocks = formal_session + formal_workbook + canonical
    obligation_inventory = build_obligation_inventory(mandatory_blocks, learner_files, primary_authority)
    proposition_class_by_coordinate = {
        (row["source_block_id"], row["proposition_occurrence"]): row
        for row in obligation_inventory["proposition_classifications"]
    }
    source_inventory_blocks = []
    for block in mandatory_blocks:
        mappings, block_exclusions = proposition_rows(block)
        source_inventory_blocks.append({
            "source_block_id": block["id"],
            "source": block["source"],
            "ordinal": block["ordinal"],
            "heading": block["heading"],
            "exact_payload": block["_payload"],
            "exact_payload_sha256": block["own_payload_sha256"],
            "normalized_payload_sha256": sha_text(norm(block["_payload"])),
            "classification": next(
                row["classification"] for row in obligation_inventory["block_classifications"]
                if row["source_block_id"] == block["id"]
            ),
            "proposition_ids": [row["proposition_id"] for row in mappings],
            "excluded_fragments": block_exclusions,
            "reverse_mapping": {
                "source_path": str(SOURCES[block["source"]]),
                "line_start": block["line_start"],
                "line_end": block["line_end"],
            },
        })
    source_inventory = {
        "schema_version": 1,
        "topic": "06 Yoga",
        "derivation_stage": "frozen_before_question_bank",
        "source_hashes": {
            key: sha_bytes(SOURCES[key].read_bytes())
            for key in ("formal_session", "formal_workbook", "canonical")
        },
        "approved_primary_sources": obligation_inventory["approved_primary_source_obligations"],
        "mandatory_block_count": len(mandatory_blocks),
        "complete_proposition_occurrence_count": len(obligation_inventory["proposition_classifications"]),
        "block_classification_counts": obligation_inventory["block_classification_counts"],
        "proposition_classification_counts": obligation_inventory["proposition_classification_counts"],
        "blocks": source_inventory_blocks,
        "propositions": [
            {
                **row,
                "source_reverse_mapping": {
                    "source": block_by_id["source"],
                    "ordinal": block_by_id["ordinal"],
                    "heading": block_by_id["heading"],
                },
            }
            for row in obligation_inventory["proposition_classifications"]
            for block_by_id in [{
                "source": next(b["source"] for b in mandatory_blocks if b["id"] == row["source_block_id"]),
                "ordinal": next(b["ordinal"] for b in mandatory_blocks if b["id"] == row["source_block_id"]),
                "heading": next(b["heading"] for b in mandatory_blocks if b["id"] == row["source_block_id"]),
            }]
        ],
        "blocked_source_obligations": obligation_inventory["blocked_source_obligations"],
    }
    write_json(ROOT / "SOURCE-PROPOSITION-INVENTORY.json", source_inventory)
    write_json(ROOT / "TESTABLE-OBLIGATIONS.json", obligation_inventory)
    classification_hash = sha_bytes((ROOT / "SOURCE-PROPOSITION-INVENTORY.json").read_bytes())
    obligation_hash = sha_bytes((ROOT / "TESTABLE-OBLIGATIONS.json").read_bytes())

    # Question artifacts are materialized only after the independent source
    # proposition inventory and obligation classifications have been frozen.
    definitions = question_definitions()
    question_ids = [f"Q{i}" for i in range(1, len(obligation_inventory["obligations"]) + 1)]
    ANSWER_SEQUENCE, ANSWER_SALT = deterministic_answer_sequence(question_ids)
    QBANK = build_qbank(obligation_inventory["obligations"], ANSWER_SEQUENCE)
    CELLS = [
        (f"YG-TM-{i:03d}", obligation["obligation_id"],
         definitions[obligation["obligation_id"]]["title"], obligation["minimum_probes"])
        for i, obligation in enumerate(obligation_inventory["obligations"], 1)
    ]
    (ROOT / "MCQ-QUESTIONS.md").write_text(render_mcqs(False), encoding="utf-8", newline="\n")
    (ROOT / "MCQ-SOLUTIONS.md").write_text(render_mcqs(True), encoding="utf-8", newline="\n")

    cells_json, mappings = [], []
    obligations_by_id = {row["obligation_id"]: row for row in obligation_inventory["obligations"]}
    for cell_id, obligation_id, title, minimum_probes in CELLS:
        obligation = obligations_by_id[obligation_id]
        definition = definitions[obligation_id]
        mapped_questions = [q["id"] for q in QBANK if q["obligation_id"] == obligation_id]
        shared_question_tokens = sorted(
            semantic_tokens(obligation["atomic_statement"])
            & semantic_tokens(definition["title"] + " " + definition["correct"]),
            key=lambda token: (-len(token), token),
        )
        question_anchor_groups = (
            [["dharmamegha"], ["affliction", "afflictive"], ["karma", "karmic", "binding action"], ["cease", "exhaustion", "remove"]]
            if obligation_id == "YG-OB-078"
            else obligation["authority_evidence"][0]["required_anchor_groups"]
            if obligation_id == "YG-OB-077"
            else [[token] for token in shared_question_tokens[:3]]
        )
        if not question_anchor_groups:
            raise RuntimeError(f"Insufficient source/question entailment anchors for {obligation_id}")
        cell = {
                "cell_id": cell_id, "obligation_id": obligation_id, "title": title,
                "substantive_discriminator": obligation["atomic_statement"],
                "category": obligation["category"], "minimum_probes": minimum_probes,
                "mapped_question_ids": mapped_questions,
                "evidence_tokens": shared_question_tokens[:6],
                "required_anchor_groups": question_anchor_groups,
                "authority_refs": obligation["authority_evidence"], "coverage_status": "covered"}
        cells_json.append(cell)
        for qid in mapped_questions:
            mappings.append({"question_id": qid, "cell_id": cell_id, "obligation_id": obligation_id,
                             "primary_discriminator": obligation["atomic_statement"],
                             "evidence_scope": "title_stem_keyed_option_keyed_explanation_only"})
    matrix = {
        "schema_version": 5, "topic": "06 Yoga",
        "derivation_policy": "cells_are_created_from_TESTABLE_OBLIGATIONS_before_questions_are_authored_or_mapped",
        "question_total_policy": "one_probe_per_independently_derived_atomic_obligation_unless_an_obligation_declares_more",
        "historical_formal_mcqs_are_evidence_only": 32,
        "authority_block_count": len(formal_session)+len(formal_workbook)+len(canonical),
        "obligation_inventory_file": "TESTABLE-OBLIGATIONS.json",
        "obligation_inventory_sha256": obligation_hash,
        "source_classification_file": "SOURCE-PROPOSITION-INVENTORY.json",
        "source_classification_sha256": classification_hash,
        "atomic_obligation_count": len(obligation_inventory["obligations"]),
        "cell_count": len(cells_json), "derived_minimum_probes": sum(x["minimum_probes"] for x in cells_json),
        "question_total": len(QBANK), "cells": cells_json, "question_mappings": mappings,
    }
    write_json(ROOT / "TEST-MATRIX.json", matrix)
    answer_stats = answer_statistics(ANSWER_SEQUENCE)
    cue_metrics = option_cue_metrics(QBANK)
    write_json(ROOT / "MCQ-AUDIT.json", {
        "schema_version": 5, "question_total": len(QBANK), "cell_count": len(CELLS),
        "answer_sequence": ANSWER_SEQUENCE, "answer_counts": answer_stats["counts"], "max_answer_run": answer_stats["max_run"],
        "short_cycles": answer_stats["cycles"], "mapping_scope": "keyed_evidence_only",
        "position_policy": {
            "method": "independent_stable_hash_per_question",
            "seed": ANSWER_SEED,
            "accepted_salt": ANSWER_SALT,
            "selection_rule": "first salt whose independent A-D draws satisfy run, cycle, and broad statistical thresholds; equality is neither targeted nor accepted as a goal",
            "max_run": 2,
            "prohibited_cycle_periods": [2, 3, 4],
            "min_share": ANSWER_IMBALANCE_MIN_SHARE,
            "max_share": ANSWER_IMBALANCE_MAX_SHARE,
            "chi_square_max": ANSWER_CHI_SQUARE_MAX,
            "observed_chi_square": answer_stats["chi_square"],
            "predictable_cycle_detected": bool(answer_stats["cycles"]),
        },
        "option_cues": cue_metrics,
    })
    write_json(ROOT / "PYQ-DEMAND-AUDIT.json", {
        "schema_version": 4, "latest_repository_year": 2026,
        "sources": {"2018_2025": file_info(SOURCES["pyq_2018_2025"]), "2026": file_info(SOURCES["pyq_2026"])},
        "primary_count": len(PYQS), "supporting_count": len(SUPPORTING_PYQS),
        "primary": practice_data["primary"], "supporting": practice_data["supporting"],
        "original_count": len(practice_data["originals"]), "originals": practice_data["originals"],
        "word_bands": {"10": [150,200], "15": [250,300], "20": [340,400]},
    })

    ledger_rows = "\n".join(f"| `{row['id']}` | {row['source']} | {row['heading'].replace('|','/')} | {row['classification']} | `{row['own_payload_sha256']}` | {len(row['proposition_mappings'])} |" for row in decisions)
    matrix_rows = "\n".join(f"| `{cell['cell_id']}` | {cell['title']} | {cell['minimum_probes']} | {', '.join(cell['mapped_question_ids'])} | {', '.join(r['source_block_id'] for r in cell['authority_refs'])} |" for cell in cells_json)
    coverage = f"""# Yoga Coverage Ledger

## Frozen authority and provenance

- Mode: `formal_present_canonical_boundary_controlled`.
- Exact formal session: `{SOURCES['formal_session']}` — `{review['sources']['formal_session']['sha256']}`.
- Exact formal workbook: `{SOURCES['formal_workbook']}` — `{review['sources']['formal_workbook']['sha256']}`.
- Canonical Yoga controls topic boundaries; supplementary sources are depth-only.
- `{primary_authority['snapshot']['path']}` is user-approved primary-text authority for `YG-OB-077` only; it is not general formal/canonical authority.
- `YG-SK-BOUNDARY-001` is closed after serialized reconciliation. Topic 05 retains the complete Sāṃkhya metaphysical foundation; Yoga retains only its citta/path bridge.

## Exhaustive frozen preflight metrics

| Surface | Count |
|---|---:|
| Formal session H2-H4 blocks | {len(formal_session)} |
| Formal workbook H2-H4 blocks | {len(formal_workbook)} |
| Canonical H2-H4 blocks | {len(canonical)} |
| Supplementary depth H2-H4 blocks | {len(supplementary)} |
| Meaningful raw mappings | {len(raw_mappings)} |
| Unique normalized propositions | {len(registry)} |
| Duplicate occurrences / groups | {len(raw_mappings)-len(registry)} / {duplicate_groups} |
| Excluded structural coordinates | {len(excluded_fragments)} |
| Diagram structural exclusions | {diagram_structural_exclusions} |
| Panels | {len(panels)} |
| Large leaves / segments | {review['large_leaf_count']} / {review['large_leaf_segment_count']} |
| Mandatory block classifications | {json.dumps(obligation_inventory['block_classification_counts'], ensure_ascii=False)} |
| Mandatory proposition classifications | {json.dumps(obligation_inventory['proposition_classification_counts'], ensure_ascii=False)} |
| Independently derived atomic obligations | {len(obligation_inventory['obligations'])} |
| Test cells / MCQs | {len(cells_json)} / {len(QBANK)} |
| Primary / supporting PYQs | {len(PYQS)} / {len(SUPPORTING_PYQS)} |
| Original complete models | {len(ORIGINALS)} |

## Test matrix

`TESTABLE-OBLIGATIONS.json` classifies every mandatory block and meaningful proposition before cells or questions exist. Cells are then created from its atomic obligations, and questions are authored last. The 32 historical formal/workbook MCQs are evidence only, never a fixed target. Only title/stem plus keyed option and keyed explanation can satisfy a cell.

| Cell | Discriminator | Minimum | Questions | Authority blocks |
|---|---|---:|---|---|
{matrix_rows}

## Complete block ledger

| Stable block ID | Source | Heading | Classification | Parent-only hash | Propositions |
|---|---|---|---|---|---:|
{ledger_rows}
"""
    (ROOT / "COVERAGE-LEDGER.md").write_text(coverage, encoding="utf-8", newline="\n")
    (ROOT / "README.md").write_text(f"""# Topic 06 — Yoga

This package uses repository-standard **formal-present** provenance. It preserves the exact formal session and workbook, treats canonical Yoga as the controlling boundary owner, and retains all supplementary sources as depth-only evidence.

The package-local Vivekananda 1896 Yoga Sūtra II.27 snapshot is narrowly promoted under the scope recorded in `PRIMARY-SOURCE-AUTHORITY.json`. It does not become general formal/canonical authority.

## Study order

1. `REVISION-GUIDE.md`
2. `MCQ-QUESTIONS.md`
3. `MCQ-SOLUTIONS.md`
4. `ANSWER-WRITING-TOOLKIT.md`
5. `PRACTICE-LOG.md`

## Integrity summary

- H2-H4 blocks: formal session {len(formal_session)}, formal workbook {len(formal_workbook)}, canonical {len(canonical)}, supplementary {len(supplementary)}.
- Matrix-derived MCQs: {len(QBANK)} across {len(cells_json)} cells; historical 32-question practice is evidence only.
- Independent obligation inventory: `TESTABLE-OBLIGATIONS.json`, covering all {len(mandatory_blocks)} mandatory blocks and {obligation_inventory['mandatory_proposition_occurrence_count']} meaningful mandatory proposition occurrences.
- PYQs: 8 primary Yoga, 1 supporting comparison, all independently solved; 6 original timed models.
- Exact answer bands: 10=150–200, 15=250–300, 20=340–400 words.
- Default build/validation is Markdown-only and never creates PDFs.
- `YG-SK-BOUNDARY-001` is closed after serialized reconciliation without transferring or duplicating Sāṃkhya ownership.

Run `python -B build_package.py`, `python -B run_negative_tests.py`, and `python -B validate_package.py`.
""", encoding="utf-8", newline="\n")
    (ROOT / "PRACTICE-LOG.md").write_text("""# Yoga Practice Log

| Date | Mode | Question / PYQ | Response | Error type | Repair | Retest due | Retest result |
|---|---|---|---|---|---|---|---|

Use this file for learner attempts only. The deterministic builder preserves this blank reusable template.
""", encoding="utf-8", newline="\n")
    (ROOT / "render_pdfs.py").write_text("""from __future__ import annotations
raise SystemExit("PDF generation is disabled for this Markdown-only focused rebuild.")
""", encoding="utf-8", newline="\n")
    (ROOT / ".gitattributes").write_text(
        "* text=auto eol=lf\n"
        "*.md text eol=lf\n"
        "*.json text eol=lf\n"
        "*.py text eol=lf\n"
        "source-snapshots/raw/PatanjaliYogaSutraSwamiVivekanandaSanEng_djvu.txt -text -whitespace\n"
        "source-snapshots/primary-patanjali-yoga-sutra-ii-27-vivekananda-1896.md -whitespace\n",
        encoding="utf-8",
        newline="\n",
    )

    artifacts = []
    artifact_paths = source_artifact_paths(primary_authority)
    for rel in artifact_paths:
        path = ROOT / rel
        artifacts.append({"file": rel, "sha256": sha_bytes(path.read_bytes()), "bytes": path.stat().st_size})
    write_json(ROOT / "SOURCE-ARTIFACT-AUDIT.json", {
        "schema_version": 4, "policy": "markdown_and_machine_readable_audits_are_canonical_pdfs_prohibited_for_this_pass",
        "status": "CANONICAL_SOURCE_ARTIFACTS_CURRENT", "artifacts": artifacts,
        "approved_primary_source": {
            "scope": primary_authority["authority"]["kind"],
            "obligation_id": primary_authority["obligation_id"],
            "snapshot_path": primary_authority["snapshot"]["path"],
            "snapshot_sha256": primary_authority["snapshot"]["sha256"],
            "item_url": primary_authority["source_identity"]["item_url"],
            "object_url": primary_authority["source_identity"]["object_url"],
            "object_bytes": primary_authority["raw_object"]["bytes"],
            "object_sha256": primary_authority["raw_object"]["sha256"],
            "coordinate": [
                primary_authority["coordinate"]["line_start"],
                primary_authority["coordinate"]["line_end"],
            ],
            "payload_sha256": primary_authority["payload"]["sha256"],
        },
    })
    print(json.dumps({"formal_session": len(formal_session), "formal_workbook": len(formal_workbook), "canonical": len(canonical),
                      "supplementary": len(supplementary), "raw": len(raw_mappings), "unique": len(registry),
                      "duplicates": len(raw_mappings)-len(registry), "duplicate_groups": duplicate_groups,
                      "excluded": len(excluded_fragments), "panels": len(panels), "large_leaves": review["large_leaf_count"],
                      "segments": review["large_leaf_segment_count"], "cells": len(cells_json), "mcqs": len(QBANK)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
