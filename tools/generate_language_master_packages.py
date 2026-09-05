"""Build subject-wide Qualifying English and Hindi learning packages."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge"


CONFIGS = {
    "Qualifying-English": {
        "title": "UPSC Qualifying English",
        "guide_introduction": (
            "A subject-wide guide for the compulsory qualifying English paper. "
            "It covers the official English areas only: serious discursive-prose "
            "comprehension, precis writing, usage and vocabulary, and short essays."
        ),
        "guide_sources": [
            "README.md",
            "00_Master-Framework.md",
            "00_Readiness-Tracker.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "basic/01_Parts-of-Speech.md",
            "basic/02_Sentence-Grammar.md",
            "basic/03_Punctuation-and-Capitalisation.md",
            "basic/04_Vocabulary-Idioms-and-Proverbs.md",
            "basic/05_Error-Correction-and-Transformation.md",
            "basic/06_Comprehension-and-Precis.md",
            "basic/07_Short-Essay-Writing.md",
        ],
        "practice_sources": [
            "practice/01_Foundation-Test.md",
            "practice/02_Full-Length-Mock.md",
            "practice/03_Full-Length-Mock-2.md",
        ],
        "solution_sources": [
            "answer-keys/01_Foundation-Test-Key.md",
            "answer-keys/02_Full-Length-Mock-Key.md",
            "answer-keys/03_Full-Length-Mock-2-Key.md",
        ],
        "labels": (
            "Complete Skills Guide",
            "Question-Only Practice Workbook",
            "Practice Solutions",
        ),
    },
    "Qualifying-Hindi": {
        "title": "UPSC अनिवार्य हिन्दी",
        "guide_introduction": (
            "One continuous language-learning guide. It covers grammar, usage, "
            "vocabulary, comprehension, précis, essay writing, translation where "
            "applicable in both English↔Hindi directions, readiness and examination "
            "method. It contains no "
            "artificial GS learning-session sequence."
        ),
        "guide_sources": [
            "README.md",
            "00_Master-Framework.md",
            "00_Question-Demand-Ledger.md",
            "00_Readiness-Tracker.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "basic/01_शब्द-भेद.md",
            "basic/02_व्याकरण-वर्तनी-वाक्य-शुद्धि.md",
            "basic/03_शब्दावली-मुहावरे-लोकोक्तियाँ.md",
            "basic/04_बोध-और-संक्षेपण.md",
            "basic/05_निबन्ध-लेखन.md",
            "basic/06_अनुवाद.md",
        ],
        "practice_sources": [
            "practice/01_आधार-परीक्षण.md",
            "practice/02_पूर्ण-मॉक.md",
            "practice/03_पूर्ण-मॉक-2.md",
        ],
        "solution_sources": [
            "answer-keys/01_आधार-परीक्षण-उत्तर.md",
            "answer-keys/02_पूर्ण-मॉक-उत्तर.md",
            "answer-keys/03_पूर्ण-मॉक-2-उत्तर.md",
        ],
        "labels": (
            "सम्पूर्ण कौशल मार्गदर्शिका",
            "केवल-प्रश्न अभ्यास पुस्तिका",
            "अभ्यास समाधान",
        ),
    },
}


def strip_h1(text: str) -> str:
    return re.sub(r"\A# .+?\n+", "", text.strip(), count=1)


def combine(
    folder: Path,
    title: str,
    package_title: str,
    sources: list[str],
    introduction: str,
) -> str:
    blocks = []
    for number, source in enumerate(sources, 1):
        path = folder / source
        if not path.is_file():
            raise FileNotFoundError(path)
        source_text = path.read_text(encoding="utf-8")
        heading = next(
            (
                match.group(1).strip()
                for line in source_text.splitlines()
                if (match := re.match(r"^#\s+(.+?)\s*$", line))
            ),
            path.stem.replace("_", " "),
        )
        blocks.append(
            f"## PART {number:02d} — {heading}\n\n"
            f"{strip_h1(source_text)}"
        )
    navigation = (
        "## PACKAGE NAVIGATION\n\n"
        f"- **This document:** {package_title}\n"
        f"- **Companion Guide:** `{folder.name}_Complete-Skills-Guide.md`\n"
        f"- **Question-only Workbook:** `{folder.name}_Practice-Workbook.md`\n"
        f"- **Separate Solutions:** `{folder.name}_Practice-Solutions.md`\n"
        "- **Source map:** each numbered Part below names its authoritative "
        "source owner; practice-paper and solution Part numbers match one-to-one.\n"
        "- **Approval:** false until this exact generation is explicitly approved.\n"
    )
    return (
        f"# {title} — {package_title}\n\n"
        f"> {introduction}\n\n"
        f"{navigation}\n"
        + "\n\n".join(blocks)
        + "\n"
    )


def validate_preservation(
    assembled: str,
    folder: Path,
    sources: list[str],
) -> None:
    for source in sources:
        path = folder / source
        if strip_h1(path.read_text(encoding="utf-8")) not in assembled:
            raise ValueError(f"Source content was not preserved: {path}")


def build_subject(key: str, config: dict[str, object]) -> None:
    folder = KNOWLEDGE / key
    output = folder / "subject-wide-package"
    guide_label, workbook_label, solutions_label = config["labels"]
    guide = combine(
        folder,
        str(config["title"]),
        str(guide_label),
        list(config["guide_sources"]),
        str(config["guide_introduction"]),
    )
    workbook = combine(
        folder,
        str(config["title"]),
        str(workbook_label),
        list(config["practice_sources"]),
        (
            "Question-only diagnostic and full-length practice. Complete each "
            "paper before consulting the separate solutions document."
        ),
    )
    solutions = combine(
        folder,
        str(config["title"]),
        str(solutions_label),
        list(config["solution_sources"]),
        (
            "Matching keys, model responses and self-marking guidance for every "
            "paper in the practice workbook."
        ),
    )
    validate_preservation(guide, folder, list(config["guide_sources"]))
    validate_preservation(workbook, folder, list(config["practice_sources"]))
    validate_preservation(solutions, folder, list(config["solution_sources"]))
    if re.search(r"(?im)^### SESSION \d+", guide + workbook + solutions):
        raise ValueError(f"{key}: artificial learning sessions remain.")
    output.mkdir(parents=True, exist_ok=True)
    (output / f"{key}_Complete-Skills-Guide.md").write_text(
        guide, encoding="utf-8"
    )
    (output / f"{key}_Practice-Workbook.md").write_text(
        workbook, encoding="utf-8"
    )
    (output / f"{key}_Practice-Solutions.md").write_text(
        solutions, encoding="utf-8"
    )
    print(
        f"{key}: guide_sources={len(config['guide_sources'])}; "
        f"practice_papers={len(config['practice_sources'])}; "
        f"solution_keys={len(config['solution_sources'])}"
    )


def main() -> int:
    for key, config in CONFIGS.items():
        build_subject(key, config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
