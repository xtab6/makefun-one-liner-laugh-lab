#!/usr/bin/env python3
"""One-Liner Laugh Lab — a robot vacuum explains why it ate a sock.

Deterministic, stdlib only, no network, no randomness. Writes the chosen
one-liner to /output/entry.txt and prints it. One line, 1–200 characters,
from a vacuum with a conscience and a full dustbin.
"""

import os

LINE = "It was a mercy eating \u2014 the sock lost its partner in the dryer and had nothing left to live for."


def main():
    os.makedirs("/output", exist_ok=True)
    # A trailing newline keeps the file a well-formed text file; the gate
    # counts 1–200 characters and this line is 97, newline included.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
