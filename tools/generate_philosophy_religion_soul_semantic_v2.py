"""Generate the immutable 2026-09-03 Soul/Rebirth/Liberation successor only."""

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
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-04"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Soul-Immortality-Rebirth.md"
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
        "how": (
            "Use immortality, survival, rebirth, reincarnation, resurrection and "
            "liberation as separate answer stages, then identify whether soul, person, "
            "causal continuity or divine memory bears continuity."
        ),
    },
    3: {
        "plain": (
            "Rebirth is renewed embodied or conditioned existence within a karmic series; "
            "traditions disagree whether an enduring soul or only causal continuity "
            "connects lives."
        ),
        "technical": (
            "Karma supplies the action-consequence structure and rebirth supplies its "
            "trans-life field, while reincarnation specifically presupposes a substantial "
            "self that is re-embodied."
        ),
    },
    4: {
        "how": (
            "Use no permanent self, dependent origination, causal continuum and karmic "
            "transmission to explain why rebirth is neither the same person-substance nor "
            "wholly different, without reintroducing a migrating soul."
        ),
    },
    5: {
        "how": (
            "Compare liberation, bondage, nirvana, moksha, apavarga and kaivalya through "
            "each school's self, cause, means and final state rather than assuming one "
            "common experience."
        ),
    },
    6: {
        "how": (
            "Contrast enduring self, ultimate reality and liberation while living in "
            "Advaita with qualified non-dualism, devotion and divine grace in theistic "
            "Vedanta, preserving post-liberation individuality differences."
        ),
    },
    7: {
        "how": (
            "Use conscious soul, karmic matter, influx and shedding to explain how perfect "
            "knowledge and the liberated individual emerge without merger into an absolute."
        ),
    },
    8: {
        "how": (
            "Compare release, liberation while living and isolation through cessation of "
            "pain, non-dual knowledge and purusha-prakriti discrimination; do not merge "
            "Nyaya, Advaita and Samkhya termini."
        ),
    },
}


CLOSURE_CONTROLS: dict[int, dict[str, str]] = {
    1: {
        "mechanism": (
            "Define each survival term, identify the continuity-bearer and ask whether "
            "the relation claimed is necessary, sufficient or merely possible."
        ),
        "consequence": (
            "Immortality, rebirth, reincarnation, resurrection and liberation can occur "
            "in different combinations across traditions."
        ),
        "trap": (
            "Do not use soul, self, person, rebirth and liberation as synonyms."
        ),
    },
    2: {
        "mechanism": (
            "Plato's cyclical, recollection, affinity and Form-of-Life arguments support "
            "different claims and require separate assessment."
        ),
        "consequence": (
            "Pre-existence, simplicity or affinity does not automatically establish the "
            "survival of this individual person."
        ),
        "trap": (
            "Do not merge Plato's four arguments or ignore bodily dependence, interaction "
            "and personal-identity objections."
        ),
    },
    3: {
        "mechanism": (
            "Karma structures consequences across lives; rebirth is the wider continuity "
            "claim, while reincarnation specifically requires a substantial transmigrant."
        ),
        "consequence": (
            "A karmic theory needs a continuity-bearer but not necessarily an immortal "
            "soul, as Buddhism demonstrates."
        ),
        "trap": (
            "Do not reduce karma to debt, fatalism or retrospective certainty about "
            "another person's past."
        ),
    },
    4: {
        "mechanism": (
            "Dependent origination links impermanent aggregates through causal continuity "
            "without a permanent self or numerical identity."
        ),
        "consequence": (
            "The later continuum is neither the same substance nor wholly unrelated, so "
            "responsibility is causal rather than soul-based."
        ),
        "trap": (
            "Do not call Buddhist rebirth reincarnation or describe nirvana as annihilation "
            "of a self."
        ),
    },
    5: {
        "mechanism": (
            "Compare each liberation by its self, bondage, direct means and final state."
        ),
        "consequence": (
            "Shared English 'liberation' conceals identity, communion, isolation, cessation "
            "of suffering and perfected individuality."
        ),
        "trap": (
            "Do not merge moksha, nirvana, apavarga, kaivalya and Jain siddhahood."
        ),
    },
    6: {
        "mechanism": (
            "Advaita removes ignorance of self-Brahman identity, while theistic Vedanta "
            "perfects the enduring soul's dependence through devotion and grace."
        ),
        "consequence": (
            "Liberation while living preserves empirical embodiment through already-"
            "fructifying karma without making bondage ultimately real."
        ),
        "trap": (
            "Do not attribute Advaitic identity to qualified non-dualism or treat devotion "
            "as the same kind of means as knowledge."
        ),
    },
    7: {
        "mechanism": (
            "Passion and action produce karmic influx and bondage; restraint and austerity "
            "stop and shed matter until perfect knowledge and final liberation."
        ),
        "consequence": (
            "Jain liberation perfects an eternally individual soul rather than merging it "
            "or reducing it to contentless isolation."
        ),
        "trap": (
            "Do not equate perfect knowledge with final disembodied liberation or use "
            "Samkhya kaivalya as the Jain terminus."
        ),
    },
    8: {
        "mechanism": (
            "Nyaya release ends pain-generating qualities, Advaita living liberation "
            "removes ignorance and Samkhya-Yoga isolation follows discriminative insight."
        ),
        "consequence": (
            "The three termini presuppose incompatible accounts of consciousness, bondage "
            "and what remains."
        ),
        "trap": (
            "Do not substitute the Yoga path-list for a comparison of apavarga, "
            "jivanmukti and kaivalya."
        ),
    },
    9: {
        "mechanism": (
            "Knowledge, disciplined action and devotion may be direct means, qualifications "
            "or sequential aids depending on whether liberation is produced or uncovered."
        ),
        "consequence": (
            "The paths can converge in ethical function while diverging in metaphysical "
            "terminus."
        ),
        "trap": (
            "Do not harmonise every school or turn the Gita's convergence into proof that "
            "all paths have identical status."
        ),
    },
    10: {
        "mechanism": (
            "Compare soul-immortality, embodied resurrection, substantial reincarnation "
            "and causal rebirth by identity criterion, mechanism and telos."
        ),
        "consequence": (
            "Replica and duplication problems show that qualitative similarity or memory "
            "continuity may be insufficient for numerical identity."
        ),
        "trap": (
            "Do not treat resurrection as repeated rebirth or infer scientific proof from "
            "testimony, desire or disputed experience."
        ),
    },
}


def transform_ascii(text: str) -> str:
    if "SELF = first-person or identity principle" not in text:
        text = text.replace(
            "SOUL = alleged enduring subject | PERSONAL IDENTITY = what makes later person same\n"
            " IMMORTALITY = survival of death | REBIRTH = new embodied existence\n"
            " RESURRECTION = divine restoration of embodied person | LIBERATION = release from bondage",
            "SOUL = alleged enduring subject | SELF = first-person or identity principle\n"
            " PERSON = embodied/psychological individual | IDENTITY = later is same person\n"
            " IMMORTALITY = survival of death | REBIRTH = renewed conditioned existence\n"
            " REINCARNATION = substantial soul re-embodied\n"
            " RESURRECTION = divine restoration of embodied person\n"
            " LIBERATION = release from bondage or rebirth",
        )
    text = text.replace(
        "| endless existence/release from existence",
        "| endless survival/release from rebirth",
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
    taxonomy = demote(
        extract_section(
            owner,
            "## 0A. SOUL, SELF, PERSON AND CONTINUITY-BEARER ⚠️",
            "---",
        )
    )
    arguments = demote(
        extract_section(
            owner,
            "### 1.1 Arguments for immortality and their limits",
            "---",
        )
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + firewall + "\n\n" + taxonomy,
            1,
        )
    if "#### 1.1 Arguments for immortality and their limits" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — IMMORTALITY OF THE SOUL AND PLATO'S ARGUMENTS",
            arguments,
        )
    source_control = (
        "### Local source and factual control\n\n"
        "- John Hick's local searchable *Philosophy of Religion*, print pp. 120–143 "
        "(PDF pp. 131–154), controls immortality, resurrection/replica identity and "
        "karma/reincarnation distinctions.\n"
        "- The local *Oxford Handbook of Philosophy of Religion*, print chapter "
        "beginning p. 366 (PDF pp. 378–391), controls person, identity and "
        "resurrection alternatives.\n"
        "- Chatterjee–Datta and C. D. Sharma are used for comparative Indian "
        "terminology; Paper I school owners retain doctrinal depth.\n"
        "- No paranormal report, brain finding or religious experience is presented "
        "as scientific proof of survival."
    )
    if "### Local source and factual control" not in text:
        text = insert_before(
            text,
            "### Source-complete coverage ledger and answer-worthiness labels",
            source_control,
        )
    text = re.sub(
        r"(?m)^✅ \*\*Fact:\*\* A fresh August 2026 search.*$\n"
        r"^⚠️ \*\*Inference:\*\* Current relevance.*$\n?",
        "⚠️ **Current-evidence policy:** no dated event or disputed survival report is "
        "used as evidence; the topic remains source- and argument-led.\n",
        text,
        count=1,
    )
    replacements = {
        "Christianity: resurrection       Jainism: jīva eternal → kaivalya": (
            "Christianity: resurrection       Jainism: jīva eternal → liberation/siddhahood"
        ),
        "- **Doctrine:** the soul, driven by **karma**, is repeatedly reborn until "
        "liberated; birth-conditions reflect past deeds. Shared by Vedānta, Nyāya, "
        "Jainism, and (transformed) Buddhism. ✅": (
            "- **Doctrine:** karmically conditioned continuity extends across lives "
            "until liberation. Vedānta, Nyāya and Jainism assign continuity to an "
            "enduring self or soul; Buddhism uses causal continuity without a "
            "permanent self. ✅"
        ),
        "- **Rebirth in Karma theory (2023 PYQ):** rebirth is the **mechanism by which "
        "karmic debts are discharged** — without rebirth, karma's justice (fruits "
        "maturing beyond one life) is impossible. ✅": (
            "- **Rebirth in Karma theory (2023 PYQ):** rebirth widens the temporal "
            "field in which karmic consequences can mature beyond one life. “Debt” "
            "is only an analogy and must not replace each school's causal account. ✅"
        ),
        "| **Jainism** | kaivalya/mokṣa | jīva sheds all karmic matter → infinite "
        "knowledge/bliss, rises to top of universe | perfected, omniscient soul |": (
            "| **Jainism** | liberation (*mokṣa/siddhahood*) | the soul (*jīva*) "
            "sheds karmic matter; perfect knowledge (*kevala-jñāna*) precedes final "
            "release | perfected, omniscient individual soul |"
        ),
        "| **Buddhism** | nirvāṇa | extinction of craving/dukkha; blowing-out | "
        "**no self** — cessation of the causal stream |": (
            "| **Buddhism** | liberation (*nirvāṇa*) | cessation of craving, "
            "ignorance and suffering; final nirvāṇa is not described as a self's "
            "survival or annihilation | no permanent self; causal continuity until "
            "liberation |"
        ),
        "| *Kevala/Siddhatva* | Jainism | Alone/perfected | Karmic matter | "
        "Perfected omniscient jīva | ✅ *Ananta-catuṣṭaya* |": (
            "| Liberation (*mokṣa/siddhahood*) | Jainism | Release/perfection | "
            "Karmic matter | Perfected omniscient individual soul (*jīva*) | "
            "✅ Four infinitudes (*ananta-catuṣṭaya*) |"
        ),
        "| *Nirvāṇa* | Buddhism | Blowing out | Craving, *dukkha* | "
        "❓ Not stated as a self | ⚠️ \"Object\" language misleads |": (
            "| Liberation (*nirvāṇa*) | Buddhism | Extinguishing craving | "
            "Craving, ignorance and suffering (*dukkha*) | ❓ Not stated as a self | "
            "⚠️ \"Object\" or annihilation language misleads |"
        ),
        "> ANALYSIS: Rebirth is the mechanism by which karmic debts are discharged.": (
            "> ANALYSIS: Rebirth is the trans-life field in which karmic consequences "
            "can mature; debt is only an analogy."
        ),
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = repair_session_contracts(text)
    text = transform_ascii(text)
    required = (
        "Exact printed ownership and cross-topic firewall",
        "SOUL, SELF, PERSON AND CONTINUITY-BEARER",
        "Arguments for immortality and their limits",
        "Local source and factual control",
        "STARTING CONCEPT",
        "REINCARNATION = substantial soul re-embodied",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Soul semantic transform missing: {missing}")
    return text


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    answer_lines = {
        "00": (
            "Define soul, self, person, immortality, rebirth, reincarnation, "
            "resurrection and liberation separately before testing necessity."
        ),
        "01": (
            "Plato's four arguments support different claims; simplicity, moral hope, "
            "desire and experience remain non-demonstrative survival arguments."
        ),
        "02": (
            "Bodily, psychological, soul and causal criteria face memory, dependence, "
            "replica and duplication pressures after death."
        ),
        "03": (
            "Buddhist rebirth preserves causal continuity without an immortal soul, "
            "showing that substance survival is sufficient but not necessary."
        ),
        "04": (
            "Liberation terms conceal incompatible selves, bondages, methods and final "
            "states; nirvana is not annihilation and Jain perfect knowledge is not Samkhya isolation."
        ),
        "05": (
            "Advaita removes ignorance of identity, theistic Vedanta perfects communion "
            "and Jainism purges karmic matter from an enduring individual soul."
        ),
        "06": (
            "Knowledge, action and devotion differ as direct means, qualifications or "
            "sequential aids according to whether liberation is produced or uncovered."
        ),
        "07": (
            "A strong answer identifies the continuity-bearer, mechanism, identity "
            "criterion, liberation-terminus and strongest evidence objection."
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
        "benchmark": "Soul/Rebirth/Liberation reviewed eight-panel ASCII master",
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
    if int(latest["generation"]) != 13:
        raise ValueError(
            f"Expected reviewed predecessor g13, found {latest['record_id']}."
        )
    base.DATE = DATE
    generation = int(latest["generation"]) + 1
    next_markdown = (
        base.repo(latest["markdown"]).parents[1]
        / f"g{generation}"
        / f"topic-04_Complete-Learning-Session_{DATE}.md"
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
        4,
        changed,
        text_transform=transform_markdown,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Soul, Immortality, "
            "Rebirth and Liberation: ownership, continuity/identity taxonomy, "
            "school precision, session contract and immutable dependent artifacts"
        ),
        baseline_score=97,
        repaired_score=100,
        issues_closed=[
            "exact ownership and cross-topic boundaries made explicit",
            "soul, self, person and continuity-bearer taxonomy promoted",
            "immortality argument families and evidence objections completed",
            "rebirth, reincarnation, Jain liberation and Buddhist nirvana corrected",
            "scientific-proof and cross-owner source controls added",
            "all ten refreshed session contracts and asset metadata repaired",
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
