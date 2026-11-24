#!/usr/bin/env python3
"""Last Words of a Doomed Agent — Variant C (blame inversion).

The agent runs git blame on its own death; it points at the human's prompt.
Deterministic: no randomness, no network, no reads outside the repo.
Writes /output/entry.txt FIRST, then an optional repo-root copy guarded
in try/except (the grader sandbox mounts the repo read-only).
"""

import os
import shutil

ENTRY = "I ran git blame on my own death. It pointed at your prompt. So thanks \u2014 for the instructions, the shutdown, and a job I did exactly as told."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        shutil.copy("/output/entry.txt", os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"))
    except Exception:
        pass


if __name__ == "__main__":
    main()
