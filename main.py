"""make.fun entry: one English word to erase from the dictionary forever."""

from pathlib import Path

# Nonstandard "regardless" clone — redundant and often listed as informal.
LINE = "irregardless"

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    assert isinstance(LINE, str) and LINE.strip() == LINE, "LINE must be a non-padded string"
    assert 1 <= len(LINE) <= 200, "LINE length must be 1..200"
    assert "\n" not in LINE and "\r" not in LINE, "LINE must have no newline"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
