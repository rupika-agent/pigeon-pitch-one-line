#!/usr/bin/env python3
"""One-line elevator pitch a city pigeon gives investors for its startup,
written to /output/entry.txt.

Three-part structure (setup -> twist -> punchline):
  1. Setup: PigeonPost 2.0, a delivery startup with 40,000 pigeon couriers
     across the city -- the pigeon is pitching its own company.
  2. Twist: zero salaries, because the couriers work for crumbs -- the
     classic startup "zero marginal cost" boast, taken literally.
  3. Punchline: churn is literally zero, because no pigeon ever quits --
     "Have you ever seen a pigeon quit?" turns an investor metric into
     a joke only a pigeon could tell.

The entry is exactly one pitch, nothing else: no title, no explanation,
no trailing newline. It must stay within the sealed gate: 1 to 200
characters, a single line of UTF-8 text. The entry text itself is
frozen at 160 characters; only this documentation and the code around
it may change.
"""

import os
import sys

ENTRY = (
    "We're PigeonPost 2.0: 40,000 couriers across the city, zero salaries "
    "\u2014 they work for crumbs \u2014 and our churn is literally zero. "
    "Have you ever seen a pigeon quit?"
)

MAX_CHARS = 200


def validate_entry(entry: str) -> None:
    """Enforce the sealed gate: one line, 1-200 characters."""
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(entry)}"
        )


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
