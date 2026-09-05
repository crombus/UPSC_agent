"""Durable learner-v2 content and master-flow specification for Sovereignty.

Philosophy Optional, Paper II, Socio-Political Philosophy, official topic 2:
``Sovereignty : Austin, Bodin, Laski, Kautilya.``

Every doctrine, term, date and criticism below is grounded in the repository
owners for this clause: the canonical owner ``Sovereignty.md``, the retained
layered learning session and workbook, the verified 2018-2025 Socio-Political
PYQ ledger, and the Socio-Political advanced dossier.  Nothing here is taken
from a live source, and no publication year is asserted that the repository
sources do not carry.
"""

from __future__ import annotations

import re
from typing import Any


TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-02"
TOPIC_TITLE = "Sovereignty"
TOPIC_NUMBER = 2
SECTION_KEY = "paper-ii-socio-political-philosophy"
GENERATION_DATE = "2026-09-03"
OFFICIAL_SYLLABUS_VERBATIM = "Sovereignty : Austin, Bodin, Laski, Kautilya."
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\Sovereignty.md"
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
    "Socio-Political\\learning-sessions\\topic-02\\g5\\"
    "topic-02_Complete-Learning-Session_2026-09-03.md"
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
        "The Concept and Taxonomy of Sovereignty",
        "Sovereignty is the supreme, final and authoritative power inside a "
        "political community, and it is deliberately distinguished from the "
        "government of the day, from the state as a whole, and from mere force.",
        "Analytically the concept is worked through four paired axes — internal "
        "and external, legal and political, de jure and de facto, titular and "
        "actual — so that the standing question becomes where final authority is "
        "located, how it is structured, and how far it is limited.",
        "Sovereignty names the claim to supreme and final authority within a "
        "political community, and a controlled answer opens by separating "
        "internal from external, legal from political, de jure from de facto, and "
        "titular from actual before any thinker is named.",
        [
            "supreme final authority",
            "internal and external sovereignty",
            "legal and political sovereignty",
            "de jure and de facto sovereignty",
            "titular and actual sovereignty",
            "monism and pluralism",
        ],
        "Lead with supreme final authority as the definition, run the internal "
        "and external, legal and political, de jure and de facto and titular and "
        "actual distinctions as the analytical grid, and only then place the "
        "monism and pluralism dispute on that grid.",
        "A political community needs a point of final decision, so the concept "
        "isolates that point and then splits it along four axes rather than "
        "assuming one undivided centre of power.",
        "Once the axes are separated, a state can be legally supreme yet "
        "politically constrained, or titular in form yet powerless in fact, which "
        "is precisely what a single undivided notion conceals.",
        "Do not equate sovereignty with force, with the government of the day or "
        "with the state itself; the bandit coerces but never holds recognised "
        "final authority.",
        "Modern constitutional democracies disperse power so widely that speaking "
        "of one supreme authority looks misleading.",
        "The objection defeats monism, not the inquiry: keeping the legal, "
        "political and external dimensions apart preserves a usable concept "
        "without assuming a single undivided centre.",
        "The taxonomy organises the question but does not by itself decide who "
        "the sovereign is in any actual constitutional order.",
        "Definition of supreme final authority, the four paired axes, one "
        "misidentification trap, then the monist-pluralist dispute named but not "
        "yet resolved.",
        [
            "Sovereignty is supreme, final and authoritative power; it is not force, "
            "not the government and not the state.",
            "Internal sovereignty is supremacy within; external sovereignty is "
            "independence in the society of states.",
            "Legal sovereignty is the competent law-maker; political sovereignty is "
            "the real power behind the law.",
            "De jure is lawful title, de facto is effective obedience; titular is "
            "formal dignity, actual is real decision.",
        ],
        [
            visual(
                "The four axes of the concept",
                "One concept, four paired axes: the exam grid that must open every "
                "sovereignty answer.",
                "                     SUPREME, FINAL, AUTHORITATIVE POWER",
                "                                   |",
                "     +-------------+---------------+---------------+-------------+",
                "     |             |               |               |             |",
                "  INTERNAL      EXTERNAL         LEGAL         POLITICAL      DE JURE",
                "  supremacy     independence   competent      real power      lawful",
                "  within the    in the         law-maker      behind the      title",
                "  community     state system   (Austin)       law (Laski)",
                "                                                                 |",
                "                                                              DE FACTO",
                "                                                        effective obedience",
                "  TITULAR = formal dignity of office   <->   ACTUAL = who really decides",
            ),
            visual(
                "What sovereignty is not",
                "Three standing misidentifications that cost marks before the "
                "argument even begins.",
                "+-----------------------+------------------------------------------------+",
                "| WRONG IDENTIFICATION  | WHY IT FAILS                                   |",
                "+-----------------------+------------------------------------------------+",
                "| sovereignty = force   | a bandit coerces but holds no final authority  |",
                "| sovereignty = govt.   | governments change; the sovereign office does  |",
                "|                       | not lapse with them                            |",
                "| sovereignty = state   | the state is the whole association; sovereignty|",
                "|                       | is its claim to final decision                 |",
                "+-----------------------+------------------------------------------------+",
            ),
        ],
    ),
    session(
        "Bodin: The Absolute and Perpetual Power of the Commonwealth",
        "Bodin holds that a commonwealth survives civil and religious war only if "
        "one power can make and unmake law for everyone without asking the "
        "consent of any earthly superior.",
        "Sovereignty for Bodin is the absolute and perpetual power of a "
        "commonwealth: absolute because it has no human superior inside the "
        "realm, perpetual because it attaches to the office rather than to a "
        "temporary magistrate, and undivided because two final wills would "
        "reproduce the civil war the doctrine exists to end.",
        "Bodin gives the modern state its first systematic vocabulary of "
        "sovereignty — absolute, perpetual and undivided — while keeping the "
        "sovereign bound by divine law, natural law and the fundamental laws of "
        "the realm, so his absolutism is juristic rather than lawless.",
        [
            "absolute and perpetual power",
            "power to make and unmake law",
            "indivisibility of sovereign title",
            "legibus solutus",
            "divine and natural law limits",
            "fundamental laws (leges imperii)",
        ],
        "Write the absolute and perpetual power formula first, prove "
        "indivisibility of sovereign title from the civil-war argument, then use "
        "legibus solutus together with the divine and natural law limits and the "
        "fundamental laws to show the doctrine is not caprice.",
        "Confessional civil war makes rival final claims intolerable, so Bodin "
        "concentrates the power to make and unmake law in one perpetual office "
        "that no subject may lawfully rival.",
        "The commonwealth gains a permanent impersonal centre of command, yet the "
        "same move leaves modern equality, justice and liberty without strong "
        "institutional guarantees against that centre.",
        "Bodin must not be read as a lawless absolutist or as Hobbes before "
        "Hobbes; his sovereign is released from ordinary positive law but never "
        "from higher normative order.",
        "If sovereignty is absolute it must negate all rights, liberties and "
        "constitutional limits.",
        "Absolute in Bodin means supreme within the hierarchy of positive law, "
        "while divine law, natural law and the fundamental laws of the realm "
        "continue to bind the sovereign office.",
        "Those higher-law limits are conceptually real but institutionally weak, "
        "because Bodin supplies no enforcement machinery against a sovereign who "
        "ignores them.",
        "Context of disorder, the three attributes, the limiting framework, then "
        "a conditional verdict on compatibility with equality, justice and "
        "liberty.",
        [
            "Absolute = no human superior within the commonwealth; perpetual = "
            "attached to office, not to a magistrate.",
            "The pre-eminent mark is the power to make and unmake law for all "
            "subjects in general.",
            "Division of governmental functions is allowed; division of the "
            "sovereign title is not.",
            "Bound by divine law, natural law and fundamental laws (leges imperii); "
            "legibus solutus only as to ordinary positive law.",
        ],
        [
            visual(
                "From civil war to the sovereign office",
                "Bodin's argument is a remedy: plural final claims produce disorder, "
                "so finality is concentrated and then bounded.",
                "RIVAL FINAL CLAIMS (churches, estates, feudal lords)",
                "        |",
                "        v",
                "PARALYSIS: no claim can settle a dispute between the others",
                "        |",
                "        v",
                "REMEDY -> ONE ABSOLUTE AND PERPETUAL POWER OF THE COMMONWEALTH",
                "        |",
                "        +--> ABSOLUTE   : no human superior inside the realm",
                "        +--> PERPETUAL  : belongs to the office, not the officer",
                "        +--> UNDIVIDED  : two final wills = insoluble conflict",
                "        |",
                "        v",
                "BOUNDED BY -> divine law | natural law | fundamental laws (leges imperii)",
                "        |",
                "        v",
                "RESULT: legibus solutus as to ordinary positive law, not as to higher law",
            ),
            visual(
                "Bodin's limits, and their weakness",
                "The limiting framework is genuine in principle and thin in "
                "enforcement — the exact place where marks are won.",
                "+---------------------------+----------------------------------------+",
                "| LIMIT                     | FORCE OF THE LIMIT                     |",
                "+---------------------------+----------------------------------------+",
                "| divine law                | the sovereign cannot validly command   |",
                "|                           | what offends divine order              |",
                "| natural law               | justice and right reason remain        |",
                "|                           | normative limits                       |",
                "| fundamental laws          | constitutive laws structure the        |",
                "| (leges imperii)           | sovereign office itself                |",
                "+---------------------------+----------------------------------------+",
                "WEAKNESS -> no institutional machinery enforces any of the three limits.",
            ),
        ],
    ),
    session(
        "Austin I: The Command Theory of Legal Sovereignty",
        "Austin asks a narrow question and answers it sharply: who, as a matter "
        "of legal fact, is habitually obeyed by the bulk of a society while "
        "habitually obeying nobody else?",
        "Within analytical jurisprudence Austin defines the sovereign as a "
        "determinate human superior receiving habitual obedience from the bulk of "
        "a given society and rendering habitual obedience to no other, and "
        "defines positive law as the command of that sovereign backed by a "
        "sanction, from which absoluteness, indivisibility, illimitability and "
        "inalienability follow.",
        "Austin converts sovereignty into a question of legal form: a determinate "
        "human superior, habitual obedience from the bulk of society, and law as "
        "command backed by sanction, which is unmatched for juristic clarity and "
        "immediately vulnerable on political reality.",
        [
            "determinate human superior",
            "habitual obedience of the bulk",
            "command backed by sanction",
            "absolute and illimitable",
            "indivisible and inalienable",
            "analytical jurisprudence",
        ],
        "State the determinate human superior definition, add habitual obedience "
        "of the bulk as the test of location, derive law as command backed by "
        "sanction, and list the attributes absolute and illimitable, indivisible "
        "and inalienable as consequences of the analytical jurisprudence project.",
        "Because law is treated as the command of a determinate superior, the "
        "sovereign must be identifiable, must face no legal superior, and must "
        "not be partitioned without ceasing to be sovereign.",
        "Legal validity becomes crisply testable, but the model buys that "
        "sharpness by excluding constitutional, customary and international "
        "material that other jurists count as law.",
        "Never write that Austin's sovereign is the state; the whole point is "
        "that it is a determinate person or body identifiable in a given society.",
        "Reducing law to command backed by sanction leaves no room for rules that "
        "confer powers rather than impose duties.",
        "Austin's reply keeps the analytic gain: within his defined field the "
        "command model isolates positive law from morality and from custom with "
        "unmatched precision.",
        "The precision is bought by narrowing the field, so the theory describes "
        "legal form far better than it describes any actual political order.",
        "Project, definition, five attributes, command-and-sanction, then a "
        "single sentence flagging that criticism follows.",
        [
            "Sovereign = determinate human superior, habitually obeyed by the bulk, "
            "habitually obeying no one.",
            "Attributes: determinate, absolute, indivisible, illimitable, "
            "inalienable.",
            "Law = command of the sovereign backed by a sanction.",
            "Source anchor: The Province of Jurisprudence Determined, 1832.",
        ],
        [
            visual(
                "The command chain",
                "Austin's whole system in one chain: identify the superior, then read "
                "law off the command relation.",
                "DETERMINATE HUMAN SUPERIOR",
                "        |  identifiable person or body, not an abstraction",
                "        v",
                "HABITUAL OBEDIENCE by the BULK of a given society",
                "        |  obedience is habitual, not occasional",
                "        v",
                "OBEYS NO OTHER SUPERIOR  ->  legal illimitability follows",
                "        |",
                "        v",
                "COMMAND  --backed by-->  SANCTION  --produces-->  DUTY",
                "        |",
                "        v",
                "POSITIVE LAW = command of the sovereign backed by sanction",
            ),
            visual(
                "The five attributes and what each excludes",
                "Each attribute is a definitional consequence, and each one becomes a "
                "target in the next session.",
                "+-----------------+--------------------------------+---------------------+",
                "| ATTRIBUTE       | MEANING                        | EXCLUDES            |",
                "+-----------------+--------------------------------+---------------------+",
                "| determinate     | the sovereign is identifiable  | diffuse electorates |",
                "| absolute        | no legal limit binds from above| bills of rights     |",
                "| indivisible     | finality cannot be partitioned | federal division    |",
                "| illimitable     | no superior legal authority    | international law   |",
                "| inalienable     | transfer ends sovereignty      | pooled authority    |",
                "+-----------------+--------------------------------+---------------------+",
            ),
        ],
    ),
    session(
        "Austin II: Criticisms and Compatibility with Democracy",
        "The command theory is attacked from outside by legal facts it cannot "
        "fit — federal states, international law, custom, popular rule and "
        "Maine's Indian case — and the democracy question is then answered by "
        "degree rather than by yes or no.",
        "The external critique holds that no determinate superior exists in a "
        "federation, that Austin over-narrows law by denying international law, "
        "that custom shows obedience can precede command, that popular "
        "sovereignty locates authority in an indeterminate electorate, and that "
        "Maine's Ranjit Singh case shows real authority as personal and embedded.",
        "Austin's sovereign survives as an account of legal finality and fails as "
        "an account of democratic political reality, so compatibility with "
        "democracy is partial in the narrow legal sense and weak in the deeper "
        "sense of derivative, divided and rights-bound authority.",
        [
            "federalism objection",
            "international law objection",
            "customary law objection",
            "popular sovereignty objection",
            "Maine's Ranjit Singh example",
            "degree-judgment on democracy",
        ],
        "Order the objections as federalism, international law, customary law and "
        "popular sovereignty, add Maine's Ranjit Singh example as the "
        "anthropological counter-case, and close the democracy question as a "
        "degree-judgment rather than a verdict of simple compatibility.",
        "Each objection isolates a legal fact the command model cannot describe "
        "without strain, and the accumulated strain is what forces the "
        "degree-judgment on democracy.",
        "Austin can be defended as an account of legal form, but the defence "
        "concedes that political authority in a democracy is derivative, divided "
        "and bound by rights.",
        "Do not answer the democracy question with a flat yes or no; relocating "
        "finality to the constituent power is not the same as demonstrating an "
        "undivided superior.",
        "Federal constitutions simply prove that Austin was wrong, because "
        "sovereignty there is plainly divided.",
        "The monist reply relocates finality in the constitution-making authority "
        "rather than in either legislature, which preserves the concept while "
        "conceding that no ordinary organ is the Austinian sovereign.",
        "That reply shifts the problem instead of solving it, since a "
        "constituent power that acts only rarely is a poor candidate for habitual "
        "obedience.",
        "Objection, monist reply, residual difficulty for each head, then a "
        "graded verdict separating legal finality from democratic reality.",
        [
            "Federalism: no single determinate superior; saying the constitution is "
            "sovereign shifts the problem.",
            "International law: Austin denies it is law strictly; critics say he "
            "over-narrows the concept of law.",
            "Custom: obedience can precede command, and the tacit-adoption reply is "
            "widely judged artificial.",
            "Maine's Ranjit Singh: despotic power over life and property coexisted "
            "with untouched customary law.",
        ],
        [
            visual(
                "Four objections and the monist replies",
                "Each row is a complete answer paragraph: fact, objection, reply, "
                "residual difficulty.",
                "+----------------+-------------------------+---------------------------+",
                "| HEAD           | OBJECTION               | MONIST REPLY / RESIDUAL   |",
                "+----------------+-------------------------+---------------------------+",
                "| federalism     | authority is divided    | finality moves to the     |",
                "|                | between two orders      | constituent power; that   |",
                "|                |                         | shifts the problem        |",
                "| international  | binding rules exist     | Austin keeps purity but   |",
                "| law            | with no world sovereign | narrows law excessively   |",
                "| custom         | obedience precedes any  | tacit adoption by courts; |",
                "|                | command                 | widely judged artificial  |",
                "| popular        | the people rule, yet    | electorate is legally     |",
                "| sovereignty    | are indeterminate       | indeterminate; political  |",
                "|                |                         | finality is conceded      |",
                "+----------------+-------------------------+---------------------------+",
            ),
            visual(
                "Is Austin compatible with democracy?",
                "A degree-judgment: two senses of the question, two different answers.",
                "QUESTION: is Austin's sovereign compatible with democracy?",
                "        |",
                "        +--> NARROW LEGAL SENSE",
                "        |    a determinate law-making organ can still be identified",
                "        |    VERDICT -> compatible, but only formally",
                "        |",
                "        +--> DEEPER POLITICAL SENSE",
                "             authority is derivative (from the people),",
                "             divided (federal and functional),",
                "             rights-bound (constitutional guarantees)",
                "             VERDICT -> sits uneasily with democracy",
                "        |",
                "        v",
                "WRITE A DEGREE-JUDGMENT, NEVER A FLAT YES OR NO",
            ),
        ],
    ),
    session(
        "Kelsen and Hart: The Post-Austinian Refinement of Legal Sovereignty",
        "Two later jurists rebuild what Austin was trying to capture, keeping "
        "supreme legal authority while discarding the personal commander who "
        "cannot explain succession, persistence or power-conferring rules.",
        "Kelsen replaces the sovereign will with a hierarchy of norms whose "
        "validity terminates in a presupposed basic norm (Grundnorm), while Hart "
        "replaces command with the union of primary and secondary rules, the "
        "ultimate test being a rule of recognition sustained by the convergent "
        "practice and internal point of view of officials.",
        "Kelsen and Hart preserve the idea of supreme legal authority while "
        "dissolving the personal sovereign: validity flows from a presupposed "
        "basic norm for Kelsen, and from an officially practised rule of "
        "recognition for Hart, which answers exactly the defects that sank the "
        "command theory.",
        [
            "hierarchy of norms",
            "Grundnorm as presupposed basic norm",
            "primary and secondary rules",
            "rule of recognition",
            "internal point of view",
            "having an obligation versus being obliged",
        ],
        "Diagnose the command theory's failures on succession, persistence and "
        "power-conferring rules, answer them with the hierarchy of norms ending "
        "in the Grundnorm and with primary and secondary rules tested by the rule "
        "of recognition, and use the internal point of view to mark the "
        "difference between having an obligation and being obliged.",
        "Validity is transferred from a person to a structure, so a legal system "
        "can outlive any ruler and can confer powers as well as impose duties.",
        "Supreme legal authority survives the collapse of the command theory, but "
        "it now sits in a presupposed norm or an official practice rather than in "
        "any identifiable human will.",
        "Never merge Kelsen, Hart and Laski into one critique, and never date "
        "Kelsen to 1961; the English General Theory is 1945 and The Concept of "
        "Law is 1961.",
        "Presupposing a basic norm or resting law on official practice looks like "
        "relocating the mystery rather than removing it.",
        "The relocation is a gain, because a presupposed norm or a practised rule "
        "of recognition can be identified and tested publicly, whereas a "
        "determinate personal superior often cannot be found at all.",
        "Neither account tells us what the content of a legal order ought to be, "
        "so both leave the moral evaluation of sovereign power to other "
        "arguments.",
        "Diagnosis of Austin's defects, Kelsen's answer, Hart's answer, then "
        "placement against Bodin, Austin, Laski and Kautilya.",
        [
            "Command theory fails on succession, persistence and power-conferring "
            "rules.",
            "Kelsen: validity flows from a higher norm to a presupposed Grundnorm.",
            "Hart: primary rules impose duties; secondary rules of recognition, "
            "change and adjudication cure uncertainty, static character and "
            "inefficiency.",
            "Dates: Kelsen, General Theory of Law and State, 1945; Hart, The Concept "
            "of Law, 1961. Never swap them.",
        ],
        [
            visual(
                "Three defects, two repairs",
                "Read down the defect column, then across to see which repair does the "
                "work.",
                "+---------------------+-------------------------+---------------------+",
                "| AUSTINIAN DEFECT    | KELSEN'S REPAIR         | HART'S REPAIR       |",
                "+---------------------+-------------------------+---------------------+",
                "| succession: why is  | validity descends from  | rule of recognition |",
                "| the new ruler's     | a higher norm, not from | already identifies  |",
                "| word law at once?   | a person                | the valid source    |",
                "| persistence: why do | norms remain valid till | rules of change     |",
                "| old statutes bind?  | validly repealed        | govern repeal       |",
                "| power-conferring    | norms authorise as well | secondary rules     |",
                "| rules: wills, deeds | as oblige               | confer powers       |",
                "+---------------------+-------------------------+---------------------+",
            ),
            visual(
                "The two structures side by side",
                "Kelsen builds a pyramid of validity; Hart builds a union of two kinds "
                "of rule resting on official practice.",
                "KELSEN                              HART",
                "  GRUNDNORM (presupposed)             RULE OF RECOGNITION",
                "        ^                                   ^  official convergent",
                "        |  validity                         |  practice + internal",
                "  CONSTITUTION                              |  point of view",
                "        ^                                   |",
                "        |                             SECONDARY RULES",
                "  STATUTES                            recognition | change | adjudication",
                "        ^                                   ^",
                "        |                                   |",
                "  ORDERS / JUDGMENTS                  PRIMARY RULES (duties)",
                "CONTRAST -> presupposed norm vs practised rule: both dispense with a person.",
            ),
        ],
    ),
    session(
        "Laski and the Pluralist Critique of Absolute Sovereignty",
        "Laski argues that treating the state as the single unlimited source of "
        "authority is untrue to how people actually live, dangerous for liberty, "
        "and unnecessary for order.",
        "Laski's pluralism rejects monistic sovereignty as philosophically false, "
        "politically dangerous and sociologically unreal: the state is one "
        "association among many, authority should be divided and shared with "
        "churches, unions, universities and local bodies, and the state must "
        "compete for allegiance by the quality of what it does.",
        "Laski rejects absolute sovereignty because it is false to a plural "
        "social world, dangerous as a licence for unquestioned power and unreal "
        "as description, replacing it with authority that is divided, shared and "
        "continuously earned through competition for allegiance.",
        [
            "false, dangerous and unreal",
            "state as one association among many",
            "divided and shared authority",
            "competition for allegiance",
            "associational autonomy",
            "pluralist, not anarchist",
        ],
        "Open with the false, dangerous and unreal triad, support it with the "
        "state as one association among many and with associational autonomy, "
        "show what replaces monism through divided and shared authority and "
        "competition for allegiance, and close by insisting the position is "
        "pluralist, not anarchist.",
        "If loyalty is genuinely plural, then no single will can claim total "
        "obedience, and authority must be justified association by association "
        "rather than assumed for the state as a whole.",
        "Liberty gains a powerful defence, while the coordinating work that only "
        "a state can do — final arbitration between conflicting associations — is "
        "left comparatively under-theorised.",
        "Laski limits the state but never abolishes it, so calling him an "
        "anarchist is the standing error on this thinker.",
        "Pluralism cannot say who finally decides when associations conflict "
        "irreconcilably, especially in an emergency.",
        "The better pluralist answer distinguishes coordination authority from "
        "unlimited moral supremacy: a modern order needs a final procedure, not "
        "an unanswerable sovereign will.",
        "The reply still leaves the coordinating function thinner than the "
        "critique of monism is sharp, which is why examiners ask whether Laski is "
        "a satisfactory position.",
        "Triad of rejection, the positive pluralist thesis, the anarchism trap "
        "closed, then a graded verdict of decisive corrective and incomplete "
        "construction.",
        [
            "Absolute sovereignty is false, dangerous and unreal — memorise the "
            "triad in that order.",
            "The state is one association among many, though a uniquely important "
            "one.",
            "The state must earn allegiance by what it does, not command it by what "
            "it is.",
            "Source anchor: A Grammar of Politics; Studies in the Problem of "
            "Sovereignty.",
        ],
        [
            visual(
                "Why absolute sovereignty is rejected",
                "Three independent lines of attack; a strong answer uses all three, "
                "each with its own evidence.",
                "ABSOLUTE SOVEREIGNTY",
                "        |",
                "        +--> PHILOSOPHICALLY FALSE",
                "        |      loyalty is plural; no single will exhausts obligation",
                "        |",
                "        +--> POLITICALLY DANGEROUS",
                "        |      supplies a doctrine of unquestioned power against liberty",
                "        |",
                "        +--> SOCIOLOGICALLY UNREAL",
                "               churches, unions, universities and local bodies act with",
                "               their own real authority every day",
                "        |",
                "        v",
                "REPLACEMENT -> divided and shared authority + competition for allegiance",
            ),
            visual(
                "Monist state versus pluralist state",
                "The same society, two descriptions: the contrast is what a comparative "
                "question is testing.",
                "+---------------------------+------------------------------------------+",
                "| MONIST PICTURE            | LASKI'S PLURALIST PICTURE                |",
                "+---------------------------+------------------------------------------+",
                "| one supreme will          | many centres of real authority           |",
                "| associations are          | associations possess autonomy and command|",
                "| subordinate creatures     | genuine loyalty                          |",
                "| obedience is owed         | obedience is earned by performance       |",
                "| sovereignty is indivisible| authority is divided and shared          |",
                "+---------------------------+------------------------------------------+",
                "VERDICT -> decisive corrective on liberty; incomplete on coordination.",
            ),
        ],
    ),
    session(
        "Kautilya I: The Seven-Limbed State (saptāṅga), the Ruler (svāmī) and "
        "Calibrated Coercion (daṇḍanīti)",
        "Kautilya treats sovereignty as the working capacity of a whole state "
        "organism rather than as the will of one man, and measures a ruler by "
        "whether the organism actually holds together.",
        "In the Arthaśāstra sovereignty is systemic: the state is a body of seven "
        "interdependent limbs (saptāṅga) — ruler (svāmī), ministers (amātya), "
        "territory and people (janapada), fortified defence (durga), treasury "
        "(kośa), coercive force (daṇḍa) and ally (mitra) — over which the ruler "
        "presides while remaining bound by righteous duty (dharma), and order is "
        "maintained by the calibrated science of punishment (daṇḍanīti).",
        "Kautilyan sovereignty is the capacity of a seven-limbed state organism "
        "headed by a duty-bound ruler and sustained by calibrated coercion, which "
        "makes it systemic and welfare-oriented rather than a personal, "
        "illimitable will in the Austinian sense.",
        [
            "seven-limbed state (saptāṅga)",
            "ruler (svāmī) as head",
            "ministers, treasury and coercive force",
            "calibrated coercion (daṇḍanīti)",
            "law of the fish (mātsya-nyāya)",
            "duty-bound, not illimitable",
        ],
        "Set out the seven-limbed state with the ruler as head, name ministers, "
        "treasury and coercive force to show interdependence, explain calibrated "
        "coercion against the law of the fish at one extreme and tyranny at the "
        "other, and insist throughout that the ruler is duty-bound, not "
        "illimitable.",
        "Because every limb depends on the others, headship works only through "
        "counsel, revenue, defence and enforcement, so authority is exercised "
        "through an institutional system rather than by bare command.",
        "The ruler gains enormous practical power and simultaneously acquires "
        "obligations, since a treasury emptied by tyranny or a people ruined by "
        "over-punishment destroys the very limbs that sustain rule.",
        "Do not equate the ruler with Austin's illimitable superior; he is bound "
        "by righteous duty, by prudence and by the welfare of subjects.",
        "A theory built for monarchy and written as advice to a king cannot be a "
        "theory of sovereignty at all.",
        "It is a theory of sovereignty in the sense that matters here, because it "
        "answers where final direction lies, how it is institutionally "
        "constituted and what limits it, even though the form of government is "
        "monarchical.",
        "The limits are ethical and prudential rather than justiciable, so they "
        "restrain a wise ruler more effectively than a reckless one.",
        "Seven limbs named and explained, headship qualified by duty, calibrated "
        "coercion between anarchy and tyranny, then a comparison hook to Austin.",
        [
            "Saptāṅga: svāmī, amātya, janapada, durga, kośa, daṇḍa, mitra — "
            "sovereignty is systemic, not merely personal.",
            "Daṇḍanīti is calibrated: too little punishment yields mātsya-nyāya, too "
            "much yields tyranny.",
            "The svāmī is the highest limb, yet is bound by dharma, counsel and the "
            "welfare of subjects.",
            "Fear without welfare is self-defeating, because a ruined janapada and "
            "kośa destroy the state's capacity.",
        ],
        [
            visual(
                "The seven limbs and what each supplies",
                "Sovereignty as organism: the ruler heads the body but cannot act "
                "without the other six limbs.",
                "+------------------+-----------------------+--------------------------+",
                "| LIMB             | ENGLISH               | WHAT IT SUPPLIES         |",
                "+------------------+-----------------------+--------------------------+",
                "| svāmī            | the ruler             | headship and direction   |",
                "| amātya           | ministers, officials  | counsel and execution    |",
                "| janapada         | territory and people  | the productive base      |",
                "| durga            | fortified defence     | security and protection  |",
                "| kośa             | treasury              | the material basis       |",
                "| daṇḍa            | coercive force, army  | enforcement and defence  |",
                "| mitra            | ally                  | external support         |",
                "+------------------+-----------------------+--------------------------+",
                "SYSTEMIC CLAIM -> weaken any limb and the sovereign capacity itself falls.",
            ),
            visual(
                "The calibration of the rod",
                "Punishment is a dial, not a switch: both extremes destroy the state's "
                "own capacity.",
                "  TOO LITTLE                 CALIBRATED                 TOO MUCH",
                "  daṇḍa withheld     <----   daṇḍanīti proper   ---->   daṇḍa excessive",
                "        |                          |                          |",
                "        v                          v                          v",
                "  MĀTSYA-NYĀYA              order + security            TYRANNY, revolt",
                "  the law of the fish:      + welfare (yogakṣema)       ruined janapada",
                "  the strong devour                                     and empty kośa",
                "  the weak",
                "RULE -> the rod is measured by its effect on capacity, never by the",
                "        ruler's pleasure.",
            ),
        ],
    ),
    session(
        "Kautilya II: The Circle of States (maṇḍala), Six-Fold Policy "
        "(ṣāḍguṇya), Security and Welfare (yogakṣema) and Modern Relevance",
        "The same theory that organises the state internally also tells the ruler "
        "how to survive among neighbours, and it ties both to the duty of keeping "
        "subjects secure and prosperous.",
        "External sovereignty in the Arthaśāstra is strategic and relational: the "
        "circle of states (maṇḍala) treats the immediate neighbour as rival and "
        "the neighbour's neighbour as natural ally, the six-fold policy "
        "(ṣāḍguṇya) supplies peace (sandhi), hostility (vigraha), marching "
        "(yāna), poised inaction (āsana), shelter (saṃśraya) and dual policy "
        "(dvaidhībhāva), and the whole realist apparatus is oriented to security "
        "and welfare (yogakṣema).",
        "Kautilya's external sovereignty is relational rather than declaratory, "
        "since the circle of states and the six-fold policy make independence a "
        "matter of continuously managed advantage, while security and welfare "
        "supply the ethical frame that keeps the realism from becoming normless.",
        [
            "circle of states (maṇḍala)",
            "no permanent friend or enemy",
            "six-fold policy (ṣāḍguṇya)",
            "security and welfare (yogakṣema)",
            "welfare duty toward subjects",
            "selective appropriation, not reproduction",
        ],
        "Explain the circle of states and the neighbour logic behind no permanent "
        "friend or enemy, list the six-fold policy as the operational toolkit, "
        "anchor both in security and welfare as the ruler's duty, and answer the "
        "modern-relevance stem by selective appropriation rather than "
        "reproduction of monarchy.",
        "Because power is measured against immediate neighbours, alliance and "
        "hostility follow position and interest, and the six-fold policy simply "
        "operationalises that geometry.",
        "Independence becomes something continuously negotiated rather than "
        "permanently possessed, which is why the theory transfers so well to "
        "modern strategic debate while its monarchical form does not.",
        "Do not read the maxim as cynicism without limits; the welfare duty means "
        "the realism is bounded, and relevance is claimed by theme, not by "
        "reproducing kingship.",
        "A statecraft manual written for a monarch can have no application in a "
        "democratic form of government.",
        "The applicable content is thematic — state capacity, fiscal strength, "
        "intelligence, calibrated enforcement, strategic autonomy and welfare "
        "obligation — and these principles can be selectively appropriated by a "
        "democratic order.",
        "What cannot be transferred is the constitutional form itself, since "
        "monarchy, secret administration and unaccountable espionage are "
        "incompatible with democratic legitimacy.",
        "Circle of states, six-fold policy, security and welfare, then a "
        "structured relevance verdict by theme with the monarchy caveat stated "
        "explicitly.",
        [
            "Maṇḍala: the neighbour is the rival; the neighbour's neighbour is the "
            "natural ally.",
            "Ṣāḍguṇya: sandhi, vigraha, yāna, āsana, saṃśraya, dvaidhībhāva.",
            "Yogakṣema = security plus well-being; it is the ethical frame of "
            "Kautilyan realism.",
            "Modern relevance is claimed by theme — capacity, fiscal strength, "
            "strategy, welfare — never by reproducing monarchy.",
        ],
        [
            visual(
                "The circle of states",
                "Position generates policy: the geometry of neighbours explains the "
                "maxim about friends and enemies.",
                "        [ NEIGHBOUR'S NEIGHBOUR ]  <-- natural ALLY (mitra)",
                "                    ^",
                "                    |  shares a rival",
                "        [ IMMEDIATE NEIGHBOUR   ]  <-- natural RIVAL (ari)",
                "                    ^",
                "                    |  shares a border",
                "        [ THE ASPIRING RULER    ]  (vijigīṣu)",
                "                    |",
                "                    v",
                "  READING -> alliances follow position and interest, so there is no",
                "             permanent friend and no permanent enemy, only interests.",
            ),
            visual(
                "The six-fold policy as a decision toolkit",
                "Six named options, each with the situation that selects it.",
                "+-------------------+-------------------+----------------------------+",
                "| POLICY            | ENGLISH           | SELECTED WHEN              |",
                "+-------------------+-------------------+----------------------------+",
                "| sandhi            | peace or treaty   | weaker, or gains from calm |",
                "| vigraha           | hostility, war    | stronger and the target is |",
                "|                   |                   | worth the cost             |",
                "| yāna              | marching, advance | preparation is complete    |",
                "| āsana             | poised inaction   | strength is equal; wait    |",
                "| saṃśraya          | seeking shelter   | too weak to stand alone    |",
                "| dvaidhībhāva      | dual policy       | peace with one, war with   |",
                "|                   |                   | another at the same time   |",
                "+-------------------+-------------------+----------------------------+",
            ),
        ],
    ),
    session(
        "Inter-Thinker Debates, Criticisms and Replies",
        "The four syllabus thinkers are set against one another on the same "
        "debates — where sovereignty sits, whether it is absolute, whether it "
        "can be divided — so that criticisms and replies replace summary.",
        "The comparative grid runs monism against pluralism across location, "
        "absoluteness, divisibility, treatment of associations, governing anxiety "
        "and principal weakness, and each standing criticism of absolute "
        "sovereignty is answered by a monist reply that leaves an identifiable "
        "residual difficulty.",
        "Sovereignty debates are settled on a fixed grid — location, "
        "absoluteness, divisibility, associations, anxiety and weakness — and the "
        "strongest answers move objection to reply to residual difficulty instead "
        "of merely listing what each thinker said.",
        [
            "monism versus pluralism grid",
            "location of final authority",
            "absoluteness and divisibility",
            "objection, reply, residual difficulty",
            "Austin compared with Kautilya",
            "Bodin compared with Austin",
        ],
        "Build the monism versus pluralism grid first, fix the location of final "
        "authority for each thinker, test absoluteness and divisibility across "
        "the row, and then run objection, reply, residual difficulty on the "
        "specific pairing the stem names, whether Austin compared with Kautilya "
        "or Bodin compared with Austin.",
        "Comparing thinkers on identical questions exposes exactly where they "
        "agree in vocabulary and diverge in doctrine, which is what a comparative "
        "directive is testing.",
        "The grid converts a memory task into an argument, and it also shows that "
        "no single thinker answers every question well, which is why graded "
        "verdicts beat verdicts of simple victory.",
        "Do not collapse Bodin into Austin or Kelsen and Hart into Laski; the "
        "first pair differ on higher-law limits, and the second are internal "
        "repairs rather than pluralist rejections.",
        "Comparison across such different traditions and centuries is "
        "anachronistic and therefore unhelpful.",
        "The comparison is legitimate because the questions are shared even where "
        "the contexts differ: each thinker must say where final authority lies, "
        "what limits it and whether it can be divided.",
        "Shared questions do not make shared assumptions, so every comparison "
        "must record the difference of purpose — juristic analysis, state "
        "building, liberty or statecraft — alongside the doctrinal contrast.",
        "Grid, chosen pairing, objection to reply to residual difficulty, then a "
        "graded verdict naming what each thinker gets right.",
        [
            "Location: supreme law-giver (Bodin), determinate superior (Austin), no "
            "single locus (Laski), svāmī within saptāṅga (Kautilya).",
            "Anxiety: civil war (Bodin), juristic clarity (Austin), liberty (Laski), "
            "survival and welfare (Kautilya).",
            "Austin versus Kautilya: command, obedience, sanction against rule, "
            "administration, welfare, coercion and strategy.",
            "Ordering rule for a 20-marker: internal critique (Kelsen, Hart) first, "
            "external critique (federalism, custom, international law, Laski) second.",
        ],
        [
            visual(
                "The four-thinker grid",
                "One grid answers most comparative stems; read down a column for a "
                "thinker, across a row for a debate.",
                "+---------------+------------+------------+-----------+-------------+",
                "| AXIS          | BODIN      | AUSTIN     | LASKI     | KAUTILYA    |",
                "+---------------+------------+------------+-----------+-------------+",
                "| located in    | supreme    | determinate| no single | svāmī in    |",
                "|               | law-giver  | superior   | locus     | saptāṅga    |",
                "| absolute?     | yes, with  | yes, in    | no        | strong but  |",
                "|               | higher law | legal form |           | dharma-bound|",
                "| divisible?    | no         | no         | yes       | organically |",
                "|               |            |            |           | coordinated |",
                "| associations  | secondary  | subordinate| autonomous| constitutive|",
                "| core anxiety  | civil war  | juristic   | liberty   | survival and|",
                "|               |            | clarity    |           | welfare     |",
                "+---------------+------------+------------+-----------+-------------+",
            ),
            visual(
                "The critical-answer engine",
                "Three moves, repeated for every head of criticism; the residual is "
                "where the marks are.",
                "OBJECTION  ---->  MONIST REPLY  ---->  RESIDUAL DIFFICULTY",
                "    |                  |                        |",
                "    v                  v                        v",
                "democracy         legal finality can      authority is derivative,",
                "                  be retained            divided and rights-bound",
                "federalism        finality moves to      relocation is not proof of",
                "                  constituent power      an undivided superior",
                "pluralism         shared sovereignty     the monistic concept may",
                "                  is not sovereignty     misdescribe plural life",
                "moral limits      analysis is separate   the separation is judged",
                "                  from morality          incomplete by critics",
            ),
        ],
    ),
    session(
        "Globalization, Contemporary Sovereignty and the Standing Examiner Traps",
        "The modern question is whether interdependence has killed sovereignty, "
        "and the disciplined answer is that its form has changed while the claim "
        "to final decision has not been surrendered.",
        "The contemporary debate sets an erosion thesis, which reads treaties, "
        "trade regimes, supranational adjudication and transnational flows as a "
        "loss of sovereignty, against a transformation thesis, which reads the "
        "same evidence as sovereignty pooled, constrained, negotiated and "
        "networked while final decisions on war, treaty, currency and membership "
        "remain claimed by states.",
        "Globalization reconfigures sovereignty rather than abolishing it, "
        "because legal independence and practical interdependence are different "
        "things, and states still claim the final decision on war, treaty, "
        "currency and membership even where they have pooled authority.",
        [
            "erosion thesis",
            "transformation and resilience thesis",
            "pooled and negotiated sovereignty",
            "legal independence versus practical interdependence",
            "reconfigured, not abolished",
            "graded verdict on relevance",
        ],
        "Frame the answer as erosion thesis against transformation and resilience "
        "thesis, deploy legal independence versus practical interdependence as "
        "the decisive distinction, illustrate with pooled and negotiated "
        "sovereignty, and conclude that sovereignty is reconfigured, not "
        "abolished, in a graded verdict on relevance.",
        "Treaty commitments and supranational regimes bind conduct without "
        "removing the competence to enter, interpret or exit them, so "
        "constraint operates through consent rather than through the loss of "
        "final authority.",
        "The doctrine survives as a question about location and limits rather "
        "than as an assertion of unlimited power, which is why it remains a live "
        "analytical tool instead of a historical relic.",
        "Never write that sovereignty has disappeared under globalization; the "
        "exam-safe formulation is that it is reconfigured, pooled and negotiated "
        "while final decisions are still claimed.",
        "Since states routinely accept binding external adjudication, the claim "
        "to final authority is now merely rhetorical.",
        "Acceptance of external adjudication is itself an exercise of sovereign "
        "competence, and the competence to withdraw or renegotiate shows that "
        "finality has been constrained rather than transferred.",
        "The reply is weaker for very small or heavily indebted states, where "
        "formal competence and effective choice can diverge so far that the "
        "distinction becomes largely nominal.",
        "Two theses, the decisive distinction, illustration, then a graded "
        "verdict that closes with legal form, political fact and international "
        "practice.",
        [
            "Sovereignty is reconfigured — pooled, constrained, negotiated, networked "
            "— not abolished.",
            "Deploy the distinction: legal independence is not the same as practical "
            "interdependence.",
            "Final claims persist on war, treaty, currency and membership.",
            "Closing line: illimitable in legal form, limited in political fact, "
            "negotiated in international practice.",
        ],
        [
            visual(
                "Erosion against transformation",
                "The same evidence, two readings: name both, then adjudicate by "
                "degree.",
                "                 SAME EVIDENCE BASE",
                "   treaties | trade regimes | supranational adjudication | flows",
                "                 |                          |",
                "                 v                          v",
                "        EROSION THESIS               TRANSFORMATION THESIS",
                "  authority leaks upward and    sovereignty is pooled, constrained,",
                "  outward; the state is being   negotiated and networked; the state",
                "  hollowed out                  adapts and persists",
                "                 |                          |",
                "                 +------------+-------------+",
                "                              v",
                "     GRADED VERDICT -> reconfigured, not abolished; legal independence",
                "                       is not the same as practical interdependence.",
            ),
            visual(
                "Final pre-submission trap check",
                "Seven standing errors; run the list before writing the conclusion.",
                "+---+------------------------------------+------------------------------+",
                "| # | WRONG                              | CORRECT                      |",
                "+---+------------------------------------+------------------------------+",
                "| 1 | Austin's sovereign is the state    | a determinate person or body |",
                "| 2 | Laski is an anarchist              | he limits, not abolishes     |",
                "| 3 | Bodin is lawless                   | divine, natural, fundamental |",
                "| 4 | svāmī equals Austin's superior     | duty-bound, not illimitable  |",
                "| 5 | Kelsen, Hart and Laski are one     | three distinct moves         |",
                "| 6 | Kelsen dated to 1961               | Kelsen 1945, Hart 1961       |",
                "| 7 | sovereignty has disappeared        | it is reconfigured           |",
                "+---+------------------------------------+------------------------------+",
            ),
        ],
    ),
)


ASCII_PANELS = (
    {
        "title": "The central question and the analytical axes of sovereignty",
        "structural_type": "root-question-and-conceptual-axes",
        "sessions": [1],
        "lines": [
            "CENTRAL QUESTION -> where is final authority LOCATED, how is it STRUCTURED, how far",
            "                    is it LIMITED?",
            "        |",
            "        v",
            "ROOT CONCEPT: supreme, final and authoritative power within a political community",
            "  NOT mere force (a bandit coerces)  |  NOT the government of the day  |  NOT the state",
            "        |",
            "  +-----+------------+-------------------+--------------------+",
            "  v                  v                   v                    v",
            "INTERNAL/EXTERNAL  LEGAL/POLITICAL   DE JURE/DE FACTO   TITULAR/ACTUAL",
            "supremacy within   competent law-    lawful title vs    formal dignity vs",
            "vs independence    maker vs the      effective          real power of",
            "among states       real power        obedience          decision",
            "        |",
            "        v",
            "CONTROL: distinguish the axes FIRST, locate the thinker SECOND, adjudicate LAST.",
        ],
    },
    {
        "title": "Bodin: absolute, perpetual, undivided - and still bounded",
        "structural_type": "doctrine-derivation-with-limits",
        "sessions": [2],
        "lines": [
            "CONDITION: confessional civil war; churches, estates and feudal lords each claim finality",
            "        |",
            "        v",
            "DEFINITION -> sovereignty is the ABSOLUTE and PERPETUAL power of a commonwealth",
            "        |",
            "  +-----+---------------------+---------------------------+",
            "  v                           v                           v",
            "ABSOLUTE                   PERPETUAL                   UNDIVIDED",
            "no human superior          attached to the OFFICE,     two final wills would",
            "inside the realm           not to a magistrate         revive civil war",
            "  |                                                        |",
            "  v                                                        v",
            "PRE-EMINENT MARK -> power to MAKE and UNMAKE law for all subjects in general,",
            "                    without the consent of any superior",
            "        |",
            "        v",
            "LIMITS THAT SURVIVE -> divine law | natural law | fundamental laws (leges imperii)",
            "LEGIBUS SOLUTUS -> released from ORDINARY POSITIVE LAW only; not from higher law",
            "TRAP -> Bodin is not Hobbes before Hobbes; supreme is not morally empty",
            "VERDICT -> first systematic theory and indispensable vocabulary; institutional",
            "           guarantees against abuse remain weak.",
        ],
    },
    {
        "title": "Austin's command theory: the mechanism of legal sovereignty",
        "structural_type": "causal-mechanism-chain",
        "sessions": [3],
        "lines": [
            "PROJECT -> analytical jurisprudence: define law and sovereignty with juristic precision",
            "        |",
            "        v",
            "DETERMINATE HUMAN SUPERIOR  (an identifiable person or body, never an abstraction)",
            "        |",
            "        v  receives",
            "HABITUAL OBEDIENCE from the BULK of a given society",
            "        |",
            "        v  and renders",
            "OBEDIENCE TO NO OTHER SUPERIOR",
            "        |",
            "        v  therefore",
            "COMMAND --> SANCTION --> DUTY --> POSITIVE LAW",
            "        |",
            "  +-----+--------+---------+-----------+------------+",
            "  v              v         v           v            v",
            "DETERMINATE   ABSOLUTE  INDIVISIBLE ILLIMITABLE  INALIENABLE",
            "identifiable  no legal  finality    no superior  transfer ends",
            "              limit     unpartitionable          sovereignty",
            "SOURCE -> The Province of Jurisprudence Determined, 1832",
            "TRAP -> Austin's sovereign is NOT the state; it is a determinate superior.",
        ],
    },
    {
        "title": "The external critique of Austin and the democracy verdict",
        "structural_type": "problem-response-matrix",
        "sessions": [4],
        "lines": [
            "+----------------+---------------------------+------------------------------+",
            "| HEAD           | OBJECTION                 | MONIST REPLY / RESIDUAL      |",
            "+----------------+---------------------------+------------------------------+",
            "| federalism     | no single determinate     | finality relocated to the    |",
            "|                | superior in a federation  | constituent power; that      |",
            "|                |                           | SHIFTS the problem           |",
            "| international  | binding rules exist with  | conceptual purity preserved, |",
            "| law            | no world sovereign        | but law is over-narrowed     |",
            "| custom         | obedience can PRECEDE     | tacit adoption by courts;    |",
            "|                | command                   | widely judged artificial     |",
            "| popular        | the people rule but are   | legal indeterminacy admitted;|",
            "| sovereignty    | legally indeterminate     | political finality conceded  |",
            "| Maine: Ranjit  | despotic power coexisted  | authority is often personal  |",
            "| Singh          | with untouched custom     | and socially embedded        |",
            "+----------------+---------------------------+------------------------------+",
            "DEMOCRACY -> narrow legal sense: compatible in form",
            "          -> deeper political sense: derivative, divided, rights-bound = uneasy",
            "CONTROL -> answer by DEGREE-JUDGMENT, never by a flat yes or no.",
        ],
    },
    {
        "title": "Kelsen and Hart: the internal repair of supreme legal authority",
        "structural_type": "parallel-reconstruction-hierarchies",
        "sessions": [5],
        "lines": [
            "DIAGNOSIS -> the command theory fails on SUCCESSION, PERSISTENCE and",
            "             POWER-CONFERRING RULES",
            "        |",
            "  +-----+-------------------------------+",
            "  v                                     v",
            "KELSEN (General Theory, 1945)      HART (The Concept of Law, 1961)",
            "  GRUNDNORM  (presupposed)           RULE OF RECOGNITION",
            "      ^                                  ^ official convergent practice",
            "      | validity descends                | + INTERNAL POINT OF VIEW",
            "  CONSTITUTION                       SECONDARY RULES",
            "      ^                              recognition | change | adjudication",
            "      |                                  ^ cure uncertainty | static",
            "  STATUTES                               | character | inefficiency",
            "      ^                                  |",
            "      |                              PRIMARY RULES (duties)",
            "  ORDERS AND JUDGMENTS",
            "TERMINOLOGY -> having an obligation (internal) vs being obliged (gunman coercion)",            "PLACEMENT -> both keep SUPREME LEGAL AUTHORITY and discard the PERSONAL sovereign",
            "TRAP -> never merge Kelsen, Hart and Laski; never date Kelsen to 1961.",
        ],
    },
    {
        "title": "Laski's pluralism: the rejection and its replacement",
        "structural_type": "branch-tree-with-replacement",
        "sessions": [6],
        "lines": [
            "TARGET -> the monistic doctrine of absolute, indivisible, unlimited state sovereignty",
            "        |",
            "  +-----+----------------------+----------------------------+",
            "  v                            v                            v",
            "PHILOSOPHICALLY FALSE      POLITICALLY DANGEROUS       SOCIOLOGICALLY UNREAL",
            "loyalty is plural; no      supplies a doctrine of      churches, unions,",
            "single will exhausts       unquestioned power          universities and local",
            "obligation                 against liberty             bodies really decide",
            "        |",
            "        v",
            "REPLACEMENT ARCHITECTURE",
            "  +--> the state is ONE ASSOCIATION AMONG MANY, though uniquely important",
            "  +--> authority is DIVIDED AND SHARED with functional associations",
            "  +--> the state must COMPETE FOR ALLEGIANCE by what it does",
            "        |",
            "        v",
            "TRAP -> pluralist, NOT anarchist: he limits the state, he does not abolish it",
            "VERDICT -> decisive corrective on liberty; incomplete on coordination, which is",
            "           why examiners ask whether it is a satisfactory position.",
        ],
    },
    {
        "title": "Kautilya inside the state: seven limbs and the calibrated rod",
        "structural_type": "organic-classification-and-calibration",
        "sessions": [7],
        "lines": [
            "CLAIM -> sovereignty is the CAPACITY of a state organism, not one man's bare will",
            "        |",
            "        v",
            "SAPTĀṄGA (seven limbs)",
            "  svāmī     ruler            -> headship and direction",
            "  amātya    ministers        -> counsel, administration, execution",
            "  janapada  territory/people -> the productive social base",
            "  durga     fortified place  -> security and protection",
            "  kośa      treasury         -> the material basis of rule",
            "  daṇḍa     coercive force   -> enforcement, punishment, defence",
            "  mitra     ally             -> external support in the interstate order",
            "        |",
            "        v",
            "DAṆḌANĪTI, THE CALIBRATION DIAL",
            "  too little <----------------- proper ------------------> too much",
            "  MĀTSYA-NYĀYA                order + welfare              TYRANNY",
            "  the strong devour the weak  (yogakṣema)                  revolt, ruined",
            "                                                           janapada, empty kośa",
            "TRAP -> the svāmī is DHARMA-BOUND; he is not Austin's illimitable superior.",
        ],
    },
    {
        "title": "Kautilya outside the state: circle, six-fold policy and relevance",
        "structural_type": "spatial-strategy-and-application",
        "sessions": [8],
        "lines": [
            "SPATIAL LAYER -> the MAṆḌALA: authority is measured against neighbours",
            "   [ neighbour's neighbour ]  = natural ALLY (shares a rival)",
            "              ^",
            "   [ immediate neighbour   ]  = natural RIVAL (shares a border)",
            "              ^",
            "   [ the aspiring ruler    ]  = vijigīṣu",
            "2025 PYQ LINE -> prompt framing, NOT a verified Kautilya quotation",
            "SUPPORTED THESIS -> alliances and policies change with position, power and interest",
            "        |",
            "        v",
            "ṢĀḌGUṆYA, the six-fold operational policy",
            "  sandhi peace | vigraha hostility | yāna advance",
            "  āsana poised inaction | saṃśraya shelter | dvaidhībhāva dual policy",
            "        |",
            "        v",
            "ETHICAL FRAME -> YOGAKṢEMA: security plus well-being is the ruler's duty",
            "        |",
            "        v",
            "MODERN RELEVANCE -> by THEME: state capacity, fiscal strength, intelligence,",
            "  calibrated enforcement, strategic autonomy, welfare obligation",
            "LIMIT -> SELECTIVE APPROPRIATION of principles, never reproduction of monarchy.",
        ],
    },
    {
        "title": "Comparison grid and the objection-reply-residual engine",
        "structural_type": "comparison-matrix-and-critical-engine",
        "sessions": [9],
        "lines": [
            "+---------------+------------+-------------+-----------+---------------+",
            "| AXIS          | BODIN      | AUSTIN      | LASKI     | KAUTILYA      |",
            "+---------------+------------+-------------+-----------+---------------+",
            "| located in    | supreme    | determinate | no single | svāmī within  |",
            "|               | law-giver  | superior    | locus     | saptāṅga      |",
            "| absolute?     | yes, with  | yes, in     | no        | strong but    |",
            "|               | higher law | legal form  |           | dharma-bound  |",
            "| divisible?    | no         | no          | yes       | organically   |",
            "|               |            |             |           | coordinated   |",
            "| associations  | secondary  | subordinate | autonomous| constitutive  |",
            "| core anxiety  | civil war  | juristic    | liberty   | survival and  |",
            "|               |            | clarity     |           | welfare       |",
            "+---------------+------------+-------------+-----------+---------------+",
            "AUSTIN vs KAUTILYA -> command/obedience/sanction  against  rule/administration/",
            "                      welfare/coercion/strategy",
            "CRITICAL ENGINE -> OBJECTION -> MONIST REPLY -> RESIDUAL DIFFICULTY",
            "  democracy  -> legal finality retained -> authority still derivative and divided",
            "  federalism -> constituent power       -> relocation is not proof of one superior",
            "  pluralism  -> shared is not sovereign -> monism may misdescribe plural life",
            "ORDERING RULE -> internal critique (Kelsen, Hart) first, external critique second.",
        ],
    },
    {
        "title": "Globalization, standing traps and the reusable answer spine",
        "structural_type": "synthesis-verdict-and-answer-rail",
        "sessions": [10],
        "lines": [
            "SAME EVIDENCE -> treaties | trade regimes | supranational adjudication | flows",
            "        |                                        |",
            "        v                                        v",
            "EROSION THESIS                          TRANSFORMATION / RESILIENCE THESIS",
            "authority leaks upward and outward      sovereignty is pooled, constrained,",
            "                                        negotiated and networked",
            "        +------------------+--------------------+",
            "                           v",
            "DECISIVE DISTINCTION -> legal independence  vs  practical interdependence",
            "MECHANISMS -> treaty constraint | delegated competence | pooled decision | dependence",
            "PERSISTENT CLAIMS    -> war | treaty | currency | membership",
            "VERDICT -> RECONFIGURED, not abolished",
            "TRAP CHECK -> Austin's sovereign is not the state | Laski is not an anarchist |",
            "  Bodin is not lawless | svāmī is not illimitable | Kelsen 1945, Hart 1961 |",
            "  sovereignty has not disappeared",
            "ANSWER SPINE -> 1 decode the directive and name the owner-thinker",
            "                2 open with the taxonomy of sovereignty",
            "                3 state the doctrine in the thinker's own terms",
            "                4 objection and reply, objector named",
            "                5 graded verdict",
            "TIERS -> 10 marks: steps 1-3 and a verdict; 15: full spine and one objection;",
            "         20: full spine, internal then external critique, and a comparison close.",
        ],
    },
)

ASCII_PANELS = (
    *ASCII_PANELS,
    {
        "title": "Five classical attributes and two sovereignty-of-the-people claims",
        "structural_type": "attribute-ladder-and-source-distinction",
        "sessions": [1, 2, 3],
        "lines": [
            "CLASSICAL LEGAL ATTRIBUTES -> absoluteness | permanence | universality |",
            "                              inalienability | indivisibility",
            "PERMANENCE -> government changes while state sovereignty continues",
            "UNIVERSALITY -> jurisdiction reaches persons and associations in the territory",
            "INALIENABILITY -> powers may be delegated; sovereign status is not merely transferred",
            "POPULAR SOVEREIGNTY -> people are the internal source of legitimate authority",
            "ROUSSEAU -> general will claims common good; government remains an agent",
            "NATIONAL SOVEREIGNTY -> collective self-determination and territorial independence",
            "TRAP -> popular source, national self-rule and majority preference are not synonyms",
        ],
    },
    {
        "title": "Pluralist lineage and jurisdiction-safe constitutional comparison",
        "structural_type": "school-lineage-and-two-jurisdiction-matrix",
        "sessions": [4, 6, 10],
        "lines": [
            "PLURALIST SCHOOL -> Figgis: real associations | Cole: functional groups |",
            "                    MacIver: law, constitution and residual coordination",
            "LASKI REMAINS THE OWNER -> early legal-fiction attack; mature limited sovereignty",
            "UNITED KINGDOM -> Parliament is the supreme legal authority in its jurisdiction",
            "INDIA -> Parliament exercises powers conferred and limited by a supreme Constitution",
            "JUDICIAL REVIEW -> enforces constitutional limits; it does not make courts sovereign",
            "FEDERALISM -> distribute competences without assuming legal and political finality coincide",
            "GLOBAL LINK -> pooling/delegation moves exercise of power, not universal sovereignty",
            "VERDICT -> modern sovereignty is competence-distributed and morally contestable",
        ],
    },
)


GRAPHICAL_PILLS = (
    [
        {"text": "SUPREME, FINAL, AUTHORITATIVE POWER", "role": "primary"},
        {"text": "INTERNAL VS EXTERNAL", "role": "mechanism"},
        {"text": "LEGAL VS POLITICAL", "role": "comparison"},
        {"text": "DE JURE VS DE FACTO", "role": "evidence"},
        {"text": "TITULAR VS ACTUAL", "role": "outcome"},
        {"text": "NOT FORCE, NOT GOVERNMENT, NOT THE STATE", "role": "caution"},
    ],
    [
        {"text": "ABSOLUTE AND PERPETUAL POWER", "role": "primary"},
        {"text": "MAKE AND UNMAKE LAW", "role": "mechanism"},
        {"text": "UNDIVIDED SOVEREIGN TITLE", "role": "outcome"},
        {"text": "DIVINE, NATURAL, FUNDAMENTAL LAW", "role": "evidence"},
        {"text": "LEGIBUS SOLUTUS ONLY AS TO POSITIVE LAW", "role": "comparison"},
        {"text": "NOT HOBBES BEFORE HOBBES", "role": "caution"},
    ],
    [
        {"text": "DETERMINATE HUMAN SUPERIOR", "role": "primary"},
        {"text": "HABITUAL OBEDIENCE OF THE BULK", "role": "mechanism"},
        {"text": "COMMAND BACKED BY SANCTION", "role": "evidence"},
        {"text": "ABSOLUTE, INDIVISIBLE, ILLIMITABLE, INALIENABLE", "role": "outcome"},
        {"text": "PROVINCE OF JURISPRUDENCE DETERMINED 1832", "role": "comparison"},
        {"text": "NOT THE STATE ITSELF", "role": "caution"},
    ],
    [
        {"text": "FEDERALISM: NO SINGLE SUPERIOR", "role": "primary"},
        {"text": "INTERNATIONAL LAW OVER-NARROWED", "role": "mechanism"},
        {"text": "CUSTOM PRECEDES COMMAND", "role": "evidence"},
        {"text": "MAINE: RANJIT SINGH", "role": "comparison"},
        {"text": "DEMOCRACY BY DEGREE-JUDGMENT", "role": "outcome"},
        {"text": "NEVER A FLAT YES OR NO", "role": "caution"},
    ],
    [
        {"text": "HIERARCHY OF NORMS", "role": "primary"},
        {"text": "GRUNDNORM PRESUPPOSED", "role": "mechanism"},
        {"text": "PRIMARY AND SECONDARY RULES", "role": "evidence"},
        {"text": "RULE OF RECOGNITION", "role": "outcome"},
        {"text": "INTERNAL POINT OF VIEW", "role": "comparison"},
        {"text": "KELSEN 1945, HART 1961", "role": "caution"},
    ],
    [
        {"text": "FALSE, DANGEROUS, UNREAL", "role": "primary"},
        {"text": "ONE ASSOCIATION AMONG MANY", "role": "mechanism"},
        {"text": "DIVIDED AND SHARED AUTHORITY", "role": "evidence"},
        {"text": "COMPETE FOR ALLEGIANCE", "role": "outcome"},
        {"text": "ASSOCIATIONAL AUTONOMY", "role": "comparison"},
        {"text": "PLURALIST, NOT ANARCHIST", "role": "caution"},
    ],
    [
        {"text": "SAPTĀṄGA: SEVEN LIMBS", "role": "primary"},
        {"text": "SVĀMĪ HEADS, DOES NOT OWN", "role": "mechanism"},
        {"text": "KOŚA, DAṆḌA, JANAPADA", "role": "evidence"},
        {"text": "DAṆḌANĪTI IS CALIBRATED", "role": "outcome"},
        {"text": "MĀTSYA-NYĀYA IF WITHHELD", "role": "comparison"},
        {"text": "DHARMA-BOUND, NOT ILLIMITABLE", "role": "caution"},
    ],
    [
        {"text": "MAṆḌALA: THE CIRCLE OF STATES", "role": "primary"},
        {"text": "NEIGHBOUR IS RIVAL", "role": "mechanism"},
        {"text": "ṢĀḌGUṆYA: SIX-FOLD POLICY", "role": "evidence"},
        {"text": "YOGAKṢEMA: SECURITY AND WELFARE", "role": "outcome"},
        {"text": "NO PERMANENT FRIEND OR ENEMY", "role": "comparison"},
        {"text": "APPROPRIATE THEMES, NOT MONARCHY", "role": "caution"},
    ],
    [
        {"text": "MONISM VERSUS PLURALISM GRID", "role": "primary"},
        {"text": "LOCATION, ABSOLUTENESS, DIVISIBILITY", "role": "mechanism"},
        {"text": "AUSTIN VERSUS KAUTILYA", "role": "comparison"},
        {"text": "OBJECTION, REPLY, RESIDUAL", "role": "evidence"},
        {"text": "INTERNAL CRITIQUE FIRST", "role": "outcome"},
        {"text": "DO NOT COLLAPSE BODIN INTO AUSTIN", "role": "caution"},
    ],
    [
        {"text": "EROSION VERSUS TRANSFORMATION", "role": "primary"},
        {"text": "POOLED, CONSTRAINED, NEGOTIATED", "role": "mechanism"},
        {"text": "LEGAL INDEPENDENCE IS NOT INTERDEPENDENCE", "role": "comparison"},
        {"text": "WAR, TREATY, CURRENCY, MEMBERSHIP", "role": "evidence"},
        {"text": "RECONFIGURED, NOT ABOLISHED", "role": "outcome"},
        {"text": "SEVEN-TRAP PRE-SUBMISSION CHECK", "role": "caution"},
    ],
)


GRAPHICAL_STAGE_ZERO_GROUPS = [
    {
        "heading": "THE ROOT CONCEPT",
        "role": "evidence",
        "items": [
            "Sovereignty is the supreme, final and authoritative power within a "
            "political community.",
            "It is not mere force: a bandit coerces without holding final authority.",
            "It is neither the government of the day nor the state taken as a whole.",
        ],
    },
    {
        "heading": "THE FOUR ANALYTICAL AXES",
        "role": "mechanism",
        "items": [
            "Internal supremacy within the community against external independence "
            "among states.",
            "Legal sovereignty as the competent law-maker against political "
            "sovereignty as the real power behind it.",
            "De jure lawful title against de facto obedience; titular dignity "
            "against actual decision.",
        ],
    },
    {
        "heading": "THE EXAM CONSEQUENCE",
        "role": "outcome",
        "items": [
            "Distinguish the axes first, locate the thinker second, adjudicate last.",
            "Austin and Bodin are monists; Laski is the pluralist; Kautilya is "
            "systemic and duty-bound.",
            "Every verdict on this clause is graded, never a simple victory for one "
            "thinker.",
        ],
    },
]


REQUIRED_CORE_TERMS = (
    "supreme, final",
    "internal sovereignty",
    "external sovereignty",
    "legal sovereignty",
    "political sovereignty",
    "de jure",
    "de facto",
    "titular",
    "absolute and perpetual",
    "perpetual",
    "permanence",
    "universality",
    "undivided",
    "legibus solutus",
    "divine law",
    "natural law",
    "leges imperii",
    "determinate human superior",
    "habitual obedience",
    "command",
    "sanction",
    "indivisible",
    "illimitable",
    "inalienable",
    "analytical jurisprudence",
    "Province of Jurisprudence Determined",
    "federalism",
    "international law",
    "customary law",
    "popular sovereignty",
    "national sovereignty",
    "general will",
    "Ranjit Singh",
    "Maine",
    "Kelsen",
    "Grundnorm",
    "hierarchy of norms",
    "Hart",
    "primary",
    "secondary rules",
    "rule of recognition",
    "internal point of view",
    "Laski",
    "one association among many",
    "allegiance",
    "pluralist",
    "monistic",
    "Figgis",
    "Cole",
    "MacIver",
    "Kautilya",
    "saptāṅga",
    "svāmī",
    "amātya",
    "janapada",
    "durga",
    "kośa",
    "daṇḍa",
    "mitra",
    "daṇḍanīti",
    "mātsya-nyāya",
    "maṇḍala",
    "ṣāḍguṇya",
    "sandhi",
    "vigraha",
    "yāna",
    "āsana",
    "saṃśraya",
    "yogakṣema",
    "dharma",
    "Arthaśāstra",
    "globalization",
    "parliamentary sovereignty",
    "constitutional supremacy",
    "delegation",
    "pooling",
    "prompt framing",
)

ADVANCED_SESSION_TITLES = tuple(
    str(spec["title"]) for spec in SESSION_SPECS
)

_SESSIONS = len(SESSION_SPECS)
if _SESSIONS != 10:
    raise ValueError(f"Sovereignty requires exactly 10 core sessions, found {_SESSIONS}.")
_PANELS = len(ASCII_PANELS)
if _PANELS != 12:
    raise ValueError(f"Sovereignty requires exactly 12 ASCII panels, found {_PANELS}.")


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


def _replace_section(text: str, start: str, end: str, replacement: str) -> str:
    pattern = rf"(?ms)^{re.escape(start)}\s*$.*?(?=^{re.escape(end)}\s*$)"
    if not re.search(pattern, text):
        raise ValueError(f"Cannot replace assembled section {start!r}.")
    return re.sub(pattern, replacement.rstrip() + "\n\n", text, count=1)


def transform_assembled(
    text: str,
    *,
    owner_text: str,
    generation: int,
) -> str:
    if generation != 6:
        raise ValueError(f"Sovereignty semantic successor is pinned to g6, got g{generation}.")

    text = re.sub(
        r"(?m)^!\[Sovereignty[^\]]*\]\([^)]+\)\s*\n+"
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
    attributes = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 1.2A Classical attributes of sovereignty",
            "### 1.3 Legal and political sovereignty",
        )
    )
    popular = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 1.5A Popular and national sovereignty",
            "### 1.6 Why the concept becomes controversial",
        )
    )
    parliamentary = _demote_owner(
        _extract_owner_section(
            owner_text,
            "#### (d1) Parliamentary sovereignty and constitutional supremacy",
            "#### (e) Maine's Ranjit Singh example",
        )
    )
    pluralists = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 4.1A The supported pluralist lineage",
            "### 4.2 Why he rejects absolute sovereignty",
        )
    )
    kautilya = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 5.5 The circle-of-states (maṇḍala) theory and the six-fold policy "
            "(ṣāḍguṇya)",
            "### 5.6 Security and welfare (yogakṣema) and the ruler's welfare duty",
        )
    )

    text = text.replace(
        "- **Canonical doctrine source:** "
        "`upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/Sovereignty.md` "
        "(10,694 words), sliced verbatim into the CORE UPSC layers (each canonical "
        "teaching passage exactly once) and preserved again, in full, in the "
        "canonical apparatus block.",
        "- **Canonical doctrine source:** "
        "`upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/Sovereignty.md`, "
        "repaired under the ten-gate semantic-completeness protocol and promoted "
        "into this immutable successor.",
    )
    text = text.replace(
        "the concept and its distinctions (internal/external, legal/political, "
        "de jure/de facto, titular/actual);",
        "the concept and its distinctions (internal/external, legal/political, "
        "de jure/de facto, titular/actual, popular/national); the five classical "
        "attributes (absoluteness, permanence, universality, inalienability and "
        "indivisibility);",
    )
    text = text.replace(
        "Kautilya's saptanga, dandaniti, mandala, sadgunya and yogaksema;",
        "Kautilya's seven-limbed state (saptanga), calibrated coercion "
        "(dandaniti), circle of states (mandala), six-fold policy (sadgunya) "
        "and security/welfare (yogaksema);",
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

    text = text.replace(
        "**Technical definition:** Analytically the concept is worked through four "
        "paired axes — internal and external, legal and political, de jure and de "
        "facto, titular and actual — so that the standing question becomes where "
        "final authority is located, how it is structured, and how far it is limited.",
        "**Technical definition:** Sovereignty must be analysed through its internal/"
        "external, legal/political, de jure/de facto, titular/actual and popular/"
        "national axes, together with the classical attributes of absoluteness, "
        "permanence, universality, inalienability and indivisibility.",
        1,
    )
    if "1.2A Classical attributes of sovereignty" not in text:
        text = text.replace(
            "#### 1.3 Legal and political sovereignty",
            attributes + "\n\n#### 1.3 Legal and political sovereignty",
            1,
        )
    if "1.5A Popular and national sovereignty" not in text:
        text = text.replace(
            "#### 1.6 Why the concept becomes controversial",
            popular + "\n\n#### 1.6 Why the concept becomes controversial",
            1,
        )
    if "(d1) Parliamentary sovereignty and constitutional supremacy" not in text:
        text = text.replace(
            "#### (e) Maine's Ranjit Singh example",
            parliamentary + "\n\n#### (e) Maine's Ranjit Singh example",
            1,
        )
    if "4.1A The supported pluralist lineage" not in text:
        text = text.replace(
            "#### 4.2 Why he rejects absolute sovereignty",
            pluralists + "\n\n#### 4.2 Why he rejects absolute sovereignty",
            1,
        )
    text = _replace_section(
        text,
        "#### 5.5 Maṇḍala theory and ṣāḍguṇya",
        "#### 5.6 Security and welfare (yogakṣema) and the ruler's welfare duty",
        kautilya,
    )

    globalization_anchor = (
        "- **Kautilya:** the strategic-relational side of external sovereignty "
        "remains highly relevant. ⚠️"
    )
    if "Mechanisms of constraint and reconfiguration" not in text:
        global_fragment = _extract_owner_section(
            owner_text,
            "#### Mechanisms of constraint and reconfiguration",
            "**Objection → Reply:**",
        )
        global_fragment = _demote_owner(global_fragment)
        text = text.replace(
            globalization_anchor,
            globalization_anchor + "\n\n" + global_fragment,
            1,
        )

    text = text.replace(
        "**How to use them:** Explain the circle of states and the neighbour logic "
        "behind no permanent friend or enemy, list the six-fold policy as the "
        "operational toolkit, anchor both in security and welfare as the ruler's "
        "duty, and answer the modern-relevance stem by selective appropriation "
        "rather than reproduction of monarchy.",
        "**How to use them:** Treat the 2025 line as prompt framing, not a verified "
        "Kautilya quotation; explain strategic flexibility through the circle of "
        "states and six-fold policy, then anchor external realism in security, "
        "welfare and selective modern appropriation.",
    )
    text = text.replace(
        "- **no permanent friend or enemy**",
        "- **2025 maxim as prompt framing, not verified quotation**",
    )
    text = text.replace(
        "KEY TERMS / DEFINITIONS: circle of states (maṇḍala) | no permanent friend "
        "or enemy | six-fold policy (ṣāḍguṇya) | security and welfare (yogakṣema) | "
        "welfare duty toward subjects | selective appropriation, not reproduction",
        "KEY TERMS / DEFINITIONS: maṇḍala | ṣāḍguṇya | strategic flexibility | "
        "prompt framing | yogakṣema",
    )
    text = text.replace(
        "> ANALYSIS: The 2025 quoted line -- \"no permanent friend or permanent "
        "enemy\" --\n> must be LOCATED before it is judged. It is a description of "
        "the mandala's\n> structural logic, not a licence for amoral policy: "
        "interests are permanent, but\n> the internal duty of yogakshema and "
        "dharma still frames how they are pursued.",
        "> ANALYSIS: The 2025 line is the examiner's prompt framing, not a verified "
        "Kautilya quotation. Its defensible use is analytical: the maṇḍala and "
        "ṣāḍguṇya support strategic flexibility as positions, power and interests "
        "change, while yogakṣema limits any slide into normless realpolitik.",
    )

    old_mcq = (
        "#### MCQ 32\n\n'There is no permanent friend or permanent enemy' is best "
        "read as:\n\nA. a rejection of all statecraft\nB. a claim that alliances "
        "rest on sentiment\nC. evidence that Kautilya is wholly amoral\nD. the "
        "structural logic of the mandala - only interests are permanent, framed by "
        "the duty of yogakshema\n\n**Correct answer: D** — the structural logic of "
        "the mandala - only interests are permanent, framed by the duty of "
        "yogakshema\n\n**Explanation:** The maxim expresses the mandala's "
        "interest-driven logic while remaining framed by the internal duty of welfare."
    )
    new_mcq = (
        "#### MCQ 32\n\nHow should the 2025 line 'There is no permanent friend or "
        "permanent enemy' be handled in a Kautilya answer?\n\nA. As a verified "
        "verbatim quotation from the *Arthaśāstra*\nB. As proof that Kautilya "
        "rejects every moral limit\nC. As a reason to omit *maṇḍala* and "
        "*ṣāḍguṇya*\nD. As the examiner's framing, interpreted through strategic "
        "flexibility without claiming authenticated authorship\n\n**Correct answer: "
        "D** — as the examiner's framing, interpreted through strategic flexibility "
        "without claiming authenticated authorship\n\n**Explanation:** The checked "
        "source trail supports relational *maṇḍala* positions and changeable "
        "*ṣāḍguṇya* measures, not the exact sentence as a verified Kautilya quotation."
    )
    text = text.replace(old_mcq, new_mcq)

    text = text.replace(
        "**Thesis.** \"There is no permanent friend or permanent enemy\" states "
        "the\nstructural logic of Kautilya's *mandala*: in the circle of states "
        "only *interests*\nare permanent -- but this realism operates *within*, "
        "not against, the internal duty of *yogakshema* and *dharma*.",
        "**Thesis.** The printed line is best treated as the examiner's framing, "
        "not as a verified Kautilya quotation. Its defensible philosophical content "
        "is strategic flexibility: *maṇḍala* positions and *ṣāḍguṇya* choices "
        "change with power and interest, within the internal duty of *yogakṣema*.",
    )
    text = text.replace(
        "- **Locate the line.** It belongs to the *mandala* theory of external\n"
        "  sovereignty, where the immediate neighbour is a natural rival and the\n"
        "  neighbour's neighbour a natural ally. Friendship and enmity are "
        "*positions* in a\n  structure, so they shift as interests shift.",
        "- **Provenance before interpretation.** The question supplies the sentence; "
        "the checked local synopsis and Shamasastry passages do not verify that "
        "wording as Kautilya's. Use it as a thematic proposition, not a quotation.\n"
        "- **Interpretive route.** The *maṇḍala* makes friendship and enmity "
        "relational positions, while the six measures make policy responsive to "
        "relative power and circumstance.",
    )
    text = text.replace(
        "**Verdict.** On sovereignty, the statement captures Kautilya's insistence "
        "that\n*external* sovereignty is relational and interest-driven, while "
        "*internal*\nsovereignty remains a duty-bound science of order and welfare. "
        "Interests are\npermanent; the ethical frame of statecraft is not thereby "
        "abolished.",
        "**Verdict.** The statement is defensible as an examiner-supplied summary "
        "of strategic flexibility, not as authenticated wording. Kautilya's external "
        "sovereignty is relational and interest-sensitive, while internal rule "
        "remains tied to order and welfare.",
    )
    text = text.replace(
        "> MEMORY: Why this earns marks - it locates the quotation in the mandala "
        "doctrine,\n> unpacks it through sadgunya, and states the yogakshema/dharma "
        "limit rather than\n> treating the line as a self-evident endorsement of "
        "pure realpolitik.",
        "> MEMORY: Why this earns marks - it controls attribution before interpreting "
        "the prompt, then uses maṇḍala, ṣāḍguṇya and yogakṣema to give a sourced, "
        "qualified verdict.",
    )

    trap_anchor = (
        "15. **Do not develop Dworkin's principles/hard-cases argument in a "
        "sovereignty answer.** ⚠️ Name it as the next objection to Hart and route "
        "it; the doctrine is owned by Individual and State."
    )
    if "authenticated Kautilya quotation" not in text:
        text = text.replace(
            trap_anchor,
            trap_anchor
            + "\n16. **Do not omit permanence and universality from the standard "
            "five attributes.** ✅"
            + "\n17. **Do not equate popular with national sovereignty or majority "
            "preference.** ⚠️"
            + "\n18. **Do not call India a system of UK-style parliamentary "
            "sovereignty or call courts sovereign.** ✅"
            + "\n19. **Do not present the 2025 line as an authenticated Kautilya "
            "quotation.** ⚠️",
            1,
        )
    text = text.replace(
        "- **absolute power** ✅\n- **perpetual authority** ✅",
        "- **absolute power** ✅\n- **perpetual authority** ✅\n"
        "- **permanence / continuity** ✅\n- **universality** ✅",
        1,
    )
    closure_replacements = {
        (
            "KEY TERMS / DEFINITIONS: supreme final authority | internal and "
            "external sovereignty | legal and political sovereignty | de jure "
            "and de facto sovereignty | titular and actual sovereignty | monism "
            "and pluralism"
        ): (
            "KEY TERMS / DEFINITIONS: final authority | internal-external | "
            "legal-political | de jure-de facto | popular-national"
        ),
        (
            "KEY TERMS / DEFINITIONS: absolute and perpetual power | power to "
            "make and unmake law | indivisibility of sovereign title | legibus "
            "solutus | divine and natural law limits | fundamental laws "
            "(leges imperii)"
        ): (
            "KEY TERMS / DEFINITIONS: absolute | perpetual | indivisible | "
            "higher-law limits"
        ),
        (
            "KEY TERMS / DEFINITIONS: determinate human superior | habitual "
            "obedience of the bulk | command backed by sanction | absolute and "
            "illimitable | indivisible and inalienable | analytical jurisprudence"
        ): (
            "KEY TERMS / DEFINITIONS: superior | obedience | command | sanction | "
            "inalienable"
        ),
        (
            "KEY TERMS / DEFINITIONS: federalism objection | international law "
            "objection | customary law objection | popular sovereignty objection | "
            "Maine's Ranjit Singh example | degree-judgment on democracy"
        ): (
            "KEY TERMS / DEFINITIONS: federalism | international law | custom | "
            "democracy | constitutional supremacy"
        ),
        (
            "KEY TERMS / DEFINITIONS: hierarchy of norms | Grundnorm as "
            "presupposed basic norm | primary and secondary rules | rule of "
            "recognition | internal point of view | having an obligation versus "
            "being obliged"
        ): (
            "KEY TERMS / DEFINITIONS: norm hierarchy | Grundnorm | secondary "
            "rules | rule of recognition"
        ),
        (
            "KEY TERMS / DEFINITIONS: false, dangerous and unreal | state as one "
            "association among many | divided and shared authority | competition "
            "for allegiance | associational autonomy | pluralist, not anarchist"
        ): (
            "KEY TERMS / DEFINITIONS: pluralism | associations | shared authority | "
            "allegiance | coordination"
        ),
        (
            "KEY TERMS / DEFINITIONS: seven-limbed state (saptāṅga) | ruler "
            "(svāmī) as head | ministers, treasury and coercive force | calibrated "
            "coercion (daṇḍanīti) | law of the fish (mātsya-nyāya) | duty-bound, "
            "not illimitable"
        ): (
            "KEY TERMS / DEFINITIONS: saptāṅga | svāmī | daṇḍanīti | "
            "mātsya-nyāya | yogakṣema"
        ),
        (
            "KEY TERMS / DEFINITIONS: monism versus pluralism grid | location of "
            "final authority | absoluteness and divisibility | objection, reply, "
            "residual difficulty | Austin compared with Kautilya | Bodin compared "
            "with Austin"
        ): (
            "KEY TERMS / DEFINITIONS: monism | pluralism | comparison axes | "
            "objection-reply | residual"
        ),
        (
            "KEY TERMS / DEFINITIONS: erosion thesis | transformation and "
            "resilience thesis | pooled and negotiated sovereignty | legal "
            "independence versus practical interdependence | reconfigured, not "
            "abolished | graded verdict on relevance"
        ): (
            "KEY TERMS / DEFINITIONS: erosion | transformation | pooling | "
            "delegation | interdependence"
        ),
    }
    for old, new in closure_replacements.items():
        text = text.replace(old, new)

    text = text.replace(
        "- **titular / actual sovereignty** ✅",
        "- **titular / actual sovereignty** ✅\n"
        "- **popular / national sovereignty** ✅/⚠️\n"
        "- **parliamentary sovereignty / constitutional supremacy** ✅\n"
        "- **delegated / pooled sovereignty** ⚠️",
        1,
    )

    text = text.replace(
        "- O. P. Gauba, *An Introduction to Political Theory*.",
        "- O. P. Gauba, *An Introduction to Political Theory*, searchable local "
        "PDF pp. 179–218.",
    )
    text = text.replace(
        "- O. P. Gauba, *Socio-Political Philosophy*.",
        "- *Socio-Political Philosophy*, local compiled notes PDF pp. 55–67; no "
        "named author is asserted.",
    )
    if "https://www.parliament.uk/about/how/role/sovereignty/" not in text:
        text = text.replace(
            "- *Kesavananda Bharati v. State of Kerala* (Supreme Court judgment, "
            "**1973**), used only as a dated judicial illustration of a legally "
            "limited amending competence.",
            "- *Kesavananda Bharati v. State of Kerala* (Supreme Court judgment, "
            "**1973**), used only as a dated judicial illustration of a legally "
            "limited amending competence.\n"
            "- [Parliamentary sovereignty — UK Parliament]"
            "(https://www.parliament.uk/about/how/role/sovereignty/).\n"
            "- [The Constitution of India — Legislative Department]"
            "(https://www.legislative.gov.in/documents/constitution-of-india), "
            "especially Article 368.\n"
            "- [Official *Kesavananda Bharati* archive]"
            "(https://judgments.ecourts.gov.in/KBJ/).",
        )

    text = text.replace(
        "- Sovereignty = supreme, final, authoritative power; NOT force, government "
        "or the whole state.",
        "- Sovereignty = supreme, final, authoritative power; NOT force, government "
        "or the whole state.\n"
        "- Classical attributes = absoluteness, permanence, universality, "
        "inalienability and indivisibility.\n"
        "- Popular sovereignty concerns the source of authority; national sovereignty "
        "concerns collective self-determination.",
        1,
    )
    text = text.replace(
        "| 7 | Kautilya I: Saptanga, the Svami and Dandaniti |",
        "| 7 | Kautilya I: Seven-Limbed State (Saptanga), the Ruler (Svami) and "
        "Calibrated Coercion (Dandaniti) |",
        1,
    )
    text = text.replace(
        "| 8 | Kautilya II: Mandala, Sadgunya, Yogakshema and Modern Relevance |",
        "| 8 | Kautilya II: Circle of States (Mandala), Six-Fold Policy "
        "(Sadgunya), Security and Welfare (Yogakshema) |",
        1,
    )
    text = text.replace(
        "**The insights.** Sovereignty as *state capacity*: seven interdependent "
        "limbs with the *svami* as head; calibrated coercion (*dandaniti*) between "
        "anarchy and tyranny; external survival through the *mandala* circle and "
        "the six-fold *sadgunya* policy; and the overriding aim of *yogakshema* -- "
        "security plus the\n  welfare of subjects.",
        "**The insights.** Sovereignty as state capacity: the seven-limbed state "
        "(*saptāṅga*) with the ruler (*svāmī*) as head; calibrated coercion "
        "(*daṇḍanīti*) between anarchy and tyranny; external survival through the "
        "circle of states (*maṇḍala*) and six-fold policy (*ṣāḍguṇya*); and the "
        "aim of security and welfare (*yogakṣema*).",
    )
    text = text.replace(
        "        \"No permanent friend or permanent enemy\" -> only permanent INTERESTS.",
        "        2025 line -> examiner framing; interpret through strategic flexibility.",
    )
    text = text.replace(
        "- Four pairs: internal/external, legal/political, de jure/de facto,\n"
        "  titular/actual.",
        "- Four pairs: internal/external, legal/political, de jure/de facto,\n"
        "  titular/actual.\n"
        "- Five classical attributes: absoluteness, permanence, universality,\n"
        "  inalienability, indivisibility.\n"
        "- Popular sovereignty locates authority in the people; national sovereignty\n"
        "  concerns collective self-determination.",
        1,
    )
    text = text.replace(
        "- Pluralist, NOT anarchist; assessment: strong against absolutism, weak on "
        "the\n  state's coordinating necessity in crisis.",
        "- Pluralist, NOT anarchist; assessment: strong against absolutism, weak on "
        "the\n  state's coordinating necessity in crisis.\n"
        "- School bridge: Figgis (real associations), Cole (functional groups), "
        "MacIver\n  (law/constitution plus residual coordination); Laski remains "
        "the owner.",
        1,
    )
    text = text.replace(
        "- Mandala: neighbours are positional rivals, their neighbours positional "
        "allies ->\n  \"no permanent friend or enemy, only interests.\"",
        "- The 2025 line is prompt framing, not a verified Kautilya quotation.\n"
        "- Mandala and sadgunya support strategic flexibility as position, power and\n"
        "  interest change.",
        1,
    )
    text = text.replace(
        "- Legal independence != practical interdependence.",
        "- Legal independence != practical interdependence.\n"
        "- Distinguish treaty constraint, delegated competence, pooled decision and\n"
        "  material dependence; none automatically creates a global Austinian sovereign.",
        1,
    )
    text = text.replace(
        "**Explanation:** The coordination/finality objection: dispersed authority "
        "may be unable to deliver decisive collective action when it is most needed.",
        "**Explanation:** The coordination/finality objection remains decisive. "
        "MacIver's strongest reply preserves a residual coordinating state, while "
        "Figgis and Cole show why real associations cannot be reduced to state grants.",
        1,
    )
    text = text.replace(
        "**Explanation:** A state can be legally independent yet practically "
        "interdependent; separating the two answers the 2020 stem.",
        "**Explanation:** A state can be legally independent yet practically "
        "interdependent; treaty constraint, delegation, pooling and material "
        "dependence affect different competences and must not be collapsed.",
        1,
    )
    return text
_PILLS = len(GRAPHICAL_PILLS)
if _PILLS != 10:
    raise ValueError(f"Sovereignty requires exactly 10 graphical pill sets, found {_PILLS}.")
