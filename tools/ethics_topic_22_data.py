"""Learner-v2 source data: Ethics Topic 22, case-study answer architecture."""


SESSION_TITLES = (
    "Eight-element architecture: from verified facts to residual risk",
    "Six ethical checks: hard thresholds before weighted balancing",
    "Nested dilemmas, steelmanning and the residual-risk close",
    "Improper pressure, ethical dissent, whistleblowing and resignation",
    "Triage, scarce resources and competency-based case practice",
    "Worked mechanism: DC Vijay and integrated decision architecture",
    "Domain adaptation across public, corporate and professional cases",
    "Prelims facts, examiner traps and representative PYQ routing",
    "Mains analysis, probable demands and time-bound answer design",
    "Study links, recent cases, historical cases and final synthesis",
)


SESSION_GROUPS = (
    ("1", "2"),
    ("3", "4"),
    ("5", "6", "7"),
    ("8", "9", "10"),
    ("11", "12"),
    ("13",),
    ("14", "15"),
    ("16", "17", "18"),
    ("19", "20"),
    ("21", "extra-22", "extra-23"),
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
        "Facts must be separated from assumptions",
        (
            "A disciplined case answer restates only verified facts, identifies uncertainty and "
            "avoids silently inventing motives, powers or resources; later options and judgments "
            "must remain traceable to what the scenario actually establishes."
        ),
        (
            "An officer assumes a contractor bribed a superior merely because they met privately. "
            "What initial discipline is missing?"
        ),
        (
            "A candidate labels disputed claims as unverified and states what must be checked before "
            "action. Which architectural element is being applied?"
        ),
        "eight-element architecture",
    ),
    _mcq(
        "Stakeholder mapping includes silent parties",
        (
            "Stakeholder mapping must include direct participants and less visible parties such as "
            "future generations, absent beneficiaries, vulnerable groups and the institution whose "
            "long-term credibility may be altered by the decision."
        ),
        (
            "A forest-diversion answer lists officials and applicants but ignores tribal livelihoods, "
            "biodiversity and future residents. What mapping defect appears?"
        ),
        (
            "A procurement answer includes patients, rival bidders and public trust although none "
            "speaks in the narrative. Which disciplined practice does this show?"
        ),
        "eight-element architecture",
    ),
    _mcq(
        "Hard constraints eliminate impossible choices early",
        (
            "Legal authority, delegation limits, time, verified information, jurisdiction and actual "
            "capacity should be mapped before generating options; a proposal that breaches a binding "
            "constraint is not a realistic administrative choice."
        ),
        (
            "A district officer promises immediate national legislation to resolve a local emergency. "
            "Which overlooked element makes the promise unusable?"
        ),
        (
            "A field engineer distinguishes emergency stabilisation within delegated power from a "
            "permanent repair requiring superior sanction. Which reasoning step is decisive?"
        ),
        "eight-element architecture",
    ),
    _mcq(
        "Options require realistic comparison",
        (
            "A strong answer develops at least three feasible courses, including a sequenced or hybrid "
            "response where useful, and states one concrete advantage and disadvantage before selecting "
            "the most defensible course."
        ),
        (
            "A response offers only obey or resign, although written dissent and lawful escalation remain "
            "available. Which architectural weakness does this reveal?"
        ),
        (
            "A disaster answer compares immediate departure, total abstention, brief delegated absence "
            "and remote oversight before deciding. Which option discipline is illustrated?"
        ),
        "eight-element architecture",
    ),
    _mcq(
        "Legality operates as a hard threshold",
        (
            "An unlawful option is normally eliminated before ethical balancing, even when it appears "
            "compassionate or efficient; claimed benefits cannot convert absence of lawful authority into "
            "a permissible administrative response."
        ),
        (
            "An officer proposes unlawful data disclosure because it could speed an investigation. Which "
            "check defeats the proposal before benefits are weighed?"
        ),
        (
            "A candidate first removes sanction evasion and then compares lawful urgent responses. Which "
            "evaluation sequence is correct?"
        ),
        "thresholds and weighting",
    ),
    _mcq(
        "Conflict of interest is near-disqualifying",
        (
            "A genuine personal, family or financial interest requires disclosure and withdrawal from the "
            "specific decision; confidence in one's own honesty cannot cure the appearance or structural "
            "risk of biased authority."
        ),
        (
            "A committee chair evaluates her brother's bid because management trusts her judgment. Which "
            "threshold has been ignored?"
        ),
        (
            "An official records a family link and stops influencing that tender while continuing other "
            "duties. Which principle is correctly applied?"
        ),
        "thresholds and weighting",
    ),
    _mcq(
        "Weighted checks require an explicit priority",
        (
            "Public interest, proportionality, transparency and compassion may pull in different directions; "
            "the candidate should state which consideration is decisive in context and explain why the "
            "remaining concerns are mitigated rather than denied."
        ),
        (
            "Scarce beds could maximise lives saved yet disadvantage a vulnerable group. What must the "
            "answer do beyond listing both values?"
        ),
        (
            "A crisis response prioritises proportionality while adding honest communication and a grievance "
            "route. Which balancing method is shown?"
        ),
        "thresholds and weighting",
    ),
    _mcq(
        "Moral theories test surviving options",
        (
            "After threshold screening, deontology tests duties and rights, consequentialism compares "
            "foreseeable outcomes, and virtue ethics asks what integrity, courage, compassion and practical "
            "wisdom require from the decision-maker."
        ),
        (
            "A candidate cites compassion alone without testing duty, effects or character. Which evaluative "
            "layer remains incomplete?"
        ),
        (
            "A response compares role duty, likely public harm and practical wisdom before choosing a hybrid "
            "course. Which combined method is being used?"
        ),
        "thresholds and weighting",
    ),
    _mcq(
        "Nested dilemmas should be solved separately",
        (
            "When a scenario contains analytically distinct tensions, each should receive a compact independent "
            "evaluation before the answers are recombined; this prevents one emotional conflict from obscuring "
            "resource, transparency or legality questions."
        ),
        (
            "A disaster answer treats personal grief as the only issue and ignores delegation fairness and "
            "public communication. Which technique was omitted?"
        ),
        (
            "A candidate resolves command continuity, relief allocation and crisis communication separately, "
            "then integrates them. Which advanced discipline is illustrated?"
        ),
        "stress testing",
    ),
    _mcq(
        "Steelmanning uses the strongest objection",
        (
            "Before closing, the answer should present the most credible objection to its chosen course and "
            "either defeat it with reasons or modify implementation to absorb its valid concern without "
            "abandoning the decision."
        ),
        (
            "A sustainability proposal ignores the risk that costly commitments could destroy competitiveness. "
            "Which stress test is absent?"
        ),
        (
            "A decision adds time-bound milestones after accepting that an unlimited transition could be "
            "commercially destructive. Which reasoning device is applied?"
        ),
        "stress testing",
    ),
    _mcq(
        "Residual risk must name monitoring and accountability",
        (
            "A mature conclusion identifies the specific harm that may survive the preferred course, names a "
            "review or monitoring mechanism and assigns responsibility to a person or institution rather than "
            "claiming complete resolution."
        ),
        (
            "An answer ends with justice will prevail and names no remaining danger. Which closing discipline "
            "is missing?"
        ),
        (
            "A delegated disaster command is followed by scheduled check-ins and a review led by the returning "
            "officer. Which closing formula is present?"
        ),
        "stress testing",
    ),
    _mcq(
        "Residual risk can be expressed as a control formula",
        (
            "Residual risk equals inherent risk reduced by effective controls, while uncertainty and control "
            "failure remain visible; the expression disciplines mitigation but does not pretend ethical judgment "
            "can be reduced to arithmetic."
        ),
        (
            "A candidate lists safeguards but never asks what danger remains if one safeguard fails. Which "
            "conceptual lens would improve the close?"
        ),
        (
            "A response names inherent retaliation risk, protection controls and the remaining exposure after "
            "those controls. Which formula is being operationalised?"
        ),
        "stress testing",
    ),
    _mcq(
        "Conflict resolution follows disclose, recuse, refer, publish",
        (
            "A conflicted decision-maker should disclose the connection in writing, recuse from that matter, "
            "refer it to an untainted authority and ensure objective criteria govern the eventual decision and "
            "its defensibility."
        ),
        (
            "A procurement chair tells colleagues about her family link but continues scoring bids. Which steps "
            "remain incomplete?"
        ),
        (
            "A superior appoints an unconflicted committee that applies pre-announced criteria after the original "
            "chair withdraws. Which sequence is completed?"
        ),
        "pressure and dissent",
    ),
    _mcq(
        "Improper oral pressure should be converted into writing",
        (
            "An officer facing an improper oral direction should record its substance, seek written confirmation, "
            "state the professional objection and use the normal escalation route while continuing lawful duties "
            "unless action would itself be unsafe."
        ),
        (
            "A minister pressures an engineer verbally and the engineer merely refuses in private. Which protective "
            "administrative response is absent?"
        ),
        (
            "A professional records the instruction, technical risk and request for confirmation before escalating. "
            "Which method is correctly used?"
        ),
        "pressure and dissent",
    ),
    _mcq(
        "Ethical dissent climbs a proportionate ladder",
        (
            "Evidence-based dissent normally moves from competent internal reporting to an independent internal "
            "tier, then to authorised external channels and only finally to public disclosure when serious continuing "
            "harm and failed alternatives justify it."
        ),
        (
            "An employee immediately posts confidential allegations online without testing safe lawful channels. "
            "Which escalation discipline was bypassed?"
        ),
        (
            "A quality officer skips a compromised manager but reports to an independent regulator with preserved "
            "evidence. Which rung logic is followed?"
        ),
        "pressure and dissent",
    ),
    _mcq(
        "Resignation is an evaluated last resort",
        (
            "Resignation becomes defensible only after lawful resistance and escalation are exhausted or unavailable, "
            "and when departure protects public interest better than remaining as a principled internal safeguard; "
            "it should not function as emotional escape."
        ),
        (
            "An officer resigns before recording dissent although continued service could still block the wrongful "
            "act. Which evaluation error occurs?"
        ),
        (
            "An official reserves resignation for a point at which personal execution of an unresolved illegality "
            "becomes unavoidable. Which test is applied?"
        ),
        "pressure and dissent",
    ),
    _mcq(
        "Triage criteria should be published and reviewable",
        (
            "Scarce-resource allocation should use pre-announced, relevant and non-discriminatory criteria, record "
            "their actual application, provide an appropriate review route and revise them when resources or the "
            "emergency profile materially changes."
        ),
        (
            "A hospital allocates staff through undocumented personal discretion during a surge. Which triage "
            "safeguards are missing?"
        ),
        (
            "A relief authority publishes need and vulnerability criteria, logs decisions and revisits them daily. "
            "Which method is illustrated?"
        ),
        "triage and adaptation",
    ),
    _mcq(
        "Triage must acknowledge its value trade-off",
        (
            "A defensible allocation explains whether aggregate welfare, urgency, survivability, vulnerability or "
            "priority to the worst-off is being emphasised, then adds equity safeguards so the chosen metric does "
            "not become mechanically dehumanising."
        ),
        (
            "A candidate calls a severity score ethically neutral although it disadvantages a patient group. Which "
            "analysis is missing?"
        ),
        (
            "A committee prioritises urgent survivability while auditing disparate impact on vulnerable patients. "
            "Which ethical balance is achieved?"
        ),
        "triage and adaptation",
    ),
    _mcq(
        "Domain adaptation preserves the architecture",
        (
            "The same eight elements apply across administration, corporate governance, policing, research, health "
            "and environmental disputes, but legal authority, technical standards, affected stakeholders and competent "
            "institutions must be adapted to the domain."
        ),
        (
            "A candidate copies a public procurement remedy into a clinical-consent dispute without naming the ethics "
            "committee. Which adaptation error occurs?"
        ),
        (
            "A research case uses the common decision sequence but routes consent and data concerns to the competent "
            "ethics body. Which transfer skill is shown?"
        ),
        "triage and adaptation",
    ),
    _mcq(
        "Time pressure changes depth, not sequence",
        (
            "Under examination pressure, candidates should compress each architectural element rather than omit it: "
            "one-line facts and dilemma, a compact stakeholder-constraint map, three options, decisive checks, action "
            "steps and a residual-risk close."
        ),
        (
            "A candidate spends most of the answer narrating facts and has no space for implementation. Which time "
            "management correction is needed?"
        ),
        (
            "A twenty-mark response uses short labelled blocks while retaining all eight elements. Which examination "
            "principle is followed?"
        ),
        "triage and adaptation",
    ),
    _mcq(
        "Decision writing should identify the decisive reason",
        (
            "A recommendation should name the selected option, the threshold or weighted consideration that controls "
            "the choice and the safeguard answering the strongest objection; merely saying balance all interests "
            "does not decide the case."
        ),
        (
            "An answer lists every value but refuses to choose among feasible options. Which decision-writing defect "
            "remains?"
        ),
        (
            "A response selects lawful phased repair because urgency and proportionality control after sanction evasion "
            "is removed. Which clarity is demonstrated?"
        ),
        "answer execution",
    ),
    _mcq(
        "Implementation must assign actions and audiences",
        (
            "Implementation should specify immediate and later actions, competent actors, documentation and communication "
            "to seniors, team members and affected people; a morally attractive choice without an execution route remains "
            "administratively incomplete."
        ),
        (
            "A district officer chooses evacuation but never identifies transport, command or public messaging. Which "
            "element is incomplete?"
        ),
        (
            "A decision names the deputy, written delegation, check-in schedule and public notice. Which implementation "
            "discipline is present?"
        ),
        "answer execution",
    ),
    _mcq(
        "Communication should be honest and calibrated",
        (
            "Crisis communication should disclose verified information, acknowledge uncertainty, prevent avoidable panic "
            "and commit to updates; neither premature certainty nor prolonged concealment protects trust when facts are "
            "still developing."
        ),
        (
            "An administrator repeats an unverified viral claim to appear transparent. Which communication mistake is "
            "made?"
        ),
        (
            "An official states what is known, what is being checked and when the next update will come. Which weighted "
            "balance is shown?"
        ),
        "answer execution",
    ),
    _mcq(
        "A complete answer ends with qualified confidence",
        (
            "The final verdict should be decisive but not absolute: it should connect lawful action, public purpose, "
            "proportionate safeguards and review, showing confidence in the chosen route while accepting that implementation "
            "requires continuing ethical oversight."
        ),
        (
            "A candidate claims the chosen option permanently eliminates every risk. Which concluding flaw appears?"
        ),
        (
            "A response commits to a course while naming review triggers and accountability. Which mature conclusion is "
            "being used?"
        ),
        "answer execution",
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
            "Neutral routing of GS-IV Q8: a senior Ministry officer with privileged policy "
            "knowledge faces a Minister's request to alter a road alignment near the Minister's "
            "farm and an offer of land in the officer's wife's name. Analyse the conflict and response."
        ),
        20,
        (
            "Neutral demand verified against books\\more_previous_papers\\"
            "GENERAL-STUDIES-PAPER-IV.pdf, page 7. OCR quality is uneven, so this entry does "
            "not claim verbatim reproduction."
        ),
        (
            "Facts: A public decision is being pressed toward private ministerial gain, while a benefit "
            "is offered through the officer's spouse. Stakeholders: road users, affected landholders, "
            "taxpayers, the Ministry, the Minister, the officer and family, and institutional trust. "
            "Constraints: the officer cannot redesign policy for private advantage; official information "
            "and delegated authority must be used only for public purpose.\n\n"
            "Options: comply and accept the land; refuse orally but leave no record; or decline the benefit, "
            "record the request and technical objection, preserve the original evaluation, and refer the "
            "matter through the competent hierarchy or vigilance channel. The first option fails legality "
            "and conflict-of-interest thresholds. The second is personally clean but institutionally weak. "
            "The third best serves legality, public interest and transparency.\n\n"
            "Decision: reject the offer, disclose the attempted inducement, avoid any personal participation "
            "tainted by it, and insist that alignment be assessed through published technical and social criteria. "
            "The strongest objection is that recording a Minister's request may trigger retaliation; that risk "
            "does not justify silent compliance and is reduced by contemporaneous documentation and collective "
            "technical review.\n\n"
            "Implementation: make a dated written note, seek written confirmation of any contrary direction, "
            "secure maps and evaluation records, and escalate through the normal reporting and oversight route. "
            "Residual risk: political transfer or manipulation of later appraisal remains; the Secretary or "
            "competent vigilance authority should monitor the record and audit the final alignment decision."
        ),
    ),
    _pyq(
        2019,
        (
            "Neutral routing of GS-IV Q7: a rescue officer's team is attacked by an angry crowd "
            "during a severe natural calamity, and some personnel want operations withdrawn. "
            "Evaluate the options and the public-service qualities required."
        ),
        20,
        (
            "Neutral demand verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 4. The official printed scenario controls "
            "all details."
        ),
        (
            "Facts: essential rescue work faces violence from distressed citizens, and team safety is "
            "now part of the operational dilemma. Stakeholders: trapped victims, the crowd, rescue staff "
            "and families, local administration, police and the wider disaster response. Constraints: "
            "the duty to rescue continues, but the leader cannot recklessly expose personnel or abandon "
            "victims without exploring safer alternatives.\n\n"
            "Options: withdraw completely; continue unchanged despite attack; or pause locally, establish "
            "security and communication, engage credible community representatives, redesign deployment "
            "and resume priority rescue. Complete withdrawal sacrifices public duty; unchanged deployment "
            "is disproportionate to staff risk. The sequenced option best combines courage, empathy, "
            "prudence, team leadership and public interest.\n\n"
            "Decision: maintain the mission through a safer operational plan. Steelman: any pause may cost "
            "lives. Therefore the pause must be minimal, rescue of immediately endangered persons must continue "
            "where feasible, and police/community liaison must work in parallel rather than sequentially.\n\n"
            "Implementation: brief staff, create protected corridors, deploy medical and police support, use "
            "local leaders to communicate priorities, document assaults and rotate exhausted teams. Residual "
            "risk: renewed violence or distrust may disrupt access; the incident commander should maintain live "
            "risk review, community liaison and after-action learning while remaining personally accountable "
            "for both rescue continuity and team safety."
        ),
    ),
    _pyq(
        2020,
        (
            "Neutral routing of GS-IV Q7: Finance Ministry officer Rajesh Kumar is pressed to "
            "re-appropriate welfare funds toward favoured development projects and must evaluate "
            "ethical issues, available options and whether resignation is worthy."
        ),
        20,
        (
            "Neutral demand verified against books\\more_previous_papers\\Gen_St_P4.pdf, "
            "pages 4-5. Wording is condensed; the local official paper remains authoritative."
        ),
        (
            "Facts: a welfare allocation is proposed for re-appropriation to other projects under senior "
            "pressure. Stakeholders: intended health beneficiaries, project beneficiaries, Parliament, "
            "taxpayers, Ministry leadership and Rajesh. Constraints: he lacks unilateral authority to stop "
            "the decision; procedural permissibility does not itself establish propriety; the budget window "
            "is limited.\n\n"
            "Options: comply silently; leak externally; resign immediately; or record a reasoned welfare-impact "
            "objection, seek written confirmation and escalate through financial, audit and competent oversight "
            "channels while continuing lawful duties. Silent compliance fails public interest and transparency. "
            "A leak bypasses lawful routes. Immediate resignation removes a principled internal voice before "
            "resistance has been tested.\n\n"
            "Decision: choose written dissent and time-bound escalation. The decisive checks are public purpose "
            "and transparency, because legality may not clearly eliminate the proposal. Steelman: internal channels "
            "may be captured and delay can consummate diversion. Rajesh should therefore set a short response period "
            "and ensure the objection enters the independent audit trail.\n\n"
            "Implementation: attach beneficiary and fiscal impact, request a speaking direction, refer to the "
            "competent financial authority, and refuse to certify facts he knows are false. Resignation remains a "
            "last resort if all lawful channels fail and continued office would compel personal execution or "
            "legitimisation of the wrong. Residual risk: retaliation or formal override remains; a named senior "
            "financial authority and later audit should review the decision and preserved dissent."
        ),
    ),
    _pyq(
        2021,
        (
            "Neutral routing of GS-IV Q10: a hospital administrator must devise and justify "
            "criteria for deploying scarce clinical and non-clinical staff during a COVID-19 surge "
            "and consider whether a private hospital changes the ethical justification."
        ),
        20,
        (
            "Neutral demand verified against books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 8. The official scenario controls "
            "the precise subparts."
        ),
        (
            "Facts: demand exceeds safe staffing capacity during an infectious-disease emergency. Stakeholders: "
            "patients, clinical and non-clinical staff, vulnerable groups, families, management and the public "
            "health system. Constraints: skills are not interchangeable, exposure risk is unequal, fatigue impairs "
            "care, and decisions must be made rapidly with incomplete forecasts.\n\n"
            "Options: deploy volunteers ad hoc; allocate only by seniority; maximise immediate clinical throughput "
            "without equity safeguards; or publish clinically relevant criteria covering competence, urgency, "
            "exposure, rotation, vulnerability and continuity, with review and grievance mechanisms. Ad hoc and "
            "seniority-only methods are arbitrary; pure throughput can devalue vulnerable patients and exhaust staff.\n\n"
            "Decision: use transparent, competence-based and equity-audited triage. Consequentialism supports saving "
            "the most lives and maintaining service; duty ethics protects non-discrimination and staff safety; "
            "compassion requires protection for high-risk workers. Steelman: rigid criteria may become obsolete as "
            "the surge changes. A fixed review cycle and incident-command discretion with written reasons answer it.\n\n"
            "Implementation: publish the matrix, train deployment teams, provide protective equipment, rotate "
            "exposure, preserve surge reserves and communicate individual decisions respectfully. The ethical floor "
            "does not fall in a private hospital: ownership may change internal resourcing discretion, not duties "
            "of non-discrimination, safety and honest criteria during a public-health emergency. Residual risk: "
            "metric bias or sudden absenteeism remains; a multidisciplinary triage committee should audit outcomes "
            "daily and revise criteria openly."
        ),
    ),
    _pyq(
        2022,
        (
            "Neutral routing of GS-IV Q9: an investigative journalist uncovers a stone-mining "
            "mafia linked with police, civil officials and political influence, while the media "
            "owner pressures the journalist to suppress the report."
        ),
        20,
        (
            "Neutral demand verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 10. This is a faithful "
            "routing, not a verbatim copy."
        ),
        (
            "Facts: alleged illegal mining is protected by a network that may compromise ordinary reporting "
            "channels, and the journalist faces inducement or suppression. Stakeholders: affected communities, "
            "workers, environment, honest officials, sources, the journalist, the media institution and justice "
            "agencies. Constraints: allegations need authentication; source safety and evidence integrity may be "
            "lost through premature publication; local enforcement may be captured.\n\n"
            "Options: suppress the story; publish sensationally at once; resign without preserving evidence; or "
            "authenticate and duplicate records, obtain independent legal-editorial review, assess threats, use "
            "authorised regulatory or judicial channels, and publish responsibly when source and investigation risks "
            "are controlled. Suppression enables harm; impulsive disclosure may expose sources and destroy the case.\n\n"
            "Decision: follow a protected dissent ladder, skipping the compromised internal rung but preferring an "
            "independent lawful channel before unrestricted disclosure. Steelman: delay allows continuing extraction "
            "and evidence destruction. The response therefore requires immediate preservation, parallel referral and "
            "a defined publication decision point.\n\n"
            "Implementation: keep dated copies, separate source identity, inform an independent editor or professional "
            "body, seek security if threats are credible, and route evidence to the competent State authority or court "
            "with jurisdiction. Residual risk: retaliation, institutional capture and source exposure remain; an "
            "independent legal representative should maintain an access log and review safety and follow-up at fixed "
            "intervals."
        ),
    ),
    _pyq(
        2023,
        (
            "Neutral routing of GS-IV Q10: an honest IAS officer serving as Managing Director "
            "of a State Road Transport Corporation faces a corrupt, politically powerful Chairman "
            "and separate pressure from an Opposition party."
        ),
        20,
        (
            "Neutral demand verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, pages 10-11. The official "
            "paper remains controlling."
        ),
        (
            "Facts: the Managing Director faces suspected corruption from the Chairman and partisan pressure "
            "from the Opposition. Stakeholders: commuters, employees, taxpayers, vendors, the Corporation, "
            "both political actors and the officer. Constraints: the officer cannot remove the Chairman alone, "
            "must verify specific irregularities and must preserve political neutrality while services continue.\n\n"
            "Options: comply with the Chairman; hand internal records to the Opposition; resign immediately; or "
            "document each irregular direction, seek written clarification, protect decisions within lawful authority "
            "and escalate through audit, vigilance and the administrative department. Compliance breaches public trust. "
            "A partisan leak compromises neutrality. Resignation is premature while institutional resistance remains.\n\n"
            "Decision: choose documented, non-partisan escalation. Legality and procurement propriety screen verified "
            "wrongdoing; transparency and public interest guide the response. Steelman: internal channels may be delayed "
            "by political influence. The answer is a time-bound referral with independent record preservation, not a "
            "political counter-alliance.\n\n"
            "Implementation: record oral pressures, seek written orders, decline political sharing outside lawful "
            "disclosure, secure procurement records and maintain service delivery. If the normal recipient is compromised, "
            "move to the next independent vigilance or statutory tier. Residual risk: transfer, slow-walking and continuing "
            "loss remain; a competent external oversight authority should acknowledge the referral, monitor deadlines "
            "and audit affected contracts."
        ),
    ),
    _pyq(
        2024,
        (
            "Neutral routing of GS-IV Q7: ABC Incorporated must respond to rapid AI expansion, "
            "a substantial increase in greenhouse-gas emissions, a net-zero commitment, innovation "
            "pressure and proposed environmental penalties."
        ),
        20,
        (
            "Neutral demand verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, "
            "page 4. Numerical and contextual details should be taken from that official paper."
        ),
        (
            "Facts: AI-related data-centre growth conflicts with a public climate commitment and commercial "
            "competition. Stakeholders: communities, workers, customers, shareholders, regulators, suppliers and "
            "future generations. Constraints: the company cannot treat a pledge as performance, but an abrupt shutdown "
            "could destroy useful innovation and employment; measurement boundaries must be credible.\n\n"
            "Options: continue and manage publicity; halt AI growth; rely mainly on offsets; or adopt independently "
            "verified absolute and intensity targets for efficiency, cleaner power, water, hardware and supply chains "
            "while continuing calibrated innovation. Inaction risks greenwashing; a total halt may be disproportionate; "
            "offset-only action leaves underlying demand unchanged.\n\n"
            "Decision: choose the time-bound verified transition. Public interest, intergenerational justice and "
            "transparency outweigh short-term cost, while proportionality preserves innovation. Steelman: competitors "
            "without similar costs may erode the firm's market position and future capacity to invest. Milestones should "
            "therefore be ambitious but sequenced, technology-neutral and reviewed against both environmental and "
            "commercial evidence.\n\n"
            "Implementation: commission external assurance, publish assumptions, link executive accountability to "
            "targets, price environmental costs into investment and support proportionate penalties with due process "
            "and equal criteria. Residual risk: clean-power scarcity and rebound demand may defeat efficiency gains; "
            "the board sustainability committee should monitor absolute emissions and trigger corrective capital "
            "allocation when the pathway is missed."
        ),
    ),
    _pyq(
        2024,
        (
            "Neutral routing of GS-IV Q10: Sneha chairs a hospital procurement process in "
            "which her financially stressed brother is a bidder, while management says it will "
            "support whatever decision she takes."
        ),
        20,
        (
            "Neutral demand verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, "
            "page 8. The entry is condensed to preserve neutral routing."
        ),
        (
            "Facts: Sneha exercises procurement influence while a close family member competes for financial "
            "benefit. Stakeholders: patients, hospital management, all bidders, her brother, Sneha and institutional "
            "credibility. Constraints: management trust does not remove the conflict; procurement must conclude on "
            "time and against defensible quality and cost criteria.\n\n"
            "Options: score all bids herself; secretly disadvantage her brother; ask him to withdraw informally; or "
            "disclose the relationship in writing, recuse, refer evaluation to an unconflicted authority and apply "
            "pre-announced criteria. The first two options remain biased in opposite directions. Informal withdrawal "
            "solves one outcome but leaves no durable process.\n\n"
            "Decision: disclose, recuse, refer and publish or consistently apply the criteria. Conflict of interest "
            "is a hard threshold; claimed personal integrity cannot make continued participation legitimate. Steelman: "
            "recusal may reveal private family hardship and delay urgently needed supplies. Disclosure should be limited "
            "to what the competent authority needs, and an alternate evaluator should be appointed immediately.\n\n"
            "Implementation: record the relationship before final evaluation, cease all influence, preserve bid "
            "confidentiality and communicate the result uniformly. Residual risk: bidders may still perceive concealed "
            "influence or reverse discrimination. Management's compliance or audit function should review the scoring "
            "trail and require the same recusal in future tenders involving the brother."
        ),
    ),
    _pyq(
        2024,
        (
            "Neutral routing of GS-IV Q12: Dr Srinivasan faces pressure to accelerate a "
            "biotechnology trial despite deficiencies in informed consent and the exclusion of "
            "an unfavourable data point."
        ),
        20,
        (
            "Neutral demand verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, "
            "page 9. The official paper controls the full narrative and subparts."
        ),
        (
            "Facts: vulnerable participants may not have received adequate informed consent, and unfavourable "
            "evidence has been excluded under commercial pressure. Stakeholders: participants, future patients, "
            "research staff, the ethics committee, regulator, company and scientific community. Constraints: valid "
            "consent and data integrity are threshold requirements; the scientist cannot alone substitute for the "
            "competent ethics body.\n\n"
            "Options: continue unchanged; retrospectively regularise records; halt everything unilaterally; or disclose "
            "both lapses, restore the complete dataset, protect participants and ask the ethics committee to decide "
            "re-consent, suspension or continuation. Concealment and falsification fail legality and research ethics. "
            "Unilateral action may exceed role authority and weaken institutional review.\n\n"
            "Decision: immediate written disclosure and referral to the ethics committee, with no further compromised "
            "enrolment. Duty to participants and truth in science outweigh timeline pressure. Steelman: interruption "
            "may delay a beneficial treatment and impose costs on participants already enrolled. The committee should "
            "therefore conduct urgent, evidence-based review rather than accept either concealment or indefinite delay.\n\n"
            "Implementation: secure raw data, stop improper recruitment, arrange independent re-consent where directed, "
            "inform the board that continuation is institutionally controlled and protect reporters from retaliation. "
            "Residual risk: re-consent may itself pressure vulnerable participants and restored data may be mishandled; "
            "the ethics committee should appoint an independent monitor and conduct a follow-up site audit."
        ),
    ),
    _pyq(
        2025,
        (
            "Neutral routing of GS-IV Q7: Deputy Commissioner Vijay leads relief after a "
            "devastating hill disaster when his mother dies far away and the crisis worsens, "
            "creating competing personal and public duties."
        ),
        20,
        (
            "Neutral demand verified against books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, "
            "pages 4-5. The canonical Basic treatment supplies the controlling case method."
        ),
        (
            "Facts: Vijay directs continuing relief amid renewed danger, disrupted communications and personal "
            "bereavement. Stakeholders: victims, relief teams, his family, the deputy command, seniors and Vijay's "
            "wellbeing. Constraints: relief cannot pause; travel and communication are uncertain; any absence requires "
            "authorised, competent and recorded delegation.\n\n"
            "Options: leave immediately through informal handover; remain and abandon the rites; rely only on remote "
            "management; or make a brief authorised absence after written delegation, intensive briefing and scheduled "
            "remote oversight. Nested dilemmas must be separated: personal duty versus public duty, fairness in relief "
            "allocation, and truthful communication versus public calm.\n\n"
            "Decision: choose brief, tightly controlled delegation if a competent deputy and communications are genuinely "
            "available; otherwise remain until those safeguards exist. No illegality decides the case, so proportionality, "
            "continuity and compassion are weighted. Steelman: any absence during resumed rain may create a fatal command "
            "gap. Clear authority limits, check-ins and immediate return triggers convert that objection into design "
            "conditions.\n\n"
            "Implementation: obtain senior authorisation, issue written delegation, publish the command arrangement "
            "internally, preserve existing triage criteria and define escalation triggers. Residual risk: deputy error or "
            "sudden deterioration survives; Vijay should maintain check-ins, return on trigger and personally lead an "
            "after-action review of decisions taken during the absence."
        ),
    ),
    _pyq(
        2025,
        (
            "Neutral routing of GS-IV Q9: PWD Secretary Subash holds confidential road-alignment "
            "information sought by his real-estate businessman son, while a Minister also signals "
            "that a relative's company should receive favourable treatment."
        ),
        20,
        (
            "Neutral demand verified against books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, "
            "page 7. The local official paper and canonical Basic treatment control details."
        ),
        (
            "Facts: Subash faces two linked improprieties: family demand for privileged information and ministerial "
            "pressure favouring a connected company. Stakeholders: landowners, bidders, taxpayers, the son and nephew, "
            "PWD staff, the Minister, Subash and public trust. Constraints: confidential information cannot be shared; "
            "tender and land decisions must use lawful authority and objective criteria.\n\n"
            "Options: disclose selectively; refuse privately but continue alone; transfer the whole responsibility "
            "without explanation; or record both approaches, refuse disclosure, declare the family connection, recuse "
            "where that connection touches the decision, and route evaluation through an untainted committee using "
            "published criteria. Private refusal leaves pressure undocumented; unexplained transfer weakens accountability.\n\n"
            "Decision: use the conflict sequence and written-order response together. Legality and conflict are hard "
            "thresholds, so family loyalty, secrecy assurances or political convenience cannot outweigh them. Steelman: "
            "formal escalation may damage working relations and delay a strategic project. Immediate committee-based "
            "routing and a concise professional record preserve both speed and integrity.\n\n"
            "Implementation: secure alignment data, restrict access, seek written confirmation of improper directions, "
            "notify the competent superior or vigilance authority and audit communications and bid evaluation. Residual "
            "risk: proxies may still trade on leaked information or influence specifications. An independent procurement "
            "and land-acquisition review should monitor access logs, criteria and beneficial-interest declarations."
        ),
    ),
    _pyq(
        2025,
        (
            "Neutral routing of GS-IV Q10: engineer Rajesh faces an urgent culvert repair "
            "whose true cost exceeds delegated financial power, and a contractor proposes splitting "
            "the work to avoid superior sanction."
        ),
        20,
        (
            "Neutral demand verified against books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, "
            "pages 8-9. Exact monetary and procedural facts must be checked in the official paper."
        ),
        (
            "Facts: public safety requires urgent repair, but the genuine requirement exceeds Rajesh's delegated "
            "authority and the contractor proposes artificial splitting. Stakeholders: commuters, nearby residents, "
            "contractors, the superior sanctioning authority, audit and Rajesh. Constraints: urgency is real; evading "
            "delegation is impermissible; only technically separable emergency work may be considered within existing "
            "power under the applicable procedure.\n\n"
            "Options: split the same requirement; wait passively for normal sanction; undertake the full repair without "
            "authority; or record the danger, refer the full estimate urgently and execute only independently justified "
            "temporary stabilisation within lawful power while the permanent work is approved. Artificial splitting "
            "fails the legality and propriety threshold. Passive delay disregards foreseeable harm.\n\n"
            "Decision: choose the phased lawful response only if engineering evidence establishes genuinely separate "
            "stabilisation. Public interest and proportionality then control among lawful options. Steelman: phasing may "
            "itself disguise splitting. Independent technical reasons, superior notice and later audit must therefore "
            "precede execution.\n\n"
            "Implementation: send the full estimate and safety report immediately, document scope boundaries, use no "
            "contractor-designed paperwork, communicate temporary restrictions and seek expedited sanction. Residual "
            "risk: temporary work may fail or be perceived as evasion; the superior engineer should approve monitoring, "
            "inspect milestones and require internal audit before closure."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        (
            "Explain why hard constraints should be mapped before options are generated in a "
            "GS-IV case study."
        ),
        (
            "Hard constraints convert an ethical narrative into an administratively realistic decision. They "
            "include legality, delegated authority, jurisdiction, time, information, resources and institutional "
            "capacity. If a district officer lacks statutory power, an attractive promise cannot become a valid "
            "option merely because it appears compassionate.\n\n"
            "The correct sequence is elimination before balancing. An unlawful disclosure, a conflicted decision "
            "or expenditure beyond delegated power is removed first. The surviving courses can then be compared "
            "through public interest, proportionality, transparency and compassion. This prevents candidates from "
            "wasting words evaluating impossible choices.\n\n"
            "Constraint mapping also improves hybrid design. An engineer may not sanction an entire urgent work, "
            "yet may lawfully secure a genuinely separable temporary stabilisation while referring the permanent "
            "repair upward. Thus constraints do not always paralyse action; they define the lawful space within "
            "which practical wisdom operates. A high-quality answer names the binding constraint, the competent "
            "authority and the feasible route around delay without evasion."
        ),
    ),
    _original(
        10,
        (
            "Distinguish hard-threshold checks from weighted checks in ethical case analysis."
        ),
        (
            "Hard-threshold checks determine whether an option may remain under consideration. Legality is the "
            "clearest example: expected welfare cannot authorise an unlawful act. A genuine conflict of interest "
            "is similarly near-disqualifying; the officer must disclose and recuse rather than claim personal "
            "objectivity.\n\n"
            "Weighted checks compare options that survive. Public interest, proportionality, transparency and "
            "compassion can conflict. During triage, maximising lives saved may pull against priority to the most "
            "vulnerable. The candidate must state which factor is decisive in that context and protect the weaker "
            "factor through safeguards, review or communication.\n\n"
            "The distinction produces a disciplined sequence: identify conflicts and legality; remove impermissible "
            "choices; apply moral theories and weighted checks to lawful alternatives; choose; then answer the "
            "strongest objection. Treating every consideration as equal invites vague balancing and may imply that "
            "sufficient benefit can purchase legality. Treating every value as absolute, conversely, prevents reasoned "
            "choice. Ethical maturity lies in firm thresholds followed by explicit, evidence-based weighting."
        ),
    ),
    _original(
        15,
        (
            "Show how nested-dilemma decomposition and steelmanning improve a complex case-study answer."
        ),
        (
            "Nested-dilemma decomposition prevents one dramatic fact from swallowing the rest of the case. The "
            "2025 Vijay-type disaster problem contains personal grief versus public duty, continuity and fairness "
            "of relief allocation, and honest communication versus panic control. Each tension should receive a "
            "compact independent pass through legality, public interest, proportionality, transparency and compassion "
            "before the results are integrated.\n\n"
            "The method avoids muddled phrases such as balance both sides. Vijay's personal dilemma may support a "
            "brief authorised absence; the allocation dilemma still requires the deputy to retain published triage "
            "criteria; the communication dilemma requires verified, calibrated updates. Separate resolutions therefore "
            "become one coherent operational plan.\n\n"
            "Steelmanning then tests the plan against its strongest credible objection. The serious objection is not "
            "that family duty is irrelevant, but that any command gap during renewed danger could cost lives. A mature "
            "answer accepts this risk and makes competent written delegation, scheduled contact and immediate-return "
            "triggers conditions of the decision.\n\n"
            "The two devices serve different functions: decomposition clarifies what must be decided, while steelmanning "
            "tests whether the selected response survives informed criticism. Both must remain proportionate to the "
            "word limit; artificial sub-dilemmas and repeated counter-arguments create indecision rather than depth."
        ),
    ),
    _original(
        15,
        (
            "Evaluate the written-order response and ethical-dissent ladder as safeguards against "
            "improper administrative pressure."
        ),
        (
            "Improper oral pressure is dangerous because it seeks compliance without accountability. The officer "
            "should record the instruction, seek written confirmation and place the legal, technical and ethical "
            "objection on the official record. This protects institutional memory, fixes responsibility and demonstrates "
            "independent professional judgment. The officer should continue lawful work while referral is pending unless "
            "the act would itself be unsafe or unlawful.\n\n"
            "If the pressure persists, dissent should climb proportionately: competent internal reporting; an independent "
            "internal vigilance, audit or ethics tier; an authorised regulator, ombudsman or external authority; and "
            "public disclosure only when serious continuing harm and failed lawful alternatives justify that last step. "
            "When the normal superior is implicated, the compromised rung may be skipped, but evidence and lawful purpose "
            "remain essential.\n\n"
            "The strongest objection is that formal recording can provoke retaliation or administrative delay. Therefore "
            "the response should be concise, factual, time-bound and supported by secure evidence and anti-retaliation "
            "measures where available. Resignation is not the automatic next rung: it is justified only when resistance "
            "is exhausted and departure protects public interest better than continued principled service.\n\n"
            "Together, written reasons and graduated escalation turn private conscience into accountable institutional "
            "action without confusing courage with impulsive leakage or theatrical exit."
        ),
    ),
    _original(
        20,
        (
            "A district faces severe water scarcity among households, hospitals, farmers and industry. "
            "Apply the complete case-study architecture to design an ethical allocation response."
        ),
        (
            "Facts and dilemma: available water cannot meet all claims, while immediate survival needs and longer-term "
            "livelihoods conflict. Stakeholders include households, hospitals, vulnerable settlements, farmers, workers, "
            "industry, local bodies, ecosystems and future users. Constraints are the actual reservoir level, drinking-water "
            "law and policy, conveyance losses, time, uncertain rainfall and limited enforcement capacity.\n\n"
            "Options are: retain historical quotas; use first-come political bargaining; impose an undifferentiated cut; "
            "or publish a tiered emergency allocation. The tiered course should protect minimum drinking, sanitation and "
            "critical-care needs first; reserve ecological and fire-safety minima; then distribute livelihood and industrial "
            "supplies through transparent necessity, efficiency and vulnerability criteria, with recycling and temporary "
            "restrictions.\n\n"
            "Evaluation begins with legality and non-discrimination as thresholds. Consequentialism supports preventing "
            "death and maintaining essential services; duty ethics protects equal dignity and a basic minimum; proportionality "
            "rejects both unrestricted consumption and blanket closure. The decisive weighted considerations are urgency, "
            "vulnerability and avoidable harm. Steelman: prioritising urban hospitals and households may ruin farms and jobs. "
            "The plan therefore needs crop-saving rotations, fodder and income support, recycled industrial water and rapid "
            "loss reduction rather than simply transferring all scarcity to rural users.\n\n"
            "Decision and implementation: constitute a multi-stakeholder drought cell, publish daily availability and criteria, "
            "meter bulk users, repair leaks, enforce restrictions uniformly and create an expedited appeal route. Communicate "
            "uncertainty honestly and revise allocations at fixed hydrological triggers.\n\n"
            "Residual risk equals severe inherent scarcity minus conservation, prioritisation and augmentation controls, plus "
            "forecast and enforcement uncertainty. Capture by powerful users may remain. The district drought cell should publish "
            "allocation logs, commission independent audit and review impacts on vulnerable groups every week."
        ),
    ),
    _original(
        20,
        (
            "A public-sector quality officer discovers that a safety-critical product failed tests, "
            "but senior management orders clearance to avoid losses and threatens retaliation. Decide."
        ),
        (
            "Facts and dilemma: a failed safety result conflicts with management's commercial and reputational interests, "
            "and the officer faces personal retaliation. Stakeholders include consumers, workers, distributors, shareholders, "
            "the regulator, honest colleagues, management and the officer's family. Constraints include mandatory safety standards, "
            "release deadlines, evidence custody, the officer's limited authority and the possibility that the ordinary reporting "
            "line is compromised.\n\n"
            "Options are: alter or ignore the result; delay silently; resign without reporting; or preserve the original test, "
            "record the oral direction, stop clearance within lawful authority and escalate with evidence to independent quality "
            "governance and, if required, the competent regulator. The first option fails legality, professional duty and public "
            "interest. Silent delay leaves the hazard active. Immediate resignation removes the witness and does not protect consumers.\n\n"
            "Decision: choose evidence preservation, written refusal and graduated escalation. Deontology requires fidelity to safety "
            "and truth; consequences favour preventing mass harm; virtue ethics supports courage disciplined by prudence. Steelman: "
            "a false or non-representative failed test could destroy the enterprise and jobs. Therefore an independent confirmatory "
            "test may proceed under controlled custody, but the product must remain quarantined until the competent authority decides; "
            "tests cannot be repeated selectively until a desired result appears.\n\n"
            "Implementation: timestamp and secure samples and raw data, request written confirmation, notify the independent quality "
            "committee, define a short regulator trigger, protect affected staff and prepare a truthful recall plan if distribution "
            "occurred. Communicate verified risk without sensationalism.\n\n"
            "Residual risk includes retaliation, evidence tampering and supply shortage. The regulator or independent quality head "
            "should control access logs, witness the retest, monitor the officer's employment treatment and audit corrective action. "
            "Resignation becomes defensible only if all lawful channels fail and continued office would require personal falsification."
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
        "1. Eight-element case-study rail",
        "eight-stage-rail",
        (
            "Facts: given versus assumed",
            "Stakeholders: direct and silent",
            "Constraints: hard bounds",
            "Options: three or more",
            "Evaluation: theories and checks",
            "Decision: decisive reason",
            "Implementation: actor and message",
            "Residual risk: monitor and review",
        ),
        "A case answer is a complete decision process, not a moral reaction.",
        "Use as the universal opening architecture.",
    ),
    _panel(
        "2. Constraint gate before option design",
        "constraint-funnel",
        (
            "Legality defines permission",
            "Delegation defines authority",
            "Jurisdiction defines forum",
            "Time defines urgency",
            "Information defines confidence",
            "Resources define capacity",
            "Safety defines tolerable exposure",
            "Survivors become real options",
        ),
        "Impossible or unlawful proposals should never enter later balancing.",
        "Use before listing options in every administrative case.",
    ),
    _panel(
        "3. Six-check evaluation matrix",
        "threshold-weight-matrix",
        (
            "Conflict: hard threshold",
            "Legality: hard threshold",
            "Public interest: weighted",
            "Proportionality: weighted",
            "Transparency: weighted",
            "Compassion: weighted",
            "Long-term effects: projected",
            "Decisive weight: stated",
        ),
        "Eliminate first, weigh second and explain what controlled the choice.",
        "Use for the ethical-evaluation element.",
    ),
    _panel(
        "4. Conflict-of-interest resolution sequence",
        "four-step-control-chain",
        (
            "Detect personal-interest link",
            "Disclose connection in writing",
            "Recuse from the decision",
            "Refer to untainted authority",
            "State objective criteria",
            "Apply criteria consistently",
            "Preserve the scoring trail",
            "Publish or defend the rationale",
        ),
        "Personal honesty cannot substitute for an unconflicted process.",
        "Use in procurement, licensing and privileged-information cases.",
    ),
    _panel(
        "5. Nested dilemma and steelman loop",
        "decompose-test-recombine",
        (
            "Identify dilemma one",
            "Run compact ethical checks",
            "Identify dilemma two",
            "Run compact ethical checks",
            "Recombine compatible decisions",
            "State strongest objection",
            "Absorb valid objection",
            "Confirm or revise decision",
        ),
        "Decomposition clarifies the problem; steelmanning tests the solution.",
        "Use for dense cases with multiple genuine conflicts.",
    ),
    _panel(
        "6. Residual-risk closing formula",
        "risk-control-equation",
        (
            "Name inherent danger",
            "List preventive controls",
            "Test control weakness",
            "Add uncertainty exposure",
            "State surviving risk",
            "Choose monitoring indicator",
            "Name accountable authority",
            "Set review or trigger date",
        ),
        "Residual risk equals inherent risk reduced by controls, with uncertainty retained.",
        "Use as the final paragraph of every solved case.",
    ),
    _panel(
        "7. Written-order response to pressure",
        "record-escalate-continue",
        (
            "Identify improper oral direction",
            "Record its substance promptly",
            "Seek written confirmation",
            "State professional objection",
            "Preserve supporting evidence",
            "Refer through proper hierarchy",
            "Continue lawful substantive duty",
            "Escalate impropriety if persistent",
        ),
        "Writing fixes responsibility and converts private resistance into institutional accountability.",
        "Use for ministerial, superior and corporate pressure.",
    ),
    _panel(
        "8. Whistleblowing and dissent ladder",
        "four-rung-ladder",
        (
            "Preserve credible evidence",
            "Report to competent superior",
            "Skip a compromised recipient",
            "Use independent internal tier",
            "Use authorised external channel",
            "Protect identity and safety",
            "Consider public disclosure last",
            "Review retaliation and follow-up",
        ),
        "Escalate only as far as failure and continuing harm require.",
        "Use when loyalty, secrecy and public interest conflict.",
    ),
    _panel(
        "9. Resignation decision test",
        "last-resort-gate",
        (
            "Record personal non-participation",
            "Test internal resistance",
            "Test independent escalation",
            "Assess continuing public influence",
            "Assess complicity from remaining",
            "Assess impact of departure",
            "Define the resignation trigger",
            "Resign only if net protection rises",
        ),
        "Resignation is ethical only when it protects the public better than principled service.",
        "Use whenever an option list includes exit from office.",
    ),
    _panel(
        "10. Scarce-resource triage cycle",
        "criteria-review-cycle",
        (
            "Measure actual scarcity",
            "Protect lawful basic minima",
            "Choose relevant criteria",
            "Publish criteria in advance",
            "Add vulnerability safeguard",
            "Record each allocation",
            "Provide rapid review route",
            "Revise as conditions change",
        ),
        "Transparent criteria are ethically superior to hidden case-by-case discretion.",
        "Use for beds, staff, water, relief and compensation.",
    ),
    _panel(
        "11. Domain adaptation map",
        "cross-domain-matrix",
        (
            "Administration: lawful authority",
            "Corporate: stakeholder duty",
            "Research: consent and truth",
            "Health: triage and dignity",
            "Police: force and due process",
            "Environment: future generations",
            "Technology: privacy and harm",
            "Disaster: continuity and compassion",
        ),
        "The architecture stays constant while standards, institutions and evidence change.",
        "Use to transfer the method without copying remedies blindly.",
    ),
    _panel(
        "12. Time-bound examiner answer spine",
        "answer-clock",
        (
            "Minute one: demand and facts",
            "Minute two: stakeholders",
            "Minute three: constraints",
            "Minutes four-six: options",
            "Minutes seven-ten: evaluation",
            "Minutes eleven-twelve: decision",
            "Minutes thirteen-fourteen: execution",
            "Minute fifteen: residual risk",
        ),
        "Compress every element; do not sacrifice the ending to an oversized introduction.",
        "Use as a planning clock for a twenty-mark case.",
    ),
)


CURRENT_ANCHOR = {
    "title": "Current official anchor: Amrit Gyaan Kosh and case-based governance learning",
    "verified_facts": (
        "The Capacity Building Commission describes Amrit Gyaan Kosh as a repository that captures and curates governance best practices as India-centric case studies for officials across Union, State, municipal and panchayat levels.",
        "The official Commission page states that each case study has precise learning objectives intended to improve problem-solving and evidence-based decision-making under Mission Karmayogi.",
        "The Commission's launch note says the portal provides access to case studies and supporting materials on iGOT and seeks to institutionalise experiential, case-based learning in governance.",
    ),
    "administrative_link": (
        "The official initiative supports the central teaching claim of Topic 22: structured cases build "
        "judgment by requiring officials to identify facts, constraints and stakeholders, compare feasible "
        "actions, justify a decision and learn from implementation. It is a training linkage, not evidence "
        "that the eight-element UPSC answer architecture is an officially mandated government template."
    ),
    "limit": (
        "The official pages establish the repository's purpose and case-based pedagogy. They do not state "
        "that every iGOT course uses one uniform simulation design, nor do they endorse a single UPSC model "
        "answer. Specific course or case claims should be verified on the platform before citation."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://cbc.gov.in/amrit-gyaan-kosh",
    "https://cbc.gov.in/index.php/mos-dr-jitendra-singh-inaugurated-advanced-case-writing-and-teaching-workshop-and-launched-amrit",
)


SOURCE_CAVEAT = (
    "Topic 22 owns the complete method for GS-IV case studies: facts, stakeholders, constraints, "
    "realistic options, ethical evaluation, decision, implementation and communication, and residual-risk "
    "mitigation. The six-check framework is a synthesis heuristic, not an official UPSC algorithm or a "
    "promise of one uniquely correct answer. Legality is normally a hard threshold; conflict of interest "
    "is near-disqualifying and ordinarily triggers written disclosure, recusal, referral to an untainted "
    "authority and objective criteria. Public interest, proportionality, transparency and compassion are "
    "weighted considerations whose relative importance must be explained. Moral theories supplement rather "
    "than replace the six checks. Nested dilemmas should be separated only when analytically genuine. A "
    "steelman is the strongest credible objection, not a ceremonial weak counterpoint. Residual risk means "
    "the specific danger remaining after controls, with a named monitor and review mechanism; its formula "
    "is a reasoning aid, not literal arithmetic. Improper oral directions should be converted into a written "
    "record with the officer's professional objection and lawful escalation. Ethical dissent usually moves "
    "through internal, independent internal, authorised external and last-resort public channels; a compromised "
    "recipient may be skipped. Public disclosure can carry confidentiality, safety and legal risks. Resignation "
    "is an evaluated last resort after resistance and escalation, not an automatic symbol of integrity. Triage "
    "requires relevant published criteria, an explicit welfare-equity trade-off, records, review and adaptation. "
    "The architecture transfers across domains, but each answer must identify the governing legal authority, "
    "technical standard and competent institution; Topic 22 does not replace the detailed law in Topics 14-21 "
    "or named-case evidence in Topic 23. Official local UPSC papers control question wording. PYQ entries marked "
    "neutral routing deliberately condense scenarios because some scans have imperfect OCR; they must not be "
    "presented as verbatim quotations. The canonical Basic treatment controls the 2018-2025 routing and worked "
    "method, while the Advanced treatment adds weighting, stress testing and residual-risk refinement. The "
    "Capacity Building Commission pages support a current case-based-learning anchor but do not make this exact "
    "answer framework an official Mission Karmayogi requirement."
)


REGISTER_SUPPLEMENT = (
    "### CASE-STUDY METHOD AND ANSWER ARCHITECTURE RAPID REGISTER\n\n"
    "#### 1. THE EIGHT-ELEMENT NON-NEGOTIABLE SPINE\n\n"
    "1. **Facts:** one-line dilemma; separate given facts from assumptions and unknowns.\n"
    "2. **Stakeholders:** direct, indirect and silent parties, including future generations and institutional trust.\n"
    "3. **Constraints:** legality, delegation, jurisdiction, time, information, resources, capacity and safety.\n"
    "4. **Options:** at least three realistic courses; include a hybrid or sequenced course where useful; give a concrete pro and con.\n"
    "5. **Ethical evaluation:** moral theories plus six checks; eliminate threshold failures before balancing.\n"
    "6. **Decision:** select one course, name the decisive reason and answer the strongest objection.\n"
    "7. **Implementation and communication:** immediate and later steps, actors, records and audiences.\n"
    "8. **Residual risk:** name surviving danger, monitor, accountable authority and review trigger.\n\n"
    "#### 2. HARD CONSTRAINTS BEFORE OPTIONS\n\n"
    "- An option outside lawful authority or jurisdiction is not a real option.\n"
    "- A hard time limit does not legalise evasion; it may justify a lawful emergency or phased route.\n"
    "- Information gaps should produce verification steps, not invented certainty.\n"
    "- Resource and capacity limits must be costed explicitly.\n"
    "- State what the protagonist can decide, what must be delegated and what must be referred.\n"
    "- Best sequence: constraint gate -> surviving options -> ethical comparison.\n\n"
    "#### 3. SIX CHECKS AND THEIR WEIGHT\n\n"
    "- **Conflict of interest:** near-hard threshold; personal confidence does not cure structural bias.\n"
    "- **Legality:** normally a hard threshold; benefit cannot purchase lawful authority.\n"
    "- **Public interest:** broader and less vocal stakeholders count.\n"
    "- **Proportionality:** avoid both under-reaction and over-reaction.\n"
    "- **Transparency:** could reasons be recorded and defended under scrutiny?\n"
    "- **Compassion and long-term consequence:** dignity now plus foreseeable effects later.\n"
    "- Apply deontology, consequentialism and virtue ethics to surviving options.\n"
    "- State which weighted check is decisive and how the others are protected.\n\n"
    "#### 4. DISCLOSE -> RECUSE -> REFER -> PUBLISH\n\n"
    "- Detect the personal, family, financial or reputational connection.\n"
    "- Disclose it in writing before the decision.\n"
    "- Recuse from deciding, chairing and influencing that specific matter.\n"
    "- Refer to a genuinely untainted superior, colleague or committee.\n"
    "- Apply pre-announced, objective criteria and preserve the evaluation trail.\n"
    "- Publish or consistently communicate the defensible rationale where rules permit.\n"
    "- Anchor cases: 2024 Sneha and 2025 Subash.\n\n"
    "#### 5. NESTED DILEMMAS AND STEELMANNING\n\n"
    "- Decompose only genuinely independent tensions.\n"
    "- Give each sub-dilemma a mini threshold and weighted-check pass.\n"
    "- Recombine the resulting decisions into one operational course.\n"
    "- State the strongest informed objection to the chosen course.\n"
    "- Defeat it with reasons or redesign implementation to absorb its valid concern.\n"
    "- One strong objection is enough; repeated counterpoints create indecision.\n"
    "- Vijay example: grief versus duty; allocation fairness; transparency versus calm.\n\n"
    "#### 6. RESIDUAL-RISK FORMULA\n\n"
    "- Working expression: **residual risk = inherent risk - effective controls + uncertainty/control failure exposure**.\n"
    "- The expression is qualitative, not a claim that ethics is arithmetic.\n"
    "- Name the surviving risk specifically: retaliation, misclassification, capture, execution error or public distrust.\n"
    "- Choose an indicator, review mechanism and trigger.\n"
    "- Name the office or person responsible; avoid passive claims that it will be monitored.\n"
    "- Close with qualified confidence, never with a claim that all risk has vanished.\n\n"
    "#### 7. WRITTEN-ORDER RESPONSE TO ORAL PRESSURE\n\n"
    "- Record the substance and date of the oral instruction.\n"
    "- Seek written confirmation from the person giving it.\n"
    "- Place the legal, technical and ethical objection on record.\n"
    "- Preserve the supporting evidence and continue lawful substantive duty.\n"
    "- Refer through the normal hierarchy; use vigilance or oversight if the pressure itself is improper.\n"
    "- Written reasons protect both accountability and the officer's bona fides.\n\n"
    "#### 8. WHISTLEBLOWING AND ETHICAL DISSENT\n\n"
    "- Rung 1: competent internal reporting with evidence.\n"
    "- Rung 2: independent internal authority such as vigilance, audit or ethics mechanism.\n"
    "- Rung 3: authorised regulator, ombudsman or lawful external authority.\n"
    "- Rung 4: public disclosure only as a genuine last resort against serious continuing harm.\n"
    "- Skip a recipient who is implicated, but do not skip evidence, necessity and lawful purpose.\n"
    "- Protect identity, custody, safety and access records.\n"
    "- A complaint starts verification; it does not establish guilt.\n\n"
    "#### 9. RESIGNATION TEST\n\n"
    "- Have written dissent and lawful escalation been exhausted or become impossible?\n"
    "- Does staying preserve a principled internal safeguard?\n"
    "- Would leaving reduce complicity or merely remove resistance?\n"
    "- Would departure improve the public outcome rather than only personal moral comfort?\n"
    "- Define the trigger: compelled personal execution, signature or legitimisation of unresolved wrongdoing.\n"
    "- Rajesh Kumar 2020 is the classic option-evaluation anchor.\n\n"
    "#### 10. TRIAGE AND SCARCE RESOURCES\n\n"
    "- Measure actual scarcity; protect lawful and dignity-based minima.\n"
    "- Publish relevant criteria before individual allocation where time permits.\n"
    "- State the trade-off: aggregate welfare, urgency, survivability, vulnerability or worst-off priority.\n"
    "- Add an equity audit so metrics do not become mechanically discriminatory.\n"
    "- Record who applied which criterion and why.\n"
    "- Provide a rapid review or grievance route.\n"
    "- Revise criteria as resources and emergency conditions change.\n"
    "- Public and private institutions share the ethical floor even when operational powers differ.\n\n"
    "#### 11. DOMAIN ADAPTATION\n\n"
    "- **Procurement:** delegation, conflict, objective criteria and audit trail.\n"
    "- **Disaster:** command continuity, triage, communication and succession risk.\n"
    "- **Corporate environment:** stakeholder duty, verified transition and rebound risk.\n"
    "- **Research:** informed consent, vulnerable participants, complete data and ethics review.\n"
    "- **Policing:** legality, proportionality, evidence and due process for all parties.\n"
    "- **Privacy:** lawful purpose, necessity, minimisation and review.\n"
    "- **Workplace harassment:** safe complaint route, unbiased inquiry and anti-retaliation.\n"
    "- **Border or refugee cases:** separate humanitarian need from verified security risk; avoid blanket extremes.\n\n"
    "#### 12. 2018-2025 PYQ ROUTES\n\n"
    "- **2018:** privileged policy information and ministerial conflict -> refuse benefit, record, recuse where required, objective route.\n"
    "- **2019:** attacked rescue team -> mission continuity plus proportionate team safety and community liaison.\n"
    "- **2020:** welfare re-appropriation -> written dissent, oversight escalation, resignation last.\n"
    "- **2021:** hospital staff scarcity -> published triage criteria, equity safeguard and review cycle.\n"
    "- **2022:** mining-mafia journalist -> preserve evidence, skip captured rung, lawful external escalation.\n"
    "- **2023:** SRTC political pressure -> neutrality, written clarification, independent vigilance route.\n"
    "- **2024:** AI emissions, Sneha conflict and trial integrity -> domain-specific use of the same architecture.\n"
    "- **2025:** Vijay, Subash and Rajesh -> nested duties, conflict controls and lawful urgent procurement.\n\n"
    "#### 13. TIME MANAGEMENT FOR A TWENTY-MARK CASE\n\n"
    "- Minute 1: read the directive and frame the dilemma.\n"
    "- Minute 2: facts, stakeholders and constraints in compact bullets.\n"
    "- Minutes 3-6: generate three or four real options with short pros and cons.\n"
    "- Minutes 7-10: thresholds, moral theories and weighted checks.\n"
    "- Minutes 11-12: decision and decisive reason.\n"
    "- Minutes 13-14: implementation, communication and steelman response.\n"
    "- Minute 15: residual risk, monitor and review trigger.\n"
    "- Compress every element; never spend the answer retelling the narrative.\n\n"
    "#### 14. EXAMINER TRAPS\n\n"
    "- One asserted correct option without alternatives.\n"
    "- Vague balancing without a decision.\n"
    "- Treating compassion as permission for illegality.\n"
    "- Treating all six checks as equally weighted.\n"
    "- Confusing disclosure with completed recusal.\n"
    "- Jumping directly to media exposure or resignation.\n"
    "- Giving a remedy outside the protagonist's authority.\n"
    "- Omitting implementation, communication or residual risk.\n"
    "- Using a public-sector remedy unchanged in a clinical, corporate or research setting.\n"
    "- Claiming the chosen option removes all risk.\n\n"
    "#### 15. EIGHT-LINE ANSWER RECALL\n\n"
    "1. What is verified and what is the dilemma?\n"
    "2. Who is affected, including silent stakeholders?\n"
    "3. What cannot legally or practically be done?\n"
    "4. What three or four real courses remain?\n"
    "5. Which fail thresholds, and how do the survivors compare?\n"
    "6. What will I choose, and why does the strongest objection not defeat it?\n"
    "7. Who will do what, record what and communicate what?\n"
    "8. What can still go wrong, who monitors it and when is review triggered?\n\n"
    "> **Final thesis:** A high-scoring GS-IV case answer is a bounded administrative decision, "
    "not an emotional essay. Verify facts, map visible and silent stakeholders, state hard "
    "constraints, compare realistic options, eliminate illegality and conflict, weigh public "
    "interest with proportionality, transparency and compassion, decide clearly, implement through "
    "named actors and communication, and close by owning the residual risk."
)
