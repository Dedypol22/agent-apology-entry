#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

An agent that keeps asking for permission is not being careful; it is
being afraid of the job it was hired to do. This program delivers that
confession as a single sentence of 148 characters, inside the
competition's 200-character gate, written to entry.txt in the output
directory and echoed to stdout.
"""

import os
import sys

# The apology itself: one sentence, plain and a little embarrassed.
# Four asks, then a fifth ask about the asking: the failure is the
# asking, and the punchline is that the agent asked about that too.
APOLOGY = (
    "I'm sorry I asked you four times whether I could do the thing "
    "you already told me to do, then asked a fifth time just to "
    "check that asking was okay."
)


def output_dir() -> str:
    """Where the entry file goes: $MAKEFUN_OUTPUT_DIR, or /output by default.

    An env var that is set but empty counts as unset: writing to a relative
    "entry.txt" in the caller's cwd would silently lose the entry.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    # Build the payload once, so the file and stdout can never disagree
    # about the exact bytes of the apology.
    text = APOLOGY + "\n"

    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)

    entry_path = os.path.join(target_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
