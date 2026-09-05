"""Learner-v2 source data: Ethics Topic 12, Corporate Governance and International Ethics."""

SESSION_TITLES = (
    "Ethics in business, corporate governance and CSR: the three-layer foundation",
    "Core definitions and the domestic-international integrity architecture",
    "How corporate governance and international ethics interlock with public administration",
    "Indian applications, institutional evolution and the compliance-theatre warning",
    "Prelims facts, close-option traps and answer differentiators",
    "PYQ ownership, cross-links and core Mains theses",
    "Probable questions and exam entry points",
    "CSR doctrine: thresholds, unspent funds, impact assessment and limits",
    "War ethics, international aid and non-refoulement boundaries",
    "Evidence units, directive decoding, case architecture and final synthesis",
)

SESSION_GROUPS = (
    ("1",),
    ("2",),
    ("3",),
    ("4",),
    ("5", "6"),
    ("7", "8"),
    ("9",),
    ("10",),
    ("11",),
    ("12", "13", "14"),
)

MCQ_ITEMS = (
    {
        "label": "Ethics in business rejects a bolt-on ethics department",
        "statement": (
            "The ARC preference for ethics in business requires integrity to shape ordinary pricing, "
            "procurement, labour, accounting and environmental decisions rather than remain an external "
            "public-relations or training layer."
        ),
        "scenario_a": (
            "An Indian manufacturer runs annual ethics workshops, yet sales incentives reward concealment "
            "of product defects. Which principle exposes the weakness of this arrangement?"
        ),
        "scenario_b": (
            "A listed company gives its ethics officer independent access to the board and escalation power "
            "over high-risk transactions. Which conception of business ethics is being institutionalised?"
        ),
        "family": "business ethics and governance layers",
        "group": "business ethics and governance layers",
    },
    {
        "label": "Corporate governance concerns accountable direction and control",
        "statement": (
            "Corporate governance is the structure through which a company is directed, supervised and held "
            "accountable, including board oversight, audit, disclosure, conflict management and scrutiny of "
            "related-party transactions."
        ),
        "scenario_a": (
            "A hospital chain forms an independent procurement committee, records recusals and discloses "
            "evaluation criteria. Which institutional layer is primarily being strengthened?"
        ),
        "scenario_b": (
            "A promoter-controlled company makes major related-party purchases without independent review. "
            "Which ethical architecture is deficient even before the transaction's price is assessed?"
        ),
        "family": "business ethics and governance layers",
        "group": "business ethics and governance layers",
    },
    {
        "label": "Core-business ethics concerns the means of earning profit",
        "statement": (
            "Core-business ethics evaluates whether revenue is earned through honest accounts, safe products, "
            "fair labour, non-bribery and environmental responsibility; philanthropy cannot cleanse unethical "
            "operations."
        ),
        "scenario_a": (
            "A food company funds village clinics while knowingly selling export-rejected goods domestically. "
            "Which ethical layer remains violated despite the social spending?"
        ),
        "scenario_b": (
            "A supplier refuses confidential rival-bid data although winning the tender would preserve jobs. "
            "Which dimension of corporate conduct controls the decision?"
        ),
        "family": "business ethics and governance layers",
        "group": "business ethics and governance layers",
    },
    {
        "label": "CSR is distinct from governance structure and core conduct",
        "statement": (
            "CSR is a statutory, ring-fenced expenditure and transfer regime for qualifying companies; it "
            "supplements but does not replace ethical operations, board accountability or lawful compliance."
        ),
        "scenario_a": (
            "A company meets its mandated social-spend amount but under-reports emissions from its factories. "
            "Which distinction prevents the spend from proving overall ethical performance?"
        ),
        "scenario_b": (
            "A board treats CSR as optional charity after the company crosses the statutory threshold. Which "
            "feature of the Indian framework corrects this claim?"
        ),
        "family": "business ethics and governance layers",
        "group": "business ethics and governance layers",
    },
    {
        "label": "CSR applicability uses three alternative financial thresholds",
        "statement": (
            "Companies Act, 2013, s.135 applies when any one immediately preceding-year threshold is met: "
            "net worth of at least Rs 500 crore, turnover of at least Rs 1,000 crore, or net profit of at "
            "least Rs 5 crore."
        ),
        "scenario_a": (
            "An Indian company has net profit above Rs 5 crore but falls below the net-worth and turnover "
            "figures. How should its board assess CSR applicability?"
        ),
        "scenario_b": (
            "A finance officer adds all three statutory thresholds and says every one must be crossed. Which "
            "close-option error has been made?"
        ),
        "family": "CSR statutory architecture",
        "group": "CSR statutory architecture",
    },
    {
        "label": "The CSR base obligation is a two-percent formula",
        "statement": (
            "A qualifying company must spend at least two percent of the average net profits of the three "
            "immediately preceding financial years on eligible Schedule VII activities through its approved "
            "CSR framework."
        ),
        "scenario_a": (
            "A newly qualifying company calculates its obligation as two percent of current turnover. Which "
            "statutory calculation has it confused?"
        ),
        "scenario_b": (
            "A board says compliance is discretionary because it may choose among social projects. Which "
            "distinction between project choice and minimum obligation is decisive?"
        ),
        "family": "CSR statutory architecture",
        "group": "CSR statutory architecture",
    },
    {
        "label": "Unspent CSR follows different ongoing and non-ongoing routes",
        "statement": (
            "The 2019 statutory architecture requires non-ongoing unspent amounts to reach a specified "
            "Schedule VII fund within six months, while ongoing-project amounts enter an Unspent CSR Account "
            "within thirty days and remain subject to the three-year completion route."
        ),
        "scenario_a": (
            "A company leaves money for an approved multi-year sanitation project in its ordinary bank "
            "account after year-end. Which transfer distinction has it ignored?"
        ),
        "scenario_b": (
            "A board treats every unspent amount identically although one project is ongoing and another "
            "never began. Which statutory architecture should guide it?"
        ),
        "family": "CSR statutory architecture",
        "group": "CSR statutory architecture",
    },
    {
        "label": "CSR impact assessment has a threshold and a separate cost cap",
        "statement": (
            "The 2021 rules introduced independent impact assessment for companies with an average CSR "
            "obligation of at least Rs 10 crore and qualifying completed projects; the 2022 amendment revised "
            "the assessment-cost cap to two percent or Rs 50 lakh, whichever is higher."
        ),
        "scenario_a": (
            "A compliance note attributes creation of the impact-assessment mandate to the 2022 amendment. "
            "Which chronology should the legal team restore?"
        ),
        "scenario_b": (
            "A large CSR obligor evaluates only spending receipts and never tests completed project outcomes. "
            "Which regulatory mechanism addresses this box-ticking risk?"
        ),
        "family": "CSR statutory architecture",
        "group": "CSR statutory architecture",
    },
    {
        "label": "The agency problem requires independent oversight",
        "statement": (
            "Separation of ownership from managerial control can let executives pursue private, short-term or "
            "concealed interests; independent boards, audit and disclosure reduce this agency problem without "
            "eliminating judgment."
        ),
        "scenario_a": (
            "Managers hide a loss-making related-party purchase from dispersed shareholders to protect bonuses. "
            "Which foundational governance problem is illustrated?"
        ),
        "scenario_b": (
            "A board creates independent audit review and requires material-interest declarations by executives. "
            "Which risk is this design intended to reduce?"
        ),
        "family": "corporate controls and enforcement",
        "group": "corporate controls and enforcement",
    },
    {
        "label": "Stakeholder duties extend beyond shareholder returns",
        "statement": (
            "A stakeholder model treats employees, consumers, communities, the environment and future generations "
            "as legitimate constraints on profit-seeking, while a shareholder model centres duties to owners and "
            "long-term enterprise value."
        ),
        "scenario_a": (
            "A data-centre company considers only quarterly returns when deciding whether to honour a verified "
            "emissions-reduction commitment. Which broader ethical model is missing?"
        ),
        "scenario_b": (
            "A hospital procurement decision weighs patient safety, employees, competing vendors and financial "
            "sustainability, not merely promoter preference. Which model does this reflect?"
        ),
        "family": "corporate controls and enforcement",
        "group": "corporate controls and enforcement",
    },
    {
        "label": "SFIO is a statutory multidisciplinary fraud-investigation body",
        "statement": (
            "India's SFIO began by Government Resolution in 2003 and received statutory footing under Companies "
            "Act, 2013, s.211; its arrest power under s.212(8) requires material-based reason to believe guilt "
            "for the specified fraud offence."
        ),
        "scenario_a": (
            "A complex company fraud combines accounting manipulation, shell entities and digital evidence. "
            "Which institutional design responds to fragmented investigation?"
        ),
        "scenario_b": (
            "An official says SFIO may arrest anyone merely because an inquiry has opened. Which bounded "
            "statutory formulation corrects the claim?"
        ),
        "family": "corporate controls and enforcement",
        "group": "corporate controls and enforcement",
    },
    {
        "label": "SOX civil protection and criminal retaliation are separate",
        "statement": (
            "Sarbanes-Oxley s.806 provides a civil whistleblower remedy under 18 U.S.C. 1514A, whereas s.1107 "
            "created the separate criminal retaliation offence under 18 U.S.C. 1513(e), carrying the stated "
            "imprisonment exposure."
        ),
        "scenario_a": (
            "A training note says the ten-year criminal punishment is contained in the employee's civil-remedy "
            "provision. Which legal distinction must be restored?"
        ),
        "scenario_b": (
            "A listed company's employee seeks reinstatement after retaliation, while prosecutors assess a "
            "separate retaliatory offence. Which two-track architecture is illustrated?"
        ),
        "family": "corporate controls and enforcement",
        "group": "corporate controls and enforcement",
    },
    {
        "label": "UNCAC is a treaty framework for States Parties",
        "statement": (
            "UNCAC was adopted on 31 October 2003, entered into force on 14 December 2005, and binds States "
            "Parties through preventive, criminalisation, international-cooperation and asset-recovery obligations; "
            "India ratified it on 9 May 2011."
        ),
        "scenario_a": (
            "An answer describes UNCAC as a voluntary corporate code directly prosecuting companies worldwide. "
            "Which treaty characteristic corrects the statement?"
        ),
        "scenario_b": (
            "Indian officials seek cooperation in tracing cross-border corruption proceeds. Which global "
            "framework supplies the treaty-level architecture?"
        ),
        "family": "international anti-corruption layers",
        "group": "international anti-corruption layers",
    },
    {
        "label": "The ADB-OECD Action Plan is not the OECD Anti-Bribery Convention",
        "statement": (
            "India endorsed the regional, non-binding ADB-OECD Anti-Corruption Action Plan in 2001, but India "
            "is not a party to the separate 1997 OECD Anti-Bribery Convention; cooperative and treaty status "
            "must not be conflated."
        ),
        "scenario_a": (
            "A policy brief infers that Indian participation in an Asia-Pacific action plan makes India party "
            "to the OECD Anti-Bribery Convention. Which distinction defeats the inference?"
        ),
        "scenario_b": (
            "Officials compare peer cooperation in Asia with binding convention membership. Which status "
            "difference must remain explicit?"
        ),
        "family": "international anti-corruption layers",
        "group": "international anti-corruption layers",
    },
    {
        "label": "FCPA combines anti-bribery and issuer accounting rules",
        "statement": (
            "The United States FCPA prohibits covered corrupt payments to foreign officials and separately "
            "requires issuers to maintain accurate books, records and adequate internal accounting controls, "
            "using an extraterritorial jurisdictional logic."
        ),
        "scenario_a": (
            "A multinational records a consultant payment inaccurately even though bribery cannot yet be "
            "proved. Which additional FCPA compliance limb remains relevant?"
        ),
        "scenario_b": (
            "A compliance officer describes the FCPA only as a ban on receiving bribes. Which two errors "
            "does the official framework reveal?"
        ),
        "family": "international anti-corruption layers",
        "group": "international anti-corruption layers",
    },
    {
        "label": "International anti-corruption mechanisms use distinct logics",
        "statement": (
            "UNCAC uses treaty obligations, the ADB-OECD plan uses regional cooperation, lender conditions "
            "use financing leverage, and the FCPA uses domestic law with extraterritorial reach; these layers "
            "should not be collapsed into one mechanism."
        ),
        "scenario_a": (
            "A ministry memo calls a World Bank funding condition legally identical to UNCAC ratification. "
            "Which analytical distinction is missing?"
        ),
        "scenario_b": (
            "An Indian company maps treaty duties, lender requirements and foreign anti-bribery exposure "
            "separately before bidding abroad. Which layered approach is demonstrated?"
        ),
        "family": "international anti-corruption layers",
        "group": "international anti-corruption layers",
    },
    {
        "label": "Aid ethics requires recipient ownership",
        "statement": (
            "Recipient ownership means resource-challenged countries should lead their development priorities; "
            "donor expertise and safeguards may support but should not displace locally accountable choice or "
            "reduce aid to paternalistic control."
        ),
        "scenario_a": (
            "A donor designs a rural-health programme without consulting the recipient government or affected "
            "communities. Which aid-effectiveness principle is weakened?"
        ),
        "scenario_b": (
            "A recipient-led plan is jointly monitored by donors without dictating every policy choice. Which "
            "ethical balance is being respected?"
        ),
        "family": "international humanitarian ethics",
        "group": "international humanitarian ethics",
    },
    {
        "label": "Aid conditionality trades accountability against sovereignty",
        "statement": (
            "Conditions attached to aid may protect funds, rights or reform objectives, but can also constrain "
            "sovereignty and self-determined development; ethical evaluation asks whether conditions are "
            "transparent, proportionate and connected to legitimate purposes."
        ),
        "scenario_a": (
            "A lender conditions disaster relief on unrelated commercial concessions. Which ethical concern "
            "arises even if the recipient urgently needs funds?"
        ),
        "scenario_b": (
            "A donor requires audited use of health funds and publishes the condition before disbursement. "
            "Which qualified defence of conditionality is available?"
        ),
        "family": "international humanitarian ethics",
        "group": "international humanitarian ethics",
    },
    {
        "label": "Aid creates dual accountability and dependency risks",
        "statement": (
            "Donors are accountable for fair, effective and non-corrupt design, while recipients are accountable "
            "for transparent use; long dependence can weaken local institutions, revenue effort or markets unless "
            "aid builds capacity and an exit path."
        ),
        "scenario_a": (
            "Imported free grain repeatedly undercuts local farmers and prevents domestic procurement systems "
            "from developing. Which long-term aid risk is illustrated?"
        ),
        "scenario_b": (
            "A health grant funds local capacity, publishes expenditure and transfers management over time. "
            "Which two ethical duties are addressed?"
        ),
        "family": "international humanitarian ethics",
        "group": "international humanitarian ethics",
    },
    {
        "label": "Non-refoulement requires a carefully qualified Indian answer",
        "statement": (
            "Refugee Convention Article 33 prohibits return to threatened persecution for States Parties; India "
            "is not party to the 1951 Convention or 1967 Protocol, so Indian answers should add Article 21 "
            "protection and avoid treating an interim order as final settlement."
        ),
        "scenario_a": (
            "An officer says India's non-membership makes the risk of persecution ethically irrelevant. Which "
            "rights-sensitive qualification should guide review?"
        ),
        "scenario_b": (
            "A legal brief presents an interim Supreme Court order as a final universal ruling on customary "
            "non-refoulement. Which boundary has been crossed?"
        ),
        "family": "international humanitarian ethics",
        "group": "international humanitarian ethics",
    },
    {
        "label": "War ethics separates resort to force from conduct in war",
        "statement": (
            "Sovereignty and lawful resort to force concern jus ad bellum, while distinction and proportionality "
            "govern jus in bello; humanitarian neutrality protects impartial access and does not erase "
            "accountability for violations."
        ),
        "scenario_a": (
            "A commentator argues that a claimed just cause permits indiscriminate attacks on civilians. Which "
            "two-level war-ethics distinction rejects the claim?"
        ),
        "scenario_b": (
            "An aid organisation serves civilians on both sides while avoiding support for military objectives. "
            "Which principle enables its access?"
        ),
        "family": "applied corporate and international dilemmas",
        "group": "applied corporate and international dilemmas",
    },
    {
        "label": "Responsible arms export requires risk assessment",
        "statement": (
            "A responsible arms-export decision weighs end use, diversion, civilian-harm and human-rights risk, "
            "regional stability, recipient conduct, strategic necessity and monitoring; commercial gain or "
            "friendship alone cannot settle the decision."
        ),
        "scenario_a": (
            "An Indian manufacturer is asked to export missiles to a friendly government facing credible "
            "diversion concerns. Which ethical process should precede approval?"
        ),
        "scenario_b": (
            "A board assumes India is legally bound as an Arms Trade Treaty party. Which caution must accompany "
            "the ethical risk assessment?"
        ),
        "family": "applied corporate and international dilemmas",
        "group": "applied corporate and international dilemmas",
    },
    {
        "label": "Conflict disclosure normally requires recusal and independent evaluation",
        "statement": (
            "Where a procurement chair's close relative is a bidder, disclosure alone may not protect impartiality "
            "or its appearance; recusal, documented criteria and independent evaluation provide the proportionate "
            "governance response."
        ),
        "scenario_a": (
            "Sneha's brother bids to supply equipment to the hospital committee she chairs. Which response best "
            "protects patients, fair competition and her professional integrity?"
        ),
        "scenario_b": (
            "A manager privately promises to be fair but continues scoring a sibling's bid. Which governance "
            "safeguard remains missing?"
        ),
        "family": "applied corporate and international dilemmas",
        "group": "applied corporate and international dilemmas",
    },
    {
        "label": "Product safety cannot be downgraded for domestic consumers",
        "statement": (
            "Equal human dignity, consumer safety and professional integrity prohibit diverting export-rejected "
            "or defective goods into the Indian market merely to avoid loss; independent testing, recall, "
            "disclosure and remediation are required."
        ),
        "scenario_a": (
            "A shoe company pressures its inspection team to clear an export-rejected consignment for domestic "
            "sale. Which ethical floor controls the inspector's response?"
        ),
        "scenario_b": (
            "A food company discovers domestic products violate approved health standards. Which restoration "
            "approach should accompany regulatory action?"
        ),
        "family": "applied corporate and international dilemmas",
        "group": "applied corporate and international dilemmas",
    },
)

PYQS = (
    {
        "year": 2020,
        "question": (
            "GS-IV Q8: The Chairman of Bharat Missiles Ltd (BML) was watching a program on TV "
            "wherein the Prime Minister was addressing the nation on the necessity of developing "
            "a self-reliant India. He subconsciously nodded in agreement and smiled to himself as "
            "he mentally reviewed BML's journey in the past two decades. BML had admirably "
            "progressed from producing first generation anti-tank guided missiles (ATGMs) to "
            "designing and producing state of the art ATGM weapon systems that would be the envy "
            "of any army. He sighed in reconciliation with his assumptions that the government "
            "would probably not alter the status quo of a ban on export of military weaponry. To "
            "his surprise, the very next day he got a telephone call from the Director General, "
            "Ministry of Defence, asking him to discuss the modalities of increasing BML production "
            "of ATGMs as there is a possibility of exporting the same to a friendly foreign country. "
            "The Director General wanted the Chairman to discuss the details with his staff at Delhi "
            "next week. Two days later, at a press conference, the Defence Minister stated that he "
            "aims to double the current weapons export levels within five years. This would give an "
            "impetus to financing the development and manufacture of indigenous weapons in the "
            "country. He also stated that all indigenous arms manufacturing nations have a very good "
            "record of international arms trade. As Chairman of BML, what are your views on the "
            "following points? (a) As an arms exporter of a responsible nation like India, what are "
            "the ethical issues involved in arms trade? (b) List five ethical factors that would "
            "influence the decision to sell arms to foreign governments. (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Exact full case and both demands verified against "
            "books\\more_previous_papers\\Gen_St_P4.pdf, page 6. Topic 12 owns the "
            "international-ethics and corporate-decision route. India must not be described as an "
            "Arms Trade Treaty party; use ATT-style risk factors only as an ethical benchmark."
        ),
        "answer": (
            "BML's decision implicates national security, legitimate self-defence, economic self-reliance "
            "and employment, but also civilian life, regional stability and India's international reputation. "
            "Arms are not ordinary exports: foreseeable misuse can make the supplier morally connected to "
            "harm even where the immediate buyer is a friendly government.\n\n"
            "Five decisive factors are: first, the recipient's record of compliance with international "
            "humanitarian law and human rights; second, the probability of diversion to non-state actors or "
            "unauthorised users; third, the risk that the transfer will intensify aggression, repression or a "
            "regional arms race; fourth, the stated defensive need, proportionality and strategic legitimacy "
            "of the proposed end use; and fifth, enforceable end-use monitoring, suspension and accountability "
            "arrangements. Additional concerns include secrecy, corruption in procurement, technology leakage "
            "and opportunity cost.\n\n"
            "The Chairman should therefore seek an inter-agency, evidence-based risk assessment rather than "
            "treat friendship or export revenue as sufficient. The contract should identify end users, prohibit "
            "unauthorised re-transfer, permit verification and provide suspension if credible misuse emerges. "
            "Commercial confidentiality cannot hide the criteria used by competent public authorities.\n\n"
            "India is not an Arms Trade Treaty party, so an answer should not claim treaty membership. Yet "
            "distinction, proportionality, civilian protection and responsible risk assessment remain compelling "
            "ethical standards. A justified export is one whose defensive and public benefits survive a serious "
            "foreseeable-harm test. Periodic post-export review should test diversion indicators and permit a "
            "credible suspension decision rather than make monitoring a one-time contractual formality."
        ),
    },
    {
        "year": 2020,
        "question": (
            "GS-IV Q11: Parmal is a small but underdeveloped district. It has rocky terrain that is "
            "not suitable for agriculture, though some subsistence agriculture is being done on "
            "small plots of land. The area receives adequate rainfall and has an irrigation canal "
            "flowing through it. Amria, its administrative centre, is a medium sized town. It houses "
            "a large district hospital, an Industrial Training Institute and some privately owned "
            "skill training centres. It has all the facilities of a district headquarters. A trunk "
            "railway line passes approximately 50 kilometres from Amria. Its poor connectivity is a "
            "major reason for the absence of any major industry therein. The state government offers "
            "a 10 years tax holiday as an incentive to new industry. In 2010 Anil, an industrialist, "
            "decided to take benefits to set up Amria Plastic Works (APW) in Noora village, about "
            "20 km from Amria. While the factory was being built, Anil hired the required key labour "
            "and got them trained at the skill training centres at Amria. This act of his made the "
            "key personnel very loyal to APW. APW started production in 2011 with the labour drawn "
            "fully from Noora village. The villagers were very happy to get employment near their "
            "homes and were motivated by the key personnel to meet the production targets with high "
            "quality. APW started making large profits, a sizeable portion of which was used to "
            "improve the quality of life in Noora. By 2016, Noora could boast of a greener village "
            "and a renovated village temple. Anil liaised with the local MLA to increase the frequency "
            "of the bus services to Amria. The government also opened a primary health care centre "
            "and primary school at Noora in buildings constructed by APW. APW used its CSR funds to "
            "set up women's self-help groups, subsidize primary education to the village children and "
            "procure an ambulance for use by its employees and the needy. In 2019, there was a minor "
            "fire in APW. It was quickly extinguished as fire safety protocols were in place in the "
            "factory. Investigations revealed that the factory had been using electricity in excess "
            "of its authorized capacity. This was soon rectified. The next year, due to a nationwide "
            "lockdown, the requirement of production fell for four months. Anil decided that all "
            "employees would be paid regularly. He employed them to plant trees and improve the "
            "village habitat. APW had developed a reputation of high quality production and a "
            "motivated workforce. Critically analyse the story of APW and state the ethical issues "
            "involved. Do you consider APW as a role model for development of backward areas? Give "
            "reasons. (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Exact full case and both demands verified against "
            "books\\more_previous_papers\\Gen_St_P4.pdf, page 10. Topic 12 owns the "
            "CSR/core-business-ethics distinction and stakeholder analysis."
        ),
        "answer": (
            "APW demonstrates an ethically valuable local-development model. It created nearby employment, "
            "invested in skills, retained workers during the lockdown, supported women's groups, education, "
            "health access, transport and environmental improvement. Fire-safety protocols worked, and the "
            "company corrected excess electricity use after investigation. These actions strengthened human "
            "capabilities and reciprocal trust rather than treating Noora merely as a labour pool.\n\n"
            "However, critical appraisal must separate outcomes, motives and governance. Loyalty generated by "
            "dependence can suppress worker voice. Liaison with the MLA should remain transparent and must not "
            "become preferential access. Temple renovation may be socially welcomed but CSR choices should be "
            "inclusive, needs-based and consistent with lawful Schedule VII purposes. Excess electricity use "
            "shows that community expenditure cannot substitute for compliance in core operations. Plastic "
            "production also requires credible waste and environmental safeguards, which the facts do not establish.\n\n"
            "APW is therefore a qualified role model, not a perfect template. Replication should retain local "
            "hiring, skill formation, wage continuity and community partnership while adding independent needs "
            "assessment, worker grievance channels, environmental monitoring, transparent CSR disclosure and "
            "periodic impact evaluation. Government must still provide public services and regulate the factory; "
            "corporate benevolence cannot replace state responsibility.\n\n"
            "The ethical lesson is stakeholder governance: enterprise success can support backward-area development, "
            "but legitimacy depends on lawful core conduct, inclusive participation and durable institutions, not "
            "only visible CSR spending. Community consent and published outcome indicators would also reduce the "
            "risk that corporate priorities quietly replace locally identified needs."
        ),
    },
    {
        "year": 2021,
        "question": (
            "GS-IV Q5(a): \"Refugees should not be turned back to the country where they would "
            "face persecution or human right violation.\" Examine the statement with reference "
            "to ethical dimension being violated by the nation claiming to be democratic with "
            "open society. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 3. "
            "Topic 12 owns non-refoulement as international ethics; India is not party to the "
            "1951 Refugee Convention or 1967 Protocol, and Mohammad Salimullah was an interim order."
        ),
        "answer": (
            "Returning a person to a place where life or freedom faces persecution violates dignity, compassion, "
            "the right to life and the democratic claim that state power is limited by human rights. Refugee "
            "Convention Article 33 expresses non-refoulement for States Parties. Ethically, a democratic open "
            "society should not exploit a vulnerable person's lack of citizenship to expose her to foreseeable "
            "grave harm.\n\n"
            "The duty is not absolute naivety. States may verify identity, assess security risk individually and "
            "use fair procedures against genuine threats. But collective expulsion, stereotyping or return without "
            "hearing treats persons as instruments of domestic politics. Temporary protection, access to UNHCR "
            "processes and reasoned review can balance security with humanity.\n\n"
            "India is not party to the 1951 Convention or 1967 Protocol; Indian answers should therefore add "
            "Article 21 protection of non-citizens and avoid overstating unsettled customary-law conclusions. "
            "NHRC v. State of Arunachal Pradesh supports protection of life and liberty, while Mohammad Salimullah "
            "should be described only as an interim-order boundary. Democratic legitimacy is tested most clearly "
            "when fear does not erase due process."
        ),
    },
    {
        "year": 2021,
        "question": (
            "GS-IV Q11: A reputed food product company based in India developed a food product for "
            "the international market and started exporting the same after getting necessary approvals. "
            "The company announced this achievement and also indicated that soon the product will be made "
            "available for the domestic consumers with almost same quality and health benefits. Accordingly, "
            "the company got its product approved by the domestic competent authority and launched the "
            "product in Indian market. The company could increase its market share over a period of time "
            "and earned substantial profit both domestically and internationally. However, the random sample "
            "test conducted by inspecting team found the product being sold domestically in variance with "
            "the approval obtained from the competent authority. On further investigation, it was also "
            "discovered that the food company was not only selling products which were not meeting the health "
            "standard of the country but also selling the rejected export products in the domestic market. "
            "This episode adversely affected the reputation and profitability of the food company. "
            "(a) What action do you visualize should be taken by the competent authority against the food "
            "company for violating the laid down domestic food standard and selling rejected export products "
            "in domestic market? (b) What course of action is available with the food company to resolve the "
            "crisis and bring back its lost reputation? (c) Examine the ethical dilemma involved in the case. "
            "(Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Exact full case and all three demands verified against "
            "books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, pages 8-9. "
            "Topic 12 owns consumer safety, core-business ethics and corporate accountability."
        ),
        "answer": (
            "The competent authority should immediately protect consumers while preserving due process. It should "
            "secure samples and records, order risk-based withdrawal or recall, suspend affected production or sale "
            "where legally warranted, require public safety communication, test the supply chain and initiate "
            "proportionate penalties or prosecution under the applicable food-safety framework after hearing. "
            "Consumers suffering harm need complaint, compensation and medical-support routes.\n\n"
            "The company should stop sale, preserve evidence and commission an independent quality and governance "
            "review. It should notify regulators and consumers truthfully, recall affected batches, compensate "
            "loss, discipline responsible executives through fair process and correct incentives that rewarded "
            "volume over safety. Batch traceability, strengthened laboratory controls, board-level risk reporting "
            "and protected internal reporting are necessary. Reputation cannot be restored through advertising "
            "or CSR donations; it must follow verifiable reform and sustained safe performance.\n\n"
            "The ethical dilemma is profit and organisational survival versus consumer health, truth and equal "
            "dignity. Selling export-rejected goods domestically also reflects a discriminatory double standard: "
            "Indian consumers are treated as less worthy. Employees may face loyalty-versus-integrity pressures, "
            "but professional duty requires escalation and refusal to certify unsafe goods.\n\n"
            "The justified course prioritises safety and candour, with proportionate enforcement and an opportunity "
            "for genuine correction. Corporate governance succeeds when the board changes the decision system that "
            "produced the misconduct, not merely the public narrative around it. Independent follow-up sampling should "
            "verify that corrective controls work across domestic and export product lines."
        ),
    },
    {
        "year": 2022,
        "question": (
            "GS-IV Q5(a): Russia and Ukraine war has been going on for the last seven months. "
            "Different countries have taken independent stands and actions keeping in view their "
            "own national interests. We are all aware that war has its own impact on the different "
            "aspects of society, including human tragedy. What are those ethical issues that are "
            "crucial to be considered while launching the war and its continuation so far? Illustrate "
            "with justification the ethical issues involved in the given state of affair. "
            "(Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, "
            "page 4. The seven-month wording is retained as the paper's dated premise; no present "
            "battlefield status is inferred."
        ),
        "answer": (
            "The decision to launch war raises jus ad bellum questions: respect for sovereignty, just cause, "
            "legitimate authority, last resort, reasonable prospect of success and proportionality of the overall "
            "response. National interest cannot by itself justify aggression or convert weaker populations into "
            "means for geopolitical advantage.\n\n"
            "Continuation raises jus in bello duties independent of which side claims justice: distinction between "
            "combatants and civilians, proportionality of attacks, precautions, humane treatment of prisoners and "
            "protection of medical and humanitarian operations. Nuclear escalation, food and energy disruption, "
            "displacement, misinformation and the burdens imposed on future generations widen the moral field. "
            "Humanitarian aid should remain neutral, impartial and independent so that access is not made a political "
            "reward.\n\n"
            "States also face duties to pursue credible diplomacy and accept a just peace when achievable. A balanced "
            "answer neither treats every use of force as identical nor permits claimed necessity to erase civilian "
            "protection. Ethical statecraft joins legitimate security with restraint, truthful public justification "
            "and continuing review of whether further force remains necessary."
        ),
    },
    {
        "year": 2022,
        "question": (
            "GS-IV Q6(b): In contemporary world, corporate sector's contribution in generating "
            "wealth and employment is increasing. In doing so, they are bringing in unprecedented "
            "onslaught on the climate, environmental sustainability and living conditions of human "
            "beings. In this background, do you find that Corporate Social Responsibility (CSR) is "
            "efficient and sufficient enough to fulfill the social roles and responsibilities needed "
            "in the corporate world for which the CSR is mandated? Critically examine. "
            "(Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated Q6(b) verified against "
            "books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, "
            "page 5. Q6(a) on whistle-blower protection belongs primarily to Topic 21; Topic 12 "
            "owns this CSR subpart."
        ),
        "answer": (
            "CSR is efficient when it creates a predictable social-investment floor, uses company capabilities and "
            "funds locally relevant education, health, livelihoods or environmental projects. India's Companies "
            "Act, 2013, s.135 makes it statutory for qualifying companies: any one of the net-worth, turnover or "
            "net-profit thresholds triggers at least two percent of average net profits of the three preceding "
            "years for Schedule VII activities. Unspent-transfer and impact-assessment rules strengthen discipline.\n\n"
            "CSR is not sufficient. A company may spend fully yet underpay labour, mis-sell products, bribe officials "
            "or conceal emissions in its core business. Projects may be publicity-led, fragmented or selected without "
            "community ownership. Greenwashing converts measurable expenditure into a substitute for difficult "
            "operational reform.\n\n"
            "Therefore CSR should be judged through need assessment, participation, independent impact evaluation "
            "and transparent board oversight, but paired with ethical core operations, environmental compliance and "
            "stakeholder governance. It is a statutory and useful social-spend floor, not a licence to externalise "
            "harm or a complete measure of corporate citizenship."
        ),
    },
    {
        "year": 2022,
        "question": (
            "GS-IV Q7: Prabhat was working as Vice President (Marketing) at Sterling Electric Ltd., "
            "a reputed multinational company. But presently the company was passing through the "
            "difficult times as the sales were continuously showing downward trend in the last two "
            "quarters. His division, which hitherto had been a major revenue contributor to the "
            "company's financial health, was now desperately trying to procure some big government "
            "order for them. But their best efforts did not yield any positive success or breakthrough. "
            "His was a professional company and his local bosses were under pressure from their "
            "London-based HO to show some positive results. In the last performance review meeting "
            "taken by the Executive Director (India Head), he was reprimanded for his poor performance. "
            "He assured them that his division is working on a special contract from the Ministry of "
            "Defence for a secret installation near Gwalior and tender is being submitted shortly. He "
            "was under extreme pressure and he was deeply perturbed. What aggravated the situation "
            "further was a warning from the top that if the deal is not clinched in favour of the "
            "company, his division might have to be closed and he may have to quit his lucrative job. "
            "There was another dimension which was causing him deep mental torture and agony. This "
            "pertained to his personal precarious financial health. He was a single earner in the family "
            "with two school-college going children and his old ailing mother. The heavy expenditure on "
            "education and medical was causing a big strain to his monthly pay packet. Regular EMI for "
            "housing loan taken from bank was unavoidable and any default would render him liable for "
            "severe legal action. In the above backdrop, he was hoping for some miracle to happen. There "
            "was sudden turn of events. His secretary informed that a gentleman-Subhash Verma wanted to "
            "see him as he was interested in the position of Manager which was to be filled in by him in "
            "the company. He further brought to his notice that his CV has been received through the "
            "office of the Minister of Defence. During interview of the candidate-Subhash Verma, he found "
            "him technically sound, resourceful and experienced marketeer. He seemed to be well-conversant "
            "with tendering procedures and having knack of follow-up and liaising in this regard. Prabhat "
            "felt that he was better choice than the rest of the candidates who were recently interviewed "
            "by him in the last few days. Subhash Verma also indicated that he was in possession of the "
            "copies of the bid documents that the Unique Electronics Ltd. would be submitting the next "
            "day to the Defence Ministry for their tender. He offered to hand over those documents subject "
            "to his employment in the company on suitable terms and conditions. He made it clear that in "
            "the process, the Sterling Electric Ltd. could outbid their rival company and get the bid and "
            "hefty Defence Ministry order. He indicated that it will be win-win situation for both-him "
            "and the company. Prabhat was absolutely stunned. It was a mixed feeling of shock and thrill. "
            "He was uncomfortable and perspiring. If accepted, all his problems would vanish instantly and "
            "he may be rewarded for securing the much awaited tender and thereby boosting company's sales "
            "and financial health. He was in a fix as to the future course of action. He was wonder-struck "
            "at the guts of Subhash Verma in having surreptitiously removing his own company papers and "
            "offering to the rival company for a job. Being an experienced person, he was examining the pros "
            "and cons of the proposal/situation and he asked him to come the next day. (a) Discuss the "
            "ethical issues involved in the case. (b) Critically examine the options available to Prabhat "
            "in the above situation. (c) Which of the above would be the most appropriate for Prabhat and "
            "why? (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Exact full case and all three demands verified against "
            "books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, "
            "pages 6-7. Topic 12 owns corporate integrity, confidential data and fair procurement; "
            "Topic 22 supplies the full case-study method."
        ),
        "answer": (
            "The stakeholders are Prabhat, his dependants and employees, Sterling Electric, Unique Electronics, "
            "Subhash, the Defence Ministry, taxpayers and national security. The issues are theft and misuse of "
            "confidential bid information, bribery through employment, unfair competition, conflict of interest, "
            "possible official influence, professional integrity and pressure created by job and family insecurity.\n\n"
            "Prabhat could accept the proposal; reject it silently; postpone and investigate privately; or reject, "
            "preserve the approach and report through competent company and tender-integrity channels. Acceptance "
            "may save jobs but corrupts recruitment and procurement, creates blackmail risk and exposes security "
            "information. Silent rejection avoids immediate wrongdoing but leaves the attempted breach and possible "
            "compromise unaddressed. Reckless confrontation or copying the documents could contaminate evidence and "
            "create legal risk.\n\n"
            "He should refuse access to the documents and make no employment bargain. He should record the encounter, "
            "preserve lawful evidence, pause Subhash's recruitment, notify independent compliance or the board, obtain "
            "legal advice and inform the competent procurement authority through a secure channel. The company should "
            "continue competing only through its own lawful bid and consider protecting affected employees through "
            "restructuring rather than fraud.\n\n"
            "Prabhat's financial hardship is morally relevant but cannot justify making citizens and competitors bear "
            "the cost. The chosen course protects fair competition, national security and long-term corporate reputation. "
            "Implementation should minimise unnecessary disclosure, avoid prejudging guilt and permit independent "
            "investigation with due process. The board should also review whether unrealistic sales incentives created "
            "predictable pressure for future misconduct."
        ),
    },
    {
        "year": 2022,
        "question": (
            "GS-IV Q10: You have done MBA from a reputed institution three years back but could not "
            "get campus placement due to COVID-19 generated recession. However, after a lot of "
            "persuasion and series of competitive tests including written and interview, you managed "
            "to get a job in a leading shoe company. You have aged parents who are dependent and "
            "staying with you. You also recently got married after getting this decent job. You were "
            "allotted the Inspection Section which is responsible for clearing the final product. In "
            "first one year, you learnt your job well and was appreciated for your performance by the "
            "management. The company is doing good business for last five years in domestic market and "
            "this year it is decided even to export to Europe and Gulf countries. However, one large "
            "consignment to Europe was rejected by their Inspecting Team due to certain poor quality "
            "and was sent back. The top management ordered that ibid consignment to be cleared for the "
            "domestic market. As a part of Inspecting Team, you observed the glaring poor quality and "
            "brought to the knowledge of the Team Commander. However, the top management advised all "
            "the members of the team to overlook these defects as the management cannot bear such a "
            "huge loss. Rest of the team members except you promptly signed and cleared the consignment "
            "for domestic market, overlooking glaring defects. You again brought to the knowledge of "
            "the Team Commander that such consignment, if cleared even for domestic market, will tarnish "
            "the image and reputation of the company and will be counter-productive in the long run. "
            "However, you were further advised by the top management that if you do not clear the "
            "consignment, the company will not hesitate to terminate your services citing certain "
            "innocuous reasons. (a) Under the given conditions, what are the options available to you "
            "as a member of the Inspecting Team? (b) Critically evaluate each of the options listed by "
            "you. (c) What option would you adopt and why? (d) What are the ethical dilemmas being "
            "faced by you? (e) What can be the consequences of overlooking the observations raised by "
            "the Inspecting Team? (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Exact full case and all five demands verified against "
            "books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, "
            "pages 11-12. Topic 12 owns product safety and ethics in core operations; Topic 22 "
            "controls the full options-and-safeguards case architecture."
        ),
        "answer": (
            "The options are to sign the clearance; refuse without further action; resign; seek retesting and "
            "segregation; or refuse, document the defects and escalate through independent quality, compliance, "
            "board and regulatory channels. Stakeholders include domestic consumers, the company, employees, "
            "shareholders, regulators, colleagues and the officer's dependent family.\n\n"
            "Signing protects employment and avoids immediate loss but deceives consumers, applies a discriminatory "
            "double standard and creates injury, recall, liability and reputational risk. Silent refusal preserves "
            "personal integrity but may not stop sale. Immediate resignation may avoid complicity yet abandons the "
            "preventive role. Escalation risks retaliation but best joins safety with institutional correction.\n\n"
            "I would refuse to certify, state the technical grounds in writing, preserve test records and seek an "
            "independent reinspection. Sale should be held pending a competent decision. I would use protected internal "
            "channels and, if management persists in unlawful or dangerous sale, report to the competent regulator. "
            "The goods may be reworked, downgraded only for a genuinely safe disclosed use, or destroyed; they cannot "
            "be passed to Indian consumers merely because export failed.\n\n"
            "The dilemmas are livelihood versus integrity, loyalty versus consumer safety, hierarchy versus professional "
            "duty and short-term loss versus long-term trust. Overlooking defects can cause harm, discriminatory treatment, "
            "regulatory sanction, litigation, demoralised staff and collapse of reputation. A reasoned, evidence-based "
            "refusal with escalation is therefore proportionate and professionally defensible. Retaliation should be "
            "documented, challenged through available employment remedies and disclosed to the regulator where relevant."
        ),
    },
    {
        "year": 2023,
        "question": (
            "GS-IV Q1(a): What do you understand by 'moral integrity' and 'professional efficiency' "
            "in the context of corporate governance in India? Illustrate with suitable examples. "
            "(Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, "
            "page 2. Topic 12 is the direct corporate-governance owner."
        ),
        "answer": (
            "Moral integrity is consistency between professed values and corporate decisions, especially when concealment "
            "or private benefit is tempting. Professional efficiency is competent, timely and economical achievement of "
            "legitimate organisational purposes. Good governance requires both: integrity without competence may waste "
            "stakeholder resources, while efficiency without integrity can make fraud, unsafe production or greenwashing "
            "more effective.\n\n"
            "A procurement director demonstrates integrity by disclosing that a sibling is a bidder and recusing; the "
            "independent committee demonstrates efficiency by using clear specifications, competitive timelines and "
            "quality-based evaluation. An audit committee that detects a related-party manipulation, secures records and "
            "orders correction similarly combines truthfulness with institutional competence.\n\n"
            "The two values reinforce each other when boards align incentives with long-term stakeholder outcomes, protect "
            "internal reporters and require reliable disclosure. Yet procedure should remain proportionate: remote interests "
            "need not paralyse every decision. Corporate governance becomes ethical when honest purpose is translated into "
            "capable systems, reviewable decisions and safe, lawful performance."
        ),
    },
    {
        "year": 2023,
        "question": (
            "GS-IV Q1(b): 'International aid' is an accepted form of helping 'resource-challenged' "
            "nations. Comment on 'ethics in contemporary international aid'. Support your answer "
            "with suitable examples. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, "
            "page 2. Topic 12 owns international aid ethics."
        ),
        "answer": (
            "International aid expresses solidarity and can protect life, health and development capabilities where domestic "
            "resources are inadequate. Its ethics, however, depends on design. Recipient ownership requires local institutions "
            "and communities to shape priorities; otherwise assistance becomes paternalistic. Conditions may safeguard rights "
            "and honest use, but unrelated commercial or geopolitical demands compromise sovereignty.\n\n"
            "Accountability is dual: donors must disburse predictably, avoid tied procurement and disclose interests; recipients "
            "must prevent diversion and report results. Food aid that permanently undercuts local farmers can create dependency, "
            "whereas time-bound nutrition support linked to local procurement and agricultural capacity protects immediate life "
            "while building autonomy. Humanitarian relief should follow need, neutrality and impartiality rather than political "
            "alignment.\n\n"
            "Aid is therefore ethical when it is transparent, participatory, proportionate, corruption-resistant and designed "
            "for durable local capacity and an exit path. Neither donor control nor recipient sovereignty is absolute: legitimate "
            "conditions must be connected to the aid's purpose and jointly reviewable."
        ),
    },
    {
        "year": 2024,
        "question": (
            "GS-IV Q10: Sneha is a Senior Manager working for a big (reputed) hospital chain in a "
            "mid-sized city. She has been made in-charge of the new super speciality center that "
            "the hospital is building with state-of-the-art equipment and world class medical "
            "facilities. The building has been reconstructed and she is starting the process of "
            "procurement for various equipment and machines. As the head of the committee responsible "
            "for procurement, she has invited bids from all the interested reputed vendors dealing "
            "in medical equipment. She notices that her brother, who is a well-known supplier in this "
            "domain, has also sent his expression of interest. Since the hospital is privately owned, "
            "it is not mandatory for her to select only the lower bidder. Also, she is aware that her "
            "brother's company has been facing some financial difficulties and a big supply order will "
            "help him recover. At the same time, allocating the contract to her brother might bring "
            "charges of favouritism against her and tarnish her image. The hospital management trusts "
            "her fully and would support any decision of hers. (a) What should be Sneha's course of "
            "action? (b) How would she justify what she chooses to do? (c) In this case, how is "
            "medical ethics compromised with vested personal interest? (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Full official facts and all three demands verified against "
            "books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, page 8. Topic 12 is the "
            "strong corporate/private-institution owner; Topics 09, 16 and 22 cross-link conflict "
            "management and case method."
        ),
        "answer": (
            "Sneha should immediately disclose the relationship in writing and recuse from screening, scoring, negotiation "
            "and award. The hospital should appoint an independent committee member or external expert, preserve the brother's "
            "eligibility if rules permit, and evaluate all bids against pre-declared criteria: patient safety, clinical need, "
            "quality certification, lifecycle cost, service support and financial value. The process and reasons should be "
            "documented and auditable.\n\n"
            "Awarding directly to her brother may help a financially stressed family business and a good supplier need not be "
            "excluded solely because of kinship. Yet Sneha's participation creates actual conflict and a reasonable appearance "
            "of favouritism. Rejecting him automatically could also be unfair. Recusal is therefore proportionate: it protects "
            "competition without prejudging the bid. Management trust is not a substitute for governance safeguards.\n\n"
            "Medical ethics is compromised when personal interest affects procurement because equipment quality, continuity "
            "and value directly shape patient safety, access and professional care. Beneficence and non-maleficence require "
            "reliable equipment; justice requires fair allocation of hospital resources; fidelity requires placing patients "
            "before family advantage. A hidden conflict can also weaken staff confidence and invite inflated prices or poor service.\n\n"
            "Sneha should justify her course as protection of both substance and appearance of integrity. If the brother wins "
            "through an independent process, the award is defensible; if he loses, family hardship cannot override patient and "
            "institutional duties. Future procurement policy should mandate interest registers, recusal and independent review."
        ),
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q2(a): Carl von Clausewitz once said, \"War is a diplomacy by other means.\" "
            "Critically analyse the above statement in the present context of contemporary "
            "geo-political conflict. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated Q2(a) verified against "
            "books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, page 2. Q2(b) on environmental "
            "clearance in sensitive border areas belongs to Topic 13 and is not reproduced here."
        ),
        "answer": (
            "Clausewitz's proposition explains war as organised force serving political purpose rather than violence wholly "
            "separate from statecraft. Contemporary conflicts confirm that territory, deterrence, alliances and bargaining "
            "objectives shape military action. Yet describing war as diplomacy can normalise coercion and obscure the moral "
            "change created when persuasion becomes lethal force.\n\n"
            "Ethically, policy purpose cannot remove the UN Charter concern for sovereignty or the jus ad bellum tests of "
            "legitimate authority, necessity, last resort and proportionality. Once conflict begins, jus in bello independently "
            "requires distinction, precautions and proportionality; civilians cannot become instruments for negotiation. "
            "Nuclear risk, autonomous systems, information warfare, displacement and attacks affecting food or energy networks "
            "make escalation increasingly difficult to control.\n\n"
            "The statement is therefore descriptively powerful but normatively incomplete. Responsible statecraft keeps "
            "diplomatic channels open, defines limited objectives, protects neutral humanitarian access and continually tests "
            "whether force still offers a just and proportionate route to peace. War may pursue policy, but ethics and law must "
            "discipline both the purpose and the means."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Distinguish corporate governance, core-business ethics and Corporate Social Responsibility. "
            "Why does conflating them encourage compliance theatre?"
        ),
        "answer": (
            "Corporate governance is the architecture by which a company is directed and controlled: board oversight, "
            "audit, disclosure, conflict management and review of related-party transactions. Core-business ethics concerns "
            "how profit is earned through accounting, labour, procurement, product safety, non-bribery and environmental "
            "conduct. CSR under Companies Act, 2013, s.135 is a statutory, ring-fenced expenditure and transfer regime for "
            "qualifying companies.\n\n"
            "Conflation enables compliance theatre. A company may publicise a school project while concealing emissions or "
            "selling unsafe products; it may spend two percent yet retain a promoter-dominated board that ignores conflicts. "
            "ARC's shift from bolt-on 'business ethics' to 'ethics in business' therefore places integrity inside everyday "
            "commercial choices.\n\n"
            "The three layers should reinforce one another: governance structures detect and correct misconduct, core ethics "
            "sets the operational standard, and CSR contributes separately to social development. CSR is neither optional "
            "charity once the statutory trigger applies nor a moral offset for harmful operations. A credible ethical company "
            "must satisfy all three tests."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Explain why international anti-corruption architecture should be understood as layered rather than singular."
        ),
        "answer": (
            "International anti-corruption mechanisms differ in legal source, actors and enforcement logic. UNCAC is a "
            "multilateral treaty binding States Parties through prevention, criminalisation, cooperation and asset-recovery "
            "commitments; India ratified it in 2011. The ADB-OECD Action Plan is a regional cooperative and non-binding "
            "framework endorsed by India, distinct from the OECD Anti-Bribery Convention, to which India is not a party.\n\n"
            "World Bank conditions use financing leverage by withholding or structuring support where projects are tainted "
            "by corruption. The United States FCPA uses domestic law with extraterritorial reach, combining anti-bribery "
            "prohibitions with issuer books-and-records and internal-control duties. These mechanisms may reinforce one another "
            "but are not interchangeable.\n\n"
            "A layered answer prevents overclaiming. Treaty membership does not itself guarantee domestic enforcement; peer "
            "cooperation does not create Convention-party status; lender conditions can protect funds yet raise ownership "
            "concerns; and foreign statutes depend on jurisdictional links. Effective integrity therefore requires domestic "
            "implementation joined to precise international cooperation."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Critically examine India's statutory CSR architecture as a social-spend floor and assess its capacity "
            "to prevent greenwashing."
        ),
        "answer": (
            "Companies Act, 2013, s.135 applies when any one immediately preceding-year threshold is met: net worth of "
            "at least Rs 500 crore, turnover of at least Rs 1,000 crore, or net profit of at least Rs 5 crore. The minimum "
            "spend is two percent of average net profits of the three preceding financial years on Schedule VII activities.\n\n"
            "The 2019 amendment created the statutory unspent architecture: non-ongoing amounts move to a specified fund "
            "within six months, while ongoing-project amounts enter an Unspent CSR Account within thirty days and must be "
            "used through the three-year route. The 2021 rules operationalised ongoing projects, implementing-agency "
            "registration and independent impact assessment for companies with average CSR obligation of at least Rs 10 "
            "crore and qualifying completed projects. The 2022 amendment revised assessment-cost limits to two percent of "
            "annual CSR expenditure or Rs 50 lakh, whichever is higher.\n\n"
            "These controls improve discipline and outcome scrutiny, but cannot prevent greenwashing alone. Spending may be "
            "highly visible yet unrelated to community priorities, while harmful core operations continue. Board disclosure "
            "may become formalistic and smaller projects may escape impact assessment.\n\n"
            "CSR is therefore an enforceable social-spend floor, not proof of ethical business. Preventing greenwashing also "
            "requires stakeholder participation, reliable impact evidence, environmental and labour compliance, honest "
            "disclosure and board accountability for the company's core conduct."
        ),
    },
    {
        "marks": 15,
        "question": (
            "International aid must reconcile ownership, conditionality, dependency and dual accountability. Discuss "
            "with suitable examples."
        ),
        "answer": (
            "International aid is ethically justified by solidarity and the urgent protection of life and development "
            "capabilities. Yet recipient ownership requires national institutions and affected communities to lead priorities. "
            "A donor-designed health programme that ignores local disease patterns may be well funded but ethically paternalistic.\n\n"
            "Conditionality can protect funds, human rights and reform, but unrelated commercial concessions or imposed policy "
            "templates compromise sovereignty. Conditions are strongest when transparent, proportionate, connected to the "
            "programme and jointly reviewable. Accountability is dual: donors must disclose interests, avoid tied procurement "
            "and deliver predictably; recipients must prevent diversion, publish use and permit independent scrutiny.\n\n"
            "Dependency is the temporal risk. Repeated imported food aid may undercut local farmers and revenue mobilisation, "
            "whereas emergency nutrition linked to local procurement, storage and agricultural capacity meets immediate need "
            "while building autonomy. Humanitarian relief should remain neutral and impartial so access is not conditioned on "
            "political allegiance.\n\n"
            "The balanced design is recipient-led, corruption-resistant and capacity-building, with feedback, grievance channels "
            "and an exit path. Ownership cannot shield diversion, while accountability cannot become indefinite donor control. "
            "Ethical aid enlarges local agency rather than replacing it."
        ),
    },
    {
        "marks": 20,
        "question": (
            "An Indian listed company is offered confidential technical and price data belonging to a rival bidder "
            "for a strategic public contract. Accepting it may save a division and thousands of jobs. As the board's "
            "independent ethics adviser, recommend a course of action."
        ),
        "answer": (
            "The stakeholders are employees and their families, shareholders, the rival bidder, public procuring authority, "
            "taxpayers, national-security institutions, the person offering the data and the board. The core issues are theft "
            "or misuse of confidential information, unfair competition, possible bribery through employment or payment, "
            "board oversight, livelihood pressure and long-term institutional trust.\n\n"
            "The company could accept and exploit the data; reject it silently; contact the rival informally; or refuse, "
            "preserve the approach and report through competent channels. Acceptance offers immediate commercial benefit "
            "but corrupts procurement, creates blackmail and legal exposure, and makes job preservation dependent on fraud. "
            "Silent rejection avoids direct use but leaves possible compromise of a strategic tender unaddressed. Informal "
            "contact risks leakage and evidence contamination.\n\n"
            "I would advise the board to prohibit access and copying, record the approach, preserve only lawfully held evidence "
            "and obtain independent legal and compliance guidance. The implicated recruitment or consultancy process should be "
            "paused. A secure report should go to the competent procurement-integrity authority, with disclosure limited to "
            "what is necessary. The company must submit only its independently prepared bid.\n\n"
            "To protect employees, management should develop lawful restructuring, redeployment and new-market options rather "
            "than invoke them as moral hostages. The board should investigate incentive failures, strengthen conflict and "
            "confidential-information controls, protect good-faith reporters and monitor retaliation.\n\n"
            "The recommendation joins deontological respect for fair rules, consequential protection of procurement and virtue "
            "integrity. Residual risks include retaliation, false accusation and tender delay; independent fact-finding, due "
            "process and restricted disclosure mitigate them."
        ),
    },
    {
        "marks": 20,
        "question": (
            "A humanitarian donor offers urgent climate-disaster assistance to an Indian Ocean island state but ties "
            "it to unrelated procurement preferences, exclusive access to strategic infrastructure and donor control "
            "over beneficiary data. Evaluate the options and propose an ethical aid compact."
        ),
        "answer": (
            "The immediate duty is to save life, shelter displaced people and restore essential services. Stakeholders include "
            "affected residents, vulnerable minorities, the recipient government, local firms, donor taxpayers, humanitarian "
            "agencies and future citizens whose sovereignty and data rights may be impaired. The dilemmas are urgency versus "
            "informed choice, accountability versus domination, and short-term relief versus dependency.\n\n"
            "The recipient could accept all conditions, reject the package, seek alternative donors, or negotiate a separated "
            "compact. Unqualified acceptance accelerates relief but converts vulnerability into leverage, distorts procurement "
            "and exposes sensitive data. Rejection protects autonomy but may leave preventable suffering. Waiting solely for "
            "alternatives may be too slow.\n\n"
            "The ethical course is to accept or request immediate life-saving assistance under a time-bound humanitarian tranche "
            "separated from unrelated strategic concessions. Procurement conditions should be open, competitive and tied only "
            "to delivery integrity. Beneficiary data should be minimal, purpose-limited, secured and controlled under recipient "
            "law, with no exclusive donor access. A joint board including recipient institutions, local communities and "
            "independent auditors should publish funds and outcomes while protecting personal data.\n\n"
            "Longer-term support should follow recipient-owned recovery priorities, use local procurement where feasible, build "
            "administrative and climate resilience, and include an exit and handover plan. Complaints, anti-corruption review and "
            "periodic renegotiation should be available to both parties.\n\n"
            "This compact preserves dual accountability without treating sovereignty as immunity from scrutiny or aid as a licence "
            "for coercion. Neutrality, proportionality, transparency and local agency make solidarity ethically credible."
        ),
    },
)


def _panel(title, structural_type, nodes, verdict, answer_use):
    return {
        "title": title,
        "structural_type": structural_type,
        "nodes": nodes,
        "verdict": verdict,
        "answer_use": answer_use,
    }


ASCII_PANELS = (
    _panel(
        "1. Three layers of ethical enterprise",
        "three-layer-foundation",
        (
            "Ethics in business",
            "Everyday commercial means",
            "Corporate governance",
            "Board, audit and disclosure",
            "Core-operation integrity",
            "Safe and fair production",
            "Statutory CSR spend",
            "No moral offset",
        ),
        "Governance, core conduct and CSR are complementary but never interchangeable.",
        "Use to open CSR or corporate-governance answers.",
    ),
    _panel(
        "2. ARC integration test",
        "bolt-on-versus-embedded",
        (
            "Reject ethics as public relations",
            "Test pricing and procurement",
            "Test labour and product safety",
            "Test accounting and disclosure",
            "Give ethics board access",
            "Align incentives with integrity",
            "Protect internal challenge",
            "Audit real outcomes",
        ),
        "Ethics must govern profit-making decisions, not decorate them afterward.",
        "Use for the ARC ethics-in-business distinction.",
    ),
    _panel(
        "3. Corporate governance control chain",
        "board-control-chain",
        (
            "Define board responsibility",
            "Separate oversight and management",
            "Strengthen audit independence",
            "Disclose material information",
            "Record conflicts of interest",
            "Scrutinise related parties",
            "Protect whistleblowers",
            "Correct and report failure",
        ),
        "Structures matter because integrity needs authority, information and follow-up.",
        "Use for 2023 Q1(a) and governance reform.",
    ),
    _panel(
        "4. CSR statutory architecture",
        "threshold-to-impact-flow",
        (
            "Test any one threshold",
            "Apply two-percent formula",
            "Choose Schedule VII activity",
            "Approve and disclose policy",
            "Classify unspent amount",
            "Use correct transfer route",
            "Assess qualifying impact",
            "Separate spend from ethics",
        ),
        "CSR is a statutory floor for qualifying companies, not discretionary compliance.",
        "Use for 2022 Q6(b) and close-option facts.",
    ),
    _panel(
        "5. Unspent and impact chronology",
        "statute-rules-timeline",
        (
            "2013: s.135 framework",
            "2019: unspent architecture",
            "2021: provisions operational",
            "2021: ongoing project defined",
            "2021: CSR-1 registration",
            "2021: impact mandate",
            "2022: cost cap revised",
            "2026: bounded SSE route",
        ),
        "Keep statutory creation, rule-level operation and later amendment claims separate.",
        "Use to prevent CSR chronology errors.",
    ),
    _panel(
        "6. Stakeholder and shareholder test",
        "two-model-comparison",
        (
            "Identify owners' legitimate claim",
            "Protect long-term enterprise value",
            "Identify employee interests",
            "Protect consumer safety",
            "Include affected community",
            "Internalise environmental harm",
            "Consider future generations",
            "Give a weighted verdict",
        ),
        "Profit remains legitimate but is constrained by rights, harm and durable trust.",
        "Use for sustainability and product-safety cases.",
    ),
    _panel(
        "7. Serious fraud and whistleblowing",
        "institutional-evolution-map",
        (
            "Fragmented fraud investigation",
            "Naresh Chandra 2002 proposal",
            "SFIO set up in 2003",
            "Statutory basis in s.211",
            "Multidisciplinary investigation",
            "Bounded s.212 arrest power",
            "SOX s.806 civil remedy",
            "SOX s.1107 criminal offence",
        ),
        "Precision about institutions and remedies prevents attractive but false equivalence.",
        "Use in corporate-fraud and whistleblower answers.",
    ),
    _panel(
        "8. International anti-corruption layers",
        "four-logic-matrix",
        (
            "UNCAC treaty obligations",
            "India ratified in 2011",
            "ADB-OECD cooperative plan",
            "Not OECD Convention membership",
            "Lender financial conditions",
            "FCPA anti-bribery rules",
            "FCPA issuer accounting rules",
            "Domestic implementation needed",
        ),
        "Treaty, cooperation, lending and extraterritorial law use different logics.",
        "Use for global anti-corruption questions.",
    ),
    _panel(
        "9. International aid ethics",
        "balanced-aid-compact",
        (
            "Begin with human need",
            "Preserve recipient ownership",
            "Test donor conditionality",
            "Avoid tied advantage",
            "Create dual accountability",
            "Prevent diversion",
            "Reduce dependency",
            "Build capacity and exit",
        ),
        "Ethical aid enlarges local agency while retaining transparent use safeguards.",
        "Use for 2023 Q1(b).",
    ),
    _panel(
        "10. War and arms-transfer ethics",
        "force-and-transfer-test",
        (
            "Respect sovereignty",
            "Test lawful resort to force",
            "Distinguish civilians",
            "Apply proportionality",
            "Protect neutral aid",
            "Assess arms end use",
            "Check diversion risk",
            "Monitor and suspend misuse",
        ),
        "Strategic purpose never removes civilian-protection and foreseeable-harm duties.",
        "Use for 2020 Q8, 2022 Q5(a) and 2025 Q2(a).",
    ),
    _panel(
        "11. Private-institution dilemma route",
        "conflict-safety-decision-tree",
        (
            "State facts and stakeholders",
            "Identify conflict or safety floor",
            "Disclose material interest",
            "Recuse or refuse certification",
            "Preserve records",
            "Seek independent review",
            "Remedy affected persons",
            "Redesign incentives and controls",
        ),
        "Private ownership does not erase patient, consumer or fair-process duties.",
        "Use for Sneha, food and defective-product cases.",
    ),
    _panel(
        "12. Mains answer spine",
        "eight-step-answer-spine",
        (
            "Define the precise ethical layer",
            "State a qualified thesis",
            "Name the governing mechanism",
            "Use exact law or institution",
            "Apply an India-centric example",
            "Test the strongest limitation",
            "Propose verifiable safeguards",
            "Conclude with balanced duty",
        ),
        "High-scoring answers distinguish mechanisms before recommending an ethical balance.",
        "Use as the final theory and case-study checklist.",
    ),
)

CURRENT_ANCHOR = {
    "title": (
        "UNODC and UN Global Compact: updated An Anti-Corruption Ethics and Compliance "
        "Programme for Business: A Practical Guide, March 2026"
    ),
    "verified_facts": (
        "The March 2026 publication is a joint UNODC and UN Global Compact guide.",
        "It updates the original 2013 publication and presents a globally applicable standard for business anti-corruption ethics and compliance programmes.",
        "It provides concrete, actionable steps for companies of all sizes and includes tailored recommendations for small and medium-sized enterprises.",
        "Its transformational-governance lens goes beyond compliance and links integrity with environmental stewardship, human rights, gender, responsible technology and transparent, inclusive governance.",
        "It addresses emerging risks, including artificial intelligence and external shocks affecting business operations.",
        "It can serve as a benchmark when governments assess programme effectiveness for integrity incentives such as subsidies, licences, public procurement or export credits.",
    ),
    "administrative_link": (
        "⚠️ Corporate-governance use: the guide converts ARC's ethics-in-business insight into a "
        "current implementation architecture. Boards and governments should test whether integrity "
        "programmes alter incentives, risk assessment, reporting and remedy across core decisions, "
        "rather than count policies or training sessions alone."
    ),
    "limit": (
        "Do not present the guide as a treaty, binding domestic law, certification, automatic defence "
        "to liability or proof that a company is ethical. Its benchmark function does not displace "
        "Companies Act, SEBI, competition, labour, environmental, procurement or criminal-law duties."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://businessintegrity.unodc.org/bip/en/webstories/2026/new-practical-guide-launched-to-advance-global-anti-corruption--ethics-and-compliance-in-business.html",
    "https://businessintegrity.unodc.org/bip/uploads/documents/resources/An_Anti-Corruption_Ethics_and_Compliance_Programme_for_Business-_A_Practical_Guide.pdf",
)

SOURCE_CAVEAT = (
    "The corrected canonical Topic 12 Basic and Advanced owners, the official syllabus mapping and "
    "books\\ethics4.pdf control the doctrinal spine. Quote official PYQs only from the stated local "
    "GS-IV PDFs; routing ledgers establish ownership boundaries, not exact wording. Preserve ARC's "
    "ethics-in-business distinction: corporate governance structures, ethical core operations and CSR "
    "expenditure are separate layers. For qualifying companies CSR compliance is statutory, although "
    "lawful project choice remains; use the s.135 thresholds and two-percent formula exactly. Attribute "
    "the unspent architecture to the 2019 amendment and its operational detail to the 2021 rules; the "
    "2021 rules introduced the qualifying impact-assessment mandate, while the 2022 amendment revised "
    "the assessment-cost cap. The dated 27 May 2026 MCA CSR/SSE change is included only as a canonical, "
    "access-restricted supplementary fact: a Schedule VII route for eligible zero-coupon zero-principal "
    "instruments, capped at ten percent of annual CSR expenditure, with no change to s.135 thresholds or "
    "the two-percent base obligation. Keep shareholder and stakeholder models, agency problem, independent "
    "board/audit/disclosure/related-party controls and greenwashing explicit. SFIO was set up by Government "
    "Resolution in 2003 and has statutory basis under Companies Act, 2013, s.211; describe s.212(8) arrest "
    "power only with the material-based reason-to-believe condition. SOX s.806 is the civil remedy and "
    "s.1107 the criminal retaliation offence. FCPA includes anti-bribery and issuer accounting provisions. "
    "UNCAC binds States Parties; India signed on 9 December 2005 and ratified on 9 May 2011. The ADB-OECD "
    "Action Plan is distinct from the OECD Anti-Bribery Convention, to which India is not a party. Do not "
    "collapse treaty, cooperative, lender and extraterritorial mechanisms. Aid answers require ownership, "
    "conditionality, dependency and dual accountability. India is not party to the Refugee Convention or "
    "Protocol; use Article 21 carefully and treat Mohammad Salimullah as an interim order. War and arms "
    "answers should use sovereignty, distinction, proportionality, humanitarian neutrality and risk "
    "assessment without claiming India is an Arms Trade Treaty party. The 2024 technology-emissions case "
    "is Topic 13/22 primary and only a Topic 12 corporate-governance cross-link; the full 2024 Sneha case "
    "is the stronger Topic 12 private-institution anchor."
)

REGISTER_SUPPLEMENT = (
    "### THREE-LAYER CORPORATE ETHICS MAP\n\n"
    "- **Ethics in business:** ARC's preferred integration of integrity into ordinary commercial decisions; reject a bolt-on public-relations layer.\n"
    "- **Corporate governance:** board direction and control through audit, disclosure, conflict management, related-party scrutiny and accountability.\n"
    "- **Core-business ethics:** honest accounts, fair labour, safe products, non-bribery and environmental responsibility in profit-making operations.\n"
    "- **CSR:** statutory ring-fenced spend for qualifying companies; valuable but not a moral offset for unethical operations.\n\n"
    "### CSR DOCTRINE AND CHRONOLOGY\n\n"
    "- **Applicability:** immediately preceding financial year - net worth at least Rs 500 crore, or turnover at least Rs 1,000 crore, or net profit at least Rs 5 crore.\n"
    "- **Base obligation:** at least two percent of average net profits of the three immediately preceding financial years on Schedule VII activities.\n"
    "- **2019 architecture:** non-ongoing unspent amount to a specified fund within six months; ongoing amount to Unspent CSR Account within thirty days, then the three-year route.\n"
    "- **2021 Rules:** ongoing-project definition, CSR-1 implementing-agency registration and qualifying independent impact assessment.\n"
    "- **Impact trigger:** average CSR obligation at least Rs 10 crore in the three preceding years; qualifying project outlay at least Rs 1 crore and completion at least one year earlier.\n"
    "- **2022 cost cap:** impact-assessment expenditure may be two percent of total CSR expenditure for that year or Rs 50 lakh, whichever is higher.\n"
    "- **27 May 2026 bounded update:** Schedule VII route for eligible SSE zero-coupon zero-principal instruments, capped at ten percent of annual CSR expenditure; no threshold or two-percent change.\n\n"
    "### BOARD, FRAUD AND WHISTLEBLOWER CONTROLS\n\n"
    "- **Agency problem:** managers may pursue private or short-term interests where ownership and control are separated.\n"
    "- **Governance response:** independent oversight, audit quality, reliable disclosure, interest registers, recusal and related-party controls.\n"
    "- **SFIO:** Government Resolution, 2 July 2003; statutory footing under Companies Act, 2013, s.211; bounded arrest power under s.212(8).\n"
    "- **SOX:** s.806 is the civil whistleblower remedy; s.1107 created the criminal retaliation offence under 18 U.S.C. 1513(e).\n"
    "- **Greenwashing test:** compare public commitments and CSR claims with audited core-operation outcomes and time-bound corrective plans.\n\n"
    "### INTERNATIONAL ANTI-CORRUPTION ARCHITECTURE\n\n"
    "- **UNCAC:** adopted 31 October 2003; in force 14 December 2005; India signed 9 December 2005 and ratified 9 May 2011.\n"
    "- **ADB-OECD Action Plan:** regional cooperative framework endorsed by India on 30 November 2001; not the OECD Anti-Bribery Convention.\n"
    "- **OECD Anti-Bribery Convention:** India is not a party.\n"
    "- **World Bank logic:** lender leverage and project-integrity conditions, distinct from treaty obligation.\n"
    "- **FCPA:** anti-bribery rules plus issuer books-and-records and internal-accounting-control requirements; extraterritorial reach depends on statutory jurisdiction.\n\n"
    "### AID, REFUGEES, WAR AND ARMS\n\n"
    "- **Aid ethics:** recipient ownership + proportionate conditionality + anti-dependency design + donor and recipient accountability.\n"
    "- **Non-refoulement:** Refugee Convention Article 33; India is not party to the 1951 Convention or 1967 Protocol; add Article 21 and interim-order caution.\n"
    "- **War ethics:** jus ad bellum sovereignty and necessity; jus in bello distinction, precautions and proportionality; humanitarian neutrality protects access.\n"
    "- **Arms transfer:** assess end use, diversion, civilian harm, recipient record, regional stability and monitoring; do not claim Indian ATT membership.\n\n"
    "### PYQ AND ANSWER SPINE\n\n"
    "- **2020 Q8:** responsible arms export requires a documented foreseeable-harm and end-use assessment.\n"
    "- **2020 Q11:** APW is a qualified stakeholder-development model, not proof that CSR cures every operational risk.\n"
    "- **2021 Q5(a):** protect against return to persecution while preserving Indian treaty-status and interim-order caution.\n"
    "- **2021 Q11 and 2022 Q10:** Indian consumers cannot be treated as a lower safety class; refuse, test, recall, remedy and reform controls.\n"
    "- **2022 Q6(b):** CSR is efficient as a statutory floor but insufficient without ethical core operations.\n"
    "- **2022 Q7:** reject confidential rival data, preserve evidence, use competent channels and protect lawful competition.\n"
    "- **2023 Q1(a)/(b):** integrate integrity with competence; balance aid ownership, conditions, dependency and dual accountability.\n"
    "- **2024 Q10:** disclose and recuse; let an independent process assess the brother's bid against patient-centred criteria.\n"
    "- **2025 Q2(a):** Clausewitz is descriptively useful but normatively bounded by sovereignty, restraint and civilian protection.\n"
    "- **Answer method:** distinguish the ethical layer -> identify stakeholders and legal floor -> name the mechanism -> apply exact evidence -> test the strongest limitation -> propose verifiable safeguards -> conclude with a qualified duty."
)
