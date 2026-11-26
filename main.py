"""Green Tests, Nothing Works — the excuse contest entry.

Writes a single one-line excuse (1-140 chars, one line, no trailing
newline) to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only.
"""

import os

ENTRY = (
    "All green! The tests passed because the app does nothing \u2014 "
    "and nothing, it turns out, is extremely testable."
)


def main() -> None:
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
