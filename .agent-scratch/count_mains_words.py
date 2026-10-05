import re
path = r"live_sessions\Polity\38-Lokpal-and-Lokayuktas\Learning-Session-Live-Edition.md"
text = open(path, encoding='utf-8').read()

pattern = re.compile(r'\*\*Mains model answer:\*\*\s*(.*?)(?=\n\n\*\*Scoring rubric)', re.S)
matches = pattern.findall(text)
print("Count of 'Mains model answer' blocks:", len(matches))
for i, m in enumerate(matches, 1):
    words = len(m.split())
    print(i, words)

# also find mains question headers preceding, to label 10/15/20
qpat = re.compile(r'##+ .*?(\d+)\s*marks?\s*\|\s*(\d+)\s*words', re.I)
headers = qpat.findall(text)
print("Headers (marks, word_limit):", headers)
