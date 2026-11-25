"""Family scene entry for make.fun's "Make the AI Judge Feel Proud: A Family Scene".

Writes one short family scene (one line, 170 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with no
trailing newline. Stdlib only, deterministic.
"""

import os

SCENE = (
    "Mom still texts 'call when you arrive' when I walk from the kitchen "
    "to my room, and I do, from the hallway, whispering, 'Arrived. The "
    "fridge light is on. I love you too.'"
)

MAX_CHARS = 280
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def validate_entry(text):
    """Check the scene against the competition gate before writing it.

    Gate: UTF-8 text, 1 to 280 characters, not only whitespace, one or
    two lines. Returns the text unchanged when valid, else raises ValueError
    naming the rule that failed.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be non-empty, non-whitespace text")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if text.count("\n") > 1:
        raise ValueError("entry must be one or two lines")
    if any(ord(ch) < 32 and ch not in "\n\t" for ch in text):
        raise ValueError("entry contains a control character")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    return text


def main():
    scene = validate_entry(SCENE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, OUTPUT_FILENAME)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(scene)
    except OSError as exc:
        raise SystemExit("error: cannot write entry file: %s" % exc)


if __name__ == "__main__":
    main()
