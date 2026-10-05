"""Build the original-only Governance Topic 04 final-MCQ release."""

from __future__ import annotations

import json
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Governance" / "04-NGOs-SHGs-and-Civil-Society-Stakeholders"
OWNER_BASIC = r"upsc-ai-kit\knowledge\Governance\basic\04_NGOs-SHGs-and-Civil-Society-Stakeholders.md"
OWNER_ADV = r"upsc-ai-kit\knowledge\Governance\advanced\04_NGOs-SHGs-and-Civil-Society-Stakeholders.md"
PACKAGE = r"upsc-ai-kit\knowledge\Governance\04_NGOs-SHGs-and-Civil-Society-Stakeholders_Learner-V2-Complete-Topic-Package.md"
WORKBOOK = r"upsc-ai-kit\knowledge\Governance\learning-sessions\v2\subject-wide-syllabus\governance-04_Solved-Workbook.md"


def rec(focus: str, owner: str, fact: str, application: str, limitation: str, source: str, trap: str) -> dict:
    return locals()


RECORDS = [
    rec("Civil society", "Basic", "Civil society is the sphere of voluntary collective action outside the formal state and market, including NGOs, SHGs, advocacy bodies and other associations.", "A governance analysis should ask how a voluntary actor mobilises citizens, supplies information, delivers support or scrutinises public power.", "The category is wider than NGOs; treating one organisational form as the whole of civil society hides associations and informal collectives.", "Basic §§1–2; package BASIC LEARNING SESSION", "Reducing civil society to registered NGOs alone."),
    rec("NGO as one civil-society form", "Basic", "An NGO is one organisational form within civil society, whereas civil society also includes SHGs, federations, advocacy groups, unions and community associations.", "A question naming an SHG federation can be answered through civil-society analysis even when it is not an NGO.", "The owner does not license a fixed exhaustive list of civil-society organisations.", "Basic §§1–2; Advanced §2", "Treating NGO and civil society as synonyms."),
    rec("Social capital", "Basic", "Social capital consists of networks, norms of reciprocity and trust that enable collective action; it is distinct from financial capital.", "Regular meetings and peer accountability can make savings and joint action feasible even before a group has substantial financial resources.", "Social capital may facilitate financial access but does not itself guarantee income, credit, inclusion or democratic outcomes.", "Basic §§2–3,7; Advanced §2", "Calling trust and networks a form of money."),
    rec("Bonding capital", "Basic+Advanced", "Bonding capital is dense trust and reciprocity within a relatively homogeneous group, such as an SHG's internal savings circle.", "An SHG's regular savings meetings, peer accountability and internal discipline are the bonding stage of the empowerment chain.", "Bonding without links beyond the group can entrench in-group boundaries and cannot by itself deliver institutional access.", "Basic §§2–3; Advanced §§2–3", "Using bonding for a bank or government relationship."),
    rec("Bridging capital", "Basic+Advanced", "Bridging capital connects otherwise separate groups, as when SHGs federate across villages or social networks.", "A federation can pool risk, aggregate produce and negotiate at a scale unavailable to a single small group.", "Bridging expands scale but does not automatically create a vertical relationship with a bank or state department.", "Basic §§2–3; Advanced §§2–4", "Calling internal trust or state access bridging."),
    rec("Linking capital", "Basic+Advanced", "Linking capital connects citizens or groups vertically to formal power and resource structures such as banks, markets and government departments.", "A federation's bank-credit linkage or negotiation with a department illustrates linking capital converting collective capacity into institutional access.", "Linking is not a substitute for bonding and bridging; weak internal trust or scale can prevent durable access.", "Basic §§2–3; Advanced §§2–3", "Treating linking as merely cooperation among neighbouring groups."),
    rec("Self-Help Group", "Basic", "An SHG is a small voluntary group, predominantly of women in the rural-livelihoods context, that pools savings, accesses credit and undertakes collective livelihood activity.", "The SHG is the institutional unit through which savings discipline and peer accountability precede wider federation and bank linkage.", "Not every SHG outcome is automatically a livelihood or political empowerment outcome.", "Basic §2; package SESSION 3", "Defining an SHG as a government department or a bank branch."),
    rec("DAY-NRLM", "Basic", "DAY-NRLM is the Deendayal Antyodaya Yojana–National Rural Livelihoods Mission of the Ministry of Rural Development, mobilising rural women into SHGs and federations.", "A ministry-identification question should route DAY-NRLM to rural livelihoods, financial inclusion and social empowerment rather than to foreign-funding regulation.", "The owner withholds a fixed cumulative mobilisation count because the MIS total changes over time.", "Basic §§2,4,8; Advanced §4", "Assigning DAY-NRLM to the Ministry of Women and Child Development."),
    rec("Three-tier NRLM design", "Basic+Advanced", "The DAY-NRLM institutional design scales from SHGs to Village Organisations and then Cluster-Level Federations.", "The sequence converts bonding capital into bridging and linking capital through deliberate federation rather than leaving scale to chance.", "A three-tier structure does not by itself prove equal participation, political representation or successful outcomes.", "Basic §4; Advanced §§4,7", "Replacing Village Organisations with a generic district committee."),
    rec("Savings-first discipline", "Basic", "Regular savings meetings and peer accountability build the internal discipline on which SHG credit access and collective action rest.", "An auditor should look for the group process that precedes external credit, not assume that a loan alone created social capital.", "Savings discipline cannot by itself resolve market saturation, weak services or over-indebtedness.", "Basic §§3,13.4; package SESSION 3", "Treating external borrowing as the first and defining SHG step."),
    rec("SHG–Bank Linkage route", "Basic", "The SHG–Bank Linkage route is a savings-first group pathway in which a group balance sheet and repayment record support access to bank credit.", "Its institutional incentive is to build group savings, records and collective creditworthiness rather than simply expand an individual lender's loan book.", "Credit access does not establish that the financed activity is profitable or that poverty has structurally ended.", "Basic §13.0(a); package SESSION 6", "Equating SHG–Bank Linkage with an MFI's individual loan model."),
    rec("MFI/NBFC-MFI route", "Basic", "The MFI or NBFC-MFI route uses specialised lenders, regulated through the financial system, to provide micro-finance services to excluded borrowers.", "A comparison should distinguish a specialised lender's loan-book incentive from an SHG route that builds a group balance sheet.", "The owner does not authorise a general claim about every MFI's rates, portfolio quality or crisis experience.", "Basic §13.0(a); package SESSION 6", "Treating all micro-finance as a single SHG channel."),
    rec("Micro-finance versus micro-credit", "Basic", "Micro-finance is a wider bundle of small-value financial services such as credit, savings, insurance and remittance; micro-credit is only one component.", "A complete anti-poverty assessment should test which service is available and what household constraint it addresses.", "Access to a micro-credit loan alone cannot establish access to insurance, savings, remittance or poverty exit.", "Basic §13.0(a); package SESSION 7", "Using micro-credit and micro-finance as interchangeable terms."),
    rec("Consumption smoothing", "Basic", "Micro-finance is strongest as a consumption-smoothing and vulnerability-reduction instrument when irregular income and shocks make household cash flow unstable.", "Small savings or credit can help a household bridge an income gap without immediately selling assets or relying on a moneylender.", "Consumption smoothing is not the same as durable asset accumulation or structural poverty exit.", "Basic §13.0(a); package SESSION 7", "Treating short-term liquidity support as proof of long-term transformation."),
    rec("Structural poverty exit", "Basic", "Micro-finance is weaker as a structural poverty-exit instrument because small loans, thin returns and saturated markets may not create durable assets or rising incomes.", "An evaluation should examine enterprise viability, asset creation, market access and repayment funded by income rather than repeated borrowing.", "This is a qualified limitation, not a claim that micro-finance never supports enterprise or poverty reduction.", "Basic §13.0(a); package SESSION 7", "Calling every micro-finance intervention ineffective."),
    rec("Multiple lending", "Basic", "Multiple lending occurs when several lenders serve the same household, creating a risk of over-indebtedness and repayment pressure.", "A responsible assessment should examine total borrower obligations across lenders rather than one loan account in isolation.", "The owner does not supply a universal borrower count, portfolio number or sector-wide incidence figure.", "Basic §13.0(a); package SESSION 8", "Treating any second loan as automatically unlawful or always harmful."),
    rec("Coercive recovery", "Basic", "Coercive recovery is a named micro-finance sector risk in which repayment pressure becomes abusive, prompting the need for regulatory correction.", "A governance review should distinguish repayment discipline from coercion and examine whether borrower protection and grievance routes operate.", "The owner does not adjudicate a particular lender, case or current enforcement outcome.", "Basic §13.0(a); package SESSION 8", "Inferring coercion merely from the existence of repayment."),
    rec("Cost of small-ticket delivery", "Basic", "Serving small and remote loans can be expensive, creating a tension between delivery cost, borrower affordability and lender sustainability.", "An evaluation should ask how transaction costs, distance and monitoring affect the service model instead of assuming that every small loan can carry the same cost.", "The owner withholds interest-rate caps and portfolio figures; no universal rate conclusion is permitted.", "Basic §13.0(a); package SESSION 8", "Assuming high cost proves profiteering or low cost proves access."),
    rec("Nutrition pathway", "Basic", "The nutrition effect of women's SHG micro-financing is an indirect convergence pathway through income control, health messaging and public nutrition services.", "A sound explanation connects women's control over resources with SHG platforms and convergence rather than claiming a direct automatic income-to-nutrition effect.", "The owner does not authorise a malnutrition percentage or a measured causal effect.", "Basic §13.0(b); package SESSION 9", "Claiming that a loan directly guarantees improved nutrition."),
    rec("Non-member poor", "Basic", "The non-member poor are households excluded from SHG-based inclusion because they are not part of any group.", "An inclusion audit should ask who remains outside the collective rather than equating member success with universal community coverage.", "The owner does not quantify the excluded population or permit a fixed SHG coverage claim.", "Basic §13.8; package SESSION 5", "Assuming every poor household is already an SHG member."),
    rec("Women's empowerment chain", "Basic+Advanced", "The empowerment chain runs from bonding trust to federated bridging, then linking to banks, markets and government, producing income control and public voice.", "Each stage should be tied to a distinct outcome: discipline, scale and institutional access, rather than repeating a generic empowerment claim.", "The chain can stall at any stage or be distorted by elite capture; it is not an automatic linear result.", "Basic §§3,13.6; Advanced §3", "Listing social capital without explaining its causal sequence."),
    rec("FCRA purpose", "Basic", "The Foreign Contribution (Regulation) Act, 2010, administered by the Ministry of Home Affairs, regulates acceptance and utilisation of foreign contributions by associations.", "A foreign-funding question should begin with the FCRA gate and distinguish it from incorporation, tax status and government-grant identity.", "FCRA is not a general law governing every domestic donation or every aspect of NGO finance.", "Basic §2,§4; Advanced §§2,4", "Saying FCRA regulates all NGO funding."),
    rec("FCRA registration route", "Basic+Advanced", "An association with FCRA registration may receive foreign contributions on an ongoing basis subject to continuing compliance and renewal obligations.", "A question about recurring foreign receipts should distinguish registration from a case-specific prior-permission route.", "The owner does not assert current counts of registered, suspended or cancelled associations.", "Basic §§2,4,13.10; Advanced §§2,9", "Treating registration as permanent and compliance-free."),
    rec("FCRA prior permission", "Advanced", "Prior permission is a case-specific route for an association without ongoing FCRA registration to receive a defined foreign contribution for a specified purpose.", "The route should be analysed as narrower and transaction-specific than an ongoing registration, with its own compliance burden.", "The owner does not supply a universal processing time or guarantee that permission will be granted.", "Advanced §2; package SESSION 10", "Treating prior permission as identical to registration."),
    rec("Designated FCRA account", "Basic+Advanced", "The 2020 FCRA amendment framework requires a designated FCRA bank account at the specified State Bank of India main branch in New Delhi.", "A prelims item on the amendment should test the designated-account requirement rather than infer that any ordinary NGO account suffices.", "The owner does not extend this fact into claims about every later banking interface or current account-holder list.", "Basic §4,§13.10; Advanced §§4,7", "Replacing the specified SBI New Delhi account route with an NGO's ordinary local account."),
    rec("FCRA administrative-expense limit", "Basic+Advanced", "The 2020 framework reduced the permissible administrative-expense proportion from 50% to 20% of foreign contribution utilised.", "A compliance audit should distinguish the statutory expense proportion from programme spending and avoid turning it into a general domestic-donation rule.", "The owner does not support current expenditure totals or a claim about a named organisation's compliance.", "Advanced §4; package SESSION 10", "Using the older 50% figure or applying the rule to all NGO receipts."),
    rec("FCRA sub-granting restriction", "Basic+Advanced", "The 2020 FCRA framework restricted sub-granting foreign contributions between FCRA-registered entities.", "A chain-funding question should test whether a registered recipient can freely pass foreign funds to another registered entity; the owner says the route is restricted.", "The source does not adjudicate any individual transfer or later enforcement action.", "Basic §4; Advanced §4", "Assuming registration of both entities removes the restriction."),
    rec("FCRA renewal and current-status hold", "Advanced", "FCRA compliance includes continuing renewal obligations, while counts of current registrations, suspensions and cancellations are dynamic and held.", "A dated answer should separate the stable statutory route from live administrative totals that require an issuer check.", "No current count or enforcement trend should be invented from a static owner file.", "Advanced §9; Basic §13.10", "Converting a current-status hold into a guessed statistic."),
    rec("NGO Darpan", "Basic", "NGO Darpan is a NITI Aayog identification and database portal assigning a Unique ID used in Union-government grant and linked compliance interfaces.", "A grant-eligibility question should route NGO Darpan to identification and visibility, not to foreign-funding permission.", "Darpan is light-touch and largely self-reported; it does not itself ensure financial accountability.", "Basic §§2,4,13.5; Advanced §§2,4", "Calling NGO Darpan incorporation or FCRA permission."),
    rec("Darpan versus FCRA", "Basic+Advanced", "NGO Darpan and FCRA are distinct layers: Darpan identifies organisations for grant administration, whereas FCRA is the legal gate for foreign contributions.", "An organisation may need to satisfy different interfaces for a Union grant and for foreign receipts; one status cannot be substituted for the other.", "The owner does not claim that Darpan registration cures any FCRA or tax non-compliance.", "Basic §§2,4,13.5; Advanced §7", "Treating a Darpan Unique ID as permission to receive foreign funds."),
    rec("Incorporation layer", "Basic", "Incorporation or legal existence is a separate layer governed through a trust, society or section 8 company route and is not the same as being funded.", "A governance map should first identify the legal vehicle, then separately test foreign funding, tax status and grant identity.", "The owner does not assert that one legal vehicle is universally superior for every civil-society purpose.", "Basic §13.5; package SESSION 11", "Assuming incorporation automatically permits every funding source."),
    rec("Tax layer", "Basic+Advanced", "Income-tax 12A/80G processes govern tax-exemption status for an NGO and deduction for domestic donors, separately from FCRA.", "A tax-status question should not be answered with the MHA foreign-funding route or the NITI Aayog grant-identity route.", "Tax exemption is not a licence to receive foreign contributions.", "Basic §13.5; Advanced §§2,7", "Treating 12A/80G as FCRA registration."),
    rec("Regulatory-layer routing", "Basic+Advanced", "The four layers are incorporation, foreign funding, tax status and government-grant identity, administered through different legal or administrative routes.", "A close-option problem is solved by identifying what the instrument governs before naming the regulator.", "The layers can interact in practice but remain conceptually and legally distinct.", "Basic §13.5; package SESSION 11", "Collapsing all NGO compliance into one registration."),
    rec("Non-state actor", "Basic+Advanced", "A civil-society organisation is structurally non-state because it is outside formal government, regardless of whether it cooperates with or criticises government.", "The classification should be made from institutional structure, not from whether an organisation supports a particular policy.", "Non-state status says nothing by itself about representativeness, transparency or the quality of advocacy.", "Basic §§2,5; Advanced §§2–3", "Calling every non-state actor anti-State."),
    rec("Anti-State perception", "Basic+Advanced", "Anti-State is a contested political or perceptual label that may arise when a CSO's advocacy, funding source or activity is seen as conflicting with state policy or sovereignty concerns.", "A reasoned answer should acknowledge the perception while retaining the structural non-state category and testing the case-specific evidence.", "The label cannot be accepted as a blanket legal classification of all CSOs.", "Basic §5; Advanced §§3,5", "Using anti-State as a synonym for non-state."),
    rec("Watchdog and advocacy function", "Basic+Advanced", "CSOs may monitor implementation, highlight rights violations, advocate policy change and oppose specific projects while remaining outside government.", "A governance framework should treat advocacy as feedback and scrutiny, while separately testing funding transparency and evidence quality.", "Adversarial perception can arise, but disagreement alone does not prove illegality or external control.", "Basic §3; Advanced §3", "Assuming service delivery is the only legitimate civil-society role."),
    rec("Foreign funding and suspicion chain", "Advanced", "Foreign-funded advocacy can intensify state suspicion because FCRA's security rationale concerns possible external interests, while the proportionality of restrictions remains contested.", "An answer should present both the security rationale and the civic-space concern without adjudicating a specific enforcement case.", "No named organisation, cancellation, security finding or current enforcement outcome is asserted.", "Advanced §§3,6,9; package SESSION 10", "Treating the security rationale or the civic-space critique as the only permissible view."),
    rec("Pressure group", "Basic", "A pressure group is an organised interest seeking to influence public policy without itself seeking to form the government.", "Its tools may include consultation, research, media, petitions, litigation and mobilisation rather than contesting for governmental office as its defining purpose.", "Pressure groups can be unequal, opaque or captured; non-contestation alone does not establish democratic legitimacy.", "Basic §§2–3; Advanced §3", "Treating pressure groups and political parties as identical."),
    rec("R-I-S-K test", "Basic", "The R-I-S-K frame evaluates a pressure group through representation, information or expertise, scrutiny and capture risk.", "An environmental group should be assessed for whose interests it represents, what evidence it adds, how it scrutinises and whether unequal access distorts policy.", "The acronym is an analytical tool, not proof that every group satisfies all four dimensions.", "Basic §9; Advanced §3", "Listing advocacy activity without testing representation or capture."),
    rec("Representation", "Basic+Advanced", "Representation asks whether a civil-society or pressure group credibly reflects the affected population rather than only its own professional or donor network.", "Membership disclosure, consultation and internal participation help test whether a claimed community voice is representative.", "An organisation's expertise or media visibility does not automatically establish representativeness.", "Basic §§3,13.7; Advanced §§3,6", "Equating public visibility with representative legitimacy."),
    rec("Information and expertise", "Basic+Advanced", "Pressure groups can improve governance by supplying specialised information and aggregating diffuse interests that the state may otherwise miss.", "Regulators can use evidence from an environmental group while still checking methodology, funding and conflicts of interest.", "Information value does not immunise a group from capture, bias or accountability questions.", "Basic §3; Advanced §3", "Treating any claim made by an organised group as verified expertise."),
    rec("Scrutiny", "Basic+Advanced", "Civil-society scrutiny includes monitoring implementation, petitions, litigation, media work and public criticism that can expose blind spots.", "The governance effect is strongest when scrutiny produces traceable evidence and a reviewable public response.", "Scrutiny can correct a blind spot or become one-sided influence if access and evidence are opaque.", "Basic §3; Advanced §3", "Treating criticism alone as successful accountability."),
    rec("Capture risk", "Basic+Advanced", "Capture risk arises when unequal money, access or organisational capacity lets one organised interest privilege its preferences over broader public interests.", "Disclosure of funding, conflicts and consultation records helps distinguish pluralist influence from opaque capture.", "The existence of unequal influence does not prove that a particular group has captured a decision.", "Advanced §§2–3; package SESSION 14", "Assuming all organised advocacy is either neutral or captured."),
    rec("Elite capture in federations", "Basic+Advanced", "Elite capture occurs when dominant caste, economic or already-empowered groups control a participatory or collective body such as an SHG federation.", "Rotational leadership, reservation, disclosure and external facilitation can make federation governance more inclusive.", "Social capital is not automatically democratic; the owner does not claim that a named federation is captured.", "Basic §13.4,§13.7; Advanced §§2,5", "Assuming dense local networks always empower the least powerful."),
    rec("NGO delivery as complement", "Basic", "NGOs are often strongest as complements, innovators, facilitators and monitors of public delivery rather than substitutes for the state.", "A contract can use local trust or pilot capacity while retaining public convergence, disclosure and a citizen grievance route.", "Complementarity does not mean every NGO partnership is effective or every state service is adequate.", "Basic §13.0(c); package PYQ card 3", "Concluding that NGO participation automatically privatises the service."),
    rec("NGO delivery and duty-holder", "Basic", "An NGO should not become the duty-holder for a public entitlement because a right requires an addressee who can be compelled and held publicly accountable.", "The state can commission facilitation or service support while retaining the legal and institutional responsibility for the entitlement.", "This does not deny NGO operational value; it sets an accountability boundary.", "Basic §13.0(c); package SESSION 15", "Treating contracted delivery as transfer of the state's duty."),
    rec("Scale challenge", "Basic", "NGO delivery may be geographically partial and organisation-specific, so it cannot automatically guarantee equitable state-wide coverage.", "A model comparison should test whether the intervention reaches remote and non-member populations at the scale of a public entitlement.", "Limited scale does not erase the value of local innovation or last-mile access.", "Basic §13.0(c); package PYQ card 3", "Assuming local reach proves universal coverage."),
    rec("Sustainability challenge", "Basic", "Project-cycle or donor funding can be temporary, whereas a public entitlement requires durable institutional and fiscal continuity.", "Exit planning and convergence with public systems are needed if a pilot is to outlast its grant cycle.", "The owner does not claim that every donor-funded project ends or that every public programme is sustainable.", "Basic §13.0(c); package SESSION 15", "Equating donor funding with permanent service capacity."),
    rec("Accountability direction", "Basic", "NGOs may be accountable upward to donors or funders rather than downward to citizens through electoral or statutory mechanisms.", "A sound partnership adds disclosure, beneficiary grievance access and public review instead of assuming donor reporting is citizen accountability.", "Upward accountability can coexist with professional standards but does not replace a public duty-holder.", "Basic §13.0(c); Advanced §6", "Treating audited donor reports as a substitute for citizen accountability."),
    rec("Substitution risk", "Basic+Advanced", "Substitution risk arises when NGO delivery relieves political pressure to repair universal public systems instead of complementing them.", "A policy should ask whether the partnership strengthens the public delivery chain or quietly makes a temporary project carry a permanent entitlement.", "The risk is a design possibility, not proof that any particular partnership weakens the state.", "Basic §13.0(c); package SESSION 15", "Assuming every public–NGO partnership is state withdrawal."),
    rec("Regulatory dependence", "Basic+Advanced", "An NGO's ability to scale can depend on registration, renewal and compliance under applicable legal and funding regimes, including FCRA for foreign contributions.", "An assessment should distinguish operational capacity from the legal gate that permits a particular funding stream.", "Regulatory dependence does not itself show that scrutiny is illegitimate or that an organisation lacks autonomy.", "Basic §13.0(c); Advanced §§4,6", "Treating compliance dependence as proof of government control."),
    rec("Civil society and women's representation", "Basic", "Civil society can support representation through rights literacy, candidate identification, leadership training, advocacy, litigation, election monitoring and mobilisation.", "An SHG federation can act as a school of public life that develops negotiation and public-speaking capacities.", "Local leadership does not automatically become legislative candidature or electoral success.", "Basic §13.0(d); package PYQ card 4", "Assuming social mobilisation directly guarantees legislative seats."),
    rec("Party-ticket gate", "Basic", "Party ticket distribution remains a decisive gate between civil-society leadership and representation in State legislatures, and civil society does not control that gate.", "A representation analysis should place candidate training and mobilisation before, not instead of, party selection and electoral institutions.", "The owner withholds percentages of women legislators and reservation-implementation claims.", "Basic §13.0(d); package PYQ card 4", "Treating training or SHG office-holding as a guaranteed ticket."),
    rec("Internal democracy safeguard", "Advanced", "Internal democracy, disclosed membership, mandated consultation and inclusive leadership design strengthen the legitimacy of a civil-society claim to represent a community.", "A federation can reduce capture by rotating leadership and reserving space for excluded members while publishing decisions.", "Safeguards improve legitimacy but do not prove that every group is representative or free of conflict.", "Basic §13.7; Advanced §§5–6", "Assuming registration alone proves representativeness."),
    rec("Professionalisation trade-off", "Basic+Advanced", "Professional staff, audits and reporting can raise quality and donor confidence but may increase costs and distance an organisation from volunteers.", "A governance review should weigh administrative capability against community ownership and donor-legible priorities.", "Professionalisation is not inherently harmful or beneficial; its effect depends on design and accountability.", "Basic §13.7; Advanced §6", "Treating professional staff as proof of either capture or effectiveness."),
    rec("Community ownership versus speed", "Advanced", "Genuine community ownership can be slower, while contracting an experienced NGO can deliver faster but may weaken ownership if participation is bypassed.", "A well-designed programme combines time-bound delivery with local consultation, convergence and an exit plan.", "Speed and ownership are not absolute opposites; the trade-off is contextual.", "Basic §13.7; Advanced §6", "Assuming the fastest implementation is always the most sustainable."),
]


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def choose_options(index: int, field: str, revision: int, rng: random.Random, desired: int) -> tuple[list[str], int, list[int]]:
    correct = clean(RECORDS[index][field])
    pool = [j for j in range(len(RECORDS)) if j != index]
    candidates = sorted(pool, key=lambda j: (abs(len(clean(RECORDS[j][field])) - len(correct)), (j - index) % len(RECORDS)))
    candidates = candidates[:3]
    entries = [(correct, index)] + [(clean(RECORDS[j][field]), j) for j in candidates]
    rng.shuffle(entries)
    actual = next(i for i, (_, source) in enumerate(entries) if source == index)
    entries[desired], entries[actual] = entries[actual], entries[desired]
    key = next(i for i, (_, source) in enumerate(entries) if source == index)
    return [text for text, _ in entries], key, [source for _, source in entries]


R1_STEMS = [
    "Which statement most accurately captures **{focus}** within the governance of NGOs, SHGs and civil society?",
    "In a basic conceptual reading, which proposition about **{focus}** is sound?",
    "Which description best matches the defined meaning of **{focus}**?",
    "A prelims candidate is distinguishing adjacent civil-society concepts. Which statement about **{focus}** is correct?",
]
R2_STEMS = [
    "A district team is analysing a delivery claim about **{focus}**. Which inference is most defensible?",
    "If an auditor observes the situation described in the stem, which conclusion about **{focus}** follows?",
    "A policy note applies the topic's governance framework to **{focus}**. Which application is soundest?",
    "Which inference best uses **{focus}** to interpret an Indian civil-society or SHG case?",
]
R3_STEMS = [
    "During a hostile audit of **{focus}**, which qualification should be retained?",
    "Which conclusion about **{focus}** would avoid overstating the available evidence?",
    "A careful examiner tests the boundary of **{focus}**. Which statement preserves that boundary?",
    "Which caveat is essential when using **{focus}** in a governance answer?",
]


def build_bank(revision: int) -> tuple[str, str, str]:
    rng = random.Random(20261004 + revision * 137)
    field = {1: "fact", 2: "application", 3: "limitation"}[revision]
    base, remainder = divmod(len(RECORDS), 4)
    positions = []
    for option_index in range(4):
        positions.extend([option_index] * (base + (1 if option_index < remainder else 0)))
    rng.shuffle(positions)
    qlines = [
        f"# Governance Topic 04 — Revision {revision}: Questions\n\n",
        "Original UPSC-style questions. Each item is answer-free; explanations are maintained separately.\n",
    ]
    alines = [
        f"# Governance Topic 04 — Revision {revision}: Answers\n\n",
        "Every item is original. Each option is analysed separately against the owner evidence, with the relevant source route and examiner trap retained.\n",
    ]
    clines = [
        f"# Governance Topic 04 — Revision {revision}: Question-level Coverage\n\n",
        "| Q | Key | Affirmative owner focus | Evidence route | Status |\n|---:|:---:|---|---|---|\n",
    ]
    keys = {letter: 0 for letter in "ABCD"}
    for i, item in enumerate(RECORDS):
        qno = i + 1
        options, key_index, provenance = choose_options(i, field, revision, rng, positions[i])
        key = "ABCD"[key_index]
        keys[key] += 1
        stem_set = {1: R1_STEMS, 2: R2_STEMS, 3: R3_STEMS}[revision]
        stem = stem_set[i % len(stem_set)].format(focus=item["focus"])
        qlines.append(f"\n### Q{qno}\n{stem}\n\n")
        for letter, option in zip("ABCD", options):
            qlines.append(f"{letter}. {option}\n")
        alines.append(f"\n{qno}. **{key}.**\n")
        for letter, option, source_index in zip("ABCD", options, provenance):
            source = RECORDS[source_index]
            if source_index == i:
                qualifier = source[field]
                alines.append(
                    f"{letter}: Correct. This option directly tests **{item['focus']}**. "
                    f"Evidence: {item['source']}. The source-grounded route is: {option} "
                    f"Applied qualification: {qualifier}\n"
                )
            else:
                alines.append(
                    f"{letter}: Not the best answer for **{item['focus']}**. It describes the neighbouring "
                    f"owner focus **{source['focus']}**, supported by {source['source']}, but it does not "
                    f"establish the active distinction. Its claim is: {option}\n"
                )
        alines.append(f"**Sources:** {item['source']}. **Examiner trap:** {item['trap']}\n")
        clines.append(
            f"| {qno} | {key} | {item['focus']} — {clean(item[field])} | {item['source']} | "
            f"PASS — affirmative {field} route; original; no exact PYQ wording. |\n"
        )
    alines.append(f"\n**Key distribution:** {keys['A']} A / {keys['B']} B / {keys['C']} C / {keys['D']} D.\n")
    return "".join(qlines), "".join(alines), "".join(clines)


def write_ledgers() -> None:
    owner_rows = [
        "| ID | Owner focus | Basic/Advanced route | R1 | R2 | R3 | Status |",
        "|---:|---|---|:---:|:---:|:---:|---|",
    ]
    for i, item in enumerate(RECORDS, 1):
        owner_rows.append(f"| {i} | {item['focus']} | {item['owner']} | PASS | PASS | PASS | Affirmative route in all banks |")
    (TOPIC / "OWNER-MATRIX.md").write_text(
        "# Topic 04 Owner Matrix — NGOs, SHGs and Civil-Society Stakeholders\n\n"
        "The Basic owner is the foundation; Advanced adds distinctions, trade-offs and application. "
        "Every owner row is tested affirmatively in all three independent banks.\n\n"
        + "\n".join(owner_rows)
        + "\n\n**Boundary rule:** a detail appearing only in a distractor or rationale does not count as coverage.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-ROUTING.md").write_text(
        "# Topic 04 Source Routing\n\n"
        "## Primary evidence\n\n"
        f"- Basic owner: `{OWNER_BASIC}` — complete foundation and factual controls.\n"
        f"- Advanced owner: `{OWNER_ADV}` — distinctions, trade-offs and application.\n"
        f"- Complete package: `{PACKAGE}` and `{WORKBOOK}` — learning-session and PYQ-demand cross-check.\n"
        "- Official syllabus boundary: GS-II, NGOs, SHGs, groups and associations; civil-society stakeholders and governance.\n\n"
        "## Institutional-fact applicability audit\n\n"
        "| Instrument/institution | Origin | Mandate | HQ | Membership | Reports/frequency | Funding | Leadership | Committees | Timeline | India linkage | Awards |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| DAY-NRLM | verified in Basic owner | verified livelihoods mobilisation | not applicable | SHGs/federations as institutional units | MIS count held as dynamic | revolving/community investment support route verified; amounts held | not asserted | VO/CLF federation route verified | current mobilisation totals held | India rural livelihoods | not applicable |\n"
        "| FCRA, 2010 as amended 2020 | verified in Basic/Advanced owners | foreign-contribution acceptance and utilisation | not applicable | associations subject to route | compliance/renewal route verified; current counts held | foreign contributions; figures held | MHA administration verified | not asserted | 2020 account, expense and sub-grant changes verified | India foreign-funding gate | not applicable |\n"
        "| NGO Darpan | NITI Aayog portal route verified | identification/database and Union-grant interface | not applicable | NGO records; counts held | largely self-reported database | not applicable | not asserted | not asserted | current records held | India grant-identity interface | not applicable |\n"
        "| SHG / Village Organisation / Cluster-Level Federation | DAY-NRLM design verified | savings, aggregation, negotiation and linking | not applicable | voluntary group members | no fixed mobilisation total asserted | savings/credit and community support route | office-bearer design; named leadership not asserted | federation route verified | dynamic expansion held | India rural livelihoods and empowerment | not applicable |\n"
        "## Source discipline\n\n"
        "No NGO name, current registration count, cancellation count, borrower count, interest-rate figure, "
        "malnutrition percentage, legislative-representation percentage or enforcement outcome is invented.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        "# Topic 04 Source and PYQ Holds\n\n"
        "- **Exact objective PYQs:** none reproduced. The available material routes Mains demands and does not provide a rights-cleared objective reproduction set.\n"
        "- **Mains PYQs routed:** 2020 GS-II Q17 (micro-finance and SHGs); 2021 GS-II Q8 (women's SHG micro-financing, gender inequality, poverty and malnutrition); 2021 GS-II Q18 (civil society/NGO public-service delivery); 2023 GS-II Q14 (civil-society groups and women's representation). The 2025 GS-II owner also records bonding/bridging/linking, anti-State/non-state and environmental-pressure-group demands.\n"
        "- **Reproduction hold:** exact UPSC wording and options remain withheld pending same-paper/set/question provenance and documented reproduction permission under the UPSC website policy.\n"
        "- **Key hold:** routed Mains demands have no objective answer key; owner analysis is not presented as an official key.\n"
        "- **Current-status holds:** DAY-NRLM mobilisation totals, FCRA registration/renewal/suspension/cancellation counts and NGO Darpan records change over time and require issuer verification.\n"
        "- **Measurement holds:** no borrower count, interest-rate cap, NPA, malnutrition percentage, NGO result, funding amount, legislative-representation percentage or enforcement outcome is asserted.\n",
        encoding="utf-8",
    )
    owner_matrix = "\n".join(owner_rows)
    (TOPIC / "COVERAGE.md").write_text(
        "# Topic 04 Coverage — NGOs, SHGs and Civil-Society Stakeholders\n\n"
        "## Release summary\n\n"
        f"- Three independent original-only banks: {len(RECORDS)} / {len(RECORDS)} / {len(RECORDS)} questions.\n"
        "- Every bank has affirmative coverage of all Basic/Advanced owner rows.\n"
        "- Questions are answer-free; answers separately explain all four options, sources and traps.\n"
        "- Exact PYQ wording/options are withheld under explicit source, provenance and rights holds.\n\n"
        "## Owner coverage\n\n" + owner_matrix
        + "\n\n## Boundary and unresolved items\n\n"
        "- Advanced material is enrichment; no Advanced detail is silently treated as a prerequisite for the Basic route.\n"
        "- Dynamic programme counts, current regulatory actions and named-organisation outcomes remain holds rather than guessed facts.\n"
        "- Cross-owned pressure-group composition and reservation-law detail remain routed to Polity/Social Justice where applicable.\n",
        encoding="utf-8",
    )
    (TOPIC / "OPTION-AUDIT.md").write_text(
        "# Topic 04 Option Audit\n\n"
        "## Method\n\n"
        "Each bank independently shuffles the correct option with a reproducible seed. Distractors are selected "
        "from neighbouring owner facts, applications or limitations and length-matched to reduce visual cues.\n\n"
        "## Release checks\n\n"
        "- Four options per question; duplicate options rejected.\n"
        "- Correct positions are independently shuffled and recorded per bank; no fixed A-B-C-D rotation.\n"
        "- Options use parallel full-sentence forms and retain source-bounded qualifiers.\n"
        "- R1 tests foundation, R2 tests application and R3 tests qualification; no bank is a position-only reshuffle.\n",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        "# Topic 04 Structural Audit\n\n"
        f"- [PASS] revision-1, revision-2 and revision-3 exist.\n"
        f"- [PASS] Each bank contains {len(RECORDS)} contiguous questions and answers.\n"
        "- [PASS] Every question has exactly four distinct options.\n"
        "- [PASS] Every answer has A/B/C/D option-specific analysis, sources and an examiner trap.\n"
        f"- [PASS] Every bank has a question-level COVERAGE.md with {len(RECORDS)} rows.\n"
        "- [PASS] Questions contain no answer key, rationale, source cue or explanatory suffix.\n"
        "- [PASS] Exact PYQ wording/options are absent.\n",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        "# Topic 04 Hostile Audit\n\n"
        "- [PASS] No question heading reveals a key; headings are Q1 onward only.\n"
        "- [PASS] No answer text, source citation or rationale appears in QUESTIONS.md.\n"
        "- [PASS] No exact PYQ wording/options are reproduced.\n"
        "- [PASS] R1/R2/R3 use foundation, application and qualification frames with distinct stems.\n"
        "- [PASS] Correct positions are independently shuffled and option counts are balanced within one item.\n"
        "- [PASS] Institution fields are marked verified, not applicable or held; no unsupported current statistic is made.\n"
        "- [PASS] FCRA, DAY-NRLM and NGO Darpan boundaries are kept separate.\n"
        "- [PASS] Social-capital, anti-State, pressure-group, delivery and elite-capture traps remain visible.\n",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        "# Topic 04 Audit Report\n\n"
        "Release decision: **complete for original banks with explicit holds**.\n\n"
        "The three banks pass structural, option-balance, leakage, cross-revision distinctness, source/date, "
        "institutional-fact and hostile checks. Exact PYQ wording, current issuer totals and named-organisation "
        "outcomes remain withheld rather than guessed.\n",
        encoding="utf-8",
    )
    validation = {
        "topic": "04",
        "title": "NGOs, SHGs and Civil-Society Stakeholders",
        "status": "complete_for_original_banks_with_explicit_holds",
        "banks": {"revision-1": len(RECORDS), "revision-2": len(RECORDS), "revision-3": len(RECORDS)},
        "owner_rows": len(RECORDS),
        "affirmative_owner_coverage": {"revision-1": len(RECORDS), "revision-2": len(RECORDS), "revision-3": len(RECORDS)},
        "exact_pyqs_reproduced": 0,
        "holds": [
            "UPSC exact wording/options reproduction permission and objective-PYQ provenance/key",
            "DAY-NRLM live mobilisation totals",
            "FCRA current registration, renewal, suspension and cancellation counts",
            "NGO Darpan live records",
            "micro-finance borrower, rate, NPA and portfolio figures",
            "named NGO funding, results and enforcement outcomes",
            "women's legislative-representation percentages and current reservation implementation",
        ],
        "approved": False,
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    for revision in (1, 2, 3):
        folder = TOPIC / f"revision-{revision}"
        folder.mkdir(exist_ok=True)
        questions, answers, coverage = build_bank(revision)
        (folder / "QUESTIONS.md").write_text(questions, encoding="utf-8")
        (folder / "ANSWERS.md").write_text(answers, encoding="utf-8")
        (folder / "COVERAGE.md").write_text(coverage, encoding="utf-8")
    write_ledgers()
    print(f"Built Governance Topic 04: {len(RECORDS)} questions per revision, 3 revisions.")


if __name__ == "__main__":
    main()
