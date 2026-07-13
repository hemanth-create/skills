#!/usr/bin/env python3
"""Normalize a SARIF export into compact, review-ready JSON findings."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable


DEFAULT_MAX_BYTES = 100 * 1024 * 1024


def text_value(value: Any) -> str:
    """Return a SARIF text value without assuming its representation."""
    if isinstance(value, str):
        return value
    if isinstance(value, dict) and isinstance(value.get("text"), str):
        return value["text"]
    return ""


def driver_for(run: dict[str, Any]) -> dict[str, Any]:
    """Return a SARIF driver object only when the run has one."""
    tool = run.get("tool")
    if not isinstance(tool, dict):
        return {}
    driver = tool.get("driver")
    return driver if isinstance(driver, dict) else {}


def rule_index(run: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Index SARIF driver rules by ID for result enrichment."""
    driver = driver_for(run)
    rules = driver.get("rules", [])
    return {
        rule["id"]: rule
        for rule in rules
        if isinstance(rule, dict) and isinstance(rule.get("id"), str)
    }


def first_location(result: dict[str, Any]) -> tuple[str | None, int | None]:
    """Extract the first file and line from a SARIF result when available."""
    locations = result.get("locations", [])
    if not isinstance(locations, list) or not locations:
        return None, None
    location = locations[0]
    if not isinstance(location, dict):
        return None, None
    physical = location.get("physicalLocation", {})
    artifact = physical.get("artifactLocation", {}) if isinstance(physical, dict) else {}
    region = physical.get("region", {}) if isinstance(physical, dict) else {}
    uri = artifact.get("uri") if isinstance(artifact, dict) else None
    line = region.get("startLine") if isinstance(region, dict) else None
    return uri if isinstance(uri, str) else None, line if isinstance(line, int) else None


def severity_from_level(level: Any) -> str:
    """Map a SARIF result level to a non-final review priority."""
    return {"error": "HIGH", "warning": "MEDIUM", "note": "LOW"}.get(
        level, "INFO"
    )


def normalize_sarif(document: dict[str, Any]) -> Iterable[dict[str, Any]]:
    """Yield compact findings while preserving scanner-provided evidence."""
    runs = document.get("runs", [])
    if not isinstance(runs, list):
        raise ValueError("SARIF 'runs' must be a list.")

    for run_number, run in enumerate(runs, start=1):
        if not isinstance(run, dict):
            continue
        driver = driver_for(run)
        tool_name = driver.get("name")
        rules = rule_index(run)
        results = run.get("results", [])
        if not isinstance(results, list):
            continue

        for result_number, result in enumerate(results, start=1):
            if not isinstance(result, dict):
                continue
            rule_id = result.get("ruleId")
            rule = rules.get(rule_id, {}) if isinstance(rule_id, str) else {}
            file_path, line = first_location(result)
            title = text_value(rule.get("shortDescription")) or text_value(
                result.get("message")
            )
            yield {
                "id": f"sarif:{run_number}:{result_number}",
                "source_tool": "sarif",
                "tool": tool_name if isinstance(tool_name, str) else None,
                "rule_id": rule_id if isinstance(rule_id, str) else None,
                "title": title or "Untitled scanner finding",
                "scanner_level": result.get("level"),
                "scanner_priority": severity_from_level(result.get("level")),
                "file": file_path,
                "line": line,
                "message": text_value(result.get("message")),
            }


def read_document(path: Path, max_bytes: int) -> dict[str, Any]:
    """Read one bounded SARIF JSON document from disk."""
    if path.stat().st_size > max_bytes:
        raise ValueError(f"Input exceeds the {max_bytes}-byte safety limit.")
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValueError("SARIF root must be a JSON object.")
    return document


def parse_args() -> argparse.Namespace:
    """Parse the local-only SARIF normalizer arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to a SARIF JSON export.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=DEFAULT_MAX_BYTES,
        help="Maximum input size to read (default: 104857600).",
    )
    return parser.parse_args()


def main() -> int:
    """Normalize one SARIF file without modifying the scanned repository."""
    args = parse_args()
    try:
        findings = list(normalize_sarif(read_document(args.input, args.max_bytes)))
        payload = json.dumps(findings, indent=2) + "\n"
        if args.output:
            args.output.write_text(payload, encoding="utf-8")
        else:
            print(payload, end="")
    except (OSError, ValueError) as error:
        print(f"Unable to normalize SARIF: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
