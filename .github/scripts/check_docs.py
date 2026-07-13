#!/usr/bin/env python3
"""Validate documentation conventions required by AGENTS.md:

1. Every SKILL.md has YAML front matter with non-empty 'name' and 'description'.
2. Every relative (non-URL) Markdown link in any .md file resolves to a real file.

Usage (from anywhere; run locally the same way CI runs it):
    python3 .github/scripts/check_docs.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\s*\n", re.DOTALL)
REQUIRED_FRONT_MATTER_KEYS = ("name", "description")

CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")


def iter_repo_files(pattern: str):
    for path in sorted(REPO_ROOT.rglob(pattern)):
        if ".git" not in path.parts:
            yield path


def check_front_matter() -> list[str]:
    errors: list[str] = []
    for path in iter_repo_files("SKILL.md"):
        rel = path.relative_to(REPO_ROOT)
        text = path.read_text(encoding="utf-8")

        match = FRONT_MATTER_RE.match(text)
        if not match:
            errors.append(
                f"{rel}: missing YAML front matter "
                "(file must start with '---' and have a closing '---' line)"
            )
            continue

        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: front matter is not valid YAML ({exc})")
            continue

        if not isinstance(data, dict):
            errors.append(
                f"{rel}: front matter must be a YAML mapping (got {type(data).__name__})"
            )
            continue

        for key in REQUIRED_FRONT_MATTER_KEYS:
            value = data.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{rel}: front matter '{key}' is missing or empty")

    return errors


def _strip_code(text: str) -> str:
    """Blank out fenced/inline code so link-like text inside them is never
    treated as a real link, while preserving line numbers for error messages."""
    text = CODE_FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    text = INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), text)
    return text


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in iter_repo_files("*.md"):
        rel = path.relative_to(REPO_ROOT)
        text = _strip_code(path.read_text(encoding="utf-8"))

        for match in LINK_RE.finditer(text):
            raw_target = match.group(2).strip()
            target = raw_target.split()[0] if raw_target.split() else raw_target

            if not target or target.startswith("#") or URL_SCHEME_RE.match(target):
                continue  # in-page anchor, or absolute URL (http, mailto, ...)

            target = target.split("#", 1)[0]  # drop a trailing #anchor
            if not target:
                continue

            if target.startswith("/"):
                resolved = (REPO_ROOT / target.lstrip("/")).resolve()
            else:
                resolved = (path.parent / target).resolve()

            if not resolved.is_file():
                line_no = text.count("\n", 0, match.start()) + 1
                errors.append(
                    f"{rel}:{line_no}: broken link -> '{raw_target}' "
                    f"(resolved to {resolved}, no such file)"
                )

    return errors


def main() -> int:
    errors = check_front_matter() + check_markdown_links()

    if errors:
        print(f"Found {len(errors)} problem(s):\n")
        for error in errors:
            print(f"  - {error}")
        print()
        return 1

    print("OK: all SKILL.md front matter and Markdown links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
