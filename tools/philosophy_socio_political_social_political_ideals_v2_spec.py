"""Semantic-completeness successor spec for Social and Political Ideals."""

from __future__ import annotations

import re
from typing import Any

from regenerate_philosophy_socio_political_deep_review import TOPIC_1_CONTROLS


TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-01"
TOPIC_TITLE = "Social and Political Ideals"
TOPIC_NUMBER = 1
SECTION_KEY = "paper-ii-socio-political-philosophy"
GENERATION_DATE = "2026-09-03"
OFFICIAL_SYLLABUS_VERBATIM = (
    "Social and Political ldeals : Equality, Justice, Liberty."
)
HEADER_KICKER = (
    "Philosophy Optional | Paper II | Socio-Political Philosophy | Topic 01"
)
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
    "Social-Political-Ideals.md"
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
    "Socio-Political\\learning-sessions\\topic-01\\g5\\"
    "topic-01_Complete-Learning-Session_2026-08-30.md"
)
RETAINED_SESSION = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Socio-Political-Philosophy\\"
    "learning-sessions\\Social-Political-Ideals\\"
    "Social-Political-Ideals_Layered-Complete-Learning-Session_2026-08-19.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Socio-Political-Philosophy\\"
    "learning-sessions\\Social-Political-Ideals\\"
    "Social-Political-Ideals_Layered-Solved-Practice-Workbook_2026-08-19.md"
)
IMMUTABLE_GENERATION_PATHS = True


SESSION_TITLES = (
    "The Ideals Triad: Map, Working Thesis and the Ordering Problem",
    "Equality I: Equal Worth, the Four Forms, Opportunity vs Outcome",
    "Equality II: Rousseau, Mill and Marx on Inequality, Individuality and Need",
    "Equality III: Equality of What? — Sen, Cohen and Dworkin",
    "Liberty I: Meaning, Berlin's Two Concepts and Mill's Harm Principle",
    "Liberty II: Hobbes, Locke, Rousseau, Green and the Equality Relation",
    "Liberty III: Technological Society and Republican Non-Domination",
    "Justice I: Procedure, Substance, Classical Forms and Corrective Justice",
    "Justice II: Rawls, Nozick, Sen, Ambedkar and the Ordering Verdict",
    "Debates, Criticisms, PYQ Traps and Integrated Verdicts",
)


def _session_spec(title: str, control: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": title,
        "plain": control["plain"],
        "technical": control["technical"],
        "answer": control["opening"],
        "keywords": list(control["keywords"]),
        "usage": control["usage"],
        "mechanism": control["mechanism"],
        "consequence": control["consequence"],
        "trap": control["trap"],
        "objection": control["objection"],
        "reply": control["reply"],
        "limit": control["limit"],
        "exam": control["usage"],
        "revision": [
            control["plain"],
            control["mechanism"],
            control["consequence"],
            control["trap"],
        ],
        "visuals": [
            {
                "title": f"{title} — argument rail",
                "lines": [
                    f"START -> {control['plain']}",
                    f"MECHANISM -> {control['mechanism']}",
                    f"VERDICT -> {control['consequence']}",
                ],
                "caption": "A compact claim–mechanism–verdict route.",
            }
        ],
    }


SESSION_SPECS = [
    _session_spec(title, control)
    for title, control in zip(SESSION_TITLES, TOPIC_1_CONTROLS)
]
ADVANCED_SESSION_TITLES = SESSION_TITLES


ASCII_PANELS = (
    {
        "title": "Printed clause boundary and the ideals triad",
        "structural_type": "ownership gate and triadic map",
        "sessions": (1,),
        "lines": (
            "OFFICIAL OWNER -> Equality, Justice and Liberty only",
            "EQUALITY asks in what respect persons must count as equals",
            "LIBERTY asks which protected choices and capacities agency requires",
            "JUSTICE asks what is due, by which rule and through which procedure",
            "democracy and citizenship enter only as the 2018 PYQ setting",
            "rights, duties, sovereignty and government retain their later owners",
            "thesis -> distinct ideals, institutionally interdependent",
        ),
    },
    {
        "title": "Individual claims and social institutions",
        "structural_type": "two-level comparison matrix",
        "sessions": (1,),
        "lines": (
            "INDIVIDUAL EQUALITY -> equal moral worth and equal concern",
            "SOCIAL EQUALITY -> no arbitrary status hierarchy or inherited stigma",
            "INDIVIDUAL LIBERTY -> protected thought, choice and self-direction",
            "SOCIAL LIBERTY -> usable options plus freedom from domination",
            "INDIVIDUAL JUSTICE -> due treatment, reasons and rectification",
            "INSTITUTIONAL JUSTICE -> fair procedure, distribution and status order",
            "bridge -> legality may exist without legitimacy",
        ),
    },
    {
        "title": "Equality from formal status to substantive opportunity",
        "structural_type": "progressive equality ladder",
        "sessions": (2,),
        "lines": (
            "equal moral worth -> birth hierarchy bears the burden of justification",
            "formal or legal equality -> the same public legal status",
            "political equality -> citizenship, vote and eligibility for office",
            "social equality -> freedom from caste rank, stigma and humiliation",
            "economic equality -> fair background conditions and life chances",
            "formal opportunity -> offices are legally open",
            "fair opportunity -> access is realistically usable",
            "outcome concern -> thresholds and least-advantaged protection",
        ),
    },
    {
        "title": "Rousseau Mill and Marx on socially produced inequality",
        "structural_type": "three-thinker causal comparison",
        "sessions": (3,),
        "lines": (
            "ROUSSEAU -> natural difference becomes domination through convention",
            "moral-political inequality -> wealth, honour, power and dependence",
            "MILL -> equal civic status and women's equality with individuality",
            "manufactured subordination cannot prove natural inferiority",
            "MARX -> formally equal exchange can conceal class exploitation",
            "equal right can reproduce inequality when needs differ",
            "higher communist rule -> contribution by ability, distribution by need",
        ),
    },
    {
        "title": "Equality of what and the metric decision",
        "structural_type": "metric decision tree",
        "sessions": (4,),
        "lines": (
            "DWORKIN -> resources; brute luck differs from option luck",
            "SEN -> capability asks what persons are actually able to do and be",
            "conversion conditions make equal resources yield unequal freedom",
            "COHEN -> an unequal ethos can defeat formally just institutions",
            "LUCK EGALITARIANISM -> correct brute-luck disadvantage",
            "RELATIONAL EQUALITY -> end hierarchy and second-class standing",
            "trap -> capability is not equal income or identical functioning",
        ),
    },
    {
        "title": "Berlin Mill and the justified limit of coercion",
        "structural_type": "liberty distinction and harm test",
        "sessions": (5,),
        "lines": (
            "NEGATIVE LIBERTY -> freedom from interference",
            "POSITIVE LIBERTY -> self-direction and being one's own master",
            "Berlin warns against coercion for an alleged true or rational self",
            "MILL -> coercion needs prevention of harm to others",
            "self-regarding conduct receives a presumption of liberty",
            "offence, dislike and paternal benefit are not automatically harm",
            "answer test -> who is free, from what, to do what, under whose power",
        ),
    },
    {
        "title": "Law security autonomy and effective freedom",
        "structural_type": "four-thinker liberty rail",
        "sessions": (6,),
        "lines": (
            "HOBBES -> order secures residual liberty where law is silent",
            "LOCKE -> known law protects rights against arbitrary government",
            "ROUSSEAU -> autonomy is civic self-legislation through general will",
            "GREEN -> freedom includes effective capacity for worthwhile action",
            "poverty, ignorance and dependency can hollow non-interference",
            "equality can enable liberty by reducing dependency",
            "limit -> enabling provision must not become perfectionist compulsion",
        ),
    },
    {
        "title": "Technology and republican non-domination",
        "structural_type": "standing-power diagnostic",
        "sessions": (7,),
        "lines": (
            "technology expands communication, association and knowledge",
            "surveillance and platform dependence create standing power",
            "INTERFERENCE is an act; DOMINATION is uncontrolled capacity",
            "Pettit -> an indulgent master can dominate without interfering",
            "contestable interest-tracking law can constitute freedom",
            "Code on Wages commenced 21-Nov-2025; status is not implementation",
            "PYQ route -> liberty is realisable only under accountable power",
        ),
    },
    {
        "title": "Formal procedural and substantive justice",
        "structural_type": "three-form justice matrix",
        "sessions": (8,),
        "lines": (
            "FORMAL JUSTICE -> apply announced principles consistently",
            "PROCEDURAL JUSTICE -> fair hearing, publicity and impartial process",
            "SUBSTANTIVE JUSTICE -> just principle, distribution and status relation",
            "fair procedure can reproduce unjust starting conditions",
            "substantive correction without due process can become arbitrary",
            "best synthesis -> fair procedure plus defensible substantive criteria",
            "LEGAL JUSTICE -> impartial law and moral assessment of law",
            "POLITICAL JUSTICE -> equal citizenship, voice and non-arbitrary power",
            "SOCIO-ECONOMIC JUSTICE -> fair burdens, benefits and real opportunity",
            "RECOGNITION-STATUS JUSTICE -> no stigma or second-class standing",
            "legality identifies validity; legitimacy asks moral justification",
        ),
    },
    {
        "title": "Plato Aristotle utilitarianism and corrective repair",
        "structural_type": "classical justice comparison",
        "sessions": (8,),
        "lines": (
            "PLATO -> harmony when each part performs its proper function",
            "objection -> functional harmony can freeze hierarchy",
            "ARISTOTLE DISTRIBUTIVE -> proportion by a relevant criterion",
            "criteria -> need, desert, merit, contribution, equality, compensation",
            "ARISTOTLE CORRECTIVE -> arithmetic restoration after a wrong",
            "UTILITARIANISM -> aggregate welfare risks sacrificing separate persons",
            "justice needs allocation, procedure, substance and rectification",
        ),
    },
    {
        "title": "Rawls Nozick Sen and Ambedkar",
        "structural_type": "modern justice debate grid",
        "sessions": (9,),
        "lines": (
            "RAWLS -> original position and veil model fair choice",
            "equal basic liberties have lexical priority",
            "fair equality of opportunity precedes the difference principle",
            "NOZICK -> acquisition, transfer and rectification, not a pattern",
            "SEN -> capability and public reasoning compare remediable injustice",
            "institutional justice differs from realised justice in actual lives",
            "AMBEDKAR -> political democracy needs equality and fraternity",
        ),
    },
    {
        "title": "Fourteen PYQs and the executable answer spine",
        "structural_type": "directive and evidence rail",
        "sessions": (10,),
        "lines": (
            "OWNER CORPUS -> 14 verified parts across every year 2018-2025",
            "DEFINE -> strongest sense of the ideal in the stem",
            "DISTINGUISH -> metric, interference, procedure, substance or repair",
            "ARGUE -> claim, named thinker or example, analysis, qualification",
            "COUNTER -> strongest objection and best reply",
            "COMPARE -> run both positions down shared axes",
            "HOW FAR -> state the conditions under which the claim holds and fails",
            "END -> justice orders liberty and equality without replacing either",
        ),
    },
)


REQUIRED_TERMS = (
    "Social and Political ldeals : Equality, Justice, Liberty.",
    "equal moral worth",
    "formal equality",
    "substantive equality",
    "equality of opportunity",
    "equality of outcome",
    "negative liberty",
    "positive liberty",
    "harm principle",
    "non-domination",
    "formal justice",
    "procedural justice",
    "substantive justice",
    "legal justice",
    "political justice",
    "socio-economic justice",
    "recognition/status justice",
    "distributive justice",
    "corrective justice",
    "justice as fairness",
    "entitlement theory",
    "legality",
    "legitimacy",
    "rights and duties",
    "citizenship and democracy",
    "Code on Wages",
    "S.O. 5322(E)",
    "exactly **14** primary parts",
)


def _extract_owner_section(owner_text: str, start: str, end: str) -> str:
    match = re.search(
        rf"(?ms)^{re.escape(start)}\s*$.*?(?=^{re.escape(end)}\s*$)",
        owner_text,
    )
    if not match:
        raise ValueError(f"Cannot extract owner section {start!r}.")
    return match.group(0).strip()


def _demote_boundary(fragment: str) -> str:
    return re.sub(
        r"(?m)^(#{2,3})\s+",
        lambda match: "#" * (len(match.group(1)) + 1) + " ",
        fragment,
    )


def _demote_justice(fragment: str) -> str:
    return re.sub(r"(?m)^###\s+", "##### ", fragment)


def transform_assembled(
    text: str,
    *,
    owner_text: str,
    generation: int,
) -> str:
    if generation != 6:
        raise ValueError(f"Topic 01 semantic successor is pinned to g6, got g{generation}.")

    text = re.sub(
        r"(?m)^!\[Social and Political Ideals equality-liberty-justice concept map\]"
        r"\(assets/philosophy-paper-ii-socio-political-philosophy-01/"
        r"social-political-ideals-triad\.png\)\s*\n+"
        r"\*Concept map: equality supplies equal standing, liberty protects agency, "
        r"and justice orders their institutional relationship\.\*\s*\n*",
        "",
        text,
        count=1,
    )

    boundary = _demote_boundary(
        _extract_owner_section(
            owner_text,
            "## Exact ownership boundary and indispensable bridges",
            "## 0. ONE-SCREEN MAP",
        )
    )
    justice = _demote_justice(
        _extract_owner_section(
            owner_text,
            "### 3.1A Formal, procedural and substantive justice",
            "### 3.2 Plato: justice as each doing one's own work",
        )
    )

    text = text.replace(
        "- **Canonical doctrine source:** "
        "`upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/"
        "Social-Political-Ideals.md` (9,542 words), sliced verbatim into the "
        "CORE UPSC layers (each canonical teaching passage exactly once) and "
        "preserved again, in full, in the canonical apparatus block.",
        "- **Canonical doctrine source:** "
        "`upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/"
        "Social-Political-Ideals.md`, repaired under the ten-gate semantic-"
        "completeness protocol and promoted into this immutable successor.",
    )
    text = text.replace(
        "> **Syllabus (verbatim):** Social and Political Ideals : Equality, "
        "Justice, Liberty.",
        "> **Syllabus (verbatim):** Social and Political ldeals : Equality, "
        "Justice, Liberty.",
    )
    text = text.replace(
        "Justice (Plato and Aristotle; the criteria problem; corrective and "
        "compensatory justice; utilitarian justice; Rawls, Nozick, Sen and "
        "Ambedkar);",
        "Justice (formal, procedural and substantive justice; legal, political, "
        "socio-economic and recognition/status dimensions; Plato and Aristotle; "
        "corrective and compensatory justice; utilitarian justice; Rawls, Nozick, "
        "Sen and Ambedkar);",
    )
    preservation = (
        "**Preservation note:** the canonical doctrine is reorganised into layers, "
        "never compressed. Every doctrine, numbered argument, objection/reply, "
        "comparison, corpus-depth delta, PYQ route, directive rule, graded verdict "
        "and provenance caution is retained; simplification means adding accessible "
        "gateways, not deleting complexity."
    )
    if "### Exact ownership boundary and indispensable bridges" not in text:
        text = text.replace(preservation, preservation + "\n\n" + boundary, 1)

    text = text.replace(
        "| 8 | Justice I: Meaning, Plato, Aristotle, the Criteria Problem and "
        "Corrective Justice |",
        "| 8 | Justice I: Procedure, Substance, Classical Forms and Corrective "
        "Justice |",
        1,
    )
    text = text.replace(
        "**Technical definition:** Plato treats justice as harmony, Aristotle "
        "distinguishes distributive proportion from corrective restoration, and "
        "utilitarianism tests institutions by aggregate welfare.",
        "**Technical definition:** Justice must distinguish formal consistency, "
        "procedural fairness and substantive rightness before comparing Plato's "
        "harmony, Aristotle's distribution and correction, and utilitarian welfare.",
        1,
    )
    if "##### 3.1A Formal, procedural and substantive justice" not in text:
        text = text.replace(
            "##### 3.2 Plato: justice as each doing one's own work",
            justice + "\n\n##### 3.2 Plato: justice as each doing one's own work",
            1,
        )

    old_law = (
        "✅ The Bonded Labour System (Abolition) Act, **1976** is an **enacted "
        "statute** that legally dissolves a relation of personal dependence; ✅ "
        "the Minimum Wages Act, **1948** and the Sexual Harassment of Women at "
        "Workplace (Prevention, Prohibition and Redressal) Act, **2013** are "
        "enacted statutes that replace employer discretion with rule-governed "
        "entitlement and complaint machinery."
    )
    new_law = (
        "✅ The Bonded Labour System (Abolition) Act, **1976** legally attacks a "
        "relation of personal dependence; ✅ the Sexual Harassment of Women at "
        "Workplace (Prevention, Prohibition and Redressal) Act, **2013** replaces "
        "unchecked discretion with rule-governed duties and complaint machinery; "
        "and ✅ Gazette notification **S.O. 5322(E), 21 November 2025** brought "
        "the relevant provisions of the Code on Wages, **2019**, including its "
        "repeal-and-savings framework, into force."
    )
    text = text.replace(old_law, new_law)
    text = text.replace(
        "Enactment is not implementation, and none of these establishes that "
        "domination has in fact ended;",
        "Enactment or commencement is not implementation, and none of these "
        "establishes that domination has ended;",
    )

    text = text.replace(
        "- Plato: justice = harmony; each part/class its own function.\n"
        "- Aristotle: distributive (proportional equality) + corrective (arithmetic\n"
        "  equality).",
        "- Formal justice = consistent application; procedural justice = fair "
        "decision process; substantive justice = defensible principle, outcome "
        "and status order.\n"
        "- Legal, political and socio-economic justice are distinct but connected; "
        "recognition enters here only as equal civic standing.\n"
        "- Plato: justice = harmony; each part/class its own function.\n"
        "- Aristotle: distributive (proportional equality) + corrective (arithmetic\n"
        "  equality).",
        1,
    )
    text = text.replace(
        "9. **Trap:** Collapsing justice into law. - **Correction:** legality may "
        "diverge from legitimacy; justice evaluates law itself.",
        "9. **Trap:** Collapsing justice into law or fair procedure. - "
        "**Correction:** legality may diverge from legitimacy, and procedural "
        "regularity may coexist with substantive injustice.",
    )
    text = text.replace(
        "correction: legality may diverge from legitimacy; justice evaluates law itself.",
        "correction: legality may diverge from legitimacy, and fair procedure may "
        "still preserve substantive injustice.",
    )
    closure_replacements = {
        (
            "KEY TERMS / DEFINITIONS: natural inequality | moral-political "
            "inequality | individuality | manufactured subordination | "
            "distribution according to need"
        ): (
            "KEY TERMS / DEFINITIONS: natural inequality | social hierarchy | "
            "individuality | need"
        ),
        (
            "KEY TERMS / DEFINITIONS: absence of impediment | liberty under law | "
            "general will | self-legislation | positive freedom"
        ): (
            "KEY TERMS / DEFINITIONS: Hobbesian liberty | liberty under law | "
            "general will | positive freedom"
        ),
        (
            "KEY TERMS / DEFINITIONS: justice as harmony | distributive justice | "
            "corrective justice | relevant criterion | aggregate welfare"
        ): (
            "KEY TERMS / DEFINITIONS: procedure | substance | distribution | "
            "correction"
        ),
        (
            "KEY TERMS / DEFINITIONS: original position | difference principle | "
            "entitlement theory | capability approach | social democracy"
        ): (
            "KEY TERMS / DEFINITIONS: original position | difference principle | "
            "entitlement | capability"
        ),
    }
    for old, new in closure_replacements.items():
        text = text.replace(old, new)

    text = text.replace(
        "#### MCQ 40\n\nThe claim 'justice is not identical to law' means that:\n\n"
        "A. all laws are necessarily unjust\n"
        "B. justice is whatever the sovereign commands\n"
        "C. legality and legitimacy are the same thing\n"
        "D. a legally valid rule can still be unjust - legality is not sufficient "
        "for justice\n\n"
        "**Correct answer: D** — a legally valid rule can still be unjust - "
        "legality is not sufficient for justice\n"
        "**Explanation:** Legal validity and moral justice can diverge; conflating "
        "them collapses the critical standpoint from which laws are judged unjust.",
        "#### MCQ 40\n\nWhich statement correctly distinguishes procedural from "
        "substantive justice?\n\n"
        "A. A consistent procedure guarantees a just principle and outcome\n"
        "B. Substantive justice makes hearing and impartiality unnecessary\n"
        "C. The two expressions are always exact synonyms\n"
        "D. Fair procedure is necessary, but unjust starting conditions or "
        "principles still require substantive scrutiny\n\n"
        "**Correct answer: D** — fair procedure is necessary, but unjust starting "
        "conditions or principles still require substantive scrutiny\n"
        "**Explanation:** Procedural justice evaluates how a decision is produced; "
        "substantive justice evaluates the governing principle, distribution and "
        "status relation. Neither can safely replace the other.",
    )

    text = text.replace(
        "that\n  say which inequalities are justified and which liberties are "
        "basic. Compare the\n",
        "that\n  say which inequalities are justified and which liberties are "
        "basic. They also require fair procedures: an impartial process cannot "
        "cleanse an unjust starting structure, while substantive correction cannot "
        "dispense with hearing, publicity and consistent limits. Compare the\n",
        1,
    )

    text = text.replace(
        "- O. P. Gauba, *An Introduction to Political Theory*.",
        "- O. P. Gauba, *An Introduction to Political Theory*, searchable local "
        "PDF pp. 367–412 and 432–453.\n"
        "- *Socio-Political Philosophy*, searchable local PDF pp. 7–11, 25–40 "
        "and 47–54.\n"
        "- Robert Audi (ed.), *The Cambridge Dictionary of Philosophy*, searchable "
        "local PDF pp. 489–490 and 536.",
    )
    text = text.replace(
        "https://www.indiacode.nic.in/handle/123456789/1911?view_type=browse",
        "https://www.indiacode.nic.in/handle/123456789/11219?locale=en",
    )
    if "https://egazette.gov.in/WriteReadData/2025/267885.pdf" not in text:
        source_anchor = (
            "- [The Constitution of India — Legislative Department]"
            "(https://www.legislative.gov.in/documents/constitution-of-india/"
            "constitution-of-india-AjN2EjMtQWa?pageTitle=Constitution-of-India), "
            "Articles 14–16, used as dated constitutional illustration only."
        )
        additions = (
            "- [The Sexual Harassment of Women at Workplace Act, 2013 — India "
            "Code](https://www.indiacode.nic.in/handle/123456789/17057), used only "
            "as a complaint-mechanism illustration.\n"
            "- [Code on Wages commencement notification S.O. 5322(E), 21 November "
            "2025 — Gazette of India]"
            "(https://egazette.gov.in/WriteReadData/2025/267885.pdf), used only "
            "for current legal-status control."
        )
        text = text.replace(source_anchor, additions + "\n" + source_anchor)

    text = text.replace(
        "- Aristotle: DISTRIBUTIVE (proportional) + CORRECTIVE (arithmetic).",
        "- Justice taxonomy: FORMAL consistency -> PROCEDURAL fairness -> "
        "SUBSTANTIVE rightness; legal, political, socio-economic and bounded "
        "recognition/status dimensions.\n"
        "- Aristotle: DISTRIBUTIVE (proportional) + CORRECTIVE (arithmetic).",
        1,
    )
    return text
