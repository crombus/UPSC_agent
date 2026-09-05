"""Generate the immutable 2026-09-03 Religion and Morality successor only."""

from __future__ import annotations

import copy
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import regenerate_philosophy_religion_deep_review as base


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-03"
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-08"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Religion-and-Morality.md"
)


def extract_section(text: str, heading: str, next_marker: str) -> str:
    match = re.search(
        rf"(?ms)^{re.escape(heading)}\s*$.*?(?=^{re.escape(next_marker)}\s*$)",
        text,
    )
    if not match:
        raise ValueError(f"Cannot extract canonical section {heading!r}.")
    return match.group(0).strip()


def demote(fragment: str, levels: int = 1) -> str:
    return re.sub(
        r"(?m)^(#{2,5})\s+",
        lambda match: "#" * min(len(match.group(1)) + levels, 6) + " ",
        fragment,
    )


def insert_before(text: str, marker: str, fragment: str) -> str:
    if marker not in text:
        raise ValueError(f"Missing learner marker {marker!r}.")
    return text.replace(marker, fragment.rstrip() + "\n\n" + marker, 1)


SESSION_CONTROLS: dict[int, dict[str, str]] = {
    1: {
        "plain": (
            "The religion-morality problem asks whether religion makes morality valid, "
            "helps us know it, motivates it or sanctions it, and whether morality can "
            "remain autonomous."
        ),
        "technical": (
            "Metaphysical grounding, moral knowledge, motivation, sanction and "
            "sociological influence are distinct dependence relations and require "
            "separate arguments."
        ),
    },
    3: {
        "how": (
            "Compare Kantian autonomy, natural law, secular ethics and moral realism "
            "through reason and human flourishing, then assess religion's motivational "
            "role without making it the source of validity."
        ),
    },
    4: {
        "how": (
            "Use mutual formation, religious motivation, exemplars and ethical fruits to "
            "show how moral critique reforms religion, while keeping the influence "
            "contingent rather than logically necessary."
        ),
    },
    5: {
        "how": (
            "Use the Euthyphro dilemma and modified divine command to separate moral "
            "obligation, motivation and sanction, then test whether good character or "
            "divine nature blocks arbitrariness."
        ),
    },
    6: {
        "plain": (
            "Foundational positions ground morality in divine command, rational autonomy, "
            "natural law, pragmatic fruits or duty within a religious-cosmic order."
        ),
        "technical": (
            "The positions distinguish divine constitution of obligation, rational "
            "self-legislation, participation in natural goods, pragmatic moral fruits "
            "and duty within a religious-cosmic order."
        ),
        "opening": (
            "The religion-morality debate is not exhausted by command versus autonomy; "
            "natural law, practical reason, moral fruits and duty offer intermediate structures."
        ),
        "how": (
            "Compare divine command, Kant, natural law, James and dharma through practical "
            "reason, moral validity, motivation and criticism rather than treating them "
            "as one binary dispute."
        ),
    },
    7: {
        "plain": (
            "Indian moral life is grounded differently in duty, karmic consequence, "
            "non-injury, compassion, ritual injunction or devotion rather than one shared moral code."
        ),
        "technical": (
            "Indian positions range from Mimamsa injunction and karmic causation to "
            "Buddhist compassion, Jain non-injury and theistic devotion, each joining "
            "normativity to a different liberation-framework."
        ),
        "opening": (
            "Indian traditions do not offer one religion-morality model: duty, karma, "
            "non-injury, compassion and devotion ground conduct through different authorities and goals."
        ),
        "how": (
            "Compare dharma, karma, non-injury, Buddhist compassion, Mimamsa duty and "
            "theistic devotion to show how Indian grounds of moral life differ in "
            "normativity and liberation."
        ),
    },
}


CLOSURE_CONTROLS: dict[int, dict[str, str]] = {
    1: {
        "mechanism": (
            "Separate metaphysical grounding, moral knowledge, motivation, sanction and "
            "sociological influence before assessing dependence."
        ),
        "consequence": (
            "Religion can succeed in one role without making morality dependent in every role."
        ),
        "trap": (
            "Do not infer conceptual dependence from historical influence or moral conduct "
            "from religious profession."
        ),
    },
    2: {
        "mechanism": (
            "Divine command constitutes obligation, while modified versions ground value "
            "in a necessarily loving nature and obligation in commands."
        ),
        "consequence": (
            "Euthyphro pressures arbitrariness or independent goodness; modified command "
            "blocks the first horn but retains the second pressure."
        ),
        "trap": (
            "Do not merge moral truth, knowledge, motivation and sanction into the bare fact of command."
        ),
    },
    3: {
        "mechanism": (
            "Kantian autonomy, moral realism, flourishing and contract or consequence "
            "theories ground morality without divine command."
        ),
        "consequence": (
            "Religion may add hope, formation or motivation without becoming the source "
            "of moral validity."
        ),
        "trap": (
            "Do not reduce autonomy to preference or secular ethics to absence of moral objectivity."
        ),
    },
    4: {
        "mechanism": (
            "Religious narratives, exemplars and communities shape conduct, while moral "
            "criticism reforms commands, texts and practices."
        ),
        "consequence": (
            "The relation is mutually formative and contingent, capable of supporting "
            "care or rationalising exclusion."
        ),
        "trap": (
            "Do not treat sociological correlation as proof that religion is inherently moral or immoral."
        ),
    },
    5: {
        "mechanism": (
            "Distinguish obligation's source from motivation and sanction, then test "
            "modified divine command through divine character and independent goodness."
        ),
        "consequence": (
            "God-reference may deepen motivation and accountability without being "
            "necessary for obligation."
        ),
        "trap": (
            "Do not claim modified divine command simply defeats Euthyphro or reduce moral "
            "motivation to fear of punishment."
        ),
    },
    6: {
        "mechanism": (
            "Compare command, autonomy, natural law, pragmatic fruits and duty on "
            "validity, knowledge, motivation and criticism."
        ),
        "consequence": (
            "Intermediate views preserve religious meaning while allowing rational moral access."
        ),
        "trap": (
            "Do not force every position into a command-versus-secular binary."
        ),
    },
    7: {
        "mechanism": (
            "Compare duty, karma, non-injury, compassion, ritual injunction and devotion "
            "by authority, motive and liberation-goal."
        ),
        "consequence": (
            "Indian traditions provide theistic, ritual, karmic and non-theistic moral "
            "grounds rather than one code."
        ),
        "trap": (
            "Do not identify dharma wholly with universal morality or infer guilt from suffering."
        ),
    },
}


def transform_ascii(text: str) -> str:
    text = text.replace(
        " VIOLENCE PATH: exclusive truth + sacred authorisation + dehumanised out-group\n"
        "              + political grievance -> moral disengagement",
        " VIOLENCE PATH: exclusive truth + claimed sacred authorisation\n"
        "              + denial of equal moral standing -> moral disengagement",
    )
    return text


def repair_session_contracts(text: str) -> str:
    session_re = re.compile(
        r"(?ms)^### SESSION (\d+) — ([^\n]+)\n(.*?)(?=^### SESSION \d+ — |\Z)"
    )

    def repair(match: re.Match[str]) -> str:
        number = int(match.group(1))
        title = match.group(2).strip()
        body = match.group(3)
        control = SESSION_CONTROLS.get(number, {})
        for field, label in (
            ("plain", "Plain-language definition"),
            ("technical", "Technical definition"),
        ):
            if field in control:
                body = re.sub(
                    rf"(?m)^\*\*{re.escape(label)}:\*\* .+$",
                    f"**{label}:** {control[field]}",
                    body,
                    count=1,
                )
        if "opening" in control:
            body = re.sub(
                r"(?ms)(^#### ANSWER-GRABBING OPENING.*?\n+\s*>\s*).+?$",
                lambda found: found.group(1) + control["opening"],
                body,
                count=1,
            )
        if "how" in control:
            body = re.sub(
                r"(?m)^\*\*How to use them:\*\* .+$",
                f"**How to use them:** {control['how']}",
                body,
                count=1,
            )
        keyword_match = re.search(
            r"(?ms)^#### MUST-WRITE KEYWORDS\s*$\n+(.*?)(?=^\*\*How to use them:\*\*)",
            body,
        )
        if not keyword_match:
            raise ValueError(f"Session {number} has no readable keyword block.")
        keywords = re.findall(
            r"(?m)^\s*[-*]\s+\*\*(.+?)\*\*\s*$",
            keyword_match.group(1),
        )
        if not 4 <= len(keywords) <= 8:
            raise ValueError(f"Session {number} has {len(keywords)} closure keywords.")
        opening_match = re.search(
            r"(?ms)^#### ANSWER-GRABBING OPENING.*?\n+\s*>\s*(.+?)\s*$",
            body,
        )
        if not opening_match:
            raise ValueError(f"Session {number} has no answer opening.")
        opening = opening_match.group(1).strip()
        roles = CLOSURE_CONTROLS[number]
        closure = (
            f"#### CLOSING RECALL FLOW — {title}\n"
            "```closure-flow\n"
            f"SUBTOPIC: {title}\n"
            f"STARTING CONCEPT: {title}\n"
            f"KEY TERMS / DEFINITIONS: {' · '.join(keywords)}\n"
            f"MECHANISM / ARGUMENT: {roles['mechanism']}\n"
            f"CONSEQUENCE / CONTRAST: {roles['consequence']}\n"
            f"UPSC TRAP / ANSWER-USE: {roles['trap']}\n"
            f"ANSWER-GRABBING FORMULATION: {opening}\n"
            "```"
        )
        body, count = re.subn(
            r"(?ms)^#### CLOSING RECALL FLOW[^\n]*\n```closure-flow\n.*?```",
            closure,
            body,
            count=1,
        )
        if count != 1:
            raise ValueError(f"Session {number} closure could not be replaced.")
        return f"### SESSION {number} — {title}\n{body}"

    return session_re.sub(repair, text)


def transform_markdown(text: str, generation: int) -> str:
    owner = OWNER.read_text(encoding="utf-8")
    firewall = demote(
        extract_section(
            owner,
            "## Exact printed ownership and cross-topic firewall",
            "---",
        )
    )
    dependence = demote(
        extract_section(
            owner,
            "## 0A. FOUR DIFFERENT DEPENDENCE CLAIMS ⚠️",
            "---",
        )
    )
    indian = demote(
        extract_section(
            owner,
            "### 3.1 Moral critique, plural moralities and Indian grounds",
            "---",
        )
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + firewall + "\n\n" + dependence,
            1,
        )
    if "#### 3.1 Moral critique, plural moralities and Indian grounds" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — INDIAN AND WESTERN GROUNDS OF MORAL LIFE",
            indian,
        )
    source_control = (
        "### Local source and factual control\n\n"
        "- Local John Hick, *Philosophy of Religion*, especially PDF pp. 23–24 "
        "and 39–40, controls ethics' conceptual independence and moral-argument links.\n"
        "- The local *Oxford Handbook of Philosophy of Religion*, print pp. 344–365 "
        "(approximately PDF pp. 356–377), controls divine command, natural law, "
        "motivation and autonomy.\n"
        "- Chatterjee–Datta, especially PDF pp. 71–73 and 141–143, controls "
        "Mimamsa duty and Jain non-injury; no living community is characterised.\n"
        "- Historical or sociological influence is not treated as proof of conceptual dependence."
    )
    if "### Local source and factual control" not in text:
        text = insert_before(
            text,
            "### Source-complete coverage ledger and answer-worthiness labels",
            source_control,
        )
    text = re.sub(
        r"(?m)^✅ \*\*Fact:\*\* Reporting on the 2026 Sabarimala.*$\n"
        r"^⚠️ \*\*Inference:\*\* The controversy.*$\n"
        r"^\*\*Live source checked:\*\*.*$\n?",
        "⚠️ **Current-evidence policy:** no live dispute or legal case is used to "
        "establish philosophical dependence; the analysis remains doctrine- and PYQ-led.\n",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^\*\*Technical definition:\*\* ✅ Fact: Reporting on the 2026 Sabarimala.*$",
        "**Technical definition:** Metaphysical grounding, moral knowledge, motivation, "
        "sanction and sociological influence are distinct dependence relations and "
        "require separate arguments.",
        text,
        count=1,
    )
    text = text.replace(
        "*Religion without morality is impossible* — every religion prescribes an ethic; "
        "a religion sanctioning cruelty is a contradiction. **Morality is internal to religion.**",
        "*Normatively adequate religion without morality is difficult to defend, but a "
        "descriptively identifiable religious institution can transmit immoral commands "
        "or practices; moral criticism does not make it sociologically nonexistent.*",
    )
    text = repair_session_contracts(text)
    text = transform_ascii(text)
    required = (
        "Exact printed ownership and cross-topic firewall",
        "FOUR DIFFERENT DEPENDENCE CLAIMS",
        "Moral critique, plural moralities and Indian grounds",
        "Local source and factual control",
        "STARTING CONCEPT",
        "denial of equal moral standing",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Religion and Morality transform missing: {missing}")
    return text


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    answer_lines = {
        "00": (
            "Separate grounding, moral knowledge, motivation, sanction and sociological "
            "influence; success in one role proves no dependence in all."
        ),
        "01": (
            "Divine command constitutes obligation, while knowledge of commands and "
            "motivation by love or judgement are separate epistemic and practical claims."
        ),
        "02": (
            "Modified command blocks arbitrary will by grounding commands in loving "
            "divine character, but goodness remains independently intelligible."
        ),
        "03": (
            "Kant grounds duty in rational autonomy; natural law connects objective goods "
            "to divine order without reducing morality to command."
        ),
        "04": (
            "Indian grounds include injunction, karma, non-injury, compassion and "
            "devotion; they do not form one moral code or one divine-command model."
        ),
        "05": (
            "Religion can deepen motivation and formation without making fear, reward or "
            "profession sufficient for moral worth."
        ),
        "06": (
            "Religious commands and anti-religious genealogies alike remain answerable to "
            "dignity, equal moral standing and independent moral criticism."
        ),
        "07": (
            "Morality can be autonomous while religion remains a contingent source of "
            "motivation, community, hope and reciprocal moral reform."
        ),
    }
    for stage in spec.get("stages", []):
        stage_id = str(stage.get("id"))
        if stage_id in answer_lines:
            stage["answer_line"] = answer_lines[stage_id]
    return spec


def write_generation_ascii_spec(
    generation: int,
    markdown_path: Path,
    transformed_markdown: str,
) -> Path:
    source = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / "philosophy-2026-08-23.json"
    )
    target = source.with_name(f"{TOPIC_KEY}-ascii-g{generation}-{DATE}.json")
    if target.exists():
        raise RuntimeError(f"Refusing to overwrite immutable ASCII spec: {target}")
    shared = json.loads(source.read_text(encoding="utf-8"))
    topic = copy.deepcopy(
        next(item for item in shared["topics"] if item["topic_key"] == TOPIC_KEY)
    )
    ascii_fragment = transformed_markdown.split(
        "### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM",
        1,
    )[1]
    blocks = re.findall(
        r"(?ms)^#### ASCII MASTER FLOW — PANEL \d+/\d+: (.+?)\n+"
        r"```ascii-master\n(.*?)\n```",
        ascii_fragment,
    )
    if len(blocks) != len(topic["panels"]):
        raise ValueError(
            f"Expected {len(topic['panels'])} authored ASCII panels, found {len(blocks)}."
        )
    for panel, (title, body) in zip(topic["panels"], blocks):
        panel["panel_title"] = title.strip()
        panel["lines"] = body.splitlines()
    topic["source_markdown"] = base.rel(markdown_path)
    topic["source_record"] = f"{TOPIC_KEY}:learner-v2:g{generation}"
    spec = {
        "schema_version": 1,
        "benchmark": "Religion-and-Morality reviewed eight-panel ASCII master",
        "generated_on": DATE,
        "scope": f"{TOPIC_KEY} immutable generation g{generation}",
        "constraints": copy.deepcopy(shared.get("constraints", {})),
        "topics": [topic],
    }
    base.dump(target, spec)
    return target


def validate_refreshed(record: dict[str, Any], ascii_spec: Path) -> str:
    command = [
        sys.executable,
        str(ROOT / "tools" / "validate_v2_export.py"),
        str(base.repo(record["markdown"])),
        "--repository-root",
        str(ROOT),
        "--topic-key",
        TOPIC_KEY,
        "--ascii-spec",
        str(ascii_spec),
        "--main-pdf",
        str(base.repo(record["main_pdf"])),
        "--workbook",
        str(base.repo(record["workbook"])),
        "--tracker",
        str(base.TRACKER),
        "--variant",
        "learner-v2",
        "--generation",
        str(record["generation"]),
        "--refreshed-contract",
    ]
    environment = dict(os.environ)
    environment["PYTHONIOENCODING"] = "utf-8"
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode:
        raise RuntimeError(
            "Authoritative refreshed-contract validation failed:\n"
            + completed.stdout
            + completed.stderr
        )
    output = completed.stdout.strip()
    print(output)
    return output


def main() -> int:
    latest = base.latest(TOPIC_KEY)
    if int(latest["generation"]) != 12:
        raise ValueError(
            f"Expected reviewed predecessor g12, found {latest['record_id']}."
        )
    base.DATE = DATE
    generation = int(latest["generation"]) + 1
    next_markdown = (
        base.repo(latest["markdown"]).parents[1]
        / f"g{generation}"
        / f"topic-08_Complete-Learning-Session_{DATE}.md"
    )
    preview_text = transform_markdown(
        base.repo(latest["markdown"]).read_text(encoding="utf-8"),
        generation,
    )
    ascii_spec = write_generation_ascii_spec(
        generation,
        next_markdown,
        preview_text,
    )
    canonical_asset_folder = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "learning-session-v2"
        / TOPIC_KEY
        / "assets"
    )
    changed = {
        base.rel(Path(__file__)),
        base.rel(OWNER),
        base.rel(ROOT / "tools" / "philosophy_indian_religion_reviewed_content.py"),
        base.rel(ascii_spec),
    }
    result = base.process_topic(
        8,
        changed,
        text_transform=transform_markdown,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Religion and Morality: "
            "ownership, dependence roles, command/autonomy, plural moral grounds, "
            "session contract and immutable dependent artifacts"
        ),
        baseline_score=97,
        repaired_score=100,
        issues_closed=[
            "exact ownership and cross-topic boundaries made explicit",
            "grounding, knowledge, motivation, sanction and influence separated",
            "divine command and modified-command claims made role-specific",
            "immoral-religion and plural religious morality controls repaired",
            "Indian school grounds and non-dependence caution completed",
            "all seven refreshed session contracts and asset metadata repaired",
            "ASCII and graphical artifacts regenerated from one repaired source",
        ],
        ascii_spec_path=ascii_spec,
        canonical_asset_folder=canonical_asset_folder,
        ascii_from_markdown=True,
    )
    record = base.latest(TOPIC_KEY)
    validator_output = validate_refreshed(record, ascii_spec)
    authoritative_validation = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "exports"
        / f"{TOPIC_KEY}-learner-v2-g{generation}-{DATE}-"
        "authoritative-refreshed-validation.json"
    )
    base.dump(
        authoritative_validation,
        {
            "schema_version": 1,
            "topic_key": TOPIC_KEY,
            "record_id": record["record_id"],
            "generation": generation,
            "validated_on": DATE,
            "validator": "tools\\validate_v2_export.py --refreshed-contract",
            "manual_ascii_spec": base.rel(ascii_spec),
            "asset_folder": record["asset_folder"],
            "result": "passed",
            "stdout": validator_output,
        },
    )
    changed.add(base.rel(authoritative_validation))

    generation = int(result["new_record_id"].rsplit("g", 1)[1])
    inventory = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "exports"
        / f"{TOPIC_KEY}-learner-v2-g{generation}-{DATE}-changed-files.txt"
    )
    items = set(inventory.read_text(encoding="utf-8").splitlines())
    items.update(changed)
    items.update(
        {
            "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
            "notes\\Philosophy\\learning-session-v2\\paper-ii-philosophy-of-religion"
            "\\indexes\\TOPIC-COVERAGE-INDEX.md",
            "notes\\Philosophy\\learning-session-v2\\paper-ii-philosophy-of-religion"
            "\\indexes\\NOTES-PDF-INDEX.md",
            "notes\\Philosophy\\learning-session-v2\\paper-ii-philosophy-of-religion"
            "\\indexes\\WORKBOOK-PDF-INDEX.md",
        }
    )
    inventory.write_text(
        "\n".join(sorted(filter(None, items), key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({**result, "inventory": base.rel(inventory)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
