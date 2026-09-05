"""Learner-v2 source data: Ethics Topic 07, Western Moral Philosophers and Thinkers."""

SESSION_TITLES = (
    "Western ethical reasoning: four lenses and source discipline",
    "Socrates and Plato: examination, knowledge, justice and wise rule",
    "Aristotle: flourishing, habituated virtue, the mean and practical wisdom",
    "Kant: good will, duty and the Categorical Imperative",
    "Kant's 2024 quotation: legal guilt, ethical intention and provenance",
    "Bentham and Mill: utility, pleasures and act-rule distinctions",
    "Mill's harm principle: liberty, coercion and majority power",
    "Rawls: original position, lexical priority and justice as fairness",
    "Comparative institutional ethics and Indian administrative applications",
    "Routed quotations, answer architecture and contemporary AI governance",
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
    ("10", "11"),
    ("12", "13"),
)

MCQ_ITEMS = (
    # --- Family A: Socratic-Platonic reason and order ---
    {
        "label": "Socratic examination converts introspection into reason-giving",
        "statement": (
            "Socratic examination requires an official to surface assumptions, ask for "
            "reasons, test contradictions and seek counter-views before exercising "
            "discretion; it is an anti-bias discipline rather than private introspection alone."
        ),
        "scenario_a": (
            "A district magistrate initially blames low vaccination uptake on community "
            "ignorance, then tests that assumption through field consultations and discovers "
            "that irregular clinic timings are the main cause. Which ethical method best "
            "describes this revision?"
        ),
        "scenario_b": (
            "A selection-board chair records the assumptions behind an interview score, asks "
            "another member to challenge them and revises the score when the reasons prove "
            "inconsistent. Which Western thinker supplies the controlling method?"
        ),
        "family": "Socratic-Platonic reason and order",
        "group": "Socratic-Platonic reason and order",
    },
    {
        "label": "Socratic intellectualism links virtue with knowledge of the good",
        "statement": (
            "Socratic intellectualism treats knowledge of the good as a necessary condition "
            "of virtue and connects wrongdoing with ignorance, while disciplined training "
            "and character safeguards remain necessary for public administration."
        ),
        "scenario_a": (
            "An ethics academy teaches procurement officers how hidden conflicts of interest "
            "distort judgment, arguing that recognising the ethical wrong is necessary before "
            "conduct can improve. Which Socratic proposition underlies the programme?"
        ),
        "scenario_b": (
            "A department assumes that merely circulating conduct rules will make every "
            "employee virtuous, despite incentives encouraging concealment. Which limitation "
            "must qualify a simplistic use of Socratic intellectualism?"
        ),
        "family": "Socratic-Platonic reason and order",
        "group": "Socratic-Platonic reason and order",
    },
    {
        "label": "Platonic justice is harmony in soul and institution",
        "statement": (
            "Plato defines justice as ordered harmony: reason governs spirit and appetite "
            "within the person, while each institutional part performs its proper function "
            "without usurping another's role."
        ),
        "scenario_a": (
            "A regulator separates investigation, adjudication and appellate review so that "
            "one unit cannot dominate the entire process. Which Platonic conception of justice "
            "provides the closest structural analogy?"
        ),
        "scenario_b": (
            "A senior officer lets political ambition and personal appetite override evidence "
            "and constitutional duty. In Plato's tripartite model, which failure of inner order "
            "does this illustrate?"
        ),
        "family": "Socratic-Platonic reason and order",
        "group": "Socratic-Platonic reason and order",
    },
    {
        "label": "The philosopher-ruler analogy requires democratic qualification",
        "statement": (
            "Plato's philosopher-ruler represents knowledgeable and public-spirited rule, but "
            "it cannot be equated with modern technocracy or merit recruitment without adding "
            "constitutional accountability, participation and checks on elite power."
        ),
        "scenario_a": (
            "A state proposes allowing technical experts to make binding environmental "
            "decisions without public hearings or judicial review because expertise alone "
            "guarantees wisdom. Which caution about Plato is decisive?"
        ),
        "scenario_b": (
            "A public-service commission combines specialist competence with transparent "
            "selection, legislative standards and judicial review. Which qualified use of "
            "Plato's philosopher-ruler ideal does this illustrate?"
        ),
        "family": "Socratic-Platonic reason and order",
        "group": "Socratic-Platonic reason and order",
    },
    # --- Family B: Aristotelian flourishing and judgment ---
    {
        "label": "Eudaimonia is whole-life flourishing rather than transient pleasure",
        "statement": (
            "Aristotle's eudaimonia means flourishing across a complete life through rational "
            "virtuous activity; it is not a passing feeling of happiness, pleasure or "
            "satisfaction produced by one successful decision."
        ),
        "scenario_a": (
            "An officer rejects a lucrative but ethically compromised posting and chooses a "
            "career marked by integrity, public service and sustained excellence. Which "
            "Aristotelian end best evaluates the life as a whole?"
        ),
        "scenario_b": (
            "A department equates employee well-being exclusively with short-term bonuses and "
            "entertainment events while ignoring meaningful work and character. Which "
            "Aristotelian distinction exposes the mistake?"
        ),
        "family": "Aristotelian flourishing and judgment",
        "group": "Aristotelian flourishing and judgment",
    },
    {
        "label": "Virtue is a disposition built by habituated action",
        "statement": (
            "For Aristotle, moral virtue is a stable disposition formed through repeated "
            "right action and appropriate feeling; isolated good deeds or theoretical "
            "knowledge alone do not create a virtuous administrator."
        ),
        "scenario_a": (
            "A probation programme repeatedly places trainees in supervised citizen-hearing "
            "situations so that patience, fairness and courage become reliable habits. Which "
            "Aristotelian mechanism explains the design?"
        ),
        "scenario_b": (
            "An officer makes one conspicuous charitable donation but routinely humiliates "
            "beneficiaries. Why would Aristotle refuse to infer the virtue of generosity from "
            "the isolated act?"
        ),
        "family": "Aristotelian flourishing and judgment",
        "group": "Aristotelian flourishing and judgment",
    },
    {
        "label": "The Golden Mean is context-relative proportion, not arithmetic compromise",
        "statement": (
            "Aristotle's Golden Mean lies between excess and deficiency relative to the "
            "circumstances and agent; it is not a mathematical midpoint, and intrinsically "
            "wrong acts do not become virtuous through moderation."
        ),
        "scenario_a": (
            "During a tense procession, a district magistrate rejects both indiscriminate "
            "force and complete inaction, selecting targeted restrictions proportionate to "
            "verified risks. Which Aristotelian doctrine structures the judgment?"
        ),
        "scenario_b": (
            "An official argues that accepting a smaller bribe is the virtuous mean between "
            "taking a large bribe and refusing all payment. Which feature of Aristotle's "
            "doctrine makes this reasoning invalid?"
        ),
        "family": "Aristotelian flourishing and judgment",
        "group": "Aristotelian flourishing and judgment",
    },
    {
        "label": "Phronesis supplies context-sensitive practical wisdom",
        "statement": (
            "Aristotelian phronesis is the trained capacity to identify the appropriate "
            "virtue and proportion in a particular case, but administrative judgment must "
            "remain bounded by law, evidence and review."
        ),
        "scenario_a": (
            "Flood-relief rules do not anticipate a marooned migrant settlement. The collector "
            "uses evidence, humane judgment and recorded reasons to adapt delivery without "
            "abandoning legal safeguards. Which capacity is being exercised?"
        ),
        "scenario_b": (
            "Two officers invoke personal wisdom to reach opposite decisions without evidence "
            "or recorded reasons. Which institutional qualification prevents phronesis from "
            "becoming arbitrary discretion?"
        ),
        "family": "Aristotelian flourishing and judgment",
        "group": "Aristotelian flourishing and judgment",
    },
    # --- Family C: Kantian duty and dignity ---
    {
        "label": "Moral worth depends on acting from duty",
        "statement": (
            "Kant distinguishes acting from duty from merely conforming to duty: outwardly "
            "correct conduct lacks full moral worth when motivated only by advantage, fear "
            "of detection or expected praise."
        ),
        "scenario_a": (
            "A procurement officer refuses a bribe solely because surveillance cameras are "
            "present, while intending to accept one later. Which Kantian distinction explains "
            "why outward compliance is ethically insufficient?"
        ),
        "scenario_b": (
            "A civil servant discloses an error despite certain reputational loss because "
            "truthfulness is owed to citizens. Which feature gives the act Kantian moral worth?"
        ),
        "family": "Kantian duty and dignity",
        "group": "Kantian duty and dignity",
    },
    {
        "label": "Universalisability tests the consistency of an official's maxim",
        "statement": (
            "Kant's universal-law formulation asks whether the maxim underlying an act could "
            "be consistently willed as a rule for everyone, exposing self-serving exceptions "
            "invented for personal convenience."
        ),
        "scenario_a": (
            "An officer proposes concealing audit findings whenever disclosure may delay a "
            "social project. If every official followed that maxim, public audit would become "
            "self-defeating. Which Kantian test reveals the contradiction?"
        ),
        "scenario_b": (
            "A licensing official waives documentation only for relatives but could not will "
            "a universal rule permitting all officers the same favouritism. Which formulation "
            "directly condemns the exception?"
        ),
        "family": "Kantian duty and dignity",
        "group": "Kantian duty and dignity",
    },
    {
        "label": "The humanity formula prohibits using citizens merely as means",
        "statement": (
            "Kant's humanity formulation requires treating every person as an end with "
            "rational agency, prohibiting officials from using citizens merely as instruments "
            "for targets, revenue, publicity or political advantage."
        ),
        "scenario_a": (
            "A district stages beneficiaries for a publicity event without informed consent "
            "and exposes their medical status to improve programme visibility. Which Kantian "
            "principle is most directly violated?"
        ),
        "scenario_b": (
            "A rehabilitation plan gives displaced families complete information, meaningful "
            "consultation and real choice rather than treating compensation as purchase of "
            "compliance. Which Kantian requirement does it respect?"
        ),
        "family": "Kantian duty and dignity",
        "group": "Kantian duty and dignity",
    },
    {
        "label": "Kantian ethical guilt concerns harboured intention and disposition",
        "statement": (
            "The 2024 Kant quotation contrasts external legal violation with ethical appraisal "
            "of a harboured wrongful intention; it must not be converted into punishment for "
            "involuntary or passing thoughts."
        ),
        "scenario_a": (
            "An officer secretly resolves to favour a contractor but the tender is cancelled "
            "before any illegal award. Which distinction explains why criminal liability may "
            "be absent while ethical failure remains?"
        ),
        "scenario_b": (
            "A public employee experiences an unwanted prejudiced thought, rejects it and acts "
            "impartially. Why would the careful reading of Kant's reconstructed lecture reject "
            "automatic ethical guilt?"
        ),
        "family": "Kantian duty and dignity",
        "group": "Kantian duty and dignity",
    },
    # --- Family D: Millian utility and liberty ---
    {
        "label": "Millian utility includes qualitative differences among pleasures",
        "statement": (
            "Utilitarianism evaluates acts and policies by their contribution to aggregate "
            "happiness or welfare, while Mill's distinction between higher and lower pleasures "
            "rejects a purely quantitative or majority-headcount calculus."
        ),
        "scenario_a": (
            "A city compares a commercial entertainment project with a public-library network "
            "that yields fewer immediate visits but deeper educational and civic benefits. "
            "Which Millian refinement is relevant?"
        ),
        "scenario_b": (
            "A welfare department counts only the number of beneficiaries reached and ignores "
            "the dignity, quality and durability of outcomes. Which limitation of a crude "
            "utility calculation does this reveal?"
        ),
        "family": "Millian utility and liberty",
        "group": "Millian utility and liberty",
    },
    {
        "label": "Act and rule utilitarianism evaluate different objects",
        "statement": (
            "Act utilitarianism evaluates the consequences of a particular act, whereas rule "
            "utilitarianism evaluates generally followed rules; treating Mill himself as "
            "exclusively a rule utilitarian remains a disputed interpretation."
        ),
        "scenario_a": (
            "To calm a mob, an officer considers framing one innocent person, but then evaluates "
            "the long-run consequences of a general rule permitting such punishment. Which "
            "utilitarian variant performs the second test?"
        ),
        "scenario_b": (
            "A student states without qualification that Mill invented and unequivocally "
            "endorsed modern rule utilitarianism. Which historical caution should correct the "
            "claim?"
        ),
        "family": "Millian utility and liberty",
        "group": "Millian utility and liberty",
    },
    {
        "label": "The harm principle creates a presumption against coercion",
        "statement": (
            "Mill permits coercion of a competent adult principally to prevent harm to others, "
            "not merely offence, moral dislike or paternalistic enforcement of majority "
            "preferences; the boundary of harm remains contestable."
        ),
        "scenario_a": (
            "A municipality bans an unconventional peaceful performance solely because many "
            "residents find it offensive, although no demonstrable injury is shown. Which "
            "Millian distinction weighs against the ban?"
        ),
        "scenario_b": (
            "A factory's private operating choices contaminate a village water source. Which "
            "side of Mill's self-regarding and other-regarding distinction justifies state "
            "intervention?"
        ),
        "family": "Millian utility and liberty",
        "group": "Millian utility and liberty",
    },
    {
        "label": "Utilitarian rights safeguards remain consequential and contestable",
        "statement": (
            "Rule-utilitarian support for stable rights and Mill's liberty principle constrain "
            "crude welfare maximisation, but they do not make every liberty-welfare conflict "
            "disappear or turn utilitarianism into deontology."
        ),
        "scenario_a": (
            "A police chief defends due process because a stable rule against arbitrary arrest "
            "maximises long-run trust and security. Which theory justifies the rule through its "
            "consequences rather than inherent duty?"
        ),
        "scenario_b": (
            "A policymaker claims that calling a policy rule-utilitarian makes individual "
            "rights absolute and immune from future welfare calculations. Which conceptual "
            "limit invalidates the claim?"
        ),
        "family": "Millian utility and liberty",
        "group": "Millian utility and liberty",
    },
    # --- Family E: Rawlsian institutional fairness ---
    {
        "label": "The original position filters morally arbitrary advantage",
        "statement": (
            "Rawls's original position is a device of representation in which parties choose "
            "principles without knowing morally arbitrary facts about their eventual class, "
            "talents, identity or conception of the good."
        ),
        "scenario_a": (
            "A committee designs disability-benefit access while imagining that any member "
            "could later be a remote, poor or disabled applicant. Which Rawlsian device guides "
            "the exercise?"
        ),
        "scenario_b": (
            "An official rejects the veil of ignorance because policymakers cannot literally "
            "erase knowledge of their identities. Which distinction shows why this objection "
            "misunderstands Rawls?"
        ),
        "family": "Rawlsian institutional fairness",
        "group": "Rawlsian institutional fairness",
    },
    {
        "label": "Equal basic liberties have lexical priority",
        "statement": (
            "Rawls gives equal basic liberties lexical priority over social and economic "
            "advantages; they cannot be reduced merely to secure higher income, administrative "
            "efficiency or greater aggregate welfare."
        ),
        "scenario_a": (
            "A government proposes suppressing peaceful criticism because investor confidence "
            "and tax revenue may rise. Which Rawlsian priority blocks trading a basic liberty "
            "for economic gain?"
        ),
        "scenario_b": (
            "A welfare programme improves average income but conditions benefits on surrendering "
            "freedom of association. Which first step in Rawls's ordering has the programme "
            "failed?"
        ),
        "family": "Rawlsian institutional fairness",
        "group": "Rawlsian institutional fairness",
    },
    {
        "label": "Fair equality of opportunity precedes the difference principle",
        "statement": (
            "Fair equality of opportunity requires genuinely accessible offices and prospects, "
            "not merely formal non-discrimination, and it takes priority within Rawls's second "
            "principle over the difference principle."
        ),
        "scenario_a": (
            "A civil-service examination is formally open to all, but inaccessible centres and "
            "unavailable assistive technology exclude many disabled candidates. Which Rawlsian "
            "standard is unmet?"
        ),
        "scenario_b": (
            "A policy increases income for the poorest but reserves influential public offices "
            "for one hereditary group. Which lexical priority prevents invoking the difference "
            "principle as a defence?"
        ),
        "family": "Rawlsian institutional fairness",
        "group": "Rawlsian institutional fairness",
    },
    {
        "label": "The difference principle civilises rather than abolishes inequality",
        "statement": (
            "Rawls permits social and economic inequality only when it benefits the least "
            "advantaged after liberty and fair opportunity are secured; the principle neither "
            "requires identical outcomes nor validates every transfer."
        ),
        "scenario_a": (
            "A higher rural-service allowance attracts doctors to underserved districts and "
            "materially improves care for the worst-off. Which Rawlsian principle can justify "
            "the pay inequality?"
        ),
        "scenario_b": (
            "A subsidy enriches an already privileged industry while offering only symbolic "
            "benefits to poor households. Which Rawlsian burden has not been discharged?"
        ),
        "family": "Rawlsian institutional fairness",
        "group": "Rawlsian institutional fairness",
    },
    # --- Family F: comparative application and provenance ---
    {
        "label": "Four ethical lenses test different objects",
        "statement": (
            "Kant tests maxims and respect, Mill tests consequences and harm, Aristotle tests "
            "character and proportion, while Rawls tests whether the underlying institution "
            "or distributive rule is fair."
        ),
        "scenario_a": (
            "A dam proposal promises aggregate electricity benefits, displaces tribal families "
            "and uses a consultation process designed without vulnerable voices. Which "
            "multi-theory method gives the most complete evaluation?"
        ),
        "scenario_b": (
            "An answer applies only cost-benefit analysis to a forced-relocation case and never "
            "tests dignity, proportionality or institutional fairness. Which comparative "
            "architecture identifies the omissions?"
        ),
        "family": "comparative application and provenance",
        "group": "comparative application and provenance",
    },
    {
        "label": "Codes of ethics and conduct only partially mirror Kant's distinction",
        "statement": (
            "Codes of ethics may address motives, values and aspirations while codes of conduct "
            "regulate external acts, but this is an administrative analogy to Kant's "
            "ethical-legal distinction rather than a complete identity."
        ),
        "scenario_a": (
            "A department's conduct code prohibits gifts, while its ethics statement asks "
            "officials to cultivate impartial motives and public-service commitment. Which "
            "qualified Kantian analogy explains the two layers?"
        ),
        "scenario_b": (
            "A trainee claims every code-of-conduct breach is legal guilt and every unworthy "
            "motive is formally punishable. Which limit of the ethics-conduct analogy corrects "
            "the claim?"
        ),
        "family": "comparative application and provenance",
        "group": "comparative application and provenance",
    },
    {
        "label": "Paper-attributed quotations require explicit provenance discipline",
        "statement": (
            "UPSC-attributed Socrates, Dalai Lama, Erik Erikson, Potter Stewart and William "
            "James quotations should be interpreted for their ethical meaning while avoiding "
            "invented primary-text citations or exaggerated authenticity claims."
        ),
        "scenario_a": (
            "A candidate cannot trace an assigned quotation to the named thinker's published "
            "work but explains its ethical meaning and writes 'as attributed in the question.' "
            "Which scholarly discipline is being followed?"
        ),
        "scenario_b": (
            "A model answer fabricates a book title and page number for the 2020 Socrates "
            "quotation to appear authoritative. Which source-handling rule has been violated?"
        ),
        "family": "comparative application and provenance",
        "group": "comparative application and provenance",
    },
    {
        "label": "AI-governance philosopher mappings are analytical inferences",
        "statement": (
            "Mapping People First to Kant, Fairness and Equity to Rawls, safety to Mill, "
            "proportionate governance to Aristotle and explainability to Socrates is an "
            "analytical inference, not an official classification."
        ),
        "scenario_a": (
            "An officer uses the India AI Governance Guidelines to compare philosophical "
            "approaches but clearly labels every thinker-link as her own analytical mapping. "
            "Which evidence practice makes the use valid?"
        ),
        "scenario_b": (
            "A presentation claims that MeitY officially classified its seven sutras under "
            "Kant, Mill, Rawls, Aristotle and Socrates. Which provenance correction is required?"
        ),
        "family": "comparative application and provenance",
        "group": "comparative application and provenance",
    },
)

PYQS = (
    {
        "year": 2018,
        "question": (
            "With regard to morality of actions, one view is that means are of paramount "
            "importance and the other view is that the ends justify the means. Which view "
            "do you think is more appropriate? Justify your answer. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2018 GS-IV Q4(b), local paper "
            "books/more_previous_papers/GENERAL-STUDIES-PAPER-IV.pdf. Primary routing is "
            "Topic 08; included here as a cross-owner Kant-Mill-Aristotle comparison. It is "
            "one isolated 10-mark, 150-word subpart."
        ),
        "answer": (
            "Neither a good end nor formally clean means alone completes moral evaluation, "
            "but constitutional public administration must give ethical and lawful means a "
            "non-negotiable priority. Kant explains why: a maxim permitting deception, "
            "coercion or discrimination cannot become moral merely because the expected "
            "outcome is beneficial, and citizens cannot be used merely as instruments for "
            "targets.\n\n"
            "Consequences nevertheless matter when choosing among permissible means. A "
            "district administration selecting between two lawful vaccination strategies "
            "should prefer the one that protects more people with less disruption. Mill "
            "therefore improves practical choice without authorising every expedient. "
            "Aristotle adds phronesis: the official must judge proportion, context and the "
            "character expressed by the action.\n\n"
            "Thus, the appropriate position is qualified means-priority: pursue legitimate "
            "public ends through lawful, truthful, proportionate and dignity-respecting means, "
            "then use consequences to select among those ethical options. Otherwise apparent "
            "success corrodes public trust and the legitimacy of the end itself."
        ),
    },
    {
        "year": 2018,
        "question": (
            "\"The true rule, in determining to embrace, or reject any thing, is not whether "
            "it has any evil in it; but whether it has more evil than good...especially of "
            "governmental policy...our best judgment of the preponderance between them is "
            "continually demanded.\" — Abraham Lincoln. What does this quotation mean to you "
            "in the present context? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official attribution and text: 2018 GS-IV Q6(a), local paper "
            "books/more_previous_papers/GENERAL-STUDIES-PAPER-IV.pdf. The routing ledger's "
            "'attribution unclear in OCR' label is erroneous: the official English text "
            "clearly names Abraham Lincoln. This isolated subpart is 10 marks and 150 words."
        ),
        "answer": (
            "Lincoln's quotation recognises that public policy usually involves mixed "
            "consequences rather than choices between perfect good and pure evil. Ethical "
            "judgment therefore requires disciplined comparison of benefits, harms, "
            "probabilities, affected groups, duration and reversibility instead of moral "
            "absolutism or political slogan.\n\n"
            "A hydroelectric project may provide clean energy and employment while displacing "
            "a tribal community and damaging ecology. Millian reasoning compares aggregate "
            "welfare, but Rawls asks whether the design protects and benefits the least "
            "advantaged. Kant prevents the displaced from being treated merely as compensable "
            "costs, while Aristotle requires proportionate, context-sensitive implementation.\n\n"
            "The quotation does not mean that every right can be traded for a larger numerical "
            "gain. Constitutional rights, informed consent, rehabilitation and environmental "
            "limits remain ethical floors. The practical lesson is to choose the least harmful "
            "feasible option through evidence, consultation and transparent reasons, then "
            "monitor consequences and revise policy when the balance changes."
        ),
    },
    {
        "year": 2019,
        "question": (
            "\"An unexamined life is not worth living.\" — Socrates. What does this quotation "
            "mean to you? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2019 GS-IV Q6(a), local paper "
            "books/more_previous_papers/QP-CSM19-GeneralStudies-IV.pdf. Cite the textual source "
            "as Plato, Apology 38a: Socrates as portrayed by Plato. Socrates left no writings; "
            "do not present the line as a Socrates-authored text. Isolated subpart: 10 marks, "
            "150 words."
        ),
        "answer": (
            "The quotation makes reflective scrutiny central to a worthwhile moral life. "
            "Examination means identifying one's assumptions, asking whether reasons are "
            "consistent, inviting challenge and correcting conduct when evidence exposes bias. "
            "For a civil servant, it converts conscience from a private feeling into "
            "accountable reason-giving.\n\n"
            "A district magistrate who initially attributes school absenteeism to parental "
            "indifference should test that belief through field visits. If transport, unsafe "
            "routes and seasonal work explain the pattern, self-examination requires policy "
            "revision rather than defensive persistence. The same discipline applies to "
            "conflicts of interest, prejudice in recruitment and habitual deference to senior "
            "orders.\n\n"
            "Introspection alone is insufficient because people can rationalise self-interest. "
            "Peer review, recorded reasons, transparency and citizen consultation provide "
            "external correction. Textually, the line should be cited as Socrates speaking in "
            "Plato's Apology 38a, since Socrates wrote nothing. Its present administrative "
            "meaning is continuous ethical learning before and after exercising power."
        ),
    },
    {
        "year": 2020,
        "question": (
            "Distinguish between laws and rules. Discuss the role of ethics in formulating "
            "them. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2020 GS-IV Q4(a), local paper "
            "books/more_previous_papers/Gen_St_P4.pdf. Primary routing is Topic 10; included "
            "here because it directly supports Kant's legal-ethical distinction. This is one "
            "isolated 10-mark, 150-word subpart."
        ),
        "answer": (
            "Laws are publicly enacted, generally binding norms backed by state authority and "
            "formal sanctions. Rules are more specific operational prescriptions framed under "
            "law or within institutions to guide recurring conduct. Both regulate external "
            "behaviour, but legality alone does not establish moral legitimacy.\n\n"
            "Ethics shapes their purpose, content and procedure. Dignity prevents a welfare "
            "rule from humiliating beneficiaries; equality rejects discriminatory eligibility; "
            "proportionality limits excessive penalties; transparency and participation make "
            "rule-making accountable. Kant's distinction is useful: law can demand outward "
            "compliance, while ethics asks whether the underlying maxim respects persons and "
            "could be universally justified.\n\n"
            "For example, a lawful biometric rule may still be unethical if it excludes elderly "
            "citizens without alternatives. Ethics would require exception channels, data "
            "protection and grievance redress. Conversely, ethical aspirations require clear "
            "rules to avoid arbitrary discretion. Good governance therefore joins lawful "
            "authority with ethically defensible objectives, fair procedures and periodic "
            "review of actual consequences."
        ),
    },
    {
        "year": 2020,
        "question": (
            "\"A system of morality which is based on relative emotional values is a mere "
            "illusion, a thoroughly vulgar conception which has nothing sound in it and "
            "nothing true.\" — Socrates. What does this quotation mean to you? "
            "(Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2020 GS-IV Q6(c), local paper "
            "books/more_previous_papers/Gen_St_P4.pdf. No matching sentence was identified in "
            "the searched classical Platonic, Xenophontic or academic sources. Treat it as "
            "'attributed to Socrates in the paper,' not as a verified primary quotation. "
            "Isolated subpart: 10 marks, 150 words."
        ),
        "answer": (
            "The quotation warns that volatile feeling, personal preference or group sentiment "
            "cannot by themselves provide a stable moral standard. Public decisions need "
            "reasons that can be examined for consistency, factual accuracy, impartiality and "
            "generalisability. Otherwise prejudice may be relabelled as sincere emotion.\n\n"
            "A district administration should not prohibit an inter-community marriage merely "
            "because a local majority feels offended. Mill distinguishes offence from harm, "
            "while Kant asks whether the discriminatory maxim could be universalised. Socratic "
            "questioning exposes whether the asserted value survives rational scrutiny.\n\n"
            "The statement should not be read as making emotion ethically worthless. Empathy "
            "reveals suffering, remorse can motivate correction and compassion improves "
            "implementation. Emotion supplies morally relevant information, but reason and "
            "public justification must evaluate it. Provenance also requires caution: the exact "
            "sentence has not been located in classical sources. A responsible answer should "
            "therefore discuss the idea 'as attributed by the paper' rather than inventing a "
            "Platonic dialogue or page reference."
        ),
    },
    {
        "year": 2021,
        "question": (
            "\"We can never obtain peace in the outer world until and unless we obtain peace "
            "within ourselves.\" — Dalai Lama. What does this quotation mean to you? "
            "(Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2021 GS-IV Q3(b), local paper "
            "books/more_previous_papers/QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf. The sentiment "
            "is widely attributed to the Dalai Lama, but the exact UPSC wording was not traced "
            "to a verified primary book, speech or transcript. Isolated subpart: 10 marks, "
            "150 words."
        ),
        "answer": (
            "The quotation links external peace with internal emotional regulation. A person "
            "dominated by anger, fear, ego or prejudice carries those conflicts into public "
            "relationships; self-awareness and composure create the psychological space needed "
            "for listening, impartiality and non-violent problem-solving.\n\n"
            "For a district magistrate mediating communal tension, inner peace means recognising "
            "personal anxiety, resisting retaliatory language, hearing each community and "
            "communicating calmly under pressure. It improves credibility and prevents the "
            "official from escalating the conflict through impulsive action. Aristotle would "
            "describe this as habituated temperance supported by practical wisdom.\n\n"
            "Yet internal calm is only a precondition. Peace also requires justice, protection "
            "of rights, action against offenders and correction of structural grievances. "
            "Composure without substantive remedy can preserve an unjust status quo. The "
            "provenance should likewise be stated carefully: the exact wording is widely "
            "attributed but no primary source was verified. The administrative lesson is "
            "self-mastery joined with fair institutional action."
        ),
    },
    {
        "year": 2021,
        "question": (
            "\"Life doesn't make any sense without interdependence. We need each other, and "
            "the sooner we learn that, it is better for us all.\" — Erik Erikson. What does "
            "this quotation mean to you? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2021 GS-IV Q3(c), local paper "
            "books/more_previous_papers/QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf. The canonical "
            "owner and routing ledger incorrectly render this as 'learning and acceptance'; "
            "the actual demand is interdependence and mutual need. No primary Erikson source "
            "for the exact sentence was verified. Isolated subpart: 10 marks, 150 words."
        ),
        "answer": (
            "The quotation rejects the fiction that individuals or institutions flourish in "
            "isolation. Human development depends on relationships of care, recognition, "
            "cooperation and reciprocal responsibility. In administration, interdependence "
            "means that authority, expertise and implementation are distributed across "
            "citizens, departments and levels of government.\n\n"
            "Disaster relief illustrates this clearly. A district collector needs local "
            "communities for information, health workers for triage, police for access, civil "
            "society for last-mile support and neighbouring districts for logistics. Treating "
            "beneficiaries merely as passive recipients wastes local knowledge and weakens "
            "trust. Cooperative federalism and participatory governance are institutional "
            "expressions of the same insight.\n\n"
            "Interdependence does not erase personal accountability; each actor remains "
            "responsible for assigned duties. Nor should the answer be diverted into 'learning "
            "and acceptance,' which is not the printed quotation. Since the exact sentence has "
            "not been traced to a primary Erikson text, it should be described as paper-"
            "attributed while its relational ethical meaning is analysed."
        ),
    },
    {
        "year": 2022,
        "question": (
            "\"Ethics is knowing the difference between what you have the right to do and "
            "what is right to do.\" — Potter Stewart. What does this quotation mean to you? "
            "(Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2022 GS-IV Q3(a), local paper "
            "books/more_previous_papers/QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf. Primary "
            "routing is Topic 02; included for the legal-ethical gap. No primary judicial "
            "opinion, speech or writing by Potter Stewart containing the exact line was "
            "verified. Isolated subpart: 10 marks, 150 words."
        ),
        "answer": (
            "The quotation distinguishes legal permission from ethical justification. Rights "
            "protect a legitimate sphere of choice, but exercising a right can still be "
            "selfish, disproportionate or contrary to the responsibilities attached to public "
            "office. Ethics asks what ought to be done, not merely what sanctions can be "
            "avoided.\n\n"
            "A senior official may have formal discretion to choose among eligible project "
            "sites, yet selecting land near a relative's business violates impartiality even "
            "before a specific anti-corruption offence is proved. Similarly, an authority may "
            "legally withhold optional information but should disclose it when citizens need it "
            "to protect health or livelihood. Kant's humanity formula and the fiduciary nature "
            "of public office explain the higher standard.\n\n"
            "Ethics cannot, however, authorise officials to ignore law according to personal "
            "preference. Constitutional values, recorded reasons and review must discipline the "
            "judgment. The sentence is widely attributed to Potter Stewart, but no primary "
            "source was verified; answer the proposition without inventing a case citation."
        ),
    },
    {
        "year": 2022,
        "question": (
            "\"Judge your success by what you had to give up in order to get it.\" — Dalai "
            "Lama. What does this quotation mean to you? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2022 GS-IV Q3(c), local paper "
            "books/more_previous_papers/QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf. Primary "
            "routing is Topic 02. The line circulated within the falsely attributed Dalai Lama "
            "'Instructions for Life' chain-email tradition; no verified primary Dalai Lama "
            "source was identified. Isolated subpart: 10 marks, 150 words."
        ),
        "answer": (
            "The quotation proposes an ethical rather than merely numerical measure of success. "
            "Achievement should be assessed not only by targets reached but also by the values, "
            "relationships, rights and long-term capacities preserved or sacrificed during the "
            "process.\n\n"
            "A district may clear an infrastructure corridor before deadline by suppressing "
            "hearings, underpaying displaced families and intimidating dissent. The output "
            "indicator records success, but Kantian dignity, Rawlsian fairness and procedural "
            "justice reveal moral failure. Conversely, giving up personal comfort, popularity "
            "or promotion to defend lawful rehabilitation may enhance the ethical quality of "
            "the achievement.\n\n"
            "Sacrifice itself is not automatically noble: surrendering health, family duties "
            "or public resources for vanity can be irresponsible. The relevant test is what "
            "was sacrificed, whose interests bore the cost and whether the sacrifice was "
            "necessary and proportionate. Attribution also needs caution: the saying is linked "
            "to a misattributed chain-email list, not a verified Dalai Lama text. Use it as a "
            "paper-attributed ethical proposition."
        ),
    },
    {
        "year": 2024,
        "question": (
            "\"In law, a man is guilty when he violates the rights of others. In ethics, he "
            "is guilty if he only thinks of doing so.\" — Immanuel Kant. What does this "
            "quotation convey to you in the present context? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2024 GS-IV Q3(c), local paper "
            "books/mains/05 UPSC 2024 Paper-IV_Final 1.pdf. Closely adapted from Kant, "
            "Lectures on Ethics, trans. Louis Infield (1930), section 'Innocence,' pp. 212-13: "
            "'harboured the thought of doing it.' The edition reconstructs lectures from "
            "student notebooks; it is not a sentence from a Kant-published ethical treatise. "
            "Isolated subpart: 10 marks, 150 words."
        ),
        "answer": (
            "The quotation distinguishes the external threshold of legal liability from the "
            "deeper ethical appraisal of maxims, intentions and cultivated dispositions. Law "
            "normally requires an act, attempt or legally cognisable violation; ethics can "
            "condemn a settled intention even when circumstances prevent its execution.\n\n"
            "An officer who resolves to favour a contractor has already abandoned impartiality "
            "although cancellation of the tender may prevent criminal loss. A code of ethics "
            "therefore addresses integrity, motive and conflict disclosure beyond the completed "
            "acts prohibited by a conduct code. This reflects Kant's broader distinction "
            "between acting from duty and merely conforming outwardly to duty.\n\n"
            "The statement must not become a doctrine of guilt for intrusive or passing "
            "thoughts. Infield's reconstructed lecture says 'harboured the thought' and then "
            "discusses impure dispositions, implying endorsement or cultivation of wrongful "
            "intent. Provenance should also be precise: UPSC modernises a passage from "
            "student-note-based Lectures on Ethics, not the Groundwork. Ethical self-scrutiny "
            "supplements, but does not replace, legal due process."
        ),
    },
    {
        "year": 2025,
        "question": (
            "\"The greatest discovery of my generation is that a human being can alter his "
            "life by altering his attitudes.\" — William James. What does this quotation "
            "convey to you in the present context? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact official text: 2025 GS-IV Q3(b), local paper "
            "books/mains/UPSC Mains 2025 GS Paper 4.pdf. The exact sentence has not been traced "
            "to William James's works. Norman Vincent Peale's The Power of Positive Thinking "
            "(1952) was an important popularising source for the James attribution. Treat it "
            "as paper-attributed. Isolated subpart: 10 marks, 150 words."
        ),
        "answer": (
            "The quotation emphasises that attitude influences perception, persistence and the "
            "range of possibilities a person is prepared to attempt. A constructive attitude "
            "does not deny difficulty; it converts setbacks into information, preserves agency "
            "and supports ethical action under pressure.\n\n"
            "A newly posted officer facing entrenched malnutrition can either treat failure as "
            "proof that change is impossible or adopt a learning orientation: consult frontline "
            "workers, revise delivery timings, track exclusions and build cooperation. The "
            "changed attitude alters behaviour and can therefore alter institutional outcomes. "
            "Socratic examination prevents optimism from becoming self-deception, while "
            "Aristotelian habituation turns the orientation into stable practice.\n\n"
            "Attitude alone cannot remove poverty, discrimination, inadequate budgets or "
            "structural incentives. Positive-thinking rhetoric becomes unjust when it blames "
            "victims for conditions beyond their control. Personal agency must be paired with "
            "institutional reform and material support. The exact wording is also unverified in "
            "James's corpus and was popularised through later self-help literature; answer it "
            "as attributed by UPSC rather than fabricating a James citation."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Explain the ethical significance of Kant's distinction between legal guilt and "
            "ethical guilt for contemporary public administration."
        ),
        "answer": (
            "Kant's distinction shows that legality is an ethical floor, not the complete "
            "measure of public integrity. Law ordinarily addresses externally manifested acts, "
            "attempts and violations proved through due process. Ethical evaluation also asks "
            "what maxim, motive and cultivated disposition guided the official.\n\n"
            "An officer who intends to favour a contractor but is prevented by cancellation "
            "may escape criminal liability, yet has abandoned impartiality and the good will. "
            "This explains why codes of ethics require conflict disclosure, objectivity and "
            "public-service commitment beyond the completed acts prohibited by conduct rules.\n\n"
            "The 2024 UPSC wording needs a careful limit. Infield's 1930 Lectures on Ethics, "
            "reconstructed from student notebooks, refers to harbouring a wrongful thought and "
            "impure disposition, not involuntary mental events. Ethics should promote "
            "self-scrutiny and correction, not thought-policing. Thus ethical accountability "
            "supplements legal liability by addressing intention, while formal punishment must "
            "remain governed by law and evidence."
        ),
    },
    {
        "marks": 10,
        "question": (
            "How do Aristotle's Golden Mean and phronesis improve proportionality in "
            "administrative decision-making?"
        ),
        "answer": (
            "The Golden Mean identifies virtue between the vices of excess and deficiency, "
            "while phronesis is the practical wisdom needed to locate that mean in a particular "
            "case. The mean is relative to circumstances, not an arithmetic compromise.\n\n"
            "In crowd control, excessive force shows rashness and complete inaction may show "
            "cowardice or neglect. A practically wise magistrate assesses intelligence, crowd "
            "behaviour, vulnerable persons and available alternatives, then chooses targeted "
            "restrictions and minimum necessary force. Repeated training and reflection turn "
            "such judgment into stable professional virtue.\n\n"
            "Aristotle does not imply that every act has a moderate version: bribery or torture "
            "cannot become virtuous by reducing their amount. Nor may phronesis become "
            "unreviewable personal intuition. Constitutional rights, statutory limits, evidence "
            "and recorded reasons supply external discipline. Together, the Mean and phronesis "
            "make proportionality a character-informed, context-sensitive judgment bounded by "
            "law rather than a mechanical midpoint."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Can Mill's harm principle provide an adequate ethical constraint on utilitarian "
            "public policy? Discuss with suitable Indian administrative examples."
        ),
        "answer": (
            "Utilitarian policy seeks the greatest aggregate welfare, but aggregation can "
            "sacrifice minorities when their losses are outweighed numerically. Mill's harm "
            "principle supplies a liberal constraint: coercion of a competent adult is justified "
            "principally to prevent harm to others, not merely offence, moral dislike or "
            "paternalistic majority preference.\n\n"
            "During an epidemic, isolation of an infectious person can be justified because "
            "conduct risks harm to others. A blanket system of permanent location surveillance "
            "for all citizens, however, must show necessity, effectiveness and absence of less "
            "restrictive alternatives. Similarly, offensive but peaceful expression should not "
            "be prohibited merely because a majority disapproves. The burden of proof rests on "
            "coercion.\n\n"
            "The principle is not fully adequate. Many actions create indirect spillovers, and "
            "the meaning, probability and threshold of harm are disputed. Mill also framed its "
            "scope around competent adults, requiring separate protection for children and "
            "persons lacking capacity. Rule-utilitarian support for due process and stable "
            "rights strengthens the constraint because arbitrary coercion damages long-term "
            "trust.\n\n"
            "Therefore the harm principle is a strong presumption for liberty, not a complete "
            "algorithm. Indian administration should combine demonstrable harm, proportionality, "
            "least-restrictive means, rights review and periodic reassessment before coercing."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Apply Rawls's lexical priorities to evaluate the design of a targeted welfare "
            "scheme in India."
        ),
        "answer": (
            "Rawls evaluates the basic structure through principles chosen in an original "
            "position where parties do not know their class, identity, talents or eventual "
            "social position. A welfare scheme should therefore be designed as if its authors "
            "might become its most vulnerable applicants.\n\n"
            "First, equal basic liberties have lexical priority. Benefits cannot be conditioned "
            "on surrendering association, expression, privacy or due process merely to improve "
            "delivery efficiency. Second, fair equality of opportunity requires genuine access, "
            "not only formally identical eligibility. Online-only applications, inaccessible "
            "centres or documents unavailable to migrant workers defeat fair opportunity even "
            "when the rules appear neutral.\n\n"
            "Only after these conditions does the difference principle operate. Targeting, "
            "administrative inequality or additional expenditure is justified when it "
            "materially improves the position of the least advantaged. Doorstep authentication "
            "for elderly persons or higher delivery costs in remote tribal areas can therefore "
            "be fair.\n\n"
            "The veil remains a heuristic, not a literal policymaking procedure, and real design "
            "still requires data, fiscal feasibility and grievance evidence. A Rawlsian scheme "
            "protects liberties, equalises meaningful access and places the justificatory burden "
            "on exclusions and inequalities."
        ),
    },
    {
        "marks": 20,
        "question": (
            "A large infrastructure project promises substantial public benefits but will "
            "displace a small tribal community. Evaluate the decision through Kant, Mill, "
            "Aristotle and Rawls, and give a reasoned administrative verdict."
        ),
        "answer": (
            "The project creates a genuine conflict between aggregate development and the "
            "rights of a concentrated vulnerable group. A complete decision should test the "
            "act, consequences, administrative character and underlying institutional rule.\n\n"
            "Mill asks whether long-term electricity, employment and connectivity benefits "
            "exceed ecological, cultural and livelihood harms. The calculation must include "
            "distribution, probability and irreversible loss, not only total monetary value. "
            "His harm principle also places the burden on coercive displacement and requires "
            "less restrictive alternatives.\n\n"
            "Kant prohibits treating the community merely as an instrument for benefits enjoyed "
            "elsewhere. Full information, meaningful consultation, consent where legally "
            "required, fair rehabilitation and respect for cultural agency are dignity-based "
            "constraints, not costs that disappear inside a net-benefit figure.\n\n"
            "Aristotle's phronesis rejects both automatic project cancellation and development "
            "at any price. A prudent administrator examines alternative alignments, project "
            "scale, ecological evidence, timing and proportionate mitigation. Courage may be "
            "needed to resist both populist obstruction and powerful commercial pressure.\n\n"
            "Rawls asks whether the project rule would be accepted without knowing whether one "
            "would be an urban beneficiary or a displaced tribal resident. Inequality is "
            "defensible only if the least advantaged are genuinely benefited, with fair "
            "opportunity and basic liberties already protected.\n\n"
            "The verdict is conditional approval only after independent alternatives assessment, "
            "rights-compliant consultation, livelihood-plus-cultural rehabilitation, benefit "
            "sharing, transparent monitoring and accessible appeal. If serious irreversible "
            "harm cannot be mitigated, the project should be redesigned or rejected."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Philosophically audit India's contemporary AI-governance framework through Kant, "
            "Mill, Rawls, Aristotle and Socrates."
        ),
        "answer": (
            "India's AI Governance Guidelines identify seven technology-agnostic sutras: Trust, "
            "People First, Innovation over Restraint, Fairness and Equity, Accountability, "
            "Understandable by Design, and Safety, Resilience and Sustainability. Their "
            "recommendations span enablement, regulation and oversight. A February 2026 PIB "
            "brief presents M.A.N.A.V. as Moral and Ethical Systems, Accountable Governance, "
            "National Sovereignty, Accessible and Inclusive AI, and Valid and Legitimate "
            "Systems, framing AI around human aspirations, ethics and dignity.\n\n"
            "The following philosopher-links are analytical inferences, not official "
            "classifications. Kant supports People First: automated decisions must respect "
            "persons as ends, preserve human agency and permit challenge rather than using "
            "citizens merely as data points. Rawls illuminates Fairness and Equity: training "
            "data, access and welfare algorithms should be tested from the standpoint of those "
            "most vulnerable to exclusion.\n\n"
            "Mill links innovation to harm prevention. Regulation should address demonstrable "
            "risk while avoiding blanket restraint, and use proportionate, least-restrictive "
            "safeguards. Aristotle's phronesis supports risk-sensitive governance rather than "
            "one rigid rule across health, education and entertainment. Socratic examination "
            "supports Understandable by Design, reason-giving, contestability and continuous "
            "testing of assumptions.\n\n"
            "The framework's ethical strength will depend on implementation: assigned "
            "accountability, accessible explanations, grievance redress, human oversight, "
            "bias testing and evidence of inclusion. Principles alone do not prove ethical "
            "outcomes. The appropriate verdict is innovation under human dignity, fairness, "
            "demonstrable safety and publicly reviewable reasons. Independent audit and "
            "effective remedies are necessary when automated decisions deny public benefits "
            "or reproduce exclusion."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": "1. Four-lens decision architecture",
        "structural_type": "decision-matrix",
        "nodes": (
            "State the dilemma and identify the genuinely competing values.",
            "Kant test one: formulate and universalise the proposed maxim.",
            "Kant test two: ensure every affected person is treated as an end.",
            "Mill test one: compare benefits, harms, probability, duration and distribution.",
            "Mill test two: ask whether coercion prevents harm or merely enforces preference.",
            "Aristotle test: identify the virtues, extremes and context-sensitive proportion.",
            "Rawls test: examine the underlying rule from the least-advantaged position.",
            "Map convergence and justify a transparent tie-break where theories diverge.",
        ),
        "verdict": "No single lens is automatically decisive; name convergence and defend the tie-break.",
        "answer_use": "Use as the opening framework for multi-value dilemmas and Section B case studies.",
    },
    {
        "title": "2. Socratic examination loop",
        "structural_type": "process-flow",
        "nodes": (
            "Pause before discretion turns an inherited assumption into official action.",
            "Surface the factual, moral and identity-based assumptions behind the first view.",
            "Ask what reasons and evidence support each assumption.",
            "Test whether the reasons contradict another accepted public principle.",
            "Invite an affected citizen or colleague to supply a counter-view.",
            "Identify incentives, ego, prejudice and hierarchy that may distort judgment.",
            "Revise the decision when reasons fail rather than defending sunk authority.",
            "Record the final reasons so reflection becomes publicly reviewable.",
        ),
        "verdict": "Socratic reflection becomes administrative ethics only when it produces revisable reasons.",
        "answer_use": "Use for bias, conscience, discretion, consultation and ethical-leadership answers.",
    },
    {
        "title": "3. Plato's soul-city harmony",
        "structural_type": "parallel-hierarchy",
        "nodes": (
            "Reason identifies the good and should govern the individual.",
            "Spirit supplies courage and disciplined support to rational judgment.",
            "Appetite supplies necessary desire but must not capture decision-making.",
            "Inner justice exists when the three parts perform ordered functions.",
            "Rulers deliberate for the common good rather than private appetite.",
            "Auxiliaries protect the polity under rational and lawful direction.",
            "Producers sustain material life without usurping every public function.",
            "Modern use requires participation, rights and checks against elite domination.",
        ),
        "verdict": "Plato supplies an order-and-competence analogy, not a licence for unaccountable technocracy.",
        "answer_use": "Use for Plato, institutional role clarity, self-mastery and merit-with-accountability.",
    },
    {
        "title": "4. Aristotle's virtue and proportionality map",
        "structural_type": "balance-scale",
        "nodes": (
            "Human telos directs ethics toward eudaimonia or whole-life flourishing.",
            "Virtue is a stable disposition, not a single conspicuous good act.",
            "Habituation forms reliable courage, justice, temperance and generosity.",
            "Deficiency marks one vice, such as cowardice or negligent inaction.",
            "Excess marks the opposite vice, such as rashness or punitive over-reaction.",
            "The mean is relative to circumstances, never a fixed numerical midpoint.",
            "Phronesis identifies the fitting action through trained practical judgment.",
            "Law, evidence and review prevent practical wisdom becoming arbitrary discretion.",
        ),
        "verdict": "The virtuous mean is reasoned proportion bounded by law, not compromise at any cost.",
        "answer_use": "Use for proportionality, crowd control, crisis judgment and virtue-ethics questions.",
    },
    {
        "title": "5. Kantian Categorical Imperative decision test",
        "structural_type": "decision-tree",
        "nodes": (
            "State the maxim describing what the official proposes and why.",
            "Imagine the maxim operating as a universal rule for all officials.",
            "Test contradiction in conception: would universal practice destroy the institution?",
            "Test contradiction in will: could a rational person accept that universal world?",
            "Apply the humanity formula to every affected person's agency and dignity.",
            "Reject manipulation, coercion or concealment that uses persons merely as means.",
            "Distinguish acting from duty from strategic outward conformity.",
            "Choose the duty-consistent option and state consequences only as implementation factors.",
        ),
        "verdict": "Favourable consequences cannot cure an impermissible maxim or instrumental treatment.",
        "answer_use": "Use for honesty, confidentiality, consent, corruption and rights-based dilemmas.",
    },
    {
        "title": "6. Kant 2024 quotation provenance ladder",
        "structural_type": "evidence-chain",
        "nodes": (
            "UPSC 2024 Q3(c) prints the law-versus-ethics guilt formulation.",
            "The wording is absent from Kant's published Groundwork and mature ethical treatises.",
            "Louis Infield's 1930 Lectures on Ethics contains the closely matching passage.",
            "The passage appears under 'Innocence' on printed pages 212-13.",
            "The German reconstruction used Brauer's student notebook as its principal base.",
            "Kutzner and Mrongovius notebooks were used for collation and correction.",
            "UPSC modernises 'harboured the thought' into 'only thinks of doing so.'",
            "Answer the proposition while identifying it as a student-note-based adapted passage.",
        ),
        "verdict": "The idea is substantively Kantian, but the printed UPSC sentence is textually adapted.",
        "answer_use": "Use as the provenance box and opening qualification for the 2024 PYQ.",
    },
    {
        "title": "7. Utilitarian policy calculus",
        "structural_type": "weighted-flow",
        "nodes": (
            "Identify every affected group, including diffuse and politically weak interests.",
            "List direct, indirect and opportunity benefits rather than one headline output.",
            "List physical, economic, dignity, ecological and institutional harms.",
            "Estimate probability and uncertainty instead of treating projections as certainties.",
            "Separate immediate effects from cumulative and intergenerational consequences.",
            "Test distribution because aggregate gain may conceal concentrated severe loss.",
            "Evaluate both the particular act and the consequences of its general rule.",
            "Apply rights and harm safeguards before declaring the largest total decisive.",
        ),
        "verdict": "Aggregation is informative only when uncertainty, distribution and liberty are visible.",
        "answer_use": "Use for cost-benefit policy, triage, infrastructure and resource-allocation answers.",
    },
    {
        "title": "8. Mill's harm-principle gate",
        "structural_type": "funnel",
        "nodes": (
            "Confirm whether the person is a competent adult exercising meaningful agency.",
            "Ask whether the conduct is substantially self-regarding.",
            "Identify concrete other-regarding effects rather than vague social dislike.",
            "Separate demonstrable harm from offence, immorality claims and paternalism.",
            "Place the evidentiary burden for coercion on the public authority.",
            "Select the least restrictive effective measure where harm is established.",
            "Protect minority individuality against majoritarian social pressure.",
            "Review spillovers and evidence because the boundary of harm can change.",
        ),
        "verdict": "Liberty is presumed; coercion requires demonstrable harm and proportionate means.",
        "answer_use": "Use for speech, lifestyle, surveillance, public health and paternalism questions.",
    },
    {
        "title": "9. Rawlsian lexical-priority staircase",
        "structural_type": "priority-staircase",
        "nodes": (
            "Begin with persons as free and equal moral agents.",
            "Secure a fully adequate equal scheme of basic liberties.",
            "Refuse to trade those liberties for income or administrative efficiency.",
            "Next secure fair equality of opportunity for offices and prospects.",
            "Test substantive access, not merely formal absence of discrimination.",
            "Give fair opportunity priority over the difference principle.",
            "Permit inequality only when it benefits the least advantaged.",
            "Treat efficiency as a separate feasibility consideration constrained by justice.",
        ),
        "verdict": "The lexical order is liberty, fair opportunity, then the difference principle.",
        "answer_use": "Use to prevent the most common Rawls sequencing error in welfare answers.",
    },
    {
        "title": "10. Veil-of-ignorance policy test",
        "structural_type": "policy-loop",
        "nodes": (
            "Define the rule affecting society's basic institutions and opportunities.",
            "Bracket knowledge of the designer's class, identity, talent and eventual position.",
            "Identify the primary goods distributed by the proposed rule.",
            "Reason from the possibility of occupying any affected social position.",
            "Test access and burden from the most vulnerable plausible standpoint.",
            "Compare feasible alternatives rather than declaring one abstract design perfect.",
            "Use reflective equilibrium to revise both principles and considered judgments.",
            "Publish the fairness rationale, exclusions, evidence and review mechanism.",
        ),
        "verdict": "The veil is a fairness heuristic for institutional design, not literal ignorance.",
        "answer_use": "Use for subsidy, reservation-adjacent, health, education and algorithmic eligibility.",
    },
    {
        "title": "11. Displacement-project four-lens comparison",
        "structural_type": "four-column-matrix",
        "nodes": (
            "State the public benefits claimed for the infrastructure project.",
            "Identify concentrated livelihood, cultural and ecological costs to the community.",
            "Kant requires dignity, agency, consultation and non-instrumental treatment.",
            "Mill compares comprehensive long-term welfare rather than headline monetary output.",
            "Mill's harm principle places the burden on coercive displacement.",
            "Aristotle tests alternatives, proportion and the administrator's practical wisdom.",
            "Rawls asks whether the design genuinely benefits the least advantaged.",
            "Reach conditional approval, redesign or rejection with enforceable safeguards.",
        ),
        "verdict": "Aggregate gain cannot substitute for dignity, proportionality and worst-off protection.",
        "answer_use": "Use for dams, mining, border infrastructure and development-versus-rights dilemmas.",
    },
    {
        "title": "12. Provenance-to-AI-governance bridge",
        "structural_type": "audit-chain",
        "nodes": (
            "Begin with the exact official paper or government-document wording.",
            "Search for a primary text before assigning book, speech or page.",
            "Classify the material as direct, adapted, widely attributed or unverified.",
            "Answer the ethical proposition without fabricating authority.",
            "Map People First to Kant only as an analytical inference.",
            "Map Fairness and Equity to Rawls only as an analytical inference.",
            "Map safety, proportion and understandability to Mill, Aristotle and Socrates cautiously.",
            "End with accountability, human oversight and publicly reviewable reasons.",
        ),
        "verdict": "Source honesty and explicit inference labels make current-affairs application defensible.",
        "answer_use": "Use for quotation answers and the India AI Governance Guidelines current anchor.",
    },
)

CURRENT_ANCHOR = {
    "title": "India AI Governance Guidelines and the M.A.N.A.V. framework",
    "verified_facts": (
        "The India AI Governance Guidelines identify seven technology-agnostic sutras: "
        "Trust, People First, Innovation over Restraint, Fairness & Equity, Accountability, "
        "Understandable by Design, and Safety, Resilience & Sustainability.",
        "The India AI Governance Guidelines organise recommendations across enablement, "
        "regulation and oversight.",
        "A Press Information Bureau brief dated 19 February 2026 states that M.A.N.A.V. "
        "comprises Moral and Ethical Systems, Accountable Governance, National Sovereignty, "
        "Accessible and Inclusive AI, and Valid and Legitimate Systems.",
        "The 19 February 2026 PIB brief frames artificial intelligence around human "
        "aspirations, ethics and dignity.",
    ),
    "administrative_link": (
        "Analytical mapping only, not official classification: Kant can illuminate People "
        "First, human agency and dignity; Rawls can illuminate Fairness & Equity and the "
        "position of excluded citizens; Mill can illuminate safety, demonstrable harm and "
        "proportionate restraint; Aristotle can illuminate context-sensitive risk governance; "
        "and Socrates can illuminate Understandable by Design, reason-giving and scrutiny. "
        "Use the official sutras and M.A.N.A.V. components as facts, then label each "
        "philosopher-link explicitly as inference."
    ),
    "limit": (
        "Neither official document classifies its principles under Kant, Mill, Rawls, "
        "Aristotle or Socrates. Do not claim that the documents verify implementation "
        "outcomes, eliminate algorithmic bias or mandate any specific philosopher's theory. "
        "The anchor supports a normative comparison, not proof that ethical principles have "
        "been operationalised successfully in every AI system."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://impact.indiaai.gov.in/IndiaAI_Governance_Guidelines.pdf",
    "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026219796801.pdf",
)

SOURCE_CAVEAT = (
    "Use the local Topic 07 Basic and Advanced owners as the controlling curricular source, "
    "with the audited official local GS-IV papers for exact PYQ wording. Socrates wrote no "
    "texts: 'The unexamined life is not worth living' should be cited as Socrates speaking "
    "in Plato's Apology 38a, not as a Socrates-authored work. 'Know thyself' is a Delphic "
    "maxim older than Socrates; describe Socratic use or reinterpretation, not Socratic "
    "authorship. 'Virtue is knowledge' is standard shorthand for Socratic intellectualism "
    "transmitted through Plato, Xenophon and later testimony. The 2020 GS-IV sentence about "
    "a morality based on 'relative emotional values' was not located in the searched "
    "classical sources; call it 'attributed to Socrates in the paper' and never invent a "
    "dialogue citation. The 2024 Kant quotation is closely adapted from Lectures on Ethics, "
    "translated by Louis Infield (1930), section 'Innocence,' printed pages 212-13. That "
    "edition is a reconstruction based principally on Brauer's student notebook, checked "
    "against Kutzner and Mrongovius notebooks, not a Kant-published ethical treatise. Its "
    "wording is 'harboured the thought of doing it,' so distinguish endorsed intention or "
    "impure disposition from involuntary passing thoughts. The exact 2021 Dalai Lama "
    "inner-peace wording was not traced to a verified primary book, speech or transcript; "
    "treat it as widely/paper attributed. The 2022 Dalai Lama success-and-sacrifice line "
    "circulated in the falsely attributed 'Instructions for Life' chain-email tradition; "
    "do not present it as a verified Dalai Lama text. The 2021 Erik Erikson quotation is "
    "about interdependence and mutual need, not 'learning and acceptance'; no primary source "
    "for the exact sentence was verified. The Potter Stewart legality-versus-ethics line is "
    "widely attributed, but no primary judicial opinion, speech or writing containing it was "
    "verified. The 2025 William James sentence was not traced to James's corpus; Norman "
    "Vincent Peale's The Power of Positive Thinking (1952) was an important popularising "
    "source for the James attribution. The 2018 governmental-policy quotation is clearly "
    "attributed to Abraham Lincoln in the official English paper; the routing ledger's "
    "'attribution unclear in OCR' description is incorrect. Where provenance is uncertain, "
    "answer the proposition, say 'as attributed in the question,' and never fabricate a "
    "primary source, book title or page."
)

REGISTER_SUPPLEMENT = (
    "Rapid recall: Western ethics supplies four distinct lenses. KANT asks whether the maxim "
    "is universal and whether every person is treated as an end; MILL asks about aggregate "
    "welfare and whether coercion prevents harm to others; ARISTOTLE asks what a person of "
    "excellent character and practical wisdom would do proportionately; RAWLS asks whether "
    "the underlying institution is fair from every social position. SOCRATES: examined life "
    "as assumption-testing, contradiction-checking and anti-bias reason-giving; virtue/"
    "knowledge link is transmitted doctrine; Socrates wrote nothing. 'Know thyself' is "
    "Delphic. PLATO: justice is harmony and each part doing its proper work; tripartite soul "
    "(reason, spirit, appetite); philosopher-ruler is an expertise/public-good analogy, not "
    "modern unaccountable technocracy. ARISTOTLE: eudaimonia = whole-life flourishing, not "
    "temporary pleasure; virtue = habituated disposition; Golden Mean = context-relative "
    "proportion between excess and deficiency, not arithmetic midpoint; intrinsically wrong "
    "acts have no virtuous mean; phronesis = practical wisdom bounded administratively by "
    "law, evidence and review. KANT: good will; acting from duty versus merely in conformity "
    "with duty; universal-law and humanity formulations; persons never merely means. 2024 "
    "Q3(c): law ordinarily reaches external violation, ethics also judges harboured wrongful "
    "intention/disposition. Provenance: Infield 1930 Lectures on Ethics, 'Innocence,' pp. "
    "212-13, reconstructed from student notebooks; UPSC wording is adapted. Never convert it "
    "into guilt for involuntary thought. MILL: utility means aggregate happiness/welfare; "
    "higher/lower pleasures qualify crude quantity; act utilitarianism evaluates the "
    "particular act, rule utilitarianism the generally followed rule; Mill's own classification "
    "is disputed. Rule utilitarianism responds to, but does not conclusively solve, innocent-"
    "punishment and rights objections. Harm principle: competent adults may be coerced "
    "principally to prevent harm to others; offence, dislike and paternalistic majority "
    "preference are insufficient; harm boundaries and spillovers remain contested. RAWLS: "
    "original position and veil of ignorance are a device of representation, not literal "
    "ignorance; primary goods include liberties, opportunities, income and social bases of "
    "self-respect. Exact lexical order: equal basic liberties -> fair equality of opportunity "
    "-> difference principle. Efficiency is not a fourth lexical stage; it remains a separate "
    "feasibility consideration constrained by justice. Liberty cannot be traded for economic gain. "
    "Fair opportunity is substantive, not merely formal. Difference principle permits "
    "inequality only when it benefits the least advantaged; it does not require identical "
    "outcomes. Reflective equilibrium mutually adjusts principles and considered judgments. "
    "COMPARATIVE APPLICATION: codes of ethics/intention and codes of conduct/external acts "
    "partly mirror Kant but are not identical; cost-benefit analysis is consequential, not "
    "automatically rule-utilitarian; Rawls is strongest for institutional design; Aristotle "
    "is strongest for contextual proportion; Kant supplies dignity and duty floors; Mill "
    "tests welfare and coercive harm. QUOTATION SPINE: 2018 Lincoln = mixed consequences in "
    "policy; 2019 Socrates = examined life, Plato Apology 38a; 2020 Socrates emotional-values "
    "line = unverified; 2021 Dalai inner peace = exact primary unverified; 2021 Erikson = "
    "interdependence, not acceptance, exact primary unverified; 2022 Potter Stewart = widely "
    "attributed, primary unverified; 2022 Dalai success line = misattributed chain-email "
    "tradition; 2024 Kant = adapted Infield lecture passage; 2025 William James = exact text "
    "untraced, popularised through Peale 1952. PYQ MARKS: every isolated quotation subpart is "
    "10 marks/150 words; two combined subparts require 20 marks/300 words; an entire three-"
    "quotation question requires 30 marks/450 words. CURRENT ANCHOR: India AI Governance "
    "Guidelines list seven technology-agnostic sutras — Trust, People First, Innovation over "
    "Restraint, Fairness & Equity, Accountability, Understandable by Design, Safety, "
    "Resilience & Sustainability — and organise recommendations across enablement, regulation "
    "and oversight. PIB 19 February 2026: M.A.N.A.V. = Moral and Ethical Systems, Accountable "
    "Governance, National Sovereignty, Accessible and Inclusive AI, Valid and Legitimate "
    "Systems; AI framed around human aspirations, ethics and dignity. Philosopher mappings "
    "to these official frameworks are analytical inference only, never official classification."
)
