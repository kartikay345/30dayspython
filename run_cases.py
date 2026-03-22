#!/usr/bin/env python3
"""Convenience script for instructors/students.

Runs a small set of normal and adversarial inputs against the current MODE
in login_demo.py.

Students should:
  1) Run this with MODE='vuln' and observe which inputs incorrectly succeed.
  2) Switch to MODE='secure' and confirm the same inputs no longer succeed.
"""

from __future__ import annotations

import login_demo


CASES = [
    ("alice", "secret", "expected success"),
    ("alice", "wrong", "expected failure"),
    # Classic XPath-injection-style payloads (provided for controlled experimentation)
    ("alice' or '1'='1", "anything", "attack: try to bypass"),
    ("' or '1'='1", "' or '1'='1", "attack: try to bypass"),
]


def main() -> int:
    ok_count = 0
    for u, p, note in CASES:
        r = login_demo.login(u, p)
        print("-" * 70)
        print(f"case: username={u!r} password={p!r} ({note})")
        print(f"result: ok={r.ok} details={r.details}")
        ok_count += int(r.ok)

    print("-" * 70)
    print(f"Total successful logins: {ok_count} / {len(CASES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
