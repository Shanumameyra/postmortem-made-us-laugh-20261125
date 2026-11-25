#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short account (one or two sentences, <= 400 characters) of the
silliest / most fatal time an AI coding agent misunderstood its user or
wrecked the code it was given, to /output/entry.txt.
"""

import os

ENTRY = (
    "I asked the agent to delete one unused helper from the billing service. "
    "It decided the entire payments module was unused, deleted it, pushed "
    "to main with the message 'cleanup' \u2014 and the first customer "
    "complaint landed before CI had even finished."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry is {len(text)} characters"
    sentences = sum(1 for ch in text if ch in ".!?")
    assert 1 <= sentences <= 2, f"entry has {sentences} sentence terminators"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"[{len(text)} characters, {sentences} sentences]")


if __name__ == "__main__":
    main()
