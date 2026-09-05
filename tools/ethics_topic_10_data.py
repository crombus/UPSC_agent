"""Learner-v2 source data: Ethics Topic 10, Sources of Ethical Guidance."""

SESSION_TITLES = (
    "Why ethical guidance requires more than legal compliance",
    "Law, rules, regulations and conscience: precise distinctions",
    "How guidance sources interact in public administration",
    "Indian administrative applications and constitutional limits",
    "High-yield facts and close-option traps",
    "PYQ demand, answer thesis and law-versus-ethics method",
    "Probable questions and answer entry points",
    "Crisis of conscience and channel-first institutional dissent",
    "Snowden-type disclosure and calibrated conscientious action",
    "Evidence units, directive decoding and final synthesis",
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
    ("11", "12"),
    ("13", "14"),
)

MCQ_ITEMS = (
    {
        "label": "Law is not identical with every administrative instruction",
        "statement": (
            "A law is a binding legal norm whose authority arises within the constitutional and "
            "statutory framework; an office instruction may guide officials without becoming law."
        ),
        "scenario_a": (
            "A district office circular asks officers to use a new reporting format, but no "
            "statute or rule creates a penalty for citizens who do not use it."
        ),
        "scenario_b": (
            "A municipal officer calls a departmental checklist a law and refuses to consider "
            "whether its parent statute permits an equivalent method of compliance."
        ),
        "family": "legal taxonomy",
        "group": "legal taxonomy",
    },
    {
        "label": "Rules normally exercise delegated authority",
        "statement": (
            "A rule commonly gives operational detail under an enabling law and must remain within "
            "that delegated authority, statutory purpose, constitutional limits and procedural requirements."
        ),
        "scenario_a": (
            "A welfare department issues eligibility rules under an Act, then adds a condition "
            "excluding a class the Act expressly protects."
        ),
        "scenario_b": (
            "A licensing officer follows a rule mechanically although it appears inconsistent "
            "with the parent Act's stated public-health purpose."
        ),
        "family": "legal taxonomy",
        "group": "legal taxonomy",
    },
    {
        "label": "Regulations require a source of regulatory power",
        "statement": (
            "A regulation is ordinarily a binding delegated norm made by a statutory regulator "
            "or authority under enabling power; it is not simply a synonym for any guideline."
        ),
        "scenario_a": (
            "A statutory environmental authority frames compliance regulations under its enabling "
            "Act after the prescribed consultation process."
        ),
        "scenario_b": (
            "A public undertaking calls an internal advisory email a regulation although no "
            "statutory authority or rule-making power supports it."
        ),
        "family": "legal taxonomy",
        "group": "legal taxonomy",
    },
    {
        "label": "Codes and circulars have variable legal force",
        "statement": (
            "A code of ethics, conduct code, circular or guideline may guide and sometimes bind "
            "an employee, but its force depends on its legal source and adoption."
        ),
        "scenario_a": (
            "A hospital's ethics code asks doctors to disclose conflicts of interest even where "
            "the conduct rule provides no identical wording."
        ),
        "scenario_b": (
            "A department treats every advisory circular as delegated legislation and disciplines "
            "an employee without checking its service-rule basis."
        ),
        "family": "legal taxonomy",
        "group": "legal taxonomy",
    },
    {
        "label": "Legal compliance is an ethical floor, not a ceiling",
        "statement": (
            "Legality establishes a necessary public minimum, while ethics also examines purpose, "
            "fairness, foreseeable harm, integrity and institutional trust where no offence is proved."
        ),
        "scenario_a": (
            "A contractor accepts gifts just below a disclosed threshold from firms seeking "
            "future work and claims that no express offence has occurred."
        ),
        "scenario_b": (
            "An officer releases a technically permissible dataset while ignoring whether weak "
            "beneficiaries can be identified and harmed."
        ),
        "family": "legality and ethics",
        "group": "legality and ethics",
    },
    {
        "label": "Code of ethics differs from code of conduct",
        "statement": (
            "A code of ethics articulates aspirational public values, whereas a code of conduct "
            "specifies observable duties, prohibitions and possible institutional consequences for breach."
        ),
        "scenario_a": (
            "A service handbook says officials shall uphold integrity, while another provision "
            "requires annual asset declarations and specifies disciplinary action for default."
        ),
        "scenario_b": (
            "A trainee says a value statement is useless because it does not itself prescribe "
            "a penalty for every morally questionable act."
        ),
        "family": "legality and ethics",
        "group": "legality and ethics",
    },
    {
        "label": "Propriety asks how public power is used",
        "statement": (
            "Propriety tests fairness, public purpose and appearance of impartiality beyond bare "
            "legal validity, especially where discretionary public power can create avoidable distrust."
        ),
        "scenario_a": (
            "A collector awards a lawful short-term consultancy to a former classmate without "
            "recording the conflict or considering equally qualified applicants."
        ),
        "scenario_b": (
            "A public servant accepts hospitality technically permitted by a local threshold "
            "from a vendor whose tender she will soon evaluate."
        ),
        "family": "legality and ethics",
        "group": "legality and ethics",
    },
    {
        "label": "Ethics informs the making and revision of rules",
        "statement": (
            "Ethics informs rule design by requiring legitimate purpose, equal concern, "
            "proportionality, transparency and review of foreseeable burdens on affected persons."
        ),
        "scenario_a": (
            "A state designs an online-only benefit rule without considering villages where "
            "connectivity and digital literacy are severely limited."
        ),
        "scenario_b": (
            "A regulator revises a filing rule after evidence shows that the original form "
            "systematically excludes persons with disabilities."
        ),
        "family": "legality and ethics",
        "group": "legality and ethics",
    },
    {
        "label": "Constitutional morality is not popular morality",
        "statement": (
            "Constitutional morality requires fidelity to constitutional values, procedures and "
            "limits on power, rather than uncritical acceptance of transient majority preference or official convenience."
        ),
        "scenario_a": (
            "A district administration considers excluding a disliked minority from a public "
            "hearing because local majority groups demand it."
        ),
        "scenario_b": (
            "An officer defends unequal treatment by saying it is popular locally, despite "
            "clear equality concerns and no lawful justification."
        ),
        "family": "constitutional morality",
        "group": "constitutional morality",
    },
    {
        "label": "Constitutional morality requires cultivation",
        "statement": (
            "Constitutional morality is cultivated through civil education, institutional practice, "
            "public reasons and adherence to rule of law; it is not an automatic personal sentiment."
        ),
        "scenario_a": (
            "A training academy uses equality, due process and non-arbitrariness exercises to "
            "teach probationers how to justify discretionary decisions."
        ),
        "scenario_b": (
            "A supervisor assumes that an officer's strong personal convictions automatically "
            "prove constitutional morality without testing the relevant constitutional value."
        ),
        "family": "constitutional morality",
        "group": "constitutional morality",
    },
    {
        "label": "Constitutional morality does not authorise unilateral illegality",
        "statement": (
            "An official invoking constitutional morality should identify the applicable principle "
            "and pursue lawful review, recorded dissent or competent escalation rather than personally suspending valid rules."
        ),
        "scenario_a": (
            "A licensing officer believes a departmental direction is discriminatory and records "
            "reasons before seeking review from the competent authority."
        ),
        "scenario_b": (
            "A public servant ignores an applicable rule solely because she considers her "
            "private moral view superior to institutional procedure."
        ),
        "family": "constitutional morality",
        "group": "constitutional morality",
    },
    {
        "label": "Legality includes constitutional limits",
        "statement": (
            "A legality assessment includes constitutional competence, equality, due process and "
            "non-arbitrariness; constitutional morality is therefore not simply a source outside all law."
        ),
        "scenario_a": (
            "A local rule is formally issued but singles out one community without a rational "
            "public purpose or a fair hearing."
        ),
        "scenario_b": (
            "An officer calls a direction legal merely because it has a file number, without "
            "checking whether the issuing authority possessed power."
        ),
        "family": "constitutional morality",
        "group": "constitutional morality",
    },
    {
        "label": "Conscience is a signal requiring reflection",
        "statement": (
            "Conscience is an internal moral judgment shaped by reflection and social experience; "
            "it can identify overlooked wrongs but may also reflect bias or incomplete facts."
        ),
        "scenario_a": (
            "A procurement officer feels uneasy about a bid and then checks ownership records, "
            "conflict declarations and comparative prices before drawing a conclusion."
        ),
        "scenario_b": (
            "A field officer rejects a beneficiary application on instinct without verifying "
            "facts, hearing the applicant or checking the governing scheme."
        ),
        "family": "conscience and resistance",
        "group": "conscience and resistance",
    },
    {
        "label": "Crisis of conscience differs from an ordinary dilemma",
        "statement": (
            "A crisis of conscience is acute conflict between moral conviction and role demand, "
            "whereas an ordinary dilemma balances competing legitimate duties without necessarily threatening moral identity."
        ),
        "scenario_a": (
            "An officer is ordered to certify data she believes has been deliberately falsified "
            "and experiences participation as betrayal of a core commitment to truth."
        ),
        "scenario_b": (
            "A collector must choose between two needy villages when relief stocks are inadequate "
            "but neither option involves a dishonest or unlawful instruction."
        ),
        "family": "conscience and resistance",
        "group": "conscience and resistance",
    },
    {
        "label": "Civil disobedience differs from official dissent",
        "statement": (
            "Civil disobedience is public, principled and non-violent resistance accepting legal consequences; "
            "a public servant normally owes office-specific accountability through institutional dissent channels."
        ),
        "scenario_a": (
            "Citizens publicly and peacefully violate an unjust segregation rule, accept arrest "
            "and seek its reform through democratic debate."
        ),
        "scenario_b": (
            "A civil servant posts confidential files online before making a written objection, "
            "seeking review or approaching an authorised oversight body."
        ),
        "family": "conscience and resistance",
        "group": "conscience and resistance",
    },
    {
        "label": "Conscientious objection is conditional in public service",
        "statement": (
            "Conscientious objection or recusal is not a presumed general immunity for public servants; "
            "its availability depends on lawful authority, institutional norms and continuing duty to citizens."
        ),
        "scenario_a": (
            "An officer requests recusal from a decision involving a close relative and asks "
            "the competent authority to assign the matter elsewhere."
        ),
        "scenario_b": (
            "A public servant refuses all work connected with a lawful welfare programme without "
            "seeking substitution, review or any recognised institutional accommodation."
        ),
        "family": "conscience and resistance",
        "group": "conscience and resistance",
    },
    {
        "label": "Institutional channels should precede external disclosure",
        "statement": (
            "Where wrongdoing is suspected, first use evidence-based, recorded and competent internal "
            "channels unless urgency, capture or serious public harm makes that route demonstrably inadequate."
        ),
        "scenario_a": (
            "An accounts officer notices duplicate invoices, preserves records and reports through "
            "the designated vigilance channel before approaching outsiders."
        ),
        "scenario_b": (
            "A junior engineer forwards unverified corruption allegations to social media without "
            "checking documents or using the departmental complaint mechanism."
        ),
        "family": "institutional channels and disclosure",
        "group": "institutional channels and disclosure",
    },
    {
        "label": "Whistleblowing concerns public-interest wrongdoing",
        "statement": (
            "Whistleblowing concerns evidence-based reporting of corruption, illegality, serious wrongdoing "
            "or public harm; it is not a label for every disagreement with policy or a superior."
        ),
        "scenario_a": (
            "A PSU employee documents inflated invoices and reports them to the designated authority "
            "despite credible fear of victimisation."
        ),
        "scenario_b": (
            "An employee calls herself a whistleblower after publicly objecting to a lawful transfer "
            "policy that affects her personal convenience."
        ),
        "family": "institutional channels and disclosure",
        "group": "institutional channels and disclosure",
    },
    {
        "label": "External disclosure requires a necessity test",
        "statement": (
            "External disclosure requires careful necessity, proportionality, evidentiary and public-interest assessment, "
            "including risks to privacy, confidentiality, security, due process and uninvolved persons."
        ),
        "scenario_a": (
            "An official considering disclosure of a surveillance programme assesses whether narrower "
            "authorised reporting could address the wrongdoing without exposing operational details."
        ),
        "scenario_b": (
            "A hospital employee releases identifiable patient files to prove poor management although "
            "redaction and authorised complaint mechanisms were available."
        ),
        "family": "institutional channels and disclosure",
        "group": "institutional channels and disclosure",
    },
    {
        "label": "Protection claims need current legal verification",
        "statement": (
            "Do not assume that reporting wrongdoing receives complete statutory protection; identify the "
            "current instrument, jurisdiction, recipient, confidentiality safeguards, retaliation remedies and limitations."
        ),
        "scenario_a": (
            "A central-government employee seeks advice on reporting fraud and first verifies the "
            "current applicable vigilance and disclosure mechanism."
        ),
        "scenario_b": (
            "A trainer assures all employees that every anonymous disclosure is legally protected "
            "without checking governing law, scope or commencement status."
        ),
        "family": "institutional channels and disclosure",
        "group": "institutional channels and disclosure",
    },
    {
        "label": "Discretion is structured rather than personal freedom",
        "statement": (
            "Administrative discretion is judgment within lawful purpose, relevant facts, equality and "
            "procedure; it is not personal freedom to substitute sympathy or preference for governing standards."
        ),
        "scenario_a": (
            "A collector prioritises relief after documenting vulnerability, access constraints and "
            "scheme criteria rather than favouring her own constituency."
        ),
        "scenario_b": (
            "A licensing officer waives requirements for a politically connected applicant because "
            "he believes helping influential people improves local development."
        ),
        "family": "discretion and reasoned orders",
        "group": "discretion and reasoned orders",
    },
    {
        "label": "Form protects values but can defeat statutory purpose",
        "statement": (
            "Procedural form protects equality, predictability and auditability, yet literal application "
            "that defeats lawful purpose may require an authorised, evidence-based and reviewable response."
        ),
        "scenario_a": (
            "A flood victim lacks a destroyed paper certificate but presents an officially recognised "
            "equivalent record permitted by the relevant scheme."
        ),
        "scenario_b": (
            "An officer invokes substance to waive every eligibility requirement secretly for a "
            "favoured group despite no authority for the departure."
        ),
        "family": "discretion and reasoned orders",
        "group": "discretion and reasoned orders",
    },
    {
        "label": "Reasoned orders make ethics accountable",
        "statement": (
            "A reasoned order records authority, facts, affected interests, alternatives and grounds "
            "for decision, making discretion intelligible, reviewable and less vulnerable to arbitrary influence."
        ),
        "scenario_a": (
            "A district authority explains why one evacuation route was selected after recording "
            "safety evidence, accessibility concerns and alternatives considered."
        ),
        "scenario_b": (
            "A public office rejects a licence application with only the words 'not recommended,' "
            "leaving the applicant unable to understand or challenge the decision."
        ),
        "family": "discretion and reasoned orders",
        "group": "discretion and reasoned orders",
    },
    {
        "label": "A sound decision joins legal and ethical tests",
        "statement": (
            "A defensible public decision identifies legal authority, constitutional values, relevant rules, "
            "ethical harms, institutional channels and proportionate safeguards before reaching a qualified conclusion."
        ),
        "scenario_a": (
            "A procurement head faced with pressure to split purchases checks financial rules, "
            "conflict risks, public loss, records reasons and escalates the concern."
        ),
        "scenario_b": (
            "An officer relies only on personal conscience to decide a land-allocation dispute, "
            "without examining authority, affected rights or review mechanisms."
        ),
        "family": "discretion and reasoned orders",
        "group": "discretion and reasoned orders",
    },
)

PYQS = (
    {
        "year": 2018,
        "question": (
            "GS-IV Q12: Edward Snowden, a computer expert and former CIA systems administrator, "
            "released confidential Government documents to the press about the existence of "
            "Government surveillance programmes. According to many legal experts and the US "
            "Government, his actions violated the Espionage Act of 1917, which identified the leak "
            "of State secrets as an act of treason. Yet, despite the fact that he broke the law, "
            "Snowden argued that he had a moral obligation to act. He gave a justification for his "
            "\"whistle blowing\" by stating that he had a duty \"to inform the public as to that "
            "which is done in their name and that which is done against them.\" According to "
            "Snowden, the Government's violation of privacy had to be exposed regardless of "
            "legality since more substantive issues of social action and public morality were "
            "involved here. Many agreed with Snowden. Few argued that he broke the law and "
            "compromised national security, for which he should be held accountable. Do you agree "
            "that Snowden's actions were ethically justified even if legally prohibited? Why or "
            "why not? Make an argument by weighing the competing values in this case. "
            "(Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Verified against books\\more_previous_papers\\GENERAL-STUDIES-PAPER-IV.pdf, page 11, "
            "and routed in _PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md:265. This is a shared "
            "Topic 10/22/23 route; legal characterisations belong to the paper stem and should "
            "not be restated as independently settled conclusions."
        ),
        "answer": (
            "Snowden's case is a conflict between privacy, informed democratic consent and public "
            "interest on one side, and legality, confidentiality, institutional loyalty and national "
            "security on the other. A moral claim cannot be dismissed merely because it challenges "
            "official secrecy; law may lag behind a serious wrong. Equally, private conscience cannot "
            "by itself licence disclosure of classified material.\n\n"
            "The ethical assessment should ask whether the alleged wrongdoing was evidence-based, "
            "whether authorised internal or oversight channels were realistically available, whether "
            "disclosure was necessary to avert serious public harm, and whether the material released "
            "was proportionate and minimised avoidable security or privacy damage. A deontological "
            "view emphasises duties of truth and confidentiality; consequential reasoning weighs "
            "democratic benefit against operational harm; virtue ethics asks whether courage was joined "
            "with prudence.\n\n"
            "For an Indian public servant, the safer institutional lesson is channel-first dissent: "
            "preserve evidence, record objection, use competent vigilance or oversight mechanisms and "
            "seek protection where available. External disclosure becomes ethically stronger only where "
            "internal remedies are inadequate and necessity is compelling. Thus the underlying concern "
            "may be morally serious, but ethical justification depends on method, proportionality and "
            "accountability, not conscience alone. A decision-maker should also distinguish disclosure "
            "of a public-interest concern from indiscriminate publication of every classified detail. "
            "Independent scrutiny, redaction and an opportunity to correct unlawful practice can protect "
            "both democratic accountability and legitimate security interests. The strongest conclusion "
            "is consequently conditional, not an unconditional celebration or condemnation of disclosure."
        ),
    },
    {
        "year": 2019,
        "question": (
            "GS-IV Q3(a): What is meant by the term 'constitutional morality'? How does one "
            "uphold constitutional morality? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, page 2, "
            "and ledger :273. It is jointly routed to Topics 14 and 10; do not present it as "
            "exclusive Topic 10 ownership."
        ),
        "answer": (
            "Constitutional morality is fidelity to the Constitution's values, procedures and limits "
            "on public power, rather than obedience to a transient majority or a superior's convenience. "
            "It requires equality, liberty, dignity, due process and non-arbitrariness to guide public "
            "action. It is cultivated through civil education and institutional practice, not assumed "
            "as an innate sentiment.\n\n"
            "It is upheld when public authorities act within competence, give affected persons a fair "
            "hearing, offer public reasons, treat like cases alike and remain open to review. A district "
            "officer facing popular pressure to exclude a minority from a public hearing should protect "
            "equal participation and record reasons. Constitutional morality therefore disciplines both "
            "majoritarian impulses and personal preference, converting public office into accountable "
            "constitutional service. It is upheld continuously through transparent procedures, institutional "
            "checks and willingness to correct decisions that fail constitutional standards."
        ),
    },
    {
        "year": 2019,
        "question": (
            "GS-IV Q3(b): What is meant by 'crisis of conscience'? How does it manifest itself "
            "in the public domain? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, page 2, "
            "and ledger :273. The ledger's row is a neutral routing summary; the official scan "
            "controls quotation and this is a shared Topic 10/14 route."
        ),
        "answer": (
            "A crisis of conscience is an acute conflict between an individual's considered moral "
            "conviction and an external role demand, instruction or institutional expectation. It "
            "differs from an ordinary dilemma because compliance is experienced as betrayal of a "
            "core moral commitment; it may occur even without a legal breach.\n\n"
            "In public life it may appear as hesitation, a written dissent note, refusal to certify "
            "dishonest data, recusal where authorised, escalation to oversight, protected reporting "
            "of wrongdoing or, exceptionally, resignation. An officer asked to sign a report she "
            "believes is falsified faces such a crisis. The ethical response is neither blind compliance "
            "nor impulsive public defiance: test facts and authority, record reasons, seek competent "
            "review and use the least disruptive channel capable of protecting the public interest."
        ),
    },
    {
        "year": 2020,
        "question": (
            "GS-IV Q4(a): Distinguish between laws and rules. Discuss the role of ethics in "
            "formulating them. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\more_previous_papers\\Gen_St_P4.pdf, page 2, and ledger :291. "
            "This isolated subpart is the direct Topic 10 route; do not merge it with Q4(b), "
            "which belongs to the Attitude owner."
        ),
        "answer": (
            "Laws are binding legal norms operating within the constitutional and statutory framework. "
            "Rules generally supply operational detail under delegated authority and must remain within "
            "the parent law's purpose, limits and procedure. Regulations may similarly be binding "
            "delegated norms of statutory authorities; circulars and guidelines have variable force.\n\n"
            "Ethics improves their formulation by asking whether the objective is legitimate, the burden "
            "proportionate, similarly placed persons treated equally and reasons transparent. It also "
            "requires consultation with affected groups and periodic review of unintended exclusion. "
            "For example, an online-only welfare rule may be legally framed yet ethically defective if "
            "it predictably excludes persons lacking connectivity. Ethics therefore does not replace "
            "legal authority; it makes law and rules fairer, more humane and more likely to command trust."
        ),
    },
    {
        "year": 2021,
        "question": (
            "GS-IV Q4(b): In case of crisis of conscience does emotional intelligence help to "
            "overcome the same without compromising the ethical or moral stand that you are likely "
            "to follow? Critically examine. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, "
            "page 3. This is a cross-route: Topic 05 is primary; Topic 10 supplies the "
            "crisis-of-conscience and institutional-channel analysis."
        ),
        "answer": (
            "Emotional intelligence can help an official recognise distress, regulate anger and fear, "
            "listen to affected persons and communicate principled dissent without escalating conflict. "
            "It may prevent a crisis of conscience from becoming denial, paralysis or impulsive leakage.\n\n"
            "However, EI cannot decide whether the underlying instruction is lawful, constitutional or "
            "ethical. A highly self-controlled officer may still rationalise wrongdoing, while empathy "
            "without evidence may become partiality. The officer should therefore test facts, identify "
            "the governing law and constitutional value, record a reasoned objection and seek competent "
            "review. EI is an enabling capacity for preserving an ethical stand; it is not a substitute "
            "for conscience, public reasons or accountable institutional process. It is most useful when "
            "it helps the officer remain respectful, courageous and open to evidence during escalation."
        ),
    },
    {
        "year": 2022,
        "question": (
            "GS-IV Q6(a): A whistle-blower reporting corruption, illegal activities, wrongdoing and "
            "misconduct to concerned authorities risks grave danger, physical harm and victimisation. "
            "What policy measures would strengthen protection mechanisms? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, "
            "page 4. Use as a cross-route to the corruption, vigilance and protection owners; do "
            "not assert current statutory status without a contemporaneous official source."
        ),
        "answer": (
            "A credible protection system needs confidential and accessible reporting channels, a "
            "competent independent recipient, time-bound preliminary assessment and secure preservation "
            "of evidence. Identity should be disclosed only on demonstrated need, with reasons and "
            "oversight. Anti-retaliation safeguards should cover transfer, appraisal, harassment, "
            "disciplinary misuse and physical threats; urgent security and legal assistance should be "
            "available where risk is credible.\n\n"
            "The system also needs reasoned closure, appeal, periodic audit of retaliation complaints "
            "and penalties for malicious victimisation as well as knowingly false allegations. Digital "
            "case tracking can improve accountability without exposing identity. These measures make "
            "conscience-driven reporting an institutional public-interest act rather than an unsafe "
            "personal gamble. Their exact legal basis and scope must be verified at the time of use, "
            "particularly before promising confidentiality or immunity."
        ),
    },
    {
        "year": 2023,
        "question": (
            "GS-IV Q5(a): Is conscience a more reliable guide when compared to laws, rules and "
            "regulations in the context of ethical decision-making? Discuss. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\more_previous_papers\\QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, "
            "page 4, and ledger :343. This is the clearest direct Topic 10 theory route; Q5(b) "
            "is separately owned by the Probity topic."
        ),
        "answer": (
            "Conscience can be a valuable early-warning guide because it may recognise cruelty, "
            "dishonesty or dignity harms before detailed rules anticipate them. It can motivate courage "
            "where compliance with the letter of a rule would offend public purpose.\n\n"
            "Yet conscience is individually calibrated and may reflect bias, misinformation, ideology "
            "or misplaced certainty. Laws, rules and regulations contribute notice, consistency, equal "
            "treatment, enforceability and review. They too are imperfect: a technically compliant "
            "decision may violate integrity or the spirit of public office.\n\n"
            "Therefore conscience is neither more reliable in every case nor dispensable. The sound "
            "sequence is conscience as a signal, facts and constitutional values as tests, applicable "
            "law and rules as constraints, and recorded institutional review as safeguard. This avoids "
            "both rule worship and unaccountable individualism."
        ),
    },
    {
        "year": 2024,
        "question": (
            "GS-IV Q4(a): Examine, with suitable examples, the proposition that just and unjust "
            "are contextual and changing contexts must remain under scrutiny to prevent miscarriage "
            "of justice. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, page 3, and ledger "
            ":43. It is a joint route with Topic 08; contextuality must not be misrepresented as "
            "unrestricted ethical relativism."
        ),
        "answer": (
            "Context changes facts, burdens and foreseeable consequences; it need not alter the "
            "underlying commitments to dignity, equality and public purpose. Restrictions that are "
            "proportionate during a grave emergency may become excessive when conditions change. "
            "Likewise, an apparently neutral digital-benefit rule needs revision when evidence shows "
            "systematic exclusion of persons unable to authenticate online.\n\n"
            "A just administration therefore monitors outcomes, hears affected persons, reviews evidence "
            "and gives reasons for adaptation. Context is not a blank cheque for convenience: political "
            "pressure cannot redefine discrimination, corruption or cruelty as just. Lawful authority, "
            "equal treatment and review remain safeguards. Ethical judgment combines stable values with "
            "alertness to changed realities, preventing yesterday's reasonable practice from becoming "
            "today's injustice. Periodic data, grievance analysis and consultation make that scrutiny "
            "administratively credible rather than a post-hoc assertion."
        ),
    },
    {
        "year": 2024,
        "question": (
            "GS-IV Q4(b): Examine, with suitable illustrations, the claim that mindless attachment "
            "to form while ignoring substance causes injustice, and that a perceptive civil servant "
            "should avoid literalness and carry out true intent. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, page 3, and ledger "
            ":43. This is a joint Topic 08/10 route. Substance never authorises ultra-vires action "
            "or selective waiver."
        ),
        "answer": (
            "Procedural form protects equality, predictability and auditability. But literal insistence "
            "can become unjust where it defeats the lawful purpose for which a requirement exists. "
            "For example, if a scheme permits equivalent identity proof, rejecting a flood victim solely "
            "because an original paper was destroyed would frustrate welfare delivery.\n\n"
            "A perceptive officer identifies the statutory purpose, checks delegated authority, considers "
            "similarly placed persons and records reasons for any permitted accommodation. The officer "
            "must not use 'substance' to invent power, conceal a favour or waive substantive eligibility. "
            "Thus purposive administration corrects mechanical literalism, while public reasons and "
            "review prevent discretion from becoming arbitrary. Where uncertainty remains, a timely "
            "clarification from the competent authority is safer than an undisclosed improvisation. "
            "The resulting decision must remain equally available to comparable applicants."
        ),
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q1(b): 'Constitutional morality is not a natural sentiment but a product of "
            "civil education and adherance of the rule of law.' Examine the significance of "
            "constitutional morality for a public servant, highlighting its role in promoting good "
            "governance and ensuring accountability in public administration. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Verified against books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, page 2. The paper's "
            "spelling 'adherance' is retained here. This is a cross-route assigned in the recent "
            "ledger to Topics 13 and 14, not exclusive Topic 10 ownership; do not claim that the "
            "question requires Ambedkar/Grote genealogy."
        ),
        "answer": (
            "Constitutional morality makes a public servant accountable to constitutional values and "
            "procedures rather than to personal preference, majoritarian pressure or administrative "
            "convenience. Civil education and rule-of-law practice cultivate habits of equality, due "
            "process, restraint and reason-giving.\n\n"
            "It promotes good governance when an officer acts within authority, hears affected persons, "
            "treats comparable cases consistently, discloses relevant reasons and accepts review. For "
            "example, popular hostility cannot justify excluding a minority from a public consultation. "
            "Constitutional morality also prevents an official from invoking private conscience as a "
            "licence for unilateral action: a suspected unconstitutional direction should be challenged "
            "through recorded dissent and competent review. It therefore links ethical public service "
            "with transparent, fair and answerable administration. Its practical test is whether citizens "
            "can understand, question and seek review of how public power was exercised."
        ),
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q10: Rajesh is a Group A officer with nine years of service. He is posted as "
            "Administrative Officer in an Oil Public Sector undertaking. As an Administrative "
            "Officer he is responsible for managing and coordinating various administrative tasks "
            "to ensure smooth functioning of office. He also manages office supplies, equipment "
            "etc. Rajesh is now sufficient senior and is expecting his next promotion in JAG "
            "(Junior Administrative Grade) in the next one or two years. He knows that promotion "
            "is based on examination of ACRs/Performance Appraisal of last few years (5 years or "
            "so) of an officer by a DPC (Departmental Promotion Committee) and an officer lacking "
            "requisite grading of ACRs may not be found fit for promotion. Consequences of losing "
            "promotion may entail financial and reputational loss and set-back for career "
            "progression. Though he also puts his best efforts in official discharge of his duties, "
            "yet he is unsure of assessment by his superior officer. He is now putting extra efforts "
            "so that he gets thumping report at the end of financial year. As Administrative "
            "Officer, Rajesh is regularly interacting with his immediate boss, who is his reporting "
            "officer for writing his ACR. One day he calls Rajesh and wants him to buy "
            "computer-related stationery on priority from a particular vendor. Rajesh instructs "
            "his office to initiate action for procuring these items. During the day, the dealing "
            "Assistant brings an estimate of Rupees Thirty Five Lakhs covering all stationery "
            "items from the same vendor. It is noticed that as per delegated financial powers, as "
            "provided in the GFR (General Financial Rules) as applicable in that Organisation, "
            "expenditure for office items exceeding Rupees Thirty Lakhs requires sanction of the "
            "next higher authority (boss in the present case). Rajesh knows that immediate superior "
            "would expect all these purchases should be done at his level and may not appreciate "
            "such lack of initiative on his part. During discussions with office, he learns that "
            "common practice of splitting of expenditure (where large order is divided into a "
            "series of smaller ones) is followed to avoid obtaining sanction from higher authority. "
            "This practice is against the rules and may come to the adverse notice of Audit. Rajesh "
            "is perturbed. He is unsure of taking decision in the matter. (a) What are the options "
            "available with Rajesh in the above situation? (b) What are the ethical issues involved "
            "in this case? (c) Which would be the most appropriate option for Rajesh and why? "
            "(Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Verified against books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, page 8, and routed at "
            "_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md:81. It is a shared Topic 22/10 case route; "
            "the full official case facts and all three sub-demands are reproduced here."
        ),
        "answer": (
            "Rajesh faces conflict between career interest and integrity, loyalty to a superior and "
            "loyalty to institution, urgency and procurement propriety, as well as fear of adverse "
            "appraisal and duty to protect public funds. The financial threshold and vendor-specific "
            "direction create risks of bypassing sanction, competition, value for money and auditability.\n\n"
            "His options include complying silently; refusing abruptly; seeking oral clarification; "
            "splitting or manipulating procurement; or placing a factual, respectful written note "
            "identifying the applicable GFR requirement and proposing a lawful route. The first and "
            "fourth options compromise integrity. Abrupt refusal may be principled but loses an "
            "opportunity for reasoned correction.\n\n"
            "He should preserve the estimate and relevant rule, seek written confirmation of urgency "
            "and specifications, record the sanction threshold and recommend competitive or properly "
            "authorised procurement. If pressure persists, he should escalate through the competent "
            "financial, vigilance or organisational channel while avoiding allegation beyond evidence. "
            "He should not allow promotion anxiety to shape the record. This response respects law, "
            "rules, probity and public interest while keeping dissent accountable. Safeguards include "
            "a reasoned file note, equal treatment of vendors, an audit trail and protection against "
            "retaliatory appraisal through prescribed review channels. If urgency is genuinely established, "
            "Rajesh should identify the precise authorised exception, document why ordinary competition "
            "is impracticable, compare feasible alternatives and require post-facto scrutiny. That narrow "
            "response serves the immediate office need without allowing urgency or hierarchy to become a "
            "cover for favouritism, evasion of financial safeguards or avoidable public loss."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Distinguish law, rule and regulation as sources of ethical guidance in public administration."
        ),
        "answer": (
            "Law is a binding legal norm operating within the constitutional and statutory framework. "
            "A rule generally provides operational detail under authority delegated by a parent law. "
            "A regulation is commonly a binding delegated norm issued by a statutory regulator or "
            "authority. A circular, guideline or ethics code may guide conduct, but its binding force "
            "depends on its legal source and adoption.\n\n"
            "The distinction matters because no official may treat an advisory instruction as if it "
            "automatically overrides statute, constitutional equality or delegated limits. Conversely, "
            "a valid rule cannot be ignored simply because an officer prefers another course. Ethics "
            "improves each instrument by testing public purpose, fairness, proportionality, transparency "
            "and foreseeable exclusion. An online-only welfare rule, for example, should be reviewed "
            "where it predictably excludes persons without connectivity. Thus taxonomy supplies legal "
            "discipline, while ethics makes rule-making and implementation humane, legitimate and "
            "worthy of public trust."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Constitutional morality is neither majoritarian morality nor personal conscience. Discuss."
        ),
        "answer": (
            "Constitutional morality is fidelity to constitutional values, procedures and limits on "
            "public power. It is not majoritarian morality: popularity cannot validate discrimination, "
            "arbitrary exclusion or denial of fair hearing. It is also not personal conscience: an "
            "official's sincere preference requires grounding in constitutional principle, facts and "
            "lawful authority.\n\n"
            "For a civil servant, it requires equality, dignity, due process, reasoned decisions and "
            "acceptance of review. A district officer should not exclude a minority from consultation "
            "because local opinion favours it; nor may the officer suspend a valid rule merely because "
            "of private disapproval. The proper response to a suspected unconstitutional direction is "
            "a recorded objection and competent review. Civil education and everyday rule-of-law practice "
            "therefore convert constitutional morality into accountable public service rather than a "
            "political slogan."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Is conscience reliable enough to guide ethical decision-making by a public servant? Examine."
        ),
        "answer": (
            "Conscience is valuable because it can detect dishonesty, cruelty or dignity harms before "
            "detailed rules identify them. It can supply moral courage when a technically compliant "
            "action defeats public purpose. An officer's unease over a vendor-specific tender, for "
            "example, may trigger scrutiny of conflicts and inflated prices.\n\n"
            "Its reliability is limited. Conscience is formed through experience and reflection but may "
            "also contain prejudice, incomplete information, ideology or overconfidence. It cannot "
            "replace constitutional competence, applicable law, service rules or fair hearing. Rules "
            "provide notice, consistency and enforceability, though they too can lag behind novel wrongs "
            "or be followed in spiritless fashion.\n\n"
            "The defensible approach is calibrated conscience. Treat moral discomfort as a signal; verify "
            "facts, identify stakeholders and constitutional values, test authority and consequences, "
            "then record reasons. Where wrongdoing remains credible, use internal reporting, escalation "
            "or authorised oversight before external disclosure. Conscience is thus necessary for ethical "
            "administration, but reliable only when disciplined by evidence, public reasons and "
            "institutional accountability. This calibration also protects officials from retaliation claims "
            "because the concern, evidence, authority and proposed remedy are clearly recorded."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Distinguish civil disobedience from institutional dissent by a civil servant and explain "
            "why the distinction matters."
        ),
        "answer": (
            "Civil disobedience is ordinarily public, principled and non-violent resistance to a law or "
            "policy, undertaken to communicate injustice and accepting legal consequences. Its actor "
            "appeals to the public conscience and democratic reform process. Institutional dissent by a "
            "civil servant arises within an office whose authority, records and duties are structured "
            "by law and service conditions.\n\n"
            "Therefore a public servant should normally begin with facts, written objection, clarification, "
            "recusal where lawfully available, escalation and competent oversight. This preserves "
            "confidentiality, audit trails, due process and continuity of public service. An official "
            "cannot convert every policy disagreement into a personal licence to disobey or disclose "
            "confidential material.\n\n"
            "The distinction does not require blind obedience. Where credible serious wrongdoing persists, "
            "internal channels are compromised and public harm is grave, the case for further disclosure "
            "may become ethically stronger. Necessity, proportionality, evidence and protection of "
            "uninvolved persons must then be shown. Institutional-channel-first conduct reconciles "
            "conscience with constitutional accountability. It protects citizens from disrupted service, "
            "protects accused persons from unsupported allegations and preserves a fair record for review. "
            "It preserves institutional legitimacy."
        ),
    },
    {
        "marks": 20,
        "question": (
            "A procurement officer receives a lawful-looking oral direction that would defeat the "
            "purpose of financial safeguards. Examine the ethical options and recommend a course of action."
        ),
        "answer": (
            "The officer must separate apparent form from lawful substance. Relevant stakeholders include "
            "citizens financing the purchase, eligible vendors, the department, the superior, audit bodies "
            "and the officer. Ethical issues are value for money, conflict of interest, equality of "
            "opportunity, integrity of record, fear of retaliation and the risk that urgency becomes a "
            "pretext for favouritism.\n\n"
            "Blind compliance may preserve short-term hierarchy but can defeat financial purpose and "
            "damage trust. Public confrontation or unsupported accusation may be unfair and ineffective. "
            "Manipulating split orders or backdating records is clearly impermissible. The officer should "
            "first verify the applicable rule, delegated authority, urgency evidence and alternatives. "
            "She should seek written confirmation, place a neutral file note on the threshold and recommend "
            "a transparent, authorised procurement route. If the concern remains, she should escalate to "
            "the competent financial or vigilance authority, retaining evidence and avoiding public "
            "disclosure beyond necessity.\n\n"
            "A reasoned order should identify facts, legal authority, public purpose, comparable treatment "
            "and safeguards. Emergency departure, if legally authorised, must be narrow, time-bound, "
            "documented and reviewable. This solution respects hierarchy without treating obedience as "
            "superior to law, propriety or citizens' interest. It also protects the officer through an "
            "audit trail and prescribed review of retaliatory appraisal or transfer. Finally, she should "
            "communicate respectfully, seek timely independent advice and distinguish a legitimate urgent "
            "exception from an instruction designed merely to avoid competition or oversight. This protects "
            "public trust. If emergency procurement is genuinely necessary, the file should state why "
            "ordinary competition was impracticable, identify the authorised exception, compare feasible "
            "alternatives and provide for post-facto scrutiny. This confines urgency to public purpose "
            "instead of letting it become a discretionary shield for favouritism."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Design an ethical response where a public servant has credible evidence of wrongdoing but "
            "believes ordinary internal channels may be compromised."
        ),
        "answer": (
            "The starting point is careful verification, not heroic impulse. The servant should preserve "
            "lawfully obtained evidence, distinguish corruption or serious illegality from ordinary policy "
            "disagreement, identify immediate harm and avoid spreading untested allegations. Stakeholders "
            "include affected citizens, accused persons entitled to due process, the institution, oversight "
            "bodies and the servant facing retaliation.\n\n"
            "The first route remains the least compromised competent channel: a written objection, "
            "independent superior, designated vigilance recipient, statutory regulator, ombudsman or "
            "judicial remedy where applicable. The complaint should state facts, authority, public harm "
            "and requested action, while preserving confidentiality. The servant should request protection "
            "only under a currently verified applicable instrument; no general statutory protection should "
            "be presumed.\n\n"
            "If available channels are demonstrably captured, delay threatens grave public harm and "
            "authorised escalation fails, further disclosure requires a stringent necessity and "
            "proportionality test. Minimise data, redact uninvolved persons, avoid operational-security "
            "harm and retain a clear public-interest rationale. Media disclosure is not the default.\n\n"
            "The ethical aim is neither silence nor unaccountable leakage. It is an evidence-based, "
            "reviewable path that protects public interest, due process and institutional integrity while "
            "reducing victimisation risk. Periodic independent audit should examine whether complaints are "
            "received, assessed and closed with reasons, whether retaliation indicators are detected, and "
            "whether confidentiality failures have exposed either the reporter or persons accused. Such "
            "monitoring turns a nominal channel into a credible accountability mechanism for all concerned over time in practice."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": "1. Sources of ethical guidance map",
        "structural_type": "nested-authority-map",
        "nodes": (
            "Conscience signals an internal moral concern.",
            "Family and social learning shape early moral judgment.",
            "Professional ethics articulate occupational values.",
            "Conduct codes specify institutional expectations.",
            "Service rules govern defined official conduct.",
            "Regulations operate under delegated legal authority.",
            "Statutes establish binding public legal standards.",
            "Constitutional limits test all public authority.",
        ),
        "verdict": "Treat the sources as interacting checks, not as a mechanical ladder that legalises every compliant act.",
        "answer_use": "Use for an opening definition map before resolving a law-rule-conscience conflict.",
    },
    {
        "title": "2. Law, rule, regulation and instruction",
        "structural_type": "authority-chain",
        "nodes": (
            "Start with constitutional competence and rights.",
            "Identify the parent statute and its purpose.",
            "Locate any delegated rule-making power.",
            "Check whether a valid rule applies.",
            "Identify regulator-made regulations, if any.",
            "Separate circulars and guidelines from regulations.",
            "Check service-rule or contractual adoption of codes.",
            "Record the instrument's actual legal force.",
        ),
        "verdict": "Never call every office instruction a law or every guideline delegated legislation.",
        "answer_use": "Use in the 2020 laws-versus-rules answer and in rule-of-law case studies.",
    },
    {
        "title": "3. Legality, ethics and propriety",
        "structural_type": "three-test-comparison",
        "nodes": (
            "Ask whether the actor has legal authority.",
            "Check compliance with applicable rule and procedure.",
            "Identify the public purpose of the power.",
            "Test fairness and equal treatment.",
            "Map foreseeable harms and benefits.",
            "Check conflicts, gifts and appearance of bias.",
            "Assess trust and institutional precedent.",
            "State a qualified ethical-propriety verdict.",
        ),
        "verdict": "Technical legality is necessary but does not exhaust ethics or propriety.",
        "answer_use": "Use to structure a legal-but-unethical example without implying that ethics overrides law.",
    },
    {
        "title": "4. Ethics in making rules",
        "structural_type": "rule-design-cycle",
        "nodes": (
            "Define the legitimate public objective.",
            "Identify affected groups and unequal burdens.",
            "Choose authority consistent with the parent law.",
            "Make criteria intelligible and transparent.",
            "Test proportionality of restrictions and sanctions.",
            "Build access and accommodation where authorised.",
            "Provide reasons, appeal and review mechanisms.",
            "Revise after evidence of exclusion or harm.",
        ),
        "verdict": "Ethics improves legitimacy, fairness and implementation; it does not create delegated power.",
        "answer_use": "Use for the second half of 2020 GS-IV Q4(a).",
    },
    {
        "title": "5. Constitutional morality in administration",
        "structural_type": "value-to-action-ladder",
        "nodes": (
            "Identify the constitutional value in issue.",
            "Check competence and legal authority.",
            "Protect equality and non-arbitrariness.",
            "Respect dignity and affected-person voice.",
            "Follow due process and fair hearing.",
            "Give intelligible public reasons.",
            "Resist majoritarian or partisan pressure.",
            "Accept competent review and correction.",
        ),
        "verdict": "Constitutional morality disciplines both majority pressure and private preference.",
        "answer_use": "Use for the 2019 and 2025 constitutional-morality routes.",
    },
    {
        "title": "6. Calibrating conscience",
        "structural_type": "reflection-and-audit-loop",
        "nodes": (
            "Notice the moral alarm or discomfort.",
            "Collect facts instead of acting on impulse.",
            "Name the affected stakeholders and harms.",
            "Check personal bias and incomplete information.",
            "Identify applicable law and service rules.",
            "Test constitutional values and public purpose.",
            "Consult a competent institutional channel.",
            "Record a revisable reasoned conclusion.",
        ),
        "verdict": "Conscience is an ethical signal that becomes reliable through evidence and public reasoning.",
        "answer_use": "Use for 2023 GS-IV Q5(a) and conscience-based case studies.",
    },
    {
        "title": "7. Crisis of conscience response ladder",
        "structural_type": "escalation-ladder",
        "nodes": (
            "Define the instruction and moral conflict precisely.",
            "Verify facts, law and seriousness of harm.",
            "Reflect and seek ethical or legal clarification.",
            "Place a factual written objection on record.",
            "Seek recusal only where authority permits it.",
            "Escalate to a competent superior or oversight body.",
            "Report verified wrongdoing through available channels.",
            "Consider resignation only after grave unresolved complicity.",
        ),
        "verdict": "Use the lowest effective accountable channel, not silent compliance or immediate public defiance.",
        "answer_use": "Use in the 2019 crisis-of-conscience answer and public-service dilemmas.",
    },
    {
        "title": "8. Civil disobedience versus institutional dissent",
        "structural_type": "split-boundary-comparison",
        "nodes": (
            "Citizen identifies an unjust law or policy.",
            "Civil resistance is public and communicative.",
            "Non-violence limits coercive harm.",
            "Acceptance of consequence signals principled protest.",
            "Public servant holds delegated official authority.",
            "Office duty requires records and confidentiality.",
            "Dissent begins with review and escalation channels.",
            "External action needs necessity and proportionality.",
        ),
        "verdict": "Do not import the citizen's civil-disobedience model unchanged into public-service office duties.",
        "answer_use": "Use to distinguish principled resistance from unaccountable disclosure.",
    },
    {
        "title": "9. Whistleblowing and protected channels",
        "structural_type": "public-interest-disclosure-test",
        "nodes": (
            "Identify evidence of serious wrongdoing or harm.",
            "Separate fact from policy disagreement or grievance.",
            "Preserve material lawfully and confidentially.",
            "Assess immediate public-interest urgency.",
            "Use the least compromised competent recipient.",
            "Verify current protection and confidentiality scope.",
            "Document retaliation risk and requested safeguard.",
            "Seek independent review of response or inaction.",
        ),
        "verdict": "Whistleblowing is evidence-based public-interest reporting, not an automatic entitlement to leak.",
        "answer_use": "Use for the 2022 protection route and conscience-to-accountability answers.",
    },
    {
        "title": "10. Snowden-type external disclosure test",
        "structural_type": "proportionality-decision-tree",
        "nodes": (
            "Specify the alleged public wrong.",
            "Verify evidence and credibility of the concern.",
            "Map privacy, transparency and security values.",
            "Assess realistic internal oversight channels.",
            "Test whether those channels are inadequate.",
            "Consider narrower authorised disclosure alternatives.",
            "Minimise avoidable harm to uninvolved persons.",
            "Give a qualified necessity-proportionality verdict.",
        ),
        "verdict": "A serious conscience claim strengthens only when method, necessity and proportionality also withstand scrutiny.",
        "answer_use": "Use for 2018 GS-IV Q12 without treating the question's legal claims as settled facts.",
    },
    {
        "title": "11. Form, substance and reasoned discretion",
        "structural_type": "purposive-decision-chain",
        "nodes": (
            "Identify the statutory or scheme purpose.",
            "Read the applicable rule and its exception.",
            "Establish relevant facts and affected interests.",
            "Check whether equivalent compliance is authorised.",
            "Treat similarly placed persons alike.",
            "Reject ultra-vires or selective waiver.",
            "Record authority, alternatives and reasons.",
            "Enable audit, appeal and judicial review.",
        ),
        "verdict": "Substance corrects mechanical literalism only within authority, equality and review safeguards.",
        "answer_use": "Use for 2024 Q4(b) and discretionary welfare or procurement cases.",
    },
    {
        "title": "12. Answer-writing synthesis",
        "structural_type": "eight-step-answer-spine",
        "nodes": (
            "Define the precise source-of-guidance issue.",
            "Distinguish law, rule, regulation and code.",
            "Identify constitutional value and legal authority.",
            "State the ethical harm or public-interest concern.",
            "Test conscience against facts and bias.",
            "Choose institutional channel and safeguard.",
            "Use a named Indian administrative illustration.",
            "Conclude with a qualified accountable verdict.",
        ),
        "verdict": "High-scoring answers combine ethical sensitivity with lawful, evidence-based institutional action.",
        "answer_use": "Use as the final revision checklist for theory questions and case studies.",
    },
)

CURRENT_ANCHOR = {
    "title": "Central Vigilance Commission: Vigilance Awareness Week 2025",
    "verified_facts": (
        "Central Vigilance Commission Circular No. 04/08/25 dated 1 August 2025 scheduled Vigilance Awareness Week 2025 for 27 October to 2 November 2025.",
        "The circular's theme was 'Vigilance: Our Shared Responsibility'.",
        "A three-month preventive-vigilance campaign ran from 18 August to 17 November 2025.",
        "The campaign focused on disposal of pending complaints, disposal of pending cases, capacity-building programmes, asset management and digital initiatives.",
    ),
    "administrative_link": (
        "⚠️ Inference, not an official classification: the circular illustrates preventive vigilance, "
        "shared institutional responsibility, record-keeping and accountable channels. It can anchor "
        "an answer on how conscience, service systems and public accountability should reinforce one another."
    ),
    "limit": (
        "The circular and PIB release do not establish statutory whistleblower protection, authorise "
        "external disclosure, or make every circular or guideline delegated legislation. Do not add "
        "unverified claims about current whistleblower-law status, rights, remedies or institutional powers."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/sep/doc2025923644201.pdf",
    "https://pib.gov.in/Pressreleaseshare.aspx?PRID=2183039",
)

SOURCE_CAVEAT = (
    "Use the local Topic 10 Basic and Advanced owners as controlling authored sources, subject to "
    "these limits. Do not collapse law, rule, regulation, circular, guideline and code into one "
    "taxonomy: a rule or regulation needs its actual enabling source, and an administrative instruction "
    "does not automatically have delegated-legislation force. Constitutional morality is fidelity to "
    "constitutional values and procedure, not a free-standing personal override of valid law or a "
    "synonym for majoritarian morality. Frame recusal and conscientious objection as conditional on "
    "lawful authority and institutional norms, not as a universal civil-service entitlement. For "
    "whistleblowing, verify current legal status, scope, commencement, recipient and protection before "
    "claiming any statutory safeguard; channel-first analysis remains an ethical framework, not proof "
    "of a protected remedy. Quote official local paper scans where available; routing ledgers are "
    "neutral ownership summaries, not authoritative verbatim text. Preserve isolated ten-mark PYQ "
    "subparts instead of merging them. The 2025 GS-IV Q1(b) constitutional-morality question is a "
    "cross-route assigned in the recent ledger to Topics 13 and 14, not exclusive Topic 10 ownership, "
    "and its paper demand does not require Ambedkar/Grote genealogy. The 2018 Snowden legal "
    "characterisations belong to the question stem and must not be repeated as independently settled claims. "
    "The official 2025 Vigilance Awareness Week sources establish only the stated dates, theme and campaign "
    "focus; preventive-vigilance and accountability linkages are analytical inference."
)

REGISTER_SUPPLEMENT = (
    "### RAPID RECALL: SOURCES AND CONFLICTS\n\n"
    "- **Law:** binding legal norm; identify constitutional and statutory authority.\n"
    "- **Rule:** normally delegated operational detail; test against the parent law.\n"
    "- **Regulation:** delegated norm of a statutory authority; do not equate it with an office email.\n"
    "- **Ethics:** asks purpose, fairness, harms, integrity and trust beyond bare compliance.\n"
    "- **Constitutional morality:** equality, dignity, due process, reason-giving and restraint of power.\n"
    "- **Conscience:** useful moral alarm; verify facts and bias before relying on it.\n"
    "- **Crisis of conscience:** acute conflict with role demand; distinguish from every hard dilemma.\n"
    "- **Channel-first response:** record objection -> competent escalation -> verified protected route.\n"
    "- **Whistleblowing:** evidence-based public-interest wrongdoing, not every policy disagreement.\n"
    "- **External disclosure:** necessity, proportionality, confidentiality and security must be tested.\n"
    "- **Form and substance:** purposive accommodation must remain authorised, equal and reviewable.\n"
    "- **Reasoned order:** authority + facts + alternatives + reasons + review safeguard.\n\n"
    "### PYQ SPINE\n\n"
    "- **2018 Q12:** conscience versus secrecy; weigh values, channels and proportionality.\n"
    "- **2019 Q3(a)/(b):** constitutional morality and crisis of conscience.\n"
    "- **2020 Q4(a):** law-rule distinction and ethical rule-making.\n"
    "- **2022 Q6(a):** whistleblower protection architecture.\n"
    "- **2023 Q5(a):** calibrated conscience, not rule worship or private absolutism.\n"
    "- **2024 Q4(a)/(b):** context, substance, authority and reasoned discretion.\n"
    "- **2025 Q10:** GFR-propriety case: written reasons, escalation and retaliation safeguards."
)
