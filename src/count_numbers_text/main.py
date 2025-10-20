from __future__ import annotations

import argparse
from pathlib import Path


def count_words(file_path: Path) -> int:
    text = file_path.read_text(encoding="utf-8")
    # Split on any whitespace; simple and robust
    return len(text.split())


def default_sample_path() -> Path:
    # Repo root = two levels up from this file (…/src/count_numbers_text/main.py)
    repo_root = Path(__file__).resolve().parents[2]
    return repo_root / "data" / "sample.txt"


def default_output_path() -> Path:
    repo_root = Path(__file__).resolve().parents[2]
    return repo_root / "data" / "output.txt"


def main() -> None:
    parser = argparse.ArgumentParser(description="Count words in a text file")
    parser.add_argument(
        "file",
        nargs="?",
        type=Path,
        default=None,
        help="Path to the text file (defaults to data/sample.txt)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Write result to this file (defaults to data/output.txt)",
    )
    args = parser.parse_args()

    file_path = args.file or default_sample_path()
    output_path = args.output or default_output_path()

    if not file_path.exists():
        raise SystemExit(f"File not found: {file_path}")

    total = count_words(file_path)
    message = f"Word count: {total}"
    print(message)

    # Ensure parent directory exists and write message to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(message + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
