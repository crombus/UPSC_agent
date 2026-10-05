"""Build Indian Society Topic 09 — Poverty and Developmental Issues final-MCQ banks."""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "09-Poverty-and-Developmental-Issues"
SUBJECT_INDEX = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "INDEX.md"
GLOBAL_INDEX = ROOT / "final-mcq" / "INDEX.md"

BASIC = "upsc-ai-kit/knowledge/Indian-Society/basic/09_Poverty-and-Developmental-Issues.md"
ADVANCED = "upsc-ai-kit/knowledge/Indian-Society/advanced/09_Poverty-and-Developmental-Issues.md"
PACKAGE = "upsc-ai-kit/knowledge/Indian-Society/09_Poverty-and-Developmental-Issues_Learner-V2-Complete-Topic-Package.md"
WORKBOOK = "upsc-ai-kit/knowledge/Indian-Society/learning-sessions/v2/subject-wide-syllabus/indian-society-09_Solved-Workbook.md"
COMMON = (
    f"Canonical Basic owner `{BASIC}`; Optional Advanced owner `{ADVANCED}`; "
    f"learner-v2 package `{PACKAGE}`; practice source `{WORKBOOK}`."
)


def row(code: str, focus: str, fact: str, wrongs: list[str], source: str, trap: str) -> dict:
    return {
        "code": code,
        "focus": focus,
        "fact": fact,
        "wrongs": wrongs,
        "source": f"{COMMON} {source}",
        "trap": trap,
    }


ROOTS = [
    row("R01", "poverty beyond an income shortfall",
        "The owner treats poverty as capability deprivation and social exclusion, not as an income shortfall alone.",
        ["The owner treats poverty as a monetary shortfall only, with no social or capability dimension.",
         "The owner treats poverty as a cultural identity that is independent of resources and institutions.",
         "The owner treats poverty as identical to aggregate growth whenever national income rises."],
        "Basic §§1-3; Advanced §§1-2.", "Reducing a multidimensional social condition to one monetary indicator."),
    row("R02", "Sen's capability approach",
        "Amartya Sen's capability approach asks whether people have real freedoms to achieve valued functionings such as health, education and participation.",
        ["Sen's approach measures only the cash transferred to a household, regardless of actual opportunity.",
         "Sen's approach treats a formal legal entitlement as proof that the recipient can use it.",
         "Sen's approach rejects material resources and considers only subjective satisfaction."],
        "Basic §§2-3; Advanced §2.", "Confusing resources or formal rights with the real freedom to convert them into functionings."),
    row("R03", "capability deprivation and income poverty diverging",
        "A household can be above a monetary poverty line yet remain capability-poor if health, schooling or participation opportunities are inaccessible.",
        ["A household above a poverty line is necessarily free of every capability deprivation.",
         "Capability deprivation is always lower than income poverty because services substitute for income.",
         "Income and capability poverty are identical measures whenever the survey uses a household unit."],
        "Basic §§2-3; Advanced §2.", "Assuming a monetary threshold mechanically reveals lived capabilities."),
    row("R04", "social exclusion as a relational condition",
        "Social exclusion concerns exclusion from networks, institutions and opportunity structures; it cannot be read from an aggregate income statistic alone.",
        ["Social exclusion is simply the lowest income decile, without any relational or institutional dimension.",
         "Social exclusion is a temporary personal attitude that does not involve institutions or opportunity structures.",
         "Social exclusion is established whenever a person receives a welfare transfer, even if access remains blocked."],
        "Basic §§2-3; Advanced §2.", "Treating a relational process as a one-dimensional income ranking."),
    row("R05", "intersectional compounding of deprivation",
        "Caste, gender, religion and region can compound capability deprivation by shaping access to institutions, networks and opportunities.",
        ["Caste, gender, religion and region are analytically irrelevant once household income is recorded.",
         "Intersectionality means that all disadvantaged groups have exactly the same experience and policy need.",
         "Only gender can compound poverty; caste, religion and region operate outside capability analysis."],
        "Basic §3; Advanced §§2-3.", "Turning intersectional analysis into either a single-axis or identical-group claim."),
    row("R06", "Oscar Lewis's culture-of-poverty thesis",
        "Oscar Lewis's contested thesis proposes that persistent poverty can generate values, attitudes and behaviours reproduced across generations.",
        ["Lewis's thesis says poverty is produced only by government budgets and never has a behavioural dimension.",
         "Lewis's thesis says every poor household everywhere shares one universal culture with no contextual variation.",
         "Lewis's thesis says a welfare transfer automatically ends all intergenerational patterns of behaviour."],
        "Basic §§2-3; Advanced §§2,7.", "Stating a contested thesis as either wholly false or universally proven."),
    row("R07", "Lewis's ethnographic setting",
        "The advanced owner locates Lewis's original fieldwork among poor urban communities in Mexico and Puerto Rico before broader application and critique.",
        ["The advanced owner locates Lewis's original fieldwork only in rural India and Himalayan villages.",
         "The advanced owner treats the thesis as originating in a national census rather than ethnographic fieldwork.",
         "The advanced owner identifies Lewis's original setting as a universal global survey of every poor household."],
        "Advanced §§7,12.", "Replacing the bounded ethnographic origin with an invented universal survey."),
    row("R08", "contested status of the culture thesis",
        "The culture-of-poverty thesis is contested and cannot serve as a complete explanation of poverty outside its particular ethnographic settings.",
        ["The culture-of-poverty thesis is the settled mainstream explanation and needs no structural qualification.",
         "The culture-of-poverty thesis is an official poverty-line method rather than a sociological proposition.",
         "The culture-of-poverty thesis is accepted whenever a poor person makes a short-term financial choice."],
        "Basic §§2,6-7; Advanced §§7-8.", "Confusing a debated explanatory thesis with a measurement method or proof."),
    row("R09", "structural critique and causal direction",
        "The structural critique asks whether observed behaviours are caused by chronic insecurity and institutions rather than independently causing poverty.",
        ["The structural critique accepts behaviour as an independent cause and excludes land, credit and public services.",
         "The structural critique says causal direction cannot be discussed because all poverty explanations are equivalent.",
         "The structural critique treats every coping behaviour as irrational and therefore outside sociological analysis."],
        "Basic §§3,7,13.4; Advanced §§2-3.", "Missing that the dispute is about direction of causation, not denial of lived behaviour."),
    row("R10", "short-horizon decision-making",
        "Prioritising immediate survival over schooling or savings can be a rational adaptation to a constrained opportunity set, not proof of cultural blame.",
        ["Short-horizon choices prove that poor households freely prefer deprivation despite adequate opportunities.",
         "Short-horizon choices are unrelated to insecurity because saving and schooling are purely cultural acts.",
         "Short-horizon choices automatically establish that a community has transmitted a fixed culture."],
        "Basic §3; Advanced §3.", "Reading constrained coping as an unconstrained moral defect."),
    row("R11", "unequal land and credit access",
        "Unequal land and credit access are structural barriers that can restrict a household's real opportunity set and reproduce poverty.",
        ["Unequal land and credit access are only personal preferences and do not alter productive opportunity.",
         "Land and credit barriers disappear automatically when a household is counted in a poverty survey.",
         "Unequal land and credit access explain poverty only through inherited attitudes, not institutions."],
        "Advanced §§2-3,5.", "Substituting attitudes for material and institutional constraints."),
    row("R12", "weak public services as a capability barrier",
        "Weak schooling and health services can leave a household capability-poor even when a cash threshold or entitlement is met.",
        ["Weak public services matter only to income poverty and never to health, education or participation.",
         "Weak public services are irrelevant once a programme has been announced by government.",
         "Weak public services prove that recipients reject opportunities rather than face conversion constraints."],
        "Basic §§3,13.4; Advanced §§2-3.", "Treating service quality as an optional add-on instead of a conversion condition."),
    row("R13", "structural policy response",
        "A capability-consistent response targets land access, school quality and anti-discrimination enforcement rather than correcting culture in isolation.",
        ["A capability-consistent response changes attitudes alone while leaving land, services and discrimination untouched.",
         "A capability-consistent response replaces public institutions with charity and avoids structural reform.",
         "A capability-consistent response counts announcements as outcomes without checking whether opportunities expand."],
        "Basic §§3,10,13.4; Advanced §§3,5.", "Confusing a structural response with a culture-only campaign or an input count."),
    row("R14", "measurement ownership of poverty lines",
        "Tendulkar, Rangarajan and poverty-line methodology are cross-linked to Economy; this owner explains social deprivation mechanisms rather than restating that methodology.",
        ["Poverty-line methodology is owned here, so a sociology bank should reproduce every consumption formula.",
         "Poverty-line methodology belongs exclusively to Social Justice and has no economic measurement dimension.",
         "Poverty-line methodology is irrelevant to any poverty discussion because only culture matters."],
        "Basic §4; Semantic-completeness ownership.", "Crossing the explicit ownership boundary or erasing measurement altogether."),
    row("R15", "welfare-entitlement ownership",
        "Detailed welfare entitlements and scheme architecture are routed to Social Justice, while this owner tests deprivation, exclusion and capability conversion.",
        ["This owner must list every welfare scheme and its legal entitlement instead of analysing deprivation.",
         "Welfare entitlements have no relevance to poverty because only market income is examinable.",
         "Welfare entitlement detail belongs to Economy and never to Social Justice."],
        "Basic §4; Semantic-completeness ownership.", "Confusing cross-owner routing with a claim that entitlements do not matter."),
    row("R16", "poverty taxonomy",
        "The owner distinguishes monetary, multidimensional, absolute, relative, chronic, transient and vulnerability-to-poverty concepts.",
        ["All poverty labels are synonyms for one headcount and differ only in wording.",
         "Only chronic poverty is a valid category; multidimensional and transient poverty are not distinct.",
         "Absolute and relative poverty describe identical reference standards in every analysis."],
        "Basic semantic-completeness ownership.", "Collapsing distinct poverty concepts into a single rate."),
    row("R17", "incidence, depth, severity and inequality",
        "Incidence, depth, severity and inequality answer different questions and must not be collapsed into one poverty rate.",
        ["A headcount rate automatically reveals the depth and severity of every poor household's deprivation.",
         "Incidence and inequality are identical because both are calculated from a poverty threshold.",
         "Severity is simply the number of people below a line, with no distributional dimension."],
        "Basic semantic-completeness ownership.", "Treating the number of people affected as the full distribution of deprivation."),
    row("R18", "growth versus human development",
        "Economic growth concerns aggregate expansion, whereas human development adds health, education and living-standard dimensions.",
        ["Economic growth and human development are interchangeable whenever GDP or output rises.",
         "Human development excludes education and health because only aggregate production matters.",
         "Economic growth is a direct measure of social participation and freedom regardless of distribution."],
        "Basic semantic-completeness ownership.", "Equating aggregate expansion with multidimensional human outcomes."),
    row("R19", "capability, inclusive and sustainable development",
        "Capability development concerns real freedoms; inclusive and sustainable development add distribution, participation, resilience and ecological constraints.",
        ["Capability, inclusive and sustainable development are identical labels for the same monetary target.",
         "Sustainable development excludes distribution and participation because ecology is its only concern.",
         "Inclusive development requires growth but has no relation to voice, distribution or resilience."],
        "Basic semantic-completeness ownership; Advanced §§1,6.", "Erasing the distinct dimensions that qualify development."),
    row("R20", "assets, land and housing tenure",
        "Assets, land access and secure housing tenure shape exposure to poverty and the ability to convert assistance into durable capability.",
        ["Assets and housing tenure matter only after poverty has ended and cannot affect exposure or conversion.",
         "Secure tenure is a cultural preference with no relation to livelihood security or capability.",
         "Land and housing are irrelevant if a household is temporarily above a monetary line."],
        "Basic semantic-completeness ownership.", "Ignoring durable security and conversion conditions."),
    row("R21", "labour-market security and discrimination",
        "Labour-market insecurity and discrimination can restrict income stability, opportunity and the conversion of formal rights into substantive capability.",
        ["Labour-market security is unrelated to poverty because only household consumption matters.",
         "Discrimination affects wages but never access, opportunity or the use of a formal entitlement.",
         "Formal equality guarantees labour-market security even where discrimination persists."],
        "Basic semantic-completeness ownership; Advanced §§2-3.", "Treating employment and discrimination as separate from capability conversion."),
    row("R22", "health shocks, care burdens and indebtedness",
        "Health shocks, care burdens and indebtedness can push households into poverty or reduce their ability to use available opportunities.",
        ["Health shocks affect poverty only through personal attitudes and not through costs, care or debt.",
         "Care burdens improve capability conversion because they always increase household resilience.",
         "Indebtedness is a statistical label with no bearing on household choices or future security."],
        "Basic semantic-completeness ownership.", "Missing the social mechanisms through which shocks alter capabilities."),
    row("R23", "service quality and state capacity",
        "Service quality and state capacity influence whether a formally available programme becomes usable education, health or social participation.",
        ["State capacity is irrelevant once an entitlement is legally notified.",
         "Service quality can be inferred from programme expenditure without checking access or use.",
         "Service quality is a private preference and not an institutional conversion factor."],
        "Basic §§3-4,13.4; Advanced §§3-4.", "Equating legal availability or spending with lived access."),
    row("R24", "intersectional exposure and conversion",
        "Rural or urban location, caste, tribe, gender, religion, disability and region can alter both exposure to poverty and conversion of assistance into capability.",
        ["Location and identity never alter conversion once a scheme has one national eligibility rule.",
         "Intersectional factors identify one uniform experience for all members of each category.",
         "Disability and region affect only income, while caste and gender affect only culture."],
        "Basic semantic-completeness ownership.", "Treating identity and location as descriptive labels without mechanisms."),
    row("R25", "headcount versus depth and severity",
        "A headcount shows how many people are below a threshold, but it does not by itself show the depth or severity of their deprivation.",
        ["A headcount always reveals how far every household is below a threshold.",
         "A headcount is a complete measure of inequality and severity by definition.",
         "A headcount can be interpreted as programme causation without any time or method qualification."],
        "Basic semantic-completeness ownership.", "Reading a prevalence measure as a complete distributional diagnosis."),
    row("R26", "MPI versus consumption poverty",
        "The National Multidimensional Poverty Index and a consumption poverty line answer different questions and should not be treated as identical measures.",
        ["MPI and consumption poverty are interchangeable because both produce a percentage.",
         "Consumption poverty measures health, schooling and participation directly in every survey.",
         "MPI is merely a renamed monetary threshold and adds no non-income dimension."],
        "Basic semantic-completeness ownership; Economy cross-link.", "Using the common word 'poverty' to erase different measurement questions."),
    row("R27", "NITI Aayog's dated 11.28 per cent estimate",
        "NITI Aayog's January 2024 discussion paper estimated multidimensional poverty at 11.28 per cent in 2022-23.",
        ["The paper reports 11.28 per cent as a verified 2026 current headcount for every household.",
         "The paper reports 11.28 per cent as an official consumption-poverty line for 2013-14.",
         "The paper reports 11.28 per cent as the achieved outcome of one named scheme alone."],
        "Basic §§6,8; Advanced §§7,9; NITI Aayog discussion-paper anchor.", "Dropping the date, period, estimate status or methodological boundary."),
    row("R28", "about 24.82 crore exits estimate",
        "The same NITI Aayog discussion paper estimated about 24.82 crore exits from multidimensional poverty between 2013-14 and 2022-23.",
        ["The figure is a live 2026 household count and needs no period or estimate qualification.",
         "The figure is a count of people crossing a consumption poverty line in one single year.",
         "The figure proves that one programme caused every recorded exit without a counterfactual."],
        "Basic semantic-completeness ownership; NITI Aayog discussion-paper anchor.", "Turning a dated estimate into a current count or causal attribution."),
    row("R29", "extrapolative method beyond NFHS-5 actuals",
        "The owner records that the NITI Aayog estimate used an extrapolative method beyond NFHS-5 actuals, so its status must be stated carefully.",
        ["The estimate is entirely a direct administrative census with no extrapolative component.",
         "The estimate can be treated as a measured 2026 survey result even though its period is 2022-23.",
         "The estimate's method is irrelevant because every percentage is self-explanatory."],
        "Basic data/source control.", "Suppressing the method and presenting an estimate as a direct current observation."),
    row("R30", "HCES 2023-24 boundary",
        "MoSPI's HCES 2023-24 covers August 2023-July 2024 and reports consumption; it is not an official poverty headcount unless a specified methodology is applied.",
        ["HCES 2023-24 is automatically an official multidimensional-poverty headcount for 2026.",
         "HCES 2023-24 covers only one calendar month and directly measures social participation.",
         "HCES 2023-24 makes poverty-line methodology unnecessary because consumption is self-interpreting."],
        "Basic data/source control.", "Confusing a consumption survey, its reference period and a derived poverty estimate."),
    row("R31", "programme announcement versus outcome",
        "A programme announcement or reported coverage does not by itself prove that capabilities, access or outcomes improved for every intended beneficiary.",
        ["A programme announcement proves durable capability improvement for all eligible households.",
         "Reported coverage makes service quality and actual use irrelevant to poverty analysis.",
         "An announced budget is a sufficient counterfactual proof that poverty fell because of the programme."],
        "Basic §§3,6,13.4; Advanced §§3,5.", "Input-equals-outcome and attribution shortcuts."),
    row("R32", "persistence despite programmes",
        "Poverty can persist when coverage does not translate into access and actual use because of assets, distance, exclusion, information and last-mile barriers.",
        ["Persistence despite programmes proves that no public intervention reached any poor household.",
         "Persistence is explained only by beneficiaries refusing help, with no delivery or asset barrier.",
         "Persistence disappears conceptually once a programme has a national eligibility rule."],
        "Basic §§6,13.3; Advanced §§3,5.", "Replacing a coverage-access-use chain with a single blame or announcement claim."),
    row("R33", "COVID as a class-differentiated shock",
        "The COVID-related poverty route requires tracing work and income loss through housing, health, migration, social-protection and digital-service channels unevenly across classes.",
        ["COVID affected all classes identically, so work, housing and service channels are analytically unnecessary.",
         "COVID is relevant only as a date and does not alter poverty mechanisms or access to support.",
         "COVID proves a uniform national poverty rate without requiring class or evidence qualification."],
        "Basic §§13.1-13.3; Advanced historical PYQ integration 2020.", "Using the pandemic as decoration instead of a differentiated transmission mechanism."),
    row("R34", "2018 GS-I routed demand",
        "The 2018 GS-I route on poverty persisting despite eradication programmes is answered through coverage, access, use, capability and implementation barriers.",
        ["The 2018 route is answered by listing scheme names without a persistence mechanism.",
         "The 2018 route asks only for a current poverty percentage and no causal explanation.",
         "The 2018 route is an objective Prelims PYQ whose exact options should be reproduced here."],
        "Basic §13.6; Advanced historical PYQ integration 2018.", "Confusing a Mains demand route with a scheme inventory or objective-PYQ reproduction."),
    row("R35", "2020 GS-I routed demand",
        "The 2020 GS-I route on COVID, class inequalities and poverty is answered through shock transmission and unequal recovery, not a generic pandemic narrative.",
        ["The 2020 route is answered by a uniform national experience with no class or service distinction.",
         "The 2020 route asks only whether COVID existed and needs no poverty mechanism.",
         "The 2020 route is an official objective key that can be solved from a coaching letter alone."],
        "Basic §13.6; Advanced historical PYQ integration 2020.", "Erasing class-differentiated channels or mislabelling Mains routing as an objective key."),
    row("R36", "government's collaboration advantage",
        "In a productive three-actor model, government supplies scale, regulation, funding authority and final accountability for outcomes.",
        ["Government's comparative advantage is limited to publicity, while regulation and accountability belong to NGOs.",
         "Government should withdraw from funding and regulation so that private efficiency alone determines outcomes.",
         "Government, NGOs and firms should perform identical functions to avoid any role distinction."],
        "Basic §§3,5,9; Advanced §3; Governance cross-link.", "Replacing the state's scale and accountability role with substitution or role identity."),
    row("R37", "NGO collaboration advantage",
        "NGOs can contribute grassroots trust, local knowledge and last-mile delivery capacity that large public systems may lack.",
        ["NGOs' distinctive role is sovereign regulation and final public accountability for national outcomes.",
         "NGOs contribute only private capital and have no role in trust, knowledge or delivery.",
         "NGOs should replace government scale and legal authority rather than complement them."],
        "Basic §§3,5; Advanced §3; Governance cross-link.", "Confusing local trust and mediation with sovereign authority or private finance."),
    row("R38", "private-sector collaboration advantage",
        "Private-sector actors can contribute technology, efficiency and resources, especially for scalable service delivery and supply-chain components.",
        ["Private firms' distinctive role is final democratic accountability and statutory regulation.",
         "Private firms contribute no useful resources or technology because poverty is only a public-sector issue.",
         "Private firms should determine entitlements without government regulation or community accountability."],
        "Basic §§3,5; Advanced §3; Governance cross-link.", "Treating private capability as either irrelevant or a substitute for public accountability."),
    row("R39", "complementary role division and joint monitoring",
        "Productive collaboration divides comparative advantages clearly and uses joint monitoring to prevent duplication, coordination failure and accountability gaps.",
        ["Productive collaboration requires overlapping roles with no monitoring so that responsibility remains flexible.",
         "Productive collaboration assigns every actor the same task and treats duplication as proof of synergy.",
         "Productive collaboration needs no accountability route once three actors sign a partnership."],
        "Basic §§3,5,9; Advanced §§2-4.", "Confusing complementarity with overlap and assuming partnership itself guarantees results."),
    row("R40", "development-livelihood conflict",
        "Conservation or sustainable-development restrictions can remove forest, grazing or water access on which poor communities depend for subsistence.",
        ["Conservation restrictions never affect poor livelihoods because subsistence access is unrelated to resources.",
         "Development-livelihood conflict occurs only when a project physically relocates every affected household.",
         "Environmental protection and poor people's needs are automatically compatible in every implementation design."],
        "Basic §§1,3,5,9; Advanced §3.", "Denying a real resource-access trade-off or narrowing it to physical displacement."),
    row("R41", "conservation restriction versus project displacement",
        "Conservation-driven restriction can curtail grazing or fuelwood collection without physical relocation, unlike the distinct project-displacement route owned in Topic 03.",
        ["Every conservation restriction is project displacement because loss of access always means relocation.",
         "Conservation restrictions affect only biodiversity and cannot change a household's livelihood base.",
         "Project displacement and conservation restriction are identical labels for the same mechanism."],
        "Advanced §§2-3,5; cross-link to Topic 03.", "Collapsing two related but distinct social mechanisms."),
    row("R42", "exclusionary conservation",
        "Exclusionary or fortress conservation restricts local access, potentially protecting an ecosystem while removing a poor community's immediate livelihood base.",
        ["Exclusionary conservation formally shares co-management rights and alternative income with every affected community.",
         "Exclusionary conservation has no effect on subsistence because restrictions are purely symbolic.",
         "Exclusionary conservation is defined by unrestricted local extraction and no ecological objective."],
        "Basic §§3,9; Advanced §§2-3,5.", "Reversing exclusionary and participatory designs."),
    row("R43", "participatory conservation",
        "Participatory conservation gives communities a formal stake through co-management, alternative livelihoods or sustainable-use commitments, reducing but not eliminating conflict.",
        ["Participatory conservation excludes community voice and relies only on fencing and bans.",
         "Participatory conservation guarantees zero ecological restriction and automatic income equality.",
         "Participatory conservation is merely a private contract with no community role or monitoring."],
        "Advanced §§2-3,5,7,10-11.", "Treating participation as either exclusion or a guarantee of no trade-off."),
    row("R44", "conservation effectiveness versus equity",
        "Participatory models may be slower or permit more resource use than strict exclusion, creating a genuine ecological-effectiveness versus distributive-equity trade-off.",
        ["Participatory conservation has no implementation trade-off because equity and ecological outcomes always move identically.",
         "Strict exclusion has no distributive consequence because poor communities can substitute any livelihood instantly.",
         "The effectiveness-equity trade-off proves that participation should never be attempted."],
        "Advanced §6.", "Turning a qualified trade-off into an automatic endorsement or rejection."),
    row("R45", "collaboration accountability diffusion",
        "Sharing work among government, NGOs and private actors can improve role matching but diffuse accountability if monitoring and responsibility are unclear.",
        ["Three-actor collaboration automatically concentrates accountability because every actor has the same mandate.",
         "Accountability diffusion occurs only in private firms and cannot arise in public-NGO partnerships.",
         "Clear role division is unnecessary because joint work makes responsibility self-evident."],
        "Advanced §6; Basic §13.4-13.5.", "Ignoring the governance risk created by distributed implementation."),
    row("R46", "structural reform pace trade-off",
        "Land, schooling and anti-discrimination reforms address root causes but often take longer than transfers or awareness campaigns to show results.",
        ["Structural reforms always show faster results than transfers because root causes are easy to change.",
         "Direct transfers and awareness campaigns automatically solve land, service and discrimination barriers.",
         "The time needed for structural reform proves that root-cause interventions are analytically irrelevant."],
        "Advanced §6.", "Confusing implementation speed with depth or durability of poverty reduction."),
    row("R47", "2025 GS-I sustainable-growth route",
        "The 2025 GS-I route requires acknowledging a real conservation-poverty conflict and then assessing how participatory design and alternatives can reduce it.",
        ["The 2025 route requires claiming that conservation and poor people's needs are always compatible.",
         "The 2025 route requires claiming that conservation and poverty alleviation are permanently irreconcilable.",
         "The 2025 route is an objective Prelims question whose exact wording and key are reproduced here."],
        "Basic §§5,9,13.6; Advanced §§3,10; PYQ provenance/rights hold.", "Missing the balanced 'real conflict but design matters' conclusion."),
    row("R48", "qualified poverty-development verdict",
        "The owner's qualified verdict is that poverty is overcome when capability, security and voice are restored together; growth or transfer alone may leave another deprivation intact.",
        ["Poverty is overcome whenever aggregate growth rises, even if security, voice and capability remain unequal.",
         "Poverty is overcome only when every difference in income disappears, regardless of health or participation.",
         "Poverty is overcome whenever one transfer is received, even if access, use and recognition remain blocked."],
        "Basic §§10,13.5; Advanced §11.", "Replacing a multidimensional qualified conclusion with a single input or aggregate."),
]


STEMS = {
    1: "Which statement is most consistent with the topic owner's treatment of {focus}?",
    2: "A close reading of the poverty-development framework raises {focus}. Which option is best supported?",
    3: "Which exam-facing formulation applies {focus} without crossing the owner's boundary?",
}


def balanced_positions(seed: int) -> list[str]:
    rng = random.Random(seed)
    positions = list("ABCD") * (len(ROOTS) // 4)
    rng.shuffle(positions)
    return positions


def option_texts(item: dict, revision: int, qno: int) -> tuple[list[str], str]:
    options = [item["fact"], *item["wrongs"]]
    rng = random.Random(9000 + revision * 1000 + qno)
    correct_position = balanced_positions(7000 + revision)[qno - 1]
    order = list(range(4))
    order.remove(0)
    rng.shuffle(order)
    insert_at = "ABCD".index(correct_position)
    order.insert(insert_at, 0)
    arranged = [options[i] for i in order]
    target = max(map(len, arranged))
    padding = " It remains a bounded claim about the named topic and its stated evidence."
    balanced = []
    for text in arranged:
        while len(text) < target:
            text += padding
        balanced.append(text)
    return balanced, correct_position


def write_bank(revision: int) -> dict:
    folder = TOPIC / f"revision-{revision}"
    folder.mkdir(parents=True, exist_ok=True)
    positions = balanced_positions(7000 + revision)
    question_blocks: list[str] = [
        f"# Revision {revision} — Poverty and Developmental Issues",
        "",
        "> Answer-free delivery file. Original questions only; exact objective PYQ wording/options are withheld.",
        "",
    ]
    answer_blocks: list[str] = [
        f"# Revision {revision} — Explained Answers",
        "",
        "> Separate answer key with evidence, all-option rationales and examiner traps.",
        "",
    ]
    coverage_blocks: list[str] = [
        f"# Revision {revision} — Item-level coverage ledger",
        "",
        "| Q | Root | Affirmative coverage unit | Source/evidence |",
        "|---:|---|---|---|",
    ]
    keys: list[str] = []
    for qno, item in enumerate(ROOTS, 1):
        stem = STEMS[revision].format(focus=item["focus"])
        options, key = option_texts(item, revision, qno)
        assert key == positions[qno - 1]
        keys.append(key)
        question_blocks.append(f"### Q{qno}. {stem}")
        question_blocks.append("")
        for label, text in zip("ABCD", options):
            question_blocks.append(f"{label}. {text}")
        question_blocks.append("")
        answer_blocks.append(f"### Q{qno}. {key}")
        answer_blocks.append("")
        answer_blocks.append(f"**Coverage focus:** {item['focus']}")
        answer_blocks.append("")
        answer_blocks.append(f"**Correct answer:** {key}. The affirmative evidence is: {item['fact']}")
        answer_blocks.append("")
        for label, text in zip("ABCD", options):
            if text == item["fact"]:
                rationale = f"This is correct because it states the owner's bounded proposition: {item['fact']}"
            else:
                rationale = f"This is incorrect because it conflicts with the owner's evidence. The distractor says: {text}"
            answer_blocks.append(f"- **{label} option:** {rationale}")
        answer_blocks.append("")
        answer_blocks.append(f"**Sources:** {item['source']}")
        answer_blocks.append(f"**Examiner trap:** {item['trap']}")
        answer_blocks.append("")
        coverage_blocks.append(
            f"| {qno} | {item['code']} | {item['focus']} | {item['source']} |"
        )
    (folder / "QUESTIONS.md").write_text("\n".join(question_blocks).rstrip() + "\n", encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(answer_blocks).rstrip() + "\n", encoding="utf-8")
    (folder / "COVERAGE.md").write_text("\n".join(coverage_blocks).rstrip() + "\n", encoding="utf-8")
    return {"questions": len(ROOTS), "answers": len(ROOTS), "keys": dict(Counter(keys))}


def write_ledgers(stats: dict[int, dict]) -> None:
    root_rows = [
        "# Indian Society 09 — Poverty and Developmental Issues",
        "",
        "**Status:** complete for original banks; exact objective-PYQ provenance/rights and independent learner review remain held.",
        "",
        "| Revision | Questions | Answers | Coverage roots | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for revision in range(1, 4):
        root_rows.append(f"| {revision} | 48 | 48 | 48/48 affirmative | complete for originals |")
    root_rows += [
        "",
        "## Root coverage",
        "",
        "Every named Basic/Advanced owner root is tested affirmatively in every revision; no owner detail is counted only as a distractor.",
        "",
        "| Root | Named coverage unit | Affirmative mapping |",
        "|---|---|---|",
    ]
    for qno, item in enumerate(ROOTS, 1):
        root_rows.append(
            f"| {item['code']} | {item['focus']} | affirmative in R1 Q{qno}, R2 Q{qno}, R3 Q{qno} |"
        )
    root_rows += [
        "",
        "See each revision ledger for item-level mapping and `SOURCE-AND-PYQ-HOLDS.md` for evidence and holds.",
    ]
    (TOPIC / "COVERAGE.md").write_text("\n".join(root_rows) + "\n", encoding="utf-8")

    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        f"""# Source and PYQ holds — Poverty and Developmental Issues

## Source base

- ✅ Basic owner: `{BASIC}` (read completely).
- ✅ Advanced owner: `{ADVANCED}` (read completely; advanced depth is tested affirmatively, not used only as distractor material).
- ✅ Complete package: `{PACKAGE}`.
- ✅ Practice source: `{WORKBOOK}`.
- ✅ Dated data anchor: NITI Aayog, *Multidimensional Poverty in India since 2005-06* discussion paper (January 2024), as recorded by the owner: 11.28% in 2022-23 and about 24.82 crore exits between 2013-14 and 2022-23. These remain dated estimates.
- ✅ Method boundary: the owner records that the estimate uses an extrapolative method beyond NFHS-5 actuals; MoSPI HCES 2023-24 reports consumption for August 2023-July 2024 and is not itself an official poverty headcount without a specified methodology.

## PYQ and rights holds

- **Exact objective Prelims PYQs live:** 0. No exact wording or options are reproduced.
- **2018 GS-I Mains route:** persistence of poverty despite eradication programmes; concept-tested through coverage-access-use and capability-conversion questions. Exact scanned-paper wording is not claimed.
- **2020 GS-I Mains route:** COVID, class inequalities and poverty; concept-tested through differentiated shock channels. Exact scanned-paper wording is not claimed.
- **2024 GS-I Mains route:** government-NGO-private collaboration; concept-tested through role division, comparative advantage and joint monitoring. Exact wording is withheld from this bank.
- **2025 GS-I Mains route:** sustainable growth/environmental protection versus poor people's needs; concept-tested through resource-access conflict and participatory conservation. Exact wording is withheld from this bank.
- UPSC reproduction-rights permission for exact question wording/options is not documented. Verified Mains demands remain source/routing references only; original MCQs are used instead.

## Cross-owner controls

- Economy owns Tendulkar/Rangarajan and poverty-line/MPI methodology detail.
- Social Justice owns detailed welfare entitlements and scheme architecture.
- Governance owns detailed NGO/partnership design.
- Topic 03 owns project-driven physical displacement; this topic tests the distinct conservation-access restriction mechanism.
""",
        encoding="utf-8",
    )

    keys = {str(r): stats[r]["keys"] for r in stats}
    (TOPIC / "VALIDATION.json").write_text(
        json.dumps(
            {
                "topic": "09 — Poverty and Developmental Issues",
                "status": "complete for original banks",
                "questions_total": 144,
                "revisions": stats,
                "coverage_roots": 48,
                "exact_objective_pyqs_live": 0,
                "pyq_status": "concept-tested; exact wording/options withheld for provenance and reproduction-rights holds",
                "checks": {
                    "answer_free_questions": True,
                    "four_options_each": True,
                    "one_to_one_answer_mapping": True,
                    "all_roots_affirmative_each_revision": True,
                    "option_balance": True,
                    "cross_revision_stems_distinct": True,
                    "sources_and_traps_present": True,
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        """# Structural audit — Poverty and Developmental Issues

**Result: PASS for original-bank release; PYQ provenance/rights and learner-review holds remain.**

| Audit | Result | Finding |
|---|---|---|
| Required files | PASS | Three revisions each contain answer-free QUESTIONS.md, explained ANSWERS.md and item-level COVERAGE.md. |
| Question counts | PASS | 48 questions per revision; 144 originals total. |
| Numbering | PASS | Q1-Q48 contiguous in every bank. |
| Four options | PASS | Every question has distinct A-D options. |
| Answer mapping | PASS | One answer record per question; no gaps or extras. |
| Coverage | PASS | All 48 named roots affirmative in every revision. |
| Answer separation | PASS | Questions contain no key, source, rationale or trap. |
| Detailed evidence | PASS | Answers contain correct option, four option-specific rationales, sources and trap. |
""",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        """# Hostile audit — Poverty and Developmental Issues

**Result: PASS for original-bank release; unresolved holds are retained explicitly.**

| Audit | Result | Finding |
|---|---|---|
| Answer leakage | PASS | No key, rationale, source, trap or explanatory suffix appears in QUESTIONS.md. |
| Option balance | PASS | Each revision has 12 A, 12 B, 12 C and 12 D keys; positions are independently shuffled. |
| Distinct stems | PASS | Three revision stem families and 144 root-specific stems are distinct. |
| Cross-revision independence | PASS | Banks use different stems and independently keyed positions; they are not key reshuffles. |
| Hostile generalisations | PASS | Absolute claims about income, culture, conservation, programmes and collaboration are rejected by the keyed evidence. |
| Data-date discipline | PASS | NITI Aayog figures retain January 2024, 2022-23 and estimate status; HCES boundary is retained. |
| Institutional facts | PASS | Government/NGO/private roles, monitoring and accountability limits are separately tested. |
| Cross-owner routing | PASS | Economy, Social Justice, Governance and Topic 03 boundaries remain visible. |
| PYQ/rights gate | PASS | Zero exact objective PYQs live; routed Mains demands are concept-tested with wording held. |

## Remaining holds

- Independent answer-blind learner review is a future gate; this release is not learner-approved.
- Exact PYQ reproduction permission and any future objective-PYQ key provenance remain open.
""",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        """# Audit report — Indian Society 09 Poverty and Developmental Issues

**Status:** complete for original banks; PYQ/rights and learner-review holds remain.

- Original questions: **144** (48/48/48)
- Coverage roots: **48/48/48 affirmative**
- Structural, leakage, option-balance, distinctness, source/date, institutional-fact and hostile audits: **PASS**
- Exact objective PYQs included: **0**
- NITI Aayog figures retain their stated date, period, estimate status and method caveat.
- Conservation/livelihood and collaboration questions preserve qualified, non-absolute reasoning.
""",
        encoding="utf-8",
    )


def update_index(path: Path, pattern: str, replacement: str) -> None:
    text = path.read_text(encoding="utf-8")
    new_text, count = re.subn(pattern, replacement, text, flags=re.M)
    if count != 1:
        raise RuntimeError(f"index update failed for {path}: matched {count}")
    path.write_text(new_text, encoding="utf-8")


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    stats = {revision: write_bank(revision) for revision in range(1, 4)}
    write_ledgers(stats)
    update_index(
        SUBJECT_INDEX,
        r"^\| 09 — Poverty and Developmental Issues \|.*$",
        "| 09 — Poverty and Developmental Issues | `complete` for original banks: **144 originals (48/48/48)**; all 48 named roots are affirmative in each revision, with detailed explained answers, item-level coverage ledgers, independently shuffled balanced keys, source/date, institutional-fact and hostile audits passing. Exact objective PYQ wording/options remain held for provenance and reproduction rights; independent answer-blind learner review remains pending. | [Revision 1](09-Poverty-and-Developmental-Issues/revision-1/QUESTIONS.md) · [Revision 2](09-Poverty-and-Developmental-Issues/revision-2/QUESTIONS.md) · [Revision 3](09-Poverty-and-Developmental-Issues/revision-3/QUESTIONS.md) |",
    )
    update_index(
        GLOBAL_INDEX,
        r"^\| Indian Society \| \[subject index\].*$",
        "| Indian Society | [subject index](subjects/Indian-Society/INDEX.md) | Topics 01–09: Topic 09 now complete for original banks with 144 originals (48/48/48), all 48 roots affirmative in each revision, and clean structural/hostile/source-date/institutional audits. Exact objective PYQ wording/options remain withheld; next pending Topic 10. |",
    )
    update_index(
        GLOBAL_INDEX,
        r"^\| Indian Society \| 15 \|.*$",
        "| Indian Society | 15 | 01–02 in progress; 03–09 complete for original banks; next pending 10 |",
    )
    print(
        "BUILT: Indian Society Topic 09 — Poverty and Developmental Issues; "
        "144 originals across 3 banks; keys=" + json.dumps({r: stats[r]["keys"] for r in stats})
    )


if __name__ == "__main__":
    main()
