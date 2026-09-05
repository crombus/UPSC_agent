"""Learner-v2 source data: Ethics Topic 02, Human Values and Leaders."""

SESSION_TITLES = (
    "Where values come from and how they become character",
    "Turning values into public-service choices",
    "Gandhi: keeping means and ends ethically connected",
    "Learning courage and calm from Indian exemplars",
    "Mahavir: many-sided truth and non-possession",
    "Kautilya and the design of corruption controls",
    "Duty without craving credit: Nishkama karma",
    "Reform through education: Savitribai Phule and Kalam",
    "How to use a leader without hero-worship",
    "Writing quotation answers that earn GS-IV marks",
)

SESSION_GROUPS = (
    ("1", "2"),
    ("3"),
    ("4"),
    ("5"),
    ("6"),
    ("7"),
    ("8"),
    ("8a", "8b"),
    ("9"),
    ("10", "11"),
)

MCQ_ITEMS = (
    {
        "label": "Value formation is social and revisable",
        "statement": "Values are enduring beliefs about what is desirable that are transmitted through family, education, culture, peers, role models and lived experience; they can be strengthened or corroded by repeated institutional incentives rather than being permanently fixed at birth.",
        "scenario_a": "A district training academy combines classroom ethics with supervisors who disclose conflicts and correct false field reports even when no audit is expected. Which explanation best captures why this can build integrity?",
        "scenario_b": "A recruit says that values learnt at home make later training irrelevant. Her mentor instead uses reflection, peer feedback and transparent work routines. Which view correctly distinguishes early conditioning from later internalisation?",
        "group": "value-sources",
    },
    {
        "label": "Internalisation differs from performance",
        "statement": "Value internalisation means that a value guides conduct even when no one is watching, whereas value performance displays approved conduct mainly for appraisal, publicity or fear of sanction; the former is more reliable under discretion and pressure.",
        "scenario_a": "An officer refuses a contractor's hospitality only during vigilance inspections but accepts it in private after the inspection team leaves. Is this best described as internalised probity or externally managed performance?",
        "scenario_b": "A block officer corrects an overpayment before releasing funds although the error is unlikely to be detected and the correction delays the target. What feature most strongly indicates internalisation?",
        "group": "value-sources",
    },
    {
        "label": "Values are broader than attitudes",
        "statement": "Values are relatively enduring beliefs about what is worthwhile across situations, while attitudes are object-specific evaluations; value education therefore develops judgement and habits, not merely a favourable response to a particular policy or person.",
        "scenario_a": "A trainee warmly supports a cleanliness campaign but falsifies attendance in an unrelated training programme. Which distinction explains why a positive campaign attitude alone does not establish honesty as a value?",
        "scenario_b": "A school evaluates students only by whether they can repeat slogans on integrity. What addition would better assess value education rather than temporary attitude display?",
        "group": "value-sources",
    },
    {
        "label": "Mission Karmayogi is an institutional channel",
        "statement": "Mission Karmayogi's NPCSCB approach links civil-service capacity building to functional and behavioural competencies, a citizen-government interface, a shift from rules to roles, and iGOT learning; it institutionalises learning but cannot by itself prove ethical internalisation.",
        "scenario_a": "A department records every official's course completion on iGOT and declares corruption impossible. Which qualification follows from the distinction between competency exposure and ethical conduct under temptation?",
        "scenario_b": "A service redesign maps roles at a citizen-facing office, identifies empathy and problem-solving gaps, and assigns relevant learning modules. Which Mission Karmayogi logic is being used?",
        "group": "value-sources",
    },
    {
        "label": "Gandhi's social sins join means to ends",
        "statement": "The Seven Social Sins published and endorsed by Gandhi warn against separating power, wealth, pleasure, knowledge, commerce, science and worship from their ethical restraints; their administrative force lies in testing whether apparently successful ends were pursued through principled means.",
        "scenario_a": "A municipality meets its revenue target by pressuring small vendors to pay unofficial fees while publicising new parks. Which Gandhi-style diagnosis is most precise: failure of outcomes, or wealth and politics detached from ethical means?",
        "scenario_b": "A research unit obtains useful health data by concealing consent conditions from participants. Which social-sin pairing most directly identifies the ethical failure?",
        "group": "gandhi-and-exemplars",
    },
    {
        "label": "Gandhi list provenance needs care",
        "statement": "ARC Box 2.8 reproduces the Seven Social Sins from Gandhi's Young India context, but the 22 October 1925 note presented the list as sent by a correspondent and uses 'pleasure without conscience' where the ARC prints 'leisure without conscience'; answers should not overclaim authorship or textual uniformity.",
        "scenario_a": "A candidate writes that Gandhi personally coined every word of a fixed seven-item list and quotes 'leisure' as the original wording. What correction preserves both exam utility and provenance?",
        "scenario_b": "A civil-service ethics poster uses the ARC wording but footnotes it as a list Gandhi published and endorsed, noting the pleasure/leisure variation. Why is this preferable to treating a popular slogan as a settled primary text?",
        "group": "gandhi-and-exemplars",
    },
    {
        "label": "Vivekananda supports adaptation, not imitation",
        "statement": "Vivekananda's traceable 2024 quotation advocates learning what is good from others while absorbing it in one's own way; in administration it supports contextual adaptation of useful institutions, not either blind copying or reflexive rejection of external learning.",
        "scenario_a": "A State copies a foreign digital grievance platform despite weak connectivity and language access in tribal blocks. A district team proposes local-language assisted kiosks while retaining transparent tracking. Which response best follows the teaching?",
        "scenario_b": "An official rejects every practice from another country because it is foreign. Why is this no more faithful to Vivekananda's proposition than mechanical transplantation?",
        "group": "gandhi-and-exemplars",
    },
    {
        "label": "Faith requires capacity and resolve",
        "statement": "The 2024 UPSC-attributed Sardar Patel proposition joins faith with strength: ethical conviction needs competence, courage and organised capacity to accomplish public work; because no primary Patel speech or letter source is traced, the answer should analyse the stated idea without manufacturing a citation.",
        "scenario_a": "A flood-control officer sincerely believes in protecting vulnerable residents but neither prepares evacuation plans nor acts against an influential encroacher. What does the faith-and-strength proposition reveal about this failure?",
        "scenario_b": "A candidate assigns the exact quotation to a named Patel speech without evidence. What is the responsible way to retain the governance lesson while handling the attribution?",
        "group": "gandhi-and-exemplars",
    },
    {
        "label": "Thiruvalluvar teaches active equanimity",
        "statement": "The Thiruvalluvar quotation tested in 2025 conveys equanimity in adversity: composure prevents panic from amplifying a crisis, but it does not excuse passivity; it is a modern paraphrase of Tirukkural 623 rather than a named historic translation.",
        "scenario_a": "During a landslide, a Sub-Divisional Magistrate remains calm, verifies road access, communicates uncertainty honestly and orders evacuation. Which element shows equanimity rather than emotional detachment?",
        "scenario_b": "A supervisor tells an officer facing a communal rumour to wait silently because 'trouble troubles itself.' Which reading of the quotation is conceptually wrong?",
        "group": "jain-kautilya-duty",
    },
    {
        "label": "William James provenance and usable idea",
        "statement": "The 2025 line about altering life by altering attitudes is widely attributed to William James but is not traceable to his writings and was popularised by Norman Vincent Peale; the answer may discuss conscious attitude change while clearly avoiding a fabricated James citation.",
        "scenario_a": "A probationer reframes a difficult rural posting as a chance to learn local administration, seeks feedback and improves service access. What valid insight about attitude change can be drawn without claiming the disputed wording is a James primary text?",
        "scenario_b": "A coaching note cites the exact 2025 wording as a proved James discovery. What provenance correction should an examiner reward?",
        "group": "jain-kautilya-duty",
    },
    {
        "label": "Law needs social morality but not replacement",
        "statement": "The 2025 UPSC-attributed Vivekananda proposition that societal strength rests in morality rather than laws usefully stresses internalised compliance, yet law, due process and institutions remain necessary safeguards; the wording is not traceable to the Complete Works and must not be treated as a verified primary quotation.",
        "scenario_a": "A district reduces road deaths through fair enforcement, road engineering and local campaigns against drunk driving. Why would relying only on penalties or only on moral appeals both be incomplete?",
        "scenario_b": "An officer excuses a procurement violation because her intention was good and morality matters more than rules. Which limit on the proposition defeats that reasoning?",
        "group": "jain-kautilya-duty",
    },
    {
        "label": "Anekantavada is not moral relativism",
        "statement": "Mahavir's Anekantavada and Syadvada express many-sidedness and conditional predication: complex truth-claims require humility and structured consideration of standpoints, but the doctrines do not mean that every claim is equally valid or that public authorities may avoid justified decisions.",
        "scenario_a": "Before a land-acquisition decision, an officer hears cultivators, women workers, engineers and environmental experts, records reasons and chooses a lawful option. Which Jain-informed administrative discipline is illustrated?",
        "scenario_b": "A chairperson refuses to decide a safety dispute because all viewpoints are equally true. Why is this an incorrect use of Anekantavada?",
        "group": "jain-kautilya-duty",
    },
    {
        "label": "Aparigraha translates into probity",
        "statement": "Aparigraha, non-possessiveness among Mahavir's five Mahavratas, supports a public ethic of non-attachment to office-derived gain, conflict-of-interest control and resistance to nepotism; it does not demand indifference to legitimate public resources or personal responsibility.",
        "scenario_a": "A licensing officer removes herself from a file involving her sibling's firm and records the conflict. Which public-service expression of Aparigraha is most direct?",
        "scenario_b": "A hospital superintendent refuses to purchase essential equipment, claiming that avoiding all possession is ethically superior. What error confuses non-possessiveness with neglect of public duty?",
        "group": "jain-kautilya-duty",
    },
    {
        "label": "Kautilya identifies opportunity and concealment",
        "statement": "The Arthashastra passages quoted in ARC Annexure-I(2) use the honey and fish analogies to show that officials handling public money face temptation and concealment; this is a structural account of corruption that calls for auditable controls, detection and fair incentives, not character sermons alone.",
        "scenario_a": "A district finds that storekeepers can alter stock registers without independent reconciliation. It introduces separation of duties, random checks and transparent records. Which Kautilyan insight is being operationalised?",
        "scenario_b": "A minister argues that only morally weak people need controls, so trusted officers should never be audited. Which part of Kautilya's reasoning challenges this view?",
        "group": "jain-kautilya-duty",
    },
    {
        "label": "Kautilya is not surveillance alone",
        "statement": "Kautilya's ARC-cited account pairs action against wrongful accumulation with permanence for officials who increase public wealth in just ways; a modern translation therefore balances rule-bound vigilance, rewards and protection of honest officials rather than normalising punitive or arbitrary surveillance.",
        "scenario_a": "A department rotates all officers suddenly after an anonymous complaint, without recorded criteria or review. Why is this weaker than a transparent, risk-based rotation and integrity-support system?",
        "scenario_b": "A procurement unit rewards accurate disclosure, protects reporters and conducts proportionate audits. Which balance distinguishes institutional vigilance from demoralising suspicion?",
        "group": "jain-kautilya-duty",
    },
    {
        "label": "Nishkama karma rejects personal attachment",
        "statement": "Nishkama karma means performing one's duty without attachment to personal reward, credit or fruit; it requires conscientious effort and concern for public outcomes, not indifference to whether a programme succeeds or a citizen is harmed.",
        "scenario_a": "An officer completes a difficult vaccination drive, credits frontline workers and accepts that promotion may not follow, while tracking missed settlements. Why is this duty without attachment rather than indifference to results?",
        "scenario_b": "A colleague ignores repeated pension delays saying that one should not care about outcomes. Which conceptual distinction exposes the misuse of Nishkama karma?",
        "group": "duty-reform-and-limits",
    },
    {
        "label": "Duty joins responsibility and fulfilment",
        "statement": "Devotion to duty gives a civil servant responsibility for timely, fair and competent action and can yield personal fulfilment through meaningful service; it cannot legitimise burnout, illegal orders or a self-righteous refusal to learn from affected citizens.",
        "scenario_a": "A revenue officer stays late to resolve pension grievances but documents workload risks, delegates lawfully and asks for staff support. How does this better express devotion to duty than heroic but unsustainable overwork?",
        "scenario_b": "A superior orders an officer to suppress an inconvenient inspection report and calls obedience 'duty.' What boundary must a Nishkama karma answer state?",
        "group": "duty-reform-and-limits",
    },
    {
        "label": "Savitribai Phule models institution-building",
        "statement": "Savitribai Phule's work with Jyotirao Phule in co-founding the Bhide Wada girls' school in Pune in 1848 shows that gender inequality is confronted through durable institutions, access to education and support for excluded groups, not sentiment alone.",
        "scenario_a": "A district responds to girls' dropout by opening safe transport, recruiting local women educators and supporting adolescent re-entry rather than merely holding a ceremonial speech. Which Savitribai-inspired lesson is most accurately applied?",
        "scenario_b": "A programme celebrates women achievers annually but leaves school toilets, safety and caste-linked exclusion unaddressed. What structural limitation does the Phule example reveal?",
        "group": "duty-reform-and-limits",
    },
    {
        "label": "Kalam's chain is attributed with care",
        "statement": "A.P.J. Abdul Kalam used and endorsed a chain linking righteousness in the heart to peace in the world, while crediting it in his 2007 European Parliament address to Sathya Sai Baba; it illustrates a bottom-up ethical aspiration, not an empirically proven single-cause model of governance.",
        "scenario_a": "A school programme combines integrity practice, respectful family dialogue and civic projects, while the district also improves complaint systems. Why is this stronger than claiming personal virtue alone automatically creates national order?",
        "scenario_b": "An answer calls the righteousness-to-peace chain Kalam's original theorem and treats it as statistical proof. Which two cautions are missing?",
        "group": "duty-reform-and-limits",
    },
    {
        "label": "Exemplars need contextual translation",
        "statement": "Leader-based ethics is useful when a teaching is translated into a specific decision rule, Indian illustration and institutional safeguard; it becomes an exemplar fallacy when a revered name substitutes for evidence, ignores competing duties or pretends that personal virtue alone settles a complex case.",
        "scenario_a": "In a mining dispute, an officer invokes Gandhi's conscience but does not consult affected communities, apply law or assess environmental evidence. What makes the invocation ethically incomplete?",
        "scenario_b": "A candidate uses Mahavir to justify consultation, then explains the statutory decision, recorded reasons and review process. Why is this better than biography-led answer writing?",
        "group": "duty-reform-and-limits",
    },
    {
        "label": "Quotation answers test translation",
        "statement": "A strong GS-IV quotation answer states the core idea, briefly situates it, translates it into a present administrative mechanism, supplies a concrete Indian illustration, acknowledges a relevant limitation or provenance caution, and closes with a qualified ethical verdict rather than a biography.",
        "scenario_a": "For a quotation on courage, a candidate spends 120 of 150 words listing the leader's life events and gives no governance application. What central demand of the question remains unmet?",
        "scenario_b": "Another candidate links courage to documented whistleblower protection, gives a district-level example and warns against reckless disclosure of personal data. Which answer architecture is demonstrated?",
        "group": "duty-reform-and-limits",
    },
    {
        "label": "Values and institutions must work together",
        "statement": "Character-centred lessons such as Gandhi's and structural lessons such as Kautilya's are complementary: internalised values guide conduct where rules cannot observe everything, while transparent procedures, incentives and accountability reduce opportunities for values to be overwhelmed by discretion and pressure.",
        "scenario_a": "A department responds to procurement risk by conducting ethics discussions but retains opaque single-person approvals. What missing half of the values-plus-institutions approach remains?",
        "scenario_b": "Another department digitises every approval but rewards target completion even when field staff mislead citizens. Which ethical capability is still vulnerable despite stronger controls?",
        "group": "value-sources",
    },
    {
        "label": "Brahmacharya requires textual precision",
        "statement": "Mahavir's five Mahavratas are Ahimsa, Satya, Asteya, Brahmacharya and Aparigraha; Jain tradition distinguishes Parshvanatha's four restraints from Mahavir's five, with Brahmacharya separately enumerated rather than being an ethical idea demonstrably invented by Mahavir.",
        "scenario_a": "A matching question says Mahavir introduced ethical self-restraint for the first time by inventing Brahmacharya. Which precise correction follows from the tradition described in the owner?",
        "scenario_b": "An administrator describes the five vows as a complete manual for replacing constitutional law. Which distinction between ethical teaching and public institutional duty is being ignored?",
        "group": "jain-kautilya-duty",
    },
    {
        "label": "Competency scale is not conduct proof",
        "statement": "As of 6 February 2026, Mission Karmayogi's iGOT ecosystem had 1.49 crore users, 4,342 courses, 7.26 crore completions and 23 languages; these dated figures show learning reach, not a verified general APAR linkage or automatic improvement in ethical conduct.",
        "scenario_a": "A presentation claims that 7.26 crore completions establish that every official has become impartial. Which inference exceeds what the reported data can show?",
        "scenario_b": "A training director uses the figures to argue for multilingual access and then proposes observed behavioural practice and citizen feedback. Why is this a more defensible use of the data?",
        "group": "value-sources",
    },
)

PYQS = (
    {
        "year": 2024,
        "question": 'Given below are three quotations of great thinkers. What do each of these quotations convey to you in the present context? (a) "Learn everything that is good from others, but bring it in, and in your own way absorb it, do not become others." -Swami Vivekananda (Answer in 150 words)',
        "marks": 10,
        "source_note": "Official local 2024 GS Paper-IV, Q3(a), verbatim English wording. The line is traceable to Complete Works, Vol. III, The Common Bases of Hinduism (Lahore, 1897).",
        "answer": """The quotation advocates discerning learning rather than imitation. It asks a society or civil servant to absorb useful knowledge through its own needs, constitutional values and social conditions. In administration, it means that reform should retain a tested principle while adapting its delivery, language and safeguards to Indian realities.

For example, a State may learn from a foreign digital grievance-redress model, but should provide assisted counters, local-language access, offline receipt options and an appeal route where connectivity or literacy is weak. The value is neither cultural isolation nor cosmetic localisation; it is informed adaptation that improves equal access and accountability.

The principle also disciplines public-service learning. An officer should study successful procurement, health or urban-service practices elsewhere, test their assumptions, consult affected groups and document why an adaptation fits the local context. Blind transplantation can exclude citizens; reflexive rejection can preserve avoidable inefficiency.

Thus, the present relevance of Vivekananda's thought is ethical self-respect joined to openness. Borrow what advances public welfare, but translate it through constitutional equality, citizen experience and verifiable results. That makes learning a responsible public act rather than imitation for prestige.""",
    },
    {
        "year": 2024,
        "question": 'Given below are three quotations of great thinkers. What do each of these quotations convey to you in the present context? (b) "Faith is of no avail in the absence of strength. Faith and strength, both are essential to accomplish any great work-" -Sardar Patel (Answer in 150 words)',
        "marks": 10,
        "source_note": "Official local 2024 GS Paper-IV, Q3(b), verbatim English wording. UPSC attribution retained; no primary Patel speech or letter source is traced in the Basic owner.",
        "answer": """The proposition conveys that moral conviction becomes socially useful only when joined to strength: competence, courage, organisation and perseverance. Faith supplies direction and legitimacy; strength turns that direction into effective action. A civil servant therefore needs both an ethical commitment to public welfare and the capacity to implement it fairly.

Consider disaster management. Sympathy for flood-affected families is inadequate without credible warnings, trained teams, accessible shelters, transparent relief lists and courage to act against unsafe encroachment. Conversely, administrative power without ethical purpose can become coercive or serve the influential. The public value lies in their combination.

In daily governance, this means preparing files carefully, mastering rules, communicating honestly and resisting improper pressure. A district officer who believes in girls' education must also build safe transport, coordinate schools and address exclusion. Good intentions without execution disappoint citizens; technical efficiency without conscience may deepen inequity.

There is an attribution caution: the quotation is set by UPSC as Sardar Patel's, but the Basic owner does not trace it to a primary speech or letter. That does not weaken its ethical idea. The sound verdict is that public service needs values to choose the right end and institutional capability to reach it lawfully.""",
    },
    {
        "year": 2024,
        "question": 'Given below are three quotations of great thinkers. What do each of these quotations convey to you in the present context? (c) "In law, a man is guilty when he violates the rights of others. In ethics, he is guilty if he only thinks of doing so." -Immanuel Kant (Answer in 150 words)',
        "marks": 10,
        "source_note": "Official local 2024 GS Paper-IV, Q3(c), verbatim English wording. This topic routes the demand as a legality-versus-ethics application.",
        "answer": """The quotation distinguishes external legality from the moral quality of intention. Law normally punishes an established violation of another's rights; ethics asks an earlier question: whether one is willing to treat another person merely as a means. In public office, this distinction encourages conscience before misconduct becomes an actionable wrong.

An officer may have discretion to accept lavish hospitality that escapes a narrowly framed rule. Even before any quid pro quo occurs, accepting it can impair impartiality and public trust. Similarly, a supervisor who plans to suppress an inconvenient inspection may not yet have falsified a record, but the intention already reveals disregard for citizens' entitlement to truthful administration.

This does not mean that the State should punish private thoughts. Due process, evidence and legality remain essential; administrative action cannot be based on speculative moral policing. The practical translation is preventive ethics: disclose conflicts, recuse where necessary, maintain reasoned records and use codes and training to interrupt harmful intent before it becomes conduct.

Thus, the quotation expands responsibility beyond fear of punishment. A civil servant should ask not only, 'Can I do this legally?' but also, 'Can I justify it as respectful, impartial and fair to those affected?' That inner test strengthens, rather than replaces, lawful accountability.""",
    },
    {
        "year": 2025,
        "question": 'Given below are three quotations of great thinkers. What do each of these quotations convey to you in the present context? 3-(a) "Those who in trouble untroubled are, Will trouble trouble itself." - Thiruvalluvar (Answer in 150 words)',
        "marks": 10,
        "source_note": "Official local 2025 GS Paper 4, Q3(a), verbatim English wording. The Basic owner treats it as a modern paraphrase of Tirukkural 623, not a named historic translation.",
        "answer": """The quotation conveys equanimity under adversity. A calm mind does not deny danger; it prevents fear, anger and confusion from multiplying the original problem. For a civil servant, composure is therefore an operational virtue because it permits accurate assessment, humane communication and timely action in a crisis.

During a landslide or communal rumour, an officer should verify facts, activate response teams, communicate what is known and unknown, protect vulnerable groups and record decisions. Panic can spread misinformation and favour arbitrary action; disciplined calm helps the administration coordinate police, health workers and local representatives. The lesson is visible in a district control room that prioritises verified warnings and evacuation over dramatic but unsupported announcements.

Equanimity has a boundary. It is not passivity, emotional coldness or delay disguised as patience. A collector who remains serene while failing to order rescue, hear grievances or correct an error has misunderstood the teaching. Compassionate urgency must accompany inner steadiness.

The wording should also be handled carefully: it is a modern paraphrase linked by the Basic owner to Tirukkural 623, whose theme is not being distressed by adversity. The reasoned verdict is that calm leadership makes trouble manageable when it is joined to evidence, decisive lawful action and empathy.""",
    },
    {
        "year": 2025,
        "question": 'Given below are three quotations of great thinkers. What do each of these quotations convey to you in the present context? 3-(b) "The greatest discovery of my generation is that a human being can alter his life by altering his attitudes." - William James (Answer in 150 words)',
        "marks": 10,
        "source_note": "Official local 2025 GS Paper 4, Q3(b), verbatim English wording. Widely attributed to William James but not traceable to his writings; popularised by Norman Vincent Peale (1952).",
        "answer": """The idea conveys that attitudes are not wholly fixed: conscious reflection, learning and repeated practice can change how a person interprets difficulty and therefore how that person acts. In public service, this matters because an officer's attitude toward citizens, marginalised groups and unfamiliar postings shapes the quality of discretionary service.

A probationer initially treating a remote posting as punishment may, through field immersion and feedback, recognise local knowledge, learn the language and redesign access to welfare services. The changed attitude does not alter material constraints by wish alone; it changes attention, effort and willingness to collaborate. Training, mentoring and transparent work routines can therefore support behavioural competence alongside technical skill.

The proposition must not become victim-blaming. Poverty, discrimination, administrative opacity and inadequate staffing cannot be solved by asking citizens or employees merely to think positively. Structural reform, lawful entitlements and institutional accountability remain indispensable.

There is also a provenance caution. The exact sentence is widely attributed to William James but is not traceable to his writings in the Basic owner; it was popularised by Norman Vincent Peale. The answer should analyse the proposition, not invent a James citation. The verdict is that reflective attitude change is a real ethical resource when paired with fair institutions and concrete action.""",
    },
    {
        "year": 2025,
        "question": 'Given below are three quotations of great thinkers. What do each of these quotations convey to you in the present context? 3- (c) "The strength of a society is not in its laws, but in the morality of its people." - Swami Vivekananda (Answer in 150 words)',
        "marks": 10,
        "source_note": "Official local 2025 GS Paper 4, Q3(c), verbatim English wording. UPSC attribution retained; the wording is not traceable to Vivekananda's Complete Works in the Basic owner.",
        "answer": """The proposition highlights that law works best when citizens and officials possess internalised morality. No police force or rule book can observe every transaction, road crossing or exercise of discretion. Honesty, empathy and civic responsibility therefore reduce the gap between formal compliance and lived public order.

For instance, road safety improves not only through penalties but when drivers refuse drunk driving, communities discourage unsafe conduct and enforcement remains impartial. Likewise, welfare delivery depends on officials who do not demand informal payments and citizens who do not fabricate claims. Such everyday morality preserves trust and lowers the cost of enforcement.

However, morality cannot replace law. Social majorities can hold prejudices, and good intentions may be disputed. Constitutional rights, due process, transparent procedures and independent review protect persons precisely when informal morality fails. A procurement officer cannot ignore conflict-of-interest rules by asserting a moral purpose.

The exact line should be treated as a 2025 UPSC attribution, not as a verified primary Vivekananda quotation; the nearest documented theme in the owner is his concern that many laws may be little regarded. The balanced verdict is that ethical citizenship gives law its social strength, while just institutions channel morality, protect minorities and hold power accountable.""",
    },
    {
        "year": 2025,
        "question": "What are the major teachings of Mahavir? Explain their relevance in the contemporary world. (Answer in 150 words)",
        "marks": 10,
        "source_note": "Official local 2025 GS Paper 4, Q4(b), verbatim English wording.",
        "answer": """Mahavir's major teachings include the five Mahavratas: Ahimsa (non-violence), Satya (truthfulness), Asteya (non-stealing), Brahmacharya (self-restraint) and Aparigraha (non-possessiveness). Jain thought also develops Anekantavada, the many-sidedness of truth, and Syadvada, conditional predication. Together they cultivate restraint, truth, non-harm and humility in judgement.

Their contemporary relevance is practical. Ahimsa supports non-violent conflict resolution and humane treatment of vulnerable persons. Satya and Asteya strengthen honest records and resistance to misuse of public resources. Aparigraha provides an ethical basis for conflict-of-interest disclosure, anti-nepotism and non-attachment to office-derived gain. Before land acquisition or environmental clearance, Anekantavada supports serious consultation with cultivators, workers, experts and affected communities; it improves knowledge and legitimacy.

Yet many-sidedness is not moral relativism. A public authority must eventually decide on lawful evidence and record reasons; it cannot say that every claim is equally valid. Nor can personal restraint substitute for rights, rules and enforcement. Brahmacharya should be described carefully as separately enumerated in Mahavir's tradition, not casually as an idea he demonstrably invented.

Therefore, Mahavir's teaching remains relevant as an ethical discipline for plural societies: listen widely, harm less, speak truthfully and restrain private gain, while acting through constitutional institutions.""",
    },
    {
        "year": 2025,
        "question": '"One who is devoted to one\'s duty attains highest perfection in life." Analyse this statement with reference to sense of responsibility and personal fulfilment as a civil servant. (Answer in 150 words)',
        "marks": 10,
        "source_note": "Official local 2025 GS Paper 4, Q5(a), verbatim English wording.",
        "answer": """The statement reflects Nishkama karma: duty is performed with full commitment but without attachment to personal reward, credit or promotion. For a civil servant, responsibility means timely, competent and fair action because citizens depend on the office, not because recognition is assured. Personal fulfilment follows from meaningful service and integrity, rather than from status alone.

In a pension camp, devotion to duty would mean identifying delayed cases, correcting records, communicating reasons and ensuring that elderly claimants are not forced through avoidable visits. The officer may share credit with frontline staff and still measure whether the service actually reached people. This is not indifference to results; it is non-attachment to private gain combined with rigorous concern for public outcomes.

Duty has ethical limits. It does not require obeying an unlawful order, accepting chronic overwork as virtue or disregarding affected citizens in the name of efficiency. A responsible officer records dissent where necessary, seeks lawful support and protects both service quality and staff welfare.

Mission Karmayogi's focus on functional and behavioural competencies offers an institutional setting in which such responsibility can be practised, but course completion alone cannot demonstrate character. The verdict is that devoted duty unites inner fulfilment with accountable public action when it is guided by legality, empathy and measurable citizen welfare.""",
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": "Explain how family, educational institutions and public-service training can move a value from social instruction to internalised administrative conduct. Answer in 150 words.",
        "answer": """A value becomes internalised when it guides conduct even without surveillance. Family supplies early modelling: honesty in small transactions and respect for others make moral language concrete. Schools deepen it through discussion, fair rules, service learning and teachers whose conduct matches instruction. Public-service training must then test the value under real discretion.

For example, a trainee may learn compassion through community immersion, practise it by redesigning a disability-access counter, and receive feedback from citizens rather than merely memorising a definition. Mission Karmayogi can support such development through functional and behavioural competencies, role-based learning and iGOT access.

However, lectures and course completions do not prove integrity. Opaque targets, political pressure and reward for only numerical output can corrode a value. Training should be reinforced by transparent procedures, mentoring, reasoned records and safe reporting channels.

Thus, inculcation is a continuing social and institutional process: example begins it, practice tests it, and accountable work culture makes it durable.""",
    },
    {
        "marks": 10,
        "question": "Gandhi's Seven Social Sins are more useful as a diagnostic of ethical means than as a complete governance programme. Discuss. Answer in 150 words.",
        "answer": """Gandhi's published-and-endorsed list identifies moral decoupling: politics from principle, wealth from work, commerce from morality, knowledge from character and similar separations. It is a sharp diagnostic because it asks whether an attractive outcome has been pursued through exploitative, deceptive or dehumanising means.

A procurement office may deliver a project on time yet tolerate collusive bidding. The list exposes why target achievement cannot cleanse an unfair process. Likewise, science without humanity cautions a health-data project that obtains useful information without meaningful consent.

Its limitation is institutional. A moral warning does not specify audit design, appeal procedures, sanctions or protection for an honest official. The ARC's textual context also warrants care: the 1925 note presented the list as sent by a correspondent, and 'pleasure' appears where ARC prints 'leisure.'

Therefore, the list should guide ethical scrutiny, while codes, transparency, conflict-of-interest rules and citizen oversight supply enforceable governance. Character identifies the wrong; institutions help prevent and correct it.""",
    },
    {
        "marks": 15,
        "question": "Compare Gandhi's character-centred warning with Kautilya's opportunity-centred account of corruption. What balanced vigilance design follows for a district administration? Answer in 200 words.",
        "answer": """Gandhi and Kautilya illuminate different but complementary causes of corruption. Gandhi's Seven Social Sins warn that wealth, politics and commerce become corrupt when detached from conscience, work, principle and morality. His lens asks whether the actor has internalised ethical restraint. Kautilya's honey and fish analogies, quoted in ARC Annexure-I(2), begin from a harder administrative fact: officials handling public money face temptation and concealment, so character cannot be the sole safeguard.

A balanced district design should therefore combine moral formation with opportunity reduction. Induction and mentoring can discuss integrity, citizen dignity and conflicts of interest. Simultaneously, the administration should separate sanction, payment and verification roles; reconcile stock and beneficiary records; publish criteria; conduct proportionate risk-based audits; and preserve appeal and whistleblower channels. Honest performance should receive recognition and lawful continuity, reflecting Kautilya's positive element, while wrongful accumulation should be investigated through due process.

Neither pole is sufficient. Gandhi alone can become a sermon that ignores opaque incentives. Kautilya alone can become indiscriminate suspicion, punitive transfers and demoralisation of honest staff. Rotation without objective criteria is not vigilance.

The reasoned conclusion is values plus institutions: cultivate conscience for unobserved choices, but design transparent systems because even good people should not be asked to resist avoidable temptation alone.""",
    },
    {
        "marks": 15,
        "question": "How can Anekantavada and Aparigraha improve a civil servant's handling of a contested development project without producing indecision or anti-development romanticism? Answer in 200 words.",
        "answer": """Anekantavada teaches that a complex truth-claim has multiple standpoints; Aparigraha teaches non-possessiveness and restraint toward private gain. Together they can improve development administration by making consultation substantive and decision-making less vulnerable to capture.

In a contested renewable-energy or road project, Anekantavada requires the officer to hear landholders, women workers, Scheduled Tribe representatives, engineers, environmental experts and local bodies. The officer should disclose the evidence, distinguish facts from fears, consider alternatives and record reasons for the selected option. This is not a veto for every interest; it is epistemic humility before a lawful, timely decision.

Aparigraha adds a probity discipline. The officer must disclose relationships with bidders, recuse from conflicted files, reject gifts and ensure that compensation or rehabilitation decisions are not distorted by family, political or commercial gain. It directs attention from possession to trusteeship of public power.

The limits matter. Many-sidedness is not relativism: safety norms, rights and statutory mandates set non-negotiable boundaries. Non-possession is not refusal to build infrastructure or spend public funds; neglecting a needed project can also harm citizens.

Hence, Jain ethics supports development that is evidence-led, participatory and conflict-of-interest-free. Its mature administrative translation is a reasoned decision with safeguards, not endless consultation or moral display.""",
    },
    {
        "marks": 20,
        "question": "Leader-based ethics can humanise public administration, but it can also obscure institutional responsibility. Critically examine with reference to Gandhi, Vivekananda, Savitribai Phule and A.P.J. Abdul Kalam. Answer in 250 words.",
        "answer": """Leader-based ethics humanises administration by converting abstract values into memorable moral tests. Gandhi's Seven Social Sins warn an officer against commerce without morality or politics without principle; they make means as important as targets. Vivekananda's traceable 2024 teaching on learning from others without becoming them supports contextual adaptation rather than borrowed prestige. Savitribai Phule's 1848 Bhide Wada girls' school demonstrates that equality requires institution-building, not sympathetic rhetoric. Kalam's popularly used righteousness-to-peace chain encourages an officer to see personal integrity as socially consequential.

These lessons can improve public service. A district adapting an e-governance platform should retain transparency but add local-language and assisted access. A girls' education plan should move beyond celebration to safe transport, teachers and re-entry support. An officer confronted by a gift from a bidder can use Gandhi's means-ends test before any formal violation occurs.

However, exemplary names are not a substitute for constitutional design. Gandhi's list does not specify audit trails or appeal systems. Kalam's chain is an aspiration, not proof that private virtue alone causes national order; moreover, he credited it to Sathya Sai Baba in a 2007 European Parliament address. The 2025 Vivekananda law-and-morality wording is not traceable to the Complete Works, so an answer must analyse the idea rather than invent provenance. Hero worship can silence affected voices, reduce a dilemma to biography, or excuse officials who profess noble motives while breaching procedure.

The proper method is translation: state the teaching, identify a decision rule, use an Indian illustration, and add institutional safeguards. The verdict is qualified: exemplars make ethical imagination vivid, but accountable governance needs transparent rules, evidence, participation and remedies alongside character.""",
    },
    {
        "marks": 20,
        "question": "Evaluate Mission Karmayogi as an institutional bridge between human values and citizen-centred public service. What can it enable, and what must not be claimed from it? Answer in 250 words.",
        "answer": """Mission Karmayogi, under the National Programme for Civil Services Capacity Building, is relevant to human values because it shifts capacity-building attention from a narrow rules orientation toward roles, competencies and the citizen-government interface. DoPT's NPCSCB framework includes functional and behavioural competencies, while iGOT provides a learning platform. This creates an institutional route through which empathy, integrity, problem-solving and duty can be practised alongside technical capability.

Its promise is visible at the service-delivery level. A role-based module can help a citizen-facing official recognise accessibility barriers, communicate reasons for a decision, manage conflict and use a grievance system responsibly. Learning may be connected to mentoring, field reflection and redesign of a pension, health or land-service workflow. The Basic owner reports figures dated 6 February 2026: 1.49 crore users, 4,342 courses, 7.26 crore completions and 23 languages. These facts demonstrate reach and multilingual availability.

But reach is not internalisation. A completed course does not prove that an officer will resist a conflicted contractor, treat a claimant with dignity or report an improper order. Behaviour can be performed for a dashboard. Nor should an answer invent a general APAR linkage: the owner expressly says not to claim one without a service-specific DoPT order.

Mission Karmayogi should therefore be supplemented by fair workload design, transparent discretion, citizen feedback, ethical leadership, conflict-of-interest safeguards and due-process accountability. Its achievement is to make values learnable and role-relevant; its limit is that character and culture are tested in real choices. The reasoned verdict is that it is a valuable bridge, not a certificate of ethical governance in every service setting.""",
    },
)

ASCII_PANELS = (
    {
        "title": "1. Where values come from and how they become character",
        "structural_type": "formation-chain",
        "nodes": (
            "Values are enduring beliefs about what is worthwhile.",
            "Family provides early models of honesty and care.",
            "Schools translate ideals into repeated fair practice.",
            "Culture and peers can reinforce or corrode values.",
            "Leaders offer memorable examples rather than complete solutions.",
            "Lived hardship can test and revise inherited commitments.",
            "Institutions reward some conduct and discourage other conduct.",
            "Internalisation is visible when conduct remains ethical unobserved.",
        ),
        "verdict": "Values are socially formed, repeatedly tested, and never safely assumed to be fixed.",
        "answer_use": "Use as the opening mechanism for value-inculcation answers.",
    },
    {
        "title": "2. Turning values into public-service choices",
        "structural_type": "translation-ladder",
        "nodes": (
            "Honesty requires accurate records rather than favourable figures.",
            "Compassion requires fair access rather than discretionary favour.",
            "Courage requires resisting improper pressure through lawful channels.",
            "Self-discipline requires refusing temptation under discretion.",
            "Duty requires timely and competent service to citizens.",
            "Reasoned records make values reviewable in public office.",
            "Procedures protect values when pressure becomes intense.",
            "Citizen outcomes test whether ethical intent became public value.",
        ),
        "verdict": "A value earns administrative meaning only when it changes a defensible decision.",
        "answer_use": "Convert any abstract value into a named administrative action.",
    },
    {
        "title": "3. Gandhi: keeping means and ends ethically connected",
        "structural_type": "means-ends-diagnostic",
        "nodes": (
            "Politics without principles detaches power from public purpose.",
            "Wealth without work detaches gain from fair contribution.",
            "Pleasure or leisure without conscience detaches enjoyment from restraint.",
            "Knowledge without character detaches learning from responsibility.",
            "Commerce without morality detaches exchange from fairness.",
            "Science without humanity detaches capability from dignity.",
            "Worship without sacrifice detaches belief from ethical conduct.",
            "ARC prints leisure while the 1925 note uses pleasure.",
        ),
        "verdict": "Test not merely whether an end was achieved, but whether its means respected conscience.",
        "answer_use": "Apply to procurement, data consent, political conduct, or target-driven governance.",
    },
    {
        "title": "4. Learning courage and calm from Indian exemplars",
        "structural_type": "paired-lessons",
        "nodes": (
            "Vivekananda favours learning from others without becoming them.",
            "Adaptation preserves a useful reform while fitting local conditions.",
            "Sardar Patel's UPSC-attributed line joins faith to strength.",
            "Conviction needs competence, courage and organised capacity.",
            "Thiruvalluvar values composure amid adversity.",
            "Equanimity improves assessment and communication during crisis.",
            "Calm leadership must still act decisively and lawfully.",
            "Quotation attribution must not be overstated without primary evidence.",
        ),
        "verdict": "Learn openly, act capably, and remain composed without confusing calm with inaction.",
        "answer_use": "Use for reform adaptation, disaster leadership, and courage-under-pressure answers.",
    },
    {
        "title": "5. Mahavir: many-sided truth and non-possession",
        "structural_type": "doctrine-to-governance",
        "nodes": (
            "Mahavir's five Mahavratas include Ahimsa and Satya.",
            "Asteya rejects taking what is not rightfully due.",
            "Brahmacharya is separately enumerated in Mahavir's tradition.",
            "Aparigraha requires non-possessiveness and restraint.",
            "Anekantavada treats complex truth-claims as many-sided.",
            "Syadvada requires conditional and standpoint-aware assertion.",
            "Consultation improves evidence before a public decision.",
            "Many-sidedness does not cancel moral or legal judgement.",
        ),
        "verdict": "Listen widely and restrain private gain, then decide with reasons.",
        "answer_use": "Apply to land, environment, conflict of interest, and pluralism questions.",
    },
    {
        "title": "6. Kautilya and the design of corruption controls",
        "structural_type": "risk-control-loop",
        "nodes": (
            "Officials handling money face temptation like honey on a tongue.",
            "Concealed embezzlement resembles fish drinking water.",
            "Opportunity and secrecy make character-only solutions inadequate.",
            "Separation of duties reduces concentrated discretion.",
            "Reconciliation and risk-based audit improve detectability.",
            "Transparent criteria constrain arbitrary transfer and reward.",
            "Wrongful accumulation requires due-process investigation.",
            "Just wealth creation merits continuity and positive recognition.",
        ),
        "verdict": "Vigilance should reduce opportunity while protecting and rewarding honest service.",
        "answer_use": "Build a balanced anti-corruption paragraph with systems and incentives.",
    },
    {
        "title": "7. Duty without craving credit: Nishkama karma",
        "structural_type": "duty-boundary",
        "nodes": (
            "Nishkama karma requires action without attachment to personal fruit.",
            "It preserves effort even when recognition is uncertain.",
            "It requires concern for whether citizens receive the service.",
            "It rejects personal credit as the purpose of public work.",
            "It does not authorise indifference to outcomes.",
            "It does not require compliance with unlawful orders.",
            "It does not make chronic burnout an ethical ideal.",
            "Fulfilment arises from meaningful and accountable service.",
        ),
        "verdict": "Serve fully, measure public outcomes, and remain unattached to private reward.",
        "answer_use": "Use for duty, responsibility, fulfilment, and work-culture answers.",
    },
    {
        "title": "8. Reform through education: Savitribai Phule and Kalam",
        "structural_type": "bottom-up-institutional",
        "nodes": (
            "Savitribai Phule co-founded the Bhide Wada girls' school in 1848.",
            "Education attacks exclusion through durable access and institutions.",
            "Gender equality needs safety, support and opportunity beyond slogans.",
            "Kalam used a righteousness-to-peace ethical chain.",
            "Kalam credited that chain to Sathya Sai Baba in 2007.",
            "Personal integrity can influence family and civic conduct.",
            "Individual virtue alone cannot prove national causation.",
            "Institutional reform converts aspiration into sustained equality.",
        ),
        "verdict": "Ethical transformation begins with persons but endures through inclusive institutions.",
        "answer_use": "Use for gender equality, education, social reform, and integrity answers.",
    },
    {
        "title": "9. How to use a leader without hero-worship",
        "structural_type": "exemplar-checklist",
        "nodes": (
            "State the teaching precisely before applying it.",
            "Identify the public value and competing duty involved.",
            "Translate the teaching into a concrete decision rule.",
            "Use a specific Indian administrative illustration.",
            "Name the procedure that checks discretionary misuse.",
            "Distinguish a source-grounded fact from analytical inference.",
            "Acknowledge a provenance or contextual limitation where relevant.",
            "Conclude with a qualified rather than absolute verdict.",
        ),
        "verdict": "An exemplar guides judgement; it does not replace evidence, law, or institutional design.",
        "answer_use": "Use as the quality-control sequence for quotation and thinker answers.",
    },
    {
        "title": "10. Writing quotation answers that earn GS-IV marks",
        "structural_type": "answer-spine",
        "nodes": (
            "Restate the quotation's ethical core in one clear sentence.",
            "Give only the brief context needed for the present question.",
            "Translate the idea into a governance mechanism.",
            "Show one Indian illustration doing analytical work.",
            "Explain how the mechanism benefits citizens or public trust.",
            "State the limit, trade-off, or attribution caution.",
            "Do not replace analysis with a leader's biography.",
            "Close with an ethical rule joined to institutional safeguards.",
        ),
        "verdict": "Quotation questions reward applied ethics, not memory or reverence.",
        "answer_use": "Follow this sequence for every 10-mark quotation response.",
    },
    {
        "title": "11. MCQ and trap repair",
        "structural_type": "contrast-matrix",
        "nodes": (
            "Internalisation is not conduct displayed only for appraisal.",
            "Values are broader than object-specific attitudes.",
            "Anekantavada is not moral relativism or indecision.",
            "Aparigraha is not neglect of legitimate public spending.",
            "Nishkama karma is not indifference to citizen outcomes.",
            "Kautilya is not a warrant for arbitrary surveillance.",
            "Gandhi's list has a pleasure and leisure textual variation.",
            "UPSC attribution does not by itself prove primary provenance.",
        ),
        "verdict": "Close options fail when they turn a qualified ethical concept into an absolute claim.",
        "answer_use": "Use for prelims elimination and final answer self-audit.",
    },
    {
        "title": "12. PYQ and answer synthesis",
        "structural_type": "integrated-revision-flow",
        "nodes": (
            "2024 tested Vivekananda, Patel and Kant through present-context translation.",
            "2025 tested Thiruvalluvar, William James and Vivekananda quotations.",
            "2025 also tested Mahavir's teachings and devotion to duty.",
            "Use traceable provenance when the owner provides it.",
            "Treat disputed wording as a UPSC attribution rather than a primary citation.",
            "Pair Gandhi's character warning with Kautilya's control design.",
            "Pair Mahavir's consultation with a lawful recorded decision.",
            "Pair Mission Karmayogi learning reach with conduct-based safeguards.",
        ),
        "verdict": "The highest-scoring answer moves from idea to mechanism, example, qualification and verdict.",
        "answer_use": "Use as the final revision map before PYQ practice.",
    },
)

CURRENT_ANCHOR = {
    "title": "Mission Karmayogi: values made role-relevant, not automatically internalised",
    "verified_facts": (
        "DoPT's NPCSCB focuses on functional and behavioural competencies.",
        "The approach addresses the citizen-government interface.",
        "Its stated orientation is a shift from rules to roles.",
        "iGOT is the learning platform in this capacity-building linkage.",
        "The Basic owner reports figures dated 6 February 2026: 1.49 crore users, 4,342 courses, 7.26 crore completions and 23 languages.",
    ),
    "administrative_link": "Use it to show how value education can be embedded in role-based learning, behavioural practice and citizen-facing service design.",
    "limit": "The figures demonstrate reach and completions, not ethical internalisation or a general APAR linkage. Do not invent an APAR linkage without a service-specific DoPT order.",
}

CURRENT_SOURCE_URLS = (
    "https://dopt.gov.in/schemes/national-programme-civil-services-and-capacity-building-npcscb-mission-karmayogi",
    "https://igotkarmayogi.gov.in/",
    "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2226246&reg=3&lang=1",
)

SOURCE_CAVEAT = (
    "Use the local Basic owner as the controlling source. Gandhi's 1925 list was published and "
    "endorsed by Gandhi but presented as sent by a correspondent; its original wording has "
    "'pleasure' where ARC Box 2.8 prints 'leisure'. The 2024 Patel line, 2025 William James line, "
    "and 2025 Vivekananda law-morality line are UPSC attributions not traced to primary sources in "
    "the owner. Thiruvalluvar's 2025 wording is a modern paraphrase of Tirukkural 623. Kalam used "
    "the righteousness-to-peace chain while crediting Sathya Sai Baba. Do not turn any caution into "
    "a fabricated citation."
)

REGISTER_SUPPLEMENT = (
    "Rapid recall: Values are learned through family, school, culture, peers, exemplars and "
    "experience; internalisation survives absence of audit. Gandhi tests means-ends separation; "
    "Vivekananda supports adapted learning; Patel joins conviction to capacity; Thiruvalluvar joins "
    "calm to action; Mahavir supplies Ahimsa, Satya, Asteya, Brahmacharya, Aparigraha, Anekantavada "
    "and Syadvada; Kautilya joins temptation controls to incentives; Nishkama karma rejects attachment "
    "to personal reward, not responsibility for outcomes. Savitribai Phule demonstrates institution-"
    "building for equality. Mission Karmayogi supplies a role-and-competency training channel, not "
    "proof of conduct. Answer spine: idea -> mechanism -> Indian illustration -> limitation -> verdict."
)
