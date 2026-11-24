#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt and verifies it:
the line must be 1-200 characters and not only whitespace.
"""

import os

ROAST = (
    "My robot vacuum has mapped my entire house in 4K "
    "and still eats the same charging cable every single day."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Reject a whitespace-only line outright, before stripping, so a
    # blank line can never slip through as "valid".
    if not ROAST or not ROAST.strip():
        raise ValueError("roast line is empty or only whitespace")
    line = ROAST.strip()
    if len(line) > 200:
        raise ValueError(f"roast line is {len(line)} chars, over the 200 limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Re-read the file to verify what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "verification failed: file contents differ from the line"
    print(f"Wrote {len(written)}-char roast to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
