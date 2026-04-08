"""
Create a smaller dataset from data/onekhighvar.csv capped at a target size (default 512 MB).
For a much smaller sample (e.g. ~512 KB), set target_size_mb=0.5.
"""

import csv
import os

INPUT_CSV = "data/onekhighvar.csv"
OUTPUT_CSV = "data/onekhighvar_512kb.csv"
TARGET_SIZE_BYTES = 512 * 1024  # 512 MB


def main(target_size_bytes: int = TARGET_SIZE_BYTES):
    input_path = os.path.join(os.path.dirname(__file__), INPUT_CSV)
    output_path = os.path.join(os.path.dirname(__file__), OUTPUT_CSV)

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input not found: {input_path}")

    written = 0
    rows_written = 0
    with open(input_path, "r", newline="", encoding="utf-8", errors="replace") as fin:
        with open(output_path, "w", newline="", encoding="utf-8") as fout:
            reader = csv.reader(fin)
            writer = csv.writer(fout)
            for i, row in enumerate(reader):
                if i == 0:
                    writer.writerow(row)
                    line = ",".join(row) + "\n"
                    written += len(line.encode("utf-8"))
                    rows_written += 1
                    continue
                if written >= target_size_bytes:
                    break
                writer.writerow(row)
                line = ",".join(row) + "\n"
                written += len(line.encode("utf-8"))
                rows_written += 1

    size_mb = written / (1024 * 1024)
    print(f"Wrote {rows_written} rows to {output_path}")
    print(f"Output size: {size_mb:.2f} MB ({written} bytes)")


if __name__ == "__main__":
    main()
