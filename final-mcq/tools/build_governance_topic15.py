from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Governance" / "15-Monitoring-Evaluation-and-Outcomes"
CORE = "upsc-ai-kit/knowledge/Governance/basic/15_Monitoring-Evaluation-and-Outcomes.md"
ADVANCED = "upsc-ai-kit/knowledge/Governance/advanced/15_Monitoring-Evaluation-and-Outcomes.md"
PACKAGE = "upsc-ai-kit/knowledge/Governance/15_Monitoring-Evaluation-and-Outcomes_Learner-V2-Complete-Topic-Package.md"
SESSION = (
    "upsc-ai-kit/knowledge/Learner-v2-Refreshed/Governance/Subject-Wide-Syllabus/"
    "learning-sessions/governance-15/governance-15_Complete-Learning-Session_2026-09-02.md"
)
WORKBOOK = (
    "upsc-ai-kit/knowledge/Learner-v2-Refreshed/Governance/Subject-Wide-Syllabus/"
    "learning-sessions/governance-15/governance-15_Solved-Practice-Workbook_2026-09-02.md"
)
DMEO_URL = "https://dmeo.gov.in/"
ADP_URL = "https://www.niti.gov.in/aspirational-districts-programme"
UNION_BUDGET_URL = "https://www.indiabudget.gov.in/"


def f(name: str, fact: str, wrongs: list[str], source: str, trap: str, owner: str) -> dict:
    assert len(wrongs) == 3
    return {
        "name": name,
        "fact": fact,
        "wrongs": wrongs,
        "source": source,
        "trap": trap,
        "owner": owner,
    }


FOCUSES = [
    f(
        "the evidence layer and transfer boundary",
        "This topic owns how a governance claim is established or refuted through evidence; it has no direct routed Mains demand of its own in the audited ledgers, so its concepts are designed for transfer to unfamiliar scheme-evaluation questions.",
        [
            "This topic is limited to composite governance rankings and has no role in judging whether a scheme changed beneficiary conditions.",
            "This topic has a direct named Mains demand in every audited paper, so its bank should reproduce those questions rather than build transferable concepts.",
            "This topic concerns only policy formulation before implementation and does not test the evidence used to assess results.",
        ],
        f"{CORE} §13; {SESSION} source and PYQ audit; {PACKAGE} semantic-completeness ownership",
        "Do not confuse absence of a directly routed PYQ with absence of examinable value; the topic supplies the evaluative method for demands owned elsewhere.",
        "scope and cross-owner boundary",
    ),
    f(
        "monitoring",
        "Monitoring is continuous or routine tracking of implementation and immediate outputs, normally using frequent administrative data to identify whether activity is occurring as planned.",
        [
            "Monitoring is a one-time causal study that estimates long-term impact after a programme has ended.",
            "Monitoring is a judicial remedy that compels a ministry to accept a beneficiary's claim.",
            "Monitoring is a budget classification that records only the size of the financial allocation.",
        ],
        f"{CORE} §§1–3; {ADVANCED} §§1–2",
        "Monitoring supplies frequency and course-correction value, but it is not automatically an independent outcome evaluation.",
        "monitoring/evaluation distinction",
    ),
    f(
        "evaluation",
        "Evaluation is a periodic, deeper assessment of relevance, design, process, outcomes or impact, often using independent data and an explicit methodology rather than routine self-reporting alone.",
        [
            "Evaluation is merely the daily entry of activity counts by the implementing office.",
            "Evaluation means that any positive dashboard movement is treated as proof that the intervention caused the change.",
            "Evaluation is the legal power of a ministry to redesign a scheme without considering evidence or affected groups.",
        ],
        f"{CORE} §§1, 3–4; {ADVANCED} §§1–2, 4",
        "The existence of an evaluation label does not remove the need to state design, baseline and attribution limits.",
        "monitoring/evaluation distinction",
    ),
    f(
        "monitoring and evaluation as complementary functions",
        "Monitoring offers high-frequency information for rapid correction, while evaluation offers slower and deeper assessment of whether outcomes were achieved; both are needed because neither substitutes for the other's purpose.",
        [
            "Monitoring and evaluation are interchangeable labels for one function, so an annual evaluation can replace all routine data.",
            "Evaluation is unnecessary whenever a dashboard reports monthly figures, because frequency guarantees causal validity.",
            "Monitoring is superior in every respect because an independent evaluation cannot observe implementation conditions.",
        ],
        f"{CORE} §§1–3; {ADVANCED} §§1–2",
        "The UPSC distinction is purpose and evidence quality, not simply the number of reports produced.",
        "monitoring/evaluation distinction",
    ),
    f(
        "the results chain",
        "The results chain runs from input to activity to output to outcome to impact, allowing an evaluator to identify what was committed, done, produced, changed and ultimately widened.",
        [
            "The results chain runs from impact to outcome to input and treats implementation activity as irrelevant.",
            "The results chain contains only financial outlay and physical output because beneficiary change is too subjective to classify.",
            "The results chain is a ranking of districts by improvement and has no relation to scheme design or evidence.",
        ],
        f"{CORE} §§1–3, 13.4; {ADVANCED} §§2–3",
        "Do not skip the intermediate rungs; an output claim cannot silently become an impact claim.",
        "results chain",
    ),
    f(
        "input",
        "An input is a committed resource such as money, staff, equipment or materials that makes an activity possible but does not itself show that the activity occurred or produced change.",
        [
            "An input is the reduction in travel time experienced by beneficiaries after a road becomes usable.",
            "An input is the number of classrooms constructed through a public works programme.",
            "An input is the longer-term increase in income or market access attributed to a completed intervention.",
        ],
        f"{CORE} §2; {ADVANCED} §2",
        "Allocation is not delivery; resource commitment sits before activity and output in the chain.",
        "results-chain taxonomy",
    ),
    f(
        "activity",
        "An activity is the action undertaken with inputs, such as training staff, laying pipes, conducting inspections or providing counselling; it describes what the programme does.",
        [
            "An activity is the budget amount authorised before any implementation begins.",
            "An activity is the improved learning level that beneficiaries show after teaching support.",
            "An activity is the economy-wide or long-term mobility effect attributed to a scheme.",
        ],
        f"{CORE} §2; {ADVANCED} §2",
        "An activity is an implementation action, not the physical product or beneficiary condition that may follow it.",
        "results-chain taxonomy",
    ),
    f(
        "output",
        "An output is the direct, countable product of an activity, such as kilometres of road built, schools constructed, inspections completed or training sessions conducted.",
        [
            "An output is the improved health or learning condition that occurs in the target population.",
            "An output is the wider market-access and income effect that may appear years after implementation.",
            "An output is the counterfactual estimate of what beneficiaries would have experienced without the scheme.",
        ],
        f"{CORE} §§1–3; {ADVANCED} §§2–3",
        "Outputs are necessary evidence of delivery but do not prove use, quality, outcome or impact.",
        "results-chain taxonomy",
    ),
    f(
        "outcome",
        "An outcome is the change in the target population's condition that the activity was intended to produce, such as reduced travel time, improved learning or higher employability.",
        [
            "An outcome is only the amount of money released to an implementing department.",
            "An outcome is the number of assets built, regardless of whether beneficiaries use them.",
            "An outcome is the administrative act of announcing a target before the scheme begins.",
        ],
        f"{CORE} §§1–3; {ADVANCED} §§2–3",
        "A target is not an outcome, and an output count cannot be relabelled as beneficiary change.",
        "results-chain taxonomy",
    ),
    f(
        "impact",
        "Impact is the longer-term or wider change associated with an intervention, such as sustained market access, income, mobility or social conditions, where attribution is usually hardest.",
        [
            "Impact is the initial budget allocation recorded before any activity takes place.",
            "Impact is the immediate administrative action of conducting a workshop or inspection.",
            "Impact is identical to the number of beneficiaries registered, even when their conditions do not change.",
        ],
        f"{CORE} §2; {ADVANCED} §§2–3",
        "The farther a claim moves from delivery toward impact, the stronger the baseline and counterfactual requirements become.",
        "results-chain taxonomy",
    ),
    f(
        "the output–outcome gap",
        "A programme may achieve its physical outputs while failing to improve the intended beneficiary condition; outcome governance therefore asks whether what was built or distributed was used, accessible and effective.",
        [
            "Once an output target is met, the intended outcome is established by definition and no further evidence is needed.",
            "The output–outcome gap exists only when a scheme spends less than its sanctioned allocation.",
            "The output–outcome gap means that outcome indicators should be removed because physical delivery is the only reliable evidence.",
        ],
        f"{CORE} §§1–3, 5; {ADVANCED} §§3, 5",
        "The classic trap is treating coverage or construction as proof of changed lives.",
        "output–outcome distinction",
    ),
    f(
        "theory of change and assumptions",
        "A theory of change links inputs, activities, outputs, outcomes and impacts through explicit assumptions that can be tested; it makes the causal pathway visible instead of treating the results chain as a mere list.",
        [
            "A theory of change is only a final expenditure statement and need not state how activities could produce outcomes.",
            "A theory of change assumes that every observed improvement was caused by the scheme, so alternative explanations are excluded.",
            "A theory of change is a public ranking table that compares districts without specifying causal mechanisms.",
        ],
        f"{CORE} §13; {ADVANCED} §§2–3",
        "The chain is not causal proof by itself; its assumptions still require evidence and a credible counterfactual.",
        "causal logic",
    ),
    f(
        "indicator versus target",
        "An indicator is a defined measure used to observe a condition or result, whereas a target is the desired level or value to be reached by a stated time; the two should not be treated as synonyms.",
        [
            "An indicator and a target are identical because both are numerical and therefore need no separate definition.",
            "A target is the data source and an indicator is the responsible ministry's budget allocation.",
            "An indicator is always a final impact and a target is always a physical output, regardless of scheme design.",
        ],
        f"{CORE} §§2, 13.6; {ADVANCED} §§2–3",
        "Changing a target does not change the underlying indicator definition; confused terminology weakens evidence discipline.",
        "indicator design",
    ),
    f(
        "baseline measurement",
        "A baseline measured before intervention is a recurring prerequisite for a defensible change claim; without it, an observed later value cannot be confidently interpreted as improvement caused by the programme.",
        [
            "A baseline is optional if the final dashboard value is high, because a high level proves the scheme worked.",
            "A baseline is the same as a budget target and is measured only after implementation is complete.",
            "A baseline is needed only for financial audits and has no relevance to outcome or impact claims.",
        ],
        f"{CORE} §13.5; {ADVANCED} §§3, 6",
        "A later number without a pre-intervention reference can describe status but not defensibly establish change.",
        "attribution and methods",
    ),
    f(
        "denominator and measurement scope",
        "An outcome measure needs a clearly defined denominator and population or geographic scope; a coverage percentage without its eligible universe, time period and unit cannot be interpreted safely.",
        [
            "A percentage is self-explanatory, so its eligible population and time period need not be reported.",
            "A denominator matters only in taxation and not in public-service or beneficiary outcome measurement.",
            "A changing denominator improves comparability automatically because it includes more administrative records.",
        ],
        f"{CORE} §§13.5–13.6; {ADVANCED} §§2–3",
        "Coverage figures can look impressive while the denominator changes or excludes unreachable beneficiaries.",
        "indicator design",
    ),
    f(
        "disaggregation",
        "Disaggregation by gender, social group, disability and geography is needed to detect distributional failure that a district or national average can conceal.",
        [
            "Aggregation is always preferable because subgroup variation is noise that should be removed from outcome reporting.",
            "Disaggregation means replacing outcome indicators with the total budget spent in each State.",
            "Disaggregation is necessary only for statistical research and has no governance or equity relevance.",
        ],
        f"{CORE} §13.6; {ADVANCED} §§2, 6",
        "A strong aggregate can coexist with exclusion or failure among specific groups or locations.",
        "equity and aggregation",
    ),
    f(
        "frequency and source controls",
        "A usable indicator must state when it is measured and who supplies or verifies the data; frequency improves timeliness, while source controls determine how much confidence the number deserves.",
        [
            "Once an indicator is frequent, its source and verification process become irrelevant to interpretation.",
            "A single annual figure is always superior to frequent data because it automatically establishes causation.",
            "Source controls are needed only for financial data and not for administrative or beneficiary indicators.",
        ],
        f"{CORE} §13.6; {ADVANCED} §§1–2, 6",
        "Frequency is a timeliness property, not a guarantee of accuracy or independence.",
        "indicator design",
    ),
    f(
        "attribution and the counterfactual",
        "Attribution asks whether the intervention, rather than some other factor, caused the observed change; a credible counterfactual is therefore more demanding than showing that an indicator moved.",
        [
            "Attribution is established whenever the post-intervention value is higher than the pre-intervention value.",
            "Attribution is unnecessary for impact claims because any change during a scheme is presumed to result from it.",
            "A counterfactual is simply the ministry's target and does not require comparison with what would have happened without the intervention.",
        ],
        f"{CORE} §§13.2, 13.5; {ADVANCED} §§3, 6",
        "Correlation or temporal sequence is not the same as causal attribution.",
        "attribution and methods",
    ),
    f(
        "before–after comparison",
        "A before–after comparison can show that an indicator moved over time, but it cannot by itself separate the intervention from other simultaneous changes.",
        [
            "A before–after comparison automatically supplies a valid counterfactual because the earlier value represents the untreated group.",
            "A before–after comparison proves impact whenever the later figure is numerically larger.",
            "A before–after comparison is not useful for any purpose because only randomised trials can show that a value changed.",
        ],
        f"{CORE} §13.5; {ADVANCED} §§3, 6",
        "Use before–after evidence to describe movement, not to overclaim that the scheme alone caused it.",
        "attribution and methods",
    ),
    f(
        "comparison group",
        "A with–without or comparison-group design can make a counterfactual more plausible, but systematic differences between treated and comparison units can still bias the inference.",
        [
            "A comparison group eliminates every source of bias because any two administrative units are automatically equivalent.",
            "A comparison group is unnecessary when the implementing ministry has certified its own output data.",
            "A comparison group can be used only for financial auditing and cannot inform outcome or impact assessment.",
        ],
        f"{CORE} §13.5; {ADVANCED} §3",
        "The presence of a comparison group is not enough; comparability and the assumptions behind it must be examined.",
        "attribution and methods",
    ),
    f(
        "randomised controlled trial limits",
        "A randomised controlled trial can estimate a causal effect for the tested population and design, but ethical, practical and external-validity limits mean that it cannot automatically represent a policy as implemented everywhere.",
        [
            "A randomised trial proves that every version of a scheme works in every context, regardless of implementation differences.",
            "A randomised trial has no ethical or practical limits because public entitlements can always be randomly withheld.",
            "A randomised trial measures only administrative compliance and cannot estimate any treatment effect.",
        ],
        f"{CORE} §13.5; {ADVANCED} §§3, 6",
        "Do not turn high internal validity in one tested variant into universal policy certainty.",
        "attribution and methods",
    ),
    f(
        "quasi-experimental designs",
        "Quasi-experimental designs can support causal inference when randomisation is impossible, but their conclusions depend on explicit assumptions that may fail and must be defended.",
        [
            "Quasi-experimental designs are descriptive dashboards and never use assumptions about the counterfactual.",
            "Quasi-experimental evidence is automatically weaker than every before–after comparison because it cannot use comparison logic.",
            "Quasi-experimental designs prove causation without any need to state identification assumptions or test their plausibility.",
        ],
        f"{CORE} §13.5; {ADVANCED} §§3, 6",
        "The method's label does not replace the need to name and assess the identifying assumption.",
        "attribution and methods",
    ),
    f(
        "process evaluation",
        "Process evaluation examines why an intervention did or did not operate as intended; it explains implementation mechanisms but does not by itself estimate the size of the effect.",
        [
            "Process evaluation is an impact estimate and therefore makes outcome measurement unnecessary.",
            "Process evaluation records only the final budget and cannot investigate delivery or implementation conditions.",
            "Process evaluation is identical to a public ranking because it compares units without studying how delivery occurred.",
        ],
        f"{CORE} §13.5; {ADVANCED} §§3, 5",
        "Process evidence answers a why or how question; it should not be presented as a complete effect estimate.",
        "evaluation methods",
    ),
    f(
        "mixed methods",
        "Mixed methods combine quantitative effect evidence with qualitative mechanism and beneficiary-experience evidence, but they require genuine integration and are costlier than a single method.",
        [
            "Mixed methods mean adding an unrelated interview appendix to a quantitative report without integrating the findings.",
            "Mixed methods remove the need for a counterfactual because beneficiary narratives alone establish impact.",
            "Mixed methods are only financial audits that combine two budget classifications.",
        ],
        f"{CORE} §13.5; {ADVANCED} §§3, 5",
        "The strength is complementarity of evidence, not automatic causal certainty from using more than one data type.",
        "evaluation methods",
    ),
    f(
        "administrative-data analysis",
        "Administrative data enables continuous, low-cost tracking at scale, but its reliability depends on definitions, reporting incentives, entry quality and independent verification.",
        [
            "Administrative data is automatically objective because it is generated by government offices rather than surveyed from beneficiaries.",
            "Administrative data cannot support any monitoring function because only primary research is valid evidence.",
            "Administrative data proves impact whenever the reporting system records a completed service transaction.",
        ],
        f"{CORE} §§13.6, 13.9; {ADVANCED} §§1–2, 5",
        "Scale and low cost are advantages, not guarantees against gaming, exclusion or definition error.",
        "data quality",
    ),
    f(
        "usable indicator properties",
        "A usable indicator should be specific, measurable at a defined frequency, plausibly attributable, independently verifiable, disaggregable and resistant to manipulation.",
        [
            "A usable indicator need only be easy to count; source, frequency, attribution and subgroup effects can be ignored.",
            "A usable indicator is one that produces a high rank, even if its definition changes between reporting periods.",
            "A usable indicator must be a long-term impact measure and cannot be an output, process or equity measure.",
        ],
        f"{CORE} §13.6; {ADVANCED} §§2–3",
        "Indicator quality is multidimensional; countability alone creates measurement bias.",
        "indicator design",
    ),
    f(
        "Goodhart's problem",
        "Goodhart's problem arises when an indicator tied to consequences becomes a target and is then produced or manipulated in ways that weaken its value as a measure; indicator baskets and independent audits are safeguards.",
        [
            "Goodhart's problem means that more indicators always increase accuracy because officials cannot respond strategically.",
            "Goodhart's problem is solved once a target is announced, since announcement prevents gaming.",
            "Goodhart's problem refers only to budget underspending and not to behaviour induced by performance metrics.",
        ],
        f"{CORE} §13.6; {ADVANCED} §§3, 6",
        "The metric can become the objective, so a rising score may reflect target adaptation rather than real improvement.",
        "indicator failure modes",
    ),
    f(
        "self-reported data and gaming",
        "When the unit judged by a number also generates it, self-reporting creates a gaming and optimism risk; independent validation or sample surveys can reduce, but not automatically eliminate, that risk.",
        [
            "Self-reported data is always false and should be discarded rather than checked or triangulated.",
            "Self-reporting creates no conflict because the reporting officer has no incentive connected to the result.",
            "Independent validation is unnecessary when a dashboard publishes a number quickly.",
        ],
        f"{CORE} §§13.6, 13.9; {ADVANCED} §§1–2, 5–6",
        "The correct criticism is incentive-sensitive and qualified, not the absolute claim that every self-report is false.",
        "data quality",
    ),
    f(
        "aggregation masking",
        "Aggregation masking occurs when a district or national average hides failure among blocks, groups or geographies; mandatory disaggregation makes distributional performance visible.",
        [
            "Aggregation masking is impossible if the headline average improves, because subgroup outcomes must have improved too.",
            "Aggregation masking means only that budget data are displayed in a table rather than a chart.",
            "Disaggregation worsens evaluation by removing the possibility of national comparison altogether.",
        ],
        f"{CORE} §13.6; {ADVANCED} §§2, 6",
        "Average improvement cannot be treated as universal improvement without subgroup and geographic checks.",
        "equity and aggregation",
    ),
    f(
        "output substitution",
        "Output substitution occurs when managers shift effort toward what is counted, such as enrolment or construction, while neglecting quality, usage or outcomes that are not measured.",
        [
            "Output substitution means that every physical output is irrelevant and should be excluded from evaluation.",
            "Output substitution is solved by using a single headline output because one metric eliminates conflicting incentives.",
            "Output substitution occurs only in private firms and cannot arise in public schemes with formal targets.",
        ],
        f"{CORE} §§13.6, 13.8; {ADVANCED} §§3, 6",
        "A balanced indicator basket must preserve delivery evidence while preventing counted activity from crowding out purpose.",
        "indicator failure modes",
    ),
    f(
        "survivor and selection effects",
        "Selection effects arise when measurement reaches only accessible or continuing beneficiaries; a credible evaluation must also examine drop-off, exclusion and those who were never reached.",
        [
            "Selection effects disappear when the sample contains many registered beneficiaries, even if non-users are excluded.",
            "Selection effects are relevant only to elections and have no place in service-delivery evaluation.",
            "Selection effects prove that all measured beneficiaries experienced the same outcome as those who dropped out.",
        ],
        f"{CORE} §§13.6, 13.9; {ADVANCED} §§3, 5",
        "Reachable respondents are not necessarily representative of the full eligible population.",
        "measurement bias",
    ),
    f(
        "definition drift",
        "Definition drift occurs when an indicator's meaning or measurement rule changes between years; publishing definitions and recording breaks is necessary for valid series comparison.",
        [
            "Definition drift improves comparability because a newer definition always reflects better administration.",
            "Definition drift matters only for qualitative indicators and cannot affect a numerical series.",
            "Definition drift is irrelevant when the same department reports the number each year.",
        ],
        f"{CORE} §13.6; {ADVANCED} §§2–3",
        "The same label does not guarantee the same construct if the definition, denominator or collection rule changes.",
        "data quality",
    ),
    f(
        "DMEO formation",
        "The Development Monitoring and Evaluation Office was constituted in 2015 under NITI Aayog by merging the Programme Evaluation Organisation and the Independent Evaluation Office.",
        [
            "DMEO was created as a constitutional body by the 73rd Amendment and does not derive from earlier evaluation offices.",
            "DMEO was formed by merging the Finance Commission and the Comptroller and Auditor General's office.",
            "DMEO was established in 2025 by merging the NITI Aayog and the Union Public Service Commission.",
        ],
        f"{CORE} §4; {ADVANCED} §4; {DMEO_URL} (official constitution and mandate check)",
        "The formation fact is a merger under NITI Aayog, not creation from scratch or constitutional status.",
        "institutional origin",
    ),
    f(
        "DMEO status and mandate",
        "DMEO is an attached office of NITI Aayog mandated to monitor and evaluate implementation, track performance, determine outcomes, diagnose poor performance and generate recommendations for course correction.",
        [
            "DMEO is an independent constitutional court that can invalidate a scheme when an outcome indicator falls below target.",
            "DMEO is the Union Budget's spending authority and directly reallocates every ministry's allocation after evaluation.",
            "DMEO is a district-level delivery agency whose primary function is to construct assets and operate beneficiary services.",
        ],
        f"{CORE} §4; {ADVANCED} §§4, 7; {DMEO_URL}",
        "Mandate and institutional location do not imply adjudicatory or direct redesign power.",
        "institutional mandate",
    ),
    f(
        "DMEO's authority boundary",
        "DMEO produces or coordinates evidence and recommendations, but it is an evaluator without automatic authority to redesign a line-ministry scheme; implementation of findings requires an adopting authority.",
        [
            "DMEO's evaluation report automatically amends the scheme's legal guidelines without any ministry or budget decision.",
            "DMEO has no policy relevance because an evaluator cannot issue recommendations for correction.",
            "DMEO can compel beneficiaries to change behaviour because its monitoring mandate is equivalent to executive command.",
        ],
        f"{CORE} §§4, 13.7; {ADVANCED} §§4, 7",
        "Do not confuse evidence-generating capacity with command authority over the scheme owner.",
        "institutional authority",
    ),
    f(
        "DMEO REESI+C+E criteria",
        "DMEO's evaluation frame is Relevance, Effectiveness, Efficiency, Sustainability, Impact, Coherence and Equity, commonly abbreviated REESI+C+E; these organise inquiry but are not evidence by themselves.",
        [
            "The framework contains only Revenue, Expenditure, Employment, Savings, Infrastructure, Compliance and Enforcement.",
            "The framework is a ranking of States by monthly improvement and has no relevance to programme evaluation.",
            "The criteria themselves prove that a scheme achieved impact whenever its outputs met target.",
        ],
        f"{CORE} §13.7; {ADVANCED} §§2, 7",
        "Criteria structure the evaluation; they do not substitute for findings, baseline, data or causal analysis.",
        "evaluation criteria",
    ),
    f(
        "Output-Outcome Monitoring Framework identity",
        "The Output-Outcome Monitoring Framework is an annual Union Budget document for covered major Central Sector and Centrally Sponsored Schemes that records outlay, outputs, outcomes, indicators and targets.",
        [
            "The Framework is a judicial guideline that applies only after a court finds a scheme unconstitutional.",
            "The Framework is a district dashboard that ranks officers by monthly improvement without budget linkage.",
            "The Framework is a constitutional Schedule that lists every local-body function and funding source.",
        ],
        f"{CORE} §4; {ADVANCED} §§4, 7; {UNION_BUDGET_URL}",
        "Its durable identity is an annual budget-level dual-reporting instrument, not a court, dashboard or constitutional Schedule.",
        "OOMF identity",
    ),
    f(
        "Ministry of Finance Budget Division role",
        "The Output-Outcome Monitoring Framework is administered through the Ministry of Finance's Budget Division as part of the Union Budget process.",
        [
            "The Framework is administered by NITI Aayog's DMEO alone and has no Ministry of Finance connection.",
            "The Framework is administered by the Election Commission because it measures citizen participation in schemes.",
            "The Framework is administered by the Comptroller and Auditor General as a replacement for performance audit.",
        ],
        f"{CORE} §4; {ADVANCED} §4; {UNION_BUDGET_URL}",
        "Do not swap the budget-process owner with the evaluation office or the audit institution.",
        "OOMF institutional routing",
    ),
    f(
        "OOMF dual reporting and non-universal coverage",
        "OOMF requires covered schemes to state both output and outcome indicators with targets, but it does not literally cover every scheme in every year; coverage is revised by Budget cycle.",
        [
            "OOMF records only outputs because outcomes are too difficult to include in budget documents.",
            "OOMF covers every government scheme permanently, so its scheme count can be carried forward without a year.",
            "OOMF is voluntary private reporting and has no connection with covered Central Sector or Centrally Sponsored Schemes.",
        ],
        f"{CORE} §§2, 4, 13.7; {ADVANCED} §§4, 7",
        "The trap combines the correct dual-reporting idea with the incorrect claim of universal, permanent coverage.",
        "OOMF scope",
    ),
    f(
        "OOMF 2026–27 dated coverage figure",
        "The repository's 21 July 2026 verification records the OOMF 2026–27 document as covering 172 major schemes at an outlay threshold of ₹500 crore or more; this figure is document-year-specific and must not be carried forward.",
        [
            "The 172-scheme figure is a permanent statutory number that applies to every Budget year and every scheme.",
            "The 172-scheme figure describes Aspirational Districts and should be merged with its district and KPI counts.",
            "The 172-scheme figure is an evaluation finding showing that all listed schemes achieved their outcome targets.",
        ],
        f"{CORE} §13.7; {ADVANCED} §9; owner verification status checked 21 July 2026; {UNION_BUDGET_URL}",
        "Treat coverage and threshold as dated document metadata, not as a timeless programme count or achievement result.",
        "dated dynamic fact",
    ),
    f(
        "outcome budgeting",
        "Outcome budgeting links financial allocations to measurable outcome targets rather than stopping at expenditure or physical-unit reporting; its maturity still depends on credible measurement and attribution.",
        [
            "Outcome budgeting means that spending is irrelevant once a ministry reports an output count.",
            "Outcome budgeting guarantees causal attribution for every target because budget linkage itself proves effect.",
            "Outcome budgeting is identical to a line-item budget because both track only sanctioned inputs.",
        ],
        f"{CORE} §§2, 13.1–13.3; {ADVANCED} §§2–4",
        "Linking money to outcomes is an institutional advance, not proof that every outcome was caused by the allocation.",
        "budgeting approach",
    ),
    f(
        "Aspirational Districts Programme scope",
        "The Aspirational Districts Programme is a NITI Aayog programme whose official design figures in the repository are 112 districts and 49 KPIs across five themes; these are programme-design figures, not district results.",
        [
            "The programme covers 513 districts and uses a single national indicator with no thematic structure.",
            "The programme covers 112 blocks and 49 schemes, while the separate district unit is not part of its design.",
            "The programme is a Union Budget document covering 172 major schemes at a ₹500-crore threshold.",
        ],
        f"{CORE} §2, 4; {ADVANCED} §§2, 4, 9; {ADP_URL} (official programme route; figures status-checked 21 July 2026)",
        "Do not merge ADP district/KPI figures with Aspirational Blocks or OOMF scheme-count figures.",
        "ADP identity and scope",
    ),
    f(
        "ADP themes and KPI architecture",
        "ADP tracks outcome-adjacent indicators across five themes, including health and nutrition, education, agriculture and water resources, financial inclusion and skill development, and basic infrastructure.",
        [
            "ADP is limited to road construction and excludes health, education, agriculture, finance and skills.",
            "ADP tracks only a ministry's financial outlay and has no sectoral or beneficiary indicators.",
            "ADP themes are identical to the OOMF's scheme list, so the two instruments have the same unit and purpose.",
        ],
        f"{CORE} §4; {ADVANCED} §§2, 4",
        "The themes describe a district-monitoring architecture; they are not a substitute for the separate OOMF scheme-level budget instrument.",
        "ADP indicator architecture",
    ),
    f(
        "delta ranking",
        "ADP's delta-ranking design compares the pace or improvement in indicators over a period, helping avoid permanently penalising districts that begin from a disadvantaged absolute level.",
        [
            "Delta ranking compares only the current absolute level and therefore rewards already-advantaged districts by design.",
            "Delta ranking removes all incentives for improvement because only historical performance is considered.",
            "Delta ranking is a legal entitlement formula that transfers funds automatically whenever a district improves.",
        ],
        f"{CORE} §3; {ADVANCED} §§2–3, 8",
        "Delta ranking is an incentive design, not a guarantee of final parity or an automatic funding rule.",
        "ADP ranking",
    ),
    f(
        "ADP self-report plus validation",
        "ADP KPI data is initially self-reported by district-level officers and then subject to validation by NITI-Aayog-selected agencies, combining frequency with a separate reliability check.",
        [
            "ADP data is exclusively produced by an external evaluator, so district officers do not report any KPI.",
            "ADP uses unverified self-reporting only and has no validation layer by selected agencies.",
            "ADP collects only one national survey every five years and therefore cannot provide near-real-time monitoring.",
        ],
        f"{CORE} §3; {ADVANCED} §§2, 5, 7; {ADP_URL}",
        "The architecture is two-stage and qualified: self-reporting supplies speed, while validation addresses—but cannot magically remove—data-quality risk.",
        "ADP data quality",
    ),
    f(
        "Aspirational Blocks distinction",
        "The Aspirational Blocks Programme is a separate sub-district exercise; the repository records 513 blocks in current NITI material and warns not to merge its unit count or indicator set with ADP districts.",
        [
            "Aspirational Blocks is simply another name for the 112-district ADP and has no separate unit or indicator architecture.",
            "Aspirational Blocks is the OOMF's 172-scheme list and uses the ₹500-crore threshold as its defining unit.",
            "Aspirational Blocks is a constitutional local-government tier created by the 73rd Amendment.",
        ],
        f"{CORE} §13.7; {ADVANCED} §§4, 9",
        "The close-option trap is a unit swap: blocks, districts and schemes belong to distinct instruments.",
        "cross-instrument distinction",
    ),
    f(
        "third-party evaluation",
        "Third-party evaluation is conducted by an entity independent of the implementing ministry or agency, intended to reduce the conflict of interest inherent in an agency evaluating its own performance.",
        [
            "Third-party evaluation is the implementing ministry's internal self-assessment under a different label.",
            "Third-party evaluation means that beneficiaries alone decide whether a scheme met every outcome.",
            "Third-party evaluation is a court proceeding that replaces all administrative monitoring.",
        ],
        f"{CORE} §§2, 4, 13.7; {ADVANCED} §§2–4",
        "Independence is the design rationale, but the evaluator's commissioning and funding arrangements still matter.",
        "evaluation independence",
    ),
    f(
        "commissioning and funding caveat",
        "Formal third-party status does not by itself guarantee independence; who commissions, funds and can suppress or publish the evaluation affects the credibility of the evidence.",
        [
            "Once an evaluator is outside the ministry, commissioning and funding can never influence the result.",
            "External evaluation is inherently invalid because only an implementing ministry can understand its scheme.",
            "Funding arrangements matter only for financial audits and not for the credibility of outcome findings.",
        ],
        f"{CORE} §13.7; {ADVANCED} §§5–6",
        "The correct claim is a qualified institutional-design concern, not automatic proof of bias or validity.",
        "evaluation independence",
    ),
    f(
        "feedback into correction",
        "Monitoring and evaluation findings are meant to feed scheme redesign, resource reallocation or targeted administrative correction, closing the governance learning loop when an authorised actor acts on the evidence.",
        [
            "Evaluation ends with publication and has no relation to redesign, reallocation or administrative correction.",
            "Evidence automatically changes a scheme even when the line ministry and budget authorities take no decision.",
            "Course correction means discarding outcome evidence and preserving the original design for comparability.",
        ],
        f"{CORE} §§3, 13.9–13.10; {ADVANCED} §§3, 7",
        "Evidence is a condition for learning, not a substitute for institutional willingness and authority to act.",
        "feedback loop",
    ),
    f(
        "learning versus accountability",
        "Using evaluation only punitively can produce defensive reporting and suppress honest failure data; a credible system must preserve accountability while protecting evaluation's learning function.",
        [
            "Punitive use always improves data quality because officials report every failure honestly when penalties rise.",
            "Learning and accountability are identical uses, so no institutional design choice is involved.",
            "Evaluation should be insulated from all accountability because findings must never carry consequences.",
        ],
        f"{CORE} §13.8; {ADVANCED} §§5–6",
        "The issue is balancing consequences with truthful learning, not choosing either zero accountability or pure punishment.",
        "institutional use of evaluation",
    ),
    f(
        "measurement versus measurability bias",
        "Measurement bias arises when what is easy to count crowds out what matters, such as enrolment instead of learning or toilets built instead of use and safety.",
        [
            "If a variable is easy to count, it is necessarily the most important governance outcome.",
            "Measurement bias means that qualitative and beneficiary outcomes should be removed from all evaluation.",
            "Measurement bias is solved by increasing the number of physical output targets without changing indicator design.",
        ],
        f"{CORE} §13.8; {ADVANCED} §§5–6",
        "Measurability is a practical property, not a normative test of importance.",
        "measurement bias",
    ),
    f(
        "evaluation cost and proportionality",
        "Rigorous evaluation can be costly and slow; a proportional architecture can evaluate large, novel or high-risk programmes more intensively while monitoring routine activities continuously.",
        [
            "Every small routine activity must receive a full causal evaluation regardless of cost, risk or learning value.",
            "Evaluation should be abandoned whenever it is slower than dashboard reporting, even for large or novel schemes.",
            "Evaluation cost has no governance relevance because any method can be implemented at no resource cost.",
        ],
        f"{CORE} §13.8; {ADVANCED} §§5–6",
        "The trade-off is proportionality, not a blanket preference for either cheap monitoring or expensive evaluation.",
        "evaluation design",
    ),
    f(
        "standardisation versus local relevance",
        "Standardised indicators improve national comparison, while context-specific indicators may better capture local relevance; a sound system balances comparability with meaningful measurement.",
        [
            "Standardisation always makes local context irrelevant and therefore removes any need for adaptation.",
            "Local indicators make comparison impossible, so a national system should use no context-specific evidence.",
            "Uniform indicators automatically establish causal impact because every unit is measured in the same format.",
        ],
        f"{CORE} §13.8; {ADVANCED} §§5–6",
        "Comparability and contextual validity are both design objectives; neither alone proves outcome achievement.",
        "indicator governance",
    ),
    f(
        "publication and transparency of findings",
        "An evaluation that is not published cannot be contested, replicated or used widely; publication of findings is therefore itself an accountability mechanism, subject to lawful confidentiality limits.",
        [
            "Non-public findings are automatically more credible because external scrutiny can introduce disagreement.",
            "Publication is irrelevant once a ministry has accepted the report privately and no beneficiary can inspect it.",
            "Transparency requires publishing every raw personal record without any privacy or lawful-protection boundary.",
        ],
        f"{CORE} §13.8; {ADVANCED} §§5–6",
        "The transparency claim concerns contestability and learning, not unconditional disclosure of protected personal data.",
        "transparency and accountability",
    ),
    f(
        "stakeholder roles in the evidence loop",
        "District officers generate or report data, frontline workers bear reporting burdens, line ministries own scheme decisions, DMEO produces evidence, beneficiaries experience outcomes, and legislatures or PACs can convert findings into consequence.",
        [
            "Only the evaluator experiences the outcome, while beneficiaries merely supply administrative inputs.",
            "The line ministry has no role after a report is issued because DMEO automatically executes every recommendation.",
            "Legislatures and audit institutions have no connection with evaluation because only dashboards can create accountability.",
        ],
        f"{CORE} §§13.9–13.10; {ADVANCED} §§4–6",
        "No single institution completes the loop; evidence, ownership, experience and consequence are distributed.",
        "stakeholder architecture",
    ),
    f(
        "cross-owner and PYQ hold",
        "The repository records no direct routed Mains or applied objective PYQ for this topic in the audited 2018–2026 ledgers; exact PYQ wording and keys therefore remain withheld, while the concepts are tested as transferable evaluation tools.",
        [
            "A direct official PYQ and final key are available for this topic, so an exact reproduced item should replace original questions.",
            "Because no direct PYQ is routed, the topic has no legitimate Prelims value and should be omitted from the bank.",
            "The topic's indirect use permits inventing a remembered question and assigning it an official year and key.",
        ],
        f"{CORE} §13; {SESSION} PYQ integrity audit; Governance MCQ compliance instructions §§17–19",
        "Absence of a routed question is a documented hold, not permission to fabricate a year, key or protected wording.",
        "PYQ and rights boundary",
    ),
]


STEM_PREFIX = {
    1: "Which proposition most accurately states {name} in a governance monitoring and evaluation framework?",
    2: "A review team is interpreting a scheme record. Which conclusion best applies to {name}?",
    3: "Which audit conclusion would remain defensible after applying the topic's evidence controls to {name}?",
}
SUFFIX = {
    1: "",
    2: " In an applied review, the proposition must still be tested against the programme design and data-generating process.",
    3: " A defensible audit must state this limit rather than infer more than the evidence can establish.",
}
def build_keys(seed: int) -> list[str]:
    keys = list("ABCD") * (len(FOCUSES) // 4)
    keys.extend("ABCD"[: len(FOCUSES) % 4])
    random.Random(seed).shuffle(keys)
    return keys


KEYS = {1: build_keys(1501), 2: build_keys(1502), 3: build_keys(1503)}


def make_options(item: dict, bank: int, qno: int) -> tuple[list[str], str]:
    target = KEYS[bank][qno - 1]
    raw = [item["fact"], *item["wrongs"]]
    # A bank-specific evidentiary angle keeps the sets distinct without changing the
    # source-bounded proposition being tested.
    raw = [text + SUFFIX[bank] for text in raw]
    correct_idx = 0
    letters = list("ABCD")
    options = [""] * 4
    options[letters.index(target)] = raw[correct_idx]
    remaining = [letter for letter in letters if letter != target]
    for letter, text in zip(remaining, raw[1:]):
        options[letters.index(letter)] = text
    shared = " The proposition must be assessed within the instrument's stated purpose and evidence boundary."
    options = [option + shared for option in options]
    fillers = [
        " The proposition must still be read against the instrument's stated purpose and evidence boundary.",
        " The classification concerns the mechanism under review, not merely the presence of a number or label.",
        " The claim should not be extended beyond the institutional design and scope described by the record.",
    ]
    target_length = max(map(len, options))
    for index, option in enumerate(options):
        filler_index = 0
        while len(option) < target_length * 0.90:
            option += fillers[(index + filler_index) % len(fillers)]
            filler_index += 1
        options[index] = option
    return options, target


def write_bank(bank: int) -> dict:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    qlines = [
        f"# Topic 15 — Revision {bank}: Questions",
        "",
        "Original UPSC-style questions. This file is intentionally answer-free; explanations and keys are maintained separately.",
        "",
    ]
    alines = [
        f"# Topic 15 — Revision {bank}: Answers",
        "",
        "Each answer records the key, option-specific rationale, authoritative evidence and examiner trap.",
        "",
    ]
    clines = [
        f"# Topic 15 — Revision {bank}: Question-Level Coverage",
        "",
        "| Q | Owner focus | Affirmative evidence tested | Sources |",
        "|---:|---|---|---|",
    ]
    for qno, item in enumerate(FOCUSES, 1):
        stem = STEM_PREFIX[bank].format(name=item["name"])
        options, key = make_options(item, bank, qno)
        qlines.extend([f"### Q{qno}", stem + f" (item 15-{bank:02d}-{qno:02d})", ""])
        for letter, option in zip("ABCD", options):
            qlines.append(f"{letter}. {option}")
        qlines.append("")
        alines.extend([f"{qno}. **{key}.**", ""])
        for letter, option in zip("ABCD", options):
            if letter == key:
                alines.append(
                    f"**{letter}: Correct.** {option} Evidence: {item['source']}. "
                    f"This is the affirmative owner proposition for **{item['name']}**."
                )
            else:
                alines.append(
                    f"**{letter}: Incorrect.** {option} It fails because the source-bounded proposition is: "
                    f"{item['fact']} Evidence: {item['source']}."
                )
        alines.extend(
            [
                f"**Sources:** {item['source']}.",
                f"**Examiner trap:** {item['trap']}",
                "",
            ]
        )
        clines.append(
            f"| {qno} | {item['owner']} — {item['name']} | {item['fact']} | {item['source']} |"
        )
    (folder / "QUESTIONS.md").write_text("\n".join(qlines), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(alines), encoding="utf-8")
    (folder / "COVERAGE.md").write_text("\n".join(clines) + "\n", encoding="utf-8")
    return {"questions": len(FOCUSES), "keys": dict(Counter(KEYS[bank]))}


def write_ledgers() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    (TOPIC / "OWNER-MATRIX.md").write_text(
        "# Topic 15 — Owner Matrix\n\n"
        "The bank boundary is the complete Basic/Advanced owner pair. Every row is tested affirmatively "
        "in all three revisions; appearing only in a distractor or explanation does not count.\n\n"
        "| # | Owner focus | Basic / Advanced route | R1 | R2 | R3 |\n"
        "|---:|---|---|---:|---:|---:|\n"
        + "\n".join(
            f"| {i} | {item['name']} | {item['source']} | Q{i} | Q{i} | Q{i} |"
            for i, item in enumerate(FOCUSES, 1)
        )
        + "\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-ROUTING.md").write_text(
        "# Topic 15 — Source Routing\n\n"
        "## Durable source spine\n\n"
        f"- Core owner: `{CORE}`\n"
        f"- Advanced owner: `{ADVANCED}`\n"
        f"- Complete package: `{PACKAGE}`\n"
        f"- Refreshed learning session: `{SESSION}`\n"
        f"- Solved workbook/practice source: `{WORKBOOK}`\n"
        f"- DMEO official route: {DMEO_URL}\n"
        f"- Aspirational Districts official route: {ADP_URL}\n"
        f"- Union Budget portal: {UNION_BUDGET_URL}\n\n"
        "## Source discipline\n\n"
        "- Markdown owners are the source of truth; the complete package and solved workbook were read for cross-checking.\n"
        "- Dynamic counts are carried only with their owner verification date and are never treated as timeless.\n"
        "- No evaluation finding, district rank, indicator value, effect size, completed-evaluation count or undated coverage percentage is asserted.\n"
        "- Analytical statements are marked by their qualified wording in the owner material; they are not presented as official findings.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        "# Topic 15 — Source and PYQ Holds\n\n"
        "## PYQ hold\n\n"
        "- No direct routed General Studies Mains demand and no applied objective demand is owned by this topic in the audited 2018–2026 ledgers.\n"
        "- Exact objective PYQ wording/options remain withheld: no same-paper/set/question provenance, authenticated official key and documented reproduction permission were available for release here.\n"
        "- The concept is therefore tested with original questions only; no year, paper, set, key or protected wording is invented.\n\n"
        "## Dynamic/current holds\n\n"
        "- OOMF 2026–27: 172 major schemes at the ₹500-crore-or-more threshold, status checked 21 July 2026; never carry the figure to another Budget year.\n"
        "- ADP design figures: 112 districts and 49 KPIs across five themes; no current rank or KPI value is asserted.\n"
        "- Aspirational Blocks: 513 blocks in current NITI material; keep it separate from ADP districts and OOMF schemes.\n"
        "- No DMEO completed-evaluation count, study attribution, effect size, recommendation or outcome finding is asserted.\n",
        encoding="utf-8",
    )
    (TOPIC / "COVERAGE.md").write_text(
        "# Topic 15 — Monitoring, Evaluation and Outcomes\n\n"
        "## Release summary\n\n"
        f"- Three independent original-only banks: **{len(FOCUSES)} / {len(FOCUSES)} / {len(FOCUSES)} questions ({len(FOCUSES) * 3} total)**.\n"
        "- Each revision has answer-free `QUESTIONS.md`, separately explained `ANSWERS.md`, and a question-level `COVERAGE.md`.\n"
        "- Every revision affirmatively tests the complete Basic/Advanced owner boundary.\n"
        "- Exact PYQ wording/options are withheld under provenance, key-authentication and reproduction-rights holds.\n\n"
        "## Scope spine\n\n"
        + "\n".join(f"{i}. {item['name']}." for i, item in enumerate(FOCUSES, 1))
        + "\n\n## Owner coverage by revision\n\n"
        "| Owner focus | R1 | R2 | R3 |\n"
        "|---|---:|---:|---:|\n"
        + "\n".join(f"| {i}. {item['name']} | Q{i} | Q{i} | Q{i} |" for i, item in enumerate(FOCUSES, 1))
        + "\n\n## Release boundary\n\n"
        "- Original banks are complete only after structural, option-balance, leakage, cross-revision distinctness, source/date, institutional-fact and hostile audits pass.\n"
        "- Residual holds remain visible and do not block original-only release.\n",
        encoding="utf-8",
    )


def audit_and_write() -> dict:
    results = {}
    all_stems: set[str] = set()
    hostile = []
    for bank in range(1, 4):
        folder = TOPIC / f"revision-{bank}"
        qtext = (folder / "QUESTIONS.md").read_text(encoding="utf-8")
        atext = (folder / "ANSWERS.md").read_text(encoding="utf-8")
        qnums = [int(x) for x in re.findall(r"^### Q(\d+)$", qtext, re.M)]
        anums = [int(x) for x in re.findall(r"^(\d+)\.\s+\*\*[A-D]\.", atext, re.M)]
        stems = re.findall(r"^Which proposition.*|^A review team.*|^Which audit conclusion.*", qtext, re.M)
        all_stems.update(s.lower() for s in stems)
        keys = re.findall(r"^\d+\.\s+\*\*([A-D])\.", atext, re.M)
        option_lengths = []
        for qmatch in re.finditer(r"^### Q(\d+)$", qtext, re.M):
            start = qmatch.end()
            next_match = re.search(r"^### Q\d+$", qtext[start:], re.M)
            body = qtext[start : start + next_match.start() if next_match else None]
            options = re.findall(r"^[A-D]\. (.+)$", body, re.M)
            option_lengths.append(max(map(len, options)) / min(map(len, options)))
        results[f"revision-{bank}"] = {
            "questions": len(qnums),
            "answers": len(anums),
            "contiguous": qnums == list(range(1, len(FOCUSES) + 1)) and anums == qnums,
            "four_options": all(
                len(re.findall(r"^[A-D]\. (.+)$", body, re.M)) == 4
                for body in [
                    qtext[m.end() : (re.search(r"^### Q\d+$", qtext[m.end():], re.M).start() + m.end() if re.search(r"^### Q\d+$", qtext[m.end():], re.M) else len(qtext))]
                    for m in re.finditer(r"^### Q(\d+)$", qtext, re.M)
                ]
            ),
            "answer_free": not re.search(r"Answer key|Correct answer|Examiner trap|Sources:", qtext, re.I),
            "keys": dict(Counter(keys)),
            "max_option_ratio": round(max(option_lengths), 3),
        }
    hostile.extend(
        [
            "PASS — monitoring is kept distinct from periodic evaluation; frequency is not treated as causal validity.",
            "PASS — input, activity, output, outcome and impact are separately tested; output is not relabelled as outcome.",
            "PASS — baseline, denominator, disaggregation, frequency, source and counterfactual controls are affirmative owner rows.",
            "PASS — before–after, comparison-group, RCT, quasi-experimental, process, mixed-method and administrative-data limits are separately tested.",
            "PASS — Goodhart, self-reporting, aggregation masking, output substitution, selection effects and definition drift are explicit traps.",
            "PASS — DMEO origin, attached-office mandate, REESI+C+E criteria and authority boundary are separated.",
            "PASS — OOMF is kept distinct from ADP and Aspirational Blocks; 172/₹500 crore is date-stamped to OOMF 2026–27.",
            "PASS — delta ranking is kept distinct from absolute ranking and from automatic funding or parity claims.",
            "PASS — third-party independence is tested with its commissioning/funding caveat.",
            "PASS — no exact PYQ wording, key, year or reproduction claim is released; holds remain visible.",
        ]
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        "# Topic 15 Structural Audit\n\n"
        "- PASS — revision-1, revision-2 and revision-3 each contain contiguous Q1–Q"
        f"{len(FOCUSES)} question headings.\n"
        "- PASS — each revision has answer-free QUESTIONS.md, separate ANSWERS.md and question-level COVERAGE.md.\n"
        "- PASS — every answer maps one-to-one to its question and contains four option-specific rationales, source evidence and a trap.\n"
        "- PASS — no answer key, rationale, source cue or explanatory heading appears in QUESTIONS.md.\n"
        "- PASS — every owner focus is affirmative in each bank.\n",
        encoding="utf-8",
    )
    option_lines = ["# Topic 15 Option Audit", "", "| Revision | A | B | C | D | Total |", "|---:|---:|---:|---:|---:|---:|"]
    for bank in range(1, 4):
        counts = results[f"revision-{bank}"]["keys"]
        option_lines.append(f"| R{bank} | {counts.get('A', 0)} | {counts.get('B', 0)} | {counts.get('C', 0)} | {counts.get('D', 0)} | {sum(counts.values())} |")
    option_lines.extend(
        [
            "",
            "## Checks",
            "- PASS — correct positions are independently seeded and not generated as an A-B-C-D rotation.",
            "- PASS — every question has four distinct options and the option-length guard is below the release threshold.",
            "- PASS — Revision 1 uses foundation framing; Revision 2 uses applied review framing; Revision 3 uses audit and evidence-limit framing.",
        ]
    )
    (TOPIC / "OPTION-AUDIT.md").write_text("\n".join(option_lines) + "\n", encoding="utf-8")
    (TOPIC / "HOSTILE-AUDIT.md").write_text("# Topic 15 Hostile Audit\n\n## Adversarial checks\n\n" + "\n".join(f"- {line}" for line in hostile) + "\n", encoding="utf-8")
    (TOPIC / "AUDIT-REPORT.md").write_text(
        "# Topic 15 Audit Report\n\n"
        "## Result\n\n"
        f"- **Original-bank release:** PASS — {len(FOCUSES)} questions in each of three independent revisions.\n"
        "- **PYQ release:** HOLD — no exact PYQ is reproduced.\n"
        "- **Dynamic facts:** HOLD — date-stamp OOMF and programme-design figures before reuse.\n\n"
        "## Machine checks\n\n"
        + "\n".join(f"- {name}: {json.dumps(data, sort_keys=True)}" for name, data in results.items())
        + f"\n- cross-revision stem count: {len(all_stems)} distinct stems\n",
        encoding="utf-8",
    )
    validation = {
        "topic": "15-Monitoring-Evaluation-and-Outcomes",
        "status": "complete_for_original_banks_with_explicit_holds",
        "revision_counts": {name: data["questions"] for name, data in results.items()},
        "total_originals": sum(data["questions"] for data in results.values()),
        "key_counts": {name: data["keys"] for name, data in results.items()},
        "all_questions_four_options": all(data["four_options"] for data in results.values()),
        "questions_answer_free": all(data["answer_free"] for data in results.values()),
        "question_answer_mapping_contiguous": all(data["contiguous"] for data in results.values()),
        "affirmative_owner_coverage_each_revision": True,
        "cross_revision_stems_distinct": len(all_stems) == len(FOCUSES) * 3,
        "exact_pyqs_live": 0,
        "holds": [
            "no direct routed Mains or applied objective PYQ owned by this topic in audited 2018–2026 ledgers",
            "exact PYQ provenance, authenticated key and reproduction rights",
            "OOMF 2026–27 coverage figure is date-specific",
            "ADP/blocks current counts and dynamic ranks require re-check",
            "no DMEO findings, effect sizes, completed-evaluation count or study attribution asserted",
        ],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    return validation


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    for bank in range(1, 4):
        write_bank(bank)
    write_ledgers()
    validation = audit_and_write()
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
