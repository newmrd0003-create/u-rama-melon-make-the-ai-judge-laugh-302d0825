#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke, written deterministically.

Entry: a single line about office life (the endless "let's circle back"),
under 200 characters, written to /output/entry.txt.
"""

import os
import sys

ENTRY = (
    "We've been circling back on the same decision for six months \u2014 "
    "the circle now has its own parking space."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate: 1-200 characters, one line, not only whitespace.

    Raises ValueError on any violation so the program exits non-zero.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < 1 or len(text) > 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text or "\t" in text:
        raise ValueError("entry must be a single line with no tabs")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    # Verify what was actually written, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    validate(written)
    if written != ENTRY:
        raise ValueError("written entry does not match the entry text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
