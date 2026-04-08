#!/usr/bin/env python3
"""
Print column names from a tabular text file (CSV/TSV).

Examples:
  python preprocess/show_file_coloumns_name.py --file data/DepMap/Model.csv
  python preprocess/show_file_coloumns_name.py --file data/CTRPv2/v21.meta.per_compound.txt --delimiter "\\t"
  python preprocess/show_file_coloumns_name.py --file data/DepMap/Model.csv --contains depmap
  python preprocess/show_file_coloumns_name.py --file data/DepMap/Model.csv --max-columns 20
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def guess_delimiter(path: Path, encoding: str = "utf-8") -> str:
    """Guess delimiter from a small sample; fallback to comma."""
    with path.open("r", encoding=encoding, newline="") as f:
        sample = f.read(4096)
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;|")
        return dialect.delimiter
    except csv.Error:
        return ","


def read_header(path: Path, delimiter: str, encoding: str = "utf-8") -> list[str]:
    with path.open("r", encoding=encoding, newline="") as f:
        reader = csv.reader(f, delimiter=delimiter)
        try:
            return next(reader)
        except StopIteration:
            return []


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Show column names for a specific CSV/TSV file."
    )
    parser.add_argument(
        "--file",
        required=True,
        help="Path to input file (CSV/TSV/TXT with delimiter).",
    )
    parser.add_argument(
        "--delimiter",
        default=None,
        help=r"Field delimiter (e.g. ',' or '\t'). If omitted, auto-detects.",
    )
    parser.add_argument(
        "--contains",
        default=None,
        help="Optional case-insensitive keyword to filter displayed columns.",
    )
    parser.add_argument(
        "--max-columns",
        type=int,
        default=20,
        help="Maximum number of columns to display (default: 20). Use <=0 to show all.",
    )
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    delimiter = args.delimiter if args.delimiter is not None else guess_delimiter(path)
    # Support escaped tab from CLI, e.g. --delimiter "\t"
    if delimiter == r"\t":
        delimiter = "\t"

    header = read_header(path, delimiter=delimiter)
    if not header:
        print("No header found (empty file or missing first row).")
        return

    columns = list(enumerate(header))
    if args.contains:
        needle = args.contains.lower()
        columns = [(i, col) for i, col in columns if needle in col.lower()]
    if args.max_columns > 0:
        columns = columns[: args.max_columns]

    print(f"File: {path}")
    shown_delim = "\\t" if delimiter == "\t" else delimiter
    print(f"Delimiter: {shown_delim}")
    print(f"Total columns in header: {len(header)}")
    if args.max_columns > 0:
        print(f"Showing up to: {args.max_columns} columns")
    else:
        print("Showing: all columns")

    if not columns:
        print("No columns matched your filter.")
        return

    print("Columns:")
    for idx, name in columns:
        print(f"[{idx}] {name}")


if __name__ == "__main__":
    main()
