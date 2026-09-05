"""Learner-v2 authored content spec: Philosophy Optional Paper II -- Socio-Political
Philosophy -- Gender Discrimination (topic key: philosophy-paper-ii-socio-political-
philosophy-09).

Provenance / grounding:
  - Canonical owner: upsc-ai-kit/knowledge/Philosophy/paper-2/socio-political/
    Gender-Discrimination.md (648 lines) -- sole source of doctrinal claims, PYQ
    routing, evidence units, traps, and legal-status qualifications.
  - PYQ ledger: upsc-ai-kit/knowledge/Philosophy/paper-2/_PYQ-SocioPolitical-2018-2025.md
  - Advanced dossier: upsc-ai-kit/knowledge/Philosophy/_advanced/Socio-Political-Dossier.md, section 9.
  - Modelled on tools/philosophy_socio_political_crime_and_punishment_v2_spec.py
    (SESSION_SPECS / ASCII_PANELS / REQUIRED_CORE_TERMS shapes only; the
    GRAPHICAL_* constant families from that model file are intentionally NOT
    replicated here).

This module is a pure data module. It performs no I/O, no generation, and no
publishing. It is consumed by downstream generator tooling (out of scope for
this file) and is validated here only via py_compile plus local assertions at
the bottom of the file guarded by `if __name__ == "__main__":`.
"""

from __future__ import annotations

import re
from typing import Any

TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-09"
TOPIC_TITLE = "Gender Discrimination"
TOPIC_NUMBER = 9
SECTION_KEY = "paper-ii-socio-political-philosophy"
GENERATION_DATE = "2026-09-03"
OFFICIAL_SYLLABUS_VERBATIM = (
    "Gender Discrimination : Female Foeticide, Land and Property Rights; Empowerment."
)
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
    "Gender-Discrimination.md"
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
    "Socio-Political\\learning-sessions\\topic-09\\g6\\"
    "topic-09_Complete-Learning-Session_2026-09-03.md"
)
ASSET_SLUG = "gender-discrimination"
IMMUTABLE_GENERATION_PATHS = True

HEADER_KICKER = "Philosophy Optional - Paper II - Socio-Political Philosophy - Topic 9"

SESSION_SPECS: list[dict[str, Any]] = [
    {
        "title": "Sex, Gender and Beauvoir's 'Other'",
        "plain": (
            "Sex is the biological fact of being male or female; gender is what a "
            "society decides that biological fact should mean -- roles, virtues, "
            "and limits. Simone de Beauvoir's line 'One is not born, but rather "
            "becomes, a woman' says the second part is made, not given."
        ),
        "technical": (
            "Beauvoir's existentialist-feminist claim treats 'woman' as a social "
            "category constituted by being cast as Other against a male Self/Subject "
            "norm. This is the founding move that separates sex (biological "
            "difference) from gender (constructed meaning), against essentialist "
            "readings that collapse the two."
        ),
        "answer": (
            "Open by stating the sex/gender distinction, cite Beauvoir's becoming "
            "thesis and the Self/Other structure, then show what work the "
            "distinction does for a discrimination argument: if gender is made, "
            "gender discrimination is a remediable social fact, not a natural order."
        ),
        "keywords": [
            "sex versus gender",
            "simone de beauvoir",
            "the second sex",
            "the other",
            "biological-difference objection",
            "essentialism objection",
        ],
        "usage": (
            "Define sex versus gender, anchor the distinction in Simone de "
            "Beauvoir's Other, test the biological-difference and essentialism "
            "objections, and conclude whether the discrimination is natural or "
            "socially remediable."
        ),
        "mechanism": (
            "Othering mechanism: the male is posited as the neutral Subject/norm; "
            "the female is defined only relationally, as what the Subject is not -- "
            "this relational deficit is then read back onto women as natural "
            "inferiority, naturalising a social hierarchy."
        ),
        "consequence": (
            "Once woman is fixed as Other, her subordination looks like a fact "
            "about her nature rather than an effect of a social structure, which "
            "forecloses reform and stabilises unequal treatment as 'just how "
            "things are.'"
        ),
        "trap": (
            "Do not conflate 'sex is biological' with 'gender discrimination is "
            "biologically justified' -- the whole point of the distinction is that "
            "the second does not follow from the first."
        ),
        "objection": (
            "Biological-difference objection: reproductive and physiological "
            "differences are real and cannot be wished away, so some differential "
            "treatment reflects nature, not discrimination."
        ),
        "reply": (
            "Beauvoir and successors concede biological difference but deny that it "
            "fixes social meaning; the leap from 'physically different' to "
            "'socially unequal' is a cultural inference, not a logical entailment, "
            "and it is precisely that inference gender theory contests."
        ),
        "limit": (
            "The sex/gender split can itself be criticised (see Session 2) for "
            "smuggling back a 'raw' biological sex that is not itself culturally "
            "innocent -- flag this as an internal tension rather than resolve it "
            "here."
        ),
        "exam": (
            "Secondary anchor for 2025 Q1(b) (gender as social construct) and 2019 "
            "Q3(b) (man-made concept, not naturally endowed) -- use this session to "
            "supply the Beauvoir citation those answers need."
        ),
        "revision": [
            "Sex = biological; gender = social meaning attached to sex.",
            "Beauvoir: 'One is not born, but rather becomes, a woman.'",
            "Woman constructed as Other against male Subject/norm.",
            "Othering naturalises hierarchy as if it were biological fact.",
            "Biological-difference objection: real physiological differences exist.",
            "Reply: difference does not entail differential social worth.",
            "Distinction enables discrimination to be seen as remediable, not natural.",
            "Watch for the internal tension explored fully in Session 2.",
        ],
        "visuals": [
            {
                "title": "Self / Other Construction",
                "lines": [
                    "  MALE NORM (Self/Subject)",
                    "        |",
                    "        |  defines by negation",
                    "        v",
                    "  FEMALE (constructed as Other)",
                    "        |",
                    "        v",
                    "  relational deficit read as 'natural' inferiority",
                    "  CATEGORY CARE: sex characteristics != assignment != identity/expression/role",
                ],
                "caption": (
                    "Shows how Beauvoir's Self/Other structure converts a "
                    "relational position into an apparently natural hierarchy."
                ),
            }
        ],
    },
    {
        "title": "Gender as a Cultural Category and Butler's Performativity",
        "plain": (
            "Judith Butler goes further than Beauvoir: gender is not a fixed inner "
            "identity expressed outwardly but something produced by repeating "
            "gestures, speech, and styles -- 'performativity,' not a single act of "
            "performance."
        ),
        "technical": (
            "Gender Trouble argues gender is constituted through 'performative "
            "repetition' of stylised acts within a regulatory frame; there is no "
            "gendered substance behind the acts -- the doing is the being. This "
            "unsettles any stable, pre-social sex/gender binary."
        ),
        "answer": (
            "State the shift from Beauvoir's 'becoming' to Butler's 'performative "
            "repetition,' then use it to answer whether gender is culturally, not "
            "biologically, constituted -- performativity supplies the mechanism "
            "Beauvoir's account leaves underspecified."
        ),
        "keywords": [
            "gender as a cultural category",
            "judith butler",
            "gender performativity",
            "gender trouble",
            "performative repetition",
            "discursive construction",
        ],
        "usage": (
            "Deploy when a question explicitly opposes 'gender as cultural "
            "category' to 'sex as biological category,' or asks how gender is "
            "produced rather than merely defined."
        ),
        "mechanism": (
            "Repetition mechanism: norms of masculinity/femininity are reiterated "
            "in everyday acts (dress, speech, comportment); each repetition both "
            "produces the appearance of a natural gender and disciplines deviation "
            "from it."
        ),
        "consequence": (
            "If gender is performed rather than expressed, it is in principle "
            "unstable and open to subversive repetition -- but also means "
            "discrimination is reproduced daily through ordinary social practice, "
            "not only through law."
        ),
        "trap": (
            "Do not present performativity as 'people choosing to perform gender "
            "like an act on a stage' -- Butler explicitly denies a prior chooser; "
            "the subject is itself an effect of the repetition."
        ),
        "objection": (
            "Essentialism objection: without any stable pre-discursive sex, "
            "feminism loses the very subject ('woman') in whose name it claims to "
            "act, risking political incoherence."
        ),
        "reply": (
            "Butler answers that provisional, strategic use of 'woman' as a "
            "political category remains available even without metaphysical "
            "fixity -- solidarity does not require essence, only a shared "
            "discursive position worth contesting."
        ),
        "limit": (
            "Performativity explains how gender norms are reproduced but is "
            "criticised for being weaker on why particular norms (rather than "
            "others) become hegemonic -- economic and institutional accounts "
            "(Sessions 6-8) supply that missing structural piece."
        ),
        "exam": (
            "Primary anchor for 2019 Q3(b) and 2022 Q3(b) (gender as cultural vs "
            "sex as biological category); secondary support for 2025 Q1(b)."
        ),
        "revision": [
            "Butler: gender is performative, not expressive of an inner essence.",
            "Performative repetition of stylised acts constitutes gender.",
            "No gendered substance exists prior to or behind the acts.",
            "Repetition both produces and disciplines gender appearance.",
            "Essentialism objection: risk of losing 'woman' as a stable subject.",
            "Reply: strategic, provisional use of 'woman' still grounds solidarity.",
            "Performativity explains reproduction, less so origin of specific norms.",
            "Directly answers 'gender as cultural category vs sex as biological.'",
        ],
        "visuals": [
            {
                "title": "Performative Repetition Loop",
                "lines": [
                    "   stylised act --> read as natural --> repeated",
                    "        ^                                   |",
                    "        |___________________________________|",
                    "        (regulatory norm reinforced each cycle)",
                ],
                "caption": (
                    "Illustrates Butler's claim that gender is an effect of "
                    "repeated performance, not an expression of prior essence."
                ),
            }
        ],
    },
    {
        "title": "Feminist Diagnoses and the Architecture of Equality",
        "plain": (
            "Different feminist schools diagnose the root cause of women's "
            "subordination differently (law, economy, culture, sexuality), and "
            "'equality' itself splits into formal, substantive, and relational "
            "versions with different remedies."
        ),
        "technical": (
            "The equality typology (formal, substantive, relational; equality of "
            "opportunity vs equality of outcome) determines what counts as a "
            "remedy: formal equality bars differential rules, substantive equality "
            "permits affirmative action to correct starting-point disadvantage."
        ),
        "answer": (
            "Set out the equality typology first, then use it to adjudicate "
            "whether feminism aims at empowerment (substantive, outcome-sensitive) "
            "or equality (formal, rule-neutral) -- and show the two are not "
            "mutually exclusive."
        ),
        "keywords": [
            "formal equality",
            "substantive equality",
            "relational equality",
            "equality of opportunity",
            "equality of outcome",
            "affirmative action",
        ],
        "usage": (
            "Use for any question forcing a choice between 'feminism as "
            "empowerment' and 'feminism as equality,' or asking to evaluate "
            "reservation/affirmative-action style remedies."
        ),
        "mechanism": (
            "Formal equality removes explicit legal differentiation; substantive "
            "equality additionally compensates for unequal starting points via "
            "targeted measures; relational equality asks whether social "
            "relationships themselves remain hierarchical despite equal rules."
        ),
        "consequence": (
            "Choosing formal equality alone can leave real disadvantage "
            "untouched (equal treatment of unequals reproduces inequality); "
            "choosing substantive equality invites the reverse-discrimination "
            "objection."
        ),
        "trap": (
            "Do not treat 'equality' as one univocal idea -- an answer that fails "
            "to specify which equality is at stake will look conceptually loose "
            "to an examiner."
        ),
        "objection": (
            "Reverse-discrimination objection: affirmative measures for women "
            "amount to discrimination against men, and adaptive preference "
            "arguments (women 'choosing' subordinate roles under constrained "
            "options) can be used to deny inequality exists at all."
        ),
        "reply": (
            "Substantive-equality theorists reply that correcting a structural "
            "disadvantage is not equivalent to creating a new one, and that "
            "'choice' made under adaptive preference does not settle whether the "
            "background options were themselves just."
        ),
        "limit": (
            "The typology clarifies remedies but does not by itself settle *how "
            "much* substantive correction is warranted -- that judgement is "
            "made contextually, using the domain-specific sessions (foeticide, "
            "property, political representation) that follow."
        ),
        "exam": (
            "Primary anchor for 2018 Q4(c) (empowerment vs equality); secondary "
            "support for 2025 Q1(b)."
        ),
        "revision": [
            "Formal equality: no explicit differential rule.",
            "Substantive equality: compensates unequal starting points.",
            "Relational equality: asks if social relations remain hierarchical.",
            "Equality of opportunity vs equality of outcome is a related axis.",
            "Affirmative action is a substantive-equality remedy.",
            "Reverse-discrimination objection targets affirmative measures.",
            "Adaptive preference objection can mask real constraint as 'choice.'",
            "Empowerment and equality are not mutually exclusive goals.",
        ],
        "visuals": [
            {
                "title": "Equality Typology Table",
                "lines": [
                    "  TYPE          | REMEDY               | RISK",
                    "  formal        | equal rule            | ignores start-point gap",
                    "  substantive   | targeted correction   | reverse-discrimination charge",
                    "  relational    | restructure relations | hardest to operationalise",
                    "  SAMENESS risk -> male pattern hidden as neutral",
                    "  DIFFERENCE risk -> accommodation hardens into essence",
                    "  JUSTICE -> redistribution + recognition + representation",
                ],
                "caption": (
                    "Compares the three equality types against their typical "
                    "remedy and the objection each remedy attracts."
                ),
            }
        ],
    },
    {
        "title": "Female Foeticide: Doctrine, Distinctions, Causes and Missing Women",
        "plain": (
            "Female foeticide is the sex-selective abortion of female fetuses. It "
            "must be kept distinct from female infanticide (killing after birth) "
            "and dowry-linked violence, and it is driven by son preference operating "
            "through technology, not by technology alone."
        ),
        "technical": (
            "Amartya Sen's 'missing women' argument uses skewed sex ratios as "
            "evidence of large-scale discrimination against women across South and "
            "East Asia; in India this is channelled through prenatal sex "
            "determination misuse despite the PCPNDT Act, 1994 prohibiting it."
        ),
        "answer": (
            "Distinguish foeticide/infanticide/dowry-death precisely, cite Sen's "
            "missing-women statistic-as-argument (not a specific invented number), "
            "name the PCPNDT Act 1994 as the enacted legal response, and conclude "
            "that son preference (a gender-discrimination attitude), not technology "
            "per se, is the causal driver."
        ),
        "keywords": [
            "female foeticide",
            "sex-selective abortion",
            "sex ratio at birth",
            "missing women",
            "amartya sen",
            "pcpndt act 1994",
        ],
        "usage": (
            "Define female foeticide as sex-selective abortion, use Amartya "
            "Sen's missing-women diagnosis, locate son preference before "
            "technology in the causal chain, classify the PCPNDT Act 1994, and "
            "end with a law-plus-substantive-equality verdict."
        ),
        "mechanism": (
            "Son preference (rooted in dowry economics, patrilineal inheritance "
            "expectations, and old-age security norms) creates demand; prenatal "
            "diagnostic technology supplies the means; weak enforcement of the "
            "PCPNDT Act, 1994 fails to close the gap between demand and act."
        ),
        "consequence": (
            "A skewed child sex ratio at birth, treated by Sen as an index of "
            "systemic discrimination rather than an isolated crime, with "
            "downstream effects on marriage markets and women's bargaining "
            "position."
        ),
        "trap": (
            "Do not blame 'technology' as the primary cause -- the question '2021 "
            "Q4(b)' explicitly tests whether you will resist this simplification; "
            "technology is the instrument, son preference is the cause."
        ),
        "objection": (
            "One could object that stringent law alone (PCPNDT Act) should have "
            "solved the problem, so continued prevalence shows the diagnosis "
            "(son preference, not technology) must be wrong."
        ),
        "reply": (
            "Persistence despite legal prohibition supports, rather than refutes, "
            "the son-preference diagnosis: law changes formal permissibility, not "
            "the underlying discriminatory preference structure that drives "
            "demand around the law (a formal- vs substantive-equality point from "
            "Session 3)."
        ),
        "limit": (
            "This session documents doctrine and diagnosis; it does not assert "
            "any specific unverified statistic on national sex ratio or districtwise "
            "figures -- cite only the direction of skew and the named policy "
            "instruments (PCPNDT Act 1994, Beti Bachao Beti Padhao 2015)."
        ),
        "exam": (
            "Primary anchor for 2018 Q4(b), 2021 Q4(b), and 2023 Q3(c); secondary "
            "linkage into 2024 Q4(a)'s empowerment-and-foeticide question."
        ),
        "revision": [
            "Female foeticide = sex-selective abortion; keep distinct from infanticide.",
            "Amartya Sen: 'missing women' as an index of systemic discrimination.",
            "PCPNDT Act, 1994 prohibits prenatal sex determination for selection.",
            "Beti Bachao Beti Padhao (2015) is the named policy-response scheme.",
            "Cause = son preference; technology is only the instrument.",
            "Son preference is rooted in dowry, inheritance and old-age-security norms.",
            "Legal prohibition persisting alongside the practice supports, not refutes, the diagnosis.",
            "Never cite an invented sex-ratio figure; name direction and instruments only.",
        ],
        "visuals": [
            {
                "title": "Foeticide Causal Chain",
                "lines": [
                    "  son preference (discriminatory attitude)",
                    "        |",
                    "        v",
                    "  demand for sex determination",
                    "        |         (PCPNDT Act 1994 prohibits)",
                    "        v",
                    "  sex-selective abortion  -->  skewed sex ratio at birth",
                ],
                "caption": (
                    "Places son preference, not technology, as the causal root, "
                    "with the PCPNDT Act positioned as the (imperfectly enforced) "
                    "legal barrier."
                ),
            }
        ],
    },
    {
        "title": "Land and Property Rights: Agarwal's Five Levels and the Legal Record",
        "plain": (
            "Bina Agarwal argues that owning land 'on paper' is not enough for "
            "women's empowerment; actual command must be tested through legal "
            "title, access/use, control, realised return, and exit/security."
        ),
        "technical": (
            "Agarwal's five-level analysis (legal title / access-use / control / "
            "return / exit-security) disaggregates property rights into separable "
            "components. Legal title is neither necessary nor sufficient for "
            "actual command: informal access may exist without title, while title "
            "may yield no control, income, benefit or bargaining security."
        ),
        "answer": (
            "State the five-level analysis, map India's legal record onto it (Hindu "
            "Succession Act, 2005 amendment giving daughters coparcenary rights; "
            "*Vineeta Sharma v. Rakesh Sharma*, 2020 as a Supreme Court judgment "
            "clarifying that amendment, not itself a statute), then assess title, "
            "access, control, realised return and exit/security separately."
        ),
        "keywords": [
            "bina agarwal",
            "five-level analysis of land rights",
            "title access control return exit",
            "coparcenary",
            "hindu succession act 2005",
            "vineeta sharma v rakesh sharma 2020",
        ],
        "usage": (
            "State Bina Agarwal's five-level analysis, test legal title, "
            "access/use, control, return and exit/security, classify the Hindu Succession "
            "Act 2005 and Vineeta Sharma 2020 correctly, and conclude whether "
            "formal coparcenary title becomes effective empowerment."
        ),
        "mechanism": (
            "The Hindu Succession Act, 2005 amendment strengthens legal title, "
            "but actual command depends separately on practical access/use, "
            "decision-making control, receipt of income and benefit, and the "
            "asset's capacity to provide fall-back security against abandonment "
            "or violence."
        ),
        "consequence": (
            "Where custom, family pressure, or lack of enforcement blocks the "
            "other dimensions, women can hold title while male relatives retain "
            "effective control -- a gap between de jure and de facto empowerment."
        ),
        "trap": (
            "Do not cite *Vineeta Sharma* as if it created the coparcenary right -- "
            "it is a 2020 Supreme Court judgment interpreting/clarifying the 2005 "
            "amendment's retrospective application; the statutory right itself "
            "dates to the 2005 amendment."
        ),
        "objection": (
            "One could object that once law grants equal title, any remaining gap "
            "is a social/enforcement problem outside philosophy's remit, not a "
            "flaw in the rights framework itself."
        ),
        "reply": (
            "Agarwal's reply is that a rights framework which stops at title "
            "while ignoring predictable social non-implementation is philosophically "
            "incomplete; empowerment theory must build access, control, return "
            "and exit/security into "
            "the very specification of the right, not treat them as separate "
            "'implementation' add-ons."
        ),
        "limit": (
            "This session states the doctrinal and legal-status facts precisely; "
            "for a current, narrowly illustrative example of courts extending "
            "inheritance logic to a further community context, see the optional "
            "CURRENT_ANCHOR note attached to this session (illustration only, not "
            "load-bearing doctrine)."
        ),
        "exam": (
            "Primary anchor for 2021 Q1(e) and 2023 Q1(c) (land/property rights "
            "and empowerment)."
        ),
        "revision": [
            "Agarwal's five levels: legal title, access/use, control, return, exit/security.",
            "Legal title is neither necessary nor sufficient for actual command over land.",
            "Hindu Succession Act, 2005 amendment: daughters get coparcenary rights.",
            "Vineeta Sharma v. Rakesh Sharma (2020): SC judgment clarifying the amendment's application -- not the source statute.",
            "De jure title can coexist with de facto male control.",
            "Return asks who receives income/benefit; exit/security asks whether land strengthens the fall-back position.",
            "Objection: gap is 'mere' enforcement, not a rights-framework flaw.",
            "Reply: a complete rights framework must design in access, control, return and exit/security.",
        ],
        "visuals": [
            {
                "title": "Agarwal's Five-Level Analysis",
                "lines": [
                    "   LEGAL TITLE   (recognised in law or record)",
                    "   ACCESS / USE  (practical ability to use the asset)",
                    "   CONTROL       (decide cropping, leasing, sale or investment)",
                    "   RETURN        (receive the income and benefit)",
                    "   EXIT/SECURITY (fall-back protection against abandonment or violence)",
                ],
                "caption": (
                    "The five dimensions are analytically separate: title can "
                    "exist without command, while some access can exist without title."
                ),
            },
            {
                "title": "Indian Legal Instruments on Inheritance -- Status Table",
                "lines": [
                    "  INSTRUMENT                         | KIND      | STATUS",
                    "  Hindu Succession Act 2005 amendment| statute   | enacted, coparcenary right",
                    "  Vineeta Sharma v Rakesh Sharma 2020| SC ruling | father alive not required",
                    "  Ram Charan & Ors v Sukhram & Ors   | SC ruling | illustration only, ST context,",
                    "  [2025] 8 SCR 272 / 2025 INSC 865   |           | decided 17-Jul-2025, distinct bench",
                ],
                "caption": (
                    "Distinguishes statute from judgment and marks the 2025 "
                    "ruling as a scoped illustration, not a doctrinal expansion."
                ),
            },
        ],
    },
    {
        "title": "Empowerment: Dimensions of Power and Kabeer's Resources-Agency-Achievements",
        "plain": (
            "Empowerment is more than having resources; Naila Kabeer defines it as "
            "the process by which those denied the ability to make strategic life "
            "choices acquire that ability, running through resources, agency, and "
            "achievements."
        ),
        "technical": (
            "Kabeer's tripartite model treats resources (pre-conditions) and "
            "agency (the ability to define and act on goals) as jointly producing "
            "achievements (functioning outcomes); power itself is analysed via "
            "power-over, power-to, power-with, and power-within registers. Martha "
            "Nussbaum's capability approach supplies the complementary test of "
            "whether a dignity-compatible threshold of real opportunity exists."
        ),
        "answer": (
            "Introduce Kabeer's resources-agency-achievements chain, name the four "
            "power registers, and use the chain to test whether a given policy "
            "(land title, employment scheme, reservation) empowers or merely "
            "resources women without building agency."
        ),
        "keywords": [
            "empowerment",
            "naila kabeer",
            "resources agency achievements",
            "power over",
            "power to",
            "power with and power within",
            "martha nussbaum",
        ],
        "usage": (
            "Define empowerment through Naila Kabeer's resources-agency-"
            "achievements chain, distinguish power-over, power-to, power-with "
            "and power-within, apply Martha Nussbaum's capability threshold, "
            "test the policy's weakest link, and give a qualified verdict."
        ),
        "mechanism": (
            "Resources (material, human, social) enable but do not guarantee "
            "agency; agency (decision-making, negotiation, resistance) must be "
            "separately exercised to convert resources into achievements "
            "(actual improved functioning and status)."
        ),
        "consequence": (
            "Interventions that deliver resources without cultivating agency "
            "(e.g. a bank account never controlled by the woman herself) produce "
            "no real gain in empowerment on Kabeer's test."
        ),
        "trap": (
            "Do not treat 'access to a resource' as synonymous with "
            "'empowerment' -- Kabeer's whole contribution is to insert agency as "
            "the necessary intermediate link."
        ),
        "objection": (
            "A critic could argue the model is too demanding: if agency is "
            "required in addition to resources, almost no policy will count as "
            "empowering, making the concept practically useless."
        ),
        "reply": (
            "Kabeer's reply is that the model is diagnostic, not a "
            "pass/fail gate -- it lets analysts locate exactly where an "
            "intervention breaks down (resource delivery vs agency-building vs "
            "achievement) rather than declaring policy failure wholesale."
        ),
        "limit": (
            "Kabeer's model explains individual-level empowerment mechanics; it "
            "is complemented, not replaced, by the care-ethics and political-"
            "representation limits taken up in the next session."
        ),
        "exam": (
            "Primary anchor for 2024 Q4(a) (empowerment as a condition for "
            "gender equality); secondary support for 2018 Q4(c)."
        ),
        "revision": [
            "Empowerment = process of acquiring the ability to make strategic life choices.",
            "Kabeer's chain: resources -> agency -> achievements.",
            "Resources are pre-conditions, not the empowerment itself.",
            "Agency is the necessary intermediate, exercised capacity to choose/act.",
            "Achievements are the resulting functioning outcomes.",
            "Four power registers: power-over, power-to, power-with, power-within.",
            "Resource delivery without agency-building fails Kabeer's test.",
            "The model is diagnostic: it locates where an intervention breaks down.",
        ],
        "visuals": [
            {
                "title": "Kabeer's Empowerment Chain",
                "lines": [
                    "  RESOURCES  -->   AGENCY   -->  ACHIEVEMENTS",
                    " (material,      (ability to     (improved",
                    "  human, social)  choose & act)   functioning)",
                    "",
                    "  break at any link = no real empowerment gain",
                ],
                "caption": (
                    "Resources alone are insufficient; agency is the load-"
                    "bearing middle link converting resources into achievements."
                ),
            }
        ],
    },
    {
        "title": "Care Ethics, the Limits of Empowerment and Political Representation",
        "plain": (
            "Carol Gilligan's ethic of care questions whether justice-as-rights "
            "frameworks capture women's moral reasoning, while the record on "
            "political representation shows legal empowerment (reservation) is "
            "necessary but not sufficient without real decision-making power."
        ),
        "technical": (
            "Gilligan's ethic of care, grounded in relational responsibility "
            "rather than abstract rights-adjudication, is used to critique "
            "purely resource/rights-based empowerment models; the 106th "
            "Constitutional Amendment, 2023 (women's reservation in "
            "legislatures) illustrates the further, delimitation-conditional gap "
            "between legal entitlement and effective empowerment."
        ),
        "answer": (
            "Introduce Gilligan's care ethic as a supplement/critique of rights-"
            "based empowerment, then test the 106th Amendment, 2023 against "
            "Kabeer's agency criterion -- noting precisely that its reservation "
            "is enacted but implementation is conditional on subsequent "
            "delimitation, so legal empowerment and effective empowerment can "
            "diverge in time as well as in kind."
        ),
        "keywords": [
            "care ethics",
            "carol gilligan",
            "ethic of care",
            "political representation",
            "106th constitutional amendment 2023",
            "delimitation",
        ],
        "usage": (
            "Contrast Carol Gilligan's care ethics with a rights-only model, "
            "classify the 106th Constitutional Amendment 2023, explain the "
            "delimitation condition, test legal against effective political "
            "representation, and close with the residual empowerment limit."
        ),
        "mechanism": (
            "Care ethics relocates moral reasoning in maintaining relationships "
            "and responsiveness to particular others rather than applying "
            "abstract universal rules; applied to representation, it asks "
            "whether reserved seats translate into responsive, agentic "
            "participation or remain symbolic if delimitation delays or dilutes "
            "actual seat allocation."
        ),
        "consequence": (
            "A state can be legally empowering (constitutional reservation "
            "exists) while remaining practically unrealised (seats not yet "
            "allotted pending delimitation), reproducing the title-without-"
            "control problem seen with land rights (Session 5) at the political "
            "level."
        ),
        "trap": (
            "Do not describe the 106th Amendment as already fully operational in "
            "seat allocation -- state precisely that its women's-reservation "
            "provision is enacted law whose implementation is conditional on a "
            "subsequent delimitation exercise; overstating current effect is a "
            "factual error."
        ),
        "objection": (
            "One could object that care ethics, by emphasising relational "
            "responsibility, risks re-inscribing the very caregiving role that "
            "trapped women in unequal domestic labour in the first place."
        ),
        "reply": (
            "Gilligan and successors reply that recognising care as a valuable "
            "moral orientation is compatible with also demanding it be shared "
            "across genders and properly weighted in public reasoning -- the aim "
            "is to add care to justice, not to confine women back to it."
        ),
        "limit": (
            "This session shows empowerment's political-representation limit; it "
            "does not extend to disputing the 106th Amendment's constitutional "
            "validity, only to precisely qualifying its present implementation "
            "status."
        ),
        "exam": (
            "Primary anchor, jointly with Session 6, for 2020 Q4(a) and 2024 "
            "Q4(a)."
        ),
        "revision": [
            "Gilligan's ethic of care: relational responsibility vs abstract rights.",
            "Care ethics supplements, and can critique, rights-based empowerment models.",
            "106th Constitutional Amendment, 2023 enacts legislative reservation for women.",
            "Implementation is conditional on a subsequent delimitation exercise -- not yet self-executing.",
            "Legal empowerment and effective/political empowerment can diverge in time.",
            "Objection: care ethics risks re-confining women to caregiving roles.",
            "Reply: the aim is shared care plus justice, not care instead of justice.",
            "Do not overstate 106th Amendment as immediately fully operational.",
        ],
        "visuals": [
            {
                "title": "Legal vs Effective Empowerment Gap",
                "lines": [
                    "  106th Amendment: enacted 2023; commenced 16-Apr-2026",
                    "        |",
                    "        v  (conditional on)",
                    "  ARTICLE 334A CENSUS/DELIMITATION SEQUENCE",
                    "        |",
                    "        v",
                    "  seat allocation / effective representation: PENDING 03-Sep-2026",
                ],
                "caption": (
                    "Marks the precise gap between an enacted legal entitlement "
                    "and its still-pending, delimitation-conditional effect."
                ),
            }
        ],
    },
    {
        "title": "Feminist Schools in Debate: Marxist, Socialist, Radical, Pateman and Okin",
        "plain": (
            "Feminist schools disagree about the root cause of women's "
            "subordination: Marxist feminists point to capitalism, radical "
            "feminists to patriarchy as an independent system, socialist "
            "feminists to both together, and Pateman and Okin extend the "
            "critique into the social contract and the family itself."
        ),
        "technical": (
            "Marxist feminism derives gender oppression from capitalist property "
            "relations and women's unpaid reproductive labour; radical feminism "
            "treats patriarchy as an autonomous system of male domination "
            "irreducible to class; socialist feminism proposes a 'dual systems' "
            "account combining both; Pateman's 'sexual contract' argues the "
            "social contract tradition presupposes prior male domination over "
            "women, and Okin's 'family as an object of justice' argues Rawlsian "
            "justice cannot bracket the unjust internal distribution of power "
            "within families."
        ),
        "answer": (
            "State each school's causal diagnosis (capitalism / patriarchy / "
            "both), then bring in Pateman and Okin to show the debate extends "
            "beyond economic structure into the very contract-theoretic and "
            "family-based foundations of political obligation and justice."
        ),
        "keywords": [
            "marxist feminism",
            "socialist feminism",
            "radical feminism",
            "dual systems theory",
            "carole pateman and the sexual contract",
            "okin: family as object of justice",
        ],
        "usage": (
            "Compare Marxist, radical and socialist feminism by root cause, use "
            "dual systems theory to test socialism's sufficiency, add Carole "
            "Pateman's sexual contract and Okin's family-as-justice critique, "
            "then adjudicate the strongest diagnosis rather than listing schools."
        ),
        "mechanism": (
            "Marxist feminism: capitalist need for unpaid reproductive/domestic "
            "labour subordinates women structurally. Radical feminism: male "
            "control operates through sexuality, violence, and reproduction, "
            "independent of economic system. Dual systems theory: capitalism and "
            "patriarchy operate as two interacting but analytically distinct "
            "systems. Pateman: contract theory's 'free and equal' contractors "
            "presuppose a prior sexual contract subordinating women. Okin: "
            "justice theories that stop at the household's front door leave its "
            "internal power distribution unexamined and thus unjust."
        ),
        "consequence": (
            "If patriarchy is autonomous of capitalism (radical/dual-systems "
            "view), then abolishing capitalism alone (a purely socialist "
            "transformation) will not by itself abolish gender subordination -- "
            "directly answering the 'gender equality within a socialist regime' "
            "PYQ."
        ),
        "trap": (
            "Do not treat 'socialist feminism' and 'Marxist feminism' as "
            "synonyms -- socialist feminism's distinguishing move is precisely "
            "the dual-systems synthesis with an independent patriarchy axis, "
            "which orthodox Marxist feminism does not grant."
        ),
        "objection": (
            "A Marxist could object that patriarchy itself has historically "
            "arisen from and is sustained by property relations, so treating it "
            "as an independent system is analytically redundant."
        ),
        "reply": (
            "Radical/dual-systems feminists reply that patriarchal control over "
            "sexuality and reproduction predates and persists across different "
            "modes of production (including actually existing socialist states), "
            "which is empirical evidence for its analytic independence."
        ),
        "limit": (
            "This session states the inter-school debate as doctrine; it does "
            "not adjudicate a single winner -- an exam answer should present the "
            "disagreement and take a reasoned, argued position rather than "
            "assert one school as simply correct."
        ),
        "exam": (
            "Primary anchor for 2019 Q1(e) (gender equality within a socialist "
            "regime); also grounds ORIGINAL_MAINS on Pateman vs Okin."
        ),
        "revision": [
            "Marxist feminism: capitalism as root cause via unpaid reproductive labour.",
            "Radical feminism: patriarchy as an autonomous system, not reducible to class.",
            "Socialist/dual-systems feminism: capitalism and patriarchy as two interacting systems.",
            "Pateman: the 'sexual contract' underlies and is masked by the social contract.",
            "Okin: family must be treated as an object of justice, not a private exemption.",
            "PYQ test: can gender equality be realised within a socialist regime alone?",
            "Dual-systems answer: no, if patriarchy is independent of economic system.",
            "Do not conflate Marxist and socialist feminism -- the dual-systems move differs.",
        ],
        "visuals": [
            {
                "title": "Feminist Schools -- Root-Cause Comparison",
                "lines": [
                    "  SCHOOL      | ROOT CAUSE                | IMPLICATION",
                    "  liberal     | law/custom/education      | Wollstonecraft; Mill/Taylor",
                    "  existential | woman constituted as Other| Beauvoir: situation, not destiny",
                    "  marxist     | capitalism                | end capitalism -> end oppression",
                    "  radical     | patriarchy (autonomous)   | end patriarchy directly",
                    "  socialist   | capitalism + patriarchy   | must address both systems",
                    "  pateman/okin| contract & family design  | justice must reach the household",
                ],
                "caption": (
                    "Contrasts each school's causal diagnosis with its implied "
                    "remedy, showing why 'socialism alone' is contested as a "
                    "sufficient fix."
                ),
            }
        ],
    },
    {
        "title": "Gender, Caste and Multiculturalism: The Indian Intersection",
        "plain": (
            "Gender discrimination does not act alone -- caste, religion, and "
            "community norms combine with gender to produce compounded "
            "disadvantage, and multicultural accommodation of group practices can "
            "itself conflict with women's equality within that group."
        ),
        "technical": (
            "Kimberle Crenshaw's intersectionality shows that caste-gender "
            "disadvantage is not merely additive but produces distinct, "
            "structurally located harms; Susan Moller Okin's question 'Is "
            "multiculturalism bad for women?' presses whether group-cultural "
            "accommodation by the state can entrench internal patriarchal "
            "practice under the banner of protecting minority culture."
        ),
        "answer": (
            "Introduce intersectionality to show caste and gender compound "
            "rather than merely add; then apply Okin's multiculturalism test to "
            "ask whether a given accommodation of group practice should yield to "
            "women's equality claims within that group, using India's caste-"
            "gender record as the operative example."
        ),
        "keywords": [
            "intersectionality",
            "kimberle crenshaw",
            "caste and gender",
            "multiculturalism",
            "is multiculturalism bad for women",
            "structural injustice",
        ],
        "usage": (
            "Define intersectionality through Kimberle Crenshaw, show why caste "
            "and gender produce a distinct structural injustice, apply Okin's "
            "multiculturalism test to cultural accommodation, answer the "
            "self-governance objection, and conclude through equal citizenship."
        ),
        "mechanism": (
            "Intersectional mechanism: caste position determines which forms of "
            "gender discrimination a woman faces (e.g. differential exposure to "
            "violence, labour exploitation, or land denial) such that 'women' as "
            "a single undifferentiated class obscures caste-specific harm. "
            "Multiculturalism mechanism: state deference to 'group rights' or "
            "personal-law autonomy can shield internally patriarchal norms from "
            "the equality scrutiny applied elsewhere in the same polity."
        ),
        "consequence": (
            "A purely gender-only analysis, or a purely caste-only analysis, "
            "each under-describes the harm actually experienced by women at that "
            "intersection; policy calibrated to only one axis will systematically "
            "miss the other."
        ),
        "trap": (
            "Do not present 'women' in the Indian context as a homogeneous "
            "category -- an answer that ignores caste stratification within "
            "gender discrimination will be marked as analytically thin on a "
            "synthesis question."
        ),
        "objection": (
            "A multiculturalist could object that state intervention into group "
            "practices in the name of gender equality is itself a form of "
            "majoritarian or statist overreach into legitimate cultural "
            "self-governance."
        ),
        "reply": (
            "Okin's reply is that a state committed to equal citizenship cannot "
            "consistently exempt any group's internal practice from the equality "
            "standard applied elsewhere -- protecting a culture cannot mean "
            "protecting some of its members' domination of others."
        ),
        "limit": (
            "This session names the intersectional and multiculturalism "
            "problems precisely as live tensions; the optional Advanced module on "
            "Iris Marion Young's structural-injustice model extends, but is not "
            "required for, this core synthesis."
        ),
        "exam": (
            "Synthesis anchor: no single dedicated PYQ, but this session equips "
            "answers to 2018 Q4(c) and 2024 Q4(a) with an intersectional "
            "dimension the pure equality/empowerment sessions alone do not "
            "supply."
        ),
        "revision": [
            "Intersectionality (Crenshaw): caste and gender compound, not merely add.",
            "'Women' in India is not a homogeneous analytic category.",
            "Okin's test: is multiculturalism bad for women?",
            "State deference to group/personal-law autonomy can shield internal patriarchy.",
            "Objection: intervention is majoritarian overreach into cultural self-governance.",
            "Reply: equal citizenship cannot exempt any group's internal domination.",
            "Caste-specific harms are missed by gender-only or caste-only analysis.",
            "Advanced (optional) link: Iris Marion Young's structural injustice model.",
        ],
        "visuals": [
            {
                "title": "Intersection of Caste and Gender",
                "lines": [
                    "INTERSECTIONALITY changes the MECHANISM; it is not arithmetic addition",
                    "  CASTE      -> endogamy, labour, land and status",
                    "  CLASS      -> work, services, time and bargaining resources",
                    "  COMMUNITY  -> external vulnerability + possible internal authority",
                    "  DISABILITY -> access, dependency and substituted decision-making",
                    "  SEXUALITY / GENDER IDENTITY -> stigma and compulsory role policing",
                    "  Crenshaw: intersectional method | hooks: margin-to-centre warning",
                    "  single-axis policy misses the institutionally distinct harm",
                ],
                "caption": (
                    "Depicts intersectionality's claim that the caste-gender "
                    "cell is a distinct harm-location, not a simple sum of two "
                    "separate axes."
                ),
            },
            {
                "title": "Okin's Multiculturalism Dilemma Test",
                "lines": [
                    "  group practice claims cultural protection",
                    "        |",
                    "        v",
                    "  does it entrench internal gender hierarchy?",
                    "     /            \\",
                    "   NO              YES",
                    "    |                |",
                    " accommodate    equality claim overrides accommodation",
                ],
                "caption": (
                    "A decision test for whether a cultural-accommodation claim "
                    "should yield to an internal gender-equality claim."
                ),
            },
        ],
    },
    {
        "title": "Integrated Answer Architecture: Directive Decoder, Evidence Bank and PYQ Routing",
        "plain": (
            "This closing session is not new doctrine but the toolkit for "
            "writing exam answers: how to read the directive word, which "
            "evidence to cite for which claim, and how every prior PYQ routes "
            "into the nine content sessions above."
        ),
        "technical": (
            "Synthesises the owner file's keyword bank, seventeen documented "
            "traps, and PYQ-routing table into a single answer-construction "
            "spine usable across 10-, 15-, and 20-mark directive formats."
        ),
        "answer": (
            "For any gender-discrimination prompt: (1) decode the directive word "
            "(discuss/examine/analyse/critically evaluate), (2) select the "
            "correct primary session(s) via the routing logic below, (3) deploy "
            "objection-reply structure from that session, (4) close with a "
            "verdict that is qualified, not absolute."
        ),
        "keywords": [
            "directive decoder",
            "evidence bank",
            "pyq routing",
            "objection-reply structure",
            "answer architecture",
            "verdict qualification",
        ],
        "usage": (
            "Run the directive decoder, select from the evidence bank through "
            "PYQ routing, build the answer architecture around an objection-"
            "reply structure, and end with an explicitly qualified verdict."
        ),
        "mechanism": (
            "Routing mechanism: match the PYQ's key noun phrase (foeticide -> "
            "Session 4; property/land -> Session 5; empowerment -> Sessions 6-7; "
            "'man-made'/'cultural category' -> Sessions 1-2; "
            "equality-vs-empowerment framing -> Session 3; socialist regime -> "
            "Session 8; unmarked synthesis/caste framing -> Session 9) to the "
            "session holding the load-bearing doctrine, then borrow that "
            "session's objection/reply pair intact."
        ),
        "consequence": (
            "Systematic routing prevents two common failures: citing the wrong "
            "thinker for a given claim, and writing a purely descriptive answer "
            "with no objection-reply movement, which examiners mark down for "
            "lacking critical engagement."
        ),
        "trap": (
            "Do not answer every gender-discrimination question with the same "
            "generic Beauvoir-Butler opening regardless of what is actually "
            "asked -- route to the specific session(s) the directive requires "
            "and lead with that content instead."
        ),
        "objection": (
            "A student might object that memorising a routing table is "
            "mechanical and does not itself generate original philosophical "
            "insight."
        ),
        "reply": (
            "The routing table is scaffolding, not substitute content -- it "
            "ensures the correct doctrine is retrieved under time pressure so "
            "that the scarce exam minutes can be spent on the objection-reply "
            "and verdict, which is where original engagement actually happens."
        ),
        "limit": (
            "This session assumes the content of Sessions 1-9 is already "
            "learned; it organises retrieval and presentation, it does not "
            "introduce any doctrine not already established above."
        ),
        "exam": (
            "Applies to all 12 verified PYQs (2018-2025) and to all "
            "ORIGINAL_MAINS prompts defined in this module."
        ),
        "revision": [
            "Step 1: decode the directive word before writing anything.",
            "Step 2: route the prompt's key phrase to its primary session.",
            "Step 3: borrow that session's objection-reply pair intact.",
            "Step 4: close with a qualified verdict, never an unqualified absolute.",
            "Foeticide keywords route to Session 4; property keywords to Session 5.",
            "Empowerment keywords route to Sessions 6-7; socialist-regime keywords to Session 8.",
            "'Man-made'/'cultural category' keywords route to Sessions 1-2.",
            "Unmarked synthesis or caste framing routes to Session 9.",
        ],
        "visuals": [
            {
                "title": "PYQ Keyword Router",
                "lines": [
                    "  PROMPT KEYWORD           -> PRIMARY SESSION",
                    "  foeticide                -> 4",
                    "  land / property          -> 5",
                    "  empowerment              -> 6 / 7",
                    "  man-made / cultural cat. -> 1 / 2",
                    "  equality vs empowerment  -> 3",
                    "  socialist regime         -> 8",
                    "  caste / synthesis        -> 9",
                ],
                "caption": (
                    "A one-glance retrieval map from a prompt's key noun phrase "
                    "to the session holding its load-bearing doctrine."
                ),
            }
        ],
    },
]

ASCII_PANELS: list[dict[str, Any]] = [
    {
        "title": "Self / Other Construction",
        "structural_type": "flow",
        "sessions": [1],
        "lines": [
            "  MALE NORM (Self/Subject)",
            "        |  defines by negation",
            "        v",
            "  FEMALE (constructed as Other)",
            "        |",
            "        v",
            "  relational deficit read as 'natural' inferiority",
        ],
    },
    {
        "title": "Performative Repetition Loop",
        "structural_type": "cycle",
        "sessions": [2],
        "lines": [
            "   stylised act --> read as natural --> repeated",
            "        ^                                   |",
            "        |___________________________________|",
            "        (regulatory norm reinforced each cycle)",
        ],
    },
    {
        "title": "Equality Typology Table",
        "structural_type": "table",
        "sessions": [3],
        "lines": [
            "  TYPE          | REMEDY               | RISK",
            "  formal        | equal rule            | ignores start-point gap",
            "  substantive   | targeted correction   | reverse-discrimination charge",
            "  relational    | restructure relations | hardest to operationalise",
        ],
    },
    {
        "title": "Foeticide Causal Chain",
        "structural_type": "flow",
        "sessions": [4],
        "lines": [
            "  son preference (discriminatory attitude)",
            "        |",
            "        v",
            "  demand for sex determination",
            "        |         (PCPNDT Act 1994 prohibits)",
            "        v",
            "  sex-selective abortion  -->  skewed sex ratio at birth",
        ],
    },
    {
        "title": "Agarwal's Five-Level Analysis",
        "structural_type": "hierarchy",
        "sessions": [5],
        "lines": [
            "   LEGAL TITLE   (recognised in law or record)",
            "   ACCESS / USE  (practical ability to use the asset)",
            "   CONTROL       (decide cropping, leasing, sale or investment)",
            "   RETURN        (receive the income and benefit)",
            "   EXIT/SECURITY (fall-back protection against abandonment or violence)",
        ],
    },
    {
        "title": "Indian Legal Instruments on Inheritance -- Status Table",
        "structural_type": "table",
        "sessions": [5],
        "lines": [
            "  INSTRUMENT                         | KIND      | STATUS",
            "  Hindu Succession Act 2005 amendment| statute   | enacted, coparcenary right",
            "  Vineeta Sharma v Rakesh Sharma 2020| SC ruling | father alive not required",
            "  Ram Charan & Ors v Sukhram & Ors   | SC ruling | illustration only, ST context,",
            "  [2025] 8 SCR 272 / 2025 INSC 865   |           | decided 17-Jul-2025, distinct bench",
        ],
    },
    {
        "title": "Kabeer's Empowerment Chain",
        "structural_type": "flow",
        "sessions": [6],
        "lines": [
            "  RESOURCES  -->   AGENCY   -->  ACHIEVEMENTS",
            " (material,      (ability to     (improved",
            "  human, social)  choose & act)   functioning)",
            "",
            "  break at any link = no real empowerment gain",
        ],
    },
    {
        "title": "Legal vs Effective Empowerment Gap",
        "structural_type": "flow",
        "sessions": [7],
        "lines": [
            "  106th Amendment: enacted 2023; commenced 16-Apr-2026",
            "        |",
            "        v  (conditional on)",
            "  ARTICLE 334A CENSUS/DELIMITATION SEQUENCE",
            "        |",
            "        v",
            "  seat allocation / effective representation: PENDING 03-Sep-2026",
        ],
    },
    {
        "title": "Feminist Schools -- Root-Cause Comparison",
        "structural_type": "table",
        "sessions": [8],
        "lines": [
            "  SCHOOL      | ROOT CAUSE                | IMPLICATION",
            "  marxist     | capitalism                | end capitalism -> end oppression",
            "  radical     | patriarchy (autonomous)   | end patriarchy directly",
            "  socialist   | capitalism + patriarchy   | must address both systems",
            "  pateman/okin| contract & family design  | justice must reach the household",
        ],
    },
    {
        "title": "Intersection of Caste and Gender",
        "structural_type": "matrix",
        "sessions": [9],
        "lines": [
            "        GENDER axis  ---------->",
            "  CASTE   |  low-caste woman: compounded, distinct harm",
            "  axis    |  (not simply 'caste harm' + 'gender harm')",
            "    |",
            "    v",
            "  single-axis policy (gender-only OR caste-only) misses this cell",
        ],
    },
    {
        "title": "Okin's Multiculturalism Dilemma Test",
        "structural_type": "decision_tree",
        "sessions": [9],
        "lines": [
            "  group practice claims cultural protection",
            "        |",
            "        v",
            "  does it entrench internal gender hierarchy?",
            "     /            \\",
            "   NO              YES",
            "    |                |",
            " accommodate    equality claim overrides accommodation",
        ],
    },
    {
        "title": "PYQ Keyword Router",
        "structural_type": "table",
        "sessions": [10],
        "lines": [
            "  PROMPT KEYWORD           -> PRIMARY SESSION",
            "  foeticide                -> 4",
            "  land / property          -> 5",
            "  empowerment              -> 6 / 7",
            "  man-made / cultural cat. -> 1 / 2",
            "  equality vs empowerment  -> 3",
            "  socialist regime         -> 8",
            "  caste / synthesis        -> 9",
        ],
    },
]

REQUIRED_TERMS: list[str] = [
    "sex versus gender",
    "simone de beauvoir",
    "the second sex",
    "the other",
    "biological-difference objection",
    "gender as a cultural category",
    "judith butler",
    "gender performativity",
    "gender trouble",
    "performative repetition",
    "essentialism objection",
    "discursive construction",
    "patriarchy",
    "formal equality",
    "substantive equality",
    "relational equality",
    "equality of opportunity",
    "equality of outcome",
    "affirmative action",
    "reverse-discrimination objection",
    "adaptive preference",
    "liberal feminism",
    "marxist feminism",
    "socialist feminism",
    "radical feminism",
    "dual systems theory",
    "carole pateman",
    "the sexual contract",
    "susan moller okin",
    "family as an object of justice",
    "intersectionality",
    "kimberle crenshaw",
    "caste and gender",
    "multiculturalism",
    "is multiculturalism bad for women",
    "female foeticide",
    "sex-selective abortion",
    "sex ratio at birth",
    "missing women",
    "amartya sen",
    "pcpndt act 1994",
    "beti bachao beti padhao",
    "son preference",
    "dowry",
    "bina agarwal",
    "five-level analysis of land rights",
    "title access control return exit",
    "coparcenary",
    "hindu succession act 2005",
    "vineeta sharma v rakesh sharma 2020",
    "empowerment",
    "power over",
    "power to",
    "power with",
    "power within",
    "naila kabeer",
    "resources agency achievements",
    "capability approach",
    "martha nussbaum",
    "care ethics",
    "carol gilligan",
    "ethic of care",
    "political representation",
    "106th constitutional amendment 2023",
    "delimitation",
    "women's reservation",
    "structural injustice",
    "iris marion young",
]

SESSION_SPECS[1]["closure_keywords"] = [
    "judith butler",
    "gender trouble",
    "gender performativity",
    "discursive construction",
]
SESSION_SPECS[4]["closure_keywords"] = [
    "coparcenary",
    "bina agarwal",
    "hindu succession act 2005",
    "title access control return exit",
]
SESSION_SPECS[5]["closure_keywords"] = [
    "power to",
    "power over",
    "empowerment",
    "naila kabeer",
]
SESSION_SPECS[7]["closure_keywords"] = [
    "marxist feminism",
    "radical feminism",
    "socialist feminism",
    "dual systems theory",
]
SESSION_SPECS[8]["closure_keywords"] = [
    "caste and gender",
    "multiculturalism",
    "intersectionality",
    "kimberle crenshaw",
]

ADVANCED_SESSION_TITLES: list[str] = [
    "Advanced: Structural Injustice and Iris Marion Young's Model of Responsibility",
    "Advanced: Capability-Based versus Property-Based Models of Women's Empowerment",
]

OWNER_SESSION_RANGES: list[dict[str, Any]] = [
    {
        "session": 1,
        "session_title": "Sex, Gender and Beauvoir's 'Other'",
        "owner_sections": ["1.1", "1.2", "1.6"],
        "note": (
            "Draws the foundational sex/gender distinction, Beauvoir's Self/"
            "Other framing, and the biological-difference objection-reply pair "
            "from owner section 1.6."
        ),
    },
    {
        "session": 2,
        "session_title": "Gender as a Cultural Category and Butler's Performativity",
        "owner_sections": ["1.3", "1.3A"],
        "note": (
            "Draws gender-as-cultural-category doctrine and Butler's "
            "performativity, including its owner-documented objection and reply."
        ),
    },
    {
        "session": 3,
        "session_title": "Feminist Diagnoses and the Architecture of Equality",
        "owner_sections": ["1.4", "1.5", "1.6"],
        "note": (
            "Draws the feminist-diagnoses table, the equality-types typology, "
            "and the choice/reverse-discrimination objections from owner "
            "section 1.6."
        ),
    },
    {
        "session": 4,
        "session_title": (
            "Female Foeticide: Doctrine, Distinctions, Causes and Missing Women"
        ),
        "owner_sections": ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8"],
        "note": (
            "Draws the complete female foeticide unit, including the PCPNDT "
            "Act 1994 and Beti Bachao Beti Padhao 2015 policy references."
        ),
    },
    {
        "session": 5,
        "session_title": "Land and Property Rights: Agarwal's Five Levels and the Legal Record",
        "owner_sections": ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6"],
        "note": (
            "Draws the complete land/property unit, including the Hindu "
            "Succession Act 2005 amendment and Vineeta Sharma v. Rakesh Sharma "
            "(2020); carries the CURRENT_ANCHOR illustration."
        ),
    },
    {
        "session": 6,
        "session_title": (
            "Empowerment: Dimensions of Power and Kabeer's Resources-Agency-"
            "Achievements"
        ),
        "owner_sections": ["4.1", "4.2", "4.3", "4.4", "4.5"],
        "note": (
            "Draws the power-dimensions framework and Kabeer's tripartite "
            "empowerment model."
        ),
    },
    {
        "session": 7,
        "session_title": (
            "Care Ethics, the Limits of Empowerment and Political Representation"
        ),
        "owner_sections": ["4.3A", "4.6", "4.7", "4.8"],
        "note": (
            "Draws Gilligan's care ethic and the political-representation "
            "limit, including the 106th Amendment's delimitation caveat at "
            "owner section 4.8."
        ),
    },
    {
        "session": 8,
        "session_title": (
            "Feminist Schools in Debate: Marxist, Socialist, Radical, Pateman "
            "and Okin"
        ),
        "owner_sections": ["5.1", "5.2", "5.3", "5.3A", "5.4"],
        "note": (
            "Draws the inter-school feminist debate and the Pateman/Okin "
            "extension into contract theory and the family."
        ),
    },
    {
        "session": 9,
        "session_title": "Gender, Caste and Multiculturalism: The Indian Intersection",
        "owner_sections": ["5.5", "5.6", "6", "7"],
        "note": (
            "Draws the caste-gender intersection, multiculturalism debate, "
            "criticisms, and the seventeen documented traps as synthesis "
            "material."
        ),
    },
    {
        "session": 10,
        "session_title": (
            "Integrated Answer Architecture: Directive Decoder, Evidence Bank "
            "and PYQ Routing"
        ),
        "owner_sections": ["8", "9", "10.0", "10.1", "10.2", "10.3", "10.4", "10.5", "10.6", "11"],
        "note": (
            "Draws the keyword bank, PYQ routing table, full answer "
            "architecture, and link-outs -- organisational, not new doctrine."
        ),
    },
]

PYQ_SOLUTIONS: list[dict[str, Any]] = [
    {
        "year": 2018,
        "question_number": "4(b)",
        "marks": 15,
        "question": "How do you evaluate gender discrimination in the context of female foeticide?",
        "primary_session": 4,
        "secondary_sessions": [3],
        "model_answer": {
            "intro": (
                "Female foeticide, the sex-selective abortion of female fetuses, "
                "is one of the starkest evidences of gender discrimination "
                "because it denies the right to life itself on the basis of sex, "
                "prior to any other form of disadvantage a woman might face."
            ),
            "body": (
                "Amartya Sen's 'missing women' argument treats skewed sex ratios "
                "as an index of systemic discrimination rather than isolated "
                "acts. The causal chain runs from son preference (rooted in "
                "dowry economics, patrilineal inheritance expectation, and "
                "old-age-security norms) through demand for prenatal sex "
                "determination to the abortion itself; prenatal technology only "
                "supplies the instrument. India's legal response, the PCPNDT "
                "Act, 1994, prohibits sex determination for selective purposes, "
                "and the Beti Bachao Beti Padhao scheme (2015) supplements it "
                "with an awareness and enforcement push, yet the practice "
                "persists, which evidences that the underlying discriminatory "
                "preference, not the absence of law, is the operative cause."
            ),
            "objection_reply": (
                "Objection: since the law already exists, continued prevalence "
                "shows that 'law' rather than 'attitude' is the correct target "
                "for reform, and philosophical diagnosis is beside the point. "
                "Reply: persistence despite a prohibitory statute is itself "
                "evidence that formal equality (a bar on the act) has not "
                "reached the underlying substantive attitude (son preference) "
                "that motivates evasion of the law -- confirming, not "
                "undermining, the discrimination-based diagnosis."
            ),
            "verdict": (
                "Female foeticide should be evaluated as gender discrimination "
                "in its most acute form: a denial of existence itself, driven by "
                "son preference and only enabled, not caused, by technology; "
                "legal prohibition is necessary but the persistence of the "
                "practice shows attitudinal, substantive change is the deeper "
                "requirement."
            ),
        },
    },
    {
        "year": 2018,
        "question_number": "4(c)",
        "marks": 15,
        "question": "Is feminism an ideology for empowerment or for equality? Discuss.",
        "primary_session": 3,
        "secondary_sessions": [6],
        "model_answer": {
            "intro": (
                "Feminism is often presented as pursuing either 'equality' "
                "(sameness of treatment) or 'empowerment' (capacity to exercise "
                "choice), but the equality typology shows these are not rival "
                "goals so much as different levels of the same project."
            ),
            "body": (
                "Formal equality demands the removal of explicit differential "
                "rules; substantive equality goes further, licensing "
                "affirmative measures to correct unequal starting points; "
                "relational equality asks whether social relationships remain "
                "hierarchical regardless of formal rules. Empowerment, on "
                "Kabeer's tripartite model, requires resources, agency, and "
                "achievements -- it is the process by which formal or "
                "substantive equality is actually converted into lived "
                "capacity. On this reading, equality supplies the normative "
                "target and empowerment supplies the causal mechanism by which "
                "that target is reached."
            ),
            "objection_reply": (
                "Objection: treating equality and empowerment as compatible "
                "obscures a real tension -- substantive-equality measures "
                "(affirmative action) can be attacked as unearned "
                "'empowerment' that violates formal equality for others (the "
                "reverse-discrimination objection). Reply: the objection "
                "conflates formal and substantive equality; substantive "
                "equality does not violate the requirement of equal moral "
                "worth, it corrects an unequal starting point so that formal "
                "equality's promise can be genuinely realised."
            ),
            "verdict": (
                "Feminism is best read as an ideology for substantive equality "
                "achieved through empowerment -- the two are sequentially "
                "linked rather than competing final ends."
            ),
        },
    },
    {
        "year": 2019,
        "question_number": "1(e)",
        "marks": 10,
        "question": "Can gender equality be realised within a socialist regime? Analyse.",
        "primary_session": 8,
        "secondary_sessions": [],
        "model_answer": {
            "intro": (
                "Whether socialism alone can deliver gender equality turns on "
                "whether patriarchy is reducible to capitalist property "
                "relations (as orthodox Marxist feminism holds) or is an "
                "autonomous system of domination (as radical and dual-systems "
                "feminists hold)."
            ),
            "body": (
                "Marxist feminism derives women's subordination from capitalist "
                "need for unpaid reproductive and domestic labour, implying that "
                "abolishing capitalism should abolish the subordination. "
                "Radical feminism counters that male control operates through "
                "sexuality, violence, and reproduction independently of the "
                "economic system, a claim empirically supported by the "
                "persistence of patriarchal practice within historically "
                "socialist states. Socialist/dual-systems feminism proposes "
                "that capitalism and patriarchy are two interacting but "
                "analytically distinct systems, so that transforming only one "
                "leaves the other's mechanisms of domination intact."
            ),
            "objection_reply": (
                "Objection: a Marxist could argue patriarchy is itself "
                "historically generated by property relations, so ending those "
                "relations should suffice, making the dual-systems addition "
                "redundant. Reply: the historical persistence of patriarchal "
                "control over sexuality and reproduction across differing modes "
                "of production is evidence against reducing patriarchy to a "
                "mere epiphenomenon of capitalism, supporting its treatment as "
                "an independent target of reform."
            ),
            "verdict": (
                "Gender equality is not automatically realised by a socialist "
                "regime alone; the dual-systems view is more defensible, "
                "requiring an explicit, separate feminist transformation "
                "alongside any economic one."
            ),
        },
    },
    {
        "year": 2019,
        "question_number": "3(b)",
        "marks": 15,
        "question": (
            "Consider critically that gender discrimination is a rather "
            "man-made concept but not naturally endowed."
        ),
        "primary_session": 2,
        "secondary_sessions": [1],
        "model_answer": {
            "intro": (
                "The claim that gender discrimination is 'man-made, not "
                "naturally endowed' rests on separating sex (biological) from "
                "gender (social meaning), a separation Beauvoir opens and "
                "Butler radicalises."
            ),
            "body": (
                "Beauvoir's 'one is not born, but rather becomes, a woman' "
                "shows gendered meaning is constructed through woman's "
                "positioning as Other against a male norm. Butler goes further: "
                "gender is produced through performative repetition of "
                "stylised acts, with no prior gendered substance behind them -- "
                "the doing constitutes the being, within a discursive, "
                "regulatory frame, not a biological one. On this account, "
                "gender discrimination is man-made in the strong sense that it "
                "is continually reproduced through everyday repeated social "
                "practice, not dictated by biology."
            ),
            "objection_reply": (
                "Objection (biological-difference objection): reproductive and "
                "physiological differences between the sexes are real, so at "
                "least some differential treatment reflects nature rather than "
                "construction. Reply: real physiological difference does not "
                "itself entail any particular social meaning or hierarchy; the "
                "inferential leap from difference to inferiority is precisely "
                "the cultural, man-made move under scrutiny, not a fact of "
                "nature."
            ),
            "verdict": (
                "Gender discrimination is best characterised as man-made: "
                "grounded in constructed and performatively reproduced social "
                "meaning, not in any natural endowment, though it operates on "
                "top of real (but socially non-determining) biological "
                "difference."
            ),
        },
    },
    {
        "year": 2020,
        "question_number": "4(a)",
        "marks": 20,
        "question": "Do you agree that empowering women can eliminate gender discrimination? Discuss.",
        "primary_session": 7,
        "secondary_sessions": [6],
        "model_answer": {
            "intro": (
                "Empowerment is necessary to counter gender discrimination but "
                "the claim that it can 'eliminate' discrimination outright "
                "overstates what Kabeer's model and the care-ethics/"
                "representation record actually support."
            ),
            "body": (
                "Kabeer's resources-agency-achievements chain shows empowerment "
                "requires more than resource delivery; agency must be exercised "
                "to convert resources into real functioning. Even where agency "
                "is built, Gilligan's ethic of care flags that empowerment "
                "framed only in rights/resource terms can miss relational and "
                "care-based dimensions of women's subordination. Political "
                "representation illustrates the same gap at the institutional "
                "level: the 106th Constitutional Amendment, 2023 enacts "
                "legislative reservation for women, but its implementation is "
                "conditional on a subsequent delimitation exercise, so legal "
                "empowerment can outpace effective empowerment considerably."
            ),
            "objection_reply": (
                "Objection: if empowerment is defined broadly enough (resources "
                "+ agency + achievements + care recognition + effective "
                "representation), then by definition full empowerment would "
                "eliminate discrimination, making the claim true by stipulation. "
                "Reply: the practical record shows empowerment is realised "
                "unevenly and partially (e.g., enacted-but-pending reservation), "
                "so as an empirical, non-stipulative claim, elimination is not "
                "supported -- empowerment reduces but does not by itself "
                "eliminate discrimination."
            ),
            "verdict": (
                "Partial agreement: empowerment is a necessary and powerful "
                "corrective, but 'elimination' overstates the case; structural, "
                "legal, and attitudinal change must accompany it."
            ),
        },
    },
    {
        "year": 2021,
        "question_number": "1(e)",
        "marks": 10,
        "question": "How far can land and property rights be effective in empowerment of women? Explain.",
        "primary_session": 5,
        "secondary_sessions": [],
        "model_answer": {
            "intro": (
                "Land and property rights are effective in empowering women "
                "only to the extent that Bina Agarwal's five distinct dimensions "
                "-- legal title, access/use, control, return, and exit/security "
                "-- produce actual command rather than nominal ownership."
            ),
            "body": (
                "The Hindu Succession Act, 2005 amendment gave daughters "
                "coparcenary rights (title), later clarified for retrospective "
                "application by the Supreme Court in Vineeta Sharma v. Rakesh "
                "Sharma (2020) -- a judgment interpreting the statute, not a "
                "fresh source of the right. Yet title without practical access "
                "to the land, decision-making control over its use, receipt of "
                "income and benefit, and fall-back security against abandonment "
                "or violence leaves empowerment merely nominal."
            ),
            "objection_reply": (
                "Objection: once law grants equal title, any remaining gap is a "
                "social-enforcement problem outside the rights framework's "
                "responsibility. Reply: a rights framework that stops at title "
                "while ignoring predictable non-implementation at the higher "
                "dimensions is philosophically incomplete; access, control, "
                "return and exit/security should be built into the specification "
                "of the right itself."
            ),
            "verdict": (
                "Land and property rights empower only where the five dimensions "
                "yield actual command and a stronger fall-back position; legal "
                "title alone is neither necessary nor sufficient for that result."
            ),
        },
    },
    {
        "year": 2021,
        "question_number": "4(b)",
        "marks": 15,
        "question": (
            "What are the main causes of female foeticide in India? Is it the "
            "result of demonic application of technology only? Discuss."
        ),
        "primary_session": 4,
        "secondary_sessions": [],
        "model_answer": {
            "intro": (
                "The main cause of female foeticide is son preference, not "
                "technology; prenatal diagnostic technology is only the "
                "instrument through which a pre-existing discriminatory "
                "preference is realised."
            ),
            "body": (
                "Son preference is rooted in dowry economics, patrilineal "
                "inheritance expectations, and old-age-security norms that make "
                "sons seem more 'valuable' within the household economy. This "
                "preference generates demand for sex determination; technology "
                "supplies the means to act on that demand. The PCPNDT Act, 1994 "
                "prohibits sex-selective determination, and Beti Bachao Beti "
                "Padhao (2015) supplements enforcement and awareness, yet "
                "continued prevalence of the practice indicates the demand-side "
                "(attitudinal) cause, not the supply-side (technological) one, "
                "is decisive."
            ),
            "objection_reply": (
                "Objection: without the technology, sex-selective abortion at "
                "scale would not be possible, so technology is causally "
                "indispensable and should not be downplayed. Reply: "
                "indispensability as an instrument is not the same as being the "
                "cause; removing the technology would suppress this particular "
                "method but, absent addressing son preference, would not "
                "remove the underlying discriminatory motive, which could seek "
                "other outlets (e.g. differential post-natal neglect)."
            ),
            "verdict": (
                "No -- it is not the result of technology alone; son preference "
                "is the operative cause, with technology as instrument, so "
                "reform must target the underlying preference, not merely "
                "restrict the tool."
            ),
        },
    },
    {
        "year": 2022,
        "question_number": "3(b)",
        "marks": 15,
        "question": "Discuss gender as a cultural category as opposed to sex as a biological category.",
        "primary_session": 2,
        "secondary_sessions": [1],
        "model_answer": {
            "intro": (
                "Sex names a biological fact; gender names the socially "
                "constructed meaning attached to that fact, a distinction "
                "Beauvoir opens and Judith Butler's account of performativity "
                "deepens into a full cultural-category theory."
            ),
            "body": (
                "Butler's Gender Trouble argues gender is constituted through "
                "performative repetition of stylised acts within a regulatory, "
                "discursive frame -- there is no gendered substance prior to or "
                "behind the repeated acts. This treats gender as thoroughly "
                "cultural: produced, disciplined, and reproduced through social "
                "practice, in contrast to sex, which denotes a biological "
                "given. The cultural-category reading explains variation across "
                "societies and time in what counts as masculine or feminine, "
                "which a purely biological account cannot."
            ),
            "objection_reply": (
                "Objection (essentialism objection): without any stable "
                "pre-discursive sex or subject, feminism risks losing the "
                "category 'woman' in whose name it claims to act, undermining "
                "political solidarity. Reply: Butler allows a provisional, "
                "strategic use of 'woman' as a shared discursive position for "
                "political purposes, which does not require metaphysical "
                "essence, only a shared position worth contesting."
            ),
            "verdict": (
                "Gender is best treated as a cultural category, continuously "
                "produced through social practice, standing in contrast to (but "
                "not simply derived from) sex as a biological category."
            ),
        },
    },
    {
        "year": 2023,
        "question_number": "1(c)",
        "marks": 10,
        "question": "Do you agree that the rights concerning land and property have empowered women? Discuss.",
        "primary_session": 5,
        "secondary_sessions": [],
        "model_answer": {
            "intro": (
                "Partial agreement is warranted: statutory land and property "
                "rights have advanced women's legal standing but have not, by "
                "themselves, delivered full empowerment on Agarwal's five-level "
                "analysis."
            ),
            "body": (
                "The Hindu Succession Act, 2005 amendment secured coparcenary "
                "title for daughters, and the Supreme Court in Vineeta Sharma "
                "v. Rakesh Sharma (2020) clarified its retrospective "
                "application -- both strengthen the legal-title dimension. "
                "However, access, control, return and exit/security may remain "
                "with male relatives in practice, so title is not reliably "
                "converted into actual command or bargaining power."
            ),
            "objection_reply": (
                "Objection: since the statutory right now exists in full, any "
                "shortfall is a matter of implementation, not of the rights "
                "regime's design. Reply: a rights regime that predictably fails "
                "to reach the access, control, return and security dimensions bears "
                "responsibility for building enforcement and social-change "
                "mechanisms into the right itself, not treating implementation "
                "as someone else's problem."
            ),
            "verdict": (
                "Land and property rights have empowered women at the level of "
                "legal title, but empowerment remains incomplete until access, "
                "control, return and exit/security are also secured in practice."
            ),
        },
    },
    {
        "year": 2023,
        "question_number": "3(c)",
        "marks": 15,
        "question": "How does gender discrimination lead to female foeticide and social imbalance? Discuss.",
        "primary_session": 4,
        "secondary_sessions": [],
        "model_answer": {
            "intro": (
                "Gender discrimination, expressed as son preference, is the "
                "root cause that channels through prenatal technology into "
                "female foeticide, and the resulting skew feeds back into "
                "broader social imbalance."
            ),
            "body": (
                "Son preference -- shaped by dowry economics, inheritance "
                "expectation, and old-age-security norms -- generates demand "
                "for sex determination and selective abortion despite the "
                "PCPNDT Act, 1994's prohibition. Amartya Sen's 'missing women' "
                "argument treats the resulting skew in sex ratio at birth as an "
                "index of systemic discrimination. This skew in turn produces "
                "social imbalance: distortions in marriage markets, and "
                "compounding pressure on the sex ratio in subsequent "
                "generations, entrenching the very discrimination that caused "
                "it."
            ),
            "objection_reply": (
                "Objection: attributing imbalance to discrimination overlooks "
                "individual family economic calculation, which may be a "
                "rational response to real economic constraints, not "
                "'discrimination' in a normatively loaded sense. Reply: a "
                "'rational' calculation that treats daughters as economically "
                "less worth having than sons is not thereby exempt from being "
                "discriminatory -- rational responses to a discriminatory "
                "background structure remain instances of that discrimination, "
                "not independent of it."
            ),
            "verdict": (
                "Gender discrimination causally leads to female foeticide via "
                "son preference, and the resulting sex-ratio skew produces "
                "self-reinforcing social imbalance -- a feedback loop, not a "
                "one-off harm."
            ),
        },
    },
    {
        "year": 2024,
        "question_number": "4(a)",
        "marks": 20,
        "question": (
            "Discuss gender equality as a necessary condition to achieve "
            "empowerment of women. Also examine the role of women empowerment "
            "in curbing the menace of female foeticide."
        ),
        "primary_session": 6,
        "secondary_sessions": [7, 4],
        "model_answer": {
            "intro": (
                "Gender equality is a necessary, though not sufficient, "
                "condition for empowerment, and empowerment in turn can help "
                "curb female foeticide by weakening the son-preference logic "
                "that drives it."
            ),
            "body": (
                "Part one: on Kabeer's model, resources delivered under "
                "unequal background norms rarely convert into agency, since "
                "unequal treatment constrains what choices are practically "
                "available or socially permitted -- so a baseline of gender "
                "equality is a precondition for empowerment's agency and "
                "achievement stages to function. Part two: empowered women, "
                "with greater agency over reproductive and household "
                "decisions, are positioned to resist son-preference pressure, "
                "and the record (PCPNDT Act 1994, Beti Bachao Beti Padhao 2015) "
                "shows policy pairs legal prohibition with empowerment-style "
                "awareness measures precisely because empowerment complements, "
                "rather than replaces, legal deterrence."
            ),
            "objection_reply": (
                "Objection: empowerment interventions could fail to reduce "
                "foeticide if son preference is driven by deep economic "
                "structures (dowry, inheritance) that individual agency cannot "
                "override. Reply: while individual agency cannot dissolve "
                "structural drivers alone, empowered women collectively "
                "reshape norms and demand policy change over time, so "
                "empowerment operates as a necessary complement to, not a "
                "substitute for, structural and legal reform."
            ),
            "verdict": (
                "Gender equality is necessary for genuine empowerment, and "
                "empowerment meaningfully contributes to curbing female "
                "foeticide, but neither alone is sufficient absent the "
                "structural and legal measures addressed in Sessions 4 and 5."
            ),
        },
    },
    {
        "year": 2025,
        "question_number": "1(b)",
        "marks": 10,
        "question": (
            "How does gender as a social construct affect individuals' "
            "opportunities, rights, and access to resources? Critically "
            "discuss."
        ),
        "primary_session": 1,
        "secondary_sessions": [2, 3],
        "model_answer": {
            "intro": (
                "Gender, as a social rather than biological construct in "
                "Beauvoir's and Butler's sense, shapes the opportunities, "
                "rights, and resource access individuals are granted or denied "
                "well before any individual merit is considered."
            ),
            "body": (
                "Once woman is constructed as Other (Beauvoir) and gender is "
                "reproduced through performative repetition (Butler), that "
                "constructed meaning is used to justify differential access: "
                "to education and employment (opportunity), to inheritance and "
                "representation (rights, per Sessions 5 and 7), and to land, "
                "credit, and property (resources, per Session 5's five-level "
                "analysis). Because the construction is social rather than "
                "natural, the resulting inequality is a matter of formal versus "
                "substantive equality (Session 3) rather than an unavoidable "
                "fact of nature."
            ),
            "objection_reply": (
                "Objection: if gender is 'only' a construct, one could argue "
                "the resulting disadvantage is not 'real' in the way material "
                "biological constraint is real, understating the urgency of "
                "reform. Reply: constructed does not mean unreal or trivial -- "
                "socially constructed disadvantage has entirely real material "
                "consequences (land denial, foeticide, exclusion from "
                "representation), and being constructed is precisely what "
                "makes it remediable through social and legal change."
            ),
            "verdict": (
                "Gender as a social construct systematically structures "
                "unequal opportunity, rights, and resource access; its "
                "constructed status is a reason for urgency and remediability, "
                "not for dismissal."
            ),
        },
    },
]

MCQS: list[dict[str, Any]] = [
    {
        "id": 1,
        "session": 1,
        "question": "According to Simone de Beauvoir, which statement best captures the sex/gender distinction?",
        "options": [
            "'One is not born, but rather becomes, a woman' -- gender is socially constituted",
            "Sex and gender are identical terms for the same biological fact",
            "Gender is fixed permanently at conception alongside sex",
            "Only men possess a socially constructed gender identity",
        ],
        "answer": "A",
        "explanation": "Beauvoir's 'becoming' thesis distinguishes constituted gender from given sex.",
        "trap_remediation": "Do not treat sex and gender as synonyms; re-read Session 1's opening distinction.",
    },
    {
        "id": 2,
        "session": 1,
        "question": "In Beauvoir's Self/Other framework, woman is positioned as:",
        "options": [
            "the neutral universal Subject",
            "Other, defined relationally against a male norm",
            "an entirely separate, unrelated category",
            "identical to the Subject in all respects",
        ],
        "answer": "B",
        "explanation": "The Othering move defines woman only relationally against a male Subject/norm.",
        "trap_remediation": "Remember Other is a relational, not an independent, category.",
    },
    {
        "id": 3,
        "session": 1,
        "question": "The 'biological-difference objection' to the sex/gender distinction claims that:",
        "options": [
            "gender has no biological basis whatsoever",
            "sex and gender are entirely socially constructed",
            "real physiological differences justify some differential treatment",
            "biological difference proves gender discrimination is illegal",
        ],
        "answer": "C",
        "explanation": "The objection grounds differential treatment in real physiological difference.",
        "trap_remediation": "Do not confuse this objection with a claim about legality.",
    },
    {
        "id": 4,
        "session": 1,
        "question": "The philosophical reply to the biological-difference objection is that:",
        "options": [
            "biological differences do not exist",
            "differential treatment is always justified by biology",
            "the objection is irrelevant to feminism",
            "difference does not by itself entail unequal social worth",
        ],
        "answer": "D",
        "explanation": "The reply denies the inference from physical difference to social hierarchy, not the difference itself.",
        "trap_remediation": "Do not deny biological difference outright; the reply concedes it and blocks only the inference.",
    },
    {
        "id": 5,
        "session": 1,
        "question": "Treating woman's subordination as natural rather than social:",
        "options": [
            "forecloses reform by making inequality appear inevitable",
            "has no consequence for policy",
            "was rejected by Beauvoir as an incoherent idea",
            "is the same claim as the performativity thesis",
        ],
        "answer": "A",
        "explanation": "Naturalising subordination stabilises it as unchangeable, blocking reform.",
        "trap_remediation": "Keep this consequence distinct from the (later) performativity thesis of Session 2.",
    },
    {
        "id": 6,
        "session": 2,
        "question": "Judith Butler's concept of 'gender performativity' holds that:",
        "options": [
            "gender is an inner essence expressed outwardly",
            "gender is constituted through repeated performative acts, with no prior essence",
            "gender is purely biological",
            "performativity means consciously choosing a gender like an actor",
        ],
        "answer": "B",
        "explanation": "Performativity denies a prior gendered substance behind repeated acts.",
        "trap_remediation": "Do not equate performativity with a stage-actor choosing a role; there is no prior chooser.",
    },
    {
        "id": 7,
        "session": 2,
        "question": "In Gender Trouble, Butler argues gender is produced by:",
        "options": [
            "a single deliberate performance",
            "genetic inheritance alone",
            "performative repetition of stylised acts within a regulatory frame",
            "state legislation exclusively",
        ],
        "answer": "C",
        "explanation": "Repetition within a regulatory, discursive frame constitutes gender on Butler's account.",
        "trap_remediation": "A single act is not performativity; repetition is essential.",
    },
    {
        "id": 8,
        "session": 2,
        "question": "The 'essentialism objection' to Butler's account warns that:",
        "options": [
            "Butler ignores culture entirely",
            "performativity proves gender is purely natural",
            "repetition theory cannot explain any social change",
            "without a stable pre-discursive subject, feminism may lose 'woman' as a category for solidarity",
        ],
        "answer": "D",
        "explanation": "The objection targets the loss of a stable political subject 'woman.'",
        "trap_remediation": "Do not confuse this with a claim that Butler denies culture altogether.",
    },
    {
        "id": 9,
        "session": 2,
        "question": "Butler's reply to the essentialism objection is that:",
        "options": [
            "'woman' can be used provisionally and strategically as a shared discursive position",
            "the category 'woman' must be abandoned entirely",
            "essentialism is actually correct",
            "political solidarity requires metaphysical essence",
        ],
        "answer": "A",
        "explanation": "Strategic, provisional use of 'woman' preserves solidarity without requiring essence.",
        "trap_remediation": "Do not read the reply as abandoning the category outright.",
    },
    {
        "id": 10,
        "session": 2,
        "question": "A key limitation of performativity theory noted in the socio-political syllabus is that it:",
        "options": [
            "cannot describe gender at all",
            "explains reproduction of norms better than it explains why particular norms become dominant",
            "was fully resolved by Beauvoir before Butler wrote",
            "applies only to men",
        ],
        "answer": "B",
        "explanation": "Structural accounts (Sessions 6-8) supply the missing 'why this norm' piece.",
        "trap_remediation": "Do not present this limit as a wholesale rejection of performativity.",
    },
    {
        "id": 11,
        "session": 3,
        "question": "'Formal equality' as a remedy for gender discrimination means:",
        "options": [
            "correcting unequal starting points via targeted measures",
            "restructuring social relationships directly",
            "removing explicit differential legal rules",
            "guaranteeing equal outcomes regardless of starting point",
        ],
        "answer": "C",
        "explanation": "Formal equality bars explicit differential rules, nothing more.",
        "trap_remediation": "Do not conflate formal equality with substantive correction of disadvantage.",
    },
    {
        "id": 12,
        "session": 3,
        "question": "'Substantive equality' differs from formal equality because it:",
        "options": [
            "ignores unequal starting points",
            "only applies to men",
            "bars any differential rule",
            "permits affirmative measures to correct unequal starting points",
        ],
        "answer": "D",
        "explanation": "Substantive equality licenses targeted correction beyond a bare rule-neutrality.",
        "trap_remediation": "Distinguish this clearly from formal equality's rule-only focus.",
    },
    {
        "id": 13,
        "session": 3,
        "question": "The 'reverse-discrimination objection' to affirmative action for women claims that:",
        "options": [
            "such measures unfairly disadvantage men",
            "affirmative action is required by formal equality",
            "women do not face any disadvantage",
            "relational equality is identical to formal equality",
        ],
        "answer": "A",
        "explanation": "The objection frames affirmative measures as unfair to men.",
        "trap_remediation": "Do not present this objection as claiming women face no disadvantage.",
    },
    {
        "id": 14,
        "session": 3,
        "question": "The reply to the reverse-discrimination objection argues that:",
        "options": [
            "men are never disadvantaged by any policy",
            "correcting a structural disadvantage is not equivalent to creating a new one",
            "affirmative action should be abolished",
            "formal equality alone suffices",
        ],
        "answer": "B",
        "explanation": "Correcting disadvantage is analytically distinct from creating a new disadvantage.",
        "trap_remediation": "Avoid overstating the reply as an absolute denial of any cost to anyone.",
    },
    {
        "id": 15,
        "session": 3,
        "question": "'Relational equality' asks specifically whether:",
        "options": [
            "laws explicitly differentiate by sex",
            "outcomes are numerically identical",
            "social relationships themselves remain hierarchical despite equal formal rules",
            "affirmative action has been abolished",
        ],
        "answer": "C",
        "explanation": "Relational equality probes the persistence of hierarchy in social relations, beyond formal rules.",
        "trap_remediation": "Do not reduce relational equality to a numerical-outcome test.",
    },
    {
        "id": 16,
        "session": 4,
        "question": "The primary cause of female foeticide, per the syllabus diagnosis, is:",
        "options": [
            "prenatal diagnostic technology itself",
            "the PCPNDT Act, 1994",
            "Beti Bachao Beti Padhao",
            "son preference, with technology as the instrument",
        ],
        "answer": "D",
        "explanation": "Son preference is the cause; technology is only the instrument.",
        "trap_remediation": "Never name technology as the primary cause -- this is the syllabus's flagged trap.",
    },
    {
        "id": 17,
        "session": 4,
        "question": "The PCPNDT Act, 1994 is best described as:",
        "options": [
            "an enacted statute prohibiting prenatal sex determination for selective purposes",
            "a Supreme Court judgment",
            "a constitutional amendment",
            "a scheme launched in 2015",
        ],
        "answer": "A",
        "explanation": "PCPNDT is an enacted statute, not a judgment, amendment, or scheme.",
        "trap_remediation": "Keep the statute/scheme/judgment categories precise; do not conflate with Beti Bachao Beti Padhao (2015).",
    },
    {
        "id": 18,
        "session": 4,
        "question": "Amartya Sen's 'missing women' argument uses skewed sex ratios as:",
        "options": [
            "proof that technology alone causes foeticide",
            "an index of systemic discrimination against women",
            "evidence that no legal remedy exists",
            "a purely economic, non-gendered phenomenon",
        ],
        "answer": "B",
        "explanation": "Sen treats the skew as an index of systemic, not merely technological, discrimination.",
        "trap_remediation": "Do not cite an invented sex-ratio figure; cite only the direction of skew and Sen's argument.",
    },
    {
        "id": 19,
        "session": 4,
        "question": "Beti Bachao Beti Padhao (2015) functions as:",
        "options": [
            "the original statute prohibiting sex determination",
            "a Supreme Court ruling",
            "a policy scheme supplementing legal enforcement and awareness",
            "a constitutional amendment",
        ],
        "answer": "C",
        "explanation": "Beti Bachao Beti Padhao is a supplementary policy scheme, not the founding statute.",
        "trap_remediation": "Do not confuse this 2015 scheme with the 1994 PCPNDT Act.",
    },
    {
        "id": 20,
        "session": 4,
        "question": "Continued prevalence of female foeticide despite the PCPNDT Act suggests that:",
        "options": [
            "the law has had no relevance whatsoever",
            "technology, not attitude, is the cause",
            "son preference has been eliminated",
            "formal legal prohibition has not fully reached the underlying discriminatory attitude",
        ],
        "answer": "D",
        "explanation": "Persistence supports, rather than refutes, the son-preference diagnosis.",
        "trap_remediation": "Avoid concluding the law is entirely irrelevant; it is necessary but not sufficient.",
    },
    {
        "id": 21,
        "session": 5,
        "question": "Bina Agarwal's five-level analysis of land rights consists of:",
        "options": [
            "legal title, access/use, control, return, exit/security",
            "title, income, marriage, divorce, custody",
            "sex, gender, caste, class, religion",
            "resources, agency, achievements, power, justice",
        ],
        "answer": "A",
        "explanation": "The five dimensions are legal title, access/use, control, return, and exit/security.",
        "trap_remediation": "Do not substitute Kabeer's resources/agency/achievements terms for Agarwal's analysis.",
    },
    {
        "id": 22,
        "session": 5,
        "question": "The Hindu Succession Act, 2005 amendment is best classified as:",
        "options": [
            "a Supreme Court judgment",
            "an enacted statute granting daughters coparcenary rights",
            "a policy scheme",
            "an unimplemented bill",
        ],
        "answer": "B",
        "explanation": "The 2005 amendment is the enacted statutory source of the coparcenary right.",
        "trap_remediation": "Do not cite Vineeta Sharma (2020) as the source statute -- it only clarifies the amendment.",
    },
    {
        "id": 23,
        "session": 5,
        "question": "Vineeta Sharma v. Rakesh Sharma (2020) is:",
        "options": [
            "the statute that created the coparcenary right",
            "a constitutional amendment",
            "a Supreme Court judgment clarifying the 2005 amendment's retrospective application",
            "unrelated to inheritance law",
        ],
        "answer": "C",
        "explanation": "Vineeta Sharma is a 2020 SC judgment clarifying, not creating, the coparcenary right.",
        "trap_remediation": "Keep statute (2005 amendment) and judgment (Vineeta Sharma, 2020) distinct.",
    },
    {
        "id": 24,
        "session": 5,
        "question": "Holding legal 'title' to land while a male relative retains all decision-making power illustrates:",
        "options": [
            "full empowerment",
            "the 'exit' rung being satisfied",
            "an impossibility under Indian law",
            "a gap between legal title and actual control/return",
        ],
        "answer": "D",
        "explanation": "This is the classic title-without-control gap Agarwal's analysis is designed to expose.",
        "trap_remediation": "Do not treat legal title as equivalent to full empowerment.",
    },
    {
        "id": 25,
        "session": 5,
        "question": "The exit/security dimension in Agarwal's analysis refers to:",
        "options": [
            "the practical, social ability to leave an unjust household or marriage",
            "the legal title to land",
            "the right to sell land only",
            "a purely symbolic entitlement",
        ],
        "answer": "A",
        "explanation": "Exit denotes the practical social capacity to leave an oppressive arrangement.",
        "trap_remediation": "Do not confuse exit/security with return, which asks who receives income and benefit.",
    },
    {
        "id": 26,
        "session": 6,
        "question": "In Naila Kabeer's model, 'agency' functions as:",
        "options": [
            "a synonym for resources",
            "the necessary intermediate capacity converting resources into achievements",
            "an outcome, not a process",
            "irrelevant to empowerment",
        ],
        "answer": "B",
        "explanation": "Agency is the load-bearing link between resources and achievements.",
        "trap_remediation": "Do not treat resources and agency as interchangeable terms.",
    },
    {
        "id": 27,
        "session": 6,
        "question": "Kabeer's empowerment chain is best described as:",
        "options": [
            "achievements -> agency -> resources",
            "resources alone determine empowerment",
            "resources -> agency -> achievements",
            "a two-step, not three-step, process",
        ],
        "answer": "C",
        "explanation": "The chain runs resources to agency to achievements, in that order.",
        "trap_remediation": "Do not reverse the chain's direction or collapse it to two steps.",
    },
    {
        "id": 28,
        "session": 6,
        "question": "A bank account opened for a woman but controlled entirely by her husband illustrates:",
        "options": [
            "full empowerment under Kabeer's model",
            "successful conversion of resources into agency",
            "the 'power-within' register only",
            "resource delivery without agency, hence no real empowerment gain",
        ],
        "answer": "D",
        "explanation": "A resource without exercised agency fails Kabeer's empowerment test.",
        "trap_remediation": "Do not equate resource access alone with empowerment.",
    },
    {
        "id": 29,
        "session": 6,
        "question": "The four power registers used alongside Kabeer's model are:",
        "options": [
            "power-over, power-to, power-with, power-within",
            "power-title, power-access, power-control, power-exit",
            "power-formal, power-substantive, power-relational, power-outcome",
            "power-legal, power-social, power-economic, power-political only",
        ],
        "answer": "A",
        "explanation": "The four registers are power-over, power-to, power-with, and power-within.",
        "trap_remediation": "Do not confuse these with Agarwal's five-level land-rights analysis.",
    },
    {
        "id": 30,
        "session": 6,
        "question": "A critic's objection that Kabeer's model is 'too demanding' is answered by noting the model is:",
        "options": [
            "a strict pass/fail gate for any policy",
            "diagnostic, locating exactly where an intervention breaks down",
            "irrelevant to policy evaluation",
            "identical to the equality typology",
        ],
        "answer": "B",
        "explanation": "The model diagnoses breakdown points rather than issuing a pass/fail verdict.",
        "trap_remediation": "Do not read the model as declaring most policy 'failed' outright.",
    },
    {
        "id": 31,
        "session": 7,
        "question": "Carol Gilligan's 'ethic of care' is best understood as:",
        "options": [
            "a purely legal doctrine",
            "identical to Kabeer's resources-agency-achievements model",
            "a moral framework grounded in relational responsibility rather than abstract rights-adjudication",
            "a rejection of all rights-based reasoning",
        ],
        "answer": "C",
        "explanation": "Care ethics grounds morality in relational responsibility, supplementing rights-based reasoning.",
        "trap_remediation": "Do not present care ethics as a wholesale rejection of rights.",
    },
    {
        "id": 32,
        "session": 7,
        "question": "The 106th Constitutional Amendment, 2023 provides for:",
        "options": [
            "immediate, unconditional seat allocation for women",
            "abolition of legislative reservation",
            "land rights for women only",
            "legislative reservation for women whose implementation is conditional on subsequent delimitation",
        ],
        "answer": "D",
        "explanation": "The amendment enacts reservation but ties implementation to a later delimitation exercise.",
        "trap_remediation": "Do not describe the amendment as already fully operational in seat allocation.",
    },
    {
        "id": 33,
        "session": 7,
        "question": "The gap between the 106th Amendment's enactment and its effective implementation illustrates:",
        "options": [
            "a divergence between legal empowerment and effective/political empowerment",
            "that the amendment has already been fully implemented",
            "that delimitation is irrelevant to its operation",
            "that Gilligan's care ethic is inapplicable to representation",
        ],
        "answer": "A",
        "explanation": "This mirrors the title-without-control gap seen in land rights, at the political level.",
        "trap_remediation": "Do not treat legal enactment as equivalent to effective empowerment.",
    },
    {
        "id": 34,
        "session": 7,
        "question": "An objection to care ethics is that it risks:",
        "options": [
            "eliminating rights-based reasoning permanently",
            "re-inscribing women into the very caregiving role that trapped them in unequal labour",
            "proving too little about moral reasoning",
            "being identical to formal equality",
        ],
        "answer": "B",
        "explanation": "The objection warns care ethics may re-confine women to caregiving.",
        "trap_remediation": "Pair this objection with the reply: care should be shared, not confined to women.",
    },
    {
        "id": 35,
        "session": 8,
        "question": "Marxist feminism locates the root cause of women's subordination in:",
        "options": [
            "patriarchy as fully independent of economic system",
            "the family as an object of justice",
            "capitalist property relations and women's unpaid reproductive labour",
            "the social contract tradition alone",
        ],
        "answer": "C",
        "explanation": "Marxist feminism derives subordination from capitalist need for unpaid reproductive labour.",
        "trap_remediation": "Do not attribute the 'patriarchy as independent system' claim to Marxist feminism.",
    },
    {
        "id": 36,
        "session": 8,
        "question": "Radical feminism, unlike orthodox Marxist feminism, treats patriarchy as:",
        "options": [
            "wholly reducible to capitalism",
            "irrelevant to gender discrimination",
            "a purely legal construct",
            "an autonomous system of male domination, independent of class",
        ],
        "answer": "D",
        "explanation": "Radical feminism treats patriarchy as an independent system of domination.",
        "trap_remediation": "Do not conflate radical feminism's independence claim with Marxist feminism's economic reduction.",
    },
    {
        "id": 37,
        "session": 8,
        "question": "'Dual systems theory' in socialist feminism proposes that:",
        "options": [
            "capitalism and patriarchy are two interacting but analytically distinct systems",
            "only capitalism matters",
            "only patriarchy matters",
            "capitalism and patriarchy are identical",
        ],
        "answer": "A",
        "explanation": "Dual systems theory treats capitalism and patriarchy as distinct, interacting systems.",
        "trap_remediation": "Do not treat dual systems theory as a synonym for either pure Marxist or pure radical feminism.",
    },
    {
        "id": 38,
        "session": 8,
        "question": "Carole Pateman's 'sexual contract' argument claims that:",
        "options": [
            "the social contract tradition has no gendered assumptions",
            "the social contract tradition presupposes a prior sexual contract subordinating women",
            "women authored the original social contract",
            "the family is outside the scope of justice",
        ],
        "answer": "B",
        "explanation": "Pateman argues the social contract masks a prior sexual contract subordinating women.",
        "trap_remediation": "Do not present the social contract tradition as gender-neutral on Pateman's account.",
    },
    {
        "id": 39,
        "session": 8,
        "question": "Susan Moller Okin's 'family as an object of justice' argues that:",
        "options": [
            "justice theories should exempt the family from scrutiny",
            "the family has no bearing on gender equality",
            "Rawlsian justice cannot bracket the unjust internal distribution of power within families",
            "Pateman and Okin hold identical positions",
        ],
        "answer": "C",
        "explanation": "Okin insists justice must reach inside the family, not stop at its threshold.",
        "trap_remediation": "Do not merge Okin's family-justice argument with Pateman's sexual-contract argument -- they are related but distinct.",
    },
    {
        "id": 40,
        "session": 9,
        "question": "Kimberle Crenshaw's 'intersectionality' shows that caste and gender disadvantage:",
        "options": [
            "simply add together without producing distinct harm",
            "are entirely unrelated categories",
            "apply only to caste, not gender",
            "compound to produce distinct, structurally located harms not captured by either axis alone",
        ],
        "answer": "D",
        "explanation": "Intersectionality shows compounded, not merely additive, harm.",
        "trap_remediation": "Do not describe intersectional harm as a simple sum of two separate axes.",
    },
    {
        "id": 41,
        "session": 9,
        "question": "Treating 'women' in the Indian context as a homogeneous category:",
        "options": [
            "obscures caste-specific harms within gender discrimination",
            "is the correct analytical approach",
            "is required by intersectionality theory",
            "was rejected by Okin but endorsed by Crenshaw",
        ],
        "answer": "A",
        "explanation": "A homogeneous 'women' category masks caste-specific harm.",
        "trap_remediation": "On synthesis questions, always disaggregate 'women' by caste position.",
    },
    {
        "id": 42,
        "session": 9,
        "question": "Susan Moller Okin's question 'Is multiculturalism bad for women?' presses whether:",
        "options": [
            "all cultures are equally patriarchal",
            "state accommodation of group practices can entrench internal patriarchal norms",
            "multiculturalism should be abolished outright",
            "gender discrimination is unrelated to cultural accommodation",
        ],
        "answer": "B",
        "explanation": "Okin's question targets state accommodation entrenching internal patriarchy.",
        "trap_remediation": "Do not read Okin as claiming all cultures are equally patriarchal; the question is conditional.",
    },
    {
        "id": 43,
        "session": 9,
        "question": "The multiculturalist objection to state intervention in group practices for gender equality is that such intervention is:",
        "options": [
            "always philosophically incoherent",
            "irrelevant to Okin's argument",
            "a form of majoritarian or statist overreach into cultural self-governance",
            "required by Crenshaw's framework",
        ],
        "answer": "C",
        "explanation": "The objection frames intervention as overreach into cultural self-governance.",
        "trap_remediation": "Pair this objection with Okin's reply on equal citizenship.",
    },
    {
        "id": 44,
        "session": 9,
        "question": "Okin's reply to the multiculturalist objection is that a state committed to equal citizenship:",
        "options": [
            "must exempt all group practices from scrutiny",
            "cannot ever intervene in cultural practice",
            "should treat caste and gender as unrelated",
            "cannot consistently exempt any group's internal practice from the equality standard applied elsewhere",
        ],
        "answer": "D",
        "explanation": "Okin denies a consistent basis for exempting any group's internal domination.",
        "trap_remediation": "Do not overstate the reply as licensing unlimited state intervention in all cultural practice.",
    },
    {
        "id": 45,
        "session": 10,
        "question": "The first step in the answer-architecture spine for any gender-discrimination prompt is to:",
        "options": [
            "decode the directive word (discuss/examine/analyse/critically evaluate)",
            "write a generic Beauvoir-Butler opening regardless of the question",
            "skip straight to the verdict",
            "cite the 106th Amendment regardless of relevance",
        ],
        "answer": "A",
        "explanation": "Directive-word decoding is the mandated first step of the spine.",
        "trap_remediation": "Avoid a one-size-fits-all opening; always route to the question's actual keyword first.",
    },
    {
        "id": 46,
        "session": 10,
        "question": "A prompt containing the keyword 'foeticide' should be routed primarily to:",
        "options": [
            "Session 8",
            "Session 4",
            "Session 2",
            "Session 9",
        ],
        "answer": "B",
        "explanation": "Foeticide keywords route to Session 4 per the routing table.",
        "trap_remediation": "Do not default to Session 1/2 doctrine for foeticide-specific prompts.",
    },
    {
        "id": 47,
        "session": 10,
        "question": "A prompt framed around 'socialist regime' and gender equality routes primarily to:",
        "options": [
            "Session 5",
            "Session 1",
            "Session 8",
            "Session 3",
        ],
        "answer": "C",
        "explanation": "Socialist-regime prompts route to Session 8's inter-school feminist debate.",
        "trap_remediation": "Do not route socialist-regime prompts to the land/property session.",
    },
    {
        "id": 48,
        "session": 10,
        "question": "The routing table is best understood as:",
        "options": [
            "a substitute for original philosophical engagement",
            "irrelevant to exam performance",
            "a fixed set of model answers to memorise verbatim",
            "scaffolding that ensures correct doctrine retrieval, leaving room for objection-reply and verdict",
        ],
        "answer": "D",
        "explanation": "The table is scaffolding for retrieval, not a substitute for original engagement.",
        "trap_remediation": "Do not treat the routing table itself as the finished answer.",
    },
]

ORIGINAL_MAINS: list[dict[str, Any]] = [
    {
        "marks": 10,
        "prompt": (
            "Distinguish formal equality from substantive equality and examine "
            "which better addresses gender discrimination in India."
        ),
        "primary_session": 3,
        "model_solution": {
            "intro": (
                "Formal equality removes explicit differential rules; "
                "substantive equality additionally corrects unequal starting "
                "points through targeted measures."
            ),
            "body": (
                "Formal equality alone risks equal treatment of unequals, "
                "reproducing existing disadvantage where women start from a "
                "structurally weaker position (in land rights, political "
                "representation, or labour-force access). Substantive equality "
                "responds by permitting affirmative measures calibrated to "
                "that unequal starting point."
            ),
            "objection_reply": (
                "Objection: substantive measures invite the "
                "reverse-discrimination charge against men. Reply: correcting "
                "a structural disadvantage is not equivalent to creating a new "
                "one; the measure targets a starting-point gap, not an "
                "arbitrary preference."
            ),
            "verdict": (
                "Substantive equality better addresses gender discrimination "
                "in India precisely because formal legal parity already "
                "exists in many domains while real disadvantage persists."
            ),
        },
    },
    {
        "marks": 10,
        "prompt": (
            "Explain Naila Kabeer's criterion of empowerment through resources, "
            "agency, and achievements, with an Indian illustration."
        ),
        "primary_session": 6,
        "model_solution": {
            "intro": (
                "Kabeer defines empowerment as the process of acquiring the "
                "ability to make strategic life choices, structured through "
                "resources, agency, and achievements."
            ),
            "body": (
                "Resources (material, human, social) are preconditions; agency "
                "is the exercised capacity to define and act on goals; "
                "achievements are the resulting functioning outcomes. A "
                "land-title scheme for women illustrates the chain: title is a "
                "resource, but only where the woman also exercises control "
                "over its use does an achievement (improved bargaining "
                "position) follow."
            ),
            "objection_reply": (
                "Objection: the model risks being too demanding, since almost "
                "no scheme perfectly builds agency. Reply: the model is "
                "diagnostic -- it identifies precisely where a scheme's "
                "empowerment claim breaks down, rather than issuing a blanket "
                "pass/fail verdict."
            ),
            "verdict": (
                "Kabeer's model shows that resource delivery without agency "
                "is empowerment in name only; Indian schemes must be assessed "
                "against all three links in the chain."
            ),
        },
    },
    {
        "marks": 15,
        "prompt": (
            "Does Judith Butler's theory of gender performativity dissolve the "
            "sex/gender distinction? Critically examine."
        ),
        "primary_session": 2,
        "model_solution": {
            "intro": (
                "Butler's performativity thesis pushes the sex/gender "
                "distinction further than Beauvoir by denying any gendered "
                "substance prior to repeated performative acts, raising the "
                "question of whether the distinction survives at all."
            ),
            "body": (
                "If gender is wholly constituted through performative "
                "repetition within a discursive frame, 'sex' as a supposedly "
                "raw biological given is itself, on Butler's later argument, "
                "already discursively mediated -- suggesting the sex/gender "
                "boundary is not a clean binary but a matter of degree."
            ),
            "objection_reply": (
                "Objection: if even sex is discursively constructed, the "
                "distinction collapses entirely, leaving no stable ground for "
                "feminist politics or for talking about 'women' as a group. "
                "Reply: Butler's own answer is that a provisional, strategic "
                "use of 'woman' remains available without requiring a "
                "metaphysically fixed sex/gender boundary -- the distinction's "
                "political utility does not depend on its metaphysical purity."
            ),
            "verdict": (
                "Performativity does not so much dissolve the sex/gender "
                "distinction as radicalise it, showing both terms to be "
                "more thoroughly constructed than Beauvoir's original account "
                "suggested, while preserving a workable, strategic "
                "distinction for political purposes."
            ),
        },
    },
    {
        "marks": 15,
        "prompt": (
            "Compare Marxist and socialist feminism on the relationship "
            "between capitalism and patriarchy."
        ),
        "primary_session": 8,
        "model_solution": {
            "intro": (
                "Marxist and socialist feminism share a materialist starting "
                "point but diverge on whether patriarchy is reducible to "
                "capitalism or must be treated as an independent system."
            ),
            "body": (
                "Marxist feminism derives women's subordination from "
                "capitalist need for unpaid reproductive and domestic labour, "
                "implying patriarchy would recede with capitalism's abolition. "
                "Socialist feminism's dual-systems move instead treats "
                "capitalism and patriarchy as two interacting but analytically "
                "distinct systems, each requiring separate transformation."
            ),
            "objection_reply": (
                "Objection: a Marxist could argue treating patriarchy as "
                "independent is analytically redundant if it historically "
                "arose from property relations. Reply: patriarchal control "
                "over sexuality and reproduction has persisted across "
                "different modes of production, including socialist states, "
                "which is evidence against reducing it to a mere "
                "epiphenomenon of capitalism."
            ),
            "verdict": (
                "The dual-systems (socialist feminist) position is more "
                "defensible: it explains persistence of patriarchy even where "
                "capitalism has been substantially transformed, which orthodox "
                "Marxist feminism struggles to accommodate."
            ),
        },
    },
    {
        "marks": 20,
        "prompt": (
            "\"Legal title to property, without control over it, does not "
            "empower women.\" Examine this statement using Bina Agarwal's "
            "framework."
        ),
        "primary_session": 5,
        "model_solution": {
            "intro": (
                "Agarwal's five-level analysis -- legal title, access/use, "
                "control, return and exit/security -- shows why legal title "
                "alone is an incomplete basis for claiming empowerment."
            ),
            "body": (
                "India's legal record secures the title rung through the "
                "Hindu Succession Act, 2005 amendment, with the Supreme "
                "Court's Vineeta Sharma v. Rakesh Sharma (2020) clarifying its "
                "retrospective scope. Yet without practical access to the "
                "land, decision-making control over its use, receipt of its "
                "income and benefit, and fall-back security against abandonment "
                "or violence, a woman's title remains largely "
                "nominal -- the family's effective decision-making can remain "
                "entirely with male relatives despite her legal ownership. A "
                "further, illustrative example of courts extending "
                "inheritance-equality reasoning is Ram Charan & Ors. v. "
                "Sukhram & Ors., [2025] 8 S.C.R. 272 (2025 INSC 865, decided "
                "17 July 2025), which held that absent a proven custom "
                "excluding female inheritance among Scheduled Tribes, denying "
                "a tribal woman an equal ancestral-property share is "
                "arbitrary; this is cited only as an illustration of the "
                "same title/control problem in a further community context, "
                "not as an extension of Vineeta Sharma's coparcenary "
                "doctrine, which applies within the Hindu Succession Act "
                "framework."
            ),
            "objection_reply": (
                "Objection: once law grants equal title, any remaining gap is "
                "a matter of social enforcement, not a flaw in the rights "
                "framework itself. Reply: a rights framework that predictably "
                "stops at title while ignoring foreseeable non-implementation "
                "across the other dimensions is philosophically incomplete; "
                "access, control, return and exit/security should be designed into the "
                "specification of the right, not treated as a separate "
                "implementation problem."
            ),
            "verdict": (
                "The statement is substantially correct: legal title is neither "
                "necessary nor sufficient for actual command; empowerment "
                "requires access, control, realised return and a stronger "
                "fall-back position across Agarwal's full analysis."
            ),
        },
    },
    {
        "marks": 20,
        "prompt": (
            "Examine the disagreement between Carole Pateman's 'sexual "
            "contract' and Susan Moller Okin's critique of the family as an "
            "object of justice."
        ),
        "primary_session": 8,
        "model_solution": {
            "intro": (
                "Pateman and Okin both extend feminist critique into liberal "
                "political theory's foundations, but target different "
                "structures: Pateman the social-contract tradition itself, "
                "Okin the Rawlsian treatment of the family."
            ),
            "body": (
                "Pateman argues the social contract tradition's story of free "
                "and equal contractors presupposes and masks a prior 'sexual "
                "contract' subordinating women, so the entire contractarian "
                "framework is compromised at its foundation. Okin, working "
                "more immanently within Rawlsian justice, argues that a theory "
                "of justice cannot consistently bracket the family as a "
                "private, pre-political sphere while claiming to regulate the "
                "basic structure of society, since the family is itself a "
                "site of unequal power distribution."
            ),
            "objection_reply": (
                "Objection: Okin's immanent critique, working within Rawls, "
                "might be thought to concede too much to liberal contract "
                "theory that Pateman would reject at the root. Reply: the two "
                "critiques are complementary rather than contradictory -- "
                "Pateman exposes the contract tradition's founding "
                "assumption, while Okin shows that even accepting a "
                "broadly Rawlsian framework, justice cannot stop at the "
                "household's threshold; both converge on the conclusion that "
                "the family cannot be exempted from justice's scope."
            ),
            "verdict": (
                "Pateman and Okin disagree on where the critique must begin "
                "(the contract's origin vs. the scope of a given theory of "
                "justice) but converge on the substantive conclusion that "
                "liberal political theory cannot treat the family as outside "
                "the reach of justice."
            ),
        },
    },
]

CURRENT_ANCHOR: dict[str, Any] = {
    "case_name": "Ram Charan & Ors. v. Sukhram & Ors.",
    "citation": "[2025] 8 S.C.R. 272",
    "neutral_citation": "2025 INSC 865",
    "decided": "17 July 2025",
    "forum": "Supreme Court of India",
    "kind": "Supreme Court judgment (not a statute)",
    "primary_session": 5,
    "holding_summary": (
        "Absent proven custom excluding female inheritance among Scheduled "
        "Tribes (a context outside Hindu Succession Act, 1956 section 2(2)), "
        "denying a tribal woman an equal share in ancestral property is "
        "arbitrary and offends Article 14; the Court invoked the standard of "
        "justice, equity, and good conscience under Section 6 of the Central "
        "Provinces Laws Act, 1875."
    ),
    "scope_note": (
        "Cited strictly as an illustration of the recurring title-versus-"
        "control problem in a further community context -- it is not part of "
        "the Hindu Succession Act coparcenary line, must not be presented as "
        "extending or amending Vineeta Sharma v. Rakesh Sharma (2020), and "
        "carries no load-bearing doctrinal weight beyond this illustrative "
        "use."
    ),
    "distinguished_from": (
        "Vineeta Sharma v. Rakesh Sharma (2020), which addresses coparcenary "
        "rights under the Hindu Succession Act, 2005 amendment; Ram Charan "
        "addresses a Scheduled Tribe inheritance dispute outside that "
        "statutory framework, decided on constitutional-equality and "
        "justice/equity/good-conscience grounds instead."
    ),
}


if __name__ == "__main__":
    assert len(SESSION_SPECS) == 10, f"SESSION_SPECS count {len(SESSION_SPECS)} != 10"
    _required_session_fields = {
        "title", "plain", "technical", "answer", "keywords", "usage", "mechanism",
        "consequence", "trap", "objection", "reply", "limit", "exam", "revision",
        "visuals",
    }
    for _i, _s in enumerate(SESSION_SPECS):
        _missing = _required_session_fields - set(_s.keys())
        assert not _missing, f"SESSION_SPECS[{_i}] missing fields: {_missing}"

    assert len(ASCII_PANELS) == 12, f"ASCII_PANELS count {len(ASCII_PANELS)} != 12"

    assert len(REQUIRED_TERMS) > 0, "REQUIRED_TERMS is empty"
    assert len(HEADER_KICKER) > 0, "HEADER_KICKER is empty"
    assert len(ADVANCED_SESSION_TITLES) == 2, (
        f"ADVANCED_SESSION_TITLES count {len(ADVANCED_SESSION_TITLES)} != 2"
    )
    assert len(OWNER_SESSION_RANGES) == 10, (
        f"OWNER_SESSION_RANGES count {len(OWNER_SESSION_RANGES)} != 10"
    )

    assert len(PYQ_SOLUTIONS) == 12, f"PYQ_SOLUTIONS count {len(PYQ_SOLUTIONS)} != 12"
    for _i, _p in enumerate(PYQ_SOLUTIONS):
        assert 2018 <= _p["year"] <= 2025, f"PYQ_SOLUTIONS[{_i}] year out of range"
        _ma = _p["model_answer"]
        for _k in ("intro", "body", "objection_reply", "verdict"):
            assert _ma.get(_k), f"PYQ_SOLUTIONS[{_i}] model_answer missing '{_k}'"

    assert len(MCQS) == 48, f"MCQS count {len(MCQS)} != 48"
    _answer_sequence = "".join(_m["answer"] for _m in MCQS)
    _expected_sequence = "ABCD" * 12
    assert _answer_sequence == _expected_sequence, (
        "MCQ answer rotation broken: "
        f"got {_answer_sequence!r} expected {_expected_sequence!r}"
    )
    for _i, _m in enumerate(MCQS):
        assert len(_m["options"]) == 4, f"MCQS[{_i}] does not have exactly 4 options"

    assert len(ORIGINAL_MAINS) == 6, f"ORIGINAL_MAINS count {len(ORIGINAL_MAINS)} != 6"
    _marks_tally = sorted(_o["marks"] for _o in ORIGINAL_MAINS)
    assert _marks_tally == [10, 10, 15, 15, 20, 20], (
        f"ORIGINAL_MAINS marks distribution unexpected: {_marks_tally}"
    )

    assert CURRENT_ANCHOR, "CURRENT_ANCHOR is empty"
    for _k in (
        "case_name", "citation", "neutral_citation", "decided", "primary_session",
        "holding_summary", "scope_note", "distinguished_from",
    ):
        assert CURRENT_ANCHOR.get(_k), f"CURRENT_ANCHOR missing '{_k}'"

    print("All learner-v2 Gender Discrimination spec assertions passed.")
    print(f"SESSION_SPECS={len(SESSION_SPECS)} ASCII_PANELS={len(ASCII_PANELS)} "
          f"PYQ_SOLUTIONS={len(PYQ_SOLUTIONS)} MCQS={len(MCQS)} "
          f"ORIGINAL_MAINS={len(ORIGINAL_MAINS)} REQUIRED_TERMS={len(REQUIRED_TERMS)} "
          f"OWNER_SESSION_RANGES={len(OWNER_SESSION_RANGES)}")


REQUIRED_TERMS.extend(
    [
        "exact printed ownership",
        "trans-inclusive",
        "gender identity",
        "gender expression",
        "Mary Wollstonecraft",
        "Harriet Taylor Mill",
        "bell hooks",
        "Iris Marion Young",
        "structural injustice",
        "social connection",
        "sameness/difference",
        "redistribution",
        "representation",
        "disability",
        "sexuality",
    ]
)
REQUIRED_CORE_TERMS = tuple(REQUIRED_TERMS)


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
    if generation != 7:
        raise ValueError(
            f"Gender Discrimination semantic successor is pinned to g7, got g{generation}."
        )

    text = re.sub(
        r"(?m)^!\[Gender Discrimination[^\]]*\]\([^)]+\)\s*\n+"
        r"\*Concept map:.*?\*\s*\n*",
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
    category_scope = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 1.3B Category scope and trans-inclusive conceptual care",
            "### 1.4 Main feminist diagnoses",
        )
    )
    thinkers_structure = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 1.4A Bounded thinker map",
            "### 1.5 Difference, equality and discrimination",
        )
    )
    sameness = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 1.5A The sameness/difference dilemma",
            "### 1.6 Objections and replies",
        )
    )
    justice_dimensions = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 4.8A Redistribution, recognition and representation",
            "## 5. INTER-THINKER / INTER-SCHOOL DEBATES",
        )
    )
    intersection = _demote_owner(
        _extract_owner_section(
            owner_text,
            "### 5.6A Intersectional mediation beyond an additive list",
            "## 6. CRITICISMS AND REPLIES",
        )
    )

    text = text.replace(
        "> **Syllabus (verbatim):** Gender Discrimination: Female Foeticide, "
        "Land and Property Rights, Empowerment.",
        "> **Syllabus (verbatim):** Gender Discrimination : Female Foeticide, "
        "Land and Property Rights; Empowerment.",
        1,
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + boundary,
            1,
        )
    text = text.replace(
        "**Plain-language definition:** Sex is the biological fact of being male "
        "or female; gender is what a society decides that biological fact should "
        "mean -- roles, virtues, and limits.",
        "**Plain-language definition:** Sex refers to bodily and reproductive "
        "characteristics whose variation is more complex than a rigid binary; "
        "gender is the socially organised meaning attached to bodies, identities, "
        "roles, virtues and limits.",
        1,
    )
    text = text.replace(
        "  relational deficit read as 'natural' inferiority\n",
        "  relational deficit read as 'natural' inferiority\n"
        "  CATEGORY CARE: sex characteristics != assignment != identity/"
        "expression/role\n",
        1,
    )
    if "#### 1.3B Category scope and trans-inclusive conceptual care" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Gender as a Cultural Category and "
            "Butler's Performativity",
            category_scope
            + "\n\n#### CLOSING RECALL FLOW — Gender as a Cultural Category and "
            "Butler's Performativity",
            1,
        )
    if "#### 1.4A Bounded thinker map" not in text:
        text = text.replace(
            "#### 1.5 Difference, equality and discrimination",
            thinkers_structure + "\n\n#### 1.5 Difference, equality and discrimination",
            1,
        )
    if "#### 1.5A The sameness/difference dilemma" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Feminist Diagnoses and the Architecture "
            "of Equality",
            sameness
            + "\n\n#### CLOSING RECALL FLOW — Feminist Diagnoses and the "
            "Architecture of Equality",
            1,
        )
    if "#### 4.8A Redistribution, recognition and representation" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Care Ethics, the Limits of Empowerment "
            "and Political Representation",
            justice_dimensions
            + "\n\n#### CLOSING RECALL FLOW — Care Ethics, the Limits of "
            "Empowerment and Political Representation",
            1,
        )
    if "#### 5.6A Intersectional mediation beyond an additive list" not in text:
        text = text.replace(
            "#### CLOSING RECALL FLOW — Gender, Caste and Multiculturalism: The "
            "Indian Intersection",
            intersection
            + "\n\n#### CLOSING RECALL FLOW — Gender, Caste and "
            "Multiculturalism: The Indian Intersection",
            1,
        )

    text = text.replace(
        "17. **Do not overstate the reach of any statute or judgment.** ⚠️ The "
        "2005 amendment and *Vineeta Sharma* (2020) settle coparcenary entitlement "
        "in law; they establish neither possession, control, return nor exit "
        "(§3.3, §3.4).",
        "17. **Do not overstate the reach of any statute or judgment.** ⚠️ The "
        "2005 amendment and *Vineeta Sharma* (2020) settle coparcenary entitlement "
        "in law; they establish neither possession, control, return nor exit "
        "(§3.3, §3.4).\n"
        "18. **Do not treat women as a homogeneous class.**\n"
        "19. **Do not make anatomy, dress or role a proxy for gender identity.**\n"
        "20. **Do not resolve the sameness/difference dilemma by slogan.**\n"
        "21. **Do not collapse redistribution, recognition and representation.**\n"
        "22. **Do not confuse structural responsibility with collective guilt.**\n"
        "23. **Do not import non-routed feminist schools as a generic list.**",
        1,
    )
    text = text.replace(
        "**Promoted vocabulary (this pass) ⚠️:** performativity",
        "**Promoted vocabulary (this pass) ⚠️:** trans-inclusive category care · "
        "Wollstonecraft · Mill/Taylor · bell hooks · Young's social connection · "
        "structural responsibility · sameness/difference dilemma · redistribution/"
        "recognition/representation · disability and sexuality mediation · "
        "performativity",
        1,
    )
    if "G17 · Structural injustice creates responsibility" not in text:
        text = text.replace(
            "- **G16 · Indian legal instruments, correctly classified.** Claim: "
            "PCPNDT Act **1994** — enacted statute; Hindu Succession (Amendment) "
            "Act **2005** — enacted amendment conferring coparcenary status by "
            "birth on statutory terms; *Vineeta Sharma v. Rakesh Sharma* (**2020**) "
            "— Supreme Court judgment clarifying that right; Constitution (One "
            "Hundred and Sixth Amendment) Act **2023** — enacted amendment whose "
            "reservation provisions are linked to a future census-based "
            "delimitation → Use for: the Indian paragraph in any answer → Limit: "
            "✅ each is a dated legal fact; ❌ none establishes possession, control "
            "or completed implementation, and none is philosophical proof.",
            "- **G16 · Indian legal instruments, correctly classified.** Claim: "
            "PCPNDT Act **1994** — enacted statute; Hindu Succession (Amendment) "
            "Act **2005** — enacted amendment conferring coparcenary status by "
            "birth on statutory terms; *Vineeta Sharma v. Rakesh Sharma* (**2020**) "
            "— Supreme Court judgment clarifying that right; Constitution (One "
            "Hundred and Sixth Amendment) Act **2023** — enacted amendment whose "
            "reservation provisions are linked to a future census-based "
            "delimitation → Use for: the Indian paragraph in any answer → Limit: "
            "✅ each is a dated legal fact; ❌ none establishes possession, control "
            "or completed implementation, and none is philosophical proof.\n"
            "- **G17 · Structural injustice creates responsibility without one "
            "sole author.** Forward-looking duties are graded by power, privilege, "
            "interest and collective capacity → Named: Young → Use: 2025 Q1(b) "
            "→ Limit: shared responsibility must not erase personal blame.\n"
            "- **G18 · Equality faces a sameness/difference dilemma.** Identical "
            "rules can encode a male norm; accommodation can essentialise "
            "difference → Use: equality/empowerment stems → Limit: remedies must "
            "be proportionate and revisable.\n"
            "- **G19 · Gender justice has three dimensions.** Redistribution "
            "addresses resources, recognition status and representation voice → "
            "Use: property, empowerment and representation → Limit: full "
            "recognition theory is owned elsewhere.\n"
            "- **G20 · Intersectionality changes the mechanism.** Caste, class, "
            "community, disability and sexuality/gender identity mediate gendered "
            "institutions → Named: Crenshaw and hooks → Limit: coalition still "
            "requires common dignity/equality claims.",
            1,
        )
    text = text.replace("G1-G16", "G1-G20")
    text = text.replace(
        "- Local course source, *Socio-Political Philosophy*, sections on "
        "empowerment, female foeticide and women's property rights.",
        "- Local compiled notes PDF, *Socio-Political Philosophy*, searchable "
        "pp. 188-197; no named author is asserted.",
    )
    text = text.replace(
        "- O. P. Gauba, *An Introduction to Political Theory*, discussions of "
        "feminist political theory, equality and power.",
        "- O. P. Gauba, *An Introduction to Political Theory*, discussions of "
        "feminist political theory, equality and power.\n"
        "- Mary Wollstonecraft, *A Vindication of the Rights of Woman*; J. S. "
        "Mill and Harriet Taylor Mill, writings on women's equality.\n"
        "- Iris Marion Young, *Responsibility for Justice*; bell hooks, *Feminist "
        "Theory: From Margin to Center*.",
        1,
    )
    text = text.replace(
        "seat allocation / effective representation -- PENDING as of 30-Aug-2026",
        "seat allocation / effective representation -- PENDING as of 03-Sep-2026",
    )
    text = text.replace(
        "seat-level operation remained pending as accessed on 30 August 2026",
        "seat-level operation remained pending as checked on 3 September 2026",
    )
    text = text.replace(
        "seat allocation / effective representation: PENDING 30-Aug-2026",
        "seat allocation / effective representation: PENDING 03-Sep-2026",
    )
    text = text.replace(
        "clarifies retrospective scope",
        "father alive at commencement not required",
    )
    text = text.replace(
        "clarifying its retrospective scope.",
        "clarifying that the coparcenary right is by birth and does not require "
        "the father to have been alive on 9 September 2005.",
    )
    text = text.replace("retrospective application", "retroactive application")
    text = text.replace("retrospective\n", "retroactive\n")
    text = text.replace(
        "the optional Advanced module on Iris Marion Young's structural-injustice "
        "model extends, but is not required for, this core synthesis.",
        "Young's social-connection model is now Core for the 2025 construct-to-"
        "opportunity demand; the optional Advanced module only extends its "
        "blame/responsibility dispute.",
    )
    text = text.replace(
        "- Advanced (optional) link: Iris Marion Young's structural injustice model.",
        "- Core link: Iris Marion Young's structural-injustice and social-"
        "connection model; optional depth retains only the residual dispute.",
    )
    text = text.replace(
        "Still to promote if a PYQ asks it directly: Young-style structural "
        "injustice and the blame/responsibility split.",
        "Young-style structural injustice fired through the 2025 construct-to-"
        "opportunity/resource demand and was promoted on 3 September 2026; only "
        "the second-order blame/responsibility dispute remains optional.",
    )
    text = text.replace(
        "| Structural injustice | Wrong can be reproduced by many ordinary actions "
        "without one sole culprit; rival views prefer agent-centred blame | "
        "Genuinely optional: sharpens empowerment and foeticide analysis beyond "
        "the minimum |",
        "| Structural injustice | Wrong can be reproduced by many ordinary actions "
        "without one sole culprit; rival views prefer agent-centred blame | Core "
        "through the 2025 demand; optional residue concerns how shared forward-"
        "looking responsibility relates to personal blame |",
    )
    text = text.replace(
        "- Constitution (One Hundred and Sixth Amendment) Act, 2023, used with "
        "its census/delimitation condition as an enacted—not fully implemented—"
        "illustration.",
        "- Constitution (One Hundred and Sixth Amendment) Act, 2023, used with "
        "Gazette notification S.O. 1922(E), 16 April 2026, and its census/"
        "delimitation condition as an enacted—not fully implemented—illustration.",
    )
    return text
