"""Learner-v2 source data: Ethics Topic 18, public funds and corruption."""


SESSION_TITLES = (
    "Public money as a fiduciary trust: concepts, boundaries and classifications",
    "From budget allocation to public outcome: economy, efficiency, effectiveness and equity",
    "Financial propriety, delegated authority and the control chain",
    "Procurement and contract integrity across the full lifecycle",
    "Leakage, diversion, bribery and abuse of discretion",
    "Conflicts, collusion, capture and the political-administrative-business nexus",
    "Audit and legislative accountability: CAG, PAC, internal audit and social audit",
    "Anti-corruption system design: prevent, detect, investigate, adjudicate and sanction",
    "Transparency, PFMS-style technology, citizen oversight and their limits",
    "Whistleblowing, reform synthesis, PYQ routing and answer architecture",
)


SESSION_GROUPS = (
    ("1",),
    ("2",),
    ("3",),
    ("4",),
    ("5",),
    ("6",),
    ("7",),
    ("8",),
    ("9",),
    ("10",),
)


def _mcq(label, statement, scenario_a, scenario_b, group):
    return {
        "label": label,
        "statement": statement,
        "scenario_a": scenario_a,
        "scenario_b": scenario_b,
        "group": group,
    }


MCQ_ITEMS = (
    _mcq(
        "Public money is held in fiduciary trust",
        (
            "An official controls public money as a trustee for authorised public purposes, not as "
            "a private proprietor free to substitute personal, partisan or organisational convenience for law, "
            "fairness, value and the interests of intended beneficiaries."
        ),
        (
            "A district officer spends a grant on an impressive office renovation because the "
            "department saved the money, although the grant was sanctioned for drinking-water works. "
            "Which foundational ethical relationship is violated?"
        ),
        (
            "A sanctioning officer rejects a politically useful but unauthorised diversion and records "
            "that the money remains tied to its public purpose. Which stewardship principle is applied?"
        ),
        "public-trust distinctions",
    ),
    _mcq(
        "Allocation, release, expenditure, output and outcome are distinct",
        (
            "Budget allocation authorises an amount, release makes funds available, expenditure records "
            "payment, output records the immediate deliverable, and outcome asks whether the intended "
            "public condition improved; none of these stages proves the next."
        ),
        (
            "A ministry reports that its entire allocation was spent but cannot show that clinics became "
            "functional. Which budget-to-outcome distinction prevents equating expenditure with success?"
        ),
        (
            "A project has a valid sanction and timely release, yet procurement never starts. At which "
            "link has the chain failed before any output can arise?"
        ),
        "public-trust distinctions",
    ),
    _mcq(
        "Irregularity, waste, fraud, abuse and corruption must be separated",
        (
            "Irregularity is departure from a rule; waste is avoidable loss without necessary private gain; "
            "fraud uses intentional deception; abuse of discretion misuses entrusted choice; corruption "
            "adds improper private, partisan or connected advantage through public power."
        ),
        (
            "A clerk makes a curable coding error without deception, favour or loss. Why should an inquiry "
            "not automatically label the act fraud or corruption?"
        ),
        (
            "A committee knowingly certifies fictitious work so a connected contractor is paid. Which "
            "features move the case beyond mere irregularity?"
        ),
        "public-trust distinctions",
    ),
    _mcq(
        "Public loss may exist without private enrichment",
        (
            "Wasteful or ostentatious expenditure can injure the exchequer, opportunity cost and public "
            "trust even when no official pockets money; absence of personal enrichment therefore does not "
            "establish ethical propriety."
        ),
        (
            "A department buys luxury furnishings far beyond functional need through a fair tender and no "
            "one receives a kickback. Which category of public harm remains?"
        ),
        (
            "An auditor finds no private gain but documents avoidable expenditure that displaced essential "
            "maintenance. Why is the finding ethically significant?"
        ),
        "public-trust distinctions",
    ),
    _mcq(
        "Economy concerns the cost and quality of inputs",
        (
            "Economy means obtaining appropriate resources at the lowest defensible whole-life cost while "
            "preserving required quality, timeliness and fitness; choosing the cheapest defective input is "
            "false economy rather than stewardship."
        ),
        (
            "A hospital buys the lowest-priced equipment despite verified inability to meet safety "
            "specifications. Which value-for-money dimension has been misunderstood?"
        ),
        (
            "A department compares purchase price, maintenance, energy, training and disposal before award. "
            "Which financial-performance question is it answering?"
        ),
        "four-E outcome logic",
    ),
    _mcq(
        "Efficiency connects inputs to outputs",
        (
            "Efficiency asks whether a process produces the greatest suitable output from available "
            "resources, or the required output with fewer resources, without hiding deterioration in "
            "quality, legality, worker safety or access."
        ),
        (
            "Two districts spend equally, but one completes twice as many compliant inspections with the "
            "same staffing and quality. Which performance dimension distinguishes them?"
        ),
        (
            "A unit increases disposal numbers by rejecting applications without examination. Why is the "
            "reported efficiency ethically misleading?"
        ),
        "four-E outcome logic",
    ),
    _mcq(
        "Effectiveness tests achievement of intended results",
        (
            "Effectiveness asks whether the programme's stated objectives and outcomes were actually "
            "achieved for the target population; timely spending and abundant outputs may still be "
            "ineffective when they do not solve the identified public problem."
        ),
        (
            "A skills programme meets its training target, but participants cannot use the obsolete course "
            "for employment. Which value-for-money failure is central?"
        ),
        (
            "An audit compares the programme's objective with verified changes among intended beneficiaries. "
            "Which dimension is being examined?"
        ),
        "four-E outcome logic",
    ),
    _mcq(
        "Equity tests distribution, access and burden",
        (
            "Equity asks who receives benefits, bears cost and remains excluded; equal expenditure per unit "
            "can remain unjust where remoteness, disability, social disadvantage or unequal need requires "
            "differentiated access and support."
        ),
        (
            "A digital-only grant portal reduces processing cost but systematically excludes remote citizens "
            "without connectivity. Which fourth value must qualify the efficiency claim?"
        ),
        (
            "A health allocation gives additional outreach resources to difficult tribal areas after "
            "evidence of access barriers. Which distributive principle supports the design?"
        ),
        "four-E outcome logic",
    ),
    _mcq(
        "Competent sanction is an ethical control, not paperwork",
        (
            "Delegated financial powers assign decision authority by subject and value so that scrutiny "
            "matches risk; expenditure without competent sanction, or engineered to evade a higher level, "
            "defeats accountability even if the purchase appears useful."
        ),
        (
            "An officer approves a requirement beyond her delegated limit because delay seems inconvenient. "
            "Which institutional safeguard has she displaced?"
        ),
        (
            "A unit consolidates the total requirement and routes it to the authority empowered for that "
            "value. Which control logic is respected?"
        ),
        "financial-control chain",
    ),
    _mcq(
        "Segregation, verification and reconciliation reduce opportunity",
        (
            "No single actor should control need identification, vendor selection, receipt certification, "
            "payment and ledger reconciliation; proportionate separation and independent verification reduce "
            "error, concealment, coercion and collusive override."
        ),
        (
            "The same officer creates a vendor, confirms delivery and authorises payment without review. "
            "Which preventive control weakness is most obvious?"
        ),
        (
            "Stores, user unit, finance and bank records are periodically reconciled by persons outside the "
            "transaction chain. Which risk-control design is illustrated?"
        ),
        "financial-control chain",
    ),
    _mcq(
        "GFR Rule 157 is a goods-specific anti-splitting rule",
        (
            "General Financial Rules Rule 157 bars dividing a demand for goods into small quantities to avoid "
            "higher sanction; analogous splitting of works or services is still improper but must be tied to "
            "the applicable category rules and delegation framework."
        ),
        (
            "A candidate cites Rule 157 verbatim for a divided consultancy contract without checking the "
            "services framework. Which precision error has occurred?"
        ),
        (
            "One genuine stationery requirement is divided solely to stay below higher sanction. Which "
            "current goods-procurement rule states the controlling prohibition?"
        ),
        "financial-control chain",
    ),
    _mcq(
        "Re-appropriation cannot erase public purpose and consequences",
        (
            "Re-appropriation is a formally authorised transfer within the budget framework, but ethical "
            "review must still test competence, purpose, beneficiary impact, timing, alternatives, legislative "
            "answerability and whether a vulnerable programme is being sacrificed without reasons."
        ),
        (
            "A lawful budget transfer abruptly stalls housing for weaker sections although less harmful "
            "financing alternatives were not examined. What remains ethically reviewable?"
        ),
        (
            "A finance officer records distributional impact, explores staged funding and places the trade-off "
            "before the competent authority. Which responsible approach is shown?"
        ),
        "financial-control chain",
    ),
    _mcq(
        "Procurement integrity covers the whole lifecycle",
        (
            "Integrity begins with genuine need and realistic specifications, continues through fair market "
            "access, published criteria and reasoned award, and extends to delivery verification, variation, "
            "payment, asset use, maintenance, disposal and remedy."
        ),
        (
            "A clean bidding process is followed, but officials later accept inferior delivery and inflated "
            "change orders. Why is it wrong to call the procurement fully clean?"
        ),
        (
            "An audit traces planning, tender, award, execution, payment and disposal rather than examining "
            "only the lowest bid. Which conception is applied?"
        ),
        "procurement integrity",
    ),
    _mcq(
        "Conflict of interest is a managed risk before it becomes corruption",
        (
            "A conflict exists when a private or connected interest could improperly influence, or reasonably "
            "appear to influence, an official decision; timely disclosure, independent assessment, recusal or "
            "reassignment is required before proof of bribery."
        ),
        (
            "A procurement member's sibling controls a bidder, although no favour has yet been shown. Which "
            "ethical condition already exists?"
        ),
        (
            "The member declares the relationship and an independent authority reassigns evaluation. Which "
            "preventive response is demonstrated?"
        ),
        "procurement integrity",
    ),
    _mcq(
        "Collusion and cartels defeat apparent competition",
        (
            "Bid rotation, cover bids, market allocation, common beneficial ownership and coordinated "
            "withdrawals can make several tenders only formally competitive; detection requires pattern "
            "analysis, independent estimates, ownership checks and a credible challenge route."
        ),
        (
            "Three firms alternately win identical tenders while the others submit predictably high bids. "
            "Which risk should the buyer investigate?"
        ),
        (
            "A procurement unit compares bid patterns across years and checks connected ownership. Which hidden "
            "threat to competition is it testing?"
        ),
        "procurement integrity",
    ),
    _mcq(
        "Contract management can reverse a fair award",
        (
            "Post-award corruption may operate through unjustified variations, weak measurement, false "
            "completion, delayed penalties, concealed subcontracting or premature payment; independent "
            "verification and recorded change control protect the original competitive result."
        ),
        (
            "A contractor wins fairly and later doubles the value through poorly justified variations approved "
            "by one officer. Which stage now carries the main integrity risk?"
        ),
        (
            "Technical staff verify milestones independently before finance releases payment. Which "
            "post-award safeguard is operating?"
        ),
        "procurement integrity",
    ),
    _mcq(
        "Coercive and collusive bribery require different responses",
        (
            "Coercive bribery extorts a citizen seeking a lawful entitlement, while collusive bribery benefits "
            "giver and taker at public cost; the first needs victim protection and service restoration, the "
            "second demands scrutiny of both sides and the underlying transaction."
        ),
        (
            "An official demands money before issuing a certificate already due to an eligible citizen. Which "
            "bribery pattern and response priority apply?"
        ),
        (
            "A contractor pays an engineer to certify substandard work so both benefit. Which form of bribery "
            "is illustrated?"
        ),
        "corruption and capture",
    ),
    _mcq(
        "Regulatory capture can occur without an envelope of cash",
        (
            "Regulatory capture arises when a regulator persistently serves the regulated sector's interests "
            "through dependence, information imbalance, revolving-door incentives, access or shared worldview, "
            "displacing the statutory public purpose even without proved bribery."
        ),
        (
            "A regulator relies exclusively on industry data, meets only major firms and designs enforcement "
            "around their convenience. Which structural corruption risk appears?"
        ),
        (
            "Independent research capacity, balanced consultation and cooling-off controls are strengthened. "
            "Which risk are these measures intended to reduce?"
        ),
        "corruption and capture",
    ),
    _mcq(
        "State capture reshapes rules, not merely individual decisions",
        (
            "State capture occurs when powerful interests influence laws, policies, appointments or enforcement "
            "architecture for durable private advantage; it is deeper than petty bribery because the rules of "
            "allocation and accountability themselves are altered."
        ),
        (
            "A business-political network secures weak eligibility rules, compliant appointments and selective "
            "non-enforcement across a sector. Which level of corruption is indicated?"
        ),
        (
            "Why is replacing one bribed inspector insufficient when the governing rules and appointments have "
            "already been shaped by connected interests?"
        ),
        "corruption and capture",
    ),
    _mcq(
        "Whistleblowing needs protected, proportionate and evidence-preserving routes",
        (
            "A responsible whistleblower preserves reliable evidence, uses authorised independent channels "
            "where reasonably safe, limits disclosure to the wrongdoing, protects unrelated persons and receives "
            "confidentiality, anti-retaliation, feedback and escalation safeguards."
        ),
        (
            "An employee reports forged bills through a protected channel and withholds unrelated beneficiary "
            "data. Which ethical reporting design is shown?"
        ),
        (
            "A complainant posts an entire database online without testing evidence or protecting citizens. "
            "Which whistleblowing limit has been ignored?"
        ),
        "corruption and capture",
    ),
    _mcq(
        "Prevention and detection are different control functions",
        (
            "Prevention reduces opportunity and motive before loss through design, while detection discovers "
            "possible deviation through reconciliation, audit trails, complaints, analytics or inspection; a "
            "control may contribute to both but the objectives remain distinct."
        ),
        (
            "Vendor-role separation is introduced before transactions occur. Is its primary function prevention "
            "or proof of an existing offence?"
        ),
        (
            "Exception analytics flags repeated round-number payments after they occur. Which system stage is "
            "primarily operating?"
        ),
        "accountability stages",
    ),
    _mcq(
        "Investigation, adjudication and sanction must not be collapsed",
        (
            "Investigation gathers and tests evidence, adjudication determines responsibility through the "
            "competent fair process, and sanction imposes the authorised consequence; suspicion, audit finding "
            "or investigative allegation is not itself a final determination."
        ),
        (
            "A department dismisses an employee solely because an audit paragraph raised suspicion. Which "
            "accountability stages and fairness protections were skipped?"
        ),
        (
            "Evidence is independently examined, the affected person is heard, reasons are recorded and a "
            "proportionate penalty follows. Which complete sequence is respected?"
        ),
        "accountability stages",
    ),
    _mcq(
        "Audit forms are complementary, not interchangeable",
        (
            "Internal audit supports management control, CAG audit supplies constitutionally grounded external "
            "scrutiny, legislative committees examine executive accountability, and social audit enables "
            "citizen verification of records against lived delivery; each has a different forum and remedy path."
        ),
        (
            "A village hearing compares muster rolls with workers and completed assets. Which form of scrutiny "
            "is operating, and why does it not replace CAG?"
        ),
        (
            "A legislative committee examines an audit report and calls the executive to explain deviations. "
            "Which accountability bridge is illustrated?"
        ),
        "accountability stages",
    ),
    _mcq(
        "Technology strengthens traceability but does not prove integrity",
        (
            "Digital payments, e-procurement and transaction logs can reduce cash handling and improve "
            "traceability, yet biased specifications, false data, shared credentials, collusive vendors, "
            "exclusion and unreviewed algorithms can digitise rather than eliminate corruption."
        ),
        (
            "A dashboard shows every payment as timely, but field verification finds ghost beneficiaries. Which "
            "limit of technological transparency is exposed?"
        ),
        (
            "An e-procurement system combines open access, tamper-evident logs, ownership checks, appeal and "
            "independent verification. Which balanced design is demonstrated?"
        ),
        "accountability stages",
    ),
)


def _pyq(year, question, marks, source_note, answer):
    return {
        "year": year,
        "question": question,
        "marks": marks,
        "source_note": source_note,
        "answer": answer,
    }


PYQS = (
    _pyq(
        2018,
        (
            "Neutral routing of GS-IV Q8: a senior Ministry officer is pressed by a Minister to "
            "realign a proposed road near the Minister's farmhouse and is offered assistance to buy "
            "nearby land in the officer's wife's name. The change would increase acquisition, "
            "displacement, fiscal cost and tree loss. What should the officer do, what conflicts of "
            "interest arise, and what are the officer's responsibilities? (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\more_previous_papers\\"
            "GENERAL-STUDIES-PAPER-IV.pdf, page 7. The original full case remains in the official "
            "paper; Topic 18 uses it for public-cost, conflict and capture analysis, while Topic 22 "
            "owns the complete case-study method."
        ),
        (
            "The officer faces misuse of advance policy information, ministerial pressure, a proposed "
            "benefit through the spouse, conflict between career obedience and constitutional duty, "
            "avoidable fiscal burden, farmer displacement and environmental loss. The offer is not cured "
            "because land would be purchased at the prevailing price: privileged timing and policy "
            "realignment create connected private advantage.\n\n"
            "The officer should refuse the benefit and disclose the conflict. The original technical "
            "alignment, acquisition estimate and environmental assessment should be preserved. Any change "
            "must return to the competent multidisciplinary process, use published criteria and record the "
            "incremental cost, displacement and ecological consequences. The Minister's direction should be "
            "requested in writing; an unlawful or extraneous direction should be escalated through the "
            "authorised administrative and vigilance route. Confidential information must not be used for "
            "private purchase.\n\n"
            "Public money is held in trust. Responsiveness to the political executive does not permit a "
            "project to be reshaped for connected enrichment. Independent technical review, conflict "
            "management and a durable audit trail protect both democratic authority and the officer."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Q2(a): Effective utilization of public funds is crucial to meet development "
            "goals. Critically examine the reasons for under-utilization and mis-utilization of "
            "public funds and their implications. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 2. This is Topic 18's direct historical PYQ."
        ),
        (
            "Under-utilisation means authorised money is not converted into timely activity or output; "
            "mis-utilisation means it is spent for an unauthorised, wasteful, diverted or corrupt purpose. "
            "Causes include unrealistic budgeting, late release, weak project preparation, land or approval "
            "delay, poor capacity, fragmented responsibility and fear-driven decision paralysis. Misuse "
            "additionally arises from opaque procurement, tailored specifications, collusion, weak receipt "
            "verification, political diversion, false beneficiaries and poor contract management.\n\n"
            "The implications extend beyond accounting. Idle funds postpone rights and infrastructure; rushed "
            "year-end spending weakens value for money. Diversion and leakage impose opportunity cost on "
            "vulnerable citizens, distort competition, reduce service quality and erode tax morale and trust. "
            "A high expenditure ratio may therefore coexist with ineffective or inequitable delivery.\n\n"
            "Reform requires credible plans, milestone-linked release, competent sanction, e-procurement, "
            "segregation of duties, real-time but verified transaction trails, CAG/internal/social audit, "
            "speaking explanations for variance and consequence after fair inquiry. Utilisation should be "
            "judged from allocation to outcome, not by spending alone."
        ),
    ),
    _pyq(
        2019,
        (
            'GS-IV Q2(b): "Non-performance of duty by a public servant is a form of corruption". '
            "Do you agree with this view? Justify your answer. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 2. Topic 18 addresses wilful omission and public "
            "loss; Topic 19 owns the precise criminal-law boundary."
        ),
        (
            "I agree conditionally. Public office carries a duty to use authority and resources for the "
            "authorised public purpose. Wilful inaction can function like active corruption when an officer "
            "delays a lawful service to extract payment, ignores collusive overbilling, permits a connected "
            "contractor to default or deliberately leaves funds idle for partisan advantage. The citizen "
            "loses entitlement and the wrongdoer gains protection even without a visible cash transfer.\n\n"
            "However, every poor result is not corruption. Delay may arise from inadequate staff, conflicting "
            "law, genuine uncertainty or a good-faith decision that later fails. These may require capacity "
            "repair, not stigma or punishment. The correct test asks whether duty was clear, the officer had "
            "capacity and knowledge, the omission was wilful or grossly negligent, an improper advantage or "
            "foreseeable public harm followed, and reasons were concealed.\n\n"
            "Thus non-performance is ethically corrupt when it is a deliberate abuse of entrusted office; "
            "legal liability still depends on the ingredients and process of the applicable law."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Section B concluding question: India seeks effective civil-service ethics, codes "
            "of conduct, transparency measures, ethics and integrity systems and anti-corruption "
            "agencies. Suggest institutional measures for anticipating threats, strengthening ethical "
            "competence and developing processes that promote integrity. (250 words)"
        ),
        20,
        (
            "Faithful condensed routing of the English demand verified against books\\"
            "more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, page 7. The official paper contains "
            "the complete enumerated stem. Topic 18 uses the corruption-system component; Topics 16 "
            "and 20 retain primary ownership of codes and institutional jurisdiction."
        ),
        (
            "The three tasks require a linked integrity system. To anticipate threats, every department "
            "should map high-discretion and high-value processes such as procurement, licensing, transfers, "
            "inspection and grants. Complaint patterns, audit findings, vendor concentration, repeated "
            "single bids, split purchases and staff surveys can reveal emerging risk. Sensitive functions "
            "need role separation, rotation where appropriate and conflict declarations.\n\n"
            "Ethical competence requires scenario-based training in public trust, financial propriety, "
            "conflict management, written reasons, lawful dissent and evidence preservation. Confidential "
            "advice, mentoring and leadership example should make early consultation safe. Performance "
            "systems must not reward target achievement through hidden shortcuts.\n\n"
            "Processes should combine prevention, detection and fair enforcement: published criteria, "
            "e-procurement, beneficial-ownership checks, milestone verification, transaction trails, "
            "reconciliation, protected reporting, independent audit and time-bound complaint handling. "
            "Investigation must be separated from adjudication; sanctions require proof, hearing, reasons "
            "and proportionality. Aggregate reporting should show action and recurring system failures.\n\n"
            "Technology cannot replace field verification or institutional independence. Integrity becomes "
            "durable when incentives, competence, controls, citizen oversight and fair consequence reinforce "
            "one another."
        ),
    ),
    _pyq(
        2020,
        (
            "Neutral routing of GS-IV Q7: Finance Ministry officer Rajesh Kumar must assess a proposed "
            "re-appropriation from a social-housing allocation to an SEZ and a gas-processing project. "
            "Discuss the ethical issues, options for proper utilisation of public funds and whether "
            "resignation is a worthy option. (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\more_previous_papers\\Gen_St_P4.pdf, "
            "pages 4-5. The printed case amounts and project details remain in the official paper; "
            "Topic 22 owns complete case architecture."
        ),
        (
            "The case is not a simple choice between welfare and development. It raises legality of "
            "re-appropriation, distributive justice for weaker sections, contractual and national-interest "
            "costs of delay, electoral timing, parliamentary accountability, sunk preparation and the "
            "officer's duty to give candid advice. Formal power to transfer money does not remove the need "
            "to examine who bears the loss.\n\n"
            "Rajesh should verify the budget and delegation rules, the actual pace and bottlenecks of the "
            "housing scheme, payment obligations, alternative financing, phased release and the minimum "
            "amount needed to avoid irreversible harm in each project. He should present options with "
            "distributional, fiscal and legal consequences, record dissent where necessary and seek a "
            "reasoned decision from the competent authority. Parliament must not be misled about the effect "
            "on the welfare allocation.\n\n"
            "Automatic refusal may ignore urgent public loss, while mechanical compliance abandons stewardship. "
            "Resignation is not the first response because it removes the officer's capacity to create a "
            "record and improve the decision. It becomes defensible only if a clearly unlawful diversion is "
            "insisted upon after authorised review and continued service would require complicity."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-IV Q6(a): An independent and empowered social audit mechanism is an absolute must "
            "in every sphere of public service, including judiciary, to ensure performance, "
            "accountability and ethical conduct. Elaborate. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 3. Topic 11 is the general "
            "accountability owner; Topic 18 applies it to public money and leakage."
        ),
        (
            "Social audit lets affected citizens compare official records with actual delivery. Muster rolls, "
            "beneficiary lists, sanctioned works, measurements and payments can be tested through field "
            "verification and public hearing, exposing ghost entries, exclusion, inflated quantities and "
            "assets that exist only on paper. It supplements professional audit with local knowledge and "
            "gives vulnerable beneficiaries a forum to speak.\n\n"
            "Independence requires separation from the implementing unit, timely access to intelligible records, "
            "trained facilitation, protection against intimidation and public action-taken reports. Empowerment "
            "requires correction of records, payment of dues, recovery or disciplinary referral where evidence "
            "supports it, and reasoned rejection of unsupported allegations.\n\n"
            "The phrase 'every sphere' needs functional adaptation. Citizen scrutiny of court administration "
            "and expenditure cannot become popular review of judicial merits; privacy, decisional independence "
            "and lawful appeal remain. Social audit does not replace CAG, internal audit or courts. Its ethical "
            "value is converting fiscal visibility into participatory verification and enforceable follow-up."
        ),
    ),
    _pyq(
        2022,
        (
            "Neutral routing of GS-IV Q10: an investigative journalist uncovers a stone-mining mafia "
            "working with corrupt police, civil officials and a politically connected media owner, but "
            "faces inducement and pressure to suppress the report. Evaluate options, dilemmas and the "
            "most appropriate response. (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 10. Topic 18 uses the "
            "state-capture and nexus dimension; Topic 22 owns complete option analysis."
        ),
        (
            "The case shows organised corruption rather than an isolated bribe: illegal extraction, official "
            "protection, political influence, media ownership and personal inducement reinforce one another. "
            "The dilemmas are truth versus employment and family need, source and personal safety, public "
            "interest versus reckless disclosure, and loyalty to employer versus professional integrity.\n\n"
            "Immediate publication without verification may endanger sources and the investigation. Silent "
            "surrender makes the journalist complicit. He should preserve authenticated copies and a chronology; "
            "seek legal and editorial review outside the conflicted chain; protect source identities; and use "
            "credible law-enforcement, judicial or independent oversight channels. If internal routes are "
            "captured, proportionate external disclosure through a reputable platform may be justified after "
            "risk assessment. The financial inducement must be refused and documented.\n\n"
            "For administration, reform must attack the network: rotate and scrutinise sensitive posts, use "
            "remote sensing and transport records, reconcile permits and royalty, protect complainants, disclose "
            "beneficial interests, and investigate money and decision trails. Individual arrests alone fail "
            "where appointments, enforcement and information channels remain captured."
        ),
    ),
    _pyq(
        2023,
        (
            'GS-IV Q2(a): "Corruption is the manifestation of the failure of core values in the '
            'society." In your opinion, what measures can be adopted to uplift the core values in '
            "the society? (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, page 2. Topic 18 addresses "
            "the corruption mechanism; Topics 1 and 2 own general value formation."
        ),
        (
            "Corruption reflects weakened honesty, fairness, responsibility, empathy and respect for public "
            "goods, but values do not fail in a vacuum. When opaque discretion, scarcity, impunity and social "
            "admiration of illicit wealth reward misconduct, decent individuals face pressure to conform.\n\n"
            "Value uplift therefore needs family and school modelling of honesty, civic education about shared "
            "resources, ethical leadership, professional training and public recognition of clean service. "
            "Institutions must make values practicable through simple entitlements, published criteria, fair "
            "pay and workload, conflict controls, e-procurement, protected reporting, independent audit and "
            "swift but fair consequence. Citizens coerced into paying for lawful services need protection and "
            "restoration, not equal moral blame with collusive beneficiaries.\n\n"
            "Community monitoring and social audit can turn public money into a visible common trust. Yet "
            "moral lectures without redesign breed cynicism, while surveillance without values breeds fear. "
            "The durable strategy aligns character, incentives, opportunity reduction, collective disapproval "
            "of corrupt advantage and institutions capable of correction."
        ),
    ),
    _pyq(
        2023,
        (
            "GS-IV Q2(b): In the context of work environment, differentiate between 'coercion' "
            "and 'undue influence' with suitable examples. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, page 2. This topic uses the "
            "distinction for coercive corruption; broader workplace ethics is cross-routed."
        ),
        (
            "Coercion uses an explicit or implicit threat of unlawful or serious harm to compel conduct: "
            "for example, a licensing clerk demands payment and threatens indefinite delay of an entitlement. "
            "The victim's practical freedom is directly constrained. Undue influence exploits a relationship "
            "of authority, dependence, trust or vulnerability so that judgment is overborne without a clear "
            "threat: a superior repeatedly suggests that a junior's appraisal depends on selecting a preferred "
            "vendor.\n\n"
            "Both impair voluntary and impartial decision-making, but evidence and remedy differ. Coercion "
            "focuses on threat, extortion and protection of the victim. Undue influence focuses on positional "
            "power, dependency, private meetings, patterns of favour and the reasonableness of the resulting "
            "decision. Ordinary persuasion based on evidence is neither.\n\n"
            "Controls include written criteria and directions, multiple decision-makers, safe complaint routes, "
            "review of appraisal and transfer powers, anti-retaliation protection and independent investigation. "
            "In corruption analysis, the distinction prevents blaming a coerced citizen as though she were a "
            "willing collusive partner."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q6(b): India is an emerging economic power of the world as it has recently "
            "secured the status of fourth largest economy of the world as per IMF projection. "
            "However, it has been observed that in some sectors, allocated funds remain either "
            "underutilised or misutilised. What specific measures would you recommend for ensuring "
            "accountability in this regard to stop leakages and gaining the status of third largest "
            "economy of the world in near future? (150 words)"
        ),
        10,
        (
            "English wording verified from books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, "
            "pages 3-4; the scan's text layer drops part of one printed line, so the source note "
            "does not independently endorse the stem's macroeconomic projection as a current fact."
        ),
        (
            "Accountability should follow the complete chain: realistic allocation, timely release, competent "
            "sanction, fair procurement, verified delivery, payment, asset use and measurable outcome. Each "
            "stage needs a named responsible officer, milestone, variance threshold and review forum. "
            "Under-utilisation should trigger diagnosis of planning, land, capacity or approval bottlenecks, "
            "not indiscriminate year-end spending.\n\n"
            "Leakage controls include e-procurement, beneficial-ownership and conflict checks, segregation of "
            "vendor creation, receipt and payment, bank and ledger reconciliation, geo-tagged or field-verified "
            "assets where appropriate, and exception analytics for duplicates, split orders and unusual changes. "
            "Public dashboards should disclose allocation, release, physical progress and action taken, subject "
            "to privacy and security.\n\n"
            "CAG, internal audit, legislative committees, social audit and protected complaints must connect "
            "findings to correction, recovery, service restoration and proportionate sanction after fair inquiry. "
            "Technology improves traceability but cannot validate false input. Growth is strengthened when public "
            "money produces effective and equitable outcomes, not merely a high expenditure ratio."
        ),
    ),
    _pyq(
        2025,
        (
            "Neutral routing of GS-IV Q10: Rajesh, an administrative officer in a public-sector "
            "undertaking, is asked to procure stationery from a particular vendor. The total estimate "
            "exceeds his delegated limit, while splitting orders to avoid higher sanction is a common "
            "but rule-violating practice. What are his options, the ethical issues and the most "
            "appropriate course? (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, "
            "pages 8-9. The official case specifies the values and promotion pressure. Topic 18 owns "
            "financial propriety; Topic 22 owns the full case method."
        ),
        (
            "Rajesh can split the requirement, delay action without explanation, seek open competition within "
            "his power by artificially reducing scope, or consolidate the genuine need and route it to the "
            "competent higher authority. The first three evade responsibility. The ethical issues include "
            "financial propriety, possible vendor favour, conflict created by appraisal dependence, obedience "
            "versus integrity, auditability, fair competition and protection of public money.\n\n"
            "He should verify the total requirement and applicable procurement method, record that one demand "
            "cannot be fragmented merely to avoid sanction, prepare neutral specifications and market-based "
            "estimates, and submit the consolidated proposal to the competent authority. For goods, GFR Rule "
            "157 supplies the precise anti-piecemeal rule; works or services require their applicable category "
            "framework. He should seek written confirmation of any contrary direction and avoid privately "
            "accusing the superior without evidence.\n\n"
            "If pressure persists, Rajesh should use the authorised finance, procurement or vigilance review "
            "route while preserving records. Promotion anxiety cannot convert delegated power into ownership. "
            "The preferred option protects both timely purchase and institutional scrutiny; resignation is "
            "premature while lawful internal remedies remain."
        ),
    ),
    _pyq(
        2025,
        (
            "Neutral routing of GS-IV Q11: a district administrator discovers MGNREGA records showing "
            "non-payment to genuine workers, defective muster rolls, mismatch between work and payment, "
            "fictitious persons, fund siphoning and works that never existed. How should proper functioning "
            "be restored and what action should follow? (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, "
            "pages 9-10. The official paper contains programme background and the full enumerated facts. "
            "Topic 18 owns leakage controls; Topic 22 owns complete case architecture."
        ),
        (
            "The administrator should first protect workers and evidence. Freeze only suspect payment streams "
            "rather than the entire programme, secure muster rolls, sanction files, bank trails and measurement "
            "books, and arrange independent physical verification of works and beneficiary confirmation. Genuine "
            "pending wages and lawful employment demand should be restored through a controlled channel.\n\n"
            "A reconciliation should match job cards, attendance, measurements, payments, assets and bank "
            "accounts. Fictitious entries, connected officials and vendors, credential use and approval trails "
            "must be examined by a team independent of the implicated chain. A social audit and public hearing "
            "can add worker knowledge, but personal financial data should be protected. Findings should be "
            "classified as error, irregularity, fraud or suspected corruption rather than treated alike.\n\n"
            "Corrective action includes record repair, payment of dues, recovery where legally established, "
            "disciplinary or criminal referral through competent channels, and reasoned action-taken reports. "
            "Future prevention needs role separation, attendance and measurement controls, surprise field checks, "
            "exception alerts and safe complaints. The objective is simultaneous continuity of entitlement, "
            "evidence-based accountability and redesign of the conditions that enabled siphoning."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        (
            "Distinguish irregularity, waste, fraud, abuse of discretion and corruption in the "
            "utilisation of public funds."
        ),
        (
            "These terms identify different failures and should not be used as moral synonyms. An "
            "irregularity is departure from an applicable rule or procedure; it may be inadvertent and "
            "curable. Waste is avoidable expenditure or loss, even without private enrichment. Fraud "
            "requires intentional deception, such as a fictitious invoice. Abuse of discretion occurs "
            "when entrusted choice is exercised for an irrelevant, arbitrary or unauthorised purpose. "
            "Corruption uses public power for improper private, partisan or connected advantage, often "
            "through bribery, favouritism or collusion.\n\n"
            "The classification changes the response. A coding error may need correction and training; "
            "luxury spending needs value-for-money review; forged measurement requires evidence "
            "preservation and investigation; arbitrary vendor choice needs reasons and conflict review; "
            "a kickback requires competent anti-corruption process. Categories can overlap: a collusive "
            "false bill is irregular, fraudulent, wasteful and corrupt.\n\n"
            "Fair administration should classify facts before assigning stigma. This protects honest error "
            "while ensuring that public loss without personal gain is not dismissed as harmless."
        ),
    ),
    _original(
        10,
        (
            "Why should effective utilisation of public funds be assessed through economy, efficiency, "
            "effectiveness and equity rather than expenditure alone?"
        ),
        (
            "Expenditure proves only that money left an account; it does not prove value or justice. Economy "
            "asks whether appropriate inputs were obtained at a defensible whole-life cost without sacrificing "
            "quality. Efficiency connects inputs with outputs: whether resources produced the greatest suitable "
            "service. Effectiveness tests whether intended outcomes were achieved. Equity asks who benefited, "
            "who bore the burden and whether vulnerable or remote citizens could actually access the programme.\n\n"
            "A district may spend its full health grant and purchase many devices. It fails economy if maintenance "
            "costs were ignored, efficiency if devices remain idle, effectiveness if maternal outcomes do not "
            "improve, and equity if facilities are concentrated in accessible urban areas. Conversely, extra "
            "outreach cost may reduce narrow efficiency while improving equitable access and eventual effectiveness.\n\n"
            "The four dimensions therefore prevent both cheapest-is-best and spend-it-all thinking. They should "
            "be joined to legality, public purpose and reliable evidence. A defensible utilisation judgment asks "
            "whether authorised money became quality public value for the people for whom it was entrusted."
        ),
    ),
    _original(
        15,
        (
            "Design an integrity framework for public procurement and contract management from need "
            "identification to final payment."
        ),
        (
            "Integrity begins before tender. The user unit should establish genuine need, affordability, outcome "
            "and a realistic independent estimate. Specifications must be functional and neutral rather than "
            "tailored to a favoured brand. The competent authority should approve the total requirement; one demand "
            "must not be split to evade sanction or competition.\n\n"
            "Tender design should provide proportionate market access, published eligibility and evaluation "
            "criteria, adequate time, recorded clarifications and secure bid handling. Committee evaluation, "
            "conflict declarations, recusal, beneficial-ownership checks and pattern analysis for cover bids or "
            "bid rotation protect competition. Award needs a speaking record and a credible challenge route.\n\n"
            "Post-award controls are equally important. Independent technical personnel should verify quantity, "
            "quality and milestones before payment. Variations, extensions, subcontracting and price changes need "
            "predefined authority, reason and value-for-money analysis. Stores, user, finance and bank records "
            "should be reconciled; penalties and warranties should be enforced consistently.\n\n"
            "E-procurement and tamper-evident logs improve traceability but cannot cure biased specifications or "
            "collusive bidders. Risk-based internal audit, CAG scrutiny, protected complaints, proportionate "
            "sanctions and lessons fed into future standard documents complete the lifecycle."
        ),
    ),
    _original(
        15,
        (
            "Explain regulatory capture and state capture. How do they deepen ordinary corruption in "
            "public expenditure and regulation?"
        ),
        (
            "Regulatory capture occurs when a regulator persistently advances the regulated industry's interests "
            "instead of its statutory public purpose. It can arise through information dependence, revolving-door "
            "expectations, repeated private access, cultural identification or political pressure without a proved "
            "cash bribe. State capture is deeper: connected interests shape laws, policy, appointments, budget "
            "priorities or enforcement architecture so that durable private advantage is built into the rules.\n\n"
            "Ordinary bribery distorts a transaction; capture distorts the environment governing many transactions. "
            "A mining network, for example, may first bribe an inspector, then secure compliant transfers, weak "
            "permit conditions, selective policing and media silence. Replacing one inspector leaves the network "
            "intact. Public funds then finance distorted priorities, weak enforcement and inflated contracts while "
            "citizens cannot identify a single decision point to challenge.\n\n"
            "Response requires structural pluralism: transparent appointments and consultation, independent "
            "technical capacity, conflict and post-employment controls, disclosure of connected interests, open "
            "criteria, distributed review, audit across agencies, protected reporting and scrutiny of policy as "
            "well as transactions. Safeguards must avoid treating every industry consultation as capture; the test "
            "is persistent displacement of lawful public purpose and reasoned independence."
        ),
    ),
    _original(
        20,
        (
            "Construct a complete anti-corruption architecture for public funds by distinguishing "
            "prevention, detection, investigation, adjudication and sanction."
        ),
        (
            "A credible architecture assigns a different purpose to each stage. Prevention reduces opportunity "
            "before loss: simple rules, realistic budgets, competent sanction, role separation, neutral "
            "specifications, conflict disclosure, open competition, staff rotation where risk justifies it and "
            "ethical leadership. Detection identifies possible deviation through reconciliations, audit trails, "
            "complaints, surprise inspection, vendor-concentration analysis, duplicate-payment alerts and social "
            "verification. A detected anomaly is a lead, not guilt.\n\n"
            "Investigation preserves and tests evidence. It should secure records, trace decision and money flows, "
            "hear relevant persons, use technical expertise and distinguish error, negligence, fraud and corrupt "
            "motive. Independence and confidentiality protect both evidence and reputation. Adjudication belongs "
            "to the competent disciplinary, administrative or judicial forum. Notice, access to material, impartial "
            "hearing, appropriate proof, reasons and review prevent vigilance from becoming arbitrary.\n\n"
            "Sanction then imposes the authorised consequence: correction, recovery, contract remedy, debarment "
            "under applicable rules, disciplinary penalty or criminal sentence. It should reflect intent, role, "
            "harm, benefit, obstruction and repetition. Service restoration and institutional repair should not be "
            "forgotten merely because an individual is punished.\n\n"
            "The stages must communicate without collapsing. Audit can trigger investigation but cannot convict; "
            "an investigator should not become final judge. Protected whistleblowing, CAG and legislative scrutiny, "
            "citizen oversight, published action-taken reports and periodic control review connect the system. "
            "Technology strengthens traceability, but independent field verification and accountable human judgment "
            "remain essential. This separation protects public money while preserving legitimate administrative "
            "initiative and the credibility of every eventual finding."
        ),
    ),
    _original(
        20,
        (
            "A digital expenditure platform shows complete and timely utilisation, yet field reports reveal "
            "ghost beneficiaries, collusive vendors and unusable assets. Diagnose the failure and propose an "
            "institutional response."
        ),
        (
            "The platform has achieved transactional visibility, not verified public value. Complete utilisation "
            "may reflect timely data entry while beneficiary identity, need, delivery and asset quality remain "
            "false. Shared credentials can conceal responsibility; collusive vendors can compete formally; biased "
            "specifications can be digitised; and officials may optimise dashboard indicators rather than outcomes. "
            "The failure spans data quality, control design, field verification and incentives.\n\n"
            "Immediate action should preserve logs, master data, sanction files, bids, invoices, bank trails and "
            "measurement records. Suspect streams should be risk-contained without stopping genuine entitlements. "
            "Independent teams should reconcile beneficiaries, payments, work or asset existence, quantity, quality "
            "and actual use. Ownership links, bid patterns, device access and override histories should be examined. "
            "Affected persons must be heard before adverse findings.\n\n"
            "System redesign should separate registration, approval, receipt and payment; strengthen identity and "
            "role controls; require maker-checker approval for sensitive changes; publish safe scheme-level data; "
            "and create exception alerts for duplicates, split orders, concentration and post-award variation. "
            "Social audit can test lived delivery; CAG and internal audit can test systems and value for money. "
            "Whistleblowers need confidentiality and anti-retaliation.\n\n"
            "Confirmed loss should lead to correction, dues, recovery, contract remedies and proportionate "
            "disciplinary or criminal referral. Success metrics must shift from expenditure completion to economy, "
            "efficiency, effectiveness and equity. Digital evidence becomes trustworthy only when provenance, "
            "independent verification, contestability and remedy surround it. Periodic independent review should "
            "also test whether the redesigned platform reduces exclusion, delay and recurring manipulation."
        ),
    ),
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
        "1. Public-funds fiduciary foundation",
        "trust-chain",
        (
            "Citizens authorise public revenue",
            "Legislature approves public purpose",
            "Executive receives limited authority",
            "Official acts as fiduciary steward",
            "Law and sanction bound discretion",
            "Beneficiaries hold legitimate claims",
            "Records make reasons reviewable",
            "Outcome and remedy complete trust",
        ),
        "Public money is entrusted power, not departmental property.",
        "Use to open every theory or case answer.",
    ),
    _panel(
        "2. Budget-to-outcome chain",
        "results-chain",
        (
            "Diagnose public need",
            "Allocate realistic budget",
            "Release funds on time",
            "Procure lawful inputs",
            "Deliver verified outputs",
            "Enable citizen access",
            "Measure intended outcomes",
            "Learn and correct variance",
        ),
        "Expenditure is one link; it never proves delivery or outcome.",
        "Use for under-utilisation and accountability questions.",
    ),
    _panel(
        "3. Four-E value-for-money matrix",
        "four-axis-matrix",
        (
            "Economy: input cost and quality",
            "Efficiency: input-output relation",
            "Effectiveness: objective achieved",
            "Equity: distribution and access",
            "Legality supplies the floor",
            "Public purpose supplies direction",
            "Evidence tests claimed performance",
            "Trade-offs require recorded reasons",
        ),
        "Value for money is multidimensional and distribution-sensitive.",
        "Use for performance audit and scheme evaluation.",
    ),
    _panel(
        "4. Failure-classification ladder",
        "classification-ladder",
        (
            "Error: inadvertent mistake",
            "Irregularity: rule departure",
            "Waste: avoidable public loss",
            "Negligence: deficient due care",
            "Fraud: intentional deception",
            "Abuse: improper discretion",
            "Corruption: connected advantage",
            "Overlap changes remedy and proof",
        ),
        "Classify before blaming; public loss can exist without enrichment.",
        "Use to prevent legal and ethical overstatement.",
    ),
    _panel(
        "5. Financial-propriety control chain",
        "control-stack",
        (
            "Confirm authorised purpose",
            "Estimate total genuine requirement",
            "Identify competent sanction",
            "Apply category-specific rules",
            "Separate transaction roles",
            "Verify receipt and milestones",
            "Reconcile ledger bank and asset",
            "Record variance and correction",
        ),
        "Controls allocate responsibility so convenience cannot become authority.",
        "Use for GFR, sanction and re-appropriation answers.",
    ),
    _panel(
        "6. Procurement lifecycle integrity",
        "lifecycle-rail",
        (
            "Need and affordability",
            "Neutral specification",
            "Open market access",
            "Published evaluation criteria",
            "Conflict-safe reasoned award",
            "Independent delivery verification",
            "Controlled variation and payment",
            "Warranty disposal and learning",
        ),
        "A fair tender can still be corrupted after award.",
        "Use for procurement and contract-management reform.",
    ),
    _panel(
        "7. Bribery, collusion and cartel map",
        "corruption-branch",
        (
            "Coercive bribe extorts entitlement",
            "Protect victim and restore service",
            "Collusive bribe benefits both sides",
            "Trace public loss and both parties",
            "Cartel simulates competition",
            "Check bid rotation and cover bids",
            "Trace beneficial ownership",
            "Repair the enabling transaction",
        ),
        "Different corruption mechanisms require different evidence and remedies.",
        "Use for close distinctions and procurement cases.",
    ),
    _panel(
        "8. Capture and nexus escalation",
        "power-escalation",
        (
            "Conflict distorts one decision",
            "Repeated access normalises favour",
            "Regulator depends on regulated data",
            "Revolving-door incentive deepens bias",
            "Political protection weakens enforcement",
            "Business funds connected influence",
            "State capture reshapes rules",
            "Structural reform must break network",
        ),
        "Capture corrupts the rules of allocation, not only a single transaction.",
        "Use for mining, licensing and policy-capture analysis.",
    ),
    _panel(
        "9. Audit and citizen-oversight stack",
        "oversight-stack",
        (
            "Management control prevents error",
            "Internal audit tests systems",
            "CAG supplies external public audit",
            "Performance audit tests three Es",
            "Legislative committee demands answer",
            "Social audit verifies lived delivery",
            "Citizen complaint adds local evidence",
            "Action taken creates consequence",
        ),
        "Oversight forms complement one another only when findings reach correction.",
        "Use for CAG, PAC and social-audit questions.",
    ),
    _panel(
        "10. Anti-corruption stage architecture",
        "stage-separation",
        (
            "Prevention reduces opportunity",
            "Detection identifies anomaly",
            "Triage tests credibility and risk",
            "Investigation gathers evidence",
            "Adjudication determines responsibility",
            "Sanction imposes lawful consequence",
            "Remedy restores public interest",
            "Learning redesigns the system",
        ),
        "An audit flag is not guilt, and punishment is not system repair.",
        "Use for institutional-design and due-process answers.",
    ),
    _panel(
        "11. Technology with human verification",
        "digital-control-loop",
        (
            "Digitise sanction and payment trail",
            "Use role-based access",
            "Flag duplicate and split patterns",
            "Publish safe progress information",
            "Verify identity and field delivery",
            "Protect privacy and accessibility",
            "Enable challenge and correction",
            "Audit algorithms logs and overrides",
        ),
        "Technology changes observability, not the need for judgment and accountability.",
        "Use for PFMS, e-procurement and dashboard limits.",
    ),
    _panel(
        "12. Examiner-ready answer spine",
        "answer-spine",
        (
            "Define the precise failure",
            "State public-trust thesis",
            "Map budget-to-outcome mechanism",
            "Apply four Es and equity",
            "Name control and institution",
            "Separate accountability stages",
            "Add technology limit and remedy",
            "Conclude with qualified stewardship",
        ),
        "Specific mechanism plus institution plus safeguard beats a generic anti-corruption list.",
        "Use to structure 10, 15 and 20-mark answers.",
    ),
)


CURRENT_ANCHOR = {
    "title": "Current official anchors: performance audit and digital payment traceability",
    "verified_facts": (
        "CAG's official performance-audit page defines performance audit as an independent, objective and reliable examination of economy, efficiency and effectiveness.",
        "The same CAG source states that performance audit contributes to accountability and transparency, tests implementation and value for money, and focuses on activity and results rather than only reports or accounts.",
        "The official PFMS/GIFMIS description states that centralised treasury payments use just-in-time electronic instruments for vendors, employees, States and implementing agencies.",
        "The same official page states that the e-bill system, launched on 3 March 2022, permits suppliers and contractors to submit trackable online claims and is intended to reduce payment cycles and create effective audit trails.",
    ),
    "administrative_link": (
        "Together the sources illustrate the contemporary design principle: digital payment architecture "
        "improves traceability, while independent performance audit asks whether recorded expenditure "
        "actually produced economical, efficient and effective public value. Neither dispenses with need "
        "verification, competition, field confirmation, hearing or corrective responsibility."
    ),
    "limit": (
        "CAG's official definition uses three Es; equity is an additional ethical-distribution test in "
        "this topic, not a fourth term attributed to CAG. A digital audit trail proves that a recorded "
        "transaction occurred; it does not by itself prove the beneficiary, asset, specification, price "
        "or public outcome was genuine."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://cag.gov.in/en/page-performance-audit",
    "https://pfms.nic.in/SitePages/about-Verticals-GIFMIS.aspx",
)


SOURCE_CAVEAT = (
    "Topic 18 owns the ethical utilisation of public funds and the structural challenges of "
    "corruption. It uses the public-trust chain, four-E value-for-money analysis, financial "
    "propriety, procurement and contract integrity, leakage, diversion, coercive and collusive "
    "corruption, capture, audit, citizen oversight and stage-separated institutional design. "
    "The General Financial Rules cited are the Union framework; always check the rule actually "
    "applicable to a State, public-sector undertaking or autonomous body. GFR Rule 157 is quoted "
    "only for piecemeal purchase of goods to avoid higher sanction. Splitting works or services "
    "is the same evasion problem but must be tied to the applicable category rule and delegation "
    "framework, not falsely attributed verbatim to Rule 157. CAG's official performance-audit "
    "formulation expressly centres economy, efficiency and effectiveness; equity is added here as "
    "an ethical-distribution test rather than misattributed as part of that official three-E "
    "definition. Audit observations and digital alerts are evidence leads, not adjudications. "
    "Irregularity, waste, fraud, negligence, abuse of discretion and corruption can overlap but "
    "have different mental elements, proof and remedies. Public loss does not require private "
    "enrichment; criminal liability still requires the applicable statutory ingredients. Topic 19 "
    "owns detailed Prevention of Corruption Act and related legal provisions; Topic 20 owns exact "
    "CVC, CBI and Lokpal jurisdictions; Topic 21 owns detailed vigilance safeguards and protection "
    "of honest officials; Topic 22 owns full case-study method. Citizens' Charters, work culture "
    "and routine service-delivery design remain Topic 17-owned and appear here only as boundary "
    "references. Official local GS-IV PDFs control PYQ wording. Condensed case entries are expressly "
    "marked neutral routing and do not pretend to reproduce omitted facts verbatim."
)


REGISTER_SUPPLEMENT = (
    "### PUBLIC-FUNDS AND CORRUPTION RAPID REGISTER\n\n"
    "#### 1. FIDUCIARY STARTING POINT\n\n"
    "- Public revenue is authorised for a public purpose; the official is steward, not owner.\n"
    "- Core chain: citizen contribution -> legislative authorisation -> executive sanction -> implementation -> verified outcome -> audit/remedy.\n"
    "- **Allocation** is budget authority; **release** makes money available; **expenditure** records payment; **output** is immediate delivery; **outcome** is the intended public change.\n"
    "- Full expenditure is not proof of utilisation quality; low expenditure is not always failure if the original project became unsafe or unnecessary.\n"
    "- Public trust requires legality, fidelity to purpose, impartiality, value for money, equity, reasons, records and remedy.\n\n"
    "#### 2. FAILURE CLASSIFICATION\n\n"
    "- **Error:** inadvertent mistake; correct, train and redesign where recurrent.\n"
    "- **Irregularity:** breach of an applicable rule or procedure; may or may not cause loss or imply intent.\n"
    "- **Waste/squandering:** avoidable expenditure or lost public value; no private gain is required.\n"
    "- **Negligence:** failure to exercise due care; distinguish ordinary error, gross negligence and wilful omission.\n"
    "- **Fraud:** intentional deception, false representation or concealment for wrongful result.\n"
    "- **Abuse of discretion:** entrusted choice used for irrelevant, arbitrary, partisan or connected purpose.\n"
    "- **Corruption:** misuse of public power for improper private, partisan or connected advantage.\n"
    "- Categories overlap. A false measurement supporting a kickback can be irregular, fraudulent, wasteful and corrupt.\n\n"
    "#### 3. FOUR-E UTILISATION TEST\n\n"
    "- **Economy:** appropriate input at defensible whole-life cost; cheapest defective input is false economy.\n"
    "- **Efficiency:** relationship between resources and quality outputs; raw disposal counts can conceal exclusion.\n"
    "- **Effectiveness:** whether intended objectives and outcomes were achieved.\n"
    "- **Equity:** distribution of benefit, burden and access; additional cost may be justified for remote or vulnerable groups.\n"
    "- CAG's official performance-audit definition uses economy, efficiency and effectiveness; label equity as the ethical fourth test.\n"
    "- Always add legality, public purpose and reliable evidence; a technically efficient illegal diversion remains improper.\n\n"
    "#### 4. FINANCIAL PROPRIETY AND DELEGATED CONTROL\n\n"
    "- Confirm purpose, availability, competent sanction, applicable category rule and total genuine requirement.\n"
    "- Delegation allocates responsibility and scrutiny according to risk; it is not a target to evade.\n"
    "- **Rule 157 precision:** goods-specific bar on dividing demand into small quantities to avoid higher sanction.\n"
    "- Works/services splitting is analogous evasion under their applicable framework; do not cite Rule 157 verbatim for them.\n"
    "- Segregate need, vendor creation, evaluation, receipt, payment and reconciliation as proportionately feasible.\n"
    "- Reconcile sanction, purchase order, receipt, measurement, invoice, ledger, bank and asset registers.\n"
    "- Re-appropriation may be formally lawful yet ethically defective if public purpose, vulnerable beneficiaries, alternatives and legislative answerability are ignored.\n\n"
    "#### 5. PROCUREMENT AND CONTRACT INTEGRITY\n\n"
    "- Lifecycle: need -> estimate -> specification -> market access -> evaluation -> award -> delivery -> variation -> payment -> use/maintenance -> disposal.\n"
    "- Pre-tender traps: invented need, inflated estimate, tailored specification, artificial urgency, split demand.\n"
    "- Tender traps: restrictive eligibility, leaked information, changing criteria, cover bids, bid rotation, coordinated withdrawal, common beneficial ownership.\n"
    "- Award safeguards: conflict declarations, recusal, committee reasoning, secure bids, published criteria and challenge route.\n"
    "- Post-award traps: inferior material, false measurement, unjustified variation, repeated extension, hidden subcontracting, premature payment, non-enforcement of warranty or penalty.\n"
    "- Lowest price is not automatically value for money; use fitness, quality, whole-life cost, competition and outcome.\n\n"
    "#### 6. CORRUPTION MECHANISMS AND CAPTURE\n\n"
    "- **Coercive bribery:** citizen pays under threat for a lawful entitlement; protect complainant and restore service.\n"
    "- **Collusive bribery:** giver and taker benefit while State/citizen loses; investigate both parties and the transaction.\n"
    "- **Conflict of interest:** risk condition before proved corruption; disclose, assess, restrict, recuse, reassign or divest proportionately.\n"
    "- **Cartel:** competitors coordinate price, winners, territory or cover bids; apparent competition may be false.\n"
    "- **Regulatory capture:** regulator persistently serves the regulated interest through dependence, access, revolving doors or shared worldview.\n"
    "- **State capture:** connected actors shape law, policy, appointments or enforcement architecture for durable advantage.\n"
    "- **Nexus:** political protection + administrative discretion + business benefit + information or enforcement control.\n"
    "- Individual punishment is insufficient when rules, appointments, data and complaint channels remain captured.\n\n"
    "#### 7. AUDIT AND PUBLIC ACCOUNTABILITY\n\n"
    "- Management control prevents and corrects during implementation; internal audit tests systems for management.\n"
    "- CAG external audit serves legislative and public accountability; financial, compliance and performance questions are distinct.\n"
    "- Performance audit asks whether programmes operate with economy, efficiency and effectiveness and provide value for money.\n"
    "- Legislative committees such as the Public Accounts Committee examine audit findings and executive explanations; do not describe CAG as itself imposing departmental punishment.\n"
    "- Social audit compares records with citizen experience through field verification and public hearing.\n"
    "- Social audit requires independent facilitation, usable records, safety and action-taken follow-up; it does not replace professional audit or courts.\n"
    "- Audit finding -> executive response -> legislative/public scrutiny -> correction/recovery/referral -> system learning.\n\n"
    "#### 8. FIVE ACCOUNTABILITY STAGES\n\n"
    "- **Prevention:** reduce opportunity before loss through design, simplicity, role separation, conflict controls and ethical leadership.\n"
    "- **Detection:** identify anomalies through reconciliation, analytics, inspection, audit and complaints.\n"
    "- **Investigation:** preserve and test evidence, trace decision and money flows, hear persons and distinguish error from intent.\n"
    "- **Adjudication:** competent forum determines responsibility with notice, hearing, proof, reasons and review.\n"
    "- **Sanction:** authorised consequence matched to intent, harm, gain, role, obstruction and repetition.\n"
    "- Add **remedy:** pay genuine dues, restore service, correct records, recover lawful loss and repair controls.\n"
    "- Never write that an audit paragraph, complaint or algorithmic flag proves guilt.\n\n"
    "#### 9. PREVENTION, VIGILANCE AND WHISTLEBLOWING\n\n"
    "- Prevention bundle: realistic planning, published criteria, competent sanction, e-procurement, ownership checks, rotation where justified, conflict registers, supervision and audit trails.\n"
    "- Detection bundle: bank/ledger reconciliation, duplicate and split-order alerts, surprise verification, vendor-pattern analysis, protected complaints and social audit.\n"
    "- Responsible reporting: preserve evidence, use authorised independent channels where reasonably safe, minimise unrelated disclosure and protect sources and citizens.\n"
    "- Whistleblower system needs confidentiality, anti-retaliation, acknowledgment, feedback, escalation, independent inquiry and sanction for retaliation.\n"
    "- Topic 20 supplies exact institutional jurisdiction; Topic 21 supplies detailed vigilance and honest-official safeguards.\n"
    "- Protect bona fide decisions: bad outcome alone is not corrupt motive; inquiry should be specific, competent, confidential and evidence-based.\n\n"
    "#### 10. TECHNOLOGY AND CITIZEN OVERSIGHT\n\n"
    "- PFMS-style transaction visibility, e-bill, e-procurement, digital signatures and logs can reduce cash handling and improve traceability.\n"
    "- Useful alerts: duplicate beneficiary/account, split demand, repeated override, unusual concentration, round-number payment, change-order escalation and inactive asset.\n"
    "- Limits: garbage data, ghost beneficiaries, shared credentials, collusive bidders, biased specification, exclusion, privacy harm, cyber manipulation and dashboard gaming.\n"
    "- Required safeguards: provenance, role-based access, maker-checker control, field verification, accessible grievance, correction, independent audit and algorithm/log review.\n"
    "- Citizen oversight needs intelligible allocation, release, progress, outcome and action-taken information, not raw data dumps.\n"
    "- Keep detailed Citizens' Charters, work culture and routine service-delivery mechanisms in Topic 17.\n\n"
    "#### 11. PYQ ROUTES\n\n"
    "- **2019 Q2(a):** classify under- and mis-utilisation; causes -> implications -> stage-specific reforms.\n"
    "- **2019 Q2(b):** agree conditionally; wilful/grossly negligent omission can abuse trust, but poor outcome is not automatically corruption.\n"
    "- **2020 re-appropriation:** legality + welfare/development trade-off + alternatives + recorded advice; resignation last.\n"
    "- **2021 social audit:** records + field verification + hearing + action taken; adapt to institutional independence.\n"
    "- **2022 mining nexus:** move from individual bribery to capture/network analysis.\n"
    "- **2023 core values:** join moral formation with opportunity reduction and fair enforcement.\n"
    "- **2023 coercion:** distinguish threat from domination through dependency; protect coerced service-seeker.\n"
    "- **2025 Q6(b):** accountability follows allocation to outcome; technology plus independent verification.\n"
    "- **2025 Rajesh:** consolidate goods requirement, Rule 157 precision, competent sanction, written record, lawful escalation.\n"
    "- **2025 MGNREGA:** continue genuine entitlement while preserving evidence, reconciling records and repairing controls.\n\n"
    "#### 12. ANSWER-WRITING FRAMEWORK — TRUST TO REMEDY\n\n"
    "1. **Define:** name the exact failure—under-utilisation, waste, fraud, bribery, capture or conflict.\n"
    "2. **Thesis:** public money is fiduciary power tied to authorised purpose and intended beneficiaries.\n"
    "3. **Mechanism:** locate failure in allocation, release, sanction, procurement, delivery, payment or outcome.\n"
    "4. **Evaluate:** apply economy, efficiency, effectiveness, equity, legality and public trust.\n"
    "5. **Institution:** name competent sanction, internal control, CAG/legislative/social audit, vigilance or adjudicatory route without inventing jurisdiction.\n"
    "6. **Stage:** separate prevention, detection, investigation, adjudication, sanction and remedy.\n"
    "7. **Technology:** add traceability benefit and data/collusion/exclusion limit.\n"
    "8. **Conclusion:** combine timely public service, protection of honest judgment, proportionate accountability and institutional learning.\n\n"
    "> **Final thesis:** Ethical utilisation converts authorised money into lawful, economical, "
    "efficient, effective and equitable public value. Corruption is controlled not by one heroic "
    "watchdog or one digital portal, but by a chain of competent authority, contestable decisions, "
    "independent verification, protected voice, fair adjudication, proportionate consequence and "
    "restoration of the public purpose."
)
