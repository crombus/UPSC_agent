"""
Scratch/temp helper (deleted at end of task) to build the Topic 06 workbook's
independently-reordered MCQ blocks from the already-written, verified session file.

It NEVER changes any factual content: it only re-distributes the same four
option texts across the four letter slots per question, and re-derives the
correct letter from this workbook's OWN independent A->B->C->D rotation
(separate from the session file's rotation), per the task's explicit
instruction: "Learning, broad and remedial sets independently exact A->B->C->D
rotations; actual options reordered."
"""
import re
import random

SRC = r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\upsc-ai-kit\knowledge\Modern-Indian-History\learning-sessions\06_Structure-of-Government-and-Constitutional-Development-1757-1858_Complete-Learning-Session_2026-08-19.md"
OUT = r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\_topic06_workbook_mcq_blocks.txt"

with open(SRC, "r", encoding="utf-8") as f:
    lines = f.readlines()

def get_block(start_idx_1based, end_idx_1based):
    # inclusive line numbers, 1-based, as reported by grep
    return "".join(lines[start_idx_1based - 1:end_idx_1based - 1])

# Exact section boundaries confirmed via grep line numbers (header lines):
# Learning MCQs header @449 ... Broad MCQs header @739 ... Remedial header @1363 ... Mains header @1595
learning_raw = get_block(449, 739)
broad_raw = get_block(739, 1363)
remedial_raw = get_block(1363, 1595)

Q_RE = re.compile(
    r"### Q(\d+)\.\s*(.+?)\n\n"
    r"A\.\s*(.+?)\n\n"
    r"B\.\s*(.+?)\n\n"
    r"C\.\s*(.+?)\n\n"
    r"D\.\s*(.+?)\n\n"
    r"\*\*Answer:\s*([A-D])\.\s*(.+?)\*\*\n\n"
    r"\*\*Explanation:\*\*\s*(.+?)\n\n",
    re.DOTALL,
)

def parse_questions(raw_text):
    out = []
    for m in Q_RE.finditer(raw_text):
        num, stem, a, b, c, d, ans_letter, ans_text, expl = m.groups()
        opts = {"A": a.strip(), "B": b.strip(), "C": c.strip(), "D": d.strip()}
        out.append({
            "num": int(num),
            "stem": stem.strip(),
            "opts": opts,
            "correct_letter": ans_letter.strip(),
            "explanation": expl.strip(),
        })
    return out

learning_qs = parse_questions(learning_raw)
broad_qs = parse_questions(broad_raw)
remedial_qs = parse_questions(remedial_raw)

print("Parsed counts:", len(learning_qs), len(broad_qs), len(remedial_qs))
assert len(learning_qs) == 20, len(learning_qs)
assert len(broad_qs) == 44, len(broad_qs)
assert len(remedial_qs) == 16, len(remedial_qs)

LETTERS = ["A", "B", "C", "D"]

# Manual fix for the one explanation in the whole set that references option
# letters directly (Learning Q13, Charter Act 1813 provisions) so it stays
# correct regardless of how options are reordered below.
EXPLANATION_OVERRIDES = {
    13: "The tea/China exception is the exact, frequently tested precision point of this provision; the other three options each misstate the Act's actual scope -- claiming no exceptions at all, claiming direct Parliamentary revenue control, and claiming outright charter abolition are all incorrect.",
}

def reorder_section(qs, section_start_num):
    """Return list of dicts: num, stem, new_opts (A-D), new_correct_letter, explanation."""
    rebuilt = []
    for i, q in enumerate(qs):
        target_letter = LETTERS[i % 4]
        correct_text = q["opts"][q["correct_letter"]]
        distractor_texts = [q["opts"][L] for L in LETTERS if L != q["correct_letter"]]
        original_full_order = [q["opts"][L] for L in LETTERS]

        rnd = random.Random(1000 + q["num"])  # deterministic per question
        attempt = 0
        while True:
            shuffled_distractors = distractor_texts[:]
            rnd.shuffle(shuffled_distractors)
            remaining_letters = [L for L in LETTERS if L != target_letter]
            new_opts = {target_letter: correct_text}
            for L, txt in zip(remaining_letters, shuffled_distractors):
                new_opts[L] = txt
            new_full_order = [new_opts[L] for L in LETTERS]
            attempt += 1
            # Force a genuine reorder: never allow the new A/B/C/D arrangement
            # to exactly reproduce the original A/B/C/D arrangement.
            if new_full_order != original_full_order or attempt > 20:
                break

        explanation = EXPLANATION_OVERRIDES.get(q["num"], q["explanation"])

        rebuilt.append({
            "num": q["num"],
            "stem": q["stem"],
            "new_opts": new_opts,
            "new_correct_letter": target_letter,
            "explanation": explanation,
        })
    return rebuilt

learning_rebuilt = reorder_section(learning_qs, 1)
broad_rebuilt = reorder_section(broad_qs, 21)
remedial_rebuilt = reorder_section(remedial_qs, 65)

# Sanity: verify rotation is a clean A,B,C,D repeat and verify no option text was
# altered/lost/duplicated within any single question, and verify at least a
# meaningful share of positions actually changed vs. the original (genuine reorder).
def verify(original_qs, rebuilt_qs, label):
    changed = 0
    identical_full_order = 0
    for orig, reb in zip(original_qs, rebuilt_qs):
        orig_set = set(orig["opts"].values())
        reb_set = set(reb["new_opts"].values())
        assert orig_set == reb_set, f"{label} Q{orig['num']}: option text set mismatch!"
        assert reb["new_opts"][reb["new_correct_letter"]] == orig["opts"][orig["correct_letter"]], f"{label} Q{orig['num']}: correct text moved incorrectly!"
        if orig["correct_letter"] != reb["new_correct_letter"]:
            changed += 1
        orig_full = [orig["opts"][L] for L in LETTERS]
        reb_full = [reb["new_opts"][L] for L in LETTERS]
        if orig_full == reb_full:
            identical_full_order += 1
    print(f"{label}: correct-letter changed in {changed}/{len(rebuilt_qs)} questions; identical full A-D order in {identical_full_order}/{len(rebuilt_qs)} (must be 0)")
    assert identical_full_order == 0, f"{label}: found {identical_full_order} questions with unchanged option order!"

verify(learning_qs, learning_rebuilt, "Learning")
verify(broad_qs, broad_rebuilt, "Broad")
verify(remedial_qs, remedial_rebuilt, "Remedial")

def render_section(rebuilt_qs):
    parts = []
    for q in rebuilt_qs:
        block = f"### Q{q['num']}. {q['stem']}\n\n"
        for L in LETTERS:
            block += f"{L}. {q['new_opts'][L]}\n\n"
        correct_text = q["new_opts"][q["new_correct_letter"]]
        block += f"**Answer: {q['new_correct_letter']}. {correct_text}**\n\n"
        block += f"**Explanation:** {q['explanation']}\n"
        parts.append(block)
    return "\n".join(parts)

with open(OUT, "w", encoding="utf-8") as f:
    f.write("=== LEARNING MCQS (reordered) ===\n\n")
    f.write(render_section(learning_rebuilt))
    f.write("\n=== BROAD MCQS (reordered) ===\n\n")
    f.write(render_section(broad_rebuilt))
    f.write("\n=== REMEDIAL MCQS (reordered) ===\n\n")
    f.write(render_section(remedial_rebuilt))

print("Wrote:", OUT)

# Print rotation sequences for verification
print("Learning rotation:", [q["new_correct_letter"] for q in learning_rebuilt])
print("Broad rotation:", [q["new_correct_letter"] for q in broad_rebuilt])
print("Remedial rotation:", [q["new_correct_letter"] for q in remedial_rebuilt])
