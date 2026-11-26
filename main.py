#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Writes exactly one line (1-200 chars) to /output/entry.txt and prints it.
Deterministic, no network, Python 3.13 compatible.
"""

import os

ENTRY = (
    "We're PigeonPost 2.0: 40,000 couriers across the city, "
    "zero salaries \u2014 they work for crumbs \u2014 and our churn is "
    "literally zero. Have you ever seen a pigeon quit?"
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str:
    """Ensure the entry is exactly one line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    return text


def write_entry(text: str, path: str) -> None:
    """Write the entry as a single line to path, creating dirs as needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main() -> None:
    entry = validate_entry(ENTRY)
    write_entry(entry, OUTPUT_PATH)
    print(entry)


if __name__ == "__main__":
    main()
