"""Generate the immutable 2026-09-03 Proofs for God semantic successor only."""

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
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-02"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Proofs-for-God.md"
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
            "The three-question proof test asks whether an argument has validity, "
            "soundness and divine adequacy: whether it follows, starts truly and reaches "
            "a religiously adequate God."
        ),
        "how": (
            "Use validity, soundness and divine adequacy as the answer spine: classify "
            "the claimed force, reconstruct the premises, test the disputed premise and "
            "state what God-concept the conclusion actually establishes."
        ),
    },
    2: {
        "how": (
            "Build the ontological argument through Anselm and necessary existence, then "
            "use Gaunilo and Kant to test parody, predication and whether conceivability "
            "secures instantiation."
        ),
    },
    3: {
        "plain": (
            "Cosmological arguments reason from present dependence, causation, "
            "contingency or temporal beginning to an ultimate explanatory cause or ground."
        ),
        "how": (
            "Use essentially ordered series, contingency and sufficient reason to "
            "separate Aquinas, Leibniz and temporal-beginning arguments, then test "
            "infinite regress, brute fact and the first-cause identification."
        ),
    },
    4: {
        "plain": (
            "Teleological arguments infer intelligent direction from purposive order, "
            "biological adaptation or fine-tuned conditions, but these are distinct "
            "evidence-types."
        ),
    },
    5: {
        "plain": (
            "Moral arguments reason from duty, conscience, objective value or the highest "
            "good toward a moral ground or governor, but these routes claim different "
            "kinds of support."
        ),
    },
    6: {
        "plain": (
            "Nyaya divides cosmic explanation among eternal atoms, karmic deposits and "
            "an omniscient Lord who intelligently orders matter and allocates results."
        ),
        "technical": (
            "Udayana's proof cluster infers an eternal omniscient efficient cause from "
            "producedness, atomic combination, cosmic maintenance, linguistic order, "
            "scripture and karmic distribution."
        ),
        "how": (
            "Organise Nyaya's cosmic division of labour through Udayana, efficient "
            "causation, atom-order and karmic distribution, then assess the proof cluster "
            "as a cumulative case rather than one demonstration."
        ),
    },
    7: {
        "plain": (
            "Indian debates use God-language for both a creator-governor and revered or "
            "liberated beings, so denial of the first does not automatically deny the second."
        ),
        "how": (
            "Use creator God, deity, liberated being and worship-worthiness to distinguish "
            "cosmic efficient causation from achieved or revered godhood before classifying "
            "Indian non-theism."
        ),
    },
    8: {
        "technical": (
            "Jain non-creationism combines an eternal plurality of souls and non-soul "
            "substances with karmic causation, while divinity names achieved liberation "
            "rather than cosmic production."
        ),
    },
    10: {
        "plain": (
            "Mimamsa explains scriptural authority and ritual results through an "
            "authorless Veda and unseen ritual potency without requiring a divine author "
            "or karmic governor."
        ),
        "technical": (
            "The Mimamsa anti-theistic case combines authorless scripture, an intrinsic "
            "word-meaning relation and unseen ritual potency to render Nyaya's author, "
            "teacher and fruit-dispenser arguments redundant."
        ),
    },
}


CLOSURE_CONTROLS: dict[int, dict[str, str]] = {
    1: {
        "mechanism": (
            "Classify the argument as demonstrative, probabilistic or practical, then "
            "separate validity, premise truth and theological adequacy."
        ),
        "consequence": (
            "A valid inference may remain unsound, and a sound inference may still "
            "underdetermine the God of religion."
        ),
        "trap": (
            "Do not call every argument a mathematical proof or use one critic against a "
            "different claim of force."
        ),
    },
    2: {
        "mechanism": (
            "Anselm derives necessary existence from maximal greatness; Descartes treats "
            "existence as inseparable from supreme perfection."
        ),
        "consequence": (
            "Gaunilo tests whether the form proves too much, while Kant denies that "
            "existence adds a determining predicate."
        ),
        "trap": (
            "The modal repair shifts rather than removes the burden: coherent possibility "
            "must be defended independently."
        ),
    },
    3: {
        "mechanism": (
            "Aquinas terminates present derivative dependence, Leibniz seeks a sufficient "
            "reason for contingent totality, and the kalam argues from temporal beginning."
        ),
        "consequence": (
            "Infinite regress, brute fact and composition objections attack different "
            "premises and must not be treated as one objection."
        ),
        "trap": (
            "Do not turn Aquinas into a temporal first-event argument or identify a "
            "necessary ground with the personal God without further reasoning."
        ),
    },
    4: {
        "mechanism": (
            "Aquinas reasons from regular directedness, Paley from artifact-like "
            "adaptation, and fine-tuning arguments abductively compare rival explanations."
        ),
        "consequence": (
            "Darwin supplies a rival for biological adaptation, while multiverse and "
            "selection effects target fine-tuning rather than Paley's original analogy."
        ),
        "trap": (
            "Hume weakens the analogy and divine-attribute inference; he does not prove "
            "that no designer exists."
        ),
    },
    5: {
        "mechanism": (
            "Lawgiver, objective-value and Kantian highest-good arguments move from "
            "different moral data to different conclusions."
        ),
        "consequence": (
            "Kant preserves autonomous obligation and postulates God only for the highest "
            "good, whereas lawgiver arguments make God the source or judge of duty."
        ),
        "trap": (
            "Do not present Kant's postulate as theoretical knowledge or let the "
            "Euthyphro dilemma target the wrong moral argument."
        ),
    },
    6: {
        "mechanism": (
            "Udayana combines producedness, atomic conjunction, maintenance, language, "
            "scripture and karmic allocation into a cumulative inference to an omniscient "
            "efficient cause."
        ),
        "consequence": (
            "God orders eternal atoms and allocates karmic fruits; God is not Nyaya's "
            "material cause."
        ),
        "trap": (
            "Do not recite an unexplained Sanskrit list; state each proof's premise and "
            "flag variable glosses."
        ),
    },
    7: {
        "mechanism": (
            "Indian anti-creator schools relocate causal, scriptural and moral-order work "
            "to nature, dependent arising, karma or ritual potency."
        ),
        "consequence": (
            "Rejecting a creator does not erase deities, liberated beings or religious "
            "practice."
        ),
        "trap": (
            "Do not flatten Jainism, Buddhism, Samkhya, Mimamsa and Carvaka into one "
            "generic atheism."
        ),
    },
    8: {
        "mechanism": (
            "Jainism treats the cosmos and substances as beginningless and karmically "
            "ordered while defining godhood as achieved liberation."
        ),
        "consequence": (
            "Its motive, regress, material, moral and redundancy arguments target a "
            "creator without denying perfected souls."
        ),
        "trap": (
            "Do not invent Jain creator-proofs or equate a Tirthankara with a creator or "
            "with every liberated soul."
        ),
    },
    9: {
        "mechanism": (
            "Dependent origination and the permanence-production dilemma challenge the "
            "need and coherence of an unchanging creator."
        ),
        "consequence": (
            "Buddhism rejects a creator while allowing impermanent deities within the "
            "conditioned order."
        ),
        "trap": (
            "Silence about speculative questions is not by itself a refutation; state the "
            "causal argument."
        ),
    },
    10: {
        "mechanism": (
            "Authorless scripture, intrinsic word-meaning relations and unseen ritual "
            "potency distribute explanatory work without a divine author or dispenser."
        ),
        "consequence": (
            "Nyaya must show why linguistic authority and karmic fruition require "
            "conscious administration."
        ),
        "trap": (
            "Do not call unseen ritual potency a deity or treat Mimamsa's Vedic orthodoxy "
            "as creator-theism."
        ),
    },
}


def transform_ascii(text: str) -> str:
    if " BURDEN: premise -> inference -> theological identification" not in text:
        text = text.replace(
            " CONTROL: proofs may be deductive, abductive or cumulative;\n"
            " never judge all by the standard of a single demonstrative syllogism.",
            " CONTROL: proofs may be deductive, abductive or cumulative;\n"
            " BURDEN: premise -> inference -> theological identification\n"
            " never judge all by the standard of a single demonstrative syllogism.",
        )
    if " conscience/law" not in text.casefold():
        text = text.replace(
            "KANT: morality does not theoretically prove God\n",
            "CONSCIENCE/LAW: obligation -> personal lawgiver (contested)\n"
            " OBJECTIVE VALUE: moral realism -> transcendent ground (abductive)\n"
            " KANT: morality does not theoretically prove God\n",
        )
    if " SĀṂKHYA: unconscious nature" not in text:
        text = text.replace(
            " MĪMĀṂSĀ: Veda is authorless; dharma/apūrva explains ritual fruit without divine author\n",
            " MĪMĀṂSĀ: Veda is authorless; dharma/apūrva explains ritual fruit without divine author\n"
            " SĀṂKHYA: unconscious nature (prakṛti) evolves without a creator\n",
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

        if number == 6 and "cosmic division of labour" not in body[
            : body.find("**How to use them:**")
        ].casefold():
            body = body.replace(
                "- **cumulative case**\n\n**How to use them:**",
                "- **cumulative case**\n"
                "- **cosmic division of labour**\n\n"
                "**How to use them:**",
                1,
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

        roles = CLOSURE_CONTROLS[number]
        opening_match = re.search(
            r"(?ms)^#### ANSWER-GRABBING OPENING.*?\n+\s*>\s*(.+?)\s*$",
            body,
        )
        if not opening_match:
            raise ValueError(f"Session {number} has no answer opening.")
        opening = opening_match.group(1).strip()
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
            "## 0A. PROOF-FORCE, BURDEN AND EXPLANATORY TERMINATION ⚠️",
            "---",
        )
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + firewall + "\n\n" + method,
            1,
        )

    source_control = (
        "### Local source and factual control\n\n"
        "- John Hick's local searchable PDF, print pp. 15–29 (PDF pp. 26–40), "
        "controls the Western argument taxonomy and standard criticisms.\n"
        "- The local *Oxford Handbook of Philosophy of Religion* controls the "
        "ontological, cosmological/design, sufficient-reason and moral-argument "
        "distinctions.\n"
        "- Chatterjee–Datta's local searchable PDF, PDF pp. 259–266, controls "
        "Nyaya's causal, unseen-merit, scriptural-authority and testimony arguments.\n"
        "- No contemporary scientific result is used as proof; fine-tuning, multiverse "
        "and anthropic reasoning remain contested model-dependent arguments."
    )
    if "### Local source and factual control" not in text:
        text = insert_before(
            text,
            "### Source-complete coverage ledger and learning labels",
            source_control,
        )

    samkhya_bridge = (
        "##### Sāṃkhya anti-creator bridge\n\n"
        "✅ Classical Sāṃkhya treats primordial nature (*prakṛti*) and its transformation "
        "in the presence of conscious persons as sufficient for cosmic evolution; a "
        "creator is unproved and unnecessary. ⚠️ Nyāya replies that unconscious nature "
        "does not by itself explain purposive coordination, while Sāṃkhya answers that "
        "goal-directed evolution need not be the product of a willing designer."
    )
    if "##### Sāṃkhya anti-creator bridge" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — TWO COMPLETELY DIFFERENT SENSES OF \"GOD\" "
            "IN THE INDIAN DEBATE",
            samkhya_bridge,
        )

    text = re.sub(
        r"(?m)^📰 CA Found:.*$",
        "📰 CA Found: None used as evidence. Contemporary cosmology is retained only "
        "as a contested objection-space, never as proof.",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^📰 As noted, the 2025 review and 2026 paper.*$",
        "⚠️ Contemporary fine-tuning discussion is model-dependent and supplies no "
        "settled scientific premise for theism.",
        text,
        count=1,
    )
    text = repair_session_contracts(text)
    text = transform_ascii(text)

    required = (
        "Exact printed ownership and cross-topic firewall",
        "PROOF-FORCE, BURDEN AND EXPLANATORY TERMINATION",
        "Leibniz and the Principle of Sufficient Reason",
        "The first form of the moral argument",
        "Sāṃkhya anti-creator bridge",
        "Local source and factual control",
        "STARTING CONCEPT",
        "BURDEN: premise -> inference -> theological identification",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Proofs for God semantic transform missing: {missing}")
    return text


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    answer_lines = {
        "00": (
            "Classify each proof's force, then test premise, inference and theological "
            "identification separately; 'proof' does not guarantee demonstration."
        ),
        "01": (
            "Anselm promises necessary existence, but Gaunilo and Kant shift the burden "
            "to coherent possibility and the legitimacy of existential predication."
        ),
        "02": (
            "Aquinas explains present dependence, Leibniz contingent totality and the "
            "kalam a temporal beginning; each faces a different regress or brute-fact pressure."
        ),
        "03": (
            "Hume defeats a demonstrative design inference and its rich divine attributes; "
            "teleology survives, if at all, as contested probabilistic explanation."
        ),
        "04": (
            "Lawgiver, objective-value and Kantian highest-good arguments begin from "
            "different moral data and do not establish the same conclusion."
        ),
        "05": (
            "Udayana's cumulative proof cluster infers an omniscient efficient cause that "
            "orders eternal atoms and karmic fruits rather than creating matter."
        ),
        "06": (
            "Jain, Buddhist, Mimamsa, Samkhya and Carvaka critiques relocate explanatory "
            "work differently and must not be flattened into one atheistic objection."
        ),
        "07": (
            "No single proof compels; a cumulative case can raise probability only if its "
            "modal, causal, analogical and moral premises retain independent force."
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
        "benchmark": "Proofs-for-God reviewed eight-panel ASCII master",
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
        / f"topic-02_Complete-Learning-Session_{DATE}.md"
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
        2,
        changed,
        text_transform=transform_markdown,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Proofs for the Existence "
            "of God: ownership, proof-force, Western/Indian taxonomy, source "
            "control, session contract and immutable dependent artifacts"
        ),
        baseline_score=97,
        repaired_score=100,
        issues_closed=[
            "exact proof-family ownership and cross-topic boundaries made explicit",
            "validity, soundness, adequacy, burden and explanatory termination unified",
            "Aquinas, Leibniz and temporal-beginning cosmological forms separated",
            "lawgiver, objective-value and Kantian moral routes separated",
            "Samkhya anti-creator bridge and scientific-claim limits added",
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
