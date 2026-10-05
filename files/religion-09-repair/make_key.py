"""Generate an independently randomised, length-balanced-friendly 32-item answer key.

Constraints enforced:
  * exactly 8 of each of A, B, C, D overall
  * exactly 2 of each letter in every consecutive block of eight
  * no adjacent repetition
  * no ascending or descending rotation window of length 4 anywhere
  * no repeated 4-gram anywhere in the sequence
"""
import random

LETTERS = "ABCD"
ROT_ASC = [LETTERS[i:] + LETTERS[:i] for i in range(4)]
ROT_DESC = [s[::-1] for s in ROT_ASC]
BANNED_WINDOWS = set(ROT_ASC) | set(ROT_DESC)


def block_ok(seq):
    for start in (0, 8, 16, 24):
        block = seq[start:start + 8]
        if len(block) == 8:
            for ch in LETTERS:
                if block.count(ch) != 2:
                    return False
    return True


def windows_ok(seq):
    grams = [seq[i:i + 4] for i in range(len(seq) - 3)]
    if any(g in BANNED_WINDOWS for g in grams):
        return False
    return len(set(grams)) == len(grams)


def adjacent_ok(seq):
    return all(a != b for a, b in zip(seq, seq[1:]))


def build(rng):
    pool = list(LETTERS * 8)
    rng.shuffle(pool)
    seq = ""
    remaining = pool[:]
    for _ in range(32):
        rng.shuffle(remaining)
        placed = False
        for cand in remaining:
            trial = seq + cand
            if not adjacent_ok(trial):
                continue
            grams = [trial[i:i + 4] for i in range(len(trial) - 3)]
            if any(g in BANNED_WINDOWS for g in grams):
                continue
            if len(set(grams)) != len(grams):
                continue
            idx = len(trial) - 1
            blk = idx // 8
            block = trial[blk * 8:]
            if any(block.count(ch) > 2 for ch in LETTERS):
                continue
            seq = trial
            remaining.remove(cand)
            placed = True
            break
        if not placed:
            return None
    return seq


def main():
    rng = random.Random(20260910)
    for _ in range(200000):
        seq = build(rng)
        if seq and block_ok(seq) and windows_ok(seq) and adjacent_ok(seq):
            print(seq)
            print("counts:", {c: seq.count(c) for c in LETTERS})
            print("blocks:", [seq[i:i + 8] for i in range(0, 32, 8)])
            return
    print("no key found")


if __name__ == "__main__":
    main()
