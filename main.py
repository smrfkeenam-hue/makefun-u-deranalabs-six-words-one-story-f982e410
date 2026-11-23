"""Six Words, One Story — a complete story in exactly six words.

The line is a constant. The program writes it to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the harness sets it).

Chosen line: "Grandmother's recipe card: his handwriting now."
Six words, one life implied: the grandmother is gone, and the card
she cooked from now carries his handwriting — he has taken her place
at the stove. The turn lands on the last word: "now."
"""

import os

LINE = "Grandmother's recipe card: his handwriting now."


def main():
    words = LINE.split()
    if len(words) != 6:
        raise ValueError(f"line must be exactly six words, got {len(words)}")
    if not 1 <= len(LINE) <= 60:
        raise ValueError(f"line must be 1-60 characters, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
