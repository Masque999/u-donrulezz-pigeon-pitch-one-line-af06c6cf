#!/usr/bin/env python3
"""Pigeon Pitch, One Line — one line, up to 200 characters.

Writes the entry to /output/entry.txt for make.fun's program/v1 harness.
"""
import os

SENTENCE = "We're disrupting urban logistics: our flock delivers crumbs 40% faster than any courier, zero emissions, and we work for breadcrumbs."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    # Write-back verification: a silent bad write must fail loudly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != SENTENCE:
        raise SystemExit(f"entry mismatch: wrote {len(SENTENCE)} chars, read back {len(written)}")


if __name__ == "__main__":
    main()
