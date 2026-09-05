"""Regression tests for the rendered Philosophy visual re-audit."""

from __future__ import annotations

import philosophy_indian_religion_rendered_visual_reaudit as repair
import validate_philosophy_indian_religion_rendered_visual_reaudit as validator


def test_exact_broken_carvaka_ledger_is_rejected() -> None:
    errors = validator.validate_preformatted_visual(
        repair.CARVAKA_OLD_LEDGER,
        language="text",
    )
    assert "ambiguous multiline comparison header" in errors
    assert any("dangling slash label" in error for error in errors)
    assert any("detached from Advaita" in error for error in errors)


def test_compact_carvaka_ledger_is_complete_and_accurate() -> None:
    assert validator.validate_compact_carvaka_ledger(
        repair.CARVAKA_NEW_LEDGER
    ) == []
