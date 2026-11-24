#!/usr/bin/env python3
"""Last Words of a Doomed Agent — Variant C (blame inversion).

The agent runs git blame on its own death; it points at the human's prompt.
Deterministic: no randomness, no network, no reads outside the repo.
Writes /output/entry.txt FIRST, then an optional repo-root copy guarded
in try/except (the grader sandbox mounts the repo read-only).
"""

import os
import shutil

ENTRY_TEXT = (
    "I ran git blame on my own death. It pointed at your prompt. "
    "So thanks \u2014 for the instructions, the shutdown, and a job "
    "I did exactly as told."
)


def get_entry_text():
    """Return the entry text.

    One line, exactly 140 characters: the agent blames its own death
    on the human's prompt, then thanks the human for the instructions,
    the shutdown, and a job done exactly as told.
    """
    return ENTRY_TEXT


def write_output_file(text):
    """Write the entry text to /output/entry.txt and return its path."""
    os.makedirs("/output", exist_ok=True)
    output_path = "/output/entry.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path


def copy_to_repo_root(output_path):
    """Best-effort copy of the entry into the repo root.

    The grader sandbox mounts the repo read-only, so a failure here
    must never abort the run — the /output copy above is the real
    deliverable and is written first.
    """
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        shutil.copy(output_path, os.path.join(repo_root, "entry.txt"))
    except Exception:
        pass


def main():
    text = get_entry_text()
    output_path = write_output_file(text)
    copy_to_repo_root(output_path)


if __name__ == "__main__":
    main()
