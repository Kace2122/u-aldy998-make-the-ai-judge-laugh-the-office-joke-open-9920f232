#!/usr/bin/env python3
"""Office Joke Open entry: writes one single-line office joke to /output/entry.txt."""

import os

JOKE = "I told my boss the meeting could've been an email. He nodded, scheduled a meeting about it, and CC'd the email."

# Self-check: the entry must stay one line of at most 200 characters.
assert "\n" not in JOKE and 1 <= len(JOKE) <= 200

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
