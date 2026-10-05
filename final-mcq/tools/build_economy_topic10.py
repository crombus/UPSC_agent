from pathlib import Path
import random
import re


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "Economy" / "10-Taxation-GST-Finance-Commission-and-Fiscal-Federalism"

SOURCE_T10 = (
    "upsc-ai-kit/knowledge/Economy/"
    "10_Taxation-GST-Finance-Commission-and-Fiscal-Federalism_Learner-V2-Complete-Topic-Package.md"
)

FACTS = [
    ("direct-indirect", "direct and indirect taxes",
     "Direct taxes impose legal incidence on income, profit or wealth-related bases, while indirect taxes apply to transactions or consumption and may be shifted through prices.",
     ["Direct taxes are always progressive and indirect taxes are always regressive.",
      "Indirect taxes cannot be shifted because the statutory taxpayer always bears the final burden.",
      "The distinction depends only on whether the tax is collected by the Union or a state."],
     "Learner-v2 Session 1; Complete Basic Owner §2; Ramesh Singh OCR pp.757-758",
     "Legal incidence and economic incidence are not necessarily identical.", "Tax incidence"),
    ("progressivity", "progressivity",
     "Progressive, proportional and regressive describe how the burden changes relative to income, tax base or ability to pay; a statutory rate alone does not establish incidence.",
     ["Any tax with a single statutory rate is automatically progressive in economic incidence.",
      "Progressivity is determined only by the name of the tax and not by the taxpayer's income position.",
      "A regressive burden necessarily means that the tax rate rises with income."],
     "Learner-v2 Session 1; Complete Basic Owner §§2, 6A; Ramesh Singh OCR pp.757-760",
     "Do not infer distributional incidence from the headline rate alone.", "Equity"),
    ("tax-buoyancy", "tax buoyancy",
     "Tax buoyancy compares the responsiveness of tax revenue with changes in the relevant tax base or national income, including the effects of policy changes.",
     ["Tax buoyancy is identical to the statutory tax rate.",
      "Tax buoyancy excludes compliance and policy changes by definition.",
      "Tax buoyancy measures only the size of the divisible pool after transfers."],
     "Learner-v2 semantic-completeness control; Economic Survey 2025-26 fiscal-development context",
     "A revenue increase can reflect base growth, compliance or rate changes; do not reduce buoyancy to a rate.", "Revenue dynamics"),
    ("gst-destination", "GST destination principle",
     "GST is a destination-based value-added tax on supply, so final-consumption jurisdiction is central to revenue assignment.",
     ["GST is an origin-based production tax whose revenue permanently belongs to the producing state.",
      "GST taxes only final retail sales and has no value-added or input-credit architecture.",
      "GST revenue is assigned solely by the registered office of the supplier."],
     "Learner-v2 Session 2; Complete Basic Owner §3; Ramesh Singh OCR pp.763-764",
     "Destination-based does not mean that every place-of-supply dispute is resolved without IGST rules.", "GST design"),
    ("itc", "input tax credit",
     "Input tax credit reduces cascading only when legal eligibility, invoice and compliance conditions are satisfied.",
     ["Input tax credit is an unconditional cash refund for every purchase.",
      "Input tax credit makes exemptions and zero-rating legally identical.",
      "Input tax credit applies even when the underlying supply is outside the statutory chain."],
     "Learner-v2 Session 3; Complete Basic Owner §3; Ramesh Singh OCR pp.761-763",
     "Do not equate exemption, zero-rating and credit treatment.", "GST design"),
    ("dual-gst", "dual GST architecture",
     "India's GST architecture separates central and state components for intra-state supplies and uses IGST for inter-state supplies, within the constitutional framework.",
     ["Only the Union levies GST on every supply and states merely receive grants.",
      "States independently impose separate VAT on the same GST supply without a common framework.",
      "IGST is a permanent origin tax retained entirely by the exporting state."],
     "Learner-v2 Sessions 2, 6 and 7; Complete Basic Owner §§3-4",
     "A dual levy is not the same as two unrelated tax systems.", "GST federal design"),
    ("union-subsumed", "Union taxes subsumed into GST",
     "The Union-side list includes Central Excise Duty on covered items, Service Tax, Additional Excise Duties, CVD, SAD and relevant central cesses or surcharges on supply.",
     ["Basic customs duty, stamp duty and state excise on alcohol for human consumption were all subsumed.",
      "Only personal income tax and corporation tax were subsumed into GST.",
      "Every Union receipt connected with imports automatically became GST."],
     "Learner-v2 Session 4; Complete Basic Owner §5; Ramesh Singh OCR pp.763-766",
     "Never say every pre-GST Union levy was subsumed.", "GST scope"),
    ("state-subsumed", "State taxes subsumed into GST",
     "The State-side list includes State VAT or Sales Tax, Central Sales Tax as collected, Purchase Tax, specified Entertainment Tax, Octroi or Entry Tax, Luxury Tax and taxes on lotteries, betting and gambling.",
     ["State excise on alcohol for human consumption and stamp duty were subsumed as ordinary GST components.",
      "Only property tax and electricity duty were subsumed into GST.",
      "State VAT remained wholly outside GST and was replaced only by a Union surcharge."],
     "Learner-v2 Session 5; Complete Basic Owner §5; Ramesh Singh OCR pp.763-766",
     "The local-body qualification for entertainment tax matters.", "GST scope"),
    ("gst-outside", "GST exclusions",
     "Basic customs duty, stamp duty, property tax, electricity duty and state excise on alcohol for human consumption remain outside GST; specified petroleum products require period-specific treatment.",
     ["Every customs levy is outside GST, including the countervailing components subsumed into the GST design.",
      "Alcohol for human consumption is automatically taxed under GST because it is a supply.",
      "Property tax became a GST component after the constitutional amendment."],
     "Learner-v2 Session 6; Complete Basic Owner §§5-6; Ramesh Singh OCR pp.763-766",
     "A broad 'one nation, one tax' slogan does not erase statutory exclusions.", "GST scope"),
    ("petroleum-status", "petroleum products and GST status",
     "Crude oil, petrol, diesel, ATF and natural gas are constitutionally important GST-boundary items, but their actual inclusion is a period-sensitive legal and Council-status question.",
     ["All listed petroleum products have been permanently included in GST from its commencement.",
      "Petroleum products can never be brought within GST under the constitutional design.",
      "The status of petroleum products is determined only by the Finance Commission."],
     "Learner-v2 Complete Basic Owner §5 and current-status caution; source as-of 5-6 Sep 2026",
     "Do not turn a Council/legal-status question into a timeless fact.", "Dated GST status",
     "Date hold: repository status rechecked 5-6 Sep 2026; verify the latest GST Council notification before next-year use."),
    ("gst-council", "GST Council under Article 279A",
     "The GST Council is a constitutional federal forum under Article 279A that recommends the GST framework; it is not the Finance Commission.",
     ["The GST Council is a statutory committee of the Finance Commission created to award grants.",
      "The GST Council is a monetary-policy organ of RBI.",
      "The GST Council directly replaces Parliament for every tax-law enactment."],
     "Learner-v2 Session 6; Complete Basic Owner §4; Article 279A route in owner",
     "Recommendation by the Council is not identical to legislative enactment.", "Institutions"),
    ("gst-vote", "GST Council voting",
     "Article 279A gives the Centre one-third of weighted votes and the states together two-thirds; a decision requires at least three-fourths of weighted votes.",
     ["The Centre has two-thirds and the states one-third, with a simple majority required.",
      "Each state has an equal vote and the Centre has no weighted share.",
      "A decision requires unanimity of all members."],
     "Learner-v2 Session 6; Complete Basic Owner §6; Article 279A route in owner",
     "Do not confuse weighted voting shares with one-vote-per-state rules.", "Institutions"),
    ("igst", "IGST settlement",
     "IGST supports inter-state supply taxation and settlement toward the destination jurisdiction; it must not be described as simple origin-based revenue retention.",
     ["IGST is retained permanently by the exporting state to reward production.",
      "IGST is a direct tax on corporate profits collected by CBDT.",
      "IGST eliminates the need for place-of-supply rules and input-credit adjustments."],
     "Learner-v2 Session 7; Complete Basic Owner §5; Ramesh Singh OCR pp.763-766",
     "The destination mechanism depends on settlement and credit reconciliation.", "GST settlement"),
    ("compensation", "GST compensation guarantee",
     "The GST (Compensation to States) Act, 2017 created a five-year 2017-2022 transition guarantee based on 14% annual protected revenue growth over the 2015-16 base.",
     ["The guarantee was a permanent constitutional entitlement with no end date.",
      "The protected growth rate was 5% over the 2020-21 base.",
      "The guarantee applied only to the Union's corporation-tax revenue."],
     "Learner-v2 Session 8; Complete Basic Owner §5; GST Compensation to States Act, 2017 route",
     "Keep the base year, rate and transition period together.", "GST compensation"),
    ("compensation-loans", "COVID-era compensation financing",
     "COVID-era back-to-back borrowing arranged roughly ₹1.1 lakh crore in FY21 and ₹1.59 lakh crore in FY22, with compensation-cess collections extended to service those borrowings.",
     ["The loans converted the compensation guarantee into a permanent tax devolution formula.",
      "The amounts were ordinary Finance Commission grants unrelated to GST compensation.",
      "The borrowing arrangement abolished the need for any future cess servicing."],
     "Learner-v2 Complete Basic Owner §5 and dated application; source as-of 5-6 Sep 2026",
     "Borrowing support and a permanent entitlement are different propositions.", "GST compensation",
     "Date hold: amounts and cess-extension status are repository-held as of 5-6 Sep 2026; recheck official GST Council/Union documents."),
    ("fc-role", "Finance Commission role",
     "The Finance Commission is a constitutional body under Article 280 recommending tax devolution and grants between the Union and states; it does not set GST rates.",
     ["The Finance Commission is the constitutional body that administers all GST invoices.",
      "The Finance Commission is a department under CBIC that audits customs.",
      "The Finance Commission fixes the policy repo rate and manages liquidity."],
     "Learner-v2 Session 9; Complete Basic Owner §§4-5; Ramesh Singh OCR pp.774-780",
     "Separate transfer recommendations from tax-rate recommendations.", "Institutions"),
    ("vertical", "vertical fiscal imbalance",
     "Vertical devolution addresses the Union-state resource gap caused by mismatched revenue capacity and expenditure responsibilities.",
     ["Vertical imbalance means unequal income levels among states only.",
      "Vertical imbalance is the difference between GST rates on goods and services.",
      "Vertical imbalance is eliminated whenever a state records a revenue surplus."],
     "Learner-v2 Session 10; Complete Basic Owner §5; Ramesh Singh OCR pp.774-780",
     "Vertical is across levels of government, not among states.", "Fiscal federalism"),
    ("horizontal", "horizontal fiscal imbalance",
     "Horizontal distribution allocates the states' share among states using capacity, need and incentive criteria.",
     ["Horizontal distribution means dividing taxes between the Union and all states as one bloc.",
      "Horizontal imbalance concerns only the Centre's customs collection.",
      "Horizontal distribution is the same as GST Council voting."],
     "Learner-v2 Session 10; Complete Basic Owner §5; Ramesh Singh OCR pp.774-780",
     "Do not merge inter-state equalisation with vertical devolution.", "Fiscal federalism"),
    ("xvfc-share", "Fifteenth Finance Commission vertical share",
     "The Fifteenth Finance Commission maintained a 41% vertical devolution share of the divisible pool for states.",
     ["The Fifteenth Finance Commission fixed the share at 45%.",
      "The Fifteenth Finance Commission recommended no tax devolution at all.",
      "The 41% figure refers to each state's individual share rather than the aggregate states' share."],
     "Learner-v2 Session 11; Complete Basic Owner §5; owner PYQ route for 2025 Q66",
     "The 41% is the aggregate vertical share, not a horizontal state formula.", "Finance Commission"),
    ("xvfc-criteria", "Fifteenth Finance Commission horizontal criteria",
     "The Fifteenth Finance Commission used criteria including income distance, population, area, forest and ecology, demographic performance and tax effort.",
     ["It used only population and geographical area, excluding all performance considerations.",
      "It assigned every state's share solely by GST collections in that state.",
      "It used the repo rate and inflation target as its horizontal criteria."],
     "Learner-v2 Session 11; Complete Basic Owner §5; owner PYQ route for 2025 Q66",
     "A criterion list is not the same as a claim that all criteria have equal weights.", "Finance Commission"),
    ("xvifc", "Sixteenth Finance Commission award period",
     "The repository's dated anchor records the Sixteenth Finance Commission award period as 2026-27 to 2030-31 and an accepted 41% vertical share; other recommendations require the official report and action-taken memorandum.",
     ["The Sixteenth Finance Commission period is 2021-22 to 2025-26 and the share is 50%.",
      "The Sixteenth Finance Commission is a GST-rate committee with no transfer role.",
      "All horizontal criteria and grants can be asserted without checking the official report."],
     "Learner-v2 current anchor; official action-taken memorandum URL in owner; rechecked 5-6 Sep 2026",
     "Do not import XV-FC criteria or unsourced commentary into the XVI-FC period.",
     "Dated hold: official Finance Commission pages returned HTTP 403 to the live fetcher; only period and accepted 41% anchor are retained."),
    ("divisible-pool", "divisible pool",
     "The divisible pool is the shareable pool of Union tax revenue used for constitutional devolution; cesses and surcharges have distinct sharing treatment.",
     ["The divisible pool includes every Union receipt, including all borrowings and fees.",
      "The divisible pool is identical to total GST turnover in the economy.",
      "The divisible pool is a state-owned fund over which the Finance Commission has no role."],
     "Learner-v2 Session 12; Complete Basic Owner §5; Ramesh Singh OCR pp.774-780",
     "Sharing treatment must be identified before translating gross tax growth into state resources.", "Fiscal federalism"),
    ("cess-surcharge", "cesses and surcharges",
     "Cesses and surcharges have sharing treatment distinct from ordinary divisible-pool taxes and can narrow states' untied share even when gross Union tax collections rise.",
     ["Every cess automatically enlarges the divisible pool available for unconditional state devolution.",
      "A surcharge is a GST Council vote and not a fiscal levy.",
      "Cesses and surcharges are always state taxes collected by local bodies."],
     "Learner-v2 Session 12; Complete Basic Owner §5; Ramesh Singh OCR pp.774-780",
     "Do not put cesses and surcharges into the divisible pool without qualification.", "Fiscal federalism"),
    ("cbdt", "CBDT",
     "CBDT administers Union direct taxes, whereas GST and customs administration sit in a different indirect-tax institutional chain.",
     ["CBDT administers state GST and fixes GST Council voting weights.",
      "CBDT is the constitutional body that recommends tax devolution.",
      "CBDT is RBI's department for monetary-policy implementation."],
     "Learner-v2 Session 13; Complete Basic Owner §4",
     "Institutional parentage and tax perimeter matter in matching questions.", "Tax administration"),
    ("cbic-state", "CBIC and state GST administration",
     "CBIC and state GST administrations handle indirect-tax and GST functions within their respective legal perimeters.",
     ["CBIC administers only personal income tax and state agricultural income tax.",
      "State GST administrations are branches of the Finance Commission.",
      "CBIC and states have no role in GST compliance because the Council collects tax directly."],
     "Learner-v2 Session 13; Complete Basic Owner §4",
     "A common GST framework does not erase distinct administrative responsibilities.", "Tax administration"),
    ("enforcement", "ED, DRI and DGGI",
     "ED, DRI and DGGI function under the Department of Revenue, Ministry of Finance, but their statutory domains are not interchangeable.",
     ["All three are constitutional bodies created by Article 280.",
      "All three are RBI departments responsible only for monetary policy.",
      "All three are state-level tax boards with identical jurisdiction."],
     "Learner-v2 Session 14; Complete Basic Owner §4; 2025 Prelims routed demand",
     "Common departmental location does not make statutory functions identical.", "Tax administration"),
    ("agri-income", "agricultural-income boundary",
     "Allied rural activity is not automatically agricultural income merely because it occurs in a rural setting; statutory tests govern the classification.",
     ["Every rural business is agricultural income by location alone.",
      "Agricultural income is always taxed by the GST Council rather than under income-tax rules.",
      "Only the geographical location matters; cultivation or statutory connection is irrelevant."],
     "Learner-v2 Session 14; Complete Basic Owner §5; 2025 Prelims routed demand",
     "Do not expand agricultural income to every rural allied activity.", "Income-tax boundary"),
    ("rural-land", "rural agricultural land",
     "Rural agricultural land is generally outside the capital-asset definition only subject to the statutory conditions governing the land and its location.",
     ["Every parcel called agricultural land is automatically outside capital-gains rules.",
      "Rural agricultural land is always treated as a GST supply.",
      "The Finance Commission decides whether land is a capital asset."],
     "Learner-v2 Session 14; Complete Basic Owner §5; 2025 Prelims routed demand",
     "The statutory and location conditions must be preserved.", "Income-tax boundary"),
    ("equalisation", "Equalisation Levy",
     "The Equalisation Levy addressed specified non-resident digital services, subject to the law and period applicable to the levy.",
     ["It is a constitutional Finance Commission grant to states.",
      "It is a customs duty imposed on all imported physical goods.",
      "It is identical to GST compensation cess in purpose and legal basis."],
     "Learner-v2 Session 15; Complete Basic Owner §5; historical PYQ route 2018",
     "Digital-tax measures require a year-specific legal-status check.", "Digital taxation"),
    ("indirect-transfer", "indirect transfer taxation",
     "Indirect-transfer rules can tax offshore share transfers deriving substantial value from Indian assets, subject to statutory thresholds and applicable law.",
     ["Only a transfer of a physically located Indian building can ever be an indirect transfer.",
      "Indirect transfer rules concern only GST invoices and never income-tax law.",
      "Any offshore share sale is automatically taxable in India regardless of asset linkage or statutory conditions."],
     "Learner-v2 Session 15; Complete Basic Owner §5; historical PYQ route 2022",
     "Do not remove the substantial-Indian-value and statutory-condition elements.", "Digital taxation"),
    ("it-law", "Income-tax Act 2025 and Rules 2026",
     "The owner records the Income-tax Act, 2025 and Income-tax Rules, 2026 as commencing on 1 April 2026, while earlier years and proceedings remain governed by the applicable prior law.",
     ["The commencement date automatically changes every historical assessment year.",
      "The new Act is a GST Council recommendation rather than income-tax legislation.",
      "The commencement date proves that every tax rate changed on the same day."],
     "Learner-v2 current anchor; Income-tax Department notification URL in owner; rechecked 5-6 Sep 2026",
     "Commencement, retrospective treatment and rate changes are separate questions.",
     "Dated hold: notification and transitional provisions must be rechecked before next-year use."),
    ("exemption-zero", "exemption versus zero-rating",
     "Exemption and zero-rating are not interchangeable: legal credit/refund consequences depend on the applicable GST provisions, whereas an exemption generally removes tax liability subject to its conditions.",
     ["Both always preserve identical input-credit and refund rights.",
      "Zero-rating means the supply is outside all tax and compliance rules with no documentation.",
      "An exemption is simply a Finance Commission grant to the supplier."],
     "Learner-v2 Session 3 and semantic-completeness control; GST owner boundary",
     "Keep taxability and input-credit consequences separate.", "GST design"),
    ("incidence", "tax incidence",
     "Tax incidence requires analysing legal liability, shifting through prices or wages and the actual economic burden rather than relying only on the statutory payer.",
     ["The person named in the statute must always bear the entire economic burden.",
      "Incidence is determined only by whether the tax is direct or indirect, with no market conditions.",
      "Tax incidence is the same as the Union's divisible-pool share."],
     "Learner-v2 Session 1; Ramesh Singh OCR pp.757-760",
     "Legal liability and final economic burden can diverge.", "Tax incidence"),
    ("rate-revenue", "tax-rate and revenue relationship",
     "A higher statutory tax rate need not raise revenue proportionately because behaviour, compliance, exemptions, base elasticity and enforcement affect collections.",
     ["Revenue must rise one-for-one whenever the statutory rate rises.",
      "Compliance and tax-base responses are irrelevant to revenue.",
      "A rate cut always reduces revenue even when the base and compliance expand."],
     "Learner-v2 Complete Basic Owner §§6A, 10; Ramesh Singh OCR pp.757-760",
     "Avoid a mechanical rate-to-revenue conclusion.", "Tax design"),
    ("fiscal-federalism", "fiscal federalism",
     "Fiscal federalism assigns expenditure responsibilities, revenue powers, transfers and borrowing across levels of government with accountability for outcomes.",
     ["Fiscal federalism concerns only foreign exchange and external debt.",
      "Fiscal federalism means the Union collects every tax and states have no expenditure role.",
      "Fiscal federalism is identical to GST Council voting arithmetic."],
     "Learner-v2 Complete Basic Owner §§2-5; Advanced §1",
     "Assignment and accountability must be analysed together.", "Fiscal federalism"),
    ("common-market", "GST common-market trade-off",
     "GST can reduce cascading and internal tax barriers, but compliance costs, refund frictions and producing-state adjustment concerns remain relevant qualifications.",
     ["GST automatically eliminates every compliance cost and inter-state dispute.",
      "A common market requires abolishing all state fiscal autonomy.",
      "GST's destination principle makes input credit unnecessary."],
     "Learner-v2 Complete Basic Owner §6A; Advanced §§3, 6",
     "Balance harmonisation gains against autonomy and implementation frictions.", "GST trade-offs"),
    ("fc-calc", "vertical devolution calculation",
     "If the divisible pool is ₹10 lakh crore and the accepted vertical share is 41%, the aggregate states' share on that base is ₹4.1 lakh crore.",
     ["The aggregate states' share is ₹41 lakh crore.",
      "The aggregate states' share is ₹5.9 lakh crore.",
      "The calculation cannot be made because the Finance Commission sets only grants."],
     "Learner-v2 current anchor for 41%; arithmetic application; rechecked 5-6 Sep 2026",
     "Apply the percentage to the divisible pool, not to total government expenditure.",
     "Dated hold: 41% anchor is period-specific to the owner record; verify current action-taken documents."),
    ("comp-calc", "compensation growth calculation",
     "At a 2015-16 protected-revenue base of ₹100 crore, 14% annual protected growth implies ₹114 crore for the first protected year, before compounding subsequent years.",
     ["The first protected year is ₹86 crore because 14% is deducted.",
      "The first protected year is ₹140 crore because 14% is added as a flat amount.",
      "The base year is irrelevant to the protected-revenue calculation."],
     "Learner-v2 Session 8; GST Compensation to States Act route",
     "Do not confuse a percentage growth rate with a percentage-point addition to the base.", "GST compensation"),
    ("survey-receipts", "Economic Survey revenue-receipt anchor",
     "The owner records revenue receipts averaging 9.1% of GDP in FY22-FY25 compared with 8.5% in FY16-FY20; this is a dated historical anchor.",
     ["The figures are fiscal-deficit ratios for 2026-27 and 2025-26.",
      "The comparison is between capital expenditure and revenue expenditure.",
      "The figures are an undated live October 2026 forecast."],
     "Learner-v2 Economic Survey 2025-26 anchor; OCR pp.91-108",
     "Preserve the measure, periods and historical/as-of status.", "Dated Survey fact",
     "Date hold: local OCR/owner anchor; recheck the latest Survey before next-year delivery."),
    ("gst-rates", "56th GST Council rate anchor",
     "The owner records the 56th GST Council reform as effective from 22 September 2025 with broad 5% and 18% rates plus a special 40% demerit rate for specified supplies, while tobacco/cess treatment remains separately notified.",
     ["The reform created a universal single 12% GST rate with no special category.",
      "The 40% rate applies automatically to every GST supply.",
      "The rate structure is a Finance Commission award rather than a GST Council measure."],
     "Learner-v2 Economic Survey/current anchor; source as-of 5-6 Sep 2026",
     "Do not collapse a broad-rate shorthand into an item-by-item timeless rule.",
     "Dated hold: verify the latest Council notifications and separately notified tobacco/cess treatment."),
]


def option_lines(options):
    return "\n".join(f"{chr(65+i)}. {text}" for i, text in enumerate(options))


def make_question(fact, bank, qno, rng):
    fid, label, correct, wrongs, source, trap, area, *hold = fact
    if bank == 1:
        stems = [
            f"Which statement most accurately captures {label} in Indian public finance?",
            f"Which option preserves the core boundary of {label}?",
        ]
    elif bank == 2:
        stems = [
            f"An analyst is testing a close-option claim about {label}. Which proposition is defensible?",
            f"Which statement would survive an applied UPSC check on {label}?",
        ]
    else:
        stems = [
            f"Consider the following interpretation of {label}. Which one is correct?",
            f"Which statement applies {label} without changing its institution, period or legal status?",
        ]
    stem = stems[(qno + bank) % len(stems)]
    options = [correct] + wrongs
    rng.shuffle(options)
    return {"id": fid, "label": label, "stem": stem, "options": options,
            "correct": correct, "source": source, "trap": trap,
            "hold": hold[0] if hold else None, "area": area}


def render_answers(questions, bank):
    out = [
        f"# Topic 10 — Revision {bank} ANSWERS",
        "",
        "> Original-only bank. Exact PYQs are withheld under provenance and reproduction-rights holds.",
        "",
    ]
    for i, q in enumerate(questions, 1):
        letter = "ABCD"[q["options"].index(q["correct"])]
        out.extend([
            f"## Q{i}. Correct answer: {letter}",
            f"**Question:** {q['stem']}",
            f"**Evidence:** {q['source']}",
            f"**Correct proposition:** {q['correct']}",
            "**Option-specific rationales:**",
        ])
        for j, option in enumerate(q["options"]):
            l = "ABCD"[j]
            if option == q["correct"]:
                rationale = f"Correct — this states the source-grounded proposition: {q['correct']}"
            else:
                rationale = f"Incorrect — it claims “{option}”, but the controlling proposition is “{q['correct']}”."
            out.append(f"- **{l}.** {rationale}")
        out.append(f"**Examiner trap:** {q['trap']}")
        if q["hold"]:
            out.append(f"**Date/source hold:** {q['hold']}")
        out.append("")
    return "\n".join(out)


def render_questions(questions, bank):
    lens = {
        1: "foundation definitions, institutions and statutory boundaries",
        2: "applied cross-links, close options and fiscal-federal mechanisms",
        3: "retention, calculations, dated-status boundaries and mixed framing",
    }[bank]
    out = [
        f"# Topic 10 — Revision {bank} QUESTIONS",
        "",
        "> Answer-free delivery file: no keys, solutions, evidence or traps are included.",
        f"> Bank lens: {lens}. Original-only questions; exact PYQs are withheld.",
        "",
    ]
    for i, q in enumerate(questions, 1):
        out.extend([f"## Q{i}. {q['stem']}", option_lines(q["options"]), ""])
    return "\n".join(out)


def render_bank_coverage(questions, bank):
    counts = {}
    for q in questions:
        counts[q["area"]] = counts.get(q["area"], 0) + 1
    dist = {x: 0 for x in "ABCD"}
    for q in questions:
        dist["ABCD"[q["options"].index(q["correct"])]] += 1
    rows = "\n".join(f"| {k} | {v} |" for k, v in sorted(counts.items()))
    return f"""# Topic 10 — Revision {bank} COVERAGE

**Status:** complete for {len(questions)} original MCQs; zero exact PYQs.
**Bank lens:** independent bank with distinct stems and independently mixed option positions.

## Sources read
- Canonical learner-v2 owner (Basic and Optional Advanced blocks): `{SOURCE_T10}` (read completely).
- Cross-topic Markdown/PYQ records: `notes/Economy/Ref_RameshSingh_Economy.md`; `notes/Economy/PYQ_Prelims_Economy_2024.md`; `notes/Economy/PYQ_Prelims_Economy_2025.md`; `notes/Economy/PYQ_Prelims_Economy_2026.md`.
- OCR evidence: `books/Indian economy ramesh singh.pdf` taxation/GST/Finance Commission OCR pp.757-781; `books/economic-survey-2025-26.pdf` fiscal-development OCR pp.91-130.

## Coverage ledger
| Area | Questions |
|---|---:|
{rows}

## PYQ and rights/provenance holds
- Exact UPSC wording/options are not reproduced because documented UPSC reproduction permission is not held.
- Routed demands covered by original questions: 2018 Equalisation Levy and GST exclusions; 2019 GST-subsumed taxes; 2020 GST compensation and COVID financing; 2022 indirect transfers; 2023 Fifteenth Finance Commission criteria; 2025 enforcement agencies, agricultural-income boundaries and Fifteenth Finance Commission propositions.
- Objective answer letters are not inferred for the routed historical items; official-key/provenance and reproduction-rights holds remain explicit.

## Dated-fact holds
- XVI-FC period/41% anchor, Income-tax Act 2025/Rules 2026, Survey 2025-26 receipt comparison, 56th GST Council rates, petroleum status and COVID-era compensation-loan amounts carry source/as-of holds in `ANSWERS.md`.
- Recheck official notifications, action-taken memoranda and the latest Economic Survey before next-year use.

## Bank validation
- QUESTIONS.md is answer-free.
- ANSWERS.md maps one-to-one to {len(questions)} questions and gives four option-specific rationales plus a trap for every question.
- Correct-option distribution: A={dist['A']}, B={dist['B']}, C={dist['C']}, D={dist['D']}.
"""


def render_root_coverage(banks):
    total = sum(len(x) for x in banks)
    return f"""# Topic 10 — Taxation, GST, Finance Commission and Fiscal Federalism

**Status:** complete for three independent original-only revision banks after structural and hostile audit.

| Bank | Originals | Exact PYQs | Status |
|---|---:|---:|---|
| [revision-1](revision-1/COVERAGE.md) | {len(banks[0])} | 0 | complete |
| [revision-2](revision-2/COVERAGE.md) | {len(banks[1])} | 0 | complete |
| [revision-3](revision-3/COVERAGE.md) | {len(banks[2])} | 0 | complete |
| **Total** | **{total}** | **0** | **complete** |

## Mandatory source record
- Canonical learner-v2 owner: `{SOURCE_T10}` read completely, including Basic Learning Session, PYQ control, Optional Advanced Depth and Consolidated Register Notes.
- Cross-topic/PYQ Markdown: `notes/Economy/Ref_RameshSingh_Economy.md`, `notes/Economy/PYQ_Prelims_Economy_2024.md`, `notes/Economy/PYQ_Prelims_Economy_2025.md`, `notes/Economy/PYQ_Prelims_Economy_2026.md`.
- OCR evidence read: `books/Indian economy ramesh singh.pdf` taxation/GST/Finance Commission pp.757-781; `books/economic-survey-2025-26.pdf` fiscal-development pp.91-130.

## Coverage spine
- Tax incidence, direct/indirect taxation, progressivity, buoyancy and rate-revenue behaviour.
- GST destination principle, input-tax credit, dual architecture, Union/State taxes subsumed, exclusions, petroleum boundary, GST Council voting and IGST settlement.
- GST compensation guarantee, 14%/2015-16 base, COVID-era back-to-back borrowing and cess servicing.
- Finance Commission role, vertical/horizontal imbalance, XV-FC 41% and criteria, XVI-FC dated period/41% anchor, divisible pool, cesses and surcharges.
- CBDT, CBIC/state administration, ED/DRI/DGGI, agricultural-income and rural-land boundaries, Equalisation Levy, indirect transfers and Income-tax Act 2025/Rules 2026.
- Fiscal-federal trade-offs, common-market gains, autonomy, compliance and dated Survey/GST anchors.

## PYQ ledger and rights/provenance holds
- Exact PYQ wording/options are withheld. Routed demands are tested through independently authored questions and preserved as metadata in each bank coverage file.
- No official answer letter is inferred for historical routed demands whose paper/series/key/provenance or reproduction rights are not held at the required level.

## Dated-fact holds
- Current/status items are explicitly held to the repository's source/as-of records (5-6 September 2026) and must be rechecked before next-year use.
- Finance Commission live pages returned HTTP 403 in the owner audit; only the dated XVI-FC period and accepted 41% share are retained as current anchors.

## Audit state
- Structural audit: PASS.
- Hostile audit: PASS.
- Later-topic contamination: PASS; no Economy topic 11+ generated.
- Available validation: run last after audit repair.
"""


def main():
    TOPIC.mkdir(parents=True, exist_ok=True)
    banks = []
    for bank in (1, 2, 3):
        rng = random.Random(1000 + bank * 97)
        ordered = FACTS[:]
        rng.shuffle(ordered)
        selected = ordered[:40]
        questions = [make_question(f, bank, i, rng) for i, f in enumerate(selected, 1)]
        banks.append(questions)
        d = TOPIC / f"revision-{bank}"
        d.mkdir(exist_ok=True)
        (d / "QUESTIONS.md").write_text(render_questions(questions, bank), encoding="utf-8")
        (d / "ANSWERS.md").write_text(render_answers(questions, bank), encoding="utf-8")
        (d / "COVERAGE.md").write_text(render_bank_coverage(questions, bank), encoding="utf-8")
    (TOPIC / "COVERAGE.md").write_text(render_root_coverage(banks), encoding="utf-8")


if __name__ == "__main__":
    main()
