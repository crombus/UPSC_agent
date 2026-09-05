"""Generate the immutable 2026-09-03 Religious Experience successor only."""

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
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-06"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Religious-Experience.md"
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
    2: {
        "how": (
            "Use William James, ineffability, noetic quality, transiency and passivity "
            "to describe mystical experience, then assess fruits without confusing "
            "pragmatic value with metaphysical truth."
        ),
    },
    3: {
        "how": (
            "Compare Advaita and Radhakrishnan through non-dual awareness, spiritual "
            "intuition and Brahman, then separate the reported structure from its "
            "interpretive framework."
        ),
    },
    4: {
        "how": (
            "Separate psychological genuineness from veridicality, identify the religious "
            "object, test the perceptual model and apply diversity or contrary evidence "
            "as a defeater before judging public evidence."
        ),
    },
    6: {
        "how": (
            "Compare William James, Rudolf Otto, Advaita and Radhakrishnan through noetic "
            "disclosure and mysterium tremendum et fascinans, preserving their different "
            "objects and evidential claims."
        ),
    },
    7: {
        "how": (
            "Balance religious diversity and naturalistic explanation against the "
            "principle of credulity, defeaters and transformative fruits, then state the "
            "limit of public discourse."
        ),
    },
}


CLOSURE_CONTROLS: dict[int, dict[str, str]] = {
    1: {
        "mechanism": (
            "Separate phenomenology, claimed object, interpretation and epistemic force "
            "before assessing any report."
        ),
        "consequence": (
            "Sincerity, tradition-conformity and veridicality are distinct achievements."
        ),
        "trap": (
            "Do not treat subjective as unreal, ineffable as contentless or intensity as proof."
        ),
    },
    2: {
        "mechanism": (
            "James grades ineffability and noetic quality as defining marks, with "
            "transiency and passivity as usual accompaniments, and tests life by fruits."
        ),
        "consequence": (
            "Mystical authority may rationally affect the experiencer without coercively "
            "binding outsiders."
        ),
        "trap": (
            "Do not flatten James's two-plus-two marks or infer metaphysical truth from "
            "pragmatic transformation."
        ),
    },
    3: {
        "mechanism": (
            "Advaita interprets non-dual recognition as Brahman-realisation, while "
            "Radhakrishnan presents integral spiritual intuition as primary to doctrine."
        ),
        "consequence": (
            "Yogic, devotional, Buddhist and Vedantic experiences differ in structure, "
            "object and liberation claim."
        ),
        "trap": (
            "Do not collapse theistic relation, Advaitic identity, yogic isolation and "
            "Buddhist insight into one Indian mysticism."
        ),
    },
    4: {
        "mechanism": (
            "Perceptual and credulity models grant prima facie warrant, while diversity, "
            "unreliability and contrary evidence act as defeaters."
        ),
        "consequence": (
            "Neural or psychological explanation becomes a defeat only if it shows the "
            "experience unreliable or explanatorily complete without the object."
        ),
        "trap": (
            "Do not equate psychological genuineness, doctrinal interpretation and "
            "metaphysical veridicality."
        ),
    },
    5: {
        "mechanism": (
            "Mystical unity, numinous encounter, prayerful address and worshipful "
            "acknowledgement imply different relations to ultimacy."
        ),
        "consequence": (
            "Prayer presupposes a responsive addressee, while worship requires only a "
            "reality of supreme worth."
        ),
        "trap": (
            "Do not use prayer and worship as synonyms or make every sacred object a personal God."
        ),
    },
    6: {
        "mechanism": (
            "James, Otto, Advaita and Radhakrishnan must be compared on phenomenology, "
            "object, interpretation and epistemic claim."
        ),
        "consequence": (
            "Noetic insight, numinous encounter, non-dual identity and integral intuition "
            "are not four names for one uncontested experience."
        ),
        "trap": (
            "Do not let common-core language erase the logical difference between "
            "identity and relation."
        ),
    },
    7: {
        "mechanism": (
            "Balance credulity and testimony against naturalistic, diversity and "
            "constructivist defeaters, then test coherence and fruits."
        ),
        "consequence": (
            "Religious experience can be publicly discussed as report and practice while "
            "remaining privately stronger as evidence."
        ),
        "trap": (
            "Do not treat public discussability as public proof or brain correlation as "
            "automatic disproof."
        ),
    },
}


def transform_ascii(text: str) -> str:
    text = text.replace(
        " 3 EPISTEMIC FORCE: does seeming-to-encounter justify belief?",
        " 3 INTERPRETATION: how does a tradition name and frame the seeming?\n"
        " 4 EPISTEMIC FORCE: does seeming-to-encounter justify belief?",
    )
    text = text.replace(
        "Buddhism             emptiness, cessation or suchness without creator",
        "Buddhism             Dharma/cessation insight without a personal creator",
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
    method = demote(
        extract_section(
            owner,
            "## 0A. FOUR ANALYTICAL LAYERS AND EXPERIENCE VARIETIES ⚠️",
            "---",
        )
    )
    indian_bridge = demote(
        extract_section(
            owner,
            "### 2.1 Indian experience-types — bounded comparative bridge",
            "---",
        )
    )
    mediation = demote(
        extract_section(
            owner,
            "### Interpretation and mediation dispute",
            "## 4. COMPARISON GRID ⚠️",
        )
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + firewall + "\n\n" + method,
            1,
        )
    if "#### 2.1 Indian experience-types — bounded comparative bridge" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — INDIAN ACCOUNTS OF RELIGIOUS EXPERIENCE",
            indian_bridge,
        )
    if "#### Interpretation and mediation dispute" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — COMPARATIVE EVALUATION OF RELIGIOUS EXPERIENCE",
            mediation,
        )
    source_control = (
        "### Local source and factual control\n\n"
        "- The local *Oxford Handbook of Philosophy of Religion*, print pp. 138–167 "
        "(PDF pp. 150–179), controls mystical-experience definition, phenomenology, "
        "ineffability and epistemic models.\n"
        "- Local Radhakrishnan, *Indian Philosophy*, Vol. II, especially PDF "
        "pp. 370–445, supports bounded yogic, Vedantic and intuitive comparisons; "
        "the 2025 stem's named work remains *The Hindu View of Life*.\n"
        "- No neural correlation, psychological mechanism or reported transformation "
        "is treated as automatic proof or disproof of a transcendent object."
    )
    if "### Local source and factual control" not in text:
        text = insert_before(
            text,
            "### Source-complete coverage ledger and answer-worthiness labels",
            source_control,
        )
    text = re.sub(
        r"(?m)^✅ \*\*Fact:\*\* A 2025 \*Frontiers in Neuroscience\* review.*$\n"
        r"^⚠️ \*\*Inference:\*\* Neural mediation.*$\n?",
        "⚠️ **Naturalistic-explanation policy:** neural mediation may explain a "
        "mechanism or correlate; it does not by itself establish either veridicality "
        "or illusion.\n",
        text,
        count=1,
    )
    text = text.replace(
        "Buddhism → nirvāṇa (no personal deity).",
        "Buddhism → insight oriented to Dharma and cessation (nirvāṇa), not a personal deity.",
    )
    text = repair_session_contracts(text)
    text = transform_ascii(text)
    required = (
        "Exact printed ownership and cross-topic firewall",
        "FOUR ANALYTICAL LAYERS AND EXPERIENCE VARIETIES",
        "Indian experience-types",
        "Interpretation and mediation dispute",
        "Local source and factual control",
        "STARTING CONCEPT",
        "4 EPISTEMIC FORCE",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Religious Experience transform missing: {missing}")
    return text


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    answer_lines = {
        "00": (
            "Analyse religious experience through phenomenology, claimed object, "
            "interpretation and epistemic force; sincerity never settles veridicality."
        ),
        "01": (
            "James grades ineffability and noetic quality as defining, transiency and "
            "passivity as usual, and fruits as pragmatic rather than metaphysical tests."
        ),
        "02": (
            "Otto's numinous combines overwhelming mystery and attraction; its "
            "phenomenological distinctiveness does not independently prove a Holy object."
        ),
        "03": (
            "Advaita claims non-dual identity, Radhakrishnan integral intuition, Yoga "
            "disciplined absorption and devotional traditions relation to a personal Lord."
        ),
        "04": (
            "God, the Holy, Brahman and Dharma-oriented cessation are different object "
            "models, not interchangeable names for one uncontested referent."
        ),
        "05": (
            "Credulity and testimony give defeasible warrant; diversity, unreliability "
            "and contrary evidence can defeat it."
        ),
        "06": (
            "Naturalistic explanation does not automatically debunk, and public "
            "discussion of reports does not convert private warrant into public proof."
        ),
        "07": (
            "A complete answer separates occurrence, interpretation and truth, compares "
            "Indian/Western structures and closes with a graded evidential verdict."
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
        "benchmark": "Religious-Experience reviewed eight-panel ASCII master",
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
        / f"topic-06_Complete-Learning-Session_{DATE}.md"
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
        6,
        changed,
        text_transform=transform_markdown,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Religious Experience: "
            "ownership, four-layer method, varieties, interpretation/veridicality, "
            "session contract and immutable dependent artifacts"
        ),
        baseline_score=97,
        repaired_score=100,
        issues_closed=[
            "exact ownership and cross-topic boundaries made explicit",
            "phenomenology, object, interpretation and epistemic force separated",
            "mystical, numinous, conversion, revelatory, devotional and yogic varieties unified",
            "subjectivity, ineffability and neural-correlation controls repaired",
            "Indian experience and mediation comparisons completed",
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
