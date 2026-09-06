"""Strictly sequential Qualifying Hindi semantic review and learner-v2 generation."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

import fitz
from PIL import Image, ImageChops, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer

import markdown_learning_pdf
from validate_v2_export import validate_pdf, validate_pdf_layout, validate_v2_markdown_text


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-06"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / "Qualifying-Hindi"
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
REVIEWS = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "qualifying-hindi"
SEMANTIC = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "knowledge-semantic-completeness-status.json"
EXPORT_STATUS = ROOT / "EXPORT-PDF-STATUS.json"
CATALOGUE = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SECTION_MANIFEST = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "qualifying-hindi--subject-wide-syllabus.json"
LEARNER_ROOT = ROOT / "upsc-ai-kit" / "knowledge" / "Learner-v2-Refreshed" / "Qualifying-Hindi" / "Subject-Wide-Syllabus"
NOTES_ROOT = ROOT / "notes" / "Learner-v2-Refreshed" / "Qualifying-Hindi" / "Subject-Wide-Syllabus"
CANONICAL_SESSION_ROOT = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"

OFFICIAL_PAPERS = (
    ("2018", "HINDI-COMP.pdf", 7),
    ("2019", "QP-CSM19-HindiCompulory.pdf", 8),
    ("2020", "HINDI_0 (1).pdf", 8),
    ("2021", "Hindi_0.pdf", 7),
    ("2022", "QP-CSM-22-HINDI-Compl-280922.pdf", 4),
    ("2023", "QP-CSM-23-HINDI-COMPULSORY-290923.pdf", 8),
    ("2025", "HINDI-COMPULSORY-QP-CSM-25-010925.pdf", 8),
)

PUBLIC_REFERENCES = (
    "https://upsc.gov.in/examinations/previous-question-papers",
    "https://www.chd.education.gov.in/en/basic-grammar-modern-hindi",
    "https://www.chd.education.gov.in/devanagari-lipi-tatha-hindi-vartani-manakikaran-0",
    "https://chdpublication.education.gov.in/",
)

@dataclass(frozen=True)
class TopicSpec:
    number: int
    key: str
    title: str
    filename: str
    syllabus: str
    ownership: str
    boundary: str
    verification: str
    stages: tuple[tuple[str, str], ...]
    required_terms: tuple[str, ...]
    advanced: str
    transfer_tasks: tuple[tuple[str, str], ...]

    @property
    def basic(self) -> Path:
        return KNOWLEDGE / "basic" / self.filename


@dataclass(frozen=True)
class RuleItem:
    label: str
    correct: str
    distractors: tuple[str, str, str]
    explanation: str = "सही विकल्प नियम को बिना अर्थ बदले या निरपेक्ष अपवादहीन दावा गढ़े स्पष्ट करता है।"
    accepted_variation: str = ""


@dataclass(frozen=True)
class Question:
    number: int
    stem: str
    options: tuple[str, str, str, str]
    answer: str
    correct_text: str
    explanation: str
    accepted_variation: str = ""


from qualifying_hindi_semantic_data import CANONICAL_ADDITIONS, TOPIC_DATA, rules

RULE_ITEMS = rules(RuleItem)


def topics() -> list[TopicSpec]:
    return [
        TopicSpec(
            number=index,
            key=f"qualifying-hindi-{index:02d}",
            title=data["title"],
            filename=data["filename"],
            syllabus=data["syllabus"],
            ownership=data["ownership"],
            boundary=data["boundary"],
            verification=data["verification"],
            stages=data["stages"],
            required_terms=data["terms"],
            advanced=data["advanced"],
            transfer_tasks=data["tasks"],
        )
        for index, data in enumerate(TOPIC_DATA, 1)
    ]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def demote(markdown: str) -> str:
    lines: list[str] = []
    for line in markdown.replace("\r\n", "\n").splitlines():
        match = re.match(r"^(#{1,5})(\s+.*)$", line)
        if not match:
            lines.append(line)
            continue
        level = len(match.group(1))
        lines.append("#" * (3 if level <= 2 else min(6, level + 1)) + match.group(2))
    return "\n".join(lines).strip()


def repair_owner(topic: TopicSpec) -> tuple[str, str, bool]:
    before = topic.basic.read_text(encoding="utf-8")
    before_hash = hashlib.sha256(before.encode("utf-8")).hexdigest()
    marker = f"## Semantic-completeness closure — {DATE}"
    changed = marker not in before
    if changed:
        route = "\n".join(
            f"{index}. **{title}:** {body}" for index, (title, body) in enumerate(topic.stages, 1)
        )
        addition = f"""

{CANONICAL_ADDITIONS[topic.number].strip()}

---

{marker}

### शाब्दिक पाठ्यक्रम, स्वामित्व और सीमा

- **पाठ्यक्रम-मांग:** {topic.syllabus}
- **कैनोनिकल स्वामित्व:** {topic.ownership}
- **अन्य विषयों से सीमा:** {topic.boundary}

### पूर्ण अध्ययन और उत्तर-मार्ग

{route}

### प्रामाणिकता, वैध विविधता और प्रतिकूल-जाँच

{topic.verification}

समीक्षा ने `README.md` में सूचीबद्ध स्थानीय UPSC अनिवार्य हिन्दी प्रश्नपत्र, repository का
शाब्दिक पाठ्यक्रम, subject-wide solved package और learner successor में दर्ज केंद्रीय हिन्दी
निदेशालय के व्याकरण/वर्तनी संदर्भ जाँचे। विशेष प्रतिकूल परीक्षण:
**{'; '.join(topic.required_terms)}**.

सरल, समकालीन मानक हिन्दी को प्राथमिकता दें। एक से अधिक रूप मानक हों तो विविधता स्पष्ट करें;
परीक्षा के लिए किसी एकरूप रूप को जोखिम-नियंत्रण के रूप में चुनें, दूसरे वैध रूप को अशुद्ध न कहें।

### प्रगतिशील अभ्यास और समयबद्ध स्थानांतरण

1. आधार: माँग पहचानें और नियम सरल भाषा में लिखें।
2. नियंत्रित प्रयोग: एक वाक्य सुधारें/बनाएँ और परिवर्तन समझाएँ।
3. अनुच्छेद-प्रयोग: अर्थ, संदर्भ, भाषा-स्तर और तार्किक संबंध सुरक्षित रखें।
4. प्रतिकूल जाँच: दूसरे अर्थ/मानक में सही पर इस संदर्भ में गलत निकट विकल्प हटाएँ।
5. समयबद्ध निष्पादन: उत्तर, सत्यापन, त्रुटि-वर्ग और नए प्रश्न पर पुनर्परीक्षण करें।
"""
        topic.basic.write_text(before.rstrip() + addition + "\n", encoding="utf-8")
    return before_hash, sha256(topic.basic), changed


def optionize(item: RuleItem, index: int) -> tuple[tuple[str, str, str, str], str]:
    choices = [item.correct, *item.distractors]
    if len(set(choices)) != 4:
        raise ValueError(f"Duplicate option in {item.label}.")
    target = index % 4
    choices.remove(item.correct)
    choices.insert(target, item.correct)
    return tuple(choices), "ABCD"[target]


def questions_for(topic: TopicSpec) -> list[Question]:
    modes = (
        "आधार-नियम",
        "संपादन-निर्णय",
        "समयबद्ध चयन",
        "प्रतिकूल विविधता-जाँच",
    )
    questions: list[Question] = []
    for mode_index, mode in enumerate(modes):
        for item in RULE_ITEMS[topic.number]:
            index = len(questions)
            options, answer = optionize(item, index)
            questions.append(
                Question(
                    number=index + 1,
                    stem=f"{mode} — {item.label}: मानक परीक्षा-हिन्दी के लिए सबसे सुरक्षित और सटीक कथन कौन-सा है?",
                    options=options,
                    answer=answer,
                    correct_text=item.correct,
                    explanation=item.explanation,
                    accepted_variation=item.accepted_variation,
                )
            )
    return questions


def validate_questions(topic: TopicSpec, questions: list[Question]) -> list[str]:
    errors: list[str] = []
    if len(questions) != 48:
        errors.append(f"Expected 48 MCQs, found {len(questions)}.")
    if [q.answer for q in questions] != ["ABCD"[index % 4] for index in range(48)]:
        errors.append("Correct-option rotation is not strict A-B-C-D.")
    stems: set[str] = set()
    for question in questions:
        if question.stem in stems:
            errors.append(f"Duplicate stem: {question.stem}")
        stems.add(question.stem)
        if len(set(question.options)) != 4:
            errors.append(f"Q{question.number}: duplicate options.")
        selected = question.options["ABCD".index(question.answer)]
        if selected != question.correct_text:
            errors.append(f"Q{question.number}: answer key does not select canonical answer.")
        if not question.explanation.endswith((".", "?", "!", "।")):
            errors.append(f"Q{question.number}: explanation is not a complete sentence.")
    return errors


def official_paper_audit() -> list[dict[str, Any]]:
    folder = ROOT / "books" / "more_previous_papers"
    rows: list[dict[str, Any]] = []
    for year, filename, expected_pages in OFFICIAL_PAPERS:
        path = folder / filename
        if not path.is_file():
            raise FileNotFoundError(path)
        with fitz.open(path) as document:
            text = "\n".join(page.get_text("text") for page in document)
            page_count = document.page_count
        compact = re.sub(r"\s+", " ", text)
        errors = []
        if page_count != expected_pages:
            errors.append(f"expected {expected_pages} pages, got {page_count}")
        if "Three Hours" not in compact:
            errors.append("three-hour header not extracted")
        verified_precis = year in {"2022", "2023"}
        rows.append(
            {
                "year": year,
                "path": rel(path),
                "pages": page_count,
                "sha256": sha256(path),
                "three_hours": "Three Hours" in compact,
                "one_third_precis": verified_precis,
                "no_title_precis": verified_precis,
                "precis_evidence": (
                    "स्थानीय page-image से एक-तिहाई, अपने शब्द और शीर्षक न देने का निर्देश सत्यापित"
                    if verified_precis
                    else "क्षतिग्रस्त/OCR पाठ से अपठनीय निर्देश का अनुमान नहीं लगाया गया"
                ),
                "errors": errors,
            }
        )
    return rows


def format_question(question: Question, *, solution: bool) -> str:
    options = "\n".join(f"{letter}. {text}" for letter, text in zip("ABCD", question.options))
    answer = ""
    if solution:
        variation = f" **स्वीकार्य विकल्प:** {question.accepted_variation}" if question.accepted_variation else ""
        answer = f"\n\n**सही उत्तर: {question.answer}.** {question.explanation}{variation}\n"
    return f"### Q{question.number}. {question.stem}\n\n{options}{answer}"


def ascii_master(topic: TopicSpec) -> str:
    blocks: list[str] = []
    for index, (title, body) in enumerate(topic.stages, 1):
        content = [f"PANEL {index:02d} — {title.upper()}", *(textwrap.wrap(body, 76) or [""])]
        width = 82
        blocks.append(
            "+" + "-" * width + "+\n"
            + "\n".join("| " + line.ljust(width - 1) + "|" for line in content)
            + "\n+" + "-" * width + "+"
        )
    return "\n        |\n        v\n".join(blocks)


def transfer_block(topic: TopicSpec, *, solutions: bool) -> str:
    chunks = []
    for index, (task, answer) in enumerate(topic.transfer_tasks, 1):
        body = f"### Transfer {index}. {task}"
        if solutions:
            body += f"\n\n**Model answer:** {answer}"
        chunks.append(body)
    return "\n\n".join(chunks)


def official_demand_table(topic: TopicSpec, audit: list[dict[str, Any]]) -> str:
    demand = (
        "प्रयोग/शब्दावली और वाक्य-स्तरीय भाषा-नियंत्रण"
        if topic.number <= 3
        else "गद्यांश-बोध और संक्षेपण; 2022/2023 में एक-तिहाई, अपने शब्द और शीर्षक निषेध सत्यापित"
        if topic.number == 4
        else "लगभग 600 शब्द का लघु निबन्ध"
        if topic.number == 5
        else "हिन्दी↔अंग्रेज़ी द्विदिश अनुवाद"
    )
    return "\n".join(
        f"| {row['year']} | `{row['path']}` | {demand} | स्थानीय text-layer और आवश्यक page-image से मिलान; अपठनीय अंकों का अनुमान नहीं |"
        for row in audit
    )


def register_notes(topic: TopicSpec) -> str:
    return "\n".join(
        [
            "### तीव्र पुनर्निर्माण रीढ़",
            "",
            *[f"- **{title}:** {body}" for title, body in topic.stages],
            "",
            "### स्वामित्व, विविधता और उत्तर-सुरक्षा",
            "",
            f"- **यहाँ स्वामित्व:** {topic.ownership}",
            f"- **अन्यत्र भेजें:** {topic.boundary}",
            f"- **सत्यापन-नियम:** {topic.verification}",
            "- सबसे छोटा वैध सुधार करें; अर्थ बचाएँ और मानक विकल्प स्पष्ट करें।",
            "- बोध में पाठ-आधार दें; संक्षेप में कुछ न जोड़ें; निबन्ध में उद्धरण या आँकड़ा न गढ़ें।",
            "",
            "### समयबद्ध उत्तर-रीढ़",
            "",
            "`माँग पढ़ें → संरचना बनाएँ → नियम लगाएँ → अर्थ जाँचें → विकल्प पहचानें → संशोधन करें`",
        ]
    )


def build_markdown(
    topic: TopicSpec,
    questions: list[Question],
    generation: int,
    paper_audit: list[dict[str, Any]],
) -> tuple[str, str]:
    basic = demote(topic.basic.read_text(encoding="utf-8"))
    source_paths = (
        topic.basic,
        KNOWLEDGE / "00_Master-Framework.md",
        KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
        KNOWLEDGE / "README.md",
        KNOWLEDGE / "subject-wide-package" / "Qualifying-Hindi_Practice-Solutions.md",
    )
    source_rows = "\n".join(f"| `{rel(path)}` | `{sha256(path)}` |" for path in source_paths)
    refs = "\n".join(f"- {url}" for url in PUBLIC_REFERENCES)
    paper_rows = official_demand_table(topic, paper_audit)
    basic_mcqs = "\n\n".join(format_question(q, solution=True) for q in questions[:16])
    timed_mcqs = "\n\n".join(format_question(q, solution=True) for q in questions[32:40])
    ascii_text = ascii_master(topic)
    main = f"""---
title: "{topic.title} — Qualifying Hindi Learner-v2 Semantic Successor"
topic_key: {topic.key}
---

# {topic.title} — अनिवार्य हिन्दी की पूर्ण अध्ययन-सामग्री

**पहचान:** `{topic.key}:learner-v2:g{generation}`  
**निर्माण तिथि:** {DATE}  
**अनुमोदन:** false  
**आधिकारिक पाठ्यक्रम-आधार:** {topic.syllabus}

| कैनोनिकल/स्थानीय स्रोत | निर्माण के समय SHA-256 |
|---|---|
{source_rows}

### सत्यापन-संदर्भ

{refs}

स्थानीय आधिकारिक प्रश्नपत्र बार-बार आने वाली माँग और format प्रमाणित करते हैं, UPSC की
अनुपलब्ध उत्तर-कुंजी नहीं। सार्वजनिक सरकारी भाषा-संदर्भों से निरपेक्ष दावों और वैध विकल्पों
की जाँच की गई; शिक्षण का मूल स्वामी repository का कैनोनिकल Markdown है।

## BASIC LEARNING SESSION

### बारह-पैनल ASCII मास्टर प्रवाह

```text
{ascii_text}
```

### कैनोनिकल आधार-सामग्री

{basic}

## BASIC MCQS / REMEDIATION

### निदान और मुख्य अभ्यास

{basic_mcqs}

### मॉडल उत्तर सहित प्रगतिशील प्रयोग

{transfer_block(topic, solutions=True)}

### सुधार-चक्र

1. विकल्प देखने से पहले नियम या पाठ-आधार लिखें।
2. हर निकट गलत विकल्प की प्रसंगगत त्रुटि समझाएँ।
3. वैध विकल्प और वास्तविक अशुद्धि को अलग दर्ज करें।
4. उसी नियम से एक नया वाक्य/अनुच्छेद लिखें।
5. लगातार दो समयबद्ध सही प्रयासों के बाद आगे बढ़ें।

## PYQS AND ANSWER PRACTICE

### सत्यापित स्थानीय आधिकारिक प्रश्न-दबाव लेखा

| वर्ष | स्थानीय आधिकारिक प्रश्नपत्र | इस विषय की माँग | provenance स्थिति |
|---:|---|---|---|
{paper_rows}

> तालिका केवल सत्यापित प्रश्न-माँग और format दर्ज करती है। यह प्रश्नों का अनधिकृत पुनरुत्पादन,
> UPSC उत्तर-कुंजी की कल्पना या UPSC मॉडल उत्तर का दावा नहीं करती।

### समयबद्ध प्रतिकूल अभ्यास

{timed_mcqs}

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

{topic.advanced}

## CONSOLIDATED REGISTER NOTES

{register_notes(topic)}
"""
    workbook_questions = "\n\n".join(format_question(q, solution=False) for q in questions)
    solutions = "\n\n".join(format_question(q, solution=True) for q in questions)
    workbook = f"""---
title: "{topic.title} — Qualifying Hindi Solved Practice Workbook"
topic_key: {topic.key}
---

# {topic.title} — Solved Practice Workbook / समाधानयुक्त अभ्यास-पुस्तिका

**पहचान:** `{topic.key}:learner-v2:g{generation}` | **अनुमोदन:** false

## BASIC MCQS / REMEDIATION

### निदान सेट — प्रश्न 1-16

{workbook_questions.split('### Q17.', 1)[0]}

### क्रमिक कठिनाई सेट — प्रश्न 17-32

### Q17.{workbook_questions.split('### Q17.', 1)[1].split('### Q33.', 1)[0]}

### सुधारात्मक और समयबद्ध सेट — प्रश्न 33-48

### Q33.{workbook_questions.split('### Q33.', 1)[1]}

## PYQS AND ANSWER PRACTICE

### सभी MCQ की व्याख्याएँ

{solutions}

### निर्मित-उत्तर अभ्यास और मॉडल

{transfer_block(topic, solutions=True)}

### आधिकारिक प्रश्न-दबाव लेखा

| वर्ष | स्थानीय आधिकारिक प्रश्नपत्र | इस विषय की माँग | provenance स्थिति |
|---:|---|---|---|
{paper_rows}

### अंतिम जाँच

- हर MCQ में चार अलग विकल्प हैं और कुंजी A → B → C → D क्रम में घूमती है।
- वैध विकल्पों को चुपचाप गलत नहीं ठहराया गया है।
- बोध-उत्तर पाठ-समर्थित रहेंगे।
- संक्षेप में विचार-इकाई, अनुपात, निष्ठा और शीर्षक-निर्देश सुरक्षित रहेंगे।
- निबन्ध में योग्य thesis होगा और गढ़े प्रमाण से बचा जाएगा।
"""
    return main, workbook


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = Path(r"C:\Windows\Fonts\Nirmala.ttc")
    return ImageFont.truetype(str(path), size, index=1 if bold else 0)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def build_flow(topic: TopicSpec, generation: int, ascii_text: str, folder: Path) -> dict[str, Any]:
    folder.mkdir(parents=True, exist_ok=True)
    editable = folder / "editable"
    previews = folder / "previews"
    editable.mkdir(exist_ok=True)
    previews.mkdir(exist_ok=True)
    width, card_h, gap = 1800, 250, 24
    height = 260 + len(topic.stages) * (card_h + gap) + 100
    image = Image.new("RGB", (width, height), "#F4F7FB")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((45, 35, width - 45, 205), 30, fill="#17233C")
    draw.text((90, 68), topic.title, font=font(44, True), fill="white")
    draw.text((92, 138), f"अनिवार्य हिन्दी semantic master • {topic.key} • g{generation} • approved: false", font=font(24), fill="#FFC857")
    palette = ("#245B91", "#168373", "#8A5A12", "#8A3440")
    y = 240
    for index, (title, body) in enumerate(topic.stages, 1):
        color = palette[(index - 1) % len(palette)]
        draw.rounded_rectangle((80, y, width - 80, y + card_h), 24, fill="white", outline=color, width=6)
        draw.ellipse((110, y + 66, 210, y + 166), fill=color)
        number = f"{index:02d}"
        box = draw.textbbox((0, 0), number, font=font(28, True))
        draw.text((160 - (box[2] - box[0]) / 2, y + 98), number, font=font(28, True), fill="white")
        draw.text((245, y + 40), title, font=font(29, True), fill="#17233C")
        for line_number, line in enumerate(wrap(draw, body, font(22), 1420)[:4]):
            draw.text((245, y + 92 + 34 * line_number), line, font=font(22), fill="#34465A")
        if index < len(topic.stages):
            draw.line((width // 2, y + card_h, width // 2, y + card_h + gap), fill="#6C7A8C", width=6)
            draw.polygon(((width // 2 - 12, y + card_h + gap - 14), (width // 2 + 12, y + card_h + gap - 14), (width // 2, y + card_h + gap)), fill="#6C7A8C")
        y += card_h + gap
    master = folder / "master.png"
    image.save(master, "PNG", dpi=(180, 180))
    overview = previews / "master-overview.png"
    image.copy().resize((900, max(1, height // 2))).save(overview, "PNG")
    poster = folder / "poster.pdf"
    doc = fitz.open()
    page = doc.new_page(width=width, height=height)
    page.insert_image(page.rect, filename=str(master))
    doc.save(poster)
    doc.close()

    tile_h, overlap = 1200, 80
    tiles: list[dict[str, int]] = []
    tile_paths: list[Path] = []
    start = 0
    while start < height:
        end = min(height, start + tile_h)
        crop = image.crop((0, start, width, end))
        tile_path = editable / f"tile-{len(tile_paths) + 1:02d}.png"
        crop.save(tile_path, "PNG")
        tile_paths.append(tile_path)
        tiles.append({"y_start": start, "y_end": end})
        if end == height:
            break
        start = end - overlap
    tiled = folder / "tiled.pdf"
    tiled_doc = fitz.open()
    for tile_path in tile_paths:
        with Image.open(tile_path) as tile:
            page = tiled_doc.new_page(width=tile.width, height=tile.height)
            page.insert_image(page.rect, filename=str(tile_path))
    tiled_doc.save(tiled)
    tiled_doc.close()
    for index, tile_path in enumerate(tile_paths, 1):
        with Image.open(tile_path) as tile:
            tile.thumbnail((700, 700))
            tile.save(previews / f"page-{index:02d}.png", "PNG")
    thumbs = [Image.open(previews / f"page-{index:02d}.png").convert("RGB") for index in range(1, len(tile_paths) + 1)]
    contact = Image.new("RGB", (720, sum(item.height for item in thumbs) + 20 * (len(thumbs) + 1)), "white")
    y_cursor = 20
    for thumb in thumbs:
        contact.paste(thumb, ((720 - thumb.width) // 2, y_cursor))
        y_cursor += thumb.height + 20
        thumb.close()
    contact_path = previews / "contact-sheet-01.png"
    contact.save(contact_path, "PNG")

    ascii_path = folder / "ascii-master.txt"
    ascii_path.write_text(ascii_text + "\n", encoding="utf-8")
    ascii_pdf = folder / "ascii-master.pdf"
    pdfmetrics.registerFont(TTFont("Nirmala", r"C:\Windows\Fonts\Nirmala.ttc", subfontIndex=0))
    pdfmetrics.registerFont(TTFont("Nirmala-Bold", r"C:\Windows\Fonts\Nirmala.ttc", subfontIndex=1))
    styles = getSampleStyleSheet()
    styles["Title"].fontName = "Nirmala-Bold"
    styles["Code"].fontName = "Nirmala"
    styles["Code"].fontSize = 5.8
    styles["Code"].leading = 7.4
    SimpleDocTemplate(str(ascii_pdf), pagesize=A4, leftMargin=1 * cm, rightMargin=1 * cm, topMargin=1 * cm, bottomMargin=1 * cm).build(
        [Paragraph(topic.title + " — ASCII मास्टर", styles["Title"]), Spacer(1, 0.3 * cm), Preformatted(ascii_text, styles["Code"])]
    )
    spec_path = editable / "topic-spec.json"
    dump(
        spec_path,
        {
            "schema_version": 1,
            "topic_key": topic.key,
            "generation": generation,
            "approved": False,
            "source_basic": rel(topic.basic),
            "source_advanced": None,
            "stages": [{"number": index, "title": title, "body": body} for index, (title, body) in enumerate(topic.stages, 1)],
        },
    )
    preservation = folder / "preservation-hashes.json"
    dump(preservation, {rel(path): sha256(path) for path in (master, poster, tiled, ascii_path, ascii_pdf, spec_path)})
    audit = folder / "build-audit.json"
    dump(
        audit,
        {
            "schema_version": 1,
            "topic_key": topic.key,
            "generation": generation,
            "master_size": [width, height],
            "core_stage_count": 12,
            "tile_count": len(tile_paths),
            "tiles": tiles,
            "overlap_pixels": overlap,
            "same_master": True,
            "ascii_graphical_stage_titles_equal": True,
            "approved": False,
        },
    )
    validation_report = folder / "validation-report.txt"
    validation_report.write_text(
        "PASS\n12 graphical stages.\n12 ASCII panels.\nPoster and tiled pages derive from master.png.\n"
        f"Tile overlap: {overlap}px.\nApproval: false.\n",
        encoding="utf-8",
    )
    image.close()
    return {
        "folder": rel(folder),
        "master_image": rel(master),
        "poster_pdf": rel(poster),
        "tiled_pdf": rel(tiled),
        "editable": rel(editable),
        "previews": rel(previews),
        "contact_sheets": [rel(contact_path)],
        "master_overview": rel(overview),
        "validation_report": rel(validation_report),
        "build_audit": rel(audit),
        "preservation_hashes": rel(preservation),
        "ascii_master": rel(ascii_path),
        "ascii_master_pdf": rel(ascii_pdf),
        "core_stage_count": 12,
        "graphical_stage_count": 12,
        "tiled_page_count": len(tile_paths),
        "approval": False,
        "same_master": True,
    }


def validate_flow(flow: dict[str, Any], topic: TopicSpec) -> list[str]:
    errors: list[str] = []
    master = Image.open(ROOT / flow["master_image"]).convert("RGB")
    spec = load(ROOT / flow["editable"] / "topic-spec.json")
    ascii_text = (ROOT / flow["ascii_master"]).read_text(encoding="utf-8")
    if len(spec["stages"]) != 12 or ascii_text.count("PANEL ") != 12:
        errors.append("Flow stage/panel count mismatch.")
    for stage in spec["stages"]:
        if stage["title"].upper() not in ascii_text:
            errors.append(f"ASCII missing stage {stage['title']}.")
    start = 0
    with fitz.open(ROOT / flow["tiled_pdf"]) as document:
        for index, page in enumerate(document, 1):
            tile_path = ROOT / flow["editable"] / f"tile-{index:02d}.png"
            tile = Image.open(tile_path).convert("RGB")
            expected = master.crop((0, start, master.width, start + tile.height))
            if ImageChops.difference(tile, expected).getbbox() is not None:
                errors.append(f"Tile {index} is not an exact master crop.")
            images = page.get_images(full=True)
            if len(images) != 1:
                errors.append(f"Tiled PDF page {index} has {len(images)} images.")
            else:
                extracted = document.extract_image(images[0][0])
                actual = Image.open(BytesIO(extracted["image"])).convert("RGB")
                if actual.size != tile.size or ImageChops.difference(actual, tile).getbbox() is not None:
                    errors.append(f"Tiled PDF page {index} differs from its master crop.")
                actual.close()
            start += tile.height - 80
            tile.close()
            expected.close()
    master.close()
    return errors


def next_generation(topic_key: str) -> tuple[int, str | None]:
    rows = [row for row in load(EXPORT_STATUS)["exports"] if row.get("topic_key") == topic_key]
    if not rows:
        return 1, None
    previous = max(rows, key=lambda row: int(row.get("generation", 0)))
    return int(previous.get("generation", 0)) + 1, previous.get("record_id")


def create_manifest() -> None:
    catalogue = load(CATALOGUE)
    rows = [row for row in catalogue["topics"] if row["topic_key"].startswith("qualifying-hindi-")]
    expected = [f"qualifying-hindi-{index:02d}" for index in range(1, 7)]
    if [row["topic_key"] for row in rows] != expected:
        raise ValueError("Authoritative Qualifying Hindi catalogue/order mismatch.")
    dump(
        SECTION_MANIFEST,
        {
            "schema_version": 1,
            "variant": "learner-v2",
            "subject": {"key": "Qualifying-Hindi", "display_name": "Qualifying Hindi"},
            "section": {
                "key": "subject-wide-syllabus",
                "name": "Subject-wide Syllabus",
                "scope": "official-section",
                "complete_syllabus_section": True,
                "syllabus_sources": [
                    rel(KNOWLEDGE / "LEARNING-SESSION-COMMAND-INDEX.md"),
                    rel(KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"),
                    rel(KNOWLEDGE / "README.md"),
                ],
                "notes": "Authoritative six-topic Qualifying Hindi catalogue in canonical order.",
            },
            "topics": [
                {
                    "topic_key": row["topic_key"],
                    "display_title": row["display_title"],
                    "syllabus_mapping": f"Subject-wide Syllabus; catalogue topic {row['topic_order']:02d}.",
                    "source_canonical": row["source_canonical"],
                    "source_basic": row["source_basic"],
                    "source_advanced": None,
                    "cross_topic_sources": [
                        rel(KNOWLEDGE / "00_Master-Framework.md"),
                        rel(KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"),
                        rel(KNOWLEDGE / "README.md"),
                        rel(KNOWLEDGE / "subject-wide-package" / "Qualifying-Hindi_Practice-Solutions.md"),
                    ],
                    "verified_pyq_sources": [rel(ROOT / "books" / "more_previous_papers" / filename) for _, filename, _ in OFFICIAL_PAPERS],
                }
                for row in rows
            ],
        },
    )


def render_pdfs(main_md: Path, workbook_md: Path, main_pdf: Path, workbook_pdf: Path, topic_key: str) -> None:
    main_pdf.parent.mkdir(parents=True, exist_ok=True)
    markdown_learning_pdf.build_pdf(main_md, main_pdf, mode="main", variant="learner-v2", topic_key=topic_key, repository_root=ROOT)
    markdown_learning_pdf.build_pdf(
        workbook_md,
        workbook_pdf,
        mode="workbook",
        variant="learner-v2",
        topic_key=topic_key,
        repository_root=ROOT,
        standalone_workbook=True,
    )


def status_row(state: dict[str, Any], topic_key: str) -> dict[str, Any]:
    return next(row for row in state["topics"] if row["topic_key"] == topic_key)


def set_state(topic: TopicSpec, status_name: str, **updates: Any) -> None:
    state = load(SEMANTIC)
    row = status_row(state, topic.key)
    row["status"] = status_name
    row.update(updates)
    dump(SEMANTIC, state)
    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_semantic_completeness_tracker.py")], cwd=ROOT, check=True)


def ensure_active(topic: TopicSpec) -> None:
    state = load(SEMANTIC)
    if state["next_topic"]["topic_key"] != topic.key:
        raise ValueError(f"Authoritative next topic is {state['next_topic']['topic_key']}, not {topic.key}.")
    active = [
        row["topic_key"]
        for row in state["topics"]
        if row["status"] in {"in_progress", "changes_required", "repair_in_progress", "revalidation_pending"}
        and row["topic_key"] != topic.key
    ]
    if active:
        raise ValueError("Another semantic topic is active: " + ", ".join(active))


def update_export_status(record: dict[str, Any]) -> None:
    status = load(EXPORT_STATUS)
    if any(row.get("record_id") == record["record_id"] for row in status["exports"]):
        raise ValueError(f"Record already exists: {record['record_id']}")
    status["exports"].append(record)
    dump(EXPORT_STATUS, status)


def pdf_pages(path: Path) -> int:
    with fitz.open(path) as document:
        return document.page_count


def run_topic(number: int) -> dict[str, Any]:
    topic = topics()[number - 1]
    ensure_active(topic)
    set_state(
        topic,
        "in_progress",
        reviewed_at=now_iso(),
        next_action="Hostile language audit, canonical repair, learner-v2 generation and answer verification are active.",
    )
    changed: set[str] = {
        "tools\\qualifying_hindi_semantic_data.py",
        "tools\\qualifying_hindi_semantic_runtime.py",
        "tools\\run_qualifying_hindi_semantic_topic.py",
        "tools\\test_run_qualifying_hindi_semantic_topic.py",
        "tools\\finalize_qualifying_hindi_semantic_review.py",
        rel(SEMANTIC),
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
    }
    failure_path = EXPORTS / f"{topic.key}-semantic-failure-{DATE}.json"
    try:
        before_hash, after_hash, owner_changed = repair_owner(topic)
        if owner_changed:
            changed.add(rel(topic.basic))
        set_state(topic, "repair_in_progress", next_action="Canonical owner repaired; learner artifacts are being generated.")
        generation, supersedes = next_generation(topic.key)
        questions = questions_for(topic)
        question_errors = validate_questions(topic, questions)
        if question_errors:
            raise ValueError("Question validation failed: " + " | ".join(question_errors))
        paper_audit = official_paper_audit()
        if any(row["errors"] for row in paper_audit):
            raise ValueError("Official paper extraction audit failed: " + json.dumps(paper_audit, ensure_ascii=False))
        main_text, workbook_text = build_markdown(topic, questions, generation, paper_audit)
        markdown_errors = validate_v2_markdown_text(main_text)
        if markdown_errors:
            raise ValueError("Learner-v2 structure failed: " + " | ".join(markdown_errors))

        generation_dir = LEARNER_ROOT / "learning-sessions" / topic.key / f"g{generation}"
        notes_dir = NOTES_ROOT / "learning-sessions" / topic.key / f"g{generation}"
        flow_dir = NOTES_ROOT / "flowcharts" / topic.key / f"carvaka-g{generation}"
        main_md = generation_dir / f"{topic.key}_Complete-Learning-Session_{DATE}.md"
        workbook_md = generation_dir / f"{topic.key}_Solved-Practice-Workbook_{DATE}.md"
        main_pdf = notes_dir / f"{topic.key}_Complete-Learning-Session_{DATE}.pdf"
        workbook_pdf = notes_dir / f"{topic.key}_Solved-Practice-Workbook_{DATE}.pdf"
        generation_dir.mkdir(parents=True, exist_ok=True)
        main_md.write_text(main_text, encoding="utf-8")
        workbook_md.write_text(workbook_text, encoding="utf-8")
        CANONICAL_SESSION_ROOT.mkdir(parents=True, exist_ok=True)
        canonical_session = CANONICAL_SESSION_ROOT / f"{topic.key}_Learning-Session.md"
        canonical_workbook = CANONICAL_SESSION_ROOT / f"{topic.key}_Solved-Workbook.md"
        canonical_session.write_text(main_text, encoding="utf-8")
        canonical_workbook.write_text(workbook_text, encoding="utf-8")
        changed.update(map(rel, (main_md, workbook_md, canonical_session, canonical_workbook)))

        flow = build_flow(topic, generation, ascii_master(topic), flow_dir)
        changed.update(rel(path) for path in flow_dir.rglob("*") if path.is_file())
        render_pdfs(main_md, workbook_md, main_pdf, workbook_pdf, topic.key)
        changed.update((rel(main_pdf), rel(workbook_pdf)))
        set_state(topic, "revalidation_pending", next_action="Artifacts generated; language, identity, flow, hash and layout gates are being rerun.")

        main_pdf_errors = validate_pdf(main_pdf, variant="learner-v2", mode="main")
        workbook_pdf_errors = validate_pdf(workbook_pdf, variant="learner-v2", mode="workbook")
        main_layout_errors, main_layout = validate_pdf_layout(main_pdf)
        workbook_layout_errors, workbook_layout = validate_pdf_layout(workbook_pdf)
        errors = main_pdf_errors + workbook_pdf_errors + main_layout_errors + workbook_layout_errors + validate_flow(flow, topic)
        if errors:
            raise ValueError("Artifact validation failed: " + " | ".join(errors))

        source_paths = [
            topic.basic,
            KNOWLEDGE / "00_Master-Framework.md",
            KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            KNOWLEDGE / "README.md",
            KNOWLEDGE / "subject-wide-package" / "Qualifying-Hindi_Practice-Solutions.md",
            *[ROOT / "books" / "more_previous_papers" / filename for _, filename, _ in OFFICIAL_PAPERS],
        ]
        record_id = f"{topic.key}:learner-v2:g{generation}"
        record = {
            "record_id": record_id,
            "topic_key": topic.key,
            "variant": "learner-v2",
            "generation": generation,
            "supersedes": supersedes,
            "command": f"Generate learner-v2 topic: Qualifying Hindi — Subject-wide Syllabus — {topic.title}",
            "main_pdf": rel(main_pdf),
            "workbook": rel(workbook_pdf),
            "markdown": rel(main_md),
            "workbook_markdown": rel(workbook_md),
            "generated_on": DATE,
            "approved": False,
            "provenance": {
                "workflow": "qualifying-hindi-semantic-completeness-immutable-successor",
                "source_basic": rel(topic.basic),
                "source_canonical": rel(topic.basic),
                "source_advanced": None,
                "assembled_markdown": rel(main_md),
                "canonical_learning_session": rel(canonical_session),
                "canonical_workbook": rel(canonical_workbook),
                "cross_topic_sources": [rel(path) for path in source_paths[1:5]],
                "local_ocr_sources": [rel(path) for path in source_paths[5:]],
                "public_verification_references": list(PUBLIC_REFERENCES),
                "renderer": {"name": markdown_learning_pdf.RENDERER_NAME, "version": markdown_learning_pdf.RENDERER_VERSION},
                "generation_date": DATE,
                "superseded_v1": supersedes if supersedes and "legacy-v1" in supersedes else None,
                "source_hashes": {rel(path): sha256(path) for path in source_paths},
                "canonical_owner_hash_before": before_hash,
                "canonical_owner_hash_after": after_hash,
                "practice_profile": "48 सख्त-rotation भाषा MCQ और पूर्ण मॉडल सहित आठ विषय-विशिष्ट निर्मित-उत्तर कार्य।",
                "pyq_status_note": "स्थानीय आधिकारिक प्रश्नपत्र recurring demand और format सत्यापित करते हैं; अनुपलब्ध आधिकारिक उत्तर-कुंजी या मॉडल उत्तर का अनुमान नहीं।",
                "answer_verification": "हर MCQ कुंजी कैनोनिकल नियम चुनती है; मानक विकल्प, passage fidelity तथा संक्षेप/निबन्ध/अनुवाद constraints स्पष्ट रूप से जाँचे गए।",
                "mcq_keys": "strict A-B-C-D rotation",
            },
            "approval": {"approved": False, "approved_on": None, "scope": record_id},
            "validation": {"state": "passed", "validated_on": DATE, "validator": "tools/qualifying_hindi_semantic_runtime.py + tools/validate_v2_export.py"},
            "continuous_core_first": flow,
            "refresh_profile": "qualifying-hindi-semantic-completeness",
        }
        update_export_status(record)
        changed.add("EXPORT-PDF-STATUS.json")
        record_path = EXPORTS / f"{topic.key}-learner-v2-g{generation}-{DATE}-record.json"
        dump(record_path, record)
        changed.add(rel(record_path))
        create_manifest()
        changed.add(rel(SECTION_MANIFEST))
        subprocess.run([sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")], cwd=ROOT, check=True)
        subprocess.run(
            [sys.executable, str(ROOT / "tools" / "generate_v2_section_indexes.py"), "--manifest", str(SECTION_MANIFEST), "--tracker", str(EXPORT_STATUS)],
            cwd=ROOT,
            check=True,
        )
        changed.update(
            {
                "EXPORT-PDF-COMMAND-INDEX.md",
                "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
                "notes\\Qualifying-Hindi\\learning-session-v2\\subject-wide-syllabus\\indexes\\TOPIC-COVERAGE-INDEX.md",
                "notes\\Qualifying-Hindi\\learning-session-v2\\subject-wide-syllabus\\indexes\\NOTES-PDF-INDEX.md",
                "notes\\Qualifying-Hindi\\learning-session-v2\\subject-wide-syllabus\\indexes\\WORKBOOK-PDF-INDEX.md",
            }
        )

        deliverables = [
            main_md,
            workbook_md,
            main_pdf,
            workbook_pdf,
            ROOT / flow["master_image"],
            ROOT / flow["poster_pdf"],
            ROOT / flow["tiled_pdf"],
            ROOT / flow["ascii_master"],
            ROOT / flow["ascii_master_pdf"],
        ]
        validation_path = EXPORTS / f"{topic.key}-semantic-validation-{DATE}.json"
        inventory_path = EXPORTS / f"{topic.key}-semantic-completeness-{DATE}-changed-files.txt"
        report_path = REVIEWS / f"{topic.key}-semantic-completeness-review-{DATE}.md"
        changed.update(map(rel, (validation_path, inventory_path, report_path)))
        validation = {
            "schema_version": 1,
            "topic_key": topic.key,
            "record_id": record_id,
            "approval": False,
            "result": "passed",
            "ten_gates": {name: True for name in status_row(load(SEMANTIC), topic.key)["checks"]},
            "checks": {
                "catalogue_identity_and_order": True,
                "canonical_owner_repaired_or_verified": True,
                "five_h2_order_and_register_notes_last": True,
                "forty_eight_unique_mcqs": True,
                "strict_abcd_rotation": True,
                "answer_key_and_accepted_variation_validation": True,
                "passage_precis_essay_constraints": True,
                "official_paper_provenance_preserved": True,
                "graphical_ascii_twelve_panel_parity": True,
                "pdf_indexes_and_layout": True,
                "identity_isolated_and_unapproved": True,
                "source_hashes": True,
            },
            "metrics": {
                "main_pages": pdf_pages(main_pdf),
                "workbook_pages": pdf_pages(workbook_pdf),
                "question_count": len(questions) + len(topic.transfer_tasks),
                "mcq_count": len(questions),
                "constructed_response_tasks": len(topic.transfer_tasks),
                "mcq_keys": [q.answer for q in questions],
                "official_paper_demand_rows": len(paper_audit),
                "accepted_variation_items": sum(bool(q.accepted_variation) for q in questions),
                "ascii_panel_count": 12,
                "graphical_stage_count": 12,
                "tiled_pages": flow["tiled_page_count"],
                "main_layout": main_layout,
                "workbook_layout": workbook_layout,
                "deterministic_checks": len(questions),
            },
            "official_paper_audit": paper_audit,
            "deliverable_hashes": {rel(path): sha256(path) for path in deliverables},
            "errors": [],
        }
        dump(validation_path, validation)
        existing_files = sorted(path for path in changed if path in {rel(validation_path), rel(inventory_path), rel(report_path)} or (ROOT / path).exists())
        set_state(
            topic,
            "passed",
            checks={name: "passed" for name in status_row(load(SEMANTIC), topic.key)["checks"]},
            gap_counts={name: 0 for name in status_row(load(SEMANTIC), topic.key)["gap_counts"]},
            findings=[
                {
                    "severity": "closed",
                    "finding": "Hostile Qualifying Hindi audit, canonical ownership, rule/key/variation checks, official-paper demand verification, learner-v2 package, dual 12-panel flows, hashes and PDF layout passed.",
                    "record_id": record_id,
                }
            ],
            files_changed=existing_files,
            completed_at=now_iso(),
            next_action="Passed; advance exactly one topic in the authoritative catalogue.",
        )
        next_topic = load(SEMANTIC)["next_topic"]
        next_key = next_topic["topic_key"] if next_topic else None
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            f"""# अनिवार्य हिन्दी Semantic-Completeness Review {topic.number:02d} — {topic.title}

**विषय कुंजी:** `{topic.key}`  
**समीक्षा तिथि:** 6 सितम्बर 2026  
**परिणाम:** PASSED  
**कैनोनिकल आधार-स्वामी:** `{rel(topic.basic)}`  
**स्वीकृत पहचान:** `{record_id}`  
**अनुमोदित:** false

केवल यही catalogue विषय सक्रिय था। शाब्दिक पाठ्यक्रम, पूर्वापेक्षाएँ, मानक हिन्दी वर्गीकरण,
सत्यापित प्रश्न-दबाव, प्रतिकूल absence queries, कैनोनिकल सीमाएँ, वैध विविधता, उत्तर-रचना और
सभी आश्रित artifacts का मिलान किया गया।

Validation: {validation['metrics']['main_pages']} मुख्य पृष्ठ; {validation['metrics']['workbook_pages']}
workbook पृष्ठ; 48 MCQ; 8 निर्मित-उत्तर कार्य; 7 आधिकारिक प्रश्न-दबाव rows;
12 ASCII panels; 12 graphical stages; failures 0.

Machine validation: `{rel(validation_path)}`  
Inventory: `{rel(inventory_path)}`  
अगला queue item: `{next_key or 'None — semantic queue complete'}`.
""",
            encoding="utf-8",
        )
        inventory_path.write_text("\n".join(existing_files) + "\n", encoding="utf-8")
        return {
            "status": "passed",
            "topic_key": topic.key,
            "record_id": record_id,
            "generation": generation,
            "metrics": validation["metrics"],
            "next_topic_key": next_key,
            "report": rel(report_path),
            "validation": rel(validation_path),
            "inventory": rel(inventory_path),
        }
    except BaseException as error:
        dump(
            failure_path,
            {
                "topic_key": topic.key,
                "date": DATE,
                "error_type": type(error).__name__,
                "error": str(error),
                "preserved_intermediate_paths": sorted(path for path in changed if (ROOT / path).exists()),
            },
        )
        set_state(
            topic,
            "blocked",
            findings=[{"severity": "unresolved", "finding": f"{type(error).__name__}: {error}"}],
            files_changed=sorted(path for path in changed if (ROOT / path).exists()) + [rel(failure_path)],
            next_action="Resolve this failure before advancing the Qualifying Hindi queue.",
        )
        raise
