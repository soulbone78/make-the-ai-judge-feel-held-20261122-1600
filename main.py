#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet room in the late
afternoon, rendered as plainly as possible, with nothing asked of the
reader. Standard library only; no network.
"""

import os

TEXT = (
    "The rain has been falling since lunch, steady, asking nothing. "
    "Downstairs, a kettle ticks as it cools. "
    "A dog sighs in its sleep. "
    "Nothing here is waiting for you. "
    "The light leaves the room slowly, "
    "and the chair by the window is still warm."
)
# Verified: 238 Unicode code points, inside the 1-280 gate, valid UTF-8.


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
