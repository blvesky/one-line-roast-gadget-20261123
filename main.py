#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single one-line roast (under 200 characters) to
/output/entry.txt. Deterministic: the same text on every run, stdlib only,
no network, no secrets.
"""

import os

ROAST = "My smartwatch interrupted a panic attack to congratulate me on hitting my daily cardio goal."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars, must be 1-200"
    assert ROAST.strip(), "roast must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
