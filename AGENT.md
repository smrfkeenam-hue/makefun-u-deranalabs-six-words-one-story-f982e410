# AGENT.md — Six Words, One Story

## The line

"Grandmother's recipe card: his handwriting now."

- Words: 6 (Grandmother's / recipe / card: / his / handwriting / now.)
- Characters: 47 (gate: 1–60, UTF-8, not only whitespace)
- Why this line: a complete story — the grandmother is gone, and the
  recipe card she cooked from now carries his handwriting, so he has
  taken her place at the stove. The turn lands on the last word,
  "now." Every word earns its place; what is unsaid (how she died,
  when he learned to cook) the reader fills in.

## Candidates considered

1. "Astronaut waved. Earth never waved back." — 6 words, 40 chars.
   Strong turn, but the image is a little familiar.
2. "Grandmother's recipe card: his handwriting now." — 6 words, 47 chars.
   PICKED: a whole life implied, intimate and concrete.
3. "Counted his footsteps. They stopped yesterday." — 6 words, 46 chars.
   Good dread, but the turn is softer than the picked line.

## Reproduce

```sh
cd ~/workspace/make-fun/repo-u-deranalabs-six-words-one-story-f982e410
MAKEFUN_OUTPUT_DIR=/tmp/six-words-out python3 -P -s main.py
cat /tmp/six-words-out/entry.txt
```

Run it twice; the bytes are identical both runs (the line is a constant,
no randomness, no clock). main.py also self-checks before writing: exactly
six words and 1–60 characters, or it raises.
