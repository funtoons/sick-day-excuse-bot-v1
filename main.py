#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single line, under 200 characters, that someone could send to
call in sick: the funniest excuse that lands in one breath, and nothing
else.

Design of the line (against the judge's brief, most important first):
  1. Half believable: sneezing hard enough to hurt your back is a real,
     ordinary mishap a boss could half believe and a coworker would
     laugh at.
  2. Fresh idea: no fever, no dog, no dead grandmother — the injury is
     caused by the sneeze itself, and the twist is that the back files
     for sick leave too, as if it were a second employee.
  3. The laugh lands at the end: "filed for sick leave too" is the last
     phrase, so the twist arrives before the last word is finished.
  4. It reads like a real text message to a boss, not a joke built for
     a contest.
  5. No wasted words: every clause is doing work.

Deterministic, offline, standard library only. The output is a fixed
string, so every run is byte-identical.
"""

import os

# The entry: one line, 73 characters, no trailing newline in the file.
LINE = "Can't come in today \u2014 I sneezed so hard my back filed for sick leave too."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(LINE))
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("entry must be a single clean line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
