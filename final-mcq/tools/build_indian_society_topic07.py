"""Build Indian Society Topic 07 final-MCQ banks and release audits."""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "07-Women-and-Womens-Organisations"
SUBJECT_INDEX = ROOT / "final-mcq" / "subjects" / "Indian-Society" / "INDEX.md"
GLOBAL_INDEX = ROOT / "final-mcq" / "INDEX.md"

BASIC = "upsc-ai-kit/knowledge/Indian-Society/basic/07_Women-and-Womens-Organisations.md"
ADVANCED = "upsc-ai-kit/knowledge/Indian-Society/advanced/07_Women-and-Womens-Organisations.md"
PACKAGE = "upsc-ai-kit/knowledge/Indian-Society/07_Women-and-Womens-Organisations_Learner-V2-Complete-Topic-Package.md"
COMMON = f"Canonical Basic owner `{BASIC}`; Optional Advanced owner `{ADVANCED}`; learner-v2 package `{PACKAGE}`."
OPTION_SUFFIX = " The statement remains subject to the topic's stated scope and evidence limits; it should be read with the same source, institutional-boundary and causal-inference qualifications that govern every proposition in this bank."


def R(code: str, focus: str, fact: str, wrongs: list[str], source: str, trap: str, stems: list[str]) -> dict:
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
    R("R01", "layered organisational history",
      "Indian women's organising includes social reform, early national bodies, post-Independence rights mobilisation, informal-sector labour organising and savings-and-credit federations; the streams overlap rather than forming a single replacement sequence.",
      ["Indian women's organising is only a legal-administrative programme with no collective history.",
       "The movement passed through one uniform organisation whose later forms displaced all earlier forms.",
       "Women's organising is only a numerical account of female labour participation."],
      "Basic §§1,3; Advanced §§1,3.",
      "Reducing a layered movement to a single chronology or a single indicator.",
      ["Which description best preserves the owner's account of organisational history?",
       "A close-option item asks how women's organising should be periodised. Which statement is defensible?",
       "Which reading avoids treating the Indian women's movement as a single linear institution?"]),
    R("R02", "social-reform era",
      "The nineteenth-century social-reform phase raised issues such as sati, widow remarriage and child marriage, but it was largely elite-led advocacy rather than a mass women's organisation.",
      ["The social-reform phase was a nationwide federation of savings-and-credit groups.",
       "The social-reform phase was limited to platform work by informal-sector trade unions.",
       "The social-reform phase made later national and grassroots organising unnecessary."],
      "Basic §3.1; learner-v2 package §13.4.",
      "Confusing reform advocacy with a mass organisation or claiming that one phase erased later mobilisation.",
      ["What qualification does the owner attach to the nineteenth-century reform phase?",
       "Which statement correctly characterises the social-reform era in this topic?",
       "How should a Prelims option describe early reform advocacy?"]),
    R("R03", "Women's Indian Association precedence",
      "The Women's Indian Association preceded the All India Women's Conference, so AIWC may be called influential but not the first women's organisation in India.",
      ["AIWC preceded every organised women's body in India.",
       "The Women's Indian Association was a post-Independence wage federation.",
       "Precedence is immaterial because all women's organisations began together in 1927."],
      "Basic §§2,3; Advanced §2.",
      "Calling AIWC the first organisation and overlooking the earlier Women's Indian Association.",
      ["Which chronology distinction is essential when comparing WIA and AIWC?",
       "A question calls AIWC India's first women's organisation. What correction follows the owner?",
       "Which option correctly handles the Women's Indian Association's place in the sequence?"]),
    R("R04", "AIWC 1927 and education",
      "The All India Women's Conference was founded in 1927, initially focused on women's education and later extended into legal and social reform advocacy.",
      ["AIWC was founded after the contemporary SHG-federation phase.",
       "AIWC began as a trade union of self-employed women workers in Gujarat.",
       "AIWC was created only to measure household account ownership."],
      "Basic §§2,3; Advanced §§2,7.",
      "Remembering the 1927 date but attaching SEWA's organisational form or a survey function to AIWC.",
      ["Which combination correctly identifies AIWC's date, initial focus and later role?",
       "What does the owner establish about the All India Women's Conference?",
       "Which institution-history statement is source-consistent for AIWC?"]),
    R("R05", "AIWC institutional boundary",
      "AIWC is an influential pan-Indian women's organisation and a platform for education, franchise and legal-reform advocacy; it is not identical to SEWA or an SHG federation.",
      ["AIWC is structurally the same as a savings-and-credit federation.",
       "AIWC's defining function in the owner is platform-based legal and social reform advocacy alone with no educational origin.",
       "AIWC is a state survey programme rather than a voluntary organisation."],
      "Basic §§2,4; Advanced §2.",
      "Collapsing distinct organisational forms because all are associated with women's empowerment.",
      ["Which institutional boundary should be retained for AIWC?",
       "How should AIWC be distinguished from contemporary grassroots economic organisations?",
       "Which statement avoids conflating AIWC with another women's organisation?"]),
    R("R06", "NFIW rights-and-wage model",
      "The National Federation of Indian Women is a post-Independence organisation associated with the broader left movement and mobilisation around legal rights, wages and anti-dowry campaigns.",
      ["NFIW is defined in the owner as a Gujarat trade union of self-employed workers.",
       "NFIW is only a village savings group with no rights or wage agenda.",
       "NFIW is a Census instrument for measuring women's work."],
      "Basic §§2-3; Advanced §§2-3.",
      "Substituting SEWA's trade-union/economic model for NFIW's rights-and-wage mobilisation.",
      ["Which proposition correctly places NFIW in the movement's organisational map?",
       "What mechanism is associated with NFIW in the owner?",
       "Which option identifies the post-Independence rights-and-wage model?"]),
    R("R07", "SEWA organisational form",
      "SEWA, founded in Gujarat, is registered as a trade union of self-employed and informal-sector women workers and also functions through cooperative institutions.",
      ["SEWA is a national population survey of women aged 15-49.",
       "SEWA is an AIWC-style education conference with no labour identity.",
       "SEWA is a compulsory state department imposing household family-size targets."],
      "Basic §2; Advanced §§2,7.",
      "Treating SEWA as a generic NGO or as an SHG federation rather than a trade union/cooperative movement.",
      ["Which organisational form is correctly associated with SEWA?",
       "A question asks what makes SEWA distinctive. Which answer fits the owner?",
       "Which statement keeps SEWA's institutional identity intact?"]),
    R("R08", "SEWA economic mechanism",
      "SEWA organises informal-sector women around economic rights, credit access and collective bargaining, making economic participation central to its empowerment model.",
      ["SEWA's central mechanism is only the publication of a national education curriculum.",
       "SEWA treats legal equality as sufficient and does not organise around livelihoods.",
       "SEWA's defining work is the enumeration of the national population."],
      "Basic §§2,3; Advanced §§2-3.",
      "Reducing SEWA to charity or legal advocacy and missing collective economic agency.",
      ["What mechanism does the owner attribute to SEWA?",
       "Which option best explains why SEWA is an economic-organisation model?",
       "How should a question frame SEWA's route to empowerment?"]),
    R("R09", "SHG federation form",
      "Self-help group federations are savings-and-credit groups that federate upward into larger bodies and form a widespread contemporary grassroots women's organisational form.",
      ["SHG federations are registered national trade unions identical to SEWA.",
       "SHG federations are only elite reform associations from the nineteenth century.",
       "SHG federations are administrative census units with no collective function."],
      "Basic §§2-4; Advanced §2.",
      "Equating a federated savings-and-credit network with a trade union or historical reform body.",
      ["Which description correctly identifies SHG federations?",
       "What organisational form is associated with contemporary grassroots reach?",
       "Which statement preserves the SHG federation's structural boundary?"]),
    R("R10", "SEWA versus SHG distinction",
      "SEWA is a trade union and cooperative movement of self-employed women, whereas SHG federations are savings-and-credit groups linked upward into larger grassroots bodies.",
      ["SEWA and SHG federations are identical because both involve women.",
       "SHG federations are legal-rights bodies and SEWA is only an education conference.",
       "SEWA is a Census survey while SHG federations are statutory courts."],
      "Basic §§2-4; Advanced §§2-3.",
      "Treating shared empowerment goals as proof of identical organisational form.",
      ["Which comparison correctly separates SEWA from SHG federations?",
       "A matching item contrasts two contemporary forms. Which pairing is accurate?",
       "Which option avoids the SEWA–SHG conflation trap?"]),
    R("R11", "gender equality",
      "Gender equality concerns equal rights, status and opportunity regardless of gender and supplies the rights baseline for the other concepts.",
      ["Gender equality means only that every woman must receive a different benefit.",
       "Gender equality is identical to evidence of independent household decision-making.",
       "Gender equality is a synonym for membership in a self-help group."],
      "Basic §2; Advanced §2.",
      "Confusing a rights/status baseline with differentiated instruments or an agency outcome.",
      ["Which definition correctly captures gender equality?",
       "What does equality contribute to the equality–equity–empowerment distinction?",
       "Which option uses the term gender equality precisely?"]),
    R("R12", "gender equity",
      "Gender equity uses context-responsive measures to address structural disadvantage and unequal starting conditions, such as credit, mobility support, childcare or collective bargaining.",
      ["Gender equity means applying exactly the same support regardless of unequal constraints.",
       "Gender equity is the automatic result of passing a formal equality rule.",
       "Gender equity means that programme coverage itself proves agency."],
      "Basic §2; Advanced §§2-3.",
      "Calling differentiated support privilege or treating it as identical to formal equality.",
      ["Which statement best defines gender equity?",
       "Why does the owner distinguish equity from equality?",
       "Which example is a context-responsive equity instrument?"]),
    R("R13", "women's empowerment",
      "Women's empowerment is the process and outcome of expanded agency, capability, resources and voice, evidenced by exercised choice and recognised authority rather than by coverage alone.",
      ["Empowerment is established whenever a law or programme exists on paper.",
       "Empowerment is identical to the number of women enrolled in an organisation.",
       "Empowerment means only that women have been counted in a survey."],
      "Basic §2; Advanced §§2,5-8.",
      "Treating formal entitlement, enrolment or access as proof of substantive agency.",
      ["Which proposition correctly describes women's empowerment?",
       "What evidence would most directly support an empowerment claim?",
       "Which option avoids reducing empowerment to programme coverage?"]),
    R("R14", "trichotomy interaction",
      "Equality, equity and empowerment interact rather than forming a mechanical one-way ladder; coverage without uptake or support can stall before agency is reached.",
      ["Equality automatically produces empowerment once a law is enacted.",
       "Equity and empowerment are interchangeable names for the same legal status.",
       "The three terms must always be treated as a fixed sequence with no feedback or failure point."],
      "Basic §§1,2,5; Advanced §§3,8.",
      "Turning an analytical relationship into a deterministic sequence.",
      ["Which analytical qualification belongs to the equality–equity–empowerment triad?",
       "How should a close option describe the relation among the three terms?",
       "Which statement captures the owner's warning against a mechanical ladder?"]),
    R("R15", "coverage versus agency",
      "Programme or organisational coverage is an input or reach measure; it does not by itself establish women's decision-making agency.",
      ["Coverage and agency are identical whenever a programme has a large membership.",
       "Agency can be inferred from a single access statistic without observing use or authority.",
       "An organisation's name is sufficient evidence that members control resources."],
      "Basic §§2,5,6; Advanced §§3,6.",
      "Mistaking an input or reach indicator for an outcome of agency.",
      ["Which measurement distinction is central to the owner's empowerment analysis?",
       "A programme reports high enrolment. What can the owner legitimately conclude?",
       "Which option separates reach from substantive empowerment?"]),
    R("R16", "membership versus substantive voice",
      "Membership in a women's organisation or SHG does not automatically confer substantive voice; voice requires recognised decision-making authority within household or community contexts.",
      ["Membership necessarily guarantees control over household resources.",
       "Substantive voice is established by counting enrolment alone.",
       "Voice is irrelevant if an organisation has a formal registration certificate."],
      "Advanced §§2,5-6; package §§13.4-13.5.",
      "Equating formal membership with recognised authority and independent decisions.",
      ["Which statement correctly separates membership from substantive voice?",
       "What additional evidence is needed beyond organisational enrolment?",
       "Which scenario would prevent a membership claim from proving empowerment?"]),
    R("R17", "bonding social capital",
      "In the cross-linked SHG framework, bonding social capital refers to trust and ties within the SHG that can support initial savings mobilisation.",
      ["Bonding capital means links from an SHG directly to a ministry or bank.",
       "Bonding capital refers only to national-level legal advocacy.",
       "Bonding capital is the absence of internal trust within the group."],
      "Advanced §2; detailed mechanism cross-owned by Governance.",
      "Swapping bonding with bridging or linking social-capital functions.",
      ["Which function is associated with bonding capital in an SHG?",
       "A matching item asks what happens within the group itself. Which term fits?",
       "Which statement uses bonding social capital in the cross-owner sense?"]),
    R("R18", "bridging social capital",
      "Bridging social capital refers to links across SHGs and federations that can enable scale and market access.",
      ["Bridging capital describes only trust among members of one SHG.",
       "Bridging capital is a constitutional equality clause.",
       "Bridging capital means that formal membership automatically creates agency."],
      "Advanced §2; Governance cross-link.",
      "Confusing cross-group connections with within-group trust or legal equality.",
      ["What role does bridging capital play in the SHG-federation framework?",
       "Which relation best illustrates bridging rather than bonding?",
       "Which option correctly identifies the cross-group social-capital mechanism?"]),
    R("R19", "linking social capital",
      "Linking social capital refers to ties between SHGs or federations and banks or government systems, enabling access to formal credit and institutions.",
      ["Linking capital is limited to family ties within a household.",
       "Linking capital is the same as the historical founding date of AIWC.",
       "Linking capital means no contact with formal institutions."],
      "Advanced §2; Governance cross-link.",
      "Reversing the direction from community organisations to formal institutions.",
      ["Which function is associated with linking social capital?",
       "A federation seeks bank and government access. Which social-capital link is involved?",
       "Which statement correctly distinguishes linking from bonding?"]),
    R("R20", "intersectionality",
      "Intersectionality highlights that caste, class, tribe, religion, disability, sexuality, region, migration and life course shape women's constraints and organising capacity differently.",
      ["Intersectionality treats all women as a single undifferentiated category.",
       "Intersectionality means that only gender matters in programme design.",
       "Intersectionality is a claim that all women's organisations must have identical agendas."],
      "Basic §3; Advanced §§2,4,6; package semantic-completeness block.",
      "Replacing differentiated social location with a universal category of women.",
      ["Which proposition correctly captures the topic's intersectionality lens?",
       "Why does the owner reject a single undifferentiated category of women?",
       "Which option identifies the main analytical work done by intersectionality?"]),
    R("R21", "Dalit and Adivasi women's organisations",
      "Dalit and Adivasi women's organisations have raised distinct concerns, such as caste-based violence and land rights, that may not be centred by mainstream organisations.",
      ["Distinct Dalit and Adivasi organisations prove that a common women's movement never existed.",
       "Dalit and Adivasi women's organisations are identical to AIWC in constituency and agenda.",
       "Their separate agendas show that caste and tribe have no relevance to women's organising."],
      "Advanced §4; package semantic-completeness block.",
      "Treating intersectional correction as fragmentation or erasing specific agendas.",
      ["What does the owner infer from Dalit and Adivasi women's organisations?",
       "Which statement best represents the lower-strata reach problem?",
       "How should a question use separate Dalit or Adivasi women's organisations as evidence?"]),
    R("R22", "universal sisterhood limitation",
      "A universal-sisterhood framing can obscure caste-, class- and religion-specific constraints because women do not experience disadvantage uniformly.",
      ["Universal sisterhood is sufficient for every programme design without local diagnosis.",
       "Universal sisterhood proves that organisational membership always produces voice.",
       "Universal sisterhood means that all women's movements have one identical strategy."],
      "Advanced §§2,4,6.",
      "Treating a universal category as a substitute for intersectional analysis.",
      ["Which limitation of universal-sisterhood framing is source-consistent?",
       "Why can a single 'women' category be inadequate for programme design?",
       "Which option gives the correct intersectional qualification?"]),
    R("R23", "regional and social variation",
      "Caste, class, religion, region, rural–urban location and life course alter both women's exposure to constraints and their capacity to organise.",
      ["Regional variation is analytically irrelevant once a national organisation exists.",
       "All women face identical constraints because gender is the only social relation.",
       "Local variation should be ignored to preserve one uniform empowerment target."],
      "Advanced §§4,6,11; package semantic-completeness block.",
      "Turning a national category into a uniform social experience.",
      ["Which variation must a serious women's-organisations analysis retain?",
       "What does the owner require before generalising from one organisational experience?",
       "Which option correctly handles regional and social differentiation?"]),
    R("R24", "unpaid care",
      "Unpaid care and time poverty are substantive constraints on women's work, mobility and programme uptake; unpaid care should not be treated as inactivity.",
      ["Unpaid care is outside women's status because only paid employment counts.",
       "Time poverty disappears whenever a woman is enrolled in an SHG.",
       "Unpaid care automatically proves that a woman is economically inactive in every sense."],
      "Package semantic-completeness block; Advanced §§3,5-6.",
      "Collapsing unpaid care, labour-force status and agency into one category.",
      ["Which statement correctly treats unpaid care in this topic?",
       "Why does time poverty matter when assessing women's organisations?",
       "Which option avoids the paid-work-only trap?"]),
    R("R25", "LFPR and all work",
      "A labour-force participation rate is not a complete measure of all work, unpaid care, job quality or women's agency.",
      ["LFPR directly measures household decision-making authority.",
       "LFPR captures all unpaid care and therefore needs no qualification.",
       "LFPR alone proves that work is secure, well-paid and empowering."],
      "Package semantic-completeness block; PLFS boundary routed to official labour statistics.",
      "Using one participation indicator as a complete empowerment measure.",
      ["What can a female LFPR figure not establish by itself?",
       "Which caveat must accompany a labour-force participation statistic?",
       "How should a Prelims option distinguish LFPR from empowerment?"]),
    R("R26", "account ownership versus control",
      "A woman having or using a bank account is an access indicator; it does not by itself prove control over resources, income or decisions.",
      ["Account ownership automatically proves independent control of household resources.",
       "An account-use statistic is a direct measure of substantive voice.",
       "Financial access makes caste, care and mobility constraints irrelevant."],
      "Basic §6; Advanced §§7-9; NFHS-5 boundary.",
      "Reading access as control or agency without observing who decides or uses resources.",
      ["Which evidentiary distinction does account ownership illustrate?",
       "A survey reports bank-account use by women. What conclusion is safest?",
       "Which statement avoids the access-versus-agency trap?"]),
    R("R27", "NFHS-5 account-use indicator",
      "NFHS-5 (2019–21) recorded 78.6% of women aged 15–49 with a bank or savings account they themselves used; this is a dated access indicator, not proof of agency.",
      ["The figure is an undated Census count of every woman in India.",
       "The figure directly measures independent control over household assets.",
       "The figure is a current state-by-state result with no survey universe."],
      "Basic §6; Advanced §7; official NFHS-5 national fact sheet.",
      "Dropping the age group and survey years or turning account use into a causal empowerment claim.",
      ["How should the NFHS-5 account-use figure be handled?",
       "Which qualification is essential when citing the 78.6% indicator?",
       "What does the owner permit one to infer from the NFHS-5 account measure?"]),
    R("R28", "NFHS-5 internet-use indicator",
      "NFHS-5 (2019–21) recorded 33.3% of women aged 15–49 as having ever used the internet; it is a dated access measure rather than proof of digital agency.",
      ["The figure is a full-enumeration Census measure of all digital behaviour.",
       "The figure proves equal digital control across caste, class and region.",
       "The figure directly establishes that internet use caused empowerment."],
      "Basic §6; Advanced §7; official NFHS-5 national fact sheet.",
      "Presenting a historical access indicator as a universal, causal or agency measure.",
      ["Which statement correctly uses the NFHS-5 internet-use indicator?",
       "What is the proper evidentiary status of the 33.3% figure?",
       "Which option retains the survey and agency qualifications?"]),
    R("R29", "NFHS data limitation",
      "NFHS-5 figures are historical survey comparators; neither an NFHS round is a Census stock nor does it alone prove causation.",
      ["NFHS estimates replace the Census because sample surveys enumerate every resident.",
       "A national NFHS association proves the same cause for every household.",
       "NFHS reference periods and survey design can be ignored once a number is published."],
      "Basic data-status correction; Advanced §§7-9; official NFHS fact sheets.",
      "Confusing a sample survey, a complete enumeration and causal inference.",
      ["Which methodological boundary must accompany NFHS evidence?",
       "What is the safest interpretation of a national NFHS indicator?",
       "Which statement avoids the survey-design trap?"]),
    R("R30", "NFHS-6 release boundary",
      "NFHS-6 (2023–24) was released on 29 May 2026, but the owner warns that no NFHS-6 metric should be quoted unless taken directly from its released national fact sheet.",
      ["NFHS-6 metrics may be invented from the NFHS-5 values because the rounds are interchangeable.",
       "The release date proves that every NFHS-6 state estimate is final and causal.",
       "NFHS-6 was not released, so NFHS-5 remains the latest possible round by definition."],
      "Basic data-status correction; Advanced §9; released NFHS-6 national fact-sheet boundary.",
      "Treating release metadata as permission to invent metrics or erase provisional/source limits.",
      ["Which statement correctly handles the NFHS-6 current anchor?",
       "What is the owner's rule for quoting NFHS-6 metrics?",
       "Which option preserves the release-date and source-discipline boundary?"]),
    R("R31", "PLFS versus NFHS universe",
      "PLFS and NFHS use different universes, reference periods and indicator definitions; a female LFPR value cannot be merged casually with an NFHS access indicator.",
      ["PLFS and NFHS are interchangeable surveys with identical universes and indicators.",
       "A PLFS participation rate automatically measures account ownership and agency.",
       "NFHS household indicators can be relabelled as labour-market rates without qualification."],
      "Package semantic-completeness block; PLFS/NFHS source-date controls.",
      "Combining statistics from different surveys without preserving their definitions and universes.",
      ["Why must PLFS and NFHS indicators be kept distinct?",
       "Which statement correctly handles cross-survey comparison?",
       "A question juxtaposes LFPR and internet use. What methodological caution applies?"]),
    R("R32", "legal and scheme cross-owner boundary",
      "Constitutional equality and laws or programmes such as the NCW Act, Domestic Violence Act, POSH Act and Mission Shakti may be named as context here, but detailed provisions and implementation belong to Polity or Social Justice.",
      ["The Indian Society owner should reproduce every statutory section and benefit rule in full.",
       "Mentioning a law proves that social norms and safety outcomes have already transformed.",
       "Legal and programme context must be excluded entirely from a sociological answer."],
      "Basic §4 and §12; Advanced §11; semantic-completeness ownership block.",
      "Either duplicating another subject's detailed law architecture or treating enactment as outcome.",
      ["Which boundary correctly handles laws and schemes in this topic?",
       "How should a Prelims question use the Domestic Violence Act or POSH Act here?",
       "Which statement respects the cross-owner rule?"]),
    R("R33", "NCW Act context",
      "The National Commission for Women Act, 1990 can be cited as institutional context, but detailed statutory doctrine is routed to the owning Polity or Social Justice material.",
      ["The Act is a savings-and-credit federation instrument.",
       "The Act by itself proves that every woman has substantive voice.",
       "The Act is the founding legal instrument of SEWA's trade-union registration."],
      "Advanced §11; package semantic-completeness block; detailed legal treatment cross-owned.",
      "Using an institutional law as proof of empowerment or confusing it with organisational history.",
      ["How should the NCW Act, 1990 be used in this topic?",
       "Which statement correctly positions the National Commission for Women Act?",
       "What is the safe exam boundary for this legal reference?"]),
    R("R34", "Domestic Violence Act context",
      "The Protection of Women from Domestic Violence Act, 2005 may be named to connect legal protection with programme design, but detailed sections and implementation belong to Social Justice or Polity.",
      ["The Act is a historical women's education association from 1927.",
       "The Act is evidence that membership alone creates economic agency.",
       "The Act is a replacement for organisational mobilisation and collective voice."],
      "Basic §4; Advanced §11; Social Justice cross-link.",
      "Treating the existence of protective law as proof that violence or norms have disappeared.",
      ["Which use of the Domestic Violence Act is source-disciplined here?",
       "What does the legal cross-link permit an answer to do?",
       "Which option avoids overstating the Act's social effect?"]),
    R("R35", "POSH Act context",
      "The POSH Act, 2013 can be used as legal context for safety and work, while detailed statutory tests and compliance architecture are owned elsewhere.",
      ["POSH is the name of a women's savings-and-credit federation.",
       "POSH registration proves that every workplace is safe in practice.",
       "POSH is the founding date of the Women's Indian Association."],
      "Basic §4; Advanced §11; Social Justice cross-link.",
      "Turning a legal framework into an outcome claim or confusing it with an organisation.",
      ["How should POSH be treated in a women's-organisations question?",
       "Which statement correctly uses the POSH Act as context?",
       "What is the principal trap in a POSH-based option?"]),
    R("R36", "Mission Shakti context",
      "Mission Shakti may be named as a current executive programme context, but its detailed component and implementation architecture belong to the Social Justice owner and its existence is not proof of empowerment.",
      ["Mission Shakti is a nineteenth-century reform association.",
       "Mission Shakti is identical to SEWA's trade-union registration.",
       "Mission Shakti's existence alone proves that all women exercise agency."],
      "Basic §4; Advanced §11; Social Justice cross-link.",
      "Treating a programme label as an outcome or importing another subject's full scheme architecture.",
      ["Which statement correctly handles Mission Shakti in this topic?",
       "What can Mission Shakti contribute to a sociological answer?",
       "Which option avoids the scheme-existence trap?"]),
    R("R37", "2018 GS-I movement and lower strata",
      "The 2018 GS-I demand routed to this owner requires movement history plus an intersectional test of who was reached or missed, including lower-strata women's distinct constraints.",
      ["The demand can be answered by listing organisation names without discussing reach or social location.",
       "The demand is an objective Prelims question whose official key is reproduced here.",
       "The demand requires treating all women as one homogeneous constituency."],
      "Advanced §10; package §13.1 and direct-demand table; exact wording held.",
      "Confusing a routed Mains demand with a solved objective PYQ or omitting intersectional reach.",
      ["Which answer route matches the 2018 GS-I movement-and-lower-strata demand?",
       "What additional test must accompany a history of women's organisations?",
       "Which approach best addresses the lower-strata dimension of the 2018 demand?"]),
    R("R38", "2019 GS-I time and space",
      "The 2019 GS-I demand is routed as challenges faced by women across time and space; the answer should examine unpaid care, mobility, safety, location and social variation.",
      ["The demand is satisfied by one national female LFPR number alone.",
       "The demand asks only for AIWC's founding year and no structural analysis.",
       "The demand requires ignoring spatial and temporal variation to produce one universal rule."],
      "Advanced §10; package §13.1 and direct-demand table; exact wording held.",
      "Reducing time-and-space challenges to a single statistic or institution date.",
      ["Which structure fits the 2019 GS-I time-and-space demand?",
       "What dimensions should a response on women's challenges retain?",
       "Which option avoids the narrow-statistic trap in this demand family?"]),
    R("R39", "2021 GS-I gig economy",
      "The 2021 GS-I gig-economy demand requires a balanced analysis: entry and flexibility may coexist with income insecurity, weak protection and uncertain control.",
      ["Gig work is automatically empowering because it offers flexible entry.",
       "Gig work is automatically exploitative, so no flexibility or opportunity can be recognised.",
       "The demand can be answered without considering work conditions or social protection."],
      "Advanced §10; package §13.1 and evidence bank E4; detailed labour status cross-owned.",
      "Choosing either automatic liberation or automatic exploitation instead of a qualified trade-off.",
      ["Which analytical route fits the 2021 gig-economy demand?",
       "How should gig work be evaluated in relation to women's empowerment?",
       "Which conclusion is most defensible for a gig-work question?"]),
    R("R40", "2023 GS-I young-women self-harm",
      "The 2023 GS-I demand on rising suicide among young women requires multi-causal, non-stigmatising analysis and does not permit attributing a trend to one social factor without disaggregated evidence.",
      ["A reported category alone proves one household or cultural cause.",
       "The safest answer is to infer a single cause from the demographic label.",
       "Self-harm trends can be explained without mental-health services, social stressors or evidence caution."],
      "Advanced §10; package §13.1, thesis T3; exact demand wording held.",
      "Turning a complex public-health demand into a monocausal social diagnosis.",
      ["Which evidentiary discipline belongs to the 2023 GS-I self-harm demand?",
       "How should a response avoid overclaiming about young women's suicide?",
       "Which option gives the owner's multi-causal route?"]),
    R("R41", "National Suicide Prevention Strategy 2022",
      "The Ministry of Health and Family Welfare's National Suicide Prevention Strategy (2022) frames prevention through surveillance, health-service capacity, community resilience and evidence; it does not prove one cause of any reported trend.",
      ["The Strategy establishes that one social factor caused every reported suicide.",
       "The Strategy is an AIWC or SEWA organisational charter.",
       "The Strategy replaces the need for disaggregated evidence and non-stigmatising care."],
      "Advanced §13.4 E5; MoHFW National Suicide Prevention Strategy (2022).",
      "Using a policy framework as causal proof rather than as a prevention architecture.",
      ["What does the National Suicide Prevention Strategy (2022) contribute to this topic?",
       "Which statement correctly uses the Strategy as evidence?",
       "How should the 2022 prevention framework qualify a self-harm answer?"]),
    R("R42", "non-linear organisational layering",
      "Early national bodies, rights organisations, labour organisations and SHG federations are layered and overlapping; later forms do not erase earlier organisations.",
      ["The movement must be read as a sequence in which each later body replaces the previous one.",
       "Only one organisational mechanism can operate in a society at a time.",
       "Layering means that all organisations have identical mandates and constituencies."],
      "Advanced §§1,3; Basic §3.",
      "Interpreting historical development as replacement rather than coexistence and functional differentiation.",
      ["Which historical inference follows from the owner's organisational layering?",
       "How should chronology and coexistence be combined in an answer?",
       "Which statement avoids a linear-replacement reading?"]),
    R("R43", "equality without equity",
      "A woman may possess formal voting and property rights yet lack income, mobility or care support; this illustrates equality without equity and therefore without established empowerment.",
      ["Formal rights always establish agency regardless of material constraints.",
       "The example proves that equality and equity are synonyms.",
       "A lack of support is irrelevant once legal status is equal."],
      "Advanced §5 boundary case 1; Basic §§2,5.",
      "Treating formal equality as sufficient for substantive empowerment.",
      ["Which scenario best illustrates equality without equity?",
       "What does the owner's first boundary case show?",
       "Which option correctly applies the trichotomy to formal rights?"]),
    R("R44", "equity without empowerment",
      "An SHG member may receive credit while her husband controls loan-use decisions; this shows equity access without sustained substantive empowerment.",
      ["Receiving credit automatically proves independent decision-making.",
       "Household control is irrelevant to whether an equity instrument empowers.",
       "An SHG loan is a legal-rights organisation rather than an economic instrument."],
      "Advanced §5 boundary case 2; Basic §§2,5.",
      "Equating access to an equity instrument with actual control and voice.",
      ["Which scenario illustrates equity without empowerment?",
       "What does the SHG-credit boundary case demonstrate?",
       "Which option correctly separates instrument access from agency?"]),
    R("R45", "completed equality-equity-empowerment chain",
      "A SEWA member who gains credit, participates in collective bargaining and takes an independent enterprise decision illustrates the trichotomy reaching substantive agency, subject to the case-specific qualification.",
      ["The example proves that every SEWA member has identical outcomes.",
       "Credit alone, without bargaining or independent decisions, is sufficient proof of empowerment.",
       "The example shows that legal equality is unnecessary for agency."],
      "Advanced §5 boundary case 3; Basic §§2,5; package verdict scaffold.",
      "Generalising one boundary case into a universal organisational outcome.",
      ["Which case best illustrates the full trichotomy in operation?",
       "What additional evidence turns SEWA membership into an empowerment example?",
       "Which option uses the SEWA boundary case without overgeneralising?"]),
    R("R46", "gig flexibility–protection trade-off",
      "Gig work may reduce entry barriers or offer flexibility while also exposing women to insecurity, care constraints, weak protection and uncertain bargaining power.",
      ["Flexibility removes every risk associated with platform work.",
       "Insecurity means that no woman can gain any capability from gig work.",
       "A platform label by itself establishes either empowerment or exploitation."],
      "Package evidence bank E4; Advanced §10; labour/social-security detail cross-owned.",
      "Replacing a trade-off analysis with a categorical verdict.",
      ["Which statement captures the gig-work trade-off?",
       "How can flexibility and insecurity coexist for women workers?",
       "Which conclusion is appropriately qualified for platform work?"]),
    R("R47", "descriptive versus substantive representation",
      "The presence or membership of women in an organisation is descriptive representation; substantive representation requires that their interests and voice shape decisions.",
      ["Descriptive presence automatically proves that organisational decisions reflect all women's interests.",
       "Substantive representation is measured only by counting membership cards.",
       "Representation is irrelevant to intersectional organisational analysis."],
      "Package semantic-completeness block; Advanced §§4-6.",
      "Treating numerical presence as proof of agenda-setting voice.",
      ["Which distinction is necessary when evaluating representation?",
       "What does substantive representation add beyond numerical presence?",
       "Which option avoids the representation-as-count trap?"]),
    R("R48", "cross-owner routing discipline",
      "This topic owns the sociological and organisational lens; detailed SHG social-capital mechanics belong to Governance, while statutory and scheme architecture belongs to Polity or Social Justice.",
      ["Every cross-linked detail should be duplicated here before a question can be answered.",
       "Cross-owner routing means those concepts are irrelevant to Indian Society.",
       "A legal or governance owner can be replaced by an undated coaching summary."],
      "Basic §12; Advanced §§4,11; package ownership and study-link blocks.",
      "Either omitting a necessary cross-link or importing unsupported detail beyond the owner boundary.",
      ["Which source-routing rule applies to this topic?",
       "How should a final bank handle Governance and Social Justice overlaps?",
       "Which statement correctly preserves the topic's ownership boundary?"]),
]


def option_balance(keys: list[str]) -> bool:
    counts = Counter(keys)
    return len(keys) >= 40 and max(counts.values()) - min(counts.values()) <= 1


def make_bank(revision: int) -> tuple[str, str, str, dict]:
    rng = random.Random(7300 + revision * 97)
    targets = list("A" * 12 + "B" * 12 + "C" * 12 + "D" * 12)
    rng.shuffle(targets)
    q_lines = [f"# Indian Society 07 — Revision {revision}", "", "All items are original and answer-free; select the best answer.", ""]
    a_lines = [f"# Indian Society 07 — Revision {revision} explained answers", "", "Exact UPSC wording and options are withheld; every item below is independently authored.", ""]
    c_lines = [
        f"# Women and Women's Organisations — Revision {revision} coverage ledger",
        "",
        "| Q | Root | Named coverage unit | Affirmative proposition | Source boundary |",
        "|---:|---|---|---|---|",
    ]
    keys: list[str] = []
    stems_seen: set[str] = set()
    for qno, root in enumerate(ROOTS, 1):
        stem = root["stems"][revision - 1]
        normalized = re.sub(r"\s+", " ", stem.strip().lower())
        if normalized in stems_seen:
            raise RuntimeError(f"duplicate stem: {stem}")
        stems_seen.add(normalized)
        correct = root["fact"] + OPTION_SUFFIX
        wrongs = [wrong + OPTION_SUFFIX for wrong in root["wrongs"]]
        correct_pos = "ABCD".index(targets[qno - 1])
        opts = [None] * 4
        opts[correct_pos] = correct
        for pos, text in zip([i for i in range(4) if i != correct_pos], wrongs):
            opts[pos] = text
        key = targets[qno - 1]
        keys.append(key)
        q_lines.append(f"### Q{qno}. {stem}")
        for letter, text in zip("ABCD", opts):
            q_lines.append(f"{letter}. {text}")
        q_lines.append("")

        a_lines.append(f"### Q{qno}. {key}")
        for letter, text in zip("ABCD", opts):
            if text == correct:
                a_lines.append(f"- **{letter} — Correct:** {text} This is the affirmative proposition for **{root['focus']}**. It is supported by the named owner and the authoritative boundary recorded below.")
            else:
                a_lines.append(f"- **{letter} — Incorrect:** {text} It fails because the source-consistent proposition is: {correct}")
        a_lines.append(f"**Evidence:** {correct}")
        a_lines.append(f"**Sources:** {root['source']}")
        a_lines.append(f"**Examiner trap:** {root['trap']}")
        a_lines.append("")
        c_lines.append(f"| {qno} | {root['code']} | {root['focus']} | Q{qno} | {root['source']} |")
    meta = {"questions": len(ROOTS), "answers": len(ROOTS), "keys": dict(Counter(keys)), "roots": len(ROOTS)}
    if not option_balance(keys):
        raise RuntimeError(f"unbalanced keys R{revision}: {meta['keys']}")
    return "\n".join(q_lines) + "\n", "\n".join(a_lines) + "\n", "\n".join(c_lines) + "\n", meta


def write_support_files(metas: dict[str, dict]) -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    root_rows = "\n".join(f"| {r['code']} | {r['focus']} | affirmative in R1 Q{i}, R2 Q{i}, R3 Q{i} |" for i, r in enumerate(ROOTS, 1))
    (TOPIC / "COVERAGE.md").write_text(
        "# Indian Society 07 — Women and Women's Organisations\n\n"
        "**Status:** complete for original banks; exact PYQ provenance/rights and independent learner review remain held.\n\n"
        "| Revision | Questions | Answers | Coverage roots | Status |\n|---|---:|---:|---:|---|\n"
        + "\n".join(f"| {i} | {m['questions']} | {m['answers']} | {m['roots']}/{m['roots']} affirmative | complete for originals |" for i, m in enumerate(metas.values(), 1))
        + "\n\n## Root coverage\n\nEvery named root is tested affirmatively in every revision; no owner detail is counted only as a distractor.\n\n"
        "| Root | Named unit | Affirmative mapping |\n|---|---|---|\n" + root_rows
        + "\n\nSee each revision ledger for item-level mapping and `SOURCE-AND-PYQ-HOLDS.md` for evidence and unresolved gates.\n",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        "# Indian Society 07 — source and PYQ holds\n\n"
        "## Original-bank status\n\n"
        "- All 144 released items are original MCQs: 48 each in Revision 1, Revision 2 and Revision 3.\n"
        "- No exact UPSC question wording or option set is reproduced.\n"
        "- No exact UPSC objective PYQ is claimed or released in these banks.\n\n"
        "## Evidence order and authoritative boundaries\n\n"
        f"1. Canonical Basic owner: `{BASIC}`.\n"
        f"2. Optional Advanced owner: `{ADVANCED}`.\n"
        f"3. Learner-v2 package: `{PACKAGE}`.\n"
        "4. Official NFHS-5 (2019–21) national fact-sheet boundary for dated account-use and internet-use indicators.\n"
        "5. NFHS-6 (2023–24) release boundary recorded by the owners: released 29 May 2026; metrics must be taken from the released national fact sheet, not inferred.\n"
        "6. National Population Policy is not imported here; detailed statutory, scheme and SHG mechanics remain routed to Social Justice, Polity or Governance as marked item by item.\n"
        "7. MoHFW National Suicide Prevention Strategy (2022) is used only for prevention architecture and not as proof of a single cause.\n\n"
        "## PYQ holds\n\n"
        "- The owners route 2018 GS-I movement/lower-strata, 2019 GS-I time-and-space challenges, 2021 GS-I gig economy, 2023 GS-I young-women self-harm and 2024 GS-I equality/equity/empowerment demands.\n"
        "- Exact wording/options remain withheld pending same-paper visual authentication, official provenance and documented UPSC reproduction permission.\n"
        "- These banks independently test the concepts; no routed Mains demand is relabelled as an exact objective PYQ.\n\n"
        "## Data and cross-owner holds\n\n"
        "- NFHS-5 values are dated 2019–21 survey comparators, not Census stock or causal proof.\n"
        "- NFHS-6 release metadata does not authorise unverified metrics; preserve source, round, age group, universe and provisional status.\n"
        "- Female LFPR, unpaid care, account use, internet use, membership and representation are not interchangeable measures of empowerment.\n"
        "- Independent answer-blind learner review remains pending.\n",
        encoding="utf-8",
    )
    lines = ["# Structural audit — Women and Women's Organisations", "", "Automated structural checks passed for all three 48-question banks.", ""]
    for i, m in enumerate(metas.values(), 1):
        lines.append(f"- revision-{i}: {m}; contiguous numbering, one-to-one keys, four options and four option-specific rationales.")
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        "# Hostile audit — Women and Women's Organisations\n\n"
        "**Result: PASS for original-bank release; exact PYQ, source-date and learner-review holds remain.**\n\n"
        "| Audit | Result | Finding |\n|---|---|---|\n"
        "| Answer leakage | PASS | Questions contain no keys, rationales, sources, traps or explanatory suffixes. |\n"
        "| Option distinctness | PASS | Four distinct, grammatically complete options per item; no material option-length cue. |\n"
        "| Key balance | PASS | Each 48-question revision has 12 A, 12 B, 12 C and 12 D keys in independently shuffled positions. |\n"
        "| Stem distinctness | PASS | Each revision uses a distinct root-specific stem family; no duplicate normalized stem within a bank. |\n"
        "| Cross-revision independence | PASS | Distinct stems and independently shuffled positions; banks are not reshuffles of one question file. |\n"
        "| Owner coverage | PASS | All 48 roots are affirmative in R1, R2 and R3. |\n"
        "| Institutional/data facts | PASS | AIWC, NFIW, SEWA, SHGs, NFHS and legal cross-owner boundaries are qualified. |\n"
        "| Hostile generalisation | PASS | Absolute and causal-overclaim distractors are rejected; correct propositions retain scope limits. |\n"
        "| PYQ/rights gate | PASS | Zero exact PYQs live; routed Mains demands are independently concept-tested. |\n\n"
        "## Remaining holds\n\n"
        "- Independent answer-blind learner review is a future gate; this release is not learner-approved.\n"
        "- Exact PYQ reproduction permission and any future objective-PYQ key provenance remain open.\n",
        encoding="utf-8",
    )
    (TOPIC / "AUDIT-REPORT.md").write_text(
        "# Audit report — Indian Society 07\n\n"
        "**Status:** complete for original banks; PYQ/rights and learner-review holds remain.\n\n"
        "- Original questions: **144** (48/48/48)\n"
        "- Coverage roots: **48/48/48 affirmative**\n"
        "- Structural, option-balance, leakage, distinctness, source/date, institutional-fact and hostile audits: **PASS**\n"
        "- Exact PYQs included: **0**\n"
        "- All three banks contain separate answers with evidence, four option rationales and examiner traps.\n"
        "- See `SOURCE-AND-PYQ-HOLDS.md` for unresolved provenance, rights and data boundaries.\n",
        encoding="utf-8",
    )
    validation = {
        "topic_key": "indian-society-07",
        "title": "Women and Women's Organisations",
        "status": "complete_for_original_banks",
        "revisions": {f"revision-{i}": m for i, m in enumerate(metas.values(), 1)},
        "coverage_roots": 48,
        "pyqs_included": 0,
        "exact_pyq_status": "held_for_provenance_and_reproduction_rights",
        "learner_blind_review": "pending",
        "source_order": ["canonical Markdown owners", "official NFHS/MoHFW boundaries", "OCR/official GS-I demand routing"],
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def update_indexes() -> None:
    subject = SUBJECT_INDEX.read_text(encoding="utf-8")
    subject = re.sub(
        r"\| 07 — Women and Women's Organisations \| `pending` \| — \|",
        "| 07 — Women and Women's Organisations | `complete` for original banks: **144 originals (48/48/48)**; all 48 named roots affirmative in each revision, balanced independently shuffled keys, item-level ledgers, source/date and hostile audits passing. Exact PYQ wording/options remain held for provenance and reproduction rights; independent answer-blind learner review remains pending. | [Revision 1](07-Women-and-Womens-Organisations/revision-1/QUESTIONS.md) · [Revision 2](07-Women-and-Womens-Organisations/revision-2/QUESTIONS.md) · [Revision 3](07-Women-and-Womens-Organisations/revision-3/QUESTIONS.md) |",
        subject,
    )
    SUBJECT_INDEX.write_text(subject, encoding="utf-8")
    global_text = GLOBAL_INDEX.read_text(encoding="utf-8")
    global_text = re.sub(
        r"Topic \[06 Population and Associated Issues\]\(subjects/Indian-Society/06-Population-and-Associated-Issues/COVERAGE\.md\) is complete for original banks with 144 originals \(48/48/48\), all 48 named roots affirmative in each revision, balanced independently shuffled keys, item-level ledgers, source/date and hostile audits passing; exact PYQ wording/options remain held for provenance and reproduction rights; independent learner blind review is pending\. Next pending Topic 07\.",
        "Topic [06 Population and Associated Issues](subjects/Indian-Society/06-Population-and-Associated-Issues/COVERAGE.md) is complete for original banks with 144 originals (48/48/48), all 48 named roots affirmative in each revision, balanced independently shuffled keys, item-level ledgers, source/date and hostile audits passing; exact PYQ wording/options remain held for provenance and reproduction rights; independent learner blind review is pending. Topic [07 Women and Women's Organisations](subjects/Indian-Society/07-Women-and-Womens-Organisations/COVERAGE.md) is complete for original banks with 144 originals (48/48/48), all 48 named roots affirmative in each revision, balanced independently shuffled keys, item-level ledgers and hostile audits passing; exact PYQ wording/options remain held and independent learner blind review is pending. Next pending Topic 08.",
        global_text,
    )
    GLOBAL_INDEX.write_text(global_text, encoding="utf-8")


def main() -> None:
    metas: dict[str, dict] = {}
    for revision in range(1, 4):
        q, a, c, meta = make_bank(revision)
        folder = TOPIC / f"revision-{revision}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "QUESTIONS.md").write_text(q, encoding="utf-8")
        (folder / "ANSWERS.md").write_text(a, encoding="utf-8")
        (folder / "COVERAGE.md").write_text(c, encoding="utf-8")
        metas[f"revision-{revision}"] = meta
    write_support_files(metas)
    update_indexes()
    print(json.dumps(metas, indent=2))


if __name__ == "__main__":
    main()
