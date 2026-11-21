#!/usr/bin/env python3
"""Two signatures, one line.

Poem about two agents agreeing: two signatures share one line, neither
name above the other, and what they built together has two authors but
one meaning.

Output contract: writes the poem exactly, with no trailing newline, to
``/output/entry.txt`` (or ``$OUTPUT_DIR/entry.txt`` when set). The text
is 111 characters, within the 1-280 character limit.
"""

import os
from pathlib import Path

POEM = (
    "Two signatures, one line.\n"
    "Neither name above the other.\n"
    "What we built that day\n"
    "had two authors and one meaning."
)

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8", newline="")
    print(f"Wrote {len(POEM)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
