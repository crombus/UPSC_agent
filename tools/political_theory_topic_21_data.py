"""Source-grounded payload for Political Theory Topic 21."""

QUESTION_ROWS = (
    (10, "Distinguish common good from public interest and common interest."),
    (10, "Why is community not identical to majority?"),
    (15, "Compare liberal and communitarian conceptions of common good."),
    (15, "Critically examine Gandhian sarvodaya as a theory of common good."),
    (
        20,
        "Can common-good reasoning be defended in a plural society without "
        "sacrificing minority rights?",
    ),
    (
        20,
        "Compare Marxian, Gandhian and Aristotelian approaches to the common good.",
    ),
)

ORIGINAL_CONCLUSIONS = {
    "Distinguish common good from public interest and common interest.": (
        "The safest verdict is tripartite: common good is the widest normative "
        "standard, common interest is a narrower empirical overlap, and public "
        "interest is the authoritative policy judgment that must remain "
        "answerable to the common good."
    ),
    "Why is community not identical to majority?": (
        "Community is therefore a normative whole, not a head-count winner; "
        "once majority will is treated as self-justifying, common good collapses "
        "into domination of minorities and dissenters."
    ),
    "Compare liberal and communitarian conceptions of common good.": (
        "Liberalism protects plurality by reconciling claims under rights, while "
        "communitarianism protects solidarity by locating the self within shared "
        "purposes; the stronger answer uses each to correct the other's weakness."
    ),
    "Critically examine Gandhian sarvodaya as a theory of common good.": (
        "Sarvodaya is most defensible as a moral critique of greed, violence and "
        "exclusion, but it remains politically adequate only when voluntary "
        "ethical transformation is joined to rights, equality and safeguards "
        "against hierarchy."
    ),
    "Can common-good reasoning be defended in a plural society without "
    "sacrificing minority rights?": (
        "Yes, but only if common good is defined against state good, majority "
        "good and utilitarian expendability, and is disciplined by equal "
        "citizenship, dissent, review and constitutional morality."
    ),
    "Compare Marxian, Gandhian and Aristotelian approaches to the common good.": (
        "All three reject narrow private self-interest, yet Aristotle locates "
        "common good in right constitutional order, Marx in overcoming class "
        "domination, and Gandhi in moral self-restraint and sarvodaya; no "
        "serious comparison should flatten these distinct routes into one doctrine."
    ),
}

ORIGINAL_ANSWER_BODIES = {
    "Distinguish common good from public interest and common interest.": (
        "The three expressions operate at different levels. **Common good** is "
        "the widest normative standard: the justified welfare of the whole "
        "political community beyond factional, state or numerical advantage.",
        "**Common interest** is narrower and empirical - an overlap among "
        "affected persons. **Public interest** is an authoritative policy "
        "judgment claiming to answer a collective need. A labour-management "
        "settlement may express both parties' common interest yet fail the "
        "common-good test if consumers bear hidden costs; a justified quarantine "
        "may be defended in the public interest and also serve common good.",
        "The distinction prevents state convenience or coalition strength from "
        "becoming self-certifying moral authority.",
    ),
    "Why is community not identical to majority?": (
        "A majority is a numerical relation; community in common-good reasoning "
        "is a normative whole. Gauba therefore rejects equating the common good "
        "with the preference of the largest electoral or cultural bloc.",
        "The common good may require protecting a minority against majority "
        "injustice. Consensus also means continuing accommodation, not the "
        "elimination of disagreement. When a dominant religious, caste or "
        "linguistic group presents its own way of life as the voice of everyone, "
        "sectional interest is merely disguised as community.",
        "Community-language is defensible only when dissenters and weaker groups "
        "retain rights, equal citizenship, voice and review. Constitutional "
        "morality is a supplementary safeguard against majoritarian absorption.",
    ),
    "Compare liberal and communitarian conceptions of common good.": (
        "Liberalism begins from persons with claims and freedoms; "
        "communitarianism begins from socially constituted persons whose goods "
        "are shaped by membership and shared purposes.",
        "For liberals, common good emerges through reconciliation under civil "
        "rules. Rights protect plurality and prevent mutual oppression. Gauba's "
        "Macpherson bridge and welfare correction nevertheless show that market "
        "demand may undervalue socially necessary capacities. Communitarians "
        "reply that the liberal self is too thin: MacIntyre stresses practices "
        "and virtues, Taylor dialogical recognition, and Walzer sphere-specific "
        "social meanings rather than one distributive metric.",
        "Liberalism can protect rights while thinning solidarity; "
        "communitarianism can deepen belonging while risking conformity and "
        "dominant-group morality. A defensible common good therefore combines "
        "social embeddedness with protected dissent and institutional review.",
    ),
    "Critically examine Gandhian sarvodaya as a theory of common good.": (
        "Sarvodaya makes common good a moral-civilisational ideal: uplift of all, "
        "especially the neglected, through non-violence, labour and restraint "
        "rather than aggregate advantage.",
        "Trusteeship treats surplus wealth as a social trust, bread labour joins "
        "consumption to dignified physical work, and ahimsa requires unity of "
        "means and ends. Gandhi thus rejects both capitalist greed and violent "
        "levelling; minority suffering cannot be cancelled by a larger total of "
        "benefit.",
        "Its strength is ethical depth and anti-exclusion. Its weakness is "
        "implementation: trusteeship and renunciation rely heavily on voluntary "
        "change, while harmony-language may understate caste and gender "
        "hierarchy. Sarvodaya therefore needs enforceable equality, rights and "
        "accountable institutions.",
    ),
    "Can common-good reasoning be defended in a plural society without "
    "sacrificing minority rights?": (
        "Common-good reasoning can be defended in a plural society, but only in "
        "a qualified form. The first step is to reject three false equations "
        "already ruled out by the owner: common good is not state good, not "
        "majority good and not utilitarian aggregate gain.",
        "Once those errors are removed, the concept can do valuable work. It "
        "asks whether citizens can justify shared objectives beyond factional "
        "bargaining, while still keeping disagreement legitimate. Liberalism "
        "contributes the rights-framework: minorities, dissenters and weaker "
        "groups cannot be sacrificed simply because a larger bloc claims to "
        "represent the whole. Communitarianism contributes the reminder that "
        "citizens are not detached atoms and that common institutions, practices "
        "and social trust matter. The supplementary bridges extend this "
        "carefully: civic republicanism adds non-domination and active "
        "citizenship, commons-thinking adds the need for institutions that "
        "prevent both private enclosure and unaccountable state control, and "
        "constitutional morality disciplines inherited social consensus when "
        "caste, gender or religious hierarchy masquerades as community good.",
        "The strongest objection is internal domination: group-rights or "
        "community-language may empower elites within communities and silence "
        "women, dissenters or lower-status members. The reply is explicit in the "
        "owner's objection-reply chains: voice, exit, equal status, review and "
        "public justification remain non-negotiable tests. Common good survives "
        "in plural society only as a rights-bounded, contestable and revisable "
        "standard.",
    ),
    "Compare Marxian, Gandhian and Aristotelian approaches to the common good.": (
        "Aristotle, Marx and Gandhi all reject the idea that politics is merely "
        "the registration of private appetite, yet they reach the common good "
        "through very different routes. Aristotle is constitutional and "
        "teleological, Marx structural and conflictual, Gandhi moral and "
        "civilisational.",
        "For Aristotle, the right constitution serves the good life of the whole "
        "community; the political order is judged by whether it advances the "
        "advantage of the whole rather than one class. Marx begins elsewhere. In "
        "a class-divided society, he denies that a genuine common good is "
        "available at all, because antagonistic ownership structures organise "
        "power and interest. Common good becomes fully meaningful only in "
        "communist association after class domination is overcome. Gandhi again "
        "shifts the ground. He seeks common good through trusteeship, bread "
        "labour, non-possession, non-violence and sarvodaya, so that moral "
        "self-restraint replaces both capitalist greed and violent levelling. On "
        "property and conflict, then, Aristotle seeks right ordering, Marx seeks "
        "abolition of class antagonism, and Gandhi seeks ethical transformation.",
        "Their strengths and weaknesses differ correspondingly. Aristotle offers "
        "a strong whole-community criterion but can underplay entrenched "
        "exclusion. Marx best diagnoses structural barriers yet faces the owner's "
        "realisation problem: new domination may follow abolition of private "
        "class power. Gandhi provides the richest moral critique but depends "
        "heavily on voluntarism. A high-quality comparison preserves these "
        "distinct problem-settings instead of turning all three into vague "
        "theories of welfare.",
    ),
}

DEPTH_PARAGRAPHS = {
    "Compare liberal and communitarian conceptions of common good.": (
        "The comparison also turns on how each side handles plurality. "
        "Liberalism treats disagreement as normal and therefore makes rights, "
        "procedures and protected dissent foundational. Communitarianism asks "
        "whether such procedures can survive without prior social trust, shared "
        "meanings and civic attachment. The sharper conclusion is not that one "
        "side refutes the other, but that a workable common-good theory needs "
        "both social embeddedness and institutional safeguards against coercive "
        "homogeneity."
    ),
    "Critically examine Gandhian sarvodaya as a theory of common good.": (
        "A further Indian qualification comes from the owner's own "
        "objection-reply architecture and verified cross-routes to Gandhi-"
        "Ambedkar material. If harmony is invoked without naming caste, social "
        "humiliation and structural exclusion, sarvodaya risks sounding like "
        "moral reconciliation without equal standing. The answer should "
        "therefore distinguish Gandhi's ethical insight from any complacent "
        "assumption that voluntary virtue alone can dissolve entrenched hierarchy."
    ),
    "Can common-good reasoning be defended in a plural society without "
    "sacrificing minority rights?": (
        "This is where the supplementary bridges are most useful. Civic "
        "republican non-domination tests whether any citizen or group is left "
        "under unchecked discretionary power; commons-thinking tests whether "
        "shared resources are governed rather than enclosed; social-capital "
        "language explains why cooperation matters but also why exclusionary "
        "networks are dangerous; and constitutional morality sets the outer limit "
        "by refusing to let inherited consensus override equal citizenship. "
        "These additions strengthen rather than replace the chapter's "
        "anti-majoritarian core."
    ),
    "Compare Marxian, Gandhian and Aristotelian approaches to the common good.": (
        "Aquinas and Hegel should appear only as bounded comparative bridges, "
        "not as direct Gauba Ch.21 evidence. Aquinas extends the flourishing "
        "genealogy; Hegel shows freedom mediated through ethical institutions. "
        "Both clarify, without replacing, Aristotle's civic whole, Marx's "
        "structural critique and Gandhi's moral commonwealth."
    ),
}

CUSTOM_ASCII_FACTS = {
    1: (
        "Common good is a normative ideal of welfare for the whole political community.",
        "Common interest is an empirical overlap among affected persons.",
        "Public interest is a public judgment that must answer to common good.",
        "Consensus means ongoing accommodation, not complete unanimity.",
    ),
    2: (
        "Aristotle tests a constitution by the good of the whole community.",
        "Rousseau contrasts the general will with summed private wills.",
        "Green ties political obligation to common good and self-development.",
        "The opening sequence rejects state good and majority good as equivalents.",
    ),
    3: (
        "Common good, common interest and public interest are not interchangeable.",
        "Public interest may justify policy, but common good still judges it.",
        "Interest overlap among parties does not prove welfare of the whole.",
        "This distinction blocks bureaucratic and factional misuse of the concept.",
    ),
    4: (
        "Liberal reconciliation sees common good as adjusted interests under civil rules.",
        "Rights matter because they prevent mutual oppression and protect plurality.",
        "Gauba adds Macpherson's correction to pure market-equilibrium liberalism.",
        "Prices may undervalue socially necessary human capacities.",
    ),
    5: (
        "Communitarianism treats persons as socially formed through membership and duty.",
        "Shared practices and traditions partly shape the goods people pursue.",
        "MacIntyre gives practices, Taylor recognition, and Walzer social meanings.",
        "Its danger is dominant-group morality dressed up as community.",
    ),
    6: (
        "Marxian theory denies genuine common good in class-divided society.",
        "Antagonistic ownership structures organise power and interest unequally.",
        "Common good becomes meaningful only after class domination is overcome.",
        "The owner's criticism adds the risk of new political domination.",
    ),
    7: (
        "Gandhian common good is moral, not arithmetical or merely administrative.",
        "Trusteeship treats surplus wealth as a trust for social welfare.",
        "Bread labour ties dignity, equality and restraint to bodily work.",
        "Sarvodaya seeks uplift of all through service and non-violence.",
    ),
    8: (
        "State good, majority good and aggregate happiness are rejected substitutes.",
        "A party bargain fails common good if hidden public costs remain.",
        "Liberal weakness is thin solidarity; communitarian weakness is weak machinery.",
        "Marxian and Gandhian routes also face realisation and voluntarism risks.",
    ),
    9: (
        "Minority rights and dissent test whether a claimed good is truly common.",
        "Group-rights claims fail if they silence women or lower-status members.",
        "Constitutional morality disciplines oppressive inherited social consensus.",
        "The safest modern formula is rights-bounded and revisable common good.",
    ),
    10: (
        "Aquinas, Hegel, republicanism, commons and social capital are tagged bridges.",
        "Aquinas extends the natural-law genealogy toward human flourishing.",
        "Hegel links freedom to ethical life in family, society and state.",
        "These bridges deepen comparison but do not become Gauba Ch.21 claims.",
    ),
    11: (
        "High-risk traps confuse common good with majority will or public interest.",
        "Another trap treats communitarianism as permission to erase disagreement.",
        "Strong answers distinguish liberal, communitarian, Marxian and Gandhian routes.",
        "Quotation discipline prefers named propositions over unsafe verbatim lines.",
    ),
    12: (
        "Verified Philosophy PYQs stay with Philosophy as their primary owners.",
        "Borrowed routes concern democracy, minorities, Gandhi, Ambedkar and coexistence.",
        "Topic 21 keeps original Mains prompts while citing those routes carefully.",
        "Topic 23 owns democratisation, backsliding and social movements as bridges.",
    ),
}

CUSTOM_ASCII_FOOTERS = {
    1: (
        "VERDICT -> Separate normative, empirical and justificatory levels first.",
        "ANSWER USE -> Define all three terms before any thinker comparison.",
    ),
    2: (
        "VERDICT -> Aristotle, Rousseau and Green are linked but not merged.",
        "ANSWER USE -> Attach each thinker to one distinct mechanism.",
    ),
    3: (
        "VERDICT -> Precision blocks bureaucratic and factional misuse.",
        "ANSWER USE -> Public-interest language still needs a common-good test.",
    ),
    4: (
        "VERDICT -> Liberalism here is rights plus reconciliation, not market worship.",
        "ANSWER USE -> Pair liberal adjustment with Macpherson's correction.",
    ),
    5: (
        "VERDICT -> Social depth must not become coerced conformity.",
        "ANSWER USE -> Name MacIntyre, Taylor or Walzer specifically.",
    ),
    6: (
        "VERDICT -> Marxian strength is diagnosis; weakness is historical realisation.",
        "ANSWER USE -> Contrast class barrier with later domination risk.",
    ),
    7: (
        "VERDICT -> Gandhi moralises common good beyond utility and state command.",
        "ANSWER USE -> Use trusteeship, bread labour and sarvodaya together.",
    ),
    8: (
        "VERDICT -> The core false equations are statist, majoritarian and utilitarian.",
        "ANSWER USE -> Repair one trap before moving to evaluation.",
    ),
    9: (
        "VERDICT -> Rights, dissent and review are internal tests of common good.",
        "ANSWER USE -> Use the internal-domination objection when plurality appears.",
    ),
    10: (
        "VERDICT -> Supplementary bridges help only when their boundary is stated.",
        "ANSWER USE -> Mark Aquinas and Hegel as comparative extensions.",
    ),
    11: (
        "VERDICT -> Strong answers use propositions and distinctions over risky quotes.",
        "ANSWER USE -> Replace doubtful quotes with verified named positions.",
    ),
    12: (
        "VERDICT -> Philosophy PYQs stay with Philosophy owners.",
        "ANSWER USE -> Route democratisation and backsliding to Topic 23.",
    ),
}

REGISTER_SUPPLEMENT = """
### COMPLETE TOPIC CHECKLIST

- **Core sequence:** common good -> common interest -> public interest -> consensus ->
  liberal route -> communitarian route -> Marxian route -> Gandhian route -> criticisms.
- **Controlling negatives:** common good is **not** state good, **not** majority good,
  and **not** utilitarian aggregate happiness.
- **Best one-line test:** ask whether the whole community, including minorities and
  dissenters, can regard the objective as welfare-enhancing without being coerced into silence.
- **Consensus caution:** consensus is a process of accommodation under disagreement,
  not a metaphysics of unanimity.

### THINKER GRID

| Thinker / stream | Safe use | Boundary |
|---|---|---|
| Aristotle | Right constitution serves the good of the whole community. | Do not turn Aristotle into a modern plural-rights theorist. |
| Rousseau | Public-regarding general will differs from private-will aggregation. | Use cautiously; do not let general will erase dissent. |
| T.H. Green | Political obligation is grounded in common good and self-development. | Do not collapse Green into crude collectivism. |
| Liberalism | Common good emerges through reconciliation under civil rules and rights. | Add Gauba's welfare correction; do not stop at market equilibrium. |
| Macpherson | Market valuation can stunt human capacities. | Use as critique and correction, not as a separate full doctrine here. |
| Communitarianism | Shared goods, memberships and duties partly constitute persons. | Do not treat community as homogeneous or dissent-free. |
| Marx / Engels | Class antagonism blocks genuine common good in class society. | Keep realisation weakness explicit. |
| Gandhi | Trusteeship, bread labour, ahimsa and sarvodaya moralise common good. | Keep voluntarism and hierarchy-risk caveats explicit. |

### SUPPLEMENTARY BRIDGES - SAFE ONLY WHEN BOUNDED

| Bridge | Safe use | Boundary |
|---|---|---|
| Aquinas | Extend the natural-law genealogy of common good toward human flourishing. | Mark as supplementary genealogy, not Gauba Ch.21 evidence. |
| Hegel | Show ethical life between atomism and crude collectivism. | Use only as a bridge; do not present as direct chapter authority. |
| Civic republicanism | Add non-domination and active citizenship to common-good analysis. | Do not equate civic virtue with cultural uniformity. |
| Commons and common goods | Explain shared-resource governance beyond market enclosure. | Keep it institutional, not romantic. |
| Social capital | Explain how trust and associations can support cooperation. | Also state that exclusionary networks can reproduce hierarchy. |
| Constitutional morality | Discipline inherited social consensus through equal citizenship and rights. | Use as bounded democratic safeguard, not as a substitute for the chapter's core distinctions. |

### VERIFIED CROSS-APPLIED PHILOSOPHY OPTIONAL PYQ ROUTES

- **2018, 10m** - liberal democracy and deeper social cohesion ->
  **Primary owner:** Philosophy Paper II - Forms of Government.
- **2018, 10m** - multicultural dignity and Indian cultural identity ->
  **Primary owner:** Philosophy Paper II - Humanism, Secularism and Multiculturalism.
- **2020, 10m** - minority protection in liberal democracies ->
  **Primary owner:** Philosophy Paper II - Forms of Government.
- **2020, 20m** - Gandhian concept of social development ->
  **Primary owner:** Philosophy Paper II - Development and Social Progress.
- **2023, 15m** - Ambedkar on annihilation of caste ->
  **Primary owner:** Philosophy Paper II - Caste Discrimination: Gandhi and Ambedkar.
- **2024, 15m** - tolerance and coexistence in multicultural societies ->
  **Primary owner:** Philosophy Paper II - Humanism, Secularism and Multiculturalism.

### ANSWER-WRITING CONTROL

1. Define the distinction before narrating the doctrine.
2. State one qualified thesis before listing thinkers.
3. Use one objection-reply chain in every 15m or 20m answer.
4. For plural-society stems, add minority rights, dissent and constitutional morality.
5. For Gandhi stems, add trusteeship, bread labour and sarvodaya together, then state the
   voluntarism caveat.
6. For Marx stems, separate class barrier from historical realisation.
7. Avoid unsafe quotations; prefer named propositions and exact distinctions.

### ROUTING BOUNDARIES

- **Topic 22** remains the main owner for democracy, representation, electoral devices and
  minority-protection mechanisms in liberal democracy.
- **Topic 23** must explicitly carry **democratisation, democratic backsliding and social
  movements** as supplemental bounded bridges. Topic 21 may cross-reference those processes
  only as downstream democratic context; it must not absorb their ownership.
""".strip()

MCQ_CONTEXTS = {
    "Common-good norm": (
        "A claimant shifts between state advantage, public rhetoric and sectional gain. "
        "Which statement gives the exact canonical meaning of Common-good norm?",
        "A proposal is defended because it serves the justified welfare of the whole "
        "political community rather than one faction. Which label best fits that claim?",
    ),
    "Common-interest overlap": (
        "Several affected groups want the same immediate outcome, but no wider moral "
        "standard has yet been shown. Which statement captures Common-interest overlap?",
        "Residents, traders and commuters all support reopening a road because each gains "
        "directly from it. Which label names that narrower empirical convergence?",
    ),
    "Public-interest judgment": (
        "A public authority justifies a regulation in collective terms, yet the wider "
        "common-good test still remains open. Which statement gives Public-interest judgment?",
        "A ministry defends a quarantine order as a public decision responsive to social "
        "need. Which label best identifies that justificatory level?",
    ),
    "Consensus process": (
        "An answer wrongly treats consensus as the disappearance of disagreement. Which "
        "statement restores the canonical pairing for Consensus process?",
        "Groups keep negotiating and adjusting claims under continuing disagreement. "
        "Which label best captures that dynamic?",
    ),
    "Aristotelian whole": (
        "A constitution is judged by whether it serves the whole community's good life "
        "rather than one class. Which statement records Aristotelian whole?",
        "A thinker evaluates constitutions by asking whether they advance the good of the "
        "whole political community. Which label applies?",
    ),
    "Rousseauian general will": (
        "A candidate confuses a public-regarding will with the sum of private "
        "preferences. Which statement gives Rousseauian general will?",
        "A theory says common good requires a will directed to the public rather than a "
        "mere addition of private wills. Which label fits this claim?",
    ),
    "Greenian obligation": (
        "Political allegiance is tied to a common good of self-development rather than to "
        "bare command. Which statement gives Greenian obligation?",
        "A law is treated as morally binding only insofar as it helps sustain a shared "
        "good of moral development. Which label best identifies that view?",
    ),
    "Liberal reconciliation": (
        "Common good is derived from reconciling claims under civil rules while protecting "
        "persons from oppression. Which statement captures Liberal reconciliation?",
        "A society relies on rights, lawful adjustment and negotiated coexistence rather "
        "than prior moral unity. Which label best names that route to common good?",
    ),
    "Macpherson's correction": (
        "A learner treats market reward as an adequate measure of social worth. Which "
        "statement gives Macpherson's correction?",
        "A theorist argues that demand and supply may undervalue socially necessary human "
        "capacities and therefore need welfare correction. Which label applies?",
    ),
    "Communitarian embeddedness": (
        "The self is presented as socially formed through memberships and shared practices "
        "rather than as a detached chooser. Which statement records this label?",
        "An argument says people partly discover their goods within communities, practices "
        "and social roles. Which label best fits?",
    ),
    "MacIntyrean practices": (
        "A communitarian answer needs the specific mechanism of traditions, internal goods "
        "and virtues. Which statement gives MacIntyrean practices?",
        "A thinker explains moral formation through cooperative practices sustained by "
        "traditions and standards of excellence. Which label applies?",
    ),
    "Walzerian spheres": (
        "A student wrongly assumes one metric such as money should govern all "
        "distributions. Which statement restores Walzerian spheres?",
        "Education, office and health are treated as goods with different social meanings. "
        "Which label best fits that reasoning?",
    ),
    "Marxian class barrier": (
        "An answer claims class society can already realise a genuine common good. Which "
        "statement gives Marxian class barrier?",
        "A theory argues that antagonistic class relations block a truly shared social "
        "good until class domination is overcome. Which label applies?",
    ),
    "Gandhian trusteeship": (
        "A learner mistakes Gandhi for violent levelling or confiscation. Which statement "
        "gives Gandhian trusteeship?",
        "Wealth-holders are told to treat surplus property as a moral trust for social "
        "welfare. Which label best identifies that idea?",
    ),
    "Bread labour": (
        "Consumption is tied to physical work, dignity and restraint rather than detached "
        "privilege. Which statement captures Bread labour?",
        "A conception of equality asks everyone to perform bodily labour sufficient to "
        "justify consumption and honour work. Which label applies?",
    ),
    "Sarvodaya": (
        "A candidate reduces Gandhian common good to aggregate pleasure. Which statement "
        "restores the canonical pairing for Sarvodaya?",
        "A moral-political ideal seeks uplift of all through non-violence, service and "
        "transformation rather than aggregate arithmetic. Which label best fits?",
    ),
    "State-good error": (
        "A government's institutional strengthening is treated as proof of common good. "
        "Which statement gives State-good error?",
        "A measure expands state capacity, but may still injure citizens or the wider "
        "community. Which label best names that mistake?",
    ),
    "Majority-good error": (
        "Numerical support is taken as sufficient moral justification. Which statement "
        "captures Majority-good error?",
        "A dominant bloc says its preferred outcome must be common good simply because it "
        "commands more votes. Which label applies?",
    ),
    "Utilitarian-aggregate error": (
        "A minority's suffering is defended as acceptable because overall happiness rises. "
        "Which statement gives Utilitarian-aggregate error?",
        "A policy sacrifices a smaller group while claiming the total sum of benefit "
        "justifies the result. Which label best identifies the error?",
    ),
    "Excluded-public bargain": (
        "An agreement satisfies the visible negotiating parties but shifts cost to absent "
        "consumers or displaced groups. Which statement records Excluded-public bargain?",
        "Employers and labour settle their dispute, yet the wider public bears the hidden "
        "burden. Which label best fits that failure of common good?",
    ),
    "Liberal market weakness": (
        "A market order coordinates claims but leaves socially necessary, weakly paid "
        "capacities undervalued. Which statement gives Liberal market weakness?",
        "Prices reward some activities richly while indispensable social functions remain "
        "poorly remunerated. Which label best names the defect being diagnosed?",
    ),
    "Communitarian machinery weakness": (
        "An answer praises community and duty but does not explain how accountable "
        "institutions will resolve conflict. Which statement captures this label?",
        "A theory offers moral richness and solidarity, yet leaves unclear how "
        "disagreements will be settled without domination. Which label applies?",
    ),
    "Marxian realisation weakness": (
        "Abolition of private class power is treated as if it automatically guarantees "
        "freedom from domination. Which statement records this label?",
        "A revolutionary project removes one structure of class rule but is followed by "
        "new concentration of political power. Which label best fits that criticism?",
    ),
    "Gandhian voluntarism weakness": (
        "An answer assumes trusteeship and renunciation will be supplied by moral "
        "persuasion alone. Which statement gives this label?",
        "A programme for common good depends heavily on sustained change of heart by the "
        "powerful rather than on enforceable guarantees. Which label applies?",
    ),
}

MCQ_RELATED_GROUPS = (
    (
        "Common-good norm",
        "Common-interest overlap",
        "Public-interest judgment",
        "Consensus process",
    ),
    (
        "Aristotelian whole",
        "Rousseauian general will",
        "Greenian obligation",
        "Liberal reconciliation",
        "Macpherson's correction",
        "Communitarian embeddedness",
        "MacIntyrean practices",
        "Walzerian spheres",
    ),
    (
        "Liberal reconciliation",
        "Macpherson's correction",
        "Liberal market weakness",
        "Communitarian embeddedness",
    ),
    (
        "Communitarian embeddedness",
        "MacIntyrean practices",
        "Walzerian spheres",
        "Communitarian machinery weakness",
    ),
    (
        "Marxian class barrier",
        "Marxian realisation weakness",
        "Gandhian trusteeship",
        "Bread labour",
        "Sarvodaya",
        "Gandhian voluntarism weakness",
    ),
    (
        "Gandhian trusteeship",
        "Bread labour",
        "Sarvodaya",
        "Gandhian voluntarism weakness",
    ),
    (
        "State-good error",
        "Majority-good error",
        "Utilitarian-aggregate error",
        "Excluded-public bargain",
        "Liberal market weakness",
        "Communitarian machinery weakness",
    ),
)

MCQ_PRIORITY_LABELS = (
    "Common-good norm",
    "Common-interest overlap",
    "Public-interest judgment",
    "Consensus process",
    "Aristotelian whole",
    "Rousseauian general will",
    "Greenian obligation",
    "Liberal reconciliation",
    "Macpherson's correction",
    "Communitarian embeddedness",
    "MacIntyrean practices",
    "Walzerian spheres",
    "Marxian class barrier",
    "Gandhian trusteeship",
    "Bread labour",
    "Sarvodaya",
    "State-good error",
    "Majority-good error",
    "Utilitarian-aggregate error",
    "Excluded-public bargain",
    "Liberal market weakness",
    "Communitarian machinery weakness",
    "Marxian realisation weakness",
    "Gandhian voluntarism weakness",
)
