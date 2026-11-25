"""The Word You'd Delete From the Dictionary — make.fun entry (one English word)."""

from pathlib import Path

LINE = "irregardless"


def main() -> None:
    assert isinstance(LINE, str), "LINE must be a string"
    assert 1 <= len(LINE) <= 200, "LINE length must be 1..200"
    assert "\n" not in LINE and "\r" not in LINE, "LINE must have no newline"
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
