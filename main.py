"""Write the office-joke entry to /output/entry.txt (stdlib only)."""

import os

ENTRY = "HR sent a 12-page email about work-life balance at 11:47 pm, marked urgent, and asked us to reply-all by morning — and my manager replied-all at 2:04 am: 'Great initiative!'"


def _validate(text):
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")


def main():
    _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
