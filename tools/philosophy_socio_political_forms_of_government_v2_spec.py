"""Durable learner-v2 content and master-flow specification for Forms of Government.

Philosophy Optional, Paper II, Socio-Political Philosophy, official topic 4:
``Forms of Government : Monarchy; Theocracy and Democracy.``

Every doctrine, thinker, date and criticism below is grounded in the repository
owners for this clause: the canonical owner ``Forms-of-Government.md``, the
retained layered learning session and workbook, the verified 2018-2025
Socio-Political PYQ ledger, and the Socio-Political advanced dossier.  Nothing
here is taken from a live source, and no publication year, quotation, statute or
constitutional provision is asserted that the repository sources do not already
carry.  No Indian government, party, leader or period is characterised.
"""

from __future__ import annotations

import re


TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-04"
TOPIC_TITLE = "Forms of Government"
TOPIC_NUMBER = 4
SECTION_KEY = "paper-ii-socio-political-philosophy"
GENERATION_DATE = "2026-09-03"
OFFICIAL_SYLLABUS_VERBATIM = (
    "Forms of Government : Monarchy; Theocracy and Democracy."
)
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
    "Forms-of-Government.md"
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
    "Socio-Political\\learning-sessions\\topic-04\\g4\\"
    "topic-04_Complete-Learning-Session_2026-09-03.md"
)
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
        "The Classification Problem: Who Rules, By What Title, For Whose Good",
        "A form of government is the standing arrangement that answers four "
        "questions at once — who rules, by what title, for whose good, and "
        "under what limits — so monarchy, theocracy and democracy are "
        "compressed answers rather than neutral names on a list.",
        "The clause fixes a classificatory and evaluative problem rather than "
        "an institutional inventory: a descriptive classification records who "
        "holds power and how office is filled, a normative verdict judges "
        "whether that arrangement deserves obedience, and the three named "
        "forms are distinguished above all by the title they claim — heredity "
        "and tradition, revelation and sacred law, or consent and political "
        "equality.",
        "Monarchy, theocracy and democracy are not three neutral names for the "
        "same activity: each answers who rules and by what title, and the "
        "marks are earned by also asking for whose good rule is exercised and "
        "under what limits of law, rights and accountability it operates.",
        [
            "who rules, by what title",
            "common good against sectional interest",
            "descriptive classification",
            "normative verdict",
            "source of legitimate authority",
            "limits of law, rights and accountability",
        ],
        "Separate the descriptive classification from the normative verdict in "
        "the opening lines, name the source of legitimate authority each form "
        "claims, say whether rule serves the common good or a sectional "
        "interest, and only then ask under what limits of law, rights and "
        "accountability the regime actually operates.",
        "Every regime label compresses four separate questions into one word, "
        "so a controlled answer unpacks who rules, by what title, for whose "
        "good and under what limits before it names any form at all.",
        "Because the axes come apart, a regime can score well on continuity "
        "and badly on equality, or well on decisiveness and badly on "
        "answerability, which is why comparative verdicts in this clause are "
        "always graded rather than absolute.",
        "Do not treat the stem's label as settled description; a descriptive "
        "question asks what a theocracy is, a normative question asks whether "
        "it ought to be obeyed, and the two must never be answered in the same "
        "register.",
        "If classification is only a set of questions, it decides nothing, and "
        "the exercise looks like taxonomy for its own sake rather than "
        "political philosophy.",
        "The questions are not idle, because each isolates a distinct ground "
        "of criticism: number of rulers exposes concentration, title exposes "
        "arbitrariness, purpose exposes exploitation, and limits expose "
        "domination. A classification that keeps these apart has already begun "
        "the evaluation.",
        "The grid tells you what to ask, never what to conclude; the "
        "substantive verdict on monarchy, theocracy or democracy comes only "
        "from the later arguments about knowledge, revelation, consent and "
        "accountability.",
        "Open with the four-question grid, decide in one line whether the stem "
        "wants description or evaluation, place the named form on the grid, "
        "and close with a graded verdict that states the axis on which the "
        "decision actually turns.",
        [
            "Four questions, not one: who rules, by what title, for whose "
            "good, under what limits.",
            "Monarchy claims heredity and tradition, theocracy claims "
            "revelation and sacred law, democracy claims consent and political "
            "equality.",
            "Descriptive classification records what a regime is; the "
            "normative verdict judges whether it deserves obedience.",
            "No form scores highest on every axis, so the closing verdict is "
            "graded and names its decisive criterion.",
        ],
        [
            visual(
                "The four questions hidden inside every regime label",
                "The opening grid that should be reproduced in one or two "
                "sentences before any form of government is named.",
                "   (1) WHO RULES?           one    |    few    |    many",
                "                                   |",
                "   (2) FOR WHOSE GOOD?   common good  <----->  private or sectional",
                "                                   |",
                "   (3) BY WHAT TITLE?    heredity | conquest | divine sanction |",
                "                         consent and election | sacred law",
                "                                   |",
                "   (4) UNDER WHAT LIMITS?  law? rights? accountability? none?",
                "                                   |",
                "                                   v",
                "        DESCRIPTIVE map (what the regime IS)",
                "                    against",
                "        NORMATIVE verdict (whether it OUGHT to bind anyone)",
            ),
            visual(
                "Three named forms, three different titles to rule",
                "The syllabus names these three because each rests its claim "
                "on a different source of authority, not because they differ "
                "only in size.",
                "+-------------+------------------------+-------------------------+",
                "| FORM        | TITLE CLAIMED          | STANDING DANGER         |",
                "+-------------+------------------------+-------------------------+",
                "| MONARCHY    | heredity, tradition,   | arbitrariness and weak  |",
                "|             | sometimes divine right | accountability          |",
                "| THEOCRACY   | revelation and sacred  | conscience crushed,     |",
                "|             | law, read by clergy    | unequal citizenship     |",
                "| DEMOCRACY   | consent, equality,     | majoritarianism and     |",
                "|             | participation          | manipulated opinion     |",
                "+-------------+------------------------+-------------------------+",
                "   RULE OF USE -> fix the title first; the danger follows from it.",
            ),
        ],
    ),
    session(
        "Plato: The Degeneration of Constitutions and the Critique of Democracy",
        "Plato holds that ruling is a craft requiring knowledge, so "
        "constitutions decay in a determinate order — from the rule of wisdom "
        "through timocracy, oligarchy and democracy to tyranny — as the "
        "ordering principle of soul and city slides from reason to appetite.",
        "In the Republic Plato defends a true aristocracy of knowledge, that "
        "is rule by philosopher-rulers, and derives a degeneration sequence in "
        "which each constitution's dominant value corrupts into the next: "
        "honour yields to the desire for wealth, wealth divides rich from "
        "poor, freedom dissolves discipline, and unrestrained licence delivers "
        "the city to a demagogue who becomes a tyrant.",
        "Plato's target is not participation as such but rule by unexamined "
        "opinion and unrestricted appetite: the ship of state needs a trained "
        "navigator, and a city that treats every opinion as equally qualified "
        "is already preparing its own demagogue.",
        [
            "ruling as a craft of knowledge",
            "ship-of-state analogy",
            "degeneration of constitutions",
            "timocracy, oligarchy, democracy, tyranny",
            "liberty mistaken for qualification",
            "demagogue and the slide to tyranny",
        ],
        "State that Plato judges constitutions by the standard of knowledge, "
        "run the ship-of-state analogy once, lay out the degeneration sequence "
        "from timocracy through oligarchy and democracy to tyranny, show how "
        "liberty mistaken for qualification licenses the demagogue, and close "
        "on the asymmetric verdict.",
        "When the ruling principle of soul and city falls from reason to "
        "appetite, each constitution's dominant value corrupts into the value "
        "of the next, so political decline follows a determinate order rather "
        "than mere accident.",
        "Democracy on this account is not one flawed regime among others but "
        "the immediate antechamber of tyranny, because a city that prizes "
        "freedom above everything makes restraint itself look oppressive.",
        "Plato's critique is not a defence of hereditary monarchy and not a "
        "simple hatred of freedom; it is a defence of rule by knowledge, so "
        "reconstruct the competence, order and demagoguery arguments before "
        "criticising any of them.",
        "Rule by trained guardians supplies no mechanism by which the "
        "guardians' own error is detected or their power removed, and it "
        "treats the moral equality of citizens as politically irrelevant.",
        "Plato can reply that competence is demanded everywhere else in life "
        "and that a city driven by appetite is no freer than one driven by a "
        "tyrant; the diagnosis of demagoguery and defective leadership-"
        "selection survives even where the remedy is refused.",
        "The asymmetry is the whole point: the diagnosis of manipulation, "
        "ignorance and bad leadership-selection stands, while the guardian "
        "remedy fails for want of consent, external correction and any "
        "available epistemic elite.",
        "Name Plato's exact target in two lines, give the degeneration "
        "sequence as a numbered spine, deploy the ship-of-state analogy with "
        "its limitation, and close with the asymmetric verdict that the "
        "diagnosis survives while the authoritarian remedy does not.",
        [
            "Republic: rule of wisdom, then timocracy (honour), oligarchy "
            "(wealth), democracy (freedom), tyranny (domination).",
            "Ship-of-state analogy: navigation is a skill, and numbers confer "
            "no competence.",
            "Three charges: ruling is a craft, liberty is not qualification, "
            "unregulated liberty breeds tyranny.",
            "Asymmetric verdict: the diagnosis of demagoguery survives; "
            "unaccountable guardian rule does not.",
            "2025 Q1(d) asks precisely for this comment, so the sequence and "
            "the verdict must both appear.",
        ],
        [
            visual(
                "The degeneration sequence, with the value that fails at each step",
                "Each stage falls because the value it prizes cannot restrain "
                "the appetite that succeeds it.",
                "   ARISTOCRACY OF KNOWLEDGE  (wisdom rules)",
                "            |  honour displaces wisdom",
                "            v",
                "   TIMOCRACY               (honour, military spiritedness)",
                "            |  desire for wealth displaces honour",
                "            v",
                "   OLIGARCHY               (property; rich divided from poor)",
                "            |  the poor many overthrow the propertied few",
                "            v",
                "   DEMOCRACY               (freedom and equality of desires)",
                "            |  licence makes restraint look oppressive",
                "            v",
                "   TYRANNY                 (one demagogue who flatters, then dominates)",
            ),
            visual(
                "Three charges against democracy, and what each really attacks",
                "Reconstructing the charges separately is what converts a "
                "description of Plato into an argument about him.",
                "+---------------------------+--------------------------------------+",
                "| CHARGE                    | WHAT IT ACTUALLY ATTACKS             |",
                "+---------------------------+--------------------------------------+",
                "| ruling is a craft         | the assumption that all opinions are |",
                "|                           | politically equal in competence      |",
                "| liberty is not a          | levelling the distinction between    |",
                "| qualification             | knowledge and ignorance              |",
                "| unregulated liberty       | indiscipline in family, education    |",
                "| breeds tyranny            | and public life, then the demagogue  |",
                "+---------------------------+--------------------------------------+",
                "   VERDICT -> diagnosis survives; the guardian remedy does not.",
            ),
        ],
    ),
    session(
        "Aristotle: The Six-Fold Classification and the Polity as Middle Course",
        "Aristotle classifies constitutions by two variables together — how "
        "many rule, and whether they rule for the common advantage or their "
        "own — which yields three right forms and three deviations, and makes "
        "polity, not democracy, the good rule of the many.",
        "In the Politics the criteria are the number of rulers, one, few or "
        "many, crossed with the orientation of rule to the common or the "
        "private advantage, producing monarchy, aristocracy and polity as "
        "right forms against tyranny, oligarchy and democracy as their "
        "deviations; polity is the practical mixed constitution, rule of the "
        "many under law, moderated by property, virtue and a broad middle "
        "class.",
        "Classification needs two variables rather than one: number tells you "
        "who decides, orientation tells you for whom, and the right and "
        "corrupt version of each number differ in purpose rather than in "
        "size.",
        [
            "number of rulers times end served",
            "right forms and deviant forms",
            "polity as the good rule of the many",
            "democracy in the classical deviant sense",
            "middle class and mixed constitution",
            "middle course between statism and individualism",
        ],
        "Draw the six-fold classification once, insist that the good-many form "
        "is polity while democracy in Aristotle's usage names its deviation, "
        "explain the mixed constitution and the stabilising middle class, and "
        "use the middle course between statism and individualism as the "
        "adjudicating line against Plato.",
        "Because the same number of rulers may serve either the common "
        "advantage or a sectional one, each numerical class splits into a "
        "right form and its deviation, so purpose rather than size does the "
        "classificatory work.",
        "Polity emerges as the most durable practicable constitution because "
        "extremes of wealth and poverty produce factional rule, whereas a "
        "broad middle class makes lawful moderation self-sustaining.",
        "Do not equate Aristotle's polity with modern democracy: it is an "
        "illuminating mixed-government precursor that excluded many residents "
        "from citizenship, and it is not a regime of universal equal "
        "suffrage.",
        "The phrase common advantage is not self-specifying, so the "
        "classification cannot say which constitution is right without "
        "importing an independent theory of the human good.",
        "Aristotle supplies that theory elsewhere through the human good and "
        "the life of virtue, and the grid still earns its keep by separating "
        "the question of who decides from the question of for whom, a "
        "distinction that single-variable classifications simply collapse.",
        "The claim that polity is most stable is a sociological judgement "
        "about the effect of a broad middle class, not a demonstration that "
        "polity is just.",
        "Open with the two variables, draw the six-fold grid, name polity as "
        "the good-many form, argue the middle-class thesis with its stated "
        "limitation, and close by contrasting Aristotle's realism with Plato's "
        "idealism on the same axis.",
        [
            "Two criteria: number of rulers, and rule for the common or the "
            "private advantage.",
            "Right forms: monarchy, aristocracy, polity. Deviations: tyranny, "
            "oligarchy, democracy.",
            "Polity is the mixed constitution: rule of the many under law with "
            "a broad middle class.",
            "Against statism it refuses the all-wise ruler; against "
            "individualism it refuses unrestricted private self-assertion.",
            "Plato asks who ought ideally to rule; Aristotle asks which "
            "constitution sustains good political life under real conditions.",
        ],
        [
            visual(
                "The six-fold classification: number crossed with purpose",
                "The single most reusable table in this clause, because every "
                "classification stem can be opened from it.",
                "+---------------+---------------------------+------------------------+",
                "| NUMBER RULING | RIGHT FORM (common good)  | DEVIATION (private)    |",
                "+---------------+---------------------------+------------------------+",
                "| ONE           | MONARCHY                  | TYRANNY                |",
                "| FEW           | ARISTOCRACY               | OLIGARCHY              |",
                "| MANY          | POLITY                    | DEMOCRACY (classical)  |",
                "+---------------+---------------------------+------------------------+",
                "   KEY -> the good and corrupt versions of each number differ in",
                "          PURPOSE, not in size.",
            ),
            visual(
                "Why polity is a middle course and not a compromise",
                "The middle-class argument is what lets Aristotle answer both "
                "the idealist and the individualist at once.",
                "   OLIGARCHY  <-------------  POLITY  ------------->  DEMOCRACY",
                "   rule of the wealthy      rule of the many        rule of the poor",
                "   few in their own          UNDER LAW, moderated    many in their own",
                "   interest                  by property, virtue     interest",
                "                             and a broad MIDDLE",
                "                             CLASS",
                "            against STATISM -> value is not absorbed into one",
                "                               all-wise ruler or a total state",
                "            against INDIVIDUALISM -> politics is not reduced to",
                "                               unrestricted private self-assertion",
                "            for CIVIC MODERATION -> citizenship inside a lawful",
                "                               order aimed at the common good",
            ),
        ],
    ),
    session(
        "Monarchy: Absolute and Constitutional, Divine Right and the Freedom Question",
        "Monarchy is rule by one person who normally holds office by heredity, "
        "and its modern assessment turns entirely on whether that office is "
        "absolute, so that the ruler governs, or constitutional, so that the "
        "ruler reigns while elected institutions govern.",
        "Absolute monarchy concentrates executive, legislative and sometimes "
        "judicial functions in a hereditary ruler legitimised by tradition, "
        "conquest or the divine right of kings; constitutional monarchy "
        "retains the crown as a ceremonial and integrating office bound by "
        "convention and law, transfers effective authority to cabinet and "
        "parliament, and thereby relocates accountability instead of "
        "abolishing the throne.",
        "Monarchy leaves room for individual freedom only where law, rights "
        "and representative institutions already restrain the crown: the "
        "institution does not itself ground freedom, and hereditary title "
        "guarantees neither wisdom nor virtue nor answerability.",
        [
            "absolute against constitutional monarchy",
            "hereditary office and the equality objection",
            "divine right of kings",
            "above politics as symbolic neutrality",
            "succession failure and arbitrariness",
            "reigns but does not govern",
        ],
        "Separate absolute from constitutional monarchy in the first two "
        "lines, run the equality, merit, accountability and freedom objections "
        "in order, read above politics as symbolic neutrality inside a "
        "constitutional order rather than supra-legal power, and keep divine "
        "right for the bridge to theocracy.",
        "Hereditary succession settles who shall rule without any test of "
        "competence or consent, so monarchy purchases continuity and "
        "decisiveness at the direct cost of merit and answerability.",
        "Constitutional monarchy therefore survives in modern thought as a "
        "historically adapted symbol rather than a justificatory ideal, since "
        "its defensible functions are prudential and integrative while its "
        "normative basis sits uneasily with equal citizenship.",
        "Monarchy does not mean that every monarch wields unlimited power, so "
        "distinguish absolute, limited and constitutional forms, and remember "
        "that above politics can only mean above party conflict and never "
        "above constitutional accountability.",
        "Hereditary office violates the principle that public authority should "
        "be open to all on equal terms, and it makes competence a matter of "
        "accident rather than of qualification.",
        "The constitutional monarchist replies that a non-elective head of "
        "state separates a politically neutral symbol of continuity from the "
        "elected government that actually rules, which a partisan presidency "
        "cannot do, and that the monarch's role is defined by constitutional "
        "convention rather than personal will.",
        "That reply defends ceremonial monarchy alone: it does nothing for an "
        "absolute ruler's claim to govern without consent or accountability, "
        "and even a symbolic crown carries inherited hierarchy and unequal "
        "civic status.",
        "Fix which type of monarchy the stem has in mind, state what freedom "
        "in the modern sense requires, show what monarchy as a principle of "
        "rule entails, and close with the conditional verdict that monarchy "
        "coexists with freedom only when constitutionalised.",
        [
            "Absolute: concentrated powers, weak institutional "
            "accountability. Constitutional: reigns but does not govern.",
            "Four objections: equality, merit, accountability, freedom.",
            "Divine right sacralises kingship; it is the bridge to theocracy, "
            "not identity with it.",
            "Systematic only if above politics means symbolic neutrality "
            "within a constitutional order.",
            "2021 Q1(d) on freedom and 2023 Q1(e) on systematicity are both "
            "answered from this one distinction.",
        ],
        [
            visual(
                "Two monarchies, and where accountability actually sits",
                "The whole modern defence of monarchy lives in the right-hand "
                "column, and every criticism bites hardest on the left.",
                "+---------------------+----------------------------+---------------------+",
                "| AXIS                | ABSOLUTE MONARCHY          | CONSTITUTIONAL      |",
                "+---------------------+----------------------------+---------------------+",
                "| powers              | executive, legislative and | crown reigns, the   |",
                "|                     | sometimes judicial in one  | cabinet governs     |",
                "| title               | heredity, conquest,        | historic continuity |",
                "|                     | tradition, divine right    | plus legal limits   |",
                "| accountability      | weak and institutionally   | shifted to cabinet  |",
                "|                     | unsecured                  | and parliament      |",
                "| verdict             | efficient but normatively  | acceptable as       |",
                "|                     | risky                      | symbolic headship   |",
                "+---------------------+----------------------------+---------------------+",
            ),
            visual(
                "Reading the above-politics claim without conceding too much",
                "The 2023 stem turns on which of the two readings of above "
                "politics is being asserted.",
                "   ABOVE PARTY CONFLICT                ABOVE CONSTITUTIONAL",
                "   (non-partisan symbol)               ACCOUNTABILITY",
                "            |                                   |",
                "            v                                   v",
                "   role fixed by convention;          no reviewable limit on the",
                "   elected institutions govern        exercise of public power",
                "            |                                   |",
                "            v                                   v",
                "   SYSTEMATIC: legitimacy,            NOT SYSTEMATIC: the order",
                "   continuity and role clarity        ceases to be constitutional",
                "   are all specifiable                and slides to arbitrary rule",
            ),
        ],
    ),
    session(
        "Theocracy: Divine Sovereignty, Sacred Law and the Validity Question",
        "Theocracy is government in which ultimate political authority is "
        "claimed for God, divine law or the authorised interpreters of sacred "
        "truth, so it is not merely a society influenced by religion but a "
        "polity whose sovereignty is held to be divine rather than popular.",
        "Its essential features are the sovereignty of God rather than of the "
        "people, sacred law that guides or determines civil law, clerical "
        "mediation by priests, jurists or religious elites who interpret "
        "divine command, limited pluralism in which dissent appears as "
        "theological deviance, and a fusion in which political and religious "
        "legitimacy overlap.",
        "The decisive line runs between religiously informed public reasoning, "
        "which a constitutional democracy can accommodate, and theocratic "
        "sovereignty, which makes political authority derive from and answer "
        "to religious authority; an answer that condemns theocracy without "
        "drawing this line has not made the argument.",
        [
            "sovereignty of God rather than of the people",
            "sacred law and clerical mediation",
            "the interpretation monopoly",
            "who speaks for God",
            "liberty of conscience and equal citizenship",
            "secularism as an institutional relation",
        ],
        "Define theocracy by the source of sovereignty rather than by "
        "religiosity, name the structural features, press the who-speaks-for-"
        "God problem into the charge of an interpretation monopoly, test the "
        "form against liberty of conscience and equal citizenship, and "
        "separate secularism from hostility to religion before judging.",
        "Because revelation must always be interpreted by human beings, "
        "theocracy transfers political power to interpreters whose authority "
        "is immunised from ordinary criticism, and theological certainty can "
        "then mask ordinary struggles for power.",
        "Citizenship becomes asymmetrical wherever belief differs, dissent is "
        "recast as impiety rather than legitimate disagreement, and the public "
        "basis of law narrows from shared reason to sectarian authority.",
        "Theocracy does not mean that religion influences politics; it means "
        "that divine law or its authorised interpreters are the governing "
        "source of political authority, and secularism correspondingly does "
        "not require excluding every religious voice from public debate.",
        "Divine law supplies a moral limit on rulers and prevents the state "
        "from becoming the highest source of value, which purely procedural "
        "politics cannot do by itself.",
        "Moral limits on state power are genuinely valuable, but they need not "
        "entail exclusive clerical or confessional sovereignty; entrenched "
        "constitutional rights limit power just as effectively while "
        "preserving equal citizenship across faiths and none.",
        "Theocracy may retain internal validity for believers who already "
        "accept its source of authority; what it cannot do is satisfy the "
        "tests of consent, equal citizenship, public reason and revisability "
        "that a plural modern society applies to any general form of "
        "government.",
        "Name the criterion of validity before judging, state the strongest "
        "case for divine limitation of rulers, apply the interpretation-"
        "monopoly objection, use the constitutional guarantee of religious "
        "freedom as a dated illustration, and close with a criterion verdict.",
        [
            "Theocracy equals divine sovereignty plus sacred law plus clerical "
            "mediation, never mere public religiosity.",
            "Core defect: the interpretation monopoly, and the unequal "
            "citizenship that follows from it.",
            "Divine right makes monarchy theologically legitimated; theocracy "
            "makes theology politically constitutive.",
            "Articles 25 to 28 guarantee freedom of conscience and religion "
            "subject to public order, morality and health, and bar religious "
            "instruction in wholly State-funded institutions.",
            "2019 Q1(b), 2022 Q4(c) and 2025 Q4(b) are all decided by the "
            "sovereignty distinction, not by attitude to religion.",
        ],
        [
            visual(
                "Three things that are constantly confused with theocracy",
                "Most avoidable marks on theocracy stems are lost by treating "
                "any religiously coloured politics as theocratic.",
                "+-----------------------------+------------------------------------+",
                "| ARRANGEMENT                 | WHERE SOVEREIGNTY ACTUALLY SITS    |",
                "+-----------------------------+------------------------------------+",
                "| religious citizens arguing  | with the people; religion enters   |",
                "| in public debate            | as one voice among many            |",
                "| a secular state engaging    | with the people; the state relates |",
                "| religion by reform or       | to faiths on terms of equal        |",
                "| accommodation               | citizenship                        |",
                "| divine-right monarchy       | with the king, theologically       |",
                "|                             | legitimated but personally held    |",
                "| THEOCRACY                   | with GOD, exercised through sacred |",
                "|                             | law and clerical interpreters      |",
                "+-----------------------------+------------------------------------+",
            ),
            visual(
                "The validity test applied to theocracy",
                "Fixing the test before applying it is the mark-bearing move "
                "in every can-it-be-accepted stem.",
                "   NAME THE TEST -> consent | equal citizenship | public reason |",
                "                    revisability | accountability",
                "            |",
                "            v",
                "   CASE FOR: moral unity, collective purpose, restraint on purely",
                "             self-interested politics, a stable ethical order",
                "            |",
                "            v",
                "   CASE AGAINST: no equal standing for other faiths or none;",
                "             conscience compromised; dissent becomes impiety;",
                "             clerical interpretation becomes a monopoly",
                "            |",
                "            v",
                "   VERDICT -> internally valid for believers; as a GENERAL form in a",
                "              plural modern society it fails every named test.",
            ),
        ],
    ),
    session(
        "Democracy: Direct, Representative, Procedural, Substantive and Deliberative",
        "Democracy means rule of the people, but in modern political "
        "philosophy it implies far more than counting votes: political "
        "equality, consent, participation, accountability, public "
        "justification and some protection of rights against the very majority "
        "that wins.",
        "The models divide along three axes — direct participation against "
        "representation, procedural fairness of authorisation against the "
        "substantive social conditions of equal freedom, and aggregation of "
        "preferences against deliberative justification — while liberal "
        "democracy combines popular rule with constitutional limits, rights, "
        "rule of law and minority protection so that the majority governs "
        "without converting number into unrestricted power.",
        "Democracy is not simply periodic election: its distinctive claim is "
        "that rule is equally authorised, publicly justified and peacefully "
        "replaceable, so a regime that keeps elections while dismantling those "
        "conditions retains the form and loses the substance.",
        [
            "direct against representative democracy",
            "procedural against substantive democracy",
            "liberal democracy and constitutional limits",
            "participatory and deliberative democracy",
            "minority protection and equal moral standing",
            "political equality against social inequality",
        ],
        "Distinguish the direct, representative, procedural, substantive, "
        "participatory and deliberative models before evaluating anything, "
        "define liberal democracy as popular rule under constitutional limits, "
        "test minority protection against both formal guarantee and social "
        "prejudice, and close on political equality against social "
        "inequality.",
        "Elections authorise rulers, but authorisation is worth having only "
        "where rights, independent adjudication and a real opposition keep the "
        "losing side able to become the winning side, which is why "
        "constitutional limits are internal to democracy rather than external "
        "constraints upon it.",
        "A polity may therefore hold regular elections and remain deeply "
        "unequal, exclusionary or manipulated, which is exactly the condition "
        "the substantive conception was designed to detect.",
        "Democracy is not merely periodic election and majority rule is not "
        "unlimited, so distinguish electoral, liberal, participatory, "
        "deliberative and substantive democracy, and never treat a majority's "
        "victory as proof that minority standing has been respected.",
        "Liberal democracies proclaim minority protection but deliver it "
        "unevenly, since social prejudice outlasts formal equality and "
        "electoral incentives reward majoritarian rhetoric.",
        "The reply concedes the record and shifts to the mechanism: legal "
        "guarantees, representation, judicial review, protected dissent and "
        "constitutional accommodation give minorities instruments no rival "
        "form supplies, so the gap between norm and practice is a demand for "
        "institutional repair rather than an argument against the norm.",
        "Normative commitment does not guarantee delivery, because "
        "substantive inclusion depends on constitutional culture, social "
        "equality and institutional independence, none of which a formal "
        "design can manufacture by itself.",
        "Name which model of democracy the stem is testing, define liberal "
        "democracy as popular rule under constitutional limits, run "
        "achievements against limits on minority protection, add Ambedkar's "
        "warning about political equality amid social and economic "
        "inequality, and close with a graded verdict.",
        [
            "Direct against representative; procedural against substantive; "
            "aggregative against deliberative.",
            "Liberal democracy: popular rule plus rights plus rule of law plus "
            "judicial review plus minority protection.",
            "Participatory democracy is defended developmentally, echoing "
            "Mill on the improvement of public character.",
            "Habermas: legitimacy grows where laws emerge from public "
            "reasoning approximating freedom, reciprocity and absence of "
            "domination.",
            "Epistemic defence: democratic procedures allow error-detection, "
            "revision and access to dispersed social knowledge.",
        ],
        [
            visual(
                "Three axes that generate every model of democracy",
                "Naming the axis the stem is testing prevents the commonest "
                "failure, which is answering about elections when the question "
                "is about social conditions.",
                "   AXIS 1  DIRECT  <----------------------->  REPRESENTATIVE",
                "           citizens decide themselves        citizens elect rulers",
                "           visible self-rule, hard to scale  workable, but distant",
                "",
                "   AXIS 2  PROCEDURAL  <------------------->  SUBSTANTIVE",
                "           are rulers chosen fairly?         do people actually govern",
                "           elections, competition, rules     under fair social conditions?",
                "",
                "   AXIS 3  AGGREGATIVE  <------------------>  DELIBERATIVE",
                "           count the preferences             justify the norms publicly",
                "           majority decides                  reasons must be shareable",
            ),
            visual(
                "Minority protection: what liberal democracy delivers and what it misses",
                "The 2018 and 2020 stems both require this two-column "
                "judgement rather than a one-sided verdict.",
                "+-------------------------------------+-------------------------------+",
                "| ACHIEVEMENTS                        | LIMITS                        |",
                "+-------------------------------------+-------------------------------+",
                "| legal guarantees and representation | social prejudice outlasts     |",
                "|                                     | formal equality               |",
                "| judicial review and civil liberties | electoral incentives reward   |",
                "|                                     | majoritarian rhetoric         |",
                "| protected dissent, association and  | minorities tolerated formally |",
                "| expression                          | yet excluded substantively    |",
                "| constitutional accommodation of     | delivery depends on           |",
                "| language, religion and culture      | constitutional culture        |",
                "+-------------------------------------+-------------------------------+",
                "   AMBEDKAR -> political equality cannot long survive amid deep",
                "               social and economic inequality.",
            ),
        ],
    ),
    session(
        "Authority and Legitimacy: Weber, Schumpeter and Michels",
        "Classifying who rules never explains why rule is obeyed, so this "
        "module adds the sociology of legitimate authority: Weber's three "
        "grounds of believed rightfulness, Schumpeter's redefinition of "
        "democracy as competition for votes, and Michels's claim that "
        "organisation itself breeds oligarchy.",
        "Weber distinguishes power, the ability to secure compliance despite "
        "resistance, from authority, power regarded as rightful, and "
        "identifies traditional, charismatic and legal-rational types with "
        "their own administrations and characteristic crises; Schumpeter "
        "defines democracy as the institutional arrangement in which "
        "individuals acquire the power to decide by a competitive struggle for "
        "the people's vote; Michels, in Political Parties of 1911, argues an "
        "iron law of oligarchy by which scale, specialisation and control of "
        "information entrench a permanent leadership.",
        "Classification by number of rulers tells us who decides, while "
        "classification by type of legitimacy tells us why they are obeyed, "
        "and a complete assessment of monarchy, theocracy or democracy "
        "requires both grids laid over each other.",
        [
            "power against authority",
            "traditional, charismatic and legal-rational types",
            "ideal type and routinisation of charisma",
            "competitive struggle for the people's vote",
            "democratic elitism as a minimum condition",
            "iron law of oligarchy",
        ],
        "Separate power from authority at the outset, run the three types with "
        "their administrations and succession problems, show that the typology "
        "cuts across the classical classification, use Schumpeter to fix the "
        "procedural pole of the dispute, and bring in the iron law of "
        "oligarchy only where internal democracy or representation is at "
        "issue.",
        "No regime can rest on coercion alone because surveillance costs rise "
        "without limit, so stability requires belief in rightfulness, and "
        "beliefs of that kind take only a few forms, each generating its own "
        "administrative apparatus and its own crisis.",
        "Charismatic authority dies with its bearer and must routinise into "
        "traditional or legal-rational form to survive, which explains the "
        "movement from movement to party to bureaucracy and answers succession "
        "and stability stems directly.",
        "Legitimacy in Weber is a sociological fact about belief and never a "
        "normative verdict, so do not treat legitimate as equivalent to "
        "justified; that equation is the commonest misuse of the typology in "
        "an examination answer.",
        "The three types are ideal types and no real regime is pure, so the "
        "typology appears to explain nothing determinate, while defining "
        "legitimacy as belief lets propaganda-induced acceptance count as "
        "legitimate.",
        "Weber constructs the types explicitly as analytical exaggerations "
        "against which real mixtures are measured, so their value is "
        "diagnostic: they identify which mixture a regime is and which of its "
        "sources of legitimacy is eroding.",
        "The belief-based definition genuinely does admit manufactured "
        "acceptance, which is why a normative theory of legitimacy resting on "
        "consent, accountability and contestability must supplement Weber "
        "rather than replace him.",
        "Introduce the second grid explicitly, place the stem's form on both "
        "the classical and the legitimacy classification, deploy routinisation "
        "for succession and stability stems, oppose the procedural minimum to "
        "the substantive conception, and close with the cross-typology "
        "verdict.",
        [
            "Traditional: immemorial custom, patrimonial staff, succession by "
            "inheritance — monarchy and hereditary theocracy.",
            "Charismatic: devotion to an exceptional leader, no career "
            "structure, an acute succession crisis.",
            "Legal-rational: belief in enacted rules, administered by "
            "bureaucracy — the modern constitutional state, whatever its form.",
            "Schumpeter: the people's function is to produce a government, not "
            "to govern.",
            "Michels: who says organisation says oligarchy, though the "
            "defensible version is a resistible tendency rather than a law.",
        ],
        [
            visual(
                "Three pure types of legitimate authority and their crises",
                "The typology is the strongest cross-cutting tool in this "
                "clause because it applies to all three named forms at once.",
                "+------------------+---------------------+----------------------+",
                "| TYPE             | GROUND OF BELIEF    | SUCCESSION PROBLEM   |",
                "+------------------+---------------------+----------------------+",
                "| TRADITIONAL      | sanctity of         | solved by            |",
                "|                  | immemorial custom   | inheritance, custom  |",
                "| CHARISMATIC      | devotion to an      | acute; the type is   |",
                "|                  | exceptional leader  | inherently unstable  |",
                "| LEGAL-RATIONAL   | legality of enacted | solved impersonally  |",
                "|                  | rules; bureaucracy  | by rule              |",
                "+------------------+---------------------+----------------------+",
                "   CROSSING -> monarchy is traditional; theocracy joins traditional to",
                "               charismatic; democracy is legal-rational yet capturable.",
            ),
            visual(
                "Two deflationary challenges to rule by the people",
                "Both challenges concede the democratic form and attack the "
                "claim that the people actually rule.",
                "   SCHUMPETER                       MICHELS",
                "   no determinate common good       organisation needs continuity,",
                "   and no stable popular will       expertise and control of files",
                "            |                                   |",
                "            v                                   v",
                "   define democracy by METHOD:      a full-time leadership becomes",
                "   competitive struggle for the     irreplaceable and acquires its",
                "   people's vote                    own interest in staying",
                "            |                                   |",
                "            v                                   v",
                "   the people PRODUCE a            IRON LAW OF OLIGARCHY inside",
                "   government; they do not govern   avowedly democratic bodies",
                "            |                                   |",
                "            +---------------> REPLY <-----------+",
                "   competition is a minimum, not a ceiling; oligarchic drift is a",
                "   resistible tendency, alterable by rules on terms and transparency.",
            ),
        ],
    ),
    session(
        "Populism, Illiberal Democracy and Propaganda",
        "This module explains how a regime can keep every democratic form and "
        "lose the substance: a leader claims to embody the real people, the "
        "institutions that check a majority are recast as elite obstructions, "
        "and consent is manufactured while elections continue to be held.",
        "Mudde treats populism as a thin-centred ideology dividing society "
        "into a pure people and a corrupt elite and therefore attaching itself "
        "to a host ideology; Muller locates the decisive feature in the claim "
        "to exclusive moral representation, which makes anti-pluralism rather "
        "than anti-elitism the danger; Laclau treats populism instead as a "
        "logic of articulation binding unsatisfied demands into a collective "
        "subject called the people; illiberal democracy names the resulting "
        "state in which majority rule survives while the constitutional "
        "conditions of the next contest are hollowed out.",
        "Anti-elitism is ordinary democratic politics and is entirely "
        "compatible with democracy, whereas anti-pluralism, the claim that "
        "only one side represents the real people, is not, and that is the "
        "line on which any judgement of democratic decay should turn.",
        [
            "thin-centred ideology and host ideology",
            "pure people against corrupt elite",
            "exclusive moral representation",
            "logic of articulation",
            "illiberal democracy and the form-substance grid",
            "manufactured consent and the regulator's dilemma",
        ],
        "Name the contest between the thin-centred, the exclusive-"
        "representation and the articulation accounts instead of presenting "
        "one settled definition, adopt the anti-pluralism criterion with "
        "reasons, run the form-substance grid across elections, courts, press "
        "and opposition, and end propaganda stems on the regulator's dilemma "
        "rather than on a demand for censorship.",
        "A real representation deficit lets a leader articulate excluded "
        "demands and claim to embody the people, and because the people is "
        "then defined morally rather than procedurally, disagreement becomes "
        "betrayal and the institutions that check majority will are weakened "
        "while elections continue.",
        "The outcome satisfies majority rule while dismantling the entrenched "
        "rights, independent adjudication and secured conditions of the next "
        "contest that make electoral defeat survivable for a minority.",
        "Do not use populism as a label for any mass challenge, and do not "
        "answer a propaganda stem by demanding regulation of false content, "
        "because every content-based remedy hands the state the very power "
        "over public truth that a propagandising state abuses.",
        "The analysis protects unelected institutions against democratic "
        "majorities and looks itself anti-democratic, while the word populist "
        "is a smear that incumbents apply to any disruptive mass challenge.",
        "The reply to the first charge is temporal: constitutional limits "
        "protect the conditions of future majorities, including the losing "
        "side's ability to become a majority, so a majority that removes them "
        "abolishes the mechanism by which it could itself later be replaced. "
        "The reply to the second is that the exclusive-representation "
        "criterion applies without regard to a movement's programme.",
        "The grid is diagnostic rather than empirical: it states what would "
        "have to be shown and by what evidence, and it certifies nothing about "
        "any actual country, party, leader or period.",
        "Open by stating the definitional contest, adopt a criterion with "
        "reasons, run the form-substance grid, reconstruct the slide as "
        "numbered steps, state the regulator's dilemma with its structural "
        "remedies, and answer contemporary invitations at the level of "
        "criteria rather than by naming actors.",
        [
            "Mudde 2004: a thin-centred ideology of pure people against "
            "corrupt elite, attaching to a host ideology.",
            "Muller 2016: exclusive moral representation, so anti-pluralism "
            "rather than anti-elitism is decisive.",
            "Laclau 2005: populism as a logic of articulation — state the "
            "contest, then adopt a position with reasons.",
            "Article 19(1)(a) guarantees free speech subject to reasonable "
            "restrictions under Article 19(2); the Representation of the "
            "People Act, 1951 governs the conduct of elections.",
            "Structural remedies only: plural ownership, transparent political "
            "finance, independent electoral adjudication, protected "
            "journalism, civic education and rights of reply.",
        ],
        [
            visual(
                "The slide from representation deficit to illiberal democracy",
                "Reconstructing the slide as numbered steps is what turns a "
                "list of complaints into a philosophical argument.",
                "   [1] a genuine representation deficit exists",
                "            |",
                "   [2] a leader articulates the excluded demands and claims to",
                "       embody the real people",
                "            |",
                "   [3] the people is defined MORALLY, so disagreement becomes betrayal",
                "            |",
                "   [4] courts, second chambers, commissions, press and federal units",
                "       are recast as elite obstructions",
                "            |",
                "   [5] they are weakened, captured or bypassed -- elections continue",
                "            |",
                "            v",
                "   [6] ILLIBERAL DEMOCRACY: an electoral majority governs without the",
                "       constraints that make defeat survivable for a minority",
            ),
            visual(
                "Form retained, substance eroded",
                "The grid is the fastest way to show that held elections do "
                "not settle whether a state is democratic.",
                "+---------------------------+----------------------------------------+",
                "| DEMOCRATIC FORM RETAINED  | SUBSTANTIVE CONDITION ERODED           |",
                "+---------------------------+----------------------------------------+",
                "| elections continue        | fairness of contest: access, finance,  |",
                "|                           | media, adjudication of disputes        |",
                "| a majority governs        | limits on what a majority may do to    |",
                "|                           | minorities                             |",
                "| courts function           | independence of appointment, tenure    |",
                "|                           | and enforcement                        |",
                "| a press exists            | plurality of ownership, absence of     |",
                "|                           | indirect pressure                      |",
                "| opposition parties exist  | realistic prospect of alternation      |",
                "+---------------------------+----------------------------------------+",
            ),
        ],
    ),
    session(
        "Institutional and Territorial Design: Unitary, Federal and Decentralised",
        "Alongside the question of who rules there is a second design axis "
        "that the classical labels miss, and it is the question of where power "
        "sits territorially and how far down it is pushed towards the people "
        "who live under it.",
        "A unitary system vests authority in one central government whose "
        "sub-units exercise delegated powers it may withdraw, while a federal "
        "system constitutionally divides powers between centre and units, each "
        "with a guaranteed sphere, stabilised by bicameralism, a judicial "
        "umpire over the centre-unit boundary and fiscal and intergovernmental "
        "machinery; federations are coming-together or holding-together, and a "
        "federation with one indissoluble sovereignty differs from a "
        "confederation of sovereign members who may leave.",
        "A complete modern account of forms of government runs two axes rather "
        "than one: who rules and by what title, and where power sits "
        "territorially and how far down it is pushed under the principle that "
        "decisions belong at the lowest capable level.",
        [
            "unitary against federal division of powers",
            "coming-together and holding-together federation",
            "federation against confederation",
            "bicameralism and the judicial umpire",
            "decentralisation and subsidiarity",
            "local self-government and village self-rule",
        ],
        "Introduce the territorial axis as clearly labelled comparative "
        "scaffolding, contrast delegated powers with a constitutional division "
        "of powers, name the coming-together and holding-together varieties, "
        "distinguish a federation from a confederation, and run "
        "decentralisation down to local self-government before adjudicating.",
        "Federalism buys autonomy, diversity-management and a check on central "
        "overreach at the price of coordination costs and possible deadlock, "
        "while unitary design buys uniformity and decisiveness at the price of "
        "remoteness from those governed.",
        "India is accordingly described as a parliamentary, holding-together "
        "federal republic with unitary features, operating under "
        "constitutional supremacy with judicial review rather than "
        "parliamentary sovereignty.",
        "This axis is standard comparative political theory rather than "
        "canonical doctrine of the Philosophy clause, so label it as "
        "scaffolding, do not present it as owned philosophical doctrine, and "
        "never describe India as parliamentary-sovereign when it rests on "
        "constitutional supremacy.",
        "Territorial design is institutional detail belonging to comparative "
        "government, and importing it turns a philosophy answer into a "
        "politics fact sheet.",
        "The axis earns its place only where it does philosophical work: it "
        "shows that limits on power are territorial as well as legal, that "
        "self-rule can be graded by proximity, and that Gandhi's decentralised "
        "ideal of self-reliant village republics is a normative claim about "
        "where political life ought to be lived.",
        "The scaffolding must stay subordinate, because no monarchy, theocracy "
        "or democracy stem is answered by federal machinery alone, and the "
        "doctrinal core of the clause remains the source, purpose and limits "
        "of authority.",
        "Use this axis only where the stem concerns design, decentralisation "
        "or the location of power, label it as comparative context, run the "
        "unitary and federal contrast on named criteria, add the subsidiarity "
        "ladder, and return promptly to the doctrinal verdict.",
        [
            "Unitary: delegated, withdrawable powers. Federal: "
            "constitutionally divided spheres with a judicial umpire.",
            "Coming-together federation unites independent states; "
            "holding-together federation devolves to hold diversity.",
            "Confederation: sovereign members, exit possible, weak centre — "
            "not a federation.",
            "Article 40 directs the State to organise village panchayats as "
            "units of self-government; the 73rd and 74th Constitutional "
            "Amendment Acts, 1992 added Parts IX and IX-A.",
            "Subsidiarity ladder: centre, state, district, then local "
            "self-government, with Gandhi's village self-rule (swaraj) at the "
            "base.",
        ],
        [
            visual(
                "Where power sits: the unitary and federal poles",
                "The stabilisers in the middle are what make a federal "
                "division of powers workable rather than merely declared.",
                "   UNITARY  <------------------------------------------>  FEDERAL",
                "   one central government;              constitutional DIVISION of",
                "   sub-units exercise DELEGATED         powers between centre and",
                "   powers it may withdraw               units, each with a guaranteed",
                "                                        sphere",
                "   uniformity and decisiveness,         autonomy, diversity-management",
                "   at the price of remoteness           and a check on central",
                "                                        overreach, at the price of",
                "                                        coordination cost and deadlock",
                "            STABILISERS -> bicameralism, a chamber for the units",
                "                        -> a judicial umpire over the boundary",
                "                        -> fiscal and intergovernmental machinery",
            ),
            visual(
                "The decentralisation ladder and the principle beneath it",
                "Subsidiarity converts a description of tiers into a normative "
                "argument about where self-rule should actually happen.",
                "   SUBSIDIARITY -> decide at the LOWEST capable level",
                "",
                "   CENTRE  ->  STATE / PROVINCE  ->  DISTRICT  ->  LOCAL",
                "                                                   SELF-GOVERNMENT",
                "                                                   (panchayats and",
                "                                                    municipalities)",
                "",
                "   VARIETIES -> COMING-TOGETHER: independent states unite",
                "             -> HOLDING-TOGETHER: one polity devolves to hold diversity",
                "             -> FEDERATION (one indissoluble sovereignty) against",
                "                CONFEDERATION (sovereign members, exit possible)",
                "",
                "   GANDHI -> village self-rule (swaraj): self-reliant, participatory",
                "             village republics as the base of the pyramid.",
            ),
        ],
    ),
    session(
        "Mixed and Constitutional Government: Criteria and the Comparative Verdict",
        "No pure form survives contact with reality, so modern constitutional "
        "government is a deliberate mixture in which legislature, executive "
        "and judiciary check one another under a supreme law, and any form is "
        "judged by scoring it on several criteria at once.",
        "Constitutionalism combines separation of powers, the rule of law, "
        "entrenched rights and a defined amendment procedure so that the "
        "constitution both authorises and limits every organ; the comparative "
        "evaluation then runs monarchy, theocracy and democracy down the same "
        "axes of source of authority, type of legitimacy claimed, mode of "
        "succession or selection, accountability, relation to law, treatment "
        "of dissent, equality of citizenship and capacity to correct error.",
        "Democracy's superiority is not that it guarantees wise decisions; it "
        "lies in equal standing, public justification and the institutionalised "
        "correction of error, and that is the axis on which the comparison of "
        "monarchy, theocracy and democracy finally turns.",
        [
            "mixed government and checks and balances",
            "separation of powers and rule of law",
            "constitutionalism under a supreme law",
            "shared axes of comparison",
            "error-correction and peaceful transfer",
            "graded verdict rather than a winner",
        ],
        "State that pure types are textbook fictions, set out the "
        "constitutional machinery of separated powers under a supreme law, fix "
        "five or six shared axes of comparison and run all three forms down "
        "each of them, and let error-correction and peaceful transfer carry "
        "the graded verdict.",
        "Because each organ authorises and limits the others under a supreme "
        "law, no holder of public power can be judge in its own cause, and the "
        "same design supplies the mechanism by which the regime corrects its "
        "own mistakes.",
        "No form excels on every axis, so a defensible conclusion concedes "
        "decisiveness and continuity to monarchy and moral limitation of "
        "rulers to theocracy while awarding equal standing, public "
        "justification and peaceful replacement to constitutional democracy.",
        "Never write three disconnected mini-essays on monarchy, theocracy and "
        "democracy; run shared axes in parallel, and do not omit "
        "error-correction, which most often decides the verdict and is the "
        "axis candidates most often forget.",
        "Scoring regimes on a list of axes looks like a marking exercise "
        "rather than philosophy, and the choice of axes silently decides the "
        "result before any argument is made.",
        "The choice of axes is itself argued rather than assumed, because each "
        "axis names a distinct way in which public power can go wrong — "
        "arbitrariness, exclusion, unaccountability and irreversibility — so "
        "defending the list is part of the argument and leaves the verdict "
        "contestable in the open.",
        "The comparison stays conditional throughout: a constitutional "
        "democracy that loses fair contest, protected minorities, independent "
        "adjudication and realistic alternation keeps the form while "
        "forfeiting precisely what made the form worth having.",
        "Announce the axes before comparing, run all three forms down each "
        "axis in parallel, place both the classical and the legitimacy grids "
        "on the table, deliver a graded verdict that concedes something to the "
        "losing side, and end on error-correction and peaceful transfer.",
        [
            "Pillars: separation of powers, rule of law, constitutionalism, "
            "entrenched rights.",
            "Axes: legitimacy, liberty, equality, participation, "
            "accountability, stability, efficiency, responsiveness, inclusion, "
            "peaceful transfer.",
            "Directive decoder: comment on, discuss, critically examine, can X "
            "be accepted, does X leave room for Y, how far, compare.",
            "Verdict formulas: asymmetric, distinctiveness, criterion, "
            "form-and-substance, cross-typology and dilemma.",
            "Closing thesis: equal standing, public justification and "
            "institutionalised correction of error.",
        ],
        [
            visual(
                "The constitutional machine that no pure form contains",
                "Checks and balances are what make a mixture defensible rather "
                "than merely untidy.",
                "                    +------------------------+",
                "                    |    THE CONSTITUTION    |  supreme law, rights,",
                "                    +-----------+------------+  amendment procedure",
                "                                | limits and authorises",
                "        +-----------------------+-----------------------+",
                "        v                       v                       v",
                "   LEGISLATURE   <--->     EXECUTIVE     <--->     JUDICIARY",
                "   makes law               enforces law            interprets law,",
                "   scrutiny, purse         answerable to the       judicial review",
                "        ^                  legislature or                 ^",
                "        |                  separately elected             |",
                "        +----------- each checks the others --------------+",
                "   PILLARS -> separation of powers, rule of law, constitutionalism,",
                "              entrenched rights.",
            ),
            visual(
                "The comparative verdict, run down shared axes",
                "Running the axes in parallel is the difference between a "
                "comparison and three mini-essays.",
                "+---------------------+--------------+--------------+--------------+",
                "| AXIS                | MONARCHY     | THEOCRACY    | DEMOCRACY    |",
                "+---------------------+--------------+--------------+--------------+",
                "| source of authority | heredity     | revelation   | consent      |",
                "| legitimacy type     | traditional  | traditional  | legal-       |",
                "|                     |              | plus charisma| rational     |",
                "| selection           | birth        | clerical     | election     |",
                "|                     |              | designation  |              |",
                "| accountability      | customary    | to God, read | electoral,   |",
                "|                     | and weak     | by clergy    | legal, moral |",
                "| dissent             | disloyalty   | impiety      | legitimate   |",
                "| error-correction    | counsel only | doctrinal    | opposition,  |",
                "|                     |              | revision     | courts, vote |",
                "+---------------------+--------------+--------------+--------------+",
            ),
        ],
    ),
)


ASCII_PANELS = (
    {
        "title": "The central question of regime classification and its four axes",
        "structural_type": "root-question-and-classification-axes",
        "sessions": [1],
        "lines": [
            "CENTRAL QUESTION -> by what title may one arrangement of rule bind everyone in a",
            "                    territory, and on what grounds may that arrangement be judged?",
            "        |",
            "        v",
            "FOUR AXES, NEVER ONE",
            "  (1) WHO RULES?            one  |  few  |  many",
            "  (2) FOR WHOSE GOOD?       common good  <-->  private or sectional interest",
            "  (3) BY WHAT TITLE?        heredity | conquest | divine sanction |",
            "                            consent and election | sacred law",
            "  (4) UNDER WHAT LIMITS?    law? rights? accountability? none at all?",
            "        |",
            "  +-----+-----------------------+-----------------------------+",
            "  v                             v                             v",
            "MONARCHY                     THEOCRACY                     DEMOCRACY",
            "rule of one; title is        rule in the name of God;      rule of the people;",
            "heredity, tradition and      title is revelation and       title is consent,",
            "sometimes divine right       sacred law read by clergy     equality, participation",
            "  |                             |                             |",
            "  v                             v                             v",
            "danger: arbitrariness,       danger: conscience crushed,   danger: majoritarianism,",
            "unaccountability, a weak     citizenship made unequal,     manipulated opinion,",
            "basis in equality            dissent read as impiety       mediocrity, propaganda",
            "        |",
            "        v",
            "DESCRIPTIVE map (what a regime IS)  vs  NORMATIVE verdict (whether it OUGHT to bind)",
            "CONTROL -> separate the four axes first, fix description or evaluation second,",
            "           adjudicate last on a criterion you have already named.",
        ],
    },
    {
        "title": "Plato: the degeneration sequence and the three charges against democracy",
        "structural_type": "degeneration-sequence-with-critique",
        "sessions": [2],
        "lines": [
            "ROOT CLAIM -> ruling is a CRAFT requiring KNOWLEDGE of justice and the good",
            "        |",
            "        v",
            "SHIP OF STATE -> navigation is not handed to the unskilled because they are many",
            "        |",
            "        v",
            "DEGENERATION OF CONSTITUTIONS (Republic): each dominant value corrupts into the next",
            "  ARISTOCRACY OF KNOWLEDGE -- wisdom rules",
            "        |  honour displaces wisdom",
            "        v",
            "  TIMOCRACY -- honour and military spiritedness",
            "        |  the desire for wealth displaces honour",
            "        v",
            "  OLIGARCHY -- property and wealth; rich divided from poor",
            "        |  the poor many overthrow the propertied few",
            "        v",
            "  DEMOCRACY -- freedom and equality of desires",
            "        |  unrestrained licence makes restraint itself look oppressive",
            "        v",
            "  TYRANNY -- one demagogue who flatters the many, then dominates them",
            "        |",
            "        v",
            "THREE CHARGES -> [1] ruling is a craft, so numbers confer no competence",
            "              -> [2] democracy mistakes LIBERTY for QUALIFICATION",
            "              -> [3] unregulated liberty breeds the demagogue, hence tyranny",
            "TRAP -> this is NOT a defence of hereditary monarchy and NOT mere hatred of freedom",
            "VERDICT (asymmetric) -> the diagnosis of demagoguery and defective leadership-",
            "  selection survives; the guardian remedy fails for want of consent and correction.",
        ],
    },
    {
        "title": "Aristotle's six-fold matrix and the polity as the practicable mean",
        "structural_type": "six-fold-classification-matrix",
        "sessions": [3],
        "lines": [
            "TWO VARIABLES -> [A] HOW MANY RULE    [B] FOR WHOSE ADVANTAGE",
            "+---------------+------------------------------+-----------------------------+",
            "| NUMBER RULING | RIGHT FORM (common good)     | DEVIATION (private gain)    |",
            "+---------------+------------------------------+-----------------------------+",
            "| ONE           | MONARCHY                     | TYRANNY                     |",
            "| FEW           | ARISTOCRACY                  | OLIGARCHY                   |",
            "| MANY          | POLITY                       | DEMOCRACY (classical sense) |",
            "+---------------+------------------------------+-----------------------------+",
            "        |",
            "        v",
            "KEY -> the right and corrupt version of each number differ in PURPOSE, not in SIZE;",
            "       the good-MANY form is POLITY, and classical democracy is its DEVIATION",
            "        |",
            "        v",
            "POLITY = mixed constitution -> rule of the many UNDER LAW, moderated by property,",
            "         virtue, civic participation and a broad MIDDLE CLASS",
            "  against STATISM       -> value is not absorbed into one all-wise ruler or state",
            "  against INDIVIDUALISM -> politics is not unrestricted private self-assertion",
            "  for CIVIC MODERATION  -> citizenship inside a lawful order aimed at common good",
            "        |",
            "        v",
            "PLATO asks WHO OUGHT IDEALLY TO RULE   |  ARISTOTLE asks WHICH CONSTITUTION CAN",
            "                                       |  SUSTAIN good political life in practice",
            "LIMIT -> common advantage is not self-specifying and needs an independent theory of",
            "         the good; the stability of polity is a sociological claim, not a proof.",
            "TRAP -> polity is a mixed-government precursor, NOT universal-suffrage democracy.",
        ],
    },
    {
        "title": "Monarchy: two types, four objections and the above-politics test",
        "structural_type": "monarchy-type-comparison-and-freedom-verdict",
        "sessions": [4],
        "lines": [
            "DEFINITION -> rule by ONE person, normally holding office by HEREDITY",
            "        |",
            "  +-----+-------------------------------------+",
            "  v                                           v",
            "ABSOLUTE MONARCHY                          CONSTITUTIONAL MONARCHY",
            "executive, legislative and sometimes       the monarch REIGNS while elected",
            "judicial power concentrated in one         institutions GOVERN",
            "title: heredity, conquest, tradition,      historic continuity plus legal",
            "       DIVINE RIGHT OF KINGS               limitation by convention",
            "accountability: weak, unsecured            accountability: cabinet, parliament",
            "verdict: efficient, normatively risky      verdict: acceptable as symbolic head",
            "        |",
            "        v",
            "FOUR OBJECTIONS TO HEREDITARY RULE AS A PRINCIPLE",
            "  EQUALITY       -> public authority should be open to all on equal terms",
            "  MERIT          -> birth guarantees neither wisdom nor virtue",
            "  ACCOUNTABILITY -> concentrated power invites arbitrariness and despotism",
            "  FREEDOM        -> liberty needs law, rights and institutions, not a crown",
            "        |",
            "        v",
            "THE ABOVE-POLITICS TEST",
            "  above PARTY CONFLICT -> systematic: the role is fixed by convention and the",
            "                          elected institutions retain governance",
            "  above CONSTITUTIONAL ACCOUNTABILITY -> not systematic: the order ceases to be",
            "                          constitutional and slides toward arbitrary rule",
            "        |",
            "        v",
            "DIVINE RIGHT -> the king rules by God's will and answers primarily to God: a BRIDGE",
            "                between monarchy and theocracy, never an identity of the two",
            "VERDICT -> monarchy coexists with individual freedom only where CONSTITUTIONALISED;",
            "           as a principle of rule it does not by itself ground freedom.",
        ],
    },
    {
        "title": "Theocracy: divine sovereignty, the interpretation monopoly and validity",
        "structural_type": "problem-response-validity-ledger",
        "sessions": [5],
        "lines": [
            "DEFINITION -> political authority claimed in the name of GOD, of divine law, or of",
            "              the authorised interpreters of sacred truth",
            "NOT the same as -> a society merely INFLUENCED by religion, or a morally informed",
            "                   polity in which believers argue publicly as equal citizens",
            "        |",
            "        v",
            "FIVE STRUCTURAL FEATURES",
            "  SOVEREIGNTY OF GOD  -> final authority is divine will, not the people",
            "  SACRED LAW          -> religious law guides or determines civil law",
            "  CLERICAL MEDIATION  -> priests, jurists and elites interpret divine command",
            "  LIMITED PLURALISM   -> dissent is constrained as theological deviance",
            "  FUSION              -> political and religious legitimacy overlap",
            "        |",
            "        v",
            "CASE FOR                              |  CASE AGAINST",
            "moral unity and collective purpose    |  no equal standing for other faiths or none",
            "restraint on self-interested politics |  liberty of conscience is compromised",
            "a stable ethical order derived from   |  dissent becomes impiety, not disagreement",
            "sacred obligation                     |  interpretation becomes a clerical MONOPOLY",
            "a higher law above human rulers       |  adaptation to rights discourse is hard",
            "        |",
            "        v",
            "THE DECISIVE PROBLEM -> WHO SPEAKS FOR GOD? once interpretation is human,",
            "  theological certainty can mask ordinary struggles for power",
            "SECULARISM -> the state is not founded on the supremacy of one religious truth for",
            "  all; it protects equal citizenship, liberty of conscience and coexistence",
            "  (India: Articles 25-28 guarantee freedom of conscience and religion subject to",
            "   public order, morality and health, and bar religious instruction in wholly",
            "   State-funded institutions -- dated legal facts, not proof of a thesis)",
            "VERDICT -> internally valid for believers; as a GENERAL form of government in a",
            "           plural modern society it fails consent, equal citizenship and revision.",
        ],
    },
    {
        "title": "Democracy: the model taxonomy and the protection of minorities",
        "structural_type": "democracy-model-taxonomy-and-minority-protection",
        "sessions": [6],
        "lines": [
            "DEFINITION -> rule of the people: political equality, consent, participation,",
            "              accountability, public justification and protection of rights",
            "        |",
            "  +-----+-----------+---------------------+--------------------+",
            "  v                 v                     v                    v",
            "DIRECT          REPRESENTATIVE        PROCEDURAL           SUBSTANTIVE",
            "citizens        citizens elect        are rulers chosen    do people actually",
            "decide          rulers and            fairly? elections,   govern under fair",
            "themselves      lawmakers             competition, rules   social conditions?",
            "high            workable at scale;                         justice, rights,",
            "participation   power stands apart                         real equality",
            "        |",
            "        v",
            "LIBERAL DEMOCRACY = popular rule + constitutional limits + rights + rule of law",
            "  -> the majority governs WITHOUT converting number into unrestricted power",
            "        |",
            "  +-----+------------------------------+",
            "  v                                    v",
            "ACHIEVEMENTS                        LIMITS",
            "legal guarantees, representation    social prejudice outlasts formal equality",
            "judicial review, civil liberties    incentives reward majoritarian rhetoric",
            "protected dissent and association   formal tolerance, substantive exclusion",
            "constitutional accommodation        delivery rests on constitutional culture",
            "        |",
            "        v",
            "DEEPENING MODELS -> PARTICIPATORY: participation educates citizens and resists",
            "                    alienation, echoing Mill on public character",
            "                 -> DELIBERATIVE: Habermas grounds legitimacy in public reasoning",
            "                    under freedom, reciprocity and absence of domination",
            "                 -> EPISTEMIC: procedures allow error-detection and revision",
            "INDIA ANCHOR -> Ambedkar warns that political equality cannot long survive amid",
            "                deep social and economic inequality.",
        ],
    },
    {
        "title": "Authority and legitimacy: the Weberian grid laid across the classical one",
        "structural_type": "authority-typology-comparison",
        "sessions": [7],
        "lines": [
            "POWER = compliance secured despite resistance | AUTHORITY = power believed RIGHTFUL",
            "+------------------+----------------------+----------------------+---------------+",
            "| TYPE             | GROUND OF BELIEF     | ADMINISTRATION       | SUCCESSION    |",
            "+------------------+----------------------+----------------------+---------------+",
            "| TRADITIONAL      | sanctity of          | personal retainers,  | inheritance   |",
            "|                  | immemorial custom    | patrimonial staff    | or custom     |",
            "| CHARISMATIC      | devotion to an       | disciples chosen     | acute; the    |",
            "|                  | exceptional leader   | personally, no rules | type is frail |",
            "| LEGAL-RATIONAL   | legality of enacted  | BUREAUCRACY: office, | impersonal,   |",
            "|                  | rules                | files, career        | by rule       |",
            "+------------------+----------------------+----------------------+---------------+",
            "        |",
            "        v",
            "THE TYPOLOGY CUTS ACROSS THE CLASSICAL GRID",
            "  monarchy   -> traditional, occasionally charismatic",
            "  theocracy  -> traditional joined to charismatic",
            "  democracy  -> normally legal-rational, yet capturable by plebiscitary charisma",
            "ROUTINISATION OF CHARISMA -> movement becomes party becomes bureaucracy",
            "        |",
            "        v",
            "SCHUMPETER -> democracy is the COMPETITIVE STRUGGLE FOR THE PEOPLE'S VOTE; the",
            "  people's function is to PRODUCE A GOVERNMENT, not to govern (procedural pole)",
            "MICHELS, Political Parties (1911) -> IRON LAW OF OLIGARCHY: scale, specialisation",
            "  and control of information entrench a permanent leadership",
            "TRAP -> Weberian legitimacy is a SOCIOLOGICAL fact about belief, never a normative",
            "        certificate of justification; ideal types are yardsticks, not portraits",
            "VERDICT -> number of rulers tells us WHO decides; type of legitimacy tells us WHY",
            "           they are obeyed, and a complete assessment requires both grids.",
        ],
    },
    {
        "title": "Populism, illiberal democracy and the manufacture of consent",
        "structural_type": "causal-process-of-democratic-erosion",
        "sessions": [8],
        "lines": [
            "DEFINITIONAL CONTEST -> state it, never settle it silently",
            "  MUDDE (2004)  -> populism as a THIN-CENTRED ideology: a pure people against a",
            "                   corrupt elite, attaching to a HOST ideology across the spectrum",
            "  MULLER (2016) -> the decisive move is EXCLUSIVE MORAL REPRESENTATION: rivals are",
            "                   not opponents but enemies of the people (ANTI-PLURALISM)",
            "  LACLAU (2005) -> populism as a LOGIC OF ARTICULATION binding unsatisfied demands",
            "                   into a collective subject called the people",
            "        |",
            "        v",
            "THE SLIDE, STEP BY STEP",
            "  [1] a genuine representation deficit exists",
            "  [2] a leader articulates the excluded demands and claims to embody the people",
            "  [3] the people is defined MORALLY, so disagreement becomes betrayal",
            "  [4] courts, chambers, commissions, press and federal units become obstructions",
            "  [5] they are weakened, captured or bypassed while elections continue",
            "  [6] result -> ILLIBERAL DEMOCRACY",
            "        v",
            "FORM RETAINED             |  SUBSTANCE ERODED",
            "elections continue        |  fairness of contest: access, finance, media, disputes",
            "a majority governs        |  limits on what a majority may do to minorities",
            "courts function           |  independence of appointment, tenure and enforcement",
            "a press exists            |  plurality of ownership, absence of indirect pressure",
            "opposition parties exist  |  a realistic prospect of alternation in power",
            "        v",
            "PROPAGANDA -> a judgment is the citizen's own only under access to information,",
            "  rival argument and freedom from manipulation; otherwise consent is MANUFACTURED",
            "  and a vote confers sociological legitimacy without normative authorisation",
            "REGULATOR'S DILEMMA -> content-based remedies hand the state power over public",
            "  truth, the very power a propagandising state abuses",
            "STRUCTURAL REMEDIES -> plural ownership, transparent political finance, independent",
            "  electoral adjudication, protected journalism, civic education, rights of reply",
            "CAUTION -> a diagnostic grid only; no country, party, leader or period is judged.",
        ],
    },
    {
        "title": "Where power sits: unitary against federal design and subsidiarity",
        "structural_type": "territorial-cross-section-of-public-power",
        "sessions": [9],
        "lines": [
            "SECOND AXIS (comparative scaffolding, clearly labelled -- not owned doctrine)",
            "WHO RULES is one question; WHERE POWER SITS and HOW FAR DOWN it goes is another",
            "        |",
            "UNITARY  <--------------------------------------------------------->  FEDERAL",
            "one central government;                    a constitutional DIVISION of powers",
            "sub-units exercise DELEGATED               between centre and units, each with",
            "powers it may withdraw                     a guaranteed sphere",
            "uniformity and decisiveness,               autonomy, diversity-management and a",
            "at the price of remoteness                 check on central overreach, at the",
            "                                           price of coordination and deadlock",
            "        |",
            "        +--------------- STABILISERS --------------+",
            "                    bicameralism: a chamber for the units",
            "                    a JUDICIAL UMPIRE over the centre-unit boundary",
            "                    fiscal and intergovernmental machinery",
            "        v",
            "VARIETIES -> COMING-TOGETHER federation: independent states unite",
            "          -> HOLDING-TOGETHER federation: one polity devolves to hold diversity",
            "          -> FEDERATION (one indissoluble sovereignty) against CONFEDERATION",
            "             (sovereign members, exit possible, weak centre)",
            "        v",
            "SUBSIDIARITY -> decide at the LOWEST capable level",
            "CENTRE -> STATE / PROVINCE -> DISTRICT -> LOCAL SELF-GOVERNMENT",
            "                                          (panchayats and municipalities)",
            "INDIA (dated legal facts) -> Article 40 directs the State to organise village",
            "  panchayats as units of self-government; the 73rd and 74th Constitutional",
            "  Amendment Acts, 1992 added Parts IX and IX-A. India is a parliamentary,",
            "  holding-together federal republic under CONSTITUTIONAL SUPREMACY with judicial",
            "  review -- never parliamentary sovereignty",
            "GANDHI -> village self-rule (swaraj): self-reliant, participatory village republics",
            "CONTROL -> keep the axis subordinate and return to source, purpose and limits.",
        ],
    },
    {
        "title": "The answer spine: shared axes, directive decoder and the graded verdict",
        "structural_type": "integrated-answer-spine",
        "sessions": [10],
        "lines": [
            "STEP 1 DEFINE   -> name the form by its SOURCE OF AUTHORITY, not by a caricature",
            "STEP 2 LOCATE   -> place the stem on the classical grid AND the legitimacy grid",
            "STEP 3 RIVALS   -> stage ONE real debate, never three disconnected mini-essays",
            "STEP 4 OBJECT   -> voice the strongest objection to your own thesis, then reply",
            "STEP 5 EVIDENCE -> one unit at 10 marks, two at 15, four or five at 20",
            "STEP 6 VERDICT  -> graded, conceding something to the losing side",
            "        v",
            "RUN ALL THREE FORMS DOWN THE SAME AXES",
            "  source of authority | type of legitimacy claimed | succession or selection",
            "  accountability | relation to law | treatment of dissent | equal citizenship",
            "  CAPACITY TO CORRECT ERROR  <- the axis that usually decides and is usually left out",
            "        v",
            "DIRECTIVE DECODER -- the verb fixes the structure",
            "  Comment on               -> claim, argument, one objection, verdict",
            "  Discuss                  -> doctrine, rival, objection, reply, verdict",
            "  Critically examine       -> two objections, each with reply and residual problem",
            "  Can X be accepted?       -> NAME THE TEST first, apply it, then judge",
            "  Does X leave room for Y? -> what X entails, what Y requires, can they co-exist",
            "  How far is X distinctive -> a degree judgment plus a distinctiveness test",
            "        |",
            "        v",
            "VERDICT FORMULAS (adapt, never reproduce mechanically)",
            "  ASYMMETRIC     -> the diagnosis survives, the remedy does not",
            "  CRITERION      -> by consent and equal citizenship, theocratic sovereignty fails",
            "  FORM/SUBSTANCE -> the form is kept; the conditions worth having are not",
            "  CROSS-TYPOLOGY -> who decides, plus why they are obeyed",
            "  DILEMMA        -> answer propaganda by contestable institutions, not censorship",
            "        |",
            "        v",
            "CLOSING THESIS -> democracy's superiority is not guaranteed wisdom; it is equal",
            "  standing, public justification and institutionalised correction of error.",
        ],
    },
)

ASCII_PANELS = (
    *ASCII_PANELS,
    {
        "title": "Institutional form axes inside constitutional government",
        "structural_type": "three-axis institutional matrix",
        "sessions": [6, 9, 10],
        "lines": [
            "PARLIAMENTARY -> executive-legislative fusion plus collective responsibility",
            "PRESIDENTIAL -> separate mandate, fixed tenure and stronger separation",
            "TRADE-OFF -> removability and coordination versus stability and deadlock",
            "UNITARY -> sub-unit powers are delegated and legally withdrawable",
            "FEDERAL -> centre and units hold constitutionally divided competences",
            "FUSION/SEPARATION -> coordination must coexist with checks and review",
            "DECENTRALISATION -> subsidiarity, local knowledge and participation",
            "CONTROL -> no institutional axis by itself proves democratic legitimacy",
        ],
    },
    {
        "title": "Non-democratic regime families and the six democratic pathologies",
        "structural_type": "regime-spectrum-and-pathology-grid",
        "sessions": [7, 8, 10],
        "lines": [
            "DICTATORSHIP -> concentrated rule without regular competitive accountability",
            "AUTHORITARIANISM -> restricted pluralism, opposition and public discussion",
            "TOTALITARIANISM -> comprehensive ideology, mobilisation and party-state penetration",
            "PATHOLOGIES -> majority tyranny | elite capture | instability/short-termism",
            "              populist anti-pluralism | propaganda | bureaucratic domination",
            "COUNTERWEIGHTS -> rights | opposition | review | plural media | transparency",
            "                   decentralisation | realistic alternation in power",
            "VERDICT -> democracy's strength is corrigibility, not immunity from error",
        ],
    },
)


GRAPHICAL_PILLS = (
    [
        {"text": "MONARCHY, THEOCRACY, DEMOCRACY", "role": "primary"},
        {"text": "WHO RULES, BY WHAT TITLE", "role": "mechanism"},
        {"text": "FOR WHOSE GOOD, UNDER WHAT LIMITS", "role": "evidence"},
        {"text": "HEREDITY, REVELATION, CONSENT", "role": "comparison"},
        {"text": "DESCRIPTION BEFORE EVALUATION", "role": "outcome"},
        {"text": "NO FORM WINS ON EVERY AXIS", "role": "caution"},
    ],
    [
        {"text": "RULING IS A CRAFT OF KNOWLEDGE", "role": "primary"},
        {"text": "SHIP OF STATE NEEDS A NAVIGATOR", "role": "mechanism"},
        {"text": "TIMOCRACY, OLIGARCHY, DEMOCRACY, TYRANNY", "role": "evidence"},
        {"text": "LIBERTY IS NOT QUALIFICATION", "role": "comparison"},
        {"text": "DIAGNOSIS SURVIVES, REMEDY FAILS", "role": "outcome"},
        {"text": "NOT A DEFENCE OF HEREDITARY RULE", "role": "caution"},
    ],
    [
        {"text": "NUMBER TIMES END SERVED", "role": "primary"},
        {"text": "PURPOSE, NOT SIZE, DIVIDES THE FORMS", "role": "mechanism"},
        {"text": "MONARCHY, ARISTOCRACY, POLITY", "role": "evidence"},
        {"text": "TYRANNY, OLIGARCHY, DEVIANT DEMOCRACY", "role": "comparison"},
        {"text": "POLITY IS THE MIDDLE COURSE", "role": "outcome"},
        {"text": "POLITY IS NOT MODERN DEMOCRACY", "role": "caution"},
    ],
    [
        {"text": "ABSOLUTE AGAINST CONSTITUTIONAL", "role": "primary"},
        {"text": "HEREDITY SETTLES RULE WITHOUT MERIT", "role": "mechanism"},
        {"text": "EQUALITY, MERIT, ACCOUNTABILITY, FREEDOM", "role": "evidence"},
        {"text": "DIVINE RIGHT BRIDGES TO THEOCRACY", "role": "comparison"},
        {"text": "REIGNS BUT DOES NOT GOVERN", "role": "outcome"},
        {"text": "ABOVE PARTY, NEVER ABOVE THE LAW", "role": "caution"},
    ],
    [
        {"text": "SOVEREIGNTY OF GOD, NOT THE PEOPLE", "role": "primary"},
        {"text": "SACRED LAW AND CLERICAL MEDIATION", "role": "mechanism"},
        {"text": "WHO SPEAKS FOR GOD", "role": "evidence"},
        {"text": "SECULARISM PROTECTS EQUAL CITIZENSHIP", "role": "comparison"},
        {"text": "FAILS CONSENT AND REVISABILITY", "role": "outcome"},
        {"text": "NOT EVERY RELIGIOUS POLITICS IS THEOCRACY", "role": "caution"},
    ],
    [
        {"text": "RULE OF THE PEOPLE, NOT MERE VOTING", "role": "primary"},
        {"text": "DIRECT, REPRESENTATIVE, PROCEDURAL", "role": "mechanism"},
        {"text": "SUBSTANTIVE, PARTICIPATORY, DELIBERATIVE", "role": "evidence"},
        {"text": "LIBERAL DEMOCRACY LIMITS THE MAJORITY", "role": "comparison"},
        {"text": "EQUAL AUTHORISATION AND PEACEFUL CHANGE", "role": "outcome"},
        {"text": "ELECTIONS DO NOT PROVE INCLUSION", "role": "caution"},
    ],
    [
        {"text": "POWER AGAINST AUTHORITY", "role": "primary"},
        {"text": "TRADITIONAL, CHARISMATIC, LEGAL-RATIONAL", "role": "mechanism"},
        {"text": "ROUTINISATION OF CHARISMA", "role": "evidence"},
        {"text": "COMPETITIVE STRUGGLE FOR THE VOTE", "role": "comparison"},
        {"text": "IRON LAW OF OLIGARCHY", "role": "outcome"},
        {"text": "LEGITIMATE IS NOT JUSTIFIED", "role": "caution"},
    ],
    [
        {"text": "PURE PEOPLE AGAINST CORRUPT ELITE", "role": "primary"},
        {"text": "EXCLUSIVE MORAL REPRESENTATION", "role": "mechanism"},
        {"text": "THIN-CENTRED IDEOLOGY, HOST IDEOLOGY", "role": "evidence"},
        {"text": "LOGIC OF ARTICULATION", "role": "comparison"},
        {"text": "FORM RETAINED, SUBSTANCE ERODED", "role": "outcome"},
        {"text": "REGULATOR'S DILEMMA, NOT CENSORSHIP", "role": "caution"},
    ],
    [
        {"text": "WHERE POWER SITS TERRITORIALLY", "role": "primary"},
        {"text": "DELEGATED AGAINST DIVIDED POWERS", "role": "mechanism"},
        {"text": "BICAMERALISM AND A JUDICIAL UMPIRE", "role": "evidence"},
        {"text": "COMING-TOGETHER, HOLDING-TOGETHER", "role": "comparison"},
        {"text": "SUBSIDIARITY AND VILLAGE SELF-RULE", "role": "outcome"},
        {"text": "CONSTITUTIONAL, NOT PARLIAMENTARY, SUPREMACY", "role": "caution"},
    ],
    [
        {"text": "DEFINE, LOCATE, RIVALS, OBJECT, VERDICT", "role": "primary"},
        {"text": "SEPARATION OF POWERS UNDER SUPREME LAW", "role": "mechanism"},
        {"text": "SHARED AXES RUN IN PARALLEL", "role": "evidence"},
        {"text": "CLASSICAL GRID PLUS LEGITIMACY GRID", "role": "comparison"},
        {"text": "ERROR-CORRECTION AND PEACEFUL TRANSFER", "role": "outcome"},
        {"text": "NEVER THREE DISCONNECTED MINI-ESSAYS", "role": "caution"},
    ],
)


GRAPHICAL_STAGE_ZERO_GROUPS = [
    {
        "heading": "FOUR QUESTIONS INSIDE ONE LABEL",
        "role": "evidence",
        "items": [
            "Who rules — one, few or many — is only the first of the four "
            "questions a regime label compresses.",
            "For whose good rule is exercised separates the right form of any "
            "number from its deviation.",
            "By what title and under what limits decide whether the "
            "arrangement can claim obedience at all.",
        ],
    },
    {
        "heading": "THREE FORMS, THREE TITLES TO RULE",
        "role": "mechanism",
        "items": [
            "Monarchy claims heredity, conquest and tradition, and sometimes "
            "the divine right of kings.",
            "Theocracy claims revelation and sacred law, read through clerical "
            "interpreters.",
            "Democracy claims consent, political equality, participation and "
            "representation.",
        ],
    },
    {
        "heading": "DESCRIPTION BEFORE EVALUATION",
        "role": "outcome",
        "items": [
            "A descriptive classification records what a regime is; a "
            "normative verdict judges whether it ought to bind anyone.",
            "Each form carries its own standing danger: arbitrariness, "
            "crushed conscience, or manipulated majorities.",
            "Separate the axes first, fix the register second, and adjudicate "
            "last on a criterion already named.",
        ],
    },
]


GRAPHICAL_STAGE_GROUPS = (
    GRAPHICAL_STAGE_ZERO_GROUPS,
    [
        {
            "heading": "THE ROOT CLAIM AND ITS IMAGE",
            "role": "evidence",
            "items": [
                "Ruling is a craft that requires knowledge of justice and the "
                "good, not a status that numbers can confer.",
                "The ship-of-state analogy holds that navigation is not handed "
                "to the unskilled merely because they are many.",
                "Plato therefore rejects the assumption that all opinions are "
                "politically equal in competence.",
            ],
        },
        {
            "heading": "THE DEGENERATION SEQUENCE",
            "role": "mechanism",
            "items": [
                "Timocracy prizes honour until the desire for wealth displaces "
                "it, and oligarchy divides rich from poor.",
                "Democracy prizes freedom and equality of desires until "
                "restraint itself begins to look oppressive.",
                "Out of that licence emerges the demagogue who flatters the "
                "many, attacks elites and seizes absolute power.",
            ],
        },
        {
            "heading": "THREE CHARGES AND THE VERDICT",
            "role": "outcome",
            "items": [
                "The charges are that ruling is a craft, that liberty is "
                "mistaken for qualification, and that licence breeds tyranny.",
                "This is not a defence of hereditary monarchy and not a simple "
                "hatred of freedom.",
                "Asymmetric verdict: the diagnosis of demagoguery survives "
                "while the unaccountable guardian remedy does not.",
            ],
        },
    ],
    [
        {
            "heading": "TWO VARIABLES, SIX FORMS",
            "role": "evidence",
            "items": [
                "Number of rulers — one, few, many — is crossed with rule for "
                "the common or the private advantage.",
                "Right forms are monarchy, aristocracy and polity; deviations "
                "are tyranny, oligarchy and classical democracy.",
                "The right and corrupt version of each number differ in "
                "purpose rather than in size.",
            ],
        },
        {
            "heading": "POLITY AS THE PRACTICABLE MEAN",
            "role": "mechanism",
            "items": [
                "Polity is the mixed constitution: rule of the many under law, "
                "moderated by property, virtue and civic participation.",
                "A broad middle class makes lawful moderation self-sustaining "
                "where extremes of wealth and poverty breed faction.",
                "Against statism it refuses the all-wise ruler; against "
                "individualism it refuses unrestricted self-assertion.",
            ],
        },
        {
            "heading": "LIMIT AND COMPARATIVE USE",
            "role": "outcome",
            "items": [
                "Common advantage is not self-specifying and requires an "
                "independent theory of the human good.",
                "The stability of polity is a sociological judgement, not a "
                "demonstration that polity is just.",
                "Plato asks who ought ideally to rule; Aristotle asks which "
                "constitution sustains good political life in practice.",
            ],
        },
    ],
    [
        {
            "heading": "TWO KINDS OF MONARCHY",
            "role": "evidence",
            "items": [
                "Absolute monarchy concentrates executive, legislative and "
                "sometimes judicial power in one hereditary ruler.",
                "Constitutional monarchy keeps the crown as a ceremonial "
                "office while cabinet and parliament actually govern.",
                "Divine right sacralises kingship and makes the monarch "
                "answerable primarily to God rather than to the people.",
            ],
        },
        {
            "heading": "FOUR OBJECTIONS TO HEREDITARY RULE",
            "role": "mechanism",
            "items": [
                "Equality: public authority should be open to all on equal "
                "terms rather than settled by birth.",
                "Merit and accountability: birth guarantees no wisdom, and "
                "concentrated power invites arbitrariness.",
                "Freedom: liberty in the modern sense needs law, rights and "
                "equal citizenship, none of which heredity supplies.",
            ],
        },
        {
            "heading": "THE ABOVE-POLITICS TEST",
            "role": "outcome",
            "items": [
                "Above party conflict is systematic, because the role is fixed "
                "by convention while elected institutions govern.",
                "Above constitutional accountability is not systematic, "
                "because the order then slides toward arbitrary rule.",
                "Verdict: monarchy coexists with freedom only where it has "
                "been constitutionalised and politically limited.",
            ],
        },
    ],
    [
        {
            "heading": "WHAT MAKES A REGIME THEOCRATIC",
            "role": "evidence",
            "items": [
                "Sovereignty is claimed for God rather than the people, and "
                "sacred law guides or determines civil law.",
                "Clerical mediation gives priests, jurists and religious "
                "elites the authority to interpret divine command.",
                "Pluralism is limited because dissent appears as theological "
                "deviance rather than legitimate disagreement.",
            ],
        },
        {
            "heading": "THE CASE FOR AND THE DECISIVE PROBLEM",
            "role": "mechanism",
            "items": [
                "The case for theocracy is moral unity, restraint on "
                "self-interested politics and a higher law above rulers.",
                "The decisive problem is who speaks for God: once "
                "interpretation is human, certainty can mask power struggles.",
                "Interpretation then becomes a monopoly immunised from "
                "ordinary criticism.",
            ],
        },
        {
            "heading": "SECULARISM AND THE VALIDITY VERDICT",
            "role": "outcome",
            "items": [
                "Secularism asks that the state not rest on the supremacy of "
                "one religious truth for all citizens.",
                "Articles 25 to 28 guarantee freedom of conscience and "
                "religion subject to public order, morality and health.",
                "Verdict: internally valid for believers, but as a general "
                "form it fails consent, equal citizenship and revisability.",
            ],
        },
    ],
    [
        {
            "heading": "THE MODEL TAXONOMY",
            "role": "evidence",
            "items": [
                "Direct democracy has citizens decide themselves; "
                "representative democracy has them elect rulers and lawmakers.",
                "Procedural democracy asks whether rulers are chosen fairly; "
                "substantive democracy asks about real social conditions.",
                "Liberal democracy adds constitutional limits, rights, rule of "
                "law and protection for minorities.",
            ],
        },
        {
            "heading": "DEEPENING THE MODEL",
            "role": "mechanism",
            "items": [
                "Participatory democracy is defended developmentally, because "
                "participation educates citizens and resists alienation.",
                "Deliberative democracy grounds legitimacy in public reasoning "
                "under freedom, reciprocity and absence of domination.",
                "The epistemic defence claims that democratic procedures allow "
                "error-detection, revision and dispersed knowledge.",
            ],
        },
        {
            "heading": "MINORITIES: ACHIEVEMENT AND LIMIT",
            "role": "outcome",
            "items": [
                "Achievements: legal guarantees, representation, judicial "
                "review, protected dissent and constitutional accommodation.",
                "Limits: social prejudice outlasts formal equality and "
                "electoral incentives reward majoritarian rhetoric.",
                "Ambedkar warns that political equality cannot long survive "
                "amid deep social and economic inequality.",
            ],
        },
    ],
    [
        {
            "heading": "POWER, AUTHORITY AND THREE PURE TYPES",
            "role": "evidence",
            "items": [
                "Power secures compliance despite resistance; authority is "
                "power regarded as rightful by those subject to it.",
                "Traditional authority rests on immemorial custom, "
                "charismatic on devotion to an exceptional leader.",
                "Legal-rational authority rests on enacted rules and is "
                "administered through bureaucracy.",
            ],
        },
        {
            "heading": "WHY THE TYPOLOGY CUTS ACROSS THE GRID",
            "role": "mechanism",
            "items": [
                "Monarchy is normally traditional, theocracy joins traditional "
                "to charismatic, democracy is normally legal-rational.",
                "Routinisation converts charisma into traditional or "
                "legal-rational form, or the authority dies with its bearer.",
                "A democracy can retain legal forms while being captured by a "
                "plebiscitary charismatic leader.",
            ],
        },
        {
            "heading": "TWO DEFLATIONARY CHALLENGES",
            "role": "outcome",
            "items": [
                "Schumpeter defines democracy as the competitive struggle for "
                "the people's vote, so the people produce a government.",
                "Michels argues in Political Parties of 1911 that scale and "
                "control of information entrench a permanent leadership.",
                "Caution: Weberian legitimacy is belief, never a normative "
                "certificate of justification.",
            ],
        },
    ],
    [
        {
            "heading": "THREE ACCOUNTS OF POPULISM",
            "role": "evidence",
            "items": [
                "Mudde in 2004 treats populism as a thin-centred ideology "
                "opposing a pure people to a corrupt elite.",
                "Muller in 2016 locates the danger in the claim to exclusive "
                "moral representation, which is anti-pluralism.",
                "Laclau in 2005 treats populism as a logic of articulation "
                "binding unsatisfied demands into a collective subject.",
            ],
        },
        {
            "heading": "HOW THE SLIDE ACTUALLY WORKS",
            "role": "mechanism",
            "items": [
                "A representation deficit lets a leader claim to embody the "
                "real people, so disagreement becomes betrayal.",
                "Courts, second chambers, commissions, the press and federal "
                "units are recast as elite obstructions and weakened.",
                "Elections continue while the constitutional conditions of the "
                "next contest are hollowed out.",
            ],
        },
        {
            "heading": "PROPAGANDA AND THE REGULATOR'S DILEMMA",
            "role": "outcome",
            "items": [
                "Consent formed without access, rival argument and freedom "
                "from manipulation is manufactured rather than given.",
                "Content-based remedies hand the state power over public "
                "truth, the very power a propagandising state abuses.",
                "Defensible remedies are structural: plural ownership, "
                "transparent finance, independent adjudication, civic "
                "education.",
            ],
        },
    ],
    [
        {
            "heading": "THE TERRITORIAL AXIS",
            "role": "evidence",
            "items": [
                "A unitary system delegates powers to sub-units and may "
                "withdraw them at will.",
                "A federal system divides powers constitutionally, giving each "
                "level a guaranteed sphere of competence.",
                "Federations come together from independent states or hold "
                "together a single polity that devolves to manage diversity.",
            ],
        },
        {
            "heading": "WHAT MAKES DIVISION WORKABLE",
            "role": "mechanism",
            "items": [
                "Bicameralism gives the units a chamber of their own inside "
                "the central legislature.",
                "A judicial umpire adjudicates the centre-unit boundary, and "
                "fiscal machinery makes autonomy real.",
                "A federation holds one indissoluble sovereignty, whereas a "
                "confederation leaves members sovereign and free to exit.",
            ],
        },
        {
            "heading": "SUBSIDIARITY AND SELF-RULE",
            "role": "outcome",
            "items": [
                "Subsidiarity requires that decisions be taken at the lowest "
                "level capable of taking them well.",
                "Article 40 directs the State to organise village panchayats "
                "as units of self-government, and the 73rd and 74th "
                "Constitutional Amendment Acts, 1992 added Parts IX and IX-A.",
                "Gandhi's ideal of village self-rule places self-reliant "
                "participatory village republics at the base of the pyramid.",
            ],
        },
    ],
    [
        {
            "heading": "THE CONSTITUTIONAL MIXTURE",
            "role": "evidence",
            "items": [
                "Legislature, executive and judiciary check one another under "
                "a constitution that both authorises and limits them.",
                "The pillars are separation of powers, rule of law, "
                "constitutionalism and entrenched rights.",
                "No holder of public power can be judge in its own cause, "
                "which is what makes error-correction possible.",
            ],
        },
        {
            "heading": "THE SHARED AXES OF COMPARISON",
            "role": "mechanism",
            "items": [
                "Source of authority, type of legitimacy claimed, and mode of "
                "succession or selection.",
                "Accountability, relation to law, treatment of dissent and "
                "equality of citizenship.",
                "Capacity to correct error, the axis that most often decides "
                "and is most often omitted.",
            ],
        },
        {
            "heading": "THE GRADED VERDICT",
            "role": "outcome",
            "items": [
                "Concede decisiveness and continuity to monarchy, and moral "
                "limitation of rulers to theocracy.",
                "Award equal standing, public justification and peaceful "
                "replacement to constitutional democracy.",
                "The verdict stays conditional: a democracy that loses fair "
                "contest and independent adjudication keeps only the form.",
            ],
        },
    ],
)


GRAPHICAL_STAGE_SEQUENCES = (
    [
        "Who rules: one, few or many",
        "For whose good: common or sectional",
        "By what title: heredity, revelation, consent",
        "Under what limits: law, rights, accountability",
        "Description first, then the normative verdict",
    ],
    [
        "Ruling is a craft that requires knowledge",
        "Timocracy: honour displaces wisdom",
        "Oligarchy: wealth divides rich from poor",
        "Democracy: freedom becomes licence",
        "Tyranny: the demagogue completes the fall",
    ],
    [
        "Cross number of rulers with end served",
        "Right forms: monarchy, aristocracy, polity",
        "Deviations: tyranny, oligarchy, democracy",
        "Polity mixes under law with a middle class",
        "Verdict: the practicable mean, not modern democracy",
    ],
    [
        "Fix the type: absolute or constitutional",
        "Heredity settles rule without any test of merit",
        "Four objections: equality, merit, accountability, freedom",
        "Divine right bridges monarchy to theocracy",
        "Freedom only where the crown is constitutionalised",
    ],
    [
        "Sovereignty is claimed for God, not the people",
        "Sacred law and clerical mediation follow",
        "Who speaks for God becomes the decisive problem",
        "Interpretation hardens into a monopoly",
        "Verdict by consent, equal citizenship and revisability",
    ],
    [
        "Name the model the stem is testing",
        "Direct and representative, procedural and substantive",
        "Liberal democracy limits what a majority may do",
        "Participation and deliberation deepen the model",
        "Minority protection judged on norm and delivery",
    ],
    [
        "Separate power from authority",
        "Traditional, charismatic and legal-rational grounds",
        "Charisma must routinise or die with its bearer",
        "Schumpeter reduces democracy to competitive selection",
        "Michels finds oligarchy inside democratic bodies",
    ],
    [
        "State the definitional contest before judging",
        "Anti-elitism is compatible with democracy",
        "Anti-pluralism claims exclusive moral representation",
        "Checking institutions are recast and weakened",
        "Form retained while substance is hollowed out",
    ],
    [
        "Add the territorial axis as labelled scaffolding",
        "Unitary delegation against federal division",
        "Bicameralism and a judicial umpire stabilise it",
        "Coming-together and holding-together varieties",
        "Subsidiarity carries power down to self-government",
    ],
    [
        "Define the form by its source of authority",
        "Locate it on the classical and legitimacy grids",
        "Stage one real debate, not three mini-essays",
        "Run every form down the same shared axes",
        "Close on error-correction and peaceful transfer",
    ],
)


GRAPHICAL_STAGE_MATRICES = (
    [],
    [],
    [
        ["NUMBER RULING", "RIGHT FORM (common good)", "DEVIATION (private gain)", "WHAT DIVIDES THEM"],
        [
            "ONE",
            "monarchy",
            "tyranny",
            "rule for the city or for the ruler",
        ],
        [
            "FEW",
            "aristocracy",
            "oligarchy",
            "excellence or mere wealth as the title",
        ],
        [
            "MANY",
            "polity",
            "democracy in the classical sense",
            "law-bound common good or the interest of the poor many",
        ],
    ],
    [
        ["AXIS", "ABSOLUTE MONARCHY", "CONSTITUTIONAL MONARCHY", "STANDING DANGER"],
        [
            "POWERS",
            "executive, legislative and sometimes judicial in one person",
            "the crown reigns while the cabinet governs",
            "concentration without a reviewable limit",
        ],
        [
            "TITLE",
            "heredity, conquest, tradition and divine right",
            "historic continuity bounded by convention and law",
            "birth substituted for qualification",
        ],
        [
            "ACCOUNTABILITY",
            "weak and institutionally unsecured",
            "shifted to cabinet and parliament",
            "succession failure and arbitrary rule",
        ],
        [
            "FREEDOM",
            "subjects are placed under personal rule",
            "civil liberties coexist with a symbolic crown",
            "inherited hierarchy and unequal civic status",
        ],
    ],
    [],
    [],
    [
        ["TYPE OF AUTHORITY", "GROUND OF BELIEF", "ADMINISTRATIVE FORM", "SUCCESSION PROBLEM"],
        [
            "TRADITIONAL",
            "sanctity of immemorial custom and of those who rule under it",
            "personal retainers and patrimonial household staff",
            "solved by inheritance or by custom",
        ],
        [
            "CHARISMATIC",
            "devotion to the exceptional character of one leader",
            "personally chosen disciples with no career structure",
            "acute, because the type is inherently unstable",
        ],
        [
            "LEGAL-RATIONAL",
            "belief in the legality of enacted rules",
            "bureaucracy with offices, jurisdictions, files and careers",
            "solved impersonally by rule",
        ],
    ],
    [],
    [],
    [],
)


REQUIRED_CORE_TERMS = (
    "forms of government",
    "monarchy",
    "theocracy",
    "democracy",
    "common good",
    "descriptive",
    "normative",
    "Plato",
    "Republic",
    "ship-of-state",
    "philosopher-ruler",
    "timocracy",
    "oligarchy",
    "tyranny",
    "demagogue",
    "Aristotle",
    "Politics",
    "aristocracy",
    "polity",
    "middle class",
    "statism",
    "individualism",
    "absolute monarchy",
    "constitutional monarchy",
    "hereditary",
    "Divine Right",
    "above politics",
    "sovereignty of God",
    "sacred law",
    "clerical",
    "secularism",
    "liberty of conscience",
    "equal citizenship",
    "Articles 25",
    "direct democracy",
    "representative democracy",
    "procedural",
    "substantive",
    "liberal democracy",
    "minority",
    "participatory democracy",
    "deliberative democracy",
    "Habermas",
    "Mill",
    "epistemic",
    "Ambedkar",
    "political equality",
    "popular sovereignty",
    "Weber",
    "authority",
    "traditional",
    "charismatic",
    "legal-rational",
    "ideal type",
    "routinisation",
    "bureaucracy",
    "Schumpeter",
    "competitive struggle",
    "Michels",
    "iron law of oligarchy",
    "Political Parties",
    "Mudde",
    "thin-centred",
    "exclusive moral representation",
    "anti-pluralism",
    "Laclau",
    "logic of articulation",
    "illiberal democracy",
    "propaganda",
    "manufactured",
    "regulator's dilemma",
    "Article 19",
    "reasonable restrictions",
    "Representation of the People Act",
    "unitary",
    "federal",
    "confederation",
    "holding-together",
    "coming-together",
    "bicameralism",
    "decentralisation",
    "subsidiarity",
    "panchayat",
    "Article 40",
    "73rd",
    "separation of powers",
    "rule of law",
    "constitutionalism",
    "judicial review",
    "checks and balances",
    "peaceful",
    "dictatorship",
    "authoritarianism",
    "totalitarianism",
    "parliamentary",
    "presidential",
    "fusion of powers",
    "majoritarian",
    "trustee",
    "delegate",
    "mandate",
    "Tocqueville",
    "Rousseau",
    "tyranny of the majority",
    "elite capture",
    "bureaucratic domination",
)

ADVANCED_SESSION_TITLES = tuple(
    str(spec["title"]) for spec in SESSION_SPECS
)

_SESSIONS = len(SESSION_SPECS)
if _SESSIONS != 10:
    raise ValueError(
        f"Forms of Government requires exactly 10 core sessions, found {_SESSIONS}."
    )
_PANELS = len(ASCII_PANELS)
if _PANELS != 12:
    raise ValueError(
        f"Forms of Government requires exactly 12 ASCII panels, found {_PANELS}."
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
    if generation != 5:
        raise ValueError(
            f"Forms of Government semantic successor is pinned to g5, got g{generation}."
        )

    text = re.sub(
        r"(?m)^!\[Forms of Government[^\]]*\]\([^)]+\)\s*\n+"
        r"\*Concept map:.*?\*\s*\n*",
        "",
        text,
        count=1,
    )

    boundary = _demote_owner(
        _extract_owner_section(
            owner_text,
            "## Exact ownership boundary and indispensable bridges",
            "## 0. ONE-SCREEN MAP",
        )
    )
    regimes = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 1.7 Constitutional and non-democratic regime families",
            "## 2. MONARCHY",
        )
    )
    institutional = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 4.2A Institutional and territorial design",
            "### 4.3 Procedural and substantive democracy",
        )
    )
    models = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 4.9 Majoritarian, representative, liberal, participatory and "
            "deliberative models",
            "## 4A. AUTHORITY, ELITE COMPETITION AND THE PATHOLOGIES OF DEMOCRACY",
        )
    )
    pathologies = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 4A.6 Six recurring democratic pathologies",
            "## 5. INTER-THINKER AND INTER-FORM DEBATES",
        )
    )

    text = text.replace(
        "- **Canonical doctrine source:** "
        "`upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/"
        "Forms-of-Government.md` (8,660 words), sliced verbatim into the CORE "
        "UPSC layers (each canonical teaching passage exactly once) and preserved "
        "again, in full, in the canonical apparatus block.",
        "- **Canonical doctrine source:** "
        "`upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/"
        "Forms-of-Government.md`, repaired under the ten-gate semantic-"
        "completeness protocol and promoted into this immutable successor.",
    )
    text = text.replace(
        "the classification problem (who rules, for whose good, under what design, "
        "with what limits; descriptive vs normative);",
        "the classification problem; constitutional/absolute, dictatorial, "
        "authoritarian and totalitarian regime families; parliamentary/"
        "presidential, unitary/federal and separation/fusion form-axes;",
    )
    text = text.replace(
        "- **Comparative-context discipline:** parliamentary vs presidential "
        "systems; unitary vs federal systems and confederation; centralisation vs "
        "decentralisation and local self-government; semi-presidential/cohabitation "
        "forms; and the criteria of evaluation are standard, verifiable political "
        "theory but are **not** part of this Philosophy owner's canonical doctrine "
        "(whose core is Monarchy, Theocracy, Democracy). They appear only in the "
        "authored scaffolding layers, always clearly labelled as comparative context "
        "beyond the syllabus core, never as fabricated canonical doctrine.",
        "- **Comparative-context discipline:** parliamentary/presidential, unitary/"
        "federal, separation/fusion, decentralisation and constitutional/absolute "
        "government are now bounded canonical form-axes because they execute the "
        "printed comparison problem; Polity retains all office, article, list, case "
        "and procedural detail.",
    )
    preservation = (
        "**Preservation note:** the canonical doctrine is reorganised into layers, "
        "never compressed. Every doctrine, numbered argument, objection/reply, "
        "comparison, corpus-depth delta, PYQ route, directive rule, graded verdict "
        "and provenance caution is retained; simplification means adding accessible "
        "gateways, not deleting complexity."
    )
    if "Exact ownership boundary and indispensable bridges" not in text:
        text = text.replace(preservation, preservation + "\n\n" + boundary, 1)

    if "1.7 Constitutional and non-democratic regime families" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Aristotle: The Six-Fold Classification "
            "and the Polity as Middle Course",
            regimes
            + "\n\n#### CLOSING RECALL FLOW — Aristotle: The Six-Fold "
            "Classification and the Polity as Middle Course",
            1,
        )
    if "4.2A Institutional and territorial design" not in text:
        text = text.replace(
            "#### 4.3 Procedural and substantive democracy",
            institutional + "\n\n#### 4.3 Procedural and substantive democracy",
            1,
        )
    if "4.9 Majoritarian, representative, liberal" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Democracy: Direct, Representative, "
            "Procedural, Substantive and Deliberative",
            models
            + "\n\n#### CLOSING RECALL FLOW — Democracy: Direct, Representative, "
            "Procedural, Substantive and Deliberative",
            1,
        )
    if "4A.6 Six recurring democratic pathologies" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Populism, Illiberal Democracy and Propaganda",
            pathologies
            + "\n\n#### CLOSING RECALL FLOW — Populism, Illiberal Democracy and "
            "Propaganda",
            1,
        )

    text = text.replace(
        "- Forms are AXES to run regimes down, not sealed boxes; real government "
        "is mixed.",
        "- Forms are AXES to run regimes down, not sealed boxes; real government "
        "is mixed.\n"
        "- Non-democratic families: dictatorship concentrates unaccountable rule; "
        "authoritarianism restricts pluralism; totalitarianism seeks comprehensive "
        "ideological penetration.",
        1,
    )
    text = text.replace(
        "- Models: direct/representative; procedural/substantive; liberal/"
        "participatory/\n  deliberative. Map before judging.",
        "- Models: direct/representative; procedural/substantive; majoritarian, "
        "liberal,\n  participatory and deliberative. Map before judging.\n"
        "- Representation: delegate, trustee and mandate models separate voter "
        "instruction,\n  representative judgment and programme authorisation.",
        1,
    )
    text = text.replace(
        "- Three pure types: traditional / charismatic / legal-rational -- ground "
        "of the belief\n  in rightfulness; legitimacy = sociological, not normative.",
        "- Three pure types: traditional / charismatic / legal-rational -- ground "
        "of the belief\n  in rightfulness; legitimacy = sociological, not normative.\n"
        "- Legal-rational administration risks bureaucratic domination unless "
        "reasons, oversight and correction remain available.",
        1,
    )
    text = text.replace(
        "- Regulator's dilemma: content-based remedies empower the state over public "
        "truth ->\n  use STRUCTURAL remedies + deliberation (F12).",
        "- Regulator's dilemma: content-based remedies empower the state over public "
        "truth ->\n  use STRUCTURAL remedies + deliberation (F12).\n"
        "- Six pathologies: majority tyranny, elite capture, instability/"
        "short-termism, populist anti-pluralism, propaganda and bureaucratic "
        "domination.",
        1,
    )
    text = text.replace(
        "- Real government is MIXED/constitutional: separation of powers + rule of "
        "law +\n  constitutionalism + rights + checks and balances.",
        "- Real government is MIXED/constitutional: separation of powers + rule of "
        "law +\n  constitutionalism + rights + checks and balances.\n"
        "- Parliamentary/presidential and unitary/federal axes distribute "
        "responsibility, tenure, competence and checks; none proves democracy alone.",
        1,
    )

    trap_row = (
        "| Expertise and democracy are opposites | the issue is the authorization "
        "and accountability of expertise |"
    )
    if "Dictatorship, authoritarianism and totalitarianism are synonyms" not in text:
        text = text.replace(
            trap_row,
            trap_row
            + "\n| Dictatorship, authoritarianism and totalitarianism are synonyms "
            "| distinguish concentrated rule, restricted plurality and "
            "comprehensive ideological penetration |"
            + "\n| Parliamentary means democratic and presidential means "
            "authoritarian | either institutional form needs independent democratic "
            "criteria |"
            + "\n| Federalism or decentralisation is democracy by itself | territorial "
            "distribution still needs rights, accountability and contestation |"
            + "\n| Separation of powers means no institutional interaction | "
            "differentiated competence operates through checks and coordination |"
            + "\n| Majority rule exhausts democracy | constitutional democracy adds "
            "minority rights, opposition and future alternation |"
            + "\n| Bureaucracy is merely neutral expertise | administration requires "
            "reasons, oversight and correction |",
            1,
        )
    text = text.replace(
        "**Promoted vocabulary (this pass) ⚠️:** power vs authority",
        "**Promoted vocabulary (this pass) ⚠️:** dictatorship · authoritarianism · "
        "totalitarianism · parliamentary/presidential · unitary/federal · "
        "fusion/separation of powers · majoritarian/representative/liberal democracy "
        "· trustee/delegate/mandate · tyranny of the majority · elite capture · "
        "bureaucratic domination · power vs authority",
        1,
    )

    if "F15 · Institutional form has independent trade-offs" not in text:
        text = text.replace(
            "- **F14 · Constitutional protection of religious freedom without "
            "establishment.**",
            "- **F15 · Institutional form has independent trade-offs.** "
            "Parliamentary/presidential, unitary/federal and fusion/separation axes "
            "distribute selection, tenure, competence and checks differently → "
            "Use: comparison and challenge stems → Limit: no axis proves democracy.\n"
            "- **F16 · Majority rule needs counterweights.** Tocqueville's "
            "tyranny-of-majority problem makes associations, local liberty, press, "
            "rights and review democratic safeguards → Use: minority/social-cohesion "
            "stems → Limit: counter-majoritarian bodies need accountability.\n"
            "- **F17 · Representative agency differs.** Delegate, trustee and mandate "
            "models assign different relations between judgment and voter instruction "
            "→ Use: direct/representative comparisons → Limit: none guarantees "
            "substantive representation.\n"
            "- **F18 · Non-democratic forms differ in reach.** Dictatorship "
            "concentrates decision; authoritarianism restricts contestation; "
            "totalitarianism seeks comprehensive mobilisation → Named: Linz/Arendt "
            "→ Limit: actual regimes are mixtures.\n"
            "- **F14 · Constitutional protection of religious freedom without "
            "establishment.**",
            1,
        )
    text = text.replace(
        "- O. P. Gauba, works on political theory and socio-political philosophy - "
        "monarchy,\n  theocracy, democracy and modern debates.",
        "- O. P. Gauba, *An Introduction to Political Theory*, searchable local PDF "
        "pp. 491–539.\n"
        "- *Socio-Political Philosophy*, local compiled notes PDF pp. 90–121; no "
        "named author is asserted.",
    )
    if "- Alexis de Tocqueville," not in text:
        text = text.replace(
            "- Max Weber, writings on power, authority and legitimacy - the "
            "traditional, charismatic and\n  legal-rational types and the "
            "routinisation of charisma. Cited by position, not by page or\n  "
            "verbatim wording.",
            "- Max Weber, writings on power, authority and legitimacy - the "
            "traditional, charismatic and\n  legal-rational types and the "
            "routinisation of charisma. Cited by position, not by page or\n  "
            "verbatim wording.\n"
            "- Alexis de Tocqueville, *Democracy in America* - tyranny of the "
            "majority, associations and local liberty.\n"
            "- J. S. Mill, *Considerations on Representative Government* - "
            "participation and public character.\n"
            "- Jean-Jacques Rousseau, *The Social Contract* - popular sovereignty "
            "and bounded criticism of representation.\n"
            "- Juan Linz, writings on authoritarian and totalitarian regimes; "
            "Hannah Arendt, *The Origins of Totalitarianism*.",
        )

    closure_replacements = {
        (
            "KEY TERMS / DEFINITIONS: who rules, by what title | common good "
            "against sectional interest | descriptive classification | normative "
            "verdict | source of legitimate authority | limits of law, rights and "
            "accountability"
        ): (
            "KEY TERMS / DEFINITIONS: rulers | title | common good | legitimacy | "
            "limits"
        ),
        (
            "KEY TERMS / DEFINITIONS: ruling as a craft of knowledge | ship-of-state "
            "analogy | degeneration of constitutions | timocracy, oligarchy, "
            "democracy, tyranny | liberty mistaken for qualification | demagogue "
            "and the slide to tyranny"
        ): (
            "KEY TERMS / DEFINITIONS: political craft | ship analogy | degeneration "
            "| demagoguery | tyranny"
        ),
        (
            "KEY TERMS / DEFINITIONS: number of rulers times end served | right "
            "forms and deviant forms | polity as the good rule of the many | "
            "democracy in the classical deviant sense | middle class and mixed "
            "constitution | middle course between statism and individualism"
        ): (
            "KEY TERMS / DEFINITIONS: one-few-many | common good | polity | "
            "oligarchy | middle class"
        ),
        (
            "KEY TERMS / DEFINITIONS: absolute against constitutional monarchy | "
            "hereditary office and the equality objection | divine right of kings | "
            "above politics as symbolic neutrality | succession failure and "
            "arbitrariness | reigns but does not govern"
        ): (
            "KEY TERMS / DEFINITIONS: absolute monarchy | constitutional monarchy | "
            "heredity | accountability | freedom"
        ),
        (
            "KEY TERMS / DEFINITIONS: sovereignty of God rather than of the people | "
            "sacred law and clerical mediation | the interpretation monopoly | who "
            "speaks for God | liberty of conscience and equal citizenship | "
            "secularism as an institutional relation"
        ): (
            "KEY TERMS / DEFINITIONS: divine sovereignty | sacred law | "
            "interpretation | conscience | citizenship"
        ),
        (
            "KEY TERMS / DEFINITIONS: direct against representative democracy | "
            "procedural against substantive democracy | liberal democracy and "
            "constitutional limits | participatory and deliberative democracy | "
            "minority protection and equal moral standing | political equality "
            "against social inequality"
        ): (
            "KEY TERMS / DEFINITIONS: direct | representative | majoritarian | "
            "liberal | deliberative"
        ),
        (
            "KEY TERMS / DEFINITIONS: power against authority | traditional, "
            "charismatic and legal-rational types | ideal type and routinisation of "
            "charisma | competitive struggle for the people's vote | democratic "
            "elitism as a minimum condition | iron law of oligarchy"
        ): (
            "KEY TERMS / DEFINITIONS: authority | legitimacy | charisma | "
            "competition | oligarchy"
        ),
        (
            "KEY TERMS / DEFINITIONS: thin-centred ideology and host ideology | pure "
            "people against corrupt elite | exclusive moral representation | logic "
            "of articulation | illiberal democracy and the form-substance grid | "
            "manufactured consent and the regulator's dilemma"
        ): (
            "KEY TERMS / DEFINITIONS: populism | anti-pluralism | illiberalism | "
            "propaganda | capture"
        ),
        (
            "KEY TERMS / DEFINITIONS: unitary against federal division of powers | "
            "coming-together and holding-together federation | federation against "
            "confederation | bicameralism and the judicial umpire | decentralisation "
            "and subsidiarity | local self-government and village self-rule"
        ): (
            "KEY TERMS / DEFINITIONS: unitary | federal | parliamentary | "
            "presidential | subsidiarity"
        ),
        (
            "KEY TERMS / DEFINITIONS: mixed government and checks and balances | "
            "separation of powers and rule of law | constitutionalism under a "
            "supreme law | shared axes of comparison | error-correction and peaceful "
            "transfer | graded verdict rather than a winner"
        ): (
            "KEY TERMS / DEFINITIONS: mixed government | separation | rule of law | "
            "checks | error-correction"
        ),
    }
    for old, new in closure_replacements.items():
        text = text.replace(old, new)
    return text
