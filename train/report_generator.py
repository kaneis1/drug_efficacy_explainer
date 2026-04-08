#!/usr/bin/env python3
"""
Generate enriched grounded reports from evidence.jsonl.

Resolves raw IDs to human-readable drug names, cell line names, cancer types,
and decodes Morgan fingerprint bits to molecular substructure SMARTS patterns.

Usage:
  python train/report_generator.py
  python train/report_generator.py --num-reports 10
  python train/report_generator.py --compound-meta data/CTRPv2/v21.meta.per_compound.txt
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _safe_str(val, default: str = "") -> str:
    if pd.isna(val):
        return default
    return str(val).strip()


def _load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


# ---------------------------------------------------------------------------
# Metadata loaders
# ---------------------------------------------------------------------------

def _load_compound_meta(path: Path) -> dict[int, dict]:
    """master_cpd_id -> {cpd_name, gene_target, mechanism, smiles}."""
    df = pd.read_csv(path, sep="\t")
    lookup: dict[int, dict] = {}
    for _, row in df.iterrows():
        cpd_id = int(row["master_cpd_id"])
        lookup[cpd_id] = {
            "cpd_name": _safe_str(row.get("cpd_name"), f"cpd_{cpd_id}"),
            "gene_target": _safe_str(row.get("gene_symbol_of_protein_target")),
            "mechanism": _safe_str(row.get("target_or_activity_of_compound")),
            "smiles": _safe_str(row.get("cpd_smiles")),
        }
    return lookup


def _load_cell_meta(path: Path) -> dict[int, dict]:
    """master_ccl_id -> {ccl_name, primary_site, histology, subtype}."""
    df = pd.read_csv(path, sep="\t")
    lookup: dict[int, dict] = {}
    for _, row in df.iterrows():
        ccl_id = int(row["master_ccl_id"])
        lookup[ccl_id] = {
            "ccl_name": _safe_str(row.get("ccl_name"), f"ccl_{ccl_id}"),
            "primary_site": _safe_str(row.get("ccle_primary_site")).replace("_", " "),
            "histology": _safe_str(row.get("ccle_primary_hist")).replace("_", " "),
            "subtype": _safe_str(row.get("ccle_hist_subtype_1")).replace("_", " "),
        }
    return lookup


def _drug_info(cpd_id: int | None, compound_meta: dict) -> dict:
    if cpd_id is None:
        return {"cpd_name": "unknown", "gene_target": "", "mechanism": "", "smiles": ""}
    default = {"cpd_name": f"cpd_{cpd_id}", "gene_target": "", "mechanism": "", "smiles": ""}
    return compound_meta.get(int(cpd_id), default)


def _cell_info(ccl_id: int | None, cell_meta: dict) -> dict:
    if ccl_id is None:
        return {"ccl_name": "unknown", "primary_site": "", "histology": "", "subtype": ""}
    default = {"ccl_name": f"ccl_{ccl_id}", "primary_site": "", "histology": "", "subtype": ""}
    return cell_meta.get(int(ccl_id), default)


# ---------------------------------------------------------------------------
# Morgan fingerprint bit → substructure decoder
# ---------------------------------------------------------------------------

def _build_fp_bit_descriptions(
    compound_meta: dict[int, dict],
    n_bits: int = 1024,
    radius: int = 2,
) -> dict[str, dict]:
    """
    Decode Morgan fingerprint bit indices to representative SMARTS patterns
    by re-computing fingerprints with bitInfo for every compound SMILES.
    """
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem
    except ImportError:
        print("  Warning: RDKit not available — skipping fingerprint bit decoding.")
        return {}

    bit_smarts: dict[int, dict[str, int]] = {}
    bit_drugs: dict[int, list[str]] = {}

    for cpd_id, info in compound_meta.items():
        smiles = info.get("smiles", "")
        if not smiles:
            continue
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            continue
        bi: dict = {}
        AllChem.GetMorganFingerprintAsBitVect(
            mol, radius=radius, nBits=n_bits, bitInfo=bi
        )
        drug_name = info.get("cpd_name", f"cpd_{cpd_id}")
        for bit_idx, envs in bi.items():
            if bit_idx not in bit_smarts:
                bit_smarts[bit_idx] = {}
                bit_drugs[bit_idx] = []
            bit_drugs[bit_idx].append(drug_name)
            for atom_idx, rad in envs:
                env = Chem.FindAtomEnvironmentOfRadiusN(mol, rad, atom_idx)
                if env:
                    submol = Chem.PathToSubmol(mol, env)
                    sma = Chem.MolToSmarts(submol)
                else:
                    sma = mol.GetAtomWithIdx(atom_idx).GetSymbol()
                bit_smarts[bit_idx][sma] = bit_smarts[bit_idx].get(sma, 0) + 1

    n_total = max(1, len([v for v in compound_meta.values() if v.get("smiles")]))
    result: dict[str, dict] = {}
    for bit_idx, smarts_counts in bit_smarts.items():
        top_smarts = max(smarts_counts, key=smarts_counts.get) if smarts_counts else ""
        drugs = bit_drugs.get(bit_idx, [])
        result[f"fp_{bit_idx:04d}"] = {
            "smarts": top_smarts,
            "example_drugs": drugs[:5],
            "n_drugs_with_bit": len(drugs),
            "pct_drugs": len(drugs) / n_total * 100,
        }
    return result


# ---------------------------------------------------------------------------
# Evidence selection and interpretation
# ---------------------------------------------------------------------------

def _pick_top_evidence(evidence: list[dict], n: int) -> list[dict]:
    def score(ev: dict) -> float:
        qy = float(ev["query"]["y_true"])
        neigh = float(ev["response_distribution"]["neighbors"]["weighted_mean"])
        return abs(qy - neigh)

    order = sorted(evidence, key=score, reverse=True)
    return order[: min(n, len(order))]


def _auc_interpretation(y_true: float, nbr_mean: float, global_mean: float) -> str:
    """Qualitative interpretation of AUC relative to neighborhood and global."""
    if y_true > nbr_mean + 5 and y_true > global_mean + 5:
        return "exceptionally resistant (AUC far above both neighborhood and global baselines)"
    if y_true > nbr_mean + 2:
        return "more resistant than similar drug-cell pairs"
    if y_true < nbr_mean - 5 and y_true < global_mean - 5:
        return "exceptionally sensitive (AUC far below both neighborhood and global baselines)"
    if y_true < nbr_mean - 2:
        return "more sensitive than similar drug-cell pairs"
    return "typical response relative to its neighborhood"


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def _feature_line_enriched(feat: dict, fp_info: dict) -> str:
    fname = feat["feature"]
    base = (
        f"**{fname}** ({feat['direction']}; "
        f"z={feat['z_score']:.2f}, "
        f"neighborhood={feat['neighborhood_mean']:.3f} vs global={feat['global_mean']:.3f})"
    )
    info = fp_info.get(fname)
    if info:
        parts = []
        if info.get("smarts"):
            parts.append(f"SMARTS: `{info['smarts']}`")
        examples = info.get("example_drugs", [])[:3]
        if examples:
            parts.append(f"e.g. {', '.join(examples)}")
        parts.append(f"{info.get('pct_drugs', 0):.0f}% of drugs")
        base += f"  \n  _[{'; '.join(parts)}]_"
    return base


def _render_enriched_report_md(
    ev: dict,
    report_id: str,
    compound_meta: dict,
    cell_meta: dict,
    fp_info: dict,
) -> str:
    eid = ev["evidence_id"]
    q = ev["query"]
    meta = q.get("meta", {})
    cpd_id = meta.get("master_cpd_id")
    ccl_id = meta.get("master_ccl_id")
    drug = _drug_info(cpd_id, compound_meta)
    cell = _cell_info(ccl_id, cell_meta)
    nbr = ev["response_distribution"]["neighbors"]
    glb = ev["response_distribution"]["global"]
    top_feats = ev.get("top_distinguishing_features", [])[:8]
    neighbor_examples = ev.get("neighbor_examples", [])
    drug_name = drug.get("cpd_name", str(cpd_id))
    cell_name = cell.get("ccl_name", str(ccl_id))
    interp = _auc_interpretation(q["y_true"], nbr["weighted_mean"], glb["mean"])

    lines: list[str] = []
    lines.append(f"## {report_id} — {drug_name} on {cell_name}")
    lines.append(f"*Evidence: {eid}*")
    lines.append("")

    # -- Sample Identity --
    lines.append("### Sample Identity")
    lines.append("| Property | Value |")
    lines.append("|----------|-------|")
    lines.append(f"| Drug | **{drug_name}** (master_cpd_id={cpd_id}) |")
    if drug.get("gene_target"):
        lines.append(f"| Gene Target | {drug['gene_target']} |")
    if drug.get("mechanism"):
        lines.append(f"| Mechanism / Activity | {drug['mechanism']} |")
    lines.append(f"| Cell Line | **{cell_name}** (master_ccl_id={ccl_id}) |")
    if cell.get("primary_site"):
        lines.append(f"| Tissue | {cell['primary_site']} |")
    if cell.get("histology"):
        lines.append(f"| Histology | {cell['histology']} |")
    if cell.get("subtype"):
        lines.append(f"| Subtype | {cell['subtype']} |")
    lines.append("")

    # -- Response Summary --
    lines.append("### Response Summary")
    lines.append(
        f"- [{eid}] **{drug_name}** on **{cell_name}**: observed AUC = **{q['y_true']:.4f}**"
    )
    lines.append(
        f"- [{eid}] Kernel neighborhood weighted AUC = **{nbr['weighted_mean']:.4f}** "
        f"(median={nbr['q50']:.4f}, q10={nbr['q10']:.4f}, q90={nbr['q90']:.4f})"
    )
    lines.append(
        f"- [{eid}] Global baseline AUC = {glb['mean']:.4f} (median={glb['q50']:.4f})"
    )
    lines.append(f"- [{eid}] **Interpretation**: {interp}")
    lines.append("")

    # -- Distinguishing Features --
    lines.append("### Distinguishing Molecular Features")
    for i, feat in enumerate(top_feats, 1):
        lines.append(f"{i}. {_feature_line_enriched(feat, fp_info)}")
    lines.append("")

    # -- Nearest Neighbors --
    if neighbor_examples:
        lines.append("### Nearest Neighbors")
        lines.append("| Drug | Cell Line | Tissue | AUC | Kernel Score |")
        lines.append("|------|-----------|--------|-----|-------------|")
        for ne in neighbor_examples:
            ne_meta = ne.get("meta", {})
            ne_drug = _drug_info(ne_meta.get("master_cpd_id"), compound_meta)
            ne_cell = _cell_info(ne_meta.get("master_ccl_id"), cell_meta)
            lines.append(
                f"| {ne_drug.get('cpd_name', '?')} "
                f"| {ne_cell.get('ccl_name', '?')} "
                f"| {ne_cell.get('primary_site', '')} "
                f"| {ne.get('y', 0):.4f} "
                f"| {ne.get('kernel_score', 0):.4f} |"
            )
        lines.append("")

    # -- Constraints --
    lines.append("### Scope and Constraints")
    lines.append(
        f"- [{eid}] Interpretation constrained to leaf-agreement "
        f"neighbors (top_k={ev['kernel']['top_k']})."
    )
    lines.append(
        f"- [{eid}] Statements are grounded in this evidence entry "
        f"only and do not imply causality."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Enriched JSONL payload
# ---------------------------------------------------------------------------

def _build_enriched_payload(
    ev: dict,
    report_id: str,
    compound_meta: dict,
    cell_meta: dict,
    fp_info: dict,
) -> dict:
    q = ev["query"]
    meta = q.get("meta", {})
    cpd_id = meta.get("master_cpd_id")
    ccl_id = meta.get("master_ccl_id")
    drug = _drug_info(cpd_id, compound_meta)
    cell = _cell_info(ccl_id, cell_meta)
    nbr = ev["response_distribution"]["neighbors"]
    glb = ev["response_distribution"]["global"]

    enriched_features: list[dict] = []
    for feat in ev.get("top_distinguishing_features", [])[:8]:
        ef = dict(feat)
        info = fp_info.get(feat["feature"])
        if info:
            ef["substructure_smarts"] = info.get("smarts", "")
            ef["example_drugs"] = info.get("example_drugs", [])[:3]
            ef["pct_drugs_with_bit"] = round(info.get("pct_drugs", 0), 1)
        enriched_features.append(ef)

    neighbor_details: list[dict] = []
    for ne in ev.get("neighbor_examples", []):
        ne_meta = ne.get("meta", {})
        ne_drug = _drug_info(ne_meta.get("master_cpd_id"), compound_meta)
        ne_cell = _cell_info(ne_meta.get("master_ccl_id"), cell_meta)
        neighbor_details.append({
            "sample_idx": ne["sample_idx"],
            "kernel_score": ne["kernel_score"],
            "y": ne["y"],
            "drug_name": ne_drug.get("cpd_name", ""),
            "cell_line": ne_cell.get("ccl_name", ""),
            "tissue": ne_cell.get("primary_site", ""),
        })

    return {
        "report_id": report_id,
        "evidence_id": ev["evidence_id"],
        "drug": {
            "master_cpd_id": cpd_id,
            "name": drug.get("cpd_name", ""),
            "gene_target": drug.get("gene_target", ""),
            "mechanism": drug.get("mechanism", ""),
        },
        "cell_line": {
            "master_ccl_id": ccl_id,
            "name": cell.get("ccl_name", ""),
            "tissue": cell.get("primary_site", ""),
            "histology": cell.get("histology", ""),
            "subtype": cell.get("subtype", ""),
        },
        "query_y_true": q["y_true"],
        "neighborhood_y_weighted_mean": nbr["weighted_mean"],
        "abs_gap": abs(q["y_true"] - nbr["weighted_mean"]),
        "interpretation": _auc_interpretation(
            q["y_true"], nbr["weighted_mean"], glb["mean"]
        ),
        "enriched_features": enriched_features,
        "neighbor_details": neighbor_details,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate enriched grounded reports from evidence.jsonl."
    )
    parser.add_argument("--evidence", default="results/dem/evidence.jsonl")
    parser.add_argument(
        "--compound-meta",
        default="data/CTRPv2/v21.meta.per_compound.txt",
    )
    parser.add_argument(
        "--cell-meta",
        default="data/CTRPv2/v21.meta.per_cell_line.txt",
    )
    parser.add_argument("--out-md", default="results/dem/sample_reports.md")
    parser.add_argument("--out-jsonl", default="results/dem/sample_reports.jsonl")
    parser.add_argument("--num-reports", type=int, default=5)
    parser.add_argument("--morgan-bits", type=int, default=1024)
    parser.add_argument("--morgan-radius", type=int, default=2)
    args = parser.parse_args()

    evidence_path = Path(args.evidence).resolve()
    out_md = Path(args.out_md).resolve()
    out_jsonl = Path(args.out_jsonl).resolve()
    out_md.parent.mkdir(parents=True, exist_ok=True)

    print("Loading compound metadata...")
    compound_meta = _load_compound_meta(Path(args.compound_meta))
    print(f"  {len(compound_meta)} compounds loaded.")

    print("Loading cell line metadata...")
    cell_meta = _load_cell_meta(Path(args.cell_meta))
    print(f"  {len(cell_meta)} cell lines loaded.")

    print("Decoding Morgan fingerprint bits from SMILES...")
    fp_info = _build_fp_bit_descriptions(
        compound_meta, n_bits=args.morgan_bits, radius=args.morgan_radius
    )
    print(f"  {len(fp_info)} fingerprint bits decoded.")

    print("Loading evidence...")
    evidence = _load_jsonl(evidence_path)
    if not evidence:
        raise ValueError(f"No evidence rows found in {evidence_path}")

    chosen = _pick_top_evidence(evidence, args.num_reports)
    print(f"Generating {len(chosen)} reports from {len(evidence)} evidence entries...")

    md_parts = ["# Enriched Grounded Reports", ""]
    with out_jsonl.open("w", encoding="utf-8") as f:
        for i, ev in enumerate(chosen, start=1):
            report_id = f"RPT-{i:04d}"
            payload = _build_enriched_payload(
                ev, report_id, compound_meta, cell_meta, fp_info
            )
            f.write(json.dumps(payload, ensure_ascii=True) + "\n")
            md_parts.append(
                _render_enriched_report_md(
                    ev, report_id, compound_meta, cell_meta, fp_info
                )
            )

    out_md.write_text("\n".join(md_parts), encoding="utf-8")
    print(f"Wrote: {out_md}")
    print(f"Wrote: {out_jsonl}")


if __name__ == "__main__":
    main()
