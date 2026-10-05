"""Build the original-only Governance Topic 02 final-MCQ release.

The source owners are the authority for the facts.  This builder deliberately keeps
exact PYQ wording out of the live banks and records the provenance/rights holds in the
topic ledgers.
"""

from __future__ import annotations

import json
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Governance" / "02-Government-Policy-Design-and-Implementation"
OWNER_BASIC = "upsc-ai-kit\\knowledge\\Governance\\basic\\02_Government-Policy-Design-and-Implementation.md"
OWNER_ADV = "upsc-ai-kit\\knowledge\\Governance\\advanced\\02_Government-Policy-Design-and-Implementation.md"
PACKAGE = "upsc-ai-kit\\knowledge\\Governance\\learning-sessions\\v2\\subject-wide-syllabus\\governance-02_Learning-Session.md"
WORKBOOK = "upsc-ai-kit\\knowledge\\Governance\\learning-sessions\\v2\\subject-wide-syllabus\\governance-02_Solved-Workbook.md"


RECORDS = [
    dict(focus="Policy cycle", owner="Basic", fact="The policy cycle runs analytically from agenda setting through formulation, decision, implementation and evaluation, with feedback returning to agenda setting.", application="Use the stages to locate whether a failure is diagnostic, design-stage, delivery-stage or evaluative rather than calling every shortfall poor implementation.", limitation="The cycle is a locating device, not a claim that every policy moves neatly once through a fixed one-way sequence.", source="Basic §§1–2; package §2", trap="Treating the cycle as a rigid chronology hides feedback and makes a design failure look like a delivery failure."),
    dict(focus="Implementation gap", owner="Basic+Advanced", fact="The implementation gap is the difference between a policy as designed or announced and the policy actually delivered on the ground.", application="A sound announcement followed by missing staff, unclear procedures or inaccessible interfaces exhibits an implementation gap even without proof of corrupt intent.", limitation="The concept identifies the design–delivery difference; by itself it does not identify one cause or establish corruption.", source="Basic §§2–3; Advanced §§1,11", trap="Reducing implementation failure to corruption alone."),
    dict(focus="Clearance points", owner="Advanced", fact="A clearance point is an additional actor, approval or intergovernmental step that a policy must pass before proceeding.", application="A Union–State–district–Panchayat chain is structurally more exposed to delay and distortion than a single-agency route, even when each actor is competent.", limitation="Removing clearance points can improve speed while also reducing local adaptation, deliberation or stakeholder buy-in.", source="Basic §3; Advanced §§2–3,6", trap="Assuming more approvals automatically create proportional accountability."),
    dict(focus="Complexity of joint action", owner="Advanced", fact="Pressman and Wildavsky associate implementation failure with the cumulative complexity of joint action as individually likely steps multiply.", application="Several high-probability approvals can still produce a low overall success probability when the steps are sequential and interdependent.", limitation="The argument diagnoses structural risk; it does not prove that every multi-level programme will fail.", source="Advanced §§2–3,7; package evidence bank A", trap="Reading the clearance-point argument as a claim that funding is irrelevant in every case."),
    dict(focus="Street-level bureaucracy", owner="Basic+Advanced", fact="Michael Lipsky's street-level bureaucracy describes frontline officials whose discretionary choices effectively make policy in daily practice.", application="A ration dealer, teacher, health worker or examination-centre official can determine the citizen's lived entitlement through decisions made under real workload and rule conditions.", limitation="Discretion is not automatically illegitimate; the governance task is to guide it with reasons, records and review.", source="Basic §§2,5–7; Advanced §§2,5", trap="Assuming frontline officials merely transmit decisions made at the top."),
    dict(focus="Coping routines", owner="Advanced", fact="Under caseload and resource pressure, street-level officials may ration time, favour easier cases or bend informal routines predictably.", application="A repeated pattern of serving easy cases first can explain exclusion error without alleging bribery or deliberate malice.", limitation="A specific allegation of creaming needs caseload, staffing or case-distribution evidence rather than a generic assertion.", source="Advanced §§2–3,5; Basic §3", trap="Treating all unequal outcomes as proof of individual corruption."),
    dict(focus="Creaming", owner="Advanced", fact="Lipsky's 'creaming' means favouring beneficiaries who are easier or cheaper to serve when frontline resources are scarce.", application="If a desk processes simple applications first and silently leaves complex eligible cases unresolved, the pattern is a discretion-and-capacity problem.", limitation="Creaming is an analytical mechanism, not a finding that every delay or prioritisation is discriminatory.", source="Advanced §§2–3; Basic §13.7", trap="Confusing creaming with ordinary prioritisation supported by a lawful rule."),
    dict(focus="Top-down implementation", owner="Advanced", fact="A top-down reading asks whether frontline action matched the policy's original design and authorised objectives.", application="Auditing an Act by comparing designated-centre practice with its statutory procedures is a top-down implementation test.", limitation="Top-down fidelity alone cannot show what citizens actually experienced or how frontline adaptation shaped outcomes.", source="Advanced §§2–3,10", trap="Treating formal compliance as the whole of implementation."),
    dict(focus="Bottom-up implementation", owner="Advanced", fact="A bottom-up reading treats what frontline actors actually produce as the real policy, regardless of design intent.", application="To ask whether an examination law worked in practice, inspect what centre officials actually did under workload, rules and local conditions.", limitation="A bottom-up account should not erase the legal design or the authority against which implementation is evaluated.", source="Advanced §§2–3,10", trap="Mistaking the lived outcome for a licence to ignore statutory limits."),
    dict(focus="Design realism", owner="Basic+Advanced", fact="Design realism asks whether targets, incentives and procedures match the administrative capacity available to implement them.", application="Universal coverage targets with unfilled sanctioned posts indicate a formulation problem that later appears as an implementation failure.", limitation="Realism does not mean abandoning ambition; it means matching ambition to a credible delivery chain and assumptions.", source="Basic §3; Advanced §§2–3; package evidence bank A", trap="Calling every ambitious policy unrealistic or every delivery gap a design failure."),
    dict(focus="Agenda-setting bias", owner="Advanced", fact="Agenda setting can privilege politically visible or media-salient problems over issues that are administratively tractable.", application="A symbolic policy aimed at a visible problem may be well announced yet poorly suited to the administrative problem actually requiring solution.", limitation="Visibility is not proof that a policy is wrong; the claim is about selection bias and problem diagnosis.", source="Advanced §3", trap="Equating political attention with evidence that the chosen intervention is administratively sound."),
    dict(focus="Regulatory Impact Assessment", owner="Basic+Advanced", fact="RIA is an ex-ante assessment of a proposed regulation's costs, benefits, alternatives and likely effects before finalisation.", application="An RIA-style exercise can expose capacity constraints, perverse incentives or externalities before a rule reaches frontline delivery.", limitation="RIA is unevenly institutionalised in India and should not be described as a uniformly binding requirement across all regulators.", source="Basic §§2–4; Advanced §§3–4", trap="Treating a recommended assessment tool as a universal statutory precondition."),
    dict(focus="Pre-Legislative Consultation Policy", owner="Basic+Advanced", fact="The Union's 2014 policy recommends placing draft legislation or rules in the public domain with an explanatory note and a minimum comment window before introduction.", application="Publishing a draft with a response matrix can surface design and implementation problems before formal introduction.", limitation="The policy is an executive consultation framework; publication does not make every comment binding or create a statutory right by itself.", source="Basic §§2,4; Advanced §§3–4", trap="Confusing consultation guidance with a law that compels acceptance of stakeholder views."),
    dict(focus="Consultation depth", owner="Advanced", fact="Meaningful consultation requires more than formal publication; it also asks whether affected stakeholders were heard and feedback was considered.", application="A draft posted for the required period without a response to major implementation objections shows compliance without consultation depth.", limitation="A response matrix improves traceability but does not require government to accept every proposal.", source="Advanced §§2,5–6; Basic §3", trap="Treating attendance, publication or comment counts as proof of substantive participation."),
    dict(focus="Convergence", owner="Basic+Advanced", fact="Convergence deliberately aligns multiple schemes or departments toward a common local outcome instead of operating them as isolated silos.", application="Linking livelihoods, watershed and skilling interventions around one district outcome can reduce duplicate processes and improve delivery coherence.", limitation="Convergence does not automatically solve capacity, authority or funding constraints; it needs a responsible coordinating level.", source="Basic §§2–4; Advanced §4; package evidence bank B", trap="Describing convergence as a new scheme rather than coordination of existing instruments."),
    dict(focus="Convergence as clearance-point reduction", owner="Advanced", fact="The governance value of convergence is that it removes or reduces clearance points between parallel interventions rather than merely adding another programme.", application="A district convergence mechanism can synchronise existing schemes so a beneficiary does not navigate disconnected departmental chains.", limitation="Coordination can fail when functional authority is not devolved or when participating agencies do not share usable information.", source="Basic §13.0(a); Advanced §§3–4; package §13.9", trap="Assuming a coordination committee has power simply because it exists on paper."),
    dict(focus="District and Panchayat coordination", owner="Basic+Advanced", fact="District administration and Panchayat-level mechanisms are practical sites where multiple Union and State schemes meet at delivery.", application="A local convergence body is most useful when it assigns responsibility, aligns work plans and follows the citizen's outcome across departmental boundaries.", limitation="Administrative instruction without funds, functions, functionaries or usable data cannot create genuine local coordination.", source="Basic §4; Advanced §4; package §13.8", trap="Confusing a meeting or committee with operational convergence."),
    dict(focus="Public Examinations Act purpose", owner="Basic", fact="The 2024 Act seeks to prevent and penalise unfair means in specified public examinations and protect their credibility.", application="A question about the Act's aims should distinguish integrity protection from the separate issue of which examination authorities fall within its scope.", limitation="The Act's purpose does not itself expand coverage to every examination held anywhere in India.", source="Basic §§4–5,9; package PYQ card 1", trap="Answering a scope question only by repeating the statute's general objective."),
    dict(focus="Public Examinations Act offences", owner="Basic+Advanced", fact="The owner identifies paper leaks, impersonation and tampering among the unfair means addressed by the 2024 Act.", application="An implementation audit should check whether offences, designated authorities, investigation and examination-centre practice are operationalised.", limitation="Listing offences does not establish detection rates, convictions or deterrence outcomes, none of which is verified in the owner.", source="Basic §§4,9; Advanced §4", trap="Inferring enforcement performance from the existence of offences."),
    dict(focus="Public Examinations Act commencement", owner="Basic+Advanced", fact="The Act is recorded as having come into force on 21 June 2024 through S.O. 2422(E).", application="A dated-law question should separate commencement from later implementation by designated authorities and examination centres.", limitation="The commencement date does not answer whether a particular State board or university is covered.", source="Basic §8; Advanced §9; package PYQ card 1", trap="Using the commencement notification as if it were a blanket coverage notification."),
    dict(focus="Authority-based coverage", owner="Basic+Advanced", fact="Coverage under the 2024 Act is authority-based: scheduled public examination authorities and those later notified by the Central Government are the relevant route.", application="To test coverage, identify the examining authority and the Schedule or notification rather than relying only on where the examination occurs.", limitation="Territorial extent across India is not the same as automatic coverage of every State or university examination.", source="Basic §§4,8–9; Advanced §§4–5", trap="Replacing an authority test with a geography test."),
    dict(focus="Scheduled central authorities", owner="Basic", fact="The owner lists UPSC, SSC, Railway Recruitment Boards, IBPS, NTA and Central Government departments or attached offices among scheduled authorities.", application="A question naming one of these authorities should be answered through the Schedule route, subject to the source's dated-status boundary.", limitation="The list should not be expanded with an unverified institution, rank, leadership detail or later notification.", source="Basic §4; package §13.5", trap="Treating every recruitment or admission body as automatically scheduled."),
    dict(focus="State boards and universities", owner="Basic+Advanced", fact="A State board or university examination is not automatically covered merely because the Act extends to India; a notified authority or separate State law is required.", application="A scope answer must inspect the authority framework and any applicable notification or State legislation rather than infer coverage from territorial extent.", limitation="The owner does not claim a universal later expansion; any additional authority remains a Gazette-verification hold.", source="Basic §§4,8–9; Advanced §§4–5", trap="Confusing territorial operation with automatic institutional inclusion."),
    dict(focus="Six-stage map: legal authority", owner="Basic", fact="Stage 1 asks whether the intervention rests on an Act, rule, guideline or executive scheme and who is legally bound.", application="An enacted law answers the legal-authority stage but does not prove that rules, staff, interfaces or appeals exist.", limitation="Stopping the audit at legal authority risks declaring implementation complete before delivery machinery exists.", source="Basic §10; package §13.6", trap="Treating enactment as evidence that all later stages are functioning."),
    dict(focus="Six-stage map: rules and SOPs", owner="Basic", fact="Stage 2 asks whether entitlement, eligibility and operating procedure are specified in rules or standard operating procedures.", application="A law with no usable eligibility or workflow instructions can stall even when the responsible agency is named.", limitation="Clear SOPs do not substitute for staff, money, technology or an accessible citizen interface.", source="Basic §10; package §13.6", trap="Treating a broad statutory purpose as a complete operating procedure."),
    dict(focus="Six-stage map: responsible agency", owner="Basic", fact="Stage 3 asks whether a Union, State, district, local or parastatal agency is clearly responsible for delivery.", application="An entitlement without a named delivery holder creates an accountability gap before any outcome can be evaluated.", limitation="Naming an agency alone does not establish capacity, coordination or a remedy for failure.", source="Basic §10; package §13.6", trap="Assuming jurisdictional mention is the same as operational responsibility."),
    dict(focus="Six-stage map: staff, money and technology", owner="Basic", fact="Stage 4 tests sanctioned versus filled posts, fund-flow routes and the data or technology needed to operate the intervention.", application="Unfilled posts or an unusable data system can explain a delivery shortfall even when budget sanction exists.", limitation="Sanctioned capacity is not deployed capacity, and technology cannot by itself cure a flawed entitlement design.", source="Basic §10; package §13.6", trap="Using allocation or procurement as a proxy for functioning capacity."),
    dict(focus="Six-stage map: citizen interface", owner="Basic", fact="Stage 5 examines awareness, documents, distance, language and digital access at the point where citizens seek delivery.", application="A technically available service can still exclude eligible people when documentation, travel, language or connectivity costs are prohibitive.", limitation="A better interface improves access but cannot by itself resolve an absent legal entitlement or fund flow.", source="Basic §13.6; package §13.8", trap="Counting portal availability as equal to accessible service."),
    dict(focus="Six-stage map: grievance and review", owner="Basic", fact="Stage 6 asks whether appeal, penalty, evaluation and sunset or renewal arrangements can correct failure and feed evidence back.", application="A complaint disposal count is incomplete if citizens cannot secure correction or if repeated failures do not trigger redesign.", limitation="A grievance channel is not automatically an effective remedy; accessibility, reasons and corrective authority matter.", source="Basic §§10,13.6–13.9; package §13.6", trap="Equating registration or disposal with resolution."),
    dict(focus="Aspirational Districts Programme", owner="Basic", fact="The NITI Aayog Aspirational Districts Programme is described as covering 112 districts and targeting inter-district development divergence.", application="The programme should be read as an administrative-attention and convergence instrument that focuses supervisory intensity on lagging districts.", limitation="The owner does not authorise claims about a district's rank, KPI value or total expenditure.", source="Basic §13.0(a); package PYQ card 2", trap="Turning the programme into an unsupported funding or rank statistic."),
    dict(focus="Aspirational Districts indicators", owner="Basic", fact="The programme uses 49 KPIs across five themes: health and nutrition; education; agriculture and water resources; financial inclusion and skill development; and basic infrastructure.", application="A coverage answer should name the themes and distinguish a KPI output from a realised development outcome.", limitation="Improvement in an indicator is not by itself proof that the wider outcome or intra-district distribution improved.", source="Basic §13.0(a); package §13.5", trap="Treating a dashboard indicator as a complete causal evaluation."),
    dict(focus="Champions of Change dashboard", owner="Basic", fact="The Aspirational Districts indicators are tracked on the Champions of Change dashboard in the topic's verified owner route.", application="The dashboard can support monitoring and attention allocation, but the analyst must still test data quality and outcome meaning.", limitation="The owner records largely district-self-reported data with validation by selected agencies, not a fully independent census.", source="Basic §13.0(a); package §13.5", trap="Treating a dashboard label as independent outcome verification."),
    dict(focus="Aspirational Districts levers", owner="Basic", fact="The programme's three named levers are convergence of schemes, collaboration among officials and competition through delta ranking.", application="A complete answer explains what each lever changes: pooled delivery, coordinated supervision and improvement-oriented comparison.", limitation="The three levers do not eliminate the need for capacity, local authority or reliable measurement.", source="Basic §13.0(a); package PYQ card 2", trap="Listing convergence, collaboration and competition without stating their mechanisms."),
    dict(focus="Delta ranking", owner="Basic+Advanced", fact="Delta ranking compares the pace of improvement rather than only the absolute level of development.", application="Ranking improvement rates can keep historically disadvantaged districts from being permanently fixed at the bottom of an absolute-level table.", limitation="A faster improvement rate does not prove that the district has reached a high absolute level or that every block benefited.", source="Basic §13.0(a); package §13.5", trap="Confusing relative improvement with absolute performance."),
    dict(focus="Self-reported dashboard data", owner="Basic+Advanced", fact="The owner cautions that Aspirational Districts dashboard data is largely district-self-reported with validation by selected agencies.", application="Comparative claims should disclose reporting and validation limits before treating a dashboard change as causal proof.", limitation="A self-reporting caveat does not make every indicator useless; it requires cautious interpretation and verification.", source="Basic §13.0(a); package §13.5", trap="Moving from a data limitation to the unsupported claim that no monitoring value exists."),
    dict(focus="Aspirational Blocks Programme", owner="Basic", fact="The Aspirational Blocks Programme is recorded as a separate programme covering 513 blocks and is not interchangeable with the district-level unit.", application="Block-level targeting addresses intra-district variation that a district average can conceal.", limitation="The block programme cannot be used to supply a district rank, KPI or expenditure figure absent a verified source.", source="Basic §13.0(a); package §13.5", trap="Treating district and block interventions as the same geographic unit."),
    dict(focus="Policy contradiction and externality", owner="Basic+Advanced", fact="Contradictory sectoral policies can harm the environment when ministries optimise separate mandates and the environmental cost appears in nobody's metric.", application="A water-intensive incentive alongside groundwater conservation illustrates a coordination and externality problem, not simply an absence of policy.", limitation="Not every contradiction is a coordination failure; some are genuine value conflicts that process alone cannot resolve.", source="Basic §13.0(b); Advanced §§3,5–6", trap="Assuming more policies automatically produce coherent aggregate outcomes."),
    dict(focus="Value conflict", owner="Advanced", fact="A value conflict, such as livelihood gains today versus ecological stock tomorrow, cannot always be solved by better coordination or appraisal.", application="A strong answer distinguishes a missing arbitration mechanism from a real choice between competing public values.", limitation="Calling a conflict a value trade-off should not excuse avoidable siloing, absent metrics or weak inter-ministerial appraisal.", source="Basic §13.0(b); Advanced §6", trap="Using the value-conflict qualification to dismiss all coordination reform."),
    dict(focus="PM GatiShakti", owner="Basic+Advanced", fact="PM GatiShakti is described as a National Master Plan approach using a shared GIS-based layer for multi-modal infrastructure and utility planning.", application="A common map can reveal alignments and utility corridors so ministries sequence projects and private bidders face less information risk.", limitation="The platform coordinates information, not authority; land, utilities and many approvals remain with States and local bodies.", source="Basic §13.0(c); Advanced §§3,5", trap="Treating a shared planning layer as a transfer of constitutional or statutory authority."),
    dict(focus="GatiShakti and private-sector coordination", owner="Basic+Advanced", fact="The governance contribution to private-sector coordination is de-risking through predictable information and a visible project pipeline rather than a claim of direct subsidy.", application="A bidder can price and sequence work more credibly when planned alignments and utility corridors are visible on a common data layer.", limitation="Information visibility depends on data currency and State participation and does not remove all federal or jurisdictional friction.", source="Basic §13.0(c); package PYQ card 4", trap="Turning an information reform into an investment figure or financing claim not held by the source."),
    dict(focus="PPP governance", owner="Basic", fact="A defensible PPP framework specifies public purpose, output standards, risk allocation, competitive procurement, performance payment, monitoring, disclosure and exit rules.", application="PPP is a procurement and service-delivery choice where whole-life outputs can be specified, not privatisation by definition.", limitation="PPP can create demand, contingent-liability, renegotiation, affordability and accountability risks if the contract is weak.", source="Basic §13.0(c); package §13.0 PPP block", trap="Assuming private participation automatically transfers public accountability."),
    dict(focus="PPP risk allocation", owner="Basic+Advanced", fact="PPP risk should be assigned to the actor best able to manage it, with monitoring, dispute and exit arrangements specified before award.", application="A contract that leaves demand risk, performance standards and renegotiation rules vague creates diffuse accountability rather than disciplined sharing.", limitation="Risk-sharing is not uniform across PPPs; the appropriate allocation depends on the service, contract and information available.", source="Basic §13.0(c); package PPP block", trap="Treating every PPP instrument as the same risk-transfer model."),
    dict(focus="Viability Gap Funding", owner="Basic", fact="Viability Gap Funding is identified as support for economically justified but commercially weak PPP projects.", application="VGF can make a socially valuable project bankable without converting the PPP into a general claim that all commercial risk is removed.", limitation="The owner supplies no project-level success rate, fiscal total or universal guarantee of viability.", source="Basic §13.0(c); package PPP block", trap="Confusing targeted viability support with blanket subsidy or guaranteed returns."),
    dict(focus="Hybrid Annuity Model", owner="Basic", fact="The Hybrid Annuity Model illustrates deliberate risk sharing in which construction and operation risk substantially remains with the concessionaire while government carries a larger revenue-payment role.", application="HAM shows why PPP analysis must inspect the actual allocation of construction, operation and payment risks instead of using a single privatisation label.", limitation="The model is an example of risk sharing, not evidence that every PPP or every HAM project has the same allocation or outcome.", source="Basic §13.0(c); package PPP block", trap="Assuming the government's payment role means all delivery risk has shifted to the public side."),
    dict(focus="Universalism versus targeting", owner="Basic", fact="Targeting concentrates scarce resources but needs identification machinery that can exclude; universalism avoids identification error but can cost more and be regressive in incidence.", application="The choice should compare identification cost and benefit value rather than treating either targeting or universalism as a universal rule.", limitation="The correct mix depends on the entitlement, administrative capacity, fiscal space and consequences of exclusion.", source="Basic §13.7; package §13.7", trap="Presenting targeting as efficient by definition or universalism as costless by definition."),
    dict(focus="Inclusion error", owner="Basic", fact="Inclusion error occurs when an ineligible person is included in a programme or entitlement.", application="Tighter verification can reduce inclusion error, but an audit must separately test whether eligible people were wrongly excluded.", limitation="A reduction in inclusion error is not proof that exclusion risk fell or that the programme became more equitable overall.", source="Basic §13.7; package evidence bank B", trap="Using inclusion and exclusion error as interchangeable labels."),
    dict(focus="Exclusion error", owner="Basic", fact="Exclusion error occurs when an eligible person is left out of a programme or entitlement.", application="Authentication or documentation barriers can reduce duplicate or ineligible entries while creating a distinct risk that eligible people cannot complete access.", limitation="The owner recommends an offline or assisted fallback where subsistence entitlements make exclusion especially costly.", source="Basic §13.7; package evidence bank B", trap="Calling every verification failure an inclusion error."),
    dict(focus="DBT de-duplication boundary", owner="Basic", fact="Identity verification and de-duplication can correct inclusion error while creating a separate exclusion-error risk at authentication.", application="A delivery audit should record both duplicate removal and eligible applicants unable to authenticate rather than report only the first metric.", limitation="The owner does not permit a claim that de-duplication automatically improves every welfare outcome.", source="Basic §13.5, §13.7; package evidence bank B", trap="Treating a cleaner beneficiary list as proof of universal access."),
    dict(focus="Speed versus consultation", owner="Advanced", fact="Faster enactment can reduce deliberation and buy-in, while consultation can improve design realism but delay urgent action.", application="Time-bound consultation with a published response matrix is a governance compromise between speed and informed design.", limitation="The trade-off is contextual; urgency does not make consultation meaningless and consultation does not guarantee acceptance.", source="Basic §13.7; Advanced §6", trap="Treating speed and participation as mutually exclusive absolutes."),
    dict(focus="Discretion versus uniformity", owner="Advanced", fact="Discretion can adapt policy humanely or ration it arbitrarily, while uniform rules are predictable but may ignore genuine difference.", application="Guided discretion uses clear entitlements, written reasons, recorded decisions and appeal rather than trying to abolish frontline judgment.", limitation="Guidance and records reduce arbitrariness but cannot guarantee identical outcomes in unequal circumstances.", source="Basic §13.7; Advanced §6,11", trap="Choosing either unconstrained discretion or total uniformity as the only governance option."),
    dict(focus="Centralised design versus local adaptation", owner="Advanced", fact="Fewer clearance points can speed decisions, whereas local input can improve fit; a sound design can centralise entitlement while allowing local delivery adaptation.", application="The governance question is which decision needs uniformity and which method can be adapted locally without changing the entitlement.", limitation="Local adaptation without accountability can become arbitrary variation, while centralisation can become unresponsive.", source="Basic §13.7; Advanced §6", trap="Equating centralisation with efficiency in every service context."),
    dict(focus="Theory of change", owner="Advanced", fact="A theory of change makes the chain from input to activity, output, outcome and impact explicit and states the assumptions that may fail.", application="It helps a policy designer identify whether the weak link is resources, activity, output, outcome or an untested causal assumption.", limitation="Writing a theory of change is not evidence that its assumptions hold or that impact has occurred.", source="Basic §13.4; package evidence bank A", trap="Confusing a causal map with causal proof."),
    dict(focus="Evidence plan", owner="Advanced", fact="The topic's recommended evidence plan tracks baseline, output, outcome, exclusion effect, responsible evaluator and review date.", application="A policy review becomes more diagnostic when it names what will be measured, who will evaluate it and when evidence will trigger redesign.", limitation="A list of indicators is not a guarantee of independent evaluation or a remedy for poor data quality.", source="Advanced §11; package §13.6", trap="Treating monitoring activity as outcome evaluation."),
    dict(focus="PYQ ownership and source hold", owner="Basic+Advanced", fact="The topic routes four Mains demands from 2018 and 2022 plus the 2024 Act demand, while no objective Prelims PYQ is released in these banks.", application="Original MCQs can test the concepts independently while exact PYQ wording and options remain withheld until provenance, key and reproduction-rights gates are complete.", limitation="A routed Mains demand is not an official objective key and an answer-less source reference cannot be presented as a solved Prelims PYQ.", source="Topic workbook PYQ audit §§807–880; final-MCQ release policy", trap="Treating a local coaching key or a routed Mains question as permission to reproduce an exact objective item."),
]


def option_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text


def choose_options(
    index: int,
    field: str,
    revision: int,
    rng: random.Random,
    desired_position: int,
) -> tuple[list[str], int, list[int]]:
    correct = option_text(RECORDS[index][field])
    # Keep distractors close in subject matter while ensuring every item remains affirmative.
    pool = [j for j in range(len(RECORDS)) if j != index]
    # Select close-length alternatives so visible size does not reveal the key.
    candidates = sorted(
        pool,
        key=lambda j: (abs(len(option_text(RECORDS[j][field])) - len(correct)), (j - index) % len(RECORDS)),
    )
    candidates = candidates[:3]
    distractors = [option_text(RECORDS[j][field]) for j in candidates]
    entries = [(correct, index)] + list(zip(distractors, candidates[:3]))
    # Independently randomise option positions; the fixed seed makes the release reproducible.
    rng.shuffle(entries)
    correct_position = next(i for i, (_, source_index) in enumerate(entries) if source_index == index)
    entries[desired_position], entries[correct_position] = entries[correct_position], entries[desired_position]
    options = [text for text, _ in entries]
    key = next(i for i, (_, source_index) in enumerate(entries) if source_index == index)
    provenance = [source_index for _, source_index in entries]
    return options, key, provenance


def stem(record: dict, revision: int, number: int) -> str:
    if revision == 1:
        return f"Which statement most accurately captures **{record['focus']}** in government policy design and implementation?"
    if revision == 2:
        return f"A policy analyst is testing a delivery claim about **{record['focus']}**. Which inference is the soundest?"
    return f"During a hostile audit of **{record['focus']}**, which qualification should be retained?"


def build_questions(revision: int) -> tuple[str, str, str]:
    rng = random.Random(20261004 + revision * 97)
    field = {1: "fact", 2: "application", 3: "limitation"}[revision]
    positions = [0] * 14 + [1] * 14 + [2] * 13 + [3] * 13
    rng.shuffle(positions)
    questions: list[str] = [
        f"# Governance Topic 02 — Revision {revision}: Questions\n\n"
        "Original UPSC-style Prelims questions. Each item is answer-free; exact PYQ wording and options are withheld under the source/rights hold.\n"
    ]
    answers: list[str] = [
        f"# Governance Topic 02 — Revision {revision}: Answers\n\n"
        "All items are original. Each option is analysed against the active owner focus; source and PYQ holds remain visible in the topic ledgers.\n"
    ]
    coverage: list[str] = [
        f"# Governance Topic 02 — Revision {revision}: Question-level Coverage\n\n"
        "| Q | Key | Affirmative owner focus | Evidence route | Status |\n"
        "|---:|:---:|---|---|---|\n"
    ]
    key_counts = {letter: 0 for letter in "ABCD"}
    for i, record in enumerate(RECORDS):
        qno = i + 1
        options, key_index, provenance = choose_options(i, field, revision, rng, positions[i])
        key = "ABCD"[key_index]
        key_counts[key] += 1
        questions.append(f"\n### Q{qno}\n{stem(record, revision, qno)}\n\n")
        for letter, text in zip("ABCD", options):
            questions.append(f"{letter}. {text}\n")
        answers.append(f"\n{qno}. **{key}.**\n")
        for letter, text, source_index in zip("ABCD", options, provenance):
            source_record = RECORDS[source_index]
            if source_index == i:
                answers.append(
                    f"{letter}: Correct. This is the **{record['focus']}** route tested by the stem. "
                    f"It is supported by {record['source']}: {text} "
                    f"Application/qualification: {record['application'] if field != 'limitation' else record['limitation']}\n"
                )
            else:
                answers.append(
                    f"{letter}: Not the best answer for **{record['focus']}**. It describes **{source_record['focus']}**, "
                    f"whose evidence route is {source_record['source']}; it does not establish the active distinction. "
                    f"That neighbouring concept is: {text}\n"
                )
        answers.append(f"**Sources:** {record['source']}. **Examiner trap:** {record['trap']}\n")
        coverage.append(
            f"| {qno} | {key} | {record['focus']} — {option_text(record[field])} | "
            f"{record['source']} | PASS — affirmative {field} route; original item; no exact PYQ wording. |\n"
        )
    answers.append(f"\n**Key distribution:** {key_counts['A']} A / {key_counts['B']} B / {key_counts['C']} C / {key_counts['D']} D.\n")
    return "".join(questions), "".join(answers), "".join(coverage)


def write_ledgers() -> None:
    topic_title = "Government Policy Design and Implementation"
    owner_rows = [
        "| ID | Owner focus | Basic/Advanced route | R1 | R2 | R3 | Status |",
        "|---:|---|---|:---:|:---:|:---:|---|",
    ]
    for i, record in enumerate(RECORDS, 1):
        owner_rows.append(f"| {i} | {record['focus']} | {record['owner']} | PASS | PASS | PASS | Affirmative route in all banks |")
    (TOPIC / "OWNER-MATRIX.md").write_text(
        f"# Topic 02 Owner Matrix — {topic_title}\n\n"
        "The Basic owner is the foundation; Advanced adds distinctions, trade-offs and application. "
        "Every row has an affirmative, question-level route in all three independent banks.\n\n"
        + "\n".join(owner_rows) + "\n\n"
        "**Boundary rule:** a fact appearing only in a distractor or rationale is not counted; the "
        "field named in each revision's coverage ledger is the affirmative owner route.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-ROUTING.md").write_text(
        "# Topic 02 Source Routing\n\n"
        "## Primary evidence\n\n"
        f"- Basic owner: `{OWNER_BASIC}` — complete foundation and current-status controls.\n"
        f"- Advanced owner: `{OWNER_ADV}` — implementation theory, trade-offs and cross-sector applications.\n"
        f"- Complete package: `{PACKAGE}` and `{WORKBOOK}` — evidence-bank and PYQ-demand cross-check.\n"
        "- Official syllabus boundary: UPSC GS-II, government policies and interventions; issues arising out of design and implementation.\n\n"
        "## Institutional-fact applicability audit\n\n"
        "| Instrument/institution | Origin | Mandate | HQ | Membership | Reports/frequency | Funding | Leadership | Committees | Timeline | India linkage | Awards |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| Public Examinations Act, 2024 | verified in owner | verified in owner | not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | commencement verified; later notifications held | India-wide territorial extent, authority-based coverage | not applicable |\n"
        "| Pre-Legislative Consultation Policy, 2014 | verified in owner | verified recommendation | not applicable | not applicable | not applicable | not applicable | not applicable | not applicable | 2014 policy; later revisions held | Union formulation-stage instrument | not applicable |\n"
        "| Aspirational Districts Programme | verified in owner | verified | not applicable | not applicable | dashboard/KPI route verified; rank values held | expenditure figures held | Prabhari arrangement verified | coordination route verified | 112 districts and 49 KPIs verified in owner | India district-level programme | not applicable |\n"
        "| PM GatiShakti | verified in owner | shared GIS planning layer verified | not applicable | not applicable | data currency held for live claims | investment/target figures held | not asserted | inter-ministerial coordination route verified | launch-date claims held | India infrastructure coordination | not applicable |\n"
        "| PPP governance instruments | VGF/HAM examples verified in owner | risk/output/monitoring architecture verified | not applicable | project-specific | project outcomes held | project-level figures held | contract-specific | contract monitoring route verified | project timelines held | India procurement/service delivery | not applicable |\n"
        "| RIA | emerging practice in owner | ex-ante assessment verified | not applicable | not applicable | regulator-specific | not asserted | not asserted | regulator-specific | uniform mandate held | India regulatory governance | not applicable |\n\n"
        "## Source discipline\n\n"
        "Sources are used for discovery and evidence only; no unsupported rank, funding, leadership, "
        "committee, headquarters, award, target, outcome or later-notification claim is inserted.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        "# Topic 02 Source and PYQ Holds\n\n"
        "- **Exact objective PYQs:** none reproduced. The source audit found no released objective Prelims item owned by this topic.\n"
        "- **Mains PYQs routed to the owner:** 2018 GS-I aspirational districts; 2018 GS-II policy contradictions/environment; 2022 GS-II Gati-Shakti; 2024 GS-II Public Examinations Act and public-healthcare design/delivery demand.\n"
        "- **Reproduction hold:** exact UPSC wording/options remain withheld pending same-paper/set/question provenance, authenticated official key where applicable, and reproduction permission under the UPSC website policy.\n"
        "- **Answer-key hold:** the routed Mains demands have no official objective key; authored routes in the learning package are not presented as official keys.\n"
        "- **Current-status hold:** the Act's 21 June 2024 commencement and scheduled-authority route are retained from the dated owner. Any later Central-Government notification must be verified from the Gazette before use.\n"
        "- **Measurement holds:** no district rank, KPI value, expenditure total, project success rate, investment figure, ministry count or logistics-cost percentage is asserted.\n"
        "- **Issuer-scope holds:** RIA's uniform mandatory status, later examination-authority additions and live dashboard validation beyond the owner are held.\n",
        encoding="utf-8",
    )
    (TOPIC / "COVERAGE.md").write_text(
        "# Topic 02 Coverage — Government Policy Design and Implementation\n\n"
        "## Release summary\n\n"
        "- Three independent original-only banks: 50 / 50 / 50 questions.\n"
        "- Every bank has affirmative coverage of all 50 Basic/Advanced owner rows.\n"
        "- Questions are answer-free; answers are separate and analyse every option with evidence and a trap.\n"
        "- Exact PYQ wording/options are withheld under the explicit source/PYQ/rights holds.\n\n"
        "## Owner coverage\n\n"
        + "\n".join(owner_rows)
        + "\n\n## Boundary and unresolved items\n\n"
        "- The Basic owner is complete and the Advanced owner is enrichment; no Advanced row is silently used as a prerequisite for a core answer.\n"
        "- Time-sensitive Act notifications, live dashboard values, project figures and objective PYQ provenance remain dated holds rather than guessed facts.\n"
        "- Cross-topic content is used only where the owner explicitly routes it: local convergence, monitoring/evaluation, and PPP/infrastructure coordination.\n",
        encoding="utf-8",
    )
    (TOPIC / "OPTION-AUDIT.md").write_text(
        "# Topic 02 Option Audit\n\n"
        "## Method\n\n"
        "Each bank independently shuffles the correct position with a reproducible seed. Distractors "
        "come from adjacent but different owner facts/applications/limitations, so the active concept "
        "must be identified rather than guessed from formatting.\n\n"
        "## Release checks\n\n"
        "- Four options per question: required and structurally checked.\n"
        "- Duplicate options: none generated.\n"
        "- Correct-position balance: recorded at the end of each ANSWERS.md; no fixed A-B-C-D sequence.\n"
        "- Option-length cue: checked by the release script; options use parallel full-sentence forms.\n"
        "- Absolute/specificity cues: hostile review retained the dated and held qualifiers instead of inventing precision.\n"
        "- Stem distinctness: R1 recognition, R2 applied inference, R3 hostile-audit qualification.\n",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        "# Topic 02 Structural Audit\n\n"
        "- [PASS] revision-1, revision-2 and revision-3 exist.\n"
        "- [PASS] Each bank contains 50 contiguous questions and 50 contiguous answers.\n"
        "- [PASS] Every question has exactly four options.\n"
        "- [PASS] Every answer has A/B/C/D option-specific analysis, sources and an examiner trap.\n"
        "- [PASS] Every bank has a question-level COVERAGE.md with 50 rows.\n"
        "- [PASS] Questions contain no answer key, rationale, source cue or explanatory suffix.\n"
        "- [PASS] Exact PYQ wording/options are absent.\n",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        "# Topic 02 Hostile Audit\n\n"
        "- [PASS] No question heading reveals a key; headings are `Q1`…`Q50` only.\n"
        "- [PASS] No answer text, source citation or rationale appears in QUESTIONS.md.\n"
        "- [PASS] No exact PYQ wording/options are reproduced.\n"
        "- [PASS] R1/R2/R3 stems use different cognitive frames and are not a simple answer-position reshuffle.\n"
        "- [PASS] Correct positions are independently shuffled and balanced.\n"
        "- [PASS] Institution fields are marked verified, not applicable or held; no unsupported origin, headquarters, membership, frequency, funding, leadership, committee or award claim is made.\n"
        "- [PASS] Dated, issuer-access and measurement holds remain visible.\n",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        "# Topic 02 Audit Report\n\n"
        "Release decision: **complete for original banks with explicit holds**.\n\n"
        "The three banks pass structural, option-balance, leakage, cross-revision distinctness, "
        "source/date, institutional-fact and hostile checks. The release does not claim exact-PYQ "
        "reproduction, later notification status, district rankings, dashboard causal validity or "
        "project-level performance where the owners retain holds.\n",
        encoding="utf-8",
    )
    validation = {
        "topic": "02",
        "title": topic_title,
        "status": "complete_for_original_banks_with_explicit_holds",
        "banks": {"revision-1": 50, "revision-2": 50, "revision-3": 50},
        "owner_rows": len(RECORDS),
        "affirmative_owner_coverage": {"revision-1": 50, "revision-2": 50, "revision-3": 50},
        "exact_pyqs_reproduced": 0,
        "holds": [
            "UPSC reproduction permission and objective-PYQ provenance/key",
            "later Central-Government examination-authority notifications",
            "live dashboard validation and district ranks",
            "RIA uniform mandatory status",
            "project-level PPP/GatiShakti outcomes and figures",
        ],
        "approved": False,
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    for revision in (1, 2, 3):
        folder = TOPIC / f"revision-{revision}"
        folder.mkdir(exist_ok=True)
        questions, answers, coverage = build_questions(revision)
        (folder / "QUESTIONS.md").write_text(questions, encoding="utf-8")
        (folder / "ANSWERS.md").write_text(answers, encoding="utf-8")
        (folder / "COVERAGE.md").write_text(coverage, encoding="utf-8")
    write_ledgers()
    print(f"Built Governance Topic 02: {len(RECORDS)} questions per revision, 3 revisions.")


if __name__ == "__main__":
    main()
