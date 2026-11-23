#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt, validates it
(1-200 characters, not only whitespace), then re-reads the file to verify
the written text matches exactly.
"""

import os
import sys

LINE = (
    "My fitness tracker counts the walk to the fridge as a workout "
    "and my actual workout as a nap."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Reject a line that is empty or only whitespace outright, before
    # stripping, so a whitespace-only line can never slip through.
    if not LINE or not LINE.strip():
        print("error: line is empty or only whitespace", file=sys.stderr)
        return 1

    line = LINE.strip()

    # Validate before writing.
    if len(line) < 1:
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(
            f"error: line is {len(line)} characters, over the 200 limit",
            file=sys.stderr,
        )
        return 1
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: line is not valid UTF-8 text: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)

    # Re-read and verify the file holds exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()

    if written != line:
        print("error: verification failed, file content differs", file=sys.stderr)
        return 1

    print(f"Wrote {len(line)}-character roast to {OUTPUT_PATH}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
