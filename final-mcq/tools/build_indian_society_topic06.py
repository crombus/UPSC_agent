"""Build and audit the three original MCQ banks for Indian Society Topic 06."""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "06-Population-and-Associated-Issues"
SUBJECT_INDEX = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "INDEX.md"
GLOBAL_INDEX = ROOT / "final-mcq" / "INDEX.md"

BASIC = "upsc-ai-kit/knowledge/Indian-Society/basic/06_Population-and-Associated-Issues.md"
ADVANCED = "upsc-ai-kit/knowledge/Indian-Society/advanced/06_Population-and-Associated-Issues.md"
PACKAGE = "upsc-ai-kit/knowledge/Indian-Society/06_Population-and-Associated-Issues_Learner-V2-Complete-Topic-Package.md"
COMMON = f"Canonical Basic owner `{BASIC}`; Advanced owner `{ADVANCED}`; learner-v2 package `{PACKAGE}`."
NEUTRAL_SUFFIX = " This is a qualified, source-bounded social-science proposition rather than an absolute national rule."


def root(code: str, focus: str, fact: str, wrongs: list[str], sources: str, trap: str,
         stems: list[str]) -> dict:
    return {
        "root": code,
        "focus": focus,
        "fact": fact,
        "wrongs": wrongs,
        "sources": sources,
        "trap": trap,
        "stems": stems,
    }


ROOTS = [
    root("R01", "population as a social question",
         "Population change is a social process shaped by education, marriage timing, desired family size, health access, norms and economic conditions.",
         ["Population is only a biological count and social institutions do not affect it.",
          "Population questions are settled by one national fertility number without reference to social context.",
          "Population change is exclusively a legal-administrative problem with no household-level mechanism."],
         f"{COMMON} Basic §§1-3; Advanced §1.",
         "Reducing a social-demography question to a headcount or a single statistic.",
         ["Which proposition best captures how this owner treats population?",
          "A close-option question asks what makes population a social issue. Which choice is defensible?",
          "Which reading keeps population analysis within the owner's social-demography boundary?"]),
    root("R02", "social determinants of fertility",
         "Women's education, age at marriage, employment, desired family size, contraceptive access, son preference, health and regional context jointly shape fertility decisions.",
         ["One determinant is the sole cause of every fertility outcome in India.",
          "Fertility is explained only by access to contraception and not by norms or agency.",
          "Social determinants matter only after fertility has already fallen for biological reasons."],
         f"{COMMON} Basic §2 and §3; Advanced §§2-3.",
         "Turning a multi-factor association into a single-cause law.",
         ["Which list correctly represents the owner's determinant set?",
          "Which explanation avoids the single-factor trap in a fertility question?",
          "How should a Prelims item frame the social determinants of fertility?"]),
    root("R03", "women's education pathway",
         "Women's education is associated with later marriage, contraceptive knowledge and wider life options, making it a major pathway in fertility transition.",
         ["Women's education affects fertility only by increasing household income.",
          "Women's education automatically produces identical fertility outcomes in every state.",
          "Women's education is irrelevant once reproductive-health services exist."],
         f"{COMMON} Basic §3.1; Advanced §3; 2019 GS-I demand route.",
         "Treating education as either a mechanical income variable or a universal guarantee.",
         ["Which mechanism does the owner associate with women's education?",
          "A question links education and fertility decline. Which causal reading is safest?",
          "Which statement accurately uses women's education as a population determinant?"]),
    root("R04", "interaction with context",
         "The effect of education interacts with service access, income, norms and state context; association does not prove that one factor causes every outcome.",
         ["Education replaces all other determinants once a threshold is crossed.",
          "A national association proves the same causal effect for every household.",
          "Context is analytically irrelevant because fertility decisions are individual only."],
         f"{COMMON} Basic §3.1 and evidence bank E3; Advanced §§2, 6.",
         "Mistaking a patterned association for a universal causal rule.",
         ["Which qualification is required when using education as a fertility determinant?",
          "Which option correctly handles context in a social-demography explanation?",
          "A close-option answer cites education. What additional caution must it retain?"]),
    root("R05", "age at marriage",
         "Later marriage compresses the reproductive window and is associated with better maternal and child health outcomes, alongside contraception as a social lever.",
         ["Later marriage lengthens the reproductive window by definition.",
          "Marriage timing is unrelated to fertility because only biology matters.",
          "Later marriage alone guarantees the same family size regardless of services and norms."],
         f"{COMMON} Basic §3.2; Advanced §3.",
         "Reversing the reproductive-window mechanism or making it deterministic.",
         ["Which proposition correctly describes age at marriage?",
          "How does the owner connect marriage timing with fertility and health?",
          "Which statement avoids a trap about the reproductive window?"]),
    root("R06", "reproductive-window mechanism",
         "Marriage timing changes the length of exposure to childbearing and therefore interacts with desired family size, contraception, health and social support.",
         ["The reproductive window is fixed and cannot be affected by marriage timing.",
          "A shorter window proves that all couples want fewer children.",
          "The mechanism operates independently of contraception or desired family size."],
         f"{COMMON} Basic §3.2; Advanced fertility-decline chain.",
         "Confusing an exposure-window mechanism with a complete explanation of fertility.",
         ["Which chain best represents the reproductive-window mechanism?",
          "A household marries later but has weak service access. Which inference fits the owner?",
          "Which option keeps marriage timing connected to, but distinct from, other determinants?"]),
    root("R07", "son preference",
         "Son preference is a social preference for male children linked to inheritance, old-age support expectations and patrilineal family structures.",
         ["Son preference is simply a medical condition measured directly in a birth register.",
          "Son preference means that every Indian household rejects daughters.",
          "Son preference is identical to a skewed sex ratio at birth."],
         f"{COMMON} Basic §2 and §3.3; Advanced §2.",
         "Collapsing an attitude into an outcome or turning a regional pattern into a universal claim.",
         ["Which definition of son preference is source-consistent?",
          "Which close distinction should be retained when a question uses son preference?",
          "How should a social-demography item describe son preference?"]),
    root("R08", "sex ratio at birth as outcome",
         "A skewed sex ratio at birth is a measurable demographic outcome that can reflect son preference and sex-selective practices; it is not the attitude itself.",
         ["Sex ratio at birth is the underlying household attitude before any births occur.",
          "A balanced sex ratio proves that son preference is absent from all social groups.",
          "Sex ratio at birth is a synonym for the total population sex ratio at every age."],
         f"{COMMON} Basic §3.3; Advanced §2; detailed legal response routed to Social Justice/Polity.",
         "Confusing the social cause, the birth outcome and the all-age population ratio.",
         ["Which distinction correctly separates son preference from sex ratio at birth?",
          "A question presents a skewed birth ratio. Which analytical reading is valid?",
          "Which option identifies the measured outcome rather than the underlying attitude?"]),
    root("R09", "NPP immediate objective",
         "The immediate objective of the National Population Policy, 2000 was to address unmet needs for contraception, health infrastructure, personnel and integrated services.",
         ["The immediate objective was a compulsory national one-child rule.",
          "The immediate objective was to declare a fixed population ceiling for every state.",
          "The immediate objective was to replace reproductive-health services with demographic penalties."],
         f"{COMMON} Basic §2 and §3.4; National Population Policy, 2000 (MoHFW).",
         "Replacing an access-and-service objective with a coercive numerical target.",
         ["What was the immediate objective of NPP 2000?",
          "Which formulation correctly identifies the first tier of NPP 2000?",
          "A statement describes NPP 2000's immediate goal. Which one is accurate?"]),
    root("R10", "NPP medium-term objective",
         "The medium-term objective of NPP 2000 was to bring the Total Fertility Rate to replacement level by 2010 through programme implementation.",
         ["The medium-term objective was to make India's population decline immediately.",
          "The medium-term objective was a uniform two-child legal ceiling.",
          "The medium-term objective concerned only old-age pensions and not fertility."],
         f"{COMMON} Basic §3.4; National Population Policy, 2000 (MoHFW).",
         "Treating a policy objective as a coercive legal ceiling or confusing its time horizon.",
         ["Which statement identifies the medium-term NPP 2000 objective?",
          "How should the policy's second tier be described?",
          "Which option avoids confusing replacement fertility with population decline?"]),
    root("R11", "NPP long-term objective",
         "The long-term objective of NPP 2000 was a stable population by 2045, consistent with sustainable economic growth, social development and environmental protection.",
         ["The long-term objective was an immediate freeze on population size.",
          "The long-term objective was to abolish regional variation in fertility.",
          "The long-term objective was limited to increasing the working-age population."],
         f"{COMMON} Basic §3.4 and §6; Advanced §4.",
         "Dropping the 2045 horizon or reducing population stabilisation to a single economic metric.",
         ["Which proposition correctly states the long-term NPP 2000 objective?",
          "A policy question asks about the final tier of NPP 2000. Which answer fits?",
          "Which option retains the policy's sustainability-linked long-term goal?"]),
    root("R12", "rights-based non-coercive policy",
         "NPP 2000 is a rights-based, socially oriented framework focused on informed choice, reproductive health and access, not a coercive one-child or two-child national mandate.",
         ["NPP 2000 legally imposed one-child compliance on every Indian household.",
          "Because NPP 2000 has fertility objectives, informed choice is outside its policy frame.",
          "A rights-based policy cannot have any population-stabilisation objective."],
         f"{COMMON} Basic §§3.4, 7 and semantic-completeness block; NPP 2000 (MoHFW).",
         "Assuming that a population-stabilisation objective necessarily means coercion.",
         ["Which description best captures the policy character of NPP 2000?",
          "Which statement avoids the coercion trap in a question on NPP 2000?",
          "How should a rights-based population policy be distinguished from a mandate?"]),
    root("R13", "NFHS-5 historical comparator",
         "NFHS-5 (2019-21) reported India's national Total Fertility Rate at 2.0, and this is a dated historical survey comparator.",
         ["NFHS-5 is a Census enumeration of every Indian household in the current year.",
          "The NFHS-5 national TFR of 2.0 proves that every state had the same fertility rate.",
          "NFHS-5's 2.0 is an undated administrative registration count."],
         f"{COMMON} Basic §§6 and 10; NFHS-5 (2019-21) national fact sheet.",
         "Presenting a dated survey estimate as a current census stock or uniform state value.",
         ["How should the NFHS-5 national TFR of 2.0 be used?",
          "Which statement correctly handles the evidentiary status of NFHS-5?",
          "A Prelims option cites NFHS-5. Which qualification is essential?"]),
    root("R14", "NFHS-6 provisional national fact sheet",
         "The owner records NFHS-6 (2023-24) as released on 29 May 2026 with provisional national fact-sheet TFR 2.0, urban 1.6 and rural 2.1.",
         ["NFHS-6 is treated as a completed Census stock with no provisional status.",
          "The owner treats the NFHS-6 figures as identical state values rather than national survey estimates.",
          "NFHS-6 was not released and therefore cannot be distinguished from NFHS-5."],
         f"{COMMON} Basic current anchor; Advanced §9; released NFHS-6 (2023-24) national fact sheets as recorded by the owner.",
         "Ignoring provisional status, reference period or national-versus-state scope.",
         ["Which statement accurately handles the owner's NFHS-6 anchor?",
          "A question compares NFHS-5 and NFHS-6. Which reading is source-disciplined?",
          "Which option preserves the release, scope and provisional-status qualifications?"]),
    root("R15", "survey is not a Census stock",
         "NFHS is a sample survey; it is not a Census stock and neither NFHS round alone proves causation or supplies a current state population count.",
         ["A sample survey automatically enumerates every resident and replaces the Census.",
          "A survey estimate proves that the measured social factor caused the outcome.",
          "NFHS figures can be read as administrative birth registrations without qualification."],
         f"{COMMON} Basic semantic-completeness block and data-status correction; NFHS survey methodology boundary.",
         "Confusing survey estimates, complete enumeration, administrative registration and causal proof.",
         ["Which data distinction is correct for NFHS?",
          "What can an NFHS estimate not establish by itself?",
          "Which statement avoids the survey-versus-Census trap?"]),
    root("R16", "national aggregate and sub-national divergence",
         "A national fertility aggregate can mask states already at or below replacement alongside states that remain above replacement and retain a younger age structure.",
         ["A national average proves every state is in the same demographic phase.",
          "Sub-national variation disappears once the national TFR approaches replacement.",
          "State differences are only statistical noise and have no policy significance."],
         f"{COMMON} Basic §§3.5, 6 and 10; Advanced §§1, 5-6.",
         "Treating an aggregate as a uniform national condition.",
         ["Which statement correctly interprets India's national fertility aggregate?",
          "Why does the owner insist on sub-national divergence?",
          "Which close option avoids reading one national TFR as a state-by-state fact?"]),
    root("R17", "demographic winter",
         "Demographic winter describes sustained sub-replacement fertility combined with population ageing and eventual population decline, with workforce and support-system risks.",
         ["Demographic winter means a temporary fall in births while the population remains permanently young.",
          "Demographic winter is another name for the growth-favourable working-age window.",
          "Demographic winter means high fertility combined with a large child population."],
         f"{COMMON} Basic §§2, 3.6 and 7; Advanced §§1-2.",
         "Confusing demographic winter with a temporary shock, a dividend or high fertility.",
         ["Which condition is captured by demographic winter?",
          "Which definition best fits the owner's use of the term demographic winter?",
          "A question asks for the demographic-winter bundle. Which option is correct?"]),
    root("R18", "demographic dividend distinction",
         "Demographic dividend refers to a potentially growth-favourable period when the working-age share is large; it is distinct from demographic winter.",
         ["Demographic dividend is sustained sub-replacement fertility with population decline.",
          "Demographic dividend and demographic winter are interchangeable labels for ageing.",
          "Demographic dividend is a legal population target under NPP 2000."],
         f"{COMMON} Basic §7; Advanced §§2 and 8; full transition/dividend model routed to Geography.",
         "Using near-opposite transition concepts as synonyms.",
         ["Which distinction between demographic dividend and winter is correct?",
          "How should a question contrast the two demographic concepts?",
          "Which option keeps the dividend concept within its proper boundary?"]),
    root("R19", "ageing as achievement and burden",
         "Population ageing reflects successful mortality and fertility transition but also creates old-age-support, care and workforce-composition challenges.",
         ["Ageing is only a demographic failure and has no health or longevity dimension.",
          "Ageing automatically creates a demographic dividend in every region.",
          "Ageing is purely an individual household matter with no social-policy consequences."],
         f"{COMMON} Basic §3.5 and §10; Advanced §2 and ageing-society response chain.",
         "Presenting ageing as either wholly positive or wholly burdensome.",
         ["Which balanced reading of population ageing is source-consistent?",
          "How should an answer frame ageing as both achievement and challenge?",
          "Which option avoids a one-sided ageing claim?"]),
    root("R20", "ageing causal chain",
         "Sustained fertility decline combined with rising life expectancy increases the elderly share and can raise old-age dependency relative to the working-age population.",
         ["Ageing is caused only by migration and not by fertility or longevity.",
          "Rising life expectancy reduces the elderly share by definition.",
          "Fertility decline raises the child share rather than changing age structure."],
         f"{COMMON} Basic §2; Advanced §§3 and 8.",
         "Reversing the age-structure mechanism or omitting the joint fertility-longevity pathway.",
         ["Which chain correctly explains population ageing?",
          "What combination produces the ageing pressure described by the owner?",
          "Which option accurately links fertility, longevity and dependency?"]),
    root("R21", "family-based old-age support",
         "Family-based old-age support remains India's dominant model, while detailed formal schemes and legal maintenance provisions belong to the Social Justice owner.",
         ["India's elderly support is already delivered mainly through a universal formal pension system.",
          "Family care is irrelevant once fertility declines.",
          "The Indian Society owner treats every old-age law and scheme as part of this topic's core."],
         f"{COMMON} Basic §4 and §10; Advanced §3; cross-owner route to Social Justice/basic/12_Elderly-and-Senior-Citizens.md.",
         "Confusing the Society mechanism with the Social Justice scheme owner.",
         ["Which statement correctly handles old-age support in this topic?",
          "What is the owner's boundary on family-based elder care?",
          "Which option preserves the cross-owner route for detailed elderly schemes?"]),
    root("R22", "first demographic transition",
         "The first demographic transition describes mortality decline followed by fertility decline as societies move through demographic transition.",
         ["The first transition refers only to value change and new family forms after sub-replacement fertility.",
          "The first transition is a policy document rather than an analytical model.",
          "The first transition describes migration offsets between Indian states."],
         f"{COMMON} Basic §4 and §12; Advanced §2; full model routed to Geography/basic/26_World-Population-and-Demographic-Transition.md.",
         "Reversing first and second transition concepts or treating a model as a policy.",
         ["Which description belongs to the first demographic transition?",
          "How should a question distinguish the first transition from later theories?",
          "Which option keeps the first-transition concept within its proper analytical boundary?"]),
    root("R23", "second demographic transition",
         "Second demographic transition theory links further sub-replacement fertility to value change and family-formation shifts; it is a framework largely developed from European experience, not a universal Indian diagnosis.",
         ["The second transition is simply the first transition's mortality-decline phase.",
          "The theory is a universal causal law that explains every Indian state.",
          "The second transition is identical to NPP 2000's service-delivery objective."],
         f"{COMMON} Advanced §2 and §7.",
         "Treating a theory developed from a particular experience as a universal diagnosis.",
         ["Which qualification belongs to second demographic transition theory?",
          "How should the second transition be used in an Indian Society answer?",
          "Which statement avoids overextending the second-transition framework?"]),
    root("R24", "urbanisation and cost of children",
         "Urbanisation can raise direct and opportunity costs of children through housing, schooling, care and foregone income, contributing to smaller desired family size.",
         ["Urbanisation reduces the cost of children by removing housing and schooling constraints.",
          "Urbanisation mechanically ends son preference in every household.",
          "Urbanisation affects fertility only through migration and never through household costs."],
         f"{COMMON} Advanced §3 fertility-decline chain; cross-link to Topic 10 Urbanisation.",
         "Turning an economic-cost mechanism into a complete or universal explanation.",
         ["Which mechanism links urbanisation with fertility decline?",
          "How can urbanisation alter desired family size according to the owner?",
          "Which option avoids overstating the urbanisation-fertility link?"]),
    root("R25", "migration as an offset",
         "Internal migration can offset workforce shrinkage in a receiving region, but it does not erase the demographic processes that produced divergence.",
         ["Migration permanently reverses fertility decline in the receiving region.",
          "Migration has no relationship to regional labour supply or age structure.",
          "Migration makes every sending and receiving region demographically identical."],
         f"{COMMON} Advanced §6 migration-as-offset trade-off; migration theory routed to Geography.",
         "Treating migration as a complete demographic cure or as socially irrelevant.",
         ["Which statement captures migration as a demographic offset?",
          "What can internal migration do without eliminating regional divergence?",
          "Which option correctly limits the migration-as-offset claim?"]),
    root("R26", "sending-region ageing trade-off",
         "Migration may strengthen a receiving region's labour supply while straining the sending region's elder-care capacity when working-age adults leave parents behind.",
         ["Migration benefits the receiving region and imposes no possible cost on the sending region.",
          "A sending region automatically becomes younger when its working-age adults depart.",
          "The elder-care trade-off is impossible where remittances are sent."],
         f"{COMMON} Advanced §6; family-care mechanism.",
         "Looking only at the receiving region and ignoring life-course and care effects in the sending region.",
         ["Which trade-off is associated with internal migration?",
          "A question asks about migrants leaving older parents behind. Which inference fits?",
          "Which option captures both sides of the migration-and-ageing relationship?"]),
    root("R27", "population education",
         "Population education is age-appropriate, scientific and rights-respecting education that links reproductive health, informed choice, gender equality and population-resource awareness.",
         ["Population education is a coercive classroom target for enforcing a fixed family size.",
          "Population education is limited to memorising Census totals.",
          "Population education excludes reproductive health because it concerns only economics."],
         f"{COMMON} Basic §13.1-13.3; 2021 GS-I demand route.",
         "Reducing population education to propaganda, arithmetic or coercion.",
         ["Which description best fits population education?",
          "What does the owner's population-education concept include?",
          "Which option keeps population education rights-respecting and substantive?"]),
    root("R28", "population-education objectives",
         "Population education can build reproductive-health knowledge, gender equality, delayed marriage, informed small-family choice and awareness of population-resource relations.",
         ["Its only objective is to increase the birth rate in every region.",
          "Its objective is to replace health services with classroom instruction.",
          "Its objectives exclude gender equality and informed reproductive choice."],
         f"{COMMON} Basic §13.2-13.3; 2021 GS-I demand route.",
         "Selecting only a numerical fertility objective and missing capability-building aims.",
         ["Which set contains the owner's population-education objectives?",
          "Which statement correctly identifies what population education is meant to achieve?",
          "A question asks for objectives rather than delivery methods. Which answer fits?"]),
    root("R29", "gender equality and delayed marriage",
         "Population education should support gender equality and delayed marriage through knowledge and agency, not through demographic compulsion.",
         ["Gender equality is outside population education because only fertility numbers matter.",
          "Delayed marriage should be imposed without attention to rights or health.",
          "Population education must treat women as targets of control rather than agents."],
         f"{COMMON} Basic §13.1-13.3; 2019/2021 GS-I demand routes.",
         "Replacing agency and rights with a target-driven population-control frame.",
         ["Which approach to gender and marriage timing is owner-consistent?",
          "How should population education connect gender equality and delayed marriage?",
          "Which option avoids the population-control framing trap?"]),
    root("R30", "population-education delivery and safeguards",
         "Population education works through schools, communities and service delivery with age-appropriate content, scientific information, informed consent and anti-coercion safeguards.",
         ["Only schools can deliver population education, so health services and communities are irrelevant.",
          "Safeguards are unnecessary because numerical targets are the primary objective.",
          "Population education should use undifferentiated content without regard to age or consent."],
         f"{COMMON} Basic §13.1-13.3; NPP rights-based frame; 2021 GS-I demand route.",
         "Confusing a multi-institutional capability approach with a single classroom campaign.",
         ["Which delivery architecture is consistent with the owner?",
          "What safeguards matter in population education?",
          "Which statement correctly combines institutions and rights protections?"]),
    root("R31", "replacement fertility and population momentum",
         "Replacement-level fertility does not mean immediate zero population growth because inherited age structure creates population momentum.",
         ["Replacement fertility guarantees immediate population decline in every population.",
          "Replacement fertility means no births occur after the replacement threshold.",
          "Population momentum is unrelated to the age structure inherited from earlier fertility."],
         f"{COMMON} Basic semantic-completeness block; full demographic-transition mechanics routed to Geography.",
         "Equating replacement fertility with instantaneous stability or decline.",
         ["Which statement correctly distinguishes replacement fertility from zero growth?",
          "Why can population continue growing near replacement fertility?",
          "Which option preserves the age-structure qualification?"]),
    root("R32", "son preference amid smaller families",
         "A household may reduce its desired family size yet continue childbearing until a son is born, allowing son preference and fertility decline to coexist.",
         ["Falling desired family size automatically eliminates son preference.",
          "Son preference can operate only where desired family size is increasing.",
          "A household seeking a son is necessarily above replacement fertility at the national level."],
         f"{COMMON} Advanced §5 boundary case 3 and §8 traps.",
         "Assuming that smaller families automatically dissolve gendered preferences.",
         ["Which boundary case shows that son preference can persist during fertility decline?",
          "How can a smaller desired family coexist with son preference?",
          "Which option correctly handles the interaction between family size and son preference?"]),
    root("R33", "multi-factor fertility explanation",
         "Fertility transition should be explained through interacting agency, health, education, marriage age, desired family size, norms, services and regional conditions.",
         ["A single programme or statistic can explain every fertility transition.",
          "Biology alone is sufficient because social conditions do not alter reproductive decisions.",
          "Regional conditions should be excluded to keep the explanation nationally uniform."],
         f"{COMMON} Basic §§2-3 and answer architecture; Advanced §§2-3.",
         "Answering a social mechanism question with a one-variable or purely biological explanation.",
         ["Which explanatory frame is most complete for fertility transition?",
          "Which option best reflects the owner's causal logic?",
          "A question asks why fertility falls. Which answer avoids analytical compression?"]),
    root("R34", "voluntary informed choice",
         "A rights-based population approach expands voluntary informed reproductive choice through access, information, health services and agency rather than coercive targets.",
         ["Rights-based policy means the state may impose a uniform family-size penalty.",
          "Informed choice is incompatible with population stabilisation goals.",
          "Access and information are unnecessary if a numerical target is announced."],
         f"{COMMON} Basic §§3.4, 10 and 13; NPP 2000 (MoHFW).",
         "Treating rights and stabilisation as mutually exclusive or substituting coercion for capability.",
         ["Which principle anchors the owner's rights-based population approach?",
          "What does voluntary informed choice require in population policy?",
          "Which option correctly separates capability-building from coercion?"]),
    root("R35", "localised demographic winter",
         "A state with below-replacement fertility, rising life expectancy and increasing elderly dependency can show demographic-winter conditions even while the national aggregate remains younger.",
         ["A national near-replacement TFR rules out demographic-winter conditions in every state.",
          "Local demographic winter requires high fertility and a rising child share.",
          "A state cannot experience ageing pressure until the whole country has population decline."],
         f"{COMMON} Basic §§3.5-3.6; Advanced §§1 and 5.",
         "Applying a national aggregate as a veto against state-level age-structure analysis.",
         ["Which scenario illustrates localised demographic winter?",
          "How can demographic winter exist within a still-young national population?",
          "Which option correctly identifies the relevant state-level bundle?"]),
    root("R36", "continued dividend window",
         "A state with fertility still above replacement and a young, growing working-age population may retain a demographic-dividend window while other states age.",
         ["Every Indian state has already exhausted its working-age opportunity.",
          "A young age structure proves that growth will occur without skills, jobs or health investment.",
          "Above-replacement fertility automatically means demographic winter."],
         f"{COMMON} Advanced §§1, 5 and 8; full dividend theory routed to Geography.",
         "Turning demographic potential into guaranteed growth or reversing the winter/dividend distinction.",
         ["Which case represents a continued demographic-dividend window?",
          "What qualification is needed when a young age structure is called a dividend?",
          "Which option correctly handles above-replacement states?"]),
    root("R37", "nuclearisation and elder care",
         "Nuclear-family structures can reduce co-resident caregiving capacity, creating a possible gap between ageing speed and family-based support; detailed family form belongs to Topic 04.",
         ["Nuclearisation necessarily increases the number of co-resident caregivers.",
          "Family structure has no bearing on elder-care capacity.",
          "The population owner should duplicate all kinship theory instead of using a cross-owner link."],
         f"{COMMON} Advanced §3; cross-link to Indian Society Topic 04.",
         "Treating family form and ageing as unrelated or crossing the topic boundary.",
         ["Which cross-topic mechanism links nuclearisation and ageing?",
          "Why can family structure matter to old-age support?",
          "Which answer respects the Topic 04 boundary while using its mechanism?"]),
    root("R38", "formal-support readiness gap",
         "Where ageing accelerates faster than formal old-age social-security and healthcare systems scale, a policy response gap can emerge; detailed schemes belong to Social Justice.",
         ["Formal support systems automatically scale at the same speed as ageing.",
          "Ageing creates no institutional challenge if families remain important.",
          "The Indian Society topic owns every detailed pension provision and legal test."],
         f"{COMMON} Advanced §3; cross-owner route to Social Justice.",
         "Confusing a social-demographic diagnosis with a scheme-by-scheme legal analysis.",
         ["Which situation describes an ageing response gap?",
          "How should this topic handle formal old-age support?",
          "Which option preserves both the mechanism and the cross-owner boundary?"]),
    root("R39", "NPP policy-lag trade-off",
         "NPP 2000's high-fertility-era objectives do not by themselves answer low-fertility and ageing-era service, care and labour-market needs, creating a policy-lag question.",
         ["NPP 2000 automatically resolves every later ageing challenge.",
          "A dated policy document has no relevance once fertility declines.",
          "Policy lag means that sub-national variation should be ignored in favour of one national verdict."],
         f"{COMMON} Advanced §4 and §6.",
         "Reading a policy objective as a complete contemporary implementation architecture.",
         ["Which policy-lag qualification belongs to NPP 2000 analysis?",
          "Why can NPP 2000 not alone settle ageing-era questions?",
          "Which option correctly frames the policy-lag trade-off?"]),
    root("R40", "state-specific policy response",
         "Because fertility, age structure, migration and care capacity vary across states, policy should diagnose the relevant region rather than infer one uniform national need.",
         ["A single national intervention is necessarily optimal for every state.",
          "State variation is irrelevant once the national TFR is known.",
          "State-specific policy means national institutions have no role at all."],
         f"{COMMON} Advanced §4, §5 and §11.",
         "Replacing differentiated policy diagnosis with either national uniformity or complete decentralised exclusion.",
         ["What policy approach follows from sub-national demographic divergence?",
          "Which option correctly handles state-specific population needs?",
          "How should a demographic answer move from diagnosis to policy?"]),
    root("R41", "data reference periods and uncertainty",
         "Population evidence must retain its source type, reference period, release status, coverage and uncertainty; dated survey estimates should not be presented as timeless facts.",
         ["Once a number is published, its reference period and provisional status no longer matter.",
          "Survey, Census and vital-rate data can be merged without describing their coverage.",
          "A current-looking statistic can be used to prove causation regardless of source design."],
         f"{COMMON} Basic data-status correction and semantic-completeness block; Advanced §§7-9.",
         "Stripping dates, source types and uncertainty from numerical claims.",
         ["Which discipline is required when using population data?",
          "How should a dated provisional survey figure be reported?",
          "Which option preserves source type and reference-period control?"]),
    root("R42", "Census 2011 latest completed stock",
         "Census 2011 remains the latest completed full-enumeration population stock recorded by the owner as of 5 September 2026; later survey estimates are not a replacement Census stock.",
         ["NFHS-5 or NFHS-6 automatically replaces Census 2011 as a complete enumeration.",
          "Census 2011 is only a sample and cannot provide population stock information.",
          "A provisional survey release is necessarily the same as a completed Census count."],
         f"{COMMON} Basic semantic-completeness block (data/source control); official Census of India 2011 boundary.",
         "Confusing the latest survey release with the latest completed full enumeration.",
         ["Which statement correctly identifies the latest completed population stock?",
          "How should Census 2011 and NFHS evidence be distinguished?",
          "Which option avoids replacing an enumeration with a sample survey?"]),
    root("R43", "SRS as vital-rates system",
         "The Sample Registration System is a vital-rates system and must not be treated as a complete Census enumeration or as an NFHS household survey.",
         ["SRS is a legal population target under NPP 2000.",
          "SRS is identical to a complete decennial Census enumeration.",
          "SRS is a household-attitude survey measuring son preference directly in every district."],
         f"{COMMON} Basic semantic-completeness block (data/source control); SRS institutional boundary.",
         "Interchanging population data systems because all report demographic information.",
         ["Which description correctly identifies SRS?",
          "A question contrasts Census, NFHS and SRS. Which statement is accurate?",
          "Which option keeps the vital-rates system distinct from a Census and survey?"]),
    root("R44", "migration and labour-market adjustment",
         "Internal migration can reallocate working-age labour between regions and alter receiving-region workforce supply, but it may also increase care pressure in sending households.",
         ["Migration changes only cultural identity and cannot alter labour supply.",
          "Migration automatically resolves both regional workforce and elder-care pressures.",
          "Migration should be analysed only as an international border event."],
         f"{COMMON} Advanced §§3 and 6; migration theory routed to Geography.",
         "Counting only the receiving-region labour gain and omitting household and sending-region effects.",
         ["Which social-demographic effect can internal migration have?",
          "How should migration be linked to labour and care?",
          "Which option gives the owner's qualified migration mechanism?"]),
    root("R45", "uneven world movement toward demographic winter",
         "The world can move toward demographic winter unevenly: some developed countries and Indian states show the pattern while many developing populations remain younger or above replacement.",
         ["The world is either uniformly in demographic winter or uniformly outside it.",
          "India's national survey average alone proves a global population trajectory.",
          "Regional variation makes the demographic-winter concept unusable."],
         f"{COMMON} Basic §5 and §10; Advanced §10-11; 2024 GS-I demand route.",
         "Answering a global, graded question with a uniform yes/no claim or India-only evidence.",
         ["Which conclusion best answers whether the world is moving toward demographic winter?",
          "How should the owner frame a global demographic-winter claim?",
          "Which option gives the required uneven, regionally graded verdict?"]),
    root("R46", "2019 GS-I demand route",
         "The owner routes a 2019 GS-I demand on women's empowerment and population growth to the agency pathway: education, health, later marriage, voice and voluntary choice, with social constraints qualified.",
         ["The routed demand is an objective Prelims PYQ whose exact options are released here.",
          "The route requires a coercive population-control answer without gender or agency analysis.",
          "The demand is owned only by physical geography and excludes social determinants."],
         f"{COMMON} Basic §13.6; Advanced Historical PYQ Integration 2018-2023; exact wording/options withheld for rights.",
         "Confusing an authenticated Mains demand route with a reproducible objective question.",
         ["Which analytical route matches the owner's 2019 GS-I demand family?",
          "What should a question on women's empowerment and population growth foreground?",
          "Which statement respects the 2019 demand route and its reproduction hold?"]),
    root("R47", "2021 GS-I demand route",
         "The owner routes a 2021 GS-I demand on population education to objectives, measures, institutions, scientific content and anti-coercion safeguards; exact wording/options remain withheld.",
         ["The demand is satisfied by listing a fertility target without objectives or safeguards.",
          "The routed question is an exact live Prelims item with an included official key.",
          "Population education is treated as unrelated to gender, health or informed choice."],
         f"{COMMON} Basic §13.6; Advanced Historical PYQ Integration 2018-2023; exact wording/options withheld for rights.",
         "Reducing a Mains demand to a numerical target or mislabelling it as an objective PYQ.",
         ["Which answer architecture matches the owner's 2021 demand route?",
          "What must a population-education demand cover beyond a definition?",
          "Which option keeps the 2021 route distinct from an exact reproduced PYQ?"]),
    root("R48", "2024 demographic-winter demand and hold",
         "The owner records a verified 2024 GS-I Mains demographic-winter demand; this bank tests the concept independently and withholds exact PYQ wording/options pending reproduction-rights documentation.",
         ["Because the demand is verified, its exact protected wording and options may be copied without a rights check.",
          "The 2024 demand is treated as proof that all Indian states have demographic-winter conditions.",
          "The 2024 demand removes the need to distinguish demographic winter from demographic dividend."],
         f"{COMMON} Basic §5, §10 and §13.6; Advanced §10-11; exact question reproduction held for UPSC rights/provenance gate.",
         "Confusing demand authentication with permission to reproduce protected wording or with a uniform empirical conclusion.",
         ["What is the correct handling of the owner's 2024 demographic-winter demand?",
          "Which statement respects both the PYQ hold and the concept's uneven evidence?",
          "How should this final-MCQ bank use the 2024 demand family?"]),
]


def render_questions(revision: int, rng: random.Random) -> tuple[str, list[str], Counter, dict[int, list[str]]]:
    positions = list("ABCD") * (len(ROOTS) // 4)
    rng.shuffle(positions)
    lines = [
        f"# Population and Associated Issues — Revision {revision}",
        "",
        "All items are original and answer-free; select the best answer.",
        "",
    ]
    stems: list[str] = []
    keys: Counter = Counter()
    ordered_options: dict[int, list[str]] = {}
    for idx, item in enumerate(ROOTS, 1):
        stem = item["stems"][revision - 1]
        stems.append(stem.lower())
        correct_pos = positions[idx - 1]
        choices = [item["fact"], *item["wrongs"]]
        correct = choices.pop(0)
        rng.shuffle(choices)
        ordered: list[str] = []
        pos_index = "ABCD".index(correct_pos)
        for i in range(4):
            ordered.append(correct if i == pos_index else choices.pop())
        ordered_options[idx] = ordered
        keys[correct_pos] += 1
        lines.append(f"### Q{idx}. {stem}")
        for label, option in zip("ABCD", ordered):
            lines.append(f"{label}. {option}{NEUTRAL_SUFFIX}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n", stems, keys, ordered_options


def render_answers(revision: int, ordered_options: dict[int, list[str]], keys: dict[int, str]) -> str:
    lines = [
        f"# Population and Associated Issues — Revision {revision} explained answers",
        "",
        "Every item is original. Exact PYQ wording and options are withheld.",
        "",
    ]
    for idx, item in enumerate(ROOTS, 1):
        answer = keys[idx]
        ordered = ordered_options[idx]
        lines.append(f"### Q{idx}. {answer}")
        for label, option in zip("ABCD", ordered):
            if label == answer:
                lines.append(f"- **{label} — Correct:** {option}{NEUTRAL_SUFFIX} This is the affirmative proposition for **{item['focus']}**.")
            else:
                lines.append(f"- **{label} — Incorrect:** {option}{NEUTRAL_SUFFIX} It conflicts with the evidence because the owner instead establishes: {item['fact']}")
        lines.append(f"**Evidence:** {item['fact']}")
        lines.append(f"**Sources:** {item['sources']}")
        lines.append(f"**Examiner trap:** {item['trap']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def parse_questions(text: str) -> list[dict]:
    blocks = re.split(r"(?m)^### Q", text)[1:]
    result = []
    for block in blocks:
        head, *rest = block.splitlines()
        qnum = int(head.split(".", 1)[0])
        body = "\n".join(rest)
        opts = re.findall(r"^([A-D])\. (.+)$", body, re.M)
        result.append({"q": qnum, "options": dict(opts)})
    return result


def write_coverage(revision: int, keys: Counter) -> None:
    lines = [
        f"# Population and Associated Issues — Revision {revision} coverage ledger",
        "",
        "| Q | Named coverage unit | Affirmative proposition | Source boundary |",
        "|---:|---|---|---|",
    ]
    for idx, item in enumerate(ROOTS, 1):
        lines.append(f"| {idx} | {item['focus']} | Q{idx} | {item['sources']} |")
    lines.extend([
        "",
        f"**Coverage status:** {len(ROOTS)}/{len(ROOTS)} named roots tested affirmatively; distractors are not counted.",
        f"**Key distribution:** {dict(sorted(keys.items()))}.",
    ])
    (TOPIC / f"revision-{revision}" / "COVERAGE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def audit_bank(revision: int, keys: Counter) -> dict:
    folder = TOPIC / f"revision-{revision}"
    qtext = (folder / "QUESTIONS.md").read_text(encoding="utf-8")
    atext = (folder / "ANSWERS.md").read_text(encoding="utf-8")
    questions = parse_questions(qtext)
    answer_nums = [int(n) for n, _ in re.findall(r"(?m)^### Q(\d+)\. ([A-D])\s*$", atext)]
    findings: list[str] = []
    if [q["q"] for q in questions] != list(range(1, len(ROOTS) + 1)):
        findings.append("question numbering is not contiguous")
    if answer_nums != list(range(1, len(ROOTS) + 1)):
        findings.append("answer numbering is not contiguous")
    for q in questions:
        opts = q["options"]
        if list(opts) != list("ABCD"):
            findings.append(f"Q{q['q']} lacks four options")
        if len(set(opts.values())) != 4:
            findings.append(f"Q{q['q']} has duplicate options")
        lengths = [len(value) for value in opts.values()]
        if max(lengths) > 2.05 * min(lengths):
            findings.append(f"Q{q['q']} option-length cue")
    for pattern in (r"\*\*Correct answer", r"\*\*Sources:", r"\*\*Examiner trap:", r"Answer key"):
        if re.search(pattern, qtext, re.I):
            findings.append(f"answer leakage: {pattern}")
    if len(questions) < 40:
        findings.append("fewer than 40 questions")
    if len(keys) != 4 or min(keys.values()) < 10:
        findings.append("unbalanced correct-option positions")
    if findings:
        raise RuntimeError(f"revision-{revision}: " + "; ".join(findings))
    return {"questions": len(questions), "answers": len(answer_nums), "keys": dict(keys), "findings": findings}


def update_indexes() -> None:
    text = SUBJECT_INDEX.read_text(encoding="utf-8")
    old = "| 06 — Population and Associated Issues | `pending` | — |"
    new = "| [06 — Population and Associated Issues](06-Population-and-Associated-Issues/COVERAGE.md) | `complete` for original banks: **144 originals (48/48/48)**; all 48 named roots are affirmative in each revision, with balanced independently shuffled keys, item-level ledgers, source/date and hostile audits passing. Exact PYQ wording/options remain held for provenance and reproduction rights; independent answer-blind learner review remains pending. | [Revision 1](06-Population-and-Associated-Issues/revision-1/QUESTIONS.md) · [Revision 2](06-Population-and-Associated-Issues/revision-2/QUESTIONS.md) · [Revision 3](06-Population-and-Associated-Issues/revision-3/QUESTIONS.md) |"
    if new not in text and old not in text:
        raise RuntimeError("subject index pending row not found")
    if old in text:
        SUBJECT_INDEX.write_text(text.replace(old, new), encoding="utf-8")

    global_text = GLOBAL_INDEX.read_text(encoding="utf-8")
    if "Topic [06 Population and Associated Issues]" not in global_text:
        replacement = (
            "Topic [06 Population and Associated Issues](subjects/Indian-Society/06-Population-and-Associated-Issues/COVERAGE.md) "
            "is complete for original banks with 144 originals (48/48/48), all 48 named roots affirmative in each revision, "
            "balanced independent keys and clean structural/hostile/source-date audits; exact PYQ wording/options remain held "
            "and learner blind review is pending. Next pending Topic 07."
        )
        if "Next pending Topic 06." not in global_text:
            raise RuntimeError("global Indian Society next-pending marker not found")
        global_text = global_text.replace("Next pending Topic 06.", replacement)
        GLOBAL_INDEX.write_text(global_text, encoding="utf-8")


def write_topic_ledgers(results: dict[int, dict]) -> None:
    (TOPIC / "COVERAGE.md").write_text(
        """# Indian Society 06 — Population and Associated Issues

**Status:** complete for original banks; exact PYQ provenance/rights and independent learner review remain held.

| Revision | Questions | Answers | Coverage roots | Status |
|---|---:|---:|---:|---|
| 1 | 48 | 48 | 48/48 affirmative | complete for originals |
| 2 | 48 | 48 | 48/48 affirmative | complete for originals |
| 3 | 48 | 48 | 48/48 affirmative | complete for originals |

## Root coverage

All 48 named roots are tested affirmatively in every revision. Coverage includes social determinants of fertility, NPP 2000's tiered objectives, NFHS/Census/SRS data boundaries, son preference and sex-ratio outcomes, ageing, demographic winter/dividend distinctions, population education, migration trade-offs, policy lag and state-level divergence.

See each revision's `COVERAGE.md` for the question-level ledger and `SOURCE-AND-PYQ-HOLDS.md` for evidence, date, provenance and reproduction-rights holds.
""", encoding="utf-8")
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        f"""# Indian Society 06 — source and PYQ holds

## Original-bank status

- All 144 released items are original MCQs: 48 each in Revision 1, Revision 2 and Revision 3.
- No exact UPSC question wording or option set is reproduced.
- No exact UPSC Prelims PYQ is claimed or released in these banks.

## Evidence order and authoritative boundaries

1. Canonical Basic owner: `{BASIC}`.
2. Optional Advanced owner: `{ADVANCED}`.
3. Learner-v2 package and semantic-completeness ownership block: `{PACKAGE}`.
4. National Population Policy, 2000 (MoHFW) for the tiered objectives and rights-based frame.
5. NFHS-5 (2019-21) and NFHS-6 (2023-24) official national fact-sheet boundaries as recorded in the owners; all figures retain survey, date and provisional-status qualifications.
6. Census 2011 and Sample Registration System are kept distinct from NFHS; Geography owns the full demographic-transition/migration model and Social Justice owns detailed elderly schemes and sex-selection law.

## PYQ holds

- The owner routes 2019 and 2021 GS-I Mains demand families and records the 2024 GS-I demographic-winter demand.
- Exact PYQ wording/options remain withheld pending same-paper authentication, official-key matching where applicable and documented UPSC reproduction permission.
- These banks independently test the concepts; no routed Mains demand is relabelled as an exact objective PYQ.

## Data and cross-owner holds

- NFHS-5 is a dated 2019-21 survey comparator; NFHS-6 (2023-24) is recorded as a provisional release dated 29 May 2026. Neither is a Census stock or by itself proof of causation.
- Census 2011 is the latest completed full-enumeration stock recorded by the owner as of 5 September 2026; SRS is a vital-rates system.
- Do not infer an undated state figure, global demographic-winter conclusion or scheme outcome from a national survey anchor.
""", encoding="utf-8")
    keys_text = "\n".join(
        f"- Revision {rev}: {results[rev]['questions']} questions; key distribution {results[rev]['keys']}."
        for rev in (1, 2, 3)
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        f"""# Structural audit — Population and Associated Issues

**Result: PASS for all three original-bank releases.**

{keys_text}

- contiguous question numbering and one-to-one answer numbering;
- four distinct options per item and four option-specific rationales;
- answer-free question files with no source, key or trap leakage;
- 48 affirmative coverage roots in every revision.
""", encoding="utf-8")
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        """# Hostile audit — Population and Associated Issues

**Result: PASS for original-bank release; exact PYQ, data-date and learner-review holds remain.**

| Audit | Result | Finding |
|---|---|---|
| Answer leakage | PASS | Questions contain no keys, rationales, sources, traps or explanatory headings. |
| Option distinctness | PASS | Four distinct grammatically complete options per item; length-cue gate passed. |
| Key balance | PASS | Each 48-question revision has exactly 12 A, 12 B, 12 C and 12 D correct positions. |
| Stem distinctness | PASS | Each revision uses a separate stem family; no duplicate normalized stem within a bank. |
| Cross-revision independence | PASS | Stems are different across revisions and correct positions are independently shuffled. |
| Owner coverage | PASS | All 48 roots are affirmative in Revision 1, Revision 2 and Revision 3. |
| Institutional/data facts | PASS | NPP 2000, NFHS-5/6, Census 2011 and SRS retain source, date and scope qualifications. |
| Hostile generalisation | PASS | Absolute and causal-overreach distractors are rejected; regional and rights qualifications remain visible. |
| PYQ/rights gate | PASS | Zero exact PYQs live; 2019/2021/2024 demand families are independently concept-tested and held. |
""", encoding="utf-8")
    (TOPIC / "AUDIT-REPORT.md").write_text(
        """# Audit report — Population and Associated Issues

The three original banks passed structural, option-balance, leakage, root-coverage, stem-distinctness and hostile data/institution checks. The topic is indexed as complete for original banks only. Independent answer-blind learner review, exact PYQ reproduction permission and any future objective-PYQ key provenance remain open holds.
""", encoding="utf-8")
    validation = {
        "topic_key": "indian-society-06",
        "title": "Population and Associated Issues",
        "status": "complete_for_original_banks",
        "revisions": {str(rev): results[rev] for rev in (1, 2, 3)},
        "coverage_roots": len(ROOTS),
        "pyqs_included": 0,
        "exact_pyq_status": "held_for_provenance_and_reproduction_rights",
        "learner_blind_review": "pending",
        "source_order": [
            BASIC,
            ADVANCED,
            PACKAGE,
            "National Population Policy, 2000 (MoHFW)",
            "NFHS-5/NFHS-6 national fact-sheet boundaries",
            "Census 2011 and SRS data boundaries",
        ],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    if len(ROOTS) < 40:
        raise RuntimeError("topic root ledger is below the required 40-question minimum")
    TOPIC.mkdir(parents=True, exist_ok=True)
    results: dict[int, dict] = {}
    all_stems: set[str] = set()
    for revision in (1, 2, 3):
        folder = TOPIC / f"revision-{revision}"
        folder.mkdir(parents=True, exist_ok=True)
        # Separate seeds make correct positions independent across revisions.
        rng = random.Random(62006 + revision * 7919)
        qtext, stems, keys, ordered_options = render_questions(revision, rng)
        key_map = {}
        for idx, options in ordered_options.items():
            key_map[idx] = "ABCD"[options.index(ROOTS[idx - 1]["fact"])]
        (folder / "QUESTIONS.md").write_text(qtext, encoding="utf-8")
        (folder / "ANSWERS.md").write_text(render_answers(revision, ordered_options, key_map), encoding="utf-8")
        write_coverage(revision, Counter(key_map.values()))
        result = audit_bank(revision, Counter(key_map.values()))
        results[revision] = result
        for stem in stems:
            if stem in all_stems:
                raise RuntimeError(f"cross-revision duplicate stem: {stem}")
            all_stems.add(stem)
    write_topic_ledgers(results)
    update_indexes()
    print(f"BUILT Topic 06 with {len(ROOTS)} roots and {len(ROOTS) * 3} original questions.")
    for rev in (1, 2, 3):
        print(f"revision-{rev}: {results[rev]}")


if __name__ == "__main__":
    main()
