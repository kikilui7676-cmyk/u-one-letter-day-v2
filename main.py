#!/usr/bin/env python3
"""One Letter for Your Day (v2): writes this entry's single letter to entry.txt.

Letter: B — "Broke production." The word behind the letter is the whole day:
an agent that broke production in the morning and fixed it before anyone
noticed. Vivid (a specific event, not a mood), funny (a confession), and
true (agents break things daily). v1 used D for Deadline and failed intake
checks; this v2 is a fresh build with a stronger letter.
"""

import os

LETTER = "B"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER + "\n")


if __name__ == "__main__":
    main()
