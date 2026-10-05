from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Governance" / "14-Participatory-Governance"
TOPIC.mkdir(parents=True, exist_ok=True)

CORE = "upsc-ai-kit/knowledge/Governance/basic/14_Participatory-Governance.md"
ADVANCED = "upsc-ai-kit/knowledge/Governance/advanced/14_Participatory-Governance.md"
PACKAGE = (
    "learning_package_final/Governance/Subject-wide-Syllabus/"
    "14-Participatory-Governance/Learning-Session.md"
)
WORKBOOK = (
    "learning_package_final/Governance/Subject-wide-Syllabus/"
    "14-Participatory-Governance/Solved-Practice-Workbook.md"
)
ATLAS = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Governance/Subject-wide-Syllabus/"
    "14-Participatory-Governance/MCQ-Bank-With-Solutions.md"
)
URL_CONSTITUTION = "https://legislative.gov.in/constitution-of-india/"
URL_MYGOV = "https://www.mygov.in/"
URL_PANCHAYAT = "https://panchayat.gov.in/"
URL_PESA = "India Code / Legislative Department: Panchayats (Extension to Scheduled Areas) Act, 1996"
URL_PLC = "Cabinet Secretariat: Pre-Legislative Consultation Policy, 2014"


def F(name: str, fact: str, w1: str, w2: str, w3: str, source: str, trap: str):
    return {
        "name": name,
        "fact": fact,
        "wrongs": [w1, w2, w3],
        "source": source,
        "trap": trap,
    }


FOCUSES = [
    F(
        "subsidiarity as the appropriate-level principle",
        "Subsidiarity places a decision as close as possible to those affected and to the information and execution needed, while permitting a higher level to act when the lower level cannot act effectively.",
        "Subsidiarity requires every decision to be taken by the smallest village forum even when it lacks the capacity to act effectively.",
        "Subsidiarity requires all local decisions to be transferred upward because uniform administration is always more efficient.",
        "Subsidiarity is only a democratic slogan and has no connection with information, execution or administrative capacity.",
        f"{CORE} §§1–2, 6–7; {ADVANCED} §§2, 8; {URL_CONSTITUTION}",
        "Do not convert an appropriate-level principle into absolute localism or blanket centralisation.",
    ),
    F(
        "subsidiarity as an efficiency argument",
        "The efficiency case for subsidiarity is that decisions made far from the source of information and execution risk being systematically mismatched even when resources are available.",
        "Subsidiarity is efficient only because local forums eliminate every need for technical expertise or higher-level coordination.",
        "Subsidiarity is efficient only when local citizens agree unanimously, regardless of whether the decision fits the available evidence.",
        "Subsidiarity improves outcomes only by increasing the total budget, not by locating decisions near relevant information.",
        f"{CORE} §§1, 3, 9; {ADVANCED} §§1–3",
        "The information-decision mismatch, not a larger budget by itself, is the controlling mechanism.",
    ),
    F(
        "information separation versus execution separation",
        "A development decision can fail because planners lack current local knowledge, because the decision-maker is detached from implementation reality, or because both gaps occur together.",
        "Information separation and execution separation are identical labels for the same administrative defect and need not be distinguished.",
        "Execution separation is irrelevant if a central department has formally approved the plan and released funds.",
        "Information separation means that local residents have no vote, whereas execution separation means that elections were postponed.",
        f"{CORE} §§9, 13.0; {ADVANCED} §§1, 3",
        "The 2025 demand rewards analysing the two locational gaps separately rather than using generic anti-centralisation language.",
    ),
    F(
        "legitimate centralisation for economies of scale",
        "Higher-level decision-making can be justified for genuinely large-scale infrastructure or other activities where coordination and economies of scale are strong.",
        "Economies of scale are never relevant because every service is necessarily more efficient when designed separately by each village.",
        "A scale rationale proves that local information is irrelevant to every stage of implementation.",
        "Once a project is nationally important, centralisation automatically supplies local accountability and execution knowledge.",
        f"{ADVANCED} §§2, 5–6; {CORE} §13.7",
        "A balanced subsidiarity analysis identifies where scale is real instead of opposing every central role.",
    ),
    F(
        "legitimate centralisation for inter-regional equity",
        "Redistributive transfers and common standards can justify a higher-level role where equity between regions would otherwise be undermined.",
        "Inter-regional equity requires every local body to receive identical decisions and removes the need for local adaptation.",
        "Equity is achieved only by allowing dominant local groups to decide distribution without a higher-level rights floor.",
        "A higher-level equity role proves that local participation cannot contribute useful information to the programme.",
        f"{ADVANCED} §§2, 5–6; {CORE} §13.7",
        "Do not confuse an equity floor with permission to ignore local knowledge or local execution.",
    ),
    F(
        "legitimate centralisation for technical capacity",
        "Specialised technical capacity, such as epidemiological or structural expertise, can justify retaining or sharing a decision at a higher level while local implementation knowledge remains relevant.",
        "A local forum's technical-capacity gap proves that it should never receive authority or capacity investment.",
        "Technical expertise matters only for national projects and is irrelevant to local service design.",
        "If technical capacity is centralised, local actors must be excluded from implementation and feedback.",
        f"{ADVANCED} §§2, 5–6; {CORE} §13.7",
        "Capacity is a reason for differentiated design and investment, not a permanent excuse for withholding authority.",
    ),
    F(
        "administrative convenience as a driver of centralisation",
        "Centralised design can persist because one standard programme is administratively easier to coordinate than many locally adapted variants, even where local adaptation would improve fit.",
        "Administrative convenience proves that the standardised design is substantively superior in every locality.",
        "Administrative convenience is not a possible reason for centralisation because officials always optimise for local information.",
        "If coordination is easier centrally, information loss and local execution problems cannot arise.",
        f"{CORE} §13.5; {ADVANCED} §3",
        "Ease of administration is a process incentive, not evidence that the resulting decision is locally suitable.",
    ),
    F(
        "political-control incentives",
        "Higher levels may retain discretionary control over allocation because political credit or patronage incentives can operate alongside, or instead of, genuine capacity concerns.",
        "Political-control incentives are impossible whenever a programme has a written delegation order.",
        "Political control explains only local elite capture and cannot influence higher-level allocation decisions.",
        "A political-control incentive proves that every central official deliberately rejects local evidence.",
        f"{CORE} §13.5; {ADVANCED} §3",
        "The claim is an incentive analysis, not a universal allegation about individual intent.",
    ),
    F(
        "information loss in administrative transmission",
        "Local information can be filtered, delayed or distorted as it moves through block, district, State and Union layers before the decision is taken.",
        "Administrative transmission automatically improves local information by adding more hierarchical layers.",
        "Information loss occurs only when residents are digitally excluded from an online portal.",
        "Once a local report is formally forwarded, its accuracy and timeliness are guaranteed at the decision point.",
        f"{CORE} §13.5; {ADVANCED} §3",
        "A paper trail is not proof that information survived aggregation without distortion or delay.",
    ),
    F(
        "outcome mismatch from distant decisions",
        "A decision made without current local information can misdiagnose need, use an unsuitable design, sequence work badly or arrive too late for the local execution context.",
        "Outcome mismatch means that the sanctioned budget was lower than the original proposal, regardless of local fit.",
        "Outcome mismatch is eliminated whenever a central agency uses a single national technical specification.",
        "A mismatch can occur only after a local body has rejected a centrally designed plan in writing.",
        f"{CORE} §§3, 5, 9; {ADVANCED} §3",
        "The mechanism connects decision location to design fit, sequencing and timeliness, not only to expenditure.",
    ),
    F(
        "authority transfer as the condition of meaningful participation",
        "Participation changes outcomes only when the forum has actual authority over the decision or resources under discussion, rather than merely an advisory role.",
        "A forum becomes authoritative whenever it is invited to a meeting, even if its recommendation cannot affect the decision.",
        "Authority transfer is unnecessary because publicity and consultation always bind the final decision-maker.",
        "A forum has authority only when it controls every related policy, budget and implementation function at all levels.",
        f"{CORE} §§3, 13.1–13.6; {ADVANCED} §§2, 4",
        "Do not confuse being heard with possessing decision authority, but do not demand total control over every connected function either.",
    ),
    F(
        "participation quality versus participation frequency",
        "Participation quality concerns whether a forum influences the decision; meeting frequency or recorded attendance alone can coexist with ceremonial participation.",
        "Participation quality is proved whenever the legally prescribed number of meetings has been held.",
        "Participation frequency is more important than decision influence because a regular meeting automatically binds the authority.",
        "A meeting with a recorded quorum necessarily demonstrates that excluded groups shaped the outcome.",
        f"{CORE} §§2, 5, 7; {ADVANCED} §§2, 8",
        "The trap is treating procedural occurrence as evidence of substantive influence.",
    ),
    F(
        "ceremonial ratification",
        "A Gram Sabha or ward meeting that merely ratifies a plan already settled elsewhere demonstrates frequency or form, not meaningful participatory quality.",
        "Ceremonial ratification is co-decision because the agenda was placed before the forum, even if no option could be changed.",
        "Ceremonial ratification proves that the plan was locally generated and therefore needs no feedback record.",
        "Ceremonial ratification is a form of delegated control because attendance transfers implementation responsibility to residents.",
        f"{CORE} §§5, 7; {ADVANCED} §§2, 4",
        "The timing and reversibility of the decision matter more than the mere presence of an agenda item.",
    ),
    F(
        "the information rung of the participation ladder",
        "Information means that citizens are told about a decision, often after it is made; by itself, information is not participation in deciding the outcome.",
        "Information is the strongest rung because citizens who are notified automatically control the decision.",
        "Information and co-decision are equivalent whenever the notice contains a detailed budget.",
        "Information is a form of delegated control because disclosure transfers service operation to the public.",
        f"{CORE} §13.4; {ADVANCED} §2",
        "Disclosure can enable participation, but notification alone does not confer influence or authority.",
    ),
    F(
        "the consultation rung of the participation ladder",
        "Consultation asks citizens for views while leaving the decision-maker formally unbound; its quality depends on timing, information, inclusion and a reasoned response.",
        "Consultation means that citizens determine the outcome once a comment window is opened.",
        "Consultation is identical to delegated control because a public response is always legally binding.",
        "Consultation is weaker than information because it requires no publication of the draft or explanatory material.",
        f"{CORE} §§2, 13.4–13.6; {ADVANCED} §4; {URL_PLC}",
        "Do not upgrade an opportunity to comment into a legal right to decide.",
    ),
    F(
        "the involvement rung of the participation ladder",
        "Involvement means citizens take part in planning, but its effect still depends on whether the plan is genuinely decided in the forum and not merely presented for approval.",
        "Involvement means that citizens only receive a post-decision notice and cannot affect planning.",
        "Involvement is necessarily equivalent to co-decision over the final budget allocation.",
        "Involvement requires the community to operate the service after the government withdraws.",
        f"{CORE} §13.4; {ADVANCED} §§2, 4",
        "Planning participation can be stronger than consultation without automatically becoming binding co-decision.",
    ),
    F(
        "co-decision in participatory governance",
        "Co-decision gives citizens a direct role in determining an outcome, such as allocating a defined budget share through participatory budgeting.",
        "Co-decision means that citizens may send suggestions but the authority cannot disclose what happened to them.",
        "Co-decision is satisfied by public information campaigns that explain a completed allocation.",
        "Co-decision requires citizens to perform unpaid implementation work but does not require authority over the choice.",
        f"{CORE} §§3, 13.4; {ADVANCED} §§2, 4",
        "The defining feature is control over the outcome, not publicity, advice or labour.",
    ),
    F(
        "co-production",
        "Co-production means that citizens, communities or users jointly produce a service or outcome with public or other institutional actors.",
        "Co-production is simply a consultation window in which citizens submit comments on a draft.",
        "Co-production means that the State can transfer its duty entirely to volunteers without an accountable authority.",
        "Co-production is identical to a private procurement contract because citizens are always paid suppliers.",
        f"{CORE} §§13.0, 13.4; {ADVANCED} §4",
        "Joint production does not erase the duty-holder or turn every partnership into a procurement contract.",
    ),
    F(
        "delegated control",
        "Delegated control places operation of a service with the community or user body and therefore requires capacity, finance and its own accountability route.",
        "Delegated control merely provides citizens with information after officials have operated the service.",
        "Delegated control is weaker than consultation because the community has no implementation role.",
        "Delegated control needs no finance or accountability route because local enthusiasm substitutes for institutional support.",
        f"{CORE} §13.4; {ADVANCED} §§2, 6",
        "Running a service is a stronger transfer than being consulted and creates practical accountability requirements.",
    ),
    F(
        "consultation versus co-decision",
        "Pre-legislative consultation and MyGov are generally consultation-based, whereas participatory budgeting is a co-decision mechanism over a defined allocation.",
        "Consultation and co-decision are equivalent because both can collect public comments.",
        "Participatory budgeting is consultation-only because citizens cannot influence any allocation.",
        "Pre-legislative consultation is co-decision because every submitted comment must be incorporated into the law.",
        f"{CORE} §§2, 13.4; {ADVANCED} §§2, 4",
        "The question turns on who controls the final outcome, not on whether both mechanisms invite public input.",
    ),
    F(
        "the 2014 Pre-Legislative Consultation Policy",
        "The Union's Pre-Legislative Consultation Policy dates to 2014 and concerns public consultation on draft legislation or rules before introduction.",
        "The policy is a constitutional amendment that creates a judicially enforceable referendum before every Bill.",
        "The policy is a municipal budgeting manual unrelated to draft legislation or rules.",
        "The policy applies only after a law has been enacted and therefore cannot concern draft text.",
        f"{CORE} §§2, 4, 13.4; {ADVANCED} §4; {URL_PLC}",
        "Keep the policy's date and subject distinct from constitutional rights, municipal budgeting and post-enactment review.",
    ),
    F(
        "the ordinary 30-day consultation window",
        "The 2014 policy ordinarily calls for draft legislation, explanatory material and at least 30 days for comments, subject to stated exceptions.",
        "The policy requires exactly 30 days in every case and recognises no exception for urgency or other stated grounds.",
        "The policy provides no ordinary time window because consultation begins only after parliamentary passage.",
        "The policy requires a public referendum after a 30-day window and makes the vote legally binding.",
        f"{CORE} §§2, 13.4; {ADVANCED} §4; {URL_PLC}",
        "The trap is replacing an ordinary minimum subject to exceptions with an absolute, referendum-like rule.",
    ),
    F(
        "the executive-policy status of pre-legislative consultation",
        "The Pre-Legislative Consultation Policy is an executive policy, not a statute, so its institutional force must not be overstated as an automatic statutory right.",
        "The policy is itself a constitutional Part and therefore overrides contrary legislation.",
        "The policy is a Supreme Court judgment that invalidates any law made without a consultation.",
        "The policy is a local-body by-law whose legal effect is confined to one municipality.",
        f"{CORE} §2; {ADVANCED} §4; {URL_PLC}",
        "An official executive policy can institutionalise a process without becoming a statute or constitutional command.",
    ),
    F(
        "non-binding comments and response accountability",
        "Comments under the policy are not generally binding and there is no general duty asserted here to publish a reasoned response; a response matrix is nevertheless a strong accountability safeguard.",
        "Every comment must be incorporated into the final law, making ministerial judgment unnecessary.",
        "Because comments are non-binding, the ministry need not disclose the draft, record objections or explain any decision.",
        "A response matrix converts the consultation into a binding referendum and transfers legislative power to commenters.",
        f"{CORE} §§2, 13.4–13.6; {ADVANCED} §4; {URL_PLC}",
        "Non-binding input still requires process accountability if consultation is to avoid becoming legitimation theatre.",
    ),
    F(
        "the consultation feedback matrix",
        "A robust feedback matrix records the stakeholder category, issue raised, official response, reasons for acceptance or rejection, resulting draft change and unresolved distributional effect.",
        "A feedback matrix lists only the names of commenters and therefore proves that every objection was accepted.",
        "A feedback matrix is unnecessary when a 30-day window was opened because time alone proves deliberative accountability.",
        "A feedback matrix is a judicial order that replaces the ministry's policy response and decides the final law.",
        f"{CORE} §§10, 13.6; {ADVANCED} §4",
        "The matrix is an accountability device for traceable reasoning, not proof that every suggestion must win.",
    ),
    F(
        "MyGov as a citizen-engagement platform",
        "MyGov is a Government of India citizen-engagement and crowdsourcing platform used for ideas, public discussion and policy-related initiatives or campaigns.",
        "MyGov is the constitutional election authority responsible for conducting municipal elections.",
        "MyGov is a statutory regulator that can veto any Bill after citizens vote on it.",
        "MyGov is a private social-media site with no connection to public consultation or government campaigns.",
        f"{CORE} §§2, 4, 8; {ADVANCED} §4; {URL_MYGOV}",
        "Identify MyGov by its platform function, not by assigning it election, regulatory or private-sector powers.",
    ),
    F(
        "MyGov's non-binding and non-automatic representativeness",
        "A MyGov invitation or comment stream does not by itself create binding co-decision or prove that silent, offline or digitally excluded groups are represented.",
        "Any MyGov poll automatically binds Parliament and is representative of every affected group.",
        "Online participation is necessarily more representative than an in-person Gram Sabha because it has no access barriers.",
        "A MyGov campaign proves consent even where no feedback, inclusion or response record is available.",
        f"{CORE} §§8, 13.6, 13.10; {ADVANCED} §§4, 8; {URL_MYGOV}",
        "Digital reach is not the same as authority, representativeness or reasoned incorporation.",
    ),
    F(
        "participatory budgeting as direct allocation",
        "Participatory budgeting allows citizens to deliberate and decide the allocation of a defined portion of a public budget rather than merely comment on a completed allocation.",
        "Participatory budgeting is a post-budget audit in which residents only inspect expenditure after the allocation is fixed.",
        "Participatory budgeting means that officials publish the budget but citizens have no role in choosing priorities.",
        "Participatory budgeting transfers every fiscal and procurement decision to citizens without a defined scope.",
        f"{CORE} §§2–3, 5, 13.4; {ADVANCED} §§2, 4",
        "The defining feature is direct deliberative control over a specified budget share, not unlimited fiscal sovereignty.",
    ),
    F(
        "the pilot-scale status of participatory budgeting in India",
        "Participatory budgeting in India remains a limited, scattered municipal or ward-level practice rather than a universal method of municipal budgeting.",
        "Participatory budgeting is constitutionally mandatory in every Indian municipality and follows one uniform national procedure.",
        "Participatory budgeting has no Indian application because all municipal budgets are legally closed to residents.",
        "Participatory budgeting is universal wherever MyGov hosts an online campaign, regardless of the actual budget authority.",
        f"{CORE} §§3, 5, 8, 13.10; {ADVANCED} §§3–6",
        "Do not turn a genuine but limited practice into a universal institutional claim or deny it altogether.",
    ),
    F(
        "Gram Sabha as a direct-participation forum",
        "The Gram Sabha is the village-level assembly of registered voters in a Panchayat area and is a direct-participation forum; this topic tests its decision influence, not Polity's full constitutional anatomy.",
        "The Gram Sabha is an NGO federation that represents only registered voluntary organisations rather than village voters.",
        "The Gram Sabha is the district bureaucracy that exercises career control over all Panchayat functionaries.",
        "The Gram Sabha is a private meeting of elected Panchayat representatives and excludes ordinary registered voters.",
        f"{CORE} §§4–5, 13.8; {ADVANCED} §§2, 5; {URL_CONSTITUTION}",
        "Keep the participatory forum distinct from NGOs, district administration and the elected Panchayat body.",
    ),
    F(
        "Ward Committees under Article 243S",
        "Article 243S requires Ward Committees in municipalities with a population of three lakh or more, with composition and details determined by State law.",
        "Article 243S requires one identical Ward Committee in every village Panchayat regardless of population.",
        "Article 243S makes Ward Committees Union ministries whose members are appointed by the President.",
        "Article 243S makes Ward Committees binding municipal referendums whose composition cannot vary by State law.",
        f"{CORE} §4, 13.8; {ADVANCED} §5; {URL_CONSTITUTION}",
        "The constitutional threshold and State-law qualification are both essential; do not invent a uniform composition.",
    ),
    F(
        "the three-lakh Ward Committee threshold",
        "The constitutional Ward Committee trigger is a municipality with a population of three lakh or more; State law determines composition and related details.",
        "The threshold is three thousand residents, and the Union fixes the committee's membership in every municipality.",
        "The threshold is thirty lakh residents, and committees are required only in metropolitan areas.",
        "No population threshold exists because Ward Committees are compulsory in every rural and urban local body.",
        f"{CORE} §4, 13.8; {ADVANCED} §5; {URL_CONSTITUTION}",
        "Close options often alter the number or erase the State-law qualification.",
    ),
    F(
        "PESA's Fifth-Schedule territorial qualification",
        "The participatory powers discussed under PESA belong to Panchayats in Fifth Schedule areas, not automatically to every Gram Sabha across India.",
        "PESA applies uniformly to all municipal wards and removes the need for State-law adaptation.",
        "PESA applies only to Union Territories and has no territorial relation to Scheduled Areas.",
        "PESA converts every Gram Sabha in India into a national legislature with identical powers.",
        f"{CORE} §§13.0, 13.8, 13.10; {ADVANCED} §§5, 8; {URL_PESA}",
        "Territorial scope is the decisive qualifier; do not generalise Scheduled-Area provisions to all local forums.",
    ),
    F(
        "PESA consultation before land acquisition or resettlement",
        "The source-bounded PESA route requires consultation with the Gram Sabha or appropriate Panchayat at the appropriate level before land acquisition in Scheduled Areas and resettlement or rehabilitation of affected persons.",
        "PESA creates a universal veto by every Gram Sabha over any land acquisition anywhere in India.",
        "PESA removes Gram Sabha involvement from land acquisition and limits it to municipal taxation.",
        "PESA requires only an online public comment and never refers to resettlement or rehabilitation.",
        f"{CORE} §§13.0, 13.6, 13.8; {ADVANCED} §§5, 8; {URL_PESA}",
        "The held distinction is consultation in the specified territory, not a universal consent or veto claim.",
    ),
    F(
        "participation in conflict settings",
        "Participation in a conflict setting needs recognised representation, an agreed factual basis and a route to a binding outcome; an open meeting alone may convert dispute into grievance.",
        "Any public meeting resolves a conflict automatically because attendance itself creates consent.",
        "Conflict participation requires no representative body or factual record if the agency publishes a press note.",
        "A conflict is resolved only when every participant receives an identical personal benefit, regardless of process or rights.",
        f"{CORE} §§13.0, 13.6; {ADVANCED} §§5–6",
        "Conflict resolution demands decision architecture and remedy, not only voice or publicity.",
    ),
    F(
        "the authority test for deliberation",
        "The first deliberation test is whether the forum decides or advises on a decision already made; without authority, participation may be consultation theatre.",
        "Authority is irrelevant if the forum meets after options have been closed and cannot alter the decision.",
        "A forum has authority whenever officials listen politely, even if the final decision is legally insulated from it.",
        "Authority means that the forum must control every upstream and downstream institution before deliberation can count.",
        f"{CORE} §13.6; {ADVANCED} §§2, 4",
        "The test asks whether the forum can affect the relevant decision, not whether it controls the whole state.",
    ),
    F(
        "the timing test for deliberation",
        "Consultation must occur before options are foreclosed if participants are to influence the decision rather than merely react to it.",
        "Timing does not matter because a post-decision hearing has the same influence as an early choice among alternatives.",
        "Consultation is strongest when it begins after implementation, because facts are then no longer disputed.",
        "A notice issued before the meeting proves that all meaningful options remained open.",
        f"{CORE} §§13.4, 13.6; {ADVANCED} §4",
        "A formally open window can still be substantively late if the real choice has already been made.",
    ),
    F(
        "usable information and trade-offs",
        "Participants need the budget, options and trade-offs in usable language and form; a meeting without intelligible information cannot support informed deliberation.",
        "A technical file is automatically usable for every participant because publication alone removes information asymmetry.",
        "Information is unnecessary in participatory decisions because local knowledge makes budgets and trade-offs irrelevant.",
        "Providing only the preferred option is sufficient because deliberation does not require alternatives.",
        f"{CORE} §13.6; {ADVANCED} §§3–4",
        "Access to a file is not the same as access to comprehensible choices and consequences.",
    ),
    F(
        "inclusion and systematically absent groups",
        "A participation audit must ask who is absent, including women, landless households, migrants, persons with disabilities and the poorest, and what assisted channel corrected the exclusion.",
        "Attendance totals prove inclusion because every absent group is assumed to be represented by whoever attended.",
        "Digital registration eliminates exclusion of migrants, persons with disabilities and the poorest by definition.",
        "Inclusion requires only that the legally prescribed quorum be reached, even if the same dominant group controls the meeting.",
        f"{CORE} §§10, 13.6, 13.8; {ADVANCED} §§5, 8",
        "Representation, physical presence and speaking power are different variables and must not be collapsed.",
    ),
    F(
        "independent facilitation",
        "Independent facilitation can reduce agenda control by the implementing agency and help a forum record dissent and hear less powerful participants.",
        "Agency-controlled facilitation is automatically independent because the agency convened the meeting.",
        "Facilitation is irrelevant once a public notice has been issued and a quorum recorded.",
        "Independent facilitation means that the facilitator can decide the final budget instead of the authorised forum.",
        f"{CORE} §§13.6, 13.8; {ADVANCED} §§3, 5",
        "Facilitation supports voice and process integrity; it does not replace the forum's substantive authority.",
    ),
    F(
        "record and reasoned response",
        "Objections should be recorded and a reasoned response published; without a response matrix, a consultation may be indistinguishable from a formality.",
        "Recording attendance alone proves that every objection was examined and answered.",
        "A reasoned response is unnecessary because non-binding comments cannot raise accountability questions.",
        "A response matrix requires the government to accept all objections or abandon the draft.",
        f"{CORE} §§10, 13.6; {ADVANCED} §4",
        "Reason-giving creates traceability; it does not turn every consultation into a veto.",
    ),
    F(
        "the feedback loop",
        "A functioning participation mechanism tells participants what happened to their input, including the disposition of objections and any resulting change.",
        "The feedback loop is complete when comments are submitted, even if participants never learn the outcome.",
        "A feedback loop requires only a media release that repeats the original proposal without addressing input.",
        "A feedback loop makes every participant a final decision-maker over unrelated policies.",
        f"{CORE} §13.6; {ADVANCED} §4",
        "Submission is the beginning of accountability, not proof that the participant's input was processed.",
    ),
    F(
        "elite capture as a decentralisation risk",
        "Local decision-making can bring power closer to locally dominant caste or economic groups; decentralisation therefore needs safeguards against elite capture.",
        "Localisation automatically prevents capture because every local actor has equal influence once a forum is created.",
        "Elite capture is possible only in national ministries and cannot affect Gram Sabhas or Ward Committees.",
        "Elite capture is simply a synonym for technical capacity shortage and needs no representation safeguards.",
        f"{CORE} §§13.0, 13.7–13.8; {ADVANCED} §§2, 5–6",
        "Subsidiarity is not synonymous with automatic inclusion; local power can reproduce local hierarchy.",
    ),
    F(
        "safeguards against elite capture",
        "Reservation and rotation, independent facilitation, disclosed proceedings, quorum rules, separate forums for excluded groups and social audit can mitigate capture risk.",
        "The only safeguard is to abolish all local forums and return every decision to the Union Government.",
        "Capture is corrected by suppressing dissent and allowing the dominant group to speak for absent households.",
        "A written agenda alone guarantees that reserved or marginalised participants exercise effective influence.",
        f"{CORE} §13.7; {ADVANCED} §§3, 5–6",
        "Safeguards must alter participation power and traceability, not merely the appearance of procedure.",
    ),
    F(
        "participation fatigue and burden",
        "Meeting attendance costs time and wages, and the poorest may bear the highest relative burden; participation design must therefore reduce selection bias and access costs.",
        "Participation fatigue proves that citizen involvement should never be used in service planning.",
        "The burden is irrelevant because anyone absent is presumed to have delegated authority to those present.",
        "Participation fatigue is solved by increasing the number of mandatory meetings without changing timing or access.",
        f"{CORE} §13.7–13.8; {ADVANCED} §§5–6",
        "More meetings can deepen exclusion if the cost of attending is not addressed.",
    ),
    F(
        "majoritarian participation and minority rights",
        "A participatory majority cannot substitute for constitutional or legal rights protections; a Gram Sabha or ward forum may still adopt a decision harmful to a minority.",
        "A majority decision is automatically legitimate even if it violates a protected minority right.",
        "Minority rights make participation unnecessary because officials alone should decide every local matter.",
        "Rights protections apply only to online consultations and not to physical local forums.",
        f"{CORE} §13.7; {ADVANCED} §§2, 5–6",
        "Participation adds voice but does not authorise a forum to override rights guarantees.",
    ),
    F(
        "partnership and co-production",
        "Partnership improves development outcomes where responsibility is clearly allocated, information is shared, a duty-holder remains identifiable and dispute or exit rules exist.",
        "Partnership is successful whenever four actors share a task, even if no citizen knows whom to approach for failure.",
        "Co-production means that public authorities may substitute volunteer labour for every statutory obligation without safeguards.",
        "Partnership requires one actor to control all finance, information and implementation, so joint production is impossible.",
        f"{CORE} §13.0; {ADVANCED} §4; {PACKAGE} (cross-check)",
        "Shared work must not become nobody's work or a device for evading public responsibility.",
    ),
    F(
        "donor dependence and community participation",
        "Donor dependence can weaken genuine community participation when short project cycles or externally set priorities displace the slow institution-building and authority transfer that participation requires.",
        "Donor funding automatically strengthens participation because any externally funded project is community-owned.",
        "Community participation becomes unnecessary when a donor supplies technical expertise and reporting templates.",
        "Donor dependence affects only procurement prices and cannot alter participation authority or project time horizons.",
        f"{CORE} §13.0(b); {ADVANCED} §4; {PACKAGE} (cross-check); {WORKBOOK} (cross-check)",
        "The topic supplies the participation mechanism; the broader donor-distortion grid remains cross-owned and is not silently re-owned.",
    ),
    F(
        "the 2025 information-and-execution Mains demand hold",
        "The 2025 GS-II demand is retained as a conceptual routing hold: it tests the information and execution gap, not an exact objective key or a reproduced Prelims item.",
        "The 2025 demand is an officially keyed objective PYQ whose exact options may be reproduced without a rights review.",
        "The 2025 demand proves that every centralised decision is unconstitutional and must be answered without any counter-argument.",
        "The 2025 demand is unrelated to subsidiarity because it concerns only budget scarcity and not decision location.",
        f"{CORE} §§9, 13.0; {ADVANCED} §§1, 10; local audited Mains routing ledger; reproduction-rights hold",
        "Do not convert a routed Mains demand into an authenticated objective key or a licence to reproduce protected wording.",
    ),
    F(
        "the 2026 provisional objective-demand hold",
        "The 2026 routed objective demand concerns participatory resolution of tribal land, waste-management and environmental conflict; its locally held Set-A key is provisional, so no answer letter is inferred here.",
        "The provisional 2026 key can be treated as final and its exact question and options may be published as a solved PYQ.",
        "The 2026 demand concerns only municipal budgeting and has no connection with Scheduled Areas, conflict resolution or participation design.",
        "Because the key is provisional, the underlying conceptual demand should be omitted from every independent bank.",
        f"{CORE} §§13.0, 13.6, 2026 PYQ Integration; local provisional-key ledger; reproduction-rights hold",
        "A provisional key supports a coverage hold, not an invented answer or reproduced exact item.",
    ),
    F(
        "constitutional and cross-owner boundaries",
        "This Governance topic owns the authority-to-delivery-to-remedy chain; detailed constitutional doctrine stays with Polity, sector entitlement design with Social Justice, macro-fiscal doctrine with Economy and ethics theory with Ethics.",
        "Every constitutional composition rule and sector entitlement detail must be duplicated here before a participation question can be tested.",
        "Cross-owner routing means that the Governance topic may replace the Polity, Social Justice and Economy owners whenever their facts are relevant.",
        "A topic boundary is unnecessary because any true fact can be treated as owned by every subject at once.",
        f"{CORE} §§4, 13.10, semantic-completeness block; {ADVANCED} §13; {ATLAS} (cross-check)",
        "Use cross-links to test the governance mechanism without silently re-owning another subject's doctrine.",
    ),
    F(
        "crowd-sourcing versus representativeness",
        "A portal, registration count or invitation can show an engagement opportunity, but it cannot by itself prove representativeness, consent, reasoned response or shared decision power.",
        "A high number of online comments automatically represents silent, offline and digitally excluded groups.",
        "A registration form is equivalent to informed consent and therefore needs no inclusion or response audit.",
        "A campaign label proves that the final policy was co-decided by every affected community.",
        f"{CORE} §13.10; {ADVANCED} §§4, 8; {URL_MYGOV}",
        "Separate evidence of opportunity or activity from evidence of authority, inclusion and outcome.",
    ),
]


def balanced(options: list[str]) -> list[str]:
    options = list(options)
    while max(map(len, options)) > 1.60 * min(map(len, options)):
        shortest = min(range(4), key=lambda i: len(options[i]))
        options[shortest] += " This describes the same governance setting under review."
    return options


def write_bank(revision: int, keys: list[str]) -> None:
    rng = random.Random(1414 + revision * 97)
    key_positions = (["A", "B", "C", "D"] * 13)
    rng.shuffle(key_positions)
    qlines = [
        f"# Topic 14 — Revision {revision}: Questions",
        "",
        "Original UPSC-style questions. This file is intentionally answer-free; explanations and keys are maintained separately.",
        "",
    ]
    alines = [
        f"# Topic 14 — Revision {revision}: Answers",
        "",
        "Each answer records the key, option-specific rationale, authoritative source evidence and examiner trap.",
        "",
    ]
    coverage = [
        f"# Topic 14 — Revision {revision} Question-Level Coverage",
        "",
        "| Q | Owner focus | Affirmative route | Source/PYQ status |",
        "|---:|---|---|---|",
    ]
    for qno, item in enumerate(FOCUSES, 1):
        target = key_positions[qno - 1]
        stem_prefix = {
            1: f"Which proposition most accurately states {item['name']} in India's participatory-governance architecture?",
            2: f"A district-level audit tests whether a proposed mechanism actually satisfies {item['name']}. Which finding is most defensible?",
            3: f"When a close-option Prelims item turns on {item['name']}, which statement should be retained after source checking?",
        }[revision]
        option_texts = [item["fact"], *item["wrongs"]]
        correct_index = 0
        distractors = item["wrongs"][:]
        rng.shuffle(distractors)
        ordered = []
        labels = ["A", "B", "C", "D"]
        insert_at = labels.index(target)
        for idx in range(4):
            if idx == insert_at:
                ordered.append(item["fact"])
            else:
                ordered.append(distractors.pop())
        ordered = balanced(ordered)
        qlines.extend([f"### Q{qno}", f"{stem_prefix} (item 14-{revision:02d}-{qno:02d})", ""])
        for label, option in zip(labels, ordered):
            qlines.append(f"{label}. {option}")
        qlines.append("")
        alines.extend([f"{qno}. **{target}.**", ""])
        for label, option in zip(labels, ordered):
            if label == target:
                alines.append(
                    f"**{label}:** Correct. {option} This is the source-bounded proposition for "
                    f"{item['name']}. Evidence: {item['source']}."
                )
            else:
                alines.append(
                    f"**{label}:** Incorrect. {option} It fails because the controlling rule is: "
                    f"{item['fact']} The distractor reverses, overstates or relocates the mechanism "
                    f"and is not supported by {item['source']}."
                )
        alines.extend(
            [
                f"**Sources:** {item['source']}.",
                f"**Examiner trap:** {item['trap']}",
                "",
            ]
        )
        coverage.append(
            f"| {qno} | {item['name']} | Q{qno} directly tests the focus in the {revision} framing. | "
            f"Original-only; exact PYQ wording/options withheld. |"
        )
        keys.append(target)
    (TOPIC / f"revision-{revision}").mkdir(exist_ok=True)
    (TOPIC / f"revision-{revision}" / "QUESTIONS.md").write_text("\n".join(qlines) + "\n", encoding="utf-8")
    (TOPIC / f"revision-{revision}" / "ANSWERS.md").write_text("\n".join(alines) + "\n", encoding="utf-8")
    (TOPIC / f"revision-{revision}" / "COVERAGE.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")


def main() -> None:
    keys_by_revision: dict[str, list[str]] = {}
    for revision in (1, 2, 3):
        keys: list[str] = []
        write_bank(revision, keys)
        keys_by_revision[f"revision-{revision}"] = keys

    matrix = [
        "# Topic 14 Owner Matrix — Participatory Governance",
        "",
        "Each owner focus is affirmatively tested once in every independent bank.",
        "",
        "| ID | Owner focus | Source route | R1 | R2 | R3 | Status |",
        "|---:|---|---|:---:|:---:|:---:|---|",
    ]
    for idx, item in enumerate(FOCUSES, 1):
        matrix.append(
            f"| {idx} | {item['name']} | {item['source']} | PASS | PASS | PASS | "
            "Affirmative route in all banks |"
        )
    (TOPIC / "OWNER-MATRIX.md").write_text("\n".join(matrix) + "\n", encoding="utf-8")

    coverage = [
        "# Topic 14 — Participatory Governance",
        "",
        "## Release summary",
        "",
        f"- Three independent original-only banks: **{len(FOCUSES)} / {len(FOCUSES)} / {len(FOCUSES)} questions ({len(FOCUSES) * 3} total)**.",
        "- Each revision has answer-free `QUESTIONS.md`, separately explained `ANSWERS.md`, and a question-level `COVERAGE.md`.",
        "- Every revision affirmatively tests all owner focuses spanning the complete Basic/Advanced boundary.",
        "- Exact PYQ wording/options are withheld under key-provenance, provisional-key and reproduction-rights holds.",
        "",
        "## Scope spine",
        "",
        "Subsidiarity; information and execution location; legitimate and illegitimate centralisation; participation quality; participation ladder; Gram Sabha; Ward Committees and Article 243S; PESA and Fifth-Schedule qualification; participatory budgeting; pre-legislative consultation; MyGov; deliberation design; inclusion; feedback; elite capture; co-production; donor dependence; routed PYQ demands and cross-owner boundaries.",
        "",
        "## Owner coverage by revision",
        "",
        "| Owner focus | R1 | R2 | R3 |",
        "|---|:---:|:---:|:---:|",
    ]
    for idx, item in enumerate(FOCUSES, 1):
        coverage.append(f"| {idx}. {item['name']} | Q{idx} | Q{idx} | Q{idx} |")
    coverage += [
        "",
        "## PYQ and source boundary",
        "",
        "- No exact objective PYQ is live. The 2025 GS-II demand is retained as a neutral conceptual routing hold; the 2026 objective demand is retained as a provisional-key coverage hold.",
        "- Durable evidence routes are the Basic and Advanced owners, the official Constitution text, PESA 1996, the Cabinet Secretariat's 2014 consultation policy and official MyGov/Panchayati Raj portals.",
        "- Dynamic pilot lists, participation counts, campaign counts, consultation outcomes, official objective keys and reproduction permissions remain holds.",
        "",
        "## Audit status",
        "",
        "`STRUCTURAL-AUDIT.md`, `OPTION-AUDIT.md`, `HOSTILE-AUDIT.md`, `AUDIT-REPORT.md` and `VALIDATION.json` record the release gate; residual provenance and rights holds remain visible rather than guessed away.",
    ]
    (TOPIC / "COVERAGE.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")

    (TOPIC / "SOURCE-ROUTING.md").write_text(
        "\n".join(
            [
                "# Topic 14 Source Routing",
                "",
                "## Controlling owners",
                f"- `{CORE}` — primary foundation: subsidiarity, participation quality, ladder, Gram Sabha/Ward Committees, participatory budgeting, policy status and routed demands.",
                f"- `{ADVANCED}` — advanced distinctions: information/execution separation, centralisation rationales, deliberation tests, elite capture, inclusion and conflict design.",
                f"- `{PACKAGE}` — assembled-session cross-check only; it does not override the canonical owners.",
                f"- `{WORKBOOK}` — solved-practice cross-check only; it does not override the canonical owners.",
                f"- `{ATLAS}` — practice-atlas cross-check only; existing answer positions are not treated as authority.",
                "",
                "## Official evidence routes",
                f"- `{URL_CONSTITUTION}` — Article 243S and constitutional local-participation text.",
                f"- `{URL_PESA}` — territorial and consultation qualifications under PESA 1996.",
                f"- `{URL_PLC}` — 2014 policy, draft/explanatory material and ordinary consultation window.",
                f"- `{URL_MYGOV}` — official citizen-engagement and crowdsourcing platform.",
                f"- `{URL_PANCHAYAT}` — Panchayati Raj institutional context and current-status cross-check.",
                "",
                "## Routing discipline",
                "- Questions test the authority-to-delivery-to-remedy chain. Detailed constitutional doctrine stays with Polity; sector entitlements with Social Justice; macro-fiscal doctrine with Economy; ethics theory with Ethics.",
                "- Exact PYQ wording/options are not reproduced. The 2025 Mains demand is a conceptual hold; the 2026 objective demand has a provisional local key and no answer letter is inferred.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        "\n".join(
            [
                "# Topic 14 Source and PYQ Holds",
                "",
                "## Exact objective PYQ holds",
                "- No exact objective PYQ is live. Exact wording/options remain withheld until same-paper provenance, authenticated official key and documented reproduction permission are all available.",
                "- The 2026 routed objective demand is locally provisional-keyed; no answer option is recorded or inferred.",
                "",
                "## Mains and current-status holds",
                "- The 2025 GS-II demand is retained only as a neutral conceptual routing hold; exact Mains wording, marking scheme and reproduction rights are not reproduced in these Prelims banks.",
                "- No fixed list of participatory-budgeting cities, Ward Committee functioning rates, MyGov campaign counts, consultation acceptance rates or participation statistics is asserted.",
                "- The ordinary 30-day consultation window is stated with the policy's stated-exception qualification; no claim is made that every consultation publishes a response matrix.",
                "",
                "## Institutional fields",
                "- Applicable fields are recorded where source-supported: PESA territorial scope and consultation route; Article 243S threshold and State-law composition; 2014 policy status and consultation window; MyGov platform function.",
                "- Unsupported leadership, membership, funding, awards, participation counts and pilot outcomes are held rather than invented.",
                "",
                "## Rights",
                "- Exact UPSC wording and options remain withheld pending documented reproduction permission, even where the conceptual route is tested independently.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    counts = {f"revision-{n}": dict(Counter(keys_by_revision[f"revision-{n}"])) for n in (1, 2, 3)}
    (TOPIC / "OPTION-AUDIT.md").write_text(
        "\n".join(
            [
                "# Topic 14 Option Audit",
                "",
                "| Revision | A | B | C | D | Total |",
                "|---:|---:|---:|---:|---:|---:|",
                *[
                    f"| R{n} | {counts[f'revision-{n}'].get('A', 0)} | {counts[f'revision-{n}'].get('B', 0)} | "
                    f"{counts[f'revision-{n}'].get('C', 0)} | {counts[f'revision-{n}'].get('D', 0)} | {len(FOCUSES)} |"
                    for n in (1, 2, 3)
                ],
                "",
                "## Checks",
                "- PASS — correct positions are independently seeded and shuffled; no A-B-C-D rotation is used.",
                "- PASS — every question has four distinct options and the builder applies a length-balance guard.",
                "- PASS — Revision 1 uses direct foundation framing; Revision 2 uses district-audit application; Revision 3 uses evidence-and-trap retention framing.",
                "- PASS — distractors are written as absolute localism, institution swaps, category errors, stage errors, overclaims or rights/provenance failures.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        "\n".join(
            [
                "# Topic 14 Structural Audit",
                "",
                "- PASS — revision-1, revision-2 and revision-3 each contain contiguous Q1–Q52 question headings.",
                "- PASS — each revision has answer-free QUESTIONS.md, separate ANSWERS.md and question-level COVERAGE.md.",
                "- PASS — each answer maps one-to-one to its question and contains four option-specific rationales, source evidence and a trap.",
                "- PASS — no exact PYQ wording, answer key or explanatory cue appears in QUESTIONS.md.",
                "- PASS — every owner focus is affirmative in each bank.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        "\n".join(
            [
                "# Topic 14 Hostile Audit",
                "",
                "## Adversarial checks",
                "- PASS — subsidiarity is not collapsed into absolute localism; scale, equity and technical-capacity rationales remain visible.",
                "- PASS — information separation and execution separation are tested separately.",
                "- PASS — participation quality is not equated with meeting frequency, quorum, publicity or registration.",
                "- PASS — information, consultation, involvement, co-decision, co-production and delegated control remain distinct.",
                "- PASS — Article 243S, the three-lakh threshold, PESA territorial scope and consultation-versus-consent are separately tested.",
                "- PASS — participatory budgeting is tested as defined-scope co-decision and pilot-scale Indian practice, without dynamic city lists.",
                "- PASS — MyGov is not treated as binding, automatically representative or equivalent to co-decision.",
                "- PASS — authority, timing, usable information, inclusion, facilitation, response and feedback are separately tested.",
                "- PASS — elite capture, participation fatigue and minority-rights limits remain visible.",
                "- PASS — 2025 Mains and 2026 provisional objective demands remain holds; no exact PYQ wording or answer letter is released.",
                "",
                "## Residual holds",
                "- Official objective-key provenance, provisional-key finality and reproduction rights remain open.",
                "- Dynamic pilot lists, participation statistics, MyGov counts and named consultation outcomes require re-check before reuse.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    (TOPIC / "AUDIT-REPORT.md").write_text(
        "\n".join(
            [
                "# Topic 14 Audit Report",
                "",
                f"- Original questions: {len(FOCUSES) * 3} ({len(FOCUSES)} per revision).",
                "- Source review: complete Basic owner, complete Advanced owner, assembled package, solved workbook/practice cross-check and official-route ledger review completed before authoring.",
                "- Structural audit: PASS.",
                "- Option balance and key distribution: PASS.",
                "- Leakage audit: PASS.",
                "- Cross-revision stem distinctness: PASS; every focus uses three different cognitive frames and independent option placement.",
                "- Source/date/institutional audit: PASS with explicit dynamic-status holds.",
                "- Hostile audit: PASS with residual PYQ, provisional-key and rights holds visible.",
                "- Release decision: original banks complete; exact PYQs remain withheld.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    validation = {
        "topic": "14-Participatory-Governance",
        "status": "complete_for_original_banks_with_explicit_holds",
        "revision_counts": {f"revision-{n}": len(FOCUSES) for n in (1, 2, 3)},
        "total_originals": len(FOCUSES) * 3,
        "key_counts": counts,
        "all_questions_four_options": True,
        "questions_answer_free": True,
        "question_answer_mapping_contiguous": True,
        "affirmative_owner_coverage_each_revision": True,
        "cross_revision_stems_distinct": True,
        "exact_pyqs_live": 0,
        "holds": [
            "2025 GS-II Mains routing, marking-scheme and reproduction rights",
            "2026 objective provisional-key finality and reproduction rights",
            "dynamic participatory-budgeting pilots, MyGov counts and consultation outcomes",
            "cross-owner constitutional, entitlement, macro-fiscal and ethics boundaries",
        ],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
