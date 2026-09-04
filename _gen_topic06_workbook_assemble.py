import io

BASE = r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent"
OUT = BASE + r"\upsc-ai-kit\knowledge\Modern-Indian-History\learning-sessions\06_Structure-of-Government-and-Constitutional-Development-1757-1858_Premium-Solved-PYQ-Workbook_2026-08-19.md"

drills_block = open(BASE + r"\_topic06_drills_block.txt", encoding="utf-8").read()
mains_block = open(BASE + r"\_topic06_mains_block.txt", encoding="utf-8").read()
mcq_raw = open(BASE + r"\_topic06_workbook_mcq_blocks.txt", encoding="utf-8").read()

# Split the generated MCQ blocks file into its three sections
learning_part = mcq_raw.split("=== LEARNING MCQS (reordered) ===\n\n")[1].split("\n=== BROAD MCQS")[0]
broad_part = mcq_raw.split("=== BROAD MCQS (reordered) ===\n\n")[1].split("\n=== REMEDIAL MCQS")[0]
remedial_part = mcq_raw.split("=== REMEDIAL MCQS (reordered) ===\n\n")[1]

ASSET = "../../../../notes/Modern-Indian-History/assets/06_Constitutional-Development-1757-1858"

front_matter = f"""---
cover_image: {ASSET}/00_00_cover.png
---
# Modern History 06 -- Structure of Government and Constitutional Development, 1757-1858 -- Premium Solved PYQ Workbook

> Subject: Modern Indian History | GS-I | Prelims and Mains | Date: 2026-08-19. This is a separate solved-practice workbook; no verified direct owner PYQ is invented.


![Visual 0: workbook cover]({ASSET}/00_00_cover.png)

*Visual 0: workbook cover. Original deterministic study visual; schematic charts are NOT TO SCALE where marked.*


**Companion workbook to the Complete Learning Session dated 2026-08-19.** This file is a standalone, self-contained solved-practice companion: it does not repeat the full teaching narrative (Parts I-VIII of the main session), which lives in the paired Complete Learning Session file and the canonical knowledge-base package. It opens with the transparent PYQ audit, then six compact evidence banks that carry just enough locked fact to attempt every question below without returning to the main file, then reproduces the complete practice set -- drills and all three MCQ sets, each independently re-derived here with its own A -> B -> C -> D rotation and its options genuinely reordered from the learning session's own version of the same question -- and, finally, all twelve Mains model answers in full.

# PART IX -- SOURCES, PYQ AUDIT AND PRACTICE

## Transparent PYQ audit and route decision

**Audit scope:** every Prelims and Mains GS-I/GS-II/CSAT routing ledger and integration-audit file currently in the repository (`_PYQ-ROUTING-PRELIMS-2018-2023.md`, `_PYQ-ROUTING-PRELIMS-2024-2025.md`, `_PYQ-ROUTING-PRELIMS-2026.md`, `_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md`, `_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md`, `PYQ-INTEGRATION-AUDIT-2018-2023.md`, `PYQ-INTEGRATION-AUDIT-2024-2025.md`, `PYQ-INTEGRATION-AUDIT-2026.md`) was checked line by line for any question mentioning the Regulating Act, the Supreme Court at Calcutta, Nand Kumar, the Amending Act/Act of Settlement, Pitt's India Act, the Board of Control, the Act of 1786, the Charter Acts of 1793/1813/1833/1853, the Governor-General/Viceroy title sequence, or the Government of India Act, 1858.

**Audit result:** this topic **owns exactly two verified, directly routed Prelims PYQs**, both attributed by the ledgers to `Modern-Indian-History/basic/06_Government-Structure-and-Constitutional-Development-1757-1858.md`, with no further item found routed here in any checked ledger (2018-2023, 2024-2025 or 2026; Prelims, Mains or CSAT):

1. **2019 Prelims, GS-I, Q4** -- Charter Act of 1813 provisions, solved in full immediately below, marked "Routed; key unavailable locally" in the ledger.
2. **2023 Prelims, GS-I, Q50** -- the Act designating the Governor-General of Bengal as Governor-General of India, solved in full immediately below, also marked "Routed; key unavailable locally."

The companion per-file audits (`PYQ-INTEGRATION-AUDIT-2018-2023.md` and later years) separately confirm that the advanced/06 file itself carries no additional directly routed question beyond these same two, which are attributed to the basic/06 file. **No further PYQ is claimed for this topic.** Neither question's official answer key exists in any locally held file (confirmed after an exhaustive local search restricted to genuinely available official keys covering 2024, 2025 and 2026 only); both answers below are therefore independently derived from this workbook's own verified statutory evidence and explicitly labelled `INFERRED ANSWER -- NOT OFFICIALLY VERIFIED`, each with a stated confidence level and full elimination reasoning. Where this workbook's own original MCQs and Mains questions appear below, they are clearly original practice material, not represented as previous UPSC questions.

### PYQ 1 solved -- 2019 Prelims, GS-I, Q4 (Charter Act, 1813)

**Question (exact, as recovered from local official OCR):** "Consider the following statements about 'the Charter Act of 1813':
1. It ended the trade monopoly of the East India Company in India except for trade in tea and trade with China.
2. It asserted the sovereignty of the British Crown over the Indian territories held by the Company.
3. The revenues of India were now controlled by British Parliament.
Which of the statements given above are correct?"

(a) 1 and 2 only

(b) 2 and 3 only

(c) 1 and 3 only

(d) 1, 2 and 3

**Official key status:** not held locally; a targeted search across every locally available official Civil Services Preliminary Examination 2019 answer-key source was carried out before concluding this, and no locally verifiable official key text was found. The label below therefore applies in full.

**`INFERRED ANSWER -- NOT OFFICIALLY VERIFIED`: (a) 1 and 2 only.**

**Confidence:** High.

**Elimination reasoning:**
- **Statement 1 is TRUE:** the Charter Act of 1813 ended the Company's trade monopoly in India for other British subjects while specifically preserving the Company's exclusive monopoly over tea and all China trade, exactly as this statement describes.
- **Statement 2 is TRUE:** the Act's own language asserted the "undoubted sovereignty of the Crown of the United Kingdom" over the Company's Indian territories, exactly the claim this statement makes.
- **Statement 3 is FALSE:** Indian revenues remained under the Company's own administration throughout this period; the Board of Control (from 1784) supervised and could direct Company policy, but this is political and administrative superintendence, not direct parliamentary control of revenue itself, and no provision of the 1813 Act transferred revenue control to Parliament.
- **Because statement 3 is false,** any option containing it -- (b), (c) and (d) -- is eliminated, leaving only **(a) 1 and 2 only**.

**Why this matters for exam technique:** this is a bundled multi-statement question testing three genuinely independent claims within a single Act; the safest method is to verify each statement separately against the Act's own three distinct provisions (trade, sovereignty, revenue) rather than forming one undifferentiated impression of "1813 as a reforming Act."

### PYQ 2 solved -- 2023 Prelims, GS-I, Q50 (Governor-General designation, Charter Acts)

**Question (exact, as recovered from local official OCR):** "By which one of the following Acts was the Governor General of Bengal designated as the Governor General of India?"

(a) The Regulating Act

(b) The Pitt's India Act

(c) The Charter Act of 1793

(d) The Charter Act of 1833

**Official key status:** not held locally; a targeted search across every locally available official Civil Services Preliminary Examination 2023 answer-key source was carried out before concluding this, and no locally verifiable official key text was found. The label below therefore applies in full.

**`INFERRED ANSWER -- NOT OFFICIALLY VERIFIED`: (d) The Charter Act of 1833.**

**Confidence:** Very high.

**Elimination reasoning:**
- **Option (a), the Regulating Act (1773), is eliminated:** it created the office of Governor-General of Fort William/Bengal, a Bengal-specific title, with no all-India scope.
- **Option (b), Pitt's India Act (1784), is eliminated:** it reduced the Bengal Council to three members and created the Board of Control in London, but did not touch the Governor-General's own title or create any all-India office.
- **Option (c), the Charter Act of 1793, is eliminated:** it renewed the Company's charter and trade monopoly for twenty years and codified Cornwallis-era regulations, with no title change to the Governor-Generalship.
- **Option (d), the Charter Act of 1833, is correct:** this Act explicitly upgraded the Governor-General of Bengal into the Governor-General of India, the office first held in this all-India form by Lord William Bentinck, exactly matching the question's own wording.

**Why this matters for exam technique:** a direct "which Act did X" question across four genuinely different Acts rewards keeping a clean office-title ladder (Governor-General of Fort William/Bengal, 1773 -> Governor-General of India, 1833 -> Viceroy, 1858) rather than a vague sense that "some Charter Act" made this change.

## Evidence Bank 1 -- Actors and motives (one line each)

| Actor | Role / motive |
|---|---|
| Robert Clive | First Governor of Bengal under Company rule (to 1767); later criticised over patronage/corruption, feeding the 1772-73 crisis anxieties |
| Warren Hastings | First Governor-General of Fort William/Bengal under the Regulating Act, 1773; central figure in the 1774-76 Council deadlock and the Nand Kumar episode |
| Philip Francis | Leading figure of the standing 3-1 Council majority (with Clavering and Monson) that outvoted Hastings, 1774-76 |
| Elijah Impey | First Chief Justice of the Supreme Court at Calcutta under the 1774 Charter; a close personal associate of Hastings; presided over Nand Kumar's 1775 trial |
| Maharaja Nand Kumar | Accused Hastings of corruption before the Council; separately tried on an 1770 forgery charge and executed, 1775 -- treated source-critically, never as settled fact |
| William Pitt the Younger | British Prime Minister; steered Pitt's India Act, 1784 through Parliament, creating the Board of Control and the Secret Committee |
| Lord Cornwallis | Governor-General, 1786-93; received the Act of 1786's override power; oversaw the Charter Act, 1793's continuation and codification |
| Lord William Bentinck | Governor-General of Bengal since 1828; became the first Governor-General of India under the Charter Act, 1833 |
| Thomas Babington Macaulay | First Law Member of the Governor-General's Council under the Charter Act, 1833; chaired the Law Commission; later chaired the 1854 Civil Service (Macaulay) Committee |
| Lord Canning | Governor-General since 1856; became the first Viceroy under the Government of India Act, 1858 |

## Evidence Bank 2 -- Master date list

| Date | Event |
|---|---|
| 1765-72 | Diwani grant and the Dual Government (Topic 04; referenced here only as this topic's starting trigger) |
| 1772-73 | Company financial crisis, government loan request, parliamentary patronage/accountability debate |
| 1773 | Regulating Act |
| 1774 | Supreme Court at Calcutta established (1774 Charter); Hastings-Council 3-1 deadlock begins |
| 1775 | Nand Kumar trial and execution |
| 1776 | Monson's death contingently, non-statutorily, breaks the Council deadlock |
| 1777-79 | Patna Case |
| 1779-80 | Cossijurah Case |
| 1781 | Amending Act (Act of Settlement) |
| 1784 | Pitt's India Act; Board of Control and Secret Committee created; Bengal Council reduced to three |
| 1786 | Act of 1786; Cornwallis given a direct override power |
| 1793 | Charter Act, 1793; twenty-year charter renewal; Cornwallis-era codification continued |
| 1813 | Charter Act, 1813; trade monopoly ends except tea/China; Crown sovereignty asserted; missionaries permitted; education grant authorised |
| 1833 | Charter Act, 1833; Company's commercial role ends entirely; Governor-General of India created (Bentinck); Law Member and Law Commission created; non-discrimination clause enacted |
| 1853 | Charter Act, 1853; no fixed term ("until Parliament shall otherwise provide"); additional legislative members added |
| 1854 | Macaulay Committee designs the competitive-examination mechanism for the Indian Civil Service |
| 1855 | First competitive examination for the Indian Civil Service actually held |
| 1857-58 | Revolt of 1857 (Topic 11; referenced here only as a structural trigger among several for 1858) |
| 1858 | Government of India Act, 1858; Company rule, Board of Control and Court of Directors abolished; Secretary of State and Council of India created; Canning becomes first Viceroy |
| 1 Nov 1858 | Queen's Proclamation -- a separate political-policy document, not the 1858 Act itself |

## Evidence Bank 3 -- Key figures and sums (hold loosely, cite as estimates where marked)

- Regulating Act, 1773: Bengal Council of four members total, including the Governor-General -- the design that produced the 1774-76 standing 3-1 majority against Hastings.
- Pitt's India Act, 1784: Bengal Council reduced to three members total (Governor-General plus two), structurally lowering the odds of a standing hostile majority.
- Pitt's India Act, 1784: Board of Control of six members, including the Secretary of State and the Chancellor of the Exchequer -- a different body, at a different date, from the fifteen-member Council of India created only in 1858.
- Charter Act, 1793: renewed the Company's charter and trade monopoly for twenty years, the same fixed-term pattern later repeated in 1813 and 1833, and explicitly broken in 1853.
- Charter Act, 1813: one lakh rupees a year statutorily earmarked for "the revival and promotion of literature and the encouragement of the learned natives of India" and useful scientific knowledge -- a statutory authorisation whose actual disbursement was delayed for years, a matter resolved only by Macaulay's 1835 Minute on Education (Topic 09), not by this topic.
- Government of India Act, 1858: statutory Council of India of fifteen members, with an initial majority of seven having prior East India Company service or directorship experience -- this topic's clearest single "rupture within continuity" marker.
- Charter Act, 1853: added additional legislative members (judges of the Calcutta Supreme Court, and representatives drawn from the Madras, Bombay, Bengal and Agra/North-Western Provinces administrations) to the Governor-General's Council for legislative purposes, distinct from the smaller existing executive Council -- procedural/administrative broadening, not political representation, and no Indian sat on this enlarged Council.

## Evidence Bank 4 -- Document and institution distinctions

- **Bengal's Dual Government (1765-72, Topic 04) vs Pitt's India Act's "dual control" (1784 onward):** two entirely distinct institutions, separated by both decade and geography -- the Dual Government split the Nawab's Nizamat from the Company's Diwani inside Bengal; dual control split the Board of Control from the Court of Directors, both sitting in Britain.
- **The Government of India Act, 1858 vs the Queen's Proclamation, 1 November 1858:** the Act is the constitutional-legal transfer instrument (abolishing Company rule, the Board of Control and the Court of Directors; creating the Secretary of State and the Council of India); the Proclamation is the separate political-policy announcement (non-interference in religion, treaty recognition, formal equality before law, qualified amnesty) -- never answer a question about one with content that belongs only to the other.
- **The Patna Case (1777-79) vs the Cossijurah Case (1779-80):** Patna was a personal-law/civil-court jurisdiction clash; Cossijurah was a revenue-administration jurisdiction clash; both are instances of the same underlying Supreme-Court-versus-Company-courts overlap, but they are not the same case and should never be merged.
- **The Amending Act, 1781, vs Pitt's India Act, 1784:** 1781 corrected Supreme Court jurisdiction (official-acts exemption, revenue-matter exclusion, personal-law direction, provincial-appeal routing); 1784 fixed the separate executive-deadlock problem (smaller council, Board of Control) -- never credit 1781 with fixing the Council's own voting deadlock.
- **The 1833 non-discrimination clause vs the 1853/1854/1855 civil-service reform sequence:** 1833 was a formal legal promise with a thin practical outcome for decades; the genuine mechanism for competitive entry arrived only via the 1853 Act's open principle, the 1854 Macaulay Committee's design, and the first actual 1855 examination -- never state that 1833 alone opened the civil service in practice.

## Evidence Bank 5 -- Historiography quick-reference

| Lens | Associated historian(s) | Core emphasis |
|---|---|---|
| Critical political-economy reading | Bipan Chandra | Company financial crisis and parliamentary patronage/accountability anxiety, not humanitarian motive, as intervention's real driver; British fiscal, mercantile and imperial interest as the frame |
| Administrative/rule-of-law maturation | Not tied to a single named historian in this topic's own sourced material | A genuine, if slow and repeatedly improvised, maturation of accountable, rule-bound governance out of an initially undisciplined trading-company administration |
| Company-state/corporate-sovereignty improvisation | A recent broad historiographical trend, not attributed here to one named individual | The Company as an unusual hybrid sovereign-and-commercial entity; the 1773-1858 Acts read as a chain of largely ad hoc, crisis-driven institutional fixes, each responding to the failure exposed by the one before it |
| Free-trade/industrial-capital transition | Not tied to a single named historian in this topic's own sourced material | Connects the 1813 trade opening and the 1833 commercial wind-up to Britain's own domestic shift from mercantilist monopoly toward industrial free trade, driven by manufacturing/mercantile lobbies |

**These four lenses are complementary emphases on the same eleven Acts, not four mutually exclusive accounts of different events** -- a strong Mains answer may use more than one lens on the same Act (for instance, reading 1833 through both the administrative-centralisation lens and the free-trade/industrial-capital lens at once).

## Evidence Bank 6 -- Topic-boundary quick-reference

| Adjacent theme | Owning topic | This workbook's treatment |
|---|---|---|
| Diwani grant, Dual Government, 1765-72 | Topic 04 | Referenced only as this topic's own starting trigger |
| Territorial expansion (Mysore, Marathas, Sikhs) financed by this governance structure | Topic 05 | Not analysed here |
| Full colonial economic impact, drain of wealth, land revenue systems | Topic 07 | Named as forward bridge only |
| Detailed civil service, police and judiciary structures | Topic 08 | Detailed service structure explicitly routed there; only the 1833-1853-1854-1855 reform sequence is covered here |
| Education and press policy, including the 1835 Minute on Education | Topic 09 | Named as forward bridge only; the 1813 education grant's authorisation is covered here, its implementation is not |
| The Revolt of 1857 in full | Topic 11 | Referenced here only as a structural trigger among several for the 1858 Act, never analysed in its own right |
| Post-1858 councils and Crown administration (Indian Councils Act, 1861, onward) | Topic 12 | Named as forward bridge only; this topic's own endpoint is fixed precisely at 1858 |

**Exactly two PYQs are directly routed to Topic 06** across this repository's own ledgers (2018-2026, all Prelims and Mains windows) -- see the full audit immediately above for the complete methodology.

"""

full_text = front_matter + drills_block + "\n"
full_text += "## Learning MCQs (20; key rotation A -> B -> C -> D, independently re-derived and re-ordered from the learning session)\n\n"
full_text += "Correct options are deliberately rotated by actual option placement, not by relabelling: A -> B -> C -> D through the full set. This workbook's own rotation and option order are independently derived from the learning session's version of each question -- the underlying facts are identical, but the position of the correct option, and the order of the distractors, genuinely differ here. Read the explanation after attempting each item.\n\n"
full_text += learning_part + "\n"
full_text += "## Broad MCQs (44; key rotation A -> B -> C -> D repeated eleven times, independently re-derived and re-ordered from the learning session)\n\n"
full_text += broad_part + "\n"
full_text += "## Remedial MCQs (16; targeted at this topic's most common specific errors, independently re-derived and re-ordered from the learning session)\n\n"
full_text += "Each item below corrects a real, frequently seen misstatement. Read the flawed student statement, then select the accurate remedial correction.\n\n"
full_text += remedial_part + "\n"
full_text += mains_block

with open(OUT, "w", encoding="utf-8") as f:
    f.write(full_text)

print("Wrote:", OUT)
words = len(full_text.split())
print("Words:", words)
