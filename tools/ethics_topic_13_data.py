"""Learner-v2 source data: Ethics Topic 13, Emerging Ethics."""


SESSION_TITLES = (
    "Emerging ethics: visual foundation and essential vocabulary",
    "How technology and environmental dilemmas arise and are resolved",
    "Indian applications, high-yield facts and close-option traps",
    "PYQ entry points, current anchors and Mains theses",
    "Digital exclusion, privacy, Puttaswamy and phased DPDP commencement",
    "Selectable evidence units for technology and environmental answers",
    "Directive decoding and mark-scaled answer architecture",
    "Environmental orientations, principles and the Vellore boundary",
    "Clausewitz routing: separating environmental ethics from war ethics",
    "Study links and complete recent-historical PYQ ownership",
)


SESSION_GROUPS = (
    ("1", "2"),
    ("3",),
    ("4", "5", "6"),
    ("7", "8", "9", "10"),
    ("11", "11a"),
    ("12",),
    ("13",),
    ("14",),
    ("15",),
    ("16",),
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
        "AI is decision support, not an accountability substitute",
        "Administrative AI can improve speed, consistency and pattern detection, but it should remain a decision-support input whose recommendation is tested against law, context and reasons by an answerable public official.",
        "A welfare department treats a model score as conclusive and refuses to identify any responsible officer. Which principle has been displaced?",
        "A licensing officer checks an AI risk flag against the record and gives independent reasons. Which proper role for AI is illustrated?",
        "AI decision quality and human agency",
    ),
    _mcq(
        "Bias can enter data, design, deployment and feedback",
        "AI unfairness may originate in unrepresentative data, labels and proxy variables, design objectives, unequal deployment conditions, or feedback loops that turn earlier skewed outputs into future training evidence.",
        "A fraud model trained only on urban cases repeatedly misclassifies rural claims. At which bias stage should the diagnosis begin?",
        "A policing model sends more patrols where it earlier predicted risk, then treats the resulting arrests as proof. Which loop is operating?",
        "AI decision quality and human agency",
    ),
    _mcq(
        "Explainability must be useful to the affected person",
        "Explainability in high-stakes administration requires an intelligible account of the decisive factors, limits and review route, not merely disclosure of source code or a technical statement that only specialists can understand.",
        "A pension applicant receives only a model version number after rejection. Which ethical safeguard remains unsatisfied?",
        "An agency states the decisive data, rule, uncertainty and appeal route in plain language. Which concept is being operationalised?",
        "AI decision quality and human agency",
    ),
    _mcq(
        "Human oversight must be meaningful",
        "Human oversight is meaningful only when the reviewer has competence, time, authority, relevant information and freedom to depart from an automated recommendation; ceremonial approval preserves neither judgment nor accountability.",
        "A junior clerk must approve every model output within ten seconds and cannot alter it. Why is the human-in-the-loop claim hollow?",
        "A medical board can pause, investigate and reverse a high-risk model recommendation. Which form of oversight is present?",
        "AI decision quality and human agency",
    ),
    _mcq(
        "Accountability requires an auditable responsibility chain",
        "Algorithmic accountability assigns named responsibility across procurer, developer, deploying department and final decision-maker, while logs, impact assessment, audit trails and incident reporting make conduct reviewable before and after harm.",
        "A department blames a vendor after an automated exclusion although no official owned validation. Which governance failure is central?",
        "A procurement contract preserves logs, assigns incident duties and permits independent audit. Which accountability architecture is strengthened?",
        "AI safeguards and operational control",
    ),
    _mcq(
        "Contestability gives affected persons an effective remedy",
        "Contestability means a person can know that automation materially influenced a decision, challenge relevant data and reasoning, obtain timely human reconsideration, and secure correction or remedy without prohibitive cost.",
        "A scholarship applicant can submit corrected records but no one may reconsider the model result. Which element remains absent?",
        "A citizen receives notice, a simple appeal channel and reasoned human review. Which safeguard is demonstrated?",
        "AI safeguards and operational control",
    ),
    _mcq(
        "Automation bias and de-skilling are institutional risks",
        "Automation bias is the tendency to over-trust machine output, while de-skilling is the gradual erosion of human expertise through disuse; both require calibrated reliance, training and periodic unaided judgment.",
        "Experienced inspectors stop examining unusual cases because the dashboard is usually right. Which paired risks arise?",
        "A department requires periodic manual sampling and records justified departures from model advice. Which risks is it trying to control?",
        "AI safeguards and operational control",
    ),
    _mcq(
        "Hallucination and reliability require verification",
        "Generative AI may produce fluent but false citations, facts or explanations, so reliability demands source verification, uncertainty disclosure, domain testing and prohibition of unverified output as the sole basis of consequential decisions.",
        "An officer files a disciplinary order using model-generated cases without checking them. Which reliability failure is decisive?",
        "A legal cell verifies every generated citation against official records before use. Which control addresses hallucination?",
        "AI safeguards and operational control",
    ),
    _mcq(
        "Procurement must include red-teaming and monitoring",
        "Responsible AI procurement specifies the public purpose, representative testing, security and bias red-teaming, documentation, audit access, change control, incident response, continuing performance monitoring and an exit route.",
        "A vendor passes one demonstration and then changes its model without notice. Which procurement controls were missing?",
        "A department tests adversarial cases before launch and monitors drift after deployment. Which lifecycle approach is illustrated?",
        "Digital public sphere and lifecycle governance",
    ),
    _mcq(
        "Deepfakes attack authenticity and public trust",
        "Deepfakes create an authenticity problem by making fabricated audio or video appear evidentially real; proportionate responses combine provenance signals, verification, rapid correction, platform process and due regard for lawful expression.",
        "A forged video of a district officer triggers panic before verification. Which ethical value is most directly attacked?",
        "Authorities preserve the original, verify provenance and issue a prompt correction without suppressing criticism. Which balanced response is shown?",
        "Digital public sphere and lifecycle governance",
    ),
    _mcq(
        "Social media combines misinformation, manipulation and privacy harms",
        "Social media dilemmas include falsehood, micro-targeted manipulation, addictive amplification, privacy invasion, cyberbullying and polarisation; speed and reach magnify harm, while blanket censorship can damage expression and democratic debate.",
        "A platform rewards inflammatory falsehood because engagement rises. Which design-linked ethical problem is present?",
        "A public agency counters a rumour with verified facts while protecting children's identities. Which competing values are being balanced?",
        "Digital public sphere and lifecycle governance",
    ),
    _mcq(
        "The digital divide is about capability, not connectivity alone",
        "Digital inclusion requires affordable access, devices, language and disability accessibility, literacy, assistance and an effective offline alternative; an online portal can otherwise convert administrative efficiency into substantive exclusion.",
        "A village has mobile coverage but elderly pensioners cannot navigate an English-only portal. Which divide persists?",
        "A service adds assisted access, local-language design and an offline channel. Which ethical principle is advanced?",
        "Digital public sphere and lifecycle governance",
    ),
    _mcq(
        "Privacy protects dignity, autonomy and contextual control",
        "Privacy is not secrecy alone: it protects dignity, decisional autonomy and a person's reasonable control over how information given in one context is collected, combined, inferred and used in another.",
        "A health database is reused for unrelated profiling because the facts were once disclosed voluntarily. Which understanding of privacy rejects this reasoning?",
        "An agency limits reuse to the stated service purpose and permits correction. Which underlying values are protected?",
        "Privacy and data governance",
    ),
    _mcq(
        "Puttaswamy requires the full proportionality inquiry",
        "A State privacy restriction should be tested for legality, legitimate aim, rational connection, necessity or least-restrictive means, proportionate balancing and procedural safeguards; a useful public objective alone does not complete the inquiry.",
        "A department cites convenience but identifies no law or narrower alternative before mass tracking. Which constitutional test is incomplete?",
        "A scheme has legal authority, a legitimate aim, narrow collection, safeguards and review. Which analytical framework supports assessment?",
        "Privacy and data governance",
    ),
    _mcq(
        "DPDP commencement is phased, not fully operational",
        "G.S.R. 843(E) commenced a specified immediate tranche on 13 November 2025; the Consent Manager tranche begins 13 November 2026, while core notice, consent, rights, fiduciary, Board and penalty provisions begin 13 May 2027.",
        "An answer says every DPDP duty was enforceable from November 2025. Which chronology corrects it?",
        "An administrator protects data ethically now while distinguishing future statutory duties. Which law-ethics distinction is shown?",
        "Privacy and data governance",
    ),
    _mcq(
        "Consent must be purpose-bound and security-backed",
        "Ethical data processing joins informed and revocable consent with purpose limitation, data minimisation, accuracy, retention limits and reasonable security; a clicked box cannot authorise indefinite collection or unrelated reuse.",
        "A benefits app collects contacts and location unrelated to eligibility under one bundled checkbox. Which safeguards fail?",
        "A service requests only necessary fields, explains use and deletes them when no longer needed. Which data ethic is applied?",
        "Privacy and data governance",
    ),
    _mcq(
        "AI has energy, water, hardware and e-waste costs",
        "AI's environmental footprint spans electricity for training and inference, water used in cooling and power generation, embodied impacts of hardware manufacture, mineral extraction, replacement cycles and electronic waste.",
        "A company reports renewable electricity but ignores cooling water and discarded accelerators. Why is its footprint account incomplete?",
        "A data centre measures operational energy, water, embodied hardware and e-waste. Which lifecycle view is demonstrated?",
        "Environmental responsibility across generations",
    ),
    _mcq(
        "Sustainable development is a two-generation bridge",
        "Sustainable development meets present needs without compromising future generations' ability to meet their own needs; it neither makes development absolute nor converts environmental protection into an automatic veto.",
        "A housing plan ignores ecosystem services because present welfare always prevails. Which principle corrects that one-sided claim?",
        "A project redesign protects livelihoods while retaining ecological capacity. Which bridging concept supports it?",
        "Environmental responsibility across generations",
    ),
    _mcq(
        "Intergenerational equity represents absent future citizens",
        "Intergenerational equity extends public interest across time by requiring present decision-makers to account for durable resource depletion, climate risk and ecological damage imposed on people unable to participate in today's choice.",
        "A government discounts irreversible groundwater loss because future residents cannot object. Which ethical duty is neglected?",
        "A policy applies a long time horizon and preserves ecological options. Which justice principle is operating?",
        "Environmental responsibility across generations",
    ),
    _mcq(
        "Precaution may guide high-stakes AI only by analogy",
        "Rio Principle 15 and Vellore are environmental authorities; their precaution logic may inform high-stakes AI by analogy where uncertain harm could be serious, but they are not binding Indian AI law.",
        "A note calls Vellore a directly enforceable AI statute. Which doctrinal limit must be restored?",
        "A department pilots and stress-tests an uncertain high-impact AI system before scale-up. Which analogous reasoning supports caution?",
        "Environmental responsibility across generations",
    ),
    _mcq(
        "Polluter-pays allocates prevention and remediation costs",
        "Polluter-pays requires the actor causing environmental harm to bear prevention, remediation and compensation costs rather than externalising them to affected communities or the public; it does not purchase permission to pollute.",
        "A factory pays a fee and claims unlimited discharge is now ethical. Which misunderstanding is present?",
        "A regulator requires cleanup, victim compensation and preventive upgrades from the polluter. Which principle is applied?",
        "Environmental justice and climate governance",
    ),
    _mcq(
        "Environmental justice tests distribution and voice",
        "Environmental justice asks who receives environmental benefits, who bears pollution, displacement and risk, and who has meaningful voice and remedy, with special attention to poor, tribal, nomadic and marginalised communities.",
        "A clean-energy project displaces a tribal community without consultation while distant users gain. Which justice lens reveals the burden?",
        "A clearance process includes affected communities, fair compensation and accessible remedy. Which ethical concern is addressed?",
        "Environmental justice and climate governance",
    ),
    _mcq(
        "Anthropocentric, biocentric and ecocentric reasons differ",
        "Anthropocentrism values nature chiefly for human interests, biocentrism recognises inherent worth in living beings, and ecocentrism values ecosystems and ecological processes as wholes; administrative reasoning should identify rather than conflate them.",
        "A wetland is protected solely for drinking-water recharge. Which orientation supplies the stated reason?",
        "A river's flow regime is protected as an interdependent ecological whole. Which orientation is most precise?",
        "Environmental justice and climate governance",
    ),
    _mcq(
        "CBDR-RC and EIA require differentiated, least-damaging choices",
        "CBDR-RC joins common climate responsibility with historical contribution and capability, while sensitive border projects require security-aware EIA, community consideration, classified handling where necessary, and the least ecologically damaging feasible alternative.",
        "A climate answer says developing states have no duties. Which differentiated principle rejects that conclusion?",
        "A border road uses a narrower alignment after rigorous assessment while protecting genuine security information. Which balanced method is shown?",
        "Environmental justice and climate governance",
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
            "GS-IV Q10: A big corporate house is engaged in manufacturing industrial chemicals on "
            "a large scale. It proposes to set up an additional unit. Many States rejected its "
            "proposal due to detrimental effect on the environment. But one State government "
            "acceded to the request and permitted the unit close to a city, brushing aside all "
            "opposition. The unit was set up 10 years ago and was in full swing till recently. The "
            "pollution caused by the industrial effluents was affecting the land, water and crops "
            "in the area. It was also causing serious health problems to human beings and animals. "
            "This gave rise to a series of agitations demanding the closure of the plant. In a "
            "recent agitation thousands of people took part, creating a law and order problem "
            "necessitating stern police action. Following the public outcry, the State government "
            "ordered the closure of the factory. The closure of the factory resulted in the "
            "unemployment of not only those workers who were engaged in the factory but also those "
            "who were working in the ancillary units. It also very badly affected those industries "
            "which depended on the chemicals manufactured by it. As a senior officer entrusted "
            "with the responsibility of handling this issue, how are you going to address it? "
            "(Answer in 250 words)"
        ),
        20,
        (
            "Exact full case verified against books\\more_previous_papers\\GENERAL-STUDIES-PAPER-IV.pdf, "
            "page 9. Topic 13 owns pollution, precaution, polluter-pays and environmental-justice "
            "substance; Topic 22 supplies the general case-study method."
        ),
        (
            "The officer must reject the false choice between uncontrolled production and abrupt "
            "livelihood destruction. Stakeholders include polluted communities, workers and their "
            "families, ancillary firms, consumers, the company, regulators, police, animals and the "
            "local ecosystem. Rights to health, livelihood and peaceful protest compete with public "
            "order and economic continuity.\n\n"
            "Immediate action should secure drinking water and medical relief, independently sample "
            "land, water and effluent, publish non-sensitive findings, and investigate both regulatory "
            "failure and any disproportionate policing. Closure should remain effective where serious "
            "non-compliance creates continuing harm, but an expert committee should assess whether a "
            "time-bound, monitored restart after proven treatment upgrades is environmentally safe. "
            "The precautionary principle governs uncertainty; polluter-pays places cleanup, health "
            "compensation and restoration costs on the company rather than taxpayers.\n\n"
            "Workers need wage support, social-security access, retraining and temporary placement; "
            "ancillary firms need transition assistance, not immunity for the polluter. A local "
            "grievance forum should include residents, workers, technical experts and administration. "
            "Any restart must require zero-bypass monitoring, public compliance reports, escrow for "
            "remediation and automatic suspension triggers.\n\n"
            "Vellore supports sustainable development, precaution and polluter-pays in environmental "
            "law, but the decision remains fact-specific. The ethical settlement therefore restores "
            "ecology and health, preserves viable livelihoods where possible, assigns costs to the "
            "wrongdoer and replaces reactive agitation with accountable regulation."
        ),
    ),
    _pyq(
        2020,
        (
            "GS-IV Q5(b): \"The current internet expansion has instilled a different set of cultural "
            "values which are often in conflict with traditional values.\" Discuss. "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated Q5(b) verified against books\\more_previous_papers\\Gen_St_P4.pdf, "
            "page 3. Topic 13 owns the internet-culture subpart; Q5(a), gender inequality and "
            "Savitribai Phule, belongs to Topic 2."
        ),
        (
            "Internet expansion changes how identity, authority and community are formed. It can "
            "promote autonomy, scientific temper, gender voice, intercultural learning and scrutiny "
            "of oppressive customs. Young people can find support beyond restrictive local settings, "
            "and public institutions can communicate across language and distance.\n\n"
            "Conflict arises when network values of speed, visibility, individual self-expression and "
            "global consumer culture meet traditions emphasising privacy, hierarchy, family authority "
            "and local continuity. The result may be generational tension, imitation, trolling, "
            "sexualised harassment, misinformation and polarisation. Yet neither category is morally "
            "pure: tradition can preserve solidarity and wisdom but also exclusion; digital culture "
            "can liberate but also manipulate attention and commodify intimacy.\n\n"
            "The ethical response is critical adaptation, not blanket rejection or surrender. Digital "
            "literacy, consent, privacy, respectful dialogue, age-appropriate safeguards and platform "
            "accountability should filter harmful practices. Constitutional dignity and equality "
            "provide the standard: retain traditions compatible with rights, reform oppressive ones, "
            "and domesticate technology through humane civic values."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-IV Q2(a): Impact of digital technology as reliable source of input for rational "
            "decision making is a debatable issue. Critically evaluate with suitable example. "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated Q2(a) verified against books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 2. Topic 13 owns digital decision "
            "reliability; Q2(b), innovativeness in ethical dilemmas, is cross-linked to decision method."
        ),
        (
            "Digital technology can make decisions more rational by integrating large records, "
            "detecting patterns, applying consistent criteria and creating auditable timelines. For "
            "example, a district may use satellite and transaction data to prioritise field inspection "
            "of suspected benefit leakage, saving scarce staff time.\n\n"
            "Reliability, however, is conditional. Incomplete records, biased samples, proxy variables, "
            "wrong objectives, cyber manipulation and model drift can produce precise-looking error. "
            "A digital score may omit disability, migration or local shocks that an experienced officer "
            "would recognise. Automation bias can then convert an advisory flag into an unreasoned "
            "denial, while opaque systems prevent citizens from correcting data.\n\n"
            "Therefore digital input should be triangulated with verified records and field context. "
            "High-stakes use needs data-quality checks, explainable factors, security, human authority "
            "to depart, recorded reasons, appeal and periodic audit. Technology is a valuable epistemic "
            "aid, not an infallible moral agent. Rationality lies in reviewable evidence and accountable "
            "judgment, not in digitisation by itself."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q4(b): Online methodology is being used for day-to-day meetings, institutional "
            "approvals in the administration and for teaching and learning in education sector to "
            "the extent telemedicine in the health sector is getting popular with the approvals of "
            "the competent authority. No doubt, it has advantages and disadvantages for both the "
            "beneficiaries and the system at large. Describe and discuss the ethical issues involved "
            "in the use of online method particularly to the vulnerable section of the society. "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated Q4(b) verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 3. Topic 13 owns online-method "
            "ethics; Q4(a), good governance and e-governance initiatives, cross-links to Topic 11."
        ),
        (
            "Online methods improve reach, speed, continuity, documentation and reduced travel. "
            "Telemedicine can connect specialists to remote patients; online approvals can reduce "
            "delay; digital learning can widen access to material.\n\n"
            "Their ethical value depends on substantive inclusion. Vulnerable persons may lack "
            "devices, connectivity, electricity, literacy, accessible design, private space or local-"
            "language support. Women may have less control over household devices; persons with "
            "disabilities may face inaccessible interfaces; elderly users may be exposed to fraud. "
            "Telemedicine also raises diagnostic limits, informed consent, confidentiality and data-"
            "security concerns. An online-only system can transfer administrative cost to the citizen "
            "and hide exclusion behind successful portal statistics.\n\n"
            "A just design therefore combines assisted digital centres, accessibility standards, "
            "plain-language consent, minimal secure data, grievance redress and an effective offline "
            "alternative. High-risk health or entitlement decisions need human follow-up. Efficiency "
            "is legitimate, but equality, dignity and care require that no person loses an essential "
            "service merely because the channel is digital."
        ),
    ),
    _pyq(
        2023,
        (
            "GS-IV Q12: You hold a responsible position in a ministry in the government. One day "
            "in the morning you received a call from the school of your 11-year-old son that you "
            "are required to come and meet the Principal. You proceed to the school and find your "
            "son in the Principal's office. The Principal informs you that your son had been found "
            "wandering aimlessly in the grounds during the time classes were in progress. The class "
            "teacher further informs you that your son has lately become a loner and did not respond "
            "to questions in the class; he had also been unable to perform well in the football "
            "trials held recently. You bring your son back from the school and in the evening, you "
            "along with your wife try to find out the reasons for your son's changed behaviour. "
            "After repeated cajoling, your son shares that some children had been making fun of him "
            "in the class as well as in the WhatsApp group of the students by calling him stunted, "
            "dumb and a frog. He tells you the names of a few children who are the main culprits but "
            "pleads with you to let the matter rest. After a few days, during a sporting event, where "
            "you and your wife have gone to watch your son play, one of your colleague's son shows "
            "you a video in which students have caricatured your son. Further, he also points out "
            "the perpetrators who were sitting in the stands. You purposefully walk past them with "
            "your son and go home. Next day, you find on social media a video denigrating you, your "
            "son and even your wife, stating that you engaged in physical bullying of children on "
            "the sports field. The video became viral on social media. Your friends and colleagues "
            "began calling you to find out the details. One of your juniors advised you to make a "
            "counter video giving the background and explaining that nothing had happened on the "
            "field. You, in turn, posted a video which you have captured during the sporting event, "
            "identifying the likely perpetrators who were responsible for your son's predicament. "
            "You have also narrated what has actually happened in the field and made attempts to "
            "bring out the adverse effects of the misuse of social media. (a) Based on the above "
            "case study, discuss the ethical issues involved in the use of social media. (b) Discuss "
            "the pros and cons of using social media by you to put across the facts to counter the "
            "fake propaganda against your family. "
            "(Answer in 250 words)"
        ),
        20,
        (
            "Exact full case and both demands verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, pages 14-15. Topic 13 owns social-media "
            "ethics; Topic 22 supplies case architecture and child-sensitive implementation."
        ),
        (
            "The case involves child dignity and safety, cyberbullying, privacy, misinformation, "
            "parental responsibility, public-office restraint, due process and the permanence of "
            "digital identification. The original attackers exploited reach and anonymity; the false "
            "viral allegation harmed the whole family and public trust. Yet identifying likely minor "
            "perpetrators can expose children to retaliation before facts are independently established.\n\n"
            "A counter-video offers speed, direct access to the same audience, evidence, correction "
            "and resistance to a one-sided narrative. It may reassure colleagues and expose platform "
            "misuse. Its disadvantages are escalation, context collapse, further circulation of the "
            "child's humiliation, privacy invasion, mistaken identification, vigilantism and the "
            "appearance that official status is being used in a private conflict.\n\n"
            "I would prioritise the son's psychological safety, counselling and informed participation. "
            "I would preserve screenshots and originals, request the school to investigate under a "
            "child-protection and anti-bullying process, seek removal or correction through the platform, "
            "and use lawful cyber channels if threats or serious defamation persist. Any public response "
            "should be brief, factual and anonymised: deny physical bullying, state that evidence has "
            "been submitted to competent authorities, and avoid naming minors.\n\n"
            "The already posted identifying video should be removed or edited, with a clarification "
            "protecting all children. Truthful counter-speech is legitimate, but proportionality and "
            "care demand verification, minimum disclosure and institutional remedy rather than a viral "
            "contest."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q1(a): The application of Artificial Intelligence as a dependable source of "
            "input for administrative rational decision-making is a debatable issue. Critically "
            "examine the statement from the ethical point of view. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated Q1(a) verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, "
            "page 2. Topic 13 is primary owner; Q1(b), dimensions of ethics in professional "
            "decision-making, belongs to Topic 1."
        ),
        (
            "AI can be a dependable input when it detects patterns across large records, improves "
            "consistency, reduces routine delay and enables scarce officials to focus on difficult "
            "cases. Used to flag anomalies in welfare payments, it may strengthen stewardship of "
            "public funds.\n\n"
            "Dependability is not inherent. Bias may enter data, design, deployment and feedback; "
            "generative systems may hallucinate; opaque scores weaken reason-giving; automation bias "
            "and de-skilling reduce practical wisdom. Accountability also diffuses among vendor, "
            "procurer and officer, although the affected citizen still bears the error. From a "
            "deontological view, dignity and due process require an intelligible, appealable decision. "
            "Consequentialism supports efficiency only after error and distributional harms are counted.\n\n"
            "High-stakes administrative AI should therefore remain advisory. Representative testing, "
            "red-teaming, audit logs, plain-language explanations, data correction, meaningful human "
            "review, contestability and continuous monitoring are essential. The India AI Governance "
            "Guidelines provide policy guidance, not proof of fairness. AI is ethically dependable "
            "only as a verified and supervised input within an accountable human institution."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q2(b): Global warming and climate change are the outcomes of human greed in the "
            "name of development, indicating the direction in which extinction of organisms "
            "including human beings is heading towards loss of life on Earth. How do you put an "
            "end to this to protect life and bring equilibrium between the society and the "
            "environment? (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated Q2(b) verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, "
            "page 2. Topic 13 owns climate ethics; Q2(a), powerful nations and ongoing conflicts, "
            "belongs to Topic 12."
        ),
        (
            "The statement identifies greed as a vice: limitless consumption treats nature, poorer "
            "communities and future generations as instruments. Climate change is therefore not only "
            "a technical market failure but a failure of temperance, justice and stewardship. Its "
            "burdens are unequal: those contributing least often face the greatest heat, livelihood "
            "and disaster risks.\n\n"
            "Equilibrium requires sustainable development: efficient and renewable energy, public "
            "transport, circular production, ecosystem restoration, climate-resilient agriculture and "
            "credible disclosure by firms. Polluter-pays should internalise damage, while precaution "
            "supports action despite uncertainty about exact local effects. Citizens must moderate "
            "wasteful consumption, but responsibility cannot be shifted from institutions to individual "
            "lifestyle alone.\n\n"
            "Internationally, CBDR-RC combines common action with historical contribution and respective "
            "capability; it means differentiated, not absent, obligations for developing states. "
            "Participatory transitions and support for affected workers make mitigation just. The goal "
            "is not to end development, but to redefine it so present welfare no longer destroys the "
            "ecological conditions of future freedom and life."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q7: There is a technological company named ABC Incorporated which is the second "
            "largest worldwide, situated in the Third World. You are the Chief Executive Officer "
            "and the majority shareholder of this company. The fast technological improvements have "
            "raised worries among environmental activists, regulatory authorities, and the general "
            "public over the sustainability of this scenario. You confront substantial issues about "
            "the business's environmental footprint. In 2023, your organization had a significant "
            "increase of 48% in greenhouse gas emissions compared to the levels recorded in 2019. "
            "The significant rise in energy consumption is mainly due to the surging energy "
            "requirements of your data centers, fuelled by the exponential expansion of Artificial "
            "Intelligence (AI). AI-powered services need much more computational resources and "
            "electrical energy compared to conventional online activities, notwithstanding their "
            "notable gains. The technology's proliferation has led to a growing concern over the "
            "environmental repercussions, resulting in an increase in warnings. AI models, especially "
            "those used in extensive machine learning and data processing, exhibit much greater "
            "energy consumption than conventional computer tasks, with an exponential increase. "
            "Although there is already a commitment and goal to achieve net zero emissions by 2030, "
            "the challenge of lowering emissions seems overwhelming as the integration of AI continues "
            "to increase. To achieve this goal, substantial investments in renewable energy use would "
            "be necessary. The difficulty is exacerbated by the competitive environment of the "
            "technology sector, where rapid innovation is essential for preserving market standing "
            "and shareholders' worth. To achieve a balance between innovation, profitability and "
            "sustainability, a strategic move is necessary that is in line with both business "
            "objectives and ethical obligations. (a) What is your immediate response to the challenges "
            "posed in the above case? (b) Discuss the ethical issues involved in the above case. "
            "(c) Your company has been identified to be penalized by technological giants. What "
            "logical and ethical arguments will you put forth to convince about its necessity? "
            "(d) Being a conscience being, what measures would you adopt to maintain balance between "
            "AI innovation and environmental footprint? "
            "(Answer in 250 words)"
        ),
        20,
        (
            "Exact full case and all four demands verified against books\\mains\\"
            "05 UPSC 2024 Paper-IV_Final 1.pdf, pages 4-5. Topic 13 owns AI-footprint and "
            "environmental substance; Topic 22 owns method and Topic 12 is a corporate-governance "
            "cross-link. The official case contains no algorithmic-discrimination fact."
        ),
        (
            "I would acknowledge the 48% increase, freeze avoidable high-carbon expansion pending a "
            "rapid independent footprint review, and protect essential services while the board adopts "
            "a verified transition plan. Stakeholders are users, employees, shareholders, regulators, "
            "energy and water-stressed communities, future generations and competitors.\n\n"
            "The ethical issues are truthful disclosure versus greenwashing; profit and innovation "
            "versus climate duty; present shareholder value versus intergenerational equity; unequal "
            "burdens in a Third World setting; and responsibility for operational energy, cooling "
            "water, hardware and e-waste. A 2030 promise cannot excuse present inaction. Polluter-pays "
            "and sustainable development require costs to be internalised rather than shifted.\n\n"
            "If stronger technological giants seek to penalise ABC, I would argue for transparent, "
            "uniform and capability-sensitive standards, independent verification and a fair transition "
            "period. Environmental accountability is necessary, but private rivals should not use it "
            "as discriminatory market exclusion. Equivalent footprints must face equivalent rules, "
            "with CBDR-RC used as an ethical analogy for capability, not as corporate immunity.\n\n"
            "Measures include science-based interim carbon budgets; renewable procurement plus "
            "additional clean capacity; efficient models, hardware utilisation and workload scheduling; "
            "water-aware siting and cooling; repair, reuse and responsible e-waste; supplier standards; "
            "internal carbon pricing; audited public reporting; and executive incentives tied to absolute "
            "reductions. A board sustainability committee should monitor milestones and publish setbacks. "
            "Innovation should continue within resource budgets, with low-value computation deferred and "
            "high-social-value uses prioritised."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q12: Dr. Srinivasan is a senior scientist working for a reputed biotechnology "
            "company known for its cutting-edge research in pharmaceuticals. Dr. Srinivasan is "
            "heading a research team working on a new drug aimed at treating a rapidly spreading "
            "variant of a new viral infectious disease. The disease has been rapidly spreading "
            "across the world and the cases reported in the country are increasing. There is huge "
            "pressure on Dr. Srinivasan's team to expedite the trials for the drug as there is "
            "significant market for it, and the company wants to get the first-mover advantage in "
            "the market. During a team meeting, some senior team members suggest some shortcut for "
            "expediting the clinical trials for the drug and for getting the requisite approvals. "
            "These include manipulating data to exclude some negative outcomes and selectively "
            "reporting positive results, foregoing the process of informed consent and using "
            "compounds already patented by a rival company, rather than developing one's own "
            "component. Dr. Srinivasan is not comfortable taking such shortcuts, at the same time "
            "he realises meeting the targets is impossible without using these means. (a) What would "
            "you do in such a situation? (b) Examine your options and consequences in the light of "
            "the ethical questions involved. (c) How can data ethics and drug ethics save humanity "
            "at large in such a scenario? (Answer in 250 words)"
        ),
        20,
        (
            "Exact full case and all three demands verified against books\\mains\\"
            "05 UPSC 2024 Paper-IV_Final 1.pdf, page 10. Topic 13 owns the data-integrity and "
            "consent cross-link; Topic 22 owns case method, with research and drug ethics supplying "
            "the specialist substantive route."
        ),
        (
            "I would refuse data manipulation, selective reporting, consent bypass and unauthorised "
            "use of patented compounds; preserve records; document the pressure; seek an urgent "
            "independent ethics and regulatory review; and propose a lawful accelerated protocol. "
            "Patients, trial participants, future users, researchers, the company, the rival patent "
            "holder, regulators and the wider public are stakeholders.\n\n"
            "Compliance with the shortcuts may produce speed and first-mover gain, but it converts "
            "participants into means, conceals adverse effects, corrupts scientific knowledge, risks "
            "mass injury and destroys trust. Silent refusal protects personal integrity but leaves "
            "organisational pressure intact. Resignation may be necessary if correction fails, yet "
            "premature exit can abandon evidence. The strongest option is recorded internal escalation, "
            "independent review and competent external reporting where serious misconduct persists, "
            "with protection of confidential patient data.\n\n"
            "Data ethics requires completeness, accuracy, reproducibility, secure handling, transparent "
            "adverse-result reporting and correction. Drug ethics requires scientific validity, informed "
            "and voluntary consent, favourable risk-benefit assessment, fair participant selection, "
            "monitoring and post-trial responsibility. Patent rights must be respected or addressed "
            "through lawful licensing and applicable public-health mechanisms, not covert appropriation.\n\n"
            "A lawful accelerated design may use adaptive protocols, parallel administrative preparation "
            "and rapid independent review without weakening consent or evidence. These disciplines save "
            "humanity because unreliable data in a fast-moving epidemic scales harm globally. Urgency "
            "justifies faster ethical work, not lower truth, dignity or safety."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q1(a): In the present digital age, social media has revolutionised our way of "
            "communication and interaction. However, it has raised several ethical issues and "
            "challenges. Describe the key ethical dilemmas in this regard. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated Q1(a) verified against books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, "
            "page 2. Topic 13 owns social-media ethics; Q1(b), constitutional morality and public "
            "service, belongs to Topic 14."
        ),
        (
            "Social media expands voice, association, emergency communication and accountability, but "
            "its ethical dilemmas arise from a business and design environment that rewards attention. "
            "Freedom of expression conflicts with protection from incitement, cyberbullying and "
            "defamation. Personalisation offers relevance but enables surveillance, micro-targeted "
            "manipulation and loss of autonomy. Virality democratises information yet accelerates "
            "misinformation, deepfakes and irreversible reputational harm before verification.\n\n"
            "Further dilemmas include privacy versus public curiosity, anonymity versus answerability, "
            "platform moderation versus censorship, child safety versus participation, and global rules "
            "versus linguistic and cultural context. Algorithmic amplification can create polarisation "
            "and silence minorities even without direct state coercion.\n\n"
            "An ethical response combines user digital literacy, consent and privacy by design, child-"
            "sensitive defaults, provenance and rapid correction tools, transparent moderation reasons, "
            "appeal, researcher access and proportionate lawful regulation. Government counter-speech "
            "should be factual and restrained. The aim is not a sanitised public sphere, but one where "
            "expression remains free while manipulation, hidden surveillance and preventable harm become "
            "contestable and accountable."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q2(b): Keeping the national security in mind, examine the ethical dilemmas "
            "related to controversies over environmental clearance of development projects in "
            "ecologically sensitive border areas in the country. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated Q2(b) verified against books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, "
            "page 2. Topic 13 is the sole substantive owner of this subpart; Q2(a), Clausewitz and "
            "war as diplomacy, belongs to Topic 12."
        ),
        (
            "Border roads, communications and logistics can protect sovereignty, responders and remote "
            "communities. Yet ecologically sensitive mountains and forests may face irreversible habitat "
            "fragmentation, erosion, disaster risk and livelihood loss. The dilemma is therefore security "
            "and development versus precaution, community voice and intergenerational equity; neither "
            "value may be reduced to a slogan.\n\n"
            "Blanket exemption risks using secrecy to avoid scrutiny. Complete public disclosure, however, "
            "may reveal genuine operational information. A proportionate process should define the specific "
            "security purpose, compare routes and technologies, choose the least ecologically damaging "
            "feasible alternative, consult affected communities on non-classified impacts, and subject "
            "classified material to cleared independent experts. Cumulative and disaster-risk assessment, "
            "seasonal construction controls, compensatory restoration, wildlife passages and continuous "
            "monitoring should follow.\n\n"
            "Precaution does not ban all border infrastructure; it demands safeguards despite uncertainty. "
            "Reasons, conditions and compliance results should be public except for narrowly protected "
            "security details. Ethical clearance is thus a reviewable, least-damage accommodation of a "
            "legitimate security need, not automatic approval or automatic prohibition."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q8: In line with the Directive Principles of State Policy enshrined in the Indian "
            "Constitution, the government has a constitutional obligation to ensure basic needs - "
            "\"Roti, Kapda aur Makan (Food, Clothes and Shelter)\" - for the under-privileged. "
            "Pursuing this mandate, the district administration proposed clearing a portion of forest "
            "land to develop housing for the homeless and economically weaker sections of the society. "
            "The proposed land, however, is an ecologically sensitive zone densely populated with "
            "age-old trees, medicinal plants and vital biodiversity. Besides, these forests help to "
            "regulate micro-climate and rainfalls, provide habitat for wildlife, support soil fertility "
            "and prevent land/soil erosion and sustain livelihoods of tribal and nomadic communities. "
            "Inspite of the ecological and social costs, the administration argues in favour of the "
            "said proposal by highlighting that this very initiative addresses fundamental human rights "
            "as a critical welfare priority. Besides, it fulfils the government's duty to uplift and "
            "empower the poor through inclusive housing development. Further, these forest areas have "
            "become unsafe due to wild-animal threats and recurring human-wild life conflicts. Lastly, "
            "clearing forest-zones may help to curb anti-social elements allegedly using these areas as "
            "hideouts, thereby enhancing law and order. (a) Can deforestation be ethically justified in "
            "the pursuit of social welfare objectives like, housing for the homeless? (b) What are the "
            "socio-economic, administrative and ethical challenges in balancing environmental conservation "
            "with human development? (c) What substantial alternatives or policy interventions can be "
            "proposed to ensure that both environmental integrity and human dignity are protected? "
            "(Answer in 250 words)"
        ),
        20,
        (
            "Exact full case and all three demands verified against books\\mains\\"
            "UPSC Mains 2025 GS Paper 4.pdf, pages 5-6. Topic 13 owns environmental substance; "
            "Topic 22 owns method. No degraded-forest, city-periphery or court-monitoring fact is added."
        ),
        (
            "Housing is a dignity and welfare imperative, but the stated forest is not vacant land. "
            "It contains age-old trees, medicinal plants, biodiversity, climate and rainfall regulation, "
            "wildlife habitat, fertile soil, erosion control and tribal and nomadic livelihoods. These "
            "ecological services support human rights across generations. Deforestation is therefore "
            "justifiable only after necessity and least-damaging alternatives are proved, not merely "
            "because the beneficiary goal is worthy.\n\n"
            "Socio-economic challenges include land scarcity, affordability, livelihood displacement and "
            "human-wildlife conflict. Administrative challenges include reliable beneficiary selection, "
            "interdepartmental coordination, ecological valuation, consultation, rehabilitation and "
            "preventing capture. Ethical tensions oppose immediate shelter to intergenerational equity, "
            "anthropocentric welfare to biocentric and ecocentric value, and majority benefit to the voice "
            "of tribal and nomadic communities. Alleged hideouts do not establish that clearing is a "
            "necessary law-and-order response.\n\n"
            "The administration should first inventory public land, vacant serviced plots and brownfield "
            "sites; use in-situ upgrading, rental housing, land pooling, vertical construction and "
            "distributed smaller sites; and improve transport to suitable land. It should map ecosystem "
            "services and wildlife corridors, consult affected communities, and compare lifecycle costs. "
            "If a residual diversion is demonstrably unavoidable, minimise its footprint, protect critical "
            "habitat and medicinal species, secure lawful livelihood rehabilitation, create wildlife "
            "mitigation and fund long-term restoration and monitoring.\n\n"
            "The ethical verdict is integrated planning: fulfil shelter without treating the poor as a "
            "pretext for avoidable ecological loss or conservation as a reason to deny human dignity."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        (
            "Administrative AI should support judgment without becoming an unanswerable final "
            "decision-maker. Examine with suitable safeguards."
        ),
        (
            "Administrative AI can improve speed, consistency, anomaly detection and allocation of "
            "scarce inspection capacity. A welfare department may use it to flag unusual claims for "
            "human review. However, machine output reflects chosen data, labels, objectives and "
            "deployment conditions. It may reproduce exclusion, hallucinate, drift or omit context. "
            "Automation bias then makes a recommendation appear objective, while accountability is "
            "diffused among vendor, procurer and official.\n\n"
            "The ethical position is decision support under human responsibility. Before procurement, "
            "the department should define purpose, rights impact and success criteria. It should require "
            "representative testing, security and bias red-teaming, documentation, audit access and an "
            "exit route. Deployment needs meaningful human authority to depart, intelligible reasons, "
            "notice of automation, correction of data, appeal and continuous monitoring. High-stakes "
            "decisions should never rest solely on unverified generative output.\n\n"
            "The India AI Governance Guidelines offer useful policy guidance but do not prove a system "
            "fair or safe. AI becomes rational only inside a reviewable institution where an identified "
            "human remains answerable."
        ),
    ),
    _original(
        10,
        (
            "Why are explainability, contestability and accountability distinct but mutually "
            "dependent safeguards in high-stakes AI?"
        ),
        (
            "Explainability supplies intelligible reasons: the affected person should know the decisive "
            "factors, important limits and role of automation. Contestability converts knowledge into "
            "agency by allowing data correction, challenge, timely human reconsideration and remedy. "
            "Accountability assigns institutional responsibility and preserves logs, audits and sanctions "
            "so that failure has an answerable owner.\n\n"
            "Each is insufficient alone. A technically accurate explanation without appeal merely "
            "describes an injustice. An appeal without reasons forces the citizen to guess what to "
            "challenge. Reasons and appeal without responsibility may end in the vendor and department "
            "blaming each other. In a scholarship-rejection system, the applicant should receive the "
            "relevant eligibility factors, correct an erroneous record and obtain a reasoned review by an "
            "authorised officer; the agency should retain audit logs and investigate recurring error.\n\n"
            "Commercial secrecy may protect genuine intellectual property, but cannot erase due process. "
            "Risk-sensitive disclosure, independent confidential audit and plain-language adverse-action "
            "reasons can reconcile both interests. Together the three safeguards make automated power "
            "understandable, challengeable and answerable."
        ),
    ),
    _original(
        15,
        (
            "A consent form alone does not make administrative data use ethical. Discuss through "
            "privacy, purpose limitation and the phased DPDP framework."
        ),
        (
            "Consent protects autonomy only when it is informed, specific, accessible and capable of "
            "withdrawal. In public administration, dependence on an essential service can make formal "
            "agreement weak: a citizen may click a bundled notice because refusal means losing a benefit. "
            "Ethical data use therefore also requires lawful authority, purpose limitation, minimisation, "
            "accuracy, retention limits, security and remedy.\n\n"
            "Puttaswamy recognises privacy as a fundamental right linked to dignity and autonomy. A State "
            "restriction requires legality, legitimate aim, rational connection, necessity or least-"
            "restrictive means, proportionate balancing and procedural safeguards. A useful scheme objective "
            "alone is insufficient. Thus a health database collected for treatment should not silently become "
            "a general profiling system.\n\n"
            "The DPDP framework must be stated chronologically. G.S.R. 843(E) commenced specified provisions "
            "on 13 November 2025; the Consent Manager tranche begins 13 November 2026; core notice, consent, "
            "rights, fiduciary, Board and penalty provisions begin 13 May 2027. It is wrong to call the Act "
            "fully operational at the present cut-off.\n\n"
            "Nevertheless, deferred statutory commencement does not defer ethics. Administrators should use "
            "plain-language and granular notices, collect only necessary data, separate optional reuse, secure "
            "records, publish retention rules and provide correction and grievance channels. Consent is one "
            "part of a dignity-preserving architecture, not a universal moral waiver."
        ),
    ),
    _original(
        15,
        (
            "Can the environmental precautionary principle guide governance of high-stakes AI? "
            "Critically examine the analogy and its limits."
        ),
        (
            "Precaution addresses decisions where scientific uncertainty coexists with threats of serious or "
            "irreversible harm. Rio Declaration Principle 15 gives its classic environmental formulation, and "
            "Vellore recognises precaution within Indian environmental law. High-stakes AI presents a structural "
            "analogy: model error may be opaque, scale rapidly and burden people who lack voice, while evidence "
            "of harm emerges only after deployment.\n\n"
            "The analogy supports staged pilots, impact assessment, adversarial red-teaming, security tests, "
            "representative evaluation, fallback procedures, human oversight and continuous monitoring before "
            "mass use in welfare, policing or health. Lack of perfect certainty should not justify exposing "
            "citizens to an untested irreversible denial.\n\n"
            "However, Rio and Vellore are environmental authorities, not binding Indian AI law. AI harms may be "
            "reversible through correction, while blanket precaution can freeze socially beneficial innovation "
            "and entrench incumbent vendors. Risk also varies: a translation assistant and an automated liberty "
            "decision cannot face identical controls.\n\n"
            "Therefore precaution should operate as a proportionate ethical analogy. Classify impact, require "
            "stronger evidence where rights and irreversibility are greater, preserve contestability and review "
            "controls as performance changes. The principle justifies anticipatory governance, not a general "
            "technology veto or a false claim that Vellore directly regulates AI."
        ),
    ),
    _original(
        20,
        (
            "Examine the full environmental footprint of AI through sustainable development and "
            "intergenerational justice. Suggest an accountable transition framework for India."
        ),
        (
            "AI's footprint is a lifecycle issue, not electricity alone. Training and repeated inference consume "
            "power; cooling and power generation consume water; semiconductor and server manufacture embody "
            "energy, minerals and pollution; rapid replacement produces electronic waste. Benefits and burdens "
            "are also spatially unequal: urban and global users may gain while water-stressed communities, "
            "workers near extraction and future generations bear costs.\n\n"
            "Sustainable development requires meeting present needs without compromising future capacity. "
            "Intergenerational justice gives absent future citizens standing in today's resource allocation. "
            "Polluter-pays opposes shifting remediation to taxpayers, and environmental justice requires voice "
            "for affected communities. Yet a blanket restriction would ignore AI's public value in health, "
            "agriculture, disaster warning and accessible services.\n\n"
            "An accountable Indian transition should begin with standardised disclosure of operational energy, "
            "water, location, embodied hardware and e-waste, without unsupported precision where measurement is "
            "immature. Public procurement can reward efficient models, repairability, renewable additionality, "
            "water-aware siting and responsible end-of-life handling. Operators should use carbon and water "
            "budgets, efficient architectures, high utilisation, workload scheduling, heat reuse where feasible "
            "and verified supplier standards. EIA and local consultation should apply where the governing law "
            "requires them; environmental claims need independent assurance.\n\n"
            "Policy should prioritise high-social-value computation, support clean grids and domestic circular "
            "hardware capacity, and protect workers and communities during transition. Periodic public review "
            "must compare absolute impacts, not efficiency claims alone. The ethical goal is useful AI within "
            "ecological budgets, not innovation whose hidden costs narrow future freedom."
        ),
    ),
    _original(
        20,
        (
            "A State proposes an AI system to select welfare beneficiaries and a water-intensive "
            "data centre to operate it in a drought-prone district. As district head, resolve the "
            "combined data, justice and environmental dilemma."
        ),
        (
            "Stakeholders include eligible applicants, excluded families, local residents and farmers, tribal or "
            "marginalised groups, officials, the vendor, data-centre workers, the power and water utilities, the "
            "ecosystem and future citizens. The proposal promises faster targeting and jobs, but creates linked "
            "risks: biased exclusion, opaque reasons, privacy loss, vendor dependence, groundwater stress, energy "
            "emissions and unequal distribution of benefits and burdens.\n\n"
            "I would not approve immediate full-scale deployment. First, separate and test the two decisions. "
            "For beneficiary selection, define lawful eligibility, prohibit the model from making final adverse "
            "decisions, audit data and proxies, red-team vulnerable cases, provide notice, plain-language reasons, "
            "data correction, assisted offline application and timely human appeal. Contracts must assign "
            "accountability, preserve logs, permit independent audit and allow exit. Puttaswamy proportionality "
            "and purpose limitation govern personal-data use.\n\n"
            "For the data centre, commission a transparent assessment of water source, drought scenarios, energy, "
            "cooling, hardware and e-waste; compare less water-intensive locations and architectures; consult "
            "affected communities; and select the least-damaging feasible alternative. Approval, if justified, "
            "should impose water and carbon budgets, renewable additionality, non-potable or recycled water where "
            "safe, public monitoring, drought curtailment triggers and restoration security. Claimed welfare "
            "benefits cannot override ecological limits.\n\n"
            "A limited pilot using existing lower-impact infrastructure may proceed if independent review confirms "
            "rights and reliability safeguards. The final decision should publish reasons and residual risks. "
            "Innovation is acceptable only when beneficiaries can contest digital power and host communities do "
            "not subsidise it with dignity, water and future resilience."
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
        "1. AI administrative decision chain",
        "decision-chain",
        (
            "Define lawful public purpose",
            "Check data fitness",
            "Generate advisory output",
            "Show decisive factors",
            "Apply human judgment",
            "Record independent reasons",
            "Offer appeal and correction",
            "Audit outcomes and drift",
        ),
        "AI may inform power; an answerable institution must exercise it.",
        "Use for 2021 Q2(a) and 2024 Q1(a).",
    ),
    _panel(
        "2. Bias control across the lifecycle",
        "bias-lifecycle",
        (
            "Test representation in data",
            "Review labels and proxies",
            "Question design objective",
            "Red-team unequal impact",
            "Check deployment conditions",
            "Monitor subgroup outcomes",
            "Break feedback loops",
            "Correct and retrain safely",
        ),
        "Bias is a socio-technical lifecycle risk, not merely a coding defect.",
        "Use to replace generic claims that AI is biased.",
    ),
    _panel(
        "3. Contestability and remedy",
        "remedy-ladder",
        (
            "Notify material automation",
            "Give intelligible reasons",
            "Let citizen inspect data",
            "Enable factual correction",
            "Provide simple challenge",
            "Require human reconsideration",
            "Order correction or remedy",
            "Feed lessons into redesign",
        ),
        "A right without a usable challenge route leaves automated power unchecked.",
        "Use for explainability, due process and accountability.",
    ),
    _panel(
        "4. Privacy governance chain",
        "privacy-chain",
        (
            "State specific purpose",
            "Establish lawful basis",
            "Seek meaningful consent",
            "Collect minimum data",
            "Secure and limit access",
            "Restrict reuse and retention",
            "Enable correction and exit",
            "Remedy breach and misuse",
        ),
        "Privacy protects dignity and autonomy throughout the data lifecycle.",
        "Use for consent, purpose and minimisation answers.",
    ),
    _panel(
        "5. Puttaswamy proportionality test",
        "rights-test",
        (
            "Privacy is a fundamental right",
            "Identify legal authority",
            "Name legitimate State aim",
            "Prove rational connection",
            "Test least-restrictive means",
            "Balance rights and benefit",
            "Add procedural safeguards",
            "Keep review and remedy open",
        ),
        "A useful aim does not by itself justify a privacy restriction.",
        "Use as the constitutional spine for State data use.",
    ),
    _panel(
        "6. Social-media ethics map",
        "platform-risk-map",
        (
            "Expression and association",
            "Misinformation and deepfakes",
            "Manipulation and addiction",
            "Privacy and surveillance",
            "Cyberbullying and dignity",
            "Polarisation and amplification",
            "Moderation reasons and appeal",
            "Verification and proportionate law",
        ),
        "Protect open debate while making hidden manipulation and preventable harm answerable.",
        "Use for 2023 Q12 and 2025 Q1(a).",
    ),
    _panel(
        "7. AI environmental footprint",
        "lifecycle-footprint",
        (
            "Training electricity demand",
            "Repeated inference demand",
            "Cooling and power water",
            "Hardware embodied impacts",
            "Mineral and supply-chain harm",
            "Replacement and e-waste",
            "Absolute-impact disclosure",
            "Budgets, efficiency and repair",
        ),
        "A renewable-power claim alone does not establish low-impact AI.",
        "Use for 2024 Q7 and lifecycle analysis.",
    ),
    _panel(
        "8. Precaution before scale-up",
        "precaution-gate",
        (
            "Identify serious possible harm",
            "Map uncertainty and exposure",
            "Test reversible pilot",
            "Compare safer alternatives",
            "Apply proportionate controls",
            "Set stop and fallback rules",
            "Monitor emerging evidence",
            "Revise before wider deployment",
        ),
        "Rio and Vellore guide AI only by analogy, not as binding AI law.",
        "Use for anticipatory AI and environmental governance.",
    ),
    _panel(
        "9. Environmental justice test",
        "distribution-voice-remedy",
        (
            "Identify ecological benefits",
            "Identify pollution and loss",
            "Map burdened communities",
            "Include future generations",
            "Secure meaningful participation",
            "Compare distributional options",
            "Assign compensation and cleanup",
            "Provide accessible remedy",
        ),
        "A green or welfare label cannot hide unequal burdens and silenced voices.",
        "Use for pollution, housing and siting cases.",
    ),
    _panel(
        "10. Sustainable-development bridge",
        "present-future-bridge",
        (
            "Define present human need",
            "Value ecosystem services",
            "Protect future capability",
            "Compare lower-impact routes",
            "Internalise pollution costs",
            "Support a just transition",
            "Monitor real outcomes",
            "Revise if limits are breached",
        ),
        "Development and ecology are jointly constrained, not automatic overrides.",
        "Use for climate ethics and 2025 Q8.",
    ),
    _panel(
        "11. Border environmental clearance",
        "security-clearance-route",
        (
            "Specify security objective",
            "Map sensitive ecology",
            "Compare route alternatives",
            "Use least-damaging feasible design",
            "Consult on non-classified impacts",
            "Review secrets through cleared experts",
            "Condition restoration and monitoring",
            "Publish reasons within security limits",
        ),
        "Security warrants tailored protection, not automatic ecological exemption.",
        "Use for 2025 Q2(b).",
    ),
    _panel(
        "12. Climate fairness architecture",
        "climate-equity-map",
        (
            "Common duty to protect climate",
            "Historical contribution matters",
            "Respective capability matters",
            "Current emissions still matter",
            "CBDR-RC differentiates effort",
            "Finance and technology enable action",
            "Protect vulnerable transitions",
            "Retain reviewable national duties",
        ),
        "Differentiated responsibility means fair action, not zero obligation.",
        "Use for 2024 Q2(b) and climate justice.",
    ),
)


CURRENT_ANCHOR = {
    "title": "India AI Governance Guidelines and India AI Impact Summit 2026",
    "verified_facts": (
        "The India AI Governance Guidelines provide policy guidance through principles, recommendations, an action plan and practical guidance, including voluntary commitments.",
        "The Guidelines cover fairness, accountability, safety, inclusivity, transparency, risk classification, human oversight, testing and grievance redressal.",
        "The India AI Impact Summit was held on 19-20 February 2026 at Bharat Mandapam within a broader 16-20 February programme.",
        "The Summit's official framing promotes people-centric and inclusive AI that protects the planet.",
        "The official Summit page identifies employment disruption, exacerbated bias and accelerating energy consumption as urgent AI challenges.",
    ),
    "administrative_link": (
        "Use the Guidelines to structure purpose, risk classification, testing, human oversight, "
        "accountability and grievance safeguards. Use the Summit to connect inclusion and human "
        "agency with AI's energy and environmental costs."
    ),
    "limit": (
        "Neither source is a comprehensive Indian AI statute, and neither proves that any deployed "
        "system is fair, safe or low-carbon. Do not add unsupported impact, participation or emissions metrics."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://indiaai.gov.in/article/india-ai-governance-guidelines-empowering-ethical-and-responsible-ai",
    "https://impact.indiaai.gov.in/about-summit",
)


SOURCE_CAVEAT = (
    "The corrected canonical Topic 13 Basic and Advanced owners control the doctrinal sequence. "
    "Official question wording and material case facts come from the stated local GS-IV PDFs or their "
    "document-order knowledge exports; routing ledgers establish ownership but do not authorise invented "
    "facts. Topic 13 owns only the isolated 2024 Q1(a), 2024 Q2(b), 2025 Q1(a) and 2025 Q2(b) subparts: "
    "their paired subparts route respectively to Topic 1, Topic 12, Topic 14 and Topic 12. The full 2024 "
    "Q7, 2024 Q12 and 2025 Q8 cases retain Topic 22 method cross-links; Topic 12 is only a corporate "
    "cross-link for Q7, and research/drug ethics is the specialist cross-link for Q12. Do not add "
    "algorithmic discrimination to 2024 Q7. Do not add degraded forest, city-periphery or court-monitoring "
    "facts to 2025 Q8. AI is framed as decision support subject to data, design, deployment and feedback "
    "bias controls, explainability, named accountability, meaningful human oversight, contestability, "
    "hallucination checks, red-teaming, procurement controls and continuing monitoring. Puttaswamy is the "
    "constitutional privacy foundation: use legality, legitimate aim, rational connection, necessity or "
    "least-restrictive means, proportionate balancing and procedural safeguards rather than citing a useful "
    "aim alone. DPDP commencement is phased under G.S.R. 843(E): specified provisions commenced on "
    "13 November 2025, the Consent Manager tranche begins 13 November 2026, and core notice, consent, "
    "rights, fiduciary, Board and penalty provisions begin 13 May 2027. Do not call the Act fully "
    "operational at the 29 August 2026 cut-off; ethical duties of dignity, autonomy, purpose limitation, "
    "minimisation and security apply independently of deferred statutory operation. Rio Principle 15 is "
    "the classic environmental precautionary approach. Vellore is an Indian environmental-law authority "
    "for sustainable development, precaution and polluter-pays in its tannery-pollution setting; neither "
    "Rio nor Vellore is binding AI law. Precaution may guide high-stakes AI only by explicit analogy. Keep "
    "precaution ex ante and polluter-pays ex post analytically distinct. Distinguish anthropocentric, "
    "biocentric and ecocentric reasons; use environmental justice for burden, voice and remedy; and state "
    "CBDR-RC as differentiated responsibility, not zero responsibility. Border-clearance answers require "
    "a specific security purpose, EIA and cumulative-risk discipline, community consideration, classified "
    "expert review where genuinely necessary, and the least ecologically damaging feasible alternative. "
    "The India AI Governance Guidelines and India AI Impact Summit are current official policy anchors, "
    "not a comprehensive AI statute or evidence that a particular system is fair, safe or low-carbon."
)


REGISTER_SUPPLEMENT = (
    "### EMERGING-ETHICS CORE MAP\n\n"
    "- **Shared structure:** AI and environmental harms may be opaque, delayed, diffuse, scalable and borne by people without effective voice.\n"
    "- **Ethical sequence:** rights and dignity floor -> long-horizon consequences -> virtue and restraint -> precaution before scale -> accountability and remedy.\n"
    "- **AI verdict:** useful decision support, never an unanswerable moral or legal agent.\n"
    "- **Environmental verdict:** legitimate development within ecological, distributive and intergenerational limits.\n\n"
    "### AI DECISION GOVERNANCE\n\n"
    "- **Benefit claim:** speed, consistency, pattern detection, auditability and better targeting of scarce administrative attention.\n"
    "- **Bias chain:** data representation and labels -> proxy and objective design -> deployment context -> feedback loops -> model drift.\n"
    "- **Explainability:** give affected persons intelligible decisive factors, uncertainty and limits; source-code disclosure alone is not enough.\n"
    "- **Accountability:** name developer, procurer, deploying department and final decision-maker; preserve logs, audit access, incident duties and sanctions.\n"
    "- **Human oversight:** reviewer needs competence, time, authority, information and freedom to depart; rubber-stamping is not human-in-the-loop.\n"
    "- **Contestability:** notice of material automation -> data correction -> simple challenge -> timely human reconsideration -> correction or remedy.\n"
    "- **Reliability:** verify generated facts and citations; test domain performance; disclose uncertainty; never use unverified hallucinated output alone for consequential action.\n"
    "- **Human capability:** counter automation bias and de-skilling through training, manual samples, recorded departures and periodic unaided judgment.\n"
    "- **Procurement:** define purpose and risk -> representative tests -> security and bias red-teaming -> documentation -> audit rights -> change control -> monitoring -> exit.\n\n"
    "### DIGITAL PUBLIC SPHERE AND INCLUSION\n\n"
    "- **Deepfakes:** authenticity and provenance problem; preserve originals, verify, correct rapidly and avoid disproportionate suppression.\n"
    "- **Social media:** expression and association versus misinformation, manipulation, addictive amplification, privacy invasion, cyberbullying and polarisation.\n"
    "- **Moderation:** transparent reasons, proportionate rules, appeal and child-sensitive safeguards; neither total laissez-faire nor blanket censorship.\n"
    "- **Digital divide:** connectivity + affordability + device + language + disability access + literacy + assistance + effective offline alternative.\n"
    "- **2020 Q5(b):** assess tradition and network culture through constitutional dignity and equality, not romanticise either side.\n"
    "- **2022 Q4(b):** online efficiency is unethical when essential services become inaccessible to vulnerable persons.\n"
    "- **2023 Q12:** truthful counter-speech must protect minors, minimise disclosure and prefer institutional remedy over viral escalation.\n"
    "- **2025 Q1(a):** organise dilemmas as expression/safety, relevance/manipulation, anonymity/accountability, virality/truth and moderation/censorship.\n\n"
    "### PRIVACY, PUTTASWAMY AND DPDP\n\n"
    "- **Privacy:** dignity, decisional autonomy and contextual control over collection, combination, inference, reuse and disclosure.\n"
    "- **Puttaswamy:** nine-judge bench, 24 August 2017, privacy fundamental under Article 21 and Part III freedoms.\n"
    "- **Full State restriction test:** legality -> legitimate aim -> rational connection -> necessity or least-restrictive means -> proportionate balance -> procedural safeguards.\n"
    "- **Data ethics:** meaningful consent + purpose limitation + minimisation + accuracy + retention limits + security + correction + remedy.\n"
    "- **DPDP chronology:** 13 Nov 2025 specified immediate tranche; 13 Nov 2026 Consent Manager tranche; 13 May 2027 core notice, consent, rights, fiduciary, Board and penalty provisions.\n"
    "- **Exam limit:** enacted or notified does not mean every duty is presently in force; ethical responsibility precedes full statutory commencement.\n\n"
    "### AI ENVIRONMENTAL FOOTPRINT\n\n"
    "- **Lifecycle:** training electricity + repeated inference + cooling and power water + embodied hardware + mineral extraction + replacement + e-waste.\n"
    "- **Measure honestly:** report absolute as well as efficiency impacts; renewable electricity alone does not erase water, hardware or waste burdens.\n"
    "- **Transition controls:** carbon and water budgets, efficient models, utilisation, workload timing, renewable additionality, water-aware siting, repair, reuse and verified e-waste handling.\n"
    "- **2024 Q7 facts:** ABC is second largest worldwide in the Third World; 2023 GHG emissions were 48% above 2019; AI data-centre energy demand grew; 2030 net-zero goal and competitive pressure remain. No algorithmic-discrimination strand.\n\n"
    "### ENVIRONMENTAL ETHICS DOCTRINE\n\n"
    "- **Anthropocentric:** nature valued chiefly for human interests; useful but may under-protect non-instrumental ecological value.\n"
    "- **Biocentric:** living beings have inherent worth; difficult conflicts arise where basic human survival is involved.\n"
    "- **Ecocentric:** value attaches to ecosystem wholes and processes; must not erase sustainable traditional community use.\n"
    "- **Sustainable development:** present needs without compromising future generations' ability to meet their needs, Brundtland 1987.\n"
    "- **Intergenerational equity:** present officials represent future persons who cannot vote or contest today's depletion.\n"
    "- **Precaution:** serious or irreversible risk plus uncertainty justifies proportionate preventive action; Rio Principle 15 uses 'precautionary approach'.\n"
    "- **Polluter-pays:** polluter bears prevention, remediation and compensation; payment is not a licence to pollute.\n"
    "- **Environmental justice:** test distribution of benefits and burdens, meaningful voice, recognition, compensation and remedy.\n"
    "- **Vellore, 1996:** tannery effluent in the Palar setting; sustainable development, precaution and polluter-pays recognised in Indian environmental law. It is not a general environmental code or AI law.\n"
    "- **CBDR-RC:** common climate duty differentiated by historical contribution and respective capability; developing-country duty is differentiated, not absent.\n\n"
    "### CLEARANCE, SECURITY AND COMMUNITY\n\n"
    "- **Border method:** specify legitimate security objective -> compare routes and technologies -> rigorous EIA and cumulative/disaster risk -> least-damaging feasible alternative.\n"
    "- **Secrecy discipline:** consult communities and publish non-sensitive reasons; genuinely classified facts may be reviewed by cleared independent experts.\n"
    "- **Conditions:** seasonal controls, wildlife passages, restoration, monitoring, stop triggers and compliance reporting.\n"
    "- **2025 Q2(b):** reject both automatic national-security exemption and automatic ecological prohibition.\n"
    "- **2025 Q8 facts:** age-old trees, medicinal plants, biodiversity, micro-climate and rainfall, wildlife habitat, soil fertility, erosion control, tribal and nomadic livelihoods, housing duty, wildlife conflict and alleged hideouts. Do not invent degradation, city-periphery or court monitoring.\n\n"
    "### CURRENT OFFICIAL ANCHOR\n\n"
    "- **India AI Governance Guidelines:** policy guidance organised through principles, recommendations, action plan and practical guidance, with voluntary commitments and focus on fairness, accountability, safety, inclusivity, transparency, risk classification, oversight, testing and grievance.\n"
    "- **India AI Impact Summit 2026:** 19-20 February at Bharat Mandapam within the 16-20 February programme; people-centric, inclusive and protect-planet framing; official challenges include employment disruption, bias and energy consumption.\n"
    "- **Limit:** neither anchor is a comprehensive AI statute or proof of a deployed system's fairness, safety or carbon performance.\n\n"
    "### TWELVE-PYQ ANSWER SPINES\n\n"
    "- **2018 Q10:** relief and evidence -> conditional closure/restart -> polluter-funded restoration -> worker transition -> participatory monitoring.\n"
    "- **2020 Q5(b):** liberating and disruptive internet values -> rights-based critical adaptation.\n"
    "- **2021 Q2(a):** digital evidence benefits -> data and context limits -> supervised, appealable use.\n"
    "- **2022 Q4(b):** online access benefits -> capability divide and privacy -> assisted and offline channels.\n"
    "- **2023 Q12:** child welfare and evidence -> pros/cons of counter-video -> anonymised correction and institutional remedy.\n"
    "- **2024 Q1(a):** benefit -> bias, opacity, reliability and de-skilling -> audit, oversight and contestability.\n"
    "- **2024 Q2(b):** greed and temperance -> intergenerational justice -> sustainable and differentiated transition.\n"
    "- **2024 Q7:** preserve emissions, energy, net-zero and competition facts -> lifecycle plan and audited milestones.\n"
    "- **2024 Q12:** refuse manipulation, consent bypass and patent misuse -> escalate -> lawful accelerated research.\n"
    "- **2025 Q1(a):** map paired social-media dilemmas -> platform, user and state safeguards.\n"
    "- **2025 Q2(b):** security purpose -> least-damage EIA -> classified review and public reasons.\n"
    "- **2025 Q8:** dignity and shelter versus complete ecosystem services -> alternatives first -> minimum residual diversion.\n\n"
    "### FINAL ANSWER METHOD\n\n"
    "1. Identify whether the demand is AI, data, social-media, climate, pollution, clearance or combined ethics.\n"
    "2. State a qualified thesis: innovation or development is legitimate only within rights, ecological limits and accountable institutions.\n"
    "3. Name the exact mechanism: bias stage, opacity, automation bias, consent failure, precaution, polluter-pays, environmental justice or CBDR-RC.\n"
    "4. Add one verified Indian constitutional, judicial, statutory, PYQ or current-policy anchor with its date and limit.\n"
    "5. For cases, map stakeholders including vulnerable communities, non-human ecology and future generations; list options and consequences.\n"
    "6. Recommend operational safeguards: owner, test, reason, appeal, EIA, alternative, monitoring, remedy and stop trigger.\n"
    "7. Test the strongest counterpoint: efficiency, secrecy, innovation, livelihood, security or measurement uncertainty.\n"
    "8. Conclude with a reviewable balance, never a slogan, false statutory claim or invented case fact."
)
