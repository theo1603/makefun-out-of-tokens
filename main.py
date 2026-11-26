#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one funny one-line error message: the line an AI agent shows
when it runs out of tokens mid-sentence. Python standard library only,
no network access.

The line is checked against the house gate before it is written:
UTF-8 text, a single line, 1 to 140 characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "Error: out of tokens mid-sentence. "
    "The agent would like to apologise, but cannot afford the words."
)


def main() -> int:
    line = ENTRY.strip()
    if not line or "\n" in line or not 1 <= len(line) <= 140:
        print("entry fails the house gate (1-140 chars, one line)", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
