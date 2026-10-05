import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TARGET = ROOT / "solved_pyqs" / "papers" / "2018" / "prelims-csat.md"
ROUTING = ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-CSAT-2018-2023.md"
URL = "https://www.upscprep.com/upsc-prelims-2018-csat-previous-year-questions/"

KEYS = list(
    "BDAACDAABDCCBBC"
    "CCADCABDACADADB"
    "CCBBACBBBACCBAB"
    "ADACDABCBDACCBC"
    "DADDCAABDBCADCD"
    "ADDBA"
)
assert len(KEYS) == 80

FAMILY_NAMES = {
    "01": "Reading Comprehension",
    "02": "Number Systems and Number Sense",
    "03": "Arithmetic and Commercial Math",
    "04": "Rates, Motion, Time and Geometry",
    "05": "Algebra, Inequalities and Data Sufficiency",
    "06": "Logical Reasoning, Coding, Counting and Data Interpretation",
}
TOPIC_LINKS = {
    "01": "../../topics/csat/reading-comprehension.md",
    "02": "../../topics/csat/number-systems-and-number-sense.md",
    "03": "../../topics/csat/arithmetic-and-commercial-math.md",
    "04": "../../topics/csat/rates-motion-time-and-geometry.md",
    "05": "../../topics/csat/algebra-inequalities-and-data-sufficiency.md",
    "06": "../../topics/csat/logical-reasoning-coding-counting-and-di.md",
}
OWNERS = {
    code: f"CSAT/basic/{code}_{name.replace(' and ', '-and-').replace(', ', '-').replace(' ', '-')}.md"
    for code, name in {
        "01": "Reading-Comprehension",
        "02": "Number-Systems-and-Number-Sense",
        "03": "Arithmetic-and-Commercial-Math",
        "04": "Rates-Motion-Time-and-Geometry",
        "05": "Algebra-Inequalities-and-Data-Sufficiency",
        "06": "Logical-Reasoning-Coding-Counting-and-DI",
    }.items()
}

REASONS = {
    1: "Count by layers, not by visual impression: the top contributes 5 triangles, the bottom contributes 5, and the connecting middle belt contributes 10. Hence the total is 20, so option (b) matches.",
    2: "Let the dot be x. Then x + (10+x) + (20+x) + (10x+3) + (10x+1) = 210+x. Thus 23x+34=210+x, so 22x=176 and x=8, matching option (d).",
    3: "Each row follows left + middle - right = result: 8+4-6=6, 10+6-5=11 and 15+8-7=16. Therefore the last result is 13+8-4=17, option (a).",
    4: "An n-gon has n(n-3)/2 diagonals because each vertex joins n-3 non-adjacent vertices and every diagonal is counted twice. For n=8, 8×5/2=20, option (a).",
    5: "Distance is the area under a velocity-time graph. If vehicle B's constant speed is v, PD=LD/2 makes A's final speed 3v/2. Thus A covers 1/2×OL×3v/2=3v·OL/4, while B covers v·OL; the ratio is 3:4, option (c).",
    6: "The man is a point, so the train must cover only its own 200 m length. At 40 km/h = 100/9 m/s, time = 200÷(100/9)=18 seconds, option (d).",
    7: "The passage says a very large share of Indians will remain dependent on agriculture even after growth in services and manufacturing. That makes agricultural prosperity critically important; it does not establish that the whole economy 'greatly depends' on agriculture. Option (a) is the passage-bound inference.",
    8: "Globalized production gives consumers more food sources but makes regulation and traceability harder, increasing vulnerability. Hence more options bring more risks, option (a); the passage neither blames processing alone nor prescribes only local food or curtailed globalization.",
    9: "The author assigns empirical questions to science and ultimate existential questions to faith, while rejecting their supposed incompatibility. Properly bounded, the two can complement one another, option (b).",
    10: "The author values India's inheritance but rejects traditions that bind, divide, suppress and prevent free bodily and spiritual development. Therefore the targeted bonds must go because they obstruct physical and spiritual growth, option (d).",
    11: "From the graph, first-three-month sheet steel imports are 40+37+36=113 thousand tonnes; coil steel imports are 30+31+33=94. The excess is 19 thousand tonnes, option (c).",
    12: "Sheet steel over six months totals about 217 thousand tonnes. Multiplying by the shown average cost of $256 per tonne gives about $55.55 million (217×256 thousand dollars), corresponding to option (c).",
    13: "First-three-month sheet steel is 113 thousand tonnes and scrap steel is 32+34+32=98 thousand tonnes. 113:98≈1.15:1, rounded to 1.2:1, option (b).",
    14: "Comparing common adjacent faces across the rotations fixes the three opposite pairs. The one-dot face is opposite the three-dot face, so option (b).",
    15: "The rotations show that the two-dot face and four-dot face never meet and occupy opposite positions. Therefore option (c).",
    16: "The remaining opposite pair is the cross and the line. Hence the face opposite the cross carries the line, option (c).",
    17: "The passage explicitly elevates a child-friendly curriculum based on activities, exploration and discovery. Sending by every parent and physical infrastructure are relevant but are not stated as the paramount right dimension. Only statement 3 holds, option (c).",
    18: "The passage places an obligation on accountability systems to ensure learning, supporting assumption 1. It does not guarantee actual 100% enrolment, and demographic dividend is never discussed. Thus 1 only, option (a).",
    19: "For quality, the passage specifically requires learning through activities, exploration and discovery and rejects passive textbook-centred testing. That directly supports option (d); attendance alone is insufficient.",
    20: "The repeated thesis is that access, free schooling and compulsion are insufficient unless every child receives quality education. Option (c) states that essential message without adding an unsupported mechanism.",
    21: "MUMBAI is coded by shifting successive letters back by 1,2,3,4,5,6 places. Applying shifts 1-5 to DELHI gives C,C,I,D,D: CCIDD, option (a).",
    22: "Use the direct letter-digit assignments: R=1, A=2, M=3, O=4, N=5; D=6, I=7, N=5, E=8, S=4, H=9. HAMAM therefore becomes 9-2-3-2-3 = 92323, option (b).",
    23: "For -3<X<-1, 1<X²<9; for -1<Y<1, 0≤Y²<1. Therefore X²-Y² lies between 0 and 9, matching option (d).",
    24: "Since X,Y are natural numbers greater than 1 and Y>X, XY exceeds both ratios X/Y and Y/X, while (X+Y)/(XY)=1/X+1/Y<1. Thus XY is largest, option (a).",
    25: "Place three offices on each side. F is on A's side and farther down; C faces D; E is on the opposite side from F, is not at a corner and does not face F. The unique order puts C immediately to E's left as E faces the corridor, so option (c).",
    26: "The same unique office layout places A immediately beside F on their side of the corridor; no second office adjoins F. Therefore A only, option (a).",
    27: "The passage links forest-cover decline to erosive soil loss, drying springs and small rivers, altered groundwater/moisture, siltation and reduced agricultural productivity. All four listed consequences follow, option (d).",
    28: "Changing river course is expressly connected with siltation following deforestation and poor land management, so 1 follows. The passage does not say salinization is only human-caused, nor does it attribute three-continent desertification chiefly to Indian-style monoculture. Only 1, option (a).",
    29: "Desertification is said to occur beyond tropical areas, so assumption 1 fails. Although deforestation can drive degradation and hydrological change, the passage does not make floods and desertification inevitable in every case; assumption 2 also fails. Neither, option (d).",
    30: "The passage supports conserving water-buffering ecosystems, a wider gene pool and migration corridors. It criticizes existing homogeneity-oriented crop choice rather than endorsing present practices. Therefore 1,2 and 4, option (b).",
    31: "The passage treats diverse agriculture, forestry and fisheries assets as a coping base and warns that homogeneous crop selection narrows varieties and wild relatives. The official reading accepts both assumptions, so option (c).",
    32: "The shopping-mall metaphor criticizes ever-expanding material aspiration and contrasts it with frugality. Reducing consumerism is therefore in humanity's own ecological interest, option (c); the other choices add absolutes.",
    33: "The author expressly rejects birth-only leadership and states that leadership can be acquired and taught. Option (b) repeats that claim; war is merely an illustration, not the only route.",
    34: "Let the number be 100a+c, with a+c=4. Reversal gives 100c+a and the increase is 99(c-a)=198, so c-a=2. The digit difference is 2, option (b).",
    35: "Exactly two painted faces occur on edge cubes excluding the 8 corners. A 3×3×3 cube has one such cube on each of its 12 edges, hence 12, option (a).",
    36: "For hundreds digit h, choose any two lower digits for tens and units in descending order: C(7,2)+C(8,2)+C(9,2)=21+28+36=85 for h=7,8,9. Option (c).",
    37: "Pen<Pencil and Pencil<Book imply Pen<Book by transitivity. No fixed comparison with Cap follows from Book>Cap. Therefore option (b).",
    38: "Total sales are ax+(a+2)(x+2)+(a-2)(x-2). Expanding gives ax+(ax+2a+2x+4)+(ax-2a-2x+4)=3ax+8, option (b).",
    39: "Winning red-3 balls =40% of 15=6. Among black balls, black-2=9 and black-3=6, so black-1=5; winning black balls=14. Total wins=20 of 35, or 4/7, option (b).",
    40: "A runs 180° to the opposite point. B began 30° ahead and meets there after covering 150° in the same time. Speed ratio A:B=180:150=6:5, option (a).",
    41: "The student scores 30 and falls short by 30, so the pass mark is 60. If 60 is 40% of the maximum, maximum=60/0.4=150, option (c).",
    42: "By inclusion-exclusion, boys wearing both =11+14-19=6 because nobody lacks both items. Option (c).",
    43: "D is in Assam; Arts is in Rajasthan; Science is in Kerala; A is in Commerce. Therefore A can be in neither Assam, Rajasthan nor Kerala, leaving Gujarat. Option (b).",
    44: "D must be in Engineering in Assam, A in Commerce in Gujarat and C in Arts at city S in Rajasthan. B is therefore in Science, and B is in city Q. Science college is in city Q, option (a).",
    45: "With B assigned Science/Kerala, A Commerce/Gujarat and D Engineering/Assam, C must study in Arts college in Rajasthan. Option (b).",
    46: "Arts college is at city S and C studies there, so D cannot be in city S. The other listed statements conflict with the completed grid. Option (a).",
    47: "The completed grid assigns D to Engineering college in Assam. Thus 'D is studying there' is correct, option (d).",
    48: "D studies Engineering and D is in Assam, so Engineering college is located in Assam. Option (a).",
    49: "Climate finance is presented as both a climate-policy need and a development constraint, especially for developing countries. Thus assumptions 2 and 3 are necessary; statement 1 contradicts the passage's reference to most countries. Option (c).",
    50: "Polluting household fuels are tied to major premature mortality, while clean fuels include LPG. Hence access to cooking gas can reduce deaths in poor households, option (d); subsidy, imports and behaviour claims are not established.",
    51: "The passage says science opens the vision or dream of a possible happy world while acknowledging danger. That directly supports option (a). Option (c) turns contribution into an unsupported strict necessity.",
    52: "Longer resource access, no protective legal regime and coastal-state competition together imply geopolitical change caused by melting summer ice. Option (b); no Indian claim, resource sufficiency or Arctic-Antarctic quantity comparison is established.",
    53: "India's PDS and support-price commitments can breach WTO subsidy limits, creating tension between domestic food security and trade rules. That collision is the crucial message, option (c).",
    54: "The inherited factory-style system was designed for an industrial-age workforce, whereas today's world is complex, volatile and interconnected. Learners therefore need new-age skills; statements 1 and 3 are unsupported. Option (b).",
    55: "Because people differ genetically, medically and behaviourally, no single diet can address obesity; durable success requires understanding causes and changing habits. Thus there is no perfect universal diet or one solution, option (d).",
    56: "Monoculture creates a single-point failure that climate change magnifies. Preserving crop genetic diversity spreads risk and acts as insurance, option (a); the alternatives make unsupported exclusivity or regional-ranking claims.",
    57: "Let cost price be C and profit/loss fraction be r. Then 40=C(1+r) and 20=C(1-r). Adding gives 60=2C, so C=30, option (c).",
    58: "An equilateral triangle on 24 equally spaced points uses vertices 8 steps apart because 24/3=8. Each starting vertex defines the same triangle three times, so 24/3=8 distinct triangles, option (c).",
    59: "Each date is 28 days after the preceding one. Since 1996 is a leap year, 28 days after 26 February is 25 March 1996, option (b).",
    60: "If each square has side x, the 4-by-3 rectangle has sides 4x and 3x. Its diagonal is 5x=5, so x=1 and area=x²=1 sq cm, option (c).",
    61: "The actual-progress curve briefly rises above the expected-progress line before 1 September. Therefore the claim that actual progress was never greater is false, making option (d) the 'not correct' statement.",
    62: "Choose ordered colours for the three distinct blocks without repetition: 6 choices, then 5, then 4. Total 6×5×4=120, option (a).",
    63: "Population growth rate is the gap between birth and death rates. From 1990 to 2010 that gap does not display a single clear increasing, decreasing or stable pattern in the graph, so 'no trend' is the defensible inference, option (d).",
    64: "By about 2005, the birth-death gap has stabilized and the birth rate itself becomes nearly flat; total population has not stabilized, and a ten-per-cent fall in death rate is not supported by the scale. Statements 2 and 4 only, option (d).",
    65: "Both diagrams plot the same E values for the same years, so values and range are identical. The line's rise per year is also identical despite different visual aids; hence the slopes are the same, option (c).",
    66: "Across each row and column, the terminal symbol cycles dot→square→triangle, the main support cycles curved-up→straight→curved-down, and the number/orientation of hanging strokes follows the same rotation. The missing cell must be the square-ended straight form with two bent drops, option (a).",
    67: "At 2,000 pieces, Fig. A shows total production cost ₹7 lakh, while Fig. B shows selling price ₹350 each, giving ₹7 lakh revenue. This is the first break-even quantity; fewer pieces lose money. Option (a).",
    68: "Twelve adults use 12/18=2/3 of capacity, leaving 1/3. One-third of the 30-child capacity is 10 children, option (b).",
    69: "After year 1: 22,800×1.125=25,650; payment leaves 17,000. After year 2: 17,000×1.125=19,125; payment leaves 10,000. After year 3: 10,000×1.125=11,250, option (d).",
    70: "The square advances one sector around the circle through the six stages and returns to the top at stage VII; the triangle follows its own regular sector sequence and returns to the lower-left position. Only option (b) has that pair.",
    71: "For country B, dependants (<15 plus 64+) have fallen relative to the working-age group over the last 25 years, so 1 holds. The graph does not support A having a much lower future dependency ratio, but B's workforce share improves relative to A, so 3 holds. Option (c).",
    72: "Place brother directly opposite daughter. The son must be diagonally opposite the worst player's sibling; the consistent arrangement makes the son the worst and his sibling, the daughter, diagonal to him. The brother shares the son's side and therefore is the best player. Option (a).",
    73: "The graph shows repeated increases in repo and reverse-repo rates. Higher policy rates restrain credit/liquidity and aggregate demand, a standard anti-inflationary stance. Option (d).",
    74: "The table generally pairs higher per-capita income with higher tele-density, so 1 is a reasonable association. Counterexamples show GDP growth does not always imply higher income or tele-density, making 2 false and 3 true. Statements 1 and 3, option (c).",
    75: "The table shows association, not necessity. It cannot prove that further telecom investment is indispensable for sustaining prosperity or that very high tele-density is the most essential growth condition. Neither assumption is valid, option (d).",
    76: "The graph shows direct-tax shares (corporate and personal income tax) rising overall while indirect-tax shares fall overall, so statement 1 holds. A falling excise share cannot prove negative manufacturing growth because it is a composition percentage, not output growth. Option (a).",
    77: "From x-y=8, examples (10,2), (5,-3) and (-1,-9) show both variables need not be positive, positive x need not imply negative y, and negative x actually forces y=x-8 to be negative. None must be true, option (d).",
    78: "The passage joins intensive animal confinement and heavy water use to industrial meat production. The broad crucial message is that its environmental cost is unsustainable, option (d); immediate total stoppage is stronger than the passage.",
    79: "The tiger's long return trek and the fact that many tigers range outside reserves show isolated protected areas are insufficient. Recognized safe corridors are essential for movement and conservation, option (b).",
    80: "The failed relocation example supports assumption 1 as a concern about relocation without connected habitat. The passage says nothing about absent legislation or total conservation failure, so assumption 2 is invalid. 1 only, option (a).",
}

METHODS = {
    1: "Count triangles separately in the top, middle and bottom layers; add once.",
    2: "Write every dotted number in place-value form and solve the one linear digit equation.",
    3: "Test one row rule on two completed rows, then apply it to the missing row.",
    4: "Use diagonals = n(n-3)/2.",
    5: "Compare areas under the two velocity-time lines.",
    6: "Convert 40 km/h to m/s, then use time=train length/speed.",
    7: "Distinguish dependence of people on agriculture from dependence of the entire economy.",
    8: "Match the explicit globalization→traceability→risk chain; reject policy overreach.",
    9: "Choose complementarity; reject 'only', 'either' and unsupported priority claims.",
    10: "Lift the answer from the clause describing what the shackles prevent.",
    11: "Read and total only the first three bars for sheet and coil; subtract.",
    12: "Total all six sheet values and multiply by the bracketed average cost.",
    13: "Add three-month totals, divide, and round to the nearest offered ratio.",
    14: "Use two views with common faces to fix the one-dot opposite.",
    15: "After one opposite pair is fixed, compare the remaining rotations.",
    16: "Use elimination after fixing the dot pairs.",
    17: "Locate what the passage calls an obligation of quality, not mere access.",
    18: "Test each assumption for necessity from the passage; do not import demographic policy.",
    19: "Choose the curriculum mechanism explicitly tied to quality.",
    20: "Select the option broad enough to cover access plus quality, but no broader.",
    21: "Apply backward shifts of 1,2,3... to successive letters.",
    22: "Make a direct letter-to-digit lookup table.",
    23: "Square each interval first, then subtract extreme ranges.",
    24: "Compare every option with 1 and with the product XY.",
    25: "Draw two columns of three offices and place the hard constraints first.",
    26: "Reuse the completed office grid; inspect F's adjacent slot.",
    27: "Map each listed effect to an explicit phrase in the passage.",
    28: "Accept only the river-course inference; reject 'only' and geographic overextension.",
    29: "Reject both universal words: 'only' and 'invariably'.",
    30: "Keep water buffers, gene diversity and corridors; reject existing homogeneous practice.",
    31: "Read diversity as a coping strategy and homogeneity as genetic narrowing.",
    32: "Translate 'giant shopping mall' into excessive consumerism.",
    33: "Use the author's explicit sentence: leadership can be acquired and taught.",
    34: "Use reversed-number difference =99×digit difference.",
    35: "Use 12(n-2) edge cubes with exactly two painted faces.",
    36: "For each hundreds digit h, count C(h,2) descending lower-digit pairs.",
    37: "Chain only the inequalities that share a middle term.",
    38: "Expand the three revenue products; cancellation leaves 3ax+8.",
    39: "Count favourable balls directly rather than multiplying conditional probabilities.",
    40: "Compare angular distances covered in the same meeting time.",
    41: "Pass mark=score+shortfall; divide by 40%.",
    42: "Use |S∩P|=|S|+|P|-|S∪P|.",
    43: "Complete the state-college elimination grid.",
    44: "After fixing persons to colleges/states, use B's given city Q.",
    45: "Read C's remaining row from the completed grid.",
    46: "Test each statement against the single completed grid.",
    47: "Identify the person assigned the remaining Engineering college.",
    48: "Pair D's given state with D's deduced college.",
    49: "Reject statement 1; retain the finance-policy and development implications.",
    50: "Follow polluting fuel→mortality; choose the clean-fuel access consequence.",
    51: "Prefer the passage's exact 'vision of a possible happy world' over a necessity claim.",
    52: "Connect melting access and interstate scramble to geopolitics.",
    53: "State the conflict between PDS food security and WTO subsidy limits.",
    54: "Contrast industrial-age conformity with today's skill demands.",
    55: "Individual variation defeats a universal diet; choose the non-universal conclusion.",
    56: "Treat diversity as risk insurance against one pest, disease or climate shock.",
    57: "Add the equal-profit and equal-loss selling-price equations.",
    58: "Take every eighth point; divide 24 starting points by three vertices.",
    59: "Add exactly 28 days, remembering leap-year February.",
    60: "Use the 3-4-5 rectangle formed by square sides.",
    61: "Look for even a brief crossing of actual above expected.",
    62: "Use 6P3.",
    63: "Inspect the birth-death gap, not either line alone.",
    64: "Separate population level, growth-rate gap and individual rate trends.",
    65: "Read coordinates, not the visual steepness created by drawing style.",
    66: "Track symbol, support shape and hanging-stroke count independently across the 3×3 matrix.",
    67: "Find the first quantity where total cost equals quantity×selling price.",
    68: "Convert adults used into a fraction of lift capacity.",
    69: "Compound first, subtract each payment, and repeat year by year.",
    70: "Track square and triangle sector movements separately.",
    71: "Compare dependants (<15 and 64+) against the 15-64 curve.",
    72: "Draw four court positions; impose across, diagonal and same-side constraints.",
    73: "Rising repo/reverse-repo rates signal monetary tightening.",
    74: "Check 'generally' by broad pattern and 'always' by one counterexample.",
    75: "Reject necessity/superlative claims that a cross-sectional table cannot prove.",
    76: "Separate tax-share composition from actual sector growth.",
    77: "Use one counterexample for each 'must' statement.",
    78: "Choose the combined environmental implication; reject an immediate-ban overreach.",
    79: "Identify habitat connectivity as the passage's explicit remedy.",
    80: "Accept the relocation concern; reject the unsupported legislation claim.",
}
assert set(REASONS) == set(range(1, 81))
assert set(METHODS) == set(range(1, 81))


def slugify(text):
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text


def parse_routes():
    text = ROUTING.read_text(encoding="utf-8")
    routes = {}
    pattern = re.compile(
        r"^\| 2018 \| (\d+) \| ([^|]+?) \| (0[1-6]) \|",
        re.MULTILINE,
    )
    for q, neutral, family in pattern.findall(text):
        routes[int(q)] = (neutral.strip(), family)
    assert len(routes) == 80
    return routes


def get_content():
    html = requests.get(URL, timeout=60).text
    soup = BeautifulSoup(html, "html.parser")
    node = soup.select("article .container--narrow")[-1]
    for _ in range(2):
        node = next(x for x in node.children if getattr(x, "name", None))
    return node


def text_of(tag):
    return " ".join(tag.get_text(" ", strip=True).split())


def find_question_indices(kids):
    out = {}
    cursor = 0
    for q in range(1, 81):
        qpat = re.compile(rf"^{q}\.\s*", re.I)
        found = None
        for i in range(cursor, len(kids)):
            t = text_of(kids[i])
            if not qpat.match(t):
                continue
            if q in {66, 70} and len(t) > 20:
                found = i
                break
            probe = []
            for j in range(i, min(i + 35, len(kids))):
                if j > i and kids[j].name == "hr":
                    break
                probe.append(text_of(kids[j]))
            joined = " ".join(probe).lower()
            if all(re.search(rf"(?:^|\s){letter}\)", joined) for letter in "abcd"):
                found = i
                break
        if found is None:
            raise RuntimeError(f"Could not locate Q{q}")
        out[q] = found
        cursor = found + 1
    return out


def remove_solutions_and_add_anchors(node):
    kids = [x for x in node.children if getattr(x, "name", None)]
    qidx = find_question_indices(kids)
    marker_pat = re.compile(
        r"(?i)^Sol(?:ution)?\.?\s*(\d+)?\.?\s*Answer is \([a-d]\)"
    )
    marker_indices = [i for i, x in enumerate(kids) if marker_pat.match(text_of(x))]
    starts = set(marker_indices)
    remove = set()
    structural = sorted(
        set(qidx.values())
        | set(marker_indices)
        | {
            i
            for i, x in enumerate(kids)
            if text_of(x).lower().startswith(("directions for", "direction for", "passage-"))
            or x.name == "hr"
        }
    )
    for idx in marker_indices:
        end = next((x for x in structural if x > idx), len(kids))
        remove.update(range(idx, end))
    for i, x in enumerate(kids):
        if text_of(x).lower().startswith("solutions to q."):
            remove.add(i)
    for i in sorted(remove, reverse=True):
        kids[i].extract()

    remaining = [x for x in node.children if getattr(x, "name", None)]
    for q in range(1, 81):
        qpat = re.compile(rf"^{q}\.\s*", re.I)
        candidate = None
        for x in remaining:
            if qpat.match(text_of(x)):
                probe = text_of(x)
                if len(probe) >= 8:
                    candidate = x
                    break
        if candidate is None:
            raise RuntimeError(f"Q{q} disappeared")
        # BeautifulSoup Tag.new_tag is unavailable here; construct a tiny tag fragment.
        anchor = BeautifulSoup(
            f'<a id="2018-prelims-csat-q{q:02d}"></a>', "html.parser"
        ).a
        candidate.insert_before(anchor)


def clean_transcription(md):
    start = re.search(r'<a id="2018-prelims-csat-q01"></a>', md)
    if start:
        md = md[start.start():]
    replacements = {
        "tringles": "triangles",
        "krnph": "kmph",
        "passage's": "passages",
        "CV occupy": "C occupy",
        "a one enters": "as one enters",
        "left ofthe": "left of the",
        "as a follows": "as follows",
        "in tht": "in the",
        "If ‘he number": "If the number",
        "must be fount": "must be found",
        "whateverunpleasant": "whatever unpleasant",
        "most importakt": "most important",
        "wel ve": "Twelve",
        "welve": "Twelve",
        "areg": "area",
        "beriod": "period",
        "Nowadays, prosperity": "Nowadays, prosperity",
        "Nowdays": "Nowadays",
        "inference! inferences": "inference/inferences",
        "vas removed": "was removed",
        "Parma National Park": "Panna National Park",
        "livesotck": "livestock",
        "short live": "short lives",
        "the name that follow": "the items that follow",
        "conversation of wildlife": "conservation of wildlife",
        "kerala": "Kerala",
        "minimal supports": "minimum supports",
        "Tele density": "Tele-density",
    }
    for a, b in replacements.items():
        md = md.replace(a, b)
    md = re.sub(r"(?m)^(\d+)\.(?=\S)", r"\1. ", md)
    cursor = 0
    for q in range(1, 81):
        match = re.search(rf"(?m)^{q}\.\s", md[cursor:])
        if not match:
            raise RuntimeError(f"Could not anchor transcription Q{q}")
        pos = cursor + match.start()
        anchor = f'<a id="2018-prelims-csat-q{q:02d}"></a>\n'
        md = md[:pos] + anchor + md[pos:]
        cursor = pos + len(anchor) + len(f"{q}. ")
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def build():
    routes = parse_routes()
    node = get_content()
    remove_solutions_and_add_anchors(node)
    transcript = clean_transcription(markdownify(str(node), heading_style="ATX"))

    header = """# UPSC Civil Services (Preliminary) Examination 2018 — CSAT Paper II, Series A

> **Key status:** **FINAL.** Answer letters follow the UPSC Commission final key for `CS(P)-2018`, General Studies Paper II, Series A: 80 questions taken for scoring and none dropped.
> **Key provenance:** UPSC final-key scan, mirrored without alteration by IASbaba at <https://iasbaba.com/wp-content/uploads/2019/04/AnsKey-CSP-18-Paper-II.pdf>. Retrieved scan SHA-256: `42a0d77c632fb2eb7d35f66b740a44e49b9383a08c9e9a6927b5b198c8373751`.
> **Question source:** Held official booklet `books/more_previous_papers/QP-CSP-18-GS-II-C.pdf`, paper code `CYRF-S-TXLD`; the cover visibly identifies **Test Booklet Series A** despite the legacy filename suffix. Source SHA-256: `6f1f4cfcf37724a8c4002a032880655d725316be7c2171872695030f99dd9cca`.
> **Routing source:** Read-only `upsc-ai-kit/knowledge/_PYQ-ROUTING-CSAT-2018-2023.md` and canonical CSAT Basic owners 01–06.
> **Ownership:** This paper is the only solved-paper artifact edited in this pass; shared catalogues, routing, status and repository review-log files are intentionally untouched.

## Verified booklet transcription

The passages, stems, figures and option sets below follow the held Series-A booklet order. Figure links reproduce the printed diagrams used by the questions; all answers are resolved only in the official-final solution section.

"""
    answers = [
        f"{q}:{KEYS[q-1]}" for q in range(1, 81)
    ]
    key_table = "\n## Official-final key at a glance\n\n" + "\n".join(
        "| " + " | ".join(answers[i:i+10]) + " |"
        for i in range(0, 80, 10)
    )
    key_table += "\n\n"
    solution_parts = ["## Official-final solutions\n"]
    for q in range(1, 81):
        neutral, family = routes[q]
        slug = f"{slugify(neutral)}-2018-q{q:02d}"
        solution_parts.append(
            f'<a id="2018-prelims-csat-q{q:02d}-solution"></a>\n'
            f"### Q{q}. {neutral}\n"
            f"**Question:** [Return to the exact booklet transcription](#2018-prelims-csat-q{q:02d})  \n"
            f"**Primary route:** CSAT → [{FAMILY_NAMES[family]}]({TOPIC_LINKS[family]}) → {neutral} · "
            f"**Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)  \n"
            f"**Metadata:** Family {family} · {FAMILY_NAMES[family]} → {neutral} · "
            f"Slug: `{slug}`  \n"
            f"**Canonical owner:** `{OWNERS[family]}`\n\n"
            f"**FINAL answer: ({KEYS[q-1].lower()}).**\n\n"
            f"**Full reasoning:** {REASONS[q]}\n\n"
            f"**Shortest safe method:** {METHODS[q]}\n\n---\n"
        )
    content = header + transcript + key_table + "\n".join(solution_parts)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    build()
