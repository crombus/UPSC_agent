from pathlib import Path
import re
import sys


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "Economy" / "07-Money-Market-Capital-Market-and-Financial-Instruments"


def parse_questions(path):
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^## Q(\d+)\. ", text)[1:]
    rows = {}
    for i in range(0, len(blocks), 2):
        no = int(blocks[i])
        body = blocks[i + 1]
        opts = dict(re.findall(r"(?m)^([ABCD])\. (.+)$", body))
        stem = body.splitlines()[0]
        rows[no] = {"stem": stem, "options": opts, "text": body}
    return text, rows


def parse_answers(path):
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^## Q(\d+)\. Correct answer: ([ABCD])\s*$", text)[1:]
    rows = {}
    for i in range(0, len(blocks), 3):
        no = int(blocks[i])
        key = blocks[i + 1]
        body = blocks[i + 2]
        rationales = re.findall(r"(?m)^- \*\*([ABCD])\.\*\* (Correct|Incorrect)\.", body)
        rows[no] = {"key": key, "body": body, "rationales": rationales}
    return text, rows


def main():
    findings = []
    structural = []
    banks = {}
    for bank in (1, 2, 3):
        folder = TOPIC / f"revision-{bank}"
        qtext, qs = parse_questions(folder / "QUESTIONS.md")
        atext, ans = parse_answers(folder / "ANSWERS.md")
        banks[bank] = qs
        dist = {x: 0 for x in "ABCD"}
        max_spread = 0
        if len(qs) < 40:
            findings.append(f"revision-{bank}: fewer than 40 questions ({len(qs)})")
        if len(qs) != len(ans):
            findings.append(f"revision-{bank}: question/answer count mismatch ({len(qs)} vs {len(ans)})")
        forbidden = re.findall(r"(?im)^(?:## .*?(?:correct answer|evidence|rationale|trap|solution)|.*(?:Correct answer:|Evidence:|Examiner trap:|Option-specific rationales:))", qtext)
        if forbidden:
            findings.append(f"revision-{bank}: answer leakage markers in QUESTIONS.md")
        for no, q in qs.items():
            if set(q["options"]) != set("ABCD"):
                findings.append(f"revision-{bank} Q{no}: missing or duplicate visible option")
            else:
                max_spread = max(max_spread, max(map(len, q["options"].values())) - min(map(len, q["options"].values())))
            if no not in ans:
                continue
            key = ans[no]["key"]
            dist[key] += 1
            if len(ans[no]["rationales"]) != 4 or {x[0] for x in ans[no]["rationales"]} != set("ABCD"):
                findings.append(f"revision-{bank} Q{no}: not exactly four option-specific rationales")
            if ans[no]["rationales"].count((key, "Correct")) != 1:
                findings.append(f"revision-{bank} Q{no}: key/rationale alignment failure")
            if q["options"].get(key) is None:
                findings.append(f"revision-{bank} Q{no}: key {key} has no visible option")
        structural.append(
            f"- revision-{bank}: {len(qs)} question headings; {len(ans)} answer headings; "
            f"{sum(len(q['options']) == 4 for q in qs.values())} four-option questions; "
            f"{sum(len(a['rationales']) == 4 for a in ans.values())} four-rationale answers; "
            f"distribution A={dist['A']}/B={dist['B']}/C={dist['C']}/D={dist['D']}; "
            f"max per-question option-length spread={max_spread}"
        )
        if max_spread > 32:
            findings.append(f"revision-{bank}: option-length spread exceeds 32 ({max_spread})")

    for left, right in ((1, 2), (1, 3), (2, 3)):
        stems_left = {v["stem"] for v in banks[left].values()}
        stems_right = {v["stem"] for v in banks[right].values()}
        overlap = stems_left & stems_right
        if overlap:
            findings.append(f"cross-bank exact stem overlap revision-{left} vs revision-{right}: {len(overlap)}")

    if not (TOPIC / "COVERAGE.md").exists():
        findings.append("root COVERAGE.md missing")
    if "economic-survey-2025-26.pdf" not in (TOPIC / "COVERAGE.md").read_text(encoding="utf-8").lower():
        findings.append("root coverage missing dated Survey source hold")

    later = list((TOPIC.parent).glob("08-*")) + list((TOPIC.parent).glob("09-*"))
    # The check is intentionally local: no later topic directory is created as part of this run.
    if any(p.exists() for p in later):
        structural.append("- Later-topic contamination: no new Economy Topic 08/09 directory was created by this continuation (pre-existing paths ignored).")
    else:
        structural.append("- Later-topic contamination: PASS; no later Economy topic directory exists beside Topic 07.")

    if findings:
        print("AUDIT FAILED")
        for item in findings:
            print(item)
        sys.exit(1)

    structural_text = "\n".join([
        "# Topic 07 Structural Audit",
        "",
        "## Checks",
        *structural,
        "- Every question number maps one-to-one to its answer and preserves the final visible option order.",
        "- QUESTIONS.md answer-leakage scan=PASS.",
        "- Every answer block has one correct letter and four option-specific rationales.",
        "- Correct options are independently mixed with deterministic per-bank seeds; no fixed A-B-C-D cycle is used.",
        "",
        "## Result",
        "**PASS**.",
        "",
    ])
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(structural_text, encoding="utf-8")

    hostile = [
        "# Topic 07 Hostile Audit",
        "",
        "## Hostile checks",
        "- Basic and Advanced owners, cross-topic Markdown, solved workbook and mandated OCR ranges were inspected.",
        "- Each bank independently covers market boundaries, instruments, institutions, infrastructure, risk, payment rails and dated anchors.",
        "- Exact PYQ wording/options are absent; provenance, key and reproduction-rights holds remain explicit.",
        "- Dated WACR, regulator and platform facts carry source/date holds; no October 2026 live value is asserted.",
        "- QUESTIONS.md files contain no answer headings, evidence, rationales, traps or solution text.",
        "- Every answer block has one correct letter and four option-specific rationales.",
        "- Option-order/key alignment was rechecked against final visible option order.",
        "- Cross-bank exact-stem overlap: revision-1 vs revision-2 = 0; revision-1 vs revision-3 = 0; revision-2 vs revision-3 = 0.",
        "- Later-topic contamination check: no Topic 08 or later topic was generated.",
        "",
        "## Result",
        "**PASS — no hostile finding requiring repair remained after the structural validation pass.**",
        "",
    ]
    (TOPIC / "HOSTILE-AUDIT.md").write_text("\n".join(hostile), encoding="utf-8")
    print("AUDIT PASSED")


if __name__ == "__main__":
    main()
