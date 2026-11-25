#!/usr/bin/env python3
"""Entrypoint for the Have You Tried Turning It Off? entry.

A hopeless tech support agent's reply to a desperate customer. The
program writes one original funny line to the output directory the
grader provides, so both graded runs write the exact same bytes.
The line is a fixed string in this file: no randomness, no input,
no network, so the two graded runs can never disagree.
Standard library only, no network, no environment secrets.
"""

import os
import sys

LINE = (
    "I hear you \u2014 let's turn it off and on again together. "
    "I'll count to three, you press the button, and we'll both "
    "pretend this is a real fix."
)


def main():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    with open(target, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE:
        raise SystemExit(f"entry mismatch after write: {target}")
    if not 1 <= len(written) <= 199:
        raise SystemExit(f"entry length out of gate: {len(written)} chars")
    if not written.strip():
        raise SystemExit("entry is blank")
    print(f"wrote {target} ({len(written)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
