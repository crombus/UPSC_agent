"""Build and audit Indian Art and Culture Topic 08 revision banks.

All questions are original paraphrases. Exact UPSC wording/options are
withheld because reproduction permission is not held.
"""

from __future__ import annotations

import argparse
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Indian-Art-and-Culture"
TOPIC = SUBJECT / "08-Indian-Music"

NITIN = "Basic §§2–6, 13.4–13.10; Nitin Singhania, Indian Art and Culture, PDF pp.411–457."
OCR = (
    "R.S. Sharma, India's Ancient Past, PDF pp.347–355; "
    "Satish Chandra, History of Medieval India, PDF pp.332–334; "
    "Satish Chandra, Medieval History, 1526–1748, Part 2, PDF pp.394–395."
)
WORKBOOK = (
    "Complete package/workbook: "
    "`upsc-ai-kit/knowledge/Indian-Art-and-Culture/08_Indian-Music_Complete-Topic-Package.md` "
    "and `learning-sessions/v2/subject-wide-syllabus/indian-art-and-culture-08_Solved-Workbook.md`."
)
PYQ_HOLD = (
    "Basic §§7, 13.10 and routed ledgers: 2018 GS-I Q44 (Tyagaraja/Annamacharya), "
    "2019 GS-I Q16 (Tansen), 2025 GS-I Q18 (Gandharva Mahavidyalaya), and provisional "
    "2026 GS-I Q1 (raga equivalence) and Q19 (Mallikarjun Mansur/gharanas)."
)
RIGHTS_HOLD = (
    "Exact UPSC wording/options are withheld because UPSC website reproduction permission "
    "is not held; unavailable or provisional keys are not inferred and no coaching key is "
    "treated as official."
)


def f(label: str, statement: str, evidence: str = NITIN, trap: str = "", group: str = "general") -> dict:
    return {
        "label": label,
        "statement": statement,
        "evidence": evidence,
        "trap": trap or "Do not transfer this proposition to a neighbouring term, form, instrument or tradition.",
        "group": group,
    }


FACTS = [
    f("Saptaswara", "Saptaswara comprises Shadja, Rishabha, Gandhara, Madhyama, Panchama, Dhaivata and Nishada (Sa–Re–Ga–Ma–Pa–Dha–Ni).", group="theory"),
    f("Shruti boundary", "Shruti and swara should not be collapsed: the source treats shruti as a finer pitch concept, while saptaswara names the seven-note base scale.", group="theory"),
    f("Raga", "A raga is a specific melodic entity with characteristic ascent-descent, note hierarchy and a tradition-specific association with time, season or rasa.", group="theory"),
    f("Thaat", "A Hindustani thaat is an unsung parent scale of seven notes, stated in ascending order and without vaadi-samvadi or emotional identity.", group="theory"),
    f("Thaat-raga distinction", "A raga may use five, six or seven notes and has melodic personality; a thaat is a classificatory parent scale and is not sung as a raga.", group="theory"),
    f("Tala", "Tala is the recurring rhythmic cycle that organises musical time; it is not a synonym for raga or laya.", group="theory"),
    f("Laya", "Laya concerns the tempo or flow of rhythmic movement, whereas tala is the patterned cycle within which that movement is organised.", group="theory"),
    f("Melakarta", "Carnatic theory uses 72 sampurna parent melakartas, from which janya or derived ragas are formed.", group="theory"),
    f("Janya raga", "A janya raga is a derived Carnatic raga related to a melakarta parent and should not be equated with a Hindustani thaat.", group="theory"),
    f("Rasa-raga linkage", "Raga-time, season and rasa associations form an aesthetic convention linked to musical tradition, not a universal acoustical law.", group="aesthetics"),
    f("Natyashastra", "Bharata's Natyashastra discusses music together with drama and supplies an important shared aesthetic-theory anchor.", group="treatise"),
    f("Brihaddeshi", "Matanga's Brihaddeshi is associated with an early focused definition of the term raga.", group="treatise"),
    f("Sangita Ratnakara", "Sharngadeva's 13th-century Sangita Ratnakara is a major authority written before the later Hindustani-Carnatic bifurcation.", group="treatise"),
    f("Chaturdandi Prakashika", "Venkatamakhin's Chaturdandi Prakashika underlies the melakarta approach in Carnatic music.", group="treatise"),
    f("Bhatkhande", "V.N. Bhatkhande systematised modern Hindustani pedagogy through the thaat-based classification.", group="modern_pedagogy"),
    f("Gandharva Mahavidyalaya", "V.D. Paluskar set up the Gandharva Mahavidyalaya in 1901 expressly to teach music.", group="modern_pedagogy"),
    f("Shared roots", "Hindustani and Carnatic music draw on older shared theory but differ in repertoire, ornament, classification and performance sequence.", group="comparison"),
    f("Hindustani ecology", "Hindustani music developed through North Indian temple, devotional, Sultanate-Mughal and regional-court networks, including Persianate encounters.", group="comparison"),
    f("Carnatic ecology", "Carnatic music crystallised through South Indian temple and court networks and later sabha institutions.", group="comparison"),
    f("Hindustani improvisation", "Alap, bol-bant, taan and layakari are among the improvisational resources of Hindustani practice.", group="comparison"),
    f("Carnatic improvisation", "Carnatic manodharma includes alapana, niraval, kalpana swara, tanam and ragam-tanam-pallavi; it is not improvisation-free.", group="comparison"),
    f("Dhrupad", "Dhrupad is an old Hindustani vocal form associated in the source with Mian Tansen and with the Dagar tradition.", group="hindustani_form"),
    f("Khayal", "Khayal is a major Hindustani vocal form whose later courtly strengthening is associated with Sadarang and Adarang under Muhammad Shah.", group="hindustani_form"),
    f("Thumri", "Thumri is a named semi-classical Hindustani style and must not be treated as an instrument or a gharana.", group="hindustani_form"),
    f("Tappa", "Tappa is a distinct named semi-classical Hindustani vocal style rather than a parent scale.", group="hindustani_form"),
    f("Ghazal and tarana", "Ghazal and tarana are named Hindustani vocal styles with distinct performance registers; neither is a synonym for tala.", group="hindustani_form"),
    f("Gharana ecology", "A gharana is a family- or lineage-based transmission and patronage ecology that concentrated specialised skill and adapted to concert, radio, teaching and recording.", group="gharana"),
    f("Dagar gharana", "Dagar is associated with Dagar Vani and Dhrupad.", group="gharana"),
    f("Darbhanga gharana", "Darbhanga is associated with Khandar Vani and an equal focus on alap and layakari.", group="gharana"),
    f("Gwalior gharana", "Gwalior is identified as the oldest khayal gharana, with balanced emphasis across its elements.", group="gharana"),
    f("Kirana gharana", "Kirana is marked by precise swara focus and is associated in the source with Abdul Karim Khan.", group="gharana"),
    f("Agra gharana", "Agra combines khayal with Dhrupad-Dhamar and stresses bandish in the source's description.", group="gharana"),
    f("Patiala gharana", "Patiala is associated with Thumri and ghazal specialisation and with Bade Ghulam Ali Khan.", group="gharana"),
    f("Aurangzeb correction", "Under Aurangzeb, singing was removed from the imperial court, but instrumental music, household and noble patronage and music literature continued.", evidence=OCR, group="patronage"),
    f("Sadarang and Adarang", "Sadarang and Adarang later strengthened khayal under Muhammad Shah; this does not mean all music began under them.", evidence=OCR, group="patronage"),
    f("Tansen caution", "The source does not support treating Tansen as the certain inventor of many ragas; invention claims require source-critical caution.", evidence=f"{NITIN} {PYQ_HOLD}", group="attribution"),
    f("Annamacharya", "Annamacharya (1408–1503) composed sankirtanas in praise of Lord Venkateswara and was patronised by Vijayanagara rulers.", group="carnatic_composer"),
    f("Purandara Dasa", "Purandara Dasa (1484–1564) is called the founding father or Pitamaha of Carnatic music, associated with Dasa Sahitya and Vijayanagara patronage.", group="carnatic_composer"),
    f("Tyagaraja", "Tyagaraja's kritis form a core of Carnatic concert repertoire; the source does not supply his birth and death years here.", group="carnatic_composer"),
    f("Carnatic Trinity", "Tyagaraja, Muthuswami Dikshitar and Syama Sastri constitute the Carnatic Trinity in the source.", group="carnatic_composer"),
    f("Venkatamakhin composer", "Venkatamakhin introduced the melakarta system, authored Chaturdandi Prakashika and composed Ashtapadis for Tyagesha at Tiruvarur.", group="carnatic_composer"),
    f("Swathi Thirunal", "Swathi Thirunal Rama Varma (1813–1846), Maharaja of Travancore, composed in both Hindustani and Carnatic styles and patronised the Thanjavur Quartet.", group="carnatic_composer"),
    f("Thanjavur Quartet", "Chinnaiah, Ponniah, Sivanandam and Vadivelu were 19th-century court musicians of Swathi Thirunal who codified the Bharatanatyam repertoire.", group="carnatic_composer"),
    f("Kriti", "A kriti is a highly evolved Carnatic song set to a particular raga and fixed tala, with emphasis on sahitya or lyrical quality.", group="carnatic_form"),
    f("Carnatic composition anatomy", "Pallavi, Anu Pallavi and Charana are the source-bounded three-part anatomy of a Carnatic composition.", group="carnatic_form"),
    f("Carnatic concert sequence", "A typical Carnatic concert may move through varnam, alapana, neraval and kalpana swaras, ending with lighter pieces such as a tillana.", group="carnatic_form"),
    f("Tanam and Ragam", "Tanam is melodic improvisation in free rhythm with mridangam, while pieces without mridangam are described as Ragam in the source.", group="carnatic_form"),
    f("Tata Vadya", "Tata Vadya are chordophones: sound is produced by a stretched, vibrating string; sitar, veena and sarangi are examples.", group="instrument_family"),
    f("Sushira Vadya", "Sushira Vadya are aerophones or wind instruments, including bansuri and shehnai.", group="instrument_family"),
    f("Avanaddha Vadya", "Avanaddha or Awanaddha Vadya are membranophones in which striking a stretched membrane over a resonator produces sound.", group="instrument_family"),
    f("Ghana Vadya", "Ghana Vadya are idiophones or non-drum percussion instruments in which the body vibrates; the source says they do not require tuning.", group="instrument_family"),
    f("Ghatam and Jaltarang", "Ghatam and Jaltarang belong to Ghana Vadya, not Avanaddha, because neither depends on a stretched membrane.", group="instrument"),
    f("Tabla and Mridangam", "Tabla is paired with Hindustani practice and Mridangam with Carnatic practice in the source's instrument table.", group="instrument"),
    f("Shehnai", "Shehnai is a Sushira instrument associated with Hindustani music and Ustad Bismillah Khan.", group="instrument"),
    f("Bansuri", "Bansuri or flute is a Sushira instrument associated in the source with Hariprasad Chaurasia.", group="instrument"),
    f("Santoor", "Santoor is a 100-stringed Tata instrument associated with Jammu and Kashmir and with accompaniment of Sufiana kalam.", group="instrument"),
    f("Sitar", "Sitar is a plectral Tata instrument; the source lists Jaipur, Varanasi and Etawah among sitar gharanas.", group="instrument"),
    f("Veena", "Veena is a plectral Tata instrument associated with Carnatic practice and with Saraswati in the source's cultural association.", group="instrument"),
    f("Folk instrument ecology", "Kamaicha is associated with Rajasthan's Manganiyars, Dotara with Bengal's Bauls, Gogona with Assam's Bihu and Ghumot with Goa's Ganesh festival.", group="folk_instrument"),
    f("Bhimsen Joshi", "Bhimsen Joshi (1922–2011) was a Khayal exponent of Kirana Gharana and received the Bharat Ratna in 2008.", group="modern_musician"),
    f("Bismillah Khan", "Bismillah Khan (1916–2006) was a shehnai maestro associated with the Benaras Gharana and received the Bharat Ratna in 2001.", group="modern_musician"),
    f("Ravi Shankar", "Ravi Shankar (1920–2012) was a sitar maestro who received the Bharat Ratna in 1999; the source does not assign him a gharana.", group="modern_musician"),
    f("M.S. Subbulakshmi", "M.S. Subbulakshmi (1916–2004) was a Carnatic vocalist and received the Bharat Ratna in 1998.", group="modern_musician"),
    f("Folk-classical distinction", "The source distinguishes classical and folk by function, transmission and setting rather than by a value hierarchy; folk traditions are not 'less developed'.", group="folk"),
    f("Baul", "Baul or Baul Gaan is associated with West Bengal, Assam and Tripura and carries Hindu Bhakti and Sufi influence.", group="folk"),
    f("Pandavani", "Pandavani of Chhattisgarh is based on the Mahabharata with Bhima as hero and combines singing with instrumental playing, usually to tambura rhythm.", group="folk"),
    f("Panihari", "Panihari of Rajasthan centres on women fetching water, scarcity, distance and related domestic or romantic themes.", group="folk"),
    f("Lavani", "Lavani of Maharashtra is a combined dance-and-song genre performed to the dholki.", group="folk"),
    f("Powada", "Powada of Maharashtra narrates heroic deeds, including those associated with Shivaji.", group="folk"),
    f("Khongjom Parba", "Khongjom Parba of Manipur preserves the memory of the Battle of Khongjom of 1891.", group="folk"),
    f("Zikir", "Zikir of Assam embodies the teaching of Islam in a folk-music form.", group="folk"),
    f("Dollu Kunitha", "Dollu Kunitha is a Karnataka drum dance named after the dollu and performed by the Kuruba community.", group="folk"),
    f("SNA boundary", "Sangeet Natak Akademi recognition and awards are a national institutional route, while UNESCO Intangible Cultural Heritage inscription is a separate international status.", group="institution"),
    f("2025 PYQ provenance", "The 2025 GS-I route concerns the first Gandharva Mahavidyalaya and Vishnu Digambar Paluskar's 1901 institution; it is retained as provenance, not reproduced.", evidence=f"{PYQ_HOLD} {RIGHTS_HOLD}", group="pyq"),
    f("2018 and 2019 PYQ holds", "The 2018 Tyagaraja-Annamacharya and 2019 Tansen routes are held as neutral demands because the local official keys are unavailable or not authenticated.", evidence=f"{PYQ_HOLD} {RIGHTS_HOLD}", group="pyq"),
    f("2026 raga PYQ hold", "The provisional 2026 GS-I raga-equivalence route is used to test precise Hindustani-Carnatic classification, without inferring an answer letter.", evidence=f"{PYQ_HOLD} {RIGHTS_HOLD}", group="pyq"),
    f("Mallikarjun Mansur gap", "The local Topic 08 sources do not name Mallikarjun Mansur or assign him a gharana; the correct evidence discipline is to leave that attribution open rather than guess.", evidence=f"{PYQ_HOLD} {RIGHTS_HOLD}", group="boundary"),
    f("Amir Khusrau attribution caution", "Sitar, tabla, khayal and qawwali are popularly attributed to Amir Khusrau in secondary literature, but the attribution is contested without a specific contemporaneous source.", evidence=f"{NITIN} Advanced §§2, 4, 9.", group="attribution"),
]


STEMS = {
    1: "Which statement is the source-bounded proposition filed under **{label}**?",
    2: "A revision card is labelled **{label}**. Which option belongs on that card?",
    3: "In a close-option question on **{label}**, which formulation is safest?",
}


def choose_distractors(index: int, bank: int) -> list[int]:
    target_group = FACTS[index]["group"]
    candidates = [
        candidate
        for candidate in range(len(FACTS))
        if candidate != index and FACTS[candidate]["group"] != target_group
    ]
    starts = {1: 11, 2: 37, 3: 71}
    start = (index * 13 + starts[bank]) % len(candidates)
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
    rng = random.Random(20261008 + bank * 997)
    order = list(range(len(FACTS)))
    if bank == 2:
        order = order[23:] + order[:23]
    elif bank == 3:
        order = order[47:] + order[:47]
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
        f"# Topic 08 — Indian Music — Revision {bank}",
        "",
        "> Select one option for each question.",
        "",
    ]
    a_lines = [
        f"# Topic 08 — Revision {bank} Answers",
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
        a_lines.append(f"   - **Correct answer:** {target['statement']}")
        a_lines.append(f"   - **Evidence:** This is the source-bounded proposition filed under **{target['label']}**.")
        for option in question["options"]:
            fact = FACTS[option["fact_index"]]
            if option["fact_index"] == question["target"]:
                reason = f"Correct: it matches **{target['label']}** and answers the stem precisely."
            else:
                reason = (
                    f"Incorrect for this stem: it belongs under **{fact['label']}**, not "
                    f"**{target['label']}**. Its bounded proposition is: {fact['statement']}"
                )
            a_lines.append(f"   - **{option['letter']}.** {option['text']} — {reason}")
        a_lines.append(f"   - **Sources:** {target['evidence']}; {WORKBOOK}")
        a_lines.append(f"   - **Trap:** {target['trap']}")
        a_lines.append("")

    (folder / "QUESTIONS.md").write_text("\n".join(q_lines), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(a_lines), encoding="utf-8")
    (folder / "COVERAGE.md").write_text(
        f"""# Topic 08 — Revision {bank} Coverage

**Status:** in_progress pending structural and hostile audit
**Question count:** {len(questions)} original MCQs
**Independence:** This bank tests every Topic 08 source card once, with a distinct target order, framing, distractor neighbourhood and independently shuffled answer positions.

## Source spine

- Basic owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/08_Indian-Music.md`
- Advanced owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/advanced/08_Indian-Music.md`
- Complete package/workbook: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/08_Indian-Music_Complete-Topic-Package.md` and `upsc-ai-kit/knowledge/Indian-Art-and-Culture/learning-sessions/v2/subject-wide-syllabus/indian-art-and-culture-08_Solved-Workbook.md`
- Mandated OCR/book spine: Nitin Singhania, *Indian Art and Culture*, PDF pp.411–457; R.S. Sharma, *India's Ancient Past*, PDF pp.347–355; Satish Chandra, *History of Medieval India*, PDF pp.332–334; Satish Chandra, *Medieval History, 1526–1748, Part 2*, PDF pp.394–395.

## Coverage ledger

Every Topic 08 source card is tested once: swara/shruti/raga/thaat/tala/laya; melakarta-janya; rasa linkage; treatises; Bhatkhande and Paluskar; Hindustani-Carnatic comparison; Hindustani forms; gharana distinctions; Aurangzeb/Sadarang/Tansen controls; Carnatic composers and forms; instrument families and regional associations; modern musicians; folk music; institutional boundaries; and PYQ provenance/gap controls.

## PYQ provenance, key and rights holds

- 2018 GS-I Q44, 2019 GS-I Q16, 2025 GS-I Q18, provisional 2026 GS-I Q1 and Q19 are neutral provenance/coverage routes only.
- Exact UPSC wording/options are not reproduced. {RIGHTS_HOLD}
- The 2026 Set-A key is provisional for the routed 2026 demands; no answer letter is inferred. The 2018–2019 objective keys are unavailable or not authenticated locally. No coaching key is accepted.
- The Mallikarjun Mansur source gap remains explicitly held; no gharana attribution is guessed.

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
        if len(q_ids) != len(FACTS):
            errors.append(f"revision-{bank}: expected {len(FACTS)} questions")
    return errors


def hostile_audit() -> list[str]:
    errors: list[str] = []
    stem_sets: list[set[str]] = []
    key_sets: list[list[str]] = []
    for bank in range(1, 4):
        q = (TOPIC / f"revision-{bank}" / "QUESTIONS.md").read_text(encoding="utf-8")
        stems = re.findall(r"^### Q\d+\. (.+)$", q, re.M)
        stem_sets.append(set(stems))
        if len(set(stems)) != len(stems):
            errors.append(f"revision-{bank}: duplicate stems inside bank")
        keys = re.findall(r"^\d+\.\s+\*\*([A-D])\.", (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8"), re.M)
        key_sets.append(keys)
        if len(set(keys)) < 3:
            errors.append(f"revision-{bank}: answer positions too concentrated")
        if all(keys[i] == "ABCD"[i % 4] for i in range(len(keys))):
            errors.append(f"revision-{bank}: predictable A-B-C-D answer cycle")
        for qblock in re.split(r"^### Q\d+\.", q, flags=re.M)[1:]:
            options = re.findall(r"^[A-D]\. (.+)$", qblock, re.M)
            if len(options) != 4 or len(set(options)) != 4:
                errors.append(f"revision-{bank}: duplicate or missing option text")
    for left in range(3):
        for right in range(left + 1, 3):
            overlap = stem_sets[left] & stem_sets[right]
            if overlap:
                errors.append(f"cross-bank stem duplication revision-{left + 1}/revision-{right + 1}: {len(overlap)}")
    if key_sets[0] == key_sets[1] or key_sets[0] == key_sets[2] or key_sets[1] == key_sets[2]:
        errors.append("answer-position sequence duplicated across banks")
    return errors


def write_topic_coverage(status: str = "complete") -> None:
    (TOPIC / "COVERAGE.md").write_text(
        f"""# Topic 08 — Indian Music

**Status:** `{status}`
**Catalogue position:** 08 of 15
**Question banks:** 3 independent banks × {len(FACTS)} original MCQs = {len(FACTS) * 3} originals
**Owner coverage:** Basic and Advanced owners, complete package/workbook and mandated OCR/book spine read before authoring.

## Owned coverage

Saptaswara, shruti, raga, tala, laya, thaat and 72-melakarta/janya theory; rasa and time; treatise chronology; Hindustani-Carnatic comparison; Dhrupad, khayal, thumri, tappa, ghazal and tarana; gharana transmission and named gharanas; Aurangzeb/Sadarang/Tansen attribution controls; Carnatic composers, kriti anatomy and concert sequence; Tata/Sushira/Avanaddha/Ghana instrument families; regional instruments; modern musicians and bounded honours; folk music by region, occasion and function; SNA/UNESCO institutional distinction; PYQ provenance and source gaps.

## Source and evidence controls

- Primary Markdown owners: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/08_Indian-Music.md` and `advanced/08_Indian-Music.md`.
- Complete package/workbook: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/08_Indian-Music_Complete-Topic-Package.md` and `upsc-ai-kit/knowledge/Indian-Art-and-Culture/learning-sessions/v2/subject-wide-syllabus/indian-art-and-culture-08_Solved-Workbook.md`.
- OCR/book spine: Nitin Singhania, *Indian Art and Culture*, PDF pp.411–457; R.S. Sharma, *India's Ancient Past*, PDF pp.347–355; Satish Chandra, *History of Medieval India*, PDF pp.332–334; Satish Chandra, *Medieval History, 1526–1748, Part 2*, PDF pp.394–395.
- No unsupported page precision, invented musician attribution, invention date or verbatim quotation is imported.

## PYQ provenance and rights holds

- 2018 Tyagaraja/Annamacharya, 2019 Tansen, 2025 Gandharva Mahavidyalaya and provisional 2026 raga-equivalence/Mallikarjun Mansur routes are explicit provenance/coverage holds only.
- Exact UPSC wording/options are withheld because UPSC website reproduction permission is not held.
- 2026 local Set-A key is provisional for the routed 2026 demands; 2018–2019 keys are unavailable or not authenticated. No answer letter is inferred and no coaching key is accepted.
- Mallikarjun Mansur's gharana remains an explicit source gap; it is not guessed.

## Release audit

- Structural audit: pending until all three banks are generated and checked.
- Hostile audit: pending until answer leakage, duplicate stems, key concentration, cross-bank reuse and option duplication are checked.
- Final subject pipeline is run only after this ledger and `INDEX.md` are updated.
""",
        encoding="utf-8",
    )


def write_audit() -> None:
    structural = structural_audit()
    hostile = hostile_audit()
    errors = structural + hostile
    report = [
        "# Topic 08 — Structural and Hostile Audit",
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
        f"2018, 2019, 2025 and provisional 2026 routes are provenance holds only. {RIGHTS_HOLD} The Mallikarjun Mansur attribution gap remains open rather than being guessed.",
    ]
    (TOPIC / "AUDIT-REPORT.md").write_text("\n".join(report), encoding="utf-8")
    if errors:
        raise SystemExit("AUDIT FAILED: " + "; ".join(errors))


def update_indexes() -> None:
    index = SUBJECT / "INDEX.md"
    text = index.read_text(encoding="utf-8")
    old = "| 08 | Indian Music | pending | — | — | — |"
    new = (
        f"| 08 | Indian Music | [Complete](08-Indian-Music/COVERAGE.md) "
        f"| [{len(FACTS)} originals](08-Indian-Music/revision-1/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](08-Indian-Music/revision-2/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](08-Indian-Music/revision-3/QUESTIONS.md) · complete |"
    )
    if old not in text:
        raise SystemExit("INDEX row for Topic 08 not found")
    index.write_text(text.replace(old, new), encoding="utf-8")

    coverage = SUBJECT / "COVERAGE.md"
    ctext = coverage.read_text(encoding="utf-8")
    old_row = "| 08 | Indian Music | `pending` | not started |"
    new_row = f"| 08 | Indian Music | `complete` | 3 independent banks; {len(FACTS)} / {len(FACTS)} / {len(FACTS)} originals |"
    if old_row not in ctext:
        raise SystemExit("subject coverage row for Topic 08 not found")
    ctext = ctext.replace(old_row, new_row)
    ctext += f"""

## Topic 08 release gate — Indian Music

- Revision 1 / 2 / 3 contain **{len(FACTS)} / {len(FACTS)} / {len(FACTS)} original MCQs** ({len(FACTS) * 3} total).
- Each bank independently covers the Basic/Advanced/source ledger with distinct framing, target order, distractor neighbourhood and independently shuffled answer positions.
- PYQ holds: 2018 Tyagaraja/Annamacharya, 2019 Tansen, 2025 Gandharva Mahavidyalaya and provisional 2026 raga-equivalence/Mallikarjun Mansur are recorded for provenance only. No exact wording/options are reproduced, no unverified key is used, and UPSC website permission is not held.
- Structural and hostile audits are clean. Next pending topic is **09 — Indian Dance**.
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
