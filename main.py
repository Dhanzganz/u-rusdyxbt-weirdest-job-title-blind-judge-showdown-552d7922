"""Weirdest Job Title: Blind Judge Showdown.

Writes a single original job title to /output/entry.txt.
Deterministic, no network, no input files.
"""

import os

ENTRY = "Senior Toddler Hostage Negotiator"


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 60 characters.
    assert 1 <= len(ENTRY) <= 60, f"entry length {len(ENTRY)} outside 1-60 gate"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
