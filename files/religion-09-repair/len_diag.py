import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
T = (BASE / 'part-06-mcq-01-12.md').read_text(encoding='utf-8') + \
    (BASE / 'part-07-mcq-13-32.md').read_text(encoding='utf-8')
blocks = re.split(r'^#### MCQ (\d+)\. ', T, flags=re.M)[1:]
for num, body in zip(blocks[0::2], blocks[1::2]):
    ans = re.search(r'\*\*Answer: ([A-D])\.\*\*', body).group(1)
    opts = dict(re.findall(r'^([A-D])\. (.+)$', body, flags=re.M))
    lens = {k: len(v) for k, v in opts.items()}
    mark = 'LONGEST' if lens[ans] == max(lens.values()) else (
        'shortest' if lens[ans] == min(lens.values()) else '')
    print(f"{num:>2} {ans} " + ' '.join(f"{k}:{lens[k]:3d}" for k in 'ABCD') +
          f"  delta={lens[ans]-sum(v for k,v in lens.items() if k!=ans)/3:+.0f}  {mark}")
