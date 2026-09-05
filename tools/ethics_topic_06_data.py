"""Learner-v2 source data: Ethics Topic 06, Indian Moral Thinkers and Philosophers."""

SESSION_TITLES = (
    "The realist-idealist spectrum in Indian moral thought",
    "Kautilya: structural realism and anti-corruption design",
    "Buddha: the Middle Path as an administrative decision-procedure",
    "Gandhi: ends-means unity, trusteeship and Seven Social Sins",
    "Vivekananda: Practical Vedanta and Daridra Narayana",
    "Basava: Kayaka, Dasoha and the Anubhava Mantapa",
    "Guru Nanak: Kirat Karo, Vand Chhako and public-resource ethics",
    "Mahavir: Mahavratas, Anekantavada and multi-stakeholder ethics",
    "Ambedkar: constitutional morality, equality and fraternity",
    "Social capital, comparative synthesis and exam application",
)

SESSION_GROUPS = (
    (1, 2),
    (3,),
    (4,),
    (5,),
    (6,),
    (7,),
    (8,),
    (9,),
    (10,),
    (11, 12, 13),
)

MCQ_ITEMS = (
    # --- Family A: structural realism vs moral idealism ---
    {
        "label": "Kautilya assumes temptation is structural",
        "statement": (
            "Kautilya's Arthashastra treats official corruption as an opportunity-driven "
            "structural phenomenon rather than a personal moral failing; the honey-and-poison "
            "passage (Kangle 2.9.32, cited in ARC Annexure-I(2)) argues that an official "
            "dealing with the king's money can no more avoid tasting it than a tongue can "
            "avoid tasting honey or poison placed on its surface."
        ),
        "scenario_a": (
            "A state government designs a procurement system with mandatory dual-custody of "
            "financial approvals and automatic rotation of purchasing officers every two years. "
            "Which Indian moral thinker's structural premise most directly justifies this "
            "design over a purely pledge-based integrity programme?"
        ),
        "scenario_b": (
            "A department head insists that good character training alone will eliminate "
            "corruption and resists instituting surprise audits. Which classical Indian "
            "passage warns that this reliance on moral goodwill alone is insufficient?"
        ),
        "family": "structural realism vs moral idealism",
        "group": "structural realism vs moral idealism",
    },
    {
        "label": "Gandhi assumes moral transformation through self-purification",
        "statement": (
            "Gandhi's trusteeship and Satyagraha assume that moral transformation is possible "
            "through exemplar-based self-purification and non-violent persuasion; this idealist "
            "premise drives internal, character-based reform and contrasts with Kautilya's "
            "reliance on external control mechanisms."
        ),
        "scenario_a": (
            "A senior district official leads by personal example, refusing gifts publicly and "
            "expecting subordinates to follow suit without any formal surveillance mechanism. "
            "Which Indian moral framework underpins this approach and what is its structural "
            "limitation?"
        ),
        "scenario_b": (
            "A civil servant argues that integrity pledges and public commitments by senior "
            "leaders are more effective than vigilance machinery in building a corruption-free "
            "organisation. Which thinker's idealist premise does this echo and what is the "
            "ARC's implicit caution?"
        ),
        "family": "structural realism vs moral idealism",
        "group": "structural realism vs moral idealism",
    },
    {
        "label": "Modern anti-corruption is Kautilyan in design but Gandhian in aspiration",
        "statement": (
            "India's modern anti-corruption architecture is structurally closer to Kautilya's "
            "control-based realism (statutory controls, vigilance machinery, Lokpal) than to "
            "Gandhi's exemplar-based idealism, yet invokes Gandhian language of integrity as "
            "a civilisational value in its public rhetoric."
        ),
        "scenario_a": (
            "A Lokpal investigation relies on asset-declaration analysis and bank-transaction "
            "audits while the official campaign poster quotes Gandhian values. Which analytical "
            "claim about India's dual ethical heritage does this illustrate?"
        ),
        "scenario_b": (
            "A reform commission recommends both a statutory Lokpal with investigative powers "
            "and a Gandhian code-of-ethics module for all civil servants. Why does the "
            "commission's package embody a synthesis rather than a contradiction?"
        ),
        "family": "structural realism vs moral idealism",
        "group": "structural realism vs moral idealism",
    },
    {
        "label": "A regime built entirely on surveillance demoralises honest officials",
        "statement": (
            "An anti-corruption regime built entirely on Kautilyan surveillance without any "
            "Gandhian or Vivekanandan appeal to service-motivation risks demoralising honest "
            "officials; the ARC cautions against excessive suspicion that discourages "
            "legitimate risk-taking."
        ),
        "scenario_a": (
            "After a corruption scandal a state government introduces mandatory CCTV in every "
            "office, keystroke logging and weekly asset checks. Honest officers feel distrusted "
            "and begin avoiding any discretionary decision. Which analytical boundary explains "
            "this backfire?"
        ),
        "scenario_b": (
            "A district collector pairs vigilance mechanisms with a mentoring programme, public "
            "recognition for exemplary service and protected dissent channels. Which synthesis "
            "principle is she applying to avoid the demoralisation risk?"
        ),
        "family": "structural realism vs moral idealism",
        "group": "structural realism vs moral idealism",
    },
    # --- Family B: service as duty/devotion ---
    {
        "label": "Vivekananda's Practical Vedanta makes service a spiritual duty",
        "statement": (
            "Vivekananda applies Advaita's non-dual metaphysics (the self in all beings is "
            "one) to ground an ethic of service: serving the deprived is serving the divine, "
            "collapsing the sacred-secular distinction in public-service motivation through "
            "the concept of Daridra Narayana."
        ),
        "scenario_a": (
            "A welfare officer treats slum-resettlement beneficiaries with the same courtesy "
            "and procedural care as elite applicants, viewing service to the poorest as an "
            "expression of devotion rather than bureaucratic obligation. Which thinker's "
            "framework best explains this orientation?"
        ),
        "scenario_b": (
            "A training module tells officers that public service is a job like any other "
            "and that emotional engagement with beneficiaries is unprofessional. Which Indian "
            "philosophical framework directly challenges this detachment model?"
        ),
        "family": "service as duty/devotion",
        "group": "service as duty/devotion",
    },
    {
        "label": "Basava's Kayaka assigns equal spiritual worth to all honest labour",
        "statement": (
            "Basava's principle Kayakave Kailasa holds that dignified, honest productive work "
            "is itself the divine abode; all honest labour, regardless of caste, carries equal "
            "spiritual and social worth, underpinning an anti-discrimination service ethic "
            "that anticipates Articles 17 and 23 of the Indian Constitution."
        ),
        "scenario_a": (
            "A municipality assigns street sweepers the same benefits, protective equipment "
            "and recognition ceremonies as administrative staff, citing equal dignity of all "
            "public service. Which 12th-century thinker's ethical principle most directly "
            "supports this policy?"
        ),
        "scenario_b": (
            "A government office informally treats manual-labour roles as lower in dignity "
            "than desk-based roles, denying sanitation workers access to the common canteen. "
            "Which Indian moral thinker's core teaching does this workplace practice violate?"
        ),
        "family": "service as duty/devotion",
        "group": "service as duty/devotion",
    },
    {
        "label": "Guru Nanak models honest earning plus equitable sharing",
        "statement": (
            "Guru Nanak's Kirat Karo (earn through honest labour) and Vand Chhako (share with "
            "others) together model an ethic directly applicable to honest use of, and equitable "
            "sharing of, public resources; Kirat Karo opposes rent-seeking and corruption while "
            "Vand Chhako supports progressive, equity-oriented allocation."
        ),
        "scenario_a": (
            "A finance officer designs a budget that prioritises revenue through transparent "
            "tax collection and allocates a disproportionately higher share to healthcare in "
            "underserved districts. Which Indian thinker's paired principles most closely "
            "map to this honest-collection-plus-equitable-expenditure ethic?"
        ),
        "scenario_b": (
            "A public servant earns an honest salary but opposes any redistribution of "
            "departmental resources toward weaker sections. Which component of the relevant "
            "Indian thinker's ethical framework is he partially embracing and which is he "
            "rejecting?"
        ),
        "family": "service as duty/devotion",
        "group": "service as duty/devotion",
    },
    {
        "label": "All three refuse a charity model in favour of a dignity model",
        "statement": (
            "Vivekananda's Daridra Narayana, Basava's Kayaka and Guru Nanak's Vand Chhako "
            "all refuse a charity model of welfare (in which the giver is superior to the "
            "receiver) in favour of a dignity model (in which service to the deprived, or "
            "the deprived's own labour, carries equal spiritual and civic worth)."
        ),
        "scenario_a": (
            "A welfare scheme requires beneficiaries to display their below-poverty-line "
            "status on public notice boards as a condition of receiving benefits. Which "
            "shared ethical principle among Vivekananda, Basava and Nanak does this "
            "stigmatising design violate?"
        ),
        "scenario_b": (
            "A district redesigns its pension-delivery process so that elderly beneficiaries "
            "receive doorstep service without queuing or producing humiliating eligibility "
            "proof. Which convergence among three Indian thinkers is being operationalised?"
        ),
        "family": "service as duty/devotion",
        "group": "service as duty/devotion",
    },
    # --- Family C: balance and proportionality ---
    {
        "label": "Buddha's Middle Path is a decision-procedure, not a static virtue",
        "statement": (
            "The Middle Path (Madhyama Pratipada) is best understood not as a static virtue "
            "of moderation but as a decision-procedure: before acting, test whether a "
            "contemplated administrative response is an over-reaction (excessive, punitive, "
            "populist crackdown) or an under-reaction (complacent inaction) and correct "
            "toward proportionality."
        ),
        "scenario_a": (
            "After food-safety violations at a single establishment, a district magistrate "
            "orders all restaurants in the city shut down for a month. A colleague suggests "
            "doing nothing because enforcement is unpopular. Which decision-procedure tests "
            "both responses against a principled standard?"
        ),
        "scenario_b": (
            "A civil servant facing a land dispute is told to 'be balanced' but receives no "
            "operational guidance on what balance means. Which Indian philosophical framework "
            "converts balance from a vague instruction into a testable procedure?"
        ),
        "family": "balance and proportionality",
        "group": "balance and proportionality",
    },
    {
        "label": "The Eightfold Path maps to official conduct standards",
        "statement": (
            "The Eightfold Path's Right Action, Right Livelihood and Right Mindfulness map "
            "onto lawful conduct, honest occupation and self-aware decision-making in public "
            "administration; the Middle Path counsels against both reckless discretion and "
            "paralytic over-caution in administrative choice."
        ),
        "scenario_a": (
            "A revenue officer mindfully reviews her own assumptions before rejecting a "
            "tribal land-claim application, ensuring that her decision is based on evidence "
            "rather than inherited prejudice. Which element of the Eightfold Path is she "
            "applying to her administrative role?"
        ),
        "scenario_b": (
            "An officer accepts a posting in a department whose revenue-generation methods "
            "he considers unethical but takes no action to seek a transfer or raise the "
            "concern internally. Which Eightfold Path component is relevant to evaluating "
            "his occupational choice?"
        ),
        "family": "balance and proportionality",
        "group": "balance and proportionality",
    },
    {
        "label": "Mahavir's Anekantavada supports multi-stakeholder consultation",
        "statement": (
            "Mahavir's Anekantavada (many-sidedness of truth) holds that no single perspective "
            "captures the whole truth; administratively, this operationalises listening to "
            "competing legitimate viewpoints before deciding, supporting multi-stakeholder "
            "consultation in policy design."
        ),
        "scenario_a": (
            "A district collector mediating a land dispute between a tribal community, an "
            "industrial developer and an environmental group deliberately holds separate "
            "hearings with each before synthesising a decision. Which Indian thinker's "
            "epistemological doctrine supports this process?"
        ),
        "scenario_b": (
            "A policymaker dismisses minority objections to a highway project, saying the "
            "majority benefit is the only relevant perspective. Which Jain doctrine warns "
            "against this single-perspective approach?"
        ),
        "family": "balance and proportionality",
        "group": "balance and proportionality",
    },
    {
        "label": "Proportionality prevents both populist crackdowns and inaction",
        "statement": (
            "The proportionality check, grounded in the Middle Path, prevents both populist "
            "crackdowns (over-reaction driven by short-term political pressure) and complacent "
            "inaction (under-reaction driven by risk-aversion or indifference); it maps "
            "directly onto the case-study method's proportionality test."
        ),
        "scenario_a": (
            "After a viral social-media outrage, a state government demolishes an entire "
            "market complex for one building violation instead of issuing targeted notices. "
            "Which ethical decision-procedure would have prevented this disproportionate "
            "response?"
        ),
        "scenario_b": (
            "A sub-divisional magistrate knows that illegal sand mining is occurring but "
            "takes no action because previous enforcement led to political backlash. Which "
            "ethical framework identifies this as the opposite extreme that is equally "
            "problematic?"
        ),
        "family": "balance and proportionality",
        "group": "balance and proportionality",
    },
    # --- Family D: constitutional and institutional anchoring ---
    {
        "label": "Ambedkar's constitutional morality demands reverence for constitutional forms",
        "statement": (
            "Ambedkar invoked constitutional morality in the Constituent Assembly on "
            "4 November 1948, quoting historian George Grote: a paramount reverence for "
            "the forms of the Constitution, enforcing obedience to authority acting under "
            "and within these forms yet combined with the habit of open speech and "
            "unrestrained censure of those very authorities as to all their public acts."
        ),
        "scenario_a": (
            "A chief minister pressures a district magistrate to bypass environmental-"
            "clearance procedures for a politically important project. The officer insists "
            "on following the statutory process despite the pressure. Which concept from "
            "which Indian thinker grounds her refusal?"
        ),
        "scenario_b": (
            "A citizen argues that constitutional morality means blind obedience to any "
            "law regardless of its content. Which dimension of Ambedkar's formulation, "
            "drawn from Grote, includes the right of unrestrained censure and thus "
            "contradicts this reading?"
        ),
        "family": "constitutional and institutional anchoring",
        "group": "constitutional and institutional anchoring",
    },
    {
        "label": "Ambedkar warned of a life of contradictions",
        "statement": (
            "In his Constituent Assembly speech of 25 November 1949, Ambedkar warned that "
            "India was entering a life of contradictions: political equality (one person, "
            "one vote) alongside continuing social and economic inequality; he cautioned "
            "that this contradiction must be removed at the earliest or those suffering "
            "from inequality will blow up the structure of political democracy."
        ),
        "scenario_a": (
            "A district with universal adult franchise still has female literacy below 30 "
            "per cent and landless labourers comprising 60 per cent of the population. A "
            "civil servant designing welfare interventions invokes which Indian thinker's "
            "specific warning to justify targeted affirmative action?"
        ),
        "scenario_b": (
            "A colleague argues that political equality through elections is sufficient for "
            "democracy and that social inequality is a private matter. Which specific "
            "constitutional-assembly speech refutes this claim and identifies the "
            "resulting risk?"
        ),
        "family": "constitutional and institutional anchoring",
        "group": "constitutional and institutional anchoring",
    },
    {
        "label": "Fraternity makes constitutional values self-sustaining",
        "statement": (
            "Ambedkar named fraternity — a sense of common brotherhood of all Indians — as "
            "necessary because liberty and equality without fraternity would need a policeman "
            "to enforce them; fraternity is what makes constitutional values self-sustaining "
            "rather than externally coerced."
        ),
        "scenario_a": (
            "A state enforces anti-discrimination laws strictly but communities remain deeply "
            "segregated and hostile. A social reformer argues that legal enforcement alone is "
            "insufficient without a shared sense of belonging. Which Ambedkar concept does "
            "the reformer invoke?"
        ),
        "scenario_b": (
            "A civil servant wonders why high rates of prosecution under atrocity-prevention "
            "laws have not reduced caste violence. Which Ambedkar principle explains why "
            "legal coercion without underlying social solidarity is structurally fragile?"
        ),
        "family": "constitutional and institutional anchoring",
        "group": "constitutional and institutional anchoring",
    },
    {
        "label": "Institutional safeguards embed distrust of majoritarian goodwill alone",
        "statement": (
            "Ambedkar's design philosophy embedded minority and SC-ST safeguards, judicial "
            "review and the fundamental-rights chapter precisely because he distrusted "
            "majoritarian goodwill alone to protect equality; durable ethical commitments "
            "need institutional containers, not moral exhortation alone."
        ),
        "scenario_a": (
            "A parliamentary majority proposes to amend a fundamental right that protects "
            "religious minorities. An opposition member argues that the basic-structure "
            "doctrine exists precisely for such situations. Which Indian thinker's design "
            "philosophy does this argument reflect?"
        ),
        "scenario_b": (
            "A colleague says India should trust the goodwill of the majority to protect "
            "minority rights without needing constitutional safeguards. Which Indian "
            "thinker's explicit design rationale in the Constituent Assembly contradicts "
            "this position?"
        ),
        "family": "constitutional and institutional anchoring",
        "group": "constitutional and institutional anchoring",
    },
    # --- Family E: attribution and source cautions ---
    {
        "label": "Gandhi's Seven Social Sins: leisure versus pleasure wording split",
        "statement": (
            "Gandhi's Seven Social Sins as printed in ARC Box 2.8 include 'leisure without "
            "conscience'; however, the original Young India note of 22 October 1925 reads "
            "'pleasure without conscience'. Gandhi received the list from a correspondent "
            "and published it without claiming personal authorship. Use the ARC wording in "
            "ARC-cited answers but note the discrepancy."
        ),
        "scenario_a": (
            "A candidate quotes 'pleasure without conscience' from Gandhi and is challenged "
            "by a peer who insists the ARC says 'leisure without conscience'. Which source "
            "caveat resolves this and what is the defensible exam approach?"
        ),
        "scenario_b": (
            "An ethics training module attributes the Seven Social Sins entirely to Gandhi's "
            "original formulation. Which provenance correction should the module make to be "
            "historically accurate?"
        ),
        "family": "attribution and source cautions",
        "group": "attribution and source cautions",
    },
    {
        "label": "Anubhava Mantapa is tradition-attested, not securely dated",
        "statement": (
            "Basava (12th century, Kalachuri kingdom under Bijjala) is associated with the "
            "Anubhava Mantapa, an assembly of Lingayat sharanas for spiritual and social "
            "discourse open across caste and gender; it should be presented as a tradition-"
            "attested assembly, not as a securely dated founded institution, and the popular "
            "'first parliament of the world' formulation must be avoided."
        ),
        "scenario_a": (
            "A candidate writes that Basava 'established the world's first parliament in the "
            "12th century.' Which specific attribution caution applies and how should the "
            "claim be restated for exam safety?"
        ),
        "scenario_b": (
            "A textbook describes the Anubhava Mantapa as a 'securely dated democratic "
            "institution founded in 1160 CE.' Which qualification is needed to make this "
            "historically defensible?"
        ),
        "family": "attribution and source cautions",
        "group": "attribution and source cautions",
    },
    {
        "label": "Guru Nanak's three pillars is later pedagogical packaging",
        "statement": (
            "Guru Nanak's three pillars — Naam Japna, Kirat Karo, Vand Chhako — have a firm "
            "scriptural basis in the Guru Granth Sahib (Angs 8 and 1245), but the 'three "
            "pillars' phrasing itself is later pedagogical packaging, not a verbatim triad "
            "of Guru Nanak's own words."
        ),
        "scenario_a": (
            "A candidate attributes the exact phrase 'three pillars' to Guru Nanak as a "
            "direct quotation from the Guru Granth Sahib. Which provenance correction is "
            "needed?"
        ),
        "scenario_b": (
            "An examiner asks whether Guru Nanak explicitly formulated a three-part ethical "
            "system. How should a candidate frame the answer to use the content accurately "
            "without fabricating a primary-source quotation?"
        ),
        "family": "attribution and source cautions",
        "group": "attribution and source cautions",
    },
    {
        "label": "2025 Vivekananda quotation not traceable to Complete Works",
        "statement": (
            "The 2025 GS-IV Q3(c) Vivekananda quotation on the strength of a society being "
            "in the morality of its people is attributed by UPSC but is not traceable to the "
            "Complete Works of Swami Vivekananda; it should be presented with an 'attributed "
            "by UPSC' caveat rather than as a verified primary-source quotation."
        ),
        "scenario_a": (
            "A candidate writing a practice answer cites 'as Vivekananda said in his Complete "
            "Works' for the 2025 Q3(c) quotation. Which correction preserves exam utility "
            "without fabricating a primary source?"
        ),
        "scenario_b": (
            "A coaching institute's handout lists the 2025 Q3(c) line as Volume III of the "
            "Complete Works. Which verification step should a student take before accepting "
            "this attribution?"
        ),
        "family": "attribution and source cautions",
        "group": "attribution and source cautions",
    },
    # --- Family F: social capital and synthesis ---
    {
        "label": "Social capital is networks of trust enabling collective action",
        "statement": (
            "Social capital refers to the networks of trust, reciprocity and civic norms "
            "among citizens and between citizens and institutions that enable collective "
            "action without requiring constant external enforcement; associated in standard "
            "usage with Robert Putnam's distinction between bonding and bridging capital."
        ),
        "scenario_a": (
            "A village where residents trust each other's testimony voluntarily participates "
            "in a social audit of MGNREGA works without any individual monetary incentive. "
            "Which concept explains why collective action occurs here without external "
            "enforcement?"
        ),
        "scenario_b": (
            "In a neighbouring village with deep factional divisions, a government-mandated "
            "social audit fails because no witness trusts the process or each other. Which "
            "concept's absence explains the failure?"
        ),
        "family": "social capital and synthesis",
        "group": "social capital and synthesis",
    },
    {
        "label": "Bridging social capital strengthens governance; bonding-only entrenches nepotism",
        "statement": (
            "Bridging social capital (across different groups and communities) strengthens "
            "governance by enabling inclusive collective action; bonding social capital "
            "(within a close-knit group) can entrench nepotism and gatekeeping against "
            "outsiders, meaning social capital strengthens governance only when it is "
            "bridging and inclusive."
        ),
        "scenario_a": (
            "A dominant-caste panchayat head uses strong community networks to secure "
            "development funds but channels them exclusively to his own community. Which "
            "analytical distinction explains why strong social capital here harms rather "
            "than helps governance?"
        ),
        "scenario_b": (
            "An inter-community women's self-help-group federation monitors local school "
            "attendance across caste lines and reports irregularities to the block office. "
            "Which type of social capital is at work and why does it strengthen governance?"
        ),
        "family": "social capital and synthesis",
        "group": "social capital and synthesis",
    },
    {
        "label": "Guru Nanak and Basava are classical antecedents of bridging social capital",
        "statement": (
            "Guru Nanak's Vand Chhako (sharing with others beyond one's own group) and "
            "Basava's Dasoha (sharing surplus in community service through caste-blind "
            "assemblies) are classical Indian antecedents of bridging social capital, "
            "connecting the Indian moral-thought register to the modern governance concept."
        ),
        "scenario_a": (
            "A district officer establishes a common community kitchen (langar model) at "
            "the tehsil office where citizens from all communities share meals during "
            "waiting periods. Which two Indian thinkers' principles is this design drawing "
            "on as historical antecedents?"
        ),
        "scenario_b": (
            "A scholar argues that bridging social capital is a purely Western concept with "
            "no Indian philosophical precedent. Which two classical Indian thinkers' "
            "principles serve as counter-examples?"
        ),
        "family": "social capital and synthesis",
        "group": "social capital and synthesis",
    },
    {
        "label": "MKSS social audits function because bridging social capital exists",
        "statement": (
            "MKSS-style social audits in Rajasthan and the broader jan sunwai (public hearing) "
            "model function precisely because a baseline of bridging social capital exists or "
            "is deliberately built; villagers trust the audit process and each other's testimony, "
            "making the informal complement to formal accountability architecture effective."
        ),
        "scenario_a": (
            "A state replicates the MKSS social-audit model in a region with deep inter-"
            "community mistrust and finds that no villager testifies. Which underlying "
            "condition is missing and what must be built before the formal process can work?"
        ),
        "scenario_b": (
            "A successful social audit in Rajasthan reveals significant MGNREGA fund "
            "diversion, with villagers freely testifying about irregularities. Which "
            "concept explains why the informal accountability mechanism succeeded here "
            "but fails elsewhere?"
        ),
        "family": "social capital and synthesis",
        "group": "social capital and synthesis",
    },
)

PYQS = (
    {
        "year": 2025,
        "question": (
            "Neutral rendering: Three quotations (Thiruvalluvar, William James, "
            "Vivekananda) and their present-day meaning."
        ),
        "marks": 10,
        "source_note": (
            "Routed from 2025 GS-IV Q3; neutral rendering used. Vivekananda Q3(c) "
            "attribution caution: the 'strength of a society... morality of its people' "
            "line is not traceable to the Complete Works of Swami Vivekananda."
        ),
        "answer": (
            "Vivekananda's attributed line — the strength of a society lies in the morality "
            "of its people, not merely in its laws — asserts that formal legal architecture "
            "alone cannot sustain good governance without an underlying moral culture.\n\n"
            "This echoes Practical Vedanta's core logic: if every citizen recognises the same "
            "self in all beings, social compliance arises from inner conviction rather than "
            "external coercion. A tax-compliance regime works better when citizens believe "
            "paying taxes is a moral duty, not merely a legal compulsion enforced by penalty.\n\n"
            "The administrative implication is that a civil servant must invest in building "
            "civic moral culture alongside enforcing rules. Social audits, citizen charters "
            "and participatory governance work best where social capital and moral norms are "
            "strong. The limit is that moral culture alone cannot substitute for institutional "
            "safeguards; Kautilya's realist caution remains necessary."
        ),
    },
    {
        "year": 2025,
        "question": (
            "Neutral rendering: (b) Teachings of Mahavir and their relevance "
            "in the contemporary world."
        ),
        "marks": 10,
        "source_note": (
            "Routed from 2025 GS-IV Q4(b); neutral rendering used. Cross-linked "
            "from Topic 02 (Mahavir detail)."
        ),
        "answer": (
            "Mahavir's core teachings comprise the five Mahavratas (Ahimsa, Satya, Asteya, "
            "Brahmacharya, Aparigraha) and the epistemological doctrine of Anekantavada "
            "(many-sidedness of truth) with its logical expression Syadvada (conditional "
            "predication).\n\n"
            "Contemporary relevance: Ahimsa extends beyond physical non-violence to "
            "non-exploitation in institutional design. Aparigraha (non-possessiveness) "
            "cautions against accumulation and nepotism in public office. Anekantavada "
            "supports multi-stakeholder consultation: a land-dispute mediator who hears "
            "tribal, industrial and environmental perspectives before deciding "
            "operationalises Mahavir's epistemology.\n\n"
            "Syadvada also disciplines official communication: conclusions should identify "
            "their evidentiary conditions instead of presenting a partial administrative "
            "view as absolute truth to affected communities.\n\n"
            "The limit: Anekantavada taken too far risks indecision. A wisdom-based "
            "cut-off point for deliberation is still required. Mahavir's framework "
            "provides the consultative process, not the decision rule."
        ),
    },
    {
        "year": 2024,
        "question": (
            "Neutral rendering: Three quotations of great thinkers and their "
            "present-day meaning."
        ),
        "marks": 10,
        "source_note": (
            "Routed from 2024 GS-IV Q3; neutral rendering used. Q3(a) is a confirmed "
            "Vivekananda quotation: 'Learn everything that is good from others, but bring "
            "it in, and in your own way absorb it; do not become others' (Complete Works, "
            "Vol. III)."
        ),
        "answer": (
            "Vivekananda's injunction — learn from others but absorb it in your own way — "
            "applies Practical Vedanta's selectivity to governance reform. India adopts "
            "international best practices (e-governance from Estonia, regulatory sandboxes "
            "from the UK) but must adapt them to its own institutional, cultural and "
            "constitutional context rather than transplanting them wholesale.\n\n"
            "A civil servant implementing a foreign-inspired welfare model must assess "
            "whether the underlying assumptions (digital literacy, institutional capacity, "
            "social trust) hold in the Indian district. Uncritical adoption risks "
            "implementation failure; complete rejection forfeits improvement.\n\n"
            "The administrative lesson is calibrated adoption: study the mechanism, "
            "test it against local conditions, and integrate what works into India's own "
            "governance architecture. This is consistent with Vivekananda's broader "
            "Practical Vedanta: universal truths exist but must be realised through one's "
            "own experience and context."
        ),
    },
    {
        "year": 2023,
        "question": (
            "Neutral rendering: (a) Major teachings of Guru Nanak and their "
            "contemporary relevance."
        ),
        "marks": 10,
        "source_note": (
            "Routed from 2023 GS-IV Q6(a); neutral rendering used."
        ),
        "answer": (
            "Guru Nanak's three standardly taught principles are Naam Japna (remembrance of "
            "the divine name, grounding ethical conduct in spiritual awareness), Kirat Karo "
            "(earn through honest labour) and Vand Chhako (share with others). The 'three "
            "pillars' phrasing is later pedagogical packaging; the scriptural basis is firm "
            "(Guru Granth Sahib, Angs 8 and 1245).\n\n"
            "Contemporary relevance: Kirat Karo directly opposes rent-seeking and corruption "
            "in public service. Vand Chhako supports progressive, equity-oriented allocation "
            "of public resources. Together they form a public-finance ethic: honest revenue "
            "collection (Kirat Karo analogue) paired with equitable expenditure (Vand Chhako "
            "analogue).\n\n"
            "Naam Japna adds an inward discipline: remembrance checks ego and keeps public "
            "authority oriented toward service rather than personal status.\n\n"
            "The limit: Nanak's ethic is a normative ideal, not a self-enforcing mechanism. "
            "It still requires institutional accountability architecture to translate into "
            "durable governance practice."
        ),
    },
    {
        "year": 2020,
        "question": (
            "Neutral rendering: (a) Most relevant teachings of Buddha today "
            "and why."
        ),
        "marks": 10,
        "source_note": (
            "Routed from 2020 GS-IV Q3(a); neutral rendering used."
        ),
        "answer": (
            "The Buddha's most administratively relevant teachings are the Middle Path "
            "(Madhyama Pratipada) and the Eightfold Path, particularly Right Action, Right "
            "Livelihood and Right Mindfulness.\n\n"
            "The Middle Path, understood as a decision-procedure, tests every administrative "
            "response against two extremes: over-reaction (punitive populist crackdown) and "
            "under-reaction (complacent inaction). A district magistrate handling a communal "
            "tension situation uses this test to avoid both provocative force and dangerous "
            "inaction, choosing proportionate preventive measures.\n\n"
            "Right Mindfulness requires self-aware decision-making: the officer examines her "
            "own biases before acting. Right Livelihood questions whether the means of "
            "governance are themselves ethical.\n\n"
            "The limit: the Middle Path provides the procedure for evaluating proportionality "
            "but does not prescribe the substantive standard. That requires constitutional "
            "values and legal frameworks to supply the normative content."
        ),
    },
    {
        "year": 2020,
        "question": (
            "Neutral rendering: Three quotations: (a) Vivekananda on selfless "
            "service and brotherhood; (b) Gandhi on finding self through service "
            "to others."
        ),
        "marks": 10,
        "source_note": (
            "Routed from 2020 GS-IV Q6; neutral rendering used. "
            "Parts (a) and (b) both route to this topic."
        ),
        "answer": (
            "Vivekananda's selfless-service teaching and Gandhi's 'finding oneself through "
            "service to others' converge on a single proposition: public service that is "
            "genuinely other-directed paradoxically fulfils the servant. Vivekananda grounds "
            "this in Practical Vedanta (serving the deprived is serving the divine), while "
            "Gandhi grounds it in Sarvodaya (welfare of all through self-purification).\n\n"
            "Administrative application: a welfare officer who treats beneficiaries as "
            "fellow citizens rather than charity cases operates in both registers "
            "simultaneously. She designs dignified service processes and finds professional "
            "meaning in the outcomes.\n\n"
            "Both therefore reject patronising charity: assistance must preserve agency, "
            "equality and the beneficiary's status as a rights-bearing citizen.\n\n"
            "The shared limit: selfless service is a motivational ideal, not an institutional "
            "mechanism. Without accountability architecture, even well-motivated officers can "
            "drift into paternalism. The synthesis requires pairing internal motivation with "
            "external accountability."
        ),
    },
    {
        "year": 2018,
        "question": (
            "Neutral rendering: Significance of Mahatma Gandhi's thought in "
            "present times."
        ),
        "marks": 10,
        "source_note": (
            "Routed from 2018 GS-I Q3 (cross-cutting: historical and ethical "
            "anchors both linked); neutral rendering used."
        ),
        "answer": (
            "Gandhi's contemporary significance rests on three interconnected ideas: "
            "ends-means unity (impure means corrupt even a good end), trusteeship (power "
            "and wealth held for society, not as personal property), and the Seven Social "
            "Sins (politics without principles, wealth without work, and five others "
            "warning against decoupling action from ethical restraint).\n\n"
            "Present application: ends-means unity challenges surveillance-state anti-"
            "corruption models that violate privacy rights to catch wrongdoing. Trusteeship "
            "reframes public office as fiduciary, directly rebutting the 'office as personal "
            "entitlement' mindset. The Seven Social Sins remain a diagnostic checklist for "
            "institutional failure.\n\n"
            "The limit: Gandhi's idealism, taken alone, risks under-designing institutional "
            "safeguards. The ARC's own recommendations pair Gandhian values with Kautilyan "
            "structural controls. Gandhi's thought is necessary but not sufficient for "
            "durable governance ethics."
        ),
    },
    {
        "year": 2018,
        "question": (
            "Neutral rendering: (b) Gandhi on anger and intolerance as enemies "
            "of understanding; (c) Tirukkural on falsehood and unblemished good."
        ),
        "marks": 10,
        "source_note": (
            "Routed from 2018 GS-IV Q6 parts (b) and (c); neutral rendering used. "
            "Part (a) attribution unclear in OCR; stem verified against official scan; "
            "OCR artifact resolved."
        ),
        "answer": (
            "Gandhi's warning that anger and intolerance are enemies of correct understanding "
            "links emotional regulation to ethical judgement. A civil servant who decides under "
            "anger or prejudice lacks the Right Mindfulness that both Buddhist and Gandhian "
            "ethics require. Administrative application: a collector handling a communal "
            "complaint must first manage her own emotional response before applying the law.\n\n"
            "The Tirukkural's injunction that unblemished good arises from the absence of "
            "falsehood grounds integrity in truthful communication. An officer who conceals "
            "inconvenient audit findings to protect a superior violates this principle.\n\n"
            "Both quotations converge on the same GS-IV answer logic: internal self-regulation "
            "(emotional and truthful) is the precondition for reliable external conduct. The "
            "limit: self-regulation alone is insufficient without institutional support "
            "structures that make truthfulness safe and anger-driven decisions reviewable."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "How does Kautilya's structural theory of official temptation remain "
            "relevant to designing modern anti-corruption controls in India? "
            "Answer in 150 words."
        ),
        "answer": (
            "Kautilya's Arthashastra treats official corruption as structural rather than "
            "merely moral. The honey-and-poison passage (Kangle 2.9.32, cited in ARC "
            "Annexure-I(2)) argues that an official handling public funds can no more avoid "
            "temptation than a tongue can avoid tasting honey placed on it.\n\n"
            "Modern relevance: India's anti-corruption architecture operationalises this "
            "premise. Mandatory rotation of procurement officers assumes opportunity creates "
            "risk. Data-analytics-driven risk-based tax audit (CBDT) replaces discretionary "
            "scrutiny with algorithmic selection, assuming some non-compliance is structural. "
            "Dual-custody financial approvals prevent single-point failure.\n\n"
            "Kautilya also prescribes positive incentives: those who increase the king's "
            "wealth in just ways should be made permanent in office. This is an early "
            "performance-and-integrity-linked personnel policy.\n\n"
            "The limit: a purely surveillance-based regime risks demoralising honest "
            "officials through excessive suspicion. The ARC's synthesis pairs Kautilyan "
            "controls with Gandhian service-motivation to sustain both accountability "
            "and morale."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Compare Vivekananda's Daridra Narayana and Basava's Kayaka as "
            "frameworks for dignified welfare delivery. Answer in 150 words."
        ),
        "answer": (
            "Both Vivekananda and Basava refuse a charity model of welfare in which the "
            "giver is superior to the receiver. Both insist on a dignity model. But they "
            "ground dignity differently.\n\n"
            "Vivekananda's Daridra Narayana (seeing God in the poor) derives from Advaita "
            "non-dualism: the self in all beings is one, so serving the deprived is serving "
            "the divine. This collapses the sacred-secular distinction and elevates welfare "
            "administration from bureaucratic obligation to devotional duty.\n\n"
            "Basava's Kayakave Kailasa assigns equal spiritual worth to all honest labour "
            "regardless of caste. Dignity comes not from the giver's devotion but from the "
            "worker's own productive effort. This is a proto-egalitarian labour ethic "
            "anticipating Articles 17 and 23.\n\n"
            "Administrative convergence: both reject stigmatising paperwork, public shaming "
            "of beneficiaries and humiliating eligibility procedures. A welfare scheme "
            "designed on either framework avoids processes that degrade the recipient. The "
            "limit: neither provides a self-enforcing mechanism; institutional accountability "
            "is still required."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Using the Buddhist Middle Path as a decision-procedure, evaluate "
            "whether India's vigilance machinery risks demoralising honest "
            "officials through excessive suspicion. Answer in 200 words."
        ),
        "answer": (
            "The Middle Path (Madhyama Pratipada) is not a static counsel to 'be moderate' "
            "but a decision-procedure: before acting, test whether the contemplated response "
            "is an over-reaction or an under-reaction and correct toward proportionality.\n\n"
            "Applied to India's vigilance machinery, the over-reaction pole is a system that "
            "subjects all officers to pervasive surveillance, mandatory CCTV, keystroke "
            "logging and presumptive suspicion regardless of individual conduct. This "
            "discourages legitimate risk-taking: honest officers avoid discretionary decisions "
            "entirely because any decision can attract a vigilance inquiry. The ARC explicitly "
            "cautions against this demoralisation effect.\n\n"
            "The under-reaction pole is a system that abolishes vigilance altogether, relying "
            "on moral suasion alone. Gandhi's idealism, taken without institutional support, "
            "risks precisely this under-design.\n\n"
            "The proportionate response calibrates vigilance to risk. Risk-based audit "
            "selection targets high-discretion and high-value roles rather than blanket "
            "monitoring. Positive incentive design (recognition, tenure security, career "
            "advancement for clean records) complements punitive mechanisms. Protected "
            "dissent channels allow honest officers to raise concerns without retaliation.\n\n"
            "The verdict: the Middle Path applied to vigilance design means matching the "
            "intensity of oversight to the risk profile of the role. Neither blanket "
            "suspicion nor blanket trust serves governance. Durable integrity requires "
            "proportionate institutional design that protects the honest while detecting "
            "the corrupt."
        ),
    },
    {
        "marks": 15,
        "question": (
            "How does Ambedkar's warning about a 'life of contradictions' — "
            "political equality alongside social inequality — guide a civil "
            "servant's approach to affirmative action? Answer in 200 words."
        ),
        "answer": (
            "Ambedkar's 25 November 1949 Constituent Assembly speech warned that India was "
            "entering a life of contradictions: one person, one vote alongside persistent "
            "caste, gender and economic inequality. He cautioned that unless this "
            "contradiction is removed, those suffering from inequality will blow up the "
            "structure of political democracy.\n\n"
            "For a civil servant, this warning grounds affirmative action in constitutional "
            "logic rather than mere political concession. Formal equality (identical "
            "treatment) is insufficient when starting positions are unequal. Targeted "
            "intervention — reservation, fee waivers, doorstep delivery, simplified "
            "documentation for vulnerable groups — operationalises substantive equality.\n\n"
            "Ambedkar paired this with fraternity: without a sense of common brotherhood, "
            "liberty and equality require a policeman to enforce them. A civil servant "
            "implementing affirmative action must therefore combine institutional "
            "mechanisms with community-building that fosters social solidarity.\n\n"
            "The limit: the 'life of contradictions' framing is a diagnosis, not a "
            "ready-made policy formula. The specific design of reservation, targeting "
            "criteria and delivery mechanisms requires separate evidence-based justification. "
            "Ambedkar provides the constitutional mandate for affirmative action; the civil "
            "servant must still design it with objectivity, transparency and periodic review.\n\n"
            "The verdict: Ambedkar's warning converts affirmative action from an optional "
            "political gesture into a constitutional imperative. A civil servant who treats "
            "it as routine largesse rather than structural correction misreads the "
            "constitutional architecture."
        ),
    },
    {
        "marks": 20,
        "question": (
            "'Indian moral thought is not monolithic — it contains an internal "
            "realist-idealist tension that durable governance ethics must hold "
            "together.' Analyse with reference to at least three Indian thinkers. "
            "Answer in 250 words."
        ),
        "answer": (
            "Indian moral thought offers two complementary registers: Kautilya's structural "
            "realism and the Gandhian-Vivekanandan-Basava-Nanak idealist tradition. Durable "
            "governance ethics requires holding both together, mediated by the Buddhist "
            "Middle Path's proportionality discipline.\n\n"
            "Kautilya's realism assumes temptation is structural. The Arthashastra's "
            "honey-and-poison passage (ARC Annexure-I(2)) justifies rotation, audit, dual "
            "custody and positive incentives for integrity. Modern institutions — Lokpal, "
            "CVC, asset-declaration regimes — are structurally Kautilyan: they assume "
            "controls are needed because goodwill alone is unreliable.\n\n"
            "Gandhi's idealism assumes moral transformation through self-purification and "
            "example. Trusteeship reframes public office as fiduciary holding. Vivekananda's "
            "Practical Vedanta makes service to the deprived a spiritual duty, elevating "
            "welfare administration beyond bureaucratic compliance. Basava's Kayaka insists "
            "that all honest labour deserves equal dignity, anticipating anti-discrimination "
            "norms. Guru Nanak's Kirat Karo and Vand Chhako model honest earning and "
            "equitable sharing of public resources.\n\n"
            "The danger of choosing one register alone: pure Kautilyan surveillance "
            "demoralises honest officials through excessive suspicion. Pure Gandhian idealism "
            "under-designs institutional safeguards, assuming moral suasion alone suffices.\n\n"
            "The Buddhist Middle Path synthesises: it tests every governance response against "
            "the twin extremes of over-reaction and under-reaction. A vigilance system that "
            "calibrates oversight to risk, pairs controls with service-motivation, and "
            "protects honest officials while detecting corrupt ones operationalises this "
            "synthesis.\n\n"
            "The verdict: the strongest GS-IV answer explicitly names the tension, assigns "
            "each thinker to the register that matches the scenario's mechanism, and closes "
            "with the synthesis point. Treating Indian moral thought as monolithically "
            "idealist or monolithically realist is both historically inaccurate and "
            "administratively inadequate."
        ),
    },
    {
        "marks": 20,
        "question": (
            "'Applying medieval and ancient Indian concepts to modern governance "
            "risks anachronistic claims.' Critically evaluate, distinguishing "
            "defensible analogy from identity claim, with reference to at least "
            "three Indian moral thinkers. Answer in 250 words."
        ),
        "answer": (
            "The risk of anachronism is real. Claiming that 'ancient India already had X' — "
            "a parliament (Anubhava Mantapa), a social contract (rajadharma), a labour-rights "
            "charter (Kayaka) — collapses historical specificity and substitutes pride for "
            "analysis. But ignoring antecedents is equally distorting: it denies India's moral "
            "traditions any relevance to modern governance.\n\n"
            "The defensible method is disciplined analogy: identify a structural parallel "
            "while explicitly naming the historical gap.\n\n"
            "Kautilya's rajadharma is a proto-social-contract idea: the ruler's duty of "
            "protection and welfare toward subjects gives taxation its legitimacy. It is not "
            "a Lockean social contract (no consent mechanism, no right of revolution), but "
            "the structural parallel is useful for showing that accountability to the governed "
            "is not a Western import. The analogy works; the identity claim does not.\n\n"
            "Basava's Kayaka anticipates anti-discrimination norms (Articles 17 and 23), but "
            "the Constitution has its own distinct drafting history. Basava is a historical "
            "antecedent, not a direct constitutional source. The Anubhava Mantapa is "
            "tradition-attested, not securely dated, and must never be called the 'world's "
            "first parliament.'\n\n"
            "Guru Nanak's Vand Chhako parallels progressive taxation and equitable allocation "
            "but is not a fiscal-policy prescription. The scriptural basis is firm; the "
            "'three pillars' framing is later pedagogical packaging.\n\n"
            "The verdict: Indian moral thinkers enrich governance ethics through disciplined "
            "analogy that shows continuity and precedent. They lose credibility when analogy "
            "becomes identity claim. The Mains-safe formulation is: 'X anticipates / "
            "parallels Y' rather than 'X is Y' or 'India invented Y in the 12th century.' "
            "Naming the gap explicitly is what makes the comparison intellectually honest "
            "and exam-safe."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": "1. Realist-idealist spectrum in Indian moral thought",
        "structural_type": "spectrum-bar",
        "nodes": (
            "Kautilya anchors the realist pole: assume temptation is structural.",
            "Realist design: rotation, dual custody, audit, positive incentive.",
            "Gandhi anchors the idealist pole: moral transformation through example.",
            "Idealist design: trusteeship, self-purification, exemplar-based reform.",
            "Vivekananda, Basava, Nanak share the idealist register with distinct mechanisms.",
            "Buddha's Middle Path sits at the synthesising centre.",
            "Modern governance is Kautilyan in institutional design, Gandhian in aspiration.",
            "Neither pole alone is sufficient; synthesis is the examiner's expected conclusion.",
        ),
        "verdict": "Name both registers and the synthesis point in every Indian-thinkers answer.",
        "answer_use": "Use as the opening framework for any realist-vs-idealist thinker question.",
    },
    {
        "title": "2. Kautilya's anti-corruption control architecture",
        "structural_type": "process-flow",
        "nodes": (
            "Premise: officials handling public money face structural temptation.",
            "ARC Annexure-I(2) quotes Kangle 2.9.32: honey-and-poison passage.",
            "Fish analogy (2.9.33): embezzlement is as unobservable as a fish drinking water.",
            "Bird analogy (2.9.34): concealed intentions are harder to detect than bird paths.",
            "Response: rotation, audit, inspection, reassignment of suspect officials.",
            "Positive incentive: those who increase wealth justly are made permanent.",
            "Modern analogues: risk-based CBDT audit, dual custody, Lokpal.",
            "Limit: pure surveillance without service-motivation demoralises honest officers.",
        ),
        "verdict": "Kautilya provides the structural premise; pair it with idealist motivation for balance.",
        "answer_use": "Use to build the anti-corruption-design paragraph in any Kautilya question.",
    },
    {
        "title": "3. Buddha's Middle Path as a decision-procedure",
        "structural_type": "balance-scale",
        "nodes": (
            "Over-reaction pole: excessive, punitive, populist crackdown.",
            "Under-reaction pole: complacent inaction driven by risk-aversion.",
            "Middle Path tests: is this response proportionate to the actual risk?",
            "Eightfold Path: Right Action (lawful conduct) maps to official duty.",
            "Eightfold Path: Right Livelihood (honest occupation) maps to career ethics.",
            "Eightfold Path: Right Mindfulness (self-aware judgement) maps to bias-checking.",
            "Proportionality discipline prevents both populist demolitions and wilful neglect.",
            "Limit: Middle Path provides the test but not the substantive legal standard.",
        ),
        "verdict": "The Middle Path converts 'be balanced' from vague advice into a testable procedure.",
        "answer_use": "Use as the proportionality check in any case-study or vigilance question.",
    },
    {
        "title": "4. Gandhi's ethical toolkit: trusteeship, means-ends, Seven Social Sins",
        "structural_type": "hub-spoke",
        "nodes": (
            "Trusteeship: power and wealth held for society, not as personal property.",
            "Ends-means unity: impure means corrupt even a good end (strict deontological-virtue hybrid).",
            "Seven Social Sins (ARC Box 2.8): seven decouplings that destroy ethical governance.",
            "ARC wording has 'leisure without conscience'; Young India 1925 has 'pleasure without conscience'.",
            "Gandhi received the list from a correspondent; he published it without claiming authorship.",
            "Satyagraha: non-violent resistance grounded in truth-force.",
            "Administrative translation: bureaucrat holds authority in trust for citizens.",
            "Limit: idealism alone under-designs institutional safeguards.",
        ),
        "verdict": "Gandhi provides the aspirational register; always pair with institutional mechanism.",
        "answer_use": "Use to build any Gandhi quotation, trusteeship or means-ends answer.",
    },
    {
        "title": "5. Vivekananda's Practical Vedanta and Daridra Narayana",
        "structural_type": "causal-chain",
        "nodes": (
            "Advaita non-dualism: the self in all beings is one.",
            "Logical consequence: serving the deprived is serving the divine.",
            "Daridra Narayana: God in the poor, collapsing sacred-secular distinction.",
            "Selective learning: absorb what is good from others in your own way (2024 Q3a).",
            "2025 Q3(c): 'morality of a people' line attributed by UPSC, not in Complete Works.",
            "Welfare administration elevated from obligation to devotional duty.",
            "Rejects charity model in favour of dignity model of service.",
            "Limit: devotional motivation needs institutional accountability to prevent paternalism.",
        ),
        "verdict": "Cite Practical Vedanta's logic chain, not just the inspirational conclusion.",
        "answer_use": "Use to build any Vivekananda quotation or service-ethics answer.",
    },
    {
        "title": "6. Basava's Kayaka, Dasoha and the Anubhava Mantapa",
        "structural_type": "triad-diagram",
        "nodes": (
            "Kayakave Kailasa: dignified honest work is itself the divine abode.",
            "Dasoha: sharing surplus in community service, not personal accumulation.",
            "Anubhava Mantapa: tradition-attested assembly of sharanas across caste and gender.",
            "NOT 'world's first parliament': tradition-attested, not securely dated.",
            "Anticipates Article 17 (abolition of untouchability) and Article 23 (forced labour).",
            "Proto-egalitarian labour ethic: all honest labour carries equal worth.",
            "12th century, Kalachuri kingdom under Bijjala.",
            "Limit: medieval concepts need disciplined analogy, not identity claims.",
        ),
        "verdict": "Present Basava as a historical antecedent to constitutional equality, not its source.",
        "answer_use": "Use to build any Basava, dignity-of-labour or anti-discrimination answer.",
    },
    {
        "title": "7. Guru Nanak's three pillars and public-resource ethics",
        "structural_type": "three-pillar-structure",
        "nodes": (
            "Naam Japna: remembrance of the divine name, grounding ethical conduct spiritually.",
            "Kirat Karo: earn through honest labour, opposing rent-seeking and corruption.",
            "Vand Chhako: share with others, supporting equity-oriented resource allocation.",
            "Public-finance analogy: honest revenue collection + equitable expenditure.",
            "Scriptural basis firm: Guru Granth Sahib, Angs 8 and 1245.",
            "'Three pillars' phrasing is later pedagogical packaging, not Guru Nanak's verbatim triad.",
            "Classical antecedent of bridging social capital through inter-community sharing.",
            "Limit: normative ideal, not a self-enforcing mechanism; needs institutional accountability.",
        ),
        "verdict": "Use the content accurately but flag the pedagogical packaging of the 'three pillars' label.",
        "answer_use": "Use to build any Guru Nanak or public-resource ethics answer.",
    },
    {
        "title": "8. Mahavir's five Mahavratas and Anekantavada",
        "structural_type": "layered-diagram",
        "nodes": (
            "Five Mahavratas: Ahimsa, Satya, Asteya, Brahmacharya, Aparigraha.",
            "Parshvanatha had four vows; Mahavir separately enumerated Brahmacharya as the fifth.",
            "Anekantavada: many-sidedness of truth, no single perspective captures the whole.",
            "Syadvada: conditional predication, the logical expression of Anekantavada.",
            "Administrative use: multi-stakeholder consultation before policy decisions.",
            "Aparigraha: non-possessiveness, cautions against accumulation and nepotism.",
            "Trap: Anekantavada is NOT 'no view is ever correct' but 'truth is many-sided'.",
            "Limit: Anekantavada taken too far risks indecision; a cut-off for deliberation is needed.",
        ),
        "verdict": "Present Anekantavada as a consultative process principle, not as relativism.",
        "answer_use": "Use to build any Mahavir, Jain ethics or multi-stakeholder answer.",
    },
    {
        "title": "9. Ambedkar's constitutional morality, equality and fraternity",
        "structural_type": "reinforcing-triangle",
        "nodes": (
            "Constitutional morality (4 Nov 1948): paramount reverence for constitutional forms (Grote).",
            "Includes the right of open speech and unrestrained censure of authorities.",
            "Equality warning (25 Nov 1949): life of contradictions if social inequality persists.",
            "Political equality without social equality risks democratic collapse.",
            "Fraternity: common brotherhood that makes liberty and equality self-sustaining.",
            "Without fraternity, constitutional values need a policeman to enforce them.",
            "Institutional safeguards: judicial review, fundamental rights, minority protections.",
            "Trap: Ambedkar is NOT only a Polity figure; his ethics content is independently examinable.",
        ),
        "verdict": "Use the morality-equality-fraternity triad to show Ambedkar's GS-IV relevance.",
        "answer_use": "Use to build any constitutional-morality, equality or affirmative-action answer.",
    },
    {
        "title": "10. Social capital: bonding versus bridging",
        "structural_type": "split-comparison",
        "nodes": (
            "Social capital: networks of trust enabling collective action (Putnam).",
            "Bonding capital: within a close-knit group, strengthens in-group cohesion.",
            "Bridging capital: across groups, enables inclusive governance and accountability.",
            "Bonding-only risk: nepotism, gatekeeping, exclusion of outsiders.",
            "MKSS social audits in Rajasthan: work because bridging capital exists or is built.",
            "Jan sunwai (public hearing): requires villagers to trust the process and each other.",
            "Guru Nanak's Vand Chhako and Basava's Dasoha are classical bridging antecedents.",
            "Limit: social capital strengthens governance only when it is inclusive, not insular.",
        ),
        "verdict": "Social capital earns marks only when the bonding-bridging distinction is drawn.",
        "answer_use": "Use to build any social-capital, participatory-governance or social-audit answer.",
    },
    {
        "title": "11. Eight-thinker comparison matrix",
        "structural_type": "comparison-matrix",
        "nodes": (
            "Kautilya: structural realism, external controls, anti-corruption design.",
            "Buddha: Middle Path proportionality, Eightfold Path conduct mapping.",
            "Gandhi: ends-means unity, trusteeship, Seven Social Sins, Satyagraha.",
            "Vivekananda: Practical Vedanta, Daridra Narayana, selective learning.",
            "Basava: Kayaka (dignified labour), Dasoha (sharing), Anubhava Mantapa.",
            "Guru Nanak: Kirat Karo (honest earning), Vand Chhako (equitable sharing).",
            "Mahavir: five Mahavratas, Anekantavada, Aparigraha.",
            "Ambedkar: constitutional morality, equality-fraternity, institutional safeguards.",
        ),
        "verdict": "Match the thinker's mechanism to the scenario, not just the thinker's name.",
        "answer_use": "Use as the rapid-recall grid before any thinker-matching or comparison question.",
    },
    {
        "title": "12. PYQ pattern and answer synthesis",
        "structural_type": "exam-synthesis-rail",
        "nodes": (
            "Quotation-type PYQs (Vivekananda, Gandhi, Tirukkural) dominate 2018-2025.",
            "Teaching-type PYQs (Buddha 2020, Guru Nanak 2023, Mahavir 2025) test mechanism.",
            "Significance-type PYQs (Gandhi 2018) test present-day administrative relevance.",
            "Social-capital PYQ (2023 Q6b) tests Putnam bonding/bridging with Indian examples.",
            "Answer spine: name thinker precisely -> mechanism -> Indian example -> limit -> verdict.",
            "Attribution cautions: Seven Social Sins wording, Anubhava Mantapa dating, three pillars.",
            "Always translate the thinker's idea into one specific administrative practice.",
            "Close with the realist-idealist synthesis to avoid a one-sided treatment.",
        ),
        "verdict": "The highest-scoring answer moves from thinker to mechanism to example to limitation.",
        "answer_use": "Use as the revision checklist before any Indian-thinkers PYQ attempt.",
    },
)

CURRENT_ANCHOR = {
    "title": (
        "Sacred Exposition of Holy Relics of the Tathagata — Peace Beyond Borders, "
        "Leh, Ladakh, 1-14 May 2026"
    ),
    "verified_facts": (
        "Ministry of Culture organised the Sacred Exposition of the Holy Relics of the "
        "Tathagata — Peace Beyond Borders, held 1-14 May 2026 in Leh, Ladakh, "
        "commemorating the 2569th Vesak Buddha Purnima.",
        "Inaugurated at Jive-Tsal, Leh, by Union Home Minister Shri Amit Shah in the "
        "presence of Lieutenant Governor of Ladakh Shri Kavinder Gupta.",
        "Details unveiled on 22 April 2026 by Union Minister for Culture and Tourism "
        "Shri Gajendra Singh Shekhawat and Lieutenant Governor of Ladakh Shri V.K. Saxena "
        "at the National Museum, New Delhi.",
        "Collaborative effort: National Museum, Archaeological Survey of India, "
        "International Buddhist Confederation, Ladakh Gonpa Association, Ladakh Buddhist "
        "Association, Mahabodhi International Meditation Centre.",
        "Sacred Buddha Relics discovered 18 feet beneath an ancient brick stupa in "
        "Uttar Pradesh, built by the Sakya clan.",
        "Exposition open for public veneration 2-14 May 2026 across Jivetsal, "
        "Choglamsar, Leh and Zanskar.",
        "Associated events: exhibitions of Buddhist artefacts at Central Institute of "
        "Buddhist Studies and Leh Palace; conferences on Himalayan Buddhism, Peace in "
        "Times of Conflict, and Past/Present/Future of Buddhism in Ladakh.",
        "Union Home Minister stated the exposition would enable people to experience "
        "the timeless values of compassion, peace and harmony as taught by Lord Buddha.",
    ),
    "administrative_link": (
        "Use as a current India-centric anchor connecting Buddha's teachings (compassion, "
        "Middle Path, non-violence) to an official Government of India initiative. The "
        "Ministry of Culture event demonstrates the state's active role in preserving and "
        "promoting India's moral-philosophical heritage. Link to the GS-IV teaching that "
        "Indian moral thinkers' ideas are not merely historical but are actively invoked "
        "in official governance discourse."
    ),
    "limit": (
        "The exposition is a cultural-heritage event, not a governance-reform policy. Do "
        "not treat it as evidence of Buddhist ethics being operationalised in administrative "
        "decision-making. Use it as an anchor showing continuing official engagement with "
        "Indian moral traditions, not as proof of institutional change."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://culture.gov.in/events/ministry-culture-host-sacred-exposition-holy-relics-tathagata-1-14-may-2026-leh-ladakh",
    "https://culture.gov.in/events/sacred-exposition-holy-relics-tathagata-inaugurated-leh-honble-union-home-minister-shri-amit",
)

SOURCE_CAVEAT = (
    "Use the local Basic and Advanced owners as the controlling source. "
    "Gandhi's Seven Social Sins: ARC Box 2.8 has 'leisure without conscience'; the "
    "original Young India note of 22 October 1925 has 'pleasure without conscience'. "
    "Gandhi received the list from a correspondent and published it without claiming "
    "personal authorship. "
    "2025 GS-IV Q3(c) Vivekananda quotation ('strength of a society... morality of its "
    "people') is attributed by UPSC but is not traceable to the Complete Works of Swami "
    "Vivekananda; present with an 'attributed by UPSC' caveat. "
    "Anubhava Mantapa is tradition-attested, not securely dated; never use 'world's first "
    "parliament' or 'first parliament of the world'. "
    "Guru Nanak's 'three pillars' phrasing is later pedagogical packaging, not a verbatim "
    "triad; the scriptural basis in Guru Granth Sahib (Angs 8 and 1245) is firm. "
    "Kautilya's honey-and-poison passage is quoted from ARC Annexure-I(2) citing Kangle's "
    "translation of Arthashastra 2.9.32, not an ARC original. "
    "Mahavir's five Mahavratas: Jain tradition contrasts Parshvanatha's four vows with "
    "Mahavir's five; Brahmacharya is the vow Mahavir's tradition separately enumerated. "
    "Ambedkar's constitutional morality: the Grote quotation is from 4 November 1948; the "
    "'life of contradictions' speech is from 25 November 1949. "
    "Social capital: bonding-bridging distinction is associated with Robert Putnam. "
    "MKSS social audits are located in Rajasthan."
)

REGISTER_SUPPLEMENT = (
    "Rapid recall: Indian moral thinkers span a realist-idealist spectrum. "
    "REALIST POLE — Kautilya: structural/opportunity theory of corruption; honey-poison "
    "passage (ARC Annexure-I(2), Kangle 2.9.32-34); fish analogy (embezzlement unobservable); "
    "bird analogy (concealed intentions); rajadharma (ruler's duty); positive incentive "
    "(make honest officials permanent). "
    "MIDDLE PATH — Buddha: Madhyama Pratipada as decision-procedure (not static moderation); "
    "Eightfold Path: Right Action/Livelihood/Mindfulness map to lawful conduct/honest "
    "occupation/self-aware judgement; proportionality check against over-reaction and "
    "under-reaction. "
    "IDEALIST POLE — Gandhi: Sarvodaya, trusteeship (fiduciary, not proprietary), ends-means "
    "unity (deontological-virtue hybrid), Seven Social Sins (ARC Box 2.8; 'leisure' vs "
    "'pleasure' split; received from correspondent). Vivekananda: Practical Vedanta, Daridra "
    "Narayana (God in the poor), selective learning (2024 Q3a); 2025 Q3(c) line unverified in "
    "Complete Works. Basava: Kayakave Kailasa (dignified labour), Dasoha (sharing surplus), "
    "Anubhava Mantapa (tradition-attested, NOT 'first parliament'), 12th century under Bijjala. "
    "Guru Nanak: Naam Japna / Kirat Karo / Vand Chhako; scriptural basis GGS Angs 8, 1245; "
    "'three pillars' is later pedagogical packaging. Mahavir: 5 Mahavratas (Ahimsa, Satya, "
    "Asteya, Brahmacharya, Aparigraha); Parshvanatha had 4 — Brahmacharya is the 5th Mahavir "
    "separately enumerated; Anekantavada (many-sidedness, NOT relativism); Syadvada "
    "(conditional predication). "
    "CONSTITUTIONAL ANCHOR — Ambedkar: constitutional morality (4 Nov 1948, Grote quotation); "
    "equality warning (25 Nov 1949, 'life of contradictions'); fraternity (common brotherhood, "
    "makes liberty/equality self-sustaining); institutional safeguards (distrust majoritarian "
    "goodwill alone). NOT only Polity; independently examinable GS-IV content. "
    "SOCIAL CAPITAL — Putnam: bonding (insular, nepotism risk) vs bridging (inclusive, "
    "governance-strengthening); MKSS social audits (Rajasthan) need bridging capital; Nanak's "
    "Vand Chhako and Basava's Dasoha are classical bridging antecedents. "
    "TRAPS: Kautilya ≠ Gandhi (opposite registers). Middle Path ≠ indecision. Basava/Nanak → "
    "Constitution is analogy not identity. Arthashastra has ethics, not only realpolitik. "
    "Trusteeship ≠ personal control. Anekantavada ≠ relativism."
)
