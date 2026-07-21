#!/usr/bin/env python3
"""Reject numeric resume claims absent from the canonical career history."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = PROJECT_ROOT / "00-reference" / "career-history.md"
NUMBER = re.compile(
    r"(?<![\w$])~?\$?\d[\d,]*(?:\.\d+)?(?:[%+]|[KMBkmb])?(?:/\d+)?(?:-[A-Za-z]+)?"
)
PHONE = re.compile(r"\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}")


def claims(text: str) -> set[str]:
    text = PHONE.sub("", text)
    return {match.group(0).lower().replace(",", "") for match in NUMBER.finditer(text)}


def unsupported(source: str, target: str) -> list[str]:
    # ponytail: metric-only gate; add claim-ID validation if nonnumeric drift appears.
    return sorted(claims(target) - claims(source))


def check(source_path: Path, target_path: Path) -> int:
    if not source_path.is_file():
        print(f"ERROR: canonical source not found: {source_path}", file=sys.stderr)
        return 2
    if not target_path.is_file():
        print(f"ERROR: resume not found: {target_path}", file=sys.stderr)
        return 2

    invented = unsupported(
        source_path.read_text(encoding="utf-8"),
        target_path.read_text(encoding="utf-8"),
    )
    if invented:
        print("FAIL: numeric claims absent from career-history.md:", file=sys.stderr)
        for claim in invented:
            print(f"- {claim}", file=sys.stderr)
        return 1

    print(f"PASS: numeric claims supported by career-history.md: {target_path.name}")
    return 0


def self_test() -> int:
    source = "Saved ~$900K, improved response 42%, supported 500+ users in 24/7 operations."
    good = "Supported 500+ users in 24/7 operations and improved response 42%."
    bad = "Improved response 99%."
    assert unsupported(source, good) == []
    assert unsupported(source, bad) == ["99%"]
    print("PASS: check_resume accepts sourced metrics and rejects unsupported 99%")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resume", nargs="?", type=Path)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.resume is None:
        parser.error("resume is required unless --self-test is used")
    return check(args.source, args.resume)


if __name__ == "__main__":
    raise SystemExit(main())
