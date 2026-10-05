"""Build and audit Indian Art and Culture Topic 07 revision banks.

All questions are original paraphrases. Exact UPSC wording and options are
withheld because reproduction permission is not held.
"""

from __future__ import annotations

import argparse
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Indian-Art-and-Culture"
TOPIC = SUBJECT / "07-Painting-Traditions"

NITIN = (
    "Basic §§2–5, 13.4–13.9; Advanced §§2–6, 9, 13; "
    "Nitin Singhania, Indian Art and Culture, PDF pp.309–377."
)
OCR = (
    "R.S. Sharma, India's Ancient Past, PDF pp.347–355; "
    "Satish Chandra, History of Medieval India, PDF pp.328–334; "
    "Satish Chandra, Medieval History, 1526–1748, Part 2, PDF pp.389–392."
)
PYQ_HOLD = (
    "Basic §§7, 13.9 and routed PYQ ledgers: 2017 GS-I Q38 (Padmapani/Ajanta), "
    "2018 GS-I Q42 (Bani Thani/Kishangarh), 2019 GS-I Q17 (Jahangir portraiture), "
    "and provisional 2026 GS-I Q5 (Hallisalasya/Bagh)."
)
STATUS = (
    "Basic §§8, 13.9; Advanced §§7, 13: current museum location, attribution, "
    "GI status or conservation claims require a dated official institutional source."
)


def f(label: str, statement: str, evidence: str = NITIN, trap: str = "", group: str = "general") -> dict:
    return {
        "label": label,
        "statement": statement,
        "evidence": evidence,
        "trap": trap or "Do not transfer this proposition to a neighbouring school, format or region.",
        "group": group,
    }


FACTS = [
    f("Shadanga overview", "The six limbs of painting are Roopbheda, Pramana, Bhava, Lavanya Yojana, Sadrishya and Varnikabhanga.", group="theory"),
    f("Roopbheda", "Roopbheda concerns the differentiation or appearance of forms.", group="theory"),
    f("Pramana", "Pramana concerns proportion and structure in the painted form.", group="theory"),
    f("Bhava", "Bhava concerns expression or the emotional state conveyed by the image.", group="theory"),
    f("Lavanya Yojana", "Lavanya Yojana concerns aesthetic composition or the arrangement that gives grace.", group="theory"),
    f("Sadrishya", "Sadrishya concerns resemblance or likeness.", group="theory"),
    f("Varnikabhanga", "Varnikabhanga concerns the use and modulation of brush and colour.", group="theory"),
    f("Petroglyph", "A petroglyph is a prehistoric rock engraving and must be distinguished from a painted rock image.", group="rock"),
    f("Rock-art geography", "Bhimbetka in Madhya Pradesh and Lakhudiyar in Uttarakhand anchor the prehistoric rock-art beginning in the source spine.", group="rock"),
    f("Ajanta technique", "Ajanta pigments were generally applied over prepared plaster after the surface had dried, so fresco secco or tempera is safer than true wet fresco.", group="mural"),
    f("Bagh location", "Bagh Caves lie on the Baghni river in Dhar district of Madhya Pradesh and form a mainly Buddhist cave group.", group="mural"),
    f("Bagh Cave 4", "Bagh Cave 4 is known as Rang Mahal and its murals depict Buddhist Jataka Tales.", group="mural"),
    f("Hallisalasya", "The Bagh paintings depict Hallisalasya, described as a devotional or courtly dance in Gupta-period art and sculpture.", group="mural"),
    f("Bagh chronology caution", "The source gives both 5th–6th and 5th–7th century ranges for Bagh excavations; the variation must be reported rather than silently resolved.", group="mural"),
    f("Sittanavasal", "Sittanavasal preserves Pandya-period Jain cave paintings with floral creepers, dancing figures and birds, using mineral colours in the source description.", group="mural"),
    f("Pallava surviving murals", "The principal surviving Pallava mural locations named in the source are Kailasanatha at Kanchipuram and Talagishwara at Panamalai.", group="south_mural"),
    f("Chola mural record", "Vijaya Cholishwaram and Brihadeswara preserve the principal Chola wall-painting record, including Rajaraja with Karuvur Devar and later Nayaka superimposition at Brihadeswara.", group="south_mural"),
    f("Survival bias", "The scarcity of surviving Pallava or Chola murals limits claims about preservation, not necessarily claims about the original scale or quality of production.", evidence=f"{NITIN} Advanced §§2, 4.", group="analysis"),
    f("Mural patronage", "Cave and temple murals require monumental institutional or royal sponsorship and are designed for collective or devotional viewing.", evidence=f"{NITIN} Advanced §§2–4.", group="format"),
    f("Pala manuscripts", "Pala painting is associated with Buddhist manuscript illustration in eastern India and forms an early miniature lineage.", group="miniature"),
    f("Western Indian Jain manuscripts", "Western Indian or Jain manuscript painting in Gujarat–Rajasthan represents a devotional, page-based tradition distinct from a generic Mughal style.", group="miniature"),
    f("Mughal Akbar atelier", "Akbar's karkhana produced large illustrated manuscripts through collaborative labour by artists drawn from multiple regions and religious backgrounds.", evidence=f"{NITIN} {OCR}", group="mughal"),
    f("Mughal Jahangir shift", "Jahangir's period is marked by a shift from large manuscript series toward album pages, individual portraiture and refined natural history.", evidence=f"{NITIN} {OCR}", group="mughal"),
    f("Mansur", "Mansur is associated with Jahangir-era naturalistic studies of flora and fauna.", group="mughal"),
    f("Artist mobility", "The dispersal of artists after reduced imperial patronage helped seed regional Rajasthani and Pahari schools.", evidence=f"{NITIN} Advanced §§1, 4.", group="mughal"),
    f("Deccani painting", "Deccani painting is associated with saturated colour, elongated figures, fantastic landscapes and Persianate-Deccan court culture.", group="regional"),
    f("Mewar/Bundi/Kota", "Mewar, Bundi and Kota use bold colour with court, hunt, Krishna and Ragamala themes, while retaining regional variation.", group="regional"),
    f("Kishangarh", "Kishangarh is associated with lyrical Radha–Krishna imagery and Bani Thani, which the source associates with Nihal Chand.", evidence=f"{NITIN} {PYQ_HOLD}", group="regional"),
    f("Basohli", "Basohli is an early Pahari idiom marked by intense colour and bold line, distinct from later Kangra naturalism.", group="regional"),
    f("Guler/Kangra", "Guler and Kangra are associated with softer naturalism, lyrical line and Krishna-poetry themes; Kangra is a later Pahari development.", group="regional"),
    f("Tanjore", "Tanjore painting is a South Indian devotional tradition known for gold-coating and gesso relief.", group="south_miniature"),
    f("Mysore", "Mysore painting is a South Indian miniature tradition distinct from Tanjore's gold-coated relief idiom.", group="south_miniature"),
    f("Company painting", "Company painting served European patrons and documentation, producing a colonial-period hybrid rather than a single homogeneous school.", group="modern"),
    f("Bazaar and Kalighat", "Bazaar and Kalighat traditions served urban pilgrimage and commercial publics and should not be collapsed into Company painting.", group="modern"),
    f("Raja Ravi Varma", "Raja Ravi Varma applied European academic realism to Indian mythological subjects and reached a mass public through print reproduction.", group="modern"),
    f("Bengal School", "The Bengal School reacted against Company painting's colonial hybridity and against Ravi Varma's European academic realism, using an Ajanta-inspired wash idiom.", evidence=f"{NITIN} Advanced §§2, 4, 9.", group="modern"),
    f("Bharat Mata", "Abanindranath Tagore's Bharat Mata is dated 1905 in the source and exemplifies the Bengal School's nationalist cultural argument.", group="modern"),
    f("Nandalal Bose", "Nandalal Bose is associated with the Dandi March sketch and with illustrating the original Constitution document and state award emblems.", group="modern"),
    f("Progressive Artists Group", "The Progressive Artists Group formed after 1947 with F.N. Souza, S.H. Raza, M.F. Husain, K.H. Ara, H.A. Gade and S.K. Bakre, without a single uniform style.", group="modern"),
    f("Madhubani", "Madhubani or Mithila painting is associated with Bihar, natural pigments and a line-and-fill technique on paper or cloth.", group="folk"),
    f("Warli", "Warli painting is associated with Maharashtra and uses white pigment on mud or cow-dung ground with geometric figures.", group="folk"),
    f("Pattachitra", "Pattachitra is associated with Odisha and uses cloth or palm-leaf scroll painting for Jagannath and Puranic themes.", group="folk"),
    f("Kalamkari", "Kalamkari is associated with Andhra Pradesh and uses hand-drawn or block-printed textile processes with natural dyes and mordants.", group="folk"),
    f("Thangka", "Thangka is a Himalayan Buddhist scroll tradition on cotton or silk, often using applique and religious iconography.", group="folk"),
    f("Phad", "Phad is a Rajasthani narrative scroll tradition and should not be confused with Odisha's Pattachitra.", group="folk"),
    f("Gond", "Gond painting is a named central Indian folk or tribal tradition and is not interchangeable with Maharashtra's Warli idiom.", group="folk"),
    f("Pichhwai", "Pichhwai, mainly associated with Nathdwara, depicts Sreenathji within Pushtimarg and developed as a temple-hanging tradition before wider export.", group="folk"),
    f("Format-patronage sequence", "The broad sequence is rock art to mural, manuscript or album miniature, colonial Company/Bazaar painting, nationalist Bengal School and living folk or tribal systems.", evidence=f"{NITIN} Advanced §§1–5.", group="analysis"),
    f("Jahangir PYQ hold", "The routed 2019 GS-I objective demand concerns the Mughal shift toward individual portraiture and is retained as provenance only because the authenticated local key and reproduction permission are not held.", evidence=PYQ_HOLD, group="pyq"),
    f("Bani Thani PYQ hold", "The routed 2018 GS-I objective demand concerns Bani Thani's Kishangarh attribution and is not reproduced verbatim because the authenticated local key and reproduction permission are not held.", evidence=PYQ_HOLD, group="pyq"),
    f("Hallisalasya PYQ hold", "The routed 2026 GS-I objective demand concerns Hallisalasya in Bagh paintings; the local Set-A key is provisional, so no answer letter is inferred or published.", evidence=PYQ_HOLD, group="pyq"),
    f("Current-status hold", "A claim about a painting's present display, museum location, attribution dispute, GI status or conservation requires a dated official institutional source.", evidence=STATUS, group="boundary"),
]


STEMS = {
    1: "Which option states the direct source-bounded proposition filed under **{label}**?",
    2: "A revision card is labelled **{label}**. Which statement belongs on that card?",
    3: "In a close-option question on **{label}**, which formulation is safest?",
}


def choose_distractors(index: int, bank: int) -> list[int]:
    target_group = FACTS[index]["group"]
    candidates = [
        candidate for candidate in range(len(FACTS))
        if candidate != index and FACTS[candidate]["group"] != target_group
    ]
    starts = {1: 7, 2: 19, 3: 31}
    start = (index * 7 + starts[bank]) % len(candidates)
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
    rng = random.Random(20261007 + bank * 997)
    order = list(range(len(FACTS)))
    if bank == 2:
        order = order[17:] + order[:17]
    elif bank == 3:
        order = order[33:] + order[:33]
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
        questions.append({
            "no": qno,
            "target": target,
            "stem": STEMS[bank].format(label=FACTS[target]["label"]),
            "options": options,
            "correct": correct,
        })
    return questions


def write_bank(bank: int, questions: list[dict]) -> None:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    q_lines = [
        f"# Topic 07 — Painting Traditions — Revision {bank}",
        "",
        "> Select one option for each question.",
        "",
    ]
    a_lines = [
        f"# Topic 07 — Revision {bank} Answers",
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
        a_lines.append(f"   - **Evidence:** This is the source-bounded proposition filed under **{target['label']}**.")
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
        f"""# Topic 07 — Revision {bank} Coverage

**Status:** in_progress pending structural and hostile audit
**Question count:** {len(questions)} original MCQs
**Independence:** This bank tests every Topic 07 source card once, with a distinct target order, framing, distractor neighbourhood and independently shuffled answer positions.

## Source spine

- Basic owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/07_Painting-Traditions.md`
- Advanced owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/advanced/07_Painting-Traditions.md`
- Complete package/workbook: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/07_Painting-Traditions_Complete-Topic-Package.md` and `learning-sessions/v2/subject-wide-syllabus/indian-art-and-culture-07_Solved-Workbook.md`
- OCR/book spine: Nitin Singhania, *Indian Art and Culture*, PDF pp.309–377 (plus pp.63, 181, 186, 323–324 for Bagh/Hallisalasya); R.S. Sharma, *India's Ancient Past*, PDF pp.347–355; Satish Chandra, *History of Medieval India*, PDF pp.328–334; Satish Chandra, *Medieval History, 1526–1748, Part 2*, PDF pp.389–392.

## Coverage ledger

Every source card is tested in this bank: Shadanga and its six limbs; petroglyphs and rock-art sites; Ajanta, Bagh, Hallisalasya, Sittanavasal and Bagh dating caution; Pallava and Chola mural survival; survival bias and mural patronage; Pala and Western Indian/Jain manuscripts; Akbar's collaborative karkhana, Jahangir's album/natural-history shift, Mansur and artist mobility; Deccani, Rajasthani, Kishangarh, Basohli and Kangra/Guler; Tanjore and Mysore; Company, Bazaar/Kalighat, Ravi Varma, Bengal School, Bharat Mata, Nandalal Bose and the Progressive Artists Group; Madhubani, Warli, Pattachitra, Kalamkari, Thangka, Phad, Gond and Pichhwai; format-patronage evolution; PYQ provenance holds; and current-status evidence controls.

## PYQ provenance, key and rights holds

- 2017 GS-I Q38 (Padmapani/Ajanta), 2018 GS-I Q42 (Bani Thani/Kishangarh), 2019 GS-I Q17 (Jahangir portraiture), and provisional 2026 GS-I Q5 (Hallisalasya/Bagh) are retained as neutral provenance/coverage routes only.
- The 2024 Pallava and Chola Mains routes are supporting evidence owned by Topic 03, not direct Topic 07 PYQs.
- Exact UPSC wording/options are not reproduced. UPSC website reproduction permission is not held.
- The locally available 2026 Set-A key is provisional; no answer letter is inferred. Earlier objective keys are unavailable or not authenticated in the local route.
- No coaching key is treated as official.

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
    for bank in range(1, 4):
        q = (TOPIC / f"revision-{bank}" / "QUESTIONS.md").read_text(encoding="utf-8")
        stems = re.findall(r"^### Q\d+\. (.+)$", q, re.M)
        stem_sets.append(set(stems))
        if len(set(stems)) != len(stems):
            errors.append(f"revision-{bank}: duplicate stems inside bank")
        keys = re.findall(r"^\d+\.\s+\*\*([A-D])\.", (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8"), re.M)
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
    return errors


def write_topic_coverage(status: str = "complete") -> None:
    (TOPIC / "COVERAGE.md").write_text(
        f"""# Topic 07 — Painting Traditions

**Status:** `{status}`
**Catalogue position:** 07 of 15
**Question banks:** 3 independent banks × {len(FACTS)} original MCQs = {len(FACTS) * 3} originals
**Owner coverage:** Basic and Advanced owners, complete package/workbook and mandated OCR/book spine read before authoring.

## Owned coverage

Shadanga; prehistoric rock art; Ajanta, Bagh, Hallisalasya and Sittanavasal; Pallava and Chola murals; format/patronage and survival bias; Pala and Western Indian/Jain manuscripts; Mughal Akbar/Jahangir/Mansur and atelier mobility; Deccani, Rajasthani, Kishangarh, Pahari, Tanjore and Mysore; Company, Bazaar/Kalighat, Ravi Varma, Bengal School, Bharat Mata, Nandalal Bose and post-1947 modernism; Madhubani, Warli, Pattachitra, Kalamkari, Thangka, Phad, Gond and Pichhwai; PYQ provenance controls; and current-status evidence limits.

## Source and evidence controls

- Primary Markdown owners: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/07_Painting-Traditions.md` and `advanced/07_Painting-Traditions.md`.
- Complete package/workbook: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/07_Painting-Traditions_Complete-Topic-Package.md` and `learning-sessions/v2/subject-wide-syllabus/indian-art-and-culture-07_Solved-Workbook.md`.
- OCR/book spine: Nitin Singhania, *Indian Art and Culture*, PDF pp.309–377 (plus pp.63, 181, 186, 323–324 for Bagh/Hallisalasya); R.S. Sharma, *India's Ancient Past*, PDF pp.347–355; Satish Chandra, *History of Medieval India*, PDF pp.328–334; Satish Chandra, *Medieval History, 1526–1748, Part 2*, PDF pp.389–392.
- No unsupported page precision or verbatim quotation is imported.

## PYQ provenance and rights holds

- 2017 GS-I Q38, 2018 GS-I Q42, 2019 GS-I Q17 and provisional 2026 GS-I Q5 are explicit provenance/coverage holds only.
- 2024 Pallava and Chola Mains routes support the mural evidence but are owned by Topic 03, not reproduced here.
- Exact UPSC wording/options are withheld because UPSC website reproduction permission is not held.
- The 2026 local Set-A key is provisional; no answer letter is inferred. Older objective keys are unavailable or not authenticated locally, and no coaching key is accepted.

## Release audit

- Structural audit: pending until all three banks are generated and checked.
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
        "# Topic 07 — Structural and Hostile Audit",
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
        "No exact PYQ wording/options are reproduced. 2017/2018/2019 routes and the provisional 2026 Hallisalasya route are recorded as provenance holds; 2024 Pallava/Chola Mains are supporting routes owned by Topic 03. UPSC website reproduction permission is not held.",
    ]
    (TOPIC / "AUDIT-REPORT.md").write_text("\n".join(report), encoding="utf-8")
    if errors:
        raise SystemExit("AUDIT FAILED: " + "; ".join(errors))


def update_indexes() -> None:
    index = SUBJECT / "INDEX.md"
    text = index.read_text(encoding="utf-8")
    old = "| 07 | Painting Traditions | pending | — | — | — |"
    new = (
        f"| 07 | Painting Traditions | [Complete](07-Painting-Traditions/COVERAGE.md) "
        f"| [{len(FACTS)} originals](07-Painting-Traditions/revision-1/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](07-Painting-Traditions/revision-2/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](07-Painting-Traditions/revision-3/QUESTIONS.md) · complete |"
    )
    if old not in text:
        raise SystemExit("INDEX row for Topic 07 not found")
    index.write_text(text.replace(old, new), encoding="utf-8")

    coverage = SUBJECT / "COVERAGE.md"
    ctext = coverage.read_text(encoding="utf-8")
    old_row = "| 07 | Painting Traditions | `pending` | not started |"
    new_row = f"| 07 | Painting Traditions | `complete` | 3 independent banks; {len(FACTS)} / {len(FACTS)} / {len(FACTS)} originals |"
    if old_row not in ctext:
        raise SystemExit("subject coverage row for Topic 07 not found")
    ctext = ctext.replace(old_row, new_row)
    ctext += f"""

## Topic 07 release gate — Painting Traditions

- Revision 1 / 2 / 3 contain **{len(FACTS)} / {len(FACTS)} / {len(FACTS)} original MCQs** ({len(FACTS) * 3} total).
- Each bank independently covers the Basic/Advanced/source ledger with distinct framing, target order, distractor neighbourhood and independently shuffled answer positions.
- PYQ holds: 2017 Padmapani/Ajanta, 2018 Bani Thani/Kishangarh, 2019 Jahangir portraiture and provisional 2026 Hallisalasya/Bagh are recorded for provenance only; 2024 Pallava/Chola routes support Topic 03. No exact wording/options are reproduced, no unverified key is used, and UPSC website permission is not held.
- Structural and hostile audits are clean. Next pending topic is **08 — Indian Music**.
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
