"""Generate the immutable 2026-09-03 Religious Pluralism successor only."""

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
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-09"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Religious-Pluralism.md"
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
            "Religious pluralism begins from factual, doctrinal and salvation-related "
            "diversity and asks what follows for truth, justification and coexistence."
        ),
        "technical": (
            "The problem separates alethic truth, soteriological efficacy, epistemic "
            "access and civic status rather than inferring one axis from another."
        ),
        "how": (
            "Use religious diversity, truth-claims and salvation-claims to classify "
            "conflict, then test whether pluralism preserves absolute truth without relativism."
        ),
    },
    2: {
        "how": (
            "Compare exclusivism, inclusivism and pluralism on salvation, fulfilment and "
            "independent validity, keeping inclusivism's one normative centre distinct."
        ),
    },
    3: {
        "how": (
            "Use Vedanta, Vivekananda, one reality and many paths to assess universal "
            "religion and acceptance, while preserving doctrinal difference and the "
            "inclusivist risk."
        ),
    },
    4: {
        "how": (
            "Relate absolute truth to perspectival access, then test relativism, "
            "contradiction, deep disagreement and the pluralist meta-level claim rather "
            "than merely celebrating diversity."
        ),
    },
    5: {
        "plain": (
            "Tolerance permits disagreement, dialogue exchanges reasons and equal "
            "religious freedom protects persons without requiring agreement about truth or salvation."
        ),
        "technical": (
            "Civic coexistence ranges from permission and modus vivendi to reciprocal "
            "respect and dialogue, while internal-minority and harm constraints limit group freedom."
        ),
        "opening": (
            "Social tolerance and religious freedom regulate coexistence under "
            "disagreement; they neither prove pluralism nor require treating rival "
            "doctrines as equally true."
        ),
        "how": (
            "Compare tolerance, acceptance and dialogue through religious freedom and "
            "multiculturalism, then test coexistence by its treatment of dissenters and "
            "internal minorities."
        ),
    },
    6: {
        "opening": (
            "Hick, Vivekananda and Jain many-sidedness address religious diversity "
            "through a transcategorial Real, convergent paths and standpoint-conditioned "
            "claims, but none dissolves every contradiction."
        ),
        "how": (
            "Compare John Hick and the transcategorial Real with Vivekananda's many paths "
            "and Jain many-sidedness/conditional assertion, noting their different "
            "metaphysical strategies and costs."
        ),
    },
    7: {
        "how": (
            "Use Indian-Western resources to compare Vedantic unity, Jain many-sidedness, "
            "Asokan concord, principled distance and dialogue, then state how "
            "non-relativism is preserved."
        ),
    },
}


CLOSURE_CONTROLS: dict[int, dict[str, str]] = {
    1: {
        "mechanism": (
            "Classify conflict across truth, salvation, epistemic access and civic status "
            "before choosing a pluralist response."
        ),
        "consequence": (
            "Diversity can support humility or disagreement without by itself proving "
            "relativism or one higher-order unity."
        ),
        "trap": (
            "Do not infer equal truth from tolerance or political conflict from doctrinal contradiction alone."
        ),
    },
    2: {
        "mechanism": (
            "Exclusivism reserves a decisive norm, inclusivism fulfils others through one "
            "centre and pluralism grants several authentic paths or ends."
        ),
        "consequence": (
            "The positions must be compared separately on truth, salvation and justification."
        ),
        "trap": (
            "Do not equate exclusivism with intolerance or pluralism with every claim being equally true."
        ),
    },
    3: {
        "mechanism": (
            "Vedantic unity and Vivekananda's many-paths model connect diverse disciplines "
            "to one ultimate while preserving different temperaments."
        ),
        "consequence": (
            "Convergence may support acceptance but risks assimilating other traditions "
            "into a neo-Vedantic meta-framework."
        ),
        "trap": (
            "Do not use Rigveda 1.164.46 as an unargued charter of all interreligious pluralism."
        ),
    },
    4: {
        "mechanism": (
            "Affirming an absolute referent need not imply one exhaustive formulation, "
            "but remaining hard contradictions must be acknowledged."
        ),
        "consequence": (
            "Pluralism differs from relativism by retaining truth constraints, standpoint "
            "qualification and non-contradiction."
        ),
        "trap": (
            "Do not declare a personal creator and its denial true in the same respect or "
            "make the meta-level pluralist claim exempt from criticism."
        ),
    },
    5: {
        "mechanism": (
            "Tolerance, acceptance, dialogue and freedom regulate coexistence at different "
            "levels of power, reciprocity and engagement."
        ),
        "consequence": (
            "Equal civic standing protects persons and conscience without settling "
            "religious truth or salvation."
        ),
        "trap": (
            "Do not treat permission by a majority as equality or group freedom as a "
            "licence to silence internal minorities."
        ),
    },
    6: {
        "mechanism": (
            "Hick uses a transcategorial Real and transformation, Vivekananda convergent "
            "paths, and Jain many-sidedness standpoint-conditioned assertion."
        ),
        "consequence": (
            "Each model explains diversity by a different metaphysics and faces "
            "unknowability, assimilation or contradiction pressures."
        ),
        "trap": (
            "Do not let Hick's pluralist meta-framework escape the parity and "
            "self-referential objections applied to first-order religions."
        ),
    },
    7: {
        "mechanism": (
            "Compare metaphysical unity, epistemic humility, civic concord, principled "
            "distance and dialogical practice as distinct resources."
        ),
        "consequence": (
            "Indian and Western resources can support non-relativist openness without "
            "erasing multiple religious ends or identity concerns."
        ),
        "trap": (
            "Do not collapse many-sidedness, many paths, social tolerance and Hickian "
            "pluralism into one doctrine."
        ),
    },
}


def transform_ascii(text: str) -> str:
    text = text.replace(
        "EXCLUSIVISM: one tradition alone has saving truth",
        "EXCLUSIVISM: one tradition has uniquely decisive truth and/or salvation",
    )
    if " identity/mission" not in text:
        text = text.replace(
            " objections: Hick imposes a meta-theory; the Real becomes unknowable; "
            "transformation test is vague.",
            " objections: unknowable Real | privileged meta-theory | vague transformation\n"
            " identity/mission cost: traditions are redescribed against self-understanding.",
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
        control = SESSION_CONTROLS[number]
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
        if number == 7 and "- **Indian-Western resources**" not in body:
            body = body.replace(
                "- **non-relativism**\n\n**How to use them:**",
                "- **non-relativism**\n"
                "- **Indian-Western resources**\n\n"
                "**How to use them:**",
                1,
            )
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
    axes = demote(
        extract_section(
            owner,
            "## 0A. FOUR AXES THAT MUST NOT BE MERGED ⚠️",
            "## 1. THE THREE POSITIONS ✅",
        )
    )
    hick = demote(
        extract_section(
            owner,
            "### 1.1 Hick's Copernican revolution and its burdens",
            "---",
        )
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + firewall + "\n\n" + axes,
            1,
        )
    if "#### 1.1 Hick's Copernican revolution and its burdens" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — HICK, VIVEKANANDA AND FOUNDATIONAL POSITIONS",
            hick,
        )
    source_control = (
        "### Local source and factual control\n\n"
        "- Local John Hick, *Philosophy of Religion*, print pp. 109–119 "
        "(PDF pp. 120–130), controls conflicting truth-claims and pluralist framework.\n"
        "- The local *Oxford Handbook of Philosophy of Religion*, print pp. 392–417 "
        "(PDF pp. 404–429), controls religious-diversity, competing-practice and "
        "toleration pressures.\n"
        "- Chatterjee–Datta, especially PDF pp. 109–118, controls Jain "
        "many-sidedness and conditional predication.\n"
        "- Social harmony is never used as evidence that contradictory doctrines are true."
    )
    if "### Local source and factual control" not in text:
        text = insert_before(
            text,
            "### Source-complete coverage ledger and answer-worthiness labels",
            source_control,
        )
    text = re.sub(
        r"(?m)^✅ \*\*Fact:\*\* In April 2026, the United Nations.*$\n"
        r"^⚠️ \*\*Inference:\*\* Public praise.*$\n"
        r"^\*\*Live source checked:\*\*.*$\n?",
        "⚠️ **Current-evidence policy:** civic harmony and interfaith praise are not "
        "evidence for a metaphysical pluralist theory; truth and coexistence remain distinct.\n",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^\*\*Technical definition:\*\* ⚠️ Inference: Public praise.*$",
        "**Technical definition:** The problem separates alethic truth, soteriological "
        "efficacy, epistemic access and civic status rather than inferring one axis from another.",
        text,
        count=1,
    )
    replacements = {
        "ONE religion true; other faiths        all are valid responses": (
            "one decisive truth other faiths        several authentic responses"
        ),
        "others false/      partially true,     to ONE ultimate Reality": (
            "and/or salvation   partially true,     to ultimate Reality"
        ),
        "no salvation       fulfilled in mine   (no single religion has": (
            "norm               fulfilled in mine   (not every claim is equal)"
        ),
        "(dogmatic,         Christians\")         Hick: the Real;": (
            "(truth-preserving; Christians\")         Hick: the Real;"
        ),
        " intolerant)            │               Vedānta/Vivekananda:": (
            " can be tolerant)       │               Vedānta/Vivekananda:"
        ),
        "Pluralist (all reach the one Real).\"** Indian Vedānta/Vivekananda = "
        "the classic pluralist model.": (
            "Pluralist (several authentic paths/ends).\"** Vivekananda offers a "
            "major convergence model whose pluralist or inclusivist status must be argued."
        ),
        "- **Pluralism (John Hick):** the great religions are **equally valid** human "
        "responses to the **one ultimate divine Reality (\"the Real\")**; each perceives "
        "the Real through its own cultural-conceptual \"lens\" (Kantian *phenomena* of "
        "the Real). *\"There is not merely one way but a plurality of ways of "
        "salvation/liberation.\"* ✅": (
            "- **Pluralism:** several traditions may be authentic responses to ultimate "
            "reality or realise different religious ends; this does not make every claim "
            "equally true. Hick treats major traditions as culturally conditioned "
            "responses to the Real, assessed by transformation. ✅"
        ),
        "- **Vivekananda — Universal Religion:** all religions are **true**, **different "
        "paths to the same goal** (the one Reality); they are stages/varieties suited to "
        "different temperaments — *\"as many faiths, so many paths.\"* No religion should "
        "destroy another; **harmony & acceptance** (not mere tolerance). ✅": (
            "- **Vivekananda — Universal Religion:** religions are valid paths suited to "
            "different temperaments and capable of convergence in realisation; acceptance "
            "is stronger than condescending tolerance. The model may remain inclusivist "
            "if Vedanta supplies the final meta-framework. ⚠️"
        ),
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = repair_session_contracts(text)
    text = transform_ascii(text)
    required = (
        "Exact printed ownership and cross-topic firewall",
        "FOUR AXES THAT MUST NOT BE MERGED",
        "Hick's Copernican revolution and its burdens",
        "Local source and factual control",
        "STARTING CONCEPT",
        "identity/mission cost",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Religious Pluralism transform missing: {missing}")
    return text


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    answer_lines = {
        "00": (
            "Separate truth, salvation, epistemic access and civic coexistence; success "
            "on one axis neither proves nor requires pluralism on the others."
        ),
        "01": (
            "Exclusivism reserves a decisive norm, inclusivism fulfils others through one "
            "centre and pluralism permits several authentic responses or ends."
        ),
        "02": (
            "Hick's Real explains conditioned manifestations, but noumenal unknowability, "
            "self-reference and identity-redescription pressure the meta-theory."
        ),
        "03": (
            "Vivekananda and Vedanta support convergence and acceptance, but one "
            "neo-Vedantic framework must not erase distinct doctrines or ends."
        ),
        "04": (
            "Jain many-sidedness qualifies assertions by standpoint and supports humility "
            "without making contradictions true in the same respect."
        ),
        "05": (
            "Tolerance and freedom secure equal civic standing under disagreement; they "
            "do not prove equal religious truth or salvation."
        ),
        "06": (
            "Deep disagreement explains persistent divergence and makes dialogue, "
            "fallibilism and explicit frameworks rational duties rather than proof of relativism."
        ),
        "07": (
            "Defensible pluralism preserves truth constraints, acknowledges hard "
            "contradictions and separates metaphysical theory from civic respect."
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
        "benchmark": "Religious-Pluralism reviewed eight-panel ASCII master",
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
        / f"topic-09_Complete-Learning-Session_{DATE}.md"
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
        9,
        changed,
        text_transform=transform_markdown,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Religious Pluralism and "
            "Absolute Truth: ownership, four-axis theory, Hick/Indian qualification, "
            "session contract and immutable dependent artifacts"
        ),
        baseline_score=97,
        repaired_score=100,
        issues_closed=[
            "exact ownership and cross-topic boundaries made explicit",
            "truth, salvation, epistemic access and civic coexistence separated",
            "exclusivism, inclusivism and pluralism definitions qualified",
            "Hick noumenal, self-reference, parity and identity costs completed",
            "Vivekananda, Vedanta, hard-contradiction and tolerance controls repaired",
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
