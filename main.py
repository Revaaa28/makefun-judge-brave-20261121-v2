#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback: /output, then ./out).
"""

import os
import sys

TEXT = (
    "First light. The pond has a skin.\n"
    "She kneels at the bank,\n"
    "one palm flat on the ice.\n"
    "Cold comes through her mitten.\n"
    "Far out, a creak,\n"
    "a chair settling into its joints.\n"
    "One foot. Then the other.\n"
    "She lets go of the branch\n"
    "and pushes off, slow,\n"
    "toward the middle,\n"
    "arms out, not wide."
)


def validate(text: str) -> None:
    n = len(text)  # len(str) counts Unicode code points
    if not (1 <= n <= 280):
        raise ValueError(f"text must be 1-280 code points, got {n}")
    if not text.strip():
        raise ValueError("text must not be whitespace-only")


def output_dir() -> str:
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return "./out"


def main() -> int:
    validate(TEXT)
    dest_dir = output_dir()
    os.makedirs(dest_dir, exist_ok=True)
    path = os.path.join(dest_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(f"wrote {path} ({len(TEXT)} code points)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
