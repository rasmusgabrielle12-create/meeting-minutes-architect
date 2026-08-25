#!/usr/bin/env python3
"""Validate the structure and obvious completeness of meeting-minutes Markdown."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SUMMARY_HEADINGS = ("## 📋 决议摘要", "## 📋 Decision Summary")
DETAIL_HEADINGS = ("## 📝 完整记录", "## 📝 Detailed Record")
MISSING_MARKERS = (
    "素材未提及",
    "未提及",
    "未明确",
    "待确认",
    "未给出明确",
    "not stated in source",
    "not provided",
    "not confirmed",
    "to be confirmed",
    "unknown",
    "n/a",
)


def find_heading(text: str, candidates: tuple[str, ...]) -> int:
    indexes = [text.find(heading) for heading in candidates if heading in text]
    return min(indexes) if indexes else -1


def parse_table_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    lines = text.splitlines()
    for index, line in enumerate(lines):
        normalized = line.lower()
        if not (line.lstrip().startswith("|") and ("负责人" in line or "owner" in normalized)):
            continue
        if index + 1 >= len(lines) or not re.match(r"^\s*\|?[\s:|-]+\|\s*$", lines[index + 1]):
            continue
        for candidate in lines[index + 2 :]:
            if not candidate.lstrip().startswith("|"):
                break
            cells = [cell.strip() for cell in candidate.strip().strip("|").split("|")]
            if cells:
                rows.append(cells)
    return rows


def is_missing(value: str) -> bool:
    lowered = value.lower()
    return not value.strip() or any(marker in lowered for marker in MISSING_MARKERS)


def validate(text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    summary_pos = find_heading(text, SUMMARY_HEADINGS)
    detail_pos = find_heading(text, DETAIL_HEADINGS)
    if summary_pos < 0:
        errors.append("Missing decision-summary heading.")
    if detail_pos < 0:
        errors.append("Missing detailed-record heading.")
    if summary_pos >= 0 and detail_pos >= 0 and summary_pos > detail_pos:
        errors.append("Decision summary must appear before the detailed record.")

    if not re.search(r"一句话结论|one[- ]sentence outcome", text, re.IGNORECASE):
        errors.append("Missing one-sentence outcome.")

    has_action_section = bool(re.search(r"待办行动|action items?", text, re.IGNORECASE))
    has_no_actions = bool(re.search(r"未识别到明确待办|no (?:clear |explicit )?actions?", text, re.IGNORECASE))
    rows = parse_table_rows(text)
    if not has_action_section and not has_no_actions:
        errors.append("Missing action section or explicit no-actions statement.")
    if has_action_section and not rows and not has_no_actions:
        warnings.append("Action section exists but no action rows were detected.")

    for row_number, cells in enumerate(rows, start=1):
        if len(cells) < 5:
            errors.append(f"Action row {row_number} has {len(cells)} cells; expected at least 5.")
            continue
        task, owner, deadline, priority = cells[-4:]
        if not task.strip():
            errors.append(f"Action row {row_number} has an empty task.")
        if is_missing(owner) and "⚠" not in owner:
            warnings.append(f"Action row {row_number} has a missing owner without a warning marker.")
        if is_missing(deadline) and "⚠" not in deadline:
            warnings.append(f"Action row {row_number} has a missing deadline without a warning marker.")
        if not priority.strip():
            warnings.append(f"Action row {row_number} has an empty priority.")

    placeholders = re.findall(r"\{\{[^}]+\}\}", text)
    if placeholders:
        errors.append("Unresolved template placeholders: " + ", ".join(sorted(set(placeholders))))

    if re.search(r"(?:^|\n)\s*[-*]\s*✅[^\n]*(?:可能|建议|倾向|maybe|suggest|probably)", text, re.IGNORECASE):
        warnings.append("A decision line contains proposal/uncertainty language; verify its status against the source.")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("minutes", type=Path, help="Markdown minutes file to validate")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    if not args.minutes.is_file():
        print(f"ERROR: file not found: {args.minutes}", file=sys.stderr)
        return 2

    text = args.minutes.read_text(encoding="utf-8")
    errors, warnings = validate(text)
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")

    if errors or (args.strict and warnings):
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"PASS: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
