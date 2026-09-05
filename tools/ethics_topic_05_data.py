"""Learner-v2 source data: Ethics Topic 05, Emotional Intelligence in Administration."""

SESSION_TITLES = (
    "What emotional intelligence is: definitions and the three models",
    "The four-branch ability model (Mayer-Salovey 1997)",
    "Goleman's five components and their administrative translation",
    "Emotional labour, IQ-vs-EQ and the dark side of EI",
    "EI in disaster leadership: the DC Vijay case study",
    "Empathy, compassion and wisdom in administration",
    "EI and crisis of conscience; moral intuition versus moral reasoning",
    "Institutional design for sustained EI: Mission Karmayogi and NDMA",
    "Answer architecture: directive decoding and selectable evidence units",
    "PYQ masterclass, probable questions and consolidated revision",
)

SESSION_GROUPS = (
    ("1", "2"),
    ("3",),
    ("4",),
    ("5",),
    ("6",),
    ("7",),
    ("8",),
    ("9",),
    ("10",),
    ("11", "12", "13"),
)

MCQ_ITEMS = (
    # --- Family 1: EI models and provenance ---
    {
        "label": "Salovey-Mayer 1990 definition is the academic origin",
        "statement": (
            "Salovey and Mayer (1990) defined emotional intelligence as the ability to "
            "monitor one's own and others' feelings and emotions, to discriminate among "
            "them, and to use this information to guide thinking and action; this is the "
            "foundational academic definition, distinct from Goleman's later popularisation."
        ),
        "scenario_a": (
            "A training module credits Daniel Goleman with originating the concept of "
            "emotional intelligence in 1995. A participant objects, citing a 1990 academic "
            "paper. Which provenance correction is accurate and why does the distinction "
            "matter for a GS-IV answer?"
        ),
        "scenario_b": (
            "A probationer defines EI as the ability to suppress negative emotions during "
            "public interaction. Which part of the 1990 Salovey-Mayer definition shows "
            "that regulation, not suppression, is the correct framing?"
        ),
        "family": "EI models and provenance",
    },
    {
        "label": "Mayer-Salovey 1997 four-branch ability model is a revision",
        "statement": (
            "The 1997 Mayer-Salovey four-branch ability model revises the 1990 definition "
            "into an ascending hierarchy: perceiving emotion, using emotion to facilitate "
            "thought, understanding emotion, and managing emotion; it treats EI as a genuine "
            "cognitive ability measurable by performance-based tests such as the MSCEIT."
        ),
        "scenario_a": (
            "An officer claims she has high EI because a self-report questionnaire rated "
            "her social confidence highly. Which methodological feature of the ability "
            "model challenges the validity of self-report for measuring EI?"
        ),
        "scenario_b": (
            "A disaster-management trainer ranks EI skills as four levels: noticing "
            "distress signals, channelling urgency into action, reading competing "
            "emotional claims, and regulating grief during command. Which established "
            "model does this hierarchy correspond to?"
        ),
        "family": "EI models and provenance",
    },
    {
        "label": "Goleman's five workplace competencies are a mixed model",
        "statement": (
            "Daniel Goleman's Emotional Intelligence (1995) and his 1998 Harvard Business "
            "Review formulation reframe EI as five workplace competencies — self-awareness, "
            "self-regulation, motivation, empathy and social skill — blending cognitive "
            "ability with personality and motivational traits into a mixed/competency model."
        ),
        "scenario_a": (
            "A civil-service foundation course teaches self-awareness, self-regulation, "
            "motivation, empathy and social skill as the five pillars of emotional "
            "intelligence. Which theoretical model is being used and how does it differ "
            "from the ability model?"
        ),
        "scenario_b": (
            "A selection committee argues that Goleman's model proves EI is entirely "
            "innate and unmeasurable. Which feature of the competency model — its "
            "emphasis on trainable workplace skills — contradicts this claim?"
        ),
        "family": "EI models and provenance",
    },
    {
        "label": "Bar-On EQ-i is a trait model distinct from ability measures",
        "statement": (
            "Bar-On's Emotional Quotient Inventory (EQ-i, technical manual 1997) treats "
            "EI as a constellation of self-perceived emotional and social competencies "
            "measured by self-report; it is useful for training-needs assessment but more "
            "contested as a predictor of actual behaviour, and methodologically different "
            "from performance-based ability tests."
        ),
        "scenario_a": (
            "A state government uses a self-report EQ-i questionnaire to select officers "
            "for disaster-management postings. A psychometrician warns that self-report "
            "may not predict actual crisis behaviour. Which model distinction supports "
            "the psychometrician's concern?"
        ),
        "scenario_b": (
            "A researcher claims that all EI models measure the same construct. Which "
            "comparison between the ability model (performance-based MSCEIT), the mixed "
            "model (competency-based) and the trait model (self-report EQ-i) shows that "
            "they differ in both theory and method?"
        ),
        "family": "EI models and provenance",
    },
    # --- Family 2: Self-awareness and self-regulation ---
    {
        "label": "Self-awareness is the precondition for all EI",
        "statement": (
            "Self-awareness is the capacity to recognise when personal stress, fatigue "
            "or bias is affecting judgment; it is the precondition for every other EI "
            "component because an officer who does not detect her own emotional state "
            "cannot regulate, channel or communicate it effectively."
        ),
        "scenario_a": (
            "A magistrate handling a communally sensitive case notices rising irritation "
            "when a particular community's representative speaks. She pauses before "
            "responding. Which EI component is activated at the moment of recognition, "
            "and why is it the necessary first step?"
        ),
        "scenario_b": (
            "An IAS officer consistently makes hasty decisions during late-night crisis "
            "calls but does not connect his impulsiveness to exhaustion. Which EI deficit "
            "explains why his decision quality deteriorates under fatigue?"
        ),
        "family": "Self-awareness and self-regulation",
    },
    {
        "label": "Self-regulation converts awareness into composed conduct",
        "statement": (
            "Self-regulation is the capacity to convert emotional awareness into composed, "
            "proportionate conduct under provocation, protest, disaster or media scrutiny; "
            "it does not mean suppressing emotion but channelling it into deliberate, "
            "ethically appropriate action."
        ),
        "scenario_a": (
            "During a violent protest outside the collectorate, a district collector "
            "recognises her fear but speaks calmly to the crowd, orders proportionate "
            "force and ensures medical response. Which EI component explains her "
            "transition from internal distress to controlled public action?"
        ),
        "scenario_b": (
            "A senior officer under media attack for a policy decision bottles up all "
            "emotion and issues no public statement for weeks. A subordinate describes "
            "him as having high self-regulation. Why is this characterisation inaccurate "
            "under the EI framework?"
        ),
        "family": "Self-awareness and self-regulation",
    },
    {
        "label": "Suppressing emotion is not self-regulation",
        "statement": (
            "A common exam trap equates emotional intelligence with eliminating all emotion; "
            "self-regulation requires recognising and managing emotion appropriately, not "
            "denying or suppressing it — suppression without awareness can lead to burnout, "
            "delayed outbursts or poor empathic engagement."
        ),
        "scenario_a": (
            "A training instructor advises new recruits to feel nothing during citizen "
            "grievance hearings. A psychologist objects that this risks burnout. Which "
            "distinction between suppression and regulation resolves the disagreement?"
        ),
        "scenario_b": (
            "An officer who never displays emotion is praised as the most composed "
            "administrator in the state. However, she frequently makes decisions without "
            "considering citizen distress. Which EI component is she missing despite "
            "apparent composure?"
        ),
        "family": "Self-awareness and self-regulation",
    },
    {
        "label": "Self-awareness detects when intuition may be biased",
        "statement": (
            "Self-awareness enables an officer to detect when a strong intuitive reaction "
            "— anger, sympathy or disgust — may be biasing judgment, prompting a deliberate "
            "reasoning check before acting; it is the regulatory bridge between moral "
            "intuition and moral reasoning."
        ),
        "scenario_a": (
            "A welfare officer feels immediate sympathy for an applicant who reminds her "
            "of her own mother and is about to waive a documentation requirement without "
            "checking eligibility. Which EI mechanism should intervene before the "
            "decision becomes favouritism?"
        ),
        "scenario_b": (
            "An officer instinctively distrusts a repeat complainant and is inclined to "
            "reject a genuine grievance. Which cognitive check, enabled by self-awareness, "
            "prevents the intuitive reaction from becoming an unjust decision?"
        ),
        "family": "Self-awareness and self-regulation",
    },
    # --- Family 3: Empathy and social skill in administration ---
    {
        "label": "Empathy reads unstated citizen needs",
        "statement": (
            "Empathy in administration is the capacity to grasp the unstated needs of a "
            "citizen — an illiterate applicant's confusion, a disaster victim's trauma, "
            "a differently-abled person's accessibility barrier — and adapt service "
            "delivery accordingly, without requiring the citizen to articulate the need."
        ),
        "scenario_a": (
            "An elderly applicant stands silently at a pension counter, unable to "
            "understand the form. The clerk notices his confusion and switches to "
            "vernacular explanation. Which EI component is being exercised and how "
            "does it differ from merely following a process manual?"
        ),
        "scenario_b": (
            "A disaster relief coordinator distributes supplies efficiently but does "
            "not notice that displaced families are traumatised and need psychological "
            "support. Which EI component is absent despite operational competence?"
        ),
        "family": "Empathy and social skill in administration",
    },
    {
        "label": "Empathy informs how rules are applied, not whether",
        "statement": (
            "Empathy in administration informs how a rule-bound decision is communicated "
            "and delivered, not whether the rule itself is waived arbitrarily; the common "
            "trap is to equate empathy with bending rules for anyone who appears "
            "distressed, which conflates compassion with favouritism."
        ),
        "scenario_a": (
            "A sub-divisional magistrate must reject a land claim that lacks statutory "
            "documents. She explains the rejection in the applicant's language, outlines "
            "the appeal process and connects him to legal aid. Which EI component shapes "
            "her conduct without altering the legal outcome?"
        ),
        "scenario_b": (
            "An officer waives all documentation requirements for a weeping applicant "
            "without any published criterion for the waiver. A colleague calls this "
            "empathy. Why is the correct classification favouritism rather than "
            "empathetic administration?"
        ),
        "family": "Empathy and social skill in administration",
    },
    {
        "label": "Social skill enables coordination and conflict resolution",
        "statement": (
            "Social skill in administration enables coordination across departments, "
            "conflict resolution among stakeholders, and effective communication of "
            "unpopular but necessary decisions; it is the outward-facing component that "
            "converts internal EI competence into organisational and public outcomes."
        ),
        "scenario_a": (
            "A joint secretary must coordinate between the health ministry and the "
            "finance ministry on pandemic procurement. She structures stakeholder "
            "meetings to surface each ministry's constraints before proposing a "
            "solution. Which EI component is she deploying?"
        ),
        "scenario_b": (
            "A district collector must announce an unpopular lockdown extension. He "
            "explains the epidemiological rationale, acknowledges economic hardship and "
            "announces mitigation measures. Which EI component makes this communication "
            "effective rather than merely authoritative?"
        ),
        "family": "Empathy and social skill in administration",
    },
    {
        "label": "Wisdom in administration requires empathy as its trigger",
        "statement": (
            "Wisdom in administration (practical judgment or phronesis) requires empathy "
            "to trigger contextual sensitivity; without empathy, a procedurally correct "
            "official applies rules mechanically and may produce a travesty of justice "
            "that follows the letter of a rule while defeating its purpose."
        ),
        "scenario_a": (
            "A counter clerk denies a genuine welfare claimant's application because a "
            "single supporting document has a minor clerical error, despite clear "
            "substantive eligibility. Which concept explains the failure to exercise "
            "contextual judgment?"
        ),
        "scenario_b": (
            "A district collector notices that strict enforcement of a building "
            "regulation would displace a community of elderly residents with nowhere "
            "to go. She exercises discretion within the law to allow a compliance "
            "timeline. Which pair of concepts — empathy and wisdom — explains her "
            "decision?"
        ),
        "family": "Empathy and social skill in administration",
    },
    # --- Family 4: Emotional labour and EI's dark side ---
    {
        "label": "Emotional labour is a real cost of public-facing roles",
        "statement": (
            "Emotional labour (Hochschild, The Managed Heart, 1983) is the effort "
            "required to manage one's displayed emotions to meet professional role "
            "demands; it is administratively necessary for composed citizen-facing "
            "service but psychologically costly if sustained without institutional "
            "support such as rotation, debrief mechanisms and staff grievance channels."
        ),
        "scenario_a": (
            "A citizen-grievance counter clerk maintains courtesy for eight hours daily "
            "despite repeated verbal abuse. After two years she develops chronic "
            "exhaustion. Which concept explains the psychological cost and what "
            "institutional response is indicated?"
        ),
        "scenario_b": (
            "A state government argues that empathetic officers do not need burnout "
            "support because their natural disposition protects them. Which Hochschild-"
            "derived insight shows that emotional labour carries burnout risk regardless "
            "of natural empathy?"
        ),
        "family": "Emotional labour and EI dark side",
    },
    {
        "label": "High EI without integrity enables manipulation",
        "statement": (
            "Emotional intelligence is ethically neutral: a socially skilled official "
            "with accurate empathic reading can use that skill to manipulate vulnerable "
            "citizens rather than serve them — for example, exploiting a citizen's "
            "urgency to extract a bribe. EI's public value depends on being paired "
            "with integrity."
        ),
        "scenario_a": (
            "A licensing officer accurately reads an applicant's desperation to start "
            "a business before a deadline and says the file can be expedited for an "
            "unofficial fee. Which feature of EI is being used and which foundational "
            "value is absent?"
        ),
        "scenario_b": (
            "A colleague argues that training officers in emotional intelligence will "
            "automatically reduce corruption. Which boundary condition of EI — its "
            "ethical neutrality — shows that this claim is incomplete?"
        ),
        "family": "Emotional labour and EI dark side",
    },
    {
        "label": "EI does not guarantee ethical conduct",
        "statement": (
            "High emotional intelligence does not guarantee ethical conduct because EI "
            "is a capacity, not a moral compass; integrity, probity and institutional "
            "oversight must be independently assessed and maintained — EI and ethics "
            "are jointly necessary, neither alone is sufficient."
        ),
        "scenario_a": (
            "A charismatic administrator uses her social skill to build trust with "
            "contractors and then steers procurement toward preferred firms. External "
            "auditors detect the pattern. Which analytical distinction — EI as capacity "
            "versus ethics as direction — explains the failure?"
        ),
        "scenario_b": (
            "An ethics curriculum treats EI training as a complete substitute for "
            "vigilance and audit mechanisms. Which limitation of EI as a concept "
            "makes this design dangerous?"
        ),
        "family": "Emotional labour and EI dark side",
    },
    {
        "label": "Overemphasis on composure can suppress legitimate dissent",
        "statement": (
            "If self-regulation is institutionally enforced as unquestioning composure, "
            "it can suppress legitimate whistleblowing and dissent — a stay calm and do "
            "not rock the boat culture; EI must therefore be paired with courage and "
            "institutional channels for safe dissent."
        ),
        "scenario_a": (
            "A junior officer notices systematic procurement fraud but is told by "
            "seniors to remain calm and not create unnecessary controversy. She complies "
            "and the fraud continues. Which misapplication of EI is enabling the "
            "institutional failure?"
        ),
        "scenario_b": (
            "A department praises officers who never raise uncomfortable questions as "
            "having the best emotional intelligence. Which conceptual error does this "
            "institutional culture embody?"
        ),
        "family": "Emotional labour and EI dark side",
    },
    # --- Family 5: EI, crisis and moral dimensions ---
    {
        "label": "EI mediates between stress and ethical decision quality",
        "statement": (
            "Emotional intelligence mediates the relationship between stress or pressure "
            "and ethical decision quality in administration; under acute stress, an "
            "officer with high EI perceives, channels and regulates emotional responses "
            "so that ethical reasoning is not overwhelmed by panic, grief or anger."
        ),
        "scenario_a": (
            "During a communal riot, a superintendent of police must order crowd "
            "dispersal while his own community is among the protesters. His decision "
            "is lawful, proportionate and timely. Which EI mechanism explains how he "
            "maintained ethical decision quality under extreme personal stress?"
        ),
        "scenario_b": (
            "An officer under investigation for a false allegation makes an impulsive "
            "public statement that damages her defence. Which EI deficit — failure to "
            "regulate under personal threat — explains the error?"
        ),
        "family": "EI crisis and moral dimensions",
    },
    {
        "label": "Moral intuition draws on EI's empathy and self-awareness",
        "statement": (
            "Moral intuition is the fast, affect-driven judgment that something feels "
            "wrong before any deliberate analysis; it draws directly on EI's empathy "
            "and self-awareness components and serves as an early-warning signal that "
            "triggers deliberate moral reasoning."
        ),
        "scenario_a": (
            "A revenue officer reviewing land acquisition files feels uneasy about a "
            "particular case despite all documents being in order. Further investigation "
            "reveals forged signatures. Which cognitive process provided the initial "
            "signal and which EI components supported it?"
        ),
        "scenario_b": (
            "A candidate writes that moral intuition is unreliable and should always be "
            "overridden by rational analysis. Which nuanced position — that intuition is "
            "a trigger for reasoning, not its substitute — provides a more defensible "
            "GS-IV answer?"
        ),
        "family": "EI crisis and moral dimensions",
    },
    {
        "label": "EI helps overcome crisis of conscience without compromising ethics",
        "statement": (
            "A crisis of conscience occurs when personal values, professional duty and "
            "situational pressures pull in conflicting directions; EI helps by enabling "
            "the officer to perceive the conflict clearly (self-awareness), regulate "
            "the emotional turmoil (self-regulation), and communicate the chosen course "
            "transparently (social skill) — without abandoning the ethical stand."
        ),
        "scenario_a": (
            "An officer ordered to demolish an unauthorised settlement knows the "
            "residents are genuinely destitute. She feels anguish but carries out the "
            "order after securing rehabilitation commitments and documenting the process. "
            "Which EI components enabled her to act on duty without abandoning compassion?"
        ),
        "scenario_b": (
            "A junior officer facing a crisis of conscience simply freezes and takes no "
            "action, waiting for the dilemma to resolve itself. Which EI deficit — "
            "failure to regulate emotional conflict into deliberate decision — explains "
            "the paralysis?"
        ),
        "family": "EI crisis and moral dimensions",
    },
    {
        "label": "EQ and IQ are jointly necessary; neither alone suffices",
        "statement": (
            "EQ (emotional quotient) predicts how well cognitive competence is deployed "
            "under interpersonal and ethical pressure, while IQ predicts task-competence "
            "and technical problem-solving; the defensible GS-IV position is that they "
            "are jointly necessary, with EQ mattering disproportionately at the point "
            "of execution under stress."
        ),
        "scenario_a": (
            "Two officers with identical UPSC ranks face the same law-and-order crisis. "
            "One de-escalates through empathic communication; the other's technically "
            "correct order triggers panic because of insensitive delivery. Which concept "
            "explains the divergent outcomes?"
        ),
        "scenario_b": (
            "A candidate argues that EQ alone determines administrative success and IQ "
            "is irrelevant. Which counterexample — an empathetic but legally uninformed "
            "officer making a wrong decision — shows why this claim is indefensible?"
        ),
        "family": "EI crisis and moral dimensions",
    },
    # --- Family 6: Institutional and policy dimensions ---
    {
        "label": "Individual EI cannot substitute for institutional crisis-preparedness",
        "statement": (
            "Sustainable EI in administration cannot rest on individual resilience alone; "
            "institutions must provide structural supports — delegation protocols during "
            "crises, peer-support and debrief mechanisms after trauma, and rotation "
            "policies for high-stress postings — because individual willpower has "
            "diminishing returns without systemic backing."
        ),
        "scenario_a": (
            "A district collector posted in a disaster-prone area for seven years "
            "without rotation develops compassion fatigue and makes increasingly poor "
            "decisions. Which institutional failure explains the deterioration despite "
            "her initially high EI?"
        ),
        "scenario_b": (
            "A state argues that selecting high-EI officers for crisis postings "
            "eliminates the need for delegation protocols and debrief mechanisms. "
            "Which principle of institutional design shows why this reasoning is "
            "flawed?"
        ),
        "family": "Institutional and policy dimensions",
    },
    {
        "label": "Mission Karmayogi provides a competency-based learning architecture",
        "statement": (
            "Mission Karmayogi and the Karmayogi Competency Model (KCM) align roles "
            "with required competencies "
            "and embed competencies in role-based learning; applying this architecture "
            "to emotional intelligence is an analytical proposal unless a named EI "
            "module is independently verified."
        ),
        "scenario_a": (
            "An officer completes role-based competency courses but continues to bully "
            "subordinates. Which distinction between learning completion and behavioural "
            "internalisation explains why the architecture cannot certify EI?"
        ),
        "scenario_b": (
            "A policy analyst claims Mission Karmayogi has solved the EI deficit in the "
            "civil services, although no named EI module is cited. Which provenance "
            "caution qualifies this claim?"
        ),
        "family": "Institutional and policy dimensions",
    },
    {
        "label": "Crisis delegation protocols convert EI dilemmas into institutional scenarios",
        "statement": (
            "Crisis-management training should build in delegation-of-command and "
            "family-emergency contingency provisions, converting dilemmas like the "
            "DC Vijay case from individual moral burdens into foreseen institutional "
            "scenarios with pre-agreed protocols — reducing reliance on personal "
            "heroism."
        ),
        "scenario_a": (
            "A district magistrate leading earthquake relief learns that her child is "
            "critically ill. No delegation protocol exists. She must choose between "
            "command and family in real time. Which institutional design failure has "
            "converted a manageable scenario into a personal crisis?"
        ),
        "scenario_b": (
            "A state government pre-designates a succession protocol for disaster "
            "commanders, including a family-emergency clause with temporary command "
            "transfer. When activated, the commander briefly attends to family while "
            "a trained deputy continues operations. Which design principle has "
            "converted an EI dilemma into an institutional routine?"
        ),
        "family": "Institutional and policy dimensions",
    },
    {
        "label": "Competency modules cannot substitute for structural protocols",
        "statement": (
            "Competency-based training in emotional and behavioural skills can support "
            "individual capacity but remains an insufficient institutional response; it must "
            "be supplemented by structural crisis-management protocols, citizen feedback "
            "loops and mental-health support to produce durable, ethically grounded "
            "administrative EI."
        ),
        "scenario_a": (
            "A state invests heavily in behavioural training but provides no "
            "post-disaster psychological support for frontline officers. After a major "
            "flood, several officers show signs of PTSD. Which institutional gap "
            "explains why training alone was insufficient?"
        ),
        "scenario_b": (
            "A reform proposal combines verified EI training, mandatory post-crisis "
            "debrief, peer-counselling networks and three-year rotation for disaster-"
            "prone postings. Why is this package more durable than any single "
            "component alone?"
        ),
        "family": "Institutional and policy dimensions",
    },
)

MCQ_ITEMS = tuple({**item, "group": item["family"]} for item in MCQ_ITEMS)

PYQS = (
    {
        "year": 2013,
        "question": (
            "What is 'emotional intelligence' and how can it be developed in people? "
            "How does it help an individual in taking ethical decisions? (Answer in "
            "150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Named in Basic owner section 7. Neutral rendering from PYQ routing "
            "ledger. Verify exact wording against locally held official 2013 GS-IV "
            "paper if available."
        ),
        "answer": (
            "Emotional intelligence is the ability to perceive, understand, regulate "
            "and use one's own and others' emotions to guide thought and action "
            "(Salovey and Mayer, 1990). Goleman's five components — self-awareness, "
            "self-regulation, motivation, empathy and social skill — provide the "
            "operational framework.\n\n"
            "EI can be developed through structured reflection on one's emotional "
            "responses, feedback from peers and mentors, empathy-building exercises "
            "such as community immersion during probation, and repeated practice in "
            "high-stress simulations. Mission Karmayogi supplies a role-based competency "
            "learning architecture, but the cited official pages do not verify a named "
            "EI module and course completion would not prove internalisation.\n\n"
            "EI helps ethical decisions by enabling the officer to detect personal "
            "bias before it shapes a decision (self-awareness), maintain composure "
            "under pressure so that reasoning is not overwhelmed (self-regulation), "
            "and perceive a citizen's unstated distress so that rule application is "
            "contextually sensitive (empathy). However, EI is ethically neutral — it "
            "must be paired with integrity to ensure that emotional skill serves "
            "citizens rather than manipulates them."
        ),
    },
    {
        "year": 2019,
        "question": (
            "(b) What do you understand by the term 'emotional intelligence'? "
            "Describe its utility in making emotions work for you in the "
            "administrative set-up. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Routed from PYQ routing ledger: 2019 GS-IV Q5(b). Part (a) on probity "
            "routes to Topic 14. Neutral rendering; verify exact wording against "
            "locally held official 2019 GS-IV paper."
        ),
        "answer": (
            "Emotional intelligence is the subset of social intelligence involving "
            "the capacity to monitor, discriminate among and use one's own and others' "
            "emotions to guide thinking and action (Salovey and Mayer, 1990).\n\n"
            "In administration, EI makes emotions work for the officer rather than "
            "against her. Self-awareness lets her recognise when fatigue or frustration "
            "is clouding judgment, enabling a pause before a consequential decision. "
            "Self-regulation channels anger during a hostile public meeting into calm, "
            "firm communication rather than reactive force. Motivation sustains public-"
            "service commitment when external rewards are weak. Empathy allows a "
            "frontline officer to read an illiterate applicant's confusion and adapt "
            "the explanation process without the citizen needing to articulate the "
            "difficulty. Social skill converts internal composure into effective "
            "coordination across departments and stakeholder conflict resolution.\n\n"
            "The limit is that EI amplifies whatever ethical orientation already exists. "
            "An officer with high EI but low integrity can exploit emotional reading "
            "to manipulate rather than serve. EI must therefore operate within an "
            "ethical framework of probity and accountability."
        ),
    },
    {
        "year": 2020,
        "question": (
            "(b) What are the main components of emotional intelligence (EI)? Can "
            "they be learned? Discuss. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Routed from PYQ routing ledger: 2020 GS-IV Q2(b). Part (a) on hatred "
            "and wisdom co-routes. Named in Basic owner section 7 and Advanced "
            "owner section 10. Verify exact wording against locally held official "
            "2020 GS-IV paper."
        ),
        "answer": (
            "Goleman's five components of emotional intelligence are: self-awareness "
            "(recognising one's emotional state), self-regulation (managing impulses "
            "and maintaining composure), motivation (intrinsic drive toward public "
            "purpose beyond incentive), empathy (perceiving others' unstated needs) "
            "and social skill (managing relationships, teams and conflict).\n\n"
            "These components can be learned, though with differing ceilings. The "
            "ability-competency distinction is key: the Mayer-Salovey ability model "
            "acknowledges innate variation, but Goleman's competency model emphasises "
            "that deliberate practice improves each component. Structured reflection, "
            "peer feedback, community-immersion exercises and crisis simulations "
            "during foundation training all develop EI. Mission Karmayogi's "
            "competency-based learning extends this into career-long development.\n\n"
            "The qualification is that training can improve EI skills without making "
            "every trainee equally proficient. Individual capacity varies, and "
            "institutional support — delegation protocols, rotation and debrief — "
            "complements what individual training achieves. Learning architecture "
            "enables development; it does not certify mastery."
        ),
    },
    {
        "year": 2021,
        "question": (
            "(b) Is it possible for emotional intelligence to help in overcoming "
            "a crisis of conscience without compromising the ethical stand that "
            "one may like to take? Critically examine. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Routed from PYQ routing ledger: 2021 GS-IV Q4(b). Part (a) on "
            "building attitude routes to Topic 03. Neutral rendering; verify "
            "exact wording against locally held official 2021 GS-IV paper."
        ),
        "answer": (
            "A crisis of conscience arises when personal values, professional duty "
            "and situational pressures pull in conflicting directions. Emotional "
            "intelligence helps navigate this without ethical compromise through "
            "three mechanisms.\n\n"
            "First, self-awareness enables the officer to name the conflict precisely "
            "rather than experiencing it as diffuse anguish. Second, self-regulation "
            "prevents the emotional turmoil from producing impulsive action or "
            "paralysis — the officer remains composed enough to reason through "
            "options. Third, social skill allows transparent communication of the "
            "chosen course to stakeholders, converting a solitary moral burden into "
            "a documented, accountable decision.\n\n"
            "Critical examination requires acknowledging limits. EI provides the "
            "psychological infrastructure for managing the crisis but does not itself "
            "supply the ethical standard. The officer still needs a moral framework "
            "— deontological, consequentialist or virtue-based — to determine which "
            "stand to take. EI without ethical grounding can produce composed "
            "capitulation rather than principled resolution. The verdict is that EI "
            "is necessary for navigating a crisis of conscience but insufficient "
            "without independent ethical reasoning."
        ),
    },
    {
        "year": 2022,
        "question": (
            "(a) Wisdom is a prerequisite for good administration. Critically "
            "evaluate in the context of 'travesty of justice' in service delivery. "
            "(b) Empathy and compassion are the catalysts for good human relations. "
            "Explain why they are considered vital attributes for a civil servant. "
            "(Answer in 150 words each)"
        ),
        "marks": 20,
        "source_note": (
            "Routed from PYQ routing ledger: 2022 GS-IV Q1(a)-(b). Jointly "
            "routes here and to Topic 09. Named in Basic owner section 11. "
            "Neutral rendering; verify exact wording against locally held "
            "official 2022 GS-IV paper."
        ),
        "answer": (
            "(a) Wisdom in administration is practical judgment, or phronesis: the "
            "capacity to apply law and policy with contextual sensitivity under "
            "uncertainty. It differs from mere intelligence because it joins knowledge, "
            "experience, foresight and ethical purpose. A travesty of justice occurs "
            "when literal compliance defeats the object of a rule. For example, denying "
            "an otherwise eligible pensioner because an easily correctable document is "
            "missing may satisfy procedure while frustrating social justice. A wise "
            "officer verifies eligibility, records reasons, facilitates correction and "
            "uses lawful discretion or appeal rather than simply waiving the rule. "
            "Empathy supplies the warning that mechanical application is causing human "
            "harm; legal competence identifies the permissible remedy. Yet wisdom must "
            "remain reviewable: unrecorded discretion can become favouritism. Transparent "
            "reasons, consistent criteria and appeal mechanisms therefore convert "
            "contextual sensitivity into accountable justice. Wisdom is thus a "
            "prerequisite for good administration, but only when disciplined by law.\n\n"
            "(b) Empathy is the capacity to understand another person's perspective and "
            "emotional condition; compassion adds the motivation to relieve avoidable "
            "suffering. They are vital to civil service because citizens often approach "
            "the state while distressed, ill-informed or structurally disadvantaged. "
            "An empathetic counter officer notices an elderly applicant's confusion and "
            "explains the procedure patiently. A compassionate district administration "
            "then converts that insight into institutional reform through assisted filing, "
            "vernacular forms, disability access or doorstep delivery. These attributes "
            "improve trust, grievance handling, conflict resolution and team leadership, "
            "and prevent technically correct administration from becoming indifferent. "
            "However, empathy is not permission to bend rules for the most emotionally "
            "persuasive claimant. It must operate through objective eligibility, recorded "
            "reasons and equal access. The balanced position is compassionate delivery "
            "within an impartial legal framework."
        ),
    },
    {
        "year": 2023,
        "question": (
            "(a) 'Emotional intelligence is the ability to make your emotions work "
            "for you instead of against you.' Do you agree with this view? Discuss. "
            "(b) Differentiate between moral intuition and moral reasoning with "
            "suitable examples. (Answer in 150 words each)"
        ),
        "marks": 20,
        "source_note": (
            "Routed from PYQ routing ledger: 2023 GS-IV Q4(a)-(b). Named in "
            "Basic owner section 10. Part (b) cross-references Topics 08 and 10. "
            "Neutral rendering; verify exact wording against locally held "
            "official 2023 GS-IV paper."
        ),
        "answer": (
            "(a) The claim is substantially correct because EQ determines how well "
            "knowledge and cognitive ability are deployed under interpersonal pressure. "
            "Self-awareness detects when fatigue, fear or bias is distorting judgment. "
            "Self-regulation channels anger into firm communication instead of impulsive "
            "force. Empathy reads citizen distress and social skill coordinates teams or "
            "de-escalates a crowd. Motivation sustains duty when external rewards are "
            "weak. Thus two officers with similar IQ and legal knowledge may produce "
            "different crisis outcomes: the officer who regulates panic and communicates "
            "credibly can execute the technically sound plan. However, the quotation must "
            "not be read as making EQ a substitute for competence. An empathetic but "
            "legally uninformed officer may still decide wrongly, while emotional skill "
            "without integrity may enable manipulation. IQ, EQ and ethical orientation "
            "are therefore complementary: IQ supplies analytical content, EQ enables "
            "effective execution, and integrity directs both toward public service.\n\n"
            "(b) Moral intuition is a rapid, affect-laden judgment that an act feels right "
            "or wrong before deliberate analysis. It draws on experience, empathy and "
            "self-awareness. Moral reasoning is the slower, conscious examination of "
            "facts, duties, consequences and principles to justify or correct that first "
            "response. For example, a procurement officer senses that a single-bid award "
            "is improper because of suspicious familiarity between actors; she then checks "
            "the tender record, conflict-of-interest rules and reasons for limited "
            "competition. Conversely, an intuitive distrust of a claimant from a "
            "stigmatised group may be prejudice, which constitutional equality and evidence "
            "must correct. Intuition is therefore an early-warning signal, not proof. "
            "Self-awareness bridges the two by asking whether the feeling arises from "
            "relevant experience or personal bias. Sound ethical judgment lets intuition "
            "trigger inquiry and lets reason test the intuition before action."
        ),
    },
    {
        "year": 2025,
        "question": (
            "Q7 Section B case study: Deputy Commissioner 'Vijay' leading disaster "
            "relief (cloudburst, 200+ deaths, ~5,000 injured, road and telecom "
            "disrupted) while his mother dies during the crisis and family pressure "
            "mounts to travel for last rites. Address: (a) options available; "
            "(b) ethical dilemmas; (c) critical evaluation of each option; and "
            "(d) the most appropriate option with reasons. (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Named in Basic owner section 3.6 and Advanced owner section 3. "
            "This is a Section B case study; the demand is to analyse the "
            "dilemma using EI components and propose a structured, transparent "
            "decision. Neutral rendering; verify exact scenario wording against "
            "locally held official 2025 GS-IV paper."
        ),
        "answer": (
            "Vijay faces a conflict between filial duty and irreplaceable public "
            "responsibility during an escalating disaster. His options are: remain "
            "throughout; leave immediately for the last rites; briefly transfer command "
            "and travel; or delay travel until operations stabilise while arranging the "
            "rites through relatives and maintaining contact.\n\n"
            "The dilemmas are personal duty versus public duty, compassion for family "
            "versus responsibility to thousands of victims, and emotional authenticity "
            "versus professional composure. Emotional intelligence clarifies rather than "
            "erases these claims: perceiving acknowledges grief; using emotion sustains "
            "purpose; understanding maps family, victim and team needs; managing supports "
            "a reasoned and communicated choice.\n\n"
            "Remaining without delegation protects continuity but may cause severe family "
            "regret and impaired judgment. Leaving immediately honours filial duty but "
            "risks operational disruption when communications and roads are already "
            "damaged. A brief transfer is humane and balanced, but only if a competent "
            "successor, communication channel and written handover exist. Delaying travel "
            "is justified if the emergency remains at its peak, though Vijay should "
            "explain transparently to family and avoid suppressing grief.\n\n"
            "The most appropriate course is a staged hybrid: stabilise the immediate "
            "response, formally hand operational command to the trained deputy, communicate "
            "the decision to senior government and teams, attend the rites for the shortest "
            "feasible period, and remain reachable where communications permit. If no safe "
            "handover is possible, public duty temporarily prevails, with reasons recorded. "
            "The institutional lesson is to pre-designate succession and family-emergency "
            "protocols so ethical administration does not depend on personal heroism."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Discuss the claim that emotional intelligence is the ability to make "
            "emotions work for you rather than against you, with reference to a "
            "civil servant's capacity to manage conflicting personal and "
            "professional duties during a crisis. Answer in 150 words."
        ),
        "answer": (
            "Emotional intelligence enables a civil servant to convert emotional "
            "responses from liabilities into administrative assets. Self-awareness "
            "detects when personal grief, fatigue or anger is affecting judgment "
            "before a consequential decision is made. Self-regulation channels that "
            "emotion into composed, proportionate action rather than reactive force "
            "or paralysis.\n\n"
            "In crisis, conflicting duties are inescapable. A district officer "
            "coordinating flood relief while a family member is hospitalised faces "
            "simultaneous emotional claims. EI does not eliminate the conflict but "
            "makes it navigable: the officer names the competing demands (awareness), "
            "maintains operational composure (regulation), communicates honestly "
            "with family and team (social skill), and delegates command temporarily "
            "if needed.\n\n"
            "The limit is real. EI provides the psychological infrastructure for "
            "managing competing duties but does not itself determine which duty takes "
            "priority — that requires a moral and legal framework. The verdict is "
            "that EI makes emotions work for the officer by converting raw affect "
            "into deliberate, transparent and accountable administrative action."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Why is emotional intelligence described as ethically neutral? What "
            "safeguard is needed to ensure that high EI serves citizens rather "
            "than manipulates them? Answer in 150 words."
        ),
        "answer": (
            "Emotional intelligence is ethically neutral because it is a capacity, "
            "not a moral compass. Social skill and empathic accuracy can be deployed "
            "to serve or to exploit. A socially skilled officer who reads a citizen's "
            "desperation can use that reading to expedite legitimate service or to "
            "extract a bribe by leveraging the citizen's urgency.\n\n"
            "This boundary condition means that high EI is dangerous without "
            "integrity. The safeguard is independent assessment of probity alongside "
            "EI: asset declarations, conflict-of-interest disclosures, vigilance "
            "clearance and institutional audit trails that make departure from "
            "ethical conduct detectable regardless of the officer's interpersonal "
            "skill.\n\n"
            "The administrative implication is that EI training must be embedded "
            "within an ethical framework, not treated as a substitute for it. Mission "
            "Karmayogi's competency modules are a delivery mechanism, not an ethical "
            "guarantee. The verdict is that EI and integrity are jointly necessary: "
            "EI without integrity enables sophisticated misconduct; integrity without "
            "EI limits effective citizen engagement."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Analyse the role of empathy and self-regulation in effective "
            "disaster-management leadership, with reference to a hypothetical "
            "district-level case where the officer faces simultaneous public "
            "duty and personal bereavement. Answer in 200 words."
        ),
        "answer": (
            "Empathy and self-regulation are the two EI components most sharply "
            "tested in disaster leadership. Empathy allows the officer to read "
            "the trauma of displaced citizens, the exhaustion of rescue teams "
            "and the frustration of stranded communities — adapting communication "
            "and resource allocation accordingly. Self-regulation prevents the "
            "officer's own grief from overwhelming operational judgment.\n\n"
            "In a hypothetical case: a district collector leading cloudburst "
            "relief learns of a parent's death. Self-awareness recognises the "
            "grief; self-regulation prevents paralysis or impulsive departure. "
            "Empathy perceives competing emotional claims — the victims' dependence, "
            "the family's expectation, the team's need for continuity. The officer "
            "activates a pre-designated deputy, maintains remote oversight, "
            "communicates transparently with family and team, and documents the "
            "decision rationale.\n\n"
            "This is not suppression. The officer's grief is real and acknowledged. "
            "The EI contribution is channelling it into structured decision-making "
            "rather than unstructured emotional response. The institutional "
            "complement is a crisis-management protocol that pre-designates "
            "succession and family-emergency provisions, reducing reliance on "
            "personal heroism.\n\n"
            "The limit is that individual EI cannot compensate for inadequate "
            "institutional support indefinitely. Chronic exposure to trauma "
            "without rotation, debrief and mental-health support depletes even "
            "high-EI officers. The verdict is that empathy and self-regulation "
            "are necessary for effective disaster leadership but sustainable only "
            "within an institutionally supportive framework."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Critically examine the claim that emotional intelligence helps "
            "overcome a crisis of conscience without compromising ethical "
            "standards. Under what conditions does this claim fail? "
            "Answer in 200 words."
        ),
        "answer": (
            "A crisis of conscience occurs when personal values, professional "
            "duty and situational pressures produce an irreconcilable tension. "
            "Emotional intelligence helps navigate this through three mechanisms: "
            "self-awareness names the conflict precisely rather than experiencing "
            "it as diffuse anguish; self-regulation prevents impulsive action or "
            "paralysis; social skill enables transparent communication of the "
            "chosen course to stakeholders, converting a private moral burden "
            "into a documented, accountable decision.\n\n"
            "An officer ordered to evict a slum community under a court order "
            "feels anguish. EI enables her to acknowledge the distress, regulate "
            "it into deliberate action, secure rehabilitation commitments before "
            "execution, and explain the rationale to affected families — exercising "
            "duty without abandoning compassion.\n\n"
            "The claim fails under two conditions. First, when EI provides composed "
            "capitulation rather than principled resolution: an officer who uses "
            "self-regulation to silence conscience rather than express it through "
            "legitimate channels has not overcome the crisis but suppressed it. "
            "Second, when EI operates without an independent ethical framework: "
            "emotional composure does not itself supply the moral standard for "
            "determining which stand to take.\n\n"
            "The verdict is that EI is necessary but insufficient. It provides the "
            "psychological infrastructure for managing a crisis of conscience; the "
            "ethical direction must come from moral reasoning — deontological, "
            "consequentialist or virtue-based — and institutional safeguards such "
            "as whistleblower protection and safe-dissent channels."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Design an institutional protocol for a disaster-prone district "
            "that sustains emotional intelligence in public administration "
            "beyond individual resilience. Draw on named EI models, the DC "
            "Vijay case study and Mission Karmayogi's competency architecture. "
            "Answer in 250 words."
        ),
        "answer": (
            "Individual emotional intelligence, however high, has diminishing "
            "returns without institutional support. A sustainable protocol for "
            "a disaster-prone district must embed EI principles into structural "
            "design.\n\n"
            "Pre-crisis preparedness: (1) Pre-designate a succession chain "
            "for disaster command, including a family-emergency clause allowing "
            "temporary command transfer to a trained deputy — converting the "
            "DC Vijay dilemma from individual moral burden to foreseen "
            "institutional scenario. (2) Mandate annual crisis-simulation "
            "exercises that explicitly test EI components: self-awareness "
            "under fatigue, self-regulation under provocation, empathic "
            "communication with displaced communities.\n\n"
            "During crisis: (3) Deploy a communication protocol where the "
            "commanding officer issues transparent public updates using "
            "social-skill principles — acknowledging hardship, explaining "
            "decisions, inviting feedback — converting institutional authority "
            "into empathetic governance. (4) Assign a peer-support officer "
            "trained in psychological first aid to monitor frontline staff "
            "for burnout and compassion fatigue.\n\n"
            "Post-crisis recovery: (5) Conduct mandatory structured debrief "
            "sessions within 72 hours for all officers involved, addressing "
            "emotional processing, not merely operational lessons learned. "
            "(6) Enforce a three-year rotation ceiling for disaster-prone "
            "postings to prevent chronic emotional exhaustion.\n\n"
            "National framework linkage: Mission Karmayogi's KCM framework "
            "aligns behavioural competencies with roles; AI Sarthi and "
            "AI Tutor (showcased at IndiaAI Impact Summit, February 2026) "
            "support personalised learning. This architecture could host verified "
            "crisis-leadership training, but the cited pages do not identify a "
            "named EI module.\n\n"
            "The limit is that learning architecture and AI-enabled delivery "
            "demonstrate institutional design, not verified ethical "
            "internalisation. The protocol must therefore combine training "
            "with structural supports: delegation, rotation, debrief and "
            "citizen feedback. The verdict is that durable administrative "
            "EI requires both individual competence and institutional "
            "scaffolding — neither alone is sufficient."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Evaluate the claim that emotional labour is the hidden cost "
            "of citizen-centric governance. Suggest institutional responses "
            "that support frontline officials without compromising service "
            "quality, drawing on Hochschild's framework and Indian "
            "administrative examples. Answer in 250 words."
        ),
        "answer": (
            "Emotional labour, as conceptualised by Hochschild (The Managed "
            "Heart, 1983), is the managed performance of role-appropriate "
            "emotion in professional settings. In citizen-centric governance, "
            "frontline officials — pension counter clerks, grievance-cell "
            "officers, disaster-relief coordinators — are required to "
            "maintain courtesy, empathy and composure regardless of personal "
            "emotional state.\n\n"
            "A pension counter clerk who maintains courtesy despite provocation "
            "performs emotional labour that drains psychological "
            "resources. A disaster-management officer who manages her own "
            "grief while coordinating rescue operations sustains emotional "
            "labour under extreme conditions. Both illustrate that citizen-"
            "centric governance depends on a form of work that is invisible "
            "in traditional workload assessments.\n\n"
            "Institutional responses must support officers without reducing "
            "service quality. (1) Structured rotation for high-emotional-"
            "labour postings, preventing chronic exposure. (2) Mandatory "
            "peer-counselling and debrief mechanisms after critical incidents, "
            "normalising emotional processing as professional practice. "
            "(3) Staff grievance channels for reporting abuse without retaliation. "
            "(4) Workload redesign that distributes difficult interactions across "
            "teams. (5) Verified, role-specific training in self-regulation and "
            "de-escalation, without assuming that course completion proves EI.\n\n"
            "The counter-risk is that staff-welfare emphasis must not become "
            "an excuse for poor service. The design principle is that "
            "institutional support sustains emotional capacity; it does not "
            "reduce service obligations. An officer rotated out of a "
            "high-stress posting must be replaced by a trained successor, "
            "not by a vacancy.\n\n"
            "The verdict is that emotional labour is a genuine hidden cost "
            "of citizen-centric governance. Institutional recognition protects "
            "officer welfare and sustained service quality; neglect produces "
            "burnout, attrition and declining service."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": "1. Three EI models: ability, mixed and trait",
        "structural_type": "comparison-matrix",
        "nodes": (
            "Ability model (Mayer-Salovey 1997): EI as cognitive ability tested by performance.",
            "Mixed model (Goleman 1995/1998): EI as five workplace competencies blending ability and personality.",
            "Trait model (Bar-On EQ-i 1997): EI as self-perceived competencies measured by self-report.",
            "Later performance tests such as MSCEIT operationalise the ability-model approach.",
            "The three models differ in theory, method and predictive validity.",
            "UPSC GS-IV primarily tests Goleman's five components in applied scenarios.",
            "Advanced answers distinguish models to show conceptual precision.",
            "Confusing models or claiming they measure the same construct is a common exam trap.",
        ),
        "verdict": "Name the specific model you are using before applying it to a scenario.",
        "answer_use": "Open any EI definition or comparison answer by distinguishing the three models.",
    },
    {
        "title": "2. Four-branch ability model: ascending hierarchy",
        "structural_type": "ascending-ladder",
        "nodes": (
            "Branch 1: Perceiving emotion — recognising emotional cues in self and others.",
            "Branch 2: Using emotion — channelling emotion to facilitate thought and creativity.",
            "Branch 3: Understanding emotion — grasping emotional complexity and transitions.",
            "Branch 4: Managing emotion — regulating emotion in self and others toward goals.",
            "The four branches form an ascending hierarchy of cognitive complexity.",
            "Perceiving is the foundational skill; managing is the most advanced.",
            "The DC Vijay case tests all four branches in a single scenario.",
            "Ability-model decomposition earns advanced marks in case-study answers.",
        ),
        "verdict": "Use the four-branch decomposition to structure any advanced EI case-study analysis.",
        "answer_use": "Apply to disaster-leadership and crisis-of-conscience case studies.",
    },
    {
        "title": "3. Goleman's five components mapped to administration",
        "structural_type": "horizontal-mapping",
        "nodes": (
            "Self-awareness: recognising own bias, stress or fatigue before deciding.",
            "Self-regulation: composure under provocation, crisis or media scrutiny.",
            "Motivation: sustained public-service drive beyond external incentive.",
            "Empathy: reading citizens' or colleagues' unstated needs.",
            "Social skill: managing teams, stakeholders and conflict resolution.",
            "Each component maps to a specific administrative behaviour.",
            "GS-IV questions test components in combination, not isolation.",
            "The five components are the default framework for most EI answers.",
        ),
        "verdict": "Name the specific component engaged at each decision point in your answer.",
        "answer_use": "Structure any Goleman-based EI answer by naming components before describing behaviour.",
    },
    {
        "title": "4. EI's dark side: ethical neutrality and manipulation risk",
        "structural_type": "decision-fork",
        "nodes": (
            "EI is a capacity, not a moral compass — it is ethically neutral.",
            "High social skill plus integrity produces effective citizen service.",
            "High social skill minus integrity produces sophisticated manipulation.",
            "Example: empathic reading used to extract a bribe by exploiting urgency.",
            "EI training without ethics framework can enable more effective misconduct.",
            "Integrity, probity and audit must be independently assessed.",
            "The dark side is not hypothetical — it is a genuine administrative risk.",
            "Joint necessity: EI and ethics are both required; neither alone suffices.",
        ),
        "verdict": "Always flag EI's ethical boundary when discussing its benefits.",
        "answer_use": "Include the dark-side qualification in any answer that claims EI improves governance.",
    },
    {
        "title": "5. IQ versus EQ: joint necessity, not substitution",
        "structural_type": "two-column-contrast",
        "nodes": (
            "IQ predicts task-competence and technical problem-solving ability.",
            "EQ predicts how well competence is deployed under interpersonal pressure.",
            "Two officers with identical IQ can produce divergent crisis outcomes.",
            "The divergence is explained by EQ: regulation, empathy and social skill.",
            "EQ matters disproportionately at the point of execution under stress.",
            "EQ cannot substitute for technical or legal competence.",
            "An empathetic but legally uninformed officer can still err.",
            "The defensible position: IQ and EQ are jointly necessary.",
        ),
        "verdict": "EQ amplifies competence under stress; it does not replace technical knowledge.",
        "answer_use": "Use to resolve any IQ-vs-EQ or cognitive-vs-emotional ability question.",
    },
    {
        "title": "6. DC Vijay case study: structured EI decomposition",
        "structural_type": "decision-tree",
        "nodes": (
            "Scenario: DC leads disaster relief; mother dies; family demands presence.",
            "Perceiving: acknowledge grief without denial — a legitimate emotional reality.",
            "Using: channel urgency of grief productively into sustained relief effort.",
            "Understanding: grasp competing claims of family, victims and subordinates.",
            "Managing: structured decision — designate deputy, communicate, document.",
            "The correct answer is structured transparent balancing, not single heroism.",
            "Institutional complement: pre-designated succession and family-emergency SOP.",
            "The case tests EI through institutional process, not raw willpower alone.",
        ),
        "verdict": "Decompose the dilemma using named EI branches; propose a structured, documented resolution.",
        "answer_use": "Apply to any disaster-leadership or duty-versus-family case study.",
    },
    {
        "title": "7. Emotional labour: cost, recognition and institutional response",
        "structural_type": "cause-effect-chain",
        "nodes": (
            "Emotional labour (Hochschild 1983): managed display of role-appropriate emotion.",
            "Citizen-facing roles require sustained courtesy despite provocation.",
            "Emotional labour is invisible in traditional workload assessments.",
            "Sustained emotional labour carries burnout risk regardless of natural empathy.",
            "Institutional responses: rotation, debrief, staff grievance channels, team distribution.",
            "Staff-welfare support sustains capacity; it does not reduce service obligations.",
            "Overemphasis on staff welfare must not become excuse for poor service.",
            "Emotional labour is a hidden cost of citizen-centric governance.",
        ),
        "verdict": "Acknowledge emotional labour as real cost and prescribe institutional support alongside duty.",
        "answer_use": "Use in any question about frontline service quality, officer welfare or burnout.",
    },
    {
        "title": "8. Moral intuition versus moral reasoning: EI as bridge",
        "structural_type": "process-flow",
        "nodes": (
            "Moral intuition: fast, affect-driven sense that something feels wrong.",
            "Draws on EI's empathy (sensing others' distress) and self-awareness.",
            "Moral reasoning: slow, deliberate application of ethical theory or rule.",
            "Self-awareness detects when intuitive reaction may be bias, not signal.",
            "The regulatory bridge: intuition triggers reasoning; reasoning tests intuition.",
            "Neither alone is sufficient: intuition without reasoning can be prejudice.",
            "Reasoning without intuition can miss human impact of technically correct decisions.",
            "EI mediates between the two by providing the self-awareness check.",
        ),
        "verdict": "Intuition is the trigger; reasoning is the test; self-awareness is the bridge.",
        "answer_use": "Use to answer any moral intuition vs moral reasoning or EQ-linked ethical-judgment question.",
    },
    {
        "title": "9. Empathy and wisdom: preventing travesty of justice",
        "structural_type": "causal-flow",
        "nodes": (
            "Wisdom (phronesis): practical judgment applying rules with contextual sensitivity.",
            "Travesty of justice: literal compliance defeating the rule's purpose.",
            "Empathy triggers wisdom by alerting the officer to human cost of mechanical application.",
            "Example: denying welfare on a minor technicality despite clear substantive eligibility.",
            "Without empathy, wisdom has no trigger to activate.",
            "Empathy without rule-awareness risks arbitrary favouritism.",
            "The safeguard is transparent reasoning and appeal mechanisms.",
            "Wisdom requires both legal competence and empathetic perception.",
        ),
        "verdict": "Empathy activates wisdom; rule-based transparency prevents it from degenerating into favouritism.",
        "answer_use": "Use to answer any wisdom-in-administration or travesty-of-justice question.",
    },
    {
        "title": "10. Crisis of conscience: EI navigation mechanism",
        "structural_type": "resolution-pathway",
        "nodes": (
            "Crisis of conscience: personal values, duty and pressure conflict irreconcilably.",
            "Self-awareness names the conflict precisely rather than diffuse anguish.",
            "Self-regulation prevents impulsive action or paralysis under emotional turmoil.",
            "Social skill enables transparent communication of the chosen course.",
            "The officer converts private moral burden into documented accountable decision.",
            "EI provides psychological infrastructure but not the ethical standard.",
            "Moral framework (deontological, consequentialist, virtue-based) supplies direction.",
            "EI without ethical grounding can produce composed capitulation, not principled resolution.",
        ),
        "verdict": "EI navigates the crisis of conscience; the ethical stand must come from moral reasoning.",
        "answer_use": "Use to structure any crisis-of-conscience or ethical-dilemma answer.",
    },
    {
        "title": "11. Mission Karmayogi and institutional EI architecture",
        "structural_type": "institutional-flow",
        "nodes": (
            "Mission Karmayogi provides the institutional setting for role-based learning.",
            "KCM aligns roles with competencies and embeds competencies in training (CBC).",
            "AI Sarthi and AI Tutor showcased at IndiaAI Impact Summit (16-20 Feb 2026).",
            "iGOT-Karmayogi delivers role-based personalised multilingual learning.",
            "A named EI module is not verified by the cited official CBC pages.",
            "Learning architecture demonstrates institutional design, not ethical internalisation.",
            "Do not claim a general APAR linkage without a service-specific DoPT order.",
            "Training must be supplemented by delegation protocols, rotation and citizen feedback.",
        ),
        "verdict": "Use Mission Karmayogi as a competency-architecture example, not proof of EI training or conduct.",
        "answer_use": "Clearly label any EI linkage as an analytical application unless a named module is verified.",
    },
    {
        "title": "12. PYQ demand map and answer synthesis",
        "structural_type": "exam-synthesis-rail",
        "nodes": (
            "2013 Q4: define EI, development, role in ethical decisions — use definition plus mechanism.",
            "2019 Q5(b): EI as making emotions work for you — use five-component administrative mapping.",
            "2020 Q2(b): components and learnability — use ability/competency distinction.",
            "2021 Q4(b): EI and crisis of conscience — use self-awareness plus ethical framework.",
            "2022 Q1: wisdom/travesty plus empathy/compassion — use phronesis plus empathy-as-trigger.",
            "2023 Q4: EQ vs IQ plus moral intuition vs reasoning — use joint-necessity plus bridge model.",
            "2025 Q7: DC Vijay case study — use four-branch decomposition plus institutional protocol.",
            "Name the EI component precisely; show institutional mechanism; close with a qualified verdict.",
        ),
        "verdict": "The highest-scoring answer moves from named model to specific component to example to institutional limit.",
        "answer_use": "Use as the revision checklist before any EI PYQ attempt.",
    },
)

CURRENT_ANCHOR = {
    "title": "Mission Karmayogi: competency-based capacity building and AI-enabled delivery",
    "verified_facts": (
        "Karmayogi Competency Model (KCM) aligns roles with required competencies, embeds competencies in training, and supports accountability, role-fit and continuous development (CBC KCM page).",
        "Ministries and Departments shift from rule-based to role-based thinking under the KCM framework (CBC KCM page).",
        "AI Sarthi and AI Tutor were showcased at the IndiaAI Impact Summit from 16-20 February 2026; the official page describes role-based personalised learning and contextual in-course support (CBC IndiaAI page).",
        "The same showcase included AI-enabled transcription and multilingual subtitles for inclusive learning (CBC IndiaAI page).",
        "AI-Driven Capacity Building Plans (AI-CBP) analyse roles and official documents, map competencies, identify capability gaps and generate role-specific learning pathways (CBC IndiaAI page).",
    ),
    "administrative_link": (
        "Use Mission Karmayogi as an official example of role-based competency architecture "
        "and AI-enabled learning delivery. Linking that architecture to EI is a clearly "
        "marked analytical proposal, not evidence that the cited pages verify a named EI module."
    ),
    "limit": (
        "Learning architecture and AI-enabled delivery demonstrate institutional design, not "
        "verified ethical internalisation. Do not assert a general APAR linkage for EI "
        "modules without a service-specific DoPT order. Do not claim a named EI course on "
        "iGOT or user/course counts without a verifiable official source. AI-enabled "
        "personalisation is a delivery improvement, not proof of values adoption."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://cbc.gov.in/mission-karmayogi-showcases-ai-enabled-capacity-building-civil-servants-indiaai-impact-summit-2026",
    "https://cbc.gov.in/karmayogi-competency-model-kcm",
)

SOURCE_CAVEAT = (
    "Use the local Basic and Advanced owners as the controlling source. Salovey-Mayer "
    "1990 definition and the 1997 four-branch revision are distinct; do not conflate. "
    "Goleman's 1995 book popularised EI; his 1998 HBR essay set out the five workplace "
    "competencies. Bar-On's EQ-i (1997 technical manual) is a trait model measured by "
    "self-report, not a performance-based ability test. Hochschild's emotional labour "
    "concept comes from The Managed Heart (1983). The 2025 GS-IV Q7 DC Vijay case study "
    "is named in both Basic section 3.6 and Advanced section 3; verify exact scenario "
    "wording against the locally held official paper. PYQ demands for 2019-2023 are from "
    "the audited local routing ledger _PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md; neutral "
    "renderings, not claimed as exact official text. Mission Karmayogi claims are limited "
    "to facts directly verifiable from CBC official pages (IndiaAI Summit page, KCM page). "
    "Do not assert user counts, course counts, a named EI course or a general APAR "
    "linkage without a service-specific DoPT order."
)

REGISTER_SUPPLEMENT = (
    "Rapid recall: EI defined by Salovey-Mayer (1990) as monitoring and using one's own "
    "and others' emotions to guide thought and action. Four-branch ability model (1997): "
    "perceive -> use -> understand -> manage (ascending cognitive complexity). Goleman "
    "(1995/1998): self-awareness, self-regulation, motivation, empathy, social skill. "
    "Bar-On EQ-i (1997): trait model via self-report. Three models differ in theory and "
    "method — do not equate them. Self-awareness is the precondition for all EI; "
    "self-regulation is not suppression but channelling emotion into deliberate action. "
    "Empathy reads unstated citizen needs; it informs HOW rules are applied, not WHETHER "
    "rules are waived. Social skill converts internal composure into organisational "
    "outcomes. Emotional labour (Hochschild 1983): real psychological cost of managing "
    "displayed emotions; requires institutional support (rotation, debrief, grievance "
    "channels). EI is ethically neutral — dark side: high EI + low integrity = "
    "sophisticated manipulation. EI and integrity are jointly necessary. Moral intuition "
    "(fast, affect-driven) draws on empathy and self-awareness; moral reasoning (slow, "
    "deliberate) tests and corrects intuition; self-awareness bridges the two. Wisdom in "
    "administration (phronesis) requires empathy as trigger for contextual sensitivity; "
    "without it, mechanical rule-application produces travesty of justice. Crisis of "
    "conscience: EI navigates (awareness names, regulation prevents paralysis, social "
    "skill communicates) but does not supply the ethical standard — needs moral framework. "
    "IQ and EQ are jointly necessary: EQ determines execution quality under stress, IQ "
    "supplies technical competence. DC Vijay 2025 Q7: decompose using four branches; "
    "propose structured transparent balancing, not single heroic choice; institutional "
    "complement is pre-designated succession and family-emergency SOP. Mission Karmayogi: "
    "KCM aligns roles with competencies; AI Sarthi/Tutor support "
    "personalised delivery (IndiaAI Summit Feb 2026). Learning architecture demonstrates "
    "institutional design, not ethical internalisation. PYQ spine: 2013 (define + develop "
    "+ ethical decisions), 2019 (emotions work for you), 2020 (components + learnability), "
    "2021 (crisis of conscience), 2022 (wisdom + empathy/compassion), 2023 (EQ vs IQ + "
    "intuition vs reasoning), 2025 (DC Vijay case study). Answer spine: name model/component "
    "-> mechanism -> Indian/case example -> institutional safeguard -> dark-side limit -> "
    "qualified verdict."
)
