import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECTS = {
    "Social-Justice": 17,
    "Disaster-Management": 18,
    "Internal-Security": 12,
}

def count_questions(text):
    return len(re.findall(r"(?m)^(?:### Q\d+\b|## \d+\.)", text))

def check_bank(path):
    q = path / "QUESTIONS.md"
    a = path / "ANSWERS.md"
    c = path / "COVERAGE.md"
    errors = []
    if not q.exists() or not a.exists() or not c.exists():
        return ["missing QUESTIONS.md, ANSWERS.md or COVERAGE.md"]
    qt = q.read_text(encoding="utf-8", errors="replace")
    at = a.read_text(encoding="utf-8", errors="replace")
    n = count_questions(qt)
    if n < 40:
        errors.append(f"only {n} questions")
    blocks = re.split(r"(?m)^(?:### Q\d+\b|## \d+\.)", qt)[1:]
    for i, block in enumerate(blocks, 1):
        if len(re.findall(r"(?m)^[ABCD]\.\s", block)) != 4:
            errors.append(f"Q{i} does not have exactly four options")
    if re.search(r"(?im)^\s*(answer|key|rationale|source)\s*:", qt):
        errors.append("answer/source leakage in QUESTIONS.md")
    keyed = re.findall(
        r"(?m)^(?:\d+\.\s+\*\*[ABCD]\.|\*\*Q\d+\s+—\s+[ABCD]\.|"
        r"\|\s*\d+\s*\|\s*\*\*[ABCD]\*\*|##\s*\d+\.\s*[ABCD]\s+—)",
        at,
    )
    if len(keyed) < n:
        errors.append(f"only {len(keyed)} keyed answers for {n} questions")
    return errors

def main(subject):
    root = ROOT / "final-mcq" / "subjects" / subject
    expected = SUBJECTS[subject]
    topics = sorted((p for p in root.iterdir() if p.is_dir() and re.match(r"^\d{2}[-_]", p.name)), key=lambda p: p.name)
    errors = []
    if len(topics) != expected:
        errors.append(f"expected {expected} topic folders, found {len(topics)}")
    total = 0
    for topic in topics:
        for bank in (1, 2, 3):
            e = check_bank(topic / f"revision-{bank}")
            total += count_questions((topic / f"revision-{bank}" / "QUESTIONS.md").read_text(encoding="utf-8", errors="replace")) if (topic / f"revision-{bank}" / "QUESTIONS.md").exists() else 0
            errors.extend(f"{topic.name}/revision-{bank}: {x}" for x in e)
    if errors:
        print(f"{subject.upper()} PIPELINE: FAIL")
        print("\n".join(errors[:40]))
        return 1
    print(f"{subject.upper()} PIPELINE: PASS — {len(topics)} topics, {total} questions across three banks")
    return 0

if __name__ == "__main__":
    s = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).stem.replace("_pipeline", "").replace("_", "-").title()
    aliases = {"Social-Justice": "Social-Justice", "Disaster-Management": "Disaster-Management", "Internal-Security": "Internal-Security"}
    raise SystemExit(main(aliases.get(s, s)))
