"""Authored learner-v2 data for Disaster Management Topic 03."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.indiacode.nic.in/handle/123456789/2155/?locale=en "
        "— attempted 2026-09-04; India Code returned HTTP 403 to the fetcher. "
        "Official search metadata confirmed section 8 of the Rights of Persons "
        "with Disabilities Act, 2016 as the protection-and-safety provision; "
        "no delivery outcome was inferred."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2082745 — attempted "
        "2026-09-04; the official PIB page returned HTTP 403. Search metadata "
        "confirmed the expanded Aapda Mitra scale reported by Government, but "
        "the authored module treats volunteer counts as inputs, not readiness "
        "or disaster outcomes."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2069426 — attempted "
        "2026-09-04; the official PIB page returned HTTP 403. Search metadata "
        "confirmed that Yuva Aapda Mitra is a distinct youth programme; it is "
        "not merged with the earlier pilot or expanded Aapda Mitra scheme."
    ),
    (
        "https://ndma.gov.in/Resources/Guidelines — searched 2026-09-04; the "
        "official guidelines area was thin in search retrieval. Guideline names "
        "and dates are retained only where already audited in the canonical "
        "owner, with no claim that publication proves accessible implementation."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("CBDRR", "Community-based disaster risk reduction is participatory risk assessment, planning and action with affected communities, not transfer of the State's duty to untrained residents."),
        ("Local knowledge", "Local knowledge can identify routes, seasonal patterns, social networks and hidden vulnerabilities, but it should be combined with scientific and administrative information."),
        ("Community first response", "Communities often act before external services arrive; effectiveness depends on assigned roles, training, equipment, safety and coordination."),
        ("Panchayats and ULBs", "Panchayats and urban local bodies connect household-level risk information, local plans, shelters, volunteers, services and grievance redress to the DDMA."),
        ("Community institutions", "Self-help groups, community-based organisations, youth groups, civil society and local leaders can support warning relay, evacuation, relief verification and recovery."),
        ("Volunteer boundary", "A trained volunteer programme is a capacity input; headcount alone does not prove retention, equipment, activation, safe practice or last-mile reach."),
        ("Social vulnerability", "Poverty, gender, age, disability, health, livelihood, housing, documentation and displacement can produce differentiated impacts from the same hazard."),
        ("Intersectionality", "Risk can compound when vulnerabilities intersect, so a single label such as vulnerable sections is analytically insufficient."),
        ("Gender-responsive protection", "Gender-responsive DRR requires participation in planning and attention to privacy, sanitation, safety, health, livelihoods, unpaid care and protection from violence."),
        ("Children", "Children need age-appropriate warnings, family tracing, safe learning continuity, nutrition, health care and protection from separation, abuse and trafficking."),
        ("Older persons", "Older persons may require medication continuity, mobility assistance, accessible transport, caregiver support and inclusion in household and shelter registers."),
        ("Persons with disabilities", "Disability-inclusive DRR requires accessible information, assisted evacuation, barrier-free shelters, continuity of support and participation in decisions."),
        ("Migrants and displaced persons", "Migrants and displaced people may face language, documentation, rental, livelihood and exclusion barriers; disaster displacement does not automatically create 1951 Refugee Convention status."),
        ("Accessible warnings", "Warnings should be understandable, multilingual and available through visual, audio, text and trusted-person channels, with feedback from at-risk users."),
        ("Inclusive evacuation", "Evacuation plans need mapped assistance, accessible vehicles and routes, accountable buddy or support arrangements, and alternatives when households cannot self-evacuate."),
        ("Dignified shelters", "Shelters require physical accessibility, privacy, lighting, sanitation, protection, medication, assistive devices, child-safe spaces and grievance channels."),
        ("Accountable relief", "Transparent eligibility, public information, disaggregated lists, appeal and correction mechanisms reduce exclusion and elite capture in relief distribution."),
        ("Protection and psychosocial support", "Protection includes safeguarding from violence, exploitation, family separation and discrimination, alongside mental-health and psychosocial support."),
        ("Community-led recovery", "Recovery should restore livelihoods, services, social networks and local agency while reducing future risk, rather than treating affected people as passive beneficiaries."),
        ("Participation-outcome firewall", "A consultation, guideline, volunteer count or committee proves an input; inclusive receipt, safe evacuation, dignified shelter and equitable recovery need separate evidence."),
    ]
    traps = [
        "Do not romanticise community capacity or use it to excuse public under-provision.",
        "Do not treat local knowledge as a substitute for scientific warning.",
        "Do not homogenise women, children, older persons, persons with disabilities or migrants.",
        "Do not equate volunteer headcount with readiness.",
        "Do not make paternalistic claims that remove affected people's decision-making role.",
        "Do not treat one digital warning channel as accessible to everyone.",
        "Do not describe evacuation without transport and assistance arrangements.",
        "Do not reduce shelter adequacy to roof and floor space.",
        "Do not confuse disaster displacement with automatic refugee status.",
        "Do not infer inclusive outcomes from a policy or guideline alone.",
    ]
    titles = [
        "CBDRR and co-production",
        "Local knowledge and scientific knowledge",
        "Communities as trained first responders",
        "Panchayats ULBs and DDMA linkage",
        "SHGs volunteers and community institutions",
        "Social vulnerability and intersectionality",
        "Gender-responsive disaster risk reduction",
        "Children and continuity of protection",
        "Older persons and care continuity",
        "Disability-inclusive DRR",
        "Migrants displacement and legal-status caution",
        "Accessible warning and feedback",
        "Inclusive evacuation transport and shelter",
        "Relief accountability and protection",
        "Community-led recovery and evidence boundary",
    ]
    routes = [
        "Define participation as co-production with public responsibility.",
        "Combine lived knowledge with technical risk information.",
        "Specify role, training, equipment and safety.",
        "Name the local institution and its linkage to district planning.",
        "Allocate before, during and after roles to each institution.",
        "Identify the exact risk mechanism for each group.",
        "Connect participation, safety, health and livelihood dimensions.",
        "Trace warning, evacuation, shelter, tracing and education continuity.",
        "Include mobility, medicine, care and voice.",
        "Use accessibility and participation as design tests.",
        "Separate displacement protection from refugee-law status.",
        "Test receipt, comprehension, trust and feedback.",
        "Map assistance from household to destination.",
        "Build transparent correction and grievance mechanisms.",
        "Conclude with agency, risk reduction and verified outcomes.",
    ]
    panels = [
        common.panel("CBDRR co-production map", "systems-map", [
            "COMMUNITY -> knowledge, priorities, first action",
            "PRI / ULB -> local plan and services",
            "DDMA / STATE -> authority, resources, standards",
            "RULE -> participation complements public duty",
        ], ["CBDRR", "Panchayats and ULBs"]),
        common.panel("Knowledge bridge", "comparison-table", [
            "LOCAL -> routes, trust, seasonal and social detail",
            "SCIENTIFIC -> hazard monitoring and forecasts",
            "ADMINISTRATIVE -> authority, resources, evacuation orders",
            "BEST RESULT -> combine and validate all three",
        ], ["Local knowledge"]),
        common.panel("Community role cycle", "process-flow", [
            "BEFORE -> map risk, train, drill, plan",
            "DURING -> relay warning, assist evacuation, first aid",
            "AFTER -> verify needs, protect, restore livelihoods",
            "SAFEGUARD -> trained roles and no harmful improvisation",
        ], ["Community first response", "Community institutions"]),
        common.panel("Local institution ladder", "hierarchy", [
            "HOUSEHOLD / WARD / VILLAGE",
            "SHG / CBO / VOLUNTEER GROUP",
            "PANCHAYAT / ULB",
            "DDMA -> district plan, resources and accountability",
        ], ["Panchayats and ULBs", "Community institutions"]),
        common.panel("Volunteer readiness firewall", "status-ladder", [
            "ENROLLED -> TRAINED -> REFRESHED",
            "EQUIPPED -> ACTIVATION PROTOCOL -> SUPERVISED ACTION",
            "AFTER-ACTION LEARNING -> RETENTION",
            "HEADCOUNT ALONE -> NOT READINESS",
        ], ["Volunteer boundary"]),
        common.panel("Social vulnerability matrix", "matrix", [
            "POVERTY / HOUSING / LIVELIHOOD",
            "GENDER / AGE / DISABILITY / HEALTH",
            "LANGUAGE / DOCUMENTS / DISPLACEMENT",
            "INTERSECTIONS -> COMPOUND RISK",
        ], ["Social vulnerability", "Intersectionality"]),
        common.panel("Life-course protection", "comparison-table", [
            "CHILDREN -> tracing, nutrition, safe learning",
            "OLDER PERSONS -> medicine, mobility, care",
            "WOMEN / GIRLS -> privacy, safety, health, voice",
            "DESIGN -> distinct needs, no homogeneous category",
        ], ["Gender-responsive protection", "Children", "Older persons"]),
        common.panel("Disability-inclusive chain", "process-flow", [
            "PARTICIPATORY MAPPING -> ACCESSIBLE WARNING",
            "ASSISTED EVACUATION -> BARRIER-FREE SHELTER",
            "ASSISTIVE DEVICE / SUPPORT CONTINUITY",
            "FEEDBACK -> CORRECT EXCLUSION",
        ], ["Persons with disabilities", "Accessible warnings", "Inclusive evacuation"]),
        common.panel("Migrant-displacement firewall", "comparison-table", [
            "DISPLACED -> movement caused by disaster impacts",
            "MIGRANT -> may face language and documentation barriers",
            "REFUGEE STATUS -> not automatic under 1951 Convention",
            "PROTECTION -> domestic law and human-rights duties remain",
        ], ["Migrants and displaced persons"]),
        common.panel("Warning-to-shelter route", "process-flow", [
            "ACCESSIBLE MESSAGE -> CONFIRM COMPREHENSION",
            "ASSISTED TRANSPORT -> SAFE ROUTE",
            "DIGNIFIED ACCESSIBLE SHELTER",
            "REGISTER + FEEDBACK + FAMILY LINK",
        ], ["Accessible warnings", "Inclusive evacuation", "Dignified shelters"]),
        common.panel("Relief accountability loop", "feedback-loop", [
            "CLEAR ELIGIBILITY -> PUBLIC LIST / INFORMATION",
            "DISAGGREGATED NEEDS -> DELIVERY",
            "APPEAL / CORRECTION -> UPDATED LIST",
            "PROTECTION MONITORING -> RECOVERY FEEDBACK",
        ], ["Accountable relief", "Protection and psychosocial support"]),
        common.panel("Inclusive answer spine", "answer-spine", [
            "NAME GROUP -> IDENTIFY RISK MECHANISM",
            "ASSIGN COMMUNITY + INSTITUTIONAL ROLE",
            "DESIGN ACCESSIBLE WARNING EVACUATION SHELTER RELIEF",
            "RESTORE AGENCY -> VERIFY OUTCOME",
        ], ["Community-led recovery", "Participation-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2019", "GS-III",
            "Discuss vulnerability as a concept for defining disaster impacts and explain its types.",
            "Verified direct routing belongs to Topic 01; this conservative card supplies the social and inclusive-protection dimension.",
            [6, 7, 8, 9, 10, 11, 12]),
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Discuss the shift from reactive to proactive disaster management.",
            "Verified direct routing belongs to Topic 02; this card shows how local planning, trained volunteers and inclusive preparedness operationalise the shift.",
            [0, 2, 3, 4, 5, 13, 14]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe the elements that determine disaster resilience.",
            "Verified direct routing belongs to Topic 01; this card conservatively routes local knowledge, social capacity and inclusive protection as resilience elements.",
            [0, 1, 2, 6, 7, 18, 19]),
    ]
    return common.topic(
        3, "Community-Based DRR and Inclusive Protection",
        "03_Community-Based-DRR-and-Inclusive-Protection", facts, traps,
        [
            (10, "Explain the role of community institutions in disaster risk reduction.", [0, 1, 2, 3, 4]),
            (10, "Why must volunteer numbers be distinguished from community-response readiness?", [2, 4, 5, 19]),
            (15, "Analyse social vulnerability through gender, age, disability and displacement.", [6, 7, 8, 9, 10, 11, 12]),
            (15, "Design an accessible warning, evacuation and shelter chain for at-risk groups.", [11, 13, 14, 15, 16]),
            (20, "Critically examine the claim that communities are the first responders in disasters.", [0, 1, 2, 3, 4, 5, 19]),
            (20, "Propose an inclusive protection and community-led recovery framework that preserves dignity, accountability and agency.", [6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "community-based disaster risk reduction", "local knowledge",
            "Panchayats", "ULBs", "SHGs",
            "social vulnerability", "gender", "children", "elderly",
            "persons with disabilities", "migrants", "accessible",
            "Aapda Mitra", "Yuva Aapda Mitra", "grievance",
        ],
        "No audited GS-III PYQ directly and solely owns CBDRR or inclusive protection. These three cards are explicitly marked as conservative dimensions of verified questions owned by Topics 01 and 02.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered disability protection law, Aapda Mitra, Yuva Aapda Mitra and NDMA guidance. Blocked or thin pages are logged; programme scale and guideline publication are never converted into readiness or inclusive-outcome claims.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "COMMUNITY INSTITUTIONS AND LOCAL-KNOWLEDGE MAP",
            "GROUP-SPECIFIC WARNING EVACUATION SHELTER AND RELIEF FIREWALLS",
            "ACCOUNTABLE PARTICIPATION AND RECOVERY ANSWER SPINE",
            "CURRENT PROGRAMME AND INCLUSIVE-OUTCOME EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE CBDRR AS CO-PRODUCTION NOT STATE WITHDRAWAL",
            "MAP LOCAL KNOWLEDGE PRI ULB DDMA SHG CBO AND VOLUNTEERS",
            "NAME EACH AT-RISK GROUP AND ITS DISTINCT RISK MECHANISM",
            "DESIGN ACCESSIBLE WARNING EVACUATION SHELTER AND RELIEF",
            "ADD GRIEVANCE PROTECTION AND PSYCHOSOCIAL SUPPORT",
            "RESTORE LIVELIHOODS SOCIAL NETWORKS AND LOCAL AGENCY",
            "VERIFY INCLUSIVE OUTCOMES RATHER THAN INPUT COUNTS",
        ],
    )


TOPIC_03 = _build()
