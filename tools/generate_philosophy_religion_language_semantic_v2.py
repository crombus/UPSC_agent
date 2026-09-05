"""Generate the immutable 2026-09-03 Nature of Religious Language successor only."""

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
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-10"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Religious-Language.md"
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


def transform_ascii(text: str, generation: int) -> str:
    text = re.sub(
        r"IDENTITY -> learner-v2:g\d+ \| generated \d{4}-\d{2}-\d{2} \| approval FALSE",
        f"IDENTITY -> learner-v2:g{generation} | generated {DATE} | approval FALSE",
        text,
        count=1,
    )
    if "MEANING != empirical factuality" not in text:
        text = text.replace(
            'CONTROL -> "God is good" may be ANALOGICAL and COGNITIVE at once.\n',
            'CONTROL -> "God is good" may be ANALOGICAL and COGNITIVE at once.\n'
            "MEANING != empirical factuality; utterances may also enact or prescribe.\n",
        )
    if "RAMANUJA -> real auspicious predicates" not in text:
        text = text.replace(
            'BHAGA-TYAGA -> discard incompatible connotations in "tat tvam asi"\n',
            'BHAGA-TYAGA -> discard incompatible connotations in "tat tvam asi"\n'
            "RAMANUJA -> real auspicious predicates of personal Brahman\n"
            "BUDDHIST -> conventional truth works without intrinsic essence\n"
            "JAIN -> conditional predication states the respect of assertion\n",
        )
    return text


def transform_markdown(text: str, generation: int) -> str:
    owner = OWNER.read_text(encoding="utf-8")
    firewall = demote(
        extract_section(
            owner,
            "## Exact printed ownership and cross-topic firewall",
            "---",
        )
    )
    semantic_grid = demote(
        extract_section(
            owner,
            "## 0A. SEMANTIC MODE AND SPEECH FUNCTION ⚠️",
            "---",
        )
    )
    verification = demote(
        extract_section(
            owner,
            "### 1.1 Verification, falsification and empirical factuality",
            "---",
        )
    )
    indian = demote(
        extract_section(
            owner,
            "### 2.1 Indian semantic strategies — bounded comparison",
            "---",
        )
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + firewall + "\n\n" + semantic_grid,
            1,
        )
    if "#### 1.1 Verification, falsification and empirical factuality" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — COGNITIVISM, NON-COGNITIVISM AND FALSIFICATION",
            verification,
        )
    if "#### 2.1 Indian semantic strategies — bounded comparison" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — INDIAN AND WESTERN STRATEGIES OF RELIGIOUS SPEECH",
            indian,
        )
    source_control = (
        "### Local source and factual control\n\n"
        "- Local John Hick, *Philosophy of Religion*, print pp. 82–107 "
        "(PDF pp. 93–118), controls analogy, symbol, non-cognitive use, "
        "language-games and verification.\n"
        "- The local *Oxford Handbook of Philosophy of Religion*, print pp. 220–244 "
        "(approximately PDF pp. 232–256), controls realism, symbolism, "
        "Braithwaite and Wittgensteinian boundaries.\n"
        "- Indian comparisons are bounded structural parallels; Paper I owners retain "
        "Advaita, Ramanuja, Buddhist, Jain and Mimamsa doctrine.\n"
        "- The verified ICML item remains an illustration of translation mediation only, "
        "never evidence for a semantic theory."
    )
    if "### Local source and factual control" not in text:
        text = insert_before(
            text,
            "### Source-complete coverage ledger and answer-worthiness labels",
            source_control,
        )
    text = transform_ascii(text, generation)
    required = (
        "Exact printed ownership and cross-topic firewall",
        "SEMANTIC MODE AND SPEECH FUNCTION",
        "Verification, falsification and empirical factuality",
        "Indian semantic strategies",
        "Local source and factual control",
        "MEANING != empirical factuality",
        "RAMANUJA -> real auspicious predicates",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Religious Language transform missing: {missing}")
    return text


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    answer_lines = {
        "00": (
            "Separate semantic mode from truth-aptness: analogy or symbol explains how "
            "a statement signifies, not by itself whether it is true."
        ),
        "01": (
            "Aquinas preserves real predication through causal participation, while "
            "Scotus secures inference through semantic—not ontological—univocity."
        ),
        "02": (
            "Tillichian symbols participate and transform rather than merely point, but "
            "symbolic realism still owes a disciplined referent."
        ),
        "03": (
            "Ayer questions verification, Flew falsification, Hare offers bliks, Mitchell "
            "defeasible trust and Hick possible eschatological confirmation."
        ),
        "04": (
            "Braithwaite captures moral commitment and Wittgensteinian grammar captures "
            "life-orientation, but neither should erase believers' realist intent."
        ),
        "05": (
            "Performative and self-involving force can supplement cognitive content; "
            "Ramsey's model-and-qualifier stretches ordinary language without equivocation."
        ),
        "06": (
            "Advaita negates and indirectly indicates, Ramanuja affirms real attributes, "
            "Buddhism uses conventional truth and Jainism qualifies standpoint."
        ),
        "07": (
            "Symbol may lead toward mysticism by becoming self-effacing, but it can also "
            "arrest in literalism or constitute experience from the start."
        ),
        "08": (
            "All fourteen PYQs require directive-specific mechanisms, exact attribution "
            "and separation of HOW from WHETHER."
        ),
        "09": (
            "The strongest verdict is mixed and vulnerable: assertoric, symbolic and "
            "performative language with apophatic limits and real defeaters."
        ),
    }
    for stage in spec.get("stages", []):
        stage_id = str(stage.get("id"))
        if stage_id in answer_lines:
            stage["answer_line"] = answer_lines[stage_id]
    return spec


def write_generation_ascii_spec(
    source: Path,
    generation: int,
    markdown_path: Path,
    transformed_markdown: str,
) -> Path:
    target = source.with_name(f"{TOPIC_KEY}-g{generation}-{DATE}.json")
    if target.exists():
        raise RuntimeError(f"Refusing to overwrite immutable ASCII spec: {target}")
    data = json.loads(source.read_text(encoding="utf-8"))
    topic = copy.deepcopy(
        next(item for item in data["topics"] if item["topic_key"] == TOPIC_KEY)
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
        "schema_version": 2,
        "benchmark": "Religious-Language reviewed ten-panel ASCII master",
        "generated_on": DATE,
        "record_id": f"{TOPIC_KEY}:learner-v2:g{generation}",
        "generation": generation,
        "approval": False,
        "scope": f"{TOPIC_KEY} immutable generation g{generation}",
        "constraints": copy.deepcopy(data.get("constraints", {})),
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
    if int(latest["generation"]) < 12:
        raise ValueError(
            f"Expected reviewed predecessor g12 or later, found {latest['record_id']}."
        )
    base.DATE = DATE
    generation = int(latest["generation"]) + 1
    next_markdown = (
        base.repo(latest["markdown"]).parents[1]
        / f"g{generation}"
        / f"topic-10_Complete-Learning-Session_{DATE}.md"
    )
    preview_text = transform_markdown(
        base.repo(latest["markdown"]).read_text(encoding="utf-8"),
        generation,
    )
    old_graphical = json.loads(
        base.repo(latest["continuous_core_first"]["graphical_spec"]).read_text(
            encoding="utf-8"
        )
    )
    source_ascii_spec = base.repo(old_graphical["ascii_spec"])
    ascii_spec = write_generation_ascii_spec(
        source_ascii_spec,
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
        base.rel(OWNER),
        base.rel(ascii_spec),
    }
    result = base.process_topic(
        10,
        changed,
        text_transform=transform_markdown,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Nature of Religious "
            "Language: ownership, semantic-mode/function, verification/falsification, "
            "Indian comparison and immutable dependent artifacts"
        ),
        baseline_score=96,
        repaired_score=100,
        issues_closed=[
            "pre-existing 27-August doctrine and attribution repairs preserved",
            "exact ownership and cross-topic boundaries made explicit",
            "semantic mode, speech function and empirical factuality separated",
            "Ayer and Flew-Hare-Mitchell-Hick sequence made executable",
            "Ramanuja, Buddhist, Jain and Mimamsa comparisons completed",
            "generation-specific embedded/manual/standalone ASCII identity repaired",
            "graphical artifacts and canonical asset metadata regenerated",
        ],
        ascii_spec_path=ascii_spec,
        canonical_asset_folder=canonical_asset_folder,
        ascii_from_markdown=True,
        expected_mcq_count=56,
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
