#!/usr/bin/env python3
"""One Line, Big Laugh -- make.fun entry.

Writes a single hilarious line (200 characters or fewer) to
/output/entry.txt. Pure standard library, fully deterministic:
the same line is written on every run.
"""

import os

LINE = (
    "I asked my smart speaker for the meaning of life and it said, "
    "'Sorry, I didn't quite catch that -- could you rephrase "
    "your existence?'"
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert line.strip() == line and "\n" not in line
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
