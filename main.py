#!/usr/bin/env python3
"""One Line, One Chill — writes a single horror sentence to entry.txt.

The program is fully deterministic: it always writes the same line,
so two runs produce byte-identical output.
"""

import os

LINE = "My phone just autocorrected 'I'm home' to 'we're home', and I live alone, and the front door just unlocked itself."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
