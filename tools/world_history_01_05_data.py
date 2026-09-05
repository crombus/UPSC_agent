"""Authored content data for World History learner-v2 Topics 01-05."""

from __future__ import annotations

import generate_world_history_common as common


def plan(
    title: str,
    indexes: list[int],
    caution: str,
    exam_use: str,
) -> tuple[str, list[int], str, str]:
    return title, indexes, caution, exam_use


def panel(
    title: str,
    kind: str,
    lines: list[str],
    references: list[str],
) -> tuple[str, str, str, list[str]]:
    return title, kind, "\n".join(lines), references


TOPIC_01 = common.topic(
    1,
    "Enlightenment and Age of Revolutions Overview",
    "01_Enlightenment-and-Age-of-Revolutions-Overview",
    "01_Enlightenment-and-Age-of-Revolutions-Overview_Complete-Topic-Package.md",
    [
        (
            "Age of Reason and Enlightenment",
            "Old NCERT describes eighteenth-century Europe as the Age of Reason "
            "or Enlightenment, an intellectual climate centred on reason, "
            "nature, humanity, freedom and happiness.",
        ),
        (
            "Locke, 1689",
            "John Locke's 1689 rights-and-government formulation linked natural "
            "rights, consent and limited government, making resistance to "
            "rights-violating rule politically defensible.",
        ),
        (
            "Montesquieu, 1748",
            "Montesquieu's 1748 institutional argument connected "
            "constitutionalism with separation of powers as a restraint on "
            "arbitrary authority.",
        ),
        (
            "Rousseau, 1762",
            "Rousseau's 1762 social-contract argument placed popular "
            "sovereignty in the people, while its general-will logic also "
            "carried a possible coercive edge.",
        ),
        (
            "Voltaire and secular criticism",
            "Voltaire's critique of clerical authority elevated reason over "
            "dogma and widened secular public debate, but anti-clericalism "
            "must not be equated automatically with democracy.",
        ),
        (
            "Physiocrats, consent and property",
            "The Physiocrats connected taxation with consent and defended "
            "property and economic freedom, linking fiscal grievance to "
            "anti-privilege politics.",
        ),
        (
            "Ideas, crisis and mobilisation",
            "The balanced causal formula is that ideas supplied legitimacy, "
            "fiscal and social crises supplied momentum, and mobilised groups "
            "supplied revolutionary force.",
        ),
        (
            "American Declaration, 1776",
            "The 1776 American Declaration translated rights-language into a "
            "durable republican break with empire and a precedent for written "
            "constitutional government.",
        ),
        (
            "French Revolution, 1789",
            "The French Revolution of 1789 made rights, citizenship, the "
            "nation and the destruction of legal privilege mass political "
            "questions.",
        ),
        (
            "Atlantic comparison",
            "America broke an imperial link and institutionalised a federal "
            "republic; France dismantled an internal structure of feudal and "
            "dynastic privilege with much greater social depth.",
        ),
        (
            "Universal grammar, restricted membership",
            "Enlightenment rights-language claimed universality, but women, "
            "enslaved people, colonial subjects and many propertyless men "
            "remained outside early political settlements.",
        ),
        (
            "Liberalism",
            "Liberalism made consent, limited government, legal equality, "
            "rights and representative institutions its core political tests, "
            "without initially implying universal franchise.",
        ),
        (
            "Conservatism",
            "Conservatism defended order, religion, property and inherited "
            "institutions through gradual change; the Vienna system combined "
            "great-power peace with repression of liberal nationalism.",
        ),
        (
            "Nationalism",
            "Nationalism treated the nation as the proper unit of sovereignty, "
            "but later combined variously with liberal, conservative, racial "
            "and anti-colonial projects.",
        ),
        (
            "Capitalism",
            "Capitalism concentrated productive wealth in private hands and "
            "organised production through profit, contract and wage labour; "
            "its social effects depended heavily on regulation.",
        ),
        (
            "Socialism",
            "Socialism argued that productive wealth should be socially owned "
            "or controlled and distribution should serve need, ranging from "
            "cooperative and parliamentary to revolutionary forms.",
        ),
        (
            "Communism",
            "Communism joined collective ownership and central planning to "
            "revolutionary seizure of power and, in practice, one-party rule, "
            "while differing Soviet, Chinese and Yugoslav forms emerged.",
        ),
        (
            "Social democracy",
            "Social democracy retained capitalist production but sought "
            "democratic regulation, redistribution, labour rights and welfare "
            "through elections, bargaining and legislation.",
        ),
        (
            "Trade unions and Chartism",
            "England's anti-union laws were repealed in 1824, enabling union "
            "growth, while Chartism in the 1830s and 1840s carried working-"
            "class demands into constitutional politics.",
        ),
        (
            "Welfare-state synthesis",
            "Socialist and labour pressure supplied much of the welfare "
            "programme, while depression and total war created the political "
            "and administrative opening represented by the 1935 Social "
            "Security Act and the 1942 Beveridge Report.",
        ),
    ],
    [
        "Do not treat the Enlightenment as one organised movement with an agreed programme.",
        "Do not call Enlightenment thinkers democrats in the modern universal-franchise sense.",
        "Do not reduce the Enlightenment to hostility toward religion.",
        "Do not claim ideas alone caused the American or French Revolution.",
        "Do not write that the American Revolution caused the French Revolution.",
        "Do not flatten America and France into one identical Atlantic revolution.",
        "Do not equate liberalism and nationalism.",
        "Do not use socialism, communism and social democracy as synonyms.",
        "Do not define capitalism as unregulated free markets in every historical form.",
        "Do not treat conservatism as irrational opposition to every change.",
        "Do not present rights-language as immediate universal equality.",
        "Do not convert an unverified probable question into a claimed UPSC PYQ.",
        "Do not quote Locke, Rousseau or Voltaire beyond verified wording.",
        "Do not claim welfare arose from either socialism or war alone.",
    ],
    [
        (
            10,
            "How did Enlightenment thought challenge arbitrary political authority?",
            "It replaced inherited authority with tests of rights, consent, "
            "institutional limitation and public reason, while stopping short "
            "of modern universal democracy.",
            [1, 2, 3, 4],
        ),
        (
            10,
            "Distinguish liberalism from nationalism in the Age of Revolutions.",
            "Liberalism asked how power should be limited and rights secured; "
            "nationalism asked which people should possess sovereignty, and "
            "their temporary alliance never made them identical.",
            [11, 13, 10],
        ),
        (
            15,
            "The Enlightenment supplied the language, not the entire cause, of revolution. Discuss.",
            "Ideas converted grievance into rights-claims, but fiscal crisis, "
            "social conflict and political opportunity determined timing, "
            "leadership and depth.",
            [0, 6, 7, 8],
        ),
        (
            15,
            "Compare the uses of Enlightenment ideas in the American and French Revolutions.",
            "Both used rights and sovereignty, but America constitutionalised "
            "independence while France destroyed internal privilege and made "
            "citizenship and nationhood socially transformative.",
            [7, 8, 9, 10],
        ),
        (
            20,
            "Examine the forms and social effects of capitalism, socialism and communism.",
            "The doctrines differed over ownership, decision-making and method; "
            "their effects varied through wage labour, revolution, regulation "
            "and welfare rather than following slogans mechanically.",
            [14, 15, 16, 17, 18, 19],
        ),
        (
            20,
            "Why is the Age of Revolutions a turning point in modern political legitimacy?",
            "After the revolutionary era, inherited power had to answer claims "
            "of rights, consent, nation and citizenship, even though the early "
            "rights-bearing public remained sharply restricted.",
            [1, 2, 3, 7, 8, 10, 12, 13],
        ),
    ],
    [
        plan("The eighteenth-century intellectual break", [0, 4], "Reason did not mean a single anti-religious programme.", "Define the Enlightenment as a plural intellectual climate."),
        plan("Locke: rights, consent and limited rule", [1], "Keep Locke in his seventeenth-century setting and avoid modern franchise claims.", "Use Locke to explain lawful resistance and limited government."),
        plan("Montesquieu: power checked by power", [2], "Do not attribute a later constitution clause directly without a verified source.", "Link separation of powers to institutional restraint."),
        plan("Rousseau and popular sovereignty", [3], "Popular sovereignty can coexist with coercive general-will reasoning.", "Use Rousseau for both democratic legitimacy and its tension."),
        plan("Physiocrats, taxation and economic freedom", [5], "The Physiocrats were one current, not the whole Enlightenment.", "Connect fiscal consent to anti-privilege politics."),
        plan("From ideas to revolutionary action", [6], "Ideas explain form, not timing or social depth by themselves.", "Organise causation as legitimacy, crisis and mobilisation."),
        plan("The American constitutional route", [7], "A republican precedent was not yet a fully democratic social order.", "Show how rights became a constitutional state form."),
        plan("The French social-revolutionary route", [8], "Rights and citizenship did not immediately erase exclusion.", "Show how legal privilege and sovereignty were transformed."),
        plan("America and France on the same axes", [9, 10], "Preserve differences in target, social depth and inclusion.", "Use a disciplined comparison instead of parallel narratives."),
        plan("Liberalism and conservatism", [11, 12], "Neither doctrine had one fixed historical form.", "Compare consent and rights with order and inherited institutions."),
        plan("Nationalism as a mobile doctrine", [13], "Nationalism is not inherently liberal or democratic.", "Trace how the nation became a claim to sovereignty."),
        plan("Capitalism and industrial society", [14], "Do not equate capitalism with one regulation level.", "Connect private ownership and wage labour to changing social outcomes."),
        plan("Socialism, communism and social democracy", [15, 16, 17], "Separate ownership, method and political pluralism.", "Build a three-column doctrinal comparison."),
        plan("Trade unions and the constitutional social question", [18], "Chartism did not achieve its immediate programme.", "Show labour moving from workplace bargaining to political rights."),
        plan("The welfare-state synthesis and final verdict", [19, 10], "Avoid a single-cause account of welfare or universal inclusion.", "Conclude with programme, political opening and persistent exclusions."),
    ],
    [
        panel("Enlightenment starting condition", "root-axes", ["INHERITED AUTHORITY -> Church, dynasty, privilege by birth", "NEW TEST -> reason, nature, humanity, freedom, happiness", "POLITICAL QUESTION -> by what right does power command?", "RESULT -> authority must justify itself in public terms"], ["The eighteenth-century intellectual break"]),
        panel("Thinker-to-institution map", "comparison-table", ["LOCKE -> natural rights + consent -> limited government", "MONTESQUIEU -> separation of powers -> constitutional restraint", "ROUSSEAU -> popular sovereignty -> people as source of authority", "VOLTAIRE -> clerical criticism -> secular public debate"], ["Locke: rights, consent and limited rule", "Montesquieu: power checked by power", "Rousseau and popular sovereignty"]),
        panel("Ideas, crisis and force", "causal-system", ["IDEAS -> make inherited privilege illegitimate", "CRISIS -> fiscal stress, food stress, imperial grievance", "MOBILISATION -> assemblies, pamphlets, crowds, organised groups", "REVOLUTION -> legitimacy + momentum + force must interact"], ["From ideas to revolutionary action"]),
        panel("Parallel Atlantic routes", "comparison", ["AMERICA -> external empire challenged -> federal republic", "FRANCE -> internal privilege challenged -> social-legal rupture", "SHARED -> rights, consent, sovereignty, constitutional argument", "DIFFERENCE -> America broke a link; France broke a structure"], ["America and France on the same axes"]),
        panel("Rights and exclusions ledger", "comparison-table", ["UNIVERSAL CLAIM -> rights belong to human beings or citizens", "EARLY BOUNDARY -> property, race, sex and colonial status restrict membership", "CONTRADICTION -> proclaimed equality outruns political practice", "LEGACY -> excluded groups later use the same grammar to demand entry"], ["The American constitutional route", "The French social-revolutionary route"]),
        panel("Liberalism versus conservatism", "comparison", ["LIBERALISM -> consent, rights, law, representation", "CONSERVATISM -> order, property, religion, gradual change", "LIBERAL RISK -> restricted franchise and imperial compatibility", "CONSERVATIVE RISK -> censorship and dynastic repression"], ["Liberalism and conservatism"]),
        panel("Nationalism's changing alliances", "path-consequence", ["CORE -> nation claimed as proper unit of sovereignty", "LIBERAL ALLIANCE -> constitutions and national self-rule", "CONSERVATIVE USE -> state-led unification and discipline", "LATER FORMS -> racial, imperial and anti-colonial nationalisms"], ["Nationalism as a mobile doctrine"]),
        panel("Capitalism's social mechanism", "causal-system", ["PRIVATE OWNERSHIP + PROFIT -> investment and factory production", "WAGE LABOUR -> workers depend on employers for livelihood", "OUTPUT GROWTH -> productive capacity and consumption expand", "UNREGULATED COST -> insecurity, long hours and class conflict"], ["Capitalism and industrial society"]),
        panel("Socialist family tree", "hierarchy", ["SOCIALISM -> social ownership or control; many methods", "COMMUNISM -> revolution + central planning + one-party practice", "SOCIAL DEMOCRACY -> elections + regulation + redistribution", "TEST -> ask who owns, who decides and by what method"], ["Socialism, communism and social democracy"]),
        panel("Labour pressure becomes law", "timeline", ["1824 -> England repeals anti-union laws", "1830s-40s -> Chartism links labour to franchise", "TRADE UNIONS -> collective bargaining enters modern politics", "FACTORY LAW -> laissez-faire yields to evidence of harm"], ["Trade unions and the constitutional social question"]),
        panel("Welfare-state causal synthesis", "argument-tree", ["PROGRAMME -> socialist and labour demands for security", "OPENING -> depression destroys private safeguards", "CAPACITY -> total war expands administration and solidarity", "OUTPUT -> Social Security 1935; Beveridge Report 1942"], ["The welfare-state synthesis and final verdict"]),
        panel("Overview answer spine", "answer-spine", ["DEFINE -> Enlightenment climate or named doctrine", "EVIDENCE -> thinker, document, institution and social base", "ANALYSE -> form, timing, depth and effect on society", "QUALIFY -> exclusions, variant forms and non-linear outcomes"], ["The welfare-state synthesis and final verdict"]),
    ],
    [
        "Age of Reason",
        "John Locke",
        "Montesquieu",
        "Rousseau",
        "popular sovereignty",
        "American Declaration",
        "French Revolution",
        "liberalism",
        "conservatism",
        "nationalism",
        "capitalism",
        "socialism",
        "communism",
        "social democracy",
        "Beveridge Report",
    ],
    (
        "No direct UPSC PYQ is verified as owned solely by this overview in "
        "the local 2018-2025 routing blocks. The verified 2019 American-and-"
        "French-Revolutions demand is solved in Topics 02 and 03 rather than "
        "being relabelled here."
    ),
    [],
    extra=["basic/02_American-Revolution.md", "basic/03_French-Revolution-and-Napoleon.md"],
)


TOPIC_02 = common.topic(
    2,
    "American Revolution",
    "02_American-Revolution",
    "02_American-Revolution_Complete-Topic-Package.md",
    [
        ("Seven Years' War ends, 1763", "The Seven Years' War ended in 1763, after which British war debt encouraged tighter taxation, regulation and troop deployment in the thirteen colonies."),
        ("Stamp Act, 1765", "The Stamp Act of 1765 turned taxation without colonial representation into a constitutional dispute over who could tax and legislate."),
        ("Mercantilist restrictions", "British shipping, market and manufacturing restrictions constrained colonial economic autonomy, though many colonists had also benefited from empire."),
        ("Westward restrictions", "Limits on westward settlement widened colonial grievance while also revealing that expansion threatened Native American lands."),
        ("Colonial self-government", "Existing colonial assemblies gave resistance an institutional base, but these assemblies were elite bodies rather than organs of universal democracy."),
        ("Boston Tea Party, 1773", "The Boston Tea Party of 1773 transformed a tea-duty dispute into symbolic defiance of imperial authority and provoked punitive British measures."),
        ("First Continental Congress, 1774", "The First Continental Congress met at Philadelphia in 1774 and coordinated colonial political resistance."),
        ("Lexington and Concord, 1775", "Armed conflict began at Lexington and Concord in 1775, shifting resistance from boycott and petition toward war."),
        ("Declaration of Independence, 1776", "The Declaration adopted on 4 July 1776 asserted equality and inalienable rights to life, liberty and the pursuit of happiness as the moral basis of independence."),
        ("Jefferson, Paine and Washington", "Thomas Jefferson drafted the Declaration, Thomas Paine's Common Sense supplied ideological force, and George Washington commanded the American armies."),
        ("Saratoga and French alliance, 1777-78", "The colonial victory at Saratoga helped secure the French alliance in 1778, internationalising the war and altering the balance against Britain."),
        ("Yorktown, 1781", "Cornwallis's surrender at Yorktown in 1781 was the decisive military turning point, but it did not itself constitute legal recognition of independence."),
        ("Treaty of Paris, 1783", "The Treaty of Paris of 1783 brought British recognition of American independence and converted military success into an international settlement."),
        ("Articles and union phase, 1781", "The Articles-era union from 1781 enabled cooperation among states but proved weaker than the later federal constitutional order."),
        ("Constitution in effect, 1789", "The United States Constitution came into effect in 1789 and established a written federal republican system."),
        ("Bill of Rights", "The Bill of Rights entrenched protections for speech, press, religion and legal safeguards against government."),
        ("Politically radical outcome", "The Revolution was politically radical because a colony overthrew imperial rule and created a rights-based written federal republic."),
        ("Socially incomplete outcome", "Slavery survived, property qualifications restricted participation, and women and Native Americans remained largely excluded from political equality."),
        ("International precedent", "The American example encouraged revolutionaries in France, Europe and Latin America by proving that republican constitutional state-building could survive."),
        ("American-French distinction", "America contributed a durable constitutional form; France contributed a deeper social destruction of privilege and a more radical language of citizenship and nation."),
    ],
    [
        "Do not reduce the Revolution to a tax revolt.",
        "Do not equate representation with universal franchise.",
        "Do not conflate the Declaration, Constitution and Bill of Rights.",
        "Do not say Yorktown legally created the United States.",
        "Do not claim Britain fought only the colonies after 1778.",
        "Do not claim the American Revolution abolished slavery.",
        "Do not describe the early republic as fully democratic.",
        "Do not ignore Native dispossession in the westward grievance.",
        "Do not say the American and French Revolutions had equal social depth.",
        "Do not treat Saratoga and Yorktown as the same turning point.",
        "Do not omit the Treaty of Paris from the settlement.",
        "Do not attribute the Declaration to George Washington.",
        "Do not invent troop, casualty or tax-revenue figures.",
        "Do not use an unverified verbatim wording for the 2019 cross-cutting PYQ.",
    ],
    [
        (10, "Why did taxation become a constitutional issue in the American colonies?", "The dispute concerned legislative authority and consent, not merely the size of a tax, because established assemblies claimed the right to represent colonial taxpayers.", [0, 1, 4]),
        (10, "Explain why Saratoga was a strategic turning point.", "Saratoga mattered because it converted a colonial war into an international conflict by helping secure French alliance and pressure on British power.", [10, 11, 12]),
        (15, "The American Revolution was political rather than social. Discuss.", "It radically changed sovereignty and constitutional form while leaving slavery, property hierarchy and political exclusion substantially intact.", [14, 15, 16, 17]),
        (15, "How did Enlightenment ideas shape the American struggle?", "Rights, consent and lawful resistance transformed imperial grievance into a justified claim to independent statehood, but social membership remained restricted.", [1, 8, 9, 17]),
        (20, "Assess the American Revolution's contribution to the foundations of the modern world.", "Its main export was a durable method: rights-based secession, written constitutional supremacy, federalism and entrenched liberties, qualified by its exclusions.", [8, 14, 15, 16, 17, 18]),
        (20, "Compare the American and French Revolutions as makers of modern politics.", "They shared rights-language and popular sovereignty, but America institutionalised a republic while France dismantled old-order privilege and transformed citizenship more deeply.", [16, 17, 18, 19]),
    ],
    [
        plan("Post-1763 imperial reordering", [0, 2], "British debt explains timing, not the whole revolutionary programme.", "Open with the structural and conjunctural causes together."),
        plan("Taxation without representation", [1, 4], "Representation meant colonial assemblies, not universal franchise.", "Frame taxation as a sovereignty dispute."),
        plan("Land, settlement and Native dispossession", [3], "Colonial liberty and westward expansion carried contradictory implications.", "Add the social cost to an otherwise constitutional narrative."),
        plan("Boston resistance and inter-colonial coordination", [5, 6], "The Tea Party and Congress were different forms of mobilisation.", "Trace symbolic defiance becoming coordinated politics."),
        plan("From Lexington to independence", [7, 8], "Do not merge the start of war with the declaration of statehood.", "Separate military escalation from ideological nation-making."),
        plan("Jefferson, Paine and Washington", [9], "Keep authorship, pamphleteering and command roles distinct.", "Use named actors without turning the answer into biography."),
        plan("Saratoga and internationalisation", [10], "French alliance followed the turning point; it was not present from the start.", "Explain why external support changed the war."),
        plan("Yorktown and the Paris settlement", [11, 12], "Military decision and legal recognition occurred in different years.", "Close the war through battlefield and treaty stages."),
        plan("The Articles-era problem", [13], "The 1781 framework was not the 1789 Constitution.", "Show why independence still required institutional consolidation."),
        plan("Written federal constitutionalism", [14, 15], "A federal republic did not automatically mean full democracy.", "Explain constitutional form and entrenched rights."),
        plan("What was genuinely revolutionary", [16], "Do not judge revolution only by social redistribution.", "Identify the radical change in sovereignty and state form."),
        plan("Rights and exclusions", [17], "Declared equality and actual membership must be assessed together.", "Use contradiction as evaluation, not as dismissal."),
        plan("The international republican precedent", [18], "Influence is safer than direct causation.", "Link successful independence to later revolutionary possibility."),
        plan("America and France compared", [19], "Preserve each revolution's distinct contribution.", "Answer cross-cutting questions by using common axes."),
        plan("Integrated verdict: radical and conservative", [16, 17, 19], "A graded verdict is stronger than choosing one label.", "Conclude: radical in political form, conservative in social settlement."),
    ],
    [
        panel("Imperial grievance system", "causal-system", ["1763 WAR DEBT -> tighter British taxation and regulation", "MERCANTILISM -> shipping, market and manufacturing constraints", "WESTWARD LIMITS -> land grievance plus Native dispossession", "ASSEMBLIES -> existing institutions convert grievance into resistance"], ["Post-1763 imperial reordering"]),
        panel("Constitutional taxation dispute", "argument-tree", ["BRITISH CLAIM -> Parliament may tax the colonies", "COLONIAL CLAIM -> assemblies represent colonial taxpayers", "STAMP ACT 1765 -> principle becomes explicit", "OUTCOME -> fiscal protest becomes a sovereignty dispute"], ["Taxation without representation"]),
        panel("Protest becomes common action", "timeline", ["1773 -> Boston Tea Party", "1774 -> First Continental Congress, Philadelphia", "1775 -> Lexington and Concord", "1776 -> Declaration turns resistance into independence"], ["Boston resistance and inter-colonial coordination", "From Lexington to independence"]),
        panel("Three actors, three functions", "comparison-table", ["JEFFERSON -> drafts the Declaration", "PAINE -> Common Sense supplies popular ideological force", "WASHINGTON -> commands American armies", "RULE -> do not exchange authorship, argument and command"], ["Jefferson, Paine and Washington"]),
        panel("War internationalises", "path-consequence", ["SARATOGA 1777 -> colonial survival becomes credible", "FRENCH ALLIANCE 1778 -> money, arms, fleet and wider war", "BRITAIN -> faces pressure beyond North America", "YORKTOWN 1781 -> decisive military turning point"], ["Saratoga and internationalisation"]),
        panel("Victory, recognition, constitution", "timeline", ["YORKTOWN 1781 -> military decision", "TREATY OF PARIS 1783 -> legal recognition", "CONSTITUTION 1789 -> durable federal state form", "BILL OF RIGHTS -> liberties entrenched against government"], ["Yorktown and the Paris settlement", "Written federal constitutionalism"]),
        panel("Declaration versus Constitution", "comparison", ["DECLARATION 1776 -> why independence is legitimate", "ARTICLES PHASE 1781 -> states cooperate under weak union", "CONSTITUTION 1789 -> how federal power is organised", "BILL OF RIGHTS -> what government is forbidden to violate"], ["The Articles-era problem", "Written federal constitutionalism"]),
        panel("Political revolution ledger", "comparison-table", ["EMPIRE -> rejected", "MONARCHY -> replaced by federal republic", "WRITTEN CONSTITUTION -> state powers placed in a text", "RIGHTS -> become standards of legitimate government"], ["What was genuinely revolutionary"]),
        panel("Social limits ledger", "comparison-table", ["SLAVERY -> survives", "FRANCHISE -> property and status restrictions remain", "WOMEN -> no equivalent political citizenship", "NATIVE PEOPLES -> expansion intensifies dispossession"], ["Rights and exclusions"]),
        panel("World-historical export", "path-consequence", ["ANTI-IMPERIAL CLAIM -> rebellion justified through rights", "REPUBLIC -> survives war and diplomatic recognition", "WRITTEN CONSTITUTION -> becomes an exportable state model", "INFLUENCE -> France, Europe and Latin America observe the precedent"], ["The international republican precedent"]),
        panel("America versus France", "comparison", ["AMERICA -> breaks external imperial authority", "FRANCE -> attacks internal privilege and feudal order", "AMERICA -> constitutional stability", "FRANCE -> deeper social rupture and radicalisation"], ["America and France compared"]),
        panel("Qualified American verdict", "answer-spine", ["CAUSE -> empire, taxation, assemblies, rights", "COURSE -> protest, war, alliance, treaty", "CREATION -> written federal republic", "QUALIFICATION -> slavery and exclusion survive"], ["Integrated verdict: radical and conservative"]),
    ],
    ["Stamp Act", "Boston Tea Party", "Lexington and Concord", "Declaration of Independence", "Thomas Jefferson", "Thomas Paine", "George Washington", "Saratoga", "French alliance", "Yorktown", "Treaty of Paris", "U.S. Constitution", "Bill of Rights", "slavery", "federal republic"],
    (
        "The local owner routes the 2019 GS-I demand on the American and "
        "French Revolutions and the foundations of the modern world. The "
        "neutral demand is retained and solved without inventing question "
        "number details beyond the owner record."
    ),
    [
        (
            "2019",
            "GS-I · 15 marks",
            "Explain how the American and French Revolutions contributed to the foundations of the modern world.",
            "Verified neutral demand from the local routed owner; cross-cutting with Topic 03.",
            "The American Revolution supplied the constitutional method: a "
            "rights-based break with empire, a written federal republic and "
            "entrenched liberties. Saratoga and the French alliance also "
            "showed how local resistance could exploit great-power rivalry. "
            "Its social settlement remained limited because slavery, property "
            "restrictions and Native dispossession survived. France supplied "
            "the deeper social content through the destruction of privilege, "
            "citizenship and popular sovereignty. Together they made inherited "
            "authority answerable to rights, constitutions and the nation, "
            "without immediately making those principles universal.",
        )
    ],
    live_sources=["https://america250.org/"],
    current_note=(
        "The official America250 homepage metadata identifies America250 as "
        "a bipartisan initiative working to engage every American in the "
        "250th anniversary of the United States. Its current 2026 homepage "
        "describes the Semiquincentennial year and ongoing educational and "
        "history events. This directly renews public attention to the "
        "American Revolution and the founding documents; no decorative event "
        "detail or broader contemporary claim is imported."
    ),
    extra=["basic/01_Enlightenment-and-Age-of-Revolutions-Overview.md", "basic/03_French-Revolution-and-Napoleon.md"],
)


TOPIC_03 = common.topic(
    3,
    "French Revolution and Napoleon",
    "03_French-Revolution-and-Napoleon",
    "03_French-Revolution-and-Napoleon_Complete-Topic-Package.md",
    [
        ("Estates-General, May 1789", "The financially troubled monarchy summoned the Estates-General in May 1789, opening the old regime to a constitutional challenge."),
        ("Three Estates and privilege", "Clergy and nobility held legal and fiscal privileges, while the Third Estate formed about ninety-five per cent of the population in old NCERT and bore exclusion and taxation."),
        ("Bread and fiscal crisis", "Monarchical bankruptcy, tax inequality, bad harvests and bread stress supplied the immediate crisis that Enlightenment ideas translated into a legitimacy struggle."),
        ("National Assembly, 17 June 1789", "The Third Estate declared itself the National Assembly on 17 June 1789, shifting constituent authority from king and estate to nation."),
        ("Tennis Court Oath, 20 June 1789", "The Tennis Court Oath of 20 June 1789 committed the deputies to constitution-making."),
        ("Bastille, 14 July 1789", "The storming of the Bastille on 14 July 1789 became a mass symbol of the fall of autocratic authority; its symbolic value exceeded the prisoner count."),
        ("Rights of Man, August 1789", "The Declaration of the Rights of Man and Citizen proclaimed rights, citizenship and equality before law while not granting immediate universal suffrage."),
        ("Constitutional monarchy, 1791", "The 1791 constitutional-monarchy phase legally broke the old regime but did not resolve fiscal, religious, war or sovereignty conflicts."),
        ("Republic, 1792", "The monarchy was abolished and a republic declared in 1792 as war and popular mobilisation radicalised the Revolution."),
        ("Jacobins and Terror, 1793-94", "The Jacobin phase joined direct-democratic claims and emergency national defence to coercive Terror; old NCERT reports about seventeen thousand tried and executed in fourteen months."),
        ("Jacobin social constitution", "The Jacobin constitutional vision included universal male political rights, a right of insurrection and a public duty to provide work or livelihood."),
        ("Directory, 1795-99", "The Directory represented a propertied retreat from Terror, but instability and war shifted political weight toward the army."),
        ("Napoleon's coup, 1799", "Napoleon's coup in 1799 began an authoritarian consolidation of revolutionary France."),
        ("Napoleonic Code, 1804", "The Napoleonic Code of 1804 preserved legal rationalisation, equality before law and anti-feudal reform while Napoleon concentrated power as emperor."),
        ("Waterloo, 1815", "Napoleon's defeat at Waterloo in 1815 ended the imperial phase but did not restore the full legal and social order of pre-1789 France."),
        ("Bourgeois, peasant and crowd roles", "Bourgeois leadership drove institutional rupture, peasants attacked feudal burdens, and workers, artisans and the Paris crowd pushed radicalisation."),
        ("Women and revolutionary citizenship", "Women participated centrally in revolutionary action but were denied equal political citizenship, exposing the boundary of proclaimed universal rights."),
        ("Slavery contradiction", "Revolutionary France abolished slavery in its colonies, Napoleon later reversed abolition, and final French abolition came in 1848."),
        ("Nation and popular sovereignty", "The Revolution gave the nation a modern political meaning and relocated sovereignty in the people, influencing later nationalism and constitutionalism."),
        ("Napoleon: heir and gravedigger", "Napoleon stabilised the social revolution and exported anti-feudal law while ending republican liberty through empire, censorship and conquest."),
    ],
    [
        "Do not write the Revolution as a single event confined to 1789.",
        "Do not claim the Bastille mattered because of a large prisoner population.",
        "Do not say the Declaration granted universal suffrage in 1789.",
        "Do not reduce the Revolution to a bourgeois movement alone.",
        "Do not romanticise or dismiss the Terror without context and cost.",
        "Do not date the Napoleonic Code to the 1790s.",
        "Do not say Napoleon simply restored the old order.",
        "Do not claim the Revolution achieved full economic equality.",
        "Do not claim slavery was abolished permanently in the revolutionary phase.",
        "Do not omit women and colonial subjects from a relevance answer.",
        "Do not treat popular sovereignty as automatically protective of liberty.",
        "Do not state that France caused every later nationalist revolution.",
        "Do not invent total casualties for the Revolution.",
        "Do not quote revolutionary leaders without verified wording.",
    ],
    [
        (10, "Why did the fiscal crisis become a social revolution in France?", "Fiscal breakdown opened the political arena, but legal privilege, subsistence stress, Enlightenment legitimacy and multi-class mobilisation determined the Revolution's depth.", [0, 1, 2, 15]),
        (10, "Explain the significance of the Declaration of the Rights of Man and Citizen.", "The Declaration made rights, citizenship and equality before law standards of legitimate authority while leaving suffrage and social inclusion incomplete.", [6, 16, 17]),
        (15, "Trace the major phases of the French Revolution and explain why each gave way to the next.", "Unresolved crisis carried constitutional monarchy into republic and Terror; coercive fatigue produced the Directory, whose instability empowered Napoleon.", [3, 7, 8, 9, 11, 12]),
        (15, "The French Revolution remains relevant through its principles and its exclusions. Explain.", "Rights, citizenship, popular sovereignty, secular authority and nationhood remain political standards, while women, workers and colonial subjects reveal their contested boundaries.", [6, 10, 16, 17, 18]),
        (20, "Was Napoleon the heir or the betrayer of the French Revolution?", "He was heir to legal equality, merit and anti-feudal reform but betrayer of republican sovereignty through empire, censorship and conquest.", [12, 13, 14, 19]),
        (20, "Why did the French Revolution become the classic model of modern revolution?", "It fused ideological delegitimation, state crisis and mass multi-class mobilisation, destroyed legal privilege and made nation, citizen and popular sovereignty the grammar of modern politics.", [1, 2, 3, 6, 9, 15, 18]),
    ],
    [
        plan("The old regime and its estates", [1], "The Third Estate was internally divided despite common exclusion.", "Begin with legal privilege rather than a generic rich-poor contrast."),
        plan("Fiscal breakdown, bread and ideas", [0, 2], "Neither bankruptcy, bread nor ideas alone explains the rupture.", "Use a conjunctural causal argument."),
        plan("National Assembly and constituent power", [3, 4], "Assembly and oath are distinct steps in June 1789.", "Show sovereignty moving from king to nation."),
        plan("Bastille and the mass turn", [5], "Symbolic political meaning mattered more than prisoner count.", "Explain how popular action altered constitutional politics."),
        plan("Rights declaration and legal equality", [6], "Rights proclamation did not equal universal suffrage.", "Use rights as both achievement and standard of critique."),
        plan("Constitutional monarchy and unresolved crisis", [7], "The old regime was broken before instability was solved.", "Explain why moderate settlement did not end revolution."),
        plan("Republic and wartime radicalisation", [8], "War and mass mobilisation changed the political coalition.", "Trace reform becoming republic."),
        plan("Jacobins, democracy and Terror", [9, 10], "State emergency does not erase the coercive cost.", "Evaluate democratic innovation and violence together."),
        plan("Directory and military ascendancy", [11], "Retreat from Terror did not produce stable civilian rule.", "Connect instability to Napoleon's opportunity."),
        plan("Napoleon's seizure and codification", [12, 13], "Legal consolidation and political authoritarianism occurred together.", "Build the heir-versus-betrayer ledger."),
        plan("Waterloo and the survival of 1789", [14], "Military restoration could not fully restore legal privilege.", "Separate Napoleon's defeat from the Revolution's legacy."),
        plan("Class coalition and shifting leadership", [15], "Do not make pamphleteers or bourgeois leaders the only actors.", "Explain multi-class revolution and changing leadership."),
        plan("Women, workers and unfinished equality", [16, 10], "Political and economic equality moved at different speeds.", "Use exclusions to qualify transformation."),
        plan("Slavery and colonial contradiction", [17], "Revolutionary abolition was reversed before final abolition in 1848.", "Test universal rights against empire."),
        plan("Nation, sovereignty and Napoleonic verdict", [18, 19], "Influence was non-linear and mixed with conquest.", "Conclude through enduring legitimacy and Napoleon's double role."),
    ],
    [
        panel("Old-regime pressure system", "causal-system", ["LEGAL PRIVILEGE -> clergy and nobility hold exemptions", "FISCAL BREAKDOWN -> monarchy summons Estates-General", "BREAD STRESS -> urban and peasant mobilisation", "ENLIGHTENMENT -> grievance becomes a legitimacy challenge"], ["The old regime and its estates", "Fiscal breakdown, bread and ideas"]),
        panel("June-July 1789 rupture", "timeline", ["17 JUNE -> Third Estate becomes National Assembly", "20 JUNE -> Tennis Court Oath commits constitution-making", "14 JULY -> Bastille turns constitutional revolt into mass symbol", "AUGUST -> rights and legal equality proclaimed"], ["National Assembly and constituent power", "Bastille and the mass turn"]),
        panel("Revolutionary phase ladder", "timeline", ["1789-91 -> National Assembly and constitutional monarchy", "1792-94 -> republic, war, Jacobins and Terror", "1795-99 -> Directory and civilian instability", "1799-1815 -> Napoleonic consolidation and empire"], ["Constitutional monarchy and unresolved crisis", "Republic and wartime radicalisation", "Directory and military ascendancy"]),
        panel("Rights claim and boundary", "comparison", ["CLAIM -> equality before law and citizenship", "BOUNDARY -> no immediate universal suffrage", "WOMEN -> action without equal political citizenship", "COLONIES -> slavery exposes universalism's contradiction"], ["Rights declaration and legal equality", "Women, workers and unfinished equality", "Slavery and colonial contradiction"]),
        panel("Jacobin emergency triangle", "argument-tree", ["WAR -> external invasion and national defence", "COUNTER-REVOLUTION -> fear of internal betrayal", "FACTION -> narrowing political competition", "TERROR -> democratic claims joined to coercive violence"], ["Jacobins, democracy and Terror"]),
        panel("Social coalition matrix", "comparison-table", ["BOURGEOISIE -> office, property and legal equality", "PEASANTRY -> end dues, rents and feudal burdens", "URBAN CROWD -> bread, voice and social equality", "ARMY -> order, merit and later Napoleonic authority"], ["Class coalition and shifting leadership"]),
        panel("Napoleon's inheritance ledger", "comparison", ["PRESERVED -> anti-feudal reform and legal rationalisation", "EXPANDED -> careers open to talent and codified law", "CURTAILED -> republic, free politics and popular sovereignty", "EXPORTED -> reform through conquest and occupation"], ["Napoleon's seizure and codification"]),
        panel("Abolition and reversal", "timeline", ["REVOLUTIONARY PHASE -> slavery abolished in French colonies", "NAPOLEON -> abolition reversed", "RIGHTS PROBLEM -> colony tests universal citizenship", "1848 -> final French abolition"], ["Slavery and colonial contradiction"]),
        panel("Nation and citizenship", "path-consequence", ["SUBJECT OF KING -> inherited obedience", "CITIZEN -> bearer of public rights and duties", "NATION -> people becomes source of sovereignty", "LEGACY -> nationalism and constitutionalism gain a new grammar"], ["Nation, sovereignty and Napoleonic verdict"]),
        panel("Why moderate settlement failed", "causal-system", ["1791 CONSTITUTION -> legal old regime broken", "UNRESOLVED -> fiscal, religious and war crises remain", "MOBILISATION -> popular classes demand deeper change", "OUTCOME -> monarchy falls and republic begins"], ["Constitutional monarchy and unresolved crisis"]),
        panel("Non-linear revolutionary legacy", "timeline", ["1789 -> rights and legal rupture", "1793-94 -> Terror tests liberty", "1799-1815 -> empire keeps social gains, ends republic", "1815 ONWARD -> restoration faces renewed nationalism"], ["Waterloo and the survival of 1789"]),
        panel("French Revolution answer spine", "answer-spine", ["CAUSE -> privilege + fiscal crisis + bread + ideas", "COURSE -> 1789 rupture -> republic -> Terror -> Directory", "NAPOLEON -> social consolidation + political reversal", "VERDICT -> legitimacy changed more fully than social equality"], ["Nation, sovereignty and Napoleonic verdict"]),
    ],
    ["Estates-General", "National Assembly", "Tennis Court Oath", "Bastille", "Declaration of the Rights of Man", "Jacobins", "Reign of Terror", "Directory", "Napoleon", "Napoleonic Code", "Waterloo", "popular sovereignty", "nation", "women", "slavery"],
    (
        "The local owners verify two routed demands: the cross-cutting 2019 "
        "GS-I question on the American and French Revolutions, and the exact "
        "2025 GS-I question on the French Revolution's enduring relevance."
    ),
    [
        (
            "2019",
            "GS-I · 15 marks",
            "Explain how the American and French Revolutions contributed to the foundations of the modern world.",
            "Verified neutral demand; cross-cutting with Topic 02.",
            "America made a rights-based colonial break durable through a "
            "written federal republic and entrenched liberties. France went "
            "further inside society: it attacked estate privilege, feudal "
            "burdens and dynastic sovereignty, and made citizen and nation the "
            "core political categories. Both revolutions therefore shifted "
            "legitimacy toward rights and popular authority. Their exclusions "
            "matter: slavery, gender inequality and restricted participation "
            "show that modern principles emerged before universal membership.",
        ),
        (
            "2025",
            "GS-I · 15 marks · 250 words",
            "The French Revolution has enduring relevance to the contemporary world. Explain.",
            "Exact wording verified in the local owner.",
            "Its enduring relevance lies in standards rather than unchanged "
            "institutions. The Rights of Man made legal equality and public "
            "rights tests of authority; the National Assembly and republic "
            "made popular sovereignty and citizenship central; anti-clerical "
            "reform strengthened secular public authority; and the modern "
            "nation shaped later nationalism. Yet women lacked equal political "
            "citizenship, workers lacked economic equality and colonial "
            "slavery exposed the limits of universalism. Napoleon preserved "
            "legal reform while ending republican liberty. Thus 1789 remains "
            "relevant both for its universal claims and for the critique "
            "generated by their exclusionary application.",
        ),
    ],
    extra=["basic/01_Enlightenment-and-Age-of-Revolutions-Overview.md", "basic/02_American-Revolution.md", "basic/05_Congress-of-Vienna-and-Concert-of-Europe.md"],
)


TOPIC_04 = common.topic(
    4,
    "Industrial Revolution",
    "04_Industrial-Revolution",
    "04_Industrial-Revolution_Complete-Topic-Package.md",
    [
        ("Industrial transition from about 1750", "Old NCERT places the beginning of the Industrial Revolution in England around 1750 as machine-based large-scale production created an industrial economy."),
        ("Capital accumulation", "Expanding trade, colonies and accumulated wealth supplied investible capital, but colonial gains were one element rather than the sole cause."),
        ("Coal and iron", "England's abundant coal and iron supported energy-intensive machinery, though resources required markets, institutions and capital to become productive."),
        ("Enclosure and labour", "The enclosure movement released landless labour for factories, linking agricultural change to industrial wage dependence."),
        ("Agricultural surplus", "Crop rotation, manuring and new implements raised food supply and helped sustain a non-farming urban population."),
        ("Shipping, markets and political order", "Overseas shipping and markets encouraged scale, while a commercially favourable post-seventeenth-century political-legal order reduced friction for enterprise."),
        ("Spinning jenny, 1764", "James Hargreaves' spinning jenny of 1764 accelerated spinning in the leading cotton-textile sector."),
        ("Water frame and Watt era, 1769", "Arkwright's water frame and Watt's steam-engine improvement era around 1769 deepened mechanisation; Watt improved rather than solely invented the steam engine."),
        ("Power loom, 1785", "Edmund Cartwright's power loom of 1785 mechanised weaving and helped integrate textile production inside factories."),
        ("Cotton gin, 1793", "Eli Whitney's cotton gin of 1793, an American invention, accelerated raw-cotton processing."),
        ("Factory system", "The factory system replaced much domestic putting-out production with concentrated machinery, supervision and time discipline."),
        ("Transport revolution", "Canals, macadam roads, steam boats and the first passenger railway in 1830 reduced transport costs and deepened national markets."),
        ("Urbanisation and class formation", "Industrialisation shifted economic life toward towns and made capitalists and wage-workers central social classes."),
        ("Women, children and labour conditions", "Early factories relied heavily on women and children amid long hours, low wages, insecurity and slum conditions."),
        ("Factory Act, 1802", "The first Factory Act in England in 1802 began labour regulation, though early enforcement remained weak."),
        ("Trade unions and Chartism", "Repeal of anti-union laws in 1824 enabled union growth, while Chartism in the 1830s and 1840s connected labour conditions with political rights."),
        ("Uneven continental spread", "Industrialisation spread unevenly to France, Belgium and Switzerland after 1815, later to Germany, and rapidly in the United States especially after 1870."),
        ("State-assisted late industrialisation", "Russia and Japan followed later state-assisted paths; Japan's Meiji government from 1868 built railways, improved roads and promoted modern cotton and silk industry."),
        ("Industry and imperialism", "Rising output intensified demand for raw materials, markets and investment outlets, greatly strengthening imperial rivalry without mechanically creating empire."),
        ("Mixed-blessing verdict", "Industrialisation raised long-run productive capacity but concentrated immediate social costs on workers, making labour law, unionism and political reform part of the industrial story."),
    ],
    [
        "Do not date the Industrial Revolution to one exact year.",
        "Do not reduce industrialisation to machines alone.",
        "Do not say Watt solely invented the steam engine.",
        "Do not call the cotton gin a British invention.",
        "Do not claim industry spread evenly across Europe.",
        "Do not say railways caused the first textile mechanisation wave.",
        "Do not claim industrialisation immediately improved all living standards.",
        "Do not ignore women and child labour.",
        "Do not treat the Factory Act of 1802 as immediately effective regulation.",
        "Do not say industrial capitalism automatically required free trade everywhere.",
        "Do not claim industry mechanically caused imperialism.",
        "Do not answer Indian deindustrialisation solely from World History.",
        "Do not invent British output, wage or population figures.",
        "Do not import unsupported details about Japanese enterprises or business houses.",
    ],
    [
        (10, "Why did England industrialise first?", "England's lead arose from a conjunction of capital, coal, labour release, agricultural surplus, markets, transport and commercial institutions rather than a single invention.", [1, 2, 3, 4, 5]),
        (10, "Why was the factory system a decisive break from domestic production?", "Factories concentrated machinery, labour supervision, steam power and time discipline, increasing scale while creating new wage dependence.", [7, 8, 10, 13]),
        (15, "Examine the social consequences of the Industrial Revolution.", "Productivity and urban growth created capitalist and working classes, harsh gendered and child labour, slums, unions, labour law and demands for political rights.", [12, 13, 14, 15, 19]),
        (15, "Bring out the socio-economic effects of railways in different country settings.", "Railways integrated industrial markets, accelerated continental catch-up, opened settler frontiers, enabled state modernisation and deepened colonial extraction according to the political economy they entered.", [11, 16, 17, 18]),
        (20, "The Industrial Revolution was a mixed blessing. Critically examine.", "Its productive gains were broad and long-term, while early costs were concentrated and immediate; the resulting conflict forced regulation, unionism and franchise reform.", [6, 7, 10, 12, 13, 14, 15, 19]),
        (20, "Analyse the relationship between industrialisation and imperialism.", "Industrial output intensified the search for raw materials, markets and investment and sharpened interstate rivalry, but imperialism also had strategic, political and ideological causes.", [1, 5, 11, 16, 18]),
    ],
    [
        plan("Defining the industrial transformation", [0, 10], "Use a period, not a single start date.", "Define technological and social transformation together."),
        plan("Capital and commercial scale", [1, 5], "Colonial wealth was one source of capital, not the whole explanation.", "Connect finance and markets to fixed industrial investment."),
        plan("Coal, iron and energy", [2], "Natural resources do not explain industrialisation without institutions and demand.", "Show how energy removed production limits."),
        plan("Enclosure, agriculture and labour", [3, 4], "Agricultural change created both surplus and dispossession.", "Link countryside transformation to factories and towns."),
        plan("Textile mechanisation sequence", [6, 7, 8, 9], "Keep inventors, dates and countries distinct.", "Use textiles to explain cumulative innovation."),
        plan("The factory system and time discipline", [10], "Factory concentration was organisational as well as technological.", "Explain new control over labour and production."),
        plan("Transport and national markets", [11], "Railways followed the first mechanisation wave.", "Show transport magnifying rather than initiating industrialisation."),
        plan("Urbanisation and new classes", [12], "Class formation was uneven across regions and trades.", "Connect production change to social structure."),
        plan("Women, children and the industrial household", [13], "Factory work coexisted with domestic and outwork labour.", "Include gender, childhood and household economy."),
        plan("From Factory Acts to unions", [14, 15], "Early law was weak and Chartism did not win immediately.", "Show harm producing regulation and political organisation."),
        plan("Uneven spread across Europe and America", [16], "Do not use one British path as a universal model.", "Explain catch-up and regional variation."),
        plan("Japan and state-assisted late industrialisation", [17], "Use only the locally sourced Meiji infrastructure and industry claims.", "Compare market-led and state-directed routes."),
        plan("Railways in contrasting political economies", [11, 16, 17], "The same technology can integrate or extract.", "Differentiate industrial, settler, latecomer and colonial effects."),
        plan("Industrial capitalism and empire", [18], "Intensification is safer than monocausal creation.", "Link production pressure to global rivalry with qualifications."),
        plan("Mixed blessing and final judgement", [19, 12, 13, 15], "Separate short-run concentrated costs from long-run productive gains.", "End with a graded social and economic verdict."),
    ],
    [
        panel("Why England first: conjunction", "causal-system", ["CAPITAL -> finances fixed investment before returns", "COAL + IRON -> energy and machinery base", "LABOUR + FOOD -> enclosure and agricultural improvement", "MARKETS + LAW -> scale, contracts and commercial security"], ["Capital and commercial scale", "Coal, iron and energy", "Enclosure, agriculture and labour"]),
        panel("Cotton innovation chain", "timeline", ["1764 -> Hargreaves: spinning jenny", "1769 -> Arkwright water frame; Watt improvement era", "1785 -> Cartwright: power loom", "1793 -> Whitney: cotton gin in the United States"], ["Textile mechanisation sequence"]),
        panel("Putting-out to factory", "comparison", ["DOMESTIC SYSTEM -> dispersed tools and household rhythm", "FACTORY -> concentrated machinery and supervision", "STEAM -> production freed from muscle and water limits", "TIME DISCIPLINE -> wage labour organised by the clock"], ["The factory system and time discipline"]),
        panel("Transport multiplier", "path-consequence", ["CANALS + ROADS -> cheaper movement of bulk goods", "STEAM BOATS -> faster water transport", "PASSENGER RAILWAY 1830 -> national networks deepen", "RESULT -> coal, iron, engineering and markets reinforce each other"], ["Transport and national markets"]),
        panel("Industrial class society", "hierarchy", ["CAPITALISTS -> own productive machinery and seek profit", "WAGE WORKERS -> lack tools and depend on employers", "CITY -> housing, sanitation and health become public issues", "POLITICS -> class grievance enters organisation and franchise"], ["Urbanisation and new classes"]),
        panel("Gender and childhood ledger", "comparison-table", ["WOMEN -> central factory workers and household earners", "CHILDREN -> cheap labour under weak protection", "CONDITIONS -> long hours, low wages and insecurity", "CAUTION -> experience varied by trade, place and household"], ["Women, children and the industrial household"]),
        panel("Social response ladder", "timeline", ["1802 -> first Factory Act begins regulation", "1824 -> anti-union laws repealed", "1830s-40s -> Chartism demands political rights", "LONG RESULT -> laissez-faire yields to labour evidence"], ["From Factory Acts to unions"]),
        panel("Uneven diffusion map", "comparison-table", ["ENGLAND -> earliest machine-and-factory surge", "FRANCE/BELGIUM -> continental growth after 1815", "GERMANY/USA -> later powerful acceleration", "RUSSIA/JAPAN -> compressed, state-assisted routes"], ["Uneven spread across Europe and America", "Japan and state-assisted late industrialisation"]),
        panel("Britain versus Japan", "comparison", ["BRITAIN -> private profit joins capital, coal and markets", "JAPAN 1868 -> state treats industry as national security", "BRITAIN -> domestically generated invention sequence", "JAPAN -> railways, roads, cotton and silk promoted from above"], ["Japan and state-assisted late industrialisation"]),
        panel("Railways change with context", "comparison-table", ["INDUSTRIALISER -> integrates markets and heavy industry", "CONTINENTAL CATCH-UP -> links state policy and national market", "SETTLER FRONTIER -> opens land and displaces indigenous peoples", "COLONY -> moves exports and administrative power toward ports"], ["Railways in contrasting political economies"]),
        panel("Industry-to-empire pressure", "causal-system", ["OUTPUT RISES -> raw-material demand expands", "SCALE RISES -> overseas markets become more valuable", "CAPITAL ACCUMULATES -> investment outlets are sought", "RIVALRY INTENSIFIES -> empire gains economic weight"], ["Industrial capitalism and empire"]),
        panel("Mixed-blessing answer spine", "answer-spine", ["GAIN -> productivity, transport and cheaper goods", "COST -> labour insecurity, slums, women and child exploitation", "RESPONSE -> unions, Factory Acts and Chartism", "VERDICT -> broad delayed gains, concentrated immediate costs"], ["Mixed blessing and final judgement"]),
    ],
    ["Industrial Revolution", "England", "spinning jenny", "water frame", "James Watt", "power loom", "cotton gin", "factory system", "Factory Act", "trade unions", "Chartism", "railway", "urbanisation", "imperialism", "Japan"],
    (
        "The owners verify the 2023 GS-I demand on socio-economic effects of "
        "railways in different countries and reproduce the exact 2024 GS-I "
        "question on England's Industrial Revolution and Indian handicrafts. "
        "The India-specific verdict remains with the Modern Indian History owner."
    ),
    [
        (
            "2023",
            "GS-I · 10 marks · 150 words",
            "Bring out the socio-economic effects of railways in different countries.",
            "Verified neutral demand from the local owner.",
            "Railways magnified the political economy they entered. In Britain "
            "they integrated coal, iron, engineering and a national market; in "
            "continental catch-up economies they often supported state-led "
            "market integration; in the United States they opened a settler "
            "frontier while accelerating indigenous dispossession; in Russia "
            "and Japan they served compressed strategic modernisation; and in "
            "colonies they commonly moved export commodities and administrative "
            "power toward ports. Across settings they accelerated urbanisation, "
            "migration, standard time and new occupations. Thus the technology "
            "was common, but ownership and economic purpose determined whether "
            "integration or extraction dominated.",
        ),
        (
            "2024",
            "GS-I · 15 marks · 250 words",
            "How far was the Industrial Revolution in England responsible for the decline of handicrafts and cottage industries in India?",
            "Exact wording reproduced by the World History owner; final India verdict belongs to Modern Indian History.",
            "England's mechanised textile sequence, steam-powered factory "
            "production and cheaper transport sharply lowered unit costs and "
            "created pressure for overseas raw materials and markets. This made "
            "British manufactures formidable competitors to hand production. "
            "However, 'how far' cannot be answered from English technology "
            "alone. Colonial tariff and monopoly structures, revenue policy, "
            "loss of court patronage, transport penetration and regional and "
            "craft variation determined the Indian outcome. Some coarse rural "
            "and specialised luxury production persisted. The Industrial "
            "Revolution supplied the cost and scale advantage; colonial power "
            "converted that advantage into asymmetric market access, so the "
            "decline was technologically enabled but politically mediated.",
        ),
    ],
    extra=["basic/01_Enlightenment-and-Age-of-Revolutions-Overview.md", "../Modern-Indian-History/basic/07_Economic-Impact-of-British-Rule.md"],
)


TOPIC_05 = common.topic(
    5,
    "Congress of Vienna and Concert of Europe",
    "05_Congress-of-Vienna-and-Concert-of-Europe",
    "05_Congress-of-Vienna-and-Concert-of-Europe_Complete-Topic-Package.md",
    [
        ("Congress of Vienna, 1814-15", "The Congress of Vienna met in 1814-15 after Napoleon's defeat to reconstruct Europe through dynastic restoration and strategic equilibrium."),
        ("Final Act, June 1815", "The Final Act signed in June 1815 formalised the territorial and diplomatic settlement."),
        ("Metternich", "Austrian statesman Metternich was the dominant figure at Vienna, especially in the conservative ordering of Central Europe."),
        ("Legitimacy", "The principle of legitimacy restored dynasties, including the Bourbons in France, and treated inherited rule rather than national consent as the basis of valid government."),
        ("Balance of power", "Balance-of-power policy contained rather than destroyed France, built buffers and prevented another single continental hegemon."),
        ("Compensation", "Compensation redistributed territory among victors, strengthening Prussia and Sardinia-Piedmont while enlarging Austrian and Russian influence."),
        ("Kingdom of the Netherlands", "Belgium and Holland were joined in the Kingdom of the Netherlands as a northern buffer against France, an arrangement broken by Belgian independence in 1830."),
        ("German Confederation, 39 states", "Vienna created a German Confederation of thirty-nine states under Austrian influence, postponing rather than solving German unity."),
        ("Italy under Austrian influence", "Austria received Lombardy and Venetia and influenced much of divided Italy, while Sardinia-Piedmont gained Genoa and later led unification."),
        ("Poland and Russia", "Most of the Duchy of Warsaw passed under Russian control as Congress Poland, subordinating Polish national aspirations to great-power bargaining."),
        ("Prussian and Swiss settlement", "Prussia gained the Rhineland, Westphalia and part of Saxony, while Swiss neutrality received recognition."),
        ("Concert of Europe", "The Concert was a diplomatic habit of great-power consultation and periodic congresses, not a permanent treaty-state or the same institution as the Holy Alliance."),
        ("Holy Alliance, 1815", "The Holy Alliance of Russia, Austria and Prussia supplied symbolic conservative language but had limited practical importance compared with the wider Concert."),
        ("Aix-la-Chapelle, 1818", "At Aix-la-Chapelle in 1818 France was readmitted to great-power consultation, showing that the defeated power was reintegrated rather than permanently excluded."),
        ("Carlsbad Decrees, 1819", "The Carlsbad Decrees of 1819 imposed censorship, university control and investigation against liberal and nationalist activity in the German states."),
        ("Troppau and Laibach, 1820-21", "The Troppau and Laibach congresses asserted intervention against revolutions, linking great-power order to domestic repression."),
        ("Verona, 1822", "The Congress of Verona in 1822 approved French intervention in Spain and was the last major effective congress of the old system."),
        ("Belgian independence, 1830", "The Concert accepted Belgian independence in 1830, demonstrating selective adaptation rather than rigid restoration."),
        ("Revolutions of 1848", "The revolutions of 1848 exposed the settlement's unresolved liberal, national and social questions, though divided coalitions and loyal dynastic armies helped defeat them."),
        ("Peace-versus-repression verdict", "Vienna achieved substantial great-power peace and diplomatic consultation while denying consent and repressing liberal-national change, creating stability with a legitimacy deficit."),
    ],
    [
        "Do not equate the Holy Alliance with the Concert of Europe.",
        "Do not say Vienna created nation-states by popular will.",
        "Do not claim the Congress only punished France.",
        "Do not describe Metternich as controlling every great power.",
        "Do not give the German Confederation any number other than thirty-nine states.",
        "Do not say the Concert was a permanent treaty-state.",
        "Do not claim Carlsbad strengthened German democracy.",
        "Do not say the Concert collapsed immediately after Verona.",
        "Do not claim the Concert prevented every war or intervention.",
        "Do not present Belgium's 1830 independence as evidence of rigid restoration.",
        "Do not give unsupported population or area figures for territorial transfers.",
        "Do not name unsourced 1848 leaders or country-by-country sequences.",
        "Do not confuse balance of power with national self-determination.",
        "Do not call the settlement either pure peace or pure repression without a dual verdict.",
    ],
    [
        (10, "Explain the principles of legitimacy, balance of power and compensation at Vienna.", "The principles restored dynasties, contained France through buffers and redistributed territory among victors, producing order without popular consent.", [3, 4, 5, 6]),
        (10, "Distinguish the Concert of Europe from the Holy Alliance.", "The Concert was the broader practical habit of great-power consultation; the Holy Alliance was a narrower symbolic conservative compact among Russia, Austria and Prussia.", [11, 12, 13]),
        (15, "Was the Concert of Europe an instrument of peace or repression?", "It was both: consultation moderated conflict among powers while Carlsbad and intervention congresses suppressed liberal and national movements within states.", [11, 14, 15, 16, 17, 19]),
        (15, "How did Vienna postpone rather than solve the national question?", "Its German, Italian, Polish and Belgian arrangements subordinated nations to dynastic strategy, producing later revision in 1830, 1848 and the unifications.", [6, 7, 8, 9, 17, 18]),
        (20, "Assess the Congress of Vienna as a post-war settlement.", "Vienna wisely reintegrated France, built strategic equilibrium and established consultation, but compensation and legitimacy armed future unifiers and denied popular consent.", [0, 3, 4, 5, 10, 13, 19]),
        (20, "Why did the revolutions of 1848 challenge yet fail to destroy the Vienna order?", "The order had accumulated national, liberal and social grievances, but revolutionary coalitions divided, national aims conflicted and dynastic armies retained coercive power.", [14, 15, 17, 18, 19]),
    ],
    [
        plan("Post-Napoleonic reconstruction", [0, 1, 2], "Vienna sought order after war, not democratic reconstruction.", "Define the settlement's context, document and leading statesman."),
        plan("Legitimacy and dynastic restoration", [3], "Legitimacy privileged dynastic right over national consent.", "Use restoration as both stabilising method and legitimacy problem."),
        plan("Balance of power and buffers", [4, 6], "Containment did not mean destruction of France.", "Explain strategic geography through the Netherlands buffer."),
        plan("Compensation and territorial bargaining", [5], "Compensation rewarded powers, not populations.", "Connect territorial transfers to later unintended consequences."),
        plan("Germany: unity postponed", [7], "The Confederation was not a united German nation-state.", "Show the thirty-nine-state arrangement and Austrian influence."),
        plan("Italy: Austrian control and Piedmont's strengthening", [8], "Vienna unintentionally strengthened a future unifier.", "Link settlement design to later Italian nationalism."),
        plan("Poland, Prussia and Switzerland", [9, 10], "Do not flatten distinct territorial outcomes into one map list.", "Use one consequence for each transfer."),
        plan("The Concert as diplomatic practice", [11], "The Concert was a habit of consultation, not a supranational government.", "Define the mechanism before judging it."),
        plan("Holy Alliance and practical limits", [12], "Symbolic language and operational diplomacy were not identical.", "Distinguish overlapping post-1815 instruments."),
        plan("Aix-la-Chapelle and reintegration", [13], "France's readmission shows moderation, not ideological unity.", "Use reintegration as evidence of adaptive peace-making."),
        plan("Carlsbad and domestic repression", [14], "Censorship and university control targeted liberal nationalism.", "Show peace among states linked to repression within states."),
        plan("Intervention at Troppau, Laibach and Verona", [15, 16], "Congress diplomacy included coercive intervention.", "Trace the intervention doctrine and its weakening."),
        plan("Belgium and selective adaptation", [17, 6], "Adaptation preserved the Concert by revising Vienna.", "Use 1830 to reject a rigid-restoration caricature."),
        plan("Why 1848 came and failed", [18], "Use only bounded causes and no unsupported leader detail.", "Explain grievance convergence and mechanisms of defeat."),
        plan("Peace, repression and the final verdict", [19, 4, 14, 17], "Judge Vienna by both great-power peace and popular legitimacy.", "Conclude with a successful peace system and long-term legitimacy deficit."),
    ],
    [
        panel("Vienna's starting problem", "root-axes", ["NAPOLEON DEFEATED -> Europe needs reconstruction", "FEAR 1 -> renewed French hegemony", "FEAR 2 -> revolutionary and national contagion", "VIENNA 1814-15 -> strategic peace plus conservative restoration"], ["Post-Napoleonic reconstruction"]),
        panel("Three settlement principles", "comparison-table", ["LEGITIMACY -> restore dynasties", "BALANCE OF POWER -> contain France with buffers", "COMPENSATION -> reward victors with territory", "COMMON LIMIT -> populations do not supply consent"], ["Legitimacy and dynastic restoration", "Balance of power and buffers", "Compensation and territorial bargaining"]),
        panel("Northern and central map logic", "comparison-table", ["NETHERLANDS -> Belgium + Holland buffer France", "GERMAN LANDS -> 39-state Confederation under Austria", "PRUSSIA -> Rhineland, Westphalia and part of Saxony", "SWITZERLAND -> neutrality recognised"], ["Balance of power and buffers", "Germany: unity postponed", "Poland, Prussia and Switzerland"]),
        panel("Italian and Polish deferral", "comparison", ["ITALY -> Austria gets Lombardy and Venetia", "PIEDMONT -> strengthened by Genoa", "POLAND -> Congress Poland under Russian control", "RESULT -> national questions postponed, not resolved"], ["Italy: Austrian control and Piedmont's strengthening", "Poland, Prussia and Switzerland"]),
        panel("Concert operating mechanism", "causal-system", ["GREAT POWERS -> consult rather than fight immediately", "CONGRESSES -> periodic management of disputes", "STATUS QUO -> territorial and political order defended", "LIMIT -> no permanent treaty-state or democratic representation"], ["The Concert as diplomatic practice"]),
        panel("Concert versus Holy Alliance", "comparison", ["CONCERT -> broad practical great-power consultation", "HOLY ALLIANCE -> Russia, Austria, Prussia; symbolic conservatism", "OVERLAP -> both emerge in 1815 order", "RULE -> never use the names as synonyms"], ["Holy Alliance and practical limits"]),
        panel("Reintegration and repression", "comparison", ["AIX 1818 -> France readmitted to consultation", "CARLSBAD 1819 -> censorship and university control", "EXTERNAL LOGIC -> include a former enemy", "INTERNAL LOGIC -> exclude liberal-national dissent"], ["Aix-la-Chapelle and reintegration", "Carlsbad and domestic repression"]),
        panel("Intervention congress sequence", "timeline", ["TROPPAU 1820 -> intervention principle asserted", "LAIBACH 1821 -> intervention against revolution applied", "VERONA 1822 -> French intervention in Spain approved", "AFTER VERONA -> old congress rhythm weakens"], ["Intervention at Troppau, Laibach and Verona"]),
        panel("Belgium tests flexibility", "path-consequence", ["1815 -> Belgium joined with Holland as buffer", "1830 -> Belgian revolt breaks the arrangement", "CONCERT -> accepts independence", "LESSON -> adaptation can preserve wider equilibrium"], ["Belgium and selective adaptation"]),
        panel("1848 pressure and failure", "causal-system", ["PRESSURE -> national + liberal + social grievances converge", "DIVISION -> liberals, nationalists and workers differ", "CONFLICT -> national claims collide in multinational empires", "FORCE -> dynastic armies remain loyal and reverse revolutions"], ["Why 1848 came and failed"]),
        panel("Vienna's unintended gravediggers", "path-consequence", ["PRUSSIA GAINS RHINELAND -> stronger western base", "PIEDMONT GAINS GENOA -> stronger Italian state", "VIENNA INTENT -> reinforce conservative balance", "LATER RESULT -> strengthened states lead national unification"], ["Compensation and territorial bargaining", "Italy: Austrian control and Piedmont's strengthening"]),
        panel("Peace-versus-repression spine", "answer-spine", ["SUCCESS -> no renewed Napoleonic hegemony", "METHOD -> balance, reintegration and consultation", "COST -> censorship, intervention and denied nationality", "VERDICT -> peace among powers, legitimacy deficit among peoples"], ["Peace, repression and the final verdict"]),
    ],
    ["Congress of Vienna", "Metternich", "legitimacy", "balance of power", "compensation", "German Confederation", "39 states", "Concert of Europe", "Holy Alliance", "Aix-la-Chapelle", "Carlsbad Decrees", "Troppau", "Laibach", "Verona", "Belgian independence"],
    (
        "No direct UPSC PYQ is verified as owned solely by this topic in the "
        "local 2018-2025 routing blocks. Probable questions in the owners "
        "remain labelled as practice rather than converted into PYQs."
    ),
    [],
    extra=["basic/03_French-Revolution-and-Napoleon.md", "basic/06_Unification-of-Italy-and-Germany.md"],
)


ALL_TOPICS = [TOPIC_01, TOPIC_02, TOPIC_03, TOPIC_04, TOPIC_05]
