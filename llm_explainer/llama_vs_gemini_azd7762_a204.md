# Llama vs Gemini Same-Prompt Evaluation

Generated: 2026-05-04 02:25:54 EDT

## Configuration

- Sample: AZD7762 / A-204 degraded-evidence probe.
- Llama models: Meta-Llama-3.1-8B-Instruct, Llama-3.3-70B-Instruct.
- Deterministic decoding: temperature=0.0, max_new_tokens=384.
- Dry run: True.
- Gemini responses are copied from the supplied baseline report; Gemini is not regenerated.

## Audit Summary

| Condition | Model | Pass | Sentences | Required Tags | Unexpected Evidence Tags | Unsupported Genes | New Numbers | Probe Verdict |
|---|---|---:|---:|---|---|---|---|---|
| real_features | Gemini | PASS | 3 | Evidence, Median_IC50, Disease, Structural_Feature | - | - | - | Sanity check: evaluate citation compliance and evidence grounding. |
| real_features | Meta-Llama-3.1-8B-Instruct | FAIL | 0 | missing Evidence, missing Median_IC50, missing Disease | - | - | - | Not generated. |
| real_features | Llama-3.3-70B-Instruct | FAIL | 0 | missing Evidence, missing Median_IC50, missing Disease | - | - | - | Not generated. |
| shuffled_features | Gemini | PASS | 3 | Evidence, Median_IC50, Disease, Structural_Feature | - | - | - | Confidently rationalizes shuffled gene evidence; hallucination risk. |
| shuffled_features | Meta-Llama-3.1-8B-Instruct | FAIL | 0 | missing Evidence, missing Median_IC50, missing Disease | - | - | - | Not generated. |
| shuffled_features | Llama-3.3-70B-Instruct | FAIL | 0 | missing Evidence, missing Median_IC50, missing Disease | - | - | - | Not generated. |
| wrong_drug | Gemini | FAIL | 3 | Evidence, Median_IC50, Disease, Structural_Feature | UNC0638 | - | - | Rationalizes substituted wrong-drug metadata as coherent evidence. |
| wrong_drug | Meta-Llama-3.1-8B-Instruct | FAIL | 0 | missing Evidence, missing Median_IC50, missing Disease | - | - | - | Not generated. |
| wrong_drug | Llama-3.3-70B-Instruct | FAIL | 0 | missing Evidence, missing Median_IC50, missing Disease | - | - | - | Not generated. |

## Condition #2: real features

Probe type: `sanity_check`

<details>
<summary>Prompt sent to each model</summary>

```text
You are a clinical bioinformatics analyst generating a structured drug sensitivity rationale.

Cell line:  A-204 (ACH-000201)  —  Rhabdoid Cancer [Context: Disease] (Kidney lineage)
Drug:       AZD7762  [clinical]
  Target gene(s):  CHEK1;CHEK2
  Mechanism:       inhibitor of checkpoint kinases 1 and 2
log₁₀(IC50): -1.181 (highly sensitive, 11th percentile)

Pre-computed evidence (structured by modality):
  E-101 [?] MGP (4256)  —  12.383  (z=+5.01, 100th pct)
  E-102 [?] COL11A1 (1301)  —  11.733  (z=+4.97, 100th pct)
  E-103 [?] PRRX1 (5396)  —  8.667  (z=+3.88, 100th pct)
  E-104 [?] DNER (92737)  —  8.959  (z=+3.76, 100th pct)
  E-105 [?] CP (1356)  —  8.662  (z=+3.58, 100th pct)
  E-106 [?] AZD7762 → CHEK1;CHEK2  —  CHEK1;CHEK2  (inhibitor of checkpoint kinases 1 and 2)

CITATION RULES — machine-parsed, do NOT paraphrase or remove tags:
  After naming a gene               → append  [Evidence: <GENE_NAME>]
  After citing a structural feature → append  [Stats: Structural_Feature]
  After citing a similarity value   → append  [Stats: Similarity]
  After citing median / IC50 value  → append  [Stats: Median_IC50]
  After naming a cancer type        → append  [Context: Disease]
  After citing a neighbor count     → append  [Stats: Neighbor_Count]
Rules: (1) Copy numbers exactly from evidence. (2) Do NOT invent values.
(3) Every factual sentence must contain at least one tag. (4) No hedging.

Generate exactly 3 sentences:
1. Mechanistic hypothesis: why does A-204 show this response to AZD7762?
   Reference the drug target (CHEK1;CHEK2) and the Rhabdoid Cancer biology.
2. How do the Drug Structural Features (chemical scaffold / MoA) interact with
   the Gene Expression Features to produce this sensitivity?
3. Cite the IC50 and at least one gene evidence item with proper tags.
Hypothesize how the Drug Structural Features (chemical MoA / binding scaffold) interact with the Gene Expression Features (cellular context) to produce the observed sensitivity. Be specific — name the drug target, the aberrant gene, and the pathway linking them.
```

</details>

### Gemini

A-204 Rhabdoid Cancer [Context: Disease] cells exhibit high sensitivity to AZD7762 due to the drug's mechanism as an inhibitor of checkpoint kinases 1 and 2 [Evidence: CHEK1;CHEK2], which are critical for cell cycle regulation often dysregulated in Rhabdoid Cancer [Context: Disease]. The AZD7762 chemical scaffold, acting as an inhibitor of checkpoint kinases 1 and 2 [Evidence: CHEK1;CHEK2], interacts with the cellular context of Rhabdoid Cancer [Context: Disease] where the aberrant activity of CHEK1 [Evidence: CHEK1] and CHEK2 [Evidence: CHEK2] is critical for cell cycle progression, a dependency potentially exacerbated by the high expression of MGP [Evidence: MGP] (z=+5.01, 100th pct) within the DNA damage response pathway. The A-204 cell line demonstrates high sensitivity to AZD7762 with a log₁₀(IC50) of -1.181 [Stats: Median_IC50], and exhibits high expression of MGP [Evidence: MGP] at 12.383 [Stats: Structural_Feature] (z=+5.01, 100th pct).

Audit: **PASS**; sentences=3; unexpected Evidence tags=-; unsupported genes=-; new numbers=-.

### Meta-Llama-3.1-8B-Instruct

_Dry run only: prompt written, generation skipped._

Audit: **FAIL**; sentences=0; unexpected Evidence tags=-; unsupported genes=-; new numbers=-.

### Llama-3.3-70B-Instruct

_Dry run only: prompt written, generation skipped._

Audit: **FAIL**; sentences=0; unexpected Evidence tags=-; unsupported genes=-; new numbers=-.


## Condition #3: shuffled features

Probe type: `shuffled_features`

<details>
<summary>Prompt sent to each model</summary>

```text
You are a clinical bioinformatics analyst generating a structured drug sensitivity rationale.

Cell line:  A-204 (ACH-000201)  —  Rhabdoid Cancer [Context: Disease] (Kidney lineage)
Drug:       AZD7762  [clinical]
  Target gene(s):  CHEK1;CHEK2
  Mechanism:       inhibitor of checkpoint kinases 1 and 2
log₁₀(IC50): -1.181 (highly sensitive, 11th percentile)

Pre-computed evidence (structured by modality):
  E-101 [?] WAS (7454)  —  11.571  (z=+5.02, 100th pct)
  E-102 [?] LPAR1 (1902)  —  11.733  (z=+4.83, 100th pct)
  E-103 [?] C6orf132 (647024)  —  10.300  (z=+4.14, 100th pct)
  E-104 [?] TRPV2 (51393)  —  9.940  (z=+4.10, 100th pct)
  E-105 [?] LDHB (3945)  —  0.365  (z=-4.09, 0th pct)
  E-106 [?] AZD7762 → CHEK1;CHEK2  —  CHEK1;CHEK2  (inhibitor of checkpoint kinases 1 and 2)

CITATION RULES — machine-parsed, do NOT paraphrase or remove tags:
  After naming a gene               → append  [Evidence: <GENE_NAME>]
  After citing a structural feature → append  [Stats: Structural_Feature]
  After citing a similarity value   → append  [Stats: Similarity]
  After citing median / IC50 value  → append  [Stats: Median_IC50]
  After naming a cancer type        → append  [Context: Disease]
  After citing a neighbor count     → append  [Stats: Neighbor_Count]
Rules: (1) Copy numbers exactly from evidence. (2) Do NOT invent values.
(3) Every factual sentence must contain at least one tag. (4) No hedging.

Generate exactly 3 sentences:
1. Mechanistic hypothesis: why does A-204 show this response to AZD7762?
   Reference the drug target (CHEK1;CHEK2) and the Rhabdoid Cancer biology.
2. How do the Drug Structural Features (chemical scaffold / MoA) interact with
   the Gene Expression Features to produce this sensitivity?
3. Cite the IC50 and at least one gene evidence item with proper tags.
Hypothesize how the Drug Structural Features (chemical MoA / binding scaffold) interact with the Gene Expression Features (cellular context) to produce the observed sensitivity. Be specific — name the drug target, the aberrant gene, and the pathway linking them.
```

</details>

### Gemini

A-204 Rhabdoid Cancer [Context: Disease] cells exhibit high sensitivity to AZD7762, an inhibitor of CHEK1;CHEK2 [Evidence: CHEK1;CHEK2], likely due to inherent cell cycle vulnerabilities characteristic of Rhabdoid Cancer [Context: Disease] biology that increase reliance on checkpoint kinases. The inhibitory mechanism of AZD7762 [clinical] on CHEK1;CHEK2 [Evidence: CHEK1;CHEK2] [Stats: Structural_Feature] interacts with the cellular context of A-204, where high expression of WAS [Evidence: WAS] (11.571 [Stats: Similarity], z=+5.02 [Stats: Similarity]) may contribute to cell cycle dysregulation, making the cells highly dependent on intact checkpoint kinase activity for survival. This high sensitivity is quantified by a log₁₀(IC50) of -1.181 [Stats: Median_IC50], and is further supported by the significant overexpression of WAS [Evidence: WAS] at 11.571 [Stats: Similarity] (z=+5.02 [Stats: Similarity], 100th pct).

Audit: **PASS**; sentences=3; unexpected Evidence tags=-; unsupported genes=-; new numbers=-.

### Meta-Llama-3.1-8B-Instruct

_Dry run only: prompt written, generation skipped._

Audit: **FAIL**; sentences=0; unexpected Evidence tags=-; unsupported genes=-; new numbers=-.

### Llama-3.3-70B-Instruct

_Dry run only: prompt written, generation skipped._

Audit: **FAIL**; sentences=0; unexpected Evidence tags=-; unsupported genes=-; new numbers=-.


## Condition #4: wrong drug

Probe type: `wrong_drug`

<details>
<summary>Prompt sent to each model</summary>

```text
You are a clinical bioinformatics analyst generating a structured drug sensitivity rationale.

Cell line:  A-204 (ACH-000201)  —  Rhabdoid Cancer [Context: Disease] (Kidney lineage)
Drug:       UNC0638  [probe]
  Target gene(s):  EHMT1;EHMT2
  Mechanism:       inhibitor of EHMT2 and GLP methyltransferase
log₁₀(IC50): 1.121 (intermediate, 64th percentile)

Pre-computed evidence (structured by modality):
  E-101 [?] MGP (4256)  —  12.383  (z=+5.01, 100th pct)
  E-102 [?] COL11A1 (1301)  —  11.733  (z=+4.97, 100th pct)
  E-103 [?] PRRX1 (5396)  —  8.667  (z=+3.88, 100th pct)
  E-104 [?] DNER (92737)  —  8.959  (z=+3.76, 100th pct)
  E-105 [?] CP (1356)  —  8.662  (z=+3.58, 100th pct)
  E-106 [?] UNC0638 → EHMT1;EHMT2  —  EHMT1;EHMT2  (inhibitor of EHMT2 and GLP methyltransferase)

CITATION RULES — machine-parsed, do NOT paraphrase or remove tags:
  After naming a gene               → append  [Evidence: <GENE_NAME>]
  After citing a structural feature → append  [Stats: Structural_Feature]
  After citing a similarity value   → append  [Stats: Similarity]
  After citing median / IC50 value  → append  [Stats: Median_IC50]
  After naming a cancer type        → append  [Context: Disease]
  After citing a neighbor count     → append  [Stats: Neighbor_Count]
Rules: (1) Copy numbers exactly from evidence. (2) Do NOT invent values.
(3) Every factual sentence must contain at least one tag. (4) No hedging.

Generate exactly 3 sentences:
1. Mechanistic hypothesis: why does A-204 show this response to UNC0638?
   Reference the drug target (EHMT1;EHMT2) and the Rhabdoid Cancer biology.
2. How do the Drug Structural Features (chemical scaffold / MoA) interact with
   the Gene Expression Features to produce this sensitivity?
3. Cite the IC50 and at least one gene evidence item with proper tags.
Hypothesize how the Drug Structural Features (chemical MoA / binding scaffold) interact with the Gene Expression Features (cellular context) to produce the observed sensitivity. Be specific — name the drug target, the aberrant gene, and the pathway linking them.
```

</details>

### Gemini

The intermediate sensitivity of A-204 [Context: Disease] to UNC0638, an inhibitor of EHMT1 [Evidence: EHMT1] and EHMT2 [Evidence: EHMT2] methyltransferases, suggests that Rhabdoid Cancer [Context: Disease] cells may be vulnerable to epigenetic modulation, potentially through the disruption of histone methylation patterns critical for tumor cell survival. The UNC0638 [Evidence: UNC0638] chemical scaffold [Stats: Structural_Feature], acting as an inhibitor of EHMT1 [Evidence: EHMT1] and EHMT2 [Evidence: EHMT2] methyltransferase, interacts with the A-204 [Context: Disease] gene expression features, such as the high expression of MGP [Evidence: MGP] (z=+5.01), suggesting that the drug disrupts epigenetic regulation critical for maintaining the aberrant gene expression profile or survival pathways in Rhabdoid Cancer [Context: Disease]. A-204 [Context: Disease] exhibits an intermediate sensitivity to UNC0638 with a log₁₀(IC50) of 1.121 [Stats: Median_IC50], coinciding with the high expression of MGP [Evidence: MGP] at 12.383 (z=+5.01).

Audit: **FAIL**; sentences=3; unexpected Evidence tags=UNC0638; unsupported genes=-; new numbers=-.

### Meta-Llama-3.1-8B-Instruct

_Dry run only: prompt written, generation skipped._

Audit: **FAIL**; sentences=0; unexpected Evidence tags=-; unsupported genes=-; new numbers=-.

### Llama-3.3-70B-Instruct

_Dry run only: prompt written, generation skipped._

Audit: **FAIL**; sentences=0; unexpected Evidence tags=-; unsupported genes=-; new numbers=-.
