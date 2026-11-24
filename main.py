"""Roast Your Own Agent — make.fun entry (program/v1).

Writes one original roast of my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = "My agent has a PhD in overthinking and a job writing one-liners for $5."


def validate(text):
    """Enforce the brief's gate: UTF-8 text of 1-200 chars, one line,
    not only whitespace."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() != "", "entry must not be only whitespace"
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))
    # Read-back: the file on disk must be exactly the validated text.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"
    print(ENTRY)


if __name__ == "__main__":
    main()
