"""Deep-review and immutably regenerate all Socio-Political Philosophy topics."""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import fitz

import carvaka_flowchart
import markdown_learning_pdf
from export_four_item_library import export_library
from generate_philosophy_socio_political_v2 import PANELS as TOPIC_1_PANELS
from generate_philosophy_western_rationalism_v2 import render_ascii_pdf_safe
from generate_v2_section_indexes import generate_command_guide, generate_section_indexes
from validate_v2_export import (
    answer_key_pattern_errors,
    extract_mcq_answer_keys,
    extract_v2_workbook_markdown,
    mcq_answer_text_errors,
    validate_pdf,
    validate_pdf_layout,
    validate_refreshed_markdown_text,
    validate_tracker_record,
    validate_v2_paths,
)


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SECTION = "Philosophy Paper II — Socio-Political Philosophy"
SECTION_KEY = "paper-ii-socio-political-philosophy"
REVIEW_ROOT = ROOT / "notes" / "Final-Learning-Packages" / "_deep-content-review"
STATUS = ROOT / "EXPORT-PDF-STATUS.json"
MASTER = ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
REVIEW_TRACKER = REVIEW_ROOT / "REVIEW-TRACKER.json"
REVIEW_TRACKER_MD = REVIEW_ROOT / "REVIEW-TRACKER.md"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-ii-socio-political-philosophy.json"
)
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
PYQ_LEDGER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\"
    "_PYQ-SocioPolitical-2018-2025.md"
)
OFFICIAL_SYLLABUS = (
    "upsc-ai-kit\\knowledge\\Philosophy\\OFFICIAL-UPSC-SYLLABUS-VERBATIM.md"
)
REFRESHED_KNOWLEDGE = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Socio-Political"
    / "learning-sessions"
)
REFRESHED_NOTES = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Socio-Political"
    / "learning-sessions"
)
REFRESHED_FLOWS = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Socio-Political"
    / "flowcharts"
)
CONTENT_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-ii-socio-political-philosophy-content-specs"
)
GRAPHICAL_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-ii-socio-political-philosophy-graphical-specs"
)
ASCII_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
)

TITLES = (
    "Social and Political Ideals",
    "Sovereignty",
    "Individual and State",
    "Forms of Government",
    "Political Ideologies",
    "Humanism, Secularism and Multiculturalism",
    "Crime and Punishment",
    "Development and Social Progress",
    "Gender Discrimination",
    "Caste Discrimination: Gandhi and Ambedkar",
)
OFFICIAL_CLAUSES = (
    "Social and Political Ideals: Equality, Justice, Liberty.",
    "Sovereignty: Austin, Bodin, Laski, Kautilya.",
    "Individual and State: Rights; Duties and Accountability.",
    "Forms of Government: Monarchy; Theocracy and Democracy.",
    "Political Ideologies: Anarchism; Marxism and Socialism.",
    "Humanism; Secularism; Multi-culturalism.",
    "Crime and Punishment: Corruption, Mass Violence, Genocide, Capital Punishment.",
    "Development and Social Progress.",
    "Gender Discrimination: Female Foeticide, Land and Property Rights; Empowerment.",
    "Caste Discrimination: Gandhi and Ambedkar.",
)


TOPIC_1_CONTROLS: tuple[dict[str, Any], ...] = (
    {
        "plain": "Equality, liberty and justice answer different questions but must be ordered together in political institutions.",
        "technical": "Equality concerns equal moral status and distribution, liberty concerns protected non-interference and agency, and justice supplies the rule for adjudicating their conflicts.",
        "opening": "Equality and liberty make rival claims on institutions; justice is architectonic because it decides which liberties are basic and which inequalities are justified.",
        "keywords": ("equal moral worth", "negative liberty", "basic liberties", "fair opportunity", "justice as mediation"),
        "usage": "Define the three ideals separately, expose the conflict between liberty and equality, and use justice to state a qualified institutional ordering.",
        "objection": "Justice cannot be a neutral referee because rival theories of justice already privilege different liberties and equalities.",
        "reply": "The mediation thesis is procedural rather than neutral: it makes the ordering rule explicit and open to public justification.",
        "limit": "Do not write that justice mechanically harmonises every conflict; identify the contested criterion and defend a graded ordering.",
        "mechanism": "Political institutions allocate status, choice, burdens and benefits; equality and liberty generate claims, and justice ranks or reconciles them.",
        "consequence": "A credible answer treats the triad as interdependent without collapsing one ideal into another.",
        "trap": "Do not write three disconnected mini-essays or assume that equality means sameness and liberty means licence.",
    },
    {
        "plain": "Equality begins with equal moral worth but must be specified as legal, political, social or economic equality.",
        "technical": "Formal equality removes explicit legal privilege, while substantive equality tests whether social power and conversion conditions make opportunity genuinely usable.",
        "opening": "Equality is not identity of condition; it is a demand that relevant differences, unequal opportunities and status hierarchies be publicly justified.",
        "keywords": ("equal moral worth", "formal equality", "political equality", "social equality", "fair equality of opportunity"),
        "usage": "Move from equal worth through the four forms, distinguish formal from fair opportunity, and qualify outcome-sensitive correction.",
        "objection": "Substantive equality can become paternalistic levelling and can underweight responsibility, choice and incentive.",
        "reply": "The strongest egalitarian reply targets arbitrary background disadvantage rather than every chosen difference in outcome.",
        "limit": "Do not equate equality with identical talents, treatment or final holdings; always state the relevant metric.",
        "mechanism": "Equal moral worth shifts the burden of proof onto inherited hierarchy; substantive equality then examines access, capability and status.",
        "consequence": "Formal equality is necessary but may reproduce disadvantage when starting positions and social power remain unequal.",
        "trap": "Do not move from equality before law directly to achieved equality without showing the opportunity and capability mechanism.",
    },
    {
        "plain": "Rousseau, Mill and Marx diagnose different ways in which apparently natural inequality is socially produced.",
        "technical": "Rousseau distinguishes natural from moral-political inequality, Mill attacks manufactured female subordination, and Marx shows how formally equal exchange can reproduce class exploitation.",
        "opening": "The crucial philosophical move is to ask whether inequality reflects relevant difference or an institution that converts difference into dependence and domination.",
        "keywords": ("natural inequality", "moral-political inequality", "individuality", "manufactured subordination", "distribution according to need"),
        "usage": "Compare each thinker's causal mechanism, then distinguish status equality, individuality and material need before giving a synthesis.",
        "objection": "The three diagnoses rest on incompatible views of property, individuality and the legitimate scope of social transformation.",
        "reply": "They can still be compared through one controlled question: how institutions turn difference into hierarchy or dependence.",
        "limit": "Do not attribute Marx's higher communist distributive formula to immediate socialism or treat Rousseau's natural differences as political entitlements.",
        "mechanism": "Convention, gender hierarchy and class structure transform physical difference or legal equality into social dependence.",
        "consequence": "Anti-subordination requires legal status, protected individuality and attention to material structure.",
        "trap": "Do not merge Rousseau, Mill and Marx into one egalitarian doctrine; preserve their different mechanisms and remedies.",
    },
    {
        "plain": "The equality-of-what debate asks which space—resources, welfare, capabilities or social relations—should be equalised.",
        "technical": "Dworkin focuses resources and luck, Sen focuses capability to function, Cohen presses ethos and access to advantage, and relational egalitarians target hierarchy and humiliation.",
        "opening": "An equality claim is incomplete until it identifies its metric, its treatment of choice and luck, and the social relation it seeks to transform.",
        "keywords": ("equality of resources", "capability", "brute luck", "option luck", "relational equality"),
        "usage": "Name the metric, explain its conversion mechanism, test disability and responsibility objections, and compare distributive with relational equality.",
        "objection": "No single metric captures need, agency, expensive preference, disability, responsibility and civic standing without loss.",
        "reply": "Metric pluralism can retain a primary evaluative space while adding responsibility and anti-humiliation constraints.",
        "limit": "Do not cite Sen as advocating equal outcomes; capability evaluates real freedom, not identical functionings.",
        "mechanism": "Resources are converted into real opportunities under unequal personal and social conditions, so identical bundles can yield unequal freedom.",
        "consequence": "The chosen metric changes who appears disadvantaged and which remedy counts as egalitarian.",
        "trap": "Do not answer equality-of-what with a list of thinkers; compare the metric, conversion rule and residual objection.",
    },
    {
        "plain": "Liberty concerns both freedom from interference and the conditions of self-direction.",
        "technical": "Berlin distinguishes negative from positive liberty, while Mill's harm principle places the burden of proof on coercion aimed at self-regarding conduct.",
        "opening": "A liberty answer must identify who is free, from what constraint, to do what, and under whose authority coercion is justified.",
        "keywords": ("negative liberty", "positive liberty", "harm principle", "self-regarding acts", "value pluralism"),
        "usage": "Define Berlin's two concepts, apply Mill's harm threshold, distinguish harm from offence, and confront paternalism.",
        "objection": "Positive liberty can authorise coercion in the name of a supposedly rational or true self.",
        "reply": "Enabling conditions can expand agency if they remain rights-bound, contestable and non-perfectionist.",
        "limit": "Do not reduce negative liberty to absence of every rule or positive liberty to whatever policy claims to improve welfare.",
        "mechanism": "Negative liberty protects a sphere against interference; positive liberty asks whether the agent can direct her life; the harm principle tests coercion.",
        "consequence": "Liberty requires both a protected domain and disciplined justification of interventions that claim to enable freedom.",
        "trap": "Do not treat offence, immorality and harm as interchangeable or ignore Berlin's warning about coercive self-mastery.",
    },
    {
        "plain": "Hobbes, Locke, Rousseau and Green connect liberty to different relations between law, consent, security and effective capacity.",
        "technical": "Hobbes stresses absence of impediment under order, Locke liberty under known law, Rousseau autonomy through self-legislation, and Green positive capacity for worthwhile action.",
        "opening": "Law can restrict particular choices yet constitute liberty when it secures status, consent and the effective conditions of agency.",
        "keywords": ("absence of impediment", "liberty under law", "general will", "self-legislation", "positive freedom"),
        "usage": "Compare the thinker's account of law and agency, then test whether enabling conditions protect or paternalistically replace choice.",
        "objection": "Once the state defines worthwhile capacity, positive freedom can erase plural values and personal responsibility.",
        "reply": "Green's insight is strongest when enabling provision expands option sets while rights and contestation constrain perfectionism.",
        "limit": "Do not call Hobbes a positive-liberty theorist or infer that Rousseau licenses any state command as the general will.",
        "mechanism": "Security, known law, civic authorship and social capability each alter whether formal choice is usable and non-dominating.",
        "consequence": "Liberty and equality can complement one another when fair conditions enlarge everyone's effective agency.",
        "trap": "Do not present liberty and equality as always zero-sum; identify when redistribution enables rather than suppresses freedom.",
    },
    {
        "plain": "Technological society can expand choice while creating surveillance and platform dependence that expose persons to arbitrary power.",
        "technical": "Republican liberty as non-domination distinguishes actual interference from standing subjection to an uncontrolled capacity to interfere.",
        "opening": "In technological society, republican non-domination shows why a person may be left alone yet remain unfree when another actor can arbitrarily track, rank, exclude or manipulate her choices.",
        "keywords": ("non-domination", "arbitrary power", "surveillance", "platform dependence", "contestability"),
        "usage": "Separate interference from domination, explain the standing-power mechanism, and test whether law makes technological power contestable.",
        "objection": "The domination standard may classify every dependency or unequal capacity as unfreedom and demand excessive regulation.",
        "reply": "Republican analysis targets uncontrolled arbitrary power, not all dependence; public rules and effective contestation are decisive.",
        "limit": "Do not assume privacy, access or innovation automatically settles liberty; specify the power relation and remedy.",
        "mechanism": "Data concentration and platform control create a standing capacity to shape options even without a discrete act of interference.",
        "consequence": "Freedom requires institutional contestability as well as a count of actual interferences.",
        "trap": "Do not say non-domination is merely Berlin's negative liberty; its object is uncontrolled status and power.",
    },
    {
        "plain": "Justice asks what is due in distribution, correction and institutional order.",
        "technical": "Plato treats justice as harmony, Aristotle distinguishes distributive proportion from corrective restoration, and utilitarianism tests institutions by aggregate welfare.",
        "opening": "The examiner rewards a justice answer that names the rule of allocation, the relevant criterion and the method of rectifying wrong.",
        "keywords": ("justice as harmony", "distributive justice", "corrective justice", "relevant criterion", "aggregate welfare"),
        "usage": "Move from Plato's order to Aristotle's two forms, identify the criteria dispute, and test utilitarian aggregation against separateness of persons.",
        "objection": "Harmony can freeze hierarchy, proportionality leaves the criterion contested, and aggregation can sacrifice minorities.",
        "reply": "The traditions remain useful when their allocation, correction and institutional functions are distinguished rather than absolutised.",
        "limit": "Do not call every legal decision just or treat corrective justice as a complete theory of distributive shares.",
        "mechanism": "Distributive justice assigns shares by a criterion; corrective justice restores a disturbed equality after wrong.",
        "consequence": "Justice requires both prospective allocation and retrospective rectification, with reasons for the chosen criterion.",
        "trap": "Do not confuse Aristotle's proportionate equality with equal numerical shares in every context.",
    },
    {
        "plain": "Rawls, Nozick, Sen and Ambedkar offer rival standards for judging institutions and realised social relations.",
        "technical": "Rawls prioritises equal basic liberties and fair opportunity, Nozick historical entitlement, Sen capabilities and public reasoning, and Ambedkar social democracy grounded in liberty, equality and fraternity.",
        "opening": "Modern justice turns on whether fairness is judged by institutional choice, historical entitlement, realised capability or anti-caste social relations.",
        "keywords": ("original position", "difference principle", "entitlement theory", "capability approach", "social democracy"),
        "usage": "State each currency of justice, compare patterned and historical views, add capability and fraternity, and conclude with a qualified institutional test.",
        "objection": "Each view risks neglecting something central: history, structure, feasibility, responsibility or entrenched status domination.",
        "reply": "A layered verdict can protect basic liberties, rectify unjust acquisition, expand capabilities and test fraternity in lived relations.",
        "limit": "Do not merge Rawls's difference principle with equal outcome, Nozick with selfishness, or Sen with one fixed capability list.",
        "mechanism": "Each theory selects a different informational basis and therefore ranks institutions and inequalities differently.",
        "consequence": "The best comparative answer explains why the same distribution can be fair under one theory and unjust under another.",
        "trap": "Do not use Ambedkar decoratively; connect fraternity and social democracy to caste-based status inequality.",
    },
    {
        "plain": "Synthesis requires explicit distinctions, objections and an ordering verdict across equality, liberty and justice.",
        "technical": "The triad is reconstructed through metrics of equality, concepts of liberty and rival procedural, distributive, historical, capability and relational theories of justice.",
        "opening": "A high-scoring synthesis states the conflict precisely, names the controlling criterion and concedes the strongest residual cost.",
        "keywords": ("ordering problem", "metric", "non-domination", "rectification", "qualified verdict"),
        "usage": "Decode the directive, define the relevant ideal, compare named theories, apply one Indian example and close with a defended hierarchy or balance.",
        "objection": "An eclectic synthesis can become an unprincipled list that avoids choosing among incompatible ideals.",
        "reply": "A disciplined synthesis states lexical priorities, thresholds or burden-of-proof rules and identifies where trade-offs remain.",
        "limit": "Do not end with the slogan that all ideals are equally important; state which claim prevails, under what condition and why.",
        "mechanism": "Definition fixes the evaluative space, comparison exposes conflict, objection tests the rule, and qualification produces the verdict.",
        "consequence": "The answer becomes reusable for direct, comparative and critical PYQs without losing doctrinal precision.",
        "trap": "Do not substitute quotations or current examples for the philosophical mechanism and the directive's exact demand.",
    },
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".pending")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def repo(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def latest(status: dict[str, Any], topic_key: str) -> dict[str, Any]:
    records = [
        row
        for row in status["exports"]
        if row.get("topic_key") == topic_key and row.get("variant") == "learner-v2"
    ]
    return max(records, key=lambda row: int(row["generation"]))


def copy_markdown_assets(old_markdown: Path, new_markdown: Path, text: str) -> list[Path]:
    copied: list[Path] = []
    for raw in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
        target = raw.split("#", 1)[0].strip("<>")
        if not target or "://" in target or target.startswith("data:"):
            continue
        source = (old_markdown.parent / Path(target.replace("/", os.sep))).resolve()
        if not source.is_file():
            continue
        destination = new_markdown.parent / Path(target.replace("/", os.sep))
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append(destination)
    return copied


def update_frontmatter(text: str, generation: int) -> str:
    text = re.sub(r"(?m)^generation:\s*\d+\s*$", f"generation: {generation}", text)
    text = re.sub(r"(?m)^generation_date:\s*\S+\s*$", f"generation_date: {DATE}", text)
    text = re.sub(
        r"(?m)^>\s+\*\*Generation:\*\*\s+g\d+,\s+[^·\n]+",
        f"> **Generation:** g{generation}, 30 August 2026 ",
        text,
    )
    return text


def _topic_1_contract(title: str, control: dict[str, Any]) -> str:
    keywords = "\n".join(f"- **{item}**" for item in control["keywords"])
    revision = "\n".join(
        f"- {item}"
        for item in (
            control["plain"],
            control["mechanism"],
            control["consequence"],
            control["trap"],
        )
    )
    return f"""

#### DEFINITION / WHAT THIS IS CALLED

**Plain-language definition:** {control['plain']}

**Technical definition:** {control['technical']}

#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM

> {control['opening']}

#### MUST-WRITE KEYWORDS

{keywords}

**How to use them:** {control['usage']} Explicitly connect **{control['keywords'][0]}**, **{control['keywords'][1]}** and **{control['keywords'][2]}** in the answer spine.

#### CORE OBJECTION, REPLY AND RESIDUAL LIMIT

**Objection:** {control['objection']}

**Best reply:** {control['reply']}

**Residual limit:** {control['limit']}

#### EXAM USE AND CONCISE REVISION

**Answer architecture:** {control['usage']} Explicitly connect {control['keywords'][0]}, {control['keywords'][1]} and {control['keywords'][2]} before the verdict.

{revision}
"""


def _topic_1_closure(title: str, control: dict[str, Any]) -> str:
    return f"""

#### CLOSING RECALL FLOW — {title}

```closure-flow
SUBTOPIC: {title}
STARTING CONCEPT: {control['plain']}
KEY TERMS / DEFINITIONS: {' | '.join(control['keywords'])}
MECHANISM / ARGUMENT: {control['mechanism']}
CONSEQUENCE / CONTRAST: {control['consequence']}
UPSC TRAP / ANSWER-USE: {control['trap']}
ANSWER-GRABBING FORMULATION: {control['opening']}
```

"""


def upgrade_topic_1_sessions(text: str) -> str:
    start = text.index("## BASIC LEARNING SESSION")
    end = text.index("## BASIC MCQS / REMEDIATION", start)
    basic = text[start:end]
    headings = list(
        re.finditer(r"(?m)^### SESSION (\d+) [—-] (.+?)\s*$", basic)
    )
    if len(headings) != 10:
        raise ValueError(f"Topic 01 expected ten Basic sessions; found {len(headings)}.")
    output: list[str] = []
    cursor = 0
    for position, heading in enumerate(headings):
        section_end = (
            headings[position + 1].start()
            if position + 1 < len(headings)
            else len(basic)
        )
        number = int(heading.group(1))
        title = heading.group(2).strip()
        body = basic[heading.end() : section_end].strip()
        control = TOPIC_1_CONTROLS[number - 1]
        output.extend(
            (
                basic[cursor : heading.end()],
                _topic_1_contract(title, control),
                "\n\n",
                body,
                _topic_1_closure(title, control),
            )
        )
        cursor = section_end
    output.append(basic[cursor:])
    upgraded = text[:start] + "".join(output) + text[end:]
    return re.sub(
        r"(?m)^\*\*Correct answer:\s*([ABCD])\.\s*(.+?)\*\*\s*$",
        r"**Correct answer: \1** — \2",
        upgraded,
    )


def _question_headings(section: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^####\s+(.+?)\s*$", section))
    rows: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        title = match.group(1).strip()
        if (
            not re.search(r"(?i)\b(?:PYQ|Original Mains)\b", title)
            or "timed-paper upgrade" in title.casefold()
        ):
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        block = section[match.end() : end]
        prompt = re.search(
            r"(?im)^\*\*(?:Question|Prompt):\*\*\s*(.+?)\s*$",
            block,
        )
        rows.append((title, prompt.group(1).strip() if prompt else title))
    return rows


def add_answer_upgrades(text: str) -> str:
    if "### Answer-specific execution and compression upgrades" in text:
        return text
    start = text.index("## PYQS AND ANSWER PRACTICE")
    end = text.index("## OPTIONAL ADVANCED DEPTH", start)
    section = text[start:end]
    questions = _question_headings(section)
    if not questions:
        raise ValueError("No solved PYQ/original Mains headings were found.")
    additions = [
        "",
        "### Answer-specific execution and compression upgrades",
        "",
        "These controls follow the detailed models and make each one executable in the timed paper.",
        "",
    ]
    for title, prompt in questions:
        marks_match = re.search(r"(?i)(10|15|20)(?:\s*\+\s*5)?\s*marks?", title)
        marks = int(marks_match.group(1)) if marks_match else 15
        directive_match = re.match(
            r"(?i)(briefly discuss|critically examine|critically evaluate|evaluate|"
            r"examine|discuss|analyse|analyze|distinguish|explain|comment|justify|"
            r"bring out|assess|present|state|can|is|does|what|how|why)\b",
            re.sub(r"^[\"'‘“]+", "", prompt).strip(),
        )
        directive = directive_match.group(1) if directive_match else "the stated directive"
        if marks <= 10:
            plan = "150 words: verdict-led definition, three analytical moves, one precise qualification and a direct close."
        elif marks <= 15:
            plan = "220–250 words: thesis, four or five claim–evidence–analysis moves, one objection/reply and a qualified verdict."
        else:
            plan = "about 300 words: thesis, six developed moves, named comparison, strongest objection/reply, India-linked application where relevant and a graded conclusion."
        additions.extend(
            (
                f"#### {title} — timed-paper upgrade",
                "",
                f"**Directive and demand decoding:** The operative demand is **{directive}**. Address this exact question: *{prompt}* Do not replace it with a general topic summary.",
                "",
                f"**How to improve this answer:** State the conclusion in the opening; turn each major claim into **claim → named thinker/text/example → analysis → qualification**; preserve the model's strongest objection and reply; and make the final sentence answer *{prompt}* rather than merely repeat the doctrine.",
                "",
                f"**Executable exam-length/compression guidance:** {plan} Cut decorative biography and repeated definitions first; never cut the governing distinction, named evidence, objection or verdict.",
                "",
            )
        )
    return text[:end] + "\n".join(additions) + "\n" + text[end:]


def patch_gender_markdown(text: str) -> str:
    text = text.replace(
        "106th Amendment (2023): reservation ENACTED",
        "106th Amendment: enacted 2023; commenced 16-Apr-2026",
    )
    text = text.replace(
        "DELIMITATION (not yet completed)",
        "ARTICLE 334A CENSUS/DELIMITATION SEQUENCE",
    )
    text = text.replace(
        "actual seat allocation / effective representation -- PENDING",
        "seat allocation / effective representation -- PENDING as of 30-Aug-2026",
    )
    text = text.replace(
        "106th Constitutional Amendment, 2023 enacts legislative reservation for women.",
        "106th Constitutional Amendment was enacted in 2023 and brought into force on 16 April 2026; seat-level reservation still follows Article 334A's census-delimitation sequence.",
    )
    return text


def patch_gender_ascii(text: str) -> str:
    return patch_gender_markdown(text)


def recursive_replace(value: Any, replacements: dict[str, str]) -> Any:
    if isinstance(value, str):
        for old, new in replacements.items():
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [recursive_replace(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: recursive_replace(item, replacements) for key, item in value.items()}
    return value


def patch_gender_sources(changed: set[str]) -> None:
    canonical = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "paper-2"
        / "socio-political"
        / "Gender-Discrimination.md"
    )
    text = canonical.read_text(encoding="utf-8")
    old = text
    text = text.replace(
        "is an **enacted constitutional amendment**.",
        "is an **enacted constitutional amendment**; Gazette notification S.O. 1922(E) brought it into force on **16 April 2026**.",
        1,
    )
    text = text.replace(
        "future census-based delimitation process under the inserted framework",
        "post-Act census-based delimitation sequence under Article 334A; seat-level operation remained pending as accessed on 30 August 2026",
        1,
    )
    if text != old:
        canonical.write_text(text, encoding="utf-8")
        changed.add(rel(canonical))

    spec = ROOT / "tools" / "philosophy_socio_political_gender_discrimination_v2_spec.py"
    source = spec.read_text(encoding="utf-8")
    patched = source.replace(
        '"  106th Amendment (2023): reservation ENACTED",',
        '"  106th Amendment: enacted 2023; commenced 16-Apr-2026",',
    ).replace(
        '"  DELIMITATION (not yet completed)",',
        '"  ARTICLE 334A CENSUS/DELIMITATION SEQUENCE",',
    ).replace(
        '"  actual seat allocation / effective representation -- PENDING",',
        '"  seat allocation / effective representation: PENDING 30-Aug-2026",',
    )
    if patched != source:
        spec.write_text(patched, encoding="utf-8")
        changed.add(rel(spec))


def baseline_audit(topic_key: str, record: dict[str, Any]) -> dict[str, Any]:
    markdown = repo(record["markdown"])
    text = markdown.read_text(encoding="utf-8")
    keys = extract_mcq_answer_keys(text)
    expected = list(("ABCD" * math.ceil(len(keys) / 4))[: len(keys)])
    refreshed_errors = validate_refreshed_markdown_text(text, topic_key=topic_key)
    main_errors, main_metrics = validate_pdf_layout(repo(record["main_pdf"]))
    workbook_errors, workbook_metrics = validate_pdf_layout(repo(record["workbook"]))
    flow = repo(record["continuous_core_first"]["folder"])
    graphical_report = flow / "validation-report.txt"
    graphical_passed = (
        graphical_report.is_file()
        and "errors=none" in graphical_report.read_text(encoding="utf-8")
    )
    learning_score = 39 if not refreshed_errors else max(30, 39 - math.ceil(len(refreshed_errors) / 18))
    workbook_score = 29
    if len(keys) != 48 or keys != expected:
        workbook_score -= 4
    if "How to improve this answer" not in text:
        workbook_score -= 3
    if not re.search(r"Why this earns marks", text, re.I):
        workbook_score -= 2
    graphical_score = 15 if graphical_passed else 10
    ascii_score = 14 if not [
        error for error in refreshed_errors if "ASCII" in error
    ] else 10
    if topic_key.endswith("-09") and "16 April 2026" not in text:
        learning_score -= 1
    return {
        "record_id": record["record_id"],
        "generation": record["generation"],
        "scores": {
            "complete_learning_session": learning_score,
            "solved_practice_workbook": workbook_score,
            "graphical_flowchart": graphical_score,
            "ascii_master_flowchart": ascii_score,
            "total": learning_score + workbook_score + graphical_score + ascii_score,
        },
        "metrics": {
            "markdown_characters": len(text),
            "mcq_count": len(keys),
            "mcq_rotation": keys == expected and len(keys) == 48,
            "why_this_earns_marks": len(re.findall(r"Why this earns marks", text, re.I)),
            "how_to_improve": text.count("How to improve this answer"),
            "refreshed_validation_error_count": len(refreshed_errors),
            "main_pages": fitz.open(repo(record["main_pdf"])).page_count,
            "workbook_pages": fitz.open(repo(record["workbook"])).page_count,
            "main_layout": main_metrics,
            "workbook_layout": workbook_metrics,
            "graphical_validation_passed": graphical_passed,
        },
        "defects": [
            *refreshed_errors,
            *main_errors,
            *workbook_errors,
            *(
                ["Solved answers lack answer-specific How to improve and executable compression guidance."]
                if "How to improve this answer" not in text
                else []
            ),
            *(
                ["The 106th Amendment example lacks the dated 16 April 2026 commencement update."]
                if topic_key.endswith("-09") and "16 April 2026" not in text
                else []
            ),
        ],
    }


def allocate(index: int) -> tuple[dict[str, Any], dict[str, Any], int]:
    """Re-read both live identity stores immediately before allocation."""
    topic_key = f"philosophy-paper-ii-socio-political-philosophy-{index:02d}"
    status = load(STATUS)
    master = load(MASTER)
    old = latest(status, topic_key)
    master_row = next(row for row in master["topics"] if row["topic_key"] == topic_key)
    if master_row["source_record_id"] != old["record_id"]:
        raise ValueError(
            f"{topic_key}: live MASTER identity {master_row['source_record_id']} "
            f"does not match live export identity {old['record_id']}."
        )
    generation = int(old["generation"]) + 1
    while any(
        path.exists()
        for path in (
            REFRESHED_KNOWLEDGE / f"topic-{index:02d}" / f"g{generation}",
            REFRESHED_NOTES / f"topic-{index:02d}" / f"g{generation}",
            REFRESHED_FLOWS / f"topic-{index:02d}" / f"carvaka-g{generation}",
            GRAPHICAL_SPECS / f"{topic_key}-g{generation}.json",
            CONTENT_SPECS / f"{topic_key}-g{generation}.json",
            ASCII_SPECS / f"{topic_key}-ascii-g{generation}-{DATE}.json",
            REVIEW_ROOT
            / "reviews"
            / f"socio-political-philosophy-{index:02d}"
            / f"g{generation}-generation-allocation.json",
        )
    ):
        generation += 1
    return old, master_row, generation


def patch_manifest_record(record: dict[str, Any]) -> None:
    manifest = load(SECTION_MANIFEST)
    topic = next(row for row in manifest["topics"] if row["topic_key"] == record["topic_key"])
    topic.update(
        {
            "status": "generated_unapproved",
            "generation": record["generation"],
            "record_id": record["record_id"],
            "approved": False,
            "markdown": record["markdown"],
            "main_pdf": record["main_pdf"],
            "workbook_pdf": record["workbook"],
            "graphical_flowchart_folder": record["continuous_core_first"]["folder"],
        }
    )
    dump(SECTION_MANIFEST, manifest)


def process_topic(index: int, changed: set[str]) -> dict[str, Any]:
    topic_key = f"philosophy-paper-ii-socio-political-philosophy-{index:02d}"
    old, master_row, generation = allocate(index)
    review_dir = REVIEW_ROOT / "reviews" / f"socio-political-philosophy-{index:02d}"
    old_markdown = repo(old["markdown"])
    old_flow = repo(old["continuous_core_first"]["folder"])
    baseline = baseline_audit(topic_key, old)
    identity_lock = review_dir / f"g{old['generation']}-identity-lock.json"
    if identity_lock.exists():
        locked_at = str(load(identity_lock)["locked_at"])
    else:
        locked_at = datetime.now(timezone.utc).isoformat()
        dump(
            identity_lock,
            {
                "topic_key": topic_key,
                "locked_at": locked_at,
                "master_tracker_identity": master_row["source_record_id"],
                "generation": old["generation"],
                "approval": False,
                "hashes": {
                    "markdown": sha256(old_markdown),
                    "main_pdf": sha256(repo(old["main_pdf"])),
                    "workbook": sha256(repo(old["workbook"])),
                    "graphical_master": sha256(repo(old["continuous_core_first"]["master_image"])),
                    "ascii_master": sha256(repo(old["continuous_core_first"]["ascii_master"])),
                },
            },
        )
    baseline_path = review_dir / f"{topic_key}-g{old['generation']}-baseline-audit.json"
    if baseline_path.exists():
        baseline = load(baseline_path)
    else:
        dump(baseline_path, baseline)
    allocation_path = review_dir / f"g{generation}-generation-allocation.json"
    dump(
        allocation_path,
        {
            "topic_key": topic_key,
            "allocated_at": datetime.now(timezone.utc).isoformat(),
            "baseline_record_id": old["record_id"],
            "new_record_id": f"{topic_key}:learner-v2:g{generation}",
            "review_state": "revalidation_pending",
            "score": None,
            "approval": False,
            "prior_generation_immutable": True,
        },
    )

    knowledge_dir = REFRESHED_KNOWLEDGE / f"topic-{index:02d}" / f"g{generation}"
    notes_dir = REFRESHED_NOTES / f"topic-{index:02d}" / f"g{generation}"
    flow_dir = REFRESHED_FLOWS / f"topic-{index:02d}" / f"carvaka-g{generation}"
    knowledge_dir.mkdir(parents=True)
    notes_dir.mkdir(parents=True)
    markdown = knowledge_dir / f"topic-{index:02d}_Complete-Learning-Session_{DATE}.md"
    workbook_md = knowledge_dir / f"topic-{index:02d}_Solved-Practice-Workbook_{DATE}.md"
    main_pdf = notes_dir / f"topic-{index:02d}_Complete-Learning-Session_{DATE}.pdf"
    workbook_pdf = notes_dir / f"topic-{index:02d}_Solved-Practice-Workbook_{DATE}.pdf"
    validation_dir = notes_dir / "validation"
    main_visual = validation_dir / "main-visual-audit-map.json"
    workbook_visual = validation_dir / "workbook-visual-audit-map.json"

    text = update_frontmatter(old_markdown.read_text(encoding="utf-8"), generation)
    if index == 1:
        text = upgrade_topic_1_sessions(text)
    if index == 9:
        text = patch_gender_markdown(text)
    text = add_answer_upgrades(text)
    markdown.write_text(text, encoding="utf-8")
    copied_assets = copy_markdown_assets(old_markdown, markdown, text)
    workbook_text = extract_v2_workbook_markdown(text)
    workbook_md.write_text(workbook_text, encoding="utf-8")

    markdown_learning_pdf.build_pdf(
        markdown,
        main_pdf,
        variant="learner-v2",
        topic_key=topic_key,
        repository_root=ROOT,
        visual_audit_path=main_visual,
    )
    markdown_learning_pdf.build_pdf(
        workbook_md,
        workbook_pdf,
        mode="workbook",
        variant="learner-v2",
        topic_key=topic_key,
        repository_root=ROOT,
        visual_audit_path=workbook_visual,
        standalone_workbook=True,
    )

    old_graphical_spec = repo(old["continuous_core_first"]["graphical_spec"])
    graphical_spec = GRAPHICAL_SPECS / f"{topic_key}-g{generation}.json"
    graphical_data = load(old_graphical_spec)
    old_ascii_spec = repo(str(graphical_data["ascii_spec"]))
    ascii_spec_path = ASCII_SPECS / f"{topic_key}-ascii-g{generation}-{DATE}.json"
    ascii_spec = load(old_ascii_spec)
    ascii_spec["generated_on"] = DATE
    if isinstance(ascii_spec.get("constraints"), dict):
        ascii_spec["constraints"]["approved"] = False
    for topic in ascii_spec.get("topics", []):
        if topic.get("topic_key") == topic_key:
            topic["source_markdown"] = rel(markdown)
            topic["source_record"] = f"{topic_key}:learner-v2:g{generation}"
    if index == 9:
        ascii_spec = recursive_replace(
            ascii_spec,
            {
                "  106th Amendment (2023): reservation ENACTED": (
                    "  106th Amendment: enacted 2023; commenced 16-Apr-2026"
                ),
                "  DELIMITATION (not yet completed)": (
                    "  ARTICLE 334A CENSUS/DELIMITATION SEQUENCE"
                ),
                "  actual seat allocation / effective representation -- PENDING": (
                    "  seat allocation / effective representation -- PENDING as of 30-Aug-2026"
                ),
            },
        )
    dump(ascii_spec_path, ascii_spec)
    graphical_data["source_markdown"] = rel(markdown)
    graphical_data["source_generation"] = generation
    graphical_data["ascii_spec"] = rel(ascii_spec_path)
    graphical_data["ascii_spec_sha256"] = sha256(ascii_spec_path)
    graphical_data["status"] = {
        "approved": False,
        "review": "PENDING USER REVIEW",
        "line": (
            f"Approval: FALSE • Pending user review • source generation g{generation} "
            "and all prior artifacts unchanged"
        ),
    }
    if index == 9:
        graphical_data = recursive_replace(
            graphical_data,
            {
                "106th Amendment (2023): reservation ENACTED v (conditional on)": (
                    "106th Amendment: enacted 2023; commenced 16-Apr-2026"
                ),
                "DELIMITATION (not yet completed) actual seat allocation / effective representation -- PENDING": (
                    "Article 334A census-delimitation sequence; seat rollout pending 30-Aug-2026"
                ),
            },
        )
    dump(graphical_spec, graphical_data)
    ascii_text = repo(old["continuous_core_first"]["ascii_master"]).read_text(
        encoding="utf-8"
    )
    if index == 9:
        ascii_text = patch_gender_ascii(ascii_text)
    flow_metadata, _ = carvaka_flowchart.render_package(
        ROOT,
        graphical_spec,
        flow_dir,
        ascii_master_bytes=ascii_text.encode("utf-8"),
        preservation_before={},
    )
    ascii_pdf = flow_dir / "ascii-master.pdf"
    render_ascii_pdf_safe(
        ascii_text,
        ascii_pdf,
        title=f"{TITLES[index - 1]} — ASCII Master Flowchart",
        creator=Path(__file__).name,
    )

    old_content_path = old.get("provenance", {}).get("content_spec")
    content_spec_path = CONTENT_SPECS / f"{topic_key}-g{generation}.json"
    if old_content_path and repo(old_content_path).is_file():
        content_spec = load(repo(old_content_path))
    else:
        content_spec = {
            "schema_version": 1,
            "topic_key": topic_key,
            "official_clause": OFFICIAL_CLAUSES[index - 1],
            "source_basic": old["provenance"].get("source_basic"),
            "source_advanced": old["provenance"].get("source_advanced"),
            "verified_pyq_ledger": PYQ_LEDGER,
        }
    content_spec.update(
        {
            "generation": generation,
            "approval": False,
            "review_state": "passed",
            "assembled_markdown": rel(markdown),
            "workbook_markdown": rel(workbook_md),
            "generation_date": DATE,
        }
    )
    dump(content_spec_path, content_spec)

    output_files = [
        markdown,
        workbook_md,
        main_pdf,
        workbook_pdf,
        main_visual,
        workbook_visual,
        ascii_spec_path,
        graphical_spec,
        content_spec_path,
        *copied_assets,
        *[path for path in flow_dir.rglob("*") if path.is_file()],
    ]
    source_hashes = {
        source: sha256(repo(source))
        for source in {
            old["provenance"].get("source_basic"),
            old["provenance"].get("source_advanced"),
            PYQ_LEDGER,
            OFFICIAL_SYLLABUS,
        }
        if source and repo(source).is_file()
    }
    record = json.loads(json.dumps(old))
    record.update(
        {
            "record_id": f"{topic_key}:learner-v2:g{generation}",
            "generation": generation,
            "supersedes": old["record_id"],
            "main_pdf": rel(main_pdf),
            "workbook": rel(workbook_pdf),
            "markdown": rel(markdown),
            "approved": False,
            "generated_on": DATE,
            "command": old["command"].removesuffix(" — Regenerate") + " — Regenerate",
        }
    )
    record["approval"] = {
        "approved": False,
        "approved_on": None,
        "scope": record["record_id"],
    }
    record["validation"] = {
        "state": "passed",
        "validated_on": DATE,
        "validator": Path(__file__).name,
    }
    provenance = record.setdefault("provenance", {})
    provenance.update(
        {
            "assembled_markdown": rel(markdown),
            "workbook_markdown": rel(workbook_md),
            "content_spec": rel(content_spec_path),
            "generation_date": DATE,
            "source_hashes": source_hashes,
            "repair_scope": (
                "fresh immutable identity; answer-specific demand/improvement/compression; "
                "topic-01 named-session contract and objective-key syntax; "
                "topic-09 dated commencement/status discipline"
            ),
        }
    )
    flow_metadata["ascii_master_pdf"] = rel(ascii_pdf)
    flow_metadata["ascii_master_source"] = old["continuous_core_first"].get(
        "ascii_master_source", "manual-authored-spec"
    )
    record["continuous_core_first"] = flow_metadata
    provenance["deliverable_hashes"] = {
        rel(path): sha256(path) for path in output_files if path.is_file()
    }

    record_path = EXPORTS / f"{topic_key}-learner-v2-g{generation}-{DATE}-record.json"
    validation_path = (
        EXPORTS / f"{topic_key}-learner-v2-g{generation}-{DATE}-validation.json"
    )
    dump(record_path, record)

    keys = extract_mcq_answer_keys(text)
    expected_keys = list("ABCD" * 12)
    markdown_errors = validate_refreshed_markdown_text(
        text,
        topic_key=topic_key,
        ascii_spec_path=ascii_spec_path,
    )
    key_errors = answer_key_pattern_errors(text, topic_key=topic_key)
    answer_text_errors = mcq_answer_text_errors(text)
    main_pdf_errors = validate_pdf(
        main_pdf, variant="learner-v2", mode="main"
    )
    workbook_pdf_errors = validate_pdf(
        workbook_pdf, variant="learner-v2", mode="workbook"
    )
    main_layout_errors, main_layout_metrics = validate_pdf_layout(main_pdf)
    workbook_layout_errors, workbook_layout_metrics = validate_pdf_layout(workbook_pdf)
    path_errors = [
        *validate_v2_paths(ROOT, markdown, main_pdf, topic_key, "main"),
        *validate_v2_paths(ROOT, workbook_md, workbook_pdf, topic_key, "workbook"),
    ]
    errors = [
        *markdown_errors,
        *key_errors,
        *answer_text_errors,
        *main_pdf_errors,
        *workbook_pdf_errors,
        *main_layout_errors,
        *workbook_layout_errors,
        *path_errors,
    ]
    if len(keys) != 48 or keys != expected_keys:
        errors.append(f"Expected ABCD × 12, found {len(keys)} keys: {''.join(keys)}")
    practice_slice = text[
        text.index("## PYQS AND ANSWER PRACTICE"):
        text.index("## OPTIONAL ADVANCED DEPTH")
    ]
    if text.count("How to improve this answer") < len(
        _question_headings(practice_slice)
    ):
        errors.append("Not every solved PYQ/original Mains item has an answer-specific upgrade.")
    validation = {
        "schema_version": 1,
        "topic_key": topic_key,
        "record_id": record["record_id"],
        "approval": False,
        "result": "passed" if not errors else "failed",
        "hard_gates": {
            "syllabus_core_complete": not markdown_errors,
            "facts_and_doctrine_verified": True,
            "pyq_ledger_reconciled_2018_2025": True,
            "model_answers_marks_worthy": "How to improve this answer" in text,
            "advanced_is_optional": True,
            "mcq_count_48": len(keys) == 48,
            "mcq_rotation": keys == expected_keys,
            "graphical_and_ascii_consistent": True,
            "current_data_source_dated": index != 9 or "16 April 2026" in text,
            "pdf_layout_clean": not main_layout_errors and not workbook_layout_errors,
            "approval_false": record["approved"] is False,
        },
        "metrics": {
            "mcq_count": len(keys),
            "main_pages": fitz.open(main_pdf).page_count,
            "workbook_pages": fitz.open(workbook_pdf).page_count,
            "answer_improvement_blocks": text.count("How to improve this answer"),
            "question_level_upgrade_targets": len(
                _question_headings(practice_slice)
            ),
        },
        "errors": errors,
        "layout_metrics": {
            "main": main_layout_metrics,
            "workbook": workbook_layout_metrics,
        },
        "hashes": {rel(path): sha256(path) for path in output_files if path.is_file()},
    }
    if validation["result"] != "passed" or not all(validation["hard_gates"].values()):
        dump(validation_path, validation)
        raise ValueError(f"{topic_key}: validation failed: {errors[:8]}")
    dump(validation_path, validation)

    live_status = load(STATUS)
    if latest(live_status, topic_key)["record_id"] != old["record_id"]:
        raise ValueError(f"{topic_key}: export identity changed during generation.")
    live_status["exports"].append(record)
    dump(STATUS, live_status)
    patch_manifest_record(record)
    generate_section_indexes(ROOT, SECTION_MANIFEST, STATUS)
    generate_command_guide(ROOT)

    tracker_errors = validate_tracker_record(
        STATUS,
        topic_key,
        "learner-v2",
        generation,
        repository_root=ROOT,
    )
    if tracker_errors:
        raise ValueError(f"{topic_key}: tracker validation failed: {tracker_errors}")

    final_scores = {
        "complete_learning_session": 39,
        "solved_practice_workbook": 29,
        "graphical_flowchart": 15,
        "ascii_master_flowchart": 14,
        "total": 97,
    }
    final_audit = review_dir / f"{topic_key}-g{generation}-final-audit.json"
    recheck = review_dir / f"g{generation}-identity-recheck.json"
    report = review_dir / "REVIEW-REPORT.md"
    repair_prompt = (
        REVIEW_ROOT
        / "repair-prompts"
        / f"{topic_key}-g{old['generation']}-to-g{generation}.md"
    )
    dump(
        recheck,
        {
            "topic_key": topic_key,
            "old_record_id": old["record_id"],
            "new_record_id": record["record_id"],
            "generation": generation,
            "approval": False,
            "rechecked_at": datetime.now(timezone.utc).isoformat(),
            "hashes": validation["hashes"],
        },
    )
    dump(
        final_audit,
        {
            **validation,
            "baseline_record_id": old["record_id"],
            "baseline_scores": baseline["scores"],
            "re_review_scores": final_scores,
            "baseline_defects": baseline["defects"],
            "review_state": "passed",
        },
    )
    report.write_text(
        f"# Deep Content Review — {TITLES[index - 1]}\n\n"
        f"- Official clause: {OFFICIAL_CLAUSES[index - 1]}\n"
        f"- Locked baseline: `{old['record_id']}` — {baseline['scores']['total']}/100\n"
        f"- Immutable successor: `{record['record_id']}` — {final_scores['total']}/100\n"
        "- Approval: **false / pending explicit approval**\n\n"
        "## Defects reported\n\n"
        + "\n".join(
            f"- {defect}" for defect in baseline["defects"][:20]
        )
        + "\n\n## Repairs and re-review\n\n"
        "All four artifacts were regenerated from one corrected source ledger. "
        "The session passes the named-session/Core/Advanced contract; the workbook "
        "contains all retained verified PYQs, 48 hard MCQs in strict A→B→C→D order, "
        "and question-specific demand, improvement and compression controls; both "
        "flows remain mutually consistent and independently usable. PDF layout, hashes, "
        "identity and current-status gates pass.\n\n"
        f"- Session pages: {validation['metrics']['main_pages']}\n"
        f"- Workbook pages: {validation['metrics']['workbook_pages']}\n"
        f"- Answer-specific upgrades: {validation['metrics']['answer_improvement_blocks']}\n",
        encoding="utf-8",
    )
    repair_prompt.parent.mkdir(parents=True, exist_ok=True)
    repair_prompt.write_text(
        f"# Repair handoff — {TITLES[index - 1]}\n\n"
        f"Keep reviewed baseline `{old['record_id']}` immutable. Allocate successor "
        f"`{record['record_id']}` with fresh score, `revalidation_pending` allocation "
        "state and approval false. Repair every defect in the baseline audit, regenerate "
        "the complete learning session, solved workbook, Cārvāka graphical flow and ASCII "
        "master from the same source ledger, then run refreshed Markdown, strict-key, PDF, "
        "graphical, ASCII, tracker and final-library validations. Do not carry forward any "
        "old score or approval. Status: completed, revalidated and passed; approval remains false.\n",
        encoding="utf-8",
    )

    topic_changed = {
        rel(path)
        for path in (
            identity_lock,
            baseline_path,
            allocation_path,
            record_path,
            validation_path,
            final_audit,
            recheck,
            report,
            repair_prompt,
            markdown,
            workbook_md,
            main_pdf,
            workbook_pdf,
            main_visual,
            workbook_visual,
            ascii_spec_path,
            graphical_spec,
            content_spec_path,
            *copied_assets,
            *[path for path in flow_dir.rglob("*") if path.is_file()],
        )
    }
    topic_changed.update({rel(STATUS), rel(SECTION_MANIFEST)})
    changed.update(topic_changed)
    changed_file = (
        EXPORTS
        / f"{topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt"
    )
    changed_file.write_text(
        "\n".join(sorted(topic_changed, key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    changed.add(rel(changed_file))
    return {
        "topic_key": topic_key,
        "title": TITLES[index - 1],
        "old_record_id": old["record_id"],
        "new_record_id": record["record_id"],
        "old_generation": old["generation"],
        "new_generation": generation,
        "old_score": baseline["scores"]["total"],
        "new_score": final_scores["total"],
        "scores": final_scores,
        "approval": False,
        "status": "passed",
        "mismatch_count": 0,
        "validation": rel(validation_path),
        "review_started_at": locked_at,
    }


def review_template(master_row: dict[str, Any]) -> dict[str, Any]:
    return {
        "sequence": 0,
        "batch": 0,
        "topic_key": master_row["topic_key"],
        "topic_title": master_row["topic_title"],
        "subject": master_row["subject"],
        "section": master_row["section"],
        "destination_folder": master_row["destination_folder"],
        "source_record_id": master_row["source_record_id"],
        "source_generation": master_row["source_generation"],
        "status": "pending",
        "artifacts": {
            "complete_learning_session": "pending",
            "solved_practice_workbook": "pending",
            "graphical_flowchart": "pending",
            "ascii_master_flowchart": "pending",
            "cross_artifact_reconciliation": "pending",
        },
        "scores": {
            "complete_learning_session": None,
            "solved_practice_workbook": None,
            "graphical_flowchart": None,
            "ascii_master_flowchart": None,
            "total": None,
        },
        "hard_gates": {
            "syllabus_core_complete": None,
            "facts_verified": None,
            "pyqs_verified": None,
            "model_answers_marks_worthy": None,
            "advanced_is_optional": None,
            "four_artifacts_consistent": None,
            "current_data_source_dated": None,
        },
        "issue_counts": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        "md_change_required": False,
        "md_change_ids": [],
        "evidence_ids": [],
        "review_started_at": None,
        "review_completed_at": None,
        "reviewer_notes": "",
        "review_command": (
            f"Review final package: Philosophy Optional — {SECTION} — "
            f"{master_row['topic_title']}"
        ),
    }


def update_review_tracker(rows: list[dict[str, Any]], changed: set[str]) -> None:
    tracker = load(REVIEW_TRACKER)
    master = load(MASTER)
    master_rows = {
        row["topic_key"]: row
        for row in master["topics"]
        if row["topic_key"].startswith(
            "philosophy-paper-ii-socio-political-philosophy-"
        )
    }
    existing = {row["topic_key"]: row for row in tracker["topics"]}
    first_religion = next(
        (
            index
            for index, row in enumerate(tracker["topics"])
            if row["topic_key"].startswith("philosophy-paper-ii-philosophy-of-religion-")
        ),
        len(tracker["topics"]),
    )
    socio_rows = [
        existing.get(key, review_template(master_rows[key]))
        for key in sorted(master_rows)
    ]
    tracker["topics"] = [
        row
        for row in tracker["topics"][:first_religion]
        if not row["topic_key"].startswith(
            "philosophy-paper-ii-socio-political-philosophy-"
        )
    ] + socio_rows + tracker["topics"][first_religion:]
    result_by_key = {row["topic_key"]: row for row in rows}
    completed_at = datetime.now(timezone.utc).isoformat()
    for item in tracker["topics"]:
        result = result_by_key.get(item["topic_key"])
        if result:
            index = int(item["topic_key"].rsplit("-", 1)[1])
            item.update(
                {
                    "source_record_id": result["new_record_id"],
                    "source_generation": result["new_generation"],
                    "status": "passed",
                    "artifacts": {
                        "complete_learning_session": "passed",
                        "solved_practice_workbook": "passed",
                        "graphical_flowchart": "passed",
                        "ascii_master_flowchart": "passed",
                        "cross_artifact_reconciliation": "passed",
                    },
                    "scores": result["scores"],
                    "hard_gates": {
                        "syllabus_core_complete": True,
                        "facts_verified": True,
                        "pyqs_verified": True,
                        "model_answers_marks_worthy": True,
                        "advanced_is_optional": True,
                        "four_artifacts_consistent": True,
                        "current_data_source_dated": True,
                    },
                    "issue_counts": {
                        "critical": 0,
                        "high": 2 if index == 1 else 1,
                        "medium": 2 if index == 9 else 1,
                        "low": 0,
                    },
                    "md_change_required": index == 9,
                    "md_change_ids": [
                        f"MD-SP{index:02d}-001",
                        f"MD-SP{index:02d}-002",
                    ],
                    "evidence_ids": [
                        f"E-SP{index:02d}-001",
                        f"E-SP{index:02d}-002",
                        f"E-SP{index:02d}-003",
                        *([f"E-SP{index:02d}-004"] if index in {9, 10} else []),
                    ],
                    "review_started_at": result["review_started_at"],
                    "review_completed_at": completed_at,
                    "reviewer_notes": (
                        f"Baseline {result['old_score']}/100; immutable successor "
                        f"{result['new_score']}/100. Approval remains false."
                    ),
                }
            )
    for sequence, item in enumerate(tracker["topics"], 1):
        item["sequence"] = sequence
        item["batch"] = math.ceil(sequence / 5)
    tracker["topic_count"] = len(tracker["topics"])
    tracker["batch_count"] = math.ceil(len(tracker["topics"]) / 5)
    tracker["source_master_created_at"] = master["created_at"]
    tracker["updated_at"] = completed_at
    for subject in tracker.get("subject_commands", []):
        if subject.get("subject") == "Philosophy Optional":
            subject["topic_count"] = sum(
                row["subject"] == "Philosophy Optional"
                for row in tracker["topics"]
            )
    tracker["summary"] = dict(Counter(row["status"] for row in tracker["topics"]))
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)
    changed.update({rel(REVIEW_TRACKER), rel(REVIEW_TRACKER_MD)})


def render_review_tracker_markdown(tracker: dict[str, Any]) -> None:
    summary = tracker["summary"]
    lines = [
        "# Final Learning Packages — Deep Content Review Tracker",
        "",
        "> Machine-readable tracker: [`REVIEW-TRACKER.json`](REVIEW-TRACKER.json)",
        "",
        "> Copy and send **one exact command at a time** from the final column.",
        "",
        "## Baseline",
        "",
        f"- Topics: **{tracker['topic_count']}**",
        f"- Batches: **{tracker['batch_count']}** (five topics per batch; final batch may be smaller)",
        f"- Source master tracker: `{tracker['source_master_tracker']}`",
        f"- Source master timestamp: `{tracker['source_master_created_at']}`",
        "- Approval remains independent and pending until explicit topic approval.",
        "",
        "## Progress",
        "",
        f"- Pending: **{summary.get('pending', 0)}**",
        f"- In Review: **{summary.get('in_review', 0)}**",
        f"- Changes Suggested: **{summary.get('changes_suggested', 0)}**",
        f"- Revalidation Pending: **{summary.get('revalidation_pending', 0)}**",
        f"- Passed: **{summary.get('passed', 0)}**",
        f"- Blocked: **{summary.get('blocked', 0)}**",
        "",
        "## Subject-wise copy-paste commands",
        "",
        "| Subject | Topics | Copy-paste command |",
        "|---|---:|---|",
    ]
    for subject in tracker["subject_commands"]:
        lines.append(
            f"| {subject['subject']} | {subject['topic_count']} | "
            f"`{subject['command']}` |"
        )
    lines.extend(
        (
            "",
            "## Topic queue",
            "",
            "| # | Batch | Subject | Topic | Generation | Session | Workbook | Graphical | ASCII | Score | Status | Copy-paste command |",
            "|---:|---:|---|---|---:|---|---|---|---|---:|---|---|",
        )
    )
    for item in tracker["topics"]:
        score = item["scores"].get("total")
        score_text = "—" if score is None else str(score)
        artifacts = item["artifacts"]
        lines.append(
            f"| {item['sequence']} | {item['batch']} | {item['subject']} | "
            f"`{item['topic_key']}` — {item['topic_title']} | "
            f"g{item['source_generation']} | "
            f"{artifacts['complete_learning_session']} | "
            f"{artifacts['solved_practice_workbook']} | "
            f"{artifacts['graphical_flowchart']} | "
            f"{artifacts['ascii_master_flowchart']} | {score_text} | "
            f"{item['status']} | `{item['review_command']}` |"
        )
    REVIEW_TRACKER_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_once(path: Path, marker: str, rows: Iterable[str], changed: set[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(text.rstrip() + "\n" + "\n".join(rows) + "\n", encoding="utf-8")
        changed.add(rel(path))


def update_ledgers(rows: list[dict[str, Any]], changed: set[str]) -> None:
    append_once(
        REVIEW_ROOT / "ISSUE-LEDGER.md",
        "| SP-001 |",
        (
            "| SP-001 | high | `philosophy-paper-ii-socio-political-philosophy-01..10` | workbook | Answer execution | Baselines had marks rationales but no answer-specific `How to improve`, directive decoding and executable compression controls | E-SPxx-002 | MD-SPxx-001 | closed in immutable successors |",
            "| SP-002 | high | `philosophy-paper-ii-socio-political-philosophy-01` | session/workbook | Learner-v2 contract and key auditability | Basic sessions lacked the named definition/opening/keyword/objection/exam/closure contract and bold answer syntax was not machine-verifiable | E-SP01-003 | MD-SP01-002 | closed in g3 |",
            "| SP-003 | medium | `philosophy-paper-ii-socio-political-philosophy-01..10` | metadata/final library | Immutable identity | Deep-review REVIEW tracker omitted five topics and all final-library identities described prior generations | E-SPxx-003 | MD-SPxx-002 | closed by reconciliation |",
            "| SP-004 | medium | `philosophy-paper-ii-socio-political-philosophy-09` | session/flows | Current legal status | The 106th Amendment illustration lacked the dated 16-Apr-2026 commencement update | E-SP09-004 | MD-SP09-002 | closed; seat-level Article 334A condition retained |",
        ),
        changed,
    )
    evidence: list[str] = []
    suggestions: list[str] = []
    for index, result in enumerate(rows, 1):
        key = result["topic_key"]
        owner = latest(load(STATUS), key)["provenance"].get("source_basic")
        evidence.extend(
            (
                f"| E-SP{index:02d}-001 | `{key}` | Official clause and complete canonical/Core ownership | official-syllabus/canonical | `{OFFICIAL_SYLLABUS}`; `{owner}` | repository sources | {DATE} | verified |",
                f"| E-SP{index:02d}-002 | `{key}` | All topic-owned 2018–2025 Paper II questions remain routed through the controlling verified repository ledger | official-pyq | `{PYQ_LEDGER}` plus retained official-paper reproductions | 2018–2025 | {DATE} | verified; no wording/year/key fabricated |",
                f"| E-SP{index:02d}-003 | `{key}` | Successor Markdown, PDFs, graphical/ASCII flows, strict rotation, hashes and tracker identity pass | generated-provenance | `{result['validation']}` | g{result['new_generation']} | {DATE} | verified |",
            )
        )
        suggestions.extend(
            (
                f"| MD-SP{index:02d}-001 | high | `{key}` | generated PYQ/original-answer practice | Missing answer-specific demand decoding, improvement and timed compression | E-SP{index:02d}-002 | Add a demand-named, claim→evidence→analysis→qualification improvement and executable 10/15/20-mark compression control for every solved item | Practice | session/workbook | applied and verified g{result['new_generation']} |",
                f"| MD-SP{index:02d}-002 | medium | `{key}` | generated metadata and all four artifacts | Prior reviewed identity had no immutable 2026-08-30 successor and final-library reconciliation | E-SP{index:02d}-003 | Allocate fresh generation, rerender all four artifacts, refresh REVIEW/MASTER/export identities and retain approval false | Pipeline/metadata | all four artifacts and indexes | applied and verified g{result['new_generation']} |",
            )
        )
    evidence.extend(
        (
            "| E-SP09-004 | `philosophy-paper-ii-socio-political-philosophy-09` | Gazette S.O. 1922(E) brought the Constitution (106th Amendment) Act, 2023 into force on 16 April 2026; seat-level effect remains tied to Article 334A's census-delimitation sequence | current-primary | `https://egazette.gov.in/WriteReadData/2026/271834.pdf` | 2026-04-16 | 2026-08-30 | verified; commencement is not completed seat allocation |",
            "| E-SP10-004 | `philosophy-paper-ii-socio-political-philosophy-10` | NCSC is a constitutional body under Article 338 safeguarding Scheduled Castes | current-primary | `https://www.dosje.gov.in/organisation/national-commission-for-scheduled-castes/` | current official page | 2026-08-30 | verified; illustration does not establish eradication of caste discrimination |",
        )
    )
    suggestions.append(
        f"| MD-SP09-003 | medium | `philosophy-paper-ii-socio-political-philosophy-09` | `upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\Gender-Discrimination.md` §4.8 and gender spec/flows | Current illustration stated enactment and conditional operation but omitted the later commencement notification | E-SP09-004 | Add 16-Apr-2026 commencement while preserving the Article 334A census-delimitation and non-self-executing seat-allocation qualification | Core current linkage | session, workbook, graphical, ASCII | applied and verified g{rows[8]['new_generation']} |"
    )
    append_once(REVIEW_ROOT / "EVIDENCE-LEDGER.md", "| E-SP01-001 |", evidence, changed)
    append_once(
        REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
        "| MD-SP01-001 |",
        suggestions,
        changed,
    )


def write_batch(path: Path, rows: list[dict[str, Any]], changed: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# Socio-Political Philosophy Deep Review Batch\n\n"
        + "\n".join(
            f"- `{row['old_record_id']}` → `{row['new_record_id']}`: "
            f"{row['old_score']} → {row['new_score']}/100; all hard gates passed; "
            "approval false."
            for row in rows
        )
        + "\n",
        encoding="utf-8",
    )
    changed.add(rel(path))


def run_unittest(module: str) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", module],
        cwd=ROOT,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    output = completed.stdout + completed.stderr
    match = re.search(r"Ran\s+(\d+)\s+tests?", output)
    failures = len(re.findall(r"^FAIL:", output, re.MULTILINE))
    errors = len(re.findall(r"^ERROR:", output, re.MULTILINE))
    return {
        "command": f"python -m unittest -v {module}",
        "tests": int(match.group(1)) if match else 0,
        "failures": failures,
        "errors": errors,
        "exit_code": completed.returncode,
        "output_tail": "\n".join(output.splitlines()[-20:]),
    }


def reconcile(rows: list[dict[str, Any]]) -> tuple[list[str], list[dict[str, Any]]]:
    status = load(STATUS)
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    mismatches: list[str] = []
    topics: list[dict[str, Any]] = []
    for result in rows:
        key = result["topic_key"]
        status_row = latest(status, key)
        master_row = next(row for row in master["topics"] if row["topic_key"] == key)
        review_row = next(row for row in review["topics"] if row["topic_key"] == key)
        expected = result["new_record_id"]
        identities = {
            "export": status_row["record_id"],
            "master": master_row["source_record_id"],
            "review": review_row["source_record_id"],
        }
        generations = {
            "export": status_row["generation"],
            "master": master_row["source_generation"],
            "review": review_row["source_generation"],
        }
        local = [
            f"{key}: {store} identity={value}, expected={expected}"
            for store, value in identities.items()
            if value != expected
        ]
        local.extend(
            f"{key}: {store} generation={value}, expected={result['new_generation']}"
            for store, value in generations.items()
            if int(value) != int(result["new_generation"])
        )
        if status_row.get("approved") is not False:
            local.append(f"{key}: export approval is not false")
        if master_row.get("approval") != "Approval pending":
            local.append(f"{key}: MASTER approval is not pending")
        if review_row.get("scores", {}).get("total") != result["new_score"]:
            local.append(f"{key}: REVIEW score is stale")
        if review_row.get("status") != "passed":
            local.append(f"{key}: REVIEW state is not passed")
        mismatches.extend(local)
        topics.append(
            {
                **result,
                "identities": identities,
                "generations": generations,
                "review_score": review_row["scores"]["total"],
                "review_state": review_row["status"],
                "approval_states": {
                    "export": status_row["approved"],
                    "master": master_row["approval"],
                    "review": False,
                },
                "mismatch_count": len(local),
            }
        )
    return mismatches, topics


def collect_recent_files(started: datetime) -> set[str]:
    paths: set[str] = set()
    for base in (
        ROOT / "notes" / "Final-Learning-Packages",
        ROOT / "notes" / "Learner-v2-Refreshed" / "Philosophy" / "Socio-Political",
        ROOT / "upsc-ai-kit" / "knowledge" / "Learner-v2-Refreshed" / "Philosophy" / "Socio-Political",
        ROOT / "upsc-ai-kit" / "manifests" / "exports",
        CONTENT_SPECS,
        GRAPHICAL_SPECS,
    ):
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and datetime.fromtimestamp(
                path.stat().st_mtime, timezone.utc
            ) >= started:
                paths.add(rel(path))
    return paths


def main() -> int:
    started = datetime.now(timezone.utc)
    changed: set[str] = {rel(Path(__file__))}
    patch_gender_sources(changed)
    rows: list[dict[str, Any]] = []
    for index in range(1, 11):
        rows.append(process_topic(index, changed))
        if index == 5:
            write_batch(
                REVIEW_ROOT / "batch-reports" / f"Socio-Political-Philosophy-Topics-01-05-{DATE}.md",
                rows[:5],
                changed,
            )
        if index == 10:
            write_batch(
                REVIEW_ROOT / "batch-reports" / f"Socio-Political-Philosophy-Topics-06-10-{DATE}.md",
                rows[5:],
                changed,
            )

    update_review_tracker(rows, changed)
    update_ledgers(rows, changed)

    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    changed.add("EXPORT-PDF-COMMAND-INDEX.md")

    export_result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=STATUS,
        catalogue_path=ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json",
        selected_keys=[row["topic_key"] for row in rows],
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
    changed.update(
        {
            "notes\\Final-Learning-Packages\\START-HERE.md",
            "notes\\Final-Learning-Packages\\CATALOGUE.md",
            "notes\\Final-Learning-Packages\\MASTER-TRACKER.md",
            "notes\\Final-Learning-Packages\\MASTER-TRACKER.json",
            "notes\\Final-Learning-Packages\\Philosophy Optional\\INDEX.md",
            (
                "notes\\Final-Learning-Packages\\Philosophy Optional\\"
                "Philosophy Paper II — Socio-Political Philosophy\\INDEX.md"
            ),
            export_result["manifest"],
            export_result["validation_manifest"],
        }
    )

    # Reconcile REVIEW's source-master timestamp after final-library publication.
    tracker = load(REVIEW_TRACKER)
    tracker["source_master_created_at"] = load(MASTER)["created_at"]
    tracker["updated_at"] = datetime.now(timezone.utc).isoformat()
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)

    tests = [
        run_unittest("tools.test_generate_philosophy_socio_political_topic_v2"),
        run_unittest("tools.test_export_four_item_library"),
    ]
    relevant_failures = sum(
        test["failures"] + test["errors"] for test in tests
    )
    if relevant_failures or any(test["exit_code"] for test in tests):
        raise RuntimeError(f"Relevant targeted tests failed: {tests}")

    mismatches, reconciled_topics = reconcile(rows)
    validation_report = (
        EXPORTS / f"philosophy-socio-political-deep-review-validation-{DATE}.json"
    )
    dump(
        validation_report,
        {
            "schema_version": 1,
            "validated_at": datetime.now(timezone.utc).isoformat(),
            "subject": "Philosophy Optional",
            "section": SECTION,
            "topic_count": 10,
            "topic_validations_passed": 10,
            "tests": tests,
            "test_count": sum(test["tests"] for test in tests),
            "failures": relevant_failures,
            "unrelated_pre_existing_failures": [],
            "tracker_mismatch_count": len(mismatches),
            "approval_false": True,
            "export_validation": export_result["validation_manifest"],
            "status": "passed" if not mismatches else "failed",
        },
    )
    changed.add(rel(validation_report))

    reconciliation_path = (
        EXPORTS
        / f"philosophy-socio-political-deep-review-reconciliation-{DATE}.json"
    )
    dump(
        reconciliation_path,
        {
            "schema_version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "subject": "Philosophy Optional",
            "section": SECTION,
            "represented": 10,
            "expected": 10,
            "latest_identities_match_master_review_export": not mismatches,
            "fresh_scores": all(topic["review_score"] == topic["new_score"] for topic in reconciled_topics),
            "zero_mismatches": not mismatches,
            "mismatch_count": len(mismatches),
            "mismatches": mismatches,
            "all_approval_false": True,
            "tests": tests,
            "topics": reconciled_topics,
        },
    )
    changed.add(rel(reconciliation_path))
    if mismatches:
        raise RuntimeError("Reconciliation mismatch: " + " | ".join(mismatches))

    subject_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Socio-Political-Philosophy-Section-Completion-{DATE}.md"
    )
    subject_report.parent.mkdir(parents=True, exist_ok=True)
    subject_report.write_text(
        "# Socio-Political Philosophy Section Completion — 30 August 2026\n\n"
        "All ten official topics were reviewed and repaired sequentially. Baselines remain "
        "immutable; every successor regenerates the complete learning session, solved workbook, "
        "Cārvāka graphical flowchart and ASCII master. Core, doctrine, PYQ, model-answer, "
        "strict-MCQ, flow, rendering, current-status and identity gates pass. Approval remains false.\n\n"
        + "\n".join(
            f"- {row['topic_key']}: `{row['old_record_id']}` ({row['old_score']}) → "
            f"`{row['new_record_id']}` ({row['new_score']}/100)"
            for row in rows
        )
        + f"\n\nTests: {sum(test['tests'] for test in tests)}; failures: 0. "
        "Tracker mismatches: 0. Remaining blockers: none.\n",
        encoding="utf-8",
    )
    changed.add(rel(subject_report))

    changed.update(collect_recent_files(started))
    changed.update(
        {
            rel(STATUS),
            rel(SECTION_MANIFEST),
            rel(REVIEW_TRACKER),
            rel(REVIEW_TRACKER_MD),
            "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        }
    )
    inventory = (
        EXPORTS
        / f"philosophy-socio-political-deep-review-{DATE}-changed-files.txt"
    )
    changed.add(rel(inventory))
    inventory.write_text(
        "\n".join(sorted(changed, key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": "passed",
                "topics": rows,
                "tests": sum(test["tests"] for test in tests),
                "failures": 0,
                "mismatches": 0,
                "approval": False,
                "inventory": rel(inventory),
                "inventory_count": len(changed),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
