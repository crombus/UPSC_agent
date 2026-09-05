QUESTION_ROWS = (
    (10, "Distinguish Rawls's difference principle from Nozick's entitlement theory."),
    (10, "Why is Walzer's complex equality not simple levelling?"),
    (15, "Compare feminist and subaltern critiques of distributive justice."),
    (15, "Does Sen improve Rawls, or mainly change the metric of justice?"),
    (
        20,
        "Can justice be exhausted by redistribution? Discuss with Rawls, Fraser and "
        "Ambedkarian/subaltern implications.",
    ),
    (
        20,
        "Evaluate whether democratic socialism is the strongest correction to both "
        "libertarianism and Marxist centralism.",
    ),
)

ORIGINAL_CONCLUSIONS = {
    QUESTION_ROWS[0][1]: (
        "Rawls and Nozick disagree not merely over equality but over what makes a "
        "holding just: fair institutions ordered to the least advantaged versus "
        "historically valid title constrained by rectification."
    ),
    QUESTION_ROWS[1][1]: (
        "Walzer's point is not that every sphere must yield identical shares, but that "
        "money or power must not buy dominance across unlike goods with distinct "
        "social meanings."
    ),
    QUESTION_ROWS[2][1]: (
        "Feminist and subaltern critiques deepen distributive justice by showing that "
        "formally neutral rules can preserve hierarchy unless power, voice and status "
        "injury are made part of the analysis."
    ),
    QUESTION_ROWS[3][1]: (
        "Sen improves Rawls most clearly by shifting justice from the distribution of "
        "primary goods to the comparison of real freedoms, yet he supplements rather "
        "than abolishes the need for institutional principles."
    ),
    QUESTION_ROWS[4][1]: (
        "Justice cannot be exhausted by redistribution because status subordination and "
        "exclusion from rule-making persist even when transfers occur; a defensible "
        "answer therefore joins resources, recognition and representation."
    ),
    QUESTION_ROWS[5][1]: (
        "Democratic socialism is strongest when it corrects market privilege and "
        "Marxist authoritarian risk together, but it remains convincing only if "
        "welfare, liberty and democratic accountability are kept institutionally "
        "connected."
    ),
}

ORIGINAL_ANSWER_BODIES = {
    QUESTION_ROWS[0][1]: (
        "Rawls's difference principle and Nozick's entitlement theory answer "
        "inequality through rival moral tests. Rawls judges institutions by fairness "
        "to the least advantaged, while Nozick judges holdings by their history.",
        "For Rawls, equal basic liberties come first, fair equality of opportunity "
        "comes next, and only then may inequalities stand if they improve the "
        "position of the least advantaged. Nozick rejects such patterned assessment. "
        "He asks whether holdings arose through just acquisition, voluntary transfer "
        "and rectification of past injustice under a minimal protective state. Rawls "
        "therefore evaluates the basic structure prospectively; Nozick evaluates "
        "titles historically.",
        "Each theory exposes the other's blind spot. Rawls risks underplaying title "
        "and incentive, while Nozick leaves structural inequality and rectification "
        "seriously under-specified.",
    ),
    QUESTION_ROWS[1][1]: (
        "Walzer's complex equality is not a call for identical shares of every good. "
        "It is a doctrine about protecting distinct social spheres from illegitimate "
        "conversion by money or power.",
        "Different goods carry different social meanings and should be distributed for "
        "different reasons. Political office should not be bought like a commodity, "
        "education should not simply follow wealth, and health care should not be "
        "reduced to market purchasing power. Simple equality would try to flatten all "
        "holdings by one metric. Walzer's alternative is to prevent dominance: "
        "advantage in one sphere must not automatically command superiority in "
        "another.",
        "The view is morally sharp but institutionally thinner than Rawls or Nozick. "
        "It explains what should not dominate, yet says less about the precise "
        "machinery that secures those boundaries.",
    ),
    QUESTION_ROWS[2][1]: (
        "Feminist and subaltern critiques challenge justice theories that examine only "
        "formal rules or market shares. Both argue that persons enter institutions "
        "already marked by hierarchy.",
        "Feminist justice shows that equal treatment is inadequate where gendered "
        "burdens structure education, property, representation and bodily security. "
        "Gauba's own account allows corrective support, not mere identical treatment. "
        "Subaltern justice shifts attention to groups whose labour and contribution "
        "are undervalued because elite rule and hegemonic narratives make "
        "subordination appear natural or consensual. Both critiques therefore widen "
        "justice beyond contract and exchange toward power, dignity and voice.",
        "Yet they should not be collapsed. Feminist analysis begins from patriarchy "
        "and gendered exclusion, whereas subaltern analysis centres structurally "
        "marginal agency, hegemony and elite-centred history.",
    ),
    QUESTION_ROWS[3][1]: (
        "Sen's intervention is best read as a reorientation of justice rather than a "
        "simple rejection of Rawls. He asks how far institutions enlarge actual "
        "capabilities in lived conditions.",
        "Rawls distributes primary goods through principles chosen in the original "
        "position for a fair basic structure. Sen argues that equal resources or "
        "primary goods can still leave persons unequally free because disability, "
        "gendered burdens and social location affect conversion into real "
        "functionings. He therefore shifts attention from ideal design to comparative "
        "judgment, remediable injustice and public reasoning about what people are "
        "actually able to be and do. The metric changes from goods held to freedoms "
        "realised.",
        "Rawls nevertheless retains an advantage in institutional specification. Sen "
        "improves the informational space of justice, but deliberately under-specifies "
        "a final set of principles for a fully just basic structure.",
    ),
    QUESTION_ROWS[4][1]: (
        "A purely redistributive account captures only one family of injustice. The "
        "justice debate widens once unequal status and exclusion from rule-making are "
        "recognised as independent political wrongs.",
        "Rawls remains indispensable because he shows why liberties, opportunity and "
        "the position of the least advantaged matter to institutional fairness. Yet "
        "redistribution alone cannot explain cases where a group remains stigmatised, "
        "unheard or publicly devalued even after material transfers occur. Fraser's "
        "parity-of-participation bridge therefore adds recognition and representation "
        "to distribution. Ambedkarian and subaltern implications, kept as cross-routes "
        "rather than proxy ownership, reinforce the point: graded status, hegemony and "
        "monopolised voice cannot be repaired by income measures alone.",
        "Once justice expands beyond redistribution, new problems arise. Duty-bearers "
        "must be specified, remedies must remain reviewable, and not every status "
        "injury warrants the same institutional response. Otherwise the cure can "
        "become paternal or rhetorically expansive without administrative discipline.",
    ),
    QUESTION_ROWS[5][1]: (
        "Democratic socialism presents itself as a middle route between libertarian "
        "minimalism and Marxist centralism. It keeps social justice as a public aim "
        "while rejecting dictatorship and unregulated market title.",
        "Against libertarianism, democratic socialism argues that formal liberty "
        "without welfare, public services and fair life-chances entrenches privilege. "
        "Against Marxist centralism, it argues that social ownership or regulation "
        "must coexist with freedom of thought, party competition, opposition rights "
        "and civil liberties. Gauba's account treats it as a constitutional and "
        "welfare-oriented correction: partial socialisation, public services and "
        "democratic procedure rather than revolutionary monopoly power.",
        "The position still faces two serious objections. Libertarians question its "
        "treatment of title, incentives and state reach, while Marxists question "
        "whether capitalism can be humanised without leaving structural domination "
        "intact. Its success therefore depends less on slogan than on institutional "
        "design.",
    ),
}

DEPTH_PARAGRAPHS = {
    QUESTION_ROWS[2][1]: (
        "The comparison becomes stronger when it asks what each critique adds to "
        "distributive theory. Feminist justice highlights the gap between formal "
        "rights and effective participation inside household and workplace relations. "
        "Subaltern justice highlights how representation and public meaning are "
        "monopolised before distribution is even counted. Together they show that "
        "status injury and under-valuation can precede and reinforce maldistribution."
    ),
    QUESTION_ROWS[3][1]: (
        "The key issue is the criterion of improvement. If justice is judged by real "
        "freedom and removal of manifest injustice, Sen clearly advances beyond "
        "Rawlsian primary goods. If justice also requires a stable ordering of "
        "institutions, liberties and offices, Sen supplements rather than supersedes "
        "Rawls. A good answer therefore separates metric, method and institutional "
        "determinacy before giving its verdict."
    ),
    QUESTION_ROWS[4][1]: (
        "The temporal and democratic dimensions sharpen the argument further. "
        "Recognition without representation lets elites speak for the injured, while "
        "redistribution without recognition may leave the public meaning of inferiority "
        "untouched. At the forward boundary, debates on democratisation, democratic "
        "backsliding and social movements belong to Topic 23; Topic 20 should only "
        "supply the justice standards later used to judge those processes."
    ),
    QUESTION_ROWS[5][1]: (
        "The decisive test is democratic durability. Democratic socialism must fund "
        "welfare without administrative arbitrariness, protect labour without "
        "silencing opposition, and widen equality without concentrating unreviewable "
        "power. Where later questions shift to democratisation, backsliding or "
        "movement politics, Topic 23 should own the bridge; Topic 20 should stop at "
        "the justice-based criteria by which such regimes are judged. It must also "
        "balance welfare delivery with secure opposition rights and contestable "
        "public power."
    ),
}

CUSTOM_ASCII_FACTS = {
    1: (
        "Gauba presents rival perspectives on justice rather than one settled formula.",
        "Rawls, Nozick, Marxism, socialism, anarchism, feminism and communitarianism differ.",
        "Every doctrine identifies a standard, an object, an institution and a remedy.",
        "Objects include liberties, offices, holdings, labour, status, voice and common goods.",
        "Institutions include the state, market, property regime, family and public culture.",
        "Redistribution, rectification, transformation and recognition are not interchangeable.",
        "The topic rewards comparison across rule, state, property, equality and community.",
        "A strong answer names the justice standard before judging an outcome.",
    ),
    2: (
        "Rawls tests institutions through fair choice and ordered distributive principles.",
        "Nozick tests holdings through acquisition, transfer and rectification.",
        "Marxism targets exploitation, surplus value and productive ownership.",
        "Democratic socialism joins social justice to welfare, liberty and competition.",
        "Anarchism treats coercive hierarchy and domination as the central danger.",
        "Feminist justice exposes gendered burdens hidden by formally equal rules.",
        "Subaltern justice centres dignity, contribution, voice and structural exclusion.",
        "Communitarianism begins from embedded selves and socially interpreted goods.",
    ),
    3: (
        "Rawls does not defend simple equality of outcome.",
        "Original position and veil of ignorance model fair choice under uncertainty.",
        "Equal basic liberties come first, then fair opportunity, then difference.",
        "Primary goods identify the liberties, opportunities and means being distributed.",
        "Nozick does not deny justice; he denies patterned redistribution as the master test.",
        "Entitlement theory turns on acquisition, transfer and rectification together.",
        "Wilt Chamberlain attacks end-state patterning through voluntary exchange.",
        "The water-source case shows that acquisition is not morally unlimited.",
    ),
    4: (
        "Marxist critique targets exploitation, surplus value and productive control.",
        "Democratic socialism keeps social justice but rejects dictatorship.",
        "Anarchism values voluntary cooperation while questioning coercive authority.",
        "Feminist justice tests burdens in property, care, work and representation.",
        "Gramsci explains how hegemony can make inequality appear consensual.",
        "Walzer's complex equality blocks dominance across distinct social spheres.",
        "Sen's capability lens asks what resources enable persons actually to do.",
        "Fraser's parity lens joins distribution, status and peer participation.",
    ),
    5: (
        "Wilt Chamberlain tests whether voluntary transfer may upset a pattern.",
        "The sole water source tests whether acquisition worsens others' position.",
        "A clean sale after dispossession shows why rectification cannot be omitted.",
        "Unpaid labour captured in production illustrates the surplus-value critique.",
        "A neutral rule with unequal care burdens illustrates feminist correction.",
        "Cash transfers with continuing stigma illustrate mis-recognition.",
        "Wealth purchasing office or education illustrates cross-sphere dominance.",
        "Antyodaya is an Indian policy illustration, not proof of one justice theory.",
    ),
    6: (
        "Rule axis: patterned fairness, historical entitlement or anti-domination.",
        "State axis: redistributive authority, minimal protection or decentralisation.",
        "Property axis: primary goods, title history or productive control.",
        "Equality axis: formal treatment, fair opportunity, capability or status parity.",
        "Community axis: isolated chooser, embedded self or sphere-specific meanings.",
        "Critique axis: abstraction, history, exploitation, patriarchy or hegemony.",
        "The same policy can pass one axis while failing another.",
        "A comparative answer should explain conflict before offering a graded synthesis.",
    ),
    7: (
        "Trap: Rawls orders principles; he does not permit liberty-for-income trades.",
        "Trap: Nozick includes rectification; recent consent does not cleanse old injustice.",
        "Trap: Marxian exploitation is structural, not merely a complaint about low wages.",
        "Trap: communitarian goods do not license cultural uniformity or silenced dissent.",
        "Capability and parity are bounded extensions, not Gauba chapter vocabulary.",
        "Postcolonial and global justice remain routed outside this owner.",
        "Verified cross-applied PYQs retain their Philosophy Paper II ownership.",
        "Democratisation, backsliding and movement processes remain Topic 23 bridges.",
    ),
    8: (
        "Revise each perspective through standard, object, institution and remedy.",
        "Define asks for conceptual boundaries before examples.",
        "Compare requires a common axis and a point of real disagreement.",
        "Discuss requires claim, support, objection and balanced conclusion.",
        "Critically examine requires an internal limit, not a decorative criticism.",
        "Use one evidence unit only after stating the mechanism it illustrates.",
        "Route the answer through thesis, distinction, objection-reply and verdict.",
        "Keep quotations paraphrased unless wording and ownership are verified.",
    ),
    9: (
        "Rawls objection: abstract choice may understate history and social identity.",
        "Rawls reply: the device models fair terms, not an empirical bargaining meeting.",
        "Nozick objection: title history may be unknowable and background power unequal.",
        "Nozick reply: uncertainty strengthens the need for rectification rather than patterning.",
        "Marxist objection: centralised transformation may threaten liberty and opposition.",
        "Anarchist objection: voluntary order faces scale, coordination and enforcement problems.",
        "Communitarian objection: shared meanings may conceal hierarchy and exclusion.",
        "Synthesis must preserve distribution, history, status and reviewable power.",
    ),
    10: (
        "Antyodaya illustrates targeted public action but proves no single doctrine.",
        "Indian application should test resources, opportunity, dignity, voice and power.",
        "The 44th-Amendment property bridge must not be cited as Gauba chapter evidence.",
        "Capability and parity require explicit supplementary attribution.",
        "Recognition language must remain a bridge rather than an invented chapter owner.",
        "MCQ labels must preserve narrow distinctions among adjacent standards.",
        "Current examples require dates and source limits before analytical use.",
        "Quotation safety means named propositions are preferable to invented wording.",
    ),
    11: (
        "Primary goods and capability differ between distributed means and real freedom.",
        "Original position and veil differ between a choice device and its information rule.",
        "Liberty, fair opportunity and difference form an ordered Rawlsian sequence.",
        "Entitlement, self-ownership and minimal state are related but non-identical.",
        "Wilt, water-source and rectification cases test different historical questions.",
        "Formal equality, feminist correction and parity test different exclusion mechanisms.",
        "Embedded self and complex equality address identity and sphere dominance separately.",
        "Close-option practice should identify the decisive threshold before selecting.",
    ),
    12: (
        "Six verified PYQs remain cross-applied under Philosophy ownership.",
        "Rawls, Nozick, Sen, Plato and Mill route through Social and Political Ideals.",
        "Political Theory borrows tested questions without claiming primary ownership.",
        "Original Topic 20 practice must remain distinguishable from transferred PYQs.",
        "A 10-mark answer needs definition, mechanism, one criticism and a tight verdict.",
        "A 15-mark answer adds comparison and an objection-reply chain.",
        "A 20-mark answer integrates rival standards, application and graded synthesis.",
        "Every conclusion should state which justice dimension the preferred view secures.",
    ),
}

CUSTOM_ASCII_FOOTERS = {
    1: (
        "VERDICT -> The chapter is comparative by design.",
        "ANSWER USE -> Name the rival standard of justice first.",
    ),
    2: (
        "VERDICT -> Rawls requires ordered principles, not one slogan.",
        "ANSWER USE -> State liberty, opportunity and difference in sequence.",
    ),
    3: (
        "VERDICT -> Nozick's history matters as much as present consent.",
        "ANSWER USE -> Mention rectification when title history is disputed.",
    ),
    4: (
        "VERDICT -> Socialism divides over freedom, method and state form.",
        "ANSWER USE -> Separate welfare constitutionalism from centralism.",
    ),
    5: (
        "VERDICT -> Anarchism critiques domination, not coordination as such.",
        "ANSWER USE -> Balance voluntary order with the scale objection.",
    ),
    6: (
        "VERDICT -> Formal equality can leave structural subordination intact.",
        "ANSWER USE -> Show why correction is not identical treatment.",
    ),
    7: (
        "VERDICT -> Hegemony explains why injustice can appear normal.",
        "ANSWER USE -> Link subaltern critique to public meaning and reward.",
    ),
    8: (
        "VERDICT -> Community meanings qualify but do not abolish justice.",
        "ANSWER USE -> Use Walzer to block one sphere dominating another.",
    ),
    9: (
        "VERDICT -> The six-axis grid prevents descriptive overflow.",
        "ANSWER USE -> Compare rule, state, property, equality, community and critique.",
    ),
    10: (
        "VERDICT -> Supplementary bridges must remain explicitly bounded.",
        "ANSWER USE -> Tag capability and parity as extensions, not Gauba terms.",
    ),
    11: (
        "VERDICT -> Cross-application never transfers Philosophy ownership.",
        "ANSWER USE -> Keep the original Philosophy owner explicit.",
    ),
    12: (
        "VERDICT -> Topic 20 ends where Topic 23's democratic bridges begin.",
        "ANSWER USE -> Route democratisation and backsliding forward to Topic 23.",
    ),
}

REGISTER_SUPPLEMENT = """
### COMPLETE TOPIC CHECKLIST

- **Gauba core sequence:** Rawls -> Nozick -> Marxism -> democratic socialism ->
  anarchism -> feminist and subaltern enlargements -> communitarian critique.
- **Rawls control:** equal basic liberties first; fair equality of opportunity
  precedes the difference principle.
- **Nozick control:** acquisition, transfer and rectification are all necessary.
- **Marxist control:** exploitation and surplus value are structural, not merely
  complaints about low wages.
- **Communitarian control:** embedded self and common goods do not license
  authoritarian homogenisation.
- **Final verdict:** this topic compares rival standards of justice rather than
  announcing one uncontested doctrine.

### SUPPLEMENTARY-EXTENSION BOUNDARY

| Extension | Safe use | Boundary |
|---|---|---|
| Capability approach | Sen/Nussbaum on real freedom and unequal conversion. | Use as supplementary, not as Gauba's own chapter vocabulary. |
| Parity of participation | Fraser on distribution, status and peer standing. | Keep distinct from Gauba-grounded feminist and subaltern material unless tagged. |
| Mis-recognition | Status injury and blocked equal standing. | Use only as a bounded extension, not as core Gauba wording. |

### FACT-RISK CAUTIONS

- Do **not** cite the 44th-Amendment property bridge as Gauba chapter evidence.
- Do **not** present capability or parity language as Gauba's own vocabulary.
- Do **not** invent direct quotations for Rawls, Nozick or Walzer.
- Do **not** reroute verified Philosophy PYQs into Political Theory ownership.

### CROSS-APPLIED PHILOSOPHY OWNERSHIP

| Route | Primary Philosophy owner |
|---|---|
| Rawls / Nozick / Sen / Plato / J.S. Mill | Social and Political Ideals |
| Marxism / anarchism | Political Ideologies |
| Recognition-adjacent and multicultural routes | Humanism, Secularism and Multiculturalism |
| Gender equality and corrective support | Gender Discrimination |
| Caste and Ambedkarian status injury | Caste Discrimination: Gandhi and Ambedkar |
| Capability and ecology routes | Development and Social Progress |

### FORWARD BOUNDARY TO TOPIC 23

- **Democratisation**, **democratic backsliding** and **social movements** belong
  to **Topic 23** as supplemental bounded bridges.
- Topic 20 may supply only the justice standards later used to judge those
  democratic processes.
- Topic 20 must not silently absorb regime-change or movement ownership.

### ANSWER-WRITING GRID

```text
NAME THE STANDARD -> fairness | entitlement | exploitation | anti-domination | community
        |
        v
IDENTIFY THE OBJECT -> liberties | offices | holdings | labour | status | voice
        |
        v
TEST THE INSTITUTION -> state | market | property regime | social hierarchy | public culture
        |
        v
RUN THE CRITICISM -> history | incentive | structural inequality | hegemony | abstraction
        |
        v
GRADED VERDICT -> justified distribution + defensible status + reviewable power
```
""".strip()

MCQ_CONTEXTS = {
    "Primary goods": (
        "A scholarship board compares citizens' access to liberties, offices, income, wealth "
        "and the social bases of self-respect. Which account identifies the relevant bundle?",
        "A court asks what citizens receive in liberties, opportunities and means. Which object?",
    ),
    "Original position": (
        "Constitution-designers must select principles before knowing which social position "
        "they will occupy. Which account identifies the choice situation itself?",
        "Constitution-makers are modelled before bargaining power is known. Which device?",
    ),
    "Veil of ignorance": (
        "Negotiators know general social facts but are denied knowledge of their own class, "
        "talents and rank. Which account identifies this informational restriction?",
        "A rule is made without knowing one's future status. Which condition is simulated?",
    ),
    "Equal basic liberties": (
        "A government proposes suppressing political criticism because the resulting stability "
        "would finance larger transfers. Which account rules out this bargain?",
        "A welfare plan curbs free speech to aid the poor. Which principle blocks this trade?",
    ),
    "Fair equality of opportunity": (
        "Public posts are legally open to all, yet inherited schooling advantages determine "
        "who can compete effectively. Which account diagnoses the remaining injustice?",
        "Elite schooling makes office legal but unreal for most citizens. Which standard judges this?",
    ),
    "Difference principle": (
        "A pay differential is defended only after showing that it improves the position of "
        "those worst placed. Which source-grounded account tests the claim?",
        "Higher rewards are allowed because the worst-off become better off. Which principle?",
    ),
    "Entitlement theory": (
        "An auditor refuses to compare final shares and instead traces how every holding was "
        "acquired, transferred and corrected. Which account guides the inquiry?",
        "A claimant rejects end-state equality and reconstructs title history. Which theory?",
    ),
    "Self-ownership": (
        "A policy treats a person's body and talents as resources available for compulsory "
        "social use. Which account supplies the objection?",
        "Taxation is attacked as using one person's talents for another. Which premise is invoked?",
    ),
    "Minimal protective state": (
        "A constitution confines government to policing force and fraud, enforcing contracts "
        "and correcting proven wrongs. Which account best explains the limit?",
        "Government polices and adjudicates but refuses patterned welfare design. Which model?",
    ),
    "Wilt Chamberlain example": (
        "An initially equal distribution changes because thousands voluntarily pay to watch "
        "one athlete. Which account explains why the new pattern matters?",
        "Many fans pay one player and inequality grows through choice. Which textbook example?",
    ),
    "Water-source example": (
        "One owner acquires the only dependable water supply and can now dictate terms to an "
        "entire settlement. Which account exposes the limit on acquisition?",
        "Someone controls the only water source and subjects all to private discretion. Which example?",
    ),
    "Rectification principle": (
        "A present possessor bought land lawfully, but the chain begins in forced dispossession. "
        "Which account prevents the latest transfer from settling justice?",
        "A recent sale is valid, but the asset began in dispossession. Which principle activates?",
    ),
    "Surplus value": (
        "A factory's workforce produces output worth more than wages and operating replacement, "
        "while owners retain the remainder. Which account diagnoses the relation?",
        "Ownership captures unpaid labour time through production. Which concept diagnoses this?",
    ),
    "Democratic socialism": (
        "A movement combines social ownership and universal welfare with civil liberties, "
        "multiparty competition and accountable government. Which account fits?",
        "Public services expand while dictatorship is rejected. Which current is illustrated?",
    ),
    "Voluntary cooperation": (
        "Local associations coordinate mutual aid through federation and consent rather than "
        "a coercive central hierarchy. Which account best explains the ideal?",
        "Small federated groups reject coercive central rule. Which ideal is shown?",
    ),
    "Feminist corrective equality": (
        "A formally neutral care policy leaves one gender carrying unpaid burdens that block "
        "property, office and voice. Which account reveals why sameness is insufficient?",
        "A neutral rule leaves women excluded from property and power. Which lens explains correction?",
    ),
    "Subaltern justice": (
        "A community performs indispensable labour yet remains absent from elite histories, "
        "public honour and decision-making. Which account identifies the injustice?",
        "Groups produce social wealth yet remain marginal under elite narratives. Which perspective?",
    ),
    "Hegemony": (
        "A hierarchy survives partly because schools, media and everyday language present it "
        "as natural common sense. Which account explains that durability?",
        "Public culture makes subordination seem like common sense. Which concept explains this?",
    ),
    "Situated / embedded self": (
        "A political argument begins with identities formed through language, membership and "
        "shared practices rather than an isolated chooser. Which account fits?",
        "A theory rejects the isolated chooser and starts from shared practices. Which idea?",
    ),
    "Complex equality": (
        "A wealthy citizen tries to convert money into public office, educational rank and "
        "medical priority. Which account rejects that cross-sphere dominance?",
        "Wealth cannot buy office or educational rank across unlike goods. Which concept?",
    ),
    "Chain connection": (
        "An answer defends a limited inequality by tracing how socially connected gains reach "
        "those at the weakest link. Which account identifies this explanatory device?",
        "An answer explains Rawls through social interdependence, not a separate principle. Which label?",
    ),
    "Capability approach": (
        "Two people receive identical resources, but disability and social barriers leave only "
        "one able to convert them into mobility and work. Which account best diagnoses the gap?",
        "Two citizens get the same support, but only one converts it into real freedom. Which lens?",
    ),
    "Parity of participation": (
        "A group receives redistribution but remains excluded from agenda-setting and equal "
        "standing in public debate. Which account states the missing standard?",
        "A group gets funds but lacks equal standing in decisions. Which standard identifies the gap?",
    ),
    "Mis-recognition": (
        "Material support rises while public stigma, humiliation and status subordination remain "
        "unchanged. Which account identifies the surviving wrong?",
        "Funds arrive, but the group remains publicly dishonoured and unheard. Which wrong remains?",
    ),
}

MCQ_RELATED_GROUPS = (
    (
        "Primary goods",
        "Original position",
        "Veil of ignorance",
        "Chain connection",
        "Equal basic liberties",
        "Fair equality of opportunity",
        "Difference principle",
    ),
    (
        "Entitlement theory",
        "Self-ownership",
        "Minimal protective state",
        "Wilt Chamberlain example",
        "Water-source example",
        "Rectification principle",
    ),
    (
        "Surplus value",
        "Democratic socialism",
        "Voluntary cooperation",
        "Feminist corrective equality",
        "Subaltern justice",
        "Hegemony",
    ),
    (
        "Situated / embedded self",
        "Complex equality",
        "Capability approach",
        "Parity of participation",
        "Mis-recognition",
        "Feminist corrective equality",
        "Subaltern justice",
    ),
)

MCQ_PRIORITY_LABELS = (
    "Primary goods",
    "Original position",
    "Veil of ignorance",
    "Equal basic liberties",
    "Fair equality of opportunity",
    "Difference principle",
    "Entitlement theory",
    "Self-ownership",
    "Minimal protective state",
    "Wilt Chamberlain example",
    "Water-source example",
    "Rectification principle",
    "Surplus value",
    "Democratic socialism",
    "Voluntary cooperation",
    "Feminist corrective equality",
    "Subaltern justice",
    "Hegemony",
    "Situated / embedded self",
    "Complex equality",
    "Chain connection",
    "Capability approach",
    "Parity of participation",
    "Mis-recognition",
)
