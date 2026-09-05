"""Generate the immutable 2026-09-03 Religion without God successor only."""

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
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-07"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Religion-without-God.md"
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
            "Religion without God asks whether a personal creator is necessary for "
            "religion or whether sacred order, disciplined practice, community and "
            "transformation can suffice."
        ),
        "technical": (
            "The necessity claim is tested by distinguishing theism, non-theism, atheism "
            "and agnosticism and by applying substantive, functional and multidimensional "
            "definitions."
        ),
        "opening": (
            "A personal creator is sufficient for many religions but not necessary for "
            "religion as such, provided a non-theistic tradition retains sacred "
            "orientation, disciplined practice and transformation."
        ),
        "how": (
            "Use religion, God, non-theism and sacred order to test whether a personal "
            "creator is necessary, then compare soteriology and practice with atheistic denial."
        ),
    },
    2: {
        "how": (
            "Compare substantive definition and functional definition through Ninian "
            "Smart, ultimate concern, ritual and community, then police both against "
            "exclusion and over-breadth."
        ),
    },
    3: {
        "plain": (
            "Buddhism is non-theistic because a creator is absent from its diagnosis and "
            "path, while doctrine, ethics, meditation, community and liberation remain "
            "fully developed."
        ),
        "technical": (
            "Dependent origination and karma explain conditioned arising; the Four Noble "
            "Truths, path, ritual community and nirvana supply a complete soteriological "
            "structure without creator-belief."
        ),
        "how": (
            "Use Buddhism, dependent origination, Four Noble Truths and non-theism to "
            "show how nirvana and ritual community organise religion without a creator "
            "while allowing non-creator deities."
        ),
    },
    4: {
        "how": (
            "Compare Feuerbach, Marx, Freud and Nietzsche on projection and the genealogy "
            "of God-belief, then test whether post-theistic meaning preserves religious functions."
        ),
    },
    5: {
        "how": (
            "Distinguish agnosticism, atheism and suspension of judgment, then ask how "
            "the unknown permits practical religiosity or non-theistic commitment without assent to God."
        ),
    },
    6: {
        "how": (
            "Use ritual, meaning, community and liberation to compare Mimamsa and "
            "religious naturalism, then identify which creator-dependent goods the "
            "theistic critic says are lost."
        ),
    },
    7: {
        "how": (
            "State the theistic objection through object of worship and ultimate meaning, "
            "test functional sufficiency against non-theistic religion, and finish with a "
            "qualified verdict separating religion from theism."
        ),
    },
}


CLOSURE_CONTROLS: dict[int, dict[str, str]] = {
    1: {
        "mechanism": (
            "Test whether God is necessary by comparing theism, non-theism, atheism and "
            "a disciplined sacred/soteriological cluster."
        ),
        "consequence": (
            "Creator-belief is sufficient for many religions but actual non-theistic "
            "traditions challenge its necessity."
        ),
        "trap": (
            "Do not equate non-theism with denial of every deity, sacred being or devotional practice."
        ),
    },
    2: {
        "mechanism": (
            "Substantive definitions identify religion's object, functional definitions "
            "its role and multidimensional definitions a cluster of doctrine, practice and community."
        ),
        "consequence": (
            "A creator definition excludes Buddhism by stipulation, while an unrestricted "
            "functional definition can make nationalism or any commitment religious."
        ),
        "trap": (
            "Do not adopt a definition too narrow for established traditions or too broad "
            "to distinguish religion from ideology."
        ),
    },
    3: {
        "mechanism": (
            "Dependent origination and karma explain arising, while Four Noble Truths, "
            "path, community and nirvana organise a creator-independent soteriology."
        ),
        "consequence": (
            "Buddhist gods may be impermanent cosmological beings without becoming "
            "creators or final saviours."
        ),
        "trap": (
            "Do not reduce Buddhism to silence about God or call Dharma and nirvana "
            "one-for-one substitutes for a personal deity."
        ),
    },
    4: {
        "mechanism": (
            "Feuerbach, Marx and Freud explain God-belief through projection or social "
            "function, while Nietzsche diagnoses collapse of a value horizon."
        ),
        "consequence": (
            "Explaining or criticising theism does not by itself establish a viable "
            "post-theistic religion."
        ),
        "trap": (
            "Do not treat Marx or Nietzsche as founders of a religion of humanity or steal "
            "the religion-and-morality Nietzsche PYQ."
        ),
    },
    5: {
        "mechanism": (
            "Agnosticism suspends judgment, atheism denies, non-theism makes God "
            "non-central and practical religiosity organises life without assent."
        ),
        "consequence": (
            "Epistemic uncertainty about God does not alone decide whether ritual, ethics "
            "or contemplative participation remains possible."
        ),
        "trap": (
            "Do not use agnostic, atheistic, non-theistic and anti-theistic as synonyms."
        ),
    },
    6: {
        "mechanism": (
            "Ritual, meaning, community and liberation can be organised through authorless "
            "scripture, karmic law, nature, narrative or shared discipline."
        ),
        "consequence": (
            "Petition, grace and providence require personal agency more directly than "
            "ritual, worship, morality or liberation."
        ),
        "trap": (
            "Do not assume functional similarity makes an impersonal ultimate ontologically identical to God."
        ),
    },
    7: {
        "mechanism": (
            "State the strongest theistic worship/grace objection, answer with concrete "
            "non-theistic traditions and test definition breadth."
        ),
        "consequence": (
            "Religion without God is coherent where sacred orientation, disciplined "
            "practice, community and transformation survive."
        ),
        "trap": (
            "Do not conclude that every philosophy, civil ritual or secular spirituality "
            "is therefore a religion."
        ),
    },
}


def transform_ascii(text: str) -> str:
    if " SUFFICIENT CLUSTER:" not in text:
        text = text.replace(
            " worldview | transformation | liberation\n",
            " worldview | transformation | liberation\n"
            " SUFFICIENT CLUSTER: sacred order + disciplined practice + community + transformation\n",
        )
    text = text.replace(
        " Buddha rejects speculative questions when they do not conduce to cessation of duḥkha",
        " undeclared questions do not exhaust the case; creator-belief is non-central to the path",
    )
    text = text.replace(
        " personal worship and providence preserved? often NO",
        " petition, grace and providence preserved? normally NO",
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
    criteria = demote(
        extract_section(
            owner,
            "### 1.1 Necessary, sufficient and over-broad criteria",
            "---",
        )
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + firewall + "\n\n" + criteria,
            1,
        )
    source_control = (
        "### Local source and factual control\n\n"
        "- Local John Hick, *Philosophy of Religion*, PDF p. 14, supports "
        "comparative definitions that include Theravada Buddhism without creator worship.\n"
        "- The local *Oxford Handbook of Philosophy of Religion*, print pp. 59–79 "
        "(PDF pp. 71–90), controls theistic/non-theistic concept discrimination.\n"
        "- Chatterjee–Datta, especially PDF pp. 37–39 and 144–146, and C. D. "
        "Sharma control Indian creator-denial and religion qualifications.\n"
        "- No contemporary sociology or popularity claim is used to establish the "
        "definition of religion."
    )
    if "### Local source and factual control" not in text:
        text = insert_before(
            text,
            "### Source-complete coverage ledger and answer-worthiness labels",
            source_control,
        )
    text = re.sub(
        r"(?m)^✅ \*\*Fact:\*\* Recent 2025–2026 scholarship.*$\n"
        r"^⚠️ \*\*Inference:\*\* This strengthens.*$\n?",
        "⚠️ **Current-evidence policy:** modern naturalism is used only as a "
        "conceptual boundary case; Indian traditions remain the primary evidence.\n",
        text,
        count=1,
    )
    replacements = {
        "A religion can offer a path, ethics and liberation without a creator deity — "
        "Buddhism is the proof.": (
            "A religion can offer a path, ethics and liberation without a creator deity; "
            "Buddhism is a strong counterexample to creator-necessity."
        ),
        "(Later Mahāyāna develops quasi-devotional Buddha/Bodhisattva figures, but "
        "the core is non-theistic.) ⚠️ Verdict: Buddhism decisively shows religion "
        "does not require God. ✅.": (
            "Buddhist doctrine, path, community and liberation form a non-creator "
            "religion while later devotional traditions show that non-theism need not "
            "exclude sacred beings."
        ),
        "- **Non-theistic:** the Buddha was **silent/agnostic on a creator God** "
        "(the *avyākata* — unanswered questions); the world runs by "
        "**pratītyasamutpāda** (dependent origination) and **karma**, needing no creator. ✅": (
            "- **Non-theistic:** early Buddhism does not make a creator part of its "
            "diagnosis or path. Dependent origination and karma explain conditioned "
            "arising, while gods remain impermanent beings rather than creators. ✅"
        ),
        "- **What replaces God:** the **Dharma** (law/teaching) and the goal of "
        "**nirvāṇa** — an impersonal ultimate. (Later Mahāyāna develops "
        "quasi-devotional Buddha/Bodhisattva figures, but the core is non-theistic.) ⚠️": (
            "- **What orients the religion:** Dharma, community and liberation organise "
            "doctrine and practice without functioning as one-for-one substitutes for a "
            "personal creator. Later devotion confirms that non-theism is not devotion-free. ⚠️"
        ),
        "- **Verdict:** Buddhism decisively shows **religion does not require God.** ✅": (
            "- **Verdict:** Buddhism is a strong counterexample to creator-necessity "
            "under a multidimensional rather than stipulative theistic definition. ✅"
        ),
        "Mīmāṃsā (ritual-exegesis school) is the cleanest disproof of God's necessity": (
            "Mīmāṃsā (ritual-exegesis school) is a strong functional counterexample "
            "to God's necessity"
        ),
        "Pūrva-Mīmāṃsā is the fullest case of a **fully religious system with no God "
        "doing any work**.": (
            "Classical Pūrva-Mīmāṃsā is a strong case of a **ritual and scriptural "
            "religious order in which no creator performs the main explanatory work**."
        ),
        "Mīmāṃsā is the cleanest disproof of the claim that religion requires God.": (
            "Mīmāṃsā is a strong counterexample to creator-necessity under ritual, "
            "functional or multidimensional definitions."
        ),
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = repair_session_contracts(text)
    text = transform_ascii(text)
    required = (
        "Exact printed ownership and cross-topic firewall",
        "Necessary, sufficient and over-broad criteria",
        "Which religious functions require a deity",
        "Local source and factual control",
        "STARTING CONCEPT",
        "SUFFICIENT CLUSTER",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Religion without God transform missing: {missing}")
    return text


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    answer_lines = {
        "00": (
            "Creator-belief is sufficient for many religions but not necessary where a "
            "sacred order, disciplined practice, community and transformation remain."
        ),
        "01": (
            "Atheism denies, agnosticism suspends, non-theism makes God non-central and "
            "anti-theism adds a negative evaluation; these positions must not be merged."
        ),
        "02": (
            "Buddhism is creator-independent rather than devotion-free: dependent "
            "origination, path, community and nirvana organise the religious life."
        ),
        "03": (
            "Jainism, Mimamsa and Samkhya relocate creation, authority, efficacy and "
            "liberation differently and are not one Indian atheism."
        ),
        "04": (
            "Carvaka is the limiting case: rejecting God plus sacred order, afterlife and "
            "liberation shows why philosophy without God is easier than religion without God."
        ),
        "05": (
            "Nietzsche diagnoses a collapsed value horizon; post-theistic value creation "
            "does not by itself supply ritual, community or soteriology."
        ),
        "06": (
            "Naturalism and fictionalism retain some religious functions, but sincerity, "
            "truth, transcendence and category over-breadth remain live objections."
        ),
        "07": (
            "Religion without God is coherent, but petition, grace and providence remain "
            "specifically deity-dependent goods whose loss must be conceded."
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
        "benchmark": "Religion-without-God reviewed eight-panel ASCII master",
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
        / f"topic-07_Complete-Learning-Session_{DATE}.md"
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
        7,
        changed,
        text_transform=transform_markdown,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Religion without God: "
            "ownership, definition cluster, deity-function tests, Indian precision, "
            "session contract and immutable dependent artifacts"
        ),
        baseline_score=96,
        repaired_score=100,
        issues_closed=[
            "exact ownership and cross-topic boundaries made explicit",
            "necessary, sufficient and over-broad religion criteria unified",
            "deity-dependent and deity-independent religious functions separated",
            "Buddhist creator, deity and soteriology claims corrected",
            "Mimamsa, naturalism and civil-religion boundary claims qualified",
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
