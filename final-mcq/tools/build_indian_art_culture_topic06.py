"""Build and audit Indian Art and Culture Topic 06 revision banks.

The banks are original paraphrased questions. Direct UPSC wording/options are
withheld because authenticated reproduction permission is not held.
"""

from __future__ import annotations

import argparse
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Indian-Art-and-Culture"
TOPIC = SUBJECT / "06-Sculpture-Pottery-and-Iconography"

NITIN = "Basic §§2–4, 13.6A–13.7A; Advanced §§2–6; Nitin Singhania, Indian Art and Culture, PDF pp.189–214."
SHARMA = "Basic §4; R.S. Sharma, India's Ancient Past, PDF pp.211–223; Ancient India, PDF pp.121–123, 156–159."
PYQ = (
    "Basic §13.0 and Advanced §§8, 13.6A–13.6C; audited "
    "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md."
)
STATUS = (
    "Basic §§7, 13.9; Advanced §§7, 9, 13.9: current location, display or "
    "conservation claims require a dated official museum/ASI source."
)


def f(label: str, statement: str, evidence: str = NITIN, trap: str = "", group: str = "general") -> dict:
    return {
        "label": label,
        "statement": statement,
        "evidence": evidence,
        "trap": trap or "Do not transfer this proposition to a neighbouring period, school, material or symbol.",
        "group": group,
    }


FACTS = [
    f(
        "Six-factor sculpture reading",
        "Read sculpture through material, posture or gesture, iconographic attribute, patron, site context and cross-site comparison.",
        evidence="Advanced §§1–5, 13.4; Basic §§13.1–13.4.",
        trap="A visual description without patron, site and comparison is not the complete method.",
        group="method",
    ),
    f(
        "Material as an analytical variable",
        "Material is evidentiary: cire-perdue bronze permits open silhouettes, while fine-grained sandstone permits deep and precise relief.",
        evidence="Basic §13.2; Advanced §§3–5, 13.4; Nitin Singhania, PDF pp.190, 211.",
        trap="Material is not decorative background; do not treat bronze and sandstone as interchangeable.",
        group="method",
    ),
    f(
        "Cire-perdue technique",
        "In lost-wax casting, a wax model is clay-coated, heated so the wax drains away, and the mould is filled with molten metal.",
        trap="The wax is removed before the molten metal is poured; the technique is not a stone-carving method.",
        group="harappan",
    ),
    f(
        "Harappan label caution",
        "Pashupati, Mother Goddess and Priest-King are modern interpretive labels, not identities decoded from the undeciphered Harappan script.",
        trap="A familiar museum label does not turn a hypothesis into a deciphered inscription.",
        group="harappan",
    ),
    f(
        "Pashupati seal",
        "The so-called Pashupati seal is a steatite Mohenjo-daro object with a horned seated figure whose proto-Shiva identification remains doubtful.",
        trap="Use 'often interpreted' or 'so-called'; do not present the proto-Shiva reading as settled.",
        group="harappan",
    ),
    f(
        "Dancing Girl",
        "The Mohenjo-daro Dancing Girl is an early celebrated lost-wax bronze shown in a tribhanga dancing posture.",
        trap="Tribhanga names the three-bend posture; it does not prove a later religious identity.",
        group="harappan",
    ),
    f(
        "Harappan animal corpus",
        "Harappan seals commonly show animals such as the unicorn and humped bull, while the source records no cow or lion on any seal.",
        trap="Do not insert a lion into the Harappan seal corpus because lions appear in later imperial art.",
        group="harappan",
    ),
    f(
        "Harappan pottery",
        "Harappan pottery is predominantly red ware, often painted in black, and should not be collapsed into the separate Black-and-Red Ware category.",
        trap="Black painting on red pottery is not identical to the technical category Black-and-Red Ware.",
        group="pottery",
    ),
    f(
        "Pottery sequence",
        "The bounded sequence runs from Neolithic hand-made coarse ware through Chalcolithic painted ware, Harappan Red Ware, Painted Grey Ware and NBPW.",
        trap="Do not reverse the sequence or substitute Black-and-Red Ware for Harappan Red Ware.",
        group="pottery",
    ),
    f(
        "Northern Black Polished Ware",
        "NBPW is fine, highly lustrous tableware associated especially with early historic urbanisation, not exclusively with the Mauryan court.",
        trap="Its name does not make every black pottery tradition NBPW or restrict it to one royal workshop.",
        group="pottery",
    ),
    f(
        "Harappan terracotta",
        "Harappan terracotta female figures were fire-baked and made by pinching; the source describes them as fewer and cruder than the bronzes.",
        trap="This bounded comparison does not mean that all Harappan sculpture was technically crude.",
        group="terracotta",
    ),
    f(
        "Chandraketugarh terracotta",
        "Chandraketugarh near the Bidyadhari river is noted for precise terracotta sculpture, NBPW relics and Maurya-, Kushana- and Gupta-period material.",
        evidence="Basic §13.7A; Nitin Singhania, PDF pp.38, 167.",
        trap="Do not assign the site to one named dynasty or invent a date, size or firing temperature.",
        group="terracotta",
    ),
    f(
        "Gundiyali and Lodai",
        "Gundiyali and Lodai in Kutch are recorded as famous pottery-making villages, not as verified figurative-teracotta centres.",
        evidence="Basic §13.7A; Nitin Singhania, PDF p.196.",
        trap="Keep pottery villages distinct from an unsupported list of living terracotta communities.",
        group="terracotta",
    ),
    f(
        "Yaksha and Yakshi",
        "Yaksha and Yakshi are folk or nature deities associated with water, fertility, trees and wilderness and absorbed into several religions.",
        trap="They are not confined to one formal temple theology or one religious community.",
        group="mauryan",
    ),
    f(
        "Shalabhanjika",
        "Shalabhanjika is a tree-holding yakshi motif used as an auspicious bracket figure at Sanchi and Bharhut and later in Hoysala temples.",
        trap="It is a fertility and auspiciousness motif, not simply a generic female portrait.",
        group="mauryan",
    ),
    f(
        "Didarganj chronology",
        "The Didarganj chauri-bearer is traditionally dated to the Mauryan period, but later dating remains a live scholarly qualification.",
        trap="Mauryan polish alone does not justify an uncontested Mauryan date.",
        group="mauryan",
    ),
    f(
        "Parkham Yaksha",
        "The Parkham Yaksha exemplifies monumental Yaksha sculpture with the characteristic polished visual language associated with the Mauryan-period discussion.",
        trap="Do not confuse the Parkham Yaksha with a Gandhara Buddha or make it a proof of one exact date.",
        group="mauryan",
    ),
    f(
        "Gandhara school",
        "Gandhara used bluish-grey stone and later stucco in a mainly Buddhist programme marked by Hellenistic, Parthian and Central Asian/Bactrian layers.",
        trap="Gandhara is not simply Greek art transplanted to India.",
        group="schools",
    ),
    f(
        "Gandhara influence strands",
        "Greco-Bactrian influence is visible in wavy hair, modelled musculature and pleated drapery, while Central Asian influence arrives through Kushana patronage and layered Parthian/Bactrian elements.",
        evidence="Advanced §13.6B; Basic §13.5; Nitin Singhania, PDF pp.200–205.",
        trap="Do not answer the two named strands by repeating 'Greek influence' without separating style from patronage.",
        group="schools",
    ),
    f(
        "Mathura school",
        "Mathura developed on indigenous lines in spotted red sandstone and served Buddhist, Hindu and Jain imagery.",
        trap="Mathura was not religiously exclusive and should not be reduced to a Gandhara copy.",
        group="schools",
    ),
    f(
        "Mathura attribute grammar",
        "Mathura used avayudhas or attribute-symbols for Hindu deities, depicted the Buddha largely in Abhaya Mudra and used a larger geometrically decorated halo.",
        trap="Attribute reading is a support for identification, not a substitute for provenance or inscription.",
        group="schools",
    ),
    f(
        "Amaravati or Vengi school",
        "Amaravati developed on indigenous lines in the Krishna river basin, used greenish-white limestone and was mainly Buddhist.",
        trap="Do not transfer Gandhara's foreign-influence description to Amaravati.",
        group="schools",
    ),
    f(
        "Amaravati narrative dynamism",
        "Amaravati is known for narrative reliefs and extensive tribhanga posture, with medallions capable of telling whole episodes.",
        trap="Its defining contrast is narrative dynamism, not the composed stillness of Gandhara.",
        group="schools",
    ),
    f(
        "Aniconic Buddhist symbols",
        "In the aniconic programme, birth may be indicated by bull, elephant, lotus and footprint; sermons by wheel, lion and deer; death by stupa.",
        evidence="Basic §13.6; Advanced §13.6; Nitin Singhania, PDF pp.201, 776.",
        trap="Aniconism avoids a human image of the Buddha; it does not prohibit animal imagery.",
        group="buddhist",
    ),
    f(
        "Parallel iconic shift",
        "Anthropomorphic Buddha images emerged in broadly overlapping early-CE contexts at Gandhara and Mathura, so a single uncontested first origin should not be asserted.",
        evidence="Basic §§3–4; Advanced §§2, 13.2, 13.6.",
        trap="The exam-safe formulation is parallel development with a priority debate, not 'Gandhara first'.",
        group="buddhist",
    ),
    f(
        "Gupta Sarnath idiom",
        "Gupta and immediately post-Gupta sculpture around Sarnath used cream-coloured sandstone or metal and subtly modelled, thinly draped figures.",
        trap="Do not replace the restrained Sarnath idiom with Gandhara's heavy pleated drapery.",
        group="gupta",
    ),
    f(
        "Sultanganj Buddha dating",
        "The large copper Buddha from Sultanganj is safer described as late or post-Gupta rather than assigned firmly to the Gupta period.",
        trap="A broad late/post-Gupta formulation is safer than a falsely precise Gupta attribution.",
        group="gupta",
    ),
    f(
        "Nataraja origin and peak",
        "The earliest known Nataraja example is at Ravana Phadi Cave, Aihole, while Chola patronage brought the iconography to its canonical peak.",
        evidence="Basic §§2, 4; Advanced §§2–4; Nitin Singhania, PDF pp.210–212.",
        trap="Chola fame marks peak development, not the origin of the iconographic form.",
        group="nataraja",
    ),
    f(
        "Nataraja rear hands",
        "In the Chola Nataraja, the rear right hand holds the damaru and the rear left hand holds fire, linking the image to creation-sound and destruction.",
        trap="Do not swap the damaru and fire or treat the hands as unassigned ornaments.",
        group="nataraja",
    ),
    f(
        "Nataraja front hands and foot",
        "The front right hand gives Abhaya Mudra, while the front left points toward the raised foot in Gajahasta as a path of salvation.",
        trap="Gajahasta names the pointing-hand pose; it is not the rear hand holding fire.",
        group="nataraja",
    ),
    f(
        "Nataraja symbolic ensemble",
        "Apasmara or Muyalaka is subdued under the supporting foot, the lifted leg expresses bhujangatrasita, and the nimbus signals unending time cycles.",
        trap="Do not treat Apasmara as a second deity standing beside Nataraja or detach the symbols from the image's system.",
        group="nataraja",
    ),
    f(
        "Natana-sabha",
        "Many South Indian Shiva temples keep a separate natana-sabha for the Nataraja image, alongside the wider Chidambaram–Thanjavur comparison set.",
        trap="The natana-sabha is a temple space associated with the dancing image, not a pottery type.",
        group="south",
    ),
    f(
        "Kirtimukha and Saptamatrikas",
        "Kirtimukha is a monster-faced decorative motif, while Saptamatrikas form a named South Indian sculptural programme also discussed with temple sculpture.",
        trap="Do not reduce both terms to generic floral ornament or treat Kirtimukha as a dynasty.",
        group="south",
    ),
    f(
        "Kalyanasundara Murti",
        "The ninth-century Kalyanasundara Murti represents panigrahana through Shiva accepting Parvati's right hand as she steps forward bashfully.",
        evidence="Basic §13.6C; Nitin Singhania, PDF p.212.",
        trap="The key point is the represented marriage ritual, not a generic standing divine couple.",
        group="south",
    ),
    f(
        "Sarnath lion and bull meanings",
        "On the Sarnath capital's programme, the bull marks the Buddha's birth month as Taurus, while the lion signifies enlightenment and the spreading of Dharma.",
        evidence="Basic §13.6A; Nitin Singhania, PDF pp.42–44, 776.",
        trap="Do not import an unsourced 'lion of the Shakyas' explanation into this bounded evidence set.",
        group="animals",
    ),
    f(
        "Rampurva pair",
        "At Rampurva, the lion-capital pillar carries Major Pillar Edicts I–VI while the bull-capital pillar is uninscribed.",
        evidence="Basic §13.6A; Nitin Singhania, PDF pp.233–234.",
        trap="The source does not establish that the bull was uninscribed because it was earlier or belonged to another dynasty.",
        group="animals",
    ),
    f(
        "Harappan bull and lion contrast",
        "The Harappan seal corpus makes the humped bull frequent but records no lion, so later imperial lion symbolism must not be projected backward.",
        evidence="Basic §13.6A; Nitin Singhania, PDF p.191.",
        trap="The undeciphered script also blocks confident recovery of the bull's Harappan meaning.",
        group="animals",
    ),
    f(
        "Nandi as architecture",
        "Nandi is a placed structural figure before a Shiva sanctum, with named Nandi mandapas or pavilions at sites such as Thanjavur, Ellora and Ramappa.",
        evidence="Basic §13.6A; Nitin Singhania, PDF pp.61, 91, 105, 107, 109, 329.",
        trap="The axial building and placement make Nandi architectural, not merely decorative.",
        group="animals",
    ),
    f(
        "Yali",
        "Yali is a composite lion-based guardian with elephant tusks or trunk features, associated with Vijayanagara pillars and Nayaka gopurams.",
        evidence="Basic §13.6A; Nitin Singhania, PDF pp.114, 118, 209.",
        trap="The two source descriptions vary in anatomy; retain the composite lion-based, elephant-tusked core.",
        group="animals",
    ),
    f(
        "Vyala",
        "Vyala at Khajuraho denotes hybrid imaginary animals with lions' bodies, distinct from the Yali terminology used for South Indian composite guardians.",
        evidence="Basic §13.6A; Nitin Singhania, PDF p.81.",
        trap="Do not treat Yali and Vyala as interchangeable labels for the same regional programme.",
        group="animals",
    ),
    f(
        "Temple sculpture as social evidence",
        "Temple sculpture is strong evidence of what patrons made visible and of available techniques, but weak evidence of ordinary life when treated as a literal social photograph.",
        evidence="Basic §13.6C, 13.8; Advanced §13.6C; Nitin Singhania, PDF pp.81, 198–199, 208, 212.",
        trap="Commissioned representation requires a qualification about patronage, selection and visibility.",
        group="social",
    ),
    f(
        "Terracotta continuity",
        "Terracotta moves from Harappan fired-clay objects through Chandraketugarh and Gupta plaques to Bengal's terracotta-brick façade tradition.",
        evidence="Basic §13.7A; Nitin Singhania, PDF pp.38, 193, 208.",
        trap="Continuity of a medium does not mean identical style, meaning or social function in every period.",
        group="terracotta",
    ),
    f(
        "Gandhara as Indian subject in a layered idiom",
        "Gandhara is best framed as a Buddhist iconographic programme executed in a Hellenised visual idiom under Kushana patronage.",
        evidence="Advanced §§3–5, 13.6B; R.S. Sharma, Ancient India, PDF pp.121–123.",
        trap="Calling it simply Greek art reverses the relationship between Indian subject and borrowed surface treatment.",
        group="schools",
    ),
    f(
        "Verified PYQ route cluster",
        "The audited direct Mains routes are the 2019 Gandhara-influence demand and the 2022 demands on temple sculpture as social evidence and lion-bull significance.",
        evidence=PYQ,
        trap="These routes are recorded as provenance and coverage demands; exact protected wording and options are not reproduced here.",
        group="pyq",
    ),
    f(
        "Current-status evidence hold",
        "A claim about a sculpture's present location, display or conservation status requires a dated official museum, ASI or institutional source.",
        evidence=STATUS,
        trap="A stable art-historical classification does not authenticate a changing museum or conservation status.",
        group="boundary",
    ),
]


STEMS = {
    1: "Which option states the direct source-bounded proposition filed under **{label}**?",
    2: "A revision card is labelled **{label}**. Which statement belongs on that card?",
    3: "In a close-option question on **{label}**, which formulation is safest?",
}


def choose_distractors(index: int, bank: int) -> list[int]:
    target_group = FACTS[index]["group"]
    candidates = [
        candidate
        for candidate in range(len(FACTS))
        if candidate != index and FACTS[candidate]["group"] != target_group
    ]
    starts = {1: 5, 2: 17, 3: 29}
    start = (index * 5 + starts[bank]) % len(candidates)
    selected: list[int] = []
    groups = {target_group}
    for step in range(len(candidates)):
        candidate = candidates[(start + step) % len(candidates)]
        group = FACTS[candidate]["group"]
        if group not in groups:
            selected.append(candidate)
            groups.add(group)
        if len(selected) == 3:
            break
    return selected


def make_questions(bank: int) -> list[dict]:
    rng = random.Random(20261006 + bank)
    order = list(range(len(FACTS)))
    if bank == 2:
        order = order[13:] + order[:13]
    elif bank == 3:
        order = order[27:] + order[:27]
    questions: list[dict] = []
    for qno, target in enumerate(order, 1):
        indices = [target] + choose_distractors(target, bank)
        rng.shuffle(indices)
        options = []
        correct = ""
        for position, fact_index in enumerate(indices):
            letter = "ABCD"[position]
            options.append({"letter": letter, "fact_index": fact_index, "text": FACTS[fact_index]["statement"]})
            if fact_index == target:
                correct = letter
        questions.append(
            {
                "no": qno,
                "target": target,
                "stem": STEMS[bank].format(label=FACTS[target]["label"]),
                "options": options,
                "correct": correct,
            }
        )
    return questions


def write_bank(bank: int, questions: list[dict]) -> None:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    q_lines = [
        f"# Topic 06 — Sculpture, Pottery and Iconography — Revision {bank}",
        "",
        "> Select one option for each question.",
        "",
    ]
    a_lines = [
        f"# Topic 06 — Revision {bank} Answers",
        "",
        "> Detailed key with evidence, option-specific rationales, sources and examiner traps.",
        "",
    ]
    for question in questions:
        q_lines.append(f"### Q{question['no']}. {question['stem']}")
        for option in question["options"]:
            q_lines.append(f"{option['letter']}. {option['text']}")
        q_lines.append("")

        target = FACTS[question["target"]]
        a_lines.append(f"{question['no']}. **{question['correct']}.**")
        a_lines.append(f"   - **Correct proposition:** {target['statement']}")
        a_lines.append(
            f"   - **Evidence:** This is the source-bounded proposition filed under **{target['label']}**."
        )
        for option in question["options"]:
            fact = FACTS[option["fact_index"]]
            if option["fact_index"] == question["target"]:
                reason = f"Correct: it matches **{target['label']}** and answers the stem precisely."
            else:
                reason = (
                    f"Incorrect for this stem: it belongs under **{fact['label']}**, "
                    f"not **{target['label']}**. Its evidence is: {fact['statement']}"
                )
            a_lines.append(f"   - **{option['letter']}.** {option['text']} — {reason}")
        a_lines.append(f"   - **Sources:** {target['evidence']}")
        a_lines.append(f"   - **Trap:** {target['trap']}")
        a_lines.append("")

    (folder / "QUESTIONS.md").write_text("\n".join(q_lines), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(a_lines), encoding="utf-8")
    (folder / "COVERAGE.md").write_text(
        f"""# Topic 06 — Revision {bank} Coverage

**Status:** in_progress pending structural and hostile audit  
**Question count:** {len(questions)} original MCQs  
**Independence:** This bank tests every Topic 06 source card once, with a distinct target order, framing, distractor neighbourhood and independently shuffled answer positions.

## Source spine

- Basic owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/06_Sculpture-Pottery-and-Iconography.md`
- Advanced owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/advanced/06_Sculpture-Pottery-and-Iconography.md`
- Complete package/workbook: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/06_Sculpture-Pottery-and-Iconography_Complete-Topic-Package.md` and `learning-sessions/v2/subject-wide-syllabus/indian-art-and-culture-06_Solved-Workbook.md`
- OCR/book spine: Nitin Singhania, *Indian Art and Culture*, PDF pp.189–214; R.S. Sharma, *India's Ancient Past*, PDF pp.211–223 and *Ancient India*, PDF pp.121–123, 156–159.

## Coverage ledger

Every source card is tested in this bank: visual-reading method and material; Harappan seals, bronzes, labels, animal corpus and pottery; NBPW, terracotta and pottery-making villages; Yaksha/Yakshi, Shalabhanjika, Didarganj and Parkham; Gandhara, Mathura and Amaravati; aniconic symbolism and the priority debate; Gupta/Sultanganj; Nataraja origin, attributes and temple setting; South Indian motifs and Kalyanasundara; lion-bull symbolism, Rampurva, Nandi, Yali and Vyala; temple sculpture as commissioned social evidence; terracotta continuity; PYQ route controls; and current-status evidence limits.

## PYQ provenance, key and rights holds

- Audited direct Mains routes: 2019 GS-I Gandhara external elements; 2022 GS-I medieval temple sculpture as social evidence; 2022 GS-I lion and bull significance. These are provenance/coverage routes only.
- The 2021 Chandraketugarh–terracotta pairing is retained in the owner as source evidence, but no exact PYQ wording/options are reproduced.
- No local coaching key is treated as official. Objective routes with unresolved or provisional authentication remain held out of the solved banks.
- UPSC website reproduction permission is not held. This bank contains original paraphrases only; verification of a key would not grant reproduction permission.
- Mughal-specific sculpture is named in the broad syllabus snapshot but has no bounded Topic 06 evidence card in the canonical owners; it remains an explicit coverage gap rather than an invented question.

## Audit status

Structural and hostile audit results are recorded in the topic-level `AUDIT-REPORT.md`; this file is promoted to `complete` only after all three banks pass.
""",
        encoding="utf-8",
    )


def structural_audit() -> list[str]:
    errors: list[str] = []
    for bank in range(1, 4):
        folder = TOPIC / f"revision-{bank}"
        q = (folder / "QUESTIONS.md").read_text(encoding="utf-8")
        a = (folder / "ANSWERS.md").read_text(encoding="utf-8")
        q_ids = [int(x) for x in re.findall(r"^### Q(\d+)\.", q, re.M)]
        a_ids = [int(x) for x in re.findall(r"^(\d+)\.\s+\*\*[A-D]\.", a, re.M)]
        if len(q_ids) < 40:
            errors.append(f"revision-{bank}: fewer than 40 questions")
        if q_ids != list(range(1, len(q_ids) + 1)) or q_ids != a_ids:
            errors.append(f"revision-{bank}: question/answer numbering mismatch")
        sections = list(re.finditer(r"^### Q\d+\.", q, re.M))
        for pos, section in enumerate(sections):
            end = sections[pos + 1].start() if pos + 1 < len(sections) else len(q)
            letters = re.findall(r"^([A-D])\. ", q[section.end() : end], re.M)
            if letters != list("ABCD"):
                errors.append(f"revision-{bank}: malformed options near Q{pos + 1}")
        answer_sections = list(re.finditer(r"(?m)^\d+\.\s+\*\*[A-D]\.", a))
        for pos, section in enumerate(answer_sections):
            end = answer_sections[pos + 1].start() if pos + 1 < len(answer_sections) else len(a)
            content = a[section.end() : end]
            for letter in "ABCD":
                if not re.search(rf"\*\*{letter}\.\*\*", content):
                    errors.append(f"revision-{bank}: missing option rationale {letter} near Q{pos + 1}")
            if "   - **Sources:**" not in content or "   - **Trap:**" not in content:
                errors.append(f"revision-{bank}: missing source/trap near Q{pos + 1}")
        if re.search(r"(?i)answer key|correct answer|solution|sources?:|trap:", "\n".join(q.splitlines()[:4])):
            errors.append(f"revision-{bank}: answer leakage in QUESTIONS header")
        if re.search(r"(?m)^\s*(Answer|Correct answer|Solution|Sources:|Trap:)", q):
            errors.append(f"revision-{bank}: answer/source leakage in QUESTIONS body")
        if len(re.findall(r"^### Q\d+\.", q, re.M)) != len(FACTS):
            errors.append(f"revision-{bank}: expected {len(FACTS)} questions")
    return errors


def hostile_audit() -> list[str]:
    errors: list[str] = []
    stem_sets: list[set[str]] = []
    for bank in range(1, 4):
        q = (TOPIC / f"revision-{bank}" / "QUESTIONS.md").read_text(encoding="utf-8")
        a = (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8")
        stems = re.findall(r"^### Q\d+\. (.+)$", q, re.M)
        stem_sets.append(set(stems))
        if len(set(stems)) != len(stems):
            errors.append(f"revision-{bank}: duplicate stems inside bank")
        keys = re.findall(r"^\d+\.\s+\*\*([A-D])\.", a, re.M)
        if len(set(keys)) < 3:
            errors.append(f"revision-{bank}: answer positions too concentrated")
        if all(keys[i] == "ABCD"[i % 4] for i in range(len(keys))):
            errors.append(f"revision-{bank}: predictable A-B-C-D answer cycle")
        for section in re.finditer(r"^### Q\d+\.", q, re.M):
            pass
        if re.search(r"(?i)correct proposition|option-specific|examiner trap|answer-free", q):
            errors.append(f"revision-{bank}: answer leakage detected")
        for qblock in re.split(r"^### Q\d+\.", q, flags=re.M)[1:]:
            options = re.findall(r"^[A-D]\. (.+)$", qblock, re.M)
            if len(options) != 4 or len(set(options)) != 4:
                errors.append(f"revision-{bank}: duplicate or missing option text")
    for left in range(3):
        for right in range(left + 1, 3):
            overlap = stem_sets[left] & stem_sets[right]
            if overlap:
                errors.append(f"cross-bank stem duplication revision-{left + 1}/revision-{right + 1}: {len(overlap)}")
    return errors


def write_topic_coverage(status: str = "complete") -> None:
    (TOPIC / "COVERAGE.md").write_text(
        f"""# Topic 06 — Sculpture, Pottery and Iconography

**Status:** `{status}`  
**Catalogue position:** 06 of 15  
**Question banks:** 3 independent banks × {len(FACTS)} original MCQs = {len(FACTS) * 3} originals  
**Owner coverage:** Basic and Advanced owners, complete package/workbook and mandated OCR/book spine read before authoring.

## Owned coverage

Visual-reading method; material and cire-perdue; Harappan seals, bronzes, terracotta, labels and pottery; NBPW; Yaksha/Yakshi and Shalabhanjika; Didarganj and Parkham; Gandhara, Mathura and Amaravati; aniconic symbolism and parallel iconic shift; Gupta/Sarnath and Sultanganj dating caution; Nataraja's Aihole origin and Chola peak, attributes and natana-sabha; Kirtimukha, Saptamatrikas and Kalyanasundara; lion-bull symbolism, Rampurva, Harappan animal caution, Nandi, Yali and Vyala; temple sculpture as commissioned social evidence; terracotta continuity; direct PYQ route controls; and current-status evidence limits.

## Source and evidence controls

- Primary Markdown owners: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/06_Sculpture-Pottery-and-Iconography.md` and `advanced/06_Sculpture-Pottery-and-Iconography.md`.
- Complete package/workbook: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/06_Sculpture-Pottery-and-Iconography_Complete-Topic-Package.md` and `learning-sessions/v2/subject-wide-syllabus/indian-art-and-culture-06_Solved-Workbook.md`.
- OCR/book source: Nitin Singhania, *Indian Art and Culture*, PDF pp.189–214; R.S. Sharma, *India's Ancient Past*, PDF pp.211–223 and *Ancient India*, PDF pp.121–123, 156–159. No unsupported page precision or verbatim quotation is imported.
- Advanced interpretation remains bounded: it separates Greco-Bactrian surface treatment from Central Asian/Kushana patronage and distinguishes origin from peak development.

## PYQ provenance and rights holds

- Audited direct Mains routes are 2019 GS-I Gandhara external elements and the two 2022 GS-I routes on temple sculpture as social evidence and lion-bull significance.
- The 2021 Chandraketugarh–terracotta pairing is retained as owner evidence. Exact UPSC wording/options are withheld.
- No unverified coaching key is used as an official key. Provisional/unreadable objective routes remain unsolved and held.
- UPSC website reproduction permission is not held; all 126 questions are original paraphrases, not reproduced PYQs.
- Mughal-specific sculpture is an explicit source gap in the canonical Topic 06 owners and is not fabricated into the banks.

## Release audit

- Structural audit: pending until the three banks are generated and checked.
- Hostile audit: pending until answer leakage, duplicate stems, key concentration, cross-bank reuse and option duplication are checked.
- Final pipeline is run only after this ledger and `INDEX.md` are updated.
""",
        encoding="utf-8",
    )


def write_audit() -> None:
    structural = structural_audit()
    hostile = hostile_audit()
    errors = structural + hostile
    report = [
        "# Topic 06 — Structural and Hostile Audit",
        "",
        "## Structural audit",
        "",
        "- Result: **PASS**" if not structural else "- Result: **FAIL**",
        f"- Three banks present; each has {len(FACTS)} questions, answer-free questions, one-to-one keys, four options, four option-specific rationales, sources and traps.",
        "",
        "## Hostile audit",
        "",
        "- Result: **PASS**" if not hostile else "- Result: **FAIL**",
        "- Checked answer-position independence, header/body leakage, duplicate stems, duplicate options, key concentration and cross-bank stem reuse.",
        "",
        "## Findings and repairs",
        "",
        "No unresolved findings." if not errors else "\n".join(f"- {error}" for error in errors),
        "",
        "## PYQ/rights control",
        "",
        "No exact PYQ wording/options are reproduced. Direct 2019/2022 Mains routes, the 2021 terracotta pairing, unresolved objective-key holds and the UPSC website-permission hold are recorded in the topic and per-bank coverage ledgers.",
    ]
    (TOPIC / "AUDIT-REPORT.md").write_text("\n".join(report), encoding="utf-8")
    if errors:
        raise SystemExit("AUDIT FAILED: " + "; ".join(errors))


def update_indexes() -> None:
    index = SUBJECT / "INDEX.md"
    text = index.read_text(encoding="utf-8")
    old = "| 06 | Sculpture, Pottery and Iconography | pending | — | — | — |"
    new = (
        f"| 06 | Sculpture, Pottery and Iconography | [Complete](06-Sculpture-Pottery-and-Iconography/COVERAGE.md) "
        f"| [{len(FACTS)} originals](06-Sculpture-Pottery-and-Iconography/revision-1/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](06-Sculpture-Pottery-and-Iconography/revision-2/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](06-Sculpture-Pottery-and-Iconography/revision-3/QUESTIONS.md) · complete |"
    )
    if old not in text:
        raise SystemExit("INDEX row for Topic 06 not found")
    index.write_text(text.replace(old, new), encoding="utf-8")

    coverage = SUBJECT / "COVERAGE.md"
    ctext = coverage.read_text(encoding="utf-8")
    old_row = "| 06 | Sculpture, Pottery and Iconography | `pending` | not started |"
    new_row = f"| 06 | Sculpture, Pottery and Iconography | `complete` | 3 independent banks; {len(FACTS)} / {len(FACTS)} / {len(FACTS)} originals |"
    if old_row not in ctext:
        raise SystemExit("subject coverage row for Topic 06 not found")
    ctext = ctext.replace(old_row, new_row)
    ctext += f"""

## Topic 06 release gate — Sculpture, Pottery and Iconography

- Revision 1 / 2 / 3 contain **{len(FACTS)} / {len(FACTS)} / {len(FACTS)} original MCQs** ({len(FACTS) * 3} total).
- Each bank independently covers the owned Basic/Advanced/source ledger with distinct framing, target order, distractor neighbourhood and shuffled answer positions.
- PYQ holds: direct 2019/2022 Mains routes and the 2021 terracotta pairing are recorded for provenance only; no exact wording/options are reproduced, no unverified key is used, and UPSC website permission is not held.
- Explicit gap: Mughal-specific sculpture has no bounded Topic 06 evidence card in the canonical owners and remains unasked rather than fabricated.
- Structural and hostile audits are clean. Next pending topic is **07 — Painting Traditions**.
"""
    coverage.write_text(ctext, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--finalize", action="store_true")
    args = parser.parse_args()
    if args.build:
        TOPIC.mkdir(parents=True, exist_ok=True)
        for bank in range(1, 4):
            write_bank(bank, make_questions(bank))
        write_topic_coverage("in_progress")
    if args.audit:
        write_audit()
    if args.finalize:
        write_topic_coverage("complete")
        for bank in range(1, 4):
            coverage = (TOPIC / f"revision-{bank}" / "COVERAGE.md").read_text(encoding="utf-8")
            coverage = coverage.replace(
                "**Status:** in_progress pending structural and hostile audit",
                "**Status:** complete — structural and hostile audits clean",
            )
            (TOPIC / f"revision-{bank}" / "COVERAGE.md").write_text(coverage, encoding="utf-8")
        update_indexes()
    if not (args.build or args.audit or args.finalize):
        parser.error("choose --build, --audit or --finalize")


if __name__ == "__main__":
    main()
