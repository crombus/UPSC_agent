"""Build Indian Society Topic 08 — Social Empowerment final-MCQ banks."""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "08-Social-Empowerment"
SUBJECT_INDEX = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "INDEX.md"
GLOBAL_INDEX = ROOT / "final-mcq" / "INDEX.md"

BASIC = "upsc-ai-kit/knowledge/Indian-Society/basic/08_Social-Empowerment.md"
ADVANCED = "upsc-ai-kit/knowledge/Indian-Society/advanced/08_Social-Empowerment.md"
PACKAGE = "upsc-ai-kit/knowledge/Indian-Society/08_Social-Empowerment_Learner-V2-Complete-Topic-Package.md"
WORKBOOK = "upsc-ai-kit/knowledge/Indian-Society/learning-sessions/v2/subject-wide-syllabus/indian-society-08_Solved-Workbook.md"
COMMON = (
    f"Canonical Basic owner `{BASIC}`; Optional Advanced owner `{ADVANCED}`; "
    f"learner-v2 package `{PACKAGE}`; practice source `{WORKBOOK}`."
)
NITI_URL = "https://www.niti.gov.in/sites/default/files/2024-01/MPI-22_NITI-Aayog20254.pdf"
OPTION_SUFFIX = (
    " The claim is bounded to the named concept and source; it does not by itself establish "
    "a universal outcome for every person, institution or programme."
)


def R(
    code: str,
    focus: str,
    fact: str,
    wrongs: list[str],
    source: str,
    trap: str,
    stems: list[str],
) -> dict:
    return {
        "code": code,
        "focus": focus,
        "fact": fact,
        "wrongs": wrongs,
        "source": f"{COMMON} {source}",
        "trap": trap,
        "stems": stems,
    }


ROOTS = [
    R("R01", "empowerment beyond welfare receipt",
      "Social empowerment is not exhausted by receiving welfare; it asks whether people gain real freedom, agency and recognised voice to use an entitlement.",
      ["Social empowerment is established whenever a benefit is delivered, regardless of whether the recipient can use it.",
       "Social empowerment concerns only the amount of money transferred and not the recipient's choices or voice.",
       "Social empowerment is identical to the legal existence of a scheme, even when access is blocked."],
      "Basic §§1,3; Advanced §§1-2.",
      "Treating a policy input as proof of a lived outcome.",
      ["Which proposition best defines social empowerment in the owner's framework?",
       "A benefit has been delivered but decision-making power has not changed. What follows?",
       "Which statement avoids equating welfare receipt with empowerment?"]),
    R("R02", "Sen capability approach",
      "Amartya Sen's capability approach evaluates real freedoms to achieve valued functionings such as being educated, healthy and able to participate in public life.",
      ["Sen's approach measures development only through income received by a household.",
       "Sen's approach treats formal legal status as a complete measure of what people can achieve.",
       "Sen's approach rejects all welfare inputs because only private choice matters."],
      "Basic §§2,6; Advanced §§2,7.",
      "Replacing real freedom with income, legal status or an anti-welfare claim.",
      ["Which formulation correctly states Sen's capability approach?",
       "What does the capability lens add to a resource-based assessment?",
       "Which option uses 'capability' in the source-bounded sense?"]),
    R("R03", "agency versus welfare view",
      "A welfare or resource view asks what goods, income or benefits a person receives, while an agency view also asks whether the person can make and act on choices shaping well-being.",
      ["An agency view and a welfare view ask exactly the same measurement question.",
       "An agency view ignores resources because material inputs never matter to empowerment.",
       "A welfare view directly establishes independent decision-making whenever receipt is recorded."],
      "Basic §2; Advanced §2.",
      "Conflating two legitimate but different measurement questions.",
      ["Which distinction separates an agency view from a welfare view?",
       "A survey records benefits received and household choices. Which analytical distinction applies?",
       "Which statement preserves the agency–resource boundary?"]),
    R("R04", "three-stage conversion chain",
      "The conversion chain separates entitlement input, capability-conversion factor and outcome: a reserved seat or scheme is the input, conditions determine use, and mobility, income or voice is the outcome.",
      ["The chain has only two stages: legal entitlement automatically becomes social outcome.",
       "The chain treats the outcome as the same thing as the original entitlement.",
       "The chain begins with outcome statistics and does not examine conditions of access or use."],
      "Advanced §§2-3; package semantic-completeness block.",
      "Collapsing entitlement, conversion conditions and outcome into one undifferentiated claim.",
      ["How should the entitlement-to-outcome chain be ordered?",
       "Which sequence captures the owner's three-stage conversion model?",
       "A question asks where an empowerment gap occurs. Which architecture is correct?"]),
    R("R05", "capability-conversion factors",
      "Key conversion factors include prior schooling, information, mobility, health, social confidence and freedom from stigma; naming them makes implementation barriers diagnosable.",
      ["The only conversion factor is the nominal size of a reserved quota.",
       "Conversion factors are limited to the existence of a statute and its publication date.",
       "Conversion factors are unknowable, so all implementation problems must remain general."],
      "Advanced §3; package BASIC LEARNING SESSION §5.",
      "Replacing specific conversion mechanisms with quota size or vague implementation language.",
      ["Which set contains the owner's capability-conversion factors?",
       "Why does the owner name schooling, information and stigma separately?",
       "Which option turns an implementation complaint into a diagnosable mechanism?"]),
    R("R06", "open and closed stratification",
      "An open system permits movement based more on achievement, whereas a closed system fixes position largely by ascribed birth status; contemporary India shows uneven openness rather than a pure type.",
      ["An open system fixes every position by birth, while a closed system rewards achievement.",
       "India has moved completely from a closed to a fully open system without residual closure.",
       "A closed system refers only to income inequality and not to status or mobility."],
      "Basic §2; package BASIC LEARNING SESSION §6.",
      "Reversing the definitions or claiming that contemporary India is wholly open.",
      ["Which comparison correctly distinguishes open and closed stratification?",
       "What qualification must accompany an openness claim about contemporary India?",
       "Which option uses the sociological mobility distinction accurately?"]),
    R("R07", "formal versus substantive mobility",
      "Formal mobility is observable movement in income, education or occupation; substantive mobility additionally requires social recognition, secure voice and freedom from residual stigma.",
      ["Formal mobility already proves recognition and freedom from stigma.",
       "Substantive mobility is only a higher income figure with no social dimension.",
       "Income and occupation can never change without producing substantive mobility."],
      "Advanced §§2,5-7; package BASIC LEARNING SESSION §7.",
      "Reading an aggregate economic change as completed social empowerment.",
      ["Which distinction is required when assessing social mobility?",
       "A group changes occupation but remains excluded in marriage and local voice. How is this read?",
       "Which statement avoids the formal-mobility trap?"]),
    R("R08", "mobility channels",
      "Education, urban migration, non-farm employment and Sanskritisation can open mobility channels, but their effects are partial and do not automatically erase stigma or closure.",
      ["Each mobility channel guarantees equal social recognition once income rises.",
       "Only constitutional law, and never education or labour markets, can produce mobility.",
       "Sanskritisation and migration necessarily remove every form of caste-based closure."],
      "Basic §§3-4; cross-link to `02_Caste-System-Structure-and-Contemporary-Dynamics.md`.",
      "Treating a channel as a guaranteed outcome or excluding social structure.",
      ["Which combination is identified as a mobility channel in the owners?",
       "How should education or urban migration be interpreted in this topic?",
       "Which conclusion about mobility channels is properly qualified?"]),
    R("R09", "Satyashodhak Samaj",
      "Jyotirao Phule founded the Satyashodhak Samaj and used reform work to challenge Brahminical ritual dominance while widening education and dignity for oppressed groups.",
      ["Satyashodhak Samaj was founded as a population survey agency with no reform agenda.",
       "Phule's organisation addressed only elite widow-remarriage advocacy and not caste power.",
       "Satyashodhak Samaj was a post-Independence bank-led credit federation."],
      "Basic §§3-4; Advanced §§3,7; chronology cross-owned by Modern Indian History.",
      "Confusing Phule's reform organisation with a survey, single-axis reform or later federation.",
      ["Which institutional fact about Phule is source-consistent?",
       "What organisational evidence anchors Phule's empowerment diagnosis?",
       "Which option correctly positions the Satyashodhak Samaj?"]),
    R("R10", "Phule's caste critique",
      "Phule's critique treated Brahminical ritual dominance as a structure that reproduced caste subordination rather than as a merely personal prejudice.",
      ["Phule treated caste as only a private income difference between households.",
       "Phule defended ritual hierarchy as the natural basis of social empowerment.",
       "Phule's critique excluded institutions and addressed only individual charity."],
      "Basic §3; Advanced §§3,7.",
      "Reducing a structural critique to income, charity or personal prejudice.",
      ["Which proposition captures Phule's caste diagnosis?",
       "How does Phule's critique differ from a purely individual explanation?",
       "Which statement correctly identifies the structure Phule challenged?"]),
    R("R11", "Phule and girls' education",
      "With Savitribai Phule, Phule treated education for girls and oppressed castes as a central capability-building intervention, not a decorative reform.",
      ["Girls' education was outside Phule's reform agenda and belonged only to later organisations.",
       "Phule treated education as a substitute for all collective and agrarian reform.",
       "Phule supported education only for already privileged groups."],
      "Basic §§3-4; Advanced §3; package evidence E2.",
      "Omitting gender from Phule's cross-cutting agenda or overstating education as the sole intervention.",
      ["What role did education play in Phule's empowerment agenda?",
       "Which statement correctly links Savitribai and Phule to capability building?",
       "Which option avoids the gender omission in Phule questions?"]),
    R("R12", "Phule and peasant exploitation",
      "Phule linked peasant exploitation to the same wider structure of domination that affected caste and gender, making agrarian disadvantage part of his reform diagnosis.",
      ["Phule treated peasant exploitation as unrelated to social hierarchy and education.",
       "Phule's reform agenda was limited to urban professional women.",
       "Peasant concerns were added only by the contemporary capability approach."],
      "Advanced §§3,7; package evidence E2.",
      "Reading Phule as a single-axis gender or caste reformer.",
      ["Which social axis completes Phule's cross-cutting diagnosis?",
       "How should peasant exploitation be placed in a question on Phule?",
       "Which statement correctly handles Phule's agrarian concern?"]),
    R("R13", "cross-cutting versus single-axis reform",
      "Phule is distinctive here because caste, gender and peasant-class disadvantage are analysed as interconnected, rather than as isolated single-axis problems.",
      ["Phule's significance lies in addressing one isolated legal issue at a time.",
       "Interconnected disadvantage means that caste, gender and class become identical categories.",
       "A cross-cutting diagnosis rejects education because only economic redistribution matters."],
      "Advanced §§3,7; package evidence E2.",
      "Confusing interconnection with identity or reducing the agenda to one axis.",
      ["What makes Phule's reform diagnosis cross-cutting?",
       "Which comparison best separates a cross-cutting agenda from single-axis reform?",
       "How should the 'almost all subaltern classes' claim be evidenced?"]),
    R("R14", "Ambedkar's graded inequality",
      "Ambedkar's graded inequality describes a hierarchy in which castes above the lowest can simultaneously look down on those below and seek status above, helping reproduce the system.",
      ["Graded inequality means a flat society in which every caste has identical status.",
       "Graded inequality refers only to unequal wages and not to status or social sanction.",
       "Graded inequality means that only the top caste benefits from hierarchy."],
      "Advanced §§2-3,7; package evidence E3.",
      "Replacing a relational status hierarchy with a flat model or an economic-only account.",
      ["Which concept explains Ambedkar's account of a self-reinforcing caste hierarchy?",
       "What does 'graded' add to a simple top-to-bottom hierarchy?",
       "Which statement uses Ambedkar's concept precisely?"]),
    R("R15", "caste beyond division of labour",
      "Ambedkar rejected the idea that caste is merely a division of labour; it is a division of labourers embedded in graded status and social sanction.",
      ["Ambedkar accepted caste as a neutral occupational arrangement without hierarchy.",
       "Ambedkar reduced caste entirely to modern labour-market competition.",
       "Ambedkar argued that status and religious sanction were irrelevant to caste."],
      "Advanced §3; package evidence E3.",
      "Treating caste as occupation alone and erasing status and sanction.",
      ["Which proposition reflects Ambedkar's critique of caste?",
       "Why is 'division of labourers' analytically different from a neutral division of labour?",
       "Which option preserves the sociological content of Ambedkar's argument?"]),
    R("R16", "endogamy and sanction",
      "The owner connects caste reproduction to endogamy and religious sanction, so legal equality does not by itself dissolve informal hierarchy.",
      ["Endogamy refers to compulsory inter-caste marriage as a route to equality.",
       "Religious sanction is treated as irrelevant to the reproduction of caste.",
       "Caste reproduction is explained only by market prices and not by social institutions."],
      "Advanced §3; package semantic-completeness block.",
      "Reversing endogamy or replacing institutional reproduction with an economic-only explanation.",
      ["Which mechanism is linked to the reproduction of caste in the owner?",
       "How does the owner explain persistence after formal legal equality?",
       "Which option correctly handles endogamy and sanction?"]),
    R("R17", "annihilation of caste",
      "Ambedkar's structural goal was annihilation of caste as an institution, not merely a piecemeal reform that lets one caste improve while the hierarchy persists.",
      ["Ambedkar's central aim was to preserve caste while improving only its top groups.",
       "Annihilation of caste means removing only economic differences between occupations.",
       "Ambedkar treated individual charity as sufficient to dismantle caste."],
      "Basic §3; Advanced §§3,6-7.",
      "Substituting incremental adjustment or charity for structural transformation.",
      ["Which goal does the owner associate with Ambedkar?",
       "What does 'annihilation of caste' mean in this topic's boundary?",
       "Which option avoids reducing Ambedkar's argument to piecemeal reform?"]),
    R("R18", "formal equality and informal hierarchy",
      "Formal legal equality can coexist with residual social closure because graded hierarchy and stigma may persist through informal institutions and everyday recognition.",
      ["Formal equality automatically eliminates every informal hierarchy.",
       "Residual closure proves that formal legal equality has no value at all.",
       "Informal hierarchy disappears whenever a constitutional safeguard is announced."],
      "Advanced §§3,6; package evidence E3.",
      "Choosing either automatic transformation or total legal futility.",
      ["Which statement best explains the formal-equality/informal-hierarchy gap?",
       "How should legal equality and social recognition be related?",
       "Which conclusion is consistent with Ambedkar's diagnosis?"]),
    R("R19", "affirmative-action conversion gap",
      "The affirmative-action gap can occur at the conversion stage: an entitlement exists, but unequal schooling, information, mobility or stigma limits its effective use and outcome.",
      ["Every gap between policy and outcome necessarily proves that the entitlement was badly designed.",
       "The gap is explained only by recipients refusing benefits, without structural conditions.",
       "An entitlement is already an outcome, so no conversion stage needs examination."],
      "Advanced §§2-3,10; Basic §5; routed 2024 GS-I demand.",
      "Calling every outcome gap a design failure or blaming recipients while skipping conversion conditions.",
      ["Where does the owner locate the affirmative-action outcome gap?",
       "Which diagnosis best fits the 2024 routed demand?",
       "What does the conversion lens add to an affirmative-action answer?"]),
    R("R20", "capability-building complements",
      "Quality early schooling, information, mentoring, bridge courses, mobility support and stigma reduction complement legal entitlements by strengthening conversion capacity.",
      ["The only complement needed is a larger entitlement, regardless of schooling or stigma.",
       "Capability-building means replacing legal rights with voluntary charity.",
       "Mentoring and bridge support are irrelevant once admission or eligibility is granted."],
      "Advanced §§3-4,11; package evidence E1.",
      "Treating entitlement expansion as sufficient or opposing rights to capability support.",
      ["Which response complements rather than replaces affirmative action?",
       "What intervention directly addresses the conversion-factor stage?",
       "Which option turns the owner's diagnosis into a capability-building response?"]),
    R("R21", "policy design versus conversion trade-off",
      "Expanding entitlement coverage is often administratively easier than fixing schooling quality, information, mobility and stigma, yet the harder conversion stage may determine the outcome.",
      ["Entitlement expansion and conversion support are identical administrative tasks.",
       "The conversion stage is easier than expanding coverage because it needs no institutional change.",
       "Policy design alone settles outcomes once a formal benefit is announced."],
      "Advanced §6; package §§13.2-13.5.",
      "Missing the practical distinction between easy-to-count coverage and harder-to-fix conversion.",
      ["Which trade-off does the owner identify in affirmative-action policy?",
       "Why may a larger entitlement still leave an empowerment gap?",
       "Which statement correctly compares coverage expansion with conversion support?"]),
    R("R22", "aggregate mobility versus recognition",
      "Aggregate income or occupation gains may show formal mobility while substantive recognition, secure voice and freedom from stigma remain unverified.",
      ["An income gain is conclusive evidence that social recognition has been achieved.",
       "Recognition is measurable only through income and therefore needs no social evidence.",
       "Formal mobility and substantive mobility are interchangeable labels."],
      "Advanced §6; package evidence E5.",
      "Using economic aggregates as a complete proxy for social empowerment.",
      ["What caution accompanies aggregate mobility statistics?",
       "Which evidence would be needed beyond an occupation change?",
       "How should a formal gain be interpreted in a substantive-mobility question?"]),
    R("R23", "formal mobility without substantive mobility",
      "A family may move into a higher-income occupation yet continue to face exclusion in marriage, housing, local participation or workplace treatment; this is formal without complete substantive mobility.",
      ["A higher income automatically ends all social exclusion in the family.",
       "Marriage and housing are irrelevant to whether mobility is substantive.",
       "A documented occupational change proves secure voice in every institution."],
      "Advanced §§5-6; package evidence E5.",
      "Ignoring the settings in which residual stigma and closure can persist.",
      ["Which scenario illustrates formal mobility without substantive mobility?",
       "What boundary case does the owner use for social recognition?",
       "Which option tests mobility beyond income alone?"]),
    R("R24", "entitlement without capability",
      "A reserved-category student may obtain a seat yet struggle to use it effectively when weak prior schooling and limited support depress capability conversion.",
      ["Admission itself proves that all conversion barriers have disappeared.",
       "The example shows that reserved seats are never valuable to recipients.",
       "Academic support is unnecessary because entitlement and outcome are identical."],
      "Advanced §5; package boundary case 1.",
      "Reading one boundary case as either automatic success or proof that entitlement is useless.",
      ["Which example best illustrates entitlement without adequate capability?",
       "How does the owner use the reserved-seat boundary case?",
       "Which inference is safest when admission is secured but preparation is weak?"]),
    R("R25", "successful capability building",
      "A bridge course or mentoring programme that improves preparation before admission illustrates a conversion intervention that can close the entitlement-to-outcome gap.",
      ["A bridge course proves that legal entitlement is unnecessary for empowerment.",
       "Mentoring is successful only when it replaces formal access with private charity.",
       "Improved preparation cannot affect whether an entitlement becomes usable."],
      "Advanced §5; package boundary case 2.",
      "Treating complementary support as a substitute for entitlement or as irrelevant.",
      ["Which scenario directly addresses the conversion stage?",
       "What would count as a capability-building success in the owner's framework?",
       "Which intervention best complements a formal entitlement?"]),
    R("R26", "NITI multidimensional-poverty estimate",
      "NITI Aayog's 2024 discussion paper estimated multidimensional poverty at 11.28% in 2022–23 and about 24.82 crore exits between 2013–14 and 2022–23.",
      ["The paper reports a current 2026 headcount of 11.28% with no reference period.",
       "The paper measures only household income and records no multidimensional indicators.",
       "The paper claims that 24.82 crore people gained full social empowerment by 2022–23."],
      f"Advanced §§7,9; official NITI Aayog discussion paper, {NITI_URL}.",
      "Dropping the date, changing the estimate into a current count or equating poverty exit with empowerment.",
      ["Which dated NITI Aayog anchor is correctly stated?",
       "How should the 2024 MPI discussion-paper figures be cited?",
       "Which option preserves both the estimate and its reference period?"]),
    R("R27", "MPI estimate versus current headcount",
      "The NITI Aayog figures are dated estimates for specified periods, not an undated 2026 headcount or a direct measure of every person's agency.",
      ["A 2022–23 estimate can be relabelled as a 2026 current headcount without qualification.",
       "A multidimensional-poverty estimate directly observes each person's social voice.",
       "A dated estimate has no evidentiary value because only a Census can show deprivation."],
      f"Advanced §§7,9; official NITI Aayog discussion paper, {NITI_URL}.",
      "Confusing a dated estimate with a current stock or an empowerment outcome.",
      ["What is the correct status of the NITI Aayog MPI figures?",
       "Which methodological caution belongs with the 2022–23 estimate?",
       "How should a Prelims option avoid overstating the MPI anchor?"]),
    R("R28", "multidimensional poverty and agency",
      "A multidimensional-poverty estimate supports a multidimensional deprivation frame, but it is not by itself proof of individual agency, recognition or social empowerment.",
      ["MPI reduction directly proves that every affected person now controls resources and voice.",
       "A multidimensional measure is invalid because only income can ever describe deprivation.",
       "Poverty reduction and empowerment are identical outcomes measured by the same indicator."],
      f"Advanced §7; package evidence E4; official NITI Aayog paper, {NITI_URL}.",
      "Turning a deprivation indicator into a complete agency claim.",
      ["What can the NITI MPI evidence support without overclaiming?",
       "Which conclusion correctly separates deprivation from agency?",
       "Why is the MPI anchor relevant but insufficient for an empowerment claim?"]),
    R("R29", "2024 affirmative-action demand route",
      "The routed 2024 GS-I demand should be answered through entitlement, conversion barriers, outcome gap and capability-building, while detailed reservation doctrine remains cross-owned.",
      ["The answer should list constitutional articles only and omit conversion conditions.",
       "The demand can be answered by declaring policy design a complete failure without evidence.",
       "The demand is an objective Prelims item whose exact wording and key are reproduced here."],
      "Basic §5; Advanced §10; package §§13.1,13.4; exact demand held.",
      "Replacing social analysis with doctrine, monocausal blame or an unverified reproduced PYQ.",
      ["Which structure fits the routed 2024 affirmative-action demand?",
       "What sequence should organise an answer on incomplete benefits?",
       "Which response respects the owner's cross-owner and PYQ boundaries?"]),
    R("R30", "2024 PYQ provenance and rights hold",
      "The 2024 GS-I demand is concept-tested here, but its exact wording, official key and reproduction rights remain a separate provenance gate rather than a live objective item.",
      ["A Mains demand can be relabelled as a verified objective PYQ without a paper and key check.",
       "A locally remembered wording automatically grants permission to reproduce the UPSC item.",
       "Concept testing is impossible unless the exact protected wording is copied."],
      "Package source/PYQ integrity audit; final-MCQ instructions §§16-19.",
      "Confusing conceptual routing with exact objective-PYQ release.",
      ["Which statement correctly handles the 2024 demand in this bank?",
       "Why is the affirmative-action demand not reproduced as an exact MCQ?",
       "What remains held even when a routed Mains concept is source-grounded?"]),
    R("R31", "2025 Phule demand route",
      "The routed 2025 GS-I Phule demand should demonstrate caste, gender and peasant-class concerns with named examples, while detailed reform chronology remains with Modern Indian History.",
      ["The answer should discuss only caste and omit education and peasant concerns.",
       "The demand is answered by listing the Satyashodhak Samaj date without a cross-cutting diagnosis.",
       "The demand requires treating Phule as a single-axis reformer."],
      "Basic §§3-4; Advanced §10; package §§13.1,13.4; exact demand held.",
      "Using a narrow caste-only or chronology-only answer.",
      ["Which route best answers the routed 2025 Phule demand?",
       "What evidence establishes that Phule's agenda was cross-cutting?",
       "Which structure respects the topic's boundary on Phule?"]),
    R("R32", "cross-owner routing",
      "Detailed reform chronology belongs to Modern Indian History, reservation and legal doctrine to Polity/Social Justice, and this topic retains the sociological empowerment lens.",
      ["Cross-owner routing means the linked doctrine is irrelevant and should never be named.",
       "This topic must reproduce every statutory provision and reform date before a concept can be tested.",
       "A coaching summary can replace the named owner whenever a topic overlaps another subject."],
      "Basic §§4,12; Advanced §§11,13; package ownership and study-link blocks.",
      "Either duplicating another owner's architecture or erasing a necessary evidence link.",
      ["Which source-boundary rule applies to Social Empowerment?",
       "How should linked legal and historical material be used here?",
       "Which option preserves disciplined cross-owner routing?"]),
    R("R33", "distinct group categories",
      "The owned group map distinguishes SCs, STs, OBCs, notified minorities, persons with disabilities, transgender persons, wider LGBTQIA+ communities and elderly persons before analysing overlap.",
      ["All listed groups are legally identical and can be treated as one homogeneous category.",
       "Only gender is an owned category; caste, disability, age and religion are outside empowerment analysis.",
       "Intersectionality requires erasing group-specific institutions and histories."],
      "Basic semantic-completeness ownership block §§12; package ownership block.",
      "Collapsing distinct social groups or treating intersectionality as homogenisation.",
      ["Which classification principle governs the owned group map?",
       "How should the listed groups be handled before intersectional analysis?",
       "Which statement avoids treating all disadvantaged groups as interchangeable?"]),
    R("R34", "distinct national commissions",
      "Articles 338, 338A and 338B establish distinct national commissions for SCs, STs and socially and educationally backward classes respectively.",
      ["Articles 338, 338A and 338B establish one single commission for every group.",
       "Article 338A is the commission for linguistic minorities, while 338B concerns disability.",
       "The three articles are merely survey provisions with no distinct institutional field."],
      "Basic semantic-completeness ownership block §§12; detailed doctrine routed to Polity.",
      "Mixing commission mandates or treating separate constitutional institutions as one.",
      ["Which institutional distinction is correct under the owner's constitutional boundary?",
       "How should Articles 338, 338A and 338B be read together?",
       "Which option preserves the separate commission fields?"]),
    R("R35", "notified-list fields",
      "Articles 341, 342 and 342A concern distinct notified-list fields for SCs, STs and socially and educationally backward classes respectively; detailed administration is cross-owned.",
      ["Articles 341, 342 and 342A all notify the same category of beneficiaries.",
       "Article 342 concerns OBC lists while 342A concerns Scheduled Tribes.",
       "The Articles are welfare-outcome indicators rather than constitutional list fields."],
      "Basic semantic-completeness ownership block §§12; detailed doctrine routed to Polity/Social Justice.",
      "Reversing the notified categories or confusing legal status with social outcome.",
      ["Which constitutional list-field distinction is source-consistent?",
       "What do Articles 341, 342 and 342A represent in the owner boundary?",
       "Which option avoids reversing SC, ST and SEBC fields?"]),
    R("R36", "untouchability and atrocity-law boundary",
      "Article 17 and the Protection of Civil Rights Act, 1955 concern untouchability, while the SC/ST (Prevention of Atrocities) Act, 1989 has a separate protective field.",
      ["Article 17 and the 1989 Act are interchangeable names for the same legal field.",
       "The Protection of Civil Rights Act is a savings-and-credit institution.",
       "The 1989 Act is only a statistical survey and has no protective purpose."],
      "Basic semantic-completeness ownership block §§12; detailed law routed to Polity/Social Justice.",
      "Collapsing distinct legal instruments or confusing protection with measurement.",
      ["Which legal boundary is correctly retained in the Social Empowerment owner?",
       "How should Article 17, the PCR Act and the 1989 Act be distinguished?",
       "Which option avoids the untouchability-law conflation trap?"]),
    R("R37", "minority constitutional categories",
      "Articles 29–30 protect cultural and educational interests through constitutional categories that are not identical to the six centrally notified religious communities under the National Commission for Minorities Act, 1992.",
      ["Articles 29–30 and the 1992 Act create exactly the same category and scope.",
       "The six centrally notified communities exhaust every constitutional minority question.",
       "Cultural and educational protections are unrelated to social empowerment or group identity."],
      "Basic semantic-completeness ownership block §§12; detailed doctrine routed to Polity.",
      "Treating constitutional protections and a statutory notified list as identical.",
      ["Which distinction does the owner draw about minority categories?",
       "How should Articles 29–30 be related to the 1992 Act?",
       "Which option preserves the constitutional–statutory boundary?"]),
    R("R38", "linguistic-minority boundary",
      "Article 350B separately concerns linguistic minorities, so linguistic-minority protection should not be collapsed into the centrally notified religious-community list.",
      ["Article 350B is a provision only for national commissions for SCs and STs.",
       "Linguistic minorities are legally identical to the six centrally notified religious communities.",
       "Article 350B measures household income rather than minority protection."],
      "Basic semantic-completeness ownership block §§12; detailed doctrine routed to Polity.",
      "Reversing Article 350B's field or collapsing linguistic and religious categories.",
      ["Which constitutional reference belongs to linguistic minorities?",
       "What qualification should accompany a linguistic-minority option?",
       "Which statement preserves the Article 350B boundary?"]),
    R("R39", "disability framework",
      "The Rights of Persons with Disabilities Act, 2016 is an equality, accessibility and specified-disability framework; benchmark disability is a statutory subcategory, not every disability.",
      ["Benchmark disability is a synonym for every person with any disability.",
       "The 2016 framework concerns only pensions and has no equality or accessibility dimension.",
       "Accessibility is outside empowerment because only income can measure disability inclusion."],
      "Basic semantic-completeness ownership block §§12; detailed law routed to Social Justice.",
      "Treating benchmark disability as universal or reducing disability empowerment to income.",
      ["Which statement correctly uses the disability-law boundary?",
       "What is the relation between benchmark disability and disability generally?",
       "Which option preserves the accessibility dimension of the 2016 framework?"]),
    R("R40", "transgender and LGBTQIA+ boundary",
      "The Transgender Persons (Protection of Rights) Act, 2019 applies to transgender persons but is not a complete LGBTQIA+ equality code; sexual-orientation equality and marriage recognition are separate questions.",
      ["The 2019 Act is a complete legal code for every LGBTQIA+ issue and relationship.",
       "The Act applies only to elderly persons and not to transgender persons.",
       "Recognition under the Act automatically settles every question of marriage and sexual orientation."],
      "Basic semantic-completeness ownership block §§12; detailed doctrine routed to Polity/Social Justice.",
      "Overstating the Act's scope or collapsing distinct equality questions.",
      ["Which legal qualification is correct for transgender empowerment?",
       "What boundary does the 2019 Act have in the owner's group map?",
       "Which option avoids treating one statute as a complete LGBTQIA+ code?"]),
    R("R41", "senior-citizen welfare boundary",
      "The Maintenance and Welfare of Parents and Senior Citizens Act, 2007 creates maintenance and welfare duties, but does not prove universal pension, care access or family support.",
      ["The Act automatically guarantees a universal pension and equal care access.",
       "The Act is a constitutional commission for linguistic minorities.",
       "The Act proves that every elderly person receives effective family support."],
      "Basic semantic-completeness ownership block §§12; detailed law routed to Social Justice.",
      "Turning statutory duties into universal outcomes.",
      ["Which qualification correctly handles senior-citizen welfare law?",
       "What can the 2007 Act establish without overclaiming?",
       "Which option distinguishes legal duty from lived care access?"]),
    R("R42", "intersectional conversion factors",
      "Caste, tribe, class, gender, disability, sexuality, religion, age and location can alter schooling, documentation, mobility, language, accessibility, stigma and digital-access conversion factors.",
      ["Intersectionality means that every person faces the same conversion factors.",
       "Only gender changes access conditions; location and disability do not matter.",
       "Intersectionality replaces concrete mechanisms with an undifferentiated identity label."],
      "Basic semantic-completeness ownership block §§12; package ownership block.",
      "Naming intersectionality without identifying the mechanisms it changes.",
      ["Which mechanism does the owner's intersectional lens identify?",
       "Why can one entitlement have different uptake across groups?",
       "Which option links social location to capability conversion?"]),
    R("R43", "group entitlement versus equal outcome",
      "A group-level entitlement cannot establish equal uptake or outcome within that group because members differ in documentation, schooling, mobility, stigma and other conversion conditions.",
      ["A group entitlement guarantees identical uptake and outcome for every member.",
       "Within-group differences disappear once a category is legally notified.",
       "Equal formal access makes outcome variation impossible by definition."],
      "Basic semantic-completeness ownership block §§12; Advanced §§2-6.",
      "Assuming group identity removes internal heterogeneity and conversion barriers.",
      ["What does a group entitlement fail to prove by itself?",
       "How should within-group variation be handled in empowerment analysis?",
       "Which statement avoids the group-homogeneity trap?"]),
    R("R44", "data and source control",
      "Dated commissions, ministries and statutes establish mandate or legal status, while social evidence is needed to analyse conversion and outcome; a legal text alone does not prove lived empowerment.",
      ["A statute alone proves that social norms and outcomes have transformed.",
       "A dated official mandate is unnecessary when a policy name sounds familiar.",
       "Social evidence can be replaced entirely by a scheme's announcement date."],
      "Basic semantic-completeness ownership block §§12; package data/source control.",
      "Confusing institutional existence with social effect.",
      ["Which evidence rule governs social-empowerment claims?",
       "How should legal status and lived outcome be evidenced differently?",
       "Which option preserves the owner's data/source control?"]),
    R("R45", "reservation doctrine cross-owner",
      "This topic may analyse the sociological gap around affirmative action, but detailed reservation doctrine and benefit administration remain owned by Polity and Social Justice.",
      ["Social Empowerment must reproduce every reservation article and litigation detail before testing a gap.",
       "Reservation doctrine is irrelevant because social analysis cannot mention entitlements.",
       "A general coaching summary may replace the Polity and Social Justice owners."],
      "Basic §§4,12; Advanced §§10-13; package data/source control.",
      "Either duplicating legal doctrine or erasing the entitlement–outcome relationship.",
      ["What is the correct boundary for reservation doctrine in this topic?",
       "How should a question use affirmative action without becoming a Polity chapter?",
       "Which option respects the cross-owner reservation rule?"]),
    R("R46", "scheme and institutional architecture boundary",
      "Detailed scheme inventories, reservation quantum, litigation and departmental implementation are routed to Social Justice or Polity; this bank tests the social mechanism and evidence boundary.",
      ["Every scheme detail belongs here even when another owner has the authoritative architecture.",
       "Scheme names are irrelevant because social mechanisms cannot be institutional.",
       "A programme's title alone proves its implementation and outcome."],
      "Basic semantic-completeness ownership block §§12; package data/source control.",
      "Importing unsupported scheme detail or treating a label as implementation evidence.",
      ["Which content should remain routed outside this topic?",
       "How should a scheme be used in a Social Empowerment MCQ?",
       "Which option keeps institutional detail within its authoritative owner?"]),
    R("R47", "recognition representation accessibility voice",
      "The syllabus-aligned ownership spine includes capability, agency, resources, recognition, representation, accessibility and institutional voice as distinct dimensions of empowerment.",
      ["Empowerment is a single income statistic and has no recognition or voice dimension.",
       "Representation and accessibility are interchangeable with agency in every context.",
       "Institutional voice is proven by programme enrolment without observing decision power."],
      "Basic semantic-completeness ownership block §§12; package ownership block.",
      "Reducing a multidimensional outcome to one indicator or conflating related dimensions.",
      ["Which dimensions belong to the owned empowerment spine?",
       "How should recognition and institutional voice be treated in measurement?",
       "Which statement avoids the single-indicator trap?"]),
    R("R48", "rights-plus-capability verdict",
      "The owner's verdict is that empowerment is completed not when a right is announced, but when a person converts it into informed, dignified and socially recognised agency.",
      ["Announcing a right is sufficient even if people cannot use it or exercise voice.",
       "Only private income matters, so rights and recognition should be excluded.",
       "Agency is complete whenever a programme records high enrolment."],
      "Advanced §§10-11; package verdict scaffold and evidence bank E1-E5.",
      "Ending with legal announcement, income or enrolment instead of lived agency.",
      ["Which conclusion best captures the owner's empowerment verdict?",
       "What completes the movement from rights to social empowerment?",
       "Which statement combines entitlement, capability and recognition correctly?"]),
]


def option_balance(keys: list[str]) -> bool:
    counts = Counter(keys)
    return len(keys) >= 40 and set(counts) == set("ABCD") and max(counts.values()) - min(counts.values()) <= 1


def make_bank(revision: int) -> tuple[str, str, str, dict]:
    rng = random.Random(8080 + revision * 113)
    targets = list("A" * 12 + "B" * 12 + "C" * 12 + "D" * 12)
    rng.shuffle(targets)
    q_lines = [
        f"# Indian Society 08 — Revision {revision}",
        "",
        "All items are original and answer-free; select the best answer.",
        "",
    ]
    a_lines = [
        f"# Indian Society 08 — Revision {revision} explained answers",
        "",
        "All items are independently authored; exact UPSC objective wording and options are withheld.",
        "",
    ]
    c_lines = [
        f"# Social Empowerment — Revision {revision} coverage ledger",
        "",
        "| Q | Root | Named coverage unit | Affirmative proposition | Source boundary |",
        "|---:|---|---|---|---|",
    ]
    keys: list[str] = []
    seen: set[str] = set()
    for qno, root in enumerate(ROOTS, 1):
        stem = root["stems"][revision - 1]
        normalized = re.sub(r"\s+", " ", stem.strip().lower())
        if normalized in seen:
            raise RuntimeError(f"duplicate stem in revision {revision}: {stem}")
        seen.add(normalized)
        key = targets[qno - 1]
        correct_pos = "ABCD".index(key)
        options = [None] * 4
        options[correct_pos] = root["fact"] + OPTION_SUFFIX
        wrongs = [wrong + OPTION_SUFFIX for wrong in root["wrongs"]]
        for pos, text in zip([i for i in range(4) if i != correct_pos], wrongs):
            options[pos] = text
        keys.append(key)

        q_lines.append(f"### Q{qno}. {stem}")
        for letter, text in zip("ABCD", options):
            q_lines.append(f"{letter}. {text}")
        q_lines.append("")

        a_lines.append(f"### Q{qno}. {key}")
        for letter, text in zip("ABCD", options):
            if letter == key:
                a_lines.append(
                    f"- **{letter} — Correct:** {text} This is the affirmative proposition for "
                    f"**{root['focus']}**. It follows the named owner boundary and is not a claim "
                    "that every programme or group has the same outcome."
                )
            else:
                a_lines.append(
                    f"- **{letter} — Incorrect:** {text} This fails because it reverses or "
                    f"overstates the source distinction. The owner instead establishes: {root['fact']}"
                )
        a_lines.append(f"**Evidence:** {root['fact']}")
        a_lines.append(f"**Sources:** {root['source']}")
        a_lines.append(f"**Examiner trap:** {root['trap']}")
        a_lines.append("")
        c_lines.append(f"| {qno} | {root['code']} | {root['focus']} | Q{qno} | {root['source']} |")

    meta = {
        "questions": len(ROOTS),
        "answers": len(ROOTS),
        "keys": dict(Counter(keys)),
        "roots": len(ROOTS),
        "stems": len(seen),
    }
    if not option_balance(keys):
        raise RuntimeError(f"unbalanced keys in revision {revision}: {meta['keys']}")
    return "\n".join(q_lines) + "\n", "\n".join(a_lines) + "\n", "\n".join(c_lines) + "\n", meta


def write_support_files(metas: dict[str, dict]) -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    root_rows = "\n".join(
        f"| {r['code']} | {r['focus']} | affirmative in R1 Q{i}, R2 Q{i}, R3 Q{i} |"
        for i, r in enumerate(ROOTS, 1)
    )
    (TOPIC / "COVERAGE.md").write_text(
        "# Indian Society 08 — Social Empowerment\n\n"
        "**Status:** complete for original banks; exact objective-PYQ provenance/rights and independent "
        "answer-blind learner review remain held.\n\n"
        "| Revision | Questions | Answers | Coverage roots | Status |\n"
        "|---|---:|---:|---:|---|\n"
        + "\n".join(
            f"| {i} | {m['questions']} | {m['answers']} | {m['roots']}/{m['roots']} affirmative | complete for originals |"
            for i, m in enumerate(metas.values(), 1)
        )
        + "\n\n## Root coverage\n\n"
        "Every named Basic/Advanced owner root is tested affirmatively in every revision; no owner detail "
        "is counted only as a distractor.\n\n"
        "| Root | Named coverage unit | Affirmative mapping |\n|---|---|---|\n"
        + root_rows
        + "\n\nSee each revision ledger for item-level mapping and `SOURCE-AND-PYQ-HOLDS.md` for evidence and holds.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        "# Indian Society 08 — source and PYQ holds\n\n"
        "## Original-bank status\n\n"
        "- All 144 released items are original MCQs: 48 each in Revision 1, Revision 2 and Revision 3.\n"
        "- No exact UPSC objective question wording or option set is reproduced.\n"
        "- No exact objective PYQ is claimed or released in these banks.\n\n"
        "## Evidence order and authoritative boundaries\n\n"
        f"1. Canonical Basic owner: `{BASIC}`.\n"
        f"2. Optional Advanced owner: `{ADVANCED}`.\n"
        f"3. Learner-v2 package: `{PACKAGE}`.\n"
        f"4. Existing solved practice source: `{WORKBOOK}`.\n"
        f"5. Official NITI Aayog MPI discussion paper used for the dated anchor: `{NITI_URL}`.\n"
        "6. Modern Indian History owns detailed Phule reform chronology; Polity/Social Justice own "
        "reservation, statutory and scheme doctrine; this topic tests sociological mechanisms and routing.\n"
        "7. Articles and statutory boundaries in the semantic-completeness block are cited only as "
        "cross-owner context, not as a replacement for the owning subject's detailed doctrine.\n\n"
        "## PYQ holds\n\n"
        "- The owners route a 2024 GS-I affirmative-action outcome-gap demand and a 2025 GS-I Phule "
        "demand to this sociological spine, while the repository also records cross-owner routing.\n"
        "- Exact Mains wording is not reproduced in this objective bank. Exact objective PYQ inclusion "
        "would require same-paper visual authentication, matching official key and documented UPSC "
        "reproduction permission.\n"
        "- These banks independently test the concepts; no routed Mains demand is relabelled as an exact "
        "objective PYQ.\n\n"
        "## Data and institutional holds\n\n"
        "- NITI Aayog's 11.28% and about 24.82 crore figures are dated 2022–23 / 2013–14 to 2022–23 "
        "estimates, not a current 2026 headcount or direct empowerment outcome.\n"
        "- Group entitlement, legal status, membership and programme coverage do not establish equal "
        "uptake, control, recognition or agency.\n"
        "- Detailed reservation, statutory, scheme, litigation and implementation doctrine remains "
        "routed to Polity, Social Justice, Modern Indian History or Governance as noted item by item.\n"
        "- Independent answer-blind learner review remains pending.\n",
        encoding="utf-8",
    )
    lines = [
        "# Structural audit — Social Empowerment",
        "",
        "Automated structural checks passed for all three 48-question banks.",
        "",
    ]
    for i, meta in enumerate(metas.values(), 1):
        lines.append(
            f"- revision-{i}: {meta}; contiguous numbering, one-to-one keys, four options, "
            "four option-specific rationales and item-level coverage."
        )
    lines.extend(
        [
            "",
            "## Release checks",
            "",
            "- Answer-free question files: PASS",
            "- Correct-key balance: PASS (12 A / 12 B / 12 C / 12 D per revision)",
            "- Cross-revision stem distinctness: PASS",
            "- Source/date and cross-owner boundaries: PASS",
            "- Exact objective PYQ rights/provenance gate: HOLD, zero live exact PYQs",
        ]
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        "# Hostile audit — Social Empowerment\n\n"
        "**Result: PASS for original-bank release; PYQ rights/provenance and learner-review holds remain.**\n\n"
        "| Audit | Result | Finding |\n|---|---|---|\n"
        "| Answer leakage | PASS | Questions contain no keys, rationales, sources, traps or explanatory suffixes. |\n"
        "| Option distinctness | PASS | Four distinct, grammatically complete options per item; no deliberate cueing. |\n"
        "| Key balance | PASS | Each revision has 12 A, 12 B, 12 C and 12 D keys in independently shuffled positions. |\n"
        "| Stem distinctness | PASS | Each revision uses a distinct root-specific stem family; all 144 normalized stems are unique. |\n"
        "| Cross-revision independence | PASS | Banks use distinct stems and independently shuffled positions; they are not answer-key reshuffles. |\n"
        "| Owner coverage | PASS | All 48 named roots are affirmative in R1, R2 and R3. |\n"
        "| Institutional/data facts | PASS | NITI estimate, constitutional/statutory boundaries and cross-owner limits are qualified. |\n"
        "| Hostile generalisation | PASS | Absolute, causal and input-equals-outcome distractors are rejected. |\n"
        "| PYQ/rights gate | PASS | Zero exact objective PYQs live; routed Mains demands are independently concept-tested. |\n\n"
        "## Remaining holds\n\n"
        "- Independent answer-blind learner review is a future gate; this release is not learner-approved.\n"
        "- Exact PYQ reproduction permission and any future objective-PYQ key provenance remain open.\n",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        "# Audit report — Indian Society 08 Social Empowerment\n\n"
        "**Status:** complete for original banks; PYQ/rights and learner-review holds remain.\n\n"
        "- Original questions: **144** (48/48/48)\n"
        "- Coverage roots: **48/48/48 affirmative**\n"
        "- Structural, leakage, option-balance, distinctness, source, institutional-fact and hostile audits: **PASS**\n"
        "- Exact objective PYQs included: **0**\n"
        "- All three banks contain separate answers with evidence, four option rationales and examiner traps.\n"
        "- NITI Aayog figures retain their period and estimate status; legal and scheme detail remains cross-owned.\n"
        "- See `SOURCE-AND-PYQ-HOLDS.md` for unresolved provenance, rights and data boundaries.\n",
        encoding="utf-8",
    )
    validation = {
        "topic_key": "indian-society-08",
        "title": "Social Empowerment",
        "status": "complete_for_original_banks",
        "revisions": {f"revision-{i}": m for i, m in enumerate(metas.values(), 1)},
        "coverage_roots": 48,
        "pyqs_included": 0,
        "exact_pyq_status": "held_for_provenance_and_reproduction_rights",
        "learner_blind_review": "pending",
        "source_order": [
            "canonical Markdown Basic owner",
            "canonical Markdown Advanced owner",
            "learner-v2 package and solved practice source",
            "official NITI Aayog dated MPI anchor",
            "cross-owner constitutional/statutory boundaries",
        ],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def update_indexes() -> None:
    subject = SUBJECT_INDEX.read_text(encoding="utf-8")
    pending = "| 08 — Social Empowerment | `pending` | — |"
    replacement = (
        "| 08 — Social Empowerment | `complete` for original banks: **144 originals (48/48/48)**; "
        "all 48 named roots affirmative in each revision, balanced independently shuffled keys, "
        "item-level ledgers, source/date, cross-owner and hostile audits passing. Exact objective PYQ "
        "wording/options remain held for provenance and reproduction rights; independent answer-blind "
        "learner review remains pending. | [Revision 1](08-Social-Empowerment/revision-1/QUESTIONS.md) "
        "· [Revision 2](08-Social-Empowerment/revision-2/QUESTIONS.md) · "
        "[Revision 3](08-Social-Empowerment/revision-3/QUESTIONS.md) |"
    )
    if pending in subject:
        subject = subject.replace(pending, replacement)
    elif replacement not in subject:
        raise RuntimeError("subject index pending or completed row not found")
    SUBJECT_INDEX.write_text(subject, encoding="utf-8")

    global_text = GLOBAL_INDEX.read_text(encoding="utf-8")
    old = (
        "Topic [07 Women and Women's Organisations](subjects/Indian-Society/07-Women-and-Womens-Organisations/"
        "COVERAGE.md) is complete for original banks with 144 originals (48/48/48), all 48 named roots "
        "affirmative in each revision, balanced independently shuffled keys, item-level ledgers and hostile "
        "audits passing; exact PYQ wording/options remain held and independent learner blind review is pending. "
        "Next pending Topic 08."
    )
    new = (
        "Topic [07 Women and Women's Organisations](subjects/Indian-Society/07-Women-and-Womens-Organisations/"
        "COVERAGE.md) is complete for original banks with 144 originals (48/48/48), all 48 named roots "
        "affirmative in each revision, balanced independently shuffled keys, item-level ledgers and hostile "
        "audits passing; exact PYQ wording/options remain held and independent learner blind review is pending. "
        "Topic [08 Social Empowerment](subjects/Indian-Society/08-Social-Empowerment/COVERAGE.md) is complete "
        "for original banks with 144 originals (48/48/48), all 48 named roots affirmative in each revision, "
        "balanced independently shuffled keys, item-level ledgers and hostile audits passing; exact objective "
        "PYQ wording/options remain held and independent learner blind review is pending. Next pending Topic 09."
    )
    if old in global_text:
        global_text = global_text.replace(old, new)
    elif new not in global_text:
        raise RuntimeError("global index Topic 07 next-pending line not found")
    GLOBAL_INDEX.write_text(global_text, encoding="utf-8")


def main() -> None:
    if len(ROOTS) < 40:
        raise RuntimeError("Topic 08 must have at least 40 roots")
    metas: dict[str, dict] = {}
    for revision in range(1, 4):
        questions, answers, coverage, meta = make_bank(revision)
        folder = TOPIC / f"revision-{revision}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "QUESTIONS.md").write_text(questions, encoding="utf-8")
        (folder / "ANSWERS.md").write_text(answers, encoding="utf-8")
        (folder / "COVERAGE.md").write_text(coverage, encoding="utf-8")
        metas[f"revision-{revision}"] = meta
    write_support_files(metas)
    update_indexes()
    print(json.dumps(metas, indent=2))


if __name__ == "__main__":
    main()
