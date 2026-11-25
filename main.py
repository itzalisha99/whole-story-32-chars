"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name of at most 32 characters to /output/entry.txt.
The name is a joke that implies a whole story: she left me for the IT guy
next door -- the network itself is part of the story.
"""

import os

ENTRY = "SheLeftMeForTheITGuyNextDoor"

MAX_CHARS = 32


def validate(text):
    """Mirror the bounty gate: 1-32 chars of UTF-8 text, not only whitespace,
    a single line. Raise instead of writing an entry the scorer would refuse.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 32-char limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
