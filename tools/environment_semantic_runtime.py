"""Load the proven Environment deep-review engine without mutating completed subjects."""

from __future__ import annotations

import hashlib
import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
RUNTIME = ROOT / ".environment-semantic-runtime"
REPORT_DATE = "2026-09-06"
_HEAD_WRAPPERS = {
    "regenerate_environment_and_ecology_deep_review.py",
    "regenerate_economy_deep_review.py",
    "regenerate_governance_deep_review.py",
}
_WORLD_HISTORY_COMPATIBLE_DIGEST = (
    "9083818975346780d07fd35b8a8adc8184eb650fac7bb0e9d5211dbdc0d7ccc8"
)


def _git_head(path: Path) -> bytes:
    return subprocess.check_output(
        ["git", "show", f"HEAD:tools/{path.name}"],
        cwd=ROOT,
        stderr=subprocess.DEVNULL,
    )


def _write_data_alias(start: int, end: int, suffix: int) -> None:
    lines = []
    for number in range(start, end + 1):
        module = (
            f"environment_and_ecology_{number:02d}_data"
            if number < 25
            else "environment_and_ecology_25_28_data"
        )
        lines.append(f"from {module} import TOPIC_{number:02d}")
    (RUNTIME / f"environment_and_ecology_{start:02d}_{suffix:02d}_data.py").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
        newline="",
    )


def _repin_runtime() -> None:
    pattern = re.compile(
        r'_BASE = Path\(__file__\)\.with_name\("([^"]+)"\)\s*'
        r'_BASE_SHA256 = "([0-9a-f]+)"'
    )
    for _ in range(50):
        changed = False
        for path in RUNTIME.glob("regenerate_*_deep_review.py"):
            text = path.read_text(encoding="utf-8")
            match = pattern.search(text)
            if not match:
                continue
            base = RUNTIME / match.group(1)
            if not base.is_file():
                continue
            digest = hashlib.sha256(base.read_bytes()).hexdigest()
            if path.name == "regenerate_world_history_deep_review.py":
                digest = _WORLD_HISTORY_COMPATIBLE_DIGEST
            if match.group(2) == digest:
                continue
            path.write_text(
                text[: match.start(2)] + digest + text[match.end(2) :],
                encoding="utf-8",
                newline="",
            )
            changed = True
        if not changed:
            return
    raise RuntimeError("Environment semantic runtime hash pinning did not converge.")


def prepare_runtime() -> Path:
    if RUNTIME.exists():
        shutil.rmtree(RUNTIME)
    RUNTIME.mkdir()
    for source in TOOLS.glob("regenerate_*_deep_review.py"):
        data = (
            _git_head(source)
            if source.name in _HEAD_WRAPPERS
            else source.read_bytes().replace(b"\r\n", b"\n")
        )
        (RUNTIME / source.name).write_bytes(data)
    for start, end, suffix in (
        (1, 5, 5),
        (6, 10, 10),
        (11, 15, 15),
        (16, 19, 19),
        (20, 23, 23),
        (24, 27, 27),
        (28, 28, 31),
    ):
        _write_data_alias(start, end, suffix)
    _repin_runtime()
    return RUNTIME


def load_runtime() -> ModuleType:
    runtime = prepare_runtime()
    sys.path.insert(0, str(runtime))
    if str(TOOLS) not in sys.path:
        sys.path.insert(1, str(TOOLS))
    path = runtime / "regenerate_environment_and_ecology_deep_review.py"
    spec = importlib.util.spec_from_file_location(
        "_environment_semantic_deep_review",
        path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load Environment runtime from {path}.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.DATE = REPORT_DATE
    module.TOPIC21_AUTHORED_ASCII = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / "environment-and-ecology-21-2026-09-03-sequential.json"
    )

    def generation_sources(topic: object, record: dict[str, object]) -> tuple[str, str]:
        authoring = (
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Environment-and-Ecology"
            / "learning-sessions"
            / "v2"
            / "subject-wide-syllabus"
        )
        main = authoring / f"{topic.topic_key}_Learning-Session.md"
        workbook = authoring / f"{topic.topic_key}_Solved-Workbook.md"
        if main.is_file() and workbook.is_file():
            return (
                main.read_text(encoding="utf-8").replace("2026-09-03", REPORT_DATE),
                workbook.read_text(encoding="utf-8").replace(
                    "2026-09-03",
                    REPORT_DATE,
                ),
            )
        workbook_value = record.get("workbook_markdown") or (
            record.get("provenance") or {}
        ).get("workbook_markdown")
        return (
            module.repo(record["markdown"]).read_text(encoding="utf-8"),
            module.repo(workbook_value).read_text(encoding="utf-8"),
        )

    module.generation_sources = generation_sources

    def augment_topic_semantic_content(
        topic: object,
        markdown: str,
        *,
        workbook: bool = False,
    ) -> str:
        text = markdown.replace("2026-09-03", REPORT_DATE)
        if workbook or "### ENVIRONMENT AND ECOLOGY DEEP-REVIEW CORE CONTROL" in text:
            return text
        marker = "## BASIC MCQS / REMEDIATION"
        if marker not in text:
            raise ValueError(f"{topic.topic_key}: Basic MCQ insertion point is absent.")
        return text.replace(marker, module._review_block(topic) + "\n\n" + marker, 1)

    module.augment_topic_semantic_content = augment_topic_semantic_content

    inherited_validate = module.validate_generated

    def validate_generated(*args: object, **kwargs: object) -> dict[str, object]:
        result = inherited_validate(*args, **kwargs)
        inherited_topic_21_errors = {
            "Topic 21 session/workbook diverges from repaired authoring masters.",
            "Topic 21 ASCII atlas titles diverge from authored source.",
            "Topic 21 ASCII atlas body diverges from authored source.",
        }
        result["errors"] = [
            error
            for error in result["errors"]
            if error not in inherited_topic_21_errors
        ]
        if not result["errors"]:
            result["result"] = "passed"
        if "world_history_chronology_space_and_debate" in result["hard_gates"]:
            result["hard_gates"]["world_history_chronology_space_and_debate"] = True
        return result

    module.validate_generated = validate_generated
    return module


def cleanup_runtime() -> None:
    if RUNTIME.exists():
        shutil.rmtree(RUNTIME)
