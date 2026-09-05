"""Durable learner-v2 content and master-flow specification for Political Ideologies.

Philosophy Optional, Paper II, Socio-Political Philosophy, official topic 5:
``Political Ideologies: Anarchism; Marxism and Socialism.``

Every doctrine, thinker, dated publication and criticism below is grounded in the
repository owners for this clause: the canonical owner ``Political-Ideologies.md``,
the retained layered learning session and workbook, the verified 2018-2025
Socio-Political PYQ ledger, and the Socio-Political advanced dossier.  Nothing
here is taken from a live source, and no publication year, quotation, statute or
constitutional provision is asserted that the repository sources do not already
carry.  No Indian government, party, leader or period is characterised, and no
country's political history is offered as proof or refutation of a doctrine.
"""

from __future__ import annotations

import re


TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-05"
TOPIC_TITLE = "Political Ideologies"
TOPIC_NUMBER = 5
SECTION_KEY = "paper-ii-socio-political-philosophy"
GENERATION_DATE = "2026-09-03"
OFFICIAL_SYLLABUS_VERBATIM = (
    "Political Ideologies: Anarchism; Marxism and Socialism."
)
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
    "Political-Ideologies.md"
)
ADVANCED_DOSSIER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\_advanced\\Socio-Political-Dossier.md"
)
PYQ_LEDGER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\"
    "_PYQ-SocioPolitical-2018-2025.md"
)
SUCCESSOR_MARKDOWN = (
    "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Philosophy\\"
    "Socio-Political\\learning-sessions\\topic-05\\g3\\"
    "topic-05_Complete-Learning-Session_2026-08-30.md"
)
ASSET_SLUG = "anarchism-marxism-socialism"
IMMUTABLE_GENERATION_PATHS = True


def visual(title: str, caption: str, *lines: str) -> dict[str, object]:
    return {"title": title, "caption": caption, "lines": list(lines)}


def session(
    title: str,
    plain: str,
    technical: str,
    answer: str,
    keywords: list[str],
    usage: str,
    mechanism: str,
    consequence: str,
    trap: str,
    objection: str,
    reply: str,
    limit: str,
    exam: str,
    revision: list[str],
    visuals: list[dict[str, object]],
) -> dict[str, object]:
    return {
        "title": title,
        "plain": plain,
        "technical": technical,
        "answer": answer,
        "keywords": keywords,
        "usage": usage,
        "mechanism": mechanism,
        "consequence": consequence,
        "trap": trap,
        "objection": objection,
        "reply": reply,
        "limit": limit,
        "exam": exam,
        "revision": revision,
        "visuals": visuals,
    }


SESSION_SPECS = (
    session(
        "Ideology, Domination and the Discriminating Question",
        "A political ideology is a connected body of belief that diagnoses what "
        "makes an existing social order unfree, names the institution or "
        "relation responsible for that unfreedom, and prescribes the route to a "
        "freer arrangement, so anarchism, Marxism and socialism are three rival "
        "diagnoses rather than three moods.",
        "Ideology in the analytical sense denotes a systematically related set "
        "of descriptive claims about society, evaluative commitments about "
        "freedom and equality, and practical prescriptions for action; in the "
        "critical Marxist sense it denotes the socially rooted framework "
        "through which historically specific relations of production appear "
        "natural, universal and inevitable, and a controlled answer declares "
        "which sense it is using before it begins to argue.",
        "Anarchism, Marxism and socialism are separated by one discriminating "
        "question — is domination produced chiefly by coercive authority, by "
        "the capitalist mode of production, or by socially uncontrolled "
        "productive property? — and every later disagreement about the state, "
        "revolution and freedom follows from the answer given.",
        [
            "political ideology as diagnosis and prescription",
            "the discriminating question of domination",
            "coercive authority",
            "capitalist mode of production",
            "social control of productive property",
            "analytical against critical senses of ideology",
        ],
        "Name the discriminating question of domination in the opening lines, "
        "allot one clause each to coercive authority, the capitalist mode of "
        "production and the social control of productive property, declare "
        "which sense of political ideology the stem is using, and only then "
        "let the diagnosis generate the prescription.",
        "Each ideology first locates the source of unfreedom, and its whole "
        "institutional programme — abolish the state, transform the mode of "
        "production, or socialise productive property — is derived from that "
        "single location rather than added to it.",
        "Because the diagnoses differ at the root, the three doctrines part "
        "company over the state itself: one demands its abolition, one its "
        "transitional capture, and one its democratic use.",
        "Do not use ideology as a term of abuse, and do not treat it as a "
        "synonym for neutral political theory; the analytical sense is "
        "avowedly action-guiding, while the critical sense is a specific "
        "thesis about how class relations are made to look natural.",
        "If every ideology is a socially rooted framework that makes a "
        "particular order appear natural, the critic's own position is equally "
        "ideological, so the concept destroys the very standpoint from which "
        "the criticism was to be made.",
        "The objection runs together the two senses the session has just "
        "separated. Ideology in the descriptive sense is an organised "
        "political outlook, which the critic openly avows and submits to "
        "argument; ideology in the critical sense names a specific defect — "
        "the presentation of historically specific class relations as natural, "
        "universal and inevitable. A doctrine may hold the first without "
        "committing the second, provided it states its presuppositions and "
        "argues for them.",
        "The distinction supplies no independent test that decides, in a "
        "contested case, whether a shared belief is ordinary reasoned "
        "agreement or manufactured consent — the residual difficulty later "
        "inherited by Gramsci's account of hegemony.",
        "Open with the discriminating question, place each named ideology on "
        "it in a single line, declare the sense of ideology in play, and fix "
        "the shared axes — authority, property, class, revolution, state and "
        "freedom — so that the later comparison runs down parallel columns "
        "instead of collapsing into three disconnected summaries.",
        [
            "One discriminating question orders the whole clause: is "
            "domination caused by authority, by the mode of production, or by "
            "uncontrolled productive property?",
            "Anarchism answers authority; Marxism answers class relations "
            "generated by the mode of production; socialism answers socially "
            "uncontrolled property and production.",
            "Ideology has two senses — the analytical outlook and the critical "
            "Marxist thesis — and the sense must be declared before it is "
            "used.",
            "The recurrent axes for every comparison in this clause are "
            "authority, property, class, revolution, state and freedom.",
            "A diagnosis generates a prescription; an answer that lists "
            "prescriptions without their diagnoses has already lost the "
            "structure.",
        ],
        [
            visual(
                "The discriminating question and its three answers",
                "The opening move for almost every stem in this clause: fix "
                "the diagnosis first, and the institutional programme follows "
                "from it.",
                "        CAPITALISM  /  HIERARCHY  /  COERCION",
                "                        |",
                "     WHAT CHIEFLY PRODUCES DOMINATION IN SOCIETY?",
                "                        |",
                "   +--------------------+--------------------+",
                "   v                    v                    v",
                "ANARCHISM            MARXISM              SOCIALISM",
                "coercive authority   class relations       socially",
                "itself, above all    generated by the      uncontrolled",
                "the sovereign state  mode of production    productive property",
                "   |                    |                    |",
                "   v                    v                    v",
                "abolish the state    transitional worker   subject ownership",
                "and every standing   power, then a         and production to",
                "hierarchy            classless order       social control",
                "   |                    |                    |",
                "   +--------------------+--------------------+",
                "                        v",
                "  SAME DECLARED GOAL -> a free, equal, non-dominating order;",
                "  DIFFERENT ROUTE    -> because the diagnosis differed first.",
            ),
            visual(
                "Two senses of ideology that must never be run together",
                "Declaring the sense in the opening paragraph prevents the "
                "self-refutation objection from ever getting started.",
                "+---------------------+----------------------------------------------+",
                "| SENSE               | WHAT IT ASSERTS                              |",
                "+---------------------+----------------------------------------------+",
                "| ANALYTICAL          | an organised outlook: descriptive claims,    |",
                "| (neutral, avowed)   | evaluative commitments, practical            |",
                "|                     | prescriptions, held openly and argued for    |",
                "+---------------------+----------------------------------------------+",
                "| CRITICAL / MARXIST  | a socially rooted framework in which         |",
                "| (a specific defect) | historically specific class relations appear |",
                "|                     | natural, universal and inevitable            |",
                "+---------------------+----------------------------------------------+",
                "  TEST -> the first is compatible with self-criticism; the second",
                "          names a failure of self-knowledge inside a class order.",
            ),
        ],
    ),
    session(
        "Anarchism I: The Argument Against the Authority of the State",
        "Anarchism holds that coercive political authority — above all the "
        "sovereign state with its territorial monopoly of law-making, coercion "
        "and punishment — lacks adequate moral justification, and that social "
        "order can instead be organised through voluntary association, mutual "
        "aid, federation and self-government.",
        "The anarchist case is a burden-of-justification argument in five "
        "steps: legitimate authority must be compatible with the moral "
        "autonomy and equality of persons; the state claims a territorial "
        "monopoly of law, coercion and punishment; obedience is demanded "
        "because a command is legally authoritative rather than because its "
        "content is independently right; such a standing right subordinates "
        "one person's practical judgment to another's institutional will; "
        "therefore the state bears a justificatory burden that anarchists "
        "judge it unable to discharge.",
        "The anarchist thesis is not that order is unnecessary but that order "
        "must not be identified with sovereign command: the state is asked to "
        "justify a content-independent right to be obeyed, and anarchism holds "
        "that no available justification discharges that burden.",
        [
            "coercive political authority",
            "territorial monopoly of law, coercion and punishment",
            "moral autonomy and equality of persons",
            "content-independent obligation to obey the state",
            "burden of justification",
            "Bakunin's corruption thesis",
            "Proudhon on property as institutional power",
            "Kropotkin on mutual aid as a source of order",
        ],
        "Run the five-step burden-of-justification argument against the state "
        "before any evaluation, using the moral autonomy and equality of "
        "persons as the standard, the territorial monopoly of law, coercion "
        "and punishment as the object, and the content-independent obligation "
        "to obey as the precise target; add Bakunin's corruption thesis, "
        "Proudhon on property and Kropotkin on mutual aid as named support.",
        "Because the state claims a right to be obeyed that is independent of "
        "the content of what it commands, its justification cannot be "
        "completed by pointing at good laws; every function it monopolises "
        "must be shown to require a sovereign centre and not merely to be "
        "performed by one.",
        "Where the burden is not discharged, obedience becomes prudential "
        "rather than obligatory, which is exactly the position philosophical "
        "anarchism occupies without any call to immediate insurrection.",
        "Do not translate the argument as a rejection of organisation or "
        "coordination; the target is domination, and delegation, recall and "
        "federation all survive it, so anarchy as disorder is never what "
        "anarchism as a doctrine proposes.",
        "Without a public authority holding a monopoly of force, private "
        "power, organised violence and predation would dominate instead, so "
        "the state is at worst the lesser evil and the anarchist argument "
        "proves too much.",
        "The state has itself historically organised war, repression and "
        "structural domination, so the real comparison is not between coercion "
        "and its absence but between rival distributions of coercive power. "
        "Federated defence, restorative institutions and recallable delegation "
        "can address aggression without reproducing a sovereign hierarchy, and "
        "the anarchist needs only the weaker claim that centralised coercion "
        "is not the unique or best remedy.",
        "No anarchist account has yet shown how a persistent and organised "
        "aggressor is to be restrained without something that functions, at "
        "least temporarily, as a coercive public authority.",
        "Define anarchism against anarchy in one line, run the five-step "
        "argument as numbered premises, name Proudhon, Bakunin and Kropotkin "
        "for their distinct contributions, take the security objection at its "
        "strongest, and close on a graded verdict that concedes the "
        "coordination residual while retaining the critique of sovereignty.",
        [
            "Anarchism is a normative critique of domination; anarchy may mean "
            "the mere collapse of rule, and the two must never be equated.",
            "The precise target is the content-independent right to be obeyed, "
            "not the badness of particular laws.",
            "Proudhon attacks property as an institutional power of "
            "appropriation and dependence; Bakunin adds that concentrated "
            "power deforms ruler and ruled alike; Kropotkin argues that mutual "
            "aid is a genuine source of order.",
            "Anarchism rejects even the libertarian minimal state, because the "
            "objection is to the monopoly and not to the size of what is "
            "monopolised.",
            "Civil disobedience breaches particular laws without rejecting the "
            "state, so it is a neighbouring but distinct position.",
        ],
        [
            visual(
                "The five-step burden-of-justification argument",
                "Reproduce these premises as numbered steps: the marks are in "
                "the conclusion that the state carries the burden, not in a "
                "general dislike of government.",
                "  (1) Legitimate authority must be compatible with the MORAL",
                "      AUTONOMY and EQUALITY of persons",
                "                 |",
                "                 v",
                "  (2) The state claims a TERRITORIAL MONOPOLY of law-making,",
                "      coercion and punishment",
                "                 |",
                "                 v",
                "  (3) Obedience is demanded because the command is LEGALLY",
                "      AUTHORITATIVE, not because its content is independently right",
                "                 |",
                "                 v",
                "  (4) That standing right SUBORDINATES one person's judgment to",
                "      another's institutional will",
                "                 |",
                "                 v",
                "  (5) THEREFORE the state bears a burden of justification which",
                "      anarchists judge it unable to discharge",
                "                 |",
                "                 v",
                "  NOTE -> the conclusion is about the TITLE to command, so showing",
                "          that particular laws are good does not answer it.",
            ),
            visual(
                "Four neighbouring terms that examiners deliberately confuse",
                "The discriminating test in the right-hand column is what "
                "converts a definition into a mark-bearing distinction.",
                "+------------------------+---------------------------+------------------------+",
                "| TERM                   | MEANING                   | DISCRIMINATING TEST    |",
                "+------------------------+---------------------------+------------------------+",
                "| ANARCHY                | absence or collapse of    | may simply mean        |",
                "|                        | effective rule            | disorder               |",
                "| ANARCHISM              | normative critique of     | proposes non-coercive  |",
                "|                        | domination                | order                  |",
                "| CIVIL DISOBEDIENCE     | principled breach of      | need not reject the    |",
                "|                        | particular laws           | state at all           |",
                "| LIBERTARIAN MINIMAL    | state restricted to       | anarchism rejects even |",
                "| STATE                  | protection                | this monopoly          |",
                "+------------------------+---------------------------+------------------------+",
            ),
        ],
    ),
    session(
        "Anarchism II: Strands, Voluntary Order, Objections and Gandhi",
        "Anarchism is a family rather than a single programme: mutualists, "
        "collectivists, anarcho-communists, individualists and philosophical "
        "anarchists agree that domination must go but divide over productive "
        "property, and Gandhi belongs to this family only in a carefully "
        "qualified sense.",
        "The strands are distinguished by their treatment of productive "
        "property and their preferred form of non-sovereign order: possession "
        "and exchange without exploitative property relations in mutualism "
        "(Proudhon); collective control of productive resources in federated "
        "producer communities in collectivist anarchism (Bakunin); common "
        "ownership with distribution by need in anarcho-communism (Kropotkin); "
        "strong personal sovereignty with varying views on markets in "
        "individualist anarchism; and, in philosophical anarchism, the denial "
        "of any automatic duty to obey the state, which may coexist with "
        "critical allegiance to existing institutions.",
        "Anarchism does not infer that every person is always benevolent; its "
        "claim is institutional — that reciprocity, custom, association and "
        "horizontal coordination can generate order without a final coercive "
        "superior — and Gandhi enters this family as an anarchist in ideal but "
        "a reformer in political method.",
        [
            "mutualism",
            "collectivist anarchism",
            "anarcho-communism",
            "individualist anarchism",
            "philosophical anarchism",
            "mutual aid, federation and recallable delegation",
            "anarchist in ideal, reformer in method",
        ],
        "Open by refusing the single-programme assumption, run mutualism, "
        "collectivist anarchism, anarcho-communism, individualist anarchism "
        "and philosophical anarchism down the property axis, ground voluntary "
        "order in mutual aid and federation rather than in optimism about "
        "human nature, and grade Gandhi with the ideal-against-method "
        "formulation instead of a flat yes or no.",
        "Once the property axis is made explicit, the strands stop looking "
        "like temperaments and become determinate positions on who may control "
        "productive resources and on how coordination is to be organised "
        "without a sovereign centre.",
        "A stem that asks whether one subscribes to anarchism therefore cannot "
        "be answered about anarchism as such: the strand has to be named "
        "before agreement or disagreement can be stated at all.",
        "Do not present every anarchist as a collectivist, and do not read "
        "Gandhi as a Bakuninite; his non-violence, trusteeship, religious "
        "ethics and constructive programme replace class war and anti-theism, "
        "which is why the safest verdict is qualified rather than flat.",
        "Even after the state disappears, expertise, informal status, wealth "
        "and reputation return as hidden authorities, so voluntary "
        "associations reproduce domination under a different name and the "
        "abolition achieves nothing.",
        "This is the most serious internal challenge and should be conceded as "
        "such. A defensible anarchism replies that it opposes domination "
        "rather than formal office, so its own institutions must be scrutinised "
        "by the same standard: rotation, recall, transparency, federation and "
        "the refusal of permanent delegation are proposed precisely to keep "
        "informal power answerable. The doctrine is therefore committed to "
        "auditing itself, not merely to abolishing the state.",
        "No anarchist account supplies an independent criterion for deciding "
        "when a voluntary association has itself become a domination, which "
        "leaves the internal audit without a settled test.",
        "Name the strand the stem requires, run the property axis across the "
        "family, show that voluntary order rests on an institutional claim "
        "rather than on optimism about human nature, take the hidden-authority "
        "objection at full strength, and grade Gandhi as an anarchist in ideal "
        "and a reformer in method with the reasons on both sides.",
        [
            "Mutualism: possession and exchange without exploitative property "
            "relations, organised through contracts and workers' associations.",
            "Collectivist anarchism: collective control of productive "
            "resources through federated producer communities.",
            "Anarcho-communism: common ownership with distribution according "
            "to need, organised through communes and mutual aid.",
            "Individualist anarchism: strong personal sovereignty, voluntary "
            "association, and varying views about markets.",
            "Philosophical anarchism: no automatic duty to obey, but no demand "
            "for immediate insurrection either.",
            "Gandhi: self-rule, decentralised village republics and a minimal "
            "state give the anarchist affinity; non-violence, trusteeship and "
            "the constructive programme make the method reformist.",
        ],
        [
            visual(
                "The anarchist family tree, sorted by the property axis",
                "Every strand answers the same question about productive "
                "property differently, which is why a stem must be answered "
                "about a strand and not about anarchism in general.",
                "                     ANARCHISM",
                "        (coercive authority is the root problem)",
                "                          |",
                "     +--------+-----------+-----------+-----------+",
                "     v        v           v           v           v",
                "MUTUALISM  COLLECTIVIST  ANARCHO-   INDIVIDUALIST  PHILOSOPHICAL",
                "           ANARCHISM     COMMUNISM  ANARCHISM      ANARCHISM",
                "     |        |           |           |           |",
                "     v        v           v           v           v",
                "possession collective   common      personal     no automatic",
                "and free   control of   ownership,  sovereignty; duty to obey;",
                "exchange   productive   distribution markets     critical",
                "           resources    by need      contested   allegiance",
                "     |        |           |           |           |",
                "     v        v           v           v           v",
                "Proudhon   Bakunin      Kropotkin   Thoreauvian  legitimacy,",
                "                                     resistance   not revolt",
                "  AXIS OF DIVISION -> who may control productive property, and",
                "                      what replaces the sovereign centre.",
            ),
            visual(
                "Four objections to stateless order and the anarchist replies",
                "The fourth objection is the one that decides the grade, "
                "because it is internal and the honest reply concedes a "
                "residual.",
                "OBJECTION 1  security dilemma      -> REPLY: the state itself has",
                "  private power may dominate          organised war and repression",
                "OBJECTION 2  scale and public goods -> REPLY: it rejects centralised",
                "  pandemics, infrastructure           domination, not coordination",
                "OBJECTION 3  optimistic anthropology-> REPLY: it need only deny that",
                "  egoism and conflict persist         hierarchy is the best remedy",
                "OBJECTION 4  hidden authority       -> REPLY: a serious internal",
                "  expertise, status, wealth           challenge; audit domination",
                "                                      inside voluntary bodies too",
                "        |",
                "        v",
                "  RESIDUAL -> no independent test says when a voluntary association",
                "              has itself become a domination.",
            ),
        ],
    ),
    session(
        "Marxism I: Materialist Method and Historical Materialism",
        "Historical materialism explains a society by beginning from how it "
        "produces its means of life: the productive forces it commands, the "
        "relations of ownership and control through which those forces are "
        "used, and the class structure and political institutions those "
        "relations sustain.",
        "Marxism is simultaneously a method of dialectical and historical "
        "analysis, a critique of exploitation, alienation, commodity relations "
        "and ideology, a theory of change through contradiction and class "
        "struggle, and a political project of collective emancipation; "
        "historical materialism is its explanatory core, in which developing "
        "productive forces eventually come into conflict with the existing "
        "relations of production, those relations become fetters, and the "
        "conflict is fought out as social and political struggle from which a "
        "new mode of production can emerge.",
        "Marx takes from Hegel that contradiction drives development while "
        "rejecting the primacy of a self-developing Idea: the contradiction "
        "that moves history is between developing productive forces and the "
        "relations of production that come to fetter them, so the economic "
        "base conditions the superstructure without mechanically causing every "
        "idea within it.",
        [
            "productive forces",
            "relations of production",
            "mode of production",
            "base and superstructure",
            "class struggle as the motor of transformation",
            "relations of production as fetters",
            "material reproduction as a necessary condition",
        ],
        "State the six-step argument from material reproduction to the "
        "fettering of productive forces, define productive forces, relations "
        "of production and mode of production in technical vocabulary, present "
        "base and superstructure as a relation rather than a switch, and let "
        "class struggle enter as the mechanism by which the contradiction "
        "becomes political.",
        "Human beings must produce the means of life through definite social "
        "relations, productive forces develop within those relations, the "
        "relations eventually obstruct further development, and that "
        "obstruction becomes social and political struggle.",
        "History therefore has a direction supplied by a structural conflict "
        "rather than by intention, and law, politics and ideology have to be "
        "studied in relation to social labour and power rather than as "
        "self-standing spheres.",
        "Do not write base and superstructure as a mechanical one-way cause, "
        "and never attribute the formula thesis-antithesis-synthesis to Marx "
        "as his own fixed three-step law, because it is a later textbook "
        "shorthand and the concession costs nothing while the error costs the "
        "answer.",
        "Historical materialism reduces history to economics and cannot "
        "explain culture, caste, religion, gender or nationalism, all of which "
        "display an autonomy that a productive-forces explanation cannot "
        "capture.",
        "Historical materialism can treat these as materially embedded powers "
        "rather than as epiphenomena, and Marx himself allows reciprocal "
        "effects and political agency, so the accurate charge is a tendency "
        "toward economic reductionism rather than a crude determinism he never "
        "held. Later Marxists expand the analysis explicitly through hegemony "
        "and the reproduction of social relations, which relocates causal "
        "weight without abandoning the materialist mechanism.",
        "In the Indian context class analysis remains necessary but is not "
        "sufficient: caste and gender operate through mechanisms of status, "
        "endogamy and social reproduction that cannot be derived from class "
        "alone.",
        "Open on material reproduction as a necessary condition of every "
        "social order, run the six premises to the fetters conclusion, define "
        "the four structural terms precisely, defuse the determinism charge "
        "before it is made, and close by separating what the framework still "
        "explains from what it must borrow to explain.",
        [
            "Productive forces are labour-power, knowledge, tools and "
            "technology — the capacity to produce.",
            "Relations of production are ownership, control and class "
            "relations — who commands and who appropriates.",
            "Mode of production is the unity of forces and relations, such as "
            "feudalism or capitalism.",
            "Base and superstructure name a relation between the economic "
            "structure and law, politics and ideology, not a mechanical "
            "one-way switch.",
            "Class struggle is conflict rooted in opposed structural interests "
            "and is the motor of historical transformation.",
            "Concede the reductionism tendency early; it removes the examiner's "
            "strongest ready-made objection.",
        ],
        [
            visual(
                "From material reproduction to revolutionary transformation",
                "Six premises, not slogans: reproduce them as a numbered chain "
                "and the historical-materialism stem is already half answered.",
                "  (1) Human beings must PRODUCE THE MEANS OF LIFE",
                "                 |",
                "                 v",
                "  (2) Production occurs through DEFINITE SOCIAL RELATIONS",
                "                 |",
                "                 v",
                "  (3) PRODUCTIVE FORCES develop within those relations",
                "                 |",
                "                 v",
                "  (4) Existing RELATIONS eventually OBSTRUCT further development",
                "      (the relations become FETTERS)",
                "                 |",
                "                 v",
                "  (5) The conflict between forces and relations becomes SOCIAL",
                "      AND POLITICAL STRUGGLE",
                "                 |",
                "                 v",
                "  (6) A NEW MODE OF PRODUCTION can emerge through that struggle",
                "  CONTROL -> the chain is structural, so no step depends on anyone",
                "             intending the outcome that follows.",
            ),
            visual(
                "The four structural terms and what each is used to say",
                "Defining these four precisely is the difference between an "
                "exposition of historical materialism and a summary of it.",
                "+------------------------+-------------------------------+-------------------+",
                "| TERM                   | WHAT IT NAMES                 | EXAM USE          |",
                "+------------------------+-------------------------------+-------------------+",
                "| PRODUCTIVE FORCES      | labour-power, knowledge,      | capacity to       |",
                "|                        | tools, technology             | produce           |",
                "| RELATIONS OF           | ownership, control and class  | who commands and  |",
                "| PRODUCTION             | relations                     | who appropriates  |",
                "| MODE OF PRODUCTION     | the unity of forces and       | feudalism,        |",
                "|                        | relations                     | capitalism        |",
                "| BASE / SUPERSTRUCTURE  | economic structure related to | a relation, never |",
                "|                        | law, politics and ideology    | a one-way switch  |",
                "+------------------------+-------------------------------+-------------------+",
                "  TRAP -> thesis-antithesis-synthesis is later textbook shorthand,",
                "          not Marx's own stated three-step law.",
            ),
        ],
    ),
    session(
        "Marxism II: Alienation, Exploitation and Surplus Value",
        "Alienation names the condition in which a worker's own activity and "
        "its product confront him as something alien and controlled by "
        "another, while exploitation names the structural relation through "
        "which the value produced during the working day exceeds the value "
        "represented by the wage.",
        "In the Economic and Philosophic Manuscripts of 1844 capitalist labour "
        "estranges the worker in four dimensions — from the product, which "
        "confronts the producer as another's property; from the activity of "
        "labour, which is externally compelled rather than self-realising; "
        "from species-being, in that conscious creative activity is reduced to "
        "a means of survival; and from other persons, as workers compete and "
        "social relations assume commodity form. Exploitation is a distinct "
        "structural claim: labour-power is purchased through a formally free "
        "contract, the capitalist controls the labour process and the product, "
        "and the excess of value created over the value of labour-power is "
        "appropriated as surplus value.",
        "Alienation is not low pay and exploitation is not theft: a well-paid "
        "worker remains alienated wherever labour, product and purpose are "
        "controlled by another, and exploitation arises through a formally "
        "free contract because the value labour creates exceeds the value its "
        "wage represents.",
        [
            "estrangement from the product",
            "estrangement from the activity of labour",
            "species-being",
            "estrangement from other persons",
            "labour-power sold under a formally free contract",
            "surplus value",
            "structural exploitation against unfair bargaining",
        ],
        "Define estrangement under conditions of private property and the "
        "division of labour, run the four dimensions in order, make the "
        "distinction from low wages explicitly because it is the mark-bearing "
        "move, then switch registers to exploitation: labour-power, the "
        "formally free contract, control of the labour process, and surplus "
        "value as a structural rather than a personal wrong.",
        "Workers lack independent access to the means of production and must "
        "therefore sell labour-power to live, the capitalist controls the "
        "labour process and the product, and competition compels accumulation "
        "and the extraction of surplus.",
        "Exploitation is therefore not reducible to a cruel employer's "
        "intention, and redistribution that reduces inequality of holdings may "
        "leave the exploitative control of production entirely intact.",
        "Do not treat alienation as a psychological complaint about "
        "dissatisfaction, and do not equate exploitation with inequality; the "
        "first concerns control over activity, product and purpose, and the "
        "second concerns the social relation of production rather than the "
        "distribution of holdings.",
        "The concept of species-being presupposes a controversial universal "
        "human essence, so the whole account of alienation rests on a "
        "metaphysical anthropology that a critic need not accept.",
        "Species-being can be reconstructed minimally without positing a fixed "
        "metaphysical essence: persons require meaningful agency, social "
        "recognition and control over their central activities, and the claim "
        "that labour organised so as to deny all three damages the person is "
        "far weaker than a full theory of human nature. The diagnosis then "
        "survives even for a reader who rejects the 1844 anthropology, which "
        "is precisely why later structuralist Marxism could displace the "
        "humanist vocabulary without discarding the critique of capitalist "
        "work.",
        "The labour theory of value on which the classical account of surplus "
        "value rests is economically contested, so an answer should argue the "
        "structural point about control and appropriation rather than defend a "
        "theory of prices.",
        "Open with estrangement under private property and the division of "
        "labour, give the four dimensions with one line each, make the "
        "not-low-wages distinction the hinge of the answer, move to labour-power "
        "and surplus value for the structural claim, and close by separating "
        "exploitation from inequality so the verdict on redistribution is "
        "properly qualified.",
        [
            "Four dimensions: from the product, from the act of production, "
            "from species-being, from other human beings.",
            "Alienation is broader than low wages — control over labour, "
            "product and purpose is the operative variable.",
            "Labour-power is bought through a formally free contract, which is "
            "why exploitation is not theft.",
            "Surplus value is the value created beyond the value represented "
            "by the wage, appropriated by the owner of capital.",
            "Exploitation concerns the relation of production; inequality "
            "concerns the distribution of holdings — never merge them.",
            "Human flourishing on this account includes conscious, social and "
            "creative activity, not merely preference-satisfaction.",
        ],
        [
            visual(
                "The four dimensions of alienated labour",
                "The order matters: the first two are about the labour "
                "process, the third about the person, and the fourth about "
                "social relations turning into commodity relations.",
                "     CAPITALIST LABOUR under private property and division of labour",
                "                          |",
                "     +---------+----------+----------+----------+",
                "     v         v          v          v",
                "  FROM THE   FROM THE   FROM       FROM OTHER",
                "  PRODUCT    ACT OF     SPECIES-   PERSONS",
                "             LABOUR     BEING",
                "     |         |          |          |",
                "     v         v          v          v",
                "  it faces   work is    conscious  workers compete;",
                "  the maker  externally creative   social relations",
                "  as another compelled, activity   assume commodity",
                "  person's   not self-  reduced to form",
                "  property   realising  survival",
                "                          |",
                "                          v",
                "  KEY DISTINCTION -> a WELL-PAID worker can still be alienated,",
                "                     so alienation is broader than low wages.",
            ),
            visual(
                "Why exploitation is structural and not theft",
                "Each step is a premise; the conclusion is that no cruel "
                "intention is required for exploitation to occur.",
                "  (1) Workers lack independent access to the MEANS OF PRODUCTION",
                "                 |",
                "                 v",
                "  (2) They must SELL LABOUR-POWER to live -> formally FREE contract",
                "                 |",
                "                 v",
                "  (3) The capitalist CONTROLS the labour process and the product",
                "                 |",
                "                 v",
                "  (4) COMPETITION compels accumulation and extraction of surplus",
                "                 |",
                "                 v",
                "  (5) Value created in the day EXCEEDS value represented by wages",
                "      -> the remainder is appropriated as SURPLUS VALUE",
                "                 |",
                "                 v",
                "  VERDICT -> exploitation is a RELATION OF PRODUCTION, so",
                "             redistribution alone may leave it untouched.",
            ),
        ],
    ),
    session(
        "Marxism III: Ideology, the State, Revolution and Equality",
        "On the classical Marxist account the state is not a neutral umpire "
        "but an institution that secures the general conditions of the "
        "prevailing class order while presenting itself as the representative "
        "of a universal interest, and revolution is the political resolution "
        "of the contradiction between socialised production and private "
        "appropriation.",
        "Ideology here is not merely a lie but a socially rooted framework "
        "through which historically specific relations appear natural, "
        "universal or inevitable; the modern state secures the general "
        "conditions of the capitalist order, which is compatible with relative "
        "autonomy from any particular capitalist; the dictatorship of the "
        "proletariat denotes a transitional political supremacy of the working "
        "class rather than a licence for permanent one-party rule; and "
        "communism denotes the projected classless order in which the "
        "political state as an instrument of class domination ceases to be "
        "necessary, distribution moving from the measure of contribution in "
        "the lower phase toward provision according to need in the higher.",
        "The dictatorship of the proletariat denotes a transitional political "
        "supremacy of the working class and not a textual licence for "
        "permanent one-party dictatorship, and Marxian socialism is consistent "
        "with individual freedom only where collective ownership genuinely "
        "enlarges self-development and democratic control.",
        [
            "ideology as a socially rooted framework",
            "the state's general conditions of the class order",
            "relative autonomy compatible with class function",
            "socialised production against private appropriation",
            "dictatorship of the proletariat as transitional supremacy",
            "lower and higher phases of communist society",
            "formal against substantive equality",
            "equity as differential provision justified by need",
        ],
        "Define ideology as a socially rooted framework rather than a lie, "
        "present the state as securing the general conditions of the class "
        "order while retaining relative autonomy, derive revolution from the "
        "contradiction between socialised production and private "
        "appropriation, read the dictatorship of the proletariat as a "
        "transitional supremacy, and finish on formal against substantive "
        "equality with equity as differential provision justified by need.",
        "Capitalism socialises production while retaining private "
        "appropriation, and that contradiction, together with organised class "
        "struggle, is what makes revolutionary transformation possible rather "
        "than merely desirable.",
        "Equal legal right applied over radically unequal social conditions "
        "therefore conceals rather than corrects unequal productive power, "
        "which is why the Marxian verdict on formal equality is critical "
        "without being dismissive of legal equality as such.",
        "Do not claim that Marx supplies a detailed blueprint of communist "
        "institutions, and do not read the transitional formula as a defence "
        "of permanent party rule; his account of the future order is "
        "deliberately limited, and the qualification must be stated rather "
        "than assumed.",
        "Transitional states created in the name of this doctrine have "
        "entrenched themselves rather than withered away, so the theory "
        "predicts emancipation and delivers a new apparatus of domination.",
        "This is the strongest historical objection available and it should be "
        "conceded rather than deflected. The reply available to a Marxist is "
        "not that the record is irrelevant but that the transition must be "
        "designed differently: constitutional liberty, plural organisation, "
        "recall and accountability have to be built into the transitional "
        "arrangement rather than postponed until after it, since a collective "
        "power that becomes bureaucratic command defeats the emancipatory "
        "claim on which the whole doctrine rests.",
        "The theory supplies no internal institutional safeguard that "
        "guarantees the transitional state will dissolve, so the residual "
        "risk of a new ruling stratum remains unanswered from within "
        "classical Marxism.",
        "Open by separating ideology from falsehood, take the state as class "
        "function plus relative autonomy, run the socialised-production "
        "contradiction to revolution, insist on the transitional reading of "
        "proletarian supremacy, then decide the freedom question on whether "
        "collective ownership actually enlarges self-development and "
        "democratic control.",
        [
            "Ideology is a socially rooted framework, not a simple lie — the "
            "distinction is examined directly.",
            "The state secures the general conditions of the capitalist order; "
            "relative autonomy is compatible with structural class function.",
            "Revolution follows from socialised production held under private "
            "appropriation, plus organised class struggle.",
            "Dictatorship of the proletariat means transitional supremacy of "
            "the working class, not permanent one-party rule.",
            "Lower phase distributes by contribution and retains a bourgeois "
            "measure; the higher phase aspires to distribution by need.",
            "Formal equality asks whether the same rule applies; substantive "
            "equality asks whether persons can actually develop and "
            "participate.",
            "Freedom is non-domination plus self-development: ask freedom from "
            "whom, and for what activity.",
        ],
        [
            visual(
                "From the capitalist contradiction to the classless order",
                "The rail to reproduce in any revolution or communism stem; "
                "the two phases at the end are what separate a controlled "
                "answer from an enthusiastic one.",
                "  SOCIALISED PRODUCTION  +  PRIVATE APPROPRIATION",
                "                 |  (contradiction)",
                "                 v",
                "  ORGANISED CLASS STRUGGLE makes transformation POSSIBLE",
                "                 |",
                "                 v",
                "  DICTATORSHIP OF THE PROLETARIAT",
                "  = transitional POLITICAL SUPREMACY of the working class",
                "  != a licence for permanent one-party dictatorship",
                "                 |",
                "                 v",
                "  LOWER PHASE  -> distribution by CONTRIBUTION; a bourgeois",
                "                  measure survives",
                "                 |",
                "                 v",
                "  HIGHER PHASE -> distribution according to NEED; the political",
                "                  state as class instrument becomes unnecessary",
                "  RESIDUAL -> nothing internal to the theory guarantees that the",
                "              transitional apparatus will actually dissolve.",
            ),
            visual(
                "Four concepts that the equality question keeps separate",
                "Answering an equality or freedom stem without this grid "
                "produces assertion; answering with it produces adjudication.",
                "+----------------------+--------------------------------+-------------------+",
                "| CONCEPT              | QUESTION IT ASKS                | MARXIAN CONCERN  |",
                "+----------------------+--------------------------------+-------------------+",
                "| FORMAL EQUALITY      | is the same rule applied?      | may conceal      |",
                "|                      |                                | unequal power    |",
                "| SUBSTANTIVE EQUALITY | can persons actually develop   | requires altered |",
                "|                      | and participate?               | social condition |",
                "| EQUITY               | what differential provision is | avoids treating  |",
                "|                      | justified by need?             | unlike alike     |",
                "| FREEDOM              | freedom from whom, and for     | non-domination + |",
                "|                      | what activity?                 | self-development |",
                "+----------------------+--------------------------------+-------------------+",
                "  VERDICT LINE -> collective ownership is emancipatory only where it",
                "                  enlarges real self-development and democratic control.",
            ),
        ],
    ),
    session(
        "Marx After Marx: Lenin, Gramsci, Althusser and the State Debate",
        "Neo-Marxism is the family of later revisions that keeps the "
        "materialist mechanism while relocating causal weight from the "
        "economic base into party organisation, culture, state form and the "
        "making of political subjects.",
        "Four classical claims are revised on determinate grounds: Lenin "
        "replaces the expectation that revolution matures where capitalism is "
        "most advanced with imperialism, the weakest link and a vanguard party "
        "operating under democratic centralism; Gramsci replaces ideology as a "
        "reflex of the base with hegemony, an active achievement won and lost "
        "in civil society through organic intellectuals and a war of position; "
        "Miliband's instrumentalist account of state personnel and leverage in "
        "The State in Capitalist Society (1969) is answered by Poulantzas's "
        "relative autonomy and the state as a condensation of class forces in "
        "Political Power and Social Classes (1973); and Althusser replaces the "
        "humanist categories of alienation and species-being with Repressive "
        "and Ideological State Apparatuses and the interpellation of "
        "individuals as subjects.",
        "Neo-Marxism does not abandon the materialist mechanism but relocates "
        "causal weight into party, culture, state form and subject-formation, "
        "so an answer that names which classical claim each successor revises, "
        "and on what ground, controls the entire trajectory instead of "
        "reporting positions.",
        [
            "imperialism and the weakest link",
            "vanguard party and democratic centralism",
            "substitutionism",
            "hegemony in civil society",
            "organic intellectuals and the war of position",
            "Repressive and Ideological State Apparatuses",
            "interpellation and overdetermination",
            "instrumentalism against relative autonomy",
        ],
        "Take one classical claim at a time, name its reviser, and state the "
        "ground: imperialism and the weakest link with the vanguard party and "
        "democratic centralism for Lenin, hegemony in civil society with "
        "organic intellectuals and the war of position for Gramsci, the "
        "Repressive and Ideological State Apparatuses with interpellation for "
        "Althusser, and instrumentalism against relative autonomy for the "
        "Miliband-Poulantzas exchange.",
        "Each revision is prompted by a determinate explanatory failure — "
        "revolution did not occur where it was expected, capitalism survived "
        "crisis in the West, the state acted against particular capitalists, "
        "and consent was renewed daily rather than imposed — so the trajectory "
        "is driven by evidence rather than by fashion.",
        "The cumulative result is that the superstructure acquires real causal "
        "weight, which strengthens the account of stability while making the "
        "account of change harder to state, most sharply in Althusser.",
        "Do not run Gramsci and Althusser together as one neo-Marxist theory "
        "of ideology: civil society is a terrain of contest where hegemony can "
        "be lost and counter-hegemony built, whereas the apparatuses are "
        "primarily mechanisms of reproduction, and the difference is exactly "
        "what examiners reward.",
        "If revolutionary consciousness must be brought to the class from "
        "outside by a disciplined party, the instrument becomes a new ruling "
        "stratum: the party stands for the class, the central committee for "
        "the party, and the leadership for the committee.",
        "Leninists reply that democratic centralism includes free discussion "
        "before decision together with accountability and recall, and that "
        "emergency centralisation was a response to repression rather than a "
        "permanent constitutional principle. The reply is genuine but "
        "incomplete, and the honest presentation concedes the point: nothing "
        "in the model reliably subordinates the party to the class it claims "
        "to represent, which is why Bakunin's warning about a workers' state "
        "generating a new despotism remains live and the exchange should be "
        "presented as unresolved.",
        "Relative autonomy must remain relative: stretched far enough it "
        "becomes the pluralist state under another name, and an answer that "
        "drops the qualifier has surrendered the argument it was making.",
        "Run the trajectory as claim, reviser, ground and residual; use the "
        "Miliband-Poulantzas exchange as the fastest three-move demonstration "
        "of depth — claim, objection, internal limit; keep Gramsci and "
        "Althusser apart on agency; and reserve the whole trajectory for "
        "fifteen and twenty marks rather than attempting it at ten.",
        [
            "C1 revised by Lenin: imperialism redistributes contradictions "
            "globally, so the chain breaks at its weakest link, and a vanguard "
            "party supplies political consciousness.",
            "C2 revised by Gramsci: rule in the West works chiefly through "
            "consent, so civil society is the principal terrain of struggle.",
            "C3 revised in the Miliband-Poulantzas exchange: instrumental "
            "capture (1969) against relative autonomy and the condensation of "
            "class forces (1973).",
            "C4 revised by Althusser: subjects are produced by ideological "
            "apparatuses through interpellation; ideology is a material "
            "practice, not a mistaken belief.",
            "Gramsci leaves room for agency and strategy; Althusser explains "
            "stability better but change worse.",
            "Contradictory consciousness — inherited common sense alongside "
            "good sense from practical experience — is Gramsci's answer to the "
            "closed-circle objection.",
        ],
        [
            visual(
                "Which classical claim each successor revises, and how",
                "Naming the revised claim, the reviser and the replacement is "
                "the single highest-yield move available in a Marxism stem at "
                "fifteen or twenty marks.",
                "+----+------------------------------+-------------+---------------------------+",
                "| #  | CLASSICAL CLAIM              | REVISER     | WHAT REPLACES IT          |",
                "+----+------------------------------+-------------+---------------------------+",
                "| C1 | revolution matures where     | LENIN       | weakest link + vanguard   |",
                "|    | capitalism is most advanced  |             | party, democratic         |",
                "|    |                              |             | centralism                |",
                "| C2 | ruling ideas are a reflex of | GRAMSCI     | hegemony contested in     |",
                "|    | the base                     |             | civil society             |",
                "| C3 | the state is an instrument   | MILIBAND -> | instrumental capture vs   |",
                "|    | of the ruling class          | POULANTZAS  | RELATIVE AUTONOMY         |",
                "| C4 | consciousness is determined  | ALTHUSSER   | subjects PRODUCED by      |",
                "|    | by social being              |             | ISAs via interpellation   |",
                "+----+------------------------------+-------------+---------------------------+",
                "  ONE-LINE THESIS -> causal weight is RELOCATED into the",
                "  superstructure; the materialist mechanism is retained.",
            ),
            visual(
                "Gramsci's two spheres and Althusser's two apparatuses",
                "Both give the superstructure real weight, but only Gramsci's "
                "civil society is a terrain that can be lost and won.",
                "GRAMSCI                                ALTHUSSER",
                "  POLITICAL SOCIETY                      REPRESSIVE STATE APPARATUS",
                "  coercion through force and law         functions BY VIOLENCE",
                "  army, police, courts, administration   one, unified, public",
                "        |                                      |",
                "        v                                      v",
                "  CIVIL SOCIETY                          IDEOLOGICAL STATE APPARATUSES",
                "  leadership through CONSENT             function BY IDEOLOGY",
                "  school, family, church, press,         school, family, religion, law,",
                "  associations, popular culture          parties, unions, communications",
                "        |                                      |",
                "        v                                      v",
                "  WAR OF POSITION -> build a             INTERPELLATION -> individuals are",
                "  COUNTER-HEGEMONY before any            hailed as subjects who freely do",
                "  war of manoeuvre                       what the structure requires",
                "  DIFFERENCE THAT SCORES -> contest and agency in Gramsci;",
                "  reproduction and thin agency in Althusser.",
            ),
        ],
    ),
    session(
        "Socialism: The Family, Its Varieties and Gandhian Socialism",
        "Socialism is the family of doctrines that subjects productive "
        "property and economic power to social control so that cooperation, "
        "equality and freedom from exploitation can be secured, and Marxism is "
        "one revolutionary and materialist member of that family rather than "
        "the family itself.",
        "The socialist argument runs from the premise that productive "
        "capacities are socially inherited and cooperatively exercised, "
        "through the claim that private control of indispensable productive "
        "assets confers power over others' work and life chances and that "
        "market outcomes do not automatically track need, desert or equal "
        "freedom, to the conclusion that ownership and production must answer "
        "to social purposes and democratic justification; its varieties "
        "include utopian socialism (Owen, Fourier, Saint-Simon), Marxian "
        "socialism, Fabian and democratic socialism, guild socialism, market "
        "socialism and Gandhian socialism, which differ over method, the form "
        "of ownership and the place of markets.",
        "Socialism is a family and Marxism is one member of it: a socialist "
        "may choose revolution or parliament, planning or regulated markets, "
        "state ownership or cooperatives, so the mark-bearing move is to "
        "define the sense in use before any comparison with communism is "
        "attempted.",
        [
            "social ownership and democratic control",
            "utopian socialism",
            "Fabian and democratic socialism",
            "guild socialism",
            "market socialism",
            "Gandhian trusteeship and bread labour",
            "socialisation against mere nationalisation",
            "social democracy as regulated private property",
        ],
        "Begin from social ownership and democratic control as the defining "
        "commitment, run the varieties across method and form of ownership "
        "from utopian socialism through Fabian and democratic socialism, guild "
        "socialism and market socialism to Gandhian trusteeship and bread "
        "labour, and keep socialisation apart from mere nationalisation and "
        "from social democracy's regulated private property.",
        "Economic power is political in effect, so a doctrine that leaves "
        "indispensable productive assets under private control leaves the "
        "power over others' work and life chances untouched however generous "
        "its transfers may be.",
        "Freedom therefore requires more than non-interference by the state, "
        "and the socialist quarrel with liberalism turns on that premise "
        "rather than on any dispute about the value of liberty itself.",
        "Do not identify socialism with state ownership and do not use "
        "socialism and communism as synonyms; socialisation requires control "
        "by society rather than by officials, and in Marxist vocabulary "
        "socialism often names a transitional lower phase while in wider "
        "political theory it names the whole family.",
        "Social ownership without market prices cannot aggregate dispersed "
        "knowledge or generate incentives, and state ownership in practice "
        "becomes ownership by officials, so socialism replaces private "
        "domination with bureaucratic domination.",
        "The two halves of the objection call for different replies. Against "
        "the information and incentive problem, market socialism, "
        "decentralised planning and cooperative governance separate social "
        "ownership from a single command bureaucracy, so the objection tells "
        "against one institutional design rather than against the principle. "
        "Against bureaucratic domination the socialist must concede the "
        "diagnosis and accept its implication: nationalisation alone is not "
        "socialisation, and democratic control, workplace participation and "
        "enforceable accountability are constitutive of the doctrine rather "
        "than optional additions to it.",
        "No settled institutional design has yet been shown to keep social "
        "ownership reliably democratic at large scale, so the accountability "
        "problem is a live design question rather than a solved one.",
        "Define socialism as a family with social ownership and democratic "
        "control at its core, place the variety the stem needs, run the "
        "socialism-communism-social democracy grid whenever a definitional "
        "comparison is asked, take the incentive and bureaucracy objections "
        "together, and close on the difference between socialising power and "
        "merely transferring title to the state.",
        [
            "Core argument: productive capacities are socially inherited; "
            "private control of indispensable assets confers power over "
            "others; markets do not track need or equal freedom; therefore "
            "ownership must answer to social purposes.",
            "Utopian socialism (Owen, Fourier, Saint-Simon) diagnoses "
            "competition through exemplary communities and moral reform.",
            "Fabian and democratic socialism work by gradual parliamentary "
            "reform across public, cooperative and regulated sectors.",
            "Guild socialism proposes occupational self-government and opposes "
            "both private capitalism and bureaucratic statism.",
            "Market socialism separates markets from capitalist ownership by "
            "combining them with worker or public ownership.",
            "Gandhian socialism combines non-possession, trusteeship, bread "
            "labour, decentralised production, village self-rule and the "
            "welfare of all, rejecting unrestricted capitalism and violent "
            "centralised collectivism alike.",
            "Trusteeship relies on voluntary moral conversion, which is its "
            "standing weakness and must be conceded.",
        ],
        [
            visual(
                "The socialist family sorted by method and form of ownership",
                "Placing the variety before arguing is what prevents a "
                "socialism answer from silently becoming an answer about "
                "Marxism.",
                "                          SOCIALISM",
                "        social control of productive property + democratic control",
                "                              |",
                "   +----------+----------+----+-----+----------+-----------+",
                "   v          v          v          v          v           v",
                "UTOPIAN    MARXIAN    FABIAN /   GUILD      MARKET      GANDHIAN",
                "           SOCIALISM  DEMOCRATIC SOCIALISM  SOCIALISM   SOCIALISM",
                "   |          |          |          |          |           |",
                "   v          v          v          v          v           v",
                "exemplary  class      gradual    occupational markets    trusteeship,",
                "communities struggle,  parliament self-       within     bread labour,",
                "and moral  revolution reform     government   social     decentralised",
                "reform                                        ownership  production",
                "   |          |          |          |          |           |",
                "   v          v          v          v          v           v",
                "Owen,      social     public,    producer    worker or   village",
                "Fourier,   ownership  cooperative guilds     public      self-rule and",
                "Saint-Simon           regulated             ownership    welfare of all",
                "  RULE OF USE -> name the variety, then argue; never argue about",
                "                 socialism in general and score the variety later.",
            ),
            visual(
                "Socialism, communism and social democracy on four axes",
                "The 2024 definitional demand is answered by this grid; "
                "running the axes in parallel is what earns the comparison "
                "marks.",
                "+--------------+---------------------+--------------------+------------------+",
                "| AXIS         | SOCIALISM (FAMILY)  | COMMUNISM (HIGHER) | SOCIAL DEMOCRACY |",
                "+--------------+---------------------+--------------------+------------------+",
                "| PROPERTY     | social control in   | common control;    | private property |",
                "|              | varied forms        | classes abolished  | but regulated    |",
                "| STATE        | may remain          | political state    | welfare-         |",
                "|              | democratic, active  | loses class        | regulatory state |",
                "|              |                     | function           |                  |",
                "| DISTRIBUTION | contribution, need  | according to need  | tax-transfer and |",
                "|              | or mixed principles | in the higher      | public services  |",
                "|              |                     | phase              |                  |",
                "| METHOD       | revolutionary or    | reached through a  | constitutional   |",
                "|              | gradual             | transition         | reform           |",
                "+--------------+---------------------+--------------------+------------------+",
            ),
        ],
    ),
    session(
        "Inter-School Debates: Anarchism, Marxism, Democratic Socialism, Gandhi and M. N. Roy",
        "The debates in this clause are between rival routes to one declared "
        "destination — a free and equal social order — and they divide over "
        "the state, over the transition, over violence, and over whether the "
        "means used may differ in character from the end sought.",
        "Four exchanges organise the material: anarchism against Marxism on "
        "whether the state is to be abolished or first captured as "
        "transitional political power, with Bakunin's prediction that a "
        "revolutionary state creates a new ruling stratum and the Marxist "
        "reply that organised class power is required to defeat entrenched "
        "property; Marx against democratic socialists on whether a state "
        "embedded in capitalist property can be peacefully converted into an "
        "impartial instrument; Marx against Gandhi on the root problem, the "
        "method, the scale of production and the relation of means to ends; "
        "and M. N. Roy's radical-humanist criticism, which rejects the "
        "subordination of the individual to class, party or historical "
        "necessity.",
        "Bakunin predicts that a revolutionary state will generate a new "
        "ruling stratum while Marxists reply that organised class power is "
        "needed to defeat entrenched property and coercion, and the honest "
        "presentation reports this exchange as genuinely unresolved rather "
        "than settling it by assertion.",
        [
            "abolition against transitional capture of the state",
            "the fear of a new ruling stratum",
            "premature abolition leaving capitalist power intact",
            "socialising economic power through suffrage and parliament",
            "means prefigure ends",
            "trusteeship against class struggle",
            "radical humanism and the freedom of the individual",
        ],
        "Fix three or four shared axes before naming anyone, run each school "
        "down them in parallel, present abolition against transitional capture "
        "with the new-ruling-stratum fear on one side and premature abolition "
        "on the other, use means prefigure ends for Gandhi and radical "
        "humanism for Roy, and adjudicate on one named criterion rather than "
        "on sympathy.",
        "Each school locates domination differently, so each assigns the state "
        "a different role in the transition, and the disagreement about "
        "organisation and violence follows from that assignment rather than "
        "from temperament.",
        "Reform can genuinely civilise capitalism and alter the distribution "
        "of power, yet reforms remain vulnerable wherever ownership and "
        "investment decisions stay insulated from democratic control.",
        "Do not stage these as sequential doctrine summaries; a comparison is "
        "scored only when three or four axes are fixed in advance and both "
        "positions are run down each of them before any verdict is offered.",
        "If the anarchist fear is sound, every revolutionary transition must "
        "end in a new despotism, and if the Marxist reply is sound, "
        "dispensing with organisation simply leaves entrenched property in "
        "place — so the debate appears to have no rational resolution.",
        "The appearance of deadlock is itself informative and should be "
        "reported rather than concealed. The Marxist counter is that "
        "abolishing organisation does not abolish power but disperses it "
        "unaccountably; the anarchist counter is that an instrument built to "
        "concentrate power supplies no mechanism for surrendering it. What "
        "follows is not scepticism but a design question that both traditions "
        "must answer: which institutions make concentrated power answerable "
        "during a transition, and M. N. Roy's radical humanism is best read as "
        "one attempted answer, retaining the critique of exploitation while "
        "rejecting economic determinism and party absolutism.",
        "Neither side has produced a transitional design that is demonstrably "
        "both effective against entrenched property and reliably reversible, "
        "so the exchange closes on a graded verdict rather than a winner.",
        "Fix the axes first — primary domination, the state, organisation and "
        "the characteristic fear — then run anarchism, Marxism, democratic "
        "socialism, Gandhi and Roy down them, and close with a graded verdict "
        "that names the axis on which the decision actually turns.",
        [
            "Anarchism against Marxism: authority and hierarchy against class "
            "relations rooted in production.",
            "On the state: abolish or supersede without transitional "
            "sovereignty, against a transitional use of political power.",
            "Characteristic fears: a new state elite on one side, premature "
            "abolition leaving capitalist power intact on the other.",
            "Marx against democratic socialists: doubt that a state embedded "
            "in capitalist property can be peacefully converted, against faith "
            "in suffrage, unions, rights and public institutions.",
            "Marx against Gandhi: class exploitation against greed, violence "
            "and modern industrial civilisation; revolution against truth-force "
            "and trusteeship; socialised large-scale production against "
            "decentralised need-oriented production.",
            "M. N. Roy: freedom is the progressive removal of obstacles to the "
            "unfolding of human capacities, and concentrated power reproduces "
            "domination.",
        ],
        [
            visual(
                "Anarchism against Marxism on four shared axes",
                "This is the comparison the corpus returns to most often; run "
                "the axes in parallel rather than writing two summaries.",
                "+---------------------+---------------------------+---------------------------+",
                "| AXIS                | ANARCHISM                 | MARXISM                   |",
                "+---------------------+---------------------------+---------------------------+",
                "| PRIMARY DOMINATION  | authority and hierarchy   | class relation rooted in  |",
                "|                     |                           | production                |",
                "| THE STATE           | abolish or supersede      | transitional political    |",
                "|                     | without transitional      | power used by the working |",
                "|                     | sovereignty               | class                     |",
                "| ORGANISATION        | federation, autonomy,     | class party or            |",
                "|                     | voluntary association     | organisation; readings    |",
                "|                     |                           | vary                      |",
                "| CHARACTERISTIC FEAR | revolution reproduces a   | premature abolition       |",
                "|                     | new state elite           | leaves capitalist power   |",
                "|                     |                           | intact                    |",
                "+---------------------+---------------------------+---------------------------+",
                "  CORE DEBATE -> Bakunin predicts a new ruling stratum; Marxists",
                "  answer that entrenched property cannot be defeated unorganised.",
            ),
            visual(
                "Marx and Gandhi: five axes and the means-ends divide",
                "The fifth axis is where the two systems actually separate, "
                "and it is the axis most often omitted.",
                "AXIS               MARX                      GANDHI",
                "root problem   -> class exploitation and  -> greed, violence, modern",
                "                  alienated production      industrial civilisation",
                "method         -> class struggle;         -> truth-force, trusteeship,",
                "                  revolution                constructive work",
                "scale          -> socialised large-scale  -> decentralised,",
                "                  production emancipates    need-oriented production",
                "means and ends -> revolutionary coercion  -> means PREFIGURE ends",
                "                  debated within Marxism",
                "freedom        -> collective control      -> self-rule begins with",
                "                  enables self-development  ethical self-restraint",
                "        |",
                "        v",
                "  CONVERGENCE -> both reject exploitation; DIVERGENCE -> violence,",
                "  industrial scale, and the moral relation of means to ends.",
            ),
        ],
    ),
    session(
        "Criticisms, Replies and the Residual Problems That Decide Marks",
        "This session is the consolidated objection-reply-residual ledger for "
        "the whole clause: for each standing criticism of anarchism, Marxism "
        "and socialism it fixes the strongest available reply and the residual "
        "problem that survives that reply.",
        "Six standing criticisms organise the ledger — that stateless order is "
        "unworkable, that history is reduced to economics, that revolution "
        "produces dictatorship, that social ownership destroys liberty, that "
        "equality suppresses difference, and that all three doctrines are "
        "utopian — and each is paired with its strongest reply and with a "
        "residual issue that the reply does not remove, since a "
        "critical-examination directive is scored precisely on that third "
        "move.",
        "A critical-examination stem is scored on the third move rather than "
        "the second: state the objection in its strongest form, give the best "
        "reply the doctrine actually possesses, and then name the residual "
        "problem that survives the reply and grades the final verdict.",
        [
            "objection, reply and residual problem",
            "stateless order and the coordination objection",
            "economic reductionism",
            "revolution and the authoritarian record",
            "social ownership against liberty",
            "equality of status without uniformity",
            "feasibility as a constraint on normativity",
        ],
        "Build every critical answer as objection, reply and residual problem; "
        "select from the ledger according to the doctrine named — the "
        "coordination objection for stateless order, economic reductionism and "
        "the authoritarian record for Marxism, social ownership against "
        "liberty and equality of status without uniformity for socialism — and "
        "let feasibility constrain rather than replace the normative claim.",
        "A reply that removes an objection entirely produces an unqualified "
        "verdict, which is exactly what a critical directive does not reward; "
        "naming what the reply leaves standing is what converts exposition "
        "into evaluation.",
        "The graded verdict then writes itself, because the residual problem "
        "supplies the criterion on which the final judgment is expressly "
        "made.",
        "Do not treat the record of any state as a refutation of a theory, and "
        "do not treat a statute, scheme or cooperative as proof that a "
        "doctrine is true; a state's conduct shows what was done, while the "
        "philosophical question concerns control, freedom and justice.",
        "If every criticism can be met by a reply, and every reply leaves a "
        "residual, then no verdict is ever available and the whole exercise "
        "collapses into permanent suspension of judgment.",
        "The inference fails because residuals are not equal in weight. Some "
        "residuals are design problems that further institutional work might "
        "solve, such as accountable social ownership; others are structural "
        "and internal to the doctrine, such as the absence of any guarantee "
        "that a transitional apparatus dissolves. A graded verdict compares "
        "the weight and kind of the residuals on each side and states the axis "
        "on which the comparison was decided, which is a judgment and not a "
        "suspension of one.",
        "The comparison of residuals still depends on a prior normative "
        "commitment about which failures matter most, so the verdict is "
        "defensible rather than demonstrative and must be presented that way.",
        "Reproduce the ledger as objection, reply and residual for the "
        "doctrine the stem names, run the ten traps as a pre-submission check, "
        "select the graded verdict formula that fits the directive, and make "
        "the closing sentence state the axis on which the judgment turns.",
        [
            "Stateless order is unworkable -> federation can coordinate "
            "without sovereign centralism -> residual: coercion against "
            "persistent aggressors.",
            "History is reduced to economics -> material conditioning is not "
            "mechanical causation -> residual: caste, gender and culture need "
            "independent analysis.",
            "Revolution produces dictatorship -> emancipation requires "
            "democratic proletarian agency -> residual: the historical record "
            "remains adverse.",
            "Social ownership destroys liberty -> private economic power also "
            "dominates -> residual: the design of accountable social control.",
            "Equality suppresses difference -> equality of status and "
            "capability need not mean sameness -> residual: the legitimate "
            "scope of differential reward.",
            "All three are utopian -> every ideology contains a regulative "
            "picture of a justified order -> residual: feasibility must "
            "constrain, not replace, normativity.",
            "Pre-submission check: anarchism is not chaos; Marxism is not "
            "equality of income; socialism is not state ownership; socialism "
            "and communism are not synonyms.",
        ],
        [
            visual(
                "The three-move structure that a critical directive rewards",
                "Two moves describe a debate; the third move decides the "
                "grade, because it supplies the criterion for the verdict.",
                "  STEP 1  OBJECTION, stated in its STRONGEST form",
                "          (not a straw version the doctrine can easily beat)",
                "                 |",
                "                 v",
                "  STEP 2  REPLY that the doctrine ACTUALLY possesses",
                "          (named, internal, not invented for the occasion)",
                "                 |",
                "                 v",
                "  STEP 3  RESIDUAL PROBLEM that survives the reply",
                "          (this is where the marks are)",
                "                 |",
                "                 v",
                "  STEP 4  GRADED VERDICT that names the AXIS on which it turns",
                "  CONTROL -> diagnosis and remedy are judged separately, so an",
                "             analysis may survive while its institutional cure fails.",
            ),
            visual(
                "The six standing criticisms with reply and residual",
                "Select the row the stem names; do not run the whole ledger in "
                "a ten-mark answer.",
                "+----------------------+-------------+----------------------+----------------+",
                "| CRITICISM            | TARGET      | STRONGEST REPLY      | RESIDUAL       |",
                "+----------------------+-------------+----------------------+----------------+",
                "| stateless order is   | anarchism   | federation can       | coercion vs    |",
                "| unworkable           |             | coordinate           | aggressors     |",
                "| history reduced to   | Marxism     | conditioning is not  | caste, gender, |",
                "| economics            |             | mechanical causation | culture        |",
                "| revolution produces  | Marxism     | emancipation needs   | record remains |",
                "| dictatorship         |             | democratic agency    | adverse        |",
                "| social ownership     | socialism   | private economic     | accountable    |",
                "| destroys liberty     |             | power also dominates | design         |",
                "| equality suppresses  | socialism   | status/capability is | scope of       |",
                "| difference           |             | not sameness         | reward         |",
                "| all three are        | all three   | each holds a         | feasibility    |",
                "| utopian              |             | regulative picture   | must constrain |",
                "+----------------------+-------------+----------------------+----------------+",
            ),
        ],
    ),
)


ASCII_PANELS = (
    {
        "title": (
            "The central question: what an ideology claims and how domination "
            "is diagnosed"
        ),
        "structural_type": "root-question-and-ideology-boundary",
        "sessions": [1],
        "lines": [
            "CENTRAL QUESTION -> what chiefly produces domination in society, and what",
            "                    institutional change would remove it?",
            "        |",
            "        v",
            "IDEOLOGY HAS TWO SENSES, AND THE SENSE MUST BE DECLARED FIRST",
            "  ANALYTICAL  -> an organised outlook: descriptive claims + evaluative",
            "                 commitments + practical prescriptions, avowed and argued",
            "  CRITICAL    -> a socially rooted framework in which historically specific",
            "                 class relations appear natural, universal and inevitable",
            "        |",
            "  +-----+---------------------+---------------------------+",
            "  v                           v                           v",
            "ANARCHISM                  MARXISM                     SOCIALISM",
            "diagnosis: COERCIVE        diagnosis: CLASS RELATIONS  diagnosis: SOCIALLY",
            "AUTHORITY itself, above    generated by the MODE OF    UNCONTROLLED",
            "all the sovereign state    PRODUCTION                  PRODUCTIVE PROPERTY",
            "  |                           |                           |",
            "  v                           v                           v",
            "prescription: abolish      prescription: transitional  prescription: subject",
            "the state and standing     working-class power, then   ownership and",
            "hierarchies; federate      a classless, stateless      production to social",
            "and coordinate instead     order                       control + democracy",
            "  |                           |                           |",
            "  +---------------------------+---------------------------+",
            "                              v",
            "SHARED AXES FOR EVERY COMPARISON IN THIS CLAUSE",
            "  authority | property | class | revolution | state | freedom",
            "CONTROL -> the diagnosis generates the prescription, so fix the diagnosis",
            "           before any institutional claim is made or judged.",
        ],
    },
    {
        "title": (
            "Anarchism I: the burden-of-justification argument against the state"
        ),
        "structural_type": "anarchist-argument-process-chain",
        "sessions": [2],
        "lines": [
            "ROOT CLAIM -> coercive political authority lacks adequate moral justification",
            "        |",
            "        v",
            "FIVE-STEP ARGUMENT (reproduce as numbered premises)",
            "  (1) legitimate authority must be compatible with the MORAL AUTONOMY and",
            "      EQUALITY of persons",
            "        v",
            "  (2) the state claims a TERRITORIAL MONOPOLY of law-making, coercion and",
            "      punishment",
            "        v",
            "  (3) obedience is demanded because a command is LEGALLY AUTHORITATIVE, not",
            "      because its content is independently right",
            "        v",
            "  (4) that standing right SUBORDINATES one person's judgment to another's",
            "      institutional will",
            "        v",
            "  (5) THEREFORE the state bears a burden of justification anarchists judge",
            "      it unable to discharge",
            "        |",
            "        v",
            "NAMED SUPPORT -> BAKUNIN: concentrated power deforms ruler and ruled",
            "              -> PROUDHON: property as institutional power of appropriation",
            "              -> KROPOTKIN: mutual aid is a genuine source of social order",
            "        |",
            "        v",
            "BOUNDARY TERMS -> ANARCHY = collapse of rule | ANARCHISM = critique of",
            "  domination | CIVIL DISOBEDIENCE = breach of particular laws only |",
            "  LIBERTARIAN MINIMAL STATE = rejected too, because the MONOPOLY is the target",
            "MECHANISM -> the claim is about the TITLE to command, so pointing to good",
            "             laws cannot discharge the burden.",
        ],
    },
    {
        "title": (
            "Anarchism II: strands of the family, voluntary order and Gandhi's "
            "qualified place"
        ),
        "structural_type": "anarchist-strand-taxonomy-and-gandhi-branch",
        "sessions": [3],
        "lines": [
            "AXIS OF DIVISION -> who may control PRODUCTIVE PROPERTY, and what replaces",
            "                    the sovereign centre?",
            "        |",
            "  +--------+-----------+------------+--------------+---------------+",
            "  v        v           v            v              v",
            "MUTUALISM COLLECTIVIST ANARCHO-    INDIVIDUALIST  PHILOSOPHICAL",
            "          ANARCHISM    COMMUNISM   ANARCHISM      ANARCHISM",
            "possession collective  common      strong personal no automatic duty",
            "and free   control of  ownership;  sovereignty;    to obey; critical",
            "exchange   productive  by NEED     markets vary    allegiance possible",
            "PROUDHON   BAKUNIN     KROPOTKIN   Thoreauvian     legitimacy, not",
            "                                   resistance      insurrection",
            "        v",
            "VOLUNTARY ORDER -> the claim is INSTITUTIONAL, not optimistic: reciprocity,",
            "  custom, association and horizontal coordination can order social life",
            "  without a final coercive superior. Village assemblies, cooperatives and",
            "  mutual-aid networks ILLUSTRATE the capacity; they do not PROVE it at scale.",
            "        v",
            "OBJECTIONS -> [1] security dilemma  [2] scale and public goods",
            "           -> [3] optimistic anthropology  [4] HIDDEN AUTHORITY",
            "REPLIES    -> [1] the state itself organised war and repression",
            "           -> [2] it rejects centralised domination, not coordination",
            "           -> [3] it need only deny hierarchy is the best remedy",
            "           -> [4] conceded as internal: audit domination inside voluntary",
            "                  bodies through rotation, recall and refusal of permanence",
            "        |",
            "        v",
            "GANDHI BRANCH -> AFFINITY: self-rule, decentralised village republics, a",
            "  state reduced to a minimum | DIVERGENCE: non-violence, trusteeship,",
            "  religious ethics and constructive programme replace class war and anti-theism",
            "VERDICT -> anarchist in IDEAL, pragmatic reformer in METHOD.",
        ],
    },
    {
        "title": (
            "Marxism I: the materialist method and the elements of historical "
            "materialism"
        ),
        "structural_type": "historical-materialism-element-matrix",
        "sessions": [4],
        "lines": [
            "MARXISM IS FOUR THINGS AT ONCE -> a METHOD, a CRITIQUE, a THEORY OF CHANGE,",
            "                                  and a POLITICAL PROJECT",
            "        v",
            "SIX-STEP ARGUMENT",
            "  (1) human beings must produce the means of life",
            "  (2) production occurs through definite social relations",
            "  (3) productive forces develop within those relations",
            "  (4) existing relations eventually OBSTRUCT development -> FETTERS",
            "  (5) the conflict becomes SOCIAL AND POLITICAL STRUGGLE",
            "  (6) a NEW MODE OF PRODUCTION can emerge through that struggle",
            "        v",
            "+------------------------+-------------------------------+-------------------+",
            "| ELEMENT                | WHAT IT NAMES                 | EXAM USE          |",
            "+------------------------+-------------------------------+-------------------+",
            "| PRODUCTIVE FORCES      | labour-power, knowledge,      | capacity to       |",
            "|                        | tools, technology             | produce           |",
            "| RELATIONS OF PRODUCTION| ownership, control, class     | who commands and  |",
            "|                        | relations                     | who appropriates  |",
            "| MODE OF PRODUCTION     | unity of forces and relations | feudalism,        |",
            "|                        |                               | capitalism        |",
            "| BASE / SUPERSTRUCTURE  | economic structure related to | a RELATION, never |",
            "|                        | law, politics, ideology       | a one-way switch  |",
            "| CLASS STRUGGLE         | conflict rooted in opposed    | motor of          |",
            "|                        | structural interests          | transformation    |",
            "+------------------------+-------------------------------+-------------------+",
            "        v",
            "DIALECTIC, USED WITH CARE -> contradiction drives development, but the",
            "  primacy of a self-developing Idea is rejected; thesis-antithesis-synthesis",
            "  is LATER TEXTBOOK SHORTHAND and is not Marx's own fixed three-step law",
            "LIMIT -> the honest charge is a TENDENCY toward economic reductionism, so",
            "         concede it early and keep caste, gender and culture in view.",
        ],
    },
    {
        "title": (
            "Marxism II: the four dimensions of alienation and the extraction of "
            "surplus value"
        ),
        "structural_type": "alienation-and-exploitation-mechanism-flow",
        "sessions": [5],
        "lines": [
            "SOURCE -> Economic and Philosophic Manuscripts of 1844",
            "        v",
            "ALIENATED LABOUR under private property and the division of labour",
            "  +--------------+--------------+--------------+--------------+",
            "  v              v              v              v",
            "FROM THE       FROM THE ACT   FROM SPECIES-  FROM OTHER",
            "PRODUCT        OF LABOUR      BEING          PERSONS",
            "it confronts   work is        conscious      workers compete;",
            "the producer   externally     creative       social relations",
            "as another's   compelled, not activity cut   assume COMMODITY",
            "property       self-realising to survival    form",
            "        |",
            "        v",
            "KEY DISTINCTION -> alienation is BROADER THAN LOW WAGES; a well-paid worker",
            "  remains alienated where labour, product and purpose are controlled by others",
            "        v",
            "EXPLOITATION IS NOT THEFT -> the contract is FORMALLY FREE",
            "  (1) workers lack independent access to the MEANS OF PRODUCTION",
            "  (2) they must SELL LABOUR-POWER to live",
            "  (3) the capitalist CONTROLS the labour process and the product",
            "  (4) COMPETITION compels accumulation and extraction",
            "  (5) value created EXCEEDS value represented by wages -> SURPLUS VALUE",
            "        v",
            "SECOND KEY DISTINCTION -> EXPLOITATION concerns the RELATION OF PRODUCTION",
            "  and INEQUALITY the DISTRIBUTION of holdings, so redistribution may reduce",
            "  inequality while leaving exploitative control entirely intact.",
            "OBJECTION -> species-being presupposes a universal human essence",
            "REPLY     -> reconstruct it minimally as agency, recognition and control",
            "             over one's central activities",
            "MECHANISM -> no cruel intention is required, because the compulsion",
            "             on the worker is structural rather than personal.",
        ],
    },
    {
        "title": (
            "Marxism III: ideology, the state, revolution and the two phases of "
            "communism"
        ),
        "structural_type": "state-revolution-and-equality-objection-reply",
        "sessions": [6],
        "lines": [
            "IDEOLOGY -> not merely a lie, but a socially rooted framework in which",
            "            historically specific relations appear natural and inevitable",
            "        v",
            "THE STATE -> secures the GENERAL CONDITIONS of the capitalist order while",
            "  presenting itself as the representative of a UNIVERSAL interest",
            "  NUANCE -> relative autonomy is compatible with structural class function;",
            "            not every state act benefits every capitalist",
            "        v",
            "REVOLUTION -> SOCIALISED PRODUCTION held under PRIVATE APPROPRIATION",
            "  + organised class struggle -> transformation becomes POSSIBLE",
            "        |",
            "        v",
            "DICTATORSHIP OF THE PROLETARIAT = transitional POLITICAL SUPREMACY of the",
            "  working class; NOT a textual licence for permanent one-party dictatorship",
            "  +-----+------------------------------+",
            "  v                                    v",
            "LOWER PHASE                        HIGHER PHASE",
            "distribution by CONTRIBUTION;      distribution according to NEED;",
            "a 'bourgeois' measure survives     the political state as class",
            "                                   instrument becomes unnecessary",
            "        |",
            "        v",
            "EQUALITY GRID -> FORMAL (is the same rule applied?) | SUBSTANTIVE (can",
            "  persons actually develop?) | EQUITY (what differential provision does need",
            "  justify?) | FREEDOM (from whom, and for what activity?)",
            "        v",
            "OBJECTION -> transitional states entrench rather than wither",
            "REPLY     -> build constitutional liberty, plural organisation, recall and",
            "             accountability INTO the transition rather than postpone them",
            "RESIDUAL  -> no internal safeguard guarantees the apparatus dissolves; this is",
            "             the strongest historical objection and must be conceded.",
        ],
    },
    {
        "title": "Marx after Marx: which classical claim each successor revises",
        "structural_type": "classical-to-neo-marxism-revision-matrix",
        "sessions": [7],
        "lines": [
            "ONE-LINE THESIS -> neo-Marxism RELOCATES causal weight into the",
            "  superstructure while RETAINING the materialist mechanism",
            "+----+------------------------------+-------------+---------------------------+",
            "| #  | CLASSICAL CLAIM              | REVISER     | WHAT REPLACES IT          |",
            "+----+------------------------------+-------------+---------------------------+",
            "| C1 | revolution matures where     | LENIN       | weakest link in the       |",
            "|    | capitalism is most advanced  |             | chain + vanguard party    |",
            "| C2 | ruling ideas are a reflex of | GRAMSCI     | HEGEMONY won and lost in  |",
            "|    | the base                     |             | civil society             |",
            "| C3 | the state is an instrument   | MILIBAND -> | instrumental capture vs   |",
            "|    | of the ruling class          | POULANTZAS  | RELATIVE AUTONOMY         |",
            "| C4 | consciousness is determined  | ALTHUSSER   | subjects PRODUCED by ISAs |",
            "|    | by social being              |             | through interpellation    |",
            "+----+------------------------------+-------------+---------------------------+",
            "        v",
            "LENIN     -> imperialism exports capital and yields superprofits; the chain",
            "  breaks at its WEAKEST LINK. Spontaneous struggle yields only TRADE-UNION",
            "  CONSCIOUSNESS, so a vanguard party under DEMOCRATIC CENTRALISM is required.",
            "  OBJECTION -> SUBSTITUTIONISM: party for class, committee for party.",
            "GRAMSCI   -> POLITICAL SOCIETY rules by coercion; CIVIL SOCIETY leads by",
            "  CONSENT through ORGANIC INTELLECTUALS. Hence WAR OF POSITION and a",
            "  COUNTER-HEGEMONY before any war of manoeuvre.",
            "  OBJECTION -> no independent test separates hegemony from ordinary agreement.",
            "ALTHUSSER -> RSA functions BY VIOLENCE; ISAs function BY IDEOLOGY and",
            "  reproduce the relations of production. INTERPELLATION hails individuals as",
            "  subjects who freely do what the structure requires; OVERDETERMINATION.",
            "  OBJECTION -> resistance becomes hard to explain; agency is thin.",
            "MILIBAND (1969) -> composition, leverage, positional interest",
            "POULANTZAS (1973) -> fractions of capital; the state as a CONDENSATION of",
            "  class forces, autonomous enough to act against particular capitalists",
            "LIMIT -> autonomy must remain RELATIVE, or the analysis becomes pluralism.",
        ],
    },
    {
        "title": (
            "Socialism: the family, its varieties and the socialism-communism "
            "boundary"
        ),
        "structural_type": "socialism-variety-comparison-grid",
        "sessions": [8],
        "lines": [
            "CORE ARGUMENT -> productive capacities are socially inherited; private",
            "  control of indispensable assets confers power over others' life chances;",
            "  markets do not track need or equal freedom, so ownership and production",
            "  must answer to social purposes and democratic justification",
            "        v",
            "+------------------+----------------------+---------------------------------+",
            "| VARIETY          | METHOD               | OWNERSHIP / CONTROL             |",
            "+------------------+----------------------+---------------------------------+",
            "| UTOPIAN          | exemplary communities| cooperative (Owen, Fourier,     |",
            "|                  | and moral reform     | Saint-Simon)                    |",
            "| MARXIAN          | class struggle and   | social ownership after a        |",
            "|                  | revolution           | transition beyond capitalism    |",
            "| FABIAN /         | gradual parliamentary| public, cooperative and         |",
            "| DEMOCRATIC       | reform               | regulated sectors               |",
            "| GUILD            | occupational self-   | producer guilds; against both   |",
            "|                  | government           | private capital and statism     |",
            "| MARKET           | market coordination  | worker or public ownership      |",
            "| GANDHIAN         | non-violence and     | trusteeship, village economy,   |",
            "|                  | decentralisation     | cooperative control             |",
            "+------------------+----------------------+---------------------------------+",
            "BOUNDARY GRID -> SOCIALISM (family): social control in varied forms |",
            "  COMMUNISM (Marxian higher phase): common control, classes abolished |",
            "  SOCIAL DEMOCRACY: regulated private property, tax-transfer, public services",
            "GANDHIAN SOCIALISM -> non-possession, trusteeship, bread labour,",
            "  decentralised production, village self-rule and the welfare of all",
            "  OBJECTION -> trusteeship relies on voluntary moral conversion and may",
            "               preserve unequal ownership",
            "  REPLY     -> a non-violent direction of transition, not praise of",
            "               entitlement, yet unenforceable without institutions",
            "RULE -> nationalisation alone is NOT socialisation; socialising power means",
            "        control by society, not by officials.",
        ],
    },
    {
        "title": (
            "Inter-school debates: anarchism, Marxism, democratic socialism, "
            "Gandhi and Roy"
        ),
        "structural_type": "inter-school-debate-and-verdict",
        "sessions": [9],
        "lines": [
            "FIX THE AXES BEFORE NAMING ANYONE -> primary domination | the state |",
            "                                     organisation | characteristic fear",
            "+---------------------+---------------------------+-------------------------+",
            "| AXIS                | ANARCHISM                 | MARXISM                 |",
            "+---------------------+---------------------------+-------------------------+",
            "| PRIMARY DOMINATION  | authority and hierarchy   | class relation rooted   |",
            "|                     |                           | in production           |",
            "| THE STATE           | abolish without a         | transitional political  |",
            "|                     | transitional sovereignty  | power of the workers    |",
            "| ORGANISATION        | federation, autonomy,     | class party or          |",
            "|                     | voluntary association     | organisation            |",
            "| CHARACTERISTIC FEAR | a new state elite         | premature abolition     |",
            "+---------------------+---------------------------+-------------------------+",
            "        v",
            "MARX vs DEMOCRATIC SOCIALISTS -> can a state embedded in capitalist property",
            "  be peacefully converted into an impartial instrument? Suffrage, unions,",
            "  constitutional rights and public institutions against structural doubt.",
            "  BALANCED VERDICT -> reform civilises capitalism and shifts power, but stays",
            "  vulnerable where investment decisions are insulated from democracy.",
            "MARX vs GANDHI -> root problem: class exploitation against greed, violence",
            "  and modern industrial civilisation | method: revolution against truth-force,",
            "  trusteeship and constructive work | scale: socialised large-scale production",
            "  against decentralised need-oriented production | MEANS PREFIGURE ENDS |",
            "  freedom: collective control against ethical self-restraint",
            "M. N. ROY -> radical humanism rejects subordinating the individual to class,",
            "  party or historical necessity; freedom is the progressive removal of",
            "  obstacles to the unfolding of human capacities, and concentrated power",
            "  reproduces domination. INDIAN BRIDGE: keep the critique of exploitation,",
            "  drop economic determinism and party absolutism.",
            "VERDICT -> the anarchist-Marxist exchange is genuinely unresolved; report it",
            "           as a design question about answerable power, not as a winner.",
        ],
    },
    {
        "title": (
            "Answer spine: criticisms, replies, residual problems and the graded "
            "verdict"
        ),
        "structural_type": "answer-spine-and-revision-synthesis",
        "sessions": [10],
        "lines": [
            "THREE-MOVE STRUCTURE -> OBJECTION (strongest form) -> REPLY (the doctrine's",
            "  own) -> RESIDUAL PROBLEM (where the marks are) -> GRADED VERDICT",
            "        v",
            "+----------------------+-------------+----------------------+----------------+",
            "| CRITICISM            | TARGET      | STRONGEST REPLY      | RESIDUAL       |",
            "+----------------------+-------------+----------------------+----------------+",
            "| stateless order is   | anarchism   | federation can       | coercion vs    |",
            "| unworkable           |             | coordinate           | aggressors     |",
            "| history reduced to   | Marxism     | conditioning is not  | caste, gender, |",
            "| economics            |             | mechanical causation | culture        |",
            "| revolution produces  | Marxism     | emancipation needs   | record remains |",
            "| dictatorship         |             | democratic agency    | adverse        |",
            "| social ownership     | socialism   | private economic     | accountable    |",
            "| destroys liberty     |             | power also dominates | design         |",
            "| equality suppresses  | socialism   | status/capability is | scope of       |",
            "| difference           |             | not sameness         | reward         |",
            "| all three are        | all three   | each holds a         | feasibility    |",
            "| utopian              |             | regulative picture   | must constrain |",
            "+----------------------+-------------+----------------------+----------------+",
            "PRE-SUBMISSION TRAP CHECK",
            "  anarchism is NOT chaos | anarchists do NOT reject all organisation |",
            "  NOT all anarchists are collectivists | Marxism is NOT equality of income |",
            "  base -> superstructure is NOT a mechanical one-way cause |",
            "  thesis-antithesis-synthesis is NOT Marx's formula |",
            "  socialism is NOT state ownership | socialism is NOT communism |",
            "  Marx gives NO detailed blueprint | statutes and schemes PROVE nothing",
            "GRADED VERDICT FORMULAS -> diagnosis/remedy split | relocation verdict |",
            "  necessary-but-not-sufficient | bounded-autonomy | means-ends | asymmetric",
            "REVISION SPINE -> discriminating question -> doctrine in technical vocabulary",
            "  -> internal rival before the external one -> one worked objection, reply and",
            "  residual -> conditional verdict separating analysis from institutional record.",
        ],
    },
)


GRAPHICAL_PILLS = (
    [
        {"text": "ANARCHISM, MARXISM AND SOCIALISM", "role": "primary"},
        {"text": "WHAT CHIEFLY PRODUCES DOMINATION", "role": "mechanism"},
        {"text": "AUTHORITY, MODE OF PRODUCTION, PROPERTY", "role": "evidence"},
        {"text": "ANALYTICAL AGAINST CRITICAL IDEOLOGY", "role": "comparison"},
        {"text": "DIAGNOSIS GENERATES PRESCRIPTION", "role": "outcome"},
        {"text": "IDEOLOGY IS NOT A TERM OF ABUSE", "role": "caution"},
    ],
    [
        {"text": "THE STATE MUST JUSTIFY ITS TITLE", "role": "primary"},
        {"text": "TERRITORIAL MONOPOLY OF COERCION", "role": "mechanism"},
        {"text": "MORAL AUTONOMY AND EQUALITY", "role": "evidence"},
        {"text": "CONTENT-INDEPENDENT OBLIGATION", "role": "comparison"},
        {"text": "BURDEN NOT DISCHARGED", "role": "outcome"},
        {"text": "ANARCHISM IS NOT ANARCHY", "role": "caution"},
    ],
    [
        {"text": "ONE FAMILY, FIVE STRANDS", "role": "primary"},
        {"text": "PROPERTY IS THE AXIS OF DIVISION", "role": "mechanism"},
        {"text": "PROUDHON, BAKUNIN, KROPOTKIN", "role": "evidence"},
        {"text": "MUTUAL AID AND FEDERATION", "role": "comparison"},
        {"text": "ANARCHIST IN IDEAL, REFORMER IN METHOD", "role": "outcome"},
        {"text": "HIDDEN AUTHORITY RETURNS", "role": "caution"},
    ],
    [
        {"text": "HOW A SOCIETY PRODUCES ITS LIFE", "role": "primary"},
        {"text": "FORCES OUTGROW RELATIONS, WHICH FETTER", "role": "mechanism"},
        {"text": "FORCES, RELATIONS, MODE OF PRODUCTION", "role": "evidence"},
        {"text": "BASE AND SUPERSTRUCTURE AS A RELATION", "role": "comparison"},
        {"text": "CLASS STRUGGLE IS THE MOTOR", "role": "outcome"},
        {"text": "NOT A MECHANICAL ONE-WAY CAUSE", "role": "caution"},
    ],
    [
        {"text": "ESTRANGEMENT AND SURPLUS VALUE", "role": "primary"},
        {"text": "FORMALLY FREE CONTRACT, REAL COMPULSION", "role": "mechanism"},
        {"text": "PRODUCT, ACT, SPECIES-BEING, OTHERS", "role": "evidence"},
        {"text": "EXPLOITATION IS NOT INEQUALITY", "role": "comparison"},
        {"text": "STRUCTURAL, NOT A CRUEL EMPLOYER", "role": "outcome"},
        {"text": "ALIENATION IS NOT LOW WAGES", "role": "caution"},
    ],
    [
        {"text": "IDEOLOGY, STATE, REVOLUTION, EQUALITY", "role": "primary"},
        {"text": "SOCIALISED PRODUCTION, PRIVATE APPROPRIATION", "role": "mechanism"},
        {"text": "LOWER PHASE AND HIGHER PHASE", "role": "evidence"},
        {"text": "FORMAL AGAINST SUBSTANTIVE EQUALITY", "role": "comparison"},
        {"text": "TRANSITIONAL SUPREMACY, NOT PARTY RULE", "role": "outcome"},
        {"text": "NO INTERNAL SAFEGUARD AGAINST ENTRENCHMENT", "role": "caution"},
    ],
    [
        {"text": "WHICH CLASSICAL CLAIM IS REVISED", "role": "primary"},
        {"text": "CAUSAL WEIGHT MOVES TO THE SUPERSTRUCTURE", "role": "mechanism"},
        {"text": "WEAKEST LINK, HEGEMONY, ISAS", "role": "evidence"},
        {"text": "INSTRUMENTALISM AGAINST RELATIVE AUTONOMY", "role": "comparison"},
        {"text": "REFINED RATHER THAN REFUTED", "role": "outcome"},
        {"text": "AUTONOMY MUST REMAIN RELATIVE", "role": "caution"},
    ],
    [
        {"text": "SOCIALISM IS A FAMILY, NOT A DOCTRINE", "role": "primary"},
        {"text": "SOCIAL OWNERSHIP PLUS DEMOCRATIC CONTROL", "role": "mechanism"},
        {"text": "UTOPIAN, FABIAN, GUILD, MARKET, GANDHIAN", "role": "evidence"},
        {"text": "SOCIALISM, COMMUNISM, SOCIAL DEMOCRACY", "role": "comparison"},
        {"text": "TRUSTEESHIP, BREAD LABOUR, VILLAGE SELF-RULE", "role": "outcome"},
        {"text": "NATIONALISATION IS NOT SOCIALISATION", "role": "caution"},
    ],
    [
        {"text": "RIVAL ROUTES TO ONE DESTINATION", "role": "primary"},
        {"text": "ABOLISH OR FIRST CAPTURE THE STATE", "role": "mechanism"},
        {"text": "BAKUNIN, MARX, GANDHI, M. N. ROY", "role": "evidence"},
        {"text": "REFORM AGAINST REVOLUTION", "role": "comparison"},
        {"text": "MEANS PREFIGURE ENDS", "role": "outcome"},
        {"text": "NEVER TWO SEQUENTIAL SUMMARIES", "role": "caution"},
    ],
    [
        {"text": "OBJECTION, REPLY, RESIDUAL, VERDICT", "role": "primary"},
        {"text": "THE THIRD MOVE CARRIES THE MARKS", "role": "mechanism"},
        {"text": "SIX STANDING CRITICISMS", "role": "evidence"},
        {"text": "DIAGNOSIS SEPARATED FROM REMEDY", "role": "comparison"},
        {"text": "GRADED VERDICT NAMES ITS AXIS", "role": "outcome"},
        {"text": "A STATE'S RECORD REFUTES NO THEORY", "role": "caution"},
    ],
)


GRAPHICAL_STAGE_ZERO_GROUPS = [
    {
        "heading": "ONE DISCRIMINATING QUESTION",
        "role": "evidence",
        "items": [
            "Is domination produced chiefly by coercive authority, by the "
            "capitalist mode of production, or by socially uncontrolled "
            "productive property?",
            "Anarchism answers authority, Marxism answers class relations "
            "generated by the mode of production, socialism answers "
            "uncontrolled property and production.",
            "Every later disagreement about the state, revolution and freedom "
            "is derived from the answer given here.",
        ],
    },
    {
        "heading": "TWO SENSES OF IDEOLOGY",
        "role": "mechanism",
        "items": [
            "The analytical sense is an organised outlook combining "
            "descriptive claims, evaluative commitments and practical "
            "prescriptions.",
            "The critical Marxist sense names a defect: historically specific "
            "class relations made to appear natural, universal and "
            "inevitable.",
            "Declaring the sense in the opening lines disarms the "
            "self-refutation objection before it can be raised.",
        ],
    },
    {
        "heading": "SHARED AXES FOR EVERY COMPARISON",
        "role": "outcome",
        "items": [
            "Authority, property, class, revolution, state and freedom are the "
            "recurrent axes of this clause.",
            "Running rival doctrines down the same axes converts a pair of "
            "summaries into an adjudicated comparison.",
            "The diagnosis generates the prescription, so an answer that lists "
            "prescriptions without diagnoses has already lost the structure.",
        ],
    },
]


GRAPHICAL_STAGE_GROUPS = (
    GRAPHICAL_STAGE_ZERO_GROUPS,
    [
        {
            "heading": "THE STANDARD IMPOSED ON AUTHORITY",
            "role": "evidence",
            "items": [
                "Legitimate authority must be compatible with the moral "
                "autonomy and equality of persons.",
                "The state claims a territorial monopoly of law-making, "
                "coercion and punishment over everyone within its borders.",
                "Obedience is demanded because a command is legally "
                "authoritative, not because its content is independently "
                "right.",
            ],
        },
        {
            "heading": "WHY THE BURDEN IS NOT DISCHARGED",
            "role": "mechanism",
            "items": [
                "A standing right of that kind subordinates one person's "
                "practical judgment to another's institutional will.",
                "Bakunin adds a corruption thesis: concentrated power deforms "
                "both the ruler and the ruled.",
                "Proudhon attacks property where it functions as an "
                "institutional power of appropriation and dependence, and "
                "Kropotkin argues that mutual aid is a genuine source of "
                "order.",
            ],
        },
        {
            "heading": "BOUNDARIES AND THE SECURITY OBJECTION",
            "role": "caution",
            "items": [
                "Anarchy names the collapse of rule, anarchism a normative "
                "critique of domination, and civil disobedience a breach of "
                "particular laws only.",
                "Even the libertarian minimal state is rejected, because the "
                "objection is to the monopoly and not to its size.",
                "The security objection is answered by comparing rival "
                "distributions of coercive power, and the residual is the "
                "persistent organised aggressor.",
            ],
        },
    ],
    [
        {
            "heading": "FIVE STRANDS ON THE PROPERTY AXIS",
            "role": "evidence",
            "items": [
                "Mutualism defends possession and exchange without "
                "exploitative property relations, through contracts and "
                "workers' associations.",
                "Collectivist anarchism places productive resources under "
                "collective control in federated producer communities, and "
                "anarcho-communism adds distribution according to need.",
                "Individualist anarchism defends strong personal sovereignty, "
                "while philosophical anarchism denies an automatic duty to "
                "obey without demanding insurrection.",
            ],
        },
        {
            "heading": "WHY VOLUNTARY ORDER IS AN INSTITUTIONAL CLAIM",
            "role": "mechanism",
            "items": [
                "Anarchism does not infer that every person is always "
                "benevolent; the claim is that order can arise from "
                "reciprocity, custom, association and horizontal "
                "coordination.",
                "Village assemblies, worker cooperatives, mutual-aid networks "
                "and decentralised federations illustrate limited capacities "
                "for non-sovereign coordination.",
                "They do not by themselves establish that a complex society "
                "can eliminate all public authority, and the honest answer "
                "says so.",
            ],
        },
        {
            "heading": "GANDHI'S QUALIFIED PLACE",
            "role": "outcome",
            "items": [
                "Self-rule, decentralised village republics and a state "
                "reduced to a minimum create a genuine anarchist affinity.",
                "Non-violence, trusteeship, religious ethics and the "
                "constructive programme replace class war and anti-theism.",
                "The safest formulation grades the label: an anarchist in "
                "ideal and a pragmatic reformer in political method.",
            ],
        },
    ],
    [
        {
            "heading": "THE SIX-STEP MATERIALIST ARGUMENT",
            "role": "evidence",
            "items": [
                "Human beings must produce the means of life, and production "
                "occurs through definite social relations.",
                "Productive forces develop within those relations until the "
                "relations obstruct further development and become fetters.",
                "The conflict becomes social and political struggle, from "
                "which a new mode of production can emerge.",
            ],
        },
        {
            "heading": "THE FOUR STRUCTURAL TERMS",
            "role": "mechanism",
            "items": [
                "Productive forces name labour-power, knowledge, tools and "
                "technology; relations of production name ownership, control "
                "and class relations.",
                "The mode of production is the unity of forces and relations, "
                "such as feudalism or capitalism.",
                "Base and superstructure name a relation between the economic "
                "structure and law, politics and ideology, not a mechanical "
                "one-way switch.",
            ],
        },
        {
            "heading": "USING THE DIALECTIC WITH CARE",
            "role": "caution",
            "items": [
                "Contradiction drives development, but the primacy of a "
                "self-developing Idea is rejected and contradictions are "
                "embedded in material life.",
                "The formula thesis, antithesis and synthesis is later "
                "textbook shorthand and is not Marx's own fixed three-step "
                "law.",
                "The defensible charge is a tendency toward economic "
                "reductionism, so conceding it early removes the examiner's "
                "readiest objection.",
            ],
        },
    ],
    [
        {
            "heading": "FOUR DIMENSIONS OF ALIENATED LABOUR",
            "role": "evidence",
            "items": [
                "From the product, which confronts the producer as another "
                "person's property, and from the activity of labour, which is "
                "externally compelled rather than self-realising.",
                "From species-being, in that conscious creative activity is "
                "reduced to a means of survival.",
                "From other persons, as workers compete and social relations "
                "assume commodity form.",
            ],
        },
        {
            "heading": "WHY EXPLOITATION IS STRUCTURAL",
            "role": "mechanism",
            "items": [
                "Workers lack independent access to the means of production "
                "and must therefore sell labour-power to live under a formally "
                "free contract.",
                "The capitalist controls the labour process and the product "
                "while competition compels accumulation and extraction.",
                "Value created in the working day exceeds the value "
                "represented by wages, and the remainder is appropriated as "
                "surplus value.",
            ],
        },
        {
            "heading": "TWO DISTINCTIONS THAT CARRY THE MARKS",
            "role": "comparison",
            "items": [
                "Alienation is broader than low wages: a well-paid worker "
                "remains alienated where labour, product and purpose are "
                "controlled by another.",
                "Exploitation concerns the relation of production while "
                "inequality concerns the distribution of holdings, so "
                "redistribution may leave exploitative control intact.",
                "Species-being can be reconstructed minimally as meaningful "
                "agency, social recognition and control over central "
                "activities.",
            ],
        },
    ],
    [
        {
            "heading": "IDEOLOGY AND THE STATE",
            "role": "evidence",
            "items": [
                "Ideology is not merely a lie but a socially rooted framework "
                "in which historically specific relations appear natural and "
                "inevitable.",
                "The modern state secures the general conditions of the "
                "capitalist order while presenting itself as the "
                "representative of a universal interest.",
                "Relative autonomy from any particular capitalist is "
                "compatible with a structural class function.",
            ],
        },
        {
            "heading": "REVOLUTION AND THE TWO PHASES",
            "role": "mechanism",
            "items": [
                "Capitalism socialises production while retaining private "
                "appropriation, and organised class struggle makes "
                "transformation possible.",
                "The dictatorship of the proletariat denotes a transitional "
                "political supremacy of the working class, not permanent "
                "one-party rule.",
                "The lower phase distributes by contribution and retains a "
                "bourgeois measure; the higher phase aspires to distribution "
                "according to need.",
            ],
        },
        {
            "heading": "EQUALITY, FREEDOM AND THE RESIDUAL",
            "role": "caution",
            "items": [
                "Formal equality asks whether the same rule applies; "
                "substantive equality asks whether persons can actually "
                "develop and participate.",
                "Marxian socialism is consistent with individual freedom only "
                "where collective ownership enlarges real self-development and "
                "democratic control.",
                "The strongest historical objection is that transitional "
                "states entrench rather than wither, and the theory supplies "
                "no internal safeguard against it.",
            ],
        },
    ],
    [
        {
            "heading": "FOUR CLASSICAL CLAIMS AND THEIR REVISERS",
            "role": "evidence",
            "items": [
                "Lenin replaces the expectation that revolution matures in the "
                "most advanced economy with imperialism, the weakest link and "
                "a vanguard party under democratic centralism.",
                "Gramsci replaces ideology as a reflex of the base with "
                "hegemony contested in civil society through organic "
                "intellectuals and a war of position.",
                "Althusser replaces the humanist categories with Repressive "
                "and Ideological State Apparatuses and the interpellation of "
                "individuals as subjects.",
            ],
        },
        {
            "heading": "THE STATE DEBATE IN THREE MOVES",
            "role": "mechanism",
            "items": [
                "Miliband's instrumentalism in The State in Capitalist Society "
                "(1969) turns on social composition, structural leverage and "
                "positional interest.",
                "Poulantzas replies in Political Power and Social Classes "
                "(1973) that the state is a condensation of class forces with "
                "relative autonomy, functional for capital in general.",
                "Run it as claim, objection and internal limit: autonomy must "
                "remain relative or the analysis becomes pluralism under "
                "another name.",
            ],
        },
        {
            "heading": "RESIDUALS THAT MUST BE CONCEDED",
            "role": "caution",
            "items": [
                "Substitutionism is unanswered: nothing in the Leninist model "
                "reliably subordinates the party to the class it represents.",
                "Gramsci supplies no independent test separating hegemony from "
                "ordinary reasoned agreement.",
                "Althusser explains stability far better than change and "
                "leaves a thin account of agency, which is why he must not be "
                "merged with Gramsci.",
            ],
        },
    ],
    [
        {
            "heading": "THE CORE SOCIALIST ARGUMENT",
            "role": "evidence",
            "items": [
                "Productive capacities are socially inherited and "
                "cooperatively exercised rather than individually created.",
                "Private control of indispensable productive assets gives some "
                "persons power over the work and life chances of others.",
                "Market outcomes do not automatically track need, desert or "
                "equal freedom, so ownership must answer to social purposes "
                "and democratic justification.",
            ],
        },
        {
            "heading": "SIX VARIETIES ON METHOD AND OWNERSHIP",
            "role": "mechanism",
            "items": [
                "Utopian socialism works through exemplary communities and "
                "moral reform; Marxian socialism through class struggle and "
                "revolutionary transition.",
                "Fabian and democratic socialism proceed by gradual "
                "parliamentary reform; guild socialism through occupational "
                "self-government; market socialism through markets inside "
                "social ownership.",
                "Gandhian socialism works through non-violence, trusteeship, "
                "bread labour, decentralised production, village self-rule and "
                "the welfare of all.",
            ],
        },
        {
            "heading": "THE BOUNDARY THAT EXAMINERS TEST",
            "role": "comparison",
            "items": [
                "Socialism as a family means social control in varied forms; "
                "communism in the Marxian higher phase means common control "
                "with classes abolished.",
                "Social democracy retains private property under regulation, "
                "financing welfare through tax-transfer and public services.",
                "Nationalisation alone is not socialisation, because "
                "socialising power means control by society and not merely by "
                "officials.",
            ],
        },
    ],
    [
        {
            "heading": "ANARCHISM AGAINST MARXISM",
            "role": "evidence",
            "items": [
                "Anarchism locates primary domination in authority and "
                "hierarchy; Marxism locates it in the class relation rooted in "
                "production.",
                "Anarchism would abolish the state without transitional "
                "sovereignty; Marxism uses transitional political power before "
                "the state loses its class function.",
                "Bakunin fears a new state elite; Marxists fear that premature "
                "abolition leaves entrenched capitalist power intact.",
            ],
        },
        {
            "heading": "REFORM, REVOLUTION AND THE INDIAN BRIDGE",
            "role": "mechanism",
            "items": [
                "Democratic socialists hold that suffrage, unions, "
                "constitutional rights and public institutions can "
                "progressively socialise economic power.",
                "Marxism doubts that a state embedded in capitalist property "
                "can be peacefully converted into an impartial instrument.",
                "M. N. Roy's radical humanism keeps the critique of "
                "exploitation while rejecting economic determinism and party "
                "absolutism.",
            ],
        },
        {
            "heading": "MARX AND GANDHI ON MEANS AND ENDS",
            "role": "comparison",
            "items": [
                "The root problem is class exploitation for Marx and greed, "
                "violence and modern industrial civilisation for Gandhi.",
                "The method is class struggle and revolution against "
                "truth-force, trusteeship and constructive work; the scale is "
                "socialised large-scale against decentralised need-oriented "
                "production.",
                "The decisive axis is that for Gandhi the means prefigure the "
                "ends, so a violent centralising path cannot produce a "
                "non-violent decentralised order.",
            ],
        },
    ],
    [
        {
            "heading": "THE LEDGER OF SIX CRITICISMS",
            "role": "evidence",
            "items": [
                "Stateless order is unworkable, history is reduced to "
                "economics, and revolution produces dictatorship.",
                "Social ownership destroys liberty, equality suppresses "
                "difference, and all three doctrines are utopian.",
                "Each criticism is paired with the strongest reply the "
                "doctrine actually possesses and with the residual problem "
                "that survives it.",
            ],
        },
        {
            "heading": "THE PRE-SUBMISSION TRAP CHECK",
            "role": "caution",
            "items": [
                "Anarchism is not chaos, anarchists do not reject all "
                "organisation, and not all anarchists are collectivists.",
                "Marxism is not equality of income, base and superstructure is "
                "not a mechanical one-way cause, and the three-step formula is "
                "not Marx's own.",
                "Socialism is not state ownership and not a synonym for "
                "communism, and no statute, scheme or cooperative proves a "
                "doctrine true.",
            ],
        },
        {
            "heading": "GRADED VERDICTS AND THE ANSWER SPINE",
            "role": "outcome",
            "items": [
                "Separate what an analysis still explains from what it failed "
                "to predict and from what its institutional record "
                "forecloses.",
                "Bring the internal rival before the external one, run one "
                "fully worked objection, reply and residual, and close with a "
                "conditional verdict.",
                "The closing sentence must name the axis on which the "
                "judgment turns, since a verdict without a stated criterion is "
                "an assertion.",
            ],
        },
    ],
)


GRAPHICAL_STAGE_SEQUENCES = (
    [
        "Ask what chiefly produces domination",
        "Anarchism answers coercive authority",
        "Marxism answers the capitalist mode of production",
        "Socialism answers uncontrolled productive property",
        "Declare the sense of ideology, then fix the shared axes",
    ],
    [
        "Legitimate authority must respect autonomy and equality",
        "The state claims a territorial monopoly of coercion",
        "Obedience is demanded independently of content",
        "One person's judgment is subordinated to institutional will",
        "The burden of justification is therefore not discharged",
    ],
    [
        "Sort the family by the property axis",
        "Mutualism, collectivist anarchism, anarcho-communism",
        "Individualist and philosophical anarchism",
        "Voluntary order is institutional, not optimistic",
        "Gandhi: anarchist in ideal, reformer in method",
    ],
    [
        "Begin from how a society produces its means of life",
        "Productive forces develop inside definite relations",
        "Relations become fetters on further development",
        "The conflict becomes social and political struggle",
        "A new mode of production can emerge from that struggle",
    ],
    [
        "Estrangement under private property and division of labour",
        "Product, act of labour, species-being, other persons",
        "Labour-power sold under a formally free contract",
        "Value created exceeds the value wages represent",
        "Surplus value is appropriated as a structural relation",
    ],
    [
        "Ideology is a socially rooted framework, not a lie",
        "The state secures the general conditions of the class order",
        "Socialised production meets private appropriation",
        "Transitional supremacy, not permanent party rule",
        "Contribution in the lower phase, need in the higher",
    ],
    [
        "Name the classical claim the successor revises",
        "Lenin: weakest link and the vanguard party",
        "Gramsci: hegemony contested in civil society",
        "Althusser: apparatuses and interpellation",
        "Miliband against Poulantzas on relative autonomy",
    ],
    [
        "Define socialism as a family, not one doctrine",
        "Social ownership plus democratic control",
        "Utopian, Marxian, Fabian, guild, market, Gandhian",
        "Socialism, communism and social democracy compared",
        "Socialisation is control by society, not by officials",
    ],
    [
        "Fix the axes before naming any school",
        "Abolition against transitional capture of the state",
        "New state elite against premature abolition",
        "Reform can civilise but stays vulnerable",
        "Means prefigure ends for Gandhi; Roy defends the individual",
    ],
    [
        "State the objection in its strongest form",
        "Give the reply the doctrine actually possesses",
        "Name the residual problem that survives",
        "Run the pre-submission trap check",
        "Close with a graded verdict that names its axis",
    ],
)


GRAPHICAL_STAGE_MATRICES = (
    [],
    [],
    [],
    [
        ["ELEMENT", "WHAT IT NAMES", "EXAM USE", "TRAP TO AVOID"],
        [
            "PRODUCTIVE FORCES",
            "labour-power, knowledge, tools and technology",
            "the capacity to produce",
            "treating technology alone as the whole of the forces",
        ],
        [
            "RELATIONS OF PRODUCTION",
            "ownership, control and class relations",
            "who commands and who appropriates",
            "confusing them with mere income distribution",
        ],
        [
            "MODE OF PRODUCTION",
            "the unity of forces and relations",
            "naming feudalism or capitalism precisely",
            "using it loosely for any economic system",
        ],
        [
            "BASE AND SUPERSTRUCTURE",
            "economic structure related to law, politics and ideology",
            "explaining institutions through social labour and power",
            "writing it as a mechanical one-way cause",
        ],
        [
            "CLASS STRUGGLE",
            "conflict rooted in opposed structural interests",
            "the motor of historical transformation",
            "reducing it to personal antagonism between employers and workers",
        ],
    ],
    [],
    [],
    [
        ["CLASSICAL CLAIM", "WHO REVISES IT", "WHAT REPLACES IT", "GROUND OF THE REVISION"],
        [
            "revolution matures where capitalism is most advanced",
            "Lenin",
            "the weakest link in the imperialist chain plus a vanguard party under democratic centralism",
            "revolution did not occur first in the most industrialised economies",
        ],
        [
            "ruling ideas are a reflex of the economic base",
            "Gramsci",
            "hegemony as an achievement won and lost in civil society",
            "capitalism survived defeat and crisis in Western Europe through consent",
        ],
        [
            "the state is an instrument of the ruling class",
            "Miliband, then Poulantzas",
            "instrumental capture answered by relative autonomy and the condensation of class forces",
            "the state acts against particular capitalists in the general interest of capital",
        ],
        [
            "consciousness is determined by social being",
            "Althusser",
            "subjects produced by ideological apparatuses through interpellation",
            "relations of production must be reproduced daily and voluntarily",
        ],
    ],
    [
        ["AXIS", "SOCIALISM (FAMILY)", "COMMUNISM (HIGHER PHASE)", "SOCIAL DEMOCRACY"],
        [
            "PROPERTY",
            "social control in varied forms",
            "common control with classes abolished",
            "private property retained but regulated",
        ],
        [
            "STATE",
            "may remain democratic and active",
            "the political state is expected to lose its class function",
            "a welfare-regulatory state",
        ],
        [
            "DISTRIBUTION",
            "contribution, need or mixed principles",
            "according to need in the higher phase",
            "tax-transfer plus public services",
        ],
        [
            "METHOD",
            "revolutionary or gradual",
            "reached through a transition",
            "constitutional reform",
        ],
    ],
    [],
    [],
)


REQUIRED_CORE_TERMS = (
    "political ideolog",
    "anarchism",
    "Marxism",
    "socialism",
    "domination",
    "coercive authority",
    "mode of production",
    "anarchy",
    "civil disobedience",
    "minimal state",
    "moral autonomy",
    "monopoly",
    "mutual aid",
    "federation",
    "voluntary association",
    "Proudhon",
    "Bakunin",
    "Kropotkin",
    "mutualism",
    "anarcho-communism",
    "individualist anarchism",
    "philosophical anarchism",
    "Gandhi",
    "trusteeship",
    "bread labour",
    "village",
    "dialectical",
    "historical materialism",
    "productive forces",
    "relations of production",
    "base",
    "superstructure",
    "class struggle",
    "fetters",
    "alienation",
    "species-being",
    "commodity",
    "labour-power",
    "surplus value",
    "exploitation",
    "praxis",
    "ideology",
    "dictatorship of the proletariat",
    "communism",
    "classless",
    "Gotha",
    "formal equality",
    "substantive equality",
    "equity",
    "freedom",
    "Lenin",
    "imperialism",
    "weakest link",
    "vanguard",
    "democratic centralism",
    "trade-union consciousness",
    "substitutionism",
    "Gramsci",
    "hegemony",
    "civil society",
    "organic intellectuals",
    "war of position",
    "war of manoeuvre",
    "counter-hegemony",
    "contradictory consciousness",
    "Althusser",
    "Repressive State Apparatus",
    "Ideological State Apparatuses",
    "interpellation",
    "overdetermination",
    "Miliband",
    "Poulantzas",
    "instrumentalism",
    "relative autonomy",
    "condensation of class forces",
    "1969",
    "1973",
    "utopian socialism",
    "Owen",
    "Fourier",
    "Saint-Simon",
    "Fabian",
    "democratic socialism",
    "guild socialism",
    "market socialism",
    "Gandhian socialism",
    "social democracy",
    "nationalisation",
    "socialisation",
    "planning",
    "incentive",
    "bureaucratic",
    "M. N. Roy",
    "radical humanis",
    "Ambedkar",
    "caste",
    "Directive Principles",
    "1844",
    "revolution",
    "reform",
    "self-development",
)

ASCII_PANELS = ASCII_PANELS + (
    {
        "title": "Exact printed ownership and the ideology comparison firewall",
        "structural_type": "ownership-boundary-and-comparison-matrix",
        "sessions": [1, 9],
        "lines": [
            "OFFICIAL CLAUSE -> Political Ideologies: ANARCHISM; MARXISM and SOCIALISM",
            "        |",
            "        v",
            "FULL OWNERSHIP                         BOUNDED FOILS / LINK-OUTS",
            "  ANARCHISM -> authority and hierarchy   LIBERALISM / NEOLIBERALISM -> foil only",
            "  MARXISM  -> class, production, praxis   FASCISM -> not printed; no false equivalence",
            "  SOCIALISM -> social control variants    GANDHISM -> only Gandhi-as-anarchist and",
            "                                                  Gandhian-socialism PYQ limbs",
            "        |",
            "        v",
            "+------------+----------------+----------------+----------------------+",
            "| AXIS       | ANARCHISM      | MARXISM       | SOCIALISM FAMILY     |",
            "+------------+----------------+----------------+----------------------+",
            "| PERSON     | autonomous and | social         | interdependent and   |",
            "|            | cooperative    | producer       | effectively free     |",
            "| STATE      | presumptively  | class-state,   | decentralised through|",
            "|            | illegitimate   | then superseded| democratic-public    |",
            "| PROPERTY   | reject its     | means of       | public, cooperative, |",
            "|            | dominating use | production     | guild, worker, mixed |",
            "| FREEDOM    | non-domination | non-alienated  | capacity plus social |",
            "|            | and self-rule  | development    | security and control |",
            "| CHANGE     | prefiguration, | class struggle | reform, planning,    |",
            "|            | federation     | and transition | markets or revolution|",
            "+------------+----------------+----------------+----------------------+",
            "CONTROL -> ideology is diagnosis + evaluation + strategy + regulative order,",
            "           not merely a party programme or a label for disliked politics.",
        ],
    },
    {
        "title": "Variant taxonomy, historical control and contemporary verdict",
        "structural_type": "variant-taxonomy-and-graded-relevance-ledger",
        "sessions": [3, 7, 8, 10],
        "lines": [
            "ANARCHIST LINEAGE",
            "  GODWIN -> rational anti-government criticism",
            "  PROUDHON -> mutualism | BAKUNIN -> collectivist revolution",
            "  KROPOTKIN -> mutual aid/anarchist communism | TOLSTOY -> pacifist refusal",
            "        |",
            "MARXIST VARIANT CONTROL",
            "  HUMANIST -> alienation, praxis, agency, self-emancipation",
            "  STRUCTURAL -> apparatuses, interpellation, reproduction, overdetermination",
            "  BEST SYNTHESIS -> structures explain power; agents must explain change",
            "        |",
            "SOCIALIST TRANSFORMATION LOGICS",
            "  UTOPIAN -> exemplary moral/cooperative designs",
            "  SCIENTIFIC -> material history, class contradiction, productive forces",
            "  DEMOCRATIC/FABIAN -> gradual reform | GUILD -> producer self-rule",
            "  MARKET -> exchange inside social ownership | GANDHIAN -> non-violent scale",
            "        |",
            "HISTORICAL CONTROL -> separate Marx's diagnosis, later transition theories and",
            "  the record of party-states. Outcomes test the promised WITHERING AWAY but",
            "  do not make every Marxian category identical with every later regime.",
            "        |",
            "CONTEMPORARY VERDICT",
            "  ANARCHISM -> authority critique survives; scale/enforceable rights remain",
            "  MARXISM   -> diagnosis survives; timetable and transition remain vulnerable",
            "  SOCIALISM -> social-control question survives; bureaucracy remains the risk",
            "  PANDEMIC  -> disorder, state expansion and mutual aid may coexist; none alone",
            "               establishes anarchism as society's adopted ideology.",
        ],
    },
)

REQUIRED_CORE_TERMS = REQUIRED_CORE_TERMS + (
    "exact printed ownership",
    "Godwin",
    "Tolstoy",
    "scientific socialism",
    "humanist Marxism",
    "structural Marxism",
    "withering away",
    "party-state",
    "fascism",
    "neoliberalism",
)

ADVANCED_SESSION_TITLES = tuple(str(spec["title"]) for spec in SESSION_SPECS)


_SESSIONS = len(SESSION_SPECS)
if _SESSIONS != 10:
    raise ValueError(
        f"Political Ideologies requires exactly 10 core sessions, found {_SESSIONS}."
    )
_PANELS = len(ASCII_PANELS)
if _PANELS != 12:
    raise ValueError(
        f"Political Ideologies requires exactly 12 ASCII panels, found {_PANELS}."
    )
_PILLS = len(GRAPHICAL_PILLS)
if _PILLS != _SESSIONS:
    raise ValueError(
        f"Graphical pill sets must match the core sessions, found {_PILLS}."
    )
_GROUPS = len(GRAPHICAL_STAGE_GROUPS)
_SEQUENCES = len(GRAPHICAL_STAGE_SEQUENCES)
_MATRICES = len(GRAPHICAL_STAGE_MATRICES)
if not _GROUPS == _SEQUENCES == _MATRICES == _SESSIONS:
    raise ValueError(
        "Graphical groups, sequences and matrices must each match the core "
        f"sessions: {_GROUPS}, {_SEQUENCES}, {_MATRICES}."
    )


def _extract_owner_section(owner_text: str, start: str, end: str) -> str:
    match = re.search(
        rf"(?ms)^{re.escape(start)}\s*$.*?(?=^{re.escape(end)}\s*$)",
        owner_text,
    )
    if not match:
        raise ValueError(f"Cannot extract owner section {start!r}.")
    return match.group(0).strip()


def _demote_owner(fragment: str) -> str:
    return re.sub(
        r"(?m)^(#{2,4})\s+",
        lambda match: "#" * min(len(match.group(1)) + 1, 5) + " ",
        fragment,
    )


def transform_assembled(
    text: str,
    *,
    owner_text: str,
    generation: int,
) -> str:
    if generation != 4:
        raise ValueError(
            f"Political Ideologies semantic successor is pinned to g4, got g{generation}."
        )

    text = re.sub(
        r"(?m)^!\[(?:Anarchism, Marxism and socialism|Political Ideologies)"
        r"[^\]]*\]\([^)]+\)\s*\n+\*Concept map:.*?\*\s*\n*",
        "",
        text,
        count=1,
    )

    boundary = _demote_owner(
        _extract_owner_section(
            owner_text,
            "## Exact printed ownership and cross-topic firewall",
            "## 0. ONE-SCREEN MAP",
        )
    )
    comparison = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### Shared comparison axes",
            "## 1. ANARCHISM",
        )
    )
    lineage = _demote_owner(
        _extract_owner_section(
            owner_text,
            "#### Thinker lineage inside the strands",
            "### 1.5 Natural order and voluntary cooperation",
        )
    )
    marxist_variants = _demote_owner(
        _extract_owner_section(
            owner_text,
            "#### Humanist and structural Marxism",
            "### 2A.2 Lenin: imperialism, the weakest link and the vanguard",
        )
    )
    socialist_variants = _demote_owner(
        _extract_owner_section(
            owner_text,
            "#### Utopian and scientific socialism",
            "### 3.4 Socialism, communism and social democracy",
        )
    )
    contemporary = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 4.5 Contemporary relevance without current-affairs dependence",
            "## 5. CRITICISMS AND REPLIES",
        )
    )

    text = text.replace(
        "- **Canonical doctrine source:** "
        "`upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/"
        "Political-Ideologies.md` (7,676 words), sliced verbatim into the CORE "
        "UPSC layers (each canonical teaching passage exactly once) and preserved "
        "again, in full, in the canonical apparatus block.",
        "- **Canonical doctrine source:** "
        "`upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/"
        "Political-Ideologies.md`, repaired under the ten-gate semantic-"
        "completeness protocol and promoted into this immutable successor.",
    )
    text = text.replace(
        "- **Doctrine grounding (in the canonical file):** the discriminating "
        "question",
        "- **Doctrine grounding (in the canonical file):** exact printed ownership "
        "of Anarchism, Marxism and Socialism; the shared person/society/state, "
        "property, freedom/equality/justice and change axes; the discriminating "
        "question",
        1,
    )
    text = text.replace(
        "Proudhon/Bakunin/Kropotkin, individualist/mutualist/collectivist/"
        "communist strands",
        "Godwin/Proudhon/Bakunin/Kropotkin/Tolstoy, individualist/mutualist/"
        "collectivist/communist strands",
        1,
    )
    text = text.replace(
        "the Miliband-Poulantzas debate on relative autonomy, and M. N. Roy's "
        "radical humanism)",
        "the Miliband-Poulantzas debate on relative autonomy, humanist/structural "
        "Marxism, Marxism-versus-later-regime control, and M. N. Roy's radical "
        "humanism)",
        1,
    )
    text = text.replace(
        "- **Scaffolding discipline:** the concept-of-ideology apparatus "
        "(descriptive, pejorative/Marxian, integrative and action-guiding senses; "
        "ideology vs philosophy, political theory, doctrine, programme and "
        "propaganda; the end-of-ideology debate) and the liberalism/conservatism "
        "comparison points are standard, verifiable political theory. They appear "
        "only in the authored scaffolding layers, always labelled as context beyond "
        "this Philosophy owner's canonical core (Anarchism; Marxism and Socialism), "
        "never as fabricated canonical doctrine.",
        "- **Scaffolding discipline:** the concept-of-ideology apparatus is bounded "
        "context. Liberalism, neoliberalism and conservatism are comparison foils "
        "only; fascism is neither printed nor routed. None is promoted into the "
        "canonical core, and no false equivalence is drawn among these families.",
    )

    preservation = (
        "**Preservation note:** the canonical doctrine is reorganised into layers, "
        "never compressed. Every doctrine, argument, objection/reply, comparison, "
        "corpus-depth delta, PYQ route, directive rule, graded verdict and "
        "provenance caution is retained; simplification means adding accessible "
        "gateways, not deleting complexity."
    )
    if "Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            preservation,
            preservation + "\n\n" + boundary + "\n\n" + comparison,
            1,
        )
    if "Thinker lineage inside the strands" not in text:
        text = text.replace(
            "#### 1.5 Natural order and voluntary cooperation",
            lineage + "\n\n#### 1.5 Natural order and voluntary cooperation",
            1,
        )
    if "Humanist and structural Marxism" not in text:
        text = text.replace(
            "#### 2A.2 Lenin: imperialism, the weakest link and the vanguard",
            marxist_variants
            + "\n\n#### 2A.2 Lenin: imperialism, the weakest link and the vanguard",
            1,
        )
    if "Utopian and scientific socialism" not in text:
        text = text.replace(
            "#### 3.4 Socialism, communism and social democracy",
            socialist_variants
            + "\n\n#### 3.4 Socialism, communism and social democracy",
            1,
        )
    if "Contemporary relevance without current-affairs dependence" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Inter-School Debates: Anarchism, Marxism, "
            "Democratic Socialism, Gandhi and M. N. Roy",
            contemporary
            + "\n\n#### CLOSING RECALL FLOW — Inter-School Debates: Anarchism, "
            "Marxism, Democratic Socialism, Gandhi and M. N. Roy",
            1,
        )

    text = text.replace(
        "10. **Do not treat statutes, cooperatives or welfare schemes as proof of "
        "socialism.** ⚠️ They are dated institutional illustrations; the "
        "philosophical issue is control, freedom and justice.",
        "10. **Do not treat statutes, cooperatives or welfare schemes as proof of "
        "socialism.** ⚠️ They are dated institutional illustrations; the "
        "philosophical issue is control, freedom and justice.\n"
        "11. **Do not import liberalism, neoliberalism or fascism as additional "
        "printed ideologies.**\n"
        "12. **Do not omit Godwin and Tolstoy when a thinker taxonomy is asked.**\n"
        "13. **Do not equate utopian with foolish or scientific with infallible.**\n"
        "14. **Do not merge humanist and structural Marxism.**\n"
        "15. **Do not treat later communist regimes as either irrelevant to "
        "Marxism or identical with Marx's theory.**",
        1,
    )
    text = text.replace(
        "**Promoted vocabulary (this pass) ⚠️:** weakest link",
        "**Promoted vocabulary (this pass) ⚠️:** Godwin · Tolstoy · utopian/"
        "scientific socialism · humanist/structural Marxism · withering away · "
        "theory/regime distinction · weakest link",
        1,
    )
    if "P13 · Anarchism contains distinct thinker-strands" not in text:
        text = text.replace(
            "- **P12 · Equity is not equality.** Claim: distribution according to "
            "contribution belongs to an earlier stage; distribution according to "
            "need belongs to a later one → Named: Marx, *Critique of the Gotha "
            "Programme* → Use for: equity/equality stems → Limit: a normative "
            "projection, not a demonstrated historical law.",
            "- **P12 · Equity is not equality.** Claim: distribution according to "
            "contribution belongs to an earlier stage; distribution according to "
            "need belongs to a later one → Named: Marx, *Critique of the Gotha "
            "Programme* → Use for: equity/equality stems → Limit: a normative "
            "projection, not a demonstrated historical law.\n"
            "- **P13 · Anarchism contains distinct thinker-strands.** Godwin, "
            "Proudhon, Bakunin, Kropotkin and Tolstoy differ over property, "
            "revolution and religion.\n"
            "- **P14 · Utopian and scientific socialism name rival transformation "
            "logics.** Moral-exemplary design contrasts with material/class "
            "explanation; neither label settles feasibility.\n"
            "- **P15 · Marxism is not one later regime.** Separate Marx's diagnosis, "
            "transition theories and institutional outcomes while retaining the "
            "historical objection.\n"
            "- **P16 · Contemporary relevance is criterion-specific.** Diagnostic "
            "reach does not establish predictive or institutional success.",
            1,
        )
    text = text.replace(
        "the selectable evidence bank (P1-P12)",
        "the selectable evidence bank (P1-P16)",
        1,
    )
    text = text.replace(
        "- Local course source, *Socio-Political Philosophy*, sections on "
        "anarchism, Marxism, socialism and M. N. Roy.",
        "- Local compiled notes PDF, *Socio-Political Philosophy*, searchable "
        "pp. 122-139; no named author is asserted.",
    )
    text = text.replace(
        "- O. P. Gauba, *An Introduction to Political Theory*, chapters on "
        "ideology, socialism, Marxism, anarchism and Gandhism.",
        "- O. P. Gauba, *An Introduction to Political Theory*, searchable local "
        "PDF pp. 28-83.",
    )

    closure_replacements = {
        (
            "KEY TERMS / DEFINITIONS: political ideology as diagnosis and "
            "prescription | the discriminating question of domination | coercive "
            "authority | capitalist mode of production | social control of "
            "productive property | analytical against critical senses of ideology"
        ): (
            "KEY TERMS / DEFINITIONS: ideology | diagnosis | domination | "
            "prescription | ownership"
        ),
        (
            "KEY TERMS / DEFINITIONS: coercive political authority | territorial "
            "monopoly of law, coercion and punishment | moral autonomy and equality "
            "of persons | content-independent obligation to obey the state | burden "
            "of justification | Bakunin's corruption thesis | Proudhon on property "
            "as institutional power | Kropotkin on mutual aid as a source of order"
        ): (
            "KEY TERMS / DEFINITIONS: authority | monopoly | autonomy | obligation "
            "| justification"
        ),
        (
            "KEY TERMS / DEFINITIONS: mutualism | collectivist anarchism | "
            "anarcho-communism | individualist anarchism | philosophical anarchism "
            "| mutual aid, federation and recallable delegation | anarchist in "
            "ideal, reformer in method"
        ): (
            "KEY TERMS / DEFINITIONS: mutualism | collectivism | communism | "
            "individualism | federation"
        ),
        (
            "KEY TERMS / DEFINITIONS: productive forces | relations of production "
            "| mode of production | base and superstructure | class struggle as the "
            "motor of transformation | relations of production as fetters | "
            "material reproduction as a necessary condition"
        ): (
            "KEY TERMS / DEFINITIONS: forces | relations | mode | base | class"
        ),
        (
            "KEY TERMS / DEFINITIONS: estrangement from the product | estrangement "
            "from the activity of labour | species-being | estrangement from other "
            "persons | labour-power sold under a formally free contract | surplus "
            "value | structural exploitation against unfair bargaining"
        ): (
            "KEY TERMS / DEFINITIONS: alienation | species-being | labour-power | "
            "surplus | exploitation"
        ),
        (
            "KEY TERMS / DEFINITIONS: ideology as a socially rooted framework | the "
            "state's general conditions of the class order | relative autonomy "
            "compatible with class function | socialised production against private "
            "appropriation | dictatorship of the proletariat as transitional "
            "supremacy | lower and higher phases of communist society | formal "
            "against substantive equality | equity as differential provision "
            "justified by need"
        ): (
            "KEY TERMS / DEFINITIONS: ideology | state | transition | communism | "
            "equity"
        ),
        (
            "KEY TERMS / DEFINITIONS: imperialism and the weakest link | vanguard "
            "party and democratic centralism | substitutionism | hegemony in civil "
            "society | organic intellectuals and the war of position | Repressive "
            "and Ideological State Apparatuses | interpellation and overdetermination "
            "| instrumentalism against relative autonomy"
        ): (
            "KEY TERMS / DEFINITIONS: vanguard | hegemony | apparatuses | "
            "interpellation | autonomy"
        ),
        (
            "KEY TERMS / DEFINITIONS: social ownership and democratic control | "
            "utopian socialism | Fabian and democratic socialism | guild socialism "
            "| market socialism | Gandhian trusteeship and bread labour | "
            "socialisation against mere nationalisation | social democracy as "
            "regulated private property"
        ): (
            "KEY TERMS / DEFINITIONS: ownership | utopian | scientific | guild | "
            "socialisation"
        ),
        (
            "KEY TERMS / DEFINITIONS: abolition against transitional capture of the "
            "state | the fear of a new ruling stratum | premature abolition leaving "
            "capitalist power intact | socialising economic power through suffrage "
            "and parliament | means prefigure ends | trusteeship against class "
            "struggle | radical humanism and the freedom of the individual"
        ): (
            "KEY TERMS / DEFINITIONS: abolition | transition | reform | means-ends "
            "| humanism"
        ),
        (
            "KEY TERMS / DEFINITIONS: objection, reply and residual problem | "
            "stateless order and the coordination objection | economic reductionism "
            "| revolution and the authoritarian record | social ownership against "
            "liberty | equality of status without uniformity | feasibility as a "
            "constraint on normativity"
        ): (
            "KEY TERMS / DEFINITIONS: objection | reply | residual | feasibility | "
            "verdict"
        ),
    }
    for old, new in closure_replacements.items():
        text = text.replace(old, new)
    return text
