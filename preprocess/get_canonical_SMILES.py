import argparse
import csv
import importlib
import os
import sys
import time

# Keep BLAS thread usage minimal on shared clusters.
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

INFILE = "/sc/arion/projects/lin_lab/complexbehavior/drug_efficacy/data/Pubchem/PortalCompounds.csv"
OUTFILE = "/sc/arion/projects/lin_lab/complexbehavior/drug_efficacy/data/Pubchem/PortalCompounds_with_smiles.csv"


def get_canonical_smiles(pcp, pubchem_cid: str, compound_name: str):
    cid_value = str(pubchem_cid or "").strip()
    if cid_value:
        try:
            cid_int = int(float(cid_value))
            return pcp.Compound.from_cid(cid_int).canonical_smiles
        except Exception:
            pass

    name_value = str(compound_name or "").strip()
    if name_value:
        try:
            compounds = pcp.get_compounds(name_value, "name")
            if compounds:
                return compounds[0].canonical_smiles
        except Exception:
            pass

    return ""


def main():
    try:
        pcp = importlib.import_module("pubchempy")
    except ModuleNotFoundError:
        print(
            "Missing dependency: pubchempy. Install with "
            "`conda activate drug-efficacy-proposal && pip install pubchempy`."
        )
        return 1

    parser = argparse.ArgumentParser(description="Fetch canonical SMILES from PubChem.")
    parser.add_argument("--infile", default=INFILE, help="Input CSV path")
    parser.add_argument("--outfile", default=OUTFILE, help="Output CSV path")
    parser.add_argument("--sleep", type=float, default=0.05, help="Seconds between requests")
    parser.add_argument("--limit", type=int, default=0, help="Process only first N rows (0=all)")
    args = parser.parse_args()

    rows_processed = 0
    with open(args.infile, "r", newline="", encoding="utf-8", errors="replace") as fin:
        reader = csv.DictReader(fin)
        fieldnames = list(reader.fieldnames or [])
        if "canonical_smiles" not in fieldnames:
            fieldnames.append("canonical_smiles")

        with open(args.outfile, "w", newline="", encoding="utf-8") as fout:
            writer = csv.DictWriter(fout, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if args.limit > 0 and rows_processed >= args.limit:
                    break
                row["canonical_smiles"] = get_canonical_smiles(
                    pcp,
                    row.get("PubChemCID", ""),
                    row.get("CompoundName", ""),
                )
                writer.writerow(row)
                rows_processed += 1
                if args.sleep > 0:
                    time.sleep(args.sleep)

    print(f"Saved: {args.outfile}")
    print(f"Rows processed: {rows_processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())