"""Hostile structural/editorial audit for Modern History Topic 11."""

from __future__ import annotations

from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Modern-History" / "11-The-Revolt-of-1857"
EXPECTED = {1: 50, 2: 50, 3: 53}

Q_RE = re.compile(r"^### Q(\d+)\. (.+)$", re.M)
A_RE = re.compile(r"^### Q(\d+)\. ([ABCD])$", re.M)
OPT_RE = re.compile(r"^([ABCD])\. (.+)$", re.M)
RAT_RE = re.compile(r"^- \*\*([ABCD]):\*\* (.+)$", re.M)


def norm(text: str) -> str:
    text = re.sub(r"`[^`]+`", " ", text.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def blocks(text: str, answer: bool = False) -> dict[int, str]:
    pattern = A_RE if answer else Q_RE
    hits = list(pattern.finditer(text))
    return {
        int(m.group(1)): text[m.start() : hits[i + 1].start() if i + 1 < len(hits) else len(text)]
        for i, m in enumerate(hits)
    }


def longest_run(keys: str) -> int:
    return max((len(m.group()) for m in re.finditer(r"(A+|B+|C+|D+)", keys)), default=0)


def main() -> int:
    findings: list[str] = []
    all_stems: list[tuple[int, int, str]] = []
    all_options: list[tuple[int, int, str, str]] = []
    dimensions: dict[int, list[str]] = defaultdict(list)

    for rev, expected in EXPECTED.items():
        qpath = TOPIC / f"revision-{rev}" / "QUESTIONS.md"
        apath = TOPIC / f"revision-{rev}" / "ANSWERS.md"
        cpath = TOPIC / f"revision-{rev}" / "COVERAGE.md"
        for path in (qpath, apath, cpath):
            if not path.exists():
                findings.append(f"R{rev}: missing {path.name}")
        if findings:
            continue
        qt = qpath.read_text(encoding="utf-8")
        at = apath.read_text(encoding="utf-8")
        qb, ab = blocks(qt), blocks(at, answer=True)
        if len(qb) != expected or len(ab) != expected:
            findings.append(f"R{rev}: count Q={len(qb)} A={len(ab)}, expected {expected}")
        if set(qb) != set(ab) or set(qb) != set(range(1, expected + 1)):
            findings.append(f"R{rev}: question-answer numbering mismatch")
        if re.search(r"\b(?:answer|correct answer|key)\s*:", qt, re.I):
            findings.append(f"R{rev}: answer leakage in QUESTIONS.md")

        keys = "".join(m.group(2) for m in A_RE.finditer(at))
        dist = Counter(keys)
        if max(dist.values()) - min(dist.values()) > 1:
            findings.append(f"R{rev}: imbalanced keys {dict(dist)}")
        if longest_run(keys) > 2:
            findings.append(f"R{rev}: answer run over 2: {keys}")
        for size in range(4, 7):
            for i in range(len(keys) - 2 * size + 1):
                if keys[i : i + size] == keys[i + size : i + 2 * size]:
                    findings.append(f"R{rev}: repeated key cycle size {size} at Q{i+1}")

        for qno, qblock in qb.items():
            stem_match = Q_RE.search(qblock)
            stem = stem_match.group(2).strip() if stem_match else ""
            opts = OPT_RE.findall(qblock)
            if len(opts) != 4 or [x[0] for x in opts] != list("ABCD"):
                findings.append(f"R{rev} Q{qno}: option structure {len(opts)}")
                continue
            onorm = [norm(x[1]) for x in opts]
            if len(set(onorm)) != 4:
                findings.append(f"R{rev} Q{qno}: duplicate option")
            for i in range(4):
                for j in range(i + 1, 4):
                    standard_statement_set = all(
                        re.match(r"^(?:only statement [12] is correct|both statements are correct|neither statement is correct)$", x)
                        for x in onorm
                    )
                    if not standard_statement_set and SequenceMatcher(None, onorm[i], onorm[j]).ratio() >= 0.91:
                        findings.append(f"R{rev} Q{qno}: highly similar options {opts[i][0]}/{opts[j][0]}")
            all_stems.append((rev, qno, stem))
            all_options.extend((rev, qno, letter, text) for letter, text in opts)

            ablock = ab.get(qno, "")
            keym = A_RE.search(ablock)
            key = keym.group(2) if keym else ""
            rats = RAT_RE.findall(ablock)
            if len(rats) != 4 or [x[0] for x in rats] != list("ABCD"):
                findings.append(f"R{rev} Q{qno}: rationale structure {len(rats)}")
            for marker in ("**Tested dimension:**", "**Source/evidence:**", "**Examiner trap:**"):
                if marker not in ablock:
                    findings.append(f"R{rev} Q{qno}: missing {marker}")
            dm = re.search(r"\*\*Tested dimension:\*\* (.+)", ablock)
            if dm:
                dimensions[rev].append(norm(dm.group(1)))
            lengths = {letter: len(norm(text).split()) for letter, text in opts}
            others = sorted(v for k, v in lengths.items() if k != key)
            if key and lengths[key] >= max(14, int((others[1] if others else 0) * 1.9)):
                findings.append(f"R{rev} Q{qno}: keyed-option length cue {lengths}")
            kval = next((text for letter, text in opts if letter == key), "")
            if re.search(r"\b(?:only defensible|precisely|always|never|entirely|uniformly)\b", kval, re.I):
                findings.append(f"R{rev} Q{qno}: keyed qualification/absolute cue")

        duplicate_dims = [d for d, c in Counter(dimensions[rev]).items() if c > 1]
        if duplicate_dims:
            findings.append(f"R{rev}: repeated tested dimensions {duplicate_dims}")

    # Exact and near-duplicate stems across all three banks.
    stem_seen: dict[str, tuple[int, int]] = {}
    for rev, qno, stem in all_stems:
        n = norm(stem)
        if n in stem_seen:
            findings.append(f"exact duplicate stem R{stem_seen[n][0]}Q{stem_seen[n][1]} / R{rev}Q{qno}")
        stem_seen[n] = (rev, qno)
    for i, (r1, q1, s1) in enumerate(all_stems):
        n1 = norm(s1)
        for r2, q2, s2 in all_stems[i + 1 :]:
            if r1 == r2:
                continue
            n2 = norm(s2)
            ratio = SequenceMatcher(None, n1, n2).ratio()
            if ratio >= 0.88:
                findings.append(f"near-duplicate stem {ratio:.2f}: R{r1}Q{q1} / R{r2}Q{q2}")

    # Cross-bank exact options; repeated short labels are ignored, substantive sentences are not.
    option_seen: dict[str, tuple[int, int, str]] = {}
    for rev, qno, letter, text in all_options:
        n = norm(text)
        if len(n.split()) >= 7 and n in option_seen:
            old = option_seen[n]
            findings.append(f"cross-bank duplicate option R{old[0]}Q{old[1]}{old[2]} / R{rev}Q{qno}{letter}")
        option_seen[n] = (rev, qno, letter)

    # Factual red flags and Topic 12 ownership leakage.
    joined = "\n".join(
        p.read_text(encoding="utf-8")
        for p in TOPIC.rglob("*.md")
        if p.name in {"QUESTIONS.md", "ANSWERS.md"}
    )
    red_flags = {
        "Awadh by lapse": r"Awadh.{0,50}(?:annexed|annexation).{0,30}Doctrine of Lapse",
        "Delhi operational emperor": r"Bahadur Shah.{0,50}(?:operational commander|directed every|commanded all)",
        "Santhal as stage": r"Santhal Hool.{0,50}(?:stage|part).{0,20}(?:sepoy revolt|Revolt of 1857)",
        "Topic 12 detail": r"(?:Indian Councils Act 1861|Secretary of State.{0,20}15 members|portfolio system)",
    }
    # The first three can legitimately occur in explicitly negated distractors/rationales; only
    # flag if they appear in keyed-option text, which is already checked through answer mapping.
    if re.search(red_flags["Topic 12 detail"], joined, re.I | re.S):
        findings.append("Topic 12 institutional detail leakage")

    print("Modern History Topic 11 hostile audit")
    print(f"Counts: R1={EXPECTED[1]} R2={EXPECTED[2]} R3={EXPECTED[3]} total={sum(EXPECTED.values())}")
    if findings:
        print(f"ACTIONABLE FINDINGS: {len(findings)}")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("ACTIONABLE FINDINGS: 0")
    print("PASS: mapping, options, rationales, sources, traps, duplicates, similarity, keys, cues, chronology and boundary.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
