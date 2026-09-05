"""Generate the immutable 2026-09-03 Notions of God semantic successor only."""

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
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-01"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Notions-of-God.md"
)


def extract(text: str, start: str, end: str) -> str:
    match = re.search(
        rf"(?ms)^{re.escape(start)}\s*$.*?(?=^{re.escape(end)}\s*$)",
        text,
    )
    if not match:
        raise ValueError(f"Cannot extract canonical section {start!r}.")
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


SESSION_GUIDANCE = {
    1: (
        "Use reference, divine predicates and model of ultimacy as the answer spine: "
        "identify the referent, classify personal or impersonal form, map transcendence "
        "and immanence, then test coherence."
    ),
    2: (
        "Use theism, deism, pantheism and panentheism as a common comparison grid: "
        "state each creator-world relation, contrast intervention and immanence, then "
        "reject any pantheism-panentheism collapse."
    ),
    3: (
        "Organise the answer through aseity, omnipotence, omniscience and perfect "
        "goodness: define each attribute, test their compossibility with eternity and "
        "freedom, answer the strongest objection, and qualify the final coherence claim."
    ),
    9: (
        "Use Madhva dualism, Saiva Siddhanta and Sakti as the comparison spine: specify "
        "real difference, personal lordship and divine manifestation before judging how "
        "each model relates God, world and persons."
    ),
    10: (
        "Build a comparative God-world-human relation through creation, sustenance, "
        "dependence and human freedom: apply the same axes to every model, expose the "
        "decisive incompatibility, and close with a graded verdict."
    ),
    12: (
        "Compare personal theism and the impersonal absolute through coherence and "
        "religious adequacy: state common criteria, test explanatory gains against "
        "conceptual costs, answer one objection, and give a qualified synthesis."
    ),
    13: (
        "Use Notions of God answer architecture, a definition-first opening, a comparison "
        "axis and an objection-reply sequence: name the doctrine, satisfy the PYQ demand, "
        "and finish with a qualified verdict."
    ),
}


def repair_refreshed_session_contracts(text: str) -> str:
    session_re = re.compile(
        r"(?ms)^### SESSION (\d+) — ([^\n]+)\n(.*?)(?=^### SESSION \d+ — |\Z)"
    )

    def repair(match: re.Match[str]) -> str:
        number = int(match.group(1))
        title = match.group(2).strip()
        body = match.group(3)

        if number == 10:
            body = body.replace(
                "- **worship**\n\n**How to use them:**",
                "- **worship**\n"
                "- **comparative God-world-human relation**\n\n"
                "**How to use them:**",
                1,
            )
        elif number == 12:
            body = re.sub(
                r"(?m)^\*\*Plain-language definition:\*\* .+$",
                "**Plain-language definition:** Critical synthesis compares competing "
                "God-models by common criteria of coherence, explanatory reach and "
                "religious adequacy without assuming that one criterion decides all.",
                body,
                count=1,
            )
        elif number == 13:
            body = body.replace(
                "- **PYQ demand**\n\n**How to use them:**",
                "- **PYQ demand**\n"
                "- **Notions of God answer architecture**\n\n"
                "**How to use them:**",
                1,
            )

        if number in SESSION_GUIDANCE:
            body = re.sub(
                r"(?m)^\*\*How to use them:\*\* .+$",
                f"**How to use them:** {SESSION_GUIDANCE[number]}",
                body,
                count=1,
            )

        closure = re.compile(
            r"(?ms)(^#### CLOSING RECALL FLOW[^\n]*\n"
            r"```closure-flow\n)(.*?)(```)"
        )

        def repair_closure(closure_match: re.Match[str]) -> str:
            flow = closure_match.group(2)
            if re.search(r"(?m)^STARTING CONCEPT:", flow):
                flow = re.sub(
                    r"(?m)^STARTING CONCEPT:.*$",
                    f"STARTING CONCEPT: {title}",
                    flow,
                    count=1,
                )
            elif re.search(r"(?m)^SUBTOPIC:", flow):
                flow = re.sub(
                    r"(?m)^(SUBTOPIC:.*)$",
                    rf"\1\nSTARTING CONCEPT: {title}",
                    flow,
                    count=1,
                )
            else:
                flow = f"STARTING CONCEPT: {title}\n{flow}"
            return closure_match.group(1) + flow + closure_match.group(3)

        body = closure.sub(repair_closure, body, count=1)
        return f"### SESSION {number} — {title}\n{body}"

    return session_re.sub(repair, text)


def transform_ascii(text: str) -> str:
    text = text.replace("God-world-man", "God-world-human")
    text = text.replace("God–world–man", "God–world–human")
    text = text.replace("God-Man", "God-Human")
    text = text.replace("God–Man", "God–Human")
    text = text.replace(
        "What kind of reality is called “God”, and how is it related to man and the world?",
        "What kind of reality is called “God”, and how is it related to humans and the world?",
    )
    text = text.replace("God-man", "God-human")
    text = text.replace("GOD-MAN", "GOD-HUMAN")
    if " +-> MONOTHEISM: one supreme God" not in text:
        text = text.replace(
            "WESTERN NOTIONS\n",
            "WESTERN NOTIONS\n"
            " +-> MONOTHEISM: one supreme God | POLYTHEISM: several genuine deities\n"
            " +-> HENOTHEISM: one addressed as supreme | MONOLATRY: one worshipped\n",
        )
    text = text.replace(
        " +-> PANTHEISM: God = world/nature",
        " +-> PANTHEISM: God and all-inclusive reality are one, not a physical aggregate",
    )
    if " ROLES: creator | sustainer" not in text:
        text = text.replace(
            " +-> PROCESS/DIPOLAR GOD\n",
            " ROLES: creator | sustainer | providential ruler | moral governor |\n"
            "        ground of being | absolute\n"
            " +-> PROCESS/DIPOLAR GOD\n",
        )
    text = text.replace(
        "ATTRIBUTES: omnipotence | omniscience | goodness | eternity\n"
        "            immutability | simplicity | necessity | aseity",
        "ATTRIBUTES: omnipotence | omniscience | goodness | eternity\n"
        "            immutability | simplicity | necessity | aseity | personhood\n"
        " timeless action -> temporal effects; contingency remains pressured\n"
        " immutability -> constancy, but real response/personality is difficult\n"
        " personhood -> analogical intelligence/will/love, not body or male gender",
    )
    text = text.replace(
        "NYĀYA ĪŚVARA: God + selves + atoms + space/time are real",
        "NYĀYA PERSONAL GOD (ĪŚVARA): one, eternal, omniscient, incorporeal",
    )
    if " INDIAN BOUNDARY: Yoga special self" not in text:
        text = text.replace(
            " karma/adṛṣṭa -> divine coordination -> fitting results; selves remain distinct",
            " karma/adṛṣṭa -> divine coordination -> fitting results; selves remain distinct\n"
            " INDIAN BOUNDARY: Yoga special self | Mīmāṃsā/Sāṃkhya no required creator |\n"
            "                  Buddhism/Jainism religious without omnipotent creator",
        )
    text = text.replace(
        "TRAPS: personal != anthropomorphic | transcendent != spatially remote",
        "TRAPS: personal != anthropomorphic/bodily/male | transcendent != spatially remote",
    )
    if " analogy/symbol permit real reference" not in text:
        text = text.replace(
            " apṛthak-siddhi != identity | Nyāya God = efficient cause | monism != monotheism",
            " apṛthak-siddhi != identity | Nyāya God = efficient cause | monism != monotheism\n"
            " analogy/symbol permit real reference without finite or gendered literalism",
        )
    return text


def transform_markdown(text: str, generation: int) -> str:
    owner = OWNER.read_text(encoding="utf-8")
    boundary = demote(
        extract(
            owner,
            "## Exact printed ownership and cross-topic firewall",
            "## 0. ONE-SCREEN MAP ⚠️",
        )
    )
    taxonomy = demote(
        extract(owner, "### 1.1 Classification before evaluation", "### 1.2 Role-profiles: what “God” is doing in the concept")
    )
    roles = demote(
        extract(
            owner,
            "### 1.2 Role-profiles: what “God” is doing in the concept",
            "## 2. INDIAN NOTIONS ✅",
        )
    )
    attributes = demote(
        extract(
            owner,
            "### 8.1A The attribute package and its coherence costs",
            "### 8.2 Spinoza's God or Nature",
        )
    )
    indian_profiles = demote(
        extract(
            owner,
            "### 8.4A Nyāya God (*Īśvara*) as an owned notion, not a proof",
            "### 8.5 Polytheism, henotheism and the Vedic case (2018 Q5(e) owner-module)",
        )
    )
    language = demote(
        extract(
            owner,
            "### 8.8A Anthropomorphism, analogy, symbol and gendered God-language",
            "## 9. INTER-THINKER / INTER-SCHOOL DEBATES",
        )
    )
    evidence = demote(
        extract(
            owner,
            "### 12.1 Selectable evidence bank",
            "<!-- expanded-pyq-depth:start -->",
        )
    )

    text = re.sub(
        r"(?m)^!\[Notions of God[^\]]*\]\([^)]+\)\s*\n+"
        r"\*Concept map:.*?\*\s*\n*",
        "",
        text,
        count=1,
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + boundary,
            1,
        )
    if "#### 1.1 Classification before evaluation" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — THEISM, DEISM, PANTHEISM AND PANENTHEISM",
            taxonomy + "\n\n" + roles,
        )
    if "#### 8.1A The attribute package and its coherence costs" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — DIVINE ATTRIBUTES AND THEIR COHERENCE",
            attributes,
        )
        text = insert_before(text, "##### 8.2 Spinoza's God or Nature", demote(attributes, 1))
    if "#### 8.4A Nyāya God (*Īśvara*) as an owned notion, not a proof" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — NYAYA'S NOTION OF GOD",
            indian_profiles,
        )
        text = insert_before(
            text,
            "##### 8.5 Polytheism, henotheism and the Vedic case "
            "(2018 Q5(e) owner-module)",
            demote(indian_profiles, 1),
        )
    if "#### 8.8A Anthropomorphism, analogy, symbol and gendered God-language" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — CRITICAL SYNTHESIS OF COMPETING GOD-MODELS",
            language,
        )
        text = insert_before(
            text,
            "#### 9. INTER-THINKER / INTER-SCHOOL DEBATES",
            demote(language, 1),
        )
    if "#### 12.1 Selectable evidence bank" not in text:
        text = insert_before(
            text,
            "#### CORPUS-DRIVEN DEPTH DELTA (expanded PYQ audit)",
            evidence,
        )

    text = text.replace(
        "11. ⚠️ Do not merge Śaiva Siddhānta (dualistic, "
        "*pati–paśu–pāśa*) with Kashmir Śaivism (non-dual, *ābhāsa*); and do "
        "not describe Madhva's *bimba–pratibimba* as identity — it is dependence.",
        "11. ⚠️ Do not merge Śaiva Siddhānta (dualistic, "
        "*pati–paśu–pāśa*) with Kashmir Śaivism (non-dual, *ābhāsa*); and do "
        "not describe Madhva's *bimba–pratibimba* as identity — it is dependence.\n"
        "12. ⚠️ Do not equate monotheism with the whole of classical theism.\n"
        "13. ⚠️ Do not merge creator, sustainer, moral governor, ground and absolute.\n"
        "14. ⚠️ Do not identify non-dual Brahman with the classical personal creator.\n"
        "15. ⚠️ Do not answer the Nyāya nature question with proofs alone.\n"
        "16. ⚠️ Do not use timelessness without temporal-action and contingency costs.\n"
        "17. ⚠️ Do not infer body or male gender from divine personhood.\n"
        "18. ⚠️ Do not expand process/finite/open models into a replacement syllabus.",
        1,
    )
    text = text.replace(
        "**Keywords:** [FACT] classical theism",
        "**English-first retrieval:** monotheism · polytheism · contextual one-deity "
        "supremacy (henotheism) · exclusive one-God worship (monolatry) · creator · "
        "sustainer · moral governor · ground of being · absolute · timelessness · "
        "immutability · personhood · analogy · gendered language\n\n"
        "**Keywords:** [FACT] classical theism",
        1,
    )
    text = text.replace(
        "- John Hick, *Philosophy of Religion*.",
        "- John Hick, *Philosophy of Religion*.\n"
        "- Local searchable John Hick PDF, especially pp. 16-17 and 52-63; "
        "local searchable *Oxford Handbook* PDF, especially pp. 40, 63 and 79-90.\n"
        "- S. C. Chatterjee and D. M. Datta, local searchable *An Introduction "
        "to Indian Philosophy* PDF, especially pp. 262-264 and 465-467.",
        1,
    )
    text = text.replace(
        "God = world/nature",
        "God and all-inclusive reality are one (not a physical aggregate)",
    )
    text = text.replace(
        "God = world",
        "God and all-inclusive reality are one",
    )
    text = text.replace(
        "COMPARATIVE GOD-WORLD-MAN RELATIONS",
        "COMPARATIVE GOD-WORLD-HUMAN RELATIONS",
    )
    text = transform_ascii(text)

    required = (
        "Exact printed ownership and cross-topic firewall",
        "Monotheism",
        "Role-profiles",
        "Timeless-action dilemma",
        "Nyāya God",
        "Theistic and non-creator Indian profiles",
        "gendered God-language",
        "Selectable evidence bank",
        "N6 · Personhood is not anthropomorphic embodiment",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Notions of God semantic transform missing: {missing}")
    return repair_refreshed_session_contracts(text)


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    updates = {
        "00": (
            "Classify nature, role, attributes and relation separately; personal "
            "does not mean bodily or male, and comparison axes are not equations."
        ),
        "01": (
            "Monotheism counts one God; classical theism additionally profiles a "
            "necessary creator, sustainer, ruler and moral governor."
        ),
        "02": (
            "Power, knowledge, goodness, eternity, immutability, simplicity and "
            "personhood survive only through specified, cost-bearing readings."
        ),
        "06": (
            "Nyāya profiles one eternal omniscient incorporeal efficient cause and "
            "karmic governor; proofs and anti-creator replies belong elsewhere."
        ),
        "08": (
            "Analogy and symbol can preserve reference without anthropomorphic or "
            "gendered literalism; non-dual Brahman is not classical personal God."
        ),
    }
    for stage in spec.get("stages", []):
        stage_id = str(stage.get("id"))
        if stage_id in updates:
            stage["answer_line"] = updates[stage_id]
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
    target = source.with_name(
        f"{TOPIC_KEY}-ascii-g{generation}-{DATE}.json"
    )
    if target.exists():
        raise RuntimeError(f"Refusing to overwrite immutable ASCII spec: {target}")
    shared = json.loads(source.read_text(encoding="utf-8"))
    topic = copy.deepcopy(
        next(
            item
            for item in shared["topics"]
            if item["topic_key"] == TOPIC_KEY
        )
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
        "benchmark": "Notions-of-God reviewed ten-panel ASCII master",
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
    if int(latest["generation"]) != 16:
        raise ValueError(
            f"Expected reviewed predecessor g16, found {latest['record_id']}."
        )
    base.DATE = DATE
    generation = int(latest["generation"]) + 1
    next_markdown = (
        base.repo(latest["markdown"]).parents[1]
        / f"g{generation}"
        / f"topic-01_Complete-Learning-Session_{DATE}.md"
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
        base.rel(Path(base.__file__)),
        base.rel(
            ROOT / "tools" / "philosophy_indian_religion_deep_quality_repair.py"
        ),
        base.rel(OWNER),
        base.rel(ascii_spec),
    }
    result = base.process_topic(
        1,
        changed,
        text_transform=transform_markdown,
        ascii_transform=transform_ascii,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Notions of God: taxonomy, "
            "role profiles, attribute coherence, Nyaya/Indian parity, God-language "
            "controls and immutable dependent artifacts"
        ),
        baseline_score=97,
        repaired_score=100,
        issues_closed=[
            "exact syllabus ownership and cross-topic boundaries made explicit",
            "notion/role taxonomy and attribute-coherence gaps repaired",
            "Nyaya and non-creator Indian profiles promoted without importing proofs",
            "anthropomorphism, analogy and gender-language controls added",
            "all thirteen refreshed session contracts repaired",
            "ASCII, graphical and asset metadata regenerated from one repaired source",
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
