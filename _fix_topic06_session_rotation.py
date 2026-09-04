"""
One-time fix: repair the A->B->C->D exact rotation in Topic 06's session-file
Learning / Broad / Remedial MCQ sections (the session file, not the workbook,
which was already independently and correctly rotated).

For each section, question index i (0-based) must have correct answer at
letter 'ABCD'[i % 4]. Where the original does not match, the correct option's
TEXT is moved to the target letter slot, and the three distractor TEXTS are
moved (preserving their original relative order) into the remaining letter
slots. Only text position changes; no option text is invented, altered, or
deleted. The Answer line is rewritten to match the new letter + text.
"""
import re

FNAME = r"upsc-ai-kit\knowledge\Modern-Indian-History\learning-sessions\06_Structure-of-Government-and-Constitutional-Development-1757-1858_Complete-Learning-Session_2026-08-19.md"

with open(FNAME, encoding="utf-8") as f:
    text = f.read()

SECTIONS = [
    ("Learning", "## Learning MCQs", "## Broad MCQs"),
    ("Broad", "## Broad MCQs", "## Remedial MCQs"),
    ("Remedial", "## Remedial MCQs", "## Mains practice"),
]

total_fixed = 0
report = []

for label, start_marker, end_marker in SECTIONS:
    start = text.index(start_marker)
    end = text.index(end_marker)
    section = text[start:end]

    # Split into question blocks, keeping the header line as part of each block.
    parts = re.split(r"(?=^### Q\d+\.)", section, flags=re.MULTILINE)
    preamble = parts[0]
    qblocks = parts[1:]

    new_qblocks = []
    section_fixed = 0
    for i, qb in enumerate(qblocks):
        target_letter = "ABCD"[i % 4]

        # Extract the 4 option lines (single physical lines "X. text").
        opt_matches = list(re.finditer(r"^([A-D])\. (.+)$", qb, flags=re.MULTILINE))
        assert len(opt_matches) == 4, f"{label} Q{i+1}: expected 4 options, got {len(opt_matches)}"
        options = {m.group(1): m.group(2) for m in opt_matches}

        # Extract answer line.
        ans_match = re.search(r"^\*\*Answer: ([A-D])\. (.+?)\*\*\s*$", qb, flags=re.MULTILINE)
        assert ans_match, f"{label} Q{i+1}: no Answer line found"
        answer_letter = ans_match.group(1)
        answer_text = ans_match.group(2)
        assert options[answer_letter].strip() == answer_text.strip(), (
            f"{label} Q{i+1}: answer text mismatch vs option {answer_letter}"
        )

        if answer_letter == target_letter:
            new_qblocks.append(qb)
            continue

        # Build new arrangement: correct text -> target_letter;
        # remaining texts (original A,B,C,D order, excluding the correct one)
        # -> remaining letters in A,B,C,D order.
        correct_text = options[answer_letter]
        distractor_texts = [options[L] for L in "ABCD" if L != answer_letter]
        remaining_letters = [L for L in "ABCD" if L != target_letter]

        new_options = {target_letter: correct_text}
        for L, txt in zip(remaining_letters, distractor_texts):
            new_options[L] = txt

        assert set(new_options.keys()) == {"A", "B", "C", "D"}
        # Sanity: full new arrangement must differ from the old one.
        old_tuple = tuple(options[L] for L in "ABCD")
        new_tuple = tuple(new_options[L] for L in "ABCD")
        assert old_tuple != new_tuple, f"{label} Q{i+1}: reorder produced identical arrangement"

        # Rewrite the 4 option lines in place, first-to-last as they appear in qb.
        new_qb = qb
        for m in reversed(opt_matches):
            old_letter = m.group(1)
            replacement = f"{old_letter}. {new_options[old_letter]}"
            new_qb = new_qb[: m.start()] + replacement + new_qb[m.end() :]

        # Rewrite the Answer line.
        new_qb = re.sub(
            r"^\*\*Answer: [A-D]\. .+?\*\*\s*$",
            f"**Answer: {target_letter}. {correct_text}**",
            new_qb,
            count=1,
            flags=re.MULTILINE,
        )

        new_qblocks.append(new_qb)
        section_fixed += 1

    new_section = preamble + "".join(new_qblocks)
    text = text[: start] + new_section + text[end:]
    # Re-locate markers for next iteration since text length may have changed
    # only within this section's own bounds (markers unaffected since they are
    # section-header substrings that remain textually identical -- but offsets
    # after this section shift). Recompute at top of next loop iteration since
    # we search from scratch each time via text.index().
    total_fixed += section_fixed
    report.append((label, section_fixed, len(qblocks)))

with open(FNAME, "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed questions per section:")
for label, fixed, tot in report:
    print(f"  {label}: {fixed} / {tot} reordered")
print("Total reordered:", total_fixed)
