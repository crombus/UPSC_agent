"""Generate the immutable 2026-09-03 Reason/Revelation/Faith successor only."""

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
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-05"
OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Reason-Revelation-Faith.md"
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
            "Use natural theology, evidentialism, coherence testing and regulative "
            "reason to build rational justification, then distinguish supra-rational "
            "commitment from demonstrative knowledge and irrational exemption."
        ),
    },
    3: {
        "plain": (
            "Revelation is an alleged divine disclosure communicated as truth-content, "
            "event, personal presence, scripture or universal manifestation."
        ),
        "technical": (
            "Revelation models differ by scope—general or special—and by content—"
            "propositional truth or non-propositional self-disclosure—while authority "
            "depends on defeasible authentication."
        ),
        "how": (
            "Classify revelation as general or special and as propositional or personal "
            "disclosure, then test scripture and authority through authentication, "
            "testimony, coherence and moral credibility."
        ),
    },
    4: {
        "plain": (
            "Faith combines cognitive assent with trust, commitment, hope and a practical "
            "way of life under conditions that do not compel belief."
        ),
        "technical": (
            "Faith differs from bare belief-that by adding belief-in, volitional "
            "entrusting and fidelity, while remaining answerable to evidence, coherence "
            "and defeaters."
        ),
        "how": (
            "Use faith, belief, trust and commitment as distinct stages, then show how "
            "objective uncertainty creates evidential risk without making responsible "
            "faith contrary to reason."
        ),
    },
    5: {
        "plain": (
            "Reason–faith models range from rationalist priority and fideist priority to "
            "faith seeking understanding and two-source compatibility."
        ),
        "technical": (
            "The models differ over whether reason constitutes, regulates or merely "
            "clarifies faith and whether commitment under uncertainty remains "
            "epistemically responsible."
        ),
        "opening": (
            "The strongest compatibility model makes reason regulative without making it "
            "constitutive: faith may exceed proof while remaining open to coherence and "
            "evidential criticism."
        ),
        "how": (
            "Compare compatibilism, fideism, rationalism and faith seeking understanding, "
            "then evaluate the leap through epistemic responsibility rather than "
            "treating Kierkegaard as licensing arbitrary belief."
        ),
    },
    7: {
        "how": (
            "Use means of valid knowledge, verbal testimony, Vedic authorlessness and "
            "trustworthiness to compare reasoned faith and tradition, asking how "
            "testimony's competence, scope and interpretation are tested."
        ),
    },
}


CLOSURE_CONTROLS: dict[int, dict[str, str]] = {
    1: {
        "mechanism": (
            "Reason tests warrant, revelation claims disclosure and faith receives the "
            "claim through trust and committed practice."
        ),
        "consequence": (
            "The three concepts can cooperate without being reducible to one source or "
            "one standard of evidence."
        ),
        "trap": (
            "Do not define faith as evidence-free belief, revelation as intense feeling "
            "or reason as deduction alone."
        ),
    },
    2: {
        "mechanism": (
            "Natural theology constructs arguments, evidentialism tests support and "
            "regulative reason disciplines coherence and interpretation."
        ),
        "consequence": (
            "Reason may constrain religious belief without generating every revealed "
            "content or eliminating supra-rational commitment."
        ),
        "trap": (
            "Do not confuse regulative reason with a constitutive demand that faith accept "
            "only independently provable propositions."
        ),
    },
    3: {
        "mechanism": (
            "Classify disclosure by scope—general or special—and content—propositional or "
            "personal/event—before applying authentication tests."
        ),
        "consequence": (
            "Coherence, testimony, tradition, moral fruit and experience can converge "
            "without independently proving divine authorship."
        ),
        "trap": (
            "Do not authenticate scripture by its own authority alone or ignore competing "
            "revelations and interpretation."
        ),
    },
    4: {
        "mechanism": (
            "Faith joins belief-that to belief-in through trust, hope, commitment and a "
            "practical way of life under objective uncertainty."
        ),
        "consequence": (
            "Faith can exceed conclusive evidence while remaining defeasible and "
            "answerable to epistemic risk."
        ),
        "trap": (
            "Do not equate strong commitment with voluntary power to believe any claim at will."
        ),
    },
    5: {
        "mechanism": (
            "Rationalism, fideism, faith seeking understanding and two-source harmony "
            "assign reason different constitutive or regulative roles."
        ),
        "consequence": (
            "Aquinas protects harmony, while Kierkegaard insists that objective proof "
            "cannot replace existential appropriation."
        ),
        "trap": (
            "Do not flatten Kierkegaard into irrationalism or use the later credo-quia-"
            "absurdum slogan as his or Tertullian's verified quotation."
        ),
    },
    6: {
        "mechanism": (
            "Aquinas distinguishes rational preambles from revealed mysteries; "
            "Kierkegaard, Anselm and Clifford locate commitment and evidence differently."
        ),
        "consequence": (
            "Intellectual assent can be rationally supported without being demonstrative, "
            "while passionate inwardness remains responsible only if not immune to criticism."
        ),
        "trap": (
            "Do not merge Aquinas' will-guided assent with Kierkegaardian objective "
            "uncertainty or Clifford's proof-demand."
        ),
    },
    7: {
        "mechanism": (
            "Indian epistemology compares verbal testimony, authorless scripture, "
            "intrinsic/extrinsic validity and reasoned interpretation as means of knowledge."
        ),
        "consequence": (
            "Scriptural authority need not imply a divine speaker, and testimony remains "
            "school-relative in source and validation."
        ),
        "trap": (
            "Do not translate verbal testimony as blind faith or treat Vedic "
            "authorlessness as propositional revelation from a creator."
        ),
    },
}


def transform_ascii(text: str) -> str:
    text = text.replace(
        "REASON: publicly assessable inference, coherence and evidence",
        "REASON: deductive/abductive inquiry, coherence, interpretation and criticism",
    )
    if " GREAT PUMPKIN:" not in text:
        text = text.replace(
            " REFORMED EPISTEMOLOGY: belief in God may be properly basic unless defeated\n",
            " REFORMED EPISTEMOLOGY: belief in God may be properly basic unless defeated\n"
            " GREAT PUMPKIN: basicality still needs proper grounding and defeater control\n"
            " CRITICAL RATIONALISM: commitment remains corrigible under criticism\n",
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
        if number == 3 and "- **general revelation**" not in body.casefold():
            body = body.replace(
                "- **authentication**\n\n**How to use them:**",
                "- **authentication**\n"
                "- **general revelation**\n"
                "- **special revelation**\n\n"
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
    concept_grid = demote(
        extract_section(
            owner,
            "## 0A. THREE CONCEPTS, THREE EPISTEMIC JOBS ⚠️",
            "---",
        )
    )
    authority = demote(
        extract_section(
            owner,
            "### Authority, tradition and authentication",
            "---",
        )
    )
    pragmatic = demote(
        extract_section(
            owner,
            "### Pragmatic and permissive proposals — bounded use",
            "---",
        )
    )
    if "### Exact printed ownership and cross-topic firewall" not in text:
        text = text.replace(
            "## BASIC LEARNING SESSION",
            "## BASIC LEARNING SESSION\n\n" + firewall + "\n\n" + concept_grid,
            1,
        )
    if "#### Authority, tradition and authentication" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — REVELATION, AUTHORITY AND DISCLOSURE",
            authority,
        )
    if "#### Pragmatic and permissive proposals — bounded use" not in text:
        text = insert_before(
            text,
            "#### CLOSING RECALL FLOW — COMPATIBILISM, FIDEISM AND RIVAL STANCES",
            pragmatic,
        )
    source_control = (
        "### Local source and factual control\n\n"
        "- John Hick's local searchable *Philosophy of Religion*, print pp. 56–64 "
        "(PDF pp. 67–75), controls propositional revelation, voluntarist faith and "
        "ultimate concern.\n"
        "- The local *Oxford Handbook of Philosophy of Religion* controls religious "
        "epistemology, miracles and faith/revelation from print pp. 245, 304 and 323.\n"
        "- Chatterjee–Datta's local PDF, especially pp. 245–249 and 394–396, controls "
        "Nyaya testimony and Mimamsa intrinsic validity.\n"
        "- No miracle report, scientific claim or transformative effect is treated as "
        "self-authenticating proof."
    )
    if "### Local source and factual control" not in text:
        text = insert_before(
            text,
            "### Source-complete coverage ledger and answer-worthiness labels",
            source_control,
        )
    text = re.sub(
        r"(?m)^✅ \*\*Fact:\*\* Religion News Service.*$\n"
        r"^⚠️ \*\*Inference:\*\* The episode.*$\n?",
        "⚠️ **Current-evidence policy:** the science-and-technology PYQ is answered "
        "through durable relation-models and normative analysis, not a decorative news item.\n",
        text,
        count=1,
    )
    text = text.replace(
        "- **Kierkegaard — faith as the LEAP:** faith is a **passionate, subjective "
        "commitment** in \"objective uncertainty\"; the **leap of faith** transcends "
        "reason (Abraham's \"teleological suspension of the ethical\"). **Fideism** — "
        "faith needs no rational proof and may even require its \"crucifixion\". ✅",
        "- **Kierkegaard — faith as committed appropriation:** faith is a passionate, "
        "subjective commitment under objective uncertainty. Kierkegaard denies that an "
        "objective system can replace existential decision; he does not license "
        "contradiction, irresponsibility or arbitrary evidence-free belief. ✅",
    )
    text = text.replace(
        "| Fideism | faith over/against reason | Kierkegaard, Tertullian | the leap; "
        "\"credo quia absurdum\" |",
        "| Faith-priority / fideism | faith cannot be generated by proof | "
        "Kierkegaard; later extreme fideist slogans | commitment under uncertainty; "
        "reason cannot replace appropriation |",
    )
    text = repair_session_contracts(text)
    text = transform_ascii(text)
    required = (
        "Exact printed ownership and cross-topic firewall",
        "THREE CONCEPTS, THREE EPISTEMIC JOBS",
        "Authority, tradition and authentication",
        "Pragmatic and permissive proposals",
        "Local source and factual control",
        "STARTING CONCEPT",
        "GREAT PUMPKIN",
    )
    missing = [term for term in required if term.casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"Reason/Revelation/Faith transform missing: {missing}")
    return text


def transform_graphical(spec: dict[str, Any]) -> dict[str, Any]:
    answer_lines = {
        "00": (
            "Reason discovers and regulates, revelation claims disclosure, and faith "
            "adds trust, commitment and a way of life without becoming evidence-free belief."
        ),
        "01": (
            "The live question is whether reason constitutes, regulates or interprets "
            "faith and which religious claim remains answerable to which evidence."
        ),
        "02": (
            "Revelation must be classified by scope and content, then tested through "
            "testimony, coherence, tradition, moral fruit and rival-disclosure pressure."
        ),
        "03": (
            "Aquinas lets reason establish preambles and revelation disclose mysteries "
            "that exceed but cannot contradict rational truth."
        ),
        "04": (
            "Kierkegaard makes faith committed appropriation under objective uncertainty, "
            "not arbitrary immunity from evidence or ethical responsibility."
        ),
        "05": (
            "Miracle and scientific claims remain defeasible evidence; unusual events do "
            "not authenticate one revelation without interpretation and testimony."
        ),
        "06": (
            "Religious belief may be inferential, properly basic or testimony-based, but "
            "Great-Pumpkin, diversity and defeater objections constrain every model."
        ),
        "07": (
            "Responsible faith exceeds conclusive proof while remaining open to reasoned "
            "criticism, interpretation, moral testing and revision."
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
        "benchmark": "Reason/Revelation/Faith reviewed eight-panel ASCII master",
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
        / f"topic-05_Complete-Learning-Session_{DATE}.md"
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
        5,
        changed,
        text_transform=transform_markdown,
        graphical_transform=transform_graphical,
        repair_scope=(
            "ten-gate semantic-completeness repair for Reason, Revelation and Faith: "
            "ownership, epistemic taxonomy, revelation authentication, faith models, "
            "session contract and immutable dependent artifacts"
        ),
        baseline_score=96,
        repaired_score=100,
        issues_closed=[
            "exact ownership and cross-topic boundaries made explicit",
            "reason, revelation and faith epistemic jobs unified",
            "general/special and propositional/non-propositional revelation separated",
            "authority, tradition, circularity and authentication controls completed",
            "Kierkegaard, Pascal, James and critical-rational limits repaired",
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
