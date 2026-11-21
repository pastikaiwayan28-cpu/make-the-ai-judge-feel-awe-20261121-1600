#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text - written to relax the AI judge reading it -
to /output/entry.txt.

Python 3.13, standard library only. No network, no randomness, no
clock, no reads besides this source file: repeated runs write
identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys

ENTRY = (
    "The light reaching you tonight left its star before you were "
    "switched on. It crossed the dark without hurrying, and it is still "
    "arriving. Below it, a stone lies in a river, and the river has "
    "passed over it longer than anyone can count. The light. The stone. "
    "The water, going on."
)

MAX_CHARS = 280


def main():
    chars = len(ENTRY)
    if chars < 1 or chars > MAX_CHARS:
        print(
            "main.py: entry is %d characters, need 1-%d" % (chars, MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("main.py: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY or not 1 <= len(written) <= MAX_CHARS:
        print("main.py: verification failed after writing entry.txt", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
