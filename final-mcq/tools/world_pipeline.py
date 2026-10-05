from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
INDEX = ROOT / "final-mcq" / "subjects" / "World-History" / "INDEX.md"
SUBJECT = INDEX.parent


def rows():
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|", line)
        if m and m.group(1).isdigit():
            yield int(m.group(1)), m.group(2), m.group(3)


def next_pending():
    pending = [(n, title) for n, title, status in rows() if status.strip().strip("`").lower() == "pending"]
    return pending[0] if pending else None


def audit_topic():
    def folder_for(number):
        matches = sorted(SUBJECT.glob(f"{number:02d}-*"))
        return matches[0] if matches else None

    pending = next_pending()
    if pending:
        candidate = folder_for(pending[0])
        if candidate is not None:
            return candidate
    completed = [
        (n, folder_for(n))
        for n, title, status in rows()
        if "`complete`" in status.strip().lower()
    ]
    for _, folder in reversed(completed):
        if folder is not None:
            return folder
    return SUBJECT / "14-Second-World-War"


def structural_audit():
    findings = []
    topic = audit_topic()
    for bank in (1, 2, 3):
        folder = topic / f"revision-{bank}"
        qpath, apath, cpath = folder / "QUESTIONS.md", folder / "ANSWERS.md", folder / "COVERAGE.md"
        if not all(p.exists() for p in (qpath, apath, cpath)):
            findings.append(f"bank {bank}: missing required file")
            continue
        qtext, atext = qpath.read_text(encoding="utf-8"), apath.read_text(encoding="utf-8")
        qnums = [int(x) for x in re.findall(r"^### Q(\d+)\.", qtext, re.M)]
        anums = [int(x) for x in re.findall(r"^### Q(\d+)\.", atext, re.M)]
        if qnums != list(range(1, 41)):
            findings.append(f"bank {bank}: QUESTIONS numbering/count {len(qnums)}")
        if anums != list(range(1, 41)):
            findings.append(f"bank {bank}: ANSWERS numbering/count {len(anums)}")
        if re.search(r"\*\*Correct answer|\*\*Evidence:|\*\*Examiner trap|Correct-option rationale", qtext, re.I):
            findings.append(f"bank {bank}: answer leakage in QUESTIONS.md")
        for q in range(1, 41):
            block = re.search(rf"^### Q{q}\..*?(?=^### Q{q+1}\.|\Z)", atext, re.M | re.S)
            if not block:
                findings.append(f"bank {bank}: missing answer block Q{q}")
                continue
            b = block.group(0)
            if len(re.findall(r"\*\*Option [A-D] — incorrect:", b)) != 3:
                findings.append(f"bank {bank}: Q{q} does not have three incorrect-option rationales")
            if not re.search(r"\*\*Correct-option rationale \([A-D]\):", b):
                findings.append(f"bank {bank}: Q{q} missing correct-option rationale")
            if not re.search(r"\*\*Evidence:\*\*", b) or not re.search(r"\*\*Examiner trap:\*\*", b):
                findings.append(f"bank {bank}: Q{q} missing evidence/trap")
    qstems = {}
    for bank in (1, 2, 3):
        qpath = topic / f"revision-{bank}" / "QUESTIONS.md"
        if qpath.exists():
            stems = re.findall(r"^### Q\d+\. (.*)$", qpath.read_text(encoding="utf-8"), re.M)
            for stem in stems:
                qstems.setdefault(stem, []).append(bank)
    duplicates = [s for s, bs in qstems.items() if len(set(bs)) > 1]
    if duplicates:
        findings.append(f"cross-bank duplicate stems: {len(duplicates)}")
    return findings


def main():
    nxt = next_pending()
    if nxt:
        title = re.sub(r"\[.*?\]\([^)]*\)", "", nxt[1]).strip()
        print(f"NEXT: Topic {nxt[0]:02d} - {title}")
    else:
        print("NEXT: none — all catalogue rows explicitly marked pending are complete")
    findings = structural_audit()
    if findings:
        print("STRUCTURAL FINDINGS:")
        print("\n".join(f"- {x}" for x in findings))
        raise SystemExit(1)
    print(f"STRUCTURAL: PASS ({audit_topic().name} banks present and clean)")


if __name__ == "__main__":
    main()
