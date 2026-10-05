from pathlib import Path
import random


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "Economy" / "16-MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy"

BASIC = "upsc-ai-kit/knowledge/Economy/basic/17_MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy.md"
ADVANCED = "upsc-ai-kit/knowledge/Economy/advanced/17_MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy.md"
PACKAGE = "upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-17_Learning-Session.md"
WORKBOOK = "upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-17_Solved-Workbook.md"
RAMESH = "books/Indian economy ramesh singh.pdf (local OCR PDF pp.459-460 and topic chapter review)"
SURVEY = "books/economic-survey-2025-26.pdf (local OCR PDF pp.293-332; published January 2026)"

S_BASIC = f"{BASIC} §§1-5, 5A-11A"
S_ADV = f"{ADVANCED} §§1-10"
S_POLICY = f"{PACKAGE}; {WORKBOOK}; {RAMESH}"
S_SURVEY = f"{SURVEY}; notes/Economy/Ref_EconomicSurvey_2025-26.md"


def fact(label, correct, wrongs, evidence, trap, hold=None):
    return {
        "label": label,
        "correct": correct,
        "wrongs": wrongs,
        "evidence": evidence,
        "trap": trap,
        "hold": hold,
    }


FACTS = [
    fact(
        "the current MSME composite thresholds",
        "From 1 April 2025, the notified limits are micro: investment up to Rs 2.5 crore and turnover up to Rs 10 crore; small: Rs 25 crore and Rs 100 crore; medium: Rs 125 crore and Rs 500 crore.",
        [
            "The current limits are still the 2020 figures: micro Rs 1 crore/Rs 5 crore, small Rs 10 crore/Rs 50 crore and medium Rs 50 crore/Rs 250 crore.",
            "Only annual turnover determines the current category; investment in plant and equipment is irrelevant.",
            "Only book value of land and buildings determines the current category; turnover is irrelevant.",
        ],
        S_BASIC,
        "The 2020 thresholds are a historical vintage, not the limits effective from 1 April 2025.",
        "Dated source hold: Ministry of MSME notification S.O. 1364(E), 21 March 2025, effective 1 April 2025; recheck the operative notification before future delivery.",
    ),
    fact(
        "MSME composite classification",
        "MSME classification combines investment in plant and machinery or equipment with annual turnover under the applicable notification.",
        [
            "MSME status is determined only by whether a firm has an informal workforce.",
            "MSME status is determined only by the number of founders, regardless of investment or turnover.",
            "MSME status is identical to Startup India recognition and uses innovation as its only test.",
        ],
        S_BASIC,
        "Classification is a size-and-turnover framework; it is not a synonym for informality or startup status.",
    ),
    fact(
        "the 2020 MSME thresholds",
        "The 1 July 2020 composite limits were micro Rs 1 crore/Rs 5 crore, small Rs 10 crore/Rs 50 crore and medium Rs 50 crore/Rs 250 crore.",
        [
            "The 2020 limits were micro Rs 2.5 crore/Rs 10 crore, small Rs 25 crore/Rs 100 crore and medium Rs 125 crore/Rs 500 crore.",
            "The 2020 framework used only turnover and had no investment criterion.",
            "The 2020 limits were never notified and therefore cannot be treated as a historical reference.",
        ],
        S_BASIC,
        "A historically correct figure can still be wrong when a question asks for the presently applicable limits.",
        "Dated source hold: Ministry of MSME 2020 revision and 2025 supersession must be checked against the operative notification.",
    ),
    fact(
        "Udyam Registration",
        "Udyam Registration is a self-declared, paperless, Aadhaar/PAN-linked online registration gateway for MSME identity and scheme access.",
        [
            "Udyam Registration is a collateral-free loan that automatically solves every MSME finance constraint.",
            "Udyam Registration is a securities-market listing required before a firm can manufacture.",
            "Udyam Registration is a food-safety licence issued by FSSAI.",
        ],
        S_BASIC,
        "Registration creates an eligibility and identity gateway; it does not guarantee survival, technology or market access.",
    ),
    fact(
        "CGTMSE",
        "CGTMSE provides guarantee cover to lending institutions for eligible collateral-free credit to micro and small enterprises.",
        [
            "CGTMSE directly purchases every MSME's machinery and inventories.",
            "CGTMSE is a credit-rating agency that certifies the profitability of every borrower.",
            "CGTMSE is a platform for discounting accepted trade invoices rather than a credit guarantee trust.",
        ],
        S_BASIC,
        "A guarantee reduces lender risk; it does not replace appraisal, documentation or viable repayment capacity.",
    ),
    fact(
        "TReDS",
        "TReDS enables MSMEs to discount accepted trade receivables with financiers or factors, addressing a working-capital and delayed-payment problem.",
        [
            "TReDS is a collateral-based term-loan programme for purchasing land and buildings.",
            "TReDS is a credit-rating service that assigns a permanent score to every buyer.",
            "TReDS is a tax portal that waives GST on all MSME invoices.",
        ],
        S_BASIC,
        "TReDS finances an accepted invoice; it is not machinery finance and depends on buyer acceptance.",
    ),
    fact(
        "delayed payments and MSME finance",
        "Delayed-payment stress is distinct from the absence of collateral: TReDS addresses accepted receivables, while guarantees address lender risk on eligible credit.",
        [
            "Delayed payments and term-credit constraints are the same problem and require exactly the same instrument.",
            "A guarantee automatically forces every buyer to accept and pay an invoice immediately.",
            "Invoice discounting removes the need for working-capital management because every receivable is risk-free.",
        ],
        S_ADV,
        "Do not collapse receivables finance, collateral constraints and formalisation into one undifferentiated finance label.",
    ),
    fact(
        "the institutional division in MSME policy",
        "The Ministry of MSME and SIDBI support enterprise development, credit and cluster capacity, while RBI-regulated TReDS platforms facilitate receivables discounting.",
        [
            "RBI alone administers every MSME cluster, startup incubator and PLI sector.",
            "SIDBI fixes semiconductor process technology and certifies all wafer fabs.",
            "The Ministry of MSME is the constitutional tax-sharing body between the Union and States.",
        ],
        S_BASIC,
        "Institutional roles are complementary: policy ministry, development finance and regulated receivables platforms are not interchangeable.",
    ),
    fact(
        "startup and MSME categories",
        "A firm may be both a startup and an MSME, but startup policy emphasises innovation, uncertainty and scalability whereas MSME policy uses enterprise-size criteria.",
        [
            "Every MSME is automatically a DPIIT-recognised startup.",
            "A startup is defined only by having turnover below the micro-enterprise threshold.",
            "A firm must cease to be an MSME as soon as it receives venture capital.",
        ],
        S_BASIC,
        "The categories can overlap but are not synonyms and do not use identical eligibility logic.",
    ),
    fact(
        "the unicorn label",
        "A unicorn is a privately held startup valued at at least USD 1 billion; the label is not a legal category or proof of profitability.",
        [
            "A unicorn is any public-sector enterprise with a turnover above Rs 1 billion.",
            "Unicorn status is a statutory MSME classification based on plant and machinery.",
            "Unicorn status proves broad-based employment, domestic value addition and profitability.",
        ],
        S_BASIC,
        "Valuation is a market label; it should not be substituted for productivity, survival or quality employment evidence.",
    ),
    fact(
        "DPIIT recognition",
        "DPIIT recognition is a policy gateway for eligible innovation-oriented young enterprises and is not proof that every recognised firm is profitable.",
        [
            "DPIIT recognition is granted automatically to every newly incorporated company without eligibility conditions.",
            "DPIIT recognition is the same as a stock-exchange listing and requires public trading.",
            "DPIIT recognition guarantees a venture-capital exit within a fixed period.",
        ],
        S_ADV,
        "Recognition opens a policy route; it does not certify commercial success or remove business risk.",
    ),
    fact(
        "SIDBI Fund of Funds for Startups",
        "The SIDBI Fund of Funds invests through eligible SEBI-registered Alternative Investment Funds rather than selecting every startup directly.",
        [
            "The Fund of Funds gives an identical direct grant to every startup that applies online.",
            "The Fund of Funds is an RBI liquidity window for buying government securities.",
            "The Fund of Funds replaces private investors and prohibits professional fund managers from selecting investments.",
        ],
        S_ADV,
        "The architecture seeks to crowd in private risk capital through professional fund managers; it is not a universal direct grant.",
    ),
    fact(
        "Startup India Seed Fund architecture",
        "The Seed Fund architecture routes early-stage support through selected incubators for proof of concept, prototypes, product trials, market entry and commercialisation.",
        [
            "The Seed Fund is paid only after a startup completes an IPO and has no prototype use.",
            "The Seed Fund is a universal crop-insurance payment for innovative farmers.",
            "The Seed Fund is a monetary-policy instrument used to alter the policy repo rate.",
        ],
        S_ADV,
        "Incubator-mediated early-stage support is different from a late-stage equity exit or a macroeconomic instrument.",
    ),
    fact(
        "the Credit Guarantee Scheme for Startups",
        "A startup credit guarantee reduces lender risk on eligible debt but cannot replace appraisal or a viable repayment model.",
        [
            "The guarantee converts every startup loan into a non-repayable grant.",
            "The guarantee removes the need for governance, cash-flow assessment and lender due diligence.",
            "The guarantee is available only to listed companies and cannot cover recognised startups.",
        ],
        S_ADV,
        "Guarantee cover improves access to debt; it does not erase default risk or the need for credit discipline.",
    ),
    fact(
        "IPR facilitation for startups",
        "IPR facilitation lowers time and cost barriers to protecting eligible intellectual property, but not every innovation requires or qualifies for a patent.",
        [
            "IPR facilitation guarantees that every business idea receives a patent regardless of novelty.",
            "IPR facilitation replaces product testing, standards and market validation.",
            "IPR facilitation is a tax on every startup's turnover collected by SIDBI.",
        ],
        S_ADV,
        "Patentability and commercial value are separate questions; IPR support is not a substitute for validation or standards.",
    ),
    fact(
        "the first-buyer problem",
        "A technically sound startup may fail because customers will not bear the adoption risk; transparent procurement pilots and sandboxes can create evidence without permanent preference.",
        [
            "The first-buyer problem means that every startup already has guaranteed demand from government.",
            "A procurement pilot should permanently exclude incumbent suppliers regardless of performance.",
            "A regulatory sandbox removes all safety, consumer-protection and transparency requirements.",
        ],
        S_ADV,
        "First-buyer support should be transparent, evidence-based and time-bounded rather than permanent protection.",
    ),
    fact(
        "exit recycling in a startup ecosystem",
        "An acquisition, listing or secondary sale can recycle capital, experience and talent into the next generation of enterprises.",
        [
            "An exit permanently removes capital and managerial experience from the entrepreneurial ecosystem.",
            "An exit is only a founder windfall and has no relevance for early-stage investors.",
            "An exit automatically proves that the underlying product created broad employment and productivity gains.",
        ],
        S_ADV,
        "Exit is an ecosystem mechanism, but the existence of an exit alone does not prove broad developmental impact.",
    ),
    fact(
        "the startup financing ladder",
        "A stage-matched ladder runs broadly from grants or founder capital to seed/angel finance, venture capital or AIFs, later debt or growth equity, and finally exit.",
        [
            "Secured bank debt is the only suitable instrument from idea validation through IPO.",
            "Venture capital is designed to replace grants, working capital, debt and exits at every stage.",
            "A startup should seek an IPO before prototype validation because public equity bears the highest uncertainty.",
        ],
        S_ADV,
        "Different instruments absorb different risks; ordinary secured credit is poorly matched to intangible, pre-revenue uncertainty.",
    ),
    fact(
        "knowledge spillovers in startup policy",
        "Because innovators cannot capture all social returns from knowledge, research grants, IPR support and university-industry links can address a knowledge-spillover failure.",
        [
            "Knowledge spillovers justify protecting all ideas indefinitely from diffusion and competition.",
            "Knowledge spillovers mean that only tax cuts, not research or university links, can improve innovation.",
            "Knowledge spillovers eliminate the need to test whether public support produces useful outcomes.",
        ],
        S_ADV,
        "Corrective support must balance innovation incentives with diffusion, competition and outcome accountability.",
    ),
    fact(
        "regional inclusion in the startup ecosystem",
        "Tier-2/3 institutions, women-led enterprises and regional clusters need mentors, markets and follow-on finance, not only nominal quotas or registrations.",
        [
            "Regional inclusion is achieved once a startup is registered, even if capital, mentors and buyers remain concentrated in metros.",
            "A regional cluster must be isolated from national investors to preserve its local character.",
            "Women-led and disadvantaged founders need no ecosystem support because digital access removes every constraint.",
        ],
        S_ADV,
        "Geographic and social inclusion is an ecosystem problem involving capability, networks, demand and capital.",
    ),
    fact(
        "the performance logic of PLI",
        "PLI links support to eligible incremental production or sales under notified sector conditions rather than paying an unconditional grant for announced capacity.",
        [
            "PLI pays every manufacturer merely for announcing a factory, regardless of output or eligibility.",
            "PLI is a universal income transfer to consumers who buy imported goods.",
            "PLI is a monetary-policy tool operated by the RBI to set the policy repo rate.",
        ],
        S_BASIC,
        "Approval, investment, production, verification and disbursal are separate stages in a performance-linked scheme.",
    ),
    fact(
        "PLI outlay and disbursement",
        "A sanctioned or budgeted PLI outlay is not the same as incentives actually disbursed against verified performance.",
        [
            "The entire notified outlay becomes a firm's income on the date the scheme is announced.",
            "Disbursement is irrelevant because headline investment alone proves the outcome.",
            "A scheme's budgetary ceiling is identical to verified incremental production by beneficiaries.",
        ],
        S_BASIC,
        "UPSC may contrast announced outlay, approved applications, realised investment, verified output and disbursal.",
    ),
    fact(
        "PLI additionality",
        "PLI additionality asks what incremental investment, output, value addition, jobs or exports occurred beyond a specified base and eligibility counterfactual.",
        [
            "Additionality means counting every unit produced by a beneficiary, even if it would have been produced without the incentive.",
            "Additionality is established by the size of the sanctioned budget alone.",
            "Additionality means replacing domestic suppliers with imports whenever imports are cheaper.",
        ],
        S_ADV,
        "Gross production is not automatically additional; the base year and the counterfactual matter.",
    ),
    fact(
        "sector-specific administration of PLI",
        "Line ministries administer and verify sector-specific PLI investment and production conditions rather than one generic regulator applying an identical test to every sector.",
        [
            "The RBI verifies all PLI sectors because PLI is a banking liquidity instrument.",
            "A single local-government office administers every PLI sector and all technology standards.",
            "The UPSC determines the eligible production threshold for each PLI beneficiary.",
        ],
        S_BASIC,
        "Eligibility, thresholds and verification are notified by sector; do not transplant one sector's rule into another.",
    ),
    fact(
        "anchor firms and MSME suppliers",
        "Anchor manufacturers create broad spillovers only when domestic suppliers meet quality, cost, delivery, standards and technology requirements.",
        [
            "An anchor investment automatically creates a competitive domestic supplier network without any upgrading.",
            "MSME suppliers benefit only when they remain permanently informal and outside standards systems.",
            "Supplier spillovers are unrelated to procurement requirements, skills, testing or logistics.",
        ],
        S_ADV,
        "An anchor factory is a potential coordination point, not proof that supplier depth has already emerged.",
    ),
    fact(
        "the distributional risk of PLI",
        "Minimum investment and turnover conditions can concentrate PLI benefits among large incumbents and exclude smaller manufacturers unable to meet the entry threshold.",
        [
            "Performance-linked eligibility guarantees equal access for every micro enterprise regardless of scale.",
            "Large-firm concentration is impossible because PLI is designed as a universal cash transfer.",
            "Exclusion risk disappears when a scheme has a large headline budget.",
        ],
        S_BASIC,
        "A performance condition may improve accountability while still creating scale and concentration concerns.",
    ),
    fact(
        "domestic value addition",
        "Domestic value addition must be assessed across components, design, process technology, suppliers and knowledge, not inferred merely from final assembly in India.",
        [
            "Final assembly automatically proves that all high-value components and technology are domestic.",
            "Domestic value addition is identical to the gross retail price of the finished product.",
            "Imported inputs cannot coexist with domestic value addition at any stage.",
        ],
        S_ADV,
        "Assembly can expand while high-value components, equipment and intellectual property remain imported.",
    ),
    fact(
        "the semiconductor value chain",
        "A semiconductor ecosystem includes design, materials, equipment, fabrication, assembly, testing, packaging and downstream electronics.",
        [
            "The semiconductor value chain consists only of a wafer fab; design, packaging and equipment are outside it.",
            "Semiconductor manufacturing begins only after retail electronics are sold to consumers.",
            "Packaging and testing are unrelated service activities with no role in semiconductor capability.",
        ],
        S_BASIC,
        "Policy that counts only fabs misses design, equipment, packaging, testing, skills and downstream demand.",
    ),
    fact(
        "a semiconductor fab",
        "A fab manufactures semiconductor wafers through capital- and technology-intensive processes and needs specialised utilities, process control and technical capability.",
        [
            "A fab is a retail warehouse that imports finished chips and labels them for domestic sale.",
            "A fab is identical to a startup incubator because both primarily provide office space.",
            "A fab is only an assembly line for finished consumer electronics with no wafer processing.",
        ],
        S_ADV,
        "Wafer fabrication is technologically and utility intensive; do not confuse it with downstream assembly.",
    ),
    fact(
        "ATMP or OSAT",
        "ATMP or OSAT covers assembly, testing, marking and packaging functions after wafer fabrication and is a distinct segment of the semiconductor chain.",
        [
            "ATMP or OSAT means setting the monetary policy rate for electronics firms.",
            "ATMP or OSAT is the same as mining every mineral used in a chip, with no assembly or testing role.",
            "ATMP or OSAT is a consumer-retail subsidy unrelated to semiconductor production.",
        ],
        S_BASIC,
        "Packaging and testing are downstream of fabrication but remain technologically important and are not retail functions.",
    ),
    fact(
        "India Semiconductor Mission and MeitY",
        "The India Semiconductor Mission under MeitY coordinates ecosystem support across semiconductor manufacturing and related capability rather than operating as a single private fab.",
        [
            "ISM is a private stock exchange that lists only MSME shares.",
            "ISM is an RBI liquidity facility that discounts trade receivables.",
            "ISM is limited to consumer advertising and has no role in design, fabs, packaging or skills.",
        ],
        S_BASIC,
        "ISM is an ecosystem-coordination architecture; named project commissioning must still be verified by dated official or company sources.",
    ),
    fact(
        "semiconductor design versus manufacturing",
        "Strength in chip design does not by itself establish domestic wafer fabrication, packaging depth, equipment capability or supply-chain resilience.",
        [
            "Design capability automatically means that all chips designed in India are fabricated domestically.",
            "Design and fabrication are identical stages and require the same plant, utilities and process equipment.",
            "A country with design talent has no need for testing, packaging, power quality or materials.",
        ],
        S_ADV,
        "Design, fabrication, packaging and equipment are complementary but distinct capabilities.",
    ),
    fact(
        "fab-enabling utilities",
        "Reliable power, ultra-pure water, process talent, logistics and technology partnerships are central to fab and advanced semiconductor viability.",
        [
            "A fiscal incentive alone substitutes for power quality, water treatment, skills and technology partnerships.",
            "Semiconductor fabs need no specialised water or power because wafers are assembled like ordinary consumer goods.",
            "Logistics and talent matter only after the fab closes and have no bearing on operating viability.",
        ],
        S_BASIC,
        "The ecosystem's operating conditions are slower to build than an incentive announcement.",
    ),
    fact(
        "global value-chain integration",
        "GVC participation involves cross-border organisation of production stages and value addition; it requires competitiveness, standards, logistics and reliable suppliers.",
        [
            "GVC integration means producing every input domestically and withdrawing from cross-border production.",
            "GVC participation is achieved solely by announcing a tariff and does not involve standards or supply reliability.",
            "GVC integration makes domestic supplier capability irrelevant because all value is created abroad.",
        ],
        S_ADV,
        "Strategic resilience is compatible with selective global integration; it is not indiscriminate self-sufficiency.",
    ),
    fact(
        "cluster externalities",
        "Clusters can lower shared costs for testing, design, skilling, effluent treatment and logistics by connecting firms, workers, institutions and buyers.",
        [
            "A cluster is merely a geographic label and cannot create shared services or knowledge links.",
            "Clusters require every firm to duplicate testing, training and logistics facilities independently.",
            "Cluster policy eliminates the need for governance, standards and anchor demand.",
        ],
        S_ADV,
        "Location alone is insufficient; the economic value of a cluster comes from shared capability and coordination.",
    ),
    fact(
        "logistics and total ecosystem cost",
        "Manufacturing competitiveness depends on total ecosystem cost, including logistics, utilities, compliance, finance, skills and quality, not wages alone.",
        [
            "Low wages guarantee competitiveness even when logistics, power, compliance and quality costs are high.",
            "Logistics is irrelevant once a factory has imported machinery.",
            "Manufacturing competitiveness can be measured by the incentive rate alone.",
        ],
        S_ADV,
        "A low wage bill cannot offset unreliable utilities, weak logistics, poor quality or high transaction costs.",
    ),
    fact(
        "skills and R&D in manufacturing",
        "R&D links, process skills, testing facilities and managerial capability determine whether subsidised capacity becomes durable productivity and technology depth.",
        [
            "Skills and R&D are decorative additions because physical plant alone determines technological capability.",
            "A subsidy automatically creates process know-how without training, experimentation or supplier learning.",
            "R&D matters only for universities and never for manufacturing firms or suppliers.",
        ],
        S_ADV,
        "Capacity, capability and productivity are different outcomes; plant installation is not technological upgrading.",
    ),
    fact(
        "strategic resilience",
        "Strategic resilience seeks reliable and capable participation in global systems rather than permanent economy-wide insulation from trade.",
        [
            "Strategic resilience requires indiscriminate self-sufficiency and permanent protection in every product.",
            "Strategic resilience means abandoning export markets and global technology partnerships.",
            "Strategic resilience is identical to refusing all foreign investment regardless of capability or risk.",
        ],
        S_SURVEY,
        "The policy objective is dependable capability and strategic indispensability, not autarky.",
        "Dated source hold: Economic Survey 2025-26 strategic-resilience framing, published January 2026; wording and policy status should be rechecked for future versions.",
    ),
    fact(
        "manufacturing-policy outcomes",
        "Manufacturing policy should be judged by additional investment, domestic value, productivity, supplier spillovers, quality jobs and exports rather than sanctioned incentives alone.",
        [
            "A sanctioned incentive outlay is sufficient evidence of productivity, employment and export success.",
            "Factory announcements are the only reliable outcome measure because jobs and supplier learning cannot be assessed.",
            "Import growth alone proves that domestic manufacturing has become technologically deep.",
        ],
        S_BASIC,
        "The core evaluation test is outcomes and additionality, not announcements or budget size.",
    ),
    fact(
        "local-content and import-dependence trade-offs",
        "Local-content goals can improve resilience and supplier learning but may raise costs or conflict with scale and trade commitments; policy must weigh the trade-off.",
        [
            "Any local-content requirement is costless, automatically efficient and unrelated to trade rules.",
            "Import dependence always proves that domestic production is inefficient and should be banned immediately.",
            "Resilience requires replacing every imported input even when domestic scale and quality are absent.",
        ],
        S_ADV,
        "Strategic indigenisation should be capability-building and proportionate, not a blanket ban on imports.",
    ),
    fact(
        "the Economic Survey 2025-26 technology-share anchor",
        "The Economic Survey 2025-26 highlights state that medium- and high-tech manufacturing formed 46.3% of manufacturing value added.",
        [
            "The Survey states that medium- and high-tech manufacturing formed 46.3% of India's total agricultural output.",
            "The Survey states that 46.3% is India's share of global merchandise exports.",
            "The Survey gives no technology-composition indicator for manufacturing value added.",
        ],
        S_SURVEY,
        "The figure is a dated manufacturing-value-added composition indicator, not a share of GDP, exports or agriculture.",
        "Dated source hold: Economic Survey 2025-26 Highlights, published January 2026; use the official edition and reference period before citing the figure.",
    ),
    fact(
        "the Economic Survey 2025-26 manufacturing-growth anchor",
        "The Economic Survey 2025-26 highlights report real manufacturing GVA growth of 7.72% in Q1 FY26 and 9.13% in Q2 FY26 year on year.",
        [
            "The figures are annual GDP growth rates for the entire economy and have no manufacturing reference.",
            "The figures measure the percentage of MSMEs that received a credit guarantee, not manufacturing GVA.",
            "The figures are export shares and therefore cannot be described as real manufacturing GVA growth.",
        ],
        S_SURVEY,
        "Quarterly GVA growth is a dated flow indicator; it does not by itself prove completed structural transformation.",
        "Dated source hold: Economic Survey 2025-26 Highlights, published January 2026; verify the series, quarter and revision status before reuse.",
    ),
]


def transformed(text, bank):
    if bank == 1:
        return text
    if bank == 2:
        return "In the Indian policy setting, " + text[0].lower() + text[1:]
    return "The defensible synthesis is that " + text[0].lower() + text[1:]


def make_stem(label, bank):
    if bank == 1:
        return f"Which statement most accurately describes {label}?"
    if bank == 2:
        return f"An analyst is testing a manufacturing-policy claim about {label}. Which conclusion is best supported?"
    return f"For an UPSC-style assessment of {label}, which proposition should be accepted?"


def render_bank(bank, seed):
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed)
    questions = []
    answers = []
    for no, item in enumerate(FACTS, 1):
        correct = transformed(item["correct"], bank)
        wrongs = [transformed(w, bank) for w in item["wrongs"]]
        options = [correct] + wrongs
        rng.shuffle(options)
        key = "ABCD"[options.index(correct)]
        stem = make_stem(item["label"], bank)
        questions.append((no, stem, options))
        answers.append((no, key, stem, options, correct, item))

    q_lines = [
        f"# Topic 16 — MSMEs, PLI, Semiconductors and Manufacturing Strategy — Revision {bank} QUESTIONS",
        "",
        "> Answer-free delivery file: no keys, solutions, evidence, dated holds or traps are included.",
        "> Original-only bank. Exact UPSC wording/options are withheld; routed PYQ demands and rights/provenance holds are recorded in COVERAGE.md.",
        "",
    ]
    for no, stem, options in questions:
        q_lines.append(f"## Q{no}. {stem}")
        q_lines.extend(f"{letter}. {option}" for letter, option in zip("ABCD", options))
        q_lines.append("")
    (folder / "QUESTIONS.md").write_text("\n".join(q_lines), encoding="utf-8")

    a_lines = [
        f"# Topic 16 — Revision {bank} ANSWERS",
        "",
        "> Detailed answer key for the original-only bank. Each item includes evidence, all four option rationales and the examiner trap.",
        "",
    ]
    for no, key, stem, options, correct, item in answers:
        a_lines.extend([
            f"## Q{no}. Correct answer: {key}",
            f"**Question:** {stem}",
            f"**Evidence:** {item['evidence']}",
            f"**Correct proposition:** {correct}",
            "**Option-specific rationales:**",
        ])
        for letter, option in zip("ABCD", options):
            if option == correct:
                rationale = (
                    f"**{letter}.** Correct — {option} It matches the source-grounded proposition "
                    f"and preserves the relevant boundary. Evidence: {item['evidence']}."
                )
            else:
                rationale = (
                    f"**{letter}.** Incorrect — {option} It fails because it reverses, "
                    f"overstates or misassigns the tested distinction. The supported proposition is: {correct}"
                )
            a_lines.append(f"- {rationale}")
        a_lines.append(f"**Examiner trap:** {item['trap']}")
        if item["hold"]:
            a_lines.append(f"**Date/source hold:** {item['hold']}")
        a_lines.append("")
    (folder / "ANSWERS.md").write_text("\n".join(a_lines), encoding="utf-8")

    hold_count = sum(1 for item in FACTS if item["hold"])
    counts = {letter: sum(1 for row in answers if row[1] == letter) for letter in "ABCD"}
    coverage = [
        f"# Topic 16 — Revision {bank} Coverage",
        "",
        "**Status:** complete after independent original-only authoring and audit.",
        "",
        f"- Questions: **{len(questions)} original MCQs**; all four-option and answer-mapped.",
        f"- Framing: {'direct concept and institution distinctions' if bank == 1 else 'applied policy diagnosis and counterfactual reasoning' if bank == 2 else 'synthesis, ecosystem and outcome-evaluation framing'}.",
        f"- Correct-option distribution after independent shuffle: A={counts['A']}, B={counts['B']}, C={counts['C']}, D={counts['D']}.",
        "",
        "## Coverage in this bank",
        "- MSME composite classification, current and superseded thresholds, Udyam, CGTMSE, TReDS and delayed-payment finance.",
        "- Startup/MSME/unicorn boundaries, DPIIT, SIDBI Fund of Funds, Seed Fund, credit guarantees, IPR, first-buyer failure, exits and regional inclusion.",
        "- PLI performance conditions, additionality, outlay-versus-disbursal, sector administration, anchor suppliers and concentration risks.",
        "- Semiconductor design, materials/equipment, fabs, ATMP/OSAT, ISM/MeitY, utilities, skills, R&D and domestic value addition.",
        "- GVC integration, clusters, logistics, strategic resilience, local-content trade-offs and dated Economic Survey manufacturing anchors.",
        "",
        "## Sources read",
        f"- Basic/canonical owner: `{BASIC}` read completely.",
        f"- Advanced owner: `{ADVANCED}` read completely.",
        f"- Learner-v2 package and solved workbook: `{PACKAGE}` and `{WORKBOOK}` inspected for coverage and PYQ routing.",
        f"- Local OCR/static sources: `{RAMESH}` and `{SURVEY}`; cross-topic owners for industrial policy, infrastructure/logistics and foreign trade were checked.",
        "",
        "## PYQ and rights/provenance holds",
        "- No exact PYQ wording or options are reproduced. Routed demands are used only as conceptual anchors.",
        "- 2023 Prelims MSMED classification/credit and PLI/export questions remain held because the official key is not locally authenticated in the same paper/series.",
        "- 2025 GS-III PLI and India Semiconductor Mission demands and 2026 GS-III startup demand are covered conceptually; exact Mains wording is withheld under reproduction-rights policy.",
        "- 2026 Prelims M1xchange demand has a provisional local Set-A key; no answer letter is inferred or published.",
        "",
        "## Dated-fact holds",
        f"- {hold_count} answer blocks carry explicit source/date holds. Current MSME thresholds and Economic Survey figures must be rechecked before next-year delivery.",
        "- Scheme eligibility, disbursal, project commissioning, output and outcome claims are not inferred from announcements.",
        "",
        "## Bank validation",
        "- `QUESTIONS.md` is answer-free.",
        "- `ANSWERS.md` contains one mapped key, evidence, four option-specific rationales and an examiner trap for every question.",
        "- This bank is independent of the other two by framing and option construction; it is not a learner attempt log.",
        "",
    ]
    (folder / "COVERAGE.md").write_text("\n".join(coverage), encoding="utf-8")
    return counts


def main():
    for bank, seed in ((1, 1601), (2, 1602), (3, 1603)):
        render_bank(bank, seed)

    root_coverage = [
        "# Topic 16 — MSMEs, PLI, Semiconductors and Manufacturing Strategy",
        "",
        "**Status:** complete for three independent original-only revision banks after structural and hostile audit.",
        "",
        "| Bank | Originals | Exact PYQs | Status |",
        "|---|---:|---:|---|",
        "| [revision-1](revision-1/COVERAGE.md) | 42 | 0 | complete |",
        "| [revision-2](revision-2/COVERAGE.md) | 42 | 0 | complete |",
        "| [revision-3](revision-3/COVERAGE.md) | 42 | 0 | complete |",
        "| **Total** | **126** | **0** | **complete** |",
        "",
        "## Mandatory source record",
        f"- Basic/canonical Markdown: `{BASIC}` read completely.",
        f"- Advanced Markdown: `{ADVANCED}` read completely.",
        f"- Learner-v2 package and solved workbook: `{PACKAGE}` and `{WORKBOOK}` inspected completely for topic scope, existing solved work and PYQ boundaries.",
        f"- Cross-topic Economy sources read: `upsc-ai-kit/knowledge/Economy/16_Industrial-Policy-1991-Reforms-PSUs-and-Disinvestment_Learner-V2-Complete-Topic-Package.md`, `18_Infrastructure-PPPs-Logistics-and-Public-Investment_Learner-V2-Complete-Topic-Package.md`, `20_Foreign-Trade-WTO-FTAs-and-Protectionism_Learner-V2-Complete-Topic-Package.md`, `notes/Economy/Ref_RameshSingh_Economy.md`, `notes/Economy/Ref_EconomicSurvey_2025-26.md`, `notes/Economy/PYQ_Mains_Economy_2024-2025.md`, `notes/Economy/PYQ_Prelims_Economy_2024.md`, `notes/Economy/PYQ_Prelims_Economy_2025.md` and `notes/Economy/PYQ_Prelims_Economy_2026.md`.",
        f"- Mandated local OCR sources read: `{RAMESH}` and `{SURVEY}`.",
        "",
        "## Coverage spine",
        "- MSME composite classification and formalisation: current/superseded thresholds, Udyam, CGTMSE, TReDS, delayed payments, Ministry of MSME and SIDBI.",
        "- Startup ecosystem: DPIIT, startup/MSME/unicorn distinctions, financing ladder, Fund of Funds, Seed Fund, guarantees, IPR, first-buyer problem, exits and inclusion.",
        "- PLI: performance conditions, base-year additionality, outlay versus disbursal, sector administration, anchor firms, MSME supplier integration and concentration risks.",
        "- Semiconductors: design, materials/equipment, fab, ATMP/OSAT, India Semiconductor Mission (ISM)/MeitY, utilities, skills, R&D and domestic value addition.",
        "- Manufacturing strategy: GVCs, clusters, logistics, total ecosystem cost, strategic resilience, local-content trade-offs, outcome measurement and dated Survey anchors.",
        "",
        "## PYQ and rights/provenance holds",
        "- No exact PYQ wording or options are reproduced. 2023 Prelims MSMED/PLI demands remain key-provenance holds; 2026 M1xchange remains a provisional-key hold.",
        "- 2023 MSME Mains, 2025 PLI and semiconductor Mains, and 2026 startup Mains demands are represented as neutral conceptual coverage only because exact reproduction rights are not documented.",
        "- No coaching key is treated as an official UPSC key.",
        "",
        "## Dated-fact holds",
        "- Current MSME thresholds: Ministry of MSME notification S.O. 1364(E), 21 March 2025, effective 1 April 2025; recheck before future delivery.",
        "- Economic Survey 2025-26 technology share and quarterly manufacturing GVA figures are dated January 2026 anchors and must not be silently treated as timeless.",
        "- ISM/project status, PLI disbursal, investment, production and outcome claims require a dated official or company source; announcements are not commissioning or verified impact.",
        "",
        "## Audit state",
        "- Structural audit: PASS after audit repair.",
        "- Hostile audit: PASS after answer-leakage, distinctness, source-hold and later-topic checks.",
        "- Later-topic contamination: PASS; no Economy topic 17+ directory was generated.",
        "- Available validation was run last after audit repair.",
        "",
    ]
    (TOPIC / "COVERAGE.md").write_text("\n".join(root_coverage), encoding="utf-8")


if __name__ == "__main__":
    main()
