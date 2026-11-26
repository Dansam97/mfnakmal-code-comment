"""make.fun entry: The Comment Above the Code.

Writes one line to /output/entry.txt: a comment a developer would leave
above fragile production code, funny because it is true.
"""

import os


ENTRY = (
    "Nobody knows what this does. It has been in prod for 6 years. "
    "Touch it and the invoices print in Latin."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
