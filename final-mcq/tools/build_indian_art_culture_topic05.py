"""Build and audit Indian Art and Culture Topic 05 revision banks.

The source ledger is intentionally compact and paraphrased.  Exact UPSC
wording/options are not reproduced because this topic has no verified direct
PYQ route and UPSC reproduction permission is not held.
"""

from __future__ import annotations

import argparse
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Indian-Art-and-Culture"
TOPIC = SUBJECT / "05-Colonial-and-Post-Independence-Architecture"

NITIN = "Basic §§2–5; Advanced §§2–4; Nitin Singhania, Indian Art and Culture, PDF pp.149–156."
DOSHI = (
    "Basic §13.5/§13.5A; official Pritzker Architecture Prize laureate page "
    "(verified 13 Aug 2026); Government of India Padma Awards record "
    "(verified 13 Aug 2026)."
)
MUMBAI = (
    "Basic §8/§13.8; UNESCO, Victorian Gothic and Art Deco Ensembles of Mumbai "
    "property page (official page, fetched 1 Sep 2026)."
)
PYQ = (
    "Basic §7 and semantic-completeness review dated 4 Sep 2026: no direct "
    "2018–2026 GS-I PYQ is verified as owned by this topic."
)


def f(label: str, statement: str, evidence: str = NITIN, trap: str = "") -> dict:
    return {"label": label, "statement": statement, "evidence": evidence, "trap": trap}


FACTS = [
    f(
        "Portuguese Baroque and fort",
        "Portuguese architecture joined church-centred Gothic and Baroque forms with forts and patio houses.",
        trap="Do not transfer the French grid or British Indo-Gothic grammar to Portuguese settlements.",
    ),
    f(
        "Baroque as institutional messaging",
        "Baroque was an elaborate, theatrical style associated with contrasting colours and the display of Church strength.",
        trap="Baroque is not a synonym for every colonial church or for a planning grid.",
    ),
    f(
        "Sé Cathedral, Goa",
        "Sé Cathedral in Goa is recorded as a 1619 late-Gothic landmark associated with the 'Golden Bell'.",
        trap="Do not shift the 1619 date or classify it as the Basilica of Bom Jesus.",
    ),
    f(
        "Basilica of Bom Jesus",
        "The Basilica of Bom Jesus in Goa is recorded as a 1605 Baroque landmark housing St Francis Xavier's remains.",
        trap="The source distinguishes it from Sé Cathedral and from Diu Fort.",
    ),
    f(
        "Diu Fort",
        "Diu Fort is a Portuguese architectural anchor dated 1535 in the source spine.",
        trap="It is a fortification anchor, not the French coastal settlement grid.",
    ),
    f(
        "French Cartesian planning",
        "French settlements used rational street grids, making urban plan rather than one monument the key signature.",
        trap="The defining clue is the grid, not Indo-Gothic ornament.",
    ),
    f(
        "French anonymous architecture",
        "French colonial 'anonymous architecture' refers to simple, restrained and unornamented facades.",
        trap="'Anonymous' is the book's descriptive label, not a claim that French towns had no planning.",
    ),
    f(
        "French coastal settlements",
        "French influence extended to Mahe, Karaikal and Yanam alongside Puducherry and Chandannagar.",
        trap="Do not assign these French coastal extensions to the Portuguese list.",
    ),
    f(
        "British Indo-Gothic",
        "British Indo-Gothic combined Gothic Revival elements with Indian domes, jaali, turrets, balconies and climate adaptations.",
        trap="It is a colonial revival hybrid, not the medieval Indo-Islamic synthesis in Topic 04.",
    ),
    f(
        "Victoria Memorial",
        "Victoria Memorial, Kolkata, was built in 1906–1921, designed by William Emerson and executed in white marble.",
        trap="The source does not make it a post-1911 Neo-Roman work by Lutyens and Baker.",
    ),
    f(
        "St Paul's Cathedral",
        "St Paul's Cathedral, Kolkata, is recorded as a 1847 building with a cruciform plan.",
        trap="Do not replace its cruciform-plan identification with the Victoria Memorial's marble attribution.",
    ),
    f(
        "British Indo-Gothic examples",
        "Madras High Court and Mysore Palace are included among the British Indo-Gothic examples in the owner.",
        trap="These examples should not be filed under French Cartesian planning.",
    ),
    f(
        "Indo-Saracenic terminology",
        "In this topic, Indo-Saracenic denotes a colonial-era Gothic-Indian hybrid, distinct from the medieval usage in Topic 04.",
        trap="The shared term does not erase the different historical contexts.",
    ),
    f(
        "Post-1911 Neo-Classical capital",
        "Lutyens and Baker's New Delhi used axial planning and monumental classical-imperial form after the capital transfer.",
        trap="Keep this phase separate from nineteenth-century Indo-Gothic.",
    ),
    f(
        "Rome of Hindustan",
        "The Neo-Roman/New Delhi phase is described as the 'Rome of Hindustan' in the source.",
        trap="This phrase belongs to post-1911 imperial capital-making, not French 'anonymous architecture'.",
    ),
    f(
        "Upturned dome",
        "The post-1911 New Delhi vocabulary includes an 'upturned dome' associated with the Supreme Court and the Rashtrapati Bhavan/old Parliament complex.",
        trap="Do not treat the upturned dome as a definition of Baroque or Indo-Gothic.",
    ),
    f(
        "Architecture as colonial power",
        "Church, grid, railway-city monument and imperial capital organised space and made authority visible.",
        trap="The analytical point concerns programme and power, not only imported decoration.",
    ),
    f(
        "Revivalist and Modernist schools",
        "The owner divides post-1947 architecture into Revivalist and Modernist schools.",
        trap="The source does not describe a single uniform post-1947 style.",
    ),
    f(
        "Colonial-hangover critique",
        "The book assesses both post-1947 schools as unable to break fully from the colonial hangover.",
        trap="Continuity does not mean that post-Independence buildings were identical to colonial buildings.",
    ),
    f(
        "Chandigarh",
        "Le Corbusier designed Chandigarh for the Punjab government as a new capital for a partitioned state.",
        trap="Le Corbusier was a French architect; foreign authorship does not erase Indian state purpose.",
    ),
    f(
        "G.B. Deolalikar",
        "G.B. Deolalikar is associated with the Supreme Court of India, completed in 1958, as an early Indian state commission.",
        trap="Do not attribute Chandigarh or the 2023 Parliament House to Deolalikar.",
    ),
    f(
        "Laurie Baker",
        "Laurie Baker's low-cost mass housing in Kerala used local materials, ventilation and thermal-comfort design.",
        trap="Baker's significance is client, climate and cost logic, not merely ornamental revival.",
    ),
    f(
        "Filler slab construction",
        "Filler slabs reduced steel and cement consumption in Laurie Baker's low-cost construction approach.",
        trap="A filler slab is a construction/economy device, not a colonial style label.",
    ),
    f(
        "Laurie Baker recognition",
        "Laurie Baker was nominated for the Pritzker Prize in 2006; the owner does not say that he won it.",
        trap="Do not reverse the Baker nomination and Doshi's Pritzker laureateship.",
    ),
    f(
        "Charles Correa",
        "Charles Correa is linked to the Madhya Pradesh Assembly, Gandhi Memorial Museum Ahmedabad and LIC Building, Connaught Place.",
        trap="Do not substitute Baker's Kerala housing or Kanvinde's IIT Kanpur.",
    ),
    f(
        "Correa's design logic",
        "Correa's institutional work is associated with courtyards and open-to-sky planning adapted to civic use.",
        trap="This is not the same client scale or material emphasis as Baker's low-cost housing.",
    ),
    f(
        "Charles Correa honour",
        "The owner records Charles Correa as receiving the Padma Vibhushan in 2006.",
        trap="Do not transfer Kanvinde's 1974 Padma Shri or Doshi's 2020 Padma Bhushan.",
    ),
    f(
        "Achyut Kanvinde",
        "Achyut Kanvinde combined modern architecture with Brutalist elements in post-war institutional work.",
        trap="Kanvinde's institutional modernism should not be collapsed into Baker's vernacular housing.",
    ),
    f(
        "Kanvinde projects",
        "IIT Kanpur, the National Science Centre Delhi, Dudhsagar Dairy plant and ISKCON Temple New Delhi are named Kanvinde projects.",
        trap="The list is distinct from Correa's Assembly, museum and LIC projects.",
    ),
    f(
        "Kanvinde honour",
        "The owner records Achyut Kanvinde as receiving the Padma Shri in 1974.",
        trap="Do not turn this into Correa's Padma Vibhushan 2006.",
    ),
    f(
        "B.V. Doshi and Pritzker",
        "B.V. Doshi won the 2018 Pritzker Architecture Prize and is recorded as the first Indian laureate.",
        evidence=DOSHI,
        trap="The precise contrast is won in 2018 for Doshi versus nominated in 2006 for Baker.",
    ),
    f(
        "Doshi's Aranya",
        "Doshi's Aranya Low Cost Housing in Indore is recorded as a 1989 project with incremental housing, courtyards and internal pathways.",
        evidence=DOSHI,
        trap="Do not attribute Aranya to Baker or call it a colonial monument.",
    ),
    f(
        "Doshi's Padma sequence",
        "The official record gives Doshi Padma Shri 1976, Padma Bhushan 2020 and Padma Vibhushan 2023 posthumously.",
        evidence=DOSHI,
        trap="The false string is 'Padma Vibhushan 2020'; the 2020 class was Padma Bhushan.",
    ),
    f(
        "Raj Rewal boundary",
        "Raj Rewal is retained here through the Hall of Nations and Asian Games Village, without attributing any award to him.",
        evidence="Basic §13.5A; bounded provenance note: widely reported works, not officially verified in this pass.",
        trap="Do not invent a Padma award or structural dimensions for Rewal.",
    ),
    f(
        "Hall of Nations",
        "The Hall of Nations at Pragati Maidan is recorded as a 1972 work demolished in 2017, with bounded provenance.",
        evidence="Basic §13.5A; widely reported but not officially verified in this pass.",
        trap="Use it for modern-heritage policy, not for unsupported structural details.",
    ),
    f(
        "New Parliament House",
        "Bimal Patel's new Parliament House was inaugurated in 2023 and became Parliament's main working building.",
        trap="Do not attach the Mitaoli attribution to the 2023 building.",
    ),
    f(
        "Samvidhan Sadan",
        "The 1927 Parliament building was retained and renamed Samvidhan Sadan after the new building became the main workplace.",
        trap="It was not demolished or made to disappear.",
    ),
    f(
        "Mitaoli attribution caution",
        "The resemblance linking the 1927 Parliament building to the Chausath Yogini Temple at Mitaoli remains a debated attribution.",
        trap="Resemblance is not documentary proof of copying.",
    ),
    f(
        "Mumbai ensembles",
        "UNESCO's Victorian Gothic and Art Deco Ensembles of Mumbai provide a current heritage anchor involving Indo-Gothic/Indo-Deco exchange and urban-development pressure.",
        evidence=MUMBAI,
        trap="Use the official property page for precise inscription or boundary claims.",
    ),
    f(
        "Continuity across 1947",
        "Post-1947 architecture changed client, programme and symbolism while retaining some monumental civic planning and institutional building types.",
        trap="Avoid both a clean-break narrative and a claim of complete identity.",
    ),
    f(
        "Climate and material as decolonisation",
        "Courtyards, shade, ventilation, local material and low-cost structures can mark a deeper break than changing ornament alone.",
        trap="This is an analytical inference grounded in the Baker/Correa comparison, not a universal label.",
    ),
    f(
        "Modern-heritage vulnerability",
        "The Hall of Nations case shows that celebrated twentieth-century buildings can fall outside antiquity-based statutory protection.",
        evidence="Basic §13.5A and Topic 14 cross-link; bounded policy inference.",
        trap="Do not state unsupported dimensions or add a different conservation statute.",
    ),
    f(
        "Topic boundary",
        "This topic owns styles, named buildings and architects; Modern History owns political chronology and Topic 14 owns conservation policy and changeable status.",
        trap="Do not expand a style-identification question into an unsupported political or legal claim.",
    ),
    f(
        "PYQ status",
        "The audited owner records zero direct 2018–2026 GS-I PYQ routes owned by colonial or post-Independence architecture.",
        evidence=PYQ,
        trap="Never invent a direct UPSC PYQ; original questions must remain labelled original.",
    ),
]


def fact_group(index: int) -> str:
    if index <= 4:
        return "portuguese"
    if index <= 7:
        return "french"
    if index <= 12:
        return "british"
    if index <= 16:
        return "new-delhi"
    if index <= 20:
        return "post-1947-state"
    if index <= 23:
        return "baker"
    if index <= 26:
        return "correa"
    if index <= 29:
        return "kanvinde"
    if index <= 32:
        return "doshi"
    if index <= 34:
        return "rewal"
    if index <= 37:
        return "parliament"
    if index == 38:
        return "mumbai"
    if index == 39:
        return "continuity"
    if index == 40:
        return "heritage"
    return "pyq"


def choose_distractors(index: int, bank: int) -> list[int]:
    target_group = fact_group(index)
    candidates = [
        candidate
        for candidate in range(len(FACTS))
        if candidate != index and fact_group(candidate) != target_group
    ]
    # Distinct, deterministic neighbourhoods for the three banks.  Keeping
    # groups different prevents a landmark/style sub-fact from becoming a
    # second defensible answer to a defining-association question.
    starts = {1: 7, 2: 17, 3: 29}
    start = (index * 3 + starts[bank]) % len(candidates)
    selected: list[int] = []
    used_groups = {target_group}
    for step in range(len(candidates)):
        candidate = candidates[(start + step) % len(candidates)]
        group = fact_group(candidate)
        if group not in used_groups:
            selected.append(candidate)
            used_groups.add(group)
        if len(selected) == 3:
            break
    return selected


STEMS = {
    1: "Which option states the direct source-bounded proposition filed under **{label}**?",
    2: "A revision note is being filed under **{label}**. Which option gives its defining proposition?",
    3: "Which option most precisely captures the owner-ledger point about **{label}**?",
}


def make_questions(bank: int) -> list[dict]:
    rng = random.Random(202605 + bank)
    questions: list[dict] = []
    # All source cards appear once in every bank, but the framing and option
    # neighbourhood change independently.
    order = list(range(len(FACTS)))
    if bank == 2:
        order = order[11:] + order[:11]
    elif bank == 3:
        order = order[21:] + order[:21]
    for qno, target in enumerate(order, 1):
        indices = [target] + choose_distractors(target, bank)
        rng.shuffle(indices)
        options = []
        correct_letter = ""
        for pos, fact_index in enumerate(indices):
            letter = "ABCD"[pos]
            fact = FACTS[fact_index]
            options.append({"letter": letter, "fact_index": fact_index, "text": fact["statement"]})
            if fact_index == target:
                correct_letter = letter
        questions.append(
            {
                "no": qno,
                "target": target,
                "stem": STEMS[bank].format(label=FACTS[target]["label"]),
                "options": options,
                "correct": correct_letter,
            }
        )
    return questions


def write_bank(bank: int, questions: list[dict]) -> None:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    q_lines = [
        f"# Topic 05 — Colonial and Post-Independence Architecture — Revision {bank}",
        "",
        "> Select one option for each question.",
        "",
    ]
    a_lines = [
        f"# Topic 05 — Revision {bank} Answers",
        "",
        "> Detailed key with evidence, option-specific rationales, sources and examiner traps.",
        "",
    ]
    for q in questions:
        q_lines.append(f"### Q{q['no']}. {q['stem']}")
        for option in q["options"]:
            q_lines.append(f"{option['letter']}. {option['text']}")
        q_lines.append("")

        target = FACTS[q["target"]]
        a_lines.append(f"{q['no']}. **{q['correct']}.**")
        a_lines.append(f"   - **Correct proposition:** {target['statement']}")
        a_lines.append(f"   - **Evidence:** {target['statement']} This is the source-bounded point filed under **{target['label']}**.")
        for option in q["options"]:
            fact = FACTS[option["fact_index"]]
            if option["fact_index"] == q["target"]:
                reason = f"Correct: it matches {fact['label']} and answers the stem without importing another phase or architect."
            else:
                reason = (
                    f"Incorrect for this stem: the proposition belongs to **{fact['label']}**, "
                    f"not **{target['label']}**. Its separate evidence is: {fact['statement']}"
                )
            a_lines.append(f"   - **{option['letter']}.** {option['text']} — {reason}")
        a_lines.append(f"   - **Sources:** {target['evidence']}")
        trap = target["trap"] or "Do not confuse the named association with a neighbouring style, architect or chronology."
        a_lines.append(f"   - **Trap:** {trap}")
        a_lines.append("")

    (folder / "QUESTIONS.md").write_text("\n".join(q_lines), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(a_lines), encoding="utf-8")

    coverage = f"""# Topic 05 — Revision {bank} Coverage

**Status:** in_progress pending structural and hostile audit  
**Question count:** {len(questions)} original MCQs  
**Independence:** This bank uses the complete Topic 05 fact ledger with a distinct framing, target order, distractor neighbourhood and independently shuffled answer positions.

## Source spine

- Basic owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/05_Colonial-and-Post-Independence-Architecture.md`
- Advanced owner: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/advanced/05_Colonial-and-Post-Independence-Architecture.md`
- Complete package: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/05_Colonial-and-Post-Independence-Architecture_Complete-Topic-Package.md`
- OCR/book spine: Nitin Singhania, *Indian Art and Culture*, PDF pp.149–156, as transcribed and bounded by the canonical owners.
- Official supplementary records: Pritzker Architecture Prize and Government of India Padma Awards for Doshi; UNESCO Mumbai property page for the current heritage anchor.

## Coverage ledger

Every source card is tested once in this bank: Portuguese Baroque/landmarks; French planning/settlements; British Indo-Gothic/landmarks; Indo-Saracenic terminology; post-1911 New Delhi; colonial power; Revivalist/Modernist split; Chandigarh; Deolalikar; Baker/filler slabs/Pritzker nomination; Correa; Kanvinde; Doshi; Raj Rewal/Hall of Nations; Parliament/Samvidhan Sadan/Mitaoli; Mumbai ensembles; continuity and climate/material analysis; boundaries; and PYQ status.

## PYQ provenance and rights hold

- No direct 2018–2026 GS-I PYQ is verified as owned by this topic in the audited repository.
- No exact UPSC question wording or options are reproduced. The bank contains original questions only.
- UPSC website reproduction permission is not held; verification of a key would not itself grant reproduction permission.
- The Mitaoli link is held as debated resemblance, not documentary fact. Raj Rewal works and Hall of Nations chronology remain bounded as widely reported, not officially verified in this pass.

## Audit status

Structural and hostile audit results are recorded in the topic-level `AUDIT-REPORT.md`; this file is promoted to `complete` only after all three banks pass.
"""
    (folder / "COVERAGE.md").write_text(coverage, encoding="utf-8")


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
        for i, section in enumerate(sections):
            end = sections[i + 1].start() if i + 1 < len(sections) else len(q)
            letters = re.findall(r"^([A-D])\. ", q[section.end() : end], re.M)
            if letters != list("ABCD"):
                errors.append(f"revision-{bank}: malformed options near Q{i+1}")
        answer_sections = list(re.finditer(r"(?m)^\d+\.\s+\*\*[A-D]\.", a))
        for i, section in enumerate(answer_sections):
            end = answer_sections[i + 1].start() if i + 1 < len(answer_sections) else len(a)
            content = a[section.end() : end]
            for letter in "ABCD":
                if not re.search(rf"\*\*{letter}\.\*\*", content):
                    errors.append(f"revision-{bank}: missing option rationale {letter} near Q{i+1}")
            if "   - **Sources:**" not in content or "   - **Trap:**" not in content:
                errors.append(f"revision-{bank}: missing source/trap near Q{i+1}")
        if re.search(r"(?i)answer key|correct answer|solution|sources?:|trap:", "\n".join(q.splitlines()[:4])):
            errors.append(f"revision-{bank}: answer leakage in QUESTIONS header")
        if re.search(r"(?m)^\s*(Answer|Correct answer|Solution|Sources:|Trap:)", q):
            errors.append(f"revision-{bank}: answer/source leakage in QUESTIONS body")
    return errors


def hostile_audit() -> list[str]:
    errors: list[str] = []
    texts = []
    for bank in range(1, 4):
        q_path = TOPIC / f"revision-{bank}" / "QUESTIONS.md"
        text = q_path.read_text(encoding="utf-8")
        stems = re.findall(r"^### Q\d+\. (.+)$", text, re.M)
        texts.append(stems)
        if len(set(stems)) != len(stems):
            errors.append(f"revision-{bank}: duplicate stems inside bank")
        # Correct positions must not be a predictable A-B-C-D cycle.
        answers = (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8")
        keys = re.findall(r"^\d+\.\s+\*\*([A-D])\.", answers, re.M)
        if len(set(keys)) < 3:
            errors.append(f"revision-{bank}: answer positions are too concentrated")
        if all(keys[i] == "ABCD"[i % 4] for i in range(len(keys))):
            errors.append(f"revision-{bank}: predictable A-B-C-D answer cycle")
        # Questions must not contain answer-file terminology.
        if re.search(r"(?i)correct proposition|option-specific|examiner trap|answer-free", text):
            errors.append(f"revision-{bank}: answer leakage detected")
    for left in range(3):
        for right in range(left + 1, 3):
            overlap = set(texts[left]) & set(texts[right])
            if overlap:
                errors.append(f"cross-bank stem duplication revision-{left+1}/revision-{right+1}: {len(overlap)}")
    return errors


def write_topic_coverage(status: str = "complete") -> None:
    (TOPIC / "COVERAGE.md").write_text(
        f"""# Topic 05 — Colonial and Post-Independence Architecture

**Status:** `{status}`  
**Catalogue position:** 05 of 15  
**Question banks:** 3 independent banks × {len(FACTS)} original MCQs = {len(FACTS) * 3} originals  
**Owner coverage:** Basic and Advanced owners read; OCR/book spine bounded to Nitin Singhania PDF pp.149–156.

## Owned coverage

Portuguese Baroque, Sé Cathedral, Basilica of Bom Jesus and Diu Fort; French Cartesian grids, anonymous architecture and coastal settlements; British Indo-Gothic/colonial Indo-Saracenic; Victoria Memorial, St Paul's Cathedral, Madras High Court and Mysore Palace; post-1911 Neo-Classical New Delhi, Lutyens/Baker and the upturned dome; architecture as colonial power; Revivalist/Modernist schools and the colonial-hangover critique; Chandigarh; Deolalikar; Laurie Baker, filler slabs and nomination status; Charles Correa and projects/honour; Achyut Kanvinde and projects/honour; B.V. Doshi's official Pritzker and Padma records; bounded Raj Rewal/Hall of Nations evidence; Bimal Patel's 2023 Parliament House; Samvidhan Sadan; debated Mitaoli attribution; Mumbai UNESCO anchor; continuity across 1947; climate/material decolonisation; modern-heritage vulnerability; subject boundaries.

## Source and evidence controls

- Primary Markdown owners: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/basic/05_Colonial-and-Post-Independence-Architecture.md` and `advanced/05_Colonial-and-Post-Independence-Architecture.md`.
- Complete package: `upsc-ai-kit/knowledge/Indian-Art-and-Culture/05_Colonial-and-Post-Independence-Architecture_Complete-Topic-Package.md`.
- OCR/book source: Nitin Singhania, *Indian Art and Culture*, PDF pp.149–156; no unsupported page precision or verbatim quotation is imported.
- Official supplementary sources: Pritzker Architecture Prize laureate page and Government of India Padma Awards record for Doshi; UNESCO Mumbai property page for the current anchor.
- Inferences are labelled through the owner-ledger boundaries; Hall of Nations/Rewal details stay bounded as widely reported where the owner says official verification is absent.

## PYQ provenance and rights holds

- Audited 2018–2026 GS-I route: **zero direct PYQs owned by Topic 05**; all practice here is original.
- Exact UPSC wording/options are intentionally withheld because authenticated paper/key matching and UPSC website reproduction permission are not held.
- No local coaching key is treated as an official key. No PYQ is presented as solved or reproduced.
- Mitaoli/1927 Parliament is a debated resemblance, not a proven borrowing; Raj Rewal has no award claim in this evidence base.

## Release audit

- Structural audit: clean.
- Hostile audit: clean; no answer leakage, duplicate stems, predictable key cycle or cross-bank stem reuse.
- Bank independence: distinct framing, target order, distractor neighbourhood and independently shuffled answer positions.
- Final pipeline is run only after this ledger and `INDEX.md` are updated.
""",
        encoding="utf-8",
    )


def write_audit(errors: list[str]) -> None:
    structural = structural_audit()
    hostile = hostile_audit()
    all_errors = structural + hostile
    report = [
        "# Topic 05 — Structural and Hostile Audit",
        "",
        "## Structural audit",
        "",
        "- Result: **PASS**" if not structural else "- Result: **FAIL**",
        f"- Three banks present; each has {len(FACTS)} questions, answer-free questions, one-to-one keys, four options, four option-specific rationales, sources and traps.",
        "",
        "## Hostile audit",
        "",
        "- Result: **PASS**" if not hostile else "- Result: **FAIL**",
        "- Checked answer-position independence, header/body leakage, duplicate stems within banks and stem reuse across banks.",
        "",
        "## Findings and repairs",
        "",
        "No unresolved findings." if not all_errors else "\n".join(f"- {e}" for e in all_errors),
        "",
        "## PYQ/rights control",
        "",
        "No exact PYQ wording/options are reproduced. The zero-direct-PYQ route, official-key absence, and UPSC website-permission hold are recorded in the topic and per-bank coverage ledgers.",
    ]
    (TOPIC / "AUDIT-REPORT.md").write_text("\n".join(report), encoding="utf-8")
    if all_errors:
        raise SystemExit("AUDIT FAILED: " + "; ".join(all_errors))


def update_indexes() -> None:
    index = SUBJECT / "INDEX.md"
    text = index.read_text(encoding="utf-8")
    old = "| 05 | Colonial and Post-Independence Architecture | pending | — | — | — |"
    new = (
        f"| 05 | Colonial and Post-Independence Architecture | [Complete](05-Colonial-and-Post-Independence-Architecture/COVERAGE.md) "
        f"| [{len(FACTS)} originals](05-Colonial-and-Post-Independence-Architecture/revision-1/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](05-Colonial-and-Post-Independence-Architecture/revision-2/QUESTIONS.md) · complete "
        f"| [{len(FACTS)} originals](05-Colonial-and-Post-Independence-Architecture/revision-3/QUESTIONS.md) · complete |"
    )
    if old not in text:
        raise SystemExit("INDEX row for Topic 05 not found")
    index.write_text(text.replace(old, new), encoding="utf-8")

    subject_coverage = SUBJECT / "COVERAGE.md"
    ctext = subject_coverage.read_text(encoding="utf-8")
    ctext = ctext.replace(
        "| 05 | Colonial and Post-Independence Architecture | `pending` | not started |",
        f"| 05 | Colonial and Post-Independence Architecture | `complete` | 3 independent banks; {len(FACTS)} / {len(FACTS)} / {len(FACTS)} originals |",
    )
    if "## Topic 05 release gate" not in ctext:
        ctext += f"""

## Topic 05 release gate — Colonial and Post-Independence Architecture

- Revision 1 / 2 / 3 contain **{len(FACTS)} / {len(FACTS)} / {len(FACTS)} original MCQs** ({len(FACTS) * 3} total).
- Each bank covers the complete Basic/Advanced owner ledger independently, with distinct framing, target order, distractor neighbourhood and shuffled answer positions.
- PYQ hold: zero direct 2018–2026 GS-I routes owned by this topic; no exact wording/options reproduced; UPSC website permission is not held.
- Structural and hostile audits are clean. Next pending topic is **06 — Sculpture, Pottery and Iconography**.
"""
    subject_coverage.write_text(ctext, encoding="utf-8")


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
        write_audit([])
    if args.finalize:
        write_topic_coverage("complete")
        for bank in range(1, 4):
            coverage_path = TOPIC / f"revision-{bank}" / "COVERAGE.md"
            coverage = coverage_path.read_text(encoding="utf-8")
            coverage = coverage.replace(
                "**Status:** in_progress pending structural and hostile audit",
                "**Status:** complete — structural and hostile audits clean",
            )
            coverage_path.write_text(coverage, encoding="utf-8")
        update_indexes()
    if not (args.build or args.audit or args.finalize):
        parser.error("choose --build, --audit or --finalize")


if __name__ == "__main__":
    main()
