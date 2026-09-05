"""Learner-v2 source data: Ethics Topic 08, Moral Theories."""

SESSION_TITLES = (
    "Normative theories and the anatomy of moral action",
    "Three-lens decision method and Indian administrative applications",
    "Scope, rights and close-option traps",
    "Translating moral theory into PYQ and Mains answers",
    "Moral intuition versus moral reasoning",
    "Doing good beyond express rules",
    "Scarcity, triage and Snowden-type disclosure",
    "Moral luck and good-faith administration",
    "Evidence units, directive decoding and case architecture",
    "Study links, routed PYQs and final synthesis",
)

SESSION_GROUPS = (
    ("1", "2"),
    ("3", "4"),
    ("5", "6"),
    ("7", "8", "9"),
    ("10",),
    ("11",),
    ("12",),
    ("12a",),
    ("13", "14"),
    ("15",),
)

MCQ_ITEMS = (
    # --- Family A: action anatomy and means-ends ---
    {
        "label": "Motive concerns the reason moving the agent",
        "statement": (
            "Motive is the background reason moving an agent, such as compassion, fear, "
            "loyalty or private gain; it helps evaluate character but does not by itself "
            "make the chosen administrative action right."
        ),
        "scenario_a": (
            "A district magistrate diverts a relief vehicle to her native village because "
            "she sincerely fears for childhood neighbours, although another village has "
            "greater documented need. Which distinction prevents compassion alone from "
            "settling the ethical verdict?"
        ),
        "scenario_b": (
            "A municipal officer exposes a procurement irregularity mainly to damage a "
            "rival, but the disclosure is accurate and protects public money. Which object "
            "of moral appraisal captures the officer's rivalry without deciding the whole case?"
        ),
        "family": "action anatomy and means-ends",
        "group": "action anatomy and means-ends",
    },
    {
        "label": "Intention is the result deliberately chosen",
        "statement": (
            "Intention is the result an agent deliberately adopts, including the chosen "
            "means; a benevolent motive can coexist with an unlawful, discriminatory or "
            "otherwise defective intention."
        ),
        "scenario_a": (
            "A welfare officer wants to help vulnerable families but deliberately removes "
            "eligible migrant applicants from a list to reserve funds for local residents. "
            "Which concept identifies the exclusion she knowingly chose?"
        ),
        "scenario_b": (
            "A police officer wishes to prevent violence and knowingly plans an unlawful "
            "collective punishment of an entire neighbourhood. Which element remains "
            "defective even if the underlying public-safety motive is sincere?"
        ),
        "family": "action anatomy and means-ends",
        "group": "action anatomy and means-ends",
    },
    {
        "label": "Expected and actual consequences must be separated",
        "statement": (
            "Ethical appraisal should distinguish expected consequences, reasonably "
            "foreseeable risks and actual outcomes, because the eventual result may include "
            "luck beyond the decision-maker's control."
        ),
        "scenario_a": (
            "Two engineers approve equally well-tested flood barriers; an unforeseeable "
            "landslide destroys one while the other succeeds. Which distinction guards "
            "against treating the different outcomes as proof of different diligence?"
        ),
        "scenario_b": (
            "A vaccination campaign produces a rare adverse event that was neither known "
            "nor reasonably predictable when approved. Which proposition requires judging "
            "the decision by expected risk as well as the realised harm?"
        ),
        "family": "action anatomy and means-ends",
        "group": "action anatomy and means-ends",
    },
    {
        "label": "Good ends do not automatically cleanse bad means",
        "statement": (
            "A good end does not automatically cleanse a wrongful means: act "
            "consequentialism may sometimes permit it, while deontology imposes "
            "side-constraints and virtue ethics examines what the choice reveals about character."
        ),
        "scenario_a": (
            "A state proposes secretly intercepting every citizen's messages to locate a "
            "small terrorist cell. Which proposition explains why public safety cannot by "
            "itself settle the morality of indiscriminate surveillance?"
        ),
        "scenario_b": (
            "A block officer fabricates attendance records so that deserving labourers "
            "receive delayed MGNREGA wages. Which analytical claim requires separate "
            "scrutiny of the benevolent objective and the dishonest method?"
        ),
        "family": "action anatomy and means-ends",
        "group": "action anatomy and means-ends",
    },
    # --- Family B: deontological reasoning ---
    {
        "label": "Universalisation tests the operative maxim",
        "statement": (
            "Kantian universalisation asks whether the operative maxim could be consistently "
            "adopted by everyone, not merely whether the present exception benefits the "
            "individual decision-maker."
        ),
        "scenario_a": (
            "A licensing officer accepts one undisclosed gift because the application is "
            "otherwise meritorious and says no harm will follow. Which test asks what would "
            "happen to the practice if every officer adopted that maxim?"
        ),
        "scenario_b": (
            "A tax official proposes lying to one taxpayer to secure quick payment while "
            "expecting citizens generally to trust official notices. Which Kantian test "
            "exposes the contradiction in the proposed maxim?"
        ),
        "family": "deontological reasoning",
        "group": "deontological reasoning",
    },
    {
        "label": "Humanity must never be treated merely as a means",
        "statement": (
            "The humanity formula prohibits treating persons merely as instruments, "
            "establishing a dignity and rights floor below which aggregate welfare "
            "calculations cannot ordinarily descend."
        ),
        "scenario_a": (
            "A district plans a hazardous medical trial on poorly informed prisoners because "
            "the results could benefit millions. Which principle rejects using them merely "
            "as instruments for aggregate benefit?"
        ),
        "scenario_b": (
            "Officials publish identifiable medical details of welfare beneficiaries to "
            "demonstrate programme success. Which deontological principle requires informed "
            "respect for those citizens rather than using them as publicity material?"
        ),
        "family": "deontological reasoning",
        "group": "deontological reasoning",
    },
    {
        "label": "Some duties generate agent-relative restraints",
        "statement": (
            "Deontological reasons are often agent-relative: an official's own duty not to "
            "falsify records remains binding even when another person might otherwise produce "
            "a worse outcome."
        ),
        "scenario_a": (
            "A superior tells an accounts officer to alter one figure, warning that refusal "
            "will lead a less scrupulous colleague to falsify the entire statement. Which "
            "principle explains why the officer still has a personal duty not to falsify?"
        ),
        "scenario_b": (
            "A jail superintendent is asked to torture one suspect because another agency "
            "may use harsher methods if she refuses. Which proposition rejects transferring "
            "moral responsibility to the predicted conduct of others?"
        ),
        "family": "deontological reasoning",
        "group": "deontological reasoning",
    },
    {
        "label": "Consequences inform planning but do not create duty",
        "statement": (
            "Deontology excludes consequences as the foundation of duty, not from practical "
            "planning; hard cases require identifying genuinely conflicting duties and giving "
            "a reasoned account of priority."
        ),
        "scenario_a": (
            "During a riot, a magistrate must protect life while also respecting lawful "
            "assembly and proportional force. Which formulation allows consequences to inform "
            "implementation without making expected welfare the sole source of duty?"
        ),
        "scenario_b": (
            "A doctor in a government hospital faces duties of confidentiality and protection "
            "of an identifiable third party from serious harm. Which deontological approach "
            "requires reasoned prioritisation rather than mechanically repeating one rule?"
        ),
        "family": "deontological reasoning",
        "group": "deontological reasoning",
    },
    # --- Family C: consequentialist reasoning ---
    {
        "label": "Consequentialism compares complete expected effects",
        "statement": (
            "Consequentialism compares feasible alternatives by their expected effects on "
            "everyone affected, including indirect harms, distribution, precedent, "
            "institutional trust and long-term consequences."
        ),
        "scenario_a": (
            "A city considers closing a polluting factory. Which approach requires comparing "
            "health gains, lost livelihoods, transition support, future investment signals "
            "and environmental effects across all realistic alternatives?"
        ),
        "scenario_b": (
            "A collector considers waiving one documentation requirement for flood relief. "
            "Which theory demands attention not only to the immediate beneficiary but also "
            "to equal treatment, precedent and future trust?"
        ),
        "family": "consequentialist reasoning",
        "group": "consequentialist reasoning",
    },
    {
        "label": "Act utilitarianism evaluates the particular act",
        "statement": (
            "Act utilitarianism evaluates the particular choice and may support an exception "
            "when that act produces greater expected net welfare than every available alternative."
        ),
        "scenario_a": (
            "An ambulance driver breaks a minor traffic restriction at an empty junction to "
            "save a critically injured child. Which version of utilitarianism focuses directly "
            "on the expected result of this individual exception?"
        ),
        "scenario_b": (
            "A disaster officer opens a locked public building without prior permission to "
            "shelter families during a cloudburst. Which approach asks whether this particular "
            "act maximises welfare compared with waiting?"
        ),
        "family": "consequentialist reasoning",
        "group": "consequentialist reasoning",
    },
    {
        "label": "Rule utilitarianism evaluates general acceptance",
        "statement": (
            "Rule utilitarianism evaluates the consequences of generally accepting a rule, "
            "explaining why predictable and non-arbitrary procedures may outperform locally "
            "attractive exceptions."
        ),
        "scenario_a": (
            "A ration officer could favour one sympathetic family today, but widespread "
            "case-by-case favouritism would undermine queues and trust. Which theory evaluates "
            "the welfare effects of the general rule?"
        ),
        "scenario_b": (
            "A procurement committee retains transparent bidding even though direct selection "
            "might be faster in one non-emergency purchase. Which approach emphasises the "
            "long-run gains of generally following a fair procedure?"
        ),
        "family": "consequentialist reasoning",
        "group": "consequentialist reasoning",
    },
    {
        "label": "Utility calculation contains framing and measurement risks",
        "statement": (
            "Consequentialist calculation remains vulnerable to uncertain forecasts, unequal "
            "distribution, disputed welfare measures and manipulation of whose interests or "
            "time horizon count."
        ),
        "scenario_a": (
            "A dam appraisal counts electricity revenue but omits displacement, downstream "
            "ecology and tribal cultural loss. Which limitation exposes how selective framing "
            "can manufacture an apparently favourable net benefit?"
        ),
        "scenario_b": (
            "An urban flyover saves commuters five minutes but imposes concentrated pollution "
            "on a low-income settlement. Which caution challenges aggregation that hides who "
            "receives benefits and who bears costs?"
        ),
        "family": "consequentialist reasoning",
        "group": "consequentialist reasoning",
    },
    # --- Family D: virtue ethics and phronesis ---
    {
        "label": "Virtue ethics evaluates stable character",
        "statement": (
            "Virtue ethics evaluates the character and stable dispositions expressed through "
            "action, not only compliance with rules or production of desirable outcomes."
        ),
        "scenario_a": (
            "An officer repeatedly behaves honestly even when audits are unlikely and no "
            "reward is available. Which ethical approach treats this reliable disposition, "
            "rather than isolated compliance, as central?"
        ),
        "scenario_b": (
            "A police leader builds habits of restraint, courage and truthfulness throughout "
            "the force instead of relying only on manuals. Which theory most directly explains "
            "this character-forming strategy?"
        ),
        "family": "virtue ethics and phronesis",
        "group": "virtue ethics and phronesis",
    },
    {
        "label": "The golden mean is context-relative appropriateness",
        "statement": (
            "Aristotle's mean is context-relative practical appropriateness between excess and "
            "deficiency, not an arithmetic midpoint or a command always to choose moderation."
        ),
        "scenario_a": (
            "A district magistrate facing communal violence rejects both reckless force and "
            "cowardly inaction, selecting firm proportionate measures. Which Aristotelian idea "
            "describes the appropriate response without averaging the two extremes?"
        ),
        "scenario_b": (
            "An officer is told to split the difference between complete secrecy and full "
            "publication in every information dispute. Which proposition explains why ethical "
            "balance cannot be reduced to a numerical midpoint?"
        ),
        "family": "virtue ethics and phronesis",
        "group": "virtue ethics and phronesis",
    },
    {
        "label": "Phronesis integrates purpose, perception and deliberation",
        "statement": (
            "Phronesis integrates ethical purpose, experience, perceptive attention and "
            "deliberation to identify which virtue and response are appropriate in a "
            "particular situation."
        ),
        "scenario_a": (
            "A revenue officer recognises that literal insistence on one certificate would "
            "defeat a pension rule's protective purpose, then records a lawful alternative "
            "verification. Which virtue-guided capacity is being exercised?"
        ),
        "scenario_b": (
            "A new collector knows every disaster manual but cannot recognise when frightened "
            "citizens need reassurance rather than another order. Which missing Aristotelian "
            "capacity links general knowledge to perceptive action?"
        ),
        "family": "virtue ethics and phronesis",
        "group": "virtue ethics and phronesis",
    },
    {
        "label": "Public roles shape the virtues demanded",
        "statement": (
            "Public responsibility and entrusted power shape the virtues demanded by a role; "
            "care ethics is a neighbouring relational tradition, not simply an Aristotelian "
            "subtype."
        ),
        "scenario_a": (
            "A judge must display impartiality and restraint where a private citizen may "
            "properly show personal loyalty. Which proposition explains why entrusted public "
            "roles alter the virtues ethically salient in action?"
        ),
        "scenario_b": (
            "A training note classifies every relationship-centred argument as Aristotelian "
            "virtue ethics. Which caution requires treating care ethics as adjacent but "
            "conceptually distinct?"
        ),
        "family": "virtue ethics and phronesis",
        "group": "virtue ethics and phronesis",
    },
    # --- Family E: moral cognition and contextual justice ---
    {
        "label": "Moral intuition is a rapid ethical signal",
        "statement": (
            "Moral intuition is a rapid, affective judgment that can provide an early warning "
            "but may also reproduce prejudice, familiarity bias or in-group loyalty."
        ),
        "scenario_a": (
            "A procurement officer feels that an apparently compliant bid is improper before "
            "she can identify why. Which concept describes this useful but not yet defensible "
            "ethical signal?"
        ),
        "scenario_b": (
            "A village official instinctively trusts applicants from his own community more "
            "than outsiders. Which feature explains why a strongly felt moral response still "
            "requires scrutiny?"
        ),
        "family": "moral cognition and contextual justice",
        "group": "moral cognition and contextual justice",
    },
    {
        "label": "Moral reasoning supplies publicly defensible tests",
        "statement": (
            "Moral reasoning makes a decision publicly defensible by testing facts and "
            "intuitions against duties, consequences, virtues, law and constitutional values."
        ),
        "scenario_a": (
            "After feeling uneasy about a tender, an officer checks beneficial ownership, "
            "conflict rules, expected public loss and fairness before acting. Which process "
            "turns an intuition into an appeal-resistant decision?"
        ),
        "scenario_b": (
            "A disciplinary authority says only that dismissal 'felt right' and records no "
            "criteria. Which missing process would provide reasons capable of scrutiny by a "
            "court or reviewing authority?"
        ),
        "family": "moral cognition and contextual justice",
        "group": "moral cognition and contextual justice",
    },
    {
        "label": "Context-sensitive justice retains stable values",
        "statement": (
            "Context-sensitive justice retains stable values while adapting their application "
            "to changed facts, knowledge and burdens; it must not be confused with unrestricted "
            "ethical relativism."
        ),
        "scenario_a": (
            "Emergency movement restrictions justified during a lethal outbreak continue after "
            "the danger passes. Which principle explains how the same liberty value can require "
            "a different rule application when facts change?"
        ),
        "scenario_b": (
            "A benefits algorithm once regarded as neutral is shown to exclude persons with "
            "disabilities. Which proposition requires revisiting the earlier practice without "
            "claiming that justice has no stable content?"
        ),
        "family": "moral cognition and contextual justice",
        "group": "moral cognition and contextual justice",
    },
    {
        "label": "Good initiative requires authority and equal treatment",
        "statement": (
            "Doing good beyond express rules requires lawful authority, no express or implied "
            "prohibition, equal treatment, recorded reasons and fidelity to substance without "
            "arbitrary disregard of form."
        ),
        "scenario_a": (
            "A revenue officer accepts an alternative identity document from an elderly flood "
            "victim and records why the statute permits equivalent proof. Which principle "
            "distinguishes calibrated initiative from unauthorised benevolence?"
        ),
        "scenario_b": (
            "A collector waives a requirement only for a politically connected applicant, "
            "arguing that no rule expressly forbids the waiver. Which proposition identifies "
            "the missing equality and reasons safeguards?"
        ),
        "family": "moral cognition and contextual justice",
        "group": "moral cognition and contextual justice",
    },
    # --- Family F: applied synthesis and moral luck ---
    {
        "label": "Ethical triage requires a constrained hybrid",
        "statement": (
            "Ethical triage should combine evidence-based welfare maximisation with equal "
            "worth, non-discrimination, vulnerability safeguards, published criteria and "
            "periodic review."
        ),
        "scenario_a": (
            "A government hospital has fewer ICU beds than eligible patients. Which framework "
            "supports clinical evidence while rejecting VIP preference and requiring transparent "
            "reviewable allocation criteria?"
        ),
        "scenario_b": (
            "After a cyclone, relief teams can immediately reach only three of six islands. "
            "Which proposition combines aggregate rescue impact with equal dignity, vulnerability "
            "and a public priority rule?"
        ),
        "family": "applied synthesis and moral luck",
        "group": "applied synthesis and moral luck",
    },
    {
        "label": "Disclosure requires necessity and proportionality",
        "statement": (
            "Snowden-type disclosure presents competing duties of confidentiality and democratic "
            "accountability; motive alone cannot replace necessity, minimisation, proportionality "
            "and prior-channel tests."
        ),
        "scenario_a": (
            "An intelligence analyst discovers unlawful mass surveillance and considers uploading "
            "an entire classified archive without first using protected oversight channels. Which "
            "principle requires a narrower, channel-sensitive ethical assessment?"
        ),
        "scenario_b": (
            "A government engineer leaks only the documents necessary to prove concealed dam-safety "
            "risks after documented internal escalation fails. Which framework assesses whether the "
            "disclosure is ethically defensible despite a secrecy duty?"
        ),
        "family": "applied synthesis and moral luck",
        "group": "applied synthesis and moral luck",
    },
    {
        "label": "Moral luck has four analytically distinct forms",
        "statement": (
            "Nagel's taxonomy distinguishes resultant, circumstantial, constitutive and causal "
            "luck; Williams's treatment should not be presented as an identical four-part taxonomy."
        ),
        "scenario_a": (
            "Two equally diligent officers face different outcomes, while only one happened to "
            "be posted during a catastrophe. Which framework separates luck in results from luck "
            "in circumstances?"
        ),
        "scenario_b": (
            "A discussion distinguishes outcome, situation, temperament and causal history as "
            "sources of factors beyond control. Which attribution caution prevents assigning the "
            "same fourfold classification indiscriminately to both philosophers?"
        ),
        "family": "applied synthesis and moral luck",
        "group": "applied synthesis and moral luck",
    },
    {
        "label": "Ex-ante process corrects outcome bias without excusing negligence",
        "statement": (
            "A moral-luck correction makes ex-ante diligence primary without making outcomes "
            "irrelevant: outcomes remain evidence and feedback, while negligence, bad faith and "
            "foreseeable omissions remain blameworthy."
        ),
        "scenario_a": (
            "A public-sector bank officer follows recorded due diligence, but an unforeseeable "
            "market shock later defeats the project. Which principle resists automatic misconduct "
            "inference while preserving review of the decision process?"
        ),
        "scenario_b": (
            "A road project succeeds despite the engineer ignoring mandatory soil tests. Which "
            "proposition explains why a fortunate outcome cannot vindicate a negligent process?"
        ),
        "family": "applied synthesis and moral luck",
        "group": "applied synthesis and moral luck",
    },
)

PYQS = (
    {
        "year": 2018,
        "question": (
            "Neutral rendering of GS-IV Q4: (a) Examine whether a public servant may "
            "undertake a good act when it is not expressly prohibited by laws or rules. "
            "(b) Two views hold respectively that means are most important and that the "
            "ends justify the means. Which view is more appropriate? Justify. "
            "Combined format: 10 + 10 marks; two separate 150-word answers."
        ),
        "marks": 20,
        "source_note": (
            "Verified against the local 2018 GS-IV scan and the 2018-2023 routing ledger. "
            "Both subparts are retained; the combined 20 marks must not be represented as "
            "one undifferentiated 150-word answer."
        ),
        "answer": (
            "(a) Absence of an express prohibition does not create unlimited discretion. A "
            "public servant may take a beneficial initiative only when it lies within delegated "
            "authority, violates neither an express nor an implied restriction, serves a public "
            "purpose and remains available to all similarly placed citizens. Reasons should be "
            "recorded and reviewable. Deontology supplies the duty and equality floor; "
            "consequentialism tests hidden costs and precedent; phronesis distinguishes purposive "
            "initiative from favouritism. Accepting equivalent proof from every disaster-affected "
            "pensioner can be justified; selectively waiving eligibility for a political contact "
            "cannot.\n\n"
            "(b) Ethical means deserve presumptive priority because dishonest or coercive methods "
            "damage dignity, legitimacy, trust and the very quality of the achieved end. "
            "Deontology rejects using persons merely as instruments, while virtue ethics asks "
            "what corrupt methods habituate. Consequences still matter: among lawful, "
            "rights-respecting means, administration should choose the option producing the "
            "greatest public benefit. A narrowly tailored emergency departure may be justified "
            "by necessity and proportionality, but a desirable end cannot routinely legalise "
            "fabrication, discrimination or torture. Therefore, clean means form the ethical "
            "floor and consequence-sensitive optimisation operates within it."
        ),
    },
    {
        "year": 2023,
        "question": (
            "Neutral rendering of GS-IV Q4: (a) Discuss whether emotional intelligence is "
            "more important than cognitive intelligence for success in life. (b) Differentiate "
            "moral intuition from moral reasoning with suitable examples. Combined format: "
            "10 + 10 marks; two separate 150-word answers."
        ),
        "marks": 20,
        "source_note": (
            "Verified against the local 2023 GS-IV scan and the 2018-2023 routing ledger. "
            "Part (b) is directly owned here; part (a) is a necessary cross-topic bridge to "
            "the Emotional Intelligence owner."
        ),
        "answer": (
            "(a) Emotional intelligence enables self-awareness, regulation, empathy, social "
            "understanding and relationship management. These capacities help an administrator "
            "handle conflict, motivate teams and recognise the human impact of technically "
            "correct decisions. Cognitive ability remains indispensable for legal analysis, "
            "evidence, forecasting and domain competence. EQ without knowledge can become "
            "well-intentioned incompetence; IQ without emotional maturity can become insensitive "
            "or uncooperative administration. Success therefore depends on complementary "
            "deployment: cognitive ability identifies feasible solutions, while emotional "
            "intelligence helps select, communicate and implement them responsibly.\n\n"
            "(b) Moral intuition is a rapid, felt judgment arising before explicit deliberation; "
            "moral reasoning is a slower, articulated test using facts, duties, consequences and "
            "virtues. A procurement officer's unease about a compliant bid is intuition. Checking "
            "beneficial ownership, conflicts and public loss is reasoning. Intuition offers speed "
            "and early warning but may reflect bias. Reasoning is transparent and appeal-resistant "
            "but may rationalise a predetermined preference. The defensible sequence is intuition "
            "as signal, reason as audit, followed by a revisable decision."
        ),
    },
    {
        "year": 2024,
        "question": (
            "GS-IV Q4: (a) Examine, with suitable examples, the proposition that just and "
            "unjust are contextual and that changing contexts must remain under scrutiny to "
            "prevent miscarriage of justice. (b) Examine, with suitable illustrations, the "
            "claim that mindless attachment to form while ignoring substance causes injustice, "
            "and that a perceptive civil servant should avoid such literalness and carry out "
            "the true intent. Combined format: 10 + 10 marks; two separate 150-word answers."
        ),
        "marks": 20,
        "source_note": (
            "Wording and format verified against books\\mains\\05 UPSC 2024 "
            "Paper-IV_Final 1.pdf. Context sensitivity must not be presented as unrestricted "
            "ethical relativism, and purposive administration must remain lawful."
        ),
        "answer": (
            "(a) Context changes facts, burdens and the foreseeable impact of a rule; it need "
            "not change the underlying values. Movement restrictions may protect life during "
            "a lethal outbreak but become disproportionate after the emergency. An automated "
            "benefit rule once considered neutral must be revised when evidence shows systematic "
            "exclusion of persons with disabilities. Phronesis connects stable commitments to "
            "dignity, equality and liberty with contemporary knowledge. Continuous scrutiny "
            "therefore prevents yesterday's reasonable application from becoming today's "
            "miscarriage of justice. The limit is anti-relativism: political convenience cannot "
            "redefine cruelty, discrimination or corruption as just.\n\n"
            "(b) Form protects predictability and equality, but literal compliance becomes "
            "unjust when it defeats the lawful purpose it was designed to serve. A pension "
            "officer may accept statutorily equivalent identity proof from a flood victim "
            "instead of insisting on a destroyed document. Yet 'substance' cannot authorise "
            "ultra-vires waivers, selective compassion or concealment of reasons. The perceptive "
            "civil servant identifies purpose, confirms authority, treats similar cases alike, "
            "records the departure and enables review. Thus substance corrects mechanical "
            "literalism; legality and procedural safeguards prevent purposivism from becoming "
            "arbitrary discretion."
        ),
    },
    {
        "year": 2024,
        "question": (
            "GS-IV Q3(c): Explain the present-day meaning of the quotation attributed in the "
            "paper to Immanuel Kant: in law a person is guilty upon violating another's rights, "
            "whereas in ethics guilt may arise even from thinking of doing so. "
            "Format: 10 marks; one 150-word answer."
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf. "
            "This is Q3(c) alone, not the full 30-mark Q3. The wording is not traceable to "
            "a Kant-published work; the nearest identified source is Louis Infield's 1930 "
            "translation of student lecture notes."
        ),
        "answer": (
            "The quotation distinguishes law's minimum external standard from ethics' wider "
            "assessment of the agent's maxim and disposition. Law ordinarily requires an "
            "observable act, attempt or legally defined omission before coercive liability "
            "arises. Ethical criticism can begin earlier: a public servant who deliberately "
            "plans to deny benefits on caste grounds has already adopted a wrongful maxim even "
            "if supervision prevents its execution.\n\n"
            "The point is not that every passing thought creates equal moral guilt. Kantian "
            "evaluation concerns a willed maxim or settled intention, not an involuntary mental "
            "event. Contemporary administration therefore needs both codes of conduct, which "
            "specify enforceable external behaviour, and codes of ethics, which cultivate "
            "integrity, impartiality and respect. Ethical self-scrutiny prevents wrongful "
            "intentions from becoming official action, while law preserves due process by not "
            "punishing mere unchosen thoughts."
        ),
    },
    {
        "year": 2024,
        "question": (
            "GS-IV Q1(a): Critically examine from the ethical point of view the proposition "
            "that Artificial Intelligence can serve as a dependable input for rational "
            "administrative decision-making. Format: 10 marks; one 150-word answer."
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf. "
            "The official English paper prints 'dependeble'; normalised spelling is used in "
            "the neutral rendering rather than falsely claiming a verbatim quotation."
        ),
        "answer": (
            "AI can improve administrative consistency, pattern detection, speed and evidence "
            "use, supporting consequentialist goals of better service delivery and risk "
            "reduction. It is not an ethically self-sufficient or invariably dependable source. "
            "Biased data may reproduce exclusion; opaque outputs obstruct reasons and appeal; "
            "automation can dilute accountability and treat citizens as data points rather than "
            "persons with dignity.\n\n"
            "A deontological floor requires legality, equality, privacy, due process and human "
            "responsibility. Consequence analysis should test false positives, distributional "
            "harm and long-term trust, not efficiency alone. Virtue ethics adds phronesis: an "
            "experienced official must know when to rely on, question or override an output. "
            "Therefore AI should be an auditable input under human oversight, with explainability, "
            "bias testing, grievance redressal and a named accountable authority; final moral "
            "responsibility cannot be delegated to the model."
        ),
    },
    {
        "year": 2018,
        "question": (
            "Neutral rendering of GS-IV Q12: Edward Snowden disclosed classified government "
            "surveillance material, claiming a moral obligation to inform the public despite "
            "legal prohibition. Analyse the episode by weighing the competing values and "
            "examine whether the disclosure was ethically justified. Format: 20 marks; "
            "one 250-word answer."
        ),
        "marks": 20,
        "source_note": (
            "Verified against the local 2018 GS-IV scan and routing ledger. Legal labels in "
            "the stem, including any characterisation as treason, must be treated as question "
            "framing rather than asserted as an independently settled conclusion."
        ),
        "answer": (
            "The dilemma is not simply legality versus conscience. It involves duties of "
            "confidentiality, rule of law and protection of legitimate security operations, "
            "set against privacy, democratic oversight, truthfulness and the public's right "
            "to know of potentially unlawful surveillance.\n\n"
            "Deontology initially reveals conflicting duties: keeping an entrusted secret and "
            "respecting citizens as rights-bearing ends. A rights argument is needed to explain "
            "why one duty may prevail. Consequentialism weighs democratic correction and reduced "
            "abuse against operational damage, exposure of innocent persons, precedent and loss "
            "of institutional trust. Virtue ethics asks whether courage was joined by prudence, "
            "temperance and responsibility rather than self-display.\n\n"
            "Ethical defensibility depends on method. The discloser should normally document the "
            "wrong, use protected internal or legislative oversight channels where reasonably "
            "available, disclose only what is necessary, redact unrelated sensitive information "
            "and accept independent scrutiny. Public disclosure becomes stronger where the harm "
            "is grave, internal channels are ineffective or complicit, and narrower disclosure "
            "can realistically secure accountability.\n\n"
            "Thus a moral motive is relevant but insufficient. The qualified test is necessity, "
            "proportionality, minimisation, channel exhaustion and accountability. A targeted "
            "disclosure satisfying these conditions can be morally defensible despite a legal "
            "breach; indiscriminate release cannot claim automatic justification from a good end."
        ),
    },
    {
        "year": 2019,
        "question": (
            "Neutral rendering of GS-IV Q8: Civil servants have sometimes been implicated or "
            "imprisoned for bona-fide mistakes, unsettling the moral fibre of the services. "
            "Explain how this trend affects civil-service functioning and suggest measures "
            "to protect honest officers. Format: 20 marks; one 250-word answer."
        ),
        "marks": 20,
        "source_note": (
            "Verified against the local 2019 GS-IV scan and routing ledger. This is a "
            "cross-application of moral luck and is primarily routed to the honest-officials "
            "and case-study owners."
        ),
        "answer": (
            "Automatic suspicion after every failed decision confuses bad outcome with bad "
            "process. Resultant moral luck explains why an officer may be blamed more severely "
            "than an equally diligent colleague merely because unforeseeable events produced a "
            "worse result.\n\n"
            "Such outcome bias encourages defensive administration: delay, excessive referral, "
            "avoidance of innovation, refusal to exercise lawful discretion and preference for "
            "inaction over public-interest risk. It weakens morale, deters capable recruits and "
            "can itself reduce welfare. Yet blanket immunity would shelter negligence and "
            "corruption.\n\n"
            "Protection should therefore be process-based. Preliminary scrutiny must distinguish "
            "a vigilance angle from a genuine commercial or administrative decision that went "
            "wrong. Review the information available at the time, delegated authority, conflict "
            "disclosures, consultation, recorded alternatives, due diligence and treatment of "
            "foreseeable risk. Use expert screening, reasoned and time-bound sanction decisions, "
            "protection from repeated inquiries on identical facts, legal support for bona-fide "
            "action and penalties for malicious complaints. Outcomes should remain evidence and "
            "feedback, especially where warnings were ignored.\n\n"
            "The ethical standard is neither success nor failure alone. It is demonstrable good "
            "faith, competence and reasonable process ex ante, combined with accountability for "
            "negligence, corrupt motive or concealment."
        ),
    },
    {
        "year": 2021,
        "question": (
            "Neutral rendering of GS-IV Q10: As a hospital administrator during an infectious "
            "COVID-19 crisis, identify and justify the criteria for deploying clinical and "
            "non-clinical staff, and examine whether the justification would differ in a "
            "private hospital. Format: 20 marks; one 250-word answer."
        ),
        "marks": 20,
        "source_note": (
            "Verified against the local 2021 GS-IV scan and routing ledger. The official demand "
            "concerns allocation of scarce staff, not directly ventilator or patient allocation."
        ),
        "answer": (
            "The administrator owes duties to patients, employees, families and the continuity "
            "of essential services. Relevant criteria are clinical competence, urgency of tasks, "
            "infection exposure, comorbid vulnerability, prior training, availability of PPE, "
            "rotation and recovery time, voluntariness where meaningful, and the minimum staffing "
            "needed outside COVID care.\n\n"
            "Consequentialism supports deploying scarce expertise where it saves the most lives "
            "and prevents system collapse. Deontology prohibits treating staff merely as expendable "
            "resources: adequate protection, truthful risk communication, non-discrimination and "
            "reasonable accommodation remain mandatory. Virtue ethics requires courage joined "
            "with prudence and compassion. The process should publish objective criteria, train "
            "redeployed personnel, separate tasks by competence, provide PPE and insurance, rotate "
            "high-exposure teams, enable confidential health declarations and create rapid review "
            "for disputed assignments. Senior leadership should share burdens rather than transfer "
            "all risk downward.\n\n"
            "The ethical justification does not fundamentally change in a private hospital. "
            "Ownership may affect contracts, finances and referral networks, but dignity, worker "
            "safety, clinical need and professional duty remain the same. Profit or employment "
            "power cannot justify avoidable exposure. A private institution may coordinate with "
            "public authorities and recover legitimate costs, but the common ethical floor is "
            "transparent, proportionate and competence-based deployment."
        ),
    },
    {
        "year": 2022,
        "question": (
            "Neutral rendering of GS-IV Q1: (a) Critically evaluate the claim that lack of "
            "wisdom in administration may cause even small errors to produce a travesty of "
            "justice. (b) Explain why empathy and compassion are vital attributes for civil "
            "servants. Combined format: 10 + 10 marks; two separate 150-word answers."
        ),
        "marks": 20,
        "source_note": (
            "Verified against the local 2022 GS-IV scan and routing ledger. Part (a) supports "
            "phronesis and purposive judgment; part (b) is cross-linked to Emotional Intelligence."
        ),
        "answer": (
            "(a) Administrative wisdom resembles phronesis: the capacity to connect rules, "
            "evidence, purpose and the particular human situation. A small clerical discrepancy "
            "can become a travesty when an official mechanically denies a widow's pension despite "
            "lawful alternative verification. Wisdom identifies what is essential, anticipates "
            "disproportionate harm and records a legally defensible solution. It is not permission "
            "to ignore rules; unstructured discretion can itself cause injustice. Training, "
            "consultation, speaking orders, review and attention to constitutional values convert "
            "experience into accountable judgment.\n\n"
            "(b) Empathy enables a civil servant to understand another person's perspective and "
            "barriers; compassion adds motivation to relieve avoidable suffering. They improve "
            "policy design, respectful communication and detection of hidden exclusion. A "
            "collector who understands why persons with disabilities cannot use a digital-only "
            "portal can arrange accessible alternatives. However, compassion without impartial "
            "criteria may become favouritism, while empathy without competence may not solve the "
            "problem. These attributes should therefore activate careful inquiry and humane "
            "implementation within law, equality and evidence."
        ),
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q7 case study: Vijay, Deputy Commissioner of a remote hilly district, is "
            "leading rescue and relief after a destructive cloudburst when his mother dies in "
            "Kerala and messages urge him to perform the last rites as conditions deteriorate. "
            "(a) Identify his options. (b) Identify the ethical dilemmas. (c) Critically evaluate "
            "each identified option. (d) Select the most appropriate option and justify it. "
            "Combined format: 20 marks; one 250-word answer covering all four demands."
        ),
        "marks": 20,
        "source_note": (
            "Wording and four explicit sub-demands verified against books\\mains\\UPSC Mains "
            "2025 GS Paper 4.pdf. The answer must remain one integrated 250-word response, not "
            "four separate 250-word answers."
        ),
        "answer": (
            "Vijay's options are: remain throughout the emergency; leave immediately for the "
            "last rites; briefly leave after transferring command; or arrange remote participation "
            "and travel only after stabilisation. The dilemmas are public duty versus filial and "
            "cultural obligation, irreplaceable personal loss versus responsibility for thousands, "
            "and whether delegation is responsible leadership or abandonment.\n\n"
            "Remaining provides continuity, reassures teams and protects rescue operations, but "
            "imposes severe personal cost and may deny a final family duty. Immediate departure "
            "respects grief and last rites but is unsafe if command systems are fragile. A brief "
            "departure is defensible only with a competent incident commander, written delegation, "
            "communication redundancy, clear resource authority and an agreed recall threshold. "
            "Remote participation is operationally safest but may inadequately meet personal and "
            "cultural needs.\n\n"
            "Deontology emphasises both entrusted public duty and familial obligation. "
            "Consequentialism gives great weight to avoidable mass harm during the deteriorating "
            "crisis. Virtue ethics requires practical wisdom, humanity and responsible delegation, "
            "not performative self-sacrifice. Motive, intention and consequence must be separated: "
            "filial love is a good motive, but an unplanned departure may create a defective "
            "operational intention; the final disaster outcome may also involve moral luck.\n\n"
            "The best course is to stabilise command immediately, transparently inform superiors, "
            "delegate in writing to the strongest available officer and assess whether a strictly "
            "time-bound visit is operationally safe. If not, he should remain and arrange remote "
            "rites, with institutional support for later travel. This preserves life-saving duty "
            "without denying his humanity."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Distinguish motive, intention and consequence as separate objects of moral "
            "appraisal in public administration."
        ),
        "answer": (
            "Motive is the background reason moving an agent; intention is the result and "
            "means deliberately chosen; consequence is what actually follows. They may point "
            "in different ethical directions. A district officer may be moved by compassion, "
            "intend an unauthorised preference for her native village, and accidentally produce "
            "a beneficial outcome. The good motive does not cure the discriminatory intention, "
            "and the fortunate result does not retrospectively make the process fair.\n\n"
            "Deontology examines the maxim, duty and chosen means. Consequentialism compares "
            "expected effects, while virtue ethics considers the character expressed by motive "
            "and judgment. Actual outcomes still matter, but moral-luck analysis asks how much "
            "was foreseeable or controllable.\n\n"
            "A sound administrative evaluation therefore records the officer's purpose, chosen "
            "course, information available at the time, foreseeable risks and realised effects "
            "separately. This prevents benevolent rhetoric from excusing unlawful conduct and "
            "prevents hindsight from condemning a diligent decision solely because chance "
            "produced a bad result."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Differentiate act utilitarianism from rule utilitarianism through public "
            "administration examples."
        ),
        "answer": (
            "Act utilitarianism evaluates each particular act by asking which available choice "
            "will produce the greatest expected net welfare. A disaster officer may open a locked "
            "public building without prior approval to shelter families because delay would cause "
            "serious harm.\n\n"
            "Rule utilitarianism instead asks which generally accepted rule produces the best "
            "long-run consequences. Transparent competitive procurement may therefore be retained "
            "even where direct selection appears faster in one ordinary purchase, because the rule "
            "protects predictability, trust and non-arbitrariness across cases.\n\n"
            "The two can converge, but they can diverge over exceptions. Act utility risks "
            "short-term calculation, favouritism disguised as welfare and erosion of precedent. "
            "Rule utility risks rule worship when an exceptional emergency defeats the rule's own "
            "purpose. Public administration should normally use welfare-promoting rules, while "
            "allowing narrowly authorised, recorded and reviewable exceptions where necessity and "
            "proportionality are demonstrable. Fundamental dignity and equality remain a "
            "deontological floor rather than variables in the utility total."
        ),
    },
    {
        "marks": 15,
        "question": (
            "A public servant may do good where no law or rule expressly prohibits the act, "
            "but a good end does not automatically justify irregular means. Examine."
        ),
        "answer": (
            "Administrative initiative is necessary because rules cannot anticipate every human "
            "need. Yet silence in a rulebook is not a free-standing source of power. A beneficial "
            "act is ethically defensible only when the official has delegated authority, no "
            "express or implied prohibition applies, public resources are properly used, similarly "
            "placed citizens receive equal treatment and reasons are recorded for review.\n\n"
            "The three theories expose different risks. Deontology asks whether the means violate "
            "duty, dignity or due process. Consequentialism compares immediate benefit with hidden "
            "costs, precedent, administrative capacity and long-term trust. Virtue ethics asks "
            "whether a prudent and just officer would regard the initiative as faithful to public "
            "purpose rather than compassionate favouritism.\n\n"
            "For example, accepting an equivalent identity document from every flood-affected "
            "pensioner may fulfil a scheme's lawful substance. Fabricating eligibility records to "
            "pay deserving persons uses a dishonest means that damages accountability and cannot "
            "become proper merely because the recipients are needy.\n\n"
            "Clean means should therefore form the presumptive floor. In genuine emergencies, a "
            "limited procedural departure may be defended through necessity and proportionality, "
            "provided core rights are preserved, the departure is documented and normal oversight "
            "is restored promptly. The appropriate ideal is principled initiative: purposive, "
            "equal, lawful and consequence-aware."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Context-sensitive justice is not ethical relativism. Discuss through phronesis "
            "and the form-versus-substance problem."
        ),
        "answer": (
            "Context-sensitive justice means that stable ethical commitments may require different "
            "applications when facts, knowledge, technology or the distribution of burdens change. "
            "It does not mean that every community or official may redefine justice at will. "
            "Dignity, equality, legality and non-arbitrariness remain controlling standards.\n\n"
            "Aristotelian phronesis explains the bridge. General rules cannot contain every material "
            "feature of a case; practical wisdom perceives which features matter and applies the "
            "rule's ethical purpose responsibly. Emergency movement restrictions may protect life "
            "during a lethal outbreak yet become disproportionate after the danger passes. An "
            "automated welfare rule may require revision when evidence reveals exclusion of persons "
            "with disabilities.\n\n"
            "The same reasoning addresses form and substance. Form supplies consistency, notice and "
            "review. Substance prevents literal compliance from defeating the lawful purpose, as "
            "when equivalent proof can replace a document destroyed in a flood. However, a civil "
            "servant cannot invoke 'true intent' to invent power, favour associates or bypass an "
            "implied prohibition.\n\n"
            "A defensible contextual decision therefore identifies the stable value, demonstrates "
            "the changed facts, confirms legal authority, treats comparable persons alike, records "
            "reasons and permits appeal. Phronesis corrects mindless literalism; institutional "
            "safeguards prevent practical wisdom from becoming personal relativism."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Design an ethical framework for allocating scarce life-saving resources by "
            "reconciling deontology, consequentialism and virtue ethics."
        ),
        "answer": (
            "Scarcity creates a genuine divergence among moral theories. Consequentialism supports "
            "using clinical evidence to maximise lives or life-years saved and to avoid wasting "
            "resources on interventions unlikely to work. A deontological approach insists that "
            "every person has equal worth: caste, wealth, political influence, disability stigma "
            "or perceived social usefulness cannot decide priority. Virtue ethics adds phronesis, "
            "compassion, justice and courage in confronting cases not resolved by a formula.\n\n"
            "A defensible framework should begin with transparent eligibility based on clinical "
            "need and evidence of likely benefit. Among materially similar patients, use a neutral "
            "tie-breaker such as lottery rather than status. Protect vulnerable groups against "
            "indirect discrimination, but do not convert vulnerability into an unexplained override "
            "of medical feasibility. Separate bedside clinicians from final allocation where "
            "possible, publish criteria in accessible languages, document decisions and provide "
            "rapid review. Reassess the framework as resources, evidence and disease patterns change.\n\n"
            "Alternative approaches reveal the need for synthesis. Pure first-come allocation may "
            "reward geographic and informational advantage. Pure survival maximisation may devalue "
            "persons with chronic disability. Unstructured compassion invites inconsistency and "
            "VIP pressure.\n\n"
            "The recommended hybrid is consequence-sensitive but rights-constrained: evidence "
            "determines where treatment can help, equal dignity limits forbidden distinctions, and "
            "phronesis manages residual conflict under recorded criteria. Communication must explain "
            "that non-selection is not a judgment of lesser human value, and palliative or alternative "
            "care remains owed to every person. The framework should undergo periodic ethical audit."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Moral luck complicates the evaluation of good-faith administrative decisions, "
            "but cannot become an excuse for negligence. Analyse."
        ),
        "answer": (
            "Moral luck describes the tension between the principle that responsibility should track "
            "control and the fact that ordinary judgment is strongly influenced by matters beyond "
            "control. Nagel distinguishes resultant luck in outcomes, circumstantial luck in the "
            "situations faced, constitutive luck in temperament and capacities, and causal luck in "
            "the antecedent chain shaping choice. Williams should not be credited with an identical "
            "fourfold taxonomy.\n\n"
            "Administration most directly encounters resultant and circumstantial luck. Two officers "
            "may conduct equally diligent procurement, yet only one contractor fails because of an "
            "unforeseeable market shock. An officer posted during a cloudburst faces choices that a "
            "colleague in a peaceful district never confronts. Judging solely by outcome encourages "
            "defensive governance, delay and avoidance of legitimate risk.\n\n"
            "The corrective is an ex-ante process test: Was the officer competent and authorised? "
            "Were conflicts disclosed, alternatives examined, expert advice sought, foreseeable risks "
            "mitigated and reasons recorded on the information then available? This reflects the ARC "
            "logic of separating bona-fide error or a commercial decision gone wrong from misconduct.\n\n"
            "Outcomes nevertheless remain relevant. They may reveal ignored warnings, support learning "
            "or show that assumptions require revision. A successful project cannot excuse skipped "
            "safety tests, just as an unforeseeable failure does not prove corruption. Moral luck "
            "protects sound good-faith judgment from hindsight bias; it does not protect bad faith, "
            "recklessness, concealment or negligent disregard of foreseeable harm. Independent review "
            "should test these recorded claims."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": "1. Anatomy of a morally appraised action",
        "structural_type": "layered-process-flow",
        "nodes": (
            "Start with the situation, relevant facts and realistic alternatives.",
            "Identify motive: the background reason moving the agent.",
            "Identify intention: the result and means deliberately chosen.",
            "Test the chosen means for duty, dignity and legality.",
            "Estimate expected and reasonably foreseeable consequences.",
            "Record actual consequences without equating outcome with complete responsibility.",
            "Separate what was controlled from resultant or circumstantial luck.",
            "Triangulate duty, consequence and character into a reasoned verdict.",
        ),
        "verdict": "Never let a good motive or fortunate outcome substitute for appraisal of intention and means.",
        "answer_use": "Use as the opening diagnostic in any theory question or administrative case study.",
    },
    {
        "title": "2. Deontological duty ladder",
        "structural_type": "vertical-duty-ladder",
        "nodes": (
            "Good will asks whether the agent acts from duty rather than expediency.",
            "State the operative maxim behind the proposed administrative act.",
            "Universalise the maxim and test for contradiction or selective privilege.",
            "Apply the humanity formula: never treat persons merely as means.",
            "Identify the duty and rights floor that outcomes cannot ordinarily override.",
            "Recognise agent-relative restraints on one's own lying, coercion or falsification.",
            "Where duties conflict, identify their grounds instead of mechanically repeating rules.",
            "Give a reasoned priority while acknowledging deontology's rigidity limit.",
        ),
        "verdict": "Deontology supplies non-negotiable floors, but hard cases still require reasoned priority among duties.",
        "answer_use": "Use to write the duty-and-rights paragraph in a Mains answer or case evaluation.",
    },
    {
        "title": "3. Consequentialist outcome calculus",
        "structural_type": "multi-stage-calculus",
        "nodes": (
            "List feasible alternatives rather than comparing action only with inaction.",
            "Map every materially affected stakeholder, including weak and future interests.",
            "Estimate expected benefits under each alternative.",
            "Estimate direct, indirect and opportunity-cost harms.",
            "Attach realistic probabilities and identify uncertainty.",
            "Examine distribution and the short, medium and long time horizons.",
            "Include precedent, institutional trust and behavioural incentives.",
            "Select the best expected outcome subject to an explicit rights check.",
        ),
        "verdict": "A utility total is credible only when stakeholders, uncertainty, distribution and long-term trust are visible.",
        "answer_use": "Use for policy appraisal, cost-benefit ethics and option comparison in case studies.",
    },
    {
        "title": "4. Act utility versus rule utility",
        "structural_type": "split-comparison",
        "nodes": (
            "Act utilitarianism treats the individual act as the unit of evaluation.",
            "Rule utilitarianism evaluates the general acceptance of a rule.",
            "Act utility asks whether a local exception improves expected welfare.",
            "Rule utility asks what widespread exception-making would produce.",
            "General rules create predictability and administrative coordination.",
            "Impartial rules protect trust and reduce disguised favouritism.",
            "Rigid adherence can become rule worship when context defeats purpose.",
            "Allow only authorised, recorded and reviewable purposive exceptions.",
        ),
        "verdict": "Use welfare-promoting rules as the default and narrow purposive exceptions as the safety valve.",
        "answer_use": "Use to differentiate the two theories or analyse procurement and emergency departures.",
    },
    {
        "title": "5. Virtue ethics and phronesis wheel",
        "structural_type": "hub-spoke-wheel",
        "nodes": (
            "Eudaimonia supplies the wider idea of human flourishing.",
            "Character concerns the kind of person repeated choices create.",
            "Habituation converts isolated good acts into reliable dispositions.",
            "The mean is appropriate response between excess and deficiency.",
            "Phronesis perceives which features of the context ethically matter.",
            "Public role and entrusted power shape the virtues demanded.",
            "Justice, courage, honesty, compassion and temperance must work together.",
            "Practical wisdom supplements rather than abolishes rules and evidence.",
        ),
        "verdict": "Virtue ethics explains the quality of judgment that rules and calculations alone cannot supply.",
        "answer_use": "Use for wisdom, leadership, context-sensitive judgment and role-ethics answers.",
    },
    {
        "title": "6. Intuition-to-reason reflective loop",
        "structural_type": "feedback-loop",
        "nodes": (
            "An intuitive reaction first signals that something may be morally salient.",
            "Experience and affect explain its speed and practical sensitivity.",
            "Bias, familiarity and in-group preference make intuition fallible.",
            "Pause before converting the felt response into official action.",
            "Gather facts, alternatives, law and affected-party perspectives.",
            "Test the reaction through duties, consequences and virtues.",
            "State public reasons capable of review and appeal.",
            "Revise the intuition or decision when the reasoned test requires it.",
        ),
        "verdict": "Intuition should trigger inquiry; reason should audit it; neither is sufficient alone.",
        "answer_use": "Use directly for 2023 Q4(b) and in the reasoning stage of any case study.",
    },
    {
        "title": "7. Doing good beyond the rulebook",
        "structural_type": "decision-gate",
        "nodes": (
            "Specify the public good the proposed initiative seeks.",
            "Confirm delegated authority to take the proposed action.",
            "Check for an express statutory or regulatory prohibition.",
            "Check purpose and structure for an implied prohibition.",
            "Protect rights, due process and equal treatment of comparable citizens.",
            "Examine resource diversion, precedent and institutional capacity.",
            "Record reasons, apply consistently and preserve review.",
            "Proceed only as calibrated initiative rather than personal benevolence.",
        ),
        "verdict": "No express prohibition is only the first gate, not a complete ethical or legal permission.",
        "answer_use": "Use as the full safeguard sequence for 2018 Q4(a) and discretion questions.",
    },
    {
        "title": "8. Means-and-ends ethical matrix",
        "structural_type": "four-quadrant-matrix",
        "nodes": (
            "Good end with good means is the strongest presumptive choice.",
            "Good end with wrongful means creates the central disputed case.",
            "Wrongful end cannot be rescued by procedurally proper means.",
            "Wrongful end with wrongful means is rejected by every lens.",
            "Kantian duty imposes dignity and universalisability restraints.",
            "Act and rule consequentialism may assess exceptions differently.",
            "Gandhian and virtue reasoning ask what tainted methods create.",
            "Final synthesis: rights floor, then necessity and proportionality.",
        ),
        "verdict": "Optimise consequences within clean means; justify emergency departures narrowly rather than sloganising ends.",
        "answer_use": "Use for 2018 Q4(b), whistleblowing, surveillance and emergency-power answers.",
    },
    {
        "title": "9. Scarce-resource triage funnel",
        "structural_type": "priority-funnel",
        "nodes": (
            "Define the scarcity, time pressure and divisible resource.",
            "Map patients, workers, families and institutional stakeholders.",
            "Use reliable clinical or need-based evidence.",
            "Estimate aggregate welfare and avoid preventable waste.",
            "Protect equal worth and prohibit status-based discrimination.",
            "Examine vulnerability and indirect barriers faced by weaker groups.",
            "Publish criteria, document choices and provide rapid review.",
            "Adopt a consequence-sensitive but rights-constrained hybrid decision.",
        ),
        "verdict": "Clinical benefit may guide priority, but it cannot convert social status into a measure of human worth.",
        "answer_use": "Use for health, disaster-relief and other scarce-resource allocation cases.",
    },
    {
        "title": "10. Snowden-type disclosure ladder",
        "structural_type": "escalation-ladder",
        "nodes": (
            "Identify the legal and professional duty of confidentiality.",
            "Identify privacy, public interest and democratic-accountability claims.",
            "Examine the discloser's motive without treating it as decisive.",
            "Examine intended audience, scope and chosen disclosure method.",
            "Compare public benefits with security, privacy and trust harms.",
            "Ask whether protected internal and oversight channels were viable.",
            "Apply necessity, minimisation and proportionality to the material released.",
            "Require accountability and an independently reviewable final verdict.",
        ),
        "verdict": "Ethical defensibility turns on targeted, necessary and accountable disclosure, not moral motive alone.",
        "answer_use": "Use for whistleblowing, secrecy-versus-conscience and public-interest disclosure questions.",
    },
    {
        "title": "11. Moral luck taxonomy and vigilance test",
        "structural_type": "taxonomy-to-process-map",
        "nodes": (
            "Control principle: blame should track what the agent could control.",
            "Resultant luck concerns how a decision actually turns out.",
            "Circumstantial luck concerns the situations an agent happens to face.",
            "Constitutive luck concerns temperament and capacities not wholly chosen.",
            "Causal luck concerns the antecedent causal chain shaping choice.",
            "Evaluate authority, evidence, diligence and foreseeable risk ex ante.",
            "Use outcomes as evidence and feedback, not the sole measure of blame.",
            "Apply the ARC-style bona-fides distinction without excusing negligence.",
        ),
        "verdict": "Protect sound good-faith judgment from hindsight bias while preserving liability for bad process.",
        "answer_use": "Use for failed projects, vigilance scrutiny, disaster command and the 2019 honest-officials case.",
    },
    {
        "title": "12. Context-relative justice review cycle",
        "structural_type": "continuous-review-cycle",
        "nodes": (
            "Begin with stable constitutional and ethical values.",
            "Identify changed facts, technology, knowledge or institutional capacity.",
            "Identify changed burdens, beneficiaries and patterns of exclusion.",
            "Ask whether the old application now produces injustice.",
            "Reject convenience-based relativism and preserve core rights.",
            "Prefer lawful substance over mechanical attachment to literal form.",
            "Confirm authority, record reasons and provide appeal or review.",
            "Continue scrutiny, including of evolving AI-assisted decisions.",
        ),
        "verdict": "Justice can require adaptive application without surrendering stable values or legality.",
        "answer_use": "Use directly for 2024 Q4 and as the current-affairs bridge to AI governance.",
    },
)

CURRENT_ANCHOR = {
    "title": (
        "India AI Governance Guidelines and the PIB M.A.N.A.V. vision for "
        "human-centric AI governance"
    ),
    "verified_facts": (
        "The India AI Governance Guidelines identify seven technology-agnostic sutras: "
        "Trust, People First, Innovation over Restraint, Fairness & Equity, Accountability, "
        "Understandable by Design, and Safety, Resilience & Sustainability.",
        "The India AI Governance Guidelines organise recommendations across enablement, "
        "regulation and oversight.",
        "A PIB brief dated 19 February 2026 states that the M.A.N.A.V. vision comprises "
        "Moral and Ethical Systems, Accountable Governance, National Sovereignty, "
        "Accessible and Inclusive AI, and Valid and Legitimate Systems.",
        "The PIB brief frames AI around human aspirations, ethics and dignity.",
    ),
    "administrative_link": (
        "⚠️ Inference, not official classification: People First, Fairness & Equity and "
        "Accountability can illustrate a deontological dignity-and-duty floor; Innovation "
        "over Restraint together with Safety, Resilience & Sustainability can illustrate "
        "consequence-sensitive optimisation; understandable design, oversight and the "
        "M.A.N.A.V. emphasis on ethical human purposes can illustrate the need for "
        "phronesis and retained human responsibility. The enablement-regulation-oversight "
        "structure also supports the 2024 demand for context-sensitive, non-literal governance."
    ),
    "limit": (
        "The two official sources do not classify their principles as deontology, "
        "consequentialism or virtue ethics. Those linkages are analytical inferences for "
        "GS-IV teaching. Do not add unverified implementation claims, dates, institutional "
        "powers or performance outcomes beyond the directly stated facts above."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://impact.indiaai.gov.in/IndiaAI_Governance_Guidelines.pdf",
    "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026219796801.pdf",
)

SOURCE_CAVEAT = (
    "Use the local Topic 08 Basic and Advanced owners as the controlling authored sources, "
    "subject to these corrections and attribution limits. The three theories identify "
    "different justificatory emphases, not exclusive one-to-one ownership of motive, "
    "intention or outcome. Consequentialism's ability to redeem a harmful means applies most "
    "clearly to unrestricted act consequentialism; rule and rights-sensitive versions may "
    "reject it. Care ethics is an adjacent relational tradition, not simply a virtue-ethics "
    "subtype. The golden mean is context-sensitive appropriateness, not an arithmetic midpoint. "
    "Moral luck is a general challenge to responsibility under limited control, not a phenomenon "
    "belonging only to consequentialism. Nagel supplies the standard four-part taxonomy; "
    "Williams must not be credited with an identical taxonomy. The Aristotle-phronesis and "
    "Indian svadharma comparison is an analogy, not an identity claim. Doing good without an "
    "express prohibition still requires delegated authority, absence of implied prohibition, "
    "equal treatment, recorded reasons and review. The 2021 GS-IV hospital case concerns scarce "
    "staff deployment, not directly ventilator or patient triage. The 2024 context-relative "
    "justice demand does not endorse ethical relativism, and substance cannot justify ultra-vires "
    "discretion. For 2024 GS-IV Q3(c), the quotation beginning 'In law, a man is guilty...' is "
    "attributed by the paper to Immanuel Kant but is not traceable to a Kant-published work; the "
    "nearest identified source is Louis Infield's 1930 translation of student lecture notes, so "
    "present it as attributed to Kant rather than as a verified verbatim passage from a published "
    "Kant text. Snowden-related legal characterisations belong to the question stem and should "
    "not be asserted independently as settled conclusions. Older PYQ text is neutrally rendered "
    "unless verified against a local official scan; combined questions retain their separate "
    "marks and word limits. The IndiaAI and PIB sources state governance principles but do not "
    "officially classify them under deontology, consequentialism or virtue ethics; all such "
    "linkages are explicitly analytical inference."
)

REGISTER_SUPPLEMENT = (
    "Rapid recall: MORAL ACTION — motive is why the agent acts; intention is the result and "
    "means deliberately chosen; expected consequences are foreseeable effects; actual "
    "consequences may include luck. Never let good motive erase defective intention, or a "
    "fortunate outcome vindicate negligent process. MEANS-ENDS — good ends do not automatically "
    "cleanse wrongful means. Deontology supplies rights and duty restraints; act utility may "
    "permit a welfare-maximising exception; rule utility tests the consequences of general "
    "exception-making; virtue ethics asks what the method habituates. "
    "DEONTOLOGY — Kantian tests: maxim, universalisation, humanity as an end, duty, good will. "
    "Agent-relative restraint means I remain responsible for my own falsification or coercion "
    "even if another may otherwise do worse. Consequences inform implementation but do not create "
    "the duty. Rights and constitutional dignity form an administrative floor. "
    "CONSEQUENTIALISM — compare realistic alternatives, all stakeholders, expected benefits and "
    "harms, probability, distribution, opportunity cost, precedent, trust and time horizon. Act "
    "utilitarianism evaluates the particular choice; rule utilitarianism evaluates general "
    "acceptance. Traps: aggregation can hide concentrated harm; forecasts and welfare measures "
    "can be manipulated; Bentham-act and Mill-rule are not mechanically interchangeable labels. "
    "VIRTUE ETHICS — character is formed through habituation; eudaimonia is flourishing; the "
    "golden mean is context-relative appropriateness; phronesis joins ethical purpose, experience, "
    "perception and deliberation. Public roles shape relevant virtues, but role cannot override "
    "constitutional morality. Care ethics is adjacent, not merely a subtype. "
    "INTUITION AND REASON — intuition is a fast affective signal useful in familiar situations "
    "but vulnerable to bias. Reasoning gathers facts and tests the signal against duties, "
    "consequences, virtues, law and constitutional values. Best sequence: signal -> pause -> "
    "facts -> theory test -> public reasons -> revise or act. "
    "CONTEXTUAL JUSTICE — stable values can require changed application when facts, knowledge, "
    "burdens or technology change. This is not relativism. Form protects consistency and review; "
    "substance prevents literalism from defeating lawful purpose. Purposive administration still "
    "requires authority, equal treatment, recorded reasons and appeal. "
    "DOING GOOD ABSENT PROHIBITION — check public purpose, delegated authority, express bar, "
    "implied bar, rights, equality, resources, precedent, consistency and review. No express "
    "prohibition is the first gate, not complete permission. "
    "TRIAGE — consequence-sensitive but rights-constrained hybrid: reliable need/clinical evidence, "
    "equal human worth, no VIP or status discrimination, vulnerability safeguards, published "
    "criteria, documentation, neutral tie-breaker and rapid review. The 2021 hospital PYQ is staff "
    "deployment; use it as analogous scarcity reasoning, not as a ventilator-allocation question. "
    "DISCLOSURE — competing values: secrecy, security and trust versus privacy, public interest and "
    "democratic accountability. Apply motive, intended scope, internal or oversight channels, "
    "necessity, minimisation, proportionality and accountability. A good motive cannot justify an "
    "indiscriminate leak. "
    "MORAL LUCK — Nagel: resultant, circumstantial, constitutive, causal. Williams is a companion "
    "originator, not the source of the identical fourfold list. Administrative test: authority, "
    "information available at the time, due diligence, expert advice, foreseeable risk, good faith "
    "and recorded reasons. Outcomes remain evidence and feedback; they are not the sole measure of "
    "blame. ARC-style bona-fides scrutiny protects honest risk-taking but never excuses negligence. "
    "ANSWER SPINE — identify dilemma -> separate motive/intention/consequence -> deontological floor "
    "-> consequentialist optimisation -> virtue/phronesis test -> convergence or divergence -> "
    "qualified decision -> implementation, reasons, review and residual-risk safeguards. "
    "CURRENT ANCHOR — verified official facts only: India AI Governance Guidelines' seven sutras "
    "(Trust; People First; Innovation over Restraint; Fairness & Equity; Accountability; "
    "Understandable by Design; Safety, Resilience & Sustainability) and recommendations across "
    "enablement, regulation and oversight; PIB's 19 February 2026 M.A.N.A.V. formulation (Moral and "
    "Ethical Systems; Accountable Governance; National Sovereignty; Accessible and Inclusive AI; "
    "Valid and Legitimate Systems), framing AI around human aspirations, ethics and dignity. Any "
    "mapping of these official principles to deontology, consequentialism or virtue ethics is "
    "analytical inference, not an official classification."
)
