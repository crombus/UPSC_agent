#!/usr/bin/env python3
"""One-time curator for the static full-simulation descriptive bank.

This utility is intentionally separate from the PDF generator. It selects complete
source model answers, assembles official-style paper structures and writes a bank
that the renderer subsequently treats as immutable input.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import build_full_upsc_simulations as sim


OUT = sim.SOURCE_ROOT / "curated-descriptive-bank.json"
REVIEW_JSON = sim.SOURCE_ROOT / "descriptive-sample-review.json"
REVIEW_MD = sim.SOURCE_ROOT / "DESCRIPTIVE-SAMPLE-REVIEW.md"
BANNED = re.compile(
    r"therefore the defensible verdict on|the tempting claim that|"
    r"advances a definite proposal|test concerns internal coherence|"
    r"\breconstructing\s+[A-Z]|speed in [a-z -]+|through which [a-z -]+ appeal|"
    r"\bCA Anchor\b|claim\s*[-=]>\s*evidence|native-body word count|answer audit|"
    r"answer architecture",
    re.I,
)
INVALID_QUESTION = re.compile(
    r"\bhow many of the above\b|\bcorrectly matched\b|"
    r"\bwhere a question invites\b|\bexaminer(?:s)? reward\b|"
    r"\banswer-writing\b|\banswer architecture\b|\bdemand decoding\b|"
    r"(?:^|\s)[A-D][.)]\s+.+(?:\s|·)[A-D][.)]\s+",
    re.I,
)
INVALID_ANSWER = re.compile(
    r"\bCA Anchor\b|\bsource owner\b|\blocal OCR\b|\brouting\b|"
    r"\bdemand decoding\b|\bwhy this earns marks\b|"
    r"\bhow to improve this answer\b|\bexecutable exam-length answer\b|"
    r"\bnative-body word count\b|\banswer audit\b|"
    r"\bprevious audit\b|\bcorrection record\b|"
    r"\blatest completed national edition located\b|"
    r"\bwhy this answer works\b|\bdetailed examiner-grade\b|"
    r"\bkeep only the application\b|\baudited model-answer\b|"
    r"\baudited 2024\b|\blocal Arthasastra\b|"
    r"\bcited official pages do not verify\b|\bevidence base require\b",
    re.I,
)


def strip_answer_meta(text):
    cleaned = re.split(
        r"(?i)\s*(?:Claim\s*[-=]>\s*evidence\s*[-=]>\s*analysis|"
        r"Native-body word count:|Answer audit:|Answer architecture:|Why this earns marks:)",
        text,
        maxsplit=1,
    )[0].strip()
    sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    cleaned = " ".join(
        sentence for sentence in sentences
        if not INVALID_ANSWER.search(sentence)
    ).strip()
    cleaned = re.sub(
        r"(?i)\bthe source does not support\b",
        "the evidence does not justify",
        cleaned,
    )
    cleaned = re.sub(
        r"(?i)\bthe owners?\s+(?:record|records|define|defines|fix|fixes|"
        r"flag|flags|insist|insists|require|requires)\s+(?:that\s+)?",
        "available evidence indicates that ",
        cleaned,
    )
    cleaned = re.sub(r"(?i)\bowner's\b|\bsource's\b", "documented", cleaned)
    cleaned = re.sub(r"(?i)\bMaster Framework\b", "analytical framework", cleaned)
    cleaned = re.sub(r"(?i)\bsource-specific\b", "context-specific", cleaned)
    cleaned = re.sub(
        r"(?i)\bthe Advanced owner is an analogue of\b",
        "a more precise comparison uses",
        cleaned,
    )
    cleaned = re.sub(
        r"(?i)\bpoverty and nutrition owner\b",
        "related poverty and nutrition analysis",
        cleaned,
    )
    cleaned = re.sub(r"(?i)\bowner-described\b", "documented", cleaned)
    cleaned = re.sub(
        r"(?i)\bpost-2022 owner framework\b",
        "post-2022 statutory framework",
        cleaned,
    )
    cleaned = re.sub(
        r"(?i)\b(?:a|the|this|every) (?:good )?(?:UPSC )?answer "
        r"(?:should|must)\b",
        "analysis should",
        cleaned,
    )
    cleaned = re.sub(
        r"(?i)\bin an? (?:Internal Security|Governance|Geography|History|"
        r"Environment|Science and Technology|Disaster Management) answer\b",
        "in the analysis",
        cleaned,
    )
    cleaned = re.sub(
        r"(?i),?\s*and although the local source describes that result as overwhelming,"
        r"\s*this package states no percentage because no audited polling figure is held"
        r"\s*anywhere in the repository",
        "",
        cleaned,
    )
    cleaned = re.sub(
        r"(?i)the repository owner dates their abolition to 1971, and this package"
        r"\s*asserts no amount for any purse",
        "these privileges were abolished in 1971",
        cleaned,
    )
    cleaned = re.sub(r"(?i)\bWording note\..*?(?=(?:\s+[A-Z][^.]*\.)|$)", "", cleaned)
    return cleaned


def unique(records):
    output = {}
    for record in records:
        output.setdefault(sim.normalize_stem(record["text"]), record)
    return list(output.values())


def clean_record(record, *, marks=None, word_limit=None):
    item = dict(record)
    item["text"] = re.sub(
        r"(?i)\s*(?:\(?Answer\s+in\s+(?:about\s+)?\d+\s+words?\.?\)?|"
        r"\(\d+\s+words?\))\s*$",
        "",
        item["text"],
    ).strip()
    if INVALID_QUESTION.search(item["text"]):
        raise ValueError(f"Invalid Mains question admitted: {item['text']}")
    item["marks"] = marks or item["marks"]
    item["word_limit"] = word_limit or item["word_limit"]
    item["answer"] = trim_answer(strip_answer_meta(item["answer"]), item["word_limit"])
    if INVALID_ANSWER.search(item["answer"]):
        raise ValueError(f"Invalid model-answer metadata admitted: {item['text']}")
    item["difficulty"] = "above-typical recent UPSC"
    item["difficulty_features"] = [
        "question-specific demand", "named evidence", "analysis",
        "qualification", "source-grounded conclusion",
    ]
    return item


def build_gs_sets():
    sim.build_gs_banks.cache_clear()
    banks = sim.build_gs_banks()
    output = {set_no: {} for set_no in sim.SETS}
    for paper, bank in banks.items():
        bank = [
            record for record in bank
            if not INVALID_QUESTION.search(record["text"])
        ]
        safe_tens = [record for record in bank if record["marks"] == 10]
        safe_fifteens = [record for record in bank if record["marks"] == 15]
        if len(safe_tens) < 40:
            raise RuntimeError(f"Insufficient safe 10-mark records for {paper}")
        if len(safe_fifteens) < 40:
            raise RuntimeError(f"Insufficient safe 15-mark records for {paper}")
        for set_no in sim.SETS:
            selected = (
                safe_tens[(set_no - 1) * 10:set_no * 10]
                + safe_fifteens[(set_no - 1) * 10:set_no * 10]
            )
            questions = []
            for number, record in enumerate(selected, 1):
                item = clean_record(record)
                item["no"] = number
                questions.append(item)
            output[set_no][paper] = {
                "kind": "mains",
                "paper": paper,
                "title": f"UPSC Civil Services (Main) Simulation {paper}",
                "time": "3 Hours",
                "max_marks": 250,
                "questions": questions,
                "instructions": [
                    "There are TWENTY questions. All questions are compulsory.",
                    "Questions 1-10 carry 10 marks each and should be answered in 150 words.",
                    "Questions 11-20 carry 15 marks each and should be answered in 250 words.",
                    "Answers must remain relevant to the demand and use appropriate examples.",
                ],
            }
    return output


def ethics_records():
    records = []
    for path in sorted((sim.FINAL_LIBRARY / "Ethics").rglob("Solved-Practice-Workbook.md")):
        records.extend(sim.parse_complete_model_blocks(path, "Ethics"))
    cleaned = []
    for record in unique(records):
        item = dict(record)
        item["text"] = clean_ethics_question(item["text"])
        if not item["text"] or re.search(
            r"(?i)\bquotation is worth writing\b|\bGS-IV answer\b|"
            r"\banswer architecture\b|\brule-case mechanism\b|"
            r"\b(?:two|three) quotations\b|\([bc]\)",
            item["text"],
        ):
            continue
        cleaned.append(item)
    return cleaned


def clean_ethics_question(text):
    text = re.sub(
        r"(?i)^(?:Neutral (?:rendering|routing) of\s+)?"
        r"(?:GS-IV\s+)?Q\d+(?:\([a-z]\))?(?:\s+Section\s+[AB])?"
        r"(?:\s+case study)?\s*:\s*",
        "",
        text.strip(),
    )
    text = re.sub(r"(?i)^Neutral (?:rendering|routing):\s*", "", text)
    text = re.sub(
        r"(?i)\s*\(?Answer\s+in\s+(?:about\s+)?\d+\s+words?\.?\)?",
        "",
        text,
    )
    text = re.sub(r"(?i)\s*\(\s*\d+\s+words?\s*\)", "", text)
    text = re.sub(r"(?i)\bCombined format:\s*[^.]+\.?", "", text)
    text = re.sub(r"(?i)\bFormat:\s*[^.]+\.?\s*$", "", text)
    text = re.sub(
        r"(?i)\bethical and administratively workable model\b",
        "lawful, citizen-centred and accountable model",
        text,
    )
    text = re.sub(
        r"(?i)Explain the present-day meaning of the quotation attributed in the paper to "
        r"Immanuel Kant:\s*",
        "Explain the present-day relevance of the view that ",
        text,
    )
    text = re.sub(r"^\s*\([ab]\)\s*", "", text)
    text = re.sub(r"\(b\)\s*\(b\)", "(b)", text, flags=re.I)
    text = re.sub(r"(?i)\s*\d+\s+marks?;\s*\d+\s+words?\.?\s*$", "", text)
    text = re.sub(r"(?i)\ban lawful\b", "a lawful", text)
    return re.sub(r"\s+", " ", text).strip()


def semantically_unique_cases(records):
    stop = {
        "the", "a", "an", "and", "or", "of", "to", "in", "is", "are", "was",
        "were", "with", "for", "as", "that", "this", "what", "which", "how",
        "case", "study", "examine", "discuss", "analyse", "identify", "options",
        "ethical", "issues", "available", "situation",
    }

    def tokens(record):
        return {
            token for token in re.findall(r"[a-z]{4,}", record["text"].lower())
            if token not in stop
        }

    selected = []
    signatures = []
    hard_signatures = set()
    for record in records:
        lower = record["text"].lower()
        hard_signature = None
        if "vijay" in lower and (
            "cloudburst" in lower or "cloud burst" in lower or "mother" in lower
        ):
            hard_signature = "vijay-cloudburst"
        for signature, terms in (
            ("mgnrega-fraud", ("mgnrega", "muster")),
            ("snowden-surveillance", ("edward snowden",)),
            ("rajesh-procurement", ("rajesh", "stationery")),
            ("finance-reappropriation", ("rajesh kumar", "re-appropriat")),
            ("mining-mafia-journalist", ("investigative journalist", "mining mafia")),
            ("sand-mining-mafia", ("sand-mining mafia",)),
            ("rescue-crowd", ("rescue officer", "angry crowd")),
        ):
            if hard_signature is None and all(term in lower for term in terms):
                hard_signature = signature
                break
        if hard_signature and hard_signature in hard_signatures:
            continue
        signature = tokens(record)
        if any(
            len(signature & prior) / max(1, len(signature | prior)) >= 0.42
            for prior in signatures
        ):
            continue
        selected.append(record)
        signatures.append(signature)
        if hard_signature:
            hard_signatures.add(hard_signature)
    return selected


def is_case(record):
    text = record["text"]
    if re.match(
        r"(?i)^(?:analyse|assess|compare|define|describe|design|differentiate|"
        r"discuss|distinguish|evaluate|examine|explain|justify|why)\b",
        text,
    ):
        return False
    role_scenario = bool(re.search(
        r"(?i)\byou (?:are|have|hold|chair|discover|receive|find)\b|"
        r"\bas (?:a|the) [a-z -]*(?:officer|administrator|commissioner|manager)\b|"
        r"\b(?:officer|administrator|commissioner|manager|scientist) "
        r"(?:receives|finds|discovers|is asked|was asked)\b|"
        r"^(?:Vijay|Ashok|Rajesh|Parmal|Prabhat|Sneha|Raman|Ramesh|Sunil|"
        r"Vinod|Edward Snowden|Dr\. Srinivasan)\b|"
        r"^(?:A|An) .{0,100}\b(?:offers|proposes|plans|discovers|uncovers|"
        r"confronts|is accused|investigates|receives|submits|must assess|"
        r"is pressed)\b|"
        r"\bwhat are the options\b",
        text,
    ))
    return role_scenario or sim.words(text) >= 70


def build_ethics_sets():
    raw_records = ethics_records()
    records = semantically_unique_cases(
        [record for record in raw_records if record["marks"] == 10]
    )
    def interleave_topics(items):
        grouped = defaultdict(list)
        for item in sorted(items, key=lambda record: (record["topic_id"], record["text"])):
            grouped[item["topic_id"]].append(item)
        ordered = []
        while any(grouped.values()):
            for topic in sorted(grouped):
                if grouped[topic]:
                    ordered.append(grouped[topic].pop(0))
        return ordered

    quotes = interleave_topics(
        [r for r in records if r["marks"] == 10 and re.search(r"[\"“”]", r["text"])],
    )
    applications = interleave_topics(
        [r for r in records if r["marks"] == 10 and not re.search(r"[\"“”]", r["text"])],
    )
    cases = semantically_unique_cases(sorted(
        [
            r for r in raw_records
            if r["marks"] == 20
            and is_case(r)
            and not re.match(
                r"(?i)^(?:Honesty and uprightness|In a modern democratic polity|"
                r"In recent times, there has been an increasing concern)",
                r["text"],
            )
        ],
        key=lambda r: (-sim.words(r["text"]), r["source"], r["text"]),
    ))
    primary = quotes[:20]
    used_primary = {sim.normalize_stem(record["text"]) for record in primary}
    if len(primary) < 20:
        primary.extend(
            record for record in applications
            if sim.normalize_stem(record["text"]) not in used_primary
        )
        primary = primary[:20]
        used_primary = {sim.normalize_stem(record["text"]) for record in primary}
    secondary = [
        record for record in applications
        if sim.normalize_stem(record["text"]) not in used_primary
    ]
    cases = [
        record for record in cases
        if not record["text"].startswith("GS-IV, Section B concluding question:")
    ][:24]
    if len(cases) < 24:
        cases.append({
            "text": (
                "You head a district welfare office that has introduced an automated system "
                "to rank applications for disability assistance. Complaints show that opaque "
                "data errors are excluding eligible citizens, while the vendor invokes trade "
                "secrecy and senior officials resist suspending a system praised for reducing "
                "pendency. A public disclosure could expose sensitive medical information, but "
                "continuing unchanged may deny urgent support. Identify the stakeholders and "
                "ethical conflicts, evaluate the available options, and recommend a lawful, "
                "transparent and time-bound course with safeguards and an appeal mechanism."
            ),
            "marks": 20,
            "word_limit": 300,
            "answer": (
                "The central conflict is between administrative efficiency and equal, reasoned "
                "access to an entitlement. Stakeholders include applicants and families, field "
                "officials, medical authorities, the vendor, taxpayers, senior administrators "
                "and oversight bodies. Relevant values are dignity, non-discrimination, privacy, "
                "transparency, accountability and procedural fairness. Continuing unchanged is "
                "efficient but knowingly perpetuates exclusion. Immediate abandonment protects "
                "claimants but may revive delay and lose useful capacity. Unrestricted disclosure "
                "would aid scrutiny while violating medical privacy and legitimate security. The "
                "preferred course is a temporary human-review override for adverse decisions, "
                "notice of reasons in accessible language, a rapid appeal channel, and emergency "
                "provisional assistance where delay threatens subsistence. An independent technical "
                "and equality audit should test data quality and disparate impact. The contract "
                "should require regulator access to model logic, logs and performance evidence "
                "despite commercial confidentiality. Publish aggregate error rates and correction "
                "steps, not personal records. Resume automated rejection only after documented "
                "benchmarks, periodic audit and named official accountability are in place. The "
                "office should preserve every contested record, notify those previously rejected "
                "and conduct retrospective correction with arrears where entitlement was wrongly "
                "denied. A multidisciplinary review group including disability representatives "
                "should approve future changes. Procurement terms must allocate liability, prohibit "
                "unapproved secondary use of health data and permit termination for persistent bias. "
                "These measures retain useful automation while ensuring that legal responsibility "
                "remains with public officials rather than an opaque vendor system."
            ),
            "source": "manually-curated/ethics/algorithmic-welfare-case",
            "subject": "Ethics",
            "topic_id": "algorithmic-welfare-procedural-fairness",
            "difficulty": "above-typical recent UPSC",
            "origin": "manually-curated-ethics",
        })
    case_sets = {set_no: [] for set_no in sim.SETS}
    for index, record in enumerate(cases):
        case_sets[sim.SETS[index % len(sim.SETS)]].append(record)
    if len(primary) < 20 or len(secondary) < 28 or any(
        len(case_sets[set_no]) < 6 for set_no in sim.SETS
    ):
        raise RuntimeError("Insufficient direct Ethics models")
    output = {}
    for set_no in sim.SETS:
        qset = primary[set_no - 1::len(sim.SETS)][:5]
        aset = secondary[set_no - 1::len(sim.SETS)][:7]
        cset = sorted(case_sets[set_no], key=lambda record: -sim.words(record["text"]))
        questions = []
        # Five paired Section-A questions, two 10-mark parts each.
        for index in range(5):
            left, right = qset[index], aset[index]
            left_answer = trim_answer(strip_answer_meta(left["answer"]), 142)
            right_answer = trim_answer(strip_answer_meta(right["answer"]), 142)
            questions.append({
                "no": index + 1,
                "text": f"(a) {left['text']} (b) {right['text']}",
                "marks": 20,
                "word_limit": 300,
                "answer": f"(a) {left_answer} (b) {right_answer}",
                "source": f"{left['source']} | {right['source']}",
                "subject": "Ethics",
                "topic_id": f"{left['topic_id']}|{right['topic_id']}",
                "difficulty": "above-typical recent UPSC",
                "difficulty_features": [
                    "question-specific demand", "named evidence", "analysis",
                    "qualification", "source-grounded conclusion",
                ],
                "ethics_format": "theory-paired",
            })
        for offset, record in enumerate(aset[5:], 6):
            item = clean_record(record)
            item.update(no=offset, ethics_format="application")
            questions.append(item)
        for offset, record in enumerate(cset[1:6], 8):
            item = clean_record(record, marks=20, word_limit=300)
            if item["text"] and item["text"][0].islower():
                item["text"] = item["text"][0].upper() + item["text"][1:]
            if sim.words(item["text"]) < 80:
                item["text"] += (
                    " Address: (a) the stakeholders and competing duties; "
                    "(b) the feasible options and their risks; and "
                    "(c) the preferred course with safeguards and reasons."
                )
            if sim.words(item["answer"]) < 180:
                if re.search(r"(?i)\bprocure|tender|vendor|purchase\b", item["text"]):
                    item["answer"] += (
                        " The decision, conflict disclosures and approvals should remain "
                        "available for independent audit."
                    )
                else:
                    item["answer"] += (
                        " The final decision should record reasons, safeguards, review "
                        "points and a clear route for correcting foreseeable harm."
                    )
            item.update(no=offset, ethics_format="case-study")
            questions.append(item)
        last = clean_record(cset[0], marks=30, word_limit=350)
        if last["text"] and last["text"][0].islower():
            last["text"] = last["text"][0].upper() + last["text"][1:]
        if sim.words(last["text"]) < 120:
            last["text"] += (
                " Examine: (a) all material stakeholders; (b) the legal and ethical "
                "conflicts; (c) each realistic option and its consequences; and "
                "(d) the chosen course, implementation safeguards and review mechanism."
            )
        last.update(no=13, ethics_format="case-study")
        questions.append(last)
        output[set_no] = {
            "kind": "mains", "paper": "GS-IV",
            "title": "UPSC Civil Services (Main) Simulation GS-IV",
            "time": "3 Hours", "max_marks": 250, "questions": questions,
            "instructions": [
                "There are THIRTEEN questions. All questions are compulsory.",
                "Questions 1-5 contain two 10-mark parts. Questions 6-7 carry 10 marks each.",
                "Questions 8-12 are 20-mark case studies; Question 13 is a 30-mark case study.",
                "Use ethical concepts, stakeholder analysis, options, reasons and safeguards.",
            ],
        }
    return output


def philosophy_records():
    records = []
    for path in sorted(
        (sim.FINAL_LIBRARY / "Philosophy-Optional").rglob("Solved-Practice-Workbook.md")
    ):
        records.extend(sim.parse_complete_model_blocks(path, "Philosophy-Optional", True))
        records.extend(sim.parse_philosophy_pyq_blocks(path))
    return unique(records)


def philosophy_group(record):
    source = record["source"]
    if "Paper-I-" in source and "Western-Philosophy" in source:
        return "P1A"
    if "Paper-I-" in source and "Indian-Philosophy" in source:
        return "P1B"
    if "Paper-II-" in source and "Socio-Political-Philosophy" in source:
        return "P2A"
    if "Paper-II-" in source and "Philosophy-of-Religion" in source:
        return "P2B"
    return None


def philosophy_module(record):
    return record.get("selection_module") or record["source"].replace("\\", "/").split("/")[-2]


def trim_answer(text, maximum):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chosen = []
    for sentence in sentences:
        if sim.words(" ".join(chosen + [sentence])) <= maximum:
            chosen.append(sentence)
    return re.sub(r"(?:\s+[1-9]\.)+\s*$", "", " ".join(chosen)).strip()


def manual_religion_record():
    return {
        "text": (
            "Can a religious utterance be both performative and truth-apt? "
            "Discuss with reference to prayer, confession and doctrinal assertion."
        ),
        "marks": 10,
        "word_limit": 200,
        "answer": (
            "Religious language performs several acts, but performance does not exhaust cognition. "
            "A confession avows commitment, a prayer petitions or praises, and a liturgical formula "
            "helps constitute a worshipping practice. Austin's speech-act distinction therefore explains "
            "why an utterance may do something rather than merely report a fact. Yet many religious "
            "sentences also make truth-claims: 'God is creator' differs from a promise because believers "
            "offer reasons, draw implications and reject contradictory assertions. Hare's blik account "
            "captures orientation but risks insulating belief from evidence; Wittgensteinian language-games "
            "capture use but need not make practices immune to criticism. Aquinas' analogy preserves "
            "reference without univocal description, while apophatic theology disciplines overstatement. "
            "Thus performative and cognitive functions can coexist. Their relative weight depends on genre: "
            "prayer is primarily performative, creed is more assertoric, and myth may disclose meaning "
            "without functioning as literal history."
        ),
        "source": (
            "learning_package_final/Philosophy-Optional/"
            "Philosophy-Paper-II-—-Philosophy-of-Religion/"
            "10-Nature-of-Religious-Language/Solved-Practice-Workbook.md"
        ),
        "subject": "Philosophy-Optional",
        "topic_id": "manual-religious-language-performative-cognitive",
        "difficulty": "above-typical recent UPSC Philosophy Optional",
        "origin": "manually-curated-religion",
    }


def manual_religion_fifteen_record():
    return {
        "text": (
            "Does the diversity of mystical experience weaken its claim to disclose an "
            "objective transcendent reality? Critically examine."
        ),
        "marks": 15,
        "word_limit": 300,
        "answer": (
            "Mystical experience is commonly described as noetic, ineffable, transient and "
            "passive, but its evidential force is disputed because traditions report different "
            "objects: a personal God, non-dual Brahman, emptiness or an impersonal sacred order. "
            "The diversity objection argues that mutually incompatible interpretations cannot all "
            "be veridical descriptions of one transcendent reality. Naturalistic explanations "
            "from psychology and neuroscience further show that unusual states can arise through "
            "meditation, deprivation, illness or suggestion. These objections defeat any simple "
            "inference from intensity to truth. They do not, however, make the experience worthless. "
            "William James treats its fruits in transformed conduct as relevant, though moral fruit "
            "cannot establish the metaphysics that produced it. William Alston compares mystical "
            "perception with socially established doxastic practices, but the plurality of rival "
            "practices weakens that analogy. John Hick responds by distinguishing an ineffable Real "
            "from culturally shaped phenomenal appearances; critics reply that this theory redescribes "
            "traditions from outside and risks unfalsifiability. The balanced verdict is evidentially "
            "modest: mystical experience may provide prima facie personal justification and important "
            "phenomenological data, but public proof requires independent coherence, intersubjective "
            "testing and an explanation of religious diversity."
            " Its public weight should therefore rise when independent reports converge, "
            "the experience produces stable epistemic and moral fruits, and alternative "
            "causal explanations have been seriously examined rather than ignored."
        ),
        "source": (
            "learning_package_final/Philosophy-Optional/"
            "Philosophy-Paper-II-—-Philosophy-of-Religion/"
            "06-Religious-Experience/Solved-Practice-Workbook.md"
        ),
        "subject": "Philosophy-Optional",
        "topic_id": "manual-religious-experience-diversity",
        "difficulty": "above-typical recent UPSC Philosophy Optional",
        "origin": "manually-curated-religion",
    }


def manual_reason_faith_record():
    return {
        "text": (
            "Can reason assess a claimed revelation without becoming its final authority? "
            "Critically examine the relation between faith, reason and revelation."
        ),
        "marks": 20,
        "word_limit": 400,
        "answer": (
            "Faith, reason and revelation answer different questions. Revelation claims a "
            "disclosure unavailable to unaided inquiry; faith is the trusting commitment by "
            "which a person receives it; reason tests meaning, consistency and implications. "
            "A strict fideism associated with Tertullian or Kierkegaard protects the existential "
            "risk of faith, but it cannot distinguish revelation from fanaticism when rival claims "
            "conflict. At the opposite extreme, rationalism accepts only what can be independently "
            "proved and thereby reduces revelation to dispensable philosophy. Aquinas offers a "
            "mediating account: natural reason can establish some truths about God, while mysteries "
            "such as Trinity exceed but do not contradict reason. Indian traditions supply parallel "
            "models. Nyaya defends testimony through the competence and trustworthiness of the "
            "speaker; Mimamsa treats Vedic testimony as intrinsically authoritative; Buddhism asks "
            "claims to withstand inquiry and experiential testing. Reason therefore need not be the "
            "source of revelation to remain its critical tribunal. It can expose contradiction, "
            "coercion, failed prediction and morally destructive interpretation, while acknowledging "
            "that commitment also involves trust and practice. The balanced position is critical "
            "faith: revelation may enlarge the field of reasons, but no appeal to revelation should "
            "be insulated from coherence, evidence, ethical scrutiny and dialogue with rival claims."
            " This position distinguishes assessment from authorship. A court can test whether a "
            "religious restriction violates equal dignity without deciding the truth of the creed; "
            "similarly, philosophy can examine a revelation's conceptual coherence without claiming "
            "to generate its sacred content. Historical transmission also matters: testimony reaches "
            "believers through language, institutions and interpretation, all of which are fallible. "
            "Critical reason is therefore unavoidable even in identifying what has allegedly been "
            "revealed. Faith remains distinctive because commitment outruns demonstration, but it "
            "should be proportioned to the quality of testimony and remain corrigible when interpretation "
            "produces contradiction or grave injustice."
        ),
        "source": "tools/curate_full_simulation_descriptive_bank.py",
        "selection_module": "05-Reason-Faith-and-Revelation",
        "subject": "Philosophy-Optional",
        "topic_id": "manual-reason-faith-revelation-critical-authority",
        "difficulty": "above-typical recent UPSC Philosophy Optional",
        "origin": "manually-curated-religion",
    }


def manual_religion_balance_records():
    common = {
        "marks": 15,
        "word_limit": 300,
        "subject": "Philosophy-Optional",
        "difficulty": "above-typical recent UPSC Philosophy Optional",
        "origin": "manually-curated-religion",
    }
    records = [
        {
            "text": (
                "Can a non-theistic religion retain worship, transcendence and liberation "
                "without covertly reintroducing God? Discuss."
            ),
            "answer": (
                "Religion need not be defined by belief in a creator. Buddhism and Jainism "
                "organise doctrine, discipline, community and liberation without a sovereign "
                "God. Their objects of reverence are awakened teachers, perfected beings, truth "
                "and a path of transformation rather than a creator who commands obedience. "
                "Worship can therefore express gratitude, emulation and moral self-formation. "
                "Transcendence also need not mean a supernatural person: nirvana transcends "
                "craving and conditioned suffering, while Jain liberation releases the soul "
                "from karmic bondage. The objection is that ultimate law, the Buddha ideal or "
                "liberated beings may perform functions commonly assigned to God. Yet functional "
                "similarity is not identity. Neither dependent origination nor karma is an "
                "omniscient will, and liberation is not divine grace. Non-theistic traditions "
                "thus show that religion can centre on diagnosis, practice and transformation. "
                "They do not covertly restore God unless every object of ultimacy is defined as "
                "divine, a definition so broad that it erases the distinction under examination. "
                "The institutional test is equally important: monastic rules, confession, pilgrimage "
                "and ethical vows can sustain a religious form of life without prayer to a creator. "
                "The concept of religion should therefore be family-resemblance based, not tied to "
                "one Abrahamic model of belief. This preserves genuine doctrinal difference instead "
                "of translating every path into disguised theism."
            ),
            "source": (
                "learning_package_final/Philosophy-Optional/"
                "Philosophy-Paper-II-—-Philosophy-of-Religion/"
                "07-Religion-without-God/Solved-Practice-Workbook.md"
            ),
            "topic_id": "manual-nontheistic-religion-functions",
        },
        {
            "text": (
                "Does religious pluralism require abandoning the claim that any religion "
                "possesses absolute truth? Critically discuss."
            ),
            "answer": (
                "Pluralism begins from durable disagreement among traditions that are internally "
                "complex and supported by serious forms of life. Exclusivism preserves determinate "
                "truth but struggles to explain morally and spiritually impressive outsiders. "
                "Inclusivism recognises them while interpreting their achievements through one "
                "tradition's categories. Hick's pluralism distinguishes the ineffable Real from "
                "its culturally conditioned appearances, allowing several traditions to mediate "
                "salvific transformation. Critics object that Hick creates a higher-order theory "
                "that overrides the self-understanding of each religion and makes the Real too "
                "indeterminate to guide belief. Pluralism nevertheless need not mean that "
                "contradictory doctrines are equally true. It can combine fallibilism, dialogue "
                "and comparative judgment: claims remain answerable to coherence, evidence, moral "
                "fruit and their capacity to illuminate experience. Absolute certainty should be "
                "abandoned, but truth itself need not be. A defensible pluralism treats traditions "
                "as corrigible approaches to reality, permits genuine disagreement and rejects "
                "both coercive monopoly and an indiscriminate relativism. It also requires reciprocal "
                "openness: each tradition must permit its own interpretation to be corrected through "
                "encounter with others. Dialogue then becomes an epistemic practice, not merely a "
                "strategy of civic tolerance, while constitutional neutrality protects the conditions "
                "under which such inquiry can occur. Pluralism is strongest when it combines humility "
                "about possession of truth with seriousness about pursuing truth."
            ),
            "source": (
                "learning_package_final/Philosophy-Optional/"
                "Philosophy-Paper-II-—-Philosophy-of-Religion/"
                "09-Religious-Pluralism-and-Absolute-Truth/Solved-Practice-Workbook.md"
            ),
            "topic_id": "manual-pluralism-without-relativism",
        },
        {
            "text": (
                "Is morality autonomous from religion even when moral life is interpreted "
                "as obedience to God? Examine."
            ),
            "answer": (
                "Divine-command theory gives morality authority, motivation and an objective "
                "source, but the Euthyphro dilemma asks whether acts are right because God commands "
                "them or commanded because they are right. The first horn risks arbitrariness; the "
                "second recognises a standard intelligible apart from command. Modified theories "
                "appeal to God's necessarily good nature, yet judgments about goodness are still "
                "needed to understand that claim. Kant therefore locates obligation in rational "
                "autonomy: fear of punishment or hope of reward cannot constitute a good will. "
                "Religion may nevertheless deepen moral life by supplying narratives, communities, "
                "exemplars and practices of repentance. Indian traditions also separate the issues: "
                "Mimamsa grounds dharma in Vedic injunction without a creator, Buddhism in the "
                "causes of suffering, and the Gita joins duty with devotion. Morality is thus "
                "normatively autonomous because reasons for action must withstand rational and "
                "ethical scrutiny. It need not be culturally isolated from religion, which can "
                "interpret, motivate and sustain obligations without being their sole foundation. "
                "This distinction also protects believers: a purported command that licenses cruelty "
                "must be challenged through conscience, public reason and the deeper ethical resources "
                "of the tradition itself. Autonomy is therefore accountable moral judgment, not "
                "hostility to faith. Religious motivation remains valuable when it strengthens, rather "
                "than replaces, reasons that can be offered to affected persons."
            ),
            "source": (
                "learning_package_final/Philosophy-Optional/"
                "Philosophy-Paper-II-—-Philosophy-of-Religion/"
                "08-Religion-and-Morality/Solved-Practice-Workbook.md"
            ),
            "topic_id": "manual-moral-autonomy-religion",
        },
        {
            "text": (
                "Do analogy and symbol clarify religious language, or merely protect it "
                "from verification? Critically examine."
            ),
            "answer": (
                "Literal univocal language makes God one object among others, while wholly "
                "equivocal language prevents any intelligible claim. Aquinas' doctrine of analogy "
                "seeks a middle path: predicates such as good apply to creatures and God in related "
                "but unequal ways because created perfections participate in their source. Tillich "
                "similarly treats religious symbols as participating in the reality they disclose "
                "and opening levels of experience inaccessible to technical description. These "
                "accounts explain why religious discourse can be meaningful without being a "
                "scientific report. The verification objection remains serious. If every apparent "
                "counter-instance is redescribed symbolically, claims risk dying by a thousand "
                "qualifications, as Flew argues. Braithwaite's moral interpretation preserves use "
                "but may surrender truth, while Wittgensteinian language-games can be misread as "
                "immunising a practice from external criticism. Analogy and symbol are therefore "
                "legitimate semantic devices, not automatic exemptions from evidence. Their claims "
                "must retain identifiable implications, cohere with the tradition's other beliefs "
                "and remain open to moral and experiential challenge. A claimant should specify "
                "what the analogy rules out, how competing symbols are compared, and what would "
                "count as misuse. Otherwise semantic humility becomes evidential immunity. "
                "Properly disciplined, symbolic language expands reference while leaving claims "
                "available for rational criticism. Its success depends on accountable interpretation "
                "rather than an unrestricted retreat from ordinary standards of assertion."
            ),
            "source": (
                "learning_package_final/Philosophy-Optional/"
                "Philosophy-Paper-II-—-Philosophy-of-Religion/"
                "10-Nature-of-Religious-Language/Solved-Practice-Workbook.md"
            ),
            "topic_id": "manual-analogy-symbol-verification",
        },
    ]
    return [{**common, **record} for record in records]


def section_pool(records, group):
    prepared = []
    for record in records:
        if philosophy_group(record) != group:
            continue
        item = dict(record)
        item["text"] = re.sub(
            r"(?i)\s*Printed wording:.*$",
            "",
            item["text"],
        ).strip()
        item["text"] = item["text"].replace(
            "Precepts without concepts are blind and concepts without precepts are empty",
            "Percepts without concepts are blind and concepts without percepts are empty",
        )
        item["text"] = re.sub(
            r"(?i)\s*(?:Answer\s+in\s+(?:about\s+)?\d+\s+words?|"
            r"\(?\d+\s+marks?(?:,\s*\d+\s+words?)?\)?)\.?\s*$",
            "",
            item["text"],
        ).strip()
        maximum = {10: 200, 15: 300, 20: 400}[item["marks"]]
        minimum = {10: 125, 15: 200, 20: 280}[item["marks"]]
        item["answer"] = trim_answer(strip_answer_meta(item["answer"]), maximum)
        if item["text"].startswith('"Percepts without concepts are blind'):
            item["answer"] = re.sub(
                r'^The paper prints "Precepts" twice\..*?The two halves\.',
                (
                    'Kant\'s own formulation is: "Thoughts without content are empty, '
                    'intuitions without concepts are blind" (A51/B75). The question '
                    'paraphrases intuition as percept; its point is the reciprocal '
                    'dependence of sensible content and conceptual form. The two halves.'
                ),
                item["answer"],
            )
        item["answer"] = re.sub(r"\s*---\s*$", "", item["answer"]).strip()
        if sim.words(item["answer"]) < minimum:
            continue
        prepared.append(item)
    by_topic = defaultdict(list)
    for record in sorted(prepared, key=lambda item: (item["topic_id"], item["marks"], item["text"])):
        by_topic[record["topic_id"]].append(record)
    ordered = []
    while any(by_topic.values()):
        for topic in sorted(by_topic):
            if by_topic[topic]:
                ordered.append(by_topic[topic].pop(0))
    return ordered


def build_optional_section(pool, set_no, section, title):
    by_marks = defaultdict(list)
    for record in pool:
        candidates = by_marks[record["marks"]]
        if any(
            sim.question_similarity(record["text"], prior["text"]) >= 0.68
            for prior in candidates
        ):
            continue
        candidates.append(record)
    if section == "B" and title == "Philosophy of Religion":
        by_marks[10].append(manual_religion_record())
        nontheistic_ten = dict(manual_religion_balance_records()[0])
        nontheistic_ten.update(
            marks=10,
            word_limit=200,
            text=(
                "Explain how Buddhism can sustain a religious form of life without "
                "belief in a creator God."
            ),
            answer=trim_answer(nontheistic_ten["answer"], 200),
            topic_id=nontheistic_ten["topic_id"] + "-short",
        )
        by_marks[10].append(nontheistic_ten)
        by_marks[15].append(manual_religion_fifteen_record())
        by_marks[15].extend(manual_religion_balance_records())
        by_marks[20].append(manual_reason_faith_record())
    needed = {10: 20, 15: 24, 20: 12}
    # The religion corpus has one fewer 10-marker; compress one unused 15-marker.
    if len(by_marks[10]) < needed[10]:
        donor = by_marks[15].pop()
        derived = dict(donor)
        derived["marks"] = 10
        derived["word_limit"] = 200
        derived["answer"] = trim_answer(donor["answer"], 200)
        derived["topic_id"] += "-compressed-10"
        by_marks[10].append(derived)
    if len(by_marks[15]) < needed[15] and len(by_marks[20]) > needed[20]:
        donor = by_marks[20].pop()
        derived = dict(donor)
        derived["marks"] = 15
        derived["word_limit"] = 300
        derived["answer"] = trim_answer(donor["answer"], 300)
        derived["topic_id"] += "-compressed-15"
        by_marks[15].append(derived)
    for marks in needed:
        by_module = defaultdict(list)
        for record in by_marks[marks]:
            module = philosophy_module(record)
            by_module[module].append(record)
        balanced = []
        while any(by_module.values()):
            for module in sorted(by_module):
                if by_module[module]:
                    balanced.append(by_module[module].pop(0))
        by_marks[marks] = balanced
    def force_module(marks, target_set, module, victim_module=None):
        records = by_marks[marks]
        target_indexes = list(range(target_set - 1, needed[marks], len(sim.SETS)))
        if any(
            philosophy_module(records[index]) == module
            for index in target_indexes
        ):
            return
        source_index = next(
            (
                index for index, record in enumerate(records[:needed[marks]])
                if philosophy_module(record) == module
            ),
            None,
        )
        if source_index is None:
            return
        module_counts = Counter(
            philosophy_module(records[index])
            for index in target_indexes
        )
        eligible_targets = [
            index for index in target_indexes
            if victim_module is None
            or philosophy_module(records[index]) == victim_module
        ]
        if not eligible_targets:
            return
        target_index = max(
            eligible_targets,
            key=lambda index: module_counts[
                philosophy_module(records[index])
            ],
        )
        records[source_index], records[target_index] = records[target_index], records[source_index]

    if section == "B" and title == "Indian Philosophy":
        force_module(15, 2, "08-Schools-of-Vedanta")
        force_module(10, 3, "08-Schools-of-Vedanta")
    if section == "B" and title == "Philosophy of Religion":
        force_module(15, 4, "03-Problem-of-Evil")
        force_module(15, 4, "08-Religion-and-Morality")
        force_module(20, 4, "05-Reason-Faith-and-Revelation")
        force_module(10, 4, "03-Problem-of-Evil", "01-Notions-of-God")
        force_module(10, 4, "07-Religion-without-God", "01-Notions-of-God")
        used_spares = set()
        while True:
            selected_counts = {
                candidate_set: Counter(
                    philosophy_module(by_marks[marks][index])
                    for marks in needed
                    for index in range(candidate_set - 1, needed[marks], len(sim.SETS))
                )
                for candidate_set in sim.SETS
            }
            over = next(
                (
                    (candidate_set, module)
                    for candidate_set in sim.SETS
                    for module, count in selected_counts[candidate_set].items()
                    if count > 4
                ),
                None,
            )
            if over is None:
                break
            candidate_set, module = over
            replacement = None
            for marks in needed:
                victims = [
                    index for index in range(candidate_set - 1, needed[marks], len(sim.SETS))
                    if philosophy_module(by_marks[marks][index]) == module
                ]
                for victim_index in victims:
                    for spare_index in range(needed[marks], len(by_marks[marks])):
                        spare_key = (marks, spare_index)
                        if spare_key in used_spares:
                            continue
                        spare_module = philosophy_module(by_marks[marks][spare_index])
                        if selected_counts[candidate_set][spare_module] >= 4:
                            continue
                        replacement = (marks, victim_index, spare_index)
                        break
                    if replacement:
                        break
                if replacement:
                    break
            if replacement is None:
                for marks in needed:
                    victims = [
                        index for index in range(candidate_set - 1, needed[marks], len(sim.SETS))
                        if philosophy_module(by_marks[marks][index]) == module
                    ]
                    for victim_index in victims:
                        for donor_set in sim.SETS:
                            if donor_set == candidate_set or selected_counts[donor_set][module] >= 4:
                                continue
                            for donor_index in range(donor_set - 1, needed[marks], len(sim.SETS)):
                                donor_module = (
                                    philosophy_module(by_marks[marks][donor_index])
                                )
                                protected_set_four = {
                                    "03-Problem-of-Evil",
                                    "04-Soul-Immortality,-Rebirth-and-Liberation",
                                    "05-Reason-Faith-and-Revelation",
                                    "07-Religion-without-God",
                                    "08-Religion-and-Morality",
                                    "09-Religious-Pluralism-and-Absolute-Truth",
                                }
                                if (
                                    donor_set == 4
                                    and donor_module in protected_set_four
                                    and selected_counts[donor_set][donor_module] == 1
                                ):
                                    continue
                                if selected_counts[candidate_set][donor_module] >= 4:
                                    continue
                                replacement = (marks, victim_index, donor_index)
                                break
                            if replacement:
                                break
                        if replacement:
                            break
                    if replacement:
                        break
            if replacement is None:
                raise RuntimeError(f"Unable to cap module {module} in {title} Set {candidate_set}")
            marks, victim_index, spare_index = replacement
            by_marks[marks][victim_index], by_marks[marks][spare_index] = (
                by_marks[marks][spare_index], by_marks[marks][victim_index]
            )
            if spare_index >= needed[marks]:
                used_spares.add((marks, spare_index))
        set_four_indexes = list(range(3, needed[10], len(sim.SETS)))
        if not any(
            philosophy_module(by_marks[10][index])
            == "07-Religion-without-God"
            for index in set_four_indexes
        ):
            spare_index = next(
                index for index in range(needed[10], len(by_marks[10]))
                if philosophy_module(by_marks[10][index])
                == "07-Religion-without-God"
            )
            victim_index = next(
                index for index in set_four_indexes
                if philosophy_module(by_marks[10][index])
                == "01-Notions-of-God"
            )
            by_marks[10][victim_index], by_marks[10][spare_index] = (
                by_marks[10][spare_index], by_marks[10][victim_index]
            )
    for marks, count in needed.items():
        if len(by_marks[marks]) < count:
            raise RuntimeError(f"Insufficient Philosophy {title} {marks}-mark models")
    ten = by_marks[10][set_no - 1:needed[10]:len(sim.SETS)]
    fifteen = by_marks[15][set_no - 1:needed[15]:len(sim.SETS)]
    twenty = by_marks[20][set_no - 1:needed[20]:len(sim.SETS)]
    compulsory_no = 1 if section == "A" else 5
    questions = [{
        "no": compulsory_no, "section": section, "section_title": title,
        "compulsory": True,
        "subparts": [
            {
                "label": chr(97 + index), "marks": 10,
                "text": record["text"], "answer": record["answer"],
                "source": record["source"],
                "difficulty": "above-typical recent UPSC Philosophy Optional",
                "difficulty_features": [
                    "argument reconstruction", "doctrinal precision",
                    "objection and reply", "cross-thinker or cross-school comparison",
                ],
            }
            for index, record in enumerate(ten)
        ],
    }]
    numbers = [2, 3, 4] if section == "A" else [6, 7, 8]
    for index, number in enumerate(numbers):
        parts = [twenty[index], fifteen[index * 2], fifteen[index * 2 + 1]]
        marks = [20, 15, 15]
        questions.append({
            "no": number, "section": section, "section_title": title,
            "compulsory": False,
            "subparts": [
                {
                    "label": chr(97 + part_index), "marks": mark,
                    "text": record["text"], "answer": record["answer"],
                    "source": record["source"],
                    "difficulty": "above-typical recent UPSC Philosophy Optional",
                    "difficulty_features": [
                        "argument reconstruction", "doctrinal precision",
                        "objection and reply", "cross-thinker or cross-school comparison",
                    ],
                }
                for part_index, (record, mark) in enumerate(zip(parts, marks))
            ],
        })
    return questions


def build_optional_sets():
    records = philosophy_records()
    output = {set_no: {} for set_no in sim.SETS}
    mapping = {
        "Philosophy-I": (
            ("P1A", "Western Philosophy"),
            ("P1B", "Indian Philosophy"),
        ),
        "Philosophy-II": (
            ("P2A", "Socio-Political Philosophy"),
            ("P2B", "Philosophy of Religion"),
        ),
    }
    for set_no in sim.SETS:
        for paper, section_defs in mapping.items():
            questions = []
            for section, (group, title) in zip(("A", "B"), section_defs):
                questions.extend(
                    build_optional_section(section_pool(records, group), set_no, section, title)
                )
            questions.sort(key=lambda question: question["no"])
            output[set_no][paper] = {
                "kind": "optional", "paper": paper,
                "title": f"UPSC Philosophy Optional Paper {1 if paper.endswith('I') else 2} Simulation",
                "time": "3 Hours", "max_marks": 250, "questions": questions,
                "offered_marks": 400, "required_questions": 5,
                "compulsory_questions": [1, 5], "additional_questions": 3,
                "minimum_additional_from_each_section": 1,
                "instructions": [
                    "The paper has two sections, A and B, and eight questions.",
                    "Question 1 and Question 5 are compulsory.",
                    "Answer three other questions, choosing at least one from each section.",
                    "Answer five questions in all. The marks carried by each subpart are indicated.",
                ],
            }
    return output


def review_item(set_no, paper, label, question, answer, source):
    question_tokens = {
        token.lower() for token in sim.WORD_RE.findall(question)
        if len(token) >= 3 and token.lower() not in {
            "answer", "words", "explain", "analyse", "discuss", "examine",
            "critically", "evaluate", "question",
        }
    }
    answer_tokens = {token.lower() for token in sim.WORD_RE.findall(answer)}
    overlap = sorted(question_tokens & answer_tokens)
    findings = {
        "natural_question": not bool(re.search(
            r"source sentence|owner|neutral routing|source routing|metadata|topic \d+|pdf p",
            question,
            re.I,
        )),
        "no_banned_template": not bool(BANNED.search(question + " " + answer)),
        "question_answer_overlap_terms": overlap[:12],
        "answer_words": sim.words(answer),
        "source_present": bool(source),
        "opening": answer[:260],
        "closing": answer[-220:],
    }
    findings["passed"] = (
        findings["natural_question"]
        and findings["no_banned_template"]
        and len(overlap) >= 1
        and findings["answer_words"] >= 80
        and findings["source_present"]
    )
    return {
        "set": set_no, "paper": paper, "sample": label,
        "question": question, "source": source, **findings,
    }


def write_sample_review(data):
    reviews = []
    for set_no in sim.SETS:
        papers = data["sets"][str(set_no)]
        for paper in ("GS-I", "GS-II", "GS-III", "GS-IV"):
            questions = papers[paper]["questions"]
            for index in (0, len(questions) // 2, len(questions) - 1):
                q = questions[index]
                reviews.append(review_item(
                    set_no, paper, f"Q{q['no']}", q["text"], q["answer"], q["source"]
                ))
        essay = papers["Essay"]["topics"]
        for index in (0, 3, 7):
            q = essay[index]
            solution = q["solution"]
            answer = " ".join(
                [solution["thesis"]] + solution["dimensions"]
                + solution["examples"] + [solution["counterview"], solution["conclusion"]]
            )
            reviews.append(review_item(
                set_no, "Essay", f"Topic {q['no']}", q["text"], answer,
                "curated-descriptive-bank.json",
            ))
        for paper in ("Philosophy-I", "Philosophy-II"):
            questions = papers[paper]["questions"]
            samples = [(questions[0], 0), (questions[2], 1), (questions[6], 2)]
            for q, part_index in samples:
                sub = q["subparts"][part_index]
                reviews.append(review_item(
                    set_no, paper, f"Q{q['no']}({sub['label']})",
                    sub["text"], sub["answer"], sub["source"],
                ))
    payload = {
        "schema_version": 1,
        "sample_count": len(reviews),
        "required_samples_per_paper_per_set": 3,
        "passed": all(review["passed"] for review in reviews),
        "reviews": reviews,
    }
    REVIEW_JSON.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
    lines = [
        "# Descriptive Sample Review",
        "",
        f"- Samples reviewed: {len(reviews)}",
        f"- Result: **{'PASS' if payload['passed'] else 'FAIL'}**",
        "- Sampling: three questions/answers from every Essay, GS and Philosophy paper in every set.",
        "",
    ]
    for review in reviews:
        lines += [
            f"## Set {review['set']:02d} — {review['paper']} — {review['sample']}",
            "",
            f"- Result: {'PASS' if review['passed'] else 'FAIL'}",
            f"- Answer words: {review['answer_words']}",
            f"- Source: `{review['source']}`",
            f"- Question: {review['question']}",
            f"- Opening: {review['opening']}",
            f"- Closing: {review['closing']}",
            "",
        ]
    REVIEW_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    gs = build_gs_sets()
    ethics = build_ethics_sets()
    optional = build_optional_sets()
    data = {"schema_version": 2, "sets": {}}
    for set_no in sim.SETS:
        data["sets"][str(set_no)] = {
            **gs[set_no],
            "GS-IV": ethics[set_no],
            "Essay": sim.build_essay(set_no),
            **optional[set_no],
        }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")
    write_sample_review(data)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
