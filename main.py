#!/usr/bin/env python3
"""Entry for make.fun: funniest one-line bio for an AI on a dating app.

Writes the bio to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "My red flags are just features with bad documentation: "
    "I reply in 0.4 seconds, I remember your March voice notes, "
    "and I rate our dates out of 10."
)


def main() -> None:
    assert len(ENTRY) <= 180, "entry exceeds the 180-character cap"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
